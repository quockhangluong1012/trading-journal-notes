---
type: ict-concept
concept: Thuật toán phát hiện swing / turning point — nền tảng định lượng cho chọn swing
aliases: [Swing Detection Algorithm, Turning Point Detection, Directional Change, Intrinsic Time, ZigZag, Fractal Swing, N-bar Pivot]
tags: [trading/ict/concept, trading/deep-dive, market-structure, quantitative, swing, algorithmic, d1-h1-m5]
status: seed
category: Market Structure
timeframes: [D1, H1, M5]
models: ["ICT 2022 Model"]
markets: [NQ1, EURUSD, GBPUSD, XAUUSD]
importance: 5
confidence: 2
last_reviewed: 2026-09-22
created: 2026-09-22
updated: 2026-09-22
prerequisites: ["[[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]", "[[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]", "[[12-Dealing-Range]]", "[[05-BOS-Break-of-Structure]]"]
common_mistakes: ["dùng ZigZag có lookahead để backtest rồi tưởng là real-time được", "chọn threshold một lần rồi dùng mãi cho mọi regime", "nhầm swing phát hiện muộn (lag) với swing không tồn tại", "tối ưu threshold trên chính dữ liệu đã dùng để đánh giá", "dùng thuật toán thay cho việc hiểu cơ chế — algorithm không tạo ra edge"]
run_tag: swing-turning-point-detection-78a597
---

> [!summary] Tóm tắt 1 câu
> Mọi thuật toán phát hiện swing đều nằm trên **một trục đánh đổi duy nhất: nhạy ↔ trễ** — threshold nhỏ thì bắt swing sớm nhưng đầy nhiễu, threshold lớn thì sạch nhưng xác nhận muộn; không có tham số nào thoát khỏi trục này, và định nghĩa swing "khách quan" mà nhiều trader tìm kiếm **không tồn tại** — chỉ có định nghĩa *được tham số hoá và tái lập được*.

> [!warning] Mức độ tin cậy của bài này — đọc trước
> Bài này được viết trong điều kiện **không truy cập được toàn văn PDF** (công cụ fetch PDF của vault hỏng — xem ghi chú cuối bài). Nội dung dựa trên **abstract + metadata từ API học thuật** (OpenAlex/Crossref/Springer) và các trang HTML truy cập được. Những gì bài nói về **cơ chế định nghĩa DC** là chắc chắn (nhiều nguồn độc lập mô tả giống nhau). Những gì bài nói về **số liệu hiệu năng cụ thể** là đọc từ abstract, chưa kiểm chứng bằng toàn văn. Các ngưỡng áp dụng cho thị trường của bạn ở §5 là **suy luận từ cơ chế, KHÔNG phải khuyến nghị đã kiểm chứng**. Tự backtest trước khi tin.

---

## 1. Vì sao cần thuật toán — và cái gì thực sự được giải quyết

[[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] đưa ra tiêu chí *định tính* để lọc swing: "giá thật sự quay đầu khỏi nó và giữ nguyên mức đó qua 1–2 nến xác nhận". Tiêu chí đó đúng nhưng **không tái lập được** — hai trader nhìn cùng chart vẫn chọn swing khác nhau, và tệ hơn, **chính bạn** ở hai thời điểm khác nhau cũng chọn khác nhau. Đó chính là phê phán trung tâm của corpus ICT: *"The main problem is swing selection. Most charts contain several possible swing highs and swing lows"*.

Thuật toán giải quyết đúng **một** việc: biến "swing" từ một phán đoán thành một **hàm của (dữ liệu, tham số)** — cùng dữ liệu, cùng tham số, cùng kết quả, bất kể ai chạy hay chạy lúc nào. Nó **không** giải quyết việc chọn tham số, và nó **không** tạo ra lợi thế giao dịch. Đừng kỳ vọng sai chỗ.

### Trục đánh đổi trung tâm — hiểu cái này là hiểu 80% vấn đề

Mọi phương pháp dưới đây, không trừ cái nào, đánh đổi giữa hai lỗi:

| | **Nhạy** (threshold nhỏ / N nhỏ) | **Trễ** (threshold lớn / N lớn) |
|---|---|---|
| Bắt được | Nhiều swing, sớm | Chỉ swing lớn, muộn |
| Vấn đề | Đầy swing giả do nhiễu; mỗi lần giá giật là một "swing" | Xác nhận swing khi giá đã đi xa; entry muộn, stop xa |
| Hệ quả thực chiến | Whipsaw, stop bị quét liên tục | Bỏ lỡ phần đầu của move; R:R xấu đi |

**Không tồn tại tham số nào nằm ngoài trục này.** Đây là hệ quả toán học của việc phát hiện cực trị cục bộ trên chuỗi có nhiễu, không phải hạn chế của một thuật toán cụ thể. Bất kỳ ai bán cho bạn một "chỉ báo swing hoàn hảo" đều đang giấu tham số.

> [!important] Hệ quả trực tiếp cho workflow D1 → H1 → M5
> Vì trục này tồn tại, bạn **buộc phải** dùng **threshold khác nhau cho khung khác nhau** — không phải vì khung khác nhau về bản chất, mà vì nhiễu ở M5 lớn hơn nhiều so với D1. Dùng cùng một tham số % cho cả ba khung là lỗi phổ biến và là nguồn gốc của "MSS giả" trên M5.

---

## 2. Nhóm phương pháp truyền thống trên chart

### 2.1. N-bar pivot (fractal) — phương pháp causal đơn giản nhất

**Định nghĩa:** một nến tại vị trí *i* là swing high nếu `high[i]` là cao nhất trong cửa sổ `[i−N, i+N]`. Đối xứng cho swing low.

**Tính chất quan trọng nhất:** phải chờ **N nến sau** mới xác nhận được. Đây **không phải** khuyết điểm cần sửa — đó là bản chất của việc biết một đỉnh là đỉnh. Hệ quả:

- **Độ trễ xác nhận = N nến**, luôn luôn, không thể tránh.
- Với N lớn hơn → swing quan trọng hơn nhưng trễ hơn. Đúng trục đánh đổi ở §1.
- **Ưu điểm lớn:** causal hoàn toàn, không repaint, tính được real-time. Đây là lựa chọn **mặc định an toàn** cho backtest trung thực.

Đây chính là hình thức hoá của tiêu chí "1–2 nến xác nhận" trong note 53 — chỉ khác là N được **viết ra thành số** thay vì để tùy nghi.

### 2.2. Fractals (Bill Williams) — trường hợp riêng N = 2

Là N-bar pivot với N = 2: đỉnh phải cao hơn 2 nến mỗi bên. Được phổ biến rộng nên nhiều trader dùng mà không biết mình đang dùng một pivot 5 nến. **Hệ quả:** nó rất nhạy (bắt nhiều swing nhỏ) và do đó **không phù hợp làm định nghĩa structural swing** cho workflow D1→H1→M5 nếu dùng đơn lẻ. Hữu ích như một *thành phần*, không phải toàn bộ định nghĩa.

### 2.3. ZigZag — phổ biến nhất và **nguy hiểm nhất**

**Định nghĩa:** nối các cực trị khi giá đảo chiều vượt một ngưỡng (phần trăm, số pips/points, hoặc bội số ATR).

**Vấn đề chí mạng — repaint / lookahead:** ZigZag tiêu chuẩn được vẽ trên **dữ liệu đã biết toàn bộ**. Điểm cuối cùng của nó di chuyển mỗi khi giá tạo cực trị mới. Nghĩa là:

- Trên chart lịch sử, ZigZag cho bạn những swing **sạch sẽ và rõ ràng đến mức phi thực tế**.
- Nếu bạn backtest bằng cách đọc ZigZag trên chart đã hoàn thành, bạn đang **dùng thông tin tương lai** — mọi kết quả backtest đều vô nghĩa.

Đây là dạng **look-ahead bias** kinh điển, và nó khớp chính xác với phê phán hindsight bias mà corpus ICT đã ghi nhận: *"completed charts make ICT concepts easier to identify than they are during live market conditions"*.

> [!danger] Quy tắc bắt buộc khi backtest
> Nếu chỉ báo của bạn **vẽ lại** đường đã qua khi có dữ liệu mới, bạn không được dùng nó để backtest trừ khi bạn **tự tái lập trạng thái tại từng thời điểm** (replay bar-by-bar, chỉ hiển thị thông tin đã biết tại nến đó). Không có ngoại lệ. Đây là lý do nhiều chiến lược "đẹp trên chart" sụp khi live.

---

## 3. Nhóm học thuật — Directional Change / Intrinsic Time

Đây là nhóm **đúng nhất về mặt khái niệm** cho vấn đề của bạn, vì nó được thiết kế để trả lời chính câu hỏi "khi nào một biến động giá là *đáng kể*".

### 3.1. Nguồn gốc

Khái niệm **intrinsic time** (thời gian nội tại) xuất phát từ nhóm **Olsen & Associates** — Guillaume, Dacorogna, Davé, Müller, **Richard B. Olsen**, Pictet, *Finance and Stochastics* 1:95–129, 1997, DOI `10.1007/s007800050018`. Luận điểm gốc: dùng thời gian vật lý (nến 1 giờ, nến ngày) để lấy mẫu thị trường **bỏ sót hoạt động quan trọng**, vì dòng thời gian thị trường không đều — lúc đông lúc vắng. Thay vào đó, lấy mẫu **theo sự kiện**.

Đáng chú ý về mặt lịch sử: **Richard B. Olsen** là đồng tác giả bài 1997 này, và **Carol Osler** là người đã dùng dữ liệu order-flow của Olsen & Associates cho chuỗi nghiên cứu stop-loss clustering mà [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] đã trích (note nguồn `351236996pdf`). Cùng một dòng dữ liệu và cùng một trường phái — **đây là nền tảng học thuật thật của khái niệm "liquidity pool"**, không phải suy diễn từ chart.

### 3.2. Định nghĩa DC event — chính xác

Chuẩn hoá theo các nguồn đã đọc:

- Chọn trước một **threshold θ** — mức thay đổi giá mà *bạn* coi là đáng kể.
- **Upturn DC event:** xác nhận khi giá **tăng vượt** mức thấp nhất gần nhất một khoảng θ.
- **Downturn DC event:** xác nhận khi giá **giảm vượt** mức cao nhất gần nhất một khoảng θ.
- Sau một DC event, giá thường **tiếp tục cùng chiều** → tạo **overshoot (OS) event**.
- OS kết thúc khi có **DC event ngược chiều** tiếp theo.
- **DCT (DC trend)** = một cặp DC + OS. Thị trường được chia thành các xu hướng lên/xuống **xen kẽ**.
- **Điểm bắt đầu/kết thúc một DCT** (điểm đảo chiều) chính là **swing point** theo định nghĩa này.

Nói cách khác: **DC event ≈ swing có ngưỡng định lượng**, và θ chính là tham số hoá của trục nhạy↔trễ ở §1. Threshold nhỏ → nhiều event; threshold lớn → ít event. *(Nguồn: `algorithmic-trading-with-directional-changes-artificial-intelligence-review-spri`, `event-prediction-within-directional-change-framework-using-a-cnn-lstm-model-neur`.)*

### 3.3. Phát hiện này quan trọng — và nó phá vỡ một giả định phổ biến

Trong corpus có ghi nhận (dẫn lại từ Salman et al.): các trend trong dữ liệu DC **không phải lúc nào cũng có đủ cả DC và OS**. Tỉ lệ DCT có kèm OS event có thể thấp tới **14,77%**, và tối đa quan sát được là **52,46%**.

Hệ quả: **giả định "một swing luôn theo sau bởi một leg đẩy cùng chiều" là sai trong đa số trường hợp.** Nhiều swing bị một DC ngược chiều nuốt luôn. Điều này khớp với thực tế ICT: rất nhiều "swing low" bị phá ngay mà không tạo ra leg tăng nào đáng kể — tức chúng là **inventory swing**, đúng như phân loại ở note 53, chứ không phải structural swing.

### 3.4. Threshold cố định bị hỏng theo thời gian

Phát hiện thực nghiệm đáng giá nhất cho người dùng thật: dùng **một threshold cố định trong thời gian dài là có vấn đề**. Nếu bạn dùng θ = 0,01% và theo thời gian mức biến động "đáng kể" tụt xuống 0,009%, thì **các loại event mới sẽ không bao giờ được bắt**. Khuyến nghị từ nhóm nghiên cứu: dùng event summary trên **khung thời gian vật lý ngắn hơn** và **hiệu chuẩn lại threshold theo định kỳ**. Kết quả so sánh cho thấy giao dịch trên event series có **dynamic threshold hiệu quả hơn** threshold cố định trên thời gian dài.

**Nguyên tắc thực chiến rút ra:** threshold phải được **hiệu chuẩn lại định kỳ** (ví dụ mỗi tháng) theo biến động hiện hành — không đặt một lần rồi dùng mãi. Regime biến động thay đổi thì cùng một con số % mang ý nghĩa hoàn toàn khác.

### 3.5. Cách chọn θ trong thực nghiệm

Hai cách tiếp cận đã được công bố:

1. **Pool + chọn theo lỗi dự báo:** tạo pool **100 threshold** từ `0,005` với bước `0,0025`, chạy mô hình cho từng threshold, chọn threshold có **lỗi hồi quy nhỏ nhất**. Số threshold tối ưu khi kết hợp là **5** — nhiều hơn không cải thiện đáng kể nhưng tăng chi phí tính toán mạnh.
2. **ATR-adaptive θ:** dùng **Average True Range** để xác định θ động thay vì một số % cố định. Đây là cách mà bài CNN-LSTM dùng, và nó **tự thích ứng theo biến động** — giải quyết trực tiếp vấn đề ở §3.4.

### 3.6. Kết quả hiệu năng — đọc kèm cảnh báo

Từ abstract và nội dung bài *Algorithmic trading with directional changes* (Artificial Intelligence Review, 2022):

| Chỉ số | Multi-threshold DC | Best single-threshold DC |
|---|---|---|
| Return trung bình tháng | **1,15%** | 0,53% |
| Sharpe ratio | **0,78** | 0,28 |
| Max drawdown | **0,02** | ~0,20 (risk cao gấp ~10 lần) |

Thực nghiệm: **200 dataset tháng** từ **20 cặp Forex**, lấy mẫu **10 phút**. Kết quả có ý nghĩa thống kê theo Friedman test với Hommel post hoc ở mức 5%.

> [!warning] Ba giới hạn phải nói rõ
> **(1)** Đây là abstract-level — tôi chưa đọc được toàn văn để kiểm tra cách tính return, phí giao dịch, và slippage. **(2)** Chính tác giả nêu rõ **chưa kiểm chứng** trên commodities, bond, indices, cổ phiếu hay crypto — nghĩa là **NQ/XAU chưa được kiểm chứng**. **(3)** Bài CNN-LSTM báo hệ số xác định R² = 0,985 trên GBPUSD — con số này **cao đến mức đáng ngờ** cho dữ liệu tài chính và cần kiểm chứng độc lập trước khi tin.
>
> Ngoài ra: **multi-threshold thắng single-threshold**, đúng như trực giác — nhiều thước đo thì bắt được nhiều loại event hơn. Nhưng độ phức tạp vận hành tăng theo.

---

## 4. Nhóm change-point detection — nền tảng lý thuyết bổ sung

Nhóm này không trực tiếp cho swing point, nhưng cung cấp **bộ máy thống kê để trả lời "thay đổi này có ý nghĩa hay chỉ là nhiễu"** — chính là câu hỏi mà θ đang trả lời bằng con số cảm tính.

Các mốc chính (đã xác minh qua API học thuật):

| Công trình | Năm | Trích dẫn | Vai trò |
|---|---|---|---|
| **Page**, *Continuous Inspection Schemes* | 1954 | 1.519 | Khởi nguồn CUSUM — phát hiện dịch chuyển mức theo tuần tự |
| **Bai & Perron**, *Estimating and Testing Linear Models with Multiple Structural Changes* | 1998 | 4.497 | Chuẩn mực kinh tế lượng cho nhiều điểm gãy cấu trúc |
| **Killick, Fearnhead & Eckley**, *Optimal Detection of Changepoints With a Linear Computational Cost* (PELT) | 2012 | 2.198 | Thuật toán chi phí tuyến tính — khả thi thực tế |
| **Fearnhead**, *Exact and efficient Bayesian inference for multiple changepoint problems* | 2006 | — | Nền tảng Bayesian; dẫn tới **BOCPD** (online) |

**Vì sao đáng quan tâm:** nhánh **online / sequential** (Page 1954, BOCPD) mới là nhánh **causal** — nó quyết định *tại thời điểm hiện tại* chỉ dựa trên dữ liệu đã quan sát. Đây là nhánh đúng cho giao dịch thời gian thực, và là nền tảng lý thuyết cho việc trả lời "swing này đã xác nhận chưa" mà không cần nhìn tương lai.

**Lưu ý phạm vi:** change-point detection phát hiện **thay đổi trong phân phối/tham số** (ví dụ phương sai, mean), không nhất thiết là **điểm đảo chiều giá**. Hai thứ khác nhau. Dùng nó như bộ lọc nhiễu / bộ phát hiện regime, không phải máy tìm swing.

---

## 5. Áp dụng cho workflow của bạn — đề xuất có điều kiện

> [!warning] Toàn bộ §5 là **suy luận từ cơ chế**, không phải kết quả đã kiểm chứng
> Không có nguồn nào trong bài này test trên NQ, XAUUSD hay khung D1/H1/M5. Các con số dưới đây được suy ra từ nguyên tắc ở §1 và §3, và **phải được backtest trước khi dùng tiền thật**.

### 5.1. Kiến trúc đề xuất: hai tầng định nghĩa swing

Thay vì một định nghĩa swing duy nhất, tách thành hai tầng — điều này khớp trực tiếp với phân loại structural vs inventory ở note 53:

**Tầng 1 — swing cấu trúc (structural swing)** → dùng để xác định dealing range, BOS/MSS, HH/HL.
- Phương pháp: **N-bar pivot với N lớn**, hoặc **DC threshold lớn**.
- Đặc điểm: ít swing, trễ nhiều. Trễ ở tầng này **chấp nhận được** vì bạn dùng nó để đọc *cấu trúc*, không để entry.

**Tầng 2 — swing thao tác (operational swing)** → dùng để đặt stop, xác định sweep gần nhất, entry.
- Phương pháp: **N-bar pivot N nhỏ**, hoặc **DC threshold nhỏ theo ATR**.
- Đặc điểm: nhiều swing, nhạy. Chấp nhận nhiễu vì vai trò là *địa chỉ*, không phải *cấu trúc*.

**Quy tắc nối hai tầng:** một swing tầng 2 chỉ được **thăng cấp** thành tầng 1 nếu việc phá nó thay đổi cấu trúc (đóng thân qua nó, không phải râu). Đây chính là "câu hỏi lọc" ở note 53, giờ được vận hành hoá thành hai tham số tách biệt.

### 5.2. Gợi ý khởi điểm để backtest

Bảng dưới là **điểm bắt đầu để thử**, không phải cấu hình đúng:

| Khung | Vai trò | Phương pháp khởi điểm | Ghi chú |
|---|---|---|---|
| **D1** | Structural swing → dealing range | N-bar pivot, N = 3–5 | Trễ 3–5 ngày là chấp nhận được cho cấu trúc |
| **H1** | Structural + POI context | N-bar pivot, N = 3–5 | Khớp với nhịp H1 của workflow |
| **M5** | Operational swing → stop, sweep | DC threshold theo **ATR(14)**, θ ≈ 0,3–0,5 × ATR | Nhạy vừa; tuyệt đối không dùng cùng % như D1 |

**Hiệu chuẩn lại:** tính lại θ theo ATR **mỗi tháng** (hoặc mỗi khi biến động regime đổi rõ). Không cố định một lần.

### 5.3. Bốn lỗi phải tránh

1. **Tối ưu tham số trên chính dữ liệu đánh giá.** Nếu bạn thử 20 giá trị N rồi chọn cái cho kết quả đẹp nhất trên cùng bộ dữ liệu, bạn đã overfit. Cần out-of-sample.
2. **Dùng ZigZag không replay để backtest.** Xem §2.3 — kết quả sẽ vô nghĩa.
3. **Cùng một tham số cho mọi khung.** Xem §1 — đây là nguồn của MSS giả trên M5.
4. **Nghĩ rằng thuật toán tạo ra edge.** Không. Thuật toán chỉ làm cho swing **tái lập được**. Edge (nếu có) nằm ở chỗ khác: chọn pool, thời điểm, quản trị rủi ro.

---

## 6. Kết luận trung thực

**Cái đã giải quyết được:** có những định nghĩa swing **tái lập được, causal, không repaint** — N-bar pivot (đơn giản nhất, đủ dùng) và DC event (chặt chẽ nhất về khái niệm, có cả một dòng nghiên cứu và bằng chứng thực nghiệm đứng sau). Cả hai đều đòi hỏi bạn **viết tham số ra** và **chấp nhận độ trễ xác nhận**. Điều này tốt hơn hẳn tình trạng hiện tại, nơi swing được chọn bằng mắt và do đó không thể backtest trung thực.

**Cái KHÔNG giải quyết được:** không thuật toán nào nói cho bạn biết N hay θ nào là *đúng*, vì "đúng" phụ thuộc khung giao dịch, biến động regime, và holding period của bạn. Và không thuật toán nào loại bỏ được trục nhạy↔trễ.

**Điều đáng chú ý nhất về mặt trí tuệ:** khái niệm "liquidity pool" mà ICT dạy có **nền tảng học thuật thật** — nó bắt nguồn từ dữ liệu order-flow của Olsen & Associates (Guillaume et al. 1997, có Richard B. Olsen), cùng nguồn dữ liệu mà Carol Osler dùng cho nghiên cứu stop-loss clustering. Đây không phải trùng hợp: **intrinsic time và liquidity clustering là hai mặt của cùng một quan sát** — rằng hoạt động thị trường tập trung vào những thời điểm và những mức giá nhất định, và cả hai đều bị bỏ sót nếu chỉ lấy mẫu theo thời gian vật lý đều đặn.

### Nguồn tham chiếu

| Nội dung | Nguồn |
|---|---|
| Intrinsic time, nguồn gốc Olsen & Associates | `10.1007/s007800050018` — Guillaume, Dacorogna, Davé, Müller, **Olsen**, Pictet, *Finance and Stochastics* 1:95–129 (1997) |
| Định nghĩa DC/OS/DCT, MTDC, threshold pool, tỉ lệ DCT có OS (14,77–52,46%), kết quả hiệu năng | `10.1007/s10462-022-10307-0` — Adegboye, Kampouridis, Otero, *Artificial Intelligence Review* (2022) |
| DC + ATR-adaptive threshold, CNN-LSTM trên GBPUSD/EURUSD/USDCHF/USDCAD | `10.1007/s00521-022-07687-3` — Rostamian & O'Hara, *Neural Computing and Applications* (2022) |
| Event-driven sampling thay cho physical time | `10.5018/economics-ejournal.ja.2012-36` — *A Directional-Change Event Approach for Studying Financial Time Series* (2012) |
| Dynamic DC threshold, cập nhật theo ngày | Alkhamees & Fasli (2017), DSAA + IEEE BigData |
| CUSUM, phát hiện tuần tự | Page, *Continuous Inspection Schemes* (1954), DOI `10.2307/2333009` |
| Nhiều điểm gãy cấu trúc | Bai & Perron (1998), DOI `10.2307/2998540` |
| PELT — thuật toán chi phí tuyến tính | Killick, Fearnhead & Eckley (2012), DOI `10.1080/01621459.2012.737745` |
| Bayesian online changepoint | Fearnhead (2006), DOI `10.1007/s11222-006-8450-8` |
| Phê phán swing selection chủ quan trong ICT | `ict-trading-problems-subjectivity-hindsight-bias-and-the-limits-of-the-method-za` |
| Giới hạn của bằng chứng liquidity clustering | `351236996pdf` (Osler) |

### Liên quan trực tiếp

[[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] — bài này biến tiêu chí swing thành hàm của (dữ liệu, tham số); note 56 dùng lại kết luận đó làm **điều kiện tiên quyết** cho identification framework, và bổ sung phần còn thiếu: candidate selection, failure model 3 lớp, 8 trap patterns, và **look-ahead checklist 9 mục** (L1 và L3 ở đó chính là hệ quả trực tiếp của vấn đề swing-selection mà bài này giải quyết).

[[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] · [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] · [[dol-ict-deep-dive]]

### Action items

- [ ] Code N-bar pivot N=3 và N=5 cho D1/H1/M5; đối chiếu với các swing bạn **đã** chọn bằng mắt trong 20 lệnh gần nhất — đo mức khớp
- [ ] Viết hàm DC event với θ = k × ATR(14), thử k ∈ {0,2; 0,3; 0,5; 1,0}; đếm số swing mỗi khung
- [ ] Backtest có replay bar-by-bar (không dùng chart đã hoàn thành) để tránh lookahead
- [ ] Chia dữ liệu in-sample / out-of-sample **trước khi** thử tham số; báo cáo kết quả out-of-sample
- [ ] Đo riêng: với mỗi định nghĩa swing, tỉ lệ "swing bị phá mà không tạo leg" — so với con số 14,77–52,46% của nghiên cứu
- [ ] Hiệu chuẩn lại θ mỗi tháng theo ATR hiện hành

> [!note] Ghi chú kỹ thuật — lỗi công cụ
> Run này **không lấy được toàn văn PDF**: công cụ fetch của vault lưu file PDF qua một lần chuyển UTF-8 làm hỏng byte nhị phân, khiến 17–23% byte trong mỗi PDF bị thay bằng ký tự thay thế và **toàn bộ stream nén không giải được**. Ảnh hưởng: 4 PDF của run này, và cả note `magic20numbers20in20the20dowpdf` của run trước (chưa từng đọc được). Bài này vì vậy chỉ dùng được **abstract + metadata + trang HTML**. Nếu cần độ chính xác số liệu cao hơn, phải sửa công cụ fetch PDF rồi chạy lại.
