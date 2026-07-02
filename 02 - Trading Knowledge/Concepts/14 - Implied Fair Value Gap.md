---
type: ict-concept
concept: "Implied Fair Value Gap"
aliases:
  - Implied FVG
  - IFVG (Implied)
  - Implied Fair Value Gap
tags:
  - trading/ict/concept
  - trading/study
  - "#ImpliedFVG"
status: developing
category: PD Array
timeframes:
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[Trading Journal/02 - Trading Knowledge/Models/ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-23
created: 2026-06-23
updated: 2026-06-23
common_mistakes:
  - "[[Mistake - Trade Every FVG]]"
  - "[[Mistake - FVG Without Displacement]]"
---

# Implied Fair Value Gap

> [!summary] Tóm tắt 1 câu
> **Implied Fair Value Gap (Implied FVG) là một dạng imbalance tinh tế: trên cụm 4 nến, hai nến thân lớn nằm cạnh nhau có bóng nến chồng lấp nhưng cấu trúc tổng thể vẫn "ngụ ý" (imply) sự kém hiệu quả — vùng imbalance ẩn được xác định bằng khoảng giữa TRUNG ĐIỂM bóng phía trên của nến thấp và TRUNG ĐIỂM bóng phía dưới của nến cao.**

> [!important] Phân biệt rõ — KHÔNG nhầm với Inverse FVG
> **"Implied FVG" (ngụ ý / ẩn) ≠ "Inverse FVG" (đảo cực).**
> - **Implied FVG:** imbalance ẩn trong mô hình 4 nến mà FVG 3-nến tiêu chuẩn không hiện rõ trên chart; xác định bằng trung điểm các bóng nến.
> - **[[17 - Inverse Fair Value Gap - iFVG]]:** một FVG bình thường bị giá đóng nến xuyên qua nên ĐẢO CỰC vai trò S/R.
> Đây là hai khái niệm hoàn toàn khác nhau — đừng gộp lẫn.

---

## 1. Định nghĩa

**Khái niệm:**
Implied Fair Value Gap là một vùng **imbalance ẩn (hidden inefficiency)** không hiển thị như một [[Fair Value Gap]] 3 nến tiêu chuẩn. Trên một cụm **4 nến**, ta có **hai nến thân lớn (large-bodied)** nằm cạnh nhau (thường là nến 2 và nến 3 của cụm); bóng nến của chúng **chồng lấp** nhau nên KHÔNG để lại một gap 3-nến rõ ràng. Tuy vậy, cấu trúc tổng thể vẫn "ngụ ý" rằng có vùng giá chưa được giao dịch đầy đủ.

Cách xác định Implied FVG:
- Lấy **trung điểm bóng phía trên (upper wick midpoint)** của nến lớn **thấp hơn** trong hai nến.
- Lấy **trung điểm bóng phía dưới (lower wick midpoint)** của nến lớn **cao hơn**.
- Khoảng giữa hai mức trung điểm này chính là **Implied FVG** — vùng imbalance ẩn.

Nói cách khác: ở một FVG thường, gap nằm giữa hai biên giá rõ ràng (high nến 1 và low nến 3). Ở Implied FVG, vì bóng nến chồng lấp che mất gap, ta dùng **trung điểm các bóng nến lớn** làm biên của vùng imbalance ẩn. Đây là cách ICT "đọc" inefficiency ngay cả khi mắt thường không thấy một FVG kinh điển.

**Mục đích trong ICT:**
- Phát hiện **POI / imbalance ẩn** ở những nơi không có FVG 3-nến nhưng vẫn có inefficiency.
- Cung cấp thêm vùng entry tinh khi giá retrace, đặc biệt trong delivery mạnh mà bóng nến chồng lấp nhiều.
- Là draw on liquidity tinh tế: giá có thể quay về rebalance vùng implied này.
- Bổ trợ cho FVG thường khi cấu trúc không cho ra gap rõ.

**Vì sao khái niệm này quan trọng:**
Trong nhiều đợt displacement mạnh, nến nối tiếp nhau với bóng dài chồng lấp khiến FVG 3-nến không hình thành rõ — nhưng inefficiency vẫn tồn tại. Implied FVG cho phép định vị vùng phản ứng tiềm năng ở đó. Tuy nhiên nó **tinh tế và chủ quan hơn** FVG thường, nên ưu tiên thấp hơn và cần nhiều context xác nhận hơn.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Có imbalance ẩn nào ở vùng không có FVG 3-nến rõ ràng không?
- Khi giá retrace, vùng implied nào có thể làm POI phản ứng?
- Inefficiency "ngụ ý" này nằm ở premium hay discount?
- Đây có thực sự là Implied FVG, hay mình đang nhầm với một FVG thường / Inverse FVG?

### Implied Fair Value Gap không phải là gì
- **Không phải Inverse FVG** — không liên quan tới việc FVG cũ bị xuyên & đảo cực.
- Không phải FVG 3-nến tiêu chuẩn — gap bị bóng nến chồng lấp che đi.
- Không phải tín hiệu trade độc lập — vẫn cần bias + premium/discount + sweep + LTF confirm.
- Không ưu tiên cao bằng FVG rõ; dùng như bổ trợ/confluence.
- Không nên "ép" mọi cụm 4 nến thành Implied FVG — chỉ khi hai nến thực sự thân lớn và cấu trúc ngụ ý inefficiency.

---

## 2. Bối cảnh sử dụng

### So sánh ba khái niệm dễ lẫn

| Khái niệm | Bản chất | Cách xác định | Ưu tiên |
|---|---|---|---|
| **FVG thường (BISI/SIBI)** | Imbalance 3 nến rõ ràng | Gap giữa high nến 1 & low nến 3 (bullish) | Cao |
| **Implied FVG** | Imbalance ẩn trong cụm 4 nến, bóng chồng lấp | Trung điểm bóng 2 nến thân lớn | Trung bình (bổ trợ) |
| **[[17 - Inverse Fair Value Gap - iFVG]]** | FVG cũ bị đóng nến xuyên → đảo cực S/R | FVG fail + đóng nến xuyên qua | Cao (khi có MSS) |

> [!warning]
> Lỗi phổ biến nhất với khái niệm này là **gọi nhầm một Inverse FVG là "Implied FVG"** chỉ vì hai từ viết tắt na ná. Hãy nhớ: **Implied = ẩn (4 nến, trung điểm bóng); Inverse = đảo cực (FVG bị xuyên).**

### Khi nào khái niệm này có giá trị cao?
- [ ] Displacement mạnh nhưng bóng nến chồng lấp khiến FVG 3-nến không hiện rõ.
- [ ] Hai nến thân lớn liên tiếp với bóng dài chồng nhau.
- [ ] Vùng implied trùng một POI HTF / mức tham chiếu khác (confluence).
- [ ] Đồng hướng [[12 - Daily Bias]] và đúng phía premium/discount.
- [ ] Có liquidity sweep trước cụm nến tạo implied.

### Khi nào nên bỏ qua?
- [ ] Có sẵn một FVG 3-nến rõ ràng gần đó — ưu tiên FVG rõ hơn.
- [ ] Hai nến không thực sự thân lớn (ép mô hình).
- [ ] Vùng implied giữa range / sai phía premium-discount.
- [ ] Ngược bias, không có sweep, không có LTF confirm.
- [ ] Đang nhầm với Inverse FVG → dừng lại, đọc lại định nghĩa.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Cụm 4 nến:** xác định cụm nến, trong đó có **hai nến thân lớn** liên tiếp.
2. **Bóng nến chồng lấp:** bóng của hai nến lớn giao nhau → không có FVG 3-nến rõ.
3. **Trung điểm bóng:** lấy midpoint bóng trên của nến lớn thấp & midpoint bóng dưới của nến lớn cao.
4. **Vùng implied:** khoảng giữa hai trung điểm = Implied FVG.
5. **CE của implied:** mức 50% của vùng implied (xem [[Consequent Encroachment]]) là điểm phản ứng tinh.

### Ma trận nhận diện

| Thành phần | Bullish Implied FVG | Bearish Implied FVG | Cảnh báo / nhầm lẫn |
|---|---|---|---|
| **Hai nến lớn** | Hai nến tăng thân lớn liên tiếp | Hai nến giảm thân lớn liên tiếp | Nến nhỏ/doji → không phải implied |
| **Biên trên vùng** | Midpoint bóng dưới của nến cao | Midpoint bóng trên của nến cao | Lấy nhầm high/low thay vì midpoint |
| **Biên dưới vùng** | Midpoint bóng trên của nến thấp | Midpoint bóng dưới của nến thấp | — |
| **Bóng nến** | Chồng lấp (che FVG 3-nến) | Chồng lấp | Nếu có gap rõ → đó là FVG thường |
| **Bản chất** | Imbalance ẩn (implied) | Imbalance ẩn (implied) | KHÔNG phải Inverse FVG |

### Điều kiện bắt buộc
- [ ] Có cụm 4 nến với hai nến thân lớn liên tiếp.
- [ ] Bóng nến hai nến lớn chồng lấp (không có FVG 3-nến rõ).
- [ ] Xác định đúng trung điểm bóng của từng nến lớn.
- [ ] Xác định CE của vùng implied.

### Điều kiện tăng xác suất
- [ ] Cụm nến sinh từ displacement phá cấu trúc (BOS/MSS).
- [ ] Vùng implied trùng POI HTF / OB / equilibrium.
- [ ] Có liquidity sweep trước cụm nến.
- [ ] Đồng hướng bias và đúng premium/discount.
- [ ] LTF có MSS + phản ứng khi giá vào vùng implied.

### Điều kiện làm setup yếu đi
- Hai nến không đủ lớn → mô hình bị ép.
- Có một FVG 3-nến rõ gần đó (nên ưu tiên cái đó).
- Vùng implied giữa range / ngược bias.
- Không có sweep / không LTF confirmation.
- Nhầm lẫn với Inverse FVG.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Implied FVG
> 1. **Đây có đúng là Implied FVG (4 nến, bóng chồng, trung điểm bóng) không, hay tôi đang nhầm với FVG thường / Inverse FVG?**
> 2. **Cụm nến có sinh từ displacement phá cấu trúc, sau sweep, đúng bias không?**
> 3. **Vùng implied & CE của nó nằm ở đâu, có confluence không?**
> 4. **Có một FVG 3-nến rõ hơn để ưu tiên thay vì implied không?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **Premium/discount:** vùng implied cần Long phải ở discount; cần Short phải ở premium.
- **HTF POI:** vùng implied có nằm trong/trùng một POI HTF không.

### H1 / M15 — POI & Context
- **POI cụ thể:** ghi rõ vùng implied (hai trung điểm bóng) và CE.
- **Lý do hợp lệ:** cụm nến sinh từ displacement? sau sweep? đúng phía P/D?
- **So sánh với FVG thường:** có FVG 3-nến rõ nào đáng ưu tiên hơn không?
- **Liquidity:** giá đã sweep pool đối diện chưa.

### M5 / M1 — Confirmation & Entry
- **Có MSS không?** khi giá về vùng implied, có MSS LTF xác nhận không.
- **Có displacement LTF không?** thường tạo FVG nhỏ refine ngay quanh CE của implied.
- **Entry quanh CE của implied:** ưu tiên CE thay vì biên xa.
- **Stop logic:** ngoài biên xa vùng implied / ngoài điểm sweep.

```text
Mẫu ghi nhanh — Bullish Implied FVG Entry
HTF Bias: Bullish | Location: Discount
Cụm 4 nến: 2 nến tăng thân lớn, bóng chồng lấp (không có FVG 3-nến rõ)
Implied zone: [midpoint bóng trên nến thấp] → [midpoint bóng dưới nến cao]
CE (50%) của implied: [mid]
Sweep: đã quét SSL trước cụm nến → Yes
Có FVG 3-nến rõ hơn không? → No (nên dùng implied)
Entry plan: giá retrace về CE của implied → M5 bullish MSS + FVG nhỏ → entry quanh CE
Stop: dưới biên xa vùng implied / dưới sweep low
Target: internal liquidity trước, BSL chính sau
Invalid: đóng nến xuyên xuống dưới biên dưới vùng implied
```

> [!warning]
> Implied FVG là công cụ **bổ trợ, ưu tiên thấp hơn FVG rõ**. Nếu có một FVG 3-nến tiêu chuẩn ở vùng tương tự, hãy dùng nó. Đừng "phát minh" implied chỉ để có cớ vào lệnh.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Đúng là Implied FVG (4 nến, hai nến lớn, bóng chồng, trung điểm bóng) — không nhầm khái niệm.
- [ ] Cụm nến sinh từ displacement phá cấu trúc, sau sweep.
- [ ] Vùng implied đúng phía premium (Short) / discount (Long).
- [ ] Giá respect vùng implied / CE (reject), có LTF MSS + displacement.
- [ ] Có target liquidity rõ và R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Giá đóng nến xuyên qua biên xa vùng implied và giữ giá bên kia.
- [ ] Hai nến không đủ lớn → mô hình bị ép, không hợp lệ.
- [ ] Không có sweep / ngược bias / sai premium-discount.
- [ ] Không có LTF confirmation khi giá vào vùng implied.
- [ ] Thực ra đây là Inverse FVG hoặc FVG thường bị gọi nhầm.

### Implied FVG sau khi bị xuyên
> [!note]
> Giống FVG thường, một Implied FVG bị **đóng nến xuyên qua** có thể mất hiệu lực và **đảo cực** — lúc đó nó hành xử như một [[17 - Inverse Fair Value Gap - iFVG]] (implied). Nhưng hãy ghi rõ trong nhật ký: "Implied FVG bị xuyên → đảo cực", để không lẫn lộn khái niệm gốc với hệ quả.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Implied-Fair-Value-Gap-Example-Correct.svg]]

**Mô tả:**
Trong một đợt displacement tăng, hai nến tăng thân lớn liên tiếp có bóng chồng lấp nên không để lại FVG 3-nến rõ. Ta lấy trung điểm bóng trên của nến lớn thấp và trung điểm bóng dưới của nến lớn cao → xác định vùng Implied FVG. Cụm nến này sinh sau một sweep SSL và phá cấu trúc (bias bullish, discount). Giá retrace về CE của vùng implied, reject, M5 tạo bullish MSS → entry quanh CE → tiếp tục tăng.

**Vì sao đây là ví dụ tốt:**
- Xác định đúng vùng implied bằng **trung điểm bóng** của hai nến lớn.
- Cụm nến sinh từ displacement phá cấu trúc, sau sweep, đúng discount + bias.
- Giá respect vùng implied / CE, có LTF confirmation.
- Không có FVG 3-nến rõ hơn để ưu tiên → dùng implied hợp lý.

### Ví dụ sai / dễ nhầm
![[Implied-Fair-Value-Gap-Example-Wrong.svg]]

**Mô tả lỗi:**
Trader thấy một bullish FVG 3-nến **bị đóng nến xuyên xuống** và đảo cực — đây thực chất là một **Inverse FVG** — nhưng lại gọi nhầm nó là "Implied FVG". Việc gọi sai khái niệm dẫn tới xác định sai vùng, sai logic phản ứng (đảo cực vs imbalance ẩn) và đặt stop/entry sai chỗ.

**Bài học:**
- **Implied FVG ≠ Inverse FVG.** Implied = imbalance ẩn (4 nến, trung điểm bóng); Inverse = FVG bị xuyên & đảo cực.
- Implied FVG được xác định bằng trung điểm bóng hai nến lớn, không liên quan tới việc FVG cũ bị xuyên.
- Khi thấy FVG bị đóng nến xuyên qua, đó là [[17 - Inverse Fair Value Gap - iFVG]] — gọi đúng tên để dùng đúng logic.

---
### Sequence mẫu — Bullish Implied FVG (imbalance ẩn)
```text
HTF Bullish Bias → Location Discount
→ Sweep Sell-Side Liquidity
→ Displacement tăng: 2 nến thân lớn bóng chồng lấp (không có FVG 3-nến rõ)
→ Xác định Implied FVG = giữa 2 trung điểm bóng; tính CE của implied
→ Giá retrace về CE của implied → respect + M5 MSS/FVG nhỏ
→ Entry quanh CE; Stop dưới biên xa vùng implied / dưới sweep
→ Target: internal liquidity trước, External BSL sau
→ Invalid: đóng nến xuyên xuống dưới biên dưới vùng implied
```

### Sequence mẫu — Phân biệt với Inverse FVG (để KHÔNG nhầm)
```text
Trường hợp A — Implied FVG:
  4 nến, 2 nến lớn bóng chồng → imbalance ẩn → dùng trung điểm bóng
Trường hợp B — Inverse FVG:
  FVG 3-nến bị ĐÓNG NẾN xuyên qua → đảo cực S/R → dùng làm vùng ngược hướng cũ
→ Hai trường hợp KHÁC NHAU; ghi đúng tên trong nhật ký
```

> [!note]
> Vì Implied FVG tinh tế và chủ quan hơn, hãy luôn dùng [[10 - Consequent Encroachment (Mean Threshold)|CE]] của vùng implied làm mức tham chiếu chính và yêu cầu LTF confirmation. Nếu có một FVG 3-nến rõ, ưu tiên nó trước.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Implied FVG là bổ trợ, ưu tiên thấp hơn FVG rõ. Và trước hết: KHÔNG nhầm nó với Inverse FVG.

### A. Context (HTF)
- [ ] Daily Bias rõ: `Bullish / Bearish / Neutral`.
- [ ] Đúng là Implied FVG (4 nến, hai nến lớn, bóng chồng, trung điểm bóng).
- [ ] Cụm nến sinh từ displacement phá cấu trúc.
- [ ] Vùng implied đúng phía premium (Short) / discount (Long).
- [ ] Đã có sweep trước cụm nến.
- [ ] Không có FVG 3-nến rõ hơn để ưu tiên.

### B. Execution (LTF / khi giá tới vùng implied)
- [ ] Giá respect vùng implied / CE (reject), không đóng nến xuyên qua.
- [ ] Có LTF MSS + displacement khi giá vào vùng.
- [ ] Entry quanh CE của implied, không phải biên xa.
- [ ] Stop ngoài biên xa vùng implied / ngoài sweep.
- [ ] Target liquidity rõ; R:R đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Hai nến không đủ lớn / mô hình bị ép → không trade.
- [ ] Vùng implied giữa range / ngược bias / sai P/D → không trade.
- [ ] Chưa có sweep → không trade.
- [ ] Đang nhầm với Inverse FVG → dừng, đọc lại định nghĩa.
- [ ] Có FVG 3-nến rõ hơn → dùng cái đó thay vì implied.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Nhầm Implied với Inverse FVG | Gọi FVG bị xuyên là "Implied" | Sai logic phản ứng & vùng | Implied = ẩn (4 nến); Inverse = đảo cực |
| Ép mô hình implied | Hai nến nhỏ vẫn cố vẽ implied | Vùng vô nghĩa, nhiễu | Yêu cầu hai nến thực sự thân lớn |
| Lấy high/low thay vì trung điểm bóng | Vẽ vùng sai biên | Sai entry/stop | Dùng đúng midpoint bóng từng nến lớn |
| Ưu tiên implied hơn FVG rõ | Bỏ FVG 3-nến để chọn implied | Mất tín hiệu chất lượng cao hơn | FVG rõ ưu tiên trước, implied bổ trợ |
| Vào implied không có context | Thấy vùng là vào | Implied tinh tế, dễ sai | Cần bias + sweep + P/D + LTF confirm |
| Bỏ qua CE của implied | Vào ở biên xa | R:R kém, bỏ mức phản ứng chính | Ưu tiên entry quanh CE vùng implied |
| Không xác nhận displacement | Cụm nến không phá cấu trúc | Không có intent, dễ bị xuyên | Chỉ tính implied khi có displacement |

---

## 10. Câu hỏi tự kiểm tra

- Mình giải thích Implied FVG (4 nến, trung điểm bóng) và phân biệt với Inverse FVG trong 30 giây không?
- Đây có đúng là Implied FVG, hay là FVG thường / Inverse FVG bị gọi nhầm?
- Hai nến có thực sự thân lớn và bóng chồng lấp không?
- Vùng implied & CE của nó nằm ở đâu? Có confluence không?
- Cụm nến có sinh từ displacement phá cấu trúc, sau sweep, đúng bias không?
- Có một FVG 3-nến rõ hơn nên ưu tiên không?
- Giá đang respect vùng implied hay đã đóng nến xuyên qua?
- Setup nào trong journal đã dùng implied đúng/sai (hoặc nhầm với inverse)?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Implied Fair Value Gap là gì?
**Đáp:** Một imbalance **ẩn** trên cụm 4 nến: hai nến thân lớn có bóng chồng lấp (không có FVG 3-nến rõ) nhưng cấu trúc tổng thể ngụ ý inefficiency.

### Q2
**Hỏi:** Implied FVG được xác định bằng cách nào?
**Đáp:** Bằng **trung điểm bóng** của hai nến lớn: midpoint bóng trên của nến lớn thấp và midpoint bóng dưới của nến lớn cao; khoảng giữa hai mức đó là vùng implied.

### Q3
**Hỏi:** Implied FVG khác Inverse FVG thế nào?
**Đáp:** **Implied** = imbalance ẩn (4 nến, trung điểm bóng), FVG 3-nến không hiện rõ. **Inverse** = một FVG bình thường bị đóng nến xuyên qua nên đảo cực vai trò S/R. Hai khái niệm hoàn toàn khác nhau.

### Q4
**Hỏi:** Implied FVG khác FVG thường (3 nến) ở đâu?
**Đáp:** FVG thường có gap giữa hai biên giá rõ (3 nến). Implied FVG không có gap rõ vì bóng nến chồng lấp; phải dùng trung điểm bóng để định vùng.

### Q5
**Hỏi:** Vì sao Implied FVG có ưu tiên thấp hơn FVG rõ?
**Đáp:** Vì nó tinh tế & chủ quan hơn, dễ bị "ép" mô hình. Nếu có một FVG 3-nến rõ ở vùng tương tự thì ưu tiên FVG đó; implied chỉ là bổ trợ/confluence.

### Q6
**Hỏi:** Cần gì để một Implied FVG đáng trade?
**Đáp:** Cụm nến sinh từ displacement phá cấu trúc, sau sweep, đúng bias + premium/discount, entry quanh CE của vùng implied, và có LTF MSS/displacement xác nhận.

---

## 12. Lesson Learned

### Bài học chính
- Implied FVG = imbalance **ẩn** trên cụm 4 nến, xác định bằng **trung điểm bóng** hai nến lớn.
- **Không nhầm với Inverse FVG** — đây là lỗi nguy hiểm nhất với khái niệm này.
- Ưu tiên thấp hơn FVG 3-nến rõ; dùng như bổ trợ/confluence.
- Vẫn cần đầy đủ context: displacement + sweep + bias + premium/discount + LTF confirm.
- Dùng CE của vùng implied làm mức tham chiếu chính.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn tự hỏi "Implied hay Inverse?" trước khi dùng khái niệm này.
- [ ] Tôi chỉ vẽ implied khi hai nến thực sự thân lớn và bóng chồng lấp.
- [ ] Tôi xác định vùng bằng trung điểm bóng, không phải high/low.
- [ ] Tôi ưu tiên FVG 3-nến rõ; implied chỉ là bổ trợ.
- [ ] Tôi entry quanh CE của vùng implied với LTF confirmation.

### Câu nhắc nhở khi trade
> **"Implied là imbalance ẩn (4 nến, trung điểm bóng) — KHÔNG phải Inverse (FVG đảo cực). Có FVG rõ thì dùng FVG rõ."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt rõ Implied vs Inverse vs FVG thường không? |
| Nhận diện trên chart |  | Có xác định đúng vùng bằng trung điểm bóng hai nến lớn không? |
| Biết khi nào bỏ qua |  | Có ưu tiên FVG rõ / bỏ mô hình bị ép không? |
| Kết hợp với context HTF |  | Implied có nằm trong narrative bias + P/D + sweep không? |
| Áp dụng vào trade thực tế |  | Entry có quanh CE vùng implied với LTF confirm không? |
| Review sau trade |  | Có kiểm tra tỉ lệ nhầm Implied↔Inverse bằng journal không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 15–25 setup có gắn tag `[[Implied Fair Value Gap]]`.
- [ ] Đếm số lần gọi nhầm Implied ↔ Inverse FVG để siết kỷ luật khái niệm.
- [ ] So sánh win rate implied khi có vs không có FVG 3-nến rõ bên cạnh.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## Appendix — Implied FVG Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish / Neutral
> **Xác nhận: Implied (ẩn) — KHÔNG phải Inverse (đảo cực)?** Yes / No
> **Cụm 4 nến, hai nến thân lớn, bóng chồng lấp?** Yes / No
> **Implied zone (2 trung điểm bóng):** [low] → [high]
> **CE (50%) của implied:**
> **Sinh từ displacement phá cấu trúc?** Yes / No
> **Location:** Premium / Discount / Equilibrium
> **Có FVG 3-nến rõ hơn để ưu tiên?** Yes / No
> **Liquidity sweep trước cụm nến?** Yes / No — pool: ____
> **Entry plan (quanh CE):**
> **Stop logic (ngoài biên xa vùng implied):**
> **Target / draw on liquidity:**
> **Kill zone permitted:** London / NY AM / NY PM
> **No-trade condition:** mô hình ép / nhầm Inverse / ngược bias
