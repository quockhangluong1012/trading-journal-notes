---
type: backtest
backtest_date: 2026-07-07
trade_date: 2005-04-27
symbol: EURUSD
position: Long
result: Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[17-Inverse-Fair-Value-Gap-iFVG|IFVG]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29165
stop_loss: 1.29042
take_profit: 1.29467
r_planned: 2.48
r_multiple: 2.48
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-27 — EURUSD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2005-04-27     |
| Position             | Long           |
| Result               | Win            |
| Session              | London         |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bullish        |
| Bias Correct?        | Yes            |
| Entry                | 1.29165        |
| Stop Loss            | 1.29042        |
| Take Profit          | 1.29467        |
| R Planned            | 2.48           |
| R Multiple (kết quả) | 2.48           |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang HH/HL
  - Nhịp displacement có tạo FVG khung D1
  - => Bias chuyển sang Bullish
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day/Week High
  - Sell-side liquidity: Previous Day/Week Low 
![[Pasted image 20260707075638.png]]
### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL
- **Dealing Range**: 
	- High: 1.31266
	- Low 1.28777
	- Giá đang di chuyển về vùng Discount (đúng theo bias Bullish)
- **POI chính**: 
	- Balance Price Range (BPR): 1.29084 - 1.28927
- **Liquidity cần chờ sweep**:
  - Giá lắp Bullish Liquidity Void khung H1 (2005-04-18)
  - Giá phản ứng tại BPR khung H1
### Phân Tích:
- Ngày 18/2/2005 Giá tạo 1 bearish FVG ( khi đó vần là Bias Bearish).
- Sau đó vài cây nến giá tạo 1 nhịp giá displacement với các nến bullish lớn, đồng thời tạo FVG trùng lắp với iFVG (Bearish FVG của nhịp giá trước bị phá lên trên hình thành IFVG) tạo thành 1 vùng BPR
- Nhịp giá tạo BPR này đồng thời hình thành MSS + FVG trên khung D1
- Đồng thời nhịp displacement cũng tạo Liquidity Void
- Sau đó vài ngày giá quay lại fill Liquidity Void đó và retest vùng BPR
- Khung H1, xuất hiện phản ứng ngay sau đó giá di vào khoảng 1/4 vùng với cây nến xanh lớn
- Xuống khung M5 quan sát
![[Pasted image 20260707075743.png]]
## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá phản ứng khi vào vùng BPR (chưa tới CE)
- Giá tạo MSS + FVG với các nến tăng lớn
- Giá quá qua swing high cũ sau đó retrace về vùng FVG
- Entry khi giá vào 50% FVG
- Stoploss: swing low trước đó của nhịp quét ( giữa cạnh trên và CE BPR)
- **Entry trigger**:
  - Liquidity Sweep: Giá lắp Liquidity Void + vùng BPR
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là BPR)
- **Invalidation reason**:
  - Giá đóng qua đáy sweep/ qua BPR
- **Tôi có chờ đủ điều kiện không?** Có
![[Pasted image 20260707075820.png]]

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

- **Result**: 
	- Đóng 50% lệnh khi giá lắp tới CE của 1 Bearish Liquidity Void phía trên (chỗ này tôi quên mất khi giá quét lên Liquidity Void thường phá rất nhanh mà out sớm mất 50%) - tỉ lệ 2.48R
	- Đóng 50% còn lại khi giá quét qua đỉnh tạo Liquidity Void ( giá quét đúng râu nến qua và đóng lại bên dưới) - tỉ lệ nếu từ gốc lên là 4.2R, từ điểm take partial là 1.72R
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone (London)
  - Giá fill Bullish Liquidity Void (18/04/2005)
  - Giá đang trong vùng Discount
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về discount -> Quét EQL + CE Unicorn -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 80%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
	- Cần nhắc quan sát thêm khung M1 khi giá retrace về FVG M5

---

## 5. Lesson Learned

### Bài học kỹ thuật

> [!summary] POI sâu hơn OTE — lợi thế RR hay bẫy sweep?
> - **POI (BPR) nằm ở ~0.88 – 0.94 retracement của Dealing Range H1** (High `1.31266` / Low `1.28777`), Entry ở ~0.84 — đều **sâu hơn OTE (0.62 – 0.79)**. Về bản chất, vào sâu trong Discount là **tốt cho RR** (mua "rẻ"), KHÔNG phải lỗi.
> - **Nguy hiểm thật nằm ở external liquidity chưa quét:** đáy Dealing Range `1.28777` (external SSL) vẫn còn **~15 pip NẰM DƯỚI đáy BPR (`1.28927`)**. Một POI nằm *phía trên* vũng thanh khoản chưa bị lấy luôn có rủi ro bị **sweep trước** — nếu draw of liquidity thật của phiên là đáy range thì SL `1.29042` bị càn qua trước khi giá đi đúng hướng.
> - **Vì sao lệnh này vẫn thắng:** độ sâu **trùng khớp** với chỗ thuật toán cần lấy thanh khoản — fill **Bullish Liquidity Void (18/04)** + quét EQL — và tôi vào bằng **confirmation M5 (phản ứng → MSS → displacement → FVG → retrace 50%)**, KHÔNG đặt limit mù ở POI sâu. Chính hai yếu tố này trung hoà rủi ro độ sâu.
> - **Phân biệt 2 phép đo fib (điểm dễ nhầm nhất):** OTE đo trên **displacement leg**; Premium/Discount đo trên **Dealing Range**. "Sâu hơn OTE" trên dealing range = tốt (rẻ); nhưng nếu nhịp *displacement* bị retrace > 0.79 thì đó là **cờ vàng cho bias** (nhịp tăng gần bị negate → nghi ngờ order flow).

### Pattern lặp lại (điều cần để ý lần sau)

- **Xu hướng chọn POI rất sâu, sát đáy range.** Lần sau khi POI sâu hơn 0.79 → phản xạ đầu tiên phải là: *"còn external liquidity nào chưa quét nằm dưới POI không?"*
- **Out sớm 50% khi giá quét Liquidity Void** (đã ghi ở mục 4): giá thường phá Void **rất nhanh** → cân nhắc để runner chạy qua Void thay vì chốt tại CE của Void.

### Rule cần thêm/cập nhật vào Playbook

- [ ] **Rule "Deep POI":** Khi POI (BPR/FVG/OB) nằm **sâu hơn 0.79 của Dealing Range** → bắt buộc kiểm tra external liquidity chưa quét bên dưới. Nếu còn → **hoặc** chờ giá quét nốt vũng đó rồi mới tìm entry, **hoặc** giảm size; và **bắt buộc** vào bằng confirmation LTF (M5/M1), cấm limit mù.
- [ ] **Rule ghi log:** luôn ghi rõ đang neo fib vào **displacement leg** (cho OTE) hay **Dealing Range** (cho Premium/Discount) để tránh lẫn khung.
- [ ] **Backtest tag:** đánh tag riêng nhóm lệnh `POI-deeper-than-OTE` để **win rate + expectancy của nhóm** tự phán xử — đừng để 1 lệnh Win "phong thánh" cho kiểu entry này (cảnh giác curve-fitting, đây mới là 1 mẫu).

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

**Overall Grade**: A

---

## 7. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL — điểm mấu chốt của note này.** Note tự phát hiện và ghi thành lesson (mục 5, box summary) một quan sát quan trọng: POI (BPR 1.28927–1.29084) nằm ở retracement ≈0.84–0.94 của dealing range H1 (High 1.31266/Low 1.28777) — SÂU HƠN OTE chuẩn (0.618–0.79) — và ngay dưới BPR còn 15 pip external liquidity (SSL đáy range 1.28777) CHƯA bị quét trước khi entry. Đây là bản đồ ERL rõ ràng nhất trong cả 5 note: note chủ động cảnh báo rủi ro sweep-through chính mình, không chờ phản biện bên ngoài mới thấy.

**Chất lượng displacement/MSS.** D1 có MSS + displacement + FVG D1 — mô tả tương tự note 4 (cùng nguồn gốc bias Bullish D1, có thể từ đợt displacement D1 gần giống nhau vì 2 note cách nhau vài ngày, cùng cụm dealing range H1 High 1.31266/Low 1.28777).

**Yếu tố thời gian.** Session London, entry sau khi giá quay lại lấp Liquidity Void tạo ngày 18/04 rồi retest BPR.

**Doctrine check iFVG — trọng tâm bắt buộc theo brief.** Note mô tả: "Giá tạo 1 bearish FVG (18/04, khi bias Bearish). Sau đó vài nến giá tạo displacement bullish lớn, đồng thời tạo FVG trùng lắp với iFVG (Bearish FVG của nhịp giá trước bị phá lên trên hình thành iFVG) tạo thành 1 vùng BPR." Đây là mô tả ĐÚNG canon: iFVG chỉ tồn tại SAU khi FVG gốc (bearish) bị đóng nến xuyên qua (SKILL.md § Inversion FVG: "Chỉ tồn tại sau khi FVG bị close xuyên qua. Trước đó gọi IFVG là hindsight/overcall"). Note không gọi vùng này là iFVG NGAY khi FVG bearish vừa hình thành — chỉ gọi iFVG SAU khi ghi rõ "bị phá lên trên" — đúng trình tự thời gian theo doctrine. Đây là điểm khác biệt tích cực rõ rệt so với các note khác trong batch: label được áp dụng đúng chuẩn, không overcall sớm.

**BPR (Balance Price Range) — kiểm tra khái niệm liên quan.** BPR trong note = vùng chồng lấp giữa iFVG (bearish FVG đã bị phá) và FVG bullish mới hình thành cùng lúc trong displacement leg — đúng định nghĩa BPR chuẩn ICT (hai FVG đối nghịch chồng lên nhau tạo vùng cân bằng). Không có trong bảng thuật ngữ nhanh SKILL.md nhưng khái niệm nhất quán với cách iFVG + FVG được mô tả.

**So sánh với lệnh cùng mẫu.** So với [[2026-07-07/02 - Win - EURUSD - 2005-04-24 - Long]] — cùng dealing range H1 (High 1.31266/Low 1.28777), cùng bias D1, nhưng note 24/04 dùng Unicorn (breaker+FVG) còn note 27/04 dùng BPR (iFVG+FVG) — cho thấy trong cùng một nhịp thị trường lớn, vault ghi nhận ít nhất 2 loại POI khác nhau hình thành gần nhau — hữu ích để kiểm tra không có double-counting nếu tính thống kê theo giai đoạn.

![[EURUSD-20050427-ifvg-bpr.svg|760]]

## 8. Phản biện chuyên sâu (Devil's Advocate)

**Mode: REVIEW.** Evidence base: text note + 3 screenshot không đọc được. **evidence_sufficiency: thin.**

**Claim graph:**
- C1: D1 bias Bullish (MSS + displacement + FVG D1), cùng bối cảnh với note 24/04.
- C2: 18/04 hình thành bearish FVG H1 (khi bias còn Bearish).
- C3: Vài nến sau, displacement bullish lớn phá NGƯỢC lên qua bearish FVG này → hình thành iFVG (đúng trình tự thời gian theo doctrine) + FVG bullish mới chồng lấp → BPR (1.28927–1.29084).
- C4: BPR nằm ở retracement ≈0.84-0.94 dealing range H1 — sâu hơn OTE 0.618-0.79.
- C5: External SSL (đáy range 1.28777) còn 15 pip CHƯA quét dưới BPR — note tự nhận là rủi ro.
- C6 (**load-bearing**): Giá phản ứng tại BPR (chưa tới CE), M5 xác nhận MSS+displacement+FVG → entry 1.29165, SL 1.29042 (giữa cạnh trên và CE BPR).
- C7: Setup 80% khớp mô hình chuẩn (note tự chấm THẤP HƠN các note khác — đáng chú ý), Grade A, RR 2.48 (thoát 50% sớm, 50% sau ở R cao hơn).

**Load-bearing: C6**, phụ thuộc vào C3 (iFVG hình thành đúng thời điểm) — nếu displacement bullish không thực sự đóng nến xuyên qua bearish FVG cũ theo đúng nghĩa "close through", iFVG chưa hợp lệ theo doctrine, và BPR (vốn cần iFVG là một nửa cấu trúc) mất một chân đứng.

**Những gì còn đứng:** Trình tự thời gian mô tả iFVG là chuẩn nhất trong 5 note — không có overcall sớm. C4+C5 là tự phê bình chủ động, hiếm gặp và có giá trị cao.

**O1 · [UNSUPPORTED] · material · attacks C3**
Claim: "FVG bearish 18/04 bị phá lên trên hình thành iFVG" — không nêu giá đóng nến cụ thể của candle được cho là đã đóng xuyên qua FVG bearish.
Fails: SKILL.md § Inversion FVG đòi hỏi FVG phải "bị close xuyên qua" — note không cho giá đóng nến cụ thể để verify đóng nến có thực sự vượt qua toàn bộ FVG bearish hay chỉ chạm/xuyên một phần bằng wick.
Evidence: mục "Phân Tích" H1 chỉ nói "tạo FVG trùng lắp với iFVG... tạo thành 1 vùng BPR" — không có số giá đóng nến của candle đảo.
Consequence: nếu chỉ là wick xuyên qua (không phải body close), gọi tên iFVG là overcall theo đúng cảnh báo của doctrine ("trước đó gọi IFVG là hindsight/overcall") — dù về mặt TRÌNH TỰ THỜI GIAN note làm đúng (gọi sau khi có phá), phần "có phá bằng body close hay không" vẫn thiếu evidence.
Your best answer: note có nêu "nhịp giá tạo BPR này đồng thời hình thành MSS + FVG trên khung D1" — MSS D1 đòi hỏi body close phá structure, nên nếu MSS D1 được xác nhận, khả năng cao displacement cùng nhịp đó cũng đóng nến xuyên qua FVG bearish nhỏ hơn (H1) nằm trong cùng dải giá. Điều này làm NARROW objection: khả năng iFVG hợp lệ khá cao dựa trên suy luận gián tiếp từ MSS D1, nhưng vẫn không phải bằng chứng trực tiếp.
Retracted by: giá đóng nến cụ thể của candle H1 đảo qua FVG bearish, từ ảnh gốc.

**O2 · [HINDSIGHT] · fatal · attacks C7**
Claim: "Setup khớp 80% mô hình chuẩn" (tự chấm thấp nhất trong 5 note) nhưng vẫn Grade A — chấm sau khi biết cả 2 lần chốt lời (50% ở 2.48R, 50% ở 4.2R).
Fails: quyết định chốt 50% đầu "khi giá lấp tới CE của Bearish Liquidity Void phía trên" được note tự nhận là một sai sót ("tôi quên mất khi giá quét lên Liquidity Void thường phá rất nhanh mà out sớm mất 50%") — đây là thừa nhận lỗi quy trình rồi vẫn giữ Grade A, cho thấy Grade A neo vào tổng R cuối cùng (RR 2.48 rồi 4.2 tổng) hơn là vào chất lượng quyết định tại từng điểm quyết định.
Evidence: mục 4 "Tại sao lệnh thắng/thua?" liệt kê lý do thắng (fill Liquidity Void, Discount) nhưng không đối trừ với chính lỗi chốt sớm đã tự nhận ngay phía trên.
Consequence: Grade A ở đây gần như chắc chắn phản ánh outcome tổng thể (kết quả cuối tốt dù có lỗi quy trình giữa đường) hơn là đánh giá tách bạch quy trình.
Your best answer: "80% match (thấp hơn note khác) đã phản ánh đúng có lỗi." Không đủ: 80% vẫn tương ứng Grade A — cùng thang điểm A nhưng match% khác nhau (90% ở note khác cũng A) cho thấy ngưỡng chấm Grade A không nhất quán theo %, làm suy yếu độ tin cậy của thang Grade.
Retracted by: một bảng ngưỡng Grade rõ ràng (vd ≥85% = A, 70-85% = B) được áp dụng NHẤT QUÁN trên toàn vault; nếu không tồn tại, objection giữ nguyên ở mức fatal cho tính so sánh được của Grade.

**O3 · [METHOD] · material** — Note đã tự nhận diện đúng vấn đề (POI sâu hơn OTE, external liquidity chưa quét) và còn tự đề xuất rule "Deep POI" — đây là quy trình tốt hiếm thấy. Nhưng chính việc phát hiện này CHỈ xảy ra SAU khi biết lệnh thắng (viết trong Lesson Learned dạng box summary, văn phong phản tư) khiến khó xác định liệu tại thời điểm entry thật, người viết CÓ ý thức về rủi ro 15-pip-external-liquidity này hay không, hay chỉ nhận ra khi viết lại. Retracted by: câu trong mục M5 phân tích (viết trước Lesson Learned) có đề cập rủi ro external liquidity — nếu có, objection rút; hiện tại mục M5 không đề cập, chỉ Lesson Learned mới nói.

**Filter:** 4 objection nháp, cắt 1 (nghi ngờ về SL nằm "giữa cạnh trên và CE BPR" — mô tả mơ hồ nhưng không tìm được cách chứng minh sai lệch cụ thể, rebuttal dễ vượt qua vì đây chỉ là mô tả định tính vị trí SL → xóa). Còn 3: 1 material unsupported (narrowed), 1 fatal hindsight, 1 material method.

**Opposite case.** Từ cùng evidence: BPR có thể chỉ là một vùng "no man's land" giữa 2 FVG đối nghịch không có ý nghĩa cấu trúc thật — giá phản ứng tại đó có thể chỉ là ngẫu nhiên trùng với sweep external liquidity gần đó (Liquidity Void 18/04), không phải vì BPR "có ý nghĩa" theo canon. Với inverse này, entry vẫn đúng vị trí (vì trùng với fill Liquidity Void), nhưng lý do KHÔNG phải BPR mà là đơn giản "giá quay lại lấp gap". Tự phản biện: inverse này thực ra không mâu thuẫn nhiều với thesis gốc — note đã tự nói "lệnh thắng vì fill Bullish Liquidity Void", nghĩa là note CŨNG coi việc lấp Liquidity Void là lý do thắng chính, ngang hàng BPR — nên inverse ở đây gần trùng với một phần thesis gốc, không phải một cách đọc hoàn toàn đối lập. Nhãn: **equally viable** — cả 2 khung (BPR có ý nghĩa cấu trúc / chỉ là điểm lấp gap ngẫu nhiên trùng vị trí) đều được chính note ủng hộ ở các câu khác nhau, evidence không phân biệt được.

Distinguishing observable: nếu BPR thật sự có ý nghĩa cấu trúc (iFVG + FVG hợp lệ với body close xác nhận), giá phải phản ứng NGAY tại BPR trước khi chạm CE (note có ghi "chưa tới CE") — điều này ủng hộ BPR có ý nghĩa hơn là ngẫu nhiên; nhưng cần giá đóng nến cụ thể để xác nhận phản ứng đó không phải noise.

**Verdict: UNPROVEN.** Thin evidence. C6 phụ thuộc C3 (UNSUPPORTED/narrowed) — không FAIL rõ ràng nhưng không đủ để SURVIVES.

**Điều tôi không phá được:** trình tự thời gian gọi tên iFVG (chỉ gọi SAU khi có phá) là đúng chuẩn — đây là điểm mạnh thật, không phải hindsight về mặt TRÌNH TỰ, dù thiếu bằng chứng về BODY CLOSE.

**Điều critique này không xác lập:** không xác lập iFVG có body close xác nhận hay chỉ wick; không xác lập Grade A có phản ánh đúng process bất chấp lỗi chốt lời đã tự nhận.

**Falsification tests:**
1. Kiểm ảnh H1 gốc: giá đóng nến của candle đảo qua FVG bearish 18/04 — xác nhận body close hay chỉ wick → đóng O1.
2. Rà toàn vault để tìm bảng ngưỡng % match ↔ Grade — nếu tồn tại và nhất quán, đóng O2; nếu không, O2 giữ fatal và áp dụng cho toàn hệ thống Grade, không riêng note này.
3. Đối chiếu timestamp giữa phần M5 phân tích và box Lesson Learned — nếu rủi ro external liquidity chỉ xuất hiện ở Lesson Learned (viết sau), xác nhận O3.

## 9. Doctrine check (ICT 2022 canon)

**Thesis:** Long EURUSD 27/04/2005 — bearish FVG H1 (18/04) bị đảo (iFVG) + FVG bullish mới chồng lấp → BPR, giá quay lại BPR (sâu hơn OTE, còn external SSL chưa quét dưới) → M5 xác nhận (MSS+displacement+FVG) → entry, RR 2.48 (chốt 2 lần), Grade A, tự chấm 80% match.

**Cần sửa** (load-bearing trước):
- C3 (iFVG hình thành đúng thời điểm, load-bearing cho BPR) — **UNSUPPORTED** · trình tự thời gian đúng canon (chỉ gọi iFVG SAU khi có phá — SKILL.md § Inversion FVG) nhưng thiếu giá đóng nến cụ thể để xác nhận đó là body close (không chỉ wick) → bổ sung giá đóng nến từ ảnh gốc.
- C6 (MSS M5, kế thừa mẫu hình chung) — **UNSUPPORTED** · kế thừa từ hạn chế ghi chép chung của batch, không tính lỗi riêng.

**PASS:** C1 (bias D1 Bullish, mô tả đủ); C2 (bearish FVG H1 18/04 — mô tả rõ thời điểm hình thành, đủ để PASS ở mức mô tả); C3-trình tự (thứ tự gọi tên iFVG SAU khi có phá — ĐÚNG doctrine, đây là điểm hiếm PASS rõ rệt về mặt trình tự trong cả batch, tách biệt khỏi phần UNSUPPORTED về body-close nêu trên); C4 (retracement BPR 0.84-0.94 tính lại khớp đúng với claim note "sâu hơn OTE" — arithmetic chuẩn); C5 (external SSL 15 pip dưới BPR — tính lại khớp đúng 1.28927-1.28777=0.00150=15 pip, arithmetic chuẩn, và đây là self-critique hiếm có giá trị).

**Verdict: INSUFFICIENT EVIDENCE** — load-bearing C3 (phần body-close của iFVG) UNSUPPORTED dù trình tự thời gian đúng; không đủ để PARTIALLY ALIGNED vì thiếu evidence trực tiếp cho chính cấu trúc định nghĩa BPR.

**Notes — Doctrine drift giữa các case trong batch A:** Note này (27/04) là note DUY NHẤT trong 5 note tuân thủ đúng trình tự thời gian cho iFVG (gọi tên SAU khi có phá); các note khác trong batch (1, 2, 3, 4) không dùng nhãn iFVG nên không có cơ sở so sánh trực tiếp, nhưng đáng ghi nhận: đây là ví dụ tốt nên tham chiếu khi review các note sau có dùng iFVG, để kiểm tra tính nhất quán về trình tự gọi tên.

## 10. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật**
- Ví dụ số thật: BPR (1.28927–1.29084) ở retracement 0.84-0.94 dealing range, còn 15 pip external SSL (1.28777) chưa quét bên dưới — note tự tính đúng và tự cảnh báo rủi ro sweep-through. Tổng quát hóa: mọi POI nằm sâu hơn 0.79 (ngoài OTE chuẩn) nên có bước kiểm tra bắt buộc "còn external liquidity nào bên dưới/trên chưa quét" trước khi tin tưởng POI đó.
- Ví dụ số thật: iFVG chỉ được gọi tên SAU khi note xác nhận "FVG bearish bị phá lên trên" — đúng trình tự canon. Tổng quát hóa: quy tắc chung cho mọi nhãn iFVG trong vault là PHẢI có câu mô tả rõ trình tự "FVG gốc tồn tại trước → bị đóng nến xuyên qua → SAU ĐÓ mới gọi là iFVG", không gọi tên trước khi có phá.

**(b) Bài học quy trình/checklist**
- Note tự nhận lỗi chốt 50% sớm ("quên mất Liquidity Void thường phá rất nhanh") — đây là lỗi quy trình quản lý lệnh giữa đường, cần một checklist riêng cho quản lý lệnh (không chỉ checklist cho entry) để tránh lặp lỗi.
- Cần công thức rõ để phân biệt đo OTE trên displacement leg với đo Premium/Discount trên dealing range — note đã tự phân biệt đúng trong box "Bài học kỹ thuật", nên rule này cần lan sang các note khác trong vault còn nhầm 2 phép đo.

**(c) Bài học tâm lý-hành vi**
- Grade A vẫn được giữ dù note tự nhận có lỗi chốt lời — cho thấy khuynh hướng: kết quả tổng cuối tốt (RR cao) đủ để "tẩy" một lỗi quy trình đã biết, thay vì lỗi đó kéo Grade xuống. Đây là outcome bias khá rõ, chính note cũng nhận ra một phần khi tự chấm match% thấp hơn (80% so với 90% các note khác) nhưng Grade tổng vẫn giữ nguyên A.

**(d) Rule đề xuất cho Playbook**
- [ ] Rule "Deep POI" (đã note tự đề xuất): khi POI sâu hơn 0.79 dealing range, bắt buộc kiểm external liquidity chưa quét bên dưới/trên trước khi tin cậy toàn phần vào POI.
- [ ] Ghi rõ nhãn OTE neo vào displacement leg hay Premium/Discount neo vào dealing range trong MỌI note — tránh nhầm khung tham chiếu (rule note đã tự đề xuất, hợp lý để chính thức hóa).
- [ ] Thêm checklist "quản lý lệnh giữa đường" độc lập với checklist entry: bao gồm rule cụ thể khi giá tới Liquidity Void/CE trung gian, để tránh chốt lời theo phản ứng tức thời.

**(e) Điều KHÔNG nên học từ lệnh này**
- Không nên coi việc Grade A được giữ dù có lỗi chốt lời là bằng chứng lỗi đó "không quan trọng" — ngược lại, nên tách rõ Grade cho QUY TRÌNH ENTRY khỏi Grade cho QUẢN LÝ LỆNH để không pha trộn 2 loại đánh giá.
- Không nên coi con số RR cuối (2.48R rồi 4.2R nếu giữ hết) là benchmark kỳ vọng cho BPR/iFVG setup — n=1, và một phần R đến từ việc giá tiếp tục chạy sau khi đã có quyết định chốt sớm (không kế hoạch).
- Không nên tổng quát hóa "POI sâu hơn OTE luôn ổn nếu có confirmation LTF" chỉ từ 1 mẫu thắng — đây đúng là điều note đã tự cảnh báo (đề xuất tag riêng `POI-deeper-than-OTE` để kiểm định qua nhiều mẫu), cần tuân theo chính đề xuất đó trước khi coi là quy luật.

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[13-FVG-Fair-Value-Gap]] · [[26-OTE-Optimal-Trade-Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: _(chưa gán note lỗi)_
