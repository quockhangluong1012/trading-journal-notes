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
