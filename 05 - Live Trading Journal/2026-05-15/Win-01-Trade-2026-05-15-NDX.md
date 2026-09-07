---
date: 2026-05-15
symbol: NDX
position: Long
result: Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,368.10
take_profit: 29,420.60
stop_loss: 29,340.80
pnl: 105
r_multiple:
risk_percent: 5%
mistakes:
  - "[[07-Mistake-Risk-more-than-0.5-total-account]]"
tags:
planned_rr: 1.92
da_verdict: SURVIVES, WEAKENED
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 2, minor: 1}
da_opposite_case: weaker but non-trivial
---

# Trade 2026-05-15 - SYMBOL Position Result

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Win                                               |
| Session         | London                                            |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M5                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           |                                                   |
| Stop Loss       |                                                   |
| Take Profit     |                                                   |
| PnL             |                                                   |
| R Multiple      |                                                   |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Bullish - Giá đang trong trend tăng
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity:
  - Sell-side liquidity:
- **Ghi chú quan trọng**:
  - 

![[Pasted image 20260620062648.png]]

---

### H1

- H1 Bias: Giá trong nhịp hồi - Bearish. Chờ H1 align với khung D1
- Giá tạo 1 Order Block khung H1 từ phiên New York hôm trước

- **Cấu trúc H1**: HH/HL
- **Dealing Range chính**:
  - High: 
  - Low:
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block: Có
  - FVG: Có
  - Breaker:
  - Other: 
- **Liquidity cần chờ sweep**:
  - Chờ quét OB + old lows
- **Kịch bản mong muốn**:
  - Sau khi quét old lows, giá đảo chiều với MSS
  - MSS + Dsiplacement và quan trọng là có FVG
  - Giá retrace về FVG và tăng mạnh

![[Pasted image 20260620062706.png]]

---

### M15 / M5
- Giá retrace về vùng OB H1
- Chờ giá xuyên qua OB -> ko vào lệnh ngay khi giá chạm
- Vào khung M1 tìm tín hiệu MSS

- **Giá đã vào POI chưa?** Yes 
- **Có Liquidity Sweep chưa?** Yes
- **Sweep loại nào?**
  - Internal liquidity
- **Có Displacement chưa?** Yes
- **Có MSS chưa?** Yes
- **Có FVG hợp lệ chưa?** Yes
- **Entry có nằm trong POI không?** Yes

![[Pasted image 20260620062725.png]]

---

### M1 Entry Timeframe

- Giá quét qua vùng 50% (mean threshold) của OB
- Giá bật lên tạo thành 1 MSS
- Đồng thời giá tạo FVG trên đường di chuyển displacement
- Chờ giá hồi về vùng FVG
- Entry khi giá bật lên sau khi fill 50% FVG

- **Entry trigger**:
  - Liquidity Sweep: Quét OB
  - MSS: Có
  - Displacement: Có
  - FVG: Có
  - OB: Có
- **Entry reason**:
  - Có MSS + Dsiplacement + FVG
  - Giá retrace về FVG
- **Invalidation reason**:
  - 
- **Tôi có chờ đủ điều kiện không?** Yes
![[Pasted image 20260620062747.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [x] Đã xác định Daily Bias rõ ràng
- [x] Bias không mâu thuẫn với H1/M15
- [x] Giá đã vào vùng POI hợp lệ
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng
- [x] Có Market Structure Shift hợp lệ
- [x] Entry nằm trong FVG / OB / PD Array hợp lệ
- [x] Stop loss đặt ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt yêu cầu
- [x] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [x] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng Bias
- Xác định đúng POI khung H1
- Kiên nhẫn chờ H1 bias và D1 bias align
- Kiên nhẫn chờ giá quay về vùng POI
- Xuống khung M1 quan sát, kiên nhẫn chờ MSS + FVG hợp lệ
- Vào lệnh khi giá reject tại FVG mới tạo thay vì vào đuổi lệnh

### Điều tôi làm sai

- Chốt lời tất cả tại 1 điểm thay vè chốt từng phần

### Tâm lý khi vào lệnh

- Bình tĩnh
- Ghi chú:
  - Vào lệnh đúng setup
  - Kiên nhẫn chờ setup hình thành

### Có tuân thủ plan không?

- **Yes 
- Nếu không, tôi đã phá rule nào?
  - 

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit TP
- **Mistake chính**:
  
- **Nguyên nhân gốc rễ**:
  - 
- **Tại sao lệnh này thua/thắng?**
  - Kiên nhẫn chờ setup hình thành
  - vào lệnh khi có đủ các điều kiện
  - Không FOMO đuổi theo lệnh
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - 
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Chố lời từng phần

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Chốt lời từng phần (Partially Take Profit) — vẫn giữ, nhưng cần đo được: chốt 50% tại 1R, dời SL về BE, chốt phần còn lại tại TP gốc hoặc trailing theo cấu trúc M1 mới. Chưa có ngưỡng cụ thể trong file gốc nên chưa kiểm tra được đã thực hiện đúng chưa ở các lệnh sau.
- MSS/Displacement/FVG được tick đủ 5/5 ở mục M15-M5 và lặp lại ở M1 — đây là lệnh hiếm trong sample có đủ cả ba điều kiện entry cùng lúc theo đúng thứ tự D1→H1→M15/M5→M1 (xem O2). Giá trị học ở đây là *trình tự*, không phải kết quả Win — outcome không xác nhận trình tự đúng, trình tự tự nó đứng độc lập với kết quả (xem mục 8 §2 concede).
- Chốt toàn bộ tại một điểm (thay vì chia phần) là quyết định quản lý lệnh, không phải lỗi entry — hai loại lỗi này không nên gộp khi tính điểm tổng, vì gộp sẽ làm điểm "Entry Execution" (10/10 ở mục 7) và điểm "chốt lời" bị đánh giá bằng nhau dù thuộc hai giai đoạn khác nhau của lệnh.

### Bài học tâm lý

- Kiên nhẫn chờ setup hình thành (Patience) — giữ nguyên, đây là hành vi có thể lặp lại: không entry khi giá mới retest OB mà chưa xuống M1 xác nhận MSS+FVG.
- Cảm giác "Bình tĩnh" tự ghi nhận tại thời điểm entry — nhưng đây là self-report tại một lệnh Win; theo CS-O2/CS-O4, cảm giác kỷ luật không được xác nhận độc lập (không có nhật ký "đã bỏ qua bao nhiêu lệnh vì thiếu MSS" để so sánh) — [UNSUPPORTED] nếu dùng lệnh này làm chứng cứ "tôi luôn kiên nhẫn".

### Bài học quy trình & risk

- **risk_percent: 5%** cùng mistake tag 07 ("Risk more than 0.5% total account") xuất hiện đồng thời trong chính file này — đây là 1 trong 4/8 lệnh có risk 5% được tự gắn nhãn breach thật theo CS-O1. Bài học: risk 5% ở lệnh này KHÔNG được lesson section nào của bản gốc đề cập — mistake tag có nhưng không có dòng "Lesson Learned" tương ứng nói về risk. Đây là khoảng trống cần bổ sung, không phải suy luận thêm của agent này.
- planned_rr 1.92 khớp đúng phép tính từ entry/SL/TP (risk 27.3 điểm, reward 52.5 điểm) — RR arithmetic PASS, không phải vấn đề ở lệnh này.

### Rule cần thêm/cập nhật

- [ ] Khi risk_percent ghi 5%, BẮT BUỘC thêm một dòng "Lesson Learned" giải thích lý do (sub-account khác, hay breach thật) — điều kiện đo: mọi file có mistake tag 07 phải có ≥1 dòng lesson risk tương ứng. File này hiện KHÔNG có (liên kết O1 fatal).
- [ ] Tách chốt lời (exit management) khỏi Entry Execution khi tính Final Grade — điều kiện đo: nếu "chốt hết 1 điểm" được ghi là lỗi ở mục 4, điểm "Entry Execution" ở mục 7 (nếu áp dụng bảng chấm) không được là 10/10 do cùng một lệnh có ghi nhận lỗi thực thi.
- [ ] Khi checklist tick 13/13 "x" đồng loạt như ở đây, thêm timestamp tick (trước/sau entry) — điều kiện đo: checklist phải có cột "ticked_at" để phân biệt tick pre-trade thật với tick hồi tố khi ghi log (liên kết CS-O9, minor, xuất hiện ở file khác trong sample).

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone

---

## 7. Final Grade

| Tiêu chí         | Điểm  |
| ---------------- | ----- |
| Daily Bias       | 8/10  |
| POI Selection    | 10/10 |
| Liquidity Sweep  | 8/10  |
| MSS Confirmation | 10/10 |
| Entry Execution  | 10/10 |
| Risk Management  | 7/10  |
| Psychology       | 8/10  |

**Overall Grade**: 8.7/10

**Trade Quality**: A

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose + frontmatter only, không có chart nào đọc được (`![[Pasted image ...]]` không tồn tại trong dataset) → mọi MSS/Displacement/FVG/Sweep là **claim của user**, không phải evidence xác nhận. Sufficiency: **thin** — load-bearing claim (MSS + Displacement + FVG hợp lệ tại M1) không kiểm được từ bất cứ gì ngoài chính lời user tự thuật.

**Thesis & claims**:
- **C1**: D1 bias bullish, H1 retrace bearish rồi align lại với D1 (load-bearing cho hướng Long).
- **C2**: Giá vào POI (OB H1) → sweep internal liquidity → displacement → MSS tại M1 → FVG hình thành trên chân displacement → entry tại 50% FVG fill (**load-bearing** — đây là điều kiện entry theo đúng doctrine, nếu sai thì cả setup mất mandate).
- **C3** (từ C1+C2): Setup hợp lệ theo ICT 2022 Model, dẫn tới Win đúng quy trình (không phải ăn may).
- **C4**: risk_percent 5% là breach 10× rule 0.5% (tự gắn mistake tag 07).

**Điều gì đứng vững**: Trình tự D1→H1→M15/M5→M1 được tuân thủ đúng thứ tự nesting (không nhảy cóc TF) — đây là điểm hiếm trong sample (xem CS-O2/CS-O8 nói về rule drift ở các lệnh khác). RR thực tế 1.92 khớp đúng phép tính entry/SL/TP (risk 27.3đ, reward 52.5đ) — không có mâu thuẫn arithmetic. Checklist và narrative đồng nhất (không tự mâu thuẫn như CS-O9 ở file khác).

**Objections**:

**O1 · [METHOD] · fatal · attacks C4**
Claim: risk_percent 5% trong file này là một chi tiết phụ, không ảnh hưởng đánh giá "trade quality A / 8.7-10".
Fails: đây là 1/8 lệnh CS-O1 xác định có risk 5% VÀ tự gắn mistake tag 07 — chính user, tại thời điểm ghi log, phân loại đây là breach thật (0.5% total account), không phải lỗi ghi chép hay sub-account khác. CS-O1 (trích).
Consequence: điểm "Risk Management: 7/10" ở mục 7 không giải thích được nếu risk thật là 10× rule đã công bố — 7/10 có vẻ là "trừ điểm nhẹ" cho một breach mà theo đúng rule 0.5% phải là vi phạm nghiêm trọng, không phải điểm trừ nhỏ. Đồng thời Overall Grade 8.7/10 = A không có dòng nào cảnh báo compounding risk-of-ruin nếu 5% lặp lại (xem CS-O7).
Your best answer: "5% ở đây có thể do tính sai đơn vị risk, không phải breach thật." — Không cứu được: chính file tự gắn tag 07 "Risk more than 0.5% total account", nghĩa là user tại thời điểm ghi đã đọc đây là vi phạm trên tổng account, không phải nhầm đơn vị.
Retracted by: xác nhận từ user rằng risk_percent ở đây đo trên một sub-account nhỏ hơn tổng account dùng để tính ngưỡng 0.5% — hiện không có trong file.

**O2 · [UNSUPPORTED] · material · attacks C2 (load-bearing)**
Claim: MSS tại M1 là một "Market Structure Shift hợp lệ" theo doctrine (reversal sau sweep + displacement).
Fails: không có timestamp, không có mức giá cụ thể nào của swing bị phá cho MSS này — toàn bộ mô tả là văn xuôi ("giá bật lên tạo thành 1 MSS"). Không có gì để phân biệt một MSS thật (body close phá swing ngược ngắn hạn) với một continuation bật nhẹ được gọi tên MSS.
Consequence: load-bearing claim của cả thesis (C2) đứng trên lời tự thuật, không trên bằng chứng kiểm được — Overall Grade "MSS Confirmation: 10/10" là tự chấm, không phải điểm được xác nhận độc lập.
Your best answer: "Checklist tick x cho MSS, đó là xác nhận." — Tick là claim (nguyên tắc 7 của ict-doctrine: hình vẽ/tick của user là claim, không phải evidence); tick không tự nó chứng minh MSS đúng định nghĩa.
Retracted by: chart M1 thật kèm mức giá của swing bị phá và nến đóng cửa xuyên qua nó.

**O3 · [ARITHMETIC]/[METHOD] · material · attacks C3**
Claim: lệnh Win này chứng minh quy trình đúng (không phải ăn may như `Win-01-06-02` cùng tháng).
Fails: đây chính là điểm mù outcome-as-evidence mà CS-O2 nêu — kết luận "quy trình đúng" chỉ được phép rút ra từ việc *kiểm từng điều kiện độc lập với outcome*, không phải từ việc lệnh này Win còn `06-02` tự nhận "ăn may". So sánh khập khiễng: 05-15 có 5/5 tick đủ ở M15/M5 + đủ lại ở M1 (nếu tick đúng), còn `06-02` tick MSS=No, FVG=No nhưng vẫn Win — hai lệnh Win với chất lượng process khác biệt rõ đang bị gộp vào cùng win-rate 56% (CS-O6/mục 4 cross-setup) như hai sự kiện tương đương.
Consequence: Grade 8.7/10 "A" của lệnh này không sai vì nó Win — nó chỉ đúng NẾU các tick M1 (O2) là thật. Nhưng cùng lúc, không nên dùng cặp (05-15 Win-A vs 06-02 Win-D) để suy ra "process A luôn thắng, process D chỉ ăn may" — cả hai đều N=1.
Your best answer: không cần — đây là ghi nhận biên về cách đọc so sánh, không phải điểm phủ nhận riêng lệnh 05-15.
Retracted by: không cần discharge riêng — objection này giới hạn cách diễn giải, không đòi bằng chứng mới.

**Minor:**
- **O4 · [DOCTRINE] · minor · attacks C1** — "Discount" được ghi trong Premium/Discount nhưng không có High/Low của dealing range H1 nào được điền (`High:`, `Low:` trống) → không kiểm được midpoint để xác nhận đúng là discount. Retracted by: điền High/Low H1 thật của dealing range dùng để tính.

Drafted 5, cut 1 (một draft về "chốt lời 1 điểm thay vì chia phần" bị cắt vì user đã tự nhận đúng trong mục 4, rebuttal test không còn gì để thêm).

**Verdict: SURVIVES, WEAKENED.**
Tôi đã tấn công load-bearing claim (MSS tại M1, O2) và không phá được nó thành FAIL — vì không có chart để chứng minh sai, chỉ có thể hạ xuống UNSUPPORTED. Tôi cũng tấn công cách dùng lệnh này để chứng minh "quy trình A luôn thắng" (O3) và risk 5% ẩn dưới điểm Grade cao (O1, fatal) — O1 đứng vững vì chính file tự mâu thuẫn giữa breach thật và điểm "Risk Management 7/10".
Critique này KHÔNG xác lập: (1) MSS/FVG/Displacement mô tả trong file là sai — chỉ là chưa kiểm được; (2) Grade A/8.7 là "gian lận" — chỉ là điểm risk không phản ánh đúng mức độ breach đã tự nhận.

## 9. Opposite Case (Counter-Argument)

Load-bearing claim của kèo ngược: "MSS tại M1" mà user mô tả thực chất là **internal grab trong một continuation bullish đã có sẵn từ D1**, không phải reversal thật — giá H1 đang trong nhịp hồi bearish (tự ghi "H1 Bias: Giá trong nhịp hồi - Bearish"), và cú "bật lên" ở M1 sau khi quét 50% OB có thể đọc như tiếp diễn của D1 bullish trend đang tái khẳng định, không phải một MSS độc lập đảo chiều nhịp H1. Dưới reading này, FVG không phải "FVG của MSS hợp lệ" mà là một gap continuation bình thường trong trend D1 — lý do lệnh Win không phải vì MSS đúng, mà vì bias D1 đúng hướng và giá tiếp tục đi theo nó bất kể M1 có MSS thật hay không.

Tự đánh kèo ngược: nếu đúng là continuation thuần D1, thì tại sao user cần chờ tới M1 và tận dụng đúng FVG 50% fill để entry — một continuation thuần túy không cần điều kiện entry chặt như vậy để vẫn sinh lời; sự trùng khớp giữa "đợi FVG 50%" và điểm entry thực tế gợi ý có tồn tại một cấu trúc M1 thật, không chỉ là trôi theo D1.

Strength label: **weaker but non-trivial** — thesis gốc (MSS thật) được ưu tiên hơn vì user có mô tả trình tự Sweep→Displacement→MSS→FVG đúng thứ tự nesting, nhưng kèo ngược sẽ mạnh lên đáng kể nếu có bằng chứng giá H1 tiếp tục xu hướng bullish D1 mà không hề có một swing ngược nào đủ ý nghĩa bị phá tại M1.

Observable phân biệt hai reading: mức giá cụ thể của swing-low bị phá bởi nến MSS trên M1 và liệu nến đó có đóng cửa (body close) vượt qua swing đó hay chỉ là wick — nếu có body close phá swing ngược ngắn hạn thật, thesis gốc thắng; nếu không, kèo ngược (continuation, không MSS) thắng.

## 10. Falsification Tests

1. **Test MSS thật** (đóng O2): lấy 20 lệnh NDX M1 tự nhận "MSS + Displacement + FVG" đủ cả ba trong sample, đối chiếu với chart gốc (nếu có) xem swing bị phá có body close hay chỉ wick. ≥15/20 có body close → nâng độ tin của mô tả M1 trong toàn sample lên `partial`; nếu ngược lại, mọi "MSS=Yes" trong journal cần đọc như UNSUPPORTED mặc định.
2. **Test risk 5% có hệ thống** (đóng O1): kiểm log broker/prop-firm thật của giai đoạn 05-15 xem risk % thực đo trên account nào — nếu khớp sub-account nhỏ hơn, O1 hạ từ fatal xuống minor; nếu khớp tổng account, O1 giữ nguyên fatal.
