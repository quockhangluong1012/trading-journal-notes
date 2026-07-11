---
type: ict-concept
concept: SMT Divergence
aliases:
  - SMT Divergence
  - Smart Money Technique
  - Smart Money Divergence
  - SMT
  - Phân kỳ SMT
tags:
  - trading/ict/concept
  - trading/study
  - "#confirmation"
  - "#liquidity"
status: developing
category: Confirmation
last_reviewed: 2026-07-11
created: 2026-07-05
updated: 2026-07-11
---

# SMT Divergence

> [!summary] Tóm tắt 1 câu
> **SMT (Smart Money Technique) Divergence là hiện tượng hai tài sản CÓ TƯƠNG QUAN "lệch pha" tại một cực trị — một cái tạo đỉnh/đáy mới còn cái kia thì không — để lộ dấu chân của smart money và xác nhận rằng cực trị đó là TERMINAL (điểm cuối cùng), không phải điểm tiếp diễn.**

> [!important] Nguyên tắc cốt lõi
> Hai tài sản tương quan (NQ/ES, EURUSD/GBPUSD, XAU/DXY) được **cùng một engine phân phối giá (algorithmic delivery) của các market maker điều khiển**, nên về lý thuyết chúng phải đi cùng nhịp. Khi một cái **quét thanh khoản** (tạo lower low/higher high mới) còn cái kia **từ chối theo** (giữ đáy/không phá đỉnh), sự "lệch" đó cho thấy dòng lệnh tổ chức đang **hấp thụ ngược hướng** — cú sweep là cú lấy thanh khoản CUỐI CÙNG chứ không phải khởi đầu xu hướng mới. SMT **là xác nhận, không phải trigger**: nó nói *"cực trị này đáng tin"*, nhưng entry vẫn cần sweep + CISD/MSS + POI.

---

## 1. Định nghĩa

**Khái niệm:**
**SMT Divergence** so sánh **cấu trúc đỉnh/đáy** của hai (hoặc nhiều) công cụ tương quan tại **cùng một thời điểm** để phát hiện sự bất đồng. Trong một **bullish SMT** ở đáy: tài sản A tạo **lower low** (quét sell-side liquidity) trong khi tài sản B tạo **higher low** (không phá đáy cũ). Sự lệch này báo hiệu phe bán đã kiệt sức tại A và smart money đang gom → khả năng đảo chiều **tăng**. Bearish SMT là gương phản chiếu ở đỉnh.

![[SMT-Advanced-Anatomy.svg|697]]

*Bullish SMT: NQ tạo lower low và quét SSL, trong khi ES giữ higher low (không quét). Sự lệch pha này = tín hiệu đảo chiều tăng. Chú ý cách so ĐÚNG cực trị tương ứng: đáy cuối của NQ đối chiếu với đáy cuối của ES.*

**Nó giúp trả lời câu hỏi nào trên chart?**
- Cú phá đỉnh/đáy vừa rồi là **breakout thật** hay chỉ là **liquidity sweep** (bẫy)?
- Cực trị này có phải là **điểm cuối** của cú swing để tôi tự tin đảo chiều không?
- Daily Bias của tôi có được **xác nhận liên thị trường (inter-market)** không?

### SMT KHÔNG phải là gì
- **Không phải** trigger vào lệnh — nó là **lớp xác nhận** thêm vào sweep + CISD/MSS.
- **Không phải** RSI/MACD divergence (phân kỳ giữa giá và chỉ báo). SMT là phân kỳ giữa **hai giá của hai tài sản**.
- **Không** dùng được giữa hai tài sản **không tương quan** (vd NQ vs Gold).
- **Không** có giá trị nếu xuất hiện **giữa range**, xa các pool thanh khoản.

---

## 2. Cơ chế sâu — vì sao SMT hoạt động

Đây là phần "why" mà đa số người học SMT bỏ qua. Hiểu cơ chế mới phân biệt được SMT thật với trùng hợp ngẫu nhiên.

**(a) Cùng một engine phân phối giá.** Theo mô hình ICT, giá không "chạy tự do" mà được các market maker giao (deliver) theo thuật toán quanh các mức thanh khoản. Các chỉ số Mỹ (NQ/ES/YM) hay rổ USD (EU/GU/DXY) chia sẻ **cùng dòng vốn tổ chức và cùng lịch macro**. Khi engine muốn *phân phối thật* (bắt đầu một chân giảm mới), nó sẽ đẩy **tất cả** các công cụ liên quan tạo cực trị mới — vì lệnh tổ chức phải được lấp ở mọi công cụ trong rổ. Khi chỉ **một** công cụ phá cực trị, đó là dấu hiệu engine chỉ đang **thu thanh khoản cục bộ** (stop hunt) ở công cụ yếu hơn, chứ chưa cam kết vào một xu hướng mới.

**(b) Leader vs laggard — ai đang được "bảo vệ".** Công cụ **từ chối** tạo cực trị mới là công cụ **mạnh hơn về order flow**, đang được smart money giữ. Ở bullish SMT, tài sản giữ higher low = phe mua đang hấp thụ; tài sản kia bị đẩy xuống chỉ để **thu SSL** (stop của phe long non + lệnh sell breakout). Sau khi thanh khoản đã bị lấy, không còn "nhiên liệu" cho chân giảm → đảo chiều.

**(c) SMT phân biệt sweep terminal với breakout thật.** Một cú phá đáy có hai bản chất trái ngược: (1) *breakout thật* = khởi đầu chân giảm, cả rổ cùng xuống; (2) *liquidity sweept* = quét stop rồi quay đầu. SMT chính là bộ lọc tách hai trường hợp này bằng bằng chứng liên thị trường, điều mà nhìn một chart đơn lẻ **không thể** làm được.

> [!info] Vì sao SMT mạnh hơn nhiều chỉ báo phân kỳ
> RSI/MACD divergence chỉ so giá với một hàm toán của chính giá đó (lagging, cùng một nguồn dữ liệu). SMT so **hai dòng order flow độc lập nhưng cùng chủ**. Đó là bằng chứng **cross-sectional** — khó ngụy tạo hơn nhiều và phản ánh trực tiếp hành vi của bên phân phối.

---

## 3. Bối cảnh sử dụng

### Khi nào SMT có giá trị cao?
- [ ] So giữa hai tài sản **tương quan thật** (NQ/ES, EU/GU, XAU/DXY)
- [ ] Divergence xảy ra tại **cực trị có thanh khoản** (SSL/BSL, equal highs/lows, PDH/PDL, PWH/PWL)
- [ ] Trùng với **Daily Bias** đã xác định
- [ ] Trong **killzone** / macro window
- [ ] Đi kèm **sweep + CISD/MSS + FVG** (SMT là mảnh ghép xác nhận cuối)
- [ ] Giá đang ở vùng **Premium/Discount** hợp lý (bullish SMT nên ở discount, bearish ở premium)

### Khi nào nên bỏ qua?
- [ ] Hai tài sản **tương quan yếu** hoặc không tương quan
- [ ] Divergence ở **giữa range**, không có pool thanh khoản
- [ ] Chỉ có SMT nhưng **không có sweep** hay trigger cấu trúc
- [ ] Ngược Daily Bias mà không có narrative HTF mạnh
- [ ] Tương quan **tạm thời đảo** do tin riêng của một tài sản (vd earnings 1 cổ phiếu ảnh hưởng chỉ số; phát biểu BoE kéo GBP lệch EUR)

---

## 4. Bullish SMT vs Bearish SMT

![[SMT-Advanced-BullBear.svg|697]]

**Bullish SMT (tại ĐÁY):** A tạo **lower low** (quét SSL) nhưng B tạo **higher low** (không theo). Kỳ vọng: đảo chiều **tăng**. Chờ SSL bị quét, tìm entry **long**.

**Bearish SMT (tại ĐỈNH):** A tạo **higher high** (quét BSL) nhưng B tạo **lower high** (không theo). Kỳ vọng: đảo chiều **giảm**. Chờ BSL bị quét, tìm entry **short**.

> [!tip] Đọc phe nào là "leader", phe nào "laggard"
> Tài sản **không chịu** tạo cực trị mới thường là phe **mạnh hơn** (đang được smart money bảo vệ). Ở bullish SMT, tài sản giữ higher low = phe mua mạnh hơn → xác nhận thiên hướng mua. Đây là cách SMT tinh chỉnh **Daily Bias** liên thị trường: nếu chưa chắc bias, để SMT "bỏ phiếu" giúp.

---

## 5. Bản đồ cặp tương quan

![[SMT-Advanced-CorrelationMap.svg|697]]

SMT **chỉ hợp lệ** giữa các tài sản có tương quan thật. Có hai loại tương quan cần phân biệt rõ:

**Tương quan THUẬN (so cùng chiều):**
- Chỉ số Mỹ: **NQ ↔ ES ↔ YM ↔ RTY** — NQ vs ES là cặp SMT kinh điển nhất.
- Forex: **EURUSD ↔ GBPUSD** (đều nghịch USD nên thuận nhau).
- Kim loại: **XAUUSD ↔ XAGUSD** (vàng ↔ bạc).

**Tương quan NGHỊCH (so ngược chiều):**
- **EURUSD/GBPUSD/XAUUSD ↔ DXY** — khi DXY quét đỉnh mà EURUSD không phá đáy = bullish SMT cho EURUSD.
- **Gold ↔ US10Y (lợi suất)** — thường nghịch nhau.
- **USDJPY ↔ DXY** — thuận (JPY là đồng yếu trong rổ, USDJPY đi cùng DXY).

> [!warning] Cạm bẫy tương quan
> Tương quan **không cố định** — nó thay đổi theo chế độ thị trường (regime). Trong các giai đoạn tin tức riêng lẻ (một big-tech công bố earnings kéo NQ lệch ES; BoE/ECB ra tin kéo GBP lệch EU), tương quan có thể tạm gãy và tạo "SMT giả". Luôn ưu tiên SMT tại **cực trị có pool** và trong **killzone**, tránh đọc SMT quanh giờ tin đỏ của riêng một tài sản. Nếu nghi ngờ, kiểm tra nhanh: trong 20–30 nến gần nhất hai công cụ có đang đi cùng nhịp không? Nếu không, đừng đọc SMT lúc đó.

---

## 6. SMT nghịch đảo — đọc với DXY

![[SMT-Advanced-Inverse.svg|697]]

Với cặp **nghịch tương quan**, đỉnh của cái này nên khớp **đáy** của cái kia. Ví dụ điển hình cho trader forex/vàng: dùng **DXY** làm "tấm gương".

- Nếu **DXY tạo higher high (quét đỉnh)** nhưng **EURUSD KHÔNG tạo lower low (giữ đáy)** → **bullish SMT** cho EURUSD: USD đang bị hấp thụ ở đỉnh, EUR sắp tăng.
- Ngược lại, **DXY tạo lower low** nhưng **EURUSD không phá đỉnh** → **bearish SMT** cho EURUSD.

Đây là công cụ mạnh để xác nhận sweep trên forex/vàng khi bạn không có "cặp anh em" rõ ràng — DXY đóng vai trò benchmark cho toàn bộ rổ USD. Với XAUUSD, DXY là benchmark mặc định; có thể kết hợp thêm XAGUSD (thuận) để có "quad" xác nhận (xem mục 11).

> [!tip] Mẹo thao tác với cặp nghịch
> Để tránh nhầm chiều khi đầu óc căng lúc entry, hãy tự nhủ: *"USD lên thì EUR xuống"*. SMT nghịch = **USD làm được điều A muốn (quét đỉnh) mà EUR từ chối làm điều tương ứng (phá đáy)**. Khi bạn thấy DXY "cố" mà EUR "không chịu theo" → phe USD đang cạn lực.

---

## 7. Đọc SMT ĐÚNG điểm — độ chính xác fractal

![[SMT-Advanced-Fractal.svg|697]]

Lỗi tinh vi nhất của người mới: so **hai cực trị không tương ứng**. SMT chỉ có nghĩa khi bạn so **đúng cặp swing point cùng một cú đẩy, cùng mốc thời gian**.

- **Đúng:** đáy cuối (cú push tạo lower low) của A đối chiếu với đáy cuối của B tại **cùng nến / cùng cụm nến**. Cả hai phải là cực trị của **cùng một swing** trên cùng khung thời gian.
- **Sai:** lấy đáy của A ở swing này so với đáy của B ở swing khác (lệch vài nến, lệch cả cấu trúc). "Lệch pha" khi đó chỉ là ảo giác do lệch thời gian.

**Quy tắc thực hành:** căn hai chart **cùng khung, cùng crosshair thời gian**. Kéo crosshair đến nến tạo cực trị trên instrument giao dịch, rồi nhìn **đúng nến đó** trên benchmark. Nếu tại thời điểm A quét pool mà B đang giữ/không phá — đó là SMT thật. Nếu B phá pool ở một thời điểm khác, không tính.

> [!warning] Lệch nến = SMT giả
> Rất nhiều "SMT" trên mạng thực chất là do người vẽ chọn hai đáy tiện tay ở hai thời điểm khác nhau. Kỷ luật crosshair đồng bộ loại bỏ 90% tín hiệu rác này.

---

## 8. SMT + Sweep + CISD/MSS — thang confluence

![[SMT-Advanced-Entry-Confluence.svg|697]]

SMT phát huy sức mạnh khi là **mảnh ghép cuối** của chuỗi xác nhận, không phải khi đứng một mình:

- **SMT đơn lẻ** = chỉ là *cảnh báo* cực trị có thể terminal. Không trade.
- **SMT + sweep** = có *lý do* đảo chiều (thanh khoản đã bị lấy).
- **SMT + sweep + CISD/MSS** = có *trigger* cấu trúc → tradeable.
- **SMT + sweep + CISD/MSS + FVG/OB + killzone** = **A+ setup** — vào tại FVG (50% CE), stop sau wick sweep.

> [!info] Vì sao SMT làm entry mạnh hơn hẳn
> SMT trả lời câu hỏi mà sweep + CISD **không** trả lời được: *"cú sweep này có phải cú cuối không?"*. Một sweep có thể là cú đầu của chuỗi sweep sâu hơn (sweep chồng sweep). Nhưng nếu tài sản tương quan **từ chối** theo, xác suất đây là **cú lấy thanh khoản cuối cùng** tăng vọt → giảm mạnh tỉ lệ dính "sweep chồng sweep" và bị stop-out sớm.

---

## 9. SMT đa khung thời gian (MTF nesting)

![[SMT-Advanced-MTF.svg|697]]

SMT mạnh nhất khi **đồng thuận nhiều khung**. Quy trình lồng khung (top-down):

1. **HTF (H4/H1) — chọn bias.** Tìm SMT tại pool HTF (PDH/PDL, PWH/PWL). SMT ở đây cho biết **hướng ngày/phiên**. Ví dụ H1 bullish SMT → chỉ tìm long trong ngày.
2. **LTF (M5/M1) — tinh chỉnh entry.** Zoom vào vùng cực trị HTF, chờ **một SMT LTF cùng hướng** đi kèm sweep + CISD → đó là điểm vào chính xác với stop nhỏ, R lớn.

Khi HTF SMT và LTF SMT **cùng chỉ một hướng**, đó là confluence hạng nhất: bias được xác nhận ở tầng lớn, còn timing được xác nhận ở tầng nhỏ. Ngược lại, nếu LTF SMT **ngược** HTF SMT → cảnh giác, có thể chỉ là pullback nội bộ; đừng ép lệnh.

> [!tip] Nguyên tắc "khung trên quyết định hướng, khung dưới quyết định giờ"
> Đừng bao giờ để một LTF SMT kéo bạn đi ngược HTF bias. LTF chỉ dùng để *canh giờ vào*, không dùng để *đổi hướng*.

---

## 10. Chấm điểm chất lượng SMT (A / B / C)

![[SMT-Advanced-Grading.svg|697]]

Không phải SMT nào cũng ngang nhau. Chấm điểm giúp bạn phân bổ rủi ro hợp lý và — quan trọng hơn — **đo edge theo cấp** trong nhật ký.

- **A+ (giao dịch mạnh):** cặp tương quan lõi (NQ/ES, EU/DXY) · tại pool HTF rõ · trong killzone/macro · thuận Daily Bias · có đủ sweep + CISD/MSS + FVG.
- **B (cân nhắc, giảm size):** tương quan ổn nhưng phụ · pool LTF · ngoài macro nhưng trong session · bias trung tính · trigger yếu hơn.
- **C (bỏ qua):** tương quan yếu/theo mùa · giữa range · ngoài killzone · ngược bias không narrative · chỉ có lệch pha, thiếu trigger.

> [!tip] Dùng grading để quản lý rủi ro
> Chỉ full risk (≤0.5%) cho **A+**. Với B, cân nhắc nửa size hoặc bỏ. C thì đứng ngoài. Ghi cấp SMT vào frontmatter mỗi trade để về sau lọc `grade = A+` và xem win-rate/expectancy tách theo cấp — đây là cách biến SMT từ "cảm giác" thành **dữ liệu**.

---

## 11. SMT + Power of Three (AMD) — bắt Judas swing

![[SMT-Advanced-PO3.svg|697]]

SMT gắn rất chặt với **Power of Three (Accumulation – Manipulation – Distribution)**. Cú **Judas swing** (giai đoạn Manipulation) là cú đẩy giả để lấy thanh khoản trước khi giá đi hướng thật (Distribution). SMT thường **in ra đúng tại đỉnh/đáy của Judas swing**.

- Trong một ngày bullish: sau accumulation quanh giá mở, engine đẩy **xuống** (Judas) để quét SSL. Nếu **tại đáy Judas** xuất hiện **bullish SMT** (instrument quét, benchmark giữ đáy) → xác nhận Manipulation đã xong, **Distribution tăng** sắp bắt đầu → vào long.
- Đảo lại cho ngày bearish: Judas đẩy **lên** quét BSL, bearish SMT tại đỉnh → Distribution giảm.

Đây là một trong những confluence sạch nhất: bạn biết **narrative** (PO3) *và* có **bằng chứng liên thị trường** (SMT) cùng chỉ một hướng, ngay tại thời điểm thanh khoản bị lấy.

> [!info] Kết hợp với Turtle Soup
> Judas swing + SMT chính là bộ khung của [[33 - Turtle Soup]] nâng cao: quét một cực trị "hiển nhiên" (false breakout) rồi đảo. SMT thêm lớp xác nhận rằng cú quét đó là bẫy, không phải breakout thật.

---

## 12. Quy trình đọc SMT khi vào lệnh

**Bước 1 — Mở song song hai chart tương quan.** Ví dụ NQ + ES cạnh nhau (hoặc EURUSD + DXY). Căn **cùng khung thời gian, cùng mốc thời gian**, bật crosshair đồng bộ.

**Bước 2 — Xác định bias HTF & vùng Premium/Discount.** Bullish SMT chỉ đáng tin ở **discount**; bearish SMT ở **premium**. SMT ngược vùng PD là cờ đỏ.

**Bước 3 — Chờ giá tiếp cận một pool thanh khoản HTF.** Chỉ tìm SMT tại các cực trị có nghĩa (SSL/BSL, equal highs/lows, PDH/PDL, PWH/PWL) — không phải giữa range.

**Bước 4 — So cấu trúc tại cực trị (đúng fractal).** Một tài sản quét pool (tạo cực trị mới), cái kia không theo → SMT hình thành. Chấm điểm A/B/C. Xác nhận nó **thuận Daily Bias**.

**Bước 5 — Chờ trigger trên instrument bạn giao dịch.** Sweep + **CISD/MSS** + displacement/FVG. SMT chỉ là đèn xanh xác nhận; trigger cấu trúc mới là điểm vào.

**Bước 6 — Entry, stop, target.** Entry tại FVG (50% CE) hoặc OB; **stop sau wick của cú sweep** (chính là điểm tạo lower low/higher high — cực trị lệch pha); T1 = IRL, T2 = ERL/draw on liquidity. Cân size theo cấp SMT.

---

## 13. Ví dụ chart

### Ví dụ đúng
![[Liquidity-Sweep-Advanced-SMT.svg|697]]

**Mô tả:** Tại vùng discount, NQ quét SSL (tạo lower low) trong khi ES giữ higher low → **bullish SMT**. Ngay sau đó NQ in **CISD/MSS**, để lại FVG. Entry long tại FVG, stop dưới wick sweep, target BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- So đúng cặp tương quan kinh điển (**NQ ↔ ES**).
- SMT xảy ra **tại pool thanh khoản** (SSL), không phải giữa range.
- Có đủ chuỗi: **SMT (xác nhận) + sweep (lý do) + CISD/MSS (trigger) + FVG (entry)**.
- Ở **discount** (thuận bias long), stop rõ ràng sau wick sweep, R:R lành mạnh (T1=IRL, T2=BSL).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp 2 chart cạnh nhau (NQ+ES hoặc EURUSD+DXY): đánh dấu (1) cực trị lệch pha, (2) tài sản nào quét/không quét, (3) sweep + CISD/MSS trên instrument giao dịch, (4) entry/stop/target, (5) cấp SMT (A/B/C).*

### Ví dụ sai / dễ nhầm
![[SMT-Example-Wrong.svg|697]]

**Mô tả lỗi:** (1) So hai tài sản **không tương quan** (NQ vs Gold) → "lệch pha" là ngẫu nhiên, vô nghĩa. (2) Divergence xuất hiện **giữa range**, xa mọi pool thanh khoản → nhiễu, không phải tín hiệu.

**Bài học:**
- SMT chỉ có nghĩa giữa **tài sản tương quan thật**.
- SMT phải nằm **tại cực trị có thanh khoản**, không phải giữa range.
- SMT **không thay thế** sweep + trigger; thiếu chúng thì SMT chỉ là quan sát.

---

## 14. Thực hành tốt nhất (Best Practices)

> [!tip] 8 quy tắc SMT
> 1. **Chỉ so tài sản tương quan thật** — NQ/ES, EU/GU, XAU/DXY. Sai cặp = tín hiệu rác.
> 2. **SMT phải nằm tại pool thanh khoản** — cực trị có SSL/BSL, không phải giữa range.
> 3. **SMT là xác nhận, không phải trigger** — luôn chờ sweep + CISD/MSS mới vào.
> 4. **Căn đúng cùng khung + cùng thời điểm (crosshair đồng bộ)**, so đúng cặp swing point — tránh lệch nến gây ảo giác divergence.
> 5. **Với cặp nghịch, so ngược chiều** (DXY quét đỉnh ↔ EURUSD giữ đáy).
> 6. **Lọc theo Premium/Discount** — bullish SMT ở discount, bearish ở premium.
> 7. **Chấm cấp A/B/C** và cân size theo cấp — chỉ full risk cho A+.
> 8. **Tránh SMT quanh tin riêng** của một tài sản (earnings, phát biểu ngân hàng TW).

- Mở sẵn **layout 2 chart** (instrument giao dịch + benchmark tương quan) để không phải chuyển tab lúc quyết định.
- Ưu tiên SMT trên **HTF (H1/H4)** để chọn bias, rồi tìm SMT **LTF (M5/M1)** cùng hướng cho entry — SMT đồng thuận đa khung là cực mạnh (mục 9).
- Ghép SMT với **macro window** ([[40 - Macro Times]]): SMT hình thành ngay trong 09:50–10:10 ET là confluence hạng nhất cho NQ.
- Với XAUUSD/forex, dùng **DXY** làm benchmark mặc định vì nó phản ánh cả rổ USD; thêm cặp thuận (XAG, GU) để có "quad" xác nhận.
- **Kiểm tra tương quan còn "sống" không** trước khi đọc: 20–30 nến gần nhất hai công cụ có đi cùng nhịp không?
- **Ghi nhật ký có kỷ luật:** gắn nhãn mỗi lệnh *có/không có SMT xác nhận* và *cấp SMT* để đo edge — nhiều trader thấy win-rate tăng rõ rệt ở nhóm "có SMT A+". Đây là cách backtest biến SMT thành edge cá nhân đã kiểm chứng, thay vì niềm tin.

> [!warning] Bối cảnh prop-firm (FTMO & The5ers)
> SMT giúp **giảm tần suất dính sweep chồng sweep** — đúng loại lỗi làm cháy daily loss limit. Nhưng đừng dùng SMT để biện minh cho việc **tăng số lệnh**: chất lượng > số lượng. Trong giai đoạn foundation hiện tại, hãy backtest riêng nhóm "có SMT A+" để xem expectancy có ổn định đủ trước khi tính đến việc mua challenge. FTMO đo daily loss theo balance cố định; The5ers tham chiếu equity đóng cửa hôm trước — SMT không thay đổi các luật này, nó chỉ nâng xác suất mỗi lệnh.

---

## 16. Checklist trước khi dùng SMT vào trade

> [!warning] SMT không phải là nút "mua/bán"
> Nó chỉ xác nhận cực trị đáng tin. Entry vẫn cần sweep + trigger + POI.

- [ ] Đang so đúng **cặp tương quan thật** (và tương quan còn "sống")
- [ ] Căn cùng khung thời gian, cùng thời điểm nến; so đúng cặp swing point (fractal)
- [ ] Divergence nằm **tại pool thanh khoản** (không giữa range)
- [ ] SMT **thuận Daily Bias** và đúng vùng **Premium/Discount**
- [ ] Có **sweep** thực sự tại cực trị
- [ ] Có **CISD/MSS** trigger trên instrument giao dịch
- [ ] Có **FVG/OB** cho vùng entry
- [ ] Đang trong killzone / macro
- [ ] Với cặp nghịch: đã so **ngược chiều** đúng cách
- [ ] Đã **chấm cấp A/B/C** và cân size theo cấp
- [ ] Stop sau wick sweep; T1 = IRL, T2 = ERL
- [ ] Không đọc SMT quanh giờ tin riêng của một tài sản

---

## 17. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Sai cặp tương quan | So NQ với Gold, EUR với BTC | Chỉ dùng cặp tương quan thật (NQ/ES, EU/GU, XAU/DXY) |
| SMT giữa range | Divergence xa pool thanh khoản | Chỉ đọc SMT tại cực trị có SSL/BSL |
| Coi SMT là trigger | Vào lệnh ngay khi thấy lệch pha | SMT là xác nhận; chờ sweep + CISD/MSS |
| Lệch nến / lệch swing giữa 2 chart | Divergence "ảo" do lệch thời gian hoặc so sai cặp swing | Căn cùng khung + crosshair đồng bộ; so đúng cặp swing point |
| Nhầm với chỉ báo divergence | So giá với RSI/MACD | SMT = phân kỳ giữa 2 tài sản, không phải chỉ báo |
| Bỏ qua tin riêng | Đọc SMT lúc earnings/BoE | Tránh cực trị bị bóp méo bởi tin của một tài sản |
| Ngược vùng PD | Bullish SMT ở premium, bearish ở discount | Lọc SMT theo Premium/Discount trước khi tin |
| Không phân cấp | Trade mọi SMT với cùng size | Chấm A/B/C, chỉ full risk cho A+ |
| Để LTF SMT đổi hướng | Đi ngược HTF bias vì thấy 1 LTF SMT | Khung trên quyết định hướng, khung dưới chỉ canh giờ |

---

## 18. Câu hỏi tự kiểm tra

- Tôi giải thích được SMT trong 30 giây và phân biệt với RSI divergence không?
- Cơ chế "why" của SMT là gì — vì sao hai tài sản tương quan phải đồng pha?
- Cặp tương quan mặc định cho NQ / cho EURUSD / cho XAUUSD là gì?
- SMT là bias, POI, entry hay xác nhận? Tôi dùng nó ở bước nào trong chuỗi?
- Làm sao so đúng cặp swing point để tránh SMT giả?
- Điều gì biến một SMT thành tín hiệu giả (3 nguyên nhân)?
- Tiêu chí nào phân biệt SMT cấp A+ với cấp C?
- Lệnh nào trong journal của tôi có SMT xác nhận — win-rate/expectancy nhóm A+ khác nhóm không có SMT ra sao?

---

## 19. Flashcards / Active Recall

### Q1
**Hỏi:** SMT Divergence là gì trong 1 câu?
**Đáp:** Hai tài sản tương quan lệch pha tại cực trị (một cái quét pool, cái kia không) → xác nhận cực trị là terminal và có thể đảo chiều.

### Q2
**Hỏi:** SMT nên dùng ở bước nào trong quy trình vào lệnh?
**Đáp:** Ở bước **xác nhận** — sau khi có sweep, đi kèm CISD/MSS + FVG. SMT không phải trigger.

### Q3
**Hỏi:** Với EURUSD không có "cặp anh em" rõ, dùng gì để đọc SMT?
**Đáp:** Dùng **DXY** làm benchmark nghịch — DXY quét đỉnh mà EURUSD giữ đáy = bullish SMT.

### Q4
**Hỏi:** Vì sao SMT mạnh hơn phân kỳ RSI/MACD?
**Đáp:** RSI/MACD chỉ so giá với hàm toán của chính nó (một nguồn dữ liệu, lagging). SMT so hai dòng order flow độc lập nhưng cùng một engine phân phối → bằng chứng cross-sectional, khó ngụy tạo.

### Q5
**Hỏi:** Ba nguyên nhân biến SMT thành tín hiệu giả?
**Đáp:** (1) sai cặp tương quan; (2) SMT giữa range xa pool; (3) lệch nến/lệch swing (so sai cặp cực trị). Thêm: đọc quanh tin riêng của một tài sản.

### Q6
**Hỏi:** SMT liên hệ với Power of Three thế nào?
**Đáp:** SMT thường in ra đúng tại đỉnh/đáy của **Judas swing** (Manipulation) → xác nhận Manipulation kết thúc, Distribution (chân thật) sắp bắt đầu.

### Q7
**Hỏi:** Cấp A+ của SMT cần những gì?
**Đáp:** Cặp tương quan lõi + tại pool HTF + trong killzone/macro + thuận Daily Bias + đủ sweep + CISD/MSS + FVG.

### Q8
**Hỏi:** Nguyên tắc SMT đa khung?
**Đáp:** Khung trên (H4/H1) quyết định **hướng**; khung dưới (M5/M1) quyết định **giờ vào**. Không để LTF SMT kéo đi ngược HTF bias.
