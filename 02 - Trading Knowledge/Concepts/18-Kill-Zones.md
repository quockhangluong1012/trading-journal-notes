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
status: tested
category: Time & Price
timeframes:
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-07-12
created: 2026-06-22
updated: 2026-07-28
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

![[KillZone-Advanced-DST-Conversion.svg|697]]
*So sánh giờ Việt Nam của từng Kill Zone giữa hai chế độ: mùa hè Mỹ (EDT, UTC−4, Việt Nam = giờ NY + 11 giờ) và mùa đông Mỹ (EST, UTC−5, Việt Nam = giờ NY + 12 giờ). Toàn bộ các mốc dịch lùi thêm 1 giờ khi Mỹ chuyển sang giờ mùa đông.*

| Kill Zone (giờ New York)         | Giờ VN — mùa hè Mỹ (EDT) | Giờ VN — mùa đông Mỹ (EST) |
| -------------------------------- | ------------------------ | -------------------------- |
| Asian Range 20:00–00:00          | 07:00–11:00              | 08:00–12:00                |
| London Open KZ 02:00–05:00       | 13:00–16:00              | 14:00–17:00                |
| Silver Bullet London 03:00–04:00 | 14:00–15:00              | 15:00–16:00                |
| New York AM KZ 07:00–10:00       | 18:00–21:00              | 19:00–22:00                |
| Silver Bullet NY AM 10:00–11:00  | 21:00–22:00              | 22:00–23:00                |
| NY Lunch (vùng chết) 11:30–13:00 | 22:30–00:00              | 23:30–01:00                |
| London Close KZ 10:00–12:00      | 21:00–23:00              | 22:00–00:00                |

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

---

## 14. Phân tích chuyên sâu: cơ chế thị trường đằng sau Kill Zones

![[KillZone-Deep-Mechanism.svg|720]]
*Cơ chế thật: Kill Zone không phải "giờ đẹp" tự nhiên của thị trường mà là hệ quả trực tiếp của việc các trung tâm tài chính lớn (Tokyo, London, New York) mở cửa nối tiếp theo múi giờ — nơi số lượng participant, order book depth và các thuật toán TWAP/VWAP theo lịch cùng hoạt động đồng thời tạo ra biến động thật, đo lường được qua volume.*

### Cơ chế orderflow/auction thực sự

Kill Zone không phải một khái niệm ICT phát minh ra từ đầu — nó là sự mô tả lại một hiện tượng orderflow đã được biết đến rộng rãi trong giới định lượng và market making từ trước: **biến động và thanh khoản trong ngày không phân bố đều mà tập trung quanh giờ mở cửa của các trung tâm tài chính lớn**.

- **Số lượng participant tăng đột biến khi một trung tâm mở cửa:** khi London mở cửa (tương ứng London Open KZ ICT), toàn bộ desk trading của các ngân hàng lớn tại London đồng thời vào ca, tạo ra một cú tăng volume có thể đo lường được trên bất kỳ dữ liệu volume thô (không cần biết gì về ICT). Đây là lý do khách quan cho "biến động mở rộng" mà note đã mô tả ở mục 3.
- **Order book depth mỏng hơn ngoài giờ (Asian range, NY lunch) khiến giá dễ bị đẩy bởi lệnh tương đối nhỏ:** vào NY lunch (11:30-13:00 EST), nhiều bàn trading lớn tạm nghỉ hoặc giảm hoạt động — order book mỏng hơn đáng kể, khiến ngay cả một lệnh trung bình cũng có thể tạo ra biến động bất thường (whipsaw) không phản ánh ý định thị trường thật, đúng như note đã liệt kê "vùng chết" ở mục 5.
- **TWAP/VWAP execution algorithms của các quỹ lớn thường được lập trình chạy theo cửa sổ giờ cố định** (ví dụ chia đều khối lượng mua/bán trong suốt phiên NY chính 09:30-16:00 ET) — sự tập trung của các algo này quanh giờ mở phiên chính thức NYSE (09:30 ET, nằm trong NY AM KZ) tạo ra một phần lý do khách quan khiến NY AM được nhiều nguồn ICT coi là kill zone "nóng" nhất.
- **ICT Macro (khung ~20 phút quanh ranh giới giờ) có thể liên quan đến hiện tượng "giờ tròn" trong thuật toán thực thi** — nhiều hệ thống order routing/algo cơ chế đơn giản dùng mốc giờ tròn (00, 15, 30, 45 phút hoặc đầu/cuối giờ) làm điểm khởi động lại chu trình, tạo ra một dạng "clustering" biến động quanh các mốc này — dù đây là suy luận hợp lý chứ không phải bằng chứng trực tiếp công khai từ chính các quỹ.
- **Gamma hedging của dealer quyền chọn chỉ số (SPX/NDX 0DTE)** có xu hướng tập trung điều chỉnh quanh giờ mở cửa và đóng cửa NYSE — góp phần vào biến động cao hơn tại NY AM KZ và cuối phiên, một cơ chế hoàn toàn độc lập với "Judas Swing" narrative của ICT nhưng tạo ra hiệu ứng quan sát tương tự.

### Đối chiếu với các khung lý thuyết khác

| Khung lý thuyết | Điểm trùng với Kill Zone | Điểm khác biệt |
|---|---|---|
| **Auction Market Theory (Market Profile)** | Khái niệm "Initial Balance" (60 phút đầu phiên) trong Market Profile gần như trùng khớp về ý tưởng với NY AM KZ — cả hai đều cho rằng biến động/thông tin đầu phiên có trọng số cao hơn để định hình xu hướng ngày. | Market Profile đo bằng phân phối giá theo thời gian (TPO/volume), không chia thành các "cửa sổ giờ cố định" như Kill Zone. |
| **Wyckoff** | Không có khái niệm tương đương trực tiếp — nhưng ý tưởng "Sign of Strength"/"Sign of Weakness" thường xuất hiện quanh các đợt tăng volume, thường trùng với giờ mở phiên lớn. | Wyckoff không gắn cấu trúc của mình với múi giờ cố định — hoàn toàn dựa trên volume và cấu trúc giá bất kể giờ nào. |
| **Orderflow/Footprint** | Volume profile theo giờ trong ngày (time-of-day volume analysis) là công cụ định lượng thực có thể xác nhận trực tiếp: volume trung bình tại 09:30-11:00 ET và 02:00-05:00 ET thường cao hơn rõ rệt so với 11:30-13:00 ET trên hầu hết chỉ số/FX majors. | Đây là công cụ đo lường trực tiếp bằng số liệu; Kill Zone của ICT là một phiên bản đơn giản hóa, định tính của cùng hiện tượng. |

### Điều kiện làm Kill Zone mạnh lên/yếu đi

- **Regime trending mạnh nhiều tuần:** Kill Zone vẫn có ý nghĩa về "khi nào nên theo dõi", nhưng move có thể tiếp diễn xuyên suốt nhiều KZ liên tiếp (không dừng lại đúng biên giờ) — nghĩa là ranh giới cửa sổ trở nên ít quan trọng hơn so với việc bắt đúng hướng trend.
- **Regime ranging:** đây là môi trường Kill Zone "sạch" nhất để quan sát AMD — accumulation Á, manipulation London, distribution NY diễn ra tuần tự rõ ràng.
- **Volatility cao do tin lớn (FOMC, NFP, CPI) rơi đúng giờ KZ:** biến động tăng vọt nhưng chất lượng cấu trúc (MSS rõ ràng, không bị "gai" bởi slippage) giảm — cần tách riêng "KZ có tin" và "KZ thường" khi đánh giá.
- **Volatility thấp mùa hè/kỳ nghỉ lễ:** ngay cả trong đúng cửa sổ KZ, giá vẫn có thể chỉ đi ngang nếu thanh khoản mùa đó thấp bất thường (tuần giữa Christmas-New Year là ví dụ điển hình).
- **Loại tài sản** quyết định cửa sổ nào "nóng" nhất khác nhau đáng kể (xem bảng dưới).

### Bảng so sánh hành vi Kill Zone trên 3 loại thị trường

| Tiêu chí | FX majors (EURUSD, GBPUSD) | Index futures (NQ/ES) | Crypto (BTC/ETH) |
|---|---|---|---|
| Cửa sổ "nóng" nhất | London Open, và vùng chồng lấp London Close/NY AM | NY AM, đặc biệt quanh giờ mở NYSE 09:30 ET | Không có cửa sổ cố định rõ ràng — biến động phân bố tương đối đều hơn nhưng vẫn có xu hướng tăng nhẹ quanh giờ mở phiên Mỹ/châu Á lớn |
| Vai trò Asian Range | Rất rõ — accumulation trước khi London quét | Ít rõ ràng hơn (thanh khoản futures qua đêm mỏng, ít "range" rõ để quét) | Không có "Asian range" ý nghĩa vì giao dịch liên tục, không có phiên riêng biệt đóng/mở |
| Silver Bullet có ý nghĩa không | Có, đặc biệt London AM 03:00-04:00 ET với FX majors | Có, NY AM 10:00-11:00 ET với FVG chỉ số rất phổ biến | Ý nghĩa thấp hơn — không có cấu trúc phiên rõ để tạo FVG "sạch" theo cùng logic |
| Ảnh hưởng ngày lễ | Lễ ngân hàng UK/EU ảnh hưởng London KZ; lễ Mỹ ảnh hưởng NY KZ | Rất mạnh — nửa phiên (half-day) làm biến động NY AM/PM giảm hẳn | Không ảnh hưởng trực tiếp (giao dịch liên tục), nhưng thanh khoản gián tiếp giảm nếu market maker truyền thống nghỉ lễ |
| Khuyến nghị | Theo đúng khung Kill Zone ICT, tin cậy cao | Theo đúng khung, đặc biệt chú ý NY AM | Coi Kill Zone truyền thống chỉ là gợi ý yếu; ưu tiên theo dõi thanh khoản thực tế + lịch tin vĩ mô Mỹ ảnh hưởng gián tiếp |

> [!tip] Chốt cơ chế
> Kill Zone có nền tảng thật trong hiện tượng "volume theo giờ trong ngày" — một khái niệm đã được xác nhận bằng dữ liệu định lượng từ lâu, độc lập với ICT. Điều ICT thêm vào là **khung diễn giải AMD (Accumulation-Manipulation-Distribution)** gắn với từng cửa sổ — phần này mang tính narrative nhiều hơn và khó kiểm chứng độc lập.

---

## 15. Phản biện & giới hạn (Critique)

### 1. Phản biện từ góc nhìn khoa học/quant

- **Tính chủ quan khi vẽ ranh giới:** các mốc giờ Kill Zone (02:00-05:00, 07:00-10:00...) là số tròn tiện lợi để nhớ, không phải kết quả của phân tích thống kê tối ưu hóa ranh giới chính xác — hai nguồn ICT khác nhau đôi khi cho khung giờ hơi khác nhau (một số tài liệu ghi NY AM là 08:30-11:00, một số ghi 07:00-10:00), cho thấy ranh giới không hề "chuẩn" tuyệt đối.
- **Hindsight bias/confirmation bias:** trader nhớ rõ những ngày "London Open sweep rồi chạy đẹp" nhưng quên các ngày London Open chỉ chop nhẹ rồi đứng yên tới hết cửa sổ — không có thống kê khách quan nào được trader cá nhân log đầy đủ để so sánh.
- **Không có backtest công khai đạt chuẩn thống kê** riêng cho "setup ICT trong KZ" so với "setup ICT ngoài KZ" — dù dữ liệu volume-theo-giờ là có thật (xem mục 14), việc "setup ICT có tỷ lệ thắng cao hơn khi ở trong KZ" là một tuyên bố khác, cụ thể hơn, và chưa có ai công khai chứng minh với sample size đủ lớn.
- **Unfalsifiable khi fail:** nếu một setup trong KZ thua, thường được giải thích là "chưa đủ context (bias/sweep/POI)" — một vòng lặp lý luận khiến Kill Zone luôn "đúng về mặt lý thuyết", còn thất bại luôn đổ cho yếu tố khác.
- **Overfitting khi thêm filter:** ghép Kill Zone + AMD phase + Daily Bias + Silver Bullet + Macro cùng lúc khiến số setup "đạt đủ tiêu chuẩn" trong một tháng chỉ còn vài case — không đủ để rút ra kết luận thống kê đáng tin.
- **Backtest độc lập trái chiều:** nhiều thử nghiệm định lượng công khai về "volatility theo giờ trong ngày" trên FX/futures đều xác nhận hiện tượng tăng volume quanh London/NY open (phần cơ học, mục 14), nhưng không có backtest độc lập nào xác nhận riêng "chất lượng setup ICT" (đảo chiều đúng hướng sau sweep) cao hơn có ý nghĩa thống kê trong các cửa sổ này so với ngoài cửa sổ.
- **Giải thích thay thế đơn giản hơn:** phần lớn hiệu ứng "setup ICT chạy tốt trong KZ" có thể chỉ là hệ quả trực tiếp của **volatility cao hơn theo giờ** (một hiện tượng đã biết, không cần ICT) — bất kỳ chiến lược breakout/momentum đơn giản nào (không dùng bất kỳ khái niệm ICT nào) cũng sẽ "hoạt động tốt hơn" trong giờ có volatility cao, không chứng minh được điều gì đặc biệt về AMD hay Judas Swing.

### 2. Phản biện của phản biện

- **Phần phải chấp nhận hoàn toàn:** ranh giới giờ không chuẩn hóa tuyệt đối giữa các nguồn ICT, thiếu backtest công khai riêng cho "setup ICT trong KZ vs ngoài KZ", và rủi ro overfitting khi cộng nhiều lớp filter thời gian (KZ + Silver Bullet + Macro) — đây là sự thật.
- **Phần có thể trả lời được:**
  - **Quy tắc hóa cứng để backtest được:** hoàn toàn có thể cố định ranh giới giờ theo một định nghĩa duy nhất (ví dụ dùng đúng bảng ở mục 1 của note này) và backtest khách quan tỷ lệ MSS-thành-công trong KZ vs ngoài KZ trên dữ liệu volume thật — vấn đề là chưa ai làm công khai, không phải là không thể làm.
  - **Kill Zone là bộ lọc sự chú ý, không phải tín hiệu độc lập:** giá trị cốt lõi của Kill Zone không nằm ở việc "dự đoán move sẽ xảy ra" mà ở việc **giảm số giờ cần theo dõi từ 24 xuống 6-8 giờ có volume cao nhất** — đây là một tuyên bố về hiệu quả quan sát (attention efficiency), có thể đúng dù tuyên bố "AMD narrative" có đúng hay không.
  - **Edge đến từ risk management + location, không phải từ "dự đoán giờ":** một trader chỉ trade trong KZ **và** chỉ vào lệnh khi có sweep + MSS xác nhận thực chất đang tận dụng lợi thế volume cao (spread hẹp hơn, slippage thấp hơn, dễ đạt R:R hơn) — lợi ích này có thật và đo lường được, độc lập với việc AMD narrative có chính xác 100% hay không.

### 3. Giới hạn cứng phải chấp nhận

1. Ranh giới giờ chính xác của mỗi Kill Zone không được chuẩn hóa tuyệt đối giữa các nguồn ICT khác nhau — không có "giờ đúng duy nhất" được xác nhận khoa học.
2. Chưa có backtest công khai, độc lập, đạt chuẩn thống kê nào xác nhận riêng "chất lượng setup ICT trong KZ" cao hơn có ý nghĩa so với ngoài KZ (khác với việc chỉ xác nhận volatility cao hơn — đây là hai tuyên bố khác nhau).
3. Silver Bullet và ICT Macro có cửa sổ hẹp đến mức backtest đủ mẫu đòi hỏi rất nhiều tháng/năm dữ liệu — hầu hết trader cá nhân không có đủ mẫu để tự kiểm định độ tin cậy thực sự cho riêng mình.
4. Trên crypto (24/7, không có phiên đóng/mở rõ ràng), khái niệm Asian Range/Judas Swing gắn với Kill Zone không có nền tảng cơ học tương đương như trên FX/futures — mọi ứng dụng ở đó là suy diễn loại suy.
5. DST không đồng bộ giữa các quốc gia (Mỹ, EU, và các thị trường châu Á không dùng DST) khiến "giờ NY time" mà toàn bộ hệ thống Kill Zone dựa vào luôn cần một bước quy đổi dễ sai — đây là điểm yếu vận hành cố hữu, không thể loại bỏ hoàn toàn chỉ bằng ghi nhớ.

> [!quote] Kết luận trung thực
> Kill Zone có nền tảng cơ học thật (volume/participant theo giờ trong ngày) và đáng dùng như một **bộ lọc chú ý** giúp trader tập trung vào 6-8 giờ có thanh khoản cao nhất mỗi ngày. Nhưng phần diễn giải AMD gắn với từng cửa sổ giờ vẫn mang tính narrative, chưa được kiểm chứng độc lập — chỉ nên dùng Kill Zone để quyết định **KHI NÀO quan sát**, không dùng để tự tin thái quá về **CÁI GÌ sẽ xảy ra** trong cửa sổ đó.

---

## 16. Edge Cases thực chiến (chỉ thấy khi live/backtest đủ nhiều)

![[KillZone-Edge-Cases.svg|720]]
*Bốn edge case thời gian dễ bẫy nhất: DST Mỹ-EU lệch pha, giờ server broker GMT+2/+3, Sunday reopen bị nhầm với Kill Zone thật, và half-day sau lễ làm biến dạng thanh khoản.*

### Edge Case 1 — DST Mỹ vs DST EU lệch nhau 2-3 tuần: London Open KZ "dịch" giờ VN mà nhiều trader không nhận ra

**Tình huống:** Mỹ đổi giờ Chủ Nhật thứ hai tháng 3 (sang EDT) nhưng Anh/EU đổi giờ muộn hơn, Chủ Nhật cuối tháng 3 (sang BST). Trong ~3 tuần giao thời này, "London Open KZ" theo giờ New York (02:00-05:00 EST/EDT) tương ứng với một giờ London KHÁC so với bình thường — vì bản thân giờ địa phương London cũng đang ở chế độ cũ (GMT) trong khi Mỹ đã chuyển EDT.

**Vì sao bẫy được cả trader có kinh nghiệm:** Trader Việt Nam quy đổi Kill Zone theo bảng cố định (như bảng ở mục 3 của note) áp dụng cả năm, nhưng bảng đó giả định Mỹ và VN có chênh lệch cố định theo DST Mỹ — điều này đúng, nhưng khi trader tham chiếu thêm "giờ London mở cửa thực tế" (ví dụ để phân biệt London Open KZ ICT với giờ mở cửa sàn LSE 08:00 London time) trong 2-3 tuần giao thời, hai mốc "London Open theo ICT (giờ NY)" và "London mở cửa theo giờ London thật" lệch nhau 1 giờ so với các tuần khác trong năm.

**Cách nhận diện sớm:** Nếu đang ở khoảng giữa Chủ Nhật thứ 2 tháng 3 và Chủ Nhật cuối tháng 3, hoặc giữa Chủ Nhật cuối tháng 10 và Chủ Nhật đầu tháng 11, luôn kiểm tra kỹ cả hai loại lịch DST (Mỹ và Anh/EU) trước khi tự tin quy đổi Kill Zone.

**Cách xử lý:** Set chart theo New York time tuyệt đối làm chuẩn duy nhất (bảng quy đổi VN ở mục 3 vẫn đúng vì nó dựa trên DST Mỹ, không bị ảnh hưởng bởi DST châu Âu) — chỉ cẩn trọng khi cần đối chiếu thêm với "giờ mở cửa sàn London/LSE thật" cho mục đích khác ngoài Kill Zone ICT.

### Edge Case 2 — Giờ server broker GMT+2/+3 khiến Silver Bullet "lệch cửa sổ" so với chart hiển thị giờ server

**Tình huống:** Trader dùng nền tảng MT4/MT5 với giờ server GMT+2/+3 cố gắng canh Silver Bullet NY AM (10:00-11:00 ET) bằng cách quy đổi tay ra giờ server — nhưng quên rằng bản thân giờ server GMT+2/+3 cũng thay đổi theo DST riêng của quốc gia đặt server (thường theo giờ Israel/EU, không theo DST Mỹ), dẫn đến việc quy đổi đúng vào một thời điểm trong năm nhưng sai vào thời điểm khác.

**Vì sao bẫy được cả trader có kinh nghiệm:** Một quy đổi "10:00-11:00 ET = 17:00-18:00 giờ server" học được một lần và ghi nhớ cứng sẽ đúng trong phần lớn năm nhưng sai lệch 1 giờ trong các tuần giao thời DST không đồng bộ (tương tự Edge Case 1), khiến trader canh Silver Bullet ngay trước hoặc ngay sau cửa sổ thật mà không biết.

**Cách nhận diện sớm:** Nếu nền tảng cho phép, luôn thêm một đồng hồ phụ hiển thị "New York time" trực tiếp (nhiều nền tảng chart hiện đại hỗ trợ multi-timezone clock) thay vì tự quy đổi tay từ giờ server.

**Cách xử lý:** Tốt nhất tuyệt đối không tự tính giờ Silver Bullet bằng công thức cộng/trừ cố định — luôn xác nhận lại bằng đồng hồ NY time trực tiếp mỗi lần vào phiên, đặc biệt trong tuần đầu sau mỗi lần đổi giờ (tháng 3 và tháng 11).

### Edge Case 3 — Ngày lễ Mỹ half-day (ngày sau Thanksgiving, 24/12) làm toàn bộ NY AM/PM Kill Zone "biến dạng"

**Tình huống:** Vào ngày sau Lễ Tạ ơn (thứ Sáu, thị trường đóng cửa sớm 13:00 ET) và 24/12 (Christmas Eve, cũng thường rút ngắn phiên), khối lượng giao dịch giảm mạnh (thường 30-50% so với ngày thường) và nhiều bàn trading lớn nghỉ sớm hoặc không hoạt động đầy đủ — nhưng cửa sổ giờ NY AM KZ (07:00-10:00 EST) trên lịch vẫn "trông như bình thường".

**Vì sao bẫy được cả trader có kinh nghiệm:** Trader dựa vào lịch Kill Zone cố định sẽ vẫn kỳ vọng biến động/displacement bình thường trong NY AM KZ ngày này, nhưng thực tế giá thường chỉ đi ngang nhẹ hoặc có move giả (fakeout) do thanh khoản mỏng bất thường — sweep xảy ra dễ hơn (vì order book mỏng) nhưng MSS theo sau thường yếu, không tiếp diễn.

**Cách nhận diện sớm:** Luôn kiểm tra lịch nghỉ lễ và half-day của CME/NYSE trước mỗi tuần — đặc biệt các tuần chứa Thanksgiving (thứ Năm tuần 4 tháng 11), July 4th, Christmas, New Year's Eve.

**Cách xử lý:** Vào các ngày half-day, hạ kỳ vọng về chất lượng move trong mọi Kill Zone, giảm size hoặc bỏ qua hoàn toàn nếu không có confluence rất mạnh; không áp dụng bảng "xếp hạng biến động" ở mục 3 của note cho các ngày này.

### Edge Case 4 — Futures Sunday 18:00 ET open không phải "London Open KZ" — dễ nhầm hai khái niệm mở phiên

**Tình huống:** Một số trader mới nhầm giờ CME futures reopen Chủ Nhật (18:00 ET, liên quan đến NWOG — xem [[24 - New Week Opening Gap]]) với "London Open Kill Zone" (02:00-05:00 EST) — hai mốc hoàn toàn khác nhau về bản chất: một là giờ mở lại giao dịch futures sau cuối tuần, một là cửa sổ biến động cao do London bắt đầu hoạt động thương mại.

**Vì sao bẫy được cả trader có kinh nghiệm:** Trên chart futures, cả hai mốc đều là "điểm bắt đầu của một giai đoạn mới trong tuần" nên dễ gộp chung tư duy — nhưng thanh khoản tại 18:00 ET Chủ Nhật cực mỏng (chỉ có Sydney/Tokyo vừa mở), còn London Open KZ 02:00-05:00 EST mới là lúc thanh khoản dồi dào thật của châu Âu.

**Cách nhận diện sớm:** Nếu thấy move "mạnh" ngay lúc Sunday reopen 18:00-19:00 ET, cẩn trọng — đây thường là biến động do thanh khoản mỏng (dễ đảo ngược), không phải distribution thật theo logic Kill Zone.

**Cách xử lý:** Không trade dựa trên biến động ngay sau Sunday reopen; chờ đến đúng London Open KZ (02:00-05:00 EST, tức khi thanh khoản châu Âu thật sự vào) mới áp dụng logic AMD/Judas Swing.

### Edge Case 5 — Nến tin lớn (FOMC 14:00 ET) rơi ngay trong NY PM, nằm NGOÀI mọi Kill Zone chính — dễ bị bỏ qua hoặc trade nhầm

**Tình huống:** FOMC công bố lãi suất 14:00 ET và họp báo Chủ tịch Fed 14:30 ET — cả hai đều rơi vào khung **NY PM**, nằm ngoài các Kill Zone chính đã liệt kê ở mục 1 (London Open, NY AM, London Close, Silver Bullet NY AM). Nhiều trader mới lầm tưởng "ngoài Kill Zone thì không có move đáng kể" và bỏ lỡ hoàn toàn biến động FOMC, hoặc tệ hơn, vẫn cố áp logic Kill Zone thông thường vào một cửa sổ tin có cơ chế hoàn toàn khác.

**Vì sao bẫy được cả trader có kinh nghiệm:** Bảng Kill Zone tiêu chuẩn không có ô "FOMC window" — nếu chỉ theo checklist "trong KZ mới trade", trader sẽ vô tình bỏ qua một trong những cửa sổ biến động cao nhất trong tháng (ngày họp FOMC), hoặc áp nhầm logic sweep-MSS-FVG thông thường vào một cú di chuyển do tin thuần túy (không có logic AMD).

**Cách nhận diện sớm:** Luôn kiểm tra lịch kinh tế riêng biệt với lịch Kill Zone — ngày có FOMC/CPI/NFP cần một bộ quy tắc quản trị rủi ro khác (đứng ngoài trước tin, chờ qua tin mới đánh giá cấu trúc), không đơn giản là "trong KZ hay ngoài KZ".

**Cách xử lý:** Đánh dấu riêng "News Window" trên kế hoạch trade hằng ngày, tách biệt với 4 Kill Zone chính; coi cửa sổ 30-60 phút quanh tin lớn là một loại "vùng đặc biệt" có quy tắc riêng (đứng ngoài, hoặc chỉ trade sau khi displacement đã rõ và ổn định).

### Edge Case 6 — Silver Bullet bị hiểu sai thành "cả cửa sổ NY AM 3 giờ" khiến bộ lọc thời gian mất tác dụng

**Tình huống:** Một số trader tự học qua video cắt ghép, nhớ nhầm rằng "Silver Bullet = NY AM Kill Zone" (gộp chung thành một khung 3 giờ 07:00-10:00 EST), trong khi Silver Bullet NY AM đúng nghĩa chỉ là cửa sổ 1 giờ hẹp hơn (10:00-11:00 EST, theo bảng đã có ở mục 1 và mục 3 của note).

**Vì sao bẫy được cả trader có kinh nghiệm:** Việc mở rộng "Silver Bullet" ra 3 giờ khiến trader tìm FVG entry trong toàn bộ NY AM mà không phân biệt được cửa sổ nào là "chọn lọc cao" — làm giảm hẳn tính năng lọc chất lượng mà Silver Bullet được thiết kế để tạo ra, dẫn đến số lượng lệnh tăng nhưng chất lượng giảm.

**Cách nhận diện sớm:** Nếu thấy mình đang tìm FVG entry theo Silver Bullet suốt cả buổi sáng NY mà không có ranh giới 1 giờ rõ ràng, đó là dấu hiệu đã nhầm hai khái niệm.

**Cách xử lý:** Ghi rõ trong checklist trade: Silver Bullet NY AM = CHỈ 10:00-11:00 EST, không phải cả NY AM KZ; nếu muốn tìm entry ngoài giờ đó vẫn trong NY AM KZ, gọi đó là "NY AM KZ entry" thông thường, không gọi là Silver Bullet.

### Edge Case 7 — Kill Zone "nóng" trên NQ nhưng "lạnh" trên EURUSD cùng thời điểm — trader đa tài sản dễ áp nhầm

**Tình huống:** Một trader theo dõi song song cả NQ và EURUSD trong cùng một buổi sáng nhận thấy NQ có displacement rất rõ trong NY AM KZ (09:30-10:00 ET, quanh giờ mở NYSE) nhưng EURUSD cùng thời điểm chỉ đi ngang nhẹ — vì EURUSD đã "dùng hết" phần lớn biến động ngày trong London Open KZ (02:00-05:00 EST) từ trước đó.

**Vì sao bẫy được cả trader có kinh nghiệm:** Nếu trader áp dụng y hệt một "bảng xếp hạng Kill Zone nóng nhất" cho mọi tài sản (đã cảnh báo ở mục 3 của note là không nên biến thành luật cứng), họ sẽ ép tìm setup trên EURUSD trong giờ NY AM dù cặp tiền này đã hết "nhiên liệu" biến động cho ngày đó.

**Cách nhận diện sớm:** So sánh range đã đi (high-low tính đến hiện tại) so với ATR trung bình ngày của riêng tài sản đó — nếu EURUSD đã đi hết 80% ATR ngày ngay từ London, kỳ vọng NY AM sẽ yếu hơn bình thường cho riêng cặp này.

**Cách xử lý:** Xây bảng "Kill Zone nóng nhất" riêng cho từng tài sản cụ thể bạn trade (như bảng ở mục 3), và luôn kiểm tra range đã đi trong ngày trước khi kỳ vọng biến động tiếp theo ở cửa sổ kế tiếp.

---

## 17. Case Studies chuyên sâu

![[KillZone-Case-Study.svg|720]]
*Case Study 1 minh họa: sweep đáy Asian range 1.2675 → MSS+FVG → entry 1.2688 → TP1 1.2705 → TP2 1.2735, kết quả +2.94R, thực hiện đúng trong tuần giao thời DST.*

### Case Study 1 — GBPUSD, thắng đúng sách: Judas Swing London Open KZ đúng giờ, đúng cấu trúc

**Bối cảnh HTF:** Thứ Tư 05/03 (mùa DST Mỹ đã chuyển EDT, EU chưa chuyển — tuần giao thời Edge Case 1). D1 bias bullish (giá vừa MSS tăng H4 hai phiên trước). Asian range đêm trước: 1.2680-1.2705 (thanh khoản mỏng, đi ngang).

**Setup:** London Open KZ (quy đổi đúng theo giờ NY: 02:00-05:00 EDT — chú ý đây là tuần giao thời, không dùng nhầm giờ EU cũ), kỳ vọng Judas Swing quét đáy Asian range rồi distribution lên theo bias.

**Diễn biến & execution:**
- 02:35 ET (giờ NY, đã EDT): giá quét đáy Asian range xuống 1.2675 (sweep sellside 5 pip dưới đáy Á), để lại wick M15 rõ.
- 02:48 ET: M15 in MSS tăng (phá đỉnh nhỏ 1.2698) + FVG bullish 1.2685-1.2690.
- Entry: 1.2688. SL: 1.2672 (dưới đáy sweep 3 pip).
- TP1 tại đỉnh Asian range 1.2705 — chạm 03:30 ET.
- TP2 tại vùng BSL kế tiếp (đỉnh tuần trước) 1.2735 — chạm 07:50 ET (đầu NY AM KZ, sau khi London Close KZ tiếp sức).

**Kết quả bằng số:** Risk 16 pip. Reward tới TP2: 47 pip → R-multiple ≈ +2.94R.

**Bài học chỉ rút ra được nhờ case này:** Setup thắng đẹp chuẩn sách nhưng đòi hỏi bước kiểm tra thêm mà nhiều trader bỏ qua — vì đây là tuần giao thời DST (Mỹ đã EDT, EU chưa BST), nếu trader chỉ nhìn "giờ London theo đồng hồ treo tường" (chưa đổi) mà quên rằng Kill Zone luôn neo theo giờ NY tuyệt đối, họ có thể canh sai cửa sổ 1 giờ trong chính tuần này. Việc luôn set chart theo NY time (như mục 3 và mục 15 khuyến nghị) chứ không tính nhẩm là yếu tố then chốt giúp bắt đúng setup case này.

### Case Study 2 — NQ, setup đẹp như sách nhưng THUA: Silver Bullet NY AM ngày sau Thanksgiving

**Bối cảnh HTF:** Thứ Sáu ngay sau Lễ Tạ ơn (half-day, CME/NYSE đóng cửa sớm 13:00 ET). D1 bias bullish rõ ràng từ tuần trước. Trader theo dõi Silver Bullet NY AM (10:00-11:00 EST) như thường lệ, không điều chỉnh gì cho ngày đặc biệt này.

**Setup:** 09:55 ET, giá có một cú sweep nhỏ quét đáy 30 phút gần nhất tại 19,820, tưởng chừng chuẩn bị cho một FVG entry Silver Bullet điển hình.

**Diễn biến & execution:**
- 10:05 ET: M5 in MSS tăng nhẹ + FVG hình thành 19,825-19,830 — đúng cấu trúc sách giáo khoa.
- Entry: 19,828. SL: 19,815 (dưới sweep 5 điểm). TP dự kiến: 19,865 (draw on liquidity gần).
- 10:20 ET: giá nhích lên 19,838 rồi đảo chiều ngay, không có lực tiếp diễn — thanh khoản ngày half-day quá mỏng để duy trì displacement, giá dao động hỗn loạn quanh vùng entry.
- 10:52 ET: giá quay lại chạm SL 19,815 khi cửa sổ Silver Bullet gần kết thúc, không có tín hiệu bất thường nào khác ngoài việc thanh khoản cả ngày cực thấp (khối lượng ước tính chỉ ~35% so với thứ Sáu thường).

**Kết quả bằng số:** Lỗ 13 điểm NQ = -1R theo kế hoạch ban đầu.

**Bài học chỉ rút ra được nhờ case này:** Đây là minh chứng trực tiếp cho Edge Case 3 — cấu trúc "đẹp như sách" (sweep + MSS + FVG, đúng cửa sổ Silver Bullet) hoàn toàn không đủ nếu bỏ qua yếu tố thanh khoản theo mùa/ngày lễ. Bài học sâu hơn: **checklist Kill Zone (mục 8 của note) cần bổ sung một bước kiểm tra lịch nghỉ lễ/half-day TRƯỚC khi tin vào bất kỳ tín hiệu nào trong ngày đó** — không chỉ tránh trade vào chính giờ nghỉ, mà cả những ngày rút ngắn phiên vẫn "trông như" ngày thường trên lịch nhưng có chất lượng thanh khoản hoàn toàn khác.

### Case Study 3 — Đứng ngoài đúng: nhận ra biến động Sunday reopen không phải Kill Zone thật, tránh FOMO

**Bối cảnh HTF:** Tối Chủ Nhật, ES vừa reopen 18:00 ET sau cuối tuần. D1 bias bullish từ tuần trước (giá đóng cửa thứ Sáu ở vùng cao).

**Setup (bị cân nhắc nhưng loại bỏ):** 18:15 ET, ngay sau reopen, giá bất ngờ tăng vọt 25 điểm ES trong 10 phút — nhìn thoáng qua giống một displacement mạnh đúng hướng bias, có vẻ như một cơ hội vào lệnh sớm trước khi "mọi người khác" nhận ra.

**Diễn biến & execution (quyết định không vào lệnh):**
- Nhận ra ngay đây là 18:15 ET Chủ Nhật — theo đúng Edge Case 4 đã ghi nhận, đây KHÔNG phải bất kỳ Kill Zone chính nào (không phải London Open, không phải NY AM), mà là thời điểm thanh khoản Sydney/Tokyo vừa mở, cực mỏng.
- Quyết định: không vào lệnh, tiếp tục quan sát.
- Kết quả thực tế: giá đảo ngược hoàn toàn trong 40 phút sau đó, quay lại đúng mức Friday Close ban đầu — xác nhận đây chỉ là biến động do thanh khoản mỏng (một lệnh lớn hoặc vài lệnh trung bình đủ tạo move 25 điểm khi order book gần như trống), không phải distribution thật.

**Kết quả bằng số:** 0R (không giao dịch) — tránh một setup FOMO có khả năng dính SL cao nếu đã đu theo move giả.

**Bài học chỉ rút ra được nhờ case này:** Kỷ luật phân biệt "biến động do thanh khoản mỏng" với "biến động có cấu trúc thật" là kỹ năng chỉ có được qua nhiều lần quan sát Sunday reopen — về bản chất, quy tắc "Kill Zone là điều kiện CẦN" (đã nêu ở mục 4-5 của note) áp dụng ngược lại ở đây: **NGOÀI Kill Zone chính, một move mạnh không tự động có nghĩa gì cả, dù nó trông "đẹp" trên chart.**

### Case Study 4 — BTCUSD, minh họa Kill Zone truyền thống có ý nghĩa yếu hơn nhiều trên crypto 24/7

**Bối cảnh HTF:** Thứ Tư, BTCUSD giao dịch liên tục. Trader áp dụng y hệt bảng Kill Zone ICT (London Open 02:00-05:00 EST, NY AM 07:00-10:00 EST) cho BTC, kỳ vọng thấy accumulation Á rồi manipulation London tương tự FX.

**Setup:** Asian "range" trên BTC (đêm trước, giờ NY) từ 62,400-62,900 — nhưng đây chỉ là biến động thông thường của một tài sản 24/7, không có ý nghĩa "accumulation trước phiên London" như trên FX vì không hề có khái niệm "phiên Á đóng lại rồi London mở".

**Diễn biến & execution:**
- London Open KZ (02:00-05:00 EST): BTC có một nhịp tăng nhẹ lên 63,100, nhưng đây trùng thời điểm một tin tức về ETF Bitcoin được công bố (không liên quan gì đến "London mở cửa") — biến động thực chất do tin, bị gán nhầm cho "Judas Swing London".
- Trader vào long theo kỳ vọng continuation kiểu FX, SL dưới đáy Asian range 62,380.
- Giá sau đó dao động hỗn loạn không theo mẫu hình Kill Zone nào rõ ràng, cuối cùng chạm SL vào giữa NY AM KZ khi một tin khác (không liên quan Mỹ mở phiên) đẩy giá giảm.

**Kết quả bằng số:** Lỗ theo kế hoạch ban đầu, khoảng -1R.

**Bài học chỉ rút ra được nhờ case này:** Trên BTC/ETH, biến động không được tổ chức theo cấu trúc phiên tài chính truyền thống — tin tức (ETF flow, on-chain events, thanh lý hợp đồng phái sinh) có trọng số lớn hơn nhiều so với "giờ nào London/NY mở". Áp trực tiếp khung Kill Zone ICT (được xây dựng cho FX/futures có cấu trúc phiên rõ ràng) sang crypto là một dạng lỗi tương tự Edge Case 7 nhưng ở mức độ nặng hơn: không chỉ "Kill Zone yếu hơn" mà là **cơ chế tạo ra Kill Zone (participant theo giờ trung tâm tài chính) gần như không áp dụng được** cho một thị trường không có giờ đóng/mở.

---

## 18. Tình huống thực chiến (War Stories)

> [!example] War Story 1 — Quên tuần giao thời DST và trade lệch cả một Kill Zone
> Có một năm tôi canh London Open KZ theo công thức nhớ sẵn "14:00-17:00 giờ VN" áp dụng cả năm, quên rằng công thức đó chỉ đúng khi Mỹ đang EDT. Vào đúng tuần đầu tháng 11 (Mỹ vừa fall back về EST nhưng tôi chưa cập nhật), tôi ngồi chờ setup lúc 14:00 giờ VN — thực chất đã là giờ thứ 2 sau khi London Open KZ thật (giờ đã lệch sang 15:00-18:00 giờ VN) bắt đầu, bỏ lỡ toàn bộ move chính. Từ đó tôi luôn dùng đồng hồ hiển thị trực tiếp giờ New York, không dùng công thức quy đổi ghi nhớ cứng.

> [!example] War Story 2 — Ép lệnh vì "đã ngồi chờ cả buổi, phải có gì đó"
> Một hôm tôi ngồi theo dõi NY AM KZ cả 3 giờ mà không thấy sweep/displacement nào đủ rõ theo tiêu chuẩn của mình. Gần hết cửa sổ (09:50 ET), tôi thấy một cú nhích giá nhỏ và tự thuyết phục bản thân đó là "MSS", vào lệnh chỉ vì tâm lý "đã chờ lâu rồi, phải trade cái gì". Giá sau đó chop qua lại và tôi bị stopped out trong đúng "vùng chưa kích hoạt" mà bản thân checklist của tôi đã liệt kê. Bài học: kỷ luật đứng ngoài khi hết Kill Zone khó hơn nhiều so với lý thuyết trên giấy — cảm giác "phải làm gì đó" là kẻ thù lớn nhất của quy tắc này.

> [!example] War Story 3 — Nhầm Silver Bullet với cả buổi sáng vì học qua video cắt ghép
> Trong nhiều tháng đầu học ICT, tôi hiểu nhầm Silver Bullet là "toàn bộ buổi sáng NY" vì xem một video ngắn bị cắt mất phần định nghĩa chính xác 1 giờ. Tôi tìm FVG entry bất kỳ lúc nào trong khung 07:00-11:00 EST và gọi tất cả là "Silver Bullet setup" — dẫn đến số lượng lệnh tăng gấp 3 lần so với khi tôi hiểu đúng, nhưng chất lượng giảm rõ rệt. Chỉ khi đọc lại tài liệu gốc kỹ hơn tôi mới nhận ra mình đã tự làm loãng chính bộ lọc mà mình định dùng.

---

## 19. Câu hỏi tự kiểm tra *(bổ sung)*
- Kill Zone dựa trên cơ chế thị trường nào có thể đo lường độc lập với ICT (không cần AMD narrative)?
- Vì sao DST Mỹ và DST EU lệch nhau 2-3 tuần mỗi năm có thể khiến quy đổi Kill Zone sai dù bạn nhớ đúng công thức "bình thường"?
- Kể ra sự khác biệt giữa Sunday futures reopen (18:00 ET) và London Open Kill Zone (02:00-05:00 EST) — vì sao không nên trade biến động ngay sau reopen như một Kill Zone?
- Ngày half-day (sau Thanksiving, 24/12) ảnh hưởng thế nào đến độ tin cậy của Silver Bullet?
- Vì sao Kill Zone truyền thống ICT áp dụng yếu hơn nhiều trên crypto 24/7 so với FX/futures?

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