---
type: ict-concept
concept: ICT 2022 Model - LTF Intraday (H1-M5-M1)
aliases:
  - ICT 2022 LTF
  - ICT 2022 Intraday
  - 2022 Model H1-M5-M1
  - ICT 2022 Lower Timeframe
tags:
  - trading/ict/concept
  - trading/study
  - "#ICT2022"
  - "#LTF"
status: seed
category: Entry Model
last_reviewed: 2026-07-12
created: 2026-07-12
updated: 2026-07-12
---

# ICT 2022 Model — LTF Intraday (H1 → M5 → M1)

> [!summary] Tóm tắt 1 câu
> **Đây KHÔNG phải một mô hình mới — đây là chính [[01 - ICT 2022 Model]] được "hạ khung" xuống một tầng: bias/draw chuyển từ D1 sang H1(–H4), POI/sweep/MSS chuyển từ H1 sang M5, và entry refine chuyển từ M5 sang M1. Chuỗi 7 bước giữ nguyên; chỉ có tốc độ, tần suất và chi phí thực thi thay đổi.**

> [!important] Nguyên tắc cốt lõi của biến thể này
> **Hạ khung KHÔNG có nghĩa là bỏ HTF.** Vấn đề "chờ lâu để giá retrace về H1 POI" được giải quyết bằng cách coi H1 là *bias/context* và để M5 sinh setup — chứ KHÔNG phải bằng cách vào lệnh trên M5/M1 mà không có neo HTF. Một M5 MSS không có H1 draw phía sau chỉ là **noise**. Đây là ranh giới sống–còn của biến thể LTF: bạn đổi "chờ lâu" lấy "nhiều setup hơn", và cái giá phải trả là **nhiễu nhiều hơn + chi phí giao dịch nặng hơn tương đối + rủi ro overtrading**.

---

## 0. Vì sao cần biến thể này — vấn đề gốc & sự đánh đổi

Khung gốc của bạn là **D1 → H1 → M5**. Nút thắt: sau khi có bias D1 và đánh dấu H1 POI, **giá có thể mất nhiều giờ đến vài ngày** mới retrace về đúng H1 FVG/OB. Với người có công việc chính (Amaris) và chỉ ngồi máy được vài khung giờ cố định, điều này khiến bạn **bỏ lỡ setup** hoặc **ngồi chờ mỏi mòn** rồi vào ẩu ngoài kế hoạch.

Biến thể **H1 → M5 → M1** giải quyết đúng nút thắt đó — nhưng phải hiểu rõ mình đang đánh đổi cái gì:

| Tiêu chí | Gốc D1→H1→M5 | Biến thể H1→M5→M1 |
|---|---|---|
| Thời gian chờ retrace về POI | Hàng giờ → vài ngày | Vài phút → 1–2 giờ |
| Số setup A+ mỗi tuần | Ít (chọn lọc cao) | Nhiều hơn hẳn (mỗi phiên có thể 1–3) |
| Độ nhiễu / false signal | Thấp (HTF lọc sẵn) | **Cao** — M5 có nhiều MSS giả |
| Chi phí spread/commission so với target | Không đáng kể | **Đáng kể** — target nhỏ, phí ăn mòn R |
| Yêu cầu thời gian ngồi máy | Có thể set-and-forget | **Phải có mặt** trong killzone |
| Rủi ro tâm lý (overtrade, revenge) | Thấp | **Cao** — nhiều nút bấm hơn |
| Độ khó backtest hợp lệ | Vừa | **Khó hơn** — dễ curve-fit vì nhiều data point |

> [!warning] Sự thật khó nghe (vai trò mentor)
> Phần lớn trader ICT **cháy tài khoản ở khung thấp**, không phải khung cao. Lý do không phải vì mô hình sai, mà vì hạ khung khuếch đại đúng những điểm yếu kỷ luật của bạn: bạn thấy nhiều "cơ hội" hơn → bấm nhiều hơn → phí + slippage + sai lầm cộng dồn nhanh hơn. Biến thể này chỉ đáng theo **NẾU** kỷ luật killzone và luật "no sweep = no trade" của bạn đã vững ở khung gốc. Nếu ở D1→H1→M5 bạn còn hay chase hoặc bỏ bước sweep, hạ khung sẽ làm vỡ tài khoản nhanh gấp bội. Hãy để **dữ liệu backtest riêng của biến thể này** quyết định, đừng giả định thống kê từ khung gốc chuyển sang được.

---

## 1. Định nghĩa — bản đồ fractal "hạ một tầng"

![[ICT2022-LTF-Fractal-Shift-Diagram.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ 2 cột song song thể hiện phép "dịch một tầng khung thời gian". Cột trái ghi mô hình GỐC: 3 khối chồng dọc **D1 (Bias/Draw) → H1 (POI/Sweep/MSS) → M5 (Entry refine)**. Cột phải ghi BIẾN THỂ LTF: 3 khối tương ứng **H1/H4 (Bias/Draw) → M5 (POI/Sweep/MSS) → M1 (Entry refine)**. Dùng mũi tên chéo nối từng tầng cột trái sang đúng vai trò tầng cột phải (D1→H1, H1→M5, M5→M1) để nhấn mạnh "cùng vai trò, khác khung". Ghi chú nền: "Cùng 7 bước — chỉ trượt thang khung thời gian xuống một nấc". Đây là sơ đồ khái niệm, không phải chart giá thật.

**Khái niệm:**
ICT 2022 Model là mô hình **fractal** — cùng một logic "smart money" (quét thanh khoản → displacement để lại imbalance → retrace → chạy về pool đối diện) lặp lại ở *mọi* thang khung thời gian (xem [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]]). Vì vậy ta có thể **trượt toàn bộ bộ ba khung xuống một nấc** mà không đổi bản chất mô hình:

| Vai trò | Khung gốc | Khung biến thể LTF | Nhiệm vụ tại tầng đó |
|---|---|---|---|
| **Bias & Draw on liquidity** | D1 | **H1** (soi kèm H4 để không ngược trend lớn) | Xác định hướng + pool HTF là target cuối |
| **POI · Sweep · Displacement/MSS** | H1 | **M5** | Đánh dấu pool sẽ bị quét, chờ sweep + M5 displacement để lại FVG |
| **Confirmation & Entry refine** | M5 | **M1** | Refine điểm vào quanh CE/OTE, tối ưu stop; **không** dùng M1 làm động cơ mô hình |

> [!important] Quy tắc "một tầng bias, không nhảy cóc"
> Bias luôn nằm ở tầng **cao hơn setup đúng một–hai nấc**, không nhiều hơn. Ở biến thể này H1 là bias chính; H4 chỉ dùng để *kiểm tra không giao dịch ngược trend H4* (một bộ lọc, không phải nguồn setup). Nếu bạn để D1 làm bias rồi cố entry trên M1, bạn đang nhảy 3–4 tầng — khoảng cách quá lớn khiến M1 noise nuốt mất tín hiệu, đúng vấn đề [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]] cảnh báo.

**Chuỗi 7 bước — giữ nguyên, chỉ đổi khung:**
1. **Bias (H1, lọc H4):** Bullish / Bearish — xem [[12 - Daily Bias]]. Trên intraday, "bias" nghĩa là hướng của nhịp H1 hiện tại trong dealing range H1/H4.
2. **Draw on liquidity (H1):** pool H1 mà giá đang bị hút về (session high/low, equal highs/lows H1, PDH/PDL) — target cuối. Xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]].
3. **Liquidity Sweep (M5):** chờ M5 quét một pool (đáy/đỉnh M5, Asian range, session liquidity) + reclaim — trigger. Xem [[20 - Liquidity Sweep]].
4. **Displacement + MSS (M5):** một move M5 dứt khoát phá cấu trúc M5 theo hướng bias H1, **để lại M5 FVG**. Xem [[21 - Market Structure Shift]].
5. **FVG/POI (M5):** xác định M5 FVG + CE. Xem [[13 - FVG  - Fair Value Gap]].
6. **Entry (M1 refine):** vào khi giá retrace về M5 FVG; dùng M1 để bấm quanh CE / M1 FVG bên trong, hoặc chờ một M1 MSS xác nhận nếu muốn thêm confirmation.
7. **Target (H1):** pool H1 đối diện — internal M5 trước, external H1 sau.

**Bản chất không đổi:** vẫn là "Quét → Đẩy → Lùi → Vào → Chạy". Cái mới duy nhất là bạn đang đọc chu kỳ này ở **tầng AMD nhỏ hơn** — chính là các tầng Hourly-AMD và M5-AMD lồng bên trong Daily-AMD đã mô tả ở mục "Nested AMD" của [[01 - ICT 2022 Model]].

### Biến thể LTF KHÔNG phải là gì
- Không phải "cứ thấy M5 FVG là vào" — vẫn cần H1 bias + M5 sweep trước.
- Không phải cái cớ để **bỏ HTF context** — H1 draw là bắt buộc.
- Không phải scalp vô tội vạ ngoài killzone — ngoài killzone, M5 gần như thuần noise.
- Không phải "vào bằng M1 MSS đơn lẻ" — M1 chỉ để refine, động cơ mô hình là M5 displacement.
- Không phải mô hình có thống kê giống hệt khung gốc — **phải backtest lại từ đầu**.

---

## 2. Bối cảnh sử dụng — killzone là điều kiện GATE, không phải tùy chọn

> [!important] Trên khung thấp, timing chuyển từ "tăng xác suất" thành "bắt buộc"
> Ở khung gốc D1→H1→M5, giao dịch ngoài killzone chỉ *giảm* xác suất. Ở H1→M5→M1, giao dịch ngoài killzone gần như **chắc chắn là giao dịch với noise** — vì khi không có dòng lệnh tổ chức, M5/M1 chỉ phản ánh spread, thanh khoản mỏng và thuật toán "giữ giá". Vì vậy với biến thể này, **"đang trong killzone/macro" là một điều kiện GATE (pass/fail), không phải điểm cộng.**

### Killzone & Macro áp dụng cho biến thể (giờ ET → quy đổi VN UTC+7)

| Cửa sổ (ET) | Vai trò | NQ1/NAS100 | EURUSD/GBPUSD | Giờ VN (EDT hè / EST đông) |
|---|---|---|---|---|
| 02:33–03:00 | London 1 | — | Sweep Asian range, nhịp London đầu | 13:33 / 14:33 |
| 04:03–04:30 | London 2 (xác suất cao) | — | **Nhịp London chính (FX)** | 15:03 / 16:03 |
| 08:50–09:10 | NY AM 1 | Quanh tin 08:30, cẩn trọng slippage | Quanh tin USD | 19:50 / 20:50 |
| **09:50–10:10** | **NY AM 2 — lõi Silver Bullet** | **Cửa sổ vàng NQ1** | Tốt cho FX giờ overlap | 20:50 / 21:50 |
| 10:50–11:10 | NY AM 3 | Continuation sau SB | Continuation | 21:50 / 22:50 |

> [!info] Nhớ trừ DST
> Mỹ dùng **EDT (mùa hè)**: 10:00 ET ≈ **21:00 VN**. Mỹ dùng **EST (mùa đông)**: 10:00 ET ≈ **22:00 VN**. Chi tiết: [[40 - Macro Times]], [[18 - Kill Zones]].

### Cửa sổ thực dụng cho lịch của bạn (làm ở Amaris)
- **FX (EURUSD/GBPUSD):** khung **London (13:00–16:00 VN mùa hè)** là hợp lý nhất nếu bạn rảnh đầu giờ chiều; đây là lúc FX cho sweep "sạch" nhờ thanh khoản sâu.
- **NQ1 & FX overlap:** khung **NY AM (20:30–23:00 VN mùa hè)** — đặc biệt macro 09:50–10:10 ET — là cửa sổ chất lượng nhất cho NQ1. Nếu chỉ chọn được một khung để đánh biến thể LTF, **chọn NY AM**.
- **Tránh hoàn toàn giờ Á (sáng VN):** thanh khoản mỏng, M5 sweep giả liên tục, EURUSD↔GBPUSD SMT không đáng tin.

### Khi nào biến thể này có giá trị cao?
- [ ] Bias H1 rõ ràng, có draw on liquidity H1 cụ thể (không "neutral").
- [ ] Đang trong London Open hoặc NY AM killzone (bắt buộc).
- [ ] Có M5 liquidity sweep rõ + reclaim trước displacement.
- [ ] M5 displacement phá cấu trúc M5 và để lại FVG sạch.
- [ ] M5 FVG ở đúng premium/discount của dealing range H1, đồng hướng bias.
- [ ] H4 không ngược chiều gay gắt (bộ lọc trend lớn).

### Khi nào phải bỏ qua?
- [ ] Ngoài killzone (giờ Á, giữa trưa NY) → M5 = noise.
- [ ] H1 bias không rõ / đang range hẹp không có draw.
- [ ] Thiếu M5 sweep (vào chỉ vì thấy M5 FVG hoặc M1 MSS).
- [ ] Target H1 quá gần → sau khi trừ spread/commission, R:R thực < kế hoạch.
- [ ] Sát giờ tin lớn (NFP/CPI/FOMC/ECB/BoE) chưa có displacement rõ.

---

## 3. Displacement & MSS trên khung thấp — nơi nhiễu giết trader

![[ICT2022-LTF-M5-Displacement-vs-M1-Noise.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Chart 2 cột: cột trái "M5 displacement hợp lệ" — cụm nến M5 thân lớn, CLV cao, phá swing M5 kèm acceptance, để lại M5 FVG rõ; bên dưới lồng chart M1 tương ứng cho thấy M1 chỉ dùng để *refine* điểm vào bên trong M5 FVG. Cột phải "M1 MSS giả (noise)" — trên M1 thấy một "MSS" nhỏ nhưng khi zoom ra M5 thì đó chỉ là một nhịp giật bên trong range M5, không phá cấu trúc M5, không có H1 draw phía sau. Nhấn mạnh: "Động cơ mô hình = M5 displacement; M1 chỉ refine". Sơ đồ khái niệm, không phải chart giá thật.

> [!important] Quy tắc vàng: M5 là động cơ, M1 là vô-lăng tinh chỉnh
> Sai lầm chết người của khung thấp là **nâng M1 MSS lên thành động cơ mô hình**. Trên M1, một cú giật spread cũng tạo ra "MSS" trông y như thật. Quy tắc: **displacement + MSS phải được xác nhận trên M5** (tầng POI); M1 chỉ dùng để bấm entry chính xác hơn bên trong M5 FVG (ví dụ chờ M1 FVG hoặc M1 sweep nhỏ quanh CE). Đây chính là nội dung cốt lõi của [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]].

**4 tiêu chí displacement (áp cho M5, điều chỉnh cho khung thấp):**

| Tiêu chí | Ngưỡng ở khung gốc | Điều chỉnh cho M5 (LTF) |
|---|---|---|
| **CLV** (close location value) | ≥ 0.7–0.8 | Giữ ≥ 0.7; M5 wick nhiễu hơn nên đừng nới lỏng |
| **Body/wick ratio** | Thân ≥ 65–70% | Yêu cầu **chặt hơn**: thân ≥ 70% — M5 dễ có "nến to bấc dài" do spike |
| **Phá swing + acceptance** | Nến sau không lấp lại | Cần ≥ 1 nến M5 đóng ngoài, tốt hơn là 2 — M5 hay "phá giả" |
| **FVG sạch** | Gap 3 nến rõ | M5 FVG thường **nhỏ**; đo bằng point/pip cụ thể, đừng để spread nuốt gap |

> [!warning] Spread có thể "ăn" luôn FVG trên khung thấp
> Trên M5, một bullish FVG của NQ1 có thể chỉ rộng vài điểm; của EURUSD chỉ 2–4 pip. Nếu spread + commission ≈ độ rộng FVG, thì "entry tại CE" thực tế đã trượt qua nửa gap. **Luôn đo độ rộng FVG bằng con số tuyệt đối** và so với spread hiện tại trước khi coi nó là POI hợp lệ. Đây là lý do biến thể LTF **không hợp với broker spread rộng**.

**Double-sweep trên M5:** vì thanh khoản mỗi pool M5 nhỏ, thuật toán thường cần **quét 2 lần** (Asian low rồi London low chẳng hạn) trước displacement thật. Đừng vào ngay ở sweep đầu; chờ displacement M5 xác nhận (xem cơ chế IPDA trong [[01 - ICT 2022 Model]]).

---

## 4. Quy trình phân tích đa khung — H1 → M5 → M1

> [!example] 4 câu bắt buộc trước khi bấm lệnh
> 1. **Bias H1 và draw on liquidity H1 là gì? H4 có ngược không?**
> 2. **Đang trong killzone/macro nào? (nếu "không" → dừng)**
> 3. **M5 đã sweep pool nào + displacement M5 để lại FVG chưa?**
> 4. **Entry/stop/target ở đâu, R:R *sau khi trừ spread* có ≥ kế hoạch không?**

### H1 (lọc H4) — Bias & Narrative
- **Bias:** hướng nhịp H1 hiện tại trong dealing range H1/H4 ([[12 - Daily Bias]], [[12 - Dealing Range]]).
- **Draw:** pool H1 là target cuối (BSL cho Long / SSL cho Short) — PDH/PDL, session high/low, equal highs/lows H1.
- **Premium/Discount:** chia dealing range H1 → chỉ Long ở discount, Short ở premium ([[27 - Premium Discount]]).
- **Lọc H4:** nếu H4 đang displacement mạnh ngược hướng → hạ cấp hoặc bỏ.

### M5 — POI · Sweep · Displacement (tầng ra quyết định)
- **Đánh dấu pool M5 sẽ bị quét:** đáy/đỉnh M5, Asian range, equal M5.
- **Chờ sweep + reclaim** rồi **M5 displacement** phá cấu trúc M5 → M5 FVG.
- **Ghi cụ thể:** `M5 bullish FVG 20180.5–20188.0, CE 20184.25` (NQ1) hoặc `EURUSD M5 FVG 1.08420–1.08455, CE 1.084375`.

### M1 — Confirmation & Entry refine
- **Refine:** trong M5 FVG, tìm M1 FVG / M1 sweep nhỏ quanh CE để vào giá tốt hơn.
- **Confirmation tùy chọn:** chờ một M1 MSS nhỏ *bên trong* M5 FVG để xác nhận (giảm rủi ro dao "rơi tiếp"), đánh đổi bằng entry hơi trễ hơn.
- **Stop:** ngoài điểm M5 sweep / đầu kia M5 FVG + **buffer cho wick** (đặc biệt NQ1).
- **Target:** internal M5 liquidity trước → external H1 pool sau.

```text
Mẫu ghi nhanh — ICT 2022 LTF Long (H1→M5→M1)
Bias (H1): Bullish | H4: không ngược | Draw: H1 BSL @ [level]
Killzone: London / NY AM (macro ..:..)  ← GATE
Location: Discount của dealing range H1
(1) M5 Sweep: SSL @ [level] + reclaim
(2) M5 Displacement + MSS phá [M5 swing high] → M5 FVG
(3) M5 FVG: [low]–[high], CE [mid]  | Rộng: [x pip/pt] vs spread [y]
(4) Entry: M1 refine quanh CE / M1 FVG; Stop dưới M5 sweep + buffer
(5) Target: internal M5 [..] → external H1 BSL [..]
R:R sau trừ spread: [..]   Invalid: M5 đóng nến dưới FVG
```

```text
Mẫu ghi nhanh — ICT 2022 LTF Short (H1→M5→M1)
Bias (H1): Bearish | H4: không ngược | Draw: H1 SSL @ [level]
Killzone: London / NY AM (macro ..:..)  ← GATE
Location: Premium của dealing range H1
(1) M5 Sweep: BSL @ [level] + reclaim
(2) M5 Displacement + MSS phá [M5 swing low] → M5 FVG
(3) M5 FVG: [low]–[high], CE [mid]  | Rộng: [x pip/pt] vs spread [y]
(4) Entry: M1 refine quanh CE / M1 FVG; Stop trên M5 sweep + buffer
(5) Target: internal M5 [..] → external H1 SSL [..]
R:R sau trừ spread: [..]   Invalid: M5 đóng nến trên FVG
```

> [!warning] Đừng chase M5 displacement
> Y như khung gốc: M5 displacement để **xác nhận**, không phải để vào. Entry ở bước **retrace về M5 FVG**. Vào ngay khi thấy nến M5 lớn = bỏ bước retrace, R:R xấu, dễ trúng đỉnh/đáy micro. Xem [[35 - Aggressive Displacement Entry]] để biết *khi nào* mới được phép vào sớm (chỉ khi có tiêu chí bổ sung rất chặt).

---

## 5. Điều chỉnh theo thị trường (NQ1 vs EURUSD/GBPUSD)

Cùng một chuỗi M5, nhưng hai thị trường bạn chọn hành xử khác nhau rõ trên khung thấp:

| Đặc tính | NQ1 / NAS100 | EURUSD / GBPUSD |
|---|---|---|
| Tần suất setup M5 / phiên | Cao (nhiều nhịp sweep–displacement) | Vừa (1–2 nhịp sạch mỗi phiên chính) |
| Kích thước M5 FVG | Nhỏ–vừa, **lấp rất nhanh** (vài phút) | Nhỏ, lấp trong phiên |
| Wick / stop buffer | **Cần buffer rộng** — wick M5 dài | Buffer vừa; sweep "sạch" hơn nhờ thanh khoản sâu |
| Spread/commission so target | Trung bình (giãn quanh tin) | Thấp (trừ lúc tin) — hợp khung thấp hơn NQ1 |
| Killzone tốt nhất | **NY AM 09:50–10:10 ET** | London Open, NY AM (overlap) |
| SMT soi kèm | ES/S&P (thuận) | GBPUSD↔EURUSD (thuận) + DXY (nghịch) — [[42 - SMT Divergence]] |
| Bẫy chính | Nhiều "cơ hội" → **overtrade**; wick quét stop | Trade giờ Á thanh khoản mỏng; tin riêng GBP phá SMT |

> [!tip] Quy tắc thực dụng
> **NQ1 →** kỷ luật "chỉ 1–2 lệnh A+/phiên", buffer stop rộng cho wick, chốt một phần sớm vì FVG lấp nhanh. **EURUSD/GBPUSD →** chỉ đánh London & NY AM, dùng **SMT M5 giữa EURUSD–GBPUSD–DXY** như lớp xác nhận sweep rất mạnh (tương quan chặt trong phiên chính). Tuyệt đối tránh giờ Á.

> [!note] Vì sao bỏ XAUUSD khỏi biến thể này
> Bạn không chọn XAUUSD cho biến thể LTF — và đó là lựa chọn đúng: trên khung thấp, gold có FVG rất rộng, slippage cao và giật quanh tin, khiến M5/M1 kém tin cậy hơn nhiều so với NQ1/FX. Nếu sau này muốn thử gold ở LTF, hãy backtest **tách riêng** với stop rộng hơn và lọc tin nghiêm ngặt.

---

## 6. Quy tắc xác nhận / vô hiệu hóa

### Setup hợp lệ khi
- [ ] **GATE:** đang trong London/NY AM killzone (bắt buộc cho LTF).
- [ ] Bias H1 rõ + draw H1 xác định + H4 không ngược gay gắt.
- [ ] M5 liquidity sweep rõ + reclaim TRƯỚC displacement.
- [ ] M5 displacement đạt ≥ 3/4 tiêu chí (CLV/body-wick/acceptance/FVG), để lại M5 FVG sạch.
- [ ] Entry là **retrace** về M5 FVG (M1 refine), đúng premium/discount, không chase.
- [ ] Stop ngoài M5 sweep + buffer; target H1 pool rõ; **R:R sau trừ spread ≥ kế hoạch**.

### Setup bị vô hiệu khi
- [ ] Ngoài killzone → không phải setup LTF hợp lệ.
- [ ] Thiếu M5 sweep (vào vì M5 FVG hoặc M1 MSS đơn lẻ).
- [ ] Displacement chỉ có trên M1, không xác nhận trên M5.
- [ ] M5 đóng nến xuyên qua FVG (acceptance) → POI invalid.
- [ ] Spread + commission ≈ độ rộng FVG hoặc ăn > 1/3 target.
- [ ] Entry ngược bias H1 / sai premium-discount / chase.

### Mức độ "đủ chuỗi"

| Quan sát | Trạng thái | Cách đọc |
|---|---|---|
| GATE pass + H1 bias + M5 sweep + M5 displacement + FVG + retrace | **A+ setup** | Thực thi theo plan |
| Đủ chuỗi nhưng target H1 gần, R:R sau spread mỏng | **Hạ cấp / bỏ** | Không đáng phí + rủi ro |
| Có M5 FVG + M5 MSS nhưng KHÔNG có sweep | **Không đủ chuỗi** | Bỏ |
| Chỉ có tín hiệu trên M1, M5 chưa displacement | **Chưa tới** | Chờ M5 xác nhận |
| Đủ chuỗi nhưng ngoài killzone | **No Trade** | LTF ngoài KZ = noise |

---

## 7. Rủi ro, chi phí & hàm ý prop-firm (đọc kỹ trước khi backtest)

> [!important] Vì sao mục này quan trọng với mục tiêu FTMO / The5ers của bạn
> Bạn đang ở foundation phase, hướng tới pass **FTMO 10K** và **The5ers 10K** (mục tiêu ~7/1/2027). Biến thể LTF tương tác *trực tiếp* với luật của hai firm này theo cách khác hẳn khung gốc.

**Chi phí giao dịch (điểm yếu chí mạng của LTF):**
- Target nhỏ → **spread + commission chiếm tỷ trọng lớn trong R**. Một setup R:R "3R trên giấy" có thể còn ~2R sau chi phí. Luôn tính R:R *ròng*.
- Slippage quanh tin ăn mạnh hơn vì stop/target gần giá.

**Position sizing & stop:** stop LTF nhỏ hơn (tính theo giá) → với cùng **risk ≤ 0.5%/lệnh** (luật vault), bạn có thể size lớn hơn về khối lượng. Điều này *khuếch đại* tác động của slippage. Xem [[43 - Position Sizing]] và luật risk trong `CLAUDE.md`.

**FTMO 10K (daily loss theo balance khởi đầu cố định, reset hằng ngày; có yêu cầu số ngày trade tối thiểu):**
- LTF cho **nhiều ngày trade** hơn → dễ đạt yêu cầu min trading days.
- NHƯNG nhiều lệnh/ngày → dễ **chạm daily loss limit** nếu chuỗi thua ngắn hạn dồn lại. Cần **hard stop số lệnh/ngày**.

**The5ers 10K (logic tham chiếu equity đóng cửa hôm trước; cần số ngày có lãi tối thiểu ~0.5%+/ngày):**
- LTF hợp với yêu cầu "nhiều ngày lãi nhỏ" — mỗi phiên gom vài lệnh nhỏ đạt +0.5% dễ hơn.
- NHƯNG overtrade cuối ngày để "ép đủ 0.5%" là bẫy — trả lại lợi thế.

> [!warning] Luật khác nhau — đừng trộn thói quen
> Thói quen "gom nhiều lệnh nhỏ mỗi ngày" tối ưu cho The5ers có thể khiến bạn **chạm daily loss của FTMO** nhanh hơn. Giữ hai bộ luật tách biệt (xem project instructions). Với biến thể LTF, đề xuất tự áp: **tối đa 2–3 lệnh A+/phiên, dừng ngày khi -1R hoặc -2 lệnh liên tiếp**, bất kể firm nào.

**Guardrails tâm lý (LTF khuếch đại):**
- Overtrading, revenge trading, chase, dời stop — tất cả *nặng hơn* trên khung thấp vì nhịp nhanh và nhiều "cơ hội". Nếu thấy mình vào lệnh thứ 4–5 trong phiên, gần như chắc chắn đã rời khỏi mô hình. Liên kết: [[Mistake - Chase Displacement]], [[Mistake - Skip Liquidity Sweep]].

---

## 8. Kế hoạch backtest riêng cho biến thể (bắt buộc trước khi dùng vốn)

> [!important] KHÔNG giả định thống kê khung gốc chuyển sang
> Đây là note `status: seed` — chưa có dữ liệu. Trước khi coi biến thể này là một phần edge, nó phải qua backtest riêng, đủ mẫu, không cherry-pick. Dùng template `Backtest templete.md` và dashboard `04 - Backtesting/_Backtest Dashboard`.

Checklist backtest cho biến thể LTF:
- [ ] **Sample size:** đặt mục tiêu ≥ 50–100 setup *cùng bộ luật GATE* (killzone + sweep + M5 displacement). Khung thấp cho nhiều mẫu nhanh — tận dụng, nhưng đừng nới luật để "gom mẫu".
- [ ] **Tách theo thị trường:** NQ1 và EURUSD/GBPUSD backtest riêng — expectancy có thể khác hẳn.
- [ ] **Tách theo killzone:** so London vs NY AM; nhiều khả năng một khung vượt trội.
- [ ] **Ghi chi phí:** log R:R *ròng sau spread/commission*, không chỉ R lý thuyết.
- [ ] **Chống hindsight:** trigger (sweep + M5 displacement) phải nhận diện được *trước* khi biết kết quả — đây là bẫy curve-fitting lớn nhất của LTF vì có quá nhiều nến để "chọn đẹp".
- [ ] **Metric quyết định:** win rate, average R, **expectancy ròng**, max consecutive loss (để set daily stop), và độ ổn định giữa các phiên.
- [ ] **Readiness gate:** chỉ đưa biến thể vào demo/challenge khi expectancy ròng dương ổn định qua ≥ 2 tháng mẫu và recurring-mistake rate giảm.

> [!note]
> Đây là biến thể "con" của [[01 - ICT 2022 Model]]. Khi review trade LTF, vẫn soi qua 7 bước gốc — nhưng chấm điểm displacement trên **M5**, không phải M1, và luôn kiểm tra GATE killzone đầu tiên. Lỗi phổ biến nhất của khung thấp: **bỏ GATE killzone** và **nâng M1 noise thành động cơ mô hình**.

---

## Liên kết

**Note gốc & khung layering:**
- [[01 - ICT 2022 Model]] (note mẹ)
- [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]]
- [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]]
- [[32 - Top-down Analysis (Multiple Timeframes)]]
- [[37 - Re-mapping Dealing Range sau Displacement]]

**Bước trong chuỗi:**
- [[12 - Daily Bias]] · [[12 - Dealing Range]] · [[27 - Premium Discount]]
- [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] · [[19 - Liquidity]]
- [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- [[13 - FVG  - Fair Value Gap]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]]
- [[16 - Internal & External Range Liquidity (IRL & ERL)]]

**Timing & xác nhận:**
- [[18 - Kill Zones]] · [[40 - Macro Times]]
- [[42 - SMT Divergence]] · [[35 - Aggressive Displacement Entry]]

**Rủi ro & lỗi:**
- [[43 - Position Sizing]]
- [[Mistake - Skip Liquidity Sweep]] · [[Mistake - Chase Displacement]] · [[Mistake - Trade Against Bias]]
