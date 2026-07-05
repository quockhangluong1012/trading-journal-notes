---
type: ict-concept
concept: Central Bank Dealers Range
aliases:
  - CBDR
  - Central Bank Dealers Range
tags:
  - trading/ict/concept
  - trading/study
  - "#CBDR"
status: seed
category: Time & Price
timeframes:
  - D1
  - H1
  - M15
  - M5
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
importance: 5
last_reviewed: 2026-07-02
created: 2026-06-23
updated: 2026-07-02
common_mistakes:
  - "[[Mistake - Trade Every FVG]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
---

# Central Bank Dealers Range

> [!summary] Tóm tắt 1 câu
> **Central Bank Dealers Range (CBDR) là vùng tích lũy hẹp được đo từ ~14:00 đến 20:00 giờ New York (20:00–02:00 GMT trong cách dạy ICT cổ điển), dùng high–low của vùng này (lấy theo thân nến) làm "đơn vị" để chiếu các mức standard deviation (1x/2x/3x SD) lên trên và xuống dưới — những mức SD đó trở thành target / liquidity objective cho phiên Á và London sắp tới.**

> [!important] Nguyên tắc cốt lõi
> **CBDR chỉ có giá trị khi range NHỎ và "sạch" (lý tưởng ~40 pip với FX). CBDR là công cụ Time & Price để dự phóng target, KHÔNG phải tín hiệu entry.**
> Range càng rộng (do tin tức/biến động) thì SD projection càng vô nghĩa. CBDR mạnh nhất trên FX (EURUSD/GBPUSD), kém tin cậy trên indices/gold do biến động lớn và gap.

---

## 1. Định nghĩa

**Khái niệm:**
Central Bank Dealers Range là vùng giá tích lũy hình thành trong khoảng thời gian các dealer ngân hàng trung ương "án binh" cuối phiên New York, trước khi phiên Á mở. Trong cách dạy ICT cổ điển, cửa sổ đo là **14:00–20:00 giờ New York** (tương đương **20:00–02:00 GMT** tùy DST). Ta đo **high và low** của vùng này — ưu tiên dùng **thân nến (body)** thay vì bóng nến — để xác định kích thước range.

Từ kích thước range đó, ta chiếu các bội số **standard deviation (độ lệch chuẩn)** lên trên và xuống dưới: **+1 SD, +2 SD, +3 SD** và **-1 SD, -2 SD, -3 SD**. Mỗi SD = một lần chiều cao của CBDR. Các mức này trở thành **mục tiêu giá / vùng thanh khoản dự kiến** cho expansion của phiên Á và London. Xem thêm [[31 - Standard Deviation]] để hiểu bản chất phép chiếu.

![[CBDR-Advanced-SD-Projection.svg|697]]

> [!info] Thang SD chiếu từ range CBDR
> Range CBDR (đo theo thân nến) là "đơn vị" — mỗi bậc SD cách nhau đúng một chiều cao range. +2 SD trùng BSL thường là target chính; bias bullish thì ưu tiên phía trên, bias bearish ưu tiên phía dưới. Giá thường tôn trọng +1/+2 SD chứ hiếm khi chạm hết mọi bậc.

**Liên hệ với Asian Range & Flout:**
- **Asian Range** là một biến thể: đo range của riêng phiên Á (thường 19:00/20:00–00:00 NY) rồi chiếu SD tương tự.
- **Flout** là cách đo kết hợp CBDR + Asian Range để có một đơn vị range "trơn" hơn.
- Cả ba đều cùng một logic: lấy một vùng tích lũy hẹp làm đơn vị, rồi project SD để đoán target expansion.

**Mục đích trong ICT:**
- Cung cấp **target / draw on liquidity** đo lường được cho phiên sắp tới (giá thường chạy tới +1 hoặc +2 SD).
- Kết hợp với [[12 - Daily Bias]] để biết giá có khả năng chiếu lên SD trên (bias bullish) hay xuống SD dưới (bias bearish).
- Định khung **Premium/Discount tạm thời** quanh range tích lũy.
- Hỗ trợ canh **AMD** (Accumulation – Manipulation – Distribution): CBDR là pha Accumulation, manipulation thường quét một phía SD gần rồi distribution chạy về phía SD đối diện.

**Vì sao khái niệm này quan trọng:**
CBDR là một trong số ít công cụ ICT cho ra **target định lượng** thay vì chỉ định tính. Nó giúp trả lời "giá có thể chạy bao xa" trong phiên Á/London — đặc biệt hữu ích cho [[18 - Kill Zones]] London. Tuy nhiên nó nhạy cảm với chất lượng range: chỉ phát huy khi range hẹp và sạch.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Phiên Á/London tới giá có thể chạy tới target nào (theo SD)?
- Giá đang ở Premium hay Discount so với vùng tích lũy CBDR?
- Liquidity objective gần nhất nằm ở mức SD nào?
- Range đêm qua có đủ "sạch" để tin SD projection không?

### Central Bank Dealers Range không phải là gì
- Không phải tín hiệu entry — chỉ là khung target Time & Price.
- Không phải lúc nào cũng dùng được: range rộng/tin tức → bỏ.
- Không đáng tin trên NDX/XAUUSD như trên EURUSD/GBPUSD.
- Không thay thế bias: SD trên hay dưới được ưu tiên là do [[12 - Daily Bias]] quyết định.
- Không phải mọi SD đều bị chạm; thường giá tôn trọng +1/+2 SD là chính.

---

## 2. Bối cảnh sử dụng

### Các biến thể đo range

| Biến thể | Cửa sổ thời gian (NY) | Đo gì | Ghi chú |
|---|---|---|---|
| **CBDR** | ~14:00–20:00 | High–Low (body) cuối phiên NY | Lý tưởng ~40 pip FX |
| **Asian Range** | ~19:00/20:00–00:00 | High–Low phiên Á | Dùng khi phiên Á tích lũy gọn |
| **Flout** | Kết hợp CBDR + Asian | Trung bình/hợp nhất 2 range | Cho đơn vị "trơn" hơn |

![[CBDR-Advanced-Range-Variants.svg|697]]

> [!info] Ba cửa sổ đo trên cùng trục thời gian NY
> Cả ba biến thể chung một logic (lấy vùng tích lũy hẹp làm đơn vị rồi project SD), chỉ khác cửa sổ đo. Chọn CBDR khi cuối phiên NY tích lũy gọn; chuyển sang Asian Range khi CBDR dính đuôi tin NY nhưng phiên Á lại sạch; dùng Flout khi muốn một đơn vị SD "trơn", ít nhạy với một range lẻ méo.

> [!tip]
> Mặc định **đo theo thân nến (body)** trong cách dạy cổ điển để loại bỏ nhiễu bóng nến. Một số trader dùng cả high/low bóng — hãy nhất quán một cách đo và backtest riêng từng cách.

### Khi nào khái niệm này có giá trị cao?
- [ ] Range CBDR **hẹp** (~40 pip hoặc nhỏ hơn trên EURUSD/GBPUSD).
- [ ] Không có tin tức lớn rơi vào cửa sổ đo (NFP, FOMC, CPI...).
- [ ] Có [[12 - Daily Bias]] rõ ràng để chọn hướng SD ưu tiên.
- [ ] Đang giao dịch FX major (EURUSD/GBPUSD).
- [ ] Phiên London/NY sắp mở — cần target cho expansion.
- [ ] SD projection trùng với một POI HTF hoặc liquidity pool rõ.

### Khi nào nên bỏ qua?
- [ ] Range CBDR rộng bất thường (biến động/tin tức) → SD vô nghĩa.
- [ ] Giao dịch chỉ số/vàng (NDX, XAUUSD) — kém tin cậy, hay gap.
- [ ] Không có bias rõ, không biết ưu tiên SD trên hay dưới.
- [ ] Cuối tuần / ngày lễ thanh khoản mỏng, range méo.
- [ ] Có [[24 - New Week Opening Gap]] lớn làm lệch cấu trúc đo.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Cửa sổ thời gian:** đánh dấu vùng 14:00–20:00 NY (hoặc 20:00–02:00 GMT) trên chart M15/M5.
2. **High–Low của range:** xác định body high và body low của cụm nến tích lũy trong cửa sổ.
3. **Range nhỏ & sạch:** ít bóng dài, không có cú spike tin tức → range đáng tin.
4. **SD lines:** kẻ +1/+2/+3 SD và -1/-2/-3 SD, mỗi mức cách nhau đúng một chiều cao range.

### Điều kiện bắt buộc
- [ ] Xác định đúng cửa sổ thời gian theo múi giờ NY (lưu ý DST).
- [ ] Đo high–low theo quy ước nhất quán (body).
- [ ] Range đủ hẹp để SD có ý nghĩa.
- [ ] Vẽ đủ các mức SD cần dùng (tối thiểu ±1, ±2).

### Điều kiện tăng xác suất
- [ ] Range rất hẹp (≤ ~40 pip FX) → SD projection sắc nét.
- [ ] SD target trùng với liquidity pool ([[07 - Buy-side Liquidity]]/[[30 - Sell-side Liquidity]]) HTF.
- [ ] Bias rõ → ưu tiên một phía SD.
- [ ] Có manipulation quét SD gần trước khi expansion về SD xa (AMD).
- [ ] Phiên có volatility kỳ vọng (London/NY) để giá chạy đủ tới SD.

### Điều kiện làm setup yếu đi
- Range rộng do tin tức cuối phiên NY.
- Nhiều bóng nến dài làm high/low mơ hồ.
- Bias mâu thuẫn giữa các khung.
- Giao dịch sản phẩm biến động lớn (gold/indices).
- Tuần có ngày lễ, thanh khoản mỏng.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng CBDR
> 1. **Range CBDR đêm qua có hẹp & sạch không (≤ ~40 pip FX)?**
> 2. **Bias đang nghiêng về phía nào → ưu tiên SD trên hay dưới?**
> 3. **Mức SD nào trùng liquidity pool / POI HTF để làm target?**
> 4. **Có tin tức nào làm range/SD mất giá trị không?**

![[CBDR-Advanced-AMD-Cycle.svg|697]]

> [!info] CBDR đọc theo khung AMD
> CBDR chính là pha **Accumulation** (xem [[02 - AMD]]): vùng tích lũy hẹp làm gốc. **Manipulation** thường quét -1 SD / SSL ([[30 - Sell-side Liquidity]]) phiên Á để bẫy trước, rồi **Distribution** mới chạy expansion về +2 SD / BSL ([[07 - Buy-side Liquidity]]) đúng bias bullish. Timeline: NY cuối phiên → Á (sweep) → London (expansion).

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **Dealing range HTF:** giá đang Premium hay Discount của [[12 - Dealing Range]] lớn?
- **Liquidity target gần nhất:** BSL/SSL nào giá đang hướng tới — có trùng mức SD không?
- **POI HTF quan trọng:** FVG/OB D1/H4 nằm gần SD nào.

### H1 / M15 — POI & Context
- **POI đang quan sát:** mức SD nào (+1/+2) là target khả dĩ.
- **Lý do hợp lệ:** range CBDR hẹp + SD trùng pool thanh khoản.
- **Giá đã sweep liquidity chưa:** manipulation thường quét SD gần đối diện bias trước.
- **Phản ứng:** giá có reject ở SD gần hay xuyên qua hướng tới SD xa.

### M5 / M1 — Confirmation & Entry
- **CBDR không cho entry trực tiếp** — nó cho target. Entry vẫn theo ICT 2022: sweep → MSS → displacement → FVG.
- **Dùng SD làm TP:** đặt target tại +1/+2 SD đồng hướng bias.
- **Có MSS không?** xác nhận hướng expansion về SD đối diện.
- **Stop logic:** ngoài điểm sweep manipulation, không phải tại mức SD.

```text
Mẫu ghi nhanh — CBDR Projection (Long bias)
Cửa sổ: 14:00–20:00 NY | Range (body): [low]–[high] = ~XX pip (hẹp, sạch)
Bias: Bullish → ưu tiên SD trên
SD: +1 SD = [level], +2 SD = [level] (trùng BSL → target chính)
Manipulation kỳ vọng: quét -1 SD / SSL phiên Á trước
Expansion: sau sweep + MSS bullish → chạy về +1/+2 SD
Entry: theo ICT 2022 tại discount sau sweep
TP: +1 SD (TP1), +2 SD / BSL (TP2)
Invalid: đóng nến vượt -2 SD ngược bias / range gốc quá rộng
```

> [!warning]
> Đừng "vào lệnh tại mức SD" như thể nó là support/resistance cứng. SD là **bản đồ target**; entry vẫn phải tuân theo sweep + displacement + FVG đúng context.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Range CBDR hẹp, sạch, đo nhất quán.
- [ ] Bias rõ và SD ưu tiên đồng hướng bias.
- [ ] SD target trùng liquidity pool / POI HTF (confluence).
- [ ] Manipulation quét SD gần trước khi expansion (AMD).
- [ ] Entry độc lập theo ICT 2022, dùng SD chỉ làm target.

### Setup bị vô hiệu khi
- [ ] Range gốc quá rộng / có spike tin tức → SD không tin cậy.
- [ ] Giá đóng nến vượt sâu qua SD ngược bias mà không phản ứng.
- [ ] Bias không rõ, không biết chọn SD nào.
- [ ] Sản phẩm biến động lớn (indices/gold) làm SD lệch nhiều.
- [ ] Gap đầu tuần ([[24 - New Week Opening Gap]]) làm méo cấu trúc.

![[CBDR-Advanced-Clean-vs-Dirty.svg|697]]

> [!info] Range sạch vô hiệu hóa range bẩn
> Bên trái là range **sạch** (~40 pip, ít bóng, đo body): SD sắc nét, giá chạy tới +1/+2 SD. Bên phải là range **bẩn** (>90 pip do tin tức, bóng dài, đo cả wick): SD bị đẩy ra xa vô nghĩa, giá lẹt đẹt không chạm nổi +1 SD. Range bẩn là điều kiện vô hiệu hóa hàng đầu — thấy nó thì bỏ phiên, đừng cố ép SD.

### Đọc phản ứng tại các mức SD

| Quan sát | Ý nghĩa | Cách đọc hợp lý |
|---|---|---|
| Giá quét -1 SD rồi reject mạnh (bias bullish) | Manipulation hoàn tất | Chờ entry Long, target +1/+2 SD |
| Giá chạm +1 SD rồi consolidate | Đạt target trung gian | Cân nhắc chốt một phần, theo dõi tiếp +2 SD |
| Giá xuyên +2 SD dễ dàng | Momentum mạnh | +3 SD hoặc liquidity HTF làm target kế |
| Giá không tới nổi +1 SD, quay đầu | Range gốc sai/bias yếu | Xem lại chất lượng CBDR & bias |

### Nâng cao — Kết hợp CBDR SD với Silver Bullet / Kill Zones (target × timing)

CBDR và [[18 - Kill Zones]] trả lời hai câu hỏi khác nhau và **bổ sung** cho nhau, không thay thế: **CBDR nói giá đi BAO XA (target theo SD), Kill Zone / Silver Bullet nói vào lệnh KHI NÀO (timing).** Một setup chất lượng cao là khi hai trục này giao nhau: SD projection cho một target đo lường được, còn kill zone cung cấp cửa sổ thanh khoản để cú expansion thực sự chạy tới target đó.

Trình tự thực chiến để ghép hai công cụ:
1. **Đêm/pre-market:** đo CBDR, project SD, đánh dấu mức SD nào trùng liquidity pool HTF ([[07 - Buy-side Liquidity]] / [[30 - Sell-side Liquidity]]). Đây là "bản đồ target" tĩnh cho ngày.
2. **Kill zone mở (London 02:00–05:00 NY hoặc NY AM 08:30–11:00):** chờ manipulation quét SD gần đối diện bias, rồi entry theo ICT 2022 (sweep → MSS → displacement → FVG). Silver Bullet (10:00–11:00 NY) là cửa sổ hẹp đặc biệt hợp để "bóp cò" khi SD target đã rõ.
3. **Quản lý:** dùng +1 SD làm TP1 (thường trong tầm với của một kill zone), +2 SD / BSL làm TP2. Nếu +2 SD nằm quá xa so với range trung bình một phiên của sản phẩm, hạ kỳ vọng xuống +1 SD.

| Bối cảnh | Vai trò CBDR (target) | Vai trò Kill Zone / Silver Bullet (timing) | Ghép lại |
|---|---|---|---|
| London Open, bias bullish | +1/+2 SD trên = draw on liquidity | London KZ cung cấp expansion mạnh nhất trong ngày | SD trùng BSL + KZ London = xác suất cao nhất |
| NY AM, đã lỡ London | +2 SD / BSL còn mở phía trên | NY AM / Silver Bullet cho nhịp continuation | Vào nhịp NY nếu SD chưa bị lấy hết |
| Ngoài kill zone (giữa ngày) | SD vẫn là bản đồ | Thanh khoản mỏng, dễ tạo sweep giả | Giữ SD làm tham chiếu, KHÔNG entry |
| Phiên Á | -1 SD hay bị quét (manipulation) | Á thường là pha bẫy, không phải expansion | Coi sweep Á là tín hiệu chuẩn bị, chờ London |

> [!tip]
> Ghi vào journal cặp `sd_target_hit` × `kill_zone`: bạn sẽ nhanh chóng thấy phần lớn lần chạm +1/+2 SD "chất lượng" rơi vào đúng cửa sổ London / NY AM, còn các lần chạm ngoài KZ thường là nhiễu — dữ liệu này giúp bạn ngừng trade CBDR ngoài giờ có edge.

### Nâng cao — Vì sao SD kém tin trên indices/gold: gap, volatility và cách hiệu chỉnh

CBDR sinh ra và được kiểm chứng chủ yếu trên **FX major** (EURUSD/GBPUSD) — nơi thị trường gần như liên tục 24h, range đêm hình thành sạch, và biến động phiên tương đối đồng nhất. Trên **indices (NDX/NAS100, ES)** và **gold (XAUUSD)**, ba yếu tố cấu trúc làm SD projection lệch nhiều:

- **Gap phiên/cash open:** indices có phiên cash (RTH) và gap giữa các phiên; giá "nhảy" qua các mức SD thay vì chạy liền mạch, khiến mức SD không được test đúng như FX.
- **Volatility cao & không đồng nhất:** ATR của NDX/XAUUSD lớn và co giãn mạnh theo tin tức; một range đêm hẹp có thể bị một phiên RTH biến động gấp nhiều lần, làm +1/+2 SD trở nên quá gần (bị xuyên tức thì) hoặc quá xa (không bao giờ tới).
- **Thanh khoản phân mảnh theo phiên:** dealer FX "án binh" cuối NY tạo range tích lũy có ý nghĩa; indices/gold không có cùng cơ chế micro-structure đó ở cửa sổ CBDR cổ điển.

Cách hiệu chỉnh nếu vẫn muốn thử CBDR trên các sản phẩm này:

| Vấn đề | Biểu hiện | Cách hiệu chỉnh |
|---|---|---|
| Gap làm lệch mốc | Giá mở nhảy qua SD | Đo range trên cửa sổ khớp phiên đang trade (dùng Asian Range cho phiên Á-Âu), tránh bắc cầu qua gap |
| Range chuẩn hóa theo pip vô nghĩa | "~40 pip" không áp được cho NDX/XAUUSD | Chuẩn hóa theo **ATR / % giá** thay vì pip tuyệt đối; định nghĩa "hẹp" = range đêm < X% ATR ngày |
| SD bị xuyên tức thì | +1 SD chạm trong vài phút rồi đi tiếp | Giãn kỳ vọng: dùng +2/+3 SD làm target chính, +1 SD chỉ là trạm trung gian |
| Kết quả nhiễu, khó tin | Win rate thất thường | **Backtest riêng từng sản phẩm** ≥20–30 mẫu trước khi dùng tiền thật; nếu thống kê không có edge → bỏ hẳn CBDR cho sản phẩm đó |

> [!warning]
> Đừng "port" các con số của EURUSD sang NDX/XAUUSD. ~40 pip là ngưỡng của FX; trên indices/gold, khái niệm "range hẹp & sạch" phải được **định nghĩa lại bằng ATR/%**, và chỉ sau khi có dữ liệu backtest riêng. Mặc định của vault: ưu tiên EURUSD/GBPUSD, cẩn trọng hoặc bỏ trên NDX/XAUUSD.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Central-Bank-Dealers-Range-Example-Correct.svg|697]]

**Mô tả:**
Range CBDR 14:00–20:00 NY hẹp (~40 pip), đo theo thân nến. Bias D1 bullish nên ưu tiên SD trên. Phiên London mở, giá quét nhẹ -1 SD (manipulation) rồi displacement tăng phá cấu trúc, chạy thẳng tới +2 SD đúng nơi có BSL HTF. SD projection đóng vai bản đồ target, entry thực hiện theo ICT 2022 tại discount sau sweep.

**Vì sao đây là ví dụ tốt:**
- Range hẹp & sạch → SD đáng tin.
- Đo theo body, nhất quán.
- SD trên đồng hướng bias, +2 SD trùng liquidity pool.
- Giá tôn trọng cấu trúc AMD: quét SD gần → expansion về SD xa.

### Ví dụ sai / dễ nhầm
![[Central-Bank-Dealers-Range-Example-Wrong.svg|691]]

**Mô tả lỗi:**
Cửa sổ đo dính tin tức cuối phiên NY, các nến có bóng dài, range bị tính cả bóng → rộng hơn 90 pip. SD projection vì thế bị đẩy ra quá xa, không khả thi. Giá lẹt đẹt trong range cả phiên Á/London, không bao giờ tới +1 SD. Trader đặt TP tại SD và lệnh không bao giờ chạm target.

**Bài học:**
- Range rộng/dính tin → SD vô giá trị, bỏ qua phiên đó.
- Đo theo body, loại bóng nến nhiễu để giữ range "sạch".
- CBDR là công cụ có điều kiện, không phải lúc nào cũng áp dụng.

---
### Sequence mẫu — Dùng CBDR làm target cho Long phiên London
```text
HTF Bullish Bias
→ Đo CBDR 14:00–20:00 NY (range hẹp ~40 pip, body)
→ Project +1/+2 SD lên trên (trùng BSL → target chính)
→ Phiên Á/London: manipulation quét -1 SD / SSL (sweep)
→ Displacement tăng + MSS bullish (entry theo ICT 2022)
→ Entry tại discount sau sweep, quanh CE của FVG
→ TP1 = +1 SD; TP2 = +2 SD / BSL
→ Invalid: range gốc rộng hoặc đóng nến vượt -2 SD ngược bias
```

> [!note]
> CBDR + Silver Bullet kết hợp tốt: SD cho target, Silver Bullet kill zone cho timing entry. CBDR trả lời "đi bao xa", Silver Bullet trả lời "vào lúc nào".

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> CBDR chỉ có giá trị khi range hẹp & sạch + bias rõ. Nó là **target tool**, không phải entry signal.

### A. Context (HTF)
- [ ] Daily Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] Đo CBDR theo cửa sổ NY đúng (lưu ý DST), theo body.
- [ ] Range hẹp & sạch (≤ ~40 pip FX), không dính tin tức.
- [ ] Đang giao dịch FX major (không phải indices/gold).
- [ ] SD ưu tiên đồng hướng bias.
- [ ] SD target trùng liquidity pool / POI HTF.

### B. Execution (LTF)
- [ ] Manipulation quét SD gần đối diện bias trước khi expansion.
- [ ] Entry theo ICT 2022 (sweep → MSS → displacement → FVG), KHÔNG vào "tại mức SD".
- [ ] Dùng +1/+2 SD làm TP, không phải làm entry trigger.
- [ ] Stop logic ngoài điểm sweep, không phải tại mức SD.
- [ ] R:R đạt kế hoạch khi target là SD.

### C. Quy tắc "không có lệnh"
- [ ] Range gốc rộng / dính tin → không dùng SD.
- [ ] Bias không rõ → không chọn được SD → không trade theo CBDR.
- [ ] Sản phẩm biến động lớn (NDX/XAUUSD) → cẩn trọng / bỏ.
- [ ] Gap đầu tuần làm méo range → bỏ.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Đo sai khung giờ | Lấy nhầm múi giờ, quên DST | SD lệch hoàn toàn | Chuẩn hóa theo NY time, kiểm tra DST |
| Dùng CBDR khi range rộng | Range >40 pip do tin tức | SD quá xa, vô nghĩa | Chỉ dùng khi range hẹp & sạch |
| Đo cả bóng nến tùy tiện | High/low lấy theo spike | Range phồng lên, SD sai | Đo theo body, nhất quán một cách |
| Coi SD là entry signal | Vào lệnh ngay tại mức SD | SD là target, không phải tín hiệu | Entry theo ICT 2022, SD chỉ làm TP |
| Dùng trên gold/indices | Áp CBDR cho XAUUSD/NDX | Biến động/gap làm SD kém tin | Ưu tiên EURUSD/GBPUSD |
| Bỏ qua bias khi chọn SD | Project cả 2 phía như nhau | Mất hướng, kỳ vọng sai | Để Daily Bias quyết định SD ưu tiên |
| Kỳ vọng giá chạm mọi SD | Ôm lệnh chờ +3 SD | Phần lớn chỉ tới +1/+2 SD | Chốt từng phần tại +1/+2 SD |

---

## 10. Câu hỏi tự kiểm tra

- Mình giải thích được cửa sổ thời gian CBDR và cách project SD trong 30 giây không?
- Range đêm qua có đủ hẹp & sạch để tin SD không?
- Bias đang nghiêng đâu → SD nào được ưu tiên?
- Mức SD nào trùng liquidity pool để làm target tốt nhất?
- CBDR dùng để xác định **target** chứ không phải entry — mình có nhầm vai trò không?
- Sản phẩm đang trade có phù hợp với CBDR (FX) không?
- Điều gì làm CBDR của hôm nay bị invalid?
- Setup nào trong journal đã dùng SD làm target đúng/sai?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** CBDR được đo trong khung thời gian nào?
**Đáp:** Khoảng 14:00–20:00 giờ New York (≈ 20:00–02:00 GMT trong cách dạy ICT cổ điển), cuối phiên NY trước khi phiên Á mở.

### Q2
**Hỏi:** Đo high–low của CBDR theo body hay bóng nến?
**Đáp:** Cách dạy cổ điển ưu tiên dùng **thân nến (body)** để loại nhiễu bóng nến; cần nhất quán và backtest.

### Q3
**Hỏi:** Standard deviation projection (1x/2x/3x SD) dùng để làm gì?
**Đáp:** Làm **target / liquidity objective** cho expansion của phiên Á/London. Mỗi SD = một lần chiều cao range CBDR, chiếu lên trên và xuống dưới.

### Q4
**Hỏi:** CBDR lý tưởng có kích thước thế nào và hợp sản phẩm nào?
**Đáp:** Lý tưởng range **nhỏ (~40 pip)** trên FX (EURUSD/GBPUSD); kém tin cậy trên indices/gold do biến động & gap.

### Q5
**Hỏi:** CBDR là tín hiệu entry hay công cụ target?
**Đáp:** Là **công cụ target Time & Price**, không phải tín hiệu entry. Entry vẫn theo sweep → MSS → displacement → FVG.

### Q6
**Hỏi:** Asian Range và Flout liên quan gì tới CBDR?
**Đáp:** Cùng logic "lấy vùng tích lũy hẹp làm đơn vị rồi project SD". Asian Range đo riêng phiên Á; Flout hợp nhất CBDR + Asian Range cho đơn vị trơn hơn.

---

## 12. Lesson Learned

### Bài học chính
- CBDR là **target tool**, không phải entry signal.
- Chất lượng range quyết định tất cả: hẹp & sạch mới đáng tin.
- Đo theo body, nhất quán, chú ý múi giờ NY và DST.
- SD ưu tiên phải đồng hướng [[12 - Daily Bias]].
- Mạnh trên FX major; cẩn trọng trên gold/indices.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ project SD khi range CBDR hẹp & sạch (≤ ~40 pip FX).
- [ ] Tôi dùng SD làm TP, không bao giờ vào lệnh "tại mức SD".
- [ ] Tôi để Daily Bias quyết định SD trên hay dưới được ưu tiên.
- [ ] Tôi không dùng CBDR trên XAUUSD/NDX trừ khi đã backtest riêng.

### Câu nhắc nhở khi trade
> **"CBDR cho tôi biết giá đi BAO XA, không cho tôi biết vào lệnh KHI NÀO. Range bẩn thì bỏ."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có nắm cửa sổ giờ, cách đo body, và SD projection không? |
| Nhận diện trên chart |  | Có vẽ đúng range & các mức SD không? |
| Biết khi nào bỏ qua |  | Có dám bỏ range rộng/dính tin/gold không? |
| Kết hợp với context HTF |  | SD có được dùng cùng bias + liquidity pool không? |
| Áp dụng vào trade thực tế |  | Có dùng SD làm TP đúng và entry theo ICT 2022 không? |
| Review sau trade |  | Có thống kê tỉ lệ chạm SD bằng dữ liệu journal không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 lệnh có gắn tag `[[Central Bank Dealers Range]]`.
- [ ] Thống kê tỉ lệ giá chạm +1/+2/+3 SD theo độ "sạch" của range.
- [ ] So sánh độ tin cậy SD trên EURUSD/GBPUSD vs XAUUSD/NDX.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## 14. Best Practices

> [!success] Nguyên tắc vàng
> **"CBDR cho tôi biết giá đi BAO XA, không cho tôi biết vào lệnh KHI NÀO."** CBDR là công cụ Time & Price để dự phóng target (SD), không phải tín hiệu entry — và nó chỉ đáng tin khi range đêm qua HẸP & SẠCH. Range bẩn (rộng, dính tin, nhiều bóng) → bỏ phiên đó, đừng ép SD.

1. **Lọc chất lượng range TRƯỚC khi project SD.** Chỉ đo và chiếu SD khi range CBDR hẹp (~40 pip hoặc nhỏ hơn trên FX major) và sạch (ít bóng dài, không spike tin tức). Ghi trường `range_width_pip` và `clean_dirty` cho mỗi phiên; sau 20–30 mẫu bạn sẽ thấy rõ SD từ range sạch có tỉ lệ chạm target cao hơn hẳn range bẩn.

2. **Chuẩn hóa cửa sổ giờ theo New York và luôn kiểm tra DST.** Sai múi giờ hoặc quên đổi giờ mùa làm lệch toàn bộ range → SD sai từ gốc. Cố định cửa sổ 14:00–20:00 NY (hoặc biến thể Asian Range/Flout bạn đã chọn) và đánh dấu sẵn trên chart để không đo nhầm.

3. **Đo theo thân nến (body), nhất quán một quy ước.** Bóng nến gây nhiễu làm range phồng lên và đẩy SD ra xa vô lý. Dùng body high/low theo cách dạy cổ điển, và nếu muốn thử đo cả bóng thì backtest riêng — đừng đổi qua lại giữa hai cách trong cùng một hệ thống.

4. **Để Daily Bias quyết định phía SD ưu tiên.** CBDR chiếu cả SD trên lẫn dưới, nhưng chỉ một phía là target chính theo [[12 - Daily Bias]]: bias bullish → ưu tiên +SD (BSL phía trên); bias bearish → ưu tiên −SD. Không có bias rõ → không chọn được SD → không trade theo CBDR.

5. **Chỉ trade khi SD target trùng một liquidity pool / POI HTF (confluence).** Một mức +2 SD đơn thuần yếu hơn nhiều so với +2 SD trùng BSL/PDH hoặc một FVG HTF. Ưu tiên các phiên mà SD projection rơi đúng vào [[07 - Buy-side Liquidity|BSL]]/[[30 - Sell-side Liquidity|SSL]] có ý nghĩa — đó là nơi giá thực sự bị hút về.

6. **Dùng SD làm TP, entry theo ICT 2022; kết hợp Kill Zone cho timing.** CBDR trả lời "đi bao xa", [[18 - Kill Zones]]/Silver Bullet trả lời "vào lúc nào". Vào lệnh theo chuỗi sweep → MSS → displacement → FVG tại discount/premium, đặt +1 SD làm TP1 và +2 SD (hoặc pool trùng) làm TP2; stop nằm ngoài điểm sweep, KHÔNG tại mức SD.

7. **Cẩn trọng trên gold/indices và backtest riêng từng sản phẩm.** NDX/XAUUSD biến động lớn và hay gap khiến SD kém tin cậy hơn EURUSD/GBPUSD. Đừng áp cùng một kỳ vọng SD cho mọi sản phẩm — thống kê tỉ lệ chạm +1/+2/+3 SD riêng cho từng cặp/phiên qua 20–30 mẫu ([[04 - Backtesting]]) rồi mới đưa vào playbook.
