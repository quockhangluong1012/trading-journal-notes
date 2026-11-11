---
type: dashboard
dashboard: Goals
---

# 🎯 Bảng Điều Khiển Mục Tiêu

> **Bản đồ thư mục**
> - Mục tiêu: `09 - Goal Tracking/Goals/{Long Term, Mid Term, Short Term}`
> - Lộ trình: [[01 - Roadmap]] · Chỉ số: [[02 - Skill Metrics]]
>
> Mỗi mục tiêu là 1 note. Cột mốc (milestones) là các checkbox dưới mục `## Cột mốc`. Dashboard tự đếm số cột mốc đã hoàn thành để tính tiến độ.

## Tổng quan

```dataviewjs
const GOAL_FOLDER = '"09 - Goal Tracking/Goals"';

function txt(v){ if(v===null||v===undefined) return ""; if(typeof v==="string") return v.trim(); return String(v); }
function num(v){ const m=String(v??"").match(/-?\d+(\.\d+)?/); return m?Number(m[0]):0; }
function horizon(g){ const h=txt(g.horizon).toLowerCase(); if(h.startsWith("l")) return "Long"; if(h.startsWith("m")) return "Mid"; if(h.startsWith("s")) return "Short"; return "Unsorted"; }

// Hiển thị tiếng Việt cho trạng thái & nhóm phân loại
const STATUS_VI = {"In Progress":"Đang làm","Done":"Hoàn thành","Not Started":"Chưa bắt đầu","On Hold":"Tạm dừng"};
const CAT_VI = {"Process":"Quy trình","Skill":"Kỹ năng","Consistency":"Ổn định","Mistakes":"Lỗi","Backtest":"Backtest","Discipline":"Kỷ luật"};
function statusRaw(g){ return txt(g.status) || "Not Started"; }
function statusVi(g){ const s=statusRaw(g); return STATUS_VI[s] || s; }
function catVi(g){ const c=txt(g.category); return CAT_VI[c] || c; }
function dueDate(g){ const d=g.due_date; if(d?.toISODate) return d.toISODate(); return txt(d).slice(0,10); }

// Cột mốc = checkbox dưới heading "Cột mốc"
function milestones(g){
  const tasks = (g.file.tasks ?? []).array ? g.file.tasks.array() : (g.file.tasks ?? []);
  return tasks.filter(t => txt(t.section?.subpath).toLowerCase().includes("cột mốc"));
}
function msStats(g){
  const m = milestones(g);
  const done = m.filter(t=>t.completed).length;
  return { done, total: m.length };
}
// Tiến độ = tỷ lệ cột mốc hoàn thành; nếu chưa có cột mốc thì dùng field "progress"
function progress(g){
  const m = msStats(g);
  if(m.total>0) return Math.round(m.done/m.total*100);
  return num(g.progress);
}

const goals = dv.pages(GOAL_FOLDER)
  .where(g => g.file && g.type==="goal" && !String(g.file.path).includes("Template"))
  .array();

const total = goals.length;
const inProgress = goals.filter(g=>statusRaw(g)==="In Progress").length;
const done = goals.filter(g=>statusRaw(g)==="Done").length;
const avgProgress = total ? Math.round(goals.reduce((s,g)=>s+progress(g),0)/total) : 0;
const allMs = goals.reduce((a,g)=>{const m=msStats(g);a.done+=m.done;a.total+=m.total;return a;},{done:0,total:0});

function card(label,value){ return `<div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">${label}</div><div style="font-size:28px;font-weight:700;">${value}</div></div>`; }

dv.container.innerHTML = `
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:16px 0;">
  ${card("Tổng mục tiêu", total)}
  ${card("Đang làm", inProgress)}
  ${card("Hoàn thành", done)}
  ${card("Tiến độ TB", avgProgress + "%")}
  ${card("Cột mốc", allMs.done + " / " + allMs.total)}
</div>`;

function bar(pct){
  const c = pct>=100 ? "var(--color-green,#3ba55d)" : pct>=50 ? "var(--color-yellow,#d4a72c)" : "var(--color-red,#d64545)";
  return `<div style="background:var(--background-modifier-border);border-radius:6px;height:10px;width:120px;overflow:hidden;display:inline-block;vertical-align:middle;"><div style="height:100%;width:${pct}%;background:${c};"></div></div> <span style="font-size:12px;">${pct}%</span>`;
}

const order = {"Long":0,"Mid":1,"Short":2,"Unsorted":3};
const titles = {"Long":"🪐 Dài hạn (1–3 năm)","Mid":"🌗 Trung hạn (6–12 tháng)","Short":"⚡ Ngắn hạn (3–6 tháng)","Unsorted":"❓ Chưa phân loại"};

const groups = {};
for(const g of goals){ const h=horizon(g); (groups[h]=groups[h]||[]).push(g); }

for(const h of Object.keys(groups).sort((a,b)=>order[a]-order[b])){
  dv.header(2, titles[h]);
  const rows = groups[h]
    .sort((a,b)=>progress(b)-progress(a))
    .map(g=>{
      const m=msStats(g);
      return [ g.file.link, catVi(g), statusVi(g), bar(progress(g)),
               `${m.done}/${m.total}`, dueDate(g) ];
    });
  dv.table(["Mục tiêu","Phân loại","Trạng thái","Tiến độ","Cột mốc","Hạn"], rows);
}
```

## Cột mốc còn dang dở

```dataview
TASK
FROM "09 - Goal Tracking/Goals"
WHERE !completed AND contains(meta(section).subpath, "Cột mốc")
GROUP BY file.link
```

## Ghi chú

- Tiến độ được tính từ tỷ lệ cột mốc hoàn thành. Nếu một mục tiêu chưa có cột mốc nào, dashboard dùng field `progress` trong frontmatter.
- Tạo mục tiêu mới: copy [[Goal_Template]] vào đúng thư mục theo kỳ hạn (`Long Term` / `Mid Term` / `Short Term`) và đặt `horizon:` cho khớp (`Long` / `Mid` / `Short`).
