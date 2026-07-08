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
status: seed
category: Confirmation
timeframes:
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 2
last_reviewed: 2026-07-05
created: 2026-07-05
updated: 2026-07-05
related_concepts:
  - "[[20 - Liquidity Sweep]]"
  - "[[19 - Liquidity]]"
  - "[[41 - Change in State of Delivery]]"
  - "[[21 - Market Structure Shift]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
  - "[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]"
  - "[[33 - Turtle Soup]]"
prerequisites:
  - "[[20 - Liquidity Sweep]]"
  - "[[19 - Liquidity]]"
  - "[[12 - Daily Bias]]"
common_mistakes:
  - "[[02 - Mistake - Enter before liquidity sweep]]"
---

# SMT Divergence

> [!summary] Tóm tắt 1 câu
> **SMT (Smart Money Technique) Divergence là hiện tượng hai tài sản CÓ TƯƠNG QUAN "lệch pha" tại một cực trị — một cái tạo đỉnh/đáy mới còn cái kia thì không — để lộ dấu chân của smart money và xác nhận rằng cực trị đó là TERMINAL (điểm cuối cùng), không phải điểm tiếp diễn.**

> [!important] Nguyên tắc cốt lõi
> Hai tài sản tương quan (NQ/ES, EURUSD/GBPUSD, XAU/DXY) về lý thuyết nên đi cùng nhịp. Khi một cái **quét thanh khoản** (tạo lower low/higher high mới) còn cái kia **từ chối theo** (giữ đáy/không phá đỉnh), sự "lệch" đó cho thấy dòng lệnh tổ chức đang **hấp thụ ngược hướng** — sweep là cú lấy thanh khoản cuối cùng chứ không phải khởi đầu xu hướng mới. SMT **là xác nhận, không phải trigger**: nó nói *"cực trị này đáng tin"*, nhưng entry vẫn cần sweep + CISD/MSS + POI.

---

## 1. Định nghĩa

**Khái niệm:**
**SMT Divergence** so sánh **cấu trúc đỉnh/đáy** của hai (hoặc nhiều) công cụ tương quan tại **cùng một thời điểm** để phát hiện sự bất đồng. Trong một **bullish SMT** ở đáy: tài sản A tạo **lower low** (quét sell-side liquidity) trong khi tài sản B tạo **higher low** (không phá đáy cũ). Sự lệch này báo hiệu phe bán đã kiệt sức tại A và smart money đang gom → khả năng đảo chiều **tăng**. Bearish SMT là gương phản chiếu ở đỉnh.

**Nguồn gốc & vì sao nó hoạt động:** Đây là một trong những "smart money technique" lâu đời nhất của ICT. Logic: các chỉ số/cặp tiền tương quan được cùng một dòng vốn tổ chức điều khiển. Nếu một cú đẩy xuống là **thật** (bắt đầu xu hướng giảm mới), **cả hai** phải tạo đáy thấp hơn. Khi chỉ **một** cái làm được, cú phá đáy còn lại chỉ là **liquidity run** (quét stop) — một cái bẫy. SMT giúp phân biệt **sweep terminal** với **breakout thật**.

![[SMT-Advanced-Anatomy.svg|697]]

*Bullish SMT: NQ tạo lower low và quét SSL, trong khi ES giữ higher low (không quét). Sự lệch pha này = tín hiệu đảo chiều tăng.*

**Nó giúp trả lời câu hỏi nào trên chart?**
- Cú phá đỉnh/đáy vừa rồi là **breakout thật** hay chỉ là **liquidity sweep** (bẫy)?
- Cực trị này có phải là **điểm cuối** của cú swing để tôi tự tin đảo chiều không?
- Daily Bias của tôi có được **xác nhận liên thị trường** không?

### SMT KHÔNG phải là gì
- **Không phải** trigger vào lệnh — nó là **lớp xác nhận** thêm vào sweep + CISD/MSS.
- **Không phải** RSI/MACD divergence (phân kỳ giữa giá và chỉ báo). SMT là phân kỳ giữa **hai giá của hai tài sản**.
- **Không** dùng được giữa hai tài sản **không tương quan** (vd NQ vs Gold).
- **Không** có giá trị nếu xuất hiện **giữa range**, xa các pool thanh khoản.

---

## 2. Bối cảnh sử dụng

### Khi nào SMT có giá trị cao?
- [ ] So giữa hai tài sản **tương quan thật** (NQ/ES, EU/GU, XAU/DXY)
- [ ] Divergence xảy ra tại **cực trị có thanh khoản** (SSL/BSL, equal highs/lows)
- [ ] Trùng với **Daily Bias** đã xác định
- [ ] Trong **killzone** / macro window
- [ ] Đi kèm **sweep + CISD/MSS + FVG** (SMT là mảnh ghép xác nhận cuối)
- [ ] Giá đang ở vùng **Premium/Discount** hợp lý

### Khi nào nên bỏ qua?
- [ ] Hai tài sản **tương quan yếu** hoặc không tương quan
- [ ] Divergence ở **giữa range**, không có pool thanh khoản
- [ ] Chỉ có SMT nhưng **không có sweep** hay trigger cấu trúc
- [ ] Ngược Daily Bias mà không có narrative HTF mạnh
- [ ] Tương quan **tạm thời đảo** do tin riêng của một tài sản (vd earnings 1 cổ phiếu ảnh hưởng chỉ số)

---

## 3. Bullish SMT vs Bearish SMT

![[SMT-Advanced-BullBear.svg|697]]

**Bullish SMT (tại ĐÁY):** A tạo **lower low** (quét SSL) nhưng B tạo **higher low** (không theo). Kỳ vọng: đảo chiều **tăng**. Chờ SSL bị quét, tìm entry **long**.

**Bearish SMT (tại ĐỈNH):** A tạo **higher high** (quét BSL) nhưng B tạo **lower high** (không theo). Kỳ vọng: đảo chiều **giảm**. Chờ BSL bị quét, tìm entry **short**.

> [!tip] Đọc phe nào là "leader", phe nào "laggard"
> Tài sản **không chịu** tạo cực trị mới thường là phe **mạnh hơn** (đang được smart money bảo vệ). Ở bullish SMT, tài sản giữ higher low = phe mua mạnh hơn → xác nhận thiên hướng mua. Đây là cách SMT tinh chỉnh **Daily Bias** liên thị trường.

---

## 4. Bản đồ cặp tương quan

![[SMT-Advanced-CorrelationMap.svg|697]]

SMT **chỉ hợp lệ** giữa các tài sản có tương quan thật. Có hai loại tương quan cần phân biệt rõ:

**Tương quan THUẬN (so cùng chiều):**
- Chỉ số Mỹ: **NQ ↔ ES ↔ YM ↔ RTY** — NQ vs ES là cặp SMT kinh điển nhất.
- Forex: **EURUSD ↔ GBPUSD** (đều nghịch USD nên thuận nhau).
- Kim loại: **XAUUSD ↔ XAGUSD** (vàng ↔ bạc).

**Tương quan NGHỊCH (so ngược chiều):**
- **EURUSD/GBPUSD/XAUUSD ↔ DXY** — khi DXY quét đỉnh mà EURUSD không phá đáy = bullish SMT cho EURUSD.
- **Gold ↔ US10Y (lợi suất)** — thường nghịch nhau.

> [!warning] Cạm bẫy tương quan
> Tương quan **không cố định**. Trong các giai đoạn tin tức riêng lẻ (một big-tech công bố earnings kéo NQ lệch ES; BoE/ECB ra tin kéo GBP lệch EUR), tương quan có thể tạm gãy và tạo "SMT giả". Luôn ưu tiên SMT tại **cực trị có pool** và trong **killzone**, tránh đọc SMT quanh giờ tin đỏ của riêng một tài sản.

---

## 5. SMT nghịch đảo — đọc với DXY

![[SMT-Advanced-Inverse.svg|697]]

Với cặp **nghịch tương quan**, đỉnh của cái này nên khớp **đáy** của cái kia. Ví dụ điển hình cho trader forex/vàng: dùng **DXY** làm "tấm gương".

- Nếu **DXY tạo higher high (quét đỉnh)** nhưng **EURUSD KHÔNG tạo lower low (giữ đáy)** → **bullish SMT** cho EURUSD: USD đang bị hấp thụ ở đỉnh, EUR sắp tăng.
- Ngược lại, **DXY tạo lower low** nhưng **EURUSD không phá đỉnh** → **bearish SMT** cho EURUSD.

Đây là công cụ mạnh để xác nhận sweep trên forex/vàng khi bạn không có "cặp anh em" rõ ràng — DXY đóng vai trò benchmark cho toàn bộ rổ USD.

---

## 6. SMT + Sweep + CISD/MSS — thang confluence

![[SMT-Advanced-Entry-Confluence.svg|697]]

SMT phát huy sức mạnh khi là **mảnh ghép cuối** của chuỗi xác nhận, không phải khi đứng một mình:

- **SMT đơn lẻ** = chỉ là *cảnh báo* cực trị có thể terminal. Không trade.
- **SMT + sweep** = có *lý do* đảo chiều (thanh khoản đã bị lấy).
- **SMT + sweep + CISD/MSS** = có *trigger* cấu trúc → tradeable.
- **SMT + sweep + CISD/MSS + FVG/OB + killzone** = **A+ setup** — vào tại FVG (50% CE), stop sau wick sweep.

> [!info] Vì sao SMT làm entry mạnh hơn hẳn
> SMT trả lời câu hỏi mà sweep + CISD **không** trả lời được: *"cú sweep này có phải cú cuối không?"*. Một sweep có thể là cú đầu của chuỗi sweep sâu hơn. Nhưng nếu tài sản tương quan **từ chối** theo, xác suất đây là **cú lấy thanh khoản cuối cùng** tăng vọt → giảm mạnh tỉ lệ dính "sweep chồng sweep".

---

## 7. Quy trình đọc SMT khi vào lệnh

**Bước 1 — Mở song song hai chart tương quan.** Ví dụ NQ + ES cạnh nhau (hoặc EURUSD + DXY). Căn cùng khung thời gian, cùng mốc thời gian.

**Bước 2 — Chờ giá tiếp cận một pool thanh khoản HTF.** Chỉ tìm SMT tại các cực trị có nghĩa (SSL/BSL, equal highs/lows, PDH/PDL) — không phải giữa range.

**Bước 3 — So cấu trúc tại cực trị.** Một tài sản quét pool (tạo cực trị mới), cái kia không theo → SMT hình thành. Xác nhận nó **thuận Daily Bias**.

**Bước 4 — Chờ trigger trên instrument bạn giao dịch.** Sweep + **CISD/MSS** + displacement/FVG. SMT chỉ là đèn xanh xác nhận; trigger cấu trúc mới là điểm vào.

**Bước 5 — Entry, stop, target.** Entry tại FVG (50% CE) hoặc OB; **stop sau wick của cú sweep** (chính là điểm tạo lower low/higher high); T1 = IRL, T2 = ERL/draw on liquidity.

---

## 8. Ví dụ chart

### Ví dụ đúng
![[Liquidity-Sweep-Advanced-SMT.svg|697]]

**Mô tả:** Tại vùng discount, NQ quét SSL (tạo lower low) trong khi ES giữ higher low → **bullish SMT**. Ngay sau đó NQ in **CISD/MSS**, để lại FVG. Entry long tại FVG, stop dưới wick sweep, target BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- So đúng cặp tương quan kinh điển (**NQ ↔ ES**).
- SMT xảy ra **tại pool thanh khoản** (SSL), không phải giữa range.
- Có đủ chuỗi: **SMT (xác nhận) + sweep (lý do) + CISD/MSS (trigger) + FVG (entry)**.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp 2 chart cạnh nhau (NQ+ES hoặc EURUSD+DXY): đánh dấu (1) cực trị lệch pha, (2) tài sản nào quét/không quét, (3) sweep + CISD/MSS trên instrument giao dịch, (4) entry/stop/target.*

### Ví dụ sai / dễ nhầm
![[SMT-Example-Wrong.svg|697]]

**Mô tả lỗi:** (1) So hai tài sản **không tương quan** (NQ vs Gold) → "lệch pha" là ngẫu nhiên, vô nghĩa. (2) Divergence xuất hiện **giữa range**, xa mọi pool thanh khoản → nhiễu, không phải tín hiệu.

**Bài học:**
- SMT chỉ có nghĩa giữa **tài sản tương quan thật**.
- SMT phải nằm **tại cực trị có thanh khoản**, không phải giữa range.
- SMT **không thay thế** sweep + trigger; thiếu chúng thì SMT chỉ là quan sát.

---

## 9. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[20 - Liquidity Sweep]] — SMT xác nhận sweep là terminal
- [[41 - Change in State of Delivery]] — trigger đi kèm SMT
- [[21 - Market Structure Shift]] — xác nhận cấu trúc sau SMT
- [[13 - FVG  - Fair Value Gap]] — vùng entry
- [[33 - Turtle Soup]] — SMT tăng độ tin cho setup turtle soup
- [[12 - Daily Bias]] — SMT tinh chỉnh bias liên thị trường
- [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] — target sau đảo chiều

### Sequence mẫu
```text
HTF Bias → Discount/Premium → Pool thanh khoản HTF → Sweep (A quét, B không) = SMT → CISD/MSS → FVG/OB Entry → IRL (T1) → ERL/Draw (T2)
```

---

## 10. Thực hành tốt nhất (Best Practices)

> [!tip] 6 quy tắc SMT
> 1. **Chỉ so tài sản tương quan thật** — NQ/ES, EU/GU, XAU/DXY. Sai cặp = tín hiệu rác.
> 2. **SMT phải nằm tại pool thanh khoản** — cực trị có SSL/BSL, không phải giữa range.
> 3. **SMT là xác nhận, không phải trigger** — luôn chờ sweep + CISD/MSS mới vào.
> 4. **Căn đúng cùng khung + cùng thời điểm** hai chart, tránh lệch nến gây ảo giác divergence.
> 5. **Với cặp nghịch, so ngược chiều** (DXY quét đỉnh ↔ EURUSD giữ đáy).
> 6. **Tránh SMT quanh tin riêng** của một tài sản (earnings, phát biểu ngân hàng TW).

- Mở sẵn **layout 2 chart** (instrument giao dịch + benchmark tương quan) để không phải chuyển tab lúc quyết định.
- Ưu tiên SMT trên **HTF (H1/H4)** để chọn bias, rồi tìm SMT **LTF (M5/M1)** cùng hướng cho entry — SMT đồng thuận đa khung là cực mạnh.
- Ghép SMT với **macro window** ([[40 - Macro Times]]): SMT hình thành ngay trong 09:50–10:10 ET là confluence hạng nhất cho NQ.
- Với XAUUSD/forex, dùng **DXY** làm benchmark mặc định vì nó phản ánh cả rổ USD.
- Ghi nhật ký: gắn nhãn mỗi lệnh *có/không có SMT xác nhận* để đo edge — nhiều trader thấy win-rate tăng rõ rệt ở nhóm "có SMT".

---

## 11. Checklist trước khi dùng SMT vào trade

> [!warning] SMT không phải là nút "mua/bán"
> Nó chỉ xác nhận cực trị đáng tin. Entry vẫn cần sweep + trigger + POI.

- [ ] Đang so đúng **cặp tương quan thật**
- [ ] Căn cùng khung thời gian, cùng thời điểm nến
- [ ] Divergence nằm **tại pool thanh khoản** (không giữa range)
- [ ] SMT **thuận Daily Bias**
- [ ] Có **sweep** thực sự tại cực trị
- [ ] Có **CISD/MSS** trigger trên instrument giao dịch
- [ ] Có **FVG/OB** cho vùng entry
- [ ] Đang trong killzone / macro
- [ ] Với cặp nghịch: đã so **ngược chiều** đúng cách
- [ ] Stop sau wick sweep; T1 = IRL, T2 = ERL
- [ ] Không đọc SMT quanh giờ tin riêng của một tài sản

---

## 12. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Sai cặp tương quan | So NQ với Gold, EUR với BTC | Chỉ dùng cặp tương quan thật (NQ/ES, EU/GU, XAU/DXY) |
| SMT giữa range | Divergence xa pool thanh khoản | Chỉ đọc SMT tại cực trị có SSL/BSL |
| Coi SMT là trigger | Vào lệnh ngay khi thấy lệch pha | SMT là xác nhận; chờ sweep + CISD/MSS |
| Lệch nến giữa 2 chart | Divergence "ảo" do lệch thời gian | Căn cùng khung + cùng mốc thời gian |
| Nhầm với chỉ báo divergence | So giá với RSI/MACD | SMT = phân kỳ giữa 2 tài sản, không phải chỉ báo |
| Bỏ qua tin riêng | Đọc SMT lúc earnings/BoE | Tránh cực trị bị bóp méo bởi tin của một tài sản |

---

## 13. Câu hỏi tự kiểm tra

- Tôi giải thích được SMT trong 30 giây và phân biệt với RSI divergence không?
- Cặp tương quan mặc định cho NQ / cho EURUSD / cho XAUUSD là gì?
- SMT là bias, POI, entry hay xác nhận? Tôi dùng nó ở bước nào trong chuỗi?
- Điều gì biến một SMT thành tín hiệu giả?
- Lệnh nào trong journal của tôi có SMT xác nhận — win-rate khác nhóm không có SMT ra sao?

---

## 14. Flashcards / Active Recall

### Q1
**Hỏi:** SMT Divergence là gì trong 1 câu?
**Đáp:** Hai tài sản tương quan lệch pha tại cực trị (một cái quét pool, cái kia không) → xác nhận cực trị là terminal và có thể đảo chiều.

### Q2
**Hỏi:** SMT nên dùng ở bước nào trong quy trình vào lệnh?
**Đáp:** Ở bước **xác nhận** — sau khi có sweep, đi kèm CISD/MSS + FVG. SMT không phải trigger.

### Q3
**Hỏi:** Với EURUSD không có "cặp anh em" rõ, dùng gì để đọc SMT?
**Đáp:** Dùng **DXY** làm benchmark nghịch — DXY quét đỉnh mà EURUSD giữ đáy = bullish SMT.

---

## 15. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault dùng path riêng cho trades, thay `FROM ""` bằng ví dụ `FROM "05 - Live Trading Journal/Trades"`.

---

## 16. Nguồn tham khảo
- ICT Mentorship — Smart Money Technique (SMT) Divergence.
- ICT — Interbank correlation & USD index (DXY) như benchmark.
- Concept nội bộ: [[20 - Liquidity Sweep]], [[41 - Change in State of Delivery]], [[12 - Daily Bias]].

---

## 17. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa & logic | | |
| Chọn đúng cặp tương quan | | |
| Đọc SMT tại pool (không giữa range) | | |
| Kết hợp SMT + sweep + trigger | | |
| Áp dụng vào trade thực tế | | |

**Kế hoạch review tiếp theo:**
