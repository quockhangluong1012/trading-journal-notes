---
type: daily-summary
date: 2026-07-10
days_to_prop_exam: 181
exam_target: 2027-01-07
backtests_logged: 3
trades_logged: 0
concepts_reviewed: 1
mistakes_triggered:
  - "08 - Mistake - Weak Displacement"
  - "Vào lệnh sai Kill Zone (chưa có note riêng trong Mistake Database)"
net_r_today: 4.94
tags:
  - daily-summary
  - prop-firm-prep
---

# 🌙 Daily Summary — 2026-07-10

> [!info] Đếm ngược & chủ đề
> - **181 ngày** còn lại tới mốc tự đặt **2027-01-07** (song song **FTMO 10K$** + **The5ers High Stakes 10K$** — hai track độc lập, KHÔNG gộp luật).
> - **Giai đoạn hiện tại:** Giai đoạn 1 — Nền tảng ([[01 - Roadmap]]) — trọng tâm dữ liệu sạch + kỷ luật ghi chép.
> - **Chủ đề của ngày:** *Ngày bứt phá chất lượng, không phải ngày trả nợ.* Log **3 backtest** (đưa tổng 7→10, lần đầu **vượt nhịp cần** cho cả 2 goal đếm số), và **lần đầu tiên có 1 concept lên `tested`** (CE) — phá nút thắt "0 tested" kéo dài. Nhưng khối **nợ ghi chép** (W27, 2 nhãn phase, bảng lot size) hầu như còn nguyên: chỉ xoá được 1/5 khoản mà sáng nay đặt mục tiêu ≥3/5.

> [!warning] Cảnh báo — các khoản còn treo (cụ thể, có tên)
> 1. **Track challenge đứng yên 17 ngày & nhãn phase sai.** [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]]: dòng "Nhật ký tiến độ" gần nhất vẫn **2026-06-23** (17 ngày > ngưỡng 3), cột mốc **0/8**, `phase` vẫn ghi **"Phase 4 - Challenge"** trong khi thực tế là **Giai đoạn 0 — Chuẩn bị** (chưa mua gói). **Chưa chạm bước Giai đoạn 0 nào.** Với 181 ngày còn lại, đây là **rủi ro tiến độ số 1** — không phải số lượng backtest.
> 2. **Skill Metrics còn 1 dòng duy nhất `2026-W26` (để trống).** W27 (kết thúc 07-05) trễ **5 ngày**, W28 (đang dở) cũng chưa có dòng. Dòng W27 đã soạn sẵn trong [[2026-07 W27 - Weekly summary]] — chỉ cần tự chấm 2 điểm (1–5) rồi dán. Nợ này đã nêu ≥3 ngày.
> 3. **Bảng lot size 0,5%/1% cho tài khoản 10K$ (bước #3 của cả 2 goal challenge) chưa làm** — đây là bước Giai đoạn 0 rẻ nhất để xoá nợ #1.
> 4. **22 ngày chưa có lệnh live** (gần nhất 2026-06-18, `Loss - 01 - Trade 2026-06-18 NDX Short`). *Chấp nhận được* trong Giai đoạn 1 (ưu tiên backtest/journaling) — ghi nhận để không quên execution live vẫn là ẩn số, KHÔNG coi là thất bại của ngày.

## 📚 Học hôm nay

- ✅ **[[10 - Consequent Encroachment (Mean Threshold)]] → `status: tested`** (last_reviewed 2026-07-10). **Đây là concept ĐẦU TIÊN trong toàn vault lên mức `tested`** (trước hôm nay: 0 tested / 49 concept). Bằng chứng kiểm chứng đến trực tiếp từ backtest: cả 3 lệnh hôm nay đều dùng **CE của FVG/BPR/Unicorn** làm mốc entry (BT1 entry tại CE Unicorn H1; BT3 entry tại CE FVG nhịp đẩy). Việc này **phá nút thắt chất lượng dài hạn** mà các daily summary trước liên tục cảnh báo ("0 concept được kiểm chứng qua backtest").
- **Tình trạng concept sau hôm nay:** 49 note — **18 seed, 30 developing, 1 tested, 0 mastered** (developing 31→30, tested 0→1 so với hôm qua = đúng 1 concept dịch chuyển developing→tested).
- ⚠️ **Lưu ý trung thực về checkbox học:** file task sáng tick cả [[35 - Aggressive Displacement Entry]] và [[42 - SMT Divergence]], nhưng frontmatter 2 note này vẫn `last_reviewed: 2026-07-09` (không đổi hôm nay) → **không có bằng chứng ôn hôm nay**. Chỉ tính **1 concept có bằng chứng thật** (CE). Đây là dạng overtick cần để ý (đã gặp ở 07-06).

## 📊 Backtest hôm nay

**3 backtest mới** trong `04 - Backtesting/2026-07-10/` — tất cả EURUSD, ICT 2022 Model, khung entry M5.

### BT1 — `01 - Win - EURUSD - 2021-05-03 - Short` · Grade A · +3.075R · followed_plan **Yes**
- **Bias:** Bearish, `bias_correct: Yes`. HTF D1 giảm (LH/LL), pullback chưa phá protected high → giữ bias.
- **Chuỗi entry:** ✅ đủ và đúng thứ tự — Liquidity Sweep (quét ra ngoài cạnh trên **Unicorn** = Breaker ⊕ FVG, trong **Premium**) → reject đóng lại trong vùng → M5 Displacement + FVG + MSS → retrace CE FVG M5 → Entry. **Không mắt xích nào gãy.**
- **SL/TP & R:** SL trên điểm sweep (1.20764 = invalidation thật, không phải "đặt cho R đẹp"), blended 3.07R (partial ~2.1R + runner tới EQL). Kế hoạch = kết quả.
- **Tâm lý:** ghi nhận "còn hơi sợ khi giá quét lên FVG thêm 2 nhịp" → root cause tự chẩn: **thiếu tiêu chí trigger objective** (wick hay close? mấy nến xác nhận?).
- **Bài học:** lệnh **process A-grade** — thắng vì *quy trình*, và **đã sửa được lỗi FOMO cũ** (không vào tại CE lần chạm đầu). Cần đóng gói hành vi này thành rule định lượng.

### BT2 — `02 - Loss - EURUSD - 2021-05-07 - Short` · Grade C/D · −1R · followed_plan **No**
- **Bias:** Bearish, `bias_correct: Yes` — **nhưng đây chính là cái bẫy.** Bias đúng ≠ thời điểm entry đúng.
- **Mắt xích gãy:** ❌ **KHÔNG ở Kill Zone** (vào lúc Asia, 10:05 UTC+7). Section 3 để trống ô Kill Zone nhưng Section 2 vẫn tick `[x]` mục "Entry trong Kill Zone" → **hai mục tự mâu thuẫn trong cùng file**. ❌ Displacement yếu ("nến không quá lớn", tự ghi 2 lần) = [[08 - Mistake - Weak Displacement]]. ❌ Đứng **sai phía liquidity gần nhất**: buy-side chưa bị lấy (OB 1.21296–1.21227) nằm **cùng phía SL** → giá nhử short vào rồi chạy lên quét SL trước.
- **Root cause (tự chẩn, đúng):** lỗi **quy trình** (thiếu Kill Zone gate + nhầm HTF bias với short-term draw on liquidity) — **KHÔNG phải lỗi tâm lý**. File đã tự sửa dòng "cải thiện tâm lý" thành "thêm 4-gate pre-trade checklist".
- **Hygiene:** file tự đánh dấu lệnh này **`invalid-out-of-KZ`, KHÔNG tính vào cohort đo edge** — đây là kỷ luật thống kê rất tốt.
- ⚠️ **Data-integrity trong chính file:** `grade` frontmatter **C** vs bảng Summary **D**; `trade_date` 2021-05-07 nhưng heading/bảng ghi 2021-05-03 và phần Phân Tích ghi nhầm năm 2026. Cần đồng bộ (đưa vào việc ngày mai).

### BT3 — `03 - Win - EURUSD - 2021-07-22 - Long` · Grade B · +2.86R · followed_plan **No**
- **Bias:** Bullish, `bias_correct: Yes`. BOS bullish D1, chờ pullback về **Discount** (FVG H1) đúng vị trí.
- **Chuỗi entry:** ✅ đủ — Sweep old lows + 50% FVG H1 → Displacement + MSS → FVG M5 → retrace entry, đúng **NY KillZone** (19:10). Fractal refinement HTF→LTF chuẩn.
- **Nghịch lý `followed_plan: No`:** nội dung lại ghi "chờ đủ điều kiện: Có" và mọi checklist đều tick → cần thống nhất Yes/No.
- ⚠️ **Data-integrity:** tên file/heading ghi "Short"/"2005-05-02" nhưng thực tế là **Long / 2021-07-22** (frontmatter `position: Long` mới đúng; SL<entry<TP xác nhận Long). Mô tả "SL cạnh dưới FVG H1" lệch số (SL 1.17698 thực chất dưới **sweep low M5**).
- **Bài học lớn nhất tự rút:** "chờ ~2–3 tháng mới có 1 setup đẹp" → **selection/hindsight bias** + tần suất mẫu quá thấp nếu chỉ chạy 1 symbol/1 thời kỳ → cần **backtest song song nhiều symbol** (NAS100, GBPUSD, XAUUSD) để đạt sample size trước mốc.

### Tổng hợp ngày
- **Số lượng:** 3 backtest · **2 Win / 1 Loss / 0 BE**.
- **Net R (thô):** +3.075 − 1 + 2.86 = **+4.94R**.
- **Net R (cohort hợp lệ, loại BT2 out-of-KZ theo rule của chính file):** +3.075 + 2.86 = **+5.94R trên 2 lệnh hợp lệ**.
- **Chất lượng execution:** trending **tốt hơn** — nối tiếp mạch Grade A của 07-09; điểm âm BT2 là *lỗi quy trình đã được chẩn đúng gốc* (không đổ cho tâm lý), đúng tinh thần "good loss > bad win".
- **Chuỗi backtest:** **5 ngày liên tiếp** (07-06 → 07-10) — **dài nhất từ trước tới nay**.
- **Mẫu 2022 Model:** 10 setup — **8 Win / 2 Loss = 80%** (hoặc 8W/1L ≈ 89% nếu loại BT2 out-of-KZ). `n=10` vẫn **quá nhỏ** để kết luận edge; ràng buộc thật vẫn là **win rate >55% trên mẫu đủ lớn**.
- ⚠️ **Mẫu lệch symbol:** 9/10 note là EURUSD. Cần thêm NAS100/GBPUSD/XAUUSD để mẫu không thiên vị 1 thị trường.

## 💹 Live Trade hôm nay

**Không có lệnh live nào được log hôm nay.** Gần nhất vẫn là 2026-06-18 (`Loss - 01 - Trade 2026-06-18 NDX Short`) → **22 ngày**. Chấp nhận được trong Giai đoạn 1 (ưu tiên backtest + journaling, KHÔNG ưu tiên số lượng lệnh live), nhưng ghi nhận rõ: **execution live dưới áp lực vẫn là ẩn số chưa được kiểm chứng** cho mục tiêu funded.

## 🧠 Phân tích lỗi & tâm lý

Lỗi kích hoạt hôm nay đều nằm trong **BT2** (là backtest, **không** phải live → **không** làm đổi số đếm trong [[02 - Mistake Frequency Dashboard]]):

- **[[08 - Mistake - Weak Displacement]]** (đã có note): vào lệnh dù tự ghi "nến displacement không quá lớn" tới 2 lần. Định nghĩa lỗi: hợp lý hoá một nhịp đẩy yếu (không đạt ngưỡng ATR, không phá cấu trúc dứt khoát) thành "displacement hợp lệ" → mất dấu hiệu dòng lệnh tổ chức thật.
- **Vào lệnh sai Kill Zone** (⚠️ **chưa có note riêng** trong `06 - Mistake Database`): vào phiên Asia thanh khoản mỏng cho một mô hình *phụ thuộc Kill Zone*. → **Đề xuất tạo `[[Mistake - Vào lệnh sai Kill Zone]]`** để dashboard bắt được tần suất.
- **Lỗi nhận thức (cognitive, chưa cataloged):** nhầm **HTF bias** với **short-term draw on liquidity** — short đúng hướng dài hạn nhưng đứng sai phía liquidity chưa-bị-lấy gần nhất. Đây là bài học sâu nhất của ngày; nên cân nhắc thành một mục checklist ("liquidity chưa-bị-lấy gần nhất nằm phía nào so với entry?").

**Đối chiếu top-3 lỗi hiện tại** ([[06 - Mistake - Not Have Market Structure Shift]] 14 · [[09 - Mistake - Wrong daily bias]] 7 · [[07 - Mistake - Risk more than 0.5% total account]] 5): **không lỗi nào trong top-3 tái phát hôm nay** (BT2 có MSS, bias đúng, và là backtest nên không dính rủi ro vốn). Lỗi Weak Displacement + Kill Zone **không thuộc** top-3 → không kích hoạt cảnh báo top-3.

## 🎯 Đối chiếu mục tiêu

Ngày mốc: **2027-01-07** → còn **181 ngày**.

| Goal | progress (fm) | Cột mốc | Log gần nhất trước hôm nay | Số thật hôm nay | Nhận định |
|---|---|---|---|---|---|
| [[Pass FTMO first package challenge (10K$)]] | 0% | 0/8 | **2026-06-23 (17 ngày)** | không đổi | **Behind** — chưa chạm bước Giai đoạn 0; nhãn `phase` sai ("Phase 4"). |
| [[Pass The5er first package challenge (10k$)]] | 0% | 0/8 | **2026-06-23 (17 ngày)** | không đổi | **Behind** — như trên. |
| [[Build a statistically validated backtest sample]] | 6% | 0/4 | 2026-07-09 | **10/200 backtest** | **On track (số lượng)** — xem pace dưới. |
| [[Master the ICT 2022 Model]] | 30% | 0/5 | 2026-07-09 | **10/100 setup, 80% win** | **On track (số lượng)**, ràng buộc thật = win rate/mẫu lớn. |
| [[Hold daily journaling and process discipline]] | 40% | 0/4 | 2026-07-09 | **summary #7, 6 ngày liên tiếp** | Thói quen bền; cột mốc #1 đủ bằng chứng tick (để Khang tự chấm). |
| [[Cut my top 3 repeated mistakes]] | 20% | 0/4 | 2026-07-08 | live không đổi | Đứng yên hợp lệ (không có lệnh live). |

**Mismatch cần nêu rõ (progress fm vs cột mốc thực):**
- FTMO & The5ers: `progress 0` khớp cột mốc 0/8 — nhưng `phase: "Phase 4 - Challenge"` **sai sự thật** (đang Giai đoạn 0, chưa mua gói).
- [[Master the ICT 2022 Model]]: `progress 30%` nhưng **cột mốc 0/5** → 30% là ghi tay, chưa khớp cột mốc (thực = 0%).
- [[Hold daily journaling...]]: `progress 40%` nhưng **cột mốc 0/4** (thực = 0%); cột mốc #1 đã đủ bằng chứng.
- [[Cut my top 3...]]: `progress 20%` nhưng **cột mốc 0/4** (thực = 0%); cột mốc #1+#2 đã đủ bằng chứng.
- [[Build a statistically validated backtest sample]]: `progress 6%` gần khớp 10/200 = 5%; **cột mốc 0/4** (50 backtest chưa đạt).

**Pace verdict (số cụ thể, không cảm tính):**
- **Backtest count:** 10/200. Nhịp thực tế **10/17 ngày ≈ 0,588/ngày** (từ 2026-06-23). Nhịp cần: 190 còn lại / 355 ngày tới due 2027-06-30 ≈ **0,54/ngày**. → **Lần đầu tiên VƯỢT nhịp cần** (07-09 còn chậm 1,23×; 3 backtest hôm nay đẩy qua ngưỡng).
- **Master 2022 setup:** 10/100. Nhịp cần: 90 / 264 ngày tới due 2027-03-31 ≈ **0,34/ngày** < nhịp thực 0,588 → **trên nhịp về số lượng.** ⚠️ Nhưng ràng buộc thật là **win rate >55% trên mẫu đủ lớn** — n=10 chưa đủ.
- **Track challenge:** **behind rõ** — 181 ngày còn lại tới 2027-01-07, đã 17 ngày không có bước Giai đoạn 0 nào. Đây là chỗ pace math nói "chậm", không phải backtest.

## 📈 Cập nhật Nhật ký tiến độ

Đã **edit trực tiếp** và thêm 1 dòng cho các goal có chuyển động thật hôm nay:

- ✅ **[[Build a statistically validated backtest sample]]** — thêm dòng 2026-07-10: +3 backtest, tổng **10/200 = 5%**, chuỗi ngày thứ 5, nhịp vượt ngưỡng. Đồng thời **sync prose** "Hiện tại: 7 backtest" → **"10 backtest"** (số thực sau hôm nay).
- ✅ **[[Master the ICT 2022 Model]]** — thêm dòng 2026-07-10: +3 setup, tổng **10/100 = 10%**, mẫu 8W/2L. Đồng thời **sync prose** "Hiện tại: ~6 setup" → **"10 setup"**.
- ✅ **[[Hold daily journaling and process discipline]]** — thêm dòng 2026-07-10: daily summary #7, **6 ngày journaling liên tiếp** (07-05→07-10) + 5 ngày backtest liên tiếp.

**KHÔNG thêm dòng (nêu lý do):**
- [[Cut my top 3 repeated mistakes]]: không có lệnh live → tần suất lỗi top-3 (đo trên trade live) **không đổi**; thêm dòng sẽ là dòng rỗng.
- [[Pass FTMO...]] & [[Pass The5er...]]: **chưa làm bước Giai đoạn 0 nào** hôm nay → không có số thật để log; cố tình **không** thêm dòng "vẫn 0%" (giữ cảnh báo 17 ngày trung thực).

> [!note] Việc KHÔNG tự làm thay (để giữ vòng accountability)
> Không tự tick cột mốc và không tự sửa `progress %` (Khang tự chấm). Không tự dán W27, không tự sửa 2 nhãn `phase`, không tự lập bảng lot size — đây là **nợ tự tay** để tuần tự xoá, đã liệt kê ở Cảnh báo & Việc ngày mai.

## 🔭 Việc cần làm ngày mai

1. **Xoá nợ challenge (ưu tiên #1):** lập **bảng lot size 0,5% & 1% cho tài khoản 10K$** (bước #3 dùng chung cho CẢ HAI goal), rồi log 1 dòng "Nhật ký tiến độ" **nội dung thật** vào [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]] — xoá mốc 17 ngày. *(Nhớ phân biệt: FTMO daily loss reset từ balance gốc, ≥4 ngày giao dịch; The5ers daily drawdown từ equity đóng cửa hôm trước, ≥3 ngày lãi ≥0,5% — bảng dùng chung, ngưỡng "ngày có lãi" chỉ cho The5ers.)*
2. **Sửa 2 nhãn `phase: "Phase 4 - Challenge"` → "Giai đoạn 0 — Chuẩn bị"** trong 2 goal challenge (1 dòng frontmatter mỗi file).
3. **Dán dòng W27** (đã soạn trong [[2026-07 W27 - Weekly summary]]) vào [[02 - Skill Metrics]]; cân nhắc thêm dòng W28. Tự chấm Chất lượng quy trình + Kỷ luật (1–5).
4. **Data-integrity 2 backtest hôm nay:** BT2 đồng bộ `grade` (C↔D) + `trade_date`/năm trong body; BT3 sửa tên file/heading "Short/2005" → "Long/2021" và thống nhất `followed_plan`.
5. **Tạo `[[Mistake - Vào lệnh sai Kill Zone]]`** trong Mistake Database để bắt tần suất lỗi Kill Zone (BT2 hôm nay).
6. **Backtest ngày 6:** giữ chuỗi + **đổi symbol** (NAS100 hoặc GBPUSD/XAUUSD) để giảm lệch mẫu EURUSD 9/10; áp 4-gate pre-trade (Session → Draw → Location/OTE → Signal-quality) mà BT2 đã rút ra.
7. **Tự chấm cột mốc đã đủ bằng chứng** (Khang tự tick, không tự tick giùm): [[Hold daily journaling...]] #1, [[Cut my top 3...]] #1+#2, rồi chỉnh `progress %` cho khớp cột mốc.

## 🔗 Liên kết

[[00 - Goal Dashboard]] · [[01 - Roadmap]] · [[02 - Skill Metrics]] · [[_Backtest Dashboard]] · [[02 - Mistake Frequency Dashboard]] · [[03 - Performance Dashboard]] · [[04 - Process Quality Dashboard]]
