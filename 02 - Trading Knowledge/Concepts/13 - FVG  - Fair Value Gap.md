---
type: ict-concept
concept: Fair Value Gap
aliases:
  - FVG
  - Fair Value Gap
  - Imbalance
  - BISI
  - SIBI
tags:
  - trading/ict/concept
  - trading/study
  - "#FVG"
status: tested
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-18
common_mistakes:
  - "[[Mistake - Trade Every FVG]]"
  - "[[Mistake - FVG Without Displacement]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
---

# Fair Value Gap

> [!summary] Tóm tắt 1 câu
> **Fair Value Gap (FVG) là vùng mất cân bằng (imbalance) tạo bởi 3 nến, nơi giá được giao dịch một chiều quá nhanh do displacement, để lại một khoảng giá chưa được cân bằng mà thị trường có xu hướng quay lại rebalance — vừa là POI để vào lệnh, vừa là draw để giá bị hút về.**

> [!important] Nguyên tắc cốt lõi
> **FVG chỉ là một điểm tham chiếu giá; nó KHÔNG phải tín hiệu trade. Chỉ FVG sinh ra từ displacement phá cấu trúc (BOS/MSS), nằm tại POI HTF, đúng premium/discount, đồng hướng Daily Bias và xuất hiện sau liquidity sweep mới đáng vào lệnh.**
> Một FVG nhỏ giữa range, không có displacement, không có context bias là nhiễu — đừng trade.

---

## 1. Định nghĩa

![[FVG-Sec-01-Dinh-Nghia.svg|720]]
*Sơ đồ: Cấu trúc 3 nến của Bullish FVG (BISI) và Bearish FVG (SIBI); mức CE (50%) là tham chiếu quan trọng nhất.*

**Khái niệm:**  
Fair Value Gap là một vùng **imbalance** trên chart, hình thành khi giá di chuyển một chiều quá mạnh và quá nhanh (single-sided delivery / displacement), khiến một phần khoảng giá không được giao dịch đầy đủ ở cả hai phía. FVG được nhận diện qua **3 nến liên tiếp**:

- **Bullish FVG (BISI — Buyside Imbalance Sellside Inefficiency):** khoảng trống giữa **HIGH của nến 1** và **LOW của nến 3**, với **nến 2** là nến displacement tăng mạnh. Khoảng giữa hai mức này chưa được cân bằng bởi phía bán → giá có xu hướng quay lại lấp nó.
- **Bearish FVG (SIBI — Sellside Imbalance Buyside Inefficiency):** khoảng trống giữa **LOW của nến 1** và **HIGH của nến 3**, với **nến 2** là nến displacement giảm mạnh.

**Bản chất:** FVG là một dạng **price inefficiency**. Trong một thị trường "fair", giá nên giao dịch đủ ở cả hai phía. Khi displacement xảy ra, giá nhảy qua một vùng mà không có sự tham gia đầy đủ của bên đối diện → vùng đó "kém hiệu quả" (inefficient). Logic ICT là thị trường có xu hướng quay về **rebalance** vùng imbalance này trước khi tiếp tục delivery.

**CE (Consequent Encroachment):** là mức **50% của gap** — mức quan trọng nhất để xác nhận phản ứng. Giá thường tôn trọng CE: nếu chỉ retrace tới CE rồi reject, đó là dấu hiệu FVG đang được "respect". CE còn là điểm tham chiếu để chia một FVG lớn thành hai nửa premium/discount nội bộ.

**Mục đích trong ICT:**  
- Là **POI (Point of Interest)** để vào lệnh: chờ giá retrace về FVG rồi tìm entry.
- Là **DRAW on liquidity / draw on price**: giá bị hút về lấp FVG hoặc rebalance imbalance còn mở.
- Là bằng chứng của **intent**: một FVG sinh ra từ displacement phá cấu trúc cho thấy có "chủ đích" đẩy giá.
- Là vùng đặt **stop loss logic**: stop thường nằm ngoài đầu kia của FVG / đầu displacement.

**Vì sao khái niệm này quan trọng:**  
FVG là một trong những PD Array trung tâm của ICT 2022 model. Nhưng chính vì dễ thấy, nó là khái niệm bị **lạm dụng** nhiều nhất: trader vẽ FVG khắp nơi và trade mọi gap. FVG chỉ có edge khi đặt trong narrative HTF + liquidity + premium/discount đúng — giống hệt triết lý của [[12 - Daily Bias]].

**Nó giúp trả lời câu hỏi nào trên chart?**
- Sau displacement, giá có khả năng retrace về đâu để tìm entry?
- Imbalance nào còn mở mà giá có thể bị hút về (draw)?
- Mức 50% (CE) nào giá đang tôn trọng?
- FVG này có "chất lượng" không, hay chỉ là gap ngẫu nhiên giữa range?
- FVG đã bị xuyên thủng và đảo cực (IFVG) chưa?

### Fair Value Gap không phải là gì
- Không phải "cứ thấy gap 3 nến là vào lệnh".
- Không phải tín hiệu độc lập — nó là điểm tham chiếu giá, cần context bias + liquidity.
- Không phải mọi FVG đều phải được lấp; chỉ imbalance phù hợp narrative mới là draw đáng tin.
- Không phải lý do bỏ qua premium/discount: Long ở FVG premium hay Short ở FVG discount thường là chase.
- Không phải bất biến — khi bị đóng nến xuyên qua, FVG có thể invalid hoặc đảo cực thành IFVG.
- Không thay thế cho liquidity sweep: FVG entry trước khi sweep thường bị quét stop.

---

## 2. Bối cảnh sử dụng

![[FVG-Sec-02-Boi-Canh.svg|720]]
*Sơ đồ: Khi nào FVG có giá trị cao (đồng hướng bias, ở discount/premium, sau sweep) và khi nào nên bỏ qua.*

### Các loại / trạng thái của FVG

| Loại | Thuật ngữ ICT | Cấu trúc | Ý nghĩa thực chiến |
|---|---|---|---|
| **Bullish FVG** | BISI (Buyside Imbalance Sellside Inefficiency) | Gap giữa high nến 1 và low nến 3, nến 2 displacement tăng | Vùng discount để tìm Long khi giá retrace về; hỗ trợ |
| **Bearish FVG** | SIBI (Sellside Imbalance Buyside Inefficiency) | Gap giữa low nến 1 và high nến 3, nến 2 displacement giảm | Vùng premium để tìm Short khi giá retrace về; kháng cự |
| **Inversion FVG (IFVG)** | — | FVG bị đóng nến xuyên qua → đảo cực tính | Bullish FVG fail → thành kháng cự bearish; và ngược lại |
| **Liquidity Void / lớn** | — | Vùng imbalance rất rộng do displacement cực mạnh | Draw mạnh; giá thường rebalance phần lớn void |

> [!tip]
> FVG đóng **hai vai trò** và bạn phải biết mình đang dùng vai nào: (1) **POI để entry** khi giá retrace về; (2) **DRAW / target** khi có một FVG còn mở ở phía xa mà giá bị hút về để rebalance. Cùng một imbalance có thể là entry trên LTF và là target trên HTF.

### Khi nào khái niệm này có giá trị cao?
- [ ] FVG sinh ra từ **displacement phá cấu trúc** (BOS/MSS), không phải gap giữa range.
- [ ] FVG nằm tại **POI HTF** (D1/H4/H1 FVG hoặc OB) đồng hướng bias.
- [ ] FVG nằm đúng **premium** (cho Short) hoặc **discount** (cho Long) của dealing range.
- [ ] FVG xuất hiện **sau liquidity sweep** đúng thứ tự (sweep → displacement → FVG).
- [ ] FVG còn **unmitigated** (chưa bị lấp / chưa bị xuyên CE).
- [ ] CE (50%) của FVG trùng với một mức tham chiếu khác (OB, equilibrium, OTE).
- [ ] Có liquidity rõ ràng phía bên kia để làm target sau khi entry tại FVG.

### Khi nào nên bỏ qua?
- [ ] FVG nhỏ, không có displacement rõ, nằm giữa range / quanh equilibrium.
- [ ] FVG ngược Daily Bias mà không có counter-trend playbook riêng.
- [ ] FVG đã bị lấp toàn bộ hoặc bị đóng nến xuyên qua (đã mitigate / invalid).
- [ ] FVG ở sai phía premium/discount (Long ở FVG premium, Short ở FVG discount).
- [ ] FVG xuất hiện trước khi liquidity bị sweep — entry sẽ thành mồi cho sweep.
- [ ] Có hàng loạt FVG chồng chéo, không xác định được cái nào có ý nghĩa.
- [ ] FVG ngoài kill zone / ngoài kế hoạch session.

---

## 3. Cấu trúc nhận diện trên chart

![[FVG-Sec-03-Nhan-Dien.svg|720]]
*Sơ đồ: Quy trình nhận diện một FVG hợp lệ trên chart — displacement, gap chưa được lấp, xác định CE.*

### Dấu hiệu chính
1. **Ba nến:** xác định nến 1, nến 2 (displacement), nến 3. Gap = vùng giữa nến 1 và nến 3, KHÔNG bị thân/bóng nến 2 lấp kín.
2. **Nến giữa là displacement:** nến 2 có body lớn, đóng quyết đoán, thể hiện urgency và single-sided delivery.
3. **Khoảng trống còn thật:** với bullish FVG, low của nến 3 phải nằm CAO hơn high của nến 1; nếu chồng lấp thì không có FVG hợp lệ.
4. **CE 50%:** đánh dấu mức giữa của gap — đây là mức phản ứng quan trọng nhất.
5. **Context phá cấu trúc:** displacement tạo FVG có đi kèm BOS/MSS không? Đó là yếu tố phân biệt FVG chất lượng với gap ngẫu nhiên.

### Ma trận nhận diện FVG

| Thành phần | Bullish FVG (BISI) | Bearish FVG (SIBI) | Cảnh báo / FVG yếu |
|---|---|---|---|
| **Khoảng gap** | High nến 1 < Low nến 3 | Low nến 1 > High nến 3 | Nến 1 và 3 chồng lấp; gap quá nhỏ |
| **Nến giữa** | Displacement tăng, body lớn, đóng mạnh | Displacement giảm, body lớn, đóng mạnh | Nến 2 doji/body nhỏ, không urgency |
| **Cấu trúc** | Displacement phá swing high → BOS/MSS bullish | Displacement phá swing low → BOS/MSS bearish | Không phá cấu trúc, chỉ dao động nội bộ |
| **Location** | Ở discount của dealing range | Ở premium của dealing range | Quanh equilibrium / sai phía |
| **Liquidity** | Sau sweep SSL → repricing lên | Sau sweep BSL → repricing xuống | Chưa sweep; hoặc đã lấy target rồi |
| **Trạng thái** | Còn unmitigated, CE chưa bị xuyên | Còn unmitigated, CE chưa bị xuyên | Đã lấp toàn bộ / đóng nến xuyên qua |

### Điều kiện bắt buộc
- [ ] Xác định đúng 3 nến và khoảng gap thật (không bị lấp kín).
- [ ] Nến giữa là displacement có body rõ, không phải nến nhỏ ngẫu nhiên.
- [ ] Xác định được mức CE (50%) của FVG.
- [ ] Xác định FVG đang ở premium hay discount của dealing range phù hợp.
- [ ] Xác định trạng thái: unmitigated / partially filled / fully filled / inverted.

### Điều kiện tăng xác suất
- [ ] Displacement tạo FVG đồng thời tạo BOS/MSS có ý nghĩa.
- [ ] FVG nằm bên trong hoặc trùng một POI HTF lớn hơn (HTF FVG, OB).
- [ ] FVG xuất hiện ngay sau một liquidity sweep đúng hướng narrative.
- [ ] FVG đúng phía premium/discount cho hướng trade.
- [ ] CE của FVG trùng với equilibrium / OTE / OB → confluence.
- [ ] Còn liquidity rõ ràng (external/internal) làm target sau entry.
- [ ] FVG nằm trong kill zone phù hợp với plan session.

### Điều kiện làm setup yếu đi
- FVG sinh ra từ nến giữa body nhỏ, không có urgency / không phá cấu trúc.
- FVG nằm giữa range hoặc sai phía premium/discount.
- FVG đã bị giá test nhiều lần, mỗi lần ăn mòn dần (giảm chất lượng).
- FVG xuất hiện sau một expansion lớn đã chạy xa — entry trở thành chase.
- Nhiều FVG chồng chéo gần nhau khiến không có mức tham chiếu rõ.
- FVG ngược Daily Bias mà không có bằng chứng đảo HTF.

---

## 4. Quy trình phân tích đa khung thời gian

![[FVG-Sec-04-Da-Khung.svg|720]]
*Sơ đồ: Luồng phân tích đa khung D1/H4 → H1/M15 → M5/M1 để định vị và vào lệnh tại FVG.*

> [!example] Quy trình 4 câu bắt buộc trước khi dùng FVG
> 1. **FVG này sinh ra từ displacement phá cấu trúc hay chỉ là gap giữa range?**  
> 2. **Nó nằm ở POI HTF nào và đúng premium/discount cho hướng bias không?**  
> 3. **Liquidity đã bị sweep trước khi FVG hình thành chưa?**  
> 4. **CE của FVG ở đâu, và điều gì làm FVG này invalid?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **HTF FVG / imbalance làm DRAW:** có FVG D1/H4 nào còn mở mà giá bị hút về để rebalance không? Đây thường là **target** chứ không phải entry.
- **HTF FVG làm POI:** có D1/H4 FVG đồng hướng bias, đúng premium/discount, còn unmitigated không?
- **Vị trí premium/discount:** FVG cần Long phải ở discount; FVG cần Short phải ở premium của HTF dealing range.

### H1 / M15 — POI & Context
- **POI cụ thể:** ghi rõ vùng FVG H1/M15 và mức CE, ví dụ `H1 bullish FVG 1.0820–1.0835, CE = 1.08275`.
- **Lý do POI hợp lệ:** FVG có sinh ra từ displacement không? Có ở đúng premium/discount không? Còn unmitigated không? Đồng hướng draw on liquidity không?
- **Liquidity:** giá đã sweep pool đối diện chưa? Sweep ở đâu, reclaim/reject thế nào?
- **Phân biệt fill vs respect:** giá chạm CE rồi reject (respect) khác với giá lấp toàn bộ FVG rồi đóng nến xuyên qua (invalid).

### M5 / M1 — Confirmation & Entry
- **Có MSS không?** sau khi giá vào FVG POI, có bullish/bearish MSS xác nhận đảo hướng nội bộ không?
- **Có displacement LTF không?** displacement LTF thường tạo một FVG nhỏ hơn để làm entry refined.
- **Entry tại đâu trong FVG?** ICT thường ưu tiên entry quanh **CE (50%)** thay vì mép xa của gap, để cải thiện R:R.
- **Stop loss logic:** đặt ngoài đầu kia của FVG / ngoài điểm sweep, không đặt tùy ý.

```text
Mẫu ghi nhanh — Bullish FVG Entry
HTF Bias: Bullish | Location: Discount
Draw on liquidity: BSL tại [level]
POI: H1 bullish FVG [low]–[high], CE = [mid]
Sweep: đã quét SSL dưới [level] trước khi displacement
Entry plan: chờ giá retrace về CE của H1 FVG → M5 bullish MSS + FVG → entry quanh CE
Stop: dưới low của FVG / dưới sweep low
Target: internal liquidity trước, BSL chính sau
Invalid: đóng nến M5/H1 xuyên thủng dưới FVG (acceptance) → bỏ / chờ IFVG
```

```text
Mẫu ghi nhanh — Bearish FVG Entry
HTF Bias: Bearish | Location: Premium
Draw on liquidity: SSL tại [level]
POI: H1 bearish FVG [low]–[high], CE = [mid]
Sweep: đã quét BSL trên [level] trước khi displacement
Entry plan: chờ giá retrace lên CE của H1 FVG → M5 bearish MSS + FVG → entry quanh CE
Stop: trên high của FVG / trên sweep high
Target: internal liquidity trước, SSL chính sau
Invalid: đóng nến M5/H1 xuyên thủng trên FVG (acceptance) → bỏ / chờ IFVG
```

> [!warning]
> **FVG trên M5/M1 không "tạo" bias.** Nó chỉ là execution refinement. Một bullish M5 FVG ngược Daily Bearish Bias không cho phép Long, trừ khi HTF narrative đã thực sự đảo.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

![[FVG-Sec-05-Xac-Nhan.svg|720]]
*Sơ đồ: Điều kiện FVG được xem là hợp lệ vs bị vô hiệu — phân biệt fill / respect / mitigation / inversion.*

### Setup được xem là hợp lệ khi
- [ ] FVG sinh ra từ displacement phá cấu trúc (BOS/MSS), có chủ đích.
- [ ] FVG nằm tại POI HTF đồng hướng Daily Bias.
- [ ] FVG đúng phía premium (Short) / discount (Long) của dealing range.
- [ ] Liquidity phía đối diện đã bị sweep trước khi displacement tạo FVG.
- [ ] Giá chạm CE / vùng FVG và **respect** (reject với phản ứng), không xuyên thủng.
- [ ] LTF có MSS + displacement xác nhận khi giá vào FVG.
- [ ] Có target liquidity rõ ràng và R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Giá **đóng nến xuyên qua** toàn bộ FVG và giữ giá ngoài vùng (acceptance) → FVG invalid (có thể chuyển sang IFVG).
- [ ] FVG không sinh ra từ displacement — chỉ là gap nhỏ giữa range.
- [ ] Không có liquidity sweep trước khi vào FVG.
- [ ] FVG ở sai phía premium/discount cho hướng trade.
- [ ] FVG ngược Daily Bias mà không có bằng chứng HTF đảo.
- [ ] FVG đã bị test/ăn mòn nhiều lần, chất lượng giảm.
- [ ] LTF không tạo MSS/displacement khi giá vào FVG — chỉ "rơi xuyên" qua.

### Fill vs Respect vs Mitigation vs Inversion

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Giá chạm CE (50%) hoặc mép gần FVG rồi reject với displacement ngược | **Respect** | FVG đang giữ; entry hợp lệ quanh CE, chờ LTF confirm |
| Giá lấp một phần FVG (chưa tới CE) rồi reject | **Partial fill / respect** | FVG vẫn còn hiệu lực; phản ứng tại đầu gap |
| Giá lấp toàn bộ FVG, chạm hết gap, rồi mới reject | **Full fill (mitigation)** | Imbalance đã rebalance; chỉ trade nếu có thêm POI/confirmation |
| Giá **đóng nến** xuyên thủng và giữ giá ngoài FVG | **Invalidation** | FVG hết hiệu lực; cảnh giác đảo cực thành IFVG |
| FVG bị xuyên + đóng nến qua → đổi vai trò support/resistance | **Inversion FVG (IFVG)** | Bullish FVG fail → thành kháng cự bearish; bearish FVG fail → thành hỗ trợ bullish |

> [!note]
> **Inversion FVG (IFVG)** là khái niệm mạnh: một FVG thất bại không "biến mất" — nó đảo cực. Khi bullish FVG bị đóng nến xuyên xuống, vùng đó trở thành **kháng cự**; giá retrace lên test lại nó là cơ hội Short (đồng hướng bias bearish mới). Ngược lại với bearish FVG fail thành hỗ trợ. IFVG là dấu hiệu thị trường đã đổi delivery, thường đi kèm MSS.

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish FVG tại discount POI, Long theo ICT 2022 Model
![[FVG-Example-Correct.png]]

**Mô tả:**  
D1/H4 bullish, draw on liquidity là BSL phía trên. Giá retrace vào discount, sweep sell-side liquidity dưới một đáy ngắn hạn trong kill zone. Ngay sau sweep, một nến displacement tăng mạnh phá swing high nội bộ (MSS bullish) và để lại một bullish FVG (BISI). Giá retrace về **CE (50%)** của FVG, reject, M5 tạo bullish MSS nhỏ. Entry quanh CE; stop dưới low FVG / dưới sweep low; TP hướng về BSL.

**Vì sao đây là ví dụ tốt:**
- FVG sinh ra từ displacement **phá cấu trúc**, không phải gap ngẫu nhiên.
- FVG ở **discount** và đồng hướng Daily Bias bullish.
- Liquidity sweep xảy ra **trước** displacement và FVG.
- Entry quanh **CE** cải thiện R:R; giá respect CE thay vì xuyên thủng.
- Target là liquidity rõ (BSL), không phải TP tùy ý.

### Ví dụ sai / dễ nhầm — Long mọi bullish FVG giữa range
![[FVG-Example-Wrong.png]]

**Mô tả lỗi:**  
D1 bearish, giá đang ở premium / gần equilibrium. Trader thấy một bullish FVG nhỏ (nến giữa body trung bình, không phá cấu trúc rõ) và Long ngay vì "có FVG". Giá lấp FVG, đóng nến xuyên xuống (FVG invalid → chuyển thành bearish IFVG), rồi tiếp tục delivery xuống lấy SSL. Lệnh Long bị stop.

**Mô tả lỗi:**
- FVG không sinh ra từ displacement phá cấu trúc.
- FVG ngược Daily Bias và ở sai phía (premium) cho Long.
- Không có liquidity sweep trước đó; chưa chờ LTF confirmation.
- Trade FVG như tín hiệu độc lập thay vì điểm tham chiếu trong context.

**Bài học:**
- FVG là **điểm tham chiếu giá**, không phải tín hiệu trade độc lập.
- Không Long chỉ vì thấy bullish FVG; phải đúng bias + discount + sweep + displacement.
- Khi FVG bị đóng nến xuyên qua, nó **đảo cực (IFVG)** — đừng cố giữ lệnh ngược.

---
### Sequence mẫu — Long với Bullish FVG (BISI)
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Giá về Discount + bullish HTF POI
→ Sweep Sell-Side Liquidity
→ Displacement tăng phá cấu trúc (BOS/MSS) → tạo Bullish FVG (BISI)
→ Giá retrace về CE (50%) của FVG
→ M5/M1 bullish MSS + FVG nhỏ refined
→ Entry quanh CE; Stop dưới low FVG / dưới sweep low
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short với Bearish FVG (SIBI)
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Giá về Premium + bearish HTF POI
→ Sweep Buy-Side Liquidity
→ Displacement giảm phá cấu trúc (BOS/MSS) → tạo Bearish FVG (SIBI)
→ Giá retrace lên CE (50%) của FVG
→ M5/M1 bearish MSS + FVG nhỏ refined
→ Entry quanh CE; Stop trên high FVG / trên sweep high
→ Target: Internal liquidity trước, External SSL chính sau
```

### Sequence mẫu — Inversion FVG (IFVG)
```text
Bullish FVG cũ bị đóng nến XUYÊN XUỐNG (invalid)
→ Vùng FVG cũ đảo cực thành KHÁNG CỰ (bearish IFVG)
→ Đồng hướng bias bearish mới + MSS bearish
→ Giá retrace LÊN test lại vùng IFVG
→ Reject tại IFVG → Short
→ Stop trên đỉnh IFVG; Target SSL phía dưới
(Ngược lại cho bullish IFVG: bearish FVG fail → hỗ trợ → Long)
```

> [!note]
> Với ICT 2022 model, FVG có chất lượng không đến từ "thấy gap rồi vào", mà từ sequence: **HTF draw → retrace vào PD Array → liquidity sweep → displacement phá cấu trúc tạo FVG → entry quanh CE**. CE là điểm vào tối ưu giúp R:R đẹp hơn so với vào ở mép gap.

---

## 7. Kiến thức nâng cao (Advanced)

### 7.1. "Gia đình gap" — FVG không phải loại inefficiency duy nhất

Nhiều trader gọi mọi khoảng trống là "FVG" và trade chúng như nhau — đây là sai lầm phân loại. ICT có cả một **taxonomy của inefficiency**, mỗi loại có cấu trúc và cách dùng khác nhau:

![[FVG-Advanced-Gap-Taxonomy.svg|690]]

| Loại | Cấu trúc | Bản chất | Cách dùng thực chiến |
|---|---|---|---|
| **FVG (BISI/SIBI)** | Gap 3 nến: wick nến 1 và nến 3 không chạm nhau | Single-sided delivery do displacement | POI entry / draw; CE là mức chính |
| **Volume Imbalance** | Gap giữa **body** hai nến liên tiếp, nhưng wick chồng lấp | Inefficiency nhỏ giữa close/open | Mốc precision cho entry/target LTF; thường được rebalance nhanh — KHÔNG phải POI chính |
| **[[21 - Liquidity Void]]** | Cả một đoạn nhiều nến one-sided | Vùng thiếu giao dịch quy mô lớn, chứa nhiều FVG con | Draw mạnh; giá thường rebalance phần lớn void; bên trong void chọn FVG con làm mức |
| **[[03 - Balanced Price Range]] (BPR)** | Bullish FVG chồng lấp Bearish FVG | Vùng đã được giao dịch đủ **hai chiều** | S/R rất "cứng"; CE của BPR là mức phòng thủ; entry chất lượng cao khi retest |
| **[[14 - Implied Fair Value Gap]]** | Không có gap thật; đo bằng trung điểm wick nến 1 và nến 3 | "Gap ngầm" trong nến có wick dài | Dùng khi displacement không để lại gap thật; yếu hơn FVG thật |
| **[[06 - Breakaway Gap]]** | Gap sinh ra khi giá thoát khỏi accumulation/POI với intent cực mạnh | Gap KHÔNG có nhu cầu được lấp trong leg hiện tại | Không chờ lấp để entry — dấu hiệu trend rất mạnh; dùng làm bằng chứng bias |
| **[[23 - New Day Opening Gap]] / [[24 - New Week Opening Gap]]** | Gap giữa close phiên trước và open phiên sau | Reference gap của thuật toán theo thời gian | Mức tham chiếu draw/support-resistance trong ngày/tuần |

> [!important] Hệ quả quan trọng nhất của taxonomy
> **Không phải mọi gap đều "phải" được lấp.** Breakaway gap trong displacement thoát khỏi accumulation thường không được lấp trong cùng một leg. Kỳ vọng "gap nào cũng lấp" là lý do trader counter-trend bị nghiền trong trend mạnh. Câu hỏi đúng không phải "gap này có lấp không?" mà là "**gap này thuộc loại nào, và narrative có cần nó được lấp không?**"

### 7.2. Giải phẫu FVG: Proximal/Distal, Quadrants và độ sâu fill

![[FVG-Advanced-Quadrants.svg|646]]

**Proximal vs Distal edge.** Với một bullish FVG bên dưới giá: mép trên (gần giá) là **proximal edge**, mép dưới (xa giá) là **distal edge**. Mọi kế hoạch entry/stop nên gọi tên hai mép này thay vì "trên/dưới" mơ hồ — vì với bearish FVG thì đảo ngược.

**Quadrant theory.** Chia gap thành 4 phần (0–25–50–75–100%). Ứng dụng:
- Trong displacement **rất mạnh** (nhiều FVG xếp chồng, sweep rõ), giá thường chỉ nhúng tới **upper quadrant hoặc CE** của bullish FVG rồi bật — chờ distal sẽ lỡ tàu.
- Giá lấp tới **lower quadrant / distal** rồi mới bật = phản ứng yếu hơn → hạ kỳ vọng, bắt buộc có LTF MSS trước khi vào, hoặc bỏ.
- **Độ sâu fill là thông tin**, không chỉ là chuyện entry: chạm proximal rồi bay = demand/supply cực mạnh; cần lấp toàn bộ mới bật = sponsorship yếu dần.

**Ba cấp độ entry theo độ sâu:**

| Kiểu entry | Vị trí | Điều kiện cho phép | Trade-off |
|---|---|---|---|
| **Aggressive** | Limit tại proximal edge | Sweep rõ + displacement cực mạnh + FVG chồng OB | Win rate thấp hơn, R:R cao nhất, dễ dính chạm giả |
| **Standard** | Limit/market quanh CE | Điều kiện FVG chuẩn (checklist mục 8) | Mặc định — cân bằng nhất |
| **Conservative** | Sau khi giá reject CE + M1/M5 MSS xác nhận | FVG fill sâu, context kém chắc chắn | Win rate cao hơn, R:R giảm, có thể lỡ move |

**Stop loss:** luôn đặt ngoài **distal edge + buffer** (spread/vài tick) hoặc dưới sweep low — không đặt tại distal chính xác vì thuật toán hay quét đúng mép. Nếu stop hợp lệ khiến size quá lớn so với 0.5% risk → **giảm size, không bóp stop**.

### 7.3. FVG theo trục thời gian (Time & Price)

ICT nhấn mạnh **thời gian đứng trước giá**: cùng một cấu trúc FVG, giá trị hoàn toàn khác nhau tùy thời điểm hình thành.

- **FVG trong Kill Zone > ngoài Kill Zone.** FVG sinh trong London Open / NY AM ([[18 - Kill Zones]]) mang intent của thuật toán ở thời điểm delivery chính. FVG hình thành trong lunch (12:00–13:00 NY) hoặc cuối NY PM thường là nhiễu thanh khoản mỏng.
- **Macro windows.** Các cửa sổ macro (~9:50–10:10, 10:50–11:10, 13:10–13:40, 14:50–15:10 NY time) là lúc thuật toán chạy run-on-liquidity / rebalance. FVG hình thành hoặc được retest trong macro có xác suất phản ứng cao hơn rõ rệt — đặc biệt với NQ.
- **First Presented FVG (FPFVG).** FVG **đầu tiên** hình thành sau 9:30 open của index futures là anchor của NY AM session model: giá thường quay lại rebalance FPFVG trước khi chạy leg chính của phiên sáng. Kết hợp với Silver Bullet window (10:00–11:00: tìm FVG entry đầu tiên trong cửa sổ này) tạo thành playbook thời gian cụ thể cho NQ.
- **Tuổi của FVG.** LTF FVG (M1–M15) hết hạn nhanh — thường chỉ trong phiên; nếu qua ngày mà chưa được dùng, giá trị giảm mạnh. HTF FVG (H4/D1/W) giữ giá trị nhiều ngày tới nhiều tuần. FVG D1/W chưa lấp của tuần trước là draw tự nhiên cho tuần sau.
- **Số lần test.** Mỗi lần giá chạm vào FVG mà chưa xuyên, một phần lệnh trong đó được tiêu thụ → **first touch đáng tin nhất**, từ lần 3 trở đi coi như đã cạn.

### 7.4. Delivery state & chuỗi re-delivery

Đây là tầng hiểu sâu nhất về FVG: **BISI/SIBI không chỉ là "vùng" — chúng mô tả TRẠNG THÁI delivery của thị trường.**

- Một BISI đang được respect nghĩa là thị trường đang ở trạng thái **buy-side delivery** (dòng chào giá lên). Khi giá trade through BISI và đóng nến dưới nó, trạng thái flip sang **sell-side delivery** — và vùng đó trở thành IFVG. Inversion không phải "pattern", nó là **bằng chứng đổi trạng thái delivery**.
- **Chuỗi re-delivery trong trend:** một trend giảm sạch sẽ vận hành theo chu kỳ `tạo SIBI → retrace rebalance SIBI (chạm CE) → expansion xuống tạo SIBI mới → lặp lại`. Trade trend = trade chuỗi rebalance các SIBI liên tiếp; SIBI **mới nhất** (gần giá nhất) được respect trước.
- **Stacked FVGs:** một leg để lại 2–3 FVG cùng hướng xếp chồng = institutional sponsorship mạnh; ưu tiên FVG gần nhất làm entry, các FVG sâu hơn làm phòng tuyến dự phòng.
- **Leg không để lại FVG nào** = thiếu displacement/intent → nhiều khả năng đó là retracement (corrective) chứ không phải impulse. Đây là cách dùng FVG để **đọc cấu trúc**, không chỉ để entry: leg nào có FVG là leg có chủ đích.

### 7.5. Best Practices — FVG

> [!success] Best Practices
> 1. **Chấm điểm trước khi trade.** Mỗi FVG được chấm theo 5 tiêu chí: (1) sinh từ displacement phá BOS/MSS, (2) tại/trùng POI HTF, (3) đúng premium/discount, (4) sau liquidity sweep, (5) còn unmitigated. **Chỉ trade FVG đạt 4/5 trở lên.**
> 2. **Chọn trước, không vẽ đuổi.** Đánh dấu tối đa 2–3 FVG "đáng theo dõi" từ pre-market. FVG vẽ mới trong lúc giá đang chạy = quyết định FOMO, chất lượng thấp.
> 3. **Confluence thay số lượng.** FVG chồng OB (fair value area), CE trùng OTE/equilibrium, FVG nằm trong HTF FVG — một setup confluence đáng giá hơn năm setup đơn lẻ.
> 4. **Entry mặc định tại CE.** Aggressive tại proximal chỉ khi displacement cực mạnh và sweep rõ; conservative khi fill sâu. Ghi `entry_relative_to_ce` vào journal để backtest.
> 5. **Invalidation đúng timeframe.** FVG H1 cần **H1 đóng nến** xuyên distal mới invalid — một cây M1 xuyên qua không có ý nghĩa. Sai timeframe khi đánh giá invalidation là nguồn thoát non/gồng sai phổ biến nhất.
> 6. **Tôn trọng thời gian.** Ưu tiên FVG hình thành/retest trong kill zone và macro window; với NQ chú ý FPFVG sau 9:30 và Silver Bullet 10:00–11:00.
> 7. **Log để kiểm chứng.** Thêm vào frontmatter trade: `fvg_from_displacement`, `entry_relative_to_ce` (proximal/CE/distal), `fill_depth`, `in_killzone`, `fvg_age` — sau 30+ mẫu mới đủ dữ liệu chỉnh rule.
> 8. **Một FVG fail là dữ liệu, không phải thất bại.** Khi FVG bị xuyên, việc đầu tiên là đánh dấu IFVG và hỏi "delivery state đã flip chưa?" — thay vì tìm FVG khác cùng hướng để "gỡ".

---

## Tình huống thực chiến (War Stories)

> [!info] Vì sao có mục này
> Checklist ở mục 8 lọc FVG *xấu*. Mục này dành cho những FVG **pass toàn bộ checklist** nhưng vẫn thất bại — vì các biến mà lý thuyết chuẩn không đặt tên: chất liệu của nến tạo gap, tốc độ giá tiếp cận gap, lịch sử chạm ngoài phiên của mình, và microstructure của chính công cụ đang trade.

### W0. Tầng WHY nền tảng — vì sao giá "phải" quay lại một cái gap?

"Thị trường quay lại lấp imbalance" nghe như tín điều. Ba cơ chế biến nó thành logic — và phân xử luôn gap nào lấp, gap nào không:

1. **Gap = quãng giá KHÔNG AI KỊP GIAO DỊCH — và các lệnh bị bỏ lại vẫn còn sống.** Khi displacement kéo giá qua một vùng quá nhanh, các lệnh limit mua/bán đặt sẵn trong vùng đó **không được khớp** (giá nhảy qua). Các tổ chức đặt lệnh đó không hủy kế hoạch — lệnh của họ vẫn nằm trong sổ, tại đúng các mức giá bên trong gap. Giá quay lại FVG không phải vì "thị trường công bằng", mà vì **về đó còn thanh khoản chờ sẵn để khớp nốt phần việc dang dở** — với bên đã đẩy giá, đó là nơi rẻ nhất để mua thêm/xả bớt tồn kho. FVG là POI vì nó là *kho lệnh chưa dùng*.
2. **Vì sao CE (50%) hoạt động? Vì nó là điểm cân bằng chi phí của chính bên tạo gap.** Bên khởi xướng displacement có giá vốn trung bình quanh nửa dưới của leg. Cho phép giá retrace *qua* CE của gap do chính mình tạo nghĩa là để vị thế chìm về vùng vốn — mất lợi thế đã trả tiền mua. Vì vậy lớp phòng thủ tự nhiên (mua thêm để chặn) tập trung từ CE trở xuống proximal. CE bị đóng thân xuyên qua đồng nghĩa **bên tạo gap đã bỏ vị thế hoặc bị nuốt** — đó là lý do inversion (IFVG) là bằng chứng đổi delivery chứ không phải pattern trang trí.
3. **Vì sao có gap KHÔNG lấp (breakaway)? Vì không còn tồn kho nào cần cân.** Nếu displacement khởi phát từ một accumulation đã hoàn tất (mọi lệnh đã gom đủ trước đó), bên khởi xướng **không cần quay lại mua thêm** — không có lệnh dang dở trong gap, không có lý do kinh tế nào để redeliver. Câu hỏi "gap này có lấp không?" vì thế quy về: **"bên tạo gap còn việc chưa xong ở đó không?"** — trả lời bằng bối cảnh (gap thoát khỏi POI sau sweep = breakaway; gap giữa leg đang chạy = kho lệnh còn dùng).

Ba cơ chế này chạy xuyên các W bên dưới: news gap không có kho lệnh nào bên trong (W1); grind vào gap = kho lệnh bị rút dần trước khi giá tới (W2); cú chạm ngoài phiên đã tiêu một phần kho (W3).

### W1. FVG sinh từ news candle — cùng hình dạng, khác hẳn "chất liệu"

![[FVG-War-News-Candle-FVG.svg|720]]
*Sơ đồ: FVG từ displacement có cấu trúc được respect tại CE; FVG từ spike CPI/NFP là vùng chân không — giá cắt xuyên không phản ứng.*

**Sách giáo khoa nói:** gap 3 nến + nến giữa displacement = FVG hợp lệ.

**Thực tế phát hiện:** nến 8:30 CPI/NFP thỏa mọi tiêu chí hình học — body khổng lồ, phá cấu trúc, gap rộng. Nhưng gap đó in ra trong lúc **spread giãn và quote gần như đóng băng**: không có chuỗi lệnh thuật toán thật sự được khớp tại các mức giá bên trong gap. Nó là *vết nhảy* của giá, không phải *dấu vết* của lệnh. Hệ quả: không ai có position cần phòng thủ tại CE của nó → khi giá quay lại, vùng này bị cắt xuyên với tần suất cao hơn hẳn FVG cùng kích thước sinh trong kill zone không có tin.

**Rule đo được:**
- FVG sinh trong ±2 phút quanh high-impact news → gắn nhãn riêng, **mặc định không dùng làm POI entry**.
- Nó chỉ "tốt nghiệp" thành POI khi giá **re-deliver** qua vùng đó lần nữa bằng displacement có cấu trúc (sweep đứng trước, không có tin) — lúc đó vẽ lại theo leg mới.
- Journal: `fvg_origin` (killzone_algo / news_spike / thin_liquidity). Sau 30 mẫu, so respect-rate tại CE giữa các nhóm — chênh lệch thường đủ lớn để tự nó thành rule.

### W2. Tốc độ tiếp cận FVG — "rơi nhanh chạm bật" vs "bò từ từ vào"

![[FVG-War-Approach-Speed.svg|720]]
*Sơ đồ: fast tap (rebalance chuẩn — giữ plan) vs slow grind bậc thang (hấp thụ — rút limit, đòi LTF MSS).*

**Sách giáo khoa nói:** chờ giá retrace về CE rồi entry.

**Thực tế phát hiện sau nhiều lần bị xuyên limit:** *cách* giá đi vào FVG dự báo kết quả tốt hơn cả chất lượng của chính FVG. Hai chế độ:
- **Fast tap:** 2–4 nến dốc rơi thẳng vào gap, chạm CE, bật ra trong 1–2 nến. Đây là hành vi rebalance — thuật toán quay lại "lấy nốt hàng" ở giá tốt rồi tiếp tục. Limit tại CE hoạt động đúng thiết kế.
- **Slow grind:** chuỗi nến nhỏ bậc thang gặm dần vào gap, mỗi nến một chút, không có nỗ lực đẩy ra. Đây là hành vi **hấp thụ**: lệnh nằm trong gap đang bị tiêu hoá dần bởi một dòng lệnh kiên nhẫn ngược hướng. Khi giá tới CE thì phòng tuyến đã mỏng — xuyên thủng là kết cục phổ biến.

**Rule đo được:**
- Giá tiếp cận FVG bằng grind (nhiều hơn ~5–6 nến LTF liên tiếp cùng hướng, body nhỏ, không có displacement ngược nào xen giữa) → **rút limit order**, chuyển sang chế độ "chỉ vào nếu có LTF MSS trong gap".
- Journal: `approach_speed` (fast_tap / grind) — biến này kết hợp với `entry_relative_to_ce` là cặp thống kê giá trị nhất về FVG.

### W3. "First touch" giả — cú chạm thật đã xảy ra ngoài phiên của bạn

**Tình huống:** bạn đánh dấu một H1 FVG chưa mitigate từ hôm qua, sáng nay giá quay về, bạn coi là first touch (đáng tin nhất). Lệnh fail. Mở M5 xem lại: **lúc 3 giờ sáng giờ mình ngủ**, giá đã wick vào gap một lần trong phiên Á thanh khoản mỏng. Trên H1 wick đó gần như vô hình (nằm trong bóng một nến dài), nhưng phần lệnh trong gap đã bị tiêu thụ một phần — cú chạm của bạn thực chất là **lần chạm thứ hai**.

**Rule đo được:**
- Trước khi tin một "first touch": thả xuống M5/M15 và **tua lại toàn bộ lịch sử giá từ lúc FVG hình thành** — đếm số lần wick đã vào gap, kể cả ngoài phiên. Mất 60 giây, cứu nhiều lệnh.
- Journal: `touch_count_actual` (đếm trên LTF, không phải trên khung đang trade).

### W4. CE là "luật" trên NQ nhưng chỉ là "gợi ý" trên EURUSD — hiệu chỉnh theo từng công cụ

**Tình huống:** cùng một playbook FVG, backtest trên NQ cho thấy giá respect CE rất sạch (chạm 50%, bật); mang nguyên sang EURUSD thì liên tục "thua oan" — giá thường xuyên fill sâu 75–100% gap, thậm chí wick qua distal vài pip rồi mới đảo. Không phải model sai — **độ sâu fill điển hình là thuộc tính riêng của từng thị trường** (độ dày thanh khoản, tick size, mức độ tham gia của thuật toán CME vs interbank khác nhau).

**Rule đo được:**
- Không dùng chung một quy tắc entry-depth cho mọi market. Thống kê `fill_depth` **theo từng symbol** trong backtest (NQ riêng, EURUSD riêng, XAUUSD riêng) rồi mới đặt rule entry/stop cho từng cái.
- Với market hay fill sâu: entry mặc định dời từ CE xuống lower quadrant, hoặc luôn đòi LTF MSS; stop buffer sau distal cũng phải rộng hơn (đặc biệt XAUUSD).
- Đây là ứng dụng trực tiếp của nguyên tắc trong [[04 - Backtesting]]: dữ liệu của chính mình trên chính market đó là trọng tài, không phải video ICT quay trên ES.

### W5. Limit tại mép FVG không khớp — vì chart của bạn là bid-chart

**Tình huống (FX/CFD):** bạn đặt sell limit tại proximal edge của một bearish FVG trên EURUSD/XAUUSD. Giá "chạm đúng mép" trên chart rồi rơi thẳng — nhưng lệnh không khớp, hoặc khớp trong backtest mà không bao giờ khớp live. Lý do: **chart vẽ giá bid**, trong khi sell limit khớp theo bid nhưng cú chạm bạn thấy có thể chỉ là ask chạm (hoặc ngược lại với buy limit — ask đã chạm mức từ trước khi chart hiển thị). Trên gold spread 20–40 cent, sai số này nuốt trọn những cú "chạm mép rồi bay".

**Rule đo được:**
- Entry mặc định tại **CE thay vì mép** — vừa cải thiện R:R vừa tạo buffer tự nhiên cho spread.
- Nếu vẫn muốn mép: cộng/trừ spread trung bình của phiên vào giá limit (buy limit đặt cao hơn mép một spread; sell limit thấp hơn một spread).
- Backtest phải mô phỏng spread — mọi entry "khớp đúng đỉnh wick chạm mép" cần bị nghi ngờ là phantom fill (cùng họ với bài học W3 bên [[20 - Liquidity Sweep]]).

> [!success] Tổng kết mục War Stories
> Một FVG không chỉ có *hình dạng* — nó có **chất liệu** (nến gì tạo ra nó — W1), **cách bị tiếp cận** (W2), **lịch sử chạm thật** (W3), **quốc tịch** (market nào — W4) và **cơ chế khớp lệnh** quanh nó (W5). Journal fields: `fvg_origin`, `approach_speed`, `touch_count_actual`, `fill_depth` theo symbol.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> FVG chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**. KHÔNG trade mọi FVG.

### A. Context (HTF)
- [ ] Daily Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] FVG đồng hướng bias, không phải FVG ngược.
- [ ] FVG nằm đúng premium (Short) / discount (Long) của HTF dealing range.
- [ ] FVG nằm tại / trùng một POI HTF có ý nghĩa.
- [ ] Có draw on liquidity rõ ràng làm target.
- [ ] FVG sinh ra từ displacement phá cấu trúc, không phải gap giữa range.
- [ ] Xác định mức CE (50%) và level invalidation của FVG.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã vào vùng FVG đúng premium/discount cho hướng trade.
- [ ] Đã có liquidity sweep hợp lý TRƯỚC khi displacement tạo FVG.
- [ ] Giá respect CE / mép FVG (reject), không đóng nến xuyên qua.
- [ ] Có LTF MSS + displacement xác nhận khi giá vào FVG.
- [ ] Entry quanh CE, không chase ở mép xa.
- [ ] Stop loss logic: ngoài đầu kia FVG / ngoài điểm sweep.
- [ ] Target là liquidity rõ; đường tới target không bị FVG/imbalance cản trở chưa xử lý.
- [ ] R:R tối thiểu đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] FVG không sinh ra từ displacement → không trade.
- [ ] FVG ngược bias / sai premium-discount → không trade.
- [ ] Chưa có liquidity sweep → không trade.
- [ ] FVG đã bị đóng nến xuyên qua (invalid) → không trade (trừ kế hoạch IFVG riêng).
- [ ] FVG giữa range / không có POI HTF → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade mọi FVG | Vẽ FVG khắp chart, vào lệnh ở bất kỳ gap nào | Phần lớn FVG là nhiễu, không có edge | Chỉ trade FVG tại POI HTF + đúng bias + sau sweep |
| FVG không có displacement | Nến giữa body nhỏ, không phá cấu trúc | Không phản ánh intent, dễ bị xuyên qua | Yêu cầu displacement phá BOS/MSS mới tính FVG chất lượng |
| Bỏ qua premium/discount | Long ở FVG premium, Short ở FVG discount | Entry trở thành chase, R:R xấu | Long chỉ ở FVG discount, Short chỉ ở FVG premium |
| Vào trước liquidity sweep | Giá chưa quét đỉnh/đáy đã entry tại FVG | Stop nằm đúng nơi market còn muốn quét | Chờ sweep → displacement → FVG, đúng thứ tự |
| Nhầm fill với invalidation | Coi giá lấp FVG là "fail" và thoát sớm | Lấp tới CE/full fill có thể vẫn respect | Phân biệt respect (reject) vs đóng nến xuyên qua (invalid) |
| Bỏ qua CE | Entry ở mép xa gap, không dùng 50% | R:R kém; bỏ lỡ mức phản ứng quan trọng nhất | Ưu tiên entry quanh CE; coi CE là mức xác nhận |
| Không nhận ra IFVG | FVG bị xuyên rồi vẫn cố giữ lệnh ngược | FVG fail đảo cực thành S/R ngược hướng | Khi FVG bị đóng nến xuyên qua, đảo tư duy sang IFVG |
| Trade FVG ngược bias | Bullish FVG đẹp nhưng HTF bearish | Target ngược hướng thiếu room, xác suất thấp | Chỉ trade FVG đồng hướng Daily Bias |
| Chọn sai FVG khi chồng chéo | Nhiều FVG gần nhau, vào đại một cái | Mức tham chiếu mơ hồ, stop/target không logic | Chọn FVG trùng POI HTF / có confluence rõ nhất |
| Chase FVG sau expansion lớn | Vào FVG hình thành cuối một leg đã chạy xa | Phần lớn range đã tiêu thụ, dễ retrace | Chờ FVG tại POI HTF mới hoặc bỏ qua |

---

## 10. Câu hỏi tự kiểm tra

- Mình có giải thích được FVG (BISI/SIBI) và cấu trúc 3 nến trong 30 giây không?
- FVG này sinh ra từ displacement phá cấu trúc hay chỉ là gap giữa range?
- Mức CE (50%) của FVG nằm ở đâu? Giá đang respect hay xuyên qua nó?
- FVG đang ở premium hay discount của **dealing range nào**?
- Liquidity đã bị sweep trước khi FVG hình thành chưa?
- FVG đang đóng vai POI để entry hay DRAW để làm target?
- Điều gì làm FVG này invalid, và nếu invalid thì IFVG sẽ ở đâu?
- FVG này có đồng hướng Daily Bias không?
- Nếu mình không trade FVG này, lý do "No Trade" là gì?
- Setup nào trong trade journal đã dùng FVG đúng/sai context?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Fair Value Gap được tạo bởi mấy nến, và bullish FVG nằm ở đâu?  
**Đáp:** 3 nến. Bullish FVG (BISI) là khoảng trống giữa HIGH của nến 1 và LOW của nến 3, với nến 2 là displacement tăng mạnh (single-sided delivery).

### Q2
**Hỏi:** BISI và SIBI nghĩa là gì?  
**Đáp:** BISI = Buyside Imbalance Sellside Inefficiency (bullish FVG). SIBI = Sellside Imbalance Buyside Inefficiency (bearish FVG).

### Q3
**Hỏi:** CE (Consequent Encroachment) là gì và vì sao quan trọng?  
**Đáp:** CE là mức 50% của gap — mức phản ứng quan trọng nhất. Giá thường tôn trọng CE; entry tối ưu thường nằm quanh CE và CE dùng để xác nhận FVG đang được respect.

### Q4
**Hỏi:** FVG đóng vai trò kép nào trong ICT?  
**Đáp:** (1) POI để vào lệnh khi giá retrace về FVG; (2) DRAW — giá bị hút về để lấp/rebalance imbalance còn mở.

### Q5
**Hỏi:** Inversion FVG (IFVG) là gì?  
**Đáp:** Khi một FVG bị giá đóng nến xuyên thủng qua, nó đảo cực tính: bullish FVG fail → thành kháng cự bearish; bearish FVG fail → thành hỗ trợ bullish.

### Q6
**Hỏi:** Điều gì phân biệt một FVG chất lượng cao với một FVG yếu?  
**Đáp:** FVG tốt sinh ra từ displacement PHÁ CẤU TRÚC (BOS/MSS) có chủ đích, nằm tại POI HTF, đúng premium/discount, đồng hướng bias và sau liquidity sweep. FVG nhỏ giữa range, không displacement = yếu.

### Q7
**Hỏi:** Phân biệt "respect" và "invalidation" của một FVG?  
**Đáp:** Respect = giá chạm CE / mép gap rồi reject (kể cả full fill rồi quay đầu). Invalidation = giá đóng nến xuyên qua và giữ giá ngoài FVG → FVG hết hiệu lực, có thể đảo thành IFVG.

### Q8
**Hỏi:** Tại sao KHÔNG nên trade mọi FVG?  
**Đáp:** Phần lớn FVG là nhiễu giữa range, không có edge. Chỉ FVG tại POI HTF, đúng context bias, đúng premium/discount và sau sweep mới có xác suất cao.

---

## 12. Lesson Learned

### Bài học chính
- FVG là **điểm tham chiếu giá / price inefficiency**, không phải tín hiệu trade độc lập.
- FVG chất lượng phải có **intent**: sinh ra từ displacement phá cấu trúc, không phải gap ngẫu nhiên.
- **CE (50%)** là mức quan trọng nhất: entry quanh CE cải thiện R:R và là mức để đo respect/invalidation.
- FVG có vai trò kép — biết rõ mình đang dùng nó làm **POI để entry** hay **DRAW để target**.
- Khi FVG bị đóng nến xuyên qua, nó **đảo cực thành IFVG** — đừng cố giữ lệnh ngược.
- Không trade mọi FVG; chỉ FVG đúng bias + premium/discount + sau sweep mới đáng vào.

### Quy tắc cá nhân rút ra
- [ ] Tôi không gọi một gap là "FVG đáng trade" nếu nến giữa không phải displacement phá cấu trúc.
- [ ] Tôi chỉ Long ở FVG discount và Short ở FVG premium, đồng hướng Daily Bias.
- [ ] Tôi luôn chờ liquidity sweep TRƯỚC khi vào lệnh tại FVG.
- [ ] Tôi ưu tiên entry quanh CE và đặt stop ngoài đầu kia của FVG / ngoài điểm sweep.
- [ ] Khi FVG bị đóng nến xuyên qua, tôi chuyển tư duy sang IFVG thay vì cố giữ lệnh cũ.
- [ ] Khi nhiều FVG chồng chéo, tôi chỉ chọn cái trùng POI HTF / có confluence rõ nhất.

### Câu nhắc nhở khi trade
> **"FVG không phải là lệnh — nó là nơi tôi chờ. Chỉ vào khi displacement có chủ đích, đúng premium/discount, sau sweep, và giá respect CE."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt BISI/SIBI, CE, và vai trò POI vs DRAW không? |
| Nhận diện trên chart |  | Có xác định đúng 3 nến, gap thật và mức CE không? |
| Biết khi nào bỏ qua |  | Có dám bỏ FVG giữa range / không displacement / ngược bias không? |
| Kết hợp với context HTF |  | FVG có được đặt trong narrative bias + premium/discount + sweep không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra quanh CE sau sweep + displacement không? |
| Review sau trade |  | Có kiểm tra chất lượng FVG bằng dữ liệu journal thay vì cảm xúc không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Fair Value Gap]]`.
- [ ] Review riêng: FVG có displacement vs không; entry tại CE vs mép gap; FVG sau sweep vs trước sweep.
- [ ] Thống kê win rate, average R, lỗi lặp lại theo `fvg_from_displacement` và `entry_relative_to_ce`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.
