---
type: weekly-summary
week: 2026-W28
start_date: 2026-07-06
end_date: 2026-07-12
days_to_prop_exam: 179
exam_target: 2027-01-07
backtests_logged_week: 9
trades_logged_week: 0
concepts_reviewed_week: 18
net_r_week: 0
days_with_data: 6
tags: [weekly-summary, prop-firm-prep]
---

# 🗓️ Weekly Summary — 2026-W28 (2026-07-06 → 2026-07-12)

> [!info] Đếm ngược & bối cảnh
> - **179 ngày** còn lại tới mốc tự đặt **2027-01-07** (song song **FTMO 10K$** + **The5ers High Stakes 10K$** — hai track độc lập, KHÔNG gộp luật).
> - **Giai đoạn hiện tại:** Giai đoạn 1 — Nền tảng ([[01 - Roadmap]]) — trọng tâm là dữ liệu sạch + kỷ luật ghi chép, KHÔNG phải khối lượng lệnh live.
> - **Dữ liệu tuần:** **6/7 ngày có Daily Summary** (07-06 → 07-11). Ngày 07-12 (Chủ nhật, chốt tuần) **chưa có Daily Summary** tại thời điểm tạo bản này → ghi "chưa có dữ liệu", không suy đoán. Daily Tasks có đủ 7/7 ngày.
> - **Chủ đề của tuần:** *Tuần backtest mạnh nhất và bứt phá chất lượng học* — nối chuỗi backtest dài nhất từ trước tới nay, lần đầu vượt nhịp cần cho hai goal đếm số, và phá nút thắt "0 concept `tested`". Nhưng **khối nợ track challenge (FTMO/The5ers) gần như còn nguyên** suốt cả tuần — đây vẫn là rủi ro tiến độ #1.

> [!warning] Cảnh báo — nợ tồn đọng & vấn đề dữ liệu (nêu, KHÔNG tự sửa)
> 1. **Track challenge đứng yên 19 ngày (rủi ro tiến độ #1).** [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]] có dòng "Nhật ký tiến độ" cuối cùng vẫn **2026-06-23**. Cả tuần W28 **không có bước Giai đoạn 0 thật nào** (bảng lot size 0,5%/1% cho tài khoản 10K$ vẫn chưa lập). Với 179 ngày còn lại, đây là điểm nghẽn thật — KHÔNG phải số lượng backtest.
> 2. **Nhãn `phase: "Phase 4 - Challenge"` SAI trong cả 2 goal challenge** — thực tế cả hai đang ở **Giai đoạn 0 — Chuẩn bị** (chưa mua gói). Hệ quả: dataview trong [[01 - Roadmap]] đang xếp 2 goal này vào "Giai đoạn 4 — Thử thách". Chỉ cần sửa 1 dòng frontmatter mỗi file — nêu suốt tuần vẫn chưa sửa.
> 3. **4/6 goal lệch `progress` (frontmatter) vs cột mốc thật:** Backtest sample (6% vs 0/4), Master 2022 (30% vs 0/5), Cut top-3 (20% vs 0/4), Journaling (40% vs 0/4). Theo công thức dashboard, cả 4 đều **0%** theo cột mốc. FTMO/The5ers (0% vs 0/8) là 2 goal duy nhất khớp.
> 4. **Mismatch Daily Summary ↔ thực tế file (07-11):** `2026-07-11 - Daily summary.md` ghi `backtests_logged: 0` và "thư mục `04 - Backtesting/2026-07-11/` không tồn tại", **nhưng thư mục đó nay có 1 note thật** (`01 - Win - EURUSD - 2013-11-21 - Long.md`, `backtest_date: 2026-07-11`). Note được tạo *sau* khi summary 07-11 chạy → cần đối chiếu lại (tick nhầm ngày hay summary chạy trước backtest?).
> 5. **Schema `net_r_today` dùng không nhất quán cả tuần:** 07-10 ghi **4.94** (là R *backtest*, không có lệnh live), trong khi 07-06/07/08/09 ghi **0** dù cũng có R backtest; 07-11 ghi chuỗi **"chưa có dữ liệu"**. Trường này nên thống nhất chỉ đo *live* (và để backtest R ở chỗ khác) để dashboard tương lai không cộng nhầm.
> 6. **`baseline` frontmatter lệch số thật:** [[Build a statistically validated backtest sample]] `baseline: "6"` (thực tế đã **11** note); [[Master the ICT 2022 Model]] `baseline: "5"` (thực tế **11** setup). Đây là nợ cũ kiểu "baseline không đối chiếu", lặp lại ở dạng mới.
> 7. **Note lỗi "Vào lệnh sai Kill Zone" vẫn CHƯA được tạo** trong `06 - Mistake Database/` (đề xuất từ 07-10) → dashboard tần suất lỗi không bắt được lỗi này.
> 8. **Mẫu backtest lệch thị trường tuyệt đối: 11/11 note là EURUSD.** Mục tiêu "đổi sang NAS100/GBPUSD/XAUUSD" đặt ra nhiều ngày vẫn chưa thực hiện — rủi ro edge thiên vị 1 thị trường.
> 9. **Standing note — 24 ngày không có lệnh live** (gần nhất 2026-06-18 `Loss - 01 - Trade 2026-06-18 NDX Short`). Chấp nhận được trong Giai đoạn 1, ghi nhận để không quên execution live vẫn là ẩn số chưa kiểm chứng.

## 📊 Số liệu tổng hợp trong tuần

| Chỉ số | Giá trị | Ghi chú |
|---|---|---|
| Ngày có Daily Summary | **6/7** | 07-06→07-11 có; 07-12 (chốt tuần) chưa có |
| Backtest log (theo frontmatter Daily Summary) | **9** | 2+2+1+1+3+0 (07-11 frontmatter ghi 0) |
| Backtest — số **note file thật** trong tuần | **10** | 07-11 nay có 1 note (xem Cảnh báo #4) → khớp con số "10" Khang ghi ở [[02 - Skill Metrics]] |
| Tổng backtest toàn vault | **11** | 10 trong tuần + 1 note W27 (`2026-07-01`) |
| Lệnh live | **0** | Không có lệnh live nào cả tuần |
| Net R (live) | **0** | Không có lệnh live |
| Net R (backtest, không phải tiền thật) | **~ +15,4R** | 07-06 +4,88 · 07-07 +4,71 · 07-08 −1 · 07-09 +2,85 · 07-10 +4,94 (cohort hợp lệ +5,94) · 07-11 Win (r_planned 3,41) |
| Lượt ôn concept (tổng frontmatter) | **18** | ~15 concept riêng biệt có bằng chứng `last_reviewed`/đổi status |
| Chuỗi backtest liên tiếp | **6 ngày** (07-06→07-11) | Dài nhất từ trước tới nay (nếu tính note 07-11 nay đã tồn tại) |
| Chuỗi journaling liên tiếp | **7 ngày** (07-05→07-11) | Dài nhất từ trước tới nay |

**`mistakes_triggered` gộp cả tuần (dedup + số lần) — toàn bộ trong BACKTEST, không có lỗi live:**

| Lỗi | Số lần | Ngày | Ghi chú |
|---|---:|---|---|
| [[08 - Mistake - Weak Displacement]] | 2 | 07-08, 07-10 | Vào lệnh khi nhịp đẩy chỉ gồm nến thân nhỏ/doji |
| [[04 - Mistake - FOMO Entry]] | 1 | 07-08 | *Root cause* của cụm lỗi 07-08 |
| [[06 - Mistake - Not Have Market Structure Shift]] | 1 | 07-08 | Lỗi top-3 #1 — tái xuất trong backtest (nơi cần bắt được nó) |
| [[10 - Mistake - FVG Not Valid]] | 1 | 07-08 | FVG entry sinh từ nến thân nhỏ |
| Vào lệnh sai Kill Zone | 1 | 07-10 | ⚠️ **Chưa có note** trong Mistake Database |

> [!info] Tần suất lỗi top-3 trên trade **live** giữ nguyên cả tuần
> [[06 - Mistake - Not Have Market Structure Shift]] = **14** · [[09 - Mistake - Wrong daily bias]] = **7** · [[07 - Mistake - Risk more than 0.5% total account]] = **5**. Không có lệnh live nào trong tuần nên [[02 - Mistake Frequency Dashboard]] (chỉ đọc field `mistakes` của trade live) không đổi. Cả 3 note lỗi đều đã có nội dung biện pháp đối phó đầy đủ (244/280/287 dòng — viết từ 07-08, vẫn còn nguyên).

## 🎯 Đối chiếu mục tiêu (theo công thức cột mốc, KHÔNG dùng `progress` ghi tay)

> Công thức dashboard: `progress = (cột mốc đã tick) / (tổng cột mốc) × 100`; chỉ fallback về field `progress:` khi goal không có cột mốc nào. Cả 6 goal đều có cột mốc → tỉ lệ cột mốc là con số đúng duy nhất.

| Goal | `progress` (fm) | Cột mốc | % theo cột mốc | Khớp? | `phase:` hợp lý? | Log gần nhất (đến 07-12) |
|---|---:|---|---:|---|---|---|
| [[Pass FTMO first package challenge (10K$)]] | 0% | 0/8 | 0% | ✅ | ❌ Ghi "Phase 4 - Challenge" nhưng thực tế **Giai đoạn 0 — Chuẩn bị** | 2026-06-23 (**19 ngày**) |
| [[Pass The5er first package challenge (10k$)]] | 0% | 0/8 | 0% | ✅ | ❌ Cùng lỗi nhãn phase như FTMO | 2026-06-23 (**19 ngày**) |
| [[Build a statistically validated backtest sample]] | 6% | 0/4 | 0% | ❌ **Lệch** | ✅ Phase 2 hợp lý | 2026-07-10 (**2 ngày**) |
| [[Master the ICT 2022 Model]] | 30% | 0/5 | 0% | ❌ **Lệch** | ✅ Phase 2 hợp lý | 2026-07-10 (**2 ngày**) |
| [[Cut my top 3 repeated mistakes]] | 20% | 0/4 | 0% | ❌ **Lệch** | ✅ Phase 1 hợp lý | 2026-07-08 (**4 ngày**) |
| [[Hold daily journaling and process discipline]] | 40% | 0/4 | 0% | ❌ **Lệch** | ✅ Phase 1 hợp lý | 2026-07-11 (**1 ngày** — mới nhất) |

> [!note] Cột mốc đã DƯ bằng chứng để tick nhưng chưa được tick (để Khang tự chấm, routine không tự tick)
> - [[Hold daily journaling and process discipline]] **#1** ("Định nghĩa quy trình ghi nhật ký hàng ngày") — chuỗi journaling 7 ngày + hệ thống tasks/summary chạy ổn định là bằng chứng quá đủ.
> - [[Cut my top 3 repeated mistakes]] **#1** ("Xác định top-3") + **#2** ("Viết biện pháp đối phó") — top-3 đã xác định (06/09/07) và cả 3 note đã viết biện pháp từ 07-08.
> Tick 3 cột mốc này + chỉnh `progress` cho khớp tỉ lệ sẽ xoá được 2/4 mismatch đang tồn tại.

## 📚 1. Học được gì tuần này

Đây là **tuần học mạnh nhất** từ khi có hệ thống, với bằng chứng frontmatter thật (không chỉ checkbox):

- **Phá nút thắt "0 `tested`":** [[10 - Consequent Encroachment (Mean Threshold)]] là concept **đầu tiên toàn vault** lên `status: tested` (07-10), kiểm chứng trực tiếp qua backtest (nhiều lệnh entry tại CE của FVG/BPR/Unicorn). Tại thời điểm tạo bản này, số concept `tested` đã lên **5** (thêm [[13 - FVG  - Fair Value Gap]], [[03 - Balanced Price Range]], [[25 - OB - Order Block]], [[18 - Kill Zones]] — 4 note này lên `tested` **sau 07-11**, tức trong ngày 07-12 chưa có Daily Summary; ghi nhận là số liệu thật tại thời điểm chốt, không tính vào rollup 6 ngày).
- **Chuỗi nâng `seed → developing` có bằng chứng:** [[21 - Market Structure Shift]] + [[41 - Change in State of Delivery]] (07-07); [[05 - BOS - Break of Structure]] + [[04 - Breaker Block]] + [[18 - Kill Zones]] (07-08); [[35 - Aggressive Displacement Entry]] + [[10 - Consequent Encroachment (Mean Threshold)]] + [[42 - SMT Divergence]] (07-09). 07-09 còn ôn thêm 6 concept ngoài task-list.
- **Snapshot concept tại thời điểm chốt (07-12):** **50 note — 17 `seed`, 28 `developing`, 5 `tested`, 0 `mastered`** (đầu tuần 07-06 là 44 note, 19 `seed`/24 `developing`/0 `tested`).
- **Trọng tâm học bám sát điểm yếu execution:** MSS/BOS/CISD (trị lỗi #1), Aggressive Displacement (trị Weak Displacement), Kill Zones (trị lỗi out-of-KZ), SMT (trị lỗi #2 Wrong bias) — học có mục tiêu, không tản mạn.

## 💪 2. Làm tốt điều gì

- **Kỷ luật ghi chép bền:** 7 ngày journaling liên tiếp (07-05→07-11), 8 Daily Summary tổng cộng — đây là bằng chứng cho cột mốc #1 của [[Hold daily journaling and process discipline]].
- **Chất lượng backtest tự sửa trong tuần:** 07-08 log điểm âm đầu tiên (Grade D, FOMO) → **07-09 bật lại Grade A** đúng rule "No MSS No Entry" vừa viết. "A good win *sau* a good loss" — bài học được *áp dụng*, không chỉ ghi.
- **Kỷ luật thống kê:** lệnh out-of-Kill-Zone 07-10 được tự đánh dấu `invalid-out-of-KZ` và **loại khỏi cohort đo edge** — đúng cách xử lý mẫu.
- **Trả nợ lớn ngày 07-08:** viết nội dung thật cho 3 note lỗi top-3 (rỗng 6 ngày), điền Lesson Learned 2 backtest 07-06, sửa `baseline`/`progress` — ngày trả nợ kỷ luật lớn nhất của hệ thống.

## 🔧 3. Cần cải thiện điều gì (riêng tuần này)

- **Track challenge đứng yên cả tuần:** 0 bước Giai đoạn 0 nào được chạm trong suốt W28. Đây là việc *rẻ* (bảng lot size là bài giấy) nhưng liên tục bị đẩy sau backtest.
- **Nợ hành chính dai dẳng:** nhãn `phase` sai, `baseline` lệch, note Kill Zone chưa tạo — toàn việc 1–5 phút nhưng bị hoãn nhiều ngày. Xu hướng "trì hoãn task track/hành chính vì chúng dễ hơn backtest" đã được chính Daily Summary 07-11 chỉ ra.
- **Mẫu backtest 11/11 EURUSD:** cần đa dạng thị trường trước khi mẫu đủ lớn, nếu không edge đo được sẽ thiên vị.

## 🚫 4. Lỗi/thói quen xấu lặp trong tuần

- **Overtick checkbox không khớp bằng chứng:** 07-06 (nhiều mục ôn concept + "sửa baseline" tick nhưng file không đổi) và 07-10 (tick [[35 - Aggressive Displacement Entry]] + [[42 - SMT Divergence]] nhưng `last_reviewed` không đổi). 07-11 đã tự bù đúng 2 note này — nhưng thói quen tick-cho-xong cần cảnh giác.
- **Mismatch prose ↔ frontmatter** lặp lại xuyên tuần (baseline, "Cách đo lường → Hiện tại") — sửa một chỗ, bỏ lại chỗ kia.
- **Mismatch Daily Summary ↔ file thật (07-11 backtest):** dạng nợ dữ liệu mới, cần quy trình "đối chiếu file trước khi chốt summary".

## 🩺 5. Có đang đúng nhịp không? (pace check)

Còn **179 ngày** tới 2027-01-07; đã trôi **19 ngày** kể từ `start_date` chung 2026-06-23.

- ✅ **Backtest sample** (due 2027-06-30): **11/200 = 5,5%**. Nhịp thực tế ~**0,58/ngày** > nhịp cần ~**0,54/ngày** → **trên nhịp về số lượng**. *Ràng buộc thật:* mẫu 11/11 EURUSD chưa đại diện; cột mốc đầu (50 backtest) vẫn 0/4.
- ✅ **Master ICT 2022** (due 2027-03-31): **11/100 setup**, nhịp ~0,58/ngày > nhịp cần ~0,34/ngày → **trên nhịp về số lượng**. *Ràng buộc thật:* **win rate >55%** với n=11 còn quá nhỏ để kết luận (dù mẫu hiện ~9W/2L).
- ✅ **Journaling & 🟡 Cut top-3:** journaling đang rất tốt; cut-top-3 có bằng chứng chất lượng (né lỗi #1 trong replay) nhưng số đo là *tần suất trên lệnh live* → đứng yên hợp lệ vì 0 lệnh live.
- ❌ **BEHIND — hai track challenge (điểm nghẽn thật):** 0/8 cột mốc, 0 bước Giai đoạn 0, log stale **19 ngày**, nhãn phase sai. Với 179 ngày tới mốc tự đặt, cần **bắt đầu Giai đoạn 0 ngay** (lot size → playbook → demo 2 tuần) để đủ thời gian cho 2 phase × 2 quỹ. Mỗi ngày trì hoãn ăn thẳng vào đệm.

**Kết luận (theo house rule — flag chứ không hợp lý hoá):** track dữ liệu/kỷ luật **đúng hoặc trên nhịp**; track challenge **chậm rõ và là rủi ro #1**. Chưa "báo động đỏ" ở mốc 179 ngày, nhưng thế "0 bước Giai đoạn 0 sau 19 ngày" phải được phá tuần tới.

## 🎯 6. Trọng tâm tuần tới (2026-W29) — ưu tiên nợ cũ nhất trước

1. **[Nợ 19 ngày — ưu tiên tuyệt đối] Lập bảng lot size 0,5%/1% cho tài khoản 10K$** (50$/100$ mỗi lệnh; pip value & lot cho NQ/NDX, EURUSD, GBPUSD, XAUUSD; The5ers thêm cột ngưỡng "ngày có lãi = +50$"). Xong → **log 1 dòng thật** vào cả [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]] để phá thế đứng yên.
2. **Sửa nhãn `phase`** trong 2 goal challenge: `"Phase 4 - Challenge"` → `"Phase 0 - Preparation"` (1 dòng frontmatter/file).
3. **Tick cột mốc đã dư bằng chứng** (Khang tự chấm): Journaling #1, Cut-top-3 #1+#2 → rồi chỉnh `progress` cho khớp cột mốc, xoá bớt mismatch.
4. **Đa dạng thị trường backtest:** log ≥1 backtest NAS100/GBPUSD/XAUUSD để phá thế 11/11 EURUSD.
5. **Vá dữ liệu vụn:** đối chiếu note backtest 07-11 với summary 07-11; tạo note `[[Mistake - Vào lệnh sai Kill Zone]]`; đồng bộ `baseline` (Backtest sample & Master 2022 → 11).

*(Tuần này **0 lệnh live** → KHÔNG cần chạy [[Weekly_Trading_Review_ICT_Obsidian|Weekly Trading Review]] đầy đủ — vẫn đúng phạm vi Giai đoạn 1. Chỉ chạy review nặng đó khi có khối lượng lệnh live thật.)*

## 📋 Đề xuất cập nhật (dán tay vào file gốc — KHÔNG tự sửa file có Dataview)

> [!tip] `02 - Skill Metrics.md` — dòng W28 ĐÃ được Khang điền sẵn
> Bảng tuần hiện đã có: `| 2026-W28 | 10 | (trống) | 3 | 4 | Tuần đầu bắt đầu tập trung học tập và backtest |`.
> Gợi ý tinh chỉnh nhẹ (không bắt buộc):
> - Cột **"Lỗi top-3 (số lần)"** đang trống → nên ghi **0** (không có lệnh live nào trong tuần; mọi lỗi đều trong backtest, không tính vào tần suất live).
> - Cột **"Backtest trong tuần" = 10** khớp số note file thật trong tuần (07-06→07-11); lưu ý tổng frontmatter Daily Summary là 9 do 07-11 ghi 0 (xem Cảnh báo #4).

**[[Build a statistically validated backtest sample]] → Nhật ký tiến độ** — thêm dòng (bắt được backtest 07-11 chưa log):
```
| 2026-07-12 | 6 | Chốt tuần W28: +1 backtest thật 07-11 (EURUSD Long 2013-11-21, Win) → tổng 11/200 = 5,5%; nhịp ~0,58/ngày trên nhịp cần ~0,54. ⚠️ Summary 07-11 ghi 0 backtest — cần đối chiếu. ⚠️ baseline frontmatter còn "6", nên bump 11. Mẫu 11/11 EURUSD. Cột mốc "50 backtest" vẫn 0/4. |
```

**[[Master the ICT 2022 Model]] → Nhật ký tiến độ** — thêm dòng:
```
| 2026-07-12 | 30 | Chốt tuần W28: 11 setup 2022-model (≈9W/2L). +1 setup 07-11 (EURUSD Long 2013-11-21, Win, đủ chuỗi Sweep→Displacement→MSS→FVG). Nhịp số lượng trên chuẩn nhưng n=11 chưa kết luận được win rate >55%. baseline frontmatter còn "5" → bump 11. Checklist vào/ra lệnh (cột mốc #1) vẫn chưa viết. Cột mốc "50 setup" vẫn 0/5. |
```

**[[Hold daily journaling and process discipline]] → Nhật ký tiến độ** — thêm dòng chốt tuần:
```
| 2026-07-12 | 40 | Chốt tuần W28: 6/7 ngày có Daily Summary (07-06→07-11; 07-12 chưa có), chuỗi journaling 7 ngày liên tiếp. Cột mốc #1 dư bằng chứng để tick — progress 40% ghi tay vẫn chưa khớp cột mốc 0/4 (0%). |
```

*(KHÔNG đề xuất dòng cho FTMO, The5ers, Cut-top-3: không có chuyển động thật trong tuần → thêm dòng sẽ là dòng rỗng. Cách xoá nợ đẹp nhất cho FTMO/The5ers là làm bảng lot size rồi mới log — xem Trọng tâm #1.)*

## 🔗 Nguồn dữ liệu đã đọc

- `00 - Inbox/02 - Daily Summary/2026-07-06 … 2026-07-11 - Daily summary.md` (6 file)
- `00 - Inbox/01 - Daily Tasks/2026-07-06 … 2026-07-12 tasks.md` (đối chiếu, 7 file)
- `00 - Inbox/03 - Weekly Summary/2026-07 W27 - Weekly summary.md` (mẫu định dạng tuần trước)
- 6 goal file: FTMO, The5ers, Build a statistically validated backtest sample, Master the ICT 2022 Model, Cut my top 3 repeated mistakes, Hold daily journaling and process discipline
- `09 - Goal Tracking/01 - Roadmap.md`, `09 - Goal Tracking/02 - Skill Metrics.md`
- `04 - Backtesting/` (đếm trực tiếp: 11 note; 2026-07-11 nay có 1 note — mâu thuẫn với summary 07-11)
- `02 - Trading Knowledge/Concepts/` (đếm status: 50 note — 17 seed / 28 developing / 5 tested / 0 mastered)
- `06 - Mistake Database/` (xác nhận 3 note top-3 có nội dung: 244/280/287 dòng; note "Vào lệnh sai Kill Zone" chưa tồn tại)
- `05 - Live Trading Journal/Trades/` (xác nhận 0 lệnh live trong tuần)

## 🔗 Liên kết

[[00 - Goal Dashboard]] · [[01 - Roadmap]] · [[02 - Skill Metrics]] · [[_Backtest Dashboard]] · [[02 - Mistake Frequency Dashboard]] · [[03 - Performance Dashboard]] · [[04 - Process Quality Dashboard]]
