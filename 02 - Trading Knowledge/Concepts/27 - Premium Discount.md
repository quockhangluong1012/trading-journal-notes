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
updated: 2026-07-03
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

### Nâng cao — Chia nhỏ Premium/Discount thành quartile (0-25-50-75-100%) để đọc "sâu" hay "nhẹ"

Nhị phân trên/dưới 50% là phép chia thô: nó chỉ nói giá "rẻ" hay "đắt", chứ không nói **rẻ tới mức nào**. ICT thực chiến hay chia nhỏ range thành **4 quartile** để định lượng độ "sâu" — dùng con số này để điều chỉnh conviction và mức độ mạnh dạn khi entry, thay vì coi mọi điểm dưới 50% là như nhau.

![[Premium-Discount-Advanced-Quartiles.svg]]
*Bốn quartile của một dealing range: Deep Discount (0-25%) và Deep Premium (75-100%) là vùng conviction cao nhất — nơi PD Array đáng tin nhất và OTE (62-79%) thường rơi vào; Discount nông (25-50%) và Premium nông (50-75%) đòi hỏi thêm confluence trước khi tin tưởng.*

| Quartile | Khoảng Fib | Đọc "sâu/nhẹ" | Conviction / hành động |
|---|---|---|---|
| **Deep Discount** | 0% → 25% | Rất "rẻ" | Conviction cao nhất cho Long; size đủ theo plan nếu có PD Array + sweep |
| **Discount nông** | 25% → 50% | "Rẻ" vừa phải | Long được nhưng cần thêm confluence (POI HTF, MSS rõ); cẩn trọng vì có thể còn nhúng sâu hơn |
| **Premium nông** | 50% → 75% | "Đắt" vừa phải | Short được nhưng cần thêm confluence; phản ứng thường yếu hơn deep premium |
| **Deep Premium** | 75% → 100% | Rất "đắt" | Conviction cao nhất cho Short; size đủ theo plan nếu có PD Array + sweep |

> [!tip]
> Quartile không đổi **hướng** lệnh — discount nông vẫn là discount, vẫn chỉ đi tìm Long. Nó chỉ đổi **mức độ tự tin và cỡ lệnh**: một bullish FVG ở deep discount (0-25%) đáng tin hơn nhiều so với cùng loại FVG ở discount nông (25-50%), vốn dễ bị giá xuyên qua để tìm tiếp vùng sâu hơn. Ghi trường `pd_quartile: extreme-discount | discount | premium | extreme-premium` vào journal cho mỗi lệnh để sau này so sánh win rate/R theo từng quartile — cần backtest xác nhận trước khi coi đây là quy tắc cứng.

### Nâng cao — Premium/Discount lồng nhau đa khung thời gian: khi H4 và M15 mâu thuẫn

Dealing Range có tính fractal (xem [[12 - Dealing Range]]): H4 có range của nó, và bên trong H4 lại có một range con nhỏ hơn trên M15. Vì hai range đo trên hai swing khác nhau, **cùng một điểm giá hoàn toàn có thể vừa nằm ở Discount của H4, vừa nằm ở Premium của M15** — đây không phải lỗi vẽ sai, mà là hệ quả tự nhiên của cấu trúc lồng nhau.

![[Premium-Discount-Advanced-NestedTimeframes.svg]]
*Một H4 dealing range lớn (trái) với giá đang ở Discount, chứa bên trong nó một M15 range nhỏ hơn (zoom phải) nơi CHÍNH điểm giá đó lại rơi vào Premium của M15. Quy tắc: H4 quyết định bias/POI, M15 chỉ tinh chỉnh thời điểm entry.*

Quy tắc giải quyết xung đột — **HTF governs bias/POI, LTF refines entry timing**:
- **HTF dealing range (H4) quyết định HƯỚNG được phép tìm lệnh.** Nếu H4 đang discount, chỉ đi tìm Long — bất kể M15 đang premium hay discount.
- **LTF dealing range (M15) không được phép phủ quyết hướng của HTF.** Vai trò của M15 chỉ là tinh chỉnh **thời điểm và giá entry cụ thể**, không phải để quyết định Long hay Short.
- Khi H4 discount nhưng M15 đang premium: **chờ** — hoặc chờ M15 tự retrace về discount của chính nó, hoặc chờ M15 tạo một MSS bullish riêng (nhịp displacement mới nội bộ) trước khi tìm entry. Không Long ngay lúc M15 đang premium chỉ vì H4 đã discount.
- Khi H4 discount VÀ M15 cũng discount (cộng hưởng hai tầng) → đây là setup chất lượng cao nhất, conviction tối đa.

**Ví dụ thực hành:** H4 bias Bullish, giá ở discount H4 (khoảng 30% range H4). Trên M15, cùng điểm giá đó lại nằm ở 65% của range M15 con (tức premium M15) vì M15 vừa tạo một swing low mới gần hơn. Quy tắc: KHÔNG Long ngay. Chờ M15 hoặc retrace xuống dưới 50% của chính nó, hoặc quét thanh khoản nội bộ rồi MSS bullish — khi đó M15 mới "đồng ý" với H4, và entry lúc này có cả hai tầng xác suất cộng dồn.

> [!warning]
> Đừng nhầm mâu thuẫn đa khung với "chọn sai range". Nếu cả H4 và M15 đều được vẽ đúng (swing có displacement/BOS, có liquidity ở hai đầu), mâu thuẫn Premium/Discount giữa chúng là **bình thường** — chỉ cần biết tầng nào governs quyết định gì. Xem thêm ma trận alignment 2 tầng ở [[12 - Dealing Range]] (mục A2. Nested ranges).

### Nâng cao — Overlap giữa Premium/Discount và OTE (62-79%)

[[26 - OTE - Optimal Trade Entry|OTE]] và Premium/Discount thường được dạy tách rời, nhưng về bản chất chúng là **hai công cụ đo cùng một thứ ở hai độ phân giải khác nhau**: Premium/Discount cho biết giá đang ở nửa nào của range; OTE (62-79% retracement của nhịp displacement) tinh chỉnh xuống một dải giá cụ thể — và với một nhịp Long hợp lệ, dải 62-79% đó gần như luôn rơi vào phần **discount sâu** của chính range đang dùng. Đây là lý do OTE "vừa vặn" cho R:R tốt: nó là điểm cực đoan của discount, không phải điểm giữa.

![[Premium-Discount-Advanced-vs-OTE.svg]]
*Bên trái: trường hợp lý tưởng — dải OTE 62-79% được tính trên CHÍNH nhịp tạo ra dealing range, nên nằm gọn trong Discount → hai lớp confluence cộng hưởng. Bên phải: trường hợp phân kỳ — OTE tính trên một nhịp displacement nhỏ hơn/khác swing với dealing range, khiến dải OTE lấn gần hoặc vượt qua Equilibrium.*

| Tình huống | Quan hệ OTE ↔ Premium/Discount | Hành động |
|---|---|---|
| Fib OTE kéo trên đúng nhịp tạo dealing range | OTE 62-79% nằm gọn trong discount (Long)/premium (Short) | Confluence mạnh nhất — vào theo kế hoạch, conviction cao |
| Fib OTE kéo trên một nhịp LTF nhỏ hơn, nội bộ | OTE có thể lấn gần EQ hoặc lệch sang nửa đối diện | Kiểm tra lại: nhịp LTF có thực sự phá cấu trúc và đồng hướng bias không trước khi tin |
| OTE nằm đúng vùng nhưng dealing range chọn sai (swing nhỏ/cũ) | Coi như "trùng khớp giả" | Vẽ lại dealing range đúng trước, rồi xét lại OTE có còn hợp lệ không |

**Quy tắc giải quyết khi hai công cụ mâu thuẫn:** nếu vùng OTE (tính đúng theo quy trình của [[26 - OTE - Optimal Trade Entry]] — trên nhịp displacement đã phá cấu trúc) lại rơi ra ngoài Discount/Premium của dealing range đúng, **ưu tiên vị trí Premium/Discount của HTF dealing range** làm bộ lọc chính; OTE lúc này chỉ dùng để tinh entry trong phần discount/premium đó, không dùng để đổi hướng bias. Ngược lại, nếu dealing range đúng nhưng OTE tính sai nhịp (nhịp không phá cấu trúc), lỗi nằm ở OTE — sửa theo checklist của OTE trước, không đổ lỗi cho Premium/Discount.

> [!note]
> Khi cả hai đồng thuận (OTE nằm trong đúng nửa range của Premium/Discount), đây là một trong những confluence mạnh nhất trong ICT 2022 Model — hai công cụ độc lập cùng chỉ về một vùng giá. Cần backtest xác nhận tỉ lệ entry "OTE trùng discount/premium" thắng nhiều hơn "OTE lệch khỏi discount/premium" trước khi coi đây là rule cứng cho size lệnh.

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

### Giải phẫu
![[Premium-Discount-Anatomy.svg]]

**Mô tả:**
Cấu trúc đầy đủ của một dealing range: **swing low (0%)** và **swing high (100%)** xác định hai đầu range; mốc **50% (Equilibrium)** chia range thành **Premium** (nửa trên, đi tìm Short) và **Discount** (nửa dưới, đi tìm Long); dải **OTE (62–79%)** được overlay bên trong discount — vùng entry tối ưu khi giá retrace đủ sâu sau một nhịp displacement.

- **Swing High (100%)** và **Swing Low (0%)** phải được tạo bởi displacement/BOS, không phải swing ngẫu nhiên (xem [[12 - Dealing Range]]).
- **Equilibrium (50%)** là ranh giới, không phải vùng entry — chỉ dùng để biết nghiêng Long hay Short.
- **Dải OTE (62–79%)** nằm gọn trong phần discount sâu — đây là lý do OTE cho R:R tốt hơn nhiều so với entry ở 50%.
- Bullish PD Array (OB/FVG) nằm trong discount đáng tin hơn cùng loại PD Array nằm trong premium, và ngược lại với bearish PD Array.

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

## Best Practices

> [!success] Nguyên tắc vàng
> **Premium/Discount chỉ có nghĩa khi được đo trên một dealing range đúng — và ngay cả khi range đúng, nó vẫn chỉ là một bộ lọc VỊ TRÍ, không phải tín hiệu vào lệnh.** Càng định lượng vị trí đó (quartile, đa khung, overlap OTE) thay vì dừng ở nhị phân trên/dưới 50%, bộ lọc này càng sắc và càng đáng để backtest xác nhận.

1. **Luôn xác định đúng dealing range trước khi đọc bất kỳ con số premium/discount nào.** Range phải được vẽ từ swing có displacement/BOS, lý tưởng là đã lấy liquidity ở hai đầu (xem [[12 - Dealing Range]]). Chọn range quá nhỏ hoặc quá cũ khiến toàn bộ premium/discount phái sinh đều sai — đây là lỗi gốc rễ nguy hiểm nhất trong khái niệm này.

2. **Khi H4 và M15 (hoặc bất kỳ cặp HTF/LTF nào) mâu thuẫn về premium/discount, luôn để HTF quyết định hướng, LTF chỉ tinh entry.** Không bao giờ để một range LTF phủ quyết bias đã xác lập trên HTF. Nếu H4 discount nhưng M15 đang premium, chờ M15 tự retrace hoặc tạo MSS riêng — không Long ngay. Ghi trường `htf_ltf_pd_conflict: yes/no` vào journal cho mỗi lệnh để sau này đo xem việc chờ đồng thuận hai tầng có thực sự nâng win rate không.

3. **Dùng quartile (0-25-50-75-100%) để định lượng conviction, không chỉ dừng ở nhị phân trên/dưới 50%.** Một PD Array ở deep discount (0-25%) đáng tin hơn nhiều so với cùng loại PD Array ở discount nông (25-50%) — vốn còn nguy cơ bị giá xuyên qua để tìm vùng sâu hơn. Ghi `pd_quartile: extreme-discount | discount | premium | extreme-premium` cho mỗi lệnh và dùng nó để điều chỉnh size, không chỉ hướng lệnh.

4. **Coi overlap giữa Premium/Discount và [[26 - OTE - Optimal Trade Entry|OTE]] là một lớp confluence cần kiểm tra, không phải hai khái niệm tách rời.** Khi dải OTE 62-79% của một nhịp displacement hợp lệ nằm gọn trong discount (Long)/premium (Short) của dealing range đang dùng, đó là entry có hai lớp xác suất cộng dồn. Nếu chúng phân kỳ, ưu tiên vị trí Premium/Discount của HTF dealing range làm bộ lọc chính.

5. **Không bao giờ coi equilibrium (50%) là vùng entry.** Đây là ranh giới ra quyết định, không phải POI — vào lệnh ngay tại 50% gần như luôn cho R:R kém và dễ bị chop. Luôn chờ giá đi đủ sâu vào premium/discount (lý tưởng tới OTE hoặc quartile cực trị) trước khi tìm PD Array để entry.

6. **Premium/Discount không thay thế Daily Bias, PD Array, liquidity sweep hay MSS — nó là một lớp lọc trong một chuỗi, không phải toàn bộ chuỗi.** Discount đồng hướng bias mà không có PD Array hợp lệ = không có POI = không có lệnh. Luôn xác nhận đủ chuỗi: `Bias → Dealing Range → Premium/Discount → PD Array (POI) → Liquidity Sweep → MSS/Displacement → FVG/OB entry`.

7. **Ghi lại đầy đủ các trường định lượng cho mỗi lệnh có dùng Premium/Discount:** `pd_location`, `pd_quartile`, `htf_ltf_pd_conflict`, `entry_in_ote`. Đây là dữ liệu tối thiểu để trả lời câu hỏi thực chiến: quartile nào cho win rate cao nhất, xung đột đa khung có đáng chờ không, overlap OTE có thực sự nâng R không — tất cả **cần backtest xác nhận** trước khi trở thành quy tắc cứng.

8. **Sau 20–30 mẫu, review riêng theo `symbol`** (NQ1/NAS100, EURUSD, GBPUSD, XAUUSD gần như chắc chắn có đặc tính retrace/quartile khác nhau) thay vì gộp chung mọi thị trường vào một con số kết luận. Đối chiếu kết quả với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]], đồng thời nâng `confidence` của note này khi đã có đủ bằng chứng.

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
