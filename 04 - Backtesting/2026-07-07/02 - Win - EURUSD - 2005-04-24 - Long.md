---
type: backtest
backtest_date: 2026-07-07
trade_date: 2005-04-24
symbol: EURUSD
position: Long
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[07 - Unicorn Model|Unicorn Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29582
stop_loss: 1.29451
take_profit: 1.29884
r_planned: 2.23
r_multiple: 2.23
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-24 — EURSUD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                 |
| -------------------- | ------------------------------------- |
| Symbol               | EURUSD                                |
| Trade Date (dữ liệu) | 2005-04-24                            |
| Position             | Long                                  |
| Result               | Win                                   |
| Session              | New York                              |
| Setup                | ICT 2022 Model                        |
| Entry Model          | [[07 - Unicorn Model|Unicorn Model]] |
| Entry Timeframe      | M5                                    |
| HTF Bias             | Bullish                               |
| Bias Correct?        | Yes                                   |
| Entry                | 1.29582                               |
| Stop Loss            | 1.29451                               |
| Take Profit          | 1.29884                               |
| R Planned            | 2.23                                  |
| R Multiple (kết quả) | 2.23                                  |
| Grade                | A                                     |

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
![[Pasted image 20260707061746.png]]
### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL
- **Dealing Range**: 
	- High: 1.31266
	- Low 1.28777
	- Giá đang di chuyển về vùng Discount (đúng theo bias Bullish)
- **POI chính**: 
	- Breaker Block : 1.29480 - 1.29357
	- FVG: 1.29595 - 1.29426
	- Vùng Unircorn (quan trọng - POI chính): vùng overlap giữa Breaker Block và FVG -> 1.29498 - 1.29433
- **Liquidity cần chờ sweep**:
  - Vùng FVG khung H1
  - Vùng Breaker Block
  - Đặc biệt quan sát giá phản ứng tại vùng Unicorn
### Phân Tích:
- 2 -3 ngày trước H1 vẫn đang trong xu hướng giảm (Bearish Bias) và hình thành OB trên khung H1 (khi đó tôi đang chờ giá quay lại và xem setup lệnh short hình thành)
- Ngày hôm sau giá bật lên mạnh (displacement) phá qua các swing high khung H1 (và swing high khung D1) -> dẫn đến khung D1 hình thành MSS + FVG
- Bias sau đó đổi sang Bullish
- Vùng Order Block ban đầu sau nhịp displacement phá qua trở thành Bullish Breaker Block
- Đồng thời trong nhịp đẩy giá mạnh (displacement) có hình thành FVG khung H1, trùng lắp 1 phần với Breaker Block
- Phần Overlap đó hình thành 1 vùng quan trọng là Unicorn khung H1
- Sau đó tôi chờ giá quay về vùng Unicorn này
- Unicorn này nằm đúng trong OTE - đặc biệt là nằm sát cạnh CE của OTE (sweet spot 0.705)
- Tuy nhiên phải chờ khá lâu để giá quay về vùng này (setup ngày 18, tới ngày 26 giá mới quay về)
- Giá quay về CE của vùng Unicorn và xuất hiện dấu hiệu rejection
- Xuống khung M5 quan sát
![[Pasted image 20260707061856.png]]
## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá chạm vùng Unicorn với các râu nến ( chạm vào bật ra và đóng bên ngoài 4 nến liền tiếp và có 1 nếm quét qua vùng CE)
- Sau đó giá bật lên với các nến lớn (displacement)
- Giá tạo MSS + FVG
- Entry tại FVG
- Stoploss đặt bên dưới điểm sweep (CE unicorn)
- **Entry trigger**:
  - Liquidity Sweep: Quét EQL, 50% Unicorn
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là Unicorn)
- **Invalidation reason**:
  - Giá đóng qua đáy sweep/qua unicorn
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260707062004.png]]
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

- **Result**: Đóng lệnh khi đạt 2.3R thay vì đợi hết TP
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone (New york)
  - Giá quét EQL (khung M5), quét tới CE unicorn
  - Giá đang trong vùng Discount và quan trọng là đang trong khu vực sweet spot OTE
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về discount -> Quét EQL + CE Unicorn -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- **Swing high/low M5 dùng làm TP thực chất là một vũng [[20-Liquidity-Sweep|BSL/SSL]]** — giá bị *draw* tới để **quét** rồi mới đảo, chứ không "hướng tới cái đỉnh". Vì vậy nên đặt TP **nhỉnh dưới đỉnh vài pip** (front-run liquidity) thay vì đặt ngay tại/vượt đỉnh → tăng tỉ lệ khớp TP và giải quyết đúng nỗi "giá gần chạm TP rồi quay đầu".
- **TP tại đỉnh M5 gần nhất chỉ tối ưu win rate**, nó cắt cụt các lệnh còn draw HTF cao hơn (đánh đổi *hit rate ↔ average R*). Lệnh này rơi đúng vào kịch bản đó: TP nằm ở **BSL trung gian** (đường đỏ dưới), còn một swing high cao hơn (đường đỏ trên) **chưa bị quét** → đáng lẽ nên giữ một phần làm runner.
- **Quyết định "cắt hết hay để runner" phải dựa trên bản đồ Draw on Liquidity đa khung** (đỉnh M5 là *điểm đến cuối* hay *trạm trung gian*?), lấy từ phân tích H1/D1 (draw = PDH/PWH), **không dựa vào cảm giác**.

### Pattern lặp lại (điều cần để ý lần sau)

- Xu hướng **chốt toàn bộ tại đỉnh M5 gần nhất** → khóa mọi lệnh thắng quanh ~2R, ép average R xuống dù win rate cao. Về dài hạn hệ thống ICT 2022 sống nhờ các cú runner; nén hết về 2R sẽ bào mòn expectancy.
- Note ghi *"Đóng khi đạt 2.3R thay vì đợi hết TP"* → cần phân biệt rõ: **chốt theo kế hoạch (2R rule)** hay **chốt vì sốt ruột**. Nếu là cái sau thì dù kết quả +2.3R, đây vẫn là **lỗi process** cần đánh dấu vì không lặp lại được một cách kỷ luật.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Đặt TP **nhỉnh dưới** swing high/low mục tiêu vài pip (front-run BSL/SSL), không đặt tại/vượt đỉnh.
- [ ] Áp dụng **scale-out**: chốt 50–70% tại BSL/SSL trung gian gần nhất → dời SL về **BE** → để phần còn lại chạy tới **draw HTF kế tiếp** (đỉnh xa hơn / PDH/PWH).
- [ ] Ghi thêm field **MFE (Maximum Favorable Excursion)** cho mỗi lệnh backtest (sau khi chạm đỉnh M5 gần nhất, giá còn đi thêm bao nhiêu R tới draw HTF kế tiếp trước khi retrace về BE) để **định lượng full-exit vs partial** sau 30–50 mẫu, thay vì quyết định bằng linh cảm.

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

**Bản đồ liquidity IRL↔ERL.** Draw on liquidity D1: PDH/PWH (buy-side) và PDL/PWL (sell-side). Entry Long 1.29582 tại vùng Unicorn (breaker ∩ FVG). Dealing Range H1: High 1.31266/Low 1.28777, mid 1.30022. Entry ở retracement ≈0.677 từ high — nằm trong Discount, trong khoảng OTE 0.618–0.79, khớp claim "nằm sát CE của OTE (sweet spot 0.705)" (tính lại CE dealing range 0.705 ≈ 1.31266 - 0.705×2.489 = 1.29511, gần khớp entry 1.29582, chênh 7 pip — có thể note đang neo OTE vào leg displacement riêng, không phải toàn dealing range, nên số không trùng khớp tuyệt đối. Đây là điểm cần làm rõ, không mặc định khớp).

**Chất lượng displacement/MSS.** D1 có MSS + displacement phá swing low lớn, tạo FVG D1 — mô tả rõ ràng nhất trong 5 note về nguồn gốc breaker: "Vùng Order Block ban đầu sau nhịp displacement phá qua trở thành Bullish Breaker Block" — đây đúng chuỗi sự kiện canon của breaker (OB thất bại + đảo cực sau khi structure bị phá), không phải chỉ gọi tên tùy ý.

**Yếu tố thời gian.** Setup hình thành từ 18/04, giá quay lại vùng Unicorn tới 26/04 — note ghi rõ "phải chờ khá lâu" — đây là độ trễ hiếm khi được ghi nhận minh bạch trong các note khác, đáng khen về tính trung thực dữ liệu.

**Vị trí entry trong dealing range.** Retracement ≈0.677, khớp Discount + OTE — nhất quán giữa 3 lớp (Dealing Range, OTE, POI Unicorn).

**Doctrine kiểm tra Unicorn — điểm quan trọng nhất của note này.** Unicorn Model theo canon yêu cầu overlap giữa breaker và FVG. Note ghi: Breaker 1.29357–1.29480, FVG 1.29426–1.29595, Unicorn (overlap) ghi là 1.29433–1.29498. Tính lại bằng arithmetic: overlap thực = max(1.29357,1.29426) đến min(1.29480,1.29595) = 1.29426–1.29480. So với số note ghi (1.29433–1.29498): cạnh dưới lệch 0.00007 (~0.7 pip, có thể do rounding khi đọc chart), nhưng cạnh trên lệch 0.00018 (~1.8 pip, note ghi 1.29498 > overlap thực 1.29480) — con số note ghi VƯỢT RA NGOÀI overlap thực tế được tính từ 2 range mà chính note cung cấp. Đây là một arithmetic discrepancy nhỏ nhưng đáng nêu vì Unicorn hoàn toàn định nghĩa bằng phép giao (intersection) của breaker và FVG.

![[EURUSD-20050424-unicorn-overlap.svg|760]]

## 8. Phản biện chuyên sâu (Devil's Advocate)

**Mode: REVIEW.** Evidence base: text note + 3 screenshot không đọc được. **evidence_sufficiency: thin.**

**Claim graph:**
- C1: D1 MSS + displacement phá swing low lớn → bias Bullish, FVG D1.
- C2: OB H1 trước đó (khi bias còn Bearish) bị phá bởi displacement D1 → trở thành Bullish Breaker (1.29357–1.29480).
- C3: FVG H1 hình thành trong displacement leg (1.29426–1.29595), overlap với Breaker → vùng Unicorn.
- C4 (**arithmetic**): Unicorn range note ghi 1.29433–1.29498 — lệch nhẹ so với overlap tính từ chính 2 range đã cho (1.29426–1.29480).
- C5: Giá chờ 8 ngày (18→26/04) quay lại Unicorn, phản ứng tại CE (~1.29466), xuống M5 thấy MSS + displacement + FVG.
- C6 (**load-bearing**): Entry tại FVG M5 (1.29582), trong vùng Unicorn + OTE, SL dưới CE Unicorn.
- C7: Setup Unicorn Model chuẩn, RR 2.23-2.3, Grade A.

**Load-bearing: C6**, phụ thuộc trực tiếp vào C2+C3 (breaker và FVG có thật + có overlap đúng) — nếu C2 hoặc C3 sai (ví dụ breaker không thực sự phá structure trước khi đảo cực, hoặc FVG không thực chất là 3-candle imbalance), toàn bộ nhãn "Unicorn" sụp, chỉ còn là một OB + FVG bình thường không có tên đặc biệt.

**Những gì còn đứng:** Chuỗi hình thành breaker (OB cũ bị phá qua bởi displacement mới, đảo cực) mô tả đúng canon breaker — đây là mô tả breaker rõ ràng và đúng thứ tự sự kiện nhất trong batch A.

**O1 · [ARITHMETIC] · material · attacks C4**
Claim: "Vùng Unicorn: 1.29498 - 1.29433" (overlap breaker ∩ FVG).
Evidence: Breaker 1.29357–1.29480, FVG 1.29426–1.29595. Overlap tính đúng = max(1.29357,1.29426)–min(1.29480,1.29595) = 1.29426–1.29480. Cạnh trên note ghi (1.29498) vượt quá cạnh trên overlap tính được (1.29480) 1.8 pip.
Consequence: nếu dùng đúng overlap tính lại (1.29426–1.29480) thay vì số note ghi, CE Unicorn đúng = 1.29453 (không phải 1.29466 như note). SL 1.29451 khi đó nằm RẤT SÁT dưới CE đúng (chỉ 0.2 pip), thay vì cách CE ghi 1.29466 khoảng 1.5 pip — buffer SL mỏng hơn note thể hiện.
Retracted by: xác nhận số breaker/FVG gốc trong note bị đọc sai từ chart (ví dụ FVG top thực ra là 1.29613 chứ không phải 1.29595), khi đó overlap tính lại sẽ khớp số note ghi.

**O2 · [HINDSIGHT] · fatal · attacks C7**
Claim: Grade A, "khớp 90% mô hình chuẩn" — chấm sau biết kết quả (đóng lệnh sớm ở 2.3R thay vì chờ hết TP, ghi trong mục 4).
Fails: không có invalidation condition nào ghi trước khi biết giá phản ứng ra sao tại Unicorn trong 8 ngày chờ — "chờ giá quay về vùng này" không kèm điều kiện hết hạn (vd "nếu quá N ngày không quay về, huỷ setup"), nên không thể phân biệt được kiên nhẫn có kỷ luật với việc giữ một ý tưởng bias vô thời hạn.
Evidence: mục 4 viết "Đóng lệnh khi đạt 2.3R thay vì đợi hết TP" — chính note tự nhận đây có thể là quyết định theo cảm giác ("nếu vào lại tôi sẽ...Partial take profit" — nghĩa là lần này chưa có kế hoạch partial rõ từ đầu).
Consequence: Grade A và "90% khớp mô hình" được chấm SAU khi biết cả outcome (Hit gần TP) và quyết định thoát lệnh sớm — không tách được phần nào của đánh giá phản ánh process tại thời điểm entry, phần nào phản ánh sự hài lòng với kết quả cuối.
Your best answer: "Checklist mục 2/3 (Entry Sequence, Setup Quality) tick đầy đủ trước khi biết kết quả thoát lệnh." Không đủ — không có bằng chứng thứ tự ghi chép; checklist có thể được điền cùng lúc với phần replay.
Retracted by: bằng chứng thời điểm ghi (note LIVE tại 26/04 trước khi biết outcome, hoặc log tách bạch rõ before/after).

**O3 · [DOCTRINE] · material · attacks C3**
Claim: FVG H1 (1.29426–1.29595) là FVG hợp lệ hình thành trong displacement leg.
Fails: SKILL.md § FVG yêu cầu "phải là sản phẩm của displacement leg + imbalance thật (3-candle)" — note không cho số liệu 3 nến cấu thành FVG (nến 1/2/3 với giá cụ thể), chỉ nói "đồng thời trong nhịp đẩy giá mạnh có hình thành FVG khung H1".
Consequence: nếu FVG này thực chất chỉ là gap nhỏ không đạt chuẩn 3-nến rõ ràng, overlap Unicorn (breaker∩FVG) không có FVG hợp lệ để giao, và nhãn "Unicorn" không đứng vững — status đúng là UNSUPPORTED, không phải FAIL, vì không có bằng chứng ngược lại.
Your best answer: không có — thiếu dữ liệu thuần túy.
Retracted by: 3 giá nến cấu thành FVG H1 từ ảnh gốc.

**Filter:** 4 objection nháp, cắt 1 (nghi ngờ về độ trễ 8 ngày làm giảm giá trị setup — không đổi kết luận về validity của Unicorn, chỉ là quan sát về thời gian → chuyển thành ghi chú trong Lesson Learned thay vì objection). Còn 3: 1 material arithmetic, 1 fatal hindsight, 1 material doctrine/unsupported.

**Opposite case.** Từ cùng evidence: vùng "Unicorn" có thể chỉ là một breaker đơn thuần (không cần FVG overlap để có giá trị) — giá phản ứng tại breaker là đủ để giải thích entry, và "FVG overlap" chỉ là một chi tiết trang trí thêm vào sau khi thấy giá phản ứng đúng, không phải yếu tố quyết định. Tự phản biện: nếu đúng vậy, note phải giải thích được TẠI SAO chọn breaker cụ thể này (1.29357–1.29480) mà không phải một breaker khác trên H1/D1 — và câu trả lời note đưa ra (overlap với FVG tạo Unicorn, nằm sát OTE 0.705) chính là lý do chọn — nên inverse yếu vì nó bỏ qua chính tiêu chí lựa chọn confluence mà note dùng. Nhãn: **weaker but non-trivial** — inverse chỉ mạnh nếu overlap FVG thực chất không tồn tại (xem O3).

Distinguishing observable: 3 giá nến cấu thành FVG H1 — nếu xác nhận có imbalance 3-nến thật giữa 1.29426–1.29595, Unicorn thật; nếu không, chỉ còn breaker đơn, và inverse mạnh hơn.

**Verdict: UNPROVEN.** Thin evidence. Load-bearing C6 phụ thuộc C3 (UNSUPPORTED) — không FAIL rõ ràng, không đủ để SURVIVES.

**Điều tôi không phá được:** chuỗi hình thành breaker (OB cũ bị phá bởi displacement D1, đảo cực) là mô tả breaker đúng canon, rõ ràng nhất trong batch A — không tìm được mâu thuẫn nội tại nào ở tầng D1/H1 cho phần này.

**Điều critique này không xác lập:** không xác lập FVG H1 có đạt chuẩn 3-nến; không xác lập liệu quyết định thoát lệnh sớm ở 2.3R và Grade A có độc lập với biết trước outcome.

**Falsification tests:**
1. Kiểm ảnh H1 gốc: 3 nến cấu thành FVG H1 (giá cụ thể) — xác nhận hoặc phủ nhận C3/O3.
2. Đối chiếu số Unicorn overlap ghi trong note với ảnh gốc để xác nhận hoặc sửa O1.
3. Rà toàn vault các setup có nhãn "Unicorn Model" (nếu có nhiều hơn 1) để kiểm tra công thức overlap có được tính nhất quán (đúng arithmetic breaker∩FVG) ở tất cả, hay chỉ lệch ở note này — nếu lệch có hệ thống, đây là doctrine drift cấp batch.

## 9. Doctrine check (ICT 2022 canon)

**Thesis:** Long EURUSD 24/04/2005 — breaker H1 (từ OB cũ bị phá đảo cực) overlap FVG H1 → Unicorn Model, chờ 8 ngày giá quay về CE Unicorn, phản ứng M5 (MSS+displacement+FVG) → entry, RR 2.23-2.3, Grade A.

**Cần sửa** (load-bearing trước):
- C3 (FVG H1 hợp lệ, load-bearing cho Unicorn) — **UNSUPPORTED** · không có 3 giá nến cấu thành FVG (SKILL.md § FVG: "phải là sản phẩm của displacement + imbalance thật 3-candle") → bổ sung số liệu nến từ ảnh gốc.
- C4 (Unicorn overlap range) — **FAIL** · arithmetic: overlap tính từ 2 range breaker (1.29357–1.29480) và FVG (1.29426–1.29595) đã cho ra 1.29426–1.29480, không khớp số note ghi 1.29433–1.29498 (cạnh trên lệch 1.8 pip, vượt ra ngoài giao thực) → sửa lại theo đúng công thức giao (intersection) của 2 range đã nêu, hoặc sửa lại số breaker/FVG nếu bị đọc nhầm từ chart.
- C6 (MSS M5, kế thừa mẫu hình chung của batch) — **UNSUPPORTED** · không có swing point/giá đóng nến cụ thể — kế thừa từ hạn chế ghi chép chung, không tính là lỗi riêng.

**PASS:** C1 (MSS+displacement D1 tạo bias Bullish — mô tả đủ, đúng chuỗi); C2 (Breaker: chuỗi sự kiện OB cũ bị phá + đảo cực đúng canon breaker — SKILL.md § Breaker "OB thất bại sau khi lấy liquidity + phá structure, đảo cực. Cần chuỗi sự kiện" — note mô tả đủ chuỗi này, PASS); C5 (retracement dealing range 0.677 nằm trong Discount + OTE — arithmetic khớp).

**Verdict: INSUFFICIENT EVIDENCE** — load-bearing C3 UNSUPPORTED khiến claim Unicorn (đòi hỏi FVG hợp lệ) chưa kiểm chứng được đầy đủ; cộng thêm C4 FAIL (lỗi arithmetic độc lập ở vùng overlap) → không thể là PARTIALLY ALIGNED vì lỗi C4 tác động trực tiếp đến chính định nghĩa POI.

**Notes:** Đây là note đầu tiên trong batch A thể hiện breaker được mô tả ĐÚNG chuỗi sự kiện canon (không chỉ gọi tên) — nên ghi nhận như một điểm tích cực hiếm trong nhóm note sớm này. Tuy nhiên chính vì Unicorn là một cấu trúc phức tạp (2 lớp: breaker + FVG), sai số arithmetic ở phép giao trở nên đáng kể hơn so với các label đơn giản (OB, FVG riêng lẻ) ở 2 note trước.

## 10. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật**
- Ví dụ số thật: Unicorn overlap tính từ breaker (1.29357–1.29480) và FVG (1.29426–1.29595) đúng ra là 1.29426–1.29480, nhưng note ghi 1.29433–1.29498 — cạnh trên lệch 1.8 pip ra ngoài overlap thực. Tổng quát hóa: mọi claim Unicorn phải kèm phép tính giao (intersection) rõ ràng bằng công thức max(low1,low2)–min(high1,high2), không ghi số "áng chừng" từ mắt nhìn chart.
- Ví dụ số thật: giá chờ 8 ngày (18→26/04) mới quay về Unicorn — đây là một khoảng chờ dài, đáng ghi nhận rằng không phải mọi Unicorn đều được test nhanh; kiên nhẫn giữ ý tưởng qua nhiều ngày là một phần chi phí thời gian thực của setup này.

**(b) Bài học quy trình/checklist**
- Không có invalidation-by-time rule khi chờ giá quay về POI nhiều ngày — cần một ngưỡng rõ ràng (ví dụ "nếu D1 bias đổi hướng hoặc có tin tức lớn trong thời gian chờ, huỷ ý tưởng") để tránh giữ một bias cũ quá lâu chỉ vì "đã phân tích rồi".
- Quyết định thoát lệnh sớm ở 2.3R "thay vì đợi hết TP" cần một rule rõ ràng TRƯỚC khi vào lệnh (case này không có), để phân biệt kỷ luật với phản ứng cảm tính giữa lệnh.

**(c) Bài học tâm lý-hành vi**
- Đây là note có khoảng chờ dài nhất (8 ngày) trong batch — nguy cơ tâm lý "đã đầu tư thời gian phân tích nên phải đợi cho ra kết quả" (sunk cost trong việc chờ setup) cần được cảnh giác dù không có bằng chứng cụ thể nó đã xảy ra ở đây.

**(d) Rule đề xuất cho Playbook**
- [ ] Mọi claim Unicorn Model bắt buộc kèm 2 range (breaker, FVG) + công thức giao tính bằng số, không ước lượng bằng mắt.
- [ ] Khi chờ giá quay về POI H1/D1 quá 3-5 ngày, ghi thêm điều kiện huỷ ý tưởng theo thời gian hoặc theo thay đổi cấu trúc D1.
- [ ] Rule thoát lệnh sớm (trước TP) phải được định nghĩa trước khi vào (ví dụ: "chốt 50% khi chạm PD array trung gian gần nhất"), không quyết định giữa chừng.

**(e) Điều KHÔNG nên học từ lệnh này**
- Không nên coi số liệu Unicorn overlap trong note này là chuẩn tính toán — số bị lệch nhỏ so với công thức giao đúng, cần tự tính lại trước khi dùng làm mẫu.
- Không nên coi việc chờ 8 ngày rồi entry thắng là bằng chứng "kiên nhẫn luôn được đền đáp" — n=1, và không có rule invalidation theo thời gian để biết khi nào kiên nhẫn trở thành cố chấp.
- Không nên dùng quyết định thoát sớm ở 2.3R của lệnh này làm chuẩn cho các lệnh sau — quyết định này không có kế hoạch trước, chỉ nên học từ nó ở việc CẦN có kế hoạch, không phải học theo con số 2.3R cụ thể.

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[13-FVG-Fair-Value-Gap]] · [[26-OTE-Optimal-Trade-Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: _(chưa gán note lỗi)_
