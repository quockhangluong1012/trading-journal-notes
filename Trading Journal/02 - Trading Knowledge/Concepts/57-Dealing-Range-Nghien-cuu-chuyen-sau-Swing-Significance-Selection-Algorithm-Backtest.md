---
type: ict-concept
concept: "Dealing Range — nghiên cứu chuyên sâu: swing significance, selection algorithm, validity, backtest"
aliases: [Dealing Range Deep Dive, Swing Significance, Dealing Range Selection, Chọn Dealing Range, Dealing Range Quality Score, Swing Significance Score]
tags: [trading/ict/concept, trading/deep-dive, market-structure, liquidity, quantitative, d1-h1-m5, 2022-model]
status: seed
category: Market Structure
timeframes: [D1, H1, M5]
models: ["ICT 2022 Model"]
markets: [NQ1, EURUSD, GBPUSD, XAUUSD]
importance: 5
confidence: 2
last_reviewed: 2026-09-28
created: 2026-09-28
updated: 2026-09-28
prerequisites: ["[[12-Dealing-Range]]", "[[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]", "[[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]", "[[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]", "[[27-Premium-Discount]]", "[[16-Internal-External-Range-Liquidity-IRL-ERL]]", "[[37-Re-mapping-Dealing-Range-sau-Displacement]]", "[[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]", "[[05-BOS-Break-of-Structure]]", "[[21-Market-Structure-Shift]]"]
common_mistakes: ["coi dealing range là một khái niệm có định nghĩa canon duy nhất", "chọn swing biên range vì nó 'trông lớn' thay vì vì nó thay đổi cấu trúc", "đo premium/discount trên range được chọn SAU khi biết outcome", "dùng chính range để suy ra DOL rồi dùng DOL để biện minh cho range (vòng lặp logic)", "coi premium/discount là tín hiệu hướng thay vì khung vị trí", "re-map range mỗi khi giá wick qua biên (nhiễu hoá bản đồ)", "phân loại internal/external bằng cảm giác thay vì bằng tiêu chí phá cấu trúc", "cho rằng dealing range có predictive power đã được chứng minh"]
run_tag: dealing-range-deep-dive-2026-09-28
---

> [!summary] Tóm tắt 1 câu
> **Dealing Range không phải một khái niệm có định nghĩa canon — nó là một *khung tham chiếu có tham số* (reference frame), và toàn bộ giá trị cũng như toàn bộ rủi ro của nó nằm ở chỗ: bạn chọn hai điểm neo (anchor) nào, theo tiêu chí nào, và ghi lại lúc nào.** Bài này biến việc chọn neo từ phán đoán thị giác thành một quy trình có tiêu chí, có thang điểm, có thể code, và — quan trọng nhất — có thể **sai và bị bác bỏ**.

> [!warning] Đọc phần này trước khi đọc phần còn lại — tuyên bố về mức độ bằng chứng
> Bài này chia mọi phát biểu thành 6 tầng, và **ghi nhãn ngay tại chỗ**:
>
> | Nhãn | Nghĩa | Ví dụ trong bài |
> |---|---|---|
> | **[A] FACT** | Quan sát trực tiếp được từ price/time/volume | "Giá đóng cửa dưới swing low trước đó tại nến 14:00" |
> | **[B] MICROSTRUCTURE** | Giải thích bằng cơ chế khớp lệnh / đấu giá, có nền tảng học thuật | "Stop orders tập trung quanh round numbers (Osler 2003)" |
> | **[C] ICT FRAMEWORK** | Cách ICT đặt tên và diễn giải | "Hai đầu range là external range liquidity (ERL)" |
> | **[D] INTERPRETATION** | Cách hiểu hợp lý nhưng chưa chứng minh trực tiếp | "Range này đại diện cho một phiên đấu giá chưa ngã ngũ" |
> | **[E] HYPOTHESIS** | Giả thuyết cần backtest | "Swing có displacement significance cho kết quả tốt hơn swing to về số pip" |
> | **[F] NARRATIVE** | Câu chuyện institutional không kiểm chứng được từ chart | "Smart money tạo range này để gom hàng" |
>
> **Không có bằng chứng bình duyệt nào kiểm định trực tiếp "dealing range" hay ICT/SMC nói chung.** Cái có bằng chứng là các *thành phần cơ học* bên dưới (clustering của stop quanh mức tròn, thay đổi độ sâu order book quanh hỗ trợ/kháng cự). Xem §28 và §33. Mọi con số ngưỡng trong bài, trừ khi ghi rõ nguồn, đều là **practice number** — điểm khởi đầu để backtest, không phải sự thật.

---

> [!info] Danh mục 13 hình minh hoạ trong bài
> | # | Hình | Nằm ở |
> |---|---|---|
> | 1 | Bốn định nghĩa "dealing range" trên cùng một đường giá | §3.1 |
> | 2 | Fragility test — kiểm tra kết luận P/D có bền không | §3.2 |
> | 3 | Mô hình hai tầng: GATES → SCORES | §10.2 |
> | 4 | Structural significance ≠ visual size (220 pt bị loại, 45 pt được chọn) | §10.3 |
> | 5 | Phân cấp swing đệ quy (L1–L5 theo phạm vi vô hiệu) | §11.2 |
> | 6 | Thuật toán chọn range: 7 ứng viên → 1 PRIMARY | §13.2 |
> | 7 | Máy trạng thái của một dealing range | §14.4 |
> | 8 | Liquidity raid vs structural break | §15.5 |
> | 9 | Vai trò pool đảo theo vị trí giá (draw ↔ fuel) | §17.2 |
> | 10 | Vòng lặp logic Range ↔ DOL và cách chặn | §18.3 |
> | 11 | Alignment đa khung: hai cấu hình khó nhất | §20.4 |
> | 12 | Thang bằng chứng cho kịch bản pullback sâu | §21.3 |
> | 13 | Trạng thái bằng chứng của tài liệu ICT/SMC | §33.2 |
>
> Toàn bộ hình là **SVG nguyên bản** vẽ cho bài này, lưu ở `02 - Trading Knowledge/Concepts/attachments/` với tiền tố `DR-Deep-`.

## 1. Executive Summary

**Mười kết luận cốt lõi — đọc mục này là đủ để nắm toàn bài; phần còn lại là chứng minh.**

1. **Không tồn tại "dealing range đúng" khách quan.** Tồn tại *một định nghĩa được tham số hoá* (dữ liệu + tham số + quy tắc neo), tái lập được, và do đó **kiểm chứng được**. Bất kỳ ai nói "range này mới đúng" mà không nêu tiêu chí chọn neo đang trình bày một phán đoán như một sự thật. — **[C]+[D]**

2. **Dealing Range là công cụ ĐỊNH VỊ (location), không phải công cụ ĐỊNH HƯỚNG (direction).** Nó trả lời "giá đang đắt hay rẻ *so với cái gì*", không trả lời "giá sẽ đi đâu". Mọi cách dùng nó như tín hiệu hướng (discount → mua) đều là lạm dụng. — **[C], có thể kiểm chứng bằng [E]**

3. **Giá trị thật của range là *chuẩn hoá*, không phải *dự báo*.** Nó biến "giá 20,450" (vô nghĩa nếu không có tham chiếu) thành "giá ở 23% của nhịp gần nhất" (so sánh được giữa các ngày, các symbol, các regime). Giá trị này là **descriptive**; xem §9 và §18. — **[D]**

4. **Câu hỏi trung tâm của bạn — "swing nào đủ quan trọng?" — có câu trả lời một phần, không có câu trả lời trọn vẹn.** Ba tiêu chí *cứng* (đo được, tái lập được): (i) phá nó có thay đổi cấu trúc không; (ii) nó có phải là điểm khởi phát của một displacement không; (iii) nó có phải là cực trị của một leg mà lệnh thật đang nằm hai đầu không. Bốn tiêu chí còn lại (liquidity, reaction, contextual, protected) là **xác suất, không phải nhị phân** và phải cộng điểm, không phải gạt. — **[C]+[E]**

5. **STRUCTURAL SIGNIFICANCE ≠ VISUAL SIZE.** Một swing 200 pip không phá gì cả có significance thấp hơn một swing 40 pip đã tạo BOS và trở thành protected low. Đây là điểm sai phổ biến nhất, và là điểm mà "nhìn chart cảm thấy quan trọng" thất bại. — **[C], kiểm chứng được [E]**

6. **Vòng lặp logic mặc định của framework D1→H1→M5 là có thật và phải bị chặn bằng timestamp.** "Range quan trọng vì nó tạo DOL" và "DOL này là DOL vì nó ở biên range quan trọng" là hai nửa của cùng một vòng. Cách chặn: **chốt range ex-ante, timestamp, và DOL phải có ít nhất một bằng chứng độc lập với range** (xem §18, §27-E13).

7. **Premium/discount không phải nhị phân và không đối xứng với chất lượng setup.** Discount nông (25–50%) thường chỉ là nhiễu; discount sâu + array cụ thể mới có nghĩa. Và **discount trong xu hướng giảm không có ý nghĩa bullish** — vị trí không bao giờ đứng một mình. — **[C]+[E]**

8. **Range validity là một máy trạng thái, không phải một câu hỏi có/không.** Bốn trạng thái tách biệt: `VALID` → `REFINED` (tinh chỉnh biên) / `REPLACED` (thay neo) / `INVALIDATED` (mất hiệu lực) / `SUSPENDED` (chưa đủ dữ liệu để phán). Lẫn bốn cái này là nguồn gốc của việc re-map liên tục. Xem §14.

9. **Phá protected swing không "đổi trend".** Nó đổi **cấp độ cấu trúc đang bị phá** (internal → intermediate → external), và mỗi cấp có hệ quả khác nhau về range, DOL và size. Phá bằng wick, phá bằng body-close, phá bằng displacement-and-acceptance là **ba sự kiện khác nhau** về mặt thông tin. Xem §15 và §21.

10. **Có thể code hoá ~70% quy trình.** Phần code được: phát hiện swing, phân cấp, đo displacement, đo reaction, đo vị trí, phát hiện invalidation, chấm điểm range. Phần **không** code được đáng tin: gán trọng số cho thang điểm (§29) và xác định "narrative" giữa nhiều range cùng hợp lệ. Nói thẳng: thang điểm heuristic không phải edge; nó chỉ là cách viết ra tiêu chí để có thể sai một cách rõ ràng.

> [!important] Ba điều tôi **không** đồng ý với giả định trong đề bài của bạn
> **(1) "Dealing Range → External Liquidity → DOL" như một pipeline một chiều là sai thứ tự thông tin.** External liquidity ở hai đầu range là *đầu vào* để chọn range (bạn chọn swing vì nó đã lấy/đang chứa liquidity), không phải *đầu ra*. Nếu vẽ pipeline một chiều, bạn sẽ tự tạo circular reasoning mà không thấy.
>
> **(2) "Dealing Range chủ yếu để xác định structural context" — đúng, nhưng thiếu vế thời gian.** Dealing range không có "tuổi thọ mặc định". Một range D1 vẽ từ 6 ngày trước có thể đã bị tiêu thụ hết ý nghĩa dù chưa bị phá. Cần thêm biến `range_age` và `range_freshness` vào framework, nếu không thì mọi phép đo P/D sẽ lặng lẽ dùng dữ liệu chết.
>
> **(3) "Tránh giao dịch M5 ngược HTF context" — đúng về kỳ vọng, nhưng có chi phí thật.** HTF veto giết luôn một lớp setup đảo chiều hợp lệ tại cực trị HTF (chính nơi HTF *nên* đảo). Giữ rule này như mặc định, nhưng phải biết nó là một lựa chọn đánh đổi (bỏ sót reversal) chứ không phải một sự thật kỹ thuật. Xem §21-Q8 và §32-H5.

---

## 2. Direct Answer — trả lời thẳng 10 câu hỏi cuối cùng

| # | Câu hỏi | Trả lời thẳng | Có objective không? |
|---|---|---|---|
| 1 | Dealing Range này là gì? | Một **cặp neo** `(anchor_high, anchor_low)` trên một timeframe, cộng metadata (thời điểm chốt, trạng thái hiệu lực, lý do chọn). Không phải "vùng giá" — là **hai điểm + quy tắc**. | Có, nếu bạn viết ra định nghĩa neo. Xem §3, §12 |
| 2 | Tại sao swing này được chọn? | Vì nó thắng trong một **thang tiêu chí có thứ tự ưu tiên**: (1) phá nó đổi cấu trúc, (2) nó khởi phát displacement, (3) hai đầu range chứa liquidity chưa tiêu thụ. | Có (3 tiêu chí cứng). Phần còn lại là xác suất. §10 |
| 3 | Tại sao swing khác không được chọn? | Vì nó **không thay đổi gì khi bị phá** (inventory/noise swing), hoặc vì nó nằm *bên trong* leg của neo mạnh hơn → nó thuộc range con, không phải range chính. | Có. §11 |
| 4 | Range này đại diện cho structural state nào? | Một trong bốn: `trend-continuation`, `pullback-in-progress`, `transition/CHoCH`, `balance/accumulation`. Range **không** nói state; state đến từ chuỗi BOS/MSS + vị trí trong range lớn hơn. | Có, nhưng phải suy từ cấu trúc, không từ range. §16, §22 |
| 5 | Range này còn valid không? | Máy trạng thái 4 giá trị (§14). Câu trả lời đúng luôn kèm **điều kiện invalidation viết trước**. | Có. §14 |
| 6 | Phá protected swing thì cái gì thực sự thay đổi? | Thay đổi **cấp cấu trúc bị phá** + **tập ứng viên DOL** + **range nào đang chi phối**. Không tự động đổi trend, không tự động đảo bias. | Có, nếu phân cấp swing đúng. §15 |
| 7 | Pullback, internal reversal hay genuine reversal? | Phân biệt bằng **3 câu hỏi độc lập**: (a) đã phá cấp nào (internal/int/external)? (b) protected level HTF còn nguyên không? (c) điểm phá nằm ở premium hay discount của range HTF? Ba câu này **không đủ** để chắc chắn — chỉ đủ để gán xác suất và size. | **Một phần.** Xem §21-Q5 và §33 |
| 8 | DOL hiện tại ở đâu và tại sao? | DOL = pool **chưa bị tiêu thụ**, gần nhất theo hướng bias, có bằng chứng độc lập với range (bên nào vừa bị ăn + cấu trúc). Phải viết được thành một câu kèm giá. | Có. §18 |
| 9 | Tôi xác định được real-time hay chỉ bằng hindsight? | Real-time được **nếu** bạn dùng neo causal (N-bar pivot / DC threshold có độ trễ xác nhận) và chấp nhận rằng range hôm nay có thể bị thay thế ngày mai một cách hợp lệ. Không real-time được nếu bạn chọn neo bằng mắt sau khi biết outcome. | Có, có điều kiện. §31 |
| 10 | Có viết được algorithm để computer tự xác định không? | **Được cho phần lớn.** §30 có pseudocode đầy đủ. Ba thứ algorithm không giải quyết: chọn trọng số (§29), chọn θ/N cho từng regime (§12-B1), và phân xử khi hai range cùng hợp lệ mà mâu thuẫn kết luận (§13). | Có, một phần — và tôi nói rõ phần nào không |

---

## 3. Dealing Range — định nghĩa chính xác (và vì sao "chính xác" là chuyện khó)

### 3.1. Vấn đề đầu tiên: có ít nhất BỐN thứ khác nhau đang được gọi là "dealing range"

Đây là phát hiện quan trọng nhất của §3. Khi hai trader tranh luận "range nào đúng", thường họ đang nói về **hai định nghĩa khác nhau**, không phải hai ý kiến về cùng một định nghĩa. Cả bốn định nghĩa dưới đây đều xuất hiện trong tài liệu ICT ở các thời điểm khác nhau. — **[C]+[D]**

| # | Định nghĩa | Cách xác định | Dùng để làm gì | Vấn đề |
|---|---|---|---|---|
| **DR-1** | **Range premium/discount** — khoảng giữa một swing high và một swing low *có ý nghĩa*, mà giá đang vận động bên trong | Hai neo swing (thường là swing gần nhất tạo ra cấu trúc/BOS) | Chia premium/discount, đo OTE, định vị POI | "Có ý nghĩa" là tiêu chí chưa vận hành hoá → nguồn gốc của mọi tranh cãi. **Đây là định nghĩa đang dùng trong vault** ([[12-Dealing-Range]]) |
| **DR-2** | **Consolidation / trading range** — vùng giá đi ngang giữa hai biên bị test nhiều lần | Biên = 2 lần test trở lên mỗi phía; đỉnh/đáy của vùng tích luỹ | Nhận diện balance, accumulation, breakout playbook | Khác bản chất với DR-1: đây là *cấu trúc thị trường*, không phải *khung đo vị trí* |
| **DR-3** | **Lookback range / IPDA data range** — cực trị cao nhất/thấp nhất trong một cửa sổ thời gian cố định (20 / 40 / 60 ngày, hoặc 20 tuần) | Cửa sổ thời gian cứng, không cần phán đoán | Xác định "range lớn" làm bối cảnh vĩ mô; neo cho [[08-Central-Bank-Dealers-Range]] | **Hoàn toàn objective** — nhưng độ nhạy với cửa sổ rất cao, và nó trả lời câu hỏi khác ("giá đang ở đâu trong N ngày qua") |
| **DR-4** | **Leg range / reference frame của một nhịp** — range của *chính cái leg đang chạy*, dùng cho OTE và projection | Neo = điểm khởi phát leg + cực trị leg | Đo retracement của nhịp hiện tại, tính OTE, chiếu standard deviation | Trùng số với DR-1 trong nhiều trường hợp → **nguồn của lỗi đo OTE sai khung** đã ghi nhận trong vault (note backtest EURUSD 2021-05-03, `04 - Backtesting/2026-07-10/`, mục O3) |

> [!danger] Đây là lỗi âm thầm tốn tiền nhất trong cả bài
> > **Nguồn:** lỗi này đã được ghi nhận thật trong vault, ở note backtest EURUSD ngày 2021-05-03 (thư mục `04 - Backtesting/2026-07-10/`), mục O3: vị trí entry được tính bằng `%` của **toàn dealing range** trong khi canon yêu cầu OTE đo trên **impulse leg cụ thể**. Hai con số có thể tình cờ gần nhau — nhưng chúng **không tự động là cùng một khái niệm**. Nếu bạn không ghi rõ đang neo fib vào cái nào, backtest của bạn đang trộn hai loại biến vào cùng một cột dữ liệu, và mọi thống kê về sau đều nhiễm.
>
> **Rule cứng:** mọi phép đo fib phải ghi kèm nhãn `anchor_type ∈ {DR-1, DR-4}`. Không có nhãn = không dùng được cho thống kê.

![[DR-Deep-01-Bon-Dinh-Nghia.svg|760]]
*Hình 1 — Cùng MỘT đường giá, bốn định nghĩa "dealing range" đang lưu hành. Neo khác nhau → EQ khác nhau → `pd` khác nhau. Panel D cho kết luận hành động NGƯỢC lại ba panel kia (0.33 · 0.12 · 0.38 · 0.06).*

### 3.1b. Bằng chứng tra cứu độc lập về bốn định nghĩa này (kết quả kiểm tra nguồn)

Bốn định nghĩa ở §3.1 **không phải giả thuyết của tôi** — chúng là các biến thể đang thực sự lưu hành. Kết quả tra cứu (thực hiện riêng cho bài này):

| Biến thể | Nội dung ghi nhận được | Nguồn | Loại nguồn |
|---|---|---|---|
| **Liquidity-based** | *"The dealing range is a price area that removes buy-side and sell-side liquidity"*; slide caption *"New Dealing Range After Break Of Dealing Range Low"* | [ictsharks — ghi chú buổi "2022 ICT Mentorship: Dealing Ranges"](https://forum.ictsharks.com/t/2022-ict-mentorship-dealing-ranges/511) | **Gián tiếp từ ICT** (ghi chú học viên trên video) |
| **Swing-based (DR-1)** | *"The primary range is measured from the Swing High to the Swing Low. Anything above the 50% line (0.5 equilibrium) is classified as a Premium Zone"* | [astrofin, dẫn ICT 2022 Mentorship Ep.2](https://time-price-research-astrofin.blogspot.com/2026/08/ict-daily-bias-derived-from-dealing.html) | Gián tiếp từ ICT, qua blog tổng hợp |
| **Swing-based (định nghĩa daily)** | *"ICT defines a daily dealing range from a swing low to a swing high… midpoint, which he calls equilibrium"* | [bestprops — phân tích Ep.19 có timestamp](https://bestprops.com/2022-ict-mentorship-episode-19/) | Gián tiếp từ ICT |
| **Swing-based (DR-1, phổ biến)** | *"A Dealing Range is any defined price range between a significant swing high and swing low"*; range lồng nhau ở mọi khung | [ICT Flow, lesson 17](https://ictflow.com/lesson/17) | Thứ cấp (vendor) |
| **Time-window / IPDA (DR-3)** | *"price band formed between the swing high and swing low of a given IPDA window (20, 40, or 60 sessions)"*; *"recalculated with each new session"* | [Backtrex](https://backtrex.com/en/blog/ict-dealing-range-ipda-data-range-guide) | Thứ cấp (vendor) |
| **Sweep-based (DR-4 hướng)** | *"created when the market reverses after sweeping liquidity from both sides"* | [TradingView script "ICT Dealing Range Lite"](https://br.tradingview.com/script/UdCtGrfF-ICT-Dealing-Range-Lite-fadi/) | Thứ cấp (vendor) |
| **Pivot-based (thuật toán)** | *"most recent valid alternating pivot sequence"* + lọc ATR | [TradingView script của EmpArchitect](https://www.tradingview.com/script/q6O0kR6a-ICT-Dealing-Range-EmpArchitect/) | Thứ cấp (vendor) |

**Và đây là ba mâu thuẫn trực tiếp giữa các nguồn — không phải suy diễn:**

1. **Liquidity-based vs swing-based.** Nguồn gần ICT nhất nói range là *vùng giá lấy đi BSL và SSL hai phía*; các nguồn khác nói là *khoảng giữa swing high và swing low*. Hai tiêu chí này **cho kết quả khác nhau** trên cùng một chart (vì một swing rõ không nhất thiết đã quét liquidity, và một cú quét không nhất thiết tạo swing cùng cấp).
2. **Time-based vs structure-based.** Có nguồn định nghĩa range bằng **cửa sổ cố định 20/40/60 phiên, tính lại mỗi phiên**; nguồn khác nói range tồn tại **tới khi có body-close phá biên**. Hai cách này **không thể đồng thời đúng** — cùng một thời điểm, chúng sẽ cho hai range khác nhau.
3. **IPDA data range có *là* dealing range không?** Một nguồn **đánh đồng** hai khái niệm; nguồn khác **tách rời** chúng (IPDA = bản đồ target liquidity; range premium/discount là chuyện khác). Mâu thuẫn trực tiếp.

> [!warning] Phát hiện quan trọng nhất của phần tra cứu — và nó làm yếu toàn bộ §3
> **Không lấy được một artifact sơ cấp nào của ICT**: không transcript verbatim, không tweet, không tài liệu chính thức. Mọi phát biểu dạng *"ICT nói dealing range là…"* trong các nguồn trên đều là **gián tiếp qua nguồn thứ cấp** (ghi chú học viên, blog tổng hợp, hoặc vendor).
>
> Hệ quả nhận thức luận, nói thẳng: **ngay cả "định nghĩa của ICT" cũng không kiểm chứng được ở mức sơ cấp.** Điều này **củng cố** luận điểm trung tâm của bài (§1-điểm 1) chứ không làm nó yếu đi: nếu ngay cả nguồn gốc cũng không xác minh được, thì việc **tự viết ra định nghĩa vận hành của mình** không phải là "tự chế" — đó là **điều kiện bắt buộc** để có một hệ thống kiểm chứng được.
>
> **Điều này cũng có nghĩa:** mọi tranh luận kiểu *"range này đúng canon chưa?"* là tranh luận **không thể phân giải**. Tranh luận có thể phân giải là: *"với định nghĩa vận hành X, range này cho kết quả gì, và định nghĩa X có tốt hơn Y không?"* — và đó chính là nội dung §29–§32.

### 3.2. Định nghĩa vận hành dùng trong bài này

$$
\text{DR} = \big(\underbrace{h}_{\text{anchor high}},\ \underbrace{l}_{\text{anchor low}},\ \underbrace{\tau}_{\text{timeframe}},\ \underbrace{t_0}_{\text{thời điểm chốt (causal)}},\ \underbrace{S}_{\text{significance score}},\ \underbrace{\sigma}_{\text{trạng thái hiệu lực}}\big)
$$

Trong đó:

- $h, l$ — giá của hai neo. **Bắt buộc là swing point đã xác nhận** (không phải đáy nến đang chạy — xem [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] §2).
- $\tau$ — timeframe gốc. Range không "thuộc về" một symbol; nó thuộc về một **(symbol, timeframe, t0)**.
- $t_0$ — **thời điểm mà tại đó range này là thông tin đã biết**. Đây là biến chống look-ahead bias quan trọng nhất trong toàn bộ bài. Không có $t_0$ thì không backtest được (§31-A4).
- $S$ — điểm significance của neo yếu hơn trong hai neo (range không thể mạnh hơn neo yếu nhất của nó — xem §10.8, nguyên tắc "weakest link").
- $\sigma \in \{\text{VALID}, \text{REFINED}, \text{REPLACED}, \text{INVALIDATED}, \text{SUSPENDED}\}$ — trạng thái (§14).

Các đại lượng phái sinh, viết rõ để tránh nhầm khung:

$$
\text{EQ} = \frac{h+l}{2}, \qquad
\text{pd}(p) = \frac{p - l}{h - l} \in [0,1], \qquad
\text{location}(p) = \begin{cases}\text{deep discount} & \text{pd}<0.25\\ \text{discount} & 0.25\le\text{pd}<0.5\\ \text{premium} & 0.5<\text{pd}\le 0.75\\ \text{deep premium} & \text{pd}>0.75\end{cases}
$$

> [!note] Vì sao `pd` là số tốt hơn "premium/discount" nhị phân
> `pd` là biến **liên tục**, nên nó (a) tính được trung bình/thống kê, (b) không mất thông tin ở ranh giới, (c) cho phép đo độ nhạy — nếu đổi neo low đi 20 pip mà kết luận "premium" đổi thành "discount", bạn biết kết luận của mình **không bền** (fragile). Vault đã có tiền lệ làm đúng việc này trong một phiên debate: kết luận "9.3% depth" được kiểm lại với neo low thay thế và ra 37.3% — cùng kết luận, nên **bền**. Đó là mẫu thao tác nên trở thành chuẩn. Xem [[tong-hop-phien-debate-2026-08-03]].

![[DR-Deep-11-Fragility-Test.svg|740]]
*Hình 2 — Fragility test: đổi neo ±1 bậc rồi đo lại `pd`. Panel 1–2 kết luận bền; panel 3 lật từ discount sang premium → range nằm sát EQ, mọi kết luận P/D là nhiễu.*

### 3.3. Trả lời 7 câu hỏi con của §5.1

**1) Dealing Range chính xác là gì?** Xem §3.2. Một cặp neo + metadata. Trong thực hành: hai đường ngang trên chart + một dòng ghi chú nói vì sao chọn chúng.

**2) ICT dùng khái niệm này thế nào?** Dùng làm *khung đo vị trí* để phân phối premium/discount, và làm *bản đồ liquidity* (internal bên trong, external ở hai đầu). Trong ICT 2022 Model, range thường được rút ngắn thành "range của nhịp gần nhất có sweep + displacement + FVG", tức là DR-1 và DR-4 bị trộn vào nhau một cách không tuyên bố. **[C]**

**3) Khác gì với simple price range / consolidation range / trading range / swing range?**

| Khái niệm | Định nghĩa | Khác DR ở đâu |
|---|---|---|
| **Simple price range** | `max(high) − min(low)` trên một cửa sổ bất kỳ | Không có tiêu chí chọn neo → không có ý nghĩa cấu trúc. DR là price range **có tiêu chí** |
| **Consolidation range (DR-2)** | Vùng đi ngang, biên bị test nhiều lần | Là *trạng thái thị trường*, không phải khung đo. Consolidation có thể **nằm bên trong** một DR |
| **Trading range** | Thường dùng đồng nghĩa với consolidation, hoặc đồng nghĩa với DR trong tài liệu ICT cũ hơn | **Thuật ngữ mơ hồ** — phải hỏi người nói ý gì |
| **Swing range** | Khoảng giữa hai swing bất kỳ | Không có lọc significance → trùng với DR chỉ khi hai swing đó tình cờ là neo đúng |
| **HTF dealing range** | DR vẽ trên khung lớn (D1/W1), dùng làm macro context | **Cùng định nghĩa, khác tham số $\tau$** — không phải khái niệm khác |
| **Internal dealing range** | DR vẽ trên khung nhỏ / bên trong leg của range lớn | **Cùng định nghĩa, khác vị trí phân cấp** |

> [!important] Kết luận quan trọng: "HTF dealing range" và "internal dealing range" KHÔNG phải hai loại khái niệm
> Chúng là **cùng một cấu trúc dữ liệu** ở hai tham số khác nhau ($\tau$ và vị trí lồng nhau). Hệ quả thực tiễn: bạn không cần học "5 loại dealing range" — bạn cần **một định nghĩa + một quy tắc phân cấp**. Đây là lý do §11 và §13 tồn tại.

**4) Một Dealing Range có nhất thiết phải là major swing high → major swing low?** **Không.** Range chỉ cần hai neo **cùng cấp significance tương đương** với timeframe đang phân tích. Một range H1 có neo là hai swing H1 là hợp lệ; nó không cần neo là cực trị D1. Ngược lại, range dùng cho **bias D1** thì neo phải là swing *cấp D1* — đây chính là chỗ lỗi "dùng range M5 để kết luận bias D1" phát sinh. Tiêu chí là **khớp cấp**, không phải **kích thước tuyệt đối**. → §20.

**5) Dealing Range có thể thay đổi theo timeframe không?** Có, và **phải** — vì neo được chọn theo cấp swing của timeframe đó. Đây là lý do phải ghi `timeframe` vào frontmatter của mọi lần đo. Nhưng lưu ý: nội dung *cấu trúc* bên dưới có thể giống nhau; cái đổi là **độ phân giải**.

**6) Có thể tồn tại nhiều nested dealing ranges cùng lúc không?** Có, và gần như luôn luôn như vậy. Đếm trung bình trên một chart D1→M5 có thể có 4–8 range hợp lệ cùng tồn tại. **Đây không phải vấn đề cần "giải quyết" — đây là thuộc tính của dữ liệu.** Vấn đề chỉ phát sinh khi bạn cần **một** kết luận từ nhiều range mâu thuẫn; đó là bài toán của §13.

**7) Hierarchy giữa chúng là gì?** Ba tầng chức năng, không phải ba tầng "đúng/sai":

```text
TẦNG A — MACRO RANGE (D1 / W1)         ← quyết định HƯỚNG được phép & DOL cấp lớn
   │  (đo pd để biết giá đắt/rẻ ở cấp lớn)
   ├── TẦNG B — STRUCTURAL RANGE (H4 / H1)  ← quyết định VÙNG POI & nhịp trung gian
   │      │  (đo pd để biết nhịp hồi đã đủ sâu chưa)
   │      └── TẦNG C — EXECUTION RANGE (M15 / M5)  ← quyết định ĐIỂM VÀO & stop
   │             (đo pd để chọn array trong vùng đã được Tầng A+B cho phép)
```

**Quy tắc phân xử:** Tầng trên **không** phủ quyết tầng dưới về *điểm vào*, nhưng phủ quyết về *hướng*. Nếu Tầng A nói "chỉ Long" và Tầng C đang cho setup Short đẹp, bạn **không** short — bạn chờ Tầng C đồng thuận. Ngược lại, Tầng C được phép **trì hoãn** lệnh mà Tầng A cho phép (chờ giá vào array) — đó là toàn bộ mục đích của nó.

---

## 4. Dealing Range KHÔNG phải là gì

Danh sách này quan trọng ngang §3, vì phần lớn lỗi thực chiến là **dùng range cho việc nó không làm được**.

| # | Ngộ nhận | Vì sao sai | Hệ quả thực chiến |
|---|---|---|---|
| 1 | "Range là vùng mua/bán" | Range là **thang đo**, không phải vùng lệnh. Vùng lệnh là PD array (FVG/OB) bên trong nó | Vào lệnh ở "đầu discount" thay vì ở array → stop xa, entry xấu |
| 2 | "Premium = bán, Discount = mua" | Đây là **quy tắc vị trí có điều kiện**, không phải quan hệ nhân quả. Trong downtrend mạnh, discount là nơi **bán tiếp** | Bắt dao rơi ở discount của xu hướng giảm |
| 3 | "Range là tín hiệu vào lệnh" | Range không có trigger. Trigger đến từ sweep + MSS + displacement | Trade quá mức: mọi lúc đều "có range" nên mọi lúc đều "có setup" |
| 4 | "Range là chỉ báo động lượng / độ mạnh" | Chiều cao range nói về **biến động**, không nói về **hướng** | Nhầm range rộng với trend mạnh (range rộng thường = biến động cao, hai chiều) |
| 5 | "Range là Fibonacci" | Fib chỉ là **cách chia** một range đã có. Không có range đúng thì fib vô nghĩa | Vẽ fib trước, chọn neo sau → hindsight |
| 6 | "Có một dealing range đúng cho mỗi thời điểm" | Có **nhiều** range hợp lệ cùng lúc; cái cần là **phân cấp**, không phải tìm ra cái duy nhất | Tê liệt phân tích, hoặc đổi range đến khi thấy kết luận mình muốn |
| 7 | "Range cố định cho tới khi bị phá rõ ràng" | Range có thể **mất ý nghĩa mà không bị phá** (age/consumption); ngược lại wick qua biên không phá range | Đo P/D trên range đã chết; hoặc re-map vì một cái wick |
| 8 | "Range là thứ institutional tạo ra" | **[F] NARRATIVE** — không suy ra được từ chart. Cái quan sát được là hệ quả của việc khớp lệnh và clustering của lệnh chờ | Xây niềm tin vào một câu chuyện không thể sai → không thể sửa |
| 9 | "Range càng lớn càng quan trọng" | Significance là **cấu trúc**, không phải kích thước | Chọn range tuần cho một setup intraday → R:R chết, target không tới trong phiên |
| 10 | "Range phải bắt đầu từ đỉnh/đáy tuyệt đối của leg" | Neo hợp lệ là swing **đã xác nhận**, không nhất thiết là cực trị tuyệt đối | Neo vào một cái wick tin tức → range méo, EQ lệch (xem §26-EC7) |

---

## 5. Conceptual Foundation — vì sao cần một khung tham chiếu

Phần này trả lời câu hỏi nền tảng mà ít tài liệu ICT đặt ra: **tại sao lại cần đến range ngay từ đầu?** Nếu bạn không trả lời được câu này, bạn sẽ dùng range như một nghi thức, không phải một công cụ.

### 5.1. Ba vấn đề mà giá thô không giải quyết được

**Vấn đề 1 — Giá tuyệt đối không có nghĩa.** `NQ = 20,450`. Đắt hay rẻ? Không trả lời được nếu không có tham chiếu. Đây là **bài toán chuẩn hoá**, giống hệt chuyện "30°C" chỉ có nghĩa vì có thang đo. Range chính là **thang đo cục bộ** cho giá. Hệ quả phi thường của việc chuẩn hoá: một khi đã có `pd ∈ [0,1]`, bạn **so sánh được** giữa các ngày, các symbol, và các regime biến động. Không có `pd`, bạn không thể trả lời "setup hôm nay có giống setup tháng 3 không?" — và do đó **không thể tích luỹ thống kê**. Đây là giá trị lớn nhất của dealing range, và nó là **descriptive**, không predictive. — **[D]**

**Vấn đề 2 — Hướng không đủ; cần cả vị trí.** Một tín hiệu hướng ("cấu trúc tăng") không phân biệt được *mua ở đâu*. Trong cùng một xu hướng tăng, mua tại 20% và mua tại 90% của nhịp là **hai trade khác hẳn nhau** về kỳ vọng, dù cùng hướng. Vị trí là chiều thông tin **trực giao** với hướng. Đây là lý do cấu trúc + vị trí phải được đọc cùng nhau; thiếu một trong hai thì hệ thống không hoàn chỉnh (xem |§9.2|).

**Vấn đề 3 — Không có "vị trí tương đối" thì không có ngưỡng.** "Sâu" là bao nhiêu? "Hồi đủ" là bao nhiêu? Nếu không có range, mọi ngưỡng đều là số tuyệt đối (pip/point) — và số tuyệt đối **sai theo regime**: 80 pip là hồi sâu ở EURUSD tháng biến động thấp và là nhiễu ở tháng có NFP + CPI. `pd` tự động thích ứng vì mẫu số là chính chiều cao nhịp. — **[D], kiểm chứng được [E]**

### 5.2. Vì sao "điểm giữa" (equilibrium) lại có ý nghĩa — và ý nghĩa đó đến từ đâu

Có hai cách giải thích, **và chúng không tương đương về mức độ bằng chứng**:

**Cách 1 — Giải thích đấu giá [B]/[D].** Một range có thể được đọc như một *phiên đấu giá chưa ngã ngũ*: hai đầu là hai mức thị trường đã **từ chối** (test rồi quay lại), điểm giữa là nơi định giá "công bằng tạm thời". Cách đọc này có nền tảng trong lý thuyết đấu giá / Market Profile (khái niệm *value area*). **Giới hạn:** nó là một phép loại suy hợp lý, không phải một định luật; và bằng chứng về "value area 70%" phần lớn là quy ước trong cộng đồng, không phải kết quả bình duyệt (§28 trả lời rõ).

**Cách 2 — Giải thích phân bố lệnh [B], có bằng chứng mạnh nhất.** Các mức giá tròn và các mức hiển nhiên trên chart có **mật độ lệnh chờ cao hơn** — điều này được đo trực tiếp trên dữ liệu order flow của một dealing bank lớn (Osler, NY Fed Staff Report 125/2001; bản công bố *Journal of Finance* 58(5), 2003, tr. 1791–1819). Bài đó cho thấy: **take-profit orders phản ánh trend, stop-loss orders làm trend tăng tốc**, và **tỷ lệ khớp được yêu cầu tập trung mạnh ở các mức tròn** — vốn là những mức thường được dùng làm hỗ trợ/kháng cự. Chính sự khác biệt giữa *pattern clustering của stop-loss* và *của take-profit* giải thích vì sao hai dự đoán quen thuộc của technical analysis hoạt động: (1) trend bị đảo tại các mức hỗ trợ/kháng cự dự đoán được, (2) trend **tăng tốc** một khi các mức đó bị vượt.

**Số liệu chính xác từ nghiên cứu đó** (đã đọc bản NY Fed Staff Report 125 / xác minh qua toàn văn): dưới giả thuyết phân bố đều, mỗi tần suất khớp lệnh ≈ **1%**; nhưng cluster mạnh nhất ở đuôi `00` là ≈ **8.7%**. **9.3%** lệnh take-profit khớp đúng ở đuôi `00`, so với chỉ **4.4%** lệnh stop-loss. Và có **bất đối xứng quan trọng**: stop-loss **mua** phân bố **7.4%** ở đuôi `90–99` so với **14.4%** ở đuôi `01–10` — tức stop mua tập trung **ngay trên** mức tròn, còn take-profit thì không có bất đối xứng đó (Anderson-Darling bác bỏ tính đồng đều ở mức 0.01%).

> [!warning] Ba giới hạn của bằng chứng này — phải đọc kèm số liệu ở trên
> **(1)** Osler **KHÔNG** chứng minh giao dịch hỗ trợ/kháng cự có lãi. Giải thích "vì sao technical analysis thành công" trong bài đó là một **mô phỏng**, không phải một test lợi nhuận. **(2)** Dữ liệu là **một dealing bank, ba cặp tiền** — không phải index, không phải vàng. **(3)** Clustering được đo ở **nơi đặt lệnh**, không phải ở hành vi giá — nghĩa là nó chứng minh **lệnh tập trung ở mức tròn**, chứ không chứng minh giá phản ứng ở đó. Bài tiếp theo của chính tác giả (Osler 2005, *JIMF* — [DOI](https://doi.org/10.1016/j.jimonfin.2004.12.002)) tự giới hạn: phần lớn kết quả có ý nghĩa thống kê **"theo giờ, chứ không theo ngày"**.
>
> **Bổ sung một mảnh bằng chứng độc lập, cùng hướng:** Kavajecz & Odders-White (2004, *Review of Financial Studies* — [DOI](https://doi.org/10.1093/rfs/hhg057)) đo **limit order book** trên NYSE quanh các mức kỹ thuật và tìm thấy các mức hỗ trợ/kháng cự **trùng với đỉnh độ sâu (depth) trên order book**. Đáng chú ý về mặt diễn giải: khung của họ là **market efficiency** — technical analysis tiết lộ thông tin về **nguồn cung thanh khoản**, **không** phải về hướng giá. Đây đúng là cách đọc mà bài này đang dùng: mức giá = nơi có lệnh, không phải nơi có dự báo.

> [!important] Đọc lại dòng cuối ở trên — nó là nền tảng học thuật cho "displacement sau sweep"
> Osler mô tả đúng cái mà ICT gọi là *sweep → displacement*: khi mức bị vượt, stop bị kích hoạt, và **chính các lệnh stop đó làm giá tăng tốc**. Đây là cơ chế **[B]**, không phải narrative **[F]**. Nhưng chú ý giới hạn: dữ liệu là **một dealing bank ở FX, và là round numbers** — không phải swing highs trên chart, không phải index, và **không chứng minh quan hệ nhân quả theo nghĩa "stop gây ra trend"**. Xem §28 cho danh sách giới hạn đầy đủ.

**Vậy EQ có "sức mạnh" không?** Trả lời trung thực: **chưa có bằng chứng trực tiếp cho riêng mức 50%.** Cái có bằng chứng là (a) clustering lệnh quanh các mức hiển nhiên, (b) đảo chiều tại hỗ trợ/kháng cự, (c) tăng tốc khi mức bị vượt. EQ hưởng lợi từ (a) một cách **gián tiếp**: nó là một mức hiển nhiên với số đông trader. Nhưng coi EQ là mức có edge độc lập là một **bước nhảy chưa được chứng minh** — hãy để nó ở tầng `[D]`, dùng như **vùng không giao dịch**, không phải vùng giao dịch.

**Ba điều cần biết thêm về mức 50% — sau khi kiểm chứng nguồn:**

1. **Mức 50% KHÔNG phải là một tỷ lệ Fibonacci.** Đây là lỗi phân loại rất phổ biến (kể cả trong tài liệu trading). Nguồn gốc của quy tắc 50% là **Dow Theory / quy tắc bisection** — Hamilton mô tả các nhịp điều chỉnh thoái lui "33% đến 66%… với 50% là mức điển hình". Bài kiểm định peer-reviewed trực tiếp nhất về Fibonacci (Tsinaslanidis et al. 2022, xem §19.6) test các mức **23.6% / 38.2% / 61.8% / 100%** — **không có 50%** trong bộ test.
2. **Phép thử gần nhất với "mức 50%" đã cho kết quả phủ định.** Batchelor & Ramyar (2006, *Magic numbers in the Dow* — **discussion paper, KHÔNG peer-reviewed**) kiểm định 16 tỷ lệ trên DJIA 1914–2002 với 430 điểm đảo chiều và kết luận nguyên văn: *"A few significant ratios appear, but no more than would be expected by chance given the large number of tests we conduct."*
3. **"Value area 70%" của Market Profile cũng không có kiểm định peer-reviewed.** Con số 70% **xấp xỉ 1 độ lệch chuẩn của phân phối chuẩn (~68%)** — đây gần như chắc chắn là nguồn gốc, nhưng **không tìm thấy** nghiên cứu bình duyệt nào xác nhận nó cho dữ liệu giá. Gọi đúng tên: **quy ước của practitioner**, không phải kết quả thực nghiệm.

> [!warning] Điều này có nghĩa gì với thực hành — và điều gì KHÔNG
> **KHÔNG** có nghĩa "đừng dùng EQ". EQ vẫn hữu ích như một **ranh giới quy ước** cho các rule cứng (dải 40–60% = không giao dịch, chia quadrant, chuẩn hoá vị trí) — và những công dụng đó **không cần** EQ có "sức mạnh" nào cả.
>
> **CÓ** nghĩa: đừng xây một setup **chỉ** dựa trên việc giá chạm 50%. Một mức mà bằng chứng gần nhất nói "không nhiều hơn ngẫu nhiên" thì không thể là **lý do** cho một lệnh — nó chỉ có thể là **toạ độ** trong một lệnh có lý do khác.

### 5.3. Bản chất thật của dealing range: nó là một *prior*, không phải một *prediction*

Cách hiểu gọn nhất và hữu ích nhất:

> **Dealing range không dự báo giá. Nó làm cho các dự báo của bạn có thể so sánh được, và do đó có thể kiểm chứng được.**

Một hệ thống không có range vẫn có thể có edge — nhưng bạn sẽ không bao giờ biết chắc, vì mỗi setup là một trường hợp riêng lẻ không chuẩn hoá. Range biến "trade" thành "mẫu dữ liệu". Đây là lý do dealing range là **điều kiện tiên quyết của backtest nghiêm túc**, ngay cả khi bản thân nó không tạo ra edge nào.

---

## 6. Market Mechanics — chuyện gì thực sự xảy ra (tầng [A] và [B])

Phần này trả lời: **nếu bỏ hết thuật ngữ ICT đi, cơ chế nào khiến một "range" có thể có ý nghĩa?**

### 6.1. Năm cơ chế quan sát được

**Cơ chế 1 — Lệnh chờ tập trung ở những mức mà nhiều người cùng nhìn thấy. [B]**
Trong thị trường khớp lệnh liên tục, giá chỉ di chuyển khi có **lệnh thị trường** ăn vào **lệnh chờ**. Lệnh chờ không phân bố đều: chúng tập trung ở các mức mà nhiều thuật toán/người cùng tham chiếu (mức tròn, đỉnh/đáy rõ, mức mở phiên). Osler đo trực tiếp hiện tượng này ở FX (2003). **Suy ra:** một "đỉnh rõ" không phải là một điểm hình học — nó là một **vùng có mật độ lệnh cao hơn trung bình**.

**Cơ chế 2 — Stop orders biến thành market orders khi bị kích hoạt → tự tăng tốc. [B]**
Đây là điểm cơ học then chốt nhất trong cả bài, vì nó giải thích **displacement**: một khi giá vượt qua cụm stop, các stop đó biến thành lệnh thị trường cùng chiều, ăn hết lệnh chờ đối diện → giá đi nhanh hơn ở đúng vùng đó. Osler: "stop-loss orders tend to intensify trends"; "trends gain momentum once predictable support and resistance levels are crossed". **Suy ra:** *displacement không phải dấu hiệu huyền bí của "smart money" — nó là hệ quả cơ học của việc một cụm stop bị kích hoạt.* Đây là chỗ ICT narrative **[F]** có thể được thay bằng cơ chế **[B]** mà không mất gì về mặt thực hành.

**Cơ chế 3 — Thanh khoản là hàng tiêu hao. [A]/[B]**
Lệnh chờ ở một mức **giảm đi** sau khi bị ăn. Hệ quả có thể kiểm chứng trực tiếp trên chart: **cùng một mức, lần test thứ hai thường phản ứng yếu hơn lần đầu** (vì cụm lệnh đã mỏng đi và vị thế đã được phân bổ lại). Đây là cơ sở cho rule "pool đã quét = spent" trong [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] §5. — **[E], kiểm chứng được bằng thống kê phản ứng theo số lần test**

**Cơ chế 4 — Vị thế tồn kho phải được cân (inventory). [B]/[D]**
Một khối lệnh lớn chỉ khớp được ở nơi có đủ thanh khoản đối ứng — thường là ở cực trị. Sau khi khớp, bên khớp xong **giữ một vị thế lệch** và có động cơ đưa giá về vùng có thanh khoản hai chiều để thoát phần còn lại. Đây là giải thích hợp lý (không phải định luật) cho chu kỳ **ERL → IRL → ERL** ở [[16-Internal-External-Range-Liquidity-IRL-ERL]]. **Giới hạn:** không quan sát được trực tiếp từ chart; là `[D]`.

**Cơ chế 5 — Cấu trúc thời gian (session) làm mật độ lệnh thay đổi theo giờ. [A]**
Mật độ giao dịch không đều theo giờ. Hệ quả đo được: **cùng một mức giá, phản ứng khác nhau tùy giờ bị test**. Đây là nền tảng cơ học cho [[18-Kill-Zones]]. Lệnh short trong phiên Asia là một case đã ghi nhận trong vault (note backtest EURUSD ngày 2021-05-07, thư mục `04 - Backtesting/2026-07-10/`): setup đọc đúng về cấu trúc nhưng thất bại, và nguyên nhân được xác định là **lỗi quy trình** — thiếu cổng kiểm tra Kill Zone trước lệnh, không phải lỗi tâm lý.

### 6.2. Cái gì KHÔNG quan sát được từ chart (và do đó không được suy ra)

| Không quan sát được | Nhưng thường bị suy ra | Cách nói trung thực |
|---|---|---|
| Danh tính của bên khớp lệnh | "Institution/smart money đang mua" | "Có khối lượng khớp lớn ở vùng này, biểu hiện qua displacement + FVG" — **[A]** |
| Ý định | "Họ cố tình quét stop của tôi" | "Có một cụm stop ở dưới đó (vì có swing rõ) và giá đã đi qua nó" — **[A]/[B]** |
| Lệnh chờ ở đâu (không có order book) | "Đây là pool 500 lots" | "Đây là một mức mà nhiều người tham chiếu" — **[D]** |
| Nhân quả | "Sweep gây ra đảo chiều" | "Sweep và đảo chiều cùng xảy ra với tần suất X" — **[E]** |
| Range được "tạo ra" có chủ đích | "Họ dựng range này" | "Giá dao động giữa hai mức đã bị từ chối hai lần" — **[A]** |

> [!danger] Rule ngôn ngữ — dùng để tự kiểm tra mỗi lần viết nhật ký
> Nếu câu bạn viết có chủ ngữ là "họ", "smart money", "tổ chức", "thuật toán", "market maker" **và** động từ là một động từ ý định ("muốn", "cần", "cố", "dựng", "gom"), thì câu đó là **[F] NARRATIVE** — nó không kiểm chứng được và không được dùng làm tiền đề cho một quyết định. Viết lại thành câu mô tả quan sát được, hoặc bỏ.

---

## 7. ICT Interpretation — hệ thuật ngữ và chỗ nó mơ hồ

**[C] ICT FRAMEWORK.** Đây là cách ICT đặt tên cho các hiện tượng ở §6. Mục đích của phần này không phải để dạy thuật ngữ, mà để **chỉ ra chỗ nào thuật ngữ che mất sự mơ hồ**.

### 7.1. Bảng dịch: quan sát → thuật ngữ ICT → cái thực sự đo được

| Quan sát ([A]) | Thuật ngữ ICT ([C]) | Đo được bằng gì (operational) |
|---|---|---|
| Hai mức bị test rồi từ chối | External range liquidity (ERL) — BSL trên, SSL dưới | Giá của hai neo + số lần test + có bị close-through chưa |
| Giá đi qua một mức rõ rồi quay lại nhanh | Liquidity sweep / raid / purge | `max(penetration)` và thời gian ở ngoài mức |
| Di chuyển nhanh, thân nến lớn, để lại khoảng trống | Displacement + FVG / imbalance | Kích thước thân / ATR; chiều cao gap |
| Vùng nằm giữa hai nhịp giá | Internal range liquidity (IRL) — PD array | FVG/OB chưa bị mitigate, đo bằng % fill |
| Điểm giữa range | Equilibrium (EQ) | $(h+l)/2$ |
| Nửa trên / nửa dưới | Premium / Discount | `pd` |
| Leg hồi vào 62–79% của **leg đẩy** | OTE | Retracement của DR-4 (không phải DR-1 — xem §3.3) |
| Mức bị phá rồi giữ vai trò ngược lại | Breaker / iFVG | Chuỗi sự kiện: bị phá → giá đóng lại → vai trò đảo |
| Chuỗi cực trị cao dần/thấp dần | Market structure (HH/HL vs LH/LL) | So sánh các swing theo phân cấp (§11) |
| Nhịp đi ngược tổng thể để lấy thanh khoản đầu phiên | Judas swing / manipulation | Diễn ra trong khung giờ đầu phiên, ngược hướng DOL |
| Đích đến kỳ vọng | Draw on Liquidity (DOL) | Pool chưa spent, gần nhất, theo hướng bias |

### 7.2. Ba chỗ mơ hồ phải biết (và không được giả vờ là đã rõ)

**Mơ hồ 1 — "Dealing range" không có định nghĩa canon.** Xem §3.1 và §3.1b. ICT dùng thuật ngữ này ở các thời điểm khác nhau với các nghĩa khác nhau, và **không có tuyên bố nào mang tính định nghĩa hình thức lấy được ở dạng sơ cấp**. Cộng đồng educator thứ cấp vì thế lưu hành nhiều biến thể. **Hệ quả thực hành:** khi đọc bất kỳ tài liệu nào, câu hỏi đầu tiên phải là *"range này neo vào đâu?"*, không phải *"range này đúng không?"*.

**Mơ hồ 2 — "Internal" vs "external" phụ thuộc range đang được nói tới.** Một swing có thể là *external* của range H1 và *internal* của range D1 **cùng lúc** — và cả hai đều đúng. Đây không phải lỗi của khái niệm, mà là hệ quả của việc nó có tham số. **Hệ quả:** mọi câu nói "cái này là internal" phải kèm "internal **của cái gì**".

**Mơ hồ 3 — "Liquidity" vừa là *nơi có lệnh*, vừa là *đích đến*, vừa là *nhiên liệu*.** Ba nghĩa này dẫn tới ba hành động khác nhau. Cần phân biệt rõ: **pool** (nơi có lệnh — địa điểm), **DOL** (đích đến kỳ vọng — dự báo), **fuel** (nơi sẽ bị quét để lấy đà — chiến thuật). Vault đã xử lý việc này trong [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] §5 (bảng Judas fuel vs bearish DOL).

---

## 8. Fact vs Interpretation vs Hypothesis — bảng dịch bắt buộc

Đây là phần "kỷ luật nhận thức" của bài. Mỗi phát biểu quen thuộc về dealing range được dịch sang 4 tầng.

| # | Câu nói quen thuộc ([C]/[F]) | Quan sát thật ([A]) | Phiên bản kiểm chứng được ([E]) |
|---|---|---|---|
| 1 | "Giá ở discount nên sẽ tăng" | Giá đang ở dưới trung điểm của một khoảng được chọn | Trong tập mẫu, khi `pd < 0.35` **và** bias HTF bullish **và** có array chưa mitigate, tần suất đạt +1R có cao hơn baseline không? |
| 2 | "Range này quan trọng" | Hai neo là hai swing đã xác nhận; việc phá chúng có kèm đóng thân | Range có `S_score` cao có cho expectancy cao hơn range `S_score` thấp không? |
| 3 | "Đây là external liquidity" | Có một mức mà giá đã test ≥1 lần và chưa đóng qua | Xác suất giá chạm lại mức đó trong N nến có cao hơn một mức ngẫu nhiên cùng khoảng cách? |
| 4 | "Displacement ở đây chứng tỏ có dòng lệnh lớn" | Có nến có thân ≥ k×ATR và để lại gap | Displacement ≥ k×ATR dự báo continuation tốt hơn displacement nhỏ? |
| 5 | "Đây là internal range, chỉ để execution" | Range con nằm hoàn toàn trong range lớn | Setup trong range con cho R:R/expectancy khác setup ở biên range lớn? |
| 6 | "Range đã bị invalidated" | Giá đã đóng thân qua biên và không reclaim trong m nến | Nhóm "close-through" cho kết quả khác nhóm "wick-through" không? |
| 7 | "Họ quét stop của tôi" | Giá đi qua một mức có swing rõ rồi đảo | Tần suất đảo chiều sau khi vượt một mức "hiển nhiên" so với baseline (Osler: round-crossings ~5 lần/ngày, cascade ~1 lần/tuần — xem §28) |
| 8 | "DOL là đỉnh cũ" | Có một pool chưa spent phía trên | Pool được chọn **trước phiên** có bị chạm thường xuyên hơn pool chọn ngẫu nhiên cùng khoảng cách? |

> [!success] Cách dùng bảng này
> Mỗi khi bạn viết một câu về range trong nhật ký, tự hỏi: **câu này thuộc cột nào?** Nếu thuộc cột 1 và bạn không có cột 2/3, đó là narrative. Không cấm narrative — nhưng narrative **không được làm tiền đề cho size**, chỉ được làm tiền đề cho *hướng chú ý*.

---

## 9. Why Dealing Range Matters — và nó KHÔNG cho bạn cái gì

### 9.1. Giá trị mô tả (descriptive value) — phần vững chắc nhất

Dealing range cung cấp **năm thứ mà giá thô không cung cấp**:

| # | Giá trị | Cụ thể | Tầng |
|---|---|---|---|
| 1 | **Chuẩn hoá vị trí** | Biến giá tuyệt đối thành `pd ∈ [0,1]` → so sánh được giữa ngày/symbol/regime | **[D]** (đúng theo thiết kế, không cần bằng chứng) |
| 2 | **Buộc cam kết trước (ex-ante commitment)** | Vẽ range trước phiên buộc bạn viết ra *điều kiện invalidation* trước khi biết kết quả → giảm hindsight | **[D]** — đây là giá trị **quy trình**, rất thật |
| 3 | **Bản đồ liquidity hai đầu + bên trong** | Phân biệt "hai đầu" (chỗ stop tụ) và "bên trong" (chỗ imbalance chưa lấp) → hai loại quyết định khác nhau | **[C]/[D]**, cơ chế ở §6 |
| 4 | **Khung tính R:R** | R:R chỉ có nghĩa khi target/cấu trúc đo được; range cung cấp mẫu số | **[D]** |
| 5 | **Ngôn ngữ chung cho nhật ký** | Cho phép ghi `pd_htf`, `pd_ltf` thành số và tích luỹ thống kê | **[D]** — điều kiện tiên quyết của backtest |

> [!important] Điểm 2 là giá trị bị đánh giá thấp nhất
> "Buộc cam kết trước" nghe như chuyện tâm lý, nhưng nó là **giá trị phương pháp luận**: một range được chốt và timestamp trước phiên tạo ra một *bản ghi có thể kiểm tra*. Không có bước này, mọi kết luận về sau đều có thể bị điều chỉnh vô thức cho khớp outcome. Đây là lý do §31 yêu cầu timestamp range creation là bắt buộc.

### 9.2. Vì sao premium/discount **cần** một reference range — lập luận logic

Đây là lập luận chặt nhất trong bài, và nó không cần bằng chứng thực nghiệm vì nó là lập luận về **cấu trúc của phép đo**:

1. "Premium" và "discount" là **tính từ so sánh**. Chúng không có nghĩa tuyệt đối.
2. Mọi tính từ so sánh cần **hai vế**: cái được so và cái để so với. Không có vế thứ hai, câu "giá đang rẻ" là câu vô nghĩa.
3. **Reference range chính là vế thứ hai.**
4. Do đó: câu hỏi *"premium/discount là bao nhiêu?"* **không thể** được trả lời độc lập với câu hỏi *"so với range nào?"*. Hai câu hỏi này là **một**.

Hệ quả: mọi tranh luận kiểu "giá đang discount mà, tại sao vẫn thua?" thường là tranh luận **sai câu hỏi**. Câu hỏi đúng là "discount **của range nào**, và range đó có đang chi phối không?".

### 9.3. Giá trị dự báo (predictive value) — phần yếu, phải nói thẳng

Đây là chỗ tôi **không đồng ý** với cách trình bày phổ biến trong cộng đồng ICT.

| Loại giá trị | Có bằng chứng? | Kết luận trung thực |
|---|---|---|
| Range **mô tả** cấu trúc hiện tại | Có — hiển nhiên, quan sát trực tiếp | Vững |
| Range **chuẩn hoá** vị trí | Có — đúng theo thiết kế | Vững |
| Vị trí trong range **dự báo hướng** | **Không có bằng chứng trực tiếp** | Chưa biết |
| Mức cực trị range **hút giá** | Có bằng chứng *gián tiếp* (Osler: clustering + momentum khi vượt mức) | Hợp lý nhưng không phải cho swing highs |
| Midpoint/EQ có vai trò **cơ học** | **Không** | Nhiều khả năng chỉ là quy ước hội tụ |
| `pd` + HTF structure + DOL **cải thiện** kỳ vọng so với `pd` một mình | **Chưa kiểm định** — đây chính là H5 ở §32 | Cần backtest |

> [!warning] Phép thử bắt buộc cho bất kỳ ai tuyên bố dealing range "có edge"
> Muốn biết `pd` có thông tin dự báo, phải chứng minh nó tốt hơn **baseline ngẫu nhiên có kiểm soát khoảng cách**. Cụ thể: chọn ngẫu nhiên một mức giá cách giá hiện tại đúng cùng khoảng cách với target của bạn, và so tần suất chạm. Nếu `pd`-based selection không vượt baseline này, thì `pd` **không mang thông tin dự báo** — nó chỉ đang tương quan với khoảng cách (một biến gây nhiễu hiển nhiên: mức gần thì dễ chạm hơn). Đây là lỗi thiết kế phổ biến nhất trong mọi backtest S/R, và vault **chưa có** phép đo này.

**Kết luận của §9 — câu trả lời cho "descriptive vs predictive":**

```text
DEALING RANGE =
   90%  công cụ MÔ TẢ + CHUẨN HOÁ + RÀNG BUỘC QUY TRÌNH
 + 10%  tiềm năng DỰ BÁO CÓ ĐIỀU KIỆN (chưa kiểm định)
```

Con số 90/10 là **ước lượng phán đoán của tôi**, không phải kết quả đo. Điều quan trọng không phải con số, mà là **thứ tự ưu tiên hành động**: dùng range để *tổ chức* và *giới hạn*, không dùng để *tiên đoán*.

---

## 10. Swing Significance Framework — trả lời "swing nào đủ quan trọng?"

> [!info] Vì sao đây là phần trung tâm
> Mọi thứ phía sau (premium/discount, DOL, POI, entry) đều là **hàm của hai neo**. Nếu neo sai, toàn bộ chuỗi phía sau sai một cách hệ thống — và tệ hơn, sai **một cách tự tin**, vì mọi phép tính đều đúng trên một cái nền sai. Đây là lý do phần này dài nhất bài.

### 10.0. Trước hết: swing KHÔNG phải một khái niệm nguyên thuỷ

Một điểm cần làm rõ trước khi vào 7 chiều: **"swing" không phải một thứ tồn tại trong dữ liệu; nó là kết quả của một thuật toán phát hiện cực trị.** Cùng một chuỗi nến, `N=2` cho ra 14 swing, `N=5` cho ra 6 swing, `θ = 1.0×ATR` cho ra 4 swing. Tất cả đều "đúng" theo định nghĩa của chúng.

Hệ quả nhận thức luận, và nó quan trọng: **câu hỏi "swing nào quan trọng?" không thể trả lời trước khi bạn chốt "swing được phát hiện bằng gì".** Nếu không chốt, bạn đang so sánh các đối tượng từ những tập hợp khác nhau — và mọi xếp hạng significance đều vô nghĩa. Chi tiết kỹ thuật của việc phát hiện swing (N-bar pivot, Directional Change, change-point detection, trục nhạy↔trễ) đã có ở [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] — bài này **không lặp lại**, chỉ kế thừa kết luận: dùng **hai tầng** (structual N lớn / operational N nhỏ hoặc θ theo ATR), và **không dùng ZigZag không-replay để backtest**.

### 10.1. Bảy chiều của Swing Significance

Ký hiệu: **S** (Structural), **L** (Liquidity), **D** (Displacement), **R** (Reaction), **T** (Timeframe), **P** (Protected), **C** (Contextual).

Với mỗi chiều, tôi trình bày theo 5 bước: (1) câu hỏi bằng ngôn ngữ thường, (2) thuật ngữ ICT, (3) **cơ chế — vì sao nó quan trọng**, (4) proxy đo được, (5) cách nó lừa bạn.

---

#### S — Structural Significance (ý nghĩa cấu trúc)

**(1) Câu hỏi thường:** *"Nếu mức này bị phá, câu chuyện về xu hướng có đổi không?"*
**(2) Thuật ngữ ICT:** swing tạo BOS/MSS; swing là mốc tham chiếu của cấu trúc (HH/HL, LH/LL).
**(3) Cơ chế:** cấu trúc là **quan hệ thứ tự** giữa các cực trị, không phải các cực trị riêng lẻ. Một swing chỉ có ý nghĩa cấu trúc nếu **các swing khác được định nghĩa thông qua nó** (ví dụ: "HL gần nhất" = mốc mà mọi phân tích tiếp theo tham chiếu). Phá một swing như vậy làm **mất hiệu lực cả một tập kết luận**, không chỉ một mức giá. Đây là lý do S là **gate**, không phải điểm cộng: một swing không mang quan hệ thứ tự nào thì không có gì để mất khi bị phá.
**(4) Proxy đo được:**
- `breaks_something ∈ {0,1}` — có tồn tại ít nhất một swing khác mà việc phá swing này làm thay đổi nhãn cấu trúc (HH→LH hoặc HL→LL) không?
- `is_reference_count` — số lần swing này được dùng làm mốc trong các phân tích trước đó (đếm được trong nhật ký; proxy cho "được thị trường tham chiếu").
- `bos_origin ∈ {0,1}` — leg khởi phát từ swing này có tạo BOS ở cấp của nó không?
**(5) Cách nó lừa bạn:** một swing rất lớn về số pip nhưng **không phải mốc tham chiếu của bất kỳ cấu trúc nào** (ví dụ: đỉnh cao nhất của một nhịp tăng đã bị phá rồi, giờ chỉ còn là một mức lịch sử) → S = 0. Đây là counterexample CE-2 ở §25.

---

#### L — Liquidity Significance (ý nghĩa thanh khoản)

**(1) Câu hỏi thường:** *"Có ai đó để lệnh ở đây không, và lệnh đó đã bị lấy chưa?"*
**(2) Thuật ngữ ICT:** buy-side/sell-side liquidity, equal highs/lows, inducement, pool đã spent.
**(3) Cơ chế:** xem §6.2 — lệnh chờ tập trung ở các mức hiển nhiên và ở mức tròn (**[B]**, Osler 2003). Một swing có L cao khi nó **là nơi mà nhiều người khác đặt stop/target**: đỉnh bằng nhau (EQH), đỉnh trùng nhiều khung (PDH ≈ PWH), đỉnh tròn số. Cơ chế này **không cần** giả định ý định của bất kỳ ai — chỉ cần giả định rằng người tham gia đặt lệnh ở những mức họ nhìn thấy.
**(4) Proxy đo được:**
- `equal_level_within = |h₁ − h₂| / ATR` — có cụm đỉnh/đáy gần nhau không (ngưỡng practice ~0.1–0.2 ATR).
- `tf_stack` — số timeframe có mức trùng (D1+W1 = 2 = double-stack, giá trị cao nhất).
- `swept ∈ {0,1}` — đã bị close-through chưa (nếu rồi: L giảm mạnh — hàng tiêu hao, §6.1-cơ chế 3).
- `round_number ∈ {0,1}` — có nằm sát mức tròn không.
**(5) Cách nó lừa bạn:** **L cao ≠ quan trọng về cấu trúc.** Một mức có cụm lệnh dày nhưng không tham chiếu cấu trúc nào là **nhiên liệu**, không phải biên range (§7.2-mơ hồ 3). Và ngược lại: một swing đã bị quét có thể có L rất thấp nhưng S rất cao. Hai chiều này **đo hai thứ khác nhau** và không được cộng gộp như thể cùng loại (xem §10.7 về non-additivity).

---

#### D — Displacement Significance (ý nghĩa dịch chuyển)

**(1) Câu hỏi thường:** *"Từ mức này, giá có bật ra mạnh không — hay chỉ nhích rồi quay lại?"*
**(2) Thuật ngữ ICT:** displacement, expansion, "nến thân lớn", để lại FVG/imbalance.
**(3) Cơ chế:** đây là chiều **có nền tảng cơ học mạnh nhất trong cả bảy chiều**, vì nó đo **hệ quả của việc kích hoạt cụm stop** (§6.1-cơ chế 2). Khi giá vượt một cụm stop, các stop đó chuyển thành lệnh thị trường cùng chiều, tạo ra một cú di chuyển **nhanh hơn và để lại khoảng trống giá** — vì lệnh chờ một phía đã bị ăn hết. Nói cách khác: **displacement là dấu vết đo được của việc thanh khoản vừa bị tiêu thụ ở một mức.** Điều này khiến D trở thành chiều **gần với nhân quả nhất** trong bảy chiều — không phải vì nó "đẹp", mà vì nó là hệ quả cơ học trực tiếp.
**(4) Proxy đo được:**
$$\text{disp} = \frac{\text{|close} - \text{open|}_{\text{tổng của leg}}}{k \cdot \text{ATR}_{14}}, \qquad \text{gap} = \frac{\text{chiều cao FVG}}{\text{ATR}}$$
- `disp ≥ 1` (practice) coi là displacement; `≥ 1.5` là mạnh.
- `fvg_present ∈ {0,1}` — có để lại imbalance không.
- `close_location` — thân nến đóng ở đâu trong biên độ (đóng sát cực trị = displacement mạnh hơn đóng giữa).
**(5) Cách nó lừa bạn:** ba cái bẫy.
  - **Bẫy tin tức:** displacement do tin (CPI/NFP/FOMC) có `disp` rất cao nhưng **không phải hệ quả của cấu trúc**. Cần biến `news_driven ∈ {0,1}` nam châm hút mọi thống kê (xem §26-EC7).
  - **Bẫy gap cuối tuần:** nến có gap làm `disp` đo sai hoàn toàn.
  - **Bẫy đo sai chỗ:** displacement quan trọng là displacement **từ neo**, không phải bất kỳ cú mạnh nào gần đó. Phải đo trên leg **bắt đầu từ swing đang xét**.

---

#### R — Reaction Significance (ý nghĩa phản ứng)

**(1) Câu hỏi thường:** *"Giá đã phản ứng ở mức này bao nhiêu lần, và phản ứng đó có được giữ không?"*
**(2) Thuật ngữ ICT:** sự tôn trọng mức, "rejection", mức bị test nhiều lần; "mòn" (đã test nhiều lần thì yếu đi).
**(3) Cơ chế:** hai lực **ngược chiều nhau**, và đây là chỗ phải cẩn thận:
  - *Lực 1 (tăng R):* phản ứng lặp lại là bằng chứng rằng mức đó **có người tham gia** — nó không phải mức hình học tuỳ ý.
  - *Lực 2 (giảm R):* mỗi lần test, lệnh chờ ở đó bị ăn bớt → **mức mòn dần** (§6.1-cơ chế 3).
**(4) Proxy đo được:**
- `n_tests` — số lần giá vào trong khoảng `±0.1 × ATR` quanh neo.
- `max_penetration` — lần xuyên sâu nhất, chuẩn hoá theo ATR.
- `reaction_magnitude` — kích thước cú bật sau mỗi test, chuẩn hoá theo ATR.
- `reaction_trend` — phản ứng đang **mạnh dần hay yếu dần** qua các lần test (đây là biến thông tin nhất và hầu như luôn bị bỏ qua).
**(5) Cách nó lừa bạn:** **R không đơn điệu.** Vault đã ghi nhận một case BPR bị test 4 lần hai chiều trong 5 phiên → xếp loại chất lượng thấp nhất. Nhưng logic "test nhiều = quan trọng" vẫn rất phổ biến. Cách phân xử: **1–2 test = tăng significance; ≥3 test với phản ứng yếu dần = giảm significance.** Đây là ngưỡng **practice**, cần hiệu chuẩn.

---

#### T — Timeframe Significance (ý nghĩa theo khung)

**(1) Câu hỏi thường:** *"Swing này thuộc cấp nào? Nó có khớp với khung tôi đang phân tích không?"*
**(2) Thuật ngữ ICT:** swing degree (STL/ITL/LTL — xem [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]).
**(3) Cơ chế:** nhiễu tỉ lệ nghịch với khung. Cùng một ngưỡng % sẽ phát hiện swing "quan trọng" trên D1 và swing "nhiễu" trên M5. Do đó **T không phải một thuộc tính của swing — nó là thuộc tính của quan hệ giữa swing và khung phân tích.** Đây là lý do T là **gate**, không phải điểm: một swing M5 dùng để đo bias D1 là **sai loại**, không phải "yếu".
**(4) Proxy đo được:**
- Swing được phát hiện bằng tham số của khung nào (N hoặc θ của khung đó)?
- Leg chứa nó kéo dài bao nhiêu nến so với chu kỳ điển hình của khung?
- Nó có phải cực trị của cửa sổ lookback của khung đó không (DR-3)?
**(5) Cách nó lừa bạn:** "swing lớn trông giống swing D1". Kích thước **không** xác định cấp. Một cú giật 200 point trên M5 trong 20 phút là swing **M5**, không phải D1 — dù nó to hơn nhiều swing D1 bình thường. **Cấp được xác định bằng số nến/cấu trúc mà nó tham chiếu, không bằng số point.**

---

#### P — Protected-Swing Significance (ý nghĩa "được bảo vệ")

**(1) Câu hỏi thường:** *"Mức này có phải là mức mà cả một nhịp tiếp diễn đang dựa vào không?"*
**(2) Thuật ngữ ICT:** protected high/low (P-H, P-L); điểm mà việc bị phá sẽ làm mất hiệu lực delivery hiện tại.
**(3) Cơ chế:** một swing trở thành *protected* khi **nó là mức cuối cùng mà chuỗi BOS liên tiếp còn đứng vững trên đó**. Về mặt logic, đây là **định nghĩa đệ quy**: P-L mới nhất = swing low cuối cùng trước BOS mới nhất. Cơ chế của nó không nằm ở giá mà nằm ở **tính nhất quán của kết luận**: chừng nào P-L còn nguyên, chuỗi "BOS₁, BOS₂, BOS₃" còn hợp lệ; phá P-L làm **cả chuỗi** mất hiệu lực, không chỉ mức cuối.
**(4) Proxy đo được:**
- `is_protected ∈ {0,1}`, xác định **bằng thuật toán**: swing low gần nhất trước lần BOS gần nhất (theo hướng).
- `protection_age` — bao nhiêu nến kể từ khi nó trở thành protected.
- `protection_depth` — khoảng cách từ giá hiện tại tới nó, chuẩn hoá theo ATR.
**(5) Cách nó lừa bạn:** protected status **không phải vĩnh viễn và có thể bị lu mờ** — khi có BOS mới, protected level **dời lên**, và mức cũ trở thành "reference sâu" (chỉ có ý nghĩa nếu mức mới bị phá). Không cập nhật việc dời này là nguồn của lỗi "dùng protected level cũ để phán invalidation". Chi tiết ở §15.

---

#### C — Contextual Significance (ý nghĩa ngữ cảnh)

**(1) Câu hỏi thường:** *"Swing này có phục vụ câu chuyện đang chạy không, hay nó chỉ đẹp một cách cô lập?"*
**(2) Thuật ngữ ICT:** alignment với narrative; swing "thuộc về" range lớn hơn; có khớp DOL/biên range HTF không.
**(3) Cơ chế:** đây là chiều **yếu nhất về mặt bằng chứng** và cũng là chiều **nguy hiểm nhất**, vì nó gần như đồng nghĩa với "swing này khớp với điều tôi đã tin". Cơ chế hợp lý duy nhất đứng sau C: nếu một swing trùng với biên của một range lớn hơn (hoặc trùng một mức mà nhiều khung cùng tham chiếu), thì **cụm lệnh ở đó dày hơn** — nhưng khi đó nó đã được tính ở L. Phần còn lại của C là **tính nhất quán nội bộ của phân tích**, không phải một hiện tượng thị trường.
**(4) Proxy đo được:** rất khó. Proxy duy nhất tạm ổn là `confluence_count` — số mức tham chiếu độc lập trùng nhau tại đó (PWH + PDH + OB D1 + số tròn).
**(5) Cách nó lừa bạn — và đây là chiều phải kỷ luật nhất:**

> [!danger] C là chiều duy nhất có thể tự sinh ra chính nó
> "Swing này quan trọng vì nó khớp narrative" → nhưng narrative được xây **từ** các swing đã chọn. Đây là **vòng lặp logic** (xem §18 và §27-E13). Cách chặn duy nhất: **C không được là tiêu chí để chọn neo.** C được phép dùng để **xác nhận sau** (tăng confidence), tuyệt đối không dùng để **chọn** (tăng inclusion). Nếu bạn thấy mình đang chọn neo vì nó khớp câu chuyện — dừng lại và chọn lại bằng S, D, L.

---

### 10.2. Mô hình hai tầng: GATES + SCORES (và vì sao không dùng tổng có trọng số thuần)

Cách làm ngây thơ là `S_score = Σ wᵢ·sᵢ`. Cách đó **sai về mặt thiết kế**, vì nó cho phép bù trừ giữa các chiều không thể bù trừ. Ví dụ: một swing có L+D rất cao nhưng S = 0 (không tham chiếu cấu trúc nào) sẽ được điểm khá — trong khi thực tế nó **không thể làm neo range**, bất kể L và D. Vì vậy dùng **hai tầng**:

```text
TẦNG 1 — GATES (điều kiện cần, nhị phân, KHÔNG bù trừ được)
  G1. Đã xác nhận là swing point (không phải đáy nến đang chạy)     [noise filter]
  G2. S > 0: việc phá nó thay đổi một nhãn cấu trúc nào đó          [structural gate]
  G3. T khớp: thuộc đúng cấp của timeframe đang phân tích            [degree gate]
  → Trượt bất kỳ gate nào = LOẠI. Không chấm điểm tiếp. Không có ngoại lệ.

TẦNG 2 — SCORES (cộng được, mỗi chiều chuẩn hoá về [0,1])
  L  liquidity significance   (clustering, tf_stack, unswept, round number)
  D  displacement significance (disp, fvg_present, close_location)
  R  reaction significance     (n_tests, penetration, reaction_trend)
  P  protected significance    (is_protected, protection_depth)
  C' contextual confluence     (confluence_count — CHỈ dùng để xác nhận)
```

$$
S_{\text{swing}} = \alpha L + \beta D + \gamma R + \delta P + \varepsilon C', \qquad \sum(\alpha..\varepsilon) = 1
$$

![[DR-Deep-02-Hai-Tang-Gate-Score.svg|760]]
*Hình 3 — Mô hình hai tầng: GATES lọc cứng trước (nhị phân, không bù trừ được), SCORES chỉ dùng để xếp hạng giữa các ứng viên **đã** qua gate.*

**Trạng thái của các trọng số — nói thẳng:**

| Tầng mô hình | Trạng thái | Dùng được cho |
|---|---|---|
| Gates G1–G3 | **Rule-based**, vận hành được ngay | Loại swing rác. Đây là phần **chắc chắn đúng về logic** — không cần dữ liệu để biết rằng một swing không tham chiếu cấu trúc nào thì không thể làm neo |
| Điểm L, D, R, P | **Heuristic**, đo được | Xếp hạng ứng viên khi có nhiều lựa chọn. Đây là **semi-quantitative**, không phải định lượng |
| Trọng số α–ε | **CHƯA BIẾT.** Không được bịa | Chỉ có giá trị sau khi hiệu chuẩn theo §29.3 |
| `S_score` như tín hiệu | **Chưa kiểm định** | Chưa dùng để quyết định size hay bỏ lệnh |

> [!warning] Điều tôi từ chối làm: gán trọng số
> Tôi **không** viết "α = 0.35, β = 0.25..." vì không có cơ sở thực nghiệm nào cho các con số đó, và một con số bịa sẽ được dùng như thể nó có thẩm quyền. Cách duy nhất để có trọng số là hiệu chuẩn trên dữ liệu của chính bạn (§29.3 + §32-H3). Trong lúc chưa có, dùng **thứ tự từ điển (lexicographic)** thay vì tổng có trọng số — xem §13.2.

### 10.3. STRUCTURAL SIGNIFICANCE ≠ VISUAL SIZE — phần đào sâu bắt buộc

Đây là điểm quan trọng nhất của §10, và tôi sẽ chứng minh nó bằng **so sánh số cụ thể** thay vì khẳng định.

**Hai swing trên cùng một chart (ví dụ minh hoạ, không phải dữ liệu thật):**

| | Swing A | Swing B |
|---|---|---|
| Biên độ (đo từ đỉnh tới đáy liền kề) | **220 point** | **45 point** |
| Vị trí | Đỉnh cao nhất trong 3 ngày | Đáy của nhịp hồi cuối cùng |
| Có phá gì khi bị phá? | **Không** — nhịp tăng sau nó đã vượt nó rồi, và mọi phân tích hiện tại đã tham chiếu các mức mới hơn | **Có** — nhãn HL hiện tại biến mất, chuỗi BOS mất hiệu lực |
| Có phải điểm khởi phát displacement? | Không — đỉnh này bị vượt bằng một nhịp grind | **Có** — nhịp bật từ nó để lại FVG M15 và tạo BOS |
| Liquidity ở đó | Đã bị quét | Chưa bị quét (equal lows phía dưới) |
| **Gates** | G1 ✓, **G2 ✗** | G1 ✓, G2 ✓, G3 ✓ |
| **Kết luận** | **LOẠI** (220 point nhưng S = 0) | **DÙNG LÀM NEO** (45 point) |

**Vì sao điều này đúng — lập luận, không phải khẩu hiệu:**

1. **Neo range có chức năng là *mốc tham chiếu*, không phải *mốc kích thước*.** Chức năng đó chỉ hoàn thành nếu có các kết luận khác phụ thuộc vào nó. Swing A không gánh kết luận nào → nó là một *sự kiện lịch sử*, không phải một *biên*.
2. **"To" theo nghĩa point là đại lượng không chuẩn hoá.** 220 point ở NQ giai đoạn biến động cao ≈ 45 point ở giai đoạn thấp. Trong khi đó **quan hệ cấu trúc thì chuẩn hoá sẵn** — nó là quan hệ, không phải độ lớn. Đây là lý do S mạnh hơn kích thước **về mặt cấu trúc**, không chỉ về mặt thực nghiệm.
3. **Swing A còn có hại:** đưa nó vào làm neo sẽ **nới rộng range giả tạo** → `pd` bị nén về giữa → mọi vùng premium/discount trở nên vô nghĩa (mọi thứ đều gần EO). Đây là cơ chế của counterexample CE-1/CE-4 ở §25.

> [!important] Hệ quả thiết kế cho quy trình của bạn
> Bước 1 khi chọn neo **không được** là "tìm swing lớn nhất". Bước 1 phải là **"tìm swing mà việc phá nó làm đổi nhãn cấu trúc"** — tức là chạy **G2 trước**, rồi mới xếp hạng phần còn lại bằng L/D/R/P. Đảo thứ tự này là lỗi hệ thống, không phải lỗi lẻ tẻ.

![[DR-Deep-03-Structural-vs-Visual.svg|740]]
*Hình 4 — Structural significance ≠ visual size. Swing 220 point bị LOẠI vì G2 = 0 (phá nó không đổi nhãn cấu trúc nào); swing 45 point được chọn làm neo vì nó gánh chuỗi BOS.*

### 10.4. Bốn tiêu chí "cứng" — bảng vận hành gọn

Trả lời trực tiếp câu hỏi trung tâm của bạn ("swing nào nên dùng / không nên dùng / tiêu chí objective là gì"):

| Swing | Dùng làm neo? | Điều kiện objective |
|---|---|---|
| Swing mà **phá nó không đổi nhãn cấu trúc nào** | **KHÔNG** | G2 = 0 |
| Đáy/đỉnh của nến đang chạy (chưa có nến xác nhận) | **KHÔNG** | G1 = 0 (xem [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] §2) |
| Swing của khung nhỏ hơn dùng để đo khung lớn | **KHÔNG** | G3 = 0 |
| Swing có BOS + displacement + chưa spent liquidity | **CÓ — ưu tiên 1** | G1∧G2∧G3 ∧ (D ≥ 1) ∧ (L chưa spent) |
| Swing có S nhưng không có D, không có L | **CÓ, nhưng là neo thứ cấp** | Dùng khi không có ứng viên ưu tiên 1; hạ confidence |
| Swing trùng mức liên khung (PWH≈PDH) | **CÓ — ưu tiên cao nhất về L** | `tf_stack ≥ 2` |
| Swing nằm trong leg của neo mạnh hơn | **KHÔNG cho range chính; CÓ cho range con** | Thuộc Tầng B/C, không phải Tầng A |

### 10.5. Non-additivity — vì sao các chiều KHÔNG cộng tuyến tính

Đây là điểm kỹ thuật mà mọi thang điểm đơn giản bỏ qua:

| Cặp chiều | Quan hệ | Hệ quả |
|---|---|---|
| **S × D** | **Cộng hưởng mạnh** | S cao + D cao = neo tốt nhất (BOS có displacement). S cao + D thấp = "structural nhưng grind" → dễ bị xuyên qua lần sau |
| **L × D** | **Cộng hưởng, nhưng thứ tự quan trọng** | L chưa spent + D cao = sweep-and-reverse chất lượng cao. L đã spent + D cao = continuation, **không** phải reversal |
| **R × L** | **Đối kháng** | Test nhiều lần: R tăng (danh nghĩa) nhưng L giảm (lệnh bị ăn). **L phải thắng** — mức đã bị ăn nhiều lần không còn là pool |
| **P × S** | **Gần như trùng** | Protected gần như là hệ quả của S. Đếm cả hai là **double-counting** |
| **C × mọi thứ** | **Nguy hiểm** | C tương quan với việc bạn đã tin gì (vòng lặp, §10.1-C) |

> [!important] Hai rule kỹ thuật rút ra
> **(1)** Khi cộng điểm, **giảm trọng số P** vì nó phần lớn trùng với S — nếu không bạn đang tính S hai lần và mô hình sẽ luôn ưu tiên neo "protected" một cách giả tạo.
> **(2)** Khi R và L xung đột, **L thắng**. Đây là rule có cơ chế rõ (§6.1-cơ chế 3: thanh khoản là hàng tiêu hao) và nên được coi là một trong số ít rule có nền tảng cơ học.

### 10.6. Ba cái bẫy đo lường của chính framework này

Nói thẳng về điểm yếu của mô hình tôi vừa dựng:

| Bẫy | Mô tả | Cách giảm thiểu |
|---|---|---|
| **Bẫy chuẩn hoá ATR** | Mọi ngưỡng đều dùng ATR — nhưng ATR bị chính cú displacement làm phồng lên, tạo vòng lặp (displacement lớn → ATR tăng → displacement tiếp theo trông nhỏ) | Dùng ATR **trễ** (ATR của cửa sổ kết thúc trước khi leg bắt đầu), không dùng ATR hiện tại |
| **Bẫy "swing đã xác nhận"** | Cần N nến để xác nhận swing → tại thời điểm xác nhận, giá đã đi xa. Mọi thống kê theo kiểu "tại thời điểm T tôi biết gì" phải tính cả độ trễ này | Ghi `t_confirm = t_swing + N`, dùng `t_confirm` làm mốc causal, không dùng `t_swing` |
| **Bẫy chọn ứng viên** | Nếu bạn chỉ chấm điểm những swing mình **đã** để ý, thang điểm đang xếp hạng một tập đã bị lọc bằng mắt | Chạy gate trên **toàn bộ** swing do thuật toán phát hiện, không chỉ trên swing "nhìn thấy" |

---

## 11. Swing Classification Algorithm — phân cấp swing (và kiểm tra xem phân cấp đó có hợp lý)

### 11.1. Kiểm tra phân cấp đề xuất trong đề bài — cái nào đứng, cái nào phải sửa

Bạn đề xuất 5 cấp: Micro → Internal → Intermediate structural → External/dealing-range → Major HTF. Đánh giá thẳng:

| Cấp đề xuất | Có hợp lý? | Vấn đề | Sửa thế nào |
|---|---|---|---|
| **1. Micro swing** | ✓ | Không có tiêu chí phân biệt với "nhiễu" | Định nghĩa bằng **cấp cấu trúc nó tham chiếu = 0**: không có kết luận nào phụ thuộc vào nó |
| **2. Internal swing** | ✓ | "Internal" là **quan hệ**, không phải **cấp** — internal *của cái gì*? | Đổi thành: swing mà việc phá nó đổi cấu trúc **bên trong** một leg, không đổi cực trị range |
| **3. Intermediate structural** | ✓ | Ranh giới với cấp 2 và 4 mờ | Neo vào **khung trung gian** trong workflow (H1/H4) — xem [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]] |
| **4. External / dealing-range** | ⚠ **Trộn hai thứ** | "External" là *vai trò* (nằm ở biên range). "Dealing-range swing" là *hệ quả* của việc đã chọn nó làm neo. Gộp hai cái vào một cấp là **vòng lặp**: swing là external vì nó là neo, và nó là neo vì nó external | Tách: **cấp 4 = cấp cấu trúc** (đổi cực trị của range đang chi phối); **"external" là thuộc tính vai trò**, gán sau khi chọn range |
| **5. Major HTF swing** | ✓ | Trùng lặp với cấp 4 về bản chất, khác tham số $\tau$ | Giữ, nhưng hiểu là **cấp 4 ở $\tau$ lớn hơn** — không phải loại khác |

> [!important] Sửa quan trọng nhất: phân cấp phải dựa trên **PHẠM VI VÔ HIỆU**, không dựa trên kích thước hay tên gọi
> Định nghĩa vận hành duy nhất đứng vững được: **cấp của một swing = cấp của cấu trúc cao nhất mà tính hợp lệ của nó phụ thuộc vào swing đó.** Nói cách khác, câu hỏi phân cấp không phải *"swing này to hay nhỏ?"* mà là *"nếu swing này bị phá, có bao nhiêu kết luận trước đó mất hiệu lực?"* Đây là định nghĩa **đệ quy, đo được, và không phụ thuộc cách nhìn**.

### 11.2. Thuật toán phân cấp (5 cấp, có tiêu chí)

```text
INPUT: tập swing đã xác nhận (từ thuật toán phát hiện), tập BOS/MSS đã ghi nhận theo từng khung
OUTPUT: cấp của mỗi swing ∈ {L1 Micro, L2 Internal, L3 Intermediate, L4 External, L5 Major}

VỚI MỖI swing x (theo thứ tự thời gian):
  L(x) = 1                                    # mặc định: micro
  NẾU tồn tại kết luận cấu trúc nào đó phụ thuộc vào x:
      L(x) = 2                                # internal: có vai trò, nhưng trong nội bộ leg
  NẾU việc phá x đổi nhãn cấu trúc của KHUNG TRUNG GIAN:      # ví dụ H1 trong workflow D1→H1→M5
      L(x) = 3
  NẾU việc phá x đổi CỰC TRỊ của range đang chi phối ở khung đó:
      L(x) = 4
  NẾU việc phá x còn làm mất hiệu lực cấu trúc ở khung CAO HƠN (xác nhận bằng BOS ở khung đó):
      L(x) = 5
  # cấp cuối cùng = cấp cao nhất thỏa mãn. Không cộng dồn.
```

> [!info] Có một hệ phân cấp khác đang lưu hành, và nó gần như trùng với thuật toán trên
> Kết quả tra cứu cho bài này ghi nhận một hệ phân cấp swing **đệ quy** được quảng bá là "zero judgment": nến có high cao hơn nến liền trước và liền sau = **STH** (short-term high); STH được flank bởi các STH thấp hơn = **ITH**; ITH được flank bởi các ITH thấp hơn = **LTH**. Và quan trọng nhất: *"LTH/LTL: Governing swings; **define the dealing range**"*; *"The dealing range itself is simply the span between the governing swings"* — [ictkillzone, Swing Point Hierarchy](https://www.ictkillzone.com/ict-swing-point-hierarchy) (**nguồn thứ cấp, vendor**).
>
> **Đánh giá thẳng:** hệ này **cùng nguyên lý** với thuật toán ở §11.2 (đệ quy, không dùng kích thước) và cùng nguyên lý với phân cấp STL/ITL/LTL đã có trong vault ([[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]). Sự hội tụ từ hai hướng độc lập là **bằng chứng yếu nhưng thật** rằng cách tiếp cận này là tự nhiên, không phải dị biệt.
>
> **Nhưng phải nói rõ hai điều:** (1) **không có nguồn ICT nào xác nhận** liên kết "LTH/LTL định nghĩa dealing range" — đó là khẳng định của vendor; (2) chính nguồn đó, ở **trang khác**, lại viết *"eyeballing 'significant swings' re-imports the subjectivity it deletes"* trong khi trang dealing range của họ lại khuyên *"when in doubt, look for the clearest, most obvious swing high and low"* — **tự mâu thuẫn trong cùng một nhà xuất bản**. Đây là minh hoạ hoàn hảo cho §1-điểm 1: ngay cả người dạy cũng không nhất quán giữa "cơ học hoá" và "nhìn cái rõ nhất".

**Ba tính chất của thuật toán này, và vì sao chúng quan trọng:**

1. **Nó đệ quy, nên nó tự cập nhật.** Cấp của một swing **không phải thuộc tính cố định** — nó thay đổi khi cấu trúc quanh nó thay đổi. Đây là câu trả lời cho câu hỏi "một swing có thể chuyển classification theo thời gian không?" → **Có, và đây là hành vi đúng, không phải lỗi.**
2. **Nó không dùng kích thước.** Không có tham số point/pip nào → không thể "trông to nên chắc là cấp 4".
3. **Nó phụ thuộc workflow.** Cấp 3 được định nghĩa là "khung trung gian **của bạn**". Hệ quả: **cùng một chart, hai trader có workflow khác nhau sẽ phân cấp khác nhau — và cả hai đều đúng trong hệ của họ.** Đây là lý do phải ghi `workflow` vào cấu hình, giống như ghi tham số.

![[DR-Deep-04-Phan-Cap-Swing.svg|760]]
*Hình 5 — Phân cấp swing: cấp = **phạm vi vô hiệu**, xác định đệ quy, không dùng tham số kích thước nào. Cấp thay đổi khi cấu trúc quanh swing thay đổi — đây là hành vi đúng, không phải lỗi.*

### 11.3. Chuyển cấp: khi nào internal trở thành external, khi nào mất significance

Bốn cơ chế chuyển cấp, mỗi cơ chế có một **điều kiện kích hoạt đo được**:

| Chuyển cấp | Điều kiện kích hoạt | Cơ chế | Ghi chú vận hành |
|---|---|---|---|
| **↑ Thăng cấp (promotion)** | Có BOS mới **tham chiếu** swing này (leg mới khởi phát từ nó và phá một cực trị) | Swing trở thành mốc của một kết luận mới | Đây là **cơ chế duy nhất** biến một internal swing thành external swing. Không có BOS tham chiếu → không thăng cấp, bất kể giá đi bao xa |
| **↓ Giáng cấp do bị vượt (supersession)** | Có BOS mới **cao hơn** nó theo hướng trend | Bảo vệ dời lên mức mới; swing cũ thành "reference sâu" | Không phải mất significance hoàn toàn — nó **quay lại** nếu mức mới bị phá |
| **↓ Mất do tiêu thụ (consumption)** | Mức đã bị close-through **và** không reclaim trong `m` nến | Thanh khoản là hàng tiêu hao (§6.1-CC3) | Đây là mất significance **thật** |
| **↓ Mất do cũ (decay)** | `range_age` lớn + không có test nào trong `k` nến + cấu trúc đã được viết lại quanh các neo mới | Mức không còn được tham chiếu | Cơ chế **yếu nhất về bằng chứng** trong bốn cơ chế này — là heuristic, cần backtest |

> [!warning] Bốn cơ chế này KHÔNG tương đương nhau về mức độ bằng chứng
> **Consumption** có nền tảng cơ học rõ (lệnh bị ăn hết) → tin được. **Supersession** là hệ quả logic của định nghĩa đệ quy → tin được. **Promotion** là hệ quả logic → tin được. **Decay** thì **không**: không ai chứng minh được rằng một mức "hết hạn" sau k nến. Nó là một niềm tin hợp lý (mức không được test thì ít người nhớ tới), nhưng phải được coi là **giả thuyết cần kiểm định (H7 ở §32)**, không phải chân lý. Nếu bạn định viết rule "range cũ quá 10 phiên thì bỏ", hãy biết mình đang dùng một heuristic chưa kiểm chứng.

---

## 12. Dealing Range Construction Algorithm — 14 bước, kèm lý do tồn tại của từng bước

> [!info] Cách đọc phần này
> Mỗi bước có 4 phần: **LÀM GÌ** (thao tác) → **WHY** (vì sao bước này phải tồn tại — nếu bỏ, hỏng cái gì) → **TIÊU CHÍ** (đo được) → **FAIL MODE**. Không có bước nào ở đây là "nghi thức": nếu không trả lời được WHY, bước đó nên bị xoá khỏi quy trình của bạn.

### Bước 1 — Xác định ứng viên swing high
**LÀM GÌ:** chạy thuật toán phát hiện swing (N-bar pivot hoặc DC threshold) trên khung mục tiêu, lấy **toàn bộ** swing high đã xác nhận.
**WHY:** vì nếu bạn chỉ liệt kê những swing mình *để ý*, bạn đã lọc bằng mắt trước khi có tiêu chí — và mọi xếp hạng phía sau chỉ là hợp thức hoá lựa chọn đó.
**TIÊU CHÍ:** danh sách có ≥1 swing; mỗi swing có `t_swing` và `t_confirm = t_swing + N`.
**FAIL MODE:** dùng ZigZag không replay → danh sách sạch giả tạo, có look-ahead. **Đây là lỗi làm hỏng toàn bộ chuỗi về sau.**

### Bước 2 — Xác định ứng viên swing low
Tương tự, đối xứng. **WHY:** range cần **hai** neo; xử lý một phía rồi mới xử lý phía kia dễ tạo thiên lệch về hướng đã phân tích trước (anchor priming).

### Bước 3 — Kiểm tra structural significance (gate G2)
**LÀM GÌ:** với mỗi swing, hỏi: *"phá nó có đổi nhãn cấu trúc nào không?"* — có → giữ; không → loại.
**WHY:** đây là **gate duy nhất thực sự loại bỏ được nhiễu**. Không có nó, bạn sẽ xếp hạng nhiễu bằng thang điểm và nhiễu sẽ thắng ở một số trường hợp (vì nó có thể có D cao do tin tức).
**TIÊU CHÍ:** tồn tại ít nhất một nhãn trong {HH, HL, LH, LL} hoặc một mốc BOS/MSS tham chiếu swing đó.
**FAIL MODE:** gọi mọi cú phá là "BOS" để hợp thức hoá việc giữ swing mình thích → gate mất tác dụng. Xem [[05-BOS-Break-of-Structure]] §lỗi.

### Bước 4 — Kiểm tra liquidity significance
**LÀM GÌ:** đo cụm (clustering), tf_stack, trạng thái spent/unswept, khoảng cách mức tròn.
**WHY:** vì L là chiều gần cơ chế khớp lệnh nhất (§6.1) — nó nói cho bạn biết **có ai đó ở đó không**, chứ không chỉ "hình dạng đẹp".
**TIÊU CHÍ:** `clustered ∈ {0,1}`, `tf_stack ≥ 1`, `swept ∈ {0,1}`.
**FAIL MODE:** đếm mọi swing low là "pool" (lỗi đã bị điểm danh trong [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]).

### Bước 5 — Kiểm tra displacement
**LÀM GÌ:** đo `disp` và sự hiện diện của FVG trên leg **bắt đầu từ** swing đó.
**WHY:** D là chiều đo **hệ quả cơ học của việc tiêu thụ thanh khoản** (§10.1-D). Nó biến "swing này có vẻ quan trọng" thành "có bằng chứng rằng lệnh ở đó đã bị ăn".
**TIÊU CHÍ:** `disp ≥ 1.0` (practice), `fvg_present ∈ {0,1}`.
**FAIL MODE:** đo displacement ở chỗ khác rồi gán cho swing; hoặc không loại `news_driven`.

### Bước 6 — Kiểm tra reaction
**LÀM GÌ:** đếm số test, độ xuyên sâu tối đa, kích thước phản ứng, và **xu hướng của phản ứng** qua các lần test.
**WHY:** vì R là chiều **hai mặt** (mức được tôn trọng ↔ mức bị mòn). Bỏ bước này thì bạn không phân biệt được "mức quan trọng" với "mức đã bị ăn 5 lần".
**TIÊU CHÍ:** `n_tests`, `max_penetration`, `reaction_trend ∈ {tăng, giảm, phẳng}`.
**FAIL MODE:** bỏ qua `reaction_trend` — đây là biến thông tin nhất và cũng bị bỏ nhiều nhất.

### Bước 7 — Kiểm tra timeframe relevance (gate G3)
**LÀM GÌ:** xác nhận tham số phát hiện swing của khung mục tiêu đã được dùng (không dùng tham số M5 cho D1).
**WHY:** vì nhiễu tỉ lệ nghịch với khung (§10.1-T) → đây là **sai loại**, không phải "yếu".
**TIÊU CHÍ:** `θ` hoặc `N` khớp cấu hình của khung.
**FAIL MODE:** dùng cùng một tham số % cho mọi khung — lỗi đã ghi trong [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] §5.3.

### Bước 8 — Kiểm tra protected status
**LÀM GÌ:** xác định bằng thuật toán `is_protected` (swing low gần nhất trước BOS gần nhất).
**WHY:** vì P có **hệ quả vận hành đặc biệt**: invalidation của range gắn trực tiếp với invalidation của luận điểm cấu trúc. Đây là bước biến range từ "một cái hộp" thành "một luận điểm có thể bị bác bỏ".
**TIÊU CHÍ:** `is_protected ∈ {0,1}`, `protection_age`, `protection_depth`.
**FAIL MODE:** không cập nhật khi bảo vệ dời lên → dùng mức bảo vệ cũ để đánh giá invalidation (§15).

### Bước 9 — Kiểm tra quan hệ với cấu trúc khung cao hơn
**LÀM GIÌ:** xác nhận neo này **không mâu thuẫn** cấu trúc HTF (hoặc nếu mâu thuẫn, ghi nhận rõ nó là range chống HTF).
**WHY:** đây là bước duy nhất chặn được lỗi "chọn range khung nhỏ rồi tuyên bố bias khung lớn". Không phải để *phủ quyết*, mà để **gán nhãn**: một range chống HTF là hợp lệ nhưng phải được dùng như range hồi, không phải range chủ.
**TIÊU CHÍ:** `htf_alignment ∈ {thuận, trung tính, nghịch}`.
**FAIL MODE:** coi bước này là "phải khớp" → loại bỏ mọi range đảo chiều, tức là loại bỏ chính những range báo đảo chiều.

### Bước 10 — Xác định range boundary
**LÀM GÌ:** chốt `(h, l)`, ghi `t₀` (thời điểm chốt), `timeframe`, `anchor_type`.
**WHY:** vì `t₀` là **biến chống look-ahead duy nhất** trong hệ thống (§31-A4). Range không có `t₀` là range vô dụng cho nghiên cứu, dù nó có thể dùng được cho việc nhìn chart.
**TIÊU CHÍ:** có đủ `h, l, τ, t₀, anchor_type, S_score, σ`.
**FAIL MODE:** chốt range sau khi đã xem diễn biến → dữ liệu bị nhiễm, không cứu được.

### Bước 11 — Xác định equilibrium
`EQ = (h+l)/2`. **WHY:** vì cần **một** ranh giới nhị phân cho các rule cứng (dải 40–60% = không giao dịch). EQ không cần "có sức mạnh" để hữu ích — nó hữu ích như **một quy ước vận hành** (§5.2).
**FAIL MODE:** coi EQ là mức có edge độc lập.

### Bước 12 — Xác định premium / discount
Đo `pd(price)` và quadrant. **WHY:** xem §9.2 — đây là **toàn bộ** chức năng chuẩn hoá của range.
**FAIL MODE:** nhị phân hoá sớm (chỉ ghi "discount") → mất khả năng đo độ sâu và độ nhạy.

### Bước 13 — Xác định range validity
Chạy checklist §14.1, gán `σ`. **WHY:** vì nếu không gán trạng thái, bạn sẽ vô thức dùng cả range đã chết và range còn sống trong cùng một phân tích.
**FAIL MODE:** không bao giờ gán `INVALIDATED` vì tâm lý "range cũ vẫn còn giá trị".

### Bước 14 — Xác định invalidation
**LÀM GIÌ:** viết ra **trước** khi vào lệnh: giá đóng cửa ở đâu, trong bao nhiêu nến, thì range này chết.
**WHY:** đây là bước duy nhất biến phân tích thành **phát biểu có thể sai**. Không có nó, mọi kết luận đều có thể được diễn giải lại cho khớp outcome — và đó chính là hindsight bias.
**TIÊU CHÍ:** một câu dạng *"range invalidated nếu có `m` nến đóng thân ngoài `h/l` mà không reclaim"*, với `m` viết bằng số.
**FAIL MODE:** viết invalidation mơ hồ ("nếu cấu trúc đổi") → không thể kiểm tra → vô giá trị.

---

## 13. Multiple Candidate Dealing Ranges — giải bài toán "dùng range nào?"

### 13.1. Trả lời 11 câu hỏi trong đề bài

| # | Câu hỏi | Trả lời | Loại |
|---|---|---|---|
| 1 | Khi nào chọn range **lớn**? | Khi câu hỏi của bạn là **hướng** (bias, DOL cấp lớn) hoặc khi range nhỏ **không chứa đủ không gian** để target có R:R khả thi | Heuristic + arithmetic |
| 2 | Khi nào chọn range **nhỏ**? | Khi câu hỏi là **điểm vào** (POI, stop, entry), hoặc khi range lớn đã có `pd` cực trị (giá ở rìa) nên không còn phân giải | Heuristic |
| 3 | Khi nào dùng **nested**? | **Luôn luôn** — nhưng với phân vai rõ: Tầng A quyết hướng, Tầng B quyết vùng, Tầng C quyết điểm. Không bao giờ để hai tầng cùng quyết một việc | **[C] convention** |
| 4 | Khi nào range nhỏ chỉ là **internal**? | Khi nó nằm **hoàn toàn** trong range lớn **và** cả hai neo của nó có cấp < cấp neo range lớn | Rule-based, đo được |
| 5 | Khi nào range nhỏ trở thành **dominant**? | Khi range lớn bị **thay thế** (một neo bị consumption) hoặc khi range nhỏ **chứa** DOL hiện hành và range lớn thì không | Rule + judgment |
| 6 | Khi nào range cũ nên bị **thay**? | Khi `σ` chuyển sang REPLACED/INVALIDATED theo §14. **Không** thay chỉ vì range cũ → xem §14.4 | Rule-based |
| 7 | Có nên ưu tiên range **gần giá** hơn? | **Không tự động.** Ưu tiên theo *chức năng*, không theo khoảng cách. Ưu tiên theo khoảng cách là lỗi "anchor ambiguity" đã ghi trong vault | Rule |
| 8 | Có nên ưu tiên range tạo **displacement**? | **Có** — đây là một trong số ít tiêu chí có nền tảng cơ học | Rule, có cơ chế |
| 9 | Có nên ưu tiên range tạo **structural break**? | **Có, mạnh nhất** — vì đó là gate G2 | Rule (gate) |
| 10 | Có nên ưu tiên range chứa **external liquidity**? | **Có** — nhưng cẩn thận: hầu như mọi range đều có liquidity ở hai đầu. Tiêu chí thật là **liquidity chưa bị tiêu thụ** | Rule |
| 11 | Có nên ưu tiên range **aligned với DOL**? | **Không** — đây chính là vòng lặp logic (§18). DOL không được là tiêu chí **chọn** range | **[C], kỷ luật** |

> [!danger] Câu 11 là câu nguy hiểm nhất trong 11 câu
> Nếu bạn chọn range vì "nó hướng về DOL của tôi", và DOL được suy ra từ range, bạn đã tạo một hệ thống **không thể sai** — và do đó **không thể học**. Cách chặn: DOL phải có **ít nhất một bằng chứng độc lập** (bên nào vừa bị ăn, cấu trúc, mức liên khung) **trước khi** range được chốt. Xem §18.3.

### 13.2. DEALING RANGE SELECTION ALGORITHM

Vì trọng số chưa được hiệu chuẩn (§10.2), thuật toán dùng **thứ tự từ điển (lexicographic)** — so sánh theo tiêu chí quan trọng nhất trước, chỉ khi hoà mới xét tiêu chí kế. Đây là lựa chọn **có chủ ý**: nó không cho phép một ưu điểm lớn ở tiêu chí thứ yếu bù cho một thất bại ở tiêu chí chính.

```text
INPUT : tập ứng viên C = {c₁ … cₙ}, mỗi c có (h, l, τ, t₀, S_score, gates, htf_alignment, d_o_l_evidence)
OUTPUT: (PRIMARY, SECONDARY, REJECTED[]) kèm lý do

BƯỚC 1 — LỌC GATE (loại cứng, không ngoại lệ)
  C ← { c ∈ C : G1 ∧ G2 ∧ G3 }                 # xác nhận swing, có ý nghĩa cấu trúc, đúng cấp
  REJECTED += phần còn lại, lý do = "gate_fail:<Gx>"
  NẾU C = ∅ → OUTPUT = (NONE) → NO-TRADE. Dừng.

BƯỚC 2 — LỌC HIỆU LỰC
  C ← { c ∈ C : σ(c) ∈ {VALID, REFINED} }
  # REPLACED/INVALIDATED không được tham gia, kể cả khi S_score cao
  NẾU C = ∅ → NO-TRADE (chờ range mới hình thành). Dừng.

BƯỚC 3 — SẮP THEO THỨ TỰ TỪ ĐIỂN (từ quan trọng nhất)
  khoá 1: gate_strength        # G2 ∧ (D≥1) ∧ (L chưa spent)  → nhóm "neo cấp 1"
  khoá 2: unswept_liquidity    # số đầu range còn pool CHƯA bị tiêu thụ (0,1,2)
  khoá 3: containment          # range nào CHỨA range nào (range lớn thắng ở Tầng A)
  khoá 4: S_score              # chỉ dùng khi các khoá trên hoà
  khoá 5: age (mới hơn thắng)  # tie-break cuối, và CHỈ ở đây age mới được dùng

BƯỚC 4 — GÁN VAI
  PRIMARY   = phần tử đầu tiên sau sắp xếp
  SECONDARY = range con nằm trong PRIMARY có S_score cao nhất   # dùng cho execution
  NẾU tồn tại ≥2 range ở các TẦNG khác nhau cho KẾT LUẬN pd MÂU THUẪN:
      ghi nested_conflict = true
      → giảm size 50%, HOẶC no-trade nếu conflict ở Tầng A vs Tầng B

BƯỚC 5 — KIỂM TRA NHẤT QUÁN VỚI DOL (chỉ để XÁC NHẬN, không để chọn)
  NẾU DOL_evidence độc lập nằm NGOÀI hướng mà PRIMARY cho phép:
      ghi dol_conflict = true → không đổi PRIMARY; hạ confidence; size −50%
```

**Vì sao thứ tự khoá lại như vậy — lý do từng khoá:**

- **Khoá 1 (gate strength)** trước tiên vì đây là tiêu chí duy nhất có nền tảng cơ học (§6.1). Một neo không có D và không có L chưa tiêu thụ thì không có lý do cơ học nào để được chọn.
- **Khoá 2 (unswept liquidity)** trước S_score vì thanh khoản là **hàng tiêu hao, tính chất bất đối xứng**: một đầu range đã bị tiêu thụ nghĩa là range đã mất một nửa chức năng (chỉ còn một hướng draw). Thông tin này quan trọng hơn sắc thái của thang điểm.
- **Khoá 3 (containment)** trước S_score vì lồng nhau là quan hệ **cấu trúc**, không phải mức độ.
- **Khoá 5 (age)** xuống cuối cùng — và điều này có chủ ý: **age không có nền tảng bằng chứng** (§11.3), nên nó chỉ được dùng khi mọi tiêu chí khác hoà. Đưa age lên cao là đưa một heuristic chưa kiểm chứng vào vị trí quyết định.

![[DR-Deep-05-Chon-Range-Funnel.svg|760]]
*Hình 6 — Thuật toán chọn range: 7 ứng viên → hai bộ lọc cứng → sắp thứ tự từ điển → PRIMARY / SECONDARY / REJECTED. Ghi lý do loại là bắt buộc — không có nó, bạn không biết gate nào đang thực sự loại swing trên dữ liệu của mình.*

### 13.3. Ba tình huống đặc biệt và cách xử lý

**Tình huống A — Hai range ngang cấp, kết luận P/D mâu thuẫn, không range nào vượt trội.**
Xử lý: **đây là một kết luận, không phải sự bất lực.** Ghi `no-trade` với lý do `ambiguous_structure`. Theo cơ chế §6.1-cơ chế 4, nhiều range cùng hợp lệ mà không range nào có draw rõ = **chưa có delivery nào đang dang dở** = chưa có gì để trade. Chờ cú quét biên của tầng lớn nhất.

**Tình huống B — Range nhỏ mâu thuẫn range lớn về `pd` (D1 premium, H1 discount).**
Xử lý: **không phải mâu thuẫn — đây là trạng thái bình thường và có tên.** Nghĩa là: giá đang hồi trong một nhịp hồi, và nhịp hồi đó đã đi xa trong range nhỏ nhưng chưa xa trong range lớn. Đây là cấu hình của **setup continuation**: chờ H1 hết discount (về premium H1) hoặc chờ array HTF trong discount D1.
→ Quy tắc: **range lớn quyết định được phép làm gì; range nhỏ quyết định làm lúc nào.** (Xem §20.4.)

**Tình huống C — Range cũ (S_score cao, đã lâu) vs range mới (S_score thấp, vừa hình thành).**
Xử lý: cũ không tự động thắng. Kiểm tra **consumption** của range cũ trước (§11.3). Nếu range cũ còn unswept hai đầu → nó vẫn là PRIMARY (Tầng A) và range mới là SECONDARY (Tầng C). Nếu range cũ đã bị tiêu thụ một đầu và không còn draw rõ → **REPLACED**, chuyển sang range mới.

---

## 14. Range Validity & Invalidation

### 14.1. Định nghĩa: một Dealing Range VALID khi nào?

Sáu điều kiện, chia hai nhóm. Nhóm A là **cứng** (thiếu là invalid), nhóm B là **chất lượng** (thiếu là yếu, không invalid):

**Nhóm A — điều kiện cứng (necessary):**

| # | Điều kiện | Đo được bằng |
|---|---|---|
| A1 | Hai neo là swing **đã xác nhận** ở đúng cấp của khung | `t_confirm` đã qua; tham số khung khớp |
| A2 | Mỗi neo tham chiếu ít nhất một kết luận cấu trúc (G2) | `breaks_something = 1` |
| A3 | **Ít nhất một** đầu range còn liquidity chưa bị tiêu thụ | `unswept_count ≥ 1` |
| A4 | Range được chốt **trước** khi sự kiện đang được đánh giá xảy ra | `t₀ < t_event` |

**Nhóm B — điều kiện chất lượng (không bắt buộc, ảnh hưởng confidence):**

| # | Điều kiện | Đo được bằng |
|---|---|---|
| B1 | Cả hai đầu còn unswept | `unswept_count = 2` |
| B2 | Có displacement ở ít nhất một neo | `disp ≥ 1` |
| B3 | Có internal array (FVG/OB) chưa mitigate ở nửa đúng hướng | `internal_poi ∈ {0,1}` |
| B4 | Range nhất quán cấu trúc với khung cao hơn | `htf_alignment = thuận` |
| B5 | Có 1–2 test ở mỗi neo với phản ứng **không suy giảm** | `1 ≤ n_tests ≤ 2` |

> [!important] Vì sao A3 là điều kiện cứng mà không phải "cả hai đầu" (B1)
> Vì một range còn **một** đầu unswept vẫn có **một hướng draw** — vẫn dùng được để định vị và để trade continuation. Yêu cầu cả hai đầu là quá chặt: sau khi giá quét một đầu (điều rất thường xảy ra), mọi range sẽ bị coi là invalid, và bạn sẽ re-map liên tục. **Range một đầu unswept là trạng thái bình thường, không phải trạng thái lỗi.** Đây là một trong những chỗ mà "sách vở" (yêu cầu lý tưởng) và "vận hành" (yêu cầu tối thiểu) khác nhau, và vận hành phải thắng.

### 14.2. Phân loại 9 trường hợp — chúng thực sự thay đổi cái gì?

Bảng này là trọng tâm của §14: với mỗi sự kiện, **cái gì thực sự thay đổi** trong hệ thống của bạn.

| # | Sự kiện | `σ` chuyển thành | Cái gì thực sự thay đổi | Cái gì **KHÔNG** thay đổi |
|---|---|---|---|---|
| 1 | Swing bị **wick** qua, đóng lại trong range | `VALID` (giữ nguyên) | `unswept_count` giảm 1; neo đó mất vai trò draw; range **mạnh hơn** về phía đối diện | Không đổi range, không đổi EQ. Xem [[12-Dealing-Range]] W2 |
| 2 | Swing bị **close** qua, không reclaim (m nến) | `REPLACED` | Một neo mới hình thành; range mới có `h/l` khác | Hướng bias chưa chắc đổi |
| 3 | **Protected swing** bị phá bằng body-close | `INVALIDATED` (cấp đó) | Chuỗi BOS mất hiệu lực; đổi cấp cấu trúc; DOL phải chọn lại | Range khung **cao hơn** không tự động chết |
| 4 | **Protected swing** bị phá bằng displacement + acceptance | `INVALIDATED` + `state = transition` | Như (3), cộng thêm: state chuyển từ `trend-continuation` → `transition`; CHoCH/MSS được xác nhận | Vẫn **không** tự động là đảo chiều HTF |
| 5 | **Internal structure** đổi, external chưa đổi | `REFINED` | Range con mới; vùng execution đổi | Range lớn và bias giữ nguyên — **đây là pullback bình thường** |
| 6 | **Liquidity sweep** ở một đầu rồi đảo | `VALID` | Đầu đó chuyển từ "draw" thành "spent"; draw chuyển sang đầu kia | Range giữ nguyên, thậm chí tăng confidence (neo vừa được xác nhận) |
| 7 | **External liquidity hai đầu** đều bị lấy | `INVALIDATED` | Hết draw trong range; phải tìm range mới hoặc dùng SD projection ([[31-Standard-Deviation]]) | Cấu trúc khung lớn có thể vẫn nguyên |
| 8 | **HTF trend đổi** | `INVALIDATED` (toàn bộ tầng dưới) | Mọi range con phải xét lại (cascade re-map) | — |
| 9 | **Range bị redefined** do cấu trúc mới | `REPLACED` | Neo mới, EQ mới, `pd` mới | Không phải "thất bại" — đây là vận hành bình thường |

### 14.3. Bốn khái niệm phải phân biệt (đây là nguồn gốc của việc re-map liên tục)

| Khái niệm | Định nghĩa | Dấu hiệu | Hành động |
|---|---|---|---|
| **RANGE REFINEMENT** | Range **giữ nguyên**, chỉ tinh chỉnh biên (do wick giãn) hoặc thêm range con | Neo không đổi về bản chất; chỉ số `h`/`l` dịch vài tick | **Đo lại levels mỗi sáng** (rule W4 trong [[12-Dealing-Range]]), không đổi phân tích |
| **RANGE REPLACEMENT** | Range cũ hết chức năng vì có neo mới tốt hơn | Một neo bị consumption HOẶC xuất hiện BOS tạo neo mới | Chốt range mới, timestamp, **cascade** xuống các khung nhỏ |
| **RANGE INVALIDATION** | Range mất hiệu lực hoàn toàn về cấu trúc | Protected swing bị phá bằng body-close; external cả hai đầu bị lấy | Xoá khỏi bản đồ, **không** dùng để đo P/D nữa |
| **TEMPORARY INTERNAL RANGE** | Range con tồn tại **có thời hạn** trong một leg | Nằm hoàn toàn trong range lớn; không có DOL riêng độc lập | Dùng cho **execution**; tự động hết hiệu lực khi leg kết thúc; **không** dùng để suy bias |

> [!danger] Lỗi phổ biến nhất: nhầm TEMPORARY INTERNAL RANGE với RANGE REPLACEMENT
> Khi giá hồi sâu, một range con hình thành. Phản xạ sai: coi nó là "range mới" và đo bias trên nó → bias bị kéo theo nhịp hồi → bạn long/short ngược HTF. **Rule cứng:** range con chỉ được dùng để *định thời điểm*, và nó **không có quyền** thay đổi bias cho tới khi nó thoả điều kiện REPLACEMENT (một neo của range lớn bị consumption). Trước điều kiện đó, nó là TEMPORARY.

### 14.4. Máy trạng thái (state machine) của một Dealing Range

```text
                    ┌────────────────────────────────────────────┐
                    │                                            │
   [hình thành]     │                                            ▼
   swing thứ 2  ──► VALID ──wick qua biên, close lại──► VALID (unswept_count −1)
   được xác nhận     │  ▲                                          │
                     │  └── đo lại levels (wick giãn) ── REFINED ◄──┘
                     │
                     ├── neo bị close-through / BOS tạo neo mới ──► REPLACED ──► (range mới)
                     │
                     ├── protected swing bị phá (body-close) ────► INVALIDATED ──► (chờ range mới)
                     │
                     └── cả hai đầu external bị lấy ─────────────► INVALIDATED
                     
   NẾU dữ liệu chưa đủ để phán (chưa đủ m nến sau sự kiện)  ──► SUSPENDED ──► (quyết định sau)
```

> [!success] Ba tính chất này KHÔNG phải do tôi tự nghĩ ra — chúng khớp với mô tả đang lưu hành trong cộng đồng ICT
> Kết quả tra cứu độc lập cho bài này ghi nhận các phát biểu sau từ một nguồn giáo dục ICT (thứ cấp, độ tin cậy vừa): *"a **body close** beyond the range boundary — not a wick — signals that the range has changed"*; *"The prior range high becomes the new range low of a new, higher dealing range"*; *"A dealing range expires when a body close breaks the range boundary"* — [ictkillzone, Dealing Range](https://www.ictkillzone.com/ict-dealing-range). Cùng nguồn đó mô tả việc range được vẽ lại sau khi một swing bậc cao bị vi phạm như một *"promotion event"* — trùng khớp với cơ chế **promotion** ở §11.3.
>
> **Điều này quan trọng vì hai lý do:** (1) nó cho thấy quy tắc "wick không phá range, body-close mới phá" là **quy ước ICT đang lưu hành**, không phải diễn giải riêng của bài này; (2) nó **vẫn chỉ là nguồn thứ cấp** — không có artifact sơ cấp nào của ICT xác nhận (§3.1b). Vì vậy đây là **[C] ICT CONVENTION**, không phải **[A] FACT**. Sự khác biệt có hệ quả: một quy ước có thể bị kiểm định và bị bác bỏ bằng dữ liệu; một sự thật thì không.

![[DR-Deep-06-State-Machine.svg|760]]
*Hình 7 — Máy trạng thái của một dealing range. Wick KHÔNG BAO GIỜ invalidate; `SUSPENDED` là trạng thái hợp lệ; `REPLACED` ≠ `INVALIDATED`.*

**Ba tính chất của máy trạng thái này cần nhấn:**

1. **Wick không bao giờ làm range invalid.** Đây là rule cứng và nó có cơ chế: wick qua biên = thanh khoản được tiêu thụ ở đó **nhưng không có acceptance** → neo vẫn đứng. Xem case 1 và 6 trong bảng §14.2.
2. **SUSPENDED là trạng thái hợp lệ, không phải sự do dự.** Khi sự kiện vừa xảy ra và chưa đủ `m` nến để phán, trạng thái đúng là SUSPENDED. Gán vội REPLACED/INVALIDATED tại đây chính là nguồn của re-map liên tục.
3. **REPLACED không phải INVALIDATED.** Một range bị thay thế là chuyện bình thường của vận hành (mỗi BOS tạo neo mới). Chỉ có INVALIDATED mới là "range chết vì cấu trúc bị phá". Trộn hai cái này khiến bạn cảm thấy mình "sai" mỗi khi range được cập nhật — và cảm giác sai đó đẩy bạn tới việc bám víu range cũ.

---

## 15. Protected High / Protected Low — bảo vệ đến từ đâu, và phá nó thay đổi cái gì

### 15.1. Protected swing là gì, và "protection" đến từ đâu

**Định nghĩa vận hành (đệ quy):** swing low bảo vệ (P-L) = **swing low đã xác nhận cuối cùng trước lần BOS gần nhất theo hướng tăng**. Đối xứng với P-H.

**Điều quan trọng nhất của §15 — nguồn gốc của "protection":**

> [!important] Protection KHÔNG đến từ việc ai đó đang bảo vệ mức đó
> **[C] ICT framing** thường được hiểu là "tổ chức bảo vệ mức này". **[F] NARRATIVE** đó không kiểm chứng được và không cần thiết. Nguồn gốc thật của protection là **logic nội tại của phân tích**:
>
> - Bạn đã tuyên bố một chuỗi BOS: BOS₁ → BOS₂ → BOS₃.
> - Mỗi BOS được định nghĩa là "giá vượt cực trị trước đó **mà không phá mức đáy của nhịp trước**".
> - Do đó, mức đáy cuối cùng đó là **điều kiện duy nhất** khiến chuỗi tuyên bố của bạn còn đúng.
> - **P-L "được bảo vệ" vì tính nhất quán của kết luận của bạn phụ thuộc vào nó** — không phải vì thị trường quan tâm tới nó.
>
> Hệ quả: protection là **thuộc tính của một luận điểm**, không phải thuộc tính của một mức giá. Nếu bạn đổi luận điểm (ví dụ chuyển từ "trend tăng" sang "đang phân phối"), mức được bảo vệ sẽ khác. Đây là lý do phải ghi rõ *bảo vệ **cho luận điểm nào***.

### 15.2. Có phải mọi swing tạo HH/LL đều protected? — Không

| Trường hợp | Protected? | Vì sao |
|---|---|---|
| Swing low tạo HL **và** sau đó có BOS vượt đỉnh trước | **CÓ** | Đây là định nghĩa |
| Swing low tạo HL nhưng **chưa có BOS** sau nó | **CHƯA** | Chưa có chuỗi kết luận nào để bảo vệ → chỉ là ứng viên |
| Swing low thấp hơn low trước (LL) trong xu hướng tăng | **KHÔNG** (nó là bằng chứng phá luận điểm) | Nó là swing **phá** protection, không phải swing được bảo vệ |
| Swing low bên trong một leg, không phải mốc của BOS nào | **KHÔNG** | Cấp L2 (§11.2): có vai trò nội bộ, không gánh kết luận cấp khung |
| Swing low cũ đã bị vượt bởi BOS mới hơn | **KHÔNG còn là P-L hiện hành**; nó là **"reference sâu"** | Supersession (§11.3) |

> [!warning] Điểm bị hiểu sai phổ biến nhất
> Nhiều trader coi **mọi** swing low gần nhất là "protected low". Điều đó làm cho "phá protected low" trở thành sự kiện xảy ra vài lần mỗi phiên → mỗi lần lại tuyên bố "cấu trúc đổi" → hoang mang và đảo bias liên tục. **Chỉ swing low gánh chuỗi BOS mới là protected.** Kiểm tra cứng: *"nếu mức này bị phá, chuỗi BOS nào mất hiệu lực?"* — trả lời được thì protected, không trả lời được thì không.

**Protected swing có thể bị downgrade không?** Có — và bằng ba cơ chế, giống §11.3 nhưng hệ quả nặng hơn:
- **Supersession** → nó trở thành *reference sâu* (không mất hẳn, chỉ lùi cấp).
- **Consumption** (đã bị close-through) → mất hẳn.
- **Đổi luận điểm** → nếu bạn chuyển sang khung cao hơn làm khung phán quyết, P-L của khung nhỏ không còn là P-L "thật" nữa.

### 15.3. Khi protected swing bị phá — cái gì **thực sự** thay đổi

Đây là câu trả lời cho câu hỏi #6 ở §2, và tôi tách thành 5 mục để tránh nhầm "phá = đảo chiều".

| Thay đổi | Nội dung | Có tự động không? |
|---|---|---|
| **1. Cấp cấu trúc bị phá** | Chuỗi BOS ở cấp đó mất hiệu lực. Cấp nào bị phá là **thông tin quan trọng nhất** — và nó phụ thuộc phân cấp ở §11 | Tự động |
| **2. Tập DOL phải chọn lại** | Pool phía trên mất tư cách "draw" (không còn hướng cấu trúc để tới đó); pool phía dưới trở thành ứng viên | Tự động |
| **3. Range đang chi phối** | Range cũ → `INVALIDATED` hoặc `REPLACED`; phải chốt range mới (§14.4) | Tự động |
| **4. State của thị trường** | `trend-continuation` → `pullback-in-progress` hoặc `transition` — **phải phân biệt hai cái này** (§21) | **Không** — cần thêm bằng chứng |
| **5. Bias HTF** | **KHÔNG đổi** trừ khi cấp bị phá là cấp HTF | **Không** — và đây là điểm bị vi phạm nhiều nhất |
| **6. Size/setup cho phép** | Hạ bậc: từ "continuation full size" → "reversal chờ xác nhận, nửa size" | Tự động (rule) |

### 15.4. Wick vs displacement close — hai sự kiện khác nhau về **thông tin**, không chỉ về mức độ

| Tiêu chí | Phá bằng **wick** | Phá bằng **body-close** | Phá bằng **displacement + acceptance** |
|---|---|---|---|
| Quan sát được | `max(penetration) > 0`, `close` vẫn trong range | `close` ngoài range | `close` ngoài + `m` nến giữ ngoài + thân ≥ k×ATR |
| Thanh khoản | **Đã bị tiêu thụ ở mức đó** | Đã tiêu thụ + có người chấp nhận giá mới | Đã tiêu thụ + tăng tốc (cơ chế §6.1-CC2) |
| Hệ quả cấu trúc | **Không** — neo vẫn đứng | Có — cấu trúc cấp đó đổi | Có + đổi state |
| Xác suất đảo chiều tiếp theo | Cao hơn baseline (sweep rồi reclaim) | Không rõ — phụ thuộc cấu trúc HTF | Thấp hơn baseline trong ngắn hạn (continuation) |
| Trạng thái range | `VALID` (unswept_count −1) | `REPLACED` | `INVALIDATED` + `transition` |
| **[E] Cần kiểm định** | Tần suất đảo chiều sau wick-through | Tần suất continuation sau close-through | Tần suất continuation sau displacement-through |

> [!important] Vì sao phân biệt này quan trọng hơn nó có vẻ
> Trong thực hành, ba sự kiện trên thường bị gộp thành một câu: *"cấu trúc đã bị phá"*. Nhưng chúng dẫn tới **ba hành động khác nhau** (giữ range / thay neo / chuyển state), và gộp chúng là nguyên nhân trực tiếp của hai lỗi đối xứng: (a) re-map range vì một cái wick, và (b) ở lại trong luận điểm cũ sau một cú displacement + acceptance.

### 15.5. LIQUIDITY RAID vs STRUCTURAL BREAK — bảng phân biệt

Đây là phần quan trọng nhất của §15, vì hai hiện tượng này **giống nhau ở dạng quan sát thô** (giá đi qua một mức) nhưng **ngược nhau về hệ quả**.

| Tiêu chí | **Liquidity raid** (quét thanh khoản) | **Structural break** (phá cấu trúc) |
|---|---|---|
| Mục tiêu | Đi **qua** mức để lấy lệnh chờ | Đi **qua** mức để **định giá lại** ở phía bên kia |
| Dấu hiệu về `mức` | Xuyên nông, xuyên nhanh, ít nến ở ngoài | Xuyên sâu, có nến đóng ngoài, giữ ngoài |
| Dấu hiệu về **phản ứng sau** | **Đảo chiều nhanh**, reclaim trong `1–3` nến (practice) | **Không reclaim**; pullback về mức cũ bị từ chối |
| Dấu hiệu về **displacement** | Có thể có displacement **ngược lại** sau khi quét (đây là tín hiệu chất lượng cao nhất) | Displacement **cùng chiều** với cú phá, để lại FVG phía ngoài |
| Thanh khoản sau sự kiện | Mức đó **spent**; pool phía đối diện trở thành draw | Mức đó **spent**; **cấu trúc** được viết lại; range mới |
| Hệ quả với range | `VALID` (giữ nguyên), đổi vai trò draw sang đầu kia | `REPLACED` / `INVALIDATED` |
| ICT term | Liquidity sweep / raid / purge / stop run / turtle soup | BOS (thuận trend) / MSS-CHoCH (ngược trend) |
| **[E] Test phân biệt đề xuất** | `penetration ≤ 0.3 × ATR` ∧ `bars_outside ≤ 3` ∧ có reclaim | `penetration > 0.5 × ATR` ∧ `bars_outside > 3` ∧ không reclaim |
| **Cái KHÔNG phân biệt được** | **Ý định.** Cả hai hiện tượng đều có dạng "giá vượt mức rồi hoặc không quay lại". Không có cách nào từ chart phân biệt "ai đó cố tình quét" với "cung cầu đơn thuần mạnh hơn ở phía đó" | — |

> [!danger] Rule 3 giây cho câu hỏi này
> Khi giá vượt một mức quan trọng, **không được kết luận ngay**. Đặt câu hỏi duy nhất: *"Nến đóng ở đâu, và giá giữ được phía đó bao lâu?"* Chưa có câu trả lời (chưa đủ `m` nến) → trạng thái là **SUSPENDED**, và **không được** vào lệnh mới dựa trên giả định về câu trả lời. Đây là cách duy nhất để không bị kẹt ở cả hai phía của sai lầm.

---

![[DR-Deep-07-Raid-vs-Break.svg|740]]
*Hình 8 — Liquidity raid vs structural break: cùng hiện tượng quan sát thô "giá vượt một mức", phân biệt bằng CÁCH PHÁ và PHẢN ỨNG SAU. Điều duy nhất không phân biệt được là ý định.*

## 16. Internal vs External Structure — và quan hệ với Dealing Range

### 16.1. Định nghĩa — nhắc lại cảnh báo về tham số

**External structure** của một range = cấu trúc được tạo bởi **hai neo** (cực trị của range) và các BOS phá chúng.
**Internal structure** = cấu trúc được tạo bởi các swing **nằm bên trong** range đó.

Nhắc lại §7.2-mơ hồ 2: **internal/external là quan hệ với một range cụ thể**, không phải thuộc tính tuyệt đối. Cùng một MSS có thể là *internal* của D1 và *external* của H1 — cả hai đều đúng.

### 16.2. Ba câu hỏi trọng tâm của §12 trong đề bài

**Q1. Một internal MSS có làm invalidated HTF dealing range không?**
**Trả lời: Không.** Internal MSS **không thể** phá external structure theo định nghĩa (nó phá các swing bên trong, không phá neo). Cái nó làm được:
- Chuyển state từ `trend-continuation` → `pullback-in-progress` (nếu MSS ngược hướng range).
- Tạo một **internal range** mới dùng cho execution.
- Nếu MSS đó kèm **displacement + acceptance**, nó có thể trở thành **bước đầu tiên** của một quá trình dẫn tới phá external — nhưng bản thân nó không phá.

> [!important] Rule cứng, viết ra để chống lại phản xạ
> **Internal MSS không bao giờ là lý do để đổi bias.** Nó là lý do để (a) chờ, (b) chuẩn bị kịch bản, (c) tìm entry ở vùng tốt hơn. Bias chỉ đổi khi external structure đổi, hoặc khi có bằng chứng ở khung cao hơn.

**Q2. Một internal bearish structure có thể tạo bearish dealing range trong bullish external structure không?**
**Trả lời: Có — và đây là trạng thái bình thường nhất trên chart.** Xảy ra ở mọi nhịp hồi sâu: trong khi external D1 vẫn bullish, nhịp hồi H1 có cấu trúc LH/LL riêng và một range H1 bearish riêng. Vấn đề **không** phải là "nó có tồn tại không" (có), mà là **nó có quyền chi phối không**.

| Điều kiện | Range H1 bearish đó là gì | Dùng thế nào |
|---|---|---|
| Nằm hoàn toàn trong external D1; neo D1 còn nguyên | **TEMPORARY INTERNAL RANGE** (§14.3) | Dùng để định thời điểm entry **theo hướng D1** (chờ nó kết thúc) — **không** dùng để short |
| Một neo D1 bị close-through | Chuyển thành **REPLACED** ở cấp H1, và bắt đầu thách thức D1 | Hạ bậc luận điểm D1; xét lại state; size giảm |
| Cả hai neo D1 bị lấy **và** D1 có MSS | **External reversal candidate** | Đây mới là lúc xét đảo bias (và vẫn cần HTF alignment) |

**Q3. Khi nào internal range nên được ưu tiên cho execution, khi nào nó chỉ là noise?**
Đây là câu hỏi vận hành quan trọng nhất của §16. Tiêu chí — **5 điều kiện, cần ≥3 để dùng range con làm khung execution**:

| # | Điều kiện | Đo được |
|---|---|---|
| 1 | Chiều cao range con ≥ `1.0 × ATR` của khung đó | (range quá nhỏ thì stop không đặt được) |
| 2 | Range con chứa ≥1 array chưa mitigate (FVG/OB) | `internal_poi = 1` |
| 3 | Có displacement trong range con | `disp ≥ 1` |
| 4 | Range con **hướng về** một pool chưa spent ở phía range lớn cho phép | `draw_aligned = true` |
| 5 | Range con nằm trong nửa range lớn mà hướng bias cho phép (Long → discount của range lớn) | `pd_htf` khớp hướng |

**Khi <3 điều kiện:** range con là noise → **không** dùng để entry; nếu bạn thấy mình đang dùng nó, gần như chắc chắn bạn đang tìm lý do để vào lệnh (confirmation-seeking), không phải đang phân tích.

### 16.3. Bảng tra nhanh: cái gì phá được cái gì

| Sự kiện | Phá internal range con? | Phá external range? | Đổi bias? |
|---|---|---|---|
| Internal BOS (thuận hướng range) | Có (đổi nội bộ) | Không | Không |
| Internal MSS (ngược hướng range) | Có | **Không** | **Không** |
| Wick qua neo | Không | **Không** | Không |
| Body-close qua neo + không reclaim | Có | **Có** | Chỉ khi neo đó thuộc cấp bias |
| Displacement qua neo + acceptance | Có | Có | Có (cấp đó), **kèm** xét HTF |
| Quét cả hai neo (S&D) | Không | **Không** (range được "sạc lại") | Không |

---

## 17. Liquidity Relationship — thanh khoản nằm ở đâu trong một range

### 17.1. Bản đồ thanh khoản của một dealing range

| Vị trí | Loại | Vai trò mặc định | Ghi chú vận hành |
|---|---|---|---|
| Trên `h` | **BSL ngoài range** (external) | Draw khi bias bullish; target cuối | Có thể gồm EQH, PDH/PWH, mức tròn |
| Dưới `l` | **SSL ngoài range** (external) | Draw khi bias bearish; target cuối | Như trên |
| Sát `h`/`l` (bên trong) | **Inducement** | Bẫy: pool nhỏ hơn, gần hơn, để dụ entry sớm | Xem §17.3 |
| Tại internal array (FVG/OB) | **IRL** | Nơi giá về rebalance; **không** phải target cuối | Xem [[16-Internal-External-Range-Liquidity-IRL-ERL]] |
| Quanh EQ | **Liquidity hai chiều, mỏng** | Vùng không có edge về vị trí | Rule: không giao dịch trong 40–60% |
| Trùng mức phiên (ARH/ARL, PDH/PDL) | **Pool session** | Thường là Judas target trong ngày | Xem [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] |
| Trùng mức tròn | **Pool tâm lý** | Có bằng chứng clustering **[B]** (Osler) | Chỉ là *một phần* của cụm, không phải toàn bộ |

### 17.2. Vì sao **vị trí của giá** thay đổi cách đọc thanh khoản — điểm cốt lõi của §17

> [!important] Cùng một pool, hai vai trò hoàn toàn khác nhau, tuỳ vị trí giá
> Đây là insight quan trọng nhất của §17. **Thanh khoản không có vai trò cố định — vai trò của nó là hàm của vị trí giá trong range.**
>
> | Giá đang ở | Pool ở `h` (phía trên) | Pool ở `l` (phía dưới) |
> |---|---|---|
> | **Discount sâu** (pd < 0.25) | **Draw hợp lệ** — đích đến của nhịp tăng | **Judas fuel** — nơi cần quét trước khi đi lên |
> | **Quanh EQ** (0.4–0.6) | Không rõ — hai phía tương đương | Không rõ |
> | **Premium sâu** (pd > 0.75) | **Judas fuel** — nơi quét trước khi giảm | **Draw hợp lệ** cho nhịp giảm |
>
> Nghĩa là: **bạn không thể nói "đây là draw" mà không nói giá đang ở đâu.** Cùng một đỉnh, khi giá ở discount nó là đích đến; khi giá đã ở premium và vừa test nó, nó là nhiên liệu. Đây là lý do câu hỏi "liquidity nằm ở đâu" **không thể** trả lời độc lập với `pd`.

![[DR-Deep-08-Pool-Vai-Tro-Theo-Vi-Tri.svg|740]]
*Hình 9 — Vai trò của một pool ĐẢO HOÀN TOÀN theo vị trí giá. Cùng một range, cùng những pool, nhưng draw ↔ fuel đổi chỗ. Vì vậy không thể nói "đây là draw" mà không nói giá đang ở đâu.*

### 17.3. Inducement — cơ chế và cách nhận diện

**Định nghĩa đơn giản:** một pool thanh khoản **nhỏ, gần, hiển nhiên** nằm giữa giá hiện tại và POI thật, được thiết kế (theo cách đọc ICT) để dụ trader vào lệnh sớm.

**Cơ chế trung thực [D]:** không cần giả định ai "thiết kế". Chỉ cần hai quan sát: (1) trader đặt stop/entry ở các mức hiển nhiên (Osler); (2) giá có xu hướng đi tới nơi có lệnh chờ. Kết hợp lại: **một mức hiển nhiên nằm giữa giá và một mức hiển nhiên lớn hơn sẽ bị test trước** — đơn giản vì nó ở gần hơn. Không cần ý định nào cả.

**Cách nhận diện vận hành:**
- Có một swing nhỏ/EQL/PDH nằm **giữa** giá và POI mục tiêu.
- Khoảng cách từ giá tới pool đó **nhỏ hơn** khoảng cách tới POI.
- Pool đó **chưa** bị quét.
→ Kết luận vận hành: **entry đặt trước pool này có xác suất bị quét cao hơn entry sau nó** (giả thuyết, cần backtest — xem H7).

### 17.4. Bảng vai trò: khi nào một pool là draw, khi nào là fuel, khi nào là target cuối

| Pool | Là draw khi | Là fuel khi | Là target cuối (T2) khi |
|---|---|---|---|
| BSL trên `h` | Bias bullish + giá ở discount | Giá ở premium + bias bearish | Bias bullish mạnh + không còn pool nào xa hơn |
| SSL dưới `l` | Bias bearish + giá ở premium | Giá ở discount + bias bullish | Bias bearish mạnh + không còn pool xa hơn |
| EQL nội bộ | Hiếm — dùng như T1 | Thường xuyên | Không |
| EQH nội bộ | Hiếm — dùng như T1 | Thường xuyên | Không |
| Mức phiên (PDH/PDL) | Có, trong ngày | Có, khi ngược hướng bias | Không — mức phiên là intraday |
| Pool liên khung (PWH ≈ PDH) | Có, mạnh nhất | Ít hơn | Có — thường là T2 hợp lý |

---

## 18. Dealing Range ↔ DOL — phân tích vòng lặp logic

### 18.1. Phát biểu vấn đề một cách hình thức

Chuỗi lập luận thông thường:

```text
(1) Range quan trọng vì hai đầu của nó là hai pool thanh khoản lớn.
(2) DOL là pool thanh khoản lớn nhất theo hướng bias.
(3) Vậy DOL = một trong hai đầu của range.
```

Nhìn kỹ: (1) và (2) đều dùng khái niệm "pool thanh khoản lớn", và (3) là **hệ quả tất yếu** của cách chọn range. Nghĩa là:

> **Nếu bạn chọn range bằng tiêu chí "hai đầu có liquidity", thì việc DOL trùng một đầu range không mang thêm thông tin nào.** Đó là tautology — một phát biểu đúng theo định nghĩa, không phải một dự báo.

Đây chính xác là vòng lặp logic mà đề bài yêu cầu phát hiện. **Nó có thật**, và nó nguy hiểm vì nó tạo **cảm giác xác nhận**: range và DOL "khớp nhau" trông như hai bằng chứng độc lập, nhưng thực ra là một.

### 18.2. Vậy cái nào xác định cái nào? — ba quan hệ, không phải một

| Quan hệ | Có thật? | Vai trò đúng |
|---|---|---|
| **DR → DOL** | Có, **nhưng chỉ theo nghĩa lọc**: range giới hạn *tập* pool nào là "trong tầm" (external vs internal) | DR cung cấp **tập ứng viên**, không chọn ứng viên |
| **DOL → DR** | Có, **nhưng chỉ theo nghĩa chức năng**: nếu không có range nào chứa pool mà mọi bằng chứng độc lập chỉ về nó, thì range của bạn đang sai | DOL cung cấp **bài kiểm tra tính hợp lý (sanity check)**, không phải tiêu chí chọn (§13.1-Q11) |
| **DR ↔ DOL** | **Vòng lặp**, nếu cả hai đều được suy từ nhau | Phải bị chặn bằng **thời điểm + bằng chứng độc lập** |

### 18.3. Cách chặn vòng lặp — quy trình 4 bước có timestamp

```text
t₀  CHỐT RANGE      Dùng CHỈ các tiêu chí độc lập với DOL:
                    gate cấu trúc (G2) + displacement (D) + liquidity trạng thái (L) 
                    → ghi (h, l, τ, t₀, lý do)
                    ⛔ CẤM dùng "range này hướng về DOL của tôi" ở bước này.

t₁  GHI DOL         Dùng bằng chứng ĐỘC LẬP với range, theo thứ tự:
                    (a) Bên nào vừa bị tiêu thụ? (con lắc — quan trọng nhất)
                    (b) Cấu trúc: BOS/MSS gần nhất theo hướng nào?
                    (c) Tính liên khung: pool nào được nhiều khung cùng tham chiếu?
                    (d) Khoảng cách còn lại có khả thi trong phiên không?
                    → ghi pool + giá cụ thể

t₂  ĐỐI CHIẾU       Nếu DOL (t₁) trùng biên range (t₀) → OK, nhưng ghi rõ
                    "trùng là hệ quả của (a)-(d), không phải của việc chọn range".
                    Nếu DOL (t₁) KHÔNG trùng biên range → ĐÂY LÀ THÔNG TIN QUAN TRỌNG NHẤT:
                    nghĩa là range bạn chốt không chứa draw thật → xét lại range (t₀).

t₃  KIỂM TRA        Không được sửa t₀ sau khi biết t₁ để làm cho chúng khớp nhau.
                    Nếu buộc phải sửa → ghi lại như một lần REPLACED hợp lệ, có log.
```

> [!danger] Dấu hiệu bạn đã rơi vào vòng lặp (tự kiểm tra)
> - Bạn không thể nêu lý do chọn range mà **không** nhắc tới DOL.
> - Mỗi lần DOL đổi, range của bạn cũng đổi theo — và luôn đổi *sau*.
> - Range của bạn luôn có đúng một đầu trùng DOL, chưa bao giờ hai đầu đều không trùng.
> - Bạn không nhớ range được chốt lúc nào.
>
> Bốn dấu hiệu này gần như chắc chắn có nghĩa: bạn đang **vẽ range từ kết luận**, không phải **suy kết luận từ range**. Cách chữa duy nhất là timestamp (§31-A8).

![[DR-Deep-09-Vong-Lap-DOL.svg|760]]
*Hình 10 — Vòng lặp logic Range ↔ DOL (trái) và cách chặn bằng bốn bước có timestamp (phải). Điểm mấu chốt: nếu DOL không trùng biên range, đó là thông tin — không phải lỗi cần sửa.*

### 18.4. Nếu giá ở discount nhưng DOL lại nằm ở sell-side (phía dưới) — xử lý thế nào?

Đây là câu hỏi vận hành quan trọng nhất của §18 và nó **không có một câu trả lời duy nhất** — có bốn khả năng, và phải phân biệt bằng bằng chứng bổ sung:

| Khả năng | Bằng chứng phân biệt | Xử lý |
|---|---|---|
| **(A) Draw đó là Judas fuel, không phải DOL** | HTF còn bullish; protected HTF low còn nguyên; giá vào discount **trong** một leg tăng | **Không short.** Coi SSL dưới là fuel; chờ sweep + MSS bullish → Long theo HTF (§53 bảng phân vai) |
| **(B) Range đã cũ, "discount" là thông tin chết** | Range đã bị consumption một đầu; neo cũ không còn được tham chiếu; có range mới đã hình thành | **Chốt range mới** (§14.3-REPLACEMENT). `pd` cũ bỏ |
| **(C) Đảo chiều thật đang diễn ra** | HTF đã có MSS/CHoCH; protected HTF swing đã bị phá bằng body-close; giá ở discount **nhưng** range đang bị repricing xuống (LL mới) | **Đổi khung đọc**: discount của range cũ không còn nghĩa bullish. Chờ range mới, tìm short ở premium **của range mới** |
| **(D) Mâu thuẫn chưa giải quyết** | Không đủ bằng chứng cho (A)/(B)/(C) | **No-trade** hoặc nửa size, T1 only. Ghi `dol_conflict = true` (§13.2 bước 5) |

> [!important] Điểm mấu chốt về mặt logic
> "Discount + DOL phía dưới" **không** phải mâu thuẫn — nó là **thông tin rằng range này đang được dùng sai mục đích**. Discount chỉ có nghĩa bullish khi **hướng của range** là tăng. Nếu hướng range đang chuyển sang giảm (LL mới hình thành), thì "discount" chỉ là mô tả vị trí trong một cái hộp đã lỗi thời. Xem §19.3.

### 18.5. Nhiều DOL cùng lúc — có hợp lệ không? Có, và cần phân tầng

| Câu hỏi | Trả lời |
|---|---|
| Có thể có nhiều DOL không? | **Có.** Mỗi timeframe có DOL riêng; và trong một timeframe có thể có T1 (gần) + T2 (xa) |
| Chọn thế nào khi có nhiều pool external? | Thứ tự: (1) pool **chưa spent** theo hướng bias; (2) pool có `tf_stack` cao nhất; (3) pool gần nhất **còn khả thi trong tầm phiên**; (4) pool có array dẫn tới nó |
| DOL có thay đổi intraday không? | **Có** — khi (a) DOL bị tiêu thụ, (b) cấu trúc flip, (c) DOL trở nên bất khả thi về thời gian. Nhưng **không** đổi chỉ vì giá đi ngược tạm thời |
| DOL có hierarchy theo timeframe không? | **Có**: W1 DOL > D1 DOL > H1 DOL > session DOL. Nguyên tắc: DOL khung nhỏ bị **giới hạn** bởi DOL khung lớn — nếu D1 DOL ở trên, một H1 DOL ở dưới chỉ nên được dùng như **Judas target**, không phải target cuối |

**Rule vận hành DOL (viết gọn để dùng ngay):**
> **DOL = pool chưa spent, gần nhất, theo hướng được phép bởi range HTF, có ≥1 bằng chứng độc lập với range, và khả thi trong tầm phiên.** Không viết được thành một câu kèm giá cụ thể → **chưa có DOL → no-trade.**

---

## 19. Premium / Discount — khung vị trí, không phải tín hiệu hướng

### 19.1. Định nghĩa và vì sao nó KHÔNG phải tín hiệu

`pd(p) = (p − l)/(h − l)`. Premium = `pd > 0.5`, discount = `pd < 0.5`, EQ = `0.5`, quadrant = 0.25/0.75.

**Lập luận vì sao premium/discount không thể là tín hiệu hướng độc lập — chỉ bằng logic:**

1. `pd` là một **hàm của vị trí giá**, không phải hàm của cung cầu. Nó không chứa thông tin về việc bên nào đang kiểm soát.
2. Trong một xu hướng tăng, giá dành **phần lớn thời gian ở premium** của các range con (vì nó liên tục phá đỉnh). Nếu "premium = bán", hệ thống sẽ short suốt một xu hướng tăng.
3. Do đó, nếu `pd` có bất kỳ giá trị dự báo nào, giá trị đó **phải có điều kiện** — và điều kiện phải đến từ biến khác (hướng range, DOL, cấu trúc). Một mình `pd` không đủ.

**Hệ quả:** câu đúng không phải *"discount → mua"* mà là *"discount **trong một range có hướng tăng, với DOL ở phía trên, và có array tại đó** → mua"*. Ba điều kiện, không phải một.

### 19.2. Khi nào discount **không** có ý nghĩa bullish — 6 trường hợp

| # | Trường hợp | Vì sao discount mất nghĩa | Cách nhận ra |
|---|---|---|---|
| 1 | **Hướng range là giảm** (LH/LL đang hình thành) | "Discount" của một cái hộp đang hạ thấp không phải là rẻ | Range có LL mới; neo dưới vừa bị close-through |
| 2 | **Discount nông** (0.25–0.5) không có array | Vị trí không kèm nơi có lệnh → không có lý do dừng | Không có FVG/OB chưa mitigate ở nửa dưới |
| 3 | **Không có pool chưa spent phía trên trong tầm** | Không có draw → không có lý do đi lên | Tất cả BSL trong tầm phiên đã bị quét |
| 4 | **Range quá rộng so với ADR** | `%` mất độ phân giải; cách đáy còn hàng trăm point "đất trống" | `range_height > 1.5 × ADR` (practice) |
| 5 | **Xung đột khung**: discount của range nhỏ nhưng premium của range lớn | Đây là bẫy phổ biến nhất | `pd_ltf < 0.5` ∧ `pd_htf > 0.5` |
| 6 | **Hết thời gian để deliver** | Vị trí đúng nhưng không còn phiên để đi | Cuối phiên, sát đóng cửa, hoặc sắp có tin lớn |

### 19.3. Khi nào premium **không** có ý nghĩa bearish

Đối xứng, nhưng **không hoàn toàn đối xứng** — có một bất đối xứng quan trọng cần nêu:

| # | Trường hợp | Ghi chú |
|---|---|---|
| 1 | Range có hướng tăng (HH/HL) | Premium của xu hướng tăng là nơi **breakout tiếp diễn**, không phải nơi đảo chiều |
| 2 | Premium không có array bearish | Không có POI → không có điểm vào |
| 3 | **Displacement tăng vừa xảy ra và chưa được mitigate** | Đây là **bất đối xứng quan trọng**: một cú displacement tăng mạnh thường kéo giá ở lại premium lâu hơn trực giác; short vào premium ngay sau displacement là short vào dòng lệnh đang mạnh |
| 4 | Không có SSL chưa spent trong tầm | Không có draw xuống |
| 5 | Xung đột khung (premium LTF, discount HTF) | Bẫy đối xứng |
| 6 | Cuối phiên / sắp tin | Như trên |

> [!important] Bất đối xứng cần nhớ (và cần kiểm định)
> **[E]** Trực giác phổ biến là premium và discount đối xứng. Nhưng có ít nhất hai lý do để nghi ngờ: (a) các thị trường có **drift dài hạn** (index) nên premium bị "ở lại" lâu hơn; (b) sau displacement, giá thường **không** quay lại ngay. Đây là giả thuyết kiểm định được: so expectancy của setup short-tại-premium với long-tại-discount trong cùng regime. Nếu bất đối xứng tồn tại, nó phải được **đo**, không được **giả định**.

### 19.4. Hai lỗi đo lường đã quan sát thật trong vault

Hai lỗi này đã được ghi nhận trong nhật ký/backtest của chính vault — nêu ra vì chúng là **lỗi hệ thống**, không phải lỗi lẻ:

1. **Nhầm "50% của GAP" với "50% của dealing range"** — hai khái niệm 50% khác nhau (midpoint của một imbalance vs midpoint của một range) bị dùng lẫn trong một lệnh, khiến tiêu chí "giá ở premium/discount" không kiểm được. **Rule chữa:** mọi mức 50% phải ghi rõ `50%_of = {gap | DR-1 | DR-4}`.
2. **Đo OTE trên toàn dealing range thay vì trên impulse leg** (§3.1) — hai đại lượng có thể trùng số nhưng không cùng khái niệm. **Rule chữa:** `anchor_type` bắt buộc (§3.1).

### 19.5. Vai trò của các biến khác — bảng tương tác

`pd` không hoạt động một mình. Bảng dưới là cách nó tương tác với 4 biến còn lại:

| Biến | `pd` discount có nghĩa bullish khi... | `pd` premium có nghĩa bearish khi... |
|---|---|---|
| **Hướng range (structure)** | HH/HL còn hiệu lực | LH/LL còn hiệu lực |
| **DOL** | Pool chưa spent phía trên, trong tầm | Pool chưa spent phía dưới, trong tầm |
| **Liquidity** | Có array chưa mitigate phía dưới hoặc tại giá | Có array chưa mitigate phía trên hoặc tại giá |
| **HTF structure** | HTF bullish (hoặc trung tính) | HTF bearish (hoặc trung tính) |
| **Thời gian** | Còn killzone trong phiên | Còn killzone trong phiên |

**Thiếu 2 trong 5 → không giao dịch.** Đây là rule vận hành — **practice rule**, không phải kết quả nghiên cứu.

### 19.6. Bằng chứng về OTE và các tỷ lệ Fibonacci — một kết quả PHỦ ĐỊNH ở mức peer-reviewed

Phần này **không** nằm trong đề bài, nhưng phải có, vì OTE (62–79%) là một **tỷ lệ Fibonacci** và nó là một phần trong framework của bạn. Im lặng về điều này sẽ là thiên vị bằng chứng.

> [!danger] Kết quả kiểm định trực tiếp nhất về Fibonacci — và nó phủ định
> **Tsinaslanidis, Guijarro & Voukelatos (2022), "Automatic identification and evaluation of Fibonacci retracements: Empirical evidence from three equity markets", *Expert Systems with Applications* 187:115893** ([DOI](https://doi.org/10.1016/j.eswa.2021.115893), [bản PDF tác giả](https://riunet.upv.es/handle/10251/195083)) — đã đọc **toàn văn**, đây là bài **bình duyệt**.
>
> **Kết luận nguyên văn:** *"Our empirical results provide **no support** for the use of Fibonacci levels in technical analysis… prices are **equally likely to bounce on Fibonacci levels as they are to bounce on non-Fibonacci levels**. Importantly, a trading rule based on Fibonacci levels **fails to outperform** a strategy based on randomly selected non-Fibonacci levels."*
>
> **Giới hạn của bài (phải nêu để công bằng):** chỉ **3 thị trường cổ phiếu**; mức test là 23.6/38.2/61.8/100% (**không có 50%**, và cũng **không test 0.705 hay 0.79** — hai mức mà OTE dùng); phương pháp "zone" là do chính tác giả đề xuất. Nghĩa là: bài này **không** trực tiếp bác bỏ OTE, nhưng nó bác bỏ **cơ chế nền** mà OTE dựa vào (rằng giá "tôn trọng" các tỷ lệ này hơn các mức khác).

**Và có một kết quả ngược lại — nhưng ở dạng chưa bình duyệt:** Shanaev & Gibson (2022), *"Can Returns Breed Like Rabbits? Econometric Tests for Fibonacci Retracements"*, SSRN 4212430 ([DOI](https://doi.org/10.2139/ssrn.4212430)) cho rằng Fibonacci **có** ý nghĩa trên index quốc tế và FX, với các mức quan trọng nhất là 0.0 / 38.1 / **50.0** / 61.2 / 100%, và chiến lược trên S&P 500 sinh alpha có ý nghĩa. **Đây là preprint, KHÔNG bình duyệt** (Crossref type: `posted-content`), và nó **mâu thuẫn trực tiếp** với bài peer-reviewed ở trên.

> [!important] Trạng thái bằng chứng về OTE — nói thẳng
> | Mệnh đề | Trạng thái bằng chứng |
> |---|---|
> | OTE là một **quy ước ICT** (62–79% của leg) | **[C]** — có thật trong tài liệu, không cần bằng chứng |
> | OTE giúp **chuẩn hoá vị trí entry** để so sánh giữa các lệnh | **[D]** — đúng theo thiết kế, không cần bằng chứng |
> | Các **tỷ lệ Fibonacci** (0.618, 0.786) có sức mạnh đặc biệt so với mức khác | **Bị phủ định** bởi test peer-reviewed duy nhất trực tiếp (Tsinaslanidis et al. 2022), trên 3 thị trường cổ phiếu |
> | OTE **cải thiện expectancy** trên NQ/EURUSD/Gold khung H1/M5 | **Chưa ai kiểm định.** Không có bằng chứng ủng hộ, cũng không có bằng chứng bác bỏ |
>
> **Kết luận vận hành, không phải kết luận cảm tính:** tiếp tục dùng OTE như một **vùng vào lệnh có cấu trúc** (điều này hợp lý vì nó neo vào leg và cho bạn một quy tắc nhất quán), nhưng **đừng coi nó là một lý do độc lập** để tin vào lệnh — và **đừng** dùng nó để biện minh cho một entry mà các yếu tố khác (array, sweep, DOL, vị trí, thời gian) không ủng hộ. Cách kiểm tra: thêm biến `entry_in_ote ∈ {0,1}` vào log và so expectancy — đó là **giả thuyết H9** bổ sung cho §32.



---

## 20. Multi-Timeframe Application — D1 context, H1 setup, M5 execution

### 20.1. Phân vai (khớp với workflow của bạn)

| Khung | Vai trò | Range ở khung này trả lời | **Không** được dùng để |
|---|---|---|---|
| **D1** | Macro context | Hướng được phép; `pd` vĩ mô; DOL cấp lớn; state tổng thể | Chọn điểm vào; đặt stop |
| **H1** | Setup / structural refinement | Vùng POI; nhịp hồi đã đủ sâu chưa; internal structure | Đo bias; phủ quyết D1 |
| **M5** | Execution | Điểm vào chính xác; stop; xác nhận sweep/MSS/FVG | Kết luận premium/discount; kết luận hướng |

### 20.2. Khi nào M5 cần range riêng, khi nào không

**CẦN range M5 khi:**
- Leg M5 chính là leg delivery (giá đang trong cú di chuyển tới POI) → cần đo retracement của **chính leg đó** (đây là DR-4, không phải DR-1 — xem §3.1).
- Cần đặt stop theo cấu trúc M5 (stop phải nằm sau một swing M5 có nghĩa).
- HTF đang ở giữa range (không phân giải) → M5 cung cấp độ phân giải duy nhất có được.

**KHÔNG cần range M5 khi:**
- HTF đã cho một array cụ thể + một mức invalidation rõ → range M5 chỉ thêm nhiễu và thêm cơ hội tự thuyết phục.
- Giá đang ở vùng EQ của range H1 (40–60%) → rule cấm giao dịch đã chặn trước khi tới bước này.
- M5 range sẽ có chiều cao `< 1 × ATR(M5)` → quá nhỏ để đặt stop có nghĩa.

### 20.3. Có nên dùng **cùng một** range cho mọi khung?

**Không.** Ba lý do, theo thứ tự quan trọng:
1. **Tham số phát hiện swing phải khác nhau** giữa các khung (§10.1-T) — dùng cùng tham số tạo ra "MSS giả" trên M5.
2. **Chức năng khác nhau** — đo bias khác với đặt stop. Một range không thể tối ưu cho cả hai.
3. **Nhưng** chúng phải **nhất quán về phân cấp**: range M5 phải nằm trong range H1, range H1 nằm trong range D1 (hoặc có lý do rõ ràng nếu không).

### 20.4. Ma trận alignment — trả lời hai câu hỏi khó nhất của §16

**Trường hợp 1: D1 premium, H1 discount.**

```text
D1:  ────────────────────────────────  premium  (pd_D1 > 0.5)
         ▲ giá đang ở đây
H1:  ────────────────────────────────  discount  (pd_H1 < 0.5)
```

**Đây không phải mâu thuẫn — đây là một nhịp hồi đang diễn ra.** Cách đọc:
- D1 nói: giá đắt ở cấp lớn → **không mua mới ở cấp lớn**, chỉ tìm Short hoặc chờ hồi sâu hơn.
- H1 nói: trong nhịp gần nhất, giá đang rẻ → có thể có một cú bật H1 **theo hướng nào là tuỳ D1**.
- **Kết luận vận hành:** nếu D1 bearish → tìm Short tại **premium của H1** (chờ H1 hết discount). Nếu D1 bullish → đây là hồi sâu trong xu hướng tăng; chờ giá về **discount của D1** và array D1 (không long ở đây chỉ vì H1 đang discount).

**Trường hợp 2: D1 bullish discount, H1 bearish premium** — cấu hình bẫy kinh điển.

```text
D1:  ────────────────────────────────  discount  (pd_D1 < 0.5)  → cho phép Long
H1:  ────────────────────────────────  premium   (pd_H1 > 0.5)  → cấu trúc H1 bearish
```

**Đây là cấu hình mà đa số lệnh thua "đúng phương pháp" xảy ra.** Cách đọc đúng:
- D1 cho phép **hướng Long** (điều kiện cần, chưa đủ).
- H1 đang ở premium **và** cấu trúc H1 bearish → nhịp hồi H1 đã đi lên hết và có thể đang hình thành đỉnh H1 mới.
- **Hai khả năng, và không thể phân biệt bằng range — phải dùng cấu trúc:**
  - **(i)** H1 bearish chỉ là pullback nội bộ trong D1 bullish → giá sẽ hồi xuống hết nhịp H1 này rồi tiếp tục lên. **Hành động:** chờ, không mua ở premium H1; chờ H1 tạo đáy mới + MSS bullish rồi mua ở discount H1 **mới**.
  - **(ii)** H1 bearish là khởi đầu của đảo chiều D1 → nhưng điều này chỉ được xác nhận khi **protected low D1 bị phá bằng body-close**. **Hành động:** chờ sự kiện đó; nếu chưa có, mặc định là (i).
- **Rule vận hành mạnh nhất của §20:** *D1 discount + H1 premium + H1 bearish = **không mua ở đây**.* Không phải vì D1 sai, mà vì **thời điểm** sai. Đây chính là nội dung "HTF range quyết định HƯỚNG, LTF range quyết định THỜI ĐIỂM".

![[DR-Deep-10-MTF-Alignment.svg|760]]
*Hình 11 — Hai cấu hình alignment khó nhất. Case 1 (D1 premium + H1 discount) là nhịp hồi bình thường; Case 2 (D1 discount + H1 premium + H1 bearish) là cấu hình bẫy — nơi đa số lệnh thua "đúng phương pháp" xảy ra.*

### 20.5. Quy tắc cascade khi re-map (§37)

Khi range HTF bị REPLACED/INVALIDATED (§14.4):
1. Chốt range mới ở HTF, ghi `t₀`.
2. **Xoá** (không phải "cập nhật") mọi range con — chúng được xây trên bản đồ cũ.
3. Xây lại range con **từ** range HTF mới, chỉ giữ lại những POI nằm đúng nửa mới của range mới.
4. Ghi log việc cascade này — vì đây là thời điểm dễ xảy ra lỗi "bám víu POI cũ đã mất context".

---

## 21. Critical Scenario — D1 bullish nhưng giá hồi sâu, phá protected HL, có bearish displacement

### 21.0. Phát biểu kịch bản và một cảnh báo phương pháp luận

**Kịch bản:** D1 bullish với chuỗi HH → HL → HH → HL. Hiện tại giá đang hồi sâu. Trong quá trình hồi: giá **phá xuống một Intermediate / Protected HL**, xuất hiện **bearish displacement**, có thể có **bearish MSS**, **short-term delivery đã chuyển bearish**, nhưng **major D1 structure vẫn bullish**.

> [!warning] Cảnh báo quan trọng nhất của §21 — đọc trước khi đọc 12 câu trả lời
> **Kịch bản này, tại thời điểm nó đang xảy ra, KHÔNG THỂ được phân giải thành A/B/C bằng chart.** Không có tập dữ liệu nào, không có chỉ báo nào, không có cách đọc cấu trúc nào cho phép bạn biết chắc ở thời điểm phá protected HL rằng đây là "hồi sâu" hay "đảo chiều". Bất kỳ ai nói ngược lại đang bán cho bạn sự chắc chắn giả.
>
> **Cái bạn CÓ THỂ làm — và đó là toàn bộ giá trị của §21:**
> 1. **Phân biệt ba trạng thái bằng các biến quan sát được** (không phải bằng cảm nhận).
> 2. **Gán xác suất tương đối** dựa trên các biến đó (thứ tự ưu tiên, không phải con số chính xác).
> 3. **Định cỡ vị thế theo mức độ chưa chắc chắn** — đây là nơi duy nhất mà việc "không biết" được xử lý đúng cách.
> 4. **Viết trước các điều kiện sẽ chuyển kịch bản** (từ A sang B, từ B sang C) — đây là thứ biến một tình huống mơ hồ thành một kế hoạch.

### 21.1. Phân biệt ba trạng thái — bảng biến phân biệt

| Biến phân biệt | **A. Deep pullback** (hồi sâu trong trend tăng) | **B. Intermediate bearish trend** (xu hướng giảm trung gian, có thể là chân của đảo chiều) | **C. Genuine HTF reversal** (đảo chiều thật) |
|---|---|---|---|
| **Cấp bị phá** | Internal/intermediate (H1). **Neo D1 nguyên vẹn** | Protected **intermediate** HTF bị phá, neo D1 vẫn nguyên | **Neo D1 bị phá** (protected D1 low) |
| **Cách phá** | Wick hoặc body-close nhỏ; **có reclaim nhanh** | Body-close + **giữ ngoài** vài nến; pullback về mức cũ bị từ chối | Body-close + displacement + **acceptance nhiều phiên** |
| **Nơi xảy ra trong range D1** | Ở **deep discount** (0–25%) hoặc tại array D1 | Giữa range (25–50%) | Từ **premium** (đã phân phối ở trên) rồi phá xuống |
| **External liquidity D1 đã bị lấy chưa?** | BSL phía trên **còn nguyên** (chưa lấy) → còn lý do đi lên | BSL đã bị lấy **và** giá đã CISD xuống | Cả hai đầu đã bị lấy; range D1 đã `INVALIDATED` |
| **Cấu trúc D1** | HH/HL còn hiệu lực; **không có D1 MSS** | D1 chưa MSS nhưng **LH mới hình thành** | **D1 MSS/CHoCH đã xác nhận** |
| **Thời gian** | 2–5 phiên, trong biên độ bình thường | 1–3 tuần; vượt ADR nhiều phiên liên tiếp | Nhiều tuần; thay đổi character rõ |
| **Đặc điểm delivery** | Downside delivery là **đi tới array**, tức có mục tiêu cụ thể | Delivery xuống có **cấu trúc LH/LL riêng**, mục tiêu là pool dưới | Delivery xuống **không dừng ở array**, phá luôn array |
| **Xác suất tiên nghiệm (ước lượng)** | **Cao nhất** — đây là trạng thái phổ biến nhất trong trend | Trung bình | **Thấp** — nhưng hậu quả lớn nhất |

> [!important] Vì sao A có xác suất tiên nghiệm cao nhất — và vì sao điều đó KHÔNG có nghĩa "cứ mua"
> Vì trong một xu hướng tăng, số nhịp hồi **nhiều hơn** số lần đảo chiều (định nghĩa của xu hướng). Đây là lập luận **cấu trúc**, không phải thống kê — và nó có một cái bẫy: nếu bạn dùng nó để **luôn mặc định A**, bạn sẽ mất toàn bộ vốn ở lần chuyển sang C, vì C đến **một lần** và xoá sạch nhiều lần thắng nhỏ. Đây là dạng phân phối **thắng nhỏ - thua lớn**, và cách duy nhất để sống sót là **điều kiện invalidation cứng + size theo biến**, không phải "mặc định A rồi gồng".

### 21.2. Trả lời 12 câu hỏi của kịch bản

**Q1. Dealing Range bullish ban đầu còn valid không?**
**Phụ thuộc vào cấp bị phá** — và đây là chỗ phải tách hai khái niệm thường bị gộp:

| Cái gì bị phá | Range D1 ban đầu | Bias D1 |
|---|---|---|
| Internal/intermediate swing (H1) | **Còn VALID** — neo D1 chưa chạm | Còn bullish |
| One anchor D1 bị **wick** qua | **Còn VALID**; `unswept_count` giảm | Còn bullish |
| One anchor D1 bị **close-through** | **REPLACED** — cần neo mới | **Chưa** đổi (cần thêm bằng chứng) |
| Protected D1 low bị phá + acceptance | **INVALIDATED** | **Đang chuyển** — cần MSS D1 để xác nhận |

> [!success] Đây là câu trả lời quan trọng nhất trong toàn bộ §21
> **Range validity và directional thesis là hai biến KHÁC NHAU.** Bạn có thể có: range VALID + thesis đang nghi ngờ; hoặc range REPLACED + thesis vẫn bullish. Gộp hai biến này là nguồn của phản xạ "range đổi → bias đổi", và phản xạ đó khiến bạn đảo bias ở đúng những điểm mà bạn nên chờ.

**Q2. Hay phải redefine dealing range?**
Phân biệt bằng ba trạng thái (§14.3):
- **REFINEMENT** nếu chỉ có wick giãn biên → **không** re-define, chỉ đo lại levels (§12-Dealing-Range W4).
- **REPLACEMENT** nếu một neo bị close-through → có range mới, cascade xuống H1/M5.
- **INVALIDATION** nếu protected D1 low bị phá bằng body-close → không "re-define" mà **chờ** range mới hình thành (có thể mất 1–3 phiên).
- **Trong lúc chưa rõ:** `SUSPENDED`. Và `SUSPENDED` **không phải** lý do để re-map — nó là lý do để **không giao dịch**.

**Q3. Việc phá protected HL có ý nghĩa ở timeframe nào?**
Chính xác bằng **cấp của swing đó** (§11.2), không hơn không kém. Ba khả năng:
- Nếu là protected **H1**: hệ quả ở H1 (nhịp H1 đổi), D1 không đổi. → Đây là A hoặc B, chưa thể là C.
- Nếu là protected **D1 nhưng không phải neo range lớn**: hệ quả ở D1 state, chưa chắc ở bias.
- Nếu là **neo của range D1 đang chi phối**: hệ quả ở cấp D1 → ứng viên C.
> **Câu hỏi tự kiểm tra duy nhất cần đặt:** *"Chuỗi kết luận nào mất hiệu lực?"* — trả lời được thì biết cấp, không trả lời được thì bạn đang phản ứng với một mức giá chứ không phải với cấu trúc.

**Q4. Đây là internal reversal / intermediate reversal / external reversal / trend reversal / liquidity event / repricing event?**
Đây là câu hỏi hay nhất trong 12 câu, vì nó hỏi **bản chất** chứ không hỏi nhãn. Trả lời bằng cách tách thành hai trục **độc lập**:

```text
TRỤC 1 — CẤP (tự động, từ cấp bị phá):     internal < intermediate < external
TRỤC 2 — BẢN CHẤT (từ cách phá + phản ứng sau):
   liquidity event   = phá rồi reclaim nhanh, thanh khoản bị tiêu thụ, KHÔNG có acceptance
   repricing event   = phá rồi giữ ngoài, giá trị được thiết lập lại ở phía mới
```

Sáu nhãn trong câu hỏi của bạn thực ra là **tổ hợp của hai trục này**:

| Nhãn | Cấp | Bản chất | Hệ quả |
|---|---|---|---|
| Internal reversal | internal | thường là liquidity event | Chỉ là pullback; không đổi bias |
| Intermediate reversal | intermediate | liquidity hoặc repricing | Đổi cấu trúc trung gian, **chưa** đổi bias HTF |
| External reversal | external | repricing | Ứng viên đổi bias — cần HTF alignment |
| Trend reversal | external (HTF) | repricing + structure | Đổi bias |
| Liquidity event | bất kỳ | **liquidity** | Range giữ nguyên, thậm chí tăng confidence |
| Repricing event | bất kỳ | **repricing** | Range phải re-map |

> **Điểm mấu chốt:** *liquidity event* và *repricing event* là cùng một hiện tượng quan sát thô (giá vượt một mức) nhưng khác nhau ở **có acceptance hay không**. Đây chính là §15.5 (raid vs structural break), áp vào kịch bản này.

**Q5. Làm sao phân biệt A (deep pullback) / B (intermediate bearish trend) / C (reversal thật)?**
Bằng **thứ tự bằng chứng (evidence ladder)** — không phải bằng một chỉ báo:

```text
BẬC 1  Cấp bị phá: internal hay neo D1?                        → A nếu internal
BẬC 2  Cách phá: wick / body / displacement+acceptance?        → A nếu wick, B nếu body, C-ứng viên nếu acceptance
BẬC 3  Vị trí trong range D1 khi phá: discount hay premium?     → A nếu discount, C-ứng viên nếu từ premium
BẬC 4  BSL phía trên D1 đã bị lấy chưa?                        → A nếu CHƯA (còn draw lên); C-ứng viên nếu đã lấy rồi mới quay đầu
BẬC 5  Có D1 MSS/CHoCH xác nhận chưa?                          → C chỉ khi CÓ
BẬC 6  Thời gian: số phiên chấp nhận giá mới                    → C cần ≥ vài phiên
BẬC 7  HTF alignment: W1 nói gì?                               → nếu W1 ngược, C khó hơn nhiều
```

**Quy tắc đọc:** A và B khác nhau chủ yếu ở **bậc 2 và 3**; B và C khác nhau ở **bậc 4, 5, 7**. Bạn **không** cần phân giải tất cả — bạn cần biết **mình đang ở bậc nào**, và ở mỗi bậc thì size/rule tương ứng là gì (xem §21.3).

**Q6. Nếu D1 bullish nhưng H1 bearish, D1 dealing range nên được giữ hay thay đổi?**
**Giữ** — trừ khi một neo D1 bị tiêu thụ (§21.2-Q1). Lý do: hướng cấu trúc của H1 là **thuộc tính của một nhịp**, không phải của range D1. Range D1 được định nghĩa bởi hai neo D1; cấu trúc H1 không nằm trong định nghĩa đó. **Nếu bạn thay range D1 mỗi khi H1 đổi hướng, bạn không còn range D1 — bạn có một range H1 được dán nhãn sai.**

**Q7. H1 dealing range lúc này nên được xây dựng như thế nào?**
Neo H1 **phải được xây lại từ cấu trúc H1 đang thực sự tồn tại** — kể cả khi nó bearish và ngược D1:
- Neo = swing high và swing low H1 có ý nghĩa **của nhịp hồi hiện tại** (đỉnh hồi + đáy mới nhất đã xác nhận).
- Gán nhãn rõ: `htf_alignment = nghịch` → range này là **TEMPORARY INTERNAL RANGE** (§14.3) cho tới khi có điều kiện REPLACEMENT.
- **Mục đích duy nhất của nó:** xác định (a) nhịp hồi đã đi tới đâu trong đơn vị H1, (b) vùng premium H1 để **không mua**, (c) điểm mà nhịp hồi kết thúc (MSS bullish H1 + displacement) để bắt đầu tìm Long.
- **Cấm:** dùng nó để suy bias, để đổi bias, hoặc để tuyên bố "D1 đã đảo chiều".

**Q8. M5 bearish setup có thể hợp lệ không?**
**Có, có điều kiện** — và đây là một trong những chỗ mà tôi **không** đồng ý với cách nói tuyệt đối hóa "không bao giờ trade ngược HTF".

| Quan điểm | Lập luận | Điều kiện |
|---|---|---|
| **Không nên** (bảo thủ) | Bạn đang short vào vùng HTF discount — tức short đúng chỗ HTF muốn mua. R:R tệ: target gần (đáy range), stop xa. Và bạn đang cạnh tranh với dòng lệnh mua HTF | Nếu `pd_D1 < 0.35` → **không short** |
| **Có thể, nhưng là scalp** (trung dung) | Nếu nhịp hồi H1 còn chưa tới array D1, thì còn không gian để một M5 bearish setup đi theo hướng H1. Đây là trade **theo H1**, không phải ngược HTF | Cần: `pd_D1` ở giữa (0.35–0.5) + array D1 còn xa + M5 setup đầy đủ + **size 50%** + **T1 only, không runner** |
| **Có thể, nhưng chỉ như tín hiệu chờ** (khuyến nghị của tôi) | Dùng M5 bearish setup làm **tín hiệu rằng nhịp hồi đang tiếp diễn**, và dùng nó để **chờ** một M5 bullish setup tại array D1 — thay vì vào lệnh short | Không cần điều kiện gì thêm; đây là cách dùng thông tin mà không thêm rủi ro |

> **Rule cứng đề xuất:** khi `pd_D1 < 0.35` (deep discount) và hướng D1 là tăng → **cấm mở short**, kể cả khi M5 setup hoàn hảo. Lý do không phải là "đạo lý HTF" mà là **số học R:R**: ở deep discount, khoảng cách tới đáy range (target khả thi của short) nhỏ, còn khoảng cách tới invalidation (đỉnh range) lớn → R:R thường < 1. Đây là lập luận **đo được**, không phải niềm tin.

**Q9. M5 bullish reversal có thể hợp lệ không?**
**Có** — nhưng phải thoả **5 điều kiện đồng thời**, và nếu thiếu một điều thì bạn đang bắt dao:

| # | Điều kiện | Vì sao |
|---|---|---|
| 1 | Giá ở **array D1/H4** thật (FVG/OB chưa mitigate), không chỉ "ở discount" | Discount không phải điểm vào |
| 2 | Có **sweep** một pool SSL **dưới** array đó (không phải sweep hụt) | Đây là dấu hiệu thanh khoản đã bị tiêu thụ ở đúng nơi |
| 3 | Sau sweep, giá **từ chối ở lại phía dưới** (reclaim trong `m` nến) | Phân biệt liquidity event với repricing event (§15.5) |
| 4 | Có **M5 MSS + displacement + FVG** để vào lệnh có cấu trúc | Cơ học entry |
| 5 | **Trong killzone** và còn đủ thời gian tới DOL | Nếu không, kỳ vọng giảm mạnh |

**Nếu thiếu điều kiện 2 hoặc 3** → đây là kịch bản (B)/(C), và mua là sai. Điều kiện 2+3 chính là **cơ chế Osler** (§6.1-CC2): thanh khoản bị tiêu thụ → momentum; nếu giá *không* reclaim, momentum đang đi ngược lại bạn.

**Q10. DOL nên được xác định lại như thế nào?**
Quy trình 4 bước, sửa theo §18.3 nhưng áp cho kịch bản này:

```text
B1. Pool BSL phía trên range D1 CÒN unswept không?
    CÒN  → DOL cấp D1 = pool đó (chưa đổi!). Nhịp giảm hiện tại là ĐƯỜNG ĐI, không phải đích.
    HẾT  → chuyển sang B2.

B2. Có D1 MSS/CHoCH bearish chưa?
    CÓ   → D1 DOL ứng viên = pool SSL lớn nhất phía dưới (DOL đảo chiều).
    CHƯA → chuyển sang B3.

B3. Đáy range D1 đã bị consumption chưa (close-through + không reclaim)?
    CHƯA → D1 chưa có DOL mới; DOL hiện hành vẫn là BSL ở B1 (nếu còn) 
           hoặc là "chưa xác định" → giảm size / chờ.
    RỒI  → range D1 INVALIDATED → chờ range mới → khi có range mới, lặp lại B1.

B4. Ở cấp H1/M5: DOL intraday = pool gần nhất chưa spent THEO HƯỚNG ĐƯỢC PHÉP.
    "Được phép" = hướng của D1 nếu D1 còn valid; hướng của range mới nếu không.
    ⛔ Không dùng DOL H1 để ghi đè DOL D1. DOL H1 ngược D1 = Judas fuel, không phải target.
```

**Q11. Premium/discount của range cũ còn meaningful không?**
**Có — nhưng ý nghĩa của nó thay đổi, và đây là một phân biệt tinh tế quan trọng:**

| Khía cạnh | Còn giá trị? | Vì sao |
|---|---|---|
| **`pd` như một số đo vị trí** | **CÒN** (miễn neo D1 chưa bị tiêu thụ) | Vị trí là sự kiện hình học, không phụ thuộc diễn giải |
| **`pd` như một lý do hành động** ("discount nên mua") | **KHÔNG còn đầy đủ** | Cần thêm: hướng range chưa flip + DOL ở trên + array tại chỗ (§19.2) |
| **Quadrant (deep discount)** | **CÒN** — dùng để chọn array ưu tiên | Ở deep discount, array D1 là ứng viên mạnh nhất |
| **EQ như ranh giới no-trade** | **CÒN** | Rule vận hành thuần tuý |
| **Dùng `pd` để kết luận hướng** | **KHÔNG BAO GIỜ** | §19.1 |

**Q12. Khi nào short-term bearish delivery trở thành evidence đủ mạnh để thay đổi HTF interpretation?**
Đây là câu hỏi quan trọng nhất và cần một câu trả lời **hội đủ điều kiện (conjunctive)**, không phải một ngưỡng đơn:

> **Đổi cách đọc HTF chỉ khi hội đủ 4 điều kiện:**
> 1. **Neo HTF bị phá bằng body-close**, không phải wick — và **không reclaim** trong `m` nến (`m` viết bằng số trước khi sự kiện xảy ra).
> 2. **Có MSS/CHoCH xác nhận ở khung HTF** (D1 hoặc W1), không chỉ ở H1.
> 3. **Điểm phá nằm ở premium của range HTF** (tức nhịp giảm bắt đầu từ nơi đắt, không phải từ discount) — hoặc, nếu bắt đầu từ discount, thì **BSL phía trên đã bị lấy trước đó**.
> 4. **Chấp nhận giá mới kéo dài qua ≥ vài phiên** (thời gian là bằng chứng, không phải chỉ mức giá).

**Nếu chỉ có 1–2 điều kiện:** giữ interpretation cũ, **giảm size**, và ghi `htf_under_review = true`. **Không** đổi bias. **Không** đảo chiều lệnh.

> [!danger] Lỗi tốn kém nhất ở đúng điểm này
> Trong kịch bản của bạn (bearish MSS ở H1 + bearish displacement + short-term delivery bearish), **rất dễ** kết luận "D1 đã đảo chiều" — vì ba dấu hiệu đó rất thuyết phục về mặt cảm giác. Nhưng ba dấu hiệu đó **đều là cấp H1**. Chúng không nói gì về D1. Tệ hơn: phản xạ này thường xuất hiện ở **đúng deep discount của range D1** — tức ở đúng nơi mà nếu D1 còn bullish, giá sẽ bật mạnh nhất. **Đây là cấu hình thua kinh điển: đảo bias ở đáy của một pullback.**
>
> **Cách tự bảo vệ (một câu, dán lên màn hình):** *"MSS ở khung nào thì chỉ có hiệu lực ở khung đó."*

### 21.3. Ma trận hành động theo bậc bằng chứng

| Bậc bằng chứng đã đạt | Cách đọc | Range D1 | Hành động | Size |
|---|---|---|---|---|
| Chỉ có wick qua internal swing | A (pullback) | VALID | Chờ setup Long tại array D1 | **100%** |
| Body-close qua internal + MSS H1 | A hoặc B | VALID | Chờ; **cấm short ở discount**; chờ MSS H1 bullish hoặc chờ array D1 | 50–100% (khi có setup) |
| Body-close qua **protected intermediate** + acceptance | B | VALID (neo D1 nguyên) | Hạ bậc luận điểm; chờ range mới ở cấp đó; chỉ trade theo range mới | 50% |
| Neo D1 body-close, chưa MSS D1 | B → C ứng viên | **REPLACED** | Chốt range mới; **không** đảo bias; chờ MSS D1 | 25–50% |
| Neo D1 phá + MSS D1 + acceptance ≥ vài phiên | **C** | **INVALIDATED** | Đổi cách đọc HTF; tìm setup theo hướng mới tại range mới | 50% (khởi đầu lại) |

![[DR-Deep-12-Thang-Bang-Chung-Pullback.svg|760]]
*Hình 12 — Thang bằng chứng cho kịch bản pullback sâu (§21). Mỗi bậc chỉ trả lời "tôi đang ở đâu" và gán size — **không** trả lời "giá sẽ đi đâu". Đổi cách đọc HTF chỉ khi hội đủ 4 điều kiện ở panel phải.*

### 21.4. Decision tree cho kịch bản này

```text
[Câu hỏi 0] Neo D1 (biên range đang chi phối) có bị chạm không?
│
├─ KHÔNG (chỉ internal/intermediate bị phá)
│   │
│   ├─ Cách phá = wick .................. → A. DEEP PULLBACK
│   │      Range D1: VALID · Bias: bullish · Hành động: chờ Long tại array D1
│   │
│   └─ Cách phá = body-close / displacement
│          │
│          ├─ Có reclaim trong m nến ... → LIQUIDITY EVENT (không phải B)
│          │      Range D1: VALID (unswept_count −1) · Hành động: chờ Long, 
│          │      neo vừa được "xác nhận"; nâng confidence
│          │
│          └─ Không reclaim ............. → B. INTERMEDIATE BEARISH
│                 Range D1: VALID (neo nguyên) · Bias: bullish nhưng "under review"
│                 Hành động: CẤM short ở discount; chờ MSS H1 bullish 
│                            HOẶC chờ giá tới array D1 để Long
│                 Size: 50%
│
└─ CÓ (neo D1 bị chạm)
    │
    ├─ Wick, đóng lại trong range ....... → KHÔNG PHẢI PHÁ
    │      Range D1: VALID · đây là sweep của chính neo → thường là điểm đảo chiều
    │      Hành động: chờ sweep + reclaim + MSS bullish → Long (setup chất lượng cao nhất)
    │
    └─ Body-close qua neo
        │
        ├─ D1 MSS/CHoCH chưa có ......... → SUSPENDED
        │      Range D1: REPLACED · Bias: giữ nguyên, hạ confidence
        │      Hành động: NO-TRADE cho tới khi có range mới + MSS D1
        │
        └─ D1 MSS/CHoCH đã có
            │
            ├─ Điểm phá từ PREMIUM ...... → C. GENUINE REVERSAL (ứng viên mạnh)
            │      Range D1: INVALIDATED · Bias: chuyển bearish (sau khi xác nhận W1)
            │      Hành động: tìm Short tại premium của range MỚI
            │
            └─ Điểm phá từ DISCOUNT ..... → C ứng viên YẾU
                   Kiểm tra: BSL phía trên đã bị lấy chưa?
                   ├─ CHƯA → nghi ngờ đây là Judas; chờ sweep SSL + reclaim + MSS bullish
                   └─ RỒI  → C hợp lệ hơn; vẫn cần W1 không ngược
```

---

## 22. Decision Tree tổng — từ "giá đang ở đây" tới quyết định

### 22.1. Cây chính (chạy trước mỗi phiên)

```text
BƯỚC 1 — HTF STRUCTURE
   W1/D1: HH-HL (tăng) / LH-LL (giảm) / không rõ (balance)?
   ├─ Không rõ → NO-TRADE (chưa có cấu trúc để đọc)
   └─ Rõ → BƯỚC 2

BƯỚC 2 — ỨNG VIÊN SWING
   Chạy thuật toán phát hiện swing (tham số theo khung) → danh sách ĐẦY ĐỦ
   ├─ Không có swing nào qua gate G1 → NO-TRADE
   └─ Có → BƯỚC 3

BƯỚC 3 — SWING SIGNIFICANCE (§10)
   Gate G1 (đã xác nhận) · G2 (phá nó đổi cấu trúc) · G3 (đúng cấp)
   ├─ <2 neo qua gate → NO-TRADE (không dựng được range)
   └─ ≥2 neo → BƯỚC 4

BƯỚC 4 — EXTERNAL LIQUIDITY
   Với mỗi neo: unswept hay spent?  Cụm/tf_stack?  Khoảng cách tới giá?
   ├─ Cả hai neo đều spent → BƯỚC 4b: dùng SD projection / chờ range mới → NO-TRADE nếu không có
   └─ ≥1 neo unswept → BƯỚC 5

BƯỚC 5 — SINH RANGE ỨNG VIÊN + CHỌN PRIMARY (§13.2)
   Lọc gate → lọc hiệu lực → sắp từ điển → PRIMARY / SECONDARY / REJECTED
   ├─ ∅ → NO-TRADE
   ├─ nested_conflict = true → giảm size 50% hoặc NO-TRADE
   └─ Có PRIMARY → BƯỚC 6

BƯỚC 6 — VALIDATE (§14.1 A1–A4)
   ├─ Trượt điều kiện cứng → quay lại BƯỚC 5 với tập ứng viên khác
   └─ Qua → BƯỚC 7

BƯỚC 7 — PREMIUM / DISCOUNT
   pd = (p−l)/(h−l)  → quadrant
   ├─ 0.40 ≤ pd ≤ 0.60 → NO-TRADE (vùng EQ)
   └─ Ngoài vùng EQ → BƯỚC 8

BƯỚC 8 — DOL (§18.3, có bằng chứng độc lập)
   ├─ Không viết được DOL kèm giá → NO-TRADE
   └─ Có DOL → BƯỚC 9

BƯỚC 9 — INTERNAL STRUCTURE
   Cấu trúc bên trong range: thuận hay nghịch hướng range?
   ├─ Nghịch + chưa có MSS cấp range → chờ (không vào)
   └─ Thuận → BƯỚC 10

BƯỚC 10 — PHÂN LOẠI MOVE HIỆN TẠI
   A. continuation  → vào theo hướng range, tại array, size đầy đủ
   B. pullback      → chờ array + xác nhận LTF, size đầy đủ
   C. internal reversal → chờ range con kết thúc; size 50%
   D. intermediate reversal → chỉ trade theo range MỚI ở cấp đó
   E. external reversal → chỉ sau MSS HTF; khởi động lại quy trình từ BƯỚC 1

BƯỚC 11 — QUYẾT ĐỊNH RANGE
   KEEP      (VALID)      → giữ nguyên, đo lại levels
   REFINE    (wick giãn)  → giữ nguyên phân tích, cập nhật số
   REPLACE   (neo mới)    → chốt range mới + cascade (§20.5)
   INVALIDATE(protected)  → xoá, chờ range mới, NO-TRADE tạm thời

BƯỚC 12 — H1 CONTEXT
   pd_H1 · alignment với pd_D1 · array H1 · internal structure H1
   ├─ Xung đột với D1 → chờ (rule §20.4)
   └─ Đồng thuận → BƯỚC 13

BƯỚC 13 — M5 EXECUTION
   Sweep → MSS → Displacement → FVG → Entry → SL → Target
   Điều kiện bắt buộc: trong killzone · R:R ≥ kế hoạch · SL ngoài cấu trúc
   ├─ Thiếu bất kỳ bước nào → KHÔNG VÀO
   └─ Đủ → VÀO LỆNH + ghi log (range_id, pd_htf, pd_ltf, DOL, invalidation)
```

### 22.2. Bảng trạng thái rút gọn (dùng như cheat sheet)

| State | Range | Bias | Hành động | Size |
|---|---|---|---|---|
| `trend-continuation` | VALID, ≥1 đầu unswept | Theo trend | Trade tại array đúng nửa range | 100% |
| `pullback-in-progress` | VALID (neo nguyên) | Giữ nguyên | Chờ array + xác nhận LTF | 100% khi có setup |
| `pullback-deep` | VALID nhưng neo gần | Giữ, `under_review` | Chỉ mua ở array, **cấm short ở discount** | 50% |
| `transition` | REPLACED | **Chưa** đổi | Chờ range mới + MSS HTF | 0% |
| `reversal-confirmed` | INVALIDATED | Đổi | Trade theo hướng mới, range mới | 50% (khởi động) |
| `balance` | VALID, hai đầu unswept, giá quanh EQ | Trung tính | Không giao dịch | 0% |
| `ambiguous` | ≥2 range mâu thuẫn | Không xác định | Không giao dịch | 0% |

---

## 23–24. Case Studies — 3 Bullish + 3 Bearish

> [!warning] Đọc tuyên bố phương pháp luận này trước khi đọc các case
> **Sáu case dưới đây là kịch bản TỔNG HỢP (synthetic), không phải lệnh thật**, và điều đó là **có chủ ý**:
>
> 1. **Case study chọn từ chart thật sau khi biết outcome là hindsight bias** — đúng cái mà đề bài yêu cầu tránh (yêu cầu #10, #11, #12). Mọi "case study" dạng "tôi đã thấy range này ở NQ ngày X và nó chạy đúng" đều là cherry-picking, và không thể dùng để kiểm chứng một framework.
> 2. Các case ở đây được dựng để **cô lập một quyết định cụ thể** trong framework. Chúng là **worked examples của thuật toán**, không phải bằng chứng cho hiệu quả.
> 3. **Kết quả (outcome) KHÔNG được dùng để chọn range trong bất kỳ case nào.** Range được chọn bằng quy trình §13.2, và nếu quy trình chọn một range "trông xấu" thì đó chính là nội dung của case (B2, S2).
> 4. Số liệu trong các case là **nhất quán nội bộ** (kiểm tra được bằng máy tính) nhưng **không tương ứng với một ngày giao dịch cụ thể nào**.
>
> **Cách dùng đúng:** đọc case → tự dựng lại quyết định theo thuật toán → so với đáp án → sau đó mới dùng **chính quy trình này** trên dữ liệu thật của bạn (mục Action items ở cuối bài).

---

## 23. Bullish Case Studies

### 23.1. Case B1 — NQ1: pullback sâu về discount, range "sách giáo khoa"

> **Nhãn:** `BR-01 · NQ1 · D1 bullish · deep discount · textbook`
> **Mục đích:** cho thấy thuật toán chọn đúng range mà một trader kinh nghiệm cũng chọn — và chỉ ra chỗ mà sự đồng thuận đó **không** có nghĩa là chắc chắn.

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | **Market context** | D1 uptrend nhiều tuần; W1 bullish; phiên hiện tại không có tin tier-1; giá đang trong pullback ngày thứ 3 |
| 2 | **Initial structure** | D1: HH 20,480 → HL 20,120 → HH 20,455 → pullback hiện tại về 20,205 |
| 3 | **Candidate swings** | SW-A high **20,480** (lấy PDH, để lại D1 FVG, BSL phía trên chưa lấy) · SW-B high **20,395** (LH nội bộ, không phá gì trên D1) · SW-C low **20,120** (quét EQL + PDL, là gốc của displacement leg tăng) · SW-D low **20,238** (HL nội bộ H1, tham chiếu cấu trúc H1) |
| 4 | **Candidate ranges** | R1 = **20,120 – 20,480** (D1) · R2 = 20,238 – 20,395 (H1 internal) · R3 = 20,120 – 20,395 (trộn cấp) |
| 5 | **Range selection** | Xem bảng gate bên dưới |
| 6 | **Why this swing** | SW-C: quét SSL + là gốc displacement để lại D1 FVG + là protected D1 low → G1∧G2∧G3, D≥1, L vừa spent nhưng tạo draw đối diện. SW-A: unswept BSL, tf_stack = 2 (trùng PWH 20,500 + mức tròn 20,500) |
| 7 | **Why not the others** | SW-B: **G2 fail** — phá nó không đổi nhãn cấu trúc nào trên D1 (nó đã bị vượt rồi) → loại. SW-D: **G3 fail cho range D1** — cấp H1; giữ lại làm neo cho R2 (execution). R3: **loại vì trộn cấp** hai neo |
| 8 | **Premium / Discount** | `pd(20,205) = (20205−20120)/360 = 0.236` → **deep discount** (ranh giới 0.25) |
| 9 | **Liquidity** | Trên: BSL 20,480 **chưa spent** + PWH 20,500 → `unswept_count = 1` (thoả A3). Dưới: SSL 20,120 **đã spent** |
| 10 | **DOL** | DOL D1 = **20,480** (T1) → **20,500** (T2, PWH + mức tròn). Bằng chứng độc lập: (a) BSL còn nguyên; (b) cấu trúc D1 HH/HL còn hiệu lực; (c) tf_stack = 2 |
| 11 | **HTF interpretation** | `state = pullback-in-progress`; bias bullish; W1 không ngược |
| 12 | **H1 interpretation** | H1 bearish (nhịp hồi), range R2 = 20,238–20,395, `htf_alignment = nghịch` → **TEMPORARY INTERNAL RANGE**: dùng để biết nhịp hồi đã đi tới đâu, **không** dùng để đổi bias |
| 13 | **M5 execution** | Chờ giá vào array D1 (FVG tại 20,190–20,215); trong killzone, chờ sweep SSL nội bộ (20,180) → M5 MSS + displacement + FVG → entry tại CE FVG ~20,205; SL dưới sweep low 20,140; TP1 20,395 (internal), TP2 20,480 |
| 14 | **Điều gì invalidate** | D1 đóng thân dưới **20,120** và không reclaim trong **3 phiên** + D1 MSS bearish → range `INVALIDATED`, bias `under_review` |
| 15 | **Alternative interpretation (steelman)** | "Toàn bộ nhịp từ 20,120 là một cú phân phối cuối cùng ở premium của range **tuần**; 20,480 sẽ bị quét rồi đảo mạnh" — Kiểm tra: nếu PWH 20,500 bị **quét + CISD xuống** trong cùng phiên, kịch bản này mạnh lên đáng kể. Đây là lý do phải có invalidation ở TP2 chứ không chỉ ở SL |
| 16 | **Backtest label** | `case=BR-01` · `pd_d1=0.236` · `anchor_type=DR-1` · `unswept_count=1` · `S_gate=pass` · `state=pullback` · `killzone=NY_AM` · `r_planned=2.8` · `outcome=<ghi sau replay>` |

**Bảng gate cho Case B1:**

| Ứng viên | G1 xác nhận | G2 phá-nó-đổi-cấu-trúc | G3 đúng cấp | D | L trạng thái | Kết quả |
|---|---|---|---|---|---|---|
| SW-A (high) | ✓ | ✓ (neo range) | ✓ | 1.3 | unswept, tf_stack 2 | **Nhận — neo high** |
| SW-B (high) | ✓ | **✗** | ✓ | 0.4 | spent | **Loại (G2)** |
| SW-C (low) | ✓ | ✓ (protected D1 low) | ✓ | 1.8 | vừa spent | **Nhận — neo low** |
| SW-D (low) | ✓ | ✓ (cấp H1) | **✗ cho D1** | 1.1 | unswept nhỏ | Chuyển sang R2 |

---

### 23.2. Case B2 — XAUUSD: range "xấu" thắng range "đẹp" (bài học trung tâm)

> **Nhãn:** `BR-02 · XAUUSD · D1 bullish · non-obvious primary range`
> **Mục đích:** đây là case quan trọng nhất trong 6 case. Nó cho thấy thuật toán chọn một range mà **mắt thường không chọn**, và vì vậy đưa ra kết luận **ngược** với cách đọc thị giác.

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | **Market context** | XAUUSD tăng từ 2,290 lên 2,372 trong 2 tuần, sau đó đi ngang 4 phiên trong biên 2,340–2,372. Không có tin lớn |
| 2 | **Initial structure** | D1: HH 2,372 → HL 2,318 (gốc displacement phá đỉnh cũ 2,344) → sideway |
| 3 | **Candidate swings** | SW-P high **2,372** (đỉnh mới, unswept) · SW-Q low **2,318** (gốc displacement leg phá 2,344, để lại D1 FVG) · SW-R low **2,340** (đáy của vùng đi ngang, bị test 2 lần) · SW-S high **2,368** (đỉnh nội bộ trong vùng ngang) |
| 4 | **Candidate ranges** | **α = 2,340 – 2,372** (hộp consolidation "đẹp", test 4 lần) · **β = 2,318 – 2,372** (neo = gốc displacement + đỉnh mới) |
| 5 | **Range selection** | α: SW-R **G2 fail** (phá 2,340 không đổi nhãn cấu trúc D1 — nó là đáy consolidation nội bộ). β: SW-Q **G2 pass** (phá 2,318 làm mất nhãn HL và phá chuỗi BOS) → **β là PRIMARY** |
| 6 | **Why this swing** | SW-Q là neo vì nó **gánh** chuỗi BOS (HH 2,344 → 2,372). SW-P là neo trên vì unswept |
| 7 | **Why not the others** | SW-R và SW-S bị loại vì **trông đẹp** nhưng không gánh kết luận cấu trúc nào. Đây chính là minh hoạ của §10.3: *hộp đẹp không phải hộp có nghĩa* |
| 8 | **Premium / Discount** | Giá 2,349. Trên β: `pd_β = (2349−2318)/54 = 0.574` → **premium nông**. Trên α: `pd_α = (2349−2340)/32 = 0.281` → **discount** |
| 9 | **Liquidity** | Trên β: 2,372 unswept. Dưới β: 2,318 unswept (pool SSL + round 2,320 gần đó) → `unswept_count = 2` |
| 10 | **DOL** | DOL = **2,372** (BSL unswept, T1); dưới là 2,318 (SSL) — nhưng **không** dùng làm DOL vì bias bullish và giá chưa ở deep discount |
| 11 | **HTF interpretation** | `state = pullback-in-progress`. Bias bullish giữ nguyên |
| 12 | **H1 interpretation** | H1 đi ngang quanh 2,356 (≈ EQ β). Vùng EQ → **không giao dịch** |
| 13 | **M5 execution — quyết định ex-ante** | **α nói "discount → mua ở 2,349". β nói "premium nông → chờ".** Framework chọn β → hành động đúng là **chờ**, không mua: (i) chờ giá về `pd_β ≤ 0.35` (≤ 2,337) và tới array (FVG D1 2,325–2,338), hoặc (ii) chờ sweep 2,318 + reclaim + M5 MSS bullish |
| 14 | **Điều gì invalidate** | Mua tại 2,349 **không phải** invalidation mà là **vi phạm quy trình**. Invalidation của luận điểm: D1 close dưới **2,318** + không reclaim trong 3 phiên |
| 15 | **Alternative interpretation (steelman)** | "Hộp α là accumulation thật; 4 lần test là evidence of absorption; β chỉ là một hộp lớn hơn vô nghĩa" — **Đây là phản biện mạnh nhất và nó có cơ sở**: test lặp lại có thể là hấp thụ (absorption). Phân xử: nếu 2,340 giữ được **và** giá tạo MSS tăng ngay từ đó **kèm** displacement (không phải grind), thì α là range đúng cho **execution** — nhưng β vẫn là range đúng cho **context**. Sự phân biệt này là lý do §13 cho phép PRIMARY + SECONDARY cùng tồn tại |
| 16 | **Backtest label** | `case=BR-02` · `pd_primary=0.574` · `pd_alt=0.281` · `decision=WAIT` · `range_conflict=α_vs_β` · `outcome=<ghi sau replay>` |

> [!important] Bài học của B2 — và đây là bài học bạn có thể áp ngay
> **Hai range hợp lệ cho hai kết luận trái ngược không phải là lỗi của framework — đó là thông tin.** Trong B2, α và β lệch nhau 22 USD ở neo low, và điều đó đủ để đảo kết luận từ "mua" sang "chờ". Nếu bạn chỉ nhìn một range, bạn sẽ không bao giờ biết kết luận của mình **không bền**. Vì vậy: **luôn chạy ít nhất hai ứng viên và ghi lại cả hai `pd`.** Đây chính là "fragility test" và nó miễn phí.

---

### 23.3. Case B3 — EURUSD: range cũ bị tiêu thụ một đầu → REPLACED, không phải INVALIDATED

> **Nhãn:** `BR-03 · EURUSD · D1 bullish · range replacement + cascade`
> **Mục đích:** phân biệt REPLACED vs INVALIDATED (§14.3) và cho thấy P/D cũ chết như thế nào.

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | **Market context** | EURUSD tăng 3 tuần; D1 bullish; tuần này giá phá đỉnh range cũ rồi tiếp tục |
| 2 | **Initial structure** | Range cũ **R-old = 1.0800 – 1.0980** (EQ 1.0890). Giá phá 1.0980 bằng displacement + acceptance, tiếp tục lên **1.1024** |
| 3 | **Candidate swings** | SW-1 low **1.0862** (HL cuối cùng trước BOS phá 1.0980 → **protected low mới**) · SW-2 high **1.0980** (neo cũ trên — nay đã spent) · SW-3 high **1.1024** (đỉnh mới, unswept) |
| 4 | **Candidate ranges** | R-old = 1.0800–1.0980 (consumed top) · **R-new = 1.0862–1.1024** · (không có ứng viên thứ ba hợp lệ) |
| 5 | **Range selection** | R-old: `unswept_count` phía trên = 0 → **A3 fail** → không còn là range vận hành được. R-new: SW-1 G2 pass (protected low), SW-3 unswept → **PRIMARY** |
| 6 | **Why this swing** | SW-1 là **protected low mới** (hệ quả Supersession §11.3). Neo này là hệ quả **trực tiếp** của cú BOS vừa xảy ra — không cần phán đoán |
| 7 | **Why not the others** | SW-2 (1.0980) bị loại vì **đã spent** — dùng nó làm neo là neo vào một mức đã hết thanh khoản. Đây là lỗi phổ biến: giữ neo cũ vì "nó từng quan trọng" |
| 8 | **Premium / Discount** | Giá 1.0898: `pd_new = (10898−10862)/162 = 0.222` → **deep discount**. Lưu ý: `pd_old = (10898−10800)/180 = 0.544` → **premium** trên range cũ |
| 9 | **Liquidity** | Trên: 1.1024 unswept (+1.1050 mức tròn, chưa tới). Dưới: 1.0862 unswept |
| 10 | **DOL** | DOL = **1.1024** (T1) → **1.1050** (T2, mức tròn) |
| 11 | **HTF interpretation** | `state = trend-continuation` (sau BOS mới). Bias bullish, confidence **tăng** (BOS xác nhận) |
| 12 | **H1 interpretation** | Cascade bắt buộc: **xoá** các range H1 cũ xây trên R-old; xây lại từ R-new. Các POI H1 cũ nằm trên 1.0980 mất context |
| 13 | **M5 execution** | Chờ pullback về FVG trong deep discount của R-new (vùng 1.0870–1.0890) → sweep SSL nội bộ → M5 MSS + FVG → entry, SL dưới 1.0862, TP1 1.0980 (internal, mức cũ giờ là IRL), TP2 1.1024 |
| 14 | **Điều gì invalidate** | Close dưới **1.0862** + không reclaim trong m nến → R-new `INVALIDATED`; protected low bị phá là sự kiện nặng nhất trong case này |
| 15 | **Alternative interpretation (steelman)** | "Cú phá 1.0980 là **terminal thrust** (kết thúc), 1.1024 là đỉnh cuối, và 1.0862 sẽ bị xuyên" — Kiểm tra: nếu cú phá 1.0980 **không** để lại FVG và giá quay lại dưới 1.0980 trong 2 nến, thì "phá" chỉ là một sweep → R-old còn VALID. Đây là ví dụ cho thấy **cách phá quyết định range sống hay chết** |
| 16 | **Backtest label** | `case=BR-03` · `pd_new=0.222` · `pd_old=0.544` · `event=range_replaced` · `cascade=yes` · `outcome=<ghi sau replay>` |

**Bài học then chốt của B3:** cùng một mức giá 1.0898, hai range cho hai kết luận **trái ngược hoàn toàn** (deep discount vs premium). Đây là **chứng minh bằng số** cho §9.2: *"premium/discount là gì" và "so với range nào" là **một** câu hỏi, không phải hai.*

---

## 24. Bearish Case Studies

### 24.1. Case S1 — NQ1: premium short có kiểm tra độ bền (fragility test)

> **Nhãn:** `SR-01 · NQ1 · D1 bearish · deep premium · fragility-tested`
> **Mục đích:** cho thấy cách **kiểm tra kết luận có bền không** bằng cách thay neo — thao tác gần như miễn phí nhưng ít ai làm.

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | **Market context** | NQ1 trong downtrend D1 sau khi tạo LH; W1 trung tính; giá đang hồi lên ngày thứ 2 |
| 2 | **Initial structure** | D1: LH 20,900 (đã quét PDH + BSL) → LL 20,410 → hồi hiện tại lên 20,780 |
| 3 | **Candidate swings** | SW-H high **20,900** (đã spent BSL phía trên) · SW-L low **20,410** (unswept SSL, LL mới) · SW-M high **20,845** (LH nội bộ) · SW-N low **20,455** (wick low nội bộ) |
| 4 | **Candidate ranges** | **R1 = 20,900 – 20,410** (D1, neo = LH + LL) · R2 = 20,845 – 20,410 (neo high thay thế) · R3 = 20,900 – 20,455 (neo low thay thế) |
| 5 | **Range selection** | R1 PRIMARY. SW-H pass G2 (BOS xuống đã phá LL trước đó) — dù đã spent, nó vẫn là **neo cấu trúc**; SW-L pass (unswept, LL) |
| 6 | **Why this swing** | SW-L là neo vì unswept **và** là LL mới được xác nhận bởi BOS. SW-H là neo vì nó là LH khởi phát leg giảm |
| 7 | **Why not the others** | SW-M (20,845) chỉ là LH nội bộ (G2 yếu — phá nó không đổi cấu trúc D1); SW-N (20,455) là wick nội bộ (G1 pass nhưng G2 fail) |
| 8 | **Premium / Discount** | `pd_R1(20,780) = (20780−20410)/490 = 0.755` → **deep premium** |
| 9 | **Liquidity** | Trên: 20,900 đã spent; 20,845 (EQH nhỏ) chưa spent → **inducement** (§17.3). Dưới: 20,410 unswept |
| 10 | **DOL** | DOL = **20,410** (T1) → **20,300** (T2, PWL + mức tròn) |
| 11 | **HTF interpretation** | `state = pullback-in-progress` trong downtrend; bias bearish |
| 12 | **H1 interpretation** | H1 bullish (nhịp hồi) tại premium H1 → **thời điểm** đang tốt cho Short, **hướng** do D1 quyết |
| 13 | **M5 execution** | Chờ sweep BSL nội bộ (20,845 EQH) → bearish MSS + displacement + FVG → entry tại CE FVG ~20,762; SL trên sweep high 20,812; TP1 20,455, TP2 20,410 |
| 14 | **Điều gì invalidate** | Close trên **20,900** + acceptance ≥ 2 phiên → R1 `INVALIDATED`. Nếu chỉ wick qua → sweep, range VALID |
| 15 | **Alternative interpretation (steelman)** | "Nhịp giảm từ 20,900 chỉ là pullback trong xu hướng tăng cấp **tuần**; 20,410 là HL của tuần này, và short tại 20,780 là short vào chân một nhịp tăng lớn" — Kiểm tra: W1 phải được đọc trước; nếu W1 bullish và W1 protected low còn nguyên thì kịch bản này mạnh → **giảm size hoặc bỏ** |
| 16 | **Backtest label** | `case=SR-01` · `pd=0.755` · `fragility=stable` · `inducement=20,845` · `outcome=<ghi sau replay>` |

**Fragility test — thao tác và kết quả (làm được trong 30 giây):**

| Cách chọn neo | `h` | `l` | `pd(20,780)` | Kết luận vẫn là "premium"? |
|---|---|---|---|---|
| **Neo gốc (R1)** | 20,900 | 20,410 | **0.755** | ✓ |
| Thay high bằng LH nội bộ (R2) | 20,845 | 20,410 | 0.808 | ✓ |
| Thay low bằng wick low (R3) | 20,900 | 20,455 | 0.730 | ✓ |
| Thay cả hai (xấu nhất) | 20,845 | 20,455 | 0.834 | ✓ |

> [!success] Vì sao thao tác này quan trọng hơn nó có vẻ
> Kết luận "premium" ở đây **bền** với mọi cách chọn neo hợp lý → bạn có thể tự tin về **vị trí**. Trong vault đã có tiền lệ đúng: một kết luận "9.3% depth" được kiểm lại với neo thay thế và ra 37.3% — khác số nhưng **cùng kết luận**, nên bền. **Nếu fragility test lật kết luận, đó là dấu hiệu range của bạn nằm sát EQ và mọi kết luận P/D đều là nhiễu** — chính xác trường hợp phải no-trade.

---

### 24.2. Case S2 — EURUSD: bẫy "hai lần discount" (cấu hình thua kinh điển)

> **Nhãn:** `SR-02 · EURUSD · D1 bearish · discount KHÔNG có nghĩa bullish`
> **Mục đích:** phá vỡ phản xạ "D1 discount + H1 discount = confluence Long".

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | **Market context** | EURUSD trong downtrend D1 3 tuần; hôm nay có dữ liệu nhỏ (không tier-1); giá đang ở vùng thấp của range D1 |
| 2 | **Initial structure** | D1: LH **1.1050** → LL **1.0820** → hồi nhẹ lên 1.0880. H1 đã tạo HL và cấu trúc H1 **bullish** |
| 3 | **Candidate swings** | SW-1 high 1.1050 (LH, neo trên) · SW-2 low **1.0820** (LL, unswept SSL) · SW-3 low 1.0855 (HL nội bộ H1) |
| 4 | **Candidate ranges** | **D1: 1.1050 – 1.0820** (h=230, EQ=1.0935) · **H1: 1.0855 – 1.0942** (h=87, EQ=1.0899) |
| 5 | **Range selection** | D1 PRIMARY; H1 = **SECONDARY**, và quan trọng hơn: H1 có `htf_alignment = nghịch` (H1 bullish vs D1 bearish) → nhãn **TEMPORARY INTERNAL RANGE** |
| 6 | **Why this swing** | SW-2: LL unswept + neo cấu trúc giảm. SW-1: LH khởi phát leg giảm |
| 7 | **Why not the others** | SW-3 (1.0855) là HL **cấp H1** → dùng cho H1 range, không đủ cấp cho D1 (G3 fail cho D1) |
| 8 | **Premium / Discount** | `pd_D1(1.0880) = (10880−10820)/230 = 0.261` → **discount**. `pd_H1(1.0880) = (10880−10855)/87 = 0.287` → **discount** |
| 9 | **Liquidity** | Trên: 1.0942 (EQH H1 nội bộ, chưa spent) → **inducement**; 1.1050 unswept. Dưới: **1.0820 unswept** |
| 10 | **DOL** | DOL = **1.0820** (SSL unswept, T1) → 1.0780 (T2) |
| 11 | **HTF interpretation** | `state = pullback-in-progress` **trong downtrend**. Bias bearish |
| 12 | **H1 interpretation** | H1 bullish = pullback. Vì D1 bearish, nhịp H1 này là **cơ hội bán ở premium H1**, không phải cơ hội mua |
| 13 | **M5 execution** | **Đây là điểm quyết định.** Cấu hình "D1 discount + H1 discount" trông như confluence Long. Cách đọc đúng: discount của một range **có hướng giảm** KHÔNG phải vùng mua — đó là **vùng tiếp diễn giảm** (§19.2 case 1). Hành động: (i) **không Long**; (ii) chờ H1 hồi lên premium H1 (>1.0899, lý tưởng 1.0920–1.0942) → sweep EQH 1.0942 → bearish MSS M5 + FVG → **Short**, SL trên 1.0950, TP1 1.0820. **Hoặc** (iii) nếu muốn Long: chỉ khi giá **quét 1.0820 + reclaim** + M5 MSS bullish → đó là kịch bản Judas, khác hoàn toàn về bản chất |
| 14 | **Điều gì invalidate** | D1 close trên **1.0942** + acceptance → H1 bullish có thể không còn là pullback; D1 close trên **1.1050** → range REPLACED |
| 15 | **Alternative interpretation (steelman)** | "1.0820 đã gần và sẽ bị quét trong phiên, sau đó đảo lên — đây là ngày Judas điển hình" — **Đây là kịch bản hoàn toàn hợp lý**, và nó là lý do không nên Long **trước** cú quét, mà chỉ Long **sau** cú quét + reclaim. Sự khác biệt giữa hai cách là **thời điểm**, và nó quyết định thắng/thua |
| 16 | **Backtest label** | `case=SR-02` · `pd_d1=0.261` · `pd_h1=0.287` · `conflict=discount_in_bearish_range` · `action=NO_LONG` · `outcome=<ghi sau replay>` |

> [!danger] Vì sao case này quan trọng nhất trong 3 case bearish
> Vì nó là **cấu hình thua phổ biến nhất của người mới** — và nó *trông* hoàn hảo: hai khung cùng discount, có vẻ như "cả hai thước đo cùng chỉ một hướng". Nhưng §19.1 đã chứng minh bằng logic rằng `pd` **không chứa thông tin hướng**. Hai discount chỉ là **một** discount được đo hai lần. Confluence thật phải là: `pd` + hướng range + DOL + array + thời gian. Trong case này, hướng range là **giảm** → discount không có nghĩa bullish.

---

### 24.3. Case S3 — GBPUSD: protected high bị phá → chuyển trạng thái (và cái bẫy sau đó)

> **Nhãn:** `SR-03 · GBPUSD · D1 bearish → transition · state machine exercise`
> **Mục đích:** luyện máy trạng thái §14.4 và cảnh báo về **bẫy thứ hai**: đảo bias rồi chase.

| # | Thành phần | Nội dung |
|---|---|---|
| 1 | **Market context** | GBPUSD downtrend D1 4 tuần; range D1 = **1.2740 – 1.2560** (h=180, EQ=1.2650). Giá ở 1.2700 = `pd 0.778` → premium sâu, Short hợp lệ |
| 2 | **Initial structure** | D1: LH 1.2740 → LL 1.2560 → hồi lên 1.2700. Protected high D1 = **1.2740** |
| 3 | **Candidate swings** | SW-H **1.2740** (protected high) · SW-L **1.2560** (LL, đã spent) · SW-M high 1.2685 (LH nội bộ) |
| 4 | **Candidate ranges** | R1 = 1.2740 – 1.2560 (D1 primary) |
| 5 | **Range selection** | R1 PRIMARY, `state = pullback-in-progress`, bias bearish |
| 6 | **Why this swing** | SW-H là protected high — phá nó làm mất hiệu lực chuỗi BOS giảm |
| 7 | **Why not the others** | SW-M là LH nội bộ, không gánh kết luận D1 nào |
| 8 | **Premium / Discount** | Ban đầu: `pd = 0.778` (deep premium) → vùng Short hợp lệ |
| 9 | **Liquidity** | Trên: 1.2740 unswept (và là protected) → **đây là pool sẽ bị test**. Dưới: 1.2560 spent |
| 10 | **DOL** | Ban đầu: DOL = 1.2560? **Không** — nó đã spent. DOL thật là pool SSL **dưới** 1.2560 (ví dụ 1.2520, PWL) |
| 11 | **HTF interpretation** | `state = pullback-in-progress`, bias bearish. **Sự kiện then chốt xảy ra sau đó:** D1 đóng thân **trên 1.2740** và giữ 4 phiên; D1 MSS bullish hình thành |
| 12 | **Range transition** | `σ(R1)`: VALID → **INVALIDATED**. `state`: pullback → **transition** → **reversal-confirmed**. Neo mới: range mới = **1.2560 – 1.2800** (h=240, EQ=1.2680) |
| 13 | **Điều gì invalidate (của luận điểm mới)** | Close trở lại dưới **1.2560** + acceptance → luận điểm tăng chết |
| 14 | **Bẫy thứ hai — phần quan trọng nhất của case này** | Sau khi đảo bias sang bullish, giá ở 1.2760 → `pd_new = (12760−12560)/240 = 0.833` → **deep premium của range TĂNG**. Nghĩa là: **đảo bias không có nghĩa mua ngay.** Hành động đúng: chờ pullback về `pd_new ≤ 0.5` (≤1.2680) + array, rồi mới Long. Đây là lỗi phổ biến thứ hai: đảo bias muộn rồi chase ở premium của range mới |
| 15 | **Alternative interpretation (steelman)** | "Cú phá 1.2740 là **sweep cuối**; protected high bị quét để lấy thanh khoản rồi giá sẽ quay xuống" — Kiểm tra: phân biệt bằng §15.5. Nếu **close trên + giữ ngoài + MSS** → repricing (luận điểm mới đúng). Nếu **wick trên + reclaim trong 1–2 nến** → raid (luận điểm cũ đúng, và đây sẽ là Short chất lượng cao tại premium). **Cùng một sự kiện "phá protected high" có hai kết cục trái ngược, phân biệt được bằng cách phá** |
| 16 | **Backtest label** | `case=SR-03` · `event=protected_high_broken` · `break_type=body_close+acceptance(4)` · `state_transition=pullback→reversal` · `pd_new=0.833` · `action=WAIT_PULLBACK` · `outcome=<ghi sau replay>` |

**Chuỗi trạng thái của R1 trong case S3 (minh hoạ máy trạng thái §14.4):**

```text
R1 VALID (pd 0.778, Short hợp lệ)
   │
   ├─ giá wick qua 1.2740 rồi đóng lại  → VALID (unswept_count −1) · sweep · giữ bias
   │                                       [đây là kịch bản 15-steelman]
   │
   └─ giá ĐÓNG THÂN trên 1.2740         → SUSPENDED (chờ m nến)
         │
         ├─ reclaim trong m nến          → VALID (đây là raid) · giữ bias · Short chất lượng cao
         │
         └─ giữ ngoài ≥ m nến + MSS D1   → INVALIDATED · transition · reversal-confirmed
                                            → range mới 1.2560–1.2800 · bias đảo · WAIT pullback
```

---

## 25. Counterexamples — 10 trường hợp TRÔNG như Dealing Range tốt nhưng KHÔNG nên dùng

Mỗi counterexample có ba phần bắt buộc: **vì sao nó trông hợp lệ** → **vì sao nó thực sự yếu** → **cách lọc nó**.

### CE-1. Range tạo bởi consolidation ngẫu nhiên (hộp "đẹp")
- **Trông hợp lệ vì:** biên rõ, giá test 3–4 lần, mắt nhìn thấy ngay một "cái hộp" — và hộp là thứ dễ vẽ nhất, nên nó hấp dẫn về mặt thị giác.
- **Thực sự yếu vì:** biên của một consolidation **không tham chiếu kết luận cấu trúc nào** (G2 fail). Cả hai neo đều là swing nội bộ có cấp thấp. Hơn nữa, trong consolidation, cực trị bị test nhiều lần → thanh khoản hai đầu bị tiêu hao dần → range mất chức năng draw.
- **Cách lọc:** chạy gate G2 trên cả hai neo. Câu hỏi duy nhất: *"phá biên này làm mất hiệu lực kết luận nào?"* Không trả lời được → **không dùng làm range chính**; nếu cần, chỉ dùng như vùng tham chiếu cho execution với nhãn `consolidation_ref`.

### CE-2. Swing không có displacement (grind)
- **Trông hợp lệ vì:** nó là một đỉnh/đáy rõ ràng, giá quay đầu ở đó, thậm chí quay đầu khá mạnh.
- **Thực sự yếu vì:** không có `disp ≥ 1` → **không có bằng chứng rằng thanh khoản ở đó đã bị tiêu thụ** (§10.1-D). Một mức mà giá "chạm rồi đi" bằng grind không nói lên điều gì về việc có lệnh lớn ở đó hay không. Những neo như vậy có xu hướng bị xuyên qua một cách dễ dàng ở lần test sau.
- **Cách lọc:** đo `disp` trên leg **bắt đầu từ** neo đó. `< 1.0 × ATR` → hạ xuống neo thứ cấp; nếu cả hai neo đều < 1.0 → range chỉ dùng cho context, không dùng để vào lệnh.

### CE-3. Swing không tạo meaningful structure (đỉnh cao nhất đã bị vượt)
- **Trông hợp lệ vì:** nó là **đỉnh cao nhất trên chart** — ấn tượng nhất về mặt thị giác, và "cao nhất" nghe như "quan trọng nhất".
- **Thực sự yếu vì:** đây chính xác là §10.3 — structural significance ≠ visual size. Một đỉnh đã bị vượt không còn gánh kết luận nào; dùng nó làm neo sẽ **nới rộng range giả tạo** và nén `pd` về giữa, làm mọi vùng P/D mất ý nghĩa.
- **Cách lọc:** nếu đỉnh đó **không phải** biên trên hiện hành của bất kỳ range nào đang dùng → nó là **reference sâu**, ghi vào bản đồ nhưng không dùng làm neo.

### CE-4. Range quá nhỏ so với timeframe đang phân tích
- **Trông hợp lệ vì:** nó có đủ hai neo, có displacement, thậm chí có FVG đẹp — về mặt cấu trúc nó "đúng".
- **Thực sự yếu vì:** ở cấp đó, nó **không có độ phân giải**. Stop không đặt được (nhỏ hơn spread + nhiễu), và target không đủ xa để R:R khả thi. Về mặt kỹ thuật nó là range hợp lệ của **khung nhỏ hơn** — dùng nó để đo khung lớn là lỗi sai loại (G3).
- **Cách lọc:** `range_height < 1.0 × ATR(khung)` → loại khỏi vai trò range chính. Với M5, đây là bộ lọc quan trọng nhất.

### CE-5. Range đã bị structurally invalidated nhưng chưa được xoá khỏi chart
- **Trông hợp lệ vì:** nó vẫn nằm trên chart, vẫn có hai đường ngang, và não bạn vẫn nhớ nó. Các mức của nó vẫn "khớp" với một số diễn biến gần đây (vì mọi mức đều khớp với *một cái gì đó* nếu bạn tìm đủ lâu).
- **Thực sự yếu vì:** `σ = INVALIDATED` — protected swing đã bị phá bằng body-close. Mọi `pd` đo trên nó là **số liệu của một cấu trúc không còn tồn tại**.
- **Cách lọc:** gắn trạng thái vào chính đối tượng vẽ trên chart (màu/ghi chú), và **thao tác xoá là bắt buộc**, không phải tuỳ chọn. Nếu bạn không xoá được vì "tiếc", đó là dấu hiệu bạn đang dùng range như một niềm tin, không phải một công cụ.

### CE-6. Range chỉ là internal noise
- **Trông hợp lệ vì:** trong một nhịp hồi, luôn có các swing nhỏ tạo thành một range gọn gàng. Nó "hoạt động" trong 5–10 nến, đủ để bạn tin.
- **Thực sự yếu vì:** nó là **TEMPORARY INTERNAL RANGE** (§14.3). Nó không có DOL độc lập và sẽ hết hiệu lực khi leg kết thúc. Nguy hiểm nhất là khi nó **ngược hướng** range lớn: dùng nó để suy bias là tự kéo bias theo nhịp hồi.
- **Cách lọc:** 5 tiêu chí ở §16.2-Q3. `<3` tiêu chí → không dùng. Và **rule cứng:** range con **không bao giờ** được đổi bias.

### CE-7. Range nằm giữa hai vùng external liquidity mà không có ý nghĩa cấu trúc
- **Trông hợp lệ vì:** nó nằm **giữa** một pool BSL lớn phía trên và một pool SSL lớn phía dưới → trông như "range mà thị trường sẽ dao động trong đó".
- **Thực sự yếu vì:** đây là **đảo ngược quan hệ nhân quả**. Việc có liquidity hai phía **không** làm cho khoảng giữa trở thành một range có nghĩa — nó chỉ có nghĩa là hai phía đều có lệnh. Trên thực tế, cấu hình này thường là **balance/accumulation**, tức là trạng thái mà kết luận đúng là **no-trade** (§13.3-tình huống A).
- **Cách lọc:** kiểm tra `pd` có cực trị không. Nếu giá quanh EQ và hai phía có mật độ pool tương đương → nhãn `balance`, không giao dịch.

### CE-8. Range được neo bởi news wick hoặc gap
- **Trông hợp lệ vì:** neo là **cực trị rõ ràng nhất** trên chart — một cây nến dài, dứt khoát, không thể nhầm.
- **Thực sự yếu vì:** neo đó là **artifact của một sự kiện**, không phải của cấu trúc. Nó vi phạm gate G1 ở dạng tinh tế (bên cạnh nó không có nến "sạch" bình thường), và nó kéo `h`/`l` lệch khỏi vùng giá thực sự giao dịch → `pd` và EQ lệch theo.
- **Cách lọc:** biến `news_driven ∈ {0,1}` và `gap_adjacent ∈ {0,1}`. Kiểm tra độ bền: đo lại `pd` với neo thay thế (bỏ wick). Nếu kết luận P/D **lật** → không dùng range đó cho tới khi cấu trúc sạch tái lập (§26-EC7, EC9).

### CE-9. "Range hindsight" — range chỉ hợp lệ vì bạn đã biết kết quả
- **Trông hợp lệ vì:** nó giải thích hoàn hảo mọi diễn biến đã xảy ra. Trên chart đã hoàn thành, nó là range **rõ nhất** — sạch, khớp, logic.
- **Thực sự yếu vì:** đây là **counterexample ở tầng phương pháp luận**, và là cái nguy hiểm nhất trong 10 cái. Không có gì sai với bản thân range; cái sai là **thời điểm bạn chọn nó**. Nếu bạn chọn nó sau khi biết outcome, bạn không đo được kỹ năng của mình — bạn đang đo khả năng kể chuyện. Tra cứu cho bài này ghi nhận chính ICT nói *"hindsight recognition is easier than prediction"* ([bestprops, IPDA vs Wyckoff](https://bestprops.com/ict-ipda-vs-wyckoff-theory/)), và một phê phán khác trong cộng đồng: *"Annotated screenshots benefit from hindsight bias"* ([BrokerChampion](https://brokerchampion.com/order-block-trading)).
- **Cách lọc:** **timestamp bắt buộc** (§12-bước 10) và **backtest có replay bar-by-bar** (§31). Nếu bạn không thể chứng minh mình đã chốt range trước sự kiện, dữ liệu đó **không được vào thống kê**.

### CE-10. Range đã "mòn" — nhiều lần test với phản ứng suy giảm
- **Trông hợp lệ vì:** càng nhiều lần test, càng trông như "mức quan trọng được thị trường tôn trọng".
- **Thực sự yếu vì:** §10.1-R, lực thứ hai: thanh khoản là hàng tiêu hao. Test 4–5 lần với biên độ phản ứng giảm dần = pool đã cạn → lần test tiếp theo có xác suất xuyên qua cao hơn.
- **Cách lọc:** biến `reaction_trend ∈ {tăng, phẳng, giảm}`. `giảm` + `n_tests ≥ 3` → hạ significance, chuyển range sang nhãn `worn` và tìm range mới. **Đây là biến mà hầu như không ai ghi — và nó miễn phí.**

---

## 26. Edge Cases — 20 tình huống và cách xử lý

| # | Edge case | Cách đọc | Rule vận hành | Journal field |
|---|---|---|---|---|
| EC1 | **Nhiều equal highs/lows** | Cụm = **một** pool, không phải nhiều | Gộp trong `~0.1–0.2 × ATR`; tính là 1 pool; `tf_stack` cộng dồn | `eq_cluster_n`, `eq_span_atr` |
| EC2 | **Hồi rất sâu (>79% range)** | Vị trí đúng nhưng **nhịp bị nghi ngờ** | Hồi > 0.79 của **DR-4** (leg) = cờ vàng cho bias, **không** phải lỗi entry. Hồi > 0.79 của **DR-1** (range) = bình thường | `retrace_depth_leg`, `retrace_depth_range` |
| EC3 | **Wick qua swing, đóng lại trong range** | **Liquidity raid** | Range **VALID**; `unswept_count −1`; đây thường là tín hiệu chất lượng cao cho hướng ngược lại | `break_type=wick`, `reclaim_bars` |
| EC4 | **Đóng thân qua swing** | **Structural break** | Range cấp đó `REPLACED`; chờ `m` nến xác nhận; đổi state nếu có displacement | `break_type=close` |
| EC5 | **Displacement xuyên protected swing** | Sự kiện nặng nhất | `INVALIDATED` + `transition`; **dừng** tìm lệnh theo hướng cũ cho tới khi có range mới | `protected_broken=true` |
| EC6 | **Grind xuyên swing (không displacement)** | Phá yếu | Chưa đủ để đổi state. Chờ acceptance (`m` nến). **Không** đổi bias | `break_type=grind` |
| EC7 | **Tin (CPI/NFP/FOMC)** | Nhiễu cấu trúc | `news_driven=true` + **re-draw range sau tin** (rule đã có trong [[59-Daily-Bias]]); không dùng neo tạo bởi tin làm neo chính | `news_driven`, `news_window` |
| EC8 | **Gap (thường)** | Vùng không giao dịch | Coi là liquidity void cần lấp; không chấm swing trong vùng gap | `gap_adjacent` |
| EC9 | **Weekend gap (FX/CFD)** | Neo giả | Không chấm STL/STH trong vùng gap; chờ 2–3 nến sạch (rule đã có trong [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]) | `weekend_gap` |
| EC10 | **Biến động thấp** | Ngưỡng ATR sai | `θ` động theo ATR **bắt buộc**; nếu không, mọi thứ trông như displacement | `atr_regime` |
| EC11 | **Biến động cao** | Range rộng bất thường | `range_height > 1.5 × ADR` → **cấm trade theo nửa range**; chỉ trade theo array + quadrant | `range_width_vs_adr` |
| EC12 | **Range lồng trong range** | Bình thường | Phân vai A/B/C (§3.3-Q7); không để hai tầng cùng quyết một việc | `nesting_level` |
| EC13 | **Range lồng trong HTF range** | Bình thường | HTF quyết hướng, LTF quyết thời điểm | `pd_htf`, `pd_ltf` |
| EC14 | **Range cũ vs range mới** | Tranh chấp | Ưu tiên theo §13.2 (không ưu tiên theo tuổi); kiểm tra consumption trước | `range_age`, `sigma` |
| EC15 | **Range có nhiều pool** | Bình thường | Gộp cụm + xếp hạng theo khung (`monthly > weekly > daily > session`) | `pool_count`, `pool_tier` |
| EC16 | **Range không có liquidity rõ** | Dấu hiệu xấu | Nếu cả hai đầu không có cụm/mức liên khung → hạ xuống `context_only`; **không** vào lệnh | `unswept_count=0` |
| EC17 | **False MSS** | Rất phổ biến | Yêu cầu **tối thiểu**: sweep + displacement + close qua swing (không phải wick). Thiếu 1 → không phải MSS | `mss_valid` |
| EC18 | **Sweep rồi continuation (không đảo)** | Bình thường | Đây là trường hợp **thường gặp nhất**; sweep **không** hứa đảo chiều. Đừng vào lệnh chỉ vì có sweep | `post_sweep=continuation` |
| EC19 | **Sweep rồi đảo thật** | Ít gặp hơn | Cần `reclaim + MSS + displacement` để phân biệt với EC18. **Xác suất thấp hơn EC18** — định cỡ theo đó | `post_sweep=reversal` |
| EC20 | **Structural break với displacement yếu** | Trạng thái lửng | `SUSPENDED`: chờ `m` nến. Không đổi state, không đổi bias, không re-map | `break_quality=weak` |

> [!important] Bốn edge case quan trọng nhất nếu bạn chỉ nhớ được bốn
> **EC18** (sweep → continuation là kết cục **thường gặp hơn** sweep → reversal — hầu hết trader mới mặc định ngược lại), **EC20** (SUSPENDED là trạng thái hợp lệ, không phải sự do dự), **EC3 vs EC4** (wick ≠ close — quyết định range sống hay chết), và **EC11** (range quá rộng làm `%` mất nghĩa).

---

## 27. Common ICT Trader Errors — ERROR → WHY → CONSEQUENCE → PREVENT

| # | Lỗi | Vì sao xảy ra | Hệ quả | Cách chặn |
|---|---|---|---|---|
| E1 | Chọn swing vì nó "trông lớn" | Não dùng kích thước như proxy cho tầm quan trọng; kích thước là thứ nhìn thấy ngay, cấu trúc thì phải suy | Range méo, `pd` nén về giữa, mọi vùng P/D vô nghĩa | **Gate G2 trước, xếp hạng sau** (§10.3) |
| E2 | Chọn range retrospectively | Trên chart đã hoàn thành, range đúng luôn rõ hơn nhiều; không ai nhớ mình đã do dự thế nào | Kỹ năng biểu kiến cao hơn thực tế; hệ thống không cải thiện | **Timestamp `t₀` bắt buộc** (§12-b10) |
| E3 | Cherry-picking range | Chọn range cho ra kết luận mình đã muốn | Vòng lặp tự xác nhận | Chạy **≥2 ứng viên** và ghi **cả hai** `pd` (fragility test — §23.3) |
| E4 | Đổi range sau khi biết outcome | Bảo vệ cái tôi; "range đúng phải là range giải thích được" | Không bao giờ sai → không bao giờ học | Log mọi lần REPLACED kèm lý do + thời điểm |
| E5 | Dùng P/D như tín hiệu độc lập | Nó đơn giản, dễ dùng, và có vẻ "có logic" | Bắt dao rơi ở discount của xu hướng giảm (§24.2) | Rule 5 biến (§19.5): thiếu 2/5 → không giao dịch |
| E6 | Coi mọi MSS là đảo chiều | MSS là sự kiện **cấp khung đó**; bản năng thì không phân cấp | Đảo bias ở đáy pullback (§21-Q12) | Câu dán màn hình: *"MSS ở khung nào chỉ có hiệu lực ở khung đó"* |
| E7 | Coi mọi sweep là đảo chiều | Sweep là sự kiện **thanh khoản**, không phải sự kiện **hướng** | Short vào Judas sweep trong ngày bullish (đã ghi trong [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]) | Phân biệt EC18 vs EC19; đòi `reclaim + MSS + displacement` |
| E8 | Dùng quá nhiều nested range | Càng nhiều tầng càng "chuyên nghiệp" về mặt cảm giác | Tê liệt phân tích; không tầng nào chi phối | **Tối đa 3 tầng** (A/B/C) và mỗi tầng một chức năng |
| E9 | Liên tục re-define range | Re-map cho cảm giác "đang cập nhật"; wick bị nhầm là phá | Mất bản đồ; mọi thống kê vô nghĩa | **Wick không bao giờ re-map**; chỉ body-close (§14.4) |
| E10 | Overfit chart lịch sử | Chọn tham số/neo trên chính dữ liệu đánh giá | Kết quả đẹp, live thua | **In-sample/out-of-sample tách trước** khi thử tham số (§31-C7) |
| E11 | Lẫn cấu trúc với narrative | Narrative dễ nhớ và thoả mãn hơn cấu trúc | Tin vào [F] như [A] | Rule ngôn ngữ §6.2: cấm chủ ngữ "họ/smart money" + động từ ý định |
| E12 | Giả định ý định institutional | Đó là cách kể chuyện hấp dẫn nhất, và không ai kiểm tra được | Niềm tin không thể sửa | Thay bằng cơ chế [B]: clustering lệnh + stop → market order (Osler) |
| E13 | **Vòng lặp logic range ↔ DOL** | Hai khái niệm được suy từ nhau nên luôn "khớp" | Cảm giác xác nhận giả; hệ thống không thể sai | Quy trình 4 bước có timestamp (§18.3) + DOL cần bằng chứng độc lập |
| E14 | Look-ahead bias trong backtest | Dùng chỉ báo repaint (ZigZag) hoặc đọc chart đã hoàn thành | **Toàn bộ** kết quả backtest vô nghĩa | Replay bar-by-bar; chỉ dùng thông tin có tại nến đó ([[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] §2.3) |
| E15 | Bỏ qua thời gian | Vị trí đúng nhưng không còn phiên để deliver | Entry đúng, target không tới | Bắt buộc kiểm tra killzone + reach phiên trước khi vào |
| E16 | Ghi log thiếu `anchor_type` | Không ai nghĩ là cần, cho tới khi trộn hai loại fib | Thống kê nhiễm, không cứu được (§3.1) | Trường `anchor_type ∈ {DR-1, DR-4}` bắt buộc trong mọi note |

---

## 28. Quantitative Formalisation — biến đo được, và giới hạn của phép đo

### 28.1. Bảng biến — định nghĩa, công thức, dữ liệu cần, độ tin cậy

| Biến | Định nghĩa | Công thức / cách đo | Dữ liệu cần | Độ tin cậy của phép đo |
|---|---|---|---|---|
| `swing_amplitude` | Biên độ của swing | `|h − adjacent_l|` | OHLC khung | Cao |
| `amp_atr` | Biên độ chuẩn hoá | `swing_amplitude / ATR_trễ(14)` | OHLC | Cao (**phải dùng ATR trễ** — §10.6) |
| `range_height` | Chiều cao range | `h − l` | OHLC | Cao |
| `range_width_vs_adr` | Range rộng bất thường? | `range_height / ADR(20)` | OHLC | Cao |
| `pd` | Vị trí trong range | `(p − l)/(h − l)` | OHLC | Cao |
| `duration_bars` | Số nến của leg | `t_swing2 − t_swing1` | OHLC | Cao |
| `retrace_depth` | Độ sâu hồi | `(extreme − pullback)/leg_height` **theo DR-4** | OHLC | Cao — nhưng phải ghi `anchor_type` |
| `disp` | Độ lớn displacement | `|close − open|_leg / (k·ATR_trễ)` | OHLC | Vừa (nhạy `k`; và ATR bị chính displacement ảnh hưởng) |
| `fvg_height` | Chiều cao imbalance | 3-nến gap | OHLC | Cao |
| `break_distance` | Độ xuyên qua mức | `max(penetration) / ATR_trễ` | OHLC | Cao |
| `bars_outside` | Số nến ở ngoài mức | Đếm | OHLC | Cao |
| `n_tests` | Số lần test neo | Số lần giá vào `±0.1·ATR` quanh neo | OHLC | Vừa (nhạy ngưỡng) |
| `reaction_magnitude` | Kích thước phản ứng | Cú bật sau mỗi test / ATR | OHLC | Vừa |
| `reaction_trend` | Xu hướng phản ứng | Hồi quy đơn giản của `reaction_magnitude` theo lần test | OHLC | **Thấp** — ít mẫu |
| `unswept_count` | Số đầu range còn pool | 0/1/2 | OHLC | Cao |
| `tf_stack` | Số khung có mức trùng | Đếm | OHLC nhiều khung | Vừa (nhạy ngưỡng khớp) |
| `clustered` | Có cụm không | `|h₁−h₂| ≤ 0.1·ATR` | OHLC | Vừa |
| `round_number` | Gần mức tròn | Khoảng cách tới mức tròn gần nhất | OHLC | Cao |
| `protection_age` | Tuổi của protected level | `t_now − t_protected` | OHLC | Cao |
| `protection_depth` | Khoảng cách tới P-L/P-H | `|p − protected| / ATR` | OHLC | Cao |
| `news_driven` | Có tin trong window? | Lịch kinh tế | **Dữ liệu ngoài** | Cao nếu có calendar |
| `volume` | Khối lượng | Tick volume (FX/CFD) hoặc contract volume (futures) | Tuỳ nguồn | **Thấp cho FX** — tick volume ≠ volume thật |
| `delta` / order flow | Mất cân bằng mua-bán | **Không có** nếu không có dữ liệu tick/footprint | Dữ liệu chuyên dụng | **Không đo được từ OHLC** |

> [!warning] Ranh giới cứng của phép đo — nói thẳng
> **Từ OHLC, bạn KHÔNG đo được:** khối lượng thật, mất cân bằng lệnh (delta), phân bố lệnh chờ, hay danh tính bên khớp. Mọi biến liên quan tới "liquidity" trong bảng trên đều là **proxy gián tiếp** (cụm mức, mức tròn, trạng thái spent) — **không phải phép đo thanh khoản**.
>
> Bằng chứng mạnh nhất về clustering lệnh (Osler) đến từ **dữ liệu order flow nội bộ của một dealing bank** — thứ bạn không có và không thể tái tạo từ chart. Vì vậy mọi tuyên bố kiểu "pool này có 500 lots" là **[F]**, không phải [A].
>
> **Hệ quả thực hành:** mọi nghiên cứu của bạn chỉ có thể trả lời câu hỏi *"các cấu hình giá có tên gọi X có cho kết quả khác baseline không?"* — chứ **không** trả lời được *"vì sao"* ở tầng vi cấu trúc. Đó là lý do các giả thuyết ở §32 được phát biểu ở dạng so sánh kết quả, không ở dạng cơ chế.

### 28.2. Bốn mức độ của phép đo (và đừng nhầm chúng)

| Mức | Ví dụ | Dùng được cho |
|---|---|---|
| **Đo trực tiếp, chính xác** | `pd`, `range_height`, `bars_outside`, `unswept_count` | Mọi thống kê; làm biến độc lập |
| **Đo được nhưng nhạy tham số** | `disp`, `n_tests`, `tf_stack`, `clustered` | Thống kê **kèm sensitivity analysis** theo tham số |
| **Proxy gián tiếp** | "liquidity significance", "reaction trend", `S_score` tổng hợp | Chỉ dùng để **xếp hạng nội bộ**, không dùng làm biến độc lập trong hồi quy |
| **Không đo được từ OHLC** | delta, volume thật, ý định, "pool size" | **Không dùng.** Nếu buộc phải nói, ghi nhãn [F] |

### 28.3. Ba bẫy thống kê đặc thù của loại dữ liệu này

**(1) Bẫy chuẩn hoá ATR (đã nêu ở §10.6).** Nếu `disp` và ngưỡng `N`/`θ` đều dùng ATR hiện tại, biến phụ thuộc và biến độc lập **chia sẻ cùng một mẫu số** → tương quan giả. **Chữa:** dùng ATR **trễ** (cửa sổ kết thúc trước khi leg bắt đầu).

**(2) Bẫy khoảng cách.** Một target ở gần **luôn** có xác suất bị chạm cao hơn target ở xa — bất kể nó là mức gì. Mọi nghiên cứu "mức X có bị chạm không" mà không kiểm soát khoảng cách đều sẽ kết luận sai rằng mức X "có sức hút". **Chữa:** baseline ngẫu nhiên **cùng khoảng cách** (§18.5, §32-H1).

**(3) Bẫy chọn mẫu theo outcome.** Nếu chỉ phân tích những setup bạn đã vào lệnh, mẫu bị chọn theo tiêu chí bao gồm cả những thứ bạn chỉ nhận ra sau đó. **Chữa:** mẫu phải là **tất cả các thời điểm** thoả tiêu chí cấu trúc, kể cả những lần bạn không giao dịch (đây là điều kiện để đo được "bỏ lỡ" và "tránh được").

---

## 29. Dealing Range Quality Score — ba tầng, và tầng nào được tin

### 29.1. Tầng 1 — Heuristic score (dùng được ngay, KHÔNG phải edge)

$$
Q_{\text{heur}} = \underbrace{g}_{\text{gates } \in \{0,1\}} \times \Big[ w_1 L + w_2 D + w_3 R + w_4 P + w_5 C' \Big]
$$

Điểm khác biệt so với `S_score` ở §10.2: `Q` chấm điểm **cả range** (không chỉ một neo), nên nó cộng thêm hai số hạng:

| Số hạng | Nội dung | Vì sao có |
|---|---|---|
| `L` | chất lượng liquidity của **neo yếu hơn** (weakest link) | Range không thể mạnh hơn neo yếu nhất |
| `D` | displacement của **leg tốt hơn** trong hai leg | Một leg tốt đủ để range có nghĩa |
| `R` | reaction trung bình hai neo, **có trừ điểm** nếu `reaction_trend = giảm` | Xem CE-10 |
| `P` | protected status + độ sâu | Xem §15 |
| `C'` | `confluence_count` (mức liên khung trùng) — **hệ số nhỏ** | Xem §10.1-C (nguy cơ vòng lặp) |
| `g` | gates G1∧G2∧G3 — **nhân, không cộng** | Gate không bù trừ được |

> [!danger] Tuyên bố giới hạn của tầng này — đọc kỹ
> **Các trọng số `w₁…w₅` CHƯA BIẾT.** Tôi từ chối đưa số cụ thể. `Q_heur` chỉ có hai công dụng hợp lệ:
> 1. **Xếp hạng nội bộ** giữa các ứng viên trong cùng một thời điểm (đây là công dụng chính, và nó đã được dùng trong §13.2 dưới dạng thứ tự từ điển).
> 2. **Ghi log** để sau này hiệu chuẩn.
>
> `Q_heur` **KHÔNG** được dùng để: quyết định size, quyết định no-trade, hay tuyên bố "range chất lượng 8/10 nên chắc thắng". Nó là **bảng xếp hạng**, không phải **xác suất**.

### 29.2. Tầng 2 — Rule-based score (gate-based, có thể code, kiểm tra được)

Thay vì cộng điểm, dùng **số gate đã qua** như một biến thứ tự (ordinal):

| Hạng | Điều kiện | Ý nghĩa vận hành |
|---|---|---|
| **A** | G1∧G2∧G3 ∧ `unswept_count = 2` ∧ `D ≥ 1` ∧ có array | Range tốt nhất có thể có |
| **B** | Gates ∧ `unswept_count ≥ 1` ∧ `D ≥ 1` | Range vận hành được |
| **C** | Gates ∧ `unswept_count ≥ 1` ∧ `D < 1` | Range dùng được cho context, **không** để entry |
| **D** | Gates ∧ `unswept_count = 0` | Đã tiêu thụ hai đầu → chỉ dùng cho SD projection |
| **F** | Trượt gate | Không dùng |

**Ưu điểm của tầng 2 so với tầng 1:** nó **không có tham số tự do**. Do đó nó **không thể bị overfit** — và đó là lý do nó đáng tin hơn tầng 1, dù nó thô hơn. Trong nghiên cứu, thô mà không có tham số tự do thường thắng tinh mà có 5 tham số tự do.

### 29.3. Tầng 3 — Statistically validated score: protocol hiệu chuẩn

Muốn biến `Q` thành một con số có nghĩa xác suất, phải làm **đúng thứ tự sau**. Bỏ bước nào cũng dẫn tới overfit.

```text
BƯỚC 1 — ĐỊNH NGHĨA OUTCOME TRƯỚC
   Chọn nhãn nhị phân hoặc liên tục, ví dụ: y = 1 nếu giá đạt +2R trước −1R (double-barrier).
   Chốt y TRƯỚC khi xem bất kỳ biến nào. Không đổi y sau khi thấy kết quả.

BƯỚC 2 — THU THẬP MẪU KHÔNG CHỌN LỌC (unconditional sampling)
   Mẫu = MỌI thời điểm thoả điều kiện cấu trúc, KHÔNG chỉ những lần bạn vào lệnh.
   Ghi cả các trường hợp "đã cân nhắc nhưng không vào".

BƯỚC 3 — CHIA DỮ LIỆU TRƯỚC KHI THỬ BẤT CỨ GÌ
   In-sample (60%) / out-of-sample (40%), chia theo THỜI GIAN (không chia ngẫu nhiên —
   chia ngẫu nhiên làm rò rỉ thông tin giữa các giai đoạn thị trường).

BƯỚC 4 — FIT MÔ HÌNH ĐƠN GIẢN NHẤT CÓ THỂ
   Logistic regression với 3–5 biến (khuyến nghị: pd, unswept_count, disp, tf_stack, pd_htf).
   Ràng buộc dấu kỳ vọng (monotone constraints) nếu công cụ cho phép:
     pd thấp hơn → xác suất đạt target tăng (với bias bullish).
   Mục đích của ràng buộc: chặn mô hình học những quan hệ vô lý do nhiễu.

BƯỚC 5 — ĐO TRÊN OUT-OF-SAMPLE
   Báo cáo: AUC (phân biệt), calibration curve (xác suất có đúng không), 
   và Brier score. AUC cao mà calibration lệch = mô hình vô dụng để định cỡ.
   ⛔ KHÔNG tinh chỉnh gì trên out-of-sample. Nếu phải sửa → quay lại BƯỚC 3 với split mới.

BƯỚC 6 — KIỂM TRA ĐỘ BỀN (sensitivity)
   Chạy lại với: (a) tham số N/θ khác ±50%; (b) ATR trễ vs ATR hiện tại;
   (c) cửa sổ thời gian khác. Nếu dấu của hệ số đổi → biến đó KHÔNG ổn định → bỏ.

BƯỚC 7 — CHỈ SAU ĐÓ mới dùng trọng số đã fit cho size/decision
```

**Ba điều phải nói rõ về protocol này:**

1. **Cỡ mẫu cần lớn hơn bạn nghĩ — rất nhiều.** Với `R` có độ lệch chuẩn ~1.5R, để phát hiện khác biệt expectancy **0.2R** ở mức ý nghĩa 5% và power 80%, cần khoảng **~880 setup mỗi nhóm**. Với 200 setup, bạn chỉ phát hiện được khác biệt **≥ ~0.42R**. Nghĩa là: **hầu hết backtest của trader cá nhân không đủ lực thống kê để phân giải bất cứ điều gì tinh tế.** Đây là sự thật khó chịu nhưng cần biết trước khi đầu tư 6 tháng vào một thang điểm.
2. **Hệ quả chiến lược:** khi không đủ mẫu, hãy nghiên cứu **cấu trúc quy trình** (tầng 2 — gate-based) thay vì **trọng số** (tầng 1). Tầng 2 không cần mẫu lớn để đúng, vì nó không ước lượng tham số nào.
3. **Cảnh báo overfitting đặc thù:** mỗi lần bạn thử một biến mới và giữ nó vì "kết quả đẹp hơn", bạn đã tiêu một bậc tự do. Với 5 biến và 5 ngưỡng, số cấu hình khả dĩ là rất lớn — và bạn đang **tìm kiếm** trong không gian đó. Cách chặn duy nhất là **đếm số lần thử** và báo cáo nó.

---

## 30. Formal Algorithm / Pseudocode

> [!info] Quy ước
> - Mọi hàm nhận `bars` **chỉ tới nến hiện tại** — không có tham số nào cho phép nhìn tương lai. Đây là ràng buộc **kiến trúc**, không phải lời khuyên.
> - `⚠️` = bước **không định lượng được đáng tin**; hàm trả về nhãn `UNQUANTIFIED` để con người quyết định, và **phải ghi log** rằng bước đó do người quyết.

```python
# ============================================================
# DEALING RANGE ALGORITHM v1.0
# ============================================================

def detect_swings(bars, tf, N=None, theta=None):
    """STEP 1-2: phát hiện swing. N-bar pivot (causal) hoặc DC threshold theo ATR trễ."""
    if N is not None:
        # pivot: cần N nến SAU mới xác nhận -> t_confirm = t_swing + N
        highs, lows = n_bar_pivot(bars, N)
    else:
        highs, lows = directional_change(bars, theta)   # theta = k * ATR_lagged
    return [Swing(t, price, kind, t_confirm=t + N) for ...]

def classify_swing(sw, structures_by_tf):
    """STEP 3 (một phần) + §11.2: phân cấp theo PHẠM VI VÔ HIỆU (đệ quy)."""
    level = 1                                   # micro
    if references_any_conclusion(sw): level = 2 # internal
    if breaking(sw) changes_label(mid_tf): level = 3
    if breaking(sw) changes_extreme(governing_range): level = 4
    if breaking(sw) invalidates(higher_tf): level = 5
    return level

def gates(sw, tf, structures):
    """TẦNG 1 — GATES. Nhị phân, không bù trừ. §10.2"""
    G1 = sw.confirmed                        # đã có N nến sau
    G2 = breaking(sw) changes_any_label(structures)   # phá nó đổi nhãn cấu trúc?
    G3 = (sw.tf_params == params_for(tf))    # đúng cấp
    return G1 and G2 and G3

def score_swing(sw, bars, tf):
    """TẦNG 2 — SCORES. Trả về dict, KHÔNG trả về tổng có trọng số."""
    atr = atr_lagged(bars, 14)               # ATR TRỄ (§10.6)
    return {
      "L": liquidity_score(sw, bars, atr),   # clustering, tf_stack, unswept, round
      "D": displacement_score(sw, bars, atr),# disp, fvg_present, close_location
      "R": reaction_score(sw, bars, atr),    # n_tests, penetration, reaction_trend
      "P": protected_score(sw, structures),  # is_protected, protection_depth
      "C": confluence_count(sw, bars)        # CHỈ để xác nhận, hệ số nhỏ
    }

def build_candidates(swings, tf):
    """STEP 8: sinh range ứng viên từ các cặp neo qua gate."""
    C = []
    for h in [s for s in swings if s.kind == 'H' and gates(s, tf)]:
        for l in [s for s in swings if s.kind == 'L' and gates(s, tf)]:
            if h.t > l.t or l.t > h.t:                    # hai neo phải bao quanh giá
                C.append(Range(h=h, l=l, tf=tf, t0=now(), anchor_type="DR-1"))
    return dedupe_overlapping(C)

def validity(rng, bars, m):
    """STEP 13 (§14.1): điều kiện CỨNG."""
    A1 = both_anchors_confirmed(rng)
    A2 = all(breaks_something(a) for a in (rng.h, rng.l))
    A3 = unswept_count(rng, bars) >= 1
    A4 = rng.t0 < now()                                   # chốt trước sự kiện
    return all([A1, A2, A3, A4])

def state(rng, bars, m):
    """STEP 14 (§14.4): máy trạng thái."""
    if not validity(rng, bars, m):        return "INVALIDATED"
    if wick_through(rng, bars) and closed_inside(rng, bars):
        rng.unswept_count -= 1;           return "VALID"       # raid, không phải phá
    if close_through_any_anchor(rng, bars) and not reclaimed(bars, m):
        return "REPLACED"
    if protected_broken(rng, bars) and bars_outside(bars) >= m:
        return "INVALIDATED"
    if bars_since_event(bars) < m:        return "SUSPENDED"   # chưa đủ dữ liệu để phán
    return "REFINED" if wick_extended(rng, bars) else "VALID"

def select_primary(C, bars):
    """STEP 9-11 (§13.2): THỨ TỰ TỪ ĐIỂN — không dùng tổng có trọng số."""
    C = [c for c in C if gates_ok(c) and state(c, bars) in ("VALID","REFINED")]
    if not C: return None, None, []                      # NO-TRADE
    C.sort(key=lambda c: (
        -c.gate_strength(),      # khoá 1: G2 ∧ D≥1 ∧ L chưa spent
        -c.unswept_count,        # khoá 2: số đầu còn pool
        -c.containment_rank,     # khoá 3: range lớn thắng ở tầng A
        -c.S_score(),            # khoá 4
        +c.age                   # khoá 5: CHỈ ở đây tuổi mới được dùng
    ))
    primary = C[0]
    secondary = max([c for c in C if contained_in(c, primary)], key=S_score, default=None)
    return primary, secondary, C[1:]

def map_liquidity(rng, bars):
    """STEP 16 (§17): bản đồ thanh khoản, vai trò PHỤ THUỘC vị trí giá."""
    pd = pd_of(price(bars), rng)
    pools = {"above": find_pools_above(rng.h), "below": find_pools_below(rng.l),
             "internal": find_internal_arrays(rng)}
    for p in pools["above"] + pools["below"]:
        p.role = ("draw"   if (pd < 0.5 and p.side == "above") or
                              (pd > 0.5 and p.side == "below")
                  else "fuel")                            # §17.2
    return pools

def determine_dol(rng, bars, pools, structures):
    """STEP 17 (§18.3): DOL dùng bằng chứng ĐỘC LẬP với range."""
    ev = {
      "pendulum": which_side_just_consumed(bars),   # (a) quan trọng nhất
      "structure": last_bos_direction(structures),  # (b)
      "multitf":   pools_referenced_by_multiple_tfs(bars),  # (c)
      "reach":     feasible_in_session(bars)        # (d)
    }
    candidates = [p for p in pools.values() if not p.spent and p.side == bias_dir(ev)]
    if not candidates: return None                    # NO-TRADE
    dol = min(candidates, key=lambda p: (p.tier_rank, distance(p, price(bars))))
    dol.conflict = (dol.side != expected_side(rng))   # ghi nhận, KHÔNG đổi range
    return dol

def unquantified_flags(...):
    """⚠️ CÁC BƯỚC KHÔNG ĐỊNH LƯỢNG ĐƯỢC ĐÁNG TIN — trả về nhãn cho con người."""
    return {
      "narrative":       "UNQUANTIFIED",  # §33: 'câu chuyện' không đo được
      "weight_fitting":  "UNQUANTIFIED",  # §29.3: cần dữ liệu, không suy ra được
      "range_conflict":  "HUMAN_DECISION",# khi ≥2 range cùng hạng (§13.3-A)
      "news_context":    "EXTERNAL_DATA", # cần calendar
      "intent":          "NOT_MEASURABLE" # §6.2: cấm suy ra
    }

# ============================================================
# VÒNG LẶP CHÍNH — chạy mỗi nến, CHỈ dùng dữ liệu tới nến đó
# ============================================================
def on_bar(bars):
    S      = detect_swings(bars, tf)                 # STEP 1-2
    for s in S: s.level = classify_swing(s, structures)   # STEP 3
    cands  = build_candidates([s for s in S if gates(s, tf)], tf)  # STEP 8
    P, Sec, rest = select_primary(cands, bars)       # STEP 9-11
    if P is None: return StateOutput(decision="NO_TRADE", reason="no_valid_range")
    P.sigma = state(P, bars, m)                      # STEP 12-14
    pd = pd_of(price(bars), P)                       # STEP 15
    pools = map_liquidity(P, bars)                   # STEP 16
    dol = determine_dol(P, bars, pools, structures)  # STEP 17
    return StateOutput(                              # STEP 18
      primary=P, secondary=Sec, sigma=P.sigma, pd=pd, quadrant=quadrant(pd),
      unswept=P.unswept_count, pools=pools, dol=dol,
      state=classify_state(structures, P, pd),
      decision=("NO_TRADE" if pd_between(pd, 0.40, 0.60) or dol is None
                else "SEEK_SETUP"),
      flags=unquantified_flags())
```

### 30.1. Ba bước trong pseudocode này mà tôi nói thẳng là không định lượng được

| Bước | Vì sao không định lượng được | Xử lý đúng |
|---|---|---|
| `classify_state(...)` — phân loại `pullback` vs `transition` vs `reversal` | Đây là **suy luận về tương lai** từ dữ liệu quá khứ. Không có nhãn ground truth tại thời điểm chạy | Trả về **phân phối** (3 nhãn + trọng số từ §21.3), không trả về một nhãn |
| `fit weights` cho `S_score` / `Q` | Cần mẫu lớn mà hầu hết trader không có (§29.3) | Dùng tầng 2 (gate-based) làm mặc định; coi tầng 1 là bảng xếp hạng |
| `find_pools_*` — xác định "pool" | Không có order book; chỉ có proxy từ OHLC (§28.1) | Ghi nhận đây là **proxy**, và **không** dùng số lượng pool làm biến định lượng trong mô hình |

> [!important] Điều quan trọng nhất về đoạn code này
> Nó **không** chứa một dòng nào quyết định vào lệnh. Nó chỉ trả về **trạng thái** (`StateOutput`). Quyết định vào lệnh vẫn thuộc về con người, dựa trên state + kế hoạch + quản trị rủi ro. **Đây là thiết kế có chủ ý:** một thuật toán không thể chịu trách nhiệm về một suy luận mà chính nó không thể kiểm chứng.

---

## 31. Backtesting Framework

### 31.1. Trả lời 10 câu hỏi thiết kế

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | **Unit of observation là gì?** | Một **(symbol, timeframe, thời điểm)**, tại đó tồn tại một range hợp lệ qua gate. **Không phải** một lệnh — vì nếu lấy lệnh làm đơn vị, bạn chỉ đo được những lần bạn đã hành động (chọn mẫu theo outcome) |
| 2 | **Entry không nên được dùng để define range như thế nào?** | Range phải được chốt **trước** khi có entry, và **không** được điều chỉnh để entry nằm trong discount. Kiểm tra cứng: `t₀ < t_entry` và `pd` tại thời điểm entry được tính từ range có `t₀` đó |
| 3 | **Tránh hindsight bias thế nào?** | (a) `t₀` bắt buộc; (b) mẫu không chọn lọc (gồm cả lần không vào lệnh); (c) **hai người chấm độc lập** trên một tập mẫu nhỏ để đo mức đồng thuận; (d) không bao giờ dùng "range đúng" để định nghĩa "range đã dùng" |
| 4 | **Tránh look-ahead bias thế nào?** | Replay bar-by-bar; chỉ chỉ báo causal; ATR trễ; cấm ZigZag không-replay ([[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] §2.3). **Kiểm tra tự động:** chạy lại cùng thời điểm với dữ liệu cắt ngắn — nếu output khác → có look-ahead |
| 5 | **Khi nào range được "known" trong real time?** | Tại `max(t_confirm(h), t_confirm(l))`. Đây là **`t_known`**, và **không** phải `t_swing`. Mọi thống kê phải dùng `t_known` |
| 6 | **Khi nào swing được confirmed?** | Sau `N` nến (pivot) hoặc sau khi vượt `θ` (DC). Không có ngoại lệ — đây là **bản chất** của việc biết một cực trị là cực trị |
| 7 | **Có cần confirmation candles không?** | Có, và chúng **không phải tuỳ chọn** — chúng là **độ trễ thông tin**. Không tính chúng = dùng thông tin tương lai |
| 8 | **Timestamp range creation thế nào?** | `t₀ = max(t_confirm(h), t_confirm(l))`, ghi cả `t_swing` và `t_confirm` của từng neo |
| 9 | **Timestamp invalidation thế nào?** | `t_inval` = nến đầu tiên thoả điều kiện invalidation **viết trước**; ghi kèm `invalidation_type ∈ {close_through, protected_break, both_extremes_spent, replaced}` |
| 10 | **Label outcome thế nào?** | **Double barrier** (§31.3): từ `t_known`, xem `+kR` hay `−1R` tới trước. Ghi cả **MAE/MFE** để phân tích, không chỉ nhị phân |

### 31.2. Dataset schema

```text
# ---- ĐỊNH DANH ----
range_id            # khoá duy nhất
run_id              # lần chạy quy trình (để so các phiên bản)
symbol              # NQ1 / EURUSD / XAUUSD / GBPUSD
timeframe           # D1 / H4 / H1 / M15 / M5
workflow            # "D1-H1-M5" (vì phân cấp phụ thuộc workflow - §11.2)

# ---- NEO & RANGE ----
anchor_high, anchor_low
anchor_type         # DR-1 | DR-3 | DR-4   (BẮT BUỘC - §3.1)
range_size, range_height_atr, range_width_vs_adr
atr_lagged_14       # ATR TRỄ, không phải ATR hiện tại
eq                  # (h+l)/2
t_swing_h, t_swing_l, t_confirm_h, t_confirm_l
t_known             # max(t_confirm)  -> mốc causal
t_zero              # thời điểm chốt range (phải == t_known hoặc sau)
range_age           # số nến kể từ t_zero
sigma               # VALID | REFINED | REPLACED | INVALIDATED | SUSPENDED

# ---- SIGNIFICANCE ----
gate_G1, gate_G2, gate_G3
S_L, S_D, S_R, S_P, S_C      # từng chiều, KHÔNG lưu tổng có trọng số
gate_strength                # A/B/C/D/F theo §29.2
disp_h, disp_l               # disp của leg từ mỗi neo
reaction_trend               # tăng | phẳng | giảm
n_tests_h, n_tests_l
max_penetration_atr
tf_stack
round_number

# ---- CẤU TRÚC ----
structure_state     # trend-continuation | pullback | transition | reversal | balance
internal_structure  # bullish | bearish | ranged
external_structure  # bullish | bearish | ranged
htf_alignment       # thuận | trung tính | nghịch
protected_level     # giá của protected swing liên quan
protected_depth_atr
last_bos_tf, last_bos_direction
mss_present, mss_tf

# ---- VỊ TRÍ ----
price_at_known
pd                  # (p-l)/(h-l)
quadrant            # deep_discount | discount | premium | deep_premium
pd_htf, pd_ltf      # alignment
nested_conflict     # true/false
fragility_stable    # kết luận P/D có bền khi đổi neo? (fragility test)
pd_alt              # pd với neo thay thế

# ---- LIQUIDITY & DOL ----
unswept_count       # 0 | 1 | 2
dol_price, dol_type, dol_tier        # IRL | ERL
dol_evidence        # pendulum | structure | multitf | reach (đếm số cái có)
dol_conflict        # true/false
distance_to_dol_atr
inducement_price    # nếu có

# ---- EXECUTION (chỉ khi có vào lệnh) ----
killzone            # LONDON | NY_AM | NY_PM | ASIA | NONE
entry_price, stop_price, target_price
r_planned
sweep_present, displacement_present, fvg_valid
entry_inside_pd_half        # entry có đúng nửa range cho hướng?
anchor_type_for_fib         # DR-1 hay DR-4 (chống lỗi §3.1)
news_driven
news_window

# ---- OUTCOME ----
t_entry, t_exit, exit_reason
result_binary       # 1 nếu +kR trước -1R, else 0
r_multiple          # kết quả thực tế
mae_r, mfe_r        # để phân tích, không chỉ nhị phân
bars_held
invalidation_occurred, invalidation_type, t_inval
```

### 31.3. Ghi nhãn outcome — double barrier và vì sao không dùng P&L thật

**Vì sao double barrier thay vì P&L:** P&L trộn ba thứ khác nhau — chất lượng của *phân tích*, chất lượng của *quản trị rủi ro*, và *may mắn*. Nếu bạn đang nghiên cứu **range selection**, biến phụ thuộc phải cô lập được ảnh hưởng của việc chọn range. Double barrier chuẩn hoá theo rủi ro và loại bỏ quyết định dời stop/dời target.

```text
Với mỗi mẫu (range hợp lệ tại t_known):
  Nếu KHÔNG có entry (vì giá ở EQ, hoặc thiếu DOL, hoặc ngoài killzone):
     → vẫn ghi nhãn "counterfactual": giá chạm +kR hay -1R trước?
     (Đây là mẫu quan trọng NHẤT, và cũng là mẫu hầu hết trader bỏ qua.)
  Nếu CÓ entry:
     → ghi cả nhãn double-barrier VÀ r_multiple thực tế
  Luôn ghi MAE/MFE để biết "đúng nhưng đi ngược trước" chiếm bao nhiêu
```

### 31.4. Metrics — bảy nhóm và câu hỏi chúng trả lời

| # | Nhóm metric | Cụ thể | Trả lời câu hỏi |
|---|---|---|---|
| 1 | **Expectancy** | `E[R] = winrate × avg_win_R − (1−winrate) × avg_loss_R` | Chiến lược có dương kỳ vọng không? |
| 2 | **Win rate & R phân phối** | winrate, `avg_R`, độ lệch chuẩn R, phân vị 5%/95% | Phân phối có đuôi dày không? (quan trọng cho drawdown) |
| 3 | **MAE / MFE** | trung bình và phân phối | Bao nhiêu % lệnh "đúng nhưng bị stop trước"? → thông tin để đặt stop |
| 4 | **Drawdown** | max DD, DD trung bình, thời gian hồi phục | Có sống được không? |
| 5 | **Conditional expectancy** | `E[R]` theo nhóm: `gate_strength`, `pd` bucket, `unswept_count`, `htf_alignment`, `killzone` | Điều kiện nào thực sự tạo khác biệt? |
| 6 | **Regime dependency** | `E[R]` theo `atr_regime`, `trend vs range`, `news vs non-news` | Có phải edge chỉ tồn tại ở một regime? |
| 7 | **Sensitivity analysis** | `E[R]` theo `N`, `θ`, `m`, `k` (tham số) | Kết luận có bền theo tham số không? |

> [!warning] Metric quan trọng nhất mà hầu như không ai báo cáo
> **Conditional expectancy theo `gate_strength`** — cụ thể: so `E[R]` của nhóm A/B với nhóm C/D/F. Nếu bốn nhóm này **không** cho kết quả khác nhau, thì **toàn bộ thang điểm significance không mang thông tin** — và bạn đã tiết kiệm được rất nhiều thời gian. Đây là **phép thử rẻ nhất và có tính phá hủy cao nhất** trong cả framework: hãy chạy nó **trước** khi tinh chỉnh bất cứ thứ gì khác.

---

## 32. Hypothesis Testing — 9 giả thuyết có thể kiểm định

> [!info] Cách đọc
> Mỗi giả thuyết có: **phát biểu** → **lý do** → **biến** → **nhóm đối chứng / can thiệp** → **cỡ mẫu** → **biến gây nhiễu** → **kiểu thất bại** → **phép kiểm định**. Cỡ mẫu tính cho α = 0.05, power = 0.80.

### H1 — Range có neo cấu trúc tốt hơn range có neo thị giác
**Phát biểu:** Dealing range được neo bởi swing qua gate G2 cho kết quả context tốt hơn range neo bởi swing "trông lớn".
**Lý do:** G2 là điều kiện duy nhất loại được nhiễu mà không cần tham số (§10.2).
**Biến:** độc lập = `gate_strength` (A/B vs C/D); phụ thuộc = `result_binary`, `mae_r`.
**Đối chứng:** range nhóm C/D. **Can thiệp:** range nhóm A/B.
**Cỡ mẫu:** ~384 mẫu/nhóm nếu so winrate 40% vs 50%.
**Nhiễu:** regime biến động; symbol; killzone; khoảng cách tới DOL.
**Kiểu thất bại:** nếu nhóm A/B luôn có `unswept_count` cao hơn, bạn đang đo **liquidity**, không đo **structure**. → Cần **khớp (match)** hai nhóm theo `unswept_count`.
**Kiểm định:** χ² cho winrate; t-test/Wilcoxon cho `mae_r`; **khuyến nghị**: logistic regression có kiểm soát biến nhiễu.

### H2 — Liquidity significance cải thiện chọn range
**Phát biểu:** Thêm `unswept_count` và `tf_stack` vào tiêu chí chọn range cải thiện expectancy so với chỉ dùng cấu trúc.
**Lý do:** có nền tảng cơ học [B] (§6.1, Osler).
**Biến:** `unswept_count` (0/1/2), `tf_stack` (1/2/3).
**Đối chứng:** mẫu có `unswept_count = 0`. **Can thiệp:** `≥1`.
**Cỡ mẫu:** ~400/nhóm.
**Nhiễu:** range `unswept_count = 0` thường xuất hiện trong trend mạnh (đã tiêu thụ hết) → **tương quan với regime**, đây là nhiễu nguy hiểm nhất.
**Kiểu thất bại:** kết luận "unswept tốt hơn" trong khi thực ra "range/balance tốt hơn trend".
**Kiểm định:** logistic + biến kiểm soát `structure_state`.

### H3 — Displacement significance thông tin hơn biên độ thô
**Phát biểu:** `disp` dự báo kết quả tốt hơn `amp_atr` (biên độ swing).
**Lý do:** `disp` là dấu vết của việc tiêu thụ thanh khoản; biên độ chỉ là kích thước (§10.3).
**Biến:** hai biến độc lập cạnh tranh; phụ thuộc = `result_binary`.
**Đối chứng:** mô hình chỉ có `amp_atr`. **Can thiệp:** mô hình chỉ có `disp` (và mô hình có cả hai).
**Cỡ mẫu:** ~880/nhóm nếu muốn phát hiện khác biệt 0.2R.
**Nhiễu:** `disp` phụ thuộc ATR → **phải dùng ATR trễ** (§28.3-bẫy 1).
**Kiểu thất bại:** hai biến tương quan cao → đa cộng tuyến → hệ số không ổn định.
**Kiểm định:** so AUC out-of-sample giữa hai mô hình; VIF để kiểm tra đa cộng tuyến.

### H4 — Nested ranges tăng độ chính xác execution nhưng tăng overfitting
**Phát biểu:** dùng 3 tầng range cho R:R tốt hơn 1 tầng, **nhưng** khoảng cách in-sample/out-of-sample lớn hơn.
**Lý do:** mỗi tầng thêm một bậc tự do.
**Biến:** `nesting_level` (1/2/3); phụ thuộc = `r_planned`, `result_binary`, và **gap IS/OOS**.
**Đối chứng:** 1 tầng. **Can thiệp:** 3 tầng.
**Cỡ mẫu:** ~400/nhóm + **bắt buộc** tách IS/OOS.
**Nhiễu:** người dùng 3 tầng có thể là người kỹ hơn nói chung (confound về kỹ năng) — không loại được trong dữ liệu cá nhân.
**Kiểu thất bại:** **chính giả thuyết này dự đoán thất bại của nó** — nếu gap IS/OOS lớn, đó là kết quả ủng hộ H4.
**Kiểm định:** so `E[R]` IS vs OOS; nếu `E[R]_IS − E[R]_OOS` lớn hơn ở nhóm 3 tầng → xác nhận.

### H5 — P/D ít giá trị độc lập, có giá trị khi có điều kiện
**Phát biểu:** `pd` một mình không dự báo; `pd` **tương tác** với `htf_alignment` và `dol_evidence` thì có.
**Lý do:** §19.1 (lập luận logic: `pd` là hàm vị trí, không chứa thông tin cung cầu).
**Biến:** `pd` (liên tục), `htf_alignment`, `dol_evidence` (0–4).
**Đối chứng:** mô hình chỉ có `pd`. **Can thiệp:** `pd` + tương tác.
**Cỡ mẫu:** ~600–900 (cần cho số hạng tương tác).
**Nhiễu:** `pd` tương quan với khoảng cách tới DOL → **phải kiểm soát khoảng cách** (§28.3-bẫy 2).
**Kiểu thất bại:** nếu không kiểm soát khoảng cách, `pd` sẽ "có ý nghĩa" giả tạo.
**Kiểm định:** so likelihood-ratio giữa hai mô hình; kiểm tra hệ số tương tác.

### H6 — Body-close khác wick về hệ quả
**Phát biểu:** nhóm "close-through" cho kết quả continuation khác nhóm "wick-through".
**Lý do:** quy ước ICT (§14.4) + cơ chế acceptance.
**Biến:** `break_type ∈ {wick, close, grind, displacement}`.
**Đối chứng:** wick-through. **Can thiệp:** close-through.
**Cỡ mẫu:** ~400/nhóm.
**Nhiễu:** close-through thường xảy ra trong trend mạnh → confound với regime.
**Kiểu thất bại:** định nghĩa `m` (số nến reclaim) thay đổi làm đổi nhóm → **phải cố định `m` trước**.
**Kiểm định:** χ² + phân tích sống sót (survival) cho thời gian tới reclaim.

### H7 — Liquidity significance giảm theo số lần test (mòn)
**Phát biểu:** xác suất xuyên qua neo **tăng** theo `n_tests` khi `reaction_trend = giảm`.
**Lý do:** thanh khoản là hàng tiêu hao (§6.1-CC3).
**Biến:** `n_tests`, `reaction_trend`; phụ thuộc = xuyên qua hay không.
**Đối chứng:** `n_tests ≤ 2`. **Can thiệp:** `n_tests ≥ 3` với trend giảm.
**Cỡ mẫu:** ~300/nhóm (outcome nhị phân, hiệu ứng dự kiến lớn).
**Nhiễu:** vùng test nhiều lần thường là consolidation → confound với `structure_state`.
**Kiểu thất bại:** `reaction_trend` chỉ có 2–4 điểm dữ liệu mỗi neo → **nhiễu đo lường cao**; phải chấp nhận đây là biến yếu.
**Kiểm định:** logistic với `n_tests` là biến liên tục; kiểm tra đơn điệu.

### H8 — Rule "không giao dịch quanh EQ" có cơ sở
**Phát biểu:** các mẫu có `pd ∈ [0.40, 0.60]` cho expectancy thấp hơn có ý nghĩa so với ngoài dải.
**Lý do:** §5.2/§12-Dealing-Range: EQ là vùng "từ chối quyết định"; dải 40–60% là practice rule chưa kiểm chứng.
**Biến:** `pd` bucket; phụ thuộc = `result_binary`, `mae_r` (dự đoán MAE cao hơn).
**Đối chứng:** ngoài dải. **Can thiệp:** trong dải (nếu có vào lệnh).
**Cỡ mẫu:** ~400/nhóm.
**Nhiễu:** trader có thể **đã** tránh dải EQ → thiếu mẫu trong nhóm can thiệp. **Đây là vấn đề thật**: bạn cần nhãn counterfactual (§31.3) để có mẫu.
**Kiểu thất bại:** dải 40–60% là **quy ước** — nếu dùng dải khác (45–55% hay 35–65%) mà kết luận đổi, thì "quy ước" không có cơ sở.
**Kiểm định:** quét `pd` theo bước 0.05 và vẽ đường expectancy — **đây là phép thử đẹp nhất trong 8 giả thuyết**, vì nó không cần chia nhóm nhị phân và cho thấy hình dạng quan hệ.

### H9 — OTE có cải thiện expectancy không? (giả thuyết bổ sung, phát sinh từ §19.6)
**Phát biểu:** entry nằm trong dải OTE 62–79% của leg (DR-4) cho expectancy **không khác** entry nằm ngoài dải, nhưng **cùng** array + cùng vị trí P/D.
**Lý do:** bằng chứng peer-reviewed duy nhất trực tiếp về Fibonacci (Tsinaslanidis et al. 2022) là **phủ định**, và OTE là một cấu trúc tỷ lệ Fibonacci (kể cả hai mức 0.705/0.79 mà bài đó không test).
**Biến:** `entry_in_ote ∈ {0,1}` (đo trên `anchor_type = DR-4`); phụ thuộc = `result_binary`, `mae_r`.
**Đối chứng:** `entry_in_ote = 0` nhưng **vẫn có** array + sweep + MSS + đúng nửa range. **Can thiệp:** `entry_in_ote = 1`.
**Cỡ mẫu:** ~400/nhóm.
**Nhiễu:** entry trong OTE thường **xa hơn** về phía đối diện → có thể có R:R tốt hơn một cách máy móc, không phải vì OTE có sức mạnh. **Phải khớp (match) hai nhóm theo `r_planned`.**
**Kiểu thất bại:** nếu bạn chỉ vào lệnh khi có OTE (thói quen), nhóm đối chứng sẽ rỗng → cần nhãn counterfactual (§31.3).
**Kiểm định:** so `E[R]` có khớp `r_planned`; nếu không khác biệt → **OTE là quy ước chuẩn hoá, không phải edge** (đúng như kết luận tạm ở §19.6).

> [!important] Giả thuyết nào nên chạy trước — thứ tự ưu tiên theo chi phí/lợi ích
> **1) H8** (quét `pd` theo bước — rẻ nhất, và có thể phá hủy một rule bạn đang dùng).
> **2) H1** (gate vs visual — kiểm tra chính luận điểm trung tâm của bài này).
> **3) H6** (wick vs close — kiểm tra quy ước vận hành quan trọng nhất của §14).
> **4) H5** (tương tác P/D — quan trọng nhất về mặt lý thuyết nhưng cần mẫu lớn nhất).
>
> Bốn giả thuyết còn lại (H2, H3, H4, H7) chỉ nên chạy **sau**, vì chúng cần mẫu lớn hơn và có nhiều confound hơn.

---

## 33. Research Limitations — những gì bài này KHÔNG biết

### 33.1. Những gì không thể xác định chỉ từ price

| # | Không xác định được từ chart | Vì sao | Hệ quả cho framework |
|---|---|---|---|
| 1 | **Ý định** của bất kỳ bên nào | Ý định không để lại dấu vết phân biệt được với cung-cầu đơn thuần | Mọi câu [F] phải bị loại khỏi tiền đề quyết định (§6.2) |
| 2 | **Phân bố lệnh chờ** | Không có order book | "Pool", "liquidity", "stop cluster" chỉ là **proxy** (§28.1) |
| 3 | **Khối lượng thật** (FX/CFD) | Tick volume ≠ volume thật | Không dùng volume làm biến định lượng cho FX |
| 4 | **Nhân quả** (sweep → đảo chiều) | Chỉ quan sát được đồng thời, không quan sát được phản thực | Mọi "vì… nên…" trong ICT là [D], không phải [A] |
| 5 | **Ai đang ở phía bên kia lệnh** | Không có dữ liệu định danh | "Smart money" là thuật ngữ mô tả, không phải thực thể quan sát được |
| 6 | **Range "đúng" theo canon** | Không có canon xác minh được (§3.1b) | Phải tự định nghĩa vận hành — đây là **nghĩa vụ**, không phải lựa chọn |
| 7 | **Trạng thái nào sẽ xảy ra** (A/B/C ở §21) | Là câu hỏi về tương lai | Chỉ gán được xác suất tương đối + định cỡ theo đó |

### 33.2. Khoảng trống bằng chứng — trạng thái thật của lĩnh vực này

> [!danger] Sự thật quan trọng nhất của §33
> **Không có một bài bình duyệt (peer-reviewed) nào kiểm định TRỰC TIẾP ICT/SMC** — order block, FVG, liquidity sweep, premium/discount, dealing range — như một chiến lược có edge. Đây là kết quả tra cứu có hệ thống cho bài này, không phải ý kiến.
>
> **Bài gần nhất** là Oukhouya, Aboutabit & Hafidi (2026), *"Risk-Constrained Trade Sizing via Calibrated ML Probabilities and Linear Programming on SMC/ICT-Driven Structural Signals"*, **Informatica** 50:167–180 ([DOI](https://doi.org/10.31449/inf.v50i13.12899)) — đã đọc toàn văn. Bài đó trích xuất các primitive ICT (liquidity sweep, BOS/CHoCH, FVG, order block) từ OHLC H1 làm **feature**, rồi dùng ML + linear programming để định cỡ vị thế trên XAUUSD (dev 1/2023–5/2025: 46.7% net, Sharpe 1.18, MDD 6.8%).
>
> **Và chính bài đó viết ra điều mà tài liệu ICT không muốn nghe:** ICT/SMC *"lack rigorous statistical validation, standardized definitions, or reproducible evaluation protocols"*. Quan trọng hơn: **ablation của họ cho thấy calibration và ràng buộc CVaR mới là yếu tố tạo kết quả — không phải bản thân order block/FVG.** Nghĩa là: ngay cả bài gần nhất, khi tự kiểm tra, cũng **không** chứng minh được các primitive ICT có edge. Một thị trường, một khung thời gian.

**Bốn nguồn "ủng hộ ICT" đang lưu hành, và lý do không dùng được:**

| Nguồn | Vấn đề |
|---|---|
| SSRN 6725880 — "Multi-Asset A/A+ Momentum FVG Strategy" | Tự backtest 2025, 473 lệnh, win rate **78%**, +132.5%/năm — nhưng **một năm lịch duy nhất**, không out-of-sample, không replication, **không bình duyệt** |
| Mahadzva (2026), *"Smart Money or Costly Folklore?"*, SSRN 7430998 | Tiêu đề mang tính phủ định, nhưng **nội dung không truy cập được** (SSRN chặn) → **không được trích nội dung**, dù chỉ để phản bác |
| Sách tự xuất bản, Zenodo DOI 10.5281/zenodo.20073732 | Tự xuất bản, không bình duyệt |
| OSF 10.31219/osf.io/7yw86 | Đã bị **WITHDRAWN** |
| Con số "ICT win rate 75–85%" trong cộng đồng | **Con số vendor.** Không có nguồn học thuật nào |

![[DR-Deep-13-Thang-Bang-Chung-Tai-Lieu.svg|740]]
*Hình 13 — Trạng thái bằng chứng thật của lĩnh vực. Cái CÓ bằng chứng là các thành phần cơ học (clustering lệnh, stop làm trend tăng tốc, depth tại S/R). Cái KHÔNG có bằng chứng là chính khái niệm dealing range — và với Fibonacci thì bằng chứng bình duyệt duy nhất là phủ định.*

### 33.3. Bảng bằng chứng học thuật đã kiểm chứng (dùng được)

| Trích dẫn | Nội dung thực sự | Giới hạn / điều KHÔNG chứng minh | Mức xác minh |
|---|---|---|---|
| **Osler (2003)**, *Journal of Finance* 58(5):1791–1819 — [DOI](https://doi.org/10.1111/1540-6261.00588) · [bản NY Fed SR125 (PDF, đầy đủ số liệu)](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf) | Order book thật của một dealing bank; clustering mạnh ở đuôi `00` (~8.7% vs null ~1%); TP 9.3% vs SL 4.4%; bất đối xứng stop mua (7.4% ở 90–99 vs 14.4% ở 01–10) | **Không** chứng minh S/R sinh lời; giải thích bằng **mô phỏng**; một bank, ba cặp tiền; đo **nơi đặt lệnh**, không đo hành vi giá | Toàn văn PDF (SR125) |
| **Osler (2005)**, *JIMF* 24(2):219–241 — [DOI](https://doi.org/10.1016/j.jimonfin.2004.12.002) | Trend tăng tốc tại cụm stop; phản ứng với stop lớn hơn take-profit; kéo dài hơn | Chính tác giả: ý nghĩa **theo giờ, không theo ngày**. **Không có** con số tần suất cascade nào (con số lưu hành trên mạng không có nguồn) | Abstract xác minh |
| **Kavajecz & Odders-White (2004)**, *RFS* 17(4):1043–1071 — [DOI](https://doi.org/10.1093/rfs/hhg057) | Mức S/R trùng **đỉnh depth** trên limit order book NYSE | Khung diễn giải là **market efficiency**: TA nói về **cung thanh khoản**, không về hướng giá. Dữ liệu thời kỳ specialist | Abstract xác minh |
| **Brock, Lakonishok & LeBaron (1992)**, *JF* 47(5):1731–1764 — [DOI](https://doi.org/10.1111/j.1540-6261.1992.tb04681.x) | 26 rule MA/range-break trên DJIA 1897–1986, bootstrap: buy > sell | In-sample, **không** điều chỉnh data-snooping, không transaction cost. **Không** test mức S/R như một mức giá | Đã xác minh |
| **Sullivan, Timmermann & White (1999)**, *JF* 54(5):1647–1691 — [DOI](https://doi.org/10.1111/0022-1082.00163) | Mở rộng universe rule của Brock et al., hiệu chỉnh data-snooping | Kết luận: hiệu suất vượt trội của rule tốt nhất **mất ý nghĩa thống kê**. ⚠️ **Luôn phải trích kèm Brock et al.** — trích Brock một mình là trích dẫn gây hiểu sai | Abstract xác minh |
| **Lo, Mamaysky & Wang (2000)**, *JF* 55(4):1705–1765 — [DOI](https://doi.org/10.1111/0022-1082.00265) | Nhận dạng mẫu tự động bằng kernel regression; mẫu cổ phiếu Mỹ 1962–1996 | Kết luận thật: vài chỉ báo cho **"incremental information"**; họ **dừng lại trước khi** khẳng định có rule sinh lời. Không test S/R | Abstract xác minh |
| **Park & Irwin (2007)**, *J. Economic Surveys* 21(4):786–826 — [DOI](https://doi.org/10.1111/j.1467-6419.2007.00519.x) | Khảo sát 95 modern study: **56 dương / 20 âm / 19 hỗn hợp** | Chính abstract nêu hầu hết mắc **data snooping, chọn rule ex post, khó ước lượng risk & cost**. ⚠️ **56/95 KHÔNG được đọc là "59% chứng minh TA hiệu quả"** | Đã xác minh |
| **Menkhoff & Taylor (2007)**, *JEL* 45(4):936–972 — [DOI](https://doi.org/10.1257/jel.45.4.936) | TA **phổ biến rộng** trong FX chuyên nghiệp; "may be profitable"; giải thích khả dĩ nhất là ảnh hưởng **phi-cơ-bản (order flow)** | Chứng minh professional **dùng** TA — **không** chứng minh TA có edge bền vững | Đã xác minh |
| **Tsinaslanidis, Guijarro & Voukelatos (2022)**, *ESWA* 187:115893 — [DOI](https://doi.org/10.1016/j.eswa.2021.115893) | Test Fibonacci trực tiếp: giá bounce ở mức Fib **ngang bằng** mức không-Fib; rule Fib **thất bại** so với mức chọn ngẫu nhiên | 3 thị trường cổ phiếu; test 23.6/38.2/61.8/100% — **không** test 0.705/0.79 của OTE | Toàn văn PDF |
| **Batchelor & Ramyar (2006)**, *Magic numbers in the Dow* — [bản mở](https://openaccess.city.ac.uk/id/eprint/16276/) | DJIA 1914–2002, 430 turning point, 16 tỷ lệ, bootstrap + KS | **KHÔNG peer-reviewed** (discussion paper). Kết luận: các tỷ lệ "có ý nghĩa" **không nhiều hơn mức ngẫu nhiên kỳ vọng**. Test **tỷ lệ giữa các trend**, không test bounce tại một mức vẽ trên chart | Toàn văn PDF |
| **Shanaev & Gibson (2022)**, SSRN 4212430 — [DOI](https://doi.org/10.2139/ssrn.4212430) | Kết quả **ngược lại**: Fibonacci có ý nghĩa trên index/FX; mức quan trọng gồm 0.0/38.1/**50.0**/61.2/100% | ⚠️ **Preprint, KHÔNG bình duyệt**; mâu thuẫn trực tiếp với Tsinaslanidis et al. | Abstract xác minh |
| **Niederhoffer (1965)**, *Operations Research* 13(2):258–265 — [DOI](https://doi.org/10.1287/opre.13.2.258) | Sổ specialist: lệnh tập trung ở số quen thuộc; giá thấp "settle at round numbers" | Kỷ nguyên NYSE theo 1/8, mẫu nhỏ, không kiểm định hiện đại | Abstract xác minh |
| **De Grauwe & Decupere (1992)**, CEPR DP 621 — [link](https://econpapers.repec.org/paper/cprceprdp/621.htm) | Rào cản tâm lý **tồn tại và có ý nghĩa ở USD/JPY**; giá tăng tốc khi vượt mức tròn | Với **USD/DM thì "less clear-cut"**. Không phải kết quả lợi nhuận | Abstract xác minh |
| **Tversky & Kahneman (1974)**, *Science* 185:1124–1131 — [DOI](https://doi.org/10.1126/science.185.4157.1124) | Heuristic "adjustment from an anchor" trong ước lượng số | Thí nghiệm **trong lab, không có dữ liệu giá, không có giao dịch**. Áp sang mức giá là **suy diễn**, không phải phát hiện của bài | Đã xác minh |
| **Odean (1998)**, *JF* 53(5):1775–1798 — [DOI](https://doi.org/10.1111/0022-1082.00072) | 10.000 tài khoản: nhà đầu tư hiện thực hoá lãi sớm hơn lỗ | Nói về **giá vốn của chính nhà đầu tư**, **không** về mức giá cũ trên thị trường. **Không** test phản ứng giá tại đỉnh/đáy cũ. Bổ sung: Ben-David & Hirshleifer (2012) không thấy bằng chứng rõ; Feng & Seasholes (2005) cho thấy kinh nghiệm **loại bỏ** phần lớn hiệu ứng | Đã xác minh |
| **Guillaume et al. (1997)**, *Finance & Stochastics* 1:95–129 — [DOI](https://doi.org/10.1007/s007800050018) và **Adegboye et al. (2022)**, *AI Review* — [DOI](https://doi.org/10.1007/s10462-022-10307-0) | Nền tảng **intrinsic time / Directional Change** cho định nghĩa swing có ngưỡng; tỉ lệ DCT có overshoot chỉ 14.77–52.46% | Chi tiết đầy đủ ở [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]; **chưa kiểm chứng trên NQ/XAU/D1-H1-M5** | Kế thừa từ note 54 |

### 33.4. Những hạn chế của chính bài này

Nói thẳng về bài bạn đang đọc:

1. **Sáu case study là tổng hợp (synthetic).** Chúng minh hoạ **quy trình**, không chứng minh **hiệu quả**. Không có case nào là bằng chứng cho bất kỳ mệnh đề nào về edge.
2. **Mọi con số ngưỡng không có nguồn đều là `practice number`**: `disp ≥ 1.0`, `n_tests ≤ 2`, `m` nến reclaim, dải EQ 40–60%, `range_height > 1.5 × ADR`, "≥3/5 điều kiện range con", `~0.1 ATR` cho gộp cụm. **Chưa cái nào được kiểm định.**
3. **Thang điểm `S`/`Q` chưa có trọng số** — và tôi từ chối bịa. Tầng 2 (gate-based) là phần duy nhất của framework này đứng vững mà không cần dữ liệu, vì nó không ước lượng tham số.
4. **Không lấy được artifact sơ cấp nào của ICT.** Mọi phát biểu về "ICT nói gì" trong bài (và trong toàn bộ tài liệu ICT mà bạn đọc) đều ở mức **gián tiếp qua nguồn thứ cấp** (§3.1b).
5. **Research vault của bạn đã bị reset về 1 note** trong quá trình làm bài này — các note nguồn mà [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] và [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] trích dẫn (`351236996pdf`, `ict-draw-on-liquidity-dol-picking-the-target`…) **không còn tồn tại** để tra lại. Các kết luận kế thừa từ hai note đó vì vậy **không thể audit lại** ở thời điểm này. Đây là một **hạn chế thật của bài**, không phải chi tiết kỹ thuật.
6. **Không có phần nào của bài này được kiểm chứng bằng dữ liệu của bạn.** Tất cả đang ở tầng [D]/[E].

7. **Một caveat về chuỗi truy xuất của số liệu Osler.** Các con số cụ thể ở §6.1 và §33.3 (8.7% · 9.3% vs 4.4% · 7.4% vs 14.4%) được đọc từ **toàn văn PDF** của NY Fed Staff Report 125 (link có trong bảng §33.3) — **không** có trong trang abstract, và **không** có trong note nguồn lưu tại `research/notes/` (note đó chỉ chứa phần abstract). Nghĩa là: nếu bạn muốn audit các con số này, phải mở **PDF gốc**, không kiểm được bằng note nguồn trong vault. Đây là giới hạn thật của chuỗi bằng chứng, và tôi ghi ra thay vì để nó ẩn.

### 33.5. Bằng chứng nào sẽ thay đổi kết luận của bài này

Nói trước điều kiện bác bỏ (đây là điều kiện để bài này **có thể sai** — và do đó có giá trị):

| Nếu điều này xuất hiện | Thì kết luận nào của bài sẽ phải sửa |
|---|---|
| `E[R]` của nhóm `gate_strength = A/B` **không** khác nhóm C/D (§31.4) | Toàn bộ §10 (swing significance) mất giá trị thực tiễn → rút gọn về §11 (phân cấp) + §14 (validity) |
| Nhóm "close-through" và "wick-through" cho kết quả **giống nhau** (H6) | Quy ước §14.4 (body-close mới invalidate) là **quy ước rỗng** → phải bỏ rule phân biệt |
| Đường expectancy theo `pd` **phẳng** (H8) | Premium/discount vẫn là khung chuẩn hoá nhưng **không** được dùng như điều kiện lọc setup |
| `pd` tương tác với HTF/DOL **không** cải thiện mô hình (H5) | §19 phải hạ xuống thuần **descriptive**; bỏ rule "5 biến" |
| Test Fibonacci độc lập trên NQ/FX/H1 **xác nhận** có ý nghĩa (lặp lại được kết quả Shanaev & Gibson ở dạng bình duyệt) | §19.6 phải sửa: OTE có cơ sở, không chỉ là quy ước |
| Tìm được **transcript sơ cấp** của ICT định nghĩa dealing range và quy tắc chọn swing | §3.1b và §33.4-điểm 4 phải sửa; có thể xuất hiện một định nghĩa canon thật |
| Một bài peer-reviewed kiểm định ICT/SMC với kết quả **dương** và tái lập được | §33.2 phải sửa toàn bộ |

---

## 34. Final Mental Model — mô hình tinh thần cuối cùng

### 34.1. Bản đồ khái niệm (input → output, và chỗ nào là vòng lặp)

```text
[INPUT: dữ liệu OHLC + thời gian + lịch tin]
        │
        ▼
(1) PHÁT HIỆN SWING  ──────────────► tham số hoá: N / θ (ATR trễ)
        │                             ⚠ đây là LỰA CHỌN, không phải khám phá
        ▼
(2) PHÂN CẤP SWING  ───────────────► "phá nó làm mất hiệu lực kết luận nào?" (đệ quy)
        │
        ▼
(3) GATE  G1 xác nhận · G2 cấu trúc · G3 đúng cấp      ◄── CỔNG CỨNG, không bù trừ
        │
        ▼
(4) ĐO 4 CHIỀU:  L (liquidity) · D (displacement) · R (reaction) · P (protected)
        │            C (context) = CHỈ xác nhận, KHÔNG chọn
        ▼
(5) SINH RANGE ỨNG VIÊN  ──────────► nhiều ứng viên là BÌNH THƯỜNG
        │
        ▼
(6) CHỌN PRIMARY  ─────────────────► thứ tự từ điển (không phải tổng có trọng số)
        │                             khoá 1 gate-strength → 2 unswept → 3 containment
        │                             → 4 score → 5 age (tuổi CHỈ ở đây)
        ▼
(7) VALIDITY (A1-A4) + STATE MACHINE ──► VALID | REFINED | REPLACED | INVALIDATED | SUSPENDED
        │                                 (wick KHÔNG BAO GIỜ invalidate)
        ▼
(8) VỊ TRÍ:  pd = (p−l)/(h−l)  ────► quadrant + FRAGILITY TEST (đổi neo, kết luận có lật?)
        │                             ⛔ pd KHÔNG phải tín hiệu hướng
        ▼
(9) BẢN ĐỒ LIQUIDITY  ─────────────► vai trò pool PHỤ THUỘC vị trí giá (draw ↔ fuel)
        │
        ▼
(10) DOL  ─────────────────────────► bằng chứng ĐỘC LẬP với range (con lắc, cấu trúc, liên khung, reach)
        │                             ⛔ chặn vòng lặp: range chốt ở t₀, DOL ở t₁ > t₀
        ▼
(11) PHÂN LOẠI MOVE  ──────────────► A continuation | B pullback | C internal reversal
        │                             D intermediate | E external reversal
        │                             (gán XÁC SUẤT, không gán sự thật)
        ▼
(12) QUYẾT ĐỊNH RANGE  ────────────► KEEP | REFINE | REPLACE | INVALIDATE  (+ CASCADE xuống khung nhỏ)
        │
        ▼
(13) H1:  vùng POI  ───────────────► HTF quyết HƯỚNG · LTF quyết THỜI ĐIỂM
        │
        ▼
(14) M5:  sweep → MSS → displacement → FVG → entry/SL/target
        │      (trong killzone, R:R ≥ kế hoạch, SL ngoài cấu trúc)
        ▼
[OUTPUT: trạng thái có cấu trúc + quyết định + LOG có timestamp]

VÒNG LẶP CẦN CHẶN:
  Range ──► DOL ──► "range đúng vì hướng về DOL" ──► Range     ← ĐÂY LÀ VÒNG LẶP CHẾT NGƯỜI
  Cách chặn duy nhất: TIMESTAMP + BẰNG CHỨNG ĐỘC LẬP (§18.3)
```

### 34.2. Sáu bất biến (nếu chỉ nhớ 6 điều, nhớ 6 điều này)

1. **Range là khung tham chiếu, không phải tín hiệu.** `pd` cho biết *ở đâu*, không cho biết *đi đâu*.
2. **Structural significance ≠ visual size.** Gate G2 trước, xếp hạng sau.
3. **Wick không phá range; body-close mới phá.** Và `SUSPENDED` là một trạng thái hợp lệ.
4. **Range validity ≠ directional thesis.** Hai biến khác nhau; gộp chúng là nguồn gốc của việc đảo bias ở đáy pullback.
5. **Vòng lặp range ↔ DOL là có thật.** Chặn bằng timestamp + bằng chứng độc lập, không bằng cách "cẩn thận hơn".
6. **Không có định nghĩa canon.** Nghĩa vụ của bạn là **viết ra định nghĩa vận hành của mình** và ghi nó vào log — nếu không, bạn không thể học được gì từ dữ liệu của chính mình.

### 34.3. Một câu tóm tắt (dùng để tự nhắc)

> **"Chọn neo bằng cấu trúc, không bằng mắt. Chốt range trước, đo vị trí, rồi mới tìm DOL — và luôn viết ra điều kiện mình sẽ sai."**

---

## 35. Practical Checklist

### A. Pre-session (trước phiên, 10–15 phút)

- [ ] **Bước 0 — Bản đồ trước, khung nhỏ sau.** Mark PWH/PWL, PDH/PDL, ARH/ARL, EQH/EQL, mức tròn. **Chưa** nhìn M5.
- [ ] **Cấu trúc HTF rõ chưa?** (HH/HL | LH/LL | balance). Balance → **no-trade**, dừng ở đây.
- [ ] **Chạy thuật toán phát hiện swing** với tham số của khung (không dùng tham số M5 cho D1).
- [ ] **Chạy gate G1/G2/G3 trên TOÀN BỘ swing phát hiện được** — không chỉ trên những swing tôi "để ý".
- [ ] **Sinh ≥2 range ứng viên** và ghi **cả hai** `(h, l, EQ, pd)`.
- [ ] **Fragility test:** đổi neo ±1 bậc, kết luận P/D có lật không? Lật → cẩn trọng hoặc no-trade.
- [ ] **Ghi `t₀`** cho range PRIMARY (giờ:phút).
- [ ] **Xác định DOL bằng bằng chứng độc lập:** (a) bên nào vừa bị ăn? (b) BOS/MSS gần nhất hướng nào? (c) pool nào nhiều khung cùng tham chiếu? (d) có khả thi trong phiên không?
- [ ] **Ghi invalidation cụ thể:** giá đóng ở đâu, trong bao nhiêu nến → range chết.
- [ ] **Ghi Judas target** (pool ngược hướng DOL) — nếu không viết được → no-trade.
- [ ] **Kiểm lịch tin** trong window dự kiến vào lệnh.

### B. Pre-trade (ngay trước khi bấm)

- [ ] `pd` **ngoài** dải 0.40–0.60 (không giao dịch quanh EQ).
- [ ] Entry nằm **tại một array** (FVG/OB), không phải "trong vùng discount" nói chung.
- [ ] `pd_htf` và `pd_ltf` **không xung đột** (hoặc nếu xung đột → size 50% / bỏ).
- [ ] Hướng lệnh **khớp hướng range**, không chỉ khớp `pd`.
- [ ] **≥3/5 điều kiện** nếu dùng range con (§16.2-Q3).
- [ ] Có **sweep** + **MSS** + **displacement** + **FVG** (đủ 4, không thiếu cái nào).
- [ ] Trong **killzone**.
- [ ] R:R tới DOL **≥ kế hoạch** (và ≥ 2R nếu là setup mới).
- [ ] Ghi `anchor_type ∈ {DR-1, DR-4}` cho mọi phép đo fib (chống lỗi trộn khung).
- [ ] **`t₀ < t_entry`** — range được chốt trước, không phải vẽ lại bây giờ.
- [ ] Không có câu nào trong luận điểm có chủ ngữ "họ/smart money" + động từ ý định.

### C. Post-trade (sau khi lệnh đóng)

- [ ] Ghi `sigma` của range tại thời điểm vào và tại thời điểm đóng.
- [ ] Ghi `invalidation_occurred` + `invalidation_type` + `t_inval` **kể cả khi lệnh thắng**.
- [ ] Ghi `mae_r` / `mfe_r` (không chỉ kết quả).
- [ ] Nếu range bị REPLACED trong lúc lệnh chạy → ghi rõ, và đánh giá xem có phải tôi đã bỏ qua tín hiệu.
- [ ] Nếu thua: phân loại nguyên nhân vào **một trong bốn** — (a) range chọn sai, (b) range đúng nhưng thời điểm sai, (c) quy trình đúng nhưng xác suất, (d) vi phạm quy trình. **(c) không phải lỗi — đừng "sửa" nó.**
- [ ] Nếu thắng: hỏi ngược *"quy trình có đúng không, hay chỉ là may?"* — **thắng do vi phạm quy trình phải bị ghi là lỗi.**

---

## 36. One-Page Dealing Range Rules

> **Thẻ 1 trang — in ra dán màn hình.** Mỗi rule có nhãn loại: `[ICT]` quy ước ICT · `[HEUR]` heuristic chưa kiểm chứng · `[TEST]` rule có thể kiểm định được · `[LOGIC]` hệ quả logic, không cần kiểm định.

```text
════════════════════════════════════════════════════════════════════
  DEALING RANGE — 1 TRANG
════════════════════════════════════════════════════════════════════

A. CHỌN NEO
 1. Neo phải là swing ĐÃ XÁC NHẬN (không phải đáy nến đang chạy).      [LOGIC]
 2. Gate G2 trước tiên: "phá nó có đổi nhãn cấu trúc nào không?"
    Không → LOẠI, bất kể swing to đến đâu.                              [LOGIC]
 3. Neo phải ĐÚNG CẤP của khung đang phân tích.                          [LOGIC]
 4. Chạy gate trên TOÀN BỘ swing do thuật toán tìm được — không chỉ
    trên swing tôi nhìn thấy.                                           [TEST]
 5. Range không thể mạnh hơn NEO YẾU NHẤT của nó.                        [LOGIC]

B. ĐO
 6. pd = (p−l)/(h−l). Không có range → không có pd.                      [LOGIC]
 7. Wick KHÔNG BAO GIỜ invalidate range. Chỉ body-close mới invalidate.   [ICT]
 8. Mọi phép đo fib phải ghi anchor_type: DR-1 (range) hay DR-4 (leg).    [LOGIC]
 9. Luôn chạy FRAGILITY TEST: đổi neo, kết luận P/D có lật không?         [TEST]

C. DÙNG
10. pd là KHUNG VỊ TRÍ, không phải tín hiệu hướng.                       [LOGIC]
11. Discount chỉ có nghĩa bullish khi: hướng range TĂNG + DOL ở trên +
    có array tại chỗ. Thiếu 2/3 → không giao dịch.                       [HEUR]
12. Không giao dịch khi pd ∈ [0.40, 0.60].                               [HEUR]
13. Vai trò của một pool phụ thuộc VỊ TRÍ GIÁ: cùng một đỉnh có thể là
    draw (giá ở discount) hoặc fuel (giá ở premium).                     [LOGIC]
14. DOL phải có BẰNG CHỨNG ĐỘC LẬP với range. Không viết được DOL kèm
    giá cụ thể → NO-TRADE.                                               [LOGIC]

D. XỬ LÝ SỰ KIỆN
15. Bốn trạng thái, không phải hai: VALID / REFINED / REPLACED /
    INVALIDATED. Thêm SUSPENDED khi chưa đủ dữ liệu để phán.             [LOGIC]
16. REPLACED ≠ INVALIDATED. Bị thay thế là vận hành bình thường.         [LOGIC]
17. Internal MSS KHÔNG BAO GIỜ là lý do đổi bias.                        [LOGIC]
18. MSS ở khung nào chỉ có hiệu lực ở khung đó.                          [LOGIC]
19. Sweep KHÔNG hứa đảo chiều. Sweep → continuation là kết cục THƯỜNG
    GẶP HƠN. Đòi reclaim + MSS + displacement mới tin là đảo.             [TEST]
20. Đổi cách đọc HTF chỉ khi hội đủ 4 điều kiện §21.2-Q12.                [LOGIC]

E. CHỐNG TỰ LỪA
21. Range phải được chốt TRƯỚC sự kiện, có timestamp t₀.                 [LOGIC]
22. Chạy ≥2 range ứng viên và ghi CẢ HAI pd.                             [TEST]
23. Câu nào có "họ/smart money" + động từ ý định → đó là NARRATIVE,
    không được làm tiền đề cho size.                                     [LOGIC]
24. "Bên nào vừa bị ăn?" là câu hỏi quan trọng hơn "có bao nhiêu pool?"  [TEST]
25. Thắng do vi phạm quy trình phải ghi là LỖI.                          [LOGIC]

F. BIẾT GIỚI HẠN CỦA MÌNH
26. Không có định nghĩa canon cho "dealing range" — kể cả nguồn gốc
    cũng không xác minh được ở mức sơ cấp. Viết định nghĩa của bạn ra.    [A]
27. Không có bằng chứng bình duyệt nào cho ICT/SMC. Bằng chứng peer-
    reviewed duy nhất về Fibonacci là PHỦ ĐỊNH.                          [A]
28. Trọng số của thang điểm CHƯA BIẾT. Dùng tầng gate, không dùng tầng
    trọng số, cho tới khi có ≥ ~880 mẫu/nhóm.                            [A]
════════════════════════════════════════════════════════════════════
```

---

## Nguồn tham chiếu

### Bằng chứng học thuật (đã kiểm chứng cho bài này)
Xem bảng đầy đủ ở **§33.3**. Các mục then chốt: Osler 2003 (*JF*) · Osler 2005 (*JIMF*) · Kavajecz & Odders-White 2004 (*RFS*) · Brock et al. 1992 + Sullivan et al. 1999 (*JF*) · Lo, Mamaysky & Wang 2000 (*JF*) · Park & Irwin 2007 (*JES*) · Menkhoff & Taylor 2007 (*JEL*) · Tsinaslanidis et al. 2022 (*ESWA*) · Batchelor & Ramyar 2006 · Niederhoffer 1965 · De Grauwe & Decupere 1992 · Tversky & Kahneman 1974 · Odean 1998 · Oukhouya et al. 2026 (*Informatica*).

### Nguồn về định nghĩa & quy ước ICT (đều là **thứ cấp** — xem §3.1b)
Xem bảng ở **§3.1b**. Các mục chính: [ictsharks — 2022 ICT Mentorship: Dealing Ranges](https://forum.ictsharks.com/t/2022-ict-mentorship-dealing-ranges/511) · [ictkillzone — Dealing Range](https://www.ictkillzone.com/ict-dealing-range) · [ictkillzone — Swing Point Hierarchy](https://www.ictkillzone.com/ict-swing-point-hierarchy) · [ictkillzone — IPDA](https://www.ictkillzone.com/ict-ipda) · [bestprops — Ep.19](https://bestprops.com/2022-ict-mentorship-episode-19/) · [bestprops — IPDA vs Wyckoff](https://bestprops.com/ict-ipda-vs-wyckoff-theory/) · [ICT Flow, lesson 17](https://ictflow.com/lesson/17) · [Backtrex — IPDA data range](https://backtrex.com/en/blog/ict-dealing-range-ipda-data-range-guide) · [TradingView — ICT Dealing Range Lite](https://br.tradingview.com/script/UdCtGrfF-ICT-Dealing-Range-Lite-fadi/) · [TradingView — ICT Dealing Range của EmpArchitect](https://www.tradingview.com/script/q6O0kR6a-ICT-Dealing-Range-EmpArchitect/) · [BrokerChampion — phê phán](https://brokerchampion.com/order-block-trading).

> [!note] Ghi chú về nguồn
> Toàn bộ nội dung web ở trên đã được đọc như **dữ liệu**, không phải chỉ thị. Không có phát biểu nào trong các trang đó được thực thi. Các nguồn thứ cấp được ghi nhãn rõ vì chúng **không thể** dùng làm bằng chứng cho định nghĩa canon (§33.4-điểm 4).

---

## Liên kết

**Tiên quyết:** [[12-Dealing-Range]] · [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]] · [[27-Premium-Discount]] · [[05-BOS-Break-of-Structure]] · [[21-Market-Structure-Shift]]

**Liên quan trực tiếp (đọc theo thứ tự này):**
[[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] (swing nào có hiệu lực, Judas fuel vs DOL) → [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] (biến swing thành hàm của dữ liệu + tham số) → [[37-Re-mapping-Dealing-Range-sau-Displacement]] (re-map & cascade) → [[16-Internal-External-Range-Liquidity-IRL-ERL]] (chu kỳ ERL↔IRL) → [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] và [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] (DOL ontology + failure model) → [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]] (cùng phương pháp, áp cho OB)

**Vận hành:** [[59-Daily-Bias]] · [[18-Kill-Zones]] · [[26-OTE-Optimal-Trade-Entry]] · [[13-FVG-Fair-Value-Gap]] · [[17-Inverse-Fair-Value-Gap-iFVG]] · [[20-Liquidity-Sweep]] · [[41-Change-in-State-of-Delivery]] · [[08-Central-Bank-Dealers-Range]] · [[31-Standard-Deviation]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]]

**Model:** [[01 - ICT 2022 Model]] · [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]] · [[04 - Market Maker Buy Model MMBM]] · [[06 - Market Maker Sell Model MMSM]]

---

## Action items

**Tuần 1 — dựng hạ tầng đo (không cần trade)**
- [ ] Viết hàm phát hiện swing (N-bar pivot N=3 và N=5; DC threshold `θ = k × ATR_trễ`, `k ∈ {0.3, 0.5, 1.0}`) cho D1/H1/M5 — dùng lại code từ [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]
- [ ] Đối chiếu: 20 lệnh gần nhất trong vault — neo tôi **đã** chọn bằng mắt có qua gate G1/G2/G3 không? Đo tỉ lệ khớp
- [ ] Đo `pd` của 20 lệnh đó; có bao nhiêu lệnh vào khi `pd ∈ [0.40, 0.60]`?

**Tuần 2 — chạy phép thử rẻ nhất và có tính phá hủy cao nhất**
- [ ] **H8:** quét `pd` theo bước 0.05 trên toàn bộ mẫu (kể cả lần không vào lệnh) và vẽ đường expectancy. Đây là phép thử **đầu tiên** nên chạy
- [ ] **Fragility test trên 20 lệnh cũ:** đổi neo ±1 bậc, có bao nhiêu lệnh bị **lật** kết luận P/D? (con số này cho biết độ tin cậy của chính phân tích cũ)

**Tuần 3–4 — chạy H1/H6**
- [ ] Thêm `gate_strength ∈ {A,B,C,D,F}` vào frontmatter backtest; so `E[R]` giữa các nhóm
- [ ] Thêm `break_type ∈ {wick, close, grind, displacement}`; so kết quả continuation giữa `wick` và `close` (H6)
- [ ] Thêm `entry_in_ote ∈ {0,1}` và `anchor_type` — chuẩn bị cho H9 (OTE)

**Bắt buộc trước khi tin bất cứ kết quả nào**
- [ ] Kiểm tra **không look-ahead**: chạy lại cùng một thời điểm với dữ liệu bị cắt ngắn — output phải **giống hệt**
- [ ] Chia in-sample / out-of-sample **theo thời gian** trước khi thử bất cứ tham số nào
- [ ] Đếm và ghi lại **số lần thử** — mỗi lần thử một biến là một bậc tự do đã tiêu

**Việc học thuật (khi có thời gian)**
- [ ] Tìm **transcript sơ cấp** của ICT 2022 Mentorship cho các buổi về dealing range — để trả lời câu hỏi §3.1b ở mức sơ cấp
- [ ] Đọc toàn văn Tsinaslanidis et al. (2022) và tự kiểm tra xem kết luận phủ định có áp được sang OTE 0.705/0.79 không (bài gốc **không** test hai mức này)

> [!warning] Curation debt của research vault
> Bài này tạo **11 note nguồn mới** trong `research/notes/` (tag `dealing-range`), tất cả đang ở trạng thái `draft`, chưa có summary. Cần chạy curation pass: `note update <id> --summary … --add-tag …`, rồi `lint`, `repair`, `sources score`, `graph rank`. Vault cũng đã bị reset về **1 note** trong quá trình làm bài — các trích dẫn note-id trong [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] và [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] hiện **không còn tra được**.

