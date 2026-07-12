---
type: ict-concept
concept: Mayne Structure + OTE Model
aliases:
  - Mayne Model
  - Structure + OTE
  - Trader Mayne Model
  - Mayne Swing Model
  - Structure OTE Playbook
tags:
  - trading/ict/model
  - trading/study
  - "#mayne"
  - "#ote"
  - "#market-structure"
  - "#swing"
status: developing
category: Entry Model
timeframes:
  - D1
  - H4
  - H1
  - M15
models:
  - ICT 2022
  - Mayne Structure + OTE
markets:
  - NQ1/NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 4
confidence: 2
last_reviewed: 2026-07-12
created: 2026-07-12
updated: 2026-07-12
prerequisites:
  - "[[26 - OTE - Optimal Trade Entry]]"
  - "[[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]]"
  - "[[27 - Premium Discount]]"
  - "[[20 - Liquidity Sweep]]"
common_mistakes:
  - "Vào giữa range, không đợi OTE/discount"
  - "Ngược HTF bias"
  - "Vào mù, không chờ confirmation khung nhỏ"
---

# 14 - Mayne Structure + OTE Model

> [!info] Nguồn tham khảo
> Mô hình được biết tới rộng rãi qua playbook **"Structure + OTE"** của Trader Mayne (TheTradingMayne).
> - [Structure + OTE Playbook — Trader Mayne (ChartFanatics)](https://www.chartfanatics.com/strategies/structure-ote)
> - [Structure + OTE Playbook by Trader Mayne (TradeZella)](https://www.tradezella.com/strategies/structure-ote)

> [!summary] Tóm tắt 1 câu
> **Mayne Model là một entry model *swing, thuận xu hướng* dựng trên bộ khung ICT: đọc CẤU TRÚC thị trường HTF để xác định bias & Draw on Liquidity → chờ giá HỒI về discount/premium → tinh chỉnh điểm vào bằng OTE (Fibonacci 62–79%) trùng với một POI (OB/FVG) → chờ SWEEP thanh khoản + XÁC NHẬN cấu trúc khung nhỏ (MSS/breaker) rồi mới vào, stop ngoài đáy/đỉnh sweep, target là opposing liquidity với RR lớn.**

> [!important] Nguyên tắc cốt lõi
> **"Structure cho hướng, OTE cho giá, Confirmation cho thời điểm."** Cả ba lớp phải đồng ý. Một OTE đẹp *ngược* cấu trúc HTF là bẫy; một cấu trúc đúng nhưng vào *giữa range* (không OTE, không discount) là RR kém. Và **không vào limit mù** — Mayne luôn chờ một xác nhận cấu trúc trên khung nhỏ tại vùng OTE (đây là phần *có tính discretionary*).

> [!tip] Bản đồ đọc note này
> Mục 1–3 = *WHAT* (định nghĩa, cơ chế, cấu phần). Mục 4–7 = *HOW* (chuỗi hình thành, bullish/bearish, OTE, entry/stop/target). Mục 8–11 = *nâng cao* (grading, cross-market, so sánh với ICT 2022 thuần, confluence). Mục 12–19 = *thực chiến & prop-firm*. Nếu mới học Mayne, đọc 1→7 trước.

---

## 1. Định nghĩa

![[Mayne-Anatomy.svg|712]]

**Khái niệm:** Mayne Model là cách Trader Mayne "đóng gói" các mảnh ICT rời rạc thành một quy trình *thuận xu hướng, ưu tiên swing*. Bốn thành phần ICT mà anh ấy dựa vào — đúng như bạn nhận ra — là:
- **Market Structure** ([[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]], [[05 - BOS - Break of Structure]], [[09 - Change of Character]]) → xác định *hướng*.
- **Liquidity** ([[19 - Liquidity]], [[20 - Liquidity Sweep]], [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]) → xác định *đích đến* (DOL) và *nhiên liệu* cho move.
- **PD Array / POI** ([[25 - OB - Order Block]], [[13 - FVG  - Fair Value Gap]], [[04 - Breaker Block]]) → *nơi* giá phản ứng.
- **OTE** ([[26 - OTE - Optimal Trade Entry]]) → *giá vào chính xác* trong POI, cho stop chặt & RR lớn.

**Nó trả lời câu hỏi nào trên chart?**
- Trong một xu hướng đang chạy, **hồi tới đâu thì vào** cho RR tốt nhất mà không "bắt dao rơi"?
- Làm sao biến một POI rộng (OB/FVG) thành **một điểm vào cụ thể** với rủi ro định nghĩa rõ?
- Khi nào cú hồi là "cơ hội tiếp diễn" thay vì "đảo chiều"?

**Vì sao đây là model "swing" của Mayne:** anh ấy đọc bias trên **D1/H4**, chờ pullback nhiều nến, và giữ lệnh hướng tới opposing liquidity ở xa — nên một setup có thể chạy vài ngày. Triết lý của Mayne là **đơn giản + ít lệnh + R bất đối xứng lớn**: thà đợi một setup A+ 1:5R còn hơn 10 lệnh 1:1 lộn xộn.

### Mayne Model KHÔNG phải là gì
- Không phải scalp intraday tần suất cao — nó ưu tiên **continuation swing** trên HTF (bản này giữ nguyên phong cách gốc của Mayne).
- Không phải "vào bất kỳ OTE nào" — OTE chỉ hợp lệ khi **thuận cấu trúc + đúng P/D + trùng POI + có xác nhận**.
- Không phải hệ thống **100% cơ học** — bước xác nhận khung nhỏ (MSS/breaker) mang tính *discretionary*; Mayne nói thẳng model cần "chart time" và phải được cá nhân hóa.
- Không phải cái cớ bỏ qua quản trị rủi ro — vẫn ≤0.5%/lệnh ([[43 - Position Sizing]]).

---

## 2. Vì sao model hoạt động — ba lớp đồng thuận

> [!important] Hiểu WHY trước khi hỏi WHAT
> Trader mới copy "vẽ fib 62–79% rồi mua" mà không hiểu vì sao — nên họ mua OTE ngược trend hoặc giữa range rồi thua. Ba lớp dưới đây là *lý do* Mayne Model có edge.

**Lớp 1 — Structure = xác suất nền (base rate).** Đứng *cùng phía* với cấu trúc HTF nghĩa là đứng cùng phía [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]]. Trong uptrend, thị trường có "nợ" thanh khoản phía trên (BSL chưa quét); giá có động cơ đi lên lấy nó. Mua trong pullback của uptrend = bạn giao dịch *theo* dòng chảy tổ chức, không chống lại.

**Lớp 2 — OTE = giá vào tối ưu (risk-defined).** Vùng [[26 - OTE - Optimal Trade Entry|OTE 62–79%]] là nơi cú hồi đã đủ sâu để (a) quét thanh khoản nội vi, (b) cho phép đặt stop *ngay dưới* đáy swing/đáy sweep — tức stop **chặt**. Vì entry sâu và target xa, **RR bung ra**. Mức **0.705 = Consequent Encroachment (CE)** ([[10 - Consequent Encroachment (Mean Threshold)]]) là "mean threshold" của nhịp đẩy — điểm cân bằng mà thuật toán hay tôn trọng.

**Lớp 3 — Confirmation = lọc thời điểm (timing/edge).** OTE chỉ là *vùng*, không phải *tín hiệu*. Chờ một [[21 - Market Structure Shift|MSS]] / [[04 - Breaker Block|breaker]] / [[09 - Change of Character|CHoCH]] trên khung nhỏ **ngay tại OTE** giúp lọc bỏ trường hợp "OTE bị xuyên thẳng" (khi thực ra HTF đang đảo). Đây là cách Mayne biến một limit mù rủi ro cao thành một entry *có phản hồi từ thị trường*.

> [!warning] Hệ quả quan trọng
> Nếu chỉ có 1–2 lớp thì đây **không phải** setup Mayne A. OTE + structure nhưng *không* confirmation = hạ cấp. Structure + confirmation nhưng vào ngoài OTE (giữa range) = RR kém. **Edge nằm ở giao của cả ba.**

Liên hệ sâu: [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] — đám đông bán đáy pullback (đặt SSL ngay dưới), chính SSL đó là nhiên liệu cho cú sweep trước khi giá bật; Mayne đứng *sau* cú sweep, cùng phía tổ chức.

---

## 3. Cấu phần bắt buộc

| Cấu phần | Khung | Vai trò | Concept liên quan |
|---|---|---|---|
| **HTF Structure + Bias** | D1 / H4 | Xác định hướng (HH-HL hay LH-LL) & DOL | [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]], [[12 - Daily Bias]] |
| **Pullback vào P/D** | H4 / H1 | Giá hồi về discount (long) / premium (short) | [[27 - Premium Discount]], [[12 - Dealing Range]] |
| **POI (PD Array)** | H1 / M15 | Vùng phản ứng: OB / FVG / breaker thuận cấu trúc | [[25 - OB - Order Block]], [[13 - FVG  - Fair Value Gap]], [[04 - Breaker Block]] |
| **OTE Fib 62–79%** | trên nhịp đẩy | Tinh chỉnh điểm vào, ưu tiên 0.705 (CE) | [[26 - OTE - Optimal Trade Entry]], [[10 - Consequent Encroachment (Mean Threshold)]] |
| **Liquidity Sweep** | M15 / M5 | Quét STL/STH tại vùng hồi = nhiên liệu | [[20 - Liquidity Sweep]], [[15 - Inducement]], [[33 - Turtle Soup]] |
| **LTF Confirmation** | M5 / M1 | MSS / breaker / CHoCH xác nhận entry | [[21 - Market Structure Shift]], [[09 - Change of Character]], [[41 - Change in State of Delivery]] |
| **Target = opposing liquidity** | HTF | BSL (long) / SSL (short), IRL trước ERL sau | [[16 - Internal & External Range Liquidity (IRL & ERL)]], [[07 - Buy-side Liquidity]], [[30 - Sell-side Liquidity]] |

> [!tip] Quy tắc "đủ 4 trước khi nghĩ tới entry"
> Trước khi zoom xuống tìm confirmation, phải có đủ: (1) bias HTF rõ, (2) giá đang ở **đúng nửa** range (discount cho long), (3) một POI thật trong vùng hồi, (4) OTE của nhịp đẩy **chồng** lên POI đó. Thiếu bất kỳ điều nào → chưa phải cơ hội.

---

## 4. Chuỗi hình thành (6 bước)

![[Mayne-Formation-Sequence.svg|712]]

1. **HTF Structure + Bias** — trên D1/H4 xác định uptrend (HH-HL) hay downtrend (LH-LL) và **DOL** (thanh khoản nào giá đang hướng về).
2. **Chờ Pullback** — kiên nhẫn để giá hồi về **discount** (long) / **premium** (short) của dealing range hiện tại.
3. **POI** — vùng hồi phải chạm một PD array thuận cấu trúc (OB/FVG/breaker) — *nơi* dự kiến phản ứng.
4. **OTE Fib** — vẽ Fibonacci trên nhịp đẩy gần nhất; vùng **62–79%** (sweet spot 0.705) phải **chồng** lên POI.
5. **Sweep + LTF Confirmation** — tại OTE, chờ giá **quét STL/STH** rồi in **MSS / breaker / CHoCH** trên khung nhỏ.
6. **Entry / Stop / Target** — vào sau xác nhận; stop **ngoài đáy/đỉnh sweep**; target = **opposing liquidity** (IRL → ERL).

> [!note] Vì sao thứ tự này bắt buộc
> Bỏ bước 1–2 = giao dịch ngược dòng hoặc mua ở premium (RR kém). Bỏ bước 4 = vào một POI rộng không có điểm cụ thể, stop xa. Bỏ bước 5 = "bắt dao rơi" khi HTF thực ra đang đảo.

---

## 5. Bullish vs Bearish

![[Mayne-Bullish-vs-Bearish.svg|712]]

**Bullish (uptrend):** cấu trúc HH-HL → giá hồi về **discount** → OTE 62–79% chồng bullish OB/FVG → **sweep SSL** (đáy nội vi) → **MSS lên** khung nhỏ → **long**. Target = **BSL** / đỉnh trước (DOL).

**Bearish (downtrend):** cấu trúc LH-LL → giá hồi lên **premium** → OTE 62–79% chồng bearish OB/FVG → **sweep BSL** (đỉnh nội vi) → **MSS xuống** khung nhỏ → **short**. Target = **SSL** / đáy trước (DOL).

> [!tip] Ưu tiên khi phân vân
> Mayne Model gốc là **continuation-first**. Nếu không chắc đang tiếp diễn hay đảo chiều, **mặc định coi là continuation** và chỉ đánh thuận DOL HTF. Reversal chỉ đánh khi cấu trúc HTF *đã* chuyển (đã có CHoCH/MSS trên chính HTF), không phải "hy vọng đảo".

---

## 6. OTE — lõi của Mayne Model

![[Mayne-OTE-Zone.svg|712]]

**Cách vẽ:**
- **Bullish:** kéo Fibonacci retracement từ **swing low → swing high** của nhịp đẩy gần nhất. Vùng vào = **0.62 → 0.79**; ưu tiên **0.705** (= CE / mean threshold).
- **Bearish:** kéo từ **swing high → swing low**. Vùng vào vẫn 62–79% (nằm ở premium).

**Vì sao 62–79% chứ không phải 50%:** ở 50% (equilibrium) giá thường chưa quét đủ thanh khoản nội vi và chưa cho stop đủ chặt. Vùng 62–79% đủ sâu để cú hồi "làm sạch" SSL/BSL nhỏ và cho phép stop *ngay ngoài* đáy/đỉnh sweep → RR tối ưu. Đây chính là ý nghĩa chữ **"Optimal"** trong OTE.

> [!important] OTE không dùng đơn lẻ
> OTE là *thấu kính tinh chỉnh*, không phải tín hiệu. Sức mạnh đến từ **confluence**: OTE + POI (OB/FVG) + đúng P/D + sweep + confirmation. Vẽ fib xong mà không có POI hay ngược bias → **bỏ**. Mayne dùng OTE để *chọn giá trong vùng đúng*, không để *tạo ra* vùng đúng.

> [!tip] Mẹo confluence 0.705
> Setup mạnh nhất khi **0.705 (CE)** trùng với **CE của FVG** trong POI hoặc trùng **mép OB**. Khi ba mức mean-threshold này hội tụ → đây là "điểm vàng" của Mayne cho limit/confirmation.

---

## 7. Vào lệnh, Stop & Target

![[Mayne-Example-Correct.svg|712]]

- **Entry:** sau khi giá vào OTE + sweep + **xác nhận cấu trúc khung nhỏ** (MSS/breaker/CHoCH). Có 2 trường phái:
  - *Confirmation entry* (đúng tinh thần Mayne): chờ MSS khung nhỏ rồi vào — an toàn hơn, bỏ lỡ vài lần.
  - *Limit tại 0.705*: đặt trước tại CE của OTE trùng POI — vào được nhiều setup hơn nhưng cần P/D + bias thật chắc.
- **Stop:** **ngoài đáy của cú sweep** (long) / **ngoài đỉnh sweep** (short) — hoặc ngoài mép xa POI. KHÔNG đặt tại pivot MSS (quá chặt, dễ bị wick quét).
- **Target:** **opposing liquidity** theo DOL HTF — [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL trước, ERL sau]]. Dời stop về BE sau khi chạm T1. Vì đây là swing, target ERL thường cho **RR 3–5R+**.
- **Timing:** với NQ/FX intraday-swing, ưu tiên vùng hình thành quanh [[18 - Kill Zones|killzone]] London/NY; với swing thuần thì timing ít quan trọng hơn cấu trúc.

> [!example] Mẫu ghi nhanh — Mayne (Bullish)
> ```text
> Bias (HTF D1/H4): Bullish (HH-HL) | DOL: BSL @ [level]
> Location: Discount (dưới EQ dealing range)
> POI: bullish OB/FVG @ [low]-[high]
> OTE: 0.62=[..] 0.705=[..] 0.79=[..] (chồng POI? có/không)
> (1) Sweep STL @ [level] (wick)
> (2) LTF confirmation: MSS/breaker @ [swing] (M5/M1)
> Entry: [giá] | Stop: ngoài đáy sweep @ [level] | RR dự kiến: [..]
> T1 = IRL [..] (dời BE) → T2 = ERL/BSL [..]
> Invalid: đóng nến HTF dưới đáy sweep / mất cấu trúc HL
> ```

> [!warning] Ba lỗi quản trị lệnh phổ biến
> 1. **Stop tại pivot MSS** (quá chặt) → bị wick quét. Đặt ngoài **toàn bộ** đáy/đỉnh sweep.
> 2. **Chốt hết tại T1** → bỏ lỡ phần lớn move swing. Chốt bậc thang IRL → ERL.
> 3. **Không dời BE sau T1** → biến swing thắng lớn thành hòa/thua khi giá hồi.

---

## 8. Xếp hạng chất lượng setup (Grading)

Không phải OTE nào cũng ngang nhau. Chấm điểm **khách quan** giúp size theo chất lượng, không theo cảm xúc.

| Hạng | Điều kiện (thang 6 confluence) | Hành động |
|---|---|---|
| **A+** | Thuận HTF bias + discount/premium đúng + POI rõ + OTE chồng POI (0.705≈CE) + sweep sạch + LTF confirmation rõ (≥5–6/6) | Full size (≤0.5%) |
| **A** | Thuận bias + đúng P/D + OTE chồng POI + có confirmation, thiếu 1 lớp phụ (4/6) | Size chuẩn |
| **B** | OTE ổn nhưng POI mỏng / ngoài killzone / confirmation yếu (2–3/6) | Half-size hoặc bỏ |
| **Bỏ qua** | Ngược bias / vào giữa range không OTE / không confirmation / chỉ vào bằng chase | Không trade |

> [!tip]
> Ghi **grade** vào frontmatter mỗi trade (mục 17). Sau 20–30 lệnh, so win-rate theo grade — nếu B thua đều, đó là bằng chứng khách quan để **bỏ hẳn B**.

---

## 9. Mayne Model theo từng thị trường

Cùng logic Structure + OTE, nhưng độ sạch của pullback và độ dài wick khác nhau giữa các thị trường bạn trade.

| Đặc tính | NQ1 / NDX (NAS100) | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Cấu trúc pullback | Sắc, hồi nhanh; OTE hình thành gọn | Mượt hơn, hồi có tính "trend leg" rõ | Wick dài, pullback "giật" |
| OTE có bị xuyên? | Đôi khi xuyên nhẹ rồi bật (dùng confirmation) | Tôn trọng OTE khá tốt | Hay xuyên sâu quá 0.79 rồi mới bật |
| Rủi ro đặc thù | Nhiều nhịp nhỏ → dễ vẽ nhầm "nhịp đẩy" cho fib | Spread ăn vào entry OTE hẹp | Wick dài dễ quét stop dù hướng đúng |
| Điều chỉnh thực dụng | Vẽ fib trên nhịp đẩy **có displacement rõ**; chờ MSS M5/M1 | Tính spread vào 0.705; đòi POI đủ rộng | Nới stop ngoài wick sweep; **giảm size**; chấp nhận entry tới 0.79 |
| Timing hiệu quả | NY AM, quanh 09:30 mở NYSE | London Open, NY AM | London, NY AM, tránh sát giờ tin |

> [!tip]
> Quy tắc gọn: **NQ → fib trên nhịp displacement rõ + chờ MSS khung nhỏ; FX → tính spread vào 0.705; Gold → nới stop & giảm size vì wick.**

---

## 10. Mayne Model vs ICT 2022 thuần — khác nhau ở đâu?

> [!important] Vì sao cần phân biệt (intellectual honesty)
> Bạn nhận xét đúng: Mayne dùng đúng bộ khái niệm của [[01 - ICT 2022 Model|ICT 2022 Model]]. Nhưng "khẩu vị" khác nhau. Hiểu khác biệt giúp bạn **không trộn lẫn hai bộ rule** và để **dữ liệu backtest của chính bạn** phân xử cái nào hợp với bạn.

| Khía cạnh | ICT 2022 (bản intraday của bạn) | Mayne Structure + OTE |
|---|---|---|
| Khung & phong cách | Intraday LTF (H1→M5→M1), killzone-centric | **Swing** (D1/H4 bias), ít lệ thuộc killzone |
| Điểm vào chính | FVG/OB sau MSS (không bắt buộc fib) | **OTE 62–79%** là thấu kính vào **trung tâm** |
| Bối cảnh ưu tiên | Sweep → displacement → MSS → FVG entry | **Structure/trend continuation** trước tiên |
| Xác nhận | MSS khung entry | MSS/breaker khung nhỏ (nhấn mạnh discretion) |
| Nhịp độ | Nhiều setup/ngày | **Ít lệnh, R lớn**, giữ swing |
| Tính cơ học | Cơ học hơn | **Discretionary hơn** (Mayne nói rõ) |

**Điểm giao (cả hai cùng dùng):** [[20 - Liquidity Sweep|sweep]], displacement, [[21 - Market Structure Shift|MSS]], [[27 - Premium Discount|premium/discount]], [[25 - OB - Order Block|OB]]/[[13 - FVG  - Fair Value Gap|FVG]], [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|DOL]].

> [!warning] Đừng trộn rule của hai game
> Nếu backtest, hãy **tag rõ** `model: Mayne` vs `model: ICT-2022` để so expectancy tách bạch. Một thói quen tối ưu cho intraday 2022 (vào nhiều, cắt nhanh) có thể phá vỡ tính swing của Mayne (cần kiên nhẫn giữ lệnh tới ERL).

---

## 11. Xếp chồng confluence (Confluence Stack)

Structure + OTE là *lõi*; các lớp dưới là *chất xúc tác* nâng grade:

- **Sweep + Turtle Soup** ([[33 - Turtle Soup]], [[15 - Inducement]]): cú hồi quét đúng một STL/STH "mồi" trước khi bật = xác nhận nhiên liệu.
- **SMT Divergence** ([[42 - SMT Divergence]]): NQ vs ES, EU vs GU phân kỳ tại điểm sweep của OTE = xác nhận mạnh.
- **CISD / Displacement chất lượng** ([[41 - Change in State of Delivery]]): nến xác nhận thân lớn tại OTE → confirmation "sạch".
- **Killzone / Macro** ([[18 - Kill Zones]], [[40 - Macro Times]]): với NQ/FX, OTE hình thành trong killzone đáng tin hơn.
- **NWOG/NDOG lân cận** ([[24 - New Week Opening Gap]], [[23 - New Day Opening Gap]]): OTE gần gap mở cửa thường được tôn trọng hơn.
- **Unicorn overlap** ([[07 - Unicorn Model]]): nếu OTE 0.705 trùng vùng **breaker + FVG chồng lấn** → đây là biến thể A+ (Mayne × Unicorn).

> [!note] Nguyên tắc confluence
> Confluence để **nâng grade & size**, không để "biện minh" cho setup thiếu lõi. Không bao giờ: "ngược bias nhưng có SMT nên vẫn vào".

---

## 12. Ví dụ chart

### Ví dụ đúng
![[Mayne-Example-Correct.svg|712]]

**Mô tả:** thuận HTF bias (uptrend), giá hồi về discount, OTE 62–79% chồng OB, quét STL rồi in MSS khung nhỏ → long; stop dưới đáy sweep; target BSL. Stop chặt + target xa = RR lớn.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lệnh thật: đánh dấu (1) cấu trúc HTF + DOL, (2) nhịp đẩy dùng vẽ fib, (3) OTE 62–79% + POI, (4) điểm sweep + MSS khung nhỏ, (5) entry/stop/T1/T2. Ghi giờ ET + grade.*

### Ví dụ sai / dễ nhầm
![[Mayne-Example-Wrong.svg|712]]

**Ba lỗi:** (a) vào giữa range/premium không đợi OTE-discount → RR kém; (b) OTE đẹp nhưng **ngược HTF bias** → bẫy; (c) vào limit mù, không chờ MSS/breaker khung nhỏ → "bắt dao rơi".

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lần bạn (hoặc người khác) gọi nhầm là Mayne setup: đánh dấu vì sao thiếu lớp (structure / OTE / confirmation).*

---

## 13. Thực hành tốt nhất (Best Practices)

> [!summary]
> Đây là các thói quen chuẩn prop-firm — thứ phân biệt trader đọc đúng Mayne Model nhất quán với trader chỉ "vẽ fib rồi mua". Mục tiêu: thuận HTF, vào đúng OTE-discount, luôn có confirmation, bảo toàn vốn qua vòng thử thách.

> [!tip] Quy tắc Mayne (5 điều cốt lõi)
> 1. **Structure trước** — chỉ đánh thuận HTF bias & DOL.
> 2. **Discount/Premium đúng** — long ở discount, short ở premium; không mua giữa/trên range.
> 3. **OTE chồng POI** — 62–79% (ưu tiên 0.705) phải trùng OB/FVG thật.
> 4. **Chờ confirmation** — sweep + MSS/breaker khung nhỏ; không vào mù.
> 5. **Stop ngoài sweep, target xa** — bảo toàn RR bất đối xứng; ít lệnh, chất lượng.

### Quy trình pre-session / pre-swing
1. **D1/H4:** xác định bias (HH-HL hay LH-LL) + DOL + đánh dấu POI HTF nơi pullback có thể chạm.
2. Xác định **dealing range** hiện tại + đường EQ; chỉ săn long ở discount, short ở premium.
3. Đánh dấu STL/STH nội vi có thể bị sweep trước khi bật.
4. Viết sẵn kịch bản: "*Nếu* giá hồi về [POI] trong OTE và sweep [STL], tôi chờ MSS M5, vào ~[0.705], stop [..], target [ERL]."
5. Đặt sẵn ngưỡng **no-trade**: ngược bias / vào giữa range / không confirmation → không đánh.

### Kỷ luật `missing_step` — biến review thành nghi thức tuần
- Với mỗi lệnh Mayne thua/BE, bắt buộc điền `missing_step`: `structure` (ngược bias), `location` (sai P/D), `ote` (vào ngoài 62–79%), `poi` (không có POI thật), `confirmation` (vào mù), `stop` (đặt sai), `timing`.
- Cuối tuần ([[07 - Reviews]] / weekly summary): thống kê tần suất. Giá trị >40% lệnh thua = **ưu tiên sửa số 1** tuần sau, gắn `[[Mistake - ...]]`.

### Amateur vs Professional

| Khía cạnh | Amateur | Professional (chuẩn prop-firm) |
|---|---|---|
| Vẽ fib | Trên bất kỳ nhịp nào, kể cả ngược trend | Chỉ trên nhịp displacement thuận HTF |
| Vị trí vào | Giữa range / premium khi long | Chỉ discount cho long, premium cho short |
| Sau khi giá tới OTE | Market order ngay | Chờ sweep + MSS/breaker khung nhỏ |
| Chọn size | Cảm xúc / "chắc kèo" | Theo grade A+/A/B đã chấm |
| Không có setup | Ép vẽ một OTE để "có việc" | Chấp nhận ngày/tuần không trade |
| Giữ lệnh | Chốt non tại T1 | Chốt bậc thang IRL→ERL, dời BE |
| Tăng size | Sau vài lệnh thắng | Sau ≥30 mẫu backtest xác nhận |

> [!tip]
> Tóm Best Practices một câu: **"Thuận structure, mua discount / bán premium, đợi OTE chồng POI + confirmation — không vẽ fib rồi vào mù."**

---

## 14. Checklist trước khi vào lệnh

- [ ] HTF bias rõ (HH-HL / LH-LL) + đúng DOL
- [ ] Giá đang ở **discount** (long) / **premium** (short) của dealing range
- [ ] Có **POI** thật (OB/FVG/breaker) thuận cấu trúc trong vùng hồi
- [ ] **OTE 62–79%** của nhịp đẩy **chồng** lên POI (ưu tiên 0.705 ≈ CE)
- [ ] Đã có **sweep** STL/STH tại vùng OTE
- [ ] Có **confirmation** khung nhỏ (MSS / breaker / CHoCH)
- [ ] Đã chấm **grade** (A+/A/B) theo mục 8
- [ ] Stop **ngoài đáy/đỉnh sweep** (không tại pivot MSS)
- [ ] T1 = IRL, T2 = ERL/opposing liquidity; RR đạt kế hoạch (ưu tiên ≥3R)
- [ ] (Ưu tiên) killzone/macro + SMT + CISD
- [ ] Không ngược bias, không vào giữa range, không vào mù

---

## 15. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Ngược HTF bias | OTE đẹp nhưng ngược trend | Đứng ngược DOL → base rate thấp | Structure trước; chỉ thuận bias |
| Vào giữa range | Long ở premium / short ở discount | Stop xa, RR kém, hồi sâu quét | Chỉ long ở discount, short ở premium |
| Vẽ fib sai nhịp | Fib trên nhịp hồi thay vì nhịp đẩy | OTE lệch, entry vô nghĩa | Fib trên nhịp **displacement** thuận HTF |
| Vào mù không confirmation | Market/limit ngay khi chạm OTE | "Bắt dao rơi" khi HTF đảo | Chờ sweep + MSS/breaker khung nhỏ |
| Stop tại pivot MSS | Stop quá chặt | Bị wick sweep quét vô lý | Stop ngoài **toàn bộ** đáy/đỉnh sweep |
| Chốt non | Đóng hết tại T1 | Bỏ lỡ phần lớn move swing | Chốt bậc thang IRL→ERL, dời BE |
| Trộn rule với ICT 2022 | Cắt nhanh như intraday | Phá tính swing, expectancy nhiễu | Tag `model` riêng; theo đúng bộ rule |
| Ép setup ngày không có | Cố vẽ OTE mỗi ngày | Đánh cả B/rác → cháy dần | Chấp nhận ngày no-trade |

---

## 16. Câu hỏi tự kiểm & Flashcards

### Câu hỏi tự kiểm nhanh
- Tôi đang **thuận hay ngược** HTF structure/DOL?
- Giá ở **discount hay premium**? Có đúng cho hướng của tôi không?
- OTE 62–79% có **chồng POI thật** không, hay tôi đang ép fib?
- Đã có **sweep + confirmation** khung nhỏ chưa, hay tôi vào mù?
- Setup này grade mấy? Size tương ứng? RR có ≥3R không?
- Nếu không trade, lý do "No Trade" là gì?

### Flashcards

**Q1 — Ba lớp cốt lõi của Mayne Model là gì?**
**Structure** (hướng) + **OTE** (giá vào) + **Confirmation** (thời điểm). Cả ba phải đồng ý.

**Q2 — Vùng OTE là bao nhiêu và mức "sweet spot"?**
**62–79%** retracement; sweet spot **0.705 = CE (mean threshold)**.

**Q3 — Vẽ fib cho bullish như thế nào?**
Từ **swing low → swing high** của nhịp đẩy thuận HTF; vùng vào ở phần dưới (discount).

**Q4 — Điều gì khiến setup Mayne INVALID?**
Ngược HTF bias; vào giữa range không discount/premium; OTE không chồng POI; hoặc vào mù không confirmation.

**Q5 — Stop đặt ở đâu, vì sao?**
**Ngoài đáy/đỉnh của cú sweep** (không tại pivot MSS) → tránh bị wick quét, giữ RR chặt.

**Q6 — Mayne khác ICT 2022 intraday của tôi ở điểm nào lớn nhất?**
Mayne = **swing, thuận cấu trúc, OTE-trung tâm, ít lệnh R lớn**; ICT 2022 (bản của tôi) = **intraday, killzone-centric, FVG/OB sau MSS, nhiều setup**.

**Q7 — Điều chỉnh gì khi đánh XAUUSD?**
Nới stop ngoài wick sweep (wick dài), **giảm size**, chấp nhận entry tới 0.79.

---

## 17. Liên kết với Trade Journal

### Lệnh áp dụng đúng model này
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
> Nếu vault dùng path riêng, thay `FROM ""` bằng `FROM "05 - Live Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: Mayne # Mayne | ICT-2022 | Unicorn | MMBM | MMSM | 0830-NY | 0700-IFVG
bias: bullish # bullish | bearish
context: continuation # continuation | reversal
location: discount # discount | premium
ote_level: 0.705 # 0.62 | 0.705 | 0.79
poi_type: OB # OB | FVG | breaker
sweep: true # có sweep STL/STH trước entry
confirmation: MSS # MSS | breaker | CHoCH | none
grade: A+ # A+ | A | B
rr_planned: 4.0
missing_step: none # none | structure | location | ote | poi | confirmation | stop | timing
```

> [!tip]
> Với lệnh thua, ghi `missing_step` để biết hay sai ở đâu — phổ biến nhất là `structure` (ngược bias) hoặc `confirmation` (vào mù).

---

## 18. Lesson Learned

### Bài học chính
- Mayne Model = **Structure (hướng) + OTE (giá) + Confirmation (thời điểm)** — cả ba đồng ý mới vào.
- OTE **62–79%** (sweet spot 0.705) chỉ hợp lệ khi **chồng POI + đúng P/D + thuận bias**.
- Chỉ vào **sau sweep + MSS/breaker khung nhỏ**; stop ngoài đáy/đỉnh sweep; target opposing liquidity (RR lớn).
- Đây là model **swing, ít lệnh, discretionary** — đừng trộn rule với ICT 2022 intraday.
- Để **dữ liệu backtest của chính bạn** phân xử; tag `model: Mayne` để so expectancy tách bạch.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn xác định structure HTF **trước** khi nghĩ tới entry.
- [ ] Tôi chỉ long ở discount / short ở premium, vẽ fib trên nhịp đẩy đúng.
- [ ] Tôi chờ sweep + confirmation khung nhỏ, không vào mù.
- [ ] Tôi chấm grade và size theo grade, không theo cảm xúc.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc khi trade
> **"Structure cho hướng, OTE cho giá, Confirmation cho thời điểm. Không đủ ba, không vào."**

---

## 19. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Đọc structure HTF & xác định DOL | | Phân biệt continuation vs reversal? |
| Xác định discount/premium đúng | | Chỉ vào đúng nửa range? |
| Vẽ fib OTE đúng nhịp | | Fib trên nhịp đẩy, không nhịp hồi? |
| OTE chồng POI (confluence) | | Không ép fib khi không có POI? |
| Chờ sweep + confirmation | | Không vào mù? |
| Quản trị stop/target & RR | | Stop ngoài sweep, chốt bậc thang? |
| Tách bạch với ICT 2022 | | Tag model riêng, không trộn rule? |
| Review sau trade | | Gắn `missing_step` + review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập ≥20–30 setup tag `[[Mayne Model]]` qua [[_Backtest Dashboard]].
- [ ] Review theo `missing_step`: hay sai ở `structure`, `location`, `ote`, hay `confirmation`.
- [ ] Thống kê win-rate & expectancy theo `grade`, `context`, `market`.
- [ ] So expectancy **Mayne vs ICT 2022** để biết model nào hợp bạn hơn.
- [ ] Cập nhật rule khi đủ mẫu; nâng `confidence` trong frontmatter khi đạt mastery.

---

> [!info] Liên kết mô hình
> [[01 - ICT 2022 Model]] · [[07 - Unicorn Model]] · [[26 - OTE - Optimal Trade Entry]] · [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]] · [[27 - Premium Discount]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
