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
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-28
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

**Bản chất:** thị trường di chuyển từ một pool liquidity này tới một pool liquidity khác. Trước khi đẩy giá đi xa, market thường **lấy thanh khoản ở phía gần** (quét đỉnh/đáy gần nhất) để (1) gom lệnh đối ứng và (2) "đánh lừa" đám đông vào sai hướng. Sweep là khoảnh khắc manipulation trong chu kỳ [[02-AMD]].

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
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12-Daily-Bias]]).
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

Thước đo bổ trợ: chiếu **standard deviation của Asia range / CBDR** ([[31-Standard-Deviation]], [[08-Central-Bank-Dealers-Range]]) — manipulation leg của London thường dừng quanh 1–2 SD dưới/trên range; cú quét chạy vượt xa 2.5–3 SD mà chưa quay lại là cảnh báo mạnh rằng đây không còn là manipulation. Tốc độ quan trọng hơn độ sâu: **stop run thật rời khỏi hiện trường ngay** — nến sau sweep phải là displacement; sự do dự chính là thông tin phủ định.

### 7.4. Turtle Soup — đóng gói sweep thành một model hoàn chỉnh

[[33-Turtle-Soup]] là phiên bản model hóa của liquidity sweep: nguồn gốc từ việc trade ngược tín hiệu breakout 20-day high/low của hệ thống Turtle — tức **chuyên săn false breakout tại các mức ai-cũng-nhìn**. Bản ICT hiện đại:

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

## Tình huống thực chiến (War Stories)

> [!info] Vì sao có mục này
> Các tình huống dưới đây KHÔNG nằm trong định nghĩa chuẩn của sweep. Chúng là những cách mà một cú sweep "đúng sách giáo khoa" vẫn lấy tiền của người đã thuộc bài — chỉ lộ ra sau nhiều mẫu backtest và giờ bay live. Mỗi tình huống kết thúc bằng một rule đo được để đưa vào journal.

### W0. Tầng WHY nền tảng — vì sao sweep BUỘC PHẢI tồn tại (không phải "âm mưu", mà là cơ học)

Trước các tình huống, cần hiểu sweep ở tầng cơ chế — vì mọi rule bên dưới đều suy ra từ đây:

1. **Vì sao phải quét stop? Vì stop là thanh khoản ĐƯỢC BẢO ĐẢM.** Một quỹ muốn mua 2,000 hợp đồng NQ không thể bấm market buy — họ sẽ tự đẩy giá lên trước khi khớp xong (self-impact). Họ cần một khối lệnh **bán** lớn xuất hiện cùng lúc, tại một giá. Stop loss của người đang Long là *lệnh bán market được hẹn giờ sẵn tại một mức giá biết trước* — kích hoạt cả cụm cùng lúc. Quét xuống dưới đáy không phải trò ác ý; nó là **cách duy nhất để size lớn vào hàng mà không tự phá giá của mình**. Đây là lý do sweep xuất hiện trước gần như mọi leg lớn: leg lớn *cần* cú quét để tồn tại.
2. **Vì sao đảo chiều theo sau? Vì bên khởi xướng giờ phải BẢO VỆ tồn kho.** Sau khi khớp xong 2,000 hợp đồng ở đáy quét, bên mua có vị thế khổng lồ với giá vốn ngay tại vùng sweep. Họ không để giá quay lại vùng đó (sẽ lỗ + mất thanh khoản đã gom) → họ đẩy giá đi ngay. **Displacement chính là dấu vết của hành vi bảo vệ tồn kho này** — và đó là lý do "nến sau sweep phải là displacement" không phải quy tắc thẩm mỹ mà là chẩn đoán: không displacement = không có ai vừa gom hàng = cú xuyên mức đó không phải sweep.
3. **Vì sao reclaim là ranh giới? Vì nó phân xử AI thắng phiên đấu giá tại mức đó.** Tại đáy bị xuyên có hai dòng lệnh đối đầu: dòng bán (stop bị kích + breakout seller mới) và dòng mua (bên gom). Giá đóng nến trở lại trong range = dòng mua đã **nuốt hết** dòng bán — phe bán tại mức đó đã cạn đạn. Giá giữ ngoài (acceptance) = dòng bán còn sponsor thật → break. Reclaim không phải "pattern nến"; nó là kết quả trận đấu.

Ba cơ chế này giải thích luôn các W bên dưới: reclaim doji = trận đấu chưa ngã ngũ (W1); double sweep = bên gom cần nhiều thanh khoản hơn một pool nông cung cấp được (W2); news spike = thanh khoản bị RÚT khỏi sổ lệnh thay vì được gom (W3).

### W1. Reclaim giả — thị trường "do dự" cũng là một câu trả lời

![[Liquidity-Sweep-War-Fake-Reclaim.svg|720]]
*Sơ đồ: cùng một cú quét SSL — reclaim bằng doji lình xình (bẫy, dẫn tới tầng 2) vs reclaim bằng displacement (đảo thật).*

**Sách giáo khoa nói:** sweep + đóng nến trở lại bên trong = hợp lệ, tìm entry.

**Thực tế phát hiện sau nhiều mẫu:** có một lớp bẫy nằm *giữa* sweep và break — giá wick qua mức, đóng nến trở lại bên trong (thỏa định nghĩa reclaim!), nhưng nến reclaim là **doji/thân nhỏ**, rồi 2–3 nến tiếp theo lình xình ngay trên mức. Về mặt checklist thì "đã reclaim"; về mặt order flow thì **không có ai tài trợ cho cú đảo** — smart money lấy stop xong mà không đẩy giá đi nghĩa là họ chưa lấy đủ, và pool sâu hơn đang được chuẩn bị.

**Cơ chế:** displacement sau sweep chính là dấu vết của việc khớp lệnh lớn. Sweep tạo thanh khoản; nếu có bên mua thật sự dùng thanh khoản đó, giá *phải* rời khỏi vùng ngay (nến sau sweep là body lớn). Lình xình = thanh khoản bị lấy nhưng chưa ai dùng → xác suất cao đó chỉ là tầng mồi.

**Rule đo được:**
- Reclaim chỉ được tính khi **thân nến reclaim ≥ ~50% range nến sweep** hoặc nến kế tiếp là displacement rõ.
- **Đếm nến:** quá 2–3 nến sau reclaim mà không có displacement → hủy kịch bản, đứng ngoài. Không "chờ thêm cho chắc" — sự do dự đã là câu trả lời.
- Journal field: `reclaim_body_quality` (displacement / weak / doji) — sau 20+ mẫu sẽ thấy nhóm doji-reclaim thua vượt trội.

### W2. Double sweep phân tầng — bản đồ pool phải vẽ trước, không vẽ khi đang chảy máu

![[Liquidity-Sweep-War-Double-Sweep-Tiers.svg|720]]
*Sơ đồ: Asia Low là pool mồi, PDL trùng POI HTF là pool chính; stop sát wick sweep #1 chính là thanh khoản cho sweep #2.*

**Sách giáo khoa nói:** double sweep là rủi ro, đặt stop rộng hơn (đã nêu ở mục 5).

**Thực tế phát hiện:** double sweep KHÔNG ngẫu nhiên — nó có cấu trúc dự đoán được. Khi có **hai pool xếp tầng gần nhau** (Asia Low nông + PDL sâu hơn vài chục điểm, và PDL trùng H1 FVG), kịch bản xác suất cao nhất không phải "đảo tại Asia Low" mà là: quét Asia Low → hút một lớp trader Long sớm → dùng chính stop của họ làm nhiên liệu chặng hai xuống PDL → đảo thật tại POI. Tức là **cú sweep tầng một tồn tại để tạo ra thanh khoản cho tầng hai.** Nhìn được điều này trước phiên thì sweep #1 không còn là bẫy — nó là *lời hẹn* cho setup tại PDL.

**Rule đo được:**
- Trước phiên, xếp tầng pool: Asia H/L → London H/L → PDH/PDL → PWH/PWL. Nếu pool nông có pool sâu hơn trùng POI HTF ngay dưới/trên nó → **mặc định kịch bản phân tầng**, không trade tầng nông (hoặc size ½).
- Stop luôn ngoài **POI HTF / mốc SD kế tiếp**, không sát wick.
- Bị quét đúng kịch bản dự phòng → được re-entry **một lần** với sequence đầy đủ tại pool sâu. Không có lần ba.
- Journal: `swept_pool_tier`, `re_entry_taken`.

### W3. Sweep trong news spike — wick backtest không phải giá khớp thật

![[Liquidity-Sweep-War-News-Spike-Fill.svg|720]]
*Sơ đồ: fill trong backtest tại đáy wick vs fill thực tế sau spread giãn — phần chênh là "phantom R" làm expectancy ảo.*

**Sách giáo khoa nói:** sweep quanh 8:30 là manipulation kinh điển, đọc pool bị lấy sau tin.

**Thực tế chỉ thấy khi so backtest với live:** trên chart lịch sử, cú quét NFP/CPI trông giống mọi sweep khác — wick đẹp, reclaim đẹp. Nhưng tại thời điểm đó **spread giãn 3–10 lần, quote đóng băng, requote liên tục**. Lệnh limit trong wick có thể không bao giờ khớp; lệnh market khớp cách đáy wick hàng chục điểm; stop có thể trượt qua mức đặt. Hệ quả nguy hiểm nhất không nằm ở một lệnh thua — nó nằm ở **backtest**: nếu sample chứa các entry "khớp tại đáy wick tin", expectancy của cả model bị thổi phồng bằng những R không tồn tại. Đây là một dạng curve-fitting mà người chỉ backtest không bao giờ tự phát hiện.

**Rule đo được:**
- Không trade trong spike; chờ 5–15 phút, đọc pool bị lấy và vùng acceptance rồi mới áp model.
- Trong backtest: mọi setup có entry rơi vào ±2 phút quanh high-impact news → gắn `news_window: true` và **thống kê tách riêng**. Nếu edge của model biến mất khi loại nhóm này → edge không có thật.
- Swing tạo bởi spike tin là mức "bẩn": stop sau nó cần buffer rộng hơn, và không dùng nó làm reference swing cho MSS về sau.

### W4. Cùng một "PDL" nhưng hai thị trường nhìn hai mức khác nhau (data feed)

**Tình huống:** bạn đánh dấu PDL trên chart CFD (NAS100 của broker) và chờ sweep. Giá futures NQ đã quét PDL *của futures* và đảo — nhưng trên chart CFD của bạn, wick "chưa chạm mức". Hoặc ngược lại: CFD wick chạm do spread markup, futures không hề chạm. Với FX cũng vậy: đáy của broker A khác broker B vài pip ở các thời điểm thanh khoản mỏng.

**Bản chất:** pool liquidity thật nằm ở nơi **dòng lệnh tập trung** — với chỉ số là futures (CME), với FX là interbank. Chart CFD là bản chiếu có sai số. Sweep "gần chạm mà không chạm" trên chart của bạn có thể đã hoàn thành trên thị trường gốc.

**Rule đo được:**
- Với NQ/NAS100: **đánh dấu level trên chart futures** (NQ, kèm cả ETH/RTH rõ ràng), thực thi trên nền tảng nào cũng được nhưng bản đồ phải là futures.
- Chấp nhận "sweep hụt vài điểm" như một sweep hợp lệ **nếu** thị trường gốc đã quét và mọi lớp xác nhận (reclaim + displacement + SMT) đều có mặt.
- Backtest và live phải cùng một data feed — nếu không, thống kê sweep depth vô nghĩa.

### W5. Sweep đảo quá nhanh trong macro window — lỡ tàu là một kết quả tốt

**Tình huống:** sweep xảy ra trong macro (~9:50–10:10), reclaim và displacement hoàn thành trong 2–3 nến M1, giá rời đi không retrace. Bạn không kịp vào. Phản xạ sai phổ biến nhất: **market order đuổi theo** ở giá đã chạy 1R — biến một setup A+ (của người khác) thành một lệnh C- (của mình), stop xa, R:R nát.

**Bản chất:** tốc độ đảo là *bằng chứng chất lượng* của sweep — nhưng chất lượng của sweep không chuyển thành chất lượng của entry khi giá đã đi. Trong ICT 2022, entry tồn tại ở FVG của displacement leg; **không có retrace = không có entry = không có lệnh.** Đó là kết quả trung tính, không phải thua.

**Rule đo được:**
- Cấm market order sau khi displacement đã chạy quá mức 50% của leg (không còn OTE).
- Ghi vào journal như một `missed_valid_setup` — số này tăng nghĩa là model đang hoạt động và mình đọc đúng; nó là dữ liệu tốt, không phải nỗi đau. Nếu muốn xử lý có hệ thống: nghiên cứu riêng playbook re-delivery (giá quay lại FVG trong macro kế tiếp) thay vì chase.

### W6. Sweep tại vùng rollover/DST — pool "mới" hình thành do lệch múi giờ, không phải liquidity thật

**Tình huống:** vào 1-2 tuần giao thời DST (tháng 3, tháng 11 ở US/UK không đổi cùng ngày), hoặc quanh giờ rollover hợp đồng futures (NQ/ES chuyển hợp đồng quý), một "đáy/đỉnh mới" xuất hiện đúng tại điểm nối giữa phiên cũ và phiên mới — trông giống một pool liquidity mới hình thành, nhưng thực chất là artifact của việc lệch giờ hoặc gián đoạn dữ liệu giữa 2 hợp đồng.

**Bản chất:** rollover contract (ví dụ NQZ25 → NQH26) có thể tạo một gap giá nhỏ giữa giá đóng hợp đồng cũ và giá mở hợp đồng mới do chênh lệch cost-of-carry — gap này không phản ánh lệnh thật bị kích hoạt, chỉ là chênh lệch định giá kỹ thuật giữa hai hợp đồng. Tương tự, trong tuần DST, kill zone "London Open" theo đồng hồ quen thuộc của trader có thể lệch thật 1 giờ so với London Open theo giờ UTC, khiến một swing hình thành "ngoài kill zone thật" bị hiểu nhầm là sweep trong kill zone.

**Rule đo được:**
- Trong 1-2 tuần trước/sau ngày rollover contract chính (được lịch sàn công bố trước), không dùng swing hình thành đúng tại thời điểm rollover làm pool liquidity chính — đối chiếu với chart continuous đã điều chỉnh (back-adjusted) để loại artifact gap.
- Trong 1-2 tuần giao thời DST, verify giờ NY/London thật bằng đồng hồ thế giới, không tin nhãn giờ mặc định trên platform.
- Journal field: `rollover_window: true/false`, `dst_transition_week: true/false` — loại các mẫu này ra khỏi thống kê win rate theo kill zone để tránh làm sai lệch dữ liệu.

> [!success] Cập nhật tổng kết War Stories
> W6 bổ sung một biến ẩn thứ sáu vào danh sách ở cuối mục: **artifact lịch/hợp đồng** (rollover, DST) có thể tạo hình dạng giống sweep/pool mới nhưng không phản ánh order flow thật — luôn đối chiếu lịch rollover và lịch DST trước khi tin một swing mới hình thành tại các thời điểm nhạy cảm này.

> [!success] Tổng kết mục War Stories
> Điểm chung của cả 6 tình huống: **sweep không thất bại vì định nghĩa sai, mà vì thiếu một biến ẩn** — chất lượng thân nến reclaim (W1), cấu trúc tầng của pool (W2), microstructure lúc có tin (W3), sai lệch data feed (W4), tốc độ đảo (W5), và artifact lịch/hợp đồng (W6). Tất cả đều đo được. Đưa chúng vào frontmatter journal (`reclaim_body_quality`, `swept_pool_tier`, `news_window`, `missed_valid_setup`) để chính dữ liệu của mình phân xử, đúng tinh thần [[04 - Backtesting]].

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
- *(bổ sung)* Pool vừa bị quét nằm TRUNG GIAN (có thể là IDM) hay TẠI/NGOÀI POI (external/structural), và mình đã phân loại đúng trước khi hành động chưa?
- *(bổ sung)* Đây có phải tuần rollover contract hoặc tuần giao thời DST không — nếu có, mức độ tin tưởng vào độ sâu/thời điểm của sweep này cần hạ xuống không?
- *(bổ sung)* Nếu là crypto, mình đã kiểm tra funding rate/open interest để loại trừ khả năng đây là liquidation cascade thay vì sweep thật chưa?
- *(bổ sung)* Khung liền kề (trên/dưới) có đang cho một sweep theo HƯỚNG NGƯỢC LẠI không — đây có phải fractal conflict không?

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

### Q8 *(bổ sung)*
**Hỏi:** Vì sao trên NQ/ES, một cú sweep xảy ra đúng phiên OPEX (options expiration) lại kém tin cậy hơn cùng cú sweep đó vào một ngày thường?
**Đáp:** Vì OPEX tạo dealer hedging flow và gamma exposure bất thường lớn — giá có thể đảo ngược dữ dội quanh "gamma wall" mà không liên quan gì tới cấu trúc thanh khoản thật; một MSS "đẹp như sách" hình thành ngay sau sweep vẫn có thể fail vì lực đảo chiều đến từ dealer hedging, không phải institutional order flow theo đúng nghĩa ICT (xem Case Study B, mục 18).

### Q9 *(bổ sung)*
**Hỏi:** Trên crypto (BTCUSD/ETHUSD), làm sao phân biệt một sweep chất lượng cao với một cú "sweep" thực chất là liquidation cascade?
**Đáp:** Kiểm tra funding rate và open interest (OI) trước khi tin vào cú sweep: funding rate cực đoan (dương/âm mạnh) + OI tăng vọt trước đó là dấu hiệu đòn bẩy tích lũy quá mức — cú "sweep" tiếp theo nhiều khả năng là hiệu ứng cơ học của thanh lý dây chuyền (liquidation cascade), không phải smart money thật sự gom thanh khoản có chủ đích (xem EC5, mục 17).

### Q10 *(bổ sung)*
**Hỏi:** Phân biệt vai trò của Liquidity Sweep so với Inducement khi cả hai đều là "quét thanh khoản" về mặt hành động?
**Đáp:** Liquidity Sweep là HÀNH ĐỘNG (giá quét + reclaim tại bất kỳ pool nào), còn Inducement là VAI TRÒ của một pool cụ thể (pool mồi nằm giữa giá hiện tại và POI thật). Một cú sweep có thể xảy ra tại pool mồi (khi đó gọi là "sweep IDM") hoặc tại pool chính dẫn tới đảo chiều thật (external sweep) — bản thân hành động sweep không tự nó cho biết đó là mồi hay pool chính (xem mục 14).

### Q11 *(bổ sung)*
**Hỏi:** Vì sao một cú sweep hình thành TRONG nến tin tức mạnh (ví dụ CPI) thường kém tin cậy hơn một MSS bình thường dù trông "đẹp" hơn (displacement lớn hơn, FVG sâu hơn)?
**Đáp:** Vì nó phản ánh phản ứng tin tức tức thời, hai chiều, chưa ổn định — không phải order flow tổ chức có chủ đích. Nên chờ 5-15 phút sau tin để spread và biến động ổn định, đọc lại cấu trúc trên nền giá mới, KHÔNG vào ngay tại FVG được tạo trong chính nến tin.

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

## 14. Phân định ranh giới: Liquidity Sweep vs Inducement vs MSS

> [!danger] Góc nhìn từ Liquidity Sweep — vì sao "sweep" là từ bị lạm dụng nhiều nhất trong ba khái niệm
> Trong thực chiến, "sweep" thường bị dùng như một từ chung cho MỌI cú giá xuyên qua một mức rồi quay lại — bất kể đó là quét mồi trung gian (Inducement) hay quét pool chính dẫn tới đảo chiều thật. Bài phân định đầy đủ nằm ở [[21-Market-Structure-Shift]] mục 16; ở đây nhấn vào điểm mà Liquidity Sweep dễ bị hiểu sai nhất — **sweep là một HÀNH ĐỘNG xuất hiện ở cả hai vai trò (mồi và pool chính), không tự nó cho biết vai trò nào**.

**Câu hỏi cốt lõi mà Liquidity Sweep trả lời:** *"Giá VỪA lấy thanh khoản ở đâu, và cú lấy đó có displacement + reclaim hợp lệ không?"* — đây là một quan sát HÀNH ĐỘNG, xác nhận SAU KHI nến đã đóng. Sweep không tự phân loại "đây là mồi" hay "đây là điểm đảo" — việc phân loại đó phụ thuộc vào VỊ TRÍ của pool bị quét (đây chính là câu hỏi mà Inducement trả lời) và liệu có MSS xác nhận đảo chiều theo sau không (câu hỏi mà MSS trả lời).

**Bảng phân định nhanh theo góc nhìn sweep:**

| Loại Sweep | Vị trí pool | Có phải Inducement? | Có kèm MSS ngay sau? | Hành động đúng |
|---|---|---|---|---|
| Sweep pool nhỏ, gần POI HTF | Trung gian, giữa giá và POI | Đúng — đây chính là IDM bị quét | Không (hoặc chỉ micro-MSS không đáng tin) | KHÔNG entry — chờ giá tiếp tục tới POI |
| Sweep pool tại/ngay ngoài POI HTF (OB/FVG) | Tại POI, thường là cực dealing range | Không — đây là external/structural sweep | Có — kèm displacement + phá cấu trúc | Entry hợp lệ SAU reclaim + MSS |
| Sweep equal highs/lows dày (multi-poke) | Có thể là IDM (nếu trung gian) hoặc pool chính (nếu tại POI) | Tùy vị trí | Chỉ tại lần thọc CUỐI kèm displacement rời pool | Không vào theo poke đầu — chờ nhịp rời pool có displacement |
| Sweep trong nến tin tức (spike) | Có thể ở bất kỳ vị trí | Không xác định được chắc chắn trong lúc nến đang chạy | Không xác định được cho tới khi nến đóng ổn định | Chờ nến đóng + 1 nến xác nhận thêm trước khi phân loại |

**Ví dụ minh họa trên NQ — một chuỗi, ba lần dùng từ "sweep" với ba ý nghĩa khác nhau:**
```text
09:32 — "Sweep #1" tại đáy nhỏ 18,175 (đây thực chất là quét IDM, không đảo)
09:41 — "Sweep #2" tại đáy OB 18,135 (đây là quét pool chính tại POI — kèm MSS, đảo thật)
10:15 — "Sweep #3" trong nến CPI tại 18,090 (chưa xác định được là gì cho tới khi nến đóng ổn định)
```
Ba lần dùng đúng một từ "sweep" nhưng ý nghĩa hoàn toàn khác — kỷ luật đọc chart đòi hỏi luôn hỏi thêm "sweep NÀY đóng vai trò gì trong sequence?" trước khi hành động.

**Vì sao đây khác các case study đã có ở MSS/Inducement:** MSS (mục 16 của file MSS) đã cho ví dụ NQ phân định 3 khái niệm trên cùng một sequence tổng quát; Inducement (mục 16 của file Inducement) tập trung vào sự khác nhau giữa "sweep tại IDM" và "sweep tại pool chính". Bảng trên bổ sung góc nhìn thứ ba: từ chính hành động sweep, làm sao KHÔNG phân loại sai loại pool đang bị quét — đây là lỗi phổ biến nhất khi trader mới học, gọi bất kỳ wick nào là "sweep" mà không hỏi tiếp "sweep của POOL NÀO, vai trò gì".

---

## 15. Phân tích chuyên sâu: cơ chế thị trường đằng sau Liquidity Sweep

![[Liquidity-Sweep-Deep-Mechanism.svg|720]]
*Sơ đồ: từ limit order book tới displacement — cách một cú sweep vừa là công cụ thực thi vừa là dấu vết để lại cho trader đọc ra.*

### Cơ chế orderflow/auction thực sự tạo ra Liquidity Sweep

- **Limit order book và "thanh khoản được bảo đảm":** một stop loss là lệnh market ĐÃ ĐẶT SẴN, chờ kích hoạt tại một mức giá cụ thể. Với bên cần khớp lệnh lớn, đây là nguồn đối ứng duy nhất có thể dự đoán trước cả về khối lượng và vị trí — khác hẳn thanh khoản "trôi nổi" trên thị trường mở (không biết khi nào xuất hiện, khối lượng bao nhiêu). Sweep về bản chất là hành vi **thu hoạch thanh khoản đã biết trước vị trí**, không phải khai thác thanh khoản ngẫu nhiên.
- **Dealer hedging và gamma exposure (đặc biệt rõ trên chỉ số & vàng):** market maker/dealer nắm quyền chọn thường phải hedge delta bằng cách mua/bán chính tài sản cơ sở. Khi giá tiến gần một mức có nhiều gamma tập trung (thường trùng các mức tâm lý tròn số/PDH-PDL), động thái hedging của dealer có thể tự khuếch đại một cú sweep thành một chuyển động mạnh hơn dự kiến — đây là lý do một số cú sweep trên ES/NQ có displacement bất thường lớn so với sweep tương tự trên FX (nơi không có cấu trúc quyền chọn tập trung tương tự ở cùng quy mô).
- **TWAP/VWAP execution và "điểm dừng tất yếu":** thuật toán thực thi lớn thường tối ưu theo VWAP trong ngày — khi giá lệch quá xa khỏi VWAP về một hướng, các thuật toán mua/bán đối ứng (mean-reversion desks) có xu hướng vào mạnh hơn tại các mức cực trị, tạo áp lực đảo chiều tự nhiên SAU cú sweep — không cần "âm mưu", chỉ cần đủ số lượng thuật toán mean-reversion cùng phản ứng với cùng một mức giá cực trị.
- **Vì sao "reclaim" là ranh giới khách quan, không phải thẩm mỹ:** tại đúng mức bị xuyên, luôn có hai dòng lệnh đối đầu — dòng lệnh vừa bị kích hoạt (stop + breakout order mới) và dòng lệnh của bên đang gom hàng. Nến đóng cửa trở lại trong range nghĩa là dòng mua/bán gom hàng đã áp đảo hoàn toàn dòng lệnh vừa bị kích hoạt trong đúng khung thời gian một nến — đây là bằng chứng orderflow khách quan, không phải một pattern hình học chủ quan.

### Đối chiếu với các khung lý thuyết khác

| Khung lý thuyết | Khái niệm tương đương | Trùng ở đâu | Khác ở đâu |
|---|---|---|---|
| **Wyckoff** | Spring/Upthrust hoặc "Sign of Weakness/Strength" sau test | Cùng mô tả việc giá xuyên qua một mức rồi bị từ chối, xác nhận hấp thụ | Wyckoff gắn sự kiện này với vị trí trong schematic Accumulation/Distribution; ICT không yêu cầu schematic, chỉ cần vị trí tương đối với dealing range |
| **Auction Market Theory** | Rejection tại "excess" (đuôi phân phối volume) | Cùng ý tưởng: giá bị từ chối mạnh tại vùng thanh khoản mỏng, xác nhận bằng việc không quay lại test | AMT đo bằng volume profile khách quan; ICT đọc qua hình dạng wick + nến đóng, ít định lượng hơn |
| **Orderflow/Footprint** | Absorption/exhaustion tại đáy/đỉnh — lệnh limit lớn chống lại market order đang đẩy giá | Cùng mô tả hiện tượng: lệnh chờ lớn "nuốt" hết áp lực market order tại một mức, tạo đảo chiều | Footprint cho số liệu khớp lệnh thật theo mức giá và theo thời gian thực; ICT chỉ suy luận qua hình dạng nến sau khi đã đóng |
| **Turtle Soup (đã nêu ở mục 7.4)** | Chính là một model đóng gói sẵn của sweep + reclaim | Trùng gần như hoàn toàn về cơ chế | Turtle Soup là chiến lược cụ thể có luật vào/ra cố định; Liquidity Sweep trong ICT là một khái niệm rộng hơn, dùng trong nhiều model khác nhau |

### Bảng so sánh hành vi Sweep trên 3 loại thị trường

| Đặc điểm | FX majors (EURUSD, GBPUSD) | Index Futures (NQ/ES) | Crypto (BTC/ETH) |
|---|---|---|---|
| **Nguồn thanh khoản đối ứng chính** | Interbank + retail stop cluster | Stop cluster + dealer hedging flow (đặc biệt quanh OPEX) | Stop cluster + liquidation cascade (đòn bẩy cao khiến hiệu ứng dây chuyền mạnh hơn) |
| **Đặc điểm displacement sau sweep** | Thường tuyến tính, ít giật cục | Có thể giật mạnh bất thường quanh gamma wall | Có thể cực đoan do liquidation cascade tự khuếch đại (một sweep nhỏ kích hoạt chuỗi thanh lý margin) |
| **Độ tin cậy trung bình theo giờ** | Cao nhất London/NY overlap | Cao nhất trong RTH, đặc biệt mở phiên và power hour | Biến thiên rất lớn theo giờ — không có "giờ giao dịch chính" cố định như FX/futures |
| **Rủi ro đọc sai do feed** | Trung bình — chênh lệch giữa broker vài pip | Thấp trong RTH nếu dùng đúng futures gốc, cao khi so CFD vs futures | Cao — nhiều sàn, độ sâu order book khác nhau đáng kể |
| **Tick/point tham chiếu** | EURUSD tick 0.0001 | NQ 1pt = 20 USD, tick 0.25; ES 1pt = 50 USD, tick 0.25 | Biến động tính theo % hợp lý hơn giá tuyệt đối |

---

## 16. Phản biện & giới hạn (Critique)

### 1. Phản biện từ góc nhìn khoa học/quant

- **"Reclaim" là một ngưỡng chủ quan được ngụy trang thành khách quan:** dù mục W1 đã cố gắng lượng hóa ("thân nến reclaim ≥ ~50% range nến sweep"), ngưỡng 50% vẫn là một số tùy chọn (arbitrary) — không có cơ sở thống kê công khai nào chứng minh 50% tốt hơn 40% hay 60% trên một tập dữ liệu ngoài mẫu đủ lớn.
- **Không có định nghĩa "displacement" định lượng thống nhất:** "nến thân lớn" là mô tả tương đối — lớn so với ATR bao nhiêu chu kỳ? Các trader khác nhau dùng ngưỡng khác nhau (1.5x ATR, 2x ATR, hoặc thuần cảm quan), khiến việc backtest hai hệ thống "giống nhau về lý thuyết" cho ra kết quả rất khác nhau.
- **Hindsight bias trong việc phân loại sweep vs break:** một cú xuyên mức chỉ được gọi là "sweep" (reclaim, hợp lệ) hoặc "break" (acceptance, vô hiệu setup) SAU KHI biết nến đóng ở đâu — tại thời điểm giá đang xuyên, không có cách phân biệt chắc chắn, nghĩa là mọi phân tích "đã thấy sweep đẹp" đều mang tính hồi cố.
- **Không có backtest công khai đạt chuẩn thống kê (peer-reviewed hoặc dữ liệu mở):** phần lớn "chứng minh" hiệu quả của sweep-based entry đến từ ảnh chụp chart chọn lọc (cherry-picked) trên mạng xã hội, không phải từ bộ dữ liệu đầy đủ, không chọn lọc, kiểm định ngoài mẫu.
- **Nguy cơ curve-fitting khi thêm quá nhiều lớp xác nhận:** SMT Divergence (7.1) + thời gian sweep (7.2) + tốc độ/độ sâu (7.3) + Turtle Soup (7.4) — mỗi lớp lọc thêm giúp câu chuyện "hợp lý hơn" trên các mẫu lịch sử đã biết, nhưng cũng làm tăng số bậc tự do (degrees of freedom) của hệ thống, tăng rủi ro hệ thống chỉ khớp tốt với dữ liệu đã thấy mà không có sức mạnh dự báo thật ra ngoài mẫu.
- **Giải thích thay thế đơn giản hơn — Mean Reversion cổ điển:** hiện tượng "giá xuyên qua một mức cực trị ngắn hạn rồi đảo chiều" hoàn toàn có thể được giải thích bằng lý thuyết mean-reversion thống kê (giá dao động quá xa trung bình động ngắn hạn có xu hướng quay về) — không cần khái niệm "thanh khoản được engineer có chủ đích" để giải thích cùng một hiện tượng quan sát được.

### 2. Phản biện của phản biện — phần nào đúng, phần nào có thể trả lời

**Phải chấp nhận hoàn toàn:** các ngưỡng định lượng (50% thân nến, X lần ATR cho displacement) đều là lựa chọn tùy ý chưa được kiểm định thống kê công khai đầy đủ; hindsight bias trong phân loại sweep/break là một hạn chế cấu trúc không thể loại bỏ hoàn toàn.

**Có thể trả lời được:**
- *Cứng hóa ngưỡng để tự backtest:* dù chưa có chuẩn ngành công khai, mỗi trader hoàn toàn có thể tự cứng hóa ngưỡng (ví dụ: displacement = thân nến ≥ 1.5x ATR(14) của khung đang xét) và backtest hệ thống của CHÍNH MÌNH với ngưỡng cố định — giá trị không nằm ở việc tìm "ngưỡng đúng tuyệt đối" mà ở việc có một ngưỡng NHẤT QUÁN để đo lường hiệu quả qua thời gian.
- *Mean-reversion và "engineered liquidity" không loại trừ nhau:* hai lời giải thích có thể đúng CÙNG LÚC ở hai tầng khác nhau — mean-reversion giải thích TẠI SAO giá có xu hướng quay đầu sau khi lệch xa (động lực thống kê), còn "quét thanh khoản trước khi đảo" giải thích CƠ CHẾ VI MÔ khiến đảo chiều xảy ra chính xác tại các mức có stop cluster (không phải tại mọi điểm lệch xa ngẫu nhiên). Đây không phải hai lý thuyết cạnh tranh loại trừ nhau mà là hai tầng mô tả (thống kê vĩ mô vs cơ chế vi mô) của cùng một hiện tượng.
- *Giá trị của nhiều lớp xác nhận nằm ở việc giảm số lượng lệnh, không đảm bảo từng lệnh đúng:* SMT/timing/tốc độ không cần chứng minh mỗi lớp có ý nghĩa dự báo độc lập — vai trò thực tế của chúng là LỌC bớt số lượng setup được trade, giữ lại nhóm có nhiều tín hiệu đồng thuận nhất, tương tự cách một hệ thống định lượng dùng nhiều factor để giảm số lệnh nhưng tăng chất lượng trung bình — miễn là số lớp không tăng vô hạn chỉ để giải thích các trường hợp fail sau khi đã biết kết quả.

### 3. Giới hạn cứng phải chấp nhận (≥5)

1. Không có ngưỡng khách quan, được kiểm định công khai cho "displacement đủ mạnh" hay "reclaim đủ tin cậy" — mọi ngưỡng số đều là lựa chọn cá nhân/cộng đồng, chưa qua kiểm định thống kê ngoài mẫu quy mô lớn.
2. Việc phân loại một cú xuyên mức là "sweep" (hợp lệ) hay "break" (vô hiệu) chỉ có thể thực hiện SAU KHI nến đã đóng — tại thời điểm ra quyết định trong lúc nến đang hình thành, luôn có một khoảng không chắc chắn không thể loại bỏ.
3. Wick trên chart lịch sử không đảm bảo có thể khớp lệnh thật tại đó trong điều kiện live (đặc biệt quanh tin tức hoặc thanh khoản mỏng) — điều này làm mọi backtest dựa trên "entry tại đáy wick" có nguy cơ phóng đại expectancy thật (đã nêu ở W3).
4. Trên các cặp tài sản/thời điểm thanh khoản mỏng (crypto cuối tuần, FX phiên Á, sau giờ đóng RTH của futures), không có cách phân biệt chắc chắn giữa "sweep phản ánh hành vi tập thể thật" và "biến động giá do một lệnh lớn đơn lẻ hoặc thanh khoản mỏng gây ra" bằng việc chỉ quan sát hình dạng nến.
5. Chiến lược dựa trên sweep có độ trễ cấu trúc (phải chờ reclaim + displacement trước khi vào) — đây là đánh đổi cố hữu giữa an toàn hơn (tránh vào trước khi xác nhận) và giá vào lệnh kém hơn so với việc "đón đầu" cú sweep, không thể tối ưu cả hai đồng thời.

> [!quote] Kết luận trung thực
> Liquidity Sweep là một khung đọc order flow có cơ sở logic vững — quét thanh khoản trước khi đảo chiều là hành vi hợp lý về mặt thực thi lệnh lớn, không phải chuyện hoang đường. Nhưng các ngưỡng cụ thể (bao nhiêu % thân nến, bao nhiêu ATR) đều là lựa chọn tùy ý cần TỰ backtest và cứng hóa cho từng hệ thống cá nhân, không nên coi là chuẩn ngành đã được chứng minh. Đáng dùng ở mức **một bộ lọc timing + xác nhận trong một hệ thống có bias/POI xác định trước**, KHÔNG đáng dùng như một công cụ dự đoán chính xác từng cú quét sẽ đảo hay tiếp tục. Điều kiện dùng có trách nhiệm: cứng hóa ngưỡng đo lường được, tách riêng các mẫu trong khung giờ tin tức/thanh khoản mỏng khi backtest, và luôn coi reclaim + displacement là điều kiện CẦN chứ không phải ĐỦ để tự tin vào lệnh.

---

## 17. Edge Cases thực chiến

![[Liquidity-Sweep-Edge-Cases.svg|720]]
*EC5 minh họa: độ sâu sweep bất thường trên BTCUSD có thể là liquidation cascade giả dạng sweep chất lượng cao — luôn kiểm tra funding rate/OI trước khi tin tưởng.*

### EC1. Sweep trên chart CFD hụt vài điểm so với sweep trên futures gốc (đã có nền tảng ở W4, mở rộng thêm biến thể ngược)

**Tình huống:** biến thể ngược của W4 — chart CFD của bạn CHẠM và reclaim rõ ràng tại một mức, nhưng trên futures gốc (NQ), giá chỉ chạm hụt vài điểm rồi đảo, chưa thực sự "sweep" theo định nghĩa chuẩn (chưa xuyên qua pool thật).
**Vì sao bẫy:** trên chart CFD, hình dạng trông "hoàn hảo" hơn thực tế — dễ tự tin thái quá vào một setup mà thị trường gốc chưa hề xác nhận.
**Cách nhận diện sớm:** khi setup dựa vào một mức PDH/PDL/Asia H-L quan trọng, luôn mở song song chart futures gốc trước khi vào lệnh.
**Cách xử lý:** ưu tiên futures gốc làm bản đồ quyết định; nếu hai chart mâu thuẫn, hạ tier setup xuống hoặc bỏ qua.

### EC2. Sweep ngay trước/sau rollover contract quý — độ sâu sweep bị bóp méo bởi cost-of-carry gap

**Đã có nền tảng ở W6** — trọng tâm bổ sung ở đây: không chỉ vị trí pool bị lệch, mà ĐỘ SÂU của cú sweep (dùng để đánh giá "chữ ký" chất lượng theo mục 7.3) cũng bị bóp méo trong tuần rollover, khiến các phép đo tốc độ/độ sâu chuẩn không còn đáng tin cậy trong giai đoạn này — loại các mẫu tuần rollover khỏi thống kê `sweep_depth` và `sweep_speed`.

### EC3. Sweep trong nến gap thứ Hai — pool "cuối tuần" chưa từng được test bởi thanh khoản thật trong giờ giao dịch

**Tình huống:** giá gap qua một PDL/PWL vào phút mở phiên thứ Hai (đặc biệt sau một sự kiện cuối tuần: tin địa chính trị, on-chain event với crypto), "sweep" luôn ngay pool đó trong nến gap đầu tiên.
**Vì sao bẫy:** hình dạng giống sweep chuẩn (xuyên qua rồi có thể reclaim), nhưng gap nghĩa là không hề có dòng lệnh liên tục "chảy qua" mức đó — không có ai bị stop hunt theo đúng cơ chế W0 mô tả (thanh khoản không được "thu hoạch" tuần tự, mà bị nhảy qua).
**Cách nhận diện sớm:** kiểm tra biểu đồ có khoảng trống giá (gap) giữa nến đóng thứ Sáu và nến mở thứ Hai/thanh khoản đầu tiên không.
**Cách xử lý:** không áp dụng các rule đo lường "chữ ký sweep" (7.3) cho sweep hình thành từ gap; chờ ít nhất 2-3 nến ổn định đầu phiên trước khi đọc lại narrative.

### EC4. Sweep tại NFP/CPI/FOMC — mở rộng thêm biến thể "reclaim giả kéo dài" khác W1/W3

**Tình huống:** khác với W1 (reclaim doji thường) và W3 (fill giả trong wick), có biến thể thứ ba: nến tin tạo sweep + reclaim RÕ RÀNG (thân lớn, không doji) — nhưng 15-20 phút sau, một nến thứ hai (thường là nến phản ứng phái sinh/thanh khoản tổ chức vào muộn) quét NGƯỢC LẠI qua chính vùng đó theo hướng khác hoàn toàn.
**Vì sao bẫy được cả trader đã biết W1/W3:** nến đầu tiên thỏa mọi điều kiện "sweep hợp lệ" cả về hình dạng lẫn thời gian (không phải doji, không phải chờ trong lúc spike) — chỉ lộ ra là bẫy khi nến thứ hai xuất hiện.
**Cách nhận diện sớm:** trong 20-30 phút đầu sau tin lớn, luôn coi mọi "MSS xác nhận" là tạm thời (provisional) — không tăng size hay dời stop mạnh tay cho tới khi qua mốc 30 phút.
**Cách xử lý:** giữ size nhỏ hơn chuẩn trong 30 phút đầu sau tin lớn dù setup đã "xác nhận đầy đủ"; chỉ tăng về size chuẩn sau khi giá không có nhịp đảo ngược nào trong khung 30 phút.

### EC5. Sweep trên BTCUSD cuối tuần bị khuếch đại bởi liquidation cascade — độ sâu sweep không phản ánh thanh khoản tự nguyện

**Tình huống:** trên BTCUSD/ETHUSD, một sweep có độ sâu bất thường lớn (vượt xa "chữ ký" chuẩn ở mục 7.3) xảy ra khi thị trường có đòn bẩy cao và giá vừa chạm một mức thanh lý margin hàng loạt (liquidation cascade) — không phải vì có một bên "gom hàng" lớn theo đúng nghĩa W0 mô tả, mà vì lệnh thanh lý tự động kích hoạt dây chuyền.
**Vì sao bẫy:** độ sâu sweep lớn thường được đọc là "dấu hiệu smart money gom mạnh" (theo 7.3) — nhưng trong liquidation cascade, đó chỉ là hiệu ứng cơ học của đòn bẩy, không phản ánh ý định thật của bên nào.
**Cách nhận diện sớm:** kiểm tra open interest và funding rate trước cú sweep nếu có dữ liệu — funding rate cực đoan (dương hoặc âm mạnh) là dấu hiệu cảnh báo cascade sắp xảy ra.
**Cách xử lý:** hạ độ tin tưởng vào "chữ ký chất lượng" của sweep khi biết trước funding rate/OI đang ở mức cực đoan; ưu tiên chờ thêm xác nhận displacement THẬT (không phải chỉ độ sâu wick) trước khi vào.

### EC6. Sweep xảy ra đồng thời trên HTF và LTF nhưng theo HAI HƯỚNG NGƯỢC NHAU (fractal conflict)

**Tình huống:** H1 vừa sweep BSL (gợi ý bias giảm sắp tới), nhưng đồng thời trên M5, giá cũng vừa sweep một SSL nhỏ nội bộ (gợi ý một nhịp tăng ngắn hạn) — hai "sweep" hợp lệ về kỹ thuật nhưng ngụ ý hai hướng đối lập ở hai khung.
**Vì sao bẫy:** trader chỉ nhìn một khung tại một thời điểm dễ hành động theo tín hiệu của khung đang xem, bỏ sót mâu thuẫn từ khung khác.
**Cách nhận diện sớm:** luôn kiểm tra khung liền kề trên/dưới trước khi hành động theo một sweep — nếu có mâu thuẫn hướng rõ ràng, đó là dấu hiệu của một cấu trúc phức tạp hơn (có thể là distribution/re-accumulation), không phải sweep đơn giản.
**Cách xử lý:** khi có fractal conflict, ưu tiên hướng của khung cao hơn cho bias tổng thể, nhưng giảm size hoặc đứng ngoài cho tới khi khung thấp "đồng thuận" (không còn sweep ngược hướng) trong ít nhất 2-3 nến liên tiếp.

### EC7. Partial fill khi limit order đặt ngay tại vùng sweep — thuật toán front-run khiến giá không bao giờ chạm đủ sâu

**Tình huống:** đã xác nhận sweep + reclaim + displacement đầy đủ, đặt limit order chờ retrace vào FVG của displacement leg — nhưng giá chỉ chạm rìa xa của FVG (hoặc chạm thiếu 1-2 tick) rồi chạy tiếp, limit không khớp hoặc chỉ khớp một phần nhỏ.
**Vì sao bẫy:** sau khi đã "làm đúng mọi bước" xác nhận sweep, trader dễ chủ quan nghĩ phần khó nhất đã qua, quên rằng chính bước thực thi cuối cùng (limit fill) vẫn có rủi ro riêng, đặc biệt khi FVG mỏng hoặc trong kill zone nhiều thanh khoản cạnh tranh.
**Cách nhận diện sớm:** không thể biết trước chắc chắn, nhưng rủi ro cao hơn khi FVG có độ rộng dưới mức trung bình (ví dụ dưới 5-8 tick trên NQ) và đang trong giờ kill zone đông đúc.
**Cách xử lý:** đặt limit tại rìa GẦN của FVG (gần giá hiện tại hơn) thay vì rìa xa/giữa, đổi lấy tỷ lệ khớp cao hơn với entry hơi kém hơn một chút.

---

## 18. Case Studies chuyên sâu

> [!info] Bổ sung, không trùng với các case đã có
> Mục "Ví dụ chart" (§6) đã có 2 sequence mẫu (Long sau SSL / Short sau BSL) mang tính minh họa kỹ thuật thuần túy, và War Stories (W0-W6) là các tình huống tâm lý/vi cấu trúc. Bốn case dưới đây là NHẬT KÝ TRADE ĐẦY ĐỦ với timestamp, số liệu R cụ thể — dùng XAUUSD, NQ, EURUSD, ETHUSD để không trùng bộ instrument đã dùng trong case study của MSS (EURUSD-win/NQ-lose/XAUUSD-skip/BTCUSD-other) và Inducement (GBPUSD-win/ES-lose/XAUUSD-skip/BTCUSD-other) — ở đây đảo vai trò: XAUUSD đóng vai win, NQ đóng vai lose, EURUSD đóng vai skip, ETHUSD (thay vì BTCUSD, tránh trùng hình dạng multi-poke equal-highs đã dùng ở Inducement Case Study D) đóng vai "tài sản khác" với kịch bản single-poke hoàn toàn khác.

### Case Study A — XAUUSD, Short thắng đúng sách sau BSL Sweep tại premium

**Bối cảnh HTF:** XAUUSD, thứ Ba, Daily Bias Bearish (giá vừa fail tại D1 bearish OB 2 ngày trước, giữ dưới D1 midline). Dealing range H4: 2,355-2,410, giá hiện tại 2,398 (premium rõ).

**Setup:** H1 bearish OB tại 2,405-2,412 (POI thật). BSL target là đỉnh tuần trước (PWH) tại 2,415.

**Diễn biến & execution:**
- 08:40 NY: giá quét lên 2,417 (qua PWH — external sweep, không phải IDM vì đây là pool chính ở cực dealing range), đóng nến M15 trở lại 2,409 — reclaim rõ, thân nến reclaim chiếm ~65% range nến sweep (đạt chuẩn W1).
- 08:55: M5 phá xuống qua higher-low nội bộ 2,403 bằng nến thân lớn (~2.2x ATR(14) M5), để lại FVG 2,398-2,404 — MSS bearish xác nhận, displacement đạt chuẩn.
- 09:08: giá retrace lên 2,401 (trong FVG), Short khớp.
- Stop đặt tại 2,419 (trên sweep high, buffer 2 USD).
- Target 1: internal 2,370. Target 2: SSL sâu hơn 2,348.
- 12:30: chạm T1, dời stop về entry. 15:45: chạm T2, đóng lệnh.

**Kết quả bằng số:** Rủi ro 18 USD/oz. Lợi nhuận 53 USD/oz = **+2.94R**.

**Bài học chỉ rút ra được nhờ case này:** đây là ví dụ sách giáo khoa của external/structural sweep (không phải IDM) — pool bị quét (PWH) nằm ĐÚNG tại cực dealing range, không phải trung gian, và MSS xuất hiện ngay sau (khác hẳn sweep tại IDM, nơi giá tiếp tục đi mà không đảo ngay). Việc phân loại đúng vai trò của pool bị quét (theo bảng ở mục 14) là điều quyết định trước khi coi đây là entry hợp lệ.

![[Liquidity-Sweep-Case-Study.svg|720]]
*Diễn biến Case Study A: XAUUSD Short — BSL sweep PWH 08:40 → reclaim mạnh → MSS + FVG → entry 2,401 → target 2,348, +2.94R.*

### Case Study B — NQ, sweep "đẹp như sách" nhưng THUA vì bỏ qua chữ ký liquidation-style trong phiên có OPEX

**Bối cảnh HTF:** NQ, thứ Sáu OPEX (options expiration — thanh khoản và gamma exposure dealer cao bất thường), Daily Bias Bullish, giá test lại H1 bullish OB 18,240-18,270.

**Setup:** phía dưới OB, SSL tại đáy phiên Á 18,225. Trader áp dụng đúng toàn bộ checklist: chờ sweep + reclaim + displacement + MSS trước khi vào.

**Diễn biến & execution:**
- 09:50 NY: giá quét xuống 18,218 (qua SSL 18,225), đóng nến M5 trở lại 18,232 — reclaim đạt chuẩn (~58% thân nến).
- 09:58: M5 phá lên qua lower-high nội bộ 18,238 bằng nến thân lớn, để lại FVG 18,235-18,248 — MSS bullish xác nhận đầy đủ theo mọi tiêu chí đã học.
- 10:05: giá retrace vào FVG tại 18,240, Long khớp.
- Stop đặt tại 18,212 (dưới sweep low).
- 10:30: giá tăng lên 18,260 (gần chạm T1 18,265)... rồi đảo ngột ngạt, giảm thẳng xuyên qua entry, xuyên qua stop, chạm 18,205 trong vòng 12 phút — đặc trưng "giật cục bất thường quanh gamma wall" đã nêu ở mục 15 (bảng so sánh 3 thị trường): đúng ngày OPEX, dealer hedging flow tạo một cú đảo ngược mạnh hơn bất kỳ displacement thông thường, không liên quan gì tới cấu trúc IDM/POI đã phân tích.

**Kết quả bằng số:** Rủi ro 20 point × 20 USD = 400 USD/lot. Kết quả: **-1R**.

**Bài học chỉ rút ra được nhờ case này:** setup thỏa mọi điều kiện kỹ thuật chuẩn (sweep, reclaim, displacement, MSS, FVG entry) vẫn có thể thua vì một biến số nằm NGOÀI khung phân tích liquidity/structure thuần túy — dealer hedging flow quanh OPEX trên index futures là một lớp rủi ro riêng (đã nêu ở mục 15) cần được cộng thêm vào checklist cho các ngày OPEX, không chỉ dựa vào chất lượng sweep/MSS.

### Case Study C — EURUSD, đứng ngoài đúng vì "sweep" chỉ là break thật (acceptance), không phải rejection

**Bối cảnh HTF:** EURUSD, thứ Tư, Daily Bias Bullish, giá đang test PDL 1.0845 trong London KZ, kỳ vọng SSL sweep rồi đảo lên theo bias.

**Diễn biến & execution (quyết định KHÔNG vào):**
- 04:15 NY: giá xuyên xuống 1.0838, đóng nến M15 tại 1.0836 — giá đóng NGOÀI mức PDL, không phải reclaim bên trong (đây chính là break thật/acceptance, đã phân biệt ở mục 5: "Sweep thành công vs Sweep thất bại = Break").
- 04:30-05:00: giá tiếp tục dao động dưới PDL, không có dấu hiệu quay lại — thân nến các nến tiếp theo không cho thấy đảo, khối lượng bán vẫn chiếm ưu thế.
- Theo đúng checklist mục 8: "đóng nến ngoài mức = break, không phải sweep — không trade theo kịch bản sweep", trader giữ kỷ luật, KHÔNG cố gọi đây là "sweep sâu, sắp đảo" dù bias H4 vẫn là bullish.
- 08:20: giá tiếp tục giảm xuống 1.0790, xác nhận đây là một breakdown thật, không phải sweep — nếu đã Long "đón đầu" một cú sweep tưởng tượng tại 1.0838, lệnh sẽ lỗ nặng theo toàn bộ nhịp giảm sau đó.
- **Quyết định: đứng ngoài, ghi `outcome: break_not_sweep, action: skip` vào journal.**

**Kết quả bằng số:** 0R (không giao dịch) — tránh một lệnh Long ngược một breakdown thật đang hình thành.

**Bài học chỉ rút ra được nhờ case này:** ranh giới sweep vs break (mục 5) không phải lý thuyết suông — đây là ví dụ thực chiến nơi việc tuân thủ nghiêm ngặt định nghĩa "đóng nến bên trong = reclaim, đóng nến ngoài = break" đã bảo vệ trader khỏi một lệnh thua nặng, dù bias HTF vẫn đúng hướng dự kiến (bias đúng không có nghĩa mọi kịch bản dựa trên bias đó đều đúng thời điểm).

### Case Study D — ETHUSD, Long sau SSL Sweep đơn-lệnh (single-poke) xác nhận KHÔNG phải liquidation cascade

**Bối cảnh HTF:** ETHUSD, chiều thứ Ba (thanh khoản bình thường trong tuần, không phải cuối tuần — chủ đích chọn khung giờ này để tương phản với Case Study D của [[15-Inducement]], nơi bối cảnh là tối thứ Bảy thanh khoản mỏng), Daily Bias Bullish sau khi giá giữ vững trên D1 bullish OB 2 ngày liên tiếp. Giá quanh 3,180.

**Setup:** khác với kịch bản multi-poke equal-highs đã dùng ở Inducement Case Study D, đây là một pool ĐƠN LẺ (single old low, không phải equal lows dày) tại SSL 3,142 — đáy phiên Á duy nhất, chỉ chạm 1 lần trước đó. H1 bullish OB nằm ngay trên pool này tại 3,145-3,158.

**Diễn biến & execution (áp dụng EC5 dù đây không phải cuối tuần — funding rate vẫn cần kiểm tra bất kỳ khi nào sweep có vẻ "quá sâu"):**
- 14:20 UTC: giá thọc xuống 3,138 — SÂU HƠN bình thường so với biên độ dao động trung bình của ETHUSD phiên đó (đo bằng ATR(14) H1: cú thọc này gấp 2.3x ATR, một dấu hiệu CẦN kiểm tra theo EC5 dù không phải cuối tuần).
- Trader kiểm tra funding rate (đang dương nhẹ 0.02%, hoàn toàn bình thường) và OI (đi ngang, không tích lũy đòn bẩy) — xác nhận đây KHÔNG phải liquidation cascade, độ sâu bất thường chỉ do thanh khoản ETHUSD tại đúng phút đó mỏng hơn trung bình (không phải đòn bẩy quá tải).
- Vì đây là single-poke (không phải multi-poke như Inducement Case Study D), điều kiện vào khác hẳn: không cần chờ nhịp "rời pool" qua nhiều lần thọc — chỉ cần MỘT nến reclaim đủ chuẩn (thân ≥ 50% range nến sweep) là đủ, đúng theo rule W1 (không áp dụng rule multi-poke của mục 7 vì đây không phải equal-highs/lows dày).
- 14:21: nến reclaim đóng tại 3,159, thân nến chiếm 71% range nến sweep — đạt chuẩn W1 rõ ràng, không doji.
- 14:35: M15 phá lên qua lower-high nội bộ 3,163 bằng displacement (1.6x ATR M15), để lại FVG 3,155-3,161 — MSS bullish xác nhận.
- 14:50: giá retrace về 3,158 (trong FVG), Long khớp.
- Stop dưới sweep low 3,138, cộng buffer, đặt tại 3,131.
- Target: internal 3,225, sau đó BSL sâu hơn 3,268.
- 18:40 UTC: chạm T1, dời stop về entry. 22:15 UTC: chạm T2, đóng lệnh.

**Kết quả bằng số:** Rủi ro 27 USD/ETH. Lợi nhuận 110 USD/ETH = **+4.07R**.

**Bài học chỉ rút ra được nhờ case này (khác hẳn bài học của Inducement Case Study D):** không phải mọi sweep độ sâu bất thường trên crypto đều là cascade, và không phải mọi pool đáng ngờ đều là equal-highs/lows dày cần multi-poke — với pool ĐƠN LẺ, một nến reclaim đạt chuẩn là đủ điều kiện, miễn là đã loại trừ cascade bằng funding/OI. Bài học ở đây là **quy trình kiểm tra EC5 áp dụng cho MỌI độ sâu sweep bất thường, không chỉ giới hạn ở cuối tuần** — khác với Inducement Case Study D vốn tập trung vào rủi ro IDM giả do một lệnh lớn đơn lẻ tạo hình dạng equal-highs giả.

---
