---
type: ict-concept
concept: Change in State of Delivery
aliases:
  - Change in State of Delivery
  - CISD
  - Change in the State of Delivery
  - Đổi trạng thái giao hàng
tags:
  - trading/ict/concept
  - trading/study
  - "#market-structure"
  - "#entry-trigger"
status: developing
category: Market Structure
timeframes:
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
  - "[[35 - Aggressive Displacement Entry]]"
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
  - "[[21 - Market Structure Shift]]"
  - "[[09 - Change of Character]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[25 - OB - Order Block]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]"
  - "[[26 - OTE - Optimal Trade Entry]]"
  - "[[42 - SMT Divergence]]"
prerequisites:
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
common_mistakes:
  - "[[Mistake - Enter before liquidity sweep]]"
  - "[[Mistake - Entry When MSS not in POI Zone]]"
---

# Change in State of Delivery

> [!summary] Tóm tắt 1 câu
> **CISD (Change in State of Delivery) là khoảnh khắc giá ĐÓNG CỬA vượt qua GIÁ MỞ CỬA của chuỗi nến giao hàng cuối cùng theo hướng ngược lại — báo hiệu thuật toán đã lật "trạng thái giao hàng" từ bán-side sang buy-side (hoặc ngược lại).** Nó là phiên bản *sớm hơn và định lượng hơn* của MSS: MSS đo bằng swing high/low, CISD đo bằng open của chuỗi đẩy.

> [!important] Nguyên tắc cốt lõi
> "Delivery" là cách thuật toán IPDA **giao giá** cho thị trường theo một hướng. Một chuỗi nến cùng màu = một chân giao hàng. CISD chỉ có giá trị khi nó xảy ra **sau một cú sweep thanh khoản tại cực trị**, **thuận Daily Bias**, và **trong killzone**. CISD giữa range, ngược bias, hoặc chưa có sweep = tín hiệu giả. Câu thần chú: *"CISD không phải là lý do để đảo chiều — nó là bằng chứng rằng lý do đảo chiều (sweep + POI) đã hoàn tất."*

---

## 1. Định nghĩa

**Khái niệm:**
**Change in State of Delivery** là tín hiệu cấu trúc xác nhận rằng dòng lệnh (order flow) đã đổi chiều. Cụ thể: khi giá đang được "giao" xuống bằng một **chuỗi nến giảm liên tiếp** (bearish delivery), thì tín hiệu CISD bullish xuất hiện ở thời điểm một nến **đóng cửa BODY vượt lên trên giá MỞ CỬA của nến ĐẦU TIÊN trong chuỗi giảm đó**. Ngược lại cho bearish CISD. Đường kẻ tại giá mở cửa đó gọi là **CISD level**.

**Nguồn gốc tư duy:** CISD được ICT (Michael Huddleston) nhấn mạnh trong giai đoạn mentorship 2024 như một cách **đo sự đảo chiều chính xác hơn** so với việc chờ phá swing. Logic: nếu thuật toán vừa đẩy giá xuống bằng một loạt nến bán, thì việc giá **đóng cửa lấy lại toàn bộ điểm khởi đầu của loạt nến đó** chứng minh phe bán đã bị áp đảo hoàn toàn tại vùng đó — delivery đã đổi trạng thái.

![[CISD-Advanced-Anatomy.svg|697]]

*Giải phẫu: chuỗi nến đỏ đẩy giá xuống sweep SSL; CISD level = open của nến đỏ đầu tiên; khi nến xanh đóng qua level đó, delivery lật sang buy-side; displacement để lại FVG làm vùng entry.*

**Nó giúp trả lời câu hỏi nào trên chart?**
- Cú hồi vừa rồi chỉ là pullback hay đã là **đảo chiều thực sự** của dòng lệnh?
- Thao túng (manipulation) đã **kết thúc chưa** để chuyển sang pha phân phối?
- Điểm trigger **sớm nhất mà vẫn có bằng chứng** để vào lệnh nằm ở đâu?

### CISD KHÔNG phải là gì
- **Không phải** một tín hiệu vào lệnh máy móc — thấy CISD là mua/bán ngay. Nó cần sweep + POI + bias đi kèm.
- **Không phải** MSS. MSS phá swing; CISD phá open chuỗi đẩy. CISD thường in **trước** MSS (xem mục 4).
- **Không phải** vùng như Order Block — nó là **một mức giá tuyến tính** (một đường).
- **Không** tính khi chỉ có **wick** xuyên qua level; bắt buộc **thân nến đóng cửa** vượt qua.

---

## 2. Bối cảnh sử dụng

### Khi nào CISD có giá trị cao?
- [ ] Có Daily Bias rõ ràng và CISD in **thuận** bias
- [ ] Giá vừa **sweep thanh khoản** tại một cực trị (SSL/BSL, equal highs/lows)
- [ ] CISD xảy ra tại/gần một **POI HTF** (OB, FVG, breaker, OTE zone)
- [ ] Đang trong **killzone** (London / NY AM / NY PM) hoặc **macro window**
- [ ] Chuỗi nến đẩy trước CISD là **displacement rõ** (không phải nến lèo tèo)
- [ ] Có **SMT divergence** xác nhận cực trị là terminal ([[42 - SMT Divergence]])

### Khi nào nên bỏ qua?
- [ ] CISD xuất hiện **giữa range**, không ở cực trị
- [ ] Chưa có **sweep** trước đó — giá chưa lấy thanh khoản nào
- [ ] CISD **ngược Daily Bias** mà không có lý do HTF mạnh
- [ ] Chuỗi đẩy quá ngắn/nhiễu (1–2 nến doji) → CISD level không đáng tin
- [ ] Ngoài killzone, thanh khoản mỏng (giữa phiên Á, lunch NY)

---

## 3. Cấu trúc nhận diện & cách vẽ

![[CISD-Advanced-HowToDraw.svg|697]]

### Dấu hiệu chính
1. Một **chuỗi nến cùng màu liên tiếp** đẩy giá tới thanh khoản (đây là "delivery leg" cuối cùng).
2. Một cú **sweep** cực trị + rejection (wick từ chối) ngay cuối chuỗi.
3. Một nến **đối hướng đóng cửa BODY** vượt qua **open của nến đầu chuỗi** → CISD level bị phá.

### Điều kiện bắt buộc
- [ ] Xác định đúng **chuỗi giao hàng cuối cùng** (đoạn nến cùng màu không bị ngắt).
- [ ] CISD level = **open của nến đầu tiên** trong chuỗi đó (không phải nến bất kỳ).
- [ ] **Thân nến** (close) vượt qua level — wick không tính.
- [ ] Có **sweep thanh khoản** trước khi CISD in ra.

### Điều kiện tăng xác suất
- [ ] Nến phá CISD là **displacement** để lại FVG/imbalance
- [ ] CISD level trùng với một **Order Block / FVG / OTE** HTF
- [ ] Có **SMT divergence** giữa các cặp tương quan (NQ/ES, EU/GU, XAU/DXY)
- [ ] CISD in trong **macro window** (vd 09:50–10:10 ET cho NQ)
- [ ] Giá đang ở **Premium/Discount** đúng phía với hướng CISD

### Điều kiện làm setup yếu đi
- Chuỗi đẩy quá dài (>7–8 nến) → CISD level ở quá xa, stop rộng, RR xấu.
- Nến phá level là nến nhỏ, đóng sát mép (không displacement).
- CISD in ra trong vùng "no man's land" giữa premium và discount.

---

## 4. CISD vs MSS vs CHoCH — phân biệt sống còn

![[MSS-Advanced-CISD-vs-MSS.svg|697]]

Ba khái niệm này đều mô tả **sự đảo chiều dòng lệnh** nhưng đo bằng ba thước đo khác nhau và in ra ở ba thời điểm khác nhau:

| Khái niệm | Đo bằng | Thời điểm in | Ý nghĩa |
|---|---|---|---|
| **CISD** | Đóng qua **open chuỗi nến đẩy** | **Sớm nhất** | Delivery đổi trạng thái — nhạy, entry giá tốt |
| **MSS** ([[21 - Market Structure Shift]]) | Đóng qua **swing high/low** gần nhất | Trung bình | Cấu trúc thị trường đảo — chắc hơn CISD |
| **CHoCH** ([[09 - Change of Character]]) | Phá swing đối nghịch **đầu tiên** của trend | Trung bình–muộn | Đổi "tính cách" trend, dùng nhiều ở LTF |

> [!info] Vì sao CISD luôn in trước MSS
> Open của nến đầu chuỗi đẩy nằm **thấp hơn (gần hơn)** so với swing high phía trên (trong reversal bullish). Vì mốc gần hơn nên giá **chạm và đóng qua nó trước** khi kịp phá swing → CISD cho tín hiệu **sớm hơn**, đổi lại **rủi ro nhiễu cao hơn** nếu thiếu sweep + POI. Cách phối hợp tối ưu: dùng **CISD làm trigger sớm** để chuẩn bị, rồi **MSS làm xác nhận chắc** — hoặc vào một phần ở CISD, gia tăng ở MSS.

---

## 5. CISD vs Order Block — LEVEL vs ZONE

![[CISD-Advanced-vs-OrderBlock.svg|697]]

CISD là một **mức giá** (một đường), còn [[25 - OB - Order Block|Order Block]] là một **vùng** (dải high–low của nến gốc). Điều này quyết định cách dùng:

- **CISD** dễ đặt alert, cho **điểm trigger chính xác**, nhưng bản thân nó không phải vùng để "chờ giá phản ứng".
- **Order Block** cho **vùng entry** để đặt limit, nhưng điểm trigger kém chính xác hơn.
- **Đỉnh cao của confluence:** khi **CISD level nằm ngay trong Order Block** — bạn có cả điểm trigger sớm (CISD) lẫn vùng entry đẹp (OB) trùng nhau. Đây là kịch bản xác suất cao nhất.

---

## 6. CISD là fractal — chọn khung thời gian

![[CISD-Advanced-Timeframe.svg|697]]

CISD hoạt động ở **mọi khung** theo nguyên lý fractal. Quy tắc top-down ([[32 - Top-down Analysis (Multiple Timeframes)]]):

- **H4/H1 — Bias:** CISD trên HTF xác nhận **draw on liquidity đã đổi hướng**. Dùng để **chọn phe**, không phải để entry (entry sẽ quá muộn/stop rộng).
- **M15/M5 — Context:** chờ CISD tại POI HTF trong killzone → xác nhận thao túng kết thúc. Đây là **điểm cân bằng tốt nhất** giữa độ tin cậy và giá entry.
- **M1 — Entry:** CISD M1 cho **entry sớm nhất, stop nhỏ nhất**, nhưng **chỉ hợp lệ khi HTF + M5 đã đồng thuận**. CISD M1 đơn lẻ giữa nhiễu = bẫy.

---

## 7. Quy trình vào lệnh bằng CISD (4 bước)

![[CISD-Advanced-Entry-Sequence.svg|697]]

**Bước 1 — Xác nhận Daily Bias & vùng draw.** Biết giá đang muốn đi về đâu (BSL hay SSL) và đang ở Premium hay Discount. CISD chỉ tradeable khi in **thuận** hướng này.

**Bước 2 — Chờ sweep tại cực trị + đánh dấu CISD level.** Giá phải lấy thanh khoản (quét SSL/BSL, equal highs/lows) rồi mới tính CISD. Ngay khi có sweep, vẽ đường CISD tại open của chuỗi đẩy cuối.

**Bước 3 — Chờ nến đóng qua CISD level (displacement).** Một nến đối hướng đóng body qua level, tốt nhất là **displacement** để lại FVG. Đây là xác nhận delivery đã lật.

**Bước 4 — Entry ở retrace, không đuổi.** Đặt limit tại **FVG (50% CE)** hoặc **OB** trùng CISD level. **Stop dưới wick nến sweep** (bullish) / trên wick sweep (bearish). T1 = IRL gần nhất, T2 = ERL / draw on liquidity. Dời BE sau T1.

---

## 8. Ví dụ chart

### Ví dụ đúng
![[CISD-Example-Correct.svg|697]]

**Mô tả:** NQ, ngày bias **bullish** (HTF discount), killzone NY AM. Giá sweep đáy phiên Á (SSL) → một nến xanh **đóng qua CISD level** (open chuỗi đỏ) tạo displacement + FVG → giá hồi về FVG cho entry → delivery mua đẩy về BSL.

**Vì sao đây là ví dụ tốt:**
- CISD in **thuận Daily Bias**.
- CISD xuất hiện **ngay sau sweep** — có lý do rõ ràng để đảo chiều.
- Entry ở **retrace về FVG**, không đuổi nến displacement → stop hợp lý, RR đẹp.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lệnh NQ/EURUSD thật: đánh dấu (1) chuỗi nến đẩy + CISD level, (2) điểm sweep, (3) nến đóng qua level + FVG, (4) entry và stop. Ghi rõ khung thời gian và giờ ET.*

### Ví dụ sai / dễ nhầm
![[CISD-Example-Wrong.svg|697]]

**Mô tả lỗi:** Ngày bias **bearish** nhưng vào **long** chỉ vì thấy một nến đóng qua open chuỗi giảm — nhưng CISD này nằm **giữa range**, **chưa có sweep** thanh khoản nào, và **ngược bias**. Giá tiếp tục giảm về SSL (draw thật) → chạm stop.

**Bài học:**
- CISD **giữa range** không có giá trị — nó phải ở **cực trị sau sweep**.
- CISD **ngược bias** cần lý do HTF cực mạnh; mặc định là bỏ qua.
- Không có sweep = không có "lý do đảo chiều" → CISD chỉ là nhiễu pullback.

---

## 9. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[20 - Liquidity Sweep]] — điều kiện tiên quyết trước CISD
- [[21 - Market Structure Shift]] — xác nhận chắc hơn, in sau CISD
- [[13 - FVG  - Fair Value Gap]] — vùng entry sau CISD
- [[25 - OB - Order Block]] — trùng CISD level = confluence
- [[26 - OTE - Optimal Trade Entry]] — vùng retrace tối ưu
- [[42 - SMT Divergence]] — xác nhận cực trị terminal
- [[10 - Consequent Encroachment (Mean Threshold)]] — điểm limit trong FVG

### Sequence mẫu
```text
HTF Bias → Discount/Premium → POI HTF → Sweep cực trị → CISD close (open chuỗi đẩy) → Displacement/FVG → Entry (50% CE / OB tại CISD level) → IRL (T1) → ERL/Draw (T2)
```

---

## 10. Thực hành tốt nhất (Best Practices)

> [!tip] 6 quy tắc CISD
> 1. **Luôn chờ sweep trước** — CISD không sweep = pullback giả.
> 2. **Đo đúng chuỗi** — CISD level là open nến ĐẦU của chuỗi giao hàng cuối, không phải nến bất kỳ.
> 3. **Chỉ tính khi thân nến đóng qua level** — wick xuyên không được tính.
> 4. **Ưu tiên CISD trùng POI HTF** (OB/FVG/OTE) → entry chính xác + xác nhận cấu trúc.
> 5. **Dùng CISD làm trigger, MSS làm xác nhận** — có thể vào một phần ở CISD, gia tăng ở MSS.
> 6. **Không bao giờ CISD ngược Daily Bias** nếu không có narrative HTF rất mạnh.

- Đặt **alert** tại CISD level ngay khi thấy sweep → không phải dán mắt vào chart chờ nến đóng.
- Trên LTF, ưu tiên CISD tạo bởi **displacement mạnh** (nến thân dài, đóng gần đỉnh/đáy) — displacement yếu = delivery yếu.
- Ghép CISD với **macro window** ([[40 - Macro Times]]): CISD in trong 09:50–10:10 ET (NQ) có xác suất cao hơn hẳn CISD ngoài macro.
- Ghi nhật ký: mỗi lệnh nên đánh dấu **CISD in ở khung nào** và **có trùng POI/SMT không** để đo edge từng loại setup theo thời gian.
- Với người mới: hãy **chờ MSS xác nhận** thay vì vào ngay CISD, cho đến khi backtest chứng minh bạn đọc CISD đủ tốt.

---

## 11. Checklist trước khi trade một CISD

> [!warning] Không trade chỉ vì "thấy một nến đóng qua open chuỗi đẩy"
> CISD chỉ có giá trị khi đứng trong đúng context: sweep + POI + bias + killzone.

- [ ] Daily Bias rõ ràng (D1/H4) và CISD thuận bias
- [ ] Giá đã **sweep** một cực trị thanh khoản rõ ràng
- [ ] Xác định đúng chuỗi giao hàng cuối → CISD level chính xác
- [ ] Thân nến đóng qua CISD level (không phải wick)
- [ ] CISD nằm tại/gần POI HTF (OB/FVG/OTE)
- [ ] Có displacement tạo FVG cho vùng entry
- [ ] Đang trong killzone / macro window
- [ ] (Ưu tiên) có SMT divergence xác nhận
- [ ] Entry ở retrace (FVG 50% CE / OB), không đuổi nến
- [ ] Stop có logic (dưới/trên wick sweep); T1 = IRL, T2 = ERL
- [ ] RR tối thiểu đạt kế hoạch
- [ ] Không revenge / FOMO

---

## 12. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| CISD giữa range | Vào lệnh khi giá chưa lấy thanh khoản | Chỉ tính CISD ở cực trị SAU sweep |
| Đo sai chuỗi đẩy | Kẻ CISD level tại open nến bất kỳ | Dùng open nến ĐẦU của chuỗi cùng màu liên tiếp |
| Tính wick là đóng cửa | Wick xuyên level đã coi là CISD | Chỉ tính khi **thân nến (close)** vượt level |
| CISD ngược bias | LTF đẹp nhưng ngược hướng ngày | Bias filter bắt buộc; ngược bias = bỏ qua |
| Đuổi nến displacement | Market order ngay khi CISD in | Chờ hồi về FVG/OB, đặt limit |
| Nhầm CISD với MSS | Chờ phá swing rồi mới gọi là CISD | CISD = open chuỗi đẩy; MSS = swing |

---

## 13. Câu hỏi tự kiểm tra

- Tôi giải thích được CISD trong 30 giây và phân biệt với MSS không?
- CISD level được đo từ đâu — open của nến nào?
- Vì sao CISD luôn có cơ hội in trước MSS?
- Điều gì biến một CISD thành tín hiệu giả?
- Lệnh nào trong journal của tôi vào bằng CISD — kết quả và edge so với vào bằng MSS ra sao?

---

## 14. Flashcards / Active Recall

### Q1
**Hỏi:** CISD được đo bằng gì và in ra khi nào?
**Đáp:** Đo bằng giá OPEN của nến đầu tiên trong chuỗi giao hàng cuối; in ra khi một nến đối hướng ĐÓNG CỬA body vượt qua mức đó.

### Q2
**Hỏi:** Điều kiện quan trọng nhất để CISD hợp lệ là gì?
**Đáp:** Phải có **sweep thanh khoản tại cực trị trước đó**, thuận Daily Bias, và tốt nhất là trùng POI HTF trong killzone.

### Q3
**Hỏi:** Khác biệt cốt lõi giữa CISD và MSS?
**Đáp:** CISD phá **open chuỗi nến đẩy** (in sớm, nhạy); MSS phá **swing high/low** (in muộn hơn, chắc hơn).

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
- ICT 2024 Mentorship — Change in State of Delivery & order flow.
- ICT — Market Structure Shift vs CISD (đo swing vs đo open chuỗi đẩy).
- Concept nội bộ: [[21 - Market Structure Shift]], [[20 - Liquidity Sweep]], [[13 - FVG  - Fair Value Gap]].

---

## 17. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa & cách đo | | |
| Vẽ đúng CISD level | | |
| Phân biệt CISD / MSS / CHoCH | | |
| Kết hợp sweep + POI + bias | | |
| Áp dụng vào trade thực tế | | |

**Kế hoạch review tiếp theo:**
