---
type: dashboard
dashboard: Performance
---

# Performance Dashboard

> **Folder mapping**
> - Trade notes: `05 - Live Trading Journal/Trades`
> - Mistake database: `06 - Mistake Database`
> - Dashboards: `01 - Dashboard`
>
> Các dashboard này tự đọc trade note ở mọi thư mục con bên dưới `05 - Live Trading Journal/Trades`, ví dụ:
> `05 - Live Trading Journal/Trades/2026/06/17/...`


## Performance Summary

```dataviewjs
const TRADE_FOLDER = '"Trading Journal/05 - Live Trading Journal/Trades"';

function first(t,names){ for(const n of names){ if(t[n]!==undefined&&t[n]!==null&&t[n]!=="") return t[n]; } return null; }
function toText(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.replaceAll("[[","").replaceAll("]]","").trim(); if(v.path) return v.path.split("/").pop().replace(/\.md$/,""); if(v.display) return String(v.display); return String(v); }
function tradeDate(t){ const d=first(t,["date","trade_date","tradeDate"]); if(d?.toISODate) return d.toISODate(); if(d) return String(d).slice(0,10); const m=t.file.name.match(/\d{4}-\d{2}-\d{2}/); if(m) return m[0]; return t.file.cday?.toISODate?.() ?? ""; }
function result(t){ const raw=toText(first(t,["result","outcome","status","exit_reason"])).toLowerCase(); const name=t.file.name.toLowerCase(); if(raw.includes("win")||raw.includes("profit")||raw.includes("take profit")||raw==="tp"||name.includes("win")) return "Win"; if(raw.includes("loss")||raw.includes("stop")||raw.includes("stoploss")||raw.includes("stop loss")||raw==="sl"||name.includes("loss")) return "Loss"; if(raw.includes("be")||raw.includes("break even")||raw.includes("breakeven")) return "BE"; return "Unknown"; }
function num(v){ if(v===null||v===undefined) return null; const m=String(v).replaceAll(",","").replaceAll("−","-").match(/-?\d+(\.\d+)?/); return m ? Number(m[0]) : null; }
function rValue(t){ const explicit=num(first(t,["r_multiple","r","R","rMultiple","r-multiple"])); if(explicit!==null) return explicit; if(result(t)==="Loss") return -1; if(result(t)==="Win") return 1; return 0; }
function symbol(t){ return toText(first(t,["symbol","ticker","pair","instrument"])) || "Unknown"; }

const trades = dv.pages(TRADE_FOLDER)
  .where(t => t.file && !String(t.file.path).includes("Template"))
  .array()
  .sort((a,b)=>tradeDate(a).localeCompare(tradeDate(b)));

const wins=trades.filter(t=>result(t)==="Win");
const losses=trades.filter(t=>result(t)==="Loss");
const totalR=trades.reduce((s,t)=>s+rValue(t),0);
const avgR=trades.length ? totalR/trades.length : 0;
const avgWin=wins.length ? wins.reduce((s,t)=>s+rValue(t),0)/wins.length : 0;
const avgLoss=losses.length ? losses.reduce((s,t)=>s+rValue(t),0)/losses.length : 0;
const winrate=(wins.length+losses.length) ? wins.length/(wins.length+losses.length)*100 : 0;

let html=`
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:16px 0;">
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Total trades</div><div style="font-size:28px;font-weight:700;">${trades.length}</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Winrate</div><div style="font-size:28px;font-weight:700;">${winrate.toFixed(1)}%</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Total R</div><div style="font-size:28px;font-weight:700;">${totalR.toFixed(2)}R</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Expectancy</div><div style="font-size:28px;font-weight:700;">${avgR.toFixed(2)}R</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Average win</div><div style="font-size:28px;font-weight:700;">${avgWin.toFixed(2)}R</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Average loss</div><div style="font-size:28px;font-weight:700;">${avgLoss.toFixed(2)}R</div></div>
</div>`;

let cumulativeR=0;
const data=trades.map((t,i)=>{ cumulativeR+=rValue(t); return {index:i+1,date:tradeDate(t),trade:t.file.name,r:cumulativeR}; });
if(data.length){
  const width=900,height=340,pad=50;
  const minR=Math.min(0,...data.map(d=>d.r)), maxR=Math.max(0,...data.map(d=>d.r)), range=maxR-minR||1;
  const xStep=data.length<=1?0:(width-pad*2)/(data.length-1);
  const points=data.map((d,i)=>({ ...d, x:pad+i*xStep, y:height-pad-((d.r-minR)/range)*(height-pad*2) }));
  const zeroY=height-pad-((0-minR)/range)*(height-pad*2);
  const path=points.map((p,i)=>`${i===0?"M":"L"} ${p.x} ${p.y}`).join(" ");

  html += `<h2>Equity Curve by R</h2><svg width="100%" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">
    <line x1="${pad}" y1="${zeroY}" x2="${width-pad}" y2="${zeroY}" stroke="currentColor" opacity="0.35"/>
    <line x1="${pad}" y1="${pad}" x2="${pad}" y2="${height-pad}" stroke="currentColor" opacity="0.35"/>
    <line x1="${pad}" y1="${height-pad}" x2="${width-pad}" y2="${height-pad}" stroke="currentColor" opacity="0.35"/>
    <path d="${path}" fill="none" stroke="currentColor" stroke-width="2.5"/>`;
  points.forEach(p=>{ html += `<circle cx="${p.x}" cy="${p.y}" r="4" fill="currentColor"></circle><text x="${p.x-14}" y="${p.y-10}" font-size="11">${p.r.toFixed(1)}R</text>`; });
  html += `<text x="${pad}" y="${height-12}" font-size="11" opacity="0.75">Nếu chưa có r_multiple, dashboard tạm tính Loss=-1R, Win=+1R.</text></svg>`;
}

dv.container.innerHTML = html;

const groups={};
for(const t of trades){
  const s=symbol(t);
  groups[s]=groups[s]??{count:0,wins:0,losses:0,totalR:0};
  groups[s].count++;
  groups[s].totalR+=rValue(t);
  if(result(t)==="Win") groups[s].wins++;
  if(result(t)==="Loss") groups[s].losses++;
}
const rows=Object.entries(groups).map(([s,g])=>({symbol:s,count:g.count,winrate:(g.wins+g.losses)?g.wins/(g.wins+g.losses)*100:0,totalR:g.totalR,avgR:g.count?g.totalR/g.count:0})).sort((a,b)=>b.totalR-a.totalR);

dv.header(2,"Performance by Symbol");
dv.table(["Symbol","Trades","Winrate","Total R","Avg R"], rows.map(r=>[r.symbol,r.count,`${r.winrate.toFixed(1)}%`,`${r.totalR.toFixed(2)}R`,`${r.avgR.toFixed(2)}R`]));
```
