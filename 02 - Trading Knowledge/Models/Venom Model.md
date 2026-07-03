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
timeframes:
  - D1
  - H1
  - M15
  - M5
  - M1
markets:
  - NDX
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
models:
  - ICT 2022
  - Silver Bullet
  - OTE
  - AMD
importance: 4
confidence: 2
last_reviewed: 2026-06-24
created: 2026-06-24
updated: 2026-07-03
related_concepts:
  - "[[18 - Kill Zones]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
prerequisites:
  - "[[18 - Kill Zones]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
common_mistakes:
  - "[[Mistake - Skip Liquidity Sweep]]"
  - "[[Mistake - Chase Displacement]]"
  - "[[Mistake - Overtrading]]"
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
Venom Model là **mô hình entry theo thời gian (time-based)** trong hệ ICT, tập trung vào việc khai thác **liquidity của các phiên trước** (Asia, London) hoặc đỉnh/đáy session ngay trong một **cửa sổ kill zone**, đặc biệt quanh **New York open**. Khi giá "tiêm nọc" — tức quét pool liquidity của session — và sau đó **displacement** theo bias để lại FVG, đó là tín hiệu vào lệnh. Về cơ chế, Venom dùng đúng chuỗi [[ICT 2022 Model]] nhưng đặt nó trong một khung thời gian và một bộ liquidity reference cụ thể của phiên.

**Chuỗi điển hình của Venom:**
1. **Bias / khung tham chiếu:** xác định hướng (HTF bias) và các pool liquidity của phiên trước (Asia high/low, London high/low, PDH/PDL).
2. **Time window (cửa sổ Venom):** chỉ săn trong kill zone — phổ biến là quanh NY open / NY AM (xem [[18 - Kill Zones]]).
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

![[Venom-Session-Timeline-Diagram.png]]
*Ghi chú minh họa: Vẽ một timeline ngang thể hiện 3 phiên Asia (18:00–03:00 NY time), London (03:00–09:30 NY time), New York (09:30–16:00 NY time). Đánh dấu vùng 07:00–09:30 là "Venom Box hình thành", tô đậm/highlight khung 09:30–10:30 là "Venom Cutting Zone", và đánh dấu nhạt 10:30–10:45 là "Fading Window". Đây là sơ đồ khái niệm minh họa cửa sổ thời gian — không phải dữ liệu giá thật, chỉ dùng để định vị trực quan các khung giờ.*

---

## 2. Bối cảnh sử dụng

### Các bước & khái niệm tương ứng

| Bước | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| 1 | Bias + reference | [[12 - Daily Bias]], [[19 - Liquidity]] | Hướng gì? Pool session nào? |
| 2 | Time window | [[18 - Kill Zones]] | Đang trong cửa sổ Venom (NY open) chưa? |
| 3 | Liquidity sweep | [[20 - Liquidity Sweep]] | Đã quét Asia/London/PD pool chưa? |
| 4 | Displacement + MSS | [[Displacement]], [[21 - Market Structure Shift]] | Có phá cấu trúc + FVG không? |
| 5 | FVG entry | [[Fair Value Gap]], [[Optimal Trade Entry]] | FVG/CE ở đâu, đúng PD không? |
| 6 | Target | [[19 - Liquidity]] | Pool đối diện ở đâu? |

### Biến thể thường gặp
- **+ Silver Bullet:** Venom rất gần Silver Bullet — chạy chuỗi trong cửa sổ 1 giờ của kill zone ([[18 - Kill Zones]]).
- **+ ICT 2022 Model:** lõi entry chính là chuỗi [[ICT 2022 Model]] đặt trong time window.
- **+ OTE:** tinh chỉnh entry bằng OTE 62–79% trùng FVG ([[Optimal Trade Entry]]).
- **+ AMD:** sweep đầu NY ~ pha manipulation; displacement ~ distribution ([[02 - AMD]]).

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

![[Venom-Strike-Recognition-Chart.png]]
*Ghi chú minh họa: Vẽ một biểu đồ nến minh họa (khung M5 hoặc M15) với: (1) một đường ngang đánh dấu "Pre-market/Session Low" (pool tham chiếu), (2) một cây nến có wick dài thò xuống dưới đường đó rồi đóng cửa trở lại phía trên (khoanh tròn/chú thích "Venom Strike – sweep + reclaim"), (3) chuỗi nến displacement tăng mạnh ngay sau đó phá vỡ swing high gần nhất (chú thích "Displacement + MSS"), (4) vùng Fair Value Gap được tô màu giữa các nến displacement (chú thích "FVG – POI chờ retrace"). Đây là biểu đồ ví dụ khái niệm tự vẽ hoặc dùng chart giả lập — không dùng dữ liệu giá thật của một lệnh cụ thể.*

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Venom
> 1. **Đang trong cửa sổ Venom (NY open/kill zone) chưa?**
> 2. **Giá đã quét pool liquidity session nào chưa?**
> 3. **Có displacement + MSS để lại FVG theo bias không?**
> 4. **Entry/stop/target ở đâu, R:R bao nhiêu?**

### D1 / H1 — Bias & Reference
- **Bias:** Bullish / Bearish (xem [[12 - Daily Bias]]).
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

![[Venom-vs-SilverBullet-Window-Comparison.png]]
*Ghi chú minh họa: Vẽ sơ đồ so sánh 2 cột song song trên cùng một trục thời gian (07:00–11:00 NY time). Cột trái "Venom": highlight khung 09:30–10:30, chú thích pool bị quét là "Pre-market/Session High-Low", mũi tên chỉ vào một sweep + displacement + FVG mẫu. Cột phải "Silver Bullet AM": highlight khung 10:00–11:00, chú thích pool bị quét là "Swing high/low gần nhất (bất kỳ)", mũi tên chỉ vào một FVG mẫu không gắn với pool session. Vùng chồng lấn 10:00–10:30 tô màu riêng với chú thích "Vùng dễ nhầm lẫn — phân biệt bằng loại pool bị quét, không phải bằng giờ". Đây là sơ đồ khái niệm để đối chiếu hai model, không phải chart giao dịch thật.*

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
![[Venom-Example-Correct-NYOpen-Sweep.png]]

**Mô tả:**
HTF bias Bullish, target là session high / PDH. **(1)** Vào **NY open kill zone**, giá **quét London low** (liquidity session) rồi reclaim. **(2)** **Displacement tăng + MSS** phá swing high, để lại bullish FVG. **(3)** Giá retrace về FVG (quanh CE) → **entry**, stop dưới điểm sweep. **(4)** Giá chạy về **session high / PDH target**.

**Vì sao đây là ví dụ tốt:**
- Đúng cửa sổ thời gian (NY open) + quét đúng session pool.
- Đủ chuỗi sweep → displacement → FVG retrace.
- Entry ở discount, không chase; target pool rõ.

### Ví dụ sai / dễ nhầm — Vào ngoài cửa sổ, chưa quét session pool
![[Venom-Example-Wrong-OutsideWindow.png]]

**Mô tả lỗi:**
Trader thấy một FVG đẹp **giữa phiên chết** (ngoài cửa sổ Venom) và vào ngay, dù **chưa có cú quét liquidity session** nào. Thiếu cả "đúng giờ" lẫn "tiêm nọc", giá đi loanh quanh rồi quét stop.

**Bài học:**
- Ngoài cửa sổ thời gian → không phải Venom, dù FVG có đẹp.
- Phải có sweep session pool trước displacement.
- Time + liquidity session là hai bộ lọc không thể bỏ.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[20 - Liquidity Sweep]]
- [[Displacement]]
- [[21 - Market Structure Shift]]
- [[Fair Value Gap]]
- [[Optimal Trade Entry]]
- [[27 - Premium Discount]]
- [[18 - Kill Zones]]
- [[02 - AMD]]
- [[ICT 2022 Model]]
- [[One Shot One Kill Trading Model]]

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
> Venom, Silver Bullet và [[ICT 2022 Model]] dùng chung lõi (sweep → MSS → FVG). Điểm khác của Venom là **neo vào time window NY open + liquidity của session trước**. Kết hợp tốt với [[One Shot One Kill Trading Model]] khi muốn chọn một phát chất lượng trong ngày.

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

---

## Appendix — Venom Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Bias:** Bullish / Bearish
> **Reference pools:** Asia ____ / London ____ / PDH-PDL ____
> **Time window:** NY open / NY AM kill zone
> **Location:** Premium / Discount
> **(1) Venom strike (sweep session):** pool ____ @ ____ — reclaim? Yes/No
> **(2) Displacement + MSS:** phá ____ → FVG? Yes/No
> **(3) FVG (POI):** [low]–[high], CE ____ ; OTE/OB? ____
> **(4) Entry:** ____ ; Stop (ngoài sweep): ____
> **(5) Target:** session pool đối diện / PD ____
> **Đúng cửa sổ + đã quét session pool?** Yes / No
> **R:R dự kiến:**
> **No-trade condition:**
