---
date: 2026-05-13
symbol: NDX
position: Long
result: Loss
session: London
setup: "[[Trading Journal/03 - Playbooks/3.2 - Setups/Venom Model]]"
entry_model: Venom Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,150.00
take_profit: 29,292.00
stop_loss: 29,085.60
pnl: -129
r_multiple:
risk_percent: 5%
mistakes:
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[07-Mistake-Risk-more-than-0.5-total-account]]"
tags:
planned_rr: 2.2
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 1, minor: 1}
da_opposite_case: "not applicable (duplicate note)"
---

# Trade 2026-05-13 - NDX Long Loss

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Loss                                              |
| Session         | London                                            |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M1                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           | 29,150.00                                         |
| Stop Loss       | 29,085.60                                         |
| Take Profit     | 29,292.00                                         |
| PnL             | -129                                              |
| R Multiple      | 2.60                                              |

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

![[Pasted image 20260620070643.png]]

---

### H1

Giá đang trên đường hồi về OB khung H1

- **Cấu trúc H1**: HH/HL
- **Dealing Range chính**:
  - High:
  - Low:
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block:
  - FVG:
  - Breaker:
  - Other:
- **Liquidity cần chờ sweep**:
  - 
- **Kịch bản mong muốn**:
  - 

![[Pasted image 20260620070653.png]]

---

### M15 / M5
- Giá có 1 pha quét thanh khoản 1 đáy trước đó và hình thành MSS trong khung nhỏ, tuy nhiên giá chưa về tới OB
- Entry khi xuất hiện MSS và retrace

- **Giá đã vào POI chưa?** No
- **Có Liquidity Sweep chưa?** No
- **Sweep loại nào?**
  - Internal liquidity / External liquidity / Equal Highs / Equal Lows
- **Có Displacement chưa?** No
- **Có MSS chưa?** Yes / No
- **Có FVG hợp lệ chưa?** Yes / No
- **Entry có nằm trong POI không?** Yes / No

![[Pasted image 20260620070706.png]]

---

### M1 Entry Timeframe

- **Entry trigger**:
  - Liquidity Sweep:
  - MSS:
  - Displacement:
  - FVG:
  - OB:
- **Entry reason**:
  - 
- **Invalidation reason**:
  - 
- **Tôi có chờ đủ điều kiện không?** Yes / No
![[Pasted image 20260620070719.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [ ] Đã xác định Daily Bias rõ ràng
- [ ] Bias không mâu thuẫn với H1/M15
- [ ] Giá đã vào vùng POI hợp lệ
- [ ] Có Liquidity Sweep trước entry
- [ ] Có Displacement rõ ràng
- [ ] Có Market Structure Shift hợp lệ
- [ ] Entry nằm trong FVG / OB / PD Array hợp lệ
- [ ] Stop loss đặt ở vùng invalidation hợp lý
- [ ] RR tối thiểu đạt yêu cầu
- [ ] Đã kiểm tra tin tức quan trọng
- [ ] Không vào lệnh vì FOMO
- [ ] Không revenge trade
- [ ] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- 

### Điều tôi làm sai

- 

### Tâm lý khi vào lệnh

- Bình tĩnh / FOMO / Sợ lỡ kèo / Revenge trade / Không chắc chắn
- Ghi chú:
  - 

### Có tuân thủ plan không?

- **Yes / No**
- Nếu không, tôi đã phá rule nào?
  - 

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit SL (khớp exit_price = stop_loss = 29,085.6 theo bản trùng có prose đầy hơn — xem ghi chú trùng lệnh ở mục 8).
- **Mistake chính**:
  - [[02-Mistake-Enter-before-liquidity-sweep]]
- **Nguyên nhân gốc rễ**:
  - [[02-Mistake-Enter-before-liquidity-sweep]]
  - [[07-Mistake-Risk-more-than-0.5-total-account]]
- **Tại sao lệnh này thua/thắng?**
  - `(field trống trong bản gốc — không điền phân tích mới ngoài dữ kiện đã có trong file, theo brief: không bịa phân tích cho nội dung không thuộc lệnh này)`.
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - `(trống trong bản gốc)`.
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - `(trống trong bản gốc)`.

---

## 5. Lesson Learned

### Bài học kỹ thuật

- (Bản gốc để trống — mọi mục Lesson Learned, Rule cần thêm/cập nhật đều trống hoàn toàn trong file này.)
- Mistake tag `[[02-Mistake-Enter-before-liquidity-sweep]]` khớp trực tiếp với narrative M15 "tuy nhiên giá chưa về tới OB" trong bản trùng — nghĩa là entry xảy ra trước khi sweep chuẩn diễn ra, đúng như tag mô tả (O1, xem mục 8).

### Bài học tâm lý

- (Bản gốc để trống — không có dữ kiện tâm lý nào trong file này để mở rộng; bản trùng có field Emotions: Greedy, file này không có.)

### Bài học quy trình & risk

- risk_percent = 5% ghi rõ trong file này, khác với bản trùng (risk_percent để trống) — chênh lệch này là phần "khác" duy nhất đáng chú ý giữa hai bản, và tự nó gắn tag mistake 07 (breach risk 0.5%) — điều bản trùng KHÔNG làm (O1, liên hệ CS-O1).
- entry_model ghi "Venom Model" trong frontmatter nhưng H1 Value trong bảng Trade Summary (dòng "Entry Model") lại ghi "Liquidity Sweep + MSS + FVG / OB Reaction / Other" — hai mô tả entry_model khác nhau trong cùng file (O2).

### Rule cần thêm/cập nhật

- [ ] **KIỂM TRA ĐƯỢC**: khi hai file mô tả cùng một lệnh (entry/SL/TP giống nhau tuyệt đối), risk_percent phải được đồng bộ giữa hai bản — nếu một bản ghi 5% và bản kia để trống, đây là dữ liệu không đáng tin cho cả hai đến khi xác nhận số đúng (đóng O1).
- [ ] **KIỂM TRA ĐƯỢC**: field entry_model trong frontmatter phải khớp với dòng "Entry Model" trong bảng Trade Summary — kiểm bằng so khớp text hai chỗ trước khi lưu file (đóng O2).

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone

---

## 7. Final Grade

| Tiêu chí | Điểm |
|---|---|
| Daily Bias | /10 |
| POI Selection | /10 |
| Liquidity Sweep | /10 |
| MSS Confirmation | /10 |
| Entry Execution | /10 |
| Risk Management | /10 |
| Psychology | /10 |

**Overall Grade**: /10

**Trade Quality**: A / B / C / D / F

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Ghi chú trùng lệnh (bắt buộc đọc trước)**: File này và `Loss-01-Trade-2026-05-13-NDX-Long-1.md` mô tả **cùng một lệnh** — entry 29,150.00 / SL 29,085.60 / TP 29,292.00 giống nhau tuyệt đối; pnl -129 (file này) vs -129.6 (bản `-1`), chênh 0.6 nhiều khả năng do rounding phí giao dịch. Xem **CS-O0′ · [ARITHMETIC] · material** (`cross_setup_findings.md` mục 1) — hai bản ghi khác template cho cùng một lệnh làm phình sample N=27 thành N=25 thật. Bản `-1` có nội dung phong phú hơn (prose D1/H1/M15/Result, checklist tick, emotions, confidence) và đã được phân tích ĐẦY ĐỦ ở đó, bao gồm objection load-bearing chính (O1: entry_model claim MSS+FVG+P/D mâu thuẫn với narrative "giá chưa về tới OB"). Phần dưới đây **chỉ phản biện nội dung KHÁC giữa hai bản** — không lặp lại phân tích structure/POI đã có ở bản `-1`.

**Evidence base**: Prose rất mỏng (D1/H1/M15/M1 hầu hết trống, template chưa điền) + 3 link chart Obsidian chết. Sufficiency: **thin** — phần khác biệt duy nhất có thể kiểm là arithmetic frontmatter (risk_percent, entry_model text), không cần chart.

**Thesis & claims (chỉ phần khác biệt)**:
- C1 (load-bearing cho phần khác biệt): risk_percent = 5% là số risk thật đã dùng cho lệnh này.
- C2: entry_model = "Venom Model" là chiến lược đã áp dụng.
- C3: mistake tags `[[02 - Enter before liquidity sweep]]` và `[[07 - Risk >0.5%]]` phản ánh đúng 2 lỗi đã xảy ra.

**Điều gì đứng vững**: Mistake tag 02 (enter before liquidity sweep) khớp nhất quán với narrative M15 của bản `-1` ("giá chưa về tới OB") — đây là điểm hai bản đồng thuận dù template khác nhau, làm tăng độ tin cậy cho chính objection O1 đã nêu ở bản `-1`. Arithmetic RR (2.2) khớp giữa hai bản.

**Objections (chỉ phần khác biệt)**:

**O1 · [ARITHMETIC] · fatal · attacks C1**
Claim: risk_percent = 5% cho lệnh entry 29,150/SL 29,085.6.
Evidence: Bản `-1` (cùng entry/SL/TP tuyệt đối) để trống hoàn toàn field risk_percent. Không có cách nào từ dữ kiện hai file xác định risk % thật — 5% hay không xác định.
Consequence: nếu 5% đúng, đây là breach 10× rule 0.5% (đã tự gắn tag 07 xác nhận là breach thật, không phải lỗi ghi chép — theo logic CS-O1: 4/8 lệnh risk 5% có gắn tag 07, đúng như CS-O1 dự đoán "chính người dùng, tại thời điểm ghi journal, đã phân loại đây là breach thật"). Nếu bản `-1` (risk_percent trống) là bản đáng tin hơn, thì số 5% này không có cơ sở đối chiếu.
Your best answer: "Đây có thể là re-entry riêng biệt với risk khác, không phải cùng lệnh." — Không loại trừ được (xem CS-O0′), nhưng không có timestamp phân biệt nào giữa hai file.
Retracted by: xác nhận từ user đây là 1 lệnh duy nhất (risk 5% đúng, cần sửa bản `-1`) hoặc 2 lệnh riêng biệt (risk 5% chỉ áp dụng cho lệnh này).

**O2 · [SELF-CONTRADICTION] · material · attacks C2**
Claim: entry_model (frontmatter) = "Venom Model".
Evidence: Bảng Trade Summary, dòng "Entry Model" = "Liquidity Sweep + MSS + FVG / OB Reaction / Other" — không nhắc "Venom" ở đâu cả trong phần thân bài, khác hoàn toàn với frontmatter.
Consequence: không rõ chiến lược thật đã áp dụng là Venom Model (một mô hình riêng, dùng BPR/Venom box theo các file khác trong sample như `Win-01-05-13`/`Win-02-05-13`) hay ICT 2022 Model chuẩn (Liquidity Sweep + MSS + FVG) — hai mô hình có tiêu chí entry khác nhau, không tương đương.
Your best answer: dòng "Entry Model" trong bảng có thể là text mặc định của template chưa được cập nhật khi đổi sang Venom Model. — Có khả năng, nhưng nếu đúng thì đây là lỗi điền template lặp lại (không riêng lệnh này), và không giải thích được tại sao narrative M15/M1 cũng không có bất kỳ nhắc nào đến "Venom", "BPR", hay "Venom box" — các thuật ngữ đặc trưng của Venom Model đều vắng mặt trong toàn bộ phần thân bài.
Retracted by: một câu narrative nào trong file nhắc đến thuật ngữ Venom Model — hiện không có.

**O3 · [METHOD] · minor** — Toàn bộ checklist section 2 (13 dòng) unchecked `[ ]` 100% — khác hẳn với checklist section 2 của bản `-1` (11/11 tick `[x]`) cho cùng một lệnh. Hai checklist khác template (13 dòng vs 11 dòng) và khác trạng thái tick hoàn toàn, không thể đối chiếu chéo được. Retracted by: không cần — đây chỉ là cảnh báo không thể dùng checklist của file này để kiểm định gì thêm ngoài những gì bản `-1` đã cung cấp.

Drafted 3, cut 0.

**Verdict**: **BROKEN** — phần khác biệt duy nhất có giá trị kiểm định (risk_percent 5% vs trống) tự mâu thuẫn giữa hai bản của cùng một lệnh, không thể xác định số nào đúng (O1); entry_model cũng tự mâu thuẫn giữa frontmatter và bảng summary (O2). Struture/POI thesis chính đã BROKEN ở bản `-1` qua O1 (self-contradiction "giá chưa về tới OB").
Tôi đã tấn công gì mà không phá được: tag mistake 02 (enter before sweep) — nhất quán với bản `-1`, không mâu thuẫn.
Critique này KHÔNG xác lập: (1) risk % thật của lệnh (5% hay khác); (2) liệu đây thật là Venom Model hay ICT 2022 Model chuẩn; (3) liệu đây và bản `-1` là 1 hay 2 sự kiện giao dịch khác nhau — không có timestamp để phân biệt.

**Opposite Case**: Không áp dụng đầy đủ theo cấu trúc thường lệ vì file này là bản trùng lệnh nghèo nội dung — kèo ngược thật (đổi vai narrative cho thesis structure) đã được xử lý ở bản `-1`. Với riêng phần khác biệt (risk 5%, entry_model Venom): kèo ngược khả dĩ duy nhất là "đây là 2 lệnh riêng biệt, không phải 1 lệnh trùng" — nhưng không có fact nào (timestamp, session khác biệt rõ) hỗ trợ, nên **not viable** để dựng thành kèo ngược có sức nặng.
Strength label: **not applicable (duplicate note)**.
Observable duy nhất phân biệt: timestamp thực thi (giờ:phút) của hai file — nếu khác nhau đủ xa trong ngày 05-13, có thể là 2 lệnh; nếu không có timestamp nào khác `date:` (chỉ có ngày, không giờ), không phân biệt được.

## 9. Opposite Case (Counter-Argument)

(Xem mục 8 — theo ghi chú trùng lệnh, opposite case đầy đủ nằm ở `Loss-01-Trade-2026-05-13-NDX-Long-1.md`; phần trên chỉ xử lý phần khác biệt.)

## 10. Falsification Tests

1. **Test cho O1**: Xác nhận từ user (hoặc broker statement) risk % thật đã dùng cho entry 29,150 ngày 05-13 — nếu 5%, sửa bản `-1` để khớp; nếu khác, sửa bản này.
2. **Test cho O2**: Tìm narrative gốc (nếu còn lưu ở nơi khác) có nhắc "Venom"/"BPR"/"Venom box" cho lệnh này — nếu có, entry_model Venom đúng và dòng "Entry Model" trong bảng summary là lỗi template; nếu không, nghi vấn Venom Model chỉ là gắn nhãn sai.
