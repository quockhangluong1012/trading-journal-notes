---
type: backtest
backtest_date: 2026-01-07
trade_date: 2005-04-12
symbol: EURUSD
position: Short
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[25 - OB - Order Block|OB]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29729
stop_loss: 1.30164
take_profit: 1.28811
r_planned: 2.1
r_multiple: 2.1
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-12 — EURSUD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | EURUSD                                            |
| Trade Date (dữ liệu) | 2005-04-12                                        |
| Position             | Short                                              |
| Result               | Win                                               |
| Session              | New York                                            |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M5                                                |
| HTF Bias             | Bearish                                           |
| Bias Correct?        | Yes                                               |
| Entry                | 1.29729                                           |
| Stop Loss            | 1.30164                                           |
| Take Profit          | 1.28811                                           |
| R Planned            | 2.1                                              |
| R Multiple (kết quả) | 2.1                                              |
| Grade                | A                                                 |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang LH/LL
  - Nhịp displacement có tạo Liquidity Void
  - => Bias chuyển sang Bearish
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day High (1.30009)
  - Sell-side liquidity: Previous Day Low (1.29090)

![[Pasted image 20260706051516.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL 
- **Dealing Range**: 
	- High: 1.30585 
	- Low 1.28001
	- Giá đang di chuyển về vùng Premium (đúng theo bias Bearish)
- **POI chính**: 
	- Order Block : 1.30110 - 1.29573
- **Liquidity cần chờ sweep**:
  - Old Highs: Giá hình thành 1 Equal high khung H1 bên trong Order Block (1.30033)
  - Cạnh trên Order Block
### Phân Tích:
- Giá hình thành 1 BPR lớn bên dưới vùng discount sau 1 nhịp giá tăng mạnh (Target)
- Giá quay lại vùng Premium
- Tạo 1 Equal High rõ
- Giá Quét qua vùng equal high và cạnh trên của OB sau đó giá quay lại đóng nến vào trong OB

![[Pasted image 20260706051548.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá tạo displacement + FVG sau khi quét lên cạnh trên OB và EH
- Giá hình thành MSS
- FVG hình thành trùng lắp với OB khung H1
- Giá retrace gần tới FVG -> Entry
- Stoploss đặt trên điểm sweep
- POI đang nằm trong vùng OTE
- **Entry trigger**:
  - Liquidity Sweep: Quét qua OB + QH
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - OB: Có
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry
- **Invalidation reason**:
  - Giá đóng qua đỉnh swing high đã quét trước đó
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260706052036.png]]
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
- [x] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone (New york)
  - Giá quét EQH (khung H1 - quan trọng), quét OB
  - Giá đang trong vùng Premium và quan trọng là đang trong khu vực OTE
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về premium -> Quét OB + EQH -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Confluence mạnh nhất của lệnh này là **FVG M5 trùng lắp với Order Block H1**, và toàn bộ POI nằm trong vùng **Premium + OTE**. Đây là loại chồng lớp (HTF POI × LTF FVG × Premium × OTE) cần ưu tiên săn khi backtest — một FVG M5 đơn lẻ không gối lên POI HTF thì giá trị thống kê thấp hơn hẳn.
- Việc chờ giá quét **cả EQH H1 (thanh khoản quan trọng) lẫn cạnh trên OB** rồi mới xuất hiện MSS là bước lọc entry chất lượng. Sweep đúng thanh khoản mục tiêu (draw on liquidity) trước MSS là điều kiện, không phải tùy chọn.
- Tín hiệu **nến quét xong quay lại đóng vào trong OB** (close back inside OB) là dấu hiệu sớm, xuất hiện *trước* MSS trên M5 — có thể dùng làm cảnh báo "chuẩn bị vào vùng quan sát".

### Pattern lặp lại (điều cần để ý lần sau)

- **EQH nằm bên trong một OB lớn = nam châm thanh khoản.** Giá gần như luôn quét EQH đó trước khi đảo chiều. Khi thấy Equal Highs bên trong POI, mặc định là *chờ quét rồi mới tính entry*, đừng đón đầu.
- Chuỗi 2022 Model đã khớp gần như sách giáo khoa: Premium → sweep (OB + EQH) → MSS + displacement + FVG → retrace CE → entry. Ghi nhớ đúng trình tự này để nhận diện nhanh lần sau.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Chỉ vào 2022 Model khi **FVG entry M5 trùng/nằm trong POI HTF** (OB hoặc FVG H1). FVG M5 không có confluence HTF → bỏ qua.
- [ ] Khi kế hoạch RR > 2R, **lập kế hoạch partial TP từ trước khi vào lệnh** (ví dụ chốt 50% tại 1R hoặc tại PD array trung gian). Đây là điểm "nếu vào lại" đã tự nhận ra — biến nó thành rule thay vì tiếc nuối sau lệnh.

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | 9/10 |
| POI Selection | 9/10 |
| Liquidity Sweep | 9/10 |
| MSS Confirmation | 8/10 |
| FVG / OB Entry | 9/10 |
| Risk Management (RR) | 7/10 |

**Overall Grade**: A

---

## 7. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL.** Draw on liquidity D1 nêu rõ: Buy-side = PDH 1.30009, Sell-side = PDL 1.29090. Entry Short 1.29729 nằm giữa hai mốc này. TP 1.28811 nằm dưới PDL (1.29090) khoảng 27.9 pip — nghĩa là TP đi *xuyên qua* PDL, một external liquidity pool, trước khi tới đích — về doctrine, PDL vốn là draw on liquidity của chính setup này (SSL), nên TP hợp lý về hướng nhưng đi ngang qua chính target đã định nghĩa ban đầu (PDL) rồi mới dừng — đáng nêu vì có thể TP thực tế lấy risk cao hơn cần thiết nếu PDL đã đủ là draw. SL 1.30164 nằm trên EQH khung H1 (1.30033) khoảng 13.1 pip và trên cạnh trên OB (1.30110) khoảng 5.4 pip — buffer khá mỏng so với biên độ trung bình di chuyển của cặp tiền, nhưng đủ để tránh bị quét bởi chính điểm sweep vừa xảy ra.

**Chất lượng displacement/MSS.** Note mô tả trình tự chuẩn: quét EQH H1 + cạnh trên OB → displacement M5 tạo FVG → MSS. Điểm mạnh: sweep target có TÊN cụ thể (EQH H1 tại 1.30033), không phải sweep mơ hồ — đây là điểm khác biệt tích cực so với note 1 (2010-10-19).

**Yếu tố thời gian.** Session New York, không có giờ cụ thể trong note gốc (không có mốc HH:MM). Killzone claim vẫn ở mức tick checklist, không dẫn chứng giờ.

**Vị trí entry trong dealing range H1.** High 1.30585 / Low 1.28001, mid = 1.29293. Entry 1.29729 nằm ở phía Premium (retracement từ high ≈ 0.331 tính từ đỉnh) — khớp với bias Bearish (short từ premium). Entry nằm trong OB (1.29573–1.30110) — đúng vị trí POI đã định nghĩa.

**So sánh với lệnh cùng mẫu.** So với [[2026-07-06/02 - Win - EURUSD - 2005-04-13 - Short]] (ngày kế tiếp, cùng session/bias) — note 13/04 có phân tích lớp thanh khoản sâu hơn nhiều (CE FVG → EQH tại CE → inducement, quét 2 lần trước khi entry thật), trong khi note 12/04 chỉ có 1 lớp sweep (EQH + cạnh OB) rồi entry ngay. Đây có thể là bias người viết: ngày sau (13/04) rút được lesson "chờ inducement" — báo hiệu note 12/04 có khả năng vào sớm hơn tiêu chuẩn mà note sau mới áp dụng.

![[EURUSD-20050412-sweep-sequence.svg|760]]

## 8. Phản biện chuyên sâu (Devil's Advocate)

**Mode: REVIEW.** Evidence base: text note + 3 screenshot không đọc được (ảnh PNG). **evidence_sufficiency: thin** — không xem được ảnh M5/H1 gốc để verify MSS/displacement độc lập.

**Claim graph:**
- C1: D1 bias Bearish do MSS + displacement lớn phá swing low, tạo Liquidity Void.
- C2: H1 dealing range 1.30585–1.28001, giá ở Premium.
- C3: POI = OB H1 1.30110–1.29573, chứa EQH 1.30033 bên trong.
- C4: Giá quét EQH + cạnh trên OB, đóng nến vào trong OB → "respect OB".
- C5 (**load-bearing**): M5 hình thành displacement + FVG + MSS sau sweep, overlap OB H1 → entry hợp lệ tại 1.29729.
- C6 (từ C5): Setup ICT 2022 Model chuẩn 90%, Grade A.

**Load-bearing: C5** — nếu MSS/displacement M5 không đạt chuẩn (chỉ retrace bình thường), phần còn lại chỉ là short tại vùng cung ngẫu nhiên trùng hướng bias.

**Những gì còn đứng:** C1–C4 nhất quán nội bộ và có số liệu cụ thể (EQH 1.30033, OB range rõ) — mạnh hơn hẳn note 1 về độ cụ thể. Arithmetic RR khớp gần đúng (tính lại 2.11 vs note ghi 2.1, do rounding).

**O1 · [HINDSIGHT] · material · attacks C6**
Claim: "Setup này khớp 90% với mô hình chuẩn", Grade A — chấm trong phần replay sau khi biết Hit TP.
Fails: không có ghi chép nào tại/trước điểm entry về mức độ tin tưởng hay điều kiện invalidation cụ thể ngoài "giá đóng qua đỉnh swing high đã quét" — điều kiện này là invalidation chuẩn, không phải bằng chứng process được đánh giá độc lập với outcome.
Evidence: mục 4 viết "Lệnh thắng vì chờ đầy đủ điều kiện" — câu này chỉ có thể viết sau khi biết kết quả Hit TP.
Consequence: 90%-match và Grade A có thể phản ánh outcome (Hit TP → cảm thấy quy trình tốt) hơn là một đánh giá process độc lập.
Your best answer: "Checklist mục 2/3 tick đủ 9/9, đây là process-based, không phải outcome-based." Không đủ: checklist được tick khi viết note đầy đủ (backtest replay), sau khi đã biết outcome — thứ tự ghi chép không được ghi rõ.
Retracted by: bằng chứng cho thấy checklist được điền trước khi xem tiếp phần giá đi sau entry (ví dụ timestamp ghi chú, hoặc note dạng LIVE).

**O2 · [UNSUPPORTED] · material · attacks C5**
Claim: "Giá tạo MSS" trên M5 (không nêu swing point cụ thể bị phá hay giá đóng nến).
Fails: doctrine MSS đòi hỏi phá swing point ngược hướng sweep bằng body close (SKILL.md § MSS) — note không cho số liệu để verify điều này, chỉ nói "giá hình thành MSS".
Evidence: mục M5 "Phân tích" chỉ liệt kê hiện tượng theo tên, không có giá cụ thể của swing bị phá hoặc giá đóng nến breaking candle.
Consequence: Không thể xác nhận độc lập rằng cú phá cấu trúc M5 là MSS thật (structurally significant) hay chỉ là một internal swing nhỏ bị phá do noise.
Your best answer: "Checklist mục 2 tick MSS = có." Không đủ: tick checklist là tự khai báo, không phải evidence quan sát được (giá, nến).
Retracted by: ảnh M5 gốc hoặc mô tả bằng số của swing point bị phá + giá đóng nến breaking candle.

**O3 · [METHOD] · minor** — Setup Quality Checklist 9/9 mục tick "có" đồng loạt cho mọi tiêu chí kể cả RR ≥1:2 (đúng, RR=2.1) — không có tiêu chí nào KHÔNG đạt, khác thường cho một checklist thật (checklist luôn pass hoàn hảo có thể là dấu hiệu điền theo outcome). Retracted by: một note Win khác trong vault có ít nhất 1 mục checklist không tick — nếu tồn tại, giảm nghi ngờ pattern điền checklist theo outcome.

**Filter:** 4 objection nháp, cắt 1 (nghi ngờ về EQH 1.30033 nằm "bên trong" OB — không rõ ràng gây thay đổi kết luận, và note có nêu rõ số liệu nên rebuttal test dễ vượt qua → xóa). Còn 3: 1 material hindsight, 1 material unsupported, 1 minor method.

**Opposite case.** Từ cùng evidence: cú quét EQH + cạnh trên OB có thể chỉ là một liquidity grab tạm thời trong continuation tăng (giá vẫn có thể tiếp tục lên sau khi lấy EQH, vì EQH đơn lẻ không đảm bảo đảo chiều) — và "MSS" trên M5 chỉ là một pullback nhỏ bị hiểu nhầm thành structural shift. Tự phản biện inverse: nếu chỉ là liquidity grab tạm thời, giá thường tiếp tục breakout mới sau khi lấy EQH thay vì tạo cả displacement + FVG + retrace đúng chuẩn — chuỗi hiện tượng đầy đủ này khó giải thích bằng inverse thuần túy. Nhãn: **weaker but non-trivial** — inverse chỉ sống được nếu MSS M5 không có body close thật.

Distinguishing observable: giá đóng nến của candle phá swing high M5 — nếu đóng rõ dưới swing (không phải wick), MSS hợp lệ và inverse yếu hẳn.

**Verdict: UNPROVEN.** Evidence sufficiency thin. Load-bearing C5 không FAIL nhưng cũng UNSUPPORTED độc lập với outcome bias — dừng ở UNPROVEN.

**Điều tôi không phá được:** cấu trúc HTF (D1 bias, H1 OB + EQH cụ thể) tự nhất quán, có số liệu rõ, mạnh hơn note 1.

**Điều critique này không xác lập:** không xác lập MSS M5 có đúng canon hay không (thiếu ảnh); không xác lập Grade A có bị outcome bias hay không một cách dứt điểm.

**Falsification tests:**
1. Kiểm ảnh M5 gốc: swing point bị phá bởi MSS có giá cụ thể + đóng nến rõ dưới swing không? → đóng O2 nếu xác nhận.
2. Rà toàn vault: đếm % note Win có Setup Quality Checklist tick 9/9 hoàn hảo so với note Loss — nếu tỷ lệ 9/9 áp đảo ở Win, O3 được nâng severity.
3. Tìm bằng chứng thời điểm ghi chú (timestamp) để xác định checklist được điền trước hay sau khi biết outcome, đóng O1 nếu có bằng chứng LIVE.

## 9. Doctrine check (ICT 2022 canon)

**Thesis:** Short EURUSD 12/04/2005 — sweep EQH H1 + cạnh trên OB → MSS + displacement + FVG M5 → entry tại retrace, Grade A.

**Cần sửa** (load-bearing trước):
- C5 (MSS M5, load-bearing) — **UNSUPPORTED** · không có giá swing point bị phá hoặc giá đóng nến breaking candle (SKILL.md § MSS: cần body close phá swing ngược hướng sweep) → bổ sung số liệu từ ảnh M5 gốc.
- C4 (OB "respect", đóng nến vào trong OB) — **UNSUPPORTED** · không có giá đóng nến cụ thể của candle phản ứng → ghi rõ giá đóng để verify đóng nến nằm trong OB range (1.29573–1.30110).

**PASS:** C1 (D1 bias Bearish, có mô tả MSS + displacement + Liquidity Void — đủ mô tả định tính để PASS ở mức bias, dù thiếu giá cụ thể); C2 (dealing range H1 arithmetic hợp lệ: High 1.30585 > Low 1.28001, mid 1.29293, entry 1.29729 ở Premium — khớp tính toán); C3 (EQH nằm trong OB, cấu trúc POI hợp lý theo doctrine OB — nến gốc tạo imbalance).

**Verdict: INSUFFICIENT EVIDENCE** — load-bearing C5 (MSS M5) ở UNSUPPORTED; các claim phụ PASS không đủ nâng verdict lên PARTIALLY ALIGNED.

**Notes:** Không có doctrine drift so với note 1 — cùng một khoảng trống UNSUPPORTED cho MSS M5 (thiếu evidence giá cụ thể), là pattern lặp lại của cả batch note sớm, không riêng lệ.

## 10. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật**
- Ví dụ số thật: EQH H1 tại 1.30033 nằm trong OB 1.29573–1.30110 — một target sweep có TÊN và giá cụ thể, khác note 1 (2010-10-19) chỉ nói "old lows" mơ hồ. Tổng quát hóa: mọi sweep claim nên gắn với một mốc giá cụ thể (EQH/EQL/PDH/PDL), không mô tả chung.
- Ví dụ số thật: SL 1.30164 chỉ cách cạnh trên OB (1.30110) 5.4 pip — buffer mỏng. Tổng quát hóa: buffer SL trên điểm sweep nên tính theo ATR hoặc pip trung bình của khung thời gian, không phải khoảng cách cố định tùy cảm giác.

**(b) Bài học quy trình/checklist**
- Setup Quality Checklist 9/9 tick hoàn hảo, không một mục nào chưa đạt — cần cẩn trọng vì một checklist luôn hoàn hảo cho Win có thể phản ánh thiên kiến điền lại sau khi biết outcome hơn là đánh giá khách quan tại thời điểm quyết định.
- Lesson Learned tự nhận "RR > 2R nên lập kế hoạch partial TP trước" — đây là insight tốt nhưng chỉ xuất hiện *sau* lệnh, cần biến thành rule được kiểm tra TRƯỚC lệnh kế tiếp (không chỉ ghi nhận).

**(c) Bài học tâm lý-hành vi**
- Việc chấm Grade A và 90% match trong khi chưa xác nhận độc lập MSS M5 (chỉ mô tả bằng lời) cho thấy khả năng grade bị neo vào outcome (Hit TP) nhiều hơn vào chất lượng bằng chứng thực tế có trong note.

**(d) Rule đề xuất cho Playbook**
- [ ] Mọi sweep claim phải ghi rõ mốc giá cụ thể (EQH/EQL/PDH/PDL) — không dùng mô tả mơ hồ như "old lows".
- [ ] Setup Quality Checklist: nếu tick 9/9 hoàn hảo, thêm 1 dòng giải trình ngắn cho tiêu chí có khả năng bị điền theo outcome cao nhất (MSS, Displacement).
- [ ] RR kế hoạch > 2R → bắt buộc ghi kế hoạch partial TP TRƯỚC khi vào lệnh (không chỉ note lại sau).

**(e) Điều KHÔNG nên học từ lệnh này**
- Không nên coi checklist 9/9 hoàn hảo là chuẩn benchmark cho mọi lệnh sau — cần so sánh với các lệnh Loss để biết checklist có phân biệt được Win/Loss hay chỉ đơn giản luôn tick cao cho Win.
- Không nên dùng "giá đóng nến vào trong OB → respect OB" như một quy luật chắc chắn chỉ từ 1 mẫu — cần kiểm n≥20-30 để biết tỷ lệ OB thật sự được respect khi có đóng nến ngược.
- Không nên lấy Grade A của lệnh này làm chuẩn xác nhận rằng "EQH lồng trong OB" luôn là điểm sweep chất lượng — cần thống kê nhiều mẫu.

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
