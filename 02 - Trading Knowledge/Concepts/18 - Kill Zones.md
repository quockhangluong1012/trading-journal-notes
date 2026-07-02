---
type: ict-concept
concept: Kill Zones
aliases:
  - Kill Zones
  - Killzone
  - KZ
  - London Kill Zone
  - New York Kill Zone
  - Silver Bullet
tags:
  - trading/ict/concept
  - trading/study
  - "#KillZones"
status: developing
category: Time & Price
timeframes:
  - H1
  - M15
  - M5
  - M1
models:
  - "[[Trading Journal/02 - Trading Knowledge/Models/ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-06-22
common_mistakes:
  - "[[Mistake - Trade Outside Killzone]]"
  - "[[Mistake - Trade Dead Zone Chop]]"
  - "[[Mistake - Wrong Timezone Conversion]]"
---

# Kill Zones

> [!summary] Tóm tắt 1 câu
> **Kill Zones là các khung giờ xác suất cao trong ngày (London Open, New York Open, London Close, Silver Bullet) khi thanh khoản và biến động tập trung, nơi các setup ICT đáng tin cậy nhất thường hình thành — là yếu tố "thời gian" bổ sung cho "giá".**

> [!important] Nguyên tắc cốt lõi
> **Thời gian cũng quan trọng như giá. Một setup đẹp xuất hiện NGOÀI kill zone (giờ chết / lunch) có xác suất thấp hơn nhiều. Chỉ săn entry trong kill zone; ngoài giờ thì quan sát, không trade.**
> Giờ ICT tính theo New York time (EST/EDT). Bạn PHẢI quy đổi đúng về giờ địa phương, đặc biệt khi Mỹ đổi giờ tiết kiệm ánh sáng (DST).

---

## 1. Định nghĩa

**Khái niệm:**
Kill Zone là một **cửa sổ thời gian** trong ngày mà ICT cho rằng xác suất xuất hiện move chất lượng cao là lớn nhất — do trùng với lúc các trung tâm tài chính lớn mở cửa, thanh khoản dồi dào và "smart money" hoạt động mạnh. Thay vì trade cả ngày, ICT khuyến nghị chỉ tập trung vào vài giờ vàng này.

**Các Kill Zone chính (giờ New York — EST):**

| Kill Zone | Giờ New York (EST) | Đặc điểm |
|---|---|---|
| **Asian Range** | 20:00 – 00:00 | Thường là **accumulation** (range hẹp); đánh dấu Asian high/low làm liquidity |
| **London Open KZ** | 02:00 – 05:00 | Thường là **manipulation/đầu distribution**; move mạnh đầu tiên trong ngày |
| **New York AM KZ** | 07:00 – 10:00 | Phiên Mỹ mở; thường có Judas riêng rồi distribution chính |
| **London Close KZ** | 10:00 – 12:00 | Hồi/đảo cuối phiên London; cơ hội reversal |
| **Silver Bullet** | 03:00–04:00 / 10:00–11:00 / 14:00–15:00 | Cửa sổ 1 giờ "súng bạc" — tìm FVG entry rất chọn lọc |

> [!note]
> Giờ trên là **New York time**. Khi Mỹ ở giờ mùa hè (EDT, GMT−4) các mốc giữ nguyên theo NY nhưng lệch 1 giờ so với GMT. **Quy đổi sang giờ Việt Nam (GMT+7):**
> - London Open KZ 02:00–05:00 EST ≈ **14:00–17:00** giờ VN (mùa đông) / **13:00–16:00** (mùa hè).
> - New York AM KZ 07:00–10:00 EST ≈ **19:00–22:00** giờ VN (mùa đông) / **18:00–21:00** (mùa hè).
> - Silver Bullet NY 10:00–11:00 EST ≈ **22:00–23:00** giờ VN (mùa đông).
> Luôn kiểm tra DST của Mỹ; tốt nhất là set chart theo New York time để khỏi nhầm.

**Mục đích trong ICT:**
- Lọc **khi nào** được phép săn entry → tăng chất lượng, giảm số lệnh.
- Ghép với [[02 - AMD]]: London KZ ~ manipulation, NY KZ ~ distribution.
- Định khung cho **Silver Bullet** và các model phụ thuộc thời gian.
- Tránh các "vùng chết" (NY lunch, cuối phiên) nơi giá đi ngang/whipsaw.

**Vì sao khái niệm này quan trọng:**
Nhiều trader có hệ thống tốt nhưng vẫn thua vì trade SAI GIỜ — vào lệnh lúc thanh khoản kém, giá chỉ chop. Kill Zone là bộ lọc thời gian: cùng một setup, trong kill zone thì chạy, ngoài kill zone thì chết. Nó cũng giúp kỷ luật: bạn chỉ cần "có mặt" vài giờ, không phải dán mắt cả ngày.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Bây giờ có phải giờ đáng săn entry không (trong KZ hay vùng chết)?
- Move vừa rồi xảy ra trong kill zone nào → độ tin cậy ra sao?
- Asian range high/low (liquidity) ở đâu để chờ London quét?
- Setup này có nằm trong cửa sổ Silver Bullet không?

### Kill Zones không phải là gì
- Không phải "cứ trong kill zone là có lệnh" — vẫn cần đủ context (bias, sweep, POI).
- Không phải đảm bảo move sẽ xảy ra; có ngày KZ vẫn yên ắng.
- Không phải cố định tuyệt đối theo phút; là cửa sổ, đọc price action bên trong.
- Không miễn trừ quản trị rủi ro.
- Không giống nhau cho mọi thị trường (FX, indices, vàng có giờ "nóng" hơi khác).

---

## 2. Bối cảnh sử dụng

### Vai trò từng Kill Zone trong ngày

| Kill Zone | Vai trò AMD điển hình | Cách dùng |
|---|---|---|
| **Asian Range** | Accumulation | Đánh dấu high/low Á (liquidity); KHÔNG trade breakout |
| **London Open** | Manipulation → distribution | Chờ Judas quét Asian liquidity, vào theo phân phối |
| **New York AM** | Judas NY → distribution | Chờ sweep đầu NY, vào theo hướng bias; nhiều move chính ở đây |
| **London Close** | Reversal / profit-taking | Cơ hội đảo chiều khi London đóng |
| **Silver Bullet** | Cửa sổ FVG 1 giờ | Tìm FVG entry chọn lọc trong khung hẹp |

> [!tip]
> Cặp combo phổ biến: **Asian range (liquidity) → London KZ quét + displacement → NY AM tiếp diễn về target**. Đánh dấu Asian high/low mỗi ngày là một thói quen rất đáng giá.

### Khi nào khái niệm này có giá trị cao?
- [ ] Setup hình thành **trong** một kill zone (đặc biệt London Open / NY AM).
- [ ] Kill zone trùng với pha distribution của [[02 - AMD]].
- [ ] Có sweep liquidity + displacement xảy ra ngay trong KZ.
- [ ] Bias rõ và move trong KZ đồng hướng bias.
- [ ] Thị trường đang trong mùa "có biến động" (không phải kỳ nghỉ lễ).

### Khi nào nên bỏ qua?
- [ ] Ngoài kill zone: NY lunch (11:30–13:00), cuối phiên NY, đêm khuya FX.
- [ ] Asian session với ý định trade breakout.
- [ ] Ngày lễ / thanh khoản thấp (giá chop kể cả trong KZ).
- [ ] Tin tức lớn sắp ra trong KZ → chờ qua tin.
- [ ] Không có context (bias/sweep/POI) dù đang trong KZ.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Đánh dấu các KZ trên chart:** dùng chỉ báo session/killzone hoặc vẽ vùng giờ (theo NY time).
2. **Asian range:** xác định high/low phiên Á (liquidity hai phía).
3. **Hành vi đầu London:** quan sát Judas/sweep ngay khi London mở.
4. **Displacement trong KZ:** move mạnh + MSS xảy ra bên trong cửa sổ giờ.
5. **Vùng chết:** nhận ra các khoảng đi ngang/whipsaw ngoài KZ để tránh.

### Ma trận nhận diện

| Thành phần | Tín hiệu chất lượng (trong KZ) | Cảnh báo (ngoài KZ) |
|---|---|---|
| **Thời điểm** | London Open / NY AM / Silver Bullet | NY lunch / đêm / cuối phiên |
| **Biến động** | Range mở rộng, nến thân lớn | Nến nhỏ, wick nhiều, đi ngang |
| **Cấu trúc** | Sweep + displacement + MSS rõ | Whipsaw, không cấu trúc |
| **Liquidity** | Quét Asian/PD liquidity rồi chạy | Lình xình quanh một mức |

### Điều kiện bắt buộc
- [ ] Chart set đúng theo New York time (hoặc quy đổi chính xác).
- [ ] Đã đánh dấu các kill zone và Asian range.
- [ ] Biết hiện đang ở KZ nào hay vùng chết.

### Điều kiện tăng xác suất
- [ ] Setup trong London Open / NY AM KZ.
- [ ] KZ trùng pha distribution AMD + đồng hướng bias.
- [ ] Có sweep + displacement + MSS trong cửa sổ giờ.
- [ ] Trùng cửa sổ Silver Bullet với một FVG sạch.

### Điều kiện làm setup yếu đi
- Move xảy ra cuối KZ (gần hết cửa sổ).
- Thanh khoản ngày thấp (lễ).
- Tin tức làm nhiễu trong KZ.
- Ép vào lệnh dù KZ không cho setup rõ.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Kill Zones
> 1. **Bây giờ là KZ nào (theo NY time), hay đang là vùng chết?**
> 2. **Asian range high/low (liquidity) ở đâu?**
> 3. **Trong KZ này đã có sweep + displacement đồng hướng bias chưa?**
> 4. **Nếu hết KZ mà chưa có setup, tôi có kỷ luật đứng ngoài không?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]) → hướng kỳ vọng cho move trong KZ.
- **Draw on liquidity:** pool HTF làm target cho distribution trong NY KZ.
- **Lịch tin tức:** đánh dấu tin lớn rơi vào KZ nào.

### H1 / M15 — POI & Context
- **Asian range:** đánh dấu high/low Á.
- **POI cho KZ:** FVG/OB nơi kỳ vọng London/NY phản ứng.
- **Kế hoạch theo giờ:** "London KZ chờ Judas quét Asian low → distribution lên về PDH".

### M5 / M1 — Confirmation & Entry
- **Trong cửa sổ KZ:** chờ sweep + reclaim + MSS + displacement → entry tại FVG/OB.
- **Silver Bullet:** trong khung 1 giờ, tìm FVG sạch sau một sweep nhỏ.
- **Stop/target:** stop ngoài cực điểm sweep; target pool liquidity HTF.
- **Hết KZ:** nếu cửa sổ đóng mà chưa có setup chuẩn → bỏ, chờ KZ sau.

```text
Mẫu ghi nhanh — Kế hoạch theo Kill Zone
Daily Bias: Bullish/Bearish
Asian range: [low]–[high] (liquidity)
London KZ (14:00–17:00 VN): chờ Judas sweep [pool] → distribution
NY AM KZ (19:00–22:00 VN): tiếp diễn về [target pool]
Silver Bullet (NY 10–11h / 22:00–23:00 VN): FVG entry nếu có
KZ được phép trade hôm nay: London / NY AM
Vùng chết cần tránh: NY lunch (~23:30–01:00 VN)
```

> [!warning]
> **Đừng "ép" có lệnh chỉ vì đang trong kill zone.** KZ là điều kiện CẦN, không phải ĐỦ. Vẫn phải có bias + sweep + POI + confirm. Nhưng tuyệt đối tránh vào lệnh NGOÀI kill zone.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Diễn ra trong một kill zone chính (London Open / NY AM) hoặc Silver Bullet.
- [ ] Có sweep + displacement + MSS trong cửa sổ giờ.
- [ ] Đồng hướng Daily Bias; có POI và target liquidity.
- [ ] Không vướng tin tức lớn làm nhiễu.
- [ ] Stop/target và R:R đạt kế hoạch.

### Setup bị vô hiệu (không trade) khi
- [ ] Ngoài kill zone (vùng chết / lunch / đêm).
- [ ] Trong KZ nhưng không có sweep/displacement rõ.
- [ ] Ngược bias hoặc không có POI.
- [ ] Thanh khoản ngày thấp / sát giờ tin lớn.
- [ ] Cửa sổ KZ đã gần hết.

### KZ "nóng" vs vùng chết

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Biến động mở rộng, cấu trúc rõ, đúng giờ KZ | **KZ nóng** | Săn entry theo plan |
| Nến nhỏ, đi ngang, ngoài KZ (lunch/đêm) | **Vùng chết** | Đứng ngoài, không trade |
| Trong KZ nhưng chưa có sweep/POI | **KZ chưa "kích hoạt"** | Chờ điều kiện, đừng ép |
| Tin lớn sắp ra trong KZ | **KZ rủi ro tin** | Chờ qua tin rồi đánh giá lại |

> [!note]
> Kill Zone là "trục thời gian" của bộ ba **Time–Price–Liquidity**: [[02 - AMD]] cho biết pha nào, Kill Zone cho biết giờ nào, còn [[19 - Liquidity]] cho biết giá bị hút về đâu. Một entry A+ thường là giao điểm của cả ba.

---

## 6. Ví dụ chart

### Ví dụ đúng — Setup A+ xuất hiện trong London Kill Zone
![[Kill-Zones-Example-Correct.png]]

**Mô tả:**
Phiên Á đi ngang (accumulation), đánh dấu Asian low làm SSL. Khi **London KZ (02:00–05:00 EST)** mở, giá quét SSL (sweep) rồi **displacement tăng** phá cấu trúc — đây là setup A+ đúng giờ. Entry trong cửa sổ London KZ; move tiếp tục mở rộng và **NY AM KZ** đẩy giá về BSL target. London Close là vùng nghỉ ngắn giữa hai KZ.

**Vì sao đây là ví dụ tốt:**
- Setup hình thành **trong kill zone** với biến động mở rộng.
- Trùng pha distribution của AMD, đồng hướng bias.
- Có sweep + displacement rõ trong cửa sổ giờ.
- Tận dụng cả London + NY KZ cho cùng một narrative.

### Ví dụ sai / dễ nhầm — Trade ngoài Kill Zone (NY lunch / vùng chết)
![[Kill-Zones-Example-Wrong.png]]

**Mô tả lỗi:**
Move chính đã xảy ra trong London KZ (đã bỏ lỡ). Trader vào lệnh trong **vùng chết NY lunch (11:30–13:00 EST)** — nơi thanh khoản kém, giá chỉ đi ngang và whipsaw. Lệnh bị "cưa" liên tục, stop bị quét dù không có xu hướng nào.

**Bài học:**
- Ngoài kill zone, ngay cả "setup đẹp" cũng kém xác suất.
- NY lunch và cuối phiên là vùng chết — quan sát, không trade.
- Nếu lỡ KZ chính, hãy chờ KZ kế tiếp thay vì ép lệnh trong giờ chết.

---
### Sequence mẫu — Long trong London/NY Kill Zone
```text
Daily Bias: Bullish
→ Asian range: đánh dấu Asian low (SSL)
→ London KZ mở: Judas/Sweep SSL
→ Displacement LÊN + MSS (trong KZ) → FVG
→ Entry tại FVG/OB (đồng hướng bias, trong cửa sổ giờ)
→ Stop dưới cực điểm sweep
→ NY AM KZ: giá tiếp diễn về BSL target
```

### Sequence mẫu — Silver Bullet (NY AM)
```text
Cửa sổ Silver Bullet NY 10:00–11:00 EST
→ Một sweep nhỏ quét liquidity gần
→ Displacement tạo FVG sạch trong cửa sổ 1 giờ
→ Entry tại FVG (đồng hướng bias)
→ Stop ngoài sweep; Target liquidity gần
→ Đóng/đánh giá khi hết cửa sổ
```

> [!note]
> Kill Zone định **KHI NÀO** săn; [[02 - AMD]] định **PHA**; [[20 - Liquidity Sweep]] là **TRIGGER**; [[Fair Value Gap]]/[[Optimal Trade Entry]] là **ĐIỂM VÀO**. Thiếu yếu tố thời gian, các model còn lại mất nhiều xác suất.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Kill zone là điều kiện CẦN. Trong KZ vẫn phải có bias + sweep + POI mới vào.

### A. Context (HTF)
- [ ] Chart set đúng New York time / đã quy đổi chuẩn (chú ý DST).
- [ ] Daily Bias đã rõ → hướng kỳ vọng cho KZ.
- [ ] Asian range high/low đã đánh dấu.
- [ ] Đã xem lịch tin tức rơi vào KZ nào.

### B. Execution (trong KZ)
- [ ] Đang trong kill zone chính (London Open / NY AM) hoặc Silver Bullet.
- [ ] Có sweep + displacement + MSS trong cửa sổ giờ.
- [ ] Entry đồng hướng bias, tại POI; stop ngoài sweep.
- [ ] Target là liquidity rõ; R:R đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Ngoài kill zone (lunch/đêm/cuối phiên) → không trade.
- [ ] Trong KZ nhưng không có sweep/POI → không trade.
- [ ] Sát giờ tin lớn → chờ qua tin.
- [ ] Cửa sổ KZ gần hết, chưa có setup → bỏ, chờ KZ sau.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade ngoài kill zone | Vào lệnh NY lunch / đêm | Thanh khoản kém, whipsaw | Chỉ săn trong London/NY KZ |
| Ép lệnh trong KZ | Vào dù không có sweep/POI | KZ là điều kiện cần, không đủ | Chờ đủ context mới vào |
| Sai quy đổi múi giờ | Đánh dấu KZ lệch giờ | Bỏ lỡ / vào sai cửa sổ | Set chart theo NY time; kiểm tra DST |
| Trade breakout Asian range | Mua/bán khi phá range Á | Range Á hay là vùng bẫy | Dùng Asian H/L làm liquidity, không breakout |
| Bỏ qua lịch tin | Vào ngay trước tin lớn | Biến động tin phá cấu trúc | Tránh vào sát giờ tin |
| FOMO sau khi lỡ KZ | Cố vào sau khi move đã chạy | Entry chase, R:R xấu | Chờ KZ tiếp theo |
| Ngồi cả ngày | Trade mọi giờ vì "có thời gian" | Quá nhiều lệnh chất lượng thấp | Chỉ "có mặt" trong vài KZ |

---

## 10. Câu hỏi tự kiểm tra

- Mình có kể được 4 kill zone chính và giờ của chúng (NY time + giờ VN) không?
- Bây giờ là KZ nào hay vùng chết?
- Asian range high/low hôm nay ở đâu?
- Move trong KZ này có sweep + displacement đồng hướng bias không?
- Có tin tức lớn nào rơi vào KZ hôm nay không?
- Setup này nằm trong cửa sổ Silver Bullet không?
- Nếu hết KZ mà chưa có setup, mình có kỷ luật đứng ngoài không?
- Lệnh gần đây có lệnh nào vào ngoài KZ và bị chop không?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Kill Zone là gì?
**Đáp:** Là các khung giờ xác suất cao trong ngày (London Open, NY AM, London Close, Silver Bullet) khi thanh khoản/biến động tập trung và setup ICT đáng tin cậy nhất thường hình thành.

### Q2
**Hỏi:** Giờ London Open KZ và NY AM KZ theo New York time là gì?
**Đáp:** London Open ≈ 02:00–05:00 EST; New York AM ≈ 07:00–10:00 EST.

### Q3
**Hỏi:** Asian range dùng để làm gì?
**Đáp:** Đánh dấu high/low phiên Á làm liquidity hai phía; thường bị London quét (Judas) trước khi distribution — KHÔNG trade breakout của nó.

### Q4
**Hỏi:** Silver Bullet là gì?
**Đáp:** Cửa sổ 1 giờ (vd 10:00–11:00 EST) để tìm FVG entry rất chọn lọc sau một sweep nhỏ.

### Q5
**Hỏi:** Kill zone là điều kiện cần hay đủ để vào lệnh?
**Đáp:** Chỉ là điều kiện CẦN. Trong KZ vẫn phải có bias + sweep + POI + confirm mới vào.

### Q6
**Hỏi:** Vì sao phải chú ý DST khi dùng kill zone?
**Đáp:** Giờ ICT theo New York; khi Mỹ đổi giờ (EST↔EDT), mốc quy đổi sang giờ địa phương lệch 1 giờ → dễ đánh dấu sai cửa sổ.

### Q7
**Hỏi:** Kill zone ghép với AMD thế nào?
**Đáp:** Asia ≈ accumulation, London Open ≈ manipulation/đầu distribution, NY AM ≈ distribution chính; mỗi pha gắn một cửa sổ giờ.

---
## 12. Lesson Learned

### Bài học chính
- **Thời gian quan trọng ngang giá.** Cùng một setup, trong KZ thì chạy, ngoài KZ thì chết.
- Bốn cửa sổ vàng: **London Open, NY AM, London Close, Silver Bullet** (giờ New York).
- **Asian range** là kho liquidity để London quét — đánh dấu mỗi ngày.
- Kill zone là điều kiện **cần, không đủ**: vẫn phải có bias + sweep + POI.
- **Quy đổi múi giờ** cẩn thận (DST); tốt nhất set chart theo NY time.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ săn entry trong London Open / NY AM KZ (và Silver Bullet).
- [ ] Tôi đánh dấu Asian high/low mỗi ngày làm liquidity.
- [ ] Tôi không trade trong vùng chết (NY lunch / đêm / cuối phiên).
- [ ] Tôi không ép lệnh chỉ vì đang trong KZ — phải đủ context.
- [ ] Tôi kiểm tra DST và set chart theo New York time.

### Câu nhắc nhở khi trade
> **"Đúng giờ rồi mới nói đến đúng giá. Ngoài kill zone, tôi chỉ quan sát."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có nhớ các KZ + giờ NY + quy đổi giờ VN không? |
| Nhận diện trên chart |  | Có phân biệt KZ nóng vs vùng chết không? |
| Biết khi nào bỏ qua |  | Có kỷ luật đứng ngoài khi ngoài KZ không? |
| Kết hợp với context HTF |  | KZ có ghép với bias + AMD + liquidity không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự rơi trong KZ không? |
| Review sau trade |  | Có so sánh expectancy theo KZ bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[Kill Zones]]`.
- [ ] Review riêng: `in_killzone` true vs false; London vs NY.
- [ ] Thống kê win rate, average R theo `killzone`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## Appendix — Kill Zones Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish / Neutral
> **Chart timezone:** New York (EST/EDT)
> **Asian range:** [low]–[high]
> **KZ hôm nay được phép trade:** London Open / NY AM / London Close / Silver Bullet
> **London Open KZ:** 02:00–05:00 EST (≈14:00–17:00 VN đông / 13:00–16:00 VN hè)
> **New York AM KZ:** 07:00–10:00 EST (≈19:00–22:00 VN đông / 18:00–21:00 VN hè)
> **Silver Bullet:** 10:00–11:00 EST (≈22:00–23:00 VN đông)
> **Tin tức trong KZ?** Yes / No — giờ: ____
> **Vùng chết cần tránh:** NY lunch 11:30–13:00 EST
> **Plan theo giờ:**
> **No-trade condition:**
