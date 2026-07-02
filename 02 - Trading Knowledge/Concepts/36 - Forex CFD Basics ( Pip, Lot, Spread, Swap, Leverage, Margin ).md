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
timeframes: [] # cơ chế thị trường, không phụ thuộc khung thời gian
models: []
markets: [EURUSD, GBPUSD, NDX, XAUUSD]
importance: 5 # 1-5: nền tảng bắt buộc trước khi tính size & rủi ro
confidence: 0 # 1-5: mức độ mình hiểu khái niệm này
last_reviewed: 
created: 2026-07-01
updated: 2026-07-01
related_concepts:
  - "[[19 - Liquidity]]"
  - "[[27 - Premium Discount]]"
prerequisites: []
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

### Margin Call & Stop Out
- **Margin Level = (Equity / Used Margin) × 100%.** Càng cao càng an toàn.
- Khi lệnh lỗ, equity giảm → margin level giảm. Chạm ngưỡng **Margin Call** (thường ~100%), broker cảnh báo bạn nạp thêm tiền hoặc giảm lệnh.
- Chạm ngưỡng **Stop Out** (thường ~50%, tùy broker), broker **tự động đóng** các lệnh lỗ nhất để bảo vệ chính họ — bạn mất quyền kiểm soát.

Ví dụ: Equity $1.000, Used Margin $500 → Margin Level = **200%** *(kiểm chứng bằng code)*. Nếu lệnh lỗ khiến equity còn $250, margin level = 50% → có thể bị stop out.

> [!tip] Với Prop Firm — điều thực sự quan trọng
> Trong tài khoản prop firm, bạn **gần như không bao giờ nên đến gần margin call/stop out**, vì các giới hạn **Daily Loss** và **Max Drawdown** của họ sẽ chặn bạn **trước** khi margin cạn. Nói cách khác: nếu bạn tuân thủ rủi ro ≤0.5%/lệnh và giới hạn thua ngày, margin level sẽ luôn ở mức rất an toàn (thường >1000%). Margin chỉ trở thành vấn đề khi bạn **over-leverage** — điều mà quy tắc của bạn đã cấm.

---

## 8. Ghép tất cả lại — Công thức tính Position Size (phần quan trọng nhất)

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

> [!warning] Nhắc nhở kỷ luật (theo CLAUDE.md của vault)
> Rủi ro ≤0.5%/lệnh là **luật cứng** trong journal này. Position size PHẢI được tính từ SL và rủi ro cho phép, không bao giờ chọn "cho tròn lot" hay tăng size để "gỡ" lệnh thua. Một "lỗ tốt" (đúng quy trình) tốt hơn một "thắng xấu" (may rủi, sai size).

---

## 9. Bảng tra nhanh (Cheat Sheet)

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

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Nhầm 1 lot = 1 đơn vị tài sản | Vào 1 lot vàng nghĩ chỉ mua 1 oz | Nhớ: 1 lot vàng = 100 oz; luôn đọc contract size |
| Coi đòn bẩy cao = rủi ro cao | Sợ 1:500 hơn 1:100 dù cùng size | Rủi ro nằm ở **position size**, không ở tỷ lệ đòn bẩy |
| Chọn lot theo cảm tính | "Vào 1 lot cho tròn" | Luôn tính ngược từ rủi ro cho phép & SL |
| Bỏ qua spread khi SL nhỏ | Entry M1 SL 5 pip, spread 2 pip | Tính spread vào SL/target; ưu tiên tài khoản raw + trade trong Kill Zone |
| Quên swap khi giữ swing | Lệnh lời nhỏ bị âm sau vài đêm | Kiểm tra bảng swap; tránh giữ qua thứ Tư nếu swap âm x3 |
| Over-leverage đến gần stop out | Margin Level tụt dưới vài trăm % | Tuân thủ ≤0.5%/lệnh; nếu làm đúng, margin luôn >1000% |

---

## 11. Câu hỏi tự kiểm tra

- Vì sao pip value của EURUSD cố định ở $10/lot còn của USDJPY thì không?
- Nếu tôi đổi từ đòn bẩy 1:100 sang 1:500 mà giữ nguyên 0.5 lot, lời/lỗ bằng tiền của tôi có thay đổi không? (Đáp: **Không** — chỉ margin thay đổi.)
- Với tài khoản $50.000, rủi ro 0.5%, SL 25 pip trên GBPUSD, tôi vào bao nhiêu lot? (Gợi ý: 250 / (25 × 10) = 1.0 lot.)
- Margin Level bao nhiêu % thì thường bị stop out? Nó liên quan gì đến giới hạn drawdown của prop firm?
- Setup intraday ICT của tôi có bị ảnh hưởng bởi swap không? Vì sao?

---

## 12. Flashcards / Active Recall

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

## 13. Liên kết với Trade Journal

### Lệnh tham chiếu note nền tảng này
```dataview
TABLE date, symbol, position, pnl, r_multiple, risk_percent
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

> [!note]
> Note này là kiến thức nền, nên hãy dùng nó như "sổ tra công thức" mỗi khi tính position size cho một trade hoặc backtest. Khi ghi trade, đảm bảo `risk_percent ≤ 0.5` và kiểm tra lại size bằng công thức ở mục 8.

---

## 14. Lesson Learned

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

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa 6 khái niệm |  |  |
| Tính được pip value cho FX/vàng/chỉ số |  |  |
| Tính được position size từ rủi ro & SL |  |  |
| Phân biệt margin/equity/free margin/margin level |  |  |
| Hiểu đúng vai trò của đòn bẩy (không nhầm với rủi ro) |  |  |

**Kế hoạch review tiếp theo:** Tự tính size cho 5 setup backtest gần nhất (EURUSD, XAUUSD, NAS100) và đối chiếu với công thức mục 8.
