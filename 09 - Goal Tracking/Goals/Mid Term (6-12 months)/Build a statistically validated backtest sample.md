---
type: goal
horizon: Mid
category: Backtest
status: In Progress
priority: Medium
progress: 6
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
- **Hiện tại:** 7 backtest
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

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Master the ICT 2022 Model]]
