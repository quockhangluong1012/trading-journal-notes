---
type: ict-concept
concept: "Inducement"
aliases:
  - IDM
  - Inducement
  - Engineered Liquidity
tags:
  - trading/ict/concept
  - trading/study
  - "#Inducement"
status: developing
category: Liquidity
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
  - "[[Mistake - Entry Before Liquidity Sweep]]"
  - "[[Mistake - Trade Inducement As POI]]"
---

# Inducement

> [!summary] Tóm tắt 1 câu
> **Inducement (IDM) là thanh khoản "mồi" được engineer (cố ý tạo ra) — một swing nhỏ hoặc pool đỉnh/đáy lộ liễu nằm NGAY TRƯỚC POI thật (Order Block / FVG), dùng để dụ retail vào lệnh sớm và cung cấp đúng lượng thanh khoản mà smart money cần để khớp lệnh trước khi giá chạm POI thật.**

> [!important] Nguyên tắc cốt lõi
> **IDM là thanh khoản phải bị LẤY TRƯỚC khi giá tới POI thật. Một POI hợp lệ gần như luôn có inducement nằm phía trước nó (đáy nhỏ dưới một bullish OB, đỉnh nhỏ trên một bearish OB). Nếu bạn không thấy IDM, hãy nghi ngờ chính cái POI đó.**
> Vào lệnh TẠI vùng IDM = bạn chính là thanh khoản. Smart money quét stop của bạn rồi mới đẩy giá tới POI thật.

---

## 1. Định nghĩa

**Khái niệm:**  
Inducement (IDM) là **thanh khoản được tạo ra có chủ đích (engineered liquidity)** đặt giữa giá hiện tại và POI thật. Nó thường là một **swing nhỏ** (minor swing high/low) hoặc một **pool đỉnh/đáy lộ liễu** mà số đông trader nhìn vào sẽ coi là điểm vào lệnh hợp lý hoặc điểm đặt stop loss. Chính vì "ai cũng thấy", nó tích tụ một cụm lệnh chờ (pending orders + stop losses) — và cụm lệnh đó là nhiên liệu để smart money khớp các vị thế lớn của họ.

- **IDM trước một bullish POI:** một **đáy nhỏ (minor low / SSL)** nằm phía trên Order Block tăng. Giá phải quét đáy nhỏ này (lấy [[30 - Sell-side Liquidity]]) TRƯỚC khi chạm OB và đảo chiều lên.
- **IDM trước một bearish POI:** một **đỉnh nhỏ (minor high / BSL)** nằm phía dưới Order Block giảm. Giá phải quét đỉnh nhỏ này (lấy [[07 - Buy-side Liquidity]]) TRƯỚC khi chạm OB và đảo chiều xuống.

**Bản chất:** Inducement là một dạng [[19 - Liquidity]] đặc biệt — không phải thanh khoản ở cực range (external), mà là thanh khoản **trung gian, gần POI**, được "trưng ra" như mồi nhử. Logic ICT: thị trường là một thuật toán tìm thanh khoản. Trước khi đưa giá tới một vùng OB/FVG nơi smart money muốn khớp lệnh, thuật toán phải **gom đủ counterparty** — và IDM chính là counterparty đó. Đáy/đỉnh nhỏ bị quét là "phí vào cửa" mà giá phải trả trước khi tới POI thật.

**Phân biệt cốt lõi — IDM vs POI:**
- **IDM** = nơi retail BỊ DỤ vào lệnh / đặt stop. Giá đến đây để **lấy** thanh khoản, KHÔNG để đảo chiều.
- **POI thật** (OB/FVG) = nơi smart money thực sự khớp lệnh và đảo chiều. Giá đến đây **sau khi** đã lấy IDM.

**Mục đích trong ICT:**  
- **Xác thực một POI:** một OB/FVG có IDM phía trước thì đáng tin hơn nhiều so với một POI "trần" không có mồi. IDM là dấu hiệu vùng đó đã được engineer.
- **Lọc thời điểm vào lệnh:** chỉ vào lệnh SAU khi IDM bị quét, không vào tại IDM. Đây là bộ lọc chống "vào sớm".
- **Định vị stop loss:** stop logic thường nằm ngoài đầu kia của POI (sau khi IDM đã được quét), không nằm tại IDM.
- **Đọc narrative:** thấy IDM giúp bạn biết giá còn "một nhịp quét" nữa trước khi tới POI — tránh FOMO vào lệnh quá sớm.

**Vì sao khái niệm này quan trọng:**  
IDM là lý do số 1 khiến trader "đúng hướng nhưng vẫn thua": họ nhìn đúng POI, đúng bias, nhưng vào lệnh tại đáy/đỉnh nhỏ (IDM) ngay trước POI và bị quét stop trong gang tấc trước khi giá đảo. Hiểu IDM biến một loss thành một entry kiên nhẫn đúng chỗ.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đã lấy thanh khoản mồi (IDM) trước POI chưa, hay tôi đang định vào TẠI cái mồi?
- POI này có hợp lệ không (có IDM phía trước để xác thực không)?
- Còn một nhịp quét nữa trước khi giá đảo, hay đảo ngay bây giờ?
- Đâu là thanh khoản thật smart money nhắm tới, đâu chỉ là bẫy trung gian?

### Inducement không phải là gì
- Không phải là một structural sweep ở cực range — IDM là thanh khoản trung gian, nhỏ, gần POI.
- Không phải điểm để vào lệnh — nó là điểm để **chờ bị quét xong** rồi mới vào tại POI.
- Không phải mọi đáy/đỉnh nhỏ đều là IDM — chỉ những cái nằm logic giữa giá và một POI hợp lệ.
- Không phải tín hiệu đảo chiều — giá lấy IDM rồi thường tiếp tục tới POI mới đảo.
- Không thay thế cho POI — IDM xác thực POI, nó không phải bản thân điểm khớp lệnh.

---

## 2. Bối cảnh sử dụng

### Các dạng / trạng thái của Inducement

| Dạng IDM | Vị trí | Loại liquidity bị lấy | Ý nghĩa thực chiến |
|---|---|---|---|
| **IDM dưới bullish OB** | Đáy nhỏ phía trên OB tăng | [[30 - Sell-side Liquidity]] (SSL) | Phải quét đáy nhỏ trước → rồi chạm OB → Long |
| **IDM trên bearish OB** | Đỉnh nhỏ phía dưới OB giảm | [[07 - Buy-side Liquidity]] (BSL) | Phải quét đỉnh nhỏ trước → rồi chạm OB → Short |
| **IDM kiểu equal highs/lows** | Cặp đỉnh/đáy bằng nhau lộ liễu trước POI | BSL / SSL cụm dày | Mồi rất "ngon mắt" → càng dễ là bẫy |
| **IDM trong leg (pullback nhỏ)** | Một pullback nhỏ giữa một displacement leg | Stop của counter-trend | Lấy thanh khoản nhỏ trước khi continuation |

> [!tip]
> Quy tắc ngón tay cái của nhiều trader theo IDM: **"Mọi POI hợp lệ đều có inducement phía trước nó."** Khi quét một OB/FVG để vào lệnh, hãy hỏi: *đâu là đáy/đỉnh nhỏ mà giá sẽ lấy trước khi chạm POI này?* Nếu không tìm được IDM, POI có thể chưa "chín" hoặc bạn đang nhìn sai vùng.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có [[12 - Daily Bias]] rõ ràng và một POI HTF (OB/FVG) đồng hướng.
- [ ] Giữa giá hiện tại và POI có một swing nhỏ / pool đỉnh-đáy lộ liễu (IDM tiềm năng).
- [ ] Giá đang trong [[27 - Premium Discount|premium/discount]] phù hợp với hướng trade.
- [ ] IDM nằm logic (đáy nhỏ trên bullish OB / đỉnh nhỏ dưới bearish OB).
- [ ] Có thời điểm phù hợp: London / New York Kill Zone.
- [ ] Có liquidity target external rõ ràng phía bên kia làm draw.

### Khi nào nên bỏ qua?
- [ ] Không xác định được POI thật — chỉ thấy một đáy/đỉnh nhỏ đơn lẻ.
- [ ] Giá đang ở giữa range, không rõ premium/discount.
- [ ] Không có HTF narrative / bias.
- [ ] "IDM" thực ra là một structural sweep ở cực range (đó là external liquidity, đọc khác).
- [ ] Tín hiệu ngoài kill zone, ngoài plan session.
- [ ] Bạn đang muốn vào TẠI đáy/đỉnh nhỏ vì sợ lỡ sóng (FOMO) — đó chính là tâm lý mà IDM khai thác.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Một POI thật** (OB/FVG) HTF đồng hướng bias, đúng premium/discount.
2. **Một swing nhỏ / pool lộ liễu** nằm GIỮA giá hiện tại và POI thật — đây là IDM.
3. **IDM "ngon mắt":** đáy/đỉnh rõ, dễ nhận, nhiều khả năng cụm stop loss + pending orders.
4. **Khoảng cách:** IDM nằm GẦN POI (cùng leg), không phải ở cực range đối diện.
5. **Logic hướng:** IDM dưới bullish OB là một đáy nhỏ; IDM trên bearish OB là một đỉnh nhỏ.

### Phân biệt Inducement vs Structural Sweep (cốt lõi)

| Tiêu chí | Inducement (IDM) | Genuine Structural Sweep |
|---|---|---|
| **Vị trí** | Thanh khoản trung gian, gần POI | Thanh khoản ở cực range (external high/low) |
| **Quy mô swing** | Swing nhỏ / minor | Swing lớn, có ý nghĩa cấu trúc |
| **Vai trò** | Mồi nhử để gom liquidity trước POI | Điểm giá thực sự lấy thanh khoản chính rồi đảo |
| **Đảo chiều?** | Không đảo tại IDM — đảo tại POI sau đó | Có thể đảo ngay sau sweep (đi kèm MSS) |
| **Hệ quả entry** | Vào TẠI đây = bị quét | Sweep này thường là điều kiện entry hợp lệ |

### Điều kiện bắt buộc
- [ ] Xác định được POI thật trước (OB/FVG hợp lệ).
- [ ] Xác định được IDM nằm giữa giá và POI đó.
- [ ] IDM là thanh khoản trung gian, không phải external liquidity ở cực range.
- [ ] Xác định loại liquidity bị lấy (SSL cho bullish setup / BSL cho bearish setup).

### Điều kiện tăng xác suất
- [ ] IDM là cặp equal highs/lows lộ liễu (mồi càng "ngon" càng đáng tin là bẫy).
- [ ] POI phía sau IDM là một OB/FVG có displacement tạo ra.
- [ ] Có liquidity sweep IDM rồi mới có displacement / [[21 - Market Structure Shift|MSS]] tại POI.
- [ ] Entry nằm đúng premium/discount.
- [ ] Có external liquidity rõ ràng làm target sau khi đảo từ POI.

### Điều kiện làm setup yếu đi
- IDM mơ hồ, không rõ là đáy/đỉnh nào.
- Không có POI thật phía sau — chỉ có IDM trơ trọi.
- IDM nằm quá xa POI, không cùng một leg.
- Giá đã lấy IDM nhưng không có phản ứng nào tại POI (POI có thể fail).

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Inducement
> 1. **POI thật của tôi nằm ở đâu (OB/FVG nào)?**
> 2. **Giữa giá hiện tại và POI đó, đâu là IDM (đáy/đỉnh nhỏ giá sẽ lấy trước)?**
> 3. **Tôi có đang định vào lệnh TẠI IDM thay vì chờ nó bị quét không?**
> 4. **Sau khi IDM bị quét và giá chạm POI, đâu là tín hiệu xác nhận (MSS) để tôi vào?**

### D1 / H4 — Bias & Narrative
- Bias hiện tại: Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- Giá đang trong dealing range nào? Ở premium hay discount?
- POI HTF quan trọng (OB/FVG) làm điểm đảo dự kiến.
- External liquidity target (BSL/SSL chính) làm draw.

### H1 / M15 — POI & Inducement
- **POI cụ thể:** ghi rõ vùng OB/FVG và biên của nó.
- **IDM cụ thể:** xác định đáy/đỉnh nhỏ nằm trước POI, ví dụ `IDM = đáy nhỏ 1.0840 nằm trên bullish OB 1.0810–1.0825`.
- **Lý do POI hợp lệ:** có IDM phía trước để xác thực không? POI có sinh từ displacement không?
- **Phân biệt:** cái mình thấy là IDM (trung gian) hay là external sweep ở cực range?

### M5 / M1 — Confirmation & Entry
- Giá đã quét IDM chưa? (bắt buộc trước khi vào).
- Sau khi quét IDM, giá có chạm POI và phản ứng không?
- Có [[21 - Market Structure Shift|MSS]] tại POI sau khi IDM bị lấy không?
- Có displacement + [[Fair Value Gap|FVG]] LTF để refine entry không?

```text
Mẫu ghi nhanh — Bullish setup với IDM
HTF Bias: Bullish | Location: Discount
Draw on liquidity: BSL tại [level]
POI: H1 bullish OB [low]–[high]
IDM: đáy nhỏ (SSL) tại [level] nằm TRÊN OB
Kế hoạch: chờ giá quét đáy nhỏ IDM → chạm OB → M5 bullish MSS + FVG → entry
Stop: dưới low của OB (sau khi IDM đã bị quét)
Target: internal liquidity trước, BSL chính sau
Invalid: giá đóng nến xuyên thủng dưới OB mà không phản ứng
```

```text
Mẫu ghi nhanh — Bearish setup với IDM
HTF Bias: Bearish | Location: Premium
Draw on liquidity: SSL tại [level]
POI: H1 bearish OB [low]–[high]
IDM: đỉnh nhỏ (BSL) tại [level] nằm DƯỚI OB
Kế hoạch: chờ giá quét đỉnh nhỏ IDM → chạm OB → M5 bearish MSS + FVG → entry
Stop: trên high của OB (sau khi IDM đã bị quét)
Target: internal liquidity trước, SSL chính sau
Invalid: giá đóng nến xuyên thủng trên OB mà không phản ứng
```

> [!warning]
> **Một đáy/đỉnh nhỏ trên LTF không tự nó là tín hiệu.** Nó chỉ có nghĩa khi nằm logic GIỮA giá và một POI HTF hợp lệ. Đừng biến mọi minor swing thành "IDM" để hợp lý hóa việc vào lệnh sớm.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Có POI HTF hợp lệ đồng hướng bias.
- [ ] Có IDM nằm logic giữa giá và POI (đáy nhỏ dưới bullish OB / đỉnh nhỏ trên bearish OB).
- [ ] Giá **đã quét IDM** (lấy thanh khoản mồi) TRƯỚC khi chạm POI.
- [ ] Giá phản ứng tại POI (reject) với displacement / MSS LTF.
- [ ] Entry SAU khi IDM bị quét, không phải tại IDM.
- [ ] Có target external liquidity rõ ràng, R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Giá đóng nến xuyên thủng POI mà không phản ứng (POI fail).
- [ ] Cái "IDM" thực ra là external sweep ở cực range — narrative khác hẳn.
- [ ] Vào lệnh TẠI IDM trước khi nó bị quét → bị stop hunt.
- [ ] Không có POI thật phía sau IDM.
- [ ] Giá lấy IDM nhưng không có phản ứng nào tại POI trong kill zone dự kiến.

### So sánh: Inducement đã quét vs chưa quét

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Giá CHƯA chạm IDM, đã muốn vào tại đáy/đỉnh nhỏ | Vào sớm | Sai — bạn đang là thanh khoản; chờ IDM bị quét |
| Giá vừa quét IDM, đang tiến tới POI | Đang setup | Chờ giá chạm POI + xác nhận LTF |
| Giá quét IDM xong, chạm POI, có MSS LTF | Hợp lệ | Entry refined tại POI sau MSS |
| Giá quét IDM, chạm POI nhưng đóng nến xuyên qua | POI fail | Bỏ; có thể chuyển sang đọc IFVG / POI sâu hơn |

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Inducement-Example-Correct.svg]]

**Mô tả:**  
HTF bullish, draw là BSL phía trên. Giá retrace vào discount. Trên đường xuống, một **đáy nhỏ (IDM / SSL)** hình thành phía trên một bullish Order Block. Giá quét đáy nhỏ này (lấy thanh khoản mồi) RỒI mới chạm OB thật. Tại OB, một displacement tăng tạo MSS bullish. Entry nằm tại OB **sau khi** IDM đã bị quét; stop dưới low OB; target là BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- IDM (đáy nhỏ) bị quét **trước** khi giá tới POI thật — đúng trình tự.
- Entry tại OB, KHÔNG tại IDM → tránh stop hunt.
- POI được xác thực bởi sự có mặt của IDM phía trước.
- Có displacement + MSS xác nhận tại POI; target là external liquidity rõ ràng.

### Ví dụ sai / dễ nhầm
![[Inducement-Example-Wrong.svg]]

**Mô tả lỗi:**  
Trader thấy một đáy nhỏ và nhầm nó là Order Block / điểm đảo, vào Long ngay TẠI đáy nhỏ (IDM). Nhưng đáy nhỏ này chỉ là mồi: giá xuyên thẳng qua nó, quét stop loss của trader, rồi mới tiếp tục xuống chạm OB thật phía dưới và bật từ đó — quá muộn. Lệnh Long bị quét stop ngay trước khi giá thực sự đảo.

**Bài học:**
- IDM là nơi để **chờ bị quét**, không phải nơi để vào lệnh.
- Vào tại IDM = tự biến mình thành thanh khoản cho smart money.
- Luôn xác định POI thật và để giá lấy IDM xong rồi mới hành động.

---
### Sequence mẫu — Long với IDM trước bullish OB
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Xác định bullish OB (POI thật) ở discount
→ Xác định IDM = đáy nhỏ (SSL) nằm TRÊN OB
→ Giá QUÉT IDM (lấy thanh khoản mồi)
→ Giá chạm OB thật → displacement tăng → MSS bullish
→ M5/M1 FVG refined
→ Entry tại OB (sau khi IDM bị quét); Stop dưới low OB
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short với IDM trước bearish OB
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Xác định bearish OB (POI thật) ở premium
→ Xác định IDM = đỉnh nhỏ (BSL) nằm DƯỚI OB
→ Giá QUÉT IDM (lấy thanh khoản mồi)
→ Giá chạm OB thật → displacement giảm → MSS bearish
→ M5/M1 FVG refined
→ Entry tại OB (sau khi IDM bị quét); Stop trên high OB
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> IDM ghép cực kỳ tự nhiên với [[Order Block]] và [[Fair Value Gap]]: chuỗi chuẩn là **IDM (mồi) bị quét → POI (OB/FVG) phản ứng → MSS xác nhận → entry**. Thiếu bước "IDM bị quét", entry tại POI thường non.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Một đáy/đỉnh nhỏ chỉ là IDM khi nằm đúng **context + giữa giá và một POI HTF hợp lệ + đúng liquidity narrative**.

### A. Context (HTF)
- [ ] Daily Bias rõ: `Bullish / Bearish / Neutral`.
- [ ] Có POI HTF hợp lệ (OB/FVG) đồng hướng bias.
- [ ] POI đúng premium (Short) / discount (Long).
- [ ] Có external liquidity target rõ ràng làm draw.
- [ ] Xác định được IDM nằm GIỮA giá và POI.
- [ ] Phân biệt chắc IDM (trung gian) khác external sweep (cực range).

### B. Execution (LTF)
- [ ] Giá đã **quét IDM** trước khi chạm POI.
- [ ] Giá chạm POI và phản ứng (reject), không đóng nến xuyên qua.
- [ ] Có MSS + displacement LTF tại POI sau khi IDM bị lấy.
- [ ] Entry SAU khi IDM bị quét — không vào tại IDM.
- [ ] Stop logic: ngoài đầu kia của POI (sau sweep IDM).
- [ ] R:R tối thiểu đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Chưa quét IDM → không trade.
- [ ] Không có POI thật phía sau IDM → không trade.
- [ ] "IDM" thực ra là external sweep ở cực range → đọc lại narrative, không trade theo IDM.
- [ ] Vào TẠI IDM vì FOMO → tuyệt đối không.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Vào lệnh TẠI vùng IDM | Vào ở đáy/đỉnh nhỏ ngay trước POI | Bạn thành thanh khoản; bị quét stop | Chờ IDM bị quét, vào tại POI thật |
| Nhầm IDM là POI | Coi đáy/đỉnh nhỏ là OB/điểm đảo | Đảo chiều xảy ra tại POI, không tại IDM | Luôn xác định POI thật trước khi xét IDM |
| Bỏ qua IDM | Vào POI mà không chờ mồi bị lấy | Entry non, dễ bị nhịp quét cuối | Đợi IDM bị quét rồi mới vào POI |
| Biến mọi minor swing thành "IDM" | Gọi bất kỳ đáy/đỉnh nào là inducement | Hợp lý hóa entry sai | IDM phải nằm logic giữa giá và một POI hợp lệ |
| Nhầm IDM với structural sweep | Coi external sweep ở cực range là IDM | Narrative ngược; target sai | Phân biệt thanh khoản trung gian vs external |
| Đặt stop tại IDM | Stop nằm ở chính đáy/đỉnh mồi | Đúng nơi market còn muốn quét | Đặt stop ngoài đầu kia POI sau khi IDM bị lấy |
| FOMO khi thấy giá gần IDM | Sợ lỡ sóng nên vào trước sweep | Tâm lý mà IDM được thiết kế để khai thác | Nhắc bản thân: mồi là để chờ, không để vào |

---

## 10. Câu hỏi tự kiểm tra

- Mình giải thích được IDM khác POI trong 30 giây không?
- POI thật của setup này ở đâu, và IDM nằm ở đâu so với nó?
- Mình đang định vào TẠI IDM hay chờ nó bị quét?
- IDM này là thanh khoản trung gian hay là external sweep ở cực range?
- Loại liquidity bị lấy ở IDM là SSL hay BSL?
- Nếu giá chưa quét IDM, điều kiện "No Trade" của mình là gì?
- Stop loss của mình có vô tình nằm tại IDM không?
- Setup nào trong journal mình từng vào sớm tại IDM và bị quét?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Inducement (IDM) là gì?  
**Đáp:** Là thanh khoản "mồi" được tạo có chủ đích (engineered) — một swing nhỏ / pool lộ liễu nằm GIỮA giá và POI thật, dùng để dụ retail vào sớm và cung cấp counterparty cho smart money trước khi giá chạm POI.

### Q2
**Hỏi:** Tại sao KHÔNG được vào lệnh tại IDM?  
**Đáp:** Vì IDM là nơi giá đến để LẤY thanh khoản, không phải để đảo chiều. Vào tại IDM = trở thành thanh khoản, bị quét stop trước khi giá tới POI thật.

### Q3
**Hỏi:** Làm sao IDM xác thực một POI?  
**Đáp:** Một POI (OB/FVG) hợp lệ gần như luôn có inducement phía trước (đáy nhỏ dưới bullish OB / đỉnh nhỏ trên bearish OB). Có IDM = vùng đó đã được engineer → POI đáng tin hơn.

### Q4
**Hỏi:** Phân biệt Inducement với một structural sweep thật?  
**Đáp:** IDM là thanh khoản trung gian nhỏ, gần POI, là mồi nhử (không đảo tại đó). Structural sweep lấy thanh khoản chính ở cực range và thường đảo ngay sau đó (đi kèm MSS).

### Q5
**Hỏi:** Trình tự đúng để trade một POI có IDM?  
**Đáp:** IDM bị quét (lấy mồi) → giá chạm POI → MSS + displacement xác nhận → entry tại POI sau khi IDM đã bị lấy.

### Q6
**Hỏi:** Stop loss nên đặt ở đâu trong setup có IDM?  
**Đáp:** Ngoài đầu kia của POI (sau khi IDM đã bị quét), KHÔNG đặt tại IDM — vì IDM chính là nơi market còn muốn quét.

---

## 12. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "03 - Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
idm_present: true # có inducement trước POI không
idm_type: SSL # SSL (dưới bullish OB) | BSL (trên bearish OB)
idm_level: 1.0840 # mức đáy/đỉnh nhỏ làm mồi
idm_swept_before_entry: true # IDM đã bị quét TRƯỚC khi vào lệnh chưa
poi_type: OB # OB | FVG — POI thật phía sau IDM
entry_after_idm: true # entry sau khi IDM bị quét (true) hay tại IDM (false)
```

> [!tip]
> Sau 30–50 lệnh, so sánh: lệnh `entry_after_idm: true` vs `false`. Mục tiêu là kiểm chứng bằng dữ liệu rằng kiên nhẫn chờ IDM bị quét (thay vì vào tại IDM) thực sự cải thiện win rate và R trung bình của bạn.

---

## 13. Lesson Learned

### Bài học chính
- IDM là **mồi**, không phải điểm vào — nơi để chờ bị quét, rồi mới vào tại POI thật.
- Vào TẠI IDM = tự nguyện làm thanh khoản cho smart money.
- Một POI hợp lệ gần như luôn có inducement phía trước — dùng IDM để xác thực POI.
- Trình tự bất di bất dịch: **IDM bị quét → POI phản ứng → MSS → entry**.
- Phân biệt IDM (trung gian) với external sweep (cực range) là kỹ năng đọc narrative cốt lõi.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn xác định POI thật TRƯỚC, rồi mới tìm IDM nằm giữa giá và POI.
- [ ] Tôi không bao giờ vào lệnh tại IDM khi nó chưa bị quét.
- [ ] Tôi đặt stop ngoài đầu kia của POI, không bao giờ tại IDM.
- [ ] Khi không tìm thấy IDM trước một POI, tôi nghi ngờ chính POI đó.
- [ ] Khi sợ lỡ sóng và muốn vào sớm, tôi nhắc mình: "mồi là để chờ".

### Câu nhắc nhở khi trade
> **"Đáy/đỉnh nhỏ trước POI là mồi nhử — tôi chờ nó bị quét, tôi không phải là thanh khoản."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt được IDM vs POI vs external sweep không? |
| Nhận diện trên chart |  | Tìm đúng IDM nằm giữa giá và POI không? |
| Biết khi nào bỏ qua |  | Có dám không-trade khi IDM chưa bị quét không? |
| Kết hợp với context HTF |  | IDM có được đặt trong narrative bias + premium/discount không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra SAU khi IDM bị quét không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập 20–30 setup gắn tag `[[Inducement]]`.
- [ ] Review riêng: lệnh vào sau khi IDM bị quét vs vào tại IDM.
- [ ] Thống kê win rate / R theo `idm_swept_before_entry`.

---

## Appendix — Inducement Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**  
> **Daily Bias:** Bullish / Bearish / Neutral  
> **POI thật (OB/FVG) & vùng:** ____  
> **IDM type:** SSL (dưới bullish OB) / BSL (trên bearish OB)  
> **IDM level (đáy/đỉnh mồi):**  
> **IDM nằm giữa giá và POI?** Yes / No  
> **Đây là IDM hay external sweep?** IDM / External  
> **Location:** Premium / Discount / Equilibrium  
> **Draw on liquidity / target:**  
> **Kế hoạch:** chờ quét IDM → chạm POI → MSS → entry  
> **Entry plan (tại POI, sau khi IDM bị quét):**  
> **Stop logic (ngoài đầu kia POI):**  
> **Invalidation (đóng nến xuyên POI tại):**  
> **Kill zone permitted:** London / NY AM / NY PM  
> **No-trade condition:** IDM chưa bị quét / không có POI thật
