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
updated: 2026-07-03
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

### Order-flow / market-maker rationale — vì sao gap chưa lấp lại hoạt động như nam châm

![[VacuumBlock-OrderFlow-Rationale.png]]

**Mô tả — Giải phẫu logic order-flow đằng sau một Vacuum Block (sơ đồ minh hoạ, KHÔNG phải chart thật):**
- Cột bên trái: sổ lệnh (order book) trước gap — thể hiện thanh khoản hai chiều dày đặc quanh vùng giá cũ.
- Vùng giữa (tô xám, có ký hiệu "∅"): dải giá **không có lệnh khớp** — đúng nghĩa "chân không" thanh khoản.
- Cột bên phải: sổ lệnh sau gap — thanh khoản tái tập trung quanh mức giá mới, để lại một "khoảng trống định giá" ở giữa.
- Mũi tên cong từ vùng giá hiện tại quay ngược về dải "∅" minh hoạ lực hút "repricing" khi thuật toán tổ chức tìm **fair value** trong dải trống.

Diễn giải theo **lý thuyết thị trường đấu giá (Auction Market Theory)**: mọi mức giá tồn tại là vì có đủ hai bên đồng ý giao dịch tại đó (value được "xác nhận" bằng khối lượng). Một gap là nơi thị trường **bỏ qua bước đấu giá** — giá "nhảy cóc" từ điểm cân bằng A sang điểm cân bằng B mà không dừng lại thương lượng ở giữa. Về mặt lý thuyết định giá công bằng (fair value), dải bị bỏ qua đó **chưa từng được thị trường "phê duyệt"** là mức giá hợp lý. Đó là lý do:
- **Market maker / thuật toán delivery giá (algorithmic price delivery)** có xu hướng dẫn giá quay lại các dải chưa được đấu giá để "hoàn tất" quá trình khám phá giá (price discovery) trước khi tiếp tục xu hướng — tương tự cách IPDA (Interbank Price Delivery Algorithm) được ICT mô tả là dẫn giá tới các mức inefficiency theo chu kỳ.
- Vì không có lệnh limit/dừng nào "mắc kẹt" bên trong dải gap (không ai từng giao dịch ở đó), tính thanh khoản trong vacuum gần như bằng 0 → khi giá quay lại, nó thường **di chuyển nhanh xuyên qua phần giữa** dải (ít lực cản) rồi mới chậm lại quanh CE hoặc mép xa nơi có order flow thật.
- Đây cũng là lý do CE (50%) quan trọng hơn việc lấp 100%: về mặt thống kê, "trung điểm định giá công bằng" là nơi xác suất hai bên đồng thuận cao nhất — thuật toán không cần lấp hết dải mới coi là "đủ tái cân bằng", chỉ cần chạm ngưỡng trung bình là đủ để tiếp diễn nhiệm vụ chính (dẫn giá tới draw on liquidity xa hơn).

> [!info] Không phải phép màu, là hệ quả cấu trúc
> "Giá bị hút về gap" không phải vì thị trường có ý thức — mà vì **thanh khoản residual** (lệnh chờ, stop, order tổ chức) luôn tập trung ở các mức có giao dịch trước đó, còn vùng gap thì trống rỗng. Đường ít lực cản nhất (path of least resistance) của giá luôn đi qua vùng trống trước khi gặp vùng có thanh khoản thật.

### Cross-market nuances — VB khác nhau thế nào trên từng thị trường bạn giao dịch

Vacuum Block không "đồng nhất" giữa các thị trường — nguồn gốc gap, chu kỳ lặp lại, và độ tin cậy của magnet khác nhau đáng kể giữa index futures, forex, và vàng. Bảng dưới đây là kim chỉ nam thực chiến cho 4 thị trường trong phạm vi giao dịch:

| Thị trường | Nguồn gap chính | Đặc thù cần lưu ý | Gợi ý thực chiến |
|---|---|---|---|
| **NQ1 / NDX (NAS100)** | Session gap quanh giờ mở cửa RTH (futures đóng cửa ngắn rồi mở lại), gap qua đêm (overnight gap) do CME có phiên electronic gần như 24h nhưng thanh khoản mỏng ngoài RTH | Gap quanh mở cửa NY thường **rebalance rất nhanh** (trong Kill Zone London/NY mở) vì thanh khoản dồn về; gap qua đêm dễ bị "giả" nếu chỉ do thanh khoản mỏng chứ không phải tin thật | Ưu tiên VB hình thành ngay trước/sau [[18 - Kill Zones]] NY; cẩn trọng VB sinh trong phiên Á thanh khoản thấp — dễ bị nuốt lại ngay khi London mở |
| **EURUSD / GBPUSD** | Chủ yếu là **NWOG** (gap cuối tuần, thị trường đóng cửa thật từ tối thứ Sáu tới Chủ Nhật) — xem [[24 - New Week Opening Gap]]; hiếm khi có session gap giữa tuần vì forex giao dịch liên tục 24/5 | Sunday open thanh khoản cực thấp (chủ yếu Úc/Á mở cửa) → gap cuối tuần dễ bị "spike giả" trước khi ổn định; NWOG có xu hướng được rebalance trong 1–3 ngày đầu tuần nếu không có tin lớn phá vỡ | Không vào lệnh ngay lúc mở cửa Chủ Nhật; chờ thanh khoản London/NY thứ Hai xác nhận hướng trước khi coi NWOG là DOL đáng tin |
| **XAUUSD (Gold)** | Gap chủ yếu do **tin tức** (NFP, CPI, FOMC, biến động địa chính trị) và do vàng giao dịch qua nhiều sàn (spot vs futures) với giờ nghỉ khác nhau; ATR/ngày lớn hơn nhiều so với FX chính | Gap tin tức trên vàng thường **rộng hơn** (tính theo % ATR) và có thể **không rebalance ngay** nếu là displacement thật theo tin cơ bản (thay đổi kỳ vọng lãi suất, risk-off mạnh) — dễ nhầm "gap chờ fill" với "repricing vĩnh viễn" | Với VB do tin: đợi ít nhất 1 nến H1 đóng cửa ổn định, spread thu hẹp về bình thường rồi mới đánh giá; size lệnh nhỏ hơn bình thường vì SL cần rộng hơn theo ATR |

> [!warning] Đừng áp dụng máy móc một bộ luật cho mọi thị trường
> Một VB "unfilled 2 ngày" trên EURUSD có ý nghĩa khác hẳn một VB "unfilled 2 ngày" trên XAUUSD sau tin FOMC. Luôn hỏi: **gap này sinh ra từ cơ chế nào** (đóng/mở phiên thuần túy, hay biến động cơ bản thật)? Câu trả lời quyết định độ tin cậy của magnet.

### Edge cases nâng cao

- **Thống kê partial-fill**: trong thực chiến, đa số VB sinh từ session/weekend gap **chỉ cần chạm CE** là đã đủ để giá tiếp diễn theo bias (partial rebalance) — full fill 100% thường chỉ xảy ra khi VB nằm ngược một xu hướng yếu hoặc thị trường đi ngang tích lũy. Khi backtest, luôn tách riêng hai nhóm số liệu "chạm CE rồi tiếp diễn" và "lấp hết range" — gộp chung sẽ làm sai lệch kỳ vọng entry (xem mục Best Practices bên dưới cho cách log).
- **VB chồng (stacked/nested VB)**: đôi khi một chuỗi phiên liên tiếp để lại nhiều gap nhỏ xếp lớp lên nhau (ví dụ 2–3 phiên gap up liên tiếp trong xu hướng mạnh). Khi đó: (1) coi **toàn bộ dải từ mép ngoài cùng tới mép ngoài cùng** là một "vùng inefficiency tổng hợp", (2) mỗi VB con vẫn có CE riêng — VB con gần giá hiện tại nhất thường được test trước, (3) nếu giá xuyên qua nhiều VB con liên tiếp mà không phản ứng, đó là dấu hiệu **displacement thật** (không phải noise) — hạ ưu tiên coi các VB con này là POI phản ứng, nâng ưu tiên coi cả dải là target liquidity một chiều.
- **VB nằm trong một FVG khung lớn hơn (HTF)**: khi một Vacuum Block (thường ở M15/H1) rơi đúng vào bên trong một Fair Value Gap ở D1/H4, đây là **confluence rất mạnh** vì hai loại inefficiency khác họ (gap thật + imbalance giao dịch liên tục) cùng chỉ về một vùng giá. Quy tắc thực chiến: ưu tiên CE của khung lớn hơn (D1/H4 FVG) làm mục tiêu chính; CE của VB nhỏ hơn dùng để tinh chỉnh entry.
- **VB trở thành breaker sau khi rebalance thất bại**: nếu giá vào vùng VB, cố gắng lấp gap nhưng **thất bại giữa chừng** (không tới CE, bị đẩy ngược lại mạnh kèm displacement) — vùng biên nơi giá bị từ chối có thể hình thành một **breaker block** theo hướng ngược lại. Đây là lúc VB "đổi vai": từ target/POI rebalance chuyển thành vùng cấu trúc cho lệnh ngược hướng ban đầu. Cần MSS xác nhận trước khi coi đây là breaker hợp lệ — không tự suy diễn.

### VB và Algorithmic Price Delivery / IPDA data ranges

ICT mô tả **IPDA (Interbank Price Delivery Algorithm)** như cơ chế thuật toán dẫn giá qua các chu kỳ tra cứu dữ liệu chuẩn: **20 ngày, 40 ngày, 60 ngày**. Vacuum Block liên quan trực tiếp tới khung này theo hai cách:
1. **VB nằm trong phạm vi lookback 20/40/60 ngày** có xác suất được "thăm lại" cao hơn — vì thuật toán định giá được ICT mô tả là quét lại các mức cao/thấp và inefficiency trong các cửa sổ dữ liệu này để tìm thanh khoản và tái cân bằng giá.
2. **VB càng cũ (ngoài mốc 60 ngày)** càng mất dần độ ưu tiên trong khung IPDA hiện tại — không có nghĩa nó vô hiệu vĩnh viễn, nhưng nên hạ ưu tiên xuống dưới các VB mới hơn nằm trong lookback range đang active.

> [!tip] Cách dùng thực tế
> Khi liệt kê danh sách VB unfilled trên D1, đánh dấu thêm cột "cách đây bao nhiêu ngày" và đối chiếu với mốc 20/40/60. VB nằm trong 20 ngày gần nhất luôn được ưu tiên xem xét trước trong phiên phân tích hằng ngày.

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

### Ma trận nhận diện đa khung thời gian (Recognition Matrix)

![[VacuumBlock-Recognition-Matrix.png]]

**Mô tả — Bản đồ minh hoạ nhận diện VB qua nhiều khung thời gian (sơ đồ mẫu, hãy thay bằng chart thật của bạn):**
- Hàng trên cùng: khung D1 — hiển thị 2–3 gap lớn (session/weekend) được khoanh vùng bằng khung chữ nhật, mỗi khung ghi chú range + CE.
- Hàng giữa: khung H4 — cùng một vùng giá nhưng phóng to, cho thấy VB D1 "chứa" nhiều cấu trúc nhỏ hơn (OB, FVG nội bộ) bên trong range của nó.
- Hàng dưới: khung H1/M15 — đánh dấu đường kẻ ngang tại CE của VB D1 kéo dài xuống, cùng chú thích "vùng canh phản ứng LTF".
- Mũi tên nối 3 hàng theo chiều dọc để nhấn mạnh nguyên tắc **top-down**: VB luôn được xác định trước ở khung lớn, sau đó "chiếu" xuống khung nhỏ để tìm entry.

### So sánh dấu hiệu nhận diện theo từng khung thời gian

Không phải mọi khung thời gian đều cho tín hiệu VB rõ như nhau — bảng dưới tổng hợp cách "đọc" gap khác nhau theo khung:

| Khung | Gap dễ thấy nhất từ nguồn nào | Độ tin cậy magnet | Rủi ro đọc sai |
|---|---|---|---|
| **D1** | Weekend gap (NWOG), gap sau tin lớn qua đêm | Cao — ít nhiễu, gap thường lớn và rõ | Dễ bỏ sót gap nhỏ hơn nằm bên trong |
| **H4** | Session gap (đóng/mở phiên), gap sau tin giữa ngày | Trung bình–cao | Có thể nhầm biến động mạnh trong phiên với gap thật nếu không kiểm tra kỹ dữ liệu tick |
| **H1** | Gap quanh chuyển phiên (Á→London, London→NY) | Trung bình | Gap H1 đôi khi chỉ là noise thanh khoản mỏng, không phải inefficiency có ý nghĩa cấu trúc |
| **M15/M5** | Hiếm khi có gap thật (giao dịch gần như liên tục); chủ yếu thấy imbalance kiểu FVG | Thấp cho vai trò "VB", nhưng hữu ích để tìm FVG nội bộ khi entry | Dễ gọi nhầm displacement M5 thành "vacuum" — thực chất là Liquidity Void/FVG, không phải VB đúng nghĩa |

> [!note] Nguyên tắc top-down bắt buộc
> Luôn **xác định VB ở D1/H4 trước**, sau đó mới dùng H1/M15/M5 để tìm thời điểm entry quanh CE đã đánh dấu. Không tự vẽ VB mới ở khung nhỏ nếu nó không xuất phát từ một gap thật có thể nhìn thấy ở khung lớn hơn — nếu không sẽ nhầm sang Liquidity Void/FVG.

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

### Sơ đồ quy trình top-down đầy đủ (MTF Flow)

![[VacuumBlock-MTF-Flow.png]]

**Mô tả — Flowchart minh hoạ quy trình phân tích VB từ D1 xuống M1 (sơ đồ khối, hãy vẽ lại hoặc thay bằng ảnh chụp quy trình thật của bạn):**
- Khối 1 (trên cùng): "D1/H4 — Quét toàn bộ VB unfilled + xác định bias" → mũi tên xuống.
- Khối 2: "Chọn VB làm DOL chính (đúng phía bias + confluence)" → mũi tên xuống, có nhánh rẽ "Không đạt điều kiện → loại, quay lại Khối 1".
- Khối 3: "H1/M15 — Theo dõi giá tiếp cận mép/CE, quan sát phản ứng sơ bộ" → mũi tên xuống.
- Khối 4: "M5/M1 — Chờ liquidity sweep + displacement/MSS tại VB" → nhánh rẽ "Không có xác nhận → KHÔNG vào lệnh, tiếp tục chờ".
- Khối 5 (dưới cùng): "Entry tại FVG nội bộ → SL ngoài mép xa → TP theo CE/mép đối diện/DOL kế" → khối kết thúc "Log vào nhật ký (xem Best Practices)".

### Quy tắc phân bổ thời gian quan sát theo khung

Một sai lầm phổ biến là dành quá nhiều thời gian "canh" VB ở khung lớn và quá ít thời gian xác nhận ở khung nhỏ (hoặc ngược lại). Phân bổ hợp lý:

| Giai đoạn | Khung chính | Mục tiêu | Tần suất kiểm tra |
|---|---|---|---|
| Quét & lập danh sách VB | D1/H4 | Xác định toàn bộ VB unfilled, gắn cột "ngày tuổi" theo IPDA 20/40/60 | 1 lần/ngày (đầu phiên) |
| Theo dõi tiếp cận | H1/M15 | Phát hiện giá bắt đầu di chuyển về VB đã chọn | Vài lần/phiên, tăng tần suất khi giá còn cách CE < 1×ATR(H1) |
| Xác nhận & bấm entry | M5/M1 | Bắt sweep + displacement/MSS, vào lệnh đúng FVG nội bộ | Liên tục trong Kill Zone khi giá đã chạm vùng VB |

### Tình huống đặc biệt: VB xuất hiện ngay trong Kill Zone đang active

Khi một gap mới (ví dụ session-gap NQ1 lúc mở cửa NY) hình thành **ngay trong** [[18 - Kill Zones]] đang diễn ra, quy trình top-down chuẩn (D1 → H1 → M5) không kịp áp dụng tuần tự. Xử lý thực tế:
1. Xác nhận ngay đây có phải gap thật (đứt gãy giao dịch) hay chỉ là nến biến động mạnh trong dữ liệu — kiểm tra dữ liệu tick/giá mở cửa chính thức nếu có thể.
2. Đo nhanh range + CE trên khung đang giao dịch (thường H1/M15).
3. **Không vào lệnh ngay** — một VB vừa sinh ra trong phiên biến động cần ít nhất một nhịp ổn định (1–2 nến) trước khi coi là POI đáng tin, vì spread/độ trượt giá ngay lúc mở phiên có thể tạo tín hiệu giả.

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

## Best Practices

> [!tip] Kỷ luật thực thi (execution discipline)
> - **Không bao giờ đặt lệnh limit "mù" ngay tại mép xa của VB** chỉ vì "gap sẽ fill". Luôn chờ xác nhận (sweep + displacement/MSS) trước khi đặt lệnh — limit đặt sẵn không xác nhận là cách nhanh nhất để bị "quét" bởi một cú spike rồi đảo chiều ngược lại.
> - Nếu dùng limit order để đón phản ứng tại CE, hãy đặt **sau khi đã thấy dấu hiệu chậm lại** (wick dài, absorption) ở khung LTF — không đặt limit ngay khi vừa phát hiện VB ở D1/H4.
> - Với VB sinh trong lúc tin ra hoặc ngay đầu phiên biến động: **ưu tiên market order sau xác nhận**, tránh limit order vì spread/độ trượt có thể khiến giá không bao giờ khớp đúng mức mong muốn hoặc khớp vào đúng đỉnh/đáy spike giả.
> - Không dời SL ra xa hơn "để tránh bị quét" quanh VB — nếu setup cần SL rộng hơn mức risk cho phép, giảm size chứ không nới SL.

> [!warning] Position sizing theo biến động của gap
> - Kích thước gap (range VB) và ATR tại thời điểm đó quyết định độ rộng SL hợp lý — **không dùng size cố định cho mọi VB**. Gap càng rộng so với ATR trung bình, SL càng cần rộng hơn tương ứng → size phải giảm để giữ đúng rủi ro ≤0.5%/lệnh.
> - Với **XAUUSD và các VB gốc tin tức**: mặc định coi ATR đã tăng đột biến, tính size dựa trên SL rộng hơn bình thường (ví dụ dùng ATR(H1) đo ngay sau tin, không dùng ATR trung bình 14 ngày trước đó).
> - Với **NWOG trên EURUSD/GBPUSD**: nếu gap hình thành sau một tuần có tin vĩ mô lớn (bầu cử, quyết định lãi suất cuối tuần), coi như biến động tăng và giảm size 30–50% so với NWOG "bình thường" cho tới khi thị trường ổn định lại sau phiên mở cửa thứ Hai.
> - Không bao giờ tăng size chỉ vì "gap này to nên chắc ăn" — gap to đi kèm rủi ro trượt giá/SL rộng hơn, không đồng nghĩa xác suất thắng cao hơn.

**Phương pháp backtest cho Vacuum Block:**

| Bước | Nội dung |
|---|---|
| 1. Cỡ mẫu | Backtest tối thiểu **20–30 VB** mỗi thị trường trước khi rút kết luận (khớp với mốc "Tested" ở mục 14); tách riêng mẫu theo loại (session/weekend/news) vì hành vi khác nhau |
| 2. Log partial vs full | Với mỗi VB: ghi rõ giá có chạm CE không, có lấp hết range không, và **giá đóng cửa nến xác nhận ở đâu** so với CE — không chỉ ghi "rebalance: có/không" |
| 3. Thống kê cần theo dõi | Tỉ lệ % partial vs full theo từng loại gap; R trung bình đạt được từ entry tại CE; thời gian trung bình (số nến/giờ) từ lúc gap hình thành tới lúc chạm CE; tỉ lệ VB bị bỏ qua do vi phạm checklist mục 5 |
| 4. Phân tách theo thị trường | Không gộp chung NQ1, EURUSD/GBPUSD, XAUUSD vào một bảng thống kê — hành vi gap khác nhau theo cơ chế sinh ra (xem bảng cross-market ở mục 1) |
| 5. Đối chiếu IPDA | Ghi thêm "tuổi" của VB tại thời điểm test (trong hay ngoài mốc 20/40/60 ngày) để sau này đánh giá có mối liên hệ giữa độ tuổi và tỉ lệ rebalance hay không |

**Trường dữ liệu nên có trong nhật ký (journaling fields) khi log một trade quanh VB:**
- Loại VB (gap up/down, session/news/weekend), thị trường, khung hình thành.
- Range gap (mép trên/dưới), CE, và tuổi VB tính theo ngày tại thời điểm vào lệnh.
- Có confluence không (OB/FVG/liquidity/PD level nào).
- Xác nhận tại VB: loại sweep, loại displacement/MSS, có FVG nội bộ không.
- Kết quả: partial hay full rebalance, R đạt được, có vi phạm checklist nào không (liên kết [[06 - Mistake Database]] nếu có).
- Ghi chú ATR/biến động tại thời điểm vào lệnh (đặc biệt bắt buộc với XAUUSD và mọi news-gap).

**Bảng đối chiếu: thói quen nghiệp dư vs thói quen chuyên nghiệp**

| Tình huống | Thói quen nghiệp dư | Thói quen chuyên nghiệp |
|---|---|---|
| Phát hiện VB mới | Vào lệnh ngay khi giá chạm mép gap | Chờ sweep + displacement/MSS xác nhận trước khi hành động |
| Đặt lệnh chờ | Đặt limit "mù" tại CE hoặc mép xa từ sớm | Chỉ đặt limit sau khi LTF cho dấu hiệu phản ứng rõ |
| Size lệnh | Dùng size cố định cho mọi VB bất kể độ rộng gap | Điều chỉnh size theo ATR/độ rộng gap để giữ đúng ≤0.5% risk |
| VB do tin tức | Nhảy vào ngay giữa cú spike vì "sợ bỏ lỡ" | Đợi nến đóng cửa ổn định, spread bình thường rồi mới đánh giá |
| VB đã filled | Vẫn cố tìm phản ứng tại gap cũ | Loại khỏi danh sách theo dõi, tìm DOL/VB mới |
| Backtest | Xem vài ví dụ "đẹp" rồi kết luận VB "luôn work" | Backtest ≥20–30 mẫu, tách theo loại gap và thị trường, log đầy đủ partial/full |
| Nhật ký | Chỉ ghi thắng/thua, không ghi lại bối cảnh VB | Ghi đủ trường dữ liệu ở trên để review được nguyên nhân gốc rễ |
| VB chồng lớp | Coi mỗi VB con là một cơ hội entry riêng lẻ | Đánh giá cả dải tổng hợp, ưu tiên VB con gần giá nhất, cảnh giác displacement thật |

---

## 9. Checklist trước khi áp dụng vào trade

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

## 10. Lỗi thường gặp

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

## 11. Câu hỏi tự kiểm tra
- VB khác FVG ở điểm cốt lõi nào? (gợi ý: có/không giao dịch ở giữa)
- Vì sao một gap unfilled lại hoạt động như nam châm?
- CE của VB là gì và vì sao nó quan trọng hơn việc fill 100%?
- Khi nào một VB nên bị bỏ qua?
- NWOG quan hệ thế nào với Vacuum Block?
- Trước khi vào lệnh quanh VB cần xác nhận gì?

---

## 12. Flashcards / Active Recall

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

## 13. Lesson Learned

> [!example] Ghi chú quan sát cá nhân
> - (Điền sau khi backtest/live) VB loại nào trên NQ1/NAS100 hay được rebalance nhất? ____
> - Tỉ lệ partial (chạm CE) vs full fill quan sát được: ____
> - News-gap có đáng giao dịch không, hay nên đứng ngoài? ____
> - Sai lầm lặp lại của bản thân khi đọc VB: ____

---

## 14. Mức độ thành thạo

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