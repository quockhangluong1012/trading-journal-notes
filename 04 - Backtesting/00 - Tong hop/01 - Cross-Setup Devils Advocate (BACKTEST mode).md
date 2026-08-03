---
type: devils-advocate
mode: BACKTEST
instrument: multi (EURUSD/GBPUSD/XAUUSD/NAS100)
date: 2026-08-03
timeframes_provided: "text only (frontmatter + narrative của 22 note); không truy cập được ảnh PNG"
scope: toan-sample-22-lenh
verdict: UNPROVEN
evidence_sufficiency: thin
opposite_case_strength: equally viable (cho hầu hết claim cấp-batch)
objections: {fatal: 4, material: 5, minor: 3}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN, O5 OPEN, O6 OPEN, O7 OPEN, O8 OPEN, O9 OPEN, O10 OPEN, O11 OPEN, O12 OPEN"
tags: [ict, devils-advocate, backtest, review, cross-setup]
---

# Devil's Advocate — Toàn sample 22 lệnh (BACKTEST mode)

## 0. Evidence base

Input là **văn xuôi + frontmatter** của 22 note backtest (`analysis_summaries/aggregate_stats.md` + `batchA.md`→`batchE.md`), không phải screenshot hay JSON extraction gốc. Không ảnh PNG nào được đọc trực tiếp ở tầng tổng hợp này — mọi số dùng ở đây là số **do chính 22 note tự ghi** (category 3 theo phân loại provenance: đây là claim của người viết note, không phải evidence độc lập được xác minh bằng chart). `evidence_sufficiency: thin` cho toàn bộ phân tích này vì load-bearing claim cấp sample — "WR 77.3% phản ánh đúng edge của hệ thống" — không thể được đánh giá đầy đủ từ những gì có: không có nhật ký các setup đạt tiêu chí nhưng bị bỏ qua, không có ảnh gốc để verify độc lập bất kỳ con số nào.

**Provenance của sample (bắt buộc theo brief BACKTEST mode)**: Không có tài liệu nào trong vault mô tả **quy trình chọn lệnh để backtest** — tại sao đúng các ngày này (2005, 2010, 2013, 2014, 2016, 2021, 2024, 2026) và đúng các symbol này (EURUSD chiếm 13/22, GBPUSD 4/22, XAUUSD 4/22, NAS100 1/22) được chọn. Không có log nào về setup **đạt đủ tiêu chí 7-bước nhưng không được ghi thành note** (dù thắng hay thua). Đây là câu hỏi provenance cốt lõi mà BACKTEST mode yêu cầu trả lời trước khi tin bất kỳ tỷ lệ Win/Loss nào — xem O1.

## 1. Thesis + load-bearing claim

**Thesis mạnh nhất có thể phát biểu thay người dùng**: "22 lệnh backtest theo ICT 2022 Model cho WR 77.3% và expectancy +1.77R/lệnh, cho thấy hệ thống 7-bước (bias→draw→sweep→displacement→POI→entry→target) là một edge có thể tái lặp, với các lỗi cụ thể (entry sớm, sweep chưa đủ, POI chọn sai cấp) là nguyên nhân của toàn bộ 5 lệnh Loss."

Claim graph:
- **C1**: 22 lệnh là mẫu đại diện cho cách người dùng áp dụng ICT 2022 Model (không phải mẫu được chọn lọc theo outcome).
- **C2**: WR 77.3% (17W/5L) và tổng +37.16R là thước đo hợp lệ của hiệu suất hệ thống.
- **C3**: 5 lệnh Loss đều có `first_error_step` xác định được, và việc sửa đúng bước đó sẽ chuyển Loss thành Win hoặc No-Trade.
- **C4** (từ C3): 4/5 lệnh Loss gần nhất thuộc cùng một họ lỗi duy nhất ("Unswept Liquidity Path" — theo [[2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] mục 9.3).
- **C5**: Confluence score (thang 0-8) và POI rank (thang 8.1) là các thước đo có giá trị dự báo chất lượng setup.
- **C6**: 2 lệnh Win có `first_error_step: entry` (Edge-entry) chứng minh rằng bias/setup-selection quan trọng hơn entry precision.

**Load-bearing claim: C1 → C2.** Nếu C1 sai (sample bị chọn lọc), C2 (WR 77.3%) sụp hoàn toàn bất kể các note riêng lẻ có phân tích sâu sắc đến đâu — đây chính xác là lý do BACKTEST mode yêu cầu chạy cross-setup battery trước khi động vào bất kỳ per-setup nào.

## 2. What survives

- **Kỷ luật cắt lỗ 5/5 -1R** (mục 2 của [[00 - Backtest Dashboard & Statistics]]) là quan sát trực tiếp, không phụ thuộc vào C1/C2 — dù mẫu có bị chọn lọc theo outcome hay không, việc không lệnh Loss nào gồng quá -1R vẫn là một fact độc lập với hindsight.
- **Nỗ lực tự phê bình có thật và tăng dần theo thời gian**: các note cuối (07-14 → 07-17) tự phát hiện lỗi số của chính mình (vd note 07-17/01 tự sửa 2 lỗi 6 pip), điều mà 5 note đầu (07-01→07-07) không làm được. Đây là một cải thiện quy trình quan sát được, độc lập với câu hỏi WR có ý nghĩa hay không.
- **`first_error_step` là một field hữu ích về mặt cấu trúc** — nó buộc mỗi lệnh Loss phải quy về một bước cụ thể trong chuỗi 7 bước, thay vì mô tả mơ hồ "thua vì thị trường đảo chiều". Giá trị này độc lập với việc các bước quy về có đúng hay không (đó là câu hỏi khác, xem O4).

**Bộ lọc đã chạy**: 15 objection nháp ban đầu → cắt 3 (2 bị defeat bởi rebuttal có sẵn trong chính note gốc, 1 không thể state consequence rõ ràng) → 12 objection final ở mục 3.

## 3. Objections

**Cross-setup (Part 0.8) — báo cáo trước, vì mọi per-setup objection đều kế thừa từ đây.**

**O1 · [METHOD] · fatal · attacks C1 (load-bearing)**

Claim: "WR 77.3% (17W/5L trên 22 lệnh) là thước đo hiệu suất hệ thống ICT 2022 Model của người dùng."

Fails: Không có nhật ký survivorship. `aggregate_stats.md` và cả 5 batch summary không hề đề cập tới việc có bao nhiêu setup được xem xét, đạt một phần tiêu chí, hoặc bị bỏ qua trước khi 22 lệnh này được chọn để viết thành note đầy đủ. Backtest replay tự nó đã mang rủi ro hindsight (người viết biết trước outcome khi chọn ngày để phân tích) — nếu 22 ngày này được chọn một phần vì chúng "trông rõ ràng" trên chart (dễ nhận diện setup sau khi biết kết quả), mẫu thiên lệch về phía các setup dễ đọc = thường là các setup thắng rõ ràng.

Evidence: Không có counter-evidence trong toàn bộ 5 batch — chính `batchB.md` mục cross-trade pattern #2 và `batchE.md` mục 4 độc lập lưu ý rằng rất nhiều narrative "quá mượt" chỉ đứng vững nhờ biết outcome, cho thấy vấn đề chọn mẫu theo outcome là một khả năng thật, không phải suy đoán trừu tượng.

Consequence: Nếu đúng, WR 77.3% không đo được gì về edge thật của hệ thống — nó đo được "khả năng nhận ra setup rõ ràng khi nhìn lại", một kỹ năng khác hẳn "khả năng nhận ra setup đúng tại hard right edge trong live trading". Toàn bộ +37.16R không thể ngoại suy sang live performance.

Your best answer: "22 lệnh trải dài 2005-2026, nhiều symbol, nhiều năm khác nhau — khó có chuyện tất cả đều được chọn lọc có chủ đích theo outcome." Không cứu được: chọn lọc không cần *có chủ đích* để gây thiên lệch — chỉ cần trader có xu hướng lưu lại/viết note kỹ hơn cho các lệnh "đẹp" (dù thắng hay thua) đã đủ gây distortion; và một số ngày trùng lặp gần nhau (14/5 sáng + chiều, 19/5, cùng cụm XAUUSD) cho thấy ít nhất một phần mẫu được chọn theo chuỗi sự kiện liên tiếp trên cùng downtrend, không phải lấy mẫu ngẫu nhiên qua thời gian.

Retracted by: Một bảng log riêng liệt kê toàn bộ setup đã được xem xét trong quá trình backtest (kể cả các setup bị loại ngay từ bước 1-2 vì không đạt tiêu chí), với timestamp ghi trước khi biết outcome cuối. Không có bảng này, WR 77.3% giữ nguyên **[UNSUPPORTED]**.

**O2 · [METHOD] · fatal · attacks C4**

Claim: "4/5 lệnh Loss gần nhất là biểu hiện của MỘT lỗ hổng quy trình duy nhất — Unswept Liquidity Path."

Fails: Đây là kết luận rút ra sau khi biết cả 4 lệnh đều thua (narrative-fitting), theo đúng phân tích Devil's Advocate đã có sẵn trong chính note nguồn (mục 10 của [[2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]], objection O1 tại đó). Ba lý do: (i) không công bố mẫu số tổng số Loss trong vault (ở đây là chính xác 5/5, tức 100% theo cách đóng khung "4/5 lệnh gần nhất" — bỏ sót 05-02 khỏi phép đếm mà không giải thích tại sao); (ii) tiêu chí gộp nhóm ("SL nằm trong đường đi tới pool thanh khoản chưa bị lấy") gần như là mô tả mặc định của bất kỳ lệnh thua nào theo lens ICT — luôn tồn tại MỘT pool nào đó mà SL "nằm trên đường tới" nó; (iii) chưa test chéo tiêu chí này lên nhóm Win.

Evidence: Chính batch E mục 4 chỉ ra 2 lệnh Win trong cùng batch (07-16/02, 07-17/01) cũng có yếu tố "entry/tap nông" tương tự nhưng KHÔNG được kiểm tra xem có khớp tiêu chí "Unswept Liquidity Path" hay không.

Consequence: Nếu tiêu chí gộp nhóm không phân biệt được Win/Loss, "họ lỗi" này là một cách diễn đạt lại kết quả (thua) bằng ngôn ngữ ICT, không phải một phát hiện thật — tương đương nói "mọi lệnh thua đều thua vì giá đi ngược hướng dự đoán."

Your best answer: "first_error khác nhau ở bề mặt (sweep/poi/poi-SL/draw) chính là bằng chứng đã tìm ra tầng sâu hơn, không phải ép nhãn." Không cứu được: tính đa dạng bề mặt không loại trừ khả năng tiêu chí tầng sâu cũng chỉ là một cách mô tả lại "đã thua" — cần test chéo trên nhóm Win để phân biệt hai khả năng.

Retracted by: Áp đúng tiêu chí định lượng (không mô tả định tính) "SL nằm trong đường đi tới pool chưa lấy" lên toàn bộ 17 lệnh Win có đủ dữ liệu; nếu tỷ lệ khớp ở nhóm Win thấp hơn rõ rệt so với nhóm Loss, C4 được củng cố. Nếu tương đương, C4 bị bác.

**O3 · [METHOD] · fatal · attacks C5**

Claim: "Confluence score (0-8) và POI rank (8.1) đo được chất lượng setup."

Fails: Dữ liệu cấp sample tự mâu thuẫn với claim này. Theo mục 2 của [[00 - Backtest Dashboard & Statistics]]: Loss xuất hiện ở MỌI mức confluence (0, 1, 2, 3); lệnh Loss có confluence CAO NHẤT (3, [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short]]) lại thua; đồng thời 3 lệnh Win có confluence = 0 ([[2026-07-09/01 - Win - EURUSD - 2005-05-11- Short]], [[2026-07-10/01 - Win - EURUSD - 2021-05-03- Short]] — thực ra 1 —, và một phần của batch B). Một thước đo "chất lượng" mà không tách được kết quả tốt/xấu ở n=22 hoặc là (a) đang đo sai đại lượng, hoặc (b) cần mẫu lớn hơn rất nhiều để thấy tín hiệu qua nhiễu.

Evidence: `aggregate_stats.md` mục Key numbers dòng "Confluence score KHÔNG tách được win/loss" — đây là finding do chính hệ thống tổng hợp aggregate đã tự nhận diện, không phải suy diễn thêm ở đây.

Consequence: Nếu confluence_score không có giá trị dự báo, mọi quyết định trong tương lai dựa vào ngưỡng confluence (vd "chỉ vào lệnh khi confluence ≥ 3") không có cơ sở thực nghiệm từ chính 22 lệnh này.

Your best answer: "n=22 với chỉ 5 Loss là quá nhỏ để confluence score thể hiện giá trị thống kê — đây không phải bằng chứng phủ định, chỉ là thiếu công suất thống kê (statistical power)." Đúng một phần, ghi nhận ở Retracted by — nhưng thiếu công suất thống kê nghĩa là claim C5 phải hạ xuống UNSUPPORTED (chưa chứng minh được, theo cả hai chiều), không được nâng lên thành PASS ngầm định trong cách 22 note vẫn tiếp tục dùng confluence_score như một chỉ báo tin cậy.

Retracted by: Test correlation (hoặc đơn giản là bảng chéo) confluence_score × outcome trên ≥50 lệnh — nếu ở mẫu lớn hơn, phân phối Loss tập trung rõ ở confluence thấp, C5 được cứu; nếu vẫn trải đều, C5 bị bác chính thức.

**O4 · [METHOD] · material · attacks C3**

Claim: "5 lệnh Loss đều có first_error_step xác định rõ ràng, và đây là nguyên nhân đầy đủ của kết quả thua."

Fails: Rule drift trong cách gán `first_error_step` giữa các note. Ví dụ, [[2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short]] gán `first_error_step: poi` cho lỗi thực chất là đặt SL sai vị trí invalidation (một lỗi SL-anchoring, không phải POI-selection) — chính note gốc đã tự ghi chú rằng template 7-bước không có bước riêng cho "SL placement" nên phải ép lỗi này vào field `poi`. Tương tự, [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short]] cũng gán `poi` cho lỗi "chọn nhầm cấp độ trong stack" — hai lỗi về bản chất khác nhau (SL-anchoring vs POI-stack-priority) bị gộp chung một tên field.

Evidence: `batchD.md` Note 2 — "⚠️ Template 7-bước hiện KHÔNG có bước riêng cho Stop Loss placement... đây là khoảng trống đáng cân nhắc bổ sung vào template."

Consequence: `first_error_step: poi` xuất hiện 2 lần trong 5 Loss nhưng mô tả 2 cơ chế thất bại khác nhau — bất kỳ thống kê nào đếm "poi" như một loại lỗi duy nhất (vd trong bảng "lỗi → gate" ở [[02 - Master Lesson Learned]]) sẽ gộp nhầm hai nguyên nhân.

Retracted by: Bổ sung field `first_error_substep` hoặc field SL-placement riêng vào template, rồi backfill cho 5 lệnh Loss hiện có.

**O5 · [ARITHMETIC] · material · attacks C2**

Claim: "Tổng +37.16R và WR 77.3% là số liệu sạch, sẵn sàng dùng cho thống kê expectancy."

Fails: Ít nhất 4 trong 21 lệnh có R-multiple có nghi vấn arithmetic chưa giải quyết dứt điểm (xem mục 5 của [[00 - Backtest Dashboard & Statistics]]): [[2026-07-10/01 - Win - EURUSD - 2021-05-03- Short]] (r_multiple 3.075 vs RR trực tiếp 2.123, chênh ~1R — nghi số blended qua partial không minh bạch), [[2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short]] (r_planned 2.09 vs tính lại 2.34-2.36), [[2026-07-16/02 - Win - GBPUSD - 2014-06-25 - Long]] (r_planned 2.47 vs 2.373, do SL back-calculate ngược từ RR mục tiêu — vòng lặp tự tham chiếu).

Evidence: `batchB.md` mục 3, `batchD.md` Note 5, `batchE.md` mục 2 — cả ba độc lập xác nhận qua tính lại bằng công thức RR = |TP-entry|/|entry-SL|.

Consequence: Nếu dùng số RR blended/back-calculated thay vì RR đơn thuần từ entry/SL/TP gốc, tổng +37.16R có thể lệch vài R so với con số "sạch" — không đủ để đảo ngược kết luận tổng thể (vẫn dương rõ rệt) nhưng đủ để coi con số thập phân (37.16, không phải 37) là giả-chính-xác.

Retracted by: Tính lại toàn bộ 21 R-multiple bằng đúng một công thức thống nhất (không dùng số blended), công bố tổng mới.

**O6 · [HINDSIGHT] · material · attacks C6**

Claim: "2 lệnh Win có first_error_step: entry (Edge-entry) chứng minh bias/setup-selection quan trọng hơn entry precision."

Fails: Cả hai lệnh ([[2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]], [[2026-07-12/01 - Win - GBPUSD- 2024-12-04- Long]]) chỉ Win vì retrace không đủ sâu để phân biệt giả thuyết Edge-entry vs CE-entry — đây là outcome-as-evidence: biết trước rằng giá "chỉ" retrace tới đó rồi đảo chiều là thông tin chỉ có sau khi outcome đã xảy ra. Tại thời điểm entry, không có gì đảm bảo retrace sẽ dừng đúng ở mức đó.

Evidence: `batchC.md` mục 4 — "Outcome Win không chứng minh entry đúng — nó chỉ chứng minh retrace không đủ sâu để kiểm định giả thuyết"; đối với GBPUSD, chính note tự tính `rr_if_ce = 5.31` so với `r_multiple` thực nhận 3.4 — chi phí cơ hội ~1.9R đo được bằng số nếu giả thuyết Edge-entry sai trong một lần lặp lại khác.

Consequence: C6 không thể dùng làm bằng chứng ủng hộ Edge-entry như một kỹ thuật — ngược lại, cả hai note gốc tự đề xuất Grade tối đa = B cho loại lỗi này cho tới khi có ≥20 mẫu.

Retracted by: ≥20 mẫu Edge-entry với retrace đủ sâu để thực sự phân biệt Edge vs CE, đo tỷ lệ Edge sống sót so với CE. Xem chi tiết ở [[../Case Studies/CS-02 - Edge entry vs CE entry|CS-02]].

**O7 · [SELF-CONTRADICTION] · material · attacks C1 (rule drift)**

Claim: "Chuẩn đánh giá 'sweep' được áp dụng nhất quán xuyên 22 lệnh."

Fails: `batchD.md` mục cross-trade finding #1 xác nhận "sweep" bị dùng theo 2 chuẩn khác nhau, xuất hiện ≥3/5 lần trong riêng cụm XAUUSD — đôi khi là resting liquidity có tên cụ thể (đúng canon), đôi khi chỉ là "giá chạm cạnh một PD array khác" không kèm tên level. Đây là rule drift **hệ thống**, không phải một lần nhầm lẫn cá biệt.

Evidence: `batchD.md`, note 01/02/05 đều có `idm_swept`/`liquidity_swept = Yes` không kèm tên level cụ thể.

Consequence: Bất kỳ thống kê nào dựa vào field `liquidity_swept`/`idm_swept` như một biến nhị phân đáng tin đều đang trộn hai định nghĩa khác nhau của "sweep" — làm suy yếu độ tin cậy của mọi phân tích downstream dùng field này (bao gồm cả chính C4/O2 ở trên).

Retracted by: Backfill lại toàn bộ field `liquidity_swept`/`idm_swept` cho 22 lệnh, mỗi giá trị Yes phải kèm tên level cụ thể (PDH/PDL/EQH/EQL/session level); loại field nào không kèm được tên thành `AMBIGUOUS` thay vì `Yes`.

**O8 · [SELF-CONTRADICTION] · material · attacks C1 (grade drift)**

Claim: "Grade được chấm theo một chuẩn nhất quán cho lỗi cùng loại."

Fails: `batchC.md` mục 4 xác nhận doctrine drift trực tiếp: [[2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]] giữ Grade A dù `first_error_step: entry`, trong khi [[2026-07-12/01 - Win - GBPUSD- 2024-12-04- Long]] tự hạ Grade A→B cho cùng loại lỗi (entry chưa kiểm định). Cùng tiêu chí ("lỗi entry chưa kiểm định → hạ grade") được áp dụng không nhất quán giữa 2 case trong cùng batch.

Evidence: Trích trực tiếp `batchC.md`: "Cùng một tiêu chuẩn... được áp dụng không nhất quán giữa 2 case cùng batch — đề xuất dùng chuẩn GBPUSD (nghiêm hơn) làm baseline."

Consequence: Nếu Grade không nhất quán, phân phối Grade (A/A-/B+/B/B-/C+/C/D) trong bảng dashboard không thể dùng để so sánh "chất lượng trung bình" giữa các cụm lệnh — grade phản ánh một phần chuẩn của người chấm tại thời điểm chấm, không chỉ chất lượng lệnh.

Retracted by: Backfill lại Grade cho toàn bộ 22 lệnh theo đúng MỘT chuẩn công bố trước (đề xuất: chuẩn GBPUSD 07-12, tức hạ Overall Grade tối đa xuống B cho mọi `first_error_step` khác `none`), rồi so sánh phân phối Grade mới với phân phối cũ.

**O9 · [HINDSIGHT] · material · attacks C2 (5 note đầu)**

Claim: "5 note Win đầu tiên (07-01→07-07, đều Grade A) đóng góp hợp lệ vào WR 77.3%."

Fails: Theo `batchA.md`, cả 5/5 note này có MSS/displacement M5 (claim load-bearing) chỉ mô tả bằng lời, không kèm giá đóng nến cụ thể — và cả 5/5 đều có câu dạng "thắng vì chờ đầy đủ điều kiện" viết trong phần replay SAU khi biết outcome, không có bằng chứng tách bạch được ghi trước/sau khi biết kết quả.

Evidence: `batchA.md` Pattern #1 và #2 — "UNPROVEN đồng loạt ở cả 5 note... không note nào có bằng chứng tách bạch thời điểm ghi chú trước/sau khi biết kết quả."

Consequence: 5/17 Win (gần 30% số lệnh Win) đóng góp vào WR không thể được phân biệt khỏi khả năng "được chọn và viết lại vì biết trước là Win". Xem [[../Case Studies/CS-05 - Outcome bias va hindsight|CS-05]] cho phân tích đầy đủ.

Retracted by: Không thể retract hồi tố (outcome đã biết, không thể tái tạo trạng thái "chưa biết" cho 5 note này) — chỉ có thể ngăn ngừa ở các note tương lai bằng quy trình ghi chú tại hard right edge (đề xuất ở CS-05).

**O10 · [UNSUPPORTED] · minor · attacks C1**

Claim ngầm định: Việc XAUUSD chiếm 4/22 lệnh đều nằm trong cùng một downtrend liên tiếp (12/5, 14/5 sáng, 14/5 chiều, 19/5/2014) không ảnh hưởng tới tính độc lập của các quan sát.

Consequence: minor — 4 lệnh không hoàn toàn độc lập về mặt thống kê (cùng regime thị trường, bias D1/H1 được "tái dùng gần nguyên văn" theo `batchD.md` Note 3), nên n=22 hiệu dụng (effective sample size) nhỏ hơn 22 khi tính độ tin cậy của bất kỳ tỷ lệ nào tách theo symbol.

Retracted by: Gắn nhãn cụm ("cluster_id") cho các lệnh cùng chuỗi sự kiện liên tiếp khi tính thống kê, dùng effective sample size thay vì đếm thô.

**O11 · [UNSUPPORTED] · minor · attacks C5**

Claim: BPR (Balanced Price Range) được thống kê chung với FVG trong bảng POI vì field `poi_type` chuẩn không có lựa chọn riêng cho BPR.

Consequence: minor — hai lệnh BPR ([[2026-07-09/01 - Win - EURUSD - 2005-05-11- Short]], [[2026-07-14/03 - Win - XAUUSD- 2014-05-14 - Short]]) được tính vào nhóm "FVG 8W/1L" trong dashboard dù về cấu trúc là 2-FVG-chồng-nhau, không phải FVG đơn — không đổi kết luận chung (FVG/BPR vẫn thắng nhiều) nhưng làm giảm độ chính xác của phép so sánh "FVG đơn vs cấu trúc ghép".

Retracted by: Thêm `poi_type: BPR` vào controlled vocabulary, tách lại thống kê.

**O12 · [ARITHMETIC] · minor · attacks C2**

Claim: Lệnh #20 ([[2026-07-16/02 - Win - GBPUSD - 2014-06-25 - Long]]) thiếu `r_multiple` (None) không ảnh hưởng tới thống kê tổng.

Consequence: minor — mẫu R-multiple thực tế là n=21 chứ không phải n=22, đã được `aggregate_stats.md` ghi đúng, nhưng cần nhắc lại mỗi khi trích dẫn "tổng 22 lệnh" để tránh ai đó hiểu nhầm 37.16R là trung bình của cả 22.

Retracted by: Đã tự retract — `aggregate_stats.md` đã ghi rõ "trên 21 lệnh có số".

**Bộ lọc đã áp dụng**: 15 objection nháp → 12 objection final (3 bị cắt: 1 trùng lặp với O7, 1 không có consequence rõ ràng — chỉ là quan sát style viết, 1 bị chính rebuttal trong note gốc defeat hoàn toàn trước khi tới đây).

## 4. Opposite case

**Load-bearing claim bị đảo**: thay vì "22 lệnh chứng minh hệ thống 7-bước có edge 77.3% WR", đọc ngược cùng dữ liệu: "22 lệnh là một tập hợp các buổi tự-phê-bình chi tiết, trong đó người viết học được nhiều framework ICT hơn theo thời gian (rõ nhất ở tiến triển 07-01→07-07 theo `batchA.md` Pattern #4), nhưng WR 77.3% là sản phẩm phụ của việc chọn ngày để viết note (có thể thiên về các setup dễ đọc lại = thường là setup thắng), không phải bằng chứng cho một edge có thể tái lặp trong live trading."

**Load-bearing claim của opposite case**: sự tiến triển chất lượng phân tích (concept vocabulary phong phú hơn, tự sửa lỗi số nhiều hơn) là có thật và quan sát được trực tiếp — nhưng tiến triển về *chất lượng ghi chép* không đồng nghĩa tiến triển về *edge thật*, hai đại lượng độc lập.

**Tự phản biện case ngược**: Case này có một điểm yếu — nếu người viết chọn mẫu để "học", không phải để "chứng minh WR cao", thì động cơ thiên lệch theo hướng ngược lại (chọn cả setup khó, kể cả setup thua, để học được nhiều nhất) cũng hợp lý ngang, và thực tế 5/22 là Loss (không phải 0/22) cho thấy người viết không né tránh hoàn toàn việc ghi lại thất bại.

**Nhãn: equally viable.** Không đủ observable để phân biệt hai case chỉ từ 22 note đã biết outcome — cả hai đọc y hệt cùng một tập dữ liệu.

**Observable phân biệt được hai case**: một nhật ký độc lập (viết TRƯỚC khi biết outcome, ví dụ bằng timestamp file hoặc bằng ghi chú tại hard right edge) liệt kê MỌI setup đã được xem xét trong quá trình backtest — kể cả những setup bị loại ngay từ vòng đầu. Nếu nhật ký đó tồn tại và cho thấy tỷ lệ loại-bỏ tương đương giữa setup "trông sẽ thắng" và "trông sẽ thua", case gốc (C1 đúng, WR có ý nghĩa) được củng cố mạnh. Nếu nhật ký không tồn tại (tình trạng hiện tại), không thể phân biệt.

## 5. Verdict

**UNPROVEN.** Không có claim nào bị BROKEN dứt khoát bằng chart evidence (vì không có chart evidence ở tầng cross-setup này) — nhưng load-bearing claim C1 (provenance của sample) không được chứng minh, và O1 (fatal) cho thấy WR 77.3% không thể tách khỏi giả thuyết ngược (selection bias). Theo đúng quy tắc brief: **"WR 77.3% là [UNSUPPORTED] nếu không chứng minh được [provenance]"** — provenance không được chứng minh trong bất kỳ file nào đã đọc, nên nhãn đúng là UNPROVEN, không phải SURVIVES.

**Điều tôi tấn công và không phá được**: kỷ luật cắt lỗ (5/5 đúng -1R) và xu hướng tự sửa lỗi tăng dần theo thời gian — cả hai đứng vững độc lập với câu hỏi WR có ý nghĩa hay không.

**Điều phân tích này KHÔNG xác lập được**: (1) liệu 22 lệnh có đại diện cho toàn bộ các lần người dùng cố áp dụng ICT 2022 Model hay không; (2) liệu "họ lỗi Unswept Liquidity Path" có sức phân loại Win/Loss thật hay chỉ là mô tả lại của outcome; (3) liệu confluence_score/POI rank có giá trị dự báo ở mẫu lớn hơn — n=22 không đủ để bác bỏ CŨNG không đủ để xác nhận.

## 6. Falsification tests (tối đa 3)

1. **Test provenance (đóng O1).** Công bố nhật ký toàn bộ setup đã xem xét trong giai đoạn backtest 2026-07-01→2026-07-18 (kể cả setup bị loại), với timestamp trước outcome. Nếu tỷ lệ "được viết thành note" giữa setup-trông-sẽ-thắng và setup-trông-sẽ-thua là tương đương (chênh <15 điểm phần trăm), O1 bị rút; nếu chênh lệch lớn, O1 được xác nhận và WR 77.3% chính thức bị dán nhãn không đại diện.
2. **Test cross-validate "họ lỗi" trên nhóm Win (đóng O2).** Áp đúng tiêu chí định lượng "SL nằm trong đường đi tới pool thanh khoản chưa bị lấy, cách X pip hoặc Y% dealing range" (cần định nghĩa X/Y trước khi chạy test) lên toàn bộ 17 lệnh Win. Nếu ≥40% lệnh Win cũng khớp tiêu chí này, C4 (họ lỗi Unswept Liquidity Path có sức phân loại) bị bác; nếu <15% lệnh Win khớp, C4 được củng cố mạnh.
3. **Test confluence score trên mẫu lớn hơn (đóng O3).** Thu thập thêm ≥30 lệnh mới (giữ nguyên field `confluence_score`), chạy correlation đơn giản (hoặc bảng chéo 2×2: confluence ≥3 vs <3, Win vs Loss) trên tổng ≥52 lệnh. Nếu Loss tập trung rõ rệt ở confluence thấp (vd >70% Loss có confluence <2), O3 bị rút và confluence_score được xác nhận có giá trị dự báo ở mẫu lớn hơn; nếu phân phối vẫn trải đều như ở n=22, O3 được củng cố thành finding chính thức: confluence_score hiện tại cần thiết kế lại.

## 7. Action items

- [ ] Yêu cầu/tạo nhật ký survivorship cho các batch backtest tương lai (setup bị loại cũng phải log).
- [ ] Backfill field `liquidity_swept`/`idm_swept` với tên level cụ thể cho toàn bộ 22 lệnh (đóng O7).
- [ ] Backfill Grade theo một chuẩn thống nhất công bố trước (đóng O8) — đề xuất dùng chuẩn 07-12 (GBPUSD) làm baseline.
- [ ] Chạy lại RR cho 4 lệnh có nghi vấn arithmetic ở O5 bằng một công thức thống nhất, công bố tổng R mới.
- [ ] Thêm field `poi_type: BPR` vào controlled vocabulary (đóng O11).
- [ ] Thiết kế lại confluence_score hoặc thu thập thêm mẫu trước khi dùng nó làm gate quyết định (test 3).

Hypotheses to check (not objections):
- Có thể XAUUSD (2W/2L) đang cho tín hiệu thật rằng hệ thống kém hiệu quả hơn trên symbol có biến động khác EURUSD, nhưng n=4 quá nhỏ để tách khỏi nhiễu ngẫu nhiên.
- Có thể "London Open KZ"/"NY AM" có edge cao hơn "Asia" thật, nhưng n=1 cho Asia không cho phép kết luận — cần thêm mẫu Asia trước khi loại bỏ session này khỏi playbook.

## Liên kết

- [[00 - Backtest Dashboard & Statistics]]
- [[02 - Master Lesson Learned]]
- [[../Case Studies/CS-01 - Ho loi Trading Into Unswept Liquidity|CS-01]] · [[../Case Studies/CS-02 - Edge entry vs CE entry|CS-02]] · [[../Case Studies/CS-03 - Nghich ly POI rank|CS-03]] · [[../Case Studies/CS-04 - MSS som va sweep 2 chuan|CS-04]] · [[../Case Studies/CS-05 - Outcome bias va hindsight|CS-05]]
- Nguồn: `analysis_summaries/aggregate_stats.md`, `analysis_summaries/batchA.md` → `batchE.md`, note gốc [[2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] mục 9-10
