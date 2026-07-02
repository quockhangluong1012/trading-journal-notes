---
type: dashboard
dashboard: Process Quality
---

# Process Quality Dashboard

> **Folder mapping**
> - Trade notes: `05 - Live Trading Journal/Trades`
> - Mistake database: `06 - Mistake Database`
> - Dashboards: `01 - Dashboard`
>
> Các dashboard này tự đọc trade note ở mọi thư mục con bên dưới `05 - Live Trading Journal/Trades`, ví dụ:
> `Trading Journal/05 - Live Trading Journal/Trades/2026/06/17/...`


## Process Violations

```dataviewjs
const TRADE_FOLDER = '"05 - Live Trading Journal/Trades"';

function first(t,names){ for(const n of names){ if(t[n]!==undefined&&t[n]!==null&&t[n]!=="") return t[n]; } return null; }
function toText(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.replaceAll("[[","").replaceAll("]]","").trim(); if(v.path) return v.path.split("/").pop().replace(/\.md$/,""); if(v.display) return String(v.display); return String(v); }
function toArray(v){ if(v===null||v===undefined) return []; if(Array.isArray(v)) return v; if(v.array) return v.array(); return [v]; }
function mistakes(t){ let out=[]; for(const key of ["mistakes","mistake","Mistake","errors","error"]) out.push(...toArray(t[key])); return [...new Set(out.map(toText).filter(Boolean))]; }
function hasAny(text, words){ const s=text.toLowerCase(); return words.some(w=>s.includes(w.toLowerCase())); }

const categories=[
  {name:"No MSS / MSS invalid", patterns:["mss","market structure shift","not have market structure shift"]},
  {name:"Entry before liquidity sweep", patterns:["liquidity sweep","before liquidity","enter before liquidity"]},
  {name:"Wrong daily bias", patterns:["wrong daily bias","daily bias"]},
  {name:"Entry not in POI", patterns:["poi","not in poi","mss not in poi"]},
  {name:"Revenge trading / emotional trade", patterns:["revenge","emotional"]},
  {name:"News not checked", patterns:["news","tin tức"]},
  {name:"FOMO / chasing price", patterns:["fomo","chasing","đuổi giá"]}
];

const trades=dv.pages(TRADE_FOLDER).where(t=>t.file&&!String(t.file.path).includes("Template")).array();
const counts={}, related={};
for(const c of categories){ counts[c.name]=0; related[c.name]=[]; }
for(const t of trades){
  const joined=mistakes(t).join(" | ");
  for(const c of categories){
    if(hasAny(joined,c.patterns)){ counts[c.name]++; related[c.name].push(t.file.link); }
  }
}
const data=Object.entries(counts).filter(([_,count])=>count>0).map(([name,count])=>({name,count})).sort((a,b)=>b.count-a.count);

if(!data.length){
  dv.paragraph("No process violation data found. Add mistake links or boolean checklist fields to your trade notes.");
} else {
  const width=920, barHeight=30, gap=12, labelWidth=340, chartWidth=width-labelWidth-90;
  const height=data.length*(barHeight+gap)+32, max=Math.max(...data.map(d=>d.count));
  let svg=`<svg width="100%" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">`;
  data.forEach((d,i)=>{ const y=i*(barHeight+gap)+12; const w=(d.count/max)*chartWidth; svg+=`<text x="0" y="${y+20}" font-size="13">${d.name}</text><rect x="${labelWidth}" y="${y}" width="${w}" height="${barHeight}" rx="7" fill="currentColor" opacity="0.75"></rect><text x="${labelWidth+w+12}" y="${y+20}" font-size="13">${d.count}</text>`; });
  svg += `</svg>`;
  dv.container.innerHTML = svg;
  dv.header(2,"Violation Details");
  dv.table(["Process Violation","Count","Related Trades"], data.map(d=>[d.name,d.count,related[d.name]]));
}
```

## Checklist Compliance

Các field nên có trong trade note:

```yaml
liquidity_sweep_confirmed: true
daily_bias_confirmed: true
in_poi_zone: true
mss_confirmed: true
news_checked: true
ltf_structure_aligned: true
```

```dataviewjs
const TRADE_FOLDER = '"Trading Journal/05 - Live Trading Journal/Trades"';

function first(t,names){ for(const n of names){ if(t[n]!==undefined&&t[n]!==null&&t[n]!=="") return t[n]; } return null; }
function toText(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.replaceAll("[[","").replaceAll("]]","").trim(); if(v.path) return v.path.split("/").pop().replace(/\.md$/,""); if(v.display) return String(v.display); return String(v); }
function toArray(v){ if(v===null||v===undefined) return []; if(Array.isArray(v)) return v; if(v.array) return v.array(); return [v]; }
function mistakes(t){ let out=[]; for(const key of ["mistakes","mistake","Mistake","errors","error"]) out.push(...toArray(t[key])); return [...new Set(out.map(toText).filter(Boolean))]; }
function inferBoolean(t, fields, negativePatterns){
  const v=first(t,fields);
  if(v!==null){
    if(typeof v==="boolean") return v;
    const s=String(v).toLowerCase().trim();
    if(["true","yes","y","1","checked","confirmed","valid","pass"].includes(s)) return true;
    if(["false","no","n","0","unchecked","invalid","fail"].includes(s)) return false;
  }
  const joined=mistakes(t).join(" | ").toLowerCase();
  if(negativePatterns.some(p=>joined.includes(p.toLowerCase()))) return false;
  return null;
}
const checks=[
  {name:"Liquidity sweep confirmed", fields:["liquidity_sweep_confirmed","liquidity_sweep","sweep_confirmed"], negative:["liquidity sweep","before liquidity"]},
  {name:"Daily bias confirmed", fields:["daily_bias_confirmed","daily_bias_correct","bias_confirmed"], negative:["wrong daily bias"]},
  {name:"Entry in POI zone", fields:["in_poi_zone","entry_in_poi_zone","poi_confirmed"], negative:["not in poi","mss not in poi","poi"]},
  {name:"MSS confirmed", fields:["mss_confirmed","market_structure_shift_confirmed"], negative:["not have market structure shift","no mss","mss"]},
  {name:"News checked", fields:["news_checked","calendar_checked"], negative:["news not checked","không check","tin tức"]},
  {name:"LTF structure aligned", fields:["ltf_structure_aligned","lower_tf_structure_alignment"], negative:["counter ltf","ltf structure","m15/m5"]}
];
const trades=dv.pages(TRADE_FOLDER).where(t=>t.file&&!String(t.file.path).includes("Template")).array();
const rows=checks.map(c=>{
  let pass=0,fail=0,unknown=0;
  for(const t of trades){ const value=inferBoolean(t,c.fields,c.negative); if(value===true) pass++; else if(value===false) fail++; else unknown++; }
  const known=pass+fail, rate=known ? pass/known*100 : 0;
  return [c.name,pass,fail,unknown,known ? `${rate.toFixed(1)}%` : "-"];
});
dv.table(["Checklist Item","Pass","Fail","Unknown","Compliance"], rows);
```
