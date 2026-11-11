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
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-03
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

![[OTE-Advanced-Fib-Anatomy.svg|697]]
*Thang mức Fibonacci đầy đủ cho một nhịp Long: 0% (đỉnh nhịp) → 50% (EQ, không phải OTE) → 62% (mép trên OTE) → 70.5% (sweet spot, highlight vàng) → 79% (mép sâu OTE) → 100% (đáy nhịp, mốc stop). Các mức mở rộng -0.27/-0.62 phía trên 0% là target khi giá bật khỏi vùng OTE. Đường giá minh họa: đẩy lên phá cấu trúc, retrace vào đúng vùng 62–79%, phản ứng tại 70.5%, rồi chạy tới target mở rộng — đây là bộ khung để đọc mọi setup OTE trong các mục tiếp theo.*

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

### Nâng cao — Cuộc tranh luận 61.8 vs 70.5 vs 79: mức nào "ăn" hơn theo thị trường/phiên

Vùng 62–79% không phải một khối đồng nhất — nó là một dải, và điểm "ăn" nhất bên trong dải đó **không cố định cho mọi thị trường**. 70.5% được dạy như con số trung tâm vì nó là điểm cân bằng thống kê chung, nhưng thực chiến trên từng sản phẩm lại lệch về hai phía tùy vào tính chất di chuyển của thị trường đó.

Logic đằng sau sự lệch này nằm ở **biên độ và tốc độ của retrace**:

- **Thị trường trending mạnh, momentum cao** (ví dụ NQ1/NAS100 trong một phiên NY có displacement rõ) thường chỉ retrace **nông trong chính vùng OTE** — giá "sợ" bỏ lỡ, nên phản ứng sớm quanh mép **62%** trước khi tiếp tục theo hướng cũ. Chờ tới 70.5% hoặc 79% trong bối cảnh này đôi khi bị hụt entry vì giá không bao giờ về sâu đến vậy.
- **Thị trường choppy, nhiều pullback, ít momentum** (một số phiên Á hoặc các cặp forex ít biến động như EURUSD ngoài kill zone chính) có xu hướng đào sâu hơn trước khi đảo — mép **79%** (gần đầu nhịp) mới là nơi giá thực sự cạn lực bán/mua đối nghịch và bật lại.
- **70.5%** là con số "textbook" — một compromise hợp lý khi không có đủ dữ liệu cá nhân, nhưng dùng nó một cách giáo điều trên mọi thị trường là bỏ qua đặc tính riêng của từng sản phẩm.

Cách xử lý đúng không phải là "chọn một con số duy nhất và tin mãi mãi", mà là **log dữ liệu riêng theo từng thị trường**. Với mỗi lệnh OTE, ghi trường `ote_entry_level: 62 | 70.5 | 79` (mức gần nhất mà entry thực tế xảy ra), tách riêng theo `symbol` — NQ1/NAS100 vs EURUSD/XAUUSD gần như chắc chắn sẽ cho phân phối khác nhau vì đặc tính biến động khác nhau. Sau **30–50 mẫu mỗi thị trường**, so sánh win rate và R trung bình theo từng sub-level rồi mới kết luận "mức của tôi" cho từng sản phẩm — thay vì áp một con số 70.5% chung cho tất cả.

| Điều kiện thị trường | Sub-level có xu hướng "ăn" hơn | Vì sao |
|---|---|---|
| Trending mạnh, displacement lớn, kill zone chính (NY AM, London Open) | **62%** (mép nông) | Giá retrace ít vì lực đẩy còn mạnh; chờ sâu dễ hụt entry |
| Điều kiện trung bình, không có tín hiệu cực đoan | **70.5%** | Compromise thống kê hợp lý khi thiếu dữ liệu riêng |
| Choppy, nhiều pullback, thanh khoản thấp (session Á, ngoài kill zone) | **79%** (mép sâu) | Giá cần đào sâu hơn để hết lực đối nghịch trước khi đảo |

> [!tip]
> Đừng tranh luận "62 hay 70.5 hay 79 đúng" trên lý thuyết — hỏi "trên NQ1 của tôi, trong kill zone tôi trade, mức nào có win rate cao nhất qua 30–50 mẫu?" Câu trả lời của bạn có thể khác hẳn câu trả lời của người khác, và cả hai đều có thể đúng cho đúng bối cảnh của họ.

![[OTE-Advanced-Confluence-Stack.svg]]
*So sánh "OTE trơ" (trái) — chỉ có con số Fibonacci, không có gì buộc giá phải phản ứng, nên giá xuyên thẳng qua — với "OTE có confluence" (phải) — vùng 62–79% chứa cả một FVG và một Order Block bullish, lại đến ngay sau một liquidity sweep. Bên phải là nơi giá thực sự tôn trọng vùng và reject mạnh. Đây là lý do vì sao mức sub-level (62/70.5/79) chỉ nên được cân nhắc SAU KHI đã xác nhận có confluence — một OTE trơ ở đúng 70.5% vẫn yếu hơn một OTE có confluence ở 62%.*

### Nâng cao — OTE lồng nhau (nested/fractal OTE): dùng vùng OTE HTF chứa vùng OTE LTF để tinh chỉnh entry

Một vùng OTE kéo trên H1 hoặc H4 thường **rất rộng** — vùng 62–79% của một nhịp H1 có thể trải dài hàng chục đến hàng trăm pip/tick. Đặt lệnh limit dàn trải khắp vùng đó, hoặc vào ngay khi giá vừa chạm mép 62%, thường cho R:R và tỷ lệ khớp lệnh kém hơn nhiều so với việc chờ thêm một bước tinh chỉnh.

**Ý tưởng nested/fractal OTE:** OTE không chỉ tồn tại ở một khung thời gian — nó là một cấu trúc **fractal**, lặp lại ở mọi khung. Quy trình:

1. Xác định vùng OTE HTF (ví dụ H1) như bình thường — đây là vùng "chờ", không phải vùng "vào ngay".
2. Chờ giá đi vào bên trong vùng OTE HTF đó.
3. Trên khung nhỏ hơn (M15/M5), tìm một nhịp displacement **MỚI**, hình thành ngay bên trong vùng HTF đó, và **tự nó đã phá cấu trúc LTF** (MSS nội bộ).
4. Kéo fib riêng cho nhịp LTF này — nó sẽ có vùng 62–79% RIÊNG, nhỏ hơn và nằm gọn bên trong vùng OTE HTF.
5. Entry tại vùng OTE LTF (M5) này, KHÔNG phải tại vùng OTE HTF rộng.

Khi làm đúng, bạn đang **chồng hai lớp Fibonacci** lên nhau: giá vừa nằm trong discount/OTE của H1, vừa nằm trong discount/OTE của chính nhịp M5 mới — hai lớp xác suất cộng dồn cho một entry chặt hơn nhiều so với vào cả vùng H1 rộng. Đây cũng là cách tự nhiên để có stop ngắn hơn (ngoài 100% của nhịp M5, không phải ngoài 100% của nhịp H1) mà vẫn giữ đúng bối cảnh HTF.

| Tiêu chí | Vào cả vùng OTE H1 rộng | Vào tại OTE M5 lồng bên trong |
|---|---|---|
| Độ rộng vùng entry | Rất rộng, khó xác định điểm chính xác | Hẹp, có mép rõ ràng |
| Khoảng cách entry → stop | Xa (stop ngoài 100% của H1) | Gần hơn nhiều (stop ngoài 100% của M5) |
| R:R với cùng target | Thấp hơn | Cao hơn |
| Bằng chứng xác nhận | Chỉ có con số fib H1 | Có thêm MSS + fib LTF riêng — hai lớp confluence |
| Rủi ro | Vào sớm, giá còn đào sâu thêm trong vùng H1 | Cần kiên nhẫn chờ nhịp LTF mới hình thành, có thể bỏ lỡ nếu giá không tạo nhịp rõ |

> [!warning]
> OTE lồng nhau chỉ hợp lệ khi nhịp LTF bên trong **tự nó đã phá cấu trúc LTF** (có MSS riêng) — không phải bất kỳ dao động nhỏ nào bên trong vùng H1. Vào theo một "fib M5" kéo tùy tiện trên nhiễu giá bên trong vùng lớn là lặp lại đúng lỗi "kéo fib tùy tiện" đã nêu ở mục 9, chỉ là ở khung nhỏ hơn.

![[OTE-Advanced-Nested-MTF.svg]]
*Vùng OTE H1 (dải xanh rộng) chỉ đóng vai trò khung chờ. Ô zoom bên phải cho thấy một impulse M5 hoàn toàn mới hình thành bên trong dải đó, với vùng OTE 62–79% riêng của chính nó (dải vàng, hẹp hơn nhiều). Entry xảy ra tại OTE M5 — nơi hai lớp Fibonacci (H1 và M5) cùng đồng ý về một vùng giá, cho stop ngắn hơn và R:R tốt hơn so với vào dàn trải trong vùng H1.*

### Nâng cao — Overshoot bằng wick vs đóng nến qua 79-100%: phân biệt nhịp còn sống với nhịp đã fail

Section 5 đã quy định: "giá đóng nến vượt 100% → nhịp fail, hủy OTE". Nhưng trên chart thực tế, ranh giới giữa "giá đâm sâu vào vùng 79–100%" và "nhịp đã thật sự fail" hay bị đọc sai vì không phân biệt **wick** với **body close** — đúng nguyên tắc kỷ luật mà [[17 - Inverse Fair Value Gap - iFVG]] áp dụng cho việc xác nhận violation của FVG.

Áp dụng cùng logic CLOSE vs WICK vào OTE:

- **Wick chọc qua 79%, thậm chí qua cả 100%, nhưng đóng nến quay lại bên trong 62–79%** → đây **không nhất thiết** là nhịp fail. Nó có thể chỉ là một cú quét thanh khoản sâu hơn dự kiến (một kiểu sweep vi mô ngay trong chính nhịp retrace) trước khi giá tôn trọng vùng OTE — vẫn là một entry OTE hợp lệ, thậm chí "sâu" và có thể cho R:R tốt hơn vì entry gần mốc 100% hơn.
- **Một cây nến ĐÓNG BODY vượt hẳn qua mốc 100%** (không quay lại) → đây là "nhịp fail" thật theo đúng quy tắc đã nêu trong mục 5. Thị trường đã chấp nhận giá ở phía bên kia đầu nhịp — cấu trúc dùng để kéo fib không còn đáng tin, và OTE phải bị hủy chứ không "chờ thêm".

Hệ quả thực chiến: nếu bạn thấy giá thò wick qua 79% hoặc qua 100% rồi vội vàng hủy setup, bạn có thể đang bỏ lỡ một entry OTE sâu hợp lệ. Ngược lại, nếu bạn thấy một nến đóng hẳn bên ngoài 100% mà vẫn ôm lệnh chờ "giá quay lại", bạn đang lặp lại đúng lỗi "giữ lệnh khi nhịp fail" đã liệt kê trong bảng lỗi thường gặp.

| Quan sát tại vùng 79–100% | Phân loại | Verdict |
|---|---|---|
| Wick thò qua 79%, đóng nến trong 62–79% | Sweep vi mô trong retrace | Vẫn là OTE hợp lệ — entry sâu, R:R tốt hơn |
| Wick thò qua 100%, đóng nến quay lại trong 62–100% | Overshoot bằng wick | Nhịp còn sống — chưa hủy, theo dõi tiếp phản ứng |
| Body đóng nến vượt hẳn qua 100%, giữ giá bên ngoài | Nhịp fail thật | Hủy OTE ngay theo quy tắc mục 5 — không chờ thêm |
| Nhiều nến liên tiếp đóng ngoài 100% | Nhịp fail xác nhận, khả năng đảo cấu trúc | Hủy hoàn toàn; cân nhắc narrative đảo hướng mới |

> [!tip]
> Ghi thêm trường `ote_overshoot: wick | close | none` khi log trade. Nếu dữ liệu sau 30–50 mẫu cho thấy nhóm `wick` (overshoot bằng bóng nhưng vẫn đóng trong vùng) có win rate không thua kém nhóm entry "sạch" trong 62–79%, đó là bằng chứng bạn nên bớt hoảng khi thấy wick xuyên qua mốc 79/100% — miễn nến đóng đúng chỗ.

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

## Best Practices

> [!success] Nguyên tắc vàng
> **OTE không phải là con số Fibonacci — nó là một VÙNG CHỜ có điều kiện: chỉ kéo trên nhịp displacement đã phá cấu trúc đúng hướng bias, chỉ tin khi có confluence (FVG/OB + sweep) bên trong, và chỉ hủy khi ĐÓNG NẾN vượt 100% chứ không phải mỗi lần thấy một cái bóng nến chọc qua.** Phần lớn thất bại của OTE không đến từ Fibonacci sai, mà từ việc bỏ qua ba điều kiện đi kèm này.

1. **Chỉ kéo fib trên một nhịp displacement đã thực sự phá cấu trúc (BOS/MSS).** Đây là điều kiện tiên quyết đứng trước mọi con số Fibonacci — một vùng 62–79% kéo trên nhịp ngẫu nhiên không mang ý nghĩa gì, dù trông "đẹp" trên chart. Trước khi kéo fib, luôn tự hỏi: nhịp này có phá swing high/low nào không, và có đồng hướng [[12 - Daily Bias]] không?

2. **Không bao giờ vào ở 38–50%.** Đây là retrace nông (shallow retrace), không phải OTE — vùng equilibrium (50%) chỉ là ranh giới premium/discount, không phải vùng entry. Vào ở đây thường cho R:R kém và dễ bị cuốn vào nhịp fail sớm hơn dự kiến. Nếu giá chỉ về tới 50% rồi đảo, đó là bằng chứng lực đẩy còn mạnh — không phải cơ hội OTE bị bỏ lỡ để đuổi theo.

3. **Yêu cầu confluence (FVG/OB + sweep) trước khi tin tưởng tuyệt đối vào con số 70.5%.** Một vùng OTE "trơ" — chỉ có Fibonacci, không có FVG/OB nào chồng vào, không đến sau một liquidity sweep — là một entry yếu, bất kể nó có nằm chính xác ở 70.5% hay không. Ưu tiên tuyệt đối cho những vùng OTE nơi 62–79% trùng với một [[Fair Value Gap]] hoặc [[25 - OB - Order Block|Order Block]], đến ngay sau một [[20 - Liquidity Sweep]].

4. **Log `ote_entry_level` và `ote_confluence` cho mọi lệnh, và review riêng theo từng thị trường sau 30–50 mẫu.** Đừng tin một con số sweet-spot chung chung — NQ1/NAS100 (biến động mạnh, trending) và EURUSD/XAUUSD (đôi khi choppy hơn) có thể có sub-level tối ưu khác nhau (xem mục "Nâng cao — Cuộc tranh luận 61.8 vs 70.5 vs 79"). Chỉ dữ liệu riêng của bạn, tách theo `symbol`, mới cho câu trả lời đúng cho phong cách và thị trường bạn trade.

5. **Dùng OTE lồng nhau (nested/fractal) khi vùng OTE HTF quá rộng để vào thẳng.** Thay vì đặt lệnh dàn trải trong một vùng H1 rộng, chờ giá vào vùng đó rồi tìm một nhịp displacement MỚI trên M15/M5 tự nó đã phá cấu trúc LTF, và kéo fib riêng cho nhịp đó. Entry tại OTE LTF lồng bên trong OTE HTF cho stop ngắn hơn và R:R tốt hơn nhờ chồng hai lớp xác suất — chi tiết ở mục "Nâng cao — OTE lồng nhau".

6. **Phân biệt overshoot bằng wick với đóng nến qua 100% trước khi vội hủy setup.** Một cái bóng nến chọc qua 79% hoặc thậm chí qua 100% rồi đóng nến quay lại trong vùng KHÔNG tự động làm nhịp fail — đó có thể chỉ là một cú quét thanh khoản sâu trong chính nhịp retrace. Chỉ khi giá **đóng BODY** hẳn ngoài mốc 100% thì nhịp mới thực sự fail và OTE phải bị hủy ngay, không "chờ giá quay lại".

7. **Luôn giữ OTE ở vị trí phụ thuộc [[12 - Daily Bias]], không bao giờ dùng nó để fade xu hướng.** OTE là một execution model — nó cho biết VÙNG GIÁ để vào lệnh theo một hướng đã được xác định trước bởi bias và nhịp displacement, không phải một tín hiệu độc lập để đoán đảo chiều. Long tại vùng OTE giữa một downtrend rõ ràng (khi nhịp kéo fib không hề phá cấu trúc theo hướng bullish) là bắt dao rơi, không phải OTE.

8. **Đặt stop nghiêm ngặt ngoài mốc 100% hoặc ngoài rìa của array confluence, không bao giờ đặt bên trong chính vùng OTE.** Stop bên trong vùng 62–79% gần như chắc chắn bị quét bởi nhiễu giá bình thường trước khi nhịp đi đúng hướng — đó là lỗi "stop quá sát" đã liệt kê trong bảng lỗi thường gặp. Stop hợp lý nằm ngoài đầu nhịp (100%) hoặc ngoài rìa xa của FVG/OB đang tạo confluence cho vùng, tùy điểm nào rộng hơn nhưng vẫn hợp lý với kế hoạch R:R.