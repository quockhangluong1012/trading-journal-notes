---
date: 2026-04-23
symbol: NDX
position: Long
result: Win
session: London
setup: NQ ICT 2022 AM Delivery
entry_model: Change of Character + Liquidity Sweep/Stop Hunt + Fair Value Gap
entry_timeframe: 
higher_timeframe_bias: 
bias_correct: 
entry_price: 26,799.6
take_profit: 26,990
stop_loss: 26,708.7
exit_price: 26,799.6
pnl: 191.4
r_multiple:
planned_rr: 2.09
risk_percent: 
confidence: 4
mistakes: 
emotions:
  - Disciplined
tags:
  - ChangeOfCharacter
  - LiquiditySweepStopHunt
  - FairValueGap
  - KillZones
  - PremiumVsDiscount
  - JudasSwing
  - DailyBias
source_id: 2009
da_verdict: SURVIVES, WEAKENED
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 1, minor: 1}
da_opposite_case: "undecidable from this evidence"
---
# Trade 2026-04-23 - NDX Long Win

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Win |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Change of Character + Liquidity Sweep/Stop Hunt + Fair Value Gap |
| HTF Bias |  |
| Premium/Discount |  |
| Power of 3 |  |
| Confidence | 4/5 (High) |
| Entry | 26,799.6 |
| Stop Loss | 26,708.7 |
| Take Profit | 26,990 |
| Exit | 26,799.6 |
| PnL | 191.4 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-04-23 00:16:51 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: N/A
- **Premium/Discount**: N/A
- **Power of 3 Phase**: N/A

================ D1 ================

- Daily bias: Bullish
- Vẫn đang trong trend tăng mạnh
================ H1 ================

- Hình thành FVG khi giá di chuyển
- FVG nằm trong vùng Discount
- Giá giảm mạnh trong phiên Asia và phục hồi nhẹ đầu phiên London
- Chờ Judas Swing xảy ra trong phiên London. Judas swing hình thành lúc 16:00 quét xuống FVG
================ M15 ================

- Xuống khung M15, giá quét qua 50% FVG sau đó rút râu và đóng nến trên 50% sau đó giá đảo chiều với nến xanh tăng mạnh
================ M5 ================

- Giá tăng mạnh tạo displacement + FVG trên khung nhỏ
- Chờ giá retrace về FVG khung nhỏ và tạo tín hiệu rejection => entry long
- Target: đỉnh cũ + buffer (26,990.0)
- Stop loss: đặt dưới đáy đã bị quét trước đó (26,708.7)
- Tỷ lệ RR: 1:2.09

### Charts

![[NDX-20260423-2009-1.png]]
![[NDX-20260423-2009-2.png]]
![[NDX-20260423-2009-3.png]]
![[NDX-20260423-2009-4.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Clear liquidity target identified (buy-side or sell-side)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Partial take-profit levels are planned (1R, 2R, runner)
- [x] Not exceeding daily loss limit -- will stop trading if hit
- [x] Market Structure Shift + Displacement
- [x] Break of Structure (BOS) or Change of Character (CHOCH) confirmed
- [x] Rejection Validation When Enter PD Array Zones

---

## 3. Execution Review

Giá đi đúng theo chiến lược ban đầu, sau đó đảo chiều xuống Order block bên dưới

**Emotions**: Disciplined

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit) *(mâu thuẫn dữ kiện — xem O1: exit_price field = entry_price field = 26,799.6, không khớp cả TP 26,990 lẫn nội dung Execution Review "đảo chiều xuống Order block bên dưới")*
- **Mistake chính**:
  - [[Mistake - ]] *(trống)*
- **Nguyên nhân gốc rễ** *(suy luận có điều kiện — cần chart xác nhận, và cần sửa lỗi field exit_price trước)*:
  - Execution Review mô tả "giá đi đúng theo chiến lược ban đầu, sau đó đảo chiều xuống Order block bên dưới" — câu này mô tả một lệnh đã đạt được phần nào mục tiêu (đi đúng chiến lược) rồi *sau đó* đảo chiều, gợi ý một partial-TP hoặc trailing-stop đã chốt lời một phần trước khi giá quay đầu — nhưng không trường nào trong file xác nhận cơ chế chốt lời cụ thể này. PnL 191.4 gần khớp full reward kế hoạch (190.4, xem O1), mâu thuẫn với việc "đảo chiều" nếu đảo chiều xảy ra trước khi đạt TP.

---

## 5. Lesson Learned

**Bài học kỹ thuật** (liên kết O1)
- File này có lỗi field nghiêm trọng nhất trong 5 file batch: `exit_price` (26,799.6) trùng khớp tuyệt đối với `entry_price` (26,799.6) — về mặt số học, nếu đúng vậy thì r_multiple thực nhận phải bằng 0 và PnL phải bằng 0, nhưng PnL field ghi 191.4 (gần khớp full reward kế hoạch 190.4). Đây là một lỗi ghi log field, không phải một đặc điểm thật của lệnh.
- Execution Review viết "sau đó đảo chiều xuống Order block bên dưới" — câu này không khớp rõ với nhãn "Win (Hit Take Profit)": nếu giá đảo chiều xuống OB sau khi đạt một phần chiến lược, cần biết liệu TP đã bị hit *trước* khi đảo chiều hay lệnh đã đóng bằng cách khác.

**Bài học tâm lý**
- Execution Review không mô tả cảm xúc trong quá trình giữ lệnh, chỉ mô tả price action sau khi đóng — thiếu góc nhìn tâm lý để đối chiếu với emotions field "Disciplined".

**Bài học quy trình & risk**
- Đây là lỗi ghi log field nghiêm trọng cần sửa trước khi dùng file này cho bất kỳ thống kê cross-setup nào (win-rate, expectancy) — nếu `exit_price` sai, mọi phép tính r_multiple thực nhận dựa trên field này sẽ sai theo.

**Rule cần thêm/cập nhật**
- Rule kiểm tra được: `exit_price` không được để bằng `entry_price` khi `pnl` ≠ 0 — validation tự động này sẽ bắt được lỗi cụ thể của file này ngay khi ghi log, thay vì phải soi lại sau (liên kết O1).
- Rule kiểm tra được: khi Execution Review mô tả "đảo chiều" sau khi đạt mục tiêu, phải ghi rõ giá đảo chiều xảy ra *trước hay sau* mức TP/mức chốt lời — câu văn hiện tại mơ hồ về trình tự thời gian.

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, 4 chart Obsidian không đọc được. Sufficiency: **thin** — và load-bearing claim ở đây không phải là chất lượng setup (MSS/FVG) mà là **liệu dữ kiện số của chính file có tự nhất quán hay không** — vấn đề này kiểm được độc lập với chart, chỉ cần đối chiếu field với field.

**Thesis & claims**:
- C1: D1 bias bullish, trend tăng mạnh.
- C2: H1 — FVG hình thành trong vùng Discount; Judas Swing 16:00 quét xuống FVG.
- C3: M15 — giá quét 50% FVG, rút râu, đóng nến trên 50%, đảo chiều tăng mạnh.
- C4 (load-bearing, thuộc thesis kỹ thuật): M5 — displacement + FVG nhỏ, entry long tại rejection retest FVG (26,799.6), target đỉnh cũ+buffer (26,990), SL dưới đáy bị quét (26,708.7).
- C5 (load-bearing, thuộc tính toàn vẹn dữ kiện — carve-out ưu tiên vì đây là lỗi arithmetic cơ bản): exit_price = 26,799.6 (= entry_price) VÀ pnl = 191.4 VÀ Result = "Win (Hit TP)" — ba giá trị này không thể cùng đúng.
- Suy luận: C1+C2+C3 → C4 (entry hợp lệ theo mô tả) → kỳ vọng Win nếu target đạt — nhưng C5 chặn mọi suy luận tiếp: không biết chắc giá thực đã đi tới đâu.

**Điều gì đứng vững**:
- Chuỗi lý luận D1→H1→M15→M5 có cấu trúc và mức độ chi tiết tương đương 04-20 (đều nêu giá cụ thể cho target, SL, và các mức FVG/Judas Swing theo giờ) — về mặt narrative, đây là một trong những thesis mô tả đầy đủ nhất trong batch.
- Arithmetic RR kế hoạch: risk = |26,799.6−26,708.7| = 90.9; reward = |26,990−26,799.6| = 190.4; RR = 190.4/90.9 = 2.095 ≈ planned_rr field 2.09 và câu văn "Tỷ lệ RR: 1:2.09" trong mục 1 — ba nguồn (arithmetic, field, văn bản) khớp nhau hoàn toàn. Đây là điểm mạnh thật: không giống 04-02 nơi có câu văn "RR: 1:2" sai với field (theo CS-O6), ở đây không có mâu thuẫn nào giữa RR văn bản và RR field.
- PnL 191.4 gần khớp reward kế hoạch 190.4 (chênh 1.0, có thể do spread/phí hoặc TP thực tế 26,991 thay vì 26,990) — nghĩa là nhiều khả năng lệnh **đã Hit TP thật**, chỉ có field `exit_price` bị ghi nhầm thành entry_price.

**Objections**:

**O1 · [ARITHMETIC] · fatal · attacks C5 (load-bearing về tính toàn vẹn dữ kiện)**
Claim: `exit_price: 26,799.6` (khớp tuyệt đối `entry_price: 26,799.6`).
Fails: nếu exit_price = entry_price, r_multiple thực nhận phải = 0 và pnl phải = 0 (không tính phí) — nhưng pnl field = 191.4, một giá trị dương gần khớp chính xác với reward kế hoạch (190.4, chênh 1.0 điểm) theo tính toán risk/reward ở trên. Đây không phải làm tròn (chênh 0 điểm nếu exit=entry, không phải chênh nhỏ như rounding) — đây là hai giá trị hoàn toàn khác cấu trúc: một nói "không di chuyển" (exit=entry), một nói "đạt gần đúng full target" (pnl≈reward kế hoạch).
Evidence: entry_price=26,799.6, exit_price=26,799.6 (chênh=0); pnl=191.4; reward kế hoạch tính từ TP−entry=190.4; nếu exit thật = TP = 26,990, thì pnl_theoretical=190.4≈191.4 field (chênh 1.0, hợp lý do spread/phí) — khớp hơn nhiều so với giả thuyết exit=entry (chênh 191.4).
Consequence: `exit_price` là field sai, gần như chắc chắn phải là 26,990 (hoặc gần đó) chứ không phải 26,799.6. Điều này không đổi Result (Win vẫn đúng vì pnl dương và gần khớp full reward), nhưng làm mọi phép tính r_multiple thực nhận dựa trên exit_price field (nếu có agent nào tính sau) sẽ ra sai số 0 thay vì ~2.1R thật.
Your best answer: "Chỉ là lỗi copy-paste field, không ảnh hưởng kết luận Win/Loss." — Đúng một phần (Result label không đổi), nhưng không cứu được: nếu dùng đúng lý luận "outcome không đổi nên lỗi field không quan trọng", đây chính là kiểu suy luận outcome-as-evidence mà brief yêu cầu tránh — lỗi field integrity phải được sửa độc lập với việc nó "tình cờ" không đổi outcome.
Retracted by: một giá trị exit_price khác (ví dụ 26,990 hoặc 26,991) xác nhận từ nguồn khác (broker log, chart) — hiện chỉ suy luận được từ arithmetic pnl, không có xác nhận độc lập.

**O2 · [SELF-CONTRADICTION] · material · attacks C4**
Claim: Result = "Win (Hit Take Profit)" ngụ ý giá đạt đúng 26,990 và giữ đó làm exit.
Fails: Execution Review viết "Giá đi đúng theo chiến lược ban đầu, **sau đó đảo chiều xuống Order block bên dưới**" — câu "sau đó đảo chiều xuống" gợi ý giá đã quay đầu giảm *sau* khi đạt (một phần) mục tiêu, không đơn giản là "hit TP và dừng ở đó". Nếu giá đảo chiều xuống OB sau khi đạt gần TP, cần biết liệu lệnh đã đóng *trước khi* đảo chiều (đúng lúc hit TP, may mắn về timing) hay đóng bằng một cơ chế khác (trailing stop, manual) khi giá đang trên đường đảo chiều.
Evidence: câu Execution Review nguyên văn, đối chiếu với nhãn "Hit Take Profit" ở mục 4.
Consequence: không rõ đây là một TP hit sạch (giá chạm đúng 26,990 rồi lệnh đóng tự động) hay một manual/trailing exit gần đỉnh trước khi giá đảo chiều — hai kịch bản này có ý nghĩa khác nhau cho việc đánh giá "target đã được xác định đúng chuẩn" (TP hit sạch ủng hộ target-setting tốt hơn manual exit gần đỉnh do phản xạ).
Your best answer: "PnL 191.4 gần khớp full reward 190.4 nên chắc chắn là Hit TP sạch." — Có sức nặng (đây là lý do file được xếp SURVIVES chứ không BROKEN), nhưng không loại trừ hoàn toàn khả năng giá vượt qua 26,990 một chút trước khi đảo chiều và lệnh đóng ngay sau đó bằng cơ chế khác — hai kịch bản cho pnl gần giống nhau.
Retracted by: timestamp chính xác của việc đóng lệnh đối chiếu với thời điểm giá chạm 26,990 — hiện không có.

**O3 · [DOCTRINE] · minor**
Checklist tick "Fair Value Gap (FVG) or Order Block (OB) provides confluence" nhưng Execution Review lại nhắc tới "Order block bên dưới" như một điểm đảo chiều *sau* khi entry — không rõ đây là cùng một OB đã dùng làm confluence trước entry hay một OB khác chỉ xuất hiện/được nhận ra sau lệnh. Nếu là OB khác được nhận ra sau, nhắc tới nó trong Execution Review không phải lỗi (mô tả price action sau lệnh là hợp lệ), nhưng không nên bị hiểu lầm là một phần của "confluence" đã tick trước entry. Retracted by: không cần — chỉ là lưu ý phân biệt claim trước/sau entry, không đổi verdict.

Drafted 4, cut 1 (một draft nghi vấn Judas Swing "16:00" có đúng là thời điểm chuẩn ICT killzone London hay không — bị cắt vì 16:00 theo giờ nào không được nêu (UTC/local/broker time) nên không thể kiểm mà không suy diễn, và không ảnh hưởng consequence).

**Verdict: SURVIVES, WEAKENED.**
Load-bearing claim về tính toàn vẹn dữ kiện (C5) bị FAIL rõ bằng arithmetic (O1) — đây là lỗi field, không phải lỗi setup. Load-bearing claim về chất lượng setup kỹ thuật (C4) không bị phá nhưng bị làm mờ bởi O2 (trình tự đảo chiều không rõ). Verdict không dùng "BROKEN" vì lỗi nằm ở field ghi log (exit_price), không phải ở logic entry — nhưng "SURVIVES THIS ATTACK" cũng không dùng được vì evidence sufficiency = thin và có ít nhất 1 lỗi field chưa sửa được.

Tôi đã tấn công: tính nhất quán exit_price/pnl/Result, trình tự đảo chiều trong Execution Review — arithmetic RR kế hoạch (3 nguồn khớp nhau: field, văn bản, tính toán) không bị phá, đây là điểm mạnh thật của file.

Critique này KHÔNG xác lập: (1) giá trị exit_price đúng là bao nhiêu — chỉ suy luận từ arithmetic pnl rằng 26,799.6 gần chắc là sai; (2) rằng setup entry (MSS/CHOCH/FVG M5) có đủ chuẩn doctrine — phần này không kiểm được từ chart, chỉ nói chưa có gì phản bác.

---

## 9. Opposite Case (Counter-Argument)

Đổi narrative role: điều gì nếu exit_price = 26,799.6 không phải lỗi field, mà **pnl mới là giá trị sai** (ví dụ được tính từ một hệ thống khác, hoặc gồm cả phí/swap không phản ánh đúng exit_price) — và lệnh thực ra đã đóng ngay gần entry (breakeven-ish) rồi pnl 191.4 là do một điều chỉnh khác (rebate, hedge, hoặc lỗi hệ thống trading platform) không liên quan tới price action?

Load-bearing claim của kèo ngược: pnl field là giá trị bị lỗi/nhiễu, exit_price mới là giá trị đúng — nghĩa là lệnh thực chất đóng gần entry, không đạt được reward đáng kể, và "Win" chỉ là do một khoản cộng thêm không phải từ price action thuần.

Strongest self-objection (tự đánh kèo ngược): pnl khớp gần chính xác với reward kế hoạch tính từ TP−entry (191.4 vs 190.4, chênh chỉ 1.0 điểm/0.5%) — một sự trùng hợp này khó xảy ra nếu pnl là nhiễu ngẫu nhiên từ nguồn khác; nếu pnl bị lỗi hệ thống, xác suất nó trùng khớp gần đúng với đúng công thức reward kế hoạch của chính lệnh này là rất thấp. Ngược lại, exit_price=entry_price là một lỗi copy-paste rất phổ biến và dễ giải thích (field bị ghi đè nhầm giá trị entry khi export).

Strength label: **undecidable from this evidence** — theo nghĩa chặt: cả hai kịch bản (exit sai / pnl sai) đều là giả thuyết không kiểm chứng được trực tiếp từ file, nhưng self-objection ở trên đã đủ mạnh để nghiêng cán cân hẳn về phía "exit_price sai" — dù vậy, không có timestamp hay log giao dịch độc lập nào xác nhận trực tiếp, nên formally vẫn xếp undecidable thay vì kết luận chắc.

Observable duy nhất phân biệt hai reading: một broker/platform trade log độc lập cho giao dịch NDX đóng lúc 2026-04-23 00:16:51 — nếu log đó cho thấy giá khớp exit thực tại gần 26,990, thesis gốc (exit_price field sai) đúng; nếu log cho thấy giá khớp exit thực gần 26,799.6, kèo ngược (pnl field có nguồn gốc khác price action) trở nên phải xem xét lại nghiêm túc.

---

## 10. Falsification Tests

**Test 1** — Tìm trade log/broker statement độc lập cho lệnh NDX đóng lúc 2026-04-23 00:16:51 UTC (hoặc giờ tương đương theo timezone app). Nếu exit giá gần 26,990, O1 được xác nhận đầy đủ (exit_price field sai, cần sửa); nếu exit giá gần 26,799.6 nhưng pnl vẫn 191.4, cần điều tra nguồn khác cho pnl (kèo ngược mục 9 trở nên đáng xem xét). Đóng: O1.

**Test 2** — Đối chiếu format frontmatter của toàn bộ 27 file trong sample: đếm số file có `exit_price == entry_price` bất kể pnl. Nếu đây là lỗi lặp lại ở nhiều file khác (không chỉ file này), đó là lỗi hệ thống export/template, không phải lỗi ngẫu nhiên của riêng lệnh 04-23. Đóng: O1 (mức ảnh hưởng ra ngoài file).

**Test 3** — Xác nhận trình tự thời gian giữa "đạt gần TP" và "đảo chiều xuống OB" bằng chart M5/M1 gốc (nếu phục hồi được). Nếu giá chạm/vượt 26,990 trước khi đảo chiều, O2 được narrow (Hit TP sạch, đảo chiều chỉ là mô tả *sau* lệnh đã đóng — không ảnh hưởng Result). Nếu giá đảo chiều *trước khi* chạm đủ 26,990, cần xem lại cơ chế exit thực tế đã dùng. Đóng: O2.
