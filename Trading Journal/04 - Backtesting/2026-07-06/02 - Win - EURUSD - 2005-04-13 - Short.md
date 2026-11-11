---
type: backtest
backtest_date: 2026-01-07
trade_date: 2005-04-13
symbol: EURUSD
position: Short
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[25-OB-Order-Block|OB]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29239
stop_loss: 1.29545
take_profit: 1.28404
r_planned: 2.78
r_multiple: 2.78
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-13 — EURSUD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | EURUSD                                            |
| Trade Date (dữ liệu) | 2005-04-13                                        |
| Position             | Short                                             |
| Result               | Win                                               |
| Session              | New York                                          |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M5                                                |
| HTF Bias             | Bearish                                           |
| Bias Correct?        | Yes                                               |
| Entry                | 1.29239                                           |
| Stop Loss            | 1.29545                                           |
| Take Profit          | 1.28404                                           |
| R Planned            | 2.78                                              |
| R Multiple (kết quả) | 2.78                                              |
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
  - Buy-side liquidity: Previous Day High
  - Sell-side liquidity: Previous Day Low 

![[Pasted image 20260706054317.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: :H/:: 
- **Dealing Range**: 
	- High: 1.30153 
	- Low 1.28082
	- Giá đang di chuyển về vùng Premium (đúng theo bias Bearish)
- **POI chính**: 
	- Order Block : 1.29907 - 1.29741
	- FVG: 1.29743 - 1.29321
- **Liquidity cần chờ sweep**:
  - Vùng FVG khung H1
  - Order Block
### Phân Tích:
- Hình thành FVG sau nhịp giảm mạnh của ngày 12 để lại 1 FVG khung H1 lớn, phía trên cạnh FVG là Order Block (Bearish)
- FVG và OB nằm trong vùng OTE H1
- Giá retrace về vùng FVG (50%)
- Giá quét qua vùng CE H1 và đóng nến xuống bên dưới (2 lần) -> FVG mạnh
- Có dấu hiệu reject vùng CE, xuống khung M5 quan sát
![[Pasted image 20260706054350.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá di chuyển tới vùng CE của FVG, quét qua và sau đó đóng nến lại bên dưới
- Sau vài nến giá lại quay về đúng CE tạo thành EQH 
- Sau đó giá bật ra với các nến lớn, tuy nhiên râu nến trùng lắp -> không tạo FVG -> Quan sát tiếp không vào vội vì khả năng sẽ quét EQH
- Giá di chuyển ra khỏi FVG sau đó có các nến displacement mạnh phá lên lại FVG, quét cái đỉnh nhỏ và EQH ( quét các inducement)
- Sau khi quét giá bật xuống mạnh kèm nến displacement rất lớn tạo Liquidity Void (có nhiều FVG)
- Sau đó vào New York Killzone giá retrace về CE của FVG mới tạo của nhịp displacement
- Entry tại CE, stoploss đặt trên đỉnh cây nến quét EQH trước đó
- Bên dưới có vùng FVG trùng với Bullish Order BLock => Target tới vùng Overlap
- **Entry trigger**:
  - Liquidity Sweep: Quét qua FVG ( tới CE) + EQH + Inducement
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry
- **Invalidation reason**:
  - Giá đóng qua đỉnh swing high đã quét trước đó
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260706054240.png]]
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
  - Quan trọng là giá đã quét vung CE FVG lớn và bật ra với nến lớn tuy nhiên không tạo FVG -> Khả năng sẽ còn quét
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về premium -> Quét OB + EQH -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- **Kỷ luật lớn nhất của lệnh này là "no FVG → no entry".** Khi giá bật ra khỏi CE nhưng các nến có râu trùng lắp và *không* để lại FVG, đó là dấu hiệu thiếu displacement thật → khả năng cao còn quét EQH/inducement. Không vào vội ở nhịp bật giả này chính là điều tách một entry A khỏi một lệnh bị stop sớm.
- Chỉ nhịp **displacement thật tạo Liquidity Void (nhiều FVG chồng nhau)** sau khi quét inducement mới là xác nhận MSS đáng tin. Đây là bộ lọc chất lượng dịch chuyển, không chỉ nhìn "giá có đi xuống hay không".
- Đọc đúng **cấu trúc thanh khoản nhiều tầng** (CE của FVG H1 → EQH tại CE → inducement) là điểm mạnh nhất của lần backtest này; đó là lý do RR đạt tới 2.78 với SL rất gọn.

### Pattern lặp lại (điều cần để ý lần sau)

- Giá thường **quét CE của FVG HTF ~2 lần** rồi mới thực sự đi. Lần chạm CE đầu tiên hiếm khi là entry — đừng vào ở cú test đầu.
- Sau khi quét CE, giá hay **quay lại tạo EQH ngay tại CE**; EQH này chính là **inducement** sẽ bị lấy trước khi đảo chiều thật. Cẩn thận không entry trước khi inducement đó bị quét kèm displacement.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Chính thức hóa rule **"no FVG, no entry"**: nếu nhịp bật khỏi POI không để lại FVG (râu trùng lắp), coi như *chưa có displacement* → chờ tiếp, giả định còn ít nhất một lần sweep inducement nữa.
- [ ] Đánh dấu mọi **EQH hình thành ngay tại CE là inducement**; chỉ entry sau khi inducement đó bị quét kèm nến displacement tạo FVG mới.
- [ ] Như lệnh 12/04: RR > 2R thì **lên kế hoạch partial TP trước khi vào** — nhất quán hóa thói quen quản lý lệnh giữa các setup.

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | 9/10 |
| POI Selection | 9/10 |
| Liquidity Sweep | 10/10 |
| MSS Confirmation | 9/10 |
| FVG / OB Entry | 9/10 |
| Risk Management (RR) | 8/10 |

**Overall Grade**: A

---

## 7. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL — nhiều tầng.** Đây là note có mô tả thanh khoản phức tạp nhất trong batch: FVG H1 (1.29743–1.29321) + OB (1.29907–1.29741) ở H1, giá quét CE FVG H1 hai lần (≈1.29532 theo tính lại), sau đó tạo EQH ngay tại CE (inducement), rồi mới có displacement thật tạo "Liquidity Void" (nhiều FVG chồng). Đây là cấu trúc IRL (EQH tại CE, một dạng inducement nội bộ) → ERL (draw on liquidity PDL) rõ ràng hơn hẳn 2 note trước — người viết tự nhận ra pattern "quét CE ~2 lần rồi mới đi" trong Lesson Learned, đây là quan sát có giá trị.

**Chất lượng displacement/MSS.** Note phân biệt rõ giữa "nến lớn nhưng râu nến trùng lắp → không tạo FVG → chưa phải displacement thật" và "nến displacement thật tạo Liquidity Void (nhiều FVG chồng)". Đây là tiêu chuẩn phân loại displacement tốt hơn 2 note trước — không chỉ dựa vào kích thước nến mà dựa vào có FVG hay không (imbalance thật).

**Yếu tố thời gian.** Session New York, RR đạt 2.78 (cao nhất trong 5 note batch A) nhờ SL rất gọn (risk 30.6 pip) trong khi reward 83.5 pip.

**Vị trí entry trong dealing range.** High 1.30153/Low 1.28082, mid 1.29117, entry 1.29239 — retracement từ high ≈0.441, chỉ hơi lệch về phía Premium, không sâu như OTE 0.618-0.79 mà note H1 tự nhận "FVG và OB nằm trong vùng OTE H1" — cần lưu ý: OTE ở đây được đo trên leg displacement H1, không phải trên toàn dealing range D1/H1, nên hai phép đo (0.441 dealing range vs OTE displacement leg) không mâu thuẫn nhau, chỉ là 2 khung tham chiếu khác nhau — note không tách rõ 2 khung này, cùng lỗi mà note thứ 5 (04-27) sau này tự phát hiện và ghi lại thành lesson.

**So sánh với lệnh cùng mẫu.** So với [[2026-07-06/01 - Win - EURUSD - 2005-04-12 - Short]] (ngày trước, cùng bias/session) — note này (13/04) có độ sâu phân tích thanh khoản vượt trội: nhận diện được "nến bật giả không tạo FVG" và "inducement tại CE" — đúng là bài học nối tiếp trực tiếp từ kinh nghiệm ngày 12/04 (nơi chưa có khái niệm inducement). Đây là minh chứng cho thấy vault có tiến triển học tập thật giữa các note liên tiếp, không chỉ là ghi chép lặp.

![[EURUSD-20050413-inducement-ce.svg|760]]

## 8. Phản biện chuyên sâu (Devil's Advocate)

**Mode: REVIEW.** Evidence base: text note + 3 screenshot không đọc được. **evidence_sufficiency: thin.**

**Claim graph:**
- C1: D1 bias Bearish (MSS + displacement + Liquidity Void D1).
- C2: H1 dealing range 1.30153–1.28082, giá về Premium; FVG H1 (1.29743–1.29321) + OB liền kề, cả hai trong OTE H1.
- C3: Giá quét CE FVG H1 hai lần, đóng nến dưới CE cả hai lần → "FVG mạnh".
- C4: Giá bật ra với nến lớn nhưng râu trùng lắp → KHÔNG tạo FVG → chưa phải displacement thật (self-identified false break).
- C5: Giá quét lên lại (EQH tại CE + đỉnh nhỏ, tức inducement) rồi mới có displacement thật tạo Liquidity Void nhiều FVG.
- C6 (**load-bearing**): Entry tại CE của FVG mới (đợt displacement thật ở C5), MSS xác nhận, RR 2.78.
- C7 (từ C6): Setup ICT 2022 Model chuẩn 90%, Grade A.

**Load-bearing: C6** — toàn bộ giá trị RR cao (2.78) phụ thuộc vào việc nhận diện đúng "đợt displacement thật" (C5) khác với "đợt bật giả" (C4) — nếu ranh giới này bị đọc ngược (đợt C4 mới là thật, C5 chỉ là tiếp diễn), SL đặt trên đỉnh sweep C5 sẽ sai vị trí.

**Những gì còn đứng:** C4 là một quan sát tự phê bình mạnh — người viết chủ động phân biệt "không có FVG = chưa displacement" ngay trong lúc phân tích, đây là dấu hiệu process tốt hơn (ít nhất về mặt tường thuật) so với 2 note trước.

**O1 · [HINDSIGHT] · fatal · attacks C7**
Claim: "Setup khớp 90% mô hình chuẩn", Grade A, sau khi biết Hit TP.
Fails: không có invalidation condition được cam kết TRƯỚC khi biết đợt C4 là giả — note viết "Quan sát tiếp không vào vội vì khả năng sẽ quét EQH" nhưng đây có thể là suy luận có được SAU khi biết chuỗi sự kiện đầy đủ, viết lại trong replay.
Evidence: toàn bộ mục M5 phân tích viết liền một mạch theo thời gian chart lịch sử, không có mốc phân biệt "đây là điều tôi nghĩ TRƯỚC khi thấy nến tiếp theo" so với "đây là điều tôi thấy SAU".
Consequence: khả năng phân biệt "bật giả (C4) vs bật thật (C5)" mà note tự khen là điểm mạnh có thể chính là hindsight — trong thời gian thực, một nến lớn không FVG hoàn toàn có thể được hiểu là displacement yếu nhưng vẫn hợp lệ, và nhiều trader sẽ vào ngay tại C4 nếu không biết trước C5 sẽ xảy ra.
Your best answer: "Note ghi rõ lý do KHÔNG vào ở C4 là vì thiếu FVG — đây là một rule khách quan (no FVG no entry), không cần biết tương lai." Điều này làm objection NARROW: rule "no FVG no entry" tự nó không cần hindsight để áp dụng — nhưng việc phát hiện ra rule này và tường thuật lại mượt mà theo đúng trình tự "biết trước sẽ có inducement" vẫn có dấu hiệu kể chuyện xuôi theo outcome.
Retracted by: ghi chú thời điểm quan sát C4 được thực hiện tại đúng nến đó (không nhìn về sau), hoặc một note LIVE khác trong vault áp dụng đúng rule "no FVG no entry" tại thời điểm quyết định thật.

**O2 · [UNSUPPORTED] · material · attacks C6**
Claim: "Giá tạo MSS" ở đợt displacement thật (C5), không nêu swing point cụ thể bị phá.
Fails: cùng lỗi note 1 & 2 — SKILL.md § MSS đòi hỏi body close phá swing point, note không cho số liệu.
Evidence: mục M5 chỉ nói "Sau khi quét giá bật xuống mạnh kèm nến displacement rất lớn" — không có giá cụ thể của swing bị phá.
Consequence: không xác nhận độc lập được MSS thật hay chỉ là displacement không kèm structural break.
Your best answer: không có — đây là khoảng trống dữ liệu thuần túy.
Retracted by: ảnh M5 gốc hoặc số liệu swing point.

**O3 · [ARITHMETIC] · minor** — Note ghi CE FVG H1 "≈ vùng retest 50%" nhưng không nêu số cụ thể; tính lại CE = (1.29743+1.29321)/2 = 1.29532. Retracted by: xác nhận số 1.29532 khớp với vùng giá note mô tả "giá quay lại đúng CE tạo EQH" trong ảnh gốc.

**Filter:** 4 objection nháp, cắt 1 (nghi ngờ về khoảng cách giữa 2 lần quét CE — không đủ dữ liệu số để lập luận cụ thể, sẽ là speculative → xóa). Còn 3: 1 fatal hindsight, 1 material unsupported, 1 minor arithmetic.

**Opposite case.** Từ cùng evidence: có thể đợt "bật giả" C4 (nến lớn, không FVG) thực ra ĐÃ là đảo chiều thật, và đợt tiếp tục quét lên (EQH + đỉnh nhỏ) chỉ là một pha continuation ngắn trong xu hướng giảm mới đã bắt đầu — inducement không tồn tại, chỉ là structure noise bình thường của một move mới. Với inverse này, "MSS" thật đã xảy ra sớm hơn ở C4, và entry lý tưởng theo inverse phải sớm hơn entry thực tế của note. Tự phản biện: inverse này yếu vì chính note đã quan sát KHÔNG có FVG ở C4 — nếu không có imbalance, doctrine không cho gọi đó là displacement, nên MSS tại C4 (nếu có) không đi kèm displacement hợp lệ theo canon. Nhãn: **weaker but non-trivial** — inverse chỉ sống nếu doctrine chấp nhận MSS không cần displacement kèm theo (canon batch này không fix rõ ràng điểm này).

Distinguishing observable: liệu nến C4 có đóng vượt qua swing point cấu trúc ngắn hạn hay không — nếu có, cả 2 cách đọc (MSS sớm ở C4 hay MSS muộn ở C5) đều cần được cân nhắc lại từ ảnh gốc.

**Verdict: UNPROVEN.** Thin evidence sufficiency. C6 UNSUPPORTED, C7 HINDSIGHT fatal — nhưng không có [CHART]/[ARITHMETIC] nào FAIL trực tiếp claim cốt lõi nên không rơi xuống BROKEN; dừng ở UNPROVEN.

**Điều tôi không phá được:** khả năng phân biệt "displacement có FVG" vs "bật giả không FVG" là một tiêu chuẩn doctrine hợp lệ (SKILL.md § Displacement: "move lệt bệt overlapping không phải displacement dù đúng hướng") — về mặt định nghĩa, cách note áp dụng tiêu chuẩn này là đúng, chỉ nghi ngờ THỜI ĐIỂM áp dụng (trước hay sau khi biết outcome).

**Điều critique này không xác lập:** không xác lập MSS tại C5 có body close hợp lệ; không xác lập việc phân biệt C4/C5 được thực hiện tại hard right edge thật hay chỉ trong lúc replay.

**Falsification tests:**
1. Kiểm ảnh M5 gốc theo timestamp nến: xác nhận nến C4 (bật giả) thực sự không tạo FVG (không có gap 3-nến) theo đúng định nghĩa — đóng O1 phần nghi ngờ về tính khách quan của rule nếu FVG thật sự vắng mặt tại C4.
2. Tìm swing point cụ thể bị phá bởi MSS tại C5 trong ảnh gốc → đóng O2.
3. Rà 5-10 note khác có claim "no FVG = chưa displacement" để xem rule này được áp dụng NHẤT QUÁN trước hay chỉ xuất hiện ở note Win (nếu chỉ ở Win, tăng nghi ngờ hindsight-selective ở O1).

## 9. Doctrine check (ICT 2022 canon)

**Thesis:** Short EURUSD 13/04/2005 — quét CE FVG H1 2 lần + inducement (EQH tại CE) → displacement thật tạo Liquidity Void → MSS + FVG M5 → entry, RR 2.78, Grade A.

**Cần sửa** (load-bearing trước):
- C6 (MSS tại đợt displacement thật, load-bearing) — **UNSUPPORTED** · không có swing point/giá đóng nến cụ thể (SKILL.md § MSS) → cần ảnh xác nhận.
- C4 (nến bật giả "không tạo FVG") — **AMBIGUOUS** · doctrine không fix rõ ràng liệu một move không tạo FVG có thể vẫn là displacement hợp lệ theo tiêu chuẩn khác (vd body-to-range ratio) hay nhất thiết phải có FVG mới được gọi displacement (SKILL.md § Displacement chỉ nói "move lệt bệt overlapping không phải displacement" — không nói rõ "không FVG" ⟺ "không displacement" là quan hệ hai chiều) → đây là doctrine gap, không phải FAIL. Đọc theo chuẩn "FVG là bằng chứng tất yếu" thì claim PASS; đọc theo chuẩn "FVG chỉ là MỘT bằng chứng, không phải điều kiện cần" thì claim cần thêm bằng chứng khác (body size, momentum) mới PASS.

**PASS:** C1 (bias D1, mô tả đủ định tính); C2 (dealing range arithmetic hợp lệ, entry ở Premium khớp bias — mid 1.29117, entry 1.29239); C3 (CE FVG H1 tính lại 1.29532, khớp mô tả "quét CE 2 lần" — không mâu thuẫn arithmetic); C5 (inducement EQH tại CE — mô tả đúng khái niệm inducement theo canon: liquidity pool nhỏ bị quét trước move thật).

**Verdict: INSUFFICIENT EVIDENCE** — load-bearing C6 UNSUPPORTED.

**Notes:** Doctrine gap phát hiện ở C4 nên được ghi vào doctrine.md như một mục bổ sung: "một move không tạo FVG (3-candle gap) có thể vẫn có tốc độ/kích thước đủ tiêu chuẩn displacement khác (momentum, body ratio) hay không — canon hiện tại chỉ định nghĩa FVG là SẢN PHẨM của displacement, không định nghĩa ngược lại rằng thiếu FVG ⟹ thiếu displacement." Đây là gap thật, không phải lỗi người dùng.

## 10. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật**
- Ví dụ số thật: CE FVG H1 = (1.29743+1.29321)/2 = 1.29532, giá quét vùng này 2 lần trước khi có move thật. Tổng quát hóa: một CE bị test nhiều lần không tự động có nghĩa CE đó "mạnh hơn" — cần phân biệt test có tạo phản ứng đủ (displacement/FVG mới) hay chỉ là giá chạm rồi đi tiếp.
- Ví dụ số thật: RR đạt 2.78 với risk chỉ 30.6 pip nhờ nhận diện đúng đợt displacement thật (không phải đợt bật giả) để đặt SL gọn hơn. Tổng quát hóa: SL đặt trên/dưới đúng đợt sweep "cuối cùng" (closest to entry) luôn cho RR tốt hơn SL đặt trên sweep đầu tiên gặp phải.

**(b) Bài học quy trình/checklist**
- Rule "no FVG, no entry" được note đề xuất là một tiêu chuẩn đo lường được — nên test trên nhiều mẫu để xác nhận rule không chỉ hợp lý về lý thuyết mà còn phân biệt được Win/Loss trong thực tế (tránh rule chỉ đúng với chính mẫu tạo ra nó).
- Cần ghi rõ MỐC THỜI GIAN của mỗi quan sát trong phần phân tích M5 (ví dụ "tại nến X tôi nghĩ Y, tại nến X+3 tôi thấy Z") để tách bạch suy luận tại thời điểm quyết định khỏi suy luận trong lúc viết lại (replay).

**(c) Bài học tâm lý-hành vi**
- Khả năng cao câu chuyện "biết trước sẽ quét EQH nên không vào vội" được viết lại mượt mà SAU khi biết toàn bộ diễn biến — nguy cơ hindsight cao nhất trong 3 note đã xử lý vì đây là note có narrative "tôi đã đúng khi kiên nhẫn" rõ nét nhất.

**(d) Rule đề xuất cho Playbook**
- [ ] Chính thức hóa "no FVG, no entry" nhưng bắt buộc kiểm định trên ≥20 mẫu (bao gồm cả Loss) trước khi coi là rule chính thức.
- [ ] Mọi phân tích M5 phải đánh dấu rõ ràng thời điểm quan sát (nến số mấy) để phân biệt suy luận tại right edge với suy luận hồi tưởng.
- [ ] Khi SL được đặt trên đợt sweep thứ 2 (sau khi đã có 1 lần sweep thất bại/giả), ghi rõ lý do tại sao đợt 1 KHÔNG được coi là điểm sweep chính, để tránh cherry-pick sweep phù hợp với outcome.

**(e) Điều KHÔNG nên học từ lệnh này**
- Không nên coi việc phân biệt "bật giả không FVG" vs "displacement thật có FVG" là một kỹ năng đã thành thục chỉ từ 1 mẫu Win — đây có thể là nhận diện đúng một lần nhờ hindsight, không phải một kỹ năng phản xạ tại real-time.
- Không nên dùng RR 2.78 làm chuẩn kỳ vọng cho các setup dạng "CE test 2 lần" — mẫu quá nhỏ (n=1) để rút expectancy.
- Không nên coi câu chuyện tường thuật mượt mà (giá làm đúng những gì mình đoán) là bằng chứng cho năng lực dự đoán — chuỗi sự kiện được kể lại sau khi đã biết toàn bộ kết quả luôn có xu hướng nghe hợp lý hơn thực tế lúc đó.

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[13-FVG-Fair-Value-Gap]] · [[26-OTE-Optimal-Trade-Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: _(chưa gán note lỗi)_
