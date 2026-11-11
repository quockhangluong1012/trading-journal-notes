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
created: 2026-06-19
updated: 2026-07-08
---

# Mistake - Enter before liquidity sweep

> [!summary] Tóm tắt 1 câu
> Vào lệnh tại OB/FVG ngay lần chạm đầu tiên trong khi pool thanh khoản liên quan (SSL cho long, BSL cho short) vẫn còn nguyên — nghĩa là tự nguyện làm thanh khoản đối ứng cho cú fill của smart money thay vì chờ họ "ăn" xong rồi mới vào.

> [!danger] Nguyên tắc cốt lõi
> Không có sweep + confirmation = không có giao dịch. Một OB/FVG "đẹp" mà thanh khoản rõ ràng vẫn còn treo ngay phía sau nó gần như luôn luôn là **inducement**, không phải POI thật.

---

## 1. Mô tả lỗi

Đây là lỗi entry sớm kinh điển trong ICT 2022 Model: giá đi vào một OB hoặc FVG, xuất hiện phản ứng đầu tiên (wick nhỏ, nến đảo chiều, momentum chững lại), và trader vào lệnh ngay lập tức — trong khi liquidity pool liên quan (equal highs/lows, old high/low, session high/low) mà mô hình cần quét để có draw on liquidity **vẫn chưa bị chạm**.

Về bản chất, đây không phải là entry theo ICT 2022, mà là entry theo cảm tính "giá phản ứng là vào". Điều kiện bắt buộc của mô hình — **sweep liquidity → displacement → MSS → entry tại POI (FVG/OB) hình thành sau MSS** — bị bỏ qua bước đầu tiên và quan trọng nhất.

- Tôi vào lệnh khi thấy giá chạm OB/FVG và xuất hiện tín hiệu rejection, dù chưa có sweep.
- Tôi đuổi theo giá vì sợ bỏ lỡ, coi phản ứng giá đầu tiên là đủ điều kiện.
- Tôi bỏ qua việc kiểm tra xem còn pool thanh khoản nào "rõ ràng" đang treo ngay phía sau entry hay không.

![[EarlyEntry-Sec-01-MoTa.svg|760]]
*Sơ đồ: entry sớm khi SSL vẫn còn nguyên — SL nằm đúng nơi thuật toán còn cần chạy qua.*

---

## 2. Biểu hiện & Dấu hiệu nhận biết

| Dấu hiệu | Mức độ cảnh báo |
|---|---|
| Vào lệnh ngay lần chạm đầu tiên vào OB/FVG | Amber |
| Chưa có wick/displacement vượt qua pool thanh khoản gần nhất | Amber |
| Cảm giác FOMO "sợ bỏ lỡ lệnh đẹp" chi phối quyết định | Amber |
| Equal highs/equal lows hoặc old high/low còn "treo" ngay sau entry | Đỏ |
| OB/FVG "quá sạch, quá rõ" mà không cần chờ đợi gì | Đỏ |
| FVG hình thành nhưng không đi kèm MSS thật sự (xem [[06 - Mistake - Not Have Market Structure Shift]]) | Đỏ |

Checklist nhận diện nhanh trước khi bấm lệnh:

- [ ] Có pool thanh khoản rõ ràng (equal H/L, old H/L) nằm ngay phía sau hướng đi dự kiến của SL không?
- [ ] Nến hiện tại đã có wick/close vượt qua pool đó chưa, hay chỉ mới "chạm gần"?
- [ ] Phản ứng giá tại OB/FVG này có đi kèm MSS hợp lệ hay chỉ là momentum chững tạm thời?
- [ ] Tôi có đang vào lệnh vì sợ bỏ lỡ, hay vì đã có đủ điều kiện xác nhận?

![[EarlyEntry-Sec-02-BieuHien.svg|760]]
*Sơ đồ: các tell cảnh báo khi entry trong lúc pool thanh khoản (equal lows) vẫn còn nguyên.*

---

## 3. Cơ chế & Vì sao nguy hiểm

Thị trường (đặc biệt các cặp có thanh khoản sâu và bị chi phối bởi order flow tổ chức) vận hành theo cơ chế **draw on liquidity**: giá luôn có xu hướng di chuyển về phía pool thanh khoản gần nhất chưa bị khai thác, vì đó là nơi tồn tại resting orders (stop loss của trader retail, pending orders) mà smart money cần đối ứng để fill khối lượng lớn. Xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]].

Khi bạn entry trước khi sweep xảy ra:

1. **Inducement được kích hoạt** — OB/FVG "đẹp" mà bạn thấy thường được thiết kế (về mặt cấu trúc giá) để hấp dẫn entry sớm. Xem [[15 - Inducement]].
2. **Bạn trở thành thanh khoản** — SL của bạn nằm đúng vị trí mà thuật toán/dòng lệnh tổ chức còn cần "ăn" để hoàn tất chu trình sweep. Bạn không giao dịch cùng chiều với smart money — bạn đang cấp thanh khoản đối ứng cho họ.
3. **Sweep thật sự diễn ra sau đó** — giá tiếp tục chạy về pool SSL/BSL thật, quét luôn cả SL của bạn trên đường đi.
4. **Draw on liquidity được giải phóng** — sau khi thanh khoản đã bị hấp thụ, giá mới thật sự đảo chiều và di chuyển đúng hướng bias ban đầu của bạn — nhưng bạn đã bị out từ trước. Đây chính là mô hình **turtle soup ngược lại bạn** (xem [[33 - Turtle Soup]]).

Về mặt kỳ vọng (EV): entry sớm không làm bạn sai *hướng*, nó làm bạn sai *thời điểm và vị trí SL*. SL bị đặt tại nơi có xác suất bị chạm cao nhất trước khi di chuyển đúng hướng, nên win rate và R thực tế đều bị bào mòn dù setup "nhìn" hợp lệ.

![[EarlyEntry-Sec-03-CoChe.svg|760]]
*Sơ đồ: chuỗi cơ chế inducement → entry sớm → sweep thật → draw on liquidity, và turtle soup ngược lại trader.*

---

## 4. Ví dụ minh họa

### ✅ Đúng

Giá đi vào HTF discount POI → quét SSL cục bộ (wick xuyên qua equal lows, đóng nến trở lại bên trong range) → xuất hiện displacement mạnh + MSS xác nhận đổi cấu trúc → entry tại FVG hình thành ngay sau MSS, SL đặt dưới điểm sweep.

![[EarlyEntry-Example-Correct.svg|760]]
*Sơ đồ: HTF discount POI → sweep SSL (wick + close back inside) → displacement + MSS → entry FVG với SL dưới sweep.*

**Vì sao đúng:** Thứ tự sự kiện đầy đủ theo ICT 2022 Model — thanh khoản đã bị khai thác trước, đợt di chuyển sau đó là dòng tiền thật (không phải phản ứng ngẫu nhiên), MSS xác nhận đổi cấu trúc, và SL được đặt sau điểm sweep nên xác suất bị quét lại là thấp. Entry là kết quả của confirmation, không phải dự đoán.

### ❌ Sai

Mua FVG ngay khi giá chạm lần đầu, trong khi equal lows vẫn còn nguyên vẹn ngay phía dưới entry. Giá sau đó spike xuyên qua equal lows, quét luôn SL, rồi mới rally đúng hướng bias ban đầu.

![[EarlyEntry-Example-Wrong.svg|760]]
*Sơ đồ: mua FVG khi equal lows chưa bị quét → giá spike qua equal lows, dính SL, rồi mới rally đúng hướng.*

**Bài học:** Bias đúng không cứu được một entry sai thời điểm. Nếu đã xác định đúng hướng thị trường sẽ đi, việc **kiên nhẫn chờ sweep** không làm mất cơ hội — nó chỉ dịch chuyển điểm vào lệnh đến vị trí có SL an toàn hơn và xác suất cao hơn.

---

## 5. Kiến thức nâng cao (Advanced)

![[EarlyEntry-Advanced-Inducement.svg|760]]
*Sơ đồ: OB "rõ ràng" thường là inducement nằm TRÊN POI thật (cho lệnh mua) — quét inducement low mới lộ ra POI thật.*

### 5.1. Inducement vs POI thật

Trong đa số trường hợp, OB/FVG "sạch" và dễ thấy nhất trên chart **không phải** là POI mà ICT 2022 Model nhắm tới — nó là **inducement** đặt phía trên POI thật (đối với thiết lập mua) hoặc phía dưới POI thật (đối với thiết lập bán). Lý do: chính vì nó dễ thấy, nó thu hút entry sớm từ số đông retail, tạo ra chính pool thanh khoản (inducement low/high) mà smart money cần quét trước khi đẩy giá vào vùng discount/premium sâu hơn — nơi POI thật nằm ở đó. Cách nhận diện: nếu OB đầu tiên bạn thấy nằm ở vùng chưa đủ sâu trong discount/premium, và phía dưới/trên nó vẫn còn một mức đáy/đỉnh nhỏ (inducement low/high) chưa bị quét, hãy giả định OB đó là bẫy cho tới khi được chứng minh ngược lại.

### 5.2. Sweep quality — phân loại chất lượng cú quét

Không phải mọi cú chạm vào pool thanh khoản đều có giá trị như nhau:

- **Wick sweep + close back inside (hợp lệ):** giá xuyên qua mức thanh khoản bằng wick, nhưng đóng nến trở lại bên trong range trước đó → dấu hiệu hấp thụ thanh khoản thành công, chuẩn bị đảo chiều.
- **Body acceptance vượt qua mức (không phải sweep — là invalidation/continuation):** giá đóng nến hẳn bên ngoài mức thanh khoản → thị trường đang chấp nhận giá ở vùng mới, đây là tín hiệu tiếp diễn cấu trúc theo hướng đó, không phải sweep để đảo chiều. Nhầm lẫn hai loại này là nguyên nhân phổ biến khiến trader "đoán đáy/đỉnh" sai.

### 5.3. IRL vs ERL — quét cái nào mới đủ điều kiện entry

Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]]. Không phải lúc nào cũng cần một cú sweep external (old swing high/low) mới được entry — đôi khi internal range liquidity (một FVG chưa lấp, một inefficiency nội bộ) đã đủ để dẫn dắt giá tới POI. Việc xác định đúng target thanh khoản nào (IRL hay ERL) là điều kiện tiên quyết đang được nhắm tới trong con sóng hiện tại sẽ quyết định bạn cần chờ sweep nào trước khi entry được xem là "sạch".

### 5.4. Timing — sweep theo kill zone và Judas swing

Các cú sweep có chất lượng cao thường xảy ra trong [[18 - Kill Zones]] (London Open, New York Open) và gắn liền với Judas swing — cú đẩy giá sai hướng đầu phiên để quét thanh khoản trước khi đảo chiều theo bias thật. Một "cú sweep" xảy ra ngoài các khung giờ này (giữa phiên Á, giờ thấp thanh khoản) có độ tin cậy thấp hơn nhiều vì thiếu volume tổ chức đứng sau để xác nhận đó là hành động có chủ đích chứ không phải nhiễu giá ngẫu nhiên.

### 5.5. Đánh đổi kiên nhẫn / kỳ vọng (patience vs expectancy)

Chờ sweep làm giảm **tần suất** giao dịch (bỏ lỡ một số setup mà giá không bao giờ quay lại quét thanh khoản), nhưng đổi lại:

- **Win rate tăng** vì entry chỉ diễn ra sau khi có confirmation thật (sweep + displacement + MSS) thay vì dự đoán.
- **RR cải thiện** vì SL được đặt ngay sau điểm sweep (khoảng cách tối ưu, không cần "đệm" rộng để tránh nhiễu) thay vì đặt tại vùng còn có khả năng bị quét thêm lần nữa.

Về lâu dài, expectancy (EV = Win% × R trung bình thắng − Loss% × R trung bình thua) của việc chờ sweep gần như luôn cao hơn việc vào sớm, dù số lệnh mỗi tuần ít hơn.

### 5.6. Ngoại lệ hợp lệ — continuation entry

Không phải lúc nào cũng bắt buộc chứng kiến sweep ngay trước mắt. Nếu HTF sweep đã xảy ra trước đó (đã được xác nhận bằng MSS/displacement trên khung lớn hơn) và bạn đang tham gia vào một leg đã được thiết lập — ví dụ entry tại một FVG continuation trong cùng leg sau MSS ban đầu — thì đây là continuation entry hợp lệ, không phải lỗi entry sớm. Guardrail bắt buộc: chỉ áp dụng ngoại lệ này khi (1) MSS gốc đã rõ ràng và chưa bị phá vỡ, (2) POI continuation nằm đúng phía discount/premium phù hợp với bias, và (3) không có pool thanh khoản lớn hơn, chưa bị quét, nằm giữa giá hiện tại và POI continuation đó. Nếu có, quy tắc chờ sweep vẫn được ưu tiên.

---

## 6. Best Practices

> [!success] Best Practices
> 1. Luôn xác định pool thanh khoản liên quan (SSL/BSL, equal H/L, old H/L) trước khi tìm điểm entry — không phải sau.
> 2. Phân biệt rõ inducement OB/FVG (thường ở gần, dễ thấy) với POI thật (thường sâu hơn trong discount/premium).
> 3. Chỉ coi là "sweep hợp lệ" khi có wick xuyên qua kèm đóng nến trở lại bên trong — không tính body acceptance.
> 4. Đòi hỏi MSS thật sự sau sweep trước khi tìm FVG/OB để entry, không dùng phản ứng giá đơn thuần làm tín hiệu.
> 5. Ưu tiên các cú sweep xảy ra trong kill zone (London/NY) và gắn với Judas swing — nghi ngờ sweep ngoài khung giờ thanh khoản thấp.
> 6. Đặt SL sau điểm sweep, không đặt trước — đó là lý do RR của entry đúng thời điểm luôn tốt hơn.
> 7. Nếu dùng continuation entry, kiểm tra guardrail ở mục 5.6 trước khi bỏ qua yêu cầu sweep.
> 8. Ghi log lại mọi lần "suýt vào sớm" — kể cả khi không vào lệnh — để rèn phản xạ chờ đợi.

---

## 7. Rule phòng tránh & Checklist

- [ ] Không vào lệnh nếu chưa có sweep liquidity (wick + close back inside) được xác nhận.
- [ ] Không coi phản ứng giá đầu tiên tại OB/FVG là đủ điều kiện entry nếu chưa có MSS đi kèm.
- [ ] Kiểm tra: còn equal highs/lows hoặc old high/low nào chưa bị quét nằm giữa giá hiện tại và hướng SL dự kiến không?
- [ ] Xác định đây là entry vào IRL hay ERL, và pool nào thực sự cần bị quét trước khi entry được coi là hợp lệ.
- [ ] Nếu sweep xảy ra ngoài kill zone, hạ mức tin cậy và đòi hỏi thêm xác nhận (SMT, displacement mạnh hơn).
- [ ] Nếu dùng continuation entry, xác nhận đủ 3 điều kiện guardrail (mục 5.6) trước khi bỏ qua yêu cầu sweep.
- [ ] Đặt SL sau điểm sweep thật, không đặt tại vùng có thể còn bị quét thêm.
- [ ] Tự hỏi: "Tôi đang giao dịch theo confirmation, hay theo nỗi sợ bỏ lỡ?"

---

## 8. Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-17 EURUSD Long]]
- 

---

## 9. Flashcards / Active Recall

**Q1:** Vì sao entry trước khi sweep khiến bạn "trở thành thanh khoản" thay vì giao dịch cùng smart money?
**A1:** Vì SL của bạn nằm đúng nơi pool thanh khoản chưa bị khai thác — thuật toán/dòng lệnh tổ chức cần "ăn" đúng vị trí đó để hoàn tất draw on liquidity, nên SL của bạn trở thành một phần thanh khoản đối ứng bị quét trên đường giá di chuyển tới pool thật.

**Q2:** Phân biệt sweep hợp lệ và body acceptance như thế nào?
**A2:** Sweep hợp lệ là wick xuyên qua mức thanh khoản rồi đóng nến trở lại bên trong range trước đó (hấp thụ thanh khoản, chuẩn bị đảo chiều). Body acceptance là đóng nến hẳn bên ngoài mức đó — tín hiệu tiếp diễn cấu trúc, không phải sweep để đảo chiều.

**Q3:** Tại sao OB/FVG "quá đẹp, quá rõ" trên chart lại đáng ngờ?
**A3:** Vì tính dễ thấy của nó thu hút entry sớm từ số đông, biến chính nó thành nguồn thanh khoản (inducement) mà smart money cần quét trước khi đẩy giá vào POI thật nằm sâu hơn trong vùng discount/premium.

**Q4:** Chờ sweep làm giảm điều gì và cải thiện điều gì?
**A4:** Giảm tần suất giao dịch (một số setup không bao giờ quay lại quét thanh khoản), nhưng cải thiện win rate (chỉ vào sau confirmation thật) và RR (SL đặt gần hơn, sau điểm sweep thay vì đặt "đệm" rộng).

**Q5:** Khi nào một continuation entry không cần chờ sweep mới vẫn hợp lệ?
**A5:** Khi MSS gốc trên HTF đã rõ ràng và chưa bị phá vỡ, POI continuation nằm đúng phía discount/premium phù hợp bias, và không còn pool thanh khoản lớn nào chưa bị quét nằm giữa giá hiện tại và POI đó.

**Q6:** Vì sao sweep trong kill zone đáng tin hơn sweep giữa phiên Á?
**A6:** Vì kill zone (London/NY Open) có volume tổ chức đứng sau, thường gắn với Judas swing có chủ đích; sweep ngoài khung giờ thanh khoản thấp dễ là nhiễu giá ngẫu nhiên, thiếu dòng lệnh xác nhận.

---

## 10. Lesson Learned

Bài học chính: **kiên nhẫn chờ sweep không phải là bỏ lỡ cơ hội — nó là điều kiện để cơ hội đó thật sự tồn tại.** Một bias đúng bị phá hỏng bởi một entry sai thời điểm vẫn là một lệnh thua, và tệ hơn, nó là loại thua âm thầm bào mòn tài khoản và tâm lý (dính SL "ngay trước khi đi đúng hướng" liên tục dẫn tới tilt và mất niềm tin vào chính bias đúng của mình). Đối với tài khoản prop firm (FTMO/The5ers), việc sửa lỗi này trực tiếp cải thiện cả win rate lẫn RR — hai yếu tố quyết định tính nhất quán mà các bài đánh giá consistency của prop firm yêu cầu.

Quy tắc cá nhân:
- [ ] Không entry nếu pool thanh khoản liên quan chưa bị quét bằng wick + close back inside.
- [ ] Luôn đòi hỏi MSS sau sweep trước khi tìm điểm entry tại FVG/OB.
- [ ] Ưu tiên sweep trong kill zone; hạ độ tin cậy với sweep ngoài khung giờ thanh khoản thấp.

> Chờ đợi sweep là trả giá bằng tần suất để mua lấy xác suất — đó là một sự đánh đổi có lợi cho expectancy dài hạn, không phải sự chậm trễ vô ích.

---

## 11. Liên kết

**Concepts:** [[20 - Liquidity Sweep]] · [[15 - Inducement]] · [[19 - Liquidity]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] · [[33 - Turtle Soup]] · [[18 - Kill Zones]]

**Mistakes liên quan:** [[06 - Mistake - Not Have Market Structure Shift]] · [[03 - Mistake - Entry When MSS not in POI Zone]] · [[09 - Mistake - Wrong daily bias]]
