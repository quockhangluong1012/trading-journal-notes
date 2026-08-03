---
date: 2026-05-01
symbol: NDX
position: Long
result: Win
session: London
setup: "[[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model|ICT 2022 Model]]"
entry_model: Sell-side Liquidity + Liquidity Sweep/Stop Hunt + Order Blocks
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 27,433
take_profit: 27,473.2
stop_loss: 27,415.02
exit_price: 27,475
pnl: 155.4
r_multiple: 2.34
planned_rr: 2.24
risk_percent: 5%
confidence: 4
mistakes:
emotions:
  - Disciplined
tags:
  - SellSideLiquidity
  - LiquiditySweepStopHunt
  - OrderBlocks
  - FairValueGap
  - KillZones
  - JudasSwing
  - DailyBias
source_id: 2016
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 2, material: 1, minor: 0}
da_opposite_case: undecidable from this evidence
---
# Trade 2026-05-01 - NDX Long Win

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Win |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Sell-side Liquidity + Liquidity Sweep/Stop Hunt + Order Blocks |
| HTF Bias |  |
| Premium/Discount |  |
| Power of 3 |  |
| Confidence | 4/5 (High) |
| Entry | 27,433 |
| Stop Loss | 27,415.02 |
| Take Profit | 27,473.2 |
| Exit | 27,475 |
| PnL | 155.4 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-05-03 05:05:00 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: N/A
- **Premium/Discount**: N/A
- **Power of 3 Phase**: N/A

=============== D1 ===============

- Giá đang trong xu hướng tăng (Bullish)
=============== H1 ===============

- Giá đang di chuyển trong 1 nhịp PullBack sau khi phiên Asia tạo 1 đỉnh
- Xuống khung M15 quan sát
=============== M15 ===============

- Giá di chuyển về 1 Order Block trên khung M15 (được tạo từ phiên New York ngày trước)
- Giá quét xuống dưới đáy OB + đáy cũ (27408)
- Sau khi quét xong giá quay ngược vào range và tăng
=============== M5 ===============

- Entry

### Charts

![[NDX-20260501-2016-1.png]]
![[NDX-20260501-2016-2.png]]
![[NDX-20260501-2016-3.png]]
![[NDX-20260501-2016-4.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Market Structure Shift + Displacement
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Rejection Validation When Enter PD Array Zones
- [x] Risking no more than 0.5% of account equity
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Not exceeding daily loss limit -- will stop trading if hit

---

## 3. Execution Review

- Exit vội khi qua vừa chạm đỉnh cũ
- Quan sát đầu hiệu reject khi giá chạm thay vì exit trade liền

**Emotions**: Disciplined

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit)
- **Mistake chính**:
  - [[Mistake - ]] *(trống trong bản gốc — Execution Review tự nêu: "Exit vội khi qua vừa chạm đỉnh cũ" — mistake phù hợp là early-exit trước khi quan sát đủ tín hiệu reject, khớp trực tiếp với chính lời tự phê (suy luận có điều kiện — cần chart xác nhận vị trí đỉnh cũ so với TP đã đặt))*
- **Nguyên nhân gốc rễ**:
  - *(trống trong bản gốc)* Tự nêu trong mục 3: exit theo cảm giác khi chạm đỉnh cũ, không chờ tín hiệu reject xác nhận — mâu thuẫn với việc TP kế hoạch (27,473.2) và exit thực tế (27,475) gần như trùng khớp (chỉ chênh 1.8 điểm), nên "exit vội" ở đây có thể chỉ là tự phê về TÂM LÝ trong lúc giữ lệnh, không phải sai lệch số liệu — cần soi ở mục 8 vì đây gần khớp TP kế hoạch, không phải early-exit thực sự làm giảm lãi.

---

## 5. Lesson Learned

**Bài học kỹ thuật**
- Checklist tick "Risking no more than 0.5% of account equity" `[x]` NHƯNG frontmatter ghi `risk_percent: 5%` — mâu thuẫn trực tiếp trong cùng file, không phải suy luận. Liên kết O1 (load-bearing, [SELF-CONTRADICTION] fatal, trích CS-O1).
- SL đặt cách entry chỉ 17.98 điểm (27,433 − 27,415.02) trên NDX — cần đối chiếu doctrine "SL beyond nearest structure level + Buffer" xem khoảng cách này có đủ chỗ cho buffer thực tế trên một chỉ số có biến động M5 thường >15-20 điểm hay không. Liên kết O2.

**Bài học tâm lý**
- "Exit vội khi vừa chạm đỉnh cũ" là tự phê hợp lý CHO MỤC ĐÍCH HỌC, nhưng đây là lệnh WIN — outcome không chứng minh quy trình exit đúng hay sai; vì exit_price (27,475) gần sát TP kế hoạch (27,473.2), "exit vội" không đồng nghĩa với "để mất lợi nhuận đáng kể". Cảm giác "vội" có thể là một nhãn tâm lý áp lên một quyết định thực chất gần tối ưu.

**Bài học quy trình & risk**
- Đây là 1 trong 8 lệnh trong toàn sample có `risk_percent: 5%` (10× ngưỡng 0.5% công bố trong chính checklist của lệnh này) — theo cross_setup_findings (CS-O1), lệnh này thuộc nhóm 4/8 KHÔNG tự gắn mistake tag risk breach, trái với 4/8 lệnh khác có cùng risk_percent nhưng tự nhận đó là lỗi. Liên kết O1.
- Frontmatter của lệnh này có đầy đủ field hiếm thấy trong cụm 27/04-29/04: `entry_timeframe: M5`, `higher_timeframe_bias: D1`, `bias_correct: Bullish` — đây là lệnh chuẩn hóa dữ liệu tốt nhất trong nhóm 5 lệnh được giao, nhưng chính sự chuẩn hóa đó làm lộ rõ mâu thuẫn risk 5% vs checklist 0.5% mà các lệnh thiếu field khác không thể hiện rõ ràng bằng.

**Rule cần thêm/cập nhật**
- Rule 1: Khi `risk_percent` ghi khác 0.5%, checklist item "Risking no more than 0.5%" phải để `[ ]` (unchecked) hoặc có ghi chú giải thích rõ lý do sai khác — điều kiện đo: hai field này phải logic-nhất-quán, kiểm bằng script so khớp risk_percent với trạng thái tick. Liên kết O1.
- Rule 2: SL trên NDX (biến động cao) phải có buffer tối thiểu bằng số (ví dụ ≥0.3× ATR M5 hoặc ≥1 lần khoảng dao động trung bình của nến M5 gần nhất) trước khi coi là "beyond structure + Buffer" — điều kiện đo: khoảng cách entry-SL phải ≥ ngưỡng ATR đã định trước, không chỉ dựa cảm tính "vừa dưới OB". Liên kết O2.
- Rule 3: Không gắn nhãn tâm lý tiêu cực ("exit vội") cho một quyết định exit khi exit_price nằm trong phạm vi ±2 điểm của TP kế hoạch trên NDX — điều kiện đo: chênh lệch exit vs TP kế hoạch phải vượt một ngưỡng % biên độ trước khi coi là "vội"/lỗi thực thi.

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, không screenshot khả dụng → cấm [CHART]. "MSS", "OB", "Liquidity Sweep/Stop Hunt" là claim của user. Sufficiency: **thin** — nhưng lệnh này có frontmatter đầy đủ hơn 4 lệnh khác trong nhóm được giao (có `entry_timeframe`, `higher_timeframe_bias`, `bias_correct`), nên phần đối chiếu field-vs-field ở đây có cơ sở tốt hơn, dù vẫn không có chart để kiểm structure thật.

**Thesis & claims**:
- C1: D1 bias Bullish (frontmatter xác nhận `bias_correct: Bullish`).
- C2: H1 — pullback sau đỉnh phiên Asia.
- C3: M15 — giá về OB (tạo từ NY phiên trước), quét xuống dưới đáy OB + đáy cũ (27,408), sau đó quay lại vào range và tăng.
- C4: M5 — entry long tại 27,433 (không có narrative M5 nào khác ngoài chữ "Entry"). **Load-bearing**: cả thesis dựa vào C3 (sweep dưới 27,408 là liquidity sweep hợp lệ) VÀ vào giả định risk-management đã tuân thủ ngưỡng 0.5% mà chính checklist của file này tick — hai load-bearing riêng biệt: một về structure (C3), một về risk (checklist item risk).
- C5 (hệ quả): entry long 27,433, SL 27,415.02 (khoảng cách 17.98 điểm), TP 27,473.2 là một setup hợp lệ đầy đủ theo ICT 2022 model, risk quản lý đúng chuẩn (theo tick checklist).

**Điều gì đứng vững**: Đây là lệnh duy nhất trong 5 file được giao có field `entry_timeframe`, `higher_timeframe_bias`, `bias_correct` điền đầy đủ và nhất quán với narrative (D1 Bullish khớp `bias_correct: Bullish`) — không có mâu thuẫn bias như thấy ở `Loss-02-2026-04-28`. Trình tự D1→H1→M15→M5 đúng thứ tự nesting, không nhảy cóc timeframe. Câu chuyện sweep dưới đáy cũ 27,408 rồi quay lại range là một cấu trúc liquidity-sweep-then-reversal mạch lạc về mặt narrative (dù không kiểm được bằng chart).

**Objections**:

**O1 · [SELF-CONTRADICTION] · fatal · attacks C5 (load-bearing) — trích CS-O1**
Claim: lệnh này tuân thủ đúng quy tắc quản lý risk 0.5%/lệnh (checklist mục 2 tick `[x]` "Risking no more than 0.5% of account equity").
Fails: frontmatter cùng file ghi `risk_percent: 5%` — gấp 10 lần ngưỡng mà chính checklist của file này vừa tick là đã tuân thủ. Đây đúng là finding **CS-O1** trong cross_setup_findings (risk 5% xuất hiện ở 8/25 lệnh sample, rule drift ở cấp tự-chấm-điểm) — lệnh này (`Win-01-05-01-NDX`) thuộc nhóm 4/8 KHÔNG tự gắn mistake tag cho breach này, khác với 4/8 lệnh khác cùng risk_percent nhưng tự nhận là lỗi.
Evidence: `risk_percent: 5%` (frontmatter, dòng 19) vs checklist dòng "Risking no more than 0.5% of account equity" `[x]` (mục 2) — hai giá trị trực tiếp mâu thuẫn trong cùng một file, không cần suy diễn.
Consequence: risk thật của lệnh (5%, không phải 0.5%) làm pnl $155.4 không so sánh được theo cùng đơn vị R với các lệnh risk 0.5% khác trong sample — và vì lệnh này KHÔNG tự gắn mistake tag breach (khác 4/8 lệnh có tag), rule drift ở cấp tự-chấm-điểm không giải thích được bằng "Win thì không cần flag, Loss thì flag" (theo CS-O1, cả nhóm có-tag và không-tag đều có Win lẫn Loss).
Your best answer: "5% risk_percent áp cho một sub-account nhỏ khác quy mô, không phải 5% tổng account đo bằng 0.5% rule." — Không cứu được theo đúng lập luận CS-O1: chính mistake tag 07 (dùng ở 4/8 lệnh khác cùng field) viết rõ "Risk more than 0.5% total account", và không có ghi chú nào trong lệnh này phân biệt sub-account.
Retracted by: một ghi chú xác nhận risk_percent 5% trong file này đo trên một account/sub-account khác quy mô với account dùng để tính 0.5% — hiện không có (đúng như CS-O1 đã kết luận ở cấp sample).

**O2 · [DOCTRINE] · fatal · attacks C3, C5 (load-bearing structure)**
Claim: SL 27,415.02 (cách entry 27,433 đúng 17.98 điểm) là "placed beyond the nearest structure level + Buffer" (checklist tick `[x]`, đúng dòng cuối mục 2).
Fails: doctrine ICT về SL placement yêu cầu SL nằm ngoài structure invalidation level VÀ có buffer đủ để tránh bị quét bởi biến động thông thường (noise) — không chỉ nằm "dưới OB". NDX là chỉ số biến động cao; một SL 17.98 điểm là khoảng cách tương đối hẹp so với range nến M5/M15 thường thấy trên NDX (dao động range M15 nhiều thời điểm london/NY vượt 20-30 điểm). File không nêu con số cụ thể nào để chứng minh 17.98 điểm đã bao gồm buffer sau structure — chỉ nói "quét xuống dưới đáy OB + đáy cũ (27,408)" mà KHÔNG nói entry/SL nằm ở đâu so với 27,408: entry 27,433 đã CAO HƠN 27,408 tới 25 điểm, và SL 27,415.02 vẫn cao hơn 27,408 tới 7.02 điểm — nghĩa là SL không hề nằm bên dưới đáy cũ 27,408 đã nêu, mà nằm PHÍA TRÊN mức đó.
Evidence: 27,415.02 (SL) − 27,408 (đáy cũ tự ghi) = +7.02 điểm — SL nằm cao hơn structure level được nêu là "đáy cũ", không phải "beyond" (bên ngoài/dưới) nó. Nếu chuẩn doctrine là SL phải nằm dưới đáy cũ (để invalidation thật xảy ra khi giá phá đáy đó), SL 27,415.02 không đạt chuẩn này — nó nằm giữa entry và đáy cũ, không nằm ngoài đáy cũ.
Consequence: nếu doctrine yêu cầu SL dưới 27,408 (có buffer), SL thật cần thấp hơn nhiều so với 27,415.02 — khoảng risk thật theo chuẩn "beyond structure" có thể lớn hơn 17.98 điểm đáng kể, làm RR thật thấp hơn 2.24 đã ghi. Đây khớp trực tiếp với pattern **CS-O5** trong cross_setup_findings (RR "đẹp" là artifact của SL siết chặt, không phải chất lượng setup — ở đó là case GBPUSD SL 3.6 pips/RR 6.14; ở đây là case NDX SL 17.98 điểm nằm sai phía so với structure level tự ghi).
Your best answer: "27,408 là đáy cũ của một swing nhỏ hơn, không phải structure level dùng để đặt SL — SL thực dựa trên OB M15 gần entry hơn." — Có thể đúng, nhưng file không nêu giá cụ thể của cạnh dưới OB M15 để kiểm; nếu cạnh dưới OB M15 nằm sát 27,415, thì buffer thực tế gần như bằng 0 (SL ngay tại structure, không "beyond" nó).
Retracted by: giá cụ thể của cạnh dưới OB M15 (không phải 27,408 "đáy cũ") kèm xác nhận SL 27,415.02 nằm bên ngoài (thấp hơn) mức đó với buffer hợp lý — hiện không có trong file.

**O3 · [ARITHMETIC] · material · attacks C5**
Claim: pnl $155.4 phản ánh đúng chuyển động giá đã ghi (entry 27,433 → exit 27,475).
Fails: exit − entry = 42.0 điểm, nhưng pnl = 155.4 → tỷ lệ pnl/điểm = 3.7 — khác hoàn toàn tỷ lệ 1.0 ở hai lệnh Loss trong cụm liền trước (04-27, 04-29), và khác cả tỷ lệ 0.77 ở Win-01-04-28. Đây là lệnh DUY NHẤT trong 5 file có `risk_percent` ghi rõ (5%), và cũng là lệnh có tỷ lệ pnl/điểm cao nhất (3.7) — phù hợp về HƯỚNG với giả thuyết "risk cao hơn → pnl $ khuếch đại hơn trên cùng số điểm", nhưng 3.7 không phải đúng 10× (nếu 5% so với 0.5% chuẩn phải là hệ số 10, không phải 3.7).
Evidence: 27,475 − 27,433 = 42.0 điểm; pnl = 155.4; 155.4/42.0 = 3.7 — không khớp hệ số 10× dự kiến nếu baseline 4 lệnh khác dùng đúng 0.5%.
Consequence: không thể dùng tỷ lệ pnl/điểm để xác nhận hay bác bỏ risk_percent 5% có được áp dụng thực tế đúng cách hay không — hệ số 3.7 nằm giữa 1.0 (baseline ngờ là 0.5% chuẩn) và 10 (nếu đúng 5%/0.5%=10), không khớp rõ với giả thuyết nào.
Your best answer: "công thức tính pnl bao gồm cả phí/slippage/rounding, không thuần túy hệ số risk." — Hợp lý, hạ objection xuống material vì không đổi được kết luận chính của O1 (mâu thuẫn field risk_percent vs checklist tick vẫn đứng độc lập, không cần dựa vào O3).
Retracted by: contract/lot-size field xác nhận hệ số quy đổi điểm→$ cho lệnh này — hiện không có.

Drafted 4, cut 1 (draft về "confidence 4/5 cao dù risk 5%" bị cắt vì trùng lặp nội dung đã bao trong O1, không có consequence riêng).

**Verdict: BROKEN.** Hai load-bearing claim đều sụp: (a) risk-management claim tự mâu thuẫn ngay trong file (risk_percent 5% vs checklist tick 0.5%, O1 fatal, trích CS-O1); (b) structure claim về SL "beyond nearest structure + Buffer" tự mâu thuẫn với chính con số đáy cũ (27,408) mà file nêu — SL 27,415.02 nằm CAO HƠN, không phải THẤP HƠN, mức đáy cũ đó (O2, fatal). Tôi đã tấn công nhưng không phá được: trình tự D1→H1→M15→M5 đúng thứ tự, bias field nhất quán (hiếm trong nhóm 5 file), và câu chuyện sweep-rồi-reversal ở M15 mạch lạc về narrative. Critique này KHÔNG xác lập: (1) liệu OB M15 thật có cạnh dưới ở đâu — không có chart, có thể SL thực ra đặt đúng ngoài OB M15 (khác đáy cũ 27,408); (2) liệu risk 5% có phải lỗi ghi chép field hay là breach thật — theo CS-O1 (cross-setup), không có bằng chứng nào trong 27 file phân biệt được hai khả năng này cho bất kỳ lệnh nào trong nhóm 8 lệnh risk 5%, và lệnh này không tự gắn mistake tag khiến câu hỏi đó vẫn mở.

---

## 9. Opposite Case (Counter-Argument)

Đổi vai trò: "quét xuống dưới đáy OB + đáy cũ (27,408)" — mà thesis gốc coi là liquidity sweep hợp lệ mở đường cho long — có thể đọc thành **giá chỉ test lại (không thực sự sweep-and-reject) một vùng đã từng là support, và cú tăng sau đó là một phản ứng ngắn hạn trong một pullback D1 chưa kết thúc**, với TP 27,473.2 chỉ là một đỉnh cũ gần (không phải target liquidity lớn của D1). Dưới reading này, Win 155.4 là một scalp đúng hướng ngắn hạn trong nhiễu của pullback, không phải xác nhận đầy đủ một liquidity-sweep-reversal setup như thesis gốc mô tả — và may rủi đóng vai trò lớn hơn skill, vì SL đặt sai phía structure (O2) mà vẫn không bị quét chỉ là kết quả thuận lợi của biến động ngắn hạn.

Load-bearing claim của kèo ngược: cú "sweep" dưới 27,408 chỉ là noise/test bình thường trong pullback, TP 27,473.2 chỉ là mức kỹ thuật gần, không phải DOL thật của D1 bias.

Tự đánh kèo ngược: kèo ngược này không giải thích được TẠI SAO giá đảo chiều đúng ngay tại vùng OB M15 (được tạo từ phiên NY trước) như narrative mô tả — nếu chỉ là noise ngẫu nhiên, việc giá phản ứng chính xác tại một OB đã được định danh trước (không phải một mức bất kỳ) là một trùng hợp cần giải thích thêm mà kèo ngược không có.

**Strength label: undecidable from this evidence.** Không có chart để xác nhận độ chính xác của phản ứng giá tại OB M15, và không có cách nào phân biệt "sweep hợp lệ mở đường cho reversal thật" khỏi "test noise trong pullback" chỉ từ text — cả hai đều tương thích với toàn bộ dữ liệu đã cho.

**Observable phân biệt hai reading**: liệu vùng giá 27,473.2 (TP) có phải một liquidity pool đã được named cụ thể trên D1/H1 (ví dụ buy-side liquidity của một swing high lớn) — nếu có, thesis gốc (sweep-reversal hướng tới DOL thật) đứng; nếu 27,473.2 chỉ là một đỉnh cũ gần không gắn với cấu trúc D1 lớn hơn, kèo ngược (scalp trong noise pullback) đứng.

---

## 10. Falsification Tests

1. **Test đóng O1**: xác nhận risk_percent 5% trong lệnh này (và 7 lệnh khác cùng field trong sample) đo trên account nào — nếu có bằng chứng đây là một sub-account tách biệt với quy mô khác 0.5% rule, O1 đóng theo hướng "không phải breach thật"; nếu không, O1 giữ fatal và mở rộng thành finding hệ thống (đã có ở CS-O1).
2. **Test đóng O2**: xác nhận giá cụ thể của cạnh dưới OB M15 dùng để đặt SL 27,415.02 — nếu cạnh đó thấp hơn 27,415.02 với buffer hợp lý (không phải đáy cũ 27,408), O2 hạ xuống material; nếu cạnh OB M15 cũng nằm trên hoặc rất gần 27,415.02, O2 giữ fatal.
3. **Test đóng Opposite Case**: xác nhận 27,473.2 có phải một liquidity pool named trên D1/H1 — có → nâng opposite case xuống "not viable" (thesis gốc thắng rõ); không có → giữ "undecidable".
