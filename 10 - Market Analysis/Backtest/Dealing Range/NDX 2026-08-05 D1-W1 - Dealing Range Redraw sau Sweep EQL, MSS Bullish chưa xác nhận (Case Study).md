---
type: case-study
instrument: NDX (US Tech 100)
timeframes: [W1, D1]
date_range: 2026-08-04 → 2026-08-05
mode: LIVE
status: OPEN — chờ MSS tại 29,865.3
related: "[[2026-08-04-NDX-D1-bias-multiagent-review]]"
tags: [ict, dealing-range, sweep, mss, devils-advocate, ndx, backtest]
---
![[Pasted image 20260806064215.png]]

![[Pasted image 20260806064221.png]]
# NDX (US Tech 100) — D1/W1 Dealing Range Redraw & Sweep EQL — Case Study

> Tổng hợp toàn bộ discussion trong session (câu hỏi quy tắc redraw dealing range → áp dụng vào case NDX đang live), bổ sung phân tích doctrine sâu hơn và một pha phản biện chuyên sâu (devil's-advocate) cho các claim — bao gồm cả claim của chính mentor. Nối tiếp `2026-08-04-NDX-D1-bias-multiagent-review` (lưu trong Project "Market Analysis").

## 1. Câu hỏi gốc & bối cảnh

Câu hỏi khởi điểm: dealing range D1 cũ (30,771.6–28,215.9) bị phá xuống dưới low 27/7–30/7/2026, sau đó giá reclaim lại bên trong range cũ, quan sát trên W1 giống một liquidity sweep. Câu hỏi cốt lõi: **quy tắc gì để biết dealing range cũ còn hợp lệ hay đã cần redraw?**

Đây là lần thứ hai case NDX với cùng cặp số 30,771.6 / 28,215.9 được đưa ra kiểm định — lần đầu là multi-agent review ngày 04/08/2026 (pipeline `extract-screenshot-data` → `ict-audit` ∥ `ict-devils-advocate` → `ict-doctrine` synthesis), kết luận **NOT ALIGNED**: claim "Bias Bullish sau reclaim" FAIL vì không có MSS tại swing có ý nghĩa cấu trúc; mức 28,215.9 chỉ là internal liquidity pool, swing low thật nằm gần 27,074.

## 2. Timeline dữ liệu thu thập trong session

| # | Dữ liệu | Giá trị |
|---|---|---|
| 1 | D1 close thấp nhất trong đợt breakdown 27/7–30/7 | **27,114** (body close, không phải wick), theo sau bởi 1 nến bullish lớn |
| 2 | Swing low D1 kế tiếp (thấp hơn) | 26,874 — pullback mỏng trong nhịp tăng gần thẳng, **giá chưa từng chạm** trong nhịp này |
| 3 | W1 candle chứa breakdown | O 28,347.2 · H 28,604.6 · **L 27,062.4** · C 28,160.6 — body đóng **dưới** 28,215.9 |
| 4 | Named liquidity pool của sweep | **Relative Equal Lows (EQL)** của 2 nến D1 ngày **8/7/2026** và **13/7/2026** |
| 5 | Swing high D1 gần nhất chưa bị phá | **29,865.3** (30,771.6 là D1 DR High của leg lớn hơn/cũ hơn — cấu trúc khác) |
| 6 | W1 hiện tại (live) | O 28,447.5 · H 29,834.4 · L 28,191.8 · **C 29,758.1** (+5.67%) |

Ba phép đo độc lập cho swing low đều hội tụ về cùng vùng: 27,074 (multi-agent review 04/08) · 27,114 (D1 close) · **27,062.4 (W1 wick — số chính xác nhất, đọc trực tiếp từ trục giá)**.

## 3. Bộ quy tắc doctrine áp dụng

**Dealing range hợp lệ khi nào / redraw khi nào** (canon ICT 2022, xem `ict-doctrine/references/doctrine.md` §Dealing range, §Sweep, §MSS):

1. **Body close vs. wick** — boundary chỉ "phá" theo nghĩa cấu trúc khi có body close vượt qua; wick-only rồi reject là đang lấy liquidity ngoài boundary, không phá range.
2. **Sweep cần 3 điều kiện** — (a) named pool cụ thể bị quét, (b) giá xuyên qua, (c) có rejection (pool bị *dùng*, không chỉ chạm). Thiếu tên pool → UNSUPPORTED.
3. **Số nến & displacement quyết định Raid vs. Acceptance** — 1 nến wick-and-reject là raid (range sống); nhiều nến liên tiếp đóng cửa ngoài boundary với thân lớn là acceptance (range chết).
4. **MSS phải test đúng swing point có ý nghĩa** — cần body close, ngược short-term move, lý tưởng kèm displacement. Reclaim qua một mức tự vẽ (không phải swing thật) **không** phải MSS.
5. **Phân biệt boundary tự vẽ với liquidity pool thật** — range low bạn chọn có thể chỉ là internal pool nằm trên một swing low thật sâu hơn; đây là lỗi doctrine nặng và là lỗi gốc của case 04/08.

Xem sơ đồ quy tắc đầy đủ ở diagram 2 (mục 6).

## 4. Ruling theo claim (C1–C5)

| # | Claim | Status | Ghi chú |
|---|---|---|---|
| **C1** | D1 range gốc 30,771.6–28,215.9 đã invalid | AMBIGUOUS nghiêng PASS *(xem O2, mục 7 — không có ngưỡng doctrine cứng cho "bao nhiêu ngày = acceptance")* | Multi-day body close dưới 28,215.9 + W1 body cũng đóng dưới → nghiêng mạnh về acceptance, không phải raid |
| **C2** | Swing low mới ≈ 27,062.4 | **PASS** | 3 nguồn độc lập hội tụ, không bị objection nào đánh đổ |
| **C3** | Breakdown là sweep hợp lệ của EQL (8/7 & 13/7) | AMBIGUOUS *(xem O1)* | Tên pool hợp lệ về hình thức, nhưng chưa chứng minh được pool này pre-registered trước cú sweep — rủi ro post-hoc pattern-matching |
| **C4 — LOAD-BEARING** | Giá đang đảo chiều bullish, bias đã đổi | **FAIL/chưa PASS** | High 29,834.4 & close 29,758.1 đều chưa vượt 29,865.3 bằng body close — MSS chưa xảy ra |
| **C5** | Range vận hành hiện tại = 27,062.4–29,865.3, giá premium | **PASS** (sống sót qua sensitivity test — xem O4/mục "Sống sót") | Đổi sang range lớn hơn (27,062.4–30,771.6) không lật kết luận premium |

## 5. Sơ đồ 1 — Redraw Dealing Range

![[diagram-dealing-range-redraw.svg]]

## 6. Sơ đồ 2 — Quy tắc Sweep vs. Break

![[diagram-sweep-vs-break-rules.svg]]

Case NDX hiện tại (05/08/2026) đang nằm chính xác ở nhánh: **body close phá boundary → có displacement + acceptance → range cũ chết → nhưng MSS tại swing có ý nghĩa chưa xảy ra** → *"Range cũ chết, bias mới chưa xác nhận"*. Đây không phải một verdict tiêu cực — đây là trạng thái trung gian trung thực nhất mà evidence hiện có cho phép.

## 7. Phân tích & phản biện chuyên sâu (Devil's Advocate)

**Mode:** LIVE (outcome chưa biết cho cả hai bên) · **Evidence sufficiency:** *partial* — có D1 + W1 đầy đủ, trục giá/thời gian đọc được rõ; nhưng **hoàn toàn thiếu lớp H1** — theo đúng workflow D1→H1→M5 mà chính phương pháp của bạn yêu cầu, đây là một "chuỗi thiếu" cần bổ sung trước khi nói đến execution, không phải một FAIL, nhưng giới hạn độ mạnh của mọi verdict dưới đây.

### 7.1 Claim graph & load-bearing claim

Đã liệt kê ở mục 4 (C1–C5). **Load-bearing claim = C4**: nếu "bias đã đảo chiều bullish" sai, toàn bộ khung "redraw range mới, giá đang premium chờ tiếp diễn lên" (C5) tuy vẫn đúng về arithmetic nhưng mất hết ý nghĩa định hướng.

### 7.2 Đối tượng bị phản biện — kể cả ruling của chính mentor

**O1 · [METHOD] · material · attacks C3**
Claim: "EQL 8/7 & 13/7 là named pool bị sweep → C3 gần PASS."
Vấn đề: pool này được nêu tên **sau khi** đã thấy nến đảo chiều và giá đã hồi lên ~29,758 (câu trả lời được viết ngày 05/08, nhìn lại một sự kiện của 27–30/7). Không có bằng chứng nào (screenshot, journal entry) cho thấy 2 relative equal lows này được đánh dấu làm target **trước** cú sweep. Đây đúng dạng lỗi "vẽ POI khớp với kết luận đã biết" — known weakness #4 trong project instructions (confirmation bias / curve-fitting khi backtest).
Consequence: C3 không thể chốt PASS chỉ vì có tên pool hợp lệ về hình thức — cần chứng minh tính real-time.
Retracted by: một screenshot/journal entry đánh dấu EQL này **trước** 30/7/2026.

**O2 · [DOCTRINE GAP] · material · attacks C1 (tự-kiểm ruling của mentor ở các turn trước)**
Claim (của tôi): "3–4 ngày đóng thân dưới boundary = acceptance, không phải raid."
Vấn đề: canon ICT 2022 **không** định nghĩa một ngưỡng số ngày cụ thể để phân biệt raid kéo dài với acceptance thật — "structurally significant" ở đây là một điểm doctrine không fix được ranh giới. Ngưỡng "3–4 ngày" tôi dùng là suy luận hợp lý, không phải một con số trích được từ doctrine.
Consequence: hạ C1 từ "PASS chắc" xuống AMBIGUOUS-nghiêng-PASS — kết luận thực tế không đổi (range cũ vẫn nên coi là chết), nhưng độ tự tin cần ghi đúng mức.
Retracted by: không thể — đây là doctrine gap thật, chỉ có thể thu hẹp bằng cách bạn tự đặt và **áp dụng nhất quán** một ngưỡng cá nhân (xem Test 3, mục 7.5).

**O3 · [CHART] · fatal · attacks C4 (load-bearing)**
Claim: "Giá đang đảo chiều bullish, bias đã đổi."
Fails: MSS evidence bar cần body close qua swing point có ý nghĩa, kèm displacement.
Evidence: W1 hiện tại — High 29,834.4, Close 29,758.1 — cả hai **đều dưới** 29,865.3.
Consequence: toàn bộ narrative "bullish reversal xác nhận" hiện chưa có chân đứng; đây là đúng lỗi mà multi-agent review 04/08 đã tìm thấy, **lặp lại nguyên trạng, chưa được vá.**
Retracted by: D1 hoặc W1 đóng thân qua 29,865.3 kèm displacement.

### 7.3 Cái sống sót qua kiểm định (What survives)

- **C2** (swing low 27,062.4) — vững, 3 nguồn hội tụ, không objection nào đánh được.
- **C5's arithmetic** — đã chạy sensitivity: đổi range từ 27,062.4–29,865.3 sang 27,062.4–30,771.6, midpoint đổi từ 28,463.85 → 28,917.0, nhưng **premium/discount không lật** (giá vẫn premium ở cả hai cách tính: 92.4% và 72.7% vị trí trong range tương ứng). Đây là một objection tôi tự chạy và nó **không phá được C5** — ghi nhận công khai thay vì giả vờ không kiểm.
- **Việc đặt tên named pool cho sweep** — dù còn nghi vấn hindsight (O1), đây là tiến bộ thật về evidence discipline so với case 04/08 (lúc đó "sweep" bị gọi hoàn toàn không có pool nào).
- **Việc không vội gọi "Bias Bullish confirmed"** qua các turn trước — giữ đúng nguyên tắc Process > P&L, tự-kiểm lại vẫn đúng.

### 7.4 Case đối lập (Opposite case — cùng evidence, đổi vai trò)

**Case đối lập:** đây không phải một reversal thật, mà là một **stop-run sâu vẫn nằm trong nhịp điều chỉnh giảm lớn hơn** — rally hiện tại chỉ là relief rally kỹ thuật trước khi tiếp diễn giảm.

Cùng facts, đổi vai trò:
- Cùng nến displacement bullish (sau sweep 27,062.4) → đọc thành "bull trap được dựng trên một sweep chưa từng có MSS xác nhận", không phải khởi đầu leg tăng mới.
- Cùng vị trí giá premium sát dưới 29,865.3 → doctrine ICT thường dạy premium sát một DOL đối diện là vùng **chờ short**, không phải xác nhận đã đổi bias — case gốc và case đối lập dùng chung một fact (vị trí premium) nhưng gán ý nghĩa ngược nhau.
- Cùng multi-day acceptance dưới 28,215.9 (C1) → đọc thành bước mở đầu của một downtrend lớn hơn chưa kết thúc, sweep 27,062.4 chỉ là điểm dừng tạm thời.

**Tự tấn công case đối lập:** nếu đây chỉ là relief rally kỹ thuật, tại sao nến displacement bullish sau sweep lại lớn và dứt khoát đến vậy (đủ mạnh tạo imbalance rõ)? Một relief rally thuần kỹ thuật thường yếu và overlapping hơn. Đây là một quan sát chart-based làm **yếu một phần** case đối lập — không fatal, nhưng đáng ghi nhận.

**Nhãn:** *equally viable / undecidable from this evidence* — không đạt "stronger" vì không có fact nào mà case gốc không giải thích được và case đối lập giải thích được (ngược lại cũng vậy).

**Observable duy nhất phân định hai case:** hướng của cú breakout tiếp theo tại 29,865.3 — D1/W1 đóng thân **qua** 29,865.3 kèm displacement → case gốc thắng; giá quay đầu đóng lại **dưới** 28,215.9 (hoặc 27,062.4) **trước khi** chạm 29,865.3 → case đối lập thắng. Tại thời điểm viết note này, quan sát đó **chưa xảy ra**.

### 7.5 Falsification tests (tối đa 3, test 1 bắt buộc = invalidation condition cho LIVE mode)

1. **Test xác nhận/vô hiệu hoá (đóng O3, C4):** D1 hoặc W1 đóng thân qua 29,865.3 kèm displacement → MSS xác nhận, case gốc thắng. D1/W1 đóng thân lại dưới 28,215.9 (hoặc tệ hơn dưới 27,062.4) **trước khi** chạm 29,865.3 → case đối lập được xác nhận, coi rally hiện tại là relief rally thất bại.
2. **Test hindsight (đóng O1, C3):** tìm trong lịch sử chart/journal trước 30/7/2026 xem EQL 8/7 & 13/7 có được đánh dấu là POI/target từ trước không. Có → O1 rút, C3 lên PASS chắc. Không tìm thấy → giữ C3 ở AMBIGUOUS, ghi nhận là bài học "đặt tên pool trước, không phải sau."
3. **Test ngưỡng cá nhân (thu hẹp O2, C1):** không có test thị trường cho doctrine gap này. Thay vào đó: tự đặt một **rule cá nhân cố định** (ví dụ "≥3 ngày liên tiếp đóng thân ngoài boundary kèm displacement = acceptance") và áp dụng **nhất quán** cho mọi case sau — tránh doctrine drift giữa các lần backtest (case này dùng ngưỡng khác case khác).

### 7.6 Verdict phần phản biện

**UNPROVEN** — không tìm được lỗi fatal phá vỡ hoàn toàn case gốc, nhưng load-bearing claim (C4) vẫn đứng trên evidence chưa đủ để phân biệt với case đối lập, và evidence sufficiency ở mức *partial* (thiếu hẳn lớp H1). Đây **không phải** "SURVIVES THIS ATTACK" — không được đọc thành xác nhận bias bullish.

**Điều note này KHÔNG xác lập:** (1) không xác lập giá sẽ đi lên tiếp hay quay đầu — đó là dự đoán giá, ngoài phạm vi; (2) không xác lập rằng named pool EQL là sai — chỉ là chưa chứng minh được tính real-time; (3) không xác lập một ngưỡng "N ngày = acceptance" chính thức — đó là doctrine gap thật, cần rule cá nhân, không phải canon.

## 8. Action items (Obsidian journal)

- [ ] Redraw D1 Dealing Range trên chart: Low = 27,062.4 (không dùng 28,215.9 làm boundary hoạt động nữa)
- [ ] Theo dõi body close D1/W1 qua 29,865.3 kèm displacement — điều kiện MSS bắt buộc trước khi gọi "Bias Bullish confirmed"
- [ ] Tìm/xác nhận trong lịch sử chart trước 30/7/2026 xem EQL (8/7 & 13/7) đã được đánh dấu làm target chưa — nếu không, ghi bài học về đặt tên POI post-hoc
- [ ] Tự đặt ngưỡng cá nhân cho "bao nhiêu ngày đóng thân ngoài boundary = acceptance" và áp dụng nhất quán cho các case sau
- [ ] Bổ sung khung H1 cho case này khi có chart — hiện đang thiếu hoàn toàn lớp cấu trúc trung gian D1→H1→M5
- [ ] Không mở bias mới (long/short) dựa trên case này cho tới khi Test 1 (mục 7.5) ngã về một phía

## 9. Liên kết

- Case trước: multi-agent review 04/08/2026 (`claude/2026-08-04-NDX-D1-bias-multiagent-review.md` trong Project "Market Analysis") — verdict NOT ALIGNED, cùng lỗi gốc (reclaim ≠ MSS) mà C4 ở đây vẫn đang lặp lại chưa được vá.
- Follow-up ruling 05/08/2026 (`claude/2026-08-05-NDX-D1-range-redraw-followup.md` trong Project "Market Analysis") — bản ruling từng-claim trước khi note này tổng hợp lại đầy đủ kèm phản biện.
