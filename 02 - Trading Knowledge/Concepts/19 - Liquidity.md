---
type: ict-concept
concept: Liquidity
aliases:
  - ICT Liquidity
  - Draw on Liquidity
  - Liquidity Pools
tags:
  - trading/ict/concept
  - trading/study
  - "#Liquidity"
status: developing
category: Liquidity
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[Trading Journal/02 - Trading Knowledge/Models/ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-03
common_mistakes:
  - "[[Mistake - Entry Before Liquidity Sweep]]"
  - "[[Mistake - Wrong Draw on Liquidity]]"
  - "[[Mistake - Confusing Liquidity with Imbalance]]"
---
#Liquidity
# Liquidity

> [!summary] Tóm tắt 1 câu
> **Liquidity là các cụm lệnh chờ (resting orders: stop loss + lệnh breakout/pending) nằm trên đỉnh và dưới đáy mà thị trường — vận hành như một thuật toán — bị "hút" tới (draw on liquidity) để fill khối lượng lớn của smart money rồi phân phối / đảo chiều.**

> [!important] Nguyên tắc cốt lõi
> **Trước khi nghĩ tới entry, phải trả lời được: "Liquidity nào là draw chính mà giá đang hướng tới?"**  
> Liquidity là nhiên liệu của price delivery; sweep liquidity gần như luôn xảy ra TRƯỚC một reversal có chất lượng — không bao giờ vào lệnh khi liquidity đối diện entry chưa được lấy.

---

## 1. Định nghĩa

![[Liquidity-Sec-01-Dinh-Nghia.svg|720]]
*Sơ đồ: Liquidity là các pool lệnh chờ (BSL trên đỉnh, SSL dưới đáy) — nơi giá bị hút về để lấy "nhiên liệu".*

**Khái niệm:**  
Liquidity trong ICT là **các cụm lệnh chờ tồn tại sẵn trên thị trường** mà giá cần chạm tới để khớp được khối lượng lớn. Mỗi stop loss đặt trên một đỉnh là một lệnh thị trường (buy) ngủ đông; mỗi stop loss đặt dưới một đáy là một lệnh thị trường (sell) ngủ đông. Smart money không thể fill khối lượng lớn ở vùng "không có ai bán" hay "không có ai mua", nên thị trường được điều hướng (engineered) về các cụm lệnh này. Vì vậy ICT mô tả thị trường vận hành **như một thuật toán** đi từ pool liquidity này sang pool liquidity kia, chứ không "ngẫu nhiên" theo cung-cầu thuần.

**Mục đích trong ICT:**
- Xác định **draw on liquidity** — nơi giá có xác suất cao hướng tới làm mục tiêu (target / điểm phân phối).
- Giải thích vì sao giá "đột nhiên" đảo chiều ngay sau khi phá một đỉnh/đáy rõ ràng (đó là sweep, không phải breakout thật).
- Đặt nền cho [[12 - Daily Bias]]: bias chính là việc chọn phía liquidity (buy-side hay sell-side) sẽ là draw chính trong ngày.
- Định vị target hợp lý cho lệnh: TP đặt quanh liquidity còn mở, không phải số pip tùy ý.
- Phân biệt nơi smart money **gom lệnh** (liquidity pool) với nơi smart money **đẩy giá nhanh** (imbalance / liquidity void).

**Vì sao khái niệm này quan trọng:**  
Liquidity là **khái niệm nền tảng nhất** của toàn bộ phương pháp ICT — mọi concept khác (FVG, OB, MSS, premium/discount, dealing range) chỉ là công cụ phục vụ một câu hỏi duy nhất: *giá đang đi lấy liquidity nào?* Không hiểu liquidity, trader sẽ chase breakout đúng vào điểm sweep, đặt stop loss đúng nơi market muốn quét, và đặt target ở chỗ không có lệnh để giá tới.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đang bị **hút** về phía nào — buy-side phía trên hay sell-side phía dưới?
- Pool liquidity nào quan trọng nhất (draw chính) và pool nào chỉ là thứ yếu?
- Đỉnh/đáy này là **target để giá lấy** hay là **mức để giá tôn trọng**?
- Giá vừa **sweep** liquidity (chuẩn bị reversal) hay đang **break-and-go** (tiếp diễn)?
- Vùng này là liquidity (pool lệnh) hay liquidity void/imbalance (vùng cần rebalance)?

### Liquidity không phải là gì
- Không phải "volume cao / nhiều giao dịch" theo nghĩa cổ điển — ICT nói về **cụm lệnh chờ tại price level**, không phải traded volume.
- Không phải [[Fair Value Gap]] hay imbalance — FVG/void là vùng giá đi nhanh **thiếu** giao dịch (cần rebalance), KHÔNG phải pool lệnh.
- Không phải tín hiệu vào lệnh: nhìn thấy equal highs không có nghĩa là "Short ngay"; nó chỉ là **target** mà giá có thể hướng tới.
- Không phải breakout đáng đu theo: phá qua liquidity pool rất thường là sweep rồi đảo chiều.
- Không phải thứ chỉ tồn tại trên một timeframe: liquidity có cấp độ HTF (PWH/PWL) tới LTF (session high/low, M5 swing).

---

## 2. Bối cảnh sử dụng

![[Liquidity-Sec-02-Boi-Canh.svg|720]]
*Sơ đồ: Bối cảnh dùng liquidity — xác định draw on liquidity và pool cần sweep trước khi tìm entry.*

### Hai phía liquidity cần luôn nhận diện

| Phía | Tên | Vị trí | Loại lệnh nằm ở đó | Khi nào trở thành draw |
|---|---|---|---|---|
| **Phía trên** | [[07 - Buy-side Liquidity]] (BSL) | Trên old highs, equal/relative equal highs, swing highs, đường trendline | Buy stops của người bán khống (stop loss) + buy stop của breakout traders | Khi [[12 - Daily Bias]] bullish, hoặc khi market cần lấy BSL trước khi đảo xuống |
| **Phía dưới** | [[30 - Sell-side Liquidity]] (SSL) | Dưới old lows, equal lows, swing lows | Sell stops của người mua (stop loss) + sell stop breakout | Khi bias bearish, hoặc khi market cần lấy SSL trước khi đảo lên |

> [!tip]
> **BSL nằm phía TRÊN, SSL nằm phía DƯỚI.** Mẹo nhớ: để fill một lệnh *buy* lớn, market phải tìm tới nơi có nhiều *buy orders* chờ kích hoạt — đó là **trên** các đỉnh. Ngược lại với *sell*.

### Phân loại liquidity pool theo cấp độ

| Cấp độ | Pool tiêu biểu | Ý nghĩa thực chiến |
|---|---|---|
| **HTF / Daily reference** | PDH / PDL (Previous Day High/Low), PWH / PWL (Previous Week High/Low) | Draw mạnh nhất; thường là target chính trong ngày/tuần |
| **Session** | Asia high/low, London high/low, NY high/low | Liquidity sinh ra trong từng phiên; London thường sweep Asia, NY thường sweep London |
| **Engineered** | Equal highs / equal lows, relative equal highs/lows | Liquidity "được tạo ra" để dụ trader; mục tiêu rất hấp dẫn (xem mục dưới) |
| **Structural** | Old high/low, swing high/low, trendline liquidity | Stop loss tự nhiên của trader; pool cổ điển nhất |

### Internal vs External range liquidity

| Loại | Định nghĩa | Ví dụ thành phần | Vai trò |
|---|---|---|---|
| **External range liquidity** | Liquidity tại **đỉnh / đáy của dealing range** | BSL trên range high, SSL dưới range low | Là draw "lớn" — nơi range mở rộng để lấy |
| **Internal range liquidity** | Liquidity **bên trong** range | [[Fair Value Gap]], [[Order Block]], breaker, mitigation block nằm giữa range | Là nơi giá retrace tới trước khi đi lấy external liquidity |

> [!note]
> Quy luật ICT cổ điển: giá thường dao động **từ external → internal → external**. Sau khi lấy một external liquidity (vd BSL trên range high), giá quay vào lấy internal liquidity (vd FVG bên trong), rồi mới đi tới external liquidity phía đối diện.

### Engineered liquidity / stop hunt

Equal highs / equal lows hiếm khi xuất hiện "tình cờ". Khi giá tạo ra hai-ba đỉnh ngang bằng nhau, đám đông trader đặt **stop loss ngay phía trên** (vì nghĩ "đỉnh đôi/đỉnh ba = kháng cự mạnh"). Cụm stop đó trở thành một pool liquidity **được điều hướng (engineered)** — một mục tiêu cực kỳ hấp dẫn để smart money quét trước khi đảo chiều. Equal lows hoạt động đối xứng ở phía dưới.

> [!tip]
> Càng "đẹp", càng "rõ ràng", càng "ai cũng thấy" thì equal highs/lows càng dễ bị lấy. Đỉnh đôi sách giáo khoa thường là **liquidity được dọn sẵn**, không phải vùng đảo chiều an toàn.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có pool liquidity rõ ràng và chưa bị lấy (PDH/PDL, PWH/PWL, equal highs/lows, session high/low).
- [ ] Xác định được draw on liquidity **chính**, phân biệt với pool thứ yếu.
- [ ] Pool liquidity phù hợp với hướng [[12 - Daily Bias]] và vị trí [[27 - Premium Discount]].
- [ ] Có engineered liquidity (equal highs/lows) hình thành đúng phía draw.
- [ ] Giá đang tiến tới một external liquidity rõ ràng còn nhiều room cho R:R.

### Khi nào nên bỏ qua?
- [ ] Liquidity hai phía đều gần và không rõ phía nào là draw chính.
- [ ] Draw chính đã bị lấy xong và chưa có pool mới hình thành.
- [ ] Giá ở giữa range, không gần external liquidity nào.
- [ ] "Pool" thực ra là một imbalance / liquidity void chứ không phải cụm lệnh.
- [ ] Đường tới target bị chặn bởi một liquidity gần hơn chưa xử lý (room thực tế hẹp).

---

## 3. Cấu trúc nhận diện trên chart

![[Liquidity-Sec-03-Nhan-Dien.svg|720]]
*Sơ đồ: Nhận diện các loại pool liquidity trên chart — equal highs/lows, PDH/PDL, swing, trendline.*

### Dấu hiệu chính
1. **Đỉnh/đáy rõ ràng có nhiều người nhìn thấy:** swing high/low quan trọng, PDH/PDL, PWH/PWL — nơi stop loss tự nhiên dồn lại.
2. **Equal highs / equal lows:** hai hoặc nhiều đỉnh (đáy) gần ngang bằng → engineered liquidity, target hấp dẫn.
3. **Trendline liquidity:** chuỗi higher lows (hoặc lower highs) tạo trendline; stop của breakout/trend trader nằm dọc theo nó.
4. **Session reference:** Asia range high/low, London high/low — pool sinh ra theo cấu trúc thời gian.
5. **Vị trí so với dealing range:** pool nằm ở external (đỉnh/đáy range) hay internal (giữa range)?

### Ma trận nhận diện liquidity

| Thành phần | Buy-side Liquidity (BSL) | Sell-side Liquidity (SSL) | Cảnh báo / Không phải liquidity |
|---|---|---|---|
| **Vị trí** | Phía TRÊN: trên old highs, equal highs, swing highs, trendline kháng cự | Phía DƯỚI: dưới old lows, equal lows, swing lows, trendline hỗ trợ | Vùng ở giữa range, không có đỉnh/đáy rõ |
| **Lệnh chờ** | Buy stops (SL của short + buy stop breakout) | Sell stops (SL của long + sell stop breakout) | FVG/void là vùng THIẾU giao dịch, không có cụm lệnh |
| **Engineered** | Equal highs / relative equal highs dụ short đặt SL phía trên | Equal lows / relative equal lows dụ long đặt SL phía dưới | Một đỉnh/đáy đơn lẻ không rõ ràng, ít người để ý |
| **Reference pools** | PDH, PWH, Asia/London/NY high | PDL, PWL, Asia/London/NY low | Mức giá tròn tâm lý nhưng không trùng pool cấu trúc |
| **Khi là draw** | Bias bullish → BSL là target; hoặc cần lấy BSL trước khi đảo xuống | Bias bearish → SSL là target; hoặc cần lấy SSL trước khi đảo lên | Pool đã bị lấy rồi (đã "cạn" liquidity) |

### Điều kiện bắt buộc
- [ ] Xác định được pool nằm ở **phía nào** (trên = BSL, dưới = SSL).
- [ ] Pool tương ứng với một loại cụ thể (PDH/PDL, equal highs/lows, swing, session...).
- [ ] Pool **chưa bị lấy** (còn liquidity để hút giá tới).
- [ ] Xác định được vị trí pool trong [[12 - Dealing Range]]: external hay internal.

### Điều kiện tăng xác suất
- [ ] Pool là **engineered liquidity** (equal highs/lows) — rất dễ trở thành target.
- [ ] Pool nằm cùng phía với [[12 - Daily Bias]] và đúng [[27 - Premium Discount]] (BSL ở premium, SSL ở discount).
- [ ] Pool là HTF reference (PDH/PDL, PWH/PWL) — draw mạnh hơn pool LTF.
- [ ] Có nhiều loại liquidity chồng lên nhau tại một vùng (vd equal highs + PDH + trendline).
- [ ] Đường tới pool còn nhiều "room" và không bị pool gần hơn chặn lại.

### Điều kiện làm setup yếu đi
- Pool đã bị sweep trong phiên trước, liquidity đã cạn.
- Pool quá gần giá hiện tại → R:R kém nếu dùng làm target.
- Nhầm internal liquidity với external draw → kỳ vọng sai khoảng cách đi.
- "Pool" thực ra là một liquidity void/imbalance, không có cụm lệnh thật.
- Liquidity ngược hướng draw chính (bị dùng làm cớ trade ngược narrative).

---

## 4. Quy trình phân tích đa khung thời gian

![[Liquidity-Sec-04-Da-Khung.svg|720]]
*Sơ đồ: Luồng đa khung — HTF xác định draw chính, LTF chỉ ra pool nào bị sweep để execution.*

> [!example] Quy trình 4 câu bắt buộc trước phiên
> 1. **Draw on liquidity chính hôm nay là pool nào?** (BSL hay SSL, level cụ thể)
> 2. **Pool đó đã bị lấy chưa, còn bao nhiêu room?**
> 3. **Có engineered liquidity (equal highs/lows) nào đang được dọn sẵn không?**
> 4. **Pool nào sẽ bị sweep TRƯỚC khi giá đảo chiều theo bias?**

### D1 / H4 — Bias & Narrative
- **Draw chính HTF:** xác định BSL hay SSL là target lớn nhất. Ghi rõ level: `BSL above PWH 1.0xxx`, `SSL below PDL 1.0xxx`.
- **External liquidity của dealing range:** đánh dấu đỉnh và đáy range (đó là external liquidity hai phía).
- **Pool nào còn mở:** liệt kê PDH/PDL, PWH/PWL, swing high/low chưa bị lấy.
- **Internal liquidity:** ghi FVG/OB lớn bên trong range mà giá có thể retrace tới.
- **Narrative:** *price is being drawn toward ___ (BSL/SSL) because ___; sẽ sweep ___ trước khi đảo về ___.*

```text
Mẫu ghi nhanh — Draw lên Buy-side
HTF dealing range: [D1 low] → [D1 high]
Draw on liquidity chính: BSL above [PWH / equal highs] tại [level]
SSL cần sweep trước: SSL below [đáy ngắn hạn / equal lows] tại [level]
Expected path: sweep SSL phía dưới (lấy nhiên liệu) → bullish repricing → target BSL phía trên
Internal liquidity giữa range: bullish FVG/OB tại [level]
Cảnh báo: nếu BSL đã bị lấy hôm trước → draw có thể đã cạn
```

```text
Mẫu ghi nhanh — Draw xuống Sell-side
HTF dealing range: [D1 low] → [D1 high]
Draw on liquidity chính: SSL below [PWL / equal lows] tại [level]
BSL cần sweep trước: BSL above [đỉnh ngắn hạn / equal highs] tại [level]
Expected path: sweep BSL phía trên (lấy nhiên liệu) → bearish repricing → target SSL phía dưới
Internal liquidity giữa range: bearish FVG/OB tại [level]
Cảnh báo: nếu SSL đã bị lấy hôm trước → draw có thể đã cạn
```

### H1 / M15 — POI & Context
- **Pool nào sắp bị chạm:** giá đang tiến tới BSL hay SSL nào ở khung này?
- **Engineered liquidity:** có equal highs/lows hình thành trên H1/M15 không? Đó là target dễ bị quét.
- **Phân biệt sweep vs break-and-go:** giá chạm pool rồi reject/reclaim (sweep, chuẩn bị reversal) hay đóng nến mạnh qua pool và đi tiếp (break thật)?
- **Vị trí internal/external:** pool sắp bị lấy là internal (giữa range) hay external (đỉnh/đáy range)? External draw thường là target lớn hơn.
- **Liên kết với POI:** sau khi sweep liquidity, giá có nằm trong một [[Fair Value Gap]] / [[Order Block]] hợp lệ để tìm entry không?

### M5 / M1 — Confirmation & Entry
- **Sweep đã hoàn tất chưa:** giá đã quét liquidity đối diện entry và **reclaim** lại chưa? Đây là điều kiện tiên quyết.
- **[[20 - Liquidity Sweep]] + [[21 - Market Structure Shift]]:** sau sweep, có MSS xác nhận đảo chiều không?
- **Có displacement không:** chuyển động sau sweep có để lại FVG/imbalance không?
- **Entry tại internal liquidity của LTF:** vào lệnh ở FVG/OB hình thành từ displacement, stop nằm sau điểm sweep.
- **Target là external liquidity:** TP hướng về pool liquidity đã xác định từ HTF (BSL/SSL chính).

> [!warning]
> **Liquidity LTF không tạo bias.** Một equal highs nhỏ trên M5 không làm đổi draw chính của D1. LTF chỉ cho biết pool nào bị quét **để execution**, sau khi HTF đã chỉ rõ draw chính.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

![[Liquidity-Sec-05-Xac-Nhan.svg|720]]
*Sơ đồ: Phân biệt Sweep (wick vượt → đóng lại + displacement) với Break thật/acceptance (đóng thân, giữ giá ngoài).*

### Setup được xem là hợp lệ khi
- [ ] Draw on liquidity chính được xác định rõ và còn mở.
- [ ] Pool liquidity đối diện entry đã bị **sweep** (đã lấy nhiên liệu) trước khi tìm reversal.
- [ ] Sau sweep, giá **reclaim** lại vùng và để lại displacement / FVG.
- [ ] Có [[21 - Market Structure Shift]] xác nhận giá quay đầu khỏi pool vừa quét.
- [ ] Target là external liquidity còn mở, đủ room cho R:R.
- [ ] Pool sweep và draw target cùng phục vụ một narrative [[12 - Daily Bias]].

### Setup bị vô hiệu khi
- [ ] Giá **đóng nến mạnh qua pool và giữ giá ngoài** (acceptance) → đây là break-and-go, không phải sweep.
- [ ] Cố vào lệnh khi liquidity đối diện entry **chưa bị lấy**.
- [ ] Draw chính đã bị delivered xong; tiếp tục trade theo hướng cũ là chase liquidity đã cạn.
- [ ] Nhầm một imbalance / liquidity void thành "pool" và kỳ vọng sweep ở đó.
- [ ] Trade ngược draw chính chỉ vì thấy một pool nhỏ ngược hướng.
- [ ] Sweep xảy ra nhưng không có displacement / reclaim → chưa đủ bằng chứng đảo chiều.

### Phân biệt "sweep" và "break thật" (acceptance)

| Quan sát | Cách đọc hợp lý |
|---|---|
| Giá wick qua đỉnh/đáy (equal highs/lows, PDH/PDL) rồi đóng nến trở lại trong range, kèm displacement ngược | **Sweep / stop hunt** — liquidity đã bị lấy; chờ MSS + entry theo hướng đảo |
| Giá đóng thân nến mạnh qua pool, giữ giá ngoài vùng, pullback không reclaim được | **Break thật / acceptance** — không phải sweep; không tìm reversal ở đây |
| Giá chạm pool đúng phía draw chính rồi tiếp tục đi xa hơn | Pool chỉ là internal liquidity trên đường tới external draw — chưa phải điểm đảo |
| Một equal highs/lows "sách giáo khoa" bị phá nhẹ rồi đảo gắt | Đây là engineered liquidity bị quét — kịch bản sweep điển hình |
| Giá phá pool nhưng đó là một imbalance/FVG chưa rebalance | Không phải sweep liquidity; là giá đang đi lấp void — đọc theo logic imbalance |

---

## 6. Ví dụ chart

### Ví dụ đúng — SSL sweep trước reversal lên BSL
![[Liquidity-Example-Correct.png]]

**Mô tả:**  
D1/H4 cho draw chính là BSL phía trên (PWH còn mở). Giá retrace vào discount và tạo equal lows nhỏ trên M15 (engineered SSL). Trong London Kill Zone, giá quét SSL dưới equal lows đó — lấy sell stops của đám đông — rồi lập tức reclaim range với một displacement bullish để lại FVG. M5 xác nhận bằng [[21 - Market Structure Shift]]. Entry tại FVG retracement; TP hướng về BSL (PWH) đã xác định từ đầu.

**Vì sao đây là ví dụ tốt:**
- Draw chính (BSL phía trên) được xác định **trước**, không phải sau khi vào lệnh.
- Sweep SSL xảy ra **TRƯỚC** reversal — đúng thứ tự bắt buộc.
- Engineered liquidity (equal lows) đóng vai trò "nhiên liệu" cho leg đi lên.
- Entry tại internal liquidity (FVG), target tại external liquidity (BSL) — đi từ internal → external.

### Ví dụ sai / dễ nhầm — Long theo breakout qua equal highs
![[Liquidity-Example-Wrong.png]]

**Mô tả lỗi:**  
Giá tạo equal highs rõ ràng. Trader thấy giá phá qua và Long theo breakout, nghĩ "phá kháng cự = chạy tiếp". Nhưng equal highs đó chính là **engineered BSL** — giá chỉ quét buy stops phía trên (sweep) rồi đảo chiều xuống, kéo lệnh Long vào stop loss. Trader đã mua đúng vào nơi smart money đang **phân phối** để fill lệnh sell lớn.

**Bài học:**
- Phá qua một liquidity pool rất thường là **sweep**, không phải breakout thật.
- Equal highs "đẹp, ai cũng thấy" là target hấp dẫn nhất để bị quét.
- Hãy hỏi: "Giá đang phá vào liquidity (chuẩn bị đảo) hay phá ra khỏi vùng cạn liquidity (đi tiếp)?"
- Không bao giờ đu breakout qua pool khi đó là draw chính theo hướng ngược bias.

---
### Sequence mẫu — Long (draw lên Buy-side)
```text
HTF draw chính = BSL phía trên (PWH / equal highs)
→ Giá về Discount của Dealing Range
→ Engineered SSL (equal lows) hình thành phía dưới
→ Sweep SSL (lấy nhiên liệu / sell stops)
→ Reclaim range + Bullish displacement
→ Bullish MSS xác nhận
→ Entry tại internal liquidity (FVG / OB)
→ Stop sau điểm sweep low
→ Target: internal liquidity trước → external BSL chính (PWH) sau
```

### Sequence mẫu — Short (draw xuống Sell-side)
```text
HTF draw chính = SSL phía dưới (PWL / equal lows)
→ Giá về Premium của Dealing Range
→ Engineered BSL (equal highs) hình thành phía trên
→ Sweep BSL (lấy nhiên liệu / buy stops)
→ Reclaim range + Bearish displacement
→ Bearish MSS xác nhận
→ Entry tại internal liquidity (FVG / OB)
→ Stop sau điểm sweep high
→ Target: internal liquidity trước → external SSL chính (PWL) sau
```

> [!note]
> Logic xuyên suốt: **liquidity là nhiên liệu, giá được giao từ pool này sang pool khác.** Một leg đi lên lấy BSL gần như luôn cần quét SSL phía dưới trước để gom đủ lệnh — và ngược lại. Sweep liquidity đối diện chính là bước "nạp nhiên liệu" cho reversal.

---

## 7. Kiến thức nâng cao (Advanced)

### 7.1. Bản đồ liquidity theo phiên — "Asia tạo, London quét, NY giao"

Liquidity không chỉ có cấu trúc không gian (đỉnh/đáy) mà còn có **cấu trúc thời gian**: mỗi phiên tạo ra liquidity cho phiên sau tiêu thụ.

![[Liquidity-Advanced-Session-Map.svg]]

- **Asia (19:00–02:00 NY):** thường consolidate → **Asia Range = kho liquidity hai phía** (buy stops trên Asia high, sell stops dưới Asia low). Asia càng hẹp và "sạch", kho càng đầy.
- **London (02:00–05:00):** phiên **manipulation** kinh điển — Judas swing quét MỘT đầu Asia range (thường ngược hướng thật của ngày), tạo **high hoặc low của ngày**. Đây là lúc câu hỏi "đầu nào của Asia bị lấy?" trả lời luôn câu hỏi bias.
- **New York (07:00–11:00):** phiên **delivery** — thường không tạo cực trị mới ngược hướng mà retrace vào FVG/OB do London để lại rồi expansion tới draw HTF (PDH/PDL). NY cũng có thể **quét London high/low** trước khi chạy (NY Judas nhỏ quanh 8:30–9:30).
- Chuỗi tiêu thụ chuẩn của một ngày bullish: `sell stops dưới Asia low (London lấy) → buy stops trên London high (NY lấy trên đường đi) → PDH/BSL chính (target cuối)`. Khi bạn kể được câu chuyện của ngày dưới dạng chuỗi pool bị tiêu thụ theo thứ tự, bạn đang đọc chart đúng cách ICT.

### 7.2. Thứ bậc pool — pool nào thắng khi nhiều pool cùng mở?

Khi 3–4 pool cùng tồn tại, xung đột được phân xử theo các nguyên tắc:

| Nguyên tắc | Nội dung | Ví dụ |
|---|---|---|
| **Seniority (thâm niên khung)** | Pool khung cao hút mạnh hơn pool khung thấp | PWH thắng Asia high; Monthly old high thắng PDH |
| **Độ "sạch" (clean vs jagged)** | Equal highs/lows phẳng, ai cũng thấy = hấp dẫn hơn vùng đỉnh/đáy lởm chởm | 3 đỉnh bằng nhau trên H1 > một swing high lẻ M15 |
| **Độ tươi** | Pool chưa từng bị test hút mạnh hơn pool đã bị chạm một phần | Old high nguyên vẹn > old high đã bị wick chạm |
| **Trên đường đi của draw HTF** | Pool nằm GIỮA giá và draw chính sẽ bị tiêu thụ "tiện đường" — không phải điểm đảo | BSL nhỏ giữa đường lên PWH: giá xuyên qua, đừng Short ở đó |
| **Proximity vs Seniority** | Pool gần được lấy TRƯỚC về thời gian, nhưng pool senior quyết định HƯỚNG chung | Quét session low (gần) rồi vẫn đi lên PWH (senior) |

> [!important] Câu hỏi phân xử quan trọng nhất
> Với mỗi pool: **"Đây là TERMINUS (đích đến — nơi giá đảo) hay WAYPOINT (trạm trung chuyển — nơi giá xuyên qua)?"** Pool cùng phía với draw HTF = waypoint, sẽ bị nuốt tiện đường. Pool đối diện draw, tại HTF array = ứng viên terminus. Nhầm waypoint thành terminus là lý do Short vào giữa một leg tăng.

### 7.3. Low-resistance vs High-resistance liquidity runs

ICT phân biệt hai "địa hình" mà giá chạy qua:

- **Low-Resistance Liquidity Run (LRLR):** đường tới target có chuỗi liquidity **thuận chiều** (vd chuỗi equal lows / trendline lows bên dưới trong bias bearish) và **không có PD Array kháng cự chưa xử lý** chắn đường → giá chạy nhanh, ít pullback sâu. Đây là điều kiện của những cú "one-way day".
- **High-Resistance Liquidity Run (HRLR):** đường đi bị chắn bởi nhiều FVG/OB ngược hướng chưa mitigate, hoặc phía trước không có pool rõ → giá đi giật cục, pullback sâu, dễ fail.

Ứng dụng: trước khi vào lệnh, **soi ĐƯỜNG ĐI chứ không chỉ ĐÍCH ĐẾN**. Cùng một target SSL, nếu bên dưới là chuỗi equal lows + không có bullish HTF array chắn = LRLR, giữ full target. Nếu phải xuyên qua 2 bullish FVG D1 chưa mitigate = HRLR, chia target/giảm kỳ vọng. Trendline "đẹp" mà đám đông tựa vào chính là một LRLR chờ được thu hoạch — chuỗi stop dọc trendline là xa lộ cho giá.

### 7.4. Inducement & liquidity phân tầng trước POI

Smart money không chỉ quét pool tự nhiên — nó **xây pool** ngay trước POI thật ([[15 - Inducement]]): một swing nhỏ hình thành phía trước OB/FVG HTF, dụ trader entry sớm và đặt stop ngay dưới swing đó. Kịch bản chuẩn: giá quét inducement (đám đông tưởng "đã sweep, vào thôi") → chạy tiếp VÀO POI thật sâu hơn → đảo thật từ đó.

Kỹ thuật đọc: trước mỗi POI HTF, tìm **swing/equal nhỏ gần nhất phía trước nó**. Nếu có → giả định đó là inducement; entry chỉ hợp lệ khi CẢ inducement lẫn mép POI đã được chạm. Đây là lời giải cho câu hỏi kinh điển "vì sao giá quét xong vẫn chạy thêm 20 pip nữa rồi mới đảo" — vì cú quét đầu chỉ là tầng inducement, chưa phải pool chính.

**Liquidity ladder:** trước phiên, xếp mọi pool theo thứ tự từ giá hiện tại ra xa (cả hai phía). Kỳ vọng chuẩn: giá tiêu thụ pool theo đúng thứ tự bậc thang. Giá "nhảy cóc" bỏ qua một pool gần → pool đó sẽ được quay lại lấy sau — thường là setup cho phiên/ngày kế tiếp.

### 7.5. Đọc phản ứng SAU khi pool bị lấy (sponsorship analysis)

Việc pool bị quét chưa cho biết gì — **cách giá rời khỏi pool mới là thông tin:**

| Hành vi sau khi pool bị lấy | Cách đọc |
|---|---|
| Displacement NGAY và mạnh rời khỏi pool (nến body lớn, để lại FVG) | Pool là **terminus** — reversal được sponsor; đây là lúc tìm entry |
| Giá lình xình quanh pool 3–5+ nến, không rời được | Chưa có sponsor; nghi ngờ sẽ quét sâu thêm (double sweep) hoặc break thật |
| Xuyên qua pool bằng body, pullback nông, chạy tiếp | Pool là **waypoint** — continuation; cấm counter-trade |
| Quét pool bằng wick dài nhiều lần nhưng không đóng nến qua | Absorption — hai bên giằng co; đứng ngoài chờ phân thắng bại |

Nguyên tắc: **thời gian giá ở lại vùng pool tỉ lệ nghịch với xác suất reversal.** Reversal thật thường "rời hiện trường" ngay lập tức.

### 7.6. Best Practices — Liquidity

> [!success] Best Practices
> 1. **Vẽ liquidity map TRƯỚC phiên, không trong phiên.** Trước London/NY: đánh dấu đủ PDH/PDL, PWH/PWL, Asia high/low, equal highs/lows, swing lớn — kèm nhãn `terminus?` hay `waypoint?` cho từng pool. Trong phiên chỉ được TIÊU THỤ bản đồ, không vẽ thêm.
> 2. **Mỗi pool một câu hỏi:** "Ai kẹt ở đây và stop của họ nằm đâu?" Trả lời được = hiểu pool; không trả lời được = đừng dùng pool đó làm căn cứ.
> 3. **Soi đường đi (LRLR/HRLR) trước khi chọn target.** Target xa chỉ hợp lệ khi đường tới đó low-resistance; gặp HTF array ngược hướng chưa mitigate → chia target tại đó.
> 4. **Mặc định có inducement trước mọi POI HTF.** Chờ tầng mồi bị quét rồi mới tính entry tại POI thật; nếu không có swing mồi nào phía trước, entry tại mép POI với size thận trọng hơn.
> 5. **Đánh giá pool bằng phản ứng rời đi**, không bằng cú chạm: displacement ngay = terminus; lình xình = chờ; xuyên body = waypoint.
> 6. **Cập nhật bản đồ ngay khi một pool bị tiêu thụ:** gạch pool đã lấy, hỏi "pool kế tiếp trên thang là gì?" — bias trong ngày trôi theo thang liquidity, không theo cảm xúc.
> 7. **Log frontmatter:** `draw_on_liquidity`, `pool_role` (terminus/waypoint), `path_resistance` (low/high), `inducement_present` — sau 30+ lệnh, thống kê xem lỗi lớn nhất của mình là nhầm waypoint thành terminus hay vào trước khi inducement bị quét.
> 8. **Đừng bao giờ là liquidity.** Trước khi đặt stop, hỏi: "stop này có nằm trong một pool rõ ràng (dưới equal lows, sát swing) không?" Nếu có → dời ra ngoài cấu trúc quét (sau sweep point), hoặc bỏ setup.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Khái niệm ICT chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**.

### A. Context (HTF)
- [ ] Tôi đã xác định draw on liquidity **chính** (BSL hay SSL, level cụ thể).
- [ ] Pool draw chính còn mở (chưa bị lấy).
- [ ] Tôi phân biệt được external liquidity (target lớn) và internal liquidity (điểm retrace).
- [ ] Tôi đã ghi nhận engineered liquidity (equal highs/lows) đang được dọn sẵn.
- [ ] Draw chính phù hợp với [[12 - Daily Bias]] và [[27 - Premium Discount]].
- [ ] Tôi biết pool nào cần bị **sweep trước** để leg đảo chiều có nhiên liệu.

### B. Execution (LTF / khi giá tới POI)
- [ ] Liquidity đối diện entry đã thực sự bị **sweep** (không phải break-and-go).
- [ ] Sau sweep, giá đã **reclaim** và để lại displacement.
- [ ] Có [[21 - Market Structure Shift]] xác nhận đảo chiều.
- [ ] Entry tại internal liquidity (FVG/OB), không phải đu theo sweep.
- [ ] Stop loss nằm **sau** điểm sweep (nơi market đã quét xong).
- [ ] Target là external liquidity còn mở, đường đi đủ room cho R:R.

### C. Quy tắc "không có lệnh"
- [ ] Không xác định được draw chính → không trade.
- [ ] Liquidity đối diện entry chưa bị lấy → không trade.
- [ ] Giá đang **break-and-go** (acceptance) chứ không sweep → không tìm reversal.
- [ ] Draw chính đã cạn (đã bị lấy xong) và chưa có pool mới → không trade.
- [ ] Nhầm imbalance/void với pool → dừng lại, đọc lại chart.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Đu breakout qua pool | Long khi phá equal highs / Short khi phá equal lows | Đó thường là sweep; vào đúng nơi smart money phân phối | Hỏi "phá vào liquidity hay phá ra khỏi vùng cạn?"; chờ reclaim |
| Vào lệnh trước sweep | Liquidity đối diện entry chưa bị lấy đã vào | Stop nằm đúng nơi market còn muốn quét | Chờ sweep + reclaim + MSS đúng thứ tự |
| Đặt SL ngay trên/dưới pool | Stop loss đặt sát đỉnh đôi / đáy đôi | Đó chính là cụm liquidity market nhắm tới quét | Đặt stop **sau** điểm sweep, không tại pool |
| Nhầm liquidity với imbalance | Kỳ vọng "sweep" tại một FVG/void | Void là vùng thiếu giao dịch, không có cụm lệnh để quét | Pool = đỉnh/đáy có lệnh; void = vùng giá đi nhanh cần lấp |
| Chọn sai draw chính | Lấy pool nhỏ/gần làm target chính | Kỳ vọng sai hướng và sai khoảng cách đi | Ưu tiên HTF pool (PDH/PDL, PWH/PWL) + cùng hướng bias |
| Trade pool đã cạn | Tiếp tục target một BSL/SSL đã bị lấy | Liquidity đã hết, giá không còn lý do tới đó | Đánh dấu pool đã bị lấy; tìm pool mới chưa lấy |
| Bỏ qua thứ tự sweep-then-reverse | Tìm reversal mà chưa thấy pool nào bị quét | Reversal thiếu nhiên liệu, xác suất thấp | Yêu cầu: sweep TRƯỚC, reversal SAU — không đảo thứ tự |
| Coi mọi đỉnh/đáy là liquidity ngang nhau | Không phân biệt engineered vs structural | Bỏ lỡ target dễ bị quét nhất (equal highs/lows) | Ưu tiên engineered liquidity và HTF reference |
| Target tùy ý theo pip | TP cố định, không trùng pool nào | Không đồng bộ với draw on liquidity | Đặt TP quanh liquidity rõ: internal trước, external sau |
| Không cập nhật draw sau khi bị lấy | Giữ một narrative cũ dù pool đã sweep xong | Bias lệch khỏi delivery thực tế của market | Reassess draw mới ngay sau khi pool chính bị lấy |

---

## 10. Câu hỏi tự kiểm tra

- Tôi có giải thích được liquidity (resting orders) khác volume cổ điển thế nào không?
- BSL nằm phía nào, SSL nằm phía nào, và loại lệnh gì nằm ở mỗi pool?
- Draw on liquidity chính hôm nay là pool nào, đã bị lấy chưa?
- Đỉnh/đáy này là **target để giá lấy** hay **mức để giá tôn trọng**?
- Equal highs/lows trên chart là engineered liquidity hay chỉ tình cờ?
- Pool sắp bị chạm là internal hay external range liquidity?
- Giá đang **sweep** (chuẩn bị đảo) hay **break-and-go** (đi tiếp)?
- Vùng này là liquidity pool hay liquidity void/imbalance?
- Pool nào cần bị sweep TRƯỚC để leg đảo chiều có nhiên liệu?
- Setup nào trong journal đã đu breakout sai vào điểm sweep?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Liquidity trong ICT là gì?  
**Đáp:** Là các cụm lệnh chờ (resting orders) — stop loss và lệnh breakout/pending — nằm trên đỉnh / dưới đáy mà thị trường (vận hành như thuật toán) bị hút tới để fill khối lượng lớn của smart money.

### Q2
**Hỏi:** Buy-side liquidity nằm ở đâu và gồm những lệnh gì?  
**Đáp:** Nằm PHÍA TRÊN — trên old highs, equal/relative equal highs, swing highs, trendline. Gồm buy stops (SL của người bán khống) + buy stop của breakout traders.

### Q3
**Hỏi:** Sell-side liquidity nằm ở đâu và gồm những lệnh gì?  
**Đáp:** Nằm PHÍA DƯỚI — dưới old lows, equal lows, swing lows. Gồm sell stops (SL của người mua) + sell stop breakout.

### Q4
**Hỏi:** Engineered liquidity là gì và vì sao nguy hiểm?  
**Đáp:** Là equal highs/lows được "tạo ra" để dụ trader đặt stop loss; cụm stop đó là target hấp dẫn nhất để smart money quét. Phá qua nó thường là sweep, không phải breakout thật.

### Q5
**Hỏi:** Khác biệt giữa internal và external range liquidity?  
**Đáp:** External = liquidity tại đỉnh/đáy của dealing range (target lớn). Internal = liquidity bên trong range như FVG/OB (điểm retrace). Giá thường đi external → internal → external.

### Q6
**Hỏi:** "Draw on liquidity" nghĩa là gì?  
**Đáp:** Là pool liquidity mà giá có xác suất cao hướng tới làm target/điểm phân phối — câu hỏi nền tảng cần trả lời trước khi nghĩ tới entry.

### Q7
**Hỏi:** Liquidity và liquidity void/imbalance khác nhau ra sao?  
**Đáp:** Liquidity = pool lệnh chờ tại đỉnh/đáy (giá tới để lấy). Liquidity void/imbalance = vùng giá đi nhanh THIẾU giao dịch, cần rebalance — KHÔNG phải pool lệnh.

### Q8
**Hỏi:** Vì sao sweep liquidity thường xảy ra trước reversal?  
**Đáp:** Vì liquidity là "nhiên liệu": để đảo chiều và đi lấy pool phía đối diện, market cần quét cụm lệnh gần trước để gom đủ lệnh đối ứng cho khối lượng lớn.

---

## 12. Liên kết với Trade Journal

> [!note]
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "03 - Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
draw_on_liquidity: "BSL above PWH 1.xxxx" # pool chính giá hướng tới
liquidity_side: buy-side # buy-side | sell-side
liquidity_type: equal-highs # PDH/PDL | PWH/PWL | equal-highs/lows | session | swing | trendline
liquidity_range: external # external | internal
swept_before_entry: "SSL below equal lows 1.xxxx" # pool bị quét trước reversal
sweep_confirmed: true # true | false (đã reclaim + displacement chưa)
liquidity_target_hit: false # target đã được delivered chưa
```

> [!tip]
> Sau 30–50 lệnh có dữ liệu, tạo dashboard so sánh `swept_before_entry` (có/không) với win rate và average R. Mục tiêu là kiểm chứng giả thuyết cốt lõi: "entry SAU khi liquidity đối diện bị sweep" có edge thực tế hơn "entry trước sweep" với chính cách bạn execution hay không.

---

## 13. Lesson Learned

### Bài học chính
- Liquidity là **khái niệm nền tảng nhất**: mọi concept ICT khác chỉ phục vụ câu hỏi "giá đang đi lấy liquidity nào?".
- Phá qua một pool thường là **sweep**, không phải breakout — đừng đu theo, hãy chờ reclaim.
- Equal highs/lows "đẹp, ai cũng thấy" là **engineered liquidity** — target dễ bị quét nhất, không phải vùng đảo chiều an toàn.
- Liquidity là nhiên liệu: reversal có chất lượng gần như luôn xảy ra **sau khi** liquidity đối diện bị sweep.
- Phân biệt cho được liquidity (pool lệnh) với imbalance/void (vùng cần rebalance) — hai thứ khác bản chất.
- Đặt stop loss **sau** điểm sweep, không tại pool; đặt target quanh external liquidity, không theo pip tùy ý.

### Quy tắc cá nhân rút ra
- [ ] Tôi không vào lệnh nếu chưa xác định được draw on liquidity chính.
- [ ] Tôi không đu breakout qua pool; tôi chờ sweep + reclaim + MSS đúng thứ tự.
- [ ] Tôi không đặt stop loss ngay tại đỉnh đôi / đáy đôi — đó là nơi market nhắm tới.
- [ ] Tôi luôn hỏi "đây là pool hay là void?" trước khi kỳ vọng một sweep.
- [ ] Sau khi draw chính bị lấy xong, tôi dừng và xác định pool mới trước khi tìm lệnh tiếp.

### Câu nhắc nhở khi trade
> **"Thị trường không đi tìm giá đẹp — nó đi tìm liquidity. Hãy hỏi pool nào đang hút giá tới, đừng hỏi nến đang muốn gì."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt liquidity (resting orders) với volume và với imbalance không? |
| Nhận diện trên chart |  | Có đánh dấu đúng BSL phía trên / SSL phía dưới và phân loại pool không? |
| Biết khi nào bỏ qua |  | Có nhận ra draw đã cạn / break-and-go để không trade không? |
| Kết hợp với context HTF |  | Có xác định draw chính phù hợp Daily Bias + Premium/Discount không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra SAU sweep + reclaim + MSS không? |
| Review sau trade |  | Có kiểm tra `swept_before_entry` bằng dữ liệu journal thay vì cảm xúc không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Liquidity]]`.
- [ ] Review riêng các lệnh **có sweep trước entry** và **không có sweep**.
- [ ] Thống kê win rate, average R, lỗi lặp lại theo `liquidity_type` và `liquidity_range`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.

---

## Appendix — Liquidity Map Card

> [!abstract] Copy vào Daily Note trước London / New York
> **Date / Market:**  
> **HTF dealing range (external liquidity hai phía):**  
> **Buy-side liquidity (BSL) còn mở:** PWH / PDH / equal highs / swing high @ ___  
> **Sell-side liquidity (SSL) còn mở:** PWL / PDL / equal lows / swing low @ ___  
> **Engineered liquidity quan sát:** equal highs / equal lows @ ___  
> **Internal range liquidity:** FVG / OB @ ___  
> **DRAW ON LIQUIDITY chính (target):** BSL / SSL @ ___  
> **Pool cần SWEEP trước reversal:** ___  
> **Pool đã bị lấy (loại khỏi target):** ___  
> **Session đang quan sát:** Asia / London / NY  
> **Điều kiện invalidation (acceptance qua pool):** ___  
> **No-trade condition:** draw chưa rõ / liquidity đã cạn / là void chứ không phải pool
