---
type: ict-concept
concept: Premium / Discount
aliases:
  - Premium Discount
  - Premium/Discount
  - PD Array
  - Equilibrium
tags:
  - trading/ict/concept
  - trading/study
  - "#Premium"
  - "#Discount"
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
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-06-22
common_mistakes:
  - "[[Mistake - Buy in Premium / Sell in Discount]]"
  - "[[Mistake - Wrong Dealing Range]]"
  - "[[Mistake - Chase After Expansion]]"
---

# Premium / Discount

> [!summary] Tóm tắt 1 câu
> **Premium/Discount đo VỊ TRÍ của giá so với equilibrium (mức 50%) của một dealing range bằng Fibonacci: Discount (dưới 50%) là vùng giá "rẻ" để tìm MUA, Premium (trên 50%) là vùng giá "đắt" để tìm BÁN, còn Equilibrium (50%) là vùng trung lập/ra quyết định.**

> [!important] Nguyên tắc cốt lõi
> **Mua ở Discount, Bán ở Premium — nhưng CHỈ khi đồng hướng Daily Bias VÀ tại một PD Array hợp lệ.**  
> Premium/Discount là một bộ lọc VỊ TRÍ, không phải tín hiệu vào lệnh độc lập; nếu chọn sai dealing range thì toàn bộ premium/discount đều vô nghĩa.

---

## 1. Định nghĩa

**Khái niệm:**  
Premium/Discount là cách ICT xác định **giá hiện tại đang "đắt" hay "rẻ"** so với một dealing range cụ thể. Lấy một range rõ ràng (swing low → swing high), chia bằng Fibonacci, lấy mức 50% làm **equilibrium (EQ)**:
- **Discount** = phần dưới 50% của range → giá đang "rẻ" → đây là vùng đi tìm cơ hội **MUA**.
- **Premium** = phần trên 50% của range → giá đang "đắt" → đây là vùng đi tìm cơ hội **BÁN**.
- **Equilibrium (50%)** = mốc cân bằng/trung lập, là vùng **ra quyết định**: dưới EQ ưu tiên long setup, trên EQ ưu tiên short setup theo bias.

Đây là tư duy "mua rẻ, bán đắt" được định lượng bằng range cụ thể, thay vì cảm tính.

**Mục đích trong ICT:**  
- Tránh mua ở đỉnh (premium) và bán ở đáy (discount) — lỗi tâm lý phổ biến của FOMO/chase.
- Lọc vị trí entry: chỉ tìm Long khi giá ở discount, chỉ tìm Short khi giá ở premium.
- Kết hợp với PD Array để biết **mảng giá nào ở vùng nào** thì đáng tin hơn (bullish OB ở discount đáng tin hơn bullish OB ở premium).
- Định lượng vùng OTE (0.62–0.79) để có entry với R:R tối ưu.

**Vì sao khái niệm này quan trọng:**  
ICT 2022 model chỉ có edge khi entry nằm đúng **vị trí giá trị**. Một bullish FVG hoàn hảo ở premium thường là cái bẫy, còn cùng FVG đó ở discount lại là cơ hội. Premium/Discount giúp tránh entry tại vùng giá kém lợi thế, nơi stop loss buộc phải rộng và room tới target bị thu hẹp.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đang "đắt" hay "rẻ" so với range tôi đang giao dịch?
- Tôi nên đi tìm Long hay Short ở vị trí hiện tại?
- POI này nằm ở vùng giá hợp lý (discount cho Long / premium cho Short) hay không?
- Tôi có đang chase sau khi giá đã chạy xa khỏi equilibrium không?
- Entry này có rơi vào vùng OTE (0.62–0.79) không?

### Premium / Discount không phải là gì
- Không phải tín hiệu vào lệnh: discount không có nghĩa "mua ngay", premium không có nghĩa "bán ngay".
- Không phải chỉ báo độc lập; nó vô nghĩa nếu dealing range bị chọn sai.
- Không phải lý do bỏ qua Daily Bias: discount chỉ đáng mua khi bias là Bullish.
- Không phải mức hỗ trợ/kháng cự cứng — nó là **vùng vị trí tương đối** trong range.
- Không phải Fibonacci để "đoán" mức retrace; ICT dùng nó để phân loại vùng giá, không phải để dự báo điểm dừng.

---

## 2. Bối cảnh sử dụng

### Ba vùng vị trí cần phân biệt

| Vùng | Khoảng Fib | Ý nghĩa thực chiến | Hành động ưu tiên |
|---|---|---|---|
| **Discount** | 0.0 → dưới 0.5 | Giá "rẻ" so với range; lợi thế thuộc về bên mua | Nếu bias Bullish: tìm **Long** tại bullish PD Array (bullish OB/FVG, mitigation block, old low/SSL) |
| **Equilibrium** | quanh 0.5 | Trung lập, vùng quyết định; chưa đắt chưa rẻ | Đứng ngoài hoặc chờ; trên EQ nghiêng short, dưới EQ nghiêng long — chỉ theo bias |
| **Premium** | trên 0.5 → 1.0 | Giá "đắt" so với range; lợi thế thuộc về bên bán | Nếu bias Bearish: tìm **Short** tại bearish PD Array (bearish OB/FVG, rejection block, old high/BSL) |

> [!tip]
> **Equilibrium là vùng ra quyết định, không phải vùng entry.** Trade ngay tại 50% thường là trade giữa range với R:R xấu. Hãy để giá đi sâu hơn vào premium (cho Short) hoặc discount (cho Long) tới một PD Array hợp lệ rồi mới execution.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có một **dealing range rõ ràng và hợp lệ** (xác định bằng swing tạo displacement/BOS — xem [[12 - Dealing Range]]).
- [ ] Đã có Daily Bias rõ ràng để biết nên dùng discount hay premium ([[12 - Daily Bias]]).
- [ ] Giá đang ở discount khi bias Bullish, hoặc ở premium khi bias Bearish (đồng hướng).
- [ ] Vùng premium/discount trùng với một PD Array hợp lệ (bullish OB/FVG ở discount, bearish OB/FVG ở premium).
- [ ] Vùng entry rơi vào OTE (0.62–0.79) của leg đang giao dịch ([[Optimal Trade Entry]]).
- [ ] Có liquidity pool rõ phía bên kia EQ để làm target (BSL phía trên cho Long, SSL phía dưới cho Short).

### Khi nào nên bỏ qua?
- [ ] Dealing range không rõ hoặc chọn sai → premium/discount sai theo.
- [ ] Giá đang ở equilibrium / quanh 50% → vùng trung lập, không có lợi thế.
- [ ] Giá ở premium nhưng bias Bullish (hoặc discount nhưng bias Bearish) → ngược logic vị trí.
- [ ] Giá đã chạy xa khỏi EQ theo hướng bias → vào lệnh lúc này là chase, không phải mua rẻ/bán đắt.
- [ ] Không có PD Array hợp lệ ở vùng premium/discount → chỉ có vị trí đẹp nhưng không có POI để vào.
- [ ] Range quá lớn so với khung trade khiến "discount" vẫn cách giá hàng trăm pip không thực dụng.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Xác định dealing range trước:** chọn swing low và swing high hợp lệ (có displacement/BOS), KHÔNG dùng swing quá nhỏ hay quá cũ.
2. **Vẽ Fibonacci đúng chiều:** với bullish leg, vẽ từ **swing low → swing high**; với bearish leg, vẽ từ **swing high → swing low**.
3. **Đọc mốc 50% (EQ):** mọi thứ dưới EQ là discount, mọi thứ trên EQ là premium.
4. **Đối chiếu PD Array:** xem mảng giá nào (OB, FVG, breaker...) nằm ở phía premium hay discount để xếp hạng độ tin cậy.
5. **Khoanh vùng OTE:** vùng 0.62–0.79 là nơi entry tối ưu nếu nó trùng PD Array hợp lệ.

### Cài đặt Fibonacci theo ICT

| Mức Fib | Vai trò |
|---|---|
| **0.0** | Đầu range (swing extreme nơi bắt đầu leg) |
| **0.5 (EQ)** | Equilibrium — ranh giới premium/discount, vùng trung lập |
| **0.62** | Mép trên vùng OTE |
| **0.705** | Tâm vùng OTE (mức "sweet spot") |
| **0.79** | Mép dưới vùng OTE |
| **1.0** | Cuối range (swing extreme đối diện) |

> [!note]
> Vùng **0.62–0.79 là OTE (Optimal Trade Entry)** — vùng retrace sâu trong discount (cho Long) hoặc premium (cho Short) cho R:R tốt nhất. Premium/Discount cho biết "phía nào để tìm lệnh"; OTE tinh chỉnh "vùng giá cụ thể để vào". Xem [[Optimal Trade Entry]].

### Phân loại PD Array theo vị trí

| Discount Array (vùng tìm MUA) | Premium Array (vùng tìm BÁN) |
|---|---|
| Bullish Order Block | Bearish Order Block |
| Bullish Fair Value Gap | Bearish Fair Value Gap |
| Mitigation Block (hỗ trợ Long) | Rejection Block (hỗ trợ Short) |
| Old Low / Sell-Side Liquidity (SSL) | Old High / Buy-Side Liquidity (BSL) |
| Bullish Breaker | Bearish Breaker |
| Liquidity Void cần được lấp lên | Liquidity Void cần được lấp xuống |

> [!abstract]
> PD Array được xếp hạng từ **premium (trên cùng, để bán)** xuống **discount (dưới cùng, để mua)**. Một mảng giá cùng loại sẽ đáng tin hơn nhiều khi nó nằm đúng phía: bullish OB ở discount > bullish OB ở premium.

### Điều kiện bắt buộc
- [ ] Có dealing range hợp lệ và được vẽ Fibonacci đúng chiều.
- [ ] Xác định rõ giá đang ở discount, premium hay equilibrium.
- [ ] Vị trí phù hợp với Daily Bias (discount + Bullish, hoặc premium + Bearish).
- [ ] Có PD Array hợp lệ tại vùng premium/discount đó để làm POI.

### Điều kiện tăng xác suất
- [ ] Vùng entry rơi vào OTE (0.62–0.79).
- [ ] Premium/discount trùng với HTF PD Array (ví dụ H1 discount trùng H4 bullish FVG).
- [ ] Có liquidity sweep tại vùng cực trị của range trước khi phản ứng ([[20 - Liquidity Sweep]]).
- [ ] Có displacement + MSS trong vùng premium/discount sau khi giá chạm POI ([[21 - Market Structure Shift]]).
- [ ] Có target liquidity rõ ở phía bên kia EQ cho đủ room R:R.

### Điều kiện làm setup yếu đi
- Range chọn từ swing không có displacement/BOS → EQ đặt sai chỗ.
- Giá chỉ chạm equilibrium rồi entry — chưa đủ "rẻ"/"đắt".
- Premium/discount đúng nhưng không có PD Array nào ở đó.
- Đã có nhiều lần test vùng đó khiến PD Array bị mitigate cạn.
- Range quá lớn/quá cũ khiến vị trí premium/discount không còn liên quan tới price delivery hiện tại.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình bắt buộc trước khi dùng premium/discount
> 1. **Dealing range nào tôi đang đo?** (đầu range ở đâu, hợp lệ không?)
> 2. **Giá đang ở premium, discount hay equilibrium của range đó?**
> 3. **Vị trí này có đồng hướng Daily Bias không?**
> 4. **Có PD Array hợp lệ tại vùng premium/discount để vào không?**

### D1 / H4 — Bias & Narrative
- **Daily Bias:** Bullish / Bearish / Neutral (quyết định dùng discount hay premium).
- **HTF dealing range:** đánh dấu swing low → swing high (hoặc ngược lại) tạo displacement/BOS đáng kể.
- **Giá đang ở Premium hay Discount của HTF range?** ghi rõ % nếu được.
- **HTF PD Array đang được kích hoạt:** bullish/bearish OB, FVG, breaker nằm ở vùng nào của range.
- **Draw on liquidity:** BSL phía trên (cho Long) hay SSL phía dưới (cho Short).

```text
Mẫu ghi nhanh — Long từ Discount
HTF dealing range: [swing low] → [swing high]  (vẽ Fib low→high)
Location: Discount (< 0.5) — đang ở vùng OTE 0.62–0.79
Bias: Bullish — discount đồng hướng → tìm Long
PD Array tại discount: bullish H1 FVG / bullish OB
Draw on liquidity: BSL tại [level] (phía trên EQ)
Invalidation: giá đóng nến chấp nhận dưới đáy range (range bị phá → đổi narrative)
```

```text
Mẫu ghi nhanh — Short từ Premium
HTF dealing range: [swing high] → [swing low]  (vẽ Fib high→low)
Location: Premium (> 0.5) — đang ở vùng OTE 0.62–0.79
Bias: Bearish — premium đồng hướng → tìm Short
PD Array tại premium: bearish H1 FVG / bearish OB / rejection block
Draw on liquidity: SSL tại [level] (phía dưới EQ)
Invalidation: giá đóng nến chấp nhận trên đỉnh range (range bị phá → đổi narrative)
```

### H1 / M15 — POI & Context
- **POI đang quan sát có nằm đúng phía premium/discount không?** Bullish POI phải ở discount, bearish POI phải ở premium.
- **Đo lại premium/discount theo dealing range của chính khung này** nếu cần entry tinh hơn — đừng dùng Fib từ range khác.
- **Giá đã sweep liquidity tại cực trị range chưa?** Sweep SSL ở discount (cho Long) hoặc BSL ở premium (cho Short) củng cố reaction.
- **Vùng OTE H1/M15 có trùng PD Array không?** trùng càng nhiều confluence càng tốt.

### M5 / M1 — Confirmation & Entry
- **Giá đã vào đúng vùng premium/discount của HTF chưa?** nếu chưa, chưa execution.
- **Có MSS + displacement trong vùng premium/discount không?** ([[21 - Market Structure Shift]])
- **Entry FVG/OB có rơi vào OTE không?** ưu tiên 0.62–0.79 của leg LTF.
- **Stop loss đặt sau cực trị range / điểm sweep** để logic, không phải theo số pip cố định.

> [!warning]
> **LTF không tạo ra premium/discount; nó chỉ tinh chỉnh entry trong vùng vị trí mà HTF đã xác định.** Một M5 FVG đẹp ở vùng premium khi bias Bullish vẫn là entry sai vị trí.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Dealing range hợp lệ và Fib vẽ đúng chiều.
- [ ] Giá ở discount khi tìm Long, ở premium khi tìm Short.
- [ ] Vị trí đồng hướng Daily Bias.
- [ ] Có PD Array hợp lệ tại vùng premium/discount (lý tưởng là trong OTE 0.62–0.79).
- [ ] Có liquidity sweep + reaction tại cực trị range trước khi vào.
- [ ] Có displacement/MSS xác nhận trong vùng đó.
- [ ] Target là liquidity rõ ở phía bên kia EQ, đủ room R:R.

### Setup bị vô hiệu khi
- [ ] Giá đóng nến chấp nhận ra ngoài range → dealing range cũ không còn hiệu lực, premium/discount phải đo lại.
- [ ] Định mua nhưng giá đang ở premium, hoặc định bán nhưng giá đang ở discount.
- [ ] Vị trí ngược Daily Bias (discount nhưng bias Bearish, premium nhưng bias Bullish).
- [ ] Chỉ có vị trí đẹp nhưng không có PD Array nào để vào.
- [ ] Giá đã chạy xa khỏi EQ → entry trở thành chase.
- [ ] PD Array tại vùng đó đã bị mitigate/xuyên nhiều lần.

### Phân biệt "discount thật" và "discount giả vì sai range"

| Quan sát | Cách đọc hợp lý |
|---|---|
| Giá dưới EQ của range được vẽ từ swing có displacement/BOS rõ | Discount hợp lệ; nếu đồng bias + có PD Array thì tìm Long |
| Giá dưới EQ nhưng range vẽ từ một swing nhỏ/cũ không liên quan delivery hiện tại | Discount giả; đo lại bằng range đúng trước khi kết luận |
| Giá vào discount, sweep SSL rồi displacement lên, để lại FVG | Tín hiệu mạnh; chờ retrace vào FVG/OTE để Long |
| Giá đóng nến chấp nhận dưới đáy range cũ và không reclaim | Range đã đổi; "discount" của range cũ vô nghĩa, dựng range mới |
| Giá quanh 50% EQ | Trung lập — chưa đủ "rẻ"/"đắt", chờ giá đi sâu hơn |

---

## 6. Ví dụ chart

### Ví dụ đúng — Long từ Discount + OTE đồng hướng Bullish Bias
![[Premium-Discount-Example-Correct.png]]

**Mô tả:**  
D1/H4 Bullish, draw on liquidity là BSL phía trên. Vẽ Fibonacci từ swing low → swing high của HTF dealing range. Giá retrace xuống **discount**, đi vào vùng **OTE 0.62–0.79**, nơi có một bullish H1 FVG. Giá sweep SSL dưới đáy ngắn hạn, reclaim, rồi M5 tạo bullish MSS + displacement. Entry tại FVG trong OTE; stop dưới điểm sweep; TP hướng về BSL phía trên EQ.

**Vì sao đây là ví dụ tốt:**
- Dealing range hợp lệ, Fib vẽ đúng chiều low→high.
- Vị trí (discount) đồng hướng bias (Bullish).
- Entry trùng PD Array (bullish FVG) trong vùng OTE — confluence cao.
- Có liquidity sweep + displacement xác nhận, không phải mua mù ở discount.

### Ví dụ sai / dễ nhầm — Mua khi giá đang ở Premium sau khi đã chạy xa
![[Premium-Discount-Example-Wrong.png]]

**Mô tả lỗi:**  
Bias Bullish, giá đã expansion mạnh lên và đang ở **premium** (trên EQ), gần BSL. Trader thấy một bullish M5 FVG nhỏ và Long vì "bias Bullish". Đây là **chase ở premium**: giá chỉ pullback ngắn rồi quét BSL và đảo chiều, stop loss bị hit.

**Bài học:**
- Bias Bullish KHÔNG cho phép mua ở mọi vị trí — chỉ mua ở **discount**.
- Vị trí premium là nơi đi tìm Short (nếu có lý do), không phải nơi mua thêm.
- Hỏi: "Giá đang đắt hay rẻ so với range?" trước khi nhìn vào bất kỳ FVG nào.
- Chọn sai range cũng cho cảm giác "discount giả" — luôn kiểm tra range trước.

---
### Sequence mẫu — Long từ Discount
```text
HTF Bullish Bias
→ Xác định Dealing Range hợp lệ (vẽ Fib swing low → swing high)
→ Giá retrace vào Discount (< 0.5), lý tưởng vùng OTE 0.62–0.79
→ Discount trùng Bullish PD Array (bullish OB / FVG / mitigation block)
→ Sweep Sell-Side Liquidity tại cực trị range
→ Bullish MSS + Displacement trong vùng discount
→ Retrace vào FVG/OB (M5/M1) trong OTE
→ Stop sau điểm sweep / dưới đáy range
→ Target: liquidity phía trên EQ (internal trước, BSL chính sau)
```

### Sequence mẫu — Short từ Premium
```text
HTF Bearish Bias
→ Xác định Dealing Range hợp lệ (vẽ Fib swing high → swing low)
→ Giá retrace vào Premium (> 0.5), lý tưởng vùng OTE 0.62–0.79
→ Premium trùng Bearish PD Array (bearish OB / FVG / rejection block)
→ Sweep Buy-Side Liquidity tại cực trị range
→ Bearish MSS + Displacement trong vùng premium
→ Retrace vào FVG/OB (M5/M1) trong OTE
→ Stop sau điểm sweep / trên đỉnh range
→ Target: liquidity phía dưới EQ (internal trước, SSL chính sau)
```

> [!note]
> Premium/Discount không tự đứng một mình. Nó là lớp lọc **VỊ TRÍ** trong chuỗi: `Bias → Dealing Range → Premium/Discount → PD Array (POI) → Liquidity Sweep → MSS/Displacement → FVG/OB entry`. Bỏ qua lớp nào cũng làm giảm chất lượng setup.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Giá ở discount không phải lệnh mua; giá ở premium không phải lệnh bán. Premium/Discount chỉ có giá trị khi đúng **context + timeframe + liquidity narrative**.

### A. Context (HTF)
- [ ] Tôi đã xác định dealing range hợp lệ và vẽ Fibonacci đúng chiều.
- [ ] Tôi biết rõ giá đang ở Premium / Discount / Equilibrium.
- [ ] Vị trí premium/discount đồng hướng Daily Bias.
- [ ] Có HTF PD Array tại vùng premium/discount đó.
- [ ] Có draw on liquidity rõ ở phía bên kia EQ làm target.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã vào đúng vùng discount (cho Long) hoặc premium (cho Short), lý tưởng là OTE 0.62–0.79.
- [ ] Có PD Array hợp lệ để vào (bullish array ở discount / bearish array ở premium).
- [ ] Có liquidity sweep tại cực trị range trước reaction.
- [ ] Có MSS + displacement trong vùng đó.
- [ ] Entry FVG/OB có stop loss logic sau điểm sweep / cực trị range.
- [ ] Target là liquidity rõ phía bên kia EQ, đủ R:R.
- [ ] Tôi không chase: giá chưa chạy xa khỏi EQ theo hướng bias.

### C. Quy tắc "không có lệnh"
- [ ] Giá ở equilibrium / quanh 50% → không trade.
- [ ] Giá ở premium nhưng muốn mua (hoặc discount nhưng muốn bán) → không trade.
- [ ] Dealing range không rõ / chọn sai → không kết luận premium/discount.
- [ ] Vị trí đẹp nhưng không có PD Array → không có POI để vào → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Mua ở premium / bán ở discount | Long khi giá > EQ, Short khi giá < EQ | Vào lúc giá kém lợi thế; stop rộng, room tới target hẹp | Chỉ Long ở discount, Short ở premium; kiểm tra EQ trước khi vào |
| Chọn sai dealing range | Vẽ Fib từ swing nhỏ/cũ không có displacement | EQ đặt sai → toàn bộ premium/discount lệch theo | Chọn swing tạo displacement/BOS, phù hợp price delivery hiện tại |
| Chase sau khi giá chạy xa | Long ở premium sau bullish expansion lớn | Vào ngay trước retrace; R:R xấu, dễ bị stop | Chờ giá retrace về discount/OTE hoặc bỏ qua |
| Coi discount/premium là tín hiệu vào lệnh | "Giá ở discount nên mua luôn" | Bỏ qua bias, POI, liquidity → entry mù | Dùng nó như bộ lọc vị trí, cần thêm bias + PD Array + sweep + MSS |
| Bỏ qua Daily Bias | Mua ở discount khi bias Bearish | Vị trí "rẻ" trong một range đang đi xuống = bắt dao rơi | Chỉ mua discount khi bias Bullish, bán premium khi bias Bearish |
| Vẽ Fib sai chiều | Bullish leg lại vẽ high→low | Premium và discount bị đảo ngược | Bullish: low→high; Bearish: high→low |
| Entry tại equilibrium | Vào ngay mốc 50% | Vùng trung lập, không có lợi thế, dễ choppy | Chờ giá đi sâu vào premium/discount tới PD Array |
| Vùng đẹp nhưng không có POI | Discount nhưng không có bullish array nào | Không có điểm vào có cấu trúc, stop vô lý | Chỉ vào khi premium/discount trùng PD Array hợp lệ |
| Dùng range quá lớn cho khung nhỏ | "Discount" cách giá hàng trăm pip | Vị trí không liên quan tới execution hiện tại | Đo premium/discount theo range phù hợp khung đang trade |
| Bỏ qua liquidity sweep | Vào discount khi chưa quét SSL | Market thường còn cần lấy đáy trước khi reverse | Chờ sweep + reaction trước khi tìm entry |

---

## 10. Câu hỏi tự kiểm tra

- Tôi đang đo premium/discount theo **dealing range nào**, và range đó có hợp lệ không?
- Tôi đã vẽ Fibonacci đúng chiều (low→high cho bullish, high→low cho bearish) chưa?
- Giá hiện ở premium, discount hay equilibrium?
- Vị trí này có đồng hướng Daily Bias không?
- Có PD Array hợp lệ tại vùng premium/discount để tôi vào không?
- Entry của tôi có rơi vào OTE 0.62–0.79 không?
- Tôi đang mua rẻ/bán đắt hay đang chase sau khi giá chạy xa khỏi EQ?
- Có liquidity sweep + MSS trong vùng đó chưa, hay tôi vào chỉ vì thấy vị trí đẹp?
- Target liquidity ở phía bên kia EQ là level nào, còn đủ room R:R không?
- Nếu range bị phá (acceptance ra ngoài), tôi có biết phải đo lại premium/discount không?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Premium, Discount và Equilibrium được định nghĩa thế nào?  
**Đáp:** Trên một dealing range chia bằng Fibonacci: Discount là phần dưới 50% (giá "rẻ", vùng tìm MUA), Premium là phần trên 50% (giá "đắt", vùng tìm BÁN), Equilibrium là mốc 50% — vùng trung lập/ra quyết định.

### Q2
**Hỏi:** Nguyên tắc cốt lõi của Premium/Discount là gì?  
**Đáp:** Mua ở Discount, Bán ở Premium — nhưng chỉ khi đồng hướng Daily Bias VÀ tại một PD Array hợp lệ. Không mua premium, không bán discount.

### Q3
**Hỏi:** Vì sao chọn đúng dealing range lại quan trọng?  
**Đáp:** Premium/discount được tính từ mốc 50% của range. Chọn sai range → EQ sai → toàn bộ phân loại premium/discount lệch, dẫn tới mua premium / bán discount mà tưởng là đúng.

### Q4
**Hỏi:** Vùng OTE là gì và liên quan thế nào tới premium/discount?  
**Đáp:** OTE là vùng 0.62–0.79 của leg — vùng retrace sâu trong discount (cho Long) hoặc premium (cho Short) cho R:R tối ưu. Premium/discount cho biết phía nào tìm lệnh; OTE tinh chỉnh vùng giá cụ thể để vào.

### Q5
**Hỏi:** Giá đang ở discount, bias Bullish — có nên mua ngay không?  
**Đáp:** Không. Discount chỉ là điều kiện vị trí. Cần thêm PD Array hợp lệ tại đó, liquidity sweep và MSS/displacement xác nhận thì mới execution.

### Q6
**Hỏi:** Liệt kê vài PD Array phía discount (để mua) và phía premium (để bán).  
**Đáp:** Discount (mua): bullish OB, bullish FVG, mitigation block, old low/SSL, bullish breaker. Premium (bán): bearish OB, bearish FVG, rejection block, old high/BSL, bearish breaker.

### Q7
**Hỏi:** Equilibrium nên dùng làm vùng entry không?  
**Đáp:** Không. EQ là vùng trung lập/ra quyết định: trên EQ nghiêng short setup, dưới EQ nghiêng long setup theo bias. Entry ngay tại 50% thường là trade giữa range với R:R xấu.

### Q8
**Hỏi:** Hai lỗi nguy hiểm nhất với premium/discount là gì?  
**Đáp:** (1) Mua ở premium / bán ở discount (chase, vào lúc kém lợi thế); (2) Chọn sai dealing range khiến toàn bộ premium/discount sai lệch.

---
## 12. Lesson Learned

### Bài học chính
- Premium/Discount biến tư duy "mua rẻ, bán đắt" thành một quy tắc định lượng theo range, thay vì cảm tính.
- Toàn bộ giá trị của khái niệm phụ thuộc vào việc **chọn đúng dealing range trước**; sai range thì mọi kết luận đều sai.
- Equilibrium là vùng ra quyết định, không phải vùng entry — vào lệnh nên ở premium/discount đủ sâu, lý tưởng là OTE.
- Premium/Discount chỉ là một lớp lọc vị trí; nó phải kết hợp với bias + PD Array + liquidity sweep + MSS mới thành một setup.
- Bias Bullish không phải giấy phép mua ở mọi vị trí; vị trí premium vẫn là nơi đi tìm Short, không phải mua thêm.

### Quy tắc cá nhân rút ra
- [ ] Tôi không kết luận premium/discount nếu chưa xác định dealing range hợp lệ và vẽ Fib đúng chiều.
- [ ] Tôi chỉ tìm Long ở discount, tìm Short ở premium — không bao giờ ngược lại.
- [ ] Tôi không vào lệnh tại equilibrium; chờ giá đi sâu vào premium/discount tới PD Array.
- [ ] Tôi không chase: nếu giá đã chạy xa khỏi EQ theo hướng bias, tôi chờ retrace hoặc bỏ qua.
- [ ] Premium/discount đẹp nhưng không có PD Array = không có POI = không có lệnh.

### Câu nhắc nhở khi trade
> **"Trước khi nhìn FVG hay OB, hãy hỏi: giá đang đắt hay rẻ — và đó là range nào?"**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt rõ premium / discount / equilibrium và vai trò mỗi vùng? |
| Nhận diện trên chart |  | Vẽ Fib đúng chiều và đọc đúng EQ theo range hợp lệ? |
| Biết khi nào bỏ qua |  | Có dừng tại equilibrium / khi range không rõ không? |
| Kết hợp với context HTF |  | Có gắn premium/discount với Daily Bias + PD Array + liquidity không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự ở discount/premium tại PD Array, không chase? |
| Review sau trade |  | Có kiểm tra `pd_location` và `pd_bias_alignment` bằng dữ liệu journal? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Premium Discount]]`.
- [ ] So sánh riêng lệnh entry ở discount/premium (aligned) với lệnh ở equilibrium hoặc ngược vị trí.
- [ ] Thống kê win rate, average R theo `pd_location` và `entry_in_ote`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.

---

## Appendix — Premium/Discount Quick Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**  
> **Daily Bias:** Bullish / Bearish / Neutral  
> **Dealing range:** swing low ___ → swing high ___ (hoặc ngược lại)  
> **Fib direction:** low→high (bullish) / high→low (bearish)  
> **Vị trí hiện tại:** Premium / Discount / Equilibrium (___%)  
> **Vùng OTE (0.62–0.79):** ___ – ___  
> **PD Array tại vùng đó:** ___ (bullish/bearish OB, FVG, breaker...)  
> **Draw on liquidity (phía bên kia EQ):** ___  
> **Hành động ưu tiên:** Long từ discount / Short từ premium / No-trade  
> **Sweep cần thấy trước entry:** SSL (Long) / BSL (Short) tại ___  
> **Invalidation:** acceptance ra ngoài range tại ___  
> **No-trade condition:** giá ở equilibrium / range không rõ / ngược bias  
