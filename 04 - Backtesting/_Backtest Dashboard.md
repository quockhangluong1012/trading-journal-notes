---
type: backtest-dashboard
tags: [backtest, dashboard, ICT2022]
---

# 📊 Backtest Dashboard — ICT 2022 Model

> [!tip] Cách dùng
> Mỗi lần backtest, tạo 1 note mới từ template `Backtest templete` và lưu vào folder **04 - Backtesting**. Điền đầy đủ **frontmatter** (result, r_multiple, session, entry_model, bias_correct, grade...). Dashboard này tự động tổng hợp. Cần cài plugin **Dataview** (bật JavaScript Queries trong Settings để chạy phần KPI).

---

## 1. Tổng quan KPI

```dataviewjs
const pages = dv.pages('"04 - Backtesting"').where(p => p.type == "backtest");
const total = pages.length;
const wins = pages.where(p => p.result == "Win").length;
const losses = pages.where(p => p.result == "Loss").length;
const be = pages.where(p => p.result == "BE").length;
const decided = wins + losses;
const winrate = decided ? (wins / decided * 100) : 0;

const rVals = pages.map(p => Number(p.r_multiple)).where(r => !isNaN(r)).array();
const totalR = rVals.reduce((a,b)=>a+b, 0);
const avgR = rVals.length ? totalR / rVals.length : 0;

const winR = pages.where(p => p.result == "Win").map(p => Number(p.r_multiple)).where(r=>!isNaN(r)).array();
const lossR = pages.where(p => p.result == "Loss").map(p => Number(p.r_multiple)).where(r=>!isNaN(r)).array();
const avgWin = winR.length ? winR.reduce((a,b)=>a+b,0)/winR.length : 0;
const avgLoss = lossR.length ? lossR.reduce((a,b)=>a+b,0)/lossR.length : 0;
const winPct = decided ? wins/decided : 0;
const expectancy = (winPct * avgWin) + ((1-winPct) * avgLoss);

const biasOk = pages.where(p => p.bias_correct == "Yes").length;
const biasPct = total ? (biasOk/total*100) : 0;

dv.table(["Chỉ số", "Giá trị"], [
  ["Tổng số backtest", total],
  ["Win / Loss / BE", `${wins} / ${losses} / ${be}`],
  ["Win Rate", winrate.toFixed(1) + "%"],
  ["Tổng R", totalR.toFixed(2) + "R"],
  ["Avg R / trade", avgR.toFixed(2) + "R"],
  ["Avg Win", avgWin.toFixed(2) + "R"],
  ["Avg Loss", avgLoss.toFixed(2) + "R"],
  ["Expectancy / trade", expectancy.toFixed(2) + "R"],
  ["Bias đúng", biasPct.toFixed(1) + "%"],
]);
```

---

## 2. Equity Curve (R cộng dồn)

```dataviewjs
const pages = dv.pages('"04 - Backtesting"')
  .where(p => p.type == "backtest" && p.r_multiple != null)
  .sort(p => p.trade_date, 'asc');

let cum = 0;
const rows = pages.map(p => {
  cum += Number(p.r_multiple) || 0;
  return [p.trade_date, p.file.link, (Number(p.r_multiple)||0).toFixed(2)+"R", cum.toFixed(2)+"R"];
}).array();

dv.table(["Date", "Trade", "R", "Cumulative R"], rows);
```

---

## 3. Tất cả Backtest (mới nhất trước)

```dataview
TABLE WITHOUT ID
  file.link AS "Trade",
  symbol AS "Sym",
  position AS "Pos",
  result AS "Kết quả",
  r_multiple AS "R",
  session AS "Session",
  entry_model AS "Entry Model",
  grade AS "Grade"
FROM "04 - Backtesting"
WHERE type = "backtest"
SORT trade_date DESC
```

---

## 4. Thống kê theo Session

```dataviewjs
const pages = dv.pages('"04 - Backtesting"').where(p => p.type == "backtest");
const groups = {};
for (const p of pages) {
  const s = p.session || "—";
  if (!groups[s]) groups[s] = {n:0, w:0, r:0};
  groups[s].n++;
  if (p.result == "Win") groups[s].w++;
  groups[s].r += Number(p.r_multiple) || 0;
}
const rows = Object.entries(groups).map(([s,g]) => [
  s, g.n, g.w, (g.n ? (g.w/g.n*100).toFixed(0):0)+"%", g.r.toFixed(2)+"R"
]);
dv.table(["Session", "N", "Wins", "Win%", "Tổng R"], rows);
```

---

## 5. Thống kê theo Entry Model

```dataviewjs
const pages = dv.pages('"04 - Backtesting"').where(p => p.type == "backtest");
const groups = {};
for (const p of pages) {
  const s = p.entry_model || "—";
  if (!groups[s]) groups[s] = {n:0, w:0, r:0};
  groups[s].n++;
  if (p.result == "Win") groups[s].w++;
  groups[s].r += Number(p.r_multiple) || 0;
}
const rows = Object.entries(groups).map(([s,g]) => [
  s, g.n, g.w, (g.n ? (g.w/g.n*100).toFixed(0):0)+"%", g.r.toFixed(2)+"R"
]);
dv.table(["Entry Model", "N", "Wins", "Win%", "Tổng R"], rows);
```

---

## 5.1 CE vs Edge Entry — So sánh Expectancy

> [!tip] Mục đích
> So sánh **hai kiểu entry**: `CE` (vào 50% FVG, RR cao nhưng ít khi được fill) và `Edge` (first-touch nửa trên FVG, RR thấp hơn nhưng fill nhiều hơn). Cột **Avg RR-nếu-CE** cho thấy RR bạn *đánh đổi* khi chọn Edge. Sau đủ mẫu, hãy để **Expectancy** làm trọng tài — không phải RR/lệnh.

```dataviewjs
const pages = dv.pages('"04 - Backtesting"').where(p => p.type == "backtest");
const avg = a => a.length ? a.reduce((x,y)=>x+y,0)/a.length : 0;
const groups = {};
for (const p of pages) {
  const k = p.entry_type || "—";
  if (!groups[k]) groups[k] = {n:0, winR:[], lossR:[], rp:[], ce:[]};
  const g = groups[k];
  g.n++;
  const r = Number(p.r_multiple);
  if (p.result == "Win" && !isNaN(r)) g.winR.push(r);
  if (p.result == "Loss" && !isNaN(r)) g.lossR.push(r);
  if (!isNaN(Number(p.r_planned))) g.rp.push(Number(p.r_planned));
  if (!isNaN(Number(p.rr_if_ce))) g.ce.push(Number(p.rr_if_ce));
}
const rows = Object.entries(groups).map(([k,g]) => {
  const w = g.winR.length, l = g.lossR.length;
  const decided = w + l;
  const winPct = decided ? w/decided : 0;
  const exp = (winPct*avg(g.winR)) + ((1-winPct)*avg(g.lossR));
  return [k, g.n, `${w}/${l}`, (winPct*100).toFixed(0)+"%",
          avg(g.rp).toFixed(2)+"R", avg(g.ce).toFixed(2)+"R", exp.toFixed(2)+"R"];
});
dv.table(["Entry Type","N","W / L","Win%","Avg RR thực","Avg RR-nếu-CE","Expectancy"], rows);
```

---

## 6. Setup điểm cao cần học lại (Grade A/B)

```dataview
TABLE WITHOUT ID file.link AS "Trade", result AS "Kết quả", r_multiple AS "R", grade AS "Grade"
FROM "04 - Backtesting"
WHERE type = "backtest" AND (grade = "A" OR grade = "B")
SORT trade_date DESC
```

## 7. Setup điểm thấp cần rút kinh nghiệm (Grade D/F)

```dataview
TABLE WITHOUT ID file.link AS "Trade", result AS "Kết quả", r_multiple AS "R", grade AS "Grade"
FROM "04 - Backtesting"
WHERE type = "backtest" AND (grade = "D" OR grade = "F")
SORT trade_date DESC
```

---

### Liên kết

- Template: [[Backtest templete]]
- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]]
