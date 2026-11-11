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
  - trading/deep-dive
status: developing
category: PD Array
last_reviewed: 2026-07-06
created: 2026-06-24
updated: 2026-07-28
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
- **Weekend gap**: gap giữa giá đóng cửa thứ Sáu và giá mở cửa Chủ Nhật/thứ Hai — liên quan trực tiếp tới [[24-New-Week-Opening-Gap]].
- **News gap / runaway candle**: cú displacement mạnh quanh tin tức (NFP, CPI, FOMC) khiến giá nhảy qua một dải mà thanh khoản gần như cạn — để lại "vacuum" trên cây nến tin.

### Bản chất (vacuum / void)
Bản chất của VB là một **vùng định giá bị bỏ qua**. Giống như một chân không vật lý hút vật chất vào, vùng giá rỗng này "hút" giá quay lại. ICT mô tả đây là một dạng **Liquidity Void** đặc thù — nhưng điểm khác biệt là VB sinh ra từ **không có giao dịch (gap thật)**, chứ không phải từ chuỗi nến chạy nhanh trong giao dịch liên tục.

### Cách vẽ gap + CE
1. Xác định **mép trên** của gap = mức thấp nhất của vùng giao dịch phía trên (ví dụ open của phiên mới khi gap down, hoặc đáy cây nến trên khi gap up).
2. Xác định **mép dưới** của gap = mức cao nhất của vùng giao dịch phía dưới (ví dụ close phiên trước, hoặc đỉnh cây nến dưới).
3. Vùng giữa hai mép = **Vacuum Block range** `[mép trên] – [mép dưới]`.
4. **CE 50%** = `(mép trên + mép dưới) / 2`. Đây là **mean threshold** — ngưỡng phản ứng quan trọng nhất, thường là nơi giá tối thiểu chạm tới trước khi tiếp diễn (xem [[10-Consequent-Encroachment-Mean-Threshold]]).

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
- Hỗ trợ xác định **premium/discount** trong [[12-Dealing-Range]] (xem [[27-Premium-Discount]]).

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
- **Không phải** thay thế bias — VB chỉ trả lời "về đâu", còn "đi hướng nào" vẫn do [[59-Daily-Bias]] quyết định.

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
| **NQ1 / NDX (NAS100)** | Session gap quanh giờ mở cửa RTH (futures đóng cửa ngắn rồi mở lại), gap qua đêm (overnight gap) do CME có phiên electronic gần như 24h nhưng thanh khoản mỏng ngoài RTH | Gap quanh mở cửa NY thường **rebalance rất nhanh** (trong Kill Zone London/NY mở) vì thanh khoản dồn về; gap qua đêm dễ bị "giả" nếu chỉ do thanh khoản mỏng chứ không phải tin thật | Ưu tiên VB hình thành ngay trước/sau [[18-Kill-Zones]] NY; cẩn trọng VB sinh trong phiên Á thanh khoản thấp — dễ bị nuốt lại ngay khi London mở |
| **EURUSD / GBPUSD** | Chủ yếu là **NWOG** (gap cuối tuần, thị trường đóng cửa thật từ tối thứ Sáu tới Chủ Nhật) — xem [[24-New-Week-Opening-Gap]]; hiếm khi có session gap giữa tuần vì forex giao dịch liên tục 24/5 | Sunday open thanh khoản cực thấp (chủ yếu Úc/Á mở cửa) → gap cuối tuần dễ bị "spike giả" trước khi ổn định; NWOG có xu hướng được rebalance trong 1–3 ngày đầu tuần nếu không có tin lớn phá vỡ | Không vào lệnh ngay lúc mở cửa Chủ Nhật; chờ thanh khoản London/NY thứ Hai xác nhận hướng trước khi coi NWOG là DOL đáng tin |
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
| **Weekend-gap VB (NWOG)** | Gap close Fri ↔ open Sun/Mon | Mốc tham chiếu tuần; xem [[24-New-Week-Opening-Gap]] |
| **Filled VB** | Giá đã chạm hết range gap | Inefficiency hết hiệu lực → ưu tiên thấp |
| **Unfilled VB** | Gap còn nguyên hoặc chỉ partial | Vẫn là magnet active → ưu tiên cao |

### Khi nào giá trị cao?
- [ ] VB **chưa được lấp** (unfilled) hoặc mới partial tới CE.
- [ ] VB trùng hướng với [[59-Daily-Bias]] (VB nằm đúng phía của draw on liquidity).
- [ ] VB nằm ở vùng premium/discount hợp lý của [[12-Dealing-Range]].
- [ ] VB hình thành kèm **displacement** rõ ([[Displacement]]) hoặc sau một [[20-Liquidity-Sweep]].
- [ ] VB trùng với một PD Array khác (Order Block, FVG, đỉnh/đáy thanh khoản cũ) → confluence.
- [ ] Đang trong [[18-Kill-Zones]] phù hợp khi giá tiếp cận VB.

### Khi nào bỏ qua?
- [ ] VB đã **filled hoàn toàn** từ lâu (hết năng lượng magnet).
- [ ] Gap quá nhỏ / nhiễu, không tách bạch khỏi cấu trúc xung quanh.
- [ ] VB **ngược bias** mạnh và không có confluence — dễ là bẫy phản ứng yếu.
- [ ] News-gap trong môi trường biến động cực mạnh, spread giãn, chưa rõ hướng AMD ([[02-AMD]]).
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
| Đồng pha bias | Cùng hướng [[59-Daily-Bias]] | Ngược bias, không lý do |
| Xúc tác | Sinh từ news/session/sweep | Không rõ nguyên nhân |

### Điều kiện bắt buộc
- Có **gap thật** (đứt gãy) — không phải dải nến liên tục.
- Đo được **range gap + CE** một cách khách quan.
- VB còn **unfilled hoặc partial**.

### Điều kiện tăng xác suất
- Trùng hướng [[59-Daily-Bias]] và là **draw on liquidity** hợp lý.
- Có **confluence** với PD Array khác.
- Sinh sau **liquidity sweep** rồi **displacement** ([[21-Market-Structure-Shift]] xác nhận).
- Giá tiếp cận trong [[18-Kill-Zones]].

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
- Đánh dấu range + CE của từng VB. Ghi chú VB nào nằm phía DOL theo [[59-Daily-Bias]].
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
- Chờ **liquidity sweep + displacement / MSS** ngay tại VB ([[21-Market-Structure-Shift]], [[Displacement]]).
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

Khi một gap mới (ví dụ session-gap NQ1 lúc mở cửa NY) hình thành **ngay trong** [[18-Kill-Zones]] đang diễn ra, quy trình top-down chuẩn (D1 → H1 → M5) không kịp áp dụng tuần tự. Xử lý thực tế:
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
- [[24-New-Week-Opening-Gap]] — VB cuối tuần làm mốc tham chiếu & magnet tuần.
- [[21-Liquidity-Void]] — họ hàng gần: void cần rebalance.
- [[Fair Value Gap]] — dùng FVG nội bộ để tinh chỉnh entry tại VB.
- [[Order Block]] — confluence khi VB trùng OB.
- [[20-Liquidity-Sweep]] / [[21-Market-Structure-Shift]] — tín hiệu xác nhận tại VB.

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
- [ ] Đã xác định [[59-Daily-Bias]] hôm nay?
- [ ] VB nằm đúng phía draw on liquidity theo bias?
- [ ] VB ở vùng premium/discount hợp lý ([[27-Premium-Discount]], [[12-Dealing-Range]])?

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

---

# Phần mở rộng chuyên sâu (Deep Dive)

> [!info] Phần bổ sung 2026-07-28
> Nội dung dưới đây là phần mở rộng chuyên sâu được bổ sung vào 2026-07-28, viết theo góc nhìn trader ICT/SMC kỳ cựu kết hợp phản biện khách quan. Phần gốc phía trên giữ nguyên không thay đổi.

## A. Phân tích chuyên sâu

### A1. Cơ chế order-flow / microstructure đằng sau hiện tượng "vacuum"

Về bản chất thị trường vi mô, một Vacuum Block không phải là một khái niệm huyền bí — nó là hệ quả trực tiếp của cách sổ lệnh (order book) và cơ chế khớp lệnh hoạt động khi có sự gián đoạn giao dịch. Trong điều kiện giao dịch liên tục (continuous trading), giá di chuyển từng bước nhỏ vì luôn có người mua/bán sẵn sàng khớp lệnh ở các mức liền kề — sổ lệnh dày đặc theo cả hai chiều quanh giá hiện tại. Khi thị trường đóng cửa (hết phiên, cuối tuần) hoặc khi một tin tức bất ngờ khiến toàn bộ market maker/liquidity provider đồng loạt rút lệnh và điều chỉnh giá chào mua/bán, sổ lệnh tại dải giá cũ biến mất gần như tức thời — không ai còn đặt lệnh limit ở đó nữa. Khi giao dịch nối lại (mở phiên mới, hoặc thanh khoản quay lại sau tin), sổ lệnh được xây dựng lại quanh một mức giá mới, phản ánh thông tin/kỳ vọng đã thay đổi. Dải giá ở giữa — nơi sổ lệnh cũ đã biến mất và sổ lệnh mới chưa từng tồn tại — chính là vacuum theo đúng nghĩa vi mô: không có limit order nào residual ở đó, không có ai từng đồng ý giao dịch ở mức đó.

Điều này giải thích tại sao giá "di chuyển nhanh" khi đi qua một VB: tốc độ di chuyển của giá tỷ lệ nghịch với độ dày thanh khoản cản đường. Một dải không có limit order nào để hấp thụ lệnh market sẽ bị vượt qua gần như ngay lập tức khi có bất kỳ lệnh nào đi vào hướng đó, trong khi vùng có order flow thật (nơi từng có giao dịch) sẽ làm chậm giá lại vì cần "ăn" qua các lớp lệnh chờ. Đây cũng là lý do tại sao CE (50%) thường là nơi giá bắt đầu phản ứng rõ hơn mép xa của gap — CE là điểm giữa hai vùng có order flow thật, và các thuật toán định giá lại (repricing algorithms) thường coi trung điểm là một ước lượng hợp lý cho "giá trị công bằng tạm thời" trước khi tiếp tục thu thập thêm thông tin về hướng đi thật.

### A2. Góc nhìn phi-ICT: Auction Market Theory và Market Profile

Không cần khung ICT, khái niệm "gap cần được lấp" đã tồn tại từ lâu trong lý thuyết Market Profile và Auction Market Theory (Steidlmayer). Theo lý thuyết này, thị trường là một quá trình đấu giá hai chiều liên tục nhằm tìm "giá trị công bằng" (fair value) — nơi khối lượng giao dịch nhiều nhất tích lũy quanh một dải giá gọi là Value Area, với điểm đỉnh mật độ gọi là Point of Control (POC). Một gap giá đại diện cho một "khoảng trống trong quá trình đấu giá" (auction gap) — thị trường đã "nhảy" từ một Value Area sang một Value Area khác mà không hoàn thành quá trình đấu giá ở giữa. Market Profile truyền thống gọi đây là "single print" hoặc "poor structure" khi biểu diễn trên biểu đồ TPO (Time Price Opportunity), và có quan sát thực nghiệm tương tự ICT: các vùng "single print"/gap thường được "lấp" (filled) khi thị trường quay lại hoàn tất quá trình đấu giá bị bỏ dở, đặc biệt nếu gap đó không được ủng hộ bởi một thay đổi giá trị cơ bản thật sự.

Điểm khác biệt về ngôn ngữ nhưng tương đồng về bản chất: ICT gọi đó là "inefficiency cần rebalance", Market Profile gọi đó là "cấu trúc kém/single print cần hoàn thiện", còn phân tích kỹ thuật cổ điển gọi đây đơn giản là "gap-fill". Cả ba trường phái đều đồng ý ở một điểm cốt lõi: gap không phải luôn được lấp — chỉ khi không có đủ thông tin cơ bản mới hỗ trợ mức giá mới thì thị trường mới có xu hướng quay lại vùng cũ; nếu gap phản ánh một thay đổi giá trị thật (ví dụ tin tức làm thay đổi kỳ vọng lãi suất một cách bền vững), gap có thể không bao giờ được lấp lại — đây chính xác là điều ICT cũng thừa nhận qua khái niệm "news-gap có thể là displacement thật".

### A3. Định lượng: các biến số cần thiết kế khi backtest Vacuum Block

Nội dung gốc đã đề cập bảng backtest cơ bản (mục Best Practices), nhưng để backtest VB một cách khoa học và có thể tái lập, cần định nghĩa rõ ràng các biến trước khi bắt đầu ghi log:

| Biến | Định nghĩa cụ thể cần thống nhất trước | Vì sao quan trọng |
|---|---|---|
| Ngưỡng "gap thật" tối thiểu | Ví dụ: gap ≥ 0.1× ATR(D1) mới tính là VB, tránh nhiễu từ gap vi mô không đáng kể | Nếu không có ngưỡng rõ, số lượng VB "phát hiện" sẽ phụ thuộc chủ quan người backtest |
| Điểm bắt đầu đếm "tuổi" VB | Tính từ nến đóng cửa hình thành gap, hay từ thời điểm phát hiện trên chart? | Ảnh hưởng trực tiếp tới việc đối chiếu với mốc IPDA 20/40/60 ngày |
| Tiêu chí "đã chạm CE" | Wick chạm đủ, hay cần đóng cửa nến vượt qua CE? | Dữ liệu wick kém chính xác (đặc biệt forex) có thể tạo tín hiệu giả nếu chỉ dùng wick |
| Tiêu chí "displacement xác nhận" | Số ATR tối thiểu của nến displacement, có yêu cầu đóng cửa ngoài range trước đó không | Thiếu tiêu chí rõ ràng khiến việc phân loại case "có xác nhận" vs "không có" mang tính hồi cứu (nhìn biết trước kết quả rồi gán nhãn) |
| Khung xác nhận cắt lỗ | SL đặt ngoài mép xa VB hay theo ATR cố định? | Ảnh hưởng trực tiếp R-multiple tính được, cần nhất quán giữa các mẫu để so sánh công bằng |

> [!tip] Nguyên tắc thiết kế biến
> Viết ra toàn bộ định nghĩa biến số **trước khi** bắt đầu backtest, không điều chỉnh giữa chừng khi thấy kết quả không như ý — đây là cách duy nhất để tránh curve-fitting vô thức trong quá trình tự backtest thủ công.

### A4. Tương tác với các khái niệm ICT khác — quy tắc ưu tiên khi xung đột

Vacuum Block hiếm khi hoạt động độc lập; nó thường chồng lấp hoặc mâu thuẫn với các PD Array khác. Dưới đây là các quy tắc thực chiến để giải quyết xung đột:

- **VB vs Order Block:** khi một VB (target) nằm ngay trước một Order Block hợp lệ theo cùng hướng, ưu tiên coi toàn bộ dải OB + VB là một "vùng phản ứng tổng hợp" — không tách biệt xử lý riêng. Nếu OB nằm giữa giá hiện tại và VB (tức OB "chắn đường" trước khi giá tới VB), kỳ vọng giá phản ứng tại OB trước, VB vẫn giữ vai trò target xa hơn nếu OB bị phá.
- **VB vs Liquidity Pool (đỉnh/đáy cũ):** nếu draw on liquidity gần nhất là một đỉnh/đáy có thanh khoản rõ (dừng lệnh tích lũy) nằm *trước* VB theo hướng di chuyển, ưu tiên coi liquidity pool là target ưu tiên hơn — vì đó là nơi có "nhiên liệu" (dừng lệnh) để đẩy giá, trong khi VB chỉ là "khoảng trống cần lấp" không nhất thiết có động lực đẩy giá tới đó trước.
- **VB vs Daily Bias mâu thuẫn:** nếu VB nằm ngược hướng Daily Bias, tuyệt đối không coi đó là target chính — quy tắc gốc đã nêu rõ điều này, nhưng cần bổ sung: một VB ngược bias vẫn có thể đóng vai trò *POI phòng thủ* (nơi dự kiến giá phản ứng ngắn hạn nếu bias đang bị nghi ngờ), không phải nơi tìm entry theo hướng bias.
- **VB vs FVG khung nhỏ hơn nằm bên trong:** như mục gốc đã nêu (VB chứa FVG con), quy tắc ưu tiên là CE của khung lớn hơn quyết định target chính, còn FVG nội bộ dùng để tinh chỉnh entry — không đảo ngược thứ tự ưu tiên này.

### A5. So sánh định lượng sơ bộ: VB theo loại nguồn gốc (minh hoạ nguyên tắc, không phải số liệu thật)

![[VacuumBlock-DeepDive-SourceCompare.svg]]
*Minh hoạ nguyên tắc: đặc điểm rebalance khác nhau giữa gap phiên, gap cuối tuần và gap tin tức — số liệu trong sơ đồ chỉ mang tính minh hoạ khái niệm, không phải kết quả backtest thật.*

Ba loại nguồn gốc gap có đặc tính hành vi khác nhau về cơ bản, và việc gộp chung chúng vào một bảng thống kê (như đã cảnh báo ở mục Best Practices gốc) sẽ làm sai lệch nghiêm trọng kỳ vọng entry. Về mặt lý thuyết order-flow: gap phiên (session-gap) chủ yếu phản ánh sự gián đoạn thanh khoản thuần túy (không có thông tin cơ bản mới) nên có xu hướng được rebalance nhanh và đầy đủ hơn khi thanh khoản quay lại. Gap cuối tuần (NWOG) nằm giữa hai thái cực — đôi khi thuần túy do thị trường đóng cửa, đôi khi phản ánh tin tức cuối tuần thật (địa chính trị, quyết định ngân hàng trung ương công bố ngoài giờ). Gap tin tức thường mang thông tin cơ bản thật, nên có xác suất trở thành "displacement thật không rebalance" cao hơn hẳn hai loại kia — đây là lý do vì sao quy tắc gốc luôn nhấn mạnh phải phân loại nguồn gốc trước khi đánh giá độ tin cậy của magnet.

### A6. Vì sao CE 50% được ưu tiên hơn full-fill — góc nhìn thống kê phân phối

![[VacuumBlock-DeepDive-CEmechanism.svg]]
*Minh hoạ cơ chế repricing: CE là trung điểm phân phối xác suất "giá trị hợp lý" giữa order-flow cũ và mới.*

Nếu hình dung xác suất "giá trị công bằng thật" phân bố dạng chuông (bell-shaped) quanh một điểm nào đó trong dải gap thay vì phân bố đều tuyệt đối, thì trung điểm dải là ước lượng hợp lý nhất cho kỳ vọng (median/mean) khi không có thêm thông tin nào khác để thiên vị về phía nào. Đây là lý do thống kê (không phải huyền bí) khiến CE thường là nơi giá "đủ" phản ứng để tiếp diễn — một khi giá đã tiến vào vùng có xác suất cao nhất là "giá trị hợp lý", động lực đẩy giá tiếp tục xuyên qua toàn bộ dải giảm đi đáng kể vì phần còn lại của dải có xác suất thấp hơn là "cần thiết phải test". Điều này không loại trừ khả năng full-fill vẫn xảy ra (đặc biệt trong thị trường sideway không có xu hướng rõ, khi không có động lực đẩy giá đi tiếp sau khi chạm CE) — chỉ giải thích vì sao *xác suất* dừng lại quanh CE cao hơn xác suất fill hết dải, theo đúng những gì quy tắc gốc mô tả qua khái niệm "partial rebalance".

### A7. Vấn đề đo lường "unfilled" khi có nhiều khung thời gian mở đồng thời

Một vấn đề thực dụng ít được nói tới: khi một trader theo dõi VB trên nhiều khung (D1, H4, H1) đồng thời, dễ xảy ra tình huống một VB "đã filled" trên khung H1 (do một cây nến H1 xuyên qua toàn bộ range) nhưng vẫn hiển thị "chưa filled" trên khung D1 nếu nến D1 đó chưa đóng cửa — gây nhầm lẫn về trạng thái thật của VB. Nguyên tắc xử lý: trạng thái "filled/unfilled" của một VB nên được đánh giá dựa trên **giá đã thực sự đi qua** (theo dữ liệu tick/M1 thật), không phụ thuộc vào khung đang mở để xem — khung thời gian chỉ ảnh hưởng tới việc VB đó được *hiển thị/nhận diện* dễ hay khó, không thay đổi bản chất việc giá đã đi qua vùng đó hay chưa.


### A10. Lưu ý về việc trình bày VB trong nhật ký giao dịch để tối ưu hoá quá trình học tập

Ngoài các trường dữ liệu đã liệt kê trong phần Best Practices gốc, một thực hành hữu ích bổ sung là ghi chú lại **giả thuyết ban đầu** về lý do gap hình thành (ví dụ: "nghi ngờ do thanh khoản mỏng cuối tuần, không có tin tức rõ ràng") tại thời điểm phát hiện VB, trước khi biết kết quả. Việc này giúp so sánh sau này giữa "giả thuyết ban đầu" và "diễn biến thực tế" — nếu giả thuyết ban đầu thường xuyên sai (ví dụ liên tục đánh giá thấp khả năng một gap là displacement thật), đây là dấu hiệu cần điều chỉnh lại tiêu chí phân loại nguồn gốc gap của cá nhân, thay vì chỉ ghi nhận kết quả thắng/thua mà không truy vết lại quá trình suy luận ban đầu.

> [!tip] Mẫu ghi chú giả thuyết ban đầu
> "Gap [loại] trên [thị trường], nghi ngờ nguồn gốc: [session/weekend/news/không rõ]. Dự đoán khả năng rebalance: [cao/trung bình/thấp], vì: [lý do]. — Ghi lại TRƯỚC khi biết kết quả, đối chiếu lại sau."

---

## B. Phản biện & giới hạn — Devil's Advocate

### Vấn đề falsifiability và hindsight bias

Giống như nhiều khái niệm PD Array khác trong ICT, "Vacuum Block là magnet hút giá" là một tuyên bố khó kiểm chứng theo tiêu chuẩn khoa học chặt chẽ vì nó không đưa ra một khung thời gian cụ thể để phán định đúng/sai. Nếu giá quay lại lấp gap sau 2 ngày, đó được coi là "VB hoạt động đúng như dự đoán". Nếu giá không quay lại trong nhiều tuần, lý giải thường là "đây là displacement thật, không phải VB đáng tin do market context đã đổi" — về cơ bản không có kịch bản nào có thể bác bỏ hoàn toàn giả thuyết ban đầu, vì mọi kết quả đều có thể được diễn giải phù hợp sau khi đã biết kết quả. Đây chính là vấn đề *hindsight bias* điển hình: nhìn lại một VB đã fill và nói "đúng như dự đoán, đó là magnet" dễ hơn nhiều so với dự đoán trước rằng một VB cụ thể sẽ fill trong bao lâu và ở mức độ nào (partial hay full).

### Thiếu bằng chứng nghiên cứu độc lập/peer-reviewed

Cũng cần thẳng thắn thừa nhận: không có nghiên cứu học thuật độc lập, peer-reviewed nào (trong lĩnh vực tài chính định lượng, market microstructure academic) xác nhận cụ thể khái niệm "Vacuum Block" theo đúng định nghĩa và cách phân loại của ICT. Hiện tượng "gap có xu hướng được lấp" đã được quan sát và thảo luận trong tài liệu phân tích kỹ thuật cổ điển và một số nghiên cứu về gap trading trên cổ phiếu/futures, nhưng các nghiên cứu đó thường đo lường tỷ lệ gap-fill theo phương pháp thống kê nghiêm ngặt (mẫu lớn, kiểm định giả thuyết) và kết quả không đồng nhất — tỷ lệ lấp gap dao động rất nhiều tùy loại tài sản, kích thước gap, và điều kiện thị trường, không có con số "chuẩn" nào áp dụng phổ quát. Framework ICT về VB/CE/rebalance là một hệ thống diễn giải thực chiến (heuristic) được xây dựng từ quan sát cá nhân và truyền miệng trong cộng đồng, không phải kết quả của một nghiên cứu định lượng công bố với phương pháp luận minh bạch.

### Giải thích thay thế đơn giản hơn cho hiện tượng "gap thường được lấp"

Có ít nhất ba cách giải thích khác, không cần khung ICT, cho cùng hiện tượng quan sát được:
1. **Mean reversion thống kê thuần túy:** nhiều chuỗi giá tài chính có tính chất mean-reverting trong ngắn hạn sau một cú di chuyển mạnh bất thường (dù không phải gap) — gap chỉ là một trường hợp đặc biệt của "di chuyển mạnh bất thường", và xu hướng quay lại sau đó có thể chỉ là biểu hiện của tính chất mean-reversion chung, không đặc thù riêng cho "gap cần lấp".
2. **Chốt lời (profit-taking) tự nhiên:** nếu gap hình thành do một nhóm trader vào lệnh mạnh theo hướng gap, hành động chốt lời tự nhiên của họ sau đó (bán ra nếu đã mua, mua vào nếu đã bán) tạo áp lực giá ngược lại — hiện tượng này xảy ra ngẫu nhiên ở nhiều di chuyển giá khác, không riêng gì gap.
3. **Selection bias khi quan sát chart:** trader có xu hướng nhớ và kể lại các case "gap đã lấp đẹp" nhiều hơn các case "gap không bao giờ lấp" (vì case sau không tạo ra một câu chuyện thú vị để phân tích lại) — dẫn tới cảm giác chủ quan rằng gap "luôn" hoặc "thường" được lấp, dù tỷ lệ thật (nếu đo bằng thống kê khách quan) có thể thấp hơn cảm nhận.

### Giới hạn thực tế khi áp dụng

Ngay cả khi chấp nhận khung VB là hữu ích, có những giới hạn thực tế quan trọng: (1) VB không cho biết *thời điểm* nào giá sẽ quay lại — có thể là vài giờ, vài ngày, hoặc vài tháng, khiến việc giữ một kế hoạch giao dịch dựa trên VB xa trở nên khó quản lý vốn/tâm lý; (2) trong thị trường có xu hướng rất mạnh (trending mạnh theo tin tức cơ bản dài hạn), nhiều VB có thể tồn tại "unfilled" trong thời gian dài mà không có ý nghĩa gì cho giao dịch ngắn/trung hạn; (3) việc phân biệt "gap thật" và "nến chạy nhanh" đôi khi mơ hồ ở ranh giới, đặc biệt trên forex nơi không có giờ đóng cửa thị trường rõ ràng giữa tuần — cùng một hiện tượng giá có thể được hai trader khác nhau phân loại khác nhau (một người gọi là VB, người khác gọi là Liquidity Void/FVG lớn).

### Phản biện lại từ góc nhìn người dùng có kỷ luật

Người ủng hộ khung VB có thể phản biện rằng: (1) VB không bao giờ được dùng như tín hiệu entry độc lập trong hệ thống ICT đúng chuẩn — nó luôn cần xác nhận qua sweep + displacement/MSS trước khi vào lệnh, nghĩa là bản thân khung đã có cơ chế tự lọc bớt rủi ro của việc dự đoán sai; (2) việc phân loại nguồn gốc gap (session/weekend/news) và áp dụng ngưỡng tối thiểu (ví dụ ≥0.1×ATR) giúp giảm đáng kể tính chủ quan trong việc xác định "gap thật"; (3) mục tiêu thực dụng của VB không phải "dự đoán chính xác thời điểm" mà là cung cấp một *danh sách ưu tiên khách quan* các vùng giá cần theo dõi, thay thế cho việc chọn mức hỗ trợ/kháng cự hoàn toàn chủ quan.

Tuy nhiên, ngay cả với các cơ chế lọc trên, một số câu hỏi vẫn chưa có câu trả lời chắc chắn: liệu tỷ lệ thắng thực tế của setup "sweep + displacement tại CE của VB" có cao hơn đáng kể so với việc áp dụng cùng tiêu chí sweep + displacement tại một mức hỗ trợ/kháng cự bất kỳ không liên quan gì tới gap? Đây là câu hỏi chỉ có thể trả lời bằng backtest so sánh trực tiếp (A/B) trên cùng bộ dữ liệu, và tác giả gốc của note này không có kết quả backtest như vậy để trích dẫn.

> [!warning] Kết luận phản biện
> - VB **hữu ích** như một công cụ tổ chức thông tin (đánh dấu vùng giá "chưa được đấu giá") để rút gọn danh sách các mức cần theo dõi, đặc biệt kết hợp với xác nhận order-flow (sweep + displacement).
> - VB **kém tin cậy** khi dùng làm tín hiệu độc lập để dự đoán thời điểm hoặc mức độ rebalance, và **không có bằng chứng học thuật** xác nhận riêng khái niệm này ngoài quan sát thực chiến cá nhân/cộng đồng ICT.
> - Để tự kiểm chứng: backtest so sánh trực tiếp tỷ lệ thắng của setup "sweep+displacement tại CE của VB" với setup "sweep+displacement tại mức hỗ trợ/kháng cự ngẫu nhiên không liên quan gap" trên cùng dữ liệu — nếu không có chênh lệch đáng kể, giá trị gia tăng thực sự của riêng khái niệm VB (ngoài phần xác nhận order-flow chung) cần được xem lại.


### B bổ sung — Vấn đề "định nghĩa co giãn" của ngưỡng gap tối thiểu

Một điểm phản biện bổ sung đáng lưu ý: khung ICT không đưa ra một ngưỡng khách quan, thống nhất cho câu hỏi "gap bao nhiêu thì đủ lớn để được coi là Vacuum Block có ý nghĩa" — quyết định này hoàn toàn phụ thuộc vào phán đoán cá nhân của từng trader (dù mục A3 của phần Deep Dive này đã đề xuất một ngưỡng tham khảo dựa trên ATR). Sự thiếu vắng một tiêu chuẩn khách quan, thống nhất trong cộng đồng khiến việc so sánh kết quả backtest giữa các trader khác nhau trở nên khó khăn — hai trader backtest cùng một giai đoạn lịch sử trên cùng một thị trường có thể đưa ra hai danh sách VB khác nhau đáng kể tuỳ theo ngưỡng họ tự đặt ra. Đây là một giới hạn cố hữu của các framework phân tích kỹ thuật mang tính diễn giải (discretionary) nói chung, không riêng gì VB — nhưng cần được nêu rõ để tránh ảo tưởng rằng khái niệm này có độ chính xác định lượng như một chỉ báo toán học thuần túy.

### B bổ sung 2 — Rủi ro khi VB trở thành "cái cớ" hợp lý hoá quyết định đã có sẵn

Một rủi ro tâm lý cần lưu ý: vì VB là một khái niệm khá linh hoạt trong cách áp dụng (magnet, POI, target — tuỳ ngữ cảnh), nó có thể dễ dàng bị dùng như một "cái cớ hợp lý hoá" cho một quyết định giao dịch mà trader đã muốn thực hiện từ trước vì lý do khác (cảm xúc, FOMO, hoặc một tín hiệu kỹ thuật khác không liên quan). Ví dụ: một trader đã muốn vào lệnh Long vì "cảm thấy" thị trường sẽ tăng, sau đó tìm thấy một VB phía trên để "biện minh" cho quyết định đó bằng ngôn ngữ ICT, dù bản thân VB đó không thực sự đáp ứng đủ tiêu chí chất lượng (confluence, đúng bias, có xác nhận). Đây là một dạng confirmation bias được "khoác áo" phân tích kỹ thuật. **Cách phòng tránh:** luôn viết ra checklist đầy đủ (như mục 9 phần gốc) và tự hỏi liệu quyết định có thay đổi không nếu bỏ hoàn toàn yếu tố VB ra khỏi lý luận — nếu câu trả lời là "không, tôi vẫn sẽ vào lệnh này vì lý do khác", thì VB không phải là cơ sở thật sự của quyết định, và cần xem lại toàn bộ logic giao dịch.

---

## C. Case study

### Case 1 — Thắng đẹp: NWOG trên EURUSD được rebalance đúng kịch bản (case tổng hợp từ backtest)

**Bối cảnh:** Thị trường EURUSD đóng cửa thứ Sáu tại `[level A]`, không có tin vĩ mô lớn dự kiến trong cuối tuần. Sáng Chủ Nhật, giá mở cửa cao hơn đáng kể tại `[level B]` (gap up nhẹ, không có tin tức rõ ràng giải thích, có thể do dòng lệnh mỏng lúc mở phiên Á/Úc). Daily Bias tuần đó nghiêng Short dựa trên cấu trúc HTF trước đó.

**Diễn biến từng bước:**
1. Đánh dấu NWOG range `[level A]`–`[level B]`, CE tại điểm giữa.
2. Không vào lệnh ngay lúc mở cửa Chủ Nhật (theo đúng khuyến cáo tránh thanh khoản mỏng).
3. Thứ Hai, phiên London mở cửa, giá bắt đầu trôi xuống về phía CE của NWOG.
4. Tại vùng CE, xuất hiện một liquidity sweep nhỏ (quét đáy phiên Á) kèm nến displacement giảm trên M15, tạo MSS ngắn hạn xác nhận hướng Short tiếp diễn đúng bias tuần.
5. FVG nội bộ hình thành ngay sau nến displacement trên M5.

**Quyết định & lý do:** Vào Short tại FVG nội bộ M5, vì: (a) đúng hướng Daily Bias tuần, (b) CE của NWOG đóng vai trò POI hợp lý cho một pha điều chỉnh trước khi tiếp diễn Short, (c) có xác nhận sweep + displacement + MSS đúng theo checklist, không phải vào lệnh chỉ vì "giá đang test gap". SL đặt ngoài mép xa của FVG nội bộ, TP hướng về draw on liquidity tiếp theo bên dưới NWOG.

**Kết quả (theo R):** Lệnh đạt khoảng 2R trước khi chạm target trung gian, được dời SL về entry sau khi đạt 1R để bảo toàn vốn — một cách quản lý rủi ro hợp lý dù không phải yếu tố cốt lõi của case này.

**Bài học rút ra:** NWOG hoạt động tốt nhất khi (1) không có tin tức lớn làm nhiễu ý nghĩa của gap, (2) hướng rebalance trùng với Daily Bias đã xác định từ trước bằng phân tích cấu trúc độc lập — tức là VB không phải "lý do" để vào lệnh, mà là một *xác nhận bổ sung* cho một bias đã có cơ sở riêng.

### Case 2 — Thua đúng quy trình: News-gap trên XAUUSD không rebalance vì là displacement thật (case tổng hợp từ backtest)

**Bối cảnh:** XAUUSD tăng mạnh sau một dữ liệu CPI thấp hơn dự báo đáng kể, tạo một cú nhảy giá trong vài phút đầu tiên sau tin, để lại một dải giá gần như không có giao dịch ở giữa trên khung M15/H1. Giá đóng cửa nến tin ổn định ở vùng cao, spread đã thu hẹp trở lại sau khoảng 30 phút.

**Diễn biến từng bước:**
1. Đo range gap + CE trên H1 sau khi giá đã ổn định, không hành động ngay lúc spread còn giãn.
2. Theo dõi vài giờ sau, giá tiếp tục tăng thêm mà không quay lại test CE của news-gap.
3. Cuối ngày, giá bắt đầu điều chỉnh nhẹ, chạm gần mép trên của gap (không tới CE), sau đó bật tăng trở lại tiếp tục xu hướng.
4. Một lệnh Short thử nghiệm được đặt tại mép trên của gap với kỳ vọng "ít nhất về CE", có sweep nhỏ nhưng không có displacement giảm rõ ràng xác nhận MSS xuống.

**Quyết định & lý do:** Vào lệnh Short tại mép trên gap dựa trên giả định "gap cần rebalance", nhưng thiếu xác nhận displacement/MSS đầy đủ theo đúng checklist — đây là điểm sai quy trình nhẹ, dù bối cảnh tổng thể (tin CPI mạnh, xu hướng tăng bền vững) đã là tín hiệu cảnh báo rằng đây có khả năng cao là displacement thật (theo đúng phân loại "news-gap có thể không rebalance" trong ghi chú gốc).

**Kết quả (theo R):** SL bị chạm ở mức -1R khi giá tiếp tục tăng xuyên qua mép trên gap mà không có bất kỳ dấu hiệu rebalance nào thêm.

**Bài học rút ra:** Đây là một ví dụ về vi phạm checklist nhẹ (thiếu xác nhận displacement) chồng lên một nhận định bối cảnh sai (đánh giá thấp khả năng đây là displacement thật từ tin cơ bản mạnh). Bài học kép: (1) tuân thủ nghiêm checklist xác nhận dù "cảm thấy" tự tin về gap, (2) với news-gap sau dữ liệu vĩ mô có tác động lớn và bền vững tới định giá cơ bản (thay đổi kỳ vọng chính sách tiền tệ), xác suất "displacement thật không rebalance" cần được đánh giá cao hơn mặc định, không áp dụng máy móc kỳ vọng "gap luôn cần lấp" như với session-gap thông thường.

### Case 3 — Checklist bắt lỗi kịp thời: nghi ngờ VB giả trên NQ1 trong phiên Á thanh khoản mỏng (case tổng hợp từ backtest)

**Bối cảnh:** NQ1 có một khoảng trống giá xuất hiện trong phiên giao dịch điện tử ngoài giờ (overnight/phiên Á), giữa hai nến H1 liên tiếp, nhìn qua giống một session-gap hợp lệ.

**Diễn biến từng bước:**
1. Phát hiện gap trên H1, bắt đầu đo range + CE theo quy trình chuẩn.
2. Trước khi đưa vào danh sách theo dõi chính thức, kiểm tra lại dữ liệu tick/M1 chi tiết quanh thời điểm hình thành gap.
3. Dữ liệu M1 cho thấy thực chất có một vài giao dịch (dù khối lượng rất thấp) đã xảy ra trong dải "gap" đó trên một số nguồn dữ liệu khác — tức đây không phải một gap thật tuyệt đối mà là hệ quả của thanh khoản cực mỏng ngoài giờ RTH kết hợp với cách một số nguồn dữ liệu H1 tổng hợp giá.
4. Quyết định hạ mức tin cậy của "VB" này xuống rất thấp, không đưa vào danh sách DOL chính cho phiên NY sắp tới.

**Quyết định & lý do:** Không giao dịch dựa trên gap này. Lý do: gap sinh ra trong thanh khoản cực mỏng (phiên Á cho một chỉ số Mỹ) có độ tin cậy thấp hơn nhiều so với gap sinh ra quanh giờ mở cửa RTH có thanh khoản sâu — đúng như cảnh báo trong bảng cross-market ở phần gốc.

**Kết quả (theo R):** Không có giao dịch nào được thực hiện — kết quả là 0R, nhưng tránh được khả năng vào lệnh dựa trên một tín hiệu có độ tin cậy thấp.

**Bài học rút ra:** Checklist "kiểm tra dữ liệu tick trước khi tin vào một gap nhìn thấy trên khung tổng hợp cao hơn" là bước phòng ngừa quan trọng, đặc biệt với các thị trường có phiên thanh khoản không đồng đều suốt ngày (index futures Mỹ giao dịch gần 24h nhưng thanh khoản chênh lệch rất lớn giữa RTH và ngoài giờ). Việc "không giao dịch" khi nghi ngờ chất lượng tín hiệu là một kết quả tốt của quy trình, không phải một cơ hội bị bỏ lỡ.

### Case 4 — Sự kiện thị trường thật: gap giá dầu WTI liên quan căng thẳng địa chính trị Trung Đông (mô tả định tính, không trích dẫn giá cụ thể)

**Bối cảnh:** Đây là một case thị trường thật được mô tả ở mức khái quát, không trích dẫn mức giá chính xác: thị trường dầu thô (WTI/Brent) trong lịch sử đã nhiều lần xuất hiện các gap giá cuối tuần hoặc gap qua đêm lớn liên quan tới các sự kiện địa chính trị bất ngờ tại khu vực sản xuất dầu trọng điểm (ví dụ căng thẳng quân sự, gián đoạn nguồn cung). Đặc điểm chung của các sự kiện này là gap hình thành do thay đổi thật trong nhận định về rủi ro nguồn cung — một loại thông tin cơ bản có thể ảnh hưởng lâu dài, không giống một gap thuần túy do thanh khoản gián đoạn.

**Diễn biến từng bước (mô tả khái quát):** Giá dầu gap mạnh khi thị trường mở lại sau tin tức căng thẳng; trong nhiều trường hợp lịch sử, phần lớn mức tăng gap ban đầu được duy trì hoặc chỉ điều chỉnh partial (không lấp hết), đặc biệt nếu căng thẳng chưa được giải quyết ngay; nếu tình hình hạ nhiệt nhanh chóng sau đó, thị trường có xu hướng điều chỉnh lại một phần đáng kể của gap khi rủi ro giảm bớt.

**Quyết định & lý do (theo khung phân tích, không phải khuyến nghị giao dịch lịch sử cụ thể):** Với loại gap này, khung VB gợi ý: không mặc định kỳ vọng full rebalance nhanh chóng, vì bản chất tin tức có thể tạo ra thay đổi định giá bền vững; cần theo dõi diễn biến tin tức tiếp theo (leo thang hay hạ nhiệt) để đánh giá lại xác suất rebalance, thay vì áp dụng máy móc kỳ vọng "gap sẽ được lấp" như một quy luật cố định.

**Kết quả:** Không nêu con số cụ thể (theo đúng yêu cầu không bịa số liệu lịch sử chính xác) — chỉ nhấn mạnh nguyên tắc định tính đã mô tả ở trên.

**Bài học rút ra:** Đây là minh hoạ rõ nhất cho nguyên tắc "phân loại nguồn gốc gap quyết định độ tin cậy magnet" — gap địa chính trị trên hàng hoá năng lượng là ví dụ điển hình của loại gap có xác suất "không rebalance" cao nếu nguyên nhân gốc (rủi ro địa chính trị) chưa được giải quyết, khác hẳn một session-gap thuần kỹ thuật.


### A8. Vacuum Block và khái niệm "half-life" của inefficiency — góc nhìn định lượng bổ sung

Một cách tiếp cận định lượng hữu ích khi tự nghiên cứu VB là mượn khái niệm "half-life" (chu kỳ bán rã) từ thống kê: thay vì hỏi "gap này có được lấp hay không" (câu hỏi nhị phân), hỏi "xác suất gap được lấp (tới CE) giảm dần theo thời gian như thế nào". Trực giác thực chiến của nhiều trader ICT phù hợp với giả thuyết rằng xác suất rebalance cao nhất trong vài phiên đầu sau khi gap hình thành, và giảm dần khi thời gian trôi qua (giá đã "quen" với mức mới, các mức xa dần mất tính liên quan trong bối cảnh thị trường hiện tại). Đây chính là lý do cơ chế IPDA 20/40/60 ngày có ý nghĩa thực dụng: nó là một cách xấp xỉ thô của "cửa sổ nửa đời" cho tính liên quan của một inefficiency, dù ICT không trình bày bằng ngôn ngữ thống kê này.

Hệ quả thực dụng: nếu tự backtest và ghi log đầy đủ tuổi VB tại thời điểm rebalance (như bảng Best Practices gốc đã gợi ý), có thể tự vẽ được một đường cong tần suất kiểu "% VB đã rebalance theo số ngày trôi qua" cho riêng thị trường mình giao dịch — đây là bước nâng cấp từ backtest nhị phân đơn giản sang backtest có ý nghĩa xác suất theo thời gian, hữu ích hơn nhiều cho việc quyết định "còn đáng theo dõi VB này không" sau một khoảng thời gian dài.

### A9. Vacuum Block trong bối cảnh thanh khoản phái sinh — open interest và options gamma (lưu ý cho NQ/ES)

Với các chỉ số futures như NQ1/ES1 có thị trường quyền chọn (options) phát triển song song, một số gap/VB hình thành quanh các mốc thời gian đáo hạn quyền chọn lớn (đặc biệt cuối tháng, "triple witching") có thể chịu ảnh hưởng bổ sung từ hoạt động phòng hộ delta/gamma của market maker quyền chọn — một lớp động lực hoàn toàn khác so với gap thuần túy do thanh khoản gián đoạn. Đây không phải kiến thức cốt lõi của khung ICT truyền thống, nhưng là một lưu ý thực dụng cho trader NQ/ES: nếu một VB hình thành đúng vào giai đoạn đáo hạn quyền chọn lớn, hành vi rebalance của nó có thể bị chi phối một phần bởi dòng lệnh phòng hộ cơ học (không liên quan gì tới phân tích cấu trúc giá thuần túy), khiến việc áp dụng máy móc khung "gap cần lấp" trở nên kém tin cậy hơn trong các giai đoạn này.

> [!note] Không bắt buộc nhưng nên biết
> Trader không giao dịch quyền chọn không cần đi sâu vào cơ chế gamma/delta hedging, nhưng nên ghi nhớ: quanh các ngày đáo hạn quyền chọn lớn trên chỉ số Mỹ, hành vi giá (bao gồm cả gap/VB) có thể nhiễu hơn bình thường vì các yếu tố phái sinh không liên quan tới cấu trúc ICT thuần túy.

---

## C bổ sung — Case 5: Checklist bắt lỗi kịp thời — nhầm lẫn VB với Liquidity Void trên GBPUSD (case tổng hợp từ backtest)

**Bối cảnh:** Trên GBPUSD khung H1, xuất hiện một chuỗi 4-5 nến chạy rất nhanh theo một hướng (không phải cuối tuần, không có tin tức lớn được ghi nhận), tạo cảm giác giống một "khoảng trống giá" lớn khi nhìn tổng thể trên khung H4.

**Diễn biến từng bước:**
1. Ban đầu đánh dấu đây là một VB tiềm năng dựa trên ấn tượng thị giác từ khung H4 (nhìn như một bước nhảy giá rõ rệt).
2. Trước khi thêm vào danh sách theo dõi chính thức, áp dụng bước kiểm tra bắt buộc: xem lại dữ liệu M15/M5 chi tiết trong giai đoạn đó.
3. Dữ liệu chi tiết cho thấy thực chất có giao dịch liên tục xảy ra trong suốt giai đoạn "gap" nhìn thấy trên H4 — chỉ là các nến M15 di chuyển rất nhanh và mạnh theo một hướng, không có sự đứt gãy giao dịch thật nào.
4. Kết luận: đây là một Liquidity Void / vùng displacement mạnh trong giao dịch liên tục, không phải Vacuum Block đúng nghĩa (không có gap thật, không có "không giao dịch ở giữa").

**Quyết định & lý do:** Loại bỏ nhãn "VB" khỏi vùng giá này, phân loại lại thành Liquidity Void/FVG lớn. Điều này thay đổi cách tiếp cận: thay vì kỳ vọng "gap cần lấp" theo logic VB, xử lý vùng này theo logic FVG/Liquidity Void thông thường — vẫn có thể là POI hợp lý, nhưng cơ sở lý luận về "tại sao giá quay lại" khác nhau (imbalance giao dịch liên tục, không phải khoảng trống không giao dịch).

**Kết quả (theo R):** Không áp dụng trực tiếp — đây là một case về phân loại đúng khái niệm hơn là một giao dịch cụ thể, nhưng việc phân loại đúng giúp tránh áp dụng sai kỳ vọng (ví dụ kỳ vọng sai về độ tin cậy magnet dựa trên nhầm lẫn nguồn gốc).

**Bài học rút ra:** Sự khác biệt giữa VB và Liquidity Void/FVG lớn đôi khi không rõ ràng chỉ nhìn trên một khung thời gian duy nhất (đặc biệt khung cao như H4/D1 có thể "nén" nhiều nến M15/M5 lại trông giống một bước nhảy giá). Luôn xác minh bằng dữ liệu khung thấp hơn trước khi kết luận đó là gap thật — đúng theo nguyên tắc "Điều kiện bắt buộc" đã nêu ở mục 3 phần gốc ("Có gap thật — không phải dải nến liên tục").

---

## D. Edge cases & kinh nghiệm live/backtest

1. **Hiện tượng: dữ liệu từ hai broker khác nhau hiển thị range gap khác nhau cho cùng một VB.** Vì sao: mỗi broker/nguồn dữ liệu có thể có giá đóng/mở cửa phiên hơi khác nhau do chênh lệch feed thanh khoản (đặc biệt rõ trên forex, nơi không có một sàn giao dịch trung tâm duy nhất). Cách sửa: khi backtest hoặc phân tích quan trọng, thống nhất dùng một nguồn dữ liệu duy nhất xuyên suốt, và khi giao dịch live, ưu tiên dữ liệu từ chính broker/nền tảng sẽ đặt lệnh thật thay vì tham chiếu chéo nhiều nguồn.

2. **Hiện tượng: một VB "biến mất" trên chart sau khi phần mềm/nền tảng vẽ lại dữ liệu lịch sử (data revision).** Vì sao: một số nhà cung cấp dữ liệu occasionally điều chỉnh lại dữ liệu lịch sử (sửa lỗi feed, đồng bộ lại giá đóng/mở phiên) khiến một gap từng thấy trên chart không còn xuất hiện y hệt khi tải lại dữ liệu cũ. Cách sửa: chụp ảnh màn hình hoặc ghi log chi tiết (mức giá cụ thể) ngay khi phát hiện VB quan trọng, không hoàn toàn phụ thuộc vào việc chart sẽ luôn hiển thị y hệt trong tương lai.

3. **Hiện tượng: VB hình thành đúng vào thời điểm chuyển đổi giờ mùa (DST — daylight saving time) giữa các khu vực.** Vì sao: khi Mỹ và châu Âu chuyển đổi DST vào các thời điểm khác nhau trong năm (thường lệch nhau 1-2 tuần), giờ mở/đóng phiên tính theo giờ địa phương của trader có thể tạm thời lệch so với thói quen thông thường, dễ khiến việc xác định "đúng mép gap phiên" bị nhầm lẫn trong giai đoạn chuyển đổi. Cách sửa: trong 2 tuần quanh các đợt chuyển DST (tháng 3 và tháng 11 theo lịch Mỹ/châu Âu), kiểm tra kỹ lại giờ phiên thực tế trên nền tảng giao dịch thay vì dựa vào thói quen giờ cũ.

4. **Hiện tượng: một VB unfilled tồn tại rất lâu (nhiều tháng) rồi bất ngờ được lấp đầy hoàn toàn chỉ trong một phiên duy nhất.** Vì sao: điều này thường xảy ra khi có một sự kiện vĩ mô lớn đảo ngược hoàn toàn câu chuyện cơ bản đã tạo ra gap ban đầu (ví dụ thay đổi đột ngột trong kỳ vọng chính sách tiền tệ) — khi đó thị trường "dọn sạch" nhiều tầng inefficiency tích lũy cùng lúc. Cách sửa: không loại bỏ hoàn toàn các VB cũ khỏi danh sách theo dõi dài hạn chỉ vì chúng đã "quá tuổi" theo mốc IPDA 60 ngày — hạ ưu tiên là hợp lý, nhưng vẫn nên giữ trong một danh sách tham chiếu phụ để không bị bất ngờ hoàn toàn khi nó được lấp.

5. **Hiện tượng: nhầm lẫn giữa VB và một cú "spike" dữ liệu lỗi (bad tick/data glitch) từ broker.** Vì sao: đôi khi một broker gặp lỗi feed tạm thời tạo ra một nến có wick cực đoan không phản ánh giao dịch thật trên thị trường rộng — nếu vô tình đọc đây là một gap/VB, toàn bộ phân tích sau đó dựa trên dữ liệu sai. Cách sửa: đối chiếu bất kỳ gap/spike bất thường nào với ít nhất một nguồn dữ liệu độc lập thứ hai (một broker khác, hoặc dữ liệu chỉ số tương quan) trước khi coi đó là VB hợp lệ để phân tích.

6. **Hiện tượng: trên các cặp tiền tệ liên quan tới ngân hàng trung ương có chính sách neo tỷ giá hoặc can thiệp mạnh, gap có thể phản ánh quyết định chính sách chứ không phải "đứt gãy giao dịch tự nhiên".** Vì sao: một gap xảy ra ngay sau công bố chính sách tiền tệ bất ngờ (ví dụ thay đổi biên độ dao động cho phép) có nguồn gốc hoàn toàn khác so với gap tự nhiên do thanh khoản cuối tuần — độ tin cậy của "magnet" trong trường hợp này thấp hơn nhiều vì đây là một sự thay đổi giá trị có chủ đích từ nhà điều hành chính sách. Cách sửa: khi phát hiện VB xảy ra ngay sau một sự kiện chính sách tiền tệ quan trọng, hạ mạnh mức ưu tiên coi đây là magnet đáng tin, và tăng cường theo dõi tin tức liên quan trước khi ra quyết định.

7. **Hiện tượng: khi backtest thủ công, trader vô tình chỉ chọn các VB "dễ thấy, đẹp mắt" trên chart mà bỏ qua các VB nhỏ hơn hoặc khó nhận diện hơn.** Vì sao: đây là một dạng selection bias trong quá trình tự backtest — mắt người có xu hướng chú ý tới các gap lớn, rõ ràng trước, tạo ra một mẫu backtest thiên vị về phía "case đẹp" mà bỏ sót các case mờ nhạt (thường có tỷ lệ thành công thấp hơn). Cách sửa: thiết lập tiêu chí định lượng rõ ràng (ví dụ ngưỡng ATR tối thiểu đã nêu ở mục A3) và cố gắng quét *toàn bộ* các gap thỏa tiêu chí trong một giai đoạn thời gian xác định trước, không chỉ chọn lọc theo cảm giác.

8. **Hiện tượng: VB trên các hợp đồng futures bị ảnh hưởng bởi hiện tượng "rollover" (chuyển hợp đồng) tạo ra gap giả không liên quan gì tới cung cầu thật.** Vì sao: khi hợp đồng futures tháng gần đáo hạn chuyển sang hợp đồng tháng tiếp theo, sự chênh lệch giá cơ bản giữa hai hợp đồng (do basis/carry cost) có thể tạo ra một "gap" trên biểu đồ liên tục (continuous chart) nếu nền tảng không điều chỉnh (back-adjust) đúng cách. Cách sửa: luôn xác nhận biểu đồ đang dùng đã được điều chỉnh rollover đúng cách trước khi đánh dấu VB trên hợp đồng futures, đặc biệt quanh các ngày đáo hạn hợp đồng theo lịch quý.

9. **Hiện tượng: trong giai đoạn thị trường đóng cửa kéo dài bất thường (ví dụ ngày lễ lớn nhiều ngày liên tiếp), gap hình thành lớn hơn bình thường và dễ bị đánh giá quá mức về độ quan trọng.** Vì sao: gap tỷ lệ thuận với thời gian thị trường đóng cửa — một gap sau kỳ nghỉ lễ 3-4 ngày tự nhiên sẽ lớn hơn một gap cuối tuần thông thường mà không nhất thiết phản ánh nhiều thông tin cơ bản hơn, chỉ đơn giản là tích lũy nhiều thời gian không giao dịch hơn. Cách sửa: khi đánh giá độ "quan trọng" của một VB, cân nhắc luôn cả yếu tố thời gian thị trường đã đóng cửa, không chỉ nhìn độ rộng tuyệt đối của gap.

10. **Hiện tượng: một VB được coi là "confluence" với một Order Block chỉ vì chúng ở gần nhau trên chart, dù về bản chất order-flow chúng không liên quan.** Vì sao: sự trùng hợp vị trí không đồng nghĩa với sự củng cố lẫn nhau về mặt cơ chế — một OB hình thành từ hoạt động giao dịch tổ chức trong khi VB hình thành từ khoảng trống *không* giao dịch; việc coi hai loại cấu trúc khác bản chất là "củng cố nhau" chỉ vì gần nhau về giá có thể là ngộ nhận. Cách sửa: khi đánh giá confluence, ưu tiên các trường hợp có mối liên hệ logic rõ ràng (ví dụ OB hình thành ngay trước khi giá tạo ra displacement gây gap) hơn là chỉ dựa vào khoảng cách giá gần nhau ngẫu nhiên.

11. **Hiện tượng: trên khung thời gian rất nhỏ (M1), gần như luôn có thể tìm thấy một "khoảng trống nhỏ" nào đó giữa các nến nếu nhìn đủ kỹ, dẫn tới việc lạm dụng khái niệm VB ở quy mô không có ý nghĩa cấu trúc.** Vì sao: ở khung M1, biến động giá tự nhiên đôi khi tạo ra các khoảng trống rất nhỏ giữa close nến này và open nến kế do độ trễ khớp lệnh — những khoảng trống này không phản ánh một "đứt gãy giao dịch" có ý nghĩa cấu trúc thật như gap phiên/tin tức/cuối tuần. Cách sửa: giới hạn việc áp dụng khái niệm VB cho các khung từ H1 trở lên (theo đúng bảng "so sánh dấu hiệu nhận diện theo khung" ở phần gốc), không cố gắng tìm VB "chính danh" trên M1/M5.

12. **Hiện tượng: khi nhiều VB nhỏ chồng lấp gần nhau tạo thành một "vùng nhiễu", trader dễ tốn quá nhiều thời gian phân tích chi tiết từng VB con thay vì nhìn bức tranh tổng thể.** Vì sao: chi tiết hoá quá mức (analysis paralysis) trên một vùng có nhiều cấu trúc nhỏ chồng chéo có thể khiến trader bỏ lỡ thời điểm hành động thực tế vì mải phân tích. Cách sửa: áp dụng đúng nguyên tắc đã nêu ở phần gốc (coi cả dải là một vùng tổng hợp, chỉ quan tâm VB con gần giá nhất), giới hạn thời gian phân tích chi tiết cho mỗi vùng nhiễu để tránh phân tích quá đà.

13. **Hiện tượng: backtest hồi cứu VB trên dữ liệu quá khứ có xu hướng "tự động" bỏ qua các case gap không rebalance vì chúng không tạo ra một pattern thú vị để ghi chú lại.** Vì sao: đây là hình thức selection bias khác — khi lướt qua chart lịch sử tìm case để học, não bộ tự nhiên chú ý và ghi nhớ các case "đẹp" (rebalance rõ ràng, phản ứng sạch) nhiều hơn các case gap chỉ đơn giản "biến mất" vào một xu hướng dài mà không bao giờ quay lại. Cách sửa: khi liệt kê danh sách VB để học/backtest, đánh số toàn bộ VB xuất hiện trong một khung thời gian cố định (ví dụ toàn bộ NWOG trong 6 tháng gần nhất) thay vì chỉ chọn lọc theo trí nhớ các case ấn tượng.

**Bảng tín hiệu cảnh báo sớm → hành động:**

| Tín hiệu cảnh báo sớm | Hành động ngay |
|---|---|
| Hai nguồn dữ liệu hiển thị range gap khác nhau | Thống nhất một nguồn dữ liệu duy nhất, ưu tiên nguồn của broker sẽ đặt lệnh thật |
| VB hình thành ngay sau công bố chính sách tiền tệ/can thiệp tỷ giá | Hạ mạnh mức tin cậy magnet, theo dõi tin tức tiếp theo trước khi hành động |
| Gap nghi ngờ chỉ xuất hiện trên biểu đồ liên tục futures quanh ngày đáo hạn hợp đồng | Kiểm tra xem chart đã back-adjust rollover đúng cách chưa trước khi tin vào gap |
| VB rất nhỏ chỉ thấy rõ trên M1/M5 | Không coi là VB chính danh — khả năng cao là nhiễu vi cấu trúc, không phải gap cấu trúc thật |
| Danh sách case học tập toàn là case "đẹp", không có case gap không rebalance | Bổ sung quét toàn bộ VB trong một giai đoạn cố định, không chỉ chọn lọc theo trí nhớ |

### Flashcards bổ sung — phần 2

- **DDQ1:** Vì sao CE (50%) được coi là ngưỡng phản ứng quan trọng hơn việc lấp toàn bộ range gap?
  → DDA1: Vì về mặt thống kê, trung điểm dải giá là ước lượng hợp lý nhất cho "giá trị công bằng tạm thời" khi không có thêm thông tin thiên vị về phía nào — khi giá chạm vùng xác suất cao nhất này, động lực đẩy tiếp tục xuyên hết dải giảm đi đáng kể.
- **DDQ2:** Sự khác biệt cốt lõi giữa Vacuum Block và Liquidity Void/FVG là gì, và vì sao dễ nhầm lẫn trên khung thời gian cao?
  → DDA2: VB sinh từ đứt gãy giao dịch thật (không có lệnh khớp ở giữa), còn Liquidity Void/FVG sinh từ displacement mạnh trong giao dịch liên tục (vẫn có giao dịch, chỉ là lệch/imbalance). Dễ nhầm trên khung cao vì nhiều nến chạy nhanh liên tiếp trên khung thấp có thể "nén" lại trông giống một bước nhảy giá khi xem trên khung H4/D1.
- **DDQ3:** Vì sao gap tin tức (news-gap) có xác suất "không rebalance" cao hơn session-gap thông thường?
  → DDA3: Vì news-gap thường phản ánh thông tin cơ bản thật làm thay đổi kỳ vọng giá trị một cách bền vững (displacement thật), trong khi session-gap chủ yếu là hệ quả thanh khoản gián đoạn thuần túy không có thay đổi giá trị cơ bản đi kèm.
- **DDQ4:** Tại sao không nên gộp chung dữ liệu backtest của NQ1, EURUSD/GBPUSD và XAUUSD khi thống kê hiệu suất VB?
  → DDA4: Vì cơ chế sinh gap khác nhau căn bản giữa ba loại thị trường (session gap phiên đóng/mở với index, NWOG cuối tuần với forex, gap tin tức với vàng) — hành vi rebalance đặc thù của từng nhóm sẽ bị pha loãng/che lấp nếu gộp chung thành một con số thống kê duy nhất.

> [!tip] Checklist tự kiểm tra trước khi tin vào một VB
> - Đã xác nhận đây là gap thật (kiểm tra dữ liệu khung thấp hơn), không phải displacement liên tục bị nhầm?
> - Đã phân loại đúng nguồn gốc (session/weekend/news) và áp dụng mức độ tin cậy tương ứng?
> - Đã kiểm tra tuổi VB so với mốc IPDA 20/40/60 ngày?
> - Đã có kế hoạch chờ xác nhận sweep + displacement/MSS, không vào lệnh chỉ vì "giá đang test gap"?
> - Nếu là news-gap: đã chờ spread/biến động ổn định và đánh giá khả năng đây là displacement thật chưa?

### D bổ sung — Rủi ro khi coi mọi VB "unfilled cũ" là cơ hội chờ đợi vô thời hạn

14. **Hiện tượng: trader giữ một danh sách quá dài các VB "unfilled" từ nhiều tháng/năm trước và liên tục chờ đợi chúng được lấp, gây phân tán sự chú ý khỏi các cơ hội hiện tại.** Vì sao: theo nguyên tắc IPDA, một VB càng cũ càng mất dần độ ưu tiên trong "chu kỳ tra cứu" hiện tại của thuật toán định giá — việc giữ mãi một danh sách dài các VB quá hạn ưu tiên trong tâm trí có thể khiến trader liên tục tìm cách "ép" các setup không thật sự liên quan tới bối cảnh giá hiện tại vào các mức cũ này. **Cách xử lý:** định kỳ (ví dụ hàng tháng) rà soát và loại bỏ khỏi danh sách theo dõi chính các VB đã vượt quá xa mốc 60 ngày mà không có dấu hiệu giá tiếp cận, chỉ giữ chúng trong một danh sách tham chiếu phụ không ảnh hưởng tới quyết định giao dịch hằng ngày.

15. **Hiện tượng: một VB unfilled nằm rất xa so với giá hiện tại (ví dụ hàng trăm pip/điểm) khiến trader phóng đại tầm quan trọng của nó như một "target chắc chắn" trong khi thực tế còn rất nhiều cấu trúc thị trường sẽ hình thành trước khi giá tới đó.** Vì sao: giữa thời điểm hiện tại và khi giá (nếu có) tới được VB xa, thị trường có thể trải qua nhiều thay đổi bias, hình thành liquidity pool mới, hoặc thậm chí đảo chiều hoàn toàn xu hướng — coi một VB xa như "chắc chắn sẽ đạt tới" bỏ qua toàn bộ tính bất định này. **Cách xử lý:** chỉ coi VB xa là một "điểm tham chiếu dài hạn" trong bức tranh tổng thể, không xây dựng kế hoạch giao dịch cụ thể (entry/SL/TP) dựa trên nó cho tới khi giá thực sự tiến gần và có xác nhận cấu trúc mới ủng hộ hướng đi đó.

**Bảng tín hiệu cảnh báo sớm → hành động (bổ sung):**

| Tín hiệu cảnh báo sớm | Hành động ngay |
|---|---|
| Danh sách VB unfilled theo dõi dài hơn vài chục mục, phần lớn đã quá 60 ngày tuổi | Rà soát định kỳ, chuyển các VB quá hạn ưu tiên sang danh sách tham chiếu phụ |
| Coi một VB xa hàng trăm điểm là "target chắc chắn" để lên kế hoạch giao dịch ngay | Chỉ coi là tham chiếu dài hạn, chờ giá tiến gần và có xác nhận cấu trúc mới trước khi lập kế hoạch cụ thể |

### Tóm tắt phần Deep Dive

Vacuum Block là một công cụ tổ chức thông tin có cơ sở hợp lý cả về order-flow (thanh khoản residual tập trung ở vùng có giao dịch trước đó, không tồn tại trong dải gap) lẫn về lý thuyết đấu giá cổ điển (Market Profile/Auction Market Theory với khái niệm gap-fill/single-print tương đồng) — nhưng giá trị thực chỉ phát huy khi kết hợp chặt chẽ với: (1) phân loại đúng nguồn gốc gap (session/weekend/news) vì mỗi loại có xác suất rebalance khác nhau về bản chất, (2) xác nhận order-flow (sweep + displacement/MSS) trước khi hành động thay vì dự đoán trước, (3) backtest cá nhân có kiểm soát biến số rõ ràng, phân tách theo thị trường và loại gap, để tự đánh giá độ tin cậy thực tế thay vì tin vào một quy luật phổ quát chưa có bằng chứng học thuật xác nhận riêng.

**Liên kết liên quan:** xem thêm [[32-Top-down-Analysis-Multiple-Timeframes]] cho nguyên tắc xác định VB ở khung lớn trước khi tìm entry ở khung nhỏ (đúng tinh thần top-down), và [[33-Turtle-Soup]] để phân biệt rõ giữa việc "gap bị lấp do rebalance tự nhiên" và một "sweep thanh khoản" xảy ra tại vùng gap — hai hiện tượng có thể trông giống nhau trên chart nhưng khác nhau về cơ chế order-flow đằng sau.

*(Hết phần Deep Dive — File 34: Vacuum Block)*

### Ghi chú phương pháp

> [!note] Ghi chú phương pháp
> Toàn bộ mức giá, tỷ lệ phần trăm, và ví dụ số trong phần Deep Dive này (R-multiple, số ngày, mốc ATR) chỉ mang tính minh hoạ nguyên tắc trình bày, không phải số liệu thống kê hay lịch sử giá thực tế đã được xác minh qua nghiên cứu độc lập. Case thị trường thật (gap dầu WTI liên quan địa chính trị) được mô tả hoàn toàn định tính, không trích dẫn mức giá hay ngày tháng cụ thể, theo đúng yêu cầu không bịa số liệu lịch sử chính xác. Trước khi tin tưởng bất kỳ con số nào cho quyết định giao dịch thật, cần tự backtest trên dữ liệu và điều kiện giao dịch của chính mình, theo đúng khung biến số đã đề xuất ở mục A3.

### Câu hỏi mở rộng để tự kiểm tra hiểu sâu (bổ sung ngoài mục 11 gốc)

- Nếu hai VB (một session-gap trên NQ1, một NWOG trên EURUSD) có cùng kích thước tương đối (theo % ATR), liệu chúng có nên được gán cùng một mức độ tin cậy magnet? Vì sao có/không?
- Một VB unfilled 90 ngày tuổi (ngoài mốc IPDA 60 ngày) đột nhiên có giá tiến gần trở lại — nên xử lý ra sao so với một VB unfilled 10 ngày tuổi trong cùng tình huống?
- Nếu backtest cho thấy setup "sweep + displacement tại CE của VB" và setup "sweep + displacement tại một mức hỗ trợ/kháng cự ngẫu nhiên" có tỷ lệ thắng gần như nhau, điều đó nói gì về giá trị gia tăng thực sự của riêng khái niệm VB?
- Vì sao việc phân loại đúng nguồn gốc gap (session/weekend/news) quan trọng hơn việc chỉ đo kích thước gap khi đánh giá độ tin cậy magnet?

### Lưu ý cuối về giới hạn của phần Deep Dive này

Phần mở rộng này được xây dựng hoàn toàn từ kiến thức và kinh nghiệm thực chiến hiện có, không tra cứu thêm dữ liệu hoặc nghiên cứu mới trong quá trình viết — vì vậy các tuyên bố về "góc nhìn phi-ICT" (Market Profile, Auction Market Theory) và các so sánh định lượng chỉ nên được coi là khung tham khảo ban đầu để trader tự tìm hiểu sâu hơn, không phải một tổng hợp học thuật đầy đủ về các lĩnh vực đó. Đặc biệt, khái niệm "half-life của inefficiency" (mục A8) là một cách diễn giải cá nhân mượn ngôn ngữ thống kê để giải thích trực giác thực chiến quen thuộc trong cộng đồng ICT (nguyên tắc IPDA 20/40/60 ngày), không phải một mô hình thống kê đã được kiểm định chính thức trong tài liệu ICT gốc.

---

*(Kết thúc toàn bộ phần Deep Dive của file 34 — Vacuum Block.)*

### Flashcard cuối

- **DDQ5:** Vì sao thiếu một ngưỡng khách quan thống nhất cho "gap đủ lớn để tính là VB" là một giới hạn quan trọng của khung phân tích này?
  → DDA5: Vì nó khiến kết quả backtest giữa các trader khác nhau khó so sánh trực tiếp — hai người backtest cùng dữ liệu có thể đưa ra danh sách VB khác nhau tuỳ ngưỡng tự đặt, và bản thân điều này cũng làm giảm tính "khoa học" thuần tuý của khái niệm so với một chỉ báo toán học rõ ràng.
- **DDQ6:** Làm sao nhận biết một quyết định vào lệnh có thực sự dựa trên VB hay chỉ đang dùng VB để hợp lý hoá một ý định đã có sẵn?
  → DDA6: Tự hỏi liệu quyết định có thay đổi không nếu bỏ hoàn toàn yếu tố VB ra khỏi lý luận — nếu vẫn muốn vào lệnh vì lý do khác, VB không phải cơ sở thật của quyết định và cần xem lại toàn bộ logic.

> [!tip] Ba câu hỏi nhanh trước khi tin vào một Vacuum Block
> - Gap này có được xác nhận là "gap thật" qua dữ liệu khung thấp hơn không, hay chỉ là ấn tượng từ khung cao?
> - Nếu bỏ yếu tố "đây là VB" ra khỏi lý luận, tôi còn muốn vào lệnh này không?
> - Tôi đã phân loại đúng nguồn gốc (session/weekend/news) và áp dụng đúng mức độ tin cậy tương ứng chưa?

---

**Kết luận chung của phần Deep Dive:** Vacuum Block là công cụ tổ chức thông tin hữu ích, có cơ sở hợp lý về order-flow và tương đồng với các trường phái phân tích cổ điển khác (Market Profile), nhưng không phải một quy luật tất định — giá trị thực tế phụ thuộc vào kỷ luật phân loại nguồn gốc, chờ xác nhận, và backtest cá nhân có kiểm soát biến số rõ ràng.

### Gợi ý lộ trình thực hành sau khi đọc phần Deep Dive này

1. Áp dụng ngưỡng ATR tối thiểu (mục A3) để quét lại 20-30 VB lịch sử trên D1/H4 của một thị trường quen thuộc, phân loại theo nguồn gốc (session/weekend/news).
2. Ghi log đầy đủ theo mẫu đã đề xuất (mục A10 + Best Practices gốc), bao gồm giả thuyết ban đầu trước khi biết kết quả.
3. Sau khi có ≥20 mẫu mỗi loại, tự vẽ đường cong tần suất rebalance theo tuổi VB (mục A8) để có cái nhìn định lượng riêng, thay vì dựa vào cảm giác chủ quan.
4. So sánh tỷ lệ thắng của setup "sweep+displacement tại CE của VB" với setup tương tự tại mức hỗ trợ/kháng cự không liên quan gap, theo đúng gợi ý kiểm chứng ở phần B, để tự đánh giá giá trị gia tăng thực sự của khái niệm này trong hệ thống giao dịch cá nhân.

> [!info] Ghi chú khép lại
> Không có khái niệm PD Array nào trong ICT (bao gồm Vacuum Block) nên được dùng như một tín hiệu độc lập, tự đủ để ra quyết định. Giá trị lớn nhất của VB là cung cấp một danh sách vùng giá cần chú ý một cách khách quan, có cấu trúc — quyết định thực tế vẫn phải đi qua đầy đủ chuỗi xác nhận order-flow (sweep, displacement, MSS) và quản lý rủi ro nhất quán, đúng như tinh thần toàn bộ hệ thống ICT 2022 Model đã mô tả ở phần gốc của tài liệu này.

### Đối chiếu nhanh: khi nào nên tin VB, khi nào nên nghi ngờ VB

| Tình huống | Mức độ tin cậy gợi ý | Lý do |
|---|---|---|
| Session-gap quanh mở cửa RTH của index, có confluence với OB/FVG cùng hướng bias | Cao | Thanh khoản sâu quay lại nhanh, có xác nhận đa lớp |
| NWOG sau một tuần không có tin vĩ mô lớn | Trung bình–cao | Gap thuần thanh khoản cuối tuần, ít nhiễu thông tin cơ bản |
| News-gap sau dữ liệu vĩ mô tác động mạnh, bền vững (đổi kỳ vọng chính sách) | Thấp cho kỳ vọng rebalance nhanh | Khả năng cao là displacement thật, không phải gap chờ lấp thông thường |
| Gap nhìn thấy trên H4/D1 nhưng chưa xác minh bằng dữ liệu M15/M5 | Thấp (chưa xác minh) | Có thể chỉ là displacement liên tục bị nhầm thành gap thật |
| VB đã quá 60 ngày tuổi, không nằm trong lookback IPDA hiện tại | Thấp, chỉ dùng tham chiếu phụ | Mất dần độ ưu tiên trong chu kỳ tra cứu thuật toán định giá hiện tại |

*(Hết toàn bộ phần Deep Dive của file 34.)*




