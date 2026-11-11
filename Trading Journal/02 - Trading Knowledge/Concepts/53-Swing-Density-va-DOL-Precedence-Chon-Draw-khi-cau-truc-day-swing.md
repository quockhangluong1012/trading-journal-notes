---
type: ict-concept
concept: Swing Density & DOL Precedence — chọn Draw khi cấu trúc dày swing
aliases:
  - Swing Density
  - DOL Precedence
  - Judas Fuel vs Bearish DOL
  - Chọn DOL khi nhiều swing
tags:
  - trading/ict/concept
  - trading/deep-dive
  - liquidity
  - bias
  - market-structure
  - d1-h1-m5
  - 2022-model
status: developing
category: Liquidity
timeframes:
  - D1
  - H1
  - M5
models:
  - ICT 2022 Model
  - PO3/AMD
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-09-22
created: 2026-09-22
updated: 2026-09-22
prerequisites:
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[59-Daily-Bias]]"
  - "[[27-Premium-Discount]]"
  - "[[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]"
  - "[[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]"
common_mistakes:
  - đếm swing thay vì kiểm tra bên nào vừa bị ăn
  - coi mọi swing low là DOL tiềm năng ngang nhau
  - short vào Judas sweep vì tưởng đó là DOL
  - gộp cụm quá rộng nên mất cấu trúc
  - dùng mật độ swing làm tín hiệu vào lệnh thay vì tín hiệu no-trade
run_tag: dol-swing-density-bias-precedence-a589d9
---

> [!summary] Tóm tắt 1 câu
> Khi cấu trúc dày swing, hướng của DOL **không** quyết định bằng cách đếm swing — mà bằng cách hỏi **bên nào vừa bị ăn**, rồi lọc qua **vị trí trong dealing range**, rồi xác nhận bằng **displacement**. Trong trend tăng HH/HL, các swing low bên dưới mặc định là **Judas fuel**, không phải DOL, cho tới khi có bằng chứng spent-flip.

> [!info] Bài này bổ sung gì cho note 52
> [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] trả lời "DOL là gì và SOP đầu ngày ra sao". Bài này trả lời câu hỏi hẹp hơn nhưng khó hơn: **khi có quá nhiều swing, làm sao chốt được một hướng**. Trọng tâm là ba thứ note 52 chỉ nêu quy tắc mà chưa đưa tiêu chí vận hành: định nghĩa swing có hiệu lực, quy tắc gộp cụm, và bảng phân vai Judas-fuel vs bearish-DOL.

---

## 1. Phát biểu lại bài toán — vì sao đếm swing là sai hướng

Câu hỏi đặt ra rất tự nhiên: giá đang HH/HL, dưới thì chằng chịt swing low, trên thì có đỉnh cũ. Vậy hôm nay giá đi lên lấy đỉnh cũ rồi mới xuống, hay đi xuống quét thanh khoản đáy rồi mới tiếp tục trend?

Cách tiếp cận sai là **đếm**: "dưới có 7 swing low, trên có 2 đỉnh → chắc phải xuống quét đáy trước". Số lượng swing không mang thông tin về hướng, vì hai lý do.

Thứ nhất, phần lớn swing low trong một trend tăng **không phải là ứng viên DOL ngang hàng**. Chúng là **nhiên liệu** — chỗ đặt stop của người mua, và là nơi pha manipulation cần chạm tới để lấy khối lượng đối ứng. Một cái đáy chỉ trở thành DOL khi phía đối diện đã bị ăn xong và cấu trúc đã flip. Trước thời điểm đó, nó chỉ là dầu.

Thứ hai, câu hỏi đúng không phải "có bao nhiêu pool" mà là "**bên nào vừa bị tiêu thụ**". Thị trường vận hành theo con lắc: một leg đi quét phía này, tiêu thụ pool đó, rồi đảo sang phía đối diện. Nên thông tin quyết định nằm ở **leg HTF gần nhất vừa kết thúc thế nào**, không nằm ở số swing tích lũy.

> [!warning] Phép thử 5 giây
> Nếu bạn phải đếm hoặc kể tên quá hai ứng viên mỗi phía, bạn chưa có DOL — bạn đang có một bản đồ. DOL là thứ nhìn thấy trong 5 giây và viết ra được kèm giá cụ thể. Không viết được thì mặc định là no-trade.

---

## 2. Swing nào có hiệu lực cấu trúc, swing nào chỉ là inventory

Đây là bước chưa có trong note 52 và là gốc của toàn bộ vấn đề "quá nhiều swing".

### Định nghĩa vận hành

Một đáy **chỉ được tính là swing low** khi giá thật sự quay đầu khỏi nó **và** giữ nguyên mức đó qua 1–2 nến xác nhận. Hệ quả trực tiếp:

- **Đáy của nến gần nhất chưa phải swing point.** Nó chỉ là giá thấp nhất hiện tại. Rất nhiều "swing low" bạn đang đếm thực chất là đáy tạm của các nến đang hình thành.
- **Nến chồng lấn nhau = range, không đọc được hướng.** Khi giá đi ngang, mọi điểm cực trị đều vô nghĩa vì không có sự từ chối (rejection) thật.
- **HH/HL gãy khi giá đóng THÂN dưới swing low trước** — rút râu không tính. Đây là ranh giới cứng giữa "hồi bình thường" và "cấu trúc đổi" (xem [[05-BOS-Break-of-Structure]] và [[09-Change-of-Character]]).

### Phân loại ba tầng

| Tầng | Tiêu chí | Vai trò | Có phải DOL? |
|---|---|---|---|
| **Structural swing** | Có rejection rõ + 1–2 nến giữ mức + là mốc mà MSS/BOS tham chiếu | Neo cấu trúc, xác định dealing range | **Có** — ứng viên DOL hợp lệ |
| **Inventory swing** | Có rejection nhưng nhỏ, nằm trong leg, không mốc cấu trúc nào tham chiếu | Chứa stop của trader LTF | **Không** — là fuel / Judas target |
| **Noise low** | Đáy nến đang chạy, chưa có nến xác nhận, hoặc nằm trong vùng chồng lấn | Không có | Không — không tính vào bản đồ |

Chỉ **swing low CONFIRMED gần nhất** mới là mốc cấu trúc. Mọi đáy thấp hơn nó chỉ là pool inventory.

> [!tip] Cách lọc nhanh trên chart
> Hỏi một câu cho mỗi đáy: **"Nếu đáy này bị phá, cấu trúc có đổi không?"** Nếu câu trả lời là không — nó không phải structural swing, và không được phép làm DOL. Chỉ những đáy mà việc phá vỡ chúng thật sự thay đổi câu chuyện mới đủ tư cách.

> [!info] Vấn đề còn lại của mục này — và bài giải quyết nó
> Tiêu chí trên **đúng nhưng không tái lập được**: hai trader nhìn cùng chart vẫn chọn swing khác nhau, và chính bạn ở hai thời điểm khác nhau cũng chọn khác nhau. Nghĩa là mọi backtest dựa trên nó đều không trung thực. Bài [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] biến tiêu chí này thành **hàm của (dữ liệu, tham số)** — N-bar pivot và Directional Change threshold — để cùng dữ liệu, cùng tham số, cho cùng kết quả.

---

## 3. Từ N swing rời rạc thành một liquidity shelf — quy tắc gộp cụm

Sau khi lọc tầng 2, số ứng viên giảm mạnh. Bước tiếp theo là **gộp cụm**: nhiều mức gần nhau là **một** pool dày, không phải nhiều DOL.

### Quy tắc gộp

1. **Cụm ngang:** 2–3 đỉnh (hoặc đáy) nằm trong khoảng **~10 pips / ~10 points** quanh nhau → gộp thành một pool. Pool này dày gấp đôi vì chứa stop của nhiều nhóm lệnh.
2. **Stack đa khung:** khi **PDH trùng PWH** (hoặc PDL trùng PWL), đó là **double-stacked** — hai khung thời gian xếp stop cùng một giá. Đây là loại BSL/SSL conviction cao nhất trong tuần, và là ứng viên DOL mạnh nhất.
3. **Thứ bậc theo khung:** sau khi gộp, xếp hạng theo khung sinh ra pool — **monthly > weekly > daily > session > Asian**. Asia high của khung 15 phút **không** ngang hàng PWH. Không đánh đồng hai loại mức giá này.

### Ngưỡng mật độ — khi nào "quá nhiều" là tín hiệu dừng

Đây là phần phải nói thẳng về độ tin cậy: **không có nguồn nào trong corpus đưa ra con số mật độ định lượng.** Các ngưỡng dưới đây là **practice number** — suy ra từ logic phân loại ở §2–§3, chưa được kiểm chứng trên data. Hãy tự backtest trước khi tin.

| Trạng thái | Dấu hiệu | Hành động |
|---|---|---|
| **Đọc được** | Sau lọc + gộp còn ≤2 ứng viên mỗi phía | Tiến hành quy trình §4 |
| **Mờ** | 3–4 ứng viên mỗi phía, mật độ hai bên tương đương | Giảm size, chỉ T1, hoặc chờ |
| **Cân bằng (accumulation)** | BSL trên và SSL dưới cách đều, mật độ tương đương, weekly ở EQ | **No-trade** — đây là balance, không phải delivery |
| **Hỗn loạn** | Không lọc nổi structural swing nào; nến chồng lấn liên tục | **No-trade** — chưa có cấu trúc để đọc |

> [!important] Mật độ swing là bộ lọc loại trừ, không phải tín hiệu vào lệnh
> "Quá nhiều swing" không bao giờ là lý do để vào lệnh theo hướng này hay hướng kia. Nó chỉ là lý do để **không vào lệnh**. Dùng nó như tín hiệu entry là biến một bộ lọc an toàn thành một cỗ máy trade quá mức.

---

## 4. HH/HL với nhiều swing low bên dưới — quy trình chốt DOL đầu ngày

Bối cảnh: D1/H1 đang HH/HL, dưới giá nhiều swing low, trên có đỉnh cũ. Đây là quy trình 6 bước, chạy trước London open, làm trong 10–15 phút.

### Bước 0 — Mark bản đồ trước khi nhìn khung nhỏ

Mark PWH/PWL (Chủ nhật, giữ cả tuần), PDH/PDL (mỗi sáng, biên midnight–midnight NY; futures NQ/ES dùng RTH high/low), ARH/ARL, NY AM high/low hôm trước, EQH/EQL, news wick. **Ghi chú cụm** theo quy tắc §3. Mục đích: tách việc *thu thập* khỏi việc *quyết định*, để không bị khung nhỏ dẫn dắt.

### Bước 1 — Đọc bias HTF trước, tuyệt đối không đếm swing low

Weekly bullish hay bearish? Daily HH/HL còn hiệu lực không (thân nến, không phải râu)? Giá đang **premium hay discount** của weekly range và daily range? EQ = (high + low) / 2.

- Weekly bullish + daily HH/HL + giá ở **discount** → bias bullish, DOL ứng viên ở **trên**.
- Giá đã ở **premium cao** (sát PWH) mà chưa quét → cảnh giác Judas lên quét rồi phân phối xuống. DOL có thể vẫn là PWH, nhưng quét xong là hết.

### Bước 2 — Hỏi "bên nào vừa bị ăn" (con lắc) — **bước quan trọng nhất**

Đây là bước quyết định hướng, và là bước mà việc đếm swing low phá hoại nhiều nhất.

- Leg HTF gần nhất vừa **purge SSL dưới + displace lên + để lại D1 FVG chưa fill** → sell-side đã **spent**. DOL = buy-side phía trên. Các đáy dưới vừa bị lấy **không còn** là DOL.
- Leg gần nhất vừa **sweep BSL trên + CISD/đóng thân trở xuống** → buy-side đã spent. Reselect xuống dưới.

Nếu chưa có leg nào quét (mọi swing low còn nguyên, giá đang premium của dealing range mới) → draw gần có thể là SSL dưới **trước**, BSL trên là ERL xa.

### Bước 3 — Chốt 1 IRL (T1) + 1 ERL (T2), có giá viết ra

Theo hướng bias đã xác định ở bước 2. Viết thành câu: *"DOL = PDH 21,640 (T1), runner PWH 21,840"*.

Kiểm tra **reach phiên**: IRL phải nằm trong tầm phiên, nếu không thì đó là multi-day target chứ không phải intraday DOL → coi như không có DOL, no-trade. Ngưỡng practice: NQ ~100–250 points, EURUSD ~50–150 pips. Bỏ setup nếu khoảng từ array tới DOL **< ~2R** dù array đẹp.

### Bước 4 — Gán vai cho toàn bộ SSL bên dưới

Đây là bước trả lời trực tiếp câu hỏi "xuống quét đáy rồi tiếp tục trend?". Xem bảng phân vai ở §5.

**Mặc định trong bullish bias + discount + có displacement lên:** mọi swing low / EQL / PDL / ARL bên dưới là **Judas target (fuel)**, không phải bearish DOL. Mark SSL gần nhất làm Judas target, kế hoạch là: chờ sweep → MSS bullish M5/M15 → entry FVG/OB tại 50% CE → target IRL rồi ERL.

### Bước 5 — Viết scenario và kiểm tra cổng loại trừ

Viết một câu PO3: bias → DOL T1 giá X, T2 giá Y → Judas quét pool đối diện giá Z ở London/NY → entry sau MSS → T1 chốt 50% + BE, runner tới ERL. **Không viết được Judas target cụ thể → no-trade.**

Cổng loại trừ (một "Không" là dừng): không có unswept pool theo hướng bias trong tầm phiên; hai phía cách đều + weekly ở EQ; PDH đã quét hôm qua mà PWH cách quá xa; giá kẹt giữa range không displacement.

### Bước 6 — Xác nhận trong phiên

Trong killzone (London 14:00–17:00 VN, NY 19:00–22:00 VN): chờ sweep pool đối diện DOL → chờ displacement thân lớn + MSS + FVG → limit 50% CE. Chỉ trade FVG hình thành **sau** khi window mở; FVG cũ là stale.

---

## 5. Hai kịch bản cạnh tranh — điều kiện phân biệt

Đây là bảng trả lời trực tiếp: làm sao biết DOL hướng lên lấy đỉnh cũ rồi đi xuống, hay đi xuống lấy thanh khoản rồi tiếp tục trend.

| Tiêu chí | **Lên đỉnh cũ rồi đi xuống** (DOL = BSL trên) | **Xuống quét đáy rồi tiếp tục** (SSL dưới là fuel) |
|---|---|---|
| **Bên vừa bị ăn** | Leg gần nhất purge SSL + displace lên → sell-side spent | Leg gần nhất sweep BSL + close back inside → buy-side spent, nhưng đây là **flip xuống**, không phải "xuống rồi tiếp tục lên" |
| **Vị trí** | Giá ở **discount** (dưới EQ) | Giá ở **discount** — nhưng ý nghĩa khác: đây là điều kiện *thuận lợi*, không phải điều kiện *DOL* |
| **Xác nhận** | Displacement thân lớn + MSS + FVG chưa fill | Chỉ cần sweep + close back inside + MSS bullish M5 |
| **Kết cục leg** | Sweep BSL → phân phối xuống (đảo chiều) | Sweep SSL → đảo lên → tiếp tục trend tăng |

> [!danger] Đây là chỗ dễ nhầm nhất — và cũng là chỗ tốn tiền nhất
> Trong bối cảnh **weekly bullish + daily HH/HL + giá discount**, kịch bản thứ hai **không phải** là "DOL hướng xuống". Việc giá đi xuống quét đáy là **pha manipulation** của một ngày bullish, không phải đích đến. Người mới nhìn thấy các đáy dày đặc rồi short vào cú quét đó, tưởng mình đang trade theo DOL — thực chất đang short đúng vào chỗ tổ chức đang gom hàng.
>
> Corpus gọi đây là **lỗi hướng phổ biến nhất** trong ICT: nhầm Judas target với DOL. Judas **luôn** quét *ngược* hướng draw. Xem thêm [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] và [[15-Inducement]].

### Bảng phân vai chi tiết: Judas fuel vs bearish DOL thật

| | **Judas fuel** (manipulation target) | **Bearish DOL thật** (destination) |
|---|---|---|
| Bias + vị trí | HTF bullish, giá ở discount | HTF bearish, hoặc bullish đã mất: daily LH/LL, giá ở premium |
| Lịch sử sweep | SSL chưa quét, dày lên sau mỗi lần test (càng chạm càng nhiều stop) | BSL trên vừa sweep + CISD/CHoCH bearish đóng dưới, hoặc range high bị **body-close** xuyên |
| Vai trong phiên | Asia/London sweep ARL/PDL/EQL rồi close back inside + MSS → entry long | NY/London sweep PDH/PWH rồi **hold beyond** + build structure xuống → continuation short |
| Confluence | PDL + discount weekly + killzone + OB/FVG bullish cùng giá | PDH sweep + premium weekly + OB/FVG bearish cùng giá |
| Cách trade | **KHÔNG** short vào Judas sweep; chờ MSS rồi long, stop dưới râu sweep, T1 PDH | **KHÔNG** bắt đáy SSL; chờ sweep BSL + MSS bearish rồi short, stop trên râu sweep, T1 PDL |
| **Khi nào chuyển vai** | Khi bullish T1 + T2 đã delivered (PDH + PWH swept + displace rời đi) → SSL dưới từ fuel **thành** DOL của leg mới | Khi bearish leg sweep PDL/PWL + bullish CHoCH đóng trên → bearish DOL spent, flip lại bullish |

**Câu chốt:** các swing low bên dưới giữ vai **fuel** cho tới khi có bằng chứng **spent-flip** — nghĩa là BSL trên đã bị quét **kèm** displacement / CISD / body-close beyond **kèm** giá ở premium. Thiếu bất kỳ điều kiện nào trong ba, chúng vẫn là fuel.

### Ví dụ worked (khung NQ)

Weekly bullish. Giá mở ngày ở **21,388** — discount của dealing range. IRL = PDH **21,640** (nearest unswept BSL), ERL = PWH **21,840**. Judas target = ARL **21,332** (nearest SSL), dự phòng EQL sâu hơn **21,186**.

London 2:08 AM quét ARL 21,332 → close back inside → M5 BOS + displacement + FVG → entry long tại 50% CE **21,444**, stop **21,290** → T1 PDH 21,640 (chốt 50% + BE), runner T2 PWH 21,840.

Toàn bộ các swing low 21,332 và 21,186 trong ngày này là **fuel**, không phải bearish DOL. Chỉ khi PWH bị quét **kèm** 15M CISD đóng dưới mới flip — lúc đó DOL mới là SSL dưới.

---

## 6. DOL và daily bias — khác nhau ở cái gì, ai dẫn ai

Câu hỏi "phân biệt DOL với daily bias, cả hai cùng dùng để dự đoán hướng tiếp theo" chứa sẵn một giả định sai: rằng chúng là hai công cụ **cùng loại**, chỉ khác tên. Chúng không cùng loại.

### Khác biệt cốt lõi

| Tiêu chí | **DOL** | **Daily Bias** |
|---|---|---|
| Trả lời câu gì | Giá đi **ĐÂU** — đích đến | Hôm nay đứng **PHÍA NÀO** (long / short / skip) |
| Bản chất | Một **pool cụ thể gắn giá** (resting orders hoặc inefficiency chưa lấp) | Một **giả thuyết có thể kiểm chứng** cho phiên |
| Đơn vị thời gian | Theo **timeframe** — một DOL mỗi timeframe; weekly draw có thể ngược intraday draw | Theo **phiên** — thesis của ngày |
| Tính ổn định | Bền tới khi bị tiêu thụ hoặc bác bỏ | Ổn định theo phiên; chỉ revise khi có structural event |
| Có phải tín hiệu entry? | **Không bao giờ.** DOL là target; entry đến từ PD array trên đường đi | Cũng không — bias là **bộ lọc**, không phải trigger |

### Quan hệ: DOL **nuôi** bias, không đồng nhất

Công thức: **Bias = DOL + structure + location + time.**

- **DOL** cho biết ĐÍCH.
- **Structure** cho biết ĐƯỜNG có thông không (HH/HL còn hiệu lực? có displacement thật hay chỉ grind?).
- **Location** (premium/discount) cho biết VỊ TRÍ có đáng tiền không.
- **Time** (killzone, weekly profile, news đỏ) cho biết HÔM NAY có chạy không.

Thiếu một trong bốn, conviction hạ một bậc. Không có DOL đặt tên kèm giá = **chưa có bias**, chỉ là phỏng đoán. Nhưng DOL một mình **không** suy ra bias.

Ngược lại, có những nguồn mechanical nói gọn "trending up → bias chạy PDH". Cách nói đó đúng **như một shortcut** trong trường hợp structure, location và time đều trung tính hoặc đồng thuận. Nó sập ngay khi ba yếu tố kia mâu thuẫn với DOL — tức là đúng ở trường hợp đặc biệt, không phải trường hợp tổng quát.

### Khi mâu thuẫn — ai thắng?

Tình huống kinh điển: **bias bullish nhưng DOL gần nhất là một pool SSL phía dưới.** Xử lý theo thứ bậc:

1. **Rule 0 — No-draw / no-bias = no-trade.** Đây là cổng cứng, chạy trước mọi thứ.
2. **Rule 1 — HTF structure veto.** Weekly vs daily ngược nhau → daily move là **correction**, không phải trend mới. Chỉ trade theo weekly.
3. **Rule 2 — Unswept-validity + timeframe weight.** Pool đã quét bị loại. Nearest unswept cùng hướng bias = T1; pool khung lớn hơn = T2/runner.
4. **Rule 3 — Location veto.** Bullish chỉ tối ưu trong discount; bearish chỉ tối ưu trong premium.
5. **Rule 4 — Time/news veto.** Tin đỏ, ngoài killzone, ngày reversal theo weekly profile → hạ size hoặc skip.

**Quyết định mẫu khi bias và DOL mâu thuẫn:** vẫn lấy lệnh theo DOL, nhưng **size −50%, T1 only, không runner**. Đây là quy tắc xuất hiện trong walkthrough EUR/USD của corpus: daily bearish (SSL 1.08220) vs weekly bullish (BSL 1.09180) → vẫn short daily nhưng nửa size, chốt full ở T1, không giữ runner xuyên weekly resistance (nguồn: `interim-nearest-vs-magnet-dol-selection`, research vault).

> [!note] Vì sao không sửa bias giữa lệnh
> Move ngược bias trong pha manipulation **không phải** invalidation. Đổi bias lúc đó = systematically vào sai phía ở đúng điểm tệ nhất. Hard invalidation chỉ khi: D1 đóng **thân** vượt biên dealing range ngược bias, hoặc có D1 BOS/CHoCH ngược hướng rõ ràng. Xem [[41-Change-in-State-of-Delivery]].

### Câu kiểm tra phân biệt nhanh

- **DOL:** *"DOL = [pool] tại [giá cụ thể], loại [resting/inefficiency], tier [IRL/ERL], unswept?"* Không viết được → no-trade.
- **Bias:** *"Bias [bullish/bearish/no-trade] vì weekly [X] + daily [Y] + DOL [Z] + location [premium/discount] + session plan [sweep A → entry B → target Z], invalid khi [điều kiện cụ thể]."* Nói "tôi bullish" mà thiếu vế sau = **chưa có bias**.

---

## 7. Confluence, ngưỡng thực hành và tính khả bác

### Bộ lọc confluence cho DOL

DOL đủ chuẩn khi hội tụ càng nhiều càng tốt. Thiếu >2 thì giảm size hoặc bỏ:

- [ ] **Unswept + visible** — chưa bị quét; nhìn thấy trong 5 giây trên HTF
- [ ] **Aligned HTF structure** — weekly + daily cùng hướng; displacement HTF về phía DOL + FVG lớn chưa fill
- [ ] **Dealing range location** — DOL nằm bên kia EQ so với giá hiện tại
- [ ] **Stacking tại giá** — PDH≈PWH / PDL≈PWL; +EQH/EQL; +OB/FVG/BPR cùng zone
- [ ] **Session/killzone timing** — sweep và entry trong London hoặc NY killzone
- [ ] **Khoảng cách khả thi + R** — IRL trong tầm phiên; array→DOL ≥ ~2R
- [ ] **Xác nhận năng lượng** — displacement + MSS/CHoCH/CISD + FVG entry 50% CE; stop ngoài râu sweep

### Ngưỡng số — đọc kèm cảnh báo

Các con số dưới đây là **practice number** từ nguồn thứ cấp, **chưa kiểm chứng độc lập**. Dùng làm điểm khởi đầu để backtest, không dùng làm sự thật:

| Ngưỡng | Giá trị | Trạng thái |
|---|---|---|
| Reach phiên NQ | ~100–250 points | Practice number |
| Reach phiên EURUSD | ~50–150 pips | Practice number |
| R:R tối thiểu tới T1 | ≥ 1:2 | Practice number |
| Khoảng cách gộp cụm | ~10 pips / points | Practice number |
| Số ứng viên tối đa mỗi phía | 2 | Practice number |
| Confluence tối thiểu | 5/8 tiêu chí | Practice number |

### Tính khả bác — phần trung thực nhất của bài

> [!warning] Điều corpus **không** chứng minh được
> Khả năng **gọi tên trước** một pool cụ thể và tuyên bố đó là đích đến chắc chắn của hôm nay **chưa được chứng minh**. Bằng chứng học thuật gần nhất là nghiên cứu của Carol Osler (Fed New York / *Journal of International Money and Finance*, DOI `10.1016/j.jimonfin.2004.12.002`) về stop-loss và price cascade trong thị trường tiền tệ. Chính dữ liệu của Osler đặt ra kỷ luật quan trọng nhất:
>
> - Round-crossings xảy ra khoảng **5 lần mỗi ngày**, nhưng cascade thật chỉ khoảng **1 lần mỗi tuần** — nghĩa là **chạm pool phần lớn là nhiễu**.
> - **Causality không được chứng minh.** Không thể khẳng định stop cluster *gây ra* move.
> - Hiệu ứng chỉ kéo dài **hàng giờ**, và **không nói gì về daily bias**.
> - Round numbers **khác** swing high/low — đừng đánh đồng hai loại mức giá.

Hệ quả logic: DOL giữ được giá trị như một **bộ lọc quy trình có cổng loại trừ và điều kiện vô hiệu viết trước**. Nó **không** giữ được giá trị như một bộ dự báo chắc chắn. Nếu mọi râu nến đều lật được DOL thì DOL giải thích được mọi kết cục — tức không kiểm chứng được.

**Quan sát nào sẽ chứng minh DOL sai:** nếu tỉ lệ trúng của pool được chọn trước phiên không cao hơn đáng kể so với chọn ngẫu nhiên một mức giá bất kỳ cùng khoảng cách trên cùng market/regime, thì DOL không mang thông tin dự báo. Hiện corpus **không có** phép đo này.

**Hai loại bằng chứng sẽ thay đổi kết luận của bài này:**
1. **Transcript gốc ICT** (mentorship 2016–2023 / 2022 model) dạy nguyên văn rằng intraday chỉ trade thẳng về PWH/PWL, bỏ qua PDH/PDL gần — tức furthest-magnet thắng trong *cùng* timeframe.
2. **Backtest 60–100 phiên** trên NQ/EURUSD cho thấy việc chọn DOL trước phiên resolve tốt hơn chọn ngẫu nhiên ở mức có ý nghĩa thống kê trong trending regime.

Toàn bộ nguồn của bài này là **thứ cấp** (blog giáo dục ICT/SMC, không phải tài liệu gốc ICT). Các con số "75–85% win rate khi full alignment" xuất hiện trong corpus là **con số vendor, chưa kiểm chứng**.

### Nguồn tham chiếu trong research vault

Các quy tắc và bảng trong bài được rút từ những note nguồn sau (research vault, tra bằng `hyperresearch note show <id>`):

| Nội dung | Note nguồn |
|---|---|
| Thứ bậc chọn DOL, IRL/ERL, no-draw=no-trade | `ict-draw-on-liquidity-dol-picking-the-target` |
| Pendulum logic, premium/discount tie-break, 8 tiêu chí DOL | `draw-on-liquidity-dol-in-ict-liquidityscan` |
| DOL nuôi bias, thứ bậc veto Rule 0–4, ma trận xung đột | `interim-dol-vs-daily-bias` |
| Tiered synthesis nearest-vs-magnet, bảng Judas-fuel vs bearish-DOL | `interim-nearest-vs-magnet-dol-selection` |
| 4-tier liquidity map, SOP đầu ngày | `interim-unified-morning-dol-routine` |
| PDH/PDL/PWH/PWL, double-stacked BSL | `ict-pdh-pdl-pwh-pwl-session-reference-levels-the-inner-circle-traders` |
| HH/HL gãy bằng body close | `ict-market-structure-higher-highs-lower-lows-explained-the-inner-circle-traders` |
| Osler — stop-loss clustering, price cascade, giới hạn causality | `351236996pdf` |
| Phê phán ICT: subjectivity, hindsight bias, khó falsify | `ict-trading-problems-subjectivity-hindsight-bias-and-the-limits-of-the-method-za` |
| Backtest ICT trên NQ (7 năm tick data) | `order-block-trading-and-fair-value-gaps-tested-on-7-years-of-nq-tickstream` |

---

## 8. Lỗi thường gặp và checklist journal

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| **Đếm swing thay vì kiểm tra bên bị ăn** | Liệt kê 7 đáy dưới rồi kết luận "phải xuống" | Hỏi "bên nào vừa bị tiêu thụ?" trước khi đếm |
| **Coi mọi swing low là DOL ngang nhau** | Đối xử Asia low như PWH | Lọc theo §2, gộp cụm theo §3, xếp hạng theo khung |
| **Short vào Judas sweep** | Thấy giá quét đáy trong ngày bullish rồi short | Judas luôn quét *ngược* DOL — đó là setup, không phải invalidation |
| **Gộp cụm quá rộng** | Gộp cả một vùng 50 pips thành "một pool" | Giữ ngưỡng ~10 pips; quá rộng thì mất cấu trúc |
| **Dùng mật độ swing làm tín hiệu entry** | "Nhiều swing quá nên long/short" | Mật độ là bộ lọc **no-trade**, không phải trigger |
| **Sửa DOL giữa lệnh để nuôi runner** | Đang lãi, nới target sang pool xa hơn | Cấm. Biến completed delivery thành round trip |
| **Dùng pool đã quét làm DOL** | Vẫn target PDH đã quét hôm qua | Swept = spent = loại, reselect phía đối diện |

### Checklist trước khi vào lệnh

- [ ] Sau lọc + gộp còn **≤2 ứng viên mỗi phía** — nếu không, no-trade
- [ ] Đã trả lời **"bên nào vừa bị ăn?"** kèm bằng chứng displacement
- [ ] DOL viết ra được **kèm giá cụ thể**, không phải mô tả
- [ ] Giá ở đúng phía dealing range (long discount / short premium)
- [ ] IRL trong **tầm phiên**; array→DOL **≥ 2R**
- [ ] Đã mark **Judas target** cụ thể (pool đối diện DOL)
- [ ] Bias và DOL **không** mâu thuẫn — nếu mâu thuẫn đã hạ size 50% + T1 only
- [ ] Trong killzone, không có tin đỏ trong window

### Action items

- [ ] Backtest 60–100 phiên: chọn DOL trước phiên theo quy trình §4, ghi lại pool nào thực sự bị chạm **và theo thứ tự nào**
- [ ] Đo riêng: tỉ lệ trúng của pool "nearest unswept" vs pool "HTF xa" trong trending vs ranging regime
- [ ] Thử nghiệm ngưỡng gộp cụm (10 / 15 / 20 pips) xem ngưỡng nào cho kết quả ổn định nhất
- [ ] Tìm transcript gốc ICT 2022 model để kiểm chứng quy tắc nearest-vs-HTF trong cùng timeframe

---

## 9. Liên kết

**Tiên quyết:** [[19-Liquidity]] · [[19-Liquidity#7. Buy-Side Liquidity (BSL)|Buy-side Liquidity]] · [[19-Liquidity#8. Sell-Side Liquidity (SSL)|Sell-side Liquidity]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[27-Premium-Discount]]

**Liên quan trực tiếp:** [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] · [[59-Daily-Bias]] · [[15-Inducement]] · [[20-Liquidity-Sweep]] · [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]]

**Vận hành:** [[02-AMD]] · [[18-Kill-Zones]] · [[21-Market-Structure-Shift]] · [[09-Change-of-Character]] · [[13-FVG-Fair-Value-Gap]] · [[26-OTE-Optimal-Trade-Entry]] · [[33-Turtle-Soup]] · [[41-Change-in-State-of-Delivery]]
