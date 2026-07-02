---
type: dashboard
dashboard: Loss Review
---

# Loss Review Dashboard

> **Folder mapping**
> - Trade notes: `05 - Live Trading Journal/Trades`
> - Mistake database: `06 - Mistake Database`
> - Dashboards: `01 - Dashboard`
>
> Các dashboard này tự đọc trade note ở mọi thư mục con bên dưới `05 - Live Trading Journal/Trades`, ví dụ:
> `05 - Live Trading Journal/Trades/2026/06/17/...`


## Loss Summary + Loss by Mistake Chart

```dataviewjs
const TRADE_FOLDER = '"Trading Journal/05 - Live Trading Journal/Trades"';

function first(t, names){ for(const n of names){ if(t[n]!==undefined && t[n]!==null && t[n]!=="") return t[n]; } return null; }
function toText(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.replaceAll("[[","").replaceAll("]]","").trim(); if(v.path) return v.path.split("/").pop().replace(/\.md$/,""); if(v.display) return String(v.display); return String(v); }
function toArray(v){ if(v===null||v===undefined) return []; if(Array.isArray(v)) return v; if(v.array) return v.array(); return [v]; }
function tradeDate(t){ const d=first(t,["date","trade_date","tradeDate"]); if(d?.toISODate) return d.toISODate(); if(d) return String(d).slice(0,10); const m=t.file.name.match(/\d{4}-\d{2}-\d{2}/); if(m) return m[0]; return t.file.cday?.toISODate?.() ?? ""; }
function result(t){ const raw=toText(first(t,["result","outcome","status","exit_reason"])).toLowerCase(); const name=t.file.name.toLowerCase(); if(raw.includes("win")||raw.includes("profit")||raw.includes("take profit")||raw==="tp"||name.includes("win")) return "Win"; if(raw.includes("loss")||raw.includes("stop")||raw.includes("stoploss")||raw.includes("stop loss")||raw==="sl"||name.includes("loss")) return "Loss"; if(raw.includes("be")||raw.includes("break even")||raw.includes("breakeven")) return "BE"; return "Unknown"; }
function num(v){ if(v===null||v===undefined) return null; const m=String(v).replaceAll(",","").replaceAll("−","-").match(/-?\d+(\.\d+)?/); return m ? Number(m[0]) : null; }
function rValue(t){ const explicit=num(first(t,["r_multiple","r","R","rMultiple","r-multiple"])); if(explicit!==null) return explicit; if(result(t)==="Loss") return -1; if(result(t)==="Win") return 1; return 0; }
function mistakes(t){ let out=[]; for(const key of ["mistakes","mistake","Mistake","errors","error"]) out.push(...toArray(t[key])); return [...new Set(out.map(toText).filter(Boolean))]; }
function symbol(t){ return toText(first(t,["symbol","ticker","pair","instrument"])) || "-"; }
function direction(t){ return toText(first(t,["direction","position","side"])) || "-"; }
function setup(t){ return toText(first(t,["setup","model","playbook"])) || "-"; }

const losses = dv.pages(TRADE_FOLDER)
  .where(t => t.file && !String(t.file.path).includes("Template"))
  .where(t => result(t) === "Loss")
  .array()
  .sort((a,b)=>tradeDate(b).localeCompare(tradeDate(a)));

const totalLossR = losses.reduce((sum,t)=>sum+rValue(t),0);
const avgLossR = losses.length ? totalLossR/losses.length : 0;

const counts = {};
for(const t of losses){ for(const m of mistakes(t)) counts[m]=(counts[m]??0)+1; }
const data = Object.entries(counts).map(([label,count])=>({label,count})).sort((a,b)=>b.count-a.count);
const top = data[0];

let html = `
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:12px;margin:16px 0;">
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Total losses</div><div style="font-size:28px;font-weight:700;">${losses.length}</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Total loss R</div><div style="font-size:28px;font-weight:700;">${totalLossR.toFixed(2)}R</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Average loss</div><div style="font-size:28px;font-weight:700;">${avgLossR.toFixed(2)}R</div></div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">Top loss mistake</div><div style="font-size:18px;font-weight:650;">${top ? `${top.label} × ${top.count}` : "No data"}</div></div>
</div>`;

if(data.length){
  const width=920, barHeight=30, gap=12, labelWidth=350, chartWidth=width-labelWidth-90;
  const height=data.length*(barHeight+gap)+34, max=Math.max(...data.map(d=>d.count));
  let svg=`<h2>Loss by Mistake</h2><svg width="100%" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">`;
  data.forEach((d,i)=>{ const y=i*(barHeight+gap)+12; const w=(d.count/max)*chartWidth; svg+=`<text x="0" y="${y+20}" font-size="13">${d.label}</text><rect x="${labelWidth}" y="${y}" width="${w}" height="${barHeight}" rx="7" fill="currentColor" opacity="0.75"></rect><text x="${labelWidth+w+12}" y="${y+20}" font-size="13">${d.count}</text>`; });
  svg+=`</svg>`;
  html += svg;
}

dv.container.innerHTML = html;

dv.header(2, "Loss Trades");
dv.table(
  ["Date","Trade","Symbol","Direction","Setup","R","Mistakes"],
  losses.map(t=>[tradeDate(t), t.file.link, symbol(t), direction(t), setup(t), `${rValue(t).toFixed(2)}R`, mistakes(t).join(", ")])
);
```
