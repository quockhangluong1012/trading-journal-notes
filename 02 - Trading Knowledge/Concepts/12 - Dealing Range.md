---
type: ict-concept
concept: Dealing Range
aliases:
  - Dealing Range
  - Trading Range
tags:
  - trading/ict/concept
  - trading/study
  - "#DealingRange"
status: developing
category: Market Structure
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-07-17
created: 2026-06-22
updated: 2026-07-18
common_mistakes:
  - "[[Mistake - Wrong Dealing Range]]"
  - "[[Mistake - Premium Discount Off Wrong Range]]"
  - "[[Mistake - Buying Premium Selling Discount]]"
---

# Dealing Range

> [!summary] Tóm tắt 1 câu
> **Dealing Range là khoảng giá giữa một swing high và một swing low CÓ Ý NGHĨA mà giá đang vận động bên trong, được xác định bởi hai điểm đã lấy liquidity ở hai đầu; nó là khung tham chiếu để đo Premium/Discount, phân loại internal vs external liquidity và dự phóng draw on liquidity.**

> [!important] Nguyên tắc cốt lõi
> **Mọi phép đo Premium/Discount, mọi vùng OTE và mọi kết luận về draw on liquidity chỉ có nghĩa khi được đo trên một Dealing Range được chọn ĐÚNG.**  
> Chọn sai range — quá nhỏ, quá cũ, hay không lấy liquidity ở hai đầu — thì Premium/Discount lệch, dẫn tới mua premium / bán discount mà tưởng mình đang trade đúng vùng.

---

## 1. Định nghĩa

![[Dealing-Range-Sec-01-Dinh-Nghia.svg|720]]
*Sơ đồ: Dealing Range xác định bởi cặp swing high – swing low gần nhất; mức 50% chia premium / discount.*

**Khái niệm:**  
Dealing Range trong ICT là **khoảng giá giữa một swing high và một swing low có ý nghĩa** mà giá đang dao động bên trong tại thời điểm phân tích. Hai đầu range không phải là hai điểm bất kỳ: chúng là hai điểm mà **liquidity đã được lấy** (một đỉnh rõ ràng đã quét buy-side liquidity và một đáy rõ ràng đã quét sell-side liquidity), hoặc tối thiểu là một đỉnh rõ tới một đáy rõ tạo bởi displacement/BOS. Dealing Range là **khung tham chiếu** (reference frame) để chia premium/discount, để biết đâu là liquidity bên trong, đâu là liquidity bên ngoài, và để đoán giá đang bị hút về phía nào.

**Mục đích trong ICT:**  
- Suy ra **Premium / Discount / Equilibrium** — chia range bằng Fibonacci, 50% là equilibrium; trên 50% là premium (vùng để tìm Short), dưới 50% là discount (vùng để tìm Long). Xem [[27 - Premium Discount]].
- Phân loại **Internal range liquidity** (FVG, Order Block, imbalance nằm BÊN TRONG range) và **External range liquidity** (chính đỉnh/đáy của range = BSL/SSL nằm ở hai đầu).
- **Dự phóng draw on liquidity:** giá thường luân chuyển từ internal → external, hoặc quét external rồi đảo về internal đối diện.
- Cung cấp khung đo lường thống nhất để xây [[12 - Daily Bias]] và canh [[Optimal Trade Entry]].

**Vì sao khái niệm này quan trọng:**  
Premium/Discount, OTE, equilibrium — tất cả đều là **tỷ lệ phần trăm đo trên một range**. Nếu range sai, mọi con số phái sinh đều sai. Dealing Range đúng là **điều kiện tiên quyết** để mọi phép đo premium/discount và OTE có nghĩa. Đây cũng là nền để xây Daily Bias: bias dùng vị trí giá trong range cộng với draw on liquidity để kết luận hướng ưu tiên.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá hiện đang ở **premium hay discount**? (đo trên range nào?)
- Đâu là **external liquidity** (BSL/SSL ở hai đầu) còn mở để làm draw on liquidity?
- Đâu là **internal liquidity** (FVG/OB) mà giá có thể về để rebalance trước khi đi tiếp?
- Range hiện tại còn hiệu lực không, hay external đã bị lấy và cần vẽ range mới?
- Tôi nên tìm Long ở discount hay tìm Short ở premium của range này?

### Dealing Range không phải là gì
- Không phải mọi cặp swing high/low gần giá; phải là swing **có ý nghĩa** đã lấy liquidity.
- Không phải khung cố định vĩnh viễn; khi external bị lấy thì range cũ hết hiệu lực.
- Không phải thứ chọn theo cảm tính "nhìn cho đẹp"; phải bám displacement/BOS và narrative timeframe.
- Không phải lý do để đo Premium/Discount từ một range của timeframe khác với narrative đang phân tích.
- Không phải bản thân nó là tín hiệu vào lệnh; nó là khung tham chiếu, entry vẫn cần sweep + MSS + displacement.

---

## 2. Bối cảnh sử dụng

![[Dealing-Range-Sec-02-Boi-Canh.svg|720]]
*Sơ đồ: Bối cảnh dùng Dealing Range — định vị vùng premium/discount để canh entry đồng hướng bias.*

### Các trạng thái / phân loại liquidity trong một Dealing Range

| Thành phần | Vị trí trong range | Ý nghĩa thực chiến |
|---|---|---|
| **External liquidity (đầu trên)** | Chính swing high = **BSL** | Buy-side liquidity còn mở; là draw on liquidity tiềm năng phía trên |
| **External liquidity (đầu dưới)** | Chính swing low = **SSL** | Sell-side liquidity còn mở; là draw on liquidity tiềm năng phía dưới |
| **Internal liquidity** | FVG / OB / imbalance trong range | Vùng giá thường về để rebalance/mitigate trước khi tìm external đối diện |
| **Equilibrium (50%)** | Giữa range | Vùng trung tính; mua/bán quanh đây thường R:R kém, dễ chop |
| **Premium (trên 50%)** | Nửa trên | Vùng ưu tiên tìm **Short** / không Long mới |
| **Discount (dưới 50%)** | Nửa dưới | Vùng ưu tiên tìm **Long** / không Short mới |

> [!tip]
> **Một Dealing Range chuẩn có liquidity ở CẢ HAI đầu đã được thị trường tôn trọng.** Đỉnh là nơi buy stops nằm (BSL), đáy là nơi sell stops nằm (SSL). Đây là lý do hai đầu range trở thành draw on liquidity tự nhiên, và là lý do giá hay quét chúng.

### Khi nào khái niệm này có giá trị cao?
- [ ] Hai đầu range là swing **rõ ràng**, tạo bởi displacement/BOS và đã quét liquidity.
- [ ] Range phù hợp với **timeframe và narrative** mình đang phân tích (D1 range cho D1 bias, H1 range cho H1 context...).
- [ ] Giá đang ở **premium hoặc discount rõ ràng**, không lửng lơ quanh equilibrium.
- [ ] Có internal liquidity (FVG/OB) hợp lệ bên trong range để làm POI.
- [ ] External liquidity ở phía draw on liquidity vẫn **còn mở** (chưa bị lấy).
- [ ] Có thể viết được luồng kỳ vọng: internal → external, hoặc sweep external → đảo về internal đối diện.

### Khi nào nên bỏ qua?
- [ ] Range mơ hồ: hai đầu là swing nhỏ/cũ, không lấy liquidity, không có displacement.
- [ ] Giá đang ở giữa range (quanh equilibrium), không rõ premium/discount.
- [ ] External liquidity của range đã bị lấy xong → range cũ hết hiệu lực, chưa vẽ lại range mới.
- [ ] Đang đo Premium/Discount trên range của timeframe không khớp với narrative.
- [ ] Hai đầu range cho draw on liquidity hai phía gần như tương đương → bias không rõ.
- [ ] Không có internal POI hợp lệ để chờ reaction.

---

## 3. Cấu trúc nhận diện trên chart

![[Dealing-Range-Sec-03-Nhan-Dien.svg|720]]
*Sơ đồ: Cách chọn đúng cặp swing high/low để vẽ một Dealing Range hợp lệ trên chart.*

### Dấu hiệu chính
1. **Một swing high có ý nghĩa:** đỉnh được tạo bởi displacement/BOS, và lý tưởng là đã quét BSL phía trên (đỉnh cũ / equal highs / PDH...).
2. **Một swing low có ý nghĩa:** đáy được tạo bởi displacement/BOS, và lý tưởng là đã quét SSL phía dưới.
3. **Giá đang vận động BÊN TRONG hai điểm này:** chưa lấy external ở đầu còn lại, hoặc vừa lấy một đầu và đang quay về nửa kia.
4. **Internal structure rõ:** có FVG/OB/imbalance bên trong làm internal liquidity / POI.
5. **Tính hợp lệ theo timeframe:** range được vẽ trên đúng khung mà narrative cần (đừng dùng range M5 để kết luận bias D1).

### Ma trận nhận diện Dealing Range

| Thành phần | Range hợp lệ (Bullish context) | Range hợp lệ (Bearish context) | Cảnh báo / chọn sai |
|---|---|---|---|
| **Đầu trên (high)** | Swing high rõ đã quét BSL; là external target phía trên còn mở | Swing high rõ, vừa bị sweep BSL rồi reject → bắt đầu bearish leg | Đỉnh nhỏ/cũ, không quét liquidity, không displacement |
| **Đầu dưới (low)** | Swing low rõ vừa bị sweep SSL rồi reclaim → bắt đầu bullish leg | Swing low rõ là external target phía dưới còn mở | Đáy nhỏ/cũ, không quét liquidity, không displacement |
| **Tạo bởi** | Displacement/BOS rõ ràng | Displacement/BOS rõ ràng | Chỉ là wiggle, micro swing, hoặc swing chọn vì "gần giá" |
| **Location hiện tại** | Giá ở discount, kỳ vọng Long về BSL | Giá ở premium, kỳ vọng Short về SSL | Giá quanh equilibrium, không rõ phía |
| **Internal liquidity** | Bullish FVG/OB trong discount còn unmitigated | Bearish FVG/OB trong premium còn unmitigated | Không có internal POI hoặc đã bị mitigate hết |
| **Tính thời sự** | External phía trên CÒN MỞ | External phía dưới CÒN MỞ | External đã bị lấy → range hết hiệu lực |

### Điều kiện bắt buộc
- [ ] Xác định rõ **swing high và swing low** làm hai đầu range, và ghi giá cụ thể.
- [ ] Hai đầu range tạo bởi **displacement/BOS** và đã (hoặc liên quan tới) liquidity.
- [ ] Range được chọn **phù hợp timeframe + narrative** đang phân tích.
- [ ] Xác định được **external liquidity nào còn mở** (đầu nào là draw on liquidity).
- [ ] Đánh dấu được equilibrium (50%) để biết giá đang premium hay discount.

### Điều kiện tăng xác suất
- [ ] Cả hai đầu range đều đã **quét liquidity** rõ ràng (BSL ở đỉnh, SSL ở đáy).
- [ ] Có **internal POI** hợp lệ (FVG/OB) nằm đúng nửa premium/discount cho hướng trade.
- [ ] Một đầu range vừa bị **sweep rồi reclaim/reject** → tín hiệu giá sẽ tìm external đối diện.
- [ ] Range trùng khớp với range của timeframe cao hơn (HTF range bao trùm và hỗ trợ).
- [ ] Draw on liquidity một phía rõ ràng vượt trội phía còn lại.

### Điều kiện làm setup yếu đi
- Hai đầu range là swing nhỏ hoặc quá cũ, chọn chỉ vì gần giá.
- External của range đã bị lấy mà chưa cập nhật range mới → đang đo trên range "chết".
- Đo Premium/Discount trên range không khớp narrative timeframe.
- Giá lửng lơ quanh equilibrium, không có internal POI rõ.
- Range bị cắt ngang bởi tin tức/expansion lớn làm cấu trúc thay đổi nhưng chưa vẽ lại.

---

## 4. Quy trình phân tích đa khung thời gian

![[Dealing-Range-Sec-04-Da-Khung.svg|720]]
*Sơ đồ: Dealing Range đa khung — HTF làm khung tham chiếu, LTF để tinh chỉnh entry trong quadrant.*

> [!example] Quy trình 4 câu bắt buộc trước khi đo Premium/Discount
> 1. **Range nào là Dealing Range hợp lệ cho timeframe/narrative tôi đang phân tích?**  
> 2. **External liquidity nào (BSL/SSL) còn mở và đang là draw on liquidity?**  
> 3. **Giá đang ở premium hay discount của range đó?**  
> 4. **Range này còn hiệu lực không, hay external đã bị lấy và cần vẽ lại?**

### D1 / H4 — Range gốc & Narrative
- **Xác định D1/H4 dealing range:** đánh dấu swing high và swing low tạo bởi displacement/BOS đáng kể; ghi giá hai đầu.
- **External liquidity:** đầu trên = BSL (ví dụ PDH/PWH/swing high), đầu dưới = SSL (PDL/PWL/swing low). Ghi rõ phía nào còn mở.
- **Equilibrium:** đánh dấu 50% range; xác định giá đang premium hay discount.
- **Internal liquidity:** liệt kê D1/H4 FVG, OB, imbalance còn hiệu lực bên trong range.
- **Draw on liquidity:** kết luận giá đang bị hút về external nào, vì sao phía đó quan trọng hơn.

```text
Mẫu ghi nhanh — Dealing Range cho Bullish context
HTF dealing range: [D1 low @ 1.xxxx] → [D1 high @ 1.xxxx]
Equilibrium (50%): 1.xxxx
External liquidity còn mở: BSL trên D1 high (draw chính)
Internal liquidity: Bullish D1 FVG @ 1.xxxx (discount)
Location: Discount (giá dưới 50%)
Luồng kỳ vọng: giá về internal FVG (discount) → sweep SSL gần đó → bullish reprice → external BSL
Re-draw khi: BSL trên D1 high bị lấy → cập nhật range mới
```

```text
Mẫu ghi nhanh — Dealing Range cho Bearish context
HTF dealing range: [D1 low @ 1.xxxx] → [D1 high @ 1.xxxx]
Equilibrium (50%): 1.xxxx
External liquidity còn mở: SSL dưới D1 low (draw chính)
Internal liquidity: Bearish D1 FVG @ 1.xxxx (premium)
Location: Premium (giá trên 50%)
Luồng kỳ vọng: giá về internal FVG (premium) → sweep BSL gần đó → bearish reprice → external SSL
Re-draw khi: SSL dưới D1 low bị lấy → cập nhật range mới
```

### H1 / M15 — Range con & POI
- **H1/M15 range:** thường là một range con nằm bên trong HTF range; dùng để định vị POI chi tiết.
- **POI = internal liquidity của range:** FVG/OB bên trong, đánh giá còn unmitigated, có displacement, ở đúng nửa premium/discount.
- **Kiểm tra alignment:** range con có hỗ trợ HTF range không? (ví dụ discount của H1 range nằm trong discount của D1 range → cộng hưởng).
- **External của range con:** đỉnh/đáy H1 là BSL/SSL nội bộ — giá hay quét chúng trước khi đi tiếp.

### M5 / M1 — Confirmation & Entry
- **Vi mô hóa range:** sau khi giá vào internal POI của HTF/H1 range, xác định range M5 cục bộ để canh entry.
- **Sweep external nhỏ:** giá thường quét SSL/BSL nội bộ M5 trước MSS.
- **MSS + displacement trong POI:** chỉ tính khi giá đã ở đúng nửa range (discount cho Long, premium cho Short).
- **Entry tại internal liquidity:** FVG/OB hình thành từ displacement, ưu tiên trùng OTE của range.

> [!warning]
> **Range M5 không định nghĩa Premium/Discount của bias.** Một range nhỏ trên M5 chỉ dùng cho execution. Bias và draw on liquidity được đo trên HTF dealing range. Đừng kết luận "giá đang discount" bằng range M5 trong khi trên D1 giá đang premium.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

![[Dealing-Range-Sec-05-Xac-Nhan.svg|720]]
*Sơ đồ: Khi nào Dealing Range còn hiệu lực và khi nào phải re-map sau displacement phá range.*

### Dealing Range được xem là hợp lệ khi
- [ ] Hai đầu range là swing có ý nghĩa, tạo bởi displacement/BOS.
- [ ] Hai đầu (hoặc tối thiểu một đầu) có liên quan tới liquidity đã được lấy (BSL/SSL).
- [ ] Range được vẽ trên timeframe khớp với narrative đang phân tích.
- [ ] External liquidity ở phía draw on liquidity còn mở.
- [ ] Có internal POI hợp lệ nằm đúng nửa premium/discount.
- [ ] Premium/Discount đo trên range này nhất quán với HTF range bao trùm.

### Dealing Range bị vô hiệu (cần vẽ lại) khi
- [ ] **External liquidity (đỉnh hoặc đáy range) đã bị lấy** → một range mới đang hình thành.
- [ ] Displacement mạnh phá hẳn một đầu range và giữ acceptance bên ngoài.
- [ ] Cấu trúc HTF thay đổi (BOS ngược hướng có ý nghĩa) → narrative cũ và range cũ hết giá trị.
- [ ] Range được chọn sai từ đầu (swing nhỏ/cũ) → bỏ, chọn lại range có liquidity ở hai đầu.
- [ ] Đang đo trên range của timeframe không phù hợp → đổi sang range đúng timeframe.

### Phân biệt "sweep external rồi đảo" và "phá range thật"

| Quan sát | Cách đọc hợp lý |
|---|---|
| Giá wick qua đỉnh/đáy range (lấy BSL/SSL) rồi đóng trở lại range, kèm displacement ngược | **Sweep external** — giá có thể quay về tìm internal đối diện; chưa vẽ lại range, dùng làm tín hiệu đảo |
| Giá đóng thân nến mạnh qua đầu range, giữ acceptance ngoài, pullback không reclaim | **Phá range thật** — external đã bị lấy và chuyển delivery; vẽ range mới |
| Giá lấy external một đầu rồi đi thẳng tới external đầu kia | Luồng internal/external bình thường; range cũ hết hiệu lực sau khi đầu thứ hai bị lấy |
| Giá lấy external rồi tạo BOS ngược → swing mới có ý nghĩa | Range mới đang hình thành; cập nhật hai đầu, đo lại premium/discount |

---

## 6. Ví dụ chart

### Ví dụ đúng — Dealing Range hợp lệ, Long ở discount theo draw on liquidity lên BSL
![[Dealing-Range-Example-Correct.png]]

**Mô tả:**  
D1 có một dealing range với đáy vừa quét SSL (sweep sell-side rồi reclaim) và đỉnh là BSL còn mở phía trên. Giá đang ở **discount** (dưới 50% range), chạm bullish D1 FVG (internal liquidity). Trong kill zone, giá quét SSL nội bộ M5, tạo bullish MSS + displacement trong vùng discount, để lại FVG. Entry tại FVG; target là external BSL ở đỉnh range.

**Vì sao đây là ví dụ tốt:**
- Hai đầu range đều có ý nghĩa: đáy đã lấy SSL, đỉnh là BSL còn mở làm draw on liquidity.
- Premium/Discount được đo trên đúng range → giá thực sự ở discount, hợp lý để Long.
- Entry nằm tại internal liquidity (FVG) trong discount; target là external liquidity (BSL) — luồng internal → external rõ ràng.
- Range, location và target cùng phục vụ một narrative thay vì ghép concept rời rạc.

### Ví dụ sai / dễ nhầm — chọn range quá nhỏ → tưởng discount nhưng thực ra premium
![[Dealing-Range-Example-Wrong.png]]

**Mô tả lỗi:**  
Trader chọn một range nhỏ và mới (hai swing nhỏ gần giá) thay vì D1 dealing range thật. Trên range nhỏ này giá nằm ở "discount" nên trader Long. Nhưng trên **D1 dealing range đúng**, giá đang ở **premium** sâu, gần BSL chưa bị lấy ngay phía trên. Giá quét nốt BSP đó rồi đảo xuống, lệnh Long bị stop.

**Bài học:**
- Premium/Discount **chỉ đúng khi đo trên range đúng**; range sai → vị trí sai → mua premium tưởng là discount.
- Đây chính là lỗi đã được cảnh báo trong [[12 - Daily Bias]]: chọn dealing range quá nhỏ/quá cũ làm premium/discount lệch.
- Luôn hỏi: "Range này có liquidity ở hai đầu chưa? Nó có khớp timeframe narrative không?" trước khi tin vào con số premium/discount.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[27 - Premium Discount]]
- [[19 - Liquidity]]
- [[30 - Sell-side Liquidity]]
- [[07 - Buy-side Liquidity]]
- [[Break of Structure]]
- [[Displacement]]
- [[Optimal Trade Entry]]
- [[Fair Value Gap]]
- [[Order Block]]
- [[12 - Daily Bias]]

### Sequence mẫu — Long từ discount của Dealing Range
```text
Xác định Dealing Range hợp lệ (đáy đã sweep SSL, đỉnh BSL còn mở)
→ Đo Premium/Discount; giá ở Discount (dưới 50%)
→ Internal liquidity: Bullish FVG/OB trong discount
→ Giá về internal POI + sweep SSL nội bộ
→ Bullish MSS + Displacement trong discount
→ Entry tại FVG/OB (trùng OTE của range)
→ Stop sau swing / sweep low logic
→ Target: internal liquidity đối diện trước → external BSL (đỉnh range) sau
→ Re-draw range khi BSL bị lấy
```

### Sequence mẫu — Short từ premium của Dealing Range
```text
Xác định Dealing Range hợp lệ (đỉnh đã sweep BSL, đáy SSL còn mở)
→ Đo Premium/Discount; giá ở Premium (trên 50%)
→ Internal liquidity: Bearish FVG/OB trong premium
→ Giá về internal POI + sweep BSL nội bộ
→ Bearish MSS + Displacement trong premium
→ Entry tại FVG/OB (trùng OTE của range)
→ Stop sau swing / sweep high logic
→ Target: internal liquidity đối diện trước → external SSL (đáy range) sau
→ Re-draw range khi SSL bị lấy
```

> [!note]
> Luồng **internal ↔ external** là trục chính: sau khi giá lấy external một đầu, nó thường quay về tìm internal đối diện; sau khi rebalance ở internal, nó hướng tới external đối diện. Dealing Range cho bạn bản đồ của luồng này. OTE và premium/discount chỉ là cách đo vị trí trên bản đồ đó — và chúng vô nghĩa nếu bản đồ (range) sai.

---

## Kiến thức nâng cao (Advanced)

### A1. Quadrant theory — chia range 4 phần, không chỉ 2 nửa

Premium/Discount 50-50 là phép chia thô. Cấp độ tinh hơn là chia range thành **4 quadrant** (0–25–50–75–100%):

![[Dealing-Range-Advanced-Quadrants.svg]]

| Quadrant | Vùng | Cách đọc thực chiến |
|---|---|---|
| **75–100% (Deep Premium)** | Sát range high | Bearish PD Array tại đây có sức mạnh lớn nhất; vùng Short tối ưu; **cấm mở Long mới** |
| **50–75% (Premium nông)** | Trên EQ | Short được nhưng cần confluence mạnh (POI HTF + sweep); phản ứng thường yếu hơn deep premium |
| **25–50% (Discount nông)** | Dưới EQ | Long được nhưng cần confluence mạnh; dễ bị nhúng sâu thêm về deep discount |
| **0–25% (Deep Discount)** | Sát range low | Bullish PD Array mạnh nhất; vùng Long tối ưu — và là nơi **OTE (62–79% retracement)** thường rơi vào |

Hai ứng dụng nâng cao của quadrant:
- **Chọn POI khi có nhiều ứng viên:** nếu trong discount có 2 bullish FVG, ưu tiên cái nằm ở **deep discount**; FVG ở discount nông chỉ dùng khi có sweep + MSS rõ ngay tại đó.
- **Đọc sức khỏe của trend:** trong bullish delivery mạnh, các cú retrace chỉ về tới discount nông (25–50%) rồi chạy tiếp — retrace càng nông trend càng khỏe. Khi giá bắt đầu nhúng tới deep discount thường xuyên, một phần sponsorship đã rút.

**Hành vi quanh Equilibrium:** EQ không phải chỉ là ranh giới — nó là "vùng từ chối quyết định". Consolidation kéo dài quanh EQ nghĩa là thuật toán chưa chọn phía; breakout khỏi consolidation EQ thường chạy thẳng về một external. Rule thực dụng: **giá đóng cửa qua EQ và giữ được phía đó = xác nhận nửa range nào đang kiểm soát**.

### A2. Nested ranges & ma trận alignment đa khung

Dealing Range có tính **fractal**: bên trong D1 range có H4 range, bên trong H4 có H1, M15... Sức mạnh của một setup đến từ **sự cộng hưởng vị trí** giữa các tầng:

| Vị trí trong D1 range | Vị trí trong H1 range | Kết luận |
|---|---|---|
| Discount | Discount | **Cộng hưởng Long** — setup chất lượng cao nhất |
| Discount | Premium | Xung đột: chờ H1 retrace về discount H1 (vẫn trong discount D1) rồi mới tìm Long |
| Premium | Discount | Bẫy phổ biến nhất: "discount" H1 nhưng đang mua ở premium D1 → chỉ scalp hoặc bỏ |
| Premium | Premium | **Cộng hưởng Short** |

Quy tắc vận hành: **HTF range quyết định HƯỚNG được phép, LTF range quyết định THỜI ĐIỂM và GIÁ entry.** Không bao giờ để range LTF "phủ quyết" range HTF; xung đột = giảm size hoặc đứng ngoài.

### A3. Re-mapping range sau displacement

Khi một displacement phá external của range, bản đồ cũ hết hiệu lực **ngay lập tức** — nhưng vẽ range mới thế nào mới là kỹ năng (chi tiết đầy đủ: [[37 - Re-mapping Dealing Range sau Displacement]]). Nguyên tắc lõi:

1. **Range mới lấy gốc từ origin của displacement leg:** swing low nơi displacement khởi phát → extreme mới vừa tạo. Không giữ đầu range cũ đã bị phá làm biên.
2. **Chờ leg hoàn thành mới đo:** đo premium/discount khi displacement còn đang chạy = đo trên range chưa đóng; chờ swing xác nhận (pullback đầu tiên tạo cấu trúc) rồi mới chia EQ.
3. **Sweep ≠ re-map:** wick quét qua external rồi đóng lại trong range (sweep) KHÔNG tạo range mới — range cũ còn nguyên, thậm chí đáng tin hơn vì một đầu vừa được "sạc" liquidity. Chỉ **acceptance** (đóng thân + giữ ngoài) mới buộc re-map.
4. **Cascade re-map:** khi D1 re-map, mọi range H4/H1 bên trong phải được xét lại theo bản đồ mới — không giữ POI cũ đã mất context.

### A4. Range projection — Standard Deviation khi giá rời range

Khi external bị phá thật và giá expansion, dealing range cũ vẫn còn một công dụng cuối: **làm thước đo projection**. Dùng chiều cao range (hoặc manipulation leg) chiếu các mức -1, -2, -2.5, -4 SD theo hướng expansion để ước lượng terminus của leg mới (xem [[31 - Standard Deviation]] và [[08 - Central Bank Dealers Range]] cho phiên bản CBDR). Ứng dụng: khi không còn external liquidity rõ phía trước (giá vào "vùng trống"), SD projection + HTF FVG là hai công cụ duy nhất để định target.

### A5. Chu kỳ ERL ↔ IRL — "nhịp thở" của thị trường

Tầng hiểu cao nhất về dealing range là xem luồng internal/external như **chu kỳ hô hấp** ([[16 - Internal & External Range Liquidity (IRL & ERL)]]):

```text
Pha 1: Giá lấy ERL (external — quét range high/low)
Pha 2: Đảo, quay vào tìm IRL (internal — FVG/OB đối diện)
Pha 3: Rebalance xong IRL → expansion tới ERL đối diện
→ lặp lại trên range mới
```

Trước mỗi phiên, chỉ cần trả lời: **"Giá đang ở pha nào của chu kỳ?"**
- Vừa quét ERL và reject → kỳ vọng chạy về IRL → trade reversal về internal.
- Vừa rebalance IRL (chạm CE của FVG giữa range) → kỳ vọng expansion tới ERL → trade continuation.
- Đang lơ lửng giữa hai pha (quanh EQ, chưa chạm gì) → không có vị trí — chờ.

Đây chính là khung trả lời "hôm nay là ngày reversal hay continuation" mà không cần đoán: **câu trả lời nằm ở việc chu kỳ ERL↔IRL vừa hoàn thành bước nào.**

### Best Practices — Dealing Range

> [!success] Best Practices
> 1. **Vẽ range trước khi vẽ bất kỳ thứ gì khác.** Range là bản đồ; FVG/OB/OTE chỉ là địa danh trên bản đồ. Mở chart = xác định range D1 → H4 → H1 theo thứ tự, rồi mới đánh dấu POI.
> 2. **Mỗi range phải trả lời được "hai đầu lấy liquidity nào?".** Không trả lời được = range chọn theo cảm tính → vẽ lại.
> 3. **Dùng quadrant, không chỉ nửa range.** Ưu tiên POI ở deep discount/deep premium; POI ở quadrant nông đòi hỏi confluence gấp đôi.
> 4. **Kiểm tra alignment 2 tầng trước mọi lệnh:** vị trí trong range HTF + vị trí trong range LTF. Ghi cả hai vào journal (`location_htf`, `location_ltf`) — các lệnh "discount trong discount" sẽ tự chứng minh edge qua thống kê.
> 5. **Phân xử sweep vs acceptance TRƯỚC khi re-map.** Wick qua external = chưa re-map; thân đóng + giữ ngoài = re-map ngay và cascade xuống các range con.
> 6. **Quanh EQ = không làm gì.** Đặt rule cứng: không mở lệnh mới khi giá trong dải 40–60% của range đang dùng, trừ khi playbook continuation sau rebalance IRL cho phép.
> 7. **Khi hết external phía trước, dùng SD projection** thay vì "gồng tới mức tròn" — target phải luôn là một cấu trúc đo được.
> 8. **Định kỳ audit range:** cuối mỗi phiên tự hỏi "range tôi dùng hôm nay có còn đúng cho ngày mai?" — external nào bị lấy, cần re-map gì; ghi vào daily note để sáng hôm sau không phân tích lại từ đầu.

---

## Tình huống thực chiến (War Stories)

> [!info] Vì sao có mục này
> Mọi mục ở trên dạy cách chọn range *đúng*. Mục này trả lời câu hỏi khó hơn mà chỉ nhiều giờ backtest/live mới đặt ra: **vì sao một range "đúng" vẫn phản bội mình** — và ở tầng sâu nhất, *vì sao* dealing range hoạt động ngay từ đầu. Mỗi tình huống có ba tầng: hiện tượng → cơ chế (WHY) → rule đo được.

### W0. Tầng WHY nền tảng — vì sao giá "tôn trọng" một cái hộp vô hình?

Trước khi vào các tình huống, cần trả lời câu hỏi mà đa số trader bỏ qua: **dealing range không có sức mạnh vật lý nào — vậy tại sao nó hoạt động?**

1. **Range là bản đồ phân bố LỆNH, không phải phân bố giá.** Hai đầu range là nơi tập trung stop (external liquidity); bên trong range là nơi các lệnh đã khớp dở dang cần được "hoàn tất hai chiều" (internal — FVG/OB). Giá di chuyển vì các thuật toán khớp lệnh lớn cần **đối tác**: nơi có lệnh chờ dày nhất chính là nơi giá bị hút về. Range "hoạt động" đơn giản vì nó vẽ lại đúng nơi lệnh đang nằm — xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]].
2. **EQ 50% hoạt động vì lý thuyết đấu giá, không vì Fibonacci.** Một dealing range là một phiên đấu giá chưa ngã ngũ: hai đầu là hai mức mà thị trường đã *từ chối* (quét xong rồi quay lại). Điểm giữa của hai mức từ chối là nơi định giá "công bằng" tạm thời — trên nó người bán có lợi thế vị trí, dưới nó người mua có lợi thế. Premium/discount là phát biểu ICT của khái niệm *value area* trong auction theory. Đây là lý do EQ không cần chính xác từng tick vẫn hoạt động: nó là **vùng trọng tâm của giá trị**, không phải một mức ma thuật.
3. **Luồng internal ↔ external hoạt động vì tồn kho (inventory) phải được cân.** Market maker/thuật toán khớp một khối lệnh lớn tại external (nơi duy nhất đủ thanh khoản) sẽ ôm một vị thế tồn kho lệch; họ đẩy giá về internal (FVG — nơi giao dịch một chiều còn dang dở) để xả/cân tồn kho ở giá tốt, rồi mới bắt đầu chu kỳ mới. "Nhịp thở" ERL↔IRL ở mục A5 chính là chu kỳ cân tồn kho này nhìn từ bên ngoài.

Ba cơ chế trên là nền của mọi tình huống dưới đây: khi range "phản bội", luôn là vì một trong ba giả định (bản đồ lệnh đúng, đấu giá chưa ngã ngũ, tồn kho chưa cân) đã bị phá mà mình không nhận ra.

### W1. Cùng một ngày, hai bản đồ — range trên Futures khác range trên CFD

![[Dealing-Range-War-Feed-Divergence.svg|720]]
*Sơ đồ: NQ futures (ETH) có đỉnh overnight mà CFD không hiển thị đủ; hai đầu range lệch → EQ lệch → premium/discount lệch theo.*

**Hiện tượng:** bạn vẽ range trên chart CFD NAS100, đo discount, chờ giá về OTE — giá đảo sớm hơn vùng của bạn vài chục điểm, đúng tại mức mà *trên chart futures* là 62% retracement. Hoặc equal highs "đẹp" trên CFD không tồn tại trên futures (và không bao giờ bị quét).

**WHY — vì sao hai feed khác nhau và vì sao futures thắng:** dealing range hoạt động vì nó vẽ bản đồ *lệnh thật*. Lệnh thật của chỉ số nằm ở **CME (futures NQ)** — đó là nơi các desk lớn đặt stop, nơi thuật toán tham chiếu. CFD là giá tổng hợp broker tạo ra từ futures cộng spread markup, và nhiều broker cắt bớt giờ giao dịch → **đỉnh/đáy overnight (nơi một đầu range thật hình thành) có thể không tồn tại trên chart CFD**. Khi hai đầu range sai thì mọi số phái sinh (EQ, OTE, quadrant) sai theo — đây chính là "chọn sai range" ở mục 9, nhưng dưới dạng không thể phát hiện nếu chỉ nhìn một chart.

**Rule đo được:**
- Bản đồ (range, pool, EQ) vẽ trên **futures**; thực thi ở đâu cũng được nhưng level lấy từ bản đồ gốc.
- Backtest và live cùng một feed — nếu không, thống kê `location_in_range` vô nghĩa.
- Với FX: dùng feed có khối lượng lớn/chuẩn interbank làm tham chiếu, chấp nhận sai số vài pip giữa broker và ghi rõ điều đó vào buffer của stop.

### W2. Seek & Destroy — ngày quét cả hai đầu: range không chết, nó được "sạc lại"

![[Dealing-Range-War-Seek-Destroy-Recharge.svg|720]]
*Sơ đồ: wick qua BSL, wick qua SSL, đóng ngày giữa range — cả hai external vừa được nạp thanh khoản mới; re-map lúc này là lỗi.*

**Hiện tượng:** ngày S&D quét cả hai external rồi đóng giữa range. Phản xạ sai phổ biến: "cả hai đầu đã bị lấy → range chết → vẽ range mới nhỏ hơn bên trong". Range mới nhỏ hơn đó cho premium/discount nhiễu và hôm sau bị nghiền.

**WHY — vì sao range sau S&D lại *mạnh hơn*:** quay về cơ chế nền W0.1 — stop là hàng tiêu hao, nhưng **cú quét cũng là máy sản xuất stop mới**. Wick qua BSL kích hoạt buy stops cũ *và* kéo một lớp breakout trader mới vào Long (stop của họ giờ nằm dưới); wick qua SSL làm điều đối xứng. Đóng ngày giữa range nghĩa là thuật toán đã **kiểm tra cả hai phía và từ chối cả hai** — đó là bằng chứng đắt giá nhất có thể có rằng biên range đúng. Về mặt đấu giá (W0.2): hai mức từ chối vừa được *tái xác nhận*, nên EQ cũ càng đáng tin. Re-map chỉ được phép khi có **acceptance** (đóng thân + giữ ngoài) — wick hai phía là điều ngược lại của acceptance.

**Rule đo được:**
- Sau ngày S&D: **giữ nguyên range + EQ**, nâng độ tin của hai external thêm một bậc.
- Sweep *lần hai* cùng một đầu trong những ngày kế = tier thấp hơn lần đầu (pool đã mỏng đi) — điều chỉnh kỳ vọng reversal tương ứng.
- Break thật qua external sau ngày S&D thường cần catalyst (tin lớn, mở tuần) — không có catalyst mà "phá" thì nghi ngờ gấp đôi.
- Journal: `range_context` (fresh / one_side_swept / both_swept_SD).

### W3. Range quá rộng — khi "discount" vẫn còn cách đáy 300 điểm

**Hiện tượng:** D1 range của NQ sau một tuần biến động rộng 800 điểm. Giá "vào discount" (dưới 50%) — nhưng dưới đó vẫn còn 300 điểm không gian. Long "vì đang discount" rồi chịu 3 lần stop trước khi giá tìm được đáy thật ở deep discount.

**WHY — vì sao % không phải là khoảng cách:** premium/discount là **xác suất có điều kiện, không phải mức giá**. "Ở discount" chỉ nói rằng bên mua có lợi thế vị trí *tương đối*; nó không nói lệnh mua thật nằm ở đâu. Lệnh thật (theo W0.1) nằm tại các PD array cụ thể — FVG, OB — và trong range rộng, các array đó phân bố thưa. Khoảng giữa hai array là "đất trống": không có lệnh chờ nào ở đó, nên không có lý do nào để giá dừng ở đó. Range càng rộng, sai số của phép đo % càng lớn so với sai số của một array cụ thể.

**Rule đo được:**
- Range rộng bất thường (so với ADR trung bình 20 ngày, ví dụ > 1.5×): **cấm trade theo nửa range** — chỉ trade theo quadrant + array cụ thể (deep discount + FVG/OB, không phải "dưới 50%").
- Kết hợp ma trận A2: vị trí phải cộng hưởng ở cả hai tầng (D1 discount **và** H1 discount) và entry phải nằm *tại một array*, không nằm giữa đất trống.
- Journal: `range_width_vs_adr` — biến này giải thích một phần lớn các lệnh "đúng vùng, sai 100 điểm".

### W4. EQ "trôi" qua đêm — sáng ra mọi level lệch vài điểm mà không ai báo

**Hiện tượng:** tối hôm trước bạn đo EQ = 20,302 và đặt alert/limit quanh OTE. Trong đêm, giá nhúng nhẹ làm range low thấp hơn 18 điểm — về cấu trúc range **không đổi** (vẫn swing đó, chỉ wick sâu hơn), nhưng **mọi mức % đã trôi**: EQ mới 20,293, OTE dịch theo. Limit của bạn giờ nằm lệch ngoài vùng thật — giá chạm vùng thật, đảo, và bạn đứng ngoài nhìn (hoặc tệ hơn: limit khớp ở mức đã thành premium nông).

**WHY — vì sao vài điểm lại quan trọng ở đây:** bản thân EQ là *vùng*, không phải mức (W0.2) — nhưng **OTE và quadrant biên là nơi các cụm lệnh limit của cả đám đông ICT trader đặt gần nhau**. Thuật toán khớp quanh các cụm đó với độ chính xác cao (đó chính là lý do "quét đúng mép" tồn tại). Sai số 15–20 điểm đủ để bạn rơi từ "trong cụm" ra "ngoài cụm". Level tĩnh trong một thị trường chạy 24h là một giả định sai âm thầm.

**Rule đo được:**
- **Đo lại toàn bộ range levels mỗi sáng** như một bước cứng trong pre-market routine (không kế thừa số của hôm qua) — cùng nguyên tắc với câu hỏi mở phiên bên [[12 - Daily Bias]].
- Dùng anchored fib trên chart (neo vào swing, tự cập nhật khi wick giãn) thay vì kẻ tay mức giá tĩnh.
- Alert đặt ở *vùng* (dải giá quanh OTE) chứ không ở một tick.

### W5. Ba tầng range đều "hợp lệ" — và sự tê liệt của người phân tích giỏi

**Hiện tượng:** sau nhiều ngày consolidation, chart có 3 range lồng nhau đều đúng sách: range tuần (external chưa lấy hai đầu), range 3 ngày, range trong ngày. Ba bản đồ cho ba kết luận premium/discount khác nhau. Người mới chọn bừa; người giỏi… phân tích cả buổi rồi không trade được — cả hai đều thua theo cách của mình.

**WHY — vì sao nhiều range hợp lệ cùng lúc là một *thông điệp*, không phải một bài toán:** theo W0.3, giá di chuyển khi có tồn kho cần cân và pool rõ để nhắm tới. Ba tầng range mơ hồ chồng nhau nghĩa là **không có delivery nào đang dang dở** — thuật toán không nợ ai điều gì ở cả ba tầng. Đó chính là trạng thái "chưa chọn phía" quanh EQ (mục A1) phóng to lên nhiều tầng. Thị trường đang *tích luỹ thanh khoản hai phía để chuẩn bị cho expansion* — và expansion đó sẽ chỉ bắt đầu bằng một cú quét external của tầng LỚN nhất.
**Câu trả lời đúng không phải "chọn range nào" mà là "chưa có gì để trade cho tới khi tầng lớn nhất bị quét."**

**Rule đo được:**
- Khi ≥2 tầng range cho kết luận mâu thuẫn và không tầng nào có draw rõ vượt trội → ghi **No Trade / chờ sweep external của tầng cao nhất** vào pre-market note. Đây là một kết luận, không phải sự bất lực.
- Sau cú sweep external tầng cao nhất: các tầng dưới thường tự sắp hàng lại trong 1–2 phiên — lúc đó ma trận A2 mới dùng được.
- Journal: `nested_range_conflict` (true/false) — thống kê các lệnh vào trong trạng thái conflict; win rate của nhóm này thường là con số thuyết phục mình đứng ngoài tốt hơn mọi lời khuyên.

> [!success] Tổng kết mục War Stories
> Tầng WHY chung: dealing range hoạt động vì nó vẽ đúng **bản đồ lệnh** (W0.1), đúng **phiên đấu giá** (W0.2), đúng **chu kỳ cân tồn kho** (W0.3). Nó phản bội khi bản đồ vẽ trên feed sai (W1), khi đọc nhầm "sạc lại" thành "chết" (W2), khi nhầm % với vị trí lệnh thật (W3), khi level tĩnh trong thị trường động (W4), và khi ép mình trade lúc thuật toán không nợ ai điều gì (W5). Journal fields: `range_context`, `range_width_vs_adr`, `nested_range_conflict`.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Dealing Range chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**. Range đúng là điều kiện tiên quyết; có range chưa phải là có lệnh.

### A. Context (HTF — xác định range)
- [ ] Tôi đã chọn dealing range trên **đúng timeframe** khớp narrative.
- [ ] Hai đầu range là swing có ý nghĩa, tạo bởi displacement/BOS.
- [ ] Hai đầu range liên quan tới liquidity (BSL ở đỉnh, SSL ở đáy).
- [ ] Tôi đã đánh dấu equilibrium (50%) và biết giá đang premium hay discount.
- [ ] Tôi xác định external liquidity nào còn mở → đó là draw on liquidity.
- [ ] Có internal POI (FVG/OB) hợp lệ ở đúng nửa range cho hướng trade.
- [ ] Range hiện còn hiệu lực (external chưa bị lấy).

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã vào internal POI và đúng vùng premium/discount cho hướng trade.
- [ ] Có liquidity sweep (external nhỏ hoặc internal SSL/BSL) trước reversal.
- [ ] Có MSS trên LTF, nằm trong POI / đúng nửa range.
- [ ] Có displacement tạo FVG/OB để vào lệnh có cấu trúc.
- [ ] Entry trùng OTE / internal liquidity của range.
- [ ] Target là external liquidity rõ ràng (đầu kia của range), internal đối diện trước.
- [ ] R:R tối thiểu đạt kế hoạch (range đủ rộng để có room tới external).

### C. Quy tắc "không có lệnh"
- [ ] Không xác định được dealing range hợp lệ → không trade.
- [ ] Giá ở giữa range / quanh equilibrium → không trade.
- [ ] External đã bị lấy, range cũ hết hiệu lực, chưa vẽ range mới → không trade.
- [ ] Premium/Discount đo trên range sai timeframe → dừng lại, vẽ lại trước khi xét lệnh.

---

## 9. Lỗi thường gặp

![[Dealing-Range-Sec-09-Loi-Thuong-Gap.svg|720]]
*Sơ đồ: Các lỗi phổ biến khi chọn Dealing Range — range quá nhỏ, sai timeframe, không vẽ lại, và cách sửa.*

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Chọn range quá nhỏ | Lấy hai swing nhỏ gần giá làm range | Premium/Discount lệch → mua premium / bán discount mà tưởng đúng vùng | Chọn swing có displacement/BOS và đã lấy liquidity |
| Chọn range quá cũ | Dùng range đã hết hiệu lực vì gần giá hiện tại | External có thể đã bị lấy từ lâu; số premium/discount vô nghĩa | Cập nhật range theo swing có ý nghĩa gần nhất còn hiệu lực |
| Đo trên sai timeframe | Dùng range M5 để kết luận bias D1 | Vị trí premium/discount mâu thuẫn với HTF thật | Đo bias trên HTF range; M5 chỉ dùng cho execution |
| Không vẽ lại sau khi external bị lấy | Vẫn dùng range cũ sau khi BSL/SSL đỉnh/đáy đã bị quét | Range "chết" cho draw on liquidity sai | Khi external bị lấy → cập nhật range mới ngay |
| Lẫn internal với external | Coi FVG bên trong là target chính thay vì BSL/SSL ở hai đầu | Đặt TP sai, thoát non hoặc target không tồn tại như draw | Phân biệt: external = hai đầu range; internal = FVG/OB bên trong |
| Mua/bán quanh equilibrium | Vào lệnh khi giá ở giữa range | R:R kém, dễ chop, dễ bị quét hai phía | Chỉ Long ở discount, Short ở premium; equilibrium thì chờ |
| Bỏ qua draw on liquidity | Trade ngược phía external còn mở | Giá thường bị hút về external chưa bị lấy | Trade thuận draw: external còn mở phía nào, ưu tiên hướng đó |
| Chọn range không lấy liquidity ở đầu | Hai đầu chỉ là swing "đẹp" nhưng chưa quét stops | Đỉnh/đáy đó dễ bị xuyên thủng, range không bền | Ưu tiên hai đầu đã quét BSL/SSL rõ ràng |
| Cố giữ một range cả ngày | Thị trường đã phá range nhưng vẫn đo trên range cũ | Bias và POI lệch theo range chết | Reassess range sau mỗi lần external bị lấy hoặc BOS HTF |
| Đo OTE trên range sai | Vẽ Fibonacci 62–79% trên range không hợp lệ | Vùng OTE rơi vào nơi không có nghĩa | OTE chỉ tính trên dealing range đúng đã quét liquidity |

---

## 10. Câu hỏi tự kiểm tra

- Tôi có thể chỉ ra hai đầu Dealing Range hiện tại và giải thích vì sao chúng có ý nghĩa không?
- Hai đầu range đã lấy liquidity (BSL/SSL) chưa, hay chỉ là swing "đẹp"?
- Range tôi đang đo có khớp với timeframe và narrative tôi đang phân tích không?
- Giá đang ở premium, discount hay equilibrium của **range nào**?
- External liquidity nào còn mở? Đó có phải draw on liquidity hôm nay không?
- Đâu là internal liquidity (FVG/OB) trong range, và nó ở nửa nào?
- Range hiện còn hiệu lực không, hay external đã bị lấy và tôi cần vẽ lại?
- Tôi có đang mua premium / bán discount vì chọn sai range không?
- Luồng kỳ vọng (internal → external hoặc sweep external → đảo) là gì?
- Setup nào trong trade journal đã đo premium/discount trên range đúng/sai?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Dealing Range là gì?  
**Đáp:** Khoảng giá giữa một swing high và swing low CÓ Ý NGHĨA mà giá đang vận động bên trong, được xác định bởi hai điểm đã lấy liquidity ở hai đầu (hoặc một đỉnh rõ tới một đáy rõ). Nó là khung tham chiếu để đo premium/discount và xác định draw on liquidity.

### Q2
**Hỏi:** Dealing Range dùng để làm gì trong ICT?  
**Đáp:** (1) Suy ra Premium/Discount/Equilibrium; (2) Phân loại internal liquidity (FVG/OB bên trong) vs external liquidity (đỉnh/đáy = BSL/SSL); (3) Dự phóng draw on liquidity theo luồng internal ↔ external.

### Q3
**Hỏi:** Phân biệt internal và external range liquidity?  
**Đáp:** External = chính đỉnh/đáy range (BSL ở trên, SSL ở dưới), nằm ở hai đầu. Internal = FVG/OB/imbalance nằm BÊN TRONG range. Giá thường đi từ internal tới external hoặc quét external rồi đảo về internal đối diện.

### Q4
**Hỏi:** Làm sao chọn đúng Dealing Range?  
**Đáp:** Chọn swing high/low tạo bởi displacement/BOS và đã lấy liquidity; KHÔNG chọn swing quá nhỏ hoặc quá cũ chỉ vì gần giá. Range phải phù hợp narrative/timeframe đang phân tích.

### Q5
**Hỏi:** Khi nào phải vẽ lại Dealing Range?  
**Đáp:** Khi external liquidity (đỉnh/đáy range) bị lấy và một swing có ý nghĩa mới hình thành. Lúc đó range cũ hết hiệu lực; cập nhật range mới rồi đo lại premium/discount.

### Q6
**Hỏi:** Vì sao chọn sai Dealing Range nguy hiểm?  
**Đáp:** Vì premium/discount, OTE và equilibrium đều đo bằng % trên range. Range sai → vị trí sai → mua premium / bán discount mà tưởng đang trade đúng vùng. Đây là lỗi đã cảnh báo trong Daily Bias.

### Q7
**Hỏi:** Quan hệ giữa Dealing Range và Daily Bias?  
**Đáp:** Dealing Range là nền để xây bias. Daily Bias dùng vị trí giá trong range (premium/discount) cộng với draw on liquidity (external nào còn mở) để kết luận hướng ưu tiên Long/Short/Neutral.

---

## 12. Lesson Learned

### Bài học chính
- Dealing Range là **khung tham chiếu**, không phải tín hiệu vào lệnh; nhưng không có khung đúng thì mọi tín hiệu khác đều vô nghĩa.
- Premium/Discount và OTE chỉ là **% đo trên range** — chọn sai range là sai từ gốc, không cách nào sửa ở entry.
- External liquidity (hai đầu range) là draw on liquidity; internal liquidity (FVG/OB) là nơi rebalance — đừng lẫn lộn hai vai trò.
- Khi external bị lấy, range cũ **chết**; cố giữ range cũ là tự bóp méo bias cả ngày.
- Range đúng là **điều kiện tiên quyết** cho Daily Bias, Premium/Discount và OTE — kiểm tra range trước, đo số sau.

### Quy tắc cá nhân rút ra
- [ ] Tôi không đo premium/discount trước khi xác nhận range hợp lệ (swing có ý nghĩa + lấy liquidity + đúng timeframe).
- [ ] Tôi không Long ở premium / Short ở discount; quanh equilibrium thì chờ.
- [ ] Khi external (đỉnh/đáy range) bị lấy, tôi vẽ lại range mới trước khi tìm lệnh tiếp.
- [ ] Tôi luôn ghi external draw (BSL/SSL còn mở) và internal POI khi xác định range.
- [ ] Tôi không dùng range M5 để kết luận bias HTF; M5 chỉ cho execution.

### Câu nhắc nhở khi trade
> **"Range sai thì discount cũng là premium. Chọn đúng khung trước, mọi con số mới có nghĩa."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt internal vs external liquidity và vai trò khung tham chiếu không? |
| Nhận diện trên chart |  | Có chọn đúng hai đầu range (displacement/BOS + lấy liquidity) không? |
| Biết khi nào bỏ qua |  | Có nhận ra range chết / sai timeframe / giá ở equilibrium không? |
| Kết hợp với context HTF |  | Range con LTF có khớp và hỗ trợ HTF range không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự ở discount/premium đúng range, target tới external không? |
| Review sau trade |  | Có kiểm tra range_valid_at_entry và location_in_range bằng journal không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Dealing Range]]`.
- [ ] Review riêng các lệnh đo trên **range đúng** vs **range sai/quá nhỏ/quá cũ**.
- [ ] Thống kê win rate và average R theo `location_in_range`.
- [ ] Cập nhật rule chọn range chỉ khi dữ liệu backtest/forward test đủ mẫu.
