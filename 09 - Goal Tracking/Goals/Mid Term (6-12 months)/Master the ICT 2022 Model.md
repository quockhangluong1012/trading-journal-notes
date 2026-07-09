---
type: goal
horizon: Mid
category: Skill
status: In Progress
priority: High
progress: 30
metric: Số setup 2022-model đã backtest kèm win rate
baseline: "5"
target: 100 setup @ win rate >55%
phase: Phase 2 - Edge Building
start_date: 2026-06-23
due_date: 2027-03-31
tags:
  - goal
---

# Thành thạo ICT 2022 Model

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Kỹ năng
> - **Vì sao quan trọng:** 2022 model là edge chính của mình. Cần đủ số lần luyện tập có ghi chép để tin tưởng và thực thi một cách máy móc.
> - **Điều kiện thành công:** 100 setup 2022-model có ghi chép, với win rate xác thực trên 55%.

## Định nghĩa hoàn thành
- [ ] 100 setup được ghi nhận trong thư mục backtest
- [ ] Checklist vào/ra lệnh rõ ràng, không mơ hồ
- [ ] Win rate xác thực >55% trên mẫu

## Cách đo lường
- **Chỉ số:** Số setup đã ghi nhận + win rate
- **Hiện tại:** ~6 setup
- **Mục tiêu:** 100 setup @ win rate >55%
- **Tần suất review:** Hàng tuần

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [ ] Viết đầy đủ checklist vào/ra lệnh cho 2022 model
- [ ] 50 setup đã ghi nhận
- [ ] 100 setup đã ghi nhận
- [ ] Win rate xác thực >55% trên mẫu
- [ ] Thực thi model trên thị trường thật trọn 1 tháng

## Nhật ký tiến độ
| Ngày       | Tiến độ % | Ghi chú                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------- | --------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-06-23 |        30 | Đã ghi ~6 setup; checklist còn sơ sài.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 2026-07-06 |        30 | 2 setup ICT 2022 Model mới được backtest hôm nay (EURUSD Short 2005-04-12 và 2005-04-13), cả hai Grade A, followed_plan: Yes, đủ chuỗi Sweep → Displacement → MSS → FVG. Tổng setup ghi nhận trong `04 - Backtesting` hiện là 3 — không phải ~20 như `baseline` ghi. Checklist vào/ra lệnh (cột mốc #1) vẫn chưa được viết thành văn bản riêng; cột mốc "50 setup đã ghi nhận" vẫn 0/5.                                                                                                                                                                                                                                                                                                                                |
| 2026-07-07 |        30 | 2 setup ICT 2022 Model mới được backtest hôm nay (EURUSD Long 2005-04-24 và 2005-04-27), cả hai Grade A, followed_plan: Yes, đủ chuỗi Sweep → Displacement → MSS → FVG. Tổng setup ghi nhận trong `04 - Backtesting` hiện là 5 — không phải ~20 như `baseline` vẫn ghi (trễ 5 ngày, chưa sửa dù đã nêu từ 07-03). Nhịp thực tế 5/14 ngày ≈ 0,357 setup/ngày — gần như đúng nhịp cần thiết (0,356/ngày) để đạt 100 setup trước due_date 2027-03-31, lần đầu tiên đạt mức này. Checklist vào/ra lệnh (cột mốc #1) vẫn chưa được viết; cột mốc "50 setup đã ghi nhận" vẫn 0/5.                                                                                                                                            |
| 2026-07-08 |        30 | 1 setup mới (EURUSD Long 2005-05-02, **Loss, Grade D, followed_plan No** — vào trên nhịp reject đầu tiên khi CHƯA có Displacement + MSS = lỗi *timing*, không phải lỗi *analysis*; bias/POI/RR đều đúng). Tổng setup ghi nhận: **6/100 = 6%**. `baseline` frontmatter **đã sửa** "~20" → "5" hôm nay (nhưng prose "Cách đo lường → Hiện tại: ~20 setup" vẫn chưa vá — cần sửa thành "6 setup"). Nhịp thô 6/15 = **0,40/ngày → đã VƯỢT nhịp cần 0,356/ngày** về số lượng. ⚠️ Nhắc: mục tiêu còn ràng buộc **win rate >55%** — điểm Grade D hôm nay cho thấy chất lượng execution (chờ đủ MSS) mới là ràng buộc thật, không phải số lượng. Checklist vào/ra lệnh (cột mốc #1) vẫn chưa viết; cột mốc "50 setup" vẫn 0/5. |
| 2026-07-09 |        30 | 1 setup mới (EURUSD Short 2005-05-11, **Win, Grade A, followed_plan Yes**, đủ chuỗi Sweep buy-side tại CE của BPR H1 → Displacement → MSS → FVG → Entry). Tổng setup ghi nhận: **7/100 = 7%**. Setup Grade A followed_plan Yes **ngay sau điểm Grade D hôm qua** ⇒ bằng chứng execution đang tự sửa (chờ đủ MSS thay vì vào nhịp reject đầu, đúng rule "No MSS No Entry"). Prose "Cách đo lường → Hiện tại: ~6 setup" cần bump thành **7 setup**. Ràng buộc thật vẫn là **win rate >55%**: mẫu hiện **6 Win / 1 Loss = ~86%** nhưng **n=7 còn quá nhỏ** để kết luận. Checklist vào/ra lệnh (cột mốc #1) vẫn chưa viết — là cột mốc dễ mở khoá nhất còn lại; cột mốc "50 setup" vẫn 0/5. |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Become a consistently profitable ICT trader]], [[Build a statistically validated backtest sample]]
