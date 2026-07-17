---
type: daily-summary
date: 2026-07-17
days_to_prop_exam: 174
exam_target: 2027-01-07
backtests_logged: 2
trades_logged: 0
concepts_reviewed: 2
mistakes_triggered: ["09 - Mistake - Wrong daily bias", "02 - Mistake - Enter before liquidity sweep"]
net_r_today: "+1.33R (backtest/replay, KHÔNG phải vốn thật — Win +2.33R, Loss -1R)"
tags: [daily-summary, prop-firm-prep]
---

# 🌙 Daily Summary — 2026-07-17

> [!info] Đếm ngược
> **174 ngày** còn lại tới mốc tự đặt **2027-01-07** (song song FTMO 10K$ + The5ers High Stakes 10K$ — hai track độc lập, không mua gói nào). Giai đoạn hiện tại: **Giai đoạn 1 — Nền tảng**. Theme hôm nay: **ngày backtest tốt nhất về nội dung mentor-review trong nhiều ngày, nhưng kỷ luật "đóng vòng đo tiến độ" vẫn là điểm rò rỉ — và lần đầu tiên có một con số chiếu-nhịp cụ thể cho thấy mốc backtest 200 đang lệch sau mốc thi tự đặt.**

> [!warning] ⚠️ Cảnh báo
> 1. **Mistake top-3 tái diễn trong backtest:** `bias_correct: No` xuất hiện ở note `02 - Loss - GBPUSD - 2014-07-17` — đây là lỗi **#09 Wrong daily bias**, một trong 3 lỗi top hiện tại của Giai đoạn FOUNDATION (06, 08, 09). Xem phân tích chi tiết ở mục Backtest/Mistake dưới — có nuance quan trọng cần đọc, không chỉ là "lại phạm lỗi cũ".
> 2. **Nhịp backtest KHÔNG kịp mốc thi tự đặt 2027-01-07** (phát hiện mới, xem mục Đối chiếu mục tiêu): tại nhịp hiện tại 0,92 backtest/ngày, mốc 200 backtest sẽ chạm vào khoảng **2027-01-27** — chậm hơn ~20 ngày so với 2027-01-07.
> 3. **Log tiến độ FTMO + The5ers có dòng cho hôm nay nhưng nội dung rỗng** ("Tập trung backtest") — không đáp ứng yêu cầu cụ thể mà chính file task sáng nay đặt ra (phân biệt luật hai quỹ, đối chiếu số liệu thật). "Có dòng" ≠ "log thật".
> 4. **Lỗi ghi chép dữ liệu tái diễn ngay trong ngày tạo note lỗi:** note `01 - Win - GBPUSD - 2014-06-25 - Long.md` có filename lệch `trade_date` frontmatter (`2014-07-14`) — đúng loại lỗi mà [[12 - Mistake - Log Data Mismatch - Backtest]] (tạo hôm nay) mô tả. Chưa đổi tên file, chờ Khang xác nhận.

## 📚 Học hôm nay

**2 concept được ôn thật** (đối chiếu trực tiếp frontmatter `last_reviewed`, không dựa vào tick task-list):

- **[[29 - Sell-side Imbalance Buy-side Inefficiency]]** (SIBI) — `status: seed → developing`, `last_reviewed: 2026-06-24 → 2026-07-17`. Đây là **lần đầu tiên** concept này được ôn kể từ khi tạo (03 tuần đứng yên). Góc học: SIBI là phần bù của BISI trong một FVG giảm giá — imbalance bên bán mạnh hơn bên mua, dùng để xác nhận hướng displacement giảm trước khi tin MSS xuống; phân biệt với FVG (khái niệm cha) và với BSL/SSL (đây là *imbalance*, không phải *liquidity pool*). ⚠️ **Ghi nhận một mismatch nhỏ tự phát hiện khi đọc note:** frontmatter ghi `created: 2026-07-17` nhưng nội dung note lại nói rõ concept này được tạo từ `2026-06-24` — chính bản thân note học hôm nay cũng mang một vết "Log Data Mismatch" kiểu (a)/(c) giống hệt loại lỗi vừa được đặt tên chính thức trong `06 - Mistake Database/`. Đáng để Khang kiểm tra lại `created` field này.
- **[[12 - Dealing Range]]** — `status: developing` (không đổi), `last_reviewed: 2026-06-22 → 2026-07-17` (tái ôn, cũ nhất trong nhóm đã từng ôn). Góc học: quy trình chọn đúng swing high/low làm biên dealing range TRƯỚC khi tính Premium/Discount — ưu tiên swing tạo bởi liquidity sweep + MSS thật, không phải swing bất kỳ; chọn sai range là gốc rễ của cả [[Mistake - Wrong Dealing Range]] và [[09 - Mistake - Wrong daily bias]].
- Cả hai concept được **áp dụng trực tiếp** vào 2 backtest hôm nay (dealing range dùng để định biên H1 cho cả 2 note; SIBI dùng để mô tả "imbalance rõ" khi chấm displacement) — không phải ôn lý thuyết suông.
- **[[14 - Implied Fair Value Gap]]** (mục "nếu còn thời gian" trong task sáng) — **không có bằng chứng ôn**: `last_reviewed` vẫn giữ `2026-06-23`, không đổi. Checkbox tương ứng trong task sáng cũng để trống `[ ]` — khớp thật, không phải overtick.

## 📊 Backtest hôm nay

**2 backtest mới**, cả hai GBPUSD, chuỗi backtest sang **ngày thứ 12 liên tiếp** (07-06 → 07-17). Tổng mẫu toàn vault: **22/200 (11%)** — 13 EURUSD + 4 GBPUSD + 4 XAUUSD + 1 NAS100; **17 Win / 5 Loss ≈ 77,3%** (giảm nhẹ từ 80% ở n=20).

### `01 - Win - GBPUSD - 2014-06-25 - Long` (thực chất trade_date = 2014-07-14)
- **HTF bias:** Bullish, đúng (D1 HH/HL + Displacement Order Block, draw-on-liquidity BSL thẳng hàng).
- **Chuỗi entry:** Sweep (nội bộ, quét CE FVG H1) → Displacement + MSS (M5) → FVG M5 → Entry CE FVG M5 = 1.70837. Đủ 6/7 bước, bước 6 (Entry) chỉ **Partial**.
- **Vấn đề thật:** FVG H1 (1.70833–1.70591) trải từ EQ đến gần 0.705 OTE — bị "cắt đôi" thành nửa nông (EQ–0.618, không phải nơi smart money nạp lệnh) và nửa sâu (0.618–0.705, vùng tài trợ thật). Entry rơi vào **nửa nông**, sát cạnh trên FVG — không vào OTE (0.618–0.786).
- **R planned vs thực nhận:** 2.33 = 2.33 (hit TP đầy đủ). Nhưng nếu vào đúng sweet spot (0.705), risk ngắn hơn (~16 pip vs 26 pip) → RR lẽ ra ~5.0, gấp đôi.
- **Followed plan:** Yes. **Grade:** B (không phải A) — quy trình đúng hướng nhưng **entry vị trí kém tối ưu**, và SL sống sót nhờ **chỉ 1,5 pip đệm** khi giá quét ngược xuống cạnh dưới FVG trước khi bật lên TP — "sống sót nhờ may nhiều hơn thiết kế".
- **Bài học:** MSS trên tap NÔNG của POI HTF là MSS "sớm" — dễ là LTF inducement, chưa phải shift thật. Chỉ tin MSS sau khi giá đã chạm vùng sweet spot của POI.
- **Root cause (thắng):** đúng bias + đúng phía POI, KHÔNG phải nhờ entry tối ưu — "process che giấu bởi outcome" là đúng bài học "process over outcome" cần khắc sâu, đừng để cú thắng này *củng cố* thói quen vào nông.

### `02 - Loss - GBPUSD - 2014-07-17 - Long`
- **HTF bias:** Bullish theo D1 (HH/HL + rejection candle tại POI) — **phương pháp đọc đúng**, nhưng `bias_correct: No` vì cấu trúc H1 sau đó lật bearish (CISD). Đây là lỗi #09 top-3, nhưng đọc kỹ thì **không phải lỗi "chọn nhầm hướng từ đầu"** — root cause thật nằm ở bước Sweep (xem dưới), bias D1 tại thời điểm setup là hợp lý.
- **Chuỗi entry:** Sweep = **No** (SSL cấu trúc — đáy dealing range 1.70592 — CHƯA bị quét trước khi MSS xuất hiện) → Displacement yếu (score 2/4) → MSS (có, nhưng "sớm") → FVG hợp lệ, trong OTE (0.705, CE trùng khớp) → Entry cơ học đúng (CE M5 FVG, không chase).
- **First error step: Sweep (bước 3).** Theo đúng GATE checklist của chính playbook (sweep phải xảy ra TRƯỚC displacement/MSS), đây đáng lẽ là **No Trade** — không có đệm thanh khoản nội bộ giữa POI và điểm định nghĩa range để hấp thụ, nên giá đâm thẳng qua entry, đóng cửa dưới range low (CISD), FVG lật thành iFVG.
- **R planned vs thực nhận:** 3.40 → **−1** (SL bị quét, đúng risk 0,5% đã set).
- **Followed plan:** Yes — **không dời SL, không gồng, không revenge** — đây là **"good loss"** thật về kỷ luật, khác hẳn loss FOMO trước đây.
- **Grade:** C. Điểm mạnh: entry precision (8/10, CE ~0.705, không nông như note 01), risk management (7/10). Điểm yếu quyết định: Liquidity Sweep (2/10 — GATE fail).
- **Bài học cốt lõi:** phân biệt **internal liquidity** (wick raid nội bộ, POI còn sống) vs **structural liquidity** (đóng cửa xuyên điểm định nghĩa range = CISD = POI invalidated). MSS sớm + leg yếu + không có đệm thanh khoản nội bộ = tín hiệu No Trade, dù POI/FVG "đẹp" trên giấy.
- **Pattern mới được đề xuất (KHÔNG tạo note vội — n=1, tránh curve-fitting):** "Entry INTO liquidity — POI sát móng dealing range, SSL cấu trúc chưa quét". Về bản chất, đây trùng khớp gần như hoàn toàn với note đã có sẵn **[[02 - Mistake - Enter before liquidity sweep]]** (frequency 4, status active) — chỉ chưa được gắn wikilink chính thức từ backtest hôm nay. Khuyến nghị: link thẳng vào note có sẵn thay vì tạo note lỗi thứ 13 trùng lặp; nếu pattern "POI sát móng range không đệm" tái diễn ≥3 lần nữa thì tách thành biến thể riêng có ghi rõ trong `06 - Mistake - Enter before liquidity sweep`.

### Aggregate hôm nay
Net R backtest: **+2.33 (Win) + (−1) (Loss) = +1.33R** (dữ liệu replay lịch sử, KHÔNG phải P&L thật). Grade trung bình B/C. Cả hai note followed_plan: Yes — điểm sáng thật của ngày là **kỷ luật thực thi**, điểm cần sửa là **chất lượng lọc/vị trí entry**, không phải kỷ luật.

## 💹 Live Trade hôm nay

**Không có lệnh live nào hôm nay** — khớp với việc Giai đoạn 1/FOUNDATION chưa mua gói và chưa ưu tiên khối lượng live. Lệnh live gần nhất vẫn là `Loss - 01 - Trade 2026-06-18 NDX Short` → **29 ngày** không có lệnh live mới. Đây KHÔNG phải thất bại kỷ luật theo đúng roadmap hiện tại (backtest là ưu tiên #1), nhưng cũng là một khoảng trống thật cần ghi nhận: **execution dưới áp lực luật quỹ thật vẫn là ẩn số hoàn toàn chưa kiểm chứng** trong gần một tháng qua — 174 ngày còn lại tới mốc thi không nên trôi hết ở replay/backtest mà không có ít nhất một giai đoạn demo-live theo đúng luật FTMO/The5ers trước khi mua gói (xem Kế hoạch hành động Giai đoạn 1 trong 2 goal file challenge).

## 🧠 Phân tích lỗi & tâm lý

**Mistake chính thức tái diễn hôm nay (top-3 FOUNDATION):**

- **[[09 - Mistake - Wrong daily bias]]** — `bias_correct: No` ở note `02 - Loss GBPUSD 07-17`. **Nuance quan trọng:** đọc kỹ phân tích trong note thì đây KHÔNG phải trường hợp điển hình của lỗi 09 (chọn nhầm hướng D1 từ đầu — phương pháp đọc bias hôm nay đúng, có HH/HL + rejection candle tại POI, hợp lý tại thời điểm setup). Nó gần với việc **H1 delivery lật sau đó** (CISD) hơn là một lỗi phân tích bias gốc. Ghi nhận đúng theo field (`No` để trung thực thống kê) nhưng root cause thật của lệnh này là lỗi Sweep, không phải lỗi Bias — tránh gán nhãn sai khi review sau này.
- **[[02 - Mistake - Enter before liquidity sweep]]** (chưa được wikilink chính thức từ backtest, nhưng khớp thuyết trình gần như 1:1 với `first_error_step: sweep` của note `02`) — vào Long tại POI trong khi SSL cấu trúc bên dưới còn nguyên, tự nguyện làm thanh khoản đối ứng cho smart money. Đây là lỗi #2 trong Mistake Database (frequency 4, status active) — không phải lỗi mới, chỉ chưa được liên kết đúng từ note hôm nay.

**Mistake mới được TẠO hôm nay (không phải "tái diễn", mà là đóng nợ quy trình):**

- **[[12 - Mistake - Log Data Mismatch - Backtest]]** — tạo thật trong `06 - Mistake Database/`, đóng đúng khoản nợ 4 ngày (07-14 → 07-17) đã được nhắc trong 3 dòng log liên tiếp trước đó. Định nghĩa: dữ liệu backtest lệch nhau giữa frontmatter, bảng Backtest Summary trong thân note, phần narrative, và tên file — khiến chính sample đó không đáng tin cho thống kê expectancy, bất kể setup/entry logic đúng hay sai. 4 dạng mismatch được liệt kê rõ trong note (frontmatter-vs-filename, frontmatter-vs-bảng-summary, narrative-vs-chính-nó, R-multiple không khớp entry/SL/TP).
- **Trớ trêu cần gọi thẳng:** đúng ngày note lỗi này được tạo, note `01 - Win - GBPUSD - 2014-06-25` (log CÙNG NGÀY) lại mắc đúng dạng mismatch (a) mà note vừa mô tả — filename ghi `2014-06-25`, `trade_date` frontmatter ghi `2014-07-14`. Việc "biết lỗi" và "vẫn mắc lỗi trong cùng buổi" là chính xác kiểu pattern mà mentor cần nêu thẳng, không rationalize. Chưa đổi tên file — chờ Khang xác nhận (và lưu ý: gợi ý đổi số thứ tự file thành `02` trong note đó là SAI, vì đây là backtest đầu tiên của ngày, chỉ cần sửa phần ngày trong tên).

**Không có tín hiệu tâm lý tiêu cực đáng gờm** trong 2 backtest hôm nay — cả hai `followed_plan: Yes`, không có dấu hiệu FOMO/revenge/dời SL. Vấn đề hôm nay thuần về **chất lượng lọc setup và ghi chép dữ liệu**, không phải kỷ luật cảm xúc.

## 🎯 Đối chiếu mục tiêu

**1. [[Build a statistically validated backtest sample]]** (Mid Term) — `progress` sync 10 → **11%** (22/200). Cột mốc vẫn **0/4**. ⭐ **Phát hiện quan trọng nhất hôm nay:** nhịp thực tế từ `start_date` (24 ngày) = 22/24 ≈ **0,92 backtest/ngày**. Chiếu nhịp này, mốc 200 backtest rơi vào khoảng **2027-01-27** — **chậm hơn ~20 ngày so với mốc tự đặt sẵn sàng thi 2027-01-07** (còn 174 ngày). Cần nhịp **~1,02/ngày** (nhanh hơn hiện tại ~11%) để chạm cả hai mốc cùng lúc. Due_date frontmatter của goal (2027-06-30) không phải ràng buộc thật — mốc thật là ngày Khang tự đặt; hai mốc này đang lệch, cần quyết định: tăng nhịp, hoặc chấp nhận mua gói sớm hơn với mẫu nhỏ hơn 200 (vd dùng ngưỡng 100 setup của goal #2, cũng due sau 01-07).

**2. [[Master the ICT 2022 Model]]** (Mid Term) — `progress` giữ **30%** (đã lệch xa cột mốc thực tế 0/5 = 0%, mismatch này đã được nêu từ 07-16, vẫn chưa được Khang xác nhận sửa). Số liệu sync: 22/100 setup (22%), win rate **77%** (n=22, giảm nhẹ từ 80%, chưa đủ để kết luận xu hướng). Cột mốc #1 "viết checklist vào/ra lệnh thành văn" — đòn bẩy rẻ nhất còn treo, không cần lệnh live — **vẫn chưa làm**, đã treo từ nhiều ngày.

**3. [[Hold daily journaling and process discipline]]** (Short Term) — Track khoẻ nhất hệ thống. Journaling **14 ngày liên tiếp** (07-05→07-17), dài nhất từ trước tới nay. Progress giữ **50%** (khớp cột mốc 2/4). Cột mốc #3 "4 tuần liên tiếp 5 ngày/tuần" — chuỗi 14 ngày ≈ 2 tuần, chưa chạm nhưng đang đúng hướng.

**4. [[Cut my top 3 repeated mistakes]]** (Short Term) — `progress` giữ **20%**, cột mốc vẫn **0/4**. Đã có dòng log cho 2026-07-17 (viết trước khi backtest tối nay hoàn tất) phân tích đúng việc `bias_correct: No` tái xuất và đề xuất pattern sweep mới — nội dung log này **đã khớp tốt** với phân tích ở mục Backtest/Mistake bên trên, không cần thêm dòng trùng lặp. Tần suất lỗi **live-trade** chính thức (06=14, 09=7, 07=5) vẫn đứng yên vì không có lệnh live — chỉ số này bị đóng băng, không phải cải thiện hay xấu đi.

**5 & 6. [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]]** (cả hai nằm ở `09 - Goal Tracking/Goals/Mid Term`, KHÔNG phải `Long Term` như CLAUDE.md map — lệch cấu trúc cần cập nhật memory) — cả hai `progress: 0%`, cột mốc **0/8**, `phase: Phase 0/1 - Preparation`. Cả hai đã có dòng log ngày 2026-07-17 nhưng nội dung chỉ ghi **"Tập trung backtest"** — quá sơ sài, không đáp ứng yêu cầu cụ thể mà file task sáng nay đặt ra (ghi rõ trạng thái prep thật, phân biệt luật FTMO daily-loss-từ-balance-gốc vs The5ers daily-drawdown-từ-equity-đóng-cửa-hôm-trước + ngày-có-lãi ≥0,5%). Phần riêng của The5ers (ngưỡng "ngày có lãi = +50$" + mô phỏng drawdown prior-close) trong [[Lot size 10K]] **vẫn chưa được bổ sung** — nợ treo nhiều ngày.

**Verdict nhịp độ (174 ngày còn lại):** Journaling và kỷ luật thực thi đang **trên nhịp rõ rệt** (14 ngày liên tiếp, followed_plan Yes 2/2 hôm nay). Nhưng khi quy đổi ra số cụ thể, **mẫu backtest — điều kiện tiên quyết trước khi mua gói bất kỳ — đang chậm hơn mốc thi ~20 ngày** nếu giữ nhịp hiện tại, và **0 lệnh live 29 ngày** nghĩa là toàn bộ 174 ngày còn lại chưa hề bắt đầu giai đoạn "demo thử luật" (Giai đoạn 1 của cả 2 goal challenge) — giai đoạn này cần ít nhất 2 tuần trước khi mua gói. Nếu tính lùi: Chuẩn bị (backtest+playbook) → Demo 2 tuần → Mua gói → Phase 1/2 — 174 ngày về lý thuyết vẫn đủ, nhưng biên an toàn đang co hẹp lại vì mảng "log tiến độ 2 goal challenge" đang bị đối xử như thủ tục (dòng rỗng) hơn là công cụ điều hướng thật.

## 📈 Cập nhật Nhật ký tiến độ

Đã thêm dòng log **THẬT** cho 2026-07-17 vào 3 goal file (không phải dòng rỗng — mỗi dòng đều gắn số liệu/root-cause cụ thể từ dữ liệu hôm nay):

- **[[Build a statistically validated backtest sample]]** — dòng mới: sync 22/200 (11%), phát hiện nhịp-chậm-hơn-mốc-thi 2027-01-27 vs 2027-01-07, ghi nhận [[12 - Mistake - Log Data Mismatch - Backtest]] đã tạo, cờ mismatch tên file note `01`.
- **[[Master the ICT 2022 Model]]** — dòng mới: sync 22/100 (22%), win rate 77%, ghi nhận 2 concept áp dụng trực tiếp vào setup hôm nay, cờ mismatch tên file lặp lại.
- **[[Hold daily journaling and process discipline]]** — dòng bổ sung "(tối)" đè lên dòng sáng sớm (viết lúc 06:07, trước khi có hoạt động) bằng bằng chứng thật cuối ngày: 2 backtest + 2 concept + 1 mistake note mới + 14 ngày liên tiếp; đồng thời gọi thẳng tên vấn đề "log có dòng nhưng nội dung rỗng" ở 2 goal FTMO/The5ers.

**Không thêm dòng** cho [[Pass FTMO first package challenge (10K$)]], [[Pass The5er first package challenge (10k$)]], và [[Cut my top 3 repeated mistakes]] — cả ba đã có dòng log ngày 2026-07-17 sẵn trong file (viết trước khi routine tối nay chạy), thêm dòng nữa sẽ tạo trùng lặp. Thay vào đó, chất lượng của các dòng có sẵn được đánh giá thẳng ở mục Đối chiếu mục tiêu trên (2/3 dòng quá sơ sài, 1/3 dòng — Cut-mistakes — đã đạt chuẩn).

## 🔭 Việc cần làm ngày mai

1. **Viết lại THẬT dòng log FTMO + The5ers cho 07-17/07-18** — không chấp nhận "Tập trung backtest" là đủ. Phải có: trạng thái prep cụ thể (backtest 22/200, playbook A+ checklist vào/ra vẫn 0/5), và với The5ers riêng: bổ sung "ngày có lãi = +50$" + ví dụ mô phỏng drawdown prior-close vào [[Lot size 10K]] — nợ đã treo từ 07-13.
2. **Xác nhận rename file `01 - Win - GBPUSD - 2014-06-25 - Long.md` → `01 - Win - GBPUSD - 2014-07-14 - Long.md`** (giữ số `01`, chỉ sửa ngày) — chưa tự đổi, cần "yes" từ Khang trước.
3. **Link chính thức [[02 - Mistake - Enter before liquidity sweep]] vào note `02 - Loss - GBPUSD - 2014-07-17 - Long`** (và cân nhắc link tương tự cho note `01` nếu muốn theo dõi pattern "entry nông nửa trên POI" — chưa đủ 3 lần để tách mistake riêng, nhưng nên bắt đầu đếm).
4. **Kiểm tra `created: 2026-07-17` ở frontmatter [[29 - Sell-side Imbalance Buy-side Inefficiency]]** — có vẻ sai (nội dung note nói tạo từ 06-24); một mismatch nhỏ tự phát hiện trong lúc học hôm nay.
5. **Xác nhận có tick cột mốc #1+#2 của [[Cut my top 3 repeated mistakes]] hay không** (đề xuất từ 07-08, chưa xác nhận) và cột mốc #1 của [[Master the ICT 2022 Model]] (viết checklist vào/ra — đòn bẩy rẻ nhất, không cần lệnh live).
6. **Cân nhắc mở giai đoạn Demo thử luật (2 tuần)** cho ít nhất 1 trong 2 track FTMO/The5ers sớm hơn dự kiến — 29 ngày không lệnh live đang ăn vào 174 ngày còn lại mà chưa hề bắt đầu bước kiểm chứng execution dưới luật quỹ.
7. Tiếp tục chuỗi backtest sang ngày thứ 13 — ưu tiên thị trường non-EURUSD (hiện 9/22 ≈ 41%, đã cân đối tốt hơn nhiều so với tuần trước) và áp GATE "sweep trước displacement" nghiêm hơn để tránh lặp lại first_error_step=sweep.

## 🔗 Liên kết

[[00 - Goal Dashboard]] · [[01 - Roadmap]] · [[02 - Skill Metrics]] · [[_Backtest Dashboard]] · [[02 - Mistake Frequency Dashboard]] · [[03 - Performance Dashboard]] · [[04 - Process Quality Dashboard]]
