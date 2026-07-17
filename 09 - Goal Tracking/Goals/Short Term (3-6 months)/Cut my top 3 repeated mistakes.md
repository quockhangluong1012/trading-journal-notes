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
| 2026-07-17 | 20 | **9 ngày sau (07-08 → 07-17): vòng lặp backtest chạy mạnh, nhưng chỉ số chính thức của mục tiêu này vẫn đứng yên vì lý do có thể giải thích được — không có lệnh live nào.** Lệnh live gần nhất vẫn là 2026-06-18 (29 ngày không có trade thật) → **tần suất lỗi live-trade (06=14, 09=7, 07=5 trên tổng lệnh live) không đổi một đơn vị nào** so với 07-08, đơn giản vì cửa sổ "mỗi 20 lệnh" không nạp thêm dữ liệu live. Đây KHÔNG phải dấu hiệu xấu (không mắc thêm lỗi mới trên live) nhưng cũng không phải tiến bộ thật — chỉ số đang bị đóng băng, không phải cải thiện. <br><br>**Về backtest** (không tính vào chỉ số chính thức, nhưng là tín hiệu sớm): 16 backtest mới trải 9 ngày (07-08, 07-09, 07-10 ×3, 07-11, 07-12, 07-13, 07-14 ×3, 07-15 ×2, 07-16 ×2, 07-17 ×2) trên EURUSD/GBPUSD/XAUUSD/NAS100. Trong đó: `bias_correct: No` chỉ xuất hiện **1 lần** (07-17, GBPUSD Loss — lỗi #09 Wrong daily bias tái xuất, chỉ trong backtest); không backtest nào gắn `first_error_step: mss` trực tiếp (gần nhất là 1 lần `displacement` ở 07-08); các bản có điền `risk_percent` đều ghi đúng 0.5% — không thấy vi phạm lỗi #07 trong mẫu backtest này. **Tín hiệu mới cần theo dõi:** backtest lỗ 07-17 ([[02 - Loss - GBPUSD - 2014-07-17 - Long]]) mô tả một pattern CHƯA nằm trong top-3 hiện tại — entry đi INTO liquidity (POI sát "móng" dealing range, SSL cấu trúc chưa bị quét trước khi tin MSS "sớm"). Bản thân note đó đề xuất soi lại toàn bộ mẫu backtest để kiểm định xem đây có phải lỗi hệ thống thứ 4 hay là một biến thể của lỗi #06 (MSS) — **chưa kết luận, tránh curve-fitting với n=1**. <br><br>**Cột mốc vẫn 0/4 tick** — khuyến nghị tick #1+#2 từ 07-08 chưa được xác nhận/thực hiện; `progress` frontmatter (20) vẫn dựa trên đánh giá cũ, chưa phản ánh cột mốc thật. Cần Khang xác nhận trước khi tick (theo house rule "confirm before edits to shared/tracked state"). **Việc cần làm tiếp:** (1) xác nhận có tick cột mốc #1+#2 hay không; (2) khi có lệnh live trở lại, đối chiếu ngay xem 3 lỗi top-3 có tái xuất không — đó mới là phép thử thật của mục tiêu này, không phải số lượng backtest. |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Hold daily journaling and process discipline]]
