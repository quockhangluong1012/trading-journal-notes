---
type: ict-concept
concept: Break of Structure
aliases:
  - BOS
  - Break of Structure
tags:
  - trading/ict/concept
  - trading/study
  - "#BOS"
status: seed
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
markets:
  - EURUSD
  - GBPUSD
  - NDX
  - XAUUSD
importance: 5
confidence: 0
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-02
common_mistakes:
  - "[[Mistake - Wick Sweep Mistaken for BOS]]"
  - "[[Mistake - BOS Confused with MSS]]"
  - "[[Mistake - Chasing After BOS]]"
---

# Break of Structure

> [!summary] Tóm tắt 1 câu
> **Break of Structure (BOS) là sự kiện giá ĐÓNG NẾN với displacement qua một swing point trước đó THEO HƯỚNG xu hướng hiện tại, xác nhận order flow TIẾP DIỄN (continuation) chứ không phải đảo chiều.**

> [!important] Nguyên tắc cốt lõi
> **BOS xác nhận tiếp diễn để giữ bias; nhưng đừng nhầm sweep (wick xuyên qua rồi đóng lại) với BOS thật (body close + displacement).**  
> BOS THUẬN trend (continuation) hoàn toàn khác MSS NGƯỢC trend (reversal) — nhầm hai khái niệm này là một trong những lỗi cấu trúc nguy hiểm nhất.

---

## 1. Định nghĩa

**Khái niệm:**  
BOS trong ICT là việc giá phá một **swing point trước đó theo đúng hướng của xu hướng đang chạy**, được xác nhận bằng **đóng nến (body close) có displacement** chứ không chỉ bằng wick. Cụ thể:
- **Bullish BOS:** trong một uptrend, giá đóng nến **lên trên swing high gần nhất** (đỉnh nội bộ hoặc đỉnh cấu trúc) → xác nhận buyers vẫn kiểm soát, leg tăng tiếp diễn.
- **Bearish BOS:** trong một downtrend, giá đóng nến **xuống dưới swing low gần nhất** → xác nhận sellers vẫn kiểm soát, leg giảm tiếp diễn.

BOS là dấu hiệu **tiếp diễn (continuation)**, không phải tín hiệu đảo chiều. Nó nói: "xu hướng hiện tại vẫn còn hiệu lực".

![[BOS-Advanced-Anatomy.svg|697]]

**Vì sao body close quan trọng đến vậy (logic đấu giá):** một wick xuyên qua swing chỉ chứng minh rằng *lệnh thị trường đã chạm tới đó* — thường là stop bị kích hoạt. Một **body đóng bên ngoài swing** chứng minh điều khác hẳn: sau khi mọi stop đã khớp, thị trường vẫn **chấp nhận (acceptance)** giá ở mức mới cho tới hết cây nến. Sweep = *ghé thăm rồi bị đuổi về*; BOS = *chuyển đến ở hẳn*. Đó là lý do một cú phá chỉ được "tin" khi nến đóng — gắn nhãn khi nến chưa đóng là gắn nhãn cho một tương lai chưa xảy ra.

**Mục đích trong ICT:**  
- Xác nhận **order flow tiếp tục** theo hướng cũ → khẳng định bias tiếp diễn.
- Lập **bản đồ dealing range**: mỗi BOS định nghĩa lại external structure (đỉnh/đáy cấu trúc mới) và mở ra một leg/dealing range mới.
- Đánh dấu các swing **được bảo vệ (protected high/low)** mới sau khi cấu trúc mở rộng.
- Cung cấp logic cho stop loss và target: swing bị phá trở thành mốc tham chiếu cho liquidity hai phía.

**Vì sao khái niệm này quan trọng:**  
BOS là cách ICT đọc "thị trường có còn đi theo hướng tôi nghĩ không". Một chuỗi BOS liên tiếp cùng hướng = order flow khỏe, bias đáng tin. Nhưng nếu trader nhầm một **wick sweep** (giá chỉ chọc qua swing để lấy liquidity rồi đóng lại trong range) với một BOS thật, họ sẽ vào lệnh tiếp diễn ngay trước khi giá đảo chiều — bị trap ngay tại điểm phân phối.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Xu hướng hiện tại còn được xác nhận tiếp diễn hay không?
- Giá vừa **phá để tiếp diễn (BOS thật)** hay chỉ **sweep liquidity rồi quay đầu**?
- Đây là BOS (thuận trend) hay là MSS (ngược trend, báo đảo chiều)?
- External structure mới nằm ở đâu để vẽ lại dealing range?
- Swing nào đang là protected high/low cần theo dõi?

### Break of Structure không phải là gì
- Không phải mọi lần wick xuyên qua swing — wick xuyên rồi đóng lại trong range thường là **liquidity sweep**, không phải BOS.
- Không phải tín hiệu **đảo chiều** — đó là vai trò của [[21 - Market Structure Shift]] (MSS), phá ngược trend.
- Không phải entry trigger độc lập — BOS xác nhận context tiếp diễn, entry vẫn cần POI + displacement + sequence hợp lệ.
- Không phải lý do đuổi giá (chase) sau khi cấu trúc đã phá xa.
- Không phải bằng chứng đủ một mình; cần đặt trong [[12 - Daily Bias]] và vị trí [[27 - Premium Discount]].

---

## 2. Bối cảnh sử dụng

### Phân loại BOS theo cấp độ cấu trúc

| Loại | Định nghĩa | Ý nghĩa thực chiến |
|---|---|---|
| **Internal BOS** | Phá một swing **nội bộ** bên trong một leg lớn hơn (minor swing, micro structure) | Xác nhận pullback đã kết thúc và leg đang tiếp tục bên trong dealing range; tín hiệu nhỏ, dùng cho timing LTF |
| **External BOS** | Phá một swing **chính** tạo ra cấu trúc lớn (major swing high/low của dealing range) | Xác nhận tiếp diễn ở cấp HTF; vẽ lại external range, xác lập protected high/low mới; tín hiệu nặng ký hơn |

> [!tip]
> **Internal BOS sống bên trong External BOS.** Một loạt internal BOS cùng hướng dồn lại để cuối cùng tạo ra một external BOS. Đừng coi internal BOS trên M1/M5 ngang hàng với external BOS trên H4/D1 khi xác định bias.

![[BOS-Advanced-Internal-External.svg|697]]

### Nâng cao — BOS là lệnh "cập nhật bản đồ" (remap dealing range)

Giá trị lớn nhất của một external BOS không nằm ở tín hiệu vào lệnh, mà ở việc nó **bắt buộc bạn vẽ lại toàn bộ khung tham chiếu**:

1. **Dealing range mới:** đo từ **protected low mới** (ITL cuối cùng trước cú phá — *không phải* đáy cũ của range) tới đỉnh mới mà leg sau BOS đang in. Xem thêm [[37 - Re-mapping Dealing Range sau Displacement]].
2. **Premium/Discount dịch chuyển:** vùng từng là premium của range cũ có thể trở thành **discount của range mới**. Đây là lý do nhiều trader "chờ giá rẻ" mãi không thấy — họ đang đo độ rẻ trên bản đồ đã hết hạn.
3. **Protected swing dời theo:** mỗi BOS dời protected low/high lên/xuống một nấc. Stop loss của vị thế đang chạy cũng nên được đánh giá lại theo protected swing mới (trail theo cấu trúc, không trail theo cảm giác).
4. **Liquidity map mới:** swing vừa bị phá giờ là mốc liquidity hai phía — phía trên nó là stop của phe short mới; quay lại retest vùng phá (breaker logic) là hành vi phổ biến trước khi leg tiếp tục.

![[BOS-Advanced-Range-Remap.svg|697]]

### Khi nào khái niệm này có giá trị cao?
- [ ] Đang có một xu hướng rõ ràng (chuỗi HH/HL cho uptrend, LH/LL cho downtrend) để "tiếp diễn" có nghĩa.
- [ ] Có [[12 - Daily Bias]] đã viết ra; BOS dùng để xác nhận bias còn hiệu lực.
- [ ] BOS được tạo bằng **đóng nến + displacement**, không phải chỉ wick.
- [ ] BOS đồng thời **lấy liquidity** tại swing bị phá (sweep BSL/SSL) rồi tiếp tục đi (không quay đầu).
- [ ] BOS xảy ra **sau khi** giá phản ứng tại POI hợp lệ ở đúng vùng premium/discount.
- [ ] Swing bị phá là một **protected high/low** có ý nghĩa, không phải micro swing ngẫu nhiên.

### Khi nào nên bỏ qua?
- [ ] Giá chỉ wick qua swing rồi đóng lại trong range → khả năng là [[20 - Liquidity Sweep]], không phải BOS.
- [ ] "BOS" xảy ra giữa range, không gắn với POI hay draw on liquidity nào.
- [ ] Cấu trúc đang choppy, không có trend rõ → "tiếp diễn" không có ý nghĩa.
- [ ] BOS đã phá rất xa, daily range gần như cạn → vào lệnh giờ là chase ở premium/discount xấu.
- [ ] Tín hiệu thực ra là MSS (phá ngược trend) nhưng bị đọc nhầm thành BOS thuận trend.
- [ ] Target liquidity của leg đã bị lấy xong; BOS tiếp theo có thể là bẫy phân phối cuối.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Có xu hướng nền:** xác định leg hiện tại đang đi hướng nào (chuỗi swing cùng hướng).
2. **Swing point tham chiếu:** xác định swing high gần nhất (cho bullish BOS) hoặc swing low gần nhất (cho bearish BOS) — ưu tiên swing được bảo vệ.
3. **Đóng nến qua swing:** giá phải có **nến đóng body** qua swing đó, không chỉ wick chọc qua.
4. **Displacement:** cú phá phải có urgency — nến body lớn, quyết đoán, lý tưởng để lại FVG/imbalance.
5. **Cùng hướng trend:** cú phá phải **thuận** xu hướng hiện tại (nếu ngược trend → đó là MSS, không phải BOS).
6. **Hành vi liquidity:** thường BOS đồng thời quét liquidity tại swing bị phá; câu hỏi là giá **tiếp tục đi** hay **quay đầu**.

### Ma trận nhận diện BOS

| Thành phần | Bullish BOS | Bearish BOS | Cảnh báo (dễ nhầm) |
|---|---|---|---|
| **Trend nền** | Uptrend đang chạy (HH/HL) | Downtrend đang chạy (LH/LL) | Choppy / range / không rõ trend |
| **Swing bị phá** | Swing high gần nhất (đỉnh được bảo vệ) | Swing low gần nhất (đáy được bảo vệ) | Micro swing vô nghĩa, hoặc swing đã quá cũ |
| **Cách phá** | **Đóng body** lên trên swing high | **Đóng body** xuống dưới swing low | Chỉ **wick** xuyên qua rồi đóng lại trong range → sweep |
| **Displacement** | Nến tăng mạnh, để lại bullish FVG | Nến giảm mạnh, để lại bearish FVG | Nến yếu, không momentum, không FVG |
| **Hướng so với trend** | Thuận uptrend → tiếp diễn | Thuận downtrend → tiếp diễn | Phá **ngược** trend → đó là MSS, không phải BOS |
| **Liquidity** | Lấy BSL tại đỉnh rồi tiếp tục lên | Lấy SSL tại đáy rồi tiếp tục xuống | Lấy liquidity rồi **quay đầu** → sweep/reversal |

### Điều kiện bắt buộc
- [ ] Có **đóng nến (body close)** qua swing point, không phải chỉ wick.
- [ ] Cú phá đi **thuận hướng** xu hướng hiện tại (xác nhận, đây là điều phân biệt BOS với MSS).
- [ ] Swing bị phá là một swing point thật, có ý nghĩa cấu trúc (ưu tiên protected high/low).
- [ ] Sau khi phá, giá **không lập tức reclaim ngược lại** vào range cũ.

### Điều kiện tăng xác suất
- [ ] Cú phá có **displacement mạnh** và để lại [[Fair Value Gap]] / imbalance rõ ràng.
- [ ] BOS đồng thời **sweep liquidity** (BSL/SSL) tại swing bị phá rồi tiếp tục đi.
- [ ] BOS xảy ra ở external structure (phá swing chính) → vẽ lại dealing range lớn.
- [ ] BOS cùng hướng với [[12 - Daily Bias]] và đúng vùng [[27 - Premium Discount]].
- [ ] Có chuỗi BOS liên tiếp cùng hướng (order flow khỏe).

### Điều kiện làm setup yếu đi
- Chỉ wick xuyên qua swing rồi đóng lại trong range (sweep, không phải BOS).
- "BOS" không có displacement — nến yếu, không momentum, không FVG.
- Phá swing micro vô nghĩa thay vì swing được bảo vệ.
- BOS xảy ra sau khi leg đã chạy rất xa; phần lớn range đã được tiêu thụ.
- Cú phá thực ra ngược trend (là MSS) nhưng bị đọc nhầm thành tiếp diễn.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Bốn câu bắt buộc khi thấy giá phá một swing
> 1. **Cú phá này THUẬN hay NGƯỢC xu hướng hiện tại?** (thuận = BOS / continuation; ngược = MSS / reversal)  
> 2. **Có ĐÓNG NẾN với displacement không, hay chỉ là WICK?**  
> 3. **Giá phá để tiếp diễn, hay chỉ sweep liquidity rồi quay đầu?**  
> 4. **Đây là internal BOS (timing nhỏ) hay external BOS (vẽ lại dealing range)?**

### D1 / H4 — Bias & Narrative
- **Xu hướng HTF:** D1/H4 đang giữ uptrend (HH/HL) hay downtrend (LH/LL)?
- **External structure:** đánh dấu các swing chính. External BOS gần nhất nằm ở đâu? Nó xác nhận tiếp diễn hay đã có MSS đảo chiều?
- **Protected high/low:** swing nào đang được bảo vệ? Phá nó mới có ý nghĩa cấu trúc HTF.
- **Draw on liquidity:** sau external BOS này, leg đang hướng tới liquidity pool nào (BSL/SSL)?
- **Narrative:** trend is likely to continue from ___ toward ___; external BOS confirmed at ___; invalid if MSS forms ngược hướng at ___.

```text
Mẫu ghi nhanh — Bullish continuation (BOS thuận uptrend)
HTF trend: Uptrend (chuỗi HH/HL trên H4)
Last external BOS: H4 đóng body trên swing high tại [level] + để lại FVG
Protected low: [level] (đáy được bảo vệ, chưa bị phá)
Draw on liquidity: BSL tại [đỉnh cấu trúc / PDH]
Narrative: tiếp diễn lên; chờ pullback vào discount/POI → bullish internal BOS LTF → tham gia
Invalidation: H4 đóng body DƯỚI protected low [level] = MSS bearish, hủy bias tiếp diễn
```

```text
Mẫu ghi nhanh — Bearish continuation (BOS thuận downtrend)
HTF trend: Downtrend (chuỗi LH/LL trên H4)
Last external BOS: H4 đóng body dưới swing low tại [level] + để lại FVG
Protected high: [level] (đỉnh được bảo vệ, chưa bị phá)
Draw on liquidity: SSL tại [đáy cấu trúc / PDL]
Narrative: tiếp diễn xuống; chờ pullback lên premium/POI → bearish internal BOS LTF → tham gia
Invalidation: H4 đóng body TRÊN protected high [level] = MSS bullish, hủy bias tiếp diễn
```

### H1 / M15 — POI & Context
- **POI cùng hướng BOS:** sau external BOS, POI nào (FVG/OB hình thành từ cú phá) có thể là vùng giá retrace để tham gia tiếp diễn?
- **Phân biệt internal pullback với reversal:** pullback ngược BOS thuộc cùng dealing range là bình thường; chỉ khi giá tạo MSS (phá ngược protected swing) thì mới nghi đảo chiều.
- **Liquidity trước BOS:** swing bị phá có chứa liquidity không (equal highs/lows, swing rõ)? BOS lấy liquidity đó rồi tiếp tục mới là tín hiệu sạch.
- **Internal BOS để timing:** trong leg tiếp diễn, internal BOS xác nhận pullback đã xong và leg tiếp tục.

### M5 / M1 — Confirmation & Entry
- **Internal BOS xác nhận pullback kết thúc:** trên LTF, sau khi giá về POI và sweep liquidity, một internal BOS thuận hướng xác nhận giá quay lại tiếp diễn.
- **Body close, không wick:** kiểm tra cú phá LTF có đóng body với displacement, không chỉ là một wick chọc swing.
- **Để lại FVG/OB:** displacement của internal BOS để lại entry model có stop logic.
- **Đúng thứ tự:** POI → liquidity sweep → internal BOS + displacement → FVG entry → target external liquidity.

> [!warning]
> **Một internal BOS trên M1 không phủ định external structure HTF.** LTF BOS chỉ là timing để tham gia leg HTF; nó không "tạo" trend mới và không được dùng để đảo bias HTF.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Có xu hướng nền rõ ràng để "tiếp diễn" có nghĩa.
- [ ] Cú phá đi **thuận hướng** trend (đây là BOS, không phải MSS).
- [ ] Có **đóng body + displacement** qua swing, không chỉ wick.
- [ ] Swing bị phá là protected high/low / swing có ý nghĩa, không phải micro swing.
- [ ] BOS lấy liquidity tại swing rồi **tiếp tục đi**, không quay đầu reclaim.
- [ ] BOS đồng bộ với [[12 - Daily Bias]] và vị trí premium/discount hợp lý.
- [ ] Entry tham gia tại POI sau BOS, không phải chase sau khi đã phá xa.

### Setup bị vô hiệu khi
- [ ] Giá chỉ **wick** qua swing rồi đóng lại trong range → đây là sweep, không phải BOS.
- [ ] Sau "BOS", giá lập tức **reclaim** ngược lại range cũ (failed break / sweep).
- [ ] Cú phá không có displacement (nến yếu, không FVG).
- [ ] Cú phá thực ra **ngược trend** → đó là MSS báo đảo chiều, không được dùng làm tín hiệu tiếp diễn.
- [ ] BOS giữa range, không gắn POI / draw on liquidity nào.
- [ ] Protected swing ngược hướng đã bị phá (cấu trúc đã shift), nhưng vẫn cố trade tiếp diễn theo trend cũ.

### Phân biệt "wick sweep" và "BOS thật"

![[BOS-Advanced-Triple-Compare.svg|697]]

| Quan sát | Cách đọc hợp lý |
|---|---|
| Giá **wick** xuyên qua swing high/low rồi đóng nến **trở lại trong range**, kèm displacement ngược | **Liquidity sweep** — lấy stop tại swing rồi quay đầu; KHÔNG phải BOS; cảnh báo khả năng reversal |
| Giá **đóng body** qua swing với displacement, giữ giá ngoài swing cũ, pullback không reclaim | **BOS thật** — tiếp diễn được xác nhận; giữ bias |
| Phá swing **thuận** trend + body close + FVG | **BOS (continuation)** — order flow tiếp tục |
| Phá swing **ngược** trend (phá protected swing đối diện) + body close + displacement | **MSS (reversal)** — cấu trúc shift, chuẩn bị đổi bias; KHÔNG phải BOS |

### BOS vs MSS — bảng so sánh trọng tâm (phần dễ nhầm nhất)

| Tiêu chí | BOS (Break of Structure) | MSS (Market Structure Shift) |
|---|---|---|
| **Hướng so với trend** | **Thuận** xu hướng hiện tại | **Ngược** xu hướng hiện tại |
| **Ý nghĩa** | **Tiếp diễn (continuation)** | **Đảo chiều (reversal)** |
| **Swing bị phá** | Swing **cùng hướng** trend (đỉnh trong uptrend / đáy trong downtrend) | **Protected swing đối diện** (đáy được bảo vệ trong uptrend / đỉnh được bảo vệ trong downtrend) |
| **Tác động lên bias** | **Khẳng định** bias hiện tại | **Cảnh báo phải đổi** bias |
| **Vai trò order flow** | Order flow cũ tiếp tục | Order flow có khả năng đảo |
| **Yêu cầu chung** | Đều cần **body close + displacement** (không chỉ wick) | Đều cần **body close + displacement**; lý tưởng xảy ra sau liquidity sweep tại HTF POI |

> [!warning]
> Cùng một cú "phá swing" có thể là BOS hoặc MSS tùy hướng so với trend. Hỏi **"thuận hay ngược trend?"** TRƯỚC khi gán nhãn. Đọc nhầm BOS thành MSS (hoặc ngược lại) làm sai bias từ gốc.

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish BOS xác nhận tiếp diễn trong uptrend
![[BOS-Example-Correct.png]]

**Mô tả:**  
H4 đang uptrend (HH/HL). Giá pullback vào discount, chạm bullish H1 FVG (POI), sweep sell-side liquidity dưới đáy ngắn hạn. Sau đó một nến **đóng body** lên trên swing high gần nhất với displacement mạnh, để lại bullish FVG → đây là **BOS thật**. Giá giữ trên swing cũ, không reclaim. Internal BOS trên M5 xác nhận pullback đã xong; entry tại FVG retracement, target BSL phía trên (swing high cấu trúc tiếp theo).

**Vì sao đây là ví dụ tốt:**
- Cú phá **thuận uptrend** → đúng nghĩa continuation (BOS), không phải reversal.
- Có **body close + displacement + FVG**, không chỉ wick.
- BOS đồng thời lấy liquidity rồi **tiếp tục đi**, không quay đầu.
- Vẽ lại dealing range mới: protected low mới được xác lập, external structure mở rộng.

### Ví dụ sai / dễ nhầm — Wick sweep bị tưởng là BOS
![[BOS-Example-Wrong-Sweep.png]]

**Mô tả lỗi:**  
Trong uptrend, giá đẩy lên và **wick xuyên qua** swing high gần nhất, lấy buy-side liquidity (BSL) phía trên — nhưng nến **đóng lại bên dưới swing**, trở vào range cũ. Trader đọc nhầm đây là bullish BOS và Long tiếp diễn. Thực tế đó là **liquidity sweep** tại đỉnh; ngay sau, giá tạo bearish displacement và một MSS giảm, đảo chiều xuống — lệnh Long bị stop.

**Bài học:**
- **Wick xuyên qua KHÔNG bằng BOS.** BOS cần **đóng body** qua swing.
- Sweep tại swing thường là điểm phân phối, không phải xác nhận tiếp diễn.
- Luôn hỏi: "giá phá để **tiếp diễn** (body close + giữ giá) hay chỉ **sweep rồi quay đầu** (wick + reclaim)?"

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[21 - Market Structure Shift]] — "người anh em ngược chiều": phá ngược trend = MSS
- [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]] — đo BOS đúng degree
- [[20 - Liquidity Sweep]] — bộ lọc phân biệt phá thật vs quét thanh khoản
- [[13 - FVG  - Fair Value Gap]] / [[25 - OB - Order Block]] — entry model sau cú phá
- [[12 - Dealing Range]] / [[37 - Re-mapping Dealing Range sau Displacement]] — remap sau external BOS
- [[27 - Premium Discount]] — đo lại trên range mới
- [[04 - Breaker Block]] — swing bị phá trở thành vùng retest

### Sequence mẫu — Long tiếp diễn xác nhận bằng BOS
```text
HTF Uptrend (chuỗi HH/HL) + Bullish Daily Bias
→ Giá pullback về Discount + Bullish POI (FVG/OB)
→ Sweep Sell-Side Liquidity dưới đáy ngắn hạn
→ Internal Bullish BOS (LTF) — body close trên swing high gần nhất + displacement
→ Để lại bullish FVG / OB
→ Retrace vào FVG/OB (M5/M1)
→ Stop dưới swing / sweep low logic
→ Target: Internal liquidity trước → External BOS / BSL chính sau
```

### Sequence mẫu — Short tiếp diễn xác nhận bằng BOS
```text
HTF Downtrend (chuỗi LH/LL) + Bearish Daily Bias
→ Giá pullback lên Premium + Bearish POI (FVG/OB)
→ Sweep Buy-Side Liquidity trên đỉnh ngắn hạn
→ Internal Bearish BOS (LTF) — body close dưới swing low gần nhất + displacement
→ Để lại bearish FVG / OB
→ Retrace vào FVG/OB (M5/M1)
→ Stop trên swing / sweep high logic
→ Target: Internal liquidity trước → External BOS / SSL chính sau
```

> [!note]
> BOS xác nhận **context tiếp diễn** và cung cấp **target mapping** (swing/liquidity tiếp theo), nhưng entry vẫn nằm ở POI sau displacement. Đừng vào lệnh ngay tại điểm phá; chờ retrace vào FVG/OB hình thành từ cú phá.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Khái niệm ICT chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**.

### A. Context (HTF)
- [ ] Tôi xác định được xu hướng nền rõ ràng (HH/HL hoặc LH/LL).
- [ ] Cú phá đi **thuận** hướng trend (xác nhận đây là BOS, không phải MSS).
- [ ] Tôi đã viết [[12 - Daily Bias]] và BOS này đồng bộ với bias đó.
- [ ] Tôi đánh dấu external structure và protected high/low hiện tại.
- [ ] Tôi xác định draw on liquidity của leg sau BOS.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã vào POI đúng vùng premium/discount cho hướng trade.
- [ ] Có liquidity sweep hợp lý trước khi tìm BOS xác nhận.
- [ ] Cú phá có **đóng body**, KHÔNG chỉ wick.
- [ ] Cú phá có **displacement** và để lại FVG/OB.
- [ ] Giá **không reclaim** ngược lại range cũ sau khi phá.
- [ ] Entry tại FVG/OB có stop logic, không chase sau khi đã phá xa.
- [ ] Target là liquidity rõ ràng (internal trước, external sau).
- [ ] R:R tối thiểu đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Chỉ có wick xuyên swing rồi đóng lại trong range → đây là sweep, không trade theo tiếp diễn.
- [ ] Cú phá ngược trend (là MSS) → không xử lý như BOS, đánh giá lại bias.
- [ ] Không có displacement / không có FVG → không xem là BOS hợp lệ.
- [ ] "BOS" giữa range, không gắn POI/liquidity → không trade.
- [ ] Leg đã chạy quá xa, range cạn → bỏ qua, không chase.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Nhầm wick sweep với BOS | Giá wick qua swing rồi đóng lại trong range, vẫn coi là BOS | Vào lệnh tiếp diễn ngay trước reversal; bị trap tại điểm phân phối | Yêu cầu **body close + displacement** mới tính BOS; wick + reclaim = sweep |
| Nhầm BOS với MSS | Phá ngược trend nhưng đọc là "tiếp diễn" | Trade ngược hướng đảo chiều thực sự; bias sai từ gốc | Hỏi "thuận hay ngược trend?": thuận = BOS, ngược = MSS |
| BOS không có displacement | Nến phá yếu, không momentum, không FVG | Không phải repricing thật; dễ là noise / pullback | Chỉ tính BOS khi có displacement và để lại imbalance |
| Dùng micro swing làm tham chiếu | Phá một swing nhỏ vô nghĩa và gọi là BOS | Tín hiệu rác, sai protected swing, sai dealing range | Ưu tiên swing được bảo vệ / swing có ý nghĩa cấu trúc |
| Coi internal BOS ngang external BOS | Lấy M1 internal BOS để định trend HTF | LTF BOS không phủ định cấu trúc HTF; dễ trade ngược HTF | Phân tầng: external BOS vẽ range, internal BOS chỉ để timing |
| Chase sau BOS | Vào lệnh ngay tại điểm phá khi giá đã chạy xa | R:R xấu, vào ở premium cho Long / discount cho Short | Chờ retrace về FVG/OB hình thành từ cú phá |
| Bỏ qua câu hỏi liquidity | Không hỏi "phá để tiếp diễn hay chỉ sweep?" | Bỏ lỡ cảnh báo reversal; vào nhầm đỉnh/đáy | Luôn kiểm tra giá tiếp tục đi hay quay đầu sau khi lấy liquidity |
| Cố giữ bias sau khi MSS đã xuất hiện | Protected swing ngược đã bị phá nhưng vẫn trade trend cũ | Cấu trúc đã shift; tiếp tục trade theo trend cũ là ngược order flow mới | Khi protected swing đối diện bị phá body → reassess bias, không ép BOS |
| BOS giữa range | Phá một swing nhưng không gắn POI/liquidity/bias | Không có context; tín hiệu không có edge | Chỉ xét BOS khi nằm trong narrative + đúng premium/discount |
| Không reclaim-check | Tính BOS ngay khi nến phá còn chưa đóng | Nến có thể đóng lại trong range → biến thành sweep | Chờ nến đóng; xác nhận giá giữ ngoài swing, không reclaim |

---

## 10. Câu hỏi tự kiểm tra

- Cú phá tôi đang nhìn THUẬN hay NGƯỢC xu hướng hiện tại? (BOS hay MSS?)
- Giá có **đóng body** qua swing, hay chỉ **wick** chọc qua rồi đóng lại?
- Có displacement và FVG để lại sau cú phá không?
- Swing bị phá là protected high/low có ý nghĩa, hay chỉ là micro swing?
- BOS này lấy liquidity rồi **tiếp tục đi**, hay **sweep rồi quay đầu**?
- Đây là internal BOS (timing) hay external BOS (vẽ lại dealing range)?
- BOS này có đồng bộ với [[12 - Daily Bias]] và vị trí premium/discount không?
- Tôi đang vào lệnh tại POI sau cú phá, hay đang chase sau khi giá đã đi xa?
- Nếu giá reclaim ngược lại range, tôi có thừa nhận đó là sweep và thoát không?
- Setup nào trong trade journal đã áp dụng đúng/sai phân biệt BOS vs sweep vs MSS?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** BOS là gì và nó xác nhận điều gì?  
**Đáp:** BOS là giá đóng body với displacement qua một swing point trước đó **thuận hướng trend**; nó xác nhận order flow **tiếp diễn (continuation)**, giúp giữ bias và lập bản đồ dealing range.

### Q2
**Hỏi:** Bullish BOS và Bearish BOS khác nhau thế nào?  
**Đáp:** Bullish BOS = đóng nến **lên trên** swing high gần nhất khi đang uptrend. Bearish BOS = đóng nến **xuống dưới** swing low gần nhất khi đang downtrend. Cả hai đều thuận trend.

### Q3
**Hỏi:** Điều kiện bắt buộc để một cú phá được tính là BOS (không phải sweep)?  
**Đáp:** Phải có **đóng nến (body close) với displacement** qua swing, không chỉ wick. Wick xuyên qua rồi đóng lại trong range = liquidity sweep, không phải BOS thật.

### Q4
**Hỏi:** BOS khác MSS (Market Structure Shift) như thế nào?  
**Đáp:** BOS phá swing **thuận** trend → tiếp diễn (continuation). MSS phá swing **ngược** trend (phá protected swing đối diện) → đảo chiều (reversal). Đây là phần dễ nhầm nhất.

### Q5
**Hỏi:** Internal BOS khác External BOS ở đâu?  
**Đáp:** Internal BOS phá swing nội bộ bên trong một leg (timing nhỏ trên LTF). External BOS phá swing chính tạo cấu trúc lớn (vẽ lại dealing range, xác lập protected high/low mới).

### Q6
**Hỏi:** Khi giá phá một swing và đồng thời lấy liquidity, cần hỏi điều gì?  
**Đáp:** "Phá để **tiếp diễn** (body close + giữ giá → BOS) hay chỉ **sweep rồi quay đầu** (wick + reclaim → liquidity sweep, cảnh báo reversal)?"

### Q7
**Hỏi:** Quan hệ giữa BOS và protected high/low là gì?  
**Đáp:** Swing được bảo vệ (protected) là điểm cấu trúc quan trọng; chỉ khi **phá nó bằng body** thì cú phá mới có ý nghĩa cấu trúc thật. Phá protected swing ngược trend = MSS.

---

## 12. Lesson Learned

### Bài học chính
- BOS xác nhận **tiếp diễn**, không phải đảo chiều — đảo chiều là việc của MSS.
- Một BOS thật cần **đóng body + displacement**; wick xuyên rồi đóng lại là **sweep**, không phải BOS.
- Phân biệt BOS (thuận trend) với MSS (ngược trend) là phần dễ nhầm và đắt giá nhất — luôn hỏi hướng trước.
- Internal BOS chỉ là timing LTF; external BOS mới vẽ lại dealing range và bias cấu trúc.
- BOS thường đồng thời lấy liquidity; phải hỏi "tiếp diễn hay sweep rồi quay đầu" trước khi tin.

### Quy tắc cá nhân rút ra
- [ ] Tôi không gọi một cú phá là BOS nếu chưa có **body close + displacement**.
- [ ] Tôi luôn xác định hướng so với trend trước: thuận = BOS, ngược = MSS.
- [ ] Tôi không dùng internal BOS trên M1/M5 để phủ định external structure HTF.
- [ ] Khi giá wick qua swing rồi reclaim, tôi gọi nó là **sweep** và cảnh giác reversal, không Long/Short theo tiếp diễn.
- [ ] Tôi không chase ngay tại điểm phá; tôi chờ retrace vào FVG/OB hình thành từ cú phá.

### Câu nhắc nhở khi trade
> **"Body close là BOS, wick là sweep. Thuận trend là BOS, ngược trend là MSS. Hỏi đúng hai câu này trước khi tin vào bất kỳ cú phá nào."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt được BOS (continuation) với MSS (reversal) không? |
| Nhận diện trên chart |  | Có phân biệt body close (BOS) với wick sweep không? |
| Biết khi nào bỏ qua |  | Có bỏ qua wick sweep / BOS giữa range / chase không? |
| Kết hợp với context HTF |  | Có tách internal BOS (timing) khỏi external BOS (vẽ range) không? |
| Áp dụng vào trade thực tế |  | Entry có tại POI sau BOS, không phải chase tại điểm phá không? |
| Review sau trade |  | Có kiểm tra lệnh thua vì nhầm sweep/MSS thành BOS bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Break of Structure]]`.
- [ ] Lọc riêng các lệnh có `bos_confirmation: wick-only` và `bos_vs_mss: reversal` để đo tỷ lệ nhầm lẫn.
- [ ] Thống kê win rate theo `bos_type` (internal vs external) và `structure_alignment`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.

---

## 14. Best Practices

> [!success] Nguyên tắc vàng
> **"Body close là BOS, wick là sweep. Thuận trend là BOS, ngược trend là MSS."** Hai câu hỏi này phải trở thành phản xạ — hỏi trước MỌI cú phá, trước khi cảm xúc kịp gắn nhãn hộ bạn.

![[BOS-Advanced-Quality-Grading.svg|697]]

1. **Chờ nến ĐÓNG rồi mới gắn nhãn.** Một nến đang phá swing với body lớn có thể đóng cửa thành một wick sweep hoàn hảo. Gắn nhãn BOS khi nến chưa đóng là dự đoán, không phải phân tích. Với H1/H4, đây là chỗ cần kiên nhẫn nhất — và là chỗ tách trader có kỷ luật khỏi đám đông.

2. **Chấm grade A/B/C cho mọi BOS trước khi hành động.** Grade A (body close + displacement + FVG + sweep trước đó + đúng degree + đồng bias) mới đáng full size. Grade B đòi thêm confluence. Grade C không được dùng cho bất kỳ quyết định nào — kể cả "giữ lệnh thêm chút".

3. **Sau external BOS, việc ĐẦU TIÊN là remap, không phải tìm entry.** Vẽ lại dealing range từ protected low/high mới, đo lại premium/discount, dời protected swing. Entry chỉ hợp lệ khi được đặt trên bản đồ mới. Nhiều cú "mua discount" thua lỗ thực chất là mua premium của range mới.

4. **Không chase điểm phá — cú phá càng đẹp, retrace về FVG càng đáng chờ.** Displacement mạnh gần như luôn để lại imbalance, và thị trường có thói quen quay lại "nạp xăng" tại đó. Vào ngay tại điểm phá cho stop xa gấp 2–3 lần so với vào tại FVG với cùng target.

5. **Một chuỗi BOS cùng hướng là dữ liệu, một BOS đơn lẻ là sự kiện.** Bias mạnh được xây từ *chuỗi* external BOS đồng hướng trên H4/D1. Đừng nâng cấp một BOS M5 đơn độc thành "trend mới" — đó là công việc của external structure.

6. **Cẩn trọng với BOS cuối range (exhaustion break).** Khi daily range đã chạy gần hết ADR, hoặc leg đã lấy xong pool liquidity mục tiêu, cú BOS tiếp theo có xác suất cao là cú phân phối cuối — body close thật đấy, nhưng không còn nhiên liệu phía trước. Luôn hỏi: "sau cú phá này, giá còn CHẠY VỀ ĐÂU?"

7. **Review định kỳ các lệnh gắn nhãn sai.** Mỗi tuần lọc các lệnh thua có tag BOS và phân loại lại: bao nhiêu thực ra là sweep? bao nhiêu là MSS đọc ngược? Nhầm lẫn có hệ thống sẽ lộ ra sau 20–30 mẫu — và đó chính là mistake note đáng viết vào [[06 - Mistake Database]].
