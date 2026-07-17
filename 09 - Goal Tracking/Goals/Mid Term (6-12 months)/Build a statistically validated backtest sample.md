---
type: goal
horizon: Mid
category: Backtest
status: In Progress
priority: Medium
progress: 11
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
- **Hiện tại:** 22 backtest
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
| 2026-07-14 | 8 | **3 backtest mới (ngày năng suất nhất) + thị trường thứ 3 (XAUUSD) + chuỗi sang ngày thứ 9.** `04 - Backtesting/2026-07-14/`: `01 - Win XAUUSD 2014-05-12 Short` (POI FVG H1, R 2.9, followed_plan Yes), `02 - Loss XAUUSD 2014-05-14 Short` (POI Rejection Block, R −1, followed_plan Yes — thua vì SL đặt trong POI), `03 - Win XAUUSD 2014-05-14 Short` (POI BPR M5 trên CE FVG H1, R 2.97, followed_plan Yes). ⭐ **XAUUSD là market thứ 3** → mẫu nay **16 = 11 EURUSD + 1 GBPUSD + 1 NAS100 + 3 XAUUSD**, non-EURUSD lên **5/16**. Tổng **16/200 = 8%** — frontmatter `progress` sync 6 → **8**; prose "Hiện tại" sync 13 → **16**. Nhịp thô 16/21 ngày ≈ **0,76/ngày** > nhịp cần ~0,53/ngày (due 2027-06-30) → vẫn trên nhịp. ⚠️ **Rủi ro CHẤT LƯỢNG dữ liệu lớn nhất từ trước tới nay:** 2/3 note bị **nhiễm dữ liệu copy-paste** (`01` lẫn số/bias/heading của instrument khác; `03` phải đính chính Entry/SL/TP/R) — chính các note tự gọi đây là rủi ro #1 của mẫu ("garbage in, garbage out"). Việc mai: tạo note [[12 - Mistake - Log Data Mismatch - Backtest]] + rà sạch 3 note. Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-15 | 8 | **1 backtest SẠCH (chất > lượng) + chuỗi sang ngày thứ 10.** `04 - Backtesting/2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short` (**XAUUSD Short, Loss, Grade C+, r_planned 3.9 → r_multiple −1, followed_plan Yes**). Root cause đơn nhất, tự chấm trung thực: **SAI POI selection** — chọn Breaker Block nông (0.618) thay vì Order Block sâu (0.786) terminal → SL rơi vào đường thanh khoản dẫn tới OB, bị quét trước khi giá đảo chiều đúng hướng chạm TP ("loss đúng hướng"). ⭐ Mẫu phản chứng sạch cho **Rule POI Priority** (ưu tiên POI sâu khi ≥2 PD Array xếp chồng). Tổng **17/200 = 8.5%** — **giữ `progress: 8`** (làm tròn xuống, không thổi phồng). Prose "Hiện tại" sync 16 → **17**. Chuỗi backtest **10 ngày liên tiếp** (07-06→07-15); nhịp thô 17/22 ngày ≈ **0.77/ngày** > nhịp cần ~0.53/ngày (due 2027-06-30). ⚠️ **Housekeeping tồn từ 07-14 CHƯA đóng:** 3 note XAUUSD 07-14 vẫn `symbol:` RỖNG (chưa rà sạch) + [[12 - Mistake - Log Data Mismatch - Backtest]] vẫn chưa tạo → 3/17 mẫu vẫn chưa đáng tin. Cột mốc "50 backtest" vẫn 0/4. |
| 2026-07-16 | 10 | **2 backtest mới (EURUSD Win R 2.49, GBPUSD Win TP1 khớp nhưng r_multiple tổng chưa điền) + đính chính sai số đếm.** ⚠️ **Phát hiện: log 07-15 ghi tổng 17, nhưng đếm trực tiếp thư mục `04 - Backtesting/2026-07-15/` cho thấy 2 note** (`01 - Loss XAUUSD` + `02 - Win EURUSD 2026-11-30`, không phải 1) — log cũ bỏ sót 1 note. Tổng thực cuối 07-15 là **18**, không phải 17. Cộng 2 note hôm nay → tổng thực tế toàn vault **20/200 = 10%** (đếm trực tiếp bằng frontmatter `result:`, không dựa vào log cũ). `progress` frontmatter sync 8 → **10**; prose "Hiện tại" sync 17 → **20**. Mẫu nay: **13 EURUSD + 2 GBPUSD + 1 NAS100 + 4 XAUUSD, 16 Win/4 Loss = 80%**. Chuỗi backtest **11 ngày liên tiếp** (07-06→07-16). Nhịp từ `start_date` 2026-06-23 (23 ngày) ≈ **0,87/ngày** > nhịp cần ~0,52/ngày để đạt 200 trước due 2027-06-30 (còn 349 ngày) — vẫn trên nhịp rõ rệt. ✅ **Housekeeping đã đóng ngoài mong đợi:** kiểm tra trực tiếp hôm nay, `symbol`/`result` ở cả 3 note XAUUSD 07-14 + note XAUUSD 07-15 đều **đã điền đầy đủ** — không còn trống như 07-14/07-15 mô tả (không rõ khi nào được sửa). [[12 - Mistake - Log Data Mismatch - Backtest]] vẫn CHƯA được tạo trong `06 - Mistake Database/`. |
| 2026-07-17 | 11 | **2 backtest mới GBPUSD (chuỗi sang ngày thứ 12) + phát hiện quan trọng: nhịp hiện tại KHÔNG kịp mốc tự đặt 2027-01-07.** `04 - Backtesting/2026-07-17/`: `01 - Win GBPUSD 2014-07-14 Long` (R 2.33, entry hợp lệ nhưng nông — nửa trên FVG chưa vào OTE, xem [[Master the ICT 2022 Model]]) và `02 - Loss GBPUSD 2014-07-17 Long` (R −1, **first_error_step = sweep**: vào Long khi SSL cấu trúc dưới POI chưa bị quét — "good loss" về kỷ luật, flawed setup selection về filter). Tổng thực tế toàn vault **22/200 = 11%** (13 EURUSD + 4 GBPUSD + 4 XAUUSD + 1 NAS100; 17 Win / 5 Loss = 77,3%, giảm nhẹ từ 80% n=20). `progress` frontmatter sync 10 → **11**; prose "Hiện tại" sync 20 → **22**. ⭐ **[[12 - Mistake - Log Data Mismatch - Backtest]] đã được tạo THẬT hôm nay** trong `06 - Mistake Database/` — đóng nợ 4 ngày (07-14→07-17) nêu trong log 07-14/07-15/07-16. ⚠️ **Trớ trêu ngay trong ngày đóng nợ:** note `01 - Win GBPUSD ...` HÔM NAY lại tự phát hiện đúng loại lỗi mà note-lỗi-mới-tạo mô tả — filename ghi `2014-06-25` nhưng `trade_date` frontmatter là `2014-07-14` (lệch ngày); note tự đề xuất đổi tên nhưng gợi ý số thứ tự `02` là SAI (phải giữ `01` vì đây là backtest đầu tiên của ngày — chỉ ngày trong tên cần sửa) — **CHƯA đổi tên, chờ Khang xác nhận** theo house rule không tự rename. <br><br>⭐ **Phát hiện nhịp độ quan trọng nhất từ trước tới nay:** nhịp thực tế từ `start_date` (24 ngày) = 22/24 ≈ **0,92/ngày**. Chiếu theo nhịp này, mốc **200 backtest sẽ đạt vào khoảng 2027-01-27** — **CHẬM HƠN ~20 ngày so với mốc tự đặt sẵn sàng thi 2027-01-07** (còn 174 ngày tính từ hôm nay). Để chạm cả hai mốc cùng lúc, cần nhịp **~1,02 backtest/ngày** trở đi (nhanh hơn nhịp hiện tại ~11%) — không phải khoảng cách lớn, nhưng nếu duy trì đúng 0,92/ngày như hiện tại thì **sẽ trễ, không phải "vẫn trên nhịp" như các log trước đây kết luận khi so với due_date xa (2027-06-30)**. Due_date frontmatter của goal này (2027-06-30) không phải mốc ràng buộc thật — mốc thật là ngày tự đặt 2027-01-07; hai mốc này đang lệch nhau và cần Khang quyết định: đẩy nhịp backtest lên, hoặc chấp nhận mua gói với mẫu backtest nhỏ hơn 200 (ví dụ dùng ngưỡng 100 của [[Master the ICT 2022 Model]], due 2027-03-31 — mốc này cũng sau 01-07). Cột mốc "50 backtest" vẫn 0/4. |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Master the ICT 2022 Model]]
