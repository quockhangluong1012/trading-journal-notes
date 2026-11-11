---
type: metrics
dashboard: Skill Metrics
---

# 📊 Chỉ Số Kỹ Năng (Skill Metrics)

> 4 chỉ số đo sự tiến bộ về kỹ năng: **Giảm lỗi lặp lại**, **Số lượng backtest**, **Chất lượng quy trình**, và **Kỷ luật**. Hai chỉ số đầu được dashboard tự đọc; hai chỉ số sau được chấm tay mỗi tuần ở bảng bên dưới.

## Tổng quan

```dataviewjs
function clean(p){ return p.where(x=>x.file && !x.file.name.toLowerCase().includes("dashboard") && !x.file.name.toLowerCase().includes("template")); }

const backtests = clean(dv.pages('"04 - Backtesting"')).length;
const mistakeTypes = clean(dv.pages('"06 - Mistake Database"')).length;

function card(label,value,sub){ return `<div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">${label}</div><div style="font-size:28px;font-weight:700;">${value}</div><div style="font-size:11px;opacity:.6;">${sub||""}</div></div>`; }

dv.container.innerHTML = `
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:16px 0;">
  ${card("Backtest đã log", backtests, "mục tiêu 200")}
  ${card("Loại lỗi đang theo dõi", mistakeTypes, "trong Mistake Database")}
  ${card("Mục tiêu chống lỗi", "<2 / 20 trades", "lỗi top 3")}
  ${card("Mục tiêu kỷ luật", "5 ngày/tuần", "ghi nhật ký mỗi ngày")}
</div>`;
```

## Bảng theo dõi hàng tuần

> Mỗi tuần chấm điểm 1–5 cho hai chỉ số chấm tay. **Chất lượng quy trình** = mức độ theo checklist/playbook. **Kỷ luật** = mức độ giữ kế hoạch & quản trị rủi ro. Ghi luôn số backtest trong tuần và số lần mắc lỗi top 3.

| Tuần | Backtest trong tuần | Lỗi top-3 (số lần) | Chất lượng quy trình (1–5) | Kỷ luật (1–5) | Ghi chú |
|---|---:|---:|---:|---:|---|
| 2026-W26 |  |  |  |  | Tuần khởi tạo hệ thống mục tiêu |

## Định nghĩa chỉ số

> [!note] Cách hiểu từng chỉ số
> - **Giảm lỗi lặp lại** — tần suất 3 lỗi hay gặp nhất trên mỗi 20 lệnh. Xu hướng phải giảm. Nguồn: [[02 - Mistake Frequency Dashboard]].
> - **Số lượng backtest** — tổng số note backtest trong `04 - Backtesting`. Mẫu càng lớn, edge càng đáng tin.
> - **Chất lượng quy trình** — % lệnh theo đúng checklist/playbook (chấm tay 1–5 mỗi tuần).
> - **Kỷ luật** — giữ kế hoạch, quản trị rủi ro, ghi nhật ký đều đặn (chấm tay 1–5 mỗi tuần).

## Liên kết
- Dashboard mục tiêu: [[00 - Goal Dashboard]]
- Lộ trình: [[01 - Roadmap]]
- Dashboard lỗi: [[02 - Mistake Frequency Dashboard]]
- Dashboard chất lượng quy trình: [[04 - Process Quality Dashboard]]
