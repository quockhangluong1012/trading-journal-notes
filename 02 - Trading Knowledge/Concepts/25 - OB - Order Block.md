---
type: ict-concept
concept: Order Block
aliases:
  - OB
  - Order Block
  - Bullish OB
  - Bearish OB
tags:
  - trading/ict/concept
  - trading/study
  - "#OrderBlock"
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
last_reviewed: 2026-07-01
created: 2026-06-22
updated: 2026-07-18
common_mistakes:
  - "[[Mistake - Trade Every Order Block]]"
  - "[[Mistake - OB Without Displacement]]"
  - "[[Mistake - Confuse OB with Breaker Block]]"
---

# Order Block

> [!summary] Tóm tắt 1 câu
> **Order Block là nến (hoặc cụm nến) ngược hướng CUỐI CÙNG ngay trước một đợt displacement phá cấu trúc — một POI có narrative (sweep + displacement + imbalance), không phải mọi vùng supply/demand “nến lớn cuối cùng”.**

> [!important] Nguyên tắc cốt lõi
> **Một OB chỉ có giá trị khi nó gắn với displacement mạnh, lý tưởng có liquidity sweep ngay trước nó, để lại FVG/imbalance và gây ra BOS/MSS.**  
> Đừng “bắt” mọi OB: chỉ dùng OB ở đúng premium/discount, đồng hướng Daily Bias, và sau khi liquidity đã bị quét.

---

## 1. Định nghĩa

![[Order-Block-Sec-01-Dinh-Nghia.svg|720]]
*Sơ đồ: Bullish OB (nến giảm cuối trước displacement tăng — demand) và Bearish OB (nến tăng cuối trước displacement giảm — supply); Mean Threshold 50% là mức tham chiếu.*

**Khái niệm:**  
Order Block (OB) trong ICT là **nến hoặc cụm nến ngược hướng cuối cùng** xuất hiện ngay trước một đợt displacement đẩy giá đi mạnh và phá cấu trúc. Đây là vùng được xem là nơi “smart money” đã đặt lệnh trước khi đẩy giá, nên giá thường quay lại để mitigate (lấp lệnh) trước khi tiếp tục.

- **Bullish OB:** nến **giảm cuối cùng** trước một đợt tăng mạnh (vùng cầu / demand). Khi giá quay lại vùng này, ta kỳ vọng phản ứng tăng.
- **Bearish OB:** nến **tăng cuối cùng** trước một đợt giảm mạnh (vùng cung / supply). Khi giá quay lại vùng này, ta kỳ vọng phản ứng giảm.

OB không phải đơn thuần là “nến to nhất” hay “vùng giá phản ứng mạnh”. Trong ICT, OB **bắt buộc có narrative**: liquidity bị quét → displacement đẩy giá → để lại imbalance → phá cấu trúc.

**Mục đích trong ICT:**  
- Cung cấp một **POI có cấu trúc** để chờ giá quay về và vào lệnh, thay vì vào giữa không trung.
- Cho ra **stop loss logic**: stop đặt qua đầu kia của OB hoặc qua điểm sweep.
- Đánh dấu **vùng cầu/cung của smart money** đồng hướng với Daily Bias và draw on liquidity.
- Kết hợp với FVG/Mean Threshold để tạo entry refinement chính xác.

**Vì sao khái niệm này quan trọng:**  
OB là một trong những PD Array được dùng nhiều nhất để xác định entry. Nhưng cũng là khái niệm bị lạm dụng nhất: trader vẽ OB ở mọi nến lớn, rồi vào lệnh khi giá chỉ chạm vùng đó mà không có sweep, không có displacement. OB chỉ có edge khi nó là **mắt xích trong sequence**: HTF bias → location đúng → sweep → displacement → OB/FVG entry.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Vùng giá nào smart money có khả năng đã đặt lệnh trước đợt đẩy?
- Đâu là POI hợp lệ để chờ retrace vào, đồng hướng bias?
- Entry và stop loss nên đặt ở đâu một cách có cấu trúc?
- OB này còn “tươi” (unmitigated) hay đã bị lấp (mitigated)?
- OB này đi thuận dòng lệnh (low-resistance) hay ngược dòng (high-resistance)?

### Order Block không phải là gì
- Không phải “nến to cuối cùng” bất kỳ — nó phải gây ra displacement phá cấu trúc.
- Không phải vùng supply/demand thông thường vẽ kiểu price action — OB của ICT đòi hỏi narrative liquidity.
- Không phải lý do vào lệnh khi giá chỉ chạm vùng nhưng chưa có sweep/displacement trước đó.
- Không phải Breaker Block — OB **giữ vai trò**; Breaker là OB đã **fail rồi flip vai trò** (xem [[Breaker Block]]).
- Không phải cái cớ để Long ở premium hay Short ở discount; vẫn phải đúng vị trí trong dealing range.
- Không phải tín hiệu mạnh nếu nó được tạo giữa range, không có liquidity event và không có imbalance.

---

## 2. Bối cảnh sử dụng

![[Order-Block-Sec-02-Boi-Canh.svg|720]]
*Sơ đồ: Ma trận phân loại OB — Unmitigated/Mitigated × Low-/High-resistance; combo chất lượng cao nhất.*

### Các loại Order Block cần phân biệt

| Loại OB                | Định nghĩa                                                 | Hành động ưu tiên                                                                   |
| ---------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **Bullish OB**         | Nến giảm cuối cùng trước bullish displacement; vùng demand | Chờ giá retrace xuống mitigate OB ở **discount**, đồng hướng bullish bias, tìm Long |
| **Bearish OB**         | Nến tăng cuối cùng trước bearish displacement; vùng supply | Chờ giá retrace lên mitigate OB ở **premium**, đồng hướng bearish bias, tìm Short   |
| **Unmitigated OB**     | OB chưa bị giá quay lại lấp lần nào                        | Giá trị cao nhất: phản ứng “tươi”, ưu tiên dùng làm POI                             |
| **Mitigated OB**       | OB đã bị giá quay lại chạm/lấp                             | Giá trị giảm dần; phản ứng kế tiếp yếu hơn, cẩn trọng                               |
| **Low-resistance OB**  | OB thuận dòng lệnh chính (đồng hướng HTF delivery)         | Xác suất cao hơn; ít lực cản; ưu tiên                                               |
| **High-resistance OB** | OB đi ngược dòng lệnh chính (nhiều cản)                    | Xác suất thấp; chỉ dùng có chọn lọc với counter-trend playbook                      |
| **Breaker (đã fail)**  | OB bị phá/fail rồi đảo vai trò                             | Không còn là OB; xử lý như [[Breaker Block]]                                        |

> [!tip]
> **Unmitigated + low-resistance + đúng premium/discount + sau sweep** là tổ hợp OB chất lượng cao nhất. Một OB “tươi” đồng hướng bias sau khi liquidity vừa bị quét là kịch bản lý tưởng.

### Khi nào khái niệm này có giá trị cao?
- [ ] OB được tạo bởi displacement mạnh, phá BOS/MSS có ý nghĩa.
- [ ] Có liquidity sweep ngay trước OB (OB nằm ngay sau điểm quét đỉnh/đáy).
- [ ] OB để lại FVG/imbalance phía sau khi giá đẩy đi.
- [ ] OB còn unmitigated (giá chưa quay lại lấp lần nào).
- [ ] OB nằm đúng phía premium/discount phù hợp với hướng trade.
- [ ] OB đồng hướng với Daily Bias và draw on liquidity chính.
- [ ] OB là low-resistance (thuận dòng lệnh HTF).
- [ ] Giá tiếp cận OB trong kill zone / cửa sổ thời gian có edge.

### Khi nào nên bỏ qua?
- [ ] OB ở giữa range, gần equilibrium, không rõ premium/discount.
- [ ] OB không gắn với displacement; chỉ là một nến lớn cô lập.
- [ ] OB không có sweep trước đó và không để lại imbalance.
- [ ] OB đã bị mitigate nhiều lần (đặc biệt đã bị xuyên thân nến).
- [ ] OB ngược hướng Daily Bias mà không có counter-trend playbook.
- [ ] OB đã chuyển thành breaker (đã fail) → đọc nó như [[Breaker Block]], không như OB.
- [ ] Giá đã chạy quá xa khỏi OB; vào lệnh thành chase, R:R xấu.
- [ ] Có tin tức high-impact gần thời điểm giá chạm OB mà plan không cho phép trade.

---

## 3. Cấu trúc nhận diện trên chart

![[Order-Block-Sec-03-Nhan-Dien.svg|720]]
*Sơ đồ: Chuỗi 5 dấu hiệu đúng thứ tự của OB hợp lệ — Sweep → OB → Displacement → BOS/MSS → Imbalance.*

### Dấu hiệu chính
1. **Nến ngược hướng cuối cùng:** với bullish OB là nến giảm (down-close) cuối trước đợt tăng; với bearish OB là nến tăng (up-close) cuối trước đợt giảm.
2. **Displacement ngay sau OB:** nến/cụm nến thân lớn, có urgency, đóng quyết đoán, đẩy giá đi xa.
3. **Phá cấu trúc:** đợt displacement đó tạo BOS ([[Break of Structure]]) hoặc MSS ([[21 - Market Structure Shift]]).
4. **Imbalance để lại:** displacement thường để lại FVG ([[Fair Value Gap]]) phía sau — dấu hiệu mạnh OB hợp lệ.
5. **Liquidity sweep trước OB:** lý tưởng OB hình thành ngay sau khi giá quét một liquidity pool (đỉnh/đáy, equal highs/lows).

### Ma trận nhận diện OB

| Thành phần | Bullish OB hợp lệ | Bearish OB hợp lệ | Cảnh báo / dễ nhầm |
|---|---|---|---|
| **Nến gốc** | Nến giảm cuối cùng trước đợt tăng | Nến tăng cuối cùng trước đợt giảm | Nến lớn cô lập, không có đợt đẩy theo sau |
| **Displacement** | Bullish displacement thân lớn ngay sau OB | Bearish displacement thân lớn ngay sau OB | Đẩy yếu, nhiều wick, không quyết đoán |
| **Cấu trúc** | Phá swing high nội bộ → BOS/MSS bullish | Phá swing low nội bộ → BOS/MSS bearish | Không phá cấu trúc, chỉ dao động trong range |
| **Imbalance** | Để lại bullish FVG phía trên OB | Để lại bearish FVG phía dưới OB | Không có FVG; giá đi “lấp đầy” không bỏ trống |
| **Liquidity** | Sweep SSL/đáy ngay trước OB | Sweep BSL/đỉnh ngay trước OB | Chưa sweep gì; OB tạo giữa không trung |
| **Location** | OB nằm ở discount của dealing range | OB nằm ở premium của dealing range | OB quanh 50% equilibrium; vị trí mơ hồ |

### Điều kiện bắt buộc (theo ICT, KHÁC supply/demand thường)
- [ ] OB gắn với **displacement mạnh** ngay sau đó (không chỉ là nến lớn).
- [ ] Displacement đó **gây ra BOS/MSS** — phá cấu trúc có ý nghĩa.
- [ ] OB là **nến ngược hướng cuối cùng** trước đợt đẩy (đúng định nghĩa, không phải nến bất kỳ).
- [ ] Xác định được **đầu OB, đáy OB, và Mean Threshold (50%)** rõ ràng.

### Điều kiện tăng xác suất
- [ ] Có **liquidity sweep ngay trước OB** (OB hình thành ngay sau khi quét đỉnh/đáy).
- [ ] Displacement để lại **FVG/imbalance** rõ ràng — entry refinement có thể combine OB + FVG.
- [ ] OB còn **unmitigated** khi giá quay lại.
- [ ] OB đúng **premium (bearish) / discount (bullish)** của dealing range.
- [ ] OB **low-resistance** (thuận dòng lệnh HTF, đồng hướng bias).
- [ ] OB ở HTF (H4/H1) cho phản ứng tin cậy hơn OB nhỏ lẻ ở M1.

### Điều kiện làm setup yếu đi
- OB không có displacement theo sau; chỉ là nến lớn cô lập giữa range.
- OB không phá cấu trúc; giá vẫn dao động trong range cũ.
- OB đã bị mitigate / xuyên thân nhiều lần — phản ứng kế tiếp thường yếu.
- OB high-resistance (ngược dòng lệnh chính), bắt dao ngược trend.
- OB ở sai vị trí: Long từ bullish OB nằm ở premium, hoặc Short từ bearish OB nằm ở discount.
- OB không có sweep trước đó; thiếu hẳn narrative liquidity.
- OB đã trở thành breaker (đã fail) nhưng vẫn bị đọc như OB.

---

## 4. Quy trình phân tích đa khung thời gian

![[Order-Block-Sec-04-Da-Khung.svg|720]]
*Sơ đồ: Top-down D1/H4 → H1/M15 → M5/M1 với các câu hỏi bắt buộc trước khi dùng một OB.*

> [!example] Các câu hỏi bắt buộc trước khi dùng một OB
> 1. **OB này có gắn với displacement phá cấu trúc không?**  
> 2. **Có liquidity sweep ngay trước OB không?**  
> 3. **OB còn unmitigated và đúng premium/discount không?**  
> 4. **OB này low-resistance hay high-resistance so với HTF bias?**  
> 5. **Điều gì chứng minh OB đã fail (chuyển thành breaker)?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (theo [[12 - Daily Bias]]).
- **HTF OB quan trọng:** đánh dấu OB D1/H4 còn unmitigated, gắn với displacement và BOS rõ.
- **Location của OB:** OB nằm ở premium hay discount của HTF dealing range?
- **Draw on liquidity:** OB đồng hướng với liquidity target chính chưa?
- **Narrative:** giá có khả năng retrace về [HTF OB] tại [discount/premium], mitigate, rồi đẩy tiếp về [liquidity target]; invalid nếu giá đóng nến mạnh xuyên qua OB và giữ giá ngoài đó.

```text
Mẫu ghi nhanh — Bullish OB (Long)
HTF bias: Bullish
HTF OB: H4 bullish OB tại [vùng giá] (nến giảm cuối trước bullish displacement)
Location: Discount của D1-H4 range
Sweep trước OB: SSL tại [level] đã bị quét ngay trước OB
Imbalance: bullish FVG để lại phía trên OB
Mean Threshold (50%): [mức 50% thân OB]
Expected path: giá retrace mitigate OB tại discount → bullish reaction → target BSL [level]
Invalidation: giá đóng nến mạnh xuyên dưới đáy OB và không reclaim
```

```text
Mẫu ghi nhanh — Bearish OB (Short)
HTF bias: Bearish
HTF OB: H4 bearish OB tại [vùng giá] (nến tăng cuối trước bearish displacement)
Location: Premium của D1-H4 range
Sweep trước OB: BSL tại [level] đã bị quét ngay trước OB
Imbalance: bearish FVG để lại phía dưới OB
Mean Threshold (50%): [mức 50% thân OB]
Expected path: giá retrace mitigate OB tại premium → bearish reaction → target SSL [level]
Invalidation: giá đóng nến mạnh xuyên trên đỉnh OB và không reclaim
```

### H1 / M15 — POI & Context
- **OB đang quan sát:** ghi vùng giá cụ thể và timeframe, ví dụ `H1 bearish OB 1.0xxx–1.0xxx`.
- **OB hợp lệ không?** OB có gắn displacement không? Có để lại FVG không? Có sweep trước nó không? Còn unmitigated không? Đúng premium/discount không?
- **OB là low- hay high-resistance?** đồng hướng HTF delivery → low-resistance, ưu tiên. Ngược dòng → high-resistance, cẩn trọng.
- **Mean Threshold:** xác định mức 50% của OB để biết vùng vào lệnh và đánh giá phản ứng.
- **Phân biệt OB vs breaker:** nếu OB cũ đã bị phá rồi giá flip qua, nó là [[Breaker Block]], không phải OB còn vai trò.

### M5 / M1 — Confirmation & Entry
- **Giá đã chạm OB / Mean Threshold chưa?** ưu tiên reaction tại OB hoặc 50% OB.
- **Có MSS/displacement xác nhận trên LTF không?** khi giá chạm OB, lý tưởng có bullish/bearish MSS + displacement nhỏ để confirm.
- **Có FVG đi kèm để refine entry không?** combine OB với FVG bên trong để vào lệnh chặt hơn.
- **Entry & stop:** entry tại OB / Mean Threshold / FVG đi kèm; stop qua đầu kia của OB hoặc qua điểm sweep; target là liquidity.

> [!warning]
> **OB nhỏ trên M1/M5 không “tạo” bias.** Một LTF OB chỉ là điểm execution sau khi HTF narrative + location + liquidity sweep đã đúng bối cảnh. Không vẽ OB rồi vào lệnh tách rời khỏi context.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

![[Order-Block-Sec-05-Xac-Nhan.svg|720]]
*Sơ đồ: Phân biệt mitigation sạch (OB giữ vai trò) với OB đã fail (đóng thân + acceptance) → chuyển thành Breaker Block.*

### Setup được xem là hợp lệ khi
- [ ] OB gắn với displacement phá BOS/MSS và để lại imbalance.
- [ ] Có liquidity sweep ngay trước OB (đúng thứ tự: sweep → displacement → OB).
- [ ] OB còn unmitigated khi giá quay lại, hoặc mitigation lần đầu sạch sẽ.
- [ ] OB nằm đúng premium (cho Short) / discount (cho Long) và đồng hướng Daily Bias.
- [ ] Giá phản ứng tại OB / Mean Threshold với LTF MSS + displacement.
- [ ] Entry tại OB/Mean Threshold/FVG; stop qua đầu kia OB hoặc qua điểm sweep.
- [ ] Target là liquidity còn mở; R:R đạt tối thiểu trong plan.

### Setup bị vô hiệu khi
- [ ] Giá đóng nến mạnh xuyên qua đầu kia OB và **giữ acceptance** ngoài vùng → OB đã fail.
- [ ] Không có displacement / không phá cấu trúc sau OB → OB chỉ là vùng cung/cầu thường.
- [ ] OB hình thành mà chưa có liquidity sweep trước đó.
- [ ] OB ở giữa range hoặc sai phía premium/discount.
- [ ] Giá chỉ chạm OB nhưng không có LTF confirmation; vào lệnh “mù”.
- [ ] OB đã chuyển thành breaker (đã fail rồi flip) nhưng vẫn bị đọc như OB còn vai trò.
- [ ] HTF target đã được delivered và cấu trúc đổi hướng — OB cũ không còn ý nghĩa.

### Phân biệt “mitigate sạch” vs “OB đã fail (breaker)”

| Quan sát | Cách đọc hợp lý |
|---|---|
| Giá retrace vào OB / Mean Threshold, để lại wick, rồi reject với displacement ngược | OB còn vai trò; mitigation hợp lệ, tìm entry |
| Giá đóng thân nến xuyên qua đầu kia OB, giữ giá ngoài vùng, pullback không reclaim | OB **fail** → có thể đảo vai trò thành [[Breaker Block]]; ngừng đọc như OB |
| Giá chạm OB lần đầu (unmitigated) và phản ứng rõ | Phản ứng “tươi”, giá trị cao nhất |
| Giá đã vào OB nhiều lần, mỗi lần phản ứng yếu dần | OB suy yếu; phản ứng kế tiếp kém tin cậy |
| Giá phá OB rồi quay lại test mặt ngoài OB từ phía bên kia | Đây là dấu hiệu breaker flip, không phải mitigation OB |

> [!important]
> **OB giữ vai trò ≠ Breaker đã fail.** Một OB bị phá thân + acceptance đã “chết” với vai trò cũ; nếu giá flip qua nó và test lại từ phía ngược, hãy xử lý như [[Breaker Block]].

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish OB tại discount sau SSL sweep, Long
![[Order-Block-Example-Correct.png]]

**Mô tả:**  
HTF bias Bullish, draw on liquidity lên BSL phía trên. Giá retrace vào discount của dealing range, quét SSL dưới một đáy ngắn hạn. Ngay sau sweep, nến giảm cuối cùng (bullish OB) bị một đợt bullish displacement đẩy lên phá swing high nội bộ (BOS) và để lại bullish FVG. Giá sau đó quay lại mitigate OB / Mean Threshold; M5 cho bullish MSS + displacement. Entry tại OB/FVG; stop qua đáy OB (qua điểm sweep); target BSL.

**Vì sao đây là ví dụ tốt:**
- OB có đủ narrative: sweep SSL → displacement → imbalance → BOS.
- OB unmitigated, low-resistance, đúng discount, đồng hướng bias.
- Entry tại Mean Threshold/FVG; stop logic qua đầu kia OB.
- Target là liquidity rõ ràng, không phải TP tùy ý.

### Ví dụ sai / dễ nhầm — Long mọi “nến lớn cuối cùng” không có displacement
![[Order-Block-Example-Wrong.png]]

**Mô tả lỗi:**  
Trader thấy một nến giảm lớn rồi đánh dấu là “bullish OB” và Long ngay khi giá chạm lại. Nhưng nến đó **không gây ra displacement**, không phá cấu trúc, không có sweep trước nó, không để lại FVG. Đó chỉ là một vùng supply/demand thường giữa range. Giá xuyên thẳng qua “OB” và tiếp tục giảm.

**Bài học:**
- OB của ICT **bắt buộc có narrative** (sweep + displacement + imbalance), không chỉ là “nến lớn cuối cùng”.
- Không có displacement + không phá cấu trúc = không phải OB hợp lệ.
- Hãy hỏi: “OB này đã quét liquidity nào và phá cấu trúc gì? Còn unmitigated không? Đúng location không?”

---
### Sequence mẫu — Long từ Bullish OB
```text
HTF Bullish Bias (Daily Bias)
→ Giá về Discount của Dealing Range
→ Sweep Sell-Side Liquidity (đáy ngắn hạn / equal lows)
→ Bullish Displacement phá swing high nội bộ (BOS/MSS) + để lại FVG
→ Xác định Bullish OB = nến giảm cuối trước displacement
→ Giá retrace mitigate OB / Mean Threshold (50%)
→ Refine entry tại OB + FVG đi kèm (M5/M1)
→ Stop qua đáy OB / qua điểm sweep
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short từ Bearish OB
```text
HTF Bearish Bias (Daily Bias)
→ Giá về Premium của Dealing Range
→ Sweep Buy-Side Liquidity (đỉnh ngắn hạn / equal highs)
→ Bearish Displacement phá swing low nội bộ (BOS/MSS) + để lại FVG
→ Xác định Bearish OB = nến tăng cuối trước displacement
→ Giá retrace mitigate OB / Mean Threshold (50%)
→ Refine entry tại OB + FVG đi kèm (M5/M1)
→ Stop qua đỉnh OB / qua điểm sweep
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> OB và FVG thường đi cùng nhau: displacement vừa tạo OB ở gốc vừa để lại FVG ở thân đợt đẩy. Entry chất lượng cao là vùng **OB chồng lấp FVG** (confluence), với Mean Threshold làm mốc tinh chỉnh. Đây cũng là vùng OTE thường rơi vào (xem [[Optimal Trade Entry]]).

---

## 7. Râu hay thân? & Các kịch bản giá quay về OB

> [!summary] Chốt nhanh
> **Vẽ vùng OB bằng CẢ RÂU (high–low) để biết ranh giới sống–chết, nhưng canh entry quanh CE 50% (Mean Threshold) và đặt stop qua đáy/đỉnh râu.** OB chỉ thực sự “chết” khi có nến **đóng cửa thân** xuyên qua — râu chọc qua chưa phải là vô hiệu hóa.

### 7.1. Xác định OB bằng râu nến hay thân nến?

Đây là tranh luận kinh điển, và câu trả lời của ICT không phải “chọn một” mà là **dùng cả cây nến để vẽ vùng, rồi lấy mốc 50% (CE) làm điểm tham chiếu quan trọng nhất**.

**Trường phái tính CẢ RÂU (high → low).** Đây là định nghĩa gốc, an toàn về mặt “không bỏ sót”. Toàn bộ phạm vi từ đỉnh râu tới đáy râu là vùng OB.
- *Ưu điểm:* bao trọn mọi lệnh còn sót trong cây nến; khó bị giá “xuyên qua trong gang tấc rồi chạy” mà mình lỡ mất.
- *Nhược điểm:* vùng rộng → stop xa hơn → R:R thấp hơn nếu vào ở biên proximal.

**Trường phái tính THÂN (open → close).** Cho vùng gọn, entry đẹp, stop chặt; lập luận rằng thân là nơi “khối lượng thực” tập trung, râu chỉ là dấu vết của sự từ chối giá.
- *Ưu điểm:* R:R tốt, entry sắc, đặc biệt hợp OB khung nhỏ (M5/M1).
- *Nhược điểm:* giá có thể quét sâu vào râu (dưới thân) rồi mới quay đầu → dễ bị stop-out non dù ý tưởng đúng.

**Điểm hòa giải — thứ ICT thực sự nhấn mạnh: CE / Mean Threshold = mốc 50% của CẢ cây nến (tính râu).** Phản ứng mạnh và đáng tin nhất thường xảy ra quanh mốc 50% này, không phải ở biên trên hay biên dưới (xem [[Consequent Encroachment (Mean Threshold)]]). Vì vậy công thức thực dụng nhất:

> [!tip] Cách vẽ OB thực dụng
> 1. **Vẽ vùng bằng cả râu** (high–low) → biết ranh giới proximal / distal.
> 2. **Canh entry quanh CE 50%** → điểm xác suất cao nhất, cân bằng R:R.
> 3. **Đặt stop qua đáy râu (Bullish) / đỉnh râu (Bearish)** → không bị quét non.
> 4. **Ưu tiên chỗ OB chồng lấp FVG** ([[Fair Value Gap]]) → vùng “refined” cho R:R tốt nhất, thay vì tranh cãi râu/thân.

**Ảnh hưởng của khung thời gian:** OB khung lớn (H4/H1) nên tính cả râu vì mỗi nến chứa nhiều thông tin; OB khung nhỏ (M5/M1) có thể tinh chỉnh theo thân hoặc theo FVG bên trong để entry sắc hơn.

### 7.2. Các kịch bản giá quay về OB (mitigation scenarios)

![[Order-Block-Mitigation-Scenarios.svg|720]]

*Hình: Phổ kịch bản giá quay về Bullish OB — từ A (touch &amp; go, mạnh nhất) đến D (đóng thân xuyên, chết) và E (fail → Breaker).*

Khi giá quay lại OB, có một phổ kịch bản từ mạnh đến yếu. Đọc đúng kịch bản quyết định vào lệnh kiểu gì và khi nào phải bỏ. (Mô tả dưới đây lấy Bullish OB làm ví dụ; Bearish OB đảo chiều tương ứng.)

| Kịch bản | Hành vi giá tại OB | Cách đọc & hành động |
|---|---|---|
| **A. Touch & go (biên proximal)** | Vừa chạm đỉnh thân OB là bật ngay, không đi sâu | OB rất mạnh, thường sau displacement cực mạnh + OB còn tươi. Entry *aggressive*, nhưng chưa có xác nhận → dễ dính chạm giả |
| **B. Về đúng CE 50% rồi bật** | Lấp một nửa OB, chạm Mean Threshold rồi từ chối | **Entry sách giáo khoa** — R:R cân bằng, xác suất cao, stop dưới đáy râu hợp lý. Ưu tiên số một |
| **C. Lấp gần trọn tới biên distal** | Đi sâu tới sát đáy râu rồi mới quay đầu | “Phòng tuyến cuối” — OB còn hiệu lực *chừng nào chưa đóng cửa dưới đáy râu*. Hạ kỳ vọng, cần thêm LTF confirmation (một MSS con) trước khi vào |
| **D. Đóng cửa xuyên qua OB** | Nến đóng **thân** dưới đáy OB + giữ acceptance | **Invalidation** — OB đã chết. Bỏ ý tưởng, không gồng, không dời stop |
| **E. OB fail → Breaker** | OB bị phá rồi giá bật lại test từ phía ngược | Vùng flip vai trò thành [[Breaker Block]]. Chỉ vào khi cấu trúc đã xác nhận đảo chiều — đừng “trả thù” thị trường |

> [!warning] Ranh giới sống–chết của OB
> **Râu chọc qua = chưa chết; thân đóng cửa qua + acceptance = đã chết.** Đây chính là chỗ phân biệt *mitigation* (giá về test rồi tôn trọng OB) với *violation* (giá phá vỡ OB). Luôn xét theo **đóng cửa thân**, không phải chỉ vì một cái râu chọc qua.

**Hai lưu ý xuyên suốt mọi kịch bản:**
- **First touch mạnh hơn second touch.** OB test lần đầu (unmitigated) đáng tin nhất; mỗi lần bị chạm lại là mỗi lần yếu đi vì thanh khoản dần cạn.
- **Luôn đọc bias khung lớn.** Chỉ mua ở Bullish OB khi HTF đang tăng hoặc giá ở vùng discount; tránh bắt OB ngược xu hướng lớn.

> [!example] Ví dụ minh họa (NAS100)
> Phiên Á quét thanh khoản đáy (SSL) → tạo Bullish OB M5 → sang phiên London giá chỉ chạm nhẹ đỉnh thân OB rồi bốc thẳng (kịch bản A): người chờ CE 50% sẽ lỡ tàu. Ngược lại nếu giá lấp về đúng 50% OB rồi mới bật (kịch bản B), đó là entry lý tưởng với stop gọn dưới đáy râu.

### 7.3. Kiến thức nâng cao — "Block Family": OB và các biến thể

OB không đứng một mình. ICT có cả một **họ "block"**, và đọc nhầm loại block là đọc nhầm vai trò của vùng giá:

![[Order-Block-Advanced-Block-Family.svg]]

| Block | Định nghĩa ngắn | Khác OB ở điểm nào | Cách dùng |
|---|---|---|---|
| **Order Block** | Nến/cụm nến ngược hướng cuối trước displacement | — (chuẩn gốc) | POI entry sau retrace |
| **[[Breaker Block]]** | OB đã **fail** (đóng thân xuyên + acceptance) rồi flip vai trò | OB còn vai trò vs block đã đổi phe | Entry theo hướng MỚI khi giá retest từ phía ngược |
| **[[22 - Mitigation Block]]** | Giống breaker nhưng swing tạo nó **không sweep liquidity** (failure swing — không lấy được đỉnh/đáy cũ) | Breaker có sweep, mitigation không | Yếu hơn breaker; cần thêm confluence |
| **Propulsion Block** | Nến test/respect một OB cũ rồi tự tạo displacement mới — "OB sinh trong OB" | Được "tiếp lửa" bởi OB gốc | Momentum mạnh hơn OB thường; entry chặt, stop gọn |
| **[[28 - Rejection Block]]** | Vùng **wick dài** tại đỉnh/đáy sau khi thân nến bị xuyên | Dùng râu nến làm zone thay vì thân | Bắt reversal tại extreme sau sweep |
| **[[34 - Vacuum Block]]** | Gap sự kiện (liquidity vacuum) hai bên không giao dịch | Không phải nến ngược hướng, là khoảng trống | Mức tham chiếu rebalance |
| **Reclaimed OB** | OB bị vi phạm **ngắn hạn** (quét qua) rồi được giành lại ngay bằng displacement | Khác breaker: không có acceptance bền | OB "tái sinh" — thường rất mạnh vì đã sweep sâu thêm liquidity |

> [!important] Câu hỏi phân loại bắt buộc
> Khi giá phá qua một OB, đừng vội bỏ nó. Hỏi: **có acceptance không?** Đóng thân + giữ giá ngoài → Breaker (flip). Chỉ quét qua bằng wick/1 nến rồi displacement giành lại ngay → Reclaimed OB (còn nguyên vai trò, thậm chí mạnh hơn). Hai kết luận này cho hai lệnh NGƯỢC chiều nhau.

### 7.4. Kiến thức nâng cao — Qualification & Refinement

**Chuỗi nến ngược hướng & mức Open.** Định nghĩa đầy đủ của ICT không phải "một nến" mà là **chuỗi nến ngược hướng cuối cùng** (series of down-close candles cho bullish OB). Khi có chuỗi: lấy từ open của nến đầu chuỗi (hoặc nến có body cao nhất/thấp nhất tùy hướng). Mức tinh nhất trong OB là **opening price của nến OB** — thuật toán thường trả giá về đúng open đó trước khi đẩy. Thứ tự mức tham chiếu từ thô tới tinh: `zone cả râu → Mean Threshold 50% → open của nến OB`.

**OB tại origin của leg > OB giữa leg.** OB hình thành ngay tại swing point (điểm xuất phát của cả leg, nơi có sweep) là "true origin" — chất lượng cao nhất. OB hình thành giữa một leg đang chạy chỉ là trạm dừng, dễ bị xuyên khi leg kiệt sức.

**OB tự sweep liquidity = chất lượng cao nhất.** Kịch bản lý tưởng: chính **wick của nến OB** là cây quét liquidity (đáy nến giảm cuối cùng chọc xuống dưới equal lows rồi displacement lên). Khi đó sweep + OB + displacement cùng nằm trong 1–2 nến — narrative nén lại cực gọn, stop cực logic (dưới wick sweep).

**Nesting HTF → LTF.** Không entry trực tiếp tại H4 OB với stop H4. Quy trình refine: H4 OB xác định vùng → chờ giá vào vùng → tìm M15/M5 OB hoặc FVG **bên trong** H4 OB sau LTF MSS → entry theo LTF block, stop theo LTF block. Được cả hai: xác suất của HTF + R:R của LTF.

**Phản ứng đúng nghĩa phải NHANH.** OB chất lượng cho phản ứng ngay lần chạm đầu (vài nến LTF). Giá **lình xình bên trong** OB nhiều nến, đóng nến sâu dần qua Mean Threshold = lệnh trong block đang bị hấp thụ → xác suất flip thành breaker tăng mạnh. Thời gian giá ở trong OB tỉ lệ nghịch với chất lượng phản ứng.

### 7.5. Best Practices — Order Block

> [!success] Best Practices
> 1. **Định nghĩa trước, vẽ sau.** Chỉ vẽ OB khi trả lời được 3 câu: sweep nào ngay trước? displacement nào theo sau? cấu trúc nào bị phá? Thiếu 1 trong 3 → chỉ là nến lớn, không vẽ.
> 2. **Một OB = 3 mức.** Luôn đánh dấu đủ: mép proximal, Mean Threshold (50%), open của nến OB. Entry mặc định quanh Mean Threshold; kỳ vọng phản ứng tinh tại open.
> 3. **Ưu tiên tổ hợp "vàng":** unmitigated + low-resistance + đúng premium/discount + tự sweep liquidity + để lại FVG. Tổ hợp này hiếm — nhưng đó chính là lý do nó có edge.
> 4. **Refine HTF OB bằng LTF block.** Stop đặt theo cấu trúc LTF bên trong (sau khi có LTF MSS), không đặt stop H4 cho lệnh vào bằng tín hiệu M5.
> 5. **Đếm thời gian trong block.** Đặt rule cứng: nếu giá đóng quá N nến (vd 3 nến M5) bên trong OB mà không bật, thoát/bỏ setup — đừng chờ "nó sẽ bật".
> 6. **Phân xử phá-OB bằng acceptance.** Wick xuyên = chưa chết; thân đóng + giữ ngoài = Breaker; quét qua rồi giành lại ngay = Reclaimed. Ghi rõ kết luận vào journal thay vì cảm giác.
> 7. **Log để kiểm chứng:** `ob_swept_liquidity_itself`, `ob_origin_of_leg`, `time_in_block`, `entry_level` (edge/MT/open), `ob_with_fvg` — thống kê sau 30+ mẫu trước khi đổi rule.
> 8. **Không "trung thành" với OB cũ.** Mỗi lần external liquidity của range bị lấy hoặc BOS ngược xuất hiện, quét lại toàn bộ OB đã vẽ: cái nào mất context thì xóa. Chart sạch = quyết định sạch.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy một Order Block
> Khái niệm ICT chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**. Một OB tách khỏi sweep + displacement + location chỉ là một vùng giá vô nghĩa.

### A. Context (HTF)
- [ ] Daily Bias rõ ràng (Bullish / Bearish / Neutral) và OB đồng hướng bias.
- [ ] Xác định HTF dealing range và OB nằm đúng premium (Short) / discount (Long).
- [ ] OB là low-resistance (thuận dòng lệnh chính), không phải high-resistance.
- [ ] OB gắn với displacement đã phá BOS/MSS có ý nghĩa.
- [ ] OB còn unmitigated (hoặc mitigation lần đầu).
- [ ] Có draw on liquidity rõ làm target sau khi OB phản ứng.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã chạm OB / Mean Threshold (50%).
- [ ] Có liquidity sweep hợp lý trước OB (đúng thứ tự sweep → displacement → OB).
- [ ] Có FVG/imbalance đi kèm để refine entry.
- [ ] Có LTF MSS + displacement xác nhận phản ứng tại OB.
- [ ] Entry tại OB / Mean Threshold / FVG, không chase.
- [ ] Stop qua đầu kia của OB hoặc qua điểm sweep (stop loss logic).
- [ ] Target là liquidity còn mở; R:R đạt tối thiểu plan.

### C. Quy tắc “không có lệnh”
- [ ] OB không có displacement / không phá cấu trúc → không trade.
- [ ] Không có sweep trước OB → không trade.
- [ ] OB ở giữa range / sai premium-discount → không trade.
- [ ] OB đã fail (breaker) → không đọc như OB, không trade theo vai trò cũ.
- [ ] OB high-resistance ngược bias mà không có counter-trend playbook → không trade.

---

## 9. Lỗi thường gặp

![[Order-Block-Common-Mistakes.svg|720]]

*Hình: Đối chiếu lỗi kinh điển (vẽ OB ở nến lớn cô lập, giá xuyên thẳng qua) với OB đúng (đủ narrative: sweep → displacement → BOS + FVG).*

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Vẽ OB ở mọi nến lớn | Đánh dấu OB khắp chart, không cần displacement | Phần lớn “OB” đó không có edge; biến thành supply/demand thường | Chỉ vẽ OB là nến ngược hướng cuối trước displacement phá cấu trúc |
| OB không có displacement | Vào lệnh tại nến lớn cô lập | Không có narrative; giá xuyên qua dễ dàng | Yêu cầu displacement + BOS/MSS + imbalance theo sau |
| Bỏ qua liquidity sweep | OB tạo giữa không trung, chưa quét gì | Stop nằm đúng nơi market còn muốn quét | Ưu tiên OB hình thành ngay sau sweep đỉnh/đáy |
| Sai premium/discount | Long từ bullish OB nằm ở premium | Mua đắt / bán rẻ, R:R xấu, xác suất thấp | Long OB ở discount, Short OB ở premium theo dealing range |
| Trade OB ngược bias | OB high-resistance bắt dao ngược trend | Target ngược hướng ít room, xác suất thấp | Ưu tiên low-resistance OB đồng hướng Daily Bias |
| Nhầm OB với breaker | OB đã bị phá thân vẫn đọc như OB | Vai trò đã flip; phản ứng sẽ ngược kỳ vọng | Phân biệt OB (giữ vai trò) vs [[Breaker Block]] (đã fail rồi flip) |
| Dùng OB đã mitigate nhiều lần | Quay lại OB cũ đã bị test nhiều | Phản ứng yếu dần; lệnh đặt trễ thường thua | Ưu tiên OB unmitigated; bỏ OB đã bị xuyên nhiều |
| Bỏ qua Mean Threshold | Vào ở rìa OB, stop quá rộng | Không có mốc 50% để tinh chỉnh entry/stop | Dùng Mean Threshold (50%) làm mốc vào lệnh và đánh giá phản ứng |
| Vào lệnh không có LTF confirmation | Chạm OB là vào ngay | Giá có thể xuyên qua trước khi phản ứng | Chờ LTF MSS + displacement tại OB rồi mới vào |
| Chase sau khi giá rời OB | Vào lệnh khi giá đã chạy xa OB | R:R xấu, vào lúc gần hết move | Chờ retrace về OB/FVG hoặc bỏ qua |

---

## 10. Câu hỏi tự kiểm tra

- Mình có thể giải thích định nghĩa OB (nến ngược hướng cuối trước displacement) trong 30 giây không?
- OB này có gắn với displacement phá BOS/MSS và để lại imbalance không?
- Có liquidity sweep ngay trước OB không, đúng thứ tự sweep → displacement → OB?
- OB còn unmitigated hay đã bị lấp? Nó còn “tươi” không?
- Mean Threshold (50%) của OB này nằm ở đâu?
- OB này low-resistance hay high-resistance so với HTF bias?
- OB nằm đúng premium (Short) / discount (Long) của dealing range chưa?
- Đây là OB còn vai trò hay đã fail (breaker)?
- Entry, stop (qua đầu kia OB / điểm sweep) và target liquidity của mình ở đâu?
- Mình đang dùng OB như một mắt xích trong sequence, hay đang “bắt” mọi OB?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Order Block là gì?  
**Đáp:** Là nến (hoặc cụm nến) ngược hướng cuối cùng ngay trước một đợt displacement phá cấu trúc. Bullish OB = nến giảm cuối trước đợt tăng (demand); Bearish OB = nến tăng cuối trước đợt giảm (supply).

### Q2
**Hỏi:** Điều gì khiến một OB của ICT KHÁC vùng supply/demand thường?  
**Đáp:** OB của ICT bắt buộc có narrative: (1) displacement mạnh sau đó, (2) lý tưởng có liquidity sweep ngay trước, (3) để lại FVG/imbalance, (4) gây ra BOS/MSS. Không chỉ là “nến lớn cuối cùng”.

### Q3
**Hỏi:** Mean Threshold (Open / 50%) của OB là gì và dùng để làm gì?  
**Đáp:** Là mức 50% thân (hoặc range) của OB. Đây là mốc quan trọng để vào lệnh và đánh giá chất lượng phản ứng của giá tại OB.

### Q4
**Hỏi:** Mitigation là gì, và OB unmitigated khác mitigated thế nào?  
**Đáp:** Mitigation là khi giá quay lại “lấp lệnh” OB — đây là điểm entry. OB unmitigated (chưa bị lấp lần nào) có giá trị cao hơn OB đã mitigated, vì phản ứng “tươi” hơn.

### Q5
**Hỏi:** Phân biệt low-resistance OB và high-resistance OB?  
**Đáp:** Low-resistance OB đi thuận dòng lệnh chính (ít cản, xác suất cao hơn); high-resistance OB đi ngược dòng lệnh chính (nhiều cản, xác suất thấp). Ưu tiên low-resistance đồng hướng bias.

### Q6
**Hỏi:** Khi nào một OB trở thành Breaker Block?  
**Đáp:** Khi OB bị phá/fail (giá đóng thân xuyên qua + acceptance) rồi đảo vai trò. OB giữ vai trò ≠ breaker đã fail rồi flip. Khi OB fail, hãy xử lý nó như [[Breaker Block]], không đọc như OB cũ.

### Q7
**Hỏi:** Đặt entry, stop và target ở đâu với một OB hợp lệ?  
**Đáp:** Entry tại OB / Mean Threshold / FVG đi kèm; stop qua đầu kia của OB (hoặc qua điểm sweep); target là liquidity còn mở.

---
## 12. Lesson Learned

### Bài học chính
- OB chỉ là một **mắt xích trong sequence**, không phải tín hiệu độc lập: bias → location → sweep → displacement → OB/FVG entry.
- OB của ICT **bắt buộc có narrative**; “nến lớn cuối cùng” không có displacement/sweep/imbalance chỉ là supply/demand thường.
- OB unmitigated, low-resistance, đúng premium/discount, sau sweep là tổ hợp chất lượng cao nhất.
- Mean Threshold (50%) là mốc tinh chỉnh entry và đánh giá phản ứng — đừng vào ở rìa OB với stop quá rộng.
- Phải phân biệt OB còn vai trò vs breaker đã fail; đọc nhầm dẫn tới vào lệnh ngược.
- Chất lượng OB phải đo bằng trade journal và backtest, không bằng vài lệnh thắng/thua gần đây.

### Quy tắc cá nhân rút ra
- [ ] Tôi không vẽ OB nếu không có displacement phá cấu trúc theo sau.
- [ ] Tôi chỉ dùng OB sau khi liquidity đã bị quét đúng thứ tự (sweep → displacement → OB).
- [ ] Tôi chỉ Long OB ở discount, Short OB ở premium, đồng hướng Daily Bias.
- [ ] Tôi ưu tiên OB unmitigated, low-resistance; bỏ OB đã bị xuyên thân nhiều lần.
- [ ] Tôi dùng Mean Threshold (50%) làm mốc entry; stop qua đầu kia OB / điểm sweep.
- [ ] Khi OB bị phá thân + acceptance, tôi chuyển sang đọc nó như [[Breaker Block]], không bám vai trò cũ.

### Câu nhắc nhở khi trade
> **“Một OB không có sweep, không có displacement, không phá cấu trúc — chỉ là một cái nến. Đừng bắt mọi OB; chỉ vào tại OB đúng location, sau sweep, đồng hướng bias.”**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt OB của ICT vs supply/demand thường không? |
| Nhận diện trên chart |  | Có xác định đúng nến ngược hướng cuối + displacement + Mean Threshold không? |
| Biết khi nào bỏ qua |  | Có dám bỏ OB không có sweep/displacement hoặc sai location không? |
| Kết hợp với context HTF |  | OB có được dùng đồng hướng Daily Bias và đúng premium/discount không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự tại OB/Mean Threshold sau sweep + LTF confirmation không? |
| Review sau trade |  | Có phân biệt được OB mitigation hợp lệ vs OB đã fail (breaker) không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Order Block]]`.
- [ ] Review riêng `unmitigated vs mitigated`, `low- vs high-resistance`, `có sweep vs không sweep`.
- [ ] Thống kê win rate, average R, lỗi lặp lại theo `ob_resistance` và `ob_location`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.
