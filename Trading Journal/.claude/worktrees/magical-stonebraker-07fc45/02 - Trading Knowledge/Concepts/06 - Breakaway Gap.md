---
type: ict-concept
concept: Breakaway Gap
aliases:
  - Breakaway Gap
  - BAG
tags:
  - trading/ict/concept
  - trading/study
  - "#BreakawayGap"
status: seed
category: PD Array
last_reviewed:
created: 2026-06-26
updated: 2026-07-03
---

# Breakaway Gap (BAG)

> [!summary] Tóm tắt 1 câu
> **Breakaway Gap là khoảng gap/imbalance hình thành khi giá BỨT KHỎI một vùng tích lũy / biên range / mức quan trọng bằng một cú [[Displacement]] mạnh, đánh dấu KHỞI ĐẦU một nhịp/leg xu hướng mới; gap này thường GIỮ (không bị fill nhanh) và đóng vai trò support (bullish BAG) / resistance (bearish BAG) khi giá retest — là tín hiệu tiếp diễn theo hướng break.**

> [!important] Nguyên tắc cốt lõi
> - **Breakaway Gap = "phá range + displacement" → bắt đầu move**, không phải mọi gap đều là breakaway. Phải có một cú bứt khỏi vùng cân bằng/level thật.
> - **Breakaway thì GIỮ và TIẾP DIỄN; Exhaustion thì FILL và ĐẢO CHIỀU.** Phân biệt hai loại này là kỹ năng quan trọng nhất của khái niệm — đừng fade một breakaway gap thật (kỳ vọng nó fill như exhaustion).
> - Trong ICT, breakaway gap thường trùng một [[Fair Value Gap]] / [[21 - Liquidity Void]] do displacement tạo ra; gap "đáng được tôn trọng" này là một **PD array** để vào lệnh tiếp diễn.
> - Mạnh nhất khi **cùng hướng [[12 - Daily Bias]]**, đến **sau một [[20 - Liquidity Sweep]]** quét biên range, và break đi từ premium/discount **hướng về draw on liquidity**.

---

## 1. Định nghĩa

### Khái niệm
**Breakaway Gap (BAG)** là khoảng gap / imbalance hình thành tại thời điểm giá **bứt ra khỏi**:
- một vùng **tích lũy/phân phối (consolidation / accumulation / distribution)**, hoặc
- một **biên của range** ([[03 - Balanced Price Range]]), hoặc
- một **mức quan trọng** (key level, swing, OB cũ),

bằng một cú **[[Displacement]]** quyết liệt. Khoảnh khắc giá "nhảy" ra khỏi vùng cân bằng tạo ra một khoảng inefficiency (imbalance) — đó chính là breakaway gap. Nó đánh dấu **điểm khởi đầu của một leg xu hướng mới**.

### Bản chất
- Breakaway gap sinh ra từ **displacement** (mất cân bằng giữa mua/bán) khi thị trường rời khỏi trạng thái cân bằng — khác với một gap "vu vơ" giữa range.
- Vì đó là cú bứt phá có động lượng, gap này **có xu hướng GIỮ (không bị fill ngay)**: phe mới đang kiểm soát không cho giá quay lại lấp đầy. Khi giá retest, gap đóng vai trò **support (bullish BAG)** hoặc **resistance (bearish BAG)**.
- Đây là **tín hiệu động lượng + tiếp diễn**: thị trường vừa rời vùng cân bằng và có khả năng đi tiếp theo hướng break.

### Phân loại gap trong một xu hướng (bối cảnh classic TA, áp ICT)
Đây là phần cốt lõi cần thuộc — ba loại gap nằm ở ba vị trí khác nhau của một move:

| Loại gap | Vị trí trong move | Hành vi điển hình | Hàm ý |
|---|---|---|---|
| **Breakaway Gap** | **Khởi đầu** move (bứt khỏi range/level) | **GIỮ**, không fill nhanh; là SR khi retest | **Tiếp diễn** — vào theo hướng break |
| **Runaway / Measuring Gap** | **Giữa** xu hướng | Xác nhận động lượng đang chạy; thường cũng giữ | Trend còn khỏe — giữ lệnh |
| **Exhaustion Gap** | **Cuối** move (kiệt sức) | Thường **bị FILL nhanh** | **Cảnh báo đảo chiều** — không đu theo |

> [!important]
> Việc phải tách bạch: **Breakaway (giữ, tiếp diễn)** vs **Exhaustion (fill, đảo chiều)**. Cùng là một "gap" nhìn trên chart, nhưng nếu nó nằm ở cuối move đã chạy dài và bị fill ngay thì đó là exhaustion — fade một exhaustion thì hợp lý, fade một breakaway thật thì sai.

### Khung ICT (cách gắn vào hệ thống)
- Một breakaway gap thường **trùng một [[Fair Value Gap]] / [[21 - Liquidity Void]]** do chính cú displacement bứt range tạo ra.
- Gap "đáng được tôn trọng" này hoạt động như một **PD array / vùng support-resistance** để tìm entry **tiếp diễn** theo hướng break.
- Chất lượng cao nhất khi:
  - **Cùng hướng [[12 - Daily Bias]]** HTF;
  - Xuất hiện **sau một [[20 - Liquidity Sweep]]** quét biên range (lấy thanh khoản ở mép vùng tích lũy);
  - Break đi **từ premium/discount** ([[27 - Premium Discount]]) **hướng về một draw on liquidity** rõ ràng.

### Mục đích trong ICT
- Đánh dấu **điểm khởi đầu** của một nhịp xu hướng → giúp xác định bạn đang ở đầu hay cuối move.
- Cung cấp một **PD array để vào lệnh tiếp diễn** (retest gap edge / FVG bên trong gap).
- Là bằng chứng **thị trường đã rời trạng thái cân bằng** và chọn hướng.

### Vì sao khái niệm này quan trọng
- Nó trả lời câu hỏi sống còn: **"Move này mới bắt đầu (breakaway) hay sắp kết thúc (exhaustion)?"** — quyết định bạn nên đu theo tiếp diễn hay cảnh giác đảo chiều.
- Cho phép vào lệnh **sớm trong leg mới** với stop logic gọn (far side của gap), thay vì đuổi theo giá.

### Nó giúp trả lời câu hỏi nào trên chart?
- Giá vừa **bứt khỏi range/level bằng displacement** thật, hay chỉ là một nhịp dao động trong range?
- Gap này có khả năng **giữ và tiếp diễn** (breakaway) hay sẽ **bị fill và đảo chiều** (exhaustion)?
- Đâu là **vùng retest** (cạnh gap / FVG bên trong) để vào tiếp diễn?
- Stop logic (đóng nến sạch ngược qua gap = invalidation) và target liquidity ở đâu?

### Breakaway Gap không phải là gì
- **Không phải** mọi gap/imbalance — phải có **phá range/level + displacement** rõ.
- **Không phải** Exhaustion Gap — exhaustion nằm cuối move và thường bị fill; breakaway nằm đầu move và nên giữ. Nhầm hai loại này là lỗi nguy hiểm nhất.
- **Không phải** tín hiệu để **fade/đặt kỳ vọng "gap sẽ fill"** — một breakaway thật không fill nhanh.
- **Không phải** tín hiệu độc lập — vẫn cần đúng [[12 - Daily Bias]], [[27 - Premium Discount]], và (lý tưởng) một [[20 - Liquidity Sweep]] trước break.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái

| Trạng thái | Mô tả | Hàm ý giao dịch |
|---|---|---|
| **Bullish Breakaway Gap** | Giá bứt LÊN khỏi biên trên range bằng displacement tăng | Gap là **support** khi retest → tìm **Long** tiếp diễn |
| **Bearish Breakaway Gap** | Giá bứt XUỐNG khỏi biên dưới range bằng displacement giảm | Gap là **resistance** khi retest → tìm **Short** tiếp diễn |
| **BAG + FVG trùng** | Gap breakaway trùng FVG của nhịp displacement | Confluence mạnh, entry refined |
| **BAG đã retest & giữ** | Giá quay lại chạm cạnh gap rồi reject | Xác nhận tiếp diễn; entry chất lượng |
| **BAG bị đóng nến xuyên qua (fill)** | Giá close sạch ngược qua gap | **Invalidation** — có thể là exhaustion / false break |

### Khi nào khái niệm này có giá trị cao? (checklist)
- [ ] Có một cú **bứt khỏi range/level rõ ràng + [[Displacement]]** mạnh.
- [ ] Break **cùng hướng [[12 - Daily Bias]]** HTF.
- [ ] Có **[[20 - Liquidity Sweep]]** quét biên range ngay trước cú break.
- [ ] Gap đi **từ premium/discount hướng về một draw on liquidity** ([[27 - Premium Discount]]).
- [ ] Breakaway gap **trùng một [[Fair Value Gap]] / [[21 - Liquidity Void]]** của nhịp displacement.
- [ ] Có target liquidity rõ ở phía hướng break.

### Khi nào nên bỏ qua? (checklist)
- [ ] Không có phá range/level thật — chỉ là dao động trong range.
- [ ] Không có displacement (cú break yếu, nến nhỏ, không momentum).
- [ ] Move đã chạy rất dài → gap khả năng là **exhaustion**, không phải breakaway.
- [ ] Break **ngược [[12 - Daily Bias]]** HTF.
- [ ] Giá đóng nến sạch ngược qua gap (đã invalidation).
- [ ] Không có target liquidity rõ phía hướng break.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Vùng cân bằng trước đó**: range/consolidation hoặc một level quan trọng.
2. **Liquidity sweep (lý tưởng)**: quét biên range trước khi bứt phá.
3. **Displacement bứt phá**: nhịp mạnh rời khỏi vùng cân bằng, tạo imbalance/gap.
4. **Gap GIỮ**: giá không quay lại fill ngay; gap thành SR.
5. **Retest cạnh gap / FVG**: điểm vào lệnh tiếp diễn.

```text
Bullish Breakaway Gap
                                  ┌── displacement bứt lên (gap/FVG)
        range / consolidation     │
   ┌───────────────────────┐      │   ● retest cạnh gap = LONG
   │   ~~~ cân bằng ~~~     │──────┘   (gap làm support, giữ, không fill)
   └───────────────────────┘
        ↑ sweep SSL biên dưới trước khi break (lý tưởng)
```

### Ma trận nhận diện

| Thành phần | Bullish BAG (→ Long) | Bearish BAG (→ Short) | Cảnh báo / không phải BAG |
|---|---|---|---|
| **Vùng trước break** | Range/level, giá đang cân bằng | Range/level, giá đang cân bằng | Không có range/level rõ |
| **Sweep (lý tưởng)** | Quét SSL biên dưới range | Quét BSL biên trên range | Không có sweep |
| **Displacement** | Bứt LÊN phá biên trên + imbalance | Bứt XUỐNG phá biên dưới + imbalance | Cú break yếu, không momentum |
| **Hành vi gap** | GIỮ, làm support khi retest | GIỮ, làm resistance khi retest | Bị fill nhanh → exhaustion/false |
| **Vị trí trong move** | Đầu leg mới | Đầu leg mới | Cuối move đã chạy dài |
| **Bias** | Cùng bias bullish | Cùng bias bearish | Ngược bias |

### Điều kiện bắt buộc (must-have)
- [ ] Xác định vùng cân bằng/level mà giá bứt khỏi.
- [ ] Có **displacement** thật tạo gap/imbalance khi break.
- [ ] Xác định cạnh gap (entry zone) và mức invalidation (đóng nến sạch ngược qua gap).
- [ ] Đặt trong bối cảnh [[12 - Daily Bias]] / [[27 - Premium Discount]].

### Điều kiện tăng xác suất (nice-to-have)
- [ ] Có [[20 - Liquidity Sweep]] quét biên range trước break.
- [ ] Gap trùng một [[Fair Value Gap]] / [[21 - Liquidity Void]].
- [ ] Cùng hướng [[12 - Daily Bias]], đi về một draw on liquidity rõ.
- [ ] BAG trên HTF (D1/H4) làm khung lớn, LTF refine entry.
- [ ] Có [[21 - Market Structure Shift]] / [[Break of Structure]] đi kèm xác nhận hướng.

### Điều kiện làm setup yếu đi (warning)
- Displacement mờ nhạt, gap nhỏ / không rõ.
- Move đã chạy quá xa (nguy cơ exhaustion).
- Gap bị test nhiều lần, ăn mòn.
- Không có target liquidity rõ.

### Nâng cao — Định lượng độ mạnh của displacement tạo breakaway

"Displacement mạnh" là một phán đoán trực quan dễ sai lệch: một cây nến trông "to" trên chart NQ1 khung M1 có thể chỉ là nhiễu bình thường, trong khi một cây nến "vừa phải" trên D1 XAUUSD đã là một cú bứt phá cực đoan. Nếu chỉ eyeball, hai trader nhìn cùng một breakout có thể kết luận trái ngược nhau về việc đó có phải breakaway thật hay không. Cần một phép đo tương đối — giống cách [[31 - Standard Deviation]] dùng bội số của một đoạn tham chiếu thay vì áng chừng bằng mắt — để tách bạch một cú break đáng tin khỏi một cú break yếu dễ thành false break.

![[BreakawayGap-Advanced-DisplacementStrength.svg]]
*Ba nến cùng phá một biên range nhưng độ mạnh khác nhau: yếu (body ≈ 0.8x range trung bình 10-20 nến trước, ≈45% tổng range nến, mất 6-8 nến mới phá xong biên), vừa (body ≈ 2x average range, ≈65% tổng range, phá trong 2-3 nến), và mạnh (body ≥ 3.5x average range, ≥80% tổng range, phá chỉ trong 1 nến). Tier càng cao, breakaway càng đáng tin.*

Ba phép đo nên dùng song song, tương tự cách tiếp cận của [[28 - Rejection Block]] với tỉ lệ wick/body:

1. **Body nến displacement so với range trung bình của 10-20 nến trước đó** (một proxy kiểu ATR đơn giản, không cần chỉ báo). Đo chiều cao body (open→close) của nến bứt phá, chia cho trung bình biên độ (high-low) của 10-20 nến ngay trước nó. Tỉ lệ càng lớn, cú break càng vượt trội so với "nhịp điệu" bình thường của thị trường ngay trước đó.
2. **Body chiếm bao nhiêu % tổng range (high-low) của chính cây nến displacement.** Body chiếm phần lớn tổng range (thay vì một cây nến có wick dài hai đầu và body nhỏ ở giữa) cho thấy lực mua/bán áp đảo trong suốt cây nến, không chỉ ở một thời điểm ngắn.
3. **Tốc độ / số nến cần dùng để phá xong toàn bộ biên range.** Một cú phá sạch biên chỉ trong 1 nến thể hiện động lượng dứt khoát; một cú phải "cày" qua 6-8 nến nhỏ mới vượt được biên cho thấy phe đối lập vẫn còn kháng cự đáng kể — rủi ro false break/pullback sâu cao hơn.

| Body / avg range (10-20 nến) | Body / total range nến | Tốc độ phá biên | Tier | Hàm ý |
|---|---|---|---|---|
| < 1x avg range | < 50% | 6-8+ nến mới phá xong | **Yếu (weak)** | Dễ là false break; đòi hỏi thêm sweep + FVG rõ mới cân nhắc |
| 1.5x – 3x avg range | 55% – 75% | 2-3 nến | **Vừa (moderate)** | Chỉ trade khi có thêm confluence (sweep, bias, draw on liquidity) |
| > 3.5x avg range | ≥ 80% | 1 nến | **Mạnh (strong)** | Breakaway tin cậy cao; ưu tiên làm POI tiếp diễn chính |

> [!tip]
> Ghi `displacement_atr_ratio` (body / average range 10-20 nến) vào journal cho mỗi breakaway gap đã trade. Sau 20-30 mẫu trên NQ1/EURUSD/XAUUSD, bạn sẽ biết ngưỡng nào thực sự phân biệt breakaway "ăn tiền" khỏi breakaway "yếu dễ fail" trên từng thị trường, thay vì dùng cảm giác "nến to" chung chung.

> [!note] Không nhầm với đo Rejection Block
> Phép đo này nhìn vào **body của nến displacement khi phá RA KHỎI range** (đo động lượng tạo breakaway); còn tỉ lệ wick/body của [[28 - Rejection Block]] nhìn vào **wick của nến tại một swing high/low** (đo sự từ chối). Hai phép đo phục vụ hai câu hỏi khác nhau: "cú break này có mạnh không?" (Breakaway Gap) vs "cú từ chối này có mạnh không?" (Rejection Block) — đừng lẫn hai bảng tier với nhau khi ghi journal.

### Nâng cao — Breakaway Gap lồng nhau đa khung thời gian (nested/fractal breakaway)

Một sai lầm phổ biến khi phân tích đa khung thời gian là coi breakaway gap trên mỗi khung là một "sự kiện" độc lập. Thực tế, một breakaway gap HTF (H4/D1) hầu như luôn được **dệt nên từ một chuỗi breakaway gap nhỏ hơn trên LTF (M15/M5)** xảy ra trong cùng một nhịp displacement — chính cú "một nến" mạnh mẽ trên D1 khi zoom vào M15 lại hiện ra là 2-3 lần bứt phá nhỏ, mỗi lần tự nó cũng đủ điều kiện gọi là một breakaway gap thu nhỏ (range nhỏ → displacement nhỏ → gap nhỏ giữ).

![[BreakawayGap-Advanced-NestedTimeframes.svg]]
*Một breakaway gap H4/D1 duy nhất (khung trên) khi zoom vào M15/M5 (khung dưới) hóa ra gồm 2-3 breakaway gap nhỏ nối tiếp nhau, mỗi cái là một range → displacement → gap thu nhỏ trong cùng nhịp tăng lớn.*

Vì sao điều này quan trọng cho việc tinh chỉnh entry đa khung thời gian:
- **Các LTF breakaway gap bên trong HTF gap là POI tiếp diễn BỔ SUNG, không phải tín hiệu mâu thuẫn.** Nếu bạn đang chờ giá retest toàn bộ HTF gap để vào lệnh nhưng move quá mạnh không bao giờ quay lại đủ sâu, các LTF gap gần nhất chính là cơ hội entry tiếp diễn thực tế hơn — cùng logic, cùng hướng, chỉ khác quy mô.
- **Không nên "hủy" ý tưởng breakaway HTF chỉ vì giá không quay về đúng gap lớn.** Giá retest một trong các LTF gap con (gần điểm hiện tại nhất) vẫn tôn trọng toàn bộ cấu trúc HTF — đó là hành vi nested bình thường, không phải dấu hiệu breakaway HTF thất bại.
- **Áp dụng đúng logic phân tầng như [[31 - Standard Deviation]]**: quy mô POI phải khớp quy mô trade đang cầm. Trade intraday nên ưu tiên retest một LTF gap gần nhất; trade swing đa ngày có thể chờ retest HTF gap tổng nếu còn đủ thời gian nắm giữ.

```text
[WALKTHROUGH — Nested Breakaway trên NQ1]
HTF (H4): Range 21200-21250 → 1 nến H4 bứt lên 21250 → 21480, để lại
          HTF breakaway gap 21250-21310 (nhìn như MỘT cú displacement)

Zoom M15 trong đúng khung giờ của nến H4 đó:
  Leg con #1: range nhỏ 21250-21270 → displacement M15 → gap M15 #1 (21270-21290)
  Leg con #2: range nhỏ 21290-21310 → displacement M15 → gap M15 #2 (21310-21330)
  Leg con #3: range nhỏ 21340-21360 → displacement M15 → gap M15 #3 (21360-21390)

→ Giá sau đó chỉ retrace về gap M15 #3 (gần nhất), KHÔNG quay lại toàn bộ
  HTF gap 21250-21310.
→ Đây vẫn là entry tiếp diễn hợp lệ: cùng bias, cùng câu chuyện HTF, chỉ
  refine bằng LTF gap gần nhất thay vì chờ vô ích một retest sâu hơn.
→ SL: far side của gap M15 #3 (không phải far side của HTF gap).
```

> [!warning]
> Đừng đảo ngược logic: một LTF breakaway gap không tự động có nghĩa gì nếu nó **ngược hướng** hoặc **nằm ngoài** một HTF breakaway gap/bias đang có hiệu lực. Tính "lồng nhau" chỉ có giá trị khi LTF gap nằm **bên trong** phạm vi của nhịp displacement HTF và **cùng hướng** với nó — nếu không, đó chỉ là một breakaway gap LTF độc lập, cần đánh giá lại theo context riêng của nó.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Breakaway Gap
> 1. **Giá có thật sự bứt khỏi một range/level bằng displacement không?**
> 2. **Đây là khởi đầu move (breakaway) hay cuối move (exhaustion)?**
> 3. **Break có cùng [[12 - Daily Bias]] và đi về một draw on liquidity không?**
> 4. **Vùng retest (cạnh gap/FVG), stop (đóng nến xuyên gap) và target ở đâu, R:R bao nhiêu?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** hướng break có cùng [[12 - Daily Bias]] không?
- **Vùng cân bằng:** xác định range/level HTF và biên của nó.
- **Draw on liquidity:** tìm liquidity target phía hướng break.
- **Vị trí move:** đang ở đầu (favorable cho breakaway) hay đã chạy dài (cảnh giác exhaustion)?

### H1 / M15 — POI & Context
- **Xác định breakaway gap cụ thể:** ví dụ `bullish BAG [low]–[high] sau khi displacement phá biên trên range tại [level]`.
- **Confluence:** gap có trùng [[Fair Value Gap]] / [[21 - Liquidity Void]] không?
- **Trạng thái:** gap còn unmitigated chưa, đã retest mấy lần?

### M5 / M1 — Confirmation & Entry
- **Retest:** chờ giá retrace về cạnh gap / FVG bên trong.
- **Confirm:** quan sát giá **giữ** (reject) tại gap; lý tưởng có [[21 - Market Structure Shift]] nhỏ xác nhận tiếp diễn.
- **Entry:** tại cạnh gap / FVG; SL ở far side của gap (đóng nến sạch ngược qua gap = invalidation).
- **Target:** liquidity kế tiếp theo hướng break.

```text
[LONG SETUP — Bullish Breakaway Gap]
- HTF: bias bullish; giá vừa bứt LÊN khỏi range bằng displacement; draw on liquidity phía trên
- Vùng: (lý tưởng) sweep SSL biên dưới range trước break; gap/FVG hình thành khi bứt phá
- LTF: giá retest cạnh gap, giữ (reject) + M5 MSS tiếp diễn
- Entry: ____   SL: dưới far side của gap / dưới biên range [level]
- TP1: liquidity gần nhất [level]   TP2: external BSL / draw chính [level]
- RR dự kiến: ____
- Invalid: đóng nến sạch LẠI XUỐNG xuyên qua gap (có thể là exhaustion/false break)
```

```text
[SHORT SETUP — Bearish Breakaway Gap]
- HTF: bias bearish; giá vừa bứt XUỐNG khỏi range bằng displacement; draw on liquidity phía dưới
- Vùng: (lý tưởng) sweep BSL biên trên range trước break; gap/FVG hình thành khi bứt phá
- LTF: giá retest cạnh gap, giữ (reject) + M5 MSS tiếp diễn
- Entry: ____   SL: trên far side của gap / trên biên range [level]
- TP1: liquidity gần nhất [level]   TP2: external SSL / draw chính [level]
- RR dự kiến: ____
- Invalid: đóng nến sạch LẠI LÊN xuyên qua gap (có thể là exhaustion/false break)
```

> [!warning]
> **Đừng fade một breakaway gap thật.** Nếu giá vừa bứt khỏi range bằng displacement cùng bias, đừng đặt lệnh ngược kỳ vọng "gap sẽ fill" — đó là tâm lý dành cho exhaustion gap. Vào theo hướng break khi retest, không chống lại nó.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Có phá range/level + displacement rõ tạo gap/imbalance.
- [ ] Break cùng [[12 - Daily Bias]], đi về draw on liquidity.
- [ ] (Lý tưởng) có sweep biên range trước break; gap trùng FVG.
- [ ] Giá retest cạnh gap và **giữ** (reject) + LTF confirm.
- [ ] SL ở far side gap; target liquidity rõ; R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Không có displacement / không phá range thật → không phải breakaway.
- [ ] Giá **đóng nến sạch ngược qua gap** → invalidation (có thể là exhaustion/false break).
- [ ] Break ngược bias HTF.
- [ ] Gap nằm cuối một move đã chạy dài → nghi exhaustion.
- [ ] Không có target liquidity rõ.

### Breakaway vs Exhaustion — bảng đọc nhanh

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Gap ở đầu move, sau khi phá range + displacement, GIỮ khi retest | **Breakaway hợp lệ** | Entry tiếp diễn theo hướng break |
| Gap ở giữa trend, xác nhận động lượng, vẫn giữ | **Runaway / measuring** | Giữ lệnh, trend còn khỏe |
| Gap ở cuối move đã chạy dài, bị FILL nhanh | **Exhaustion** | Cảnh báo đảo chiều — không đu theo |
| "Gap" không có range break / không displacement | **Không phải breakaway** | Bỏ; chỉ là imbalance vu vơ |
| Breakaway hợp lệ nhưng giá đóng nến sạch xuyên qua gap | **BAG fail** | Hủy lệnh; cảnh giác false break |

> [!note]
> Một breakaway gap "bị đóng nến xuyên qua" nghĩa là **kế hoạch tiếp diễn bị vô hiệu** cho thời điểm đó — không nhất thiết xóa mốc khỏi chart. Nhưng nếu nó fill sạch ngay sau khi tạo, hãy nghi ngờ đó thực ra là exhaustion / false break, không phải breakaway thật.

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish Breakaway Gap: phá range + displacement, retest giữ, Long tiếp diễn
![[BreakawayGap-Example-Correct.svg]]

**Mô tả:**
Giá tích lũy trong một range; (lý tưởng) quét SSL dưới biên dưới range (sweep). Một **displacement tăng** bứt LÊN phá biên trên range, để lại một **gap/FVG** = breakaway gap. Giá retrace về cạnh gap, **giữ** và reject; M5 cho MSS tiếp diễn. Long tại đó; SL dưới far side gap / dưới biên range; target BSL/draw phía trên.

**Vì sao đây là ví dụ tốt:**
- Có đủ chuỗi **range → (sweep) → displacement bứt phá** trước khi gọi là breakaway.
- Gap **giữ** khi retest (không fill) → đúng bản chất breakaway, không phải exhaustion.
- Entry tiếp diễn cùng [[12 - Daily Bias]], SL logic ở far side gap.
- Target là liquidity rõ ràng phía hướng break.

### Ví dụ sai / dễ nhầm — Fade một breakaway, hoặc gọi exhaustion là breakaway
![[BreakawayGap-Example-Wrong.svg]]

**Mô tả lỗi:**
Trader thấy một gap sau khi giá đã chạy rất dài và đặt lệnh **ngược lại kỳ vọng "gap sẽ fill"** — nhưng đó là một breakaway gap thật, giá đi tiếp và quét stop. HOẶC: gọi một **exhaustion gap** (cuối move, bị fill nhanh) là "breakaway" và đu theo, rồi dính đảo chiều.

**Bài học:**
- Phân biệt **vị trí của gap trong move**: đầu move (breakaway, giữ, tiếp diễn) vs cuối move (exhaustion, fill, đảo chiều).
- Không fade một breakaway thật; không đu theo một exhaustion.
- Phải có **phá range + displacement** mới gọi là breakaway; gắn với [[12 - Daily Bias]] và draw on liquidity.
- Theo dõi xem gap có **bị đóng nến xuyên qua (fill)** không — đó là tín hiệu invalidation quan trọng.

### Giải phẫu Breakaway Gap
![[BreakawayGap-Anatomy.svg]]

**Mô tả:** Sơ đồ chú thích range/consolidation, sweep biên, displacement bứt phá, breakaway gap (FVG/liquidity void), vùng retest, và mức invalidation (đóng nến xuyên gap).

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[ICT 2022 Model]]
- [[Fair Value Gap]]
- [[21 - Liquidity Void]]
- [[Displacement]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[Break of Structure]]
- [[Order Block]]
- [[03 - Balanced Price Range]]
- [[27 - Premium Discount]]
- [[12 - Daily Bias]]
- [[19 - Liquidity]]

### Sequence mẫu — Long từ Bullish Breakaway Gap
```text
HTF Bias Bullish
→ range / consolidation (giá cân bằng)
→ (lý tưởng) Sweep SSL biên dưới range
→ Displacement tăng bứt phá biên trên range → tạo gap/FVG (= Breakaway Gap)
→ Gap GIỮ, không fill (= support)
→ Giá retrace về cạnh gap / FVG (đúng phía discount nội bộ)
→ M5/M1 confirm (giữ + MSS tiếp diễn) → Entry
→ SL: far side của gap / dưới biên range
→ Target: liquidity nội bộ trước, external BSL / draw chính sau
→ Invalid: đóng nến sạch lại xuống xuyên qua gap
```

### Sequence mẫu — Short từ Bearish Breakaway Gap
```text
HTF Bias Bearish
→ range / consolidation (giá cân bằng)
→ (lý tưởng) Sweep BSL biên trên range
→ Displacement giảm bứt phá biên dưới range → tạo gap/FVG (= Breakaway Gap)
→ Gap GIỮ, không fill (= resistance)
→ Giá retrace về cạnh gap / FVG (đúng phía premium nội bộ)
→ M5/M1 confirm (giữ + MSS tiếp diễn) → Entry
→ SL: far side của gap / trên biên range
→ Target: liquidity nội bộ trước, external SSL / draw chính sau
→ Invalid: đóng nến sạch lại lên xuyên qua gap
```

> [!note]
> Breakaway gap hoạt động mạnh nhất khi **đóng vai trò POI tiếp diễn trong khung của [[ICT 2022 Model]]**: cú displacement bứt range vừa tạo MSS/BOS vừa để lại FVG; chính FVG nằm trong breakaway gap là vùng entry refined. Nếu thiếu displacement hoặc không phá range, đừng gọi nó là breakaway.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy một cái gap
> Breakaway gap chỉ là POI tiếp diễn sau khi giá đã bứt range bằng displacement. Chỉ vào khi có context + đúng phía + xác nhận. Không fade một breakaway thật.

### A. Context (HTF)
- [ ] [[12 - Daily Bias]] rõ ràng và break **cùng hướng** bias.
- [ ] Xác định range/level mà giá bứt khỏi.
- [ ] Có displacement thật tạo gap/imbalance.
- [ ] (Lý tưởng) có sweep biên range trước break.
- [ ] Gap đi **từ premium/discount hướng về draw on liquidity** rõ.
- [ ] Đánh giá: đây là đầu move (breakaway) chứ không phải cuối move (exhaustion).

### B. Execution (LTF / khi giá retest)
- [ ] Giá retest cạnh gap / FVG và **giữ** (reject).
- [ ] (Lý tưởng) gap trùng [[Fair Value Gap]] / [[21 - Liquidity Void]].
- [ ] LTF có MSS nhỏ / phản ứng xác nhận tiếp diễn.
- [ ] Entry tại cạnh gap / FVG; SL ở far side gap.
- [ ] Target liquidity rõ; R:R tối thiểu đạt kế hoạch.
- [ ] Risk ≤ 0.5% theo khung rủi ro.

### C. Quy tắc "không có lệnh"
- [ ] Không có displacement / không phá range → không phải breakaway → không trade.
- [ ] Gap nằm cuối move đã chạy dài (nghi exhaustion) → không đu theo.
- [ ] Break ngược bias → không trade.
- [ ] Giá đã đóng nến sạch xuyên qua gap (invalidation/false break) → không trade.
- [ ] Không có target liquidity rõ → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Fade một breakaway thật | Đặt lệnh ngược kỳ vọng "gap sẽ fill" | Breakaway giữ và tiếp diễn → quét stop | Vào THEO hướng break khi retest, không chống lại |
| Nhầm exhaustion thành breakaway | Đu theo gap ở cuối move đã chạy dài | Exhaustion bị fill và đảo chiều | Kiểm tra vị trí gap trong move (đầu vs cuối) |
| Gọi mọi gap là breakaway | Đánh dấu breakaway khi không có range break + displacement | Không có cơ sở tiếp diễn | Yêu cầu phá range/level + displacement rõ |
| Trade ngược bias HTF | Break ngược [[12 - Daily Bias]] vẫn vào | Xác suất thấp | Chỉ trade breakaway cùng bias |
| Bỏ qua xác nhận động lượng | Vào ngay khi thấy gap, không chờ retest/giữ | Có thể là false break | Chờ retest + giữ + LTF confirm |
| Bỏ qua việc gap bị fill | Giữ lệnh khi giá đóng nến xuyên qua gap | Invalidation đã xảy ra | Cắt khi đóng nến sạch ngược qua gap |
| SL quá sát | Đặt SL trong vùng gap | Bị quét dễ dàng | SL ở far side của gap / ngoài biên range |
| Không có target | Trade breakaway không xác định liquidity đích | Không biết chốt ở đâu, R:R mơ hồ | Xác định draw on liquidity trước khi vào |

---

## 10. Câu hỏi tự kiểm tra
- Mình có phân biệt được Breakaway vs Exhaustion gap trong 30 giây không?
- Gap này nằm ở **đầu** hay **cuối** của move?
- Giá đã thật sự **bứt khỏi range/level bằng displacement** chưa?
- Break có **cùng [[12 - Daily Bias]]** và đi về một **draw on liquidity** không?
- Gap có **giữ** khi retest hay đã bị **fill** (invalidation)?
- Gap có trùng [[Fair Value Gap]] / [[21 - Liquidity Void]] không?
- SL (far side gap) và target (liquidity) ở đâu, R:R bao nhiêu?
- Nếu không trade gap này, lý do "No Trade" là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Breakaway Gap là gì?
**Đáp:** Khoảng gap/imbalance hình thành khi giá bứt khỏi một range/level bằng displacement mạnh, đánh dấu khởi đầu một leg xu hướng mới; gap thường giữ (không fill) và là SR cho hướng tiếp diễn.

### Q2
**Hỏi:** Khác biệt cốt lõi giữa Breakaway và Exhaustion gap?
**Đáp:** Breakaway ở **đầu** move, **giữ** (không fill), báo hiệu **tiếp diễn**. Exhaustion ở **cuối** move, thường **bị fill**, cảnh báo **đảo chiều**.

### Q3
**Hỏi:** Hai điều kiện bắt buộc để một gap là breakaway (không phải gap vu vơ)?
**Đáp:** (1) Giá phá khỏi một range/level rõ ràng; (2) Có displacement thật tạo imbalance/gap.

### Q4
**Hỏi:** Trong ICT, breakaway gap thường trùng với cái gì và đóng vai trò gì?
**Đáp:** Thường trùng một [[Fair Value Gap]] / [[21 - Liquidity Void]] của nhịp displacement; đóng vai trò PD array / support-resistance cho entry tiếp diễn.

### Q5
**Hỏi:** Đặt SL cho một bullish breakaway gap ở đâu?
**Đáp:** Ở far side của gap (dưới mép dưới gap) / dưới biên range bị phá. Đóng nến sạch xuống xuyên qua gap = invalidation.

### Q6
**Hỏi:** Khi nào một breakaway setup bị vô hiệu?
**Đáp:** Khi không có range break/displacement (không phải breakaway), khi giá đóng nến sạch ngược qua gap (fill → false break/exhaustion), hoặc khi break ngược bias HTF.

### Q7
**Hỏi:** Điều kiện làm breakaway gap chất lượng cao nhất?
**Đáp:** Cùng [[12 - Daily Bias]], đến sau một [[20 - Liquidity Sweep]] quét biên range, break từ premium/discount hướng về draw on liquidity, và gap trùng FVG.

---

## 12. Lesson Learned

### Bài học chính
- Breakaway = **phá range + displacement → khởi đầu move**; giữ và tiếp diễn.
- Đừng **fade** một breakaway thật; đừng **đu theo** một exhaustion.
- Phân biệt theo **vị trí trong move** (đầu vs cuối) và **hành vi gap** (giữ vs fill).
- Mạnh nhất khi cùng **bias** + sau **sweep** + trùng **FVG** + đi về **draw on liquidity**.
- SL ở **far side gap**; **đóng nến xuyên gap = invalidation**.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ gọi một gap là "breakaway" khi có phá range/level + displacement rõ.
- [ ] Tôi luôn hỏi: gap này ở đầu hay cuối move (breakaway hay exhaustion)?
- [ ] Tôi chỉ trade breakaway cùng [[12 - Daily Bias]] và đi về draw on liquidity.
- [ ] Tôi vào theo hướng break khi retest, không fade gap chờ fill.
- [ ] Tôi đặt SL ở far side gap và cắt khi giá đóng nến sạch xuyên qua gap.

### Câu nhắc nhở khi trade
> **"Breakaway thì GIỮ và đi tiếp; Exhaustion thì FILL rồi quay đầu — đừng nhầm hai cái và đừng fade cái đầu move."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt breakaway vs runaway vs exhaustion không? |
| Nhận diện trên chart |  | Có xác định đúng range break + displacement không? |
| Biết khi nào bỏ qua |  | Có dám bỏ "gap" thiếu range break/displacement không? |
| Kết hợp với context HTF |  | Breakaway có cùng bias + đi về draw on liquidity không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự tại retest gap đã giữ không? |
| Review sau trade |  | Có kiểm tra bằng dữ liệu journal thay vì cảm tính không? |

**Kế hoạch review tiếp theo:**
- [ ] Backtest 10–20 lần breakaway gap trên NQ1/NAS100 & EURUSD; tách riêng breakaway vs exhaustion.
- [ ] Thống kê tỉ lệ gap "giữ" vs "fill" theo vị trí trong move.
- [ ] Đối chiếu với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]].
- [ ] Review lại note này sau 2 tuần, cập nhật `confidence` & `last_reviewed`.

---

## Best Practices

> [!success] Nguyên tắc vàng
> **Một breakaway gap chỉ đáng tin khi có đủ ba yếu tố: phá range/level thật, displacement đủ mạnh theo tỉ lệ định lượng (không phải eyeball), và cùng hướng bias/draw on liquidity.** Thiếu một trong ba, "breakaway" chỉ là cái tên gắn cho một cú dao động bình thường hoặc một cái bẫy fade — đủ cả ba, nó trở thành một trong những tín hiệu tiếp diễn rõ ràng nhất trong bộ công cụ ICT.

1. **Đừng bao giờ fade một breakaway gap thật.** Đây là lỗi tốn tiền nhất gắn với khái niệm này: thấy gap "trông xa" rồi kỳ vọng nó phải fill như một exhaustion gap, trong khi bản chất breakaway là GIỮ và tiếp diễn. Trước khi đặt bất kỳ lệnh ngược nào quanh một gap, tự hỏi: *"Gap này đang ở đầu hay cuối move?"* — câu trả lời quyết định toàn bộ hướng tiếp cận.

2. **Luôn xác nhận đủ chuỗi "phá range/level + displacement" trước khi gọi tên một gap là breakaway.** Không phải mọi khoảng trống trên chart đều là breakaway — thiếu một cú phá cấu trúc thật phía sau, đó chỉ là imbalance vu vơ giữa range. Ghi `range_break_confirmed: yes/no` vào journal cho mỗi gap được đánh dấu, để tránh thói quen gọi bừa mọi gap là "breakaway".

3. **Định lượng độ mạnh displacement thay vì tin vào cảm giác "nến to".** Dùng ngưỡng cụ thể: body ≥ 3.5x average range của 10-20 nến trước, body ≥ 80% tổng range nến, hoặc phá xong biên chỉ trong 1 nến (xem mục "Nâng cao — Định lượng độ mạnh của displacement"). Ghi `displacement_atr_ratio` cho từng lệnh; một breakaway "yếu" theo bảng tier này nên đòi thêm confluence trước khi tin, không nên trade một mình.

4. **Phân biệt dứt khoát Breakaway với Exhaustion bằng vị trí trong move, không chỉ bằng hình dạng nến.** Hai loại gap có thể trông giống hệt nhau trên một khung nhìn hẹp; điều tách bạch chúng là gap này nằm ở **đầu** một nhịp mới hay ở **cuối** một move đã chạy dài. Luôn zoom ra HTF để đặt câu hỏi "move này đã đi được bao xa rồi?" trước khi tin vào bất kỳ gap nào.

5. **Yêu cầu confluence với [[Fair Value Gap]] / [[21 - Liquidity Void]] và lý tưởng một [[20 - Liquidity Sweep]] trước khi coi breakaway là chất lượng cao.** Một cú phá range không kèm sweep vẫn có thể là breakaway thật, nhưng xác suất thấp hơn hẳn so với một cú phá xảy ra ngay sau khi quét sạch thanh khoản ở biên range — đó là dấu hiệu dòng tiền lớn đã "dọn dẹp" trước khi đẩy giá đi. Ghi `liquidity_swept_before_break: yes/no` để so sánh nhóm có sweep với nhóm không.

6. **Đặt SL ở far side của gap (hoặc far side của gap con gần nhất nếu đang refine theo LTF nested gap), không đặt sát mép gần.** Đóng nến sạch xuyên ngược qua gap là mức invalidation chuẩn — đặt SL trong lòng gap khiến lệnh dễ bị quét bởi một nhịp pullback bình thường trước khi giá tiếp diễn đúng hướng.

7. **Khi phân tích đa khung thời gian, tận dụng breakaway gap lồng nhau (nested) thay vì chỉ chờ retest gap HTF.** Nếu move quá mạnh khiến giá không bao giờ quay lại đủ sâu để test toàn bộ HTF gap, các breakaway gap M15/M5 nằm bên trong nhịp displacement đó là POI tiếp diễn hợp lệ để refine entry — không phải tín hiệu mâu thuẫn với câu chuyện HTF. Ghi `nested_ltf_confirmed: yes/no` khi entry dựa trên một LTF gap con thay vì HTF gap gốc.

8. **Backtest 20-30 mẫu breakaway gap trên NQ1/EURUSD/XAUUSD trước khi tin cậy hoàn toàn**, tách riêng theo: có sweep hay không, tier displacement (yếu/vừa/mạnh), và kết quả gap giữ hay bị fill. Chỉ dữ liệu thực chiến mới trả lời được ngưỡng `displacement_atr_ratio` nào thực sự phân biệt breakaway "ăn tiền" khỏi breakaway hay fail trên từng thị trường. Đối chiếu với [[01 - Roadmap]], cập nhật [[02 - Skill Metrics]], và chỉ nâng `confidence` của note này sau khi có đủ bằng chứng thay vì để mãi ở mức seed.

