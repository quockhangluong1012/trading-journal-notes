---
type: ict-concept
concept: "Forex/CFD Basics — Pip, Lot, Spread, Swap, Leverage, Margin"
aliases:
  - Pip
  - Lot
  - Spread
  - Swap
  - Rollover
  - Leverage
  - Margin
  - Đòn bẩy
  - Ký quỹ
tags:
  - trading/ict/concept
  - trading/study
  - trading/foundation
  - trading/risk
status: developing # seed | developing | tested | mastered
category: "Risk Management"
last_reviewed: 
created: 2026-07-01
updated: 2026-07-03
common_mistakes:
  - "Nhầm 1 lot với 1 đơn vị tài sản"
  - "Tính size theo cảm tính thay vì theo pip value và stop loss"
  - "Coi đòn bẩy là 'sức mua miễn phí' thay vì công cụ khuếch đại rủi ro"
---

# Forex/CFD Basics — Pip, Lot, Spread, Swap, Leverage, Margin

> [!summary] Tóm tắt 1 câu
> Đây là 6 "đơn vị đo" nền tảng của thị trường Forex/CFD: **pip** đo mức biến động giá, **lot** đo khối lượng lệnh, **spread** là chi phí vào lệnh, **swap** là chi phí giữ lệnh qua đêm, còn **leverage/margin** quyết định bạn cần bao nhiêu tiền để mở một vị thế — hiểu đúng cả 6 mới tính được **position size** và **rủi ro ≤0.5%** một cách chính xác.

> [!info] Vì sao note này quan trọng với lộ trình Prop Firm
> Bài thi prop firm không thắng/thua bằng việc bạn đoán đúng hướng, mà bằng việc bạn **kiểm soát rủi ro và drawdown**. Muốn kiểm soát rủi ro, bạn phải dịch được một ý tưởng ICT ("vào Long NAS100, SL dưới order block 30 điểm") thành một con số khối lượng cụ thể. Toàn bộ phép dịch đó nằm ở 6 khái niệm dưới đây. Đây là **kiến thức nền (foundation)**, không phải khái niệm chart như các note ICT khác, nhưng nó là điều kiện tiên quyết để mọi setup ICT có thể áp dụng vào tài khoản thật.

---

## 1. Bức tranh tổng thể — 6 khái niệm gắn với nhau như thế nào

Trước khi đi vào từng khái niệm, hãy nhìn cách chúng liên kết thành một chuỗi logic, vì học rời rạc rất dễ quên:

```text
LOT (khối lượng)  ──►  quyết định "giá trị mỗi pip" (pip value)
PIP (mức biến động)  ──►  nhân với pip value = LỜI/LỖ bằng tiền
STOP LOSS (số pip)  ──►  cùng pip value & rủi ro cho phép = POSITION SIZE

LEVERAGE (đòn bẩy)  ──►  quyết định MARGIN cần để mở lệnh
MARGIN (ký quỹ)  ──►  phần vốn bị "khóa" lại; phần còn lại là free margin
SPREAD + SWAP  ──►  chi phí giao dịch (vào lệnh + giữ lệnh qua đêm)
```

Một cách ghi nhớ ngắn gọn: **Lot + Pip** trả lời câu hỏi *"lệnh này lời/lỗ bao nhiêu tiền?"*; **Leverage + Margin** trả lời *"tôi cần bao nhiêu vốn để mở lệnh và còn dư bao nhiêu?"*; **Spread + Swap** trả lời *"giao dịch này tốn phí gì?"*.

---

## 2. PIP — Đơn vị đo biến động giá

### Định nghĩa
**Pip** (viết tắt của *Percentage in Point* hoặc *Price Interest Point*) là đơn vị chuẩn nhỏ nhất dùng để đo mức thay đổi giá của một cặp tiền tệ theo quy ước. Nó cho phép mọi người nói về biến động giá bằng một con số dễ so sánh, thay vì đọc từng chữ số thập phân.

- Với **đa số cặp tiền** (EURUSD, GBPUSD, AUDUSD...): 1 pip = **0.0001** (chữ số thập phân thứ 4). Ví dụ EURUSD đi từ 1.0850 → 1.0851 là tăng **1 pip**.
- Với các cặp có **JPY** (USDJPY, EURJPY...): 1 pip = **0.01** (chữ số thập phân thứ 2), vì yên có giá trị nhỏ. Ví dụ USDJPY 156.20 → 156.21 là 1 pip.

### Pipette (điểm thập phân thứ 5)
Broker hiện đại báo giá thêm 1 chữ số nữa: EURUSD hiển thị **1.08505**. Chữ số cuối này gọi là **pipette** (1/10 pip). Nên đừng nhầm: 1.08500 → 1.08510 mới là 1 pip đầy đủ.

### Với Vàng (XAUUSD) và chỉ số (NAS100) — cẩn thận
Đây là chỗ hầu hết người mới nhầm, và rất quan trọng vì bạn giao dịch chính XAUUSD và NAS100:

- **XAUUSD**: quy ước "pip" không thống nhất giữa các broker. Nhiều nơi coi **1 pip = 0.10 USD** hoặc **0.01 USD**. Cách an toàn hơn là **bỏ khái niệm pip đi và tư duy theo "biến động 1 USD giá vàng"**. Ví dụ vàng đi từ 2350.00 → 2351.00 là biến động **1 USD** (100 pip nếu 1 pip = 0.01).
- **NAS100 (NDX / US100)**: đo bằng **điểm chỉ số (index point)**, không phải pip. Ví dụ NAS100 đi từ 20000.0 → 20001.0 là **1 điểm**.

> [!tip] Quy tắc thực chiến
> Với vàng và chỉ số, **đừng nói chuyện bằng pip**. Hãy nói bằng "**biến động bao nhiêu USD giá vàng**" hoặc "**bao nhiêu điểm chỉ số**", rồi nhân với giá trị mỗi USD/mỗi điểm cho khối lượng bạn định vào. Điều này loại bỏ 90% nhầm lẫn.

![[ForexBasics-Pip-Pipette-Comparison.png]]
> *Minh hoạ (cần tự vẽ/chụp lại): một sơ đồ 4 cột đặt cạnh nhau — (1) EURUSD với vị trí thập phân thứ 4 = pip và thứ 5 = pipette được khoanh tròn, (2) USDJPY với vị trí thập phân thứ 2 = pip, (3) XAUUSD với quy ước "1 pip = 0.01 hay 0.10 USD tuỳ broker" và gợi ý dùng "biến động USD" thay vì pip, (4) NAS100 với đơn vị "điểm chỉ số" thay vì pip. Đây là ảnh minh hoạ khái niệm để tự vẽ (Excalidraw/PowerPoint) hoặc chụp màn hình bảng giá thật từ nền tảng broker của bạn — không phải số liệu tài khoản thật.*

### Advanced — Đặt Stop Loss theo biến động (ATR) thay vì số pip cố định

Một sai lầm phổ biến ở trình độ trung cấp là dùng **một con số SL cố định** (ví dụ "luôn SL 20 pip" hoặc "luôn SL 50 điểm NAS100") cho mọi phiên, mọi chế độ thị trường (market regime). Vấn đề: **biến động (volatility) không cố định** — NAS100 trong phiên tin NFP có thể dao động gấp 3-4 lần một phiên Á trầm lắng. SL cố định khiến bạn:

- **Quá chật (too tight)** trong phiên biến động cao → bị quét bởi nhiễu thị trường bình thường, không phải vì setup sai.
- **Quá rộng (too loose)** trong phiên biến động thấp → risk:reward xấu đi không cần thiết, hoặc size bị giảm quá mức so với biên độ thực tế của cấu trúc.

**Giải pháp chuyên nghiệp: SL theo ATR (Average True Range).** ATR đo biến động trung bình trong N nến gần nhất (thường 14) và được quy đổi trực tiếp sang đơn vị bạn cần:

```text
SL (pip) = ATR(14) trên khung entry × hệ số nhân (thường 1.0 – 1.5)
SL (USD vàng) = ATR(14) của XAUUSD (tính bằng USD) × hệ số nhân
SL (điểm NAS100) = ATR(14) của NAS100 (tính bằng điểm) × hệ số nhân
```

Ví dụ minh hoạ: nếu ATR(14) trên M15 của NAS100 hôm nay là 45 điểm (phiên biến động cao) so với 18 điểm hôm qua (phiên trầm lắng), một SL cố định "30 điểm" sẽ **quá chật hôm nay** (dễ bị quét trước khi giá đi đúng hướng) và **quá rộng hôm qua** (risk:reward kém so với biên độ thực tế). Dùng SL = 1.2 × ATR sẽ tự động co giãn theo chế độ thị trường: ~54 điểm hôm nay, ~22 điểm hôm qua.

> [!tip] Vì sao điều này quan trọng hơn một "con số pip đẹp"
> ATR không thay thế cấu trúc ICT (order block, FVG, liquidity sweep) để đặt SL — SL vẫn phải đặt sau/dưới điểm cấu trúc hợp lệ. Nhưng ATR là **bộ lọc kiểm tra**: nếu SL cấu trúc của bạn nhỏ hơn nhiều so với ATR hiện tại của phiên, khả năng cao nó sẽ bị quét bởi nhiễu bình thường chứ không phải vì setup sai — cân nhắc khung thời gian entry lớn hơn hoặc chờ biến động giảm. Ngược lại nếu SL cấu trúc lớn hơn nhiều lần ATR, position size sẽ tự động nhỏ lại theo công thức ở mục 9, bảo vệ bạn khỏi rủi ro vượt mức trong phiên biến động thấp bất thường.

---

## 3. LOT — Đơn vị đo khối lượng lệnh

### Định nghĩa
**Lot** là đơn vị chuẩn hóa khối lượng giao dịch. Bạn không mua "10.000 euro", bạn mua "0.1 lot EURUSD" — hệ thống tự hiểu con số đơn vị đằng sau.

Với Forex, 1 standard lot = **100.000 đơn vị tiền cơ sở** (base currency). Ba cỡ lot phổ biến:

| Loại lot | Ký hiệu khối lượng | Số đơn vị (Forex) | Pip value (cặp có USD là đồng yết giá) |
|---|---:|---:|---:|
| **Standard lot** | 1.00 | 100.000 | **$10 / pip** |
| **Mini lot** | 0.10 | 10.000 | **$1 / pip** |
| **Micro lot** | 0.01 | 1.000 | **$0.10 / pip** |
| Nano lot (ít broker) | 0.001 | 100 | $0.01 / pip |

### Công thức Pip Value (giá trị mỗi pip)
Đây là công thức bạn phải thuộc lòng vì nó là cầu nối giữa "số pip" và "số tiền":

```text
Pip Value = (Kích thước 1 pip) × (Số đơn vị của lệnh)
```

**Trường hợp 1 — cặp có USD là đồng yết giá (quote), ví dụ EUR/USD, GBP/USD:**
Pip value **cố định** và không phụ thuộc tỷ giá (vì lời/lỗ đã tính sẵn bằng USD):
- 1 lot EURUSD: 0.0001 × 100.000 = **$10 / pip** *(đã kiểm chứng bằng code)*
- 0.1 lot: **$1 / pip** — 0.01 lot: **$0.10 / pip**

**Trường hợp 2 — cặp có JPY hoặc USD là đồng cơ sở (USD/JPY, USD/CAD...):**
Pip value thay đổi theo tỷ giá và phải quy đổi về USD. Ví dụ USD/JPY: pip value (USD) = (0.01 × đơn vị) / tỷ_giá_USDJPY.

**Với XAUUSD:** thường 1 standard lot = **100 ounce**. Do đó biến động **1 USD giá vàng = $100 P&L** cho 1 lot (0.1 lot = $10 cho mỗi $1 vàng). *(Kiểm chứng bằng code: 1 USD move × 100 oz = $100.)*

**Với NAS100:** tùy broker, thường **$1 / điểm / 1 lot** (một số broker dùng $0.1 hoặc $20 — **luôn kiểm tra "contract size" trong đặc tả sản phẩm của broker/prop firm trước khi vào lệnh**).

> [!warning] Lỗi kinh điển của người mới
> Nhầm "1 lot" với "1 cổ phiếu / 1 ounce / 1 euro". 1 lot vàng KHÔNG phải 1 ounce mà là **100 ounce** → biến động chỉ $3 giá vàng đã là **$300** cho mỗi lot. Đây là nguyên nhân số một khiến người mới "cháy" tài khoản dù thị trường chỉ nhích nhẹ.

![[ForexBasics-Contract-Specs-Screenshot.png]]
> *Minh hoạ (cần tự chụp lại): screenshot trang "Contract Specifications" / "Đặc tả sản phẩm" thật từ nền tảng broker hoặc prop firm bạn đang dùng (MT4/MT5 → chuột phải vào symbol → Specification, hoặc trang web broker), cho từng symbol EURUSD, GBPUSD, XAUUSD, NAS100. Đây PHẢI là ảnh chụp thật từ tài khoản/nền tảng của bạn — không dùng số liệu suy đoán, vì các con số này khác nhau giữa các broker.*

### Advanced — So sánh đặc tả hợp đồng giữa các thị trường bạn giao dịch

Bảng dưới đây tổng hợp các giá trị **điển hình/tham khảo (typical/example)** để bạn có cảm nhận về thứ tự độ lớn (order of magnitude) khi chuyển đổi giữa các symbol. **Đây KHÔNG phải số liệu chuẩn phổ quát** — XAUUSD và NAS100 đặc biệt khác nhau rất nhiều giữa các broker/prop firm (contract size, pip/point value, minimum lot step đều có thể lệch nhau).

| Symbol | Contract size điển hình (1.0 lot) | Pip/Point value điển hình (1.0 lot) | Minimum lot step điển hình | Ghi chú |
|---|---|---|---|---|
| **EURUSD** | 100.000 EUR | ~$10 / pip | 0.01 lot | Tương đối chuẩn hoá giữa các broker (quote = USD) |
| **GBPUSD** | 100.000 GBP | ~$10 / pip | 0.01 lot | Tương tự EURUSD, nhưng biến động (ATR) thường cao hơn |
| **XAUUSD** | *thường* 100 oz | *thường* ~$1 – $100 / mỗi $1 biến động, tuỳ quy ước "1 lot" của broker | 0.01 lot (một số broker: 0.1 lot) | ⚠️ **Biến thiên rất lớn giữa các broker** — một số quy ước 1 lot = 100 oz, số khác = 10 oz hoặc dùng "mini gold". **Bắt buộc kiểm tra** |
| **NAS100 / NDX** | *thường* $1 – $20 / điểm / lot | Xem cột trước | 0.1 lot hoặc 1.0 lot tuỳ broker | ⚠️ **Biến thiên rất lớn** — CFD chỉ số không có "chuẩn quốc tế" như Forex |

> [!warning] Bắt buộc xác minh trước khi trade — không được suy đoán
> Các con số cho **XAUUSD và NAS100** trong bảng trên chỉ mang tính **ví dụ minh hoạ**, KHÔNG phải số liệu chính thức áp dụng cho mọi broker. Trước khi giao dịch một symbol mới hoặc mở tài khoản prop firm mới, **luôn mở trang "Contract Specification"/"Symbol Information" chính thức của broker/prop firm đó** và xác nhận: (1) contract size, (2) giá trị mỗi pip/point cho 1.0 lot, (3) minimum lot step, (4) minimum/maximum volume. Chỉ một sai lệch nhỏ ở contract size (ví dụ tưởng $1/điểm nhưng thực tế $20/điểm) có thể khiến position size của bạn sai lệch **20 lần** — đủ để vi phạm giới hạn rủi ro 0.5%/lệnh ngay lệnh đầu tiên.

---

## 4. SPREAD — Chi phí vào lệnh (chênh lệch mua/bán)

### Định nghĩa
**Spread** là chênh lệch giữa giá **Bid** (giá bạn bán được) và giá **Ask** (giá bạn mua được). Đây là chi phí giao dịch cơ bản nhất, trả cho broker/nhà cung cấp thanh khoản.

```text
Spread = Ask − Bid
```

Ví dụ EURUSD: Bid = 1.08500, Ask = 1.08512 → spread = 0.00012 = **1.2 pip**.

### Ý nghĩa thực tế
- Khi vừa mở lệnh, bạn **luôn âm bằng đúng spread** (vào Buy ở Ask, giá thị trường tính theo Bid). Bạn phải đi đúng hướng ít nhất bằng spread mới hòa vốn.
- Spread rộng ăn mòn setup có **stop loss/target nhỏ**. Với entry ICT trên M1/M5 (SL sát), spread là yếu tố sống còn.

### Các loại tài khoản
- **Tài khoản spread cố định (fixed):** ít dùng, spread không đổi.
- **Tài khoản spread thả nổi (variable/raw):** spread rất nhỏ (đôi khi 0.0–0.2 pip trên EURUSD) nhưng tính thêm **commission** (hoa hồng, ví dụ $3.5/lot mỗi chiều). Prop firm thường dùng loại này.

> [!tip] Liên hệ ICT & Kill Zone
> Spread **giãn rộng đột ngột** vào lúc tin tức mạnh, lúc mở/đóng phiên, và ngoài giờ thanh khoản cao. Đây là lý do ICT nhấn mạnh giao dịch trong **Kill Zone (London / New York)** — thanh khoản cao thì spread hẹp và ổn định. Tránh vào lệnh ngay thời điểm tin đỏ vì spread có thể nhảy vọt và quét stop.

### Advanced — Tỷ lệ Spread/SL (Spread-to-SL Ratio) và ngưỡng "SL quá chật"

Spread nên được đánh giá **tương đối so với SL**, không phải như một con số tuyệt đối. Một spread 1.2 pip là không đáng kể với SL 30 pip, nhưng là **chi phí khổng lồ** với SL 5 pip.

```text
Spread-to-SL Ratio (%) = (Spread / Khoảng cách SL) × 100%
```

Ví dụ: EURUSD spread trung bình 1.2 pip, SL setup = 8 pip → tỷ lệ = 1.2/8 = **15%**. Nghĩa là chỉ riêng phí spread đã "ăn" 15% rủi ro dự kiến của lệnh trước khi thị trường di chuyển một milimet nào theo hướng bất lợi.

**Quy tắc kinh nghiệm (rule of thumb) để đánh giá SL "quá chật":**

| Spread-to-SL Ratio | Đánh giá | Hành động |
|---|---|---|
| < 10% | An toàn — chi phí spread không đáng kể | Vào lệnh bình thường |
| 10% – 20% | Chấp nhận được, nhưng cần ý thức chi phí | Cân nhắc dùng tài khoản raw spread + commission thay vì spread thả nổi cao |
| 20% – 35% | Cảnh báo — SL đang khá chật so với chi phí | Chỉ vào nếu chắc chắn đang trong Kill Zone thanh khoản cao (spread hẹp nhất); tránh khung giờ tin tức |
| > 35% | Quá chật — không nên vào | Chuyển sang khung thời gian entry cao hơn để có SL cấu trúc rộng hơn, hoặc bỏ qua setup |

> [!warning] Đặc biệt lưu ý với entry M1/M5 kiểu ICT
> Các entry theo mô hình ICT 2022 trên M1/M5 thường có SL rất sát (dưới order block nhỏ, dưới FVG). Đây chính là kiểu setup **dễ bị spread ăn mòn nhất**. Luôn kiểm tra spread trung bình của symbol trong đúng phiên bạn trade (London/New York Kill Zone) trước khi coi một SL là "đủ rộng" — spread ngoài Kill Zone có thể gấp 2-3 lần trong Kill Zone.

---

## 5. SWAP / ROLLOVER — Chi phí (hoặc lãi) giữ lệnh qua đêm

### Định nghĩa
**Swap** (còn gọi là **rollover** hay **phí qua đêm**) là khoản tiền được **cộng hoặc trừ** vào tài khoản khi bạn giữ một vị thế **qua thời điểm 17:00 giờ New York** (kết thúc ngày giao dịch). Nguồn gốc của nó là **chênh lệch lãi suất** giữa hai đồng tiền trong cặp.

- Mỗi cặp tiền là việc bạn **đồng thời vay một đồng và nắm giữ một đồng**. Nếu đồng bạn nắm giữ có lãi suất cao hơn đồng bạn vay → bạn **nhận swap dương**. Ngược lại → **trả swap âm** (phổ biến hơn).
- Với **CFD chỉ số/vàng**, swap phản ánh chi phí tài trợ (financing cost) cho phần đòn bẩy, thường là **âm** cho cả hai chiều Long/Short.

### Quy tắc "Triple Swap" (swap x3)
Vì giao dịch giao ngay (spot) mất 2 ngày để thanh toán, nên **thứ Tư** (Wednesday) thường bị tính **swap gấp 3 lần** để bù cho cuối tuần. Ngày này thay đổi tùy broker — cần kiểm tra.

### Ý nghĩa thực tế với style của bạn
ICT 2022 Model chủ yếu là **intraday / scalp** (vào-ra trong ngày, trong Kill Zone). Nếu bạn đóng lệnh trước 17:00 NY, **swap gần như không ảnh hưởng**. Swap chỉ quan trọng nếu bạn:
- Giữ lệnh **swing qua nhiều ngày** (khi đó phí âm tích lũy có thể ăn mòn lợi nhuận).
- Giao dịch **vàng/chỉ số swing** — phí tài trợ âm khá đáng kể.

> [!note] Với Prop Firm
> Nhiều prop firm **giữ nguyên phí swap** như tài khoản thật; một số có tài khoản "swap-free" (thường cho tài khoản Hồi giáo). Nếu chiến lược của bạn giữ lệnh qua đêm, hãy đọc kỹ điều khoản, vì phí swap tính vào drawdown và có thể khiến bạn vi phạm giới hạn thua lỗ.

---

## 6. LEVERAGE — Đòn bẩy

### Định nghĩa
**Leverage (đòn bẩy)** cho phép bạn kiểm soát một vị thế có **giá trị danh nghĩa (notional value)** lớn hơn nhiều số vốn thực bỏ ra. Nó được biểu thị bằng tỷ lệ như **1:30, 1:100, 1:500**.

- **1:100** nghĩa là mỗi 1 USD vốn của bạn kiểm soát được 100 USD giá trị thị trường.
- Nói cách khác, bạn chỉ cần đặt cọc **1%** giá trị lệnh (phần đặt cọc đó chính là **margin** — xem mục 7).

### Đòn bẩy hoạt động như thế nào — cơ chế chi tiết
Hãy hình dung một ví dụ cụ thể để thấy rõ:

Bạn muốn mua **1 lot EURUSD** ở giá 1.0850.
- **Giá trị danh nghĩa (notional)** = 100.000 × 1.0850 = **$108.500**.
- Nếu **không có đòn bẩy**, bạn cần đủ $108.500 tiền mặt — điều không thực tế với nhà giao dịch cá nhân.
- Với **đòn bẩy 1:100**, bạn chỉ cần ký quỹ **$1.085** (= 108.500 / 100). Broker "cho mượn" phần còn lại. *(Kiểm chứng bằng code.)*
- Với **1:500**, chỉ cần **$217**. Với **1:30** (giới hạn của các cơ quan quản lý như ESMA ở châu Âu cho retail), cần **$3.616**.

Điểm mấu chốt: **đòn bẩy KHÔNG làm thay đổi lời/lỗ của bạn tính bằng tiền**. Lời/lỗ luôn được quyết định bởi **số pip × pip value** (tức bởi kích thước lệnh), chứ không phải bởi tỷ lệ đòn bẩy. Đòn bẩy chỉ quyết định **bạn cần bao nhiêu tiền để mở lệnh đó**.

> [!warning] Hiểu lầm nguy hiểm nhất về đòn bẩy
> "Đòn bẩy 1:500 rủi ro gấp 5 lần 1:100" — **SAI**. Với cùng một khối lượng (ví dụ 0.5 lot), rủi ro bằng tiền của bạn **hoàn toàn giống nhau** ở mọi mức đòn bẩy; chỉ có margin bị khóa là khác. Đòn bẩy trở nên nguy hiểm khi nó **cho phép bạn mở lệnh quá lớn** so với vốn (over-leverage). Rủi ro thật sự đến từ **position size**, không phải từ con số tỷ lệ. Vì vậy quy tắc ≤0.5%/lệnh của bạn kiểm soát rủi ro tốt hơn bất kỳ giới hạn đòn bẩy nào.

### Con dao hai lưỡi
Đòn bẩy khuếch đại **cả lời lẫn lỗ tính theo % vốn**. Với $1.085 margin kiểm soát $108.500: chỉ cần EURUSD giảm ~1% (khoảng 108 pip) là bạn mất gần hết phần margin đó. Đó là lý do quản trị vốn quan trọng hơn cả việc chọn hướng.

![[ForexBasics-Leverage-Notional-Diagram.png]]
> *Minh hoạ (cần tự vẽ): một sơ đồ cột so sánh — trục hoành là các mức đòn bẩy (1:30, 1:100, 1:500), trục tung là "Margin cần" cho CÙNG một notional value $108.500 (1 lot EURUSD). Vẽ 3 cột giảm dần chiều cao ($3.616 → $1.085 → $217) và một đường ngang không đổi thể hiện "Lời/Lỗ bằng tiền không đổi ở mọi mức đòn bẩy" để nhấn mạnh: đòn bẩy chỉ thay đổi margin, không thay đổi P&L. Đây là sơ đồ khái niệm tự vẽ, không phải số liệu tài khoản thật.*

### Advanced — Đòn bẩy trong tài khoản Prop Firm khác gì tài khoản Retail

Tài khoản prop firm **không hoạt động giống tài khoản retail thông thường** dù cơ chế margin cơ bản (Notional/Leverage) vẫn giữ nguyên. Một số khác biệt quan trọng cần nắm trước khi mang tư duy "leverage retail" vào thi prop firm:

- **Leverage cap riêng của prop firm:** nhiều prop firm giới hạn đòn bẩy thấp hơn nhiều so với broker retail thông thường (ví dụ chỉ cho 1:10–1:30 trên một số chỉ số/kim loại dù retail có thể cho 1:100+), đặc biệt trong giai đoạn "funded" (đã qua thử thách) — mục tiêu là giảm rủi ro hệ thống cho công ty, không phải giúp bạn "kiếm nhanh".
- **Daily Loss Limit hoạt động độc lập với margin:** một tài khoản có thể còn rất nhiều free margin (margin level >1000%) nhưng vẫn bị **khoá tài khoản ngay lập tức** nếu chạm giới hạn lỗ ngày (ví dụ -5% ngày), bất kể margin call/stop out có xảy ra hay không. Nói cách khác: **giới hạn của prop firm luôn đến trước giới hạn margin của broker**, nếu bạn tuân thủ ≤0.5%/lệnh.
- **Scaling plan (kế hoạch mở rộng vốn):** nhiều prop firm tăng dần vốn giao dịch (và đôi khi cả tỷ lệ chia lời) sau khi bạn đạt mốc lợi nhuận nhất định trong X tháng liên tiếp mà không vi phạm rule — điều này gián tiếp khuyến khích size **nhỏ và nhất quán** hơn là size lớn một lần rồi rút.
- **Vi phạm "quá size" bị xử lý khác:** ở retail, over-leverage chỉ dẫn đến margin call/stop out (mất tiền của chính bạn). Ở prop firm, over-leverage tới mức vi phạm daily loss hoặc max drawdown thường dẫn đến **chấm dứt tài khoản ngay lập tức** (mất toàn bộ phí thi + cơ hội), bất kể bạn còn bao nhiêu margin khả dụng.

> [!tip] Hệ quả thực tế
> Khi lập kế hoạch position size cho một tài khoản prop firm mới, đừng chỉ hỏi "leverage tối đa cho phép là bao nhiêu" — hãy hỏi "giới hạn lỗ ngày là bao nhiêu %, và với ≤0.5%/lệnh tôi được phép sai tối đa bao nhiêu lệnh liên tiếp trước khi chạm giới hạn đó". Đây là câu hỏi quyết định cách bạn phân bổ rủi ro trong ngày, không phải con số đòn bẩy.

---

## 7. MARGIN — Ký quỹ

### Định nghĩa
**Margin (ký quỹ)** là số tiền broker **giữ lại (khóa)** từ tài khoản của bạn như một khoản đặt cọc để duy trì vị thế đang mở. Nó **không phải phí** — bạn được trả lại khi đóng lệnh. Margin là mặt còn lại của đồng xu đòn bẩy.

```text
Margin cần = Giá trị danh nghĩa (Notional) / Đòn bẩy
           = (Số đơn vị × Giá) / Leverage
```

### Các thuật ngữ margin bắt buộc phải phân biệt
Đây là bộ từ vựng bạn sẽ gặp trên mọi nền tảng (MT4/MT5, cTrader) và trong quy tắc prop firm:

| Thuật ngữ | Ý nghĩa |
|---|---|
| **Balance (Số dư)** | Tiền trong tài khoản khi **không có** lệnh mở |
| **Equity (Vốn chủ sở hữu)** | Balance ± lời/lỗ của các lệnh **đang mở** (real-time) |
| **Used Margin (Ký quỹ đã dùng)** | Tổng margin đang bị khóa cho các lệnh mở |
| **Free Margin (Ký quỹ khả dụng)** | Equity − Used Margin = phần còn dùng để mở lệnh mới / chịu lỗ |
| **Margin Level** | (Equity / Used Margin) × 100% — chỉ số sức khỏe tài khoản |

![[ForexBasics-Margin-Terms-Diagram.png]]
> *Minh hoạ (cần tự vẽ): sơ đồ hình khối lồng nhau hoặc thanh ngang xếp chồng thể hiện quan hệ Balance → Equity (Balance ± lời/lỗ nổi) → Used Margin (phần bị khoá bên trong Equity) → Free Margin (phần còn lại của Equity sau khi trừ Used Margin), kèm mũi tên chỉ công thức Margin Level = Equity/Used Margin ở góc. Đây là sơ đồ khái niệm tự vẽ (Excalidraw/draw.io), không phải ảnh chụp tài khoản thật.*

### Margin Call & Stop Out
- **Margin Level = (Equity / Used Margin) × 100%.** Càng cao càng an toàn.
- Khi lệnh lỗ, equity giảm → margin level giảm. Chạm ngưỡng **Margin Call** (thường ~100%), broker cảnh báo bạn nạp thêm tiền hoặc giảm lệnh.
- Chạm ngưỡng **Stop Out** (thường ~50%, tùy broker), broker **tự động đóng** các lệnh lỗ nhất để bảo vệ chính họ — bạn mất quyền kiểm soát.

Ví dụ: Equity $1.000, Used Margin $500 → Margin Level = **200%** *(kiểm chứng bằng code)*. Nếu lệnh lỗ khiến equity còn $250, margin level = 50% → có thể bị stop out.

> [!tip] Với Prop Firm — điều thực sự quan trọng
> Trong tài khoản prop firm, bạn **gần như không bao giờ nên đến gần margin call/stop out**, vì các giới hạn **Daily Loss** và **Max Drawdown** của họ sẽ chặn bạn **trước** khi margin cạn. Nói cách khác: nếu bạn tuân thủ rủi ro ≤0.5%/lệnh và giới hạn thua ngày, margin level sẽ luôn ở mức rất an toàn (thường >1000%). Margin chỉ trở thành vấn đề khi bạn **over-leverage** — điều mà quy tắc của bạn đã cấm.

### Advanced — Kịch bản stress test Margin Level khi giữ nhiều vị thế tương quan

Bảng trên tính margin cho **một lệnh đơn lẻ**. Thực tế bạn có thể giữ cùng lúc nhiều lệnh — ví dụ Long NAS100 và Long XAUUSD trong cùng phiên New York vì cả hai đều đang trong xu hướng "risk-on/USD suy yếu". Hãy đi qua một kịch bản cụ thể để thấy used margin và free margin **cộng dồn (compound)** như thế nào:

**Giả định:** Tài khoản prop $100.000, đòn bẩy 1:100, đang mở đồng thời:
- Lệnh 1: 2.5 lot EURUSD (notional ≈ $271.250) → margin ≈ **$2.712**
- Lệnh 2: 1.0 lot XAUUSD tại giá 2350 (notional = 100 oz × 2350 = $235.000) → margin ≈ **$2.350**
- Lệnh 3: 5 lot NAS100 tại 20.000 điểm, giả định $1/điểm/lot (notional ≈ $100.000) → margin ≈ **$1.000**

```text
Tổng Used Margin = 2.712 + 2.350 + 1.000 = $6.062
Equity (giả sử chưa có lời/lỗ) = $100.000
Margin Level = (100.000 / 6.062) × 100% ≈ 1.650%  → vẫn rất an toàn về mặt margin
```

Về mặt **margin thuần túy**, con số trên trông rất an toàn (margin level cao). Nhưng đây chính là **cái bẫy** của việc chỉ nhìn margin level: nếu XAUUSD và NAS100 **cùng đảo chiều bất lợi một lúc** (tương quan dương trong phiên risk-off, ví dụ USD mạnh lên đột ngột kéo cả hai xuống), thì **lỗ nổi (floating loss) của cả ba lệnh cộng dồn vào equity cùng lúc**, khiến:

1. Equity giảm nhanh hơn nhiều so với việc chỉ giữ 1 lệnh với cùng tổng risk %.
2. Margin Level giảm theo (equity giảm, used margin gần như không đổi cho đến khi bạn đóng lệnh).
3. Quan trọng hơn margin level: **tổng % rủi ro thực tế trên tài khoản** đã vượt xa 0.5% nếu mỗi lệnh được tính risk 0.5% một cách độc lập — vì thua lỗ không "độc lập" khi các lệnh tương quan.

> [!warning] Margin Level cao không đồng nghĩa với an toàn
> Margin Level chỉ đo "còn bao nhiêu margin trước khi bị stop out" — nó **không** đo rủi ro tương quan. Một tài khoản có margin level 1.500% vẫn có thể vi phạm giới hạn lỗ ngày (daily loss limit) chỉ trong vài phút nếu 3 lệnh tương quan cùng đảo chiều, vì daily loss limit tính trên **equity drawdown**, không tính trên margin level. Đây là lý do mục "Correlation & Combined Risk" dưới đây bắt buộc phải đọc trước khi giữ nhiều lệnh cùng lúc.

---

## 8. Advanced — Correlation & Combined Risk (Rủi ro tương quan & rủi ro tổng hợp)

Quy tắc "≤0.5%/lệnh" trong CLAUDE.md của vault này được thiết kế cho **một lệnh độc lập**. Khi bạn giữ **nhiều lệnh cùng lúc trên các symbol có tương quan**, rủi ro thực tế của danh mục (portfolio-level risk) **không đơn giản là tổng số học** của từng % — nó có thể cao hơn hoặc thấp hơn tuỳ tương quan là dương hay âm.

### Vì sao các symbol trong vault này có thể tương quan
Bốn thị trường bạn giao dịch (NQ1/NDX, EURUSD, GBPUSD, XAUUSD) đều chịu ảnh hưởng mạnh từ **sức mạnh đồng USD (DXY)** và tâm lý risk-on/risk-off:

- **NAS100 và XAUUSD**: trong các phiên risk-off mạnh (ví dụ tin lãi suất Fed diều hâu bất ngờ), USD thường tăng mạnh → NAS100 giảm (risk-off) và XAUUSD cũng có thể giảm (USD mạnh ép giá vàng) — tức là **tương quan dương** trong kịch bản đó dù bình thường vàng hay được coi là "hầm trú ẩn".
- **EURUSD và GBPUSD**: cả hai đều là "USD ở mẫu số" (quote currency), nên khi USD biến động mạnh theo một hướng, cả hai cặp thường **di chuyển cùng chiều với nhau** (tương quan dương khá cao, thường 0.7–0.9 trong nhiều giai đoạn).

### Nguyên tắc tính rủi ro tổng hợp
```text
Nếu 2+ lệnh có tương quan CAO (cùng hướng rủi ro với USD):
   Rủi ro tổng hợp thực tế ≈ tổng % rủi ro từng lệnh (gần như CỘNG DỒN)
   → Không nên mở nhiều lệnh 0.5% "độc lập" cùng lúc trên các symbol tương quan cao,
     vì tổng rủi ro danh mục có thể vượt xa giới hạn lỗ ngày của prop firm.

Nếu 2+ lệnh có tương quan THẤP hoặc ÂM (rủi ro triệt tiêu một phần):
   Rủi ro tổng hợp thực tế < tổng % rủi ro từng lệnh
   → Vẫn nên thận trọng vì tương quan có thể ĐẢO CHIỀU đột ngột trong sự kiện tin tức lớn
     (correlation breakdown) — không nên coi tương quan âm là "miễn phí".
```

### Hướng dẫn thực chiến cho tài khoản của bạn
- **Đặt trần rủi ro theo NHÓM tương quan, không chỉ theo từng lệnh.** Ví dụ: coi NAS100 + XAUUSD như một "nhóm USD-risk" và EURUSD + GBPUSD như một "nhóm USD-quote" — tổng rủi ro đang mở trong một nhóm không nên vượt quá một ngưỡng cứng (ví dụ 1.0%, tức tương đương 2 lệnh 0.5% cùng nhóm), ngay cả khi từng lệnh riêng lẻ đều hợp lệ theo quy tắc 0.5%.
- **Không tính "đã trade 3 lệnh 0.5% hôm nay nên vẫn an toàn"** nếu cả 3 lệnh cùng hướng rủi ro với một yếu tố chung (USD, risk sentiment). Daily loss limit của prop firm không quan tâm bạn có bao nhiêu lệnh — nó quan tâm tổng equity drawdown thực tế.
- **Ưu tiên 1 setup chất lượng cao nhất thay vì nhiều setup cùng lúc** khi các setup đó rơi vào cùng một nhóm tương quan trong cùng một phiên — đây cũng là kỷ luật phù hợp với triết lý ICT (chờ setup A+ thay vì trade dàn trải).
- **Ghi chú tương quan vào nhật ký trade** khi bạn mở nhiều hơn 1 lệnh cùng lúc, để mục "Lesson Learned" (mục 16) có dữ liệu thực tế đối chiếu thay vì chỉ lý thuyết.

> [!warning] Liên hệ trực tiếp với CLAUDE.md
> Quy tắc ≤0.5%/lệnh và giới hạn lỗ ngày trong vault này chỉ thực sự bảo vệ bạn nếu được diễn giải ở **cấp độ danh mục (portfolio level)**, không chỉ cấp độ từng lệnh. Hai lệnh 0.5% "hợp lệ" trên NAS100 và XAUUSD có thể trở thành một cú sốc **1%+ đồng thời** nếu USD giật mạnh — đủ để chạm giới hạn lỗ ngày chỉ với "hai lệnh đúng luật".

---

## 9. Ghép tất cả lại — Công thức tính Position Size (phần quan trọng nhất)

Đây là nơi 6 khái niệm hội tụ và là kỹ năng **bắt buộc phải thành thạo** trước kỳ thi prop firm. Quy trình luôn đi **ngược** từ rủi ro cho phép, KHÔNG bao giờ chọn lot theo cảm tính:

```text
Bước 1: Rủi ro cho phép ($) = Số dư tài khoản × % rủi ro (≤0.5%)
Bước 2: Xác định Stop Loss (số pip / số USD vàng / số điểm chỉ số) từ setup ICT
Bước 3: Position Size = Rủi ro cho phép ($) / (Khoảng cách SL × Giá trị mỗi đơn vị)
```

### Ví dụ 1 — EURUSD (tài khoản prop $100.000, rủi ro 0.5%)
- Rủi ro cho phép = 100.000 × 0.5% = **$500**.
- Setup ICT: Long, SL cách entry **20 pip** (dưới order block).
- Pip value = $10/pip cho 1 lot.
- Size = 500 / (20 × 10) = **2.5 lot** *(kiểm chứng bằng code)*.
- Kiểm tra margin (1:100): notional ≈ 2.5 × 108.500 = $271.250 → margin ≈ $2.712 — thừa sức với tài khoản $100k.

### Ví dụ 2 — XAUUSD (cùng tài khoản, rủi ro 0.5%)
- Rủi ro cho phép = **$500**.
- Setup: SL cách entry **$5** giá vàng.
- 1 lot vàng = 100 oz → mỗi $1 vàng = $100/lot → SL $5 = $500 lỗ/lot.
- Size = 500 / (5 × 100) = **1.0 lot** *(kiểm chứng bằng code)*.

### Ví dụ 3 — NAS100 (cùng tài khoản, rủi ro 0.5%, giả định $1/điểm/lot)
- Rủi ro cho phép = **$500**.
- Setup: SL cách entry **50 điểm**.
- Size = 500 / (50 × 1) = **10 lot** (⚠️ luôn xác nhận contract size NAS100 của broker/prop firm trước — nếu là $20/điểm thì size chỉ còn 0.5 lot).

![[ForexBasics-PositionSize-Calculator-Screenshot.png]]
> *Minh hoạ (cần tự chụp lại): screenshot một position-size calculator thật (trang web calculator của broker/prop firm, hoặc phiếu lệnh/order ticket trên nền tảng MT4/MT5/cTrader) sau khi bạn đã điền: số dư tài khoản, % rủi ro, SL (pip/USD/điểm), và calculator trả về số lot. Dùng để đối chiếu chéo với kết quả tính tay ở các ví dụ trên trước khi bấm vào lệnh thật. Đây phải là ảnh chụp công cụ thật, không phải số liệu bịa.*

### Ví dụ 4 — NAS100 với SL theo ATR thay vì số điểm cố định (nối tiếp mục Advanced ở phần Pip)
- Rủi ro cho phép = **$500** (tài khoản $100.000, rủi ro 0.5%).
- Giả sử ATR(14) trên M15 của NAS100 hôm nay đo được **38 điểm**; dùng hệ số nhân 1.2 → SL = 38 × 1.2 ≈ **46 điểm** (thay vì áp đặt "50 điểm" cố định của Ví dụ 3).
- Với contract value $1/điểm/lot: Size = 500 / (46 × 1) ≈ **10.8 lot** → làm tròn XUỐNG (xem mục Best Practices) thành **10.0 lot**.
- So sánh: nếu hôm đó ATR chỉ 15 điểm (phiên trầm lắng) và SL cấu trúc ICT của bạn vẫn đòi hỏi 50 điểm (rộng hơn nhiều so với biến động thực tế phiên đó), điều này là tín hiệu cảnh báo: cấu trúc SL không khớp với chế độ thị trường hiện tại — cân nhắc chờ biến động tăng trở lại hoặc xem lại khung thời gian entry.

> [!warning] Nhắc nhở kỷ luật (theo CLAUDE.md của vault)
> Rủi ro ≤0.5%/lệnh là **luật cứng** trong journal này. Position size PHẢI được tính từ SL và rủi ro cho phép, không bao giờ chọn "cho tròn lot" hay tăng size để "gỡ" lệnh thua. Một "lỗ tốt" (đúng quy trình) tốt hơn một "thắng xấu" (may rủi, sai size).

---

## 10. Bảng tra nhanh (Cheat Sheet)

| Khái niệm | Trả lời câu hỏi | Công thức / Con số cần nhớ |
|---|---|---|
| **Pip** | Giá biến động bao nhiêu? | FX thường: 0.0001 · JPY: 0.01 · Vàng/chỉ số: dùng USD/điểm |
| **Lot** | Lệnh lớn cỡ nào? | Standard 100k = $10/pip · Mini 10k = $1 · Micro 1k = $0.10 |
| **Pip Value** | 1 pip = bao nhiêu tiền? | Kích thước pip × số đơn vị |
| **Spread** | Chi phí vào lệnh? | Ask − Bid; hẹp trong Kill Zone, giãn khi có tin |
| **Swap** | Chi phí giữ qua đêm? | Chênh lệch lãi suất; x3 vào thứ Tư; intraday ≈ không ảnh hưởng |
| **Leverage** | Cần bao nhiêu vốn để mở? | 1:100 → đặt cọc 1% notional; KHÔNG đổi lời/lỗ bằng tiền |
| **Margin** | Bao nhiêu vốn bị khóa? | Notional / Leverage; theo dõi Margin Level = Equity/Used Margin |
| **Position Size** | Vào bao nhiêu lot? | Rủi ro $ / (SL × pip value) |

---

## 11. Best Practices

Đây là những thói quen phân biệt trader **nghiệp dư** với trader **chuyên nghiệp/chuẩn prop firm** khi áp dụng 6 khái niệm ở trên vào thực chiến — không phải lý thuyết, mà là quy trình lặp lại trước mỗi lệnh, mỗi tài khoản mới.

### Checklist xác minh Contract Spec trước khi trade một symbol/tài khoản mới
Chạy checklist này **mỗi khi** mở tài khoản prop firm mới, chuyển broker, hoặc trade một symbol lần đầu — kể cả khi bạn đã quen với symbol đó ở nơi khác:

- [ ] Mở trang "Contract Specification" / "Symbol Information" chính thức của broker/prop firm.
- [ ] Ghi lại **contract size** (số đơn vị cho 1.0 lot).
- [ ] Ghi lại **giá trị mỗi pip/point cho 1.0 lot** ở symbol đó.
- [ ] Ghi lại **minimum lot step** (0.01, 0.1, hay 1.0) và **minimum/maximum volume** cho phép.
- [ ] Kiểm tra **loại tài khoản** (spread cố định/thả nổi, có commission hay không).
- [ ] Kiểm tra **leverage cap** riêng của prop firm cho symbol đó (có thể khác leverage mặc định của tài khoản).
- [ ] Dán các con số này vào một "**bảng cheat sheet position sizing**" riêng cho tài khoản đó (xem mục dưới) trước khi vào lệnh đầu tiên.

### Luôn tính Position Size TRƯỚC khi nhìn setup trên chart
Một thói quen chuyên nghiệp ít được nhắc đến: **tính position size ngay sau khi xác định rủi ro % và trước khi mở chart tìm entry**, chứ không phải sau khi đã "thích" một setup rồi mới tính ngược ra size. Lý do: nhìn chart trước dễ tạo **thiên kiến neo (anchoring bias)** — não bộ có xu hướng chỉnh SL hoặc làm tròn size sao cho "cảm thấy hợp lý" với một con số lot định sẵn trong đầu, thay vì để công thức khách quan quyết định. Quy trình đúng thứ tự:

```text
1. Xác định rủi ro % cho phép (≤0.5%) → ra số tiền rủi ro cố định trước
2. ĐÓNG chart, chỉ giữ con số rủi ro $ đó trong đầu
3. Phân tích cấu trúc ICT độc lập, xác định entry + SL hợp lệ theo mô hình
4. Tính size = Rủi ro $ / (SL × pip value) — để công thức quyết định, không "làm tròn cho đẹp"
5. Chỉ sau đó mới kiểm tra size này có khớp minimum lot step / margin khả dụng không
```

### Giữ một "Position Sizing Cheat Table" theo từng quy mô tài khoản
Thay vì tính lại từ đầu mỗi lần, hãy chuẩn bị sẵn (ghim ở đầu vault hoặc trong `09 - Goal Tracking/`) một bảng tra nhanh: với mỗi quy mô tài khoản bạn đang/sắp trade (ví dụ $10k, $25k, $50k, $100k) và rủi ro cố định 0.5%, liệt kê sẵn "size tương ứng" cho các mức SL phổ biến (10/20/30/50 pip cho FX; $2/$5/$10 cho vàng; 20/50/100 điểm cho NAS100). Bảng này giúp bạn **kiểm tra chéo** kết quả tính tay trong lúc thị trường di chuyển nhanh, giảm sai sót do vội vàng — không thay thế việc tính chính xác theo công thức mục 9, chỉ dùng để phát hiện nhanh nếu một con số bị lệch bất thường.

### Luôn làm tròn Position Size XUỐNG, không làm tròn lên
Khi kết quả công thức không rơi đúng vào minimum lot step (ví dụ ra 2.53 lot nhưng broker chỉ chấp nhận bước 0.1 lot), **luôn làm tròn XUỐNG** (2.53 → 2.5), không bao giờ làm tròn lên (2.53 → 2.6). Làm tròn lên đồng nghĩa cố ý chấp nhận rủi ro **cao hơn** mức đã tính toán và vi phạm tinh thần của giới hạn ≤0.5%/lệnh, dù chỉ lệch một chút. Làm tròn xuống luôn là hướng an toàn — phần rủi ro "bỏ lại" chỉ khiến lệnh hơi bảo thủ hơn dự kiến, không bao giờ vượt mức cho phép.

### Amateur vs Professional/Prop-Firm Habits

| Chủ đề | Thói quen nghiệp dư (Amateur) | Thói quen chuyên nghiệp / chuẩn Prop Firm |
|---|---|---|
| **Đòn bẩy** | Chọn leverage cao nhất có thể "để có nhiều sức mua hơn" | Coi leverage chỉ là cơ chế margin; chọn size dựa trên rủi ro %, mặc kệ leverage cao hay thấp |
| **Margin** | Chỉ lo margin call/stop out, bỏ qua daily loss limit | Theo dõi equity drawdown ngày là chỉ số chính; margin level chỉ là lớp bảo vệ thứ hai |
| **Position size** | Chọn lot theo "cảm giác" hoặc "cho tròn số" | Luôn tính ngược từ rủi ro $ cố định và SL cấu trúc, làm tròn xuống theo lot step |
| **SL** | Dùng một con số pip/điểm cố định cho mọi phiên | Đối chiếu SL cấu trúc với ATR hiện tại để phát hiện SL quá chật/quá rộng so với biến động |
| **Nhiều lệnh cùng lúc** | Mở nhiều lệnh 0.5% "vì mỗi lệnh đều đúng luật" | Tính rủi ro tổng hợp theo NHÓM tương quan trước khi mở thêm lệnh thứ 2, thứ 3 |
| **Contract spec** | Giả định symbol giống broker cũ, không kiểm tra lại | Luôn xác minh contract spec bằng checklist trước MỌI tài khoản/symbol mới |
| **Sau khi thua lỗ** | Tăng size lệnh sau để "gỡ" | Giữ nguyên quy trình tính size; coi thua lỗ đúng quy trình là "lỗ tốt" |

> [!summary] Tinh thần chung của Best Practices
> Toàn bộ các thói quen trên quy về một nguyên tắc: **để công thức và checklist quyết định, không để cảm xúc hoặc sự tiện lợi quyết định**. Đây chính xác là kỹ năng được đánh giá trong bài thi prop firm — không phải khả năng đoán hướng thị trường.

---

## 12. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Nhầm 1 lot = 1 đơn vị tài sản | Vào 1 lot vàng nghĩ chỉ mua 1 oz | Nhớ: 1 lot vàng = 100 oz; luôn đọc contract size |
| Coi đòn bẩy cao = rủi ro cao | Sợ 1:500 hơn 1:100 dù cùng size | Rủi ro nằm ở **position size**, không ở tỷ lệ đòn bẩy |
| Chọn lot theo cảm tính | "Vào 1 lot cho tròn" | Luôn tính ngược từ rủi ro cho phép & SL |
| Bỏ qua spread khi SL nhỏ | Entry M1 SL 5 pip, spread 2 pip | Tính spread vào SL/target; ưu tiên tài khoản raw + trade trong Kill Zone |
| Quên swap khi giữ swing | Lệnh lời nhỏ bị âm sau vài đêm | Kiểm tra bảng swap; tránh giữ qua thứ Tư nếu swap âm x3 |
| Over-leverage đến gần stop out | Margin Level tụt dưới vài trăm % | Tuân thủ ≤0.5%/lệnh; nếu làm đúng, margin luôn >1000% |

---

## 13. Câu hỏi tự kiểm tra

- Vì sao pip value của EURUSD cố định ở $10/lot còn của USDJPY thì không?
- Nếu tôi đổi từ đòn bẩy 1:100 sang 1:500 mà giữ nguyên 0.5 lot, lời/lỗ bằng tiền của tôi có thay đổi không? (Đáp: **Không** — chỉ margin thay đổi.)
- Với tài khoản $50.000, rủi ro 0.5%, SL 25 pip trên GBPUSD, tôi vào bao nhiêu lot? (Gợi ý: 250 / (25 × 10) = 1.0 lot.)
- Margin Level bao nhiêu % thì thường bị stop out? Nó liên quan gì đến giới hạn drawdown của prop firm?
- Setup intraday ICT của tôi có bị ảnh hưởng bởi swap không? Vì sao?

---

## 14. Flashcards / Active Recall

### Q1
**Hỏi:** Công thức tính Position Size là gì?
**Đáp:** Rủi ro cho phép ($) / (Khoảng cách Stop Loss × Giá trị mỗi đơn vị/pip).

### Q2
**Hỏi:** Đòn bẩy có làm thay đổi số tiền lời/lỗ của một lệnh không?
**Đáp:** Không. Lời/lỗ do số pip × pip value (tức position size) quyết định. Đòn bẩy chỉ quyết định margin cần để mở lệnh.

### Q3
**Hỏi:** 1 standard lot vàng (XAUUSD) tương đương bao nhiêu ounce, và biến động $1 giá vàng bằng bao nhiêu tiền?
**Đáp:** 100 ounce; $1 giá vàng = $100 P&L cho 1 lot.

### Q4
**Hỏi:** Margin Level được tính thế nào và ngưỡng Stop Out phổ biến là bao nhiêu?
**Đáp:** (Equity / Used Margin) × 100%; Stop Out thường ~50% (tùy broker).

---

## 15. Liên kết với Trade Journal

### Lệnh tham chiếu note nền tảng này
```dataview
TABLE date, symbol, position, pnl, r_multiple, risk_percent
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

> [!note]
> Note này là kiến thức nền, nên hãy dùng nó như "sổ tra công thức" mỗi khi tính position size cho một trade hoặc backtest. Khi ghi trade, đảm bảo `risk_percent ≤ 0.5` và kiểm tra lại size bằng công thức ở mục 9.

---

## 16. Lesson Learned

### Bài học chính
- Toàn bộ quản trị rủi ro quy về **một phép tính**: rủi ro $ / (SL × pip value) = size. Thuộc nó là thuộc nền tảng.
- Đòn bẩy không phải "rủi ro"; **position size mới là rủi ro**.
- Với vàng/chỉ số, bỏ khái niệm pip, tư duy bằng USD/điểm để tránh nhầm.

### Quy tắc cá nhân rút ra
- [ ] Luôn tính size TRƯỚC khi vào lệnh, không bao giờ chọn lot theo cảm tính.
- [ ] Luôn xác nhận contract size của NAS100/XAUUSD trên nền tảng prop firm trước phiên.
- [ ] Kiểm tra spread & lịch tin trước khi vào entry SL nhỏ.

### Câu nhắc nhở khi trade
> "Tôi không hỏi 'vào bao nhiêu lot cho đẹp?'. Tôi hỏi 'rủi ro của tôi là $X, stop loss là Y — vậy size bắt buộc là bao nhiêu?'"

---

## 17. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa 6 khái niệm |  |  |
| Tính được pip value cho FX/vàng/chỉ số |  |  |
| Tính được position size từ rủi ro & SL |  |  |
| Phân biệt margin/equity/free margin/margin level |  |  |
| Hiểu đúng vai trò của đòn bẩy (không nhầm với rủi ro) |  |  |
| Biết đặt SL theo ATR thay vì số pip cố định |  |  |
| Tính được rủi ro tổng hợp khi giữ nhiều lệnh tương quan |  |  |
| Áp dụng checklist xác minh contract spec trước khi trade symbol/tài khoản mới |  |  |

**Kế hoạch review tiếp theo:** Tự tính size cho 5 setup backtest gần nhất (EURUSD, XAUUSD, NAS100) và đối chiếu với công thức mục 9.
