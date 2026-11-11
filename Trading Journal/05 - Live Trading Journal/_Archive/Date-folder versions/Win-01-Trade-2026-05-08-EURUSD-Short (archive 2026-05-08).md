---
date: 2026-05-08
symbol: EURUSD
position: Short
result: Win
session: London
setup: NQ ICT 2022 AM Delivery
entry_model: Buy-side Liquidity + Fair Value Gap + Order Blocks
entry_timeframe: 
higher_timeframe_bias: 
bias_correct: 
entry_price: 1.17689
take_profit: 1.17604
stop_loss: 1.17785
exit_price: 1.17604
pnl: 100
r_multiple: 0.89
planned_rr: 0.89
risk_percent: 
confidence: 3
mistakes: 
emotions:
  - Focused
tags:
  - BuySideLiquidity
  - FairValueGap
  - OrderBlocks
  - KillZones
  - DailyBias
source_id: 2017
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 2, minor: 1}
da_opposite_case: "not viable"
---
# Trade 2026-05-08 - EURUSD Short Win

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | EURUSD |
| Position | Short |
| Result | Win |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Buy-side Liquidity + Fair Value Gap + Order Blocks |
| HTF Bias |  |
| Premium/Discount |  |
| Power of 3 |  |
| Confidence | 3/5 (Medium) |
| Entry | 1.17689 |
| Stop Loss | 1.17785 |
| Take Profit | 1.17604 |
| Exit | 1.17604 |
| PnL | 100.0 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-05-09 03:38:00 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: N/A
- **Premium/Discount**: N/A
- **Power of 3 Phase**: N/A

=============== D1 ===============

- Daily bias: Giá đang trong nhịp giảm - Bearish bias
=============== H1 ===============

- Giá tạo 1 Bearish Order Block sau 1 nhịp giảm mạnh (displacement)
- Giá tạo FVG trên đường di chuyển xuống
- Giá trên khung H1 hồi về vùng OB
=============== M15 ===============

- Giá chạm vào OB và xuất hiện tín hiệu rejection
- OB nằm trong vùng OTE
- Giá hồi về 50% mean threshold và bật ngược lại
- Entry khi giá retrace OB

================= ENTRY =============

- Entry price: 1.17689
- Exist price: 1.17604
- Stoploss: 1.17785
- RR: 1:2

### Charts

![[EURUSD-20260508-2017-1.png]]
![[EURUSD-20260508-2017-2.png]]
![[EURUSD-20260508-2017-3.png]]
![[EURUSD-20260508-2017-4.png]]
![[EURUSD-20260508-2017-5.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Market Structure Shift + Displacement
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] No high-impact news events imminent (check economic calendar)
- [x] Rejection Validation When Enter PD Array Zones
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Risking no more than 0.5% of account equity

---

## 3. Execution Review

- Giá chạy xuống sau khi chạm entry ở OB
- Đóng lệnh khi giá đạt 2R

**Emotions**: Focused

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit)
- **Mistake chính**:
  - [[Mistake - ]]
- **Nguyên nhân gốc rễ**:
  - (trống trong bản gốc — dựa trên dữ kiện có trong file: entry khớp với OB retrace + rejection tại M15 như narrative mô tả; TP = exit_price = 1.17604 xác nhận lệnh chạy đến đúng target đã định, không phải manual close sớm `(suy luận có điều kiện — cần chart xác nhận vùng OB/FVG thật)`.)

---

## 5. Lesson Learned

### Bài học kỹ thuật

- (Bản gốc để trống — không có bullet gốc để giữ.)
- RR thật tính từ entry/SL/TP = 0.885 (risk 0.00096, reward 0.00085), khớp chính xác với field `planned_rr: 0.89` — nhưng **không khớp** với câu văn trong body "RR: 1:2" (O1). Kỹ thuật đo RR trong journal không nhất quán giữa frontmatter (đúng toán) và narrative (sai/lạc hậu).
- Execution Review ghi "Đóng lệnh khi giá đạt 2R" nhưng exit_price = take_profit = 1.17604 và r_multiple = 0.89 — câu "2R" không khớp với bất kỳ số liệu nào khác trong file (O2).

### Bài học tâm lý

- (Bản gốc để trống.)
- Confidence chỉ 3/5 (Medium) đi kèm một setup có RR thật <1 — đáng chú ý là user vẫn vào lệnh dù không tự tin cao, RR không đạt chuẩn tối thiểu; đây là dấu hiệu risk/reward acceptance không nhất quán với mức tự tin thấp, dù không đủ evidence để kết luận nguyên nhân tâm lý cụ thể (`suy luận có điều kiện`).

### Bài học quy trình & risk

- **RR tối thiểu**: checklist section 2 không có dòng "RR tối thiểu ≥ 1:X" nào để tick, nhưng đối chiếu với checklist các lệnh khác trong hệ thống của user (vd `Win-01-04-20` dùng chuẩn 1:3), RR 0.89 của lệnh này thấp hơn risk chấp nhận — risk nhiều hơn reward tại một lệnh vẫn được tính Win cùng cấp với các lệnh RR≥2 (liên hệ CS-O6).
- risk_percent để trống hoàn toàn trong frontmatter — không thể kiểm lệnh này có breach rule 0.5% hay không, khác với các lệnh khác trong cùng cụm ngày có field risk_percent điền rõ (liên hệ CS-O1 về rule drift ghi nhận risk).

### Rule cần thêm/cập nhật

- [ ] **KIỂM TRA ĐƯỢC**: Trước khi tick "Fair Value Gap (FVG) or Order Block (OB) provides confluence" trong checklist, RR thật (tính từ entry/SL/TP) phải ≥ 1.0 — nếu < 1.0, không tick mục này và bắt buộc field `mistakes:` phải gắn tag "Not enough RR" (đóng O1/O3, đồng bộ với cách lệnh `Win-01-05-13-NDX-Long` tự gắn tag 05 khi RR 0.6).
- [ ] **KIỂM TRA ĐƯỢC**: Câu văn RR trong body (vd "RR: 1:2") phải được tính lại bằng công thức risk=|entry-SL|, reward=|entry-TP| ngay khi ghi journal, không copy số ước lượng — kiểm bằng cách so khớp câu văn với field `planned_rr` mỗi lần tạo file mới (đóng O1).

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only + 5 link chart Obsidian không có ảnh thật trong dataset → không dùng tier [CHART]. Sufficiency: **thin** — load-bearing claim (RR thật của lệnh) tự kiểm được bằng arithmetic thuần túy từ 3 số (entry/SL/TP) đã cho, nên objection arithmetic ở đây mạnh dù sufficiency chart là thin.

**Thesis & claims**:
- C1: HTF bias D1 Bearish, entry Short khớp hướng — claim văn xuôi ("Giá đang trong nhịp giảm - Bearish bias"), không kiểm được từ evidence hiện có.
- C2: H1 có Bearish OB sau displacement, FVG hình thành trên đường giảm, giá hồi về vùng OB ở M15 với rejection — chuỗi claim liên tiếp, mỗi bước là claim văn xuôi không có evidence chart xác nhận.
- C3 (load-bearing): "RR: 1:2" — câu văn khẳng định lệnh có reward gấp đôi risk, dùng để biện minh setup "đủ chuẩn" theo checklist mọi mục đều tick `[x]` bao gồm cả các mục về structure.
- C4: Lệnh thắng (Win, TP hit, pnl +100) → checklist toàn `[x]` được đọc như "setup đã được validate đầy đủ trước entry".

Suy luận: nếu C3 đúng (RR thật 1:2), setup trông "chuẩn" theo mọi tiêu chí; C4 (outcome Win) không chứng minh C1–C3 đúng — chỉ là kết quả.

**Điều gì đứng vững**: Entry/SL/TP arithmetic khớp field `planned_rr: 0.89` và `r_multiple: 0.89` — hai field độc lập trong frontmatter đồng thuận với nhau (risk=0.00096, reward=0.00085, RR=0.885≈0.89). Direction Short khớp với TP < Entry < SL (đúng cấu trúc lệnh Short). Exit = TP = 1.17604, khớp Result "Hit Take Profit" — không có mâu thuẫn ở tầng thực thi.

**Objections**:

**O1 · [ARITHMETIC] · fatal · attacks C3 (load-bearing)**
Claim: "RR: 1:2" (dòng ENTRY trong body).
Evidence: risk = |1.17689 − 1.17785| = 0.00096; reward = |1.17604 − 1.17689| = 0.00085; RR thật = 0.00085/0.00096 = **0.885**, không phải 2. Số này khớp chính xác với `planned_rr: 0.89` và `r_multiple: 0.89` trong frontmatter — hai nguồn độc lập (arithmetic tự tính + field có sẵn) đều bác câu văn "1:2".
Consequence: câu văn "RR: 1:2" trong phần phân tích tay là **sai toán**, không phải chỉ lệch nhẹ — 2.0 vs 0.885 là sai lệch >2×. Nếu user đọc lại lệnh này trong tương lai và tin vào câu văn thay vì frontmatter, sẽ đánh giá sai chất lượng setup (nghĩ RR tốt hơn thực tế gấp hơn 2 lần). Đây chính là RR<1 mà brief đã lưu ý — risk (0.00096) lớn hơn reward (0.00085), user đang risk nhiều hơn số có thể thu về.
Your best answer: "1:2 là ước tính ban đầu lúc lên kế hoạch, giá sau đó không đạt xa như dự kiến nên RR thật giảm." — Không cứu được: TP = 1.17604 = exit_price = giá đã dùng để tính planned_rr = 0.89; không có TP khác nào được nêu để "1:2" có thể đúng ở bất kỳ mức giá nào đã ghi trong file.
Retracted by: một TP dự kiến khác (không phải 1.17604) được nêu ở đâu đó trong file để "1:2" khớp với mức đó — hiện không có.

**O2 · [SELF-CONTRADICTION] · material · attacks C4**
Claim: Execution Review "Đóng lệnh khi giá đạt 2R".
Evidence: exit_price = take_profit = 1.17604 (Result: "Hit Take Profit", không phải manual close ở mức 2R); r_multiple = 0.89. "2R" không khớp bất kỳ số liệu nào có trong file (RR thật 0.89, không phải 2).
Consequence: câu "Đóng lệnh khi giá đạt 2R" là một record sai về cách lệnh đã đóng — lệnh đóng vì hit TP đã định trước (0.89R), không phải một quyết định manual tại 2R. Điều này cùng gốc lỗi với O1 (nhầm lẫn giữa RR dự kiến "2" và RR thật 0.89), cho thấy pattern lặp lại chứ không phải lỗi đánh máy đơn lẻ.
Your best answer: "2R có thể tính trên một mốc SL khác nhỏ hơn được điều chỉnh sau entry." — Không có field nào trong file ghi SL được điều chỉnh; `stop_loss` chỉ có một giá trị 1.17785 xuyên suốt.
Retracted by: ghi chú xác nhận SL đã được trail/điều chỉnh xuống mức nào đó khiến 2R khớp — hiện không có.

**O3 · [UNSUPPORTED] · material** — Toàn bộ checklist section 2 tick `[x]` 9/9 bao gồm "Market Structure Shift + Displacement" và "Stop loss is placed beyond the nearest structure level + Buffer", nhưng risk_percent để trống hoàn toàn trong frontmatter — không thể kiểm mục cuối cùng ("Risking no more than 0.5%") có thực sự đúng hay chỉ tick theo quán tính, vì không có số để đối chiếu. Retracted by: điền risk_percent thật của lệnh này.

**O4 · [DOCTRINE] · minor** — Checklist tick "Rejection Validation When Enter PD Array Zones" nhưng narrative M15 chỉ ghi "xuất hiện tín hiệu rejection" — không tên rõ *loại* rejection (wick, engulfing, CISD) theo chuẩn cần cho "rejection validation" — doctrine yêu cầu xác nhận cụ thể hơn "có dấu hiệu", nhưng đây là gap nhỏ so với O1/O2. Retracted by: nêu rõ loại rejection cụ thể quan sát được ở M15.

Drafted 5, cut 1 (draft về "OB vs FVG bị gộp lẫn" không tách được thành objection riêng — cùng gốc thiếu chart với O3, gộp vào ghi chú).

**Verdict**: **BROKEN** — load-bearing claim C3 (RR 1:2) sai toán, chênh >2× so với số liệu chính chủ (O1). Evidence sufficiency thin cho các claim structure (C1, C2) nhưng O1 là arithmetic thuần túy, không cần chart để phán — nên BROKEN áp dụng độc lập với sufficiency chart.
Tôi đã tấn công gì mà không phá được: hướng lệnh (Short khớp bias claim), thực thi kỹ thuật (entry/exit/TP nhất quán với nhau).
Critique này KHÔNG xác lập: (1) OB/FVG/displacement ở H1/M15 có tồn tại thật trên chart hay không; (2) liệu setup có "đúng" theo ICT doctrine ở tầng structure; (3) hướng đi tiếp theo của giá sau TP — outcome Win không chứng minh RR 1:2 đúng, ngược lại arithmetic cho thấy RR thật chỉ 0.89.

**Opposite Case**: Đổi vai của "RR: 1:2" — thay vì đọc là lỗi tính, đọc như **giá trị RR mục tiêu ban đầu (kế hoạch)** trước khi entry cuối cùng bị điều chỉnh gần hơn (entry price cuối 1.17689 khác với entry ban đầu dự kiến ở mức xa hơn), khiến RR thật giảm về 0.89 nhưng câu văn "1:2" là di sản từ plan gốc chưa cập nhật. Load-bearing claim của kèo ngược: có một entry price kế hoạch khác với entry price thực thi.
Strongest self-objection: không có field "planned_entry" nào khác 1.17689 xuất hiện trong file — toàn bộ file chỉ có một entry_price duy nhất ở cả frontmatter và body, nên "entry đã đổi" là suy diễn không có chỗ bám.
Strength label: **not viable** — không có fact nào trong file gợi ý một entry/TP khác từng được cân nhắc; câu "1:2" nhiều khả năng đơn giản là lỗi ghi/copy số, không phải di sản kế hoạch.
Observable duy nhất phân biệt hai reading: lịch sử sửa file (version history) của dòng "RR: 1:2" và trường entry_price — nếu "1:2" được viết trước khi entry_price chốt ở 1.17689, kèo ngược có cơ sở; nếu viết cùng lúc/sau, thesis gốc (lỗi ghi) đúng. Không có trong file.

## 9. Opposite Case (Counter-Argument)

(Xem mục 8 — Opposite Case đã trình bày đầy đủ ở trên để tránh lặp nội dung.)

## 10. Falsification Tests

1. **Test cho O1/O2**: Rà toàn bộ 27 file journal, đếm số lần câu văn RR trong body khác với `planned_rr`/`r_multiple` field ≥ 0.3 (chênh lệch tuyệt đối). Nếu ≥ 3 file khác cũng có pattern này, đây là lỗi hệ thống ghi RR bằng tay không đối chiếu công thức — không phải riêng lệnh 05-08 (mở rộng O1 thành finding cấp cross-setup nếu đúng).
2. **Test cho O3**: Đối chiếu 8 lệnh có `risk_percent: 5%` (đã liệt kê CS-O1) với các lệnh risk_percent trống như lệnh này — nếu risk_percent trống luôn đi kèm checklist tick `[x]` đầy đủ dòng risk mà không có cách kiểm, đây là lỗ hổng ghi chép hệ thống, đóng O3 theo hướng "không kiểm được, không phải breach riêng".
3. Không có test 3 phù hợp cho O4 (minor, không cần falsification riêng theo brief) — bỏ.
