---
type: ict-concept
concept: Liquidity Void
aliases:
  - Liquidity Void
  - Liquidity Gap
  - Liquidity Vacuum
  - LV
tags:
  - trading/ict/concept
  - trading/study
  - "#LiquidityVoid"
status: seed
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[ICT 2022 Model]]"
importance: 4
confidence: 1
last_reviewed:
created: 2026-06-24
updated: 2026-06-24
related_concepts:
  - "[[Fair Value Gap]]"
  - "[[34 - Vacuum Block]]"
  - "[[29 - Sell-side Imbalance Buy-side Inefficiency]]"
  - "[[Displacement]]"
  - "[[19 - Liquidity]]"
  - "[[12 - Daily Bias]]"
prerequisites:
  - "[[Fair Value Gap]]"
  - "[[Displacement]]"
  - "[[27 - Premium Discount]]"
common_mistakes: []
---

# Liquidity Void

> [!summary] Tóm tắt 1 câu
> **Liquidity Void là một vùng giá rộng bị "xuyên thủng" bởi một cú di chuyển một chiều cực nhanh (displacement), gần như không có giao dịch hai chiều — để lại một khoảng kém hiệu quả (inefficiency) mà giá có xu hướng quay lại lấp đầy (rebalance) hoặc lao thẳng qua như một mục tiêu (draw on liquidity).**

> [!important] Nguyên tắc cốt lõi
> **Thị trường ghét sự kém hiệu quả.** Khi giá đi quá nhanh chỉ về một phía, nó bỏ lại một "chân không" thanh khoản nơi cả buy-side lẫn sell-side đều chưa được khớp đầy đủ. Algo coi vùng này vừa là **nam châm để cân bằng lại (magnet to rebalance)**, vừa là **đường cao tốc để chạy nhanh tới phía xa (price seeks the far side)**. Điều quyết định nó đóng vai trò nào chính là **bias + ngữ cảnh premium/discount + nơi thanh khoản thật sự nằm**.

---

## 1. Định nghĩa

### Khái niệm
**Liquidity Void (LV)** — còn gọi là *Liquidity Gap* hoặc *Liquidity Vacuum* — là một **dải giá** mà thị trường đi qua bằng một loạt nến displacement mạnh, gần như không có sự chồng lấp (overlap) giữa thân các nến và rất ít giao dịch hai chiều. Kết quả là một khu vực **mỏng thanh khoản**, nơi giá "trượt" qua thay vì "đi bộ" qua.

Khác với một [[Fair Value Gap]] đơn lẻ (khoảng trống ba nến rất cụ thể), Liquidity Void là một **khái niệm vùng rộng hơn**: nó thường **bao trùm nhiều FVG liên tiếp**, nhiều [[Order Block]] bị bỏ lại, và thường nối liền hai cụm thanh khoản (ví dụ từ một [[20 - Liquidity Sweep]] ở đáy lên tới buy-side liquidity ở đỉnh).

### Bản chất
- Là hệ quả trực tiếp của **[[Displacement]]** — không có displacement thì không có void.
- Là một **PD Array** ([[27 - Premium Discount]] array) ở cấp độ vùng: nó nằm hẳn trong premium hoặc discount của [[12 - Dealing Range]], và điều đó quyết định ta tiếp cận nó thế nào.
- Là một **inefficiency mang tính cấu trúc**: thị trường ghi nhớ rằng vùng này chưa được giao dịch hai chiều và sẽ tìm cách trả lại sự cân bằng.

### Mục đích trong ICT
1. **Làm TARGET (draw on liquidity):** khi giá vừa quét thanh khoản và mở ra một void phía trước, void đó trở thành "đường băng" để giá lao tới phía xa rất nhanh. Ta giao dịch *theo* hướng void.
2. **Làm MAGNET (rebalance):** một void cũ phía sau giá là vùng kém hiệu quả chưa được lấp; giá có xu hướng quay lại "rebalance" nó. Ta giao dịch *retracement* về void.
3. **Lọc bias:** nếu phía trên có void chưa lấp và phía dưới cũng có void chưa lấp, void nào "gần nguồn thanh khoản hơn" thường là draw mạnh hơn — giúp xác nhận [[12 - Daily Bias]].

### Vì sao quan trọng
Vì void trả lời được câu hỏi mà nhiều trader hay bỏ sót: **"Giá đang bị HÚT về đâu, và đi đến đó nhanh hay chậm?"** Một FVG cho ta điểm vào (POI); một Liquidity Void cho ta **đoạn đường giá có thể đi rất nhanh** và **mục tiêu giá có thể chạy thẳng tới**. Nó là cầu nối giữa "vào lệnh ở đâu" và "thoát lệnh ở đâu".

### Nó giúp trả lời câu hỏi nào trên chart?
- Sau cú displacement này, **đoạn nào giá có thể trượt nhanh không cản trở?**
- Vùng nào phía sau giá **chưa được giao dịch hai chiều** và có thể bị kéo về để lấp?
- Mục tiêu (TP) hợp lý của tôi có nằm **ở phía xa của một void** không?
- Khi giá pullback, nó đang **lấp lại void** (lành mạnh) hay đang **xuyên qua void mới** (đảo chiều/thay đổi bias)?

### Liquidity Void không phải là gì
- **Không phải** chỉ là một FVG đơn lẻ — void rộng hơn, thường chứa nhiều FVG.
- **Không phải** một điểm vào lệnh chính xác — nó là một *vùng/đoạn đường*; điểm vào cụ thể vẫn đến từ [[Fair Value Gap]], [[Order Block]] hay [[Optimal Trade Entry]] *bên trong* hoặc *ở rìa* void.
- **Không phải** lúc nào cũng được lấp 100% — fill có thể là partial (lấp một phần rồi đi tiếp).
- **Không phải** tín hiệu vào lệnh độc lập — nó cần [[20 - Liquidity Sweep]] + bias + premium/discount mới có giá trị.
- **Không phải** gap cuối tuần thuần túy (weekend gap) — dù gap cũng là một dạng inefficiency, void ở đây là khái niệm intraday/cấu trúc do displacement.

### Void vs FVG vs Imbalance (phân biệt cốt lõi)

| Tiêu chí | **Liquidity Void** | **Fair Value Gap (FVG)** | **Imbalance (SIBI/BISI)** |
|---|---|---|---|
| Quy mô | Vùng RỘNG, cả một đoạn đường | Khoảng trống 3 nến rất cụ thể | Thuật ngữ tổng quát cho mất cân bằng giao dịch |
| Cấu trúc đo | Toàn bộ dải displacement, thiếu overlap | Khoảng giữa nến 1 và nến 3 (nến giữa bỏ lại) | Một phía (buy hoặc sell) bị bỏ trống |
| Vai trò chính | TARGET + MAGNET (draw / rebalance) | POI / điểm vào lệnh | Mô tả tính chất của khoảng trống |
| Số lượng FVG bên trong | Thường chứa NHIỀU FVG | Là một đơn vị | — |
| Liên hệ | Bao trùm FVG | Là "viên gạch" cấu thành void | [[29 - Sell-side Imbalance Buy-side Inefficiency]] là loại imbalance |
| Cách dùng điển hình | "Giá sẽ chạy/quay về vùng này" | "Tôi vào lệnh tại đây" | "Vùng này thiếu giao dịch ở phía X" |

> [!tip] Cách nhớ nhanh
> **FVG là viên gạch — Liquidity Void là cả bức tường.** Khi ta nói "giá sẽ chạy tới đó", thường ta đang nói về void. Khi ta nói "tôi vào tại đó", thường ta đang nói về một FVG cụ thể bên trong/cạnh void.

---

## 2. Bối cảnh sử dụng

Liquidity Void có hai vai trò trái ngược nhau — và phần khó nhất là biết *lúc nào nó là target, lúc nào nó là rebalance magnet*.

### Các loại / trạng thái

| Loại / trạng thái | Mô tả | Vai trò | Cách giao dịch |
|---|---|---|---|
| **Void làm TARGET** | Giá vừa sweep thanh khoản, displacement mở ra void phía trước | Draw on liquidity — giá lao tới phía xa | Vào theo hướng void, TP ở phía xa của void |
| **Void làm MAGNET (rebalance)** | Void cũ phía sau giá, chưa lấp | Nam châm hút giá quay lại | Chờ retracement về void rồi vào theo bias gốc |
| **Void đang được lấp (filling)** | Giá đang pullback vào trong void | Trung tính — đang cân bằng | Quan sát phản ứng tại các FVG/OB bên trong |
| **Void đã lấp đầy (full fill)** | Giá đã trượt hết qua void | Hết "nhiên liệu" — void không còn là draw | Bỏ qua như một POI; tìm void/draw kế tiếp |
| **Void lấp một phần (partial fill)** | Giá chỉ vào tới [[10 - Consequent Encroachment (Mean Threshold)]] hoặc rìa rồi đi tiếp | Còn hiệu lực một phần | CE thường là điểm chốt/đảo chiều của pullback |
| **Void mới ngược hướng** | Pullback tạo displacement & void ngược lại | Cảnh báo đổi bias / [[21 - Market Structure Shift]] | Đánh giá lại bias, không vào theo hướng cũ |

### Khi nào có giá trị cao?
- [ ] Void hình thành **ngay sau một [[20 - Liquidity Sweep]]** (sweep → displacement → void) trong [[18 - Kill Zones]].
- [ ] Void nằm đúng **premium (cho lệnh Short)** hoặc **discount (cho lệnh Long)** của [[12 - Dealing Range]].
- [ ] Void **cùng hướng với [[12 - Daily Bias]]** và trỏ về một cụm thanh khoản rõ ràng ([[07 - Buy-side Liquidity]] / [[30 - Sell-side Liquidity]]).
- [ ] Void **chưa được lấp** và là khoảng trống "sạch" (ít overlap, nến body dài).
- [ ] Có **[[Displacement]]** rõ ràng tạo void (không phải dao động lình xình).
- [ ] Void mở ra trong/đầu một phiên ([[02 - AMD]] — manipulation → distribution).

### Khi nào nên bỏ qua?
- [ ] Void **đã được lấp đầy 100%** từ trước — không còn là draw.
- [ ] Void hình thành do **tin tức bất thường** mà không khớp bias HTF (rủi ro whipsaw).
- [ ] Void quá **nhỏ và bị overlap nhiều** — đó chỉ là dao động bình thường, không phải inefficiency thực.
- [ ] Void nằm **ngược premium/discount** so với hướng định vào (ví dụ muốn Long nhưng void nằm sâu trong premium).
- [ ] Thị trường đang trong vùng **consolidation** không có displacement — void không đáng tin.
- [ ] Không có cụm thanh khoản rõ ràng ở phía xa của void (không có "mồi" để giá chạy tới).

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Một loạt nến displacement** cùng chiều, body dài, bóng nến ngắn, đóng cửa gần đỉnh/đáy nến.
2. **Thiếu overlap**: thân nến sau gần như không chồng lên thân nến trước — giá "nhảy bậc".
3. **Chứa một hoặc nhiều [[Fair Value Gap]]** liên tiếp bên trong dải đó.
4. **Hai đầu void** thường gắn với điểm bắt đầu (sau sweep / [[Order Block]]) và điểm kết thúc (gần một cụm thanh khoản).
5. **Volume/range bất thường** so với các nến lân cận (di chuyển nhanh, biên độ lớn).
6. Trên khung lớn nhìn như **một "cây nến đơn" dài** hoặc một đoạn dốc đứng gần như thẳng đứng.

### Ma trận nhận diện

| Thành phần | Bắt buộc? | Mô tả nhận diện | Nếu thiếu |
|---|---|---|---|
| Displacement | Bắt buộc | Chuỗi nến body dài, một chiều | Không phải void, chỉ là dao động |
| Thiếu overlap giữa các nến | Bắt buộc | Giá nhảy bậc, ít giao thoa | Vùng đã "cân bằng", không phải void |
| ≥1 FVG bên trong | Tăng xác suất | Đếm FVG liên tiếp | Void yếu, dễ bị nghi ngờ |
| Sweep ngay trước void | Tăng xác suất | [[20 - Liquidity Sweep]] tạo "nhiên liệu" | Void thiếu lý do, dễ là bẫy |
| Cụm thanh khoản ở phía xa | Tăng xác suất | BSL/SSL làm "mồi" | Void không có target rõ ràng |
| Nằm đúng premium/discount | Tăng xác suất | Theo [[27 - Premium Discount]] | Vào lệnh kém lợi thế |
| Đã lấp một phần | Làm yếu đi | Giá đã đi vào một phần void | Còn lại ít "nhiên liệu" |
| Overlap nhiều, nến nhỏ | Làm yếu đi | Vùng lình xình | Không nên xem là void |

### Điều kiện bắt buộc
- [ ] Có **[[Displacement]]** thật sự (không phải tin đồn về biến động).
- [ ] Vùng **thiếu giao dịch hai chiều** rõ ràng (thiếu overlap).
- [ ] Xác định được **hai biên** của void (đỉnh và đáy của dải).

### Điều kiện tăng xác suất
- [ ] Void hình thành **sau [[20 - Liquidity Sweep]]**.
- [ ] Bên trong có **FVG liên tiếp** và/hoặc [[29 - Sell-side Imbalance Buy-side Inefficiency]].
- [ ] Phía xa của void có **cụm thanh khoản** rõ (equal highs/lows, old high/low).
- [ ] Void **cùng hướng [[12 - Daily Bias]]** và nằm đúng premium/discount.

### Điều kiện làm yếu đi
- [ ] Void **đã lấp phần lớn** hoặc đã chạm [[10 - Consequent Encroachment (Mean Threshold)]].
- [ ] Void hình thành trong **consolidation** hoặc do **tin tức lệch bias**.
- [ ] **Overlap nhiều** giữa các nến — chất lượng inefficiency thấp.
- [ ] Không có **draw on liquidity** rõ ràng ở phía xa.

---

## 4. Quy trình phân tích đa khung thời gian

> Nguyên tắc: **HTF xác định void nào là draw + premium/discount; LTF tinh chỉnh điểm vào và xác nhận displacement.**

### D1 / H4 — Bias & bản đồ void lớn
- Xác định [[12 - Daily Bias]] và [[12 - Dealing Range]] tổng (HTF premium/discount).
- Đánh dấu các **void HTF chưa lấp** (gắn với swing displacement lớn) — đây là các *draw* tầm xa.
- Xác định cụm thanh khoản chính ([[07 - Buy-side Liquidity]] / [[30 - Sell-side Liquidity]]) mà giá có thể bị hút tới.
- Quyết định: void nào là **target** (cùng hướng bias) và void nào có thể là **magnet rebalance** ngược chiều.

### H1 / M15 — Cấu trúc & lựa chọn kịch bản
- Tìm [[20 - Liquidity Sweep]] gần nhất → có displacement → có void mới mở ra không?
- Xác định [[21 - Market Structure Shift]] / [[Break of Structure]] xác nhận hướng.
- Khoanh vùng void H1/M15 nằm trong premium/discount đúng phía → đây là vùng làm việc.
- Xác định xem ta đang **đi tới void** (target) hay **chờ giá quay về void** (rebalance).

### M5 / M1 — Tinh chỉnh & vào lệnh
- Chờ giá tương tác với rìa void hoặc một [[Fair Value Gap]] / [[Order Block]] bên trong void.
- Xác nhận **displacement vi mô** + MSS trên M1/M5 trước khi vào.
- Đặt SL ngoài cấu trúc tạo void; TP ở **phía xa của void** (target) hoặc tại cụm thanh khoản kế tiếp.

```text
[KỊCH BẢN LONG — Void làm TARGET]
HTF: D1 discount, bias UP, có SSL phía dưới đã/sắp bị quét.
- Sweep SSL tại [level] (quét đáy cũ)
- Displacement UP mạnh -> mở ra Liquidity Void phía trên: [void_low] -> [void_high]
- Phía xa của void trỏ tới BSL tại [target_level]
- Vào: M5 FVG bên trong/ở chân void quanh [entry]
- SL: dưới low displacement / dưới swing [sl]
- TP1: rìa xa void [void_high]; TP2: BSL [target_level]
- RR dự kiến: ____
```

```text
[KỊCH BẢN SHORT — Void làm MAGNET / Rebalance]
HTF: H4 premium, bias DOWN, có void cũ CHƯA lấp phía trên: [void_low] -> [void_high].
- Giá pullback UP để "rebalance" void cũ (đi vào lấp inefficiency)
- Vào tại CE (mean threshold) của void [ce_level] khi M1 cho MSS xuống
- Xác nhận: displacement DOWN vi mô rời khỏi void
- SL: trên rìa trên void / trên swing [sl]
- TP: SSL phía dưới [target_level]
- RR dự kiến: ____
```

> [!warning] Bẫy đa khung
> Đừng nhầm **"giá đang lấp void cũ" (lành mạnh, theo bias)** với **"giá đang tạo void mới ngược chiều" (đảo bias)**. Nếu pullback rebalance lại đi kèm displacement mạnh xuyên qua cấu trúc → đó không còn là rebalance, mà là [[21 - Market Structure Shift]] báo đổi hướng. Luôn kiểm tra void mới có hình thành ngược chiều không.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup hợp lệ khi
- [ ] Void được tạo bởi **displacement rõ ràng** sau một **[[20 - Liquidity Sweep]]**.
- [ ] Void **cùng hướng [[12 - Daily Bias]]** và nằm đúng **premium/discount**.
- [ ] Có **draw on liquidity** rõ ở phía xa của void (target tồn tại).
- [ ] LTF cho **MSS + displacement vi mô** xác nhận trước khi vào.
- [ ] Void **chưa lấp** hoặc mới lấp một phần (còn "nhiên liệu").

### Setup bị vô hiệu khi
- [ ] Giá **đóng cửa qua hẳn rìa SL** của cấu trúc tạo void.
- [ ] Một **void mới ngược chiều** hình thành kèm MSS → bias đã đổi.
- [ ] Void **đã lấp 100%** trước khi ta kịp vào → mất draw.
- [ ] Pullback "rebalance" biến thành **breakout** xuyên qua void mà không phản ứng.
- [ ] Không còn cụm thanh khoản ở phía xa (target biến mất).

### Bảng so sánh: Void còn hiệu lực vs Void đã hết hiệu lực

| Tiêu chí | Còn hiệu lực (tradeable) | Hết hiệu lực (bỏ qua) |
|---|---|---|
| Mức độ lấp | Chưa lấp / lấp một phần | Đã lấp đầy ~100% |
| Bias | Cùng [[12 - Daily Bias]] | Ngược bias hiện tại |
| Vị trí PD | Đúng premium/discount | Sai phía |
| Draw phía xa | Có cụm thanh khoản | Không còn target |
| Phản ứng giá | Tôn trọng rìa/CE | Xuyên thẳng không phản ứng |

> [!note]
> CE — [[10 - Consequent Encroachment (Mean Threshold)]] — là đường giữa của void/FVG. Trong rất nhiều trường hợp giá **chỉ lấp tới CE rồi quay đầu** (partial fill). Hãy dùng CE làm mốc kỳ vọng cho retracement thay vì đòi giá phải lấp 100%.

---

## 6. Ví dụ chart

![[LiquidityVoid-Example-Correct.png]]

**Mô tả:** Trên chart [SYMBOL] khung [TF], giá quét [[30 - Sell-side Liquidity]] tại đáy cũ [level], sau đó bùng nổ displacement đi lên tạo một **Liquidity Void** rộng từ [void_low] đến [void_high], bên trong chứa [N] FVG liên tiếp. Phía xa của void trỏ thẳng tới buy-side liquidity tại [target_level]. Sau khi mở void, giá pullback nhẹ về một FVG ở chân void quanh [entry], rồi tiếp tục **lao qua void** lên chạm target.

**Vì sao đây là ví dụ tốt:**
- Có đủ chuỗi: **sweep → displacement → void → target** (draw on liquidity).
- Void nằm trong **discount** của [[12 - Dealing Range]] và cùng [[12 - Daily Bias]] UP.
- Điểm vào đến từ một FVG cụ thể *bên trong* void — void làm target, FVG làm POI.
- Giá tôn trọng CE của FVG khi pullback (partial fill rồi đi tiếp).

![[LiquidityVoid-Example-Wrong.png]]

**Mô tả:** Trên chart [SYMBOL] khung [TF], một void hình thành sau cú nhảy do tin tức, nhưng **ngược với bias HTF DOWN** và nằm sâu trong **premium**. Trader vào Long kỳ vọng giá lấp tiếp void lên trên, nhưng giá chỉ chạm CE rồi đảo chiều, tạo **void mới ngược hướng** (displacement DOWN) — báo hiệu đây thực ra là pullback rebalance trong xu hướng giảm, không phải void-target để Long.

**Bài học:**
- Void **ngược bias + sai premium/discount** là cái bẫy phổ biến nhất.
- Void do **tin tức** không khớp HTF thường chỉ là rebalance tạm thời, không phải draw.
- Khi **void mới ngược chiều** xuất hiện kèm MSS → đó là tín hiệu thoát/đảo, không phải tín hiệu vào tiếp.
- Đừng đòi void phải lấp 100% — partial fill tới CE là rất bình thường.

![[LiquidityVoid-Anatomy.png]]

**Mô tả (giải phẫu):** Sơ đồ đánh dấu các thành phần của một Liquidity Void chuẩn: (1) điểm sweep tạo "nhiên liệu", (2) dải displacement thiếu overlap, (3) các FVG con bên trong, (4) đường CE giữa void, (5) cụm thanh khoản ở phía xa làm target. Dùng sơ đồ này như khuôn mẫu để đối chiếu mỗi khi đánh dấu void mới trên chart thật.

---

## 7. Entry model liên quan

Liquidity Void hiếm khi là điểm vào trực tiếp — nó định *hướng* và *target*, còn điểm vào đến từ các array nhỏ hơn:

- [[Fair Value Gap]] — POI chính bên trong/ở rìa void.
- [[Order Block]] — block tạo ra cú displacement mở void.
- [[Optimal Trade Entry]] — vùng fib 62–79% trùng với rìa/CE của void.
- [[10 - Consequent Encroachment (Mean Threshold)]] — mốc partial fill, thường là điểm phản ứng.
- [[21 - Market Structure Shift]] / [[Break of Structure]] — xác nhận LTF trước khi vào.
- [[20 - Liquidity Sweep]] — sự kiện tạo "nhiên liệu" cho void.
- [[ICT 2022 Model]] — khung tích hợp sweep → MSS → FVG → target (void là target).

```text
[SEQUENCE — Void trong ICT 2022 Model]
1) HTF: xác định Daily Bias + đánh dấu void (target) trong premium/discount
2) Liquidity Sweep (quét SSL/BSL)         <- nhiên liệu
3) Displacement                            <- mở/định nghĩa void
4) MSS trên LTF                            <- xác nhận hướng
5) Pullback vào FVG/OB (POI bên trong void)<- ĐIỂM VÀO
6) Giá lao qua void -> chạm cụm thanh khoản <- TARGET (TP)
   (TP1 = rìa xa void; TP2 = BSL/SSL kế tiếp)
```

> [!note]
> Trong [[ICT 2022 Model]], **void chính là cái lý giải vì sao TP đặt được xa**: giá đi qua void rất nhanh, nên RR cao là hợp lý khi entry nằm ở chân void còn target nằm ở phía xa.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không có void hợp lệ + không có draw → KHÔNG có lệnh. Void không tự nó là tín hiệu.

### A. Context (bối cảnh)
- [ ] Đã xác định [[12 - Daily Bias]] và [[12 - Dealing Range]] (premium/discount).
- [ ] Void **cùng hướng bias** và nằm đúng phía PD.
- [ ] Có **[[20 - Liquidity Sweep]]** tạo nhiên liệu cho void.
- [ ] Có **draw on liquidity** rõ ở phía xa của void (target tồn tại).
- [ ] Void **chưa lấp / mới lấp một phần**.

### B. Execution (thực thi)
- [ ] LTF cho **MSS + displacement vi mô** xác nhận hướng.
- [ ] Điểm vào đến từ **FVG/OB/OTE** cụ thể bên trong/ở rìa void.
- [ ] SL đặt **ngoài cấu trúc tạo void** (logic, không phải cảm tính).
- [ ] TP đặt ở **rìa xa void** và/hoặc cụm thanh khoản kế tiếp.
- [ ] RR dự kiến hợp lý (ghi lại con số ____).

### C. "Không có lệnh" khi
- [ ] Void đã **lấp 100%** hoặc không còn target.
- [ ] Void **ngược bias** hoặc sai premium/discount.
- [ ] Đang trong **consolidation** / void do tin tức lệch bias.
- [ ] Xuất hiện **void mới ngược chiều** kèm MSS.
- [ ] Không có sweep / không có displacement rõ ràng.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Nhầm void với FVG đơn lẻ | Coi cả vùng rộng như một điểm vào | Vào sai vị trí, SL phi logic | Tách rõ: void = target/đoạn đường, FVG = POI |
| Trade void ngược bias | Long vào void trong premium khi bias DOWN | Đi ngược dòng tiền lớn, dễ cháy SL | Luôn lọc qua [[12 - Daily Bias]] + premium/discount |
| Đòi void lấp 100% | Giữ lệnh chờ fill toàn bộ | Bỏ lỡ partial fill / quay đầu tại CE | Dùng [[10 - Consequent Encroachment (Mean Threshold)]] làm mốc kỳ vọng |
| Bỏ qua void đã lấp | Vào vùng đã hết "nhiên liệu" | Không còn draw, giá không chạy | Kiểm tra mức độ lấp trước khi xem là target |
| Coi void do tin tức là draw | Vào sau spike news ngược bias | Whipsaw, SL bị quét hai chiều | Loại void không khớp HTF / tránh quanh tin |
| Bỏ qua void mới ngược chiều | Vẫn vào theo hướng cũ | Bias đã đổi, vào đúng đỉnh/đáy | Khi có MSS + void ngược → dừng, đánh giá lại |
| Không có target ở phía xa | Vào theo void nhưng không có cụm thanh khoản | TP mơ hồ, exit cảm tính | Chỉ trade void có [[07 - Buy-side Liquidity]]/[[30 - Sell-side Liquidity]] làm mồi |
| Đặt SL trong lòng void | SL nằm giữa vùng thiếu thanh khoản | Giá đi qua void nhanh, dễ quét SL | Đặt SL ngoài cấu trúc tạo void |

---

## 10. Câu hỏi tự kiểm tra
- Void này đang đóng vai trò **target** hay **magnet rebalance**? Vì sao?
- Void **đã lấp bao nhiêu phần** rồi? Còn "nhiên liệu" không?
- Void nằm trong **premium hay discount**? Có khớp [[12 - Daily Bias]] không?
- **Cụm thanh khoản nào** ở phía xa làm target của void?
- Có **[[20 - Liquidity Sweep]]** nào tạo ra void này không?
- Điểm vào của tôi đến từ **FVG/OB nào** bên trong/cạnh void?
- Nếu giá tạo **void mới ngược chiều**, tôi sẽ làm gì?
- TP của tôi có đặt ở **phía xa của void** không, hay chỉ là số tròn cảm tính?

---

## 11. Flashcards / Active Recall

**Q1.** Liquidity Void khác Fair Value Gap ở điểm cốt lõi nào?
> Hỏi: Khác biệt chính?
> Đáp: Void là một **vùng rộng** (thường chứa nhiều FVG) đóng vai trò **target/magnet**; FVG là **một khoảng trống 3 nến cụ thể** đóng vai trò **POI/điểm vào**. FVG là viên gạch, void là bức tường.

**Q2.** Điều kiện bắt buộc để có một Liquidity Void là gì?
> Hỏi: Không có gì thì không có void?
> Đáp: Không có **[[Displacement]]** (chuỗi nến body dài, thiếu overlap) thì không có void.

**Q3.** Khi nào void là TARGET, khi nào là MAGNET?
> Hỏi: Hai vai trò?
> Đáp: **TARGET** = void mới mở ra phía trước sau sweep, giá lao tới phía xa (đi *theo* void). **MAGNET** = void cũ phía sau chưa lấp, giá quay về *rebalance* (giao dịch retracement).

**Q4.** Partial fill nghĩa là gì và mốc nào hay được dùng?
> Hỏi: Lấp một phần?
> Đáp: Giá chỉ đi vào **một phần** void rồi quay đầu — thường tới **CE ([[10 - Consequent Encroachment (Mean Threshold)]])**, đường giữa void/FVG. Không nên đòi lấp 100%.

**Q5.** Dấu hiệu nào cảnh báo void không còn đáng tin để vào?
> Hỏi: Khi nào bỏ qua?
> Đáp: Khi void **đã lấp 100%**, **ngược bias / sai premium-discount**, hoặc xuất hiện **void mới ngược chiều kèm MSS** (báo đổi bias).

**Q6.** Trong [[ICT 2022 Model]], void giúp ích gì cho việc đặt TP?
> Hỏi: Liên hệ với TP?
> Đáp: Vì giá đi qua void **rất nhanh**, void giải thích vì sao TP đặt được xa (RR cao) — entry ở chân void, TP ở phía xa void / cụm thanh khoản kế tiếp.

---

## 12. Lesson Learned

**Bài học chính:**
- Liquidity Void không phải điểm vào — nó là **đoạn đường + mục tiêu**. Hãy ghép nó với một POI cụ thể (FVG/OB/OTE) để có entry.
- Vai trò của void (target vs rebalance) **do bias + premium/discount quyết định**, không phải do bản thân void.
- **Partial fill tới CE là bình thường** — đừng giữ lệnh chờ lấp toàn bộ.

**Quy tắc cá nhân:**
- Chỉ trade void khi có đủ **sweep + displacement + draw phía xa + đúng PD**.
- Luôn ghi rõ trong nhật ký: void đang là *target* hay *magnet*, và đã lấp bao nhiêu %.
- Khi thấy **void mới ngược chiều + MSS** → dừng giao dịch theo hướng cũ ngay.

> [!quote]
> "Giá không sợ khoảng trống — nó *bị hút* về phía khoảng trống. Việc của tôi là biết khoảng trống đó nằm trước mặt (chạy tới) hay sau lưng (quay về)."

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm (1-5) | Ghi chú |
|---|---|---|
| Nhận diện void trên chart | ____ | |
| Phân biệt void / FVG / imbalance | ____ | |
| Xác định target vs magnet | ____ | |
| Lọc bằng premium/discount + bias | ____ | |
| Ghép void với POI để vào lệnh | ____ | |
| Quản lý TP theo phía xa void | ____ | |
| **Tổng** | **____ / 30** | |

**Kế hoạch review tiếp theo:**
- [ ] Mark thủ công 10 void trên dữ liệu lịch sử, phân loại target/magnet.
- [ ] Đối chiếu mỗi void với [[12 - Daily Bias]] và premium/discount tại thời điểm đó.
- [ ] Backtest 10 setup "void làm target" trong [[18 - Kill Zones]] (ghi RR thực tế).
- [ ] Backtest 10 setup "rebalance void" và đo tỷ lệ partial fill tới CE.
- [ ] Cập nhật `confidence` và `status` sau khi hoàn tất backtest.

---

## Appendix — Liquidity Void Quick Reference Card

> [!abstract] Pre-market — điền nhanh trước phiên
> **Ngày:** ____    **Symbol:** ____    **Phiên/Kill Zone:** ____
>
> **HTF Bias (D1/H4):** ☐ Long ☐ Short → ____
> **Dealing Range / PD:** đỉnh [____] · đáy [____] · đang ở ☐ Premium ☐ Discount
>
> **Void chính (target):** [void_low] → [void_high] · hướng ____ · đã lấp ~__%
> **Void rebalance (magnet) cũ:** [____] → [____] · chưa lấp ☐
> **Sweep tạo void:** ☐ SSL ☐ BSL tại [____]
> **Draw phía xa (target thanh khoản):** [target_level] (☐ BSL ☐ SSL)
>
> **POI vào lệnh (bên trong/rìa void):** ☐ FVG ☐ OB ☐ OTE tại [entry]
> **CE (mean threshold):** [ce_level]
> **SL (ngoài cấu trúc):** [sl]    **TP1 (rìa xa void):** [____]    **TP2 (thanh khoản):** [____]
> **RR dự kiến:** ____
>
> **Vô hiệu nếu:** void lấp 100% · void mới ngược chiều + MSS · giá xuyên qua không phản ứng
> **Vai trò void hôm nay:** ☐ TARGET (đi theo) ☐ MAGNET (quay về rebalance)
