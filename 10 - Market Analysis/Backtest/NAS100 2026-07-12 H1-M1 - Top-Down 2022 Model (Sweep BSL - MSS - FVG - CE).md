---
type: market-analysis
status: backtest
date: 2026-07-12
symbol: NAS100
timeframe: H1 / M15 / M5 / M1
session: replay (FXReplay - chart Dec '08)
htf_bias: bullish impulse tu ~1168 -> cham BSL/premium ~1249-1252 -> cho dao chieu (bearish co dieu kien)
setup: 2022 Model - Sweep BSL H1 -> LTF MSS + FVG -> CE entry (short)
in_trade: false
draw_on_liquidity: BSL High dealing range ~1249-1252 (da quet) · target SSL noi bo -> EQ ~1209 -> range low ~1168
key_poi: M15 Bearish FVG (sau MSS), refine bang CE
invalidation: dong nen tren dinh FVG (huy) · tren CE (canh bao som)
topic: quy trinh top-down day du + bai hoc confirmation bias & vai tro cua CE
tags:
  - analysis
  - methodology
  - NAS100
  - ict-2022
  - top-down
  - market-structure-shift
  - fair-value-gap
  - consequent-encroachment
  - draw-on-liquidity
  - buy-side-liquidity
  - premium-discount
---

# NAS100 H1 → M1 — Top-Down 2022 Model (Sweep BSL → MSS → FVG → CE) — 2026-07-12

> [!info] Trạng thái
> **CASE STUDY / METHODOLOGY — không vào lệnh.** Note này tổng hợp một phiên phân tích top-down hoàn chỉnh trên [[01 - ICT 2022 Model]]: đi từ ý định short sai ở giữa range, đến việc giá chạy lên quét **[[07 - Buy-side Liquidity|BSL]]** đúng như dự đoán, rồi xuống khung nhỏ tìm **[[21 - Market Structure Shift|MSS]] + [[13 - FVG  - Fair Value Gap|FVG]]** và tinh chỉnh entry bằng **[[10 - Consequent Encroachment (Mean Threshold)|CE]]**. Giá trị lớn nhất của note nằm ở **các bài học kỷ luật** ở mục 9, không phải ở một tín hiệu vào lệnh.
> Bổ trợ cho: [[NAS100 2026-07-12 D1-H1 - Draw on Liquidity & Daily Bias]] và [[2026-07-12 M15 - Xác định MSS khi retrace OB H1 (nến xanh liên tiếp)]].

## Sơ đồ tổng — quy trình top-down

![[NAS100-topdown-flow-20260712.svg]]

> [!warning] Screenshot gốc chưa lưu dạng file
> 7 chart TradingView/FXReplay của phiên này đang nằm trong chat, **chưa được lưu thành file**. Hãy kéo từng ảnh vào `10 - Market Analysis/Attachments/` với đúng tên bên dưới để các embed `![[...]]` hoạt động:
> `NAS100-20260712-zoom-MSS-question.png` · `NAS100-20260712-M15-context.png` · `NAS100-20260712-M15-BSL-redbox.png` · `NAS100-20260712-H1-sweep-high.png` · `NAS100-20260712-M15-MSS-FVG.png` · `NAS100-20260712-M5-CE-reaction.png` · `NAS100-20260712-M1-confirmation.png`
> Các SVG minh họa là do tôi tạo, đã lưu sẵn và sẽ hiển thị ngay.

---

## 1. Bối cảnh HTF & [[12 - Dealing Range|Dealing Range]]

![[NAS100-20260712-M15-context.png]]

Trên **M15 (FXReplay, dữ liệu Dec 2008)**, order flow gần nhất là **bullish và impulsive**: giá tạo đáy lớn ~**1168** (ngày 30) rồi rally một mạch tạo chuỗi higher high / higher low. Phía trên là vùng cung HTF — **Order Block ~1226–1235** (hình thành từ spike đỉnh ngày 20 ~1238), với **BSL / equal highs cũ ~1249–1252 vẫn còn nguyên**.

Đây là mấu chốt của cả phiên: khi phân tích bắt đầu, giá đang ở ~1213–1215 và ý định ban đầu là **short về 1192.7**. Nhưng cấu trúc lớn đang tăng và thanh khoản lớn nằm ở **phía trên** chưa bị lấy.

Dealing range tham chiếu (đọc trên H1): **High ~1249–1252 → Low ~1168**, equilibrium (50%) **~1209**.

## 2. [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]] — minor vs major BSL

![[NAS100-20260712-M15-BSL-redbox.png]]

Câu hỏi khi đó: *ô đỏ có phải Buyside Liquidity không?* Trả lời: **có, nhưng là minor / internal liquidity** — một cụm equal highs nhỏ. Lỗi tư duy là coi nó là BSL "đáng để short về", trong khi **major external BSL** thật sự nằm cao hơn nhiều (OB 1226–1235 và đỉnh cũ ~1249–1252), và **chưa bị quét**.

> [!warning] Bài học 1 — đừng nhầm minor với major liquidity
> Giá bị hút về **pool lớn chưa quét**, không phải pool nhỏ nội bộ. Short bên dưới một BSL lớn còn nguyên = bán ngược [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw on liquidity]]. Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]].

Đồng thời, ý định short ở **1213** (giữa range, dưới OB) là **entry sai vị trí** — không phải tại POI (OB ở 1226), mà ở "no man's land" giữa range → dễ bị trôi ngược, RR mỏng (~1.5R).

## 3. Sweep BSL trên H1 — "HTF cho O DAU, LTF cho KHI NAO"

![[NAS100-20260712-H1-sweep-high.png]]

Đúng như logic thanh khoản dự báo, giá **rally lên quét BSL** — chạm/vượt High dealing range (~1249–1252, hiện 1251.8). Nếu lệnh short 1213 đã được đặt, nó đã bị stop khi giá chạy lên đây → bằng chứng sống cho **Bài học 1**.

Vấn đề tiếp theo: *"đã quét đỉnh nhưng không tìm được POI nào ở đỉnh để short"*. Đây là hiểu lầm khung thời gian:

> [!summary] Bài học 2 — POI ở đỉnh KHÔNG cần có sẵn trên HTF
> HTF (H1/H4) chỉ cho biết **vùng thanh khoản** (cái "O DAU"). **POI để vào lệnh được TẠO RA trên LTF** ngay tại thời điểm đảo chiều (cái "KHI NAO"). Không thấy POI trên H1 là bình thường — phải **xuống M15/M5/M1**. Xem [[32 - Top-down Analysis (Multiple Timeframes)]].

Việc cần làm: (1) zoom **lên** H4/D1 xác nhận 1250 là điểm dừng thật, không còn draw cao hơn; (2) nếu đúng → **xuống LTF chờ MSS**; (3) nếu giá cứ nới rộng lên không có MSS → đó là breakout, đứng ngoài.

## 4. M15 — [[21 - Market Structure Shift|MSS]] + [[13 - FVG  - Fair Value Gap|FVG]] hình thành

![[NAS100-20260712-M15-MSS-FVG.png]]

Xuống M15: giá quay đầu, tạo **displacement giảm phá short-term low = MSS xuống**, để lại **FVG**. Đây chính là cái "KHI NAO" và cái POI còn thiếu ở mục 3. Nhưng trước khi tin, phải kiểm tra chất lượng POI (tránh [[10 - Mistake - FVG Not Valid|FVG không hợp lệ]]):

| Kiểm tra | Yêu cầu |
|---|---|
| FVG đúng leg? | Là gap của **chính nhịp displacement tạo MSS**, không phải gap ngẫu nhiên. |
| Hộp vẽ đúng? | Chỉ là **khoảng trống chưa giao dịch** (high nến 1 → low nến 3), không phải cả biên độ cây nến. |
| CE đúng 50%? | Đường "CE" phải là **midpoint thật** của FVG, không phải một đường tùy ý. |
| Displacement đủ mạnh? | Thân dài, để lại imbalance rõ — tránh [[08 - Mistake - Weak Displacement|weak displacement]]. |

> [!warning] Bài học 3 — "sweep + đóng lại trong OB" ≠ MSS
> Quét thanh khoản rồi đóng cửa lại trong vùng chỉ là **phản ứng / điều kiện setup**, **chưa phải trigger**. Trigger là **MSS thật** (body close phá cấu trúc + displacement + FVG). Đừng nhầm *lower high* với *sweep*, và đừng nhầm *reaction* với *MSS*. Xem [[06 - Mistake - Not Have Market Structure Shift]].

## 5. [[10 - Consequent Encroachment (Mean Threshold)|CE]] — "retrace nông = sức mạnh"

![[FVG-CE-anatomy-20260712.svg]]

Giá retrace về FVG nhưng **chỉ vào nửa dưới (giữa cạnh dưới và CE), chưa chạm CE** rồi quay xuống. Nhiều người đọc nhầm đây là điểm yếu; thực ra ngược lại:

> [!summary] Bài học 4 — CE là TRẦN, không phải SÀN
> ICT: giá **chỉ cần chạm tới CE là đủ** để FVG được coi là respected → CE là **độ sâu tối đa kỳ vọng**, không phải mức tối thiểu phải chạm. Phản ứng **trước khi** tới CE = array mạnh, phe bán vào sớm = **tín hiệu mạnh**, không phải setup lỗi.
> Hệ quả thực thi: **đừng chờ cú chạm CE hoàn hảo** (sẽ lỡ sóng với array mạnh). POI là **cả vùng cạnh-dưới ↔ CE**, và entry phải **theo xác nhận LTF** ở bất kỳ đâu trong vùng đó — không phải một limit cứng đặt đúng tại CE.

Về SL (đánh đổi RR): **chặt** = trên CE (reject dưới CE thì reclaim CE là sai) → stop nhỏ, RR đẹp, mạo hiểm hơn; **an toàn** = trên đỉnh FVG → stop rộng, RR kém. Tránh đặt SL sát đỉnh nhỏ ở nửa dưới (whippy, dễ bị quét nhiễu).

## 6. M5 — hai kịch bản & confirmation bias

![[NAS100-20260712-M5-CE-reaction.png]]

![[M5-two-scenarios-20260712.svg]]

Trên M5, sau khi reject vùng CE, một **cây xanh lớn, mạnh** kéo ngược lên. Đây là điểm dễ mắc **confirmation bias** nhất — vì nó có thể đọc theo hai hướng đối lập:

- **Kịch bản GẤU:** reject CE → displacement giảm phá cấu trúc → cây xanh chỉ là retrace về LTF FVG để short tiếp.
- **Kịch bản BÒ:** cây đen thủng biên dưới FVG thực chất **quét sạch [[30 - Sell-side Liquidity|SSL]] dưới hộp (bear trap)** → cây xanh mạnh là phản ứng mua → giá quay lên tấn công đỉnh FVG / quét lại High H1. (Xem [[33 - Turtle Soup]].)

> [!warning] Bài học 5 — đừng pre-commit, để thị trường lộ tay
> Cây xanh quá mạnh cho một "retrace" bình thường = **cờ vàng**. Không được cho rằng short vẫn thắng chỉ vì *muốn* nó thắng. Kỷ luật: **xuống M1**, không vào mù.

## 7. M1 — xác nhận, nhưng entry đã trôi qua

![[NAS100-20260712-M1-confirmation.png]]

M1 giải quyết cái mơ hồ ở M5, và nghiêng về **gấu**: giá chạm/vượt CE tạo đỉnh → **M1 MSS xuống** → nhịp hồi tạo **lower high dưới CE rồi bị reject** → tiếp tục lower highs. Cây xanh mạnh ở M5, soi trên M1, hóa ra là một **lower high** — kịch bản bò (reclaim CE) bị bác bỏ.

**Nhưng:** khi M1 xác nhận thì **điểm vào đẹp (lower-high tại CE/nửa dưới) đã trôi qua** — giá đã rơi về biên dưới hộp. Vào bây giờ = **đuổi giữa nhịp** ([[04 - Mistake - FOMO Entry|FOMO]]). Ngoài ra vùng CE↔biên dưới đang **whipsaw** (contested), nơi sinh stop-out nhiều nhất.

> [!summary] Bài học 6 — bắt được một cú không có nghĩa phải vào bằng mọi giá
> Nếu chưa ở trong lệnh: **không đuổi**. Chờ **break–retest** biên dưới hộp, hoặc **đứng ngoài**. Một "no-trade" kỷ luật là quyết định đúng — *process over outcome*.

## 8. Kế hoạch giao dịch (nếu điều kiện hội đủ)

> [!summary] Setup chuẩn (tham chiếu, không phải lệnh live)
> **POI:** M15 Bearish FVG sau MSS, refine bằng [[10 - Consequent Encroachment (Mean Threshold)|CE]]; POI = cả vùng cạnh-dưới ↔ CE.
> **Trigger:** giá vào POI → **M1 MSS xuống + lower highs + FVG** (xem [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]]).
> **Entry:** LTF FVG tại CE / nửa dưới.
> **SL:** trên đỉnh FVG (an toàn) hoặc trên CE (chặt) — tránh đỉnh nhỏ whippy.
> **Target:** SSL nội bộ (đáy MSS vừa phá) → **EQ ~1209** → range low **~1168**. TP1 ở internal liquidity, dời BE.
> **Invalidation:** đóng nến trên **đỉnh FVG** (hủy); trên **CE** (cảnh báo sớm).
> **Risk:** ≤ 0.5%; chỉ vào nếu **RR ≥ 2.0** ([[05 - Mistake - Not enough RR]]).

## 9. Bài học rút ra (tổng hợp)

1. **Minor ≠ major liquidity** — không short dưới BSL lớn chưa quét → [[02 - Mistake - Enter before liquidity sweep]].
2. **Entry phải tại POI**, không giữa range → [[03 - Mistake - Entry When MSS not in POI Zone]].
3. **HTF = "O DAU", LTF = "KHI NAO"** — POI ở đỉnh được tạo trên LTF, không tìm trên HTF.
4. **Sweep + close-back ≠ MSS**; *lower high* ≠ *sweep* → [[06 - Mistake - Not Have Market Structure Shift]].
5. **CE là trần, không phải sàn** — retrace nông = sức mạnh; đừng chờ cú chạm CE hoàn hảo.
6. **Confirmation bias tại M5** — đừng pre-commit; xuống M1 để thị trường lộ tay.
7. **Không đuổi lệnh đã lỡ** → [[04 - Mistake - FOMO Entry]]; no-trade kỷ luật là quyết định đúng.

## 10. Câu hỏi cần chốt / next steps

- Trên **H4/D1**, còn BSL/mức cao hơn ~1252 chưa quét không? Nếu còn, cả kịch bản short này vẫn là "fade sớm".
- Xác nhận 3 điểm chất lượng POI ở mục 4 (FVG đúng leg? hộp đúng gap? CE đúng 50%?) bằng giá thực tế trên FXReplay.
- Nếu có vào lệnh, điền giá **entry / SL / target** thực tế để chuyển thành một [[08 - Templates/Backtest templete|backtest]] có số liệu (hiện `in_trade: false`).

---
*Ghi chú: phiên replay (FXReplay, dữ liệu ~Dec 2008); `date` = ngày capture (VN, UTC+7). Các mức giá đọc từ chart, làm tròn — cần xác nhận lại từ replay trước khi dùng làm số liệu backtest. Không log backtest vì không vào lệnh. Ba SVG là minh họa nguyên lý, không phải chart thật.*
