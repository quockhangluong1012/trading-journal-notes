---
type: ict-concept
concept: Top-down Analysis (Multiple Timeframes)
aliases:
  - Top-down Analysis
  - Multiple Timeframe Analysis
  - MTF
  - Top Down
tags:
  - trading/ict/concept
  - trading/study
  - "#TopDownAnalysis"
status: seed
category: Market Structure
last_reviewed:
created: 2026-06-26
updated: 2026-07-03
---

# Top-down Analysis (Multiple Timeframes)

> [!summary] Tóm tắt 1 câu
> **Top-down Analysis là quy trình phân tích đi từ khung thời gian CAO xuống khung THẤP — HTF dựng narrative & xác định [[12 - Daily Bias]] và draw on liquidity → Intermediate xác định POI/PD-array & [[12 - Dealing Range]] → LTF chờ giá tới POI trong [[18 - Kill Zones]] rồi tìm xác nhận (sweep → MSS → displacement → entry) — sao cho MỌI quyết định LTF đều nằm bên trong câu chuyện của HTF.**

> [!important] Nguyên tắc cốt lõi
> - **HTF luôn thắng LTF.** Một setup LTF "đẹp" nhưng ngược bias HTF là một cái bẫy, không phải cơ hội. Context HTF override mọi mô hình LTF đẹp mắt.
> - **Phân tích theo thứ tự CAO → THẤP, không bao giờ ngược lại.** Bắt đầu từ LTF rồi "ép" một câu chuyện lên HTF là sai lầm gốc rễ.
> - **Ba câu hỏi, ba tầng khung:** Bias (HTF) → POI (Intermediate) → Entry (LTF). Mỗi tầng trả lời đúng một câu hỏi, không lẫn lộn.
> - **Phải có draw on liquidity (DOL) trước khi xuống khung thấp.** Không biết giá đang "bị hút" về đâu thì không có lý do để vào lệnh.
> - **Khung thời gian phải ĐỒNG THUẬN (fractal / nested).** Chỉ execute entry LTF khi nó cùng hướng với bias HTF và phản ứng tại POI Intermediate.

---

## 1. Định nghĩa

### Khái niệm
**Top-down Analysis (Multiple Timeframe Analysis / MTF)** là kỷ luật phân tích thị trường **từ khung thời gian cao nhất xuống thấp nhất**, sao cho mỗi quyết định ở khung thấp luôn nằm bên trong một narrative đã được dựng ở khung cao. Đây không phải một mô hình giá (price pattern), mà là một **quy trình / workflow** tổ chức toàn bộ cách bạn đọc chart.

Phân cấp khung điển hình theo phong cách ICT:
- **HTF (Monthly / Weekly / Daily):** dựng **narrative vĩ mô** và xác định [[12 - Daily Bias]] — draw on liquidity (DOL) ở đâu? giá đang [[27 - Premium Discount|premium hay discount]]? những PD-array & liquidity pool HTF nào đang trong cuộc chơi?
- **Intermediate (4H / 1H):** định vị **POI / PD-array** mà giá sẽ phản ứng; đánh dấu [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL/ERL]]; tinh chỉnh bias và [[12 - Dealing Range]].
- **LTF (15m / 5m / 1m):** chờ giá chạm POI của HTF **trong [[18 - Kill Zones]]**, rồi tìm xác nhận: [[20 - Liquidity Sweep]] → [[21 - Market Structure Shift]] (MSS) → displacement → [[Fair Value Gap|FVG]]/[[Order Block|OB]] entry.

### Bản chất
- Top-down Analysis biến thị trường thành một cấu trúc **fractal lồng nhau (nested)**: bức tranh lớn của Weekly chứa bức tranh Daily, Daily chứa H4/H1, và H1 chứa M5/M1. Một entry M5 chỉ có ý nghĩa khi nó là một mảnh khớp với bức tranh lớn.
- Khung cao trả lời **"đi đâu" (where / why)** — bias & draw. Khung thấp trả lời **"vào lúc nào, ở đâu" (when / where exactly)** — timing & entry. Đảo ngược vai trò này là nguồn của hầu hết các lệnh xấu.
- Quy trình này **lọc nhiễu**: phần lớn tín hiệu LTF bị loại bỏ vì không khớp với HTF — đó là tính năng, không phải lỗi.

### Phân cấp khung thời gian (timeframe hierarchy)

```text
┌─ HTF (MN / W1 / D1) ── BIAS & DRAW ──────────────────────┐
│  • Daily Bias: bullish / bearish?                        │
│  • Draw on Liquidity (DOL): giá bị hút về đâu?            │
│  • Premium / Discount của dealing range lớn?             │
│        │                                                 │
│        ▼ (xuống khung)                                   │
│  ┌─ Intermediate (H4 / H1) ── POI & RANGE ────────────┐  │
│  │  • POI / PD-array giá sẽ phản ứng                   │  │
│  │  • Dealing Range + IRL / ERL                        │  │
│  │  • Refine bias, khoanh vùng chờ                     │  │
│  │        │                                            │  │
│  │        ▼ (xuống khung)                              │  │
│  │  ┌─ LTF (M15 / M5 / M1) ── ENTRY & TIMING ──────┐   │  │
│  │  │  • Chờ giá tới POI trong Kill Zone            │   │  │
│  │  │  • Sweep → MSS → displacement → FVG/OB         │   │  │
│  │  │  • Entry + SL logic + RR                       │   │  │
│  │  └──────────────────────────────────────────────┘   │  │
│  └─────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
        Bias (HTF) → POI (Intermediate) → Entry (LTF)
```

### Mục đích trong ICT
- Đảm bảo **mọi entry phục vụ một narrative HTF** thay vì là phản ứng cảm tính với một cây nến đẹp.
- Cung cấp một **chuỗi quyết định lặp lại được**: bias → POI → entry — nền tảng của [[ICT 2022 Model]].
- Giúp **lọc** setup ngược trend và tránh "bắt dao rơi" giữa range.

### Vì sao khái niệm này quan trọng
- Hầu hết lệnh thua không phải vì entry xấu mà vì **context sai**: vào đúng kỹ thuật LTF nhưng ngược bias HTF. Top-down chính là lớp phòng vệ chống lại điều này.
- Nó chuyển trader từ "săn tín hiệu" sang "đọc câu chuyện" — từ phản xạ sang quy trình.

### Nó giúp trả lời câu hỏi nào trên chart?
- Giá đang ở đâu trong narrative **lớn** (Weekly/Daily)?
- Draw on liquidity tự nhiên — giá đang bị hút về đâu?
- Giá đang ở **premium hay discount**, đã chạm POI HTF chưa?
- Đã đủ điều kiện để **xuống LTF tìm entry** chưa, hay vẫn còn phải chờ?
- Setup LTF này có **đồng thuận** với HTF không, hay đang ngược dòng?

### Top-down Analysis không phải là gì
- **Không phải** một entry signal — nó là cái khung chứa entry; bản thân nó không cho điểm vào.
- **Không phải** "mở càng nhiều khung càng tốt" — quá nhiều khung gây analysis paralysis. Chọn một bộ 3 khung gắn kết.
- **Không phải** phân tích từ dưới lên — bắt đầu từ M1 rồi suy ngược lên Daily là làm sai chiều.
- **Không phải** lý do để bỏ qua [[18 - Kill Zones]] — đúng giá nhưng sai thời gian vẫn là setup yếu.

---

## 2. Bối cảnh sử dụng

### Các bộ khung thời gian khuyến nghị (ICT-style paired timeframes)

| Bộ khung | HTF (Bias/Draw) | Intermediate (POI) | LTF (Entry) | Phù hợp với |
|---|---|---|---|---|
| **Daily-anchored** | D1 | H1 / M15 | M5 / M1 | Day trading NQ1/NAS100, FX |
| **4H-anchored** | H4 | M15 | M1 | Intraday refine, scalping có context |
| **Weekly-anchored** | W1 | D1 / H4 | H1 / M15 | Swing, định draw cả tuần |
| **Macro swing** | MN / W1 | D1 | H4 / H1 | Position, giữ nhiều ngày |

> [!tip]
> Nguyên tắc chọn bộ khung: **mỗi bước xuống một khung nên cách nhau khoảng 4–6 lần** (ví dụ D1 → H1 → M5). Đừng nhảy từ Daily thẳng xuống M1 mà bỏ qua tầng Intermediate — đó là bước hay bị bỏ sót nhất.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có [[12 - Daily Bias]] rõ ràng và một draw on liquidity (DOL) xác định trên HTF.
- [ ] Giá đang ở [[27 - Premium Discount|premium/discount]] phù hợp với hướng bias.
- [ ] Có POI HTF/Intermediate rõ (OB, FVG, NWOG/NDOG, liquidity pool) để giá phản ứng.
- [ ] Có liquidity pool ([[16 - Internal & External Range Liquidity (IRL & ERL)|IRL/ERL]]) làm target rõ.
- [ ] Thời điểm tiếp cận nằm trong [[18 - Kill Zones]] (London / NY).

### Khi nào nên bỏ qua / không xuống LTF?
- [ ] Bias HTF không rõ — giá đang loanh quanh giữa [[12 - Dealing Range]].
- [ ] Không có draw on liquidity rõ ràng → không biết giá đi đâu.
- [ ] Giá chưa chạm POI HTF (đừng tìm entry "trong không khí").
- [ ] Ngoài kill zone / có high-impact news đang chi phối.
- [ ] Các khung mâu thuẫn nhau và không có cách hòa giải hợp lý.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu một quy trình top-down "khỏe mạnh"
1. **Một câu narrative HTF viết được thành lời:** "Giá ở discount Daily, draw lên buyside [level] phía trên."
2. **Một POI Intermediate cụ thể** đã được khoanh, kèm IRL/ERL.
3. **Giá thực sự đã tới (hoặc đang tới) POI đó** — không phải đang ở giữa range.
4. **Một trigger LTF** (sweep → MSS → FVG) xảy ra **bên trong** POI, **trong kill zone**.
5. **Hướng entry = hướng bias HTF.** Ba tầng cùng kể một câu chuyện.

### Ma trận đồng thuận khung thời gian (alignment matrix)

| Tầng | Câu hỏi | Khung | Hợp lệ (✓) | Cờ đỏ (✗) |
|---|---|---|---|---|
| **HTF — Bias** | Đi đâu? Vì sao? | MN/W1/D1 | Bias rõ + DOL xác định | Giữa range, không DOL |
| **Intermediate — POI** | Phản ứng ở đâu? | H4/H1 | POI cụ thể, đúng P/D | Không có POI / sai P/D |
| **LTF — Entry** | Vào lúc nào? | M15/M5/M1 | Sweep+MSS+FVG trong POI, trong KZ | Trigger giữa range / ngoài KZ |
| **Đồng thuận** | Ba tầng có khớp? | — | Cùng hướng | LTF ngược bias HTF |

### Điều kiện bắt buộc (must-have)
- [ ] [[12 - Daily Bias]] HTF được xác định **trước** khi xuống khung.
- [ ] Một **draw on liquidity** rõ ràng (giá bị hút về đâu).
- [ ] Một **POI Intermediate** cụ thể đã khoanh vùng.
- [ ] Hướng entry LTF **đồng thuận** với bias HTF.

### Điều kiện tăng xác suất (nice-to-have)
- [ ] POI có **confluence**: OB + FVG + liquidity + [[24 - New Week Opening Gap|NWOG]]/[[23 - New Day Opening Gap|NDOG]] chồng nhau.
- [ ] Giá ở đúng [[27 - Premium Discount|premium/discount]] cho hướng vào.
- [ ] Tiếp cận POI trong [[18 - Kill Zones]].
- [ ] [[20 - Liquidity Sweep]] rõ ngay trước MSS.
- [ ] Có cả [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL]] (target gần) và **ERL** (target xa) để quản lý TP.

### Điều kiện làm quy trình yếu đi (warning)
- Bias HTF mơ hồ / vừa mới đổi chưa xác nhận.
- Bỏ qua tầng Intermediate, nhảy thẳng HTF → LTF.
- Mở quá nhiều khung gây phân vân (analysis paralysis).
- Giá chưa tới POI nhưng đã "thấy" entry trên LTF.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 3 tầng bắt buộc — đây là TRÁI TIM của khái niệm này
> Đi tuần tự **CAO → THẤP**. Mỗi tầng phải PASS mới được xuống tầng kế tiếp. Tầng nào FAIL → dừng, **không có lệnh**.
> 1. **HTF — BIAS & DRAW:** Bias là gì? Draw on liquidity ở đâu? Premium hay discount?
> 2. **INTERMEDIATE — POI & RANGE:** Giá sẽ phản ứng ở POI nào? Dealing range + IRL/ERL?
> 3. **LTF — ENTRY & TIMING:** Giá đã tới POI trong kill zone chưa? Có sweep → MSS → FVG để vào không?

### Bước 1 — HTF (MN / W1 / D1): Bias & Narrative
1. Xác định [[12 - Daily Bias]]: bullish / bearish / neutral. Viết thành một câu.
2. Xác định **Draw on Liquidity (DOL)** — giá đang bị hút về buyside hay sellside, mốc [level] nào?
3. Định vị giá trong [[12 - Dealing Range]] HTF: đang [[27 - Premium Discount|premium hay discount]]?
4. Đánh dấu các PD-array & liquidity pool HTF lớn (OB/FVG/NWOG/old highs-lows).
5. **Gate:** Nếu bias mơ hồ hoặc không có DOL → **dừng**, đứng ngoài.

### Bước 2 — Intermediate (H4 / H1): POI & Context
1. Khoanh **POI cụ thể** mà giá có khả năng phản ứng (OB, FVG, breaker, NWOG/NDOG CE).
2. Đánh dấu [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL (target gần) & ERL (target xa)]].
3. Refine bias: cấu trúc Intermediate có ủng hộ bias HTF không?
4. Xác minh POI nằm đúng [[27 - Premium Discount|premium/discount]] cho hướng vào.
5. **Gate:** Không có POI cụ thể hoặc POI sai P/D → **dừng**, chờ giá tới vùng tốt hơn.

### Bước 3 — LTF (M15 / M5 / M1): Confirmation & Entry
1. Chờ giá **thực sự chạm POI** đã khoanh, **trong [[18 - Kill Zones]]**.
2. Quan sát [[20 - Liquidity Sweep]] quét pool ngay tại/cạnh POI.
3. Chờ [[21 - Market Structure Shift]] (MSS) đúng hướng bias HTF (hoặc [[Break of Structure|BOS]] nếu tiếp diễn).
4. Tinh chỉnh entry vào [[Fair Value Gap|FVG]]/[[Order Block|OB]] hình thành sau displacement; cân nhắc [[26 - OTE - Optimal Trade Entry|OTE]].
5. SL ngoài điểm sweep / ngoài POI; TP1 = IRL, TP2 = ERL/DOL.
6. **Gate:** Không có sweep/MSS trong POI, hoặc trigger giữa range → **không có lệnh**.

```text
[LONG SETUP — top-down đồng thuận, discount → bullish]
- HTF (D1): bias bullish; giá ở discount; DOL = buyside [level] phía trên
- Intermediate (H1): POI = bullish OB/FVG ở discount [range]; ERL target [level]
- LTF (M5): giá chạm POI trong NY KZ → quét sellside → MSS lên + FVG bullish
- Entry: ____ (FVG/OB hoặc OTE)   SL: dưới điểm sweep / dưới POI [level]
- TP1: IRL [level]   TP2: ERL / DOL buyside [level]
- RR dự kiến: ____
- Đồng thuận 3 tầng? ✓ / ✗
```

```text
[SHORT SETUP — top-down đồng thuận, premium → bearish]
- HTF (D1): bias bearish; giá ở premium; DOL = sellside [level] phía dưới
- Intermediate (H1): POI = bearish OB/FVG ở premium [range]; ERL target [level]
- LTF (M5): giá chạm POI trong London KZ → quét buyside → MSS xuống + FVG bearish
- Entry: ____ (FVG/OB hoặc OTE)   SL: trên điểm sweep / trên POI [level]
- TP1: IRL [level]   TP2: ERL / DOL sellside [level]
- RR dự kiến: ____
- Đồng thuận 3 tầng? ✓ / ✗
```

> [!warning]
> **Top-down không phải lý do để "đoán" entry trước khi giá tới POI.** Bias HTF đúng nhưng giá chưa chạm POI Intermediate thì vẫn **chưa có lệnh** — đó chỉ là một kế hoạch chờ. Vào sớm "vì chắc chắn nó sẽ lên" là bỏ qua đúng tầng quan trọng nhất: timing trên LTF.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Quy trình được xem là hợp lệ khi (✓)
- [ ] Bias HTF rõ + có draw on liquidity xác định.
- [ ] POI Intermediate cụ thể, đúng premium/discount.
- [ ] Giá đã tới POI **trong kill zone**.
- [ ] Có [[20 - Liquidity Sweep]] + [[21 - Market Structure Shift]] LTF đúng hướng bias.
- [ ] Có entry array (FVG/OB/OTE), SL logic, RR đạt kế hoạch.
- [ ] **Ba tầng đồng thuận** một câu chuyện.

### Quy trình bị vô hiệu khi (✗)
- [ ] Giá **phá hẳn POI HTF** mà không phản ứng → narrative sai, hủy kế hoạch.
- [ ] MSS xảy ra **giữa range**, không nằm trong POI.
- [ ] Setup LTF **ngược bias HTF** mà không có lý do HTF đủ mạnh.
- [ ] Tiếp cận ngoài kill zone / news lớn override.
- [ ] Khung thấp đẹp nhưng khung cao mâu thuẫn → ưu tiên HTF, bỏ lệnh.

| Tiêu chí | Giữ kế hoạch (hợp lệ) | Hủy kế hoạch (vô hiệu) |
|---|---|---|
| Bias HTF | Rõ + có DOL | Mơ hồ / vừa đổi chưa xác nhận |
| Phản ứng tại POI | Reject + sweep rõ | Đóng nến xuyên qua, không phản ứng |
| Vị trí MSS | Trong POI | Giữa range |
| Đồng thuận khung | Ba tầng cùng hướng | LTF ngược HTF |
| Thời điểm | Trong kill zone | Ngoài KZ / news |

> [!note]
> Khi LTF và HTF mâu thuẫn, **HTF luôn thắng**. Một MSS đẹp trên M5 ngược với bias Daily thường chỉ là một pullback nội bộ — không phải tín hiệu đảo chiều. Quy tắc một dòng: *"Khung cao quyết định hướng, khung thấp quyết định thời điểm."*

### Nâng cao — Xử lý độ trễ giữa các tầng: khi HTF vừa đổi bias nhưng Intermediate/LTF chưa "bắt kịp"

Trong sách vở, ba tầng đồng thuận nghe như một sự kiện tức thời: HTF đổi bias, Intermediate lập tức có POI mới, LTF lập tức phản ứng đúng hướng. Thực tế trên chart sống không như vậy — có một **cửa sổ trễ (lag window)** giữa lúc HTF vừa flip và lúc các tầng thấp hơn thực sự "bắt kịp". Đây là nơi rất nhiều lệnh xấu được sinh ra: trader thấy một MSS HTF (ví dụ Daily) vừa xảy ra, lập tức coi bias đã đổi hoàn toàn, rồi vội xuống LTF săn entry theo hướng mới trong khi Intermediate còn chưa hình thành nổi một POI sạch và LTF vẫn đang hiển thị cấu trúc của hướng CŨ.

Vấn đề gốc rễ: một MSS HTF chỉ xác nhận rằng **cấu trúc đã bị phá**, không đảm bảo rằng toàn bộ delivery đã đảo ngay lập tức. Thường có một giai đoạn chuyển tiếp — có thể vài giờ đến vài phiên — nơi Intermediate vẫn đang "tiêu hóa" cú phá cấu trúc đó: tạo pullback, test lại vùng cũ, rồi mới thực sự để lại một OB/FVG sạch theo hướng mới. Nếu vào lệnh LTF theo hướng mới trước khi Intermediate xác nhận, bạn đang giao dịch một bias vẫn còn **tentative** (tạm thời, chưa chắc chắn), không phải một bias đã được cả ba tầng đồng thuận.

Cách xử lý:
- **Coi bias HTF vừa flip là "tentative" cho tới khi Intermediate tự xác nhận** bằng cấu trúc riêng của nó (một MSS/BOS nội bộ trên H4/H1 cùng hướng, hoặc một POI mới hình thành đúng vị trí premium/discount cho hướng đó).
- **Không rush entry LTF theo hướng mới trước khi Intermediate bắt kịp.** Một MSS đẹp trên M5 ngay sau khi Daily vừa đổi bias thường chỉ là phản ứng nhiễu loạn ngắn hạn, chưa phải một nhịp có cấu trúc Intermediate đứng sau.
- **Giảm size hoặc đứng ngoài trong toàn bộ cửa sổ chuyển tiếp.** Nếu buộc phải vào (ví dụ đã có sweep + MSS LTF hấp dẫn), coi đây là một lệnh "thăm dò" với risk nhỏ hơn mức chuẩn, không phải một lệnh full-conviction.

![[TopDown-Advanced-Lag-States.svg|697]]
*Timeline ba tầng: HTF flip trước (①), Intermediate xác nhận sau một khoảng trễ (②), LTF xác nhận cuối cùng (③). Vùng giữa ① và ③ là "vùng nguy hiểm" — LTF có thể vẫn còn cấu trúc hướng cũ trong khi HTF đã đổi; đây là nơi cần giảm size hoặc đứng ngoài.*

| Trạng thái | HTF flip | Intermediate xác nhận | LTF xác nhận | Hành động |
|---|---|---|---|---|
| 1 | ✓ | ✗ | ✗ | Bias tentative — chỉ theo dõi, KHÔNG vào lệnh |
| 2 | ✓ | ✓ | ✗ | Intermediate đã có POI mới — chuẩn bị, chờ LTF, size chuẩn khi có |
| 3 | ✓ | ✗ | ✓ (trông "đẹp") | Cảnh báo: LTF có thể là nhiễu loạn ngắn hạn — size nhỏ hoặc bỏ |
| 4 | ✓ | ✓ | ✓ | Đồng thuận đầy đủ — vào lệnh với size chuẩn |

> [!tip]
> Ghi lại trong journal khoảng thời gian (số nến H1/H4) giữa lúc HTF MSS xảy ra và lúc Intermediate thực sự để lại một POI sạch. Sau vài chục lần quan sát, bạn sẽ có cảm giác định lượng về "độ trễ trung bình" của cặp khung mình hay dùng — thay vì đoán mò mỗi lần.

### Nâng cao — Top-down theo thời gian (session/AMD cycle), không chỉ theo giá

Top-down Analysis thường được dạy thuần theo trục **giá** (bias → POI → entry) nhưng bỏ sót một trục quan trọng không kém: **thời gian**. Biết giá đang ở đâu trong narrative HTF — ví dụ giá đã chạm đúng POI Intermediate — không tự động có nghĩa là ĐÃ ĐẾN LÚC xuống LTF tìm trigger. Thị trường vận hành theo chu kỳ nội phiên **AMD (Accumulation – Manipulation – Distribution)**: tích lũy đi ngang, sau đó bị thao túng (thường là một sweep thanh khoản), rồi mới phân phối theo hướng thật.

Nếu giá chạm đúng POI HTF nhưng đang ở pha **Accumulation** (thường là phiên Á hoặc đầu phiên, thanh khoản mỏng, giá đi ngang hẹp), thì bất kỳ "MSS" nào xuất hiện lúc đó có xác suất cao chỉ là nhiễu nội phiên — không đủ thanh khoản đằng sau để tạo một displacement thật. Ngược lại, khi giá bước vào pha **Manipulation** — thường trùng với đầu [[18 - Kill Zones|Kill Zone]] London hoặc New York — đây là lúc thị trường thực sự "quét" thanh khoản (liquidity sweep) trước khi phân phối theo hướng đúng. Một sweep + MSS xảy ra trong đúng cửa sổ Manipulation có độ tin cậy cao hơn hẳn cùng một mẫu hình xảy ra giữa lúc Accumulation.

Nguyên tắc thực hành:
- **Đừng bắt đầu săn trigger LTF chỉ vì giá đã ở đúng vị trí (POI).** Luôn hỏi thêm: hiện tại đang ở pha nào của chu kỳ AMD trong phiên?
- **Trong pha Accumulation, chuyển sang chế độ chờ, không phải chế độ săn entry** — dù giá đang nằm đẹp tại POI HTF/Intermediate. Đánh dấu vùng, rồi chờ.
- **Ưu tiên tìm sweep → MSS trong pha Manipulation**, gần như luôn trùng khung giờ [[18 - Kill Zones]] (London Open, NY AM). Đây là lúc "câu chuyện về giá" (top-down) và "câu chuyện về thời gian" (AMD) gặp nhau.
- **Pha Distribution là lúc quản lý lệnh đã vào**, không phải lúc tìm entry mới — nếu bạn mới thấy tín hiệu ở giữa/cuối Distribution, phần lớn move ngon đã đi qua.

![[TopDown-Advanced-Session-AMD-Timing.svg|697]]
*Timeline phiên Á/London/NY với các pha AMD bên dưới. Điểm ① giá chạm HTF POI trong Accumulation → quá sớm, chưa có thanh khoản để tạo sweep thật, nên đứng ngoài chờ. Điểm ② sweep thật xảy ra trong Manipulation (trùng Kill Zone) → đây mới là cửa sổ hợp lệ để tìm MSS và entry.*

### Nâng cao — Khi nào được phép rút gọn còn 2 tầng thay vì 3, và rủi ro đi kèm

Khung 3 tầng (HTF/Intermediate/LTF) là chuẩn mực vì nó tối đa hoá confluence, nhưng nó cũng chậm hơn. Một số trader scalping cực ngắn hạn hợp thức hóa việc **rút gọn còn 2 tầng** — ví dụ gộp bias và POI vào cùng một khung H1 (bias + POI trên H1), rồi xuống thẳng M1 để tìm entry — nhằm phản ứng nhanh hơn với các cơ hội trong phiên, đặc biệt khi trade một cặp khung/instrument đã cực kỳ quen thuộc.

Đánh đổi cần hiểu rõ trước khi làm việc này:
- **Tốc độ phản ứng tăng, nhưng bộ lọc confluence giảm.** Khi bỏ bớt một tầng, số lượng tín hiệu "đủ điều kiện xem xét" tăng lên (raw signal count cao hơn) vì bạn không còn yêu cầu một POI Intermediate riêng biệt xác nhận. Nhưng đồng thời **win-rate trên mỗi tín hiệu thường giảm**, vì chính tầng Intermediate là bộ lọc đã loại bỏ phần lớn setup yếu trong khung 3 tầng chuẩn.
- **Rủi ro lớn nhất: nhầm nhiễu HTF thành một nhịp di chuyển thật.** Không có tầng Intermediate làm "trạm trung chuyển" để xác nhận cấu trúc, một biến động ngẫu nhiên trên H1 (nhiễu quanh vùng POI) dễ bị đọc nhầm thành một cú di chuyển có ý nghĩa, dẫn tới entry M1 vội vàng theo một tín hiệu chưa được lọc kỹ.
- **Quy tắc kinh nghiệm cho khi nào 2 tầng là chấp nhận được:** chỉ dành cho trader đã có kinh nghiệm và **đã backtest sâu trên đúng một instrument/session cụ thể** (ví dụ chỉ NQ1 trong NY AM Kill Zone), nơi họ đã có đủ dữ liệu để biết loại nhiễu H1 nào là an toàn để bỏ qua tầng lọc Intermediate. Người mới đang xây pattern recognition **không nên** rút gọn — thiếu tầng Intermediate ở giai đoạn này đồng nghĩa với việc không có đủ dữ liệu để phân biệt tín hiệu thật với nhiễu.

| Tiêu chí | Khung 3 tầng (chuẩn) | Khung 2 tầng (rút gọn) |
|---|---|---|
| Tốc độ phản ứng | Chậm hơn | Nhanh hơn |
| Số tín hiệu đủ điều kiện | Ít hơn (đã lọc qua Intermediate) | Nhiều hơn (raw signal cao) |
| Win-rate trên mỗi tín hiệu | Cao hơn (nhiều confluence) | Thấp hơn (ít bộ lọc) |
| Rủi ro nhầm nhiễu HTF thành move thật | Thấp hơn | Cao hơn |
| Phù hợp với | Người mới, hầu hết trường hợp | Trader dày dạn, đã backtest sâu 1 instrument/session |

> [!warning]
> Rút gọn còn 2 tầng KHÔNG phải "nâng cấp" — nó là một sự đánh đổi tốc độ lấy confluence, chỉ hợp lý khi đã có bằng chứng backtest (tối thiểu vài chục mẫu) cho thấy cặp khung rút gọn vẫn giữ được edge trên chính instrument/session bạn giao dịch. Nếu chưa có dữ liệu đó, hãy giữ nguyên khung 3 tầng.

---

## 6. Ví dụ chart

### Ví dụ đúng — Ba tầng đồng thuận
![[TopDown-Example-Correct.svg|697]]

**Mô tả:**
- **HTF (D1):** giá ở discount, bias bullish, DOL = buyside [level] phía trên (chưa lấy).
- **Intermediate (H1):** POI = bullish OB ở discount [range], trùng một FVG; ERL target rõ.
- **LTF (M5):** trong NY KZ, giá chạm POI, quét sellside, MSS lên + FVG bullish; entry tại FVG, SL dưới sweep.

**Vì sao đây là ví dụ tốt:**
- Phân tích đi đúng chiều CAO → THẤP, không bỏ tầng Intermediate.
- Entry chỉ thực hiện **sau khi giá tới POI** và có xác nhận LTF — không đoán sớm.
- Ba tầng cùng kể một câu chuyện (discount → bullish → long), trong kill zone.
- Target là liquidity rõ (IRL rồi ERL/DOL).

### Ví dụ sai / dễ nhầm — Bottom-up, LTF ngược HTF
![[TopDown-Example-Wrong.svg|697]]

**Mô tả lỗi:**
- Trader thấy một MSS đẹp trên M1 và vào long **mà chưa hề kiểm tra Daily**.
- Daily thực ra đang bearish, giá đang ở **premium** và draw xuống sellside.
- "Setup M1 đẹp" chỉ là một pullback bên trong nhịp giảm HTF; giá tiếp tục xuống, SL bị quét.

**Bài học:**
- Bắt đầu từ LTF rồi ép câu chuyện lên HTF = sai chiều gốc rễ.
- Một entry LTF đẹp **ngược bias HTF** là cái bẫy, không phải cơ hội.
- Luôn xác định bias + draw HTF **trước**, rồi mới xuống tìm entry.
- Bỏ tầng Intermediate (POI) khiến entry "lơ lửng" giữa range.

### Giải phẫu phân cấp khung
![[TopDown-Anatomy.svg|697]]

**Mô tả:** Sơ đồ chú thích ba tầng HTF → Intermediate → LTF, với câu hỏi tương ứng từng tầng (Bias/Draw → POI/Range → Entry/Timing) và mũi tên đồng thuận xuyên suốt.

---

## 7. Entry model liên quan

Khái niệm này là **bộ khung chứa** các entry model sau:
- [[ICT 2022 Model]] — hiện thân trực tiếp của top-down: bias → POI → sweep → MSS → FVG entry.
- [[12 - Daily Bias]] — sản phẩm của tầng HTF.
- [[27 - Premium Discount]] / [[12 - Dealing Range]] — định vị giá ở mỗi tầng.
- [[19 - Liquidity]] / [[16 - Internal & External Range Liquidity (IRL & ERL)]] — draw & target.
- [[20 - Liquidity Sweep]] → [[21 - Market Structure Shift]] / [[Break of Structure]] — trigger LTF.
- [[Fair Value Gap]] / [[Order Block]] / [[26 - OTE - Optimal Trade Entry]] — entry array tầng LTF.
- [[18 - Kill Zones]] — timing cho tầng LTF.
- [[24 - New Week Opening Gap]] / [[23 - New Day Opening Gap]] — POI/draw thường dùng ở tầng HTF/Intermediate.

### Sequence mẫu — chuỗi top-down chuẩn
```text
HTF (D1): Daily Bias + Draw on Liquidity + Premium/Discount
  → Intermediate (H1): khoanh POI (OB/FVG/NWOG CE) + IRL/ERL
    → LTF (M5/M1): giá tới POI trong Kill Zone
      → Liquidity Sweep → Market Structure Shift → Displacement
        → FVG/OB/OTE Entry  | SL ngoài sweep
          → TP1 = IRL  →  TP2 = ERL / Draw on Liquidity
[Kiểm tra cuối: ba tầng có ĐỒNG THUẬN không? Nếu không → No Trade]
```

> [!note]
> Top-down Analysis hoạt động mạnh nhất khi nó là **xương sống của [[ICT 2022 Model]]** — không phải một bước rời rạc. Mỗi thành phần của ICT 2022 (sweep, MSS, FVG) thực ra sống ở một tầng khung cụ thể; top-down chỉ là cách sắp xếp chúng đúng thứ tự.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không có đủ A + B + đồng thuận → KHÔNG có lệnh
> Top-down là kỷ luật, không phải gợi ý. Một tầng FAIL là cả quy trình FAIL.

### A. Context (HTF + Intermediate)
- [ ] [[12 - Daily Bias]] rõ ràng: `Bullish / Bearish`.
- [ ] Draw on liquidity (DOL) xác định: [level].
- [ ] Giá ở [[27 - Premium Discount|premium/discount]] phù hợp hướng trade.
- [ ] POI Intermediate cụ thể đã khoanh (đúng P/D).
- [ ] IRL/ERL làm target đã đánh dấu.

### B. Execution (LTF)
- [ ] Giá đã **thực sự tới POI** trong [[18 - Kill Zones]].
- [ ] Có [[20 - Liquidity Sweep]] tại/cạnh POI.
- [ ] Có [[21 - Market Structure Shift]] LTF đúng hướng bias.
- [ ] Có entry array (FVG/OB/OTE), SL ngoài sweep, RR ≥ ngưỡng.
- [ ] Risk ≤ 0.5% theo khung rủi ro.

### C. Đồng thuận & "không có lệnh"
- [ ] Ba tầng (HTF/Intermediate/LTF) **cùng kể một câu chuyện**.
- [ ] KHÔNG vào nếu LTF ngược bias HTF.
- [ ] KHÔNG vào nếu giá chưa tới POI / MSS giữa range.
- [ ] KHÔNG vào ngoài kill zone hoặc đang có news lớn.
- [ ] KHÔNG bỏ tầng Intermediate (nhảy HTF → LTF).

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Phân tích bottom-up | Bắt đầu từ M1/M5, ép story lên Daily | Sai chiều gốc; entry không có context | Luôn bắt đầu từ HTF, viết bias thành câu trước |
| Trade LTF ngược bias HTF | "M5 đẹp" nhưng Daily ngược | Vào ngược trend còn nguyên | Bỏ mọi setup LTF ngược bias HTF |
| Bỏ tầng Intermediate | Nhảy thẳng Daily → M1 | Entry lơ lửng giữa range, không POI | Luôn khoanh POI H4/H1 trước khi xuống LTF |
| Analysis paralysis | Mở 6–7 khung, không quyết được | Quá tải, bỏ lỡ timing | Chốt 1 bộ 3 khung gắn kết, tắt phần còn lại |
| Không định DOL trước | Xuống LTF khi chưa biết giá đi đâu | Không có target/lý do vào | Xác định draw on liquidity trước khi drill down |
| Bỏ qua thời gian (Kill Zone) | Chỉ nhìn giá, không nhìn giờ | Đúng giá sai giờ = xác suất thấp | Chỉ execute LTF trong London/NY KZ |
| Vào trước khi giá tới POI | "Chắc chắn nó sẽ lên" | Bỏ tầng timing, vào không xác nhận | Chờ giá chạm POI + sweep + MSS mới vào |
| Đổi bias liên tục theo LTF | Mỗi nến M1 lại đổi quan điểm | Mất neo HTF, giao dịch cảm tính | Khóa bias HTF cho cả phiên, chỉ refine không lật |

---

## 10. Câu hỏi tự kiểm tra
- Mình phân tích theo chiều nào — cao xuống thấp hay ngược lại?
- Bias HTF hiện tại là gì, và mình có viết được thành một câu không?
- Draw on liquidity của HTF nằm ở đâu?
- POI Intermediate cụ thể là gì, ở premium hay discount?
- Giá đã thực sự tới POI chưa, hay mình đang đoán?
- Setup LTF có đồng thuận với bias HTF không?
- Trigger LTF (sweep + MSS) có nằm trong POI và trong kill zone không?
- Nếu các khung mâu thuẫn, mình ưu tiên khung nào — và vì sao?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Top-down Analysis nghĩa là gì và đi theo chiều nào?
**Đáp:** Phân tích từ khung CAO xuống khung THẤP, sao cho mọi quyết định LTF nằm trong narrative HTF. Không bao giờ làm ngược lại.

### Q2
**Hỏi:** Ba tầng khung trả lời ba câu hỏi nào?
**Đáp:** HTF → Bias & Draw; Intermediate → POI & Range; LTF → Entry & Timing. (Bias → POI → Entry.)

### Q3
**Hỏi:** Khi LTF mâu thuẫn với HTF thì ưu tiên cái nào?
**Đáp:** HTF luôn thắng. Khung cao quyết định hướng, khung thấp quyết định thời điểm.

### Q4
**Hỏi:** Một bộ khung ICT-style điển hình cho day trading?
**Đáp:** D1 (bias) → H1/M15 (POI) → M5/M1 (entry); hoặc H4 → M15 → M1.

### Q5
**Hỏi:** Vì sao bỏ tầng Intermediate là lỗi nghiêm trọng?
**Đáp:** Vì entry sẽ "lơ lửng" giữa range, không gắn vào POI nào — mất chỗ phản ứng và mất stop logic.

### Q6
**Hỏi:** Phải xác định gì trên HTF trước khi được phép xuống LTF?
**Đáp:** Daily Bias + Draw on Liquidity + vị trí premium/discount. Thiếu draw thì không có lý do vào lệnh.

### Q7
**Hỏi:** Hai dấu hiệu cho thấy bạn đang làm sai (bottom-up)?
**Đáp:** (1) Bắt đầu từ M1/M5 rồi ép story lên Daily; (2) đổi bias liên tục theo từng nến LTF.

---

## 12. Liên kết với Trade Journal

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
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

---

## 13. Lesson Learned

> [!example] Ghi nhận khi áp dụng thực tế
> - Bối cảnh (cặp khung dùng): ____ → ____ → ____
> - Bias HTF & Draw on Liquidity: ____ / [level]
> - POI Intermediate: [range]
> - Trigger LTF (sweep/MSS/FVG): ____
> - Ba tầng có đồng thuận không? ✓ / ✗
> - Kết quả (R-multiple): ____
> - Điều làm đúng: ____
> - Điều cần sửa: ____
> - Liên kết tới [[Mistake - ...]] nếu có: ____

### Bài học chính
- Top-down là **quy trình**, không phải tín hiệu; nó tổ chức mọi khái niệm khác.
- HTF quyết định hướng, LTF quyết định thời điểm — không lẫn lộn.
- Phải có draw on liquidity trước khi drill down.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn phân tích CAO → THẤP, không bao giờ ngược lại.
- [ ] Tôi bỏ mọi setup LTF ngược bias HTF.
- [ ] Tôi không bỏ tầng Intermediate (POI) và không vào trước khi giá tới POI.

### Câu nhắc nhở khi trade
> **"Khung cao chọn hướng, khung thấp chọn thời điểm — entry chỉ là mảnh khớp cuối cùng của một câu chuyện đã viết xong từ Daily."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa & phân cấp khung |  | Có giải thích 3 tầng trong 30 giây không? |
| Phân tích đúng chiều (top-down) |  | Có bao giờ bị bottom-up không? |
| Xác định POI Intermediate |  | Có hay bỏ tầng này không? |
| Kỷ luật đồng thuận khung |  | Có dám bỏ LTF ngược HTF không? |
| Tích hợp vào [[ICT 2022 Model]] |  | Quy trình có liền mạch không? |
| Áp dụng vào trade thực tế |  | Kiểm tra bằng journal thay vì cảm tính? |

**Kế hoạch review tiếp theo:**
- [ ] Backtest 10–20 setup, ghi rõ ba tầng (HTF/Intermediate/LTF) cho từng cái trên NQ1/NAS100 & EURUSD.
- [ ] Mỗi phiên: viết bias HTF + DOL **trước khi** mở khung thấp.
- [ ] Thống kê win rate của setup "đồng thuận 3 tầng" vs "thiếu đồng thuận".
- [ ] Đối chiếu với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]].
- [ ] Review lại note này sau 2 tuần, cập nhật `confidence` & `last_reviewed`.

---

## Best Practices

> [!success] Nguyên tắc vàng
> **"Khung cao chọn hướng, khung thấp chọn thời điểm."** Trước khi mở bất kỳ khung thấp nào, phải viết được bias HTF + draw on liquidity thành MỘT câu rõ ràng; nếu không viết nổi câu đó, bạn chưa có quyền xuống LTF — mọi setup LTF đẹp mắt xuất hiện trước khi câu đó tồn tại đều là nhiễu, không phải cơ hội.

1. **Luôn viết bias HTF + draw on liquidity thành một câu tường minh trước khi mở khung thấp hơn.** Ví dụ: "Daily bullish, giá ở discount, draw lên buyside [level]." Nếu không thể diễn đạt được câu này một cách chắc chắn, đó là dấu hiệu bias chưa đủ rõ để hành động — đừng mở M5/M1 "để xem thử". Ghi câu này vào Daily Note trước phiên; nó là cơ sở để đối chiếu lại sau này khi review xem context ban đầu có đúng không.

2. **Không bao giờ bỏ qua tầng Intermediate/POI dù đang vội.** Nhảy thẳng từ HTF xuống LTF là lỗi phổ biến nhất trong mục 9 của note này, và nó khiến entry "lơ lửng" giữa range mà không gắn vào một POI cụ thể nào. Dù thị trường di chuyển nhanh, hãy dành ít nhất một khoảnh khắc khoanh vùng POI H4/H1 — thiếu bước này đồng nghĩa với thiếu cả điểm phản ứng lẫn logic đặt stop.

3. **Coi một bias HTF vừa mới flip là "tentative" cho tới khi Intermediate xác nhận bằng cấu trúc riêng của nó.** Như phân tích ở mục Nâng cao — Xử lý độ trễ giữa các tầng, có một cửa sổ trễ tự nhiên giữa lúc HTF đổi hướng và lúc các tầng thấp hơn "bắt kịp". Vào lệnh full-size ngay trong cửa sổ này là đặt cược vào một bias chưa được xác nhận đầy đủ.

4. **Kết hợp timing theo session/AMD với vị trí POI theo giá — đừng săn trigger LTF trong pha Accumulation.** Giá chạm đúng HTF POI không có nghĩa là "đến giờ" tìm entry; hãy xác định trước xem phiên đang ở pha Accumulation, Manipulation hay Distribution, và chỉ kỳ vọng một sweep + MSS hợp lệ khi bước vào Manipulation (thường trùng [[18 - Kill Zones]]).

5. **Chọn một bộ ba khung gắn kết cho mỗi phiên và không đổi giữa chừng.** Việc nhảy qua lại giữa nhiều tổ hợp khung (lúc dùng D1→H1→M5, lúc lại H4→M15→M1) trong cùng một phiên phân tích tạo ra analysis paralysis và khiến bias bị "làm mới" liên tục theo cảm tính LTF. Cố định một bộ khung trước khi bắt đầu, và chỉ đổi bộ khung ở đầu phiên mới.

6. **Chấp nhận rằng phần lớn tín hiệu LTF sẽ bị lọc bỏ vì mâu thuẫn với HTF — đó là hệ thống đang hoạt động đúng, không phải cơ hội bị bỏ lỡ.** Cảm giác tiếc nuối khi thấy một MSS M5 đẹp bị loại vì ngược bias Daily là bình thường, nhưng hành động theo cảm giác đó chính là cách hầu hết lệnh thua "context sai" được tạo ra. Ghi vào journal cả những setup LTF bị bỏ vì lý do này — không chỉ những lệnh đã vào — để nhìn thấy giá trị thực của bộ lọc.

7. **Chỉ rút gọn còn khung 2 tầng sau khi đã có kinh nghiệm backtest đáng kể trên một instrument/session cụ thể.** Như đã phân tích ở mục Nâng cao tương ứng, rút gọn tầng đổi lấy tốc độ bằng việc giảm confluence và tăng nguy cơ nhầm nhiễu HTF thành move thật. Người mới còn đang xây dựng pattern recognition nên luôn giữ đủ 3 tầng; chỉ cân nhắc 2 tầng sau khi có tối thiểu vài chục mẫu backtest chứng minh cặp khung rút gọn vẫn giữ được edge.

8. **Ghi lại chính xác tầng nào đã "giết chết" một setup tưởng như tốt, để xây dựng hồ sơ cá nhân về sức mạnh bộ lọc của top-down.** Mỗi khi một ý tưởng trade bị loại (ví dụ: "POI Intermediate đẹp nhưng HTF bias ngược" hoặc "LTF có MSS nhưng giá chưa từng tới POI"), gắn nhãn rõ tầng gây loại bỏ đó trong journal. Sau 30–50 lần ghi nhận, bạn sẽ có dữ liệu định lượng cho thấy tầng nào lọc nhiều nhất và học được cách nhận diện sớm hơn — biến top-down từ một quy trình trừu tượng thành một kỹ năng đo lường được, liên kết trực tiếp với [[02 - Skill Metrics]].