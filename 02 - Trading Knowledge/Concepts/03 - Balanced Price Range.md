---
type: ict-concept
concept: "Balanced Price Range"
aliases:
  - Balanced Price Range
  - BPR
  - Balance Price Range
tags:
  - trading/ict/concept
  - trading/study
  - "#BPR"
status: developing
category: PD Array
timeframes:
  - D1
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
  - "[[Mistake - Fake BPR No Overlap]]"
  - "[[Mistake - Trade BPR Against Bias]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
---

# Balanced Price Range

> [!summary] Tóm tắt 1 câu
> **Balanced Price Range (BPR) là vùng CHỒNG nhau giữa một bullish FVG và một bearish FVG ở cùng khoảng giá — hình thành khi giá đi một chiều để lại FVG, rồi đảo lại ngay để lại FVG ngược — tạo nên một vùng "đã cân bằng hai phía", trở thành POI rất mạnh mà giá thường phản ứng sắc bén khi quay lại.**

> [!important] Nguyên tắc cốt lõi
> **BPR chỉ tồn tại khi hai FVG NGƯỢC CHIỀU thực sự CHỒNG LẤP (overlap) cùng một dải giá. Phần overlap đó mới là BPR — không phải toàn bộ hai FVG. Vì vùng này đã được giao dịch cả hai chiều (xuống rồi lên), nó là vùng cân bằng/hiệu quả; khi giá quay lại, nó hoạt động như support/resistance mạnh hơn một FVG đơn lẻ.**
> Nếu hai FVG không chồng nhau → KHÔNG có BPR.

---

## 1. Định nghĩa

**Khái niệm:**  
Balanced Price Range (BPR) là vùng giao nhau (overlap) của **hai Fair Value Gap ngược chiều** nằm trên cùng một dải giá. Trình tự hình thành điển hình:

1. Giá **delivery xuống** mạnh (displacement giảm) để lại một **bearish FVG (SIBI — Sellside Imbalance Buyside Inefficiency)**.
2. Giá tạo đáy phản ứng rồi **đảo chiều lên** mạnh (displacement tăng) để lại một **bullish FVG (BISI — Buyside Imbalance Sellside Inefficiency)** chồng lên vùng SIBI vừa tạo.
3. **Phần hai FVG đè lên nhau** chính là **Balanced Price Range**.

**Vì sao gọi là "balanced":** một FVG đơn lẻ là vùng **imbalance** (mất cân bằng, chỉ giao dịch một chiều). Khi giá đi xuống để lại SIBI rồi quay lên để lại BISI ngay trên đó, vùng overlap đã được giao dịch **cả hai chiều** → mất cân bằng được "cân bằng lại" (balanced). Vùng này trở thành một mức tham chiếu giá rất nhạy: giá quay lại thường reject sắc bén vì cả hai phía đều đã để lại dấu vết order flow.

**Bullish BPR vs Bearish BPR:**
- **Bullish BPR:** dùng làm **support** / vùng tìm Long. Hình thành khi sau overlap, hướng tiếp theo là lên; giá retrace về BPR rồi bật lên.
- **Bearish BPR:** dùng làm **resistance** / vùng tìm Short. Hình thành khi sau overlap, hướng tiếp theo là xuống; giá retrace lên BPR rồi đẩy xuống.

> Lưu ý: cùng một vùng overlap có thể đóng vai bullish hay bearish tùy **context bias + hướng giá tiếp cận**. BPR không tự quyết định hướng — narrative HTF quyết định.

**CE của BPR:** giống FVG, mức **50% (Consequent Encroachment)** của vùng overlap là điểm phản ứng quan trọng nhất; entry tinh chỉnh thường quanh CE của BPR. Xem [[10 - Consequent Encroachment (Mean Threshold)]].

**Mục đích trong ICT:**  
- Là **POI cao cấp** để vào lệnh — mạnh hơn một FVG đơn vì có "confluence kép" hai chiều.
- Là **support/resistance** đáng tin khi giá quay lại.
- Là vùng đặt **stop loss logic**: stop nằm ngoài đầu kia của BPR.
- Là một dạng đặc biệt liên quan tới [[17 - Inverse Fair Value Gap - iFVG]]: BPR là nơi một FVG đã bị "đảo" và phối với FVG mới.

**Vì sao khái niệm này quan trọng:**  
BPR lọc bớt nhiễu của FVG. Thay vì trade mọi FVG, BPR cho bạn một vùng nơi **hai imbalance ngược chiều hội tụ** — xác suất phản ứng cao hơn. Nó đặc biệt hữu ích để xác định điểm đảo chiều chất lượng sau một liquidity sweep.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Vùng nào có "confluence kép" của order flow hai chiều?
- Giá quay lại đâu thì có khả năng reject mạnh nhất?
- POI nào mạnh hơn để chờ entry, thay vì FVG đơn lẻ giữa range?
- CE của BPR ở đâu để tinh chỉnh entry và đo respect/invalidation?

### Balanced Price Range không phải là gì
- Không phải một FVG đơn lẻ — phải có HAI FVG ngược chiều CHỒNG nhau.
- Không phải hai FVG nằm cách xa nhau (không overlap = không BPR).
- Không phải tín hiệu độc lập — vẫn cần bias + premium/discount + liquidity context.
- Không phải bất biến — khi giá đóng nến xuyên thủng toàn bộ BPR, nó mất hiệu lực.
- Không tự quyết định hướng — hướng do narrative HTF, không do hình dạng vùng.

---

## 2. Bối cảnh sử dụng

### So sánh BPR với FVG đơn lẻ

| Tiêu chí | FVG đơn lẻ | Balanced Price Range (BPR) |
|---|---|---|
| Cấu tạo | 1 imbalance (1 chiều) | 2 FVG ngược chiều CHỒNG nhau |
| Order flow | Một phía để lại dấu | Cả hai phía để lại dấu (đã "balanced") |
| Độ mạnh POI | Trung bình | Cao hơn (confluence kép) |
| Vùng tham chiếu | Toàn bộ gap | Chỉ phần overlap |
| Vai trò | POI / draw | POI cao cấp / S-R mạnh |
| Rủi ro nhiễu | Cao (FVG khắp nơi) | Thấp hơn (điều kiện overlap lọc bớt) |

> [!tip]
> Cách nhanh để thấy BPR: khi giá quét một đáy/đỉnh (sweep) rồi V-reversal mạnh, hãy tìm xem **FVG của leg đi và FVG của leg về** có đè lên nhau không. Phần đè lên = BPR — đó thường là điểm retest đẹp nhất.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có **liquidity sweep** rõ trước khi giá đảo chiều tạo overlap.
- [ ] BPR nằm tại / trùng một **POI HTF** đồng hướng bias.
- [ ] BPR nằm đúng **premium** (cho Short) / **discount** (cho Long) của dealing range.
- [ ] Overlap rõ ràng, có thể đo được CE của vùng.
- [ ] Có liquidity target rõ phía bên kia sau khi reject từ BPR.
- [ ] BPR còn **unmitigated** (chưa bị giá quay lại lấp/xuyên).

### Khi nào nên bỏ qua?
- [ ] Hai FVG **không chồng nhau** → không phải BPR.
- [ ] BPR nằm giữa range / quanh equilibrium, không có context.
- [ ] BPR ngược Daily Bias mà không có playbook riêng.
- [ ] BPR đã bị giá đóng nến xuyên thủng toàn bộ (đã invalid).
- [ ] Overlap quá mỏng / mơ hồ, không xác định được CE.
- [ ] Chưa có liquidity sweep — entry dễ thành mồi.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Một bearish FVG (SIBI)** từ leg giảm trước đó.
2. **Một bullish FVG (BISI)** từ leg tăng đảo chiều ngay sau (hoặc ngược lại cho bearish BPR).
3. **Vùng OVERLAP** giữa hai FVG — đây là BPR thật.
4. **CE (50%)** của vùng overlap — mức phản ứng quan trọng nhất.
5. **Context:** lý tưởng là overlap hình thành ngay sau một liquidity sweep + reversal mạnh.

### Ma trận nhận diện BPR

| Thành phần | Bullish BPR | Bearish BPR | Cảnh báo / BPR yếu |
|---|---|---|---|
| FVG thứ nhất | Bearish FVG (SIBI) từ leg xuống | Bullish FVG (BISI) từ leg lên | Chỉ có 1 FVG (không phải BPR) |
| FVG thứ hai | Bullish FVG (BISI) từ leg đảo lên | Bearish FVG (SIBI) từ leg đảo xuống | FVG thứ hai không chồng FVG đầu |
| Vùng dùng | Phần OVERLAP của 2 FVG | Phần OVERLAP của 2 FVG | Dùng nhầm toàn bộ FVG thay vì overlap |
| Vai trò | Support — tìm Long khi giá về | Resistance — tìm Short khi giá về | Ở giữa range / sai premium-discount |
| Context | Sau sweep SSL, discount, bias bullish | Sau sweep BSL, premium, bias bearish | Chưa sweep; ngược bias |
| Trạng thái | Unmitigated, CE chưa bị xuyên | Unmitigated, CE chưa bị xuyên | Đã bị đóng nến xuyên toàn bộ |

### Điều kiện bắt buộc
- [ ] Xác định được CẢ hai FVG ngược chiều.
- [ ] Hai FVG thực sự CHỒNG LẤP cùng dải giá (xác định vùng overlap).
- [ ] Đo được CE (50%) của vùng overlap.
- [ ] Biết BPR đang ở premium hay discount của dealing range phù hợp.
- [ ] Xác định trạng thái: unmitigated / đã test / đã xuyên.

### Điều kiện tăng xác suất
- [ ] BPR hình thành ngay sau một **liquidity sweep** đúng hướng narrative.
- [ ] BPR nằm bên trong / trùng một POI HTF lớn hơn (HTF FVG, OB).
- [ ] BPR đúng phía premium/discount cho hướng trade.
- [ ] CE của BPR trùng OB / equilibrium / OTE → confluence.
- [ ] Có liquidity rõ ràng làm target sau khi reject từ BPR.
- [ ] BPR nằm trong kill zone phù hợp plan session.

### Điều kiện làm setup yếu đi
- Overlap quá mỏng hoặc mơ hồ.
- BPR nằm giữa range / sai premium-discount.
- BPR đã bị test nhiều lần, ăn mòn dần.
- Không có sweep trước đó.
- Nhiều vùng overlap chồng chéo gần nhau khiến không rõ mức tham chiếu.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng BPR
> 1. **Có thật sự hai FVG NGƯỢC CHIỀU chồng nhau không, hay tôi đang nhìn một FVG đơn?**
> 2. **Vùng overlap (BPR) nằm ở POI HTF nào và đúng premium/discount không?**
> 3. **Liquidity đã bị sweep trước khi overlap hình thành chưa?**
> 4. **CE của BPR ở đâu, và điều gì làm BPR này invalid?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **HTF POI & draw:** có HTF FVG/OB nào mà giá đang bị hút về không? BPR có trùng nó không?
- **Premium/Discount:** BPR cho Long phải ở discount; BPR cho Short phải ở premium của HTF dealing range.

### H1 / M15 — POI & Context
- **Xác định BPR cụ thể:** ghi rõ vùng overlap và CE, ví dụ `H1 bullish BPR 1.0820–1.0832, CE = 1.0826`.
- **Lý do hợp lệ:** hai FVG có thật sự chồng không? Có sau sweep không? Đúng premium/discount không? Còn unmitigated không?
- **Liquidity:** giá đã sweep pool đối diện chưa?

### M5 / M1 — Confirmation & Entry
- **MSS:** sau khi giá vào BPR, có MSS xác nhận đảo hướng nội bộ không?
- **Displacement LTF:** thường tạo một FVG nhỏ refined để entry.
- **Entry:** ưu tiên quanh **CE của BPR** thay vì mép xa.
- **Stop logic:** ngoài đầu kia của BPR / ngoài điểm sweep.

```text
Mẫu ghi nhanh — Bullish BPR Entry
HTF Bias: Bullish | Location: Discount
Draw on liquidity: BSL tại [level]
POI: H1 bullish BPR [low]–[high] (overlap SIBI+BISI), CE = [mid]
Sweep: đã quét SSL dưới [level] trước khi giá đảo lên tạo overlap
Entry plan: chờ giá retrace về CE của BPR → M5 bullish MSS + FVG → entry quanh CE
Stop: dưới đáy của BPR / dưới sweep low
Target: internal liquidity trước, BSL chính sau
Invalid: đóng nến xuyên thủng dưới toàn bộ BPR → bỏ
```

```text
Mẫu ghi nhanh — Bearish BPR Entry
HTF Bias: Bearish | Location: Premium
Draw on liquidity: SSL tại [level]
POI: H1 bearish BPR [low]–[high] (overlap BISI+SIBI), CE = [mid]
Sweep: đã quét BSL trên [level] trước khi giá đảo xuống tạo overlap
Entry plan: chờ giá retrace lên CE của BPR → M5 bearish MSS + FVG → entry quanh CE
Stop: trên đỉnh của BPR / trên sweep high
Target: internal liquidity trước, SSL chính sau
Invalid: đóng nến xuyên thủng trên toàn bộ BPR → bỏ
```

> [!warning]
> **BPR trên LTF không tạo bias.** Một bullish BPR đẹp ngược Daily Bearish Bias không cho phép Long, trừ khi HTF narrative đã thực sự đảo. BPR là refinement của entry, không phải lý do đổi hướng.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Có hai FVG ngược chiều thực sự chồng lấp (vùng overlap rõ).
- [ ] BPR nằm tại POI HTF đồng hướng Daily Bias.
- [ ] BPR đúng phía premium (Short) / discount (Long).
- [ ] Liquidity đã bị sweep trước khi overlap hình thành.
- [ ] Giá chạm CE / vùng BPR và **respect** (reject với phản ứng).
- [ ] LTF có MSS + displacement xác nhận khi giá vào BPR.
- [ ] Có target liquidity rõ và R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Hai FVG **không chồng nhau** → không phải BPR ngay từ đầu.
- [ ] Giá **đóng nến xuyên qua toàn bộ BPR** và giữ giá ngoài vùng → invalid.
- [ ] Không có liquidity sweep trước khi giá vào BPR.
- [ ] BPR ở sai phía premium/discount cho hướng trade.
- [ ] BPR ngược Daily Bias mà không có bằng chứng HTF đảo.
- [ ] BPR đã bị test/ăn mòn nhiều lần.
- [ ] LTF không tạo MSS/displacement khi giá vào BPR — chỉ "rơi xuyên".

### Respect vs Invalidation của BPR

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Giá chạm CE / mép gần BPR rồi reject với displacement ngược | **Respect** | BPR đang giữ; entry hợp lệ quanh CE |
| Giá lấp một phần BPR (chưa qua CE) rồi reject | **Partial respect** | Vẫn còn hiệu lực; phản ứng ở mép vùng |
| Giá lấp hết BPR rồi mới reject | **Full fill** | Cân nhắc; cần thêm confirmation |
| Giá ĐÓNG NẾN xuyên thủng toàn bộ BPR | **Invalidation** | BPR hết hiệu lực; chuyển sang tìm POI/IFVG khác |

> [!note]
> Vì BPR đã có order flow hai chiều, một BPR bị xuyên thủng thường là tín hiệu order flow đã đổi mạnh — đừng cố giữ lệnh ngược. Khi đó hãy đọc lại theo [[17 - Inverse Fair Value Gap - iFVG]] và [[21 - Market Structure Shift]].

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Balanced-Price-Range-Example-Correct.svg]]

**Mô tả:**  
Giá delivery xuống để lại một bearish FVG (SIBI), tạo đáy phản ứng rồi displacement lên mạnh để lại một bullish FVG (BISI) chồng lên SIBI. Phần overlap = Balanced Price Range. Khi giá retrace về BPR (quanh CE), nó reject sắc bén và đi tiếp lên. Entry quanh CE của BPR; stop dưới đáy BPR; target là BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- Có ĐÚNG hai FVG ngược chiều chồng nhau → BPR thật.
- Entry dùng **phần overlap**, không dùng nhầm toàn bộ một FVG.
- Giá **respect** vùng (reject quanh CE), không xuyên thủng.
- Có hướng đi và liquidity target rõ ràng sau khi reject.

### Ví dụ sai / dễ nhầm
![[Balanced-Price-Range-Example-Wrong.svg]]

**Mô tả lỗi:**  
Trader thấy một bearish FVG ở trên và một bullish FVG ở dưới, gọi đó là "BPR" và vào lệnh — nhưng hai FVG nằm cách xa nhau, **không hề chồng lấp**. Vì không có overlap, không có vùng "balanced"; đó chỉ là hai imbalance riêng biệt. Giá đi xuyên thẳng qua vùng vô nghĩa này mà không phản ứng, lệnh bị stop.

**Bài học:**
- BPR = phần **OVERLAP** của hai FVG ngược chiều; không overlap thì không có BPR.
- Đừng gọi một FVG đơn lẻ (hay hai FVG rời rạc) là "BPR".
- Luôn kiểm tra vùng giao nhau thật trước khi coi đó là POI cao cấp.
- Không có overlap + không có sweep = không có edge.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[Fair Value Gap]]
- [[17 - Inverse Fair Value Gap - iFVG]]
- [[10 - Consequent Encroachment (Mean Threshold)]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[Order Block]]
- [[Optimal Trade Entry]]
- [[27 - Premium Discount]]
- [[19 - Liquidity]]
- [[12 - Daily Bias]]

### Sequence mẫu — Long với Bullish BPR
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Giá về Discount + bullish HTF POI
→ Sweep Sell-Side Liquidity → V-reversal
→ Leg xuống để lại SIBI; leg đảo lên để lại BISI → OVERLAP = Bullish BPR
→ Giá retrace về CE của BPR
→ M5/M1 bullish MSS + FVG nhỏ refined
→ Entry quanh CE; Stop dưới đáy BPR / dưới sweep low
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short với Bearish BPR
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Giá về Premium + bearish HTF POI
→ Sweep Buy-Side Liquidity → reversal xuống
→ Leg lên để lại BISI; leg đảo xuống để lại SIBI → OVERLAP = Bearish BPR
→ Giá retrace lên CE của BPR
→ M5/M1 bearish MSS + FVG nhỏ refined
→ Entry quanh CE; Stop trên đỉnh BPR / trên sweep high
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> BPR đặc biệt mạnh khi nó hình thành ngay tại điểm đảo chiều sau một sweep — đó là lúc order flow hai chiều "kẹp" lại một vùng giá, tạo ra một POI chất lượng cao hơn FVG đơn lẻ.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy "hai FVG ngược nhau"
> BPR chỉ tồn tại khi hai FVG thật sự CHỒNG LẤP, và chỉ có edge khi đặt trong context bias + premium/discount + liquidity.

### A. Context (HTF)
- [ ] Daily Bias đã rõ.
- [ ] BPR đồng hướng bias.
- [ ] BPR đúng premium (Short) / discount (Long).
- [ ] BPR trùng / nằm tại một POI HTF có ý nghĩa.
- [ ] Có draw on liquidity rõ làm target.
- [ ] Xác định CE của BPR và level invalidation.

### B. Execution (LTF)
- [ ] Hai FVG ngược chiều thực sự chồng nhau (overlap rõ).
- [ ] Đã có liquidity sweep TRƯỚC khi overlap hình thành.
- [ ] Giá respect CE / mép BPR (reject), không đóng nến xuyên qua.
- [ ] Có LTF MSS + displacement xác nhận.
- [ ] Entry quanh CE của BPR, không chase ở mép xa.
- [ ] Stop ngoài đầu kia BPR / ngoài điểm sweep.
- [ ] Target liquidity rõ; R:R đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Hai FVG không chồng nhau → không phải BPR → không trade.
- [ ] BPR ngược bias / sai premium-discount → không trade.
- [ ] Chưa có liquidity sweep → không trade.
- [ ] BPR đã bị đóng nến xuyên qua → không trade.
- [ ] BPR giữa range / không POI HTF → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Không có overlap thật | Gọi hai FVG rời rạc là "BPR" | Vùng vô nghĩa, giá đi xuyên | Chỉ tính BPR khi hai FVG CHỒNG nhau |
| Dùng nhầm toàn bộ FVG | Entry ở mép FVG thay vì vùng overlap | Sai mức tham chiếu, R:R xấu | Chỉ dùng phần overlap + CE của nó |
| Nhầm FVG đơn với BPR | Thấy 1 FVG mạnh là gọi BPR | Mất lợi thế confluence kép | Yêu cầu đủ 2 FVG ngược chiều |
| Bỏ qua premium/discount | Long BPR premium, Short BPR discount | Entry thành chase | Long chỉ ở BPR discount, Short ở premium |
| Vào trước liquidity sweep | Chưa quét đỉnh/đáy đã entry tại BPR | Stop nằm đúng nơi market còn muốn quét | Chờ sweep → reversal → overlap |
| Bỏ qua CE | Entry ở mép xa, không dùng 50% | Bỏ lỡ mức phản ứng quan trọng nhất | Ưu tiên entry quanh CE của BPR |
| Giữ lệnh khi BPR xuyên thủng | Coi full fill là tạm thời rồi cố giữ | Order flow đã đổi mạnh | Đóng nến xuyên qua = invalid, thoát |
| Trade BPR ngược bias | BPR đẹp nhưng HTF ngược | Target ngược hướng thiếu room | Chỉ trade BPR đồng hướng Daily Bias |

---

## 10. Câu hỏi tự kiểm tra

- Mình có giải thích BPR (overlap của SIBI + BISI) trong 30 giây không?
- Đây có thật sự là overlap của hai FVG ngược chiều, hay chỉ một FVG đơn?
- CE của vùng overlap nằm ở đâu? Giá đang respect hay xuyên qua?
- BPR đang ở premium hay discount của dealing range nào?
- Liquidity đã bị sweep trước khi overlap hình thành chưa?
- BPR có đồng hướng Daily Bias không?
- Điều gì làm BPR này invalid?
- Nếu không trade BPR này, lý do "No Trade" là gì?
- Setup nào trong journal đã dùng BPR đúng/sai context?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Balanced Price Range (BPR) là gì?  
**Đáp:** Vùng CHỒNG nhau (overlap) giữa một bullish FVG (BISI) và một bearish FVG (SIBI) ở cùng dải giá; phần overlap đã được giao dịch cả hai chiều nên "balanced".

### Q2
**Hỏi:** BPR khác FVG đơn lẻ ở điểm cốt lõi nào?  
**Đáp:** FVG đơn là imbalance một chiều; BPR là hai FVG ngược chiều chồng nhau → có order flow cả hai phía → POI mạnh hơn (confluence kép). Chỉ dùng phần overlap.

### Q3
**Hỏi:** BPR hình thành theo trình tự nào?  
**Đáp:** Giá đi một chiều để lại FVG, tạo đáy/đỉnh phản ứng rồi đảo chiều mạnh để lại FVG ngược chồng lên FVG cũ; phần đè nhau = BPR. Lý tưởng là sau một liquidity sweep.

### Q4
**Hỏi:** Vùng nào của BPR dùng làm entry và tại sao?  
**Đáp:** Phần OVERLAP (không phải toàn bộ FVG), ưu tiên quanh CE (50%) của overlap — đó là mức phản ứng quan trọng nhất và cho R:R tốt hơn.

### Q5
**Hỏi:** Khi nào BPR bị invalid?  
**Đáp:** Khi giá đóng nến xuyên thủng toàn bộ vùng overlap và giữ giá ngoài đó; thường báo order flow đã đổi mạnh — không giữ lệnh ngược.

### Q6
**Hỏi:** BPR có tự quyết định hướng trade không?  
**Đáp:** Không. Hướng do narrative HTF + premium/discount + liquidity quyết định. BPR chỉ là refinement của entry, không phải lý do đổi bias.

---

## 12. Lesson Learned

### Bài học chính
- BPR = **overlap** của hai FVG ngược chiều; chỉ phần đè nhau mới là BPR.
- Vùng này "balanced" vì đã có order flow **hai chiều** → POI mạnh hơn FVG đơn.
- Luôn dùng **CE của overlap** để tinh chỉnh entry và đo respect/invalidation.
- BPR mạnh nhất khi hình thành ngay sau một **liquidity sweep + reversal**.
- BPR không quyết định hướng — narrative HTF + premium/discount mới quyết định.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ gọi một vùng là BPR khi có ĐỦ hai FVG ngược chiều CHỒNG nhau.
- [ ] Tôi chỉ dùng phần overlap (và CE của nó) làm POI, không dùng toàn bộ FVG.
- [ ] Tôi chỉ Long BPR ở discount và Short BPR ở premium, đồng hướng bias.
- [ ] Tôi luôn chờ liquidity sweep TRƯỚC khi vào lệnh tại BPR.
- [ ] Khi BPR bị đóng nến xuyên thủng, tôi coi nó invalid và không giữ lệnh ngược.

### Câu nhắc nhở khi trade
> **"BPR là nơi hai dòng order flow gặp nhau — nhưng chỉ khi chúng thật sự CHỒNG. Không overlap, không sweep, sai phía = không phải BPR đáng trade."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt BPR (overlap) với FVG đơn không? |
| Nhận diện trên chart |  | Có xác định đúng vùng overlap và CE không? |
| Biết khi nào bỏ qua |  | Có dám bỏ "BPR" không có overlap / ngược bias không? |
| Kết hợp với context HTF |  | BPR có được đặt trong bias + premium/discount + sweep không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự quanh CE của overlap sau sweep không? |
| Review sau trade |  | Có so sánh BPR vs FVG đơn bằng dữ liệu journal không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập 20–30 setup gắn tag `[[Balanced Price Range]]`.
- [ ] Review riêng: BPR có overlap thật vs FVG đơn; BPR sau sweep vs trước sweep; entry tại CE vs mép.
- [ ] Thống kê win rate, average R theo `bpr_overlap_confirmed` và `sweep_before_bpr`.
- [ ] Chỉ cập nhật rule khi đủ mẫu backtest/forward test.

---

## Appendix — BPR Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**  
> **Daily Bias:** Bullish / Bearish / Neutral  
> **BPR type:** Bullish / Bearish  
> **BPR timeframe & overlap range:** ____ , [low]–[high]  
> **CE (50% của overlap):**  
> **Hai FVG ngược chiều có CHỒNG nhau?** Yes / No  
> **Location:** Premium / Discount / Equilibrium  
> **Trùng POI HTF nào:**  
> **Liquidity sweep trước BPR?** Yes / No — pool: ____  
> **Draw on liquidity / target:**  
> **Entry plan (quanh CE):**  
> **Stop logic:**  
> **Invalidation (đóng nến xuyên toàn bộ BPR tại):**  
> **Kill zone permitted:** London / NY AM / NY PM  
> **No-trade condition:**  
