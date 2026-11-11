---
type: ict-concept
concept: Daily Bias
aliases:
  - ICT Daily Bias
  - HTF Directional Bias
tags:
  - trading/ict/concept
  - trading/study
  - "#DailyBias"
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
last_reviewed: 2026-06-21
created: 2026-06-20
updated: 2026-07-03
common_mistakes:
  - "[[Mistake - Wrong Daily Bias]]"
  - "[[Mistake - Entry When MSS not in POI Zone]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
---

# Daily Bias

> [!summary] Tóm tắt 1 câu
> **Daily Bias là giả thuyết có điều kiện về hướng phân phối giá có xác suất cao hơn trong ngày, được xây từ HTF dealing range, draw on liquidity, vị trí Premium/Discount và PD Array; nó lọc hướng trade, không phải tín hiệu vào lệnh.**

> [!important] Nguyên tắc cốt lõi
> **Bias trả lời “ưu tiên tìm Long, Short hay đứng ngoài?”; entry model trả lời “vào ở đâu và khi nào?”.**  
> Một M5 MSS đẹp không được phép đảo ngược Daily Bias nếu nó không xuất hiện sau liquidity sweep tại HTF POI hợp lệ.

---

## 1. Định nghĩa

![[Daily-Bias-Sec-01-Dinh-Nghia.svg|720]]
*Sơ đồ: Daily Bias là giả thuyết có điều kiện về hướng phân phối giá trong ngày — bộ lọc hướng, không phải tín hiệu vào lệnh.*

**Khái niệm:**  
Daily Bias trong ICT là kỳ vọng có cấu trúc về **leg giá kế tiếp trong ngày**: giá có xác suất cao hơn sẽ được phân phối lên để tìm buy-side liquidity / rebalance vùng giá phía trên, hay phân phối xuống để tìm sell-side liquidity / rebalance vùng giá phía dưới. Bias được xây từ bức tranh HTF, không phải từ một nến D1 xanh/đỏ đơn lẻ và cũng không phải dự báo chắc chắn.

**Mục đích trong ICT:**  
- Lọc hướng giao dịch để tránh lấy mọi MSS/FVG trên M5.
- Xác định phía liquidity nên kỳ vọng làm target trong ngày.
- Biết nên chờ giá retrace vào **discount** để Long hay vào **premium** để Short.
- Liên kết cấu trúc D1/H4 với POI H1/M15 và entry model M5/M1.

**Vì sao khái niệm này quan trọng:**  
ICT 2022 model chỉ mạnh khi entry LTF đi cùng **HTF narrative**. Không có bias rõ ràng, trader thường biến mọi displacement trên M5 thành một “setup”, dẫn tới overtrading, trade giữa range hoặc trade ngược draw on liquidity chính.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đang ở đâu trong narrative?
- Giá vừa lấy thanh khoản hay chưa?
- Giá có đang phản ứng ở POI hợp lệ không?
- Có đủ điều kiện để xuống LTF tìm entry không?
- Hôm nay ưu tiên tìm Long, Short, hay **No Trade / Neutral**?

### Daily Bias không phải là gì
- Không phải “D1 đang tăng thì phải Long ngay”.
- Không phải dự đoán chắc chắn nến ngày sẽ đóng xanh hay đỏ.
- Không phải lý do bỏ qua vị trí Premium/Discount.
- Không phải quyền vào lệnh khi chưa có liquidity sweep + LTF confirmation.
- Không phải lý do cố giữ bias khi thị trường đã invalidation rõ ràng.

---

## 2. Bối cảnh sử dụng

![[Daily-Bias-Sec-02-Boi-Canh.svg|720]]
*Sơ đồ: Ba trạng thái bias (Bullish / Bearish / Neutral) và hành động ưu tiên cho mỗi trạng thái.*

### Ba trạng thái bias cần chấp nhận

| Trạng thái | Ý nghĩa thực chiến | Hành động ưu tiên |
|---|---|---|
| **Bullish** | Kỳ vọng leg kế tiếp phân phối lên; draw on liquidity quan trọng nằm phía trên | Chờ retrace xuống **discount / bullish PD Array**, sweep sell-side liquidity, rồi tìm bullish MSS + displacement trên LTF |
| **Bearish** | Kỳ vọng leg kế tiếp phân phối xuống; draw on liquidity quan trọng nằm phía dưới | Chờ retrace lên **premium / bearish PD Array**, sweep buy-side liquidity, rồi tìm bearish MSS + displacement trên LTF |
| **Neutral / Mixed** | Bằng chứng mâu thuẫn, giá ở equilibrium, hoặc mục tiêu hai phía đều gần / không rõ | Giảm tần suất; không ép trade; chỉ giao dịch nếu hệ thống có rule riêng cho range hoặc chờ narrative rõ hơn |

> [!tip]
> **Neutral là một kết luận hợp lệ.** Không có Daily Bias rõ ràng tốt hơn nhiều so với một bias được “bịa” để có lệnh.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có HTF dealing range rõ ràng được tạo bởi swing có displacement/BOS đáng kể.
- [ ] Có Daily Bias rõ ràng: hướng delivery, draw on liquidity và điểm invalidation đều được viết ra.
- [ ] Giá đang ở Premium/Discount phù hợp với hướng trade.
- [ ] Giá nằm trong hoặc phản ứng tại POI HTF/H1 hợp lệ.
- [ ] Có liquidity pool rõ ràng: PDH/PDL, PWH/PWL, Asia high/low, equal highs/lows, swing high/low đáng kể.
- [ ] Có thời điểm giao dịch phù hợp: London / New York Kill Zone theo plan của thị trường đang trade.
- [ ] Có displacement / MSS / FVG xác nhận trên LTF **sau khi** giá chạm POI và quét liquidity.

### Khi nào nên bỏ qua?
- [ ] Giá đang ở giữa range, gần equilibrium, không rõ Premium/Discount.
- [ ] Không có liquidity target rõ ràng hoặc target đã bị lấy xong.
- [ ] Không có HTF narrative; D1, H4 và H1 đang cho tín hiệu mâu thuẫn mà không giải thích được bằng pullback.
- [ ] Tín hiệu LTF xuất hiện ngoài kill zone hoặc ngoài kế hoạch session.
- [ ] Chỉ thấy mô hình nhỏ lẻ nhưng không nằm trong POI.
- [ ] R:R thực tế kém vì target liquidity quá gần hoặc stop loss phải quá rộng.
- [ ] Có tin tức high-impact gần thời điểm entry mà plan của mình không cho phép giao dịch.

---

## 3. Cấu trúc nhận diện trên chart

![[Daily-Bias-Sec-03-Nhan-Dien.svg|720]]
*Sơ đồ: Ma trận 6 thành phần (structure, draw, P/D, POI, liquidity event, LTF) cộng dồn bằng chứng để ra kết luận bias.*

### Dấu hiệu chính
1. **HTF price delivery / market structure:** D1/H4 đang mở rộng theo hướng nào, hoặc vừa có dấu hiệu chuyển delivery sau một liquidity event quan trọng?
2. **Draw on liquidity:** liquidity pool chưa được lấy nào có ý nghĩa lớn nhất và nằm ở phía nào của dealing range?
3. **Location:** giá hiện ở premium, discount hay equilibrium của dealing range phù hợp; có đang chạm HTF PD Array hỗ trợ cho leg kế tiếp không?
4. **Reaction quality:** sau khi chạm POI hoặc sweep liquidity, có displacement có chủ đích và FVG rõ không?
5. **Timing:** hành vi giá có xuất hiện trong cửa sổ thời gian hệ thống của mình có edge không?

### Ma trận xây Daily Bias

| Thành phần | Bằng chứng Bullish | Bằng chứng Bearish | Cảnh báo / Neutral |
|---|---|---|---|
| **HTF structure** | D1/H4 giữ bullish delivery; HL được bảo vệ; bullish displacement phá swing quan trọng | D1/H4 giữ bearish delivery; LH được bảo vệ; bearish displacement phá swing quan trọng | Choppy, nhiều break nhỏ, chưa xác định swing quan trọng |
| **Draw on liquidity** | BSL / swing high / PDH / PWH còn mở phía trên và phù hợp narrative | SSL / swing low / PDL / PWL còn mở phía dưới và phù hợp narrative | Liquidity hai phía đều gần; mục tiêu chính vừa bị lấy |
| **Premium/Discount** | Giá vào discount của HTF range, nhất là khi chạm bullish PD Array | Giá vào premium của HTF range, nhất là khi chạm bearish PD Array | Giá quanh 50%; range chưa rõ hoặc bị chọn sai |
| **POI / PD Array** | Bullish FVG, bullish OB, mitigation block hoặc discount array còn hiệu lực | Bearish FVG, bearish OB, mitigation block hoặc premium array còn hiệu lực | POI đã bị xuyên/mitigate nhiều lần hoặc không tạo displacement |
| **Liquidity event** | Sweep SSL rồi reject/reclaim range; sau đó bullish displacement | Sweep BSL rồi reject/reclaim range; sau đó bearish displacement | Chưa sweep, sweep nhưng đóng nến tiếp diễn, hoặc chưa có phản ứng |
| **LTF confirmation** | Bullish MSS + displacement + FVG trong POI | Bearish MSS + displacement + FVG trong POI | MSS giữa range, không có displacement, hoặc xảy ra trước POI |

### Điều kiện bắt buộc
- [ ] Xác định được **HTF dealing range** và ghi rõ hai đầu range.
- [ ] Xác định được **draw on liquidity chính**: pool nào, ở đâu, vì sao nó quan trọng hơn pool còn lại.
- [ ] Xác định được vị trí giá là premium / discount / equilibrium theo đúng dealing range.
- [ ] Có ít nhất một HTF/H1 POI hợp lệ phù hợp với bias.
- [ ] Có mức **invalidation** rõ ràng: điều gì xảy ra thì bias không còn đáng tin.

### Điều kiện tăng xác suất
- [ ] Có liquidity sweep trước đó, sau đó giá đóng/reclaim trở lại theo hướng kỳ vọng.
- [ ] Có displacement mạnh, phá cấu trúc có ý nghĩa và để lại FVG/imbalance rõ ràng.
- [ ] Có FVG/Imbalance rõ ràng để tạo entry model với stop loss logic.
- [ ] Có MSS/BOS đúng ngữ cảnh, tức là nằm **trong / ngay sau phản ứng tại POI**.
- [ ] Entry nằm trong vùng Premium/Discount hợp lý của dealing range LTF.
- [ ] Target là external/internal liquidity rõ ràng, còn mở và đủ khoảng trống cho R:R.
- [ ] H1 chỉ đang pullback ngược D1 và pullback đó đi vào đúng D1/H4 POI, thay vì H1 hình thành reversal HTF hoàn chỉnh.

### Điều kiện làm setup yếu đi
- Bias chỉ dựa vào HH/HL hoặc một cây nến D1 gần nhất, không có liquidity target.
- Giá đã chạy xa khỏi POI theo hướng bias; entry trở thành chase ở premium cho Long hoặc discount cho Short.
- M5 MSS hình thành trước liquidity sweep, hoặc ngoài HTF POI.
- H1 đã lấy target chính của D1, sau đó xuất hiện displacement mạnh ngược hướng và cấu trúc HTF thay đổi.
- Setup xuất hiện muộn sau expansion lớn; phần lớn daily range đã được tiêu thụ.

---

## 4. Quy trình phân tích đa khung thời gian

![[Daily-Bias-Sec-04-Da-Khung.svg|720]]
*Sơ đồ: Top-down D1/H4 → H1/M15 → M5/M1 với 4 câu hỏi bắt buộc trước phiên.*

> [!example] Quy trình 4 câu bắt buộc trước phiên
> 1. **Hôm nay ưu tiên Long, Short hay Neutral?**  
> 2. **Giá đang bị hút về liquidity nào?**  
> 3. **Tôi chỉ muốn vào từ POI nào và ở vùng giá nào?**  
> 4. **Điều gì chứng minh tôi sai?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral.
- **HTF dealing range:** đánh dấu swing high và swing low tạo ra displacement/BOS đáng kể; không dùng swing quá nhỏ chỉ vì nó gần giá.
- **Giá đang ở Premium hay Discount?** ghi vị trí theo range đang dùng, không dùng Fibonacci từ range khác.
- **Liquidity target gần nhất:** ghi rõ tên level, ví dụ `PDH`, `PDL`, `PWH`, `PWL`, `BSL above D1 swing high`, `SSL below equal lows`.
- **POI HTF quan trọng:** D1/H4 FVG, OB, breaker, mitigation block, opening gap hoặc vùng imbalance còn hiệu lực.
- **Narrative:** price is likely to deliver from ___ toward ___ because ___; invalid if ___.

```text
Mẫu ghi nhanh — Bullish Bias
HTF dealing range: [D1 low] → [D1 high]
Location: Discount / đang chạm bullish D1-H4 PD Array
Draw on liquidity: BSL tại [level]
Expected path: sweep SSL gần POI → bullish repricing → target BSL
Invalidation: D1/H4 chấp nhận giá phá xuống [level] + không reclaim / bearish displacement thay đổi narrative
```

```text
Mẫu ghi nhanh — Bearish Bias
HTF dealing range: [D1 low] → [D1 high]
Location: Premium / đang chạm bearish D1-H4 PD Array
Draw on liquidity: SSL tại [level]
Expected path: sweep BSL gần POI → bearish repricing → target SSL
Invalidation: D1/H4 chấp nhận giá phá lên [level] + không reclaim / bullish displacement thay đổi narrative
```

### H1 / M15 — POI & Context
- **POI đang quan sát:** ghi vùng giá cụ thể và timeframe, ví dụ `H1 bearish FVG 1.0xxx–1.0xxx`.
- **Lý do POI hợp lệ:** POI có tạo displacement không? Có ở premium/discount của HTF range không? Có còn unmitigated không? Có cùng hướng draw on liquidity không?
- **Giá đã sweep liquidity chưa?** xác định pool bị lấy, vị trí sweep, chất lượng reclaim/rejection.
- **Giá có phản ứng rõ không?** ưu tiên displacement có nến body rõ, phá swing nội bộ quan trọng và để lại imbalance.
- **Phân biệt pullback với reversal:** H1 đi ngược Daily Bias có thể chỉ là pullback nếu nó đang hướng vào POI HTF và chưa invalid HTF narrative. Không đổi bias chỉ vì vài nến H1 ngược hướng.

### M5 / M1 — Confirmation & Entry
- **Có MSS không?** MSS phải phá swing bảo vệ gần nhất có ý nghĩa, không chỉ là một micro swing.
- **MSS có nằm trong POI không?** nếu ngoài POI hoặc giữa range, xem là signal yếu / bỏ qua theo rule.
- **Có displacement không?** cần có urgency, body đóng quyết đoán, và lý tưởng là để lại FVG.
- **Có FVG/OB entry model không?** chỉ chọn entry khi retrace hợp lý vào FVG/OB hình thành từ displacement.
- **Entry có hợp lệ theo checklist không?** stop nằm sau swing logic / điểm sweep, target có liquidity rõ, không vượt risk limit.

> [!warning]
> **M5/M1 không “tạo” Daily Bias.** LTF chỉ cho phép execution sau khi HTF narrative + POI + liquidity event đã đúng bối cảnh.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

![[Daily-Bias-Sec-05-Xac-Nhan.svg|720]]
*Sơ đồ: Điều kiện setup hợp lệ vs vô hiệu; phân biệt wick qua level (sweep) và đóng thân giữ giá ngoài (acceptance/invalidation).*

### Setup được xem là hợp lệ khi
- [ ] Daily Bias được viết thành một narrative đầy đủ: `range → location → draw on liquidity → POI → invalidation`.
- [ ] Giá tiếp cận đúng POI phù hợp với bias và vị trí premium/discount.
- [ ] Liquidity phía đối diện entry bị sweep hoặc có sự kiện thanh khoản hợp lý trước reaction.
- [ ] LTF tạo MSS có ý nghĩa **trong / ngay sau POI**.
- [ ] Displacement xác nhận repricing và tạo FVG/OB để vào lệnh có cấu trúc.
- [ ] Target là liquidity còn mở, không phải một mức TP tùy ý.
- [ ] R:R sau spread/slippage vẫn đạt mức tối thiểu trong trading plan.

### Setup bị vô hiệu khi
- [ ] Giá phá hẳn POI mà không phản ứng; đóng nến và duy trì acceptance ngoài vùng POI.
- [ ] MSS xảy ra nhưng không nằm trong POI.
- [ ] Không có displacement rõ ràng sau sweep/POI.
- [ ] Liquidity sweep chưa xảy ra nhưng đã cố vào lệnh.
- [ ] Entry ngược Daily Bias mà không có lý do mạnh và không thuộc một counter-trend playbook được backtest riêng.
- [ ] HTF target của bias đã được delivered, sau đó thị trường cho thấy displacement/structure shift theo hướng ngược.
- [ ] Điều kiện invalidation đã được xác nhận: ví dụ D1/H4 chấp nhận giá xuyên level làm hỏng narrative ban đầu, thay vì chỉ wick ngắn hạn.

### Phân biệt “wick qua level” và invalidation

| Quan sát | Cách đọc hợp lý |
|---|---|
| Giá wick qua POI/liquidity rồi đóng trở lại range, kèm displacement ngược | Có thể là sweep / rejection; chờ LTF confirmation, không vội đổi bias |
| Giá đóng thân nến mạnh qua POI, tiếp tục giữ giá ngoài vùng và các pullback không reclaim được | Acceptance; bias/POI có thể invalid, ưu tiên đánh giá lại narrative |
| Một M1/M5 break ngược hướng khi D1/H4 vẫn nguyên | Có thể chỉ là internal pullback; không tự động đảo Daily Bias |
| H1/H4 displacement phá swing HTF, target cũ đã hoàn thành, tạo POI ngược hướng | Đây là bằng chứng mạnh hơn để xem xét đổi bias |

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish Daily Bias, Long theo ICT 2022 Model
![[Daily-Bias-Example-Bullish.png]]

**Mô tả:**  
D1/H4 đang có draw on liquidity lên phía trên tại BSL/PDH. Giá retrace vào discount của dealing range và chạm bullish H1 PD Array. Trong London hoặc New York Kill Zone, giá quét sell-side liquidity dưới đáy ngắn hạn, reclaim range, rồi M5 tạo bullish MSS + displacement để lại FVG. Entry tại FVG retracement; TP hướng về BSL đã xác định từ đầu.

**Vì sao đây là ví dụ tốt:**
- Daily Bias có đủ: HTF range, discount location, bullish POI và liquidity target phía trên.
- Liquidity sweep xảy ra **trước** LTF reversal signal.
- MSS + displacement nằm trong context POI, không nằm giữa range.
- Entry model và target cùng phục vụ một narrative, thay vì ghép các concept rời rạc.

### Ví dụ sai / dễ nhầm — Short vì M5 MSS giữa range
![[Daily-Bias-Example-Wrong-MSS.png]]

**Mô tả lỗi:**  
D1 vẫn bullish và target BSL phía trên còn mở. Giá đang ở discount hoặc gần equilibrium, chưa vào bearish HTF POI. Trader nhìn thấy một bearish M5 MSS/FVG nhỏ giữa range và Short. Giá chỉ pullback ngắn rồi tiếp tục mở rộng lên lấy BSL, khiến lệnh Short bị stop loss.

**Bài học:**
- MSS là **confirmation**, không phải bias độc lập.
- Không Short chỉ vì thấy displacement nếu giá chưa ở premium + bearish POI + có BSL sweep hợp lệ.
- Hãy hỏi: “Lệnh này đang đi **đến liquidity nào** và có thuận HTF narrative không?”

---
### Sequence mẫu — Long thuận Daily Bias
```text
HTF Bullish Bias
→ HTF Dealing Range
→ Giá về Discount + Bullish PD Array
→ Sweep Sell-Side Liquidity
→ Bullish MSS trong POI
→ Displacement tạo FVG/OB
→ Retrace vào FVG/OB (M5/M1)
→ Stop sau swing / sweep low logic
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short thuận Daily Bias
```text
HTF Bearish Bias
→ HTF Dealing Range
→ Giá về Premium + Bearish PD Array
→ Sweep Buy-Side Liquidity
→ Bearish MSS trong POI
→ Displacement tạo FVG/OB
→ Retrace vào FVG/OB (M5/M1)
→ Stop sau swing / sweep high logic
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> Với ICT 2022 model, sequence thường không phải là “thấy MSS rồi vào”. Sequence có chất lượng là: **HTF draw on liquidity → retracement vào PD Array → liquidity sweep → LTF MSS/displacement → FVG entry**.

---

## 7. Kiến thức nâng cao (Advanced)

### 7.1. Power of Three & Midnight Open — trục thời gian của bias

Daily Bias không chỉ là “hướng” — nó là kỳ vọng về **hình dạng của nến ngày** theo chu kỳ [[02 - AMD]] (Accumulation–Manipulation–Distribution):

![[Daily-Bias-Advanced-PO3.svg]]

- **Midnight Open (00:00 NY time)** là mức open chính thức của “ngày giao dịch” theo thuật toán. Với **bias bullish**, kỳ vọng chuẩn là: giá tích lũy quanh midnight open → **Judas swing** đẩy XUỐNG dưới open (quét SSL, thường trong London KZ 02:00–05:00) tạo **low của ngày** → rồi distribution lên suốt phần còn lại. Bias bearish đối xứng.
- Hệ quả thực chiến quan trọng nhất: **bias bullish = tìm mua Ở DƯỚI midnight open, không mua đuổi phía trên open.** Giá đang ở trên open mà bias bullish → mình đã trễ; chờ retrace về/dưới open hoặc bỏ ngày đó. Discipline này một mình nó loại bỏ phần lớn lệnh chase.
- Judas swing chính là chỗ **Daily Bias + Liquidity Sweep gặp nhau**: cú giả phá đầu London ngược bias là manipulation lấy nhiên liệu — không phải tín hiệu đổi bias. Ai không có khung PO3 sẽ bị chính cú Judas đá văng khỏi bias đúng.
- Tham chiếu thứ hai: **08:30 NY** (giờ tin) và **09:30 NYSE open** — hai thời điểm thuật toán hay chạy manipulation leg cuối trước expansion thật của NY.

### 7.2. Weekly profile — bias ngày nằm trong bias tuần

Nến tuần cũng có PO3 riêng, và ngày trong tuần có “vai” khác nhau:

| Thành phần | Nội dung | Ứng dụng |
|---|---|---|
| **Weekly Open (Chủ nhật/Thứ 2)** | Mức tham chiếu manipulation của cả tuần | Tuần bullish: tìm mua **dưới weekly open**; tuần bearish: bán trên weekly open |
| **Low/High of Week** | Trong tuần bullish, low của tuần thường hình thành **Thứ 2–Thứ 4** (kinh điển: Thứ 3/Thứ 4 tại một HTF discount array) | Đầu tuần đi ngược bias tuần = ứng viên low-of-week đang hình thành, không phải lý do đổi bias |
| **Thứ 2** | Thường là ngày định hình range, dễ nhiễu | Giảm kỳ vọng, quan sát nhiều hơn trade |
| **Thứ 3–Thứ 4** | Xác suất cao nhất cho manipulation-rồi-expansion của tuần | Các ngày “ăn dày” nhất của ICT 2022 model |
| **Thứ 5–Thứ 6** | Thường đã tiêu thụ phần lớn weekly range; Thứ 6 hay consolidate/reverse | Cẩn trọng continuation muộn; chốt mục tiêu tuần |

Trước khi viết Daily Bias, trả lời câu hỏi tuần: **”Draw của TUẦN là gì, và hôm nay là ngày thứ mấy trong câu chuyện đó?”** Một daily bias bullish vào Thứ 3 khi tuần đang tìm low-of-week tại HTF discount có xác suất khác hẳn cùng bias đó vào chiều Thứ 5 khi weekly target đã gần hoàn thành.

### 7.3. Nguồn gốc bias: giá đang được “giao” giữa hai PD Array HTF nào?

Phương pháp bias sâu nhất của ICT không phải đọc HH/HL, mà là câu hỏi: **nến D1 hiện tại đang được delivery TỪ PD Array HTF nào ĐẾN PD Array HTF nào?**

```text
Quy trình 3 bước:
1. Monthly/Weekly: giá vừa phản ứng tại array nào? (W FVG? Monthly OB? Old high/low?)
2. Từ array đó, array ĐỐI DIỆN còn mở gần nhất là gì? → đó là draw
3. Daily Bias = hướng delivery giữa hai array này, chừng nào chưa tới đích / chưa bị acceptance phủ định
```

Cách nghĩ này giải quyết hai vấn đề kinh niên: (1) bias không đổi mỗi ngày theo màu nến — nó chỉ đổi khi **giá tới đích hoặc phá gốc**; (2) mọi tranh cãi “pullback hay reversal” quy về một câu: *giá đã hoàn thành hành trình giữa hai array chưa?* Chưa tới → pullback; tới rồi + displacement ngược → hợp lệ để xây bias mới.

### 7.4. News calendar & Seek and Destroy — khi nào bias “không được phép chắc chắn”

- **Tin tức là động cơ của manipulation.** CPI / FOMC / NFP không phá ICT model — chúng **là** nhiên liệu cho leg manipulation/expansion. Hành vi chuẩn: consolidation trước tin → spike quét liquidity một phía (thường ngược hướng thật) → displacement về draw thật. Vì vậy: có tin lớn trong ngày → kỳ vọng range co lại TRƯỚC tin và bias chỉ được “kích hoạt” SAU cú quét của tin.
- **FOMC (14:00 NY):** phiên sáng trước FOMC thường là fake range; nhiều ngày FOMC đầu phiên NY chỉ là setup mồi. Rule an toàn: ngày FOMC chỉ trade NY AM nếu setup hoàn hảo, hoặc đứng ngoài chờ 14:30+.
- **Seek & Destroy profile:** ngày giá quét CẢ HAI phía (lấy cả BSL lẫn SSL) rồi đóng giữa range — thường quanh holiday, ngày chờ tin, mùa hè thanh khoản mỏng. Dấu hiệu nhận sớm: London không tạo được displacement giữ hướng; NY quét ngược lại London ngay đầu phiên. Gặp profile này → bias vô nghĩa, dừng trade, bảo toàn vốn là “lệnh thắng” của ngày.

### 7.5. Bias có cấp độ tin cậy — không phải bias nào cũng đáng 0.5% risk

Thay vì Bullish/Bearish/Neutral nhị phân, chấm bias theo **tier**:

| Tier | Điều kiện | Risk cho phép |
|---|---|---|
| **A — Full conviction** | HTF array rõ hai đầu + đúng vị trí quadrant + weekly profile thuận + không có tin lớn chắn đường | Risk chuẩn (0.5%) |
| **B — Partial** | Narrative rõ nhưng thiếu 1 yếu tố (vd đúng draw nhưng giá đang giữa range; hoặc có tin 8:30 phía trước) | 1/2 risk, hoặc chỉ trade sau khi yếu tố thiếu được giải quyết |
| **C — Guessing** | Bias viết ra chủ yếu vì “muốn có bias”; bằng chứng mâu thuẫn | = Neutral. Không trade model reversal. Chỉ quan sát |

Ghi `bias_tier` vào pre-market note và journal. Sau 30+ ngày sẽ thấy rõ: phần lớn drawdown đến từ những ngày trade tier B/C với size của tier A.

### 7.6. Best Practices — Daily Bias

> [!success] Best Practices
> 1. **Viết bias TRƯỚC khi mở LTF.** Thứ tự cố định: Monthly/Weekly array → D1 range + draw → weekly profile/ngày thứ mấy → midnight open → rồi mới được mở M15/M5. Mở M5 trước là để chart “gợi ý” bias — ngược quy trình.
> 2. **Bias phải là một câu văn hoàn chỉnh có địa chỉ:** “Giá được giao từ [array A] tới [array B]; hôm nay kỳ vọng low hình thành dưới midnight open trong London KZ; invalid nếu D1 đóng dưới [level].” Không viết được câu này = tier C.
> 3. **Một bias = một kịch bản thời gian.** Kèm theo hướng, luôn ghi: cửa sổ nào kỳ vọng manipulation (London KZ? 8:30?), cửa sổ nào kỳ vọng expansion (NY AM?). Bias đúng hướng nhưng sai giờ vẫn thua.
> 4. **Không đổi bias trong phiên vì nến LTF.** Bias chỉ được cập nhật tại các “trạm”: sau khi draw bị hit, sau acceptance qua invalidation level, hoặc sang phiên mới. Mọi cảm giác muốn đổi bias giữa phiên → ghi ra giấy, không hành động.
> 5. **Check calendar trước, bias sau.** Ngày CPI/FOMC/NFP: đánh dấu cửa sổ cấm trade và kỳ vọng fake move trước tin ngay trong pre-market card.
> 6. **Chấm `bias_tier` (A/B/C) và scale risk theo tier** — không phải mọi ngày đều xứng đáng full risk.
> 7. **Đếm “one good trade”.** Bias tồn tại để tìm MỘT lệnh đúng vị trí đúng giờ mỗi ngày, không phải để trade cả ngày theo một hướng. Sau lệnh đạt target: dừng hoặc chỉ quản lý lệnh cũ.
> 8. **Nghiệm thu cuối ngày bằng 3 câu:** Bias đúng hay sai? Nếu đúng — mình có kiếm được tiền từ nó không, vì sao? Nếu sai — sai ở narrative hay ở kỷ luật? Ghi vào daily note; đây là dữ liệu quý nhất cho weekly review.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Khái niệm ICT chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**.

### A. Daily Bias (bắt buộc trước phiên)
- [ ] Tôi ghi rõ `Bullish / Bearish / Neutral`, không chỉ “cảm giác giá sẽ tăng/giảm”.
- [ ] Xác định đúng HTF dealing range bằng swing có displacement/BOS rõ.
- [ ] Ghi draw on liquidity chính và level mục tiêu cụ thể.
- [ ] Xác định giá ở Premium / Discount / Equilibrium của range đó.
- [ ] Có HTF/H1 POI phù hợp để kỳ vọng reaction.
- [ ] Ghi level/điều kiện invalidation của bias.
- [ ] Nếu bằng chứng mâu thuẫn, tôi chọn **Neutral** và không ép trade.

### B. Execution (chỉ khi giá tới POI)
- [ ] Giá đã vào POI và đúng vùng Premium/Discount cho hướng trade.
- [ ] Có liquidity sweep hợp lý trước khi tìm reversal LTF.
- [ ] Có MSS trên LTF.
- [ ] MSS xảy ra trong POI, không phải giữa range.
- [ ] Có displacement tạo FVG/Imbalance.
- [ ] Entry tại FVG/OB có stop loss logic.
- [ ] Target là liquidity rõ ràng; đường tới target không bị cản bởi liquidity gần hơn chưa xử lý.
- [ ] Risk/reward tối thiểu đạt kế hoạch.
- [ ] Không trade vì revenge / FOMO / muốn gỡ lệnh thua.
- [ ] Không vượt số lệnh / mức rủi ro tối đa trong ngày.

### C. Quy tắc “không có lệnh”
- [ ] Không có draw on liquidity rõ → không trade.
- [ ] Không có POI phù hợp → không trade.
- [ ] Không có sweep + MSS + displacement đúng thứ tự → không trade.
- [ ] Bias Neutral / Mixed → không cố tìm setup ICT 2022 reversal.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Xác định bias chỉ bằng HH/HL | “D1 tăng nên Long” nhưng không có target/POI | Trend có thể đang chạy vào liquidity để phân phối ngược | Luôn viết: range + location + target liquidity + invalidation |
| Vào lệnh trước liquidity sweep | Giá chưa lấy đỉnh/đáy rõ ràng đã vào | Stop thường nằm đúng nơi market còn muốn quét | Chờ sweep + reclaim/reaction + displacement |
| MSS không nằm trong POI | Thấy displacement ở giữa range | Đó có thể chỉ là internal repricing/pullback | Chỉ xét MSS khi giá đã chạm HTF/H1 POI |
| Xác định sai dealing range | Chọn swing quá nhỏ hoặc quá cũ | Premium/Discount bị sai, dẫn tới mua premium / bán discount | Ưu tiên swing tạo displacement/BOS và phù hợp narrative đang chạy |
| Nhầm pullback với đảo chiều | Một M5/H1 break ngược hướng làm đổi bias | LTF structure không đủ phủ định HTF delivery | Xác định timeframe nào có quyền invalid bias; thường là H1/H4/D1 tùy thesis |
| Trade ngược bias | LTF đẹp nhưng HTF không ủng hộ | Target ngược hướng thường không đủ room, xác suất thấp | Chỉ trade counter-trend khi có playbook/backtest riêng; nếu không, bỏ qua |
| Chỉ bám một bias cả ngày | Thị trường đã hit target và chuyển delivery nhưng vẫn cố chấp | Bias là hypothesis có invalidation, không phải niềm tin | Reassess sau target lớn bị lấy hoặc HTF displacement ngược xuất hiện |
| Không chấp nhận Neutral | Cố chọn Long/Short khi D1 và H1 mâu thuẫn | Sinh FOMO, overtrading và narrative gượng ép | Ghi “Neutral” như một output chính thức trong pre-market plan |
| Chase sau displacement | Long ở premium sau bullish expansion / Short ở discount sau bearish expansion | R:R xấu và dễ vào lúc market retrace | Chờ retrace về FVG/OB phù hợp hoặc bỏ qua |
| Target tùy ý | TP theo số pip cố định, không theo liquidity | Không đồng bộ với price delivery | Đặt TP quanh liquidity rõ: internal trước, external sau |

---

## 10. Câu hỏi tự kiểm tra

- Mình có thể giải thích Daily Bias trong 30 giây không?
- Daily Bias của mình dựa trên **HTF range, liquidity target, location, POI**, hay chỉ dựa trên màu nến/trendline?
- Target liquidity cụ thể của hôm nay là level nào? Nó đã bị lấy chưa?
- Giá đang ở Premium, Discount hay Equilibrium của **range nào**?
- H1 ngược D1 là pullback vào POI hay một reversal có đủ bằng chứng?
- Điều gì, ở timeframe nào, sẽ invalid Daily Bias của mình?
- M5 MSS này có xuất hiện sau sweep và trong POI không?
- Nếu không có lệnh hôm nay, lý do “No Trade” của mình là gì?
- Setup nào trong trade journal đã áp dụng đúng/sai Daily Bias?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Daily Bias dùng để làm gì?  
**Đáp:** Xác định hướng giao dịch ưu tiên trong ngày và phía liquidity có xác suất trở thành draw on liquidity; nó lọc Long/Short/No Trade nhưng không phải entry trigger.

### Q2
**Hỏi:** Bốn thành phần tối thiểu để viết một Daily Bias là gì?  
**Đáp:** HTF dealing range, vị trí Premium/Discount, draw on liquidity rõ ràng và POI/điều kiện invalidation.

### Q3
**Hỏi:** Bullish D1 có đồng nghĩa được phép Long mọi M5 setup không?  
**Đáp:** Không. Chỉ tìm Long khi giá đến discount/bullish POI, có liquidity event phù hợp, rồi LTF MSS + displacement xác nhận.

### Q4
**Hỏi:** Khi nào một M5 MSS không đáng trade?  
**Đáp:** Khi nó xảy ra giữa range, ngoài HTF POI, trước liquidity sweep, không có displacement rõ, hoặc ngược HTF narrative mà không có counter-trend playbook.

### Q5
**Hỏi:** Khi nào nên chọn Neutral?  
**Đáp:** Khi liquidity target không rõ, price ở equilibrium/chop, HTF evidence mâu thuẫn không giải thích được, hoặc target chính đã được delivered và chưa có narrative mới.

### Q6
**Hỏi:** Điều gì làm Daily Bias bị invalid?  
**Đáp:** Điều kiện xây thesis bị phá: HTF POI bị acceptance xuyên qua, target/narrative đã hoàn thành rồi HTF displacement đổi delivery, hoặc level invalidation đã xác định từ trước bị vi phạm.

---

## 12. Lesson Learned

### Bài học chính
- Daily Bias là **narrative có thể bị phủ định**, không phải nhãn cố định cho cả ngày.
- Một bias tốt phải có **mục tiêu liquidity cụ thể**; “giá đang tăng” chưa phải là một thesis hoàn chỉnh.
- LTF entry chỉ có giá trị khi xuất hiện sau đúng sequence: POI → liquidity event → MSS → displacement → FVG/OB entry.
- Không có setup là quyết định tốt khi price ở equilibrium hoặc narrative không rõ.
- Chất lượng của bias phải được đo bằng trade journal và backtest, không bằng một vài lệnh thắng/thua gần đây.

### Quy tắc cá nhân rút ra
- [ ] Tôi không ghi Bullish/Bearish nếu chưa viết được: `range + location + draw on liquidity + POI + invalidation`.
- [ ] Tôi không vào lệnh chỉ vì M5 MSS; MSS phải ở trong POI sau liquidity sweep.
- [ ] Khi Daily Bias Neutral, tôi không cố trade ICT 2022 model.
- [ ] Tôi chỉ đổi Daily Bias khi điều kiện invalidation ở timeframe đã định trước xuất hiện, không vì cảm xúc sau một nến nhỏ.
- [ ] Sau khi target liquidity chính bị hit, tôi dừng và đánh giá lại narrative trước khi tìm lệnh tiếp.

### Câu nhắc nhở khi trade
> **“Đừng hỏi M5 đang muốn đi đâu. Hãy hỏi HTF đang cần lấy liquidity nào, và chỉ dùng M5 để tham gia tại đúng vị trí.”**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt được bias, POI và entry trigger không? |
| Nhận diện trên chart |  | Có đánh dấu đúng HTF dealing range và draw on liquidity không? |
| Biết khi nào bỏ qua |  | Có dám ghi Neutral / No Trade khi evidence mâu thuẫn không? |
| Kết hợp với context HTF |  | H1 pullback và H1 reversal có được phân biệt rõ không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra tại POI sau sweep + MSS + displacement không? |
| Review sau trade |  | Có kiểm tra bias đúng/sai bằng dữ liệu journal thay vì cảm xúc không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Daily Bias]]`.
- [ ] Review riêng các lệnh **aligned**, **counter-trend**, và **neutral nhưng vẫn trade**.
- [ ] Thống kê win rate, average R, lỗi lặp lại theo `bias_alignment`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.
