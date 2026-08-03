---
type: backtest
backtest_date: 2026-01-07
trade_date: 2010-10-19
symbol: EURUSD
position: Long
result: Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[25 - OB - Order Block|OB]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.39086
stop_loss: 1.38801
take_profit: 1.39521
r_planned: 1.53
r_multiple: 1.53
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2010-10-19 — EURSUD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | EURUSD                                            |
| Trade Date (dữ liệu) | 2010-10-19                                        |
| Position             | Long                                              |
| Result               | Win                                               |
| Session              | London                                            |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M5                                                |
| HTF Bias             | Bullish                                           |
| Bias Correct?        | Yes                                               |
| Entry                | 1.39086                                           |
| Stop Loss            | 1.38801                                           |
| Take Profit          | 1.39521                                           |
| R Planned            | 1.53                                              |
| R Multiple (kết quả) | 1.53                                              |
| Grade                | B                                                 |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - D1 đang trong nhịp tăng mạnh (treding)
  - HH/HL
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day High
  - Sell-side liquidity: Previous Day Low

![[Pasted image 20260701075001.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL 
- **Dealing Range**: 
	- High: 1.14594 
	- Low 1.38319 
	- Giá đang trong vùng Discount
- **POI chính**: 
	- Order Block : 1.3914 - 1.38869
- **Liquidity cần chờ sweep**:
  - Old lows: 1.38890
  - Cạnh dưới Order Block để quét những người vào lệnh sớm
### Phân Tích:
- Giá đang nằm trong vùng Discount của dealing range
- Giá đã quét thanh khoản và tạo 1 Order Block trước đó
- Hiện tại giá đang retrace về vùng Order Block
- Chờ Giá fill Order Block và xem phản ứng
- Giá quét xuống cạnh dưới của order block và quay lên đóng nến trên 50% -> Respect Order Block
- Sau đó xuống khung M5 quan sát phản ứng

![[Pasted image 20260701131425.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá tạo displacement + FVG sau khi quét xuống cạnh dưới OB
- Giá phá qua đỉnh trước đó tạo thành MSS
- FVG hình thành trùng lắp với OB khung H1
- Giá retrace về 50% FVG -> Entry
- Stoploss đặt dưới order block
- **Entry trigger**:
  - Liquidity Sweep: Quét qua OB + old low
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - OB: Có
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG 50% -> Entry
- **Invalidation reason**:
  - Giá đóng qua đáy cũ
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260701131752.png]]
---

## 2. ICT 2022 Model — Entry Sequence

Đánh dấu theo đúng thứ tự checklist của mô hình:

- [x] **1. Liquidity Sweep** — giá quét thanh khoản (Equal H/L, swing, Asia range...)
  - Loại: Internal / External / Equal Highs / Equal Lows
- [x] **2. Displacement** — nến đẩy mạnh, tạo FVG, phá cấu trúc nội bộ
- [x] **3. Market Structure Shift (MSS)** — phá swing point ngược hướng sweep
- [x] **4. FVG / OB hợp lệ** hình thành trong displacement leg
- [x] **5. Entry** — limit trong FVG/OB (CE - Consequent Encroachment) trong Kill Zone
- [x] **6. Stop Loss** — phía trên/dưới điểm sweep (invalidation)
- [x] **7. Take Profit** — opposing liquidity / PD array kế tiếp

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ
- [x] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [x] Entry trong POI hợp lệ, không đua giá
- [x] SL ở vùng invalidation hợp lý
- [ ] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP / Hit SL / BE / Manual Close
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về discount -> Quét OB + Old lows -> MSS + Displacement + FVG -> Giá retrace 50% FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- 

### Pattern lặp lại (điều cần để ý lần sau)

- 

### Rule cần thêm/cập nhật vào Playbook

- [ ] 

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | /10 |
| POI Selection | /10 |
| Liquidity Sweep | /10 |
| MSS Confirmation | /10 |
| FVG / OB Entry | /10 |
| Risk Management (RR) | /10 |

**Overall Grade**: A / B / C / D / F

---

## 7. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL tại thời điểm entry.** Note gốc chỉ nêu "old lows 1.38890" và "cạnh dưới OB" là liquidity chờ quét, không phân tách rõ đâu là internal (IRL) và đâu là external (ERL). Với entry 1.39086, SL 1.38801: SL nằm dưới cả OB (1.38869–1.3914) và dưới mốc old low 1.38890 khoảng 0.00089 (~8.9 pip) — nghĩa là SL đặt dưới điểm sweep, đúng logic invalidation, nhưng note không nêu có external liquidity pool nào (PDL, swing low lớn hơn) nằm giữa 1.38890 và 1.38801 hay không. Nếu có một EQL/pool khác nằm trong khoảng đó, SL đang "chia sẻ" vùng với liquidity chưa được map — một lỗ hổng bản đồ, không phải lỗi entry.

**Chất lượng displacement/MSS.** Note mô tả "giá tạo displacement + FVG sau khi quét xuống cạnh dưới OB" và "phá qua đỉnh trước đó tạo MSS" — đúng trình tự sweep → displacement → MSS. Tuy nhiên không có số liệu về kích thước nến displacement so với ATR hay số nến cấu thành FVG, nên độ mạnh displacement chỉ được mô tả định tính ("nến lớn"), không định lượng.

**Yếu tố thời gian.** Session = London, không có mốc giờ cụ thể trong note (không có khung giờ killzone chính xác). Setup Quality Checklist tick "giá nằm trong Kill Zone" nhưng không dẫn chứng giờ — đây là claim không có evidence giờ cụ thể.

**Vị trí entry trong dealing range H1** (High 1.14594 — rõ ràng là lỗi nhập liệu, giá trị này thấp hơn Low 1.38319, không hợp lý cho cặp EURUSD giai đoạn 2010; đây là lỗi số liệu trong note gốc, không sửa theo brief nhưng cần nêu ở Doctrine check).

**So sánh với các lệnh khác cùng mẫu vault.** So với [[2026-07-06/01 - Win - EURUSD - 2005-04-12 - Short]] và [[2026-07-06/02 - Win - EURUSD - 2005-04-13 - Short]] — cả hai đều có mô tả sweep target rõ tên (EQH cụ thể, FVG H1 cụ thể) và Lesson Learned đầy đủ, trong khi note 2010-10-19 này để trống hoàn toàn mục Lesson Learned và Final Grade (không điền điểm số từng tiêu chí) — cho thấy đây thực sự là note sớm nhất, quy trình ghi chép chưa định hình.

![[EURUSD-20101019-liquidity-map.svg]]

## 8. Phản biện chuyên sâu (Devil's Advocate)

**Mode: REVIEW.** Evidence base: chỉ có text trong note + 3 screenshot filename không đọc được nội dung ảnh (`Pasted image ...png`) — coi như evidence không truy cập được. Fact base = số liệu/mô tả trong note. **evidence_sufficiency: thin** — load-bearing claim (MSS + displacement tại M5) không thể kiểm chứng độc lập vì không xem được ảnh, chỉ có mô tả chủ quan của người viết.

**Claim graph:**
- C1: HTF D1 bias Bullish do "trending, HH/HL" (không có số liệu D1 cụ thể).
- C2: H1 dealing range High 1.14594 / Low 1.38319 — **số liệu tự mâu thuẫn** (High < Low).
- C3: Giá đang ở Discount, POI = OB 1.3914–1.38869.
- C4: Giá quét cạnh dưới OB + old low 1.38890, đóng nến trên 50% OB → "respect OB".
- C5: M5 hình thành displacement + FVG + MSS sau sweep, overlap với OB H1.
- C6: Entry tại CE của FVG M5 (1.39086) — **load-bearing**: toàn bộ setup phụ thuộc vào C5 (MSS/displacement M5 thật) và C3 (POI đúng vị trí discount).
- C7 (từ C5+C6): Setup là ICT 2022 Model hợp lệ → grade A.

**Load-bearing: C5** — nếu M5 không có MSS/displacement thật (chỉ là continuation retrace bình thường), toàn bộ chuỗi sweep→entry chỉ là một retrace ngẫu nhiên trùng khớp hướng bias.

**Những gì còn đứng:** C1 (bias Bullish D1) và C3 (POI OB + discount) có mô tả nhất quán nội bộ, không tự mâu thuẫn ngoài lỗi C2. Trình tự kể lại (sweep → MSS → displacement → FVG → retrace 50% → entry) đúng cấu trúc ICT 2022 Model về mặt logic tường thuật.

**O1 · [ARITHMETIC] · material · attacks C2**
Claim: "Dealing Range High: 1.14594, Low 1.38319, giá đang trong vùng Discount."
Evidence: High (1.14594) < Low (1.38319) — không thể là một dealing range hợp lệ theo bất kỳ chuẩn nào; giá trị High gần như chắc chắn là lỗi nhập (thiếu số hoặc gõ nhầm, có thể ý là 1.41594 hoặc tương tự).
Consequence: Premium/discount claim ("giá đang trong vùng Discount") không thể verify bằng số liệu đã cho — midpoint không tính được.
Retracted by: Số liệu High đúng của dealing range H1 tại thời điểm đó (cần xem lại chart nguồn).

**O2 · [HINDSIGHT] · material · attacks C7 (load-bearing chain)**
Claim: "Setup khớp 90% với mô hình chuẩn" + Grade A, chấm sau khi biết kết quả Win.
Fails: không có invalidation condition nào được viết TRƯỚC entry ngoài "giá đóng qua đáy cũ" — đây là điều kiện tồn tại từ trước, không phải bằng chứng cho thấy grade được cho dựa trên process tại thời điểm quyết định.
Evidence: mục 4 "Phân tích sau lệnh" viết theo replay, câu "lệnh thắng vì chờ đầy đủ điều kiện" là suy diễn ngược từ outcome — không có ghi chép nào từ *trước* khi biết kết quả.
Consequence: Không thể phân biệt được grade A này được chấm vì quy trình chuẩn tại điểm quyết định, hay được chấm cao hơn vì biết trước lệnh thắng (note viết sau khi replay toàn bộ, backtest mode).
Your best answer: "Checklist mục 2 và 3 đã tick đủ trước khi viết phần replay." Không đủ để bác bỏ — checklist tick sau khi xem toàn bộ chart lịch sử (bao gồm phần giá đi sau entry) không chứng minh được người viết *chỉ* dùng thông tin tới hard right edge khi tick.
Retracted by: Ghi chú thời điểm/thứ tự tick — ví dụ khẳng định checklist được điền trước khi kéo chart sang phải để xem outcome.

**O3 · [METHOD] · fatal · attacks C7**
Claim: đây là mẫu ICT 2022 Model chuẩn 90%, dùng làm phản xạ luyện tập.
Fails: không có invalidation condition độc lập với outcome được pre-registered — "giá đóng qua đáy cũ" là điều kiện chung cho mọi long setup, không riêng cho setup này; không có ngưỡng nào (ví dụ thời gian tối đa chờ, hoặc mức retrace tối đa của FVG trước khi coi là thất bại) được định nghĩa trước entry.
Consequence: Không thể tách được "quy trình đúng, thắng vì đúng" khỏi "quy trình mơ hồ, thắng vì thị trường đi đúng hướng ngẫu nhiên" — với 1 mẫu, không đủ để khẳng định phương pháp có edge.
Your best answer: "Grade A dựa trên checklist 8/9 mục tick, không dựa outcome." Không đủ: checklist là bộ tiêu chí *mô tả lại* những gì đã xảy ra, không phải điều kiện được cam kết trước khi biết giá đi đâu.
Retracted by: Một invalidation rule cụ thể, đo lường được, được ghi nhận trước khi biết kết quả (ví dụ: "nếu FVG bị lấp hoàn toàn trong vòng 3 nến M5 mà không có MSS tiếp theo → invalid").

**Filter:** 5 objection nháp, cắt 2 (một về session claim không dẫn chứng giờ cụ thể — không đổi kết luận nên xóa; một về Final Grade để trống — chỉ là thiếu dữ liệu ghi chép, không phải lỗi phân tích). Còn 3 objection: 1 material arithmetic, 1 material hindsight, 1 fatal method.

**Opposite case.** Từ cùng evidence: đây có thể chỉ là một continuation pullback trong xu hướng tăng đã xác lập từ trước (không cần sweep+MSS+FVG mới để giải thích) — giá đơn giản retrace về vùng cung cầu cũ rồi tiếp diễn, và "MSS" trên M5 chỉ là một swing nhỏ bị phá do noise, không phải structural shift thật. Load-bearing của inverse: swing bị phá trên M5 có đủ "structurally significant" theo doctrine hay không (xem Doctrine check C-số bên dưới). Tự phản biện inverse: nếu không có MSS thật, việc giá đảo đúng hướng ngay tại OB H1 vẫn là một quan sát hợp lệ (OB H1 phản ứng đúng), nên inverse không giải thích được *tại sao giá phản ứng chính xác tại OB* — nó chỉ tấn công vào lớp M5, không tấn công vào lớp H1. Nhãn: **weaker but non-trivial** — inverse chỉ mạnh nếu M5 MSS là giả, nhưng không phủ nhận được phản ứng tại OB H1.

Distinguishing observable: xem nến M5 phá swing có đóng nến (body close) vượt swing point hay chỉ có râu — nếu chỉ có râu, MSS theo doctrine không hợp lệ và inverse case mạnh hơn hẳn.

**Verdict: UNPROVEN.** Evidence sufficiency thin (không xem được ảnh) → không thể nâng lên SURVIVES. Load-bearing C5 (MSS/displacement M5) không FAIL rõ ràng (không có bằng chứng phủ nhận) nhưng cũng không được chứng minh độc lập với outcome — dừng ở UNPROVEN chứ không phải SURVIVES THIS ATTACK.

**Điều tôi không phá được:** trình tự tường thuật (bias→POI→sweep→MSS→FVG→entry) tự nhất quán và không có mâu thuẫn nội tại nào ngoài lỗi số C2.

**Điều critique này không xác lập:** không xác lập được setup này *thực sự* có MSS hợp lệ theo canon (cần ảnh M5 để xác nhận body close); không xác lập được liệu grade A phản ánh đúng chất lượng process hay bị outcome bias.

**Falsification tests (tối đa 3):**
1. Kiểm ảnh M5 gốc: MSS có body close vượt swing point không? → đóng O3 nếu xác nhận có body close rõ ràng kèm invalidation rule tương đương được áp dụng nhất quán ở ≥5 note khác trong vault.
2. Đối chiếu số liệu High/Low dealing range H1 với chart gốc để sửa O1.
3. Kiểm tra xem trong toàn vault có note nào ghi invalidation rule *trước* biết outcome (note LIVE) để xác định liệu quy trình grade A có độc lập với outcome ở batch khác không — nếu 0/toàn vault có note LIVE, O3 áp dụng cho toàn hệ thống chứ không riêng note này.

## 9. Doctrine check (ICT 2022 canon)

**Thesis:** Long EURUSD 19/10/2010 theo ICT 2022 Model — sweep OB H1 + old low → MSS + displacement + FVG M5 → entry tại CE, grade A.

**Cần sửa** (load-bearing trước):
- C5 (MSS M5) — **UNSUPPORTED** · note nói "giá phá qua đỉnh trước đó tạo MSS" nhưng không nêu swing point cụ thể bị phá hay xác nhận body close (SKILL.md § MSS: cần "phá swing point ngược hướng sweep" với body close, không chỉ wick) → cần ảnh M5 xác nhận close vượt swing để nâng lên PASS. (load-bearing)
- C2 (Dealing Range H1) — **FAIL** · High (1.14594) < Low (1.38319) là mâu thuẫn arithmetic, không phải lỗi definition nhưng làm claim Premium/Discount không kiểm được → sửa lại số liệu High đúng từ chart nguồn.
- C4 (OB "respect", đóng nến trên 50%) — **UNSUPPORTED** · claim đúng dạng hiện tượng OB nhưng không có giá nến đóng cụ thể để verify 50% → ghi rõ giá đóng của nến phản ứng.

**PASS:** C1 (bias Bullish D1, mô tả trending HH/HL — chấp nhận ở mức mô tả, không cần số cụ thể để PASS status bias); C3 (OB làm POI, cấu trúc tường thuật khớp doctrine OB = nến gốc di chuyển tạo imbalance, không mâu thuẫn nội tại); C6 (entry tại CE của FVG — công thức CE = (fvg_high+fvg_low)/2 được note tuân theo đúng ý nghĩa, dù không có số fvg_high/fvg_low riêng để tính lại).

**Verdict: INSUFFICIENT EVIDENCE** — load-bearing claim C5 (MSS M5) ở mức UNSUPPORTED do thiếu ảnh/số liệu xác nhận body close; verdict không thể là PARTIALLY ALIGNED chỉ vì các claim phụ PASS.

**Notes:** Đây là note sớm nhất trong vault, không có field `entry_type`, `confluence_score`, `first_error_step` trong frontmatter như các note sau — cấu trúc ghi chép sơ khai khiến gần như mọi claim quan trọng (MSS, OB reaction) đều dừng ở UNSUPPORTED vì thiếu số liệu tường minh, không phải vì sai định nghĩa. Đây là *doctrine gap về mặt ghi chép* (note-taking), không phải doctrine gap của canon.

## 10. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật**
- Ví dụ số thật: Dealing Range H1 ghi "High: 1.14594, Low: 1.38319" — High < Low là bất khả thi vật lý cho một range. Tổng quát hóa: mọi note backtest phải có bước validate High > Low (cho bias tăng) hoặc Low < High trước khi tính premium/discount, tốt nhất bằng công thức tự động (script) thay vì gõ tay.
- Ví dụ số thật: SL 1.38801 nằm dưới old low 1.38890 khoảng 8.9 pip nhưng note không nêu external liquidity pool nào khác gần đó. Tổng quát hóa: mọi note nên map rõ ít nhất 2 lớp liquidity (internal gần nhất + external xa nhất) quanh vùng SL để biết SL đang "mua" bao nhiêu buffer.

**(b) Bài học quy trình/checklist**
- Note không điền Final Grade (để trống `/10` mọi tiêu chí) dù Overall Grade ghi "A" — quy trình grade thiếu tính nhất quán nội bộ: không thể có Overall Grade A nếu không có điểm thành phần nào được chấm.
- Không có mốc giờ cụ thể cho killzone dù checklist tick "giá nằm trong Kill Zone" — cần ghi giờ GMT/ET cụ thể của nến entry để claim này verify được.

**(c) Bài học tâm lý-hành vi**
- Note thuộc dạng viết lại sau khi biết outcome (backtest replay), nên câu "lệnh thắng vì chờ đầy đủ điều kiện" có nguy cơ là hindsight rationalization — cảm giác tự tin về process bị khuếch đại bởi biết trước kết quả Win.
- Xu hướng chấm Grade A cho note sớm nhất, thiếu chi tiết nhất trong vault là dấu hiệu cảnh báo: giai đoạn đầu backtest thường lạc quan quá mức về khả năng nhận diện mẫu của chính mình.

**(d) Rule đề xuất cho Playbook**
- [ ] Mọi note backtest phải validate High > Low của dealing range bằng công thức trước khi ghi nhận premium/discount.
- [ ] Mọi claim MSS phải kèm giá đóng nến cụ thể phá swing point (không chỉ mô tả bằng lời) để phân biệt body close với wick.
- [ ] Final Grade phải điền đủ điểm thành phần trước khi ghi Overall Grade — không cho phép Overall Grade tồn tại độc lập với điểm chi tiết.

**(e) Điều KHÔNG nên học từ lệnh này**
- Không nên coi "90% khớp mô hình chuẩn" là benchmark định lượng đáng tin — con số này được ước lượng chủ quan sau khi biết kết quả Win, không có công thức tính %.
- Không nên dùng note này làm mẫu tham chiếu cho cách ghi MSS (thiếu giá đóng nến cụ thể) — đây là điểm yếu cần tránh lặp lại, không phải điểm mạnh cần nhân rộng.
- Không nên diễn giải Grade A của note này là bằng chứng cho thấy setup "OB H1 + FVG M5 overlap" có edge thống kê — n=1, và note không có invalidation rule độc lập với outcome.

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
