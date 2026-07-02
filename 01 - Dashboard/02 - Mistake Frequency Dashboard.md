---
type: dashboard
dashboard: Mistake Frequency
---

# Mistake Frequency Dashboard

> **Folder mapping**
> - Trade notes: `05 - Live Trading Journal/Trades`
> - Mistake database: `06 - Mistake Database`
> - Dashboards: `01 - Dashboard`
>
> Các dashboard này tự đọc trade note ở mọi thư mục con bên dưới `05 - Live Trading Journal/Trades`, ví dụ:
> `05 - Live Trading Journal/Trades/2026/06/17/...`


## Top Mistakes

```dataviewjs
const TRADE_FOLDER = '"Trading Journal/05 - Live Trading Journal/Trades"';

function toText(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.replaceAll("[[","").replaceAll("]]","").trim(); if(v.path) return v.path.split("/").pop().replace(/\.md$/,""); if(v.display) return String(v.display); return String(v); }
function toArray(v){ if(v===null||v===undefined) return []; if(Array.isArray(v)) return v; if(v.array) return v.array(); return [v]; }
function mistakes(t){ let out=[]; for(const key of ["mistakes","mistake","Mistake","errors","error"]) out.push(...toArray(t[key])); return [...new Set(out.map(toText).filter(Boolean))]; }

const trades = dv.pages(TRADE_FOLDER)
  .where(t => t.file && !String(t.file.path).includes("Template"))
  .array();

const counts = {};
const related = {};
for(const t of trades){
  for(const m of mistakes(t)){
    counts[m]=(counts[m]??0)+1;
    related[m]=related[m]??[];
    related[m].push(t.file.link);
  }
}

const data = Object.entries(counts).map(([mistake,count])=>({mistake,count})).sort((a,b)=>b.count-a.count);

if(!data.length){
  dv.paragraph("No mistake data found. Add `mistakes:` or `Mistake:` to your trade notes.");
} else {
  const width=920, barHeight=30, gap=12, labelWidth=350, chartWidth=width-labelWidth-90;
  const height=data.length*(barHeight+gap)+32, max=Math.max(...data.map(d=>d.count));
  let svg=`<svg width="100%" height="${height}" viewBox="0 0 ${width} ${height}" xmlns="http://www.w3.org/2000/svg">`;
  data.forEach((d,i)=>{ const y=i*(barHeight+gap)+12; const w=(d.count/max)*chartWidth; svg+=`<text x="0" y="${y+20}" font-size="13">${d.mistake}</text><rect x="${labelWidth}" y="${y}" width="${w}" height="${barHeight}" rx="7" fill="currentColor" opacity="0.75"></rect><text x="${labelWidth+w+12}" y="${y+20}" font-size="13">${d.count}</text>`; });
  svg += `</svg>`;
  dv.container.innerHTML = svg;

  dv.header(2, "Mistake Table");
  dv.table(["Mistake","Count","Related Trades"], data.map(d=>[d.mistake,d.count,related[d.mistake].slice(0,8)]));
}
```

## Mistake Database

```dataview
TABLE file.mtime AS "Updated"
FROM "Trading Journal/06 - Mistake Database"
SORT file.name ASC
```
