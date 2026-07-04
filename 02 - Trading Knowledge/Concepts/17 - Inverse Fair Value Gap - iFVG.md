---
type: ict-concept
concept: Inverse Fair Value Gap
aliases:
  - IFVG
  - Inversion FVG
  - Inverse Fair Value Gap
tags:
  - trading/ict/concept
  - trading/study
  - "#IFVG"
status: developing
category: PD Array
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
last_reviewed: 2026-07-02
created: 2026-06-23
updated: 2026-07-02
common_mistakes:
  - "[[Mistake - IFVG From Wick Only]]"
  - "[[Mistake - Hold Failed FVG]]"
---

# Inverse Fair Value Gap

> [!summary] Tóm tắt 1 câu
> **Inverse Fair Value Gap (IFVG) là một FVG đã bị giá ĐÓNG NẾN xuyên qua (violated), khiến nó đảo cực: một bullish FVG thất bại (giá đóng dưới nó) trở thành kháng cự bearish, còn một bearish FVG thất bại (giá đóng trên nó) trở thành hỗ trợ bullish; giá retrace về retest vùng gap cũ và phản ứng theo hướng NGƯỢC LẠI.**

> [!important] Nguyên tắc cốt lõi
> **Điều kiện sống còn của IFVG là CANDLE CLOSE qua FVG, không phải chỉ bóng nến chọc qua. Đóng nến xuyên qua = thị trường chấp nhận giá ở phía bên kia → FVG đảo cực. Bóng chọc rồi đóng lại bên trong = FVG vẫn còn hiệu lực (vẫn respect), KHÔNG phải IFVG.**
> IFVG là tín hiệu mạnh cho thấy delivery đã đổi chiều, thường đi kèm [[21 - Market Structure Shift|MSS]] — chỉ trade retest IFVG khi nó đồng hướng bias MỚI.

---

## 1. Định nghĩa

**Khái niệm:**  
Một [[Fair Value Gap|Fair Value Gap (FVG)]] bình thường là vùng imbalance mà giá có xu hướng quay lại rebalance và phản ứng theo hướng của FVG (bullish FVG = hỗ trợ, bearish FVG = kháng cự). Nhưng khi giá **đóng nến xuyên thẳng qua** FVG đó (violate), FVG "thất bại" — và thay vì biến mất, nó **đảo cực tính (polarity flip)**:

- **Bullish FVG fail → Bearish IFVG:** khi giá đóng nến XUỐNG xuyên qua một bullish FVG, vùng gap cũ (vốn là hỗ trợ) đảo thành **kháng cự**. Giá retrace LÊN test lại vùng đó và bị reject xuống → cơ hội Short.
- **Bearish FVG fail → Bullish IFVG:** khi giá đóng nến LÊN xuyên qua một bearish FVG, vùng gap cũ (vốn là kháng cự) đảo thành **hỗ trợ**. Giá retrace XUỐNG test lại vùng đó và bật lên → cơ hội Long.

**Bản chất:** IFVG dựa trên logic "support becomes resistance / resistance becomes support" nhưng áp dụng cho một PD array cụ thể (FVG). Khi một imbalance bị chối bỏ một cách dứt khoát (đóng nến qua), những ai đã vào lệnh theo hướng cũ của FVG đang mắc kẹt; vùng gap cũ trở thành nơi họ thoát lệnh (cung cấp thanh khoản ngược hướng). Đó là lý do giá phản ứng NGƯỢC tại retest. IFVG thường đánh dấu một sự **đổi delivery**, vì vậy nó hay xuất hiện cùng MSS.

**Điều kiện cốt lõi — CLOSE, không phải WICK:**
- **Đóng nến (body close) xuyên qua FVG** = violation thật → đảo cực thành IFVG.
- **Chỉ bóng nến (wick) chọc qua rồi đóng lại bên trong** = FVG vẫn respect, KHÔNG đảo cực. Đây là lỗi phổ biến nhất khi giao dịch IFVG.

**Mục đích trong ICT:**  
- **Bắt điểm đảo delivery:** IFVG là tín hiệu sớm cho thấy hướng cũ đã bị chối bỏ.
- **Cung cấp POI mới đồng hướng bias mới:** retest IFVG là entry theo hướng đảo, đặc biệt mạnh khi đi kèm MSS.
- **Định stop logic rõ ràng:** stop nằm ngoài đầu kia của IFVG (phía mà nếu giá vượt qua, sự đảo cực bị phủ nhận).
- **Xác nhận một FVG cũ đã chết:** thay vì cố giữ lệnh theo FVG đã fail, chuyển tư duy sang IFVG.

**Vì sao khái niệm này quan trọng:**  
IFVG là cách ICT biến một "FVG thất bại" thành cơ hội thay vì một cú stop. Nhiều trader thấy FVG bị xuyên thì hoang mang; người hiểu IFVG biết rằng vùng đó vừa đảo vai trò và là một POI chất lượng cho hướng mới. Nó cũng dạy kỷ luật quan trọng: **đừng cố giữ lệnh theo một FVG mà giá đã đóng nến xuyên qua.**

**Nó giúp trả lời câu hỏi nào trên chart?**
- FVG này còn hiệu lực hay đã bị đóng nến xuyên qua (đảo thành IFVG)?
- Delivery có vừa đổi chiều không (IFVG + MSS)?
- Vùng gap cũ giờ là hỗ trợ hay kháng cự?
- Đâu là POI mới đồng hướng bias mới để retest?

![[IFVG-Advanced-Anatomy.svg|697]]

> Giải phẫu một Bearish IFVG hoàn chỉnh: bullish FVG hình thành trong nhịp tăng, rồi bị một nến giảm ĐÓNG BODY xuyên thẳng xuống qua (violation) kèm displacement + MSS bearish; vùng gap cũ đảo cực thành kháng cự, giá retrace LÊN retest → reject → Short với stop trên high IFVG và target là SSL. Bullish IFVG (bearish FVG fail) là chuỗi đối xứng ngược lại.

### Inverse FVG không phải là gì
- Không phải là [[14 - Implied Fair Value Gap|Implied FVG]] — đó là khái niệm KHÁC (xem mục phân biệt bên dưới).
- Không phải kích hoạt bởi bóng nến — bắt buộc đóng nến (body close) qua FVG.
- Không phải tín hiệu đảo độc lập — cần đồng hướng bias mới / MSS để đáng tin.
- Không phải mọi FVG bị chạm đều thành IFVG — phải bị đóng nến XUYÊN QUA, không phải chỉ lấp.
- Không phải lý do để nhồi lệnh ngược trend khi chưa có xác nhận đổi delivery.

---

## 2. Bối cảnh sử dụng

### Phân biệt IFVG với Implied FVG (rất quan trọng)

> [!warning]
> **IFVG ≠ Implied FVG. Đây là hai khái niệm hoàn toàn khác nhau, dễ nhầm vì cùng viết tắt gần giống.**

| Tiêu chí | Inverse FVG (IFVG) | [[Implied Fair Value Gap|Implied FVG]] |
|---|---|---|
| **Bản chất** | Một FVG đã bị ĐÓNG NẾN xuyên qua → đảo cực | Một vùng imbalance "ngầm" suy ra từ cấu trúc nến (không phải gap 3 nến chuẩn) |
| **Cơ chế** | Polarity flip: hỗ trợ ↔ kháng cự sau violation | Vùng inefficiency ẩn giữa các bóng nến lớn / overlap |
| **Tín hiệu** | Đổi delivery, thường kèm MSS | Vẫn là một PD array để rebalance theo hướng gốc |
| **Cách dùng** | Retest → trade NGƯỢC hướng FVG cũ | Treat như FVG thông thường (cùng hướng) |

![[IFVG-Advanced-vs-Implied.svg|697]]

> Hai mini chart minh họa khác biệt cốt lõi: bên trái, IFVG là một FVG đã bị đóng nến xuyên qua → đảo cực → trade NGƯỢC hướng gốc; bên phải, [[14 - Implied Fair Value Gap|Implied FVG]] là vùng imbalance ngầm suy từ overlap các bóng nến lớn, vẫn sống và được rebalance theo CÙNG hướng. Hỏi trước khi vào lệnh: "Vùng này đã bị ĐÓNG NẾN xuyên qua chưa?" — Có → IFVG; Chưa → PD array thường.

### Các trạng thái của FVG dẫn tới IFVG

| Quan sát | Tên gọi | Kết quả |
|---|---|---|
| Giá chạm CE/mép FVG rồi reject | Respect | FVG còn hiệu lực — không phải IFVG |
| Bóng nến chọc qua FVG, body đóng lại bên trong | Wick test | FVG vẫn respect — KHÔNG đảo cực |
| Body nến đóng XUYÊN qua FVG, giá giữ phía bên kia | Violation / Inversion | FVG đảo cực thành IFVG |
| Sau inversion, giá retrace về vùng gap cũ | IFVG retest | Phản ứng NGƯỢC hướng FVG cũ → entry |

> [!tip]
> IFVG mạnh nhất khi sự violation đi kèm **displacement + MSS** (đổi cấu trúc). Một FVG bị đóng nến xuyên qua một cách yếu ớt (không displacement, không phá swing) là tín hiệu IFVG kém tin cậy hơn nhiều.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có một FVG rõ vừa bị **đóng nến xuyên qua** (không phải chỉ bóng).
- [ ] Violation đi kèm displacement + [[21 - Market Structure Shift|MSS]] đổi hướng.
- [ ] IFVG đồng hướng [[12 - Daily Bias|bias mới]] sau khi đảo.
- [ ] Giá retrace về retest vùng IFVG trong kill zone.
- [ ] Có liquidity target rõ ràng theo hướng mới.

### Khi nào nên bỏ qua?
- [ ] FVG chỉ bị **bóng nến** chọc qua, body đóng lại bên trong (vẫn respect).
- [ ] Violation không có displacement / không phá cấu trúc (đảo cực yếu).
- [ ] "IFVG" ngược bias HTF mà không có bằng chứng đổi delivery thật.
- [ ] Nhầm IFVG với Implied FVG → trade sai hướng.
- [ ] Ngoài kill zone / không có target rõ.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Một FVG gốc rõ ràng** (bullish hoặc bearish) trước đó.
2. **Một nến đóng (body close) xuyên thẳng qua** FVG đó — đây là điều kiện bắt buộc.
3. **Displacement + MSS** kèm theo violation (tăng độ tin cậy).
4. **Giá giữ ở phía bên kia** FVG sau khi đóng nến qua (acceptance).
5. **Retrace về retest** vùng gap cũ — nơi giờ đảo vai trò S/R.

### Ma trận nhận diện IFVG

| Thành phần | Bearish IFVG (từ bullish FVG fail) | Bullish IFVG (từ bearish FVG fail) | Cảnh báo / không hợp lệ |
|---|---|---|---|
| **FVG gốc** | Bullish FVG (BISI) | Bearish FVG (SIBI) | Không có FVG gốc rõ |
| **Violation** | Đóng nến XUỐNG xuyên qua | Đóng nến LÊN xuyên qua | Chỉ bóng chọc qua → không tính |
| **Vai trò mới** | Vùng cũ → kháng cự | Vùng cũ → hỗ trợ | Không có acceptance phía bên kia |
| **Hướng trade** | Short tại retest | Long tại retest | Ngược bias mới mà không có MSS |
| **MSS** | MSS bearish kèm theo | MSS bullish kèm theo | Không có MSS → đảo cực yếu |

### Điều kiện bắt buộc
- [ ] Có FVG gốc xác định rõ.
- [ ] Có **đóng nến (body close)** xuyên qua FVG (không phải bóng).
- [ ] Giá giữ ở phía bên kia FVG (acceptance), không quay lại đóng trong gap.
- [ ] Xác định được vùng IFVG để chờ retest.

### Điều kiện tăng xác suất
- [ ] Violation đi kèm displacement mạnh.
- [ ] Có MSS đổi cấu trúc cùng lúc.
- [ ] IFVG đồng hướng Daily Bias mới.
- [ ] Retest IFVG nằm đúng premium/discount cho hướng mới.
- [ ] Có liquidity target rõ ràng phía bên kia.

### Điều kiện làm setup yếu đi
- Violation chỉ bằng một nến nhỏ, không displacement.
- Không có MSS — chỉ là một nhịp đóng nến qua rồi do dự.
- Giá nhanh chóng quay lại đóng trong gap (mất acceptance).
- IFVG ngược bias HTF mà không có narrative đổi delivery.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng IFVG
> 1. **FVG gốc có thực sự bị ĐÓNG NẾN xuyên qua không (không phải chỉ bóng)?**
> 2. **Violation có đi kèm displacement + MSS đổi hướng không?**
> 3. **IFVG (vùng cũ) giờ là hỗ trợ hay kháng cự, và có đồng hướng bias mới không?**
> 4. **Đâu là retest và target theo hướng mới — điều gì làm IFVG này invalid?**

### D1 / H4 — Bias & Narrative
- Bias hiện tại: Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- Có dấu hiệu đổi delivery HTF không (một HTF FVG bị đóng nến xuyên qua)?
- Vị trí premium/discount: IFVG retest có nằm đúng phía cho hướng mới không?
- Liquidity target theo hướng mới ở đâu?

### H1 / M15 — IFVG & Context
- **FVG gốc:** ghi rõ vùng FVG gốc và mức CE.
- **Violation:** nến nào đóng xuyên qua? Có displacement/MSS không?
- **IFVG zone:** ghi rõ vùng IFVG để retest, ví dụ `Bullish FVG 1.0850–1.0865 bị đóng nến xuống → bearish IFVG retest 1.0850–1.0865`.
- **Kiểm tra acceptance:** giá có giữ phía bên kia không, hay quay lại trong gap?

### M5 / M1 — Confirmation & Entry
- Giá retrace về retest IFVG chưa?
- Có phản ứng (reject) tại IFVG với displacement/MSS LTF không?
- Entry tại retest IFVG theo hướng mới; stop ngoài đầu kia IFVG.
- Target: liquidity gần trước (partial), liquidity chính sau (full).

```text
Mẫu ghi nhanh — Bearish IFVG (bullish FVG fail)
HTF Bias: chuyển Bearish | Location: Premium
FVG gốc: bullish FVG [low]–[high]
Violation: nến đóng XUỐNG xuyên qua FVG + MSS bearish
IFVG zone: [low]–[high] (giờ là kháng cự)
Kế hoạch: chờ giá retrace LÊN retest IFVG → M5 bearish MSS → Short
Stop: trên high của IFVG / trên sweep high
Target: SSL phía dưới
Invalid: giá đóng nến LÊN lại trên IFVG (lấy lại gap) → bỏ
```

```text
Mẫu ghi nhanh — Bullish IFVG (bearish FVG fail)
HTF Bias: chuyển Bullish | Location: Discount
FVG gốc: bearish FVG [low]–[high]
Violation: nến đóng LÊN xuyên qua FVG + MSS bullish
IFVG zone: [low]–[high] (giờ là hỗ trợ)
Kế hoạch: chờ giá retrace XUỐNG retest IFVG → M5 bullish MSS → Long
Stop: dưới low của IFVG / dưới sweep low
Target: BSL phía trên
Invalid: giá đóng nến XUỐNG lại dưới IFVG (lấy lại gap) → bỏ
```

> [!warning]
> **Một FVG bị bóng nến chọc qua rồi đóng lại bên trong KHÔNG phải IFVG.** Đó vẫn là FVG hợp lệ đang được respect. Vào Short/Long ngược dựa trên "bóng đã xuyên" là lỗi kinh điển → bị quét stop khi giá tiếp tục theo hướng gốc của FVG.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] FVG gốc bị **đóng nến (body close)** xuyên qua, có acceptance phía bên kia.
- [ ] Violation đi kèm displacement + MSS đổi hướng.
- [ ] IFVG đồng hướng bias mới.
- [ ] Giá retrace về retest IFVG và reject với displacement/MSS LTF.
- [ ] Entry theo hướng mới; stop ngoài đầu kia IFVG.
- [ ] Có target liquidity rõ ràng, R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] FVG chỉ bị bóng nến chọc qua (body đóng trong gap) → vẫn là FVG, không phải IFVG.
- [ ] Giá đóng nến lại VƯỢT QUA IFVG theo hướng cũ (lấy lại gap) → đảo cực bị phủ nhận.
- [ ] Violation không có displacement/MSS → đảo cực yếu, không trade.
- [ ] Nhầm IFVG với Implied FVG → hướng trade sai.
- [ ] IFVG ngược bias HTF mà không có bằng chứng đổi delivery thật.

### CLOSE vs WICK — bảng quyết định

| Quan sát tại FVG | Phán quyết | Hành động |
|---|---|---|
| Bóng chọc qua, body đóng trong gap | FVG vẫn respect | Trade theo hướng GỐC của FVG (không phải IFVG) |
| Body đóng xuyên qua, giá giữ bên kia | Inversion xác nhận | Chờ retest → trade NGƯỢC hướng FVG cũ |
| Body đóng xuyên, rồi đóng lại quay vào gap | Inversion thất bại | Bỏ; FVG có thể vẫn còn hiệu lực |
| Đóng xuyên + displacement + MSS | IFVG chất lượng cao | Ưu tiên retest entry theo hướng mới |

![[IFVG-Advanced-Close-vs-Wick.svg|697]]

> Đây là điều kiện sống còn của IFVG, minh họa hai panel: TRÁI — bóng nến chọc qua gap nhưng body đóng lại BÊN TRONG → FVG vẫn respect, không đảo cực, giá tiếp tục hướng gốc; PHẢI — body đóng xuyên qua và giữ giá bên kia (acceptance) → inversion xác nhận → IFVG. Trước khi đảo tư duy sang IFVG, luôn chờ candle CLOSE, rồi mới chờ retest.

### Nâng cao — IFVG vs Breaker vs Mitigation: ba cách "đảo cực" và điểm chung MSS

IFVG không phải khái niệm "đảo cực" duy nhất trong ICT. Ba PD array cùng dựa trên logic **vùng cũ đổi vai trò sau khi cấu trúc đổi** — nhưng khác nhau ở *nguồn gốc vùng* và *sự kiện kích hoạt*. Hiểu rõ ba cái này giúp bạn không gọi nhầm tên và chọn đúng vùng để retest.

| Tiêu chí | Inverse FVG (IFVG) | [[04 - Breaker Block\|Breaker Block]] | [[22 - Mitigation Block\|Mitigation Block]] |
|---|---|---|---|
| **Vùng gốc** | Một [[Fair Value Gap\|FVG]] (imbalance 3 nến) | Một [[Order Block]] tạo swing high/low **bị phá** kèm sweep | Order block của một swing **không** lấy được liquidity trước khi bị phá |
| **Sự kiện kích hoạt** | Đóng nến (body close) XUYÊN qua FVG | Giá sweep liquidity → phá qua OB → OB đảo vai trò | Giá phá cấu trúc, quay lại "mitigate" OB chưa hoàn thành nhiệm vụ |
| **Bản chất đảo cực** | Imbalance bị chối bỏ → hỗ trợ ↔ kháng cự | OB bị vô hiệu sau sweep → đảo vai trò S/R | OB được dùng lại để phân phối phần lệnh còn kẹt |
| **Tín hiệu đi kèm** | Displacement + [[21 - Market Structure Shift\|MSS]] | Sweep + MSS (gần như bắt buộc) | MSS, thường không cần sweep rõ như breaker |
| **Hướng trade** | NGƯỢC hướng FVG cũ tại retest | Theo hướng breaker sau khi đảo | Theo hướng cấu trúc mới tại retest OB |

> [!tip] Điểm chung then chốt
> Cả ba đều **mạnh nhất khi đi kèm MSS**. MSS là bằng chứng "cấu trúc đã đổi" — nếu không có nó, cả ba chỉ là vùng cũ bị chạm ngẫu nhiên, không phải đảo cực thật. Khi phân vân "đây là IFVG hay breaker", hãy hỏi: vùng gốc là *một FVG bị đóng nến xuyên* (→ IFVG) hay *một OB bị phá sau sweep* (→ breaker)? Bản chất PD array khác nhau, nhưng playbook retest gần như giống hệt.

### Nâng cao — Phân tầng chất lượng inversion theo displacement + MSS + acceptance

Không phải mọi IFVG đều ngang nhau. Chất lượng của một inversion phụ thuộc vào ba trục: **độ mạnh displacement** của cú violation, **có/không MSS** đi kèm, và **độ vững của acceptance** phía bên kia. Dùng bảng dưới để chấm tier trước khi tin một IFVG — và ghi lại tier đó vào journal để có số liệu riêng.

| Tier | Displacement khi violation | MSS đi kèm | Acceptance phía bên kia | Đánh giá & hành động |
|---|---|---|---|---|
| **A — cao nhất** | Nến body lớn, để lại FVG mới cùng hướng | Có, phá swing có ý nghĩa | Nhiều nến giữ hẳn bên kia, không quay lại gap | IFVG chất lượng cao — ưu tiên retest entry theo sequence |
| **B — khá** | Body close rõ nhưng không quá mạnh | Có MSS nhưng phá swing nhỏ | Giá giữ bên kia nhưng do dự vài nến | Trade được nếu đồng bias + đúng premium/discount; giảm size |
| **C — yếu** | Body vừa đủ đóng qua, không displacement | Không có MSS | Acceptance mong manh, sát mép gap | Đảo cực nghi ngờ — chỉ theo dõi, chờ thêm xác nhận, thường bỏ |
| **Loại (không hợp lệ)** | Chỉ bóng chọc qua, body đóng trong gap | — | Giá quay lại đóng trong gap | KHÔNG phải IFVG — FVG vẫn respect, trade theo hướng gốc |

> [!warning]
> Trục dễ bị bỏ qua nhất là **acceptance**. Một violation có displacement + MSS đẹp nhưng ngay sau đó giá đóng nến quay lại trong gap = inversion thất bại, không phải IFVG tier A. Acceptance là "bằng chứng thị trường chấp nhận giá ở phía mới" — thiếu nó, sự đảo cực chưa hoàn tất.

### Nâng cao — Dùng CE của IFVG để refine entry và đo acceptance

Giống như FVG thường, một IFVG có [[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment (CE)]] — điểm giữa của vùng gap cũ. CE là công cụ tinh chỉnh mạnh cho cả entry lẫn việc đánh giá acceptance:

1. **Refine entry:** thay vì đặt lệnh ở mép xa của IFVG (retest nông) hay chờ giá xuyên hết vùng (retest sâu, dễ trượt), nhiều trader vào tại **CE của IFVG** — điểm cân bằng giữa xác suất được khớp và chất lượng giá. Với bearish IFVG, Short quanh CE khi giá retrace lên; stop vẫn nằm trên high của IFVG (ngoài đầu kia).
2. **Đo acceptance bằng CE:** sau violation, nếu giá **không thể đóng nến quay lại quá CE** về phía gap cũ, đó là acceptance mạnh — đảo cực vững. Ngược lại, nếu giá dễ dàng đóng nến vượt CE ngược lại vào gap, hãy nghi ngờ inversion (tier tụt xuống C hoặc loại).
3. **Kết hợp premium/discount:** CE của IFVG nên nằm đúng phía cho hướng mới — bearish IFVG lý tưởng có CE trong premium, bullish IFVG có CE trong discount. CE rơi vào vùng sai phía là dấu hiệu retest kém chất lượng.

> [!tip]
> CE cũng là mốc quản trị lệnh rõ ràng: với bearish IFVG đã Short, một nến đóng vượt lên trên CE ngược vào gap là cảnh báo sớm; đóng nến vượt hẳn high IFVG là invalidation dứt khoát (giá đã "lấy lại gap"). Dùng CE làm lớp cảnh báo trước, high/low IFVG làm ranh giới thoát cứng.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[Inverse-Fair-Value-Gap-Example-Correct.svg|697]]

**Mô tả:**  
Một bullish FVG hình thành trong một nhịp tăng. Sau đó một nến giảm mạnh **đóng nến xuyên thẳng xuống qua** FVG (violation), kèm displacement và MSS bearish — bias chuyển sang bearish. Vùng bullish FVG cũ giờ đảo thành **kháng cự (bearish IFVG)**. Giá retrace LÊN retest vùng đó, reject với M5 bearish MSS → entry Short. Stop trên high IFVG; target là SSL phía dưới.

**Vì sao đây là ví dụ tốt:**
- Có **đóng nến (body close)** xuyên qua FVG, không phải chỉ bóng.
- Violation đi kèm displacement + MSS → đổi delivery rõ ràng.
- Entry tại retest IFVG đồng hướng bias mới (bearish).
- Stop logic và target liquidity (SSL) rõ ràng.

### Ví dụ sai / dễ nhầm
![[Inverse-Fair-Value-Gap-Example-Wrong.svg|697]]

**Mô tả lỗi:**  
Một bullish FVG bị một nến có **bóng dưới dài chọc qua**, nhưng thân nến (body) đóng lại NGAY TRÊN FVG — tức FVG vẫn được respect. Trader vội cho rằng FVG "đã đảo cực" và vào Short (tưởng đã thành IFVG). Thực tế giá bật lên từ bullish FVG đúng theo hướng gốc, tăng tiếp về BSL, quét stop của lệnh Short.

**Bài học:**
- IFVG cần **đóng nến (body close)** xuyên qua, KHÔNG phải bóng nến.
- Bóng chọc qua = FVG vẫn còn hiệu lực, vẫn respect hướng gốc.
- Chờ candle close xác nhận trước khi đảo tư duy sang IFVG.

---
### Sequence mẫu — Bearish IFVG (bullish FVG fail) → Short
```text
Bullish FVG cũ tồn tại
→ Nến đóng (body close) XUỐNG xuyên qua FVG (violation)
→ Displacement + MSS bearish → bias chuyển bearish
→ Vùng FVG cũ đảo cực thành KHÁNG CỰ (bearish IFVG)
→ Giá retrace LÊN retest vùng IFVG
→ M5/M1 bearish MSS + displacement xác nhận
→ Entry Short tại retest; Stop trên high IFVG
→ Target: SSL phía dưới
```

![[IFVG-Advanced-Sequence-Chain.svg|697]]

> Toàn bộ chuỗi Bearish IFVG dưới dạng hộp nối mũi tên: Bullish FVG cũ → nến close xuyên xuống (violation) → displacement + MSS bearish → vùng đảo cực = bearish IFVG → retrace lên retest → M5 bearish MSS confirm → Short → target SSL. Mỗi mắt xích phải có mặt đúng thứ tự; nếu giá đóng nến lấy lại gap thì đảo cực bị phủ nhận và setup bị bỏ.

### Sequence mẫu — Bullish IFVG (bearish FVG fail) → Long
```text
Bearish FVG cũ tồn tại
→ Nến đóng (body close) LÊN xuyên qua FVG (violation)
→ Displacement + MSS bullish → bias chuyển bullish
→ Vùng FVG cũ đảo cực thành HỖ TRỢ (bullish IFVG)
→ Giá retrace XUỐNG retest vùng IFVG
→ M5/M1 bullish MSS + displacement xác nhận
→ Entry Long tại retest; Stop dưới low IFVG
→ Target: BSL phía trên
```

> [!note]
> IFVG là "anh em sinh đôi" của [[Order Block]] kiểu breaker: cả hai đều dựa trên logic vùng cũ đảo vai trò sau khi cấu trúc đổi. Khác biệt: IFVG bắt nguồn từ một FVG bị đóng nến xuyên qua, còn breaker bắt nguồn từ một OB bị phá. Cả hai mạnh nhất khi đi kèm MSS.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> IFVG chỉ có giá trị khi có **candle close qua FVG + displacement/MSS + đồng hướng bias mới + đúng premium/discount**.

### A. Context (HTF)
- [ ] Daily Bias / bias mới rõ: `Bullish / Bearish`.
- [ ] Có FVG gốc bị **đóng nến** xuyên qua (xác nhận violation).
- [ ] Violation đi kèm displacement + MSS đổi hướng.
- [ ] IFVG retest nằm đúng premium (Short) / discount (Long).
- [ ] Có liquidity target rõ ràng theo hướng mới.
- [ ] Không nhầm với Implied FVG.

### B. Execution (LTF)
- [ ] Giá retrace về retest vùng IFVG.
- [ ] Giá reject tại IFVG, không đóng nến lấy lại gap.
- [ ] Có MSS + displacement LTF xác nhận hướng mới.
- [ ] Entry tại retest theo hướng mới — không vào ngay lúc violation.
- [ ] Stop logic: ngoài đầu kia IFVG / ngoài điểm sweep.
- [ ] R:R đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Chỉ bóng nến chọc qua (không đóng nến) → không trade IFVG.
- [ ] Không có displacement/MSS → đảo cực yếu → không trade.
- [ ] Giá đóng nến lấy lại gap → đảo cực phủ nhận → không trade.
- [ ] IFVG ngược bias HTF không có narrative → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| IFVG từ bóng nến | Coi bóng chọc qua là đảo cực | FVG vẫn respect → giá tiếp tục hướng gốc | Chỉ tính IFVG khi BODY close qua FVG |
| Cố giữ lệnh theo FVG đã fail | FVG bị đóng nến xuyên mà vẫn ôm lệnh cũ | FVG đã chết và đảo cực ngược hướng | Khi FVG bị close qua, chuyển tư duy sang IFVG |
| Vào lệnh ngay lúc violation | Short/Long ngay khi nến đóng xuyên | Chưa retest, dễ bị nhịp hồi quét | Chờ retest IFVG + LTF confirmation |
| Nhầm IFVG với Implied FVG | Trade cùng hướng như FVG thường | Hai khái niệm khác hẳn → sai hướng | Phân biệt rõ: IFVG = đảo cực; Implied = PD array thường |
| Bỏ qua MSS | Trade IFVG khi chưa đổi cấu trúc | Đảo cực yếu, dễ fail | Yêu cầu displacement + MSS kèm violation |
| Stop sai chỗ | Đặt stop bên trong IFVG | Bị quét khi giá test vùng | Đặt stop ngoài đầu kia IFVG |
| IFVG ngược bias HTF | Trade IFVG counter-trend không lý do | Xác suất thấp, target thiếu room | Chỉ trade IFVG đồng hướng bias mới |

---

## 10. Câu hỏi tự kiểm tra

- Mình giải thích IFVG (và điều kiện close vs wick) trong 30 giây không?
- FVG này bị **đóng nến** xuyên qua hay chỉ bóng chọc?
- Violation có đi kèm displacement + MSS không?
- Vùng IFVG giờ là hỗ trợ hay kháng cự, và đồng hướng bias mới không?
- IFVG khác Implied FVG ở điểm nào — mình có đang nhầm không?
- Retest và target theo hướng mới ở đâu?
- Điều gì làm IFVG này invalid (giá lấy lại gap)?
- Setup nào trong journal mình từng nhầm bóng nến là IFVG?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Inverse FVG (IFVG) là gì?
**Đáp:** Là một FVG đã bị giá ĐÓNG NẾN xuyên qua (violated) khiến nó đảo cực: bullish FVG fail → kháng cự bearish; bearish FVG fail → hỗ trợ bullish. Giá retest và phản ứng NGƯỢC hướng FVG cũ.

### Q2
**Hỏi:** Điều kiện sống còn để một FVG trở thành IFVG là gì?
**Đáp:** Phải có CANDLE CLOSE (body close) xuyên qua FVG, không phải chỉ bóng nến. Bóng chọc rồi đóng lại bên trong = FVG vẫn respect.

### Q3
**Hỏi:** IFVG khác Implied FVG thế nào?
**Đáp:** IFVG = một FVG bị đóng nến xuyên qua → đảo cực, trade NGƯỢC hướng. Implied FVG = một vùng imbalance ngầm suy ra từ cấu trúc nến, dùng như PD array thường (cùng hướng). Hai khái niệm hoàn toàn khác nhau.

### Q4
**Hỏi:** Vì sao IFVG thường đi kèm MSS?
**Đáp:** Vì IFVG đánh dấu một sự đổi delivery — hướng cũ bị chối bỏ. MSS xác nhận cấu trúc đã đổi, làm IFVG đáng tin hơn nhiều.

### Q5
**Hỏi:** Khi một bullish FVG bị đóng nến xuống xuyên qua, vùng đó trở thành gì và trade thế nào?
**Đáp:** Trở thành KHÁNG CỰ (bearish IFVG). Chờ giá retrace LÊN retest → reject → Short; stop trên high IFVG; target SSL phía dưới.

### Q6
**Hỏi:** Cách vào lệnh IFVG đúng là gì — ngay khi violation hay sau đó?
**Đáp:** Sau khi violation, chờ giá RETRACE về RETEST vùng IFVG và có LTF confirmation (MSS/displacement), không vào ngay lúc nến đóng xuyên qua.

---

## 12. Liên kết với Trade Journal

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
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "03 - Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
ifvg_origin: bullish-fvg # bullish-fvg (→bearish IFVG) | bearish-fvg (→bullish IFVG)
ifvg_zone: "1.0850 → 1.0865" # vùng IFVG để retest
violation_type: close # close (hợp lệ) | wick (KHÔNG hợp lệ)
violation_with_mss: true # violation có kèm MSS không
ifvg_timeframe: H1 # timeframe của IFVG
entry_on_retest: true # entry tại retest (true) hay ngay lúc violation (false)
ifvg_alignment: aligned # aligned với bias mới | counter
```

> [!tip]
> Sau 30–50 lệnh, so sánh: `violation_type: close` vs `wick`, và `violation_with_mss: true` vs `false`. Mục tiêu là kiểm chứng bằng dữ liệu rằng IFVG chỉ có edge khi có candle close + MSS + retest.

---

## 13. Lesson Learned

### Bài học chính
- IFVG = FVG bị **đóng nến** xuyên qua → đảo cực; trade NGƯỢC hướng FVG cũ tại retest.
- Điều kiện sống còn: **CLOSE chứ không phải WICK**. Bóng chọc qua = FVG vẫn respect.
- IFVG mạnh nhất khi đi kèm displacement + MSS (đổi delivery).
- Đừng cố giữ lệnh theo một FVG đã bị đóng nến xuyên qua — chuyển sang IFVG.
- IFVG ≠ Implied FVG — đừng nhầm hai khái niệm.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ gọi một FVG là IFVG khi có BODY CLOSE xuyên qua nó.
- [ ] Tôi yêu cầu displacement + MSS kèm violation mới trade IFVG.
- [ ] Tôi vào lệnh tại RETEST IFVG, không vào ngay lúc violation.
- [ ] Tôi đặt stop ngoài đầu kia IFVG, không bên trong vùng.
- [ ] Tôi luôn kiểm tra mình đang nói về IFVG hay Implied FVG.

### Câu nhắc nhở khi trade
> **"Đóng nến xuyên FVG = FVG đảo cực. Bóng chọc qua = FVG vẫn sống. Tôi chờ candle close, rồi chờ retest."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt IFVG vs Implied FVG, close vs wick không? |
| Nhận diện trên chart |  | Xác định đúng violation (body close) và vùng IFVG không? |
| Biết khi nào bỏ qua |  | Có bỏ khi chỉ bóng chọc / không MSS không? |
| Kết hợp với context HTF |  | IFVG có đồng hướng bias mới + premium/discount không? |
| Áp dụng vào trade thực tế |  | Entry có xảy ra tại retest sau xác nhận không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup gắn tag `[[Inverse Fair Value Gap]]`.
- [ ] Review riêng: violation close vs wick; có MSS vs không.
- [ ] Thống kê win rate / R theo `violation_type` và `violation_with_mss`.

---

## 15. Best Practices

> [!success] Nguyên tắc vàng
> **"Đóng nến xuyên FVG = FVG đảo cực. Bóng chọc qua = FVG vẫn sống."** Điều kiện sống còn của IFVG là một BODY CLOSE xuyên qua FVG kèm acceptance ở phía bên kia — không phải một cái wick. Chờ candle close xác nhận, rồi chờ retest; đừng đảo tư duy chỉ vì một bóng nến.

1. **Chỉ gọi IFVG khi có BODY CLOSE + acceptance, tuyệt đối không tính wick.** Một bóng nến chọc qua FVG rồi đóng lại BÊN TRONG gap nghĩa là FVG vẫn respect và giá thường tiếp tục hướng gốc — vào ngược ở đây là lỗi kinh điển. Ghi trường `violation_type: close/wick` cho mỗi lệnh; nhóm `wick` gần như luôn có kết quả tệ hơn khi bạn soi lại.

2. **Yêu cầu displacement + MSS đi kèm violation.** Một FVG bị đóng nến xuyên qua một cách yếu ớt (không displacement, không phá swing) là inversion kém tin. IFVG chất lượng cao đánh dấu một sự đổi delivery thật — nên nó gần như luôn trùng một [[21 - Market Structure Shift|MSS]]. Log `violation_with_mss: true/false` và so sánh edge giữa hai nhóm.

3. **Vào lệnh tại RETEST, không tại cây violation.** Sau khi FVG bị close xuyên, chờ giá retrace về retest vùng IFVG rồi mới vào theo hướng mới; vào ngay lúc violation dễ bị nhịp hồi quét. Refine entry quanh CE ([[10 - Consequent Encroachment (Mean Threshold)|Mean Threshold]]) của chính vùng IFVG để có stop ngắn và R:R tốt hơn.

4. **Đặt stop ngoài ĐẦU KIA của IFVG, không bên trong vùng.** Mốc invalidation là khi giá đóng nến "lấy lại gap" (đóng vượt qua IFVG theo hướng cũ) — lúc đó đảo cực bị phủ nhận. Stop đặt bên trong vùng IFVG sẽ bị quét bởi chính nhịp test vùng bình thường.

5. **Phân biệt IFVG với [[14 - Implied Fair Value Gap|Implied FVG]] — hai khái niệm khác hẳn.** IFVG = FVG bị đóng nến xuyên qua → đảo cực → trade NGƯỢC hướng. Implied FVG = vùng imbalance ngầm suy từ cấu trúc nến → dùng như PD array thường, CÙNG hướng. Nhầm hai cái = trade sai hướng hoàn toàn; luôn tự hỏi "mình đang nói về cái nào?".

6. **Chỉ trade IFVG ĐỒNG hướng bias mới, đúng premium/discount.** Một bearish IFVG (từ bullish FVG fail) đáng tin nhất khi retest nằm ở premium và bias đã chuyển bearish; ngược lại cho bullish IFVG ở discount. IFVG counter-trend không có narrative đổi delivery thật thường thiếu room và xác suất thấp.

7. **Xếp hạng chất lượng inversion và backtest theo tổ hợp.** Chấm mỗi IFVG theo: độ mạnh displacement + có/không MSS + độ rõ acceptance. So sánh win rate / average R của nhóm "close + MSS + retest" vs các nhóm thiếu điều kiện qua 30–50 mẫu ([[04 - Backtesting]]) — dữ liệu của chính bạn sẽ chứng minh IFVG chỉ có edge khi hội đủ close + MSS + retest.