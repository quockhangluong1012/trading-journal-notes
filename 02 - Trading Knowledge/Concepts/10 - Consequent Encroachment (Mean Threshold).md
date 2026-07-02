---
type: ict-concept
concept: "Consequent Encroachment"
aliases:
  - CE
  - Mean Threshold
  - Consequent Encroachment
tags:
  - trading/ict/concept
  - trading/study
  - "#CE"
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
  - "[[Mistake - Trade Every FVG]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
---

# Consequent Encroachment

> [!summary] Tóm tắt 1 câu
> **Consequent Encroachment (CE) — còn gọi Mean Threshold — là mức 50% (trung điểm) chính xác của một FVG / gap / PD array; đây là mức phản ứng quan trọng nhất bên trong array: giá tôn trọng CE = array còn hiệu lực, còn một cú đóng nến vượt qua CE là cảnh báo array sắp bị lấp / vô hiệu.**

> [!important] Nguyên tắc cốt lõi
> **CE KHÔNG phải là tín hiệu trade — nó là mức tinh chỉnh entry và là "thước đo sức khỏe" của một PD array.**
> Entry quanh CE cho R:R đẹp hơn mép array. Nhưng CE chỉ có giá trị khi array đó vốn đã hợp lệ (sinh từ displacement, đúng bias, đúng premium/discount, sau sweep). CE của một array rác vẫn là rác.

---

## 1. Định nghĩa

**Khái niệm:**
Consequent Encroachment là **mức 50% chính xác** của một vùng PD array — thường là một [[Fair Value Gap]], nhưng cũng áp dụng cho gap, [[Order Block]], liquidity void hay [[03 - Balanced Price Range]]. Tên gọi khác là **Mean Threshold (ngưỡng trung bình)**: nó là "đường trung tâm" của array.

Cách tính cơ bản: lấy **high và low của vùng array**, CE = (high + low) / 2. Với một bullish FVG có high (= low nến 3) và low (= high nến 1), CE nằm đúng giữa hai mức đó.

ICT coi CE là **mức phản ứng quan trọng nhất** bên trong array vì:
- Giá thường chỉ cần retrace tới CE (không cần lấp hết array) là đã đủ để "rebalance" tâm lý và tiếp tục delivery.
- CE chia array thành nửa **premium nội bộ** (trên CE) và nửa **discount nội bộ** (dưới CE) — giúp định vị entry tinh hơn.
- Phản ứng tại CE cho biết array đang **respect** (còn hiệu lực) hay sắp bị **xuyên thủng** (invalid).

**Mục đích trong ICT:**
- **Tinh chỉnh entry (entry refinement):** thay vì vào ở mép xa array, vào quanh CE để cải thiện R:R và đặt stop gọn hơn.
- **Đo respect/invalidation:** giá đóng nến vượt CE theo hướng lấp array là tín hiệu cảnh báo sớm.
- **Định premium/discount nội bộ** của chính array.
- **Confluence:** khi CE của một FVG trùng với CE/mép của một array khác (OB, equilibrium, [[Optimal Trade Entry]]) → điểm vào mạnh.

**Vì sao khái niệm này quan trọng:**
CE là "bí mật" giúp entry ICT sắc hơn. Nhiều trader vào ở mép gap (full gap entry) và chịu R:R kém; vào quanh CE thường cho cùng hướng nhưng stop nhỏ hơn → R:R lớn hơn. CE cũng là tiêu chí khách quan để phân biệt một array đang được tôn trọng với một array sắp hỏng — gắn chặt với cách đọc [[Fair Value Gap]] và [[17 - Inverse Fair Value Gap - iFVG]].

**Nó giúp trả lời câu hỏi nào trên chart?**
- Mức nào bên trong array là điểm phản ứng / entry tối ưu?
- Array này còn được tôn trọng (giá reject ở CE) hay sắp hỏng (đóng nến vượt CE)?
- Entry của mình đang ở premium hay discount nội bộ của array?
- Có confluence nào tại CE để tăng xác suất không?

### Consequent Encroachment không phải là gì
- Không phải tín hiệu trade độc lập — chỉ là mức tinh chỉnh trong một array hợp lệ.
- Không phải lúc nào giá cũng dừng đúng tại CE; nó là vùng phản ứng kỳ vọng, cần xác nhận LTF.
- Không thay thế bias / sweep / premium-discount — CE chỉ dùng SAU khi array đã hợp lệ.
- Không phải mép array; nhầm CE với mép gây sai stop/entry.
- CE bị xuyên (đóng nến) không có nghĩa lập tức đảo lệnh, nhưng là cảnh báo nghiêm túc.

---

## 2. Bối cảnh sử dụng

### CE áp dụng cho những array nào

| Array | Cách tính CE | Ý nghĩa CE |
|---|---|---|
| **FVG (BISI/SIBI)** | (FVG high + FVG low) / 2 | Mức phản ứng & entry tối ưu nhất trong gap |
| **Order Block** | (OB high + OB low) / 2 | Trung điểm OB; refine entry thay vì vào nguyên OB |
| **Liquidity Void** | (void high + void low) / 2 | Vùng giữa của khoảng trống lớn |
| **Balanced Price Range** | (BPR high + BPR low) / 2 | Tâm của vùng BPR |
| **New Week Opening Gap** | (gap high + gap low) / 2 | Mức 50% của gap đầu tuần |

> [!tip]
> CE đặc biệt mạnh khi **trùng** với một mức tham chiếu khác: equilibrium của dealing range, mức 0.705 của [[Optimal Trade Entry]], mép một OB, hoặc CE của một FVG ở khung lớn hơn. CE-on-CE giữa hai khung (vd CE của H1 FVG trùng CE của M15 FVG) là confluence rất đáng giá.

### Khi nào khái niệm này có giá trị cao?
- [ ] Array gốc đã hợp lệ (sinh từ displacement, đúng bias, đúng premium/discount, sau sweep).
- [ ] Giá đang retrace về array và cần điểm entry tinh.
- [ ] CE trùng một mức tham chiếu khác (OB, equilibrium, OTE, CE khung khác).
- [ ] Muốn cải thiện R:R bằng entry sâu hơn mép gap.
- [ ] Cần một tiêu chí khách quan để theo dõi respect/invalidation của array.

### Khi nào nên bỏ qua?
- [ ] Array gốc đã rác (không displacement / giữa range / ngược bias) — CE của nó vô nghĩa.
- [ ] Giá đang chạy momentum mạnh, chưa retrace tới array.
- [ ] Array quá nhỏ, CE và mép gần như trùng → không thêm giá trị.
- [ ] Chưa có sweep / chưa có context — đừng dùng CE như cớ để vào sớm.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Xác định array hợp lệ trước:** FVG/OB/void... sinh từ displacement, đúng context.
2. **Lấy high & low của array:** xác định chính xác hai biên.
3. **Vẽ mức 50%:** CE = trung điểm; nhiều platform có sẵn công cụ FVG hiển thị CE.
4. **Quan sát phản ứng tại CE:** giá chạm CE rồi reject (respect) hay đóng nến xuyên qua (cảnh báo).

### Điều kiện bắt buộc
- [ ] Array gốc đã được xác nhận hợp lệ (không tính CE của array rác).
- [ ] Xác định đúng high/low của array để CE chính xác.
- [ ] Biết CE đang chia array thành premium/discount nội bộ nào.

### Điều kiện tăng xác suất
- [ ] CE trùng equilibrium của dealing range.
- [ ] CE trùng mức [[Optimal Trade Entry]] (vd 0.705).
- [ ] CE trùng mép / CE của một array khác (OB, FVG khung lớn).
- [ ] Có LTF MSS + displacement khi giá phản ứng tại CE.
- [ ] CE nằm đúng phía premium (Short) / discount (Long) của HTF.

### Điều kiện làm setup yếu đi
- Array gốc yếu (không displacement, giữa range).
- Array bị test nhiều lần, CE đã bị "ăn mòn".
- CE và mép array gần như trùng nhau (array quá hẹp).
- Không có xác nhận LTF khi giá tới CE — chỉ "rơi xuyên".

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng CE
> 1. **Array chứa CE này có HỢP LỆ không (displacement + bias + premium/discount + sweep)?**
> 2. **CE nằm ở đâu và có trùng mức tham chiếu nào khác không (confluence)?**
> 3. **Giá đang respect CE hay đã đóng nến xuyên qua CE?**
> 4. **Entry quanh CE có cải thiện R:R và cho stop logic gọn không?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **HTF array & CE:** có FVG/OB D1/H4 còn unmitigated mà CE của nó là draw/target không?
- **Premium/discount:** CE dùng Long phải ở discount; CE dùng Short phải ở premium của [[27 - Premium Discount]] HTF.

### H1 / M15 — POI & Context
- **POI cụ thể:** ghi rõ array và mức CE, ví dụ `H1 bullish FVG 1.0820–1.0835, CE = 1.08275`.
- **Lý do hợp lệ:** array sinh từ displacement? sau sweep? đúng phía premium/discount?
- **Confluence tại CE:** CE có trùng OB/equilibrium/OTE/CE khung khác không?
- **Respect vs xuyên:** giá chạm CE reject (respect) hay đóng nến vượt CE (cảnh báo).

### M5 / M1 — Confirmation & Entry
- **Có MSS không?** khi giá về CE, có MSS LTF xác nhận đảo hướng nội bộ không?
- **Có displacement LTF không?** thường tạo một FVG nhỏ ngay quanh CE để refine entry.
- **Entry tại CE:** ưu tiên đặt limit quanh CE thay vì mép xa array.
- **Stop logic:** ngoài mép xa của array / ngoài điểm sweep, KHÔNG đặt sát CE.

```text
Mẫu ghi nhanh — Long entry tại CE của Bullish FVG
HTF Bias: Bullish | Location: Discount
Array: H1 bullish FVG [low]–[high] (sinh từ displacement phá cấu trúc)
CE (50%): [mid]  | Confluence: trùng OB / equilibrium / OTE?
Sweep: đã quét SSL trước khi displacement → Yes
Entry plan: chờ giá retrace về CE → M5 bullish MSS + FVG nhỏ → entry quanh CE
Stop: dưới mép xa FVG / dưới sweep low (KHÔNG sát CE)
Target: internal liquidity trước, BSL chính sau
Invalid: đóng nến M5/H1 vượt CE theo hướng lấp gap → cảnh báo / bỏ
```

> [!warning]
> **CE không cho phép bỏ qua các bước trước.** Vào "tại CE" của một FVG ngược bias, giữa range, hay chưa sweep vẫn là một lệnh tồi — chỉ là tồi với R:R đẹp hơn một chút.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Array gốc hợp lệ (displacement + bias + premium/discount + sweep).
- [ ] Giá chạm CE và **respect** (reject với phản ứng), kèm LTF MSS/displacement.
- [ ] CE đúng phía premium (Short) / discount (Long).
- [ ] Có confluence tại CE (OB/equilibrium/OTE/CE khung khác).
- [ ] Stop đặt ngoài mép xa array, R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Giá **đóng nến vượt CE** theo hướng lấp array và giữ giá bên kia → cảnh báo array hỏng.
- [ ] Array gốc không hợp lệ — CE không cứu được.
- [ ] Không có LTF confirmation khi giá tới CE — chỉ "rơi xuyên".
- [ ] CE ở sai phía premium/discount cho hướng trade.
- [ ] Array đã bị test/ăn mòn nhiều lần.

### Đọc phản ứng quanh CE

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Giá chạm CE rồi reject với displacement ngược | **Respect CE** | Array còn khỏe; entry hợp lệ quanh CE + LTF confirm |
| Giá dừng trước CE (chưa tới 50%) rồi reject | **Shallow respect** | Array rất khỏe; có thể bỏ lỡ entry nếu chỉ đặt limit tại CE |
| Giá xuyên CE nhẹ rồi đóng nến quay lại trên CE | **Wick qua CE** | Vẫn respect; cảnh giác, chờ đóng nến xác nhận |
| Giá **đóng nến** vượt hẳn CE theo hướng lấp | **CE breach (cảnh báo)** | Array yếu đi; khả năng full fill / invalidation |
| Sau breach, giá lấp hết array & đóng nến xuyên | **Invalidation** | Array hỏng; cảnh giác đảo cực thành [[17 - Inverse Fair Value Gap - iFVG]] |

> [!note]
> Phân biệt **wick qua CE** và **close qua CE**. Một bóng nến chạm sâu hơn CE rồi đóng quay lại vẫn là respect (thậm chí là cú "stop hunt" quanh CE). Chỉ **đóng nến** giữ giá bên kia CE mới là cảnh báo thật.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Consequent-Encroachment-Example-Correct.svg]]

**Mô tả:**
Bias bullish, giá ở discount. Sau sweep SSL, một displacement tăng phá cấu trúc tạo bullish FVG hợp lệ. Giá retrace đúng về **CE (50%)** của FVG, để lại bóng nhẹ rồi đóng nến quay lên (respect CE), M5 tạo bullish MSS nhỏ. Entry đặt quanh CE; stop dưới mép xa FVG; giá tiếp tục delivery lên target BSL. Vào tại CE cho R:R tốt hơn nhiều so với vào ở mép trên gap.

**Vì sao đây là ví dụ tốt:**
- Array gốc hợp lệ (displacement + sweep + discount + đúng bias).
- Giá **respect CE** thay vì đóng nến xuyên qua.
- Entry quanh CE cải thiện R:R, stop gọn ngoài mép array.
- Có LTF confirmation (MSS) tại CE.

### Ví dụ sai / dễ nhầm
![[Consequent-Encroachment-Example-Wrong.svg]]

**Mô tả lỗi:**
Trader thấy bullish FVG và quyết Long quanh CE. Nhưng khi giá tới, nó **đóng nến vượt hẳn CE xuống dưới** (CE breach) — tín hiệu array đang hỏng. Thay vì tôn trọng cảnh báo, trader vẫn giữ/thêm lệnh Long "vì CE là hỗ trợ". Giá lấp toàn bộ FVG, đóng nến xuyên đáy gap (invalidation, đảo thành bearish IFVG) rồi tiếp tục xuống → stop out.

**Bài học:**
- **Đóng nến vượt CE = cảnh báo**, không phải cơ hội mua thêm.
- CE chỉ là mức tinh chỉnh trong một array còn hiệu lực; CE breach báo hiệu mất hiệu lực.
- Phân biệt rõ wick qua CE (vẫn respect) và close qua CE (cảnh báo invalid).

---
### Sequence mẫu — Long entry tại CE của Bullish FVG
```text
HTF Bullish Bias → Location Discount
→ Sweep Sell-Side Liquidity
→ Displacement tăng phá cấu trúc (BOS/MSS) → Bullish FVG hợp lệ
→ Xác định CE (50%) của FVG; kiểm tra confluence (OB/equilibrium/OTE)
→ Giá retrace về CE → respect (reject) + M5 MSS/FVG nhỏ
→ Entry quanh CE; Stop dưới mép xa FVG / dưới sweep low
→ Target: internal liquidity trước, External BSL sau
→ Invalid: đóng nến vượt CE theo hướng lấp gap → cảnh báo / bỏ
```

### Sequence mẫu — CE breach dẫn tới Inverse FVG
```text
Bullish FVG hợp lệ nhưng giá ĐÓNG NẾN vượt CE xuống (CE breach)
→ Tiếp tục lấp hết FVG & đóng nến xuyên đáy (invalidation)
→ Array đảo cực thành bearish IFVG (kháng cự)
→ Đồng hướng bias bearish mới + MSS bearish
→ Giá retrace lên test lại vùng IFVG (CE của IFVG là mức refine)
→ Short tại IFVG; Stop trên đỉnh IFVG; Target SSL
```

> [!note]
> CE là cây cầu nối giữa [[Fair Value Gap]] và [[Optimal Trade Entry]]: cả hai đều tìm cách vào sâu hơn để có R:R tốt. Trong nhiều setup, CE của FVG rơi gần vùng OTE 0.62–0.79 — khi chúng trùng nhau, đó là confluence rất mạnh.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> CE chỉ là mức tinh chỉnh entry trong một array ĐÃ hợp lệ. CE của array rác vẫn là rác.

### A. Context (HTF)
- [ ] Daily Bias rõ: `Bullish / Bearish / Neutral`.
- [ ] Array chứa CE sinh từ displacement phá cấu trúc.
- [ ] CE đúng phía premium (Short) / discount (Long) của dealing range.
- [ ] Đã có liquidity sweep trước khi array hình thành.
- [ ] Xác định chính xác high/low array → CE đúng.

### B. Execution (LTF / khi giá tới CE)
- [ ] Giá chạm CE và respect (reject), không đóng nến xuyên qua.
- [ ] Có LTF MSS + displacement khi giá tới CE.
- [ ] CE có confluence (OB/equilibrium/OTE/CE khung khác) — ưu tiên cao.
- [ ] Entry đặt quanh CE, không phải mép xa.
- [ ] Stop ngoài mép xa array / ngoài sweep, KHÔNG sát CE.
- [ ] R:R đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Array gốc không hợp lệ → không dùng CE.
- [ ] Giá đóng nến vượt CE theo hướng lấp → cảnh báo, không vào.
- [ ] Không có LTF confirmation tại CE → không vào.
- [ ] CE sai phía premium/discount → không vào.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Dùng CE của array rác | Tính CE cho FVG giữa range | CE không "phù phép" được array yếu | Xác nhận array hợp lệ trước khi tính CE |
| Nhầm CE với mép array | Đặt entry/stop sai chỗ | Stop quá sát hoặc entry sai vùng | CE = đúng 50% (high+low)/2 |
| Coi CE breach là cơ hội mua | Thêm lệnh khi đóng nến vượt CE | Array đang hỏng, dễ stop out | Đóng nến vượt CE = cảnh báo, dừng lại |
| Lẫn wick qua CE với close qua CE | Thoát/đảo lệnh vì bóng nến | Wick qua CE thường vẫn respect | Chỉ tính khi đóng nến giữ giá bên kia CE |
| Đặt stop sát CE | Stop ngay sau CE | Bị quét bởi nhiễu quanh 50% | Stop ngoài mép xa array / sweep |
| Bỏ qua confluence | Vào CE mà không kiểm tra OTE/OB | Bỏ lỡ điểm vào mạnh nhất | Ưu tiên CE trùng equilibrium/OTE/OB |
| Vào CE bất chấp bias | CE đẹp nhưng ngược Daily Bias | Xác suất thấp, target ngược hướng | Chỉ vào CE đồng hướng bias + đúng P/D |

---

## 10. Câu hỏi tự kiểm tra

- Mình giải thích CE = mức 50% (Mean Threshold) của array trong 30 giây không?
- Array chứa CE này có thực sự hợp lệ không, hay mình đang "cứu" một array rác?
- CE đang ở đâu, và có trùng confluence (OTE/equilibrium/OB) không?
- Giá đang **respect** CE hay đã **đóng nến xuyên** qua CE?
- Mình phân biệt được wick qua CE và close qua CE chưa?
- Entry quanh CE có thực sự cải thiện R:R và cho stop logic gọn không?
- CE này đang ở premium hay discount nội bộ của array, và của dealing range HTF?
- Setup nào trong journal đã vào tại CE đúng/sai?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Consequent Encroachment (CE) là gì? Còn gọi là gì?
**Đáp:** Là mức **50% chính xác (trung điểm)** của một FVG/gap/PD array, còn gọi là **Mean Threshold**. Tính bằng (high + low)/2 của array.

### Q2
**Hỏi:** Vì sao CE là mức quan trọng nhất bên trong một array?
**Đáp:** Vì giá thường chỉ cần retrace tới CE là đủ rebalance để tiếp tục delivery; CE còn là mức đo respect/invalidation và là điểm entry tinh cho R:R tốt hơn.

### Q3
**Hỏi:** Giá "respect CE" và "breach CE" khác nhau thế nào?
**Đáp:** Respect = giá chạm CE rồi reject (kể cả bóng nến xuyên rồi đóng quay lại). Breach = giá **đóng nến** vượt hẳn CE theo hướng lấp array và giữ giá bên kia → cảnh báo array sắp hỏng.

### Q4
**Hỏi:** CE giúp cải thiện entry như thế nào?
**Đáp:** Thay vì vào ở mép xa array (R:R kém), vào quanh CE cho cùng hướng nhưng stop gọn hơn → R:R lớn hơn; CE còn dùng để đặt limit chính xác.

### Q5
**Hỏi:** CE của một FVG giữa range, ngược bias có đáng trade không?
**Đáp:** Không. CE chỉ tinh chỉnh entry trong một array ĐÃ hợp lệ. Array rác thì CE của nó cũng vô nghĩa.

### Q6
**Hỏi:** CE liên quan gì tới OTE?
**Đáp:** CE thường rơi gần vùng [[Optimal Trade Entry]] (0.62–0.79). Khi CE của FVG trùng vùng OTE / equilibrium / OB, đó là confluence rất mạnh.

---

## 12. Lesson Learned

### Bài học chính
- CE = mức 50% (Mean Threshold) — mức phản ứng quan trọng nhất của array.
- CE là **mức tinh chỉnh entry**, không phải tín hiệu trade độc lập.
- Entry quanh CE cải thiện R:R; stop đặt ngoài mép xa array.
- **Đóng nến vượt CE** là cảnh báo array hỏng; phân biệt với wick qua CE.
- CE của một array rác vẫn vô giá trị — phải hợp lệ trước, refine sau.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ tính & dùng CE sau khi xác nhận array gốc hợp lệ.
- [ ] Tôi ưu tiên entry quanh CE và đặt stop ngoài mép xa array.
- [ ] Tôi coi đóng nến vượt CE là cảnh báo, không phải cớ mua thêm.
- [ ] Tôi tìm confluence tại CE (OTE/equilibrium/OB) trước khi vào.

### Câu nhắc nhở khi trade
> **"CE làm entry của tôi sắc hơn, không làm một setup tồi trở nên tốt. Đóng nến vượt CE = dừng lại."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có nắm CE = 50% (Mean Threshold) và vai trò refine không? |
| Nhận diện trên chart |  | Có vẽ đúng CE và phân biệt respect/breach không? |
| Biết khi nào bỏ qua |  | Có bỏ CE của array rác / khi CE breach không? |
| Kết hợp với context HTF |  | CE có dùng cùng bias + premium/discount + sweep không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra quanh CE với stop logic gọn không? |
| Review sau trade |  | Có so sánh at-ce vs edge bằng dữ liệu journal không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 lệnh có gắn tag `[[Consequent Encroachment]]`.
- [ ] So sánh R:R & win rate giữa entry at-ce và entry edge.
- [ ] Thống kê tỉ lệ array respect CE vs breach CE và hệ quả.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## Appendix — CE Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish / Neutral
> **Array type:** FVG / OB / BPR / void / NWOG
> **Array timeframe & range:** ____ , [low]–[high]
> **CE (50%):** ____ = (high + low) / 2
> **Array hợp lệ? (displacement + sweep + P/D)** Yes / No
> **CE confluence (OTE/equilibrium/OB/CE khung khác):**
> **Location:** Premium / Discount / Equilibrium
> **Entry plan (quanh CE):**
> **Stop logic (ngoài mép xa array):**
> **Respect vs breach (đóng nến vượt CE tại):**
> **Target / draw on liquidity:**
> **Kill zone permitted:** London / NY AM / NY PM
> **No-trade condition:** array rác / CE breach / không LTF confirm
