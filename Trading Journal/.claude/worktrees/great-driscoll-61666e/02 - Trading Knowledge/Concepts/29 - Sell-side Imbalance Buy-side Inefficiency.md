---
type: ict-concept
concept: Sell-side Imbalance Buy-side Inefficiency
aliases:
  - Sell-side Imbalance Buy-side Inefficiency
  - SIBI
  - Sellside Imbalance Buyside Inefficiency
tags:
  - trading/ict/concept
  - trading/study
  - "#SIBI"
status: seed
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[ICT 2022 Model]]"
importance: 4
confidence: 1
last_reviewed:
created: 2026-06-24
updated: 2026-06-24
related_concepts:
  - "[[Fair Value Gap]]"
  - "[[21 - Liquidity Void]]"
  - "[[03 - Balanced Price Range]]"
  - "[[27 - Premium Discount]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[Displacement]]"
prerequisites:
  - "[[Fair Value Gap]]"
  - "[[27 - Premium Discount]]"
  - "[[Displacement]]"
common_mistakes: []
---
Refer Link: [ICT SIBI and BISI Explained — Sell-Side & Buy-Side Imbalance FVGs + Free PDF](https://innercircletrader.net/tutorials/sibi-and-bisi-the-ict-concepts/)

# Sell-side Imbalance Buy-side Inefficiency

> [!summary] Tóm tắt 1 câu
> **SIBI** là một vùng inefficiency **tăng giá (bullish)** sinh ra từ một cú **displacement đi lên** — nơi sell-side bị nuốt chửng và buy-side giao dịch không hiệu quả — đo bằng khoảng trống giữa **high của nến 1** và **low của nến 3** trong mẫu 3 nến đi lên; về bản chất nó chính là **bullish FVG nhìn qua lăng kính imbalance**, nằm trong vùng **premium** và đóng vai trò **kháng cự / mục tiêu sell-side delivery** khi giá đi lên, đồng thời là **hỗ trợ** khi giá retrace về.

> [!important] Nguyên tắc cốt lõi
> **SIBI hình thành trên cú đi LÊN và là vùng BULLISH trong PREMIUM; BISI hình thành trên cú đi XUỐNG và là vùng BEARISH trong DISCOUNT.** Hai cái là cặp đối xứng (counterpart) của nhau. Tên gọi gây nhầm vì nó mô tả "side nào bị imbalance / consumed" chứ không phải hướng giá: trong **S**ell-side **I**mbalance **B**uy-side **I**nefficiency, "Sell-side Imbalance" = phía bán bị tiêu thụ/áp đảo trong cú đẩy lên, "Buy-side Inefficiency" = việc mua diễn ra không hiệu quả (bỏ lại khoảng trống). Hệ quả: giá sẽ có xu hướng quay lại **fill** vùng đó (draw to fill) hoặc dùng nó làm hỗ trợ/kháng cự — **luôn neo nhận diện vào HƯỚNG của displacement, không neo vào chữ "Sell" trong tên.**

---

## 1. Định nghĩa

### Khái niệm
**Sell-side Imbalance Buy-side Inefficiency (SIBI)** là một khoảng trống giá (price gap / imbalance) hình thành bởi một chuỗi **3 nến đi lên có displacement**. Khoảng trống được đo từ **high của nến 1** đến **low của nến 3**: vì nến giữa (nến 2) đi quá nhanh nên không có giao dịch hai chiều (two-sided trade) lấp đầy vùng giữa `high(C1)` và `low(C3)`. Đây chính là cấu trúc một **bullish Fair Value Gap**, nhưng được gọi bằng tên imbalance để mô tả *động lực order flow* đã tạo ra nó.

```text
      C3 ┌──┐  low(C3)  ─┐
         │  │           │  <-- SIBI = vùng inefficiency
   C2 ┌──┤  │           │      (gap chưa được fill)
      │  └──┘           │
   C1 │  high(C1) ──────┘
      └──┘
  (chuỗi 3 nến đi LÊN)
```

- **Cận trên (top) của SIBI** = `low(C3)`.
- **Cận dưới (bottom) của SIBI** = `high(C1)`.
- **CE (Consequent Encroachment)** = trung điểm = `(low(C3) + high(C1)) / 2` — xem [[10 - Consequent Encroachment (Mean Threshold)]].

### Bản chất
- SIBI là **dấu vết của order flow tăng**: người bán (sell-side) bị áp đảo/hấp thụ, người mua đẩy giá lên quá nhanh, để lại một "vết nứt" trên chart.
- Vì giá thích vận hành **hiệu quả (efficient delivery)**, nên thị trường có xu hướng quay lại "tô lại" (rebalance) vùng SIBI — đây là cơ sở của ý tưởng **draw on liquidity / draw to fill**.
- SIBI nằm trong nửa **premium** của dealing range (xem [[27 - Premium Discount]] và [[12 - Dealing Range]]): nó là nơi giá đã được đẩy lên cao, do đó khi giá tiếp cận từ bên dưới nó có thể đóng vai trò **kháng cự**; khi giá đã ở trên và lùi về nó đóng vai trò **hỗ trợ**.

### Giải thích tên gọi (đọc kỹ — đây là chỗ ai cũng nhầm)
| Thành phần tên | Nghĩa thực sự | KHÔNG có nghĩa là |
|---|---|---|
| **Sell-side Imbalance** | Phía bán (sellers) bị imbalance — bị tiêu thụ / áp đảo trong cú đẩy lên | Không có nghĩa "đây là tín hiệu bán" |
| **Buy-side Inefficiency** | Việc mua (buying) diễn ra **không hiệu quả** → để lại gap chưa fill | Không có nghĩa "không nên mua" |
| **Tổng thể (SIBI)** | Một **bullish imbalance** tạo bởi displacement **lên** | Không phải tín hiệu giảm |

> Mẹo nhớ: **chữ cái đầu của side bị "Imbalance" = hướng cú đẩy.** **S**ell-side Imbalance → người **bán** bị nuốt → giá đẩy **LÊN** → **SIBI = bullish**. Ngược lại **B**uy-side Imbalance → người **mua** bị nuốt → giá đẩy **XUỐNG** → **BISI = bearish**.

### Bảng làm rõ SIBI vs BISI (clarity table)
| Tiêu chí | **SIBI** (Sell-side Imbalance Buy-side Inefficiency) | **BISI** (Buy-side Imbalance Sell-side Inefficiency) |
|---|---|---|
| Hướng cú displacement tạo ra nó | Đi **LÊN** (up-move) | Đi **XUỐNG** (down-move) |
| Side bị imbalance / consumed | **Sell-side** (người bán bị nuốt) | **Buy-side** (người mua bị nuốt) |
| Side giao dịch không hiệu quả | **Buy-side** (mua bị inefficient) | **Sell-side** (bán bị inefficient) |
| Tính chất | **Bullish** inefficiency | **Bearish** inefficiency |
| Đo gap giữa | `high(C1)` → `low(C3)` của chuỗi 3 nến **lên** | `low(C1)` → `high(C3)` của chuỗi 3 nến **xuống** |
| Tương đương FVG | **Bullish FVG** | **Bearish FVG** |
| Vùng PD Array | **Premium** | **Discount** |
| Vai trò khi giá tiếp cận | **Kháng cự** (đến từ dưới) / **Hỗ trợ** (đến từ trên / retrace) | **Hỗ trợ** (đến từ trên) / **Kháng cự** (đến từ dưới / retrace) |
| Side mà giá hướng tới delivery | Hướng tới **sell-side** (giá draw lên để fill rồi có thể đảo) | Hướng tới **buy-side** |

### So sánh SIBI vs FVG vs Liquidity Void
| Khái niệm | Định nghĩa cốt lõi | Số nến | Đặc trưng phân biệt |
|---|---|---|---|
| **SIBI** | Bullish imbalance từ cú đẩy lên, gap `high(C1)→low(C3)` | 3 nến lên | Tên mô tả order flow (sell-side bị nuốt); luôn là premium array |
| **[[Fair Value Gap]] (FVG)** | Tên trung tính cho cùng cấu trúc gap 3 nến | 3 nến | SIBI = bullish FVG; BISI = bearish FVG. FVG là tên "kỹ thuật", SIBI/BISI là tên "order flow" |
| **[[21 - Liquidity Void]]** | Vùng giá lớn gần như không có giao dịch hai chiều, thường là chuỗi nến displacement dài | nhiều nến | Rộng và "trống" hơn FVG/SIBI; thường chứa nhiều SIBI/FVG nhỏ bên trong; giá thường rebalance toàn bộ void |

> [!tip] SIBI và bullish FVG là **cùng một vật thể trên chart** — chỉ khác lăng kính. Dùng "FVG" khi nói về kỹ thuật vẽ; dùng "SIBI" khi muốn nhấn mạnh *ai bị nuốt và giá sẽ draw về đâu*.

### Mục đích trong ICT
- Đánh dấu **POI (Point of Interest)** trong premium để canh sell-side delivery hoặc canh hỗ trợ cho continuation lên.
- Là **mục tiêu (target / draw on liquidity)**: giá có thể được "kéo" lên để fill SIBI ở trên.
- Là **mốc lọc bias**: vị trí SIBI trong dealing range giúp xác nhận giá đang ở premium hay discount.

### Vì sao quan trọng
- ICT cho rằng thị trường vận hành để **lấp các inefficiency** → SIBI là bản đồ chỉ nơi giá *có lý do* để quay về.
- Kết hợp với [[Displacement]], [[21 - Market Structure Shift]] và [[20 - Liquidity Sweep]], SIBI cung cấp vùng entry/exit có logic order flow chứ không phải kẻ tay tùy ý.

### Nó giúp trả lời câu hỏi gì?
- "Giá có khả năng bị **kéo lên fill** vùng nào ở phía trên không?" → SIBI chưa fill ở premium.
- "Khi giá retrace, đâu là vùng **hỗ trợ có order flow** để canh continuation lên?" → CE của SIBI.
- "Mục tiêu (TP) hợp lý của một lệnh long là ở đâu?" → SIBI/inefficiency chưa fill phía trên.

### SIBI không phải là gì
- **Không** phải tín hiệu bán chỉ vì có chữ "Sell-side".
- **Không** phải vùng tạo bởi cú đi xuống (đó là BISI).
- **Không** phải bất kỳ khoảng trống nào — phải có **displacement** (nến giữa mạnh, có ý đồ), không phải nến do thiếu thanh khoản lèo tèo.
- **Không** đảm bảo đảo chiều; nó là vùng *quan tâm*, cần xác nhận thêm (MSS, sweep, bias).

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái
| Trạng thái SIBI | Mô tả | Hàm ý giao dịch |
|---|---|---|
| **Unmitigated (chưa fill)** | Giá chưa quay lại chạm vùng | Còn "hiệu lực" hút giá; mục tiêu draw hoặc POI tiềm năng |
| **Partially filled (fill một phần)** | Giá đã chạm tới CE nhưng chưa fill hết | CE đã được "respect"; thường vẫn còn giá trị |
| **Fully filled / closed** | Giá lấp hết vùng `high(C1)→low(C3)` | Inefficiency đã rebalance; giá trị giảm mạnh |
| **Inverted (IFVG)** | Giá đóng cửa xuyên qua → SIBI bị "lật" thành kháng cự đảo chiều | Xem [[17 - Inverse Fair Value Gap - iFVG]] — đổi vai trò |
| **SIBI trong Liquidity Void** | SIBI nằm trong một [[21 - Liquidity Void]] rộng | Khả năng giá rebalance cả void cao |

### Khi nào giá trị cao? (checklist)
- [ ] SIBI sinh ra từ **displacement rõ ràng** (nến giữa thân lớn, có ý đồ).
- [ ] Đi kèm hoặc theo sau một **[[21 - Market Structure Shift]]** ủng hộ hướng lên.
- [ ] SIBI nằm tại vùng **premium** hợp lý trong [[12 - Dealing Range]].
- [ ] Hình thành sau một **[[20 - Liquidity Sweep]]** quét sell-side liquidity bên dưới.
- [ ] Trùng (confluence) với [[Order Block]], [[Optimal Trade Entry]], hoặc mức HTF.
- [ ] Khung lớn (HTF) cũng có inefficiency cùng hướng → align bias.

### Khi nào bỏ qua? (checklist)
- [ ] Gap quá nhỏ / không có displacement (chỉ là noise).
- [ ] SIBI đã **fully filled** rồi.
- [ ] Ngược với [[12 - Daily Bias]] và HTF structure.
- [ ] Nằm giữa vùng giá đi ngang, không có liquidity rõ ràng phía trên để draw tới.
- [ ] Tin tức lớn sắp ra (rủi ro spike), trừ khi đó là setup tin của bạn.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Xác định chuỗi 3 nến đi lên** có nến giữa displacement (thân lớn, ít bóng theo hướng cản).
2. **Vẽ cận dưới** tại `high(C1)` (high của nến đầu tiên).
3. **Vẽ cận trên** tại `low(C3)` (low của nến thứ ba).
4. Điều kiện gap hợp lệ: `low(C3) > high(C1)` (có khoảng trống thực sự, không chồng lấn).
5. **Đánh dấu CE** = `(low(C3) + high(C1)) / 2` — kẻ một line ngang ở giữa làm "mean threshold".
6. **Phân vùng vai trò**: nếu giá đang ở **dưới** SIBI và tiếp cận từ dưới → coi là **kháng cự / target**; nếu giá đã ở **trên** và retrace về → coi là **hỗ trợ**.
7. **Kiểm tra fill**: theo dõi xem giá chạm CE (50%) hay fill toàn bộ để cập nhật trạng thái.

### Ma trận nhận diện
| Yếu tố | SIBI hợp lệ, chất lượng cao | SIBI yếu / nghi ngờ |
|---|---|---|
| Hướng chuỗi nến | Lên rõ ràng | Lẫn lộn, không rõ |
| Nến giữa | Displacement, thân lớn | Doji / thân nhỏ |
| Kích thước gap | Đủ lớn, đo được | Vài tick, gần như chạm |
| Vị trí PD | Premium hợp lý | Giữa range vô định |
| Confluence | OB / OTE / HTF level | Đứng một mình |
| Liquidity phía trên | Có buy-side liquidity / draw rõ | Không có target |
| Trạng thái | Unmitigated | Đã fill hết |

### Điều kiện
- **Bắt buộc**: có gap thực (`low(C3) > high(C1)`); có displacement; xác định đúng hướng (lên).
- **Tăng xác suất**: theo sau sweep sell-side liquidity; align HTF bias; trùng OB/OTE; có MSS.
- **Làm yếu đi**: gap quá nhỏ; đã fill; ngược HTF; không có liquidity để draw; hình thành trong giờ thanh khoản thấp.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Bias & bản đồ
- Xác định [[12 - Daily Bias]] và [[12 - Dealing Range]]; đánh dấu các SIBI/BISI lớn chưa fill.
- Xác định **draw on liquidity**: giá HTF đang hướng tới SIBI nào ở premium?

```text
[HTF NOTE — D1/H4]
Symbol: ____   Date: ____
Daily bias: (Bullish/Bearish) ____
Dealing range: [low range] → [high range]
SIBI HTF chưa fill: top=[level] bottom=[level] CE=[level]
Draw on liquidity: hướng tới SIBI premium? (Y/N) ____
```

### H1 / M15 — Khung trung gian
- Tinh chỉnh SIBI: SIBI nào trên H1/M15 nằm trong SIBI/premium của HTF (nested)?
- Chờ giá tiếp cận; quan sát phản ứng tại CE.

### M5 / M1 — Entry refinement
- Tìm **MSS + displacement** xác nhận, rồi entry tại SIBI/FVG nhỏ trong vùng HTF.
- Dùng CE của SIBI nhỏ làm điểm vào tinh; SL ngoài cận của SIBI.

```text
[LTF NOTE — M5/M1]
SIBI entry: top=[level] bottom=[level] CE=[level]
Trigger: MSS (Y/N) ____  Displacement (Y/N) ____
Entry @ [level]  SL @ [level]  Target = SIBI/inefficiency phía trên [level]
Planned RR: ____
```

> [!warning] Đừng "fractal lộn ngược": một SIBI trên M1 *bên trong* một vùng BISI trên H4 (bias giảm) là tín hiệu **phản xu hướng HTF** — thường chỉ là retrace để giá lấy thanh khoản trước khi đi tiếp xuống. Luôn để HTF bias quyết định, LTF chỉ tinh chỉnh entry.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Xác nhận (confirmation) — checklist
- [ ] Có **displacement** tạo SIBI (không phải gap noise).
- [ ] Giá phản ứng tại **CE** hoặc tại cận của SIBI (rejection / respect).
- [ ] Có **MSS** đồng hướng trên khung entry.
- [ ] Align với [[12 - Daily Bias]] / HTF.
- [ ] Có **liquidity / inefficiency** rõ phía trên để làm target.

### Vô hiệu hóa (invalidation) — checklist
- [ ] Giá **đóng cửa xuyên qua hết** SIBI mà không phản ứng → inefficiency đã rebalance, mất giá trị (hoặc chuyển thành IFVG, xem [[17 - Inverse Fair Value Gap - iFVG]]).
- [ ] MSS ngược hướng xuất hiện sau khi vào.
- [ ] Giá giao dịch ngược qua SL ngoài cận SIBI.

### Bảng so sánh vai trò theo hướng tiếp cận
| Giá tiếp cận SIBI từ... | Vai trò SIBI | Hành động canh |
|---|---|---|
| **Từ dưới đi lên** | Kháng cự / mục tiêu fill | Canh TP cho long; cảnh giác reaction (có thể sell-side delivery) |
| **Từ trên retrace xuống** | Hỗ trợ | Canh long continuation tại CE |
| **Đóng cửa xuyên qua** | Inversion | Cân nhắc IFVG (đổi vai) |

> [!note] "Respect CE" là dấu hiệu mạnh: nếu giá chạm đúng 50% (CE) của SIBI rồi bật, đó là bằng chứng order flow vẫn còn tôn trọng vùng — ưu tiên hơn so với fill toàn bộ.

---

## 6. Ví dụ chart

### Ví dụ ĐÚNG
![[SIBI-Example-Correct.png]]

**Mô tả:** Sau khi giá [quét sell-side liquidity] bên dưới, một cú **displacement lên** tạo SIBI sạch trong premium; giá retrace về **CE** và bật lên tiếp, fill target inefficiency phía trên.
- Chuỗi 3 nến lên rõ; nến giữa thân lớn.
- Gap đo `high(C1)=[level]` → `low(C3)=[level]`, CE=[level].
- Có [[21 - Market Structure Shift]] đồng hướng trước entry.
- Retrace về CE → long; SL dưới `high(C1)`; TP tại inefficiency phía trên [level].
- Vai trò: SIBI làm **hỗ trợ** khi giá lùi về từ trên.

### Ví dụ SAI
![[SIBI-Example-Wrong.png]]

**Mô tả:** Trader nhìn thấy chữ "Sell-side" và **bán** tại SIBI trong khi HTF bias là tăng — nhầm SIBI (bullish) với BISI (bearish).
- Cú đẩy tạo vùng này thực ra là **đi lên** → đây là SIBI = bullish.
- Bias HTF tăng; bán ở đây là phản xu hướng.
- Giá chỉ retrace nhẹ rồi tiếp tục lên, dừng lỗ lệnh sell.
- Bài học: **neo vào hướng displacement, không neo vào chữ trong tên.**

### Giải phẫu (tùy chọn)
![[SIBI-Anatomy.png]]

**Mô tả:** Hình minh họa cận trên `low(C3)`, cận dưới `high(C1)`, đường CE giữa, và mũi tên "draw to fill" hướng giá quay về rebalance.

---

## 7. Entry model liên quan

- [[ICT 2022 Model]] — sweep → MSS → displacement → entry tại FVG/SIBI.
- [[Optimal Trade Entry]] — OTE thường trùng vùng SIBI/CE.
- [[Order Block]] — OB + SIBI confluence cho POI mạnh.
- [[21 - Market Structure Shift]] — trigger xác nhận hướng trước khi dùng SIBI làm entry.
- [[16 - Internal & External Range Liquidity (IRL & ERL)]] — SIBI là IRL (mục tiêu nội vùng) hút giá.

```text
[SEQUENCE — long dùng SIBI]
1. HTF bias: bullish; xác định SIBI premium / target
2. LTF: sweep sell-side liquidity (lấy thanh khoản dưới)
3. Displacement lên → tạo SIBI mới (LTF)
4. MSS xác nhận
5. Retrace về CE của SIBI
6. Entry long @ CE | SL dưới high(C1) | TP = inefficiency phía trên
```

> [!note] SIBI có thể vừa là **entry** (khi giá retrace về nó làm hỗ trợ) vừa là **target** (khi nó là inefficiency chưa fill phía trên). Phân định rõ vai trò trước khi vào lệnh.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không vào lệnh nếu chưa tick đủ nhóm A. Nhóm B/C tăng xác suất nhưng không thay được nhóm A.

**Nhóm A — Bắt buộc**
- [ ] Đã xác định đúng đây là **SIBI (bullish, từ cú lên)**, không phải BISI.
- [ ] Có **displacement** tạo vùng.
- [ ] SIBI **chưa fill hết** (còn hiệu lực).
- [ ] Align với [[12 - Daily Bias]] / HTF.
- [ ] Có **liquidity / target** rõ phía trên.

**Nhóm B — Tăng xác suất**
- [ ] Theo sau [[20 - Liquidity Sweep]] sell-side.
- [ ] Có [[21 - Market Structure Shift]] đồng hướng.
- [ ] Confluence với [[Order Block]] / [[Optimal Trade Entry]].
- [ ] Trong killzone / phiên ưu tiên.

**Nhóm C — Quản trị rủi ro & tâm lý**
- [ ] SL nằm ngoài cận SIBI một cách logic.
- [ ] Planned RR ≥ mục tiêu cá nhân.
- [ ] Risk ≤ 0.5% theo quy tắc vault.
- [ ] Không "trả thù" lệnh trước; vào theo plan.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| **Nhầm SIBI với BISI** | Bán ở SIBI vì thấy chữ "Sell-side" | Giao dịch ngược order flow; vùng bullish bị dùng làm tín hiệu bán | Neo vào **hướng displacement**: cú LÊN = SIBI = bullish |
| Bỏ qua HTF bias | Trade SIBI LTF phản xu hướng HTF | Setup phản xu hướng tỉ lệ thua cao | Luôn cho HTF quyết bias, LTF chỉ tinh chỉnh |
| Coi mọi gap là SIBI | Vẽ vùng không có displacement | Vào ở noise, không có order flow đỡ | Yêu cầu nến giữa displacement rõ |
| Vào SIBI đã fill hết | Giá đã rebalance vùng | Hết "lực hút", vùng mất giá trị | Theo dõi trạng thái fill; chỉ dùng unmitigated/partial |
| Không xác định target | Vào nhưng không biết TP | Không có draw on liquidity → giá lình xình | Xác định inefficiency/liquidity phía trên trước |
| Bỏ qua CE | Vào sớm trước CE | Bị quét sâu hơn trước khi đi | Ưu tiên reaction tại CE (50%) |
| Đặt SL bên trong SIBI | SL nằm trong vùng gap | Dễ bị quét bởi chính dao động fill | Đặt SL ngoài cận `high(C1)` |

---

## 10. Câu hỏi tự kiểm tra
1. SIBI hình thành từ cú đi lên hay đi xuống? Nó bullish hay bearish?
2. Vẽ gap SIBI đo giữa điểm nào và điểm nào của chuỗi 3 nến?
3. SIBI nằm trong vùng premium hay discount? Vì sao?
4. "Buy-side Inefficiency" trong tên có nghĩa "không nên mua" không? Giải thích.
5. Khi giá tiếp cận SIBI từ dưới vs từ trên, vai trò của nó khác nhau thế nào?
6. CE của SIBI tính ra sao và dùng để làm gì?
7. SIBI khác Liquidity Void ở chỗ nào?
8. Điều gì khiến một SIBI bị vô hiệu hóa?

---

## 11. Flashcards / Active Recall
- **Q1:** SIBI là bullish hay bearish, sinh từ hướng nào? → **A:** Bullish, từ cú **displacement đi lên**.
- **Q2:** Cách đo gap SIBI? → **A:** Từ `high(C1)` đến `low(C3)` của chuỗi 3 nến lên.
- **Q3:** "Sell-side Imbalance" nghĩa là gì? → **A:** Phía bán bị **nuốt/áp đảo** trong cú đẩy lên (không phải tín hiệu bán).
- **Q4:** SIBI nằm ở vùng PD nào? → **A:** **Premium**.
- **Q5:** Counterpart của SIBI là gì và khác ra sao? → **A:** **BISI** — bearish, từ cú xuống, đo `low(C1)→high(C3)`, nằm ở discount.
- **Q6:** CE của SIBI là gì? → **A:** Trung điểm `(low(C3)+high(C1))/2`, dùng làm mean threshold để canh entry/reaction.

---

## 12. Lesson Learned
> [!note] Cập nhật sau mỗi lần áp dụng thực chiến/backtest.
- ____
- ____
- ____

---

## 13. Mức độ thành thạo
| Tiêu chí | Tự đánh giá (1–5) | Ghi chú |
|---|---|---|
| Hiểu khái niệm & tên gọi | ____ | |
| Phân biệt SIBI vs BISI tức thì | ____ | |
| Vẽ gap + CE chính xác | ____ | |
| Áp dụng đa khung (D1→M1) | ____ | |
| Dùng làm entry / target đúng vai | ____ | |
| Tránh các lỗi thường gặp | ____ | |

**Kế hoạch review:** ôn lại sau 1 tuần → 2 tuần → 1 tháng; cập nhật `last_reviewed`; nâng `status` seed → developing khi đã backtest ≥ ___ lần; nâng `confidence` khi phân biệt SIBI/BISI không còn do dự.