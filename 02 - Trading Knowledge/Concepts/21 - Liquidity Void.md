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
status: developing
category: PD Array
last_reviewed: 2026-07-14
created: 2026-06-24
updated: 2026-07-03
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

### Nâng cao — Phân biệt Liquidity Void vs Fair Value Gap vs Balanced Price Range (BPR)

Ba khái niệm này đều thuộc "họ gap/imbalance" của ICT nhưng dễ bị dùng lẫn lộn vì cùng xoay quanh ý tưởng "khoảng trống giá chưa cân bằng". Điểm khác biệt cốt lõi nằm ở **quy mô cấu trúc** và **cơ chế hình thành**: FVG là đơn vị nhỏ nhất (3 nến), Liquidity Void là một "container" rộng hơn thường chứa nhiều FVG, còn BPR lại là sản phẩm của **hai FVG ngược chiều chồng lên nhau** — tức một dạng đã được "cân bằng" chứ không còn thuần một chiều như void hay FVG.

![[LiquidityVoid-Advanced-vs-FVG-vs-BPR.svg]]
*So sánh trực quan ba PD-array: FVG là một đơn vị 3 nến duy nhất, Liquidity Void là cả một dải displacement chứa nhiều FVG con, BPR là phần overlap giữa hai FVG ngược chiều.*

| Tiêu chí | **Liquidity Void** | **[[13 - FVG  - Fair Value Gap]]** | **[[03 - Balanced Price Range]] (BPR)** |
|---|---|---|---|
| Cơ chế định nghĩa | Chuỗi **nhiều nến displacement** cùng chiều, gần như không overlap thân nến | **3 nến** cụ thể: gap giữa nến 1 và nến 3, nến 2 là displacement | **2 FVG ngược chiều CHỒNG LẤP** nhau trên cùng dải giá |
| Số nến tối thiểu | Không cố định — thường ≥ 4-5 nến, có thể tới 8-10 nến | Đúng 3 nến | Tối thiểu 2 leg ngược chiều (mỗi leg tự đủ 3 nến để tạo FVG riêng) |
| Cái gì "lấp" (fills) nó | Giá quay lại và trượt qua một đoạn — thường chỉ tới **CE của cả dải**, không cần candle-by-candle | Giá retrace vào gap, tôn trọng CE (50%) rồi reject | Giá test lại vùng overlap; vì đã có order flow 2 chiều nên phản ứng thường sắc bén hơn |
| Điều gì vô hiệu hóa nó | Void đã **lấp gần hết** hoặc xuất hiện **void mới ngược chiều** (đổi bias) | Giá **đóng nến xuyên qua** toàn bộ FVG (mitigation → có thể đảo thành IFVG) | Giá **đóng nến xuyên qua toàn bộ vùng overlap** (order flow đã đổi mạnh) |
| Vai trò chính | **TARGET** (draw on liquidity) hoặc **MAGNET** (rebalance) — mô tả *đoạn đường* | **POI** để vào lệnh — mô tả *một điểm* | **POI cao cấp** — S/R mạnh hơn FVG đơn nhờ confluence kép |

**Khi nào một void và một FVG/BPR chồng lấp, khi nào chúng tách biệt:**
- **Chồng lấp (thường xuyên):** một Liquidity Void gần như luôn **chứa nhiều FVG con** bên trong nó — đây là quan hệ bao trùm bình thường (void = "bức tường", FVG = "viên gạch", xem mục 1). Khi trade một void làm target, điểm vào cụ thể vẫn lấy từ một FVG con bên trong hoặc ở rìa void.
- **Chồng lấp (đặc biệt):** nếu ngay **trong lòng một void** xuất hiện một cú đảo chiều ngắn tạo ra một FVG ngược hướng chồng lên FVG gốc, phần chồng đó chính là một **BPR nằm bên trong void**. Đây là dấu hiệu void đang bị "thử" bởi lực ngược trước khi quyết định tiếp tục hay đảo bias — quan sát kỹ khi thấy tình huống này.
- **Tách biệt (thường xuyên):** một Liquidity Void "sạch" — chưa có leg đảo chiều nào cắt vào nó — thì **không có BPR nào cả**, nó vẫn thuần túy là vùng một chiều. Ngược lại, một BPR có thể hình thành hoàn toàn **bên ngoài** mọi void (ví dụ ngay tại điểm V-reversal nhỏ giữa range) mà không cần một void rộng đi kèm.

> [!tip] Cách hỏi nhanh khi không chắc
> "Tôi đang nhìn **một điểm** (FVG), **một đoạn đường** (Liquidity Void), hay **một vùng đã được test hai chiều** (BPR)?" Ba câu trả lời dẫn tới ba cách dùng khác nhau: entry cụ thể, target/magnet, hoặc S/R phòng thủ.

Ghi log các trường `void_vs_fvg_overlap` (yes/no) và `void_contains_bpr` (yes/no) khi backtest để tránh nhầm lẫn ba khái niệm này trong nhật ký.

### Nâng cao — Macro Liquidity Void: khoảng trống xuyên nhiều nến liên tiếp

Một FVG chuẩn chỉ cần 3 nến. Nhưng trên thực tế, những cú displacement mạnh nhất (thường quanh news, mở phiên, hoặc breakout khỏi accumulation dài) không dừng lại ở 3 nến — chúng kéo dài thành **6, 8, thậm chí 10+ nến liên tiếp cùng chiều**, mỗi nến gần như không chồng lấp thân với nến trước. Đây là một **Macro Liquidity Void**: về bản chất vẫn là Liquidity Void, nhưng quy mô đủ lớn để cần một cách tiếp cận riêng khi xác định biên và kỳ vọng retest.

![[LiquidityVoid-Advanced-MacroVoid.svg]]
*Một macro void trải dài qua 7-8 nến displacement liên tiếp. Biên thật của void lấy từ nến đầu tiên và nến cuối cùng trong chuỗi, không phải một cặp nến 1-3 riêng lẻ nào ở giữa.*

**Cách xác định biên thật của một macro void:**
- **Biên xa (đầu chuỗi):** lấy từ **high của nến đầu tiên** trong chuỗi displacement (với void tăng) — đây là điểm giá "rời đi" trước khi bắt đầu one-sided delivery.
- **Biên gần (cuối chuỗi):** lấy từ **low của nến cuối cùng** trong chuỗi (nến mà ngay sau đó bắt đầu có nến đối lập/overlap trở lại) — đây là nơi displacement "hết hơi".
- **Không cộng dồn biên của từng FVG con.** Sai lầm phổ biến là vẽ riêng biên cho từng cặp nến rồi cố "nối" chúng lại; thay vào đó hãy nhìn cả chuỗi như MỘT khối duy nhất và chỉ lấy hai điểm cực trị ngoài cùng.

**Vì sao retest hành xử khác với một FVG đơn 3-nến:**

| Đặc điểm | FVG 3-nến đơn | Macro Liquidity Void |
|---|---|---|
| Cách lấp khi retest | Giá đi vào gap, thường chạm CE trong 1 nhịp ngắn | Giá thường lấp **một cục lớn** của cả dải trong 1-2 nến mạnh, không lấp tuần tự từng FVG con |
| Tốc độ di chuyển trong vùng | Tương đối chậm, có thể phản ứng ngay ở mép | Thường **trượt nhanh** xuyên qua nhiều FVG con liên tiếp trước khi chạm CE của toàn dải |
| Mức tham chiếu chính | CE của chính FVG đó | CE của **toàn bộ macro void** (không phải CE của từng FVG con riêng lẻ) |
| Rủi ro khi phân tích sai | Nhầm gap nhỏ giữa range thành FVG thật | Nhầm một đoạn nến giữa chuỗi là "điểm kết thúc" void, cắt ngắn void thật và đặt CE sai vị trí |

> [!warning]
> Đừng dừng việc đo void lại ở nến thứ 3-4 chỉ vì "FVG chuẩn có 3 nến". Nếu displacement vẫn tiếp diễn với các nến sau đó tiếp tục *không overlap* với nến trước, void còn đang mở rộng — hãy đợi tới khi thấy nến đầu tiên có overlap đáng kể (thân nến chồng lên thân nến liền trước) mới chốt biên gần của void.

Vì cơ chế lấp khác nhau, khi trade một macro void, ưu tiên coi **CE của toàn dải** — không phải CE của FVG con gần giá nhất — là mốc kỳ vọng partial fill chính; các FVG con bên trong chỉ dùng để tinh chỉnh entry cụ thể một khi giá đã tiến vào vùng lân cận CE đó.

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

![[LiquidityVoid-Example-Correct.svg]]

**Mô tả:** Trên chart [SYMBOL] khung [TF], giá quét [[30 - Sell-side Liquidity]] tại đáy cũ [level], sau đó bùng nổ displacement đi lên tạo một **Liquidity Void** rộng từ [void_low] đến [void_high], bên trong chứa [N] FVG liên tiếp. Phía xa của void trỏ thẳng tới buy-side liquidity tại [target_level]. Sau khi mở void, giá pullback nhẹ về một FVG ở chân void quanh [entry], rồi tiếp tục **lao qua void** lên chạm target.

**Vì sao đây là ví dụ tốt:**
- Có đủ chuỗi: **sweep → displacement → void → target** (draw on liquidity).
- Void nằm trong **discount** của [[12 - Dealing Range]] và cùng [[12 - Daily Bias]] UP.
- Điểm vào đến từ một FVG cụ thể *bên trong* void — void làm target, FVG làm POI.
- Giá tôn trọng CE của FVG khi pullback (partial fill rồi đi tiếp).

![[LiquidityVoid-Example-Wrong.svg]]

**Mô tả:** Trên chart [SYMBOL] khung [TF], một void hình thành sau cú nhảy do tin tức, nhưng **ngược với bias HTF DOWN** và nằm sâu trong **premium**. Trader vào Long kỳ vọng giá lấp tiếp void lên trên, nhưng giá chỉ chạm CE rồi đảo chiều, tạo **void mới ngược hướng** (displacement DOWN) — báo hiệu đây thực ra là pullback rebalance trong xu hướng giảm, không phải void-target để Long.

**Bài học:**
- Void **ngược bias + sai premium/discount** là cái bẫy phổ biến nhất.
- Void do **tin tức** không khớp HTF thường chỉ là rebalance tạm thời, không phải draw.
- Khi **void mới ngược chiều** xuất hiện kèm MSS → đó là tín hiệu thoát/đảo, không phải tín hiệu vào tiếp.
- Đừng đòi void phải lấp 100% — partial fill tới CE là rất bình thường.

![[LiquidityVoid-Anatomy.svg]]

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

## Best Practices

> [!success] Nguyên tắc vàng
> **Liquidity Void chỉ đáng tin khi bạn phân biệt được nó với FVG/BPR, đo được biên thật của nó (kể cả khi trải dài nhiều nến), và luôn ghép nó với một draw on liquidity + bias đúng phía — nếu không, "void" chỉ là một cái tên đẹp gắn cho một đoạn chart bất kỳ.**

1. **Luôn phân loại trước khi trade: đây là FVG (điểm), Liquidity Void (đoạn đường), hay BPR (vùng đã cân bằng)?** Nhầm ba khái niệm này là lỗi gốc phổ biến nhất — mỗi loại có cách fill và cách vô hiệu hóa khác nhau (xem bảng so sánh ở mục 3). Ghi `void_vs_fvg_overlap: yes/no` cho mỗi lần đánh dấu void để về sau kiểm tra bạn có đang lẫn lộn hai khái niệm không. Xem thêm [[13 - FVG  - Fair Value Gap]] và [[03 - Balanced Price Range]].

2. **Với void trải dài nhiều nến (macro void), lấy biên từ nến đầu và nến cuối của CẢ chuỗi, không chốt sớm ở nến thứ 3-4.** Nếu các nến sau vẫn tiếp tục không overlap với nến liền trước, void còn đang mở rộng. Ghi `void_span_candles` (số nến tạo void) vào journal — con số này giúp phân biệt một FVG-cỡ-lớn với một macro void thực sự.

3. **Không đòi hỏi full fill; dùng CE của toàn dải làm mốc kỳ vọng mặc định.** Dữ liệu thực chiến (và cách ICT/practitioner mô tả khái niệm này) đều cho thấy giá thường chỉ cần tới **Consequent Encroachment (50%)** là đủ để tiếp tục di chuyển theo hướng cũ. Giữ lệnh chờ lấp 100% dễ khiến bạn bỏ lỡ điểm reject thật hoặc hoảng loạn khi thấy giá "chưa lấp đủ". Ghi `void_fill_percent` khi review để tự xây ngưỡng kỳ vọng theo từng thị trường (NQ1/EURUSD/XAUUSD có thể khác nhau — **cần backtest xác nhận**).

4. **Chỉ coi void là draw đáng trade khi có cụm thanh khoản rõ ràng ở phía xa.** Một void không có buy-side/sell-side liquidity nào chờ sẵn ở đầu kia chỉ là một quan sát cấu trúc, không phải một target thực chiến. Luôn hỏi: "Giá đang bị hút VỀ ĐÂU, không chỉ 'đi qua đâu'?" Cross-link target với [[07 - Buy-side Liquidity]] / [[30 - Sell-side Liquidity]].

5. **Bắt buộc đối chiếu void với [[12 - Daily Bias]] và [[27 - Premium Discount]] trước khi gán vai trò TARGET hay MAGNET.** Cùng một void, sai bias/sai phía PD sẽ biến một "draw hợp lệ" thành một cái bẫy đảo chiều. Không có void nào tự thân nó quyết định hướng — narrative HTF quyết định.

6. **Cảnh giác với void mới hình thành ngược chiều bên trong một void cũ — đó thường là tín hiệu đổi bias, không phải nhiễu.** Nếu một pullback "rebalance" bất ngờ tạo ra một displacement mạnh ngược hướng với [[21 - Market Structure Shift]] đi kèm, dừng ngay giả định "đang lấp void cũ" và đánh giá lại toàn bộ setup.

7. **Đặt SL ngoài cấu trúc tạo void, không đặt SL nằm giữa lòng void.** Vì bản chất void là vùng mỏng thanh khoản, một SL đặt giữa void rất dễ bị quét khi giá "trượt" qua nhanh. SL logic phải nằm ngoài điểm bắt đầu/kết thúc thật của dải displacement.

8. **Log đầy đủ và review sau 20-30 mẫu trên NQ1/EURUSD/XAUUSD trước khi tin bất kỳ con số cụ thể nào.** Các trường nên có: `void_span_candles`, `void_vs_fvg_overlap`, `void_contains_bpr`, `void_fill_percent`, `role` (target/magnet), `bias_match` (yes/no). Không có dữ liệu thực chiến, mọi ngưỡng trong note này chỉ là khung tham khảo ban đầu — **cần backtest xác nhận** trước khi nâng `confidence`/`status` của khái niệm.
