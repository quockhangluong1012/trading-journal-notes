---
type: mistake
category: execution
severity: high
related_model: ICT 2022
frequency: 4
status: active
tags:
  - trading/ict/mistake
  - trading/review
created: 2026-07-08
updated: 2026-07-08
---

# Mistake - Weak Displacement

> [!summary] Tóm tắt 1 câu
> Chấp nhận một cú "phá vỡ" thiếu năng lượng — thân nến nhỏ, nhiều wick, các nến chồng lấn (grinding), không để lại FVG — như thể nó là displacement thật, dẫn tới một MSS giả và một chuỗi entry mất hết nền tảng bằng chứng ngay từ gốc.

> [!danger] Nguyên tắc cốt lõi
> **Displacement là một biến định lượng được, không phải cảm giác "nhìn có vẻ mạnh".** Một cú đẩy chỉ được tính là displacement khi nó để lại dấu vết của order flow áp đảo: body-to-range cao, bỏ qua giá nhanh, và **tạo ra FVG**. Không có FVG thì gần như chắc chắn chưa đủ mạnh để gọi là displacement.

---

## 1. Mô tả lỗi

Weak displacement là lỗi nằm ở **gốc của cả chuỗi ICT 2022**: displacement là thành phần tạo ra MSS (đóng nến qua protected swing) và tạo ra FVG (POI để entry). Nếu cú đẩy ban đầu yếu, thì cả MSS lẫn FVG phía sau đều thừa hưởng sự yếu đó — bạn xây một entry "A+" trên một nền móng không có bằng chứng order flow.

Cụ thể, trader mắc lỗi này khi:

- Coi một chuỗi nến tăng/giảm *đều đặn, chậm rãi* (grinding move) là displacement, dù không có nến nào thực sự bứt phá.
- Tin vào một cú break mà thân nến nhỏ, wick dài hai đầu, body-to-range thấp — tức phần lớn chuyển động bị "trả lại" ngay trong cùng nến.
- Bỏ qua việc kiểm tra xem cú đẩy có *để lại FVG* hay không — trong khi FVG là hệ quả tự nhiên và là bằng chứng khách quan của một displacement thật.
- Đánh giá displacement bằng mắt ("trông mạnh đấy") thay vì bằng tiêu chí định lượng (body-to-range, so với ATR, có/không FVG).

Đây là lỗi *tiền đề* của hai lỗi khác: nó thường sinh ra [[06 - Mistake - Not Have Market Structure Shift]] (weak MSS) và [[10 - Mistake - FVG Not Valid]] (FVG hình thành từ cú đẩy yếu không đáng tin). Sửa được weak displacement là sửa được cả cụm.

![[WeakDisp-Sec-01-MoTa.svg|760]]
*Sơ đồ: cùng phá qua một mức — bên trái grinding thân nhỏ nhiều wick không FVG (yếu), bên phải thân lớn ít wick để lại FVG (mạnh, là dấu vết order flow thật).*

---

## 2. Biểu hiện & Dấu hiệu nhận biết

Chất lượng displacement có thể chấm điểm theo 5 tiêu chí khách quan. Đây là cách biến "cảm giác mạnh/yếu" thành một quyết định có kỷ luật.

| Tiêu chí | Displacement yếu | Displacement mạnh |
|---|---|---|
| Body-to-range ratio | < 50% (wick chiếm phần lớn) | > 60-70% |
| Range so với ATR / nến liền trước | ~1x hoặc nhỏ hơn | > 1.5-2x |
| Có tạo FVG không? | Không có FVG | FVG rõ ràng |
| Chồng lấn / overlap giữa các nến | Chồng lấn nhiều (grinding) | Ít chồng lấn, dứt khoát |
| Tốc độ & đóng cửa qua mức | Chậm / chỉ wick xuyên qua | Nhanh + đóng cửa (close) qua mức |

Checklist nhanh (thiếu ≥2 tiêu chí "mạnh" → coi là weak):

- [ ] Thân nến displacement có chiếm > 60% range của chính nó không?
- [ ] Range của nó có lớn hơn rõ rệt (≥1.5x) so với trung bình các nến liền trước không?
- [ ] Cú đẩy có để lại một FVG rõ ràng không?
- [ ] Các nến có dứt khoát (ít chồng lấn) hay đang grinding lê từng chút một?
- [ ] Có nến ĐÓNG CỬA qua mức mục tiêu, hay chỉ có wick chạm qua rồi rút?

![[WeakDisp-Sec-02-BieuHien.svg|760]]
*Sơ đồ: bảng 5 tiêu chí chấm điểm chất lượng displacement với ngưỡng yếu/mạnh cho từng tiêu chí.*

---

## 3. Cơ chế & Vì sao nguy hiểm

Về bản chất order flow, **displacement mạnh là dấu vết vật lý của việc một phía áp đảo hoàn toàn phía kia tại một mức giá**. Để giá bỏ qua nhiều mức trong thời gian ngắn và để lại một khoảng FVG (vùng mà một phía không kịp khớp lệnh), cần một khối lượng lệnh thị trường (aggressive orders) đủ lớn nuốt sạch thanh khoản đối nghịch. Đây chính là [[41 - Change in State of Delivery]] — trạng thái giao hàng của thuật toán đã đổi.

Ngược lại, một cú đẩy yếu (grinding, thân nhỏ, nhiều wick, không FVG) phản ánh một trạng thái **cân bằng, giằng co** giữa hai phía — không phía nào thực sự áp đảo. Giá có thể "bò" qua một mức nhờ tích lũy dần, nhưng đó không phải là bằng chứng đổi hướng; nó dễ dàng bị đảo ngược (reclaim) ngay khi phía kia quay lại.

Khi bạn hành động dựa trên weak displacement:

1. **MSS trở thành giả.** Một cú break qua protected swing bằng grinding yếu, không FVG, chỉ là nhiễu — không phải MSS thật (xem [[06 - Mistake - Not Have Market Structure Shift]]). Bạn tưởng cấu trúc đã đổi, nhưng chưa có bằng chứng nào.
2. **FVG (nếu có) không đáng tin.** FVG hình thành từ một cú đẩy yếu thường mỏng, dễ bị lấp hết và xuyên qua — nó không phải là một POI có "trọng lượng" order flow để giá tựa vào (xem [[10 - Mistake - FVG Not Valid]]).
3. **Không có nơi để giá tựa.** Displacement mạnh để lại FVG/liquidity void — vùng inefficiency mà giá thường quay lại để "cân bằng" rồi tiếp tục. Weak displacement không tạo ra vùng này, nên pullback không có điểm đỡ, và giá dễ trôi ngược hết đường.
4. **SL mất logic.** Không có FVG/swing rõ ràng do displacement yếu tạo ra, SL bị đặt cảm tính và thường bị reclaim quét.

![[WeakDisp-Sec-03-CoChe.svg|760]]
*Sơ đồ: cú break yếu (grinding, không FVG) bị giá reclaim ngược qua mức rồi tiếp diễn hướng cũ, quét SL của entry dựa trên displacement không có bằng chứng.*

**Đối với tài khoản prop firm:** weak displacement tạo ra các entry có variance cao ngụy trang dưới vỏ bọc "có cấu trúc" — nguy hiểm hơn cả entry không cấu trúc, vì trader tin mình đã tuân thủ quy trình nên vào full size. Ghi log biến `displacement_quality: strong/weak/none` cho mọi lệnh sẽ phơi bày win rate thật của nhóm "weak" (thường thấp hơn nhiều), là dữ liệu khách quan để loại bỏ chúng khỏi playbook.

---

## 4. Ví dụ minh họa

### ✅ Đúng — displacement mạnh, đóng qua swing, để lại FVG

Giá deliver xuống một bullish POI trong Discount và quét SSL cục bộ. Ngay sau sweep, 2-3 nến thân lớn (body-to-range > 70%, range gấp ~2x các nến trước) bùng lên, **đóng cửa dứt khoát qua protected swing** và để lại một FVG rõ ràng. Tôi chờ giá pullback về FVG đó và vào lệnh, SL dưới sweep/dưới protected swing.

![[WeakDisp-Example-Correct.svg|760]]
*Sơ đồ: sweep SSL → displacement thân lớn đóng qua protected swing (= MSS) → FVG rõ ràng → entry tại FVG với target BSL.*

**Vì sao đúng:** Cú đẩy thỏa cả 5 tiêu chí — body-to-range cao, range lớn hơn ATR, tạo FVG, ít chồng lấn, đóng cửa qua mức. FVG cung cấp một POI có trọng lượng để giá tựa vào khi pullback, cho phép entry với SL chặt và RR cao. Đây là displacement thật: một dấu vết order flow, không phải nhiễu.

### ❌ Sai — coi cú grinding yếu là "MSS"

Giá bò lên qua protected swing bằng một chuỗi nến thân nhỏ, wick dài hai đầu, chồng lấn nhau, không để lại FVG nào. Tôi coi đó là MSS và vào lệnh ngay khi giá "vừa qua mức". Vài nến sau, giá reclaim ngược trở lại dưới mức, quét SL, rồi tiếp tục hướng giảm ban đầu.

![[WeakDisp-Example-Wrong.svg|760]]
*Sơ đồ: chuỗi grinding thân nhỏ không FVG bò qua mức → entry (tưởng là MSS) → giá reclaim, tiếp diễn hướng cũ, quét SL.*

**Bài học:** Một cú "break" bò qua mức mà không có body-to-range cao và không tạo FVG chỉ là kết quả của sự cân bằng tạm thời — không phải bằng chứng đổi hướng. Grinding qua một mức và displacement qua một mức trông giống nhau về *vị trí đóng cửa* nhưng hoàn toàn khác nhau về *ý nghĩa order flow*. Đây chính là [[Loss - 01 - Trade 2026-06-24 GBPUSD Long]] (xem mục 8).

---

## 5. Kiến thức nâng cao (Advanced)

![[WeakDisp-Advanced-Quality.svg|760]]
*Sơ đồ: giải phẫu body-to-range (mạnh ~75% vs yếu ~20%), thang điểm 5 tiêu chí, và chuỗi phụ thuộc displacement → MSS → FVG valid → entry A+.*

### 5.1. Body-to-range ratio — thước đo cốt lõi

Chỉ số quan trọng nhất để định lượng displacement là **tỷ lệ thân/range**: `body / (high - low)`. Một nến displacement thật có thân chiếm phần lớn range (> 60-70%), nghĩa là giá mở cửa ở một đầu và đóng ở gần đầu kia — thể hiện một phía kiểm soát toàn bộ nến, ít bị phản kháng. Một nến với thân < 50% và wick dài hai đầu, dù range tổng thể có vẻ lớn, thực chất phản ánh giằng co: giá đi xa rồi bị đẩy trả lại — chính là dấu hiệu *thiếu* áp đảo order flow. Đây là bộ lọc đầu tiên và nhanh nhất: nhìn thân nến, không nhìn range.

### 5.2. Chuẩn hóa theo ATR — mạnh so với cái gì?

"Mạnh" là một khái niệm tương đối; một range 20 pip có thể là displacement khủng khiếp trên EURUSD giờ Á nhưng chỉ là nhiễu trên XAUUSD giờ NY. Do đó cần chuẩn hóa: so range của nến displacement với **ATR** (hoặc đơn giản là trung bình range của 5-10 nến liền trước cùng khung). Một displacement thật thường có range ≥ 1.5-2x mức trung bình đó. Điều này ngăn việc gọi một nến "to hơn bình thường một chút" là displacement trong khi nó chỉ là dao động thông thường của phiên.

### 5.3. FVG như bằng chứng khách quan — không có FVG, không có displacement

Đây là quy tắc mạnh nhất và ít bị tranh cãi nhất: **một displacement thật gần như luôn để lại FVG** (một inefficiency 3-nến, nơi wick của nến 1 và nến 3 không chạm nhau). Lý do cơ học: để tạo khoảng trống đó, giá phải di chuyển đủ nhanh khiến một phía không kịp khớp lệnh — chính là định nghĩa của imbalance. Nếu một cú đẩy *không* để lại FVG nào, đó là bằng chứng khách quan rằng cả hai phía vẫn khớp lệnh đầy đủ tại mọi mức giá (tức không có imbalance, không có áp đảo). Quy tắc thực hành: dùng sự hiện diện của FVG như một bộ lọc nhị phân — không FVG thì mặc định không phải displacement, bất kể nến trông "mạnh" đến đâu.

### 5.4. Displacement vs expansion vs grinding — ba loại chuyển động

Cần phân biệt ba loại chuyển động thường bị gộp làm một:

- **Displacement (impulsive):** nhanh, thân lớn, tạo FVG, một phía áp đảo — bằng chứng order flow đổi/mở rộng. Đây là cái ICT 2022 cần.
- **Grinding (corrective/consolidation drift):** chậm, thân nhỏ, nhiều wick, chồng lấn, không FVG — giằng co cân bằng, thường là pullback hoặc tích lũy, KHÔNG phải tín hiệu hành động.
- **Expansion sau tích lũy:** một chuỗi displacement nối tiếp mở rộng range của ngày — thường xảy ra sau consolidation trong [[18 - Kill Zones]]. Đây là môi trường lý tưởng cho displacement chất lượng cao.

Nhầm grinding thành displacement là bản chất của lỗi này. Grinding *có thể* đưa giá qua một mức, nhưng nó không mang thông tin hướng đi giống displacement.

### 5.5. Liquidity void & runway — vì sao displacement mạnh "tự nuôi" chính nó

Displacement mạnh thường tạo ra một [[21 - Liquidity Void]] (vùng giá di chuyển quá nhanh, gần như không có giao dịch hai chiều). Vùng void này có hai ý nghĩa: (1) nó là bằng chứng về tốc độ/áp đảo, và (2) nó tạo ra một "đường băng" (runway) — vì thiếu thanh khoản đối nghịch trong void, giá có xu hướng di chuyển nhanh khi quay lại lấp nó, hỗ trợ continuation. Weak displacement không tạo void, nên không có runway này — một lý do nữa khiến các entry dựa trên nó thiếu lực đẩy tiếp diễn.

### 5.6. Timing — displacement thật cần volume phiên

Displacement chất lượng cao đòi hỏi khối lượng lệnh tổ chức đủ lớn, nên nó tập trung trong [[18 - Kill Zones]] (London Open, NY Open) và quanh [[40 - Macro Times]]. Một cú đẩy "trông mạnh" giữa phiên Á hoặc giờ nghỉ trưa NY — nơi thanh khoản mỏng — dễ là kết quả của spread giãn hoặc vài lệnh đơn lẻ hơn là dòng lệnh tổ chức thật. Ngay cả khi thỏa tiêu chí kỹ thuật về body-to-range, một displacement off-session vẫn nên bị hạ mức tin cậy và đòi hỏi thêm xác nhận.

---

## 6. Best Practices

> [!success] Best Practices
> 1. Luôn chấm điểm displacement theo 5 tiêu chí (body-to-range, ATR, FVG, overlap, close qua mức) trước khi tin — không đánh giá bằng mắt.
> 2. Dùng sự hiện diện của FVG làm bộ lọc nhị phân: không FVG → mặc định không phải displacement.
> 3. Kiểm tra body-to-range đầu tiên (nhanh nhất): thân < 50% range → cảnh báo yếu ngay.
> 4. Chuẩn hóa "mạnh" theo ATR / trung bình các nến trước, không so tuyệt đối giữa các cặp/khung.
> 5. Phân biệt rõ displacement (impulsive) với grinding (corrective) — grinding qua mức không phải tín hiệu hành động.
> 6. Ưu tiên displacement trong kill zone / macro times; hạ tin cậy với cú đẩy off-session dù trông mạnh.
> 7. Ghi log `displacement_quality: strong/weak/none` cho mọi lệnh để phơi bày win rate thật theo nhóm.
> 8. Với displacement điểm 2-3 (weak nhưng không phải none), giảm size hoặc chờ xác nhận thêm thay vì full size.

---

## 7. Rule phòng tránh & Checklist

- [ ] Chấm điểm displacement theo 5 tiêu chí trước khi coi bất kỳ cú break nào là hợp lệ.
- [ ] Kiểm tra body-to-range > 60% — nếu thân nhỏ nhiều wick, mặc định là weak.
- [ ] Yêu cầu cú đẩy để lại FVG rõ ràng; không FVG → không phải displacement.
- [ ] So range với ATR / nến liền trước (≥1.5x) thay vì đánh giá tuyệt đối.
- [ ] Phân biệt grinding (chồng lấn, chậm) với displacement (dứt khoát, nhanh) — không nhầm hai loại.
- [ ] Đòi hỏi nến ĐÓNG CỬA qua mức, không chấp nhận chỉ wick xuyên qua.
- [ ] Ưu tiên displacement trong kill zone; hạ tin cậy off-session.
- [ ] Ghi `displacement_quality` vào trade log để review định kỳ.

---

## 8. Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-24 GBPUSD Long]]
-

> [!info] Định dạng liên kết trade
> Khi thêm ví dụ thật, dùng đúng định dạng filename của vault: `[[Result - NN - Trade YYYY-MM-DD SYMBOL Position]]` (Result = Win/Loss/BE).

---

## 9. Flashcards / Active Recall

**Q1:** Tại sao weak displacement là lỗi "gốc" của cả chuỗi ICT 2022?
**A1:** Vì displacement tạo ra MSS (đóng nến qua protected swing) và tạo ra FVG (POI để entry). Nếu cú đẩy gốc yếu, cả MSS lẫn FVG phía sau đều thừa hưởng sự yếu đó — entry được xây trên nền không có bằng chứng order flow.

**Q2:** Chỉ số định lượng cốt lõi nhất để đánh giá displacement là gì và ngưỡng bao nhiêu?
**A2:** Body-to-range ratio = body / (high − low). Displacement mạnh có thân > 60-70% range; thân < 50% với wick dài hai đầu là dấu hiệu giằng co, thiếu áp đảo order flow.

**Q3:** Vì sao "không có FVG" gần như đồng nghĩa với "không phải displacement"?
**A3:** Để tạo FVG (inefficiency 3-nến), giá phải di chuyển đủ nhanh khiến một phía không kịp khớp lệnh — chính là định nghĩa imbalance. Không có FVG nghĩa là hai phía vẫn khớp đầy đủ tại mọi mức = không có áp đảo, không có displacement.

**Q4:** Phân biệt displacement, grinding và expansion.
**A4:** Displacement: nhanh, thân lớn, tạo FVG, một phía áp đảo (tín hiệu hành động). Grinding: chậm, thân nhỏ, chồng lấn, không FVG (giằng co, không phải tín hiệu). Expansion: chuỗi displacement mở rộng range ngày, thường sau tích lũy trong kill zone.

**Q5:** Vì sao displacement mạnh "tự nuôi" continuation còn weak thì không?
**A5:** Displacement mạnh tạo liquidity void — một "đường băng" thiếu thanh khoản đối nghịch, khiến giá di chuyển nhanh khi quay lại lấp và hỗ trợ tiếp diễn. Weak displacement không tạo void nên không có runway này.

**Q6:** Vì sao cần chuẩn hóa displacement theo ATR?
**A6:** Vì "mạnh" là tương đối — một range 20 pip có thể là displacement lớn trên EURUSD giờ Á nhưng chỉ là nhiễu trên XAUUSD giờ NY. So với ATR / trung bình nến trước (≥1.5-2x) ngăn việc gọi một dao động bình thường là displacement.

---

## 10. Lesson Learned

Weak displacement là lỗi nguy hiểm đặc biệt vì nó *cảm giác* như đang tuân thủ quy trình: có sweep, có "break", có "MSS", có "FVG" — đủ hình thức của một setup A+, nhưng thiếu cái duy nhất quan trọng là **năng lượng order flow thật**. Nó dạy một bài học sâu về ICT: mọi khái niệm (MSS, FVG, POI) đều là *hệ quả* của displacement; nếu bỏ qua chất lượng của cái gốc, mọi thứ xây lên trên đều là vỏ rỗng. Chấm điểm displacement một cách định lượng, khách quan — thay vì cảm tính — là cách biến trực giác "nhìn có vẻ mạnh" thành một quy tắc có thể backtest và cải thiện.

Quy tắc cá nhân:
- [ ] Không tin bất kỳ cú break nào nếu body-to-range thấp và không tạo FVG.
- [ ] Luôn chấm điểm 5 tiêu chí trước khi gán nhãn "displacement" cho một chuyển động.
- [ ] Ghi `displacement_quality` để dữ liệu tự loại bỏ các entry weak khỏi playbook.

> Displacement là chữ ký của smart money. Một chữ ký yếu, run rẩy, không dứt khoát thì không đáng để đặt cả tài khoản vào — hãy chờ chữ ký thật.

---

## 11. Liên kết

**Concepts:** [[35 - Aggressive Displacement Entry]] · [[41 - Change in State of Delivery]] · [[13 - FVG  - Fair Value Gap]] · [[21 - Liquidity Void]] · [[21 - Market Structure Shift]] · [[05 - BOS - Break of Structure]] · [[18 - Kill Zones]] · [[40 - Macro Times]]

**Mistakes liên quan:** [[06 - Mistake - Not Have Market Structure Shift]] · [[10 - Mistake - FVG Not Valid]] · [[03 - Mistake - Entry When MSS not in POI Zone]]
