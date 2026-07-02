---
type: ict-concept
concept: Optimal Trade Entry
aliases:
  - OTE
  - Optimal Trade Entry
  - OTE Zone
tags:
  - trading/ict/concept
  - trading/study
  - "#OTE"
status: developing
category: Entry Model
timeframes:
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
  - "[[Mistake - Fib Without Structure]]"
  - "[[Mistake - Enter Shallow Retrace]]"
  - "[[Mistake - OTE Against Bias]]"
---

# Optimal Trade Entry (OTE)

> [!summary] Tóm tắt 1 câu
> **OTE là vùng entry tối ưu nằm trong khoảng retracement 62%–79% (Fibonacci) của một nhịp displacement vừa phá cấu trúc, nơi giá cho R:R đẹp nhất khi kết hợp với POI (FVG/OB) và đúng premium/discount.**

> [!important] Nguyên tắc cốt lõi
> **OTE chỉ hợp lệ khi fib được kéo trên một nhịp displacement đã phá cấu trúc (BOS/MSS) đúng hướng bias; kéo fib tùy tiện trên nhịp ngẫu nhiên rồi vào ở retrace nông là sai bản chất.**
> OTE không phải "cứ về 62–79% là vào" — nó là vùng để CHỜ confluence (POI + sweep + LTF confirm), không phải tín hiệu độc lập.

---

## 1. Định nghĩa

**Khái niệm:**
Optimal Trade Entry là một **vùng entry** xác định bằng Fibonacci retracement của một nhịp giá (leg) có ý nghĩa. Vùng OTE nằm giữa mức **62% và 79%** retracement, với **70.5%** thường được coi là "sweet spot". Ý tưởng: sau khi giá tạo một nhịp displacement mạnh (đẩy giá và phá cấu trúc), nó thường retrace về vùng discount/premium sâu trước khi tiếp tục — vùng 62–79% là nơi entry cho **rủi ro nhỏ nhất, phần thưởng lớn nhất**.

**Cách kéo Fibonacci đúng:**
- **Long:** kéo fib từ **đáy** (swing low, 100%) lên **đỉnh** của nhịp impulse (0%). Vùng OTE là 62–79% (tức gần đáy → discount sâu).
- **Short:** kéo fib từ **đỉnh** (swing high, 100%) xuống **đáy** của nhịp impulse (0%). Vùng OTE là 62–79% (tức gần đỉnh → premium sâu).
- Nhịp được kéo fib phải là nhịp **displacement đã phá cấu trúc** (BOS/MSS), không phải một nhịp ngẫu nhiên.

**Các mức Fibonacci quan trọng trong OTE:**
- **62%** — mép trên vùng OTE.
- **70.5%** — mức entry "vàng" (trung tâm vùng).
- **79%** — mép dưới vùng OTE (gần đầu nhịp nhất; nếu vượt 79–100% thì nghi nhịp đã fail).
- **50% (EQ / equilibrium)** — không thuộc OTE; entry tại 50% là retrace nông, R:R kém hơn.
- Các mức mở rộng **−0.27, −0.62** (hoặc 1.27, 1.62) dùng làm **target**.

**Mục đích trong ICT:**
- Là **execution model**: cách vào lệnh có hệ thống với R:R tối ưu, thay vì vào tùy hứng.
- Chuẩn hóa **stop & target**: stop ngoài 100% (đầu nhịp), target tại các mức mở rộng / liquidity.
- Buộc trader vào **discount cho Long / premium cho Short** một cách định lượng.
- Tạo confluence: OTE đẹp nhất khi 62–79% trùng với FVG/OB và đến SAU một liquidity sweep.

**Vì sao khái niệm này quan trọng:**
OTE biến "premium/discount" trừu tượng thành vùng giá cụ thể có thể đặt lệnh chờ. Nó cải thiện R:R đáng kể so với vào ở 50%/38%. Nhưng nó cũng là khái niệm bị **dùng sai** nhiều: trader kéo fib bừa lên mọi nhịp, vào ở retrace nông, hoặc OTE ngược bias — biến một công cụ R:R thành cái cớ để bắt dao rơi.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Sau displacement phá cấu trúc, vùng giá nào cho entry R:R tối ưu?
- Giá đã retrace đủ sâu (62–79%) hay mới chỉ về 38–50% (nông)?
- Vùng OTE có trùng FVG/OB và đúng premium/discount không?
- Stop logic (ngoài 100%) và target (mức mở rộng / liquidity) nằm ở đâu?

### OTE không phải là gì
- Không phải "kéo fib lên bất kỳ nhịp nào rồi vào 62–79%".
- Không phải tín hiệu độc lập — cần POI + đúng bias + (lý tưởng) sweep + LTF confirm.
- Không phải entry tại 50% hay 38% — đó là retrace nông, không phải OTE.
- Không phải lý do bắt đáy/đỉnh ngược xu hướng; OTE phải đồng hướng nhịp displacement.
- Không thay thế quản trị rủi ro — R:R đẹp chỉ có ý nghĩa nếu invalidation rõ ràng.

---

## 2. Bối cảnh sử dụng

### Các mức / thành phần của OTE

| Thành phần | Mức | Vai trò thực chiến |
|---|---|---|
| **0%** | Đầu nhịp (đỉnh cho Long / đáy cho Short) | Điểm bắt đầu retrace |
| **50% (EQ)** | Equilibrium | Ranh giới premium/discount; KHÔNG phải OTE |
| **62%** | Mép vào vùng OTE | Bắt đầu vùng entry tối ưu |
| **70.5%** | Sweet spot | Mức entry "vàng" của OTE |
| **79%** | Mép sâu vùng OTE | Entry sâu nhất; vượt qua → nghi nhịp fail |
| **100%** | Cuối nhịp (swing low/high) | Mốc stop loss logic (ngoài mức này) |
| **−0.27 / −0.62** | Mở rộng | Target lợi nhuận (cùng liquidity) |

> [!tip]
> OTE mạnh nhất là **OTE có confluence**: vùng 62–79% trùng với một **FVG hoặc OB**, đúng **discount/premium** của HTF, và xuất hiện **sau một liquidity sweep**. Khi cả ba cùng rơi vào vùng OTE, đó là entry chất lượng cao.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có một nhịp displacement vừa **phá cấu trúc** (BOS/MSS) đúng hướng bias để kéo fib.
- [ ] Vùng 62–79% trùng với **FVG/OB** (confluence POI).
- [ ] OTE nằm đúng **discount** (Long) / **premium** (Short) của HTF dealing range.
- [ ] OTE xuất hiện **sau liquidity sweep** đúng narrative.
- [ ] Có target liquidity rõ tại các mức mở rộng để R:R đạt kế hoạch.

### Khi nào nên bỏ qua?
- [ ] Fib kéo trên nhịp **không phá cấu trúc** / nhịp ngẫu nhiên.
- [ ] Giá chỉ retrace nông (38–50%) — chưa vào vùng OTE.
- [ ] OTE ngược Daily Bias / sai phía premium-discount.
- [ ] Vùng OTE không trùng POI nào, không có sweep trước đó.
- [ ] Giá đã vượt 79–100% (nhịp có khả năng đã fail / đảo).
- [ ] Ngoài kill zone / ngoài plan session.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Nhịp impulse hợp lệ:** một đoạn displacement phá cấu trúc — đây là nhịp để kéo fib (0%–100%).
2. **Hướng kéo đúng:** Long kéo từ đáy lên đỉnh; Short kéo từ đỉnh xuống đáy.
3. **Vùng 62–79%:** đánh dấu vùng OTE; xác định mức 70.5% làm trung tâm.
4. **Confluence:** kiểm tra FVG/OB có nằm trong vùng OTE không.
5. **Vị trí premium/discount:** vùng OTE phải nằm ở discount (Long) hoặc premium (Short).

### Ma trận nhận diện OTE

| Thành phần | OTE Long | OTE Short | Cảnh báo / OTE yếu |
|---|---|---|---|
| **Nhịp kéo fib** | Impulse tăng phá swing high (MSS) | Impulse giảm phá swing low (MSS) | Nhịp không phá cấu trúc |
| **Hướng fib** | Đáy (100%) → đỉnh (0%) | Đỉnh (100%) → đáy (0%) | Kéo sai chiều |
| **Vùng entry** | 62–79% (discount sâu) | 62–79% (premium sâu) | Vào ở 38–50% (nông) |
| **Confluence** | FVG/OB bullish trong vùng | FVG/OB bearish trong vùng | Không trùng POI nào |
| **Liquidity** | Sau sweep SSL | Sau sweep BSL | Chưa sweep |
| **Bias** | Đồng hướng bias bullish | Đồng hướng bias bearish | Ngược bias |

### Điều kiện bắt buộc
- [ ] Xác định đúng nhịp displacement phá cấu trúc để kéo fib.
- [ ] Kéo fib đúng chiều (đáy→đỉnh cho Long, đỉnh→đáy cho Short).
- [ ] Xác định vùng 62–79% và mức 70.5%.
- [ ] Xác định mốc 100% để đặt stop logic.

### Điều kiện tăng xác suất
- [ ] Vùng OTE trùng FVG/OB (confluence POI).
- [ ] OTE đúng discount (Long) / premium (Short).
- [ ] OTE xuất hiện sau liquidity sweep đúng hướng.
- [ ] Có MSS/displacement LTF khi giá chạm vùng OTE.
- [ ] Target liquidity rõ ở mức mở rộng; R:R ≥ kế hoạch.
- [ ] Trong kill zone phù hợp.

### Điều kiện làm setup yếu đi
- Nhịp kéo fib không phá cấu trúc rõ.
- Vùng OTE không trùng POI, không có sweep.
- Giá test vùng OTE nhiều lần, ăn mòn dần.
- OTE ngược bias hoặc giữa range.
- Giá đâm sâu quá 79% liên tục (nghi nhịp đã fail).

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng OTE
> 1. **Nhịp tôi kéo fib có phải displacement đã phá cấu trúc đúng hướng bias không?**
> 2. **Vùng 62–79% có trùng FVG/OB và đúng premium/discount không?**
> 3. **Đã có liquidity sweep trước nhịp này chưa?**
> 4. **Stop (ngoài 100%) và target (mức mở rộng/liquidity) ở đâu, R:R bao nhiêu?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **Draw on liquidity:** pool nào là target — sẽ dùng làm vùng mở rộng/TP của OTE.
- **Vị trí premium/discount:** OTE Long cần ở discount HTF; OTE Short cần ở premium HTF.

### H1 / M15 — POI & Context
- **Nhịp impulse:** xác định nhịp displacement H1/M15 đã phá cấu trúc để kéo fib.
- **Vùng OTE cụ thể:** ghi mức 62%, 70.5%, 79%, ví dụ `OTE Long: 62%=1.0820, 70.5%=1.0812, 79%=1.0804`.
- **Confluence:** FVG/OB nào nằm trong vùng OTE?
- **Liquidity:** đã sweep pool đối diện trước nhịp impulse chưa?

### M5 / M1 — Confirmation & Entry
- **Vào vùng OTE:** đặt lệnh chờ trong vùng 62–79%, ưu tiên quanh 70.5% hoặc tại FVG/OB trùng vùng.
- **LTF confirm (tùy phong cách):** chờ M5/M1 có phản ứng (reject / bullish-bearish MSS nhỏ) để xác nhận, hoặc dùng lệnh limit tại 70.5%.
- **Stop loss logic:** ngoài mốc 100% (đầu nhịp) hoặc ngoài FVG/OB trùng vùng.
- **Target:** mức mở rộng (−0.27, −0.62) và/hoặc pool liquidity HTF.

```text
Mẫu ghi nhanh — OTE Long
HTF Bias: Bullish | Location: Discount
Nhịp impulse: đáy [low] → đỉnh [high] (đã MSS bullish)
OTE: 62%=[..] 70.5%=[..] 79%=[..]
Confluence: bullish FVG/OB [range] trùng vùng OTE? Yes/No
Sweep trước nhịp: SSL tại [level]? Yes/No
Entry: limit quanh 70.5% / tại FVG
Stop: dưới 100% ([low]) hoặc dưới FVG
Target: -0.27/-0.62 mở rộng + BSL [level]
Invalid: đóng nến dưới 79–100% (nhịp fail)
```

```text
Mẫu ghi nhanh — OTE Short
HTF Bias: Bearish | Location: Premium
Nhịp impulse: đỉnh [high] → đáy [low] (đã MSS bearish)
OTE: 62%=[..] 70.5%=[..] 79%=[..]
Confluence: bearish FVG/OB [range] trùng vùng OTE? Yes/No
Sweep trước nhịp: BSL tại [level]? Yes/No
Entry: limit quanh 70.5% / tại FVG
Stop: trên 100% ([high]) hoặc trên FVG
Target: -0.27/-0.62 mở rộng + SSL [level]
Invalid: đóng nến trên 79–100% (nhịp fail)
```

> [!warning]
> **OTE không phải lý do để vào ngược xu hướng.** OTE Long chỉ hợp lệ khi nhịp impulse là tăng và bias bullish. Kéo fib một nhịp giảm rồi "Long ở 70.5%" giữa downtrend là bắt dao rơi.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Fib kéo trên nhịp displacement đã phá cấu trúc, đúng chiều, đồng hướng bias.
- [ ] Giá retrace vào vùng 62–79% (không phải 38–50%).
- [ ] Vùng OTE trùng FVG/OB và đúng premium/discount.
- [ ] Có liquidity sweep trước nhịp impulse.
- [ ] Stop ngoài 100%; target tại mức mở rộng/liquidity; R:R đạt kế hoạch.
- [ ] (Tùy phong cách) có LTF confirm khi giá chạm vùng OTE.

### Setup bị vô hiệu khi
- [ ] Giá **đóng nến dưới 79–100%** (Long) / trên (Short) → nhịp impulse đã fail.
- [ ] Fib kéo trên nhịp không phá cấu trúc.
- [ ] Giá chỉ retrace nông (38–50%) rồi đi tiếp — không có entry OTE.
- [ ] OTE ngược bias / sai premium-discount.
- [ ] Không có POI/sweep nào hỗ trợ vùng OTE.

### Retrace nông vs OTE vs Nhịp fail

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Giá chỉ về 38–50% rồi tiếp tục | **Retrace nông** | Không phải entry OTE; có thể chờ continuation entry khác |
| Giá về 62–79%, reject với confluence | **OTE hợp lệ** | Entry tối ưu; stop ngoài 100% |
| Giá đâm 79% rồi vẫn reject quanh 79–90% | **OTE sâu (deep)** | Vẫn dùng được nếu có POI; stop chặt hơn |
| Đóng nến vượt 100% | **Nhịp fail** | Hủy OTE; có thể đảo hướng |

> [!note]
> OTE là **một cách định lượng hóa "mua rẻ trong discount / bán đắt trong premium"**. Vì thế nó luôn phải đi cùng [[27 - Premium Discount]]: vùng 62–79% của một nhịp Long gần như luôn nằm ở discount, và đó chính là lý do nó cho R:R tốt.

---

## 6. Ví dụ chart

### Ví dụ đúng — Retrace vào vùng 62–79% sau MSS, Long với confluence
![[OTE-Example-Correct.png]]

**Mô tả:**
HTF bias Bullish. Giá quét SSL (sweep low) rồi bật lên bằng một nhịp displacement phá swing high nội bộ (MSS bullish). Kéo fib từ đáy nhịp (100%) lên đỉnh (0%). Giá retrace về vùng **62–79%**, nơi trùng một bullish FVG/OB (confluence) và nằm ở discount. Entry quanh **70.5%**; stop dưới mốc 100% (đáy sweep); target là BSL phía trên (vùng mở rộng).

**Vì sao đây là ví dụ tốt:**
- Fib kéo trên nhịp **đã phá cấu trúc** (MSS), đồng hướng bias.
- Entry trong vùng **62–79%**, không phải retrace nông 50%.
- Vùng OTE trùng FVG/OB và đúng **discount** → confluence.
- Có **sweep** trước nhịp impulse; stop logic ngoài 100%.
- Target là liquidity rõ → R:R tối ưu.

### Ví dụ sai / dễ nhầm — Kéo fib tùy tiện, vào ở retrace nông giữa downtrend
![[OTE-Example-Wrong.png]]

**Mô tả lỗi:**
Thị trường đang giảm (bias bearish). Trader kéo fib lên một nhịp nảy nhỏ và "Long ở vùng OTE", nhưng thực ra giá chỉ retrace **nông (~38%)**, nhịp được kéo fib **không phá cấu trúc**, và lệnh **ngược hẳn xu hướng**. Không có sweep, không có MSS bullish. Giá tiếp tục giảm và stop bị quét.

**Bài học:**
- OTE chỉ dùng trên nhịp **displacement đã phá cấu trúc**, không phải nhịp nảy ngẫu nhiên.
- Vào ở 38–50% **không phải OTE**; OTE là vùng 62–79%.
- OTE phải **đồng hướng bias**; Long ở OTE giữa downtrend là bắt dao rơi.

---
### Sequence mẫu — OTE Long
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Liquidity Sweep SSL
→ Displacement tăng phá cấu trúc (MSS) → tạo nhịp impulse + FVG
→ Kéo fib: đáy (100%) → đỉnh (0%)
→ Giá retrace vào 62–79% (trùng FVG/OB, discount)
→ Entry quanh 70.5%; Stop dưới 100% / dưới FVG
→ Target: mức mở rộng -0.27/-0.62 + External BSL
```

### Sequence mẫu — OTE Short
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Liquidity Sweep BSL
→ Displacement giảm phá cấu trúc (MSS) → tạo nhịp impulse + FVG
→ Kéo fib: đỉnh (100%) → đáy (0%)
→ Giá retrace vào 62–79% (trùng FVG/OB, premium)
→ Entry quanh 70.5%; Stop trên 100% / trên FVG
→ Target: mức mở rộng -0.27/-0.62 + External SSL
```

> [!note]
> OTE là "khung định lượng" để execution các model khác: sau khi [[20 - Liquidity Sweep]] + [[21 - Market Structure Shift]] cho narrative đảo chiều, OTE cho biết **vùng giá chính xác** để vào với R:R tốt nhất, thường trùng một [[Fair Value Gap]] hoặc [[Order Block]].

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> OTE chỉ là vùng chờ. Chỉ vào khi nhịp hợp lệ + confluence + đúng bias + R:R đạt.

### A. Context (HTF)
- [ ] Daily Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] Nhịp kéo fib là displacement đã phá cấu trúc, đồng hướng bias.
- [ ] Vùng OTE nằm đúng discount (Long) / premium (Short).
- [ ] Vùng OTE trùng một POI HTF (FVG/OB).
- [ ] Có draw on liquidity rõ làm target (mức mở rộng).

### B. Execution (LTF / khi giá tới vùng OTE)
- [ ] Giá đã vào vùng 62–79% (không phải retrace nông).
- [ ] Đã có liquidity sweep trước nhịp impulse.
- [ ] (Nếu cần) LTF có phản ứng/MSS xác nhận tại vùng OTE.
- [ ] Entry quanh 70.5% / tại FVG-OB trùng vùng.
- [ ] Stop ngoài 100% / ngoài FVG.
- [ ] Target tại mức mở rộng/liquidity; R:R tối thiểu đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Nhịp kéo fib không phá cấu trúc → không trade.
- [ ] Giá mới retrace nông 38–50% → không trade (chưa OTE).
- [ ] OTE ngược bias / sai premium-discount → không trade.
- [ ] Không có confluence (POI/sweep) → không trade.
- [ ] Giá đã đóng nến vượt 100% (nhịp fail) → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Kéo fib tùy tiện | Kéo lên mọi nhịp, kể cả nhịp không phá cấu trúc | Vùng OTE vô nghĩa | Chỉ kéo fib trên nhịp displacement đã BOS/MSS |
| Vào ở retrace nông | Long/Short ở 38–50% | Chưa vào vùng OTE, R:R kém | Chỉ vào trong 62–79% |
| OTE ngược bias | Long ở OTE giữa downtrend | Bắt dao rơi, xác suất thấp | Chỉ OTE đồng hướng Daily Bias |
| Bỏ qua confluence | Vào 70.5% dù không trùng POI nào | Thiếu lý do giá phản ứng | Ưu tiên OTE trùng FVG/OB + sau sweep |
| Stop quá sát | Stop trong vùng OTE, không ngoài 100% | Bị quét trước khi đảo | Stop ngoài 100% / ngoài FVG |
| Bỏ qua premium/discount | OTE Long ở premium | Mâu thuẫn nguyên tắc mua rẻ | OTE Long ở discount, Short ở premium |
| Giữ lệnh khi nhịp fail | Giá vượt 100% mà vẫn ôm | Cấu trúc đã đảo | Cắt khi đóng nến vượt 100% |
| Quên target mở rộng | Không đặt TP theo -0.27/-0.62/liquidity | R:R không kế hoạch | Đặt target tại mức mở rộng + pool liquidity |

---

## 10. Câu hỏi tự kiểm tra

- Mình có giải thích được vùng OTE 62–79% và vì sao 70.5% là sweet spot trong 30 giây không?
- Nhịp mình kéo fib có thực sự phá cấu trúc đúng hướng bias không?
- Giá đã vào 62–79% hay mới chỉ retrace nông?
- Vùng OTE có trùng FVG/OB và đúng premium/discount không?
- Đã có sweep trước nhịp impulse chưa?
- Stop (ngoài 100%) và target (mức mở rộng/liquidity) ở đâu, R:R bao nhiêu?
- Điều gì làm nhịp này fail và hủy OTE?
- Nếu không trade OTE này, lý do "No Trade" là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Vùng OTE nằm ở khoảng Fibonacci nào và mức "vàng" là bao nhiêu?
**Đáp:** Vùng 62%–79% retracement; mức sweet spot là 70.5%.

### Q2
**Hỏi:** Kéo fib cho một lệnh Long như thế nào?
**Đáp:** Kéo từ đáy nhịp (swing low = 100%) lên đỉnh nhịp (0%); vùng OTE 62–79% nằm gần đáy → discount sâu.

### Q3
**Hỏi:** Vì sao vào ở 50% không phải là OTE?
**Đáp:** 50% là equilibrium (EQ) — retrace nông, R:R kém hơn; OTE yêu cầu retrace sâu vào discount/premium (62–79%).

### Q4
**Hỏi:** Điều kiện tiên quyết để kéo fib cho OTE là gì?
**Đáp:** Nhịp được kéo fib phải là displacement **đã phá cấu trúc** (BOS/MSS) đúng hướng bias.

### Q5
**Hỏi:** "OTE có confluence" nghĩa là gì?
**Đáp:** Vùng 62–79% trùng với FVG/OB, đúng premium/discount, và đến sau một liquidity sweep.

### Q6
**Hỏi:** Stop và target của OTE đặt ở đâu?
**Đáp:** Stop ngoài mốc 100% (đầu nhịp) hoặc ngoài FVG/OB; target tại mức mở rộng (−0.27, −0.62) và/hoặc pool liquidity.

### Q7
**Hỏi:** Khi nào OTE bị vô hiệu?
**Đáp:** Khi giá đóng nến vượt mốc 100% (nhịp impulse fail), khi fib kéo trên nhịp không phá cấu trúc, hoặc khi OTE ngược bias.

---
## 12. Lesson Learned

### Bài học chính
- OTE là **execution model định lượng R:R**, không phải tín hiệu độc lập.
- Chỉ kéo fib trên **nhịp displacement đã phá cấu trúc**, đồng hướng bias.
- Entry trong vùng **62–79%** (không phải 38–50%); 70.5% là sweet spot.
- OTE mạnh nhất khi có **confluence**: trùng FVG/OB + đúng premium/discount + sau sweep.
- Stop ngoài 100%, target tại mức mở rộng/liquidity — đó là nơi R:R đẹp đến.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ kéo fib trên nhịp đã phá cấu trúc đúng hướng bias.
- [ ] Tôi chỉ vào trong vùng 62–79%, không vào ở retrace nông.
- [ ] Tôi chỉ làm OTE đồng hướng Daily Bias và đúng premium/discount.
- [ ] Tôi ưu tiên OTE trùng FVG/OB và đến sau một sweep.
- [ ] Tôi đặt stop ngoài 100% và cắt lệnh khi giá đóng nến vượt 100%.

### Câu nhắc nhở khi trade
> **"OTE là nơi tôi mua rẻ trong discount / bán đắt trong premium — chỉ trên nhịp đã phá cấu trúc, có confluence, sau sweep."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có nắm vùng 62–79%, 70.5%, cách kéo fib không? |
| Nhận diện trên chart |  | Có chọn đúng nhịp phá cấu trúc để kéo fib không? |
| Biết khi nào bỏ qua |  | Có dám bỏ OTE ngược bias / retrace nông không? |
| Kết hợp với context HTF |  | OTE có đặt trong bias + premium/discount + confluence không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự ở 62–79% với confluence không? |
| Review sau trade |  | Có so sánh expectancy theo mức entry bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[Optimal Trade Entry]]`.
- [ ] Review riêng: entry 62% vs 70.5% vs 79%; có/không confluence; có/không sweep.
- [ ] Thống kê win rate, average R theo `ote_entry_level` và `ote_confluence`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## Appendix — OTE Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish / Neutral
> **Direction:** Long / Short
> **Nhịp impulse (đã MSS?):** [low]→[high] / [high]→[low]
> **OTE levels:** 62%=____ 70.5%=____ 79%=____
> **Confluence (FVG/OB trùng vùng?):** Yes / No — vùng: ____
> **Location:** Premium / Discount / Equilibrium
> **Sweep trước nhịp?** Yes / No — pool: ____
> **Entry plan (quanh 70.5%):**
> **Stop (ngoài 100%):**
> **Target (mở rộng -0.27/-0.62 + liquidity):**
> **R:R dự kiến:**
> **Kill zone permitted:** London / NY AM / NY PM
> **Invalidation (đóng nến vượt 100% tại):**
> **No-trade condition:**
