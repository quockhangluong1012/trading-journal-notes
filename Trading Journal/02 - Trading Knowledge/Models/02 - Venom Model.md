---
type: ict-concept
concept: Venom Model
aliases:
  - Venom Model
  - Venom
  - The Venom Model
  - ICT Venom Model
tags:
  - trading/ict/concept
  - trading/study
  - "#Venom"
status: developing
category: Entry Model
last_reviewed: 2026-06-24
created: 2026-06-24
updated: 2026-07-28
---

# Venom Model

> [!summary] Tóm tắt 1 câu
> **Venom Model là một entry model dựa trên THỜI GIAN: trong cửa sổ kill zone (đặc biệt quanh NY open), giá quét thanh khoản của một phiên trước đó (Asia/London hoặc đỉnh/đáy session), rồi displacement phá cấu trúc để lại FVG — mình vào khi giá retrace về FVG, target là pool liquidity đối diện.**

> [!important] Nguyên tắc cốt lõi
> **Venom = TIME + LIQUIDITY SWEEP + DISPLACEMENT. Sức mạnh nằm ở việc "tiêm nọc" vào đúng cửa sổ thời gian: chờ giá quét liquidity của phiên trước trong kill zone, rồi mới displacement theo bias. Sai thời gian (ngoài cửa sổ) hoặc thiếu sweep = không phải Venom.**
> Đây là một biến thể time-based gần với Silver Bullet: cùng logic ICT 2022 (sweep → MSS → FVG) nhưng neo chặt vào khung giờ và liquidity của session.

---

## 1. Định nghĩa

**Khái niệm:**
Venom Model là **mô hình entry theo thời gian (time-based)** trong hệ ICT, tập trung vào việc khai thác **liquidity của các phiên trước** (Asia, London) hoặc đỉnh/đáy session ngay trong một **cửa sổ kill zone**, đặc biệt quanh **New York open**. Khi giá "tiêm nọc" — tức quét pool liquidity của session — và sau đó **displacement** theo bias để lại FVG, đó là tín hiệu vào lệnh. Về cơ chế, Venom dùng đúng chuỗi [[01 - ICT 2022 Model]] nhưng đặt nó trong một khung thời gian và một bộ liquidity reference cụ thể của phiên.

**Chuỗi điển hình của Venom:**
1. **Bias / khung tham chiếu:** xác định hướng (HTF bias) và các pool liquidity của phiên trước (Asia high/low, London high/low, PDH/PDL).
2. **Time window (cửa sổ Venom):** chỉ săn trong kill zone — phổ biến là quanh NY open / NY AM (xem [[18-Kill-Zones]]).
3. **Liquidity sweep ("venom strike"):** trong cửa sổ đó, giá quét một pool session (ví dụ quét London low) rồi reclaim.
4. **Displacement + MSS:** một move mạnh phá cấu trúc theo bias, để lại FVG.
5. **Entry tại FVG:** giá retrace về FVG (quanh CE), vào lệnh.
6. **Target:** pool liquidity đối diện (session high/low ngược phía, PDH/PDL).

**Bản chất:** Venom mã hóa quan sát rằng tại NY open, market maker thường **quét thanh khoản tích tụ từ phiên Á/Âu** trước khi chạy hướng thật trong ngày. Nó kết hợp **time** (chỉ trong cửa sổ) với **liquidity của session** làm reference, giúp lọc nhiễu và tập trung vào thời điểm xác suất cao nhất.

**Mục đích trong ICT:**
- Cho một **khung giờ + reference liquidity** cụ thể để chờ setup, thay vì săn cả ngày.
- Tận dụng động lực của **NY open** (volume, manipulation đầu phiên).
- Định nghĩa rõ pool nào để quét và pool nào làm target trong ngày.

**Vì sao khái niệm này quan trọng:**
Nhiều trader thua vì giao dịch **sai thời điểm** (giữa phiên chết, hoặc trước khi liquidity của session bị quét). Venom buộc bạn chỉ hành động trong cửa sổ chất lượng cao, sau khi "nọc" đã được tiêm (sweep).

**Nó giúp trả lời câu hỏi nào trên chart?**
- Đang ở trong cửa sổ Venom (kill zone) chưa?
- Giá đã quét liquidity của phiên trước (Asia/London/PD) chưa?
- Có displacement + FVG theo bias sau cú quét không?
- Pool đối diện nào là target trong ngày?

### Venom không phải là gì
- Không phải tín hiệu vào bất kỳ lúc nào — nó neo vào **time window**.
- Không phải "thấy FVG là vào" — phải có sweep liquidity session trước.
- Không phải bỏ qua HTF bias / premium-discount.
- Không phải scalping bừa quanh NY open mà không có reference.
- Không đảm bảo thắng; vẫn cần risk management.

### Vì sao NY open lại đặc biệt "độc" — cơ sở lý luận sâu hơn

> [!info] Đây không phải trùng hợp — có 3 lý do cấu trúc
> NY open không "ngẫu nhiên" tạo ra sweep chất lượng cao. Ba cơ chế thị trường cộng dồn tại đúng khung giờ này khiến nó trở thành điểm áp lực thanh khoản lớn nhất trong ngày (sau Silver Bullet AM).

1. **Chồng lấn thanh khoản London–New York (session overlap):** Từ ~07:00–09:30 NY time, phiên London vẫn hoạt động trong khi bàn giao dịch NY bắt đầu vào lệnh. Đây là khung giờ có **khối lượng giao dịch lớn nhất trong ngày** trên FX và index vì hai trung tâm tài chính lớn nhất (London, New York) cùng hoạt động song song. Volume lớn = đủ "nhiên liệu" để một cú sweep quét sạch stop-loss tích lũy từ Asia + London mà không cần tin tức.
2. **Cụm lịch kinh tế Mỹ neo quanh NY open:** Phần lớn dữ liệu kinh tế Mỹ có sức ảnh hưởng cao (CPI, NFP, Retail Sales, FOMC-adjacent releases) được công bố lúc **08:30 NY time**, tức ngay trong hoặc sát cửa sổ Venom. Cú "giật" thanh khoản quanh các mốc này thường bị hiểu nhầm là random nhưng thực chất là phản ứng dồn dập của order flow tổ chức đúng vào khung Venom.
3. **"Reference price reset" của thuật toán tại cash open (09:30):** 09:30 NY là mốc mở cửa chính thức của NYSE/Nasdaq cash market. Nhiều thuật toán định giá lại (re-price) tài sản phái sinh (futures, CFDs) dựa trên cash open này — tạo ra một "điểm neo" giá mới. Range hình thành từ 08:00–09:30 (pre-market) thường bị quét ngay sau 09:30 vì thuật toán cần "dọn" thanh khoản cũ trước khi thiết lập xu hướng thật của phiên cash.

> [!tip] Ghi nhớ
> Venom không "đoán" giá đi đâu — nó khai thác một hiện tượng lặp lại: **volume cao (overlap) + tin tức cụm (08:30) + reset thuật toán (09:30 cash open) → quét thanh khoản pre-market/session trước, rồi mới chạy hướng thật.**

### Cửa sổ thời gian chính xác — "vùng cắn của Venom"

| Khung (NY time) | Tên gọi | Vai trò |
|---|---|---|
| 07:00–09:30 | **Venom Box / Pre-market range** | Hình thành range tham chiếu (high/low) — KHÔNG vào lệnh, chỉ đánh dấu pool. |
| 08:30 | **News cluster** | Nhiều tin Mỹ công bố — có thể tạo biến động giả, cẩn trọng. |
| 09:30–10:30 | **Venom Cutting Zone (cửa sổ vào lệnh chính)** | Cash market mở cửa → kỳ vọng sweep Venom Box hoặc session pool + displacement + FVG. Đây là cửa sổ săn lệnh chính thức. |
| 10:30–10:45 | **Vùng suy yếu (fading window)** | Động lực NY AM thường cạn dần; xác suất setup sạch giảm rõ rệt. |

> [!warning] Múi giờ — luôn quy đổi trước khi trade
> Toàn bộ mốc trên tính theo **New York time (ET)**. Vault chưa xác định rõ múi giờ sinh hoạt của bạn — trước phiên, hãy tự quy đổi 07:00/08:30/09:30/10:30 NY time sang giờ địa phương của bạn (lưu ý DST: ET lệch UTC-5 hoặc UTC-4 tùy mùa) và ghi thẳng giờ local vào Quick Reference Card mỗi ngày để tránh tính nhầm.

**Khung quyết định cho 10–15 phút cuối cửa sổ (khi động lực đang cạn dần, ~10:15–10:30 NY):**

| Tình huống | Hành động khuyến nghị |
|---|---|
| Đã có sweep + displacement + FVG sạch, chưa kịp entry | Vẫn có thể vào nếu FVG mới hình thành và retrace hợp lý — nhưng giảm size, vì R:R còn lại trong ngày cho move tiếp theo bị co hẹp. |
| Mới chỉ có sweep, chưa có displacement rõ | **Bỏ qua** — displacement xuất hiện trễ trong cửa sổ thường yếu, dễ bị chặn giữa chừng (chop). |
| Chưa có gì (chưa sweep) | **Không săn nữa** — coi như hôm nay "miss" Venom, chuyển sang chờ Silver Bullet AM/Lunch hoặc no-trade. |
| Đã có lệnh đang chạy từ đầu cửa sổ | Quản lý lệnh bình thường theo plan; không mở thêm lệnh Venom mới sau 10:30. |

### So sánh Venom qua các thị trường đang giao dịch

| Thị trường | Pool hay bị quét nhất | Đặc điểm riêng | Lưu ý khi áp dụng Venom |
|---|---|---|---|
| **NQ1 / NDX (NAS100)** | High/Low của **pre-market range (Venom Box 08:00–09:30)** | Rất nhạy với thanh khoản cash open; futures có sẵn volume xuyên đêm nên pre-market range rõ và đáng tin. | Đây là thị trường "chuẩn" mà Venom được mô tả phổ biến nhất — ưu tiên setup NQ1/NDX khi mới học model. |
| **EURUSD / GBPUSD** | **High/Low phiên London** (vì London đã thiết lập range đầu ngày trước khi NY vào) | Không có "cash open" như index; động lực đến từ overlap London-NY và tin tức Mỹ 08:30. | Pool tham chiếu chính là London high/low thay vì pre-market box; London low/high thường đóng vai trò như "Asia high/low" đóng vai trò với London trước đó. |
| **XAUUSD** | **Range phiên Á (Asia high/low)** làm pool tham chiếu phổ biến, đôi khi kết hợp London range | Cực nhạy tin tức (DXY, lợi suất trái phiếu Mỹ, CPI/NFP) — dễ bị "spike giả" không theo cấu trúc kỹ thuật thuần túy. | Cẩn trọng hơn với size quanh 08:30 news cluster; XAU dễ tạo sweep "quá tay" (quét sâu hơn bình thường) rồi đảo chiều mạnh — chờ FVG/MSS rõ ràng hơn là vào sớm theo sweep. |

### Phân biệt Venom vs Silver Bullet khi hai cửa sổ chồng lấn

> [!important] Vấn đề thực tế
> Cửa sổ Silver Bullet AM (thường 10:00–11:00 NY time) **chồng lấn một phần** với cuối Venom Cutting Zone (09:30–10:30) và vùng suy yếu (10:30–10:45). Nhiều trader nhầm lẫn hai model khi setup rơi vào khoảng 10:00–10:30.

| Tiêu chí | Venom | Silver Bullet |
|---|---|---|
| Pool bị quét | Liquidity **session/pre-market cụ thể** (Venom Box, Asia/London high-low, PDH-PDL) | Bất kỳ liquidity pool gần nhất (swing high/low gần đó), không nhất thiết là pool "cấp session" |
| Trọng tâm | **Time + đúng loại pool** (phải là pool session) | **Time + FVG** trong giờ, không đòi hỏi pool phải là mốc session |
| Cửa sổ đặc trưng | 09:30–10:30 (đặc biệt sát 09:30, gắn liền cash open) | 10:00–11:00 (AM), 14:00–15:00 (PM), 03:00–04:00 (London) |
| Câu hỏi phân biệt | "Pool vừa bị quét có phải là high/low của session/pre-market không?" | "Có FVG hình thành trong giờ Silver Bullet không, bất kể pool là gì?" |
| Khi trùng cả hai | Nếu sweep đúng pool session **và** nằm trong 10:00–10:30 → gọi là **Venom** (ưu tiên tên gọi theo pool bị quét, vì đó là yếu tố đặc trưng hơn); nếu chỉ là swing high/low nhỏ lẻ không phải pool session → gọi là **Silver Bullet**. |

> [!tip] Quy tắc thực dụng
> Không cần tranh cãi tên gọi khi vào lệnh — điều quan trọng là **pool nào bị quét và có displacement/FVG hợp lệ hay không**. Tên model chỉ hữu ích khi backtest/review để phân loại dữ liệu (`time_window` field trong frontmatter trade).

![[Venom-Session-Timeline-Diagram.svg]]
> [!info] Mô tả hình
> Timeline ngang thể hiện 3 phiên Asia (18:00–03:00 NY), London (03:00–09:30 NY), New York (09:30–16:00 NY). Vùng 07:00–09:30 là "Venom Box hình thành"; khung 09:30–10:30 tô đậm là "Venom Cutting Zone"; vùng nhạt 10:30–10:45 là "Fading Window". Sơ đồ khái niệm định vị các khung giờ, không phải dữ liệu giá thật.

---

## 2. Bối cảnh sử dụng

### Các bước & khái niệm tương ứng

| Bước | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| 1 | Bias + reference | [[59-Daily-Bias]], [[19-Liquidity]] | Hướng gì? Pool session nào? |
| 2 | Time window | [[18-Kill-Zones]] | Đang trong cửa sổ Venom (NY open) chưa? |
| 3 | Liquidity sweep | [[20-Liquidity-Sweep]] | Đã quét Asia/London/PD pool chưa? |
| 4 | Displacement + MSS | [[Displacement]], [[21-Market-Structure-Shift]] | Có phá cấu trúc + FVG không? |
| 5 | FVG entry | [[Fair Value Gap]], [[Optimal Trade Entry]] | FVG/CE ở đâu, đúng PD không? |
| 6 | Target | [[19-Liquidity]] | Pool đối diện ở đâu? |

### Biến thể thường gặp
- **+ Silver Bullet:** Venom rất gần Silver Bullet — chạy chuỗi trong cửa sổ 1 giờ của kill zone ([[18-Kill-Zones]]).
- **+ ICT 2022 Model:** lõi entry chính là chuỗi [[01 - ICT 2022 Model]] đặt trong time window.
- **+ OTE:** tinh chỉnh entry bằng OTE 62–79% trùng FVG ([[Optimal Trade Entry]]).
- **+ AMD:** sweep đầu NY ~ pha manipulation; displacement ~ distribution ([[02-AMD]]).

> [!tip]
> Cách nhớ nhanh Venom: **"Đúng giờ → Tiêm nọc (sweep session) → Đẩy (displacement) → Vào FVG → Chạy về pool đối diện."** Thiếu "đúng giờ" hoặc "tiêm nọc" thì không phải Venom.

### Khi nào mô hình này có giá trị cao?
- [ ] Đang trong cửa sổ Venom (NY open / NY AM kill zone).
- [ ] Có pool liquidity session rõ (Asia/London high-low, PDH/PDL).
- [ ] HTF bias rõ ràng + giá ở premium/discount phù hợp.
- [ ] Sweep session + displacement để lại FVG sạch.
- [ ] Pool đối diện làm target có room.

### Khi nào nên bỏ qua?
- [ ] Ngoài cửa sổ thời gian (giữa phiên chết).
- [ ] Chưa quét liquidity session nào.
- [ ] Bias mơ hồ / ngược premium-discount.
- [ ] Sát tin tức lớn (làm nhiễu displacement đầu phiên).
- [ ] Không có target pool rõ.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Reference session pools:** Asia high/low, London high/low, PDH/PDL đánh dấu sẵn.
2. **Time window:** giá đang ở trong cửa sổ NY open / kill zone.
3. **Sweep session ("venom strike"):** giá quét một pool session rồi reclaim.
4. **Displacement + MSS:** move mạnh phá cấu trúc, để lại FVG.
5. **Retrace về FVG:** điểm vào (quanh CE), đúng PD.

### Ma trận nhận diện Venom (Long)

| Bước | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Bias | HTF bullish, target BSL | Bias mơ hồ → bỏ |
| Time | Trong cửa sổ NY open | Ngoài cửa sổ → không phải Venom |
| Sweep | Quét session low (Asia/London) + reclaim | Không sweep → bỏ |
| Displacement/MSS | Phá swing high + bullish FVG | Move yếu → bỏ |
| Entry | FVG ở discount | Ở premium → sai chỗ |
| Target | Session high / PDH | Không pool rõ → R:R kém |

### Điều kiện bắt buộc
- [ ] Đang trong cửa sổ thời gian Venom (kill zone).
- [ ] Đã quét một pool liquidity session.
- [ ] Có displacement + MSS để lại FVG theo bias.
- [ ] Xác định FVG/CE + invalidation.
- [ ] Pool đối diện làm target rõ.

### Điều kiện tăng xác suất
- [ ] FVG trùng OTE 62–79% / OB (confluence).
- [ ] Sweep đúng pool session quan trọng (London low/high).
- [ ] Đồng hướng HTF bias + AMD distribution.
- [ ] Target có room lớn (R:R cao).

### Điều kiện làm setup yếu đi
- Sweep mờ / không reclaim rõ.
- Displacement không dứt khoát, FVG bị lấp nhanh.
- Gần cuối cửa sổ thời gian (động lực cạn).
- Vướng tin tức cùng phiên.

### Giải phẫu một "venom strike" hợp lệ — đọc sâu hơn cú sweep

> [!example] 4 câu hỏi để xác nhận đây đúng là "venom strike" chứ không phải một cú giá đi ngẫu nhiên
> 1. **Pool bị quét có phải là mốc session/pre-market rõ ràng không** (Venom Box high/low, Asia/London high-low, PDH/PDL) — hay chỉ là một swing nhỏ lẻ ngẫu nhiên?
> 2. **Cú quét có "reclaim" không** — tức giá đóng nến trở lại bên trong range sau khi thò ra ngoài pool? Quét mà không reclaim (đóng nến ngoài pool luôn) thường là breakout thật, không phải sweep thao túng.
> 3. **Wick quét có đủ "sạch" không** — một wick dài, thân nến nhỏ, thể hiện rõ việc "thò ra rồi rút về" trong 1–3 nến, tốt hơn nhiều nến dùng dằng quanh pool.
> 4. **Volume/momentum tại thời điểm quét có tăng đột biến không** (nếu chart có volume) — xác nhận đây là nơi dòng lệnh lớn vào, không phải trôi giá do thanh khoản mỏng.

**Phân biệt sweep "khỏe" và sweep "yếu":**

| Đặc điểm | Sweep khỏe (đáng tin) | Sweep yếu (nên bỏ) |
|---|---|---|
| Hình dạng nến | Wick dài, đóng cửa quay lại trong range | Đóng cửa ngoài range (acceptance), không reclaim |
| Tốc độ | Quét nhanh (1–3 nến M1/M5), dứt khoát | Lình xình nhiều nến quanh pool, không rõ ý đồ |
| Vị trí trong cửa sổ | Trong 09:30–10:15 (còn "nhiên liệu" thời gian) | Cuối cửa sổ 10:15–10:30 (dễ là move cạn, không theo sau bởi displacement thật) |
| Theo sau bởi | Displacement + MSS rõ ràng, để lại FVG sạch | Không có gì theo sau, giá đi ngang hoặc quét tiếp pool khác |

![[Venom-Strike-Recognition-Chart.svg]]
> [!info] Mô tả hình
> Biểu đồ nến M5/M15 minh họa: (1) đường ngang "Pre-market/Session Low" (pool tham chiếu); (2) một nến wick dài thò xuống dưới đường đó rồi đóng cửa trở lại phía trên ("Venom Strike – sweep + reclaim"); (3) chuỗi nến displacement tăng mạnh phá swing high gần nhất ("Displacement + MSS"); (4) vùng FVG tô màu giữa các nến displacement ("FVG – POI chờ retrace"). Biểu đồ ví dụ khái niệm, không dùng dữ liệu giá thật của một lệnh cụ thể.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Venom
> 1. **Đang trong cửa sổ Venom (NY open/kill zone) chưa?**
> 2. **Giá đã quét pool liquidity session nào chưa?**
> 3. **Có displacement + MSS để lại FVG theo bias không?**
> 4. **Entry/stop/target ở đâu, R:R bao nhiêu?**

### D1 / H1 — Bias & Reference
- **Bias:** Bullish / Bearish (xem [[59-Daily-Bias]]).
- **Reference pools:** Asia/London high-low, PDH/PDL.
- **Premium/Discount:** xác định vùng vào phù hợp với bias.

### M15 — Setup & Context
- **Pool sẽ bị sweep:** chọn pool session ngược hướng bias.
- **Chờ sweep + reclaim:** trong cửa sổ thời gian.
- **MSS + FVG:** ghi range FVG + CE, ví dụ `M15 bullish FVG 17840–17865, CE 17852`.

### M5 / M1 — Confirmation & Entry
- **Refine:** chờ M5/M1 retrace về FVG; có thể chờ M1 MSS xác nhận.
- **Entry:** tại FVG (quanh CE) / OTE trùng FVG.
- **Stop:** ngoài điểm sweep / đầu kia FVG.
- **Target:** pool session đối diện / PDH-PDL.

```text
Mẫu ghi nhanh — Venom Long
Bias (HTF): Bullish | Target: session high / PDH @ [level]
Time window: NY open / NY AM kill zone
(1) Sweep: session low (Asia/London) @ [level] + reclaim
(2) Displacement + MSS phá [swing high] → FVG
(3) FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop dưới sweep
(5) Target: session high / PDH [..]
Invalid: ngoài cửa sổ / đóng nến dưới FVG
```

> [!warning]
> **Time là một bộ lọc bắt buộc, không phải tùy chọn.** Một setup "đẹp" nhưng nằm ngoài cửa sổ Venom thì không phải Venom — động lực và xác suất của NY open chính là phần "nọc" của mô hình.

### Đối chiếu trực quan Venom vs Silver Bullet

Khi phân tích đa khung thời gian, bước đầu tiên trước khi chạy quy trình 4 câu là **xác định đang săn model nào** — vì reference pool để đối chiếu ở bước D1/H1 sẽ khác nhau (pool session cấp cao cho Venom, swing gần nhất cho Silver Bullet). Xem lại bảng phân biệt tiêu chí ở mục 1.

![[Venom-vs-SilverBullet-Window-Comparison.svg]]
> [!info] Mô tả hình
> Sơ đồ so sánh 2 cột song song trên cùng trục thời gian (07:00–11:00 NY). Cột trái "Venom": highlight 09:30–10:30, pool bị quét là "Pre-market/Session High-Low". Cột phải "Silver Bullet AM": highlight 10:00–11:00, pool bị quét là "Swing high/low gần nhất (bất kỳ)". Vùng chồng lấn 10:00–10:30 tô màu riêng, chú thích "Vùng dễ nhầm lẫn — phân biệt bằng loại pool bị quét, không phải bằng giờ". Sơ đồ khái niệm đối chiếu hai model, không phải chart giao dịch thật.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Trong cửa sổ thời gian Venom (kill zone).
- [ ] Có sweep pool liquidity session + reclaim.
- [ ] Displacement + MSS để lại FVG theo bias.
- [ ] Entry tại FVG (retrace), đúng premium/discount.
- [ ] Stop ngoài sweep; target pool đối diện rõ; R:R đạt.

### Setup bị vô hiệu khi
- [ ] Ngoài cửa sổ thời gian → không phải Venom.
- [ ] Chưa quét liquidity session.
- [ ] Displacement yếu / không để lại FVG.
- [ ] Giá **đóng nến xuyên qua FVG** (acceptance) → POI invalid.
- [ ] Entry ngược bias / sai premium-discount / chase.

### Mức độ "đủ điều kiện"

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Trong cửa sổ + sweep + displacement + FVG | **A+ Venom** | Thực thi theo plan |
| Có sweep + displacement nhưng FVG đã lấp | **Chờ POI khác** | Tìm FVG/OB tiếp theo |
| Setup đẹp nhưng ngoài cửa sổ | **Không phải Venom** | Bỏ hoặc xét model khác |
| Chưa quét session pool | **Chưa đủ** | Chờ "nọc" được tiêm |

> [!note]
> Venom là Silver Bullet "có chủ đích về liquidity session": ngoài time window, nó nhấn mạnh việc quét đúng pool của phiên trước. Khi bí, kiểm tra hai thứ: **đúng giờ chưa** và **đã quét session pool chưa**.

---

## 6. Ví dụ chart

### Ví dụ đúng — NY open: sweep London low → displacement → FVG entry → session high
![[Venom-Example-Correct-NYOpen-Sweep.svg]]
> [!info] Mô tả hình
> Chart nến minh họa chuỗi Venom hợp lệ: (1) sweep London Low + reclaim; (2) displacement tăng + MSS phá swing high để lại FVG; (3) entry tại FVG quanh CE; (4) giá chạy về session high / PDH target.

**Mô tả:**
HTF bias Bullish, target là session high / PDH. **(1)** Vào **NY open kill zone**, giá **quét London low** (liquidity session) rồi reclaim. **(2)** **Displacement tăng + MSS** phá swing high, để lại bullish FVG. **(3)** Giá retrace về FVG (quanh CE) → **entry**, stop dưới điểm sweep. **(4)** Giá chạy về **session high / PDH target**.

**Vì sao đây là ví dụ tốt:**
- Đúng cửa sổ thời gian (NY open) + quét đúng session pool.
- Đủ chuỗi sweep → displacement → FVG retrace.
- Entry ở discount, không chase; target pool rõ.

### Ví dụ sai / dễ nhầm — Vào ngoài cửa sổ, chưa quét session pool
![[Venom-Example-Wrong-OutsideWindow.svg]]
> [!info] Mô tả hình
> Chart minh họa lỗi: giữa phiên chết (ngoài cửa sổ Venom), một FVG "đẹp" xuất hiện nhưng chưa có sweep session pool nào trước đó. Entry tại FVG này (đánh dấu X đỏ) dẫn tới giá đi loanh quanh rồi quét stop — vì thiếu cả hai bộ lọc bắt buộc (time + liquidity session).

**Mô tả lỗi:**
Trader thấy một FVG đẹp **giữa phiên chết** (ngoài cửa sổ Venom) và vào ngay, dù **chưa có cú quét liquidity session** nào. Thiếu cả "đúng giờ" lẫn "tiêm nọc", giá đi loanh quanh rồi quét stop.

**Bài học:**
- Ngoài cửa sổ thời gian → không phải Venom, dù FVG có đẹp.
- Phải có sweep session pool trước displacement.
- Time + liquidity session là hai bộ lọc không thể bỏ.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[59-Daily-Bias]]
- [[19-Liquidity]]
- [[20-Liquidity-Sweep]]
- [[Displacement]]
- [[21-Market-Structure-Shift]]
- [[Fair Value Gap]]
- [[Optimal Trade Entry]]
- [[27-Premium-Discount]]
- [[18-Kill-Zones]]
- [[02-AMD]]
- [[01 - ICT 2022 Model]]
- [[03 - One Shot One Kill Trading Model]]

### Sequence mẫu — Venom Long (đầy đủ)
```text
(1) HTF Bullish bias + reference pools (Asia/London/PD)
(2) Trong cửa sổ Venom (NY open / NY AM kill zone)
(3) Sweep session low (+ reclaim) = "venom strike"
(4) Displacement tăng + MSS → bullish FVG
(5) Entry: retrace về FVG (quanh CE), lý tưởng trùng OTE/OB
(6) Stop dưới điểm sweep; Target: session high / PDH
(+ đồng hướng AMD distribution)
```

> [!note]
> Venom, Silver Bullet và [[01 - ICT 2022 Model]] dùng chung lõi (sweep → MSS → FVG). Điểm khác của Venom là **neo vào time window NY open + liquidity của session trước**. Kết hợp tốt với [[03 - One Shot One Kill Trading Model]] khi muốn chọn một phát chất lượng trong ngày.

---
## Chuyên sâu A — Edge cases & Failure modes (thực chiến Venom)

![[Venom-Advanced-EdgeCase-Matrix.svg|720]]

Sáu tình huống dưới đây là những chỗ chuỗi Venom (time → sweep → displacement → FVG) hay gãy trong thực tế mà lý thuyết gọn gàng không nhắc tới. Với mỗi ca: dấu hiệu nhận biết → cơ chế → cách xử lý.

**① Window creep — nới cửa sổ quá 10:30 rồi dán nhãn "Venom".**
Dấu hiệu: đã quá 10:30 NY time mà chưa có setup, bạn tự nhủ "chờ thêm chút" đến 10:45–11:00 rồi vào một lệnh muộn và vẫn ghi sổ là Venom. Cơ chế: động lực NY AM cạn dần sau 10:30, cái "sweep/displacement" xuất hiện muộn phần lớn là **Silver Bullet muộn** hoặc noise, không còn dòng lệnh cash-open đứng sau. **Xử lý:** đặt hard cutoff 10:30 (alarm thật, không "nhớ trong đầu"); sau mốc đó chưa vào = "miss Venom hôm nay", chuyển model hoặc no-trade. Nếu vẫn vào, đừng gắn nhãn Venom — ghi đúng `time_window` để dữ liệu không bị nhiễm.

**② News spike ≠ Venom strike.**
Dấu hiệu: quanh 08:30 CPI/NFP giá giật mạnh xuyên một pool, trông như "sweep" nhưng **không có reclaim + displacement sạch** — chỉ là một cú one-way hỗn loạn (đặc biệt XAUUSD). Cơ chế: spike do tin là phản ứng volatility tức thời, chưa phải chuỗi thao túng thanh khoản có chủ đích; wick "quá tay" của XAU dễ nuốt luôn pool rồi đảo chiều mạnh. **Xử lý:** đứng ngoài 15–30 phút đầu sau tin, chờ biến động lắng; chỉ tính là venom strike khi có đủ **sweep + reclaim** (đóng nến lại trong range) **+ displacement** sạch. Không nhầm "nến to do tin" với "nọc đã tiêm".

**③ Sweep KHÔNG reclaim cuối cửa sổ.**
Dấu hiệu: giá xuyên session pool nhưng **đóng nến luôn ở ngoài pool**, nhất là sát 10:15–10:30. Cơ chế: đóng ngoài pool = acceptance, có thể là **breakout thật đổi hướng** chứ không phải quét thanh khoản → bias trong ngày có thể đang đảo. **Xử lý:** chưa phải sweep hợp lệ; chờ nến đóng trở lại bên trong range mới coi là reclaim. Không reclaim → đứng ngoài, xem lại hướng draw ngắn hạn thay vì cố long/short theo "sweep".

**④ DST / timezone miscalc.**
Dấu hiệu: bạn quy đổi 09:30 ET sang giờ local nhưng lệch 1 giờ, dẫn tới săn nhầm cửa sổ (vào lúc thị trường thực ra chưa mở cash, hoặc đã qua cutoff). Cơ chế: ET lệch **UTC-5 (mùa đông)** hoặc **UTC-4 (mùa hè DST)**, và Mỹ đổi DST không cùng ngày với châu Âu/địa phương bạn → công thức quy đổi cũ sai vài tuần trong năm. **Xử lý:** mỗi ngày quy đổi lại 07:00/08:30/09:30/10:30 NY time sang giờ local và ghi thẳng vào Quick Reference Card; kiểm tra lại mốc DST khi qua tháng 3 và tháng 11.

**⑤ Sai loại pool.**
Dấu hiệu: bạn gọi một cú quét là venom strike nhưng cái bị quét chỉ là một **swing nhỏ ngẫu nhiên** trong cửa sổ, không phải session pool. Cơ chế: sức mạnh Venom nằm ở việc quét đúng **pool cấp session** (Venom Box high/low, Asia/London high-low, PDH/PDL) — nơi stop tích lũy thật; quét một swing lẻ M1 không giải phóng đủ thanh khoản để đứng sau displacement bền. **Xử lý:** trước 09:30 đánh dấu sẵn các pool session; trong cửa sổ chỉ tính sweep khi nó chạm đúng một trong các mốc đã đánh dấu. Nếu chỉ là swing lẻ → đó là Silver Bullet, phân loại đúng, đừng ép thành Venom.

**⑥ Displacement trễ & yếu.**
Dấu hiệu: có sweep nhưng displacement chỉ xuất hiện **10:15–10:30**, thân nến ngắn, đi được một đoạn rồi chop. Cơ chế: cuối cửa sổ hết "nhiên liệu" thời gian, order flow cash-open đã xả xong nên move không đủ lực để chạy về pool đối diện. **Xử lý:** hạ cấp về "chờ xác nhận" — nếu displacement không dứt khoát (không phá cấu trúc sạch, FVG mỏng/lấp nhanh) thì bỏ; đừng vào chỉ vì "đã có sweep rồi".

**⑦ Range tham chiếu chủ quan — hindsight-fit pool theo kết quả.**
Dấu hiệu: sau khi thấy giá đã chạy đúng hướng, bạn "chọn lại" mốc pool (Asia low thay vì pre-market low, hoặc PDL thay vì Venom Box low) sao cho câu chuyện sweep trở nên đẹp hơn. Cơ chế: Venom không có một định nghĩa pool phổ quát được kiểm chứng độc lập — "pool cấp session" có thể là Asia range, pre-market 07:00–09:30, hoặc PDH/PDL tùy người dùng, và việc chọn sau khi biết kết quả gần như luôn thiên vị về phía xác nhận (confirmation bias). **Xử lý:** cố định trước 1 quy tắc chọn pool cho mỗi thị trường (xem Chuyên sâu B #3) và ghi vào trade log field `pool_type_used`; không đổi quy tắc giữa các ngày để "khớp" với setup vừa thấy.

**⑧ Phụ thuộc timezone — lệch giờ quanh mốc đổi DST.**
Dấu hiệu: khung giờ 07:00/09:30/10:30 NY time bạn quy đổi ra giờ local bị lệch 1 giờ trong 1–3 tuần quanh Chủ Nhật thứ 2 tháng 3 và Chủ Nhật đầu tháng 11 (Mỹ đổi DST không cùng ngày với châu Âu). Cơ chế: nếu bạn dùng một bảng quy đổi giờ cố định lưu sẵn (không cập nhật theo DST hiện tại), toàn bộ cửa sổ Cutting Zone bị dịch pha 60 phút mà bạn không nhận ra ngay. **Xử lý:** đây là biến thể sâu hơn của case ④; ngoài quy đổi mỗi ngày, đặt một nhắc nhở lịch vào các mốc đổi DST (giữa tháng 3, đầu tháng 11) để kiểm tra lại toàn bộ bảng giờ, không chỉ riêng ngày đổi.

**⑨ Volume/liquidity giả trên thị trường ít thanh khoản (altcoin CFD, exotic FX).**
Dấu hiệu: bạn áp mô hình Venom (được thiết kế cho NQ1/ES, EURUSD, XAUUSD — các thị trường có dòng lệnh tổ chức quanh cash open Mỹ) lên một cặp tiền exotic hoặc CFD ít thanh khoản, nơi "sweep" có thể chỉ do một lệnh lớn đơn lẻ hoặc broker re-quote, không phải dấu vết dòng lệnh thật. Cơ chế: cơ sở lý luận của Venom (mục 1) dựa trên giả định có đủ dòng lệnh tổ chức đứng sau NY cash open; thị trường mỏng không có "cash open" tương đương nên toàn bộ logic sweep→displacement mất nền tảng. **Xử lý:** giới hạn áp dụng Venom cho các thị trường đã liệt kê có volume đủ lớn (mục "So sánh Venom qua các thị trường"); với thị trường lạ, backtest riêng ≥30-50 mẫu trước khi tin.

**⑩ Đa khung giờ mùa hè/mùa đông của chính thị trường giao dịch (không phải chỉ giờ trader).**
Dấu hiệu: London mở cửa DST khác Mỹ — có giai đoạn trong năm London/NY overlap dịch chuyển, làm phiên "London" mà bạn quy ước 03:00–09:30 NY thực ra không còn khớp với giờ giao dịch thật của London. Cơ chế: bảng giờ phiên trong mục 1 giả định NY time cố định nhưng biên giới các phiên Asia/London do sàn/thị trường tại địa phương quyết định theo giờ local của họ, không di chuyển cùng tốc độ với DST Mỹ. **Xử lý:** mỗi lần đổi DST, kiểm tra lại không chỉ giờ cửa sổ Venom mà cả biên giới 3 phiên Asia/London/NY đã dùng làm base.

**⑪ Tự tin thái quá sau một chuỗi thắng ngắn (recency bias trên mẫu nhỏ).**
Dấu hiệu: sau 5–7 lệnh Venom thắng liên tiếp trên một thị trường, bạn tăng size hoặc nới điều kiện vào lệnh (bỏ qua vài core component) vì "đang có duyên". Cơ chế: với cỡ mẫu 5-7, một chuỗi thắng hoàn toàn có thể là biến động ngẫu nhiên của một hệ thống có winrate thực 50-55%, không phải bằng chứng edge tăng lên; não người có xu hướng đọc pattern giả (Chuyên sâu B #7 đã nêu ngưỡng ≥30-50 mẫu). **Xử lý:** cố định size theo kế hoạch risk đã đặt trước; chỉ xét tăng size sau khi cỡ mẫu đủ lớn xác nhận qua nhiều chu kỳ thị trường khác nhau (không chỉ 1 trend rõ).

**⑫ Bỏ qua correlation khi trade nhiều symbol cùng cửa sổ Venom.**
Dấu hiệu: vào cùng lúc Venom Long trên NQ1 và ES vì cả hai đều "quét pre-market low" trong cùng cửa sổ 09:30-10:30 — tưởng là 2 cơ hội độc lập nhưng thực chất là 1 bet lớn hơn (hai chỉ số index Mỹ tương quan rất cao). Cơ chế: sweep NY cash-open thường xảy ra đồng thời trên các index Mỹ do cùng chịu tác động dòng lệnh mở phiên; nếu cả hai đi sai hướng, thua kép cùng lúc dù tưởng đã "phân tán risk". **Xử lý:** coi các symbol tương quan cao (NQ1/ES/YM, hoặc EURUSD/GBPUSD) là một rổ risk duy nhất trong cùng cửa sổ; giới hạn tổng risk của rổ đó bằng risk 1 lệnh, không cộng dồn.

> [!note] Nguyên tắc chung cho mọi edge case Venom
> Khi nghi ngờ **bất kỳ** mắt xích nào (time / pool / sweep-reclaim / displacement), hạ cấp về trạng thái **"chờ xác nhận thêm"** thay vì ép entry. Thiếu một core component = **No Trade**, bất kể FVG "trông" đẹp đến đâu.

---

## Chuyên sâu B — Kinh nghiệm live/backtest thực chiến

![[Venom-Advanced-WindowCreep-Timeline.svg|720]]

Những điều dưới đây thường chỉ "thấm" sau vài chục lần trade/backtest Venom — chúng không đổi lý thuyết, nhưng quyết định phần lớn khoảng cách giữa "biết model" và "kiếm được tiền từ model".

**1. Đánh dấu session pool TRƯỚC 09:30, không "tìm" pool trong cửa sổ.**
Nếu tới lúc cửa sổ mở mà bạn còn đang dò xem đâu là Asia/London high-low hay Venom Box high-low, bạn đã trễ — và dễ **bịa ra một pool cho khớp** với cú giá vừa xảy ra (hindsight). Đánh dấu xong trước 09:30; trong cửa sổ chỉ đọc price action quanh các mốc đã kẻ sẵn.

**2. Spread/slippage giãn quanh cash open 09:30 và tin 08:30 — tính vào R:R.**
R:R trên chart là gross; cái vào túi là **net sau spread/commission**. Quanh 09:30 và các mốc tin, spread giãn có thể biến stop "an toàn" thành bị wick quét và biến "R:R 3" thành R thực thấp hơn. Với **XAUUSD nới stop + giảm size** thay vì siết stop cho R:R đẹp; ghi lại spread thực để backtest biết tần suất.

**3. Session pool khác nhau theo thị trường.**
**NQ1/NDX:** pool chính là high/low của **pre-market range (Venom Box 08:00–09:30)** — futures có volume xuyên đêm nên range rõ và đáng tin. **EURUSD/GBPUSD:** dùng **London high/low** (London đã dựng range đầu ngày trước khi NY vào), không có "cash open" như index. **XAUUSD:** thường lấy **Asia range** làm pool tham chiếu, đôi khi kết hợp London. Đừng áp một reference cho mọi thị trường.

**4. Hard cutoff 10:30 — ghi lại mỗi lần bị cám dỗ "chờ thêm".**
Kỷ luật giờ cắt là phần khó nhất. Mỗi lần bạn muốn nới cửa sổ, ghi nó xuống như một **điểm dữ liệu kỷ luật** (ngày nào, bối cảnh gì, kết quả nếu có vào). Sau 30–50 lần bạn sẽ thấy rõ window creep có "trả tiền" hay không — gần như luôn là không.

**5. Tần suất thực: Venom sạch không xảy ra mỗi ngày.**
Nhiều ngày sẽ **"miss Venom"** và đó là bình thường, không phải thất bại. Kỳ vọng vào lệnh mỗi ngày là nguồn gốc của window creep và của việc ép nhãn Venom lên setup không đủ chuẩn. Một tuần vài setup A+ tốt hơn mỗi ngày một setup gượng ép.

**6. Phân biệt Venom vs Silver Bullet chỉ để phân loại dữ liệu.**
Lúc vào lệnh, điều quan trọng là **pool nào bị quét + có displacement/FVG hợp lệ không**, không phải tên gọi. Sau lệnh, ghi `time_window` (và loại pool) để backtest phân loại. Đừng tranh cãi "đây là Venom hay Silver Bullet" trong lúc thị trường đang chạy — nó lấy đi sự tập trung vào price action.

**7. Cỡ mẫu ≥30–50 backtest trước khi tin một biến thể/market.**
Đừng tăng size/confidence cho một biến thể (một market như XAU, một loại pool, một khung giờ cụ thể) chỉ vì vài lệnh "cảm thấy đúng". Chuẩn tối thiểu: **≥30–50 mẫu** ghi đủ frontmatter → xác nhận win rate & average R dương có ý nghĩa → forward test size nhỏ → rồi mới scale. Để **dữ liệu của chính bạn** làm trọng tài.

**8. Demo vs live vs funded account — kỷ luật giờ cắt "mềm" đi khi tiền thật vào cuộc.**
Trên demo, hard cutoff 10:30 dễ tuân thủ vì không có cảm giác mất tiền thật. Chuyển sang live (đặc biệt funded/prop-firm), nhiều trader thấy mình "chờ thêm" đúng những phiên căng thẳng nhất — vì áp lực phải có kết quả làm tăng động lực window creep so với lúc backtest/demo. **Ghi nhận riêng** tỷ lệ tuân thủ cutoff trên demo vs live; nếu chênh lệch lớn, vấn đề là tâm lý, không phải model.

**9. Tâm lý sau 2–3 lệnh thua liên tiếp — dễ đổi quy tắc giữa chừng.**
Sau vài lệnh Venom thua (đúng chuẩn nhưng vẫn thua vì market luôn có tỷ lệ thua), phản ứng thường gặp là nghi ngờ toàn bộ mô hình và bắt đầu "chỉnh" tiêu chí (nới pool, hạ chuẩn displacement) ngay trong lúc đang mất bình tĩnh — đây chính là lúc dễ tạo ra biến thể chưa kiểm chứng. Với winrate giả định 55%, xác suất gặp 3 lệnh thua liên tiếp trong một chuỗi 20 lệnh là *không nhỏ* (~9% mỗi cụm 3 lệnh, và tích lũy qua 18 cụm trong 20 lệnh tăng đáng kể theo phân phối nhị thức) — 2-3 lệnh thua liên tiếp là **bình thường về thống kê**, không phải tín hiệu mô hình hỏng.

**10. Journaling `missing_step` — trường dữ liệu quan trọng nhất, hay bị bỏ qua nhất.**
Nhiều trade journal chỉ ghi win/loss + R, thiếu trường mô tả **mắt xích nào (nếu có) đã thiếu hoặc yếu** khi vào lệnh (time / pool / sweep-reclaim / displacement). Không có trường này, sau 50 lệnh bạn chỉ biết winrate tổng, không biết case nào trong 12 edge case ở Chuyên sâu A đang lặp lại nhiều nhất — mất chính công cụ để cải thiện có mục tiêu.

**11. Tần suất A+ thực tế theo dữ liệu quan sát — kỳ vọng hợp lý.**
Không có con số phổ quát, nhưng nhiều trader backtest Venom trên NQ1/ES ghi nhận tần suất setup đủ chuẩn (đủ 4 core component trong cửa sổ) rơi vào khoảng 2–4 lần/tuần, không phải mỗi ngày. XAUUSD do biến động tin tức nhiều thường có tần suất thấp hơn và tỷ lệ "gãy vì news spike" (case ②) cao hơn. Đây là **quan sát cá nhân cần tự kiểm chứng lại bằng backtest riêng**, không phải chuẩn ngành đã công bố.

**12. Điều kiện được phép tăng size — không chỉ dựa vào cỡ mẫu, còn cần đa dạng điều kiện thị trường.**
Ngoài ngưỡng ≥30–50 mẫu (đã nêu ở #7), nên yêu cầu thêm: mẫu đó trải qua **ít nhất 2 chế độ biến động khác nhau** (một giai đoạn biến động cao như quanh FOMC/NFP, một giai đoạn biến động thấp) và **ít nhất 2 xu hướng HTF khác nhau** (trend rõ + range/sideways). Một winrate đẹp chỉ đến từ một giai đoạn trend mạnh duy nhất chưa đủ để tăng size — nó có thể phản ánh đặc điểm của giai đoạn đó hơn là edge bền của model.

> [!tip] Một câu gói lại
> Venom thưởng cho **chuẩn bị trước phiên** và **kỷ luật dừng đúng giờ**: đánh dấu pool trước 09:30, cắt cứng tại 10:30, và để **cỡ mẫu backtest** (không phải cảm giác) quyết định biến thể nào đáng tin.

---

## Chuyên sâu C — Case studies mổ xẻ chuyên sâu (kịch bản minh họa)

> [!info] Đây là kịch bản minh họa có nhãn
> Bốn ca dưới đây là **ví dụ khái niệm** để dạy cách chấm điểm theo chuỗi + rule. Mọi số liệu giá/level là **hypothetical, KHÔNG phải lệnh thật** — đừng dùng làm dữ liệu backtest. Mỗi ca đại diện một *loại* bài học khác nhau.

### Case 1 — NQ1 Win (đúng chuẩn)

![[Venom-Advanced-CaseStudy-Win-NQ.svg|720]]

**Chuỗi:** HTF bias Bullish, target session high. **09:35 NY**, giá **quét pre-market low (Venom Box low)** rồi **reclaim** (đóng nến lại trong range) → **displacement tăng + MSS phá swing high** → để lại bullish FVG → giá retrace về **FVG entry quanh CE ở discount** → chạy về **session high**. Sạch từ time + pool + sweep-reclaim + displacement.

**Chẩn đoán:** đủ cả bốn core component đúng thứ tự, trong cửa sổ 09:30–10:30 (sát cash open), quét đúng **pool cấp session** (Venom Box low của NQ1), entry ở discount không chase. Đây là hình mẫu **A+ Venom**.

**Bài học cốt lõi:** khi **time + đúng pool + sweep-reclaim + displacement** cùng thẳng hàng, việc còn lại chỉ là thực thi theo plan (entry CE, stop dưới sweep, target session high). Không cần "sáng tạo" thêm.

### Case 2 — XAUUSD Loss (news spike nhầm Venom strike)

![[Venom-Advanced-CaseStudy-Loss-NewsSpike-XAU.svg|720]]

**Chuỗi (gãy):** **08:30 CPI**, XAUUSD giật xuống xuyên Asia low. Trader thấy "sweep" và vào long — **NHƯNG nến đóng luôn ở ngoài pool (no reclaim), không có displacement sạch** theo sau. Giá đảo chiều mạnh sau tin, quét stop. `missing_step: sweep (reclaim) / news`.

**Chẩn đoán:** cú giật là **news spike, không phải venom strike**. Thiếu reclaim (đóng nến lại trong range) và thiếu displacement có cấu trúc → không có bằng chứng dòng lệnh tổ chức đứng sau. XAU đặc biệt dễ tạo wick "quá tay" quanh 08:30 rồi đảo. Lẽ ra phải đứng ngoài 15–30 phút chờ tin lắng.

**Bài học cốt lõi:** **sweep không reclaim = chưa phải sweep**; nến to do tin ≠ nọc đã tiêm. Quanh 08:30 giảm size hoặc đứng ngoài, chỉ vào khi cấu trúc sweep + reclaim + displacement hiện rõ sau khi volatility lắng.

### Case 3 — Win nhưng sai quy trình (window creep)

![[Venom-Advanced-CaseStudy-WinWrong-WindowCreep.svg|720]]

**Chuỗi:** cửa sổ 09:30–10:30 trôi qua không có setup. Trader nới giờ, vào một lệnh **lúc 10:50 (ngoài cửa sổ, đã window creep)** và **tình cờ thắng**. Chuỗi price action "trông" giống Venom nhưng thời gian đã sai.

**Chẩn đoán:** kết quả thắng nhưng `first_error_step: time`. Cái nguy hiểm là **thắng sẽ CỦNG CỐ thói quen nới cửa sổ (outcome bias)** — một hành vi chưa hề được backtest validate, và về dài hạn thường thua. Ghi đúng `time_window: sau-cutoff`, đừng dán nhãn Venom.

**Bài học cốt lõi:** một lệnh **THẮNG vẫn phải sửa** nếu sai quy trình. Chấm điểm bằng chuỗi + rule ("đúng cửa sổ chưa?"), không bằng P&L từng lệnh; một "good discipline" quan trọng hơn một "lucky win".

### Case 4 — No-Trade đúng (ngoài cửa sổ, chưa sweep)

![[Venom-Advanced-CaseStudy-NoTrade-OutsideWindow.svg|720]]

**Chuỗi (đứng ngoài):** giữa **phiên chết**, xuất hiện một **FVG đẹp**. Nhưng **chưa quét bất kỳ session pool nào** và đang **ngoài cửa sổ Venom**. Trader không vào — coi như **No-Trade**.

**Chẩn đoán:** thiếu **cả hai bộ lọc bắt buộc** (time + đã quét session pool). FVG đẹp không cứu được bối cảnh sai. Đứng ngoài ở đây là **quyết định đúng**, không phải "bỏ lỡ".

**Bài học cốt lõi:** **No-Trade đúng quy trình là một "kết quả tốt"** cần được ghi nhận và khen, ngang với một lệnh thắng. Kỷ luật bỏ FVG đẹp sai bối cảnh chính là edge dài hạn của Venom.

### Case 5 — Miss vì hai trader chọn pool khác nhau (tranh chấp định nghĩa)

![[Venom-Advanced-CaseStudy-Miss-AmbiguousPool.svg|720]]

**Chuỗi:** Cùng nhìn một chart NQ1 lúc 09:35, **Trader A** dùng Asia range low làm pool tham chiếu (chưa bị chạm), **Trader B** dùng pre-market low làm pool (đã bị chạm + reclaim). Trader B vào lệnh theo "sweep" của mình và thắng nhỏ; Trader A đứng ngoài vì pool của mình chưa bị chạm.

**Chẩn đoán:** cả hai đều tuân thủ đúng *quy tắc riêng* của mình — không ai sai theo logic nội bộ, nhưng kết quả khác nhau hoàn toàn. Đây là bằng chứng trực tiếp cho việc Venom **không có một định nghĩa "pool cấp session" phổ quát, khách quan** được kiểm chứng độc lập — mỗi trader/tài liệu tự chọn quy ước riêng.

**Bài học cốt lõi:** giá trị của Venom không nằm ở việc tìm "định nghĩa đúng duy nhất" (không tồn tại), mà ở việc **cố định một quy tắc chọn pool trước khi backtest** và trung thành với nó đủ lâu để dữ liệu của chính bạn có ý nghĩa thống kê — thay vì đổi quy tắc mỗi ngày theo cảm tính.

### Case 6 — Loss kép do correlation (NQ1 + ES cùng hướng)

![[Venom-Advanced-CaseStudy-Correlation-DoubleLoss.svg|720]]

**Chuỗi:** Trader thấy Venom Strike xuất hiện gần như đồng thời trên **NQ1 và ES** (09:32 và 09:33), vào Long cả hai với risk 1R mỗi lệnh, nghĩ đây là "2 cơ hội độc lập". Cả hai đảo chiều cùng lúc và thua cùng lúc.

**Chẩn đoán:** NQ1 và ES có correlation rất cao (thường >0.85–0.9) vì cùng phản ứng với dòng lệnh mở phiên Mỹ và cùng nhóm tài sản (index Mỹ). Risk thực tế của giao dịch này gần **2R trên một bet tương quan cao**, không phải 2 lệnh 1R độc lập như trader tưởng khi tính position sizing.

**Bài học cốt lõi:** khi setup Venom xuất hiện đồng thời trên các symbol tương quan cao, hãy coi cả rổ là **một risk unit duy nhất** và giới hạn tổng risk bằng risk của 1 lệnh — không cộng dồn theo số lệnh.

### Case 7 — Win nhờ kiểm tra lại giờ quanh mốc đổi DST

![[Venom-Advanced-CaseStudy-Win-DST-Correct.svg|720]]

**Chuỗi:** Đầu tháng 11 (mốc Mỹ đổi DST), trader chủ động kiểm tra lại toàn bộ bảng quy đổi giờ NY→local (thay vì dùng bảng giờ cũ đã lưu), phát hiện lệch 1 giờ và cập nhật kịp trước phiên. Vào đúng cửa sổ Cutting Zone thật, setup đủ chuẩn sweep + displacement + FVG.

**Chẩn đoán:** đây không phải một case "kỹ thuật price action" mà là case về **quy trình phòng ngừa edge case ④/⑧**. Nhiều trader khác trong tuần đổi DST đó vào nhầm cửa sổ lệch 1 giờ do dùng bảng giờ cũ.

**Bài học cốt lõi:** một phần đáng kể của "edge" trong Venom nằm ở **kỷ luật vận hành** (đúng giờ, đúng pool) chứ không chỉ ở việc đọc price action — thói quen kiểm tra định kỳ (mỗi lần đổi DST) là một quy tắc nhỏ nhưng loại bỏ được một nguồn lỗi hoàn toàn có thể tránh.

> [!summary] Bảy ca — một thông điệp
> **Kết quả (win/loss) là nhiễu ngắn hạn; tín hiệu thật là time + đúng pool + sweep-reclaim + displacement.** Case 1 thắng vì đủ chuỗi; Case 2 thua vì nhầm news spike với sweep; Case 3 thắng mà vẫn phải sửa vì window creep; Case 4 đứng ngoài mà đúng; Case 5 cho thấy định nghĩa pool có thể mơ hồ giữa hai trader; Case 6 thua vì bỏ qua correlation; Case 7 thắng nhờ kỷ luật kiểm tra DST. Chấm điểm theo `missing_step`/`time_window`/`pool_type_used`, không theo P&L từng lệnh.

---

## Phản biện & Giới hạn của mô hình

> [!warning] Đọc trước khi tin tưởng tuyệt đối vào Venom
> Phần này tổng hợp các giới hạn nhận thức luận (epistemic) và giới hạn thống kê của mô hình Venom. Mục tiêu không phải "bác bỏ" mô hình mà **định vị đúng mức độ tin tưởng** — Venom là một quy tắc thực dụng (heuristic) để phân loại price action theo giờ + pool, không phải một quy luật thị trường đã được chứng minh nhân quả.

### 1. Tính chủ quan khi chọn "range tham chiếu" — vấn đề cốt lõi

![[Venom-Advanced-ReferenceRange-Subjectivity.svg|720]]

Toàn bộ khái niệm "Venom Strike" phụ thuộc vào việc xác định đúng **pool cấp session** (mục 3, Chuyên sâu A case ⑤ và ⑦). Nhưng bản thân "pool cấp session" **không có một định nghĩa khách quan, thống nhất trong tài liệu ICT gốc hay giữa các trader thực hành**:

- Có người dùng **Asia range high/low**, có người dùng **pre-market 07:00–09:30** (Venom Box), có người dùng **PDH/PDL** (previous day high/low), có người kết hợp cả ba theo thứ tự ưu tiên tự đặt ra.
- Với cùng một chart, cùng một thời điểm, **3 quy tắc chọn pool khác nhau có thể cho ra 3 kết luận "đã sweep" hoặc "chưa sweep" khác nhau** (xem Case 5 ở Chuyên sâu C).
- Điều này khiến Venom dễ mắc **hindsight bias**: sau khi thấy giá đã chạy đúng hướng, người dùng có xu hướng chọn/điều chỉnh mốc pool sao cho câu chuyện sweep "khớp" và đẹp hơn — một dạng data dredging quy mô nhỏ nhưng lặp lại ở mỗi lệnh.

**Hệ quả cho việc tin tưởng mô hình:** một backtest Venom "thắng cao" có thể phần lớn phản ánh việc chọn pool thuận lợi trong hồi cứu (retrospective), chứ không phải một edge sẽ lặp lại khi chọn pool *trước* khi biết kết quả (prospective). Cách giảm thiểu duy nhất là cố định quy tắc chọn pool **trước khi backtest** và không thay đổi nó giữa các mẫu — nhưng điều này chỉ giảm chủ quan lặp lại, không loại bỏ được chủ quan ban đầu khi *chọn* quy tắc.

### 2. Sự phụ thuộc timezone — điểm yếu vận hành ít được nhắc tới

![[Venom-Advanced-Timezone-DST-Risk.svg|720]]

Mọi mốc giờ của Venom (07:00/09:30/10:30/10:45 NY time) được định nghĩa theo **giờ miền Đông Mỹ (ET)**, buộc trader ở mọi timezone khác phải quy đổi hằng ngày. Ba lớp rủi ro:

- **DST không đồng bộ:** Mỹ đổi giờ (Chủ Nhật thứ 2 tháng 3, Chủ Nhật đầu tháng 11) không cùng ngày với châu Âu hay các nước khác, tạo ra 1–3 tuần mỗi năm nơi công thức quy đổi "quen dùng" bị sai 1 giờ (Chuyên sâu A case ④, ⑧, ⑩).
- **Biên giới phiên Asia/London/NY** trong mục 1 giả định giờ NY cố định, nhưng biên giới thật của các phiên do giờ giao dịch địa phương của từng thị trường quyết định — cũng bị ảnh hưởng gián tiếp bởi DST của khu vực đó.
- **Không có cơ chế tự kiểm tra:** trừ khi trader chủ động đặt nhắc nhở lịch, sai lệch DST thường chỉ được phát hiện *sau* khi đã vào nhầm cửa sổ vài lần.

**Hệ quả thực dụng:** độ chính xác của "Cutting Zone 09:30–10:30" phụ thuộc vào việc trader duy trì đúng bảng quy đổi giờ theo thời gian thực — một yêu cầu vận hành nằm ngoài logic price action của mô hình, nhưng có thể phá vỡ toàn bộ tiền đề "đúng giờ" nếu bị bỏ qua.

### 3. Giới hạn thống kê chung

- **Chưa có nghiên cứu độc lập, có kiểm soát (peer-reviewed hoặc dữ liệu công khai lớn)** xác nhận Venom có edge dương ngoài các cộng đồng ICT truyền miệng và backtest cá nhân không công bố phương pháp đầy đủ.
- Ngưỡng "≥30–50 mẫu" (Chuyên sâu B #7) là quy ước thực dụng do cộng đồng trader đề xuất, **không phải cỡ mẫu tối thiểu có ý nghĩa thống kê được tính toán chính thức** (một kiểm định nhị thức thực sự với sai số hợp lý thường cần hàng trăm mẫu để phân biệt winrate 50% và 55%).
- Mô hình được thiết kế và mô tả chủ yếu qua quan sát chủ quan (discretionary reading), khiến việc backtest tự động/khách quan khó tái lập giữa hai người khác nhau đọc cùng một chart.

> [!important] Kết luận thực dụng
> Dùng Venom như một **bộ lọc thời gian + pool** để giảm nhiễu khi đọc price action, không dùng như một "quy luật thị trường" đã kiểm chứng. Luôn ghi `pool_type_used` và giờ quy đổi vào log, và tự đánh giá lại bằng dữ liệu của chính mình theo chu kỳ (ví dụ mỗi 3 tháng) vì cả tính chủ quan trong chọn pool và rủi ro DST đều có thể trôi dần (drift) theo thời gian nếu không được kiểm tra định kỳ.


---

## Best Practices

> [!summary] Tư duy cốt lõi
> Venom thưởng cho sự **chuẩn bị trước phiên** và **kỷ luật dừng đúng lúc**, không thưởng cho việc "canh chart cả ngày chờ cơ hội". Phần lớn edge nằm ở việc đánh dấu đúng pool TRƯỚC khi cửa sổ mở, và biết khi nào phải dừng lại.

### 1. Pre-session routine — đánh dấu pool TRƯỚC khi cửa sổ Venom mở

- [ ] Trước 07:00 NY time (hoặc ngay khi có dữ liệu phiên Á/London đóng), đánh dấu sẵn trên chart:
  - **Asia high/low** (toàn bộ phiên Á).
  - **London high/low** (tính đến thời điểm hiện tại nếu London chưa đóng).
  - **PDH/PDL** (Previous Day High/Low).
  - Vùng **Venom Box** sẽ tiếp tục hình thành 07:00–09:30 — cập nhật high/low của range này liên tục cho tới 09:30.
- [ ] Xác định HTF bias (D1/H1) và premium/discount **trước** khi giá vào cửa sổ — không phân tích bias giữa lúc giá đang chạy nhanh.
- [ ] Chuẩn bị sẵn danh sách tin tức trong ngày (đặc biệt mốc 08:30 NY) — biết trước hôm nay có tin lớn hay không.
- [ ] Điền trước phần "Reference pools" và "Bias" trong Quick Reference Card (Appendix) trước 09:30.

> [!tip]
> Nếu đến giờ vào cửa sổ mà bạn còn đang "tìm" xem pool nào là Asia high/low, bạn đã trễ. Việc đánh dấu phải xong TRƯỚC khi cửa sổ mở — trong cửa sổ chỉ tập trung đọc price action.

### 2. Kỷ luật giờ cắt (hard cutoff) — tránh "window creep"

> [!warning] Window creep là gì?
> "Window creep" là hiện tượng tự nới lỏng cửa sổ thời gian — ví dụ cửa sổ chính thức là 09:30–10:30 nhưng vì chưa có setup, trader tự nhủ "chờ thêm chút nữa" đến 10:45, 11:00... Đây là cách phổ biến nhất khiến một lệnh "Silver Bullet muộn" hoặc "no-setup" bị dán nhãn nhầm là Venom.

- [ ] Đặt **giờ cắt cứng** (hard cutoff) = 10:30 NY time cho việc tìm setup Venom mới. Sau mốc này, nếu chưa vào lệnh → coi như hôm nay không có Venom, dừng tìm.
- [ ] Dùng alarm/nhắc hẹn giờ thực tế (không chỉ "nhớ trong đầu") để báo hiệu hết cửa sổ.
- [ ] Nếu đã có lệnh đang chạy trước giờ cắt, được phép tiếp tục quản lý lệnh đó — hard cutoff chỉ áp dụng cho việc **mở lệnh mới**.
- [ ] Ghi lại mỗi lần bị cám dỗ "chờ thêm" — đây là dữ liệu review kỷ luật quan trọng không kém win rate.

### 3. Giảm size hoặc đứng ngoài quanh tin tức lớn trong cửa sổ

- [ ] Nếu có tin tức có sức ảnh hưởng cao (CPI, NFP, FOMC, PCE...) rơi vào 08:30 hoặc trong cửa sổ 09:30–10:30:
  - Xem xét **giảm size xuống dưới mức risk chuẩn** (ví dụ 0.25% thay vì 0.5%) cho setup đầu tiên sau tin.
  - Hoặc **đứng ngoài hoàn toàn** trong 15–30 phút đầu sau tin, chờ biến động "giả" do tin lắng xuống rồi mới đọc lại cấu trúc.
- [ ] Không nhầm lẫn "spike do tin" với "venom strike" hợp lệ — spike do tin thường không có cấu trúc sweep + reclaim + displacement sạch, mà là biến động một chiều hỗn loạn.
- [ ] Nếu đã trót vào lệnh trước khi biết có tin, ưu tiên bảo toàn vốn (dời stop về entry khi có thể) hơn là cố gắng tối đa hóa R:R qua tin.

### 4. Amateur habits vs Professional habits

| Tình huống | Thói quen nghiệp dư (Amateur) | Thói quen chuyên nghiệp (Professional) |
|---|---|---|
| Chuẩn bị trước phiên | Mở chart lúc 09:29, vội vàng tìm pool | Đánh dấu Asia/London/PDH-PDL từ trước 07:00, cập nhật Venom Box liên tục |
| Khi chưa thấy setup | Ngồi canh chart cả cửa sổ, sợ bỏ lỡ | Có hard cutoff, chấp nhận "no Venom hôm nay" và rời chart |
| Khi cửa sổ đóng mà chưa có lệnh | Tự nới giờ, coi setup 10:45 vẫn là "Venom" | Dừng tìm, chuyển model (Silver Bullet AM) hoặc nghỉ, ghi nhận là ngày không có Venom |
| Khi có tin lớn trong cửa sổ | Vào full size ngay khi thấy nến to vì "sợ lỡ sóng" | Giảm size hoặc đứng ngoài, chờ cấu trúc rõ sau khi tin lắng |
| Khi sweep chưa rõ | Vào lệnh ngay khi giá chạm pool, chưa cần reclaim | Chờ đóng nến xác nhận reclaim + displacement rồi mới vào |
| Ghi nhận kết quả | Chỉ ghi thắng/thua | Ghi `missing_step`, `time_window` thực tế, có bị window creep hay không |
| Thái độ với thua lỗ trong cửa sổ | Trade thêm lệnh "gỡ" ngay sau đó dù đã quá giờ cắt | Dừng lại đúng hard cutoff dù đang thua, review sau, không revenge trade |

---

## 9. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy FVG đẹp
> Venom đòi hỏi ĐÚNG GIỜ + ĐÃ QUÉT SESSION POOL. Thiếu một trong hai thì không phải Venom.

### A. Context (HTF + session)
- [ ] Bias đã rõ: Bullish / Bearish.
- [ ] Reference pools (Asia/London/PD) đã đánh dấu.
- [ ] Location đúng premium/discount.
- [ ] Đang trong cửa sổ thời gian Venom.

### B. Execution (LTF)
- [ ] Đã có sweep session pool + reclaim.
- [ ] Có displacement + MSS để lại FVG.
- [ ] FVG sạch, xác định CE; lý tưởng trùng OTE/OB.
- [ ] Entry ở retrace về FVG, không chase.
- [ ] Stop ngoài sweep; target pool đối diện; R:R đạt.

### C. Quy tắc "không có lệnh"
- [ ] Ngoài cửa sổ thời gian → không trade.
- [ ] Chưa quét session pool → không trade.
- [ ] Ngược bias / sai premium-discount → không trade.
- [ ] Chỉ vào được bằng chase → không trade.
- [ ] Sát tin lớn → cân nhắc bỏ.

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bỏ qua time window | Vào giữa phiên chết | Mất phần "nọc" của mô hình | Chỉ săn trong cửa sổ NY open |
| Không quét session pool | Vào trước khi có sweep | Thiếu trigger | Chờ sweep Asia/London/PD |
| Chase displacement | Vào ngay khi thấy nến lớn | Bỏ retrace, R:R xấu | Chờ giá về FVG |
| Trade ngược bias | Long/Short ngược HTF | Xác suất thấp | Đồng hướng Daily Bias |
| Sai premium/discount | Long ở premium, Short ở discount | Entry chase | Long discount, Short premium |
| FVG không từ displacement | Gọi gap thường là FVG | Không có intent | Yêu cầu displacement phá cấu trúc |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = session pool đối diện |

---

## 11. Câu hỏi tự kiểm tra

- Mình có đang ở trong cửa sổ thời gian Venom không?
- Giá đã quét pool liquidity session nào chưa?
- Có displacement + MSS để lại FVG theo bias không?
- FVG có sạch, đúng premium/discount không?
- Entry là retrace về FVG hay đang chase?
- Stop (ngoài sweep) và target (pool đối diện) ở đâu, R:R bao nhiêu?
- Nếu không trade, lý do "No Trade" là time, sweep, hay bias?

---

## 12. Flashcards / Active Recall

### Q1
**Hỏi:** Ba thành phần cốt lõi của Venom Model là gì?
**Đáp:** Time (cửa sổ kill zone, đặc biệt NY open) + Liquidity sweep của session trước + Displacement (để lại FVG).

### Q2
**Hỏi:** Venom khác Silver Bullet / ICT 2022 ở điểm nào?
**Đáp:** Cùng lõi sweep→MSS→FVG, nhưng Venom neo chặt vào time window NY open và dùng liquidity của session trước (Asia/London/PD) làm reference.

### Q3
**Hỏi:** "Venom strike" nghĩa là gì?
**Đáp:** Cú quét pool liquidity session (ví dụ London low/high) trong cửa sổ thời gian — bước trigger trước displacement.

### Q4
**Hỏi:** Điều gì làm một setup KHÔNG phải Venom dù FVG đẹp?
**Đáp:** Nếu nằm ngoài cửa sổ thời gian hoặc chưa quét session pool → không phải Venom.

### Q5
**Hỏi:** Entry và stop của Venom Long đặt ở đâu?
**Đáp:** Entry tại FVG (quanh CE) ở discount; stop dưới điểm sweep / dưới đầu kia FVG.

---

## 13. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault có folder riêng như `Trades`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: Venom # Venom | ICT-2022 | OSOK | MMBM | MMSM
bias: bullish # bullish | bearish
time_window: NY-open # cửa sổ thời gian
session_pool_swept: London-low # Asia/London/PDH/PDL
displacement_mss: true
fvg_entry: true
entry_location: Discount
target: session-high # session high/low, PDH/PDL
rr_planned: 3.0
missing_step: none # none | time | sweep | displacement | retrace
```

> [!tip]
> Với các lệnh Venom thua, ghi `missing_step` — thường lỗi rơi vào `time` (ngoài cửa sổ) hoặc `sweep` (chưa quét session pool).

---

## 14. Lesson Learned

### Bài học chính
- Venom là entry model **time-based**: đúng cửa sổ NY open + quét đúng session pool.
- Lõi vẫn là chuỗi **sweep → displacement/MSS → FVG → entry → target**.
- **Time và liquidity session** là hai bộ lọc bắt buộc, không bỏ.
- Entry ở **retrace về FVG**, không chase; stop ngoài sweep.
- Mạnh nhất khi đồng hướng HTF bias, có confluence OTE/OB.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ săn Venom trong cửa sổ thời gian (NY open/kill zone).
- [ ] Tôi chờ giá quét session pool trước khi vào.
- [ ] Tôi vào ở retrace về FVG, không chase.
- [ ] Tôi đặt stop ngoài điểm sweep.
- [ ] Khi thua, tôi ghi `missing_step` để biết lỗi time hay sweep.

### Câu nhắc nhở khi trade
> **"Đúng giờ, tiêm nọc, rồi mới bắn. Ngoài cửa sổ thì không phải Venom."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Nắm time + sweep + displacement chưa? |
| Nhận diện trên chart |  | Xác định đúng cửa sổ + session pool? |
| Biết khi nào bỏ qua |  | Dám bỏ FVG đẹp ngoài cửa sổ? |
| Kết hợp với context HTF |  | Ghép bias + premium/discount + time? |
| Áp dụng vào trade thực tế |  | Entry có thật sự ở retrace FVG không? |
| Review sau trade |  | Có gắn `missing_step` và review dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup tag `[[Venom Model]]`.
- [ ] Review theo `missing_step` (time vs sweep).
- [ ] Thống kê win rate theo `time_window` và `session_pool_swept`.
- [ ] Cập nhật rule khi đủ mẫu.
