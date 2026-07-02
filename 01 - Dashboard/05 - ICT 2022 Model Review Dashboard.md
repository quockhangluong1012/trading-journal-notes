---
type: dashboard
dashboard: ICT 2022 Model Review
---

# ICT 2022 Model Review Dashboard

> **Folder mapping**
> - Trade notes: `05 - Live Trading Journal/Trades`
> - Mistake database: `06 - Mistake Database`
> - Dashboards: `01 - Dashboard`
>
> Các dashboard này tự đọc trade note ở mọi thư mục con bên dưới `05 - Live Trading Journal/Trades`, ví dụ:
> `05 - Live Trading Journal/Trades/2026/06/17/...`


## FVG Entry With/Without MSS

Dashboard này giúp tách riêng lỗi quan trọng: **vào FVG nhưng chưa có MSS xác nhận**.

```dataviewjs
const TRADE_FOLDER = '"Trading Journal/05 - Live Trading Journal/Trades"';

function first(t,names){ for(const n of names){ if(t[n]!==undefined&&t[n]!==null&&t[n]!=="") return t[n]; } return null; }
function toText(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.replaceAll("[[","").replaceAll("]]","").trim(); if(v.path) return v.path.split("/").pop().replace(/\.md$/,""); if(v.display) return String(v.display); return String(v); }
function toArray(v){ if(v===null||v===undefined) return []; if(Array.isArray(v)) return v; if(v.array) return v.array(); return [v]; }
function tradeDate(t){ const d=first(t,["date","trade_date","tradeDate"]); if(d?.toISODate) return d.toISODate(); if(d) return String(d).slice(0,10); const m=t.file.name.match(/\d{4}-\d{2}-\d{2}/); if(m) return m[0]; return t.file.cday?.toISODate?.() ?? ""; }
function result(t){ const raw=toText(first(t,["result","outcome","status","exit_reason"])).toLowerCase(); const name=t.file.name.toLowerCase(); if(raw.includes("win")||raw.includes("profit")||raw.includes("take profit")||raw==="tp"||name.includes("win")) return "Win"; if(raw.includes("loss")||raw.includes("stop")||raw.includes("stoploss")||raw.includes("stop loss")||raw==="sl"||name.includes("loss")) return "Loss"; if(raw.includes("be")||raw.includes("break even")||raw.includes("breakeven")) return "BE"; return "Unknown"; }
function mistakes(t){ let out=[]; for(const key of ["mistakes","mistake","Mistake","errors","error"]) out.push(...toArray(t[key])); return [...new Set(out.map(toText).filter(Boolean))]; }
function boolFromFields(t,fields){ const v=first(t,fields); if(v===null) return null; if(typeof v==="boolean") return v; const s=String(v).toLowerCase().trim(); if(["true","yes","1","checked","confirmed","valid","pass"].includes(s)) return true; if(["false","no","0","unchecked","invalid","fail"].includes(s)) return false; return null; }
function hasMistake(t,words){ const joined=mistakes(t).join(" | ").toLowerCase(); return words.some(w=>joined.includes(w.toLowerCase())); }
function fvgEntry(t){ const v=boolFromFields(t,["fvg_entry","entry_fvg","entered_fvg"]); if(v!==null) return v; const text=`${toText(first(t,["setup","entry_model","model","entry"]))} ${mistakes(t).join(" ")}`.toLowerCase(); return text.includes("fvg") || text.includes("fair value gap"); }
function mssConfirmed(t){ const v=boolFromFields(t,["mss_confirmed","market_structure_shift_confirmed"]); if(v!==null) return v; if(hasMistake(t,["not have market structure shift","no mss","mss not"])) return false; return null; }

const trades=dv.pages(TRADE_FOLDER).where(t=>t.file&&!String(t.file.path).includes("Template")).array();
const fvgTrades=trades.filter(fvgEntry);

const buckets={"FVG + MSS confirmed":0,"FVG without MSS":0,"FVG + MSS unknown":0};
for(const t of fvgTrades){
  const mss=mssConfirmed(t);
  if(mss===true) buckets["FVG + MSS confirmed"]++;
  else if(mss===false) buckets["FVG without MSS"]++;
  else buckets["FVG + MSS unknown"]++;
}
const data=Object.entries(buckets).map(([name,count])=>({name,count}));

const width=850, barHeight=34, gap=14, labelWidth=260, chartWidth=width-labelWidth-90;
const height=data.length*(barHeight+gap)+34, max=Math.max(1,...data.map(d=>d.count));
let svg=`<svg width="100%" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">`;
data.forEach((d,i)=>{ const y=i*(barHeight+gap)+12; const w=(d.count/max)*chartWidth; svg+=`<text x="0" y="${y+22}" font-size="13">${d.name}</text><rect x="${labelWidth}" y="${y}" width="${w}" height="${barHeight}" rx="7" fill="currentColor" opacity="0.75"></rect><text x="${labelWidth+w+12}" y="${y+22}" font-size="13">${d.count}</text>`; });
svg += `</svg>`;
dv.container.innerHTML = svg;

dv.header(2,"FVG Trades");
dv.table(["Date","Trade","Result","FVG Entry","MSS Confirmed","Mistakes"], fvgTrades.sort((a,b)=>tradeDate(b).localeCompare(tradeDate(a))).map(t=>[tradeDate(t),t.file.link,result(t),fvgEntry(t)?"Yes":"No",mssConfirmed(t)===null?"Unknown":(mssConfirmed(t)?"Yes":"No"),mistakes(t).join(", ")]));
```

## ICT 2022 Checklist Fields nên thêm vào trade note

```yaml
model: ICT 2022
liquidity_sweep_confirmed: true
daily_bias_confirmed: true
in_poi_zone: true
displacement_confirmed: true
fvg_entry: true
mss_confirmed: true
ltf_structure_aligned: true
news_checked: true
```
