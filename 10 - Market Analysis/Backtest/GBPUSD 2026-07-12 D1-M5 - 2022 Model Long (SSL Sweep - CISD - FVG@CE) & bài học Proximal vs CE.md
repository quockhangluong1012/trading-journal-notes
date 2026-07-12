---
type: market-analysis
status: backtest
date: 2026-07-12
trade_date: 2024-12-04
symbol: GBPUSD
timeframe: D1 / H1 / M15 / M5
session: New York (replay - FXReplay, dữ liệu 04/12/2024)
htf_bias: bullish (xác nhận sau khi H1 retrace POI + M5 CISD nuốt nhịp quét OB)
setup: 2022 Model Long - SSL sweep -> CISD (M5) -> FVG@CE OB H1 -> entry discount
in_trade: true
result: Win
entry_price: 1.26615
stop_loss: 1.26494
take_profit: 1.27027
r_multiple: 3.4
grade: A
draw_on_liquidity: "BSL: H1 Dealing Range High 1.27497 · D1 FVG 1.27688-1.28586 | SSL đã quét: old low 1.24852"
key_poi: OB H1 1.26515-1.26642 (CE ~1.26579), FVG M5 trùng CE
invalidation: đóng nến M5/H1 dưới OB H1 (dưới 1.26494)
topic: quy trình top-down 2022 Model Long hoàn chỉnh + bài học Proximal vs CE (precision vs participation, expectancy)
backtest_note: "[[01 - Win - GBPUSD- 2024-12-04- Long]]"
tags:
  - analysis
  - methodology
  - GBPUSD
  - ict-2022
  - top-down
  - change-in-state-of-delivery
  - fair-value-gap
  - consequent-encroachment
  - draw-on-liquidity
  - sell-side-liquidity
  - premium-discount
  - expectancy
---

# GBPUSD D1 → M5 — 2022 Model Long (SSL Sweep → CISD → FVG@CE) & bài học Proximal vs CE — 2026-07-12

> [!info] Trạng thái
> **CASE STUDY — lệnh thật (WIN, +3.4R, grade A).** Note này tổng hợp trọn một phiên phân tích top-down [[01 - ICT 2022 Model]] Long trên GBPUSD (replay 04/12/2024): từ bias D1 còn tranh cãi → H1 xác định range + POI → M5 chờ **[[41 - Change in State of Delivery|CISD]]** để confirm và vào lệnh. Giá trị lớn nhất nằm ở **mục 5 — bài học Proximal vs CE**, một insight cậu tự rút ra từ backtest và được chính lệnh này chứng minh.
> Số liệu lệnh: xem [[01 - Win - GBPUSD- 2024-12-04- Long]]. Chart replay dữ liệu 04/12/2024; `date` = ngày capture (VN, UTC+7).

## 0. Tóm tắt lệnh

| Field | Value |
|---|---|
| Symbol / Position | GBPUSD / **Long** |
| Trade date (replay) | 2024-12-04 · Session **New York** |
| Setup | ICT 2022 Model (LTF entry M5) |
| Entry / SL / TP | **1.26615 / 1.26494 / 1.27027** |
| R multiple | **+3.4R** · Grade **A** · Followed plan: Yes |
| POI | OB H1 **1.26515–1.26642** (CE ~**1.26579**) |
| Kết quả | **Win — Hit TP** |

---

## 1. Bias D1 — "bounce" chưa phải "bullish", chờ confirm

![[Pasted image 20260712160925.png]]

Order flow gần nhất trên D1 là một **bearish displacement** từ đỉnh ~1.343 xuống. Vậy nên tại thời điểm mở phân tích, bias Bullish **chưa được xác nhận** — đây mới chỉ là một nhịp **[[27 - Premium Discount|retracement]]**, không phải reversal. Điểm mấu chốt để không tự lừa mình:

> [!warning] Bài học 1 — một cú bounce từ đáy KHÔNG tự động là bias Bullish
> Leg displacement gần nhất là **giảm** → dòng lệnh D1 chủ đạo vẫn bearish cho tới khi bị phủ nhận. Cái ủng hộ Long chỉ là: (a) giá đang trong **[[27 - Premium Discount|discount]]** của leg giảm (EQ ~1.295), và (b) giá vừa quét **old lows ([[30 - Sell-side Liquidity|SSL]])** rồi reclaim. **Bias chỉ được confirm sau** khi H1 retrace về POI và **M5 tạo [[41 - Change in State of Delivery|CISD]]** nuốt nhịp quét OB — không confirm trước bằng cảm tính.

**[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]]:**
- **BSL (mục tiêu Long):** H1 Dealing Range High **1.27497**; xa hơn là **D1 FVG 1.27688–1.28586** chưa mitigate.
- **SSL:** đã quét, SSL hiện tại là old low vừa tạo **1.24852**; sâu hơn có FVG 1.23954–1.24187.

## 2. H1 — Range, POI & vị trí Discount

![[Pasted image 20260712161058.png]]

Cấu trúc H1 chuyển **HH/HL** (order flow bullish nội bộ), nhưng hai mức D1 lại là **biên của một range H1**: **High 1.27497 ↔ Low 1.26164**. Giá đang quanh vùng **EQ (50%)** — tức "no man's land", chưa phải nơi vào lệnh.

- **POI chính:** **[[25 - OB - Order Block|Order Block]] H1 1.26515–1.26642**, hình thành từ nhịp displacement lên đỉnh cũ lúc 9:00 ngày 04/12. OB nằm ở **nửa discount** của range → hợp lệ cho Long.
- **Liquidity cần chờ sweep:** swing low dưới OB + chính vùng OB.

> [!summary] Nguyên tắc khung thời gian
> **HTF (D1/H1) cho "Ở ĐÂU"** (bias + vùng POI + DOL). **LTF (M5) cho "KHI NÀO"** (trigger vào lệnh). Giá retrace về OB lúc 16:00 → xuống M5 quan sát, **không** vào mù ở giữa range. Xem [[32 - Top-down Analysis (Multiple Timeframes)]].

## 3. M5 — CISD xác nhận & điểm vào lệnh

![[Pasted image 20260712162407.png]]

Đây là phần đắt giá nhất về mặt confirmation. Chuỗi sự kiện:

1. Giá retrace về OB → một **nến bearish displacement mạnh đóng cửa XUYÊN QUA OB** (thủng xuống cạnh dưới + râu ra ngoài). *Cách giá tới POI kiểu bạo lực này là **cờ vàng**, không phải tín hiệu mua ngay.*
2. Ngay sau đó, chuỗi **nến bullish liên tiếp** (thân lớn) **nuốt trọn** cây bearish displacement đó → hình thành **[[41 - Change in State of Delivery|CISD]]** (16:05–16:50). Đây là confirmation có **mốc tham chiếu khách quan** (đóng cửa vượt open cây displacement), mạnh và rõ hơn một "MSS mơ hồ".
3. Cú CISD để lại **2 [[13 - FVG  - Fair Value Gap|FVG]]**: **FVG#1** nằm trên OB (16:40); **FVG#2** nằm **ngay [[10 - Consequent Encroachment (Mean Threshold)|CE]] của OB** (16:30) → confluence hạng A.

> [!summary] Chuỗi trigger 2022 Model đã hội đủ
> **Sweep** (old lows + quét 50% OB) → **[[35 - Aggressive Displacement Entry|Displacement]]** (tạo FVG) → **CISD** (thay cho MSS, chặt hơn) → **retrace FVG** → **Entry**. POI = OB H1, FVG trùng OB.
> **Entry 1.26615 · SL 1.26494** (dưới OB / điểm invalidation) **· TP 1.27027** (opposing liquidity) → **+3.4R**.

> [!warning] Cây bearish thủng OB = local SSL sweep, KHÔNG phải quét 1.26164
> Đáy nhịp thọc ~1.263 vẫn **trên** SSL lớn D1 **1.26164** → đây là lệnh **nhịp intraday thuận cú đảo LTF**, không phải cược đảo trend D1. Upside bị đóng nắp ở **1.27497** (đã reject một lần) — chốt dứt khoát, đừng gồng xa hơn khi 1.27497 chưa bị phá bằng body.

## 4. Recap chuỗi ICT 2022 Model

- [x] **Liquidity Sweep** — quét old lows + 50% OB H1 ([[20 - Liquidity Sweep]])
- [x] **Displacement** — nến mạnh tạo FVG ([[35 - Aggressive Displacement Entry]])
- [x] **CISD / MSS** — chuỗi bullish nuốt nhịp giảm quét OB ([[41 - Change in State of Delivery]])
- [x] **FVG / OB hợp lệ** trong discount ([[13 - FVG  - Fair Value Gap]], [[25 - OB - Order Block]])
- [x] **Entry** trong POI, không đua giá
- [x] **SL** dưới điểm sweep/OB · **TP** opposing liquidity, **RR ≥ 2** ([[05 - Mistake - Not enough RR]])

---

## 5. ⭐ Bài học trọng tâm — Proximal vs CE (precision vs participation)

**Quan sát từ backtest:** giá **hiếm khi retrace đúng về CE** để entry — nó hay tới **gần CE rồi quay đầu**. Chờ chạm CE hoàn hảo → **bỏ lỡ rất nhiều setup**. Chính lệnh này là bằng chứng: giá **chưa chạm FVG#2 @ CE (~1.26579)** đã đảo lên, và **entry thắng 1.26615 nằm ở NỬA TRÊN OB — phía trên CE**, tức là một **entry proximal**, không phải CE.

> [!summary] Bài học 2 — CE là TRẦN (độ sâu tối đa kỳ vọng), không phải SÀN phải chạm
> Với **[[13 - FVG  - Fair Value Gap|FVG]]** mạnh, giá chỉ cần chạm **mép proximal** là đủ để reprice. **Phản ứng TRƯỚC khi tới CE = tín hiệu array mạnh**, không phải setup lỗi. POI đúng là **cả vùng cạnh-gần ↔ CE**, không phải một limit cứng đặt tại CE. Xem [[10 - Consequent Encroachment (Mean Threshold)]].

> [!warning] Bài học 3 — chọn entry theo EXPECTANCY, không theo R:R mỗi lệnh
> Một entry CE 5R nhưng chỉ khớp 20% có thể **kém expectancy hơn** một entry proximal 3R khớp 70%.
> `Expectancy/setup = fill_rate × [(win% × avgWin) − (loss% × avgLoss)]`.
> **Một entry hoàn hảo không bao giờ được khớp thì expectancy = 0.** Đây là con số phải đo trên sample thật (setup bị miss ở CE **phải tính là 0**, nếu không là hindsight bias).

**Cách xử lý (theo thứ tự ưu tiên):**

1. **Tăng độ phân giải thay vì hạ chuẩn:** khi giá vào **mép proximal**, tụt **M1** tìm **micro-CISD / micro-FVG / sweep nhỏ** làm trigger → entry sớm hơn CE (fill cao) nhưng **vẫn có confirmation**, SL vẫn dưới sweep low nên R:R gần như không xấu đi. (Xem [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]].)
2. **Định nghĩa lại entry level theo nơi thắng thật** — nếu data cho thấy lệnh thắng cụm ở proximal/FVG nông, dời reference lên đó.
3. **Điều kiện hóa theo độ mạnh displacement:** displacement mạnh → entry proximal (retrace nông); yếu/range → chờ CE hoặc distal.

> [!warning] Caveat — vào sớm hơn KHÔNG mặc định tốt hơn
> Entry proximal có thể (a) SL rộng hơn tương đối, (b) entry non → dễ bị lấp sâu quét stop, (c) nhặt phải setup kém → **win rate tụt**. Nhiều fill mà win rate giảm mạnh thì expectancy vẫn tệ. → **Phải đo bằng số, đừng đổi rule bằng cảm giác** ([[04 - Mistake - FOMO Entry]]).

## 6. Concept đã áp dụng trong lệnh này

- [[01 - ICT 2022 Model]] · [[41 - Change in State of Delivery]] · [[13 - FVG  - Fair Value Gap]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- [[25 - OB - Order Block]] · [[12 - Dealing Range]] · [[27 - Premium Discount]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- [[30 - Sell-side Liquidity]] · [[07 - Buy-side Liquidity]] · [[20 - Liquidity Sweep]] · [[35 - Aggressive Displacement Entry]]
- Nâng cao (nếu soi thêm): bearish FVG do cây thủng OB tạo ra, khi bị đóng cửa vượt lên, flip thành [[17 - Inverse Fair Value Gap - iFVG|IFVG]] đỡ giá — confluence bổ sung.

## 7. Bài học rút ra (tổng hợp)

1. **Bounce ≠ bias Bullish** — chờ CISD confirm, không confirm bias bằng cảm tính.
2. **HTF = "Ở ĐÂU", LTF = "KHI NÀO"** — POI trên H1, trigger trên M5.
3. **Cách giá tới POI quan trọng ngang cái level** — thủng OB bạo lực = cờ vàng, phải chờ CISD.
4. **CISD > MSS mơ hồ** — có mốc tham chiếu khách quan.
5. ⭐ **CE là trần, không phải sàn** — retrace nông = sức mạnh; entry proximal có kiểm soát (LTF confirm) thường thắng.
6. ⭐ **Tối ưu theo expectancy (kèm fill rate), không theo R:R mỗi lệnh.**
7. **Đây là lệnh nhịp intraday, không phải đảo trend D1** — SSL 1.26164 vẫn chưa quét; upside capped ở 1.27497.

## 8. Next steps

- Chạy bảng so sánh **Proximal vs CE** trên sample backtest: cột `fill_rate / win% / avgR / expectancy` (tính cả setup bị miss = 0) → để **số liệu chọn entry rule**, không phải cảm giác.
- Điền nốt mục **5. Lesson Learned** trong file backtest gốc [[01 - Win - GBPUSD- 2024-12-04- Long]] (root cause hiện đang trống).
- Cân nhắc nâng insight "CE là trần, entry proximal + LTF confirm" thành **rule chính thức** trong Playbook `03 - Playbooks/`.

---
*Ghi chú: phiên replay FXReplay (dữ liệu 04/12/2024); giá đọc từ chart/backtest note, có thể làm tròn. Note phương pháp + case study cho một lệnh đã vào (`in_trade: true`) — số liệu lấy từ [[01 - Win - GBPUSD- 2024-12-04- Long]].*
