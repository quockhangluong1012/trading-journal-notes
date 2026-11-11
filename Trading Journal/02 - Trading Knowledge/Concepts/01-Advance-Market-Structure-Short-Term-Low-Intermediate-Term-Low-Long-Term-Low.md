---
type: ict-concept
concept: Advance Market Structure
aliases:
  - Advance Market Structure
  - Advanced Market Structure
  - Fractal Market Structure
  - STL
  - STH
  - ITL
  - ITH
  - LTL
  - LTH
  - Short Term Low
  - Intermediate Term Low
  - Long Term Low
tags:
  - trading/ict/concept
  - trading/study
  - trading/deep-dive
  - "#MarketStructure"
status: developing
category: Market Structure
timeframes:
  - D1
  - H1
  - M5
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
version: v2
last_reviewed: 2026-11-10
created: 2026-06-23
updated: 2026-11-10
prerequisites:
  - "[[19-Liquidity]]"
  - "[[05-BOS-Break-of-Structure]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[12-Dealing-Range]]"
  - "[[32-Top-down-Analysis-Multiple-Timeframes]]"
common_mistakes:
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]"
---

# Advanced Market Structure — STL · ITL · LTL (và STH · ITH · LTH) — Deep Dive · v2

> [!summary] Tóm tắt 1 câu
> **Mọi cái đáy trên chart đều bắt đầu là một đáy nhỏ (STL). Đáy nhỏ nào thấp hơn hai đáy nhỏ đứng cạnh nó thì được gọi thêm là đáy vừa (ITL). Đáy vừa nào thấp hơn hai đáy vừa đứng cạnh nó thì được gọi thêm là đáy lớn (LTL). Đó là một cách XẾP HẠNG vị trí. Nó giúp ta biết đáy nào đáng nhìn — nó không tự nói đáy đó sẽ giữ, cũng không tự nói xu hướng đã đổi.**

> [!important] Sáu nguyên tắc cốt lõi của bản v2
> 1. **Một viên gạch duy nhất.** STL là viên gạch. ITL và LTL không phải thứ gì khác — chúng là STL được "lên cấp".
> 2. **Lên cấp là so với hàng xóm CÙNG CẤP ở HAI BÊN.** Không phải do rơi sâu bao nhiêu, không phải do mất bao lâu.
> 3. **Năm chuyện khác nhau:** hình thành ≠ xác nhận ≠ phân loại ≠ thứ bậc ≠ ý nghĩa cấu trúc.
> 4. **Cấp càng cao, biết càng muộn.** Mép phải của chart luôn chỉ là "ứng viên".
> 5. **Cấp độ ≠ protected ≠ liquidity ≠ đảo chiều.** Bốn câu hỏi riêng.
> 6. **Phá cấp nào, kết luận cấp đó — và luôn kèm tên khung** (D1-ITL, H1-STL, M5-STH…).

> [!warning] Thay đổi so với bản v1 (2026-07-28)
> Bản v1 trình bày vài điều như sự thật trong khi chúng là giả thuyết (ví dụ "đáy càng nhiều lớp mũ thì stop loss dồn bên dưới càng nhiều", "LTL là đáy của một range lớn"). Bản v1 cũng có các "case study" và "war story" mang tên thị trường thật nhưng không gắn với dữ liệu kiểm chứng được. Bản v2 **giữ nguyên luật phân loại**, nhưng tách rõ sự thật / quy ước ICT / diễn giải / giả thuyết, thêm trạng thái "ứng viên", và chỉ dùng **ví dụ dựng** có ghi rõ là ví dụ dựng. Chi tiết ở mục 29 (Nhật ký phiên bản luật). Bản v1 được lưu ở `attachments/_backup/`.

> [!note] Cách đọc note này
> - Mỗi ý lớn đi theo thứ tự: **nói đơn giản → ví dụ đời thường → chuỗi giá → định nghĩa kỹ thuật → ý nghĩa cấu trúc → trường hợp khó.**
> - Nhãn dùng xuyên suốt: **[MARKET MECHANICS]** = quan sát/cơ chế thị trường; **[ICT FRAMEWORK]** = định nghĩa, cách gọi tên của ICT; **[INTERPRETATION]** = diễn giải hợp lý nhưng không chứng minh được từ nến; **[HYPOTHESIS]** = giả thuyết cần kiểm chứng; **[BACKTEST REQUIRED]**.
> - Mọi chart trong note là **ví dụ dựng bằng tay** để minh họa luật. Nhãn STL/ITL/LTL trong hình được **máy tính tự chấm theo đúng luật**, không chấm bằng mắt.
> - Note cố ý dùng rất ít con số. Khi cần, giá được gọi bằng "bậc" (bậc 30 thấp hơn bậc 40) hoặc bằng chữ cái (đáy a, đáy b…).

---

## 1. Executive Summary

**Câu hỏi cốt lõi 1 — Vì sao thị trường có nhiều cấp độ swing?**
Vì giá không đi thẳng. Nó đi lên rồi lùi, lùi rồi lên, và các lần lên–lùi đó có **nhiều cỡ khác nhau chồng lên nhau**: gợn nhỏ nằm trên con sóng, con sóng nằm trên thủy triều. Bất kỳ đường gấp khúc nào cũng có "đáy của các đáy". Việc chia ba cấp STL/ITL/LTL là cách đặt tên cho ba cỡ đó. **[MARKET MECHANICS]** cho phần "giá gấp khúc ở mọi cỡ"; **[ICT FRAMEWORK]** cho phần đặt tên.

**Câu hỏi cốt lõi 2 — Điều gì khiến một swing low quan trọng hơn swing low khác?**
Có **hai** câu trả lời, và phải tách chúng ra:

- Theo **vị trí** (luật phân loại): đáy đó thấp hơn bao nhiêu **lớp** hàng xóm. Thấp hơn hàng xóm nhỏ → ITL. Thấp hơn cả hàng xóm vừa → LTL. Đây là quy ước, rõ ràng, lập trình được.
- Theo **việc nó đã làm** (ý nghĩa cấu trúc): cú đi lên từ đáy đó có phá được đỉnh nào không, có phải nơi cả một nhịp tăng bắt đầu không, giá có còn ở trên nó không. Đây là phần diễn giải.

Một đáy có cấp cao **thường** cũng là đáy đã làm được việc lớn — nhưng **không phải lúc nào cũng vậy**. Nhầm hai thứ này là nguồn gốc của phần lớn lỗi đọc cấu trúc.

**Ba định nghĩa (luật chính của note):** **[ICT FRAMEWORK]**

| Tên | Nói đơn giản | Luật |
|---|---|---|
| **STL** — Short-Term Low | Đáy nhỏ | Một cây nến có đáy thấp nhất; cây bên trái và cây bên phải đều có đáy cao hơn |
| **ITL** — Intermediate-Term Low | Đáy vừa | Một STL mà STL bên trái và STL bên phải đều cao hơn nó |
| **LTL** — Long-Term Low | Đáy lớn | Một ITL mà ITL bên trái và ITL bên phải đều cao hơn nó |
| **STH / ITH / LTH** | Đỉnh nhỏ / vừa / lớn | Y hệt, đổi "thấp hơn" thành "cao hơn" |

**Ba điều bản v2 muốn bạn mang đi:**

1. Nhãn cấp độ là **bản đồ**, không phải **tín hiệu**. Khi một LTL được xác nhận, giá thường đã đi xa.
2. Trong real-time, phần bên phải chart luôn thiếu hàng xóm. Hãy quen miệng với chữ **"ứng viên"**.
3. "Đáy cấp cao có nhiều liquidity hơn / khó vỡ hơn" là **giả thuyết hợp lý**, chưa phải sự thật. **[HYPOTHESIS]**

> [!caution] Một điểm cần sửa ngay trong đề bài nghiên cứu
> Đề bài viết: *"Short-Term Low là một swing low có các swing low cao hơn ở hai bên."* Câu này **trộn hai cấp**. Nếu "swing low" đã là đáy ba-nến, thì "swing low có swing low cao hơn hai bên" chính là định nghĩa của **ITL**, không phải STL. STL là cấp thấp nhất: nó được định nghĩa bằng **nến** hai bên, không phải bằng **swing** hai bên. Giữ đúng điểm này thì cả hệ thống mới khớp.

---

## 2. Mental Model của Advanced Market Structure

### 2.1 Nói đơn giản

Hãy quên chart đi một lúc.

Một em bé đi bộ trên con đường đất sau cơn mưa. Trên đường có rất nhiều **cái hố**. Có hố nông, có hố sâu. Em bé muốn biết: **hố nào là hố "to" nhất?**

Em không có thước. Em chỉ biết làm một việc: **đứng ở một cái hố và nhìn sang hai hố bên cạnh.**

### 2.2 Ví dụ cho trẻ 5 tuổi — Trò chơi "hố nào sâu nhất"

![[AMS-v2-01-Tro-Choi-Ho-Sau-Nhat.svg|960]]
*Hình AMS-v2-01 — Tám cái hố (a đến h). Ba vòng thi. Mỗi vòng chỉ so một hố với hai hố đứng ngay cạnh nó trong vòng đó.*

- **Vòng 1 — hố nhỏ.** Cái hố nào em gặp cũng được vào vòng 1. Tất cả đều là "hố nhỏ". Có tám hố: a, b, c, d, e, f, g, h.
- **Vòng 2 — hố vừa.** Luật: *hố nào sâu hơn CẢ HAI hố bên cạnh thì thắng.* Hố b sâu hơn a và c → thắng. Hố e sâu hơn d và f → thắng. Hố g sâu hơn f và h → thắng. Hố d khá sâu, nhưng bên cạnh nó là e còn sâu hơn → d thua.
- **Vòng 3 — hố lớn.** Bây giờ chỉ còn ba hố thắng vòng 2 đứng cạnh nhau: b, e, g. Luật vẫn thế. Hố e sâu hơn cả b và g → e thắng.

Điều em bé cần nhớ: **cái hố e không thay đổi gì cả.** Từ đầu đến cuối nó vẫn là cái hố đó. Nó chỉ được đeo thêm huy chương sau mỗi vòng.

> [!tip] Dịch sang chart
> Hố = đáy. Hố nhỏ = **STL**. Hố vừa = **ITL**. Hố lớn = **LTL**. "Sâu hơn hai hố bên cạnh" = "thấp hơn hai đáy cùng cấp ở hai bên".

**Chỗ ví dụ này bị giới hạn (phải nói rõ):**
1. Trong trò chơi, em bé thấy **cả con đường cùng lúc**. Trên chart thật, con đường **hiện ra dần dần** từ trái sang phải. Lúc em đứng ở hố e, các hố f, g, h **chưa tồn tại**. Đây là vấn đề lớn nhất của cả concept (xem mục 19).
2. Trò chơi chỉ so với **hai hố ngay cạnh**, không so với cả con đường. Vì vậy "hố lớn" **không có nghĩa là hố sâu nhất con đường**. Đi tiếp, em bé vẫn có thể gặp hố sâu hơn nữa (xem mục 23).

### 2.3 Hình ảnh thứ hai — thung lũng nằm trong thung lũng

![[AMS-v2-02-Thung-Lung-Long-Nhau.svg|960]]
*Hình AMS-v2-02 — Cùng một đường giá như trò chơi cái hố. Khung xám: thung lũng nhỏ. Khung xanh: thung lũng vừa. Khung đỏ: thung lũng lớn. Chúng lồng vào nhau.*

Đứng trên núi nhìn xuống, ta thấy một thung lũng lớn. Đi xuống gần hơn, ta thấy trong thung lũng lớn có những chỗ trũng nhỏ hơn. Cúi xuống nữa, trong mỗi chỗ trũng lại có vài vũng nước.

- Vũng nước = STL.
- Chỗ trũng = ITL (điểm thấp nhất của chỗ trũng đó).
- Thung lũng = LTL (điểm thấp nhất của cả thung lũng).

Điểm thấp nhất của thung lũng lớn **cũng là** một chỗ trũng, và **cũng là** một vũng nước. Một điểm — ba tên.

### 2.4 Mental model một dòng

> **Đáy lớn = đáy nhỏ nằm ở chỗ thấp nhất của một vùng rộng hơn.**
> Muốn biết "rộng hơn" là rộng đến đâu, hãy hỏi: *nó thấp hơn bao nhiêu LỚP hàng xóm?*

---

## 3. Why Market Structure Has Hierarchical Swings — Vì sao có nhiều cấp swing?

### 3.1 Nói đơn giản

Giá không bao giờ đi một mạch. Nó đi kiểu **hai bước tới, một bước lùi**. Nhưng "bước" thì có nhiều cỡ:

- Có những bước tí hon kéo dài vài cây nến.
- Nhiều bước tí hon gộp lại thành một bước vừa.
- Nhiều bước vừa gộp lại thành một bước lớn.

Mỗi lần "lùi rồi tới lại" để lại **một cái đáy**. Bước tí hon để lại đáy nhỏ. Bước vừa để lại đáy vừa. Bước lớn để lại đáy lớn. Đó là tất cả.

### 3.2 Ví dụ đời thường — sóng biển

Đứng ở bờ biển, em bé thấy:
- **Gợn lăn tăn** vỗ vào chân liên tục.
- Thỉnh thoảng có **con sóng** lớn hơn chạy vào.
- Và cả mặt nước từ từ dâng lên rồi rút xuống trong ngày: **thủy triều**.

Gợn nằm trên sóng. Sóng nằm trên thủy triều. Ba thứ xảy ra **cùng lúc**, không thứ nào "tắt" thứ nào.

Giới hạn của ví dụ: sóng biển có nguyên nhân vật lý riêng cho từng cỡ (gió, mặt trăng). Thị trường **không có** ba "cỗ máy" riêng tạo ra ba cỡ swing. Ba cấp là cách **ta** cắt một đường gấp khúc liền mạch thành ba cỡ cho dễ nói chuyện.

### 3.3 Điều gì là sự thật, điều gì là diễn giải?

**[MARKET MECHANICS] — quan sát được:**
- Đường giá gấp khúc ở **mọi độ phóng to**. Phóng to một nhịp tăng trên D1, ta thấy bên trong nó có những nhịp lên–xuống trên H1. Phóng to tiếp, lại thấy lên–xuống trên M5.
- Một cái đáy hình thành khi, quanh một mức giá, lực bán thôi đẩy được giá xuống tiếp và giá quay lên. Chart chỉ cho thấy **kết quả** đó.

**[INTERPRETATION] — hợp lý nhưng không nhìn thấy trực tiếp:**
- Người tham gia thị trường có **tầm nhìn khác nhau**: có người giữ lệnh vài phút, có người giữ vài tuần, có tổ chức gom hàng vài tháng. Mỗi nhóm tạo ra những nhịp mua–bán cỡ riêng. Các nhịp đó chồng lên nhau thành hình sóng-trong-sóng.

**[CẢNH BÁO PHẢN BIỆN] — điều ít người nói:**
- **Bất kỳ đường gấp khúc nào cũng có STL, ITL, LTL — kể cả một đường vẽ bằng cách tung đồng xu.** Luật "thấp hơn hai hàng xóm" áp vào đâu cũng ra kết quả. Vì vậy, việc *tồn tại* thứ bậc **không chứng minh** thị trường "có cấu trúc thông minh" hay có ai đó sắp đặt. Thứ bậc là một **cách mô tả**. Nó có giúp dự đoán hay không là câu hỏi khác, và câu hỏi đó phải trả lời bằng backtest. **[BACKTEST REQUIRED]**

### 3.4 Vậy tại sao vẫn nên học nó?

Vì nó giải quyết ba việc thực tế, **không cần** giả định gì về "smart money":

1. **Lọc nhiễu.** Chart M5 có hàng chục đáy mỗi phiên. Không thể coi tất cả như nhau. Thứ bậc cho ta một cách công bằng để nói "đáy này đáng nhìn hơn đáy kia".
2. **Nói cùng một ngôn ngữ giữa các khung.** "H1-ITL" là một địa chỉ rõ ràng. "Cái đáy quan trọng kia" thì không.
3. **Đặt điểm sai (invalidation) có lý do.** "Nếu D1-ITL này vỡ thì giả thuyết tăng của tôi sai" là một câu kiểm chứng được.

---

## 4. Conceptual Foundation — Nền tảng khái niệm

### 4.1 Swing, trend và market structure liên hệ thế nào?

Nói đơn giản:

- **Swing** = một lần giá quay đầu. Quay từ xuống thành lên → **swing low** (đáy). Quay từ lên thành xuống → **swing high** (đỉnh).
- **Trend** (xu hướng) = cách các đỉnh và đáy **xếp hàng** theo thời gian. Đáy sau cao hơn đáy trước, đỉnh sau cao hơn đỉnh trước → tăng. Ngược lại → giảm.
- **Market structure** = toàn bộ bức tranh: có những swing nào, chúng thuộc cấp nào, chúng xếp hàng ra sao, cái nào đang "giữ" xu hướng, cái nào đã vỡ.

Vậy market structure **không chỉ** là danh sách các điểm đảo chiều. Nó là danh sách đó **cộng** với thứ bậc **cộng** với quan hệ giữa chúng.

### 4.2 Năm khái niệm không được trộn lẫn

![[AMS-v2-07-Nam-Khai-Niem-Khac-Nhau.svg|960]]
*Hình AMS-v2-07 — Năm chuyện khác nhau về cùng một cái đáy. Ba chuyện đầu trả lời bằng luật. Chuyện thứ năm là diễn giải.*

| # | Khái niệm | Câu hỏi nó trả lời | Biết được khi nào | Bản chất |
|---|---|---|---|---|
| 1 | **Hình thành** (formation) | Có cái đáy nào vừa in ra không? | Ngay lúc giá chạm mức thấp rồi nhích lên | Quan sát |
| 2 | **Xác nhận** (confirmation) | Cái đáy đó đã chắc là đáy chưa? | Khi nến bên phải **đóng** với đáy cao hơn | Luật |
| 3 | **Phân loại** (classification) | Nó là STL, ITL hay LTL? | Khi hàng xóm cùng cấp ở **bên phải** đã được xác nhận | Luật (quy ước ICT) |
| 4 | **Thứ bậc** (hierarchy) | Đáy nào nằm trong vùng của đáy nào? | Sau khi đã phân loại | Hệ quả của luật |
| 5 | **Ý nghĩa cấu trúc** (significance) | Nếu đáy này vỡ thì điều gì đổi? | Phụ thuộc bối cảnh | **Diễn giải — cần kiểm chứng** |

Ví dụ để thấy chúng khác nhau: đáy e trong Hình 01.
- Hình thành: lúc giá chạm bậc thấp nhất.
- Xác nhận là STL: một nến sau.
- Phân loại là ITL: phải chờ đáy f xuất hiện và được xác nhận.
- Phân loại là LTL: phải chờ cả g và h.
- Ý nghĩa cấu trúc: e có phải là nơi cả nhịp tăng bắt đầu, có đang "giữ" cấu trúc tăng không — câu này **không** được trả lời chỉ bằng cái nhãn LTL.

### 4.3 Quan hệ cha–con: ba chiếc mũ

![[AMS-v2-06-Ba-Chiec-Mu.svg|960]]
*Hình AMS-v2-06 — Mọi LTL đều là ITL. Mọi ITL đều là STL. Chiều ngược lại không đúng.*

- **Một ITL có bắt buộc sinh ra từ STL không?** Có. Theo luật đệ quy, ITL *là* một STL được lên cấp. Không tồn tại ITL nào mà không phải STL.
- **Một LTL có bắt buộc "chứa" ITL và STL không?** Có, theo hai nghĩa: (1) chính nó là một ITL và một STL; (2) nó cần ít nhất một ITL ở mỗi bên làm chứng, và mỗi ITL làm chứng lại cần STL hai bên của riêng nó. Vì thế một LTL hợp lệ cần **khá nhiều** đáy nhỏ xung quanh (trong ví dụ gọn nhất có thể dựng: bảy đáy nhỏ).
- **Mọi STL có thành ITL không?** Không. Đa số STL mãi là STL.

> [!note] Chữ "term" (short / intermediate / long) dễ gây hiểu lầm
> Ba chữ này nghe như nói về **thời gian** (ngắn hạn, trung hạn, dài hạn). Nhưng luật phân loại **không đo thời gian**. Nó đếm **lớp hàng xóm**. Một LTL trên M5 có thể hình thành trong một buổi sáng. Một STL trên D1 là đáy của cả một ngày. Vì vậy trong note này, bên cạnh tên gốc, mình dùng thêm cách gọi **đáy nhỏ / đáy vừa / đáy lớn** — và luôn kèm tên khung.

---

## 5. Short-Term Low (STL) — Đáy nhỏ

### 5.1 Nói đơn giản

STL là **cái đáy nhỏ nhất mà ta chịu đặt tên**. Giá đi xuống, dừng, rồi đi lên. Chỗ dừng đó là STL.

### 5.2 Ví dụ cho trẻ 5 tuổi

Em bé nhảy xuống ba bậc cầu thang. Ở bậc giữa em đứng thấp nhất. Bậc trước đó cao hơn, bậc sau đó cũng cao hơn. Bậc giữa là "chỗ thấp nhất của ba bậc". Đó là STL.

### 5.3 Chuỗi giá đơn giản

```text
Nến 1: đáy ở bậc 8
Nến 2: đáy ở bậc 6   ← thấp nhất
Nến 3: đáy ở bậc 7

Bậc 6 thấp hơn bậc 8 (bên trái) và thấp hơn bậc 7 (bên phải)
→ Đáy của nến 2 là một STL.
```

![[AMS-v2-03-STL-Ba-Cay-Nen.svg|960]]
*Hình AMS-v2-03 — Bốn tình huống ở cấp cây nến: đủ điều kiện, chưa đủ, không đủ, và mơ hồ.*

### 5.4 Định nghĩa kỹ thuật

**[ICT FRAMEWORK]** STL là một cây nến có **đáy (low)** mà cây nến ngay bên trái và cây nến ngay bên phải đều có **đáy cao hơn**. Đây là hình ba-nến mà nhiều tài liệu gọi là *swing low* hoặc *fractal low*.

**Nguồn gốc:** cách định nghĩa này đến từ Larry Williams. Williams mô tả đỉnh ngắn hạn là một ngày có đỉnh thấp hơn ở cả hai bên, **không tính inside day** (ngày nằm lọt trong ngày trước). ICT thừa nhận ảnh hưởng của Williams trong bài giảng về market structure (theo các bản ghi chép lại — xem mục Nguồn).

**Trả lời các câu hỏi trong đề bài:**

- *Điều kiện cần?* Ba thứ: (1) một nến có đáy thấp nhất, (2) nến trái có đáy cao hơn, (3) nến phải **đã đóng** và có đáy cao hơn.
- *Hai bên có vai trò gì?* Bên trái nói "giá đã đi xuống tới đây". Bên phải nói "giá đã thôi đi xuống". Thiếu bên phải thì ta chưa biết giá đã dừng hay chưa.
- *Vì sao phải cao hơn ở cả hai phía?* Vì "đáy" nghĩa là **thấp hơn xung quanh**. Chỉ thấp hơn một phía thì đó là một cái dốc, chưa phải cái hố.
- *Một điểm thấp đơn lẻ có phải STL không?* Không. Cây nến đang chạy tạo đáy mới chỉ là "giá đang thấp". Nó thành STL khi có nến bên phải đóng cao hơn.

### 5.5 Cơ chế hình thành — kiểm tra lại trình tự trong đề bài

Đề bài nêu năm bước, trong đó bước 4 là *"Những swing low xung quanh hình thành"*. **Bước này không thuộc về STL.** STL không cần swing low nào khác. Trình tự đúng ngắn hơn:

1. Giá giảm, một cây nến in ra đáy thấp hơn nến trước.
2. Cây nến tiếp theo **không** phá đáy đó và **đóng** lại.
3. Ngay lúc nến đó đóng → STL được **xác nhận**.

Các swing low xung quanh chỉ cần đến khi ta hỏi câu **tiếp theo**: STL này có được lên cấp ITL không?

**Ba quy ước phải tự chốt (vì nguồn không thống nhất):**

| Tình huống | Vấn đề | Quy ước của note này (v2.0) |
|---|---|---|
| Nến phải là **inside bar** | Williams bỏ qua inside day; nhiều indicator ICT thì không | Bỏ qua inside bar, chờ nến kế tiếp. Chậm hơn một nến nhưng ít đáy giả hơn |
| Hai đáy **bằng nhau** | Luật ghi "cao hơn", không ghi "cao hơn hoặc bằng" | Chưa có STL duy nhất. Coi là một **vùng đáy** (relative equal lows) |
| **Outside bar** (một nến vừa có đỉnh cao nhất vừa có đáy thấp nhất) | Một nến có thể vừa là STH vừa là STL | Chấp nhận cả hai nhãn; xuống khung nhỏ hơn để biết cái nào in ra trước |

Ba quy ước này là **lựa chọn nghiên cứu**, không phải luật ICT. **[BACKTEST REQUIRED]** nếu muốn biết lựa chọn nào tốt hơn.

### 5.6 Ý nghĩa cấu trúc

- *STL đại diện cho điều gì?* **[MARKET MECHANICS]** Một lần lực bán tạm hết ở một mức giá, trong phạm vi vài cây nến. Chỉ vậy.
- *STL có thể là điểm bảo vệ cấu trúc tăng không?* Có, **ở cấp ngắn hạn**: nếu cú tăng từ STL đó đã vượt đỉnh nhỏ trước nó (xem mục 14).
- *Khi STL bị phá thì gì đổi?* Chuỗi đáy nhỏ có một đáy thấp hơn. Cấp ngắn hạn không còn "đáy cao dần". ITL và LTL **chưa bị đụng tới**.
- *Phá STL có phải MSS hay CHoCH không?* **Không tự động.** MSS theo ICT cần thêm bối cảnh (lấy liquidity trước đó, có lực, đúng vị trí). Xem mục 17.
- *Khi nào STL chỉ là dao động nhỏ?* Gần như **luôn luôn**, nếu nhìn từ khung lớn hơn. Một M5-STL là vô hình trên D1.

### 5.7 Năm ví dụ nhận diện

**Ví dụ 1 — STL rõ ràng.** Ba nến, đáy ở bậc 8 – 6 – 7. Nến giữa là STL. *Vì sao:* đủ cả ba điều kiện, nến phải đã đóng.

**Ví dụ 2 — STL trong uptrend.** Giá tăng kiểu bậc thang. Mỗi lần lùi nhẹ rồi tăng tiếp để lại một STL. Các STL **cao dần**. *Vì sao đáng chú ý:* đây là những STL "làm được việc" — mỗi cái đẩy giá lên đỉnh mới. Xem Hình 10, ô A.

**Ví dụ 3 — STL trong downtrend.** Giá giảm, nghỉ, giảm tiếp. Mỗi lần nghỉ để lại một STL. Các STL **thấp dần** và bị phá gần như ngay. *Vì sao:* cũng là STL hợp lệ, nhưng vai trò khác hẳn — chỉ là chỗ giá nghỉ chân. Cùng một nhãn, hai ý nghĩa.

**Ví dụ 4 — STL trong vùng đi ngang.** Nhiều STL nằm sát nhau ở gần cùng một mức. *Vì sao đáng chú ý:* từng cái riêng lẻ không có gì đặc biệt; cả cụm thì tạo thành relative equal lows.

**Ví dụ 5 — Giống STL nhưng chưa đủ.** Cây nến hiện tại vừa tạo đáy thấp nhất và đang bật lên mạnh, **nhưng chưa đóng**; hoặc nến bên phải có đáy **bằng** nến giữa. *Vì sao không đủ:* thiếu xác nhận bên phải. Gọi là "STL ứng viên". Xem Hình 03, ô ② và ③.

---

## 6. Intermediate-Term Low (ITL) — Đáy vừa

### 6.1 Nói đơn giản

ITL là **một đáy nhỏ thắng hai đáy nhỏ đứng cạnh nó**. "Thắng" nghĩa là thấp hơn.

### 6.2 Ví dụ cho trẻ 5 tuổi

Ba bạn nhỏ chơi trốn tìm, mỗi bạn ngồi thụp xuống trong một cái hố. Bạn ngồi ở giữa thấp hơn bạn bên trái và thấp hơn bạn bên phải. Bạn ở giữa là "người ngồi thấp nhất nhóm ba". Đó là ITL.

Nếu bạn ở giữa chỉ thấp hơn bạn bên trái, còn bạn bên phải ngồi thấp hơn nữa — thì bạn ở giữa **không thắng**.

### 6.3 Chuỗi giá đơn giản

![[AMS-v2-04-STL-Thanh-ITL.svg|960]]
*Hình AMS-v2-04 — Năm đáy nhỏ a, b, c, d, e. Chỉ c là ITL, vì cả b (bên trái) và d (bên phải) đều cao hơn c.*

```text
Đáy nhỏ:   a      b      c      d      e
Bậc:       52     46     36     44     48

Xét b: bên trái là a (cao hơn b) ✓ — bên phải là c (THẤP hơn b) ✗ → b chỉ là STL
Xét c: bên trái là b (cao hơn c) ✓ — bên phải là d (cao hơn c) ✓ → c là ITL
Xét d: bên trái là c (THẤP hơn d) ✗                              → d chỉ là STL
```

### 6.4 Định nghĩa kỹ thuật

**[ICT FRAMEWORK]** ITL là một STL mà **STL liền kề bên trái** và **STL liền kề bên phải** đều cao hơn nó.

- *ITL được xác định dựa trên swing nào?* Chỉ dựa trên **các STL**. Không dựa trên nến, không dựa trên đỉnh.
- *Quan hệ ITL–STL?* ITL là tập con của STL (Hình 06).
- *Vì sao ITL "cao cấp" hơn?* Vì để thắng, nó phải thấp hơn **một vùng rộng hơn** — vùng trải qua ít nhất ba đáy nhỏ. Nó là đáy của một nhịp lùi **lớn hơn các nhịp lùi hai bên**.

> [!caution] Nguồn không thống nhất ở đây
> Luật trên là luật **vị trí** (đệ quy), khớp với Larry Williams và với đa số tài liệu ICT. Nhưng theo các bản **ghi chép lại** bài giảng ICT 2022 Mentorship tập 12, ICT còn mô tả ITH/ITL theo **chức năng**: đỉnh/đáy hình thành khi giá quay lại lấp một khoảng trống giá (FVG) được coi là ITH/ITL, và ITH "thường" (không phải luôn luôn) có STH thấp hơn hai bên. Hai cách này có thể cho hai nhãn khác nhau. Xem mục 11.4 và Hình 12. Note này dùng luật **vị trí** làm luật chính.

### 6.5 Cơ chế hình thành từng bước

1. Giá tạo một STL (gọi là b).
2. Giá bật lên, rồi lùi xuống **sâu hơn** b, tạo STL mới (c). Lúc này b mất cơ hội lên cấp.
3. Giá bật lên từ c, rồi lùi xuống nhưng **dừng ở trên** c, tạo STL mới (d).
4. Khi d được xác nhận (nến bên phải d đóng cao hơn) → c có đủ hàng xóm hai bên, cả hai đều cao hơn.
5. **Ngay lúc đó** c được xác nhận là ITL.

Lưu ý bước 5: ITL được xác nhận **không phải lúc c in ra**, mà lúc **d được xác nhận**. Khoảng giữa hai thời điểm đó, c chỉ là "ITL ứng viên".

### 6.6 Vì sao không phải mọi STL đều thành ITL?

![[AMS-v2-10-Khong-Phai-STL-Nao-Cung-Thanh-ITL.svg|960]]
*Hình AMS-v2-10 — Ô A: bậc thang đều, mọi đáy cao hơn đáy trước → không có ITL. Ô B: một nhịp lùi sâu hơn bình thường → ITL xuất hiện.*

Vì luật đòi thấp hơn **cả hai** hàng xóm.

- Trong một nhịp tăng đều, mỗi đáy cao hơn đáy bên trái nó. Không đáy nào thắng được hàng xóm bên trái → **không có ITL nào**, dù có rất nhiều STL.
- Trong một nhịp giảm đều, mỗi đáy thấp hơn đáy bên trái, nhưng đáy bên phải lại còn thấp hơn → cũng **không có ITL**.
- ITL chỉ xuất hiện ở chỗ có **một nhịp lùi sâu hơn hai nhịp lùi bên cạnh** rồi giá quay lên lại.

> **Mental model:** ITL là dấu vết của "một lần lùi lớn hơn bình thường, rồi hồi phục".

Hệ quả thú vị: một xu hướng tăng **rất khỏe** có thể **không tạo ra ITL mới nào** trong thời gian dài. Thiếu ITL không có nghĩa là yếu.

### 6.7 Ý nghĩa cấu trúc

- *Vai trò?* **[INTERPRETATION]** ITL đánh dấu đáy của một nhịp điều chỉnh có cỡ đáng kể trên khung đang xem. Nó thường là mép dưới của vùng giá đang giao dịch (xem mục 15).
- *ITL có thể là protected low không?* Có thể, nhưng **không tự động** (mục 14).
- *Khi ITL bị phá?* Chuỗi đáy vừa có đáy thấp hơn → cấp trung hạn không còn "đáy cao dần". Vùng trong/ngoài phải vẽ lại.
- *Khác gì với phá STL?* Phá STL chỉ nói về vài cây nến gần nhất. Phá ITL nói về cả một nhịp. **[HYPOTHESIS]** Phá ITL "nghiêm trọng hơn" theo nghĩa giá ít khi chỉ là nhiễu — đây là giả thuyết cần đếm thật trên dữ liệu.
- *ITL có còn tồn tại khi các STL bên trong đã bị phá không?* **Có.** Các STL nằm **phía trên** ITL có thể vỡ hết mà ITL vẫn nguyên. Đó chính là tình huống "nội bộ đổi, mép ngoài chưa đổi" (Scenario G, mục 18).

### 6.8 Năm ví dụ nhận diện

**Ví dụ 1 — ITL rõ ràng.** Đáy c trong Hình 04. *Vì sao:* thấp hơn b và d, cả hai đã được xác nhận.

**Ví dụ 2 — ITL trong uptrend.** Hình 10, ô B: giữa một nhịp tăng có một lần lùi sâu hơn hẳn. Đáy của lần lùi đó là ITL. *Vì sao:* thấp hơn đáy nhỏ trước nó và đáy nhỏ sau nó.

**Ví dụ 3 — ITL trong downtrend.** Hình 22, vòng xanh đầu tiên bên trái: trong lúc giá đang giảm, có một đáy được hai đáy cao hơn kẹp hai bên. Nó là ITL hợp lệ — rồi bị phá khi xu hướng giảm tiếp tục. *Bài học:* ITL trong downtrend là **mục tiêu bị lấy**, không phải chỗ dựa.

**Ví dụ 4 — ITL trong vùng đi ngang.** Giá đi ngang, ba lần chạm đáy; lần giữa chọc sâu nhất. Lần giữa là ITL. *Vì sao đáng chú ý:* đây thường là cú "chọc thủng mép dưới rồi quay lại" — nơi sweep hay xảy ra.

**Ví dụ 5 — STL bị nhầm thành ITL.** Đáy b trong Hình 04: nhìn vào thấy b thấp hơn a nên tưởng "đáy quan trọng". Nhưng c bên phải còn thấp hơn. *Vì sao sai:* chỉ thắng một bên. Tình huống thứ hai hay gặp hơn: đáy sâu nhất ở **mép phải** chart (Hình 23, ô C) — chưa có hàng xóm bên phải nên chưa thể là ITL.

---

## 7. Long-Term Low (LTL) — Đáy lớn

### 7.1 Nói đơn giản

LTL là **một đáy vừa thắng hai đáy vừa đứng cạnh nó**. Cùng một trò chơi, chơi thêm một vòng nữa.

### 7.2 Ví dụ cho trẻ 5 tuổi

Mỗi lớp chọn ra bạn ngồi thấp nhất lớp (đó là các ITL). Bây giờ các bạn "thấp nhất lớp" của ba lớp cạnh nhau ngồi cùng một hàng. Bạn ở giữa thấp hơn bạn lớp bên trái và bạn lớp bên phải. Bạn đó là "thấp nhất khối". Đó là LTL.

Chú ý: "thấp nhất khối" **không có nghĩa** là thấp nhất cả trường. Khối bên cạnh vẫn có thể có bạn thấp hơn.

### 7.3 Chuỗi giá đơn giản

![[AMS-v2-05-Ba-Cap-Tren-Mot-Duong-Gia.svg|960]]
*Hình AMS-v2-05 — Tám đáy nhỏ. Ba ITL (b, e, g). e thấp hơn cả b và g → e là LTL.*

```text
Đáy nhỏ:   a    b    c    d    e    f    g    h
Bậc:       50   44   48   40   30   38   34   42

Vòng 2 (tìm ITL):  b thắng a và c ✓   e thắng d và f ✓   g thắng f và h ✓
                   d thua e ✗         c, f cao hơn hàng xóm ✗

Các ITL:           b(44)    e(30)    g(34)
Vòng 3 (tìm LTL):  e thấp hơn b ✓ và thấp hơn g ✓  →  e là LTL
```

### 7.4 Định nghĩa kỹ thuật

**[ICT FRAMEWORK]** LTL là một ITL mà **ITL liền kề bên trái** và **ITL liền kề bên phải** đều cao hơn nó.

Đây là điểm mà Larry Williams, các ghi chép ICT và tài liệu cộng đồng **đều đồng ý**: đỉnh/đáy dài hạn là đỉnh/đáy trung hạn có đỉnh/đáy trung hạn "kém hơn" ở cả hai bên.

Hai ý bổ sung từ nguồn ICT (đều là nguồn thứ cấp, **không** phải điều kiện của luật):
- LTH/LTL "thường gắn với chart ngày" (ghi chép tập 12).
- LTH/LTL "thường hình thành tại một PD array của khung lớn hơn" (bài viết cộng đồng).

Cả hai nên hiểu là **đặc điểm hay đi kèm**, dùng để tăng độ tin cậy, không dùng để định nghĩa.

### 7.5 Cơ chế hình thành — kiểm tra lại trình tự

Trình tự trong đề bài (STL → các ITL → ITL được ITL bao quanh → LTL xác nhận) là **đúng**. Bổ sung phần thời điểm:

1. Các STL hình thành dần.
2. Một số STL lên cấp ITL (mỗi cái cần STL bên phải xác nhận).
3. Một ITL (gọi là e) thấp hơn ITL bên trái nó (b).
4. Giá bật lên từ e. Để e thành LTL, phía bên phải phải xuất hiện **một ITL mới cao hơn e** (gọi là g).
5. Mà g muốn là ITL thì cần **một STL bên phải g cao hơn g** (gọi là h) được xác nhận.
6. Lúc h được xác nhận → g thành ITL → e có ITL cao hơn ở hai bên → **e được xác nhận là LTL**.

Tức là: giữa lúc e in ra và lúc e được gọi là LTL, giá phải **bật lên, lùi một nhịp đáng kể (tạo g), rồi bật lên lần nữa và lùi nhẹ (tạo h)**. Đó là một quãng đường dài (Hình 08).

### 7.6 Ý nghĩa cấu trúc — và các hiểu lầm lớn

- *LTL đại diện cho điều gì?* **[INTERPRETATION]** Đáy của nhịp điều chỉnh lớn nhất trong vùng đang xem, trên khung đang xem.
- *LTL có luôn là major low không?* **Không.** "Major" là một đánh giá; LTL là một nhãn vị trí **trên một khung**. M5-LTL chỉ là một đáy trong buổi sáng.
- *LTL có nhất thiết là đáy của một xu hướng lớn không?* **Không.** Xem ngay bên dưới.
- *LTL có thể nằm trong downtrend lớn hơn không?* **Có**, và đây là phản ví dụ quan trọng nhất của note.

![[AMS-v2-22-LTL-Trong-Xu-Huong-Giam.svg|960]]
*Hình AMS-v2-22 — Một LTL hợp lệ (vòng đỏ) nằm giữa xu hướng giảm. Sau một cú bật, giá quay xuống và xuyên qua nó.*

- *Khi LTL bị phá?* Đáy lớn nhất của khung đó không còn giữ. Cấu trúc tăng **trên khung đó** mất chỗ dựa.
- *Phá LTL có phải đảo chiều xu hướng không?* **Không tự động.** (1) Nếu trước đó xu hướng đang **giảm** (như Hình 22) thì phá LTL là **tiếp diễn**, không phải đảo chiều. (2) Nếu xu hướng đang tăng, phá LTL là bằng chứng mạnh rằng cấu trúc tăng của khung đó đã hỏng — nhưng đó vẫn có thể là một cú quét lớn rồi quay lên, và nó không nói gì về khung lớn hơn.

### 7.7 Năm ví dụ nhận diện

**Ví dụ 1 — LTL rõ ràng.** Đáy e trong Hình 05. *Vì sao:* là ITL, và hai ITL hai bên (b, g) đều cao hơn.

**Ví dụ 2 — LTL trong uptrend.** Hình 13 (Case A): LTL nằm ở đáy lớn nơi nhịp tăng bắt đầu. Sau đó các ITL **cao dần**. *Vì sao đáng chú ý:* trong một uptrend sạch, **không có LTL mới** nào hình thành — vì không ITL nào thấp hơn ITL bên trái nó. LTL mới chỉ xuất hiện sau một đợt điều chỉnh **lớn**.

**Ví dụ 3 — LTL trong downtrend.** Hình 22. *Vì sao:* đúng luật, sai kỳ vọng. Nhãn LTL không bảo vệ được nó.

**Ví dụ 4 — LTL trong vùng đi ngang rộng.** Ba đợt chạm đáy lớn, đợt giữa sâu nhất, mỗi đợt có các đáy nhỏ bên trong. **[INTERPRETATION]** Hình này trùng với mẫu hình cổ điển "vai – đầu – vai ngược": hai vai là hai ITL, đầu là LTL. Hai trường phái gọi tên khác nhau cho cùng một hình dạng.

**Ví dụ 5 — ITL bị nhầm thành LTL.** Một ITL là điểm thấp nhất trên màn hình, bên trái có ITL cao hơn, nhưng **bên phải chưa có ITL nào được xác nhận** (giá mới bật lên, chưa có nhịp lùi đủ lớn). *Vì sao sai:* thiếu nhân chứng bên phải. Đúng tên: "LTL ứng viên". Đây là lỗi phổ biến nhất khi đọc real-time.

---

## 8. Short-Term High (STH) — Đỉnh nhỏ

![[AMS-v2-11-Dinh-STH-ITH-LTH.svg|960]]
*Hình AMS-v2-11 — Phía đỉnh. Tám đỉnh nhỏ (A đến H). Ba ITH (B, E, G). Một LTH (E).*

**Nói đơn giản:** giá đi lên, dừng, rồi đi xuống. Chỗ dừng đó là đỉnh nhỏ.

**Ví dụ cho trẻ 5 tuổi:** em bé tung quả bóng lên. Quả bóng lên cao, dừng một tí ở chỗ cao nhất, rồi rơi xuống. Chỗ cao nhất đó là STH.

**Định nghĩa:** **[ICT FRAMEWORK]** một cây nến có **đỉnh (high)** mà nến bên trái và nến bên phải đều có đỉnh **thấp hơn**. Nến bên phải phải đã đóng.

**Ý nghĩa:** **[MARKET MECHANICS]** một lần lực mua tạm hết ở một mức giá, trong phạm vi vài nến. Phía trên STH là nơi lệnh chờ mua (buy stop) *có thể* nằm — của người đang bán muốn cắt lỗ và của người chờ mua khi giá vượt đỉnh.

---

## 9. Intermediate-Term High (ITH) — Đỉnh vừa

**Nói đơn giản:** một đỉnh nhỏ **cao hơn** hai đỉnh nhỏ đứng cạnh nó.

**Định nghĩa:** **[ICT FRAMEWORK]** một STH mà STH liền kề bên trái và bên phải đều thấp hơn nó.

**Cơ chế hình thành:** giá lập đỉnh B, lùi, rồi bật lên nhưng **không vượt được** B, tạo đỉnh nhỏ thấp hơn. Khi đỉnh nhỏ thấp hơn đó được xác nhận, và bên trái B cũng là một đỉnh nhỏ thấp hơn → B là ITH.

> **Mental model:** ITH là dấu vết của "một lần giá cố vượt đỉnh và **thất bại**". Chính cái đỉnh thấp hơn bên phải làm nên ITH.

**Ý nghĩa cho cấu trúc giảm:** trong một nhịp giảm, các ITH là những "bậc thang đi xuống". Chừng nào ITH gần nhất chưa bị vượt, cấp trung hạn chưa có bằng chứng đổi hướng.

---

## 10. Long-Term High (LTH) — Đỉnh lớn

**Nói đơn giản:** một đỉnh vừa cao hơn hai đỉnh vừa đứng cạnh nó.

**Định nghĩa:** **[ICT FRAMEWORK]** một ITH mà ITH liền kề bên trái và bên phải đều thấp hơn nó.

**Ý nghĩa:** đỉnh của nhịp tăng lớn nhất trong vùng đang xem, trên khung đang xem. Cũng như LTL, nó **không** tự động là "đỉnh của thị trường".

### 10.1 Quan hệ giữa ba cấp đỉnh và ba cấp đáy

- Luật **đối xứng hoàn toàn**: đổi "thấp hơn" thành "cao hơn".
- Đỉnh và đáy được phân loại **độc lập**. Việc tìm ITH chỉ nhìn các STH. Không nhìn đáy.
- Ở cấp nhỏ, đỉnh và đáy **luôn xen kẽ** (giữa hai STL luôn có ít nhất một STH).
- Ở cấp vừa và lớn, chúng **không bắt buộc xen kẽ**. Có thể có hai ITL liên tiếp mà ở giữa không có ITH nào (khi giá vẫn lập đỉnh cao dần trong lúc có hai nhịp lùi sâu). Đây là điều nhiều người không ngờ tới, và là lý do không nên vẽ cấu trúc cấp vừa thành một đường zigzag "đẹp" bằng mắt.

### 10.2 Dùng các swing high để đọc cấu trúc giảm

Xem Hình 14 (Case B). Cách đọc: tìm LTH → các ITH sau nó có **thấp dần** không → ITH gần nhất nằm ở đâu → giá đang ở dưới hay đã vượt nó.

### 10.3 Bốn chỗ BẤT đối xứng (đề bài yêu cầu kiểm tra)

Luật thì đối xứng. Nhưng thực tế có vài chỗ lệch. Mỗi chỗ được dán nhãn mức độ chắc chắn.

1. **Cổ phiếu và chỉ số: rơi thường nhanh hơn lên.** **[MARKET MECHANICS — phụ thuộc thị trường]** Ở thị trường chứng khoán, các đợt giảm thường diễn ra nhanh và gọn hơn các đợt tăng. Hệ quả có thể có: vùng đáy thường nhọn (ít nến, ít đáy nhỏ xung quanh), vùng đỉnh thường tù và kéo dài (nhiều đỉnh nhỏ sát nhau). Nếu đúng, LTL trên chỉ số sẽ có ít "nhân chứng" gần nó hơn LTH. **[HYPOTHESIS]** — chưa đếm trên dữ liệu của mình.
2. **Forex: về nguyên tắc không có lệch.** **[MARKET MECHANICS]** Một cặp tiền là tỉ lệ giữa hai đồng. Đáy của EURUSD chính là đỉnh của USD so với EUR. Không có lý do cấu trúc nào để đỉnh và đáy hành xử khác nhau.
3. **Nến outside bar và inside bar.** Một nến có thể vừa là STH vừa là STL (outside bar). Điều này phá vỡ sự xen kẽ đỉnh–đáy ở cấp nhỏ nếu ta chỉ nhìn một khung.
4. **Cách ICT nói về hai phía.** **[ICT FRAMEWORK — nguồn thứ cấp]** Theo ghi chép tập 12: khi dòng lệnh đang giảm thì các nến tăng "được tôn trọng" (không bị vượt qua), khi dòng lệnh tăng thì các nến giảm được tôn trọng. Đây là một nhận định về hành vi, **không phải** một phần của luật phân loại. **[BACKTEST REQUIRED]**

---

## 11. STL → ITL → LTL Formation Mechanism — Cơ chế "lên cấp"

Đây là phần trung tâm của note.

### 11.1 Tám câu hỏi, tám câu trả lời ngắn

| Câu hỏi | Trả lời |
|---|---|
| Vì sao thị trường có nhiều cấp swing? | Vì giá gấp khúc ở mọi cỡ; các nhịp lên–lùi nhỏ nằm trong nhịp lên–lùi lớn (mục 3) |
| Vì sao một swing low nằm trong một swing low lớn hơn? | Vì đáy lớn chỉ là đáy nhỏ ở chỗ thấp nhất của vùng rộng hơn; các đáy nhỏ khác trong vùng đó "thuộc về" nó |
| Điều gì phân biệt swing nhỏ với swing lớn? | Số **lớp hàng xóm** mà nó thắng |
| Có phải chỉ do độ cao/độ sâu? | **Không.** Một cú rơi rất dài vẫn có thể kết thúc ở một đáy cao hơn đáy bên trái → vẫn chỉ là STL (Hình 23, ô B) |
| Hay do vị trí trong cấu trúc tổng thể? | **Đúng.** Cấp độ là chuyện vị trí tương đối, không phải chuyện kích thước tuyệt đối |
| Vì sao một swing low hình thành từ nhiều chuyển động nhỏ? | Vì để giá "xuống rồi lên" ở cỡ lớn, bên trong nó phải có nhiều lần "xuống rồi lên" cỡ nhỏ |
| Swing nhỏ kết hợp thành swing lớn thế nào? | Không phải "cộng lại". Một trong số chúng **được chọn** làm đại diện: cái thấp nhất so với hai bên |
| Vì sao không coi mọi swing low ngang nhau? | Vì chúng ghi lại những nhịp lùi cỡ khác nhau. Phá một đáy nhỏ và phá một đáy lớn là hai sự kiện khác cỡ |

### 11.2 Một STL trở thành ITL như thế nào? (câu hỏi trung tâm 1)

Câu trả lời chính xác: **STL không "biến thành" ITL. Nó được GỌI THÊM là ITL khi một STL cao hơn xuất hiện và được xác nhận ở bên phải nó** (và bên trái đã có sẵn một STL cao hơn).

Tức là việc lên cấp **hoàn toàn phụ thuộc vào chuyện xảy ra sau đó**. Bản thân cái đáy không làm gì thêm. Thứ quyết định là **nhịp lùi kế tiếp có dừng ở trên nó hay không**.

- Nhịp lùi kế tiếp dừng **trên** nó → nó lên cấp.
- Nhịp lùi kế tiếp xuống **dưới** nó → nó mất cơ hội, và cái đáy mới trở thành ứng viên.

### 11.3 Một ITL trở thành LTL như thế nào? (câu hỏi trung tâm 2)

Cùng logic, lên một tầng: **ITL được gọi thêm là LTL khi một ITL cao hơn xuất hiện và được xác nhận ở bên phải nó** (và bên trái đã có sẵn một ITL cao hơn).

Mà "một ITL xuất hiện bên phải" lại đòi một nhịp lùi **đáng kể** (đủ để tạo ITL mới) rồi **thêm một nhịp lùi nhỏ nữa** (để xác nhận ITL mới đó). Vì thế LTL được xác nhận rất muộn.

![[AMS-v2-08-Do-Tre-Xac-Nhan.svg|960]]
*Hình AMS-v2-08 — Cùng một đáy e, ba thời điểm "biết": ① biết là STL, ② biết là ITL, ③ biết là LTL. Vệt đỏ dưới chân là quãng "e đã tồn tại nhưng chưa được gọi là LTL".*

> [!important] Hệ quả thực tế
> - Nhãn cấp cao **luôn đến muộn**. Đó không phải lỗi của bạn; đó là bản chất của luật.
> - Vì vậy nhãn cấp cao dùng để **đọc bối cảnh** ("đáy lớn của vùng này ở đâu?"), không dùng để **bấm nút vào lệnh**.
> - Muốn hành động sớm hơn thì phải chấp nhận làm việc với **ứng viên** — và ghi rõ đó là ứng viên.

### 11.4 Hai "ống kính": vị trí và chức năng

![[AMS-v2-12-Hai-Ong-Kinh-Vi-Tri-va-Chuc-Nang.svg|960]]
*Hình AMS-v2-12 — Đỉnh C: theo luật vị trí chỉ là STH (vì B bên trái cao hơn). Theo cách mô tả chức năng trong ghi chép tập 12, C là ITH vì nó hình thành khi giá quay lại lấp một khoảng trống giá.*

Có hai cách trả lời câu "đỉnh/đáy này thuộc cấp nào":

| | Ống kính **vị trí** | Ống kính **chức năng** |
|---|---|---|
| Hỏi gì | Nó thắng mấy lớp hàng xóm? | Nó đã làm gì? (lấp FVG? phản ứng tại mức của khung lớn?) |
| Nguồn | Larry Williams; đa số tài liệu ICT | Ghi chép lại ICT 2022 Mentorship tập 12 (nguồn thứ cấp) |
| Ưu điểm | Rõ, lập trình được, hai người chấm ra cùng kết quả | Gắn với lý do giá quay đầu |
| Nhược điểm | Có thể gắn nhãn cao cho một đáy "vô nghĩa" | Phải nhận diện FVG trước; chủ quan hơn |
| Trong downtrend | Hiếm khi có ITH (các đỉnh thấp dần → không đỉnh nào thắng bên trái) | Mỗi lần hồi lên lấp FVG đều tạo một ITH |

**Quyết định nghiên cứu của note (v2.0):** dùng ống kính **vị trí** làm luật phân loại chính. Ống kính chức năng được ghi thành **thẻ phụ** ("đỉnh này đã lấp FVG"). Không trộn hai thứ vào một nhãn. Lý do: muốn backtest được thì luật phải ra cùng một kết quả mỗi lần chấm.

> [!caution] Mức độ chắc chắn về nguồn
> Mình **không** kiểm tra được trực tiếp video tập 12 trong lần nghiên cứu này. Thông tin đến từ ghi chép của người học trên diễn đàn và một bản tóm tắt tự động (bản tóm tắt còn tự mâu thuẫn ở một chỗ). Vì vậy mọi câu "ICT nói…" về tập 12 trong note này là **[ICT FRAMEWORK — nguồn thứ cấp, chưa đối chiếu bản gốc]**. Việc cần làm: tự xem lại tập 12 và sửa mục này nếu khác.

---

## 12. Relationship Between Highs and Lows — Đỉnh và đáy liên hệ thế nào?

### 12.1 Vì sao phải nhìn cả hai phía?

**Nói đơn giản:** một cái đáy chỉ kể **nửa câu chuyện**. Nó nói "giá đã dừng rơi ở đây". Nửa còn lại là: "rồi giá lên được tới đâu?"

- Đáy **rồi** đỉnh cao hơn đỉnh trước → cái đáy đó đã **làm được việc** (đẩy giá lên vùng mới).
- Đáy **rồi** đỉnh thấp hơn đỉnh trước → cái đáy đó **chưa làm được gì**.

Chỉ nhìn các đáy, ta không phân biệt được hai trường hợp này. Đây là lý do "protected low" phải được định nghĩa bằng **đỉnh** (mục 14).

### 12.2 HH, HL, LH, LL nằm ở đâu trong hệ thống ba cấp?

HH (higher high), HL (higher low), LH (lower high), LL (lower low) **không phải cấp độ**. Chúng là **phép so sánh** giữa hai swing **cùng cấp, liền nhau**.

| Nhãn | Nghĩa | Ví dụ ở cấp vừa |
|---|---|---|
| HL | Đáy này cao hơn đáy cùng cấp trước nó | ITL mới cao hơn ITL trước |
| HH | Đỉnh này cao hơn đỉnh cùng cấp trước nó | ITH mới cao hơn ITH trước |
| LH | Đỉnh này thấp hơn đỉnh cùng cấp trước nó | ITH mới thấp hơn ITH trước |
| LL | Đáy này thấp hơn đáy cùng cấp trước nó | ITL mới thấp hơn ITL trước |

Vậy **mỗi cấp có chuỗi HH/HL/LH/LL riêng**, và mỗi cấp có xu hướng riêng:

- Chuỗi STL/STH → xu hướng ngắn hạn.
- Chuỗi ITL/ITH → xu hướng trung hạn.
- Chuỗi LTL/LTH → xu hướng dài hạn.

Ba xu hướng này **có thể khác nhau cùng một lúc**. Ngắn hạn giảm trong lúc trung hạn tăng là chuyện rất bình thường: đó chính là một nhịp hồi.

> [!warning] Lỗi kinh điển
> Viết "HL" lên chart mà không nói **HL của cấp nào**. Một đáy có thể là HL ở cấp nhỏ (cao hơn STL trước) nhưng thuộc về một chuỗi LL ở cấp vừa.

### 12.3 Swing nào đang giữ cấu trúc?

- Cấu trúc **tăng** ở một cấp được giữ bởi **một cái đáy** của cấp đó: đáy gần nhất mà từ đó giá đã vượt đỉnh.
- Cấu trúc **giảm** ở một cấp được giữ bởi **một cái đỉnh** của cấp đó: đỉnh gần nhất mà từ đó giá đã thủng đáy.

Khi swing đó bị phá → cấu trúc ở **cấp đó** đổi. Cấp khác chưa chắc.

---

## 13. Bullish and Bearish Market Structure — Cấu trúc tăng và giảm

### 13.1 Cấu trúc tăng (Case A)

![[AMS-v2-13-Case-A-Cau-Truc-Tang.svg|960]]
*Hình AMS-v2-13 — Case A. Đọc từ trái sang phải: giảm → LTL → ITL thứ nhất cao hơn LTL → vượt ITH → ITL thứ hai cao hơn → vượt ITH lần nữa.*

**Đọc theo ba cấp:**

- **Cấp lớn:** có một LTL ở đáy. Chưa có LTH nào (giá còn đang lập đỉnh mới nên chưa đỉnh nào có "hàng xóm thấp hơn bên phải" ở cấp vừa).
- **Cấp vừa:** sau LTL có hai ITL, cái sau cao hơn cái trước (HL ở cấp vừa). Có hai ITH, cái sau cao hơn cái trước (HH ở cấp vừa). → Cấp vừa đang **tăng**.
- **Cấp nhỏ:** rất nhiều chấm xám. Có lúc đáy nhỏ thấp dần (trong các nhịp lùi), có lúc cao dần. Cấp nhỏ **đổi hướng liên tục** — bình thường.

**Cái gì đang được bảo vệ?** ITL thứ hai (đường ngang xanh đậm). Cú tăng từ nó đã vượt ITH trước đó. Chừng nào nó chưa bị phá, cấu trúc tăng cấp vừa còn nguyên.

**Cái gì đã bị phá?** Hai ITH (đều bị vượt lên). Không có đáy cấp vừa nào bị phá kể từ LTL.

### 13.2 Cấu trúc giảm (Case B)

![[AMS-v2-14-Case-B-Cau-Truc-Giam.svg|960]]
*Hình AMS-v2-14 — Case B. Soi gương của Case A: LTH → ITH thấp dần → ITL thấp dần.*

Đọc tương tự, đổi chiều: LTH ở đỉnh; các ITH thấp dần (LH cấp vừa); các ITL thấp dần (LL cấp vừa). Đỉnh đang giữ cấu trúc giảm là ITH gần nhất (protected high).

### 13.3 Trả lời hai sơ đồ trong đề bài

Đề bài đưa hai sơ đồ chỉ gồm HH/HL và LH/LL rồi hỏi "swing nào là STL, ITL, LTL?". **Không trả lời được từ sơ đồ đó**, vì:

- Sơ đồ chỉ có **một cấp** swing. Mọi đỉnh/đáy trong đó ít nhất là STH/STL.
- Trong một chuỗi HL thuần (đáy nào cũng cao hơn đáy trước), **không đáy nào là ITL** theo luật vị trí — vì không đáy nào thắng được hàng xóm bên trái (Hình 10, ô A).
- Muốn có ITL/LTL, sơ đồ phải có **nhịp lùi cỡ khác nhau**. Hình 13 và 14 là phiên bản đầy đủ của hai sơ đồ đó.

Đây là một phát hiện đáng nhớ: **một xu hướng "sạch như sách giáo khoa" lại là nơi hệ thống ba cấp nói được ít nhất.**

---

## 14. Protected High and Protected Low — Đỉnh/đáy "được bảo vệ"

### 14.1 Nói đơn giản

Em bé leo cầu thang. Mỗi lần em bước lên được một bậc **cao hơn bậc cao nhất trước đó**, em đánh dấu bậc mình vừa đứng trước khi bước: "đây là chỗ mình đứng vững". Nếu sau này em tụt xuống **dưới** chỗ đánh dấu đó, em biết mình không còn leo lên nữa.

Chỗ đánh dấu đó là **protected low**.

### 14.2 Định nghĩa dùng trong note

**[INTERPRETATION — quy ước nghiên cứu v2.0]**

- **Protected low** (ở một cấp, trên một khung) = đáy gần nhất mà **cú tăng từ nó đã đóng nến vượt đỉnh cùng cấp trước đó**.
- **Protected high** = đỉnh gần nhất mà cú giảm từ nó đã đóng nến thủng đáy cùng cấp trước đó.

> [!caution] Về nguồn gốc thuật ngữ
> "Protected high/low" được dùng rất rộng trong cộng đồng ICT/SMC. Trong lần nghiên cứu này mình **không tìm được** một định nghĩa nguyên văn của ICT cho thuật ngữ này. Các nguồn thứ cấp chỉ có những câu gần nghĩa: ITH/ITL "một khi đã hình thành thì không nên bị vi phạm" (ghi chép tập 12), và "trong cấu trúc tăng, LTL gần nhất không nên bị vi phạm" (bài viết cộng đồng). Hai câu này còn **không khớp nhau** về cấp. Vì vậy định nghĩa ở trên là **quy ước của mình**, chọn vì nó kiểm chứng được.

### 14.3 Cấp độ ≠ protected

![[AMS-v2-15-Cap-Do-Khac-Protected.svg|960]]
*Hình AMS-v2-15 — Ô A: một ITL đúng luật nhưng cú bật từ nó không vượt được đỉnh nào → không protected, rồi bị thủng. Ô B: các đáy chỉ là STL nhưng mỗi cái đều đẩy giá vượt đỉnh → đáy mới nhất là protected low của cấp ngắn hạn.*

| Câu hỏi | Trả lời | Lý do |
|---|---|---|
| Mọi ITL đều là protected low? | **Không** | ITL chỉ nói về vị trí. Nếu cú tăng từ nó chưa vượt đỉnh nào thì nó chưa "giữ" cái gì (ô A) |
| Mọi LTL đều là protected low? | **Không** | Xem Hình 22: LTL trong downtrend |
| Điều gì khiến một swing thành protected? | Cú đi từ nó đã **phá được** đỉnh/đáy cùng cấp phía trước | Phải có bằng chứng "đã làm được việc" |
| Xác định dựa trên cấu trúc nào? | Dựa trên **đỉnh** (với protected low) và **đáy** (với protected high) của **cùng cấp** | Mục 12.1 |
| Có bị thay thế không? | **Có.** Mỗi lần giá lập đỉnh mới, protected low dời lên đáy vừa tạo ra cú vượt đó | Hình 13: hai đường ngang |
| Khi protected low bị phá? | Cấu trúc tăng **ở cấp đó** hết hiệu lực. Chưa chắc là giảm — chỉ chắc là "không còn tăng theo định nghĩa" | Cần thêm một đỉnh thấp hơn để gọi là giảm |

**Một STL có thể là protected, một LTL có thể không.** Hai thuộc tính này đo hai thứ khác nhau:

- **Cấp độ** = nó thắng bao nhiêu lớp hàng xóm (vị trí).
- **Protected** = nó có đang giữ một cấu trúc còn hiệu lực không (vai trò).

Trường hợp đáng tin nhất là khi **cả hai trùng nhau**: một ITL vừa đúng vị trí, vừa là nơi cú vượt ITH bắt đầu.

---

## 15. Internal vs External Structure — Cấu trúc trong và ngoài

![[AMS-v2-16-Cau-Truc-Trong-va-Ngoai.svg|960]]
*Hình AMS-v2-16 — Hai mép là ITH và ITL. Mọi STH/STL bên trong hộp xanh là cấu trúc nội bộ.*

**Nói đơn giản:** hãy nghĩ tới một cái sân có hàng rào. Hàng rào trên và hàng rào dưới là **bên ngoài**. Mọi chuyện chạy nhảy trong sân là **bên trong**. Em bé chạy lung tung trong sân không có nghĩa là em đã ra khỏi sân.

- **External structure (ngoài):** hai mép của vùng — một đỉnh và một đáy cấp cao hơn (ví dụ ITH và ITL).
- **Internal structure (trong):** mọi đỉnh/đáy cấp thấp hơn nằm giữa hai mép (STH/STL).

**Ba điều phải nhớ:**

1. **Trong/ngoài luôn tương đối.** ITH–ITL của H1 là "ngoài" đối với các STH/STL của H1, nhưng là "trong" đối với vùng ITH–ITL của D1.
2. **Phá bên trong không phải phá bên ngoài.** Một STL trong hộp bị phá: nội bộ đổi, hai mép còn nguyên.
3. **Liên hệ với liquidity:** lệnh chờ ngoài hai mép là external liquidity; lệnh chờ quanh các đỉnh/đáy nhỏ bên trong (và các khoảng trống giá bên trong) là internal liquidity. Chi tiết ở [[16-Internal-External-Range-Liquidity-IRL-ERL]] và [[12-Dealing-Range]].

---

## 16. Liquidity Relationship — Quan hệ với liquidity

### 16.1 Vì sao một swing low có thể là nơi lệnh tụ lại?

**Nói đơn giản:** ai cũng nhìn thấy cái đáy rõ nhất trên chart. Người đang mua nghĩ: "nếu giá xuống dưới cái đáy kia thì mình sai, mình sẽ bán cắt lỗ ở đó". Người chờ bán nghĩ: "nếu giá thủng cái đáy kia thì mình bán theo". Hai nhóm khác nhau, cùng đặt **lệnh bán chờ** ở ngay dưới một cái đáy.

**[MARKET MECHANICS]** Các lệnh chờ tụ quanh mức giá dễ thấy là hiện tượng có thật. Khi giá chạm tới, các lệnh chờ đó thành lệnh bán thị trường — tức là có **nhiều người sẵn sàng bán** tại đó. Ai muốn **mua số lượng lớn** sẽ tìm được người bán ở đó. Đó là nghĩa của "sell-side liquidity" (SSL) dưới đáy và "buy-side liquidity" (BSL) trên đỉnh.

**[UNKNOWN]** Chart nến **không cho thấy** có bao nhiêu lệnh ở đó, của ai, hay có ai cố ý đẩy giá tới đó không.

### 16.2 Ba tầng

![[AMS-v2-17-Liquidity-Ba-Tang.svg|960]]
*Hình AMS-v2-17 — Chỉ ba đáy chưa bị xuyên qua (h, g, e) còn là nơi lệnh có thể nằm. Các đáy a, b, c, d, f đã bị giá lấy rồi.*

Hai điều rút ra từ hình:

1. **Đáy đã bị xuyên qua thì không còn là mục tiêu.** Trong tám đáy, năm đáy đã bị giá rơi xuyên qua trên đường xuống. Chỉ còn ba.
2. **Ba đáy còn lại xếp thành ba tầng theo cấp:** STL gần nhất, ITL ở dưới, LTL ở dưới cùng.

### 16.3 Sáu câu hỏi trong đề bài

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Vì sao swing low có thể là nơi tập trung liquidity? | Vì nó là mức dễ thấy để đặt lệnh dừng lỗ và lệnh bán theo phá vỡ **[MARKET MECHANICS]** |
| 2 | STL và ITL có khác nhau về liquidity không? | **[HYPOTHESIS]** Hợp lý là có: ITL tồn tại lâu hơn và nhìn thấy được trên khung lớn hơn → nhiều người đặt lệnh quanh nó hơn. Chưa kiểm chứng |
| 3 | LTL có thu hút nhiều người hơn không? | **[HYPOTHESIS]** Hợp lý, cùng lý do. Nhưng "nhiều hơn bao nhiêu" thì không biết |
| 4 | STL bị sweep, ITL còn nguyên? | Liquidity tầng mỏng đã bị lấy. Cấu trúc cấp vừa không đổi. Nếu giá quay lên mạnh → bối cảnh mà mô hình tìm kiếm. Nếu không → có thể đang trên đường xuống ITL (Case D, mục 25) |
| 5 | ITL bị sweep, LTL còn nguyên? | Liquidity tầng giữa đã bị lấy. Cấp vừa đã có đáy thấp hơn (dù chỉ bằng râu). Cần nhìn nến đóng ở đâu để biết quét hay phá |
| 6 | LTL bị sweep? | **Kết luận được:** lệnh chờ dưới đáy lớn nhất của khung đó đã được kích hoạt. **Không kết luận được:** giá sẽ quay lên; xu hướng đã đảo; ai đã mua |

### 16.4 Ba phép "không bằng"

- **Swing low ≠ liquidity pool.** Đáy là **nơi** lệnh có thể tụ. Có tụ thật không thì không biết. Một đáy vô danh giữa vùng đi ngang, trên khung nhỏ, ngoài giờ giao dịch chính → rất có thể chẳng có gì đáng kể.
- **Liquidity sweep ≠ market structure shift.** Sweep nói "lệnh ở đó đã bị lấy". MSS nói "giá đã phá ngược một swing với lực". Sweep thường **đi trước** MSS trong mô hình ICT 2022, nhưng có sweep mà không có MSS là chuyện thường.
- **Liquidity taken ≠ trend reversal.** Lấy liquidity xong giá có thể đi tiếp cùng chiều.

**Relative equal lows/highs:** hai hay nhiều đáy gần bằng nhau. Theo luật chặt, không đáy nào thắng đáy nào → chúng **không lên cấp** được qua nhau. Nhưng **[INTERPRETATION]** chính vì nhiều đáy cùng một mức nên mức đó càng dễ thấy, càng dễ thành nơi lệnh tụ. Đây là ví dụ rõ nhất cho việc **cấp độ thấp nhưng ý nghĩa liquidity có thể cao**. Xem [[19-Liquidity]] và [[20-Liquidity-Sweep]].

---

## 17. BOS / MSS / CHoCH Relationship

### 17.1 Ba cái tên, nói đơn giản

| Tên | Nói đơn giản | Ghi chú nguồn |
|---|---|---|
| **BOS** — Break of Structure | Giá phá một đỉnh/đáy **cùng chiều** xu hướng đang có → xu hướng **tiếp tục** | Thuật ngữ phổ biến trong cộng đồng SMC/ICT. Xem [[05-BOS-Break-of-Structure]] |
| **MSS** — Market Structure Shift | Sau khi lấy liquidity, giá phá **ngược chiều** một swing ngắn hạn **với lực mạnh** → dấu hiệu sớm của đổi hướng ở cấp thấp | Thuật ngữ của ICT. Xem [[21-Market-Structure-Shift]] |
| **CHoCH** — Change of Character | Lần phá ngược chiều **đầu tiên** | Thuật ngữ của cộng đồng SMC, gần nghĩa với MSS. ICT chủ yếu dùng MSS (độ tin cậy: vừa). Xem [[09-Change-of-Character]] |

### 17.2 Phá STL / ITL / LTL thì gọi là gì?

Tên gọi phụ thuộc vào **hai** thứ, không phải một:

- **Chiều** của cú phá so với xu hướng **ở cấp đó** → quyết định là BOS (cùng chiều) hay MSS/CHoCH (ngược chiều).
- **Cấp** của swing bị phá → quyết định sự kiện đó "to" cỡ nào.

| Swing bị phá | Nếu cấp đó đang GIẢM | Nếu cấp đó đang TĂNG |
|---|---|---|
| **STL** | BOS giảm ở cấp ngắn hạn (tiếp diễn nhỏ) | Phá ngược ở cấp ngắn hạn. Là ứng viên MSS **nếu** có đủ bối cảnh. Thường chỉ là nhịp hồi |
| **ITL** | BOS giảm ở cấp trung hạn | Phá ngược ở cấp trung hạn. Cấu trúc tăng trung hạn hết hiệu lực |
| **LTL** | BOS giảm ở cấp dài hạn (Hình 22) | Phá ngược ở cấp dài hạn. Cấu trúc tăng của **khung đó** hỏng |

![[AMS-v2-26-Pha-Cap-Nao-Ket-Luan-Cap-Do.svg|960]]
*Hình AMS-v2-26 — Mỗi lần phá: cái đã đổi, cái chưa đổi, cái không kết luận được.*

**Trả lời trực tiếp:**

- *Phá STL có phải BOS không?* Chỉ khi cấp ngắn hạn đang giảm. Và khi đó nó là BOS **của cấp ngắn hạn**, không phải BOS của xu hướng lớn.
- *Khi nào chỉ là internal break?* Khi swing bị phá nằm **bên trong** hai mép ITH–ITL (hoặc LTH–LTL) hiện tại.
- *Khi nào có ý nghĩa với external structure?* Khi swing bị phá **chính là một mép**.

### 17.3 Phá thật hay chỉ là quét?

![[AMS-v2-18-Sweep-Khac-Break.svg|960]]
*Hình AMS-v2-18 — Ô A: râu chọc qua, nến đóng lại phía trên. Ô B: thân nến đóng dưới và giá ở lại.*

| Dấu hiệu | Nghiêng về **quét** (sweep) | Nghiêng về **phá** (break) |
|---|---|---|
| Nến đóng ở đâu | Đóng **lại** phía trong | Đóng **ngoài** mức |
| Nến tiếp theo | Đi ngược lại ngay | Đi tiếp, hoặc hồi về nhưng không lấy lại được mức |
| Lực (displacement) | Lực xuất hiện ở chiều **ngược** sau khi chọc | Lực xuất hiện ở chiều **phá** |
| Thời gian ở ngoài mức | Rất ngắn | Kéo dài |

- *Phá swing có cần displacement không?* Theo luật vị trí: không — giá đi qua là đi qua. Nhưng **[ICT FRAMEWORK]** MSS theo ICT đòi có lực. Một cú phá lờ đờ, không lực là cú phá **chất lượng thấp**. Xem [[50-Displacement-In-Depth]].
- *Râu xuyên qua và nến đóng xuyên qua có khác nhau không?* **Có, theo quy ước của note:** râu qua rồi đóng lại = **ứng viên quét**; thân đóng qua = **ứng viên phá**. Đây là **kinh nghiệm**, không phải luật tuyệt đối — một nến đóng dưới đáy vẫn có thể bị kéo ngược ở nến sau. **[BACKTEST REQUIRED]**

### 17.4 Sáu ví dụ ngắn

1. **STL bị phá nhưng không có MSS.** Uptrend trên H1. Giá lùi, thủng một H1-STL bằng những nến nhỏ, không lực, không có sweep trước đó. → Chỉ là nhịp hồi sâu thêm. Không gọi là MSS.
2. **STL bị phá và tạo MSS.** Giá chọc lên trên một đỉnh rõ (lấy BSL), rồi **rơi mạnh** bằng nến thân dài, đóng dưới STL gần nhất, để lại khoảng trống giá. → Đủ: sweep + phá ngược + lực. Đây là MSS giảm ở khung đó.
3. **ITL bị phá, LTL vẫn giữ.** Cấp trung hạn hết tăng. Cấp dài hạn chưa đổi. Kỳ vọng hợp lý: giá đang đi tìm liquidity ở tầng dưới, hoặc đang tạo một nhịp điều chỉnh lớn. Không gọi là đảo chiều.
4. **LTL bị phá trong một xu hướng tăng.** Cấu trúc tăng của khung đó hỏng. Việc cần làm: lên khung lớn hơn xem LTL này là gì ở đó (thường chỉ là một STL hoặc ITL).
5. **Giá sweep một swing low rồi đảo chiều.** Hình 24 (Case D). Râu qua, đóng lại, đi lên, lập đỉnh mới.
6. **Giá phá swing low và tiếp tục giảm.** Hình 18, ô B; Hình 19 (Case E).

---

## 18. Structural Evolution — Cấu trúc thay đổi theo thời gian

**Nói đơn giản:** cấu trúc không đứng yên. Mỗi cây nến mới có thể: (a) thêm một đáy/đỉnh mới, (b) lên cấp cho một đáy/đỉnh cũ, hoặc (c) phá một đáy/đỉnh cũ. Tám kịch bản dưới đây là tám kiểu thay đổi.

Một tính chất dễ chịu của luật vị trí: **nhãn đã được xác nhận thì không bao giờ bị "hạ cấp" bởi dữ liệu mới.** Hàng xóm hai bên đã cố định. Một ITL đã xác nhận mãi là ITL. Nó chỉ có thể **bị phá** (giá đi qua nó). Chỉ có nhãn **ứng viên** mới có thể bị hủy.

### Scenario A — Một STL mới hình thành

- **Quan sát được:** một nến có đáy thấp nhất, nến sau đóng với đáy cao hơn.
- **Đọc theo ICT:** có thêm một điểm ở cấp ngắn hạn. So nó với STL trước: cao hơn (HL) hay thấp hơn (LL).
- **Đã đổi:** chuỗi STL dài thêm một phần tử. STL **liền trước** nó giờ có hàng xóm bên phải → có thể vừa được xác nhận là ITL (nếu nó thấp hơn cả hai bên).
- **Chưa đổi:** mọi thứ ở cấp vừa và lớn, trừ trường hợp vừa nêu.
- **Không kết luận được:** rằng giá sẽ đi lên từ đây.

### Scenario B — Một ITL mới được xác nhận

- **Quan sát được:** một STL cao hơn vừa được xác nhận ở bên phải một STL thấp (và bên trái nó đã có STL cao hơn).
- **Đọc theo ICT:** nhịp lùi vừa rồi là một nhịp lùi "cỡ vừa" và nó **đã kết thúc** (ít nhất tạm thời). Có một mép dưới mới để vẽ vùng.
- **Đã đổi:** chuỗi ITL dài thêm. ITL liền trước nó có thể vừa đủ điều kiện thành LTL. Có một tầng SSL mới dưới ITL này.
- **Chưa đổi:** nó chưa phải protected low cho tới khi giá vượt ITH/đỉnh cùng cấp phía trước.
- **Không kết luận được:** rằng xu hướng trung hạn là tăng. Một ITL có thể hình thành giữa downtrend (Hình 22).

### Scenario C — Một LTL mới được xác nhận

- **Quan sát được:** một ITL cao hơn vừa được xác nhận bên phải một ITL thấp (và bên trái đã có ITL cao hơn).
- **Đọc theo ICT:** trên khung này, một đợt điều chỉnh lớn đã có đáy được xác định. Cấp dài hạn có điểm neo mới.
- **Đã đổi:** có điểm neo cho vùng giá lớn nhất của khung. Thường thì lúc này giá **đã đi xa** khỏi LTL.
- **Chưa đổi:** xu hướng của khung lớn hơn. LTL của H1 có thể chỉ là một STL trên D1.
- **Không kết luận được:** rằng đây là "đáy của thị trường".

### Scenario D — Phá STL, ITL còn nguyên

- **Quan sát được:** giá đóng dưới một STL; ITL bên dưới chưa bị chạm.
- **Đọc theo ICT:** thay đổi **nội bộ**. Cấp ngắn hạn có LL.
- **Đã đổi:** xu hướng cấp ngắn hạn (không còn "đáy cao dần").
- **Chưa đổi:** hai mép ITH–ITL; xu hướng cấp trung hạn.
- **Không kết luận được:** đảo chiều. Đây là hình dạng bình thường của một nhịp hồi.

### Scenario E — Phá ITL, LTL chưa bị phá

- **Quan sát được:** giá đóng dưới một ITL; LTL bên dưới còn nguyên.
- **Đọc theo ICT:** cấu trúc cấp trung hạn đổi. Nếu ITL đó là protected low → cấu trúc tăng trung hạn hết hiệu lực.
- **Đã đổi:** mép dưới của vùng; chuỗi ITL có LL; phải vẽ lại vùng trong/ngoài.
- **Chưa đổi:** cấp dài hạn; khung lớn hơn.
- **Không kết luận được:** rằng giá sẽ đi tới LTL. Có thể, nhưng không chắc.

### Scenario F — Phá LTL

- **Quan sát được:** giá đóng dưới đáy lớn nhất của khung đang xem.
- **Đọc theo ICT:** cấu trúc tăng của **khung này** không còn chỗ dựa.
- **Đã đổi:** mọi cấp trên khung này đều đã có đáy thấp hơn.
- **Chưa đổi:** có thể là **tất cả** ở khung lớn hơn, nếu LTL này chỉ là đáy nhỏ ở đó.
- **Không kết luận được:** rằng giá sẽ rơi tiếp. Đáy lớn là nơi nhiều lệnh chờ nhất (giả thuyết) → cũng là nơi một cú quét lớn rồi quay lên có thể xảy ra.

### Scenario G — Các STL đổi liên tục, ITL giữ nguyên

- **Quan sát được:** bên trong vùng, đáy nhỏ lúc cao dần lúc thấp dần; hai mép không bị chạm.
- **Đọc theo ICT:** giá đang giao dịch **trong vùng**. Cấp ngắn hạn "lật qua lật lại".
- **Đã đổi:** chỉ cấu trúc nội bộ.
- **Chưa đổi:** cấu trúc ngoài.
- **Không kết luận được:** hướng thoát khỏi vùng. Người đọc theo từng STL trong giai đoạn này sẽ **đổi ý liên tục** — đó là dấu hiệu đang nhìn sai cấp.

### Scenario H — Khung lớn đổi trong khi khung nhỏ vẫn tiếp diễn

- **Quan sát được:** D1 vừa đóng nến dưới một D1-ITL. Trên M5, giá đang bật lên, tạo đáy cao dần.
- **Đọc theo ICT:** bối cảnh lớn vừa đổi. Cú bật trên M5 là nhịp hồi **bên trong** một cấu trúc D1 đã hỏng.
- **Đã đổi:** nền (D1).
- **Chưa đổi:** cấu trúc M5 — nó tăng thật, nhưng "tăng" của nó giờ có nghĩa khác.
- **Không kết luận được:** rằng M5 tăng nghĩa là D1 "phá giả". Phải chờ D1 tự chứng minh (lấy lại mức đã mất).

![[AMS-v2-19-Case-E-Ba-Bac-Pha-Vo.svg|960]]
*Hình AMS-v2-19 — Scenario D → E → F nối tiếp nhau trên một đường giá. Mỗi vòng tròn rỗng là một lần phá.*

---

## 19. Real-time Identification — Nhận diện trong thời gian thực

### 19.1 Nói đơn giản

Nhìn lại quá khứ thì cái gì cũng rõ. Nhưng lúc đang giao dịch, **bên phải chart là một tờ giấy trắng**.

Em bé đi trên đường và gặp một cái hố rất sâu. Em muốn nói "đây là hố lớn!". Nhưng em **chưa đi tiếp** nên chưa biết các hố phía trước thế nào. Em chỉ được nói: "đây là hố sâu nhất **mình gặp từ nãy đến giờ**".

### 19.2 Từng bước theo thời gian

![[AMS-v2-09-Real-Time-Bon-Thoi-Diem.svg|960]]
*Hình AMS-v2-09 — Bốn ảnh chụp cùng một chart. Vùng xám là phần chưa xảy ra.*

| Thời điểm | Thông tin mới | Cái ta **biết** | Cái ta **chưa được nói** |
|---|---|---|---|
| **A** | Nến sau e đóng cao hơn | e là STL. b là ITL (đã xác nhận từ trước). e thấp hơn d bên trái | e là ITL — chưa có hàng xóm bên phải |
| **B** | f xuất hiện, cao hơn e, được xác nhận | **e là ITL** (d và f đều cao hơn). e thấp hơn ITL bên trái (b) → e là **LTL ứng viên** | e là LTL — bên phải chưa có ITL nào |
| **C** | g xuất hiện, thấp hơn f nhưng trên e | g là STL. g thấp hơn f bên trái → g là **ITL ứng viên**. e vẫn chưa bị chạm | g là ITL; e là LTL |
| **D** | h xuất hiện, cao hơn g, được xác nhận | **g là ITL** → hai ITL hai bên e đều cao hơn → **e là LTL** | — |

### 19.3 Bảng thời điểm xác nhận

| Cấp | Được xác nhận khi nào | Trước đó gọi là gì |
|---|---|---|
| STL | Nến bên phải **đóng** với đáy cao hơn (và không phải inside bar) | "Đáy đang hình thành" / STL ứng viên |
| ITL | STL bên phải được xác nhận **và** cao hơn | ITL ứng viên |
| LTL | ITL bên phải được xác nhận **và** cao hơn | LTL ứng viên |

**Trả lời các câu hỏi trong đề bài:**

- *Có cần chờ swing bên phải không?* **Có.** Không có cách nào khác với luật vị trí.
- *Chưa đủ dữ liệu thì gọi là gì?* **Ứng viên.** Ghi rõ còn thiếu cái gì ("thiếu STL bên phải", "thiếu ITL bên phải").
- *Có nhận diện được ITL ứng viên trước khi xác nhận không?* **Có.** Điều kiện: nó là STL đã xác nhận, thấp hơn STL bên trái, và là STL mới nhất. Lúc đó chỉ còn chờ bên phải.
- *Có dùng được LTL chưa xác nhận để ra quyết định không?* **Được, với ba điều kiện:** (1) gọi đúng tên là ứng viên; (2) điểm sai rất rõ — nếu giá xuống dưới nó thì ứng viên bị hủy; (3) không coi nó chắc chắn hơn một đáy bình thường chỉ vì bạn "cảm thấy" nó sẽ thành LTL. Ghi nhận trung thực: trong thực tế gần như **mọi** quyết định vào lệnh đều dựa trên ứng viên, vì nhãn xác nhận đến quá muộn.

### 19.4 Ba trạng thái của một nhãn

```text
ỨNG VIÊN ──(hàng xóm bên phải xác nhận, cao hơn)──► ĐÃ XÁC NHẬN ──(giá đi qua)──► ĐÃ BỊ PHÁ
    │
    └──(xuất hiện đáy thấp hơn trước khi kịp xác nhận)──► HỦY (đáy mới thành ứng viên)
```

> [!warning] Quy tắc chống hindsight
> Khi backtest hoặc xem lại chart cũ, **che phần bên phải** thời điểm quyết định. Chỉ được dùng nhãn nào **đã xác nhận tại thời điểm đó**. Nếu một setup chỉ "đẹp" khi đáy đã mang nhãn LTL, và nhãn LTL chỉ có sau khi giá đã chạy — thì setup đó **không tồn tại** trong real-time.

---

## 20. Multi-Timeframe Application — D1 → H1 → M5

### 20.1 Điều phải hiểu trước: "lên một cấp" và "lên một khung" giống nhau nhưng không phải một

Có hai cách để nhìn thấy "đáy to hơn":

- **Lên một cấp** trên cùng khung: từ H1-STL lên H1-ITL.
- **Lên một khung**: từ H1 lên D1 và nhìn D1-STL.

**[INTERPRETATION]** Hai cách này thường chỉ vào **gần cùng một chỗ**: một D1-STL thường hiện ra trên H1 như một H1-ITL hoặc H1-LTL. Nhưng **không khớp một-một**, vì nến D1 cắt thời gian theo giờ đóng cửa chứ không theo hình dạng giá.

**Quy ước của note:** phân loại **riêng** trên từng khung. Mỗi nhãn **bắt buộc** kèm tên khung: `D1-ITL`, `H1-STL`, `M5-STH`. Không bao giờ viết trống "ITL".

### 20.2 D1 — bối cảnh

| Dùng D1 để xác định | Bằng cái gì |
|---|---|
| Hướng lớn | Chuỗi D1-STL/STH gần đây và chuỗi D1-ITL/ITH |
| Vùng giá lớn (dealing range) | D1-ITH và D1-ITL gần nhất (hoặc LTH–LTL nếu có) |
| Liquidity lớn | Các D1-STL/ITL **chưa bị xuyên qua** phía dưới; D1-STH/ITH phía trên |
| Điểm sai của cả kịch bản | D1 protected low/high |

- *D1-STL nghĩa là gì?* Đáy của một ngày mà ngày trước và ngày sau đều có đáy cao hơn. Trên M5 đó đã là một đáy rất lớn.
- *D1-ITL nghĩa là gì?* Đáy của một nhịp điều chỉnh kéo dài nhiều ngày đến vài tuần.
- *D1-LTL nghĩa là gì?* Đáy của một đợt điều chỉnh nhiều tuần đến nhiều tháng. **Hiếm.** Trên một chart D1 một năm có thể chỉ có một hai cái, hoặc không có.
- *Khi nào D1 thật sự đổi cấu trúc?* Khi nến D1 **đóng** qua D1 protected low/high. (Quy ước; **[BACKTEST REQUIRED]** để so với "chỉ cần râu chạm".)
- *Khi nào chỉ là dao động nội bộ?* Khi mọi thứ xảy ra **giữa** D1-ITH và D1-ITL hiện tại.

### 20.3 H1 — setup

| Dùng H1 để xác định | Bằng cái gì |
|---|---|
| Nhịp hiện tại bên trong D1 | Chuỗi H1-ITL/ITH |
| Vùng làm việc | H1-ITH và H1-ITL gần nhất |
| Liquidity đang được "xây" | H1-STL/STH chưa bị xuyên, relative equal lows/highs trên H1 |
| Setup đang hình thành | Giá tiến về POI của D1; H1 có dấu hiệu cạn lực |

- *H1 liên hệ với D1 thế nào?* H1 là hình ảnh phóng to của **vài cây nến D1 gần nhất**.
- *H1 có thể giảm trong khi D1 vẫn tăng không?* **Có, và đó là chuyện bình thường.** Một nhịp hồi của D1 **chính là** một xu hướng giảm trên H1 (Hình 20).
- *H1-STL bị phá có ảnh hưởng đến D1 bias không?* **Không.**
- *Khi nào H1 giảm chỉ là pullback của D1?* Khi giá vẫn **ở trên** D1 protected low.
- *Khi nào H1 bắt đầu báo hiệu D1 có thể đổi?* Có một dấu hiệu sớm và một dấu hiệu quyết định. **Sớm:** chuỗi H1-ITH thấp dần kéo dài, và mỗi lần giá tới POI tăng của D1 đều không bật được. **Quyết định:** giá đóng dưới mức D1 protected low. Chỉ dấu hiệu thứ hai mới **đổi** D1; dấu hiệu thứ nhất chỉ là lý do để thận trọng.

### 20.4 M5 — vào lệnh

| Dùng M5 để xác định | Bằng cái gì |
|---|---|
| Liquidity sweep | Râu chọc qua một H1-STL / M5-ITL rồi đóng lại |
| MSS | Giá phá ngược một M5-STH/STL với lực |
| Displacement, FVG | Nến thân dài, để lại khoảng trống giá |
| Điểm dừng lỗ | Dưới/trên đáy/đỉnh M5 vừa tạo ra cú quét |

> [!danger] Lỗi số một ở khung M5
> **Không được nhầm một cú phá cấu trúc trên M5 với sự thay đổi cấu trúc của H1 hay D1.** Một M5-MSS chỉ nói: "cấu trúc **M5** vừa đổi". Nó là **cò súng**, không phải **bản đồ**.

### 20.5 Hai ví dụ dựng

![[AMS-v2-20-Case-C-D1-H1-M5-Nhip-Hoi.svg|960]]
*Hình AMS-v2-20 — D1 tăng. H1 giảm (đó là nhịp hồi của D1). M5 vừa quét đáy nhỏ và vượt đỉnh nhỏ. Ba khung, ba câu trả lời, không mâu thuẫn.*

![[AMS-v2-21-M5-Giam-Trong-Khi-H1-D1-Tang.svg|960]]
*Hình AMS-v2-21 — Ví dụ đề bài yêu cầu: M5 chuyển giảm trong khi H1 và D1 vẫn tăng.*

Cách nói đúng cho Hình 21: *"M5 đang giảm bên trong một nhịp tăng H1, bên trong một xu hướng tăng D1."* Ba mệnh đề, ba khung, ba cấp độ:

- **Cục bộ (M5):** đã đổi sang giảm.
- **Trung gian (H1):** chưa đổi — H1-STL gần nhất còn nguyên.
- **Khung lớn (D1):** không có gì xảy ra.

Bán theo M5 ở đây là bán **ngược** hai khung lớn hơn. Có thể vẫn có lãi, nhưng đó là một loại lệnh khác, cần được ghi là "countertrend" và kiểm chứng riêng.

Xem thêm: [[32-Top-down-Analysis-Multiple-Timeframes]], [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]], [[59-Daily-Bias]].

---

## 21. Common Misunderstandings — 15 hiểu lầm phổ biến

| # | Hiểu lầm | Vì sao sai | Hiểu đúng | Xem hình |
|---|---|---|---|---|
| 1 | Mọi chỗ giá thấp đều là STL | Thiếu nến bên phải đã đóng thì chưa có "đáy" | STL cần nến hai bên đều có đáy cao hơn, nến phải đã đóng | 03 |
| 2 | Nhầm STL với ITL | Chỉ thắng một bên hàng xóm, hoặc so với nến thay vì so với STL | ITL = STL thấp hơn **hai STL** hai bên | 04 |
| 3 | Nhầm ITL với LTL | Thấy nó thấp nhất màn hình nên gọi "long-term" | LTL = ITL thấp hơn **hai ITL** hai bên; thiếu bên phải → ứng viên | 05, 23C |
| 4 | Phân loại theo độ lớn của swing | Một cú rơi dài vẫn có thể dừng ở trên đáy bên trái | Cấp độ là chuyện **vị trí so với hàng xóm**, không phải kích thước | 23B |
| 5 | LTL luôn là đáy dài hạn của thị trường | LTL là nhãn trên **một khung**; và nó vẫn bị phá được | LTL = đáy lớn nhất của một vùng, trên khung đang xem | 22 |
| 6 | Mọi ITL đều là protected low | Vị trí ≠ vai trò | Protected khi cú tăng từ nó đã vượt đỉnh cùng cấp | 15 |
| 7 | Phá STL = đảo chiều | STL bị phá trong mọi nhịp hồi bình thường | Phá STL = cấp ngắn hạn đổi. Chỉ vậy | 26 |
| 8 | Phá ITL = đảo chiều khung lớn | ITL của H1 có thể là chuyện nội bộ của D1 | Phá ITL = cấp trung hạn **của khung đó** đổi | 19, 20 |
| 9 | Không phân biệt trong và ngoài | Coi mọi cú phá đều "to" như nhau | Hỏi: swing bị phá nằm trong hộp hay là mép hộp? | 16 |
| 10 | Không chờ swing được xác nhận | Đáy đang chạy có thể còn rơi | Nến chưa đóng → chưa chấm | 03② |
| 11 | Dùng hindsight để phân loại | Nhãn LTL chỉ có sau khi giá đã chạy xa | Che phần bên phải; chỉ dùng nhãn có tại thời điểm đó | 08, 09 |
| 12 | Đổi cấu trúc liên tục theo từng dao động nhỏ | Đang đọc cấp ngắn hạn mà tưởng là cấp vừa | Cấu trúc cấp vừa chỉ đổi khi ITL/ITH bị phá | Scenario G |
| 13 | Nhầm sweep với structural break | Râu chọc qua ≠ giá ở lại bên kia | Nhìn chỗ nến đóng và nến tiếp theo | 18 |
| 14 | Nhầm BOS với MSS | Cùng là "phá" nhưng khác chiều so với xu hướng | BOS = cùng chiều (tiếp diễn). MSS = ngược chiều + có lực + sau sweep | mục 17 |
| 15 | Mang thứ bậc của M5 áp lên D1 | M5-LTL có thể không nhìn thấy nổi trên D1 | Mỗi khung phân loại riêng; nhãn luôn kèm tên khung | 21 |

---

## 22. Edge Cases — 12 trường hợp khó

![[AMS-v2-23-Ba-Truong-Hop-Kho.svg|960]]
*Hình AMS-v2-23 — Ba trong số các trường hợp khó: hai đáy bằng nhau, rơi sâu nhưng không lên cấp, và đáy sâu nhất ở mép phải.*

**1. Hai STL rất gần nhau.**
*Phân loại:* cả hai là STL nếu mỗi cái đủ điều kiện ba-nến. *Chuyện gì xảy ra:* giá chạm đáy, nhích lên một hai nến, chạm lại. *Đọc:* nếu bằng nhau → vùng relative equal lows, không cái nào lên cấp qua cái kia. Nếu lệch → cái thấp hơn có cơ hội lên cấp. *Kết luận được:* có một mức dễ thấy. *Không kết luận được:* mức đó sẽ giữ.

**2. Một STL không có displacement rõ ràng.**
*Phân loại:* vẫn là STL — luật không đòi lực. *Đọc:* đáy "lờ đờ" là đáy chất lượng thấp về mặt ý nghĩa; giá rời đi chậm cho thấy không có lực mua rõ. *Kết luận được:* nó tồn tại và có thể được dùng làm hàng xóm khi phân loại. *Không kết luận được:* nó đáng làm chỗ dựa.

**3. Một swing low rất sâu nhưng không thành ITL.**
Hình 23, ô B và ô C. *Vì sao:* hoặc nó vẫn cao hơn đáy bên trái, hoặc bên phải nó có đáy thấp hơn, hoặc bên phải chưa có gì. *Bài học:* độ sâu của cú rơi không quyết định cấp.

**4. Một ITL nằm trong vùng đi ngang.**
*Phân loại:* ITL hợp lệ. *Đọc:* thường là cú chọc thủng mép dưới của vùng. *Kết luận được:* SSL dưới các đáy nhỏ trước đó đã bị lấy. *Không kết luận được:* vùng đi ngang sẽ thoát lên.

**5. Một ITL bị phá nhưng LTL còn nguyên.**
Scenario E. Cấp vừa đổi, cấp lớn chưa.

**6. Một LTL mới hình thành nhưng xu hướng lớn vẫn giảm.**
Hình 22. Nhãn đúng, kỳ vọng sai.

**7. Một STL bị sweep rồi giá tăng mạnh.**
Hình 24 (Case D). *Kết luận được:* liquidity tầng mỏng bị lấy; cấp vừa không đổi. *Không kết luận được:* ý định của ai đó.

**8. Giá tạo nhiều STL liên tiếp nhưng không hình thành ITL.**
Hình 10, ô A. Xu hướng một chiều sạch. *Hệ quả thực tế:* không có ITL mới → protected low phải lấy từ cấp ngắn hạn, hoặc chấp nhận điểm sai ở xa.

**9. Giá phá STL và ITL gần như đồng thời.**
*Chuyện gì xảy ra:* một nến dài (thường do tin) đóng dưới cả hai. *Đọc:* ghi nhận sự kiện ở **cấp cao nhất** bị phá (ITL). STL không cần ghi riêng. *Không kết luận được:* giá sẽ đi tiếp — nến tin thường bị kéo lại một phần.

**10. Giá tạo đáy mới nhưng cấu trúc lớn chưa đổi.**
Đáy mới thấp hơn STL trước nhưng vẫn trên ITL. Đây là Scenario D. "Đáy mới" phải luôn đi kèm câu hỏi: **mới so với cấp nào?**

**11. H1 tăng nhưng M5 giảm.** Hình 21.

**12. D1 giảm nhưng H1 tăng.**
Soi gương của Hình 20. H1 tăng là nhịp hồi lên của D1. *Kết luận được:* H1 đang đi về phía đỉnh/POI giảm của D1. *Không kết luận được:* D1 đã đổi — chỉ đổi khi D1 protected high bị vượt.

**Thêm hai trường hợp về dữ liệu (giữ lại từ bản v1 vì có thật):**

- **Nguồn dữ liệu khác nhau cho nhãn khác nhau.** Giờ đóng nến D1 khác nhau giữa các broker, và râu nến trên CFD có thể không tồn tại trên futures. Cùng một thị trường, hai nguồn, hai bộ D1-STL. → Chốt **một** nguồn để chấm cấu trúc: nguồn mà mình thực sự đặt lệnh.
- **Nến Chủ nhật / nến phiên ngắn.** Một nến D1 ngắn bất thường có thể tạo ra STL "giả" hoặc xóa mất một STL thật. → Ghi rõ quy ước xử lý trong backtest.

---

## 23. Counterexamples — Khi khung này cho tín hiệu sai

Một khung không giải thích được thất bại của chính nó là khung chưa hoàn chỉnh. Sáu kiểu thất bại:

| # | Tình huống | Khung nói gì | Thực tế | Bài học |
|---|---|---|---|---|
| 1 | LTL trong downtrend (Hình 22) | "Đây là đáy lớn" | Bị phá sau một cú bật | Nhãn vị trí không hứa gì về tương lai |
| 2 | ITL không protected (Hình 15A) | "Đây là đáy vừa" | Cú bật yếu, rồi thủng | Luôn kiểm tra thêm: nó đã vượt đỉnh nào chưa? |
| 3 | Xu hướng sạch (Hình 10A) | Không có ITL nào để nói | Xu hướng rất khỏe | Hệ thống ba cấp "im lặng" khi thị trường đi một mạch |
| 4 | Sweep không đảo chiều | "Liquidity đã bị lấy → chờ quay đầu" | Giá hồi nhẹ rồi rơi tiếp qua ITL | Sweep là điều kiện cần của mô hình, không phải điều kiện đủ |
| 5 | Nến đóng dưới ITL rồi bị kéo ngược | "Cấu trúc đã đổi" | Nến sau lấy lại toàn bộ | Quy ước "thân đóng = phá" vẫn sai được; cần nến tiếp theo |
| 6 | Vùng đi ngang chặt, ít biến động | Rất nhiều STL, vài ITL | Tất cả là nhiễu | Luật áp vào đâu cũng ra nhãn. Nhãn không tự mang ý nghĩa |

Thất bại số 6 nối lại với cảnh báo ở mục 3.3: **một đường ngẫu nhiên cũng có đủ STL, ITL, LTL.**

---

## 24. Practical Chart-Reading Framework — Quy trình đọc chart

### 24.1 Đánh giá quy trình trong đề bài

Quy trình đề bài đưa ra bắt đầu bằng *"Identify Market Direction"*. **Đây là chỗ cần sửa.**

- **Giả định:** biết hướng trước, rồi mới chấm swing.
- **Vấn đề:** hướng **là kết quả** của việc đọc các swing. Xác định hướng trước rồi mới phân loại là lý luận vòng tròn, và nó khiến mắt ta "chọn" những swing hợp với hướng đã nghĩ sẵn.
- **Sửa:** bước đầu tiên là **chọn khung**. Hướng xuất hiện ở bước 6, sau khi đã phân loại xong.

Hai bổ sung nữa: thêm bước **"đánh dấu mép phải"** (để không vô thức nâng cấp ứng viên), và tách **protected** thành bước riêng sau khi đã đọc hướng.

### 24.2 Quy trình mười bước (v2.0)

![[AMS-v2-25-Quy-Trinh-Muoi-Buoc.svg|960]]
*Hình AMS-v2-25 — Mười bước. Mỗi ô có một câu "dừng lại nếu…".*

| Bước | Quan sát gì | Vì sao | Điều kiện xác nhận | Lỗi hay gặp | Khi nào KHÔNG kết luận |
|---|---|---|---|---|---|
| 1. Chọn một khung | Tên khung (D1/H1/M5), tải đủ lịch sử về bên trái | Nhãn chỉ có nghĩa trong một khung | Đã ghi tên khung lên chart | Chấm H1 rồi vô thức nhìn sang M5 | Khi chưa đủ lịch sử để có hàng xóm bên trái |
| 2. Chấm STL/STH | Mọi đáy/đỉnh ba-nến | Đây là viên gạch của cả hệ thống | Nến phải đã đóng, không phải inside bar | Chấm nến đang chạy; bỏ sót đáy nhỏ làm sai hàng xóm | Nến chưa đóng |
| 3. Tìm ITL/ITH | So mỗi STL với hai STL liền kề | Lọc ra các nhịp lùi cỡ vừa | Cả hai hàng xóm đã xác nhận và "kém hơn" | So với STL xa thay vì STL **liền kề** | Thiếu một bên → ghi "ứng viên" |
| 4. Tìm LTL/LTH | So mỗi ITL với hai ITL liền kề | Tìm điểm neo lớn nhất của khung | Cả hai ITL hàng xóm đã xác nhận | Gọi đáy thấp nhất màn hình là LTL | Không có LTL nào cũng là kết quả hợp lệ |
| 5. Đánh dấu mép phải | Đáy/đỉnh mới nhất ở mỗi cấp | Chống hindsight ngay trên chart | Mỗi ứng viên có ghi "còn thiếu gì" | Nâng cấp theo cảm giác | — |
| 6. Đọc hướng từng cấp | Chuỗi cùng cấp cao dần hay thấp dần | Mỗi cấp có xu hướng riêng | Ít nhất hai đỉnh và hai đáy cùng cấp để so | Trộn STL với ITL trong một chuỗi | Chuỗi lẫn lộn → ghi "không rõ" |
| 7. Tìm swing giữ cấu trúc | Đáy nào đã đẩy giá vượt đỉnh cùng cấp | Đây là điểm sai của kịch bản | Có nến **đóng** vượt đỉnh | Coi mọi ITL là protected | Chưa có cú vượt nào → chưa có protected |
| 8. Trong/ngoài + liquidity | Hai mép; đáy/đỉnh nào chưa bị xuyên | Biết giá đang ở đâu và có thể đi đâu | Mép là swing cấp cao hơn đã xác nhận | Vẽ liquidity dưới đáy đã bị lấy | Vùng quá hẹp, toàn nhiễu |
| 9. Theo dõi phá vỡ | Râu hay thân; cấp nào; có lực không | Phân biệt quét với phá | Nến đóng + hành vi nến sau | Kết luận ngay trên nến đang chạy | Chỉ mới một nến |
| 10. Ghép ba khung | D1 → H1 → M5 | Cùng một cú phá có nghĩa khác nhau ở từng khung | Mỗi nhãn có tên khung | Để M5 cãi lại D1 | Ba khung mâu thuẫn mà không giải thích được → đứng ngoài |

### 24.3 Sơ đồ quyết định khi một đáy bị xuyên qua

```text
Giá vừa đi xuống dưới một cái đáy
│
├─ Đáy đó thuộc khung nào, cấp nào?        → ghi: ví dụ "H1-STL"
│
├─ Nến ĐÃ đóng chưa?
│    └─ CHƯA → chờ. Không kết luận.
│
├─ Nến đóng ở đâu?
│    ├─ Đóng LẠI phía trên đáy → "ứng viên QUÉT"
│    │     └─ Nến sau có đi lên với lực không?
│    │           ├─ CÓ  → quét được xác nhận. Cấu trúc cấp đó CHƯA đổi.
│    │           └─ KHÔNG → chưa rõ. Tiếp tục theo dõi.
│    │
│    └─ Đóng DƯỚI đáy → "ứng viên PHÁ"
│          └─ Nến sau có lấy lại được mức không?
│                ├─ CÓ  → phá thất bại. Xem lại như một cú quét sâu.
│                └─ KHÔNG → phá được xác nhận Ở CẤP ĐÓ.
│                      └─ Đáy đó có phải protected low không?
│                            ├─ CÓ  → cấu trúc tăng ở cấp đó hết hiệu lực.
│                            └─ KHÔNG → chỉ là một đáy thấp hơn. Xem cấp cao hơn còn nguyên không.
│
└─ Cuối cùng: lên một khung, hỏi lại "ở khung lớn hơn, chuyện này là gì?"
```

---

## 25. Case Studies — Năm ví dụ dựng

> [!note] Tất cả là ví dụ dựng
> Năm case dưới đây là **đường giá vẽ tay** để minh họa luật. Chúng không phải dữ liệu thị trường thật và **không chứng minh** điều gì về xác suất. Mỗi case được kể theo thứ tự thời gian (T0, T1, …) và chỉ dùng thông tin có tại thời điểm đó.

### Case A — Cấu trúc tăng rõ ràng (Hình 13)

- **T0.** Giá đang giảm. Trong nhịp giảm có một ITL (vòng xanh ngoài cùng bên trái): nó được hai đáy nhỏ cao hơn kẹp hai bên. Rồi nó bị phá. → Ngay từ đầu đã thấy: ITL trong downtrend không giữ.
- **T1.** Giá in ra một đáy rất sâu rồi bật lên. Lúc này nó chỉ là **STL**, và là "ITL ứng viên".
- **T2.** Các đáy nhỏ cao dần xuất hiện bên phải → đáy sâu được xác nhận là **ITL**. Vì ITL bên trái cao hơn nó → **LTL ứng viên**.
- **T3.** Một nhịp lùi sâu hơn bình thường tạo ra đáy mới (ITL thứ nhất), vẫn ở **trên** đáy sâu. Giá bật lên và **vượt ITH** trước đó.
- **T4.** Một đáy nhỏ cao hơn xuất hiện → ITL thứ nhất được **xác nhận**. Cùng lúc: đáy sâu có ITL cao hơn ở cả hai bên → **LTL được xác nhận**. *Chú ý: lúc này giá đã ở rất xa LTL.*
- **T5.** Giá lập đỉnh mới, rồi lùi sâu, thủng hai đáy nhỏ (Scenario D, hai lần) nhưng dừng **trên** ITL thứ nhất. Protected low **giữ**. Giá bật lên, vượt ITH thứ hai → đáy của nhịp lùi này thành ITL thứ hai và protected low **dời lên** đó.

**Phân loại cuối:** một LTL; hai ITL cao dần sau LTL; hai ITH cao dần; chưa có LTH. Cấp vừa: tăng. Protected low: ITL thứ hai.

### Case B — Cấu trúc giảm rõ ràng (Hình 14)

Soi gương Case A. Điểm đáng chú ý: **LTH được xác nhận muộn** — chỉ khi ITH thứ nhất (thấp hơn) đã được xác nhận. Protected high dời **xuống** mỗi lần giá thủng ITL.

### Case C — Nhịp hồi bên trong xu hướng khung lớn (Hình 20)

- **D1:** đáy cao dần, đỉnh cao dần. Giá đang lùi từ đỉnh, **chưa** thủng D1-STL gần nhất. → D1 tăng, không có gì đổi.
- **H1:** phóng to phần đang lùi. Đỉnh thấp dần, đáy thấp dần. → H1 **giảm**. Đây không mâu thuẫn với D1; đây **là** nhịp hồi của D1 nhìn gần.
- **M5:** ở cuối nhịp giảm H1, giá chọc xuống dưới một M5-STL rồi bật lên vượt M5-STH. → Cấu trúc **M5** vừa đổi sang tăng.

| Cấp | Đang đổi? | Bằng chứng |
|---|---|---|
| M5 (cục bộ) | **Có** — vừa chuyển tăng | Quét M5-STL, vượt M5-STH |
| H1 (trung gian) | **Chưa** — vẫn giảm | Chưa H1-STH nào bị vượt |
| D1 (bối cảnh) | **Không** — vẫn tăng | D1-STL gần nhất còn nguyên |

**[HYPOTHESIS]** M5 quay đầu cùng chiều D1 ở cuối một nhịp hồi H1 là bối cảnh mà ICT 2022 Model tìm kiếm. Nó có lợi thế thật hay không: **[BACKTEST REQUIRED]**.

### Case D — Quét STL, ITL và LTL còn nguyên (Hình 24)

![[AMS-v2-24-Case-D-Quet-STL.svg|960]]
*Hình AMS-v2-24 — Giá chọc nhẹ xuống dưới một STL rồi lập đỉnh mới. ITL ở xa bên dưới không bị chạm.*

- **T0.** Có một ITL (đã xác nhận) và phía trên nó là các STL cao dần. Giá đang lập đỉnh mới.
- **T1.** Giá lùi và đi xuống **dưới** STL gần nhất một chút.
- **T2.** Giá quay lên và lập đỉnh cao hơn.

| | |
|---|---|
| **Quan sát được** | Giá xuống dưới một STL một chút, rồi quay lên lập đỉnh mới |
| **Đọc theo ICT** | SSL dưới STL bị lấy. Cấp trung hạn (ITL) không đổi |
| **Đã đổi** | Cấp ngắn hạn có một đáy thấp hơn. Đáy vừa chọc xuống trở thành STL mới |
| **Chưa đổi** | ITL, LTL, xu hướng trung hạn |
| **Không kết luận được** | "Ai đó cố ý săn stop". Chart không cho biết danh tính hay ý định |

### Case E — Khả năng đảo chiều cấu trúc: phá STL → ITL → LTL (Hình 19)

- **T0.** Cấu trúc tăng: LTL ở dưới cùng, ITL ở giữa, STL gần đỉnh. Giá vừa lập đỉnh.
- **T1 — ① thủng STL.** Giá đóng dưới STL gần nhất. *Đã đổi:* cấp ngắn hạn. *Chưa đổi:* ITL, LTL. *Tại thời điểm này* không thể phân biệt với một nhịp hồi bình thường.
- **T2.** Giá bật lên nhưng **không vượt được đỉnh**, tạo đỉnh thấp hơn. Lúc đỉnh thấp hơn này được xác nhận, đỉnh cũ trở thành **ITH**. Cấp ngắn hạn giờ có cả LL lẫn LH → ngắn hạn **giảm**.
- **T3 — ② thủng ITL.** Giá rơi mạnh, đóng dưới ITL. *Đã đổi:* cấp trung hạn; nhịp tăng gần nhất hết hiệu lực. *Chưa đổi:* LTL.
- **T4.** Giá hồi lên yếu, dừng rất xa dưới đỉnh thấp trước đó.
- **T5 — ③ thủng LTL.** Giá đóng dưới LTL. Mọi cấp trên khung này đều đã có đáy thấp hơn.

**Kết luận được:** cấu trúc tăng của **khung này** đã hỏng, theo từng tầng. **Không kết luận được:** khung lớn hơn đã đảo chiều; giá sẽ rơi tiếp. Bước tiếp theo bắt buộc: lên một khung và hỏi "LTL vừa vỡ là gì ở khung đó?".

**Bài học về thời điểm:** người chờ ③ mới tin thì đã rất muộn. Người hành động ở ① thì sai rất nhiều lần (vì ① xảy ra trong mọi nhịp hồi). Không có điểm nào "đúng" tuyệt đối — đây là đánh đổi giữa **sớm** và **chắc**, và chỉ backtest mới cho biết điểm nào hợp với mình.

---

## 26. What We Actually Know vs What We Assume

### 26.1 Bảng tổng hợp

| Nhận định | Phân loại | Điều ta thật sự biết |
|---|---|---|
| STL là đáy ba-nến | **[ICT FRAMEWORK]** — định nghĩa | Rõ ràng, kiểm tra được trên nến. Gốc từ Larry Williams |
| ITL là STL có STL cao hơn hai bên | **[ICT FRAMEWORK]** — định nghĩa | Khớp giữa Williams và đa số tài liệu ICT. Ghi chép tập 12 thêm chữ "thường" |
| LTL là ITL có ITL cao hơn hai bên | **[ICT FRAMEWORK]** — định nghĩa | Điểm các nguồn đồng ý nhất |
| ITH/ITL hình thành khi giá lấp FVG | **[ICT FRAMEWORK — nguồn thứ cấp]** | Có trong ghi chép tập 12. Chưa đối chiếu bản gốc. Có thể mâu thuẫn với luật vị trí |
| Giá gấp khúc ở mọi cỡ | **[MARKET MECHANICS]** | Quan sát được trên mọi chart |
| Thứ bậc swing chứng tỏ thị trường có trật tự | **Không được ủng hộ** | Đường ngẫu nhiên cũng có đủ ba cấp |
| Lệnh chờ tụ quanh đỉnh/đáy dễ thấy | **[MARKET MECHANICS]** | Hợp lý và được ghi nhận rộng rãi; không đo được từ chart nến |
| Đáy cấp cao có nhiều liquidity hơn | **[HYPOTHESIS]** | Hợp lý. Chưa kiểm chứng |
| Phá STL nghĩa là đảo chiều | **Sai nếu nói chung** | STL bị phá trong mọi nhịp hồi |
| Phá ITL đổi cấu trúc cấp cao hơn | **Tùy bối cảnh** | Đổi cấp trung hạn **của khung đó**. Không nói gì về khung lớn hơn |
| Mọi ITL là protected low | **Không được ủng hộ** | Vị trí ≠ vai trò (Hình 15A) |
| LTL luôn đánh dấu đáy lớn của thị trường | **Không được ủng hộ** | Phản ví dụ: Hình 22 |
| ITH/ITL "một khi hình thành thì không nên bị vi phạm" | **[ICT FRAMEWORK — nguồn thứ cấp] + [BACKTEST REQUIRED]** | Là một nhận định về hành vi. Chưa có số liệu |
| "Protected high/low" là thuật ngữ gốc của ICT | **Chưa xác minh** | Không tìm được định nghĩa nguyên văn |
| Thân đóng qua = phá thật; râu qua = quét | **Heuristic** | Quy ước hữu ích; vẫn sai được |
| Ai đó cố ý đẩy giá tới đáy để lấy stop | **[SPECULATIVE]** | Chart không cho biết danh tính hay ý định |

### 26.2 Năm giả định bị phản biện

**Giả định 1 — "Swing cấp cao thì quan trọng hơn."**
*Vấn đề:* "quan trọng" chưa được định nghĩa. *Quan sát được:* swing cấp cao thắng nhiều lớp hàng xóm hơn và tồn tại lâu hơn. *Theo ICT:* nó là điểm neo cấu trúc và nơi liquidity lớn. *Giải thích khác:* nó đơn giản là điểm cực trị của một cửa sổ rộng hơn — điều mà đường ngẫu nhiên cũng có. *Hệ quả thực tế:* dùng nó làm **địa chỉ** và **điểm sai**; đừng coi nó là **dự báo**.

**Giả định 2 — "Phá cấp cao thì có nghĩa hơn phá cấp thấp."**
*Vấn đề:* nghe hợp lý nhưng chưa đo. *Quan sát được:* phá cấp cao hiếm hơn và cần giá đi xa hơn. *Giải thích khác:* vì giá phải đi xa hơn mới phá được nên dĩ nhiên trông "to" hơn — đó là hệ quả của định nghĩa, chưa chắc là thông tin mới. *Hệ quả:* **[BACKTEST REQUIRED]** — đếm: sau khi phá ITL, giá đi tiếp bao xa so với sau khi phá STL, tính theo biến động chung.

**Giả định 3 — "Chờ xác nhận thì an toàn hơn."**
*Vấn đề:* xác nhận cấp cao đến rất muộn; lúc đó điểm vào đã xa và điểm sai đã rộng. *Hệ quả:* "an toàn hơn" về nhãn không có nghĩa là "tốt hơn" về kết quả. Đây là đánh đổi, không phải chân lý.

**Giả định 4 — "Ba cấp là con số tự nhiên."**
*Vấn đề:* không có gì trong thị trường nói rằng có đúng ba cấp. Luật đệ quy có thể chạy tiếp lên cấp bốn, cấp năm. Ba là một lựa chọn tiện dụng. *Hệ quả:* nếu ba cấp trên một khung không đủ, **lên khung** thay vì bịa thêm cấp.

**Giả định 5 — "Hai người chấm sẽ ra cùng kết quả."**
*Vấn đề:* chỉ đúng nếu cả hai dùng **cùng** quy ước cho inside bar, đáy bằng nhau, nguồn dữ liệu, và lịch sử tải về. *Hệ quả:* ghi các quy ước đó ra (mục 5.5) trước khi backtest.

---

## 27. Final Mental Model

![[AMS-v2-27-Mental-Model-Cuoi.svg|960]]
*Hình AMS-v2-27 — Năm câu để mang theo.*

1. **Mọi đáy bắt đầu là đáy nhỏ.** STL là viên gạch. ITL và LTL là STL được lên cấp.
2. **Lên cấp = thấp hơn hàng xóm cùng cấp ở hai bên.** Không do rơi sâu bao nhiêu, không do mất bao lâu.
3. **Cấp càng cao, biết càng muộn.** Mép phải luôn là ứng viên.
4. **Cấp độ ≠ protected ≠ liquidity ≠ đảo chiều.** Bốn câu hỏi, trả lời riêng.
5. **Phá cấp nào, kết luận cấp đó — luôn kèm tên khung.**

Và một câu cho trẻ 5 tuổi: *"Hố to là cái hố nhỏ sâu hơn các bạn hàng xóm của nó — và em chỉ biết chắc điều đó sau khi đã đi qua và nhìn thấy các hố phía trước."*

---

## 28. Practical Checklist

### A. Trước khi chấm
- [ ] Đã chọn **một** khung và ghi tên khung
- [ ] Đã tải đủ lịch sử về bên trái
- [ ] Đã chốt nguồn dữ liệu (cùng nguồn với nơi đặt lệnh)

### B. Chấm ba cấp
- [ ] Mọi STL/STH đều có nến phải **đã đóng**
- [ ] Mỗi ITL thấp hơn **cả hai** STL liền kề (đã chỉ tay vào từng cái)
- [ ] Mỗi LTL thấp hơn **cả hai** ITL liền kề
- [ ] Đáy/đỉnh mới nhất ở mỗi cấp được ghi là **ứng viên**, kèm "còn thiếu gì"
- [ ] Không có nhãn nào được nâng cấp vì "trông to"

### C. Đọc cấu trúc
- [ ] Hướng cấp ngắn hạn: tăng / giảm / không rõ
- [ ] Hướng cấp trung hạn: tăng / giảm / không rõ
- [ ] Protected low/high của cấp trung hạn nằm ở đâu — và nó đã vượt/thủng swing nào để được gọi là protected
- [ ] Hai mép của vùng (ngoài) và giá đang ở đâu trong vùng
- [ ] Đáy/đỉnh nào **chưa bị xuyên qua** (liquidity còn nguyên)

### D. Khi có cú phá
- [ ] Swing bị phá là: khung ___ cấp ___
- [ ] Nến đã đóng. Đóng trong hay ngoài mức?
- [ ] Nến tiếp theo làm gì?
- [ ] Kết luận chỉ nói về **cấp đó, khung đó**

### E. Ghép khung
- [ ] D1 nói gì? H1 nói gì? M5 nói gì? — ba câu riêng
- [ ] Câu kết luận có dạng: "M5 ___ bên trong H1 ___ bên trong D1 ___"
- [ ] Nếu ba khung mâu thuẫn mà không giải thích được → **không vào lệnh**

### F. Ba câu "không có lệnh"
- [ ] Đang dựa vào một nhãn chỉ tồn tại nhờ hindsight
- [ ] Đang để M5 cãi lại D1 mà không ghi là countertrend
- [ ] Không chỉ ra được điểm sai (đáy/đỉnh nào vỡ thì mình sai)

---

## 29. Nhật ký phiên bản luật & Hypothesis Register

### 29.1 Luật phân loại — từ v1 sang v2.0

| | Nội dung |
|---|---|
| **LUẬT CŨ (v1)** | STL = đáy ba-nến; ITL = STL có STL cao hơn hai bên; LTL = ITL có ITL cao hơn hai bên. Kèm các khẳng định: "LTL là đáy của một range lớn", "đáy càng nhiều lớp mũ thì stop loss dồn bên dưới càng nhiều", "phá ITH mới là BOS của xu hướng trung hạn" |
| **LUẬT MỚI (v2.0)** | Giữ nguyên ba định nghĩa vị trí. **Thêm:** (1) trạng thái *ứng viên / đã xác nhận / đã bị phá*; (2) quy ước inside bar, đáy bằng nhau, outside bar; (3) mọi nhãn kèm tên khung; (4) ống kính chức năng (FVG) chỉ là thẻ phụ; (5) *protected* tách khỏi *cấp độ* và được định nghĩa bằng cú vượt đỉnh cùng cấp; (6) "phá" = thân nến đóng qua, "quét" = râu qua rồi đóng lại. **Hạ cấp:** các khẳng định về liquidity và "đáy của range lớn" từ sự thật xuống giả thuyết |
| **LÝ DO** | Bản v1 trộn vị trí với ý nghĩa, không có khái niệm ứng viên nên dễ đọc bằng hindsight, và trình bày giả thuyết như sự thật |
| **HIỆU QUẢ KỲ VỌNG** | Hai lần chấm cùng một chart ra cùng kết quả; ít lỗi "nâng cấp bằng cảm giác"; backtest được |
| **CẦN BACKTEST?** | **Có** — các quy ước (inside bar, thân/râu) là lựa chọn, chưa được so sánh |

### 29.2 Hypothesis Register

| Mã | Giả thuyết | Lý do | Cách kiểm | Điều gì bác bỏ nó | Trạng thái |
|---|---|---|---|---|---|
| HYP-AMS-001 | Sau khi nến đóng dưới một ITL, giá đi tiếp cùng chiều thường xuyên hơn so với sau khi đóng dưới một STL | ITL đại diện cho nhịp lớn hơn | Chấm tự động theo luật v2.0 trên H1; ghi lại giá đi tiếp hay quay lại trước | Hai nhóm cho kết quả gần như nhau | UNTESTED |
| HYP-AMS-002 | Cú quét một H1-ITL cùng chiều D1 cho setup M5 tốt hơn cú quét một H1-STL | Liquidity tầng dày hơn | So kết quả ICT 2022 Model theo cấp của đáy bị quét | Không khác biệt, hoặc ngược lại | UNTESTED |
| HYP-AMS-003 | ITL/ITH hình thành khi lấp FVG giữ được lâu hơn ITL/ITH không lấp FVG | Ống kính chức năng (tập 12) | Gắn thẻ FVG cho từng ITL; so tỉ lệ bị phá | Không khác biệt | UNTESTED |
| HYP-AMS-004 | Protected low (theo định nghĩa v2.0) bị phá ít thường xuyên hơn ITL không protected | Vai trò > vị trí | So hai nhóm ITL | Không khác biệt | UNTESTED |
| HYP-AMS-005 | Trên chỉ số, vùng đỉnh có nhiều đỉnh nhỏ xung quanh hơn vùng đáy | Rơi nhanh hơn lên | Đếm số STH quanh LTH so với số STL quanh LTL | Không khác biệt | UNTESTED |

Lưu ý phương pháp cho mọi giả thuyết: chấm bằng máy theo đúng luật (không chấm bằng mắt); chỉ dùng nhãn **đã xác nhận tại thời điểm đó**; tách riêng từng thị trường và từng khung; không rút kết luận từ vài chục mẫu. Xem [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] về cách phát hiện swing bằng thuật toán.

### 29.3 Phác thảo thuật toán (để tự chấm, không cần toán)

```text
ĐẦU VÀO: danh sách nến đã đóng của MỘT khung

BƯỚC 1 — tìm STL:
  với mỗi nến (bỏ qua inside bar):
    nếu đáy của nó thấp hơn đáy nến trước VÀ thấp hơn đáy nến sau → ghi là STL
  (làm tương tự với đỉnh để có STH)

BƯỚC 2 — tìm ITL:
  xếp các STL theo thứ tự thời gian
  với mỗi STL (trừ cái đầu và cái cuối):
    nếu nó thấp hơn STL liền trước VÀ thấp hơn STL liền sau → ghi thêm là ITL
  STL cuối cùng: nếu thấp hơn STL liền trước → ghi "ITL ứng viên"

BƯỚC 3 — tìm LTL:
  xếp các ITL theo thứ tự thời gian, làm y hệt bước 2

BƯỚC 4 — trạng thái:
  với mỗi đáy đã ghi: nếu có nến sau đó ĐÓNG dưới nó → "đã bị phá"
                      nếu chỉ có râu xuống dưới rồi đóng lại → "đã bị quét"

ĐẦU RA: mỗi đáy có (khung, cấp, trạng thái, thời điểm được xác nhận)
```

Cột "thời điểm được xác nhận" là thứ ngăn hindsight khi backtest: tại bất kỳ thời điểm nào, chỉ được dùng những đáy có thời điểm xác nhận **trước** thời điểm đó.

---

## 30. Research Questions — Câu hỏi còn mở

1. Tập 12 của ICT 2022 Mentorship thực sự định nghĩa ITH/ITL thế nào? (Cần tự xem lại bản gốc.)
2. "Protected high/low" có định nghĩa nguyên văn nào của ICT không?
3. Với luật v2.0, một phiên M5 điển hình của NQ có bao nhiêu STL, ITL, LTL? Con số đó có ổn định không?
4. Quy ước inside bar có làm thay đổi đáng kể số ITL không?
5. Một D1-STL thường tương ứng với cấp nào trên H1?

---

## Flashcards / Active Recall

### Q1
**Hỏi:** STL, ITL, LTL khác nhau ở điểm nào — nói bằng một câu?
**Đáp:** Cùng là một đáy; khác nhau ở số lớp hàng xóm mà nó thấp hơn: STL thấp hơn hai **nến** bên cạnh, ITL thấp hơn hai **STL** bên cạnh, LTL thấp hơn hai **ITL** bên cạnh.

### Q2
**Hỏi:** Một STL trở thành ITL lúc nào?
**Đáp:** Lúc một STL **cao hơn** ở bên phải nó được xác nhận (và bên trái đã có sẵn STL cao hơn). Không phải lúc nó in ra.

### Q3
**Hỏi:** Vì sao một xu hướng tăng rất khỏe có thể không có ITL mới nào?
**Đáp:** Vì mỗi đáy đều cao hơn đáy bên trái → không đáy nào thấp hơn cả hai hàng xóm.

### Q4
**Hỏi:** Năm khái niệm không được trộn lẫn?
**Đáp:** Hình thành, xác nhận, phân loại, thứ bậc, ý nghĩa cấu trúc.

### Q5
**Hỏi:** Mọi ITL có phải protected low không?
**Đáp:** Không. Protected khi cú tăng từ nó đã đóng nến vượt đỉnh cùng cấp trước đó.

### Q6
**Hỏi:** LTL có phải luôn là đáy lớn của thị trường?
**Đáp:** Không. Nó là đáy lớn nhất của một vùng trên **một khung**, và có thể nằm giữa downtrend rồi bị phá.

### Q7
**Hỏi:** Phá một STL trong uptrend, khi ITL còn nguyên, gọi là gì?
**Đáp:** Một cú phá nội bộ ở cấp ngắn hạn. Không phải đảo chiều. Chỉ là ứng viên MSS nếu có đủ bối cảnh (sweep trước đó, có lực).

### Q8
**Hỏi:** Đáy sâu nhất chart nằm ở mép phải. Gọi là gì?
**Đáp:** ITL ứng viên (hoặc LTL ứng viên). Chưa có hàng xóm bên phải nên chưa lên cấp.

### Q9
**Hỏi:** Vì sao viết "ITL" trống là sai?
**Đáp:** Vì cấp độ chỉ có nghĩa trong một khung. Phải viết D1-ITL, H1-ITL, M5-ITL.

### Q10
**Hỏi:** Điều gì chứng tỏ thứ bậc swing không tự mang ý nghĩa dự đoán?
**Đáp:** Một đường ngẫu nhiên cũng có đủ STL, ITL, LTL. Giá trị dự đoán phải được kiểm chứng bằng backtest.

### Q11
**Hỏi:** Hai "ống kính" để phân loại ITH/ITL?
**Đáp:** Vị trí (so với hàng xóm — luật chính) và chức năng (đã lấp FVG — theo ghi chép tập 12, dùng làm thẻ phụ).

### Q12
**Hỏi:** M5 chuyển giảm, H1 và D1 vẫn tăng. Nói thế nào cho đúng?
**Đáp:** "M5 đang giảm bên trong một nhịp tăng H1, bên trong một xu hướng tăng D1."

---

## Lesson Learned

### Bài học chính
- Phần lớn lỗi đọc cấu trúc không đến từ việc không biết định nghĩa, mà từ việc **trộn vị trí với ý nghĩa** và **nâng cấp ứng viên bằng cảm giác**.
- Hệ thống ba cấp nói được **nhiều nhất** khi thị trường có các nhịp lùi cỡ khác nhau, và **ít nhất** khi thị trường đi một mạch.
- Nhãn cấp cao luôn đến muộn. Hãy dùng nó để đọc bối cảnh.

### Quy tắc cá nhân rút ra
- Mọi nhãn trên chart đều kèm **tên khung** và **trạng thái** (ứng viên / xác nhận / đã phá).
- Trước khi gọi một đáy là protected, chỉ tay vào **cái đỉnh mà nó đã vượt**.
- Khi thấy mình đổi ý về hướng nhiều lần trong một phiên → đang đọc sai cấp; lên một cấp hoặc một khung.

### Câu nhắc khi trade
> "Đáy này thuộc khung nào, cấp nào, đã xác nhận chưa — và nếu nó vỡ thì **đúng cấp đó** đổi, không hơn."

---

## Tự kiểm tra chất lượng note (Research QC)

| # | Câu hỏi | Trả lời ở |
|---|---|---|
| 1 | Giải thích cho người mới hoàn toàn? | §2, §3 |
| 2 | Vì sao có nhiều cấp swing? | §3, §11.1 |
| 3 | STL chính xác? | §5 |
| 4 | ITL chính xác? | §6 |
| 5 | LTL chính xác? | §7 |
| 6 | STL → ITL? | §6.5, §11.2 |
| 7 | ITL → LTL? | §7.5, §11.3 |
| 8 | Swing high đối xứng (và bất đối xứng)? | §8–10 |
| 9 | Hình thành ≠ xác nhận? | §4.2, §19 |
| 10 | Thứ bậc và market structure? | §4, §12, §13 |
| 11 | Protected high/low? | §14 |
| 12 | Trong / ngoài? | §15 |
| 13 | Liquidity? | §16 |
| 14 | Phá thật ≠ quét? | §17.3, §24.3 |
| 15 | BOS, MSS, CHoCH? | §17 |
| 16 | Real-time ≠ hindsight? | §19 |
| 17 | D1 → H1 → M5? | §20, Case C |
| 18 | Phản ví dụ và trường hợp khó? | §22, §23 |
| 19 | Giả định chưa chứng minh? | §26 |
| 20 | Quy trình đọc chart thực tế? | §24, §28 |

**Những điểm note này CHƯA làm được (ghi trung thực):** chưa đối chiếu bản gốc video tập 12; chưa có ví dụ từ chart thật có dấu thời gian; chưa có số liệu backtest nào cho bất kỳ giả thuyết nào.

---

## Liên kết

**Cấu trúc:** [[05-BOS-Break-of-Structure]] · [[21-Market-Structure-Shift]] · [[09-Change-of-Character]] · [[12-Dealing-Range]] · [[37-Re-mapping-Dealing-Range-sau-Displacement]] · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]]
**Swing và thuật toán:** [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] · [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]
**Thanh khoản:** [[19-Liquidity]] · [[20-Liquidity-Sweep]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[15-Inducement]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]
**Lực và khoảng trống giá:** [[50-Displacement-In-Depth]] · [[13-FVG-Fair-Value-Gap]]
**Bối cảnh và đa khung:** [[59-Daily-Bias]] · [[27-Premium-Discount]] · [[32-Top-down-Analysis-Multiple-Timeframes]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]] · [[01 - ICT 2022 Model]]

---

## Nguồn tham khảo

> [!note] Về nguồn
> **Không có nguồn nào dưới đây là bản gốc của ICT được đối chiếu trực tiếp trong lần nghiên cứu này.** Các định nghĩa vị trí (STH/ITH/LTH) được xác nhận chéo giữa trích dẫn Larry Williams và nhiều tài liệu ICT thứ cấp, nên độ tin cậy **cao**. Các ý về tập 12 (ITH/ITL gắn với FVG, "một khi hình thành không nên bị vi phạm") đến từ ghi chép của người học và một bản tóm tắt tự động, nên độ tin cậy **vừa**. Nguồn cộng đồng có quảng cáo khóa học chỉ được dùng để mô tả cách thuật ngữ được dùng. Những chỗ các nguồn **không thống nhất** đã được nêu ở §5.5, §6.4, §11.4 và §14.2 thay vì tự gộp lại.

**Nguồn gốc khái niệm (Tier 2–3)**
- Larry Williams — *Long-Term Secrets to Short-Term Trading*. Nguồn của hệ ba cấp đỉnh/đáy ngắn hạn – trung hạn – dài hạn. *Không đọc trực tiếp; định nghĩa được dẫn qua phần mô tả của script bên dưới, và tên sách được nêu trong ghi chép tập 12.*
- TradingView — *Larry Williams: Market Structure* (script của Smollet, 2025). Dẫn lời Williams: đỉnh ngắn hạn là ngày có đỉnh thấp hơn hai bên, không tính inside day; đỉnh trung hạn là đỉnh ngắn hạn có đỉnh ngắn hạn thấp hơn hai bên; đỉnh dài hạn là đỉnh trung hạn có đỉnh trung hạn thấp hơn hai bên. https://tradingview.com/script/3bpbtsEs-Larry-Williams-Market-Structure

**ICT — nguồn thứ cấp (Tier 3–4)**
- ICT 2022 Mentorship, Episode 12 — *Market Structure for Precision Technicians*. Video gốc: https://www.youtube.com/watch?v=8GkQfdAXZP0 — **chưa xem trực tiếp trong lần nghiên cứu này.**
- ICT Sharks Forum — ghi chép tập 12 của người học (2024). LTH = ITH thấp hơn hai bên; ITH "thường" có STH thấp hơn hai bên; STH = mọi swing high còn lại; swing hình thành khi giá lấp FVG trở thành ITH/ITL và "không nên bị vi phạm"; LTH/LTL thường gắn với chart ngày; nhắc đến ảnh hưởng của Larry Williams. https://forum.ictsharks.com/t/2022-ict-mentorship-episode-12-market-structure-for-precision-technicians-advanced-price-action-theory/157
- VideoHighlight — bản tóm tắt tự động của tập 12 (có ghi chú "có thể không chính xác", và tự mâu thuẫn về việc ITH cao hay thấp hơn STH hai bên). Chỉ dùng để đối chiếu. https://videohighlight.com/v/8GkQfdAXZP0?mediaType=youtube&language=en&summaryType=default&summaryId=2s_8EU7-Ssyspf2v6W9d&aiFormatted=false
- innercircletrader.net — *ICT Advance Market Structure* (bài viết cộng đồng, có quảng cáo khóa học; tác giả không phải ICT). STH = hình ba-nến; ITH = STH có STH thấp hơn hai bên; LTH = ITH có ITH thấp hơn hai bên, "thường tại PD array của khung lớn hơn". https://innercircletrader.net/id/tutorial/ict-advance-market-structure/

**Khác**
- Bản v1 của note này (2026-06-23 → 2026-07-28), lưu tại `attachments/_backup/`.
