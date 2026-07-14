---
type: goal
horizon: Mid
category: Backtest
status: In Progress
priority: Medium
progress: 8
metric: Tổng số backtest đã log trong 04 - Backtesting
baseline: "6"
target: 200 backtest đã log
phase: Phase 2 - Edge Building
start_date: 2026-06-23
due_date: 2027-06-30
tags:
  - goal
---

# Xây dựng mẫu backtest đủ tin cậy thống kê

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Backtest
> - **Vì sao quan trọng:** Mẫu lớn và nhất quán mới biến "mình nghĩ nó chạy được" thành edge đo được. Đây là nguồn của chỉ số Số lượng backtest.
> - **Điều kiện thành công:** 200 backtest được log với các trường nhất quán (setup, R, kết quả, ghi chú).

## Định nghĩa hoàn thành
- [ ] 200 backtest được log trong `04 - Backtesting`
- [ ] Gắn tag nhất quán để dashboard đọc được
- [ ] Review thống kê tổng hợp mỗi tháng

## Cách đo lường
- **Chỉ số:** Số lượng note backtest
- **Hiện tại:** 16 backtest
- **Mục tiêu:** 200 backtest
- **Tần suất review:** Hàng tuần

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [ ] 50 backtest đã log
- [ ] 100 backtest đã log
- [ ] 200 backtest đã log
- [ ] Hình thành thói quen review số lượng backtest hàng tháng

## Nhật ký tiến độ
| Ngày | Tiến độ % | Ghi chú |
|---|---:|---|
| 2026-06-23 | 25 | Đã làm ~15 backtest; cần nhịp độ hàng tuần đều hơn. |
| 2026-07-06 | 25 | 2 backtest mới log hôm nay (`04 - Backtesting/2026-07-06/`, EURUSD Short, Grade A, R 2.1 và 2.78), phá thế đứt nhịp 5 ngày (07-02 → 07-05). Tổng số backtest thực tế trong toàn vault hiện là **3 note** — không phải ~15 như `baseline` ở trên vẫn ghi; sai lệch này đã được nêu từ 2026-07-03 nhưng `baseline` vẫn chưa được sửa. Cột mốc "50 backtest đã log" vẫn 0/4. |
| 2026-07-07 | 25 | 2 backtest mới log hôm nay (`04 - Backtesting/2026-07-07/`, EURUSD Long, Grade A, R 2.23 và 2.48), ngày backtest thứ 2 liên tiếp. Tổng số backtest thực tế trong toàn vault hiện là **5 note** — `baseline` ở frontmatter đã được sửa thành "5" hôm nay (khớp thực tế), nhưng mục "Cách đo lường → Hiện tại" ở trên vẫn ghi "~15 backtest", chưa cập nhật theo. Cột mốc "50 backtest đã log" vẫn 0/4. Nhịp thực tế 5/14 ngày ≈ 0,357/ngày, vẫn chậm hơn nhịp cần thiết (0,538/ngày) khoảng 1,5 lần. |
| 2026-07-08 | 5 | 1 backtest mới (`04 - Backtesting/2026-07-08/`, EURUSD Long 2005-05-02, **Loss, Grade D, R −1, followed_plan No** — FOMO vào trước khi có Displacement + MSS). Đây là **điểm dữ liệu âm đầu tiên** của mẫu gần đây (4 note trước đều Win Grade A) → tăng độ tin cậy thống kê của mẫu. Tổng backtest thực tế toàn vault: **6/200 = 3%**, ngày backtest **thứ 3 liên tiếp** (07-06→07-08). Nhịp thực tế 6/15 ngày = **0,40/ngày**, vẫn chậm hơn nhịp cần (0,538/ngày) ~1,35 lần nhưng đã thu hẹp so với 07-07. `progress` frontmatter đã sửa 25 → **5** hôm nay (khớp thực tế). Mục "Cách đo lường → Hiện tại" vẫn ghi "~15 backtest" — **chưa vá**, cần sửa thành "6 backtest". Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-09 | 5 | 1 backtest mới (`04 - Backtesting/2026-07-09/`, EURUSD Short 2005-05-11, **Win, Grade A, R thực nhận 2,85 / r_planned 3, followed_plan Yes** — chuỗi đầy đủ: Sweep buy-side tại CE của BPR H1 → Displacement → MSS → FVG → Entry). **Bật lại chất lượng ngay sau điểm Grade D FOMO hôm qua**, áp dụng đúng rule "No MSS No Entry". Tổng backtest thực tế toàn vault: **7/200 = 3,5%**, ngày backtest **thứ 4 liên tiếp** (07-06→07-09) — chuỗi dài nhất từ trước tới nay. Nhịp thực tế 7/16 ngày ≈ **0,44/ngày**, vẫn chậm hơn nhịp cần (~0,54/ngày) ~1,23 lần nhưng tiếp tục thu hẹp. Mục "Cách đo lường → Hiện tại" vẫn ghi "~15 backtest" — **vẫn chưa vá**, cần sửa thành "7 backtest". Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-10 | 5 | **3 backtest mới** (`04 - Backtesting/2026-07-10/`, đều EURUSD 2022 Model): 01 Win 2021-05-03 Short **Grade A followed_plan Yes R 3.075**, 02 Loss 2021-05-07 Short **Grade C/D R −1 followed_plan No — vào ngoài Kill Zone (Asia), tự đánh dấu `invalid-out-of-KZ` loại khỏi cohort edge**, 03 Win 2021-07-22 Long **Grade B R 2.86 followed_plan No**. Net R thô +4.94R (cohort hợp lệ +5.94R/2 lệnh). Tổng backtest thực tế toàn vault: **10/200 = 5%**, ngày backtest **thứ 5 liên tiếp** (07-06→07-10) — chuỗi dài nhất từ trước tới nay. Nhịp thực tế **10/17 ngày ≈ 0,588/ngày** → **lần đầu VƯỢT nhịp cần (~0,54/ngày)** cho due 2027-06-30. Prose "Cách đo lường → Hiện tại" đã **sync 7 → 10 backtest** hôm nay. ⚠️ Mẫu lệch 9/10 note là EURUSD — cần thêm NAS100/GBPUSD/XAUUSD. Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-12 | 6 | **Sync trễ 2 ngày + phá độ lệch thị trường.** Log 07-11 (backtest thứ **11**, EURUSD Long 2013-11-21) không được ghi dòng nào → dòng này gộp bù. Hôm nay (07-12) **1 backtest mới: `04 - Backtesting/2026-07-12/01 - Win - GBPUSD 2024-12-04 Long`, Win, Grade A, R 3.4 (r_planned=r_multiple), followed_plan Yes** — chuỗi đủ Sweep dưới OB H1 → CISD/MSS → 2 FVG (1 trùng CE OB) → Entry trong Discount. ⭐ **Đây là note NON-EURUSD ĐẦU TIÊN** — phá thế lệch tuyệt đối 11/11 EURUSD đã cảnh báo nhiều ngày; mẫu nay **12 note = 11 EURUSD + 1 GBPUSD**. Tổng **12/200 = 6%** (frontmatter `progress` 6 nay khớp thực tế). Prose "Hiện tại" đã sync 11 → **12**. Nhịp thô 12/19 ngày ≈ **0,63/ngày** → vẫn trên nhịp cần (~0,54/ngày) cho due 2027-06-30. ⚠️ Housekeeping: backtest hôm nay **chưa điền `risk_percent`** trong frontmatter. Bổ trợ: một phiên **top-down NAS100** đầy đủ (`10 - Market Analysis/Backtest/`, replay, no-trade) — luyện 2022 Model trên thị trường thứ 2 nhưng KHÔNG tính vào mẫu backtest graded. Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-13 | 6 | **1 backtest mới + non-EURUSD thứ 2 + chuỗi sang ngày thứ 8.** `04 - Backtesting/2026-07-13/01 - Win - NAS100 - 2026-04-02- Long` (dữ liệu 2026-04-02, **NAS100 Long, Win, Grade A, r_planned=r_multiple=2,89, followed_plan Yes**) — chuỗi đủ Sweep SSL/EQL → Displacement H1 → MSS M5 → FVG (POI H1) → Entry tại CE trong Discount. ⭐ **Note NON-EURUSD thứ 2** (sau GBPUSD 07-12) → mẫu nay **13 note = 11 EURUSD + 1 GBPUSD + 1 NAS100**; non-EURUSD lên **2/13** đúng kế hoạch task. Tổng **13/200 = 6,5%** — **giữ frontmatter `progress: 6` (làm tròn xuống để không thổi phồng), sẽ lên 7% ở backtest thứ 14.** Prose "Hiện tại" đã sync 12 → **13**. **Chuỗi backtest nay 8 ngày liên tiếp (07-06→07-13)** — đã xác minh lại: 07-11 CÓ backtest thật (EURUSD 2013-11-21), nên ghi chú "chuỗi đứt ở 07-11" trong summary 07-11 là SAI, chuỗi thực chưa từng đứt từ 07-06. Nhịp thô 13/20 ngày = **0,65/ngày** > nhịp cần 0,53/ngày (tới due 2027-06-30) → vẫn trên nhịp. ⚠️ Housekeeping: mục **5. Lesson Learned** của note hôm nay còn **BỎ TRỐNG** (5.1/5.2/5.3) dù task yêu cầu điền trong ngày — cần bổ sung. Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-14 | 8 | **3 backtest mới (ngày năng suất nhất) + thị trường thứ 3 (XAUUSD) + chuỗi sang ngày thứ 9.** `04 - Backtesting/2026-07-14/`: `01 - Win XAUUSD 2014-05-12 Short` (POI FVG H1, R 2.9, followed_plan Yes), `02 - Loss XAUUSD 2014-05-14 Short` (POI Rejection Block, R −1, followed_plan Yes — thua vì SL đặt trong POI), `03 - Win XAUUSD 2014-05-14 Short` (POI BPR M5 trên CE FVG H1, R 2.97, followed_plan Yes). ⭐ **XAUUSD là market thứ 3** → mẫu nay **16 = 11 EURUSD + 1 GBPUSD + 1 NAS100 + 3 XAUUSD**, non-EURUSD lên **5/16**. Tổng **16/200 = 8%** — frontmatter `progress` sync 6 → **8**; prose "Hiện tại" sync 13 → **16**. Nhịp thô 16/21 ngày ≈ **0,76/ngày** > nhịp cần ~0,53/ngày (due 2027-06-30) → vẫn trên nhịp. ⚠️ **Rủi ro CHẤT LƯỢNG dữ liệu lớn nhất từ trước tới nay:** 2/3 note bị **nhiễm dữ liệu copy-paste** (`01` lẫn số/bias/heading của instrument khác; `03` phải đính chính Entry/SL/TP/R) — chính các note tự gọi đây là rủi ro #1 của mẫu ("garbage in, garbage out"). Việc mai: tạo note [[Mistake - Sai lệch dữ liệu nhật ký]] + rà sạch 3 note. Cột mốc "50 backtest" vẫn 0/4. |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Master the ICT 2022 Model]]
