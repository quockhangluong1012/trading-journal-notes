---
type: ict-concept
concept: Liquidity Sweep
aliases:
  - Liquidity Sweep
  - Sweep
  - Stop Hunt
  - Liquidity Grab
  - Stop Raid
  - Turtle Soup
tags:
  - trading/ict/concept
  - trading/study
  - "#LiquiditySweep"
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
  - "[[Mistake - Trade The Wick Immediately]]"
  - "[[Mistake - Confuse Real Break With Sweep]]"
  - "[[Mistake - Entry Before Reclaim]]"
---

# Liquidity Sweep

> [!summary] Tóm tắt 1 câu
> **Liquidity Sweep là hành động giá nhanh chóng quét qua một vùng liquidity (đỉnh/đáy, equal highs/lows) để kích hoạt stop và pending order, gom thanh khoản cho "smart money", rồi đảo chiều — đây là điều kiện kích hoạt (trigger) cho hầu hết các entry ICT.**

> [!important] Nguyên tắc cốt lõi
> **Một cú quét chỉ là Liquidity Sweep khi giá QUAY NGƯỢC LẠI (reclaim) vùng vừa quét kèm displacement; nếu giá đóng nến ngoài vùng và đi tiếp, đó là BREAK THẬT, không phải sweep.**
> Sweep mà không có reclaim + displacement là cái bẫy. Đừng trade cú quét; trade phản ứng SAU cú quét.

---

## 1. Định nghĩa

![[Liquidity-Sweep-Definition.svg]]

*Hình: Phân biệt Sweep (wick xuyên → reclaim + displacement → đảo chiều) với Break thật (đóng nến vượt hẳn + acceptance → tiếp diễn).*

**Khái niệm:**
Liquidity Sweep (còn gọi stop hunt, liquidity grab, stop raid) là khi giá di chuyển vượt qua một mức nơi tập trung lệnh chờ — đỉnh cũ, đáy cũ, equal highs/lows, hoặc đường xu hướng rõ ràng — để **kích hoạt** các lệnh đó, sau đó **đảo chiều**. Nhóm thanh khoản bị quét chính là "nhiên liệu": stop loss của trader đang giữ lệnh + breakout order của trader mới vào, cộng lại tạo đủ khối lượng đối ứng để smart money khớp lệnh lớn của họ.

**Bản chất:** thị trường di chuyển từ một pool liquidity này tới một pool liquidity khác. Trước khi đẩy giá đi xa, market thường **lấy thanh khoản ở phía gần** (quét đỉnh/đáy gần nhất) để (1) gom lệnh đối ứng và (2) "đánh lừa" đám đông vào sai hướng. Sweep là khoảnh khắc manipulation trong chu kỳ [[02 - AMD]].

**Sweep vs Break (cực kỳ quan trọng):**
- **Sweep:** giá xuyên qua mức bằng **bóng nến (wick)** hoặc xuyên rồi nhanh chóng bị kéo lại, **đóng nến trở lại bên trong** vùng, kèm displacement ngược → liquidity đã bị lấy, giá đảo chiều.
- **Break thật (BOS):** giá xuyên qua và **đóng nến vượt hẳn** mức đó, có chấp nhận (acceptance), tiếp tục đi theo hướng phá → đây là tiếp diễn xu hướng, KHÔNG phải sweep.

**Mục đích trong ICT:**
- Là **trigger / điều kiện kích hoạt**: gần như mọi entry ICT (FVG, OB, OTE, Silver Bullet) đều muốn thấy một sweep TRƯỚC khi vào.
- Xác nhận **draw on liquidity** đã được "lấy": pool liquidity là mục tiêu, sweep là lúc nó được tiêu thụ.
- Đánh dấu **điểm đảo chiều tiềm năng**: đáy/đỉnh của cú sweep thường là điểm swing quan trọng để đặt stop.
- Là một nửa của cặp **"sweep → displacement"**: sweep lấy thanh khoản, displacement thể hiện intent đẩy giá hướng ngược.

**Vì sao khái niệm này quan trọng:**
Phần lớn trader thua lỗ vì họ **là** thanh khoản: họ đặt stop ngay dưới đáy, mua ngay khi giá phá đỉnh. Hiểu Liquidity Sweep giúp bạn đứng về phía ngược lại — chờ đám đông bị quét rồi mới vào. Đây là chìa khóa biến "stop hunt" từ kẻ thù thành tín hiệu.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Pool liquidity nào vừa bị lấy (BSL hay SSL)?
- Cú vượt mức này là sweep (sẽ đảo) hay break thật (sẽ tiếp diễn)?
- Giá đã reclaim vùng vừa quét chưa, có displacement xác nhận chưa?
- Đáy/đỉnh của cú sweep — nơi đặt stop loss logic — ở đâu?
- Đã đủ điều kiện trigger để tìm entry tại POI chưa?

### Liquidity Sweep không phải là gì
- Không phải "cứ thấy phá đỉnh/đáy là đảo chiều" — phải có reclaim + displacement.
- Không phải tín hiệu entry độc lập — nó là trigger, vẫn cần POI + bias + premium/discount.
- Không phải mọi cú quét đều dẫn tới đảo chiều; sweep thất bại = break thật.
- Không phải lý do để bắt đáy/đỉnh bằng tay ngay trên wick mà không chờ xác nhận.
- Không đồng nghĩa với "stop hunt xấu xa"; đó là cơ chế cung cấp thanh khoản bình thường của thị trường.

---

## 2. Bối cảnh sử dụng

![[Liquidity-Sweep-Context-Types.svg]]

*Hình: Các loại sweep — SSL Sweep (→ Long), BSL Sweep (→ Short), Turtle Soup, internal vs external; khi nào giá trị cao / nên bỏ qua.*

### Các loại / trạng thái của Liquidity Sweep

| Loại | Mô tả | Ý nghĩa thực chiến |
|---|---|---|
| **SSL Sweep (quét đáy)** | Giá quét xuống dưới đáy cũ / equal lows rồi reclaim | Tín hiệu tìm **Long**: sell-side liquidity đã bị lấy, chờ displacement lên |
| **BSL Sweep (quét đỉnh)** | Giá quét lên trên đỉnh cũ / equal highs rồi reclaim | Tín hiệu tìm **Short**: buy-side liquidity đã bị lấy, chờ displacement xuống |
| **Turtle Soup** | Phá một đáy/đỉnh "rõ ràng" để bẫy breakout trader rồi đảo | Mô hình reversal kinh điển dựa trên sweep |
| **Sweep nội bộ (internal)** | Quét thanh khoản bên trong dealing range | Thường cho move ngắn tới external liquidity |
| **Sweep external (HTF)** | Quét đỉnh/đáy lớn của HTF (PDH/PDL, PWH/PWL) | Điểm đảo chiều lớn, thường mở ra cả một leg |
| **Failed sweep = Break** | Giá xuyên + đóng nến ngoài + đi tiếp | KHÔNG phải sweep; là BOS / tiếp diễn |

> [!tip]
> Hai pool liquidity hay bị quét nhất: **equal highs/lows** (nhiều stop dồn về một mức) và **đỉnh/đáy phiên / ngày trước** (PDH/PDL). Đánh dấu sẵn các mức này trước phiên để nhận diện sweep theo thời gian thực.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có pool liquidity rõ ràng (equal highs/lows, PDH/PDL, swing cũ) ở đúng phía đối diện với hướng bias.
- [ ] Cú quét xảy ra tại **POI HTF** (FVG/OB) đồng hướng Daily Bias.
- [ ] Sweep nằm đúng premium (cho Short) / discount (cho Long).
- [ ] Sweep diễn ra trong **kill zone** (London / NY AM).
- [ ] Sau sweep có **displacement + MSS** xác nhận đảo chiều.

### Khi nào nên bỏ qua?
- [ ] Giá đóng nến vượt hẳn mức (break thật) — không reclaim.
- [ ] Sweep ngược Daily Bias mà không có bằng chứng HTF đảo.
- [ ] Sweep giữa range / quanh equilibrium, không có POI.
- [ ] Không có displacement sau sweep — chỉ "lửng lơ" quanh mức.
- [ ] Đã quét quá nhiều pool, giá đã chạy xa — entry thành chase.
- [ ] Ngoài kill zone / ngoài plan session.

---

## 3. Cấu trúc nhận diện trên chart

![[Liquidity-Sweep-Structure.svg]]

*Hình: Chuỗi 5 dấu hiệu của sweep hợp lệ — Pool → Spike/wick → Reclaim → Displacement → MSS.*

### Dấu hiệu chính
1. **Pool liquidity được xác định trước:** một mức có nhiều stop (equal highs/lows, đỉnh/đáy cũ rõ).
2. **Spike xuyên mức:** một cú đẩy nhanh vượt qua mức, thường để lại **wick dài**.
3. **Reclaim:** giá đóng nến trở lại bên trong vùng (về phía của mức vừa quét) — đây là dấu hiệu phân biệt sweep với break.
4. **Displacement ngược:** ngay sau reclaim, một nến/đoạn displacement mạnh đẩy giá hướng ngược lại.
5. **MSS:** displacement đó thường phá cấu trúc nội bộ (Market Structure Shift), xác nhận đảo chiều.

### Ma trận nhận diện Sweep

| Thành phần | SSL Sweep (→ Long) | BSL Sweep (→ Short) | Cảnh báo / Break thật |
|---|---|---|---|
| **Mức bị quét** | Đáy cũ / equal lows | Đỉnh cũ / equal highs | Mức không rõ / random |
| **Cách xuyên** | Wick dài xuống, đóng lại trên | Wick dài lên, đóng lại dưới | Đóng nến VƯỢT HẲN mức |
| **Reclaim** | Đóng nến trở lại trên mức | Đóng nến trở lại dưới mức | Không reclaim, giữ ngoài |
| **Phản ứng** | Displacement tăng + MSS bullish | Displacement giảm + MSS bearish | Tiếp tục theo hướng phá |
| **Location** | Discount của dealing range | Premium của dealing range | Quanh equilibrium |
| **Bias** | Đồng hướng bias bullish | Đồng hướng bias bearish | Ngược bias |

### Điều kiện bắt buộc
- [ ] Xác định được pool liquidity cụ thể bị quét (mức giá rõ ràng).
- [ ] Có hành vi reclaim: giá đóng nến trở lại bên trong vùng.
- [ ] Có displacement sau sweep (không chỉ một wick rồi đi ngang).
- [ ] Xác định đáy/đỉnh cú sweep để làm mốc stop loss.

### Điều kiện tăng xác suất
- [ ] Sweep tại POI HTF đồng hướng bias.
- [ ] Sweep đúng premium/discount.
- [ ] Displacement sau sweep tạo MSS + để lại FVG.
- [ ] Sweep xảy ra trong kill zone.
- [ ] Pool bị quét là external HTF (PDH/PDL, PWH/PWL) → đảo chiều mạnh hơn.
- [ ] Có một pool liquidity rõ ở phía đối diện để làm target.

### Điều kiện làm setup yếu đi
- Cú quét không có wick rõ / đóng nến vượt hẳn (nghi break thật).
- Không có displacement ngược, giá đi ngang sau sweep.
- Sweep ngược bias hoặc giữa range.
- Đã có chuỗi nhiều sweep liên tiếp, không rõ pool nào còn ý nghĩa.

---

## 4. Quy trình phân tích đa khung thời gian

![[Liquidity-Sweep-MTF-Workflow.svg]]

*Hình: Top-down D1/H4 → H1/M15 → M5/M1 với 4 câu hỏi bắt buộc; trade phản ứng sau sweep, không trade cú sweep.*

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Liquidity Sweep
> 1. **Pool liquidity nào đang là mục tiêu, và cú quét vừa rồi lấy pool nào?**
> 2. **Đây là sweep (reclaim + displacement) hay break thật (đóng nến ngoài)?**
> 3. **Sweep có ở đúng POI HTF + premium/discount + đồng hướng bias không?**
> 4. **Đáy/đỉnh sweep ở đâu để đặt stop, và target liquidity phía đối diện ở đâu?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **Pool liquidity HTF:** đánh dấu PDH/PDL, PWH/PWL, equal highs/lows lớn — đây là các mức dễ bị sweep và là draw on liquidity.
- **Draw on liquidity:** giá đang bị hút về pool nào? Sweep ở phía ngược thường mở ra leg đi về pool đó.

### H1 / M15 — POI & Context
- **POI cụ thể:** xác định FVG/OB nơi kỳ vọng sweep xảy ra, ví dụ `giá quét SSL dưới đáy M15 tại 1.0810 ngay trong vùng H1 bullish FVG`.
- **Loại pool:** equal lows / đáy cũ / PDL. Ghi rõ mức.
- **Phân biệt sweep vs break:** chờ nến H1/M15 đóng — đóng lại bên trong = sweep; đóng ngoài = break.

### M5 / M1 — Confirmation & Entry
- **Reclaim + MSS:** sau khi giá quét pool, chờ M5/M1 reclaim mức và tạo MSS ngược hướng quét.
- **Displacement + FVG:** displacement sau sweep thường để lại FVG nhỏ làm điểm entry refined.
- **Entry:** vào tại FVG/OB của đoạn displacement, hoặc retest mức vừa reclaim.
- **Stop loss logic:** đặt ngay ngoài đáy/đỉnh của cú sweep (nơi liquidity vừa bị lấy) — đây là stop "an toàn" nhất vì market vừa quét xong vùng đó.

```text
Mẫu ghi nhanh — Long sau SSL Sweep
HTF Bias: Bullish | Location: Discount
Pool bị quét: equal lows / PDL tại [level]
Sweep xác nhận: wick xuống + đóng nến TRỞ LẠI trên [level]
POI: H1 bullish FVG/OB [range]
Confirm: M5 reclaim + bullish MSS + displacement
Entry: FVG đoạn displacement / retest mức reclaim
Stop: dưới đáy cú sweep ([sweep low])
Target: BSL phía trên ([level])
Invalid: đóng nến M15/H1 lại xuống dưới [level] (thành break thật)
```

```text
Mẫu ghi nhanh — Short sau BSL Sweep
HTF Bias: Bearish | Location: Premium
Pool bị quét: equal highs / PDH tại [level]
Sweep xác nhận: wick lên + đóng nến TRỞ LẠI dưới [level]
POI: H1 bearish FVG/OB [range]
Confirm: M5 reclaim + bearish MSS + displacement
Entry: FVG đoạn displacement / retest mức reclaim
Stop: trên đỉnh cú sweep ([sweep high])
Target: SSL phía dưới ([level])
Invalid: đóng nến M15/H1 lại lên trên [level] (thành break thật)
```

> [!warning]
> **Đừng trade cú sweep — trade phản ứng sau cú sweep.** Vào lệnh ngay trên wick khi giá còn đang quét là cách nhanh nhất để bị "double sweep" (quét sâu hơn). Luôn chờ reclaim + displacement.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

![[Liquidity-Sweep-Validation.svg]]

*Hình: Sweep thành công vs Sweep yếu vs Break thật vs Double sweep — và cách phòng tránh cái bẫy double sweep.*

### Setup được xem là hợp lệ khi
- [ ] Pool liquidity bị quét rõ ràng (equal highs/lows, swing cũ, PDH/PDL).
- [ ] Giá reclaim: đóng nến trở lại bên trong vùng vừa quét.
- [ ] Có displacement + MSS xác nhận đảo chiều sau sweep.
- [ ] Sweep tại POI HTF đồng hướng bias, đúng premium/discount.
- [ ] Stop logic nằm ngoài đáy/đỉnh cú sweep; target là pool liquidity đối diện.
- [ ] R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Giá **đóng nến vượt hẳn** mức và giữ ngoài → đó là break thật, không phải sweep.
- [ ] Không có displacement/MSS sau sweep — giá đi ngang quanh mức.
- [ ] Sweep ngược bias / sai premium-discount.
- [ ] Sau khi vào, giá đóng nến lại ngoài đáy/đỉnh sweep (double sweep) → cắt lệnh.
- [ ] Sweep giữa range không có POI / target rõ.

### Sweep thành công vs Sweep thất bại (= Break)

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Wick xuyên mức, đóng nến trở lại trong vùng, kèm displacement ngược | **Sweep thành công** | Liquidity đã bị lấy → tìm entry đảo chiều |
| Xuyên mức, đóng nến trở lại nhưng KHÔNG có displacement | **Sweep yếu / chưa xác nhận** | Chờ thêm; có thể chỉ test |
| Đóng nến vượt hẳn mức + acceptance + đi tiếp | **Break thật (BOS)** | Tiếp diễn xu hướng, KHÔNG đảo |
| Reclaim rồi lại bị quét sâu hơn | **Double sweep / failed reversal** | Stop bị quét; cần vùng sâu hơn |

> [!note]
> **Double sweep** là cái bẫy phổ biến: cú sweep đầu kéo bạn vào, cú sweep thứ hai sâu hơn quét stop của bạn rồi mới đảo thật. Vào tại POI HTF lớn hơn và chờ displacement rõ giúp giảm rủi ro này; stop nên nằm ngoài cả vùng POI, không sát mép.

---

## 6. Ví dụ chart

### Ví dụ đúng — Quét SSL tại discount → displacement + MSS → Long
![[Liquidity-Sweep-Example-Correct.png]]

**Mô tả:**
HTF bias Bullish, draw on liquidity là BSL phía trên. Giá giảm vào discount và hình thành equal lows (SSL). Một cú spike quét xuống dưới SSL (wick dài), nhưng nến đóng **trở lại trên** mức (reclaim). Ngay sau đó là nến displacement tăng mạnh phá swing high nội bộ (MSS bullish), để lại bullish FVG. Giá retrace về POI (FVG/OB), entry tại đó; stop dưới đáy cú sweep; target là BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- Có reclaim rõ + displacement + MSS, không phải break thật.
- Sweep ở **discount**, đồng hướng Daily Bias bullish.
- Entry SAU sweep tại POI, không phải bắt đáy trên wick.
- Stop nằm ngoài đáy sweep (nơi liquidity vừa bị lấy → ít bị quét lại).
- Target là pool liquidity rõ ràng (BSL).

### Ví dụ sai / dễ nhầm — Long ngay trên wick, nhầm "break thật" là "sweep"
![[Liquidity-Sweep-Example-Wrong.png]]

**Mô tả lỗi:**
Giá giảm về equal lows. Khi giá xuyên xuống dưới SSL, trader lập tức Long ngay trên wick vì "chắc là sweep, sắp đảo". Nhưng nến **không reclaim** — nó đóng hẳn dưới SSL (acceptance), không có displacement ngược. Đây là **break thật**, giá tiếp tục giảm và quét luôn stop của lệnh Long.

**Bài học:**
- Sweep cần **reclaim + displacement**; chỉ một cú xuyên mức chưa đủ.
- Vào ngay trên wick = đặt cược trước khi có xác nhận; rất dễ trúng break thật hoặc double sweep.
- Phân biệt sweep (đóng lại trong vùng) với break (đóng ngoài, đi tiếp) trước khi vào.

---
### Sequence mẫu — Long sau SSL Sweep
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Giá về discount + bullish HTF POI
→ Equal lows / SSL bị quét (wick xuống + reclaim)
→ Displacement tăng phá cấu trúc (MSS) → tạo Bullish FVG
→ Giá retrace về POI (FVG/OB)
→ M5/M1 bullish MSS xác nhận
→ Entry; Stop dưới đáy cú sweep
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short sau BSL Sweep
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Giá về premium + bearish HTF POI
→ Equal highs / BSL bị quét (wick lên + reclaim)
→ Displacement giảm phá cấu trúc (MSS) → tạo Bearish FVG
→ Giá retrace về POI (FVG/OB)
→ M5/M1 bearish MSS xác nhận
→ Entry; Stop trên đỉnh cú sweep
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> Liquidity Sweep là "công tắc bật" cho các model còn lại: [[Fair Value Gap]], [[Order Block]], [[Optimal Trade Entry]] đều mạnh hơn nhiều khi xuất hiện NGAY SAU một sweep đúng hướng narrative. Thiếu sweep, các POI dễ bị xuyên thủng.

---

## 7. Kiến thức nâng cao (Advanced)

### 7.1. SMT Divergence — xác nhận sweep bằng thị trường tương quan

Công cụ mạnh nhất để phân biệt sweep với break thật **trong thời gian thực** (trước khi nến đóng) là so sánh với thị trường tương quan:

![[Liquidity-Sweep-Advanced-SMT.svg]]

- **Nguyên lý:** hai thị trường tương quan chặt (NQ–ES–YM; EURUSD–GBPUSD; DXY nghịch đảo với EURUSD) phải xác nhận lẫn nhau. Khi NQ quét xuống **lower low** mà ES **giữ higher low** (từ chối phá đáy tương ứng), đó là **SMT divergence** — bằng chứng cú phá của NQ là stop run có chủ đích, không phải sell-off thật. Thị trường "khỏe hơn" (không chịu phá đáy) tiết lộ hướng thật.
- **Cách dùng đúng:** SMT là **confirmation, không phải signal**. Chuỗi hợp lệ: giá vào HTF POI đúng premium/discount → sweep pool → **kiểm tra SMT ngay tại thời điểm sweep** → nếu diverge + displacement/MSS → entry với conviction cao hơn. SMT giữa range, ngoài POI = nhiễu (hai thị trường lệch nhau vài phút là chuyện thường).
- **Cảnh giác:** SMT có thể "vẽ lại" khi thị trường còn chạy — divergence chỉ chốt khi swing hoàn thành. Vì vậy vẫn cần displacement làm điều kiện đóng sập. Với NQ: dùng ES làm gương; với EURUSD: liếc GBPUSD và DXY (DXY quét ĐỈNH trong khi EU quét ĐÁY = cộng hưởng hoàn hảo cho Long EU).

### 7.2. Thời gian của sweep — sweep chỉ "được phép" có ý nghĩa ở vài thời điểm

Không phải mọi cú quét đều bình đẳng theo giờ. Các cửa sổ mà sweep mang intent thuật toán:

| Cửa sổ (NY time) | Tên | Hành vi sweep điển hình |
|---|---|---|
| **02:00–05:00** | London KZ | **Judas swing** — quét một đầu Asia range / PDL-PDH, tạo high/low của ngày; sweep quan trọng nhất với FX |
| **07:00–09:00** | NY pre-market | Quét London high/low trước khi NY chọn hướng thật |
| **08:30** | News embargo | Spike tin quét pool hai phía trong vài giây — không trade trong spike, đọc pool nào bị lấy SAU spike |
| **09:30–10:00** | NYSE opening run | Quét đỉnh/đáy pre-market/overnight của index; setup cho leg AM |
| **~09:50–10:10, 10:50–11:10** | Macro windows | Run-on-liquidity ngắn của thuật toán; sweep trong macro thường đảo rất nhanh |
| **12:00–13:00** | Lunch | Sweep giờ này phần lớn là nhiễu thanh khoản mỏng — hạ độ tin xuống mức thấp nhất |

Nguyên tắc: **một sweep đúng chỗ nhưng sai giờ chỉ đáng một nửa độ tin.** Cùng cú quét equal lows tại discount: xảy ra 03:30 trong London KZ = tín hiệu hạng A; xảy ra 12:20 lunch = quan sát, không hành động. Ghi `sweep_time_window` vào journal để tự kiểm chứng trên dữ liệu của chính mình.

### 7.3. Độ sâu & tốc độ của cú quét — đọc "chữ ký" của stop run

Hai biến số của mọi cú xuyên mức: **đi sâu bao nhiêu** và **ở lại bao lâu**.

| Độ sâu qua mức | Thời gian ngoài mức | Cách đọc |
|---|---|---|
| Nông (vài tick/pip, chỉ wick) | Vài giây – 1 nến | **Stop raid sạch** — chỉ cần lượng stop ngay sát mức; reversal thường nhanh và mạnh |
| Vừa (tới inducement/pool tầng 2) | 1–3 nến, có đóng nến nhẹ qua rồi reclaim ngay | **Sweep phân tầng** — quét cả lớp mồi lẫn pool chính; vẫn hợp lệ nếu reclaim + displacement |
| Sâu, càng đi càng **tăng tốc** | Nhiều nến, pullback không reclaim | **Không phải sweep** — có sponsor thật phía sau cú phá; đây là expansion/break; cấm bắt đảo |
| Sâu nhưng **giảm tốc** rồi đứng im | Nhiều nến lình xình ngoài mức | Chưa phân định — chờ; thường kết thúc bằng một trong hai kịch bản trên |

Thước đo bổ trợ: chiếu **standard deviation của Asia range / CBDR** ([[31 - Standard Deviation]], [[08 - Central Bank Dealers Range]]) — manipulation leg của London thường dừng quanh 1–2 SD dưới/trên range; cú quét chạy vượt xa 2.5–3 SD mà chưa quay lại là cảnh báo mạnh rằng đây không còn là manipulation. Tốc độ quan trọng hơn độ sâu: **stop run thật rời khỏi hiện trường ngay** — nến sau sweep phải là displacement; sự do dự chính là thông tin phủ định.

### 7.4. Turtle Soup — đóng gói sweep thành một model hoàn chỉnh

[[33 - Turtle Soup]] là phiên bản model hóa của liquidity sweep: nguồn gốc từ việc trade ngược tín hiệu breakout 20-day high/low của hệ thống Turtle — tức **chuyên săn false breakout tại các mức ai-cũng-nhìn**. Bản ICT hiện đại:

```text
Turtle Soup Long (đối xứng cho Short):
1. Xác định mức reference "công cộng": old low rõ, PDL, PWL, equal lows nhiều ngày
2. HTF context: giá ở discount, draw HTF hướng lên (bias không chống lại)
3. Giá phá XUỐNG mức đó trong kill zone → kích hoạt sell stops + hút breakout sellers
4. Reclaim trong 1–3 nến + displacement + MSS trên LTF
5. Entry FVG của displacement; stop dưới đáy sweep; target liquidity đối diện
```

Điểm cần hiểu sâu: Turtle Soup có edge vì nó trade **ngược lại hai đám đông cùng lúc** — người bị quét stop (buộc phải bán đúng đáy) và người đu breakout (bán đúng đáy). Cả hai dòng lệnh sell đó chính là thanh khoản cho lệnh buy của smart money — và của mình. Đây là lý do sweep tại mức càng "nổi tiếng" (PDL, đáy tuần, equal lows nhiều lần chạm) thì reversal càng bạo lực.

### 7.5. Giải phẫu cú sweep trên LTF — wick là một câu chuyện nén

Một wick sweep trên M15 khi thả xuống M1 là **cả một cấu trúc hoàn chỉnh**: micro-downtrend → capitulation vào pool → micro-MSS → displacement ra. Ứng dụng:

- **Entry tinh hơn:** thay vì chờ nến M15 đóng để xác nhận reclaim, đọc M1: khi micro-MSS + M1 displacement xuất hiện bên trong wick đang hình thành, đó là reclaim đang diễn ra theo thời gian thực → entry sớm hơn một nhịp, stop sát hơn.
- **Lọc sweep giả:** nếu trên M1 cú "sweep" không có capitulation + đảo cấu trúc mà chỉ là grind đều xuống, khả năng cao đây là break thật đang diễn ra chậm.
- **Đánh đổi:** M1 nhiều nhiễu — kỹ thuật này chỉ dành cho pool + POI đã lên kế hoạch trước, không phải công cụ đi săn tín hiệu mới trong phiên.

### 7.6. Best Practices — Liquidity Sweep

> [!success] Best Practices
> 1. **Lên danh sách "pool có thể bị quét" trước phiên** (Asia H/L, PDH/PDL, equal H/L, London H/L) — sweep chỉ có nghĩa tại mức đã đánh dấu trước; cú quét ở mức mình chưa từng đánh dấu = không trade.
> 2. **Ba lớp xác nhận theo thứ tự: reclaim → displacement → MSS.** Thiếu lớp nào dừng ở lớp đó. Vào lệnh khi mới có wick = đặt cược, không phải trade.
> 3. **Luôn check SMT tại thời điểm sweep** (NQ↔ES, EU↔GU/DXY). Có divergence = nâng tier setup; không có = vẫn được trade nhưng size chuẩn, không size lớn.
> 4. **Chấm giờ cho mọi sweep:** trong kill zone/macro = hạng A; ngoài giờ = hạ tier hoặc bỏ. Ghi `sweep_time_window` vào journal.
> 5. **Đọc tốc độ rời hiện trường:** nến ngay sau cú quét phải là displacement; giá lình xình ngoài mức quá 2–3 nến → hủy kịch bản reversal, không "chờ thêm cho chắc".
> 6. **Mặc định sweep có thể phân tầng (double sweep):** đặt stop ngoài POI HTF/mốc SD kế tiếp chứ không sát wick; nếu bị quét tầng hai đúng kế hoạch dự phòng, được phép re-entry MỘT lần với setup đầy đủ — không trung bình giá.
> 7. **Sau 8:30 news spike:** không trade trong spike; chờ 5–15 phút xem pool nào bị lấy và giá accept ở đâu rồi mới áp model.
> 8. **Backtest riêng biến `smt_divergence`, `sweep_depth`, `time_window`** — mục tiêu là tìm ra "chữ ký sweep" thắng nhiều nhất với chính thị trường mình trade (NQ khác EURUSD đáng kể ở độ sâu quét điển hình).

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Một cú quét không phải lệnh. Chỉ vào khi có reclaim + displacement + POI + đúng context.

### A. Context (HTF)
- [ ] Daily Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] Pool liquidity mục tiêu đã đánh dấu (equal highs/lows, PDH/PDL, swing cũ).
- [ ] Cú sweep ở đúng premium (Short) / discount (Long) của dealing range.
- [ ] Sweep tại / trùng một POI HTF có ý nghĩa, đồng hướng bias.
- [ ] Có pool liquidity đối diện làm target.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã reclaim mức vừa quét (đóng nến trở lại bên trong).
- [ ] Có displacement + MSS xác nhận đảo chiều sau sweep.
- [ ] Displacement để lại FVG/OB làm điểm entry refined.
- [ ] Entry SAU sweep, không phải bắt đáy/đỉnh trên wick.
- [ ] Stop logic: ngoài đáy/đỉnh cú sweep.
- [ ] Target là liquidity rõ; R:R tối thiểu đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Giá đóng nến vượt hẳn mức (break thật) → không trade reversal.
- [ ] Không có displacement/MSS sau sweep → không trade.
- [ ] Sweep ngược bias / sai premium-discount → không trade.
- [ ] Sweep giữa range không POI / không target → không trade.
- [ ] Đã chạy xa sau nhiều sweep → không chase.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade cú wick ngay lập tức | Long/Short ngay khi giá xuyên mức | Dễ trúng double sweep / break thật | Chờ reclaim + displacement rồi mới vào |
| Nhầm break thật là sweep | Giá đóng nến ngoài mà vẫn chờ đảo | Đặt cược ngược xu hướng tiếp diễn | Đợi nến đóng: đóng trong = sweep, đóng ngoài = break |
| Bỏ qua bias | Trade mọi sweep cả 2 chiều | Sweep ngược bias xác suất thấp | Chỉ trade sweep đồng hướng Daily Bias |
| Stop quá sát mép sweep | Stop ngay dưới wick vài pip | Double sweep quét sạch trước khi đảo | Đặt stop ngoài cả vùng POI/sweep, cho dư địa |
| Bỏ qua premium/discount | Long sweep ở premium, Short ở discount | Entry thành chase, R:R xấu | Long sweep ở discount, Short ở premium |
| Vào khi không có displacement | Giá đi ngang sau sweep mà vẫn vào | Chưa có intent đảo chiều | Yêu cầu displacement + MSS trước khi vào |
| Trade sweep giữa range | Quét pool nhỏ quanh equilibrium | Không có draw rõ, dễ nhiễu | Ưu tiên sweep tại POI HTF / external pool |
| Chase sau nhiều sweep | Vào khi giá đã chạy xa | Phần lớn move đã xong | Chờ sweep mới tại POI HTF hoặc bỏ qua |

---

## 10. Câu hỏi tự kiểm tra

- Mình có phân biệt được Sweep (reclaim) và Break thật (acceptance) trong 30 giây không?
- Pool liquidity nào vừa bị quét, và nó là internal hay external?
- Cú quét này có ở đúng premium/discount và đồng hướng Daily Bias không?
- Đã có displacement + MSS sau sweep chưa, hay mình đang vào trên wick?
- Đáy/đỉnh cú sweep ở đâu để đặt stop logic?
- Target liquidity phía đối diện ở đâu, R:R bao nhiêu?
- Điều gì làm setup này invalid (đóng nến lại ngoài mức)?
- Nếu mình không trade cú sweep này, lý do "No Trade" là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Liquidity Sweep là gì và mục đích của nó?
**Đáp:** Là hành động giá quét qua một pool liquidity (đỉnh/đáy, equal highs/lows) để kích hoạt stop + pending order, gom thanh khoản cho smart money, rồi đảo chiều. Mục đích: lấy nhiên liệu để khớp lệnh lớn và bẫy đám đông.

### Q2
**Hỏi:** Phân biệt Sweep và Break thật?
**Đáp:** Sweep = xuyên mức bằng wick rồi **đóng nến trở lại bên trong** + displacement ngược (đảo chiều). Break thật = **đóng nến vượt hẳn** mức, có acceptance, đi tiếp (tiếp diễn).

### Q3
**Hỏi:** Vì sao không nên vào lệnh ngay trên wick của cú quét?
**Đáp:** Vì chưa có xác nhận; dễ trúng break thật hoặc double sweep (cú quét sâu hơn) quét sạch stop trước khi đảo thật.

### Q4
**Hỏi:** Sau một SSL sweep hợp lệ, ta tìm vị thế gì và stop đặt ở đâu?
**Đáp:** Tìm **Long**; stop đặt ngay dưới đáy của cú sweep (nơi liquidity vừa bị lấy).

### Q5
**Hỏi:** Hai điều kiện xác nhận một sweep đã "thành công"?
**Đáp:** (1) Reclaim — giá đóng nến trở lại bên trong vùng; (2) Displacement + MSS ngược hướng quét.

### Q6
**Hỏi:** Double sweep là gì?
**Đáp:** Cú sweep đầu kéo trader vào, cú sweep thứ hai sâu hơn quét stop của họ rồi mới đảo chiều thật. Phòng tránh bằng cách vào tại POI HTF lớn và đặt stop ngoài cả vùng.

### Q7
**Hỏi:** Liquidity Sweep đóng vai trò gì với FVG/OB/OTE?
**Đáp:** Là trigger / điều kiện kích hoạt. Các POI này có xác suất cao hơn nhiều khi xuất hiện ngay SAU một sweep đúng hướng narrative.

---

## 12. Lesson Learned

### Bài học chính
- Sweep là **trigger**, không phải tín hiệu entry độc lập.
- Phân biệt **sweep (reclaim) vs break (acceptance)** là kỹ năng cốt lõi — nhầm hai cái này là nguồn thua lỗ lớn.
- Trade **phản ứng sau cú sweep** (displacement + MSS), không trade cú sweep.
- Stop hợp lý nằm **ngoài đáy/đỉnh cú sweep**, đủ dư địa để tránh double sweep.
- Sweep mạnh nhất khi ở **POI HTF + đúng premium/discount + đồng hướng bias + trong kill zone**.

### Quy tắc cá nhân rút ra
- [ ] Tôi không vào lệnh trên wick; tôi chờ nến đóng để xác nhận reclaim.
- [ ] Tôi chỉ gọi là "sweep" khi có reclaim + displacement; nếu đóng nến ngoài mức, tôi coi là break thật.
- [ ] Tôi chỉ trade sweep đồng hướng Daily Bias và đúng premium/discount.
- [ ] Tôi đặt stop ngoài đáy/đỉnh cú sweep, không sát mép.
- [ ] Khi giá đóng nến lại ngoài vùng sau khi tôi vào (double sweep), tôi cắt lệnh ngay.

### Câu nhắc nhở khi trade
> **"Tôi không bắt cú quét — tôi bắt phản ứng sau cú quét. Reclaim + displacement, rồi mới vào."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt sweep vs break, internal vs external không? |
| Nhận diện trên chart |  | Có nhận ra reclaim + displacement theo thời gian thực không? |
| Biết khi nào bỏ qua |  | Có dám bỏ cú "có vẻ sweep" khi đóng nến ngoài mức không? |
| Kết hợp với context HTF |  | Sweep có được đặt trong bias + premium/discount + POI không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra SAU reclaim, stop ngoài sweep không? |
| Review sau trade |  | Có kiểm tra bằng dữ liệu journal thay vì cảm xúc không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[Liquidity Sweep]]`.
- [ ] Review riêng: vào trên wick vs sau reclaim; stop sát mép vs ngoài POI.
- [ ] Thống kê win rate, average R theo `reclaim_confirmed` và `displacement_after_sweep`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## Appendix — Liquidity Sweep Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish / Neutral
> **Pool mục tiêu (draw):**
> **Pool vừa bị quét:** equal-highs / equal-lows / PDH / PDL / swing — mức: ____
> **Sweep hay Break?** (đóng trong = sweep / đóng ngoài = break)
> **Reclaim xác nhận?** Yes / No
> **Displacement + MSS sau sweep?** Yes / No
> **Location:** Premium / Discount / Equilibrium
> **Trùng POI HTF nào:**
> **Entry plan (sau reclaim):**
> **Stop (ngoài đáy/đỉnh sweep):**
> **Target (pool đối diện):**
> **Kill zone permitted:** London / NY AM / NY PM
> **No-trade condition:**
