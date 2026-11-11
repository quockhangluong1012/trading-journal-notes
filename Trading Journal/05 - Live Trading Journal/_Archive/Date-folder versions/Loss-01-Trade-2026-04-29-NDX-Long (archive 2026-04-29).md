---
date: 2026-04-29
symbol: NDX
position: Long
result: Loss
session: London
setup: NQ ICT 2022 AM Delivery
entry_model: Market Structure Shift + Order Blocks + Fair Value Gap
entry_timeframe: 
higher_timeframe_bias: 
bias_correct: 
entry_price: 27,091.6
take_profit: 27,167.6
stop_loss: 27,058.6
exit_price: 27,058.6
pnl: -66
r_multiple: -1
planned_rr: 2.3
risk_percent: 
confidence: 3
mistakes: 
emotions:
  - Patient
tags:
  - MarketStructureShift
  - OrderBlocks
  - FairValueGap
  - PremiumVsDiscount
  - KillZones
  - DailyBias
source_id: 2014
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 2, material: 1, minor: 0}
da_opposite_case: weaker but non-trivial
---
# Trade 2026-04-29 - NDX Long Loss

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Loss |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Market Structure Shift + Order Blocks + Fair Value Gap |
| HTF Bias |  |
| Premium/Discount |  |
| Power of 3 |  |
| Confidence | 3/5 (Medium) |
| Entry | 27,091.6 |
| Stop Loss | 27,058.6 |
| Take Profit | 27,167.6 |
| Exit | 27,058.6 |
| PnL | -66.0 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-04-29 07:19:00 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: N/A
- **Premium/Discount**: N/A
- **Power of 3 Phase**: N/A

================== Khung D1 ==================

- daily bias: Bullish (giá vẫn đang trong trend tăng)

================== Khung H1 ==================

- Phiên London mở cửa, có 1 Judas Swing đầy giá đi xuống
- Giá đi xuống chạm vào cạnh trên 1 Order Block
================== Khung M15 ==================

- Giá chạm vào cạnh trên Order Block và xuyên vào trong
- Xuống khung thời giản nhỏ hơn quan sát
================== Khung M1 ==================

- Giá bật lên tạo thành MSS + displacement
- Giá tạo FVG trên đường đảo chiều
- Chờ giá retrace về vùng FVG tìm setup long

================== Setup ==================

- Vị thế: Long
- Entry: 27091.6
- Take Profit: 27167.6
- Stop Loss: 27058.6
- Ngày: 29/04/2026
- Phiên: London

================== Kết quả ==================

- Giá tăng sau đó đến 27150 và đảo chiều đi xuống
- Giá quét OB và sâu xuống bên dưới đáy cũ trước đó (27016)
- Stop loss của lệnh bị quét sau đó giá đảo chiều
- Giá đi đúng hướng và chạm TP ở vùng London Overlap với New York

=> Lệnh hit stop loss

### Charts

![[NDX-20260429-2014-1.png]]
![[NDX-20260429-2014-2.png]]
![[NDX-20260429-2014-3.png]]
![[NDX-20260429-2014-4.png]]
![[NDX-20260429-2014-5.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Market Structure Shift + Displacement
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Rejection Validation When Enter PD Array Zones
- [x] No high-impact news events imminent (check economic calendar)
- [x] Partial take-profit levels are planned (1R, 2R, runner)
- [x] Not exceeding daily loss limit -- will stop trading if hit

---

## 3. Execution Review

- Giá quét thanh khoản sâu xuống đáy cũ => hit stop loss
- Nguyên nhanh xác định sai judas swing, liquidity sweep
- Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng

**Emotions**: Patient

---

## 4. Phân Tích Sau Lệnh

- **Result**: Loss (Hit Stop Loss)
- **Mistake chính**:
  - [[Mistake - ]] *(trống trong bản gốc — Execution Review tự nêu rõ nhất: "xác định sai judas swing, liquidity sweep" — mistake phù hợp là misidentify liquidity sweep/invalid Judas Swing, khớp với chính lời tự phê (suy luận có điều kiện — cần chart xác nhận))*
- **Nguyên nhân gốc rễ**:
  - *(trống trong bản gốc)* Tự nêu trong mục 3: "Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng" — hàm ý user đã nhận ra SAU thua rằng đáy/đỉnh bị quét trong setup này KHÔNG phải một mức quan trọng. Đây là root cause tự thuật nhưng viết SAU khi biết kết quả (Kết quả mô tả trước, Execution Review sau) — cần soi hindsight ở mục 8.

---

## 5. Lesson Learned

**Bài học kỹ thuật**
- Đây là lệnh Loss thứ 3 liên tiếp trong 3 ngày (27/04, 28/04, 29/04) đều là NDX Long dùng chung thesis "D1 bullish → chờ pullback/sweep → MSS/OB/FVG → long". Cả ba lệnh đều bị stop trong vòng vài giờ mở phiên London. Liên kết O2 (load-bearing, [METHOD] fatal — lặp thesis không điều chỉnh).
- Lesson của `Loss-01-2026-04-27` (chưa quét hết đáy cũ trước khi long) và của `Loss-02-2026-04-28` (chưa có rejection trước khi entry) đều KHÔNG xuất hiện dưới dạng điều kiện được kiểm ở lệnh này — thay vào đó, lệnh 04-29 tạo ra một lesson MỚI hoàn toàn khác ("Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng") mà không tham chiếu ngược hai lesson trước. Liên kết O1.
- Bản thân file tự nhận sai judas swing/liquidity sweep — nhưng checklist mục 2 vẫn tick `[x]` cho "Rejection Validation When Enter PD Array Zones" — tự mâu thuẫn giữa tick và tự phê. Liên kết O3.

**Bài học tâm lý**
- Emotion tự ghi "Patient" (kiên nhẫn) — khác hẳn "Greedy/Confident" (04-27) và "Greedy/Uncertain" (04-28) — nhưng kết quả vẫn Loss với cùng lỗi cấu trúc (misidentify liquidity/structure). Điều này cho thấy vấn đề không nằm ở tốc độ vào lệnh (đã "kiên nhẫn" hơn hai lệnh trước) mà nằm ở khả năng nhận diện đúng level — một vấn đề kỹ năng, không phải chỉ tâm lý.

**Bài học quy trình & risk**
- `risk_percent` trống ở cả 3 lệnh 27-29/04 — không có cách nào kiểm tra liệu size có tăng lên sau 2 lần thua liên tiếp (dấu hiệu revenge-sizing) hay giữ nguyên.
- Không có cơ chế "dừng sau N lệnh thua liên tiếp cùng thesis" — đây là lệnh Loss thứ 3, vẫn cùng setup, cùng bias, cùng phiên London, không có ghi chú nào về việc xem xét dừng hoặc đổi cách tiếp cận.
- Checklist mục 2 ở 3 lệnh có độ dài khác nhau (11 dòng ở 04-27, 4 dòng ở Loss 04-28, 8 dòng ở 04-29) — không có mẫu checklist cố định cho cùng setup "NQ ICT 2022 AM Delivery" qua 3 ngày liên tiếp.

**Rule cần thêm/cập nhật**
- Rule 1: Sau 2 lệnh Loss liên tiếp cùng thesis (D1 bullish long trong killzone London), lệnh thứ 3 cùng thesis phải trích dẫn cụ thể lesson của 2 lệnh trước và xác nhận điều kiện đó đã được kiểm — điều kiện đo: có câu tham chiếu ngược tới ít nhất 1 trong 2 lesson trước trong phần Pre-market Bias. Liên kết O2.
- Rule 2: Định nghĩa trước (không phải hồi tố) tiêu chuẩn "đáy/đỉnh cũ quan trọng" cho liquidity sweep — ví dụ: swing đã tồn tại >X nến, hoặc đã được test >=2 lần — điều kiện đo: có một quy tắc bằng số, không chỉ tính từ "quan trọng". Liên kết O1.
- Rule 3: Checklist tick "Rejection Validation" chỉ được đánh dấu khi Execution Review (viết sau) không tự phủ nhận nó — điều kiện đo: đối chiếu 2 phần này trước khi đóng file log. Liên kết O3.

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, không screenshot khả dụng → cấm [CHART]. "MSS", "Judas Swing", "displacement", "FVG" là claim của user. Sufficiency: **thin** — và load-bearing claim (liquidity sweep có quét đúng mức quan trọng hay không) đã bị chính user tự nhận là SAI trong Execution Review, nên phần lớn công việc phản biện ở đây là làm rõ HỆ QUẢ của tự nhận đó đối với chuỗi 3 lệnh, không phải tìm lỗi mới.

**Đối chiếu chuỗi 27→29/04 (yêu cầu riêng của brief)**: ba lệnh `Loss-01-2026-04-27`, `Loss-02-2026-04-28`, và lệnh này (`Loss-01-2026-04-29`) đều là NDX Long, đều dùng D1 bias Bullish, đều bị stop trong phiên London, và mỗi lệnh tự nhận một lỗi KHÁC nhau:
- 04-27: "chưa quét hết đáy cũ" + lòng tham không chốt lời sớm.
- 04-28 (Loss-02): "chưa có dấu hiệu rejection" + nóng vội.
- 04-29 (lệnh này): "xác định sai judas swing, liquidity sweep" + "Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng".
Không có lệnh nào trong 3 lệnh trích dẫn lesson của lệnh trước. Cụ thể, lesson 04-27 ("cẩn thận khi giá chưa quét hết đáy cũ") và lesson của lệnh này ("liquidity sweep phải quét đáy/đỉnh cũ quan trọng") là HAI CÁCH DIỄN ĐẠT GẦN NHƯ CÙNG MỘT VẤN ĐỀ (tầm quan trọng của level bị quét) cách nhau 2 ngày — nhưng lệnh 04-29 viết như một phát hiện mới, không tham chiếu ngược 04-27.

**Thesis & claims**:
- C1: D1 bias Bullish (lệnh thứ 3 liên tiếp dùng chung bias này không thay đổi qua 2 lần thua trước).
- C2: H1 — Judas Swing đẩy giá xuống, chạm cạnh trên 1 OB.
- C3: M15 — giá xuyên vào trong OB, xuống M1 quan sát tiếp (nhảy từ M15 xuống M1, bỏ qua M5 — khác chuẩn nesting D1→H1→M5 mà 2 lệnh trước cũng không tuân theo nhất quán).
- C4: M1 — giá bật lên tạo MSS + displacement + FVG → chờ retrace vào FVG để long. **Load-bearing**: C4 phụ thuộc việc "Judas Swing" ở C2 thực sự quét một mức liquidity quan trọng — chính Execution Review (viết sau) phủ nhận điều này ("xác định sai judas swing, liquidity sweep").
- C5 (hệ quả C1-C4): entry long tại 27,091.6 là quyết định có cơ sở.

**Điều gì đứng vững**: User tự nhận đúng nguyên nhân gốc rễ ngay trong Execution Review, không đổ lỗi cho thị trường hay tâm lý (khác 2 lệnh trước có yếu tố Greedy/Uncertain/Nóng vội) — đây là một tự phê kỹ thuật thuần túy, kiên nhẫn hơn (emotion "Patient") nhưng vẫn sai ở tầng nhận diện structure. Việc mô tả "Kết quả" ghi nhận cả việc giá SAU ĐÓ đi đúng hướng và chạm TP tại London/NY overlap là một quan sát trung thực (không né tránh), không cố gắng biện minh cho kết quả.

**Objections**:

**O1 · [METHOD] · fatal · attacks toàn bộ chuỗi Lesson Learned (load-bearing cho câu hỏi "lesson trước có được áp dụng")**
Claim: lesson "Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng" (viết ở lệnh này) là một bài học MỚI, độc lập với 2 lệnh Loss trước.
Fails: lesson của `Loss-01-2026-04-27` là "Cẩn thận khi giá chưa quét hết đáy cũ" — về bản chất là CÙNG một nhận thức (tầm quan trọng của việc quét đúng mức liquidity trước khi tin vào đảo chiều) diễn đạt theo hướng khác. Nếu lesson 04-27 đã được áp dụng như một rule kiểm tra trước entry ("đã quét đủ đáy cũ chưa?"), lỗi "xác định sai liquidity sweep" ở 04-29 có thể đã bị phát hiện TRƯỚC khi entry, không phải sau khi thua.
Evidence: so sánh trực tiếp — 04-27 lesson: "Cẩn thận khi giá chưa quét hết đáy cũ"; 04-29 root cause: "Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng" — không có câu nào trong file 04-29 tham chiếu ngược tới lesson 04-27 hay 04-28.
Consequence: đây là bằng chứng cụ thể (không suy đoán) cho đúng loại phát hiện mà CS-O2 trong cross_setup_findings mô tả ở quy mô toàn sample (lesson "chờ MSS" ghi lại 3 lần, vi phạm lại 4 lần) — ở đây là một phiên bản thu nhỏ, cùng cơ chế: rule được ghi ra sau mỗi lần thua nhưng không có cơ chế nào ép lệnh SAU kiểm tra lại lệnh TRƯỚC đã học được gì.
Your best answer: "lesson 04-27 nói về đáy cũ CHƯA bị quét (thiếu sweep), còn lesson 04-29 nói về đáy cũ bị quét nhưng KHÔNG quan trọng (sweep sai mức) — đây là hai vấn đề khác nhau." — Đúng về mặt kỹ thuật hai câu không đồng nhất 100%, nhưng cả hai đều thuộc cùng một nhóm lỗi rộng hơn ("đánh giá sai ý nghĩa của level bị quét/chưa quét") mà một checklist item duy nhất ("xác nhận level liquidity bị quét là level nào, đã từng được test bao nhiêu lần") có thể bắt được cả hai — sự vắng mặt của loại checklist item này qua cả 3 lệnh là điểm chung, không phải sự khác biệt.
Retracted by: một checklist item cụ thể về "định danh level liquidity" xuất hiện ở lệnh 04-29 (cho thấy đã cố gắng áp lesson 04-27) — hiện không có; mục 2 checklist của lệnh này (8 dòng) không có dòng nào về việc xác nhận tầm quan trọng của level bị quét.

**O2 · [HINDSIGHT] · fatal · attacks C4 (load-bearing)**
Claim: MSS + displacement + FVG trên M1 là xác nhận đủ điều kiện đảo chiều để long, dựa trên Judas Swing đã quét liquidity quan trọng.
Fails: câu Execution Review "Liquidity Sweep phải quét 1 đáy/đỉnh cũ quan trọng" xuất hiện SAU phần "Kết quả" (đã biết giá đảo chiều đi xuống, quét OB, "sâu xuống bên dưới đáy cũ trước đó 27016" — mức 27016 THẤP hơn cả stop loss 27058.6, nghĩa là giá còn giảm sâu hơn sau khi đã quét SL). Việc xác định "sai judas swing" chỉ có thể nói được SAU khi thấy giá tiếp tục giảm xuống dưới 27016 — tại thời điểm entry, level "quan trọng" hay không không có tiêu chuẩn đo trước.
Evidence: cấu trúc file: mục "Kết quả" (mô tả giá đảo chiều xuống, quét sâu tới 27016) đứng TRƯỚC mục 3 Execution Review (nơi có câu tự phê) — trình tự viết cho thấy nhận thức "sai judas swing" được rút ra từ quan sát giá đi tiếp sau khi đã biết outcome.
Consequence: "xác định sai judas swing/liquidity sweep" là một chẩn đoán retro dùng đúng thông tin (giá xuống tới 27016) mà không tồn tại tại thời điểm quyết định entry — theo nguyên tắc REVIEW mode của brief, đây là claim hợp lệ CHO MỤC ĐÍCH HỌC nhưng không chứng minh rằng có một tiêu chuẩn ĐO ĐƯỢC trước entry mà lệnh này đã vi phạm; nó chỉ chứng minh rằng outcome xấu, và user gán một nguyên nhân retro cho outcome đó.
Your best answer: "level 27016 đã là swing low được biết từ trước (không phải phát hiện sau), nên user hoàn toàn có thể so sánh Judas Swing hiện tại với 27016 TRƯỚC khi entry." — Có thể đúng, nhưng file không ghi số 27016 ở đâu trong phần Pre-market/Setup (chỉ xuất hiện ở mục Kết quả) — không có bằng chứng nào cho thấy 27016 đã được xác định là mức tham chiếu TRƯỚC entry.
Retracted by: một dòng trong Pre-market Bias hoặc Setup ghi nhận mức 27016 (hoặc bất kỳ swing low nào) là mức liquidity mục tiêu ĐÃ BIẾT trước khi entry — hiện không có.

**O3 · [SELF-CONTRADICTION] · material · attacks checklist mục 2**
Claim: "Rejection Validation When Enter PD Array Zones" đã được xác nhận trước entry (tick `[x]`).
Fails: Execution Review tự ghi "xác định sai judas swing, liquidity sweep" — nếu Judas Swing (cơ chế tạo rejection ở đây) bị xác định sai, thì "rejection validation" gắn với chính Judas Swing đó cũng không thể coi là đã được validate đúng. Tick `[x]` và tự phê ngay dưới không thể đồng thời đúng.
Evidence: checklist mục 2 dòng 5: "[x] Rejection Validation When Enter PD Array Zones"; Execution Review mục 3 dòng 2: "Nguyên nhanh xác định sai judas swing, liquidity sweep".
Consequence: giống pattern CS-O9 trong cross_setup_findings (checklist tick đầy nhưng review tự phủ nhận) — làm giảm độ tin cậy của MỌI tick khác trong cùng checklist (8 dòng), không chỉ dòng này.
Your best answer: "tick được đánh trước entry dựa trên đánh giá TẠI THỜI ĐIỂM ĐÓ, sai sót chỉ lộ ra sau." — Hợp lý và đúng với REVIEW mode (tick là quyết định ex-ante, review là ex-post) — điều này làm objection giảm từ fatal xuống material, không loại bỏ hoàn toàn: vẫn là một tín hiệu rằng checklist tick không đáng tin cậy để đánh giá "chất lượng setup tại thời điểm entry" khi đọc lại.
Retracted by: không cần — đã tự giảm mức qua rebuttal, giữ material.

Drafted 4, cut 1 (draft riêng về "risk_percent trống không đối chiếu CS-O1" bị cắt, gộp vào mục 5 vì không đủ consequence độc lập cho một objection số).

**Verdict: BROKEN.** Load-bearing claim C4 (MSS/FVG xác nhận đảo chiều dựa trên liquidity sweep quan trọng) sụp theo hai đường: (a) chẩn đoán "sai judas swing" chỉ có thể biết sau khi thấy giá tiếp tục giảm tới 27016 — hindsight, không phải tiêu chuẩn đo trước (O2, fatal); (b) lesson tương tự đã tồn tại từ 2 ngày trước (04-27) nhưng không được viện dẫn hay kiểm lại ở lệnh này — cho thấy quy trình học từ lỗi trong chuỗi 3 lệnh liên tiếp không có cơ chế thực thi, khớp đúng pattern CS-O2 ở quy mô toàn sample (O1, fatal). Tôi đã tấn công nhưng không phá được: user tự phê trung thực, không đổ lỗi cảm xúc; timeframe nesting trình bày đúng thứ tự (dù nhảy M15→M1 bỏ M5, không phải lỗi logic mà chỉ là thiếu một bước trung gian). Critique này KHÔNG xác lập: (1) liệu Judas Swing/MSS/FVG có thật trên chart — không có ảnh; (2) liệu nếu áp đúng lesson 04-27 thì lệnh này có bị hủy hay không — không kiểm được vì thiếu chart để xác nhận đáy cũ 27016 có được biết trước hay không.

---

## 9. Opposite Case (Counter-Argument)

Đổi vai trò: "Judas Swing" bị Execution Review coi là "xác định sai" có thể đọc thành **một Judas Swing hợp lệ nhưng ở cấp độ higher timeframe (H1/H4) chưa hoàn tất pha sweep** — nghĩa là cú quét sâu xuống 27016 (dưới cả SL) không phải bằng chứng "sweep sai", mà là bằng chứng level liquidity thật sự nằm SÂU HƠN mức mà setup M1 nhắm tới; setup M1 bắt đúng một MSS thật (tăng giá tạm thời) nhưng bên trong một sweep lớn hơn còn tiếp diễn xuống 27016 trước khi thị trường thực sự đảo chiều đúng hướng bias D1 (như "Kết quả" tự ghi: "Giá đi đúng hướng và chạm TP ở vùng London Overlap với New York" — SAU KHI đã quét cả SL của lệnh này).

Load-bearing claim của kèo ngược: MSS M1 là thật, nhưng entry quá sớm một bậc timeframe — cần chờ sweep hoàn tất ở H1 (tới 27016) trước khi tin MSS M1, không phải MSS M1 sai.

Tự đánh kèo ngược: nếu đúng vậy, thì "Kết quả" tự ghi giá SAU ĐÓ đi đúng hướng bias D1 và chạm TP đúng hướng lệnh gốc — đây là fact mà chính thesis gốc (Execution Review) không giải thích được tại sao setup "sai" lại đi đúng hướng dự đoán sau khi quét SL. Đây chính là fact khiến kèo ngược có sức nặng hơn bình thường.

**Strength label: weaker but non-trivial.** Kèo ngược giải thích được một fact mà thesis gốc bỏ qua (giá đi đúng hướng SAU KHI quét SL) nhưng không đủ để gọi "stronger" vì không có evidence xác nhận 27016 thực sự là target liquidity đã biết trước — nó vẫn là một cách đọc hợp lý từ đúng các fact đã có, cần thêm xác nhận cấp H1/H4 để "sống".

**Observable phân biệt hai reading**: liệu 27016 có phải một swing low được named cụ thể trên H1/H4 (không phải chỉ nhìn thấy sau khi giá chạm tới) — nếu có và nó khớp với vùng liquidity lớn hơn mà D1 bias hướng tới, kèo ngược (entry sớm một bậc TF) đứng; nếu 27016 chỉ là điểm giá tình cờ đi tới mà không gắn với structure nào, thesis gốc (Judas Swing sai hoàn toàn) đứng.

---

## 10. Falsification Tests

1. **Test đóng O1**: kiểm 5 lệnh Loss NDX Long tiếp theo trong journal (nếu có, sau 04-29) có chứa một checklist item hoặc câu văn tham chiếu ngược cụ thể tới lesson "liquidity sweep phải quét đáy/đỉnh cũ quan trọng" — có → lesson này đã được áp dụng thực; không có → tiếp tục củng cố O1/CS-O2 ở quy mô rộng hơn.
2. **Test đóng O2**: xác nhận mức 27016 có được ghi nhận là swing low quan trọng ở BẤT KỲ đâu trong Pre-market Bias/Setup của lệnh này hoặc lệnh trước đó trong journal (trước ngày 04-29) — có → O2 hạ xuống material (mức đã biết, chỉ là đánh giá sai tầm quan trọng, không phải hindsight thuần); không có → O2 giữ fatal.
3. **Test đóng phần Opposite Case**: tìm cấu trúc H1/H4 xác nhận 27016 là một named swing low (không phải điểm giá ngẫu nhiên) — có → nâng kèo ngược lên "equally viable"; không có → giữ "weaker but non-trivial".
