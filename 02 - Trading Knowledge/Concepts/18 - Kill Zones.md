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
updated: 2026-07-03
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

### Nâng cao — Bảng quy đổi giờ Kill Zone sang giờ Việt Nam (UTC+7) và ảnh hưởng của Daylight Saving Time (DST)

Đây là chỗ trader Việt Nam sai nhiều nhất: không phải sai khái niệm Kill Zone, mà sai **quy đổi giờ**. ICT dạy theo giờ New York (EST/EDT), trong khi Việt Nam dùng UTC+7 quanh năm và **không có DST**. Kết quả là cùng một Kill Zone, giờ Việt Nam sẽ lệch **đúng 1 tiếng** tùy thời điểm trong năm — nếu không để ý, bạn dễ canh lệnh sai giờ cả tháng liền mà không nhận ra.

Mỹ chuyển giờ hai lần mỗi năm: "spring forward" vào Chủ Nhật thứ hai của tháng 3 (chuyển sang EDT, UTC−4 — mùa hè) và "fall back" vào Chủ Nhật đầu tháng 11 (chuyển về EST, UTC−5 — mùa đông). Vì Việt Nam đứng yên ở UTC+7, khoảng cách giờ giữa New York và Việt Nam **co giãn theo mùa của Mỹ**, không theo mùa của Việt Nam.

![[KillZone-Advanced-DST-Conversion.svg]]
*So sánh giờ Việt Nam của từng Kill Zone giữa hai chế độ: mùa hè Mỹ (EDT, UTC−4, Việt Nam = giờ NY + 11 giờ) và mùa đông Mỹ (EST, UTC−5, Việt Nam = giờ NY + 12 giờ). Toàn bộ các mốc dịch lùi thêm 1 giờ khi Mỹ chuyển sang giờ mùa đông.*

| Kill Zone (giờ New York) | Giờ VN — mùa hè Mỹ (EDT) | Giờ VN — mùa đông Mỹ (EST) |
|---|---|---|
| Asian Range 20:00–00:00 | 07:00–11:00 | 08:00–12:00 |
| London Open KZ 02:00–05:00 | 13:00–16:00 | 14:00–17:00 |
| Silver Bullet London 03:00–04:00 | 14:00–15:00 | 15:00–16:00 |
| New York AM KZ 07:00–10:00 | 18:00–21:00 | 19:00–22:00 |
| Silver Bullet NY AM 10:00–11:00 | 21:00–22:00 | 22:00–23:00 |
| NY Lunch (vùng chết) 11:30–13:00 | 22:30–00:00 | 23:30–01:00 |
| London Close KZ 10:00–12:00 | 21:00–23:00 | 22:00–00:00 |

> [!warning] Quy tắc kiểm tra nhanh chế độ nào đang áp dụng
> Mỹ ở **giờ mùa hè (EDT)** khoảng từ Chủ Nhật thứ hai tháng 3 đến Chủ Nhật đầu tháng 11; phần còn lại của năm là **giờ mùa đông (EST)**. Ngày chuyển chính xác thay đổi mỗi năm — luôn tra lại lịch DST của Mỹ cho năm hiện tại trước khi tự quy đổi bằng trí nhớ. Cách an toàn nhất vẫn là **set đồng hồ chart theo New York time** thay vì tự cộng trừ giờ tay, vì phần lớn nền tảng chart tự động xử lý DST đúng.

### Nâng cao — Chồng lấp Kill Zone (session overlap) và mức biến động tương đối

Các Kill Zone không tồn tại độc lập — một số cửa sổ **chồng lấp lên nhau**, và đó thường là nơi thanh khoản dồn về nhiều nhất trong ngày. Hiểu phần chồng lấp giúp bạn biết nên "căng mắt" nhất vào lúc nào nếu chỉ có thời gian theo dõi một phần trong ngày.

![[KillZone-Advanced-SessionOverlap.svg]]
*NY AM Kill Zone (07:00–10:00 EST) và London Close Kill Zone (10:00–12:00 EST) nối tiếp/giao nhau quanh mốc 10:00; toàn bộ khung 07:00–10:00 là lúc London (đang đóng) và New York (vừa mở, gồm cả giờ mở cửa NYSE 09:30) cùng hoạt động — vùng được nhiều nguồn ICT coi là khối lượng giao dịch lớn nhất trong ngày.*

Về bản chất, "London Close KZ" theo ICT (10:00–12:00 EST) là phần **cuối phiên London** chồng vào **đầu phiên New York**; còn toàn bộ khối 07:00–10:00 EST (London vẫn mở tới ~11:30 giờ London, New York vừa mở) là vùng chồng lấp rộng hơn với khối lượng lệnh cao. Đây cũng là lý do NY AM KZ được nhiều nguồn ICT xem là Kill Zone có xác suất cao nhất trong ngày.

Xếp hạng biến động tương đối theo thị trường (định tính, **không phải số liệu đo được** — cần backtest xác nhận trên dữ liệu thật của chính bạn):

| Thị trường | Kill Zone thường "nóng" nhất (tương đối) | Ghi chú |
|---|---|---|
| **NQ1 / NAS100** | NY AM (đặc biệt quanh giờ mở cửa NYSE 09:30) > London Open > London Close > NY PM | Chỉ số Mỹ nhạy nhất với phiên Mỹ mở cửa |
| **EURUSD / GBPUSD** | London Open & vùng chồng lấp NY AM/London Close > NY AM thuần > NY PM | Cặp tiền châu Âu nhạy với London hơn NAS100 |
| **XAUUSD** | NY AM (tin Mỹ như CPI/NFP) & London Open thường biến động mạnh > London Close > NY PM | Vàng phản ứng mạnh với tin vĩ mô Mỹ rơi vào NY AM |

> [!warning] Đừng biến bảng này thành luật cứng
> Đây là xu hướng chung được nhiều tài liệu ICT mô tả, **không phải thống kê đo trên tài khoản của bạn**. Biến động thực tế còn phụ thuộc lịch tin, mùa thị trường (kỳ nghỉ lễ, thanh khoản mỏng cuối năm), và đặc thù từng broker/sàn. Hãy tự backtest và log `kill_zone_traded` cho từng lệnh trên NQ1, EURUSD, GBPUSD, XAUUSD trước khi kết luận cửa sổ nào thực sự phù hợp với bạn.

### Nâng cao — ICT Macro Times (khung 20 phút) lồng bên trong Kill Zone

Bên trong mỗi Kill Zone (cửa sổ rộng vài giờ), ICT còn dạy một lớp timing hẹp hơn gọi là **Macro** — các cửa sổ khoảng **20 phút**, thường nằm quanh ranh giới giờ (ví dụ 10 phút cuối của một giờ + 10 phút đầu giờ kế tiếp), nơi thuật toán được cho là "khởi động" một nhịp di chuyển giá mới. Macro không thay thế Kill Zone hay Silver Bullet — nó là một lớp tinh chỉnh **bên trong** khung đã chọn.

![[KillZone-Advanced-SilverBulletMacro.svg]]
*Quan hệ lồng nhau ba cấp: NY AM Kill Zone (07:00–10:00 EST, cửa sổ rộng nhất) chứa Silver Bullet NY AM (10:00–11:00 EST, cửa sổ 1 giờ chọn lọc hơn), và bên trong/quanh đó là các Macro ~20 phút (ví dụ 09:50–10:10, 10:50–11:10 EST) — lớp timing hẹp nhất.*

Cách các lớp lồng vào nhau:

| Cấp độ | Độ rộng cửa sổ | Ví dụ (giờ NY) | Vai trò |
|---|---|---|---|
| **Kill Zone** | Vài giờ | NY AM 07:00–10:00 | Xác định NGÀY/PHIÊN nào đáng săn entry |
| **Silver Bullet** | 1 giờ | NY AM 10:00–11:00 | Cửa sổ hẹp hơn để tìm FVG entry chọn lọc |
| **Macro** | ~20 phút | 09:50–10:10, 10:50–11:10 | Tinh chỉnh THỜI ĐIỂM vào lệnh trong khung trên |

> [!note] So sánh với phần Silver Bullet đã có ở Mục 1
> Ghi chú này **không thay đổi** giờ Silver Bullet đã nêu ở đầu note (03:00–04:00 / 10:00–11:00 / 14:00–15:00 EST) — Macro chỉ là một lớp phân tích bổ sung, chi tiết hơn, nằm bên trong hoặc lân cận các cửa sổ đó. Nếu bạn chưa quen dùng Macro, không bắt buộc phải thêm vào quy trình — Kill Zone + Silver Bullet vẫn là hai lớp chính đã đủ dùng cho phần lớn setup ICT 2022 Model.

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

### Giải phẫu — Dòng thời gian 24 giờ của các Kill Zone
![[KillZone-Anatomy.svg]]

**Mô tả:**
Toàn bộ các Kill Zone chính đặt trên một dòng thời gian 24 giờ duy nhất theo giờ New York, kèm hàng giờ Việt Nam (mùa hè EDT) ngay bên dưới để đối chiếu nhanh. Asian Range nằm về đêm giờ NY (sáng giờ VN); London Open và Silver Bullet London nối tiếp; NY AM KZ (chứa Silver Bullet NY AM) và London Close KZ chồng lấp quanh mốc 10:00; NY Lunch là vùng chết xen giữa NY AM và NY PM.

**Vì sao nên nhìn cả ngày trên một trục:**
- Thấy rõ **thứ tự** các KZ diễn ra trong ngày, không chỉ từng ô rời rạc.
- Thấy được **vùng chồng lấp** (NY AM / London Close) và **vùng chết** (NY Lunch) nằm ở đâu tương đối với nhau.
- Dễ đối chiếu chéo giờ Việt Nam mà không cần tính tay mỗi lần mở chart.

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

## Best Practices

> [!success] Nguyên tắc vàng
> **Kill Zone chỉ có giá trị khi giờ quy đổi ĐÚNG.** Một setup hoàn hảo canh sai giờ 1 tiếng vì quên DST cũng vô dụng như một setup không có sweep. Luôn xác nhận giờ trước, xác nhận context sau.

1. **Luôn kiểm tra chế độ DST của Mỹ (EDT hay EST) trước khi quy đổi Kill Zone sang giờ Việt Nam.** Vì Việt Nam không có DST, khoảng cách giờ với New York co giãn 1 tiếng tùy mùa (+11h mùa hè Mỹ, +12h mùa đông Mỹ) — xem bảng quy đổi ở Mục 3. Ghi trường `dst_regime: summer|winter` vào kế hoạch trade mỗi ngày để không bao giờ phải đoán.
2. **Ưu tiên set chart theo New York time thay vì tự cộng trừ giờ tay.** Hầu hết nền tảng chart tự xử lý DST chính xác; tự tính nhẩm là nguồn lỗi phổ biến nhất khi mới học Kill Zone. Nếu bắt buộc dùng giờ địa phương, đối chiếu lại bảng quy đổi mỗi lần Mỹ chuyển giờ (tháng 3 và tháng 11).
3. **Tránh vào lệnh ở các khung giờ thanh khoản thấp ngoài Kill Zone** — đặc biệt NY Lunch (11:30–13:00 EST), đêm khuya FX, và cuối phiên NY. Đây là nơi giá thường chỉ chop/whipsaw dù setup nhìn "đẹp" trên chart. Log `kill_zone_traded` (hoặc `dead_zone: true`) cho mỗi lệnh để sau này lọc ra và đo win rate riêng của nhóm trade ngoài giờ.
4. **Hiểu rõ các cửa sổ chồng lấp (overlap) và tận dụng chúng khi có thể** — đặc biệt vùng NY AM / London Close quanh mốc 10:00 EST, nơi nhiều nguồn ICT cho là khối lượng giao dịch cao nhất trong ngày (xem Mục 3). Đây thường là ưu tiên số một nếu bạn chỉ có thời gian theo dõi một cửa sổ mỗi ngày.
5. **Dùng Silver Bullet như một sub-window cụ thể (10:00–11:00 EST cho NY AM), không phải cách gọi khác của cả NY AM KZ.** Nhầm hai khái niệm khiến bạn mở rộng "Silver Bullet" ra 3 tiếng thay vì 1 tiếng chọn lọc — làm giảm chất lượng bộ lọc thời gian. Nếu dùng thêm ICT Macro (~20 phút, xem Mục 3), coi đó là lớp tinh chỉnh bên trong Silver Bullet, không phải thay thế nó.
6. **Không ép có lệnh chỉ vì đang trong Kill Zone.** KZ là điều kiện CẦN, không phải ĐỦ — vẫn phải có bias, sweep, và POI đúng như checklist ở Mục 8. Ghi lại số lần bạn "ép lệnh trong KZ" vào `common_mistakes` liên kết tới [[Mistake - Trade Outside Killzone]] nếu việc này lặp lại.
7. **Backtest và so sánh hiệu suất theo từng Kill Zone cho đúng thị trường bạn giao dịch (NQ1, EURUSD, GBPUSD, XAUUSD).** Bảng xếp hạng biến động tương đối ở Mục 3 chỉ là định tính từ tài liệu ICT chung — không phải số đo trên tài khoản của bạn. Sau 20–30 mẫu, so sánh win rate/average R giữa London Open, NY AM, London Close cho từng thị trường, và chỉ giữ lại Kill Zone thực sự chứng minh được edge cho phong cách của bạn.
8. **Liên kết lại với [[02 - AMD]] và [[19 - Liquidity]] mỗi khi review.** Kill Zone chỉ là một trục trong bộ ba Time–Price–Liquidity; đánh giá một trade không nên dừng ở "có đúng giờ không" mà phải hỏi thêm "đúng pha AMD chưa, đúng liquidity chưa".

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
