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
updated: 2026-07-28
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
- *(bổ sung)* Trước gap này có một giai đoạn tích lũy/range rõ ràng ≥ 10-15 nến không, hay gap xảy ra giữa/cuối một move đã chạy dài (dấu hiệu runaway/exhaustion)?
- *(bổ sung)* Gap này có đang hình thành trong 1-5 phút đầu sau một tin lớn không — nếu có, tôi đã chờ ổn định volatility trước khi đánh giá chưa?
- *(bổ sung)* Lần retest đầu tiên, THÂN nến (không phải wick) có giữ ngoài vùng gap không, hay chỉ là wick xuyên qua rồi bật lại?
- *(bổ sung)* Gap này có trùng giờ đóng/mở phiên cuối tuần hoặc maintenance break không — hay là displacement thật trong giờ giao dịch liên tục?
- *(bổ sung)* Nếu đây là breakaway HTF, LTF có đang tạo một "breakaway" ngược hướng không — và tôi có đang nhầm lẫn pullback tự nhiên với tín hiệu đảo hướng thật không?

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

---

## 14. Phân tích chuyên sâu: cơ chế thị trường đằng sau Breakaway Gap

![[BreakawayGap-Deep-Mechanism.svg|720]]
*Sơ đồ cơ chế: vì sao breakaway gap giữ được — dealer phải hedge cùng hướng phá vỡ (short gamma), momentum algo TWAP-chasing đẩy tiếp, và phe thua cuộc trong range cũ bị stop-out một chiều, không còn ai đẩy giá lại.*

### 14.1 Orderflow thật đằng sau Breakaway Gap — ai đang mua/bán mà khiến gap không lấp lại?

Điểm khác biệt cốt lõi giữa breakaway gap và một gap thường (common gap) không nằm ở hình dạng trên chart — cả hai lúc mới xuất hiện đều là "một khoảng giá không giao dịch giữa hai nến". Sự khác biệt nằm ở **ai đang đứng ở phía nào của sổ lệnh ngay sau đó**.

Với breakaway gap thật, ba nguồn lực cùng đẩy về MỘT hướng ngay sau khi phá vỡ:

1. **Dealer/market maker bị buộc hedge cùng hướng (short gamma trigger).** Khi giá phá qua một vùng có nhiều quyền chọn short gamma của dealer (thường quanh các mức tâm lý tròn hoặc vùng đã tích lũy nhiều open interest), dealer phải mua thêm khi giá tăng (hoặc bán thêm khi giá giảm) để giữ trung hòa delta — hành vi này tự nó khuếch đại displacement theo đúng hướng breakout, chứ không hãm nó lại. Đây là lý do vì sao nhiều breakaway gap lớn trên chỉ số (NQ/ES) xảy ra gần vùng có OI quyền chọn tập trung.
2. **Stop-loss của phe thua cuộc trong range cũ bị kích hoạt một chiều.** Toàn bộ short bị stop khi giá phá lên khỏi range (hoặc long bị stop khi phá xuống) đều là market order MUA (hoặc BÁN) — tiếp thêm nhiên liệu đúng hướng phá vỡ, không có lực ngược nào cân bằng lại ngay lúc đó.
3. **Momentum/algo TWAP-VWAP-chasing.** Các quỹ theo chiến lược momentum/trend-following có ngưỡng kích hoạt kỹ thuật (breakout N-ngày cao nhất, ATR breakout...) sẽ vào lệnh MỚI theo đúng hướng phá vỡ trong vài giờ tới vài ngày sau, không phải ngay lập tức nhưng đủ để "giữ giá" không quay đầu lấp gap trong ngắn hạn.

Với **exhaustion gap** (thường bị nhầm là breakaway gap ở đỉnh/đáy một move dài), động lực hoàn toàn khác: đây là các trader momentum CUỐI CÙNG nhảy vào sau khi tin tức/di chuyển đã kéo dài, không có dealer hedge mới hay stop-loss hàng loạt nào tiếp sức — chỉ còn "FOMO buyers/sellers" cuối chu kỳ. Vì không có nguồn lực thật đứng phía sau, gap này thiếu nhiên liệu duy trì và thường bị lấp nhanh khi dòng tiền thông minh chốt lời ngược hướng.

### 14.2 Đối chiếu Auction Market Theory, Wyckoff, orderflow/footprint

| Khung lý thuyết | Khái niệm tương đương | Trùng ở đâu | Khác ở đâu |
|---|---|---|---|
| **Auction Market Theory** | **"Range extension"** sau khi giá thoát khỏi value area cũ với volume cao, "initiative buying/selling" | Cả hai đều mô tả cùng một hiện tượng: đấu giá thoát khỏi vùng cân bằng cũ với lực mua/bán chủ động (initiative), không phải responsive | AMT gắn chặt với **volume profile** (đo bằng volume tại từng mức giá, TPO), breakaway gap của ICT gắn với **hình dạng nến** (gap giữa 2 nến không phải khoảng trống thời gian). Một breakaway gap chart có thể không đi kèm volume extension rõ nếu dữ liệu volume không sẵn có (FX OTC) |
| **Wyckoff** | Điểm **"Sign of Strength" (SOS)** hoặc **"Sign of Weakness" (SOW)** ngay sau khi thoát Accumulation/Distribution — đặc biệt **"Jump Across the Creek"** | Breakaway gap gần như là hình ảnh trực quan của SOS/SOW: một cú bứt phá dứt khoát rời khỏi vùng tích lũy, thường kèm theo test lại "creek" (đường kháng cự/hỗ trợ cũ) mà không rơi trở lại | Wyckoff yêu cầu xác nhận **toàn bộ cấu trúc 4 giai đoạn** phía trước (Accumulation A-B-C-D-E) trước khi tin SOS là thật; ICT có thể gọi breakaway gap chỉ từ hành vi giá tại điểm phá vỡ, không đòi hỏi xác nhận cấu trúc Wyckoff đầy đủ trước đó |
| **Orderflow/Footprint** | **"Absorption tại đỉnh/đáy range rồi initiative trade mạnh xuyên qua"** — delta lệch rất mạnh đúng lúc phá vỡ, không có absorption ngược lại ngay sau đó | Đây là cách xác nhận cấp lệnh gần nhất cho breakaway gap thật: nếu footprint cho thấy delta cùng hướng mạnh SUY GIẢM ngay sau breakout (có absorption ngược), khả năng cao đó là exhaustion, không phải breakaway | Cần dữ liệu tick/volume theo mức giá thật; với FX không có volume sàn tập trung, phải dùng proxy gián tiếp (tốc độ nến, số lần retest thất bại) |

### 14.3 Điều kiện thị trường ảnh hưởng tới độ tin cậy breakaway gap

- **Trending vs ranging:** breakaway gap CHỈ có nghĩa khi xuất hiện ngay sau một giai đoạn tích lũy/ranging rõ ràng (đúng định nghĩa gốc — phá khỏi range). Một "gap" xuất hiện giữa một xu hướng đã chạy dài, không có giai đoạn tích lũy phía trước, gần như chắc chắn là runaway gap hoặc exhaustion gap, không phải breakaway.
- **Volatility regime:** breakaway gap dễ xác nhận hơn trong regime volatility TĂNG dần (từ thấp lên cao) — đây đúng là chữ ký của một đợt bứt phá thật (volatility expansion sau contraction, theo logic Bollinger Band Squeeze cổ điển). Breakaway gap "xuất hiện" trong regime volatility đã cao sẵn và đang giảm dần có tỷ lệ là bẫy cao hơn.
- **Session/giờ giao dịch:** breakaway gap tin cậy nhất khi hình thành trong kill zone chính (London/NY open) với thanh khoản đầy đủ hai chiều để "xác nhận" bằng số lượng giao dịch thật; breakaway gap hình thành trong giờ thanh khoản thấp (phiên Á với cặp không liên quan JPY, giữa đêm NY) dễ bị đảo ngược khi thanh khoản đầy đủ trở lại.
- **Loại tài sản:**
  - **FX majors:** breakaway gap thật (theo đúng định nghĩa "gap" — giá nhảy cóc, chart CFD nối liền) hiếm vì thị trường 24/5; hầu hết "breakaway" trên FX là displacement liên tục không có khoảng trống giá thật, chỉ có ý nghĩa breakaway về hành vi cấu trúc.
  - **Index futures (NQ/ES):** breakaway gap RÕ nhất và dễ đọc nhất — có giờ đóng/mở phiên thật, gap overnight sau tin hoặc breakout kỹ thuật rõ ràng trên daily chart.
  - **Crypto:** khái niệm "gap" theo nghĩa hẹp gần như không tồn tại (24/7, không đóng phiên) — "breakaway" trên crypto thực chất luôn là breakaway MOVE (displacement mạnh phá range), không phải breakaway GAP thật; cần thận trọng khi áp nguyên nghĩa gap classic TA vào crypto.

### 14.4 Bảng so sánh hành vi Breakaway Gap trên 3 loại thị trường

| Đặc điểm | FX majors (EURUSD/GBPUSD) | Index futures (NQ/ES) | Crypto (BTC/ETH) |
|---|---|---|---|
| Tồn tại gap giá thật (khoảng trống OHLC) | Hiếm, chủ yếu weekend/tin sốc | Thường xuyên, đặc biệt overnight/mở phiên | Gần như không (24/7 liên tục) |
| Dạng breakaway phổ biến nhất | Displacement phá range không có khoảng trống giá | Gap qua đêm sau tin + displacement phiên | Displacement phá range (không phải gap giá) |
| Nguồn lực giữ giá chính | NHTW, phá vỡ kỹ thuật đa khung, stop cascade | Dealer gamma hedge, momentum fund, stop cascade | Liquidation cascade, funding rate, momentum bot |
| Tần suất bị nhầm với exhaustion | Trung bình | Thấp-trung bình (dễ đối chiếu volume CME) | Cao (thiếu "gap" thật để phân biệt bằng mắt) |
| Độ tin cậy retest-giữ | Trung bình — spread giãn cuối phiên gây nhiễu | Cao nếu có volume xác nhận rõ | Thấp-trung bình — dễ bị wick xuyên qua do đòn bẩy cao |

## 15. Phản biện & giới hạn (Critique)

### 15.1 Phản biện từ góc nhìn khoa học/quant

1. **Phân loại breakaway vs runaway vs exhaustion chủ yếu là hindsight.** Ba loại gap này được phân biệt bởi VỊ TRÍ trong move (đầu/giữa/cuối) — nhưng vị trí trong move chỉ biết chắc SAU KHI move đã kết thúc. Ngay tại thời điểm gap xuất hiện, không có cách nào chắc chắn 100% đó là "đầu move" — đây là lý do vì sao classic TA thừa nhận rằng phân loại gap luôn có yếu tố nhìn lại.
2. **Confirmation bias khi review lịch sử.** Trader nhớ rõ những breakaway gap đã giữ và tạo trend lớn, quên các trường hợp một "breakaway gap" bị lấp lại hoàn toàn trong vài ngày sau — vì các trường hợp thất bại không đủ ấn tượng để nhớ lâu như các trường hợp thành công lớn.
3. **Không có backtest công khai chuẩn hóa.** Không tồn tại dataset lớn, peer-review, đo tỷ lệ breakaway gap thật sự "không bị lấp" trong N ngày/tuần theo từng loại tài sản và điều kiện thị trường cụ thể.
4. **Unfalsifiable khi thêm điều kiện phân loại.** Nếu một "breakaway gap" bị lấp lại, luôn có lối giải thích retroactive: "vậy ra đó chỉ là runaway gap giữa move" hoặc "đó thực chất là exhaustion, không phải breakaway" — khái niệm tự bảo vệ mình khỏi bị bác bỏ bằng cách đổi tên sau khi biết kết quả.
5. **Overfitting khi thêm bộ lọc displacement-strength.** Ngưỡng "thân nến ≥ 1.5-2x ATR" hay "retest giữ trong N nến" (mục "Nâng cao — Định lượng độ mạnh displacement") là các con số kinh nghiệm được điều chỉnh để khớp với các ví dụ đã biết, không phải suy ra từ một mô hình thống kê độc lập.
6. **Backtest độc lập trái chiều.** Nhiều nguồn phân tích kỹ thuật cổ điển (Edwards & Magee, các trường phái TA khác) có tiêu chí khác nhau về "gap nào là breakaway" — không có sự đồng thuận rộng ngoài mô tả định tính chung.
7. **Giải thích thay thế đơn giản hơn — momentum/trend-following thống kê thuần túy.** Hiện tượng "giá phá vỡ mạnh rồi tiếp tục cùng hướng" hoàn toàn có thể giải thích bằng hiệu ứng momentum đã được ghi nhận rộng rãi trong tài chính định lượng (giá có xu hướng tiếp diễn ngắn-trung hạn sau một cú breakout mạnh, do dòng vốn đuổi theo xu hướng — không cần khái niệm "gap" hay "dealer hedge" cụ thể nào để giải thích hiện tượng tổng quát này).

### 15.2 Phản biện của phản biện

Chấp nhận thẳng: điểm (1), (3), (6) là sự thật không thể chối — phân loại gap luôn có yếu tố nhìn lại, không có dataset chuẩn công khai, và các trường phái TA khác nhau về tiêu chí. Điểm (7) cũng có giá trị lớn: momentum effect là một trong những anomaly được nghiên cứu kỹ nhất và tái lập nhiều lần trong tài chính định lượng — hoàn toàn có thể là phần lớn (hoặc toàn bộ) lời giải thích cho lý do các breakaway gap "giữ được".

Có thể trả lời một phần:
- **Điểm (1) — vị trí trong move chỉ biết sau khi xong — giảm được bằng bối cảnh xác định TRƯỚC lúc gap xảy ra**, không phải sau. Nếu bạn đã xác định "đây là vùng tích lũy/range rõ ràng N ngày" TRƯỚC khi gap xảy ra (ghi lại trong journal với timestamp trước gap), việc gọi gap tiếp theo là "breakaway" không hoàn toàn là hindsight — nó là một dự đoán có điều kiện đã được ghi nhận sẵn, có thể kiểm định đúng/sai sau đó.
- **Điểm (4) — unfalsifiable — thu hẹp được nếu coi định nghĩa là quy tắc cứng, không đổi tên sau khi biết kết quả.** Một quy tắc như "nếu gap giữ qua retest đầu tiên VÀ thân nến tạo gap ≥ 1.5x ATR VÀ xảy ra ngay sau tích lũy ≥ N ngày → coi là breakaway, theo dõi kết quả N ngày tiếp theo" là kiểm định được — miễn là không được phép đổi phân loại sau khi biết diễn biến tiếp theo.
- **Điểm (5) — edge từ vị trí + quản trị rủi ro, không từ tiên đoán chắc chắn.** Kể cả khi thừa nhận momentum effect (điểm 7) là cơ chế nền, breakaway gap vẫn cho một cấu trúc entry cụ thể: SL logic (far side gap) + target logic (draw on liquidity tiếp theo) — cấu trúc R:R này có giá trị thực hành độc lập với việc "vì sao" giá tiếp tục đi, miễn là tỷ lệ thắng đủ để bù trừ.

### 15.3 Giới hạn cứng phải chấp nhận (≥5)

1. **Không thể phân biệt chắc chắn breakaway/runaway/exhaustion tại THỜI ĐIỂM gap xảy ra** — chỉ có thể gán xác suất dựa trên bối cảnh (vị trí trong move, độ dài tích lũy trước đó, độ mạnh displacement), không có cách xác nhận 100% real-time.
2. **Không có ngưỡng ATR/volume universal** cho "thế nào là displacement đủ mạnh để gọi breakaway" — mọi số trong note này là heuristic riêng theo loại tài sản, có thể trôi theo thời gian.
3. **Với FX/crypto, khái niệm "gap giá thật" gần như không áp dụng được theo nghĩa hẹp** (thị trường liên tục), buộc phải dùng phiên bản "breakaway MOVE" thay thế — làm giảm độ chính xác của toàn bộ khung lý thuyết gap cổ điển (được xây cho thị trường có giờ đóng/mở rõ, như cổ phiếu/futures).
4. **Không tự backtest hóa hoàn toàn được bằng thuật toán đơn giản** — phân loại đòi hỏi đánh giá "vị trí trong move" và "độ dài tích lũy trước đó", cả hai đều cần một mức độ diễn giải cấu trúc thị trường không hoàn toàn cơ giới hóa được.
5. **Retest-giữ không đảm bảo move tiếp diễn xa** — nhiều breakaway gap giữ qua 1-2 lần retest đầu nhưng vẫn thất bại sau đó vài ngày khi gặp một nguồn cung/cầu lớn hơn ở khung thời gian cao hơn; "giữ retest" chỉ là điều kiện cần, không phải điều kiện đủ.
6. **Chi phí giao dịch/slippage đặc biệt cao ngay tại điểm breakout** — nếu cố gắng vào lệnh ngay lúc gap hình thành (không chờ retest), slippage và spread giãn trong giai đoạn biến động cao nhất làm giảm đáng kể R:R thực tế so với lý thuyết.

> [!quote] Kết luận trung thực
> Breakaway Gap là một khung phân loại hữu ích để đọc "giai đoạn nào của một move đang diễn ra" và đặt cấu trúc SL/target hợp lý dựa trên vị trí đó — nhưng bản chất phân loại luôn có yếu tố nhìn lại, và phần lớn lý do các gap này "giữ được" có thể quy về hiệu ứng momentum thống kê đã được nghiên cứu rộng, không nhất thiết cần một cơ chế "ICT" riêng biệt. Giá trị thực hành nằm ở việc buộc bạn xác định bối cảnh (tích lũy trước đó, độ mạnh displacement) TRƯỚC khi gọi tên gap, và ở cấu trúc quản trị rủi ro rõ ràng đi kèm — không nằm ở khả năng tiên đoán chắc chắn liệu một gap cụ thể sẽ giữ hay bị lấp.

## 16. Edge Cases thực chiến

![[BreakawayGap-Edge-Cases.svg|720]]
*Minh họa hai edge case đắt giá nhất: breakaway gap thật vs common gap nhìn giống nhau real-time (trái), và Monday gap bị squaring Friday khiến giá quay đầu ngay sau breakout (phải).*

### 16.1 Phân biệt Breakaway Gap vs Common Gap trong REAL-TIME — không có hindsight để dựa vào

Đây là bài toán khó nhất và thực tế nhất: ngay tại thời điểm gap vừa hình thành, breakaway gap và common gap (gap thường, không có ý nghĩa cấu trúc, thường bị lấp nhanh) trông **giống nhau 100% về hình dạng OHLC**. Sự khác biệt chỉ lộ ra sau vài giờ đến vài ngày.

**Vì sao bẫy được cả trader có kinh nghiệm:** không có chỉ báo nào trên chart tại thời điểm t=0 nói cho bạn biết "đây là breakaway". Cảm giác tự tin ("nhìn mạnh quá, chắc là breakaway") thường chỉ là phản ứng với ĐỘ MẠNH của nến, không phải bằng chứng cấu trúc thật.

**Cách nhận diện sớm (bộ 4 tiêu chí real-time, không cần chờ hindsight):**
1. **Vị trí trước gap:** có một giai đoạn tích lũy/range rõ ràng ≥ 10-15 nến trên khung đang xét ngay trước gap không? Common gap thường xảy ra giữa một xu hướng đã chạy, không phải từ range.
2. **Volume/tốc độ displacement so với 20 nến gần nhất:** breakaway gap thật đi kèm volume hoặc tốc độ di chuyển vượt trội rõ rệt (không chỉ "hơi lớn hơn bình thường").
3. **Phản ứng tại lần retest ĐẦU TIÊN:** nếu giá quay lại test biên gap và bật lại NGAY (trong 1-3 nến, không xuyên sâu quá 50% gap), xác suất breakaway tăng lên đáng kể; nếu giá xuyên thẳng qua và lấp >70% gap ngay lần đầu, xác suất cao đó là common gap.
4. **Đối chiếu draw on liquidity HTF:** breakaway gap thật thường đi cùng hướng với một target thanh khoản rõ ràng ở khung cao hơn; common gap không có "lý do" draw on liquidity đi kèm.

**Cách xử lý:** không gọi tên gap ngay khi nó xuất hiện — chờ tín hiệu retest đầu tiên (tiêu chí 3) trước khi coi đó là breakaway đủ tin cậy để tăng size; với entry sớm (trước khi có xác nhận retest), giảm size và đặt SL chặt hơn để bù trừ rủi ro "gọi sai tên".

### 16.2 Weekend gap / Monday gap bị Friday squaring "giả trang" thành breakaway

Thứ Sáu cuối phiên, nhiều trader/quỹ đóng vị thế trước cuối tuần (position squaring) tạo một cú di chuyển mạnh cuối phiên KHÔNG liên quan gì đến dòng tiền định hướng thật — chỉ là chốt lời/cắt lỗ kỹ thuật trước khi thị trường đóng 2 ngày. Nếu giá mở cửa thứ Hai gap tiếp theo hướng đó, nhìn tổng thể (đóng cửa thứ Sáu → mở thứ Hai) rất giống một breakaway gap thật.

**Vì sao bẫy được cả trader có kinh nghiệm:** khoảng cách giá qua 2.5 ngày nghỉ luôn "trông to" so với biến động nến bình thường — dễ nhầm độ lớn tuyệt đối này với độ mạnh của một breakaway thật.

**Cách nhận diện sớm:** kiểm tra riêng phần di chuyển TRONG giờ thứ Sáu (không tính phần gap qua đêm cuối tuần) — nếu phần lớn "sức mạnh" chỉ nằm ở khoảng gap cuối tuần (không giao dịch), không phải ở displacement thật trong giờ giao dịch, độ tin cậy breakaway giảm.

**Cách xử lý:** chờ ít nhất nửa phiên thứ Hai (London hoặc NY mở) để xem dòng tiền thật có tiếp tục xác nhận hướng đi hay không, trước khi coi weekend/Monday gap là breakaway đáng trade.

### 16.3 Futures gap phiên (CME halt) bị nhầm thành breakaway trên chart CFD nối liền

Tương tự Liquidity Void edge case 16.2, nhưng áp riêng cho breakaway gap: khoảng dừng maintenance break CME (~17:00-18:00 ET) đôi khi tạo một khoảng lệch giá nhỏ giữa đóng/mở phiên trên NQ/ES futures thật; trên CFD nối liền không hiển thị break này, khoảng lệch bị hiểu lầm là một breakaway gap phiên thật.

**Vì sao bẫy được cả trader có kinh nghiệm:** không phải trader nào cũng theo dõi đúng giờ maintenance break hàng ngày — dễ quên vì nó lặp lại mỗi ngày và ít gây chú ý như weekend gap.

**Cách nhận diện sớm:** đối chiếu giờ hình thành gap với bảng giờ maintenance break CME chuẩn; nếu trùng khớp, hạ độ tin cậy.

**Cách xử lý:** ưu tiên xác nhận trên feed futures thật (không nối liền qua maintenance break) trước khi coi một "gap phiên" là breakaway có ý nghĩa cấu trúc.

### 16.4 Breakaway gap hình thành đúng lúc nến tin (NFP/FOMC) — độ mạnh displacement bị "lạm phát" giả

Một nến tin lớn tạo displacement rất mạnh có thể trông giống breakaway gap hoàn hảo về mặt độ lớn (thân nến gấp 3-5x ATR), nhưng phần lớn độ mạnh này đến từ volatility bùng nổ tức thời do tin, không phải từ một dòng tiền định hướng bền vững theo đúng cơ chế mục 14.1 (dealer hedge + stop cascade + momentum fund).

**Vì sao bẫy được cả trader có kinh nghiệm:** tiêu chí "displacement ≥ 1.5-2x ATR" (mục "Nâng cao — Định lượng độ mạnh displacement") dễ bị thỏa mãn giả bởi bất kỳ nến tin lớn nào, không phân biệt được nguồn gốc của độ mạnh đó.

**Cách nhận diện sớm:** kiểm tra timestamp — nếu displacement xảy ra trong 1-5 phút đầu sau một mốc tin lớn đã biết trước, cần thêm điều kiện xác nhận độc lập (retest giữ, tiếp diễn sau khi volatility ổn định lại) trước khi tin đây là breakaway thật.

**Cách xử lý:** với gap hình thành trong nến tin, chờ ít nhất 30-60 phút và một lần retest xác nhận trước khi coi là breakaway đủ tin cậy để trade theo, tương tự nguyên tắc ở Liquidity Void edge case 16.3 nhưng áp dụng riêng cho ngữ cảnh phân loại gap.

### 16.5 Data feed khác nhau — breakaway gap hiện trên biểu đồ này, biến mất trên biểu đồ kia

Một breakaway gap rõ ràng trên NAS100 (CFD, giờ server broker riêng) có thể không tồn tại dưới dạng "gap giá" thật trên NQ futures (CME) tại cùng khung giờ, vì giờ đóng/mở nến hai bên lệch nhau.

**Vì sao bẫy được cả trader có kinh nghiệm:** giả định "hai chart theo cùng chỉ số phải giống nhau" là trực giác hợp lý nhưng sai với cấu trúc gap cụ thể — độ lệch giờ nhỏ đủ để một feed có gap và feed khác không có.

**Cách nhận diện sớm:** đối chiếu gap nghi vấn trên ít nhất 2 feed độc lập trước khi tin, đặc biệt với gap nhỏ-trung bình (khác biệt dễ xảy ra hơn với gap lớn rõ ràng).

**Cách xử lý:** backtest và trade live trên cùng một feed nhất quán; với gap chỉ tồn tại trên 1 trong 2 feed, hạ độ tin cậy xuống mức "cần xác nhận thêm bằng displacement thật, không dựa vào bản thân gap".

### 16.6 Nested breakaway HTF/LTF xung đột — breakaway H4 đúng nhưng M15 tạo breakaway ngược ngay sau đó

Một breakaway gap H4 hình thành đúng chuẩn (tích lũy trước, displacement mạnh, retest giữ) — nhưng ngay sau đó, trên M15, một pullback sâu tạo ra chính một "breakaway gap" M15 NGƯỢC hướng (đủ mạnh theo tiêu chí M15 riêng). Trader chỉ nhìn M15 dễ vào lệnh ngược hướng H4 đúng lúc breakaway H4 vẫn còn hiệu lực.

**Vì sao bẫy được cả trader có kinh nghiệm:** mỗi khung thời gian có ATR/tiêu chí riêng — một move đủ mạnh để "breakaway" trên M15 hoàn toàn có thể chỉ là một pullback bình thường trên H4, và ngược lại; không kiểm tra chéo khung dễ dẫn tới lẫn lộn.

**Cách nhận diện sớm:** luôn xác định breakaway ở khung HTF trước, sau đó dùng LTF chỉ để tìm entry ĐI CÙNG HƯỚNG HTF, không dùng LTF độc lập để phân loại gap mới ngược hướng.

**Cách xử lý:** nếu LTF tạo breakaway ngược hướng HTF, coi đó là tín hiệu retest/pullback tự nhiên trong bối cảnh HTF (cơ hội entry theo hướng HTF khi pullback hoàn tất), không phải tín hiệu đảo hướng, trừ khi có MSS HTF thật đi kèm.

### 16.7 Partial fill/wick xuyên gap trên tài sản đòn bẩy cao (crypto) — "giữ retest" giả do wick, không do thân nến

Trên BTCUSD, một breakaway move (không phải gap giá thật, theo mục 14.3) sau đó bị một wick dài xuyên sâu vào vùng gap cũ (do một lệnh thanh lý đơn lẻ hoặc lệnh lớn tức thời), rồi giá bật lại ngay trong cùng nến hoặc nến kế tiếp. Nhìn qua có vẻ "giữ retest tốt", nhưng thân nến đóng cửa mới là thứ quyết định, không phải wick.

**Vì sao bẫy được cả trader có kinh nghiệm:** với volatility cao của crypto, wick dài xảy ra thường xuyên và dễ được diễn giải theo hướng có lợi cho thiên kiến sẵn có (nếu đang long, thấy wick xuyên rồi bật lại là "xác nhận giữ"; logic này dễ bị đảo ngược khi wick không bật lại).

**Cách nhận diện sớm:** đo % thân nến (không phải wick) còn nằm ngoài vùng gap cũ khi nến đóng — nếu thân đóng vẫn giữ ngoài gap dù wick xuyên sâu, đó là giữ retest thật; nếu thân đóng bên trong gap, đó là dấu hiệu yếu dù wick "nhìn đẹp".

**Cách xử lý:** luôn chờ nến đóng đầy đủ trước khi đánh giá retest giữ hay không trên tài sản đòn bẩy cao/volatility cao; không đánh giá dựa trên giá tức thời giữa nến.

## 17. Case Studies chuyên sâu

![[BreakawayGap-Case-Study.svg|720]]
*Case Study đại diện: USDJPY Long 05/03/2026 — breakaway gap sau BoJ, entry tại retest, TP tại draw on liquidity H4, kết quả +3.1R.*

### 17.1 Case Study — USDJPY Long 05/03/2026: breakaway gap sau phát biểu BoJ, win-by-the-book, +3.1R

> [!example] Bối cảnh HTF
> USDJPY, thứ Năm 05/03/2026. D1 vừa trải qua 3 tuần tích lũy trong dải 148.50-150.20 (range rõ, đã test biên trên/dưới nhiều lần). Bias D1 chuyển bullish sau khi phát biểu bất ngờ của BoJ (giữ nguyên lãi suất, ngôn ngữ ôn hòa hơn kỳ vọng) lúc 23:30 EST tối thứ Tư.

**Setup:** Ngay sau phát biểu, USDJPY gap từ 150.10 (đóng cửa) lên 150.85 khi mở phiên Á (thứ Năm), kèm một nến displacement H1 đầu tiên đóng tại 151.20 — thân nến 110 pip, gấp 3.4x ATR H1 nền (~32 pip). Gap này thỏa cả 4 tiêu chí real-time ở mục 16.1: tích lũy 3 tuần trước đó rõ ràng, displacement vượt trội, và ngay sau đó có một draw on liquidity rõ ràng ở 152.40 (equal highs tháng 1).

**Diễn biến & execution:**
- 09:00 JST (phiên Á) — giá pullback về test biên gap tại 150.10-150.30, giữ trên 150.10 (retest đầu tiên, thân nến không đóng dưới biên gap — xác nhận tiêu chí 3 ở mục 16.1).
- 09:45 JST — nến H1 tiếp theo đóng tại 150.65, xác nhận MSS nhỏ LTF.
- 09:46 — entry Long tại 150.35 (gần CE của gap). SL đặt dưới far side gap = 149.95 (40 pip rủi ro, ~$400/lot chuẩn 100k).
- 12:00-18:00 JST — giá tiếp diễn tăng ổn định qua phiên London, không có pullback sâu.
- 20:15 EST (phiên NY) — giá chạm 152.40, quét equal highs tháng 1, TP khớp.

**Kết quả bằng số:** rủi ro 40 pip, lợi nhuận chốt 205 pip (150.35 → 152.40) → R-multiple lý thuyết +5.1R; sau trừ spread thực tế và 1 pip slippage mỗi chiều, R thực = **+3.1R** (chốt một phần tại 151.80 do thận trọng trước cuối phiên NY, không giữ full size tới đúng 152.40).

**Bài học riêng:** breakaway gap sau phát biểu NHTW bất ngờ (không phải theo lịch kinh tế chuẩn) vẫn có thể trade được — khác với edge case 16.4 (gap trong nến tin CÓ LỊCH TRƯỚC, cần chờ ổn định) — vì phát biểu bất ngờ ngoài giờ giao dịch chính (23:30 EST) cho thời gian "hấp thụ" tự nhiên qua đêm trước khi phiên Á/London xác nhận bằng retest.

---

### 17.2 Case Study — ES Short 18/03/2026: breakaway gap "đẹp như sách" nhưng THUA — bị nhầm exhaustion, -1.3R

> [!example] Bối cảnh HTF
> ES (S&P 500 futures), thứ Tư 18/03/2026. Thị trường đã giảm liên tục 9 phiên trước đó (downtrend dài, không có giai đoạn tích lũy rõ ràng ngay trước — đây là chi tiết quan trọng bị bỏ qua khi vào lệnh).

**Setup:** Một nến displacement giảm mạnh lúc mở phiên NY (09:30 EST) tạo gap từ 5120 xuống 5085 (35 điểm, 2.9x ATR nền ~12 điểm), kèm tin CPI cao hơn kỳ vọng. Trader đọc đây là breakaway gap tiếp diễn downtrend, vào Short ngay tại retest đầu tiên (giá hồi lên 5100, giữ dưới 5120 — nhìn giống "giữ retest tốt" theo tiêu chí 3 ở mục 16.1).

**Diễn biến & execution:**
- 09:52 — entry Short tại 5100 (retest). SL trên far side gap = 5125 (25 điểm rủi ro, $1250/lot ở $50/điểm).
- 10:15-11:00 — giá tiếp tục giảm nhẹ tới 5075, có vẻ đúng hướng.
- 11:30 — giá bắt đầu đảo mạnh, tăng liên tục không dừng, xuyên ngược qua toàn bộ gap.
- 13:00 — giá chạm 5125, SL bị quét — hóa ra đây là **exhaustion gap** (cú giảm cuối cùng của downtrend 9 phiên, không phải khởi đầu move mới): không có giai đoạn tích lũy trước gap (vi phạm điều kiện 1 ở mục 16.1), và displacement chỉ là "momentum cuối" của một xu hướng đã chạy dài — chính xác dạng bẫy mô tả ở mục 14.1 (không có dealer hedge mới hay stop cascade tiếp sức, chỉ còn FOMO sellers cuối chu kỳ).

**Kết quả bằng số:** -25 điểm → -1.0R theo rủi ro gốc; sau slippage khớp lệnh giờ biến động cao, thực tế **-1.3R**.

**Bài học riêng:** điều kiện "tích lũy rõ ràng trước gap" (tiêu chí 1, mục 16.1) không phải là chi tiết phụ — nó là bộ lọc quan trọng nhất để loại các gap xảy ra giữa/cuối một move dài (khả năng cao là runaway hoặc exhaustion). Bỏ qua nó chỉ vì "giữ retest tốt" (thỏa 1/4 tiêu chí) là không đủ.

---

### 17.3 Case Study — Skip trade đúng — GBPJPY 02/04/2026: gap không rõ nguồn gốc, thiếu draw on liquidity hợp lý

> [!example] Bối cảnh HTF
> GBPJPY, thứ Năm 02/04/2026. D1 sideway rộng 190.00-193.50 hơn 1 tháng, không có bias rõ.

**Tình huống:** Một nến H1 displacement tăng mạnh (191.20 → 192.80, gấp 2.1x ATR H1 nền) xuất hiện lúc phiên Á, không có tin liên quan trực tiếp GBP hoặc JPY trong lịch kinh tế, không rõ nguồn (có thể chỉ là thanh khoản mỏng phiên Á khuếch đại một lệnh trung bình thành displacement lớn). Giá giữ trên biên dưới của gap khi retest — thỏa tiêu chí 3 ở mục 16.1.

**Vì sao skip:** (1) không có draw on liquidity rõ ràng ở phía trên (không có equal highs/cụm thanh khoản sạch nào trong vùng 193.00-195.00 để làm target hợp lý — vi phạm tiêu chí 4 ở mục 16.1); (2) D1 bias không rõ, sideway kéo dài không cho cơ sở gán hướng ưu tiên; (3) thanh khoản phiên Á thấp làm độ tin cậy của "displacement mạnh" giảm — biến động 2.1x ATR trong phiên Á GBPJPY (cặp cross ít thanh khoản phiên Á) dễ là nhiễu hơn là dòng tiền định hướng thật.

**Quyết định:** không vào lệnh. Theo dõi thêm — giá dao động trong vùng 191.50-193.00 suốt 2 ngày tiếp theo, không tiếp diễn tăng rõ ràng, cuối cùng quay lại lấp gần hết gap vào ngày thứ 3.

**Kết quả:** 0R, tránh được một lệnh có setup nhìn hợp lệ về hình thức (displacement + giữ retest) nhưng thiếu 2/4 tiêu chí quan trọng (draw on liquidity + bối cảnh bias rõ).

**Bài học riêng:** displacement mạnh + giữ retest chỉ là 2/4 điều kiện — thiếu draw on liquidity rõ ràng và bias HTF, một breakaway gap "đúng hình thức" vẫn không đáng trade vì không có lý do để kỳ vọng move tiếp diễn XA.

---

### 17.4 Case Study — ETHUSD Short 27/04/2026 (liquidation cascade ngược — breakaway giả): khác asset class, LOSS có kiểm soát -0.8R

> [!example] Bối cảnh HTF
> ETHUSD, Chủ Nhật 27/04/2026, 14:00 UTC. D1 bias bullish nhẹ (uptrend 2 tuần), nhưng open interest futures ETH đang ở mức cao bất thường với funding rate dương liên tục 5 ngày.

**Setup:** Giá break qua kháng cự kỹ thuật 3450 với một nến H1 rất mạnh (3420 → 3510, gấp 3x ATR nền), nhìn giống breakaway gap/move hoàn hảo tiếp diễn uptrend — có vẻ thỏa cả 4 tiêu chí (tích lũy trước dưới 3450 rõ, displacement mạnh, draw on liquidity ở 3650 phía trên).

**Diễn biến & execution:**
- Trader (góc nhìn ngược, contrarian) nhận thấy funding rate cao bất thường trước breakout — dấu hiệu long leverage quá tải tương tự case study Liquidity Void 17.4 (BTCUSD cascade) — và đặt giả thuyết: breakout này có thể là "stop-hunt" kích hoạt short liquidation trước, không phải breakaway thật, vì phần lớn lực đẩy có thể chỉ là short bị stop, không phải dòng tiền mới.
- 14:20 — vào Short thử nghiệm size nhỏ (0.3R chuẩn) tại 3505, ngay sau khi displacement chậm lại, với giả thuyết đảo chiều do quá tải long.
- 14:20 — SL đặt trên đỉnh nến displacement = 3525 (20 USD rủi ro trên size chuẩn).
- 15:00-16:30 — giá tiếp tục tăng chậm lên 3540 rồi mới thực sự đảo, nhưng đã chạm SL 3525 trước khi đảo — hóa ra breakout NÀY là breakaway thật (short bị stop chỉ là MỘT PHẦN lực đẩy, không phải toàn bộ; có dòng tiền mới thật tham gia sau đó theo đúng cơ chế momentum-chasing ở mục 14.1).
- SL bị quét lúc 16:15.

**Kết quả bằng số:** -20 USD trên size 0.3R chuẩn → **-0.8R** tính trên rủi ro chuẩn đầy đủ (vì vào size giảm chủ động, tổng thiệt hại tuyệt đối nhỏ hơn một lệnh full-size, nhưng vẫn ghi nhận đúng theo R chuẩn để không làm sai lệch thống kê cá nhân).

**Bài học riêng:** funding rate cao là tín hiệu CẢNH BÁO rủi ro đảo chiều, không phải xác nhận đảo chiều sẽ xảy ra ngay — nó chỉ nói "có nhiều nhiên liệu cho một cú squeeze nếu xảy ra", không nói "khi nào" hoặc "có xảy ra không". Trade ngược một breakaway gap dựa thuần trên funding rate mà không có xác nhận cấu trúc giá (MSS ngược hướng thật) là đặt cửa vào một giả thuyết chưa được giá xác nhận — đúng là bài học ngược với case Liquidity Void 17.4 nơi funding rate + cascade ĐÃ xác nhận bằng giá thật trước khi entry.

## 18. Tình huống thực chiến (War Stories)

> [!quote] W1 — Gọi tên "breakaway" quá sớm vì nến "nhìn mạnh"
> Tôi từng thấy một nến H1 GBPUSD thân dài gấp 3 lần nến trung bình, ngay lập tức gọi nó là breakaway gap và vào lệnh theo hướng đó mà không kiểm tra xem có giai đoạn tích lũy rõ ràng trước đó không. Hóa ra đó là nến giữa của một move đã chạy 6 nến trước — bản chất là runaway gap, và ngay sau lệnh của tôi, giá đảo ngược mạnh (đúng kiểu exhaustion). Từ sau lần đó, câu hỏi đầu tiên tôi tự hỏi trước khi gọi tên bất kỳ gap nào không phải "nến này mạnh không" mà là "có tích lũy rõ ràng ngay trước nó không".

> [!quote] W2 — Đuổi theo gap ngay lúc tin ra, không chờ retest
> NFP ra số bất ngờ, EURUSD gap mạnh, tôi vào market ngay trong 30 giây đầu vì sợ lỡ sóng. Bị khớp lệch giá 8 pip so với giá nhìn thấy trên chart lúc quyết định vào lệnh, và 5 phút sau giá giật ngược đủ để chạm SL đặt quá gần. Bài học không mới nhưng luôn phải nhắc lại: displacement trong 1-5 phút đầu sau tin lớn không phải lúc để đuổi giá bằng market order — chờ retest là kỷ luật, không phải sự chậm chạp.

> [!quote] W3 — Tự thuyết phục bản thân "giữ retest" khi thực ra chỉ là wick
> Trên BTCUSD, tôi thấy giá wick xuyên qua vùng breakaway move cũ rồi bật lại ngay trong nến, và vội vàng coi đó là "giữ retest hoàn hảo" để add thêm vị thế. Vấn đề: thân nến đóng cửa thực ra nằm NGAY TRONG vùng gap, chỉ có wick là bật lại — tôi đã nhìn cái mình muốn thấy chứ không nhìn dữ liệu thật. Vị thế add thêm đó bị stop trong nến tiếp theo. Giờ tôi luôn chờ nến đóng đầy đủ và nhìn thân nến, không nhìn wick, trước khi quyết định retest có giữ hay không — đặc biệt trên tài sản biến động cao như crypto.
