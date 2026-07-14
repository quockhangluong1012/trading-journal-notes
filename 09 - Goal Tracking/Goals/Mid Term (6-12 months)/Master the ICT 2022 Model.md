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
- **Hiện tại:** 16 setup (13 Win / 3 Loss ≈ 81%, n=16 còn nhỏ)
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
| 2026-07-10 |        30 | **3 setup mới** (`04 - Backtesting/2026-07-10/`, đều EURUSD): 2021-05-03 Short **Win Grade A followed_plan Yes** (chuỗi đủ, entry tại CE Unicorn H1 trong Premium — sửa được lỗi FOMO-tại-CE cũ), 2021-05-07 Short **Loss Grade C/D followed_plan No** (vào ngoài Kill Zone + nhầm HTF bias với short-term draw → rút ra **4-gate pre-trade**: Session/Draw/Location-OTE/Signal-quality; đánh dấu `invalid-out-of-KZ`), 2021-07-22 Long **Win Grade B followed_plan No**. Tổng setup ghi nhận: **10/100 = 10%**, ngày backtest **thứ 5 liên tiếp**. Nhịp thô 10/17 ≈ **0,588/ngày** → trên nhịp cần (0,34/ngày tới due 2027-03-31) về **số lượng**. ⚠️ Ràng buộc THẬT vẫn là **win rate >55%**: mẫu **8 Win / 2 Loss = 80%** (≈89% nếu loại lệnh out-of-KZ) nhưng **n=10 quá nhỏ**. Prose "Cách đo lường → Hiện tại" đã **sync ~6 → 10 setup**. Cột mốc "50 setup" vẫn 0/5. |
| 2026-07-12 |        30 | **1 setup mới + bước nhảy hiểu-biết nền tảng lớn nhất từ trước tới nay.** Setup: **GBPUSD 2024-12-04 Long, Win, Grade A, R 3.4, followed_plan Yes** (`04 - Backtesting/2026-07-12/`) — chuỗi đủ Sweep dưới OB H1 → CISD/MSS → FVG trùng CE OB → Entry Discount; ⭐ **setup NON-EURUSD đầu tiên** của cả mẫu. Tổng **12/100 = 12%**. Ràng buộc THẬT vẫn là **win rate >55%**: mẫu nay **10 Win / 2 Loss ≈ 83%** nhưng **n=12 vẫn quá nhỏ** để kết luận. Prose "Hiện tại" đã sync 10 → **12 setup**. **Nền tảng concept nhảy vọt hôm nay:** 5 concept lên `tested` (từ 1 → 6): [[13 - FVG  - Fair Value Gap|FVG]], [[03 - Balanced Price Range|BPR]], [[27 - Premium Discount]], [[25 - OB - Order Block|OB]], [[18 - Kill Zones]] — đây đều là các khối trụ của chuỗi Sweep→Displacement→MSS→FVG/OB→CE. Thêm concept mới [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)|Liquidity Scale Alignment]] (developing) + Model note mới [[14 - Mayne Structure + OTE Model]] + checklist + 1 phiên top-down NAS100 đầy đủ. ⚠️ Điểm rủi ro chất lượng: backtest GBPUSD tự chấm Grade A dù phần phân tích ghi "bias D1 chưa xác nhận chính xác" → mắt xích yếu là quyết định entry-level chưa có dữ liệu validate (xem mục 5 của note). Cột mốc #1 (viết checklist vào/ra) + "50 setup" vẫn 0/5. |
| 2026-07-13 |        30 | **1 setup mới + 1 concept nền tảng lên `tested`.** Setup: **NAS100 2026-04-02 Long, Win, Grade A, R 2,89, followed_plan Yes** (`04 - Backtesting/2026-07-13/`) — chuỗi đủ Sweep SSL/EQL khung D1/H1 → Displacement H1 (tạo FVG) → MSS M5 → Entry tại CE của FVG H1 trong Discount, TP tại EQH M15. ⭐ **Setup NON-EURUSD thứ 2** (NAS100, sau GBPUSD 07-12) — mẫu đa dạng dần: 11 EURUSD + 1 GBPUSD + 1 NAS100. Tổng **13/100 = 13%**. Ràng buộc THẬT vẫn là **win rate >55%**: mẫu nay **11 Win / 2 Loss ≈ 85%** nhưng **n=13 vẫn quá nhỏ** để kết luận. Prose "Hiện tại" đã sync 12 → **13 setup**. **Concept nền tảng:** [[35 - Aggressive Displacement Entry]] lên **`tested`** hôm nay (`last_reviewed`/`updated` = 2026-07-13) → nhóm `tested` từ 6 → **7**; đây là gate "displacement thật" phục vụ trực tiếp bước Displacement của chuỗi. ⚠️ Chất lượng ghi chép: mục **5. Lesson Learned** của backtest hôm nay còn **BỎ TRỐNG** — Grade A tự chấm nhưng chưa rút root-cause/pattern/rule; cần bổ sung để setup này thực sự "có ghi chép". ⚠️ Overtick learning: task tick [[42 - SMT Divergence]] nhưng `last_reviewed` note vẫn 2026-07-11 → không tính học hôm nay. Cột mốc #1 (viết checklist vào/ra) + "50 setup" vẫn 0/5. |
| 2026-07-14 |        30 | **3 setup mới (XAUUSD — thị trường thứ 3) + 1 concept lên `developing`.** `04 - Backtesting/2026-07-14/`: `01 - Win` (POI FVG H1, R 2.9, tự chấm A → **nên A-** vì file nhiễm dữ liệu), `02 - Loss` (POI Rejection Block, R −1, tự chấm A- → **nên B/B-**: thua vì SL đặt ngay mép dưới POI thay vì trên invalidation thật của RB H1 → bị quét bởi retrace bình thường trong OTE), `03 - Win` (POI BPR M5 trùng CE FVG H1, R 2.97, Grade A thật nhờ nested confluence). Tổng **16/100 = 16%**; mẫu nay **11 EURUSD + 1 GBPUSD + 1 NAS100 + 3 XAUUSD**. Ràng buộc THẬT vẫn là **win rate >55%**: mẫu nay **13 Win / 3 Loss ≈ 81%** (giảm nhẹ từ 85% do +1 Loss), **n=16 vẫn quá nhỏ**. Prose "Hiện tại" sync 13 → **16 setup**. **Concept:** [[28 - Rejection Block]] `seed → developing` (`last_reviewed`/`updated` 07-14), áp dụng trực tiếp làm POI trong `02 - Loss`. ⚠️ **Hai rủi ro chất lượng (quan trọng cho đúng ràng buộc win rate):** (1) grade thổi phồng 2/3 note — nếu chấm đúng thì chất lượng mẫu thấp hơn con số; (2) 2/3 note nhiễm dữ liệu copy-paste → cần tạo note [[Mistake - Sai lệch dữ liệu nhật ký]] + [[Mistake - Stop loss đặt sai vị trí]] và rà sạch. Cột mốc #1 (viết checklist vào/ra) + "50 setup" vẫn 0/5. |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Become a consistently profitable ICT trader]], [[Build a statistically validated backtest sample]]
