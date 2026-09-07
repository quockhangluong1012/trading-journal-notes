---
date: 2026-06-17T08:35:00
symbol: NDX
position: Long
result: Loss
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 30,079.3
take_profit: 30,428.3
stop_loss: 29,931.1
pnl: -44.46
r_multiple:
risk_percent: 0.5%
mistakes:
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]"
tags:
planned_rr: 2.35
da_verdict: BROKEN
da_evidence_sufficiency: partial
da_objections: {fatal: 1, material: 1, minor: 1}
da_opposite_case: "not viable"
---

# Trade 17-06-2026 - SYMBOL Position Result

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Loss |
| Session |  New York |
| Setup | ICT 2022 Model |
| Entry Model | MSS + FVG |
| Entry Timeframe | M5 |
| HTF Bias | Bullish |
| Bias Correct? | No |
| Entry | 30,079.3 |
| Stop Loss | 29,931.1 |
| Take Profit | 30,428.3 |
| PnL | -44.46 |
| R Multiple | 1.75 |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Pullback
- **Lý do xác định bias**:
  - Nhìn trend tổng thể xác định bias. Tuy nhiên model là intraday thì nên tập trung vào những cây nến gần đây
  - Giá break xuống dưới Previous Day Low -> daily bias nên là Bearish thay vì Bullish
  - Xác định sai bias dẫn đến vào lệnh counter trend
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity: 30,679 - LTH
  - Sell-side liquidity: 29,981 - ITL
- **Ghi chú quan trọng**:
  - Giá hình thành 1 GAP lớn vào ngày thứ 2 (Opening Week Gap), giá có khả năng quay về lắp GAP


![[NDX-20260617-D1.png]]

---

### H1

- **Cấu trúc H1**: LH/LL
- **Dealing Range chính**: 
  - High: 30,647.8
  - Low: 29,948
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block:
  - FVG:  
  - Breaker: Không có
  - Other:
- **Liquidity cần chờ sweep**:
  - SSL
- **Kịch bản mong muốn**:
  - Quét SSl xong retrace về FVG

![[NDX-20260617-H1.png]]

---

### M15 / M5

- **Giá đã vào POI chưa?** No
- **Có Liquidity Sweep chưa?**  No
- **Sweep loại nào?**
  - Chưa Sweep
- **Có Displacement chưa?** No
- **Có MSS chưa?** No
- **Có FVG hợp lệ chưa?** No
- **Entry có nằm trong POI không?** No

![[NDX-20260617-M5.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [ ] Đã xác định Daily Bias rõ ràng
- [ ] Bias không mâu thuẫn với H1/M15
- [ ] Giá đã vào vùng POI hợp lệ
- [ ] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng
- [x] Có Market Structure Shift hợp lệ
- [ ] Entry nằm trong FVG / OB / PD Array hợp lệ
- [ ] Stop loss đặt ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt yêu cầu
- [ ] Đã kiểm tra tin tức quan trọng
- [ ] Không vào lệnh vì FOMO
- [ ] Không revenge trade
- [ ] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đính Dealing Range

### Điều tôi làm sai

- Xác định sai Daily Bias
- Tập trung vào tìm MSS trong khi giá đang không năm trong vùng POI
- Vào lệnh đuổi giá (FOMO)
### Tâm lý khi vào lệnh

- FOMO / 
- Revenge trade
- Không chắc chắn
- Ghi chú:
  - 

### Có tuân thủ plan không?

- **No**
- Nếu không, tôi đã phá rule nào?
  - Xác định sai Bias
  - Không chờ MSS
  - Không chờ Liquidity Sweep
  - FOMO

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit SL
- **Mistake chính**:
  - [[09-Mistake-Wrong-daily-bias]]
  - [[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]
  - [[01-Mistake-Emotional-revenge-trade]]
- **Nguyên nhân gốc rễ**:
  - Revenge trade, cố gắng vào lệnh để gỡ lại 2 lệnh thua trước đó
- **Tại sao lệnh này thua/thắng?**
  - Xác định sai Bias
  - Không chờ MSS
  - Không chờ Liquidity Sweep
  - FOMO
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - Giá giao dịch dưới Previous Day Low -> Bearish Bias thay vì bullish khi nhìn quá rộng
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Xác định bias cho đúng
  - Xác định Dealing Range, đánh dấu các vùng POI dựa trên Bias
  - Nếu giá cho tín hiệu break bias thì nên chuyển đổi bias theo context hiện tại, không cố bám vào bias ban đầu
  - Chờ Liquidity Sweep rõ ràng
  - Chờ MSS hợp lệ, giá phải break ITH/TML

---

## 5. Lesson Learned

Bài học gốc của user (giữ nguyên, mở rộng dưới đây):

### Bài học kỹ thuật
- Học lại cách xác định daily bias
- Cần thay đổi bias linh hoạt theo điều kiện thị trường thời điểm đó. Không cố giữ bias khi đã invalid
- **Mở rộng**: checklist tick "Có MSS hợp lệ" = `[x]` trực tiếp mâu thuẫn với dòng ngay phía trên trong section M15/M5: "Có MSS chưa? **No**" — tick pre-trade và narrative post-trade trong cùng file không khớp nhau (liên kết O1, fatal).

### Bài học tâm lý
- Không FOMO sợ bỏ lỡ kèo. 
	- Nếu setup đẹp mà lỡ nhịp -> Bỏ
	- Nếu chưa đủ các điều kiện cần thiết -> Bỏ
- Không cố trade để trả thù/gỡ lại các lệnh thua. Mỗi lệnh là độc lập
- **Mở rộng**: "Nguyên nhân gốc rễ" tự ghi rõ "Revenge trade, cố gắng vào lệnh để gỡ lại 2 lệnh thua trước đó" — nhưng lệnh này có timestamp **08:35 sáng 06-17**, TRƯỚC cả Loss-01/Loss-02 (17:36) và Loss-03 (20:09) theo frontmatter `date` của các file đó. Nếu "2 lệnh thua trước đó" không phải Loss-01/02/03 (vì chúng đều có timestamp SAU 08:35), thì 2 lệnh thua đó phải xảy ra trước 08:35 sáng 06-17 và KHÔNG có trong 6 file được giao — liên kết trực tiếp tới Bối cảnh cụm bên dưới, đây là một finding về trình tự, không phải suy diễn thêm.

### Bài học quy trình & risk
- Checklist "Pre-trade" tick MSS = true trong khi narrative ngay bên trên ghi "No" là bằng chứng checklist được tick SAU khi đã biết kết quả/diễn biến, không phải tick TRƯỚC entry để làm gate — đúng theo CS-O9 (minor, cùng pattern ở file khác trong sample) nhưng ở đây severity cao hơn vì đây nằm trong cụm revenge đang được phân tích, không phải trường hợp đơn lẻ.
- risk_percent = 0.5% — đúng chuẩn rule đã công bố (không phải 5% như 8/25 lệnh khác trong toàn sample) — điểm này PASS, không phải finding.

### Rule cần thêm/cập nhật
- Rule kiểm tra được: "Checklist Pre-trade phải được tick TRƯỚC khi entry, lưu timestamp tick riêng biệt với timestamp entry — nếu hai giá trị tick mâu thuẫn với narrative post-trade trong cùng file, coi checklist đó là invalid và không tính vào thống kê 'đã qua checklist'."
- Rule kiểm tra được: "Ghi rõ ID/timestamp của các lệnh thua được tham chiếu trong cụm từ 'gỡ lại N lệnh thua trước đó' — nếu N lệnh đó không có trong journal, đánh dấu thiếu dữ liệu, không để trống."

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, không chart, nhưng đây là file giàu cấu trúc nhất trong cụm (có checklist, Execution Review, Final Grade — khác 4 file kia trong cụm chỉ có 1-2 mục ngắn). Sufficiency: **partial** — nhiều claim tự nhận rõ ràng, nhưng vẫn thiếu chart để xác nhận cấu trúc D1/H1 thật.

**Thesis & claims**:
- C1: Bias D1 = Bullish — tự nhận SAI ngay trong file ("nên là Bearish").
- C2: Checklist tick "Có Market Structure Shift hợp lệ" = `[x]` — **load-bearing claim cho quyết định entry**, vì đây là điều kiện gate chính thức trước khi vào lệnh theo đúng template.
- C3: Narrative M15/M5 ngay phía trên ghi "Có MSS chưa? No" — trực tiếp mâu thuẫn C2.
- C4 (tự nhận): nguyên nhân gốc là revenge trade, gỡ "2 lệnh thua trước đó".
- C5: RR bảng Trade Summary ghi "R Multiple: 1.75" nhưng frontmatter `planned_rr: 2.35`.

**Điều gì đứng vững**: risk_percent 0.5% đúng chuẩn đã công bố — không có gì trong file mâu thuẫn điều này. Tự nhận đầy đủ và chi tiết nguyên nhân gốc (revenge, sai bias, thiếu MSS, FOMO) trong Execution Review là mức độ minh bạch cao nhất trong toàn cụm 6 file.

**Objections**:

**O1 · [SELF-CONTRADICTION] · fatal · attacks C2 (load-bearing)**
Claim: "Có Market Structure Shift hợp lệ" đã được xác nhận (checklist tick `[x]`) trước khi entry.
Fails: ngay trong cùng file, mục "M15/M5" hỏi trực tiếp "Có MSS chưa?" và trả lời "**No**" — cùng một file, cùng một lệnh, hai câu trả lời đối lập cho đúng một câu hỏi.
Evidence: dòng checklist mục 2 "`- [x] Có Market Structure Shift hợp lệ`" đối chiếu dòng mục 1 "`- **Có MSS chưa?** No`".
Consequence: checklist không có giá trị làm gate — nó được tick không nhất quán với chính observation đã ghi, nghĩa là hành động entry (C2 làm cơ sở) không có xác nhận MSS thật nào đứng sau, khớp đúng với mistake tag "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]" mà user tự gắn.
Your best answer: "checklist tick nhầm do điền vội." — Không cứu được: dù là nhầm hay không, hậu quả với việc đánh giá quy trình là giống nhau — checklist không đáng tin làm evidence cho "đã kiểm tra trước khi vào."
Retracted by: xác nhận rằng checklist được tick tại một thời điểm khác (trước khi quan sát M15/M5 thay đổi) — không có timestamp riêng cho từng tick để kiểm.

**O2 · [METHOD] · material · attacks C4**
Claim: "2 lệnh thua trước đó" khiến đây là revenge trade là điều đã biết rõ nguồn.
Fails: file này có timestamp 2026-06-17T08:35 — SỚM HƠN Loss-01 (18T17:36), Loss-02 (18T17:36), Loss-03 (18T20:09) theo frontmatter của 3 file đó. Nếu 2 lệnh thua "trước đó" không phải 3 lệnh này, chúng không có trong 6 file được giao xử lý — nguồn của "2 lệnh thua trước đó" là UNSUPPORTED từ chính bộ dữ liệu hiện có.
Consequence: cụm revenge 06-17 có khả năng bắt đầu SỚM HƠN những gì 6 file trong tập này thể hiện — Loss-04 (08:35) có thể là điểm giữa hoặc cuối của một chuỗi revenge dài hơn, không phải điểm bắt đầu; điều này không đổi verdict của Loss-04 (vẫn là revenge tự nhận) nhưng đổi cách đọc trình tự toàn cụm.
Retracted by: log 2 lệnh thua xảy ra trước 08:35 sáng 06-17 (ngoài phạm vi 6 file này) — không có trong dữ liệu được giao.

**O3 · [ARITHMETIC] · minor** — Trade Summary ghi "R Multiple: 1.75" nhưng frontmatter `planned_rr: 2.35`; tính lại từ entry/SL/TP: risk=148.2, reward=349.0, RR=2.355 — khớp frontmatter, KHÔNG khớp bảng 1.75. Retracted by: xác nhận "R Multiple" trong bảng đo bằng công thức khác (ví dụ R multiple thực tế đã đóng, không phải R multiple kế hoạch) — hiện không nêu rõ.

Drafted 4, cut 1 (draft [DOCTRINE] về "SL đặt beyond structure" bị loại vì checklist tick "Stop loss đặt ở vùng invalidation hợp lý" = unchecked — đã tự nhận sai, không cần thêm objection doctrine riêng, trùng lặp với việc tự nhận).

**Verdict**: **BROKEN** — load-bearing claim C2 (MSS đã xác nhận) sụp trực diện qua tự-mâu-thuẫn trong cùng file (O1, fatal), không cần chart. Tôi tấn công tính nhất quán của checklist và nguồn gốc "2 lệnh thua trước" — phá được O1 hoàn toàn (mâu thuẫn hiển nhiên trong text), không phá được hoàn toàn C4 (revenge trade tự nhận vẫn đứng, chỉ nghi vấn về NGUỒN của nó qua O2). Critique này KHÔNG xác lập được: cấu trúc H1 thật (LH/LL tự nhận, không có chart xác nhận), và danh tính chính xác của "2 lệnh thua trước đó" nếu chúng nằm ngoài 6 file này.

**Bối cảnh cụm 17–18/06**: Loss-04 (08:35 NY session) là lệnh có timestamp SỚM NHẤT trong 6 file cụm 17-18/06, nhưng lại tự nhận là hệ quả của "2 lệnh thua trước đó" — mâu thuẫn với thứ tự file nếu so với Loss-01/02 (17:36) và Loss-03 (20:09), tất cả đều timestamp SAU 08:35 (O2 trên). Đây khớp với CS-O4 (`[METHOD] · material`, "2/4 lệnh **tự nhận** là revenge trade trong đúng mistake tag của chính journal") nhưng mở rộng thêm: chuỗi revenge có khả năng bắt đầu SỚM HƠN phạm vi 6 file này, không kết thúc ở đây. Việc "chờ MSS" bị vi phạm lại đúng lỗi đã ghi thành rule 12 ngày trước (06-05) khớp với timeline CS-O2 (`[METHOD] · fatal`, "vi phạm lại lần 4"). risk_percent 0.5% đúng chuẩn ở đây — khác với 32% lệnh toàn sample risk 5% (CS-O7) — nên phần risk của lệnh này không đóng góp vào rủi ro-of-ruin cấp hệ thống.

## 9. Opposite Case (Counter-Argument)

Load-bearing claim của kèo ngược: cấu trúc H1 "LH/LL" là continuation hợp lệ của một downtrend lớn hơn D1 (chưa hoàn toàn đảo chiều thành uptrend) — "MSS chưa" ở M15/M5 chỉ có nghĩa reversal M5 chưa xảy ra, nhưng entry Long ở đây được đặt đúng như một countertrend bounce trade trong nhịp hồi ngắn, không phải một MSS-based reversal trade; nếu đọc theo khung này, "thiếu MSS" là đúng-như-kỳ-vọng chứ không phải lỗi.

**Tự đánh kèo ngược**: chính user tự chọn Entry Model = "MSS + FVG" trong Trade Summary (không phải "countertrend bounce" hay bất kỳ tên khác) — nếu đây thực sự là một countertrend bounce trade có chủ đích, tên entry model đã ghi sai từ đầu, và mistake tag "Entry When MSS not in POI Zone" (chính user tự gắn) trực tiếp phủ định cách đọc "đúng như kỳ vọng."

**Strength label**: **not viable** — user tự đặt tên entry model là MSS+FVG và tự gắn mistake tag phủ định cách đọc ngược; không có fact nào ủng hộ kèo ngược mà thesis gốc không giải thích được.

**Observable phân biệt**: chart H1 xác nhận liệu cấu trúc thật là LH/LL tiếp diễn (ủng hộ kèo ngược) hay đã có dấu hiệu chuyển tiếp — hiện không có.

## 10. Falsification Tests

1. Nếu tìm được 2 lệnh thua trước 08:35 sáng 06-17 (ngoài 6 file này) — O2 được đóng, xác nhận cụm revenge bắt đầu sớm hơn phạm vi hiện có. Nếu không tìm được trong toàn bộ journal gốc — "2 lệnh thua trước đó" chuyển thành UNSUPPORTED vĩnh viễn.
2. Nếu xác nhận checklist Pre-trade có timestamp tick riêng (trước entry) khác với thời điểm ghi narrative post-trade — O1 được narrow (không đóng hoàn toàn, nhưng giảm severity vì tick không còn đồng thời với narrative mâu thuẫn).
