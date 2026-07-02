---
type: ict-concept
concept: ICT 2022 Model
aliases:
  - ICT 2022 Model
  - ICT 2022
  - 2022 Model
  - ICT Model 2022
tags:
  - trading/ict/concept
  - trading/study
  - "#ICT2022"
status: developing
category: Entry Model
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - ICT 2022
  - Silver Bullet
  - OTE
  - AMD
  - MMXM
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-06-22
common_mistakes:
  - "[[Mistake - Skip Liquidity Sweep]]"
  - "[[Mistake - Chase Displacement]]"
  - "[[Mistake - Trade Against Bias]]"
---

# ICT 2022 Model

> [!summary] Tóm tắt 1 câu
> **ICT 2022 Model là quy trình entry hoàn chỉnh ghép các khái niệm rời rạc thành một chuỗi: xác định draw on liquidity theo bias → chờ liquidity sweep → displacement phá cấu trúc (MSS) để lại FVG → vào lệnh khi giá retrace về FVG → target pool liquidity đối diện.**

> [!important] Nguyên tắc cốt lõi
> **Mô hình là một CHUỖI có thứ tự bắt buộc: Bias → Liquidity → Sweep → Displacement/MSS → FVG → Entry → Target. Bỏ qua bất kỳ mắt xích nào (đặc biệt là liquidity sweep) đều làm setup mất xác suất.**
> Đây không phải một chỉ báo; nó là một "công thức nấu ăn". Thiếu nguyên liệu hoặc sai thứ tự thì không phải món ăn ICT 2022.

---

## 1. Định nghĩa

**Khái niệm:**
ICT 2022 Model là **mô hình giao dịch tổng hợp** mà ICT công bố trong loạt bài năm 2022, gói toàn bộ các khái niệm cốt lõi (bias, liquidity, sweep, displacement, MSS, FVG, premium/discount) thành **một quy trình entry duy nhất, lặp lại được**. Mục tiêu: biến mớ khái niệm rời rạc thành một checklist hành động rõ ràng từ HTF xuống LTF.

**Chuỗi 7 bước của mô hình:**
1. **Bias (HTF):** xác định hướng — Bullish / Bearish (xem [[12 - Daily Bias]]).
2. **Draw on liquidity:** xác định pool liquidity mà giá đang bị hút về (target cuối) và pool sẽ bị quét trước.
3. **Liquidity Sweep:** chờ giá quét một pool liquidity (đỉnh/đáy, equal highs/lows) — đây là trigger ([[20 - Liquidity Sweep]]).
4. **Displacement + MSS:** một move mạnh, quyết đoán phá cấu trúc ([[21 - Market Structure Shift]] + [[Displacement]]) theo hướng bias, **để lại FVG**.
5. **FVG (POI):** xác định Fair Value Gap của nhịp displacement — đây là điểm vào ([[Fair Value Gap]]).
6. **Entry:** vào lệnh khi giá **retrace** về FVG (thường quanh CE 50%), đúng premium/discount.
7. **Target:** pool liquidity đối diện (internal trước, external sau).

**Bản chất:** mô hình mã hóa logic "smart money": giá quét thanh khoản (lấy nhiên liệu) → đẩy mạnh đổi hướng (thể hiện intent, để lại imbalance) → quay lại lấp một phần imbalance (cho retail một điểm vào "giá tốt") → chạy về pool liquidity tiếp theo. Bạn vào cùng lúc với chiều của displacement, tại vùng giá chiết khấu.

**Mục đích trong ICT:**
- Cho một **khung execution chuẩn hóa**, lặp lại và backtest được.
- Buộc trader **chờ đủ điều kiện** thay vì vào theo cảm tính.
- Định nghĩa rõ **entry, stop, target** ở mỗi bước.
- Là "xương sống" để các biến thể (Silver Bullet, OTE, AMD) gắn vào.

**Vì sao khái niệm này quan trọng:**
Hầu hết người học ICT biết từng khái niệm riêng nhưng không biết **ghép chúng theo thứ tự nào**. ICT 2022 Model chính là thứ tự đó. Nó cũng là bộ lọc kỷ luật: nếu một setup không đi qua đủ chuỗi, bạn có lý do khách quan để "No Trade".

**Nó giúp trả lời câu hỏi nào trên chart?**
- Setup hiện tại đã đi qua đủ chuỗi (sweep → displacement → FVG) chưa?
- Đang ở bước nào của mô hình, còn thiếu bước gì?
- FVG nào là POI hợp lệ, entry và stop ở đâu?
- Pool liquidity nào là target, R:R bao nhiêu?

### ICT 2022 Model không phải là gì
- Không phải một chỉ báo / tín hiệu tự động.
- Không phải "thấy FVG là vào" — FVG chỉ là bước 5, phải có sweep + MSS trước.
- Không phải cái cớ để bỏ qua bias / premium-discount.
- Không phải chỉ dùng được một timeframe — nó là quy trình HTF→LTF.
- Không phải đảm bảo thắng; nó là khung xác suất cần kết hợp risk management.

---

## 2. Bối cảnh sử dụng

### Các bước & khái niệm tương ứng

| Bước | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| 1 | Bias | [[12 - Daily Bias]] | Hướng HTF là gì? |
| 2 | Draw on liquidity | [[19 - Liquidity]], [[12 - Dealing Range]] | Giá bị hút về pool nào? |
| 3 | Liquidity Sweep | [[20 - Liquidity Sweep]] | Đã quét pool nào, có reclaim? |
| 4 | Displacement + MSS | [[Displacement]], [[21 - Market Structure Shift]] | Có phá cấu trúc + để lại FVG không? |
| 5 | FVG (POI) | [[Fair Value Gap]], [[Order Block]] | FVG ở đâu, CE ở đâu? |
| 6 | Entry | [[27 - Premium Discount]], [[Optimal Trade Entry]] | Đúng premium/discount, R:R đủ chưa? |
| 7 | Target | [[19 - Liquidity]] | Pool đối diện ở đâu? |

### Biến thể thường gặp
- **+ OTE:** thay vì chỉ FVG, dùng vùng OTE 62–79% trùng FVG để refine entry ([[Optimal Trade Entry]]).
- **+ Silver Bullet:** chạy mô hình trong cửa sổ 1 giờ của [[18 - Kill Zones]].
- **+ AMD:** đặt mô hình trong khung Tích lũy–Thao túng–Phân phối ([[02 - AMD]]); sweep ~ manipulation, displacement ~ distribution.
- **+ Order Block / Breaker:** POI ở bước 5 có thể là OB/Breaker thay vì FVG.

> [!tip]
> Cách nhớ nhanh: **"Quét → Đẩy → Lùi → Vào → Chạy"** (Sweep → Displace/MSS → Retrace to FVG → Entry → Run to target). Nếu một setup không có cả "Quét" lẫn "Đẩy", nó không phải ICT 2022.

### Khi nào mô hình này có giá trị cao?
- [ ] Bias HTF rõ ràng, có draw on liquidity cụ thể.
- [ ] Có liquidity sweep rõ trước displacement.
- [ ] Displacement phá cấu trúc và để lại FVG sạch.
- [ ] FVG ở đúng premium/discount, đồng hướng bias.
- [ ] Trong [[18 - Kill Zones]] (London/NY) → xác suất cao hơn.

### Khi nào nên bỏ qua?
- [ ] Thiếu liquidity sweep (vào chỉ vì thấy FVG/MSS).
- [ ] Displacement yếu / không để lại FVG.
- [ ] Setup ngược bias hoặc sai premium-discount.
- [ ] Vào khi giá đã chạy xa (chase, không chờ retrace).
- [ ] Ngoài kill zone / sát giờ tin lớn.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Pool liquidity đánh dấu trước:** xác định BSL/SSL hai phía, pool là draw.
2. **Sweep:** giá quét một pool, có reclaim (đóng nến trở lại).
3. **Displacement:** nến/đoạn thân lớn, quyết đoán, phá swing (MSS).
4. **FVG:** khoảng imbalance 3 nến do displacement để lại; xác định CE.
5. **Retrace:** giá quay lại FVG đúng premium/discount → điểm vào.

### Ma trận nhận diện (Long)

| Bước | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Bias | HTF bullish, draw lên BSL | Bias không rõ → bỏ |
| Sweep | Quét SSL + reclaim | Không sweep → không phải ICT 2022 |
| Displacement/MSS | Phá swing high + FVG bullish | Move yếu, không FVG → bỏ |
| FVG | Bullish FVG (BISI), CE rõ | Không có gap thật → bỏ |
| Entry | Tại FVG, ở discount | Ở premium → sai chỗ |
| Target | BSL phía trên | Không pool rõ → R:R kém |

### Điều kiện bắt buộc
- [ ] Bias HTF xác định + draw on liquidity.
- [ ] Có liquidity sweep trước displacement.
- [ ] Displacement phá cấu trúc và để lại FVG.
- [ ] Xác định FVG/CE và mức invalidation.
- [ ] Xác định pool target.

### Điều kiện tăng xác suất
- [ ] FVG trùng OB / OTE 62–79% (confluence).
- [ ] Setup trong kill zone, trùng pha distribution AMD.
- [ ] FVG ở đúng premium/discount, đồng hướng bias.
- [ ] Stop logic ngoài điểm sweep; R:R ≥ kế hoạch.

### Điều kiện làm setup yếu đi
- Sweep mờ / không rõ reclaim.
- Displacement không dứt khoát, FVG bị lấp nhanh.
- Nhiều FVG chồng chéo, POI mơ hồ.
- Ngoài kill zone, gần tin tức.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng ICT 2022 Model
> 1. **Bias và draw on liquidity là gì?**
> 2. **Đã có liquidity sweep chưa, ở pool nào?**
> 3. **Có displacement phá cấu trúc + FVG đúng premium/discount chưa?**
> 4. **Entry/stop/target ở đâu, R:R bao nhiêu, có trong kill zone không?**

### D1 / H4 — Bias & Narrative
- **Bias:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **Draw on liquidity:** pool HTF là target cuối (BSL cho Long, SSL cho Short).
- **Dealing range & premium/discount:** xác định vùng để chỉ Long ở discount / Short ở premium.

### H1 / M15 — POI & Context
- **Pool sẽ bị sweep:** đánh dấu đỉnh/đáy, equal highs/lows.
- **Chờ sweep + displacement:** quan sát giá quét pool rồi displacement phá cấu trúc.
- **FVG cụ thể:** ghi range FVG + CE, ví dụ `H1 bullish FVG 1.0820–1.0835, CE 1.08275`.

### M5 / M1 — Confirmation & Entry
- **Refine:** trên LTF, displacement thường để lại một FVG nhỏ hơn; có thể chờ M5 MSS để xác nhận.
- **Entry:** tại FVG (quanh CE) / OTE trùng FVG.
- **Stop:** ngoài điểm sweep / đầu kia FVG.
- **Target:** internal liquidity trước, external pool sau.

```text
Mẫu ghi nhanh — ICT 2022 Long
Bias (HTF): Bullish | Draw: BSL @ [level]
Location: Discount
(1) Sweep: SSL @ [level] + reclaim
(2) Displacement + MSS phá [swing high] → FVG
(3) FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop dưới sweep / dưới FVG
(5) Target: internal [..] → external BSL [..]
Kill zone: London / NY AM
Invalid: đóng nến dưới FVG (acceptance)
```

```text
Mẫu ghi nhanh — ICT 2022 Short
Bias (HTF): Bearish | Draw: SSL @ [level]
Location: Premium
(1) Sweep: BSL @ [level] + reclaim
(2) Displacement + MSS phá [swing low] → FVG
(3) FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop trên sweep / trên FVG
(5) Target: internal [..] → external SSL [..]
Kill zone: London / NY AM
Invalid: đóng nến trên FVG (acceptance)
```

> [!warning]
> **Đừng "chase" displacement.** Bước displacement là để XÁC NHẬN, không phải để vào lệnh. Entry xảy ra ở bước RETRACE về FVG. Vào ngay khi thấy nến lớn = bỏ qua bước 6, R:R xấu và dễ trúng đỉnh/đáy ngắn hạn.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Đi qua đủ chuỗi: Bias → Sweep → Displacement/MSS → FVG → Entry (retrace) → Target.
- [ ] Liquidity sweep rõ ràng trước displacement.
- [ ] FVG sạch, đúng premium/discount, đồng hướng bias.
- [ ] Entry tại retrace về FVG (quanh CE), không chase.
- [ ] Stop ngoài sweep; target pool rõ; R:R đạt kế hoạch.
- [ ] (Lý tưởng) trong kill zone, có confluence OB/OTE.

### Setup bị vô hiệu khi
- [ ] Thiếu liquidity sweep → không phải ICT 2022.
- [ ] Displacement yếu / không để lại FVG.
- [ ] Giá **đóng nến xuyên qua FVG** (acceptance) → POI invalid.
- [ ] Entry ngược bias / sai premium-discount.
- [ ] Vào bằng cách chase, bỏ bước retrace.

### Mức độ "đủ chuỗi"

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Đủ Bias + Sweep + Displacement + FVG + retrace | **A+ setup** | Thực thi theo plan |
| Có sweep + displacement nhưng FVG đã bị lấp | **Chờ POI khác** | Tìm FVG/OB tiếp theo, đừng ép |
| Có FVG + MSS nhưng KHÔNG có sweep | **Không đủ chuỗi** | Bỏ; xác suất thấp |
| Đủ chuỗi nhưng ngoài kill zone | **Hạ cấp** | Giảm size hoặc bỏ tùy quy tắc |

> [!note]
> ICT 2022 Model là "bản đồ tổng" còn các note khác là "địa danh": khi bí, hãy về đây để kiểm tra mình đang ở bước nào và thiếu mắt xích gì. Phần lớn lỗi đến từ **bỏ qua bước 3 (sweep)** hoặc **bỏ qua bước 6 (retrace)**.

---

## 6. Ví dụ chart

### Ví dụ đúng — Đủ chuỗi: Sweep → MSS+Displacement → FVG retrace → Target
![[ICT-2022-Model-Example-Correct.png]]

**Mô tả:**
HTF bias Bullish, draw on liquidity là BSL phía trên. Giá retrace vào discount. **(1)** Một cú **sweep SSL** quét đáy ngắn hạn rồi reclaim. **(2)** Ngay sau đó là **displacement tăng** phá swing high (MSS bullish), để lại một **bullish FVG**. **(3)** Giá retrace về FVG (quanh CE) → **entry**; stop dưới điểm sweep. **(4)** Giá chạy về **BSL target**.

**Vì sao đây là ví dụ tốt:**
- Đi qua **đủ chuỗi** theo đúng thứ tự.
- Liquidity sweep xảy ra TRƯỚC displacement.
- Entry ở bước **retrace về FVG**, đúng discount, không chase.
- Stop logic ngoài sweep; target là pool liquidity rõ (BSL).

### Ví dụ sai / dễ nhầm — Chase displacement, không sweep, vào ở premium ngược bias
![[ICT-2022-Model-Example-Wrong.png]]

**Mô tả lỗi:**
Bias HTF là Bearish (draw thật là SSL phía dưới). Trader thấy một nhịp **displacement tăng** và **Long ngay ở premium** vì "có MSS + sắp có FVG". Nhưng **không hề có liquidity sweep** trước đó, entry ở **sai phía (premium)**, **ngược bias**, và **không chờ retrace**. Giá đảo xuống tiếp tục theo bias bearish về SSL; stop bị quét.

**Bài học:**
- Không có **liquidity sweep** thì không phải setup ICT 2022 — bỏ.
- Displacement để **xác nhận**, không phải để chase; entry ở **retrace về FVG**.
- Luôn kiểm tra **bias + premium/discount** trước khi vào.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[20 - Liquidity Sweep]]
- [[Displacement]]
- [[21 - Market Structure Shift]]
- [[Fair Value Gap]]
- [[Order Block]]
- [[27 - Premium Discount]]
- [[Optimal Trade Entry]]
- [[12 - Dealing Range]]
- [[18 - Kill Zones]]
- [[02 - AMD]]

### Sequence mẫu — ICT 2022 Long (đầy đủ)
```text
(1) HTF Bullish Bias + Draw on liquidity = BSL
(2) Giá ở Discount của HTF dealing range
(3) Liquidity Sweep SSL (+ reclaim)
(4) Displacement tăng phá cấu trúc (MSS) → tạo Bullish FVG
(5) Giá retrace về FVG (quanh CE), lý tưởng trùng OB/OTE
(6) Entry; Stop dưới điểm sweep / dưới FVG
(7) Target: Internal liquidity → External BSL
(+ Kill zone London/NY, + đồng hướng AMD distribution)
```

### Sequence mẫu — ICT 2022 Short (đầy đủ)
```text
(1) HTF Bearish Bias + Draw on liquidity = SSL
(2) Giá ở Premium của HTF dealing range
(3) Liquidity Sweep BSL (+ reclaim)
(4) Displacement giảm phá cấu trúc (MSS) → tạo Bearish FVG
(5) Giá retrace về FVG (quanh CE), lý tưởng trùng OB/OTE
(6) Entry; Stop trên điểm sweep / trên FVG
(7) Target: Internal liquidity → External SSL
(+ Kill zone London/NY, + đồng hướng AMD distribution)
```

> [!note]
> Đây là mô hình "mẹ"; mọi note khác trong vault là một mắt xích của nó. Khi review một trade, hãy soi nó qua 7 bước này — lỗi thường nằm ở một bước cụ thể bị bỏ qua, và đó là dữ liệu vàng để sửa.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy một mảnh của mô hình
> Phải đủ chuỗi. Một FVG hay một MSS đơn lẻ KHÔNG phải là ICT 2022 Model.

### A. Context (HTF)
- [ ] Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] Draw on liquidity (target) đã xác định.
- [ ] Location đúng: discount (Long) / premium (Short).
- [ ] Pool sẽ bị sweep đã đánh dấu.

### B. Execution (LTF)
- [ ] Đã có liquidity sweep + reclaim.
- [ ] Có displacement phá cấu trúc (MSS) để lại FVG.
- [ ] FVG sạch, xác định CE; (lý tưởng) trùng OB/OTE.
- [ ] Entry ở retrace về FVG, không chase.
- [ ] Stop ngoài sweep / đầu kia FVG.
- [ ] Target pool rõ; R:R đạt kế hoạch; trong kill zone.

### C. Quy tắc "không có lệnh"
- [ ] Thiếu liquidity sweep → không trade.
- [ ] Không có displacement/FVG → không trade.
- [ ] Ngược bias / sai premium-discount → không trade.
- [ ] Chỉ có thể vào bằng chase (không retrace) → không trade.
- [ ] Ngoài kill zone / sát tin lớn → cân nhắc bỏ.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bỏ qua liquidity sweep | Vào chỉ vì thấy FVG/MSS | Mất mắt xích quan trọng nhất | Bắt buộc có sweep trước displacement |
| Chase displacement | Vào ngay khi thấy nến lớn | Bỏ bước retrace, R:R xấu | Chờ giá retrace về FVG |
| Trade ngược bias | Long/Short ngược HTF | Target ngược, xác suất thấp | Chỉ trade đồng hướng Daily Bias |
| Sai premium/discount | Long ở premium, Short ở discount | Entry chase, R:R xấu | Long ở discount, Short ở premium |
| FVG không từ displacement | Gọi gap thường là FVG | Không có intent | Yêu cầu displacement phá cấu trúc |
| Bỏ qua kill zone | Vào giờ chết | Thanh khoản kém, whipsaw | Săn trong London/NY KZ |
| Stop tùy tiện | Không đặt ngoài sweep/FVG | Bị quét vô lý | Stop logic ngoài điểm sweep |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = pool liquidity đối diện |
| Vào khi thiếu chuỗi | Có vài bước, ép cho đủ | Setup yếu | Đủ 7 bước mới vào; nếu thiếu → No Trade |

---

## 10. Câu hỏi tự kiểm tra

- Mình có đọc thuộc chuỗi 7 bước (Bias→Liquidity→Sweep→Displacement/MSS→FVG→Entry→Target) không?
- Setup này đã đi qua đủ chuỗi chưa, đang thiếu bước nào?
- Đã có liquidity sweep trước displacement chưa?
- FVG có sạch, đúng premium/discount, đồng hướng bias không?
- Entry là retrace về FVG hay đang chase?
- Stop (ngoài sweep) và target (pool đối diện) ở đâu, R:R bao nhiêu?
- Có trong kill zone không?
- Nếu không trade, lý do "No Trade" rơi vào bước nào của mô hình?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Chuỗi 7 bước của ICT 2022 Model là gì?
**Đáp:** Bias → Draw on liquidity → Liquidity Sweep → Displacement + MSS (để lại FVG) → FVG (POI) → Entry khi retrace về FVG → Target (pool liquidity đối diện).

### Q2
**Hỏi:** Mắt xích nào hay bị bỏ qua nhất và hậu quả?
**Đáp:** Liquidity Sweep (bước 3). Bỏ qua nó khiến trader vào chỉ vì thấy FVG/MSS, thường bị stop quét vì market còn muốn lấy thanh khoản.

### Q3
**Hỏi:** Displacement trong mô hình dùng để làm gì — vào lệnh hay xác nhận?
**Đáp:** Để XÁC NHẬN (phá cấu trúc + để lại FVG). Entry xảy ra ở bước retrace về FVG, KHÔNG chase displacement.

### Q4
**Hỏi:** Entry và stop của ICT 2022 Long đặt ở đâu?
**Đáp:** Entry tại FVG (quanh CE), ở discount; stop ngoài điểm sweep / dưới đầu kia FVG.

### Q5
**Hỏi:** Điều gì làm POI (FVG) của mô hình bị vô hiệu?
**Đáp:** Khi giá đóng nến xuyên qua FVG (acceptance) → FVG invalid; hoặc khi không có sweep/displacement tạo ra nó.

### Q6
**Hỏi:** Làm sao biết một setup KHÔNG phải ICT 2022 Model?
**Đáp:** Nếu thiếu liquidity sweep hoặc thiếu displacement/MSS để lại FVG, hoặc ngược bias / sai premium-discount → không đủ chuỗi → không phải mô hình.

### Q7
**Hỏi:** Mô hình ghép với Kill Zones và AMD ra sao?
**Đáp:** Kill Zones cho biết KHI NÀO săn (London/NY); AMD cho biết PHA (sweep ~ manipulation, displacement ~ distribution). A+ setup là giao điểm của cả ba.

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
> Nếu vault có folder riêng như `Trades`, `Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "03 - Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: ICT-2022 # ICT-2022 | Silver-Bullet | OTE | AMD
bias: bullish # bullish | bearish
draw_on_liquidity: BSL # BSL | SSL
sweep_done: true # bước 3
displacement_mss: true # bước 4
fvg_entry: true # bước 5-6 (entry tại FVG retrace)
entry_location: Discount # Premium | Discount
chained_fully: true # đủ 7 bước chưa
killzone: London-Open
rr_planned: 4.0
missing_step: none # none | sweep | displacement | retrace | target
```

> [!tip]
> Trường `missing_step` là vàng: với các lệnh thua, ghi lại bước nào bị bỏ qua. Sau 30–50 lệnh, thống kê lỗi theo `missing_step` — gần như chắc chắn một vài bước (thường là sweep / retrace) chiếm phần lớn thua lỗ, và đó là nơi cần siết kỷ luật.

---

## 13. Lesson Learned

### Bài học chính
- ICT 2022 Model là **một chuỗi có thứ tự**, không phải tập hợp tín hiệu rời.
- **Liquidity sweep (bước 3)** là mắt xích sống còn — thiếu nó là không có setup.
- Displacement để **xác nhận**; entry ở bước **retrace về FVG**, không chase.
- Luôn kiểm tra **bias + premium/discount** trước khi vào.
- Mạnh nhất khi có **confluence** (OB/OTE) + trong **kill zone** + đồng hướng **AMD distribution**.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ vào lệnh khi setup đi qua đủ 7 bước.
- [ ] Tôi luôn xác nhận có liquidity sweep trước displacement.
- [ ] Tôi vào ở retrace về FVG, không chase nến lớn.
- [ ] Tôi chỉ Long ở discount / Short ở premium, đồng hướng bias.
- [ ] Khi review thua lỗ, tôi ghi rõ bước nào bị bỏ qua (`missing_step`).

### Câu nhắc nhở khi trade
> **"Quét → Đẩy → Lùi → Vào → Chạy. Thiếu một mắt xích, tôi không có lệnh."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có đọc thuộc chuỗi 7 bước không? |
| Nhận diện trên chart |  | Có xác định đúng từng bước theo thời gian thực không? |
| Biết khi nào bỏ qua |  | Có dám "No Trade" khi thiếu sweep/retrace không? |
| Kết hợp với context HTF |  | Có ghép bias + premium/discount + kill zone + AMD không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự ở retrace FVG, đủ chuỗi không? |
| Review sau trade |  | Có gắn `missing_step` và review bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[ICT 2022 Model]]`.
- [ ] Review riêng theo `missing_step`: bước nào hay bị bỏ qua nhất.
- [ ] Thống kê win rate, average R theo `chained_fully` và `killzone`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## Appendix — ICT 2022 Model Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **(1) Bias:** Bullish / Bearish / Neutral
> **(2) Draw on liquidity (target):** BSL / SSL @ ____
> **Location:** Premium / Discount
> **(3) Liquidity sweep:** pool ____ @ ____ — reclaim? Yes/No
> **(4) Displacement + MSS:** phá ____ → FVG? Yes/No
> **(5) FVG (POI):** [low]–[high], CE ____ ; confluence OB/OTE? ____
> **(6) Entry (retrace về FVG):** ____ ; Stop (ngoài sweep): ____
> **(7) Target:** internal ____ → external ____
> **Đủ chuỗi 7 bước?** Yes / No — thiếu bước: ____
> **Kill zone:** London / NY AM / NY PM
> **R:R dự kiến:**
> **No-trade condition:**
