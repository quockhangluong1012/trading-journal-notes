---
date: 2026-05-13
symbol: NDX
position: Long
result: Loss
session: London
setup: NQ ICT 2022 AM Delivery
entry_model: Market Structure Shift + Fair Value Gap + Premium vs. Discount
entry_timeframe: 
higher_timeframe_bias: Bullish
bias_correct: 
entry_price: 29,150
take_profit: 29,292
stop_loss: 29,085.6
exit_price: 29,085.6
pnl: -129.6
r_multiple: -1
planned_rr: 2.2
risk_percent: 
confidence: 3
emotions:
  - Greedy
tags:
  - MarketStructureShift
  - FairValueGap
  - PremiumVsDiscount
  - KillZones
  - DailyBias
  - Discount
source_id: 2018
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 2, minor: 1}
da_opposite_case: "equally viable"
---
# Trade 2026-05-13 - NDX Long Loss

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Loss |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Market Structure Shift + Fair Value Gap + Premium vs. Discount |
| HTF Bias | Bullish |
| Premium/Discount | Discount |
| Power of 3 | Manipulation |
| Confidence | 3/5 (Medium) |
| Entry | 29,150 |
| Stop Loss | 29,085.6 |
| Take Profit | 29,292 |
| Exit | 29,085.6 |
| PnL | -129.6 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-05-12 23:16:00 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: Bullish
- **Premium/Discount**: Discount
- **Power of 3 Phase**: Manipulation

=============== D1 ===============

- Daily bias: Bullish - Giá đang trong trend tăng
=============== H1 ===============

- Giá đang trên đường hồi về OB khung H1
=============== M15 ===============

- Giá có 1 pha quét thanh khoản 1 đáy trước đó và hình thành MSS trong khung nhỏ, tuy nhiên giá chưa về tới OB
=============== M5 ===============

- Entry khi xuất hiện MSS và retrace

=============== Result ===============

- Giá Hit STOP LOSS
- Giá hồi về vùng OB khung H1, thực hiện quét thanh khoản 1 đáy quan trọng
- Do vội vàng vào lệnh (tham) dẫn đến entry sai

### Charts

![[NDX-20260513-2018-1.png]]
![[NDX-20260513-2018-2.png]]
![[NDX-20260513-2018-3.png]]
![[NDX-20260513-2018-4.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Break of Structure (BOS) or Change of Character (CHOCH) confirmed
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Market Structure Shift + Displacement
- [x] No high-impact news events imminent (check economic calendar)
- [x] Rejection Validation When Enter PD Array Zones
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Risking no more than 0.5% of account equity
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Partial take-profit levels are planned (1R, 2R, runner)

---

## 3. Execution Review

- Giá Hit Stoploss do vào entry quá vội, không chờ giá hồi về vùng OB đã đánh dấu khung H1 và chờ 1 pha quét thanh khoản chuẩn

**Emotions**: Greedy

---

## 4. Phân Tích Sau Lệnh

- **Result**: Loss (Hit Stop Loss)
- **Mistake chính**:
  - [[Mistake - ]]
- **Nguyên nhân gốc rễ**:
  - (trống trong bản gốc — dựa trên dữ kiện có trong file: nguyên nhân gốc rễ do chính user nêu ở section 3 là "vào entry quá vội, không chờ giá hồi về vùng OB khung H1 và chờ 1 pha quét thanh khoản chuẩn" — nghĩa là MSS ở M15 được dùng làm trigger entry trong khi OB (POI chính theo bias H1) chưa đạt tới `(suy luận có điều kiện — cần chart H1/M15 xác nhận vị trí OB)`.)
- **Tại sao lệnh này thua/thắng?**
  - Theo Result section: "Giá hồi về vùng OB khung H1, thực hiện quét thanh khoản 1 đáy quan trọng" — nghĩa là entry xảy ra TRƯỚC khi vùng OB/sweep chuẩn diễn ra, entry sớm so với kế hoạch H1.
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - Theo narrative M15: "giá chưa về tới OB" — chính user đã tự ghi nhận điều kiện H1 (giá về OB) chưa đạt tại thời điểm entry, đây là cảnh báo tự ghi nhưng bị bỏ qua.
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Theo Execution Review: chờ giá hồi về đúng vùng OB H1 và chờ pha quét thanh khoản chuẩn trước khi entry `(suy diễn từ Execution Review, không phải bullet gốc riêng của section 4)`.

---

## 5. Lesson Learned

### Bài học kỹ thuật

- (Bản gốc để trống — không có bullet gốc để giữ.)
- MSS ở M15 được dùng làm trigger entry, nhưng chính narrative M15 tự ghi "giá chưa về tới OB" — nghĩa là POI chính (OB, xác định ở khung H1) chưa đạt khi entry diễn ra. Đây là entry dựa trên tín hiệu TF thấp (M15 MSS) trong khi điều kiện TF cao hơn (H1 POI) chưa thỏa — vi phạm trực tiếp chuỗi nesting D1→H1→M5 mà chính hệ thống của user theo đuổi (O1, load-bearing).
- Checklist section 2 tick `[x]` toàn bộ 11/11 dòng bao gồm "Market Structure Shift + Displacement" và "Stop loss is placed beyond the nearest structure level + Buffer" — nhưng nội dung narrative + Execution Review đồng thời phủ nhận điều kiện tiên quyết ("giá chưa về tới OB", "vào entry quá vội") — checklist tick đầy không phản ánh đúng trạng thái entry thật (O1, cùng pattern với CS-O9 đã ghi nhận cấp cross-setup).

### Bài học tâm lý

- (Bản gốc để trống.)
- Emotions field tự ghi "Greedy", và Execution Review tự dùng chữ "tham" — đây là tự nhận tâm lý hợp lý, khớp trực tiếp với hành vi entry sớm trước khi điều kiện H1 đạt. Đây là một trong ít lệnh Loss có tự nhận tâm lý rõ ràng và nhất quán với nguyên nhân kỹ thuật, không mâu thuẫn.

### Bài học quy trình & risk

- risk_percent để trống hoàn toàn — không thể kiểm lệnh này risk bao nhiêu % account, trong khi bản trùng của lệnh này (`Loss-01-Trade-2026-05-13-NDX-Long.md`) ghi risk_percent: 5% cho cùng entry/SL/TP. Không có cách xác nhận đâu là risk % thật đã dùng (O2, liên hệ CS-O0′ về việc 2 file mô tả cùng một lệnh).
- Checklist tick 11/11 hoàn hảo trên một lệnh mà chính narrative tự phủ nhận điều kiện lõi (POI H1) — cho thấy checklist "Pre-trade" trong template này nhiều khả năng được tick *sau* khi đóng lệnh như một thao tác log, không phải gate trước entry thật (liên hệ CS-O2, CS-O9).

### Rule cần thêm/cập nhật

- [ ] **KIỂM TRA ĐƯỢC**: Khi bias chính là D1→H1 (POI ở H1), entry ở M15/M5 chỉ được thực hiện SAU khi narrative xác nhận "giá đã về tới OB H1" = Yes — nếu câu trả lời là "chưa về tới" (như trường hợp này), không entry dù có MSS ở TF thấp hơn (đóng O1).
- [ ] **KIỂM TRA ĐƯỢC**: Checklist "Pre-trade" phải được tick với timestamp trước entry_price được ghi vào frontmatter — nếu không có cơ chế timestamp, thêm field `checklist_ticked_at:` để tách biệt log hồi tố khỏi gate thật (đóng O2/liên hệ CS-O9).
- [ ] **KIỂM TRA ĐƯỢC**: risk_percent phải được điền ở mọi file, không để trống — đối chiếu 2 bản ghi của cùng một lệnh (nếu có) phải khớp risk_percent, nếu không khớp thì một trong hai bản sai và cần sửa (đóng O2).

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Ghi chú trùng lệnh**: File này và `Loss-01-Trade-2026-05-13-NDX-Long.md` mô tả cùng một lệnh — entry 29,150 / SL 29,085.6 / TP 29,292 giống nhau tuyệt đối, pnl -129.6 vs -129 (chênh 0.6, có thể do rounding phí) — xem **CS-O0′** (`[ARITHMETIC] · material`, cross_setup_findings.md mục 1). Bản này có nội dung phong phú hơn (prose D1/H1/M15/Result đầy, checklist tick, emotions, confidence) nên được chọn để phân tích ĐẦY ĐỦ theo brief; bản kia chỉ phản biện phần nội dung khác (entry_model "Venom Model", mistake tags 02/07 cụ thể, risk_percent 5%).

**Evidence base**: Prose-only, 4 link chart Obsidian không có ảnh trong dataset → không dùng [CHART]. Sufficiency: **thin** — load-bearing claim (entry có tuân thủ đúng chuỗi POI H1 trước MSS M15 hay không) chỉ dựa vào lời tự thuật của user, nhưng may mắn là chính lời tự thuật này tự mâu thuẫn nội tại (không cần chart để phát hiện).

**Thesis & claims**:
- C1: HTF bias D1 Bullish, Long khớp hướng — claim văn xuôi, không kiểm độc lập được.
- C2: M15 có sweep + MSS trong khung nhỏ — claim văn xuôi.
- C3 (load-bearing): Entry hợp lệ vì có MSS + FVG + Premium/Discount (entry_model), thực hiện trong Discount zone của Long — nhưng chính narrative M15 nói thêm "**tuy nhiên giá chưa về tới OB**" (OB là POI chính ở H1).
- C4: Lệnh thua (Loss, Hit SL, pnl -129.6) → Execution Review tự quy nguyên nhân là "vào entry quá vội... không chờ pha quét thanh khoản chuẩn".

Suy luận: C3 phụ thuộc vào cả MSS M15 VÀ POI H1 cùng đạt; nhưng theo chính narrative, chỉ MSS M15 đạt, còn OB H1 (POI chính) chưa đạt — đây là điều kiện thiếu ngay trong thesis gốc, không phải suy diễn của báo cáo này.

**Điều gì đứng vững**: Arithmetic RR khớp — risk = |29,150 − 29,085.6| = 64.4, reward = |29,292 − 29,150| = 142, RR = 142/64.4 = 2.205 ≈ `planned_rr: 2.2`. Direction Long khớp cấu trúc SL < Entry < TP. Emotions "Greedy" nhất quán với Execution Review "tham" — tự nhận tâm lý không mâu thuẫn với nguyên nhân kỹ thuật đã nêu.

**Objections**:

**O1 · [SELF-CONTRADICTION] · fatal · attacks C3 (load-bearing)**
Claim: entry_model "Market Structure Shift + Fair Value Gap + Premium vs. Discount" — entry hợp lệ theo đủ 3 điều kiện.
Evidence: Narrative M15 tự ghi "Giá có 1 pha quét thanh khoản 1 đáy trước đó và hình thành MSS trong khung nhỏ, **tuy nhiên giá chưa về tới OB**"; Result section xác nhận "Giá hồi về vùng OB khung H1, thực hiện quét thanh khoản 1 đáy quan trọng" **sau khi đã entry** (tức là sự kiện OB+sweep chuẩn ở H1 xảy ra sau, không phải trước, thời điểm entry); Execution Review: "vào entry quá vội, không chờ giá hồi về vùng OB đã đánh dấu khung H1 và chờ 1 pha quét thanh khoản chuẩn".
Consequence: Entry_model liệt kê "Premium vs. Discount" như một điều kiện đã thỏa, nhưng bản thân user xác nhận vùng OB H1 (nơi xác lập Discount zone chuẩn) chưa đạt tại thời điểm entry — MSS M15 được dùng làm trigger trong khi điều kiện H1 cao hơn trong chuỗi nesting D1→H1→M5 chưa hoàn tất. Đây là entry nhảy cấp TF, bỏ qua mắt xích H1.
Your best answer: "Discount zone có thể được tính trên một dealing range khác không cần đợi giá chạm đúng OB." — Không cứu được: chính user dùng chữ "chưa về tới OB" như lý do thua, tự xác nhận OB là điều kiện bắt buộc mà mình biết chưa đạt.
Retracted by: một mức Discount zone cụ thể (không phải OB H1) được nêu rõ đã đạt tại thời điểm entry — hiện không có trong file.

**O2 · [UNSUPPORTED] · material · attacks C4**
Claim ngầm: risk % của lệnh này tuân thủ rule 0.5% (checklist tick "Risking no more than 0.5%" = `[x]`).
Fails: risk_percent field để trống hoàn toàn trong frontmatter — không có số để đối chiếu với tick `[x]`. Bản trùng của lệnh này (cùng entry/SL/TP) ghi risk_percent: 5% — nếu đó đúng là cùng một lệnh, tick `[x]` ở đây là sai (5% ≠ ≤0.5%).
Consequence: không kiểm được liệu tick "Risking no more than 0.5%" phản ánh đúng risk thật hay chỉ là tick mặc định trong template — nếu đối chiếu với bản trùng thì tick này gần như chắc là sai.
Your best answer: "Hai bản là hai lệnh riêng biệt (re-entry cùng giá), risk_percent có thể khác nhau thật." — Không loại trừ được hoàn toàn (xem CS-O0′), nhưng không có timestamp phân biệt hai sự kiện, nên vẫn treo.
Retracted by: risk_percent thật được điền vào file này, hoặc xác nhận đây là 2 lệnh độc lập với risk khác nhau.

**O3 · [METHOD] · material** — Checklist section 2 tick `[x]` toàn bộ 11/11 dòng, nhưng ít nhất 1 dòng ("Market Structure Shift + Displacement") mâu thuẫn trực tiếp với narrative (chỉ có MSS ở M15, không có xác nhận Displacement rõ ràng nào được nêu ở bất kỳ TF nào trong file) — cùng pattern outcome-agnostic checklist đã ghi nhận ở CS-O9. Retracted by: nêu rõ displacement cụ thể ở TF nào, khung giờ nào.

**O4 · [HINDSIGHT] · minor** — "Nếu được vào lại, tôi sẽ làm gì khác?" (section 4, suy diễn từ Execution Review) mô tả chờ OB H1 xác nhận trước — đây là bài học hợp lệ cho mục đích học nhưng không được dùng để đổi nhãn Loss thành "lẽ ra là Win nếu chờ" một cách hồi tố. Retracted by: không cần, đây chỉ là ghi nhận biên.

Drafted 5, cut 1 (draft về "Power of 3 Phase: Manipulation" không đủ evidence văn xuôi để tách thành objection riêng, gộp vào O1 vì cùng thuộc load-bearing POI H1).

**Verdict**: **BROKEN** — load-bearing claim C3 (entry hợp lệ theo đủ POI H1 + MSS M15) tự mâu thuẫn ngay trong narrative do chính user viết (O1) — không cần chart để phát hiện, evidence sufficiency thin không ngăn được objection self-contradiction thuần túy.
Tôi đã tấn công gì mà không phá được: hướng lệnh (Long khớp bias Bullish), arithmetic RR (2.2, đúng công thức), tự nhận tâm lý (Greedy khớp với narrative).
Critique này KHÔNG xác lập: (1) OB H1 có tồn tại đúng vị trí nào trên chart; (2) MSS M15 có hợp lệ theo doctrine (cần body close, structurally significant swing) hay không — không có chart; (3) liệu chờ đủ điều kiện H1 có tránh được loss này hay không — đây là counterfactual không kiểm được.

**Opposite Case**: Đổi vai "chưa về tới OB" — thay vì đọc là điều kiện thiếu, đọc như một internal liquidity sweep hợp lệ *trước* khi giá tiếp tục vào OB thật (tức là MSS M15 là điểm entry đúng của một leg impulse nhỏ hơn, không cần đợi OB H1 vì OB H1 chỉ là POI dự phòng, không phải điều kiện bắt buộc duy nhất). Load-bearing claim của kèo ngược: có tồn tại một tầng cấu trúc M15 độc lập, tự đủ điều kiện entry mà không cần chờ H1.
Strongest self-objection: entry_model trong frontmatter tự liệt kê "Premium vs. Discount" như một trong 3 điều kiện — nếu Discount zone được xác lập từ dealing range H1 (không nêu range nào khác), thì OB H1 vẫn là tham chiếu bắt buộc cho chính điều kiện thứ 3 mà thesis ngược cũng cần dùng.
Strength label: **equally viable** — không có evidence loại trừ hoàn toàn khả năng M15 tự có một cấu trúc đủ điều kiện riêng, nhưng cũng không có gì xác nhận nó; cả hai đọc đều dừng ở mức "có thể" vì thiếu chart.
Observable duy nhất phân biệt hai reading: chart H1/M15 thật cho thấy dealing range nào được dùng để tính Discount zone, và liệu MSS ở M15 phá một swing "structurally significant" độc lập hay chỉ là nhiễu nội bộ trước khi giá tiếp tục xuống OB H1 thật. Không có trong file.

## 9. Opposite Case (Counter-Argument)

(Xem mục 8 — Opposite Case đã trình bày đầy đủ ở trên.)

## 10. Falsification Tests

1. **Test cho O1**: Xin chart H1 thật của ngày 05-13 — nếu vị trí OB H1 nằm xa hơn giá entry 29,150 (tức giá thật chưa chạm OB tại thời điểm entry, khớp với "chưa về tới OB"), O1 HELD. Nếu OB H1 đã bao trùm mức 29,150 tại thời điểm đó, O1 giảm về `material` (entry vẫn trong POI, chỉ là user tự đánh giá quá khắt khe khi review).
2. **Test cho O2**: Xác nhận từ user liệu đây và bản `Loss-01-Trade-2026-05-13-NDX-Long.md` là 1 hay 2 lệnh — nếu 1 lệnh, risk_percent đúng là 5% (đóng O2 theo hướng breach thật, không phải thiếu dữ liệu); nếu 2 lệnh độc lập, cần risk_percent riêng cho file này.
3. **Test cho O3**: Đối chiếu 27 file journal, đếm bao nhiêu file có checklist tick 100% nhưng Execution Review tự phủ nhận ≥1 điều kiện lõi — nếu ≥ 30% số file, đây là lỗi hệ thống ghi checklist hồi tố (mở rộng CS-O9 thành finding có sample lớn hơn).
