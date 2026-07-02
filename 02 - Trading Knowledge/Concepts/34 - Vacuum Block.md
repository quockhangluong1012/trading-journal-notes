---
type: ict-concept
concept: Vacuum Block
aliases:
  - Vacuum Block
  - VB
  - Gap Vacuum
tags:
  - trading/ict/concept
  - trading/study
  - "#VacuumBlock"
status: seed
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
models:
  - "[[ICT 2022 Model]]"
importance: 3
confidence: 1
last_reviewed:
created: 2026-06-24
updated: 2026-06-24
related_concepts:
  - "[[21 - Liquidity Void]]"
  - "[[24 - New Week Opening Gap]]"
  - "[[Fair Value Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[Displacement]]"
prerequisites:
  - "[[Fair Value Gap]]"
  - "[[21 - Liquidity Void]]"
  - "[[Displacement]]"
common_mistakes: []
---

# Vacuum Block

> [!summary] Tóm tắt 1 câu
> **Vacuum Block (VB)** là vùng giá rỗng (gap/void) sinh ra khi giá nhảy qua một khoảng từ một sự **đứt gãy giao dịch** — gap giữa phiên đóng và phiên mở kế tiếp, gap cuối tuần, hoặc cú nhảy quanh tin tức — nơi giá di chuyển mà gần như **không có khối lượng trao đổi** ở giữa, tạo ra một "chân không" mà giá có xu hướng bị hút quay lại để **rebalance**.

> [!important] Nguyên tắc cốt lõi
> Một **gap = inefficiency chưa được lấp = nam châm hút giá (price magnet)**.
> Khi có một Vacuum Block: (1) đánh dấu **toàn bộ range của gap** (cận trên và cận dưới), (2) tính **CE 50% (Consequent Encroachment)** của gap đó. Giá sẽ có xu hướng được kéo về **draw on liquidity** vào range này — tối thiểu chạm CE, lý tưởng lấp đầy hoàn toàn. VB vừa là **mục tiêu (target)** khi giá ở xa, vừa là **POI (point of interest)** để tìm phản ứng khi giá quay về.

---

## 1. Định nghĩa

### Khái niệm
**Vacuum Block** là một dạng inefficiency được tạo ra bởi sự **discontinuity (đứt gãy)** trong dòng giá: giá ở phiên/cây nến trước kết thúc tại một mức, rồi mở cửa hoặc nhảy đột ngột tới một mức khác mà **không giao dịch qua khoảng ở giữa**. Khoảng "trống" đó chính là vacuum. Vì không có ai mua/bán trong vùng đó, thị trường để lại một "lỗ hổng" về định giá mà nó thường muốn quay lại để cân bằng (rebalance / fill the gap).

Các nguồn tạo VB phổ biến:
- **Session gap**: chênh lệch giữa giá đóng phiên hôm trước và giá mở phiên hôm sau (đặc biệt rõ trên index như NQ1/NAS100, futures có giờ nghỉ).
- **Weekend gap**: gap giữa giá đóng cửa thứ Sáu và giá mở cửa Chủ Nhật/thứ Hai — liên quan trực tiếp tới [[24 - New Week Opening Gap]].
- **News gap / runaway candle**: cú displacement mạnh quanh tin tức (NFP, CPI, FOMC) khiến giá nhảy qua một dải mà thanh khoản gần như cạn — để lại "vacuum" trên cây nến tin.

### Bản chất (vacuum / void)
Bản chất của VB là một **vùng định giá bị bỏ qua**. Giống như một chân không vật lý hút vật chất vào, vùng giá rỗng này "hút" giá quay lại. ICT mô tả đây là một dạng **Liquidity Void** đặc thù — nhưng điểm khác biệt là VB sinh ra từ **không có giao dịch (gap thật)**, chứ không phải từ chuỗi nến chạy nhanh trong giao dịch liên tục.

### Cách vẽ gap + CE
1. Xác định **mép trên** của gap = mức thấp nhất của vùng giao dịch phía trên (ví dụ open của phiên mới khi gap down, hoặc đáy cây nến trên khi gap up).
2. Xác định **mép dưới** của gap = mức cao nhất của vùng giao dịch phía dưới (ví dụ close phiên trước, hoặc đỉnh cây nến dưới).
3. Vùng giữa hai mép = **Vacuum Block range** `[mép trên] – [mép dưới]`.
4. **CE 50%** = `(mép trên + mép dưới) / 2`. Đây là **mean threshold** — ngưỡng phản ứng quan trọng nhất, thường là nơi giá tối thiểu chạm tới trước khi tiếp diễn (xem [[10 - Consequent Encroachment (Mean Threshold)]]).

### So sánh Vacuum Block vs FVG vs Liquidity Void vs NWOG

| Tiêu chí | Vacuum Block (VB) | Fair Value Gap (FVG) | Liquidity Void | New Week Opening Gap (NWOG) |
|---|---|---|---|---|
| Nguồn gốc | Gap / đứt gãy giao dịch (no trade) | 3 nến liên tiếp trong giao dịch liên tục | Dải nến chạy nhanh, mỏng thanh khoản | Gap cụ thể giữa close thứ Sáu & open Chủ Nhật/thứ Hai |
| Có giao dịch ở giữa? | **Không** (chân không thật) | Có, nhưng lệch (imbalance) | Rất ít | **Không** (gap cuối tuần) |
| Cách đo | Mép gap + CE | Khoảng giữa nến 1 & nến 3 + CE | Toàn dải void + CE | Close Fri ↔ Open Sun + CE |
| Khung dùng | D1/H4/H1/M15/M5 | Mọi khung | Mọi khung | Chủ yếu D1 / theo tuần |
| Vai trò | Magnet + POI + DOL | POI entry phổ biến nhất | Target rebalance | Mốc tham chiếu tuần + magnet |
| Đặc thù | Liên quan phiên/tin/cuối tuần | Bất kỳ displacement nào | Hệ quả của displacement | Là một loại VB cuối tuần |

> [!note] Quan hệ phân cấp
> **NWOG là một trường hợp đặc biệt của Vacuum Block** (gap cuối tuần). Và **Vacuum Block là một dạng Liquidity Void** sinh từ gap. FVG thì khác họ — nó là inefficiency intrabar trong giao dịch liên tục.

### Mục đích trong ICT
- Cung cấp một **draw on liquidity (DOL)** rõ ràng: nếu phía trên/dưới có một VB chưa lấp, đó là một đích hợp lý cho giá.
- Cung cấp một **POI để tìm phản ứng**: khi giá quay về CE của VB, đó là vùng canh entry theo bias.
- Hỗ trợ xác định **premium/discount** trong [[12 - Dealing Range]] (xem [[27 - Premium Discount]]).

### Vì sao quan trọng
Vì gap là một bất thường rất "sạch" và dễ thấy. Thị trường ghét sự kém hiệu quả — một vùng định giá chưa ai giao dịch sẽ là một nam châm logic. Trader biết đọc VB có một **target/POI khách quan** thay vì đoán mò.

### Nó giúp trả lời câu hỏi gì?
- "Giá đang bị **hút về đâu** (draw on liquidity)?"
- "Khi giá tới đó, **mức nào** để canh phản ứng (CE)?"
- "Inefficiency này đã được **rebalance** chưa, hay vẫn còn năng lượng kéo giá?"

### Vacuum Block không phải là gì
- **Không phải** mọi cây nến lớn — phải có **gap thật / không giao dịch ở giữa** mới gọi là vacuum đúng nghĩa (nếu là dải chạy liên tục thì đó là Liquidity Void / FVG).
- **Không phải** lệnh đảo chiều tự động — VB là **magnet/POI**, không bảo đảm phản ứng. Cần xác nhận (xem mục 5).
- **Không phải** chỉ dùng để fill rồi đảo — giá có thể chỉ chạm CE (partial) rồi đi tiếp theo bias.
- **Không phải** thay thế bias — VB chỉ trả lời "về đâu", còn "đi hướng nào" vẫn do [[12 - Daily Bias]] quyết định.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái

| Loại VB | Mô tả | Hệ quả thường thấy |
|---|---|---|
| **Gap up** | Phiên/tuần mới mở **cao hơn** close trước | VB nằm **dưới** giá → magnet kéo xuống / hỗ trợ discount |
| **Gap down** | Phiên/tuần mới mở **thấp hơn** close trước | VB nằm **trên** giá → magnet kéo lên / kháng cự premium |
| **Session-gap VB** | Gap giữa close phiên & open phiên kế (index/futures) | Thường được rebalance trong vài giờ đầu phiên mới |
| **News-gap VB** | Cú nhảy quanh tin (NFP/CPI/FOMC) | Có thể giữ lâu nếu là displacement thật; cẩn trọng độ biến động |
| **Weekend-gap VB (NWOG)** | Gap close Fri ↔ open Sun/Mon | Mốc tham chiếu tuần; xem [[24 - New Week Opening Gap]] |
| **Filled VB** | Giá đã chạm hết range gap | Inefficiency hết hiệu lực → ưu tiên thấp |
| **Unfilled VB** | Gap còn nguyên hoặc chỉ partial | Vẫn là magnet active → ưu tiên cao |

### Khi nào giá trị cao?
- [ ] VB **chưa được lấp** (unfilled) hoặc mới partial tới CE.
- [ ] VB trùng hướng với [[12 - Daily Bias]] (VB nằm đúng phía của draw on liquidity).
- [ ] VB nằm ở vùng premium/discount hợp lý của [[12 - Dealing Range]].
- [ ] VB hình thành kèm **displacement** rõ ([[Displacement]]) hoặc sau một [[20 - Liquidity Sweep]].
- [ ] VB trùng với một PD Array khác (Order Block, FVG, đỉnh/đáy thanh khoản cũ) → confluence.
- [ ] Đang trong [[18 - Kill Zones]] phù hợp khi giá tiếp cận VB.

### Khi nào bỏ qua?
- [ ] VB đã **filled hoàn toàn** từ lâu (hết năng lượng magnet).
- [ ] Gap quá nhỏ / nhiễu, không tách bạch khỏi cấu trúc xung quanh.
- [ ] VB **ngược bias** mạnh và không có confluence — dễ là bẫy phản ứng yếu.
- [ ] News-gap trong môi trường biến động cực mạnh, spread giãn, chưa rõ hướng AMD ([[02 - AMD]]).
- [ ] Có nhiều VB chồng chéo gây nhiễu — ưu tiên VB gần nhất theo hướng DOL.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Khoảng trống thật giữa hai vùng giao dịch**: close của vùng trước và open của vùng sau không liền nhau → nến/phiên không "chạm" nhau.
2. **Gap rõ trên khung lớn**: dễ thấy nhất khi mở D1/H4 — một bậc thang giá thay vì dòng liên tục.
3. **Không có wick lấp đầy ngay**: nếu cây nến mở gap đã kéo wick lấp hết thì đó không còn là VB unfilled.
4. **Đi kèm displacement / xúc tác**: gap quanh tin hoặc đầu phiên là dấu hiệu mạnh.
5. **Vùng có CE đo được**: xác định được mép trên/dưới và 50%.

### Ma trận nhận diện

| Yếu tố | VB chất lượng cao | VB chất lượng thấp / nghi ngờ |
|---|---|---|
| Đứt gãy giao dịch | Gap rõ, có khoảng trống thật | Không gap thật (chỉ nến chạy nhanh) |
| Kích thước | Đủ lớn, tách khỏi nhiễu | Quá nhỏ, lẫn trong range |
| Trạng thái fill | Unfilled / partial tới CE | Đã filled hoàn toàn |
| Confluence | Trùng OB/FVG/liquidity/PD level | Đơn độc, không có gì đỡ |
| Đồng pha bias | Cùng hướng [[12 - Daily Bias]] | Ngược bias, không lý do |
| Xúc tác | Sinh từ news/session/sweep | Không rõ nguyên nhân |

### Điều kiện bắt buộc
- Có **gap thật** (đứt gãy) — không phải dải nến liên tục.
- Đo được **range gap + CE** một cách khách quan.
- VB còn **unfilled hoặc partial**.

### Điều kiện tăng xác suất
- Trùng hướng [[12 - Daily Bias]] và là **draw on liquidity** hợp lý.
- Có **confluence** với PD Array khác.
- Sinh sau **liquidity sweep** rồi **displacement** ([[21 - Market Structure Shift]] xác nhận).
- Giá tiếp cận trong [[18 - Kill Zones]].

### Điều kiện làm yếu đi
- VB đã chạm hết range nhiều lần.
- Gap quá nhỏ hoặc nằm giữa vùng đi ngang nhiễu.
- Ngược bias mà không có lý do AMD rõ.
- Môi trường tin tức quá hỗn loạn, chưa rõ hướng.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Xác định VB lớn & bias
- Mở D1/H4 để tìm các **session/weekend/news gap** chưa lấp.
- Đánh dấu range + CE của từng VB. Ghi chú VB nào nằm phía DOL theo [[12 - Daily Bias]].
- Xác định VB nào là **target** (giá đang chạy về) và VB nào là **POI** (giá có thể phản ứng).

```text
[D1/H4 VB Map] ___-___-___
- Bias hôm nay: ____ (Long/Short) — lý do: ____
- VB phía trên: range [__]–[__] | CE [__] | trạng thái: unfilled/partial/filled
- VB phía dưới: range [__]–[__] | CE [__] | trạng thái: ____
- DOL chính: VB ____ (vì trùng bias + confluence ____)
```

### H1 / M15 — Lập kế hoạch tiếp cận
- Theo dõi giá tiến về VB đã chọn.
- Quan sát phản ứng quanh **mép VB** và **CE**: có dấu hiệu chậm lại, sweep, hay xuyên thẳng?
- Định vùng entry: thường canh phản ứng tại CE hoặc mép xa của VB.

### M5 / M1 — Xác nhận & timing entry
- Chờ **liquidity sweep + displacement / MSS** ngay tại VB ([[21 - Market Structure Shift]], [[Displacement]]).
- Xác nhận FVG nội bộ trên M1/M5 để tinh chỉnh entry (xem [[ICT 2022 Model]]).

```text
[M5/M1 Entry @ VB] ___:___
- Giá chạm: mép/CE VB [__]
- Sweep thanh khoản: có/không — quét mức [__]
- Displacement + MSS: có/không
- Entry FVG nội bộ: [__] | SL: [__] | TP: VB đối diện / DOL kế [__]
```

> [!warning] Cảnh báo timing
> VB là **magnet**, không phải tín hiệu đảo chiều tự động. Đừng vào lệnh chỉ vì "giá đang về gap". Phải có **xác nhận giá** (sweep + displacement/MSS) tại VB. Riêng news-gap: chờ biến động lắng và spread bình thường mới hành động.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Checklist xác nhận VB còn hiệu lực (active magnet)
- [ ] VB **unfilled** hoặc chỉ mới partial (chưa chạm CE hoặc chưa lấp hết).
- [ ] VB nằm đúng phía draw on liquidity theo bias.
- [ ] Có confluence (OB/FVG/liquidity/PD level).
- [ ] Khi giá tới: có phản ứng (sweep + displacement/MSS) tại mép hoặc CE.

### Checklist vô hiệu hóa (bỏ VB này đi)
- [ ] VB đã **filled hoàn toàn** và giá đóng cửa ổn định phía bên kia.
- [ ] Giá **xuyên thẳng** qua VB không phản ứng (chỉ là điểm trung chuyển, không phải POI).
- [ ] Bối cảnh đổi: bias đảo, DOL mới xuất hiện gần hơn.

### Bảng so sánh: Partial vs Full Rebalance

| Tiêu chí | Partial rebalance | Full rebalance |
|---|---|---|
| Mức giá chạm | Tới CE (50%) rồi quay | Lấp hết range gap |
| Ý nghĩa | Inefficiency vẫn còn một phần năng lượng | Inefficiency đã trung hòa |
| Kỳ vọng tiếp theo | Tiếp diễn theo bias từ CE | Có thể coi VB như "đã xong", tìm DOL mới |
| Dùng làm | POI phản ứng tại CE | Mép xa làm SL reference |

> [!note] Quy ước thực dụng
> ICT nhấn mạnh **CE là ngưỡng tối thiểu**. Nhiều lần giá chỉ cần chạm CE của VB là đủ "rebalance" để tiếp diễn. Đừng cố chờ fill 100% mới hành động — sẽ bỏ lỡ partial rebalance setup.

---

## 6. Ví dụ chart

![[VacuumBlock-Anatomy.png]]

**Mô tả — Giải phẫu một Vacuum Block:**
- Mép trên gap = [level], mép dưới gap = [level].
- CE 50% = [level] — đường giữa cần đánh dấu đậm.
- Vùng tô màu = range VB; mũi tên chỉ hướng draw on liquidity.

![[VacuumBlock-Example-Correct.png]]

**Mô tả — Ví dụ ĐÚNG (VB hoạt động như magnet + POI):**
- Phiên mở gap [up/down] để lại VB range `[__]–[__]`, CE `[__]`.
- Giá chạy [hướng] rồi bị hút quay lại VB đúng theo bias.
- Tại CE: có [liquidity sweep] + [displacement/MSS] → tín hiệu phản ứng.
- Entry tại FVG nội bộ `[__]`, SL `[__]`, TP về DOL kế `[__]`.
- Kết quả: ____ (không bịa số liệu — điền sau).

![[VacuumBlock-Example-Wrong.png]]

**Mô tả — Ví dụ SAI (vào lệnh chỉ vì "thấy gap"):**
- VB đã **filled hoàn toàn** trước đó nhưng vẫn cố canh phản ứng → magnet hết hiệu lực.
- Giá xuyên thẳng qua CE không có sweep/displacement → không phải POI.
- Vào ngược bias chỉ vì "gap sẽ fill" → bị cuốn theo.
- Bài học: gap phải **còn active** và phải có **xác nhận giá** mới hành động.

---

## 7. Entry model liên quan

- [[ICT 2022 Model]] — VB làm **draw on liquidity** & POI; entry qua sweep + displacement + FVG.
- [[24 - New Week Opening Gap]] — VB cuối tuần làm mốc tham chiếu & magnet tuần.
- [[21 - Liquidity Void]] — họ hàng gần: void cần rebalance.
- [[Fair Value Gap]] — dùng FVG nội bộ để tinh chỉnh entry tại VB.
- [[Order Block]] — confluence khi VB trùng OB.
- [[20 - Liquidity Sweep]] / [[21 - Market Structure Shift]] — tín hiệu xác nhận tại VB.

```text
[VB Entry Sequence — theo ICT 2022]
1. HTF: xác định VB unfilled đúng phía DOL + bias.
2. Giá tiếp cận VB → vào quan sát LTF.
3. Liquidity sweep quanh mép/CE của VB.
4. Displacement + MSS xác nhận đảo hướng ngắn hạn.
5. Entry tại FVG nội bộ; SL ngoài mép xa VB.
6. TP: CE → mép đối diện → DOL kế tiếp.
```

> [!note] Lưu ý ghép model
> VB không phải một "entry model" độc lập — nó là **PD Array / target / POI**. Entry thực tế vẫn đi qua khung [[ICT 2022 Model]] (sweep → displacement → FVG).

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Bắt buộc soát đủ trước khi vào lệnh quanh một Vacuum Block.

**Nhóm A — Bối cảnh & bias**
- [ ] Đã xác định [[12 - Daily Bias]] hôm nay?
- [ ] VB nằm đúng phía draw on liquidity theo bias?
- [ ] VB ở vùng premium/discount hợp lý ([[27 - Premium Discount]], [[12 - Dealing Range]])?

**Nhóm B — Chất lượng VB**
- [ ] Có gap thật (đứt gãy giao dịch), không phải nến chạy liên tục?
- [ ] VB còn unfilled / partial?
- [ ] Đã đo range + CE rõ ràng?
- [ ] Có confluence với PD Array khác?

**Nhóm C — Xác nhận & rủi ro**
- [ ] Đã có sweep + displacement/MSS tại VB chưa?
- [ ] Có FVG nội bộ để tinh chỉnh entry?
- [ ] SL/TP rõ ràng, R hợp lý? Rủi ro ≤0.5% lệnh?
- [ ] Nếu là news-gap: biến động & spread đã ổn định?

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Vào lệnh chỉ vì "thấy gap" | Không chờ xác nhận, vào ngay khi giá về VB | VB là magnet, không phải tín hiệu đảo | Chờ sweep + displacement/MSS tại VB |
| Nhầm Liquidity Void/FVG thành VB | Gọi nến chạy nhanh là "vacuum" | Không có gap thật → logic magnet yếu hơn | Chỉ gọi VB khi có đứt gãy giao dịch thật |
| Bỏ qua CE, đòi fill 100% | Chờ giá lấp hết gap mới vào | Bỏ lỡ partial rebalance tại CE | Coi CE là ngưỡng tối thiểu để hành động |
| Dùng VB đã filled | Canh phản ứng tại gap cũ đã lấp | Hết năng lượng magnet → phản ứng yếu | Loại VB filled; chỉ dùng unfilled/partial |
| Ngược bias | Long/Short ngược DOL chỉ vì "gap sẽ fill" | Đi ngược dòng tiền chính | Luôn ưu tiên VB cùng hướng bias |
| Vào giữa cú news | Vào lệnh ngay trong cú nhảy tin | Spread giãn, slippage, hướng chưa rõ | Chờ biến động lắng, spread bình thường |
| Đánh dấu gap sai mép | Vẽ range lệch → CE sai | Sai POI/SL/TP toàn bộ | Xác định đúng close trước & open sau |

---

## 10. Câu hỏi tự kiểm tra
- VB khác FVG ở điểm cốt lõi nào? (gợi ý: có/không giao dịch ở giữa)
- Vì sao một gap unfilled lại hoạt động như nam châm?
- CE của VB là gì và vì sao nó quan trọng hơn việc fill 100%?
- Khi nào một VB nên bị bỏ qua?
- NWOG quan hệ thế nào với Vacuum Block?
- Trước khi vào lệnh quanh VB cần xác nhận gì?

---

## 11. Flashcards / Active Recall

> [!tip] Active recall — che đáp án và tự trả lời.

**Q1.** Vacuum Block là gì?
> Vùng giá rỗng sinh từ gap/đứt gãy giao dịch (session/weekend/news) — giá nhảy qua mà không giao dịch ở giữa, tạo "chân không" hút giá quay lại rebalance.

**Q2.** VB khác FVG thế nào?
> FVG = inefficiency intrabar (3 nến) trong giao dịch liên tục. VB = gap từ sự đứt gãy (không giao dịch ở giữa). VB là họ hàng của Liquidity Void; NWOG là một loại VB cuối tuần.

**Q3.** Cách đánh dấu một VB?
> Mép trên gap, mép dưới gap, và CE = trung điểm 50%. CE là ngưỡng phản ứng chính.

**Q4.** Vì sao VB là magnet?
> Inefficiency chưa lấp = vùng định giá bị bỏ qua; thị trường có xu hướng quay lại cân bằng nó (draw on liquidity).

**Q5.** Partial vs full rebalance?
> Partial = chạm tới CE rồi tiếp diễn theo bias. Full = lấp hết range gap (inefficiency trung hòa, tìm DOL mới).

**Q6.** Điều kiện vào lệnh quanh VB?
> VB unfilled/partial + đúng phía bias + confluence + có sweep & displacement/MSS xác nhận tại VB + FVG nội bộ để timing.

---

## 12. Lesson Learned

> [!example] Ghi chú quan sát cá nhân
> - (Điền sau khi backtest/live) VB loại nào trên NQ1/NAS100 hay được rebalance nhất? ____
> - Tỉ lệ partial (chạm CE) vs full fill quan sát được: ____
> - News-gap có đáng giao dịch không, hay nên đứng ngoài? ____
> - Sai lầm lặp lại của bản thân khi đọc VB: ____

---

## 13. Mức độ thành thạo

| Cấp độ | Tiêu chí | Đạt? |
|---|---|---|
| Seed | Hiểu định nghĩa, phân biệt VB/FVG/Void/NWOG | [ ] |
| Developing | Đánh dấu đúng range + CE trên chart thật | [ ] |
| Tested | Backtest ≥20 mẫu VB với thống kê partial/full | [ ] |
| Mastered | Dùng VB nhất quán làm DOL/POI trong [[ICT 2022 Model]] live | [ ] |

**Kế hoạch ôn tập:**
- Tuần 1–2: học định nghĩa, đánh dấu 10 VB lịch sử trên D1/H4 (NQ1, EURUSD, XAUUSD).
- Tuần 3–4: backtest 20 setup VB, ghi partial vs full, đo R.
- Hàng tuần: rà soát trong [[07 - Reviews]] xem có vào lệnh quanh VB sai checklist không.
- Cập nhật `confidence` & `status` khi đạt mốc.

---

## Appendix — Vacuum Block Quick Reference Card

> [!abstract] Thẻ tra nhanh — Vacuum Block (VB)
> **Là gì:** gap/void từ đứt gãy giao dịch (session/weekend/news) → nam châm hút giá rebalance.
> **Đánh dấu:** mép trên `[__]` – mép dưới `[__]` | **CE 50%** `[__]`.
> **Vai trò:** Draw on liquidity (target) + POI (phản ứng).
> **Loại:** gap up / gap down / session / news / weekend (NWOG) | trạng thái: unfilled / partial / filled.
> **Active khi:** unfilled/partial + đúng bias + confluence.
> **Vào lệnh:** chờ sweep + displacement/MSS tại mép/CE → FVG nội bộ → SL ngoài mép xa → TP CE/mép đối diện/DOL kế.
> **Tránh:** VB đã filled, vào chỉ vì "thấy gap", ngược bias, vào giữa cú news.
> **Khác FVG:** VB = không giao dịch ở giữa (gap); FVG = imbalance 3 nến liên tục.
> **Liên quan:** [[21 - Liquidity Void]] · [[24 - New Week Opening Gap]] · [[Fair Value Gap]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[Displacement]] · [[ICT 2022 Model]]
