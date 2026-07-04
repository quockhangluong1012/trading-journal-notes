---
type: ict-concept
concept: Advance Market Structure
aliases:
  - Advance Market Structure
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
  - "#MarketStructure"
status: developing
category: Market Structure
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
importance: 5
last_reviewed: 2026-06-23
created: 2026-06-23
updated: 2026-07-02
common_mistakes:
  - "[[Mistake - Mislabel Market Structure]]"
  - "[[Mistake - BOS On Minor Swing]]"
  - "[[Mistake - Trade Against HTF Structure]]"
---

# Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )

> [!summary] Tóm tắt 1 câu
> **Advance Market Structure là cách ICT xác định swing point THẬT theo phân cấp fractal — Short Term (STL/STH) là đơn vị nhỏ nhất, Intermediate Term (ITL/ITH) gom các Short Term, và Long Term (LTL/LTH) gom các Intermediate Term — để mình đo BOS/MSS đúng "degree", lọc nhiễu và biết đỉnh/đáy nào đang được bảo vệ (protected).**

> [!important] Nguyên tắc cốt lõi
> **Mỗi degree cấu trúc được định nghĩa bằng phần tử của degree nhỏ hơn ở HAI BÊN: STL = nến low có higher-low hai bên; ITL = một STL có STL cao hơn ở hai bên; LTL = một ITL có ITL cao hơn ở hai bên (đảo ngược cho high). BOS/MSS chỉ có ý nghĩa khi đo ĐÚNG degree — phá một STH lẻ KHÔNG phải BOS của xu hướng, nó chỉ là nhiễu nội bộ.**
> Mislabel cấu trúc là gốc rễ của hầu hết lỗi: vào ngược trend, dời stop sai, gọi pullback là đảo chiều.

---

## 1. Định nghĩa

**Khái niệm:**  
Advance Market Structure (cấu trúc thị trường nâng cao) là hệ thống phân cấp **fractal** để xác định swing point thật trong ICT. Thay vì gọi bất kỳ đỉnh/đáy nhỏ nào là "swing", ICT chia cấu trúc thành ba cấp độ (degree), mỗi cấp được định nghĩa đệ quy từ cấp nhỏ hơn:

- **Short Term Low (STL):** một nến có **low**, mà nến **ngay trước và ngay sau đều có low CAO HƠN** (higher low ở cả hai phía). Đây là đáy fractal nhỏ nhất.
- **Short Term High (STH):** một nến có **high**, mà nến trước và sau đều có high THẤP HƠN (lower high hai phía). Đỉnh fractal nhỏ nhất.
- **Intermediate Term Low (ITL):** một **STL có một STL cao hơn ở mỗi bên** (STL bên trái cao hơn và STL bên phải cao hơn). Nói cách khác, ITL là STL "thấp nhất cục bộ" giữa hai STL cao hơn.
- **Intermediate Term High (ITH):** một **STH có một STH thấp hơn ở mỗi bên**.
- **Long Term Low (LTL):** một **ITL có một ITL cao hơn ở mỗi bên**. Đây là swing point cấp cao nhất — đáy của một range lớn.
- **Long Term High (LTH):** một **ITH có một ITH thấp hơn ở mỗi bên**.

![[AMS-Advanced-Fractal-Hierarchy.svg|697]]

**Tính lồng nhau (nesting):** một LTL luôn **đồng thời** là một ITL và một STL — degree cao không thay thế degree thấp mà *bao trùm* nó. Khi nhìn một đáy quan trọng, hãy tự hỏi: "đáy này đang đội bao nhiêu lớp mũ?" Đáy càng nhiều lớp (STL + ITL + LTL cùng lúc), stop loss dồn phía dưới càng nhiều và ý nghĩa cấu trúc càng lớn.

**Cấu trúc là "bộ nhớ" của thị trường:** mỗi swing point là dấu vết một lần order flow đổi phía tại đó. STL ghi lại cuộc giằng co vài nến; ITL ghi lại cuộc giằng co của cả một nhịp; LTL ghi lại điểm mà cả một chiến dịch mua/bán lớn được khởi động. Vì vậy khi giá quay lại gần một swing degree cao, thị trường "nhớ" — phản ứng thường mạnh và nhiều thanh khoản hơn hẳn khi chạm một STL vô danh.

**Bản chất (fractal):** cấu trúc lặp lại ở mọi degree. Một STL trên M5 có thể là một ITL khi nhìn rộng hơn, và một LTL trên M15 có thể chỉ là một STL trên H4. **Degree luôn mang tính tương đối với khung quan sát.** Điều quan trọng không phải con số tuyệt đối mà là **thứ bậc**: cái nào gom cái nào.

**Mục đích trong ICT:**  
- Xác định **swing point thật** để vẽ [[12 - Dealing Range]] và xác định Premium/Discount chính xác.
- Đo **BOS/MSS đúng degree**: phá ITH mới là BOS của xu hướng trung hạn; phá STH chỉ là chuyển động nội bộ.
- Xác định **Protected High / Protected Low** — đỉnh/đáy mà nếu bị phá thì cấu trúc đổi.
- **Lọc nhiễu**: bỏ qua các dao động nhỏ không đủ tư cách swing, tránh overtrade.
- Định vị **liquidity**: dưới mỗi STL/ITL/LTL là sell-side liquidity; trên mỗi STH/ITH/LTH là buy-side liquidity, với "trọng lượng" tăng dần theo degree.

**Vì sao khái niệm này quan trọng:**  
Mọi khái niệm ICT khác (bias, dealing range, premium/discount, OTE, liquidity target) đều **dựa trên việc bạn đọc cấu trúc đúng**. Nếu bạn gắn nhãn swing sai, toàn bộ phân tích phía sau lệch. Đây là **nền móng** — quan trọng ngang [[19 - Liquidity]].

**Nó giúp trả lời câu hỏi nào trên chart?**
- Đỉnh/đáy nào là swing point THẬT, đỉnh/đáy nào chỉ là nhiễu?
- Giá vừa phá cấu trúc ở degree nào — nội bộ (STH) hay xu hướng (ITH/LTH)?
- Đáy/đỉnh nào đang được "bảo vệ" (protected) — nếu bị phá thì bias đổi?
- Pullback hiện tại còn nằm trong cấu trúc tăng hay đã thực sự đảo?
- Liquidity quan trọng (degree cao) đang nằm ở đâu?

### Advance Market Structure không phải là gì
- Không phải "cứ thấy một đỉnh nhô lên là swing high".
- Không phải đường zigzag tự động — nó là phân cấp logic dựa trên higher-low/lower-high hai bên.
- Không phải bias độc lập — nó cung cấp khung để đọc bias, không tự nó là tín hiệu.
- Không phải bất biến theo timeframe — degree luôn tương đối với khung bạn đang xem.
- Không phải lý do bỏ qua liquidity: một BOS "đẹp" thường chỉ là sweep nếu chưa lấy thanh khoản đối diện.

---

## 2. Bối cảnh sử dụng

### Ba degree và ý nghĩa thực chiến

| Degree | Định nghĩa (cho Low) | Định nghĩa (cho High) | Vai trò thực chiến |
|---|---|---|---|
| **Short Term (STL/STH)** | Nến low có higher-low hai bên | Nến high có lower-high hai bên | Swing nhỏ nhất; cấu trúc nội bộ (internal); execution LTF |
| **Intermediate Term (ITL/ITH)** | STL có STL cao hơn hai bên | STH có STH thấp hơn hai bên | Swing trung hạn; định nghĩa dealing range thực; BOS/MSS có ý nghĩa |
| **Long Term (LTL/LTH)** | ITL có ITL cao hơn hai bên | ITH có ITH thấp hơn hai bên | Swing cấp cao; protected high/low; cấu trúc & bias chính |

![[AMS-Advanced-Degree-Liquidity-Weight.svg|697]]

### Nâng cao — Trọng lượng liquidity theo degree

Mỗi swing point là một **kho stop loss**, nhưng kho không bằng nhau:

- **Dưới STL:** chỉ có stop của trader LTF vào lệnh vài nến gần đây → pool mỏng. Sweep tại đây thường chỉ là **inducement** cho một nhịp nhỏ.
- **Dưới ITL:** cộng dồn stop của tất cả những ai mua trong cả nhịp đó → pool trung bình. Sweep ITL đủ nhiên liệu cho một leg M15–H1.
- **Dưới LTL:** stop của các vị thế swing/position + pending sell-stop breakout → pool "nặng" nhất. Sweep LTL thường mở ra **đảo chiều HTF hoặc leg nhiều ngày**.

Hệ quả thực chiến: **target và sweep phải "cân degree"**. Một setup M5 nhắm tới BSL trên một STH thì R:R nhỏ và hợp lý; nhưng kỳ vọng đảo chiều H4 chỉ vì giá sweep một STL trên M5 là lệch degree — nhiên liệu không đủ cho kỳ vọng đó. Ngược lại, khi giá vừa sweep một LTL của khung H4 mà bạn chỉ dám nhắm 10 pip, bạn đang bỏ phí phần lớn move.

### Nâng cao — Neo degree vào timeframe (khung phán quyết)

Vì degree tương đối, mỗi trader phải tự **khóa một quy ước** và giữ nó nhất quán. Quy ước gợi ý cho hệ ICT 2022 intraday (NQ/FX):

| Vai trò | Timeframe | Degree dùng ở khung này |
|---|---|---|
| Khung phán quyết bias | D1 / H4 | Chuỗi ITH/ITL của D1-H4 quyết định trend; LTL/LTH = invalidation của cả narrative |
| Khung làm việc (dealing range) | H1 / M15 | ITL/ITH của H1-M15 vẽ dealing range thực; BOS/MSS "có ý nghĩa" đo ở đây |
| Khung execution | M5 / M1 | STL/STH để timing entry, đặt stop, đọc inducement |

Nguyên tắc: **nhãn degree chỉ có nghĩa bên trong khung đã chọn**. Khi chuyển khung, phải "dịch" lại nhãn (xem sơ đồ ở mục 4), không mang nhãn M1 lên áp cho H4.

> [!tip]
> Một mẹo đọc nhanh: bắt đầu từ **STL/STH** (chấm tất cả các đáy/đỉnh có higher-low/lower-high hai bên), rồi "nâng cấp": STL nào có STL cao hơn hai bên → ITL; ITL nào có ITL cao hơn hai bên → LTL. Bạn đang xây một cây phân cấp từ dưới lên. Cùng logic cho high.

### Khi nào khái niệm này có giá trị cao?
- [ ] Cần xác định **Dealing Range** thật để đo Premium/Discount.
- [ ] Cần phân biệt **BOS xu hướng** (phá ITH/LTH) với **chuyển động nội bộ** (phá STH).
- [ ] Cần biết **Protected Low/High** để xác định invalidation của bias.
- [ ] Đang đa khung: dùng degree HTF làm khung tham chiếu, degree LTF làm execution.
- [ ] Thị trường trending rõ — phân cấp fractal đọc rất sạch.
- [ ] Trước khi đặt target liquidity: degree càng cao, liquidity càng "nặng".

### Khi nào nên bỏ qua / cẩn trọng?
- [ ] Thị trường đi ngang choppy, swing chồng chéo — degree mờ, dễ mislabel.
- [ ] Tin tức mạnh tạo nến dị thường phá vỡ logic fractal tạm thời.
- [ ] Khung quá nhỏ (M1) trong giờ thanh khoản thấp — nhiễu nhiều hơn cấu trúc.
- [ ] Chỉ nhìn một timeframe và cố ép degree — luôn đối chiếu HTF.

---

## 3. Cấu trúc nhận diện trên chart

![[AMS-Advanced-Mapping-Workflow.svg|697]]

### Dấu hiệu chính
1. **STL/STH (cấp 1):** một nến low (high) với nến hai bên đều có low cao hơn (high thấp hơn). Đây là viên gạch nền.
2. **ITL/ITH (cấp 2):** một STL (STH) nằm THẤP NHẤT (CAO NHẤT) cục bộ giữa hai STL cao hơn (hai STH thấp hơn).
3. **LTL/LTH (cấp 3):** một ITL (ITH) nằm thấp nhất (cao nhất) giữa hai ITL cao hơn (hai ITH thấp hơn).
4. **Chuỗi higher-high + higher-low theo degree:** uptrend thật = ITH và ITL đều dâng lên; downtrend = ITH và ITL đều hạ xuống.
5. **Protected high/low:** trong uptrend, ITL/LTL gần nhất tạo ra trước BOS là đáy được bảo vệ; thủng nó = cảnh báo đổi cấu trúc.

### Ma trận nhận diện theo degree

| Thành phần | Đáy (Low side) | Đỉnh (High side) | Cảnh báo / dễ nhầm |
|---|---|---|---|
| **Short Term** | Low có higher-low 2 bên | High có lower-high 2 bên | Bóng nến nhiễu; đếm sai nến hai bên |
| **Intermediate** | STL có STL cao hơn 2 bên | STH có STH thấp hơn 2 bên | Nhầm một STL lẻ thành ITL |
| **Long Term** | ITL có ITL cao hơn 2 bên | ITH có ITH thấp hơn 2 bên | Bỏ sót một ITL → vẽ LTL sai |
| **Trend** | Chuỗi ITL dâng = uptrend | Chuỗi ITH hạ = downtrend | Pullback bị gọi nhầm là đảo |
| **BOS/MSS** | Phá ITL = BOS Bearish hợp lệ | Phá ITH = BOS Bullish hợp lệ | Phá STH/STL lẻ ≠ BOS xu hướng |
| **Protected** | ITL/LTL trước BOS = protected low | ITH/LTH trước BOS = protected high | Thủng protected = đổi cấu trúc |

### Điều kiện bắt buộc
- [ ] Đếm đúng nến hai bên để xác lập STL/STH (higher-low / lower-high thật).
- [ ] Nâng cấp degree theo đúng định nghĩa đệ quy (STL→ITL→LTL).
- [ ] Xác định được Protected High và Protected Low hiện tại.
- [ ] Biết mình đang đo BOS/MSS ở degree nào.

### Điều kiện tăng độ tin cậy
- [ ] Degree HTF (D1/H4) và degree LTF (M15/M5) đồng thuận hướng.
- [ ] BOS xu hướng (phá ITH/LTH) đi kèm displacement và FVG.
- [ ] BOS xảy ra SAU một liquidity sweep degree thấp hơn (sweep STL → BOS bullish).
- [ ] Cấu trúc đọc sạch, swing không chồng chéo.
- [ ] Protected level trùng một POI HTF (OB/FVG).

### Điều kiện làm việc đọc cấu trúc yếu đi
- Thị trường choppy, nhiều swing kích thước gần bằng nhau.
- Cố ép một degree duy nhất mà không đối chiếu HTF.
- Bỏ qua bóng nến / dùng đóng cửa tùy tiện khi xác định swing.
- Đánh dấu BOS dựa vào cảm giác thay vì định nghĩa fractal.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc khi đọc cấu trúc
> 1. **Ở degree nào tôi đang đọc — Short, Intermediate hay Long Term?**
> 2. **Swing này có đủ điều kiện higher-low/lower-high hai bên để là swing THẬT không?**
> 3. **Cái vừa bị phá là STH/STL lẻ (nội bộ) hay ITH/ITL/LTH/LTL (xu hướng)?**
> 4. **Protected High/Low hiện tại ở đâu, và thủng nó nghĩa là gì?**

![[AMS-Advanced-MTF-Mapping.svg|697]]

### D1 / H4 — Bias & Degree chính
- **Bias hiện tại:** đọc theo chuỗi ITH/ITL (hoặc LTH/LTL) — dâng lên = bullish, hạ xuống = bearish.
- **Long Term structure:** xác định LTL/LTH gần nhất; đây là khung của bias chính.
- **Protected level HTF:** ITL/LTL (bullish) hoặc ITH/LTH (bearish) cần được giữ.
- **Dealing range:** từ swing degree cao → đo Premium/Discount.

### H1 / M15 — Intermediate context
- **Intermediate degree:** chấm ITL/ITH; xác định cấu trúc trung hạn có đồng thuận HTF không.
- **BOS/MSS có ý nghĩa:** chỉ tính khi phá ITH/ITL, không phải STH/STL lẻ.
- **Liquidity:** dưới mỗi ITL = SSL; trên mỗi ITH = BSL — đây là các pool đáng chú ý.

### M5 / M1 — Short term & Entry
- **Short term degree:** chấm STL/STH để tìm điểm execution.
- **MSS nội bộ:** sau khi giá vào POI HTF, một MSS Short Term (phá STH/STL) dùng để xác nhận entry — nhưng phải ĐỒNG HƯỚNG degree HTF.
- **Entry refinement:** STL/STH gần nhất giúp đặt stop logic (ngoài swing thật, không tùy ý).

```text
Mẫu ghi nhanh — đọc cấu trúc trước khi vào lệnh
HTF (D1/H4): chuỗi ITL dâng → Bullish | LTL bảo vệ tại [level]
H1/M15: ITL gần nhất tại [level] (protected low) — chưa thủng
Liquidity: SSL dưới ITL [level]; BSL trên ITH [level] (target)
Sự kiện: giá sweep STL nội bộ → M5 MSS bullish (phá STH) ĐỒNG HƯỚNG HTF
Entry: theo POI sau MSS Short Term; Stop dưới STL thật vừa tạo
Invalid: đóng nến thủng protected ITL/LTL → bias bullish hỏng
```

> [!warning]
> **Một MSS trên M1/M5 không nâng cấp thành đổi xu hướng HTF.** Phá một STH chỉ là chuyển động Short Term. Đừng để một "BOS" degree thấp khiến bạn trade ngược ITH/LTH degree cao đang còn nguyên.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Một swing point được xem là HỢP LỆ khi
- [ ] STL/STH: có higher-low / lower-high ở cả hai nến kề.
- [ ] ITL/ITH: là STL/STH cực trị giữa hai STL/STH cùng loại cao hơn / thấp hơn.
- [ ] LTL/LTH: là ITL/ITH cực trị giữa hai ITL/ITH cùng loại cao hơn / thấp hơn.
- [ ] Degree được xác định nhất quán, không nhảy degree giữa chừng.

### Một "BOS/MSS" bị xem là KHÔNG hợp lệ (chỉ là nhiễu) khi
- [ ] Cái bị phá chỉ là STH/STL lẻ trong khi đang xét xu hướng HTF.
- [ ] "Break" thực ra là một liquidity sweep (wick xuyên rồi đóng nến quay lại).
- [ ] Không có displacement — chỉ trôi qua mức cũ một chút.
- [ ] Break ngược degree HTF mà không có chuỗi xác nhận (sweep → displacement → BOS đúng degree).

![[AMS-Advanced-Protected-Levels.svg|697]]

### Đổi cấu trúc (Change of Character) được xác nhận khi
- [ ] Trong uptrend, giá **đóng nến thủng Protected Low (ITL/LTL)** đang giữ → cấu trúc bullish bị tổn thương.
- [ ] Sau đó hình thành lower ITH + lower ITL → xác nhận downtrend mới.
- [ ] (Đảo ngược cho downtrend → uptrend.)

### So sánh: Sweep vs BOS thật

![[AMS-Advanced-Sweep-vs-BOS.svg|697]]

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Wick xuyên qua swing rồi ĐÓNG NẾN quay lại trong range | **Liquidity Sweep** | Lấy thanh khoản; thường đảo hướng — KHÔNG phải BOS |
| Thân nến ĐÓNG CỬA vượt hẳn swing + displacement | **BOS thật (đúng degree)** | Cấu trúc tiếp diễn theo hướng phá |
| Phá STH lẻ trong pullback của uptrend | **Internal move** | Bình thường trong xu hướng; không đổi bias |
| Đóng nến thủng protected ITL/LTL | **Change of Character** | Cảnh báo đảo cấu trúc; chờ xác nhận chuỗi mới |

> [!note]
> **Sweep ≠ BOS.** Đây là phân biệt sống còn. Rất nhiều "BOS" thực chất là sweep: giá chỉ wick xuyên swing để lấy liquidity rồi đảo. BOS thật cần **đóng nến vượt + displacement**, và lý tưởng là sau khi đã sweep liquidity đối diện.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Advance-Market-Structure-Example-Correct.svg|697]]

**Mô tả:**  
Một uptrend đọc đúng phân cấp: các STL nhỏ được gom thành ITL, các ITL được gom dưới một LTL gốc (protected low). Mỗi degree đều thỏa điều kiện higher-low hai bên. BOS được đo khi giá đóng nến vượt ITH degree trung hạn, kèm chuỗi higher-high nối tiếp. Đáy LTL phía dưới là protected low — chừng nào chưa thủng, bias vẫn bullish.

**Vì sao đây là ví dụ tốt:**
- Mỗi swing được nâng cấp degree đúng định nghĩa (STL→ITL→LTL).
- BOS đo ở **đúng degree** (phá ITH), không phải STH lẻ.
- Protected Low (LTL) rõ ràng → biết chính xác khi nào bias hỏng.
- Cấu trúc sạch giúp đặt dealing range và đọc liquidity theo degree.

### Ví dụ sai / dễ nhầm
![[Advance-Market-Structure-Example-Wrong.svg|697]]

**Mô tả lỗi:**  
Trader gắn nhãn "BOS" lên một STH lẻ xuất hiện trong một pullback của xu hướng giảm. Thực tế Protected High (LTH) phía trên chưa hề bị phá, và chuỗi lower-low vẫn tiếp diễn. "BOS" này chỉ là chuyển động nội bộ Short Term, không phải đổi xu hướng. Vào Long theo nó là trade ngược cấu trúc lớn.

**Bài học:**
- Phá một STH lẻ KHÔNG phải BOS của xu hướng — phải đo theo degree (ITH/LTH).
- Luôn xác định Protected High/Low THẬT trước khi tuyên bố đổi cấu trúc.
- Pullback có swing nhỏ là bình thường; đừng nhầm với đảo chiều.
- Đọc sai degree = mọi phân tích phía sau (bias, P/D, target) đều lệch.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[05 - BOS - Break of Structure]] — cú phá tiếp diễn, phải đo đúng degree
- [[21 - Market Structure Shift]] — cú phá đảo chiều, xác nhận trên LTF
- [[09 - Change of Character]] — thủng protected level, cảnh báo đổi cấu trúc
- [[12 - Dealing Range]] — vẽ từ swing degree cao
- [[27 - Premium Discount]] — đo trên dealing range đúng degree
- [[19 - Liquidity]] / [[20 - Liquidity Sweep]] — trọng lượng pool theo degree
- [[15 - Inducement]] — sweep STL nội bộ trước move thật

### Sequence mẫu — Long theo cấu trúc tăng đúng degree
```text
HTF: chuỗi ITL dâng → Bullish; LTL = protected low
→ Giá pullback về Discount của dealing range (đo theo swing degree cao)
→ Sweep SSL dưới một STL nội bộ (inducement) — KHÔNG thủng protected ITL/LTL
→ Displacement tăng phá STH nội bộ → MSS Short Term ĐỒNG HƯỚNG HTF
→ Entry tại POI (FVG/OB) sau MSS
→ Stop dưới STL thật vừa tạo (ngoài sweep)
→ Target: BSL trên ITH/LTH degree cao hơn
```

### Sequence mẫu — Nhận diện Change of Character (đảo cấu trúc)
```text
Uptrend: ITL đang dâng, LTL = protected low
→ Giá ĐÓNG NẾN thủng protected ITL/LTL (không chỉ wick)
→ Change of Character: bias bullish bị tổn thương
→ Chờ hình thành lower ITH + lower ITL để xác nhận downtrend
→ Sau đó mới tìm Short theo cấu trúc giảm mới (không Short sớm)
```

> [!note]
> Trong ICT 2022 model, degree là "bộ lọc" của toàn bộ setup: bạn dùng degree HTF để xác định hướng và protected level, dùng degree LTF (MSS Short Term) để execution. Sai degree = lệch toàn bộ chuỗi.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy "một cái đỉnh/đáy bị phá"
> Cấu trúc chỉ có giá trị khi đọc đúng **degree + context + liquidity**. Một break sai degree là cái bẫy.

### A. Context (HTF)
- [ ] Đã xác định degree chính (D1/H4) và hướng theo chuỗi ITH/ITL.
- [ ] Đã chấm Protected High và Protected Low hiện tại.
- [ ] Biết dealing range thật (theo swing degree cao) và vị trí Premium/Discount.
- [ ] Liquidity theo degree đã được định vị (SSL dưới ITL/LTL, BSL trên ITH/LTH).

### B. Execution (LTF)
- [ ] MSS Short Term ĐỒNG HƯỚNG degree HTF (không ngược).
- [ ] Cái bị phá là swing THẬT, không phải bóng nến nhiễu.
- [ ] Đã có liquidity sweep nội bộ trước khi BOS/MSS (đúng thứ tự).
- [ ] Có displacement + FVG/OB làm POI entry.
- [ ] Stop đặt ngoài swing THẬT (STL/STH), không tùy ý.
- [ ] Protected level chưa bị thủng theo hướng ngược.

### C. Quy tắc "không có lệnh"
- [ ] "BOS" chỉ là phá STH/STL lẻ → không trade theo như đảo xu hướng.
- [ ] Đó thực ra là sweep (wick xuyên rồi đóng quay lại) → không coi là BOS.
- [ ] Setup ngược degree HTF mà chưa có Change of Character xác nhận → không trade.
- [ ] Cấu trúc choppy, degree mờ → đứng ngoài.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Mislabel degree | Gọi STL lẻ là ITL/LTL | Dealing range & P/D sai theo | Nâng cấp degree đúng định nghĩa đệ quy |
| BOS trên swing nhỏ | Đánh BOS lên STH lẻ trong pullback | Trade ngược xu hướng lớn | Chỉ tính BOS khi phá ITH/ITL/LTH/LTL |
| Nhầm sweep với BOS | Coi wick xuyên swing là "phá cấu trúc" | Vào đúng lúc giá sắp đảo | Yêu cầu đóng nến vượt + displacement |
| Bỏ qua protected level | Không biết đáy/đỉnh nào đang giữ bias | Không có invalidation rõ ràng | Luôn chấm Protected High/Low trước |
| Nhầm pullback với đảo | Thấy vài swing ngược là tưởng đổi trend | Đóng lệnh sớm / vào ngược | Chờ Change of Character (đóng nến thủng protected) |
| Ép một timeframe | Chỉ đọc M5, bỏ HTF | Degree LTF mâu thuẫn HTF | Luôn đối chiếu degree HTF trước |
| Đếm sai nến hai bên | Bỏ qua bóng nến / đếm thiếu | STL/STH xác lập sai từ gốc | Kiểm tra rõ low/high hai nến kề |
| MSS LTF ngược HTF | Long theo MSS M1 khi HTF bearish | Counter-trend không có edge | MSS execution phải đồng hướng degree HTF |

---

## 10. Câu hỏi tự kiểm tra

- Mình có giải thích STL → ITL → LTL (và bản high) trong 30 giây không?
- Swing này là degree nào, và nó có thỏa điều kiện higher-low/lower-high hai bên không?
- Cái vừa bị phá là nội bộ (STH/STL) hay xu hướng (ITH/ITL/LTH/LTL)?
- Đây là BOS thật hay chỉ là một liquidity sweep?
- Protected High/Low hiện tại ở đâu? Thủng nó nghĩa là gì?
- Degree LTF của mình có đồng hướng degree HTF không?
- Nếu mình không trade, lý do "No Trade" theo cấu trúc là gì?
- Setup nào trong journal đã mislabel degree dẫn tới lỗi?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Định nghĩa Short Term Low (STL) là gì?  
**Đáp:** Một nến có low mà nến ngay trước và ngay sau đều có low CAO HƠN (higher-low ở cả hai bên). Đảo ngược cho STH (lower-high hai bên).

### Q2
**Hỏi:** ITL và LTL được định nghĩa thế nào theo phân cấp?  
**Đáp:** ITL = một STL có một STL cao hơn ở mỗi bên. LTL = một ITL có một ITL cao hơn ở mỗi bên. Đệ quy từ degree nhỏ lên degree lớn.

### Q3
**Hỏi:** Vì sao phá một STH lẻ KHÔNG phải BOS của xu hướng?  
**Đáp:** Vì STH chỉ là cấu trúc Short Term (nội bộ). BOS xu hướng chỉ có ý nghĩa khi phá ITH/LTH — degree tương ứng với xu hướng đang xét.

### Q4
**Hỏi:** Protected Low/High là gì?  
**Đáp:** Trong uptrend, ITL/LTL gần nhất tạo trước BOS là đáy được bảo vệ; đóng nến thủng nó = Change of Character (cảnh báo đảo). Đảo ngược cho protected high trong downtrend.

### Q5
**Hỏi:** Phân biệt Liquidity Sweep và BOS thật?  
**Đáp:** Sweep = wick xuyên swing rồi đóng nến quay lại range (lấy thanh khoản, thường đảo). BOS thật = đóng nến vượt hẳn swing + displacement (cấu trúc tiếp diễn).

### Q6
**Hỏi:** "Degree mang tính tương đối" nghĩa là gì?  
**Đáp:** Một STL trên M5 có thể là ITL khi nhìn rộng hơn; một LTL trên M15 có thể chỉ là STL trên H4. Thứ bậc (cái gom cái) mới quan trọng, không phải nhãn tuyệt đối.

### Q7
**Hỏi:** Tại sao đọc cấu trúc đúng là nền móng của mọi setup ICT?  
**Đáp:** Vì dealing range, premium/discount, OTE, liquidity target đều dựa trên swing point. Mislabel swing = toàn bộ phân tích phía sau lệch.

---

## 12. Lesson Learned

### Bài học chính
- Cấu trúc là **fractal phân cấp**: STL→ITL→LTL (và bản high), định nghĩa đệ quy bằng higher-low/lower-high hai bên.
- **BOS/MSS phải đo đúng degree** — phá STH lẻ chỉ là nội bộ, không phải đổi xu hướng.
- **Protected High/Low** cho biết chính xác khi nào bias hỏng (Change of Character).
- **Sweep ≠ BOS**: đừng nhầm wick lấy thanh khoản với phá cấu trúc thật.
- Degree LTF execution phải **đồng hướng** degree HTF.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn chấm degree (STL/ITL/LTL) trước khi gọi bất cứ gì là "BOS".
- [ ] Tôi không trade theo break của STH/STL lẻ như thể đó là đảo xu hướng.
- [ ] Tôi luôn xác định Protected High/Low và coi đó là invalidation của bias.
- [ ] Tôi phân biệt sweep (wick + đóng quay lại) với BOS (đóng nến vượt + displacement).
- [ ] MSS execution của tôi phải đồng hướng degree HTF, nếu không thì đứng ngoài.

### Câu nhắc nhở khi trade
> **"Trước khi gọi 'BOS', hỏi: degree nào? Cái này là swing thật hay nhiễu? Protected level còn nguyên không? Đây là phá cấu trúc hay chỉ là sweep?"**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt STL/ITL/LTL và bản high theo định nghĩa đệ quy không? |
| Nhận diện trên chart |  | Có nâng cấp degree đúng và chấm protected level không? |
| Biết khi nào bỏ qua |  | Có dám bỏ "BOS" trên swing nhỏ / khi cấu trúc choppy không? |
| Kết hợp với context HTF |  | Degree LTF có được đặt trong khung degree HTF không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự theo BOS đúng degree + protected level không? |
| Review sau trade |  | Có kiểm tra mislabel degree bằng dữ liệu journal không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập 20–30 setup gắn tag `[[Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]]`.
- [ ] Review riêng: BOS thật vs nhầm sweep; MSS đồng hướng vs ngược HTF; protected level còn nguyên vs đã thủng.
- [ ] Thống kê win rate theo `bos_degree` và `mss_aligned_htf`.
- [ ] Chỉ cập nhật rule khi đủ mẫu backtest/forward test.

---

## 14. Best Practices

> [!success] Nguyên tắc vàng
> **"Chấm degree trước, tìm setup sau."** Mở chart là chấm STL→ITL→LTL và protected level TRƯỚC KHI nghĩ đến bất kỳ lệnh nào. Setup chỉ là hệ quả của cấu trúc đọc đúng.

1. **Khóa một khung phán quyết và không đổi giữa phiên.** Chọn H4 (bias) + M15 (dealing range) + M5/M1 (execution) rồi giữ nguyên quy ước. Phần lớn lỗi mislabel đến từ việc "trượt khung" vô thức khi lệnh đang chạy — chart lúc đó không đổi, chỉ có tâm lý muốn tìm lý do giữ lệnh.

2. **Chấm swing bằng bóng nến, không bằng body.** STL/STH được định nghĩa bằng low/high tuyệt đối (kể cả wick). Chỉ khi đánh giá *cú phá* (BOS/MSS/CHoCH) mới yêu cầu body close. Hai việc này ngược nhau và hay bị lẫn: **xác lập swing = wick; xác nhận phá = body**.

3. **Luôn biết hai con số: Protected Low và Protected High hiện tại.** Trước mỗi phiên, viết ra hai mức này trong Daily Note. Nếu không trả lời được "thủng mức nào thì bias hỏng?" trong 5 giây, nghĩa là chưa đọc xong cấu trúc — chưa được trade.

4. **Cân degree giữa sweep, entry và target.** Sweep STL → kỳ vọng nhịp nhỏ; sweep ITL → leg M15-H1; sweep LTL → khả năng đảo HTF. Đừng bắt một cú sweep STL "gánh" một target external HTF, và đừng thoát non một lệnh bắt nguồn từ sweep LTL.

5. **Khi cấu trúc choppy, quyền cao nhất là đứng ngoài.** Nếu sau 5 phút chấm swing mà các degree chồng chéo không phân định được, thị trường đang trong giai đoạn tái tích lũy — mọi nhãn BOS/MSS lúc này đều là đoán. Ghi "No Trade — structure unclear" là một quyết định trading đúng nghĩa.

6. **Sau mỗi BOS, dời protected level một cách máy móc.** BOS mới → protected low/high mới = ITL/ITH cuối trước cú phá. Làm thủ công từng lần, đừng để mức cũ "dính" trên chart — protected level lỗi thời là nguyên nhân phổ biến của việc giữ lệnh quá lâu sau khi cấu trúc đã đổi.

7. **Backtest riêng kỹ năng gắn nhãn, tách khỏi kỹ năng entry.** Mỗi tuần lấy 10 đoạn chart cũ, che phần bên phải, chấm degree rồi so với diễn biến thật. Kỹ năng này đo được ([[02 - Skill Metrics]]) và cải thiện nhanh hơn nhiều khi luyện tách rời khỏi áp lực vào lệnh.
