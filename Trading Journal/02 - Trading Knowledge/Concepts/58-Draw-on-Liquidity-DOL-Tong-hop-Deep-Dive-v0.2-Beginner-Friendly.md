---
type: ict-concept
concept: Draw on Liquidity (DOL) — Tổng hợp deep-dive v0.2 (beginner-friendly)
aliases:
  - DOL tổng hợp
  - DOL v0.2
  - Draw on Liquidity deep dive
  - DOL beginner
tags:
  - trading/ict/concept
  - trading/deep-dive
  - liquidity
  - dol
  - d1-h1-m5
  - 2022-model
  - quantitative
  - backtest
status: developing
category: Liquidity
timeframes:
  - D1
  - H1
  - M5
models:
  - ICT 2022 Model
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-11-06
created: 2026-09-30
updated: 2026-09-30
prerequisites:
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[12-Dealing-Range]]"
  - "[[59-Daily-Bias]]"
  - "[[27-Premium-Discount]]"
  - "[[13-FVG-Fair-Value-Gap]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[50-Displacement-In-Depth]]"
common_mistakes:
  - coi DOL là chắc chắn
  - chọn pool gần nhất làm DOL (ảo giác 63%, EV = 0)
  - dùng bias để chọn DOL rồi dùng DOL xác nhận bias
  - coi mọi DOL là ERL
  - không cập nhật DOL đã tiêu
  - vào lệnh khi còn pool chưa quét sau SL
  - đo R:R tới DOL xa mà bỏ qua vật cản
  - gọi mọi lệnh thua là bị bẫy
---

# Draw on Liquidity (DOL) — Tổng hợp deep-dive v0.2

> [!summary] Tóm tắt 1 câu
> **DOL là một dự báo có đối thủ, có hạn giờ và có điểm sai** về việc thanh khoản của *ai* sẽ bị lấy tiếp theo. Nó chọn **đích**; POI chọn **chỗ lên tàu**; M5 chỉ quyết định **có lên tàu hay không**. *(Câu này là bản nháp: hãy viết lại bằng lời của bạn theo tinh thần template.)*

> [!info] Note này là gì và đọc thế nào
> Đây là bản **gộp toàn bộ** phần nghiên cứu deep-dive về DOL thành **một note duy nhất**, theo đúng 13 phần bạn yêu cầu, kèm **17 hình SVG** (lưu trong `attachments/`, tên bắt đầu bằng `DOL-TongHop-`). Ngôn ngữ đi từ đơn giản đến kỹ thuật: mỗi phần mở đầu bằng “Nói đơn giản” cho người mới, sau đó mới đến định nghĩa chính xác.
> Nhãn dùng trong note: **[MARKET MECHANICS]** cơ chế thị trường có bằng chứng · **[ICT FRAMEWORK]** thuật ngữ/khung của ICT · **[INTERPRETATION]** diễn giải hợp lý · **[HYPOTHESIS]** giả thuyết cần kiểm chứng · **[SPECULATIVE]** tường thuật không kiểm chứng được · **[HEURISTIC]** ngưỡng đề xuất · **[BACKTEST REQUIRED]** phải backtest.

> [!warning] Giới hạn bằng chứng — đọc trước khi tin bất kỳ con số nào
> - **Chưa có backtest nào được chạy** trong note này. Toàn bộ phần định lượng (mục 12) là *thiết kế đề xuất*. Các giả thuyết HYP-DOL-001..010 đều **UNTESTED**.
> - Các con số như 63%, bảng xác suất chạm mức, bảng cỡ mẫu là **kết quả tính toán từ mô hình bước đi ngẫu nhiên**, không phải kết quả từ dữ liệu thị trường thật.
> - **Mọi mức giá trong ví dụ (mục 7) là số minh họa**, không phải dữ liệu giao dịch thật và không phải khuyến nghị. Chỉ các case ở mục 8 (C1–C4) lấy từ journal thật của bạn.
> - Nội dung ICT được tóm tắt từ transcript của bên thứ ba (Sozai) và các trang cộng đồng; IPDA không có nguồn gốc dẫn được. Hãy đối chiếu video gốc trước khi trích nguyên văn vào vault. Các con số của McLean & Pontiff lấy từ bản tóm tắt của CFA Institute, chưa đối chiếu toàn văn.

### Bản đồ trả lời: WHAT → WHY → HOW → WHEN → WHEN NOT → DISTINGUISH → APPLY → QUANTIFY → BACKTEST

| Câu hỏi | Trả lời ở đâu |
|---|---|
| **WHAT** — DOL là gì? | Mục 1 (định nghĩa 5 phần), mục 2 (nền tảng từ số 0) |
| **WHY** — vì sao nó tồn tại? | Mục 2 (BSL/SSL từ lệnh chờ), mục 3 (cơ chế thị trường) |
| **HOW** — nhận diện DOL thế nào? | Mục 1 (7 câu hỏi), mục 5 (con lắc, DOL lồng nhau, chọn ứng viên) |
| **WHEN** — áp dụng khi nào, ở khung nào? | Mục 6 (D1 → H1 → M5, giờ VN) |
| **WHEN NOT** — khi nào không áp dụng? | Mục 9 (14 edge case + 8 trường hợp không nên dùng) |
| **DISTINGUISH** — phân biệt với khái niệm gần | Mục 1 (4 thứ hay nhập làm một), mục 4 (mechanics vs ICT), mục 5 (bảng quan hệ) |
| **APPLY** — áp dụng thế nào? | Mục 6, mục 7 (3 bullish + 3 bearish), mục 11 (quy tắc v0.2) |
| **QUANTIFY** — đo thế nào? | Mục 12.1–12.2 (biến, baseline, horizon) |
| **BACKTEST** — kiểm định thế nào? | Mục 12.3–12.6 (bốn nghiên cứu, cỡ mẫu, field, hypothesis register) |
| **Bẫy đám đông** khi ai cũng biết DOL | Mục 3.5, mục 8 (8 bẫy), mục 10 |

---

## 1. Direct Answer

**Nói đơn giản (cho người mới):** Draw on Liquidity (DOL) là **"điểm đến" mà bạn dự đoán giá sẽ chạm tới tiếp theo**. Điểm đến đó thường là nơi có rất nhiều lệnh đang "ngủ" chờ sẵn, như stop-loss và lệnh breakout nằm trên một đỉnh cũ hoặc dưới một đáy cũ. Nó cũng có thể là một "khoảng trống giá" (FVG, opening gap) mà giá bỏ lại khi chạy quá nhanh.

**Nói chính xác (định nghĩa dùng được để backtest):** DOL là một **dự báo**, không phải một vật thể trên chart. Một DOL đầy đủ có 5 phần:

1. **Thời điểm khóa (t):** lúc bạn chốt dự báo. Ví dụ 11:00 giờ VN, tức 00:00 New York khi Mỹ đang dùng giờ mùa hè.
2. **Mục tiêu:** một mức hoặc vùng giá cụ thể. Đó có thể là ERL (đỉnh/đáy bên ngoài range) hoặc IRL (FVG, gap, đỉnh/đáy ngắn hạn bên trong range).
3. **Đối thủ (competitor):** mức thanh khoản quan trọng nhất ở phía ngược lại. DOL chỉ có nghĩa khi bạn nói được câu "giá sẽ chạm A **trước** B".
4. **Thời hạn (horizon):** trong phiên này, hết ngày, hay trong tuần.
5. **Điểm sai (invalidation):** sự kiện khiến bạn bỏ dự báo trước khi A hoặc B bị chạm.

Nếu thiếu phần 3 và 4, DOL gần như lúc nào cũng "đúng". Lý do: chờ đủ lâu thì giá sẽ chạm hầu hết các mức, và mức gần hơn thường bị chạm trước chỉ vì nó gần. Phần Quantification sẽ chứng minh điều này bằng số.

**Bốn thứ hay bị nhập làm một:**

| Khái niệm | Là gì | Câu hỏi nó trả lời |
|---|---|---|
| Liquidity pool | Vật thể trên chart (PDH, EQL, Asia high, FVG…) | Lệnh đang nằm ở đâu? |
| DOL | Dự báo pool nào bị chạm trước, trong bao lâu | Giá sẽ tới đâu trước? |
| Setup | Điều kiện vào lệnh trên đường tới DOL | Lên tàu ở đâu, khi nào? |
| Target (TP) | Nơi thoát lệnh, thường đặt **trước** DOL một chút | Xuống tàu ở đâu? |

![[DOL-TongHop-01-Nam-Phan-Cua-Mot-DOL.svg|760]]
*Hình 1 — Năm phần của một DOL và bốn khái niệm hay bị nhập làm một.*

**Cách xác định DOL — 7 câu hỏi** (chi tiết ở phần D1 → H1 → M5):

1. Có những pool nào ở **cả hai phía**? (ERL + IRL, tối đa 3 mỗi phía)
2. Pool nào còn nguyên, pool nào **đã bị lấy** (spent)?
3. **Bên nào vừa bị lấy** gần nhất? Sau đó giá đóng nến quay lại (sweep) hay chấp nhận vượt qua (run)?
4. **Displacement** gần nhất đi về hướng nào, và có phá swing cấu trúc không?
5. Giá đang ở **premium hay discount** của dealing range? Câu này chủ yếu cho biết chất lượng R:R, không cho biết hướng.
6. **Đường đi** tới mục tiêu có thông (LRLR) hay bị chặn (HRLR)?
7. **Trong bao lâu**, và nếu sai thì sai ở đâu?

Đầu ra luôn gồm: **DOL chính, DOL thay thế, điều kiện chuyển đổi, điểm vô hiệu và tier (A/B/C)**. Nếu không trả lời được câu 3 và 4 thì kết luận là "không có DOL", tức là không có trade. Đó là một kết luận hợp lệ.

**Về giả định "càng nhiều người biết thì thị trường càng tạo bẫy": giả định này đúng một nửa.**

- **Phần đúng [MARKET MECHANICS]:** hành vi dễ đoán tạo ra lệnh tập trung ở chỗ dễ đoán.
  - Khi hàng nghìn người cùng đặt stop ngay dưới râu nến sweep, cùng chốt lời đúng tại EQH, cùng vào ở FVG đầu tiên, thì chính các cụm lệnh đó trở thành thanh khoản mới.
  - Edge của một mẫu hình phổ biến cũng có xu hướng bị bào mòn. Với cổ phiếu, [McLean & Pontiff (2016)](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365) thấy lợi nhuận của các anomaly thấp hơn khoảng 26% ngoài mẫu và khoảng 58% sau khi được công bố.
- **Phần sai hoặc thiếu:**
  - "Thị trường" không phải một người có ý đồ, và chart không cho thấy ý đồ.
  - Trên CME, stop order **không nằm trong sổ lệnh** cho tới khi được kích hoạt ([CME](https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/futures-order-types)), nên không ai "nhìn thấy" stop của bạn.
  - Spot FX phân mảnh qua hơn 75 venue và phần lớn giao dịch được dealer khớp nội bộ ([BIS 2019](https://bis.org/publ/qtrpdf/r_qt1912g.htm)). Stop CFD của bạn có thể không bao giờ ra tới thị trường liên ngân hàng.
  - Các mức "hiển nhiên" như đỉnh cũ hay số tròn đã hiển nhiên từ trước khi ICT tồn tại.

Phần lớn cái gọi là "bẫy" giải thích được bằng 6 cơ chế, không cần giả định có ai đó nhắm vào bạn:

1. Đúng đích nhưng sai đường.
2. Nhầm pool trung gian với DOL thật.
3. DOL đã được giao mà vẫn trade tiếp.
4. Stop/TP đặt đúng chỗ đám đông đặt.
5. Ảo giác thống kê (chọn pool gần nhất, không có horizon).
6. Tự kể chuyện sau khi thua.

**Bằng chứng từ chính journal của bạn:** trong `05 - Live Trading Journal` có 8 lệnh thua mà note mô tả là "bị quét stop" (từ 25/03 tới 18/06). Cả 8 lệnh đều có ít nhất một lỗi quy trình hoặc quản lý lệnh do chính bạn ghi lại: vào trước khi sweep, ngược xu hướng, MSS ngoài POI, không thoát khi có MSS ngược, hoặc đặt stop ngay trên một đáy cũ chưa bị quét. Nói thẳng: "bẫy" trong dữ liệu của bạn chủ yếu là những lần bạn đứng vào chỗ mà quy tắc của chính bạn đã cấm. Đây là tin tốt, vì lỗi quy trình sửa được, còn "thuật toán nhắm vào tôi" thì không.

**Sáu chỉnh sửa cho framework hiện tại:**

1. **DOL không chỉ nằm ở D1.** DOL lồng nhau theo tầng: tuần → ngày → phiên. D1 cho "đích lớn", H1 cho "trạm trung gian". M5 **không có DOL riêng**, chỉ có trigger và quản lý lệnh.
2. **DOL không phải lúc nào cũng là External Liquidity.** Ngay sau khi một ERL bị lấy, đích tiếp theo thường là IRL (FVG, NDOG/NWOG). Dòng D1 của bạn ghi "External Liquidity + DOL" là đang thiếu IRL.
3. **Thứ tự nhân quả:** Dealing Range → bản đồ liquidity → DOL (chính/thay thế) → Daily Bias. Không được chọn DOL "theo hướng bias" rồi lại dùng DOL để xác nhận bias. Đó là lập luận vòng tròn, và note 52/53 của bạn đang mắc lỗi này.
4. **Bước M5 "Liquidity Sweep" cần ghi rõ ba điều:** sweep ở phía **ngược** với DOL, xảy ra tại POI HTF, và **không còn pool chưa quét nào nằm giữa entry và SL** (đúng tinh thần [[13-Mistake-Trading-Into-Unswept-Liquidity]]).
5. **"Liquidity Engineering" ở H1 nên đổi thành "liquidity formation".** Sự hình thành là thứ quan sát được. Chữ "engineering" hàm ý chủ đích, mà chủ đích thì không quan sát được.
6. **Thêm chiều thời gian.** Mọi DOL cần horizon và killzone. Không có nó thì DOL không bao giờ sai, nên bạn cũng không thể học từ nó.

> [!info] Note này khác gì các note DOL đã có trong vault
> Vault đã có nhiều note về DOL: [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]], [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]], [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]], [[dol-ict-deep-dive]] và [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]], cùng [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] và Anti-Crowd-Trap Checklist. Bốn note đầu (39, 52, 53, deep-dive) mâu thuẫn nhau ở ít nhất 6 điểm nền tảng. Note này làm ba việc: (a) viết lại để người mới cũng hiểu sâu; (b) gộp các chỗ mâu thuẫn thành bộ quy tắc v0.2 (bảng OLD → NEW ở mục 11); (c) bổ sung phần còn thiếu: toán baseline, horizon, front-running, stop buffer, feed/roll, cỡ mẫu và case thật từ journal của bạn. Các ví dụ và counterexample đều mới, không lặp lại bộ trong `dol-ict-deep-dive`. Note 56 được viết độc lập và **chưa được đối chiếu từng dòng** với note này (xem Phụ lục B).

---

## 2. Conceptual Foundation

**Nói đơn giản:** mỗi giao dịch cần hai bên. DOL là câu hỏi "giá sẽ đi tới đâu để tìm bên còn lại". Muốn hiểu câu hỏi đó thì phải hiểu lệnh nằm ở đâu và vì sao.

### 2.1 Bắt đầu từ số 0: ba loại lệnh

| Loại lệnh | Hành vi | Vai trò với thanh khoản | Ví dụ |
|---|---|---|---|
| Market order | Khớp ngay ở giá tốt nhất đang có | **Lấy** thanh khoản (ăn vào các lệnh đang chờ) | "Mua ngay 1 lot" |
| Limit order | Nằm chờ ở một giá cố định; với futures thì hiện trong sổ lệnh | **Cung cấp** thanh khoản (tạo độ sâu) | "Bán nếu giá lên 1.1010" |
| Stop order | "Ngủ", **không hiện** cho tới khi giá chạm mức kích hoạt, rồi biến thành lệnh market (hoặc limit) | Là dòng lệnh chủ động đang chờ sẵn: khi thức dậy, nó **lấy** thanh khoản | "Nếu giá lên 1.1005 thì mua" (stop-loss của lệnh short) |

Trên CME, stop order sau khi được sàn chấp nhận không vào sổ lệnh ngay. Nó phải được kích hoạt bởi một giao dịch tại mức giá đã đặt. Khi kích hoạt, nó thành stop-limit (vào sổ như một lệnh limit) hoặc "stop with protection" (khớp như lệnh market nhưng có giới hạn trượt giá). Với CFD/FX retail, stop của bạn do broker giữ. Tùy mô hình (B-book hay A-book), lệnh có thể được khớp nội bộ và không bao giờ ra thị trường liên ngân hàng.

### 2.2 Ai đặt lệnh ở đâu: nguồn gốc của BSL và SSL

Giả sử EURUSD có một đỉnh cũ rõ ràng ở 1.1000 (số minh họa). Phía trên nó có hai nhóm lệnh **MUA** đang ngủ:

- Người đang **short** đặt stop-loss ở 1.1003–1.1008. Khi kích hoạt, stop này thành lệnh **mua**.
- Người muốn **mua khi phá đỉnh** đặt buy stop ở 1.1002. Đây cũng là lệnh **mua**.

Gộp lại, ta có **Buy-side Liquidity (BSL)**: cụm lệnh mua nằm trên đỉnh. Phía dưới đáy cũ thì ngược lại. Stop-loss của người long cộng với sell stop của người bán theo breakout tạo thành **Sell-side Liquidity (SSL)**.

Khi giá chạm 1.1002, vài trăm lệnh mua market xuất hiện gần như cùng lúc. Chúng ăn hết lệnh bán đang chờ ở 1.1002, rồi 1.1003, rồi 1.1004…, nên giá **nhảy rất nhanh**. Đó là "price cascade" mà [Osler (2005)](https://www.newyorkfed.org/research/staff_reports/sr150.html) đo được trên thị trường FX: xu hướng tăng tốc tại các mức có cụm stop-loss, và stop-loss gây tác động lớn hơn, kéo dài hơn take-profit.

![[DOL-TongHop-02-Stop-Thanh-BSL-SSL.svg|760]]
*Hình 2 — Từ lệnh chờ đến BSL/SSL: stop “ngủ” thức dậy thành lệnh gì.*

### 2.3 Hai nghĩa của chữ "liquidity" — chỗ gây nhầm nhiều nhất

| | Nghĩa trong sách tài chính (vi cấu trúc) | Nghĩa trong ICT |
|---|---|---|
| Liquidity là gì | Khả năng giao dịch khối lượng lớn, nhanh, ít trượt giá, tức là **độ sâu của lệnh limit** | **Cụm lệnh sẽ bị buộc khớp** ở một mức giá dự đoán được, chủ yếu là stop |
| Ai tạo ra | Market maker, người đặt lệnh limit | Người đặt stop-loss và lệnh breakout |
| Khi giá chạm | Lệnh limit **hấp thụ** dòng lệnh | Stop **thức dậy** và **đẩy** giá đi |

Nghịch lý ở đây là: về kỹ thuật, stop **tiêu thụ** thanh khoản chứ không cung cấp. Nhưng hãy nhìn từ phía một bên đang muốn **bán khối lượng rất lớn**. Với họ, cú bùng nổ lệnh MUA do buy stop kích hoạt chính là "đối ứng" họ cần: họ khớp được lệnh bán limit đặt sẵn phía trên mà không tự đè giá xuống. Vì vậy ICT gọi cụm stop là "liquidity". Nó là **nguồn đối ứng gần như chắc chắn, nằm ở một mức giá đoán trước được**.

### 2.4 "Draw" là lực hút hay là xác suất?

ICT dùng hình ảnh cái kẹp giấy và nam châm: một số mức giá tạo ra một "xung lực hút" lên giá (2022 Mentorship Ep. 2, theo transcript của bên thứ ba). Hình ảnh này dễ nhớ nhưng dễ gây hiểu sai theo hai cách. Nam châm là **tất định**, kẹp giấy chắc chắn bị hút, còn DOL là **xác suất**. Nam châm cũng không có "hạn giờ", trong khi dự báo DOL thì bắt buộc phải có.

Ẩn dụ chính xác hơn là **GPS**:

| GPS | ICT |
|---|---|
| Điểm đến | DOL |
| Tuyến đường | Market structure, trạng thái delivery |
| Kẹt xe | Vật cản trên đường (HRLR: PD array ngược chiều chưa được mitigate) |
| Đi đường vòng | Judas swing / manipulation |
| Ga lên tàu | POI |
| Chỗ nhận ra "bản đồ sai rồi" | Invalidation / stop-loss |
| Xuống trước ga cuối một chút | TP đặt trước DOL để tránh bị front-run |
| Giờ đến dự kiến | Horizon |

Giới hạn của ẩn dụ: điểm đến của GPS là do bạn chọn nên chắc chắn, còn DOL là thứ bạn **đoán**. Thị trường có thể đổi điểm đến giữa đường khi có tin tức, và GPS không có "đối thủ".

### 2.5 ERL và IRL — hai loại điểm đến

- **ERL (External Range Liquidity):** thanh khoản ở **mép** dealing range hiện tại: đỉnh/đáy cũ, PDH/PDL, PWH/PWL, EQH/EQL.
- **IRL (Internal Range Liquidity):** thanh khoản **bên trong** range. Nhiều tài liệu cộng đồng nói IRL = FVG, nhưng theo transcript Ep. 3, định nghĩa của ICT rộng hơn: *"internal range liquidity is a short term higher low with stops above or below it or an imbalance in that same range of price action"*. Tức là IRL gồm cả các swing ngắn hạn bên trong leg mà giá đang retrace vào, chứ không chỉ FVG.

Nguyên lý "con lắc" của ICT: giá đi từ ERL về IRL, rồi từ IRL ra ERL [ICT FRAMEWORK → HYPOTHESIS, BACKTEST REQUIRED]. Hệ quả thực hành: **ngay sau khi một ERL bị lấy, DOL gần nhất thường là IRL ở phía ngược lại, chứ chưa phải ERL ở mép bên kia.**

### 2.6 DOL là một biến trạng thái, không phải một đường kẻ

`Dự kiến (projected)` → `Đang được giao (active)` → `Đã chạm (delivered)` → `Đã tiêu (spent)` hoặc `Đổi hướng (flip)`

DOL giống đèn giao thông hơn là một đường kẻ: nó đổi màu theo sự kiện. Mỗi lần đổi (sweep, run, MSS khung lớn, tin tức) cần được ghi lại. Lỗi phổ biến nhất là kẻ DOL từ thứ Hai rồi tới thứ Tư vẫn trade theo nó, dù nó đã được giao từ thứ Ba.

Hình dưới gom mọi thứ vào một bức tranh: dealing range, BSL/SSL, EQ, premium/discount, IRL, DOL và đối thủ.

![[DOL-TongHop-03-Giai-Phau-Dealing-Range.svg|1516]]
*Hình 3 — Giải phẫu một DOL trong dealing range.*

Đọc hình theo thứ tự này: giá đang nằm **trong FVG ở nửa discount**. Phía trên là cụm BSL (DOL dự báo), phía dưới là cụm SSL (đối thủ). Toàn bộ câu hỏi DOL chỉ là: *cụm nào bị chạm trước, và trong bao lâu?*

---

## 3. Market Mechanism

**Nói đơn giản:** khi giá chạm một cụm stop, có hai khả năng. Nếu có ai đó "đỡ" dòng lệnh bị ép, giá bật lại (sweep). Nếu không ai đỡ, hoặc có tin mới, giá chạy tiếp (run). Bạn không biết trước khả năng nào sẽ xảy ra. Vì vậy phải chờ xác nhận, và xác nhận nào cũng tốn R:R.

### 3.1 Bốn nhịp khi giá chạm cụm stop

1. **Tiếp cận:** giá tiến gần đỉnh cũ. Trader breakout và những người đặt TP phía trên bắt đầu hành động. Nếu có bên muốn "chặn" đỉnh thì lệnh bán của họ đã nằm sẵn ở đó.
2. **Kích hoạt:** giá chạm mức, stop thức dậy, một loạt lệnh mua market xuất hiện, giá tăng tốc (cascade). Nhịp này có bằng chứng thực nghiệm (Osler 2005).
3. **Hấp thụ hay không:**
   - Nếu phía trên có **lệnh limit bán lớn**, tức là có bên đang tận dụng dòng mua bị ép, thì dòng stop bị hấp thụ. Khi stop cạn, **không còn ai buộc phải mua**, giá rơi lại vào range → **sweep**.
   - Nếu không ai hấp thụ, hoặc xuất hiện **thông tin mới** (tin vĩ mô, định giá lại), người mua chủ động tiếp tục vào → giá chấp nhận vượt qua → **run** tới pool tiếp theo.
4. **Dấu vết để lại:** sweep thường để lại một cú đảo có displacement. Run để lại chuỗi nến đóng cửa bên ngoài mức.

Nhịp 3 có cơ sở lý thuyết. [Grossman & Miller (1988)](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1988.tb04594.x) mô tả rằng bên cần khớp ngay (cần "immediacy") phải chịu một khoản nhượng bộ giá cho bên cung cấp thanh khoản, và giá có xu hướng hồi lại khi bên cung cấp tháo vị thế. Từ đó có hai loại tác động:

- **Tác động tạm thời (temporary impact):** dòng lệnh bị ép và không mang thông tin (như stop-loss). Giá lệch đi rồi hồi lại, khớp với kịch bản "sweep rồi đảo chiều".
- **Tác động vĩnh viễn (permanent impact):** dòng lệnh mang thông tin. Giá được định giá lại, khớp với kịch bản "run và tiếp diễn".

**Chart không cho bạn biết trước dòng lệnh nào mang thông tin.** Bạn chỉ biết sau đó, qua cách nến đóng cửa và displacement phản ứng. Đó là lý do mọi mô hình ICT đều đòi xác nhận (đóng nến quay lại, displacement ngược chiều, MSS). Cũng vì vậy mà xác nhận luôn đến muộn: bạn trả bằng R:R để đổi lấy thông tin.

### 3.2 Ai đứng ở phía bên kia?

Note 39 viết rằng tổ chức lớn "buộc phải ĐẨY GIÁ tới nơi tập trung dày đặc lệnh chờ". Câu này **nói quá** [SPECULATIVE INSTITUTIONAL NARRATIVE]. Bên lớn có nhiều cách khớp lệnh khác:

- chia nhỏ lệnh theo thời gian bằng thuật toán (TWAP/VWAP);
- khớp theo khối qua RFQ hoặc qua dealer;
- được dealer khớp nội bộ;
- dồn vào các thời điểm thanh khoản dày tự nhiên như mở cửa, đóng cửa, giờ fixing.

Cụm stop chỉ là **một** nguồn đối ứng tiện lợi, không phải nguồn duy nhất và cũng không bắt buộc.

Cách nói chính xác hơn [INTERPRETATION]: *khi giá tiến gần một cụm stop, các bên cần đối ứng ở chiều ngược lại có động cơ khớp lệnh tại đó. Việc ai đó chủ động "đẩy" giá tới đó là có thể, nhưng chart không chứng minh được.*

Những bên có thể đứng ở phía kia của một cú sweep:

- market maker/HFT, kiếm tiền từ spread và từ tác động tạm thời;
- bên đặt sẵn lệnh limit lớn;
- dealer quyền chọn đang hedge;
- các thuật toán thực thi lệnh;
- chính những trader bị kích hoạt stop ở phía đối diện.

### 3.3 NQ và FX khác nhau ở chỗ nào

| | NQ/ES (CME futures) | Spot FX / CFD (EURUSD, GBPUSD, XAUUSD CFD) |
|---|---|---|
| Sổ lệnh | Một sổ lệnh tập trung | Phân mảnh qua hơn 75 venue; phần giao dịch "nhìn thấy được" ngày càng giảm (BIS 2019) |
| Stop của bạn | Nằm ở sàn/broker, **không hiện** trong sổ lệnh cho tới khi kích hoạt | Nằm ở broker; có thể được khớp nội bộ |
| Giá/khối lượng | Công khai và thống nhất | Mỗi feed có đỉnh/đáy hơi khác nhau |
| Hệ quả cho DOL | Mức giá thống nhất, nhưng mỗi quý phải roll hợp đồng | EQH có thể "bằng nhau" trên feed này mà lệch trên feed khác |

Hệ quả cho câu hỏi về bẫy: trên EURUSD CFD, kịch bản "thuật toán liên ngân hàng săn stop của tôi" gần như không thể xảy ra về mặt cấu trúc, vì stop của bạn thường không tới được đó. Điều có thật là **rất nhiều người** (quỹ, khách hàng ngân hàng, hệ thống kỹ thuật) cùng đặt stop ở cùng những mức hiển nhiên, và **tổng** các lệnh đó mới là thứ có tác động.

### 3.4 Vì sao "draw" xuất hiện: bốn lý do không cần phép màu

1. **Phản hồi dương gần mức [MARKET MECHANICS]:** khi giá tới gần cụm stop, một phần stop kích hoạt và đẩy giá tới gần hơn nữa, giống như bước xuống một con dốc.
2. **Nhiều người chủ động nhắm vào cùng một mức [MARKET MECHANICS]:** TP của trader theo xu hướng, thuật toán breakout, trailing stop. Theo [Osler (2003)](https://www.newyorkfed.org/research/staff_reports/sr125.html), với dữ liệu lệnh của một ngân hàng lớn, TP tụ ở số tròn (thường khiến xu hướng đảo chiều), còn stop-loss tụ ngay sau số tròn (thường khiến xu hướng tăng tốc).
3. **Hồi lại sau cú sốc thanh khoản [MARKET MECHANICS]:** tác động tạm thời có xu hướng hồi. Sau khi một ERL bị sweep, giá quay vào bên trong range. ICT gọi nhịp này là "từ ERL về IRL".
4. **Hình học thuần túy [STATISTICS] — lý do quan trọng nhất và bị bỏ qua nhiều nhất:** kể cả khi thị trường hoàn toàn ngẫu nhiên, mức **gần hơn** vẫn bị chạm trước thường xuyên hơn. Và nếu chờ đủ lâu, **hầu hết** các mức đều bị chạm.

Với một bước đi ngẫu nhiên không có xu hướng, xác suất chạm mức phía trên (cách **a**) trước mức phía dưới (cách **b**) là:

**P(chạm mức trên trước) = b / (a + b)**

| Khoảng cách tới DOL : tới đối thủ | P(DOL bị chạm trước) nếu thị trường ngẫu nhiên |
|---|---|
| 1 : 3 | 75% |
| 1 : 1 | 50% |
| 2 : 1 | 33% |
| 3 : 1 | 25% |

![[DOL-TongHop-04-Baseline-Hinh-Hoc-Khoang-Cach.svg|1516]]
*Hình 4 — Khoảng cách quyết định xác suất, kể cả khi thị trường hoàn toàn ngẫu nhiên.*

Mình đã chạy mô phỏng với khoảng cách ngẫu nhiên. Nếu bạn **luôn chọn pool gần hơn làm DOL**, "tỷ lệ đúng" trung bình là **63%**, dù thị trường không có lực hút nào. Còn nếu đặt TP tại DOL và SL tại pool đối thủ, kỳ vọng mỗi lệnh đúng bằng **0R** (trước phí). Đây là một đẳng thức toán học: **tỷ lệ thắng hòa vốn của một R:R bất kỳ bằng đúng xác suất ngẫu nhiên để giá chạm TP trước SL.** Vì vậy DOL chỉ có edge khi tỷ lệ chạm **vượt** baseline b/(a+b). Tỷ lệ chạm "cao" thôi thì chưa đủ.

### 3.5 Câu hỏi đám đông, nói bằng ngôn ngữ cơ học

**Phần quan sát được [MARKET MECHANICS]:** khi nhiều người dùng cùng một quy tắc, lệnh của họ tụ ở cùng mức giá:

- **Entry** tụ ở FVG đầu tiên sau MSS.
- **Stop** tụ ngay dưới râu nến sweep, tạo ra một pool **mới**, rất hiển nhiên, chỉ cách entry vài điểm.
- **TP** tụ đúng tại EQH/PDH, tạo ra một "bức tường" lệnh bán ngay dưới mức đó.

Từ đó có ba hệ quả cơ học, không cần ai có ý đồ:

- (a) cú quét thứ hai vào râu sweep có rất nhiều "nhiên liệu";
- (b) giá hay dừng lại cách DOL vài tick vì gặp bức tường TP (front-run);
- (c) khi setup thất bại, mọi người thoát cùng lúc, giá tăng tốc, và ai cũng có cảm giác "bị bẫy".

**Phần không quan sát được:** danh tính và ý đồ của bên đối diện, cũng như tỷ trọng thực tế của "dòng lệnh ICT" trong NQ hay EURUSD. Chính note 38 của bạn cũng thừa nhận chưa có nghiên cứu độc lập nào đo trực tiếp hiện tượng này.

**Phiên bản có thể kiểm định:** thay câu "thị trường bẫy người biết ICT" bằng giả thuyết HYP-DOL-008: *"setup có điểm 'độ hiển nhiên' cao cho expectancy thấp hơn setup có điểm thấp, sau khi đã kiểm soát khoảng cách và trạng thái HTF."* Nếu dữ liệu không ủng hộ, quy tắc "setup càng đẹp càng dễ là bẫy" trong Anti-Crowd-Trap Checklist nên bị bỏ, dù nghe có vẻ khôn ngoan.

Hình dưới minh họa nhịp 3: cùng một cú chạm vào cụm stop, nhưng hai kết cục khác nhau.

![[DOL-TongHop-05-Sweep-vs-Run.svg|760]]
*Hình 5 — Sweep hay run: cùng một cú chạm cụm stop, hai kết cục.*

Để ý rằng trong vài nến đầu, hai khung trông giống hệt nhau. Chỗ khác nhau chỉ lộ ra **sau đó**: nến đóng cửa ở đâu, và có ai hấp thụ hay không.

---

## 4. ICT Interpretation

**Nói đơn giản:** ICT cho bạn một "câu chuyện" giải thích vì sao giá đi tới thanh khoản. Có phần của câu chuyện là cơ chế thị trường có thật, có phần là giả thuyết cần kiểm chứng, và có phần là tường thuật không kiểm chứng được. Bạn giữ được phần *quy trình* của ICT mà không cần tin toàn bộ câu chuyện.

### 4.1 ICT thực sự dạy gì về DOL

Tóm tắt dưới đây lấy từ 2022 Mentorship, qua transcript của bên thứ ba (Sozai), và từ các khái niệm ICT phổ biến. Trước khi trích nguyên văn vào vault, hãy đối chiếu lại với video gốc.

1. **Giá đi tìm một trong hai thứ:** thanh khoản (buy stop trên đỉnh cũ, sell stop dưới đáy cũ) hoặc imbalance (FVG) cần được "rebalance" (Ep. 2).
2. **Hình ảnh nam châm:** một số mức giá và yếu tố mùa vụ tạo ra "xung lực hút" lên giá, như nam châm hút kẹp giấy (Ep. 2, khoảng [22:39]).
3. **Buy stop nằm trên đỉnh cũ là "logic đơn giản", nhìn chart là thấy** (Ep. 3, [00:07:41]).
4. **IRL** là swing ngắn hạn bên trong leg đang retrace, hoặc imbalance trong cùng vùng đó (Ep. 3, [00:35:16]). **ERL** là các đỉnh/đáy định nghĩa range.
5. **Con lắc ERL ↔ IRL:** sau khi lấy thanh khoản bên ngoài, giá quay vào bên trong, rồi lại ra bên ngoài.
6. **"Sucker play", tiền thân của Judas swing:** giá giảm trước để kéo người bán vào, chạy ngược lại họ, rồi mới tấn công buy stop phía trên (Ep. 2, [34:19]).
7. **Chuỗi setup 2022:** run on liquidity → phá cấu trúc (một short-term low/high bị phá) → imbalance → vào lệnh (Ep. 2, [44:39]).
8. **IPDA data ranges:** đỉnh/đáy của 20, 40 và 60 ngày giao dịch gần nhất là các mốc thanh khoản tham chiếu, kèm "quarterly shift" mỗi 3–4 tháng. Các trang cộng đồng khẳng định IPDA là một thuật toán có thật nhưng không dẫn được nguồn gốc nào ([innercircletrader.net](https://innercircletrader.net/tutorials/ict-ipda/)).
9. **LRLR và HRLR:**
   - LRLR (low resistance liquidity run): các swing ngắn hạn nằm giữa đỉnh cũ và đáy cũ, ít mức phòng thủ, giá quét qua dễ và để lại FVG.
   - HRLR (high resistance liquidity run): đỉnh/đáy cũ được nhiều swing ngắn hạn "bảo vệ", giá tới chậm và thường cần tin tức ([tóm tắt cộng đồng](https://innercircletrader.net/tutorials/ict-hrlr-lrlr/)).
10. **Premium/Discount và PD array:** mua ở discount để hướng tới BSL, bán ở premium để hướng tới SSL.
11. **Daily bias là "narrative"** đi từ khung lớn xuống: hôm nay giá được giao từ đâu tới đâu.

### 4.2 Phân loại từng tuyên bố: đâu là cơ chế, đâu là diễn giải

| # | Tuyên bố | Nhãn | Lý do | Cách kiểm tra |
|---|---|---|---|---|
| 1 | Stop tụ quanh đỉnh/đáy cũ và số tròn | [MARKET MECHANICS] một phần | Osler chứng minh stop tụ ở số tròn (dữ liệu một ngân hàng). Việc stop tụ ở swing là thực hành phổ biến nhưng ít bằng chứng trực tiếp hơn | Không nhìn thấy stop; đo gián tiếp qua tốc độ tăng sau khi vượt mức |
| 2 | Stop kích hoạt làm giá tăng tốc | [MARKET MECHANICS] | Osler 2005 | So tốc độ sau khi vượt mức với các mức ngẫu nhiên |
| 3 | Sau sweep, giá thường đảo chiều | [HYPOTHESIS] | Cơ chế tác động tạm thời là có thật, nhưng không phải sweep nào cũng đảo | So tỷ lệ đảo sau sweep với sau các cú vượt mức ngẫu nhiên |
| 4 | Giá "bị hút" về DOL | [HYPOTHESIS] | Có thể chỉ là hiệu ứng khoảng cách | So với baseline b/(a+b) |
| 5 | Smart money "engineer" ra EQH/EQL | [SPECULATIVE NARRATIVE] | Ý đồ không quan sát được | Chỉ kiểm tra được hệ quả: EQH có bị chạm/phá nhiều hơn một đỉnh đơn ở cùng khoảng cách không? |
| 6 | IPDA là một thuật toán có thật | [SPECULATIVE] | Không có bằng chứng công khai | Không kiểm định trực tiếp được |
| 7 | Đỉnh/đáy 20/40/60 ngày quan trọng | [ICT FRAMEWORK → HYPOTHESIS] | Dùng được như một feature | So tỷ lệ chạm/đảo với các mức khác |
| 8 | FVG sẽ được lấp | [HYPOTHESIS] | Retrace vốn đã phổ biến, nên "lấp FVG" có thể chỉ là tần suất nền | So với các vùng ngẫu nhiên cùng kích thước |
| 9 | Displacement thể hiện ý đồ của tổ chức | [INTERPRETATION] | Quan sát được: mất cân bằng lớn của lệnh chủ động. Không quan sát được: ai đặt lệnh | Đo hệ quả: xác suất tiếp diễn sau displacement |
| 10 | Judas swing ở đầu phiên đi ngược hướng thật | [ICT FRAMEWORK] | Dễ bị định nghĩa sau khi sự việc đã xảy ra: cứ cú ngược nào mà sau đó giá đảo thì "là Judas" | Phải định nghĩa trước: giờ nào, sâu bao nhiêu, lấy pool nào |
| 11 | Premium/Discount | [ICT FRAMEWORK] | Giá trị chính nằm ở hình học R:R, không phải dự báo hướng | Kiểm tra giá trị dự báo sau khi đã kiểm soát khoảng cách |
| 12 | LRLR/HRLR | [ICT FRAMEWORK → HYPOTHESIS] | Vật cản làm chậm giá là hợp lý | Đo tốc độ và tỷ lệ tới DOL theo số vật cản trên đường |
| 13 | "Thị trường bẫy những người biết ICT" | [SPECULATIVE] | Không đo được ý đồ | HYP-DOL-008 (độ hiển nhiên) |

### 4.3 Premium/discount và khoảng cách kéo ngược chiều nhau

Giả sử giá đang ở **discount sâu** của range, tức là gần đáy. Theo ICT, DOL nên là BSL ở phía trên. Nhưng theo hình học, SSL ở phía dưới **gần hơn nhiều**, nên baseline lại nghiêng về việc SSL bị chạm trước. Hai lực này ngược chiều nhau.

Vì vậy, nếu premium/discount thật sự dự báo được hướng [HYPOTHESIS], nó phải **thắng được hiệu ứng khoảng cách**, chứ không chỉ "đúng nhiều". Đây cũng là lý do mô hình ICT không mua ngay khi giá vừa vào discount, mà **chờ SSL gần bị quét trước** (sweep ở phía ngược lại). Làm vậy là loại bỏ đối thủ ở gần trước, rồi mới đặt cược vào đích ở xa. Hiểu điểm này rồi thì bạn sẽ thấy "chờ sweep" không phải một nghi thức, mà là cách sửa một bất lợi về hình học.

### 4.4 ICT đáng giá ở đâu, kể cả khi câu chuyện không chứng minh được

Nếu tách phần "vì sao" (narrative) ra khỏi phần "làm gì" (quy trình), quy trình của ICT vẫn để lại 5 thói quen tốt:

1. Xác định mục tiêu **trước** khi vào lệnh.
2. Luôn hỏi "ai đang **buộc** phải giao dịch, và ở mức giá nào".
3. Chờ thanh khoản ở phía ngược lại bị lấy trước, rồi mới đặt cược vào phía kia.
4. Đồng bộ các khung thời gian.
5. Có điểm sai rõ ràng.

Bạn có thể giữ toàn bộ quy trình này mà không cần tin rằng có một thuật toán bí mật đang điều khiển giá.

---

## 5. Structural Context

**Nói đơn giản:** market structure tạo ra các pool, dealing range chia chúng thành pool "ngoài" và pool "trong", còn displacement và MSS cho biết phía nào đang được giao. DOL là nơi tất cả các yếu tố đó gặp nhau.

### 5.1 DOL liên hệ với từng khái niệm như thế nào

| Khái niệm | Quan hệ với DOL | Chiều ảnh hưởng | Quy tắc thực hành |
|---|---|---|---|
| Liquidity | Pool là **ứng viên**; DOL là ứng viên được **chọn** | Liquidity → DOL | Mọi DOL đều là liquidity, nhưng không phải liquidity nào cũng là DOL |
| Market structure | Mỗi swing **tạo ra** một pool; cấu trúc cho biết giá đang được giao theo chiều nào | Structure → DOL | Trong leg tăng, đỉnh chưa bị vượt là ứng viên DOL; đáy tạo ra BOS gần nhất là điểm vô hiệu |
| Dealing range | Quyết định pool nào là **ngoài** (ERL), pool nào là **trong** (IRL); cho biết vị trí P/D | Range → DOL | Chốt cố định range trước phiên; không vẽ lại giữa phiên trừ khi có MSS ở khung lớn |
| Daily Bias | Bias là **đầu ra**: "hôm nay DOL chính nằm hướng nào, với điều kiện gì" | DOL → Bias | Không chọn DOL theo bias |
| Displacement | Bằng chứng cho thấy một phía đang được giao; đồng thời tạo ra IRL mới (FVG) | Displacement → cập nhật DOL | Chỉ tính displacement có phá swing cấu trúc |
| MSS | "Đổi hướng DOL", nhưng chỉ ở **đúng khung của nó** | MSS → đổi DOL cùng khung | MSS trên M5 không đổi được DOL trên D1 |
| FVG | Có hai vai: **đích IRL** (sau khi ERL bị lấy) hoặc **POI** (trên đường ra ERL) | Tùy trạng thái | Hỏi "bên nào vừa bị lấy" để biết FVG đang đóng vai nào |
| POI | Là nơi lên tàu, còn DOL là nơi xuống tàu | POI cần có DOL phía sau | POI không có DOL phía sau thì không có trade ([[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]) |

Có hai quan hệ hay bị hiểu sai nhất.

**Daily Bias ≠ DOL.** Bias là một câu có điều kiện, ví dụ: "Hôm nay nghiêng về tăng, hướng tới PDH rồi PWH, **miễn là** H1 không đóng cửa dưới X." DOL là mức giá nằm trong câu đó.

Case EURUSD 2021-05-07 của bạn là ví dụ kinh điển. Bias HTF giảm là **đúng** (`bias_correct: Yes`), nhưng DOL ngắn hạn lại hướng **lên**, vì buy-side 1.21227–1.21296 chưa bị lấy. Kết quả là lệnh short thua. Bias đúng không cứu được một DOL ngắn hạn sai.

**FVG không có vai cố định.** Cùng một bullish FVG, với phe mua đang chờ thì nó là POI (nơi lên tàu). Nhưng với giá đang giảm xuống từ ERL phía trên, nó lại là DOL (đích IRL). FVG đang đóng vai nào phụ thuộc vào trạng thái của con lắc.

### 5.2 Con lắc như một cỗ máy trạng thái [HYPOTHESIS]

**Trạng thái 1 — Vừa lấy ERL dưới** (SSL bị sweep, nến đóng cửa quay lại trong range):

- DOL gần là IRL phía trên: FVG tạo ra lúc giá bật lên, hoặc một swing ngắn hạn.
- Nếu có thêm displacement và MSS, DOL xa là ERL phía trên.

**Trạng thái 2 — Vừa lấy ERL trên:** mọi thứ đảo ngược so với trạng thái 1.

**Trạng thái 3 — Chưa bên nào bị lấy** (giá ở giữa range, không có displacement):

- Chưa có DOL có hướng, nên chờ cú raid đầu tiên.
- Đây thường là lúc Judas swing xuất hiện.

**Chuyển trạng thái:**

- **Sweep:** giá vượt mức ít nhất τ, rồi đóng nến quay lại, kèm displacement ngược chiều → con lắc đổi phía.
- **Run:** giá được chấp nhận ở phía bên kia, tức có ≥ 2 nến đóng cửa bên ngoài mức, tính theo khung của mức đó → DOL dời sang pool kế tiếp **cùng phía**.

Hình dưới vẽ đúng nhịp này.

![[DOL-TongHop-06-Con-Lac-ERL-IRL.svg|1516]]
*Hình 6 — Con lắc ERL ↔ IRL: năm nhịp.*

Câu hỏi quan trọng nhất mỗi sáng là **"con lắc đang ở nhịp nào?"**. Ở nhịp 2 và 4, FVG là **đích**. Ở nhịp 1 và 3, cũng FVG đó lại là **nơi lên tàu** cho chặng tiếp theo.

### 5.3 DOL lồng nhau (nested DOL)

| Tầng | Ứng viên điển hình | Vai trò | Sự kiện nào được phép đổi nó |
|---|---|---|---|
| Tuần / tháng | PWH/PWL, đỉnh/đáy tháng, đỉnh/đáy 20–60 ngày, FVG W1/D1 | Đích "chiến lược", dành cho runner | MSS trên D1/W1, hoặc nến D1 đóng cửa chấp nhận vượt mức |
| Ngày | PDH/PDL, swing D1, FVG D1/H4, NWOG/NDOG | DOL của Daily Bias, dùng làm T2 | MSS trên H4/H1 có displacement |
| Phiên | High/low phiên Á và London, EQH/EQL H1, FVG H1 | T1 (trạm trung gian), hoặc "nhiên liệu" cho Judas | MSS trên M15/M5 |
| Thực thi | Swing M5/M1 | **Không phải DOL**, chỉ là trigger và công cụ quản lý lệnh | — |

![[DOL-TongHop-07-DOL-Long-Nhau.svg|1516]]
*Hình 7 — DOL lồng nhau: bốn tầng, mỗi tầng một vai.*

Ba quy tắc cho DOL lồng nhau:

1. DOL ở tầng dưới luôn là **một trong hai thứ**: hoặc là bậc thang cùng chiều với DOL tầng trên (stepping stone), hoặc là nhịp retrace ngược chiều về IRL. Không có khả năng thứ ba.
2. Sự kiện ở tầng dưới không đổi được DOL của tầng trên. Đây chính là quy tắc "scale alignment" trong note 43: trigger và target phải thuộc hai tầng khác nhau.
3. T1 là pool có ý nghĩa gần nhất theo hướng lệnh. T2 là DOL ngày. Runner nhắm tới DOL tuần, và chỉ để runner khi đường đi thông.

### 5.4 Khi có nhiều ứng viên giống nhau thì chọn thế nào

**Bước A — Lập bản đồ.** Mỗi phía tối đa 3 ứng viên. Ghi giá của từng ứng viên, và khoảng cách từ giá hiện tại tới nó tính bằng ATR của khung chứa mức đó.

**Bước B — Gộp thành "kệ thanh khoản".** Các pool cách nhau không quá 0.15 × ATR (của khung chứa mức) thì gộp thành một kệ, ví dụ PDH + EQH + một số tròn. Kệ càng nhiều lớp và thuộc khung càng lớn thì càng "nặng" [HEURISTIC].

Ngưỡng theo ATR này thay cho con số cố định "~10 pips/points" trong note 53. Lý do: 10 điểm NQ và 10 pip EURUSD không cùng quy mô, và mỗi thị trường có mức biến động riêng.

**Bước C — Loại những ứng viên không đủ điều kiện:**

- **Pool đã tiêu:** giá đã giao dịch xuyên qua nó ít nhất τ.
- **Ngoài tầm với của horizon:** trong mô hình ngẫu nhiên, một mức cách 1.5 ATR chỉ có khoảng 2% khả năng bị chạm trong một ngày. Mức đó là DOL tuần, không phải DOL hôm nay.
- **Bị chặn:** giữa giá và ứng viên có một PD array ngược chiều ở khung lớn chưa được mitigate. Khi đó DOL thực tế là chính vật cản đó.

**Bước D — Xếp hạng bằng các "họ bằng chứng" độc lập**, không đếm trùng:

1. **Trạng thái con lắc:** bên nào vừa bị lấy, và đó là sweep hay run?
2. **Displacement cấu trúc:** leg gần nhất có phá swing cấu trúc theo hướng đó không?
3. **Vị trí trên khung lớn:** premium hay discount. Nhớ rằng yếu tố này kéo ngược chiều với khoảng cách.
4. **Đường đi:** LRLR hay HRLR, và vật cản chặn đường đầu tiên là gì?
5. **Thời gian:** killzone sắp tới, lịch tin tức, ngày nào trong tuần.
6. **Liên thị trường (chỉ dùng để phá thế hòa):** SMT giữa NQ/ES, hoặc giữa EURUSD/GBPUSD.

Lưu ý: chuỗi sweep → displacement → MSS → FVG là **một chuỗi nhân quả**. Nó chỉ tính là **một** họ bằng chứng (chất lượng trigger), không phải bốn phiếu riêng. Thang 5/8 điểm trong note 52 đang đếm trùng chỗ này.

**Bước E — Đầu ra.** Ghi rõ DOL chính, DOL thay thế, điều kiện đổi DOL (flip), điểm vô hiệu, horizon và tier. Nếu sau các bước trên vẫn mơ hồ, quyết định đúng là: "Chưa có DOL. Chờ ERL đầu tiên bị lấy rồi đọc phản ứng của giá."

**Bốn tình huống đặc biệt:**

- **Hai pool cùng phía**, ví dụ PDH ở gần và PWH ở xa. Đừng hỏi "cái nào là DOL". Hãy hỏi "cái nào là **điểm kết thúc leg**". Pool có ý nghĩa ở khung lớn, hoặc pool có một PD array premium khung lớn nằm ngay phía trên, thường là điểm kết thúc. Pool còn lại chỉ là bậc thang.
- **Hai phía cách đều nhau và không có displacement.** Thị trường đang cân bằng, nên chưa có DOL có hướng.
- **Khung lớn và khung nhỏ mâu thuẫn**, ví dụ D1 hướng lên nhưng H1 đang giảm. H1 đang đi về IRL. Short theo H1 là lệnh ngược khung lớn: chỉ nửa size, chỉ T1, không runner, hoặc bỏ luôn. Trade tốt hơn là long **từ chính IRL đó**.
- **Pool nằm ngay tại POI của khung lớn.** Khi đó cú quét pool chính là điểm vào lệnh (Turtle Soup). Đây là ngoại lệ A trong note 43.

---

## 6. D1 → H1 → M5 Application

**Nói đơn giản:** D1 chọn **đích**, H1 chọn **đường đi và ga lên tàu**, M5 chỉ quyết định **có lên tàu hay không**. M5 không bao giờ được đổi đích.

![[DOL-TongHop-08-D1-H1-M5-Vai-Tro.svg|1516]]
*Hình 8 — D1 chọn đích, H1 chọn đường và ga, M5 quyết định lên tàu.*

### 6.0 Mốc giờ Việt Nam (quan trọng vì Mỹ đổi giờ)

Mỹ dùng giờ mùa hè (EDT) tới ngày 01/11/2026. Note 52 và 53 của bạn chỉ quy đổi theo giờ mùa đông, nên các mốc trong đó hiện đang lệch 1 tiếng.

| Mốc (giờ New York)                           | Giờ VN khi Mỹ dùng EDT (bây giờ → 01/11) | Giờ VN khi Mỹ dùng EST (sau 01/11) |
| -------------------------------------------- | ---------------------------------------- | ---------------------------------- |
| 00:00 NY — midnight open, thời điểm khóa DOL | 11:00                                    | 12:00                              |
| London KZ 02:00–05:00                        | 13:00–16:00                              | 14:00–17:00                        |
| NY AM KZ 07:00–10:00 (index: 08:30–11:00)    | 18:00–21:00 (19:30–22:00)                | 19:00–22:00 (20:30–23:00)          |
| Đóng nến D1 FX lúc 17:00                     | 04:00 sáng hôm sau                       | 05:00 sáng hôm sau                 |
| Phiên NQ đầy đủ (ETH) 18:00–17:00            | 05:00 → 04:00 hôm sau                    | 06:00 → 05:00 hôm sau              |

Hãy chọn **một** định nghĩa "ngày" và ghi nó vào thẻ DOL. Ví dụ: với NQ dùng ETH 18:00–17:00 NY, với FX dùng mốc đóng nến 17:00 NY. Lý do: cùng một ngày nhưng tính theo định nghĩa khác nhau thì PDH/PDL sẽ ra những con số khác nhau.

### 6.1 D1 — "Tôi đang ở đâu, và đích lớn ở đâu?" (làm một lần, trước 11:00 VN)

1. **Chốt cố định dealing range D1.** Dùng swing high và swing low gần nhất đang bao quanh giá và có ý nghĩa cấu trúc, nghĩa là swing đó đã tạo BOS/MSS hoặc đã có phản ứng ít nhất 1 ATR D1. Nếu muốn khách quan hơn, dùng thuật toán Directional Change trong note 54.
2. **Vẽ bản đồ ERL:** PWH/PWL, PDH/PDL, các swing D1, EQH/EQL trên D1, và (tùy chọn) đỉnh/đáy 20/40/60 ngày.
3. **Vẽ bản đồ IRL:** FVG D1/H4 chưa được lấp, NWOG/NDOG, các swing ngắn hạn trong leg gần nhất.
4. **Xác định con lắc đang ở đâu:** ERL nào bị lấy gần nhất, vào ngày nào? Sau đó nến D1 đóng cửa quay lại trong range (sweep) hay đóng cửa vượt ra ngoài (run)?
5. **Xác định vị trí:** giá đang ở bao nhiêu % của range, tức là premium hay discount.
6. **Kiểm tra đường đi:** liệt kê các vật cản nằm giữa giá và từng ứng viên DOL.
7. **Viết thẻ DOL** theo mẫu ở mục 4.

### 6.2 H1 — "Giá đang cư xử thế nào trong bối cảnh đó?"

1. **Liệt kê pool của phiên:** high/low phiên Á, high/low London, EQH/EQL trên H1. Gán vai cho từng pool:
   - "nhiên liệu": nằm ở phía ngược với DOL, là nơi Judas có thể quét qua;
   - "bậc thang": nằm cùng phía với DOL.
2. **Chọn POI.** Nếu DOL hướng lên, chọn FVG/OB trên H1 hoặc H4 nằm ở vùng discount của leg H1. Tốt nhất là POI nằm gần, hoặc ngay dưới, một pool có thể bị quét.
3. **Qua cổng Mistake 13.** Hỏi: "Pool chưa quét gần nhất nằm ở phía nào so với SL dự kiến?" Nếu nó nằm phía SL và gần (≤ 0.5 ATR H1) thì chưa trade. Chờ pool đó bị quét trước.
4. **Đọc trạng thái delivery:** H1 đang displacement về phía DOL, hay đang retrace về IRL?

### 6.3 M5 — "Đã có trigger chưa?" (chỉ trong killzone)

1. **Sweep ở phía ngược lại, ngay tại POI H1.** Với lệnh long, đó là cú quét SSL trên M5/H1, ví dụ quét low phiên Á hoặc low London.
2. **MSS có displacement hướng về DOL.** Thân nến phải đóng cửa vượt qua swing đã khởi động nhịp giảm trước đó, chứ không phải vượt một swing M5 vụn vặt.
3. **Entry.** Vào ở FVG đầu tiên xuất hiện sau MSS, đặt lệnh limit ở CE. Ngoại lệ: nếu cú sweep đầu quá nông (chưa đạt τ) mà ngay bên dưới vẫn còn một pool hiển nhiên, hãy chờ cú thao túng thứ hai.
4. **SL.** Đặt ngoài đỉnh/đáy của cú sweep, cộng thêm buffer 0.1–0.2 ATR M5 [HEURISTIC]. Nếu pool cấu trúc kế tiếp nằm trong phạm vi 0.5 ATR H1, đặt SL ra ngoài cả pool đó. Sau khi có SL, **tính lại size để rủi ro không quá 0.5%**.
5. **TP.**
   - T1: đặt **trước** bậc thang đầu tiên, chừa buffer 0.05–0.1 ATR.
   - T2: đặt trước DOL ngày.
   - Runner (tùy chọn): hướng về DOL tuần.
6. **R:R.** Tính R:R đến vật cản chặn đường đầu tiên; kết quả phải đạt ít nhất 2. Bậc thang trên một đường LRLR không tính là vật cản. Một mức từng có phản ứng mạnh (HRLR) thì có tính.

**Ba việc M5 không được làm:**

- tạo ra một DOL mới cho ngày hôm đó;
- lật ngược DOL của D1;
- "cứu" một narrative D1 đã sai.

### 6.4 Thẻ DOL trước phiên (mẫu để copy vào daily note)

```
THẺ DOL — [ngày] — [symbol]         Khóa lúc: 11:00 VN (00:00 NY)
Định nghĩa ngày: ETH 18:00–17:00 NY  /  FX 17:00 NY
D1 range: H ____ / L ____ / EQ ____  → giá ở ____% (premium / discount)
Con lắc: bên vừa bị lấy ____ (ngày ____; sweep / run)
DOL chính: ____ (loại ____, khung ____) — cách ____ ATR — horizon ____
Đối thủ:   ____ — cách ____ ATR — baseline P = b/(a+b) = ____
DOL thay thế: ____  | điều kiện flip: ____
Invalidation: ____
Đường đi: LRLR / HRLR — vật cản chặn đầu tiên: ____
Tin tức: ____  | Tier: A / B / C
Pool "nhiên liệu" phía ngược (nơi Judas có thể quét): ____
```

Khi backtest bằng Bar Replay, bạn **phải điền xong thẻ này trước khi bấm play**. Đó là cách duy nhất để đo DOL mà không bị nhiễm hindsight.

---

## 7. Detailed Examples

> [!warning] Số minh họa, không phải dữ liệu thật
> Mọi mức giá dưới đây là **số minh họa** để giảng giải. Đây không phải dữ liệu thật và không phải khuyến nghị giao dịch. Mỗi ví dụ đi theo mốc thời gian T0 → T5, để tách thông tin có **trước** khi vào lệnh (ex-ante) khỏi thông tin chỉ biết được **sau** đó (ex-post).

### Bullish 1 — NQ: tiếp diễn theo nhịp ERL → IRL → ERL (DOL tuần, T1 là PDH)

**T0 — Bối cảnh D1 (sáng thứ Hai, trước 11:00 VN):**

- Cấu trúc D1 đang tăng (HH/HL).
- Thứ Ba tuần trước, giá quét đáy swing 26,380 (SSL) nhưng nến D1 đóng cửa quay lại phía trên.
- Tiếp theo là một cú displacement tăng, để lại **FVG D1 26,650–26,780** (CE 26,715).
- Thứ Sáu giá lên tới PDH **27,050**. Tuần mới mở cửa ở 26,900.
- Dealing range: từ 26,380 lên PWH 27,450 (PWH chưa bị lấy). EQ = 26,915, tức giá mở cửa đang nằm sát EQ.
- ATR D1 ≈ 400 điểm.

**Thẻ DOL:**

- **DOL tuần** = PWH 27,450, cách giá +550 điểm (1.375 ATR). **Đối thủ** = đáy sweep 26,380, cách −520.
- **Baseline chỉ 48.6%**, gần như tung đồng xu. Khoảng cách không cho lợi thế gì, nên mọi lợi thế phải đến từ bằng chứng.
- Bằng chứng:
  - con lắc: ERL phía dưới đã bị lấy và sau đó có displacement tăng → đang ở trạng thái 1;
  - IRL (FVG D1) chưa được retest;
  - đường lên PWH là LRLR: chỉ có vài swing H1 nhỏ, không có FVG giảm D1 nào chưa được mitigate.
- Kết luận: **Tier A**. Kế hoạch là chờ giá về IRL (FVG D1) để mua, T1 = PDH, T2 = PWH.
- Invalidation: nến D1 đóng cửa dưới 26,650 (IRL bị phá), hoặc H1 có displacement giảm xuyên qua low London kèm MSS giảm.
- Trong mô hình ngẫu nhiên, xác suất PWH bị chạm trong vòng 5 ngày chỉ khoảng 33%. Đừng coi việc runner chạy tới PWH trong tuần là chắc chắn.

**T1 — Phiên Á (05:00–11:00 VN):** giá đi ngang trong range 26,820–26,940. Low phiên Á (26,820) là SSL của phiên, tức "nhiên liệu" nằm ngay trên FVG D1.

**T2 — London (13:00 VN):** giá quét low phiên Á, xuống tới **26,745**. Mức này nằm trong FVG D1 và vẫn trên CE. Đây là cú sweep ở phía ngược lại, xảy ra đúng tại POI khung lớn.

**T3 — M5:** một cú displacement tăng phá lower high 26,835 (MSS), để lại FVG M5 26,790–26,815.

**T4 — Lệnh:**

- Entry 26,802. SL 26,735 (dưới đáy sweep 10 điểm), rủi ro 67 điểm.
- T1 = 27,040 (dưới PDH 10 điểm) → **3.55R**. Chỉ cần tỷ lệ thắng 22% là hòa vốn.
- T2 = 27,435 (dưới PWH 15 điểm) → **9.45R**, chỉ dành cho một phần runner nhỏ.

**T5 — Kết quả (giả định):** phiên NY chạm T1. PWH có tới hay không còn phụ thuộc vào diễn biến cả tuần.

**Nhánh sai:** nếu trong phiên London giá xuyên thủng 26,650 với displacement và H1 đóng cửa dưới mức này, FVG D1 đã thất bại. Theo con lắc, ERL phía dưới (26,380 và thấp hơn) có thể trở thành DOL. Khi đó đứng ngoài, không "bắt đáy".

**Bài học:** DOL (PWH) không phải chỗ vào lệnh. IRL (FVG D1) là POI, low phiên Á là nhiên liệu, còn PDH là bậc thang.

### Bullish 2 — EURUSD: quét ERL khung lớn (đáy 40 ngày) → DOL lật sang IRL phía trên

**T0 — Bối cảnh D1:**

- EURUSD đã giảm 3 tuần. Đáy 40 ngày nằm ở 1.0850.
- Ngay bên dưới là **FVG tăng W1 1.0790–1.0830**, một POI discount của khung lớn.
- ATR D1 ≈ 60 pip.
- Ngày X: giá quét xuống **1.0812** (thấp hơn đáy 40 ngày 38 pip, lọt vào FVG tuần), rồi nến D1 đóng cửa ở **1.0872**, tức đã quay lại trên 1.0850. Đây là kiểu "không đóng cửa được bên dưới" (failure to close below), một dạng Turtle Soup D1. High của ngày X là 1.0888.

**Thẻ DOL (tối ngày X):**

- Các ứng viên phía trên:
  - PDH 1.0888: chỉ là bậc thang, vì đó là high của chính cây nến đảo chiều;
  - **FVG giảm D1 1.0930–1.0965** (CE 1.09475): IRL còn lại từ nhịp giảm trước đó;
  - lower high D1 ở 1.1010: ERL ngắn hạn.
- Con lắc vừa lấy ERL phía dưới, nên **DOL gần nhất là IRL (FVG D1)**, chưa phải 1.1010.
- Baseline: CE cách +75.5 pip, đáy sweep cách −60 pip → **44%**. Bằng chứng phải đủ mạnh để bù được bất lợi về khoảng cách này.
- Horizon: 3 ngày. Trong mô hình ngẫu nhiên, xác suất chạm CE trong 3 ngày chỉ khoảng 25%.
- Invalidation: nến D1 đóng cửa dưới 1.0812, tức cú sweep đã biến thành run.

**T1–T3 — Phiên London hôm sau:** giá hồi về FVG H1 1.0850–1.0862 (do cây nến đảo chiều tạo ra), quét low phiên Á 1.0855 xuống 1.0846, rồi M5 xuất hiện MSS tăng.

**T4 — Lệnh:**

- Entry 1.0862. SL 1.0842, rủi ro 20 pip.
- T1 = 1.0928 (ngay dưới đáy FVG D1) → **3.3R**.
- T2 = 1.0946 (ngay dưới CE) → **4.2R**.
- PDH 1.0888 chỉ cho 1.3R. Nếu PDH chỉ là một đỉnh "nhẹ", coi nó là bậc thang và **không** đặt T1 ở đó. Nếu nó từng có phản ứng mạnh (HRLR) thì phải coi là vật cản. Khi đó R:R tới vật cản nhỏ hơn 2, nên bỏ lệnh.

**Yếu tố phá thế hòa (tùy chọn):** GBPUSD tạo đáy thấp hơn trong khi EURUSD thì không, tức có SMT tăng [HYPOTHESIS].

**T5 — Kết quả (giả định):** trong 2 ngày, giá đi vào FVG D1.

**Có nên để runner không?** Chỉ nghĩ tới mục tiêu 1.1010 nếu nến D1 đóng cửa **xuyên qua** FVG giảm. Khi đó FVG đã bị "disrespect" và thành IFVG, dấu hiệu cho thấy DOL đã dời ra ERL.

**Bài học:** sau khi một ERL khung lớn bị quét, đích đầu tiên là IRL. Giữ lệnh chờ đỉnh xa theo quán tính chính là lỗi trong lệnh NDX ngày 27/04 của bạn: lệnh đã đạt +2.63R tại FVG, nhưng vẫn được giữ để chạy tới đỉnh cũ (5.61R), rồi dính stop ở **−1.34R**.

### Bullish 3 — XAUUSD: NWOG là DOL (IRL) sau cú quét đáy thứ Sáu

**T0 — Bối cảnh:**

- Thứ Sáu đóng cửa ở 3,050.0. Chủ nhật mở cửa ở 3,038.0, tạo ra **NWOG 3,038–3,050** (CE 3,044).
- High thứ Sáu là 3,062 (PDH). Low thứ Sáu là 3,028. ATR D1 ≈ 40.

**T1 — Phiên Á thứ Hai:** giá giảm xuống 3,026, quét đáy thứ Sáu 3,028 (SSL).

**T2 — London:** một cú displacement tăng đưa giá lên 3,041, tức đã lọt vào NWOG, và để lại FVG M5 3,029–3,033.

**Thẻ DOL (lúc London mở cửa, giá quanh 3,033):**

- DOL = đỉnh NWOG 3,050, cách +17. Đối thủ = đáy vừa tạo 3,026, cách −7.
- **Baseline chỉ 29%**, vì DOL xa gấp khoảng 2.4 lần đối thủ.
- Bằng chứng: SSL đã bị lấy, có displacement tăng, NWOG là IRL chưa được lấp, bối cảnh tuần đang tăng.
- Kết luận: Tier B, vì thiếu một cú displacement phá swing cấu trúc trên H1.

**T3–T4 — Lệnh:**

- Entry 3,031 (CE của FVG M5). SL 3,024 (dưới đáy sweep 2.0), rủi ro 7.0.
- T1 = 3,049.5 (ngay dưới đỉnh NWOG) → **2.64R**.
- T2 = 3,061 (ngay dưới PDH) → **4.29R**.

**Bài học:**

- "Gap sẽ được lấp" là một giả thuyết cần backtest, không phải một định luật.
- Gap cuối tuần trên CFD vàng phụ thuộc vào feed của broker. Hợp đồng GC giao dịch gần như liên tục nên gap có thể khác. Hãy kiểm tra feed trước khi coi NWOG là một mức giá thật.
- Với baseline chỉ 29%, lệnh này chỉ có edge nếu backtest của bạn cho thấy tổ hợp "SSL bị quét + displacement + gap chưa lấp" thật sự vượt baseline.

Hình dưới vẽ ba ví dụ bullish ở dạng sơ đồ. Mỗi hình gồm DOL, các bậc thang, POI/IRL và pool bị quét làm nhiên liệu.

![[DOL-TongHop-09-Vi-Du-Bullish.svg|1516]]
*Hình 9 — Ba ví dụ bullish (mức giá là số minh họa).*

Điểm chung của ba ví dụ bullish: **lệnh không bao giờ vào ngay tại DOL, cũng không vào trước khi pool "nhiên liệu" ở phía ngược lại bị lấy**. DOL chỉ cho biết đích; chỗ lên tàu là POI hoặc IRL sau khi đối thủ ở gần đã bị loại bỏ.

### Bearish 1 — GBPUSD: quét EQH và đỉnh 60 ngày, đâm vào POI premium tuần, rồi DOL lật xuống

**T0 — Bối cảnh D1:**

- Hai đỉnh D1 ở 1.3446 và 1.3450 chỉ cách nhau 4 pip (khoảng 0.05 ATR), nên được coi là **EQH**. Mức này cũng trùng đỉnh 60 ngày.
- Ngay phía trên là **FVG giảm W1 1.3470–1.3510**, một POI premium của khung lớn.
- ATR D1 khoảng 80 pip.
- Cộng lại, đây là một "kệ thanh khoản" 3 lớp: EQH, đỉnh 60 ngày, và POI tuần.

**Ngày X:** giá chạy lên 1.3482, quét qua EQH 32 pip và lọt vào FVG tuần. Sau đó nến D1 đóng cửa ở **1.3418**, tức đã nằm dưới EQH, với một thân nến giảm lớn (displacement). Cú giảm này để lại một FVG giảm trên H4 ở 1.3430–1.3445.

**Thẻ DOL:**

- DOL gần = **FVG tăng D1 1.3320–1.3350** (IRL). DOL xa = higher low D1 ở 1.3300 (ERL).
- Đối thủ = đỉnh vừa bị quét ở 1.3482. Khoảng cách tới DOL là 68 pip, tới đối thủ là 64 pip, nên baseline chỉ **48.5%**.
- Horizon: 2 ngày.
- Invalidation: nến D1 đóng cửa trên 1.3450, nghĩa là giá đã được chấp nhận trên EQH. Khi đó DOL dời lên đỉnh FVG tuần ở 1.3510.

**T1–T3 — Ngày hôm sau:** giá hồi lên trong phiên London. Sang NY AM, giá quét high London (1.3436) lên tới 1.3441, lọt vào FVG H4, rồi M5 xuất hiện MSS giảm.

**T4 — Lệnh:**

- Entry 1.3428. SL 1.3448. Rủi ro 20 pip.
- T1 = 1.3353 → **3.75R**.
- T2 = 1.3303 → **6.25R** (phần runner).

**Bài học về "độ hiển nhiên":** đây đúng là loại EQH mà ai cũng thấy. Nhưng thứ quyết định không phải là mức đó hiển nhiên đến đâu, mà là **giá phản ứng thế nào** ở đó: nến đóng cửa quay lại dưới kệ, có displacement, và có POI khung lớn nằm ngay phía trên. Nếu nến D1 đóng cửa trên 1.3450, thì chính mức EQH hiển nhiên ấy lại trở thành bằng chứng cho một cú run.

### Bearish 2 — NQ: tiếp diễn giảm trên đường LRLR, nhưng phải chờ PDH bị quét trước

**T0 — Bối cảnh:**

- D1 đang giảm. Giá phá xuống dưới 26,600 (BOS) bằng displacement, để lại FVG giảm D1 26,750–26,880.
- Thứ Năm, giá hồi lên retest FVG này (high 26,840) và bị đẩy xuống.
- Thứ Sáu đóng cửa ở 26,560. PDH là 26,700.
- Phía dưới có **EQL 26,205/26,198**, tức một cụm đáy bằng nhau quanh 26,200.
- Giữa giá và EQL chỉ có hai swing H1 nhỏ ở 26,480 và 26,410 (đóng vai bậc thang). Không có PD array tăng nào trên D1 chắn đường, nên đây là **đường LRLR**.

**Thẻ DOL — chỗ nhiều người tính sai:**

- DOL = EQL 26,200, cách giá −360. Đối thủ = PDH 26,700, chỉ cách +140. Vì vậy baseline chỉ **28%**.
- Trong mô hình ngẫu nhiên, sau 5 ngày PDH có khoảng 80% khả năng đã bị chạm, còn EQL chỉ khoảng 52%.
- Kết luận: **short ngay lúc mở cửa nghĩa là đặt cược vào một đích xa, trong khi đối thủ gần hơn tới 2.6 lần.** Kế hoạch đúng là để đối thủ bị loại trước: chờ PDH bị quét (Judas ở NY AM), rồi mới short từ vùng premium.

**T1–T3 — NY AM thứ Hai:** giá lên tới **26,705**, quét qua PDH 5 điểm và lọt vào FVG giảm H1 26,680–26,720. Sau đó M5 xuất hiện MSS giảm, phá higher low 26,650 bằng displacement.

**T4 — Lệnh:**

- Entry 26,662. SL 26,725, cao hơn đỉnh sweep 20 điểm. Rủi ro 63 điểm.
- T1 = 26,488, ngay trước swing 26,480 → **2.76R**.
- T2 = 26,212, ngay trước EQL → **7.14R**.

**Bài học:** có DOL không có nghĩa là có lệnh. Cùng một DOL, nếu vào lệnh trước khi đối thủ ở gần bị loại, bạn đang chơi một bài toán 28%. Nếu vào sau khi PDH đã bị quét, đó là một bài toán khác hẳn, vì SL lúc này nằm trên một vùng thanh khoản **đã** bị lấy.

### Bearish 3 — XAUUSD: sau khi lấy PWH, DOL là IRL. Chốt ở IRL, đừng tham đáy

**T0 — Bối cảnh:** tuần đang tăng. PWH ở 3,110. FVG tăng trên H1 được tạo từ thứ Hai, **3,070–3,080** (CE 3,075), vẫn chưa được lấp.

**T1–T2 — NY AM thứ Ba:** giá quét PWH lên tới 3,118. Sau đó có displacement giảm, và M5 xuất hiện MSS giảm.

**Thẻ DOL (lập trong phiên):**

- DOL = IRL, tức FVG trên H1.
- Đối thủ = đỉnh mới 3,118, cách +10. Đỉnh FVG cách −27.5. Vì vậy baseline chỉ **27%**.
- Đây là lệnh **ngược khung lớn**, vì cấu trúc tuần vẫn đang tăng.
- Quy tắc cho loại lệnh này: rủi ro chỉ còn một nửa (0.25%), chỉ đặt T1/T2 tại IRL, **không để runner**.

**T3–T4 — Lệnh:**

- Entry 3,108. SL 3,121. Rủi ro 13.
- T1 = 3,080.5 → **2.12R**.
- T2 = 3,075.5, ngay trước CE → **2.5R**.

**Khi nào DOL được dời xa hơn?** Chỉ khi nến H1 đóng cửa **xuyên qua** FVG kèm displacement, tức FVG bị "disrespect" và trở thành IFVG. Lúc đó ERL phía dưới mới trở thành ứng viên. Nhưng đó là **một quyết định mới**, không phải lý do để tiếp tục giữ lệnh cũ.

**Bài học:** sau khi một ERL bị lấy, IRL là đích tự nhiên. Tham đáy tuần khi cấu trúc tuần đang tăng sẽ biến một lệnh hồi hợp lệ thành một lệnh đánh ngược xu hướng.

![[DOL-TongHop-10-Vi-Du-Bearish.svg|1516]]
*Hình 10 — Ba ví dụ bearish (mức giá là số minh họa).*

Chú ý ví dụ S2: hình vẽ cố tình cho giá **đi lên quét PDH trước**. Đó là bước mà trader vào lệnh sớm hay bỏ qua, và cũng là bước biến một bài toán 28% thành một setup có cấu trúc.

---

## 8. Counterexamples

Mỗi counterexample dưới đây nhìn rất giống một setup đúng. Bốn trường hợp đầu là **case thật lấy từ vault của bạn**.

### C1 — Đúng đích, sai đường: SL nằm ngay trên một đáy cũ chưa bị quét

*Live, NDX, 29/04/2026, Long* — [[Loss - 01 - Trade 2026-04-29 NDX Long]]

**Dữ liệu đã ghi:**

- Entry 27,091.6, SL 27,058.6 (rủi ro 33 điểm), TP 27,167.6 (**2.3R**).
- Phiên London có một Judas swing giảm.
- Note ghi lại: "Giá quét OB và sâu xuống bên dưới đáy cũ trước đó (27016)" → "Stop loss của lệnh bị quét sau đó giá đảo chiều" → "Giá đi đúng hướng và chạm TP ở vùng London Overlap với New York".

**Phân tích:**

- DOL (chính là TP) **đúng**. Vấn đề là đáy cũ 27,016, một pool chưa bị quét, nằm **dưới SL 42.6 điểm**. Pool chưa quét gần nhất lại nằm về phía SL, nên theo chính Mistake 13 đây là NO-TRADE.
- Dời SL xuống dưới 27,016 có cứu được lệnh không? Không. Đặt SL ở 27,006 thì rủi ro tăng lên 85.6 điểm, R:R tụt còn **0.89**, và lệnh vẫn phải bỏ.
- Cách làm đúng duy nhất: **chờ 27,016 bị quét xong**, rồi mới đánh giá lại điểm vào.

**Kết luận:** đây không phải "thị trường giăng bẫy". Đây là một thứ tự delivery hoàn toàn đọc được: nhiên liệu phía dưới bị lấy trước, sau đó giá mới đi tới đích.

### C2 — Bias đúng, nhưng DOL ngắn hạn sai

*Backtest, EURUSD, 2021-05-07, Short, phiên Á* — [[02 - Loss- EURUSD - 2021-05-07- Short]]

**Dữ liệu đã ghi:**

- `htf_bias: Bearish` và `bias_correct: Yes`, nhưng `step2_draw_ok: No` và `first_error_step: draw`.
- Note ghi: "Short-term draw thực tế đang hướng lên (buy-side 1.21296–1.21227 chưa bị lấy)". Chỉ cần một nến bullish displacement trong phiên thanh khoản mỏng là giá đã chạy xuyên OB và SL để lấy phần buy-side này.

**Phân tích:** đây là xung đột giữa hai tầng DOL. DOL của phiên (BSL phía trên) phải được giao **trước** DOL khung lớn (phía dưới). Setup nhìn rất giống Bearish 1: POI ở premium, bias đúng. Nhưng nó thiếu đúng một điều kiện: **pool ở phía ngược lại chưa bị lấy**.

### C3 — MSS mồi: POI nằm sát "móng nhà", SSL cấu trúc vẫn còn nguyên

*Backtest, GBPUSD, 2014-07-17, Long, −1R, tag `good-loss`* — [[02 - Loss - GBPUSD - 2014-07-17 - Long]]

**Dữ liệu đã ghi:**

- POI là một FVG có cạnh dưới 1.70873, chỉ cách đáy range 1.70592 khoảng 28 pip. Giữa hai mức không có EQL hay swing nội bộ nào.
- MSS M5 lúc 19:15 xuất hiện khi SSL cấu trúc **chưa** bị quét.
- Sau đó giá "quét mạnh qua SL" rồi "xuyên thủng cả dealing range low".

**Phân tích:** DOL ngắn hạn thực sự là SSL cấu trúc ở bên dưới. MSS M5 chỉ phá một swing nội bộ, đúng như chính note đã kết luận: "rất dễ là LTF inducement". Tag `good-loss` hợp lý nếu xét **kỷ luật**. Nhưng nếu xét **cách đọc DOL** thì đây là lỗi tránh được.

### C4 — Đã tới IRL rồi nhưng vẫn giữ lệnh chờ ERL

*Live, NDX, 27/04/2026, Long, −1.34R* — [[Loss - 01 - Trade 2026-04-27 NDX Long]]

**Dữ liệu đã ghi:**

- "Tuy nhiên giá chưa quét swing low cũ."
- Lệnh đã đạt **2.63R** tại FVG, nhưng "do tham nên vẫn để giá chạy đến đỉnh cũ (1:5.61 RR)".
- Kết cục: "Hit stop loss sau khi không chốt lời ở FVG."

**Phân tích:** hai lỗi DOL chồng lên nhau.

1. Vào lệnh khi pool ở phía ngược lại chưa bị lấy (giống C1).
2. Nhầm tầng DOL. FVG là IRL, tức đích tự nhiên của nhịp đó. Đỉnh cũ ở xa (ERL) chỉ nên là mục tiêu của runner **sau khi** đã chốt phần lớn vị thế tại IRL.

### C5 — DOL đã được giao

*Giả định; vault chưa có case tương ứng*

**Tình huống:** thứ Ba, giá quét PWH rồi nến D1 đóng cửa quay lại dưới mức đó. Sang thứ Tư, bạn vẫn "mua dip để hướng tới BSL". Nhưng BSL tuần **đã tiêu**. Theo nguyên lý con lắc, đích lúc này là IRL ở phía dưới. Diễn biến điển hình: các nhịp bật lên đều nông, rồi thất bại dần.

**Dấu hiệu nhận biết:**

- giá đã giao dịch xuyên qua pool ít nhất τ;
- có displacement **đi ra xa** khỏi pool;
- các nhịp hồi sau đó không tạo được MSS tăng trên H1.

### C6 — Đường bị chặn (HRLR)

*Giả định*

**Tình huống:** DOL tăng là PWH. Nhưng giữa đường có một FVG giảm H4 còn mới, cộng với high London từng bị từ chối mạnh. Trên M5, sweep và MSS hình thành rất đẹp. Nhưng giá khựng lại đúng ở FVG H4 rồi đảo chiều.

**Quy tắc:** đo R:R tới **vật cản chặn đường đầu tiên**, không đo tới PWH. Nếu R:R đó nhỏ hơn 2 thì bỏ lệnh, hoặc đặt T1 ngay trước vật cản và chấp nhận R nhỏ.

### Bẫy khi DOL trở nên phổ biến: 8 bẫy, cơ chế, và cách phòng tránh

Note 38 của bạn liệt kê 6 "kỹ thuật Smart Money". Bảng dưới viết lại các bẫy đó theo hướng **không cần giả định ai có ý đồ gì**. Mỗi bẫy có một cơ chế cơ học, dấu hiệu sớm, cách tránh, và một biến để đo.

| # | Bẫy | Cơ chế (không cần ý đồ) | Dấu hiệu sớm | Cách tránh | Biến để đo |
|---|---|---|---|---|---|
| T1 | Đúng đích, sai đường (vào lệnh quá sớm) | Stop của những người vào sớm tạo thành pool mới gần nhất | Có pool chưa quét nằm giữa entry và SL; chưa vào killzone | Qua cổng Mistake 13; chờ sweep phía ngược trong killzone | `unswept_pool_sl_side` |
| T2 | Sweep của sweep | Stop tụ ngay dưới râu nến sweep, tạo ra một pool mới rất hiển nhiên | Cú sweep đầu nông (< 0.1 ATR); displacement yếu | Đặt SL cách râu ít nhất 0.1–0.2 ATR rồi tính lại size; hoặc chờ sweep kép | MAE của các lệnh thắng, đo từ râu |
| T3 | TP bị front-run | TP tụ đúng tại EQH/PDH, tạo thành bức tường lệnh ngay dưới mức | Giá chậm lại khi còn cách mức khoảng 0.1 ATR | Đặt TP trước mức 0.05–0.1 ATR; chốt lời từng phần | `dol_near_miss` |
| T4 | MSS mồi | MSS chỉ phá một swing nội bộ, trong khi pool khung lớn còn nguyên | MSS không nằm ở POI khung lớn; swing bị phá quá nhỏ | Chỉ tính MSS phá swing cấu trúc tại POI, sau khi đã quét một pool có ý nghĩa | `mss_swing_level` (internal/structural) |
| T5 | DOL đã tiêu | Đích đã bị lấy nhưng đám đông vẫn giao dịch theo quán tính | Pool đã bị xuyên ≥ τ; có displacement đi ra xa | Cập nhật trạng thái DOL; không mở lệnh mới hướng tới một DOL đã tiêu | `dol_state_at_entry` |
| T6 | Tin tức quét cả hai đầu | Tin mới làm giá được định giá lại; spread giãn, stop bị trượt giá | Có tin tier-1 trong vòng 15 phút | Không mở lệnh mới trong khoảng từ 10 phút trước tới 15 phút sau tin [HEURISTIC]; chờ cấu trúc hình thành sau tin | `news_window` |
| T7 | Ảo giác thống kê | Chọn pool gần nhất và không đặt horizon, nên "độ chính xác" cao nhưng EV = 0 | Hit rate cao nhưng R:R < 1 | Luôn ghi đối thủ và horizon; so kết quả với baseline | `baseline_p`, `edge` |
| T8 | Tự kể chuyện sau khi thua (hindsight) | Thua xong lúc nào cũng tìm được lý do "smart money bẫy tôi" | Lời giải thích chỉ xuất hiện sau khi thua | Phân loại lỗ ngay từ đầu: lỗi quy trình / thua hợp lệ / mô hình sai | `loss_class` |

**Ba điểm cần nói thẳng:**

1. **Về T2 và "sweep kép".** Vault có 4 lệnh thắng nhờ sweep kép: NAS100 2026-04-02 (+2.89R), EURUSD 2016-06-12 (+2.49R), EURUSD 2016-11-30 (+2.09R), EURUSD 2005-04-13 (+2.78R). Nhưng 4 lệnh thắng mà không có nhóm đối chứng thì **chưa phải bằng chứng**. Đây cũng chính là lý do [[CS-01 - Ho loi Trading Into Unswept Liquidity]] của bạn đánh giá Mistake 13 là UNSUPPORTED: thiếu nhóm lệnh thắng để so sánh.
2. **Về T8.** Trong backtest XAUUSD 2014-05-19 ([[01 - Loss - XAUUSD - 2014-05-19 - Short]]), mục 9 giải thích lệnh thua bằng câu "bạn chọn đúng cái POI mà thuật toán *muốn* đám đông chọn". Đây là một khẳng định về ý đồ, và nó được viết **sau khi** đã thua. Nghe thì sâu sắc, nhưng không dạy được gì, vì câu đó giải thích được mọi kết quả.
3. **Về "nguyên tắc vàng" trong [[Anti-Crowd-Trap Checklist (Chống bẫy đám đông ICT)]].** Câu "setup càng đẹp sách vở… xác suất là bẫy càng cao" chưa từng được kiểm định, và còn mâu thuẫn với phần D1/C5 của chính note 38.

   Đề xuất cho v0.2: **chỉ bắt buộc thêm lớp xác nhận chống bẫy khi có điều kiện khách quan**, không phải khi setup trông "đẹp". Các điều kiện đó là:
   - (a) có pool chưa quét nằm trong phạm vi 0.5 ATR H1 phía sau SL;
   - (b) cú sweep đầu nông hơn τ;
   - (c) lệnh rơi vào cửa sổ tin tức.

   Điểm "độ hiển nhiên" vẫn nên được **ghi lại** như một biến (HYP-DOL-008), để dữ liệu tự trả lời. Hiện có 0 trade hay backtest nào tham chiếu checklist này. Nếu muốn giữ nó, bạn phải thực sự dùng và đo nó.

Hình dưới tóm tắt 6 bẫy có hình dạng đặc trưng trên chart. T7 và T8 là bẫy về thống kê và tâm lý nên không vẽ được.

![[DOL-TongHop-11-Bay-Pho-Bien.svg|1516]]
*Hình 11 — Sáu bẫy có hình dạng đặc trưng trên chart.*

Có một điểm chung trong cả 6 khung trên: **thanh khoản của chính bạn** (stop, entry, TP) là thứ dễ bị lấy nhất ở bước tiếp theo. Tránh bẫy không có nghĩa là đoán được ý đồ của ai, mà là **đừng đứng ở chỗ đó**.

---

## 9. Edge Cases

**Nói đơn giản:** phần lớn các tình huống "khó" đến từ ba nguồn: (1) giá chỉ chạm hay đã thật sự xuyên qua mức; (2) mức giá được đo bằng dữ liệu nào (feed, hợp đồng, định nghĩa nến ngày); (3) thị trường lúc đó có đủ thanh khoản để mọi thứ còn ý nghĩa hay không.

| # | Edge case | Vì sao khó | Cách xử lý |
|---|---|---|---|
| 1 | **Chạm không phải là quét:** giá chạm EQH 3 lần nhưng không vượt qua | Note 39 nói chạm nhiều lần làm pool "cạn". Note 52/53 nói pool "dày lên". Cả hai đều đúng một phần | Khi giá chỉ chạm mà không xuyên qua, stop phía trên **không** bị kích hoạt, nên vẫn còn nguyên và còn tích thêm. Thứ bị bào mòn là **lệnh limit đang phòng thủ** tại mức đó. Vì vậy càng chạm nhiều lần, khả năng mức bị phá càng cao [HYPOTHESIS HYP-DOL-009] |
| 2 | **Quét một phần:** giá xuyên 2 pip rồi quay lại | Stop đặt sát mức đã bị kích hoạt; stop đặt xa hơn vẫn còn | Pool "đã tiêu" khi giá xuyên ≥ τ (gợi ý: 0.1 ATR của khung chứa mức). Nếu xuyên chưa tới τ thì là "tiêu một phần": vẫn là DOL nhưng yếu hơn. Cách này giải được mâu thuẫn giữa note 52 và 53 |
| 3 | **Gap nhảy qua mức** (cuối tuần, lúc ra tin) | Pool "bị lấy" dù không có giao dịch nào tại mức đó; stop khớp tại giá gap | Coi như pool đã được giao. Bản thân gap trở thành một IRL mới (NWOG/NDOG) |
| 4 | **Sweep biến thành run** | Vài nến đầu nhìn giống hệt nhau | Xét nến đóng cửa **ở đúng khung của mức**: mức D1 cần xét close D1/H4, không phải close M1. Giá được coi là chấp nhận bên kia mức khi có ≥ 2 close bên ngoài, hoặc 1 close kèm displacement [HEURISTIC] |
| 5 | **Kệ thanh khoản:** PDH, EQH và số tròn nằm trong phạm vi 0.15 ATR | Nhiều pool chồng nhau nên có nhiều cách trả lời | Gộp lại thành một mục tiêu. Kỳ vọng phản ứng mạnh hơn, dù giá quét qua hay phá qua |
| 6 | **Feed khác nhau** (FX/CFD) | Hai đỉnh "bằng nhau" trên broker này có thể lệch 3 pip trên broker khác | Dùng dung sai tính theo ATR, không đòi "bằng tuyệt đối". Backtest và live phải dùng cùng một feed |
| 7 | **Định nghĩa nến ngày** | PDH tính theo mốc 17:00 NY, theo 00:00 NY và theo phiên RTH là ba con số khác nhau | Chọn một định nghĩa và ghi vào thẻ DOL. Test xem kết quả nhạy thế nào khi đổi định nghĩa |
| 8 | **Roll hợp đồng NQ** (tháng 3/6/9/12, khoảng 1 tuần trước thứ Sáu tuần thứ ba của tháng) | Trên chart liên tục chưa điều chỉnh, PWH/PDH trước khi roll bị lệch so với hợp đồng mới. Chênh lệch giữa hai kỳ hạn có thể lên tới hàng trăm điểm khi lãi suất cao | Vẽ các mức trên đúng hợp đồng đang giao dịch. Trong tuần roll thì hạ tier |
| 9 | **Thanh khoản mỏng** (phiên Á, ngày lễ, ngay trước tin) | Sweep "rẻ", ai cũng quét được. Sự kiện đồng bảng Anh ngày 07/10/2016 xảy ra đầu phiên Á; BIS nhấn mạnh vai trò của thời điểm trong ngày và các "bộ khuếch đại cơ học" như hedging quyền chọn ([BIS](https://www.bis.org/publ/mktc09.htm)) | Nếu phiên London/NY không đi tiếp theo hướng đó, đừng coi cú sweep mức khung lớn trong phiên Á là xác nhận |
| 10 | **Cả hai phía bị lấy trong cùng một ngày** (outside day, seek & destroy) | DOL mất khả năng dự báo | Khi phía thứ hai đã bị lấy, dừng tìm setup cho tới khi có cấu trúc mới |
| 11 | **Xung đột giữa hai thị trường** (NQ lấy BSL nhưng ES thì không) | Không rõ nên theo DOL của thị trường nào | Theo DOL của thị trường bạn đang giao dịch. SMT chỉ dùng để phá thế hòa |
| 12 | **Pool nằm ngay tại POI khung lớn** | Pool vừa là đích, vừa là điểm đảo chiều | Cú quét pool chính là điểm vào lệnh (Turtle Soup) |
| 13 | **Phiên mở cửa khi giá đang nằm trong FVG** | IRL đang được giao dở dang | DOL gần là CE hoặc mép còn lại của FVG. Không giao dịch ở giữa FVG |
| 14 | **Ngày đáo hạn quyền chọn (OPEX) hoặc giá đang ở gần một strike lớn** | Có thêm một "nam châm" khác: hoạt động hedging quyền chọn có thể ghim giá quanh strike. Hiện tượng pinning đã được ghi nhận ở cổ phiếu ([Ni, Pearson & Poteshman 2005](https://www.sciencedirect.com/science/article/abs/pii/S0304405X05000577)) và ở S&P 500 futures ([Golez & Jackwerth 2012](https://ideas.repec.org/a/eee/jfinec/v106y2012i3p566-585.html)) | Trong ngày đáo hạn, đừng giải thích mọi chuyển động bằng BSL/SSL |

### Khi nào KHÔNG nên áp dụng DOL

1. **Không có dealing range rõ ràng:** giá đang nén, pool ở hai phía cách đều nhau, không có displacement.
2. **Trong cửa sổ tin tier-1** (CPI, NFP, FOMC) và vào các ngày ngân hàng trung ương họp. Một cú sốc thông tin làm bản đồ thanh khoản mất hết ý nghĩa. Ví dụ cực đoan: ngày 15/01/2015, khi SNB bỏ mức sàn của EURCHF, stop bị khớp ở những mức giá rất xa, và không có DOL nào còn ý nghĩa.
3. **Ngày lễ, phiên rút ngắn, phiên thanh khoản mỏng.**
4. **Sau khi cả hai phía đã bị lấy** trong ngày.
5. **DOL nằm ngoài tầm với của horizon**, ví dụ cách hơn 1.5 ATR trong khi horizon chỉ là một ngày.
6. **Lý do duy nhất để vào lệnh là "có DOL"**, trong khi không có POI và không có trigger.
7. **Không xác định được mức giá một cách nhất quán**, ví dụ các feed cho số khác nhau, hoặc dữ liệu backtest lệch múi giờ server.
8. **Thị trường đang chịu chi phối bởi một cơ chế khác:** cổ phiếu quanh ngày báo cáo lợi nhuận, crypto với các chuỗi thanh lý đòn bẩy, hoặc những ngày giá bị ghim quanh strike vào dịp OPEX.

---

## 10. Common Mistakes

**Nói đơn giản:** gần như mọi lỗi với DOL đều rơi vào một trong ba nhóm: (1) coi dự báo là chắc chắn, (2) đo sai (không có đối thủ, không có horizon, dữ liệu không nhất quán), và (3) vào lệnh ở chỗ mà thanh khoản của chính mình sẽ bị lấy tiếp theo.

| # | Lỗi | Vì sao sai | Cách sửa | Liên kết vault |
|---|---|---|---|---|
| 1 | Coi DOL là chắc chắn ("giá phải về đó") | DOL chỉ là một xác suất, và có hạn giờ | Luôn ghi đối thủ, horizon và invalidation | — |
| 2 | Chọn pool **gần nhất** làm DOL | Cho khoảng 63% "độ chính xác" giả trong khi EV = 0 | So với baseline b/(a+b) | — |
| 3 | Dùng bias để chọn DOL, rồi dùng DOL để xác nhận bias | Lập luận vòng tròn, nên không bao giờ sai | Dựng bản đồ và xác định trạng thái một cách độc lập; bias chỉ là kết quả đầu ra | [[09-Mistake-Wrong-daily-bias]] |
| 4 | Coi mọi DOL là ERL | Ngay sau khi ERL bị lấy, đích gần nhất là IRL | Hỏi "bên nào vừa bị lấy?" | — |
| 5 | Không cập nhật một DOL đã tiêu | Vẫn trade hướng về một đích đã được giao | Theo dõi trạng thái: projected → active → delivered → spent/flip | — |
| 6 | Coi mọi cú xuyên qua mức là sweep | Có sweep, nhưng cũng có run | Xét close theo khung của mức, kèm displacement | [[20-Liquidity-Sweep]] |
| 7 | Vào lệnh khi còn pool chưa quét nằm phía SL | "Đúng đích, sai đường" (C1, C4) | Áp dụng cổng Mistake 13 | [[13-Mistake-Trading-Into-Unswept-Liquidity]], [[02-Mistake-Enter-before-liquidity-sweep]] |
| 8 | MSS trên M5 ngược với DOL khung lớn, hoặc nằm ngoài POI | MSS mồi (C3) | MSS phải phá một swing cấu trúc tại POI | [[03-Mistake-Entry-When-MSS-not-in-POI-Zone]] |
| 9 | Đếm sweep, MSS, displacement và FVG thành 4 điểm riêng | Đây là một chuỗi nhân quả nhưng bị tính 4 lần | Chỉ đếm các nhóm bằng chứng độc lập với nhau | — |
| 10 | Đo R:R tới DOL xa mà bỏ qua vật cản | HRLR làm lệnh chết giữa đường | Đo R:R tới vật cản chặn đường đầu tiên | [[05-Mistake-Not-enough-RR]] |
| 11 | Đặt TP đúng tại mức, đặt SL ngay dưới râu | Dính front-run và sweep của sweep | Chừa buffer theo ATR, rồi tính lại size | — |
| 12 | Dùng ngưỡng cố định bằng pip/điểm (ví dụ "10 pips") | Không cùng quy mô giữa các thị trường và giữa các giai đoạn biến động | Chuẩn hóa theo ATR | — |
| 13 | Nhầm giờ killzone khi Mỹ đổi giờ | Lệch 1 tiếng | Dùng bảng quy đổi EDT/EST | [[18-Kill-Zones]] |
| 14 | Vẽ mức trên một feed hoặc hợp đồng khác với lúc giao dịch | PDH/PWH bị sai | Dùng một feed, một hợp đồng, một định nghĩa ngày | — |
| 15 | Gọi mọi lệnh thua là "bị bẫy" | Không rút ra được bài học nào | Phân loại lệnh thua ngay từ đầu | — |
| 16 | Giữ runner trong lệnh ngược khung lớn | Biến một lệnh hồi thành lệnh ngược xu hướng | Lệnh ngược khung lớn: nửa rủi ro, chỉ nhắm IRL, không để runner | — |

---

## 11. Decision Rules

### 11.1 Bộ quy tắc DOL v0.2 (bản hợp nhất)

![[DOL-TongHop-12-Rule-Set-v0-2.svg|1516]]
*Hình 12 — Bản đồ bộ quy tắc DOL v0.2.*

**Bắt buộc (Required).** Thiếu một điều kiện là không có DOL:

- **R1** — Có dealing range rõ ràng và đã chốt cố định trước phiên.
- **R2** — DOL là một pool **chưa tiêu** (chưa bị xuyên ≥ τ), nằm ở khung ≥ khung dùng để xác định bias.
- **R3** — Đã ghi **đối thủ**, **horizon** và **invalidation** trước thời điểm khóa.
- **R4** — DOL nằm trong tầm với của horizon, tức ≤ 1.0–1.5 ATR D1 nếu horizon là 1–2 ngày [HEURISTIC].
- **R5** — Xác định được trạng thái con lắc (bên nào vừa bị lấy), hoặc ghi rõ "trạng thái 3: chưa có hướng".

**Hỗ trợ (Supporting).** Dùng để xếp tier:

- **S1** — Có displacement cấu trúc hướng về DOL.
- **S2** — Vị trí premium/discount thuận lợi cho entry.
- **S3** — Đường đi là LRLR.
- **S4** — Sắp tới có killzone và không có tin tier-1.
- **S5** — SMT (chỉ để phá thế hòa).

**Tier:**

- **A** = R1–R5 + S1 + (S2 hoặc S3), và không dính điều kiện loại trừ nào.
- **B** = R1–R5 + một trong S1/S2/S3.
- **C** = các trường hợp còn lại. Chỉ quan sát, không trade.

**Loại trừ (Disqualifying).** Dính một điều kiện là không trade:

- **D1** — Có pool chưa quét trong vòng 0.5 ATR H1 phía sau SL (cổng Mistake 13).
- **D2** — Đang trong cửa sổ từ 10 phút trước tới 15 phút sau một tin tier-1 [HEURISTIC].
- **D3** — Cả hai phía đã bị lấy trong ngày.
- **D4** — R:R tới vật cản chặn đường đầu tiên nhỏ hơn 2.
- **D5** — DOL đã tiêu.
- **D6** — Tuần roll hợp đồng (NQ) hoặc ngày lễ. Trường hợp này không loại hẳn, nhưng tối đa chỉ được tier B.

**Xác nhận (Confirmation) — trigger trên M5:** sweep ở phía ngược lại tại POI → MSS phá một swing cấu trúc, có displacement hướng về DOL → FVG. Đây là **một** chuỗi duy nhất. Thiếu bất kỳ mắt xích nào thì chưa có trigger.

**Vô hiệu (Invalidation):**

- Giá đóng nến ở khung của DOL và được chấp nhận theo hướng ngược lại, ví dụ nến H1/H4 đóng cửa xuyên qua POI và IRL kèm displacement.
- Xuất hiện MSS ở khung từ H1 trở lên, ngược hướng DOL.
- Tin tức làm thay đổi bối cảnh.

**Quản lý lệnh:**

- T1 đặt trước bậc thang đầu tiên.
- T2 đặt trước DOL.
- Chỉ giữ runner khi setup đạt tier A và đường đi là LRLR.
- Lệnh ngược khung lớn: rủi ro 0.25%, chỉ nhắm IRL, không giữ runner.

### 11.2 Bảng hòa giải OLD → NEW (theo quy ước versioning của bạn)

| Chủ đề | OLD (vault hiện tại) | NEW (v0.2) | Lý do | Hiệu quả kỳ vọng | Cần backtest? |
|---|---|---|---|---|---|
| Định nghĩa | Note 39: "vùng có mật độ lệnh chờ cao nhất". Note 52: "pool tiếp theo" | DOL là một dự báo gồm: mục tiêu, đối thủ, horizon, invalidation | Kiểm chứng được | Không còn kiểu DOL "lúc nào cũng đúng" | Có |
| Bias ↔ DOL | Note 52/53: DOL nuôi bias, nhưng lại chọn DOL theo hướng bias | Dựng bản đồ và trạng thái trước; bias là đầu ra | Phá vòng lập luận tròn | Bias sai sẽ lộ ra | Có |
| Pool gần hay xa | Note 52: pool gần nhất chưa quét là DOL. Deep-dive: pool bên ngoài (external) là DOL | T1 là bậc thang gần nhất; DOL là điểm kết thúc leg ở khung của bias | Hai vai trò khác nhau | Hết tranh cãi giữa T1 và DOL | Có |
| Có bắt buộc sweep phía ngược không? | Note 52/53: có. Deep-dive: không, với lệnh continuation | Lệnh reversal: bắt buộc. Lệnh continuation: thay bằng cổng "không có pool chưa quét phía sau SL" | Chức năng thật của sweep là dọn sạch pool phía sau SL | Giữ lại được các lệnh continuation hợp lệ | Có |
| Premium/discount | Note 52/53: cổng cứng quyết định hướng | Premium/discount chỉ lọc vị trí vào lệnh và R:R. Hướng đến từ con lắc và displacement | Premium/discount kéo ngược chiều với khoảng cách | Ít lệnh "đúng hướng nhưng sai chỗ" hơn | Có |
| Cách chấm điểm | Note 52: thang 5/8 điểm, tính MSS, displacement và FVG thành điểm riêng | Chỉ đếm các nhóm bằng chứng độc lập | Tránh đếm trùng | Tier phản ánh đúng hơn | Có |
| Pool bị chạm nhiều lần | Note 39: pool cạn dần. Note 52/53: pool dày lên | Chạm khác xuyên. Pool chỉ "tiêu" khi bị xuyên ≥ τ | Đúng với cơ chế của stop | Các note nhất quán với nhau | Có |
| Chống bẫy | Checklist: setup "đẹp" là bẫy, bắt buộc thêm lớp xác nhận | Chỉ bắt buộc khi dính D1, khi sweep nông, hoặc khi có tin. Độ hiển nhiên chỉ được ghi lại để đo | Tránh dùng một quy tắc chưa kiểm định | Ít bỏ lỡ lệnh tốt | Có (HYP-DOL-008) |
| Các ngưỡng | R:R 1.5 hay 2; cụm 10 pip; cửa sổ tin ±5/10/15/30 phút | R:R ≥ 2 tính tới vật cản; cụm 0.15 ATR; cửa sổ tin −10/+15 phút | Dùng một chuẩn duy nhất | Dễ đo | Có |

### 11.3 Cây quyết định DOL

![[DOL-TongHop-13-Cay-Quyet-Dinh.svg|1516]]
*Hình 13 — Cây quyết định DOL, từ dealing range đến lệnh.*

> [!note]- Bản text của cây quyết định (bấm để mở)
> ```
> Có dealing range rõ ràng (đã đóng băng)?
> ├─ KHÔNG → Không có DOL → không trade
> └─ CÓ → Map ≤3 pool mỗi phía (ERL + IRL), loại pool đã tiêu (xuyên ≥ τ)
>     │
>     ├─ Bên nào vừa bị lấy?
>     │   ├─ Chưa bên nào → trạng thái 3 → chờ cú raid đầu tiên
>     │   └─ Có → đóng nến quay lại (sweep)?
>     │         ├─ CÓ → DOL gần = IRL phía ngược; DOL xa = ERL đối diện
>     │         └─ KHÔNG (run) → DOL = pool kế tiếp cùng phía
>     │
>     ├─ Displacement cấu trúc hướng về DOL?   KHÔNG → tối đa tier B
>     ├─ Đường đi: HRLR → DOL = vật cản đầu tiên (hoặc bỏ) | LRLR → giữ
>     ├─ Trong tầm với horizon?   KHÔNG → đổi thành DOL tuần, dùng bậc thang
>     ├─ Tin tier-1 / ngày lễ / tuần roll?   CÓ → hạ tier hoặc đứng ngoài
>     │
>     └─ OUTPUT: DOL chính + thay thế + flip + invalidation + tier
>           └─ H1/M5: sweep phía ngược tại POI → MSS + displacement → FVG
>                 → Pool chưa quét phía sau SL?   CÓ → chờ    KHÔNG ↓
>                 → R:R tới vật cản đầu tiên ≥ 2?  KHÔNG → bỏ  CÓ → vào lệnh ≤ 0.5%
> ```

---

## 12. Quantification

**Nói đơn giản:** đừng hỏi "DOL của tôi đúng bao nhiêu phần trăm". Hãy hỏi: "DOL của tôi đúng **nhiều hơn** bao nhiêu so với một người chỉ dựa vào khoảng cách, trong cùng một khoảng thời gian?" Con số chênh lệch đó mới là edge.

### 12.1 Biến quan sát và ngưỡng đề xuất (tách riêng hai thứ này)

| Biến | Cách đo | Ngưỡng đề xuất [HEURISTIC — phải test] |
|---|---|---|
| `d_dol`, `d_opp` | Khoảng cách từ giá lúc khóa tới DOL và tới đối thủ, chia cho ATR(14) của khung chứa mức đó | DOL ngày ≤ 1.0–1.5 ATR D1 |
| `baseline_p` | d_opp / (d_dol + d_opp) | Không có ngưỡng; đây là mốc để so sánh |
| Loại và khung của pool | PDH/PWH/EQH/session/FVG/NWOG…; M15/H1/H4/D1/W1 | — |
| Tuổi và số lần chạm | Số nến kể từ khi pool hình thành; số lần giá chạm mà không xuyên qua | Từ 3 lần chạm trở lên thì theo dõi HYP-DOL-009 |
| τ (độ xuyên) | Phần giá đi vượt qua mức, tính theo ATR | Coi là "đã tiêu" khi ≥ 0.1 ATR |
| EQH/EQL | Hai swing cách nhau ≤ x ATR theo giá, và cách nhau ≥ m nến theo thời gian | x = 0.05–0.1; m = 5 |
| Kệ thanh khoản | Các pool nằm trong phạm vi 0.15 ATR của nhau | — |
| Trạng thái con lắc | Phía ERL bị lấy gần nhất; là sweep hay run; bao nhiêu nến đã trôi qua | — |
| Displacement cấu trúc | Thân nến ≥ 1.0 ATR (hoặc 2 nến liên tiếp ≥ 0.6 ATR), tạo FVG ≥ 0.1 ATR, và phá một swing cấu trúc | Xem note 50 |
| Vị trí | (giá − L) / (H − L) trong dealing range | < 0.5 là discount, > 0.5 là premium |
| Đường đi | Số PD array ngược chiều chưa được mitigate nằm giữa giá và DOL; vật cản chặn đường đầu tiên | Bằng 0 → LRLR |
| Thời gian | Phiên, ngày trong tuần, cờ tin tức | Cửa sổ tin −10/+15 phút |
| Độ hiển nhiên (0–4) | +1 nếu là EQH/EQL; +1 nếu trùng PDH/PDL/PWH/PWL hoặc high/low của phiên; +1 nếu có số tròn trong phạm vi 0.05 ATR; +1 nếu là chuỗi "sách giáo khoa" diễn ra trong killzone | Chỉ ghi lại, không dùng để lọc |

**Biến kết quả:**

- `dol_first`: +1 nếu DOL bị chạm trước; −1 nếu đối thủ bị chạm trước; 0 nếu hết horizon mà chưa mức nào bị chạm.
- Thời gian cho tới khi chạm.
- MAE trước khi chạm.
- Độ vượt (overshoot) qua DOL.
- Near-miss: nếu không chạm thì giá đã tới gần mức nhất là bao xa.
- Phản ứng sau khi chạm: giá có quay về IRL trong vòng N nến không?

### 12.2 Con số trung tâm: edge = tỷ lệ chạm trước − baseline

Chỉ tính trên những dự báo **đã được ghi lại trước** khi giá chạy. Nếu bạn gán xác suất cho dự báo (ví dụ tier A tương đương 60%), hãy đo thêm **Brier score** và **calibration**: những ngày bạn nói "60%", giá có thật sự chạm DOL trong khoảng 60% số ngày đó không?

**Horizon quan trọng đến mức nào?** Bảng dưới là xác suất giá chạm một mức cách d ATR trong vòng T ngày, theo mô hình ngẫu nhiên:

| d (ATR) | 1 ngày | 2 ngày | 5 ngày | 10 ngày | 20 ngày |
|---|---|---|---|---|---|
| 0.25 | 69% | 78% | 86% | 90% | 93% |
| 0.5 | 42% | 57% | 72% | 80% | 86% |
| 1.0 | 11% | 26% | 48% | 61% | 72% |
| 1.5 | 2% | 9% | 28% | 45% | 59% |
| 2.0 | ~0% | 2% | 15% | 31% | 48% |

![[DOL-TongHop-14-Xac-Suat-Cham-Theo-Horizon.svg|1516]]
*Hình 14 — Xác suất chạm mức theo khoảng cách và horizon (mô hình ngẫu nhiên).*

Cách đọc bảng:

- Câu "PWH sẽ bị lấy" mà không kèm horizon thì gần như chắc chắn đúng, miễn là chờ đủ lâu.
- Một mức cách 1 ATR bị chạm ngay trong ngày có baseline chỉ 11%. Nếu các dự báo DOL trong ngày của bạn ở khoảng cách đó chạm được 30%, **đó** mới là tín hiệu.
- Thị trường thật có đuôi dày, có xu hướng, và biến động dồn thành cụm. Vì vậy nên thay bảng này bằng **baseline thực nghiệm** tính từ chính dữ liệu của bạn: chọn các thời điểm ngẫu nhiên, rồi đo tỷ lệ chạm theo từng khoảng cách.

### 12.3 Thiết kế backtest

![[DOL-TongHop-15-Lo-Trinh-Nghien-Cuu.svg|1516]]
*Hình 15 — Lộ trình backtest A → D và các hàng rào chống sai lệch.*

**Nghiên cứu A — Chỉ dự báo, không vào lệnh:**

- Đơn vị là một ngày giao dịch. Đến giờ khóa (11:00 VN), điền thẻ DOL. Kết quả ghi lại là `dol_first` trong horizon.
- Dữ liệu: NQ, EURUSD, GBPUSD, XAUUSD, ít nhất 2 năm. Chia train/test theo thời gian.
- Chỉ số: tỷ lệ chạm, edge so với baseline, Brier score, thời gian tới khi chạm.
- Tách kết quả theo tier, theo trạng thái con lắc và theo phiên.

**Nghiên cứu B — Ablation (thêm dần từng lớp):**

1. Chỉ dùng khoảng cách.
2. Thêm trạng thái con lắc.
3. Thêm displacement.
4. Thêm vị trí premium/discount.
5. Thêm đường đi.
6. Thêm thời gian.

Chỉ giữ lại một lớp nếu nó cải thiện kết quả **ngoài mẫu**.

**Nghiên cứu C — Các bẫy:**

1. `unswept_pool_sl_side` (có/không) so với expectancy. Phải có **cả lệnh thắng lẫn lệnh thua**. Thiếu nhóm thắng chính là lý do CS-01 bị đánh giá UNSUPPORTED.
2. Buffer của SL: 0, 0.1 và 0.2 ATR. So sánh expectancy, không chỉ so win rate.
3. Near-miss của TP.
4. MSS cùng chiều khung lớn so với MSS ngược chiều khung lớn.
5. Điểm độ hiển nhiên (0–4) so với expectancy (HYP-DOL-008).
6. Các cửa sổ tin: ±5, ±10, ±15, ±30 phút.

**Nghiên cứu D — Vào lệnh thật theo mô hình:** so ICT 2022 **có** bộ lọc DOL v0.2 với ICT 2022 **không có** bộ lọc. Chỉ số: expectancy (R), profit factor, max drawdown, MAE/MFE, chuỗi thua dài nhất.

**Chống sai lệch:**

- **Nhìn trước tương lai (lookahead):**
  - Swing fractal k nến chỉ được xác nhận sau k nến.
  - FVG chỉ tồn tại sau khi nến thứ 3 đóng cửa.
  - EQH chỉ tồn tại sau khi đỉnh thứ 2 hình thành và giá đã rời đi.
  - Giá đóng cửa D1 chỉ có khi nến D1 đóng.
- **Hindsight:** điền thẻ DOL **trước** khi bấm play.
- **Chọn mẫu thiên lệch:** ghi lại **mọi** ngày, không chỉ những ngày có setup đẹp. Nếu backtest thủ công thì chọn ngày một cách ngẫu nhiên.
- **Dữ liệu:** dùng một feed, một định nghĩa ngày, và xử lý roll của NQ.
- **Kiểm định nhiều lần:** nếu thử 20 biến thể, khả năng có ít nhất một biến thể trông "có ý nghĩa" chỉ vì may mắn là **64%**. Giữ riêng một tập dữ liệu khóa lại và chỉ mở nó đúng một lần.

### 12.4 Cần bao nhiêu mẫu?

| Baseline | Edge muốn phát hiện | Số mẫu cần (α = 0.05 hai phía, power 80%) |
|---|---|---|
| 50% | +5 điểm % (lên 55%) | ~783 |
| 50% | +10 điểm % (lên 60%) | ~194 |
| 50% | +15 điểm % (lên 65%) | ~85 |
| 33% | +7 điểm % (lên 40%) | ~364 |
| 33% | +10 điểm % (lên 43%) | ~180 |

Khoảng tin cậy 95% (Wilson) khi tỷ lệ quan sát được là 60%:

- 12/20 → [39%, 78%]
- 18/30 → [42%, 75%]
- 60/100 → [50%, 69%], **vừa đủ** để loại trừ 50%
- 120/200 → [53%, 67%]

![[DOL-TongHop-16-Khoang-Tin-Cay-Wilson.svg|1516]]
*Hình 16 — Khoảng tin cậy Wilson: bao nhiêu mẫu thì đủ.*

Ý nghĩa thực tế: 30 lệnh không nói được gì về edge của DOL. Các con số 20–30 hay 30–50 mẫu trong note 38 và 43 chỉ đủ để phát hiện lỗi vận hành, chưa đủ để chứng minh edge.

### 12.5 Field đề xuất cho template backtest và trade (chưa sửa file nào)

```
dol_price, dol_type, dol_tf, dol_side, dol_distance_atr,
competitor_price, competitor_distance_atr, baseline_p, dol_horizon,
pendulum_last_taken (bsl|ssl|none), pendulum_mode (sweep|run),
dol_state_at_entry (projected|active|delivered|spent),
path (lrlr|hrlr), first_blocking_pool, unswept_pool_sl_side (Y/N),
obviousness (0–4), dol_first (1|-1|0), dol_time_to_hit_min,
dol_near_miss_atr, loss_class (process|valid|model)
```

Cần sửa thêm một chỗ quan trọng. Trong các note ở `05 - Live Trading Journal/Trades/`, trường `bias_correct` hiện có 11 giá trị "Bullish", phần còn lại để trống, và không có giá trị Yes/No nào. Trường `higher_timeframe_bias` thì có 12 giá trị "D1". Với dữ liệu hiện tại, **không thể đo từ các lệnh live xem bias hay DOL đúng hay sai**.

### 12.6 Hypothesis register

| ID | Giả thuyết | Bác bỏ nếu | Trạng thái |
|---|---|---|---|
| HYP-DOL-001 | DOL chính (đăng ký trước) bị chạm trước, với edge ≥ +8 điểm % so với baseline | CI 95% vẫn chứa 0 sau ≥ 200 ngày | UNTESTED |
| HYP-DOL-002 | Sau khi ERL bị sweep (xuyên ≥ τ rồi đóng cửa quay lại), IRL ở phía ngược lại bị chạm trước nhiều hơn baseline | Edge ≤ 0 | UNTESTED |
| HYP-DOL-003 | Dự báo cùng chiều với displacement cấu trúc có edge cao hơn dự báo không có displacement | Không khác biệt | UNTESTED |
| HYP-DOL-004 | Ở cùng khoảng cách, đường LRLR tới DOL nhanh hơn hoặc thường xuyên hơn đường HRLR | Không khác biệt | UNTESTED |
| HYP-DOL-005 | Có pool chưa quét trong phạm vi 0.5 ATR phía sau SL thì expectancy thấp hơn (cần cả lệnh thắng lẫn thua) | Không khác biệt | UNTESTED (CS-01: UNSUPPORTED vì thiếu nhóm đối chứng) |
| HYP-DOL-006 | Buffer SL ≥ 0.15 ATR làm tăng expectancy, dù R:R giảm | Expectancy không tăng | UNTESTED |
| HYP-DOL-007 | Đặt TP trước mức 0.05–0.1 ATR làm tăng R thực nhận | Không tăng | UNTESTED |
| HYP-DOL-008 | Điểm độ hiển nhiên càng cao thì expectancy càng thấp (giả thuyết "bẫy đám đông") | Expectancy bằng hoặc cao hơn | UNTESTED |
| HYP-DOL-009 | Mức bị chạm ≥ 3 lần mà không bị xuyên thì bị phá (run) nhiều hơn là đảo chiều | Không khác biệt | UNTESTED |
| HYP-DOL-010 | Bỏ các lệnh trong cửa sổ từ 10 phút trước tới 15 phút sau tin tier-1 giúp cải thiện expectancy | Không cải thiện | UNTESTED |

> [!tip] Tự kiểm tra kết quả của bạn
> Dùng công thức ở **Phụ lục A** để so tỷ lệ DOL của bạn với baseline, tỷ lệ thắng hòa vốn và khoảng tin cậy.

---

## 13. Final Mental Model

**Tóm lại trong một câu:** DOL là một dự báo có **đối thủ**, có **hạn giờ** và có **điểm sai**, về việc thanh khoản của *ai* sẽ bị lấy tiếp theo.

![[DOL-TongHop-17-Ban-Do-Vai-Tro.svg|1516]]
*Hình 17 — Bản đồ vai trò (Final Mental Model).*

**Năm câu hỏi cần thuộc lòng:**

1. Các bể thanh khoản nằm ở đâu, xét cả hai phía?
2. Bể nào còn nguyên?
3. Phía nào vừa bị lấy, và đó là sweep hay run?
4. Đường tới đích có thông không?
5. Horizon là bao lâu, và nếu sai thì sai ở đâu?

**Mỗi khái niệm giữ đúng một vai:**

| Khái niệm | Vai |
|---|---|
| DOL | Xác định **đích** |
| Con lắc ERL ↔ IRL | Xác định **thứ tự** giá đi qua các mức |
| Structure + displacement | Cung cấp **bằng chứng** |
| Premium/discount | Chọn **chỗ vào** lệnh (quyết định R:R), không cho biết hướng |
| Killzone / tin tức | Quyết định **hôm nay** có trade hay không |
| Cổng Mistake 13 | Quyết định **chỗ đặt stop** |
| Baseline b/(a+b) | Cho biết **sự thật** |

**Thế nào là bị "bẫy":** bạn bị bẫy khi chính thanh khoản của bạn (stop, entry, TP) là thứ dễ bị lấy nhất ở bước tiếp theo. Tránh bẫy không phải là đoán ý đồ của smart money, mà là **không đứng vào những chỗ đó**:

- không để một pool chưa quét nằm ngay sau SL;
- không đặt SL sát dưới râu nến;
- không đặt TP đúng tại mức giá;
- không trade theo một DOL đã được giao;
- không vào lệnh trong cửa sổ tin tức.

**Kết luận thẳng:** trong dữ liệu hiện tại của bạn, DOL vẫn là một giả thuyết có cấu trúc tốt chứ chưa phải một edge đã được chứng minh. Lý do: journal live chưa đo được nó (không có field DOL, và `bias_correct` đang chứa "Bullish" thay vì Yes/No). Bước có giá trị nhất lúc này là điền khoảng 200 thẻ DOL đăng ký trước trong Bar Replay (Nghiên cứu A), rồi dùng công thức ở Phụ lục A để so kết quả với baseline. Làm việc này sẽ đáng giá hơn viết thêm một note khái niệm nữa.

**Một câu hỏi để tự kiểm tra:** D1 đang tăng; tuần trước SSL đã bị quét và sau đó có displacement tăng; hôm nay giá nằm ở 45% range. PDH cách +0.4 ATR, PWH cách +1.4 ATR. Phía dưới, low phiên Á cách −0.2 ATR, và FVG D1 bắt đầu từ −0.35 ATR. Hãy viết thẻ DOL của bạn (DOL chính, T1, đối thủ, baseline, invalidation, tier). Sau đó cho biết sự kiện nào phải xảy ra **trước** thì bạn mới được phép long.

---

## Phụ lục A — Công thức để tự kiểm tra kết quả DOL (thay cho máy tính trong chat)

Dùng khi bạn đã ghi lại **trước** các dự báo DOL (mục 12.3, Nghiên cứu A) và muốn biết kết quả có thực sự vượt baseline hay không.

| Đại lượng | Công thức | Ghi chú |
|---|---|---|
| Khoảng cách | `a` = khoảng cách tới DOL, `b` = tới đối thủ (đơn vị ATR của khung chứa mức) | Ghi tại thời điểm khóa |
| Baseline | `b / (a + b)` | Xác suất DOL bị chạm trước nếu thị trường ngẫu nhiên |
| R:R | `RR = a / b` | TP tại DOL, SL tại đối thủ |
| Hòa vốn | `(1 + c) / (1 + RR)`, với `c` = phí tính bằng R | `c = 0` thì bằng đúng baseline |
| Xác suất chạm theo horizon | `2 · (1 − Φ(1.5958 · a / √T))` | Mô hình ngẫu nhiên; giả định 1 ATR ≈ 1.596σ ngày; T = số ngày; Φ = phân phối chuẩn tích lũy |
| Tỷ lệ quan sát | `p = k / n` | k = số lần DOL bị chạm trước, n = số dự báo |
| Khoảng tin cậy 95% (Wilson) | `centre = (p + z²/2n) / (1 + z²/n)`; `half = z·√(p(1−p)/n + z²/4n²) / (1 + z²/n)`; z = 1.96 | Không dùng xấp xỉ chuẩn khi n nhỏ |
| Edge | `p − baseline` | Tính bằng điểm phần trăm |
| Kỳ vọng mỗi lệnh | `EV = p·RR − (1 − p) − c` | Đơn vị R |
| Cỡ mẫu cần | `n ≈ ((1.96·√(b₀(1−b₀)) + 0.8416·√(p(1−p))) / (p − b₀))²` | α = 0.05 hai phía, power 80%, b₀ = baseline |

**Quy tắc kết luận:**

- Cận dưới của khoảng tin cậy **lớn hơn** max(baseline, hòa vốn) → có dấu hiệu edge (vẫn phải kiểm tra lại ngoài mẫu).
- Cận trên **nhỏ hơn** baseline → dự báo đang kém hơn việc chỉ dựa vào khoảng cách.
- Còn lại → **chưa chứng minh được edge**.

**Ví dụ tính tay** (số giả định để minh họa cách dùng): a = 1.0 ATR, b = 1.0 ATR, T = 2 ngày, phí c = 0.05R, n = 100 dự báo, k = 60.

| Đại lượng | Kết quả |
|---|---|
| Baseline | 50.0% |
| R:R | 1.00 |
| Hòa vốn (có phí) | 52.5% |
| Xác suất chạm trong 2 ngày (ngẫu nhiên) | 25.9% |
| Tỷ lệ quan sát | 60.0% |
| Khoảng tin cậy 95% | 50.2% – 69.1% |
| Edge | +10.0 điểm % |
| EV | +0.15R |
| Cỡ mẫu cần để phát hiện edge 10 điểm | ≈ 194 |

Kết luận của ví dụ: cận dưới 50.2% vượt baseline nhưng **chưa vượt mức hòa vốn 52.5%**, nên **chưa chứng minh được edge** sau khi tính phí. Đây là lý do 100 mẫu thường chưa đủ.

---

## Phụ lục B — Liên hệ với các note khác trong vault

Bảng này ghi những gì đã đọc được ở các note liên quan (không sửa file nào). Các điểm “cần sửa” được gom ở Phụ lục C.

| Note | Nó làm tốt | Điểm lệch so với note này |
|---|---|---|
| [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] | Đặt câu hỏi “ai là đối ứng” | Câu “buộc phải ĐẨY GIÁ” là nói quá; Case 1 (CHF 2015) mang nhãn “Thắng đẹp” dù chính nội dung nói đó không phải ví dụ DOL; cửa sổ tin không nhất quán với note khác |
| [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] | SOP đầu ngày, Rules 0–4 | Thang 5/8 điểm đếm trùng chuỗi sweep → MSS → displacement → FVG; “DOL nuôi bias” là lập luận vòng tròn; ví dụ NQ chỉ có 1.3R tới T1; quy đổi giờ VN chỉ đúng mùa đông |
| [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] | Heuristic con lắc | Ngưỡng “~10 pips/points” không chuẩn hóa theo ATR; nguồn trỏ tới research note không còn tồn tại |
| [[dol-ict-deep-dive]] | Định nghĩa vận hành và khung backtest tốt | Thiếu frontmatter; có 24 chú thích `[^n]` nhưng không có định nghĩa nào |
| [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] | Sáu “kỹ thuật Smart Money” và phần tự phê bình | Các case C2–C6 trông như case tổng hợp, chưa thấy dữ liệu gốc đi kèm |
| [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] | Ontology 4 tầng, epistemic ladder, failure model 3 lớp, decision tree 13 bước (theo phần giới thiệu của chính note) | **Chưa đối chiếu từng dòng** với note này; nên đọc song song khi hợp nhất quy tắc |
| [[Anti-Crowd-Trap Checklist (Chống bẫy đám đông ICT)]] | Hệ thống hóa các bẫy | “Nguyên tắc vàng” (setup càng đẹp càng dễ là bẫy) chưa được kiểm định; 0 trade/backtest tham chiếu |
| [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[CS-01 - Ho loi Trading Into Unswept Liquidity]] | Cổng D1 trong quy tắc v0.2 bắt nguồn từ đây | CS-01 đánh giá UNSUPPORTED vì thiếu nhóm lệnh thắng để so sánh |

---

## Phụ lục C — Các vấn đề dữ liệu đã phát hiện trong vault (chưa sửa gì)

Đã kiểm tra lại bằng lệnh trên chính vault vào ngày 2026-09-30.

- **`risk_percent: 5%` ở 7 note trade** trong `05 - Live Trading Journal/Trades/`, trong khi quy tắc là ≤ 0.5% (10 lần). Nếu là lỗi gõ thì dashboard đang tính sai; nếu là con số thật thì đó là vấn đề lớn hơn cả DOL.
- **`bias_correct` không có giá trị Yes/No nào**: 11 note ghi “Bullish”, phần còn lại để trống. `higher_timeframe_bias` có 12 note ghi “D1”. Vì vậy **không thể đo từ lệnh live** xem bias hay DOL đúng hay sai.
- **Query Dataview trong note 39** lọc theo `contains(string(Mistake), this.file.name)`, trong khi các note trade dùng khóa `mistakes` (theo CLAUDE.md của vault), nên query này không trả về kết quả nào.
- **`dol-ict-deep-dive.md`** không có frontmatter, tên file không theo quy ước `NN-Hyphenated-Name`, và có 24 chú thích không có định nghĩa.
- **Case 1 trong note 39** (CHF 2015) có tiêu đề “Thắng đẹp” nhưng nội dung nói đây không phải ví dụ DOL cổ điển.
- **Giờ killzone quy đổi sang giờ VN ở note 52/53** chỉ đúng vào mùa đông; hiện (tới 01/11/2026) đang lệch 1 tiếng.
- **Anti-Crowd-Trap Checklist có 0 tham chiếu** từ trade hoặc backtest nào.

**Field DOL đề xuất thêm vào template** (xem danh sách đầy đủ ở mục 12.5): `dol_price, dol_type, dol_tf, dol_side, dol_distance_atr, competitor_price, competitor_distance_atr, baseline_p, dol_horizon, pendulum_last_taken, pendulum_mode, dol_state_at_entry, path, first_blocking_pool, unswept_pool_sl_side, obviousness, dol_first, dol_time_to_hit_min, dol_near_miss_atr, loss_class`.

---

## Phụ lục D — Phần theo template `ICT_Concept_Template`

### Câu hỏi tự kiểm tra

- Mình có giải thích được DOL trong 30 giây, gồm đủ đối thủ, horizon và invalidation không?
- DOL dùng để xác định **bias**, **POI**, **entry** hay **target**? (Đáp án theo note này: **đích**, không phải bất kỳ thứ nào còn lại.)
- Nó cần ở khung nào để có giá trị? (D1/W1 cho đích lớn, H4/H1 cho DOL ngày, M15/M5 chỉ cho T1 và trigger.)
- Điều gì làm DOL bị vô hiệu? (Đóng nến ở khung của DOL được chấp nhận theo hướng ngược lại; MSS từ H1 trở lên ngược hướng; tin đổi bối cảnh.)
- Lệnh nào trong journal của mình đã đúng hoặc sai theo khái niệm này? (Xem C1, C2, C4 ở mục 8.)

### Flashcards / Active Recall

**Q1.** DOL dùng để làm gì?
**A.** Chọn **đích**: một dự báo có đối thủ, horizon và invalidation. Không phải chỗ vào lệnh.

**Q2.** Điều kiện hợp lệ quan trọng nhất là gì?
**A.** Đã ghi đối thủ, horizon, invalidation **trước** thời điểm khóa (R3), và DOL còn **chưa tiêu** (R2).

**Q3.** Lỗi phổ biến nhất là gì?
**A.** “Đúng đích, sai đường”: vào lệnh khi còn pool chưa quét nằm phía SL; hoặc chọn pool gần nhất làm DOL rồi tưởng mình đúng 63%.

**Q4.** Edge của DOL là gì?
**A.** Tỷ lệ chạm trước thực tế trừ baseline `b/(a+b)`, ở cùng khoảng cách và cùng horizon.

**Q5.** Làm sao phân biệt sweep với run?
**A.** Xét close ở đúng khung của mức: ≥ 2 close bên ngoài, hoặc 1 close kèm displacement, là “chấp nhận” (run). [HEURISTIC]

### Lesson Learned

**Bài học chính** (rút ra từ chính nghiên cứu này, không phải từ backtest):

- DOL không sai khi không có đối thủ và horizon, nên bạn không học được gì từ nó.
- Baseline `b/(a+b)` là sự thật cần so với; “tỷ lệ đúng” đứng một mình không có nghĩa.
- “Bẫy” trong dữ liệu của bạn phần lớn là lỗi quy trình, nghĩa là sửa được.

**Quy tắc cá nhân đề xuất** (chưa áp dụng, hãy chỉnh lại bằng lời của bạn):

- [ ] Điền thẻ DOL trước thời điểm khóa (11:00 VN khi Mỹ dùng EDT) và **trước khi bấm play** khi backtest.
- [ ] Không vào lệnh khi còn pool chưa quét trong 0.5 ATR H1 phía sau SL.
- [ ] Đặt TP trước mức 0.05–0.1 ATR; SL cách râu sweep 0.1–0.2 ATR rồi tính lại size (≤ 0.5%).
- [ ] Phân loại mọi lệnh thua: lỗi quy trình / thua hợp lệ / mô hình sai.
- [ ] Ghi `dol_first` cho **mọi** ngày, không chỉ ngày có setup đẹp.

### Câu nhắc khi trade

> DOL cho tôi biết **đích**. Tôi chỉ lên tàu ở POI, sau khi đối thủ gần đã bị loại, và tôi không đứng ở chỗ thanh khoản của chính mình sẽ bị lấy tiếp theo.

---

## Nguồn

**Web** (Tier 1–2 cho cơ chế và số liệu; Tier 3–4 chỉ để mô tả quan điểm cộng đồng):

- [Osler (2005), Stop-Loss Orders and Price Cascades — NY Fed SR150](https://www.newyorkfed.org/research/staff_reports/sr150.html)
- [Osler (2003), Currency Orders and Exchange Rate Dynamics — NY Fed SR125](https://www.newyorkfed.org/research/staff_reports/sr125.html)
- [Grossman & Miller (1988), Liquidity and Market Structure](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.1988.tb04594.x)
- [McLean & Pontiff (2016), Does Academic Research Destroy Stock Return Predictability?](https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365) · [CFA Digest summary](https://rpc.cfainstitute.org/research/cfa-digest/2016/06/does-academic-research-destroy-stock-return-predictability-digest-summary)
- [CME — Futures Order Types](https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/futures-order-types)
- [BIS (2019), FX trade execution: complex and highly fragmented](https://bis.org/publ/qtrpdf/r_qt1912g.htm)
- [BIS Markets Committee — The sterling “flash event” of 7 October 2016](https://www.bis.org/publ/mktc09.htm)
- [Ni, Pearson & Poteshman (2005), Stock price clustering on option expiration dates](https://www.sciencedirect.com/science/article/abs/pii/S0304405X05000577)
- [Golez & Jackwerth (2012), Pinning in the S&P 500 futures](https://ideas.repec.org/a/eee/jfinec/v106y2012i3p566-585.html)
- [2022 ICT Mentorship Ep. 2 — transcript (Sozai, bên thứ ba)](https://sozai.app/transcript/2022-ict-mentorship-episode-2/) · [Ep. 3](https://sozai.app/transcript/2022-ict-mentorship-episode-3/)
- [innercircletrader.net — IPDA](https://innercircletrader.net/tutorials/ict-ipda/) · [HRLR/LRLR](https://innercircletrader.net/tutorials/ict-hrlr-lrlr/) (nguồn cộng đồng, Tier 3–4)

**Vault:**

- Trade live: [[Loss - 01 - Trade 2026-04-29 NDX Long]] · [[Loss - 01 - Trade 2026-04-27 NDX Long]]
- Backtest: [[02 - Loss- EURUSD - 2021-05-07- Short]] · [[02 - Loss - GBPUSD - 2014-07-17 - Long]] · [[01 - Loss - XAUUSD - 2014-05-19 - Short]] · [[CS-01 - Ho loi Trading Into Unswept Liquidity]]
- Khái niệm: [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] · [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] · [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[dol-ict-deep-dive]]
- Playbook & mistake: [[Anti-Crowd-Trap Checklist (Chống bẫy đám đông ICT)]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[02-Mistake-Enter-before-liquidity-sweep]] · [[03-Mistake-Entry-When-MSS-not-in-POI-Zone]] · [[05-Mistake-Not-enough-RR]] · [[09-Mistake-Wrong-daily-bias]]
