---
type: goal
horizon: Short
category: Mistakes
status: In Progress
priority: High
progress: 20
metric: Tần suất 3 lỗi hay lặp nhất trên mỗi 20 lệnh
baseline: xem Mistake Frequency Dashboard
target: <2 lần trên mỗi 20 lệnh
phase: Phase 1 - Foundation
start_date: 2026-06-23
due_date: 2026-12-23
tags:
  - goal
---

# Cắt giảm 3 lỗi hay lặp lại nhất

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Lỗi
> - **Vì sao quan trọng:** Phần lớn thiệt hại đến từ một nhóm nhỏ lỗi lặp lại. Diệt được top 3 là cách sửa đường cong vốn nhanh nhất. Đây là nguồn của chỉ số Giảm lỗi.
> - **Điều kiện thành công:** 3 lỗi hay lặp nhất, mỗi lỗi xuất hiện dưới 2 lần trên mỗi 20 lệnh.

## Định nghĩa hoàn thành
- [ ] Xác định top 3 lỗi hiện tại từ Mistake Database
- [ ] Viết biện pháp đối phó cụ thể cho từng lỗi
- [ ] Tần suất giảm xuống dưới 2 lần / 20 lệnh cho cả ba lỗi

## Cách đo lường
- **Chỉ số:** Số lần mắc mỗi lỗi top-3 trên mỗi 20 lệnh (cuốn chiếu)
- **Hiện tại:** Xem [[02 - Mistake Frequency Dashboard]]
- **Mục tiêu:** <2 lần / 20 lệnh
- **Tần suất review:** Hàng tuần

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [ ] Xác định top 3 lỗi từ Mistake Database
- [ ] Viết biện pháp đối phó (luật/mục checklist) cho từng lỗi
- [ ] Hai tuần liền không mắc lỗi số 1
- [ ] Cả ba lỗi đều dưới 2 lần / 20 lệnh

## Nhật ký tiến độ
| Ngày | Tiến độ % | Ghi chú |
|---|---:|---|
| 2026-06-23 | 20 | Lấy điểm xuất phát từ Mistake Frequency Dashboard. |
| 2026-07-08 | 20 | **Chuyển động thật đầu tiên sau 15 ngày đứng yên.** 3 note lỗi top-3 — rỗng suốt 6 ngày (từ 07-03) — hôm nay đã có nội dung THẬT kèm biện pháp đối phó cụ thể: [[06 - Mistake - Not Have Market Structure Shift]] (244 dòng — "sweep là câu hỏi, MSS là câu trả lời"; 2 biến thể lỗi; rule "No MSS No Entry"), [[09 - Mistake - Wrong daily bias]] (280 dòng, kèm SVG), [[07 - Mistake - Risk more than 0.5% total account]] (287 dòng). Việc này **mở khoá cột mốc #2** ("Viết biện pháp đối phó cho từng lỗi") vốn bị chặn từ 07-03. Cột mốc #1 ("Xác định top-3 từ Mistake Database") cũng đã có đủ bằng chứng (top-3 hiện tại: 06=14 lần, 09=7 lần, 07=5 lần trên trade live). **Đề nghị tick cột mốc #1 + #2** và chỉnh `progress` cho khớp. Lưu ý: tần suất lỗi live-trade CHƯA đổi (không có lệnh live hôm nay; lỗi #1 tái xuất hôm nay chỉ trong backtest, không tính vào [[02 - Mistake Frequency Dashboard]]). |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Hold daily journaling and process discipline]]
