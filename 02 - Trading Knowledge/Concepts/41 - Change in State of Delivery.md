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
last_reviewed: 2026-07-07
created: 2026-07-05
updated: 2026-07-07
---

# Change in State of Delivery

> [!summary] Tóm tắt 1 câu
> **CISD (Change in State of Delivery) là khoảnh khắc giá ĐÓNG CỬA vượt qua GIÁ MỞ CỬA của chuỗi nến giao hàng cuối cùng theo hướng ngược lại — báo hiệu thuật toán đã lật "trạng thái giao hàng" từ sell-side sang buy-side (hoặc ngược lại).** Nó là phiên bản *sớm hơn và định lượng hơn* của MSS: MSS đo bằng swing high/low, CISD đo bằng open của chuỗi đẩy.

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
- **Không phải** MSS. MSS phá swing; CISD phá open chuỗi đẩy. CISD thường in **trước** MSS (xem mục 5).
- **Không phải** vùng như Order Block — nó là **một mức giá tuyến tính** (một đường).
- **Không** tính khi chỉ có **wick** xuyên qua level; bắt buộc **thân nến đóng cửa** vượt qua.

---

## 2. Cơ chế thuật toán: vì sao "delivery" đo bằng OPEN

![[CISD-Advanced-Algorithm.svg|697]]

Đây là phần cốt lõi tách người hiểu CISD sâu khỏi người chỉ vẽ đường theo công thức.

**"Delivery" nghĩa là gì?** ICT mô hình hoá thị trường như một **thuật toán giao giá (price delivery)** — IPDA (Interbank Price Delivery Algorithm). Thuật toán không "mua/bán" theo cảm xúc; nó **giao giá theo một chương trình** hướng về một mục tiêu thanh khoản (draw on liquidity, xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]). Khi đang giao xuống, ta thấy một **chuỗi nến giảm cùng màu** — đó là một "chân giao hàng" (delivery leg) thể hiện chương trình đang chạy theo chiều bán.

**Vì sao mốc quan trọng là OPEN, không phải low hay close?**
- **Open của nến đầu chuỗi = nơi chương trình bán bắt đầu.** Nó là "dấu vân tay" của ý định thuật toán tại thời điểm khởi động leg đó.
- Khi giá **đóng cửa body vượt trở lại qua open đó**, toàn bộ vùng giá mà chương trình bán đã "giao" bị **lấy lại hoàn toàn** — không còn nến bán nào của leg đó còn giữ quyền kiểm soát. Đây chính là "đổi trạng thái".
- **Low chỉ là nơi sweep** — nơi thanh khoản bị lấy, không phải nơi ý định bắt đầu. Dùng low để đo đảo chiều sẽ nhiễu (mỗi wick dài lại báo sai).
- **Close của các nến giữa chuỗi** cũng không đại diện cho điểm khởi đầu ý định; chỉ open nến đầu mới là mốc "state".

> [!info] Tư duy "state machine"
> Coi thị trường như một máy trạng thái hai chiều: **SELL-SIDE state** ⇄ **BUY-SIDE state**. Chuyển trạng thái chỉ hợp lệ khi có **trigger đủ mạnh**: (1) sweep thanh khoản cực trị + (2) đóng qua open của leg. Thiếu một trong hai, "chuyển trạng thái" chỉ là nhiễu — giá vẫn ở state cũ và sẽ tiếp tục giao theo hướng cũ. Đây là lý do CISD **không sweep = pullback giả**.

**Hệ quả thực chiến:** vì open nằm gần hơn swing, CISD **in sớm hơn** MSS (mục 5). Đổi lại, tín hiệu sớm hơn = nhiễu hơn, nên bắt buộc phải lọc bằng context (sweep + POI + bias). CISD là công cụ *sắc* nhưng *cần tay nghề*.

---

## 3. Bối cảnh sử dụng

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

## 4. Cấu trúc nhận diện & cách vẽ

![[CISD-Advanced-HowToDraw.svg|697]]

### Dấu hiệu chính
1. Một **chuỗi nến cùng màu liên tiếp** đẩy giá tới thanh khoản (đây là "delivery leg" cuối cùng).
2. Một cú **sweep** cực trị + rejection (wick từ chối) ngay cuối chuỗi.
3. Một nến **đối hướng đóng cửa BODY** vượt qua **open của nến đầu chuỗi** → CISD level bị phá.

### Cách đếm "chuỗi giao hàng cuối" cho chính xác
Đây là chỗ 80% lỗi vẽ CISD xảy ra. Quy tắc thực hành:
- Bắt đầu từ **cực trị (đáy/đỉnh vừa sweep)** và đếm ngược lên: gộp các nến **cùng màu liên tiếp** thành một chuỗi.
- Một hoặc hai **nến ngược màu thân rất nhỏ (doji/inside)** nằm giữa chuỗi thường được **bỏ qua** nếu chúng không phá cấu trúc vi mô — chúng chỉ là "nghỉ" trong cùng một leg giao hàng.
- **CISD level = open của nến ĐẦU TIÊN** của chuỗi đó (nến ở trên cùng, xa cực trị nhất).
- Nếu có nghi ngờ giữa hai cách đếm, chọn cách cho **level bảo thủ hơn** (xa hơn) để tránh tín hiệu giả; hoặc chờ **MSS xác nhận**.

### Điều kiện bắt buộc
- [ ] Xác định đúng **chuỗi giao hàng cuối** (đoạn nến cùng màu không bị ngắt).
- [ ] CISD level = **open của nến đầu tiên** trong chuỗi đó (không phải nến bất kỳ).
- [ ] **Thân nến** (close) vượt qua level — wick không tính.
- [ ] Có **sweep thanh khoản** trước khi CISD in ra.

### Điều kiện tăng xác suất
- [ ] Nến phá CISD là **displacement** để lại FVG/imbalance ([[13 - FVG  - Fair Value Gap|FVG]])
- [ ] CISD level trùng với một **Order Block / FVG / OTE** HTF
- [ ] Có **SMT divergence** giữa các cặp tương quan (NQ/ES, EU/GU, XAU/DXY)
- [ ] CISD in trong **macro window** (vd 09:50–10:10 ET cho NQ)
- [ ] Giá đang ở **Premium/Discount** đúng phía với hướng CISD ([[27 - Premium Discount]])

### Điều kiện làm setup yếu đi
- Chuỗi đẩy quá dài (>7–8 nến) → CISD level ở quá xa, stop rộng, RR xấu.
- Nến phá level là nến nhỏ, đóng sát mép (không displacement).
- CISD in ra trong vùng "no man's land" giữa premium và discount.

---

## 5. CISD vs MSS vs CHoCH — phân biệt sống còn

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

## 6. CISD vs Order Block — LEVEL vs ZONE

![[CISD-Advanced-vs-OrderBlock.svg|697]]

CISD là một **mức giá** (một đường), còn [[25 - OB - Order Block|Order Block]] là một **vùng** (dải high–low của nến gốc). Điều này quyết định cách dùng:

- **CISD** dễ đặt alert, cho **điểm trigger chính xác**, nhưng bản thân nó không phải vùng để "chờ giá phản ứng".
- **Order Block** cho **vùng entry** để đặt limit, nhưng điểm trigger kém chính xác hơn.
- **Đỉnh cao của confluence:** khi **CISD level nằm ngay trong Order Block** — bạn có cả điểm trigger sớm (CISD) lẫn vùng entry đẹp (OB) trùng nhau. Đây là kịch bản xác suất cao nhất.

---

## 7. CISD là fractal — chọn khung & CISD lồng nhau

![[CISD-Advanced-Timeframe.svg|697]]

CISD hoạt động ở **mọi khung** theo nguyên lý fractal. Quy tắc top-down ([[32 - Top-down Analysis (Multiple Timeframes)]]):

- **H4/H1 — Bias:** CISD trên HTF xác nhận **draw on liquidity đã đổi hướng**. Dùng để **chọn phe**, không phải để entry (entry sẽ quá muộn/stop rộng).
- **M15/M5 — Context:** chờ CISD tại POI HTF trong killzone → xác nhận thao túng kết thúc. Đây là **điểm cân bằng tốt nhất** giữa độ tin cậy và giá entry.
- **M1 — Entry:** CISD M1 cho **entry sớm nhất, stop nhỏ nhất**, nhưng **chỉ hợp lệ khi HTF + M5 đã đồng thuận**. CISD M1 đơn lẻ giữa nhiễu = bẫy.

### CISD lồng nhau (nested) & CISD thất bại (failed)

![[CISD-Advanced-Nested.svg|697]]

**Nested CISD:** một CISD trên HTF (vd M15) thường được cấu thành bởi **nhiều CISD nhỏ trên LTF** (M1/M5) khi ta phóng to. Ứng dụng thực chiến quan trọng:
- Dùng **CISD LTF** để **vào lệnh sớm với stop nhỏ**, rồi **gia tăng (scale-in)** khi **CISD HTF** đóng xác nhận.
- Chuỗi nested cho phép **dời stop nhanh**: mỗi CISD LTF mới thuận hướng là một cột mốc để trail.

**Failed CISD (bẫy):** CISD bị **vô hiệu** khi một nến sau đó **đóng body trở lại phía sai** của CISD level. Nguyên nhân điển hình: CISD in ra **thiếu sweep**, **ngược bias**, hoặc **giữa range**. Đây là tín hiệu **cắt lệnh dứt khoát** — đừng "hy vọng" nó hồi lại. Một CISD thất bại thường tự nó trở thành **inducement** cho phe ngược lại (xem [[15 - Inducement]]).

> [!warning] Quy tắc invalidation
> Bullish CISD bị huỷ khi giá **đóng cửa body trở lại DƯỚI** CISD level (và/hoặc dưới wick sweep). Đặt mức này làm **stop logic**, không phải một con số cảm tính.

---

## 8. CISD trong Power of Three (AMD)

![[CISD-Advanced-PO3.svg|697]]

Ghép CISD vào khung **Power of Three / AMD** ([[02 - AMD]]) là cách mạnh nhất để biết mình đang ở đâu trong "câu chuyện" trong ngày:

- **Accumulation:** giá tích luỹ quanh giá mở cửa (open) — chưa trade.
- **Manipulation:** thuật toán **đẩy giá ngược hướng thật** để sweep thanh khoản (vd quét SSL trong ngày bullish). Đây là "chân giao hàng" mà ta sẽ đo CISD.
- **CISD = ranh giới M → D:** khi nến đóng qua **open của chân manipulation**, thao túng kết thúc và **Distribution** (chân đi thật, hướng bias) bắt đầu.
- **Distribution:** giá giao về **draw on liquidity** (BSL/SSL đối diện) — đây là đoạn ta kiếm lợi nhuận.

**Vì sao hữu ích:** rất nhiều lệnh thua là do vào **trong pha Manipulation** (tưởng là đảo chiều). CISD cho ta một **mốc khách quan** để nói "manipulation đã xong" trước khi cam kết vốn. Câu hỏi vàng: *"Nến này đóng qua open của chân thao túng chưa?"* — chưa thì chưa vào.

---

## 9. CISD theo giá mở cửa (Opening-price reclaim)

![[CISD-Advanced-Reclaim.svg|697]]

Một biến thể cao cấp: dùng **giá mở cửa tham chiếu** (Midnight Open 00:00 ET, hoặc [[23 - New Day Opening Gap|NDOG]] / [[24 - New Week Opening Gap|NWOG]]) làm **mốc delivery gốc** thay cho open của một chuỗi nến LTF.

- Thuật toán coi **open trong ngày là "giá trị công bằng"**: dưới open = **discount** (rẻ), trên open = **premium** (đắt).
- Kịch bản bullish: giá bị đẩy **xuống dưới open** để sweep SSL (manipulation, gom hàng giá rẻ) → sau đó một nến **đóng cửa trở lại TRÊN open** = **opening-price reclaim**. Đây là một dạng CISD ở "độ phân giải trong ngày" và thường **xác nhận bias bullish của ngày**.
- Confluence mạnh nhất: reclaim open **trùng** NDOG/NWOG, hoặc trùng CE của một FVG HTF.

> [!tip] Dùng open làm bộ lọc bias
> Trong ngày, hãy hỏi: *giá đang ở trên hay dưới open?* Trên open + CISD bullish = đồng thuận. Dưới open mà cố long chỉ vì CISD LTF = đánh ngược "state" trong ngày → xác suất thấp.

---

## 10. Chiếu Standard Deviation từ chân CISD để tìm target

![[CISD-Advanced-StdDev.svg|697]]

CISD không chỉ cho **điểm vào**; chân giao hàng của nó cho ta một **thước đo khách quan để chiếu mục tiêu** ([[31 - Standard Deviation]]):

1. **Đo 1 SD** = khoảng cách từ **điểm sweep (cực trị)** tới **CISD level** — chính là biên độ của chân thao túng.
2. **Chiếu bội số** theo hướng delivery mới: **-2 SD, -2.5 SD, -4 SD** (dấu âm chỉ hướng mở rộng ngược lại chân thao túng).
3. **Gán target:** thường **-2 SD ≈ T1 / IRL gần nhất**, **-2.5 SD ≈ T2**, **-4 SD** cho ngày xu hướng mạnh.

**Best practice:** đừng chốt tại một SD "trần trụi". Ưu tiên SD **trùng với IRL/ERL** ([[16 - Internal & External Range Liquidity (IRL & ERL)]]) hoặc **POI HTF** — confluence giữa SD và một pool thanh khoản thật cho target đáng tin hơn nhiều so với một con số hình học đơn thuần.

---

## 11. Quy trình vào lệnh bằng CISD (nâng cao)

![[CISD-Advanced-Entry-Sequence.svg|697]]

**Bước 1 — Xác nhận Daily Bias & vùng draw.** Biết giá đang muốn đi về đâu (BSL hay SSL) và đang ở Premium hay Discount. CISD chỉ tradeable khi in **thuận** hướng này.

**Bước 2 — Chờ sweep tại cực trị + đánh dấu CISD level.** Giá phải lấy thanh khoản (quét SSL/BSL, equal highs/lows) rồi mới tính CISD. Ngay khi có sweep, vẽ đường CISD tại open của chuỗi đẩy cuối.

**Bước 3 — Chờ nến đóng qua CISD level (displacement).** Một nến đối hướng đóng body qua level, tốt nhất là **displacement** để lại FVG. Đây là xác nhận delivery đã lật.

**Bước 4 — Entry ở retrace, không đuổi.** Đặt limit tại **FVG (50% CE)** hoặc **OB** trùng CISD level. **Stop dưới wick nến sweep** (bullish) / trên wick sweep (bearish). T1 = IRL gần nhất, T2 = ERL / draw on liquidity. Dời BE sau T1.

### Scaling nâng cao (khi đã thành thạo)
- **Vào một phần ở CISD LTF** (M1) với stop nhỏ dưới wick sweep → **gia tăng khi CISD/MSS HTF** (M5/M15) xác nhận. Rủi ro trung bình mỗi lệnh vẫn ≤ 0.5% ([[43 - Position Sizing]]).
- **Nếu bỏ lỡ retrace đầu:** chờ **CISD nội bộ tiếp theo** trên đường đi (nested) thay vì đuổi giá.
- **Quản lý theo SD:** chốt một phần ở -2 SD, để phần còn lại chạy về ERL với stop đã BE.

---

## 12. Ví dụ chart

### Ví dụ đúng 1 — NQ, NY AM (long)
![[CISD-Example-Correct.svg|697]]

**Mô tả:** NQ, ngày bias **bullish** (HTF discount), killzone NY AM. Giá sweep đáy phiên Á (SSL) → một nến xanh **đóng qua CISD level** (open chuỗi đỏ) tạo displacement + FVG → giá hồi về FVG cho entry → delivery mua đẩy về BSL.

**Vì sao đây là ví dụ tốt:**
- CISD in **thuận Daily Bias**.
- CISD xuất hiện **ngay sau sweep** — có lý do rõ ràng để đảo chiều.
- Entry ở **retrace về FVG**, không đuổi nến displacement → stop hợp lý, RR đẹp.

### Ví dụ đúng 2 — EURUSD, London (short)
![[CISD-Example-EURUSD-London.svg|697]]

**Mô tả:** EURUSD, bias D1 **bearish** (premium). London Open quét **đỉnh phiên Á (BSL / equal highs)** → một nến đỏ **đóng dưới CISD level** (open của chuỗi tăng cuối) tạo displacement giảm + FVG → giá retrace vào FVG cho entry short → giao về SSL.

**Vì sao đây là ví dụ tốt:**
- Đối xứng hoàn toàn với ví dụ long — chứng minh CISD **fractal & đối xứng hai chiều**.
- Sweep BSL **thuận bias bearish**; entry ở retrace FVG (50% CE); stop trên wick sweep.
- Target là **SSL** — một draw on liquidity thật, không phải mục tiêu tuỳ ý.

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

## 13. Thực hành tốt nhất (Best Practices)

> [!tip] 8 quy tắc CISD
> 1. **Luôn chờ sweep trước** — CISD không sweep = pullback giả.
> 2. **Đo đúng chuỗi** — CISD level là open nến ĐẦU của chuỗi giao hàng cuối, không phải nến bất kỳ.
> 3. **Chỉ tính khi thân nến đóng qua level** — wick xuyên không được tính.
> 4. **Ưu tiên CISD trùng POI HTF** (OB/FVG/OTE) → entry chính xác + xác nhận cấu trúc.
> 5. **Dùng CISD làm trigger, MSS làm xác nhận** — có thể vào một phần ở CISD, gia tăng ở MSS.
> 6. **Không bao giờ CISD ngược Daily Bias** nếu không có narrative HTF rất mạnh.
> 7. **Đặt invalidation rõ ràng** — CISD huỷ khi giá đóng body trở lại phía sai của level. Đó là stop, không phải "cảm giác".
> 8. **Chiếu SD từ chân CISD** để có target khách quan, ưu tiên SD trùng IRL/ERL.

- Đặt **alert** tại CISD level ngay khi thấy sweep → không phải dán mắt vào chart chờ nến đóng.
- Trên LTF, ưu tiên CISD tạo bởi **displacement mạnh** (nến thân dài, đóng gần đỉnh/đáy) — displacement yếu = delivery yếu.
- Ghép CISD với **macro window** ([[40 - Macro Times]]): CISD in trong 09:50–10:10 ET (NQ) có xác suất cao hơn hẳn CISD ngoài macro.
- Dùng **open trong ngày làm bộ lọc bias** (mục 9): đừng long khi giá còn dưới open, đừng short khi còn trên open, trừ khi HTF ép buộc.
- Ghi nhật ký: mỗi lệnh nên đánh dấu **CISD in ở khung nào**, **có trùng POI/SMT không**, **có nằm sau sweep + trong AMD-distribution không** để đo edge từng loại setup theo thời gian.
- Với người mới: hãy **chờ MSS xác nhận** thay vì vào ngay CISD, cho đến khi backtest chứng minh bạn đọc CISD đủ tốt.

---

## 14. Checklist trước khi trade một CISD

> [!warning] Không trade chỉ vì "thấy một nến đóng qua open chuỗi đẩy"
> CISD chỉ có giá trị khi đứng trong đúng context: sweep + POI + bias + killzone.

- [ ] Daily Bias rõ ràng (D1/H4) và CISD thuận bias
- [ ] Giá đã **sweep** một cực trị thanh khoản rõ ràng
- [ ] Xác định đúng chuỗi giao hàng cuối → CISD level chính xác
- [ ] Thân nến đóng qua CISD level (không phải wick)
- [ ] CISD nằm tại/gần POI HTF (OB/FVG/OTE)
- [ ] Có displacement tạo FVG cho vùng entry
- [ ] Đang trong killzone / macro window
- [ ] Vị trí trong AMD hợp lý (manipulation đã kết thúc, đang vào distribution)
- [ ] (Ưu tiên) có SMT divergence xác nhận
- [ ] Entry ở retrace (FVG 50% CE / OB), không đuổi nến
- [ ] Stop có logic (dưới/trên wick sweep, = mức invalidation); T1 = IRL, T2 = ERL
- [ ] Target chiếu bằng SD trùng pool thanh khoản
- [ ] RR tối thiểu đạt kế hoạch
- [ ] Không revenge / FOMO

---

## 15. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| CISD giữa range | Vào lệnh khi giá chưa lấy thanh khoản | Chỉ tính CISD ở cực trị SAU sweep |
| Đo sai chuỗi đẩy | Kẻ CISD level tại open nến bất kỳ | Dùng open nến ĐẦU của chuỗi cùng màu liên tiếp |
| Tính wick là đóng cửa | Wick xuyên level đã coi là CISD | Chỉ tính khi **thân nến (close)** vượt level |
| CISD ngược bias | LTF đẹp nhưng ngược hướng ngày | Bias filter bắt buộc; ngược bias = bỏ qua |
| Đuổi nến displacement | Market order ngay khi CISD in | Chờ hồi về FVG/OB, đặt limit |
| Nhầm CISD với MSS | Chờ phá swing rồi mới gọi là CISD | CISD = open chuỗi đẩy; MSS = swing |
| Không cắt CISD thất bại | Giá đóng lại phía sai của level nhưng vẫn giữ lệnh | Đóng body ngược level = invalidation → cắt ngay |
| Vào trong pha Manipulation | Tưởng sweep là đảo chiều, chưa có CISD | Chờ đóng qua open chân thao túng (M→D) |

---

## 16. Câu hỏi tự kiểm tra

- Tôi giải thích được CISD trong 30 giây và phân biệt với MSS không?
- CISD level được đo từ đâu — open của nến nào, và **vì sao là open chứ không phải low/close**?
- Vì sao CISD luôn có cơ hội in trước MSS?
- Điều gì biến một CISD thành tín hiệu giả? Điều gì **vô hiệu hoá** một CISD đã in?
- CISD nằm ở đâu trong mô hình AMD, và vì sao nó là mốc an toàn để chuyển sang distribution?
- Tôi chiếu SD target từ chân CISD như thế nào?
- Lệnh nào trong journal của tôi vào bằng CISD — kết quả và edge so với vào bằng MSS ra sao?

---

## 17. Flashcards / Active Recall

### Q1
**Hỏi:** CISD được đo bằng gì và in ra khi nào?
**Đáp:** Đo bằng giá OPEN của nến đầu tiên trong chuỗi giao hàng cuối; in ra khi một nến đối hướng ĐÓNG CỬA body vượt qua mức đó.

### Q2
**Hỏi:** Điều kiện quan trọng nhất để CISD hợp lệ là gì?
**Đáp:** Phải có **sweep thanh khoản tại cực trị trước đó**, thuận Daily Bias, và tốt nhất là trùng POI HTF trong killzone.

### Q3
**Hỏi:** Khác biệt cốt lõi giữa CISD và MSS?
**Đáp:** CISD phá **open chuỗi nến đẩy** (in sớm, nhạy); MSS phá **swing high/low** (in muộn hơn, chắc hơn).

### Q4
**Hỏi:** Vì sao đo delivery bằng OPEN chứ không phải low hay close?
**Đáp:** Open nến đầu = nơi chương trình giao hàng bắt đầu (ý định thuật toán). Đóng qua open = lấy lại toàn bộ order flow của leg; low chỉ là nơi sweep, không phải nơi ý định khởi động.

### Q5
**Hỏi:** CISD nằm ở đâu trong Power of Three?
**Đáp:** Là ranh giới **Manipulation → Distribution** — mốc xác nhận thao túng đã kết thúc, an toàn hơn để trade cùng chiều distribution.

### Q6
**Hỏi:** Khi nào một CISD đã in bị vô hiệu?
**Đáp:** Khi một nến sau đó đóng body trở lại **phía sai** của CISD level (thường do thiếu sweep/ngược bias) — đây là mức invalidation/stop.

---
> [!note]
> Nếu path không khớp, đổi `FROM` cho đúng cấu trúc vault. Muốn đo **edge của CISD**, so sánh win rate & expectancy của các lệnh entry_model chứa "CISD" với các lệnh entry bằng "MSS".

---

## 19. Lesson Learned

### Bài học chính
- CISD là **trigger sớm**, không phải lý do đảo chiều — lý do luôn là **sweep + POI + bias**.
- Đo bằng **open**, không phải wick/low; **close** phải vượt level.
- CISD ngược bias hoặc giữa range là **cái bẫy phổ biến nhất** — bỏ qua theo mặc định.

### Quy tắc cá nhân rút ra
- [ ] Chỉ vẽ CISD **sau khi** thấy một cú sweep cực trị rõ ràng.
- [ ] Luôn ghi trong journal: CISD in ở khung nào + trùng POI/SMT/AMD không.
- [ ] Cắt ngay khi CISD thất bại (đóng ngược level) — không "hy vọng".

### Câu nhắc nhở khi trade
> "CISD chỉ xác nhận điều mà sweep + POI + bias đã kể. Không có câu chuyện đó, một nến đóng qua open chỉ là nhiễu."
