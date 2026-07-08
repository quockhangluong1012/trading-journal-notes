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

# Mistake - FVG Not Valid

> [!summary] Tóm tắt 1 câu
> Vào lệnh tại một khoảng trống 3 nến chỉ vì nó *trông giống* một FVG — trong khi nó không thỏa các điều kiện hợp lệ (sinh từ displacement mạnh, còn fresh, đúng phía Premium/Discount, cùng hướng bias/draw HTF, có cấu trúc chống lưng, đủ dày để dùng CE) — biến một hình dạng trên chart thành một POI không có trọng lượng order flow.

> [!danger] Nguyên tắc cốt lõi
> **Hình dạng FVG là điều kiện cần, không phải điều kiện đủ.** Bất kỳ chuyển động nào cũng để lại vô số khoảng trống 3 nến; chỉ một số ít trong đó là POI đáng vào. Một FVG đáng giao dịch là một FVG *có bối cảnh* — nó ở đúng nơi, đúng phía, đúng hướng, và được sinh ra bởi bằng chứng order flow thật.

---

## 1. Mô tả lỗi

FVG Not Valid là lỗi coi *mọi* khoảng trống 3 nến là một Fair Value Gap có thể entry. Về mặt hình học, một FVG chỉ đơn giản là vùng inefficiency giữa wick của nến 1 và wick của nến 3 (xem [[13 - FVG  - Fair Value Gap]]). Nhưng thị trường tạo ra hàng chục khoảng trống như vậy mỗi phiên — phần lớn không mang ý nghĩa gì. Trader mắc lỗi này khi:

- Vẽ một FVG bất kỳ đâu giá có khoảng trống và coi đó là POI, không kiểm tra bối cảnh.
- Vào một FVG **đã bị mitigate** (giá đã quay lại chạm/lấp trước đó) — nơi các lệnh tổ chức chống lưng cho FVG đã được khớp hết.
- Vào một FVG nằm **sai phía Premium/Discount** — ví dụ mua tại một bullish FVG nằm trong vùng Premium, hoặc ngược hướng bias HTF.
- Vào một FVG sinh ra từ một cú đẩy **yếu** (grinding), không phải displacement thật — kế thừa trực tiếp lỗi [[08 - Mistake - Weak Displacement]].
- Vào một FVG **ngẫu nhiên** giữa range, không được tạo bởi một MSS/CISD, nên không có vai trò cấu trúc.
- Đo và đặt entry sai mốc — vào ở rìa FVG thay vì quanh CE (Consequent Encroachment, 50% của FVG).

Đây là lỗi ở khâu chọn POI. Nó thường là hệ quả cuối của chuỗi: weak displacement → weak MSS → FVG không đáng tin. Sửa lỗi này đòi hỏi một bộ tiêu chí hợp lệ rõ ràng thay cho phản xạ "thấy khoảng trống là vào".

![[FVGInvalid-Sec-01-MoTa.svg|760]]
*Sơ đồ: giải phẫu một FVG hợp lệ (sinh từ displacement, khe rõ, còn nguyên, đúng phía Discount) so với một FVG không hợp lệ (mỏng, sinh từ cú đẩy yếu, đã bị wick sau lấp hết / sai phía).*

---

## 2. Biểu hiện & Dấu hiệu nhận biết

Một FVG chỉ là POI đáng vào khi thỏa **đủ 6 điều kiện**. Đây là bộ lọc biến "thấy khoảng trống là vào" thành một quyết định có kỷ luật.

| # | Điều kiện hợp lệ | Dấu hiệu KHÔNG hợp lệ |
|---|---|---|
| 1 | Nến giữa là displacement mạnh (body lớn) | Sinh từ grinding / cú đẩy yếu, không có body lớn |
| 2 | Còn fresh (chưa bị giá quay lại chạm/lấp) | Đã bị test/mitigate một phần hoặc toàn bộ |
| 3 | Đúng phía Premium/Discount | Bullish FVG ở Premium / bearish FVG ở Discount |
| 4 | Cùng hướng bias HTF + draw on liquidity | Ngược bias, là FVG counter-trend |
| 5 | Có MSS/CISD chống lưng (được tạo bởi cú shift) | FVG ngẫu nhiên giữa range, không vai trò cấu trúc |
| 6 | Đủ dày để dùng CE làm mốc entry/SL | Quá mỏng, chỉ là nhiễu, không đo được CE |

Checklist nhanh (thiếu 1 điều kiện đỏ → không entry):

- [ ] Nến giữa của FVG có phải displacement thật không (không phải grinding)?
- [ ] FVG này còn nguyên (fresh), hay giá đã từng quay lại chạm/lấp nó?
- [ ] Bullish FVG có nằm trong Discount không? Bearish FVG có nằm trong Premium không?
- [ ] FVG này có cùng hướng với bias HTF và draw on liquidity không?
- [ ] FVG được tạo ra bởi một MSS/CISD, hay chỉ là một khoảng trống ngẫu nhiên?
- [ ] FVG có đủ dày để đặt entry quanh CE và SL hợp lý không?

![[FVGInvalid-Sec-02-BieuHien.svg|760]]
*Sơ đồ: bảng 6 điều kiện hợp lệ của một FVG (displacement, fresh, đúng PD, đúng bias, có MSS chống lưng, đủ dày/CE dùng được).*

---

## 3. Cơ chế & Vì sao nguy hiểm

Về bản chất order flow, một FVG là dấu vết của một **imbalance** — vùng giá mà một phía áp đảo mạnh đến mức phía kia không kịp khớp lệnh, để lại các đơn hàng chưa được thực thi. Thuật toán có xu hướng đưa giá quay lại vùng này để "cân bằng" (rebalance/mitigate) — khớp nốt các đơn còn treo — trước khi tiếp tục. Chính cơ chế đó khiến FVG trở thành một POI: nó là *nơi có lệnh tổ chức đang chờ*.

Nhưng logic đó chỉ đúng khi các điều kiện bối cảnh được thỏa. Khi entry một FVG không hợp lệ:

1. **FVG đã mitigate = "hết đơn hàng".** Nếu giá đã quay lại lấp FVG trước đó, các lệnh tổ chức chống lưng cho nó đã được khớp. Lần thứ hai giá quay lại, không còn lực đỡ — giá xuyên thẳng qua và quét SL. Đây là cơ chế thất bại phổ biến nhất của lỗi này.
2. **Sai phía PD = giao dịch ngược giá trị.** Một bullish FVG nằm ở Premium nghĩa là bạn đang mua đắt; nó thường chỉ là một FVG counter-trend hình thành trong một pullback của xu hướng giảm lớn hơn — giá pullback tới đó rồi tiếp tục giảm. Xem [[27 - Premium Discount]].
3. **Ngược draw HTF = bơi ngược dòng.** Nếu draw on liquidity của khung lớn hướng xuống (về SSL), thì một FVG mua, dù fresh và đúng hình dạng, vẫn đang cược ngược dòng chảy thanh khoản chính — xác suất thấp.
4. **Không có cấu trúc chống lưng = không có "lý do" để giá tôn trọng.** Một FVG được tạo bởi MSS/CISD ([[41 - Change in State of Delivery]]) đánh dấu nơi order flow vừa đổi; một FVG ngẫu nhiên giữa range không đánh dấu gì cả — không có lý do thuật toán nào để giá phản ứng tại đó.
5. **Sinh từ displacement yếu = imbalance giả.** Nếu nến giữa không phải displacement thật, thì "khoảng trống" đó không phản ánh imbalance thực — không có đơn hàng chưa khớp đáng kể để chờ (xem [[08 - Mistake - Weak Displacement]]).

![[FVGInvalid-Sec-03-CoChe.svg|760]]
*Sơ đồ: FVG được tôn trọng ở lần chạm đầu tiên (đơn hàng còn), nhưng ở lần thứ hai — sau khi đã mitigate — giá xuyên thẳng qua vì đơn hàng đã hết, quét SL.*

**Đối với tài khoản prop firm:** vì FVG là bước chọn điểm entry cuối cùng, một FVG không hợp lệ dẫn thẳng tới SL bị quét mà không có bất kỳ "đệm" cấu trúc nào. Do FVG xuất hiện dày đặc, đây cũng là lỗi dễ dẫn tới overtrading (vào mọi khoảng trống thấy được). Ghi log biến `fvg_valid: yes/no` và lý do loại (mitigated / wrong PD / against bias / weak disp) sẽ phơi bày nhóm FVG nào thực sự có edge.

---

## 4. Ví dụ minh họa

### ✅ Đúng — FVG hợp lệ: fresh, Discount, theo bias, entry tại CE

HTF bias bullish, draw on liquidity hướng lên BSL. Giá sweep SSL cục bộ, sau đó một displacement mạnh đóng qua protected swing (MSS) và để lại một FVG rõ ràng nằm trong vùng **Discount**. FVG này còn nguyên (chưa bị chạm). Tôi chờ giá pullback về **CE (50%)** của FVG và vào lệnh tại đó, SL dưới FVG/điểm sweep, target là BSL.

![[FVGInvalid-Example-Correct.svg|760]]
*Sơ đồ: sweep → displacement + MSS tạo FVG fresh trong Discount đúng bias bullish → entry tại CE của FVG, SL dưới FVG, target BSL.*

**Vì sao đúng:** FVG thỏa cả 6 điều kiện — sinh từ displacement, còn fresh, nằm ở Discount, cùng hướng bias/draw HTF, được tạo bởi MSS (có cấu trúc chống lưng), và đủ dày để dùng CE làm mốc entry/SL. Đây là một POI *có bối cảnh*, không phải một khoảng trống ngẫu nhiên.

### ❌ Sai — mua FVG nằm ở Premium, ngược bias HTF

HTF bias là giảm (draw hướng xuống SSL). Trong một nhịp pullback tăng, hình thành một bullish FVG nằm ở vùng **Premium**. Tôi thấy "một FVG đẹp" và vào mua tại đó — bỏ qua việc nó ở sai phía PD và ngược hướng bias. Giá chỉ pullback chạm FVG rồi tiếp tục giảm theo đúng bias HTF, quét SL sớm.

![[FVGInvalid-Example-Wrong.svg|760]]
*Sơ đồ: HTF bias giảm; bullish FVG nằm ở Premium (sai phía, ngược draw) → BUY → giá tiếp tục giảm theo bias, quét SL.*

**Bài học:** Một FVG "hình dạng đẹp" nhưng sai phía Premium/Discount và ngược draw HTF chỉ là một bẫy counter-trend. Hình dạng không bao giờ đủ — phải hỏi *FVG này ở đâu, thuộc leg nào, cùng hướng gì*. Đây chính là [[Loss - 01 - Trade 2026-06-26 XAUUSD Long]] (xem mục 8).

---

## 5. Kiến thức nâng cao (Advanced)

![[FVGInvalid-Advanced-Validity.svg|760]]
*Sơ đồ: CE (50%) làm mốc entry/đo phản ứng, ba mức độ mitigation (fresh > partial > đã lấp hết), khái niệm iFVG (FVG bị đóng xuyên → đổi vai trò), và cây quyết định 5 bước trước khi entry một FVG.*

### 5.1. Consequent Encroachment (CE) — đo và entry tại 50%, không tại rìa

[[10 - Consequent Encroachment (Mean Threshold)]] là mức 50% (mean threshold) của một FVG, và nó là mốc quan trọng hơn hai rìa. Lý do: CE đại diện cho "giá trị trung bình" của vùng imbalance — nơi lệnh tổ chức có mật độ cao nhất. Thực hành: entry nên đặt quanh CE, và một FVG được coi là còn hiệu lực khi giá chưa đóng cửa vượt qua CE của nó. Nhiều trader mắc lỗi vào ngay tại rìa gần của FVG (điểm chạm đầu tiên) và bị stopped out bởi dao động thông thường bên trong FVG — trong khi phản ứng thật thường xảy ra quanh CE. Dùng CE cũng cho SL chặt hơn và RR tốt hơn.

### 5.2. Mức độ mitigation — fresh > partial > đã lấp hết

Không phải FVG "đã bị chạm" nào cũng vô dụng như nhau; có một phổ:

- **Fresh (0% mitigated):** giá chưa từng quay lại — đầy đủ đơn hàng, xác suất phản ứng cao nhất.
- **Partial (chạm tới CE nhưng chưa lấp hết):** một phần đơn đã khớp; nếu giá chỉ chạm rìa xa và bật, phần quanh CE có thể vẫn còn hiệu lực. Đánh giá cẩn thận.
- **Đã lấp hết (fully mitigated):** giá đã đi qua toàn bộ FVG hoặc đóng cửa vượt CE — coi như hết đơn hàng, hết hiệu lực. Không entry lần hai vào một FVG đã lấp hết.

Quy tắc: ưu tiên tuyệt đối FVG fresh; với FVG đã chạm, chỉ cân nhắc nếu phản ứng tập trung quanh CE và phần quan trọng chưa bị xuyên.

### 5.3. Inverse FVG (iFVG) — khi FVG đổi vai trò

Khi giá **đóng cửa xuyên qua** một FVG theo hướng ngược lại (ví dụ một bullish FVG bị một nến giảm đóng cửa hẳn bên dưới), FVG đó thất bại và **đảo vai trò** thành [[17 - Inverse Fair Value Gap - iFVG]] — từ vùng hỗ trợ trở thành vùng kháng cự (và ngược lại). Đây vừa là bẫy (nếu bạn vẫn cố mua một bullish FVG đã bị đóng xuyên), vừa là cơ hội (nếu bạn nhận ra nó đã thành iFVG và giao dịch theo chiều mới). Nhầm một iFVG với một FVG còn hiệu lực là một biến thể tinh vi của lỗi "FVG not valid".

### 5.4. FVG ngẫu nhiên vs FVG có cấu trúc (do MSS/CISD tạo)

Điểm phân biệt quan trọng nhất về *chất lượng*: một FVG được tạo ra bởi chính cú displacement gây ra MSS/CISD đánh dấu nơi order flow vừa đổi hướng — nó có "lý do tồn tại". Một FVG hình thành giữa một range đi ngang, hoặc trong một nhịp continuation không đáng kể, không đánh dấu sự kiện order flow nào — nó chỉ là inefficiency vô nghĩa. Bài kiểm tra: *"FVG này được sinh ra bởi sự kiện gì?"* Nếu câu trả lời không phải "cú MSS/displacement vừa đổi cấu trúc", hãy nghi ngờ.

### 5.5. Đa khung & FVG lồng nhau (nested/fractal)

FVG tồn tại ở mọi khung thời gian, và một FVG HTF (H1/H4) thường chứa nhiều FVG LTF (M5/M1) bên trong. Confluence mạnh nhất là khi một FVG LTF nằm ngay bên trong CE của một FVG HTF cùng hướng — hai vùng imbalance chồng nhau. Ngược lại, một FVG M1 đơn lẻ, không nằm trong bất kỳ FVG HTF nào và ngược hướng khung lớn, là ứng viên yếu nhất. Dùng FVG HTF để xác định "vùng", FVG LTF để tinh chỉnh entry — không dùng một FVG M1 lạc lõng làm lý do entry chính.

### 5.6. Implied FVG & thị trường ít gap

[[14 - Implied Fair Value Gap]] (IFVG theo nghĩa "implied") là dạng inefficiency tinh vi hơn, nơi khoảng trống bị che một phần bởi wick nhưng vẫn tồn tại imbalance về mặt body. Ở các thị trường/khung có ít gap rõ ràng, biết đọc implied FVG giúp không bỏ lỡ POI thật — nhưng cũng đòi hỏi kỷ luật cao hơn để không "tưởng tượng" ra FVG ở nơi không có. Đây là vùng cần backtest cá nhân để xác định nó có edge với instrument của mình hay không, thay vì áp dụng máy móc.

---

## 6. Best Practices

> [!success] Best Practices
> 1. Chạy đủ 6 điều kiện hợp lệ trước khi coi bất kỳ khoảng trống nào là POI — hình dạng không đủ.
> 2. Kiểm tra nến giữa là displacement thật (liên kết trực tiếp với việc chấm điểm displacement).
> 3. Chỉ vào FVG fresh; không entry lần hai vào một FVG đã bị lấp hết (fully mitigated).
> 4. Luôn xác định phía PD: bullish FVG chỉ mua ở Discount, bearish FVG chỉ bán ở Premium.
> 5. Đối chiếu FVG với bias HTF + draw on liquidity — loại các FVG counter-trend.
> 6. Entry quanh CE (50%), không tại rìa gần; dùng CE để đánh giá FVG còn hiệu lực hay không.
> 7. Nhận diện iFVG: nếu giá đã đóng cửa xuyên qua FVG, coi nó đã đổi vai trò, không giao dịch theo chiều cũ.
> 8. Ưu tiên confluence đa khung (FVG LTF nằm trong CE của FVG HTF cùng hướng); ghi `fvg_valid` + lý do loại vào log.

---

## 7. Rule phòng tránh & Checklist

- [ ] Không entry một FVG nếu chưa chạy qua đủ 6 điều kiện hợp lệ.
- [ ] Xác nhận nến giữa là displacement mạnh, không phải grinding.
- [ ] Chỉ vào FVG fresh; loại bỏ FVG đã lấp hết.
- [ ] Kiểm tra đúng phía PD (bullish→Discount, bearish→Premium).
- [ ] Đối chiếu cùng hướng bias HTF + draw on liquidity; loại FVG counter-trend.
- [ ] Xác nhận FVG được tạo bởi MSS/CISD, không phải khoảng trống ngẫu nhiên.
- [ ] Entry quanh CE, đặt SL dựa trên rìa xa/điểm sweep — không vào ở rìa gần.
- [ ] Nếu giá đã đóng cửa xuyên qua FVG, xử lý như iFVG (đổi chiều), không cố vào theo chiều cũ.

---

## 8. Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-26 XAUUSD Long]]
-

> [!info] Định dạng liên kết trade
> Khi thêm ví dụ thật, dùng đúng định dạng filename của vault: `[[Result - NN - Trade YYYY-MM-DD SYMBOL Position]]` (Result = Win/Loss/BE).

---

## 9. Flashcards / Active Recall

**Q1:** Vì sao "hình dạng FVG" chỉ là điều kiện cần, không đủ?
**A1:** Vì mọi chuyển động đều để lại vô số khoảng trống 3 nến, phần lớn vô nghĩa. Một FVG đáng vào phải *có bối cảnh*: sinh từ displacement mạnh, còn fresh, đúng phía PD, cùng hướng bias/draw HTF, có MSS/CISD chống lưng, và đủ dày để dùng CE.

**Q2:** Vì sao một FVG đã mitigate thường thất bại ở lần chạm thứ hai?
**A2:** FVG là nơi có lệnh tổ chức chưa khớp. Khi giá đã quay lại lấp nó lần đầu, các lệnh đó đã được thực thi ("hết đơn hàng"). Lần thứ hai không còn lực đỡ, giá xuyên thẳng qua và quét SL.

**Q3:** CE là gì và vì sao nên entry quanh CE thay vì tại rìa FVG?
**A3:** CE (Consequent Encroachment) là mức 50% của FVG — nơi lệnh tổ chức có mật độ cao nhất và là mốc đánh giá FVG còn hiệu lực. Entry tại rìa gần dễ bị dao động thông thường bên trong FVG quét; phản ứng thật thường quanh CE, cho SL chặt hơn và RR tốt hơn.

**Q4:** iFVG hình thành khi nào và ý nghĩa của nó?
**A4:** Khi giá đóng cửa xuyên qua một FVG theo hướng ngược, FVG đó thất bại và đảo vai trò thành Inverse FVG — hỗ trợ thành kháng cự (và ngược lại). Cố giao dịch theo chiều cũ của một FVG đã thành iFVG là một biến thể tinh vi của lỗi này.

**Q5:** Làm sao phân biệt FVG "có cấu trúc" với FVG "ngẫu nhiên"?
**A5:** Hỏi "FVG này được sinh ra bởi sự kiện gì?" FVG có cấu trúc được tạo bởi chính cú displacement gây ra MSS/CISD (đánh dấu order flow vừa đổi). FVG ngẫu nhiên hình thành giữa range/continuation không đáng kể, không đánh dấu sự kiện nào — không có lý do để giá tôn trọng.

**Q6:** Vì sao một bullish FVG ở Premium ngược bias HTF là bẫy?
**A6:** Nó thường chỉ là FVG counter-trend hình thành trong một pullback tăng của xu hướng giảm lớn hơn; mua ở Premium là mua đắt, và ngược draw on liquidity HTF. Giá pullback chạm FVG rồi tiếp tục theo bias giảm, quét SL.

---

## 10. Lesson Learned

FVG Not Valid là lỗi dạy rõ nhất một chân lý của ICT: **một khái niệm chỉ có giá trị trong đúng bối cảnh của nó.** FVG không phải là một tín hiệu tự thân — nó là một *dấu vết* của order flow, và dấu vết chỉ có ý nghĩa khi ta biết nó đến từ đâu (displacement thật hay yếu), ở đâu (Premium hay Discount), theo hướng nào (cùng hay ngược draw HTF), và còn nguyên hay đã cạn (fresh hay mitigated). Vào một FVG mà không hỏi những câu này là biến một công cụ đọc order flow thành một trò tô màu khoảng trống trên chart.

Về hành trình prop firm, FVG là mắt xích cuối trước khi bấm lệnh, nên chất lượng của nó quyết định trực tiếp SL có bị quét hay không. Kết hợp với việc sửa [[08 - Mistake - Weak Displacement]] (cái gốc) và [[06 - Mistake - Not Have Market Structure Shift]] (cái giữa), việc chỉ chọn FVG hợp lệ hoàn thiện một quy trình entry có bằng chứng từ đầu đến cuối — chính là loại nhất quán mà FTMO/The5ers đo lường.

Quy tắc cá nhân:
- [ ] Không entry một FVG nếu không trả lời được: sinh từ đâu, ở phía nào, theo hướng nào, còn fresh không.
- [ ] Entry quanh CE, không tại rìa; loại FVG đã lấp hết.
- [ ] Ghi `fvg_valid` + lý do loại để dữ liệu tự dạy mình nhóm FVG nào có edge.

> Một khoảng trống trên chart không phải là một cơ hội — nó là một câu hỏi. Chỉ khi cả sáu câu trả lời cùng "có", nó mới trở thành một điểm vào lệnh.

---

## 11. Liên kết

**Concepts:** [[13 - FVG  - Fair Value Gap]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[17 - Inverse Fair Value Gap - iFVG]] · [[14 - Implied Fair Value Gap]] · [[27 - Premium Discount]] · [[35 - Aggressive Displacement Entry]] · [[41 - Change in State of Delivery]] · [[21 - Liquidity Void]]

**Mistakes liên quan:** [[08 - Mistake - Weak Displacement]] · [[06 - Mistake - Not Have Market Structure Shift]] · [[02 - Mistake - Enter before liquidity sweep]]
