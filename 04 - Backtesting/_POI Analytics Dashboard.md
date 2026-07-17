---
type: poi-dashboard
tags: [backtest, dashboard, ICT2022, POI]
---

# 🎯 POI Analytics Dashboard — ICT 2022 Model

> [!tip] Cách dùng
> Dashboard này chỉ tổng hợp các backtest tạo từ template **`Backtest template - POI & Step Decision (ICT 2022)`** (những note có `poi_type` là loại POI thật, không phải wikilink model). Lưu note vào folder **04 - Backtesting**, điền đầy đủ frontmatter theo từ vựng chuẩn trong template. Cần plugin **Dataview** (bật JavaScript Queries).
>
> Mục tiêu: trả lời bằng số liệu — *POI nào tôi áp dụng tốt nhất? Vào Edge/CE/OTE cho expectancy cao hơn? Lệnh limit có hay bị bỏ lỡ không? Tôi hay gãy chuỗi ở bước nào?* Cần **≥30 mẫu/nhóm** trước khi tin một kết luận.

> [!warning] Ngưỡng mẫu tối thiểu
> Mọi bảng dưới đây tô đậm ý nghĩa chỉ khi N đủ lớn. Nhóm có **N < 10** → coi là *quan sát sơ bộ*, chưa phải edge. Đừng đổi rule dựa trên 3–4 mẫu.

---

```dataviewjs
// ===== Helpers dùng chung cho toàn bộ dashboard =====
function first(v){
  if (v == null) return null;
  if (Array.isArray(v)) return v.length ? v[0] : null;
  if (typeof v === "object" && v.values) return v.values.length ? v.values[0] : null;
  return v;
}
function S(v){ const f = first(v); return f == null ? null : String(f).trim(); }
function N(v){ const f = first(v); const n = Number(f); return isNaN(n) ? null : n; }
function yes(v){ const s = S(v); return s && s.toLowerCase() === "yes"; }
function avg(a){ return a.length ? a.reduce((x,y)=>x+y,0)/a.length : 0; }
function expectancy(winR, lossR){
  const w = winR.length, l = lossR.length, d = w + l;
  const wp = d ? w/d : 0;
  return (wp*avg(winR)) + ((1-wp)*avg(lossR));
}
// Chỉ lấy backtest có poi_type là loại POI thật (loại bỏ note cũ ghi poi_type = model)
function poiPages(dv){
  return dv.pages('"04 - Backtesting"').where(p => {
    if (p.type !== "backtest") return false;
    const pt = S(p.poi_type);
    if (!pt) return false;
    if (pt.includes("2022 Model") || pt.startsWith("[[")) return false;
    return true;
  });
}
window.__poiHelpers = { first, S, N, yes, avg, expectancy, poiPages };
dv.paragraph("✅ Helpers loaded. Tổng số backtest POI hợp lệ: **" + poiPages(dv).length + "**");
```

---

## 1. POI Type — POI nào tôi áp dụng tốt nhất?

```dataviewjs
const {S,N,expectancy,avg,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const g = {};
for (const p of pages){
  const k = S(p.poi_type) || "—";
  (g[k] ??= {n:0, w:0, l:0, be:0, winR:[], lossR:[], allR:[]});
  const r = N(p.r_multiple), res = (S(p.result)||"").toLowerCase();
  g[k].n++;
  if (res==="win"){ g[k].w++; if(r!=null) g[k].winR.push(r); }
  else if (res==="loss"){ g[k].l++; if(r!=null) g[k].lossR.push(r); }
  else if (res==="be"){ g[k].be++; }
  if (r!=null) g[k].allR.push(r);
}
const rows = Object.entries(g).map(([k,v])=>{
  const dec = v.w+v.l;
  const wr = dec ? (v.w/dec*100) : 0;
  return [k, v.n, `${v.w}/${v.l}/${v.be}`, wr.toFixed(0)+"%",
          avg(v.allR).toFixed(2)+"R", v.allR.reduce((a,b)=>a+b,0).toFixed(1)+"R",
          expectancy(v.winR,v.lossR).toFixed(2)+"R"];
}).sort((a,b)=>parseFloat(b[6])-parseFloat(a[6]));
dv.table(["POI Type","N","W/L/BE","Win%","Avg R","Tổng R","Expectancy"], rows);
```

> [!note] Đọc bảng này thế nào
> Sắp xếp theo **Expectancy** (kỳ vọng R/lệnh) — cao nhất trên cùng. Đây mới là thước đo "POI nào tốt", **không phải** Win% (một POI win 40% nhưng RR cao vẫn có thể lãi hơn POI win 70% RR thấp). Chỉ tin nhóm có N đủ lớn.

---

## 2. POI Rank (thang chất lượng 8.1) — hạng cao có thực sự tốt hơn?

```dataviewjs
const {S,N,expectancy,avg,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const label = {1:"1 · FVG đơn",2:"2 · FVG+OB",3:"3 · Breaker",4:"4 · iFVG",5:"5 · Unicorn"};
const g = {};
for (const p of pages){
  const rk = N(p.poi_rank);
  const k = rk!=null ? (label[rk] || ("Rank "+rk)) : "— (chưa xếp hạng)";
  (g[k] ??= {n:0,w:0,l:0,winR:[],lossR:[],allR:[]});
  const r=N(p.r_multiple), res=(S(p.result)||"").toLowerCase();
  g[k].n++;
  if(res==="win"){g[k].w++; if(r!=null)g[k].winR.push(r);}
  else if(res==="loss"){g[k].l++; if(r!=null)g[k].lossR.push(r);}
  if(r!=null)g[k].allR.push(r);
}
const rows = Object.entries(g).map(([k,v])=>{
  const dec=v.w+v.l, wr=dec?(v.w/dec*100):0;
  return [k, v.n, `${v.w}/${v.l}`, wr.toFixed(0)+"%", avg(v.allR).toFixed(2)+"R", expectancy(v.winR,v.lossR).toFixed(2)+"R"];
}).sort((a,b)=>a[0].localeCompare(b[0]));
dv.table(["POI Rank","N","W/L","Win%","Avg R","Expectancy"], rows);
```

> [!tip] Giả thuyết kiểm định: hạng POI càng cao (Breaker/iFVG/Unicorn) → expectancy càng cao. Nếu dữ liệu của bạn **không** cho thấy điều đó, đừng ép — có thể bạn nhận diện POI hạng cao chưa chuẩn, hoặc POI đơn giản lại hợp phong cách bạn hơn. Để dữ liệu là trọng tài.

---

## 3. Entry Type — vào Edge, CE hay OTE cho kết quả tốt hơn? (kèm fill-rate)

```dataviewjs
const {S,N,expectancy,avg,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const g = {};
for (const p of pages){
  const k = S(p.entry_type) || "—";
  (g[k] ??= {n:0,w:0,l:0,filled:0,partial:0,nofill:0,winR:[],lossR:[],rp:[],ce:[],ote:[]});
  const r=N(p.r_multiple), res=(S(p.result)||"").toLowerCase(), lf=(S(p.limit_filled)||"").toLowerCase();
  g[k].n++;
  if(res==="win"){g[k].w++; if(r!=null)g[k].winR.push(r);}
  else if(res==="loss"){g[k].l++; if(r!=null)g[k].lossR.push(r);}
  if(lf==="yes")g[k].filled++; else if(lf==="partial")g[k].partial++; else if(lf==="no")g[k].nofill++;
  const rp=N(p.r_planned), ce=N(p.rr_if_ce), ote=N(p.rr_if_ote);
  if(rp!=null)g[k].rp.push(rp); if(ce!=null)g[k].ce.push(ce); if(ote!=null)g[k].ote.push(ote);
}
const rows = Object.entries(g).map(([k,v])=>{
  const dec=v.w+v.l, wr=dec?(v.w/dec*100):0;
  const fillAttempts=v.filled+v.partial+v.nofill;
  const fillRate = fillAttempts ? ((v.filled+0.5*v.partial)/fillAttempts*100) : 0;
  return [k, v.n, `${v.w}/${v.l}`, wr.toFixed(0)+"%", fillRate.toFixed(0)+"%",
          avg(v.rp).toFixed(2)+"R", avg(v.ce).toFixed(2)+"R", avg(v.ote).toFixed(2)+"R",
          expectancy(v.winR,v.lossR).toFixed(2)+"R"];
});
dv.table(["Entry Type","N","W/L","Win%","Fill-rate","Avg RR thực","Avg RR-nếu-CE","Avg RR-nếu-OTE","Expectancy"], rows);
```

> [!important] Đọc trade-off Fill-rate ↔ Expectancy
> - **Fill-rate** = tỷ lệ lệnh limit được khớp (Partial tính 0.5). Vào càng sâu (CE/OTE) → RR cao nhưng fill-rate thường thấp hơn (giá không phải lúc nào cũng về tới CE).
> - Câu hỏi thật: *entry type nào cho **expectancy × cơ hội được fill** cao nhất?* Một Edge fill-rate 90% expectancy 0.6R có thể lãi tổng nhiều hơn CE fill-rate 40% expectancy 1.2R. Nhìn cả hai cột cùng lúc.

---

## 4. Fill Depth — giá thường đi sâu bao nhiêu vào FVG?

```dataviewjs
const {S,N,avg,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const win=[], loss=[], all=[];
let filledYes=0, partial=0, no=0, tot=0;
for (const p of pages){
  const d=N(p.fill_depth_pct), res=(S(p.result)||"").toLowerCase(), lf=(S(p.limit_filled)||"").toLowerCase();
  if(d!=null){ all.push(d); if(res==="win")win.push(d); else if(res==="loss")loss.push(d); }
  if(lf){ tot++; if(lf==="yes")filledYes++; else if(lf==="partial")partial++; else if(lf==="no")no++; }
}
dv.table(["Chỉ số","Giá trị"],[
  ["Lệnh có ghi fill_depth", all.length],
  ["Fill depth TB (tất cả)", avg(all).toFixed(0)+"%"],
  ["Fill depth TB (Win)", avg(win).toFixed(0)+"%"],
  ["Fill depth TB (Loss)", avg(loss).toFixed(0)+"%"],
  ["Limit Filled: Yes / Partial / No", `${filledYes} / ${partial} / ${no}`],
  ["Tỷ lệ KHÔNG được fill", tot ? (no/tot*100).toFixed(0)+"%" : "—"],
]);
```

> [!note] Nếu **fill depth TB của Win** thấp hơn hẳn của Loss → có thể lệnh thắng thường được fill nông (giá phản ứng sớm), còn lệnh để giá đi sâu tới mép xa hay là lệnh thua. Gợi ý: cân nhắc vào nông hơn (Edge) hoặc chia lệnh. Cần đủ mẫu.

---

## 5. First Error Step — tôi hay gãy chuỗi ở bước nào? (heatmap)

```dataviewjs
const {S,N,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const order = ["none","bias","draw","sweep","displacement","poi","entry","target"];
const g = {}; for(const s of order) g[s]={n:0,w:0,l:0,be:0,rsum:0};
for (const p of pages){
  let k = S(p.first_error_step);
  k = (k||"").toLowerCase(); if(!order.includes(k)) k = "none";
  const r=N(p.r_multiple), res=(S(p.result)||"").toLowerCase();
  g[k].n++;
  if(res==="win")g[k].w++; else if(res==="loss")g[k].l++; else if(res==="be")g[k].be++;
  if(r!=null)g[k].rsum+=r;
}
const rows = order.filter(s=>g[s].n>0).map(s=>{
  const v=g[s], dec=v.w+v.l, wr=dec?(v.w/dec*100):0;
  return [s==="none"?"none (đủ chuỗi)":s, v.n, `${v.w}/${v.l}/${v.be}`, wr.toFixed(0)+"%", v.rsum.toFixed(1)+"R"];
});
dv.table(["First Error Step","N","W/L/BE","Win%","Tổng R"], rows);
```

```dataviewjs
// Missing step (dùng riêng cho lệnh Loss/BE) — nghi thức Weekly Review
const {S,poiPages} = window.__poiHelpers;
const pages = poiPages(dv).where(p => { const r=(S(p.result)||"").toLowerCase(); return r==="loss"||r==="be"; });
const order=["none","sweep","displacement","retrace","target"];
const c={}; for(const s of order)c[s]=0; let tot=0;
for(const p of pages){ let k=(S(p.missing_step)||"").toLowerCase(); if(!order.includes(k))k="none"; c[k]++; tot++; }
const rows=order.filter(s=>c[s]>0).map(s=>[s, c[s], tot?(c[s]/tot*100).toFixed(0)+"%":"—"]);
dv.header(4, "Missing Step trên các lệnh Loss/BE (N="+tot+")");
dv.table(["Missing Step","Số lần","% lệnh thua"], rows);
```

> [!warning] Nghi thức Weekly Review
> Nếu một `missing_step` chiếm **>40%** lệnh thua → đây là **ưu tiên sửa số 1** tuần kế tiếp. Ghi vào Weekly Review + gắn `[[Mistake - ...]]` tương ứng. (Theo Best Practices của [[01 - ICT 2022 Model]].)

---

## 6. Per-Step Accuracy — độ chính xác từng bước

```dataviewjs
const {S,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const steps = [
  ["1 · Bias","step1_bias_ok"],["2 · Draw","step2_draw_ok"],["3 · Sweep","step3_sweep_ok"],
  ["4 · Displacement/MSS","step4_displacement_ok"],["5 · POI","step5_poi_ok"],
  ["6 · Entry (retrace)","step6_entry_ok"],["7 · Target","step7_target_ok"],
];
const rows = steps.map(([label,key])=>{
  let ok=0, no=0, na=0;
  for(const p of pages){ const v=(S(p[key])||"").toLowerCase();
    if(v==="yes")ok++; else if(v==="no")no++; else if(v==="na")na++; }
  const dec=ok+no; const acc=dec?(ok/dec*100):0;
  return [label, ok, no, na, acc.toFixed(0)+"%"];
}).sort((a,b)=>parseFloat(a[4])-parseFloat(b[4]));
dv.table(["Bước","Đúng","Sai","NA","Độ chính xác"], rows);
```

> [!tip] Bảng này xếp bước **yếu nhất lên đầu** (độ chính xác thấp nhất). Đây là bước cần luyện có mục tiêu — dồn buổi học/backtest vào đúng mắt xích đang gãy nhiều nhất.

---

## 7. Hiệu quả từng Confluence (SCORE 8.4)

```dataviewjs
const {S,N,yes,expectancy,avg,poiPages} = window.__poiHelpers;
const pages = poiPages(dv);
const conf = [
  ["CE∩OTE overlap","ce_ote_overlap"],["SMT confirm","smt_confirm"],["CISD confirm","cisd_confirm"],
  ["In macro time","in_macro_time"],["NWOG/NDOG align","nwog_ndog_align"],
  ["−2SD/ERL target","sd_target_align"],["IDM swept","idm_swept"],
];
const rows = conf.map(([label,key])=>{
  const on={w:[],l:[],n:0}, off={w:[],l:[],n:0};
  for(const p of pages){ const r=N(p.r_multiple), res=(S(p.result)||"").toLowerCase();
    const bucket = yes(p[key]) ? on : off; bucket.n++;
    if(res==="win"&&r!=null)bucket.w.push(r); else if(res==="loss"&&r!=null)bucket.l.push(r); }
  const wr=b=>{const d=b.w.length+b.l.length; return d?(b.w.length/d*100).toFixed(0)+"%":"—";};
  return [label, `${on.n}`, wr(on), expectancy(on.w,on.l).toFixed(2)+"R",
          `${off.n}`, wr(off), expectancy(off.w,off.l).toFixed(2)+"R"];
});
dv.table(["Confluence","N (có)","Win% (có)","Exp (có)","N (không)","Win% (không)","Exp (không)"], rows);
```

> [!important] So sánh cột **"có" vs "không"**: nếu một confluence khi bật (có) cho expectancy cao hơn hẳn khi tắt → nó thực sự tạo edge **trên dữ liệu của bạn**. Nếu chênh lệch không đáng kể (hoặc ngược) → confluence đó có thể chỉ là niềm tin lý thuyết, cân nhắc bỏ khỏi checklist để giảm nhiễu.

---

## 8. Toàn bộ Backtest POI (mới nhất trước)

```dataview
TABLE WITHOUT ID
  file.link AS "Trade",
  poi_type AS "POI",
  poi_rank AS "Rk",
  entry_type AS "Entry",
  limit_filled AS "Fill",
  result AS "KQ",
  r_multiple AS "R",
  first_error_step AS "Err@",
  grade AS "Grade"
FROM "04 - Backtesting"
WHERE type = "backtest" AND poi_type
SORT trade_date DESC
```

---

### Liên kết
- Template: [[Backtest template - POI & Step Decision (ICT 2022)]]
- Dashboard gốc: [[_Backtest Dashboard]]
- Model: [[01 - ICT 2022 Model]]
