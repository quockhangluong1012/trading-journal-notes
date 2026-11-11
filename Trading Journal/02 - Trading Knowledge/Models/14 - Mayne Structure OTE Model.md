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
last_reviewed: 2026-07-28
created: 2026-07-12
updated: 2026-07-28
prerequisites:
  - "[[26-OTE-Optimal-Trade-Entry]]"
  - "[[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]"
  - "[[27-Premium-Discount]]"
  - "[[20-Liquidity-Sweep]]"
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
> Mục 1–3 = *WHAT* (định nghĩa, cơ chế, cấu phần). Mục 4–7 = *HOW* (chuỗi hình thành, bullish/bearish, OTE, entry/stop/target). Mục 8–11 = *nâng cao* (grading, cross-market, so sánh với ICT 2022 thuần, confluence). Mục 12–15 = *phản biện, edge case, case study, kinh nghiệm live/backtest* (đọc kỹ trước khi risk-on thật). Mục 16–23 = *thực chiến & prop-firm*. Nếu mới học Mayne, đọc 1→7 trước.

---

## 1. Định nghĩa

![[MayneOTE-Anatomy.svg|712]]

**Khái niệm:** Mayne Model là cách Trader Mayne "đóng gói" các mảnh ICT rời rạc thành một quy trình *thuận xu hướng, ưu tiên swing*. Bốn thành phần ICT mà anh ấy dựa vào — đúng như bạn nhận ra — là:
- **Market Structure** ([[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]], [[05-BOS-Break-of-Structure]], [[09-Change-of-Character]]) → xác định *hướng*.
- **Liquidity** ([[19-Liquidity]], [[20-Liquidity-Sweep]], [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]) → xác định *đích đến* (DOL) và *nhiên liệu* cho move.
- **PD Array / POI** ([[25-OB-Order-Block]], [[13-FVG-Fair-Value-Gap]], [[04-Breaker-Block]]) → *nơi* giá phản ứng.
- **OTE** ([[26-OTE-Optimal-Trade-Entry]]) → *giá vào chính xác* trong POI, cho stop chặt & RR lớn.

**Nó trả lời câu hỏi nào trên chart?**
- Trong một xu hướng đang chạy, **hồi tới đâu thì vào** cho RR tốt nhất mà không "bắt dao rơi"?
- Làm sao biến một POI rộng (OB/FVG) thành **một điểm vào cụ thể** với rủi ro định nghĩa rõ?
- Khi nào cú hồi là "cơ hội tiếp diễn" thay vì "đảo chiều"?

**Vì sao đây là model "swing" của Mayne:** anh ấy đọc bias trên **D1/H4**, chờ pullback nhiều nến, và giữ lệnh hướng tới opposing liquidity ở xa — nên một setup có thể chạy vài ngày. Triết lý của Mayne là **đơn giản + ít lệnh + R bất đối xứng lớn**: thà đợi một setup A+ 1:5R còn hơn 10 lệnh 1:1 lộn xộn.

### Mayne Model KHÔNG phải là gì
- Không phải scalp intraday tần suất cao — nó ưu tiên **continuation swing** trên HTF (bản này giữ nguyên phong cách gốc của Mayne).
- Không phải "vào bất kỳ OTE nào" — OTE chỉ hợp lệ khi **thuận cấu trúc + đúng P/D + trùng POI + có xác nhận**.
- Không phải hệ thống **100% cơ học** — bước xác nhận khung nhỏ (MSS/breaker) mang tính *discretionary*; Mayne nói thẳng model cần "chart time" và phải được cá nhân hóa.
- Không phải cái cớ bỏ qua quản trị rủi ro — vẫn ≤0.5%/lệnh ([[43-Position-Sizing]]).

---

## 2. Vì sao model hoạt động — ba lớp đồng thuận

> [!important] Hiểu WHY trước khi hỏi WHAT
> Trader mới copy "vẽ fib 62–79% rồi mua" mà không hiểu vì sao — nên họ mua OTE ngược trend hoặc giữa range rồi thua. Ba lớp dưới đây là *lý do* Mayne Model có edge.

**Lớp 1 — Structure = xác suất nền (base rate).** Đứng *cùng phía* với cấu trúc HTF nghĩa là đứng cùng phía [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung|Draw on Liquidity]]. Trong uptrend, thị trường có "nợ" thanh khoản phía trên (BSL chưa quét); giá có động cơ đi lên lấy nó. Mua trong pullback của uptrend = bạn giao dịch *theo* dòng chảy tổ chức, không chống lại.

**Lớp 2 — OTE = giá vào tối ưu (risk-defined).** Vùng [[26-OTE-Optimal-Trade-Entry|OTE 62–79%]] là nơi cú hồi đã đủ sâu để (a) quét thanh khoản nội vi, (b) cho phép đặt stop *ngay dưới* đáy swing/đáy sweep — tức stop **chặt**. Vì entry sâu và target xa, **RR bung ra**. Mức **0.705 = Consequent Encroachment (CE)** ([[10-Consequent-Encroachment-Mean-Threshold]]) là "mean threshold" của nhịp đẩy — điểm cân bằng mà thuật toán hay tôn trọng.

**Lớp 3 — Confirmation = lọc thời điểm (timing/edge).** OTE chỉ là *vùng*, không phải *tín hiệu*. Chờ một [[21-Market-Structure-Shift|MSS]] / [[04-Breaker-Block|breaker]] / [[09-Change-of-Character|CHoCH]] trên khung nhỏ **ngay tại OTE** giúp lọc bỏ trường hợp "OTE bị xuyên thẳng" (khi thực ra HTF đang đảo). Đây là cách Mayne biến một limit mù rủi ro cao thành một entry *có phản hồi từ thị trường*.

> [!warning] Hệ quả quan trọng
> Nếu chỉ có 1–2 lớp thì đây **không phải** setup Mayne A. OTE + structure nhưng *không* confirmation = hạ cấp. Structure + confirmation nhưng vào ngoài OTE (giữa range) = RR kém. **Edge nằm ở giao của cả ba.**

Liên hệ sâu: [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] — đám đông bán đáy pullback (đặt SSL ngay dưới), chính SSL đó là nhiên liệu cho cú sweep trước khi giá bật; Mayne đứng *sau* cú sweep, cùng phía tổ chức.

---

## 3. Cấu phần bắt buộc

| Cấu phần | Khung | Vai trò | Concept liên quan |
|---|---|---|---|
| **HTF Structure + Bias** | D1 / H4 | Xác định hướng (HH-HL hay LH-LL) & DOL | [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]], [[59-Daily-Bias]] |
| **Pullback vào P/D** | H4 / H1 | Giá hồi về discount (long) / premium (short) | [[27-Premium-Discount]], [[12-Dealing-Range]] |
| **POI (PD Array)** | H1 / M15 | Vùng phản ứng: OB / FVG / breaker thuận cấu trúc | [[25-OB-Order-Block]], [[13-FVG-Fair-Value-Gap]], [[04-Breaker-Block]] |
| **OTE Fib 62–79%** | trên nhịp đẩy | Tinh chỉnh điểm vào, ưu tiên 0.705 (CE) | [[26-OTE-Optimal-Trade-Entry]], [[10-Consequent-Encroachment-Mean-Threshold]] |
| **Liquidity Sweep** | M15 / M5 | Quét STL/STH tại vùng hồi = nhiên liệu | [[20-Liquidity-Sweep]], [[15-Inducement]], [[33-Turtle-Soup]] |
| **LTF Confirmation** | M5 / M1 | MSS / breaker / CHoCH xác nhận entry | [[21-Market-Structure-Shift]], [[09-Change-of-Character]], [[41-Change-in-State-of-Delivery]] |
| **Target = opposing liquidity** | HTF | BSL (long) / SSL (short), IRL trước ERL sau | [[16-Internal-External-Range-Liquidity-IRL-ERL]], [[19-Liquidity#7. Buy-Side Liquidity (BSL)\|Buy-side Liquidity]], [[19-Liquidity#8. Sell-Side Liquidity (SSL)\|Sell-side Liquidity]] |

> [!tip] Quy tắc "đủ 4 trước khi nghĩ tới entry"
> Trước khi zoom xuống tìm confirmation, phải có đủ: (1) bias HTF rõ, (2) giá đang ở **đúng nửa** range (discount cho long), (3) một POI thật trong vùng hồi, (4) OTE của nhịp đẩy **chồng** lên POI đó. Thiếu bất kỳ điều nào → chưa phải cơ hội.

---

## 4. Chuỗi hình thành (6 bước)

![[MayneOTE-Formation-Sequence.svg|712]]

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

![[MayneOTE-Bullish-vs-Bearish.svg|712]]

**Bullish (uptrend):** cấu trúc HH-HL → giá hồi về **discount** → OTE 62–79% chồng bullish OB/FVG → **sweep SSL** (đáy nội vi) → **MSS lên** khung nhỏ → **long**. Target = **BSL** / đỉnh trước (DOL).

**Bearish (downtrend):** cấu trúc LH-LL → giá hồi lên **premium** → OTE 62–79% chồng bearish OB/FVG → **sweep BSL** (đỉnh nội vi) → **MSS xuống** khung nhỏ → **short**. Target = **SSL** / đáy trước (DOL).

> [!tip] Ưu tiên khi phân vân
> Mayne Model gốc là **continuation-first**. Nếu không chắc đang tiếp diễn hay đảo chiều, **mặc định coi là continuation** và chỉ đánh thuận DOL HTF. Reversal chỉ đánh khi cấu trúc HTF *đã* chuyển (đã có CHoCH/MSS trên chính HTF), không phải "hy vọng đảo".

---

## 6. OTE — lõi của Mayne Model

![[MayneOTE-Zone-Diagram.svg|712]]

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

![[MayneOTE-Example-Correct.svg|712]]

- **Entry:** sau khi giá vào OTE + sweep + **xác nhận cấu trúc khung nhỏ** (MSS/breaker/CHoCH). Có 2 trường phái:
  - *Confirmation entry* (đúng tinh thần Mayne): chờ MSS khung nhỏ rồi vào — an toàn hơn, bỏ lỡ vài lần.
  - *Limit tại 0.705*: đặt trước tại CE của OTE trùng POI — vào được nhiều setup hơn nhưng cần P/D + bias thật chắc.
- **Stop:** **ngoài đáy của cú sweep** (long) / **ngoài đỉnh sweep** (short) — hoặc ngoài mép xa POI. KHÔNG đặt tại pivot MSS (quá chặt, dễ bị wick quét).
- **Target:** **opposing liquidity** theo DOL HTF — [[16-Internal-External-Range-Liquidity-IRL-ERL|IRL trước, ERL sau]]. Dời stop về BE sau khi chạm T1. Vì đây là swing, target ERL thường cho **RR 3–5R+**.
- **Timing:** với NQ/FX intraday-swing, ưu tiên vùng hình thành quanh [[18-Kill-Zones|killzone]] London/NY; với swing thuần thì timing ít quan trọng hơn cấu trúc.

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

**Điểm giao (cả hai cùng dùng):** [[20-Liquidity-Sweep|sweep]], displacement, [[21-Market-Structure-Shift|MSS]], [[27-Premium-Discount|premium/discount]], [[25-OB-Order-Block|OB]]/[[13-FVG-Fair-Value-Gap|FVG]], [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung|DOL]].

> [!warning] Đừng trộn rule của hai game
> Nếu backtest, hãy **tag rõ** `model: Mayne` vs `model: ICT-2022` để so expectancy tách bạch. Một thói quen tối ưu cho intraday 2022 (vào nhiều, cắt nhanh) có thể phá vỡ tính swing của Mayne (cần kiên nhẫn giữ lệnh tới ERL).

---

## 11. Xếp chồng confluence (Confluence Stack)

Structure + OTE là *lõi*; các lớp dưới là *chất xúc tác* nâng grade:

- **Sweep + Turtle Soup** ([[33-Turtle-Soup]], [[15-Inducement]]): cú hồi quét đúng một STL/STH "mồi" trước khi bật = xác nhận nhiên liệu.
- **SMT Divergence** ([[42-SMT-Divergence]]): NQ vs ES, EU vs GU phân kỳ tại điểm sweep của OTE = xác nhận mạnh.
- **CISD / Displacement chất lượng** ([[41-Change-in-State-of-Delivery]]): nến xác nhận thân lớn tại OTE → confirmation "sạch".
- **Killzone / Macro** ([[18-Kill-Zones]], [[40-Macro-Times]]): với NQ/FX, OTE hình thành trong killzone đáng tin hơn.
- **NWOG/NDOG lân cận** ([[24-New-Week-Opening-Gap]], [[23-New-Day-Opening-Gap]]): OTE gần gap mở cửa thường được tôn trọng hơn.
- **Unicorn overlap** ([[07 - Unicorn Model]]): nếu OTE 0.705 trùng vùng **breaker + FVG chồng lấn** → đây là biến thể A+ (Mayne × Unicorn).

> [!note] Nguyên tắc confluence
> Confluence để **nâng grade & size**, không để "biện minh" cho setup thiếu lõi. Không bao giờ: "ngược bias nhưng có SMT nên vẫn vào".

---

## 12. Phản biện & Giới hạn của mô hình

> [!warning] Đọc mục này TRƯỚC khi risk-on thật
> Mục đích không phải phá niềm tin vào Mayne Model, mà để bạn tách được phần **có thể kiểm định** khỏi phần **narrative không kiểm định được** — và tự backtest với con mắt hoài nghi đúng mức.

### A. Vấn đề epistemic — "smart money điều phối giá qua IPDA" là gì?
Mayne Model thừa hưởng nguyên xi giả định nền tảng của ICT: có một "smart money"/thuật toán (IPDA) chủ động dẫn giá tới các mức thanh khoản, và các tỷ lệ Fibonacci (62–79%, 0.705) là mức "thuật toán tôn trọng". Đây là **narrative không thể kiểm chứng trực tiếp** — không có cách nào chứng minh hay bác bỏ "thuật toán ngân hàng dùng đúng 0.705" từ dữ liệu giá công khai.

**Giải thích thay thế hợp lý không kém:**
- **Auction Market Theory:** giá dao động quanh vùng giá trị (value area); retracement 60–80% chỉ là hệ quả thống kê tự nhiên của biến động hai chiều quanh một xu hướng, không cần "ai đó" nhắm tới.
- **Mean-reversion quanh tin tức:** nhiều retracement sâu xảy ra quanh giờ tin (London/NY open, macro) do thanh khoản mỏng rồi dày trở lại — không liên quan gì tới "bẫy thanh khoản có chủ đích".
- **Volatility clustering:** biến động lớn (impulse) có xu hướng đi kèm biến động lớn tiếp theo (điều hồi sâu) — hiện tượng đã biết trong tài chính định lượng, không cần giả thuyết "thao túng".
- **Self-fulfilling vì đông người trade cùng công thức:** khi hàng chục nghìn trader retail cùng vẽ fib 62–79% và đặt lệnh quanh đó, chính hành vi tập thể này tạo ra phản ứng giá tại vùng đó — không phải vì "smart money" định trước, mà vì đám đông ICT tạo ra chính cái họ đang cố phát hiện.

> [!note] Không cần tin narrative để dùng model
> Bạn không cần tin "smart money" có tồn tại để OTE vẫn có ích — chỉ cần công nhận: (1) retracement 60–80% là vùng RR tốt về mặt hình học (stop chặt, target xa), (2) đủ nhiều người hành động giống nhau tại đó để tạo phản ứng ngắn hạn. Hai điều này không đòi hỏi niềm tin vào IPDA.

### B. Phản biện đặc thù: OTE 62–79% có cơ sở thống kê không?
Đây là điểm yếu lớn nhất của riêng mô hình Mayne so với các model khác:
- **Không có nghiên cứu thống kê công khai nào** chứng minh retracement dừng lại chính xác trong khoảng 62–79% thường xuyên hơn các khoảng khác. Độ sâu hồi giá (retracement depth) trong thực tế phân phối **liên tục** — không có "bức tường" tại 62% hay 79%; giá có thể dừng ở 45%, 55%, 83%, 91% với tần suất không nhỏ.
- Con số 0.705 (CE) đến từ toán học của chính công thức Fibonacci (trung điểm giữa hai mức 0.618 và 0.786, xấp xỉ), **không phải từ một phát hiện thực nghiệm** về hành vi giá.
- Việc "0.705 là mean threshold thuật toán tôn trọng" là một khẳng định định tính lặp lại trong cộng đồng ICT/Mayne, chưa từng thấy kèm dữ liệu backtest lớn, đa thị trường, đa khung thời gian được công bố công khai.
- **Hệ quả thực dụng:** không dùng OTE như một "vùng thiêng" tự thân. OTE chỉ có giá trị khi là **một trong nhiều bộ lọc** (POI + P/D + sweep + confirmation) — đúng như mục 2 của bài đã nhấn mạnh "OTE không dùng đơn lẻ". Phản biện này củng cố thêm lý do tại sao Mayne bắt buộc thêm lớp confirmation thay vì tin thuần fib.

### C. Degrees of freedom — vấn đề lớn nhất khi chọn swing leg để kéo fib

![[MayneOTE-Advanced-DegreesOfFreedom.svg|712]]

> [!info] Mô tả hình
> Cùng một chart, 3 trader chọn 3 cặp swing anchor khác nhau (nhịp lớn nhất A→D, nhịp cuối C→D, nhịp giữa B→D) để kéo fib — ra 3 vùng OTE không trùng nhau, minh họa bậc tự do (degrees of freedom) lớn nhất trong việc áp dụng model.

Đây là phản biện đặc thù quan trọng nhất với Mayne Model: **vùng OTE phụ thuộc hoàn toàn vào việc chọn swing leg nào để kéo fib.**
- ICT 2022 gốc còn có FVG/OB là điểm neo tương đối khách quan (khoảng trống giá cụ thể). Mayne Model đặt fib là **thấu kính trung tâm**, nhưng "nhịp đẩy gần nhất" là khái niệm **discretionary**: nhịp từ đáy nào tới đỉnh nào? Có tính luôn phần internal retracement nhỏ trong nhịp đó không?
- Trên chart thật, gần như luôn có ≥3 cách hợp lý để chọn cặp swing high/low làm anchor — mỗi cách cho một vùng OTE khác nhau vài chục pip/point.
- Đây chính là bậc tự do (degree of freedom) lớn nhất trong các model ICT: bạn có thể luôn "tìm ra" một cách vẽ fib khiến giá "trúng OTE" sau khi đã biết kết quả — đây là gốc rễ của hindsight bias khi backtest Mayne (xem thêm mục D).
- **Cách giảm thiểu:** cố định quy tắc TRƯỚC khi vào lệnh — ví dụ "chỉ vẽ trên nhịp có displacement rõ (≥2 nến thân lớn liên tiếp), tính từ swing point được xác nhận bởi BOS/CHOCH gần nhất" — và áp dụng nhất quán, không đổi quy tắc giữa chừng để "cho vừa" một setup đẹp.

### D. Phản biện: fib kéo trên wick vs body cho hai vùng OTE khác nhau

![[MayneOTE-Advanced-WickVsBody-Fib.svg|712]]

> [!info] Mô tả hình
> So sánh song song: kéo fib theo đáy/đỉnh wick cho vùng OTE rộng và sâu hơn; kéo theo thân nến (body/close) cho vùng OTE hẹp và nông hơn — cùng một nhịp giá nhưng hai kết quả khác nhau.

Ngay cả khi đã thống nhất chọn đúng cặp swing anchor, vẫn còn một lựa chọn discretionary khác: **đo theo wick (đuôi nến) hay theo body (thân nến/close)?**
- Kéo theo wick cho vùng OTE rộng và "sâu" hơn (entry dễ khớp hơn nhưng đôi khi giá đã đảo trước khi chạm).
- Kéo theo body cho vùng OTE hẹp và "nông" hơn (entry sát giá hơn nhưng dễ hụt nếu chỉ có wick chạm mà không có nến đóng cửa trong vùng).
- Cả ICT gốc lẫn Mayne đều không có quy tắc chính thức công bố rõ ràng cho việc này — mỗi trader/mentor có thói quen riêng. Trader mới dễ nhầm lẫn khi so hai chart "giống hệt nhau" từ hai nguồn nhưng vẽ khác kết quả.
- **Khuyến nghị:** chọn MỘT chuẩn (khuyến nghị: wick cho nến xác nhận swing, body cho phần nội bộ nếu volatility cao như Gold/NQ) và ghi rõ vào rule cá nhân, backtest thống nhất theo đúng chuẩn đó.

### E. Structure mapping (BOS/CHOCH) — nhiều trường phái đếm swing khác nhau
Một lớp mơ hồ khác nằm ngay ở bước 1 (HTF Structure): "swing high/swing low" được đếm khác nhau tùy trường phái.
- **Mayne gốc** thường dùng swing đơn giản (fractal 3-nến hoặc mắt nhìn trực quan trên D1/H4).
- **ICT gốc** nhấn mạnh Short-Term Low/High, Intermediate-Term Low/High, Long-Term Low/High — phân cấp có định nghĩa chặt hơn theo số lượng nến xác nhận.
- **SMC (Smart Money Concepts, các trường phái phái sinh khác)** dùng quy tắc đếm BOS/CHOCH riêng, đôi khi yêu cầu đóng nến ngoài swing, đôi khi chỉ cần wick.
- **Hệ quả:** một trader dùng chuẩn Mayne có thể thấy cấu trúc là "HH-HL" (uptrend còn nguyên), trong khi một trader dùng chuẩn ICT phân cấp đầy đủ đã thấy "CHOCH" (đảo chiều) trên cùng chart, cùng thời điểm — hai bias mâu thuẫn trực tiếp.
- **Cách giảm thiểu:** chọn một trường phái đếm swing DUY NHẤT (ví dụ: 01 - Advance Market Structure của bộ tài liệu này) và dùng xuyên suốt để bias không bị "nhảy" tùy theo bạn đang xem nguồn nào.

### F. OTE không có yếu tố thời gian — khác các model killzone-based
Khác với 08:30 NY Model, Venom, hay Silver Bullet — vốn giới hạn cửa sổ vào lệnh theo giờ cụ thể — **Mayne/OTE không có bộ lọc thời gian bắt buộc**. Hệ quả hai chiều:
- **Ưu điểm:** linh hoạt hơn, có thể áp dụng cho swing đa khung mà không bị ràng buộc "chỉ được vào trong 09:50–10:10 NY".
- **Nhược điểm (thường bị bỏ qua):** vì không có timing filter, model dễ bị dùng để "biện minh" cho việc vào lệnh bất kỳ giờ nào miễn giá chạm OTE — kể cả giờ thanh khoản mỏng (tối thứ Sáu, đêm châu Á với FX major) nơi phản ứng giá kém tin cậy hơn hẳn. Bảng mục 9 (theo thị trường) đã gợi ý timing tốt hơn cho từng thị trường, nhưng đây **không phải quy tắc cứng của Mayne gốc** — dễ bị trader bỏ qua khi ép setup.
- **Khuyến nghị tự đặt filter:** nếu trade NQ/FX, ưu tiên OTE hình thành trong killzone London/NY dù model không bắt buộc; nếu swing thuần đa ngày, chấp nhận timing kém quan trọng hơn nhưng vẫn tránh entry cuối phiên thứ Sáu/đầu tuần thanh khoản mỏng.

### G. Rủi ro thống kê khi backtest Mayne Model
- **Hindsight bias kép:** không chỉ "nhìn lại chart nào cũng thấy setup" (bias chung của ICT), Mayne còn cộng thêm bias chọn swing leg (mục C) — tức là hai lớp hindsight chồng lên nhau, dễ khiến backtest tay có winrate ảo cao hơn live rất nhiều.
- **Degrees of freedom:** chọn nhịp đẩy nào, chọn POI nào (OB hay FVG hay breaker), chọn khung xác nhận nào (M15/M5/M1) — mỗi lựa chọn là một "nút vặn" có thể chỉnh sau khi biết kết quả, dẫn tới overfit trên tập dữ liệu đã xem.
- **Sample size nhỏ do bản chất ít lệnh:** Mayne cố ý "ít lệnh, R lớn" — nghĩa là để có 100 mẫu backtest cần theo dõi rất nhiều tuần/tháng D1/H4, lâu hơn nhiều so với model intraday. Kết luận rút ra từ 15–20 lệnh dễ nhiễu do may rủi ngẫu nhiên.
- **Survivorship của case được chia sẻ:** các ảnh chụp màn hình "Mayne setup thắng lớn" lan truyền trên mạng xã hội chỉ là phần nổi — không ai đăng 5 lần OTE bị xuyên thẳng không bật. Đừng suy ra winrate từ mật độ ảnh đẹp bạn thấy online.

### H. Điều kiện thị trường làm mô hình gãy
- **Trend không có pullback sạch** (climax/parabolic move, thường quanh tin lớn hoặc short squeeze): giá không hồi về 62–79% mà chạy thẳng — chờ OTE nghĩa là đứng ngoài toàn bộ move.
- **Range/sideway kéo dài không có DOL rõ:** không có "nhịp đẩy" đúng nghĩa để kéo fib — ép vẽ fib trong range là vẽ trên nhiễu, không phải trend.
- **Volatility nén rồi giãn đột ngột** (trước/sau tin lớn): fib vẽ trước tin trở nên vô nghĩa ngay khi tin ra vì cấu trúc bị viết lại hoàn toàn.
- **Thị trường có gap lớn** (mở cửa tuần, sau kỳ nghỉ): nhịp đẩy "gần nhất" có thể bị gap che khuất, khiến swing anchor không phản ánh đúng cung/cầu thật.

### I. Cách tự kiểm định khách quan
1. **Pre-registration:** viết quy tắc chọn swing anchor, wick/body, khung xác nhận... TRƯỚC khi xem forward data — không sửa quy tắc giữa chừng.
2. **Forward test thật** (demo hoặc size rất nhỏ) song song với backtest tay, so lệch kết quả.
3. **Đếm cả setup bị bỏ lỡ** (không chỉ lệnh đã vào) — nếu bạn chỉ ghi lệnh đã trade, bạn đang bỏ qua toàn bộ trường hợp OTE không phản ứng (survivorship nội bộ).
4. **Walk-forward:** chia dữ liệu theo thời gian, tối ưu trên đoạn đầu, kiểm định trên đoạn sau chưa từng "nhìn" khi chỉnh quy tắc.
5. **Tối thiểu 100+ mẫu/regime** trước khi kết luận model "có edge" trên một thị trường/điều kiện cụ thể — với tần suất ít lệnh của Mayne, việc này có thể mất nhiều tháng, đây là lý do càng cần kỷ luật ghi chép từ sớm.

---

## 13. Edge cases & Failure modes (mở rộng)

> [!important] Đây là các tình huống chỉ ai live/backtest đủ lâu mới gặp
> Mỗi case theo cấu trúc: **hiện tượng → cách nhận diện sớm → hành động đúng → bài học**.

### Edge case 1 — Retrace chỉ dừng ở 50–58% rồi chạy thẳng (miss entry)
- **Hiện tượng:** giá hồi chưa tới 62% đã đảo chiều mạnh và chạy hết move, không bao giờ chạm vùng OTE bạn đang chờ.
- **Cách nhận diện sớm:** nến phản ứng tại 50–58% có thân lớn, đóng cửa mạnh, kèm volume/momentum bất thường (thường sau tin bất ngờ hoặc sweep thanh khoản nhỏ ở đúng vùng 50%).
- **Hành động đúng:** nếu có POI thật (OB/FVG) chồng đúng vùng 50–58% + đã có MSS khung nhỏ xác nhận, đây vẫn có thể là entry hợp lệ dạng "OTE nông" — không cứng nhắc chờ đúng 62% nếu các lớp còn lại đã đồng thuận. Nếu không có POI, chấp nhận bỏ lỡ, không đuổi giá.
- **Bài học:** OTE 62–79% là vùng ưu tiên, không phải điều kiện cần duy nhất; một CE/POI mạnh ở nông hơn vẫn đáng cân nhắc nếu cấu trúc + xác nhận đều rõ.

### Edge case 2 — Retrace xuyên 79%, chạm 88.6% rồi mới đảo (SL bị quét oan)

![[MayneOTE-Advanced-CaseStudy-Loss-SLSweep886.svg|712]]

> [!info] Mô tả hình
> Case tái dựng: giá vào lệnh tại 0.705, tiếp tục xuyên qua 0.79 và quét SL đặt ngoài vùng OTE tại khoảng 0.886, sau đó mới đảo chiều đúng hướng ban đầu — minh họa rủi ro "đúng hướng, sai timing/SL".

- **Hiện tượng:** bạn vào tại 0.705 với SL hợp lý ngoài đáy sweep, nhưng giá tiếp tục xuyên qua 0.79, chạm gần 0.886/1.0 rồi mới bật đúng hướng ban đầu — bạn bị quét lệnh oan dù bias đúng.
- **Cách nhận diện sớm:** đây thường xảy ra ở thị trường có wick dài/volatility cao (Gold, NQ những phiên tin) — nến tại OTE không có MSS/CISD rõ ràng, chỉ là một cây nến phản ứng yếu rồi tiếp tục giảm.
- **Hành động đúng:** với thị trường biết trước là "hay xuyên sâu" (xem mục 9 — XAUUSD), nới SL ra ngoài 0.886/1.0 và giảm size tương ứng thay vì SL sát 0.79; hoặc chờ MSS thật sự đóng nến xác nhận trước khi vào thay vì vào sớm tại 0.705.
- **Bài học:** "đúng hướng nhưng sai điểm vào/SL" là một dạng thua phổ biến và không đồng nghĩa model sai — đây là lý do phải tách bạch review theo `missing_step: stop` riêng với `missing_step: structure`.

### Edge case 3 — Fib kéo trên wick vs body cho hai vùng OTE lệch nhau

![[MayneOTE-Advanced-WickVsBody-Fib.svg|712]]

> [!info] Mô tả hình
> Xem mô tả tại mục 12.D — minh họa hai cách đo (wick/body) cho hai entry khác nhau trên cùng một nhịp giá.

- **Hiện tượng:** bạn backtest lại một setup cũ theo trí nhớ, ra kết quả khác với lúc live vì lần này vô thức đo fib theo body thay vì wick (hoặc ngược lại).
- **Cách nhận diện sớm:** khi hai vùng OTE tính ra chênh nhau đáng kể (>15–20% khoảng nhịp đẩy), đó là dấu hiệu bạn đang ở biên giới wick/body — cần chốt quy tắc trước khi tiếp tục.
- **Hành động đúng:** cố định MỘT chuẩn đo (khuyến nghị: wick để xác định 0% và 100% anchor, nhưng ưu tiên xác nhận bằng nến đóng cửa trong vùng OTE trước khi entry) và áp dụng nhất quán.
- **Bài học:** thiếu chuẩn hóa bước đo fib là một nguồn nhiễu âm thầm trong dữ liệu backtest cá nhân — dễ khiến bạn nghĩ "model không nhất quán" trong khi vấn đề là quy trình đo của chính bạn không nhất quán.

### Edge case 4 — Leg mở rộng (extension) làm phải vẽ lại fib giữa chừng
- **Hiện tượng:** bạn vẽ fib trên nhịp đẩy A→B, đang chờ giá hồi vào OTE thì giá bất ngờ tạo thêm một chân đẩy mới vượt qua B (tới C) trước khi hồi — toàn bộ vùng OTE cũ giờ sai vì "nhịp đẩy" thực ra chưa kết thúc ở B.
- **Cách nhận diện sớm:** giá tiếp tục đóng nến mới cao hơn (bullish) hoặc thấp hơn (bearish) đỉnh/đáy bạn dùng làm anchor 100% trước khi kịp hồi về OTE cũ.
- **Hành động đúng:** vẽ lại fib ngay khi swing point mới được xác nhận (A→C thay vì A→B); vùng OTE mới sẽ cao hơn/thấp hơn vùng cũ — không cố "giữ" vùng cũ chỉ vì đã trót vẽ.
- **Bài học:** OTE là một vật thể động, không tĩnh — cần cập nhật lại mỗi khi cấu trúc tạo swing point mới, đặc biệt ở thị trường nhiều nhịp nhỏ như NQ (xem mục 9).

### Edge case 5 — OTE trùng FVG (confluence) vs OTE trơ trọi (không POI)

![[MayneOTE-Advanced-FVGConfluence-vs-Naked.svg|712]]

> [!info] Mô tả hình
> So sánh song song: bên trái OTE chồng đúng một FVG thật (phản ứng dứt khoát, grade A/A+); bên phải OTE không có POI nào chồng lên (giá chop, không phản ứng rõ, nên bỏ hoặc hạ grade).

- **Hiện tượng:** hai setup nhìn "giống Mayne" như nhau về mặt fib, nhưng một cái có FVG/OB thật chồng đúng vùng 62–79%, cái còn lại chỉ có con số fib suông không có POI nào.
- **Cách nhận diện sớm:** trước khi vào lệnh, luôn tự hỏi "nếu bỏ đường fib đi, tôi có còn nhìn thấy một POI thật (khoảng trống giá, order block rõ ràng) tại đây không?" Nếu câu trả lời là không, đây là OTE trơ trọi.
- **Hành động đúng:** OTE trơ trọi (không có FVG/OB) tự động hạ xuống nhóm "Bỏ qua" hoặc tối đa Grade B theo mục 8 — không nâng cấp giả bằng cách "thấy giá phản ứng nhẹ thì coi như có POI".
- **Bài học:** đây là lý do mục 3 yêu cầu "đủ 4 trước khi nghĩ tới entry" — thiếu riêng lớp POI là đủ để loại một setup, dù fib có đẹp tới đâu.

### Edge case 6 — Double purge: sweep 2 lần trước khi giá thực sự đảo tại OTE
- **Hiện tượng:** giá quét STL lần 1 tại OTE, bật nhẹ như sắp MSS nhưng lại rớt xuống quét STL lần 2 (thấp hơn lần 1) trước khi mới thực sự đảo chiều — trader vào ngay sau sweep lần 1 bị dính SL.
- **Cách nhận diện sớm:** sweep lần 1 không đi kèm displacement rõ (chỉ 1 nến wick dài đơn lẻ, không có 2–3 nến thân lớn xác nhận); volume/momentum yếu ngay sau sweep.
- **Hành động đúng:** chờ MSS thực sự đóng nến xác nhận phá cấu trúc khung nhỏ, không vào ngay khi thấy wick sweep đầu tiên; nếu đã vào và bị quét lần 2, đây là tín hiệu để chờ sweep tiếp theo thay vì gồng hoặc revenge trade ngay.
- **Bài học:** "một cú sweep" không đảm bảo đó là cú sweep cuối cùng — double/triple purge phổ biến hơn người mới nghĩ, đặc biệt quanh vùng thanh khoản dày (số tròn, đáy/đỉnh tuần trước).

### Edge case 7 — MSS xác nhận bằng wick vs bằng đóng nến (body-close) cho tín hiệu khác nhau
- **Hiện tượng:** giá xuyên qua swing pivot bằng wick (MSS "kiểu wick") nhưng đóng cửa lại bên trong cấu trúc cũ — một số trader coi đây đã là MSS hợp lệ, số khác chờ nến đóng cửa hẳn ngoài pivot (MSS "kiểu body-close") mới xác nhận.
- **Cách nhận diện sớm:** theo dõi xem nến phá pivot có đóng cửa vượt qua mức đó hay chỉ có râu nến chạm tới rồi rút lại.
- **Hành động đúng:** MSS kiểu wick vào sớm hơn nhưng tỷ lệ nhiễu (false break) cao hơn; MSS kiểu body-close vào trễ hơn (entry xấu hơn chút) nhưng đáng tin hơn. Chọn một chuẩn cố định theo mức độ chấp nhận rủi ro, không đổi qua lại giữa hai kiểu tùy tiện.
- **Bài học:** đây là một trong những điểm "discretionary" Mayne thừa nhận thẳng — nhưng discretionary không có nghĩa là tùy hứng; vẫn cần một quy tắc nhất quán được viết ra trước.

### Edge case 8 — Spread giãn tại London Open/rollover 5PM NY làm SL bị quét oan dù đúng hướng
- **Hiện tượng:** entry đúng tại OTE, cấu trúc đúng, nhưng SL bị quét bởi một cú giãn spread đột ngột lúc London mở cửa hoặc giờ rollover 5PM NY (đặc biệt trên FX/Gold), không phải bởi price action thật.
- **Cách nhận diện sớm:** SL của bạn đặt gần đúng vào khung giờ rollover/London open; broker có spread thả nổi (variable spread) thay vì cố định.
- **Hành động đúng:** biết trước lịch giãn spread của broker, tránh đặt SL sát các mốc pivot ngay trước giờ rollover nếu có thể; nếu bắt buộc giữ lệnh qua giờ đó, nới SL thêm một biên đủ để chịu được spread giãn tạm thời thay vì SL lý thuyết sát nhất.
- **Bài học:** một số lệnh thua không phải do model sai mà do cấu trúc chi phí giao dịch (spread/rollover) — cần tách riêng khi thống kê `missing_step`, đừng quy hết về lỗi đọc cấu trúc.

### Edge case 9 — DST (giờ mùa) làm lệch khung killzone tham chiếu khi backtest xuyên năm
- **Hiện tượng:** khi backtest dữ liệu nhiều tháng liền, các mốc "killzone London/NY" tính theo giờ ET bị lệch 1 tiếng so với giờ địa phương của bạn vào các thời điểm chuyển đổi DST (tháng 3 và tháng 11 tại Mỹ, ngày chuyển khác tại châu Âu) — dữ liệu bị gắn sai nhãn thời gian nếu không cập nhật.
- **Cách nhận diện sớm:** thấy các setup "trong killzone" nhưng biểu đồ thực tế cho thấy setup xảy ra sớm/muộn hơn 1 tiếng so với khung giờ bạn quen.
- **Hành động đúng:** luôn tính giờ theo ET (Eastern Time) làm chuẩn thay vì giờ địa phương cố định; kiểm tra lịch DST hai vùng (Mỹ và châu Âu chuyển ngày khác nhau) khi backtest chart đa năm.
- **Bài học:** vì Mayne ít phụ thuộc timing hơn model intraday, DST ít ảnh hưởng trực tiếp tới entry, nhưng vẫn ảnh hưởng gián tiếp khi bạn dùng killzone làm bộ lọc phụ (mục 11) — đảm bảo nhãn thời gian đúng trước khi kết luận "setup trong killzone thắng nhiều hơn".

### Edge case 10 — Entry limit đặt tại 0.705 không khớp vì giá chỉ chạm mép ngoài vùng OTE
- **Hiện tượng:** bạn đặt lệnh limit chờ sẵn tại 0.705 theo trường phái "Limit tại 0.705" (mục 7), nhưng giá chỉ chạm tới khoảng 0.66–0.68 rồi đảo chiều — lệnh không khớp, sau đó giá chạy đúng hướng bạn dự đoán mà không có bạn trong lệnh.
- **Cách nhận diện sớm:** nến phản ứng đầu tiên trong vùng OTE xuất hiện ở phần nông (gần 0.62) với thân lớn — dấu hiệu giá có thể không cần đi sâu tới 0.705.
- **Hành động đúng:** với setup có nhiều lớp confluence mạnh (POI rõ, sweep đã xảy ra ở phần nông), cân nhắc đặt thêm một limit phụ gần mép 0.62 thay vì chỉ đặt độc nhất tại 0.705; hoặc chấp nhận đây là chi phí của trường phái limit — đổi lại việc limit vào được nhiều setup hơn tổng thể.
- **Bài học:** trường phái limit tại 0.705 và trường phái chờ confirmation có đánh đổi khác nhau — limit ăn nhiều setup hơn nhưng cũng có tỷ lệ "hụt do chưa tới giá" riêng, không chỉ có rủi ro "vào mù".

### Edge case 11 — Gap cuối tuần hoặc gap tin lớn "nuốt" toàn bộ vùng OTE đã vẽ
- **Hiện tượng:** bạn vẽ OTE cho phiên tuần tới dựa trên cấu trúc H4 cuối tuần trước, nhưng giá mở cửa tuần mới (hoặc sau tin lớn) gap thẳng qua toàn bộ vùng OTE, khiến vùng đó không còn được test lại theo cách thông thường.
- **Cách nhận diện sớm:** theo dõi lịch kinh tế/tin cuối tuần và early Sunday/Monday open để dự đoán khả năng gap; nếu NWOG (New Week Opening Gap) lớn xuất hiện ngay sát vùng OTE, khả năng "nuốt" vùng đó là có thật.
- **Hành động đúng:** sau gap lớn, vẽ lại cấu trúc và fib từ dữ liệu mới thay vì cố đợi giá "quay lại lấp gap để test OTE cũ" — điều này có thể không xảy ra trong khung thời gian hợp lý. Coi gap như một sự kiện tái thiết lập cấu trúc (structure reset).
- **Bài học:** OTE được vẽ trên dữ liệu quá khứ không có "quyền" bắt giá phải quay lại — gap là một trong những lý do khiến setup A+ trên giấy không bao giờ được test trên thực tế.

---

## 14. Case studies — mổ xẻ sâu

> [!warning] Về tính xác thực
> Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa — không gắn với ngày/giờ thị trường cụ thể có thể kiểm chứng sai. Không bịa số liệu thị trường thật; các đặc điểm phiên/tin (killzone, NFP/FOMC/CPI generic) chỉ mô tả đặc điểm phổ biến đã biết.

### Case 1 (WIN) — Continuation swing NQ: sweep SSL tại OTE + MSS M5, target BSL cũ

**Bối cảnh HTF:** D1/H4 NQ đang trong uptrend rõ (chuỗi HH-HL nhiều tuần liền), DOL là một vùng BSL cũ nằm cách giá hiện tại một khoảng đáng kể phía trên. Dealing range hiện tại có EQ rõ ràng; giá vừa đóng nến H4 rút khỏi vùng premium, bắt đầu hồi.

**Diễn biến theo mốc:**
- *H4:* giá hồi từ đỉnh gần nhất, cắt xuống dưới EQ, tiến vào vùng discount — đúng điều kiện bước 2 của quy trình.
- *H1:* xuất hiện một bullish OB rõ ràng nằm trong vùng discount, trùng gần đúng khoảng 62–79% của nhịp đẩy H4 gần nhất khi kéo fib theo quy tắc đã cố định trước (wick anchor, nhịp có displacement).
- *M15→M5:* giá tiếp tục hồi vào vùng OTE, quét một STL nội vi (đáy hình thành vài giờ trước) bằng một wick rõ, sau đó in liền 2 nến M5 thân lớn tăng, phá qua swing high gần nhất trên M5 → MSS lên hợp lệ theo kiểu body-close.

**Quyết định & lý do:** trader chờ đúng cả 3 lớp (structure thuận, OTE chồng OB, sweep+MSS xác nhận) trước khi vào — không vào sớm khi mới thấy wick quét STL. Entry đặt ngay sau nến MSS đóng cửa, gần vùng 0.705.

**Kết quả (R):** Stop đặt ngoài đáy toàn bộ cú sweep (không tại pivot MSS). Target chia bậc: T1 = IRL gần nhất (dời BE sau khi chạm), T2 = BSL/DOL ban đầu. Tổng kết quả minh họa: khoảng **+4.2R**.

**Mổ xẻ lỗi/điểm đúng quy trình:** điểm đúng lớn nhất là kiên nhẫn chờ đủ 3 lớp thay vì vào ngay khi giá "trông có vẻ" chạm OTE. Không có lỗi quy trình đáng kể trong case này — đây là ví dụ mẫu của setup A+ theo đúng chấm điểm mục 8.

**Bài học chuyển hóa thành rule:** "Không có MSS body-close trên khung xác nhận = không vào, bất kể OTE + POI đẹp thế nào." Rule này được ghi vào checklist cá nhân sau case.

---

### Case 2 (LOSS) — OTE đẹp trên GBPUSD nhưng xuyên qua 0.79 quét SL trước khi đảo đúng hướng

**Bối cảnh HTF:** D1 GBPUSD trong xu hướng tăng vừa phải, DOL là BSL tuần trước. Giá hồi về discount sau một nhịp đẩy H4 có displacement rõ.

**Diễn biến theo mốc:**
- *H4/H1:* OTE 62–79% được vẽ đúng theo quy tắc cố định (wick anchor), chồng gần đúng một FVG nhỏ hình thành trong nhịp đẩy trước đó.
- *M15:* giá vào vùng OTE, xuất hiện một nến phản ứng đầu tiên tại khoảng 0.68 nhưng không có displacement rõ (thân nhỏ, không phá cấu trúc M5 nào).
- *M5:* trader nóng vội vào lệnh ngay tại nến phản ứng đó (chưa có MSS thật sự đóng nến), đặt SL sát ngay dưới đáy nến đó — quá gần theo đúng kiểu lỗi "stop tại pivot" đã cảnh báo ở mục 7.
- Giá tiếp tục xuyên xuống, quét qua 0.79, chạm gần 0.886 — nơi có SL của trader — trước khi thực sự tạo MSS M5 hợp lệ và bật đúng hướng ban đầu.

**Quyết định & lý do:** vào lệnh sớm vì "sợ bỏ lỡ" khi thấy OTE + POI đẹp, bỏ qua yêu cầu chờ confirmation thật sự.

**Kết quả (R):** dừng lỗ tại mức đã đặt quá sát, kết quả **-1R**, trong khi nếu chờ MSS thật (xuất hiện sau đó ở vùng gần 0.85–0.886) và đặt SL ngoài toàn bộ vùng xuyên, giao dịch đúng quy trình lẽ ra vẫn có thể đạt **+3R theo hướng ban đầu**.

**Mổ xẻ lỗi/điểm đúng quy trình:** lỗi kép — (1) vào mù không chờ MSS thật, (2) SL đặt tại pivot quá chặt thay vì ngoài toàn bộ vùng sweep tiềm năng. Điểm đúng: bias HTF và vị trí P/D (discount) đều chính xác — đây không phải lỗi đọc cấu trúc mà là lỗi thực thi/quản trị lệnh.

**Bài học chuyển hóa thành rule:** "Trên cặp/thị trường có lịch sử xuyên sâu qua 0.79 (theo bảng mục 9), mặc định chờ đóng nến xác nhận MSS thay vì vào tại nến phản ứng đầu tiên; đặt SL tính thêm biên cho khả năng chạm tới 0.886."

---

### Case 3 (NO-TRADE/MISS) — OTE trơ trọi trên XAUUSD, đúng đắn bỏ qua rồi giá chạy mạnh

**Bối cảnh HTF:** D1 Gold trong xu hướng tăng dài hạn, DOL là một vùng BSL rất xa phía trên. Giá hồi về gần vùng discount sau một nhịp tăng có displacement.

**Diễn biến theo mốc:**
- *H4:* fib OTE được kéo đúng quy tắc, vùng 62–79% rơi vào một khu vực giá không có OB/FVG rõ ràng nào — chỉ là một đoạn giá "trống", không có cấu trúc POI cụ thể.
- *M15:* giá đi vào vùng OTE, dao động qua lại (chop) không có sweep rõ, không có nến phản ứng thân lớn.
- Trader áp dụng đúng checklist mục 3 ("đủ 4 trước khi nghĩ tới entry"): OTE có, nhưng thiếu hẳn lớp POI thật → theo mục 8, đây thuộc nhóm "Bỏ qua". Trader quyết định không trade, ghi log `missing_step: poi`.

**Quyết định & lý do:** dù rất muốn vào vì bias + vị trí đều đúng, thiếu POI là đủ để loại setup theo rule đã tự đặt trước (pre-registration, mục 12.I).

**Kết quả (R):** không có lệnh nào được mở. Giá sau đó tiếp tục hồi sâu hơn dự kiến (xuyên qua cả vùng OTE ban đầu) rồi mới thực sự bật và chạy một nhịp mạnh hướng lên — nếu trader đã vào tại 0.705 như một OTE "trơ trọi" thông thường, khả năng cao đã bị quét trước khi giá bật.

**Mổ xẻ lỗi/điểm đúng quy trình:** không có lỗi — đây là ví dụ mẫu của kỷ luật "no-trade" đúng. Cảm giác tiếc nuối (giá cuối cùng vẫn chạy đúng hướng) không đồng nghĩa quyết định sai; quyết định được đánh giá bằng **quy trình tại thời điểm ra quyết định**, không phải bằng kết quả nhìn lại.

**Bài học chuyển hóa thành rule:** "Đánh giá chất lượng quyết định bằng thông tin có tại thời điểm đó, không phải bằng những gì giá làm sau này (outcome bias). Ghi nhận các case no-trade đúng quy trình vào thống kê để không bị hiểu nhầm là 'bỏ lỡ do sợ hãi'."

---

## 15. Kinh nghiệm live/backtest ít người nói (mở rộng)

### Slippage/spread thực tế đúng thời điểm model entry
Vì Mayne thường vào lệnh sau MSS/breaker trên khung rất nhỏ (M5/M1), entry hay rơi vào đúng lúc biến động tăng đột ngột (ngay sau displacement) — đây là thời điểm spread trên FX/Gold hoặc slippage trên NQ/futures thường **giãn tạm thời**, không phải mức spread trung bình bạn thấy lúc thị trường yên tĩnh. Khi backtest tay trên chart lịch sử, gần như không thể mô phỏng đúng độ giãn này — dẫn tới kết quả backtest luôn đẹp hơn live một khoảng cố định. Cách bù trừ thực dụng: cộng thêm 1–3 pip (FX)/vài tick (NQ)/$0.3–0.5 (Gold) vào entry giả định khi backtest để ước lượng gần đúng hơn với live.

### Khác biệt demo vs live vs funded account (drawdown rule làm méo execution)
- **Demo:** không có áp lực tâm lý thật, dễ chờ đủ cả 3 lớp (structure + OTE + confirmation) một cách kỷ luật — kết quả demo thường tốt hơn live đáng kể dù cùng một bộ rule.
- **Live tài khoản cá nhân:** áp lực tiền thật khiến trader dễ vào sớm hơn (sợ bỏ lỡ) hoặc thoát sớm hơn (sợ mất lời) so với kế hoạch — đúng dạng lỗi "chốt non tại T1" đã liệt kê ở mục 7.
- **Funded/prop-firm account:** có thêm ràng buộc **daily/max drawdown** — điều này làm méo execution của chính Mayne Model, vốn là model swing "giữ lệnh nhiều ngày, ít lệnh". Nếu một lệnh Mayne đang mở khiến floating drawdown tiến gần ngưỡng daily loss limit, trader funded buộc phải đóng sớm bất kể setup còn hợp lệ — đây không phải lỗi đọc model, mà là xung đột cấu trúc giữa một model swing và luật risk ngày của prop-firm. **Khuyến nghị:** giảm size Mayne trên tài khoản funded có daily drawdown chặt, hoặc chỉ áp dụng Mayne trên loại tài khoản cho phép giữ lệnh qua đêm/qua nhiều ngày mà không bị siết theo ngày.

### Tâm lý sau 2–3 loss liên tiếp đúng model
Vì Mayne ít lệnh, một chuỗi 2–3 loss liên tiếp chiếm tỷ trọng tâm lý lớn hơn nhiều so với model intraday nhiều lệnh (nơi một chuỗi thua tương tự "trôi qua" trong vài giờ). Phản ứng phổ biến: nghi ngờ toàn bộ model, tăng size để "gỡ" ở lệnh tiếp theo, hoặc bắt đầu vào cả những setup Grade B để có thêm cơ hội — cả ba đều sai hướng. Cách xử lý đúng: **trước khi trade tiếp, kiểm tra lại 2–3 loss đó là lỗi thực thi (`missing_step` cụ thể) hay đơn thuần là biến động bình thường của một model có winrate <100%** (xem mục chuỗi thua nhị thức bên dưới).

### Chuỗi thua theo phân phối nhị thức với winrate của model
Với một model có winrate thực tế giả định quanh 40–45% (điển hình cho các model "ít lệnh, R lớn" như Mayne khi tính đúng cả setup Grade A/A+), xác suất gặp một chuỗi 3 lệnh thua liên tiếp trong một dãy dài lệnh **không hề nhỏ** — đây là hệ quả toán học của phân phối nhị thức, không phải dấu hiệu "model hỏng". Trước khi kết luận model không còn hoạt động, hãy tính thử: với winrate ~40%, xác suất có ít nhất một chuỗi 3 thua liên tiếp trong 20 lệnh là khá cao một cách tự nhiên. Việc hiểu con số này giúp tránh bỏ model đúng lúc nó đang hoạt động bình thường trong biên độ ngẫu nhiên của nó.

### Journaling `missing_step` — mở rộng thực dụng
Ngoài các nhãn đã có (`structure`, `location`, `ote`, `poi`, `confirmation`, `stop`, `timing`), với Mayne Model nên tách thêm hai nhãn phụ để phản ánh đúng các edge case ở mục 13: `fib_anchor` (chọn sai/khác nhịp đẩy để kéo fib — mục 12.C) và `execution_cost` (thua do spread/slippage/rollover chứ không phải đọc sai cấu trúc — Edge case 8). Tách rõ hai nhãn này giúp thống kê cuối tuần không đổ oan mọi lỗi về "đọc sai structure" trong khi vấn đề thực ra nằm ở khâu đo lường hoặc chi phí giao dịch.

### Kỳ vọng tần suất setup A+ thực tế
Với một trader theo dõi 2–3 cặp/thị trường (ví dụ NQ + EURUSD + XAUUSD) trên khung D1/H4, tần suất setup đạt đủ Grade A/A+ theo đúng mục 8 (≥4–6/6 confluence) thực tế thường rơi vào khoảng **vài setup mỗi tuần**, không phải mỗi ngày — đây là bản chất "ít lệnh" mà Mayne chủ đích hướng tới. Trader mới thường đánh giá thấp việc này và vô tình hạ chuẩn xuống Grade B để có đủ "cảm giác hoạt động" mỗi ngày — đây chính là lỗi "ép setup ngày không có" đã liệt kê ở bảng lỗi thường gặp (mục 19).

### Khi nào được phép tăng size
Chỉ tăng size sau khi thỏa đồng thời: (1) đã tích lũy ≥30 mẫu backtest/forward-test được tag `model: Mayne` rõ ràng theo đúng mục 21, (2) expectancy dương nhất quán qua ít nhất 2 giai đoạn thị trường khác nhau (ví dụ một giai đoạn trend rõ và một giai đoạn biến động hơn), (3) tỷ lệ `missing_step: none` (thực thi đúng quy trình) chiếm đa số trong các lệnh thua — nếu phần lớn lệnh thua vẫn do lỗi thực thi, tăng size chỉ khuếch đại lỗi, chưa phải lúc. Không tăng size chỉ vì "vài lệnh gần đây thắng" — đây là sai lầm amateur đã nêu ở bảng mục 17 (Amateur vs Professional).


---

## 16. Ví dụ chart

### Ví dụ đúng
![[MayneOTE-Example-Correct.svg|712]]

**Mô tả:** thuận HTF bias (uptrend), giá hồi về discount, OTE 62–79% chồng OB, quét STL rồi in MSS khung nhỏ → long; stop dưới đáy sweep; target BSL. Stop chặt + target xa = RR lớn.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lệnh thật: đánh dấu (1) cấu trúc HTF + DOL, (2) nhịp đẩy dùng vẽ fib, (3) OTE 62–79% + POI, (4) điểm sweep + MSS khung nhỏ, (5) entry/stop/T1/T2. Ghi giờ ET + grade.*

### Ví dụ sai / dễ nhầm
![[MayneOTE-Example-Wrong.svg|712]]

**Ba lỗi:** (a) vào giữa range/premium không đợi OTE-discount → RR kém; (b) OTE đẹp nhưng **ngược HTF bias** → bẫy; (c) vào limit mù, không chờ MSS/breaker khung nhỏ → "bắt dao rơi".

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lần bạn (hoặc người khác) gọi nhầm là Mayne setup: đánh dấu vì sao thiếu lớp (structure / OTE / confirmation).*

---

## 17. Thực hành tốt nhất (Best Practices)

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

## 18. Checklist trước khi vào lệnh

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

## 19. Lỗi thường gặp

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

## 20. Câu hỏi tự kiểm & Flashcards

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

## 21. Liên kết với Trade Journal

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

## 22. Lesson Learned

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

## 23. Mức độ thành thạo

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
> [[01 - ICT 2022 Model]] · [[07 - Unicorn Model]] · [[26-OTE-Optimal-Trade-Entry]] · [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]] · [[27-Premium-Discount]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]
