---
date: 2026-04-01
symbol: NQ1
position: Long
result: Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 24,139.25
take_profit: 24,501
stop_loss: 23,990
exit_price: 24,179
pnl: 80
r_multiple: 0.27
planned_rr: 2.42
risk_percent:
confidence: 3
mistakes:
emotions:
  - Patient
  - Focused
  - Analytical
tags:
  - FairValueGap
  - Displacement
  - LiquiditySweepStopHunt
  - MarketStructureShift
  - DailyBias
  - BalancedPriceRange
source_id: 2007
da_verdict: SURVIVES, WEAKENED
da_evidence_sufficiency: thin
da_objections: {fatal: 0, material: 2, minor: 1}
da_opposite_case: "equally viable"
---
# Trade 2026-04-01 - NQ1 Long Win

## 0. Trade Summary

| Field                 | Value                                                     |
| --------------------- | ----------------------------------------------------------- |
| Symbol                | NQ1                                                       |
| Position              | Long                                                      |
| Result                | Win                                                       |
| Session               | London                                                    |
| Setup                 | NQ ICT 2022 AM Delivery                                   |
| Entry Model           | Fair Value Gap + Displacement + Liquidity Sweep/Stop Hunt |
| HTF Bias              |                                                           |
| Premium/Discount      |                                                           |
| Power of 3            |                                                           |
| Confidence            | 3/5 (Medium)                                              |
| Entry                 | 24,139.25                                                 |
| Stop Loss             | 23,990                                                    |
| Take Profit           | 24,501                                                    |
| Exit                  | 24,179                                                    |
| PnL                   | 80.0                                                      |
| R Multiple (realized) |                                                           |
| Planned RR            |                                                           |
| Risk %                |                                                           |
| Closed                | 2026-04-01 01:28:02.0544998                               |

---

## 1. Pre-market Bias & Analysis

- Daily bias: Khung 1 giờ xu hướng giảm và đang trong nhịp Pullback ( có thể xem xét trade ngắn setup long)
- Giá tăng mạnh để lại FVG (khung M15)
- Xuống khung M5 thấy trong đợt giảm lần trước giá tạo 1 Bearish FVG và sau đó nhịp Pullback tạo ra 1 Bullish FVG overlap với Bearish FVG (nay đã thành iFVG) hình thành 1 vùng BPR (Balance Price Range)
- Chờ giá retrace lên về vùng BPR khung M5 và chờ phản ứng
- Khi giá quay lại vùng BPR xuất hiện rejection. Khi giá chạm BPR, giá đi xuyên xuống vùng 50% (mean threshold) và phản ứng.
- nhiều cây nên đỏ liên tục từ cạnh BPR xuống 50% (khung M1) giống với khái niệm CISD. Sau đó giá đảo chiều với nhiều cây nến xanh và vượt qua mốc cao nhất của CISD giảm, xuất hiện FVG trên đường đi
-Chờ giá quay về FVG và tìm setup long ngắn hạn ( nhịp Pullback trên khung lớn)

### Charts

![[NQ1-20260401-2007-1.png]]
![[NQ1-20260401-2007-2.png]]
![[NQ1-20260401-2007-3.png]]
![[NQ1-20260401-2007-4.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Market Structure Shift + Displacement
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Clear liquidity target identified (buy-side or sell-side)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Rejection Validation When Enter PD Array Zones
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Partial take-profit levels are planned (1R, 2R, runner)
- [x] Not exceeding daily loss limit -- will stop trading if hit

---

## 3. Execution Review

Do setup long ngắn hạn -> đóng vị thế khi giá quét đỉnh cũ (24181)

**Emotions**: Patient, Focused, Analytical

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit) *(sai lệch với dữ kiện — xem O1: exit 24,179 ≠ TP 24,501, thực chất đây là một lệnh đóng tay sớm, không phải hit TP)*
- **Mistake chính**:
  - [[Mistake - ]] *(trống — không mistake tag nào được gán dù có ít nhất 1 điểm cần gắn: đóng lệnh sớm không theo kế hoạch TP ban đầu, xem O1)*
- **Nguyên nhân gốc rễ** *(suy luận có điều kiện — cần chart xác nhận)*:
  - Theo Execution Review: lệnh được đóng thủ công khi giá "quét đỉnh cũ (24181)" — một liquidity target trung gian, không phải TP kế hoạch (24,501). R thực nhận 0.27, thấp hơn rất nhiều so với 2.42 kế hoạch. Nguyên nhân gốc là quyết định exit sớm, không phải structure hay setup thất bại — nhưng file không cho biết cơ sở ICT nào (nếu có) đứng sau quyết định exit tại đúng "24181" ngoài việc đó tình cờ là một mức đỉnh cũ.

---

## 5. Lesson Learned

**Bài học kỹ thuật** (liên kết O1)
- Setup entry (bias D1 pullback ngắn hạn, CISD trên M1, FVG retest, BPR) là chuỗi lý luận đa timeframe khá đầy đủ trong văn bản — nhưng "Result: Win (Hit Take Profit)" trong mục 4 không khớp với exit thực tế 24,179 khi TP kế hoạch là 24,501. Kết quả thật là một *manual exit* tại một liquidity target trung gian, không phải TP hit.
- Field "Daily bias" tại mục 1 tự mô tả "Khung 1 giờ xu hướng giảm" nhưng label field frontmatter là `higher_timeframe_bias: D1` — không nhất quán giữa văn bản (nói H1) và field (nói D1); không ảnh hưởng outcome nhưng là một điểm nhòe timeframe cần làm rõ khi tra cứu chéo giữa các lệnh (đối chiếu CS-O8 về bias-TF drift).

**Bài học tâm lý**
- Emotions ghi "Patient, Focused, Analytical" nhưng hành vi thực tế (đóng lệnh sớm tại R=0.27 khi kế hoạch R=2.42, tức chỉ đạt ~11% mục tiêu reward) mô tả một exit theo phản xạ khi thấy giá "quét đỉnh cũ" — nhãn cảm xúc tự ghi không mô tả đúng động lực quyết định thực tế của việc chốt sớm.

**Bài học quy trình & risk**
- Checklist có dòng "Partial take-profit levels are planned (1R, 2R, runner)" tick `[x]`, nhưng Execution Review không hề đề cập kế hoạch chốt từng phần nào — không rõ việc đóng tại 24,179 là một phần kế hoạch scale-out đã định trước, hay một quyết định phát sinh tại chỗ. Field trống (`risk_percent`, `r_multiple`, `planned_rr` ở bảng mục 0) làm mất khả năng đối chiếu số với frontmatter.

**Rule cần thêm/cập nhật**
- Rule kiểm tra được: khi exit_price khác cả TP và SL kế hoạch, trường "Result" phải ghi rõ "Manual Exit" thay vì "Hit Take Profit" — và Execution Review phải nêu lý do cụ thể tại sao mức exit đó được chọn thay vì TP đã định (liên kết O1).
- Rule kiểm tra được: nếu checklist tick "Partial TP planned", Execution Review phải liệt kê rõ các mức 1R/2R/runner đã định trước khi vào lệnh — nếu không liệt kê được, không tick ô này (liên kết O2, [UNSUPPORTED]).

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, 4 chart Obsidian không đọc được. Sufficiency: **thin** — load-bearing claim (liệu setup entry có đạt điều kiện MSS/FVG theo đúng chuỗi lý luận D1→H1→M5 mà user tự mô tả) chỉ kiểm được qua văn bản tự thuật, không kiểm được qua chart.

**Thesis & claims**:
- C1: D1 bias giảm, đang pullback → có thể xem xét long ngắn hạn (mục 1, câu 1).
- C2: M15 hình thành FVG bullish sau move tăng; M5 có Bearish FVG cũ overlap Bullish FVG mới → thành iFVG, tạo BPR.
- C3: Giá retrace về BPR, xuất hiện rejection; M1 có chuỗi nến giảm giống CISD rồi đảo chiều vượt cao nhất của CISD giảm, tạo FVG mới.
- C4 (load-bearing): Entry long tại FVG mới hình thành (24,139.25) có đủ MSS + Displacement + FVG theo đúng checklist tick — cơ sở của toàn bộ setup.
- C5: Kết quả Win vì giá đạt TP — checklist tick "Result: Win (Hit Take Profit)".
- Suy luận: C1+C2+C3 → C4 (entry hợp lệ) → kỳ vọng C5 (đạt TP). Nhưng C5 **không khớp dữ kiện số** (xem O1) — đây là điểm gãy giữa thesis process và outcome ghi nhận.

**Điều gì đứng vững**:
- Chuỗi lý luận đa timeframe D1→M15→M5→M1 trong mục 1 có cấu trúc logic nội tại nhất quán (bias pullback → FVG hình thành → retrace → rejection → CISD → MSS → entry) — không có mâu thuẫn nội tại giữa các bước, khác hẳn file 03-30. Đây là điểm khác biệt đáng ghi nhận dù không kiểm được bằng chart.
- Arithmetic RR: risk = |24,139.25−23,990| = 149.25, reward = |24,501−24,139.25| = 361.75, RR = 361.75/149.25 = 2.424 ≈ planned_rr 2.42 — khớp.
- Arithmetic r_multiple thực nhận: (24,179−24,139.25)/149.25 = 0.266 ≈ field 0.27 — khớp đúng phép tính, không phải lỗi số học.

**Objections**:

**O1 · [SELF-CONTRADICTION] / [ARITHMETIC] · material · attacks C5**
Claim: mục 4 ghi "Result: Win (Hit Take Profit)".
Fails: exit_price (24,179) cách xa take_profit (24,501) — 322 điểm, tức chỉ đạt 11% khoảng cách tới TP. "Hit Take Profit" theo nghĩa thông thường (giá chạm đúng mức TP đã đặt) không khớp — đây là một manual exit, tự ghi rõ trong Execution Review: "đóng vị thế khi giá quét đỉnh cũ (24181)".
Evidence: TP field = 24,501; exit_price field = 24,179; Execution Review "đóng vị thế khi giá quét đỉnh cũ (24181)" (chênh 2 điểm so với exit_price ghi trong frontmatter — có thể do làm tròn hoặc trượt giá khi khớp lệnh).
Consequence: Nhãn "Hit Take Profit" là mô tả sai loại kết quả — R thực nhận (0.27) phản ánh một quyết định exit sớm, không phải cơ chế TP tự động. Việc gọi đây là "Win (Hit TP)" thay vì "Win (Manual Exit, partial R)" làm méo cách hiểu chất lượng setup khi tra cứu chéo (một setup RR kế hoạch 2.42 chỉ hiện thực hoá 0.27, chưa tới 1/8 kế hoạch).
Your best answer: "Miễn kết quả dương (Win) thì gọi 'Hit Take Profit' cũng không sai về bản chất." — Không cứu được: hai loại kết quả này có ý nghĩa khác nhau cho việc đánh giá edge — một hệ thống "Win nhờ TP tự động" và một hệ thống "Win nhờ exit tay tuỳ cảm tính" có profile risk khác hẳn, dù cùng dấu PnL.
Retracted by: xác nhận có một partial-TP kế hoạch từ trước tại đúng mức "đỉnh cũ 24181" — hiện Execution Review không nêu đây là kế hoạch có trước, chỉ nêu là hành động tại chỗ.

**O2 · [UNSUPPORTED] · material · attacks C2, C4**
Claim: checklist tick "Market Structure Shift + Displacement" và "Fair Value Gap (FVG) or OB provides confluence" cho entry tại 24,139.25.
Fails: Mục 1 mô tả MSS bằng câu "giá đảo chiều với nhiều cây nến xanh và vượt qua mốc cao nhất của CISD giảm" — không nêu giá cụ thể của swing bị phá, không nêu candle nào đóng nến xác nhận body-close (yêu cầu chuẩn cho MSS). "CISD" cũng được mô tả bằng suy diễn tương tự ("giống với khái niệm CISD"), không phải khẳng định chắc — chính câu chữ của user dùng "giống với" cho thấy user cũng không chắc đây có đúng là CISD chuẩn.
Evidence: không có số giá nào cho swing MSS trong toàn mục 1; cụm từ "giống với khái niệm CISD" (không phải "là CISD").
Consequence: claim MSS/CISD làm nền cho entry là claim văn xuôi mô tả một pattern quan sát, chưa đủ evidence bar để coi là "confirmed" theo đúng nghĩa doctrine — dù không có gì trong file *phản bác* MSS đã xảy ra, cũng không có gì *xác nhận* độc lập ngoài mô tả của người viết chính lệnh này.
Retracted by: chart M1/M5 gốc cho thấy body-close cụ thể xác nhận MSS tại swing nào — hiện không có.

**O3 · [DOCTRINE] · minor**
Field "Daily bias" trong mục 1 viết "Khung 1 giờ xu hướng giảm" (mô tả H1) nhưng frontmatter field khai `higher_timeframe_bias: D1` — nhãn timeframe không khớp giữa văn bản và field, dù không đổi kết luận Win/Loss. Retracted by: không cần — chỉ là lưu ý nhất quán ghi log, không ảnh hưởng verdict.

Drafted 4, cut 1 (một draft về "BPR/iFVG có thực sự tồn tại trước khi giá quay lại test không" bị cắt vì không thể phân biệt với hindsight — retest bản thân là bằng chứng vòng, không phải objection độc lập).

**Verdict: SURVIVES, WEAKENED.**
Load-bearing claim C4 (entry có MSS+FVG hợp lệ) không bị FAIL — không có gì trong file *mâu thuẫn* với việc MSS đã xảy ra — nhưng cũng không PASS đầy đủ (O2, UNSUPPORTED vì thiếu structure level cụ thể). Claim phụ C5 (Result label) FAIL rõ (O1).

Tôi đã tấn công: nhãn kết quả (Result label), cơ sở MSS/CISD, tính nhất quán field bias-TF — chuỗi lý luận đa-timeframe tổng thể (C1→C3) không bị phá, đây là phần khác biệt tích cực so với file 03-30.

Critique này KHÔNG xác lập: (1) setup này thực sự có MSS chuẩn theo doctrine (chỉ nói chưa có bằng chứng phản bác, không phải bằng chứng xác nhận); (2) quyết định exit sớm tại 24,181 là sai lầm — đóng sớm có thể là quản trị risk hợp lý, phản biện này không đánh giá điều đó theo hướng khuyến nghị.

---

## 9. Opposite Case (Counter-Argument)

Đổi narrative role: điều gì nếu "quét đỉnh cũ (24181)" không phải là một manual exit tuỳ cảm tính, mà chính là **DOL (draw on liquidity) đã xác định từ trước** — một buy-side liquidity pool nhỏ nằm giữa entry và TP kế hoạch, và user đã đóng đúng lúc thanh khoản đó bị quét (đúng như "Clear liquidity target identified" đã tick ở checklist) — trước khi giá có khả năng đảo chiều mà chưa kịp chạy hết tới 24,501?

Load-bearing claim của kèo ngược: "24,181" là một liquidity target trung gian đã biết trước (không phải phát sinh tại chỗ), nên đóng lệnh tại đó là kỷ luật chốt lời theo kế hoạch, không phải thiếu kiên nhẫn.

Strongest self-objection (tự đánh kèo ngược): Execution Review dùng động từ "Do setup long ngắn hạn" — cụm "ngắn hạn" mô tả *cách nhìn tổng thể của setup* (mục 1 gọi đây là "setup long ngắn hạn" trong "nhịp Pullback trên khung lớn"), chứ không nêu rõ 24,181 từng được xác định là target *trước* khi vào lệnh ở đâu trong mục 1 — không có câu nào trong Pre-market Analysis nhắc tới mức 24,181 hay "đỉnh cũ" này trước entry. Nếu đó thực sự là target đã biết trước, lẽ ra phải xuất hiện trong phần lập kế hoạch, không chỉ trong Execution Review viết sau.

Strength label: **equally viable**. Cả hai reading cùng khớp với duy nhất sự kiện quan sát được (exit tại 24,179 gần mức "24181"), và file không có đủ chi tiết ở mục 1 (kế hoạch trước lệnh) để phân biệt "đã biết trước" và "phát sinh tại chỗ".

Observable duy nhất phân biệt hai reading: liệu mức "24181" (hoặc mức đỉnh cũ tương đương) có được nêu tên như một liquidity target trong phần Pre-market Analysis (mục 1) *trước khi* lệnh được vào — nếu có, kèo gốc (kỷ luật chốt lời theo kế hoạch) đúng; nếu hoàn toàn không xuất hiện trước đó, kèo ngược yếu đi và nghiêng về "quyết định tại chỗ khi thấy giá phản ứng".

---

## 10. Falsification Tests

**Test 1** — Kiểm 4 chart gốc (nếu phục hồi được từ Obsidian vault khác) xem mức 24,181 có được đánh dấu là liquidity target *trước* thời điểm entry 01:28:02 hay không. Nếu có, O1 được narrow: "Hit Take Profit" vẫn sai tên nhưng không phải "exit tuỳ cảm tính". Nếu không, giữ nguyên O1 fatal-material. Đóng: O1.

**Test 2** — Đối chiếu N lệnh khác trong sample có cùng cấu trúc thesis "D1→M15→M5→M1" tương tự và tick MSS+FVG mà không nêu số giá cụ thể cho swing MSS. Nếu pattern "MSS mô tả bằng lời, không kèm giá" xuất hiện ở >50% các lệnh Win trong sample, đây là lỗi hệ thống ghi log MSS, không riêng file này. Đóng: O2.

**Test 3** — Tính lại r_multiple thực nhận nếu giả định user giữ lệnh tới đúng TP kế hoạch (24,501) thay vì exit tại 24,179: R sẽ là 2.42 thay vì 0.27 — chênh lệch 2.15R. Nếu áp dụng cho toàn bộ các lệnh Win có manual-exit-sớm tương tự trong sample, expectancy $/lệnh của nhóm này (theo CS-O về expectancy) sẽ đổi khác đáng kể so với con số +$62.42/lệnh đã tính trên PnL thực. Đóng: O1 (mức ảnh hưởng ra ngoài file, liên kết cross-setup expectancy).
