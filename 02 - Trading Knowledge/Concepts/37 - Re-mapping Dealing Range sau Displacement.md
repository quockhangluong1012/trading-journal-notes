---
type: ict-concept
concept: Re-mapping Dealing Range sau Displacement
aliases:
  - Re-mapping Dealing Range
  - Re-draw Dealing Range
  - Cập nhật Dealing Range sau displacement
  - Range Shift
tags:
  - trading/ict/concept
  - trading/study
  - "#DealingRange"
  - "#Displacement"
status: developing
category: Market Structure
last_reviewed: 2026-07-01
created: 2026-07-01
updated: 2026-07-03
common_mistakes:
  - "[[Mistake - Không re-map range sau displacement]]"
  - "[[Mistake - Wrong Dealing Range]]"
  - "[[Mistake - Thoát lệnh sớm]]"
---

# Re-mapping Dealing Range sau Displacement

> [!summary] Tóm tắt 1 câu
> **Sau mỗi nhịp displacement lấy external liquidity của range cũ, range cũ đã "chết" — mình phải VẼ LẠI dealing range trên swing mới (đáy mới → đỉnh mới) để đo lại premium/discount, phân loại lại internal/external liquidity và tìm POI tiếp theo; POI mới gần như luôn là FVG/OB do chính nhịp displacement để lại.**

> [!important] Nguyên tắc cốt lõi
> **POI không biến mất — nó đổi dạng.** Khi OB cũ đã mitigate và bạn "không thấy POI nào để theo dõi", nguyên nhân thường không phải hết cơ hội, mà là bạn vẫn đang nhìn vào **range cũ**. Displacement vừa rồi đã tạo ra một range mới và để lại PD array mới (FVG/OB) bên trong nó. Nhiệm vụ của bạn là re-map, không phải chờ đợi.

---

## 1. Định nghĩa

**Khái niệm:**  
Re-mapping Dealing Range là hành động **vẽ lại khung dealing range** sau khi một nhịp **displacement** (giãn nở mạnh, có động lượng, thường tạo FVG) đã **lấy external liquidity** ở một đầu range cũ hoặc tạo một swing point mới có ý nghĩa. Range cũ — vốn dùng để đo premium/discount và phân loại liquidity — không còn phản ánh cấu trúc hiện tại, nên mọi phép đo dựa trên nó trở nên sai. Re-mapping nghĩa là: xác định lại **swing high mới** và **swing low mới**, đo lại **equilibrium (50%)**, phân loại lại **internal vs external liquidity**, và từ đó **định vị POI tiếp theo**.

Đây là một **quy trình bảo trì range**, không phải một entry model. Nó là bước "cập nhật bản đồ" sau khi thị trường đã đi một quãng đường mới. Xem nền tảng ở [[12 - Dealing Range]].

**Mục đích trong ICT:**  
- **Giữ premium/discount luôn đúng thời sự:** sau displacement, giá có thể đã chuyển từ discount của range cũ sang một range hoàn toàn mới; nếu không re-map, bạn sẽ Long ở "discount" tưởng tượng trong khi thực chất đang ở premium của range mới.
- **Tái phân loại liquidity:** đỉnh vừa bị quét trở thành liquidity đã tiêu thụ; đáy mới / đỉnh mới trở thành external mới; các FVG/OB trong nhịp đẩy trở thành internal liquidity mới. Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]].
- **Tìm POI kế tiếp:** nhịp displacement tự sinh ra PD array (FVG, OB, breaker). POI tiếp theo là cái nằm trong **discount/equilibrium của range mới** và còn unmitigated.
- **Cập nhật draw on liquidity:** external nào vừa bị lấy, external nào còn mở → hướng hút tiếp theo của giá.

**Vì sao khái niệm này quan trọng:**  
Vì thị trường vận động theo chu kỳ **expansion → retracement → expansion**. Mỗi expansion (displacement) reset lại bối cảnh. Trader hay bị "kẹt" ở range cũ: họ chờ giá quay lại một OB đã mitigate, hoặc kết luận "hết setup", trong khi range mới đã hình thành ngay trước mắt với POI mới rõ ràng. Đây chính xác là tình huống "OB H1 đã mitigate, không thấy POI nào tiếp theo" — vấn đề nằm ở việc chưa re-map, chứ không phải hết cơ hội.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Range cũ còn hiệu lực không, hay displacement vừa rồi đã làm nó "chết"?
- Sau nhịp đẩy này, đâu là **swing high/low mới** tạo thành range hiện tại?
- Giá đang ở premium hay discount của **range MỚI** (không phải range cũ)?
- POI tiếp theo nằm ở đâu — FVG/OB nào trong nhịp displacement còn unmitigated?
- External liquidity nào vừa bị lấy, cái nào còn mở làm draw on liquidity?

### Re-mapping không phải là gì
- Không phải vẽ lại range mỗi khi giá nhích một chút; chỉ re-map khi có **displacement lấy external** hoặc tạo swing point có ý nghĩa.
- Không phải lý do để "dời cọc" cho khớp lệnh đang thua; re-map là đọc cấu trúc khách quan, không phải hợp lý hóa.
- Không phải chỉ đổi con số Fibonacci; nó bao gồm tái phân loại liquidity và xác định POI mới.
- Không phải tín hiệu vào lệnh; sau khi re-map xong, entry vẫn cần sweep + MSS + displacement trên LTF.

### Lý thuyết nested ranges (range lồng nhau / fractal range)

**Nguyên lý fractal:** Dealing range không tồn tại đơn lẻ trên một khung thời gian — nó luôn là một **mảnh vỡ (fractal)** của một range lớn hơn ở khung cao hơn. Một range M15 mới re-map luôn nằm **bên trong** một range H1 vẫn còn hiệu lực; range H1 đó lại nằm bên trong một range H4/D1 còn hiệu lực. Re-mapping ở LTF **không xóa** range HTF — nó chỉ cập nhật "lớp trong cùng" của một chồng range (stack) đang tồn tại song song trên nhiều khung. Đây là phần mở rộng trực tiếp của tư duy đa khung thời gian ở [[32 - Top-down Analysis (Multiple Timeframes)]].

> [!example] Mô hình "chồng range" (range stack)
> ```text
> D1 range   [chưa chết — external D1 chưa bị lấy]
>   └─ H4 range   [chưa chết — external H4 chưa bị lấy]
>        └─ H1 range   [VỪA CHẾT — re-map sau displacement]
>             └─ M15 range MỚI   [vừa vẽ lại, con của H1 mới]
> ```
> Khi H1 range chết và được re-map, H4 và D1 range **phía trên nó không nhất thiết đổi** — chúng chỉ đổi khi chính external của H4/D1 bị lấy. Re-map luôn diễn ra từ trong ra ngoài (LTF trước), hiếm khi buộc phải vẽ lại HTF.

**Cách giữ "ngăn xếp range" (range stack) trong đầu mà không bị rối:**
1. **Luôn neo theo thứ tự D1 → H4 → H1 → M15** khi review — không nhảy cóc khung.
2. Với mỗi khung, chỉ ghi 3 giá trị: **đáy, đỉnh, equilibrium**. Đây là "trạng thái" tối thiểu của một range.
3. Khi một range con (M15/H1) được re-map, **kiểm tra ngay** range cha (H4/D1) có còn chứa range con mới không — nếu range con mới đã "trồi" ra ngoài range cha (tức displacement đã đủ mạnh để lấy cả external cha), thì range cha cũng phải re-map theo tầng.
4. Dùng Quick Reference Card ở Appendix cho **từng tầng** riêng biệt trong Daily Note, đánh số tầng (D1/H4/H1/M15) để không lẫn lộn quy tắc "range nào đang chết, range nào vẫn sống".
5. Quy tắc vàng: **range con chết thường xuyên hơn range cha rất nhiều lần** — đừng hoảng khi phải re-map M15 nhiều lần trong một phiên, miễn range cha (H4/D1) vẫn nguyên vẹn thì bias tổng thể không đổi.

> [!info] Ví dụ minh họa — Nested Ranges Diagram
> ![[RemapRange-Nested-Ranges-Diagram.png]]
> **Chú thích cần vẽ (minh họa khái niệm, KHÔNG phải dữ liệu giao dịch thật):** một khung hình chữ nhật lớn nhãn "D1 Range (đáy–đỉnh)" bao ngoài; bên trong vẽ một hình chữ nhật nhỏ hơn nhãn "H1 Range (đáy–đỉnh, nằm trong discount D1)"; bên trong hình đó vẽ tiếp một hình nhỏ nhất nhãn "M15 Range mới sau displacement". Dùng 3 màu khác nhau cho 3 khung, mỗi khung ghi kèm equilibrium (đường 50% chấm) của chính nó, thể hiện rõ cả ba range tồn tại đồng thời, lồng vào nhau, không cái nào "xóa" cái nào.

---

## 2. Bối cảnh sử dụng

### Ba tình huống kích hoạt re-mapping

| Tình huống kích hoạt | Chuyện gì vừa xảy ra | Hành động re-map |
|---|---|---|
| **External của range cũ bị lấy** | Displacement đóng thân qua đỉnh/đáy range cũ và giữ acceptance | Range cũ chết; vẽ range mới lấy đỉnh/đáy vừa tạo |
| **Swing point mới có ý nghĩa hình thành** | Sau sweep + MSS + displacement, giá tạo đáy/đỉnh mới rõ ràng | Dùng đáy/đỉnh mới làm một đầu range mới |
| **Đã "ăn" xong một nhịp, cần tìm nhịp kế** | Bạn vừa đóng lệnh tại internal liquidity (như quét đỉnh cũ) | Re-map trên swing (đáy entry → đỉnh vừa quét) để tìm POI retrace tiếp |

> [!tip]
> Tình huống thứ ba chính là **case của bạn**: bạn Long từ discount, thoát ở 1.6R khi giá quét đỉnh cũ (một internal/minor BSL). Nhịp đi lên đó là một **displacement leg mới**. Re-map ngay trên swing "đáy bạn entry → đỉnh vừa quét" thì POI tiếp theo (FVG/OB của chính nhịp này) hiện ra lập tức.

### Khi nào khái niệm này có giá trị cao?
- [ ] Vừa có một nhịp **displacement rõ ràng** (nến thân dài, momentum, để lại FVG).
- [ ] Displacement đó **lấy external liquidity** (quét đỉnh/đáy cũ) hoặc tạo **swing point mới**.
- [ ] Bạn vừa đóng một lệnh và đang tìm cơ hội tiếp theo cùng hướng bias.
- [ ] Daily Bias / HTF narrative vẫn còn hiệu lực (draw on liquidity chính chưa hoàn tất).
- [ ] Có FVG/OB do nhịp displacement để lại, còn unmitigated, nằm ở discount/premium của range mới.

### Khi nào nên bỏ qua?
- [ ] Nhịp giá vừa rồi chỉ là **wiggle / micro move**, không phải displacement thật → chưa cần vẽ lại.
- [ ] External chính của HTF range đã bị lấy và **draw on liquidity đã hoàn tất** → không re-map để cố tìm entry cùng hướng, mà cân nhắc đảo bias.
- [ ] Giá đang ở **equilibrium của range mới** → có range mới nhưng không có location tốt, vẫn phải chờ.
- [ ] Re-map ra range nhưng **không có internal POI hợp lệ** → không có gì để theo dõi thật, đứng ngoài.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Một nhịp displacement mới:** chuỗi nến giãn nở cùng hướng, momentum rõ, thường để lại một hoặc nhiều FVG chưa được lấp.
2. **External cũ bị chạm/lấy:** displacement quét qua đỉnh (BSL) hoặc đáy (SSL) của range trước đó.
3. **Swing point mới:** một đỉnh mới (nếu đẩy lên) hoặc đáy mới (nếu đẩy xuống) đủ rõ để làm đầu range.
4. **PD array mới bên trong nhịp đẩy:** FVG, OB, hoặc breaker do displacement tạo ra → ứng viên POI.
5. **Range cũ hết vai trò:** premium/discount đo trên range cũ mâu thuẫn với hành vi giá hiện tại.

### Quy trình re-map 5 bước (làm theo thứ tự)

```text
1. XÁC NHẬN displacement thật (không phải wiggle) và nó đã lấy external nào.
2. VẼ range mới: chọn swing low mới và swing high mới có ý nghĩa làm hai đầu.
3. ĐO equilibrium (50%) của range mới → giá đang premium hay discount?
4. PHÂN LOẠI lại liquidity: external mới (hai đầu) + internal mới (FVG/OB trong nhịp đẩy).
5. CHỌN POI tiếp theo: internal PD array còn unmitigated ở đúng nửa range cho hướng bias.
```

### Điều kiện bắt buộc (để một lần re-map là hợp lệ)
- [ ] Có displacement thật, xác nhận bằng momentum + FVG (không phải nến do dự).
- [ ] Xác định rõ **hai đầu range mới** và ghi giá cụ thể của từng đầu.
- [ ] Đo và đánh dấu **equilibrium (50%)** của range mới.
- [ ] Xác định **external nào vừa bị lấy** và **external nào còn mở** (draw on liquidity).
- [ ] Liệt kê **internal POI** (FVG/OB) hợp lệ trong range mới.

### Điều kiện tăng xác suất (POI mới đáng theo dõi)
- [ ] POI mới trùng với **discount/equilibrium của range mới** cho lệnh Long (hoặc premium cho Short).
- [ ] POI mới **cộng hưởng** với một PD array HTF (ví dụ FVG H1 nằm trong discount của range D1).
- [ ] External phía draw on liquidity **vẫn còn mở** (còn room để giá chạy tới target).
- [ ] Nhịp displacement đủ mạnh để tạo FVG "sạch" (ít bị lấp một phần).
- [ ] Range mới nằm cùng hướng với [[12 - Daily Bias]].

### Điều kiện làm setup yếu đi
- Displacement yếu / mập mờ → range mới không đáng tin.
- Draw on liquidity chính đã hoàn tất → tìm entry cùng hướng là bơi ngược narrative.
- FVG/OB của nhịp đẩy đã bị lấp gần hết → POI cạn.
- Range mới quá nhỏ, không đủ room tới external → R:R kém.

> [!info] Ví dụ minh họa — 5-Step Re-map Process Visual
> ![[RemapRange-5Step-Process-Visual.png]]
> **Chú thích cần vẽ (minh họa quy trình, KHÔNG phải chart giao dịch thật):** một sơ đồ 5 ô theo chiều ngang hoặc dọc, đánh số 1→5, khớp đúng "Quy trình re-map 5 bước" ở trên: Ô 1 "Xác nhận displacement thật" (vẽ nến thân dài + FVG); Ô 2 "Vẽ range mới" (vẽ 2 đường ngang đáy/đỉnh mới); Ô 3 "Đo equilibrium" (vẽ đường 50% chấm giữa); Ô 4 "Phân loại lại liquidity" (đánh dấu external mới bằng mũi tên, internal mới bằng khung FVG/OB); Ô 5 "Chọn POI tiếp theo" (khoanh tròn FVG/OB còn unmitigated ở đúng nửa range). Dùng mũi tên nối tuần tự 1→2→3→4→5 để nhấn mạnh đây là quy trình có thứ tự, không được nhảy bước.

### Rủi ro hai đầu: Over-re-mapping vs Under-re-mapping

Re-mapping là một kỹ năng cần **hiệu chỉnh đúng tần suất** — sai ở cả hai phía đều tốn tiền, theo hai cách khác nhau.

| Thất bại | Biểu hiện | Hậu quả | Cách tự kiểm tra |
|---|---|---|---|
| **Over-re-mapping** (vẽ lại quá thường xuyên trên noise) | Redraw range mỗi khi có một nến thân vừa hoặc một wick nhỏ chạm quanh đỉnh/đáy; không phân biệt được displacement thật với dao động bình thường | Liên tục đổi bias, đổi POI; không đủ thời gian để một setup "chín"; giao dịch quá tay theo từng nến nhỏ; dễ bị nhiễu trên NQ1/NDX vì volatility cao | Hỏi: "Nến vừa rồi có FVG không, có đóng thân qua external cũ và giữ acceptance không?" Nếu không cả hai → chưa đủ điều kiện re-map |
| **Under-re-mapping** (bám range cũ đã chết) | Range đã bị displacement thật xuyên qua từ lâu nhưng vẫn tiếp tục đo premium/discount trên range cũ; chờ giá quay lại một OB đã mitigate | Bỏ lỡ toàn bộ chuỗi lệnh tiếp theo cùng narrative; đọc sai premium/discount → Long nhầm premium của range mới; "đóng băng" phân tích vì cố tìm POI không còn tồn tại | Hỏi: "External nào của range hiện tại tôi đang dùng đã bị lấy chưa? Nếu rồi, tại sao tôi chưa vẽ range mới?" |

> [!tip] Vùng an toàn ở giữa
> Điểm cân bằng đúng là: **chỉ re-map khi CẢ HAI** điều kiện xảy ra đồng thời — (1) có displacement thật xác nhận bằng momentum + FVG, VÀ (2) nó lấy external hoặc tạo swing point có ý nghĩa. Thiếu một trong hai → chưa re-map (tránh over); đủ cả hai mà vẫn không re-map → đang under.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] 4 câu hỏi bắt buộc sau mỗi nhịp displacement
> 1. **Displacement vừa rồi có lấy external của range cũ / tạo swing mới không?** (nếu có → range cũ chết)
> 2. **Hai đầu của range MỚI là đâu, equilibrium ở giá nào?**
> 3. **Giá đang premium hay discount của range MỚI?**
> 4. **POI tiếp theo (FVG/OB nào của nhịp đẩy) còn unmitigated và ở đúng nửa range?**

### D1 / H4 — Bias & Narrative có còn hiệu lực?
- **Kiểm tra draw on liquidity HTF:** external chính (ví dụ đường xanh trên = BSL lớn) đã bị lấy chưa? Chưa → bias giữ nguyên, có lý do tìm entry cùng hướng sau khi re-map. Rồi → cân nhắc đảo bias thay vì re-map để cố Long tiếp.
- **Range gốc HTF:** re-map ở LTF không được mâu thuẫn với range D1. Range mới của H1 lý tưởng nằm gọn trong discount (cho Long) của range D1.

### H1 / M15 — Vẽ lại range con & xác định POI mới
- **Vẽ range H1 mới:** đáy mới (đáy bạn vừa entry / đáy displacement) → đỉnh mới (đỉnh vừa bị quét). Đây là "swing mới" thay cho range đã dùng OB cũ.
- **POI mới = internal của range H1 mới:** thường là **FVG H1** do nhịp displacement đi lên để lại. Chọn cái gần discount/equilibrium nhất và còn unmitigated.
- **POI dự phòng:** breaker block (nếu có minor high bị phá trong nhịp đẩy) hoặc mitigation block; OB cũ đã mitigate xếp ưu tiên thấp nhất.
- **External mới của range con:** đỉnh vừa quét là BSL nội bộ đã tiêu thụ; external còn mở là mục tiêu tiếp (đỉnh cao hơn / HTF BSL).

### M5 / M1 — Chờ giá về POI mới rồi mới tìm entry
- **Không đuổi giá ở premium** của range mới. Chờ retrace về POI H1 đã đánh dấu.
- **Khi giá chạm POI:** xuống M5 chờ đúng chuỗi ICT 2022 — sweep liquidity nội bộ → **MSS + displacement + FVG M5** → entry tại 50% FVG M5 (giống hệt lệnh trước của bạn). Xem [[21 - Market Structure Shift]].
- **Quản lý lệnh lần này:** target external còn mở; **scale-out tại internal liquidity, giữ runner** — sửa lỗi thoát toàn bộ ở 1.6R.

> [!warning]
> Range M5 cục bộ chỉ dùng cho execution. Việc "giá đang discount" để quyết định Long/Short phải đo trên **range H1/D1 đã re-map**, không phải range M5.

### Khung quyết định nâng cao — "Consumed hoàn toàn" hay "Consumed một phần"?

Đây là **ca khó nhất** trong re-mapping: displacement vừa lấy một internal liquidity pool, nhưng pool đó lại nằm **rất gần** (hoặc trùng) với external HTF. Câu hỏi bắt buộc: range đã "vẽ xong" (draw complete, cân nhắc đảo bias) hay "mới lấy một phần" (còn room, re-map và đi tiếp)?

> [!example] Ba tiêu chí phân định — chấm điểm từng cái trước khi kết luận
> 1. **Khoảng cách tới external HTF thật:** internal vừa lấy có phải chính là external HTF (trùng giá, hoặc lệch dưới 10-15% biên độ range HTF) không? Nếu đúng → nghiêng về "fully consumed". Nếu internal đó chỉ là một minor high/low nằm giữa chừng, còn cách external HTF một khoảng đáng kể → nghiêng về "partially consumed".
> 2. **Cấu trúc HTF có break không?** Nếu nhịp displacement chỉ tạo BOS/MSS trên LTF (M15/H1) mà cấu trúc H4/D1 **chưa break** (chưa có higher high/lower low mới trên H4/D1) → range HTF vẫn nguyên, đây là "partially consumed", re-map con bên trong là đủ. Nếu displacement đủ mạnh để **break luôn cấu trúc H4/D1** → "fully consumed", phải re-map cả tầng cha, và cân nhắc nghiêm túc khả năng đảo bias.
> 3. **FVG HTF còn unmitigated không?** Nếu vẫn còn một FVG H4/D1 phía sau (chưa bị lấp) làm "lực hút ngược" hoặc làm điểm dừng hợp lý cho retracement → thị trường nhiều khả năng chưa "xong việc" ở phía đó, ủng hộ "partially consumed". Nếu FVG HTF đó đã bị lấp hoàn toàn trong đúng nhịp displacement này → giảm một điểm tựa quan trọng cho việc tiếp tục, nghiêng về "fully consumed".

| Tiêu chí | Nghiêng "Partially consumed" (re-map, đi tiếp) | Nghiêng "Fully consumed" (draw complete, cân nhắc đảo) |
|---|---|---|
| Khoảng cách internal vừa lấy → external HTF | Còn cách xa (>15-20% biên độ range HTF) | Trùng hoặc rất sát external HTF |
| Cấu trúc H4/D1 | Chưa break, chỉ break LTF | Đã break cùng lúc trên H4/D1 |
| FVG HTF phía sau | Còn unmitigated, chưa bị chạm | Đã bị lấp bởi chính nhịp displacement |
| Phản ứng giá tại vùng vừa quét | Tiếp tục momentum cùng hướng, đóng nến giữ acceptance | Wick dài, đảo chiều ngay, dấu hiệu turtle soup |
| Hành động đúng | Re-map range con, tìm POI mới, đi tiếp cùng bias | Re-map range cha, hạ độ ưu tiên bias cũ, tìm xác nhận đảo (sweep + MSS ngược) trước khi vào lệnh ngược |

> [!warning] Khi không chắc — mặc định thận trọng
> Nếu 3 tiêu chí trên cho tín hiệu trái chiều nhau (ví dụ: khoảng cách gần external nhưng cấu trúc H4 chưa break), **ưu tiên giả định "partially consumed" nhưng giảm size** — vẫn re-map và đi tiếp, nhưng không all-in vào giả thuyết tiếp diễn; đồng thời đặt cảnh báo theo dõi sát dấu hiệu đảo (sweep thất bại, MSS ngược trên LTF).

### Re-mapping theo đặc thù thị trường: NQ1/NDX vs EURUSD/GBPUSD/XAUUSD

Tần suất và cách re-map **không giống nhau** giữa các thị trường bạn giao dịch, vì volatility và nhịp độ phiên khác nhau đáng kể.

| Đặc điểm | NQ1 / NDX (NAS100) | EURUSD / GBPUSD / XAUUSD |
|---|---|---|
| Tần suất re-map trong 1 phiên | Cao — có thể re-map nhiều lần trong cùng London hoặc NY session do các nhịp displacement liên tiếp, volatility lớn, nhiều swing nhỏ có ý nghĩa | Thấp hơn — thường 1-2 lần re-map "đáng kể" mỗi ngày; range có xu hướng bền hơn giữa các phiên |
| Biên độ mỗi lần re-map | Range con thường nhỏ (theo điểm chỉ số) nhưng tỷ lệ % biến động lớn → dễ nhầm noise với displacement thật nếu không kiểm tra FVG rõ ràng | Range con thường lớn hơn về "thời gian hình thành", ít range giả; displacement rõ ràng hơn trên M15/H1 |
| Rủi ro chính | **Over-re-mapping**: đuổi theo từng nhịp giật do tin tức/thanh khoản mỏng đầu phiên NY; dễ đổi POI liên tục trong 15-30 phút | **Under-re-mapping**: giữ range cũ quá lâu vì thị trường "chậm", dễ bỏ lỡ khi một displacement hiếm hoi nhưng thật sự quan trọng xảy ra (đặc biệt quanh tin NFP/CPI với XAUUSD) |
| Khung nên dùng để xác nhận displacement trước khi re-map | Bắt buộc xác nhận trên M15/H1 (không re-map chỉ dựa trên M1/M5 noise) | Có thể tin tưởng M15/H1 ngay khi displacement xuất hiện, ít cần lọc thêm |
| Hướng dẫn thực hành | Giới hạn số lần re-map thực sự ảnh hưởng đến quyết định vào lệnh — tối đa theo dõi 2-3 tầng range (H1 → M15 → M5) mỗi phiên; bỏ qua các "giả displacement" trên M1 | Khi một displacement H1/H4 thật xuất hiện (hiếm hơn), re-map ngay lập tức và nghiêm túc theo hết chuỗi lệnh — đây thường là narrative chính trong ngày, không phải noise |

> [!tip] Quy tắc thực dụng cho tài khoản của bạn
> Với **NQ1/NDX**: chỉ tăng mức độ tin cậy của một re-map khi displacement đóng thân rõ ràng qua external trên **H1** (không phải M5), vì volatility cao khiến M5 sinh ra rất nhiều "range giả". Với **EURUSD/GBPUSD/XAUUSD**: đừng chờ quá lâu để xác nhận — một displacement H1 thật trên các cặp này thường là toàn bộ cơ hội trong ngày, chậm re-map đồng nghĩa bỏ lỡ cả chuỗi lệnh.

> [!info] Ví dụ minh họa — Displacement (tạo range mới) vs Pullback (không tạo range mới)
> ![[RemapRange-Displacement-vs-Pullback-Comparison.png]]
> **Chú thích cần vẽ (so sánh khái niệm cạnh nhau, KHÔNG phải chart giao dịch thật):** chia đôi hình theo chiều dọc. Bên trái nhãn "DISPLACEMENT — tạo range mới": vẽ 2-3 nến thân dài liên tiếp cùng hướng, để lại một FVG rõ ràng, đóng thân qua đường external cũ (nét đứt) và giữ giá ở bên ngoài (acceptance) — ghi chú "Re-map required". Bên phải nhãn "PULLBACK — không tạo range mới": vẽ các nến thân nhỏ, nhiều wick, dao động qua lại quanh một vùng, không chạm external, không để lại FVG đáng kể — ghi chú "Giữ nguyên range cũ, không re-map". Dùng cùng trục giá để người xem so sánh trực quan biên độ và "chất lượng" của hai loại nhịp.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Re-map được xem là hợp lệ khi
- [ ] Có displacement thật đã lấy external cũ hoặc tạo swing mới có ý nghĩa.
- [ ] Hai đầu range mới rõ ràng, tạo bởi displacement/BOS, ghi được giá.
- [ ] Equilibrium mới được đo và giá có location rõ (premium hoặc discount).
- [ ] Có internal POI hợp lệ, còn unmitigated, đúng nửa range cho hướng bias.
- [ ] Range mới không mâu thuẫn với HTF range/bias.

### KHÔNG re-map (hoặc re-map là sai) khi
- [ ] Nhịp giá chỉ là retracement/wiggle, chưa phải displacement → range cũ vẫn sống.
- [ ] Bạn vẽ lại range chỉ để "cứu" một lệnh đang thua (bias confirmation).
- [ ] External chính HTF đã bị lấy, draw hoàn tất → nên đảo bias, không re-map cùng hướng.
- [ ] Sau re-map giá ở equilibrium hoặc không có POI → có range nhưng không có lệnh.

### Phân biệt "displacement tạo range mới" vs "chỉ là pullback trong range cũ"

| Quan sát | Cách đọc hợp lý |
|---|---|
| Nến thân dài, momentum, để lại FVG, đóng qua external cũ và giữ acceptance | **Displacement thật** → range cũ chết, re-map |
| Giá nhích lên nhưng thân nến nhỏ, nhiều wick, không lấy external, không FVG | **Chỉ pullback** → giữ range cũ, chưa re-map |
| Giá wick qua external rồi đóng ngược lại vào range + displacement ngược | **Sweep external** (turtle soup) → có thể đảo; re-map theo hướng đảo nếu MSS xác nhận |
| Giá lấy external một đầu rồi tạo BOS cùng hướng, swing mới rõ | **Range dịch chuyển** → re-map, hai đầu mới, đo lại premium/discount |

---

## 6. Ví dụ chart

### Ví dụ đúng — Re-map sau khi Long chạm internal liquidity, tìm được FVG H1 làm POI tiếp
![[RemapRange-Example-Correct-NewPOIFound.png]]

**Mô tả:**  
Range cũ: đáy đã sweep SSL → OB H1 ở discount. Trader Long tại FVG M5 trong OB đó, giá displacement đi lên và **quét một đỉnh cũ (internal BSL)** — trader thoát 1.6R. Thay vì kết luận "hết POI vì OB đã mitigate", trader **re-map**: vẽ range mới từ **đáy vừa entry → đỉnh vừa quét**, đo equilibrium. Nhịp đẩy lên để lại một **FVG H1** nằm ở discount của range mới, còn unmitigated. Đó là POI tiếp theo. Trader chờ giá retrace về FVG H1, xuống M5 chờ MSS + displacement + FVG M5, vào Long tiếp, target là external BSL còn mở (đỉnh cao hơn / đường xanh trên).

**Vì sao đây là ví dụ tốt:**
- OB cũ mitigate không có nghĩa hết cơ hội — nhịp displacement tự tạo POI mới (FVG H1).
- Premium/discount được đo lại trên **range mới**, nên location vẫn đúng để Long tiếp.
- Draw on liquidity (external BSL) vẫn còn mở → có lý do và có room cho lệnh tiếp theo.
- Luồng internal → external được nối tiếp mạch lạc thay vì "chờ trong vô định".

### Ví dụ sai / dễ nhầm — không re-map, cố chờ OB cũ hoặc Long ở premium range mới
![[RemapRange-Example-Wrong-StuckOnOldOB.png]]

**Mô tả lỗi:**  
Sau khi thoát lệnh, trader vẫn dán mắt vào OB H1 cũ (đã mitigate) và chờ giá quay lại đó — nhưng giá không về, trader bỏ lỡ nhịp tiếp theo. Hoặc tệ hơn: trader thấy giá đang đi lên, nhảy vào Long ngay mà không re-map, hóa ra giá đang ở **premium của range mới**, sát BSL sắp bị quét → giá đảo, lệnh thua.

**Bài học:**
- **POI đổi dạng sau displacement** — đừng chờ POI cũ đã tiêu thụ.
- Trước khi vào lệnh tiếp, **luôn re-map và đo lại premium/discount trên range mới**; đừng Long ở premium vì tưởng còn ở discount range cũ.
- Đây là mặt còn lại của [[12 - Dealing Range]]: chọn/giữ sai range → mua premium tưởng discount.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[12 - Dealing Range]]
- [[27 - Premium Discount]]
- [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[13 - FVG  - Fair Value Gap]]
- [[25 - OB - Order Block]]
- [[04 - Breaker Block]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[26 - OTE - Optimal Trade Entry]]
- [[12 - Daily Bias]]
- [[32 - Top-down Analysis (Multiple Timeframes)]]
- [[35 - Aggressive Displacement Entry]]

### Sequence mẫu — Re-map để tìm nhịp Long thứ hai
```text
Đã Long nhịp 1 từ discount range cũ → giá displacement lên, quét internal BSL (đỉnh cũ) → thoát/scale-out
→ RE-MAP: vẽ range mới [đáy entry → đỉnh vừa quét], đo equilibrium
→ Phân loại lại: external cũ (SSL đáy) đã tiêu thụ; internal MỚI = FVG/OB của nhịp đẩy
→ Chọn POI: FVG H1 trong discount range mới, còn unmitigated
→ Chờ giá retrace về POI (không đuổi ở premium)
→ M5: sweep nội bộ → MSS + Displacement + FVG M5 → entry 50% FVG
→ Stop dưới POI/swing low; Target: external BSL còn mở
→ Scale-out ở internal, giữ runner tới external (sửa lỗi thoát non 1.6R)
→ Re-map lại khi external tiếp theo bị lấy
```

> [!note]
> Re-mapping là cách biến một lệnh đơn lẻ thành **chuỗi lệnh cùng một narrative**: mỗi displacement lấy một tầng liquidity, để lại một POI mới cho nhịp sau, cho tới khi draw on liquidity HTF hoàn tất. Đây là tư duy "trading the delivery" thay vì "một lệnh rồi hết".

---

## Best Practices

> [!summary] Tinh thần của mục này
> Biết quy trình re-map (mục 3-4) là điều kiện cần; **biến nó thành thói quen kỷ luật, nhất quán** mới là điều kiện đủ để nó tạo ra edge thật trên tài khoản. Đây là những thói quen phân biệt trader chuyên nghiệp với người mới biết khái niệm.

### 1. Re-map NGAY khi xác nhận displacement thật — đừng chờ

Ngay khi nến đóng thân xác nhận displacement (momentum + FVG + lấy external/tạo swing mới), **vẽ range mới trong vòng vài giây**, không đợi thêm nến xác nhận, không đợi "chắc chắn hơn".

> [!warning] Cái giá của re-map trễ
> Re-mapping trễ (chờ thêm 2-3 nến để "chắc ăn") thường khiến bạn **bỏ lỡ chính nhịp continuation** mà range mới vừa mở ra — giá đã chạy qua POI mới (FVG/OB của nhịp đẩy) trước khi bạn kịp đánh dấu nó. Hậu quả điển hình: bạn nhận ra POI mới *sau khi* giá đã rời khỏi đó, và phải chờ một chu kỳ displacement khác. Trong ICT 2022 Model, cửa sổ giữa lúc POI mới hình thành và lúc giá quay lại lấp nó thường rất hẹp — chậm một nhịp là mất một entry.

### 2. Giữ một log/screenshot đơn giản cho mỗi lần re-map trong phiên

Mỗi khi re-map, chụp nhanh 1 ảnh màn hình (hoặc ghi 1 dòng vào Quick Reference Card ở Appendix) với tối thiểu: giờ, hai đầu range mới, POI được chọn. Cuối phiên/cuối ngày, xâu chuỗi lại các log này theo thứ tự thời gian.

> [!tip] Vì sao việc này quan trọng
> Một chuỗi log re-map theo thời gian biến một phiên giao dịch rời rạc thành **một câu chuyện có thể review**: bạn thấy rõ narrative đã "consumed" bao nhiêu tầng liquidity, ở đâu range bị đọc sai, ở đâu bạn re-map đúng nhưng vào lệnh sai thời điểm. Không có log này, review cuối ngày chỉ dựa vào trí nhớ — dễ bóp méo theo hướng có lợi cho cái tôi (hindsight bias).

### 3. Tự kiểm tra để tránh bẫy "re-map để hợp lý hóa lệnh thua"

Đây là lỗi nghiêm trọng nhất liên quan đến re-mapping (xem thêm mục 10). Trước khi vẽ lại bất kỳ range nào **trong lúc đang có một lệnh mở đang lỗ**, bắt buộc tự hỏi:

> [!question] Câu hỏi tự kiểm tra bắt buộc
> **"Nếu tôi KHÔNG có lệnh nào đang mở lúc này, tôi có vẽ range y hệt thế này không?"**
> - Nếu câu trả lời là **Có** (bạn sẽ vẽ giống vậy dù không có lệnh nào bị ảnh hưởng) → re-map hợp lệ, cứ tiếp tục.
> - Nếu câu trả lời là **Không / Không chắc** (bạn đang cố nắn range để đường equilibrium/POI trùng khớp với vị thế đang có) → đây là bias confirmation, dừng lại, không re-map, chấp nhận đọc cấu trúc khách quan kể cả khi nó xác nhận lệnh đang thua.

### 4. Re-mapping phải dẫn dắt scale-out & giữ runner, không chỉ dẫn dắt entry

Mỗi lần re-map không chỉ tìm POI vào lệnh mới — nó còn định nghĩa lại **các mốc internal/external tiếp theo để quản lý lệnh đang chạy**:
- Khi giá tiến tới **internal liquidity mới** (được xác định lại sau re-map gần nhất) → đây là điểm hợp lý để **chốt một phần (scale-out)**, đúng như bài học ở mục 6 (sửa lỗi thoát toàn bộ ở 1.6R).
- Phần **runner còn lại** nên được giữ tới **external mới** của range vừa re-map — không phải external của range cũ (đã tiêu thụ) và cũng không chốt cảm tính giữa chừng.
- Mỗi khi một external mới bị lấy, đó vừa là tín hiệu chốt thêm một phần, vừa là tín hiệu **re-map lần kế tiếp** — hai hành động luôn đi cùng nhau, không tách rời.

### 5. Bảng đối chiếu: Thói quen nghiệp dư vs Thói quen chuyên nghiệp

| Tình huống | Thói quen nghiệp dư | Thói quen chuyên nghiệp |
|---|---|---|
| Vừa xác nhận displacement thật | Ghi nhận trong đầu, "để lát nữa vẽ lại" | Vẽ range mới ngay lập tức, ghi giá hai đầu trước khi làm gì khác |
| Đang có lệnh mở đang lỗ | Vẽ lại range sao cho entry "trông như" đang ở discount/premium đúng | Tự hỏi "nếu không có lệnh, tôi có vẽ vậy không?" — giữ range khách quan dù bất lợi cho lệnh hiện tại |
| OB/POI cũ đã mitigate | Kết luận "hết setup", đứng ngoài chờ giá quay lại chỗ cũ | Re-map ngay, tìm POI mới (FVG/OB của nhịp đẩy) trong range vừa vẽ lại |
| Giá chạm internal liquidity mới | Thoát toàn bộ vị thế vì "ăn chắc", hoặc ngược lại tham lam không chốt gì cả | Scale-out một phần tại internal, dời stop hợp lý, giữ runner tới external mới |
| Review cuối ngày | Nhớ lại đại khái "hôm nay có re-map vài lần" | Có log/screenshot từng lần re-map theo thời gian, đối chiếu được narrative đã đi đúng hay sai ở đâu |
| Nhịp giá nhỏ, nhiều wick xuất hiện | Vẽ lại range theo mỗi dao động nhỏ (over-re-mapping) | Kiểm tra đủ điều kiện (momentum + FVG + lấy external/swing mới) trước khi re-map |
| External HTF đã bị lấy, draw hoàn tất | Cố re-map liên tục để tìm lệnh cùng hướng cũ | Dừng tìm lệnh cùng hướng, đánh giá nghiêm túc khả năng đảo bias |

---

## 9. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Re-map cho bạn range và POI mới — nhưng có range chưa phải có lệnh. Vẫn cần location đúng + POI hợp lệ + xác nhận LTF.

### A. Trigger & Context
- [ ] Nhịp vừa rồi là **displacement thật** (momentum + FVG), không phải wiggle.
- [ ] Nó đã **lấy external cũ / tạo swing mới** → range cũ hết hiệu lực.
- [ ] HTF bias & draw on liquidity chính **vẫn còn hiệu lực** (external chính chưa bị lấy).

### B. Re-map (vẽ lại khung)
- [ ] Đã vẽ **range mới**, ghi giá hai đầu.
- [ ] Đã đo **equilibrium (50%)**; biết giá đang premium hay discount range mới.
- [ ] Đã phân loại **external mới** (đầu nào còn mở = draw) và **internal mới** (FVG/OB).
- [ ] Đã chọn **POI tiếp theo** ở đúng nửa range, còn unmitigated.

### C. Execution (khi giá về POI)
- [ ] Giá đã retrace về POI (không đuổi ở premium/equilibrium).
- [ ] Có sweep + MSS + displacement + FVG trên M5 trong POI.
- [ ] Entry có stop logic (dưới POI/swing).
- [ ] Target là external còn mở; có kế hoạch **scale-out + giữ runner**.
- [ ] R:R đạt kế hoạch; range mới đủ room tới external.

### D. Quy tắc "không có lệnh"
- [ ] Chỉ là pullback, chưa displacement → không re-map, không lệnh.
- [ ] Draw HTF đã hoàn tất → không cố Long cùng hướng; xét đảo bias.
- [ ] Sau re-map giá ở equilibrium / không có POI → chờ.
- [ ] Đang muốn re-map để hợp lý hóa một lệnh thua → dừng, đây là bias.

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Không re-map sau displacement | "OB đã mitigate, hết POI để theo dõi" | Vẽ range mới trên swing mới; POI = FVG/OB của nhịp đẩy |
| Chờ POI đã tiêu thụ | Ngồi đợi giá quay lại OB cũ đã mitigate | POI đổi dạng; chuyển sang internal PD array mới |
| Long ở premium range mới | Nhảy vào theo momentum, không đo lại location | Re-map + đo equilibrium trước; chỉ Long ở discount |
| Re-map để cứu lệnh thua | Vẽ lại range cho khớp lệnh đang lỗ | Re-map là đọc cấu trúc khách quan, không phải hợp lý hóa |
| Re-map khi mới chỉ pullback | Vẽ range mới sau một nhịp hồi nhỏ | Chỉ re-map khi có displacement thật (momentum + FVG) |
| Bỏ qua draw HTF đã xong | Cố tìm Long tiếp sau khi BSL lớn đã bị lấy | Kiểm tra external HTF; nếu draw xong → xét đảo bias |
| Thoát non không giữ runner | Đóng toàn bộ ở internal liquidity (như 1.6R) | Scale-out ở internal, giữ runner tới external mới |

---

## 11. Câu hỏi tự kiểm tra

- Nhịp vừa rồi là displacement thật hay chỉ pullback?
- Displacement đó đã lấy external nào, tạo swing mới ở đâu?
- Hai đầu range MỚI là gì, equilibrium ở giá nào?
- Giá đang premium hay discount của range mới?
- POI tiếp theo là FVG/OB nào của nhịp đẩy, còn unmitigated không?
- External nào vừa tiêu thụ, external nào còn mở làm draw?
- Draw on liquidity HTF còn hiệu lực không, hay tôi nên đảo bias?
- Tôi đang re-map để đọc thị trường, hay để cứu một lệnh thua?

---

## 12. Flashcards / Active Recall

### Q1
**Hỏi:** Re-mapping Dealing Range là gì?  
**Đáp:** Vẽ lại khung dealing range sau khi displacement lấy external cũ / tạo swing mới, để đo lại premium/discount, phân loại lại internal-external liquidity và tìm POI tiếp theo. Là quy trình bảo trì range, không phải entry model.

### Q2
**Hỏi:** Khi nào phải re-map?  
**Đáp:** Khi có displacement thật (momentum + FVG) đã lấy external của range cũ hoặc tạo một swing point mới có ý nghĩa; hoặc khi vừa đóng một nhịp và cần tìm nhịp kế cùng hướng bias.

### Q3
**Hỏi:** "OB đã mitigate, không còn POI" — sai ở đâu?  
**Đáp:** POI không biến mất mà đổi dạng. Nhịp displacement để lại FVG/OB mới. Vẫn đang nhìn range cũ nên không thấy; re-map thì POI mới (FVG H1 trong discount range mới) hiện ra.

### Q4
**Hỏi:** Điều kiện quan trọng nhất để re-map hợp lệ?  
**Đáp:** Phải có displacement THẬT (không phải pullback/wiggle) và nó đã lấy external / tạo swing mới; đồng thời HTF bias & draw còn hiệu lực.

### Q5
**Hỏi:** Sau re-map, POI tiếp theo thường là gì?  
**Đáp:** FVG (hoặc OB/breaker) do nhịp displacement tạo ra, nằm ở discount/equilibrium của range mới và còn unmitigated.

### Q6
**Hỏi:** Khi nào KHÔNG nên re-map để tìm lệnh cùng hướng?  
**Đáp:** Khi external chính của HTF đã bị lấy và draw on liquidity đã hoàn tất — lúc đó nên xét đảo bias, không cố Long/Short cùng hướng cũ.

---

## 13. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, mistakes
FROM ""
WHERE contains(string(mistakes), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault dùng path riêng cho trades, thay `FROM ""` bằng `FROM "05 - Live Trading Journal/Trades"`.

---

## 14. Lesson Learned

### Bài học chính
- **POI không biến mất, nó đổi dạng.** OB mitigate ≠ hết cơ hội; displacement tạo POI mới.
- Sau mỗi displacement, range cũ **chết** — premium/discount phải đo lại trên range mới trước khi nghĩ tới entry.
- Re-mapping biến một lệnh đơn lẻ thành **chuỗi lệnh cùng narrative** cho tới khi draw HTF hoàn tất.
- Re-map là đọc cấu trúc **khách quan**, tuyệt đối không dùng để hợp lý hóa một lệnh đang thua.
- Kết hợp re-map với **scale-out + runner**: mỗi tầng liquidity là một chốt một phần, không thoát toàn bộ ở internal.

### Quy tắc cá nhân rút ra
- [ ] Mỗi khi đóng một nhịp, tôi re-map range mới trước khi kết luận "hết POI".
- [ ] Tôi chỉ re-map khi có displacement thật, không re-map sau pullback.
- [ ] Tôi luôn đo lại equilibrium range mới trước khi vào lệnh tiếp — không Long ở premium.
- [ ] Nếu draw HTF đã hoàn tất, tôi xét đảo bias thay vì cố tìm lệnh cùng hướng.

### Câu nhắc nhở khi trade
> **"OB cũ mitigate rồi thì vẽ lại range — POI không mất, nó chỉ chuyển sang cái FVG mà cú displacement vừa để lại."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt re-map với chọn range ban đầu không? |
| Nhận diện trên chart |  | Có phân biệt displacement thật vs pullback để quyết định re-map không? |
| Biết khi nào bỏ qua |  | Có nhận ra khi draw HTF đã xong nên đảo bias thay vì re-map không? |
| Kết hợp với context HTF |  | Range mới có nằm trong discount/premium của HTF range không? |
| Áp dụng vào trade thực tế |  | Có tìm được POI tiếp theo và giữ runner tới external không? |

**Kế hoạch review tiếp theo:**  
- [ ] Đối chiếu lại lệnh EURUSD/NAS100 gần nhất: sau khi thoát 1.6R, POI tiếp theo (FVG H1) nằm ở đâu?
- [ ] Backtest 20–30 setup có nhịp displacement lấy internal liquidity → thống kê xác suất nhịp tiếp theo tới external.
- [ ] So sánh R trung bình khi thoát toàn bộ ở internal vs scale-out + runner tới external.
