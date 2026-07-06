---
type: ict-concept
concept: ICT 2022 Model
aliases:
  - ICT 2022 Model
  - ICT 2022
  - 2022 Model
  - ICT Model 2022
tags:
  - trading/ict/concept
  - trading/study
  - "#ICT2022"
status: developing
category: Entry Model
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - ICT 2022
  - Silver Bullet
  - OTE
  - AMD
  - MMXM
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-05
common_mistakes:
  - "[[Mistake - Skip Liquidity Sweep]]"
  - "[[Mistake - Chase Displacement]]"
  - "[[Mistake - Trade Against Bias]]"
---

# ICT 2022 Model

> [!summary] Tóm tắt 1 câu
> **ICT 2022 Model là quy trình entry hoàn chỉnh ghép các khái niệm rời rạc thành một chuỗi: xác định draw on liquidity theo bias → chờ liquidity sweep → displacement phá cấu trúc (MSS) để lại FVG → vào lệnh khi giá retrace về FVG → target pool liquidity đối diện.**

> [!important] Nguyên tắc cốt lõi
> **Mô hình là một CHUỖI có thứ tự bắt buộc: Bias → Liquidity → Sweep → Displacement/MSS → FVG → Entry → Target. Bỏ qua bất kỳ mắt xích nào (đặc biệt là liquidity sweep) đều làm setup mất xác suất.**
> Đây không phải một chỉ báo; nó là một "công thức nấu ăn". Thiếu nguyên liệu hoặc sai thứ tự thì không phải món ăn ICT 2022.

---

## 1. Định nghĩa

![[ICT2022-7Step-Flow-Diagram.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ luồng (flow diagram) dạng 7 khối nối tiếp nhau theo chiều ngang hoặc chiều dọc, mỗi khối là một bước: **(1) Bias (HTF) → (2) Draw on Liquidity → (3) Liquidity Sweep → (4) Displacement + MSS → (5) FVG (POI) → (6) Entry (retrace) → (7) Target**. Dùng mũi tên liền nét nối các bước theo đúng thứ tự bắt buộc, có thể thêm icon nhỏ cho từng bước (con mắt cho Bias, nam châm cho Liquidity, lưỡi dao cho Sweep, tia chớp cho Displacement, khoảng trống cho FVG, mục tiêu cho Entry, cờ đích cho Target). Đây là sơ đồ khái niệm minh họa quy trình, không phải chart giá thật.

**Khái niệm:**
ICT 2022 Model là **mô hình giao dịch tổng hợp** mà ICT công bố trong loạt bài năm 2022, gói toàn bộ các khái niệm cốt lõi (bias, liquidity, sweep, displacement, MSS, FVG, premium/discount) thành **một quy trình entry duy nhất, lặp lại được**. Mục tiêu: biến mớ khái niệm rời rạc thành một checklist hành động rõ ràng từ HTF xuống LTF.

**Chuỗi 7 bước của mô hình:**
1. **Bias (HTF):** xác định hướng — Bullish / Bearish (xem [[12 - Daily Bias]]).
2. **Draw on liquidity:** xác định pool liquidity mà giá đang bị hút về (target cuối) và pool sẽ bị quét trước.
3. **Liquidity Sweep:** chờ giá quét một pool liquidity (đỉnh/đáy, equal highs/lows) — đây là trigger ([[20 - Liquidity Sweep]]).
4. **Displacement + MSS:** một move mạnh, quyết đoán phá cấu trúc ([[21 - Market Structure Shift]] + [[Displacement]]) theo hướng bias, **để lại FVG**.
5. **FVG (POI):** xác định Fair Value Gap của nhịp displacement — đây là điểm vào ([[Fair Value Gap]]).
6. **Entry:** vào lệnh khi giá **retrace** về FVG (thường quanh CE 50%), đúng premium/discount.
7. **Target:** pool liquidity đối diện (internal trước, external sau).

**Bản chất:** mô hình mã hóa logic "smart money": giá quét thanh khoản (lấy nhiên liệu) → đẩy mạnh đổi hướng (thể hiện intent, để lại imbalance) → quay lại lấp một phần imbalance (cho retail một điểm vào "giá tốt") → chạy về pool liquidity tiếp theo. Bạn vào cùng lúc với chiều của displacement, tại vùng giá chiết khấu.

**Mục đích trong ICT:**
- Cho một **khung execution chuẩn hóa**, lặp lại và backtest được.
- Buộc trader **chờ đủ điều kiện** thay vì vào theo cảm tính.
- Định nghĩa rõ **entry, stop, target** ở mỗi bước.
- Là "xương sống" để các biến thể (Silver Bullet, OTE, AMD) gắn vào.

**Vì sao khái niệm này quan trọng:**
Hầu hết người học ICT biết từng khái niệm riêng nhưng không biết **ghép chúng theo thứ tự nào**. ICT 2022 Model chính là thứ tự đó. Nó cũng là bộ lọc kỷ luật: nếu một setup không đi qua đủ chuỗi, bạn có lý do khách quan để "No Trade".

**Nó giúp trả lời câu hỏi nào trên chart?**
- Setup hiện tại đã đi qua đủ chuỗi (sweep → displacement → FVG) chưa?
- Đang ở bước nào của mô hình, còn thiếu bước gì?
- FVG nào là POI hợp lệ, entry và stop ở đâu?
- Pool liquidity nào là target, R:R bao nhiêu?

### ICT 2022 Model không phải là gì
- Không phải một chỉ báo / tín hiệu tự động.
- Không phải "thấy FVG là vào" — FVG chỉ là bước 5, phải có sweep + MSS trước.
- Không phải cái cớ để bỏ qua bias / premium-discount.
- Không phải chỉ dùng được một timeframe — nó là quy trình HTF→LTF.
- Không phải đảm bảo thắng; nó là khung xác suất cần kết hợp risk management.

### Vì sao mô hình này hoạt động — nền tảng IPDA & "smart money"

> [!important] Đây là phần lý thuyết nền — hiểu WHY trước khi hỏi WHAT
> Phần lớn trader học thuộc 7 bước như một công thức máy móc mà không hiểu **vì sao** chuỗi này lặp lại được trên mọi thị trường, mọi khung thời gian. Không hiểu lý thuyết nền thì khi thị trường "phá lệ" một lần, trader sẽ hoảng và bỏ mô hình đúng lúc nó vẫn đang đúng.

**IPDA — Interbank Price Delivery Algorithm (khái niệm của ICT):**
- ICT mô tả price delivery trên các cặp FX/index/kim loại như được chi phối bởi một **thuật toán phân phối giá liên ngân hàng** — không phải một cái máy chủ vật lý cụ thể, mà là **mô hình tư duy** để giải thích hành vi giá lặp lại: giá không di chuyển ngẫu nhiên, nó di chuyển **từ pool thanh khoản này sang pool thanh khoản khác**, dùng các phạm vi lookback chuẩn (IPDA data ranges: 20/40 ngày cho short-term, 1 năm / nhiều năm cho long-term) để xác định đâu là "old high/low" đáng quét.
- Hệ quả thực dụng cho ICT 2022 Model: bước 2 (**draw on liquidity**) không phải đoán mò — nó dựa trên giả định rằng thuật toán sẽ **tìm tới thanh khoản nghỉ tại các mức cũ** (equal highs/lows, old swing points, session highs/lows) trước khi thực sự "muốn" đi xa hơn.

**Vì sao giá "phải" săn thanh khoản trước khi di chuyển thật:**
- Thị trường OTC (FX, một phần index CFD) không có sàn khớp lệnh tập trung; các tổ chức lớn (ngân hàng, quỹ) cần **thanh khoản đối ứng đủ lớn** để vào/thoát vị thế mà không trượt giá quá nhiều.
- Thanh khoản đối ứng lớn nhất nằm ở **cụm lệnh dừng (stop-loss) của retail** — nằm ngay trên đỉnh cũ (buy-side liquidity) và ngay dưới đáy cũ (sell-side liquidity), vì đó là nơi phần lớn trader retail đặt stop hoặc chờ breakout.
- "Smart money" (thuật ngữ ICT dùng, không hàm ý một nhóm cụ thể) được mô hình hóa như bên **hấp thụ (absorb)** thanh khoản đó: đẩy giá **quét qua** các mức stop này (bước 3 — Sweep) để có đủ đối ứng khớp lệnh, RỒI mới đẩy giá thật theo hướng dự định (bước 4 — Displacement).
- Đây là lý do bước Sweep **luôn đứng trước** Displacement trong chuỗi — về logic, không thể có move thật "miễn phí" khi vẫn còn pool thanh khoản gần đó chưa bị động tới; thị trường có xu hướng dọn thanh khoản gần nhất trước khi cam kết hướng đi.

**Vì sao displacement để lại FVG là dấu hiệu của "intent":**
- Khi các lệnh lớn được khớp dồn dập theo một hướng (sau khi đã có đủ thanh khoản đối ứng từ sweep), giá bị đẩy nhanh tới mức **bên mua/bên bán không kịp giao dịch ở mọi mức giá trung gian** → để lại khoảng trống (imbalance / FVG). FVG vì vậy không phải hiện tượng ngẫu nhiên, mà là **dấu vân tay của việc "hết đối ứng"** tại các mức đó — một bằng chứng gián tiếp cho thấy vừa có dòng lệnh mất cân bằng thật, không phải noise.
- Đây cũng là lý do ICT dùng FVG (thay vì chỉ dùng MSS) làm POI: FVG đánh dấu đúng **vùng giá mà thị trường "nợ" một sự cân bằng lại** — xác suất giá quay lại lấp một phần cao hơn so với chọn bừa một vùng hỗ trợ/kháng cự cũ.

**Áp dụng thực dụng của lý thuyết này:**
- Trước phiên, luôn hỏi: *"Pool thanh khoản nào retail đang set up để bị quét?"* — đó thường chính là setup mà đám đông nhìn thấy rõ nhất (equal highs/lows đẹp, đỉnh/đáy vừa hình thành).
- Đừng coi sweep là "tín hiệu đảo chiều ngay lập tức" — nó là bước **thu thập thanh khoản**; xác nhận đảo chiều thật nằm ở bước Displacement + MSS theo sau.
- Hiểu IPDA giúp bạn KHÔNG hoảng khi giá "quét" thêm một pool nữa trước khi displacement — thuật toán có thể cần nhiều hơn một lần quét nếu thanh khoản một pool không đủ; đây là lý do một số setup có "double sweep" trước khi displacement thật sự xảy ra.

---

## 2. Bối cảnh sử dụng

### Các bước & khái niệm tương ứng

| Bước | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| 1 | Bias | [[12 - Daily Bias]] | Hướng HTF là gì? |
| 2 | Draw on liquidity | [[19 - Liquidity]], [[12 - Dealing Range]] | Giá bị hút về pool nào? |
| 3 | Liquidity Sweep | [[20 - Liquidity Sweep]] | Đã quét pool nào, có reclaim? |
| 4 | Displacement + MSS | [[Displacement]], [[21 - Market Structure Shift]] | Có phá cấu trúc + để lại FVG không? |
| 5 | FVG (POI) | [[Fair Value Gap]], [[Order Block]] | FVG ở đâu, CE ở đâu? |
| 6 | Entry | [[27 - Premium Discount]], [[Optimal Trade Entry]] | Đúng premium/discount, R:R đủ chưa? |
| 7 | Target | [[19 - Liquidity]] | Pool đối diện ở đâu? |

### Biến thể thường gặp
- **+ OTE:** thay vì chỉ FVG, dùng vùng OTE 62–79% trùng FVG để refine entry ([[Optimal Trade Entry]]).
- **+ Silver Bullet:** chạy mô hình trong cửa sổ 1 giờ của [[18 - Kill Zones]].
- **+ AMD:** đặt mô hình trong khung Tích lũy–Thao túng–Phân phối ([[02 - AMD]]); sweep ~ manipulation, displacement ~ distribution.
- **+ Order Block / Breaker:** POI ở bước 5 có thể là OB/Breaker thay vì FVG.

> [!tip]
> Cách nhớ nhanh: **"Quét → Đẩy → Lùi → Vào → Chạy"** (Sweep → Displace/MSS → Retrace to FVG → Entry → Run to target). Nếu một setup không có cả "Quét" lẫn "Đẩy", nó không phải ICT 2022.

### Khi nào mô hình này có giá trị cao?
- [ ] Bias HTF rõ ràng, có draw on liquidity cụ thể.
- [ ] Có liquidity sweep rõ trước displacement.
- [ ] Displacement phá cấu trúc và để lại FVG sạch.
- [ ] FVG ở đúng premium/discount, đồng hướng bias.
- [ ] Trong [[18 - Kill Zones]] (London/NY) → xác suất cao hơn.

### Khi nào nên bỏ qua?
- [ ] Thiếu liquidity sweep (vào chỉ vì thấy FVG/MSS).
- [ ] Displacement yếu / không để lại FVG.
- [ ] Setup ngược bias hoặc sai premium-discount.
- [ ] Vào khi giá đã chạy xa (chase, không chờ retrace).
- [ ] Ngoài kill zone / sát giờ tin lớn.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Pool liquidity đánh dấu trước:** xác định BSL/SSL hai phía, pool là draw.
2. **Sweep:** giá quét một pool, có reclaim (đóng nến trở lại).
3. **Displacement:** nến/đoạn thân lớn, quyết đoán, phá swing (MSS).
4. **FVG:** khoảng imbalance 3 nến do displacement để lại; xác định CE.
5. **Retrace:** giá quay lại FVG đúng premium/discount → điểm vào.

### Ma trận nhận diện (Long)

| Bước | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Bias | HTF bullish, draw lên BSL | Bias không rõ → bỏ |
| Sweep | Quét SSL + reclaim | Không sweep → không phải ICT 2022 |
| Displacement/MSS | Phá swing high + FVG bullish | Move yếu, không FVG → bỏ |
| FVG | Bullish FVG (BISI), CE rõ | Không có gap thật → bỏ |
| Entry | Tại FVG, ở discount | Ở premium → sai chỗ |
| Target | BSL phía trên | Không pool rõ → R:R kém |

### Điều kiện bắt buộc
- [ ] Bias HTF xác định + draw on liquidity.
- [ ] Có liquidity sweep trước displacement.
- [ ] Displacement phá cấu trúc và để lại FVG.
- [ ] Xác định FVG/CE và mức invalidation.
- [ ] Xác định pool target.

### Điều kiện tăng xác suất
- [ ] FVG trùng OB / OTE 62–79% (confluence).
- [ ] Setup trong kill zone, trùng pha distribution AMD.
- [ ] FVG ở đúng premium/discount, đồng hướng bias.
- [ ] Stop logic ngoài điểm sweep; R:R ≥ kế hoạch.

### Điều kiện làm setup yếu đi
- Sweep mờ / không rõ reclaim.
- Displacement không dứt khoát, FVG bị lấp nhanh.
- Nhiều FVG chồng chéo, POI mơ hồ.
- Ngoài kill zone, gần tin tức.

### Displacement thật vs. nến to nhưng yếu — khung đánh giá khách quan hóa

![[ICT2022-Displacement-vs-WeakCandle-Comparison.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Chart minh họa 2 cột cạnh nhau: bên trái là "Displacement hợp lệ" — một nến/chuỗi nến thân lớn, đóng cửa gần đỉnh/đáy (close location value cao), bấc ngắn, phá rõ swing point cũ và có nến sau đó KHÔNG đóng cửa lấp lại vùng vừa phá (acceptance), để lại FVG rõ 3 nến. Bên phải là "Nến to nhưng yếu" — nến thân lớn nhưng bấc dài cả hai đầu, đóng cửa giữa thân (close location value ~50%), không thực sự phá qua swing point hoặc phá rồi bị nến sau đóng cửa lấp ngược lại (rejection/failure to accept), không để lại FVG sạch. Đây là chart minh họa khái niệm, không phải dữ liệu giao dịch thật.

> [!important] Đây là bước chủ quan nhất trong mô hình — cần một khung đánh giá càng khách quan càng tốt
> "Displacement" là điểm mà trader mới hay nhầm nhất: thấy một nến thân dài là gọi ngay là displacement. Nhưng không phải cứ nến to là có "intent" thật. Dưới đây là 4 tiêu chí kiểm tra gần như định lượng được, dùng thay thế cho cảm tính "nhìn to là được".

**Tiêu chí 1 — Close Location Value (CLV):**
- Công thức: `CLV = (Close − Low) / (High − Low)` cho nến tăng mong muốn (ngược lại cho nến giảm dùng `(High − Close) / (High − Low)`).
- Displacement hợp lệ: CLV nên **≥ 0.7–0.8** — tức giá đóng cửa gần đỉnh nến (cho move tăng) hoặc gần đáy nến (cho move giảm). CLV thấp (~0.5) nghĩa là phe đối lập đã đẩy giá lùi lại đáng kể trong chính nến đó → dấu hiệu hấp thụ (absorption), không phải đẩy giá dứt khoát.

**Tiêu chí 2 — Tỷ lệ thân nến / bấc nến (body-to-wick ratio):**
- Displacement hợp lệ: thân nến nên chiếm **≥ 65–70%** tổng range của nến; bấc đối lập (bấc trên với nến tăng, bấc dưới với nến giảm) nên nhỏ.
- Bấc đối lập dài cho thấy có lực cản mạnh đã đẩy giá lùi lại trong quá trình hình thành nến — một "nến to" với bấc dài hai đầu thường là kết quả của volatility/tin tức, không phải một dòng lệnh một chiều thật.

**Tiêu chí 3 — Có phá swing point kèm "acceptance" hay không:**
- Không chỉ cần giá xuyên qua swing high/low cũ; cần **nến tiếp theo (hoặc vài nến sau) KHÔNG đóng cửa quay lại bên trong** vùng vừa phá — đây gọi là "acceptance" (thị trường chấp nhận mức giá mới).
- Nếu giá phá swing rồi nến ngay sau đó đóng cửa lấp lại (failure to accept / phá giả), đây là **liquidity grab**, không phải MSS + displacement thật — thường đây chính là bước Sweep của một chu kỳ khác, không phải Displacement.

**Tiêu chí 4 — Có để lại FVG sạch 3 nến hay không:**
- Displacement thật gần như luôn để lại một FVG rõ ràng (gap giữa wick của nến 1 và nến 3 trong bộ 3 nến) vì tốc độ di chuyển vượt quá khả năng khớp lệnh liên tục ở mọi mức giá.
- Nếu "nến to" đó KHÔNG để lại FVG nào (các nến liền kề chồng lấn hoàn toàn), khả năng cao đó là volatility thường (tin tức, thanh khoản mỏng cuối phiên) chứ không phải dòng lệnh mất cân bằng có chủ đích.

**Bảng quyết định nhanh:**

| Tiêu chí | Displacement hợp lệ | Nến to nhưng yếu (bỏ qua) |
|---|---|---|
| CLV | ≥ 0.7–0.8 | ~0.4–0.6 |
| Body/wick ratio | Thân ≥ 65–70% range | Bấc hai đầu dài, thân < 50% |
| Phá swing + acceptance | Có, nến sau không lấp lại | Phá rồi bị lấp ngay (failure) |
| FVG để lại | Có, 3 nến rõ | Không có gap, nến chồng lấn |
| Số nến tạo move | 1–3 nến dứt khoát | Nhiều nến giằng co rồi mới đóng xa |

> [!tip]
> Nếu một setup đạt ≥ 3/4 tiêu chí trên, có thể coi là displacement hợp lệ để tiếp tục sang bước FVG/Entry. Nếu chỉ đạt 1–2 tiêu chí, nên hạ cấp thành "chờ xác nhận thêm" thay vì loại vào entry ngay.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng ICT 2022 Model
> 1. **Bias và draw on liquidity là gì?**
> 2. **Đã có liquidity sweep chưa, ở pool nào?**
> 3. **Có displacement phá cấu trúc + FVG đúng premium/discount chưa?**
> 4. **Entry/stop/target ở đâu, R:R bao nhiêu, có trong kill zone không?**

### D1 / H4 — Bias & Narrative
- **Bias:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- **Draw on liquidity:** pool HTF là target cuối (BSL cho Long, SSL cho Short).
- **Dealing range & premium/discount:** xác định vùng để chỉ Long ở discount / Short ở premium.

### H1 / M15 — POI & Context
- **Pool sẽ bị sweep:** đánh dấu đỉnh/đáy, equal highs/lows.
- **Chờ sweep + displacement:** quan sát giá quét pool rồi displacement phá cấu trúc.
- **FVG cụ thể:** ghi range FVG + CE, ví dụ `H1 bullish FVG 1.0820–1.0835, CE 1.08275`.

### M5 / M1 — Confirmation & Entry
- **Refine:** trên LTF, displacement thường để lại một FVG nhỏ hơn; có thể chờ M5 MSS để xác nhận.
- **Entry:** tại FVG (quanh CE) / OTE trùng FVG.
- **Stop:** ngoài điểm sweep / đầu kia FVG.
- **Target:** internal liquidity trước, external pool sau.

```text
Mẫu ghi nhanh — ICT 2022 Long
Bias (HTF): Bullish | Draw: BSL @ [level]
Location: Discount
(1) Sweep: SSL @ [level] + reclaim
(2) Displacement + MSS phá [swing high] → FVG
(3) FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop dưới sweep / dưới FVG
(5) Target: internal [..] → external BSL [..]
Kill zone: London / NY AM
Invalid: đóng nến dưới FVG (acceptance)
```

```text
Mẫu ghi nhanh — ICT 2022 Short
Bias (HTF): Bearish | Draw: SSL @ [level]
Location: Premium
(1) Sweep: BSL @ [level] + reclaim
(2) Displacement + MSS phá [swing low] → FVG
(3) FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop trên sweep / trên FVG
(5) Target: internal [..] → external SSL [..]
Kill zone: London / NY AM
Invalid: đóng nến trên FVG (acceptance)
```

> [!warning]
> **Đừng "chase" displacement.** Bước displacement là để XÁC NHẬN, không phải để vào lệnh. Entry xảy ra ở bước RETRACE về FVG. Vào ngay khi thấy nến lớn = bỏ qua bước 6, R:R xấu và dễ trúng đỉnh/đáy ngắn hạn.

### Mô hình biểu hiện khác nhau ra sao trên từng thị trường đang trade

![[ICT2022-CrossMarket-Behavior-Comparison.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Bảng/sơ đồ 3 cột so sánh side-by-side hành vi giá của NQ1/NDX, EURUSD/GBPUSD, và XAUUSD trong cùng một khung thời gian intraday (ví dụ cùng 1 phiên NY AM), mỗi cột minh họa nhịp sweep-displacement-FVG điển hình của thị trường đó với biên độ và tốc độ khác nhau (NQ1 nhiều nhịp nhỏ liên tục, FX có "khoảng lặng" quanh handoff phiên, XAUUSD có nhịp giật mạnh quanh mốc tin tức với FVG rộng). Đây là sơ đồ minh họa hành vi thị trường mang tính khái niệm, không phải chart giá thật.

Cùng một chuỗi 7 bước, nhưng **tốc độ, biên độ, và rủi ro thực thi khác nhau đáng kể** giữa các thị trường đang trade. Không điều chỉnh theo đặc tính thị trường là nguyên nhân phổ biến khiến một setup "đúng lý thuyết" vẫn lỗ vì sai kỳ vọng thực thi.

| Đặc tính | NQ1 / NDX (NAS100) | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Beta / biến động | Rất cao, biến động nhanh theo phút | Trung bình, mượt hơn theo phiên | Cao, giật mạnh quanh tin |
| Tần suất sweep trong ngày | Nhiều lần intraday (thường 3–6+ lần) | Thường 1–2 sweep rõ mỗi phiên chính | Thất thường, tăng đột biến quanh tin |
| Động lực thanh khoản chính | Order flow index, phái sinh, mở cửa phiên Mỹ | Handoff thanh khoản London → NY (Á/Âu thấp) | Tin tức vĩ mô (CPI, NFP, Fed) + dòng trú ẩn an toàn |
| Kích thước FVG điển hình | Nhỏ–vừa, lấp nhanh (vài phút–giờ) | Nhỏ, thường lấp trong phiên | Rộng hơn hẳn, có thể để trống nhiều giờ/ngày |
| Rủi ro trượt giá (slippage) | Trung bình (CFD/future, spread giãn quanh tin) | Thấp (thanh khoản FX lớn) trừ lúc tin | Cao, đặc biệt quanh NFP/CPI/FOMC |
| Kill zone hiệu quả nhất | NY AM (mở cửa phiên Mỹ), London Open | London Open, NY AM (giờ handoff) | London Open, NY AM, và quanh giờ tin |
| Điều chỉnh thực dụng | Size nhỏ hơn vì biến động nhanh; chấp nhận nhiều setup A+ hơn/ngày; stop cần buffer do wick dài | Kiên nhẫn chờ đúng phiên handoff; tránh trade giờ Á thanh khoản mỏng; sweep dễ "sạch" hơn nhờ thanh khoản sâu | Tránh vào lệnh sát giờ tin nếu chưa có displacement rõ; nới stop/giảm size vì FVG rộng và slippage cao; ưu tiên chờ displacement dứt khoát hơn là entry sớm |

> [!tip]
> Quy tắc thực dụng: **NQ1 → nhiều cơ hội, cần kỷ luật KHÔNG ép thêm lệnh; FX → cần kiên nhẫn chờ đúng phiên; XAUUSD → ưu tiên chất lượng displacement hơn tốc độ vào lệnh, và luôn tính slippage vào R:R kế hoạch.**

### Biến thể nâng cao — Single-leg vs. Multi-leg continuation entry

Phần lớn ví dụ trong note này mô tả **một chu kỳ 7 bước duy nhất** (single-leg): sweep → displacement → FVG → entry → target, kết thúc khi chạm target. Nhưng trong một ngày có xu hướng mạnh, mô hình có thể **lặp lại nhiều lần theo cùng một hướng** — đây là biến thể multi-leg continuation.

- **Single-leg entry:** một chu kỳ 7 bước, một entry, một target; phù hợp với ngày sideway/range hoặc khi chỉ có một cơ hội A+ rõ ràng.
- **Multi-leg continuation:** sau khi chu kỳ 7 bước đầu tiên hoàn tất và target internal bị chạm, giá tạo ra một **dealing range mới** (thường nhỏ hơn) ngay trong nhịp trend đang chạy; nhịp retrace tiếp theo lại tạo ra một sweep nhỏ + displacement mới + FVG mới trong nội bộ trend đó → đây thực chất là chạy lại 7 bước ở một "vòng lặp" nhỏ hơn (nested cycle) mà không cần chờ giá quay lại bias gốc.
- Điều kiện bắt buộc để coi là multi-leg hợp lệ (không phải chase): sau mỗi leg, **dealing range phải được re-map lại** dựa trên displacement mới nhất — xem chi tiết tại [[37 - Re-mapping Dealing Range sau Displacement]]. Nếu không re-map, trader dễ nhầm lẫn giữa "continuation hợp lệ" và "chase trend đã muộn".
- Quản trị rủi ro cho multi-leg: mỗi leg vẫn phải tuân thủ risk ≤0.5%/lệnh độc lập; không cộng dồn size chỉ vì "đang đúng trend"; chỉ vào leg tiếp theo nếu leg đó **đi qua đủ 7 bước riêng của nó** (đặc biệt vẫn cần một sweep nhỏ nội bộ, không chỉ có displacement).

> [!warning]
> Multi-leg continuation KHÔNG có nghĩa là "cứ trend là vào thêm". Mỗi leg mới vẫn phải có sweep + displacement + FVG riêng. Vào thêm chỉ vì "đang thắng, muốn nhồi lệnh" mà bỏ qua sweep nội bộ là chase, không phải multi-leg hợp lệ.

### Mô hình lồng trong AMD đa khung thời gian (Nested AMD)

![[ICT2022-Nested-AMD-Diagram.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ 3 tầng lồng nhau kiểu "hộp trong hộp": tầng ngoài cùng là một chu kỳ AMD Daily (Accumulation–Manipulation–Distribution) trải dài cả phiên; bên trong pha Manipulation/Distribution của tầng Daily, vẽ một chu kỳ AMD Hourly hoàn chỉnh thu nhỏ; và bên trong pha Manipulation/Distribution của tầng Hourly đó lại vẽ tiếp một chu kỳ AMD 5-phút hoàn chỉnh. Dùng màu khác nhau cho mỗi tầng và ghi chú rõ "Daily AMD ⊃ Hourly AMD ⊃ 5-min AMD". Đây là sơ đồ khái niệm minh họa tính fractal của mô hình, không phải chart giá thật.

> [!important] Đây là cách nhìn nâng cao nhất về mô hình — tính chất fractal
> ICT 2022 Model không chỉ chạy một lần trên một khung thời gian. Vì AMD (Accumulation – Manipulation – Distribution, xem [[02 - AMD]]) có tính **fractal**, một chu kỳ AMD lớn trên Daily luôn CHỨA nhiều chu kỳ AMD nhỏ hơn trên Hourly, và mỗi chu kỳ Hourly đó lại chứa nhiều chu kỳ AMD nhỏ hơn nữa trên M5. Bước Sweep + Displacement của ICT 2022 Model thực chất là cách gọi tên hành vi giá tại pha Manipulation → Distribution, ở BẤT KỲ tầng nào trong cấu trúc lồng này.

- **Daily AMD:** Accumulation thường là phiên Á (range hẹp), Manipulation là sweep thanh khoản đầu London/NY, Distribution là move chính trong ngày (thường London hoặc NY session) — đây là bias/draw on liquidity ở bước 1–2 của mô hình.
- **Hourly AMD (lồng trong pha Manipulation/Distribution của Daily):** trong chính nhịp di chuyển chính của ngày, vẫn có các chu kỳ tích lũy–thao túng–phân phối nhỏ hơn theo giờ — mỗi chu kỳ này có thể tự nó là một setup ICT 2022 Model đầy đủ (sweep nhỏ + displacement nhỏ + FVG nhỏ) dùng để refine entry cho hướng Daily.
- **5-phút AMD (lồng trong pha Manipulation/Distribution của Hourly):** đây là nơi entry thực tế thường diễn ra — một chu kỳ AMD cực ngắn cho phép xác định điểm sweep + displacement chính xác tới từng nến M1–M5, tối ưu hóa stop loss và điểm vào so với chỉ dùng H1.
- **Ứng dụng thực dụng:** khi phân tích đa khung thời gian (xem mục 4 phía trên), thực chất bạn đang **xác định vị trí hiện tại trong 3 tầng AMD lồng nhau** — D1 cho biết đang ở pha nào của AMD lớn, H1 cho biết đang ở pha nào của AMD vừa, M5/M1 cho biết đang ở pha nào của AMD nhỏ nhất để bấm entry. Một setup A+ thực sự mạnh là khi **cả 3 tầng đều đang ở pha Manipulation→Distribution cùng hướng** (confluence đa tầng), không chỉ một tầng.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Đi qua đủ chuỗi: Bias → Sweep → Displacement/MSS → FVG → Entry (retrace) → Target.
- [ ] Liquidity sweep rõ ràng trước displacement.
- [ ] FVG sạch, đúng premium/discount, đồng hướng bias.
- [ ] Entry tại retrace về FVG (quanh CE), không chase.
- [ ] Stop ngoài sweep; target pool rõ; R:R đạt kế hoạch.
- [ ] (Lý tưởng) trong kill zone, có confluence OB/OTE.

### Setup bị vô hiệu khi
- [ ] Thiếu liquidity sweep → không phải ICT 2022.
- [ ] Displacement yếu / không để lại FVG.
- [ ] Giá **đóng nến xuyên qua FVG** (acceptance) → POI invalid.
- [ ] Entry ngược bias / sai premium-discount.
- [ ] Vào bằng cách chase, bỏ bước retrace.

### Mức độ "đủ chuỗi"

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Đủ Bias + Sweep + Displacement + FVG + retrace | **A+ setup** | Thực thi theo plan |
| Có sweep + displacement nhưng FVG đã bị lấp | **Chờ POI khác** | Tìm FVG/OB tiếp theo, đừng ép |
| Có FVG + MSS nhưng KHÔNG có sweep | **Không đủ chuỗi** | Bỏ; xác suất thấp |
| Đủ chuỗi nhưng ngoài kill zone | **Hạ cấp** | Giảm size hoặc bỏ tùy quy tắc |

> [!note]
> ICT 2022 Model là "bản đồ tổng" còn các note khác là "địa danh": khi bí, hãy về đây để kiểm tra mình đang ở bước nào và thiếu mắt xích gì. Phần lớn lỗi đến từ **bỏ qua bước 3 (sweep)** hoặc **bỏ qua bước 6 (retrace)**.

---

## 6. Ví dụ chart

### Ví dụ đúng — Đủ chuỗi: Sweep → MSS+Displacement → FVG retrace → Target
![[ICT-2022-Model-Example-Correct.png]]

**Mô tả:**
HTF bias Bullish, draw on liquidity là BSL phía trên. Giá retrace vào discount. **(1)** Một cú **sweep SSL** quét đáy ngắn hạn rồi reclaim. **(2)** Ngay sau đó là **displacement tăng** phá swing high (MSS bullish), để lại một **bullish FVG**. **(3)** Giá retrace về FVG (quanh CE) → **entry**; stop dưới điểm sweep. **(4)** Giá chạy về **BSL target**.

**Vì sao đây là ví dụ tốt:**
- Đi qua **đủ chuỗi** theo đúng thứ tự.
- Liquidity sweep xảy ra TRƯỚC displacement.
- Entry ở bước **retrace về FVG**, đúng discount, không chase.
- Stop logic ngoài sweep; target là pool liquidity rõ (BSL).

### Ví dụ sai / dễ nhầm — Chase displacement, không sweep, vào ở premium ngược bias
![[ICT-2022-Model-Example-Wrong.png]]

**Mô tả lỗi:**
Bias HTF là Bearish (draw thật là SSL phía dưới). Trader thấy một nhịp **displacement tăng** và **Long ngay ở premium** vì "có MSS + sắp có FVG". Nhưng **không hề có liquidity sweep** trước đó, entry ở **sai phía (premium)**, **ngược bias**, và **không chờ retrace**. Giá đảo xuống tiếp tục theo bias bearish về SSL; stop bị quét.

**Bài học:**
- Không có **liquidity sweep** thì không phải setup ICT 2022 — bỏ.
- Displacement để **xác nhận**, không phải để chase; entry ở **retrace về FVG**.
- Luôn kiểm tra **bias + premium/discount** trước khi vào.

---

**Confluence nâng cao (mục 8):**
- [[42 - SMT Divergence]]
- [[40 - Macro Times]]
- [[41 - Change in State of Delivery]]
- [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]
- [[04 - Breaker Block]]
- [[07 - Unicorn Model]]
- [[17 - Inverse Fair Value Gap - iFVG]]
- [[31 - Standard Deviation]]
- [[15 - Inducement]]
- [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[10 - Consequent Encroachment (Mean Threshold)]]
- [[23 - New Day Opening Gap]]
- [[24 - New Week Opening Gap]]
- [[43 - Position Sizing]]

### Sequence mẫu — ICT 2022 Long (đầy đủ)
```text
(1) HTF Bullish Bias + Draw on liquidity = BSL
(2) Giá ở Discount của HTF dealing range
(3) Liquidity Sweep SSL (+ reclaim)
(4) Displacement tăng phá cấu trúc (MSS) → tạo Bullish FVG
(5) Giá retrace về FVG (quanh CE), lý tưởng trùng OB/OTE
(6) Entry; Stop dưới điểm sweep / dưới FVG
(7) Target: Internal liquidity → External BSL
(+ Kill zone London/NY, + đồng hướng AMD distribution)
```

### Sequence mẫu — ICT 2022 Short (đầy đủ)
```text
(1) HTF Bearish Bias + Draw on liquidity = SSL
(2) Giá ở Premium của HTF dealing range
(3) Liquidity Sweep BSL (+ reclaim)
(4) Displacement giảm phá cấu trúc (MSS) → tạo Bearish FVG
(5) Giá retrace về FVG (quanh CE), lý tưởng trùng OB/OTE
(6) Entry; Stop trên điểm sweep / trên FVG
(7) Target: Internal liquidity → External SSL
(+ Kill zone London/NY, + đồng hướng AMD distribution)
```

> [!note]
> Đây là mô hình "mẹ"; mọi note khác trong vault là một mắt xích của nó. Khi review một trade, hãy soi nó qua 7 bước này — lỗi thường nằm ở một bước cụ thể bị bỏ qua, và đó là dữ liệu vàng để sửa.

---

## 8. Confluence Stack & POI nâng cao — nâng cấp mô hình

![[ICT2022-Confluence-Stack-Diagram.png]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ dạng "cột chồng lớp" (stacked layers): nền dưới cùng là **Core Sequence** (7 bước bắt buộc) vẽ như một nền tảng đặc; phía trên xếp chồng 4 lớp confluence trong suốt, mỗi lớp một màu — (1) **POI Quality** (FVG⊂OB⊂Breaker⊂Unicorn), (2) **Timing** (Killzone → Macro time → NWOG/NDOG), (3) **Cross-market** (SMT divergence NQ/ES, EURUSD/GBPUSD/DXY), (4) **Location/Target** (P/D + Std Dev + ERL). Bên phải là một "cột nhiệt kế" chấm điểm chạy từ C (dưới) → A+ (trên) tương ứng số lớp confluence xếp được. Đây là sơ đồ khái niệm minh họa cách "chồng" xác suất, không phải chart giá thật.

> [!important] Confluence KHÔNG thay thế Core Sequence — nó chỉ CHỒNG THÊM xác suất
> Mục này giả định setup đã đi qua đủ chuỗi 7 bước ở mục 1–5 (Bias → Sweep → Displacement/MSS → FVG → Entry retrace → Target). **Confluence là lớp phủ (overlay), không phải lớp thay thế.** Không bao giờ dùng "có SMT" hay "đúng macro time" để bù cho một setup **thiếu sweep** — thiếu core là No Trade bất kể bao nhiêu confluence. Confluence chỉ có tác dụng phân loại **A+ vs A vs B** giữa những setup ĐÃ hợp lệ, và quyết định **size**.

Bốn nhóm confluence dưới đây được sắp theo đúng thứ tự bạn nên kiểm tra sau khi core sequence đã pass: **(8.1) chọn & xếp hạng POI → (8.2) xác nhận chéo thị trường → (8.3) tinh chỉnh timing → (8.4) chấm điểm tổng & quyết định size.**

---

### 8.1 — POI Refinement: chọn và xếp hạng điểm vào khi có nhiều lựa chọn

Bước 5 của mô hình gốc chỉ nói "FVG (POI)". Trong thực tế, sau một displacement thường tồn tại **nhiều POI chồng nhau** (FVG, OB, Breaker, iFVG, OTE zone). Vấn đề không phải "có POI không" mà là "**POI nào chất lượng nhất để đặt entry và stop**". Đây là thang phân loại POI theo độ mạnh (từ yếu → mạnh):

| Hạng | Loại POI | Vì sao mạnh hơn | Note liên kết |
|---|---|---|---|
| 1 (nền) | **FVG đơn thuần** | Chỉ là imbalance 3 nến — bằng chứng "hết đối ứng", nhưng đứng một mình là POI cơ bản nhất | [[Fair Value Gap]] |
| 2 | **FVG + Order Block** | FVG nằm chồng lên OB (nến gốc trước displacement) — vừa có imbalance vừa có vùng lệnh tổ chức | [[Order Block]] |
| 3 | **Breaker Block** | OB đã fail + flip polarity — thêm bằng chứng "đổi trạng thái giao hàng" | [[04 - Breaker Block]] |
| 4 | **iFVG** | FVG bị close-through và đảo cực — xác nhận delivery đã flip, mạnh cho reversal entry | [[17 - Inverse Fair Value Gap - iFVG]] |
| 5 (đỉnh) | **Unicorn (Breaker ∩ FVG)** | Breaker và FVG từ cùng displacement **trùng vùng** — hai loại POI độc lập cùng chỉ một mức giá | [[07 - Unicorn Model]] |

> [!tip] Quy tắc chọn POI khi có nhiều cái chồng nhau
> Ưu tiên POI **có nhiều "lý do" trùng nhau tại cùng một dải giá**, không phải POI gần giá nhất. Thứ tự ưu tiên thực dụng: **Unicorn > iFVG/Breaker có FVG hỗ trợ > FVG+OB > FVG đơn**. Nếu POI hạng cao (Unicorn) nằm sâu hơn một chút nhưng cho R:R vẫn đạt kế hoạch → chọn nó thay vì FVG nông nhưng "trơ trọi".

**Refine entry trong POI bằng CE và OTE (hai lớp lồng nhau):**
- **CE (Consequent Encroachment) = 50% của FVG** ([[10 - Consequent Encroachment (Mean Threshold)]]): mức tham chiếu chuẩn để đặt limit trong FVG. Giá thường phản ứng quanh CE hơn là mép FVG.
- **OTE 62–79% (sweet spot 70.5%)** ([[Optimal Trade Entry]]): đo trên toàn nhịp displacement (từ điểm sweep tới đỉnh/đáy displacement).
- **Confluence entry mạnh nhất = CE của FVG rơi trúng dải OTE 62–79%.** Khi hai lớp này overlap, bạn có một entry vừa "đúng imbalance" (CE) vừa "đúng chiết khấu Fibonacci" (OTE) — đây là điểm vào tối ưu của mô hình.

> [!warning] Bẫy "POI đẹp quá" — liquidity reflexivity
> Một POI trông "sạch và rõ" (FVG đẹp, OB rõ, equal highs ngay trên) chính là nơi **đám đông ICT cũng nhìn thấy** → cụm stop retail dồn về đó → trở thành pool thanh khoản để smart money quét ngược ([[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]). Đối phó: đừng đặt entry/stop tại mép POI "hiển nhiên"; ưu tiên POI có thêm một **inducement** ([[15 - Inducement]]) bị quét trước nó, và đặt stop ngoài vùng thanh khoản mà đám đông sẽ đặt.

**Phân biệt POI internal vs external (dùng để xếp thứ tự target):**
- POI/entry thường nằm ở **IRL (internal range liquidity)** — FVG, OB bên trong dealing range.
- Target đi theo trình tự **external → internal → external**: sau khi sweep ERL, giá lấp IRL (đây là entry), rồi chạy về ERL đối diện ([[16 - Internal & External Range Liquidity (IRL & ERL)]]). Điều này giúp bạn không đặt target "lửng lơ" giữa range.

---

### 8.2 — Multi-market Confirmation: xác nhận chéo thị trường

Đây là lớp confluence mạnh nhất mà mô hình gốc chưa khai thác: **một setup trên một cặp/chỉ số được xác nhận bởi hành vi của cặp/chỉ số tương quan.** Cốt lõi là **SMT Divergence** ([[42 - SMT Divergence]]).

**Các cặp tương quan dùng cho hai thị trường bạn trade:**

| Thị trường trade | Cặp/chỉ số soi kèm | Loại tương quan | Cách đọc SMT |
|---|---|---|---|
| **NQ1 / NAS100** | ES / S&P 500 (SPX) | Thuận (dương) | Đáy: NQ tạo **lower low** nhưng ES chỉ **higher low** (không confirm đáy) → **bullish SMT**. Đỉnh: NQ **higher high** nhưng ES **lower high** → **bearish SMT**. |
| **EURUSD** | GBPUSD | Thuận (dương) | Đáy: một cặp quét đáy mới, cặp kia giữ đáy cao hơn → bullish SMT cho cặp giữ được. |
| **EURUSD / GBPUSD** | DXY (Dollar Index) | Nghịch (âm) | DXY tạo **higher high** nhưng EURUSD **không** tạo lower low tương ứng → **bullish SMT** cho EURUSD (USD đuối). |

> [!important] SMT chỉ có giá trị TẠI điểm sweep, trong bối cảnh HTF PD Array
> SMT không phải chỉ báo chạy nền. Nó chỉ đáng tin khi xuất hiện **đúng lúc bước 3 (Sweep) của mô hình** đang diễn ra, tại một HTF POI/PD array. Quy trình ghép SMT vào ICT 2022 Model:
> 1. Setup tới bước 3: giá đang quét pool thanh khoản (SSL cho Long / BSL cho Short).
> 2. Mở cặp tương quan **cùng khung thời gian** (M15/M5 cho execution) đặt cạnh nhau.
> 3. Kiểm tra: tại chính cú sweep đó, cặp kia **có confirm cùng cực trị không**? Nếu **không confirm** (divergence) → đây là bằng chứng cú sweep là "quét thanh khoản rồi quay đầu", không phải breakout thật.
> 4. SMT divergence + displacement/MSS theo sau = xác nhận sweep chất lượng cao → +điểm confluence.

**Nguyên tắc độ tin cậy:** tương quan càng chặt, SMT càng đáng tin. ES↔NQ và EURUSD↔GBPUSD tương quan rất chặt trong phiên chính → SMT giữa chúng đáng tin. Tương quan yếu đi ngoài killzone hoặc quanh tin riêng lẻ (ví dụ tin chỉ tác động GBP) → giảm trọng số SMT lúc đó.

> [!tip] Reflexivity như một lớp xác nhận ngược
> Ngoài SMT, hãy tự hỏi câu của [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]: *"Nếu tôi là đám đông ICT, tôi sẽ vào ở đâu và đặt stop ở đâu?"* Nếu cú sweep vừa rồi vừa quét đúng cụm stop đó VÀ có SMT divergence xác nhận → xác suất setup là "bẫy đám đông đã hoàn tất, giờ tới lượt move thật" tăng mạnh.

---

### 8.3 — Timing & Macro Precision: bấm entry đúng "giờ thuật toán"

Mô hình gốc chỉ yêu cầu "trong kill zone". Lớp này siết timing xuống **cửa sổ macro 5–20 phút** — nơi IPDA thực sự repricing ([[40 - Macro Times]], [[18 - Kill Zones]]).

**Ba tầng timing, siết dần:**
1. **Killzone (tầng thô):** London Open & NY AM là hai KZ chất lượng nhất cho cả NQ1 và FX.
2. **Macro time (tầng tinh) — giờ ET:** đây là các cửa sổ giá hay sweep/displacement nhất *bên trong* KZ:

| Macro (ET) | Vai trò | Ghi chú thị trường |
|---|---|---|
| 02:33–03:00 | London 1 | FX: nhịp London đầu, sweep Asian range |
| 04:03–04:30 | London 2 (xác suất cao) | FX: nhịp London chính |
| 08:50–09:10 | NY AM 1 | Trùng quanh tin 08:30, cẩn trọng slippage |
| **09:50–10:10** | **NY AM 2 — lõi Silver Bullet** | **NQ1: cửa sổ vàng.** FVG entry hình thành ~09:50, distribution fire ~10:10 |
| 10:50–11:10 | NY AM 3 | Nhịp continuation sau SB |
| 13:10–13:40 | NY PM 1 | Sau lunch, thanh khoản quay lại |
| 14:50–15:10 | NY PM 2 | Dễ biến động quanh FOMC |

3. **Silver Bullet (cửa sổ 1 giờ):** NY AM **10:00–11:00 ET** là bản Silver Bullet mạnh nhất — trùng overlap London–NY, dòng lệnh tổ chức Mỹ triển khai sau khi opening range đã lập. Với NQ1 đây là khung ưu tiên số một; setup ICT 2022 đủ chuỗi rơi vào 09:50–10:10 ET = confluence timing mạnh nhất.

> [!info] Đổi giờ Việt Nam (UTC+7)
> Nhớ trừ DST của Mỹ: khi Mỹ dùng **EDT (mùa hè)**, 10:00 ET ≈ **21:00 VN**; khi Mỹ dùng **EST (mùa đông)**, 10:00 ET ≈ **22:00 VN**. Chi tiết xem bảng trong [[40 - Macro Times]] và [[18 - Kill Zones]].

**Session-open gaps như POI/target bổ sung:**
- **NDOG — New Day Opening Gap** ([[23 - New Day Opening Gap]]): gap 17:00 ET; giá hay quay lại lấp, dùng làm POI/target intraday.
- **NWOG — New Week Opening Gap** ([[24 - New Week Opening Gap]]): gap cuối tuần → thứ Hai; là mức tham chiếu tuần quan trọng, đặc biệt cho FX. Nếu FVG entry của bạn trùng NWOG/NDOG → +điểm confluence.

> [!warning] News filter — bắt buộc cho cả hai thị trường
> Đừng vào entry **sát giờ tin lớn** (NFP, CPI, FOMC, ECB/BoE rate) khi chưa có displacement rõ. Với NQ1, tin 08:30 ET và FOMC 14:00 ET dễ tạo "nến to giả" (volatility, không phải intent — xem khung CLV/wick ở mục 3). Với EURUSD/GBPUSD, tránh entry quanh tin USD (làm nhiễu SMT với DXY) và tin riêng của GBP (phá tương quan EURUSD↔GBPUSD). Quy tắc: có tin đỏ trong 15 phút tới → chờ tin ra + displacement xác nhận rồi mới tính entry.

---

### 8.4 — Confluence Scoring & Risk Filter: chấm điểm và quyết định size

Đây là phần biến toàn bộ mục 8 thành **một quy tắc khách quan, backtest được**. Ý tưởng: tách rõ **GATE (cổng bắt buộc)** khỏi **SCORE (điểm cộng thêm)**.

> [!important] Bước 0 — GATE (không tính điểm, chỉ pass/fail)
> Nếu **bất kỳ** mục nào dưới đây fail → **No Trade**, dừng luôn, không cần chấm điểm:
> - [ ] Bias HTF rõ + draw on liquidity xác định
> - [ ] Có liquidity sweep TRƯỚC displacement (+ reclaim)
> - [ ] Displacement hợp lệ theo khung CLV/wick/acceptance/FVG ở mục 3 (đạt ≥3/4 tiêu chí)
> - [ ] Có FVG sạch từ displacement + entry là **retrace** (không chase)
> - [ ] Entry đúng phía Premium/Discount, đồng hướng bias
> - [ ] Stop có logic (ngoài sweep / đầu kia FVG) + target là pool rõ + R:R ≥ kế hoạch

**Bước 1 — SCORE: mỗi confluence dưới đây +1 điểm** (chỉ chấm sau khi GATE đã pass):

| # | Confluence | +Điểm | Nguồn |
|---|---|---:|---|
| 1 | POI hạng ≥3 (Breaker/iFVG/**Unicorn**), không phải FVG trơ | +1 | 8.1 |
| 2 | CE của FVG trùng dải OTE 62–79% | +1 | 8.1 |
| 3 | SMT divergence xác nhận tại điểm sweep | +1 | 8.2 |
| 4 | CISD xác nhận flip delivery trên LTF | +1 | [[41 - Change in State of Delivery]] |
| 5 | Entry rơi trong **macro time** (không chỉ killzone) | +1 | 8.3 |
| 6 | Trùng NWOG/NDOG hoặc HTF PD array (FVG/OB HTF) | +1 | 8.3 |
| 7 | Target trùng **-2 SD projection** và/hoặc ERL rõ | +1 | [[31 - Standard Deviation]], 8.1 |
| 8 | Có inducement bị quét trước POI (bẫy đám đông đã xong) | +1 | [[15 - Inducement]] |

**Bước 2 — Quy đổi điểm → hạng → size:**

| Tổng điểm | Hạng | Hành động & Size (theo [[43 - Position Sizing]]) |
|---:|---|---|
| ≥ 5 | **A+** | Full size chuẩn **≤0.5%**. Setup ưu tiên cao nhất. |
| 3–4 | **A** | Size chuẩn hoặc giảm nhẹ (0.3–0.5%). Vào nếu R:R tốt. |
| 2 | **B** | Half-size (≤0.25%) hoặc bỏ nếu ngoài killzone. |
| 0–1 | **C** | **No Trade** — chỉ quan sát/ghi chép. GATE pass nhưng thiếu confluence = xác suất chưa đủ để cam kết vốn. |

> [!warning] Ba quy tắc chống lạm dụng điểm số
> 1. **Không "chế" điểm.** Chỉ tick confluence khi nó thực sự có mặt tại thời điểm ra quyết định, không phải nhìn lại sau khi giá đã chạy.
> 2. **GATE luôn thắng SCORE.** 8/8 điểm nhưng thiếu một mục GATE = vẫn No Trade.
> 3. **Điểm cao không được phép phá risk.** A+ vẫn ≤0.5%/lệnh và vẫn tuân thủ daily/weekly loss limit + số lệnh tối đa/ngày. Điểm số quyết định **có vào và size bao nhiêu trong khung cho phép**, không phải cái cớ để nhồi rủi ro.

**Khác biệt thực dụng theo thị trường (áp cho scoring):**
- **NQ1/NAS100:** confluence #3 (SMT với ES) và #5 (macro 09:50–10:10) là hai điểm dễ đạt và giá trị nhất — ưu tiên săn A+ trong Silver Bullet. Do biến động nhanh, một setup chỉ B (2 điểm) ngoài macro time nên **bỏ** thay vì half-size, vì slippage/wick dễ ăn stop.
- **EURUSD/GBPUSD:** confluence #3 (SMT EURUSD↔GBPUSD↔DXY) và #6 (NWOG) rất mạnh nhờ thanh khoản sâu và tương quan chặt. Kiên nhẫn chờ đúng phiên handoff London→NY; sweep ở FX "sạch" hơn nên khi có SMT + macro time, độ tin cậy A+ cao.

> [!tip] Gợi ý frontmatter để log & backtest điểm confluence
> Bổ sung vào frontmatter mỗi trade (nối tiếp mục 13) để Weekly Review thống kê được hiệu quả của từng confluence:
> ```yaml
> confluence_score: 5        # tổng điểm 0-8
> grade: A+                  # A+ | A | B | C
> poi_type: Unicorn          # FVG | FVG+OB | Breaker | iFVG | Unicorn
> ce_ote_overlap: true
> smt_confirm: true          # có SMT tại sweep không
> cisd_confirm: true
> in_macro_time: true        # 8.3
> nwog_ndog_align: false
> sd_target_align: true      # target trùng -2SD/ERL
> idm_swept: true
> correlated_asset: ES       # ES | GBPUSD | DXY
> ```
> Sau 30–50 lệnh, thống kê **win rate & average R theo `grade` và theo từng confluence** — bạn sẽ biết confluence nào thực sự tạo edge trên chính dữ liệu của mình, không chỉ theo lý thuyết. Đây là vòng lặp cải thiện dựa trên số liệu mà cả note này hướng tới.

> [!note] Tóm tắt mục 8 trong một câu
> **Core Sequence quyết định CÓ được vào lệnh không (GATE); Confluence Stack quyết định lệnh đó ĐÁNG bao nhiêu (SCORE → hạng → size). Xác suất được "chồng" chứ không "thay thế".**

---

## Best Practices

> [!summary]
> Đây là các thói quen ở mức chuyên nghiệp / chuẩn prop-firm — thứ phân biệt trader áp dụng ICT 2022 Model một cách nhất quán, có kỷ luật, với trader chỉ biết lý thuyết nhưng thực thi tùy hứng. Mục tiêu cuối: qua được vòng đánh giá prop-firm và giữ được tài khoản funded lâu dài, không chỉ "biết mô hình".

### Quy trình pre-session — map bias & liquidity TRƯỚC khi phiên bắt đầu

- **Không phân tích phản ứng (reactive), luôn phân tích chủ động (proactive) trước phiên.** Việc map bias và pool thanh khoản phải hoàn tất TRƯỚC khi kill zone mở, không phải trong lúc giá đang chạy.
- Trình tự pre-session đề xuất (làm 15–30 phút trước London Open hoặc NY AM):
  1. Xem lại D1/H4: xác định Bias hiện tại, dealing range, premium/discount.
  2. Đánh dấu sẵn TẤT CẢ pool thanh khoản còn "sống" trên H1/M15 (equal highs/lows, đỉnh/đáy phiên trước, old swing points) — cả hai phía, không chỉ phía đồng hướng bias.
  3. Xác định trước 1–2 pool nào **nhiều khả năng bị sweep trước** (dựa trên khoảng cách, độ "đẹp" của equal highs/lows — pool càng rõ ràng, càng dễ hút giá).
  4. Viết sẵn kịch bản Long và kịch bản Short vào Quick Reference Card (mục Appendix) trước khi phiên mở — kể cả kịch bản bạn cho là ít khả năng hơn.
  5. Xác định kill zone sẽ theo dõi và **khung giờ dừng tìm setup mới** nếu không có gì xảy ra (tránh ngồi canh cả ngày).
- Lợi ích: khi sweep + displacement thật sự xảy ra, bạn chỉ cần "khớp" với kịch bản đã viết sẵn thay vì phân tích trong áp lực thời gian thực — giảm mạnh sai số cảm tính.

### Kỷ luật `missing_step` — biến thành nghi thức review hằng tuần

- Trường `missing_step` (xem mục 13) không nên chỉ là một ô điền cho có. Biến nó thành **một nghi thức bắt buộc trong Weekly Review** (xem [[07 - Reviews]]):
  - Cuối mỗi tuần, lọc toàn bộ lệnh thua/BE trong tuần, thống kê `missing_step` xuất hiện bao nhiêu lần cho mỗi giá trị (`sweep`, `displacement`, `retrace`, `target`, `none`).
  - Nếu một giá trị chiếm >40% lệnh thua trong tuần → đây là **ưu tiên sửa số 1** của tuần kế tiếp, ghi thẳng vào note Weekly Review và gắn `[[Mistake - ...]]` tương ứng.
  - Không cho phép để trống `missing_step` ở lệnh thua "vì lười điền" — thiếu dữ liệu này làm hỏng toàn bộ vòng lặp cải thiện dựa trên số liệu mà note này đang xây dựng.
- Sau 4–6 tuần áp dụng nghi thức này liên tục, nên thấy tần suất một `missing_step` cụ thể giảm dần — đây là bằng chứng khách quan cho việc kỷ luật đang cải thiện, không chỉ "cảm thấy tốt hơn".

### Kỳ vọng thực tế: bao nhiêu setup A+ mỗi ngày/tuần

- Với một mô hình đòi hỏi đủ 7 bước (đặc biệt sweep + displacement hợp lệ theo khung ở mục 3), số setup A+ thật sự **hiếm hơn nhiều** so với số lần "trông giống" setup.
- Kỳ vọng thực dụng theo thị trường:
  - NQ1/NDX: khoảng **1–3 setup A+/ngày** trong kill zone chính (NY AM), có ngày 0.
  - EURUSD/GBPUSD: khoảng **3–6 setup A+/tuần** trên mỗi cặp nếu chỉ săn trong London/NY kill zone.
  - XAUUSD: thất thường hơn, phụ thuộc lịch tin — có tuần 1–2 setup rất sạch, có tuần gần như không có gì đạt chuẩn.
- **Ép thêm lệnh để "đủ chỉ tiêu" phá hủy edge thống kê của toàn bộ hệ thống** — mỗi lệnh không đủ chuỗi 7 bước làm loãng win rate và R kỳ vọng đã được backtest, khiến số liệu thật của bạn không còn phản ánh đúng chất lượng mô hình. Số lệnh ít nhưng đúng chuẩn luôn tốt hơn số lệnh nhiều nhưng lẫn lộn.
- Quy tắc thực dụng: đặt **giới hạn cứng số lệnh tối đa/ngày** (ví dụ 1–2 lệnh cho NQ1) và một khi đã chạm giới hạn, chuyển sang chế độ quan sát/ghi chép, không tìm thêm lý do để vào lệnh.

### Scale confidence & size chỉ sau khi đã backtest đủ mẫu

- Không tăng size hoặc confidence cho một biến thể/setup con (ví dụ: multi-leg continuation, Silver Bullet trong kill zone cụ thể, hoặc một market riêng như XAUUSD) chỉ dựa trên vài lệnh live "cảm thấy đúng".
- Chuẩn tối thiểu trước khi tăng size: **≥ 30–50 mẫu backtest** cho đúng biến thể đó, ghi đầy đủ frontmatter theo chuẩn backtest của vault (`type: backtest`, `setup`, `entry_model`, `r_multiple`, `followed_plan`...) và tổng hợp qua [[04 - Backtesting/_Backtest Dashboard]].
- Quy trình scale đề xuất:
  1. Backtest ≥30–50 mẫu → xác nhận win rate và average R dương có ý nghĩa thống kê (không phải may mắn từ mẫu nhỏ).
  2. Forward test với size tối thiểu (risk thấp hơn mức chuẩn ≤0.5%) trên tài khoản demo hoặc live nhỏ trong 15–20 lệnh tiếp theo.
  3. Chỉ sau khi cả hai giai đoạn trên khớp với kỳ vọng đã backtest, mới tăng size về mức chuẩn ≤0.5%/lệnh.
- Không bao giờ nhảy thẳng từ "lý thuyết đọc được" sang "trade full size" — đây là lỗi phổ biến nhất khiến trader mất tài khoản prop-firm ngay trong tháng đầu.

### Amateur habits vs. Professional habits khi thực thi mô hình live

| Khía cạnh | Amateur (nghiệp dư) | Professional (chuyên nghiệp / chuẩn prop-firm) |
|---|---|---|
| Chuẩn bị trước phiên | Mở chart khi kill zone đã bắt đầu, phân tích tại chỗ | Map bias + pool thanh khoản + kịch bản Long/Short xong trước khi kill zone mở |
| Phản ứng với sweep | Vào lệnh ngay khi thấy giá quét đỉnh/đáy | Chờ displacement + MSS xác nhận sau sweep rồi mới hành động |
| Phản ứng với displacement | Chase ngay khi thấy nến lớn | Chờ retrace về FVG (bước 6), không đuổi giá |
| Đánh giá displacement | "Nến to là được" | Kiểm tra CLV, body/wick ratio, acceptance, FVG theo khung ở mục 3 |
| Số lệnh/ngày | Trade nhiều để "kiếm cơ hội", ép setup yếu | Giới hạn cứng số lệnh A+/ngày, chấp nhận ngày 0 lệnh |
| Sau lệnh thua | Vào lệnh gỡ ngay (revenge trade) | Dừng, ghi `missing_step`, chờ setup A+ tiếp theo đúng chuẩn |
| Tăng size | Tăng size sau vài lệnh thắng liên tiếp "cảm thấy tự tin" | Chỉ tăng size sau ≥30–50 mẫu backtest + forward test xác nhận |
| Review cuối tuần | Chỉ nhìn tổng P&L | Thống kê `missing_step`, `chained_fully`, `killzone` theo dữ liệu, không chỉ theo cảm giác |
| Đa thị trường | Áp dụng y hệt một cách trade cho NQ1, FX, XAUUSD | Điều chỉnh size/kỳ vọng/kiên nhẫn theo đặc tính từng thị trường (mục 4) |
| Multi-leg trong trend | Nhồi thêm lệnh chỉ vì "đang đúng trend" | Chỉ vào leg mới nếu có sweep + displacement riêng, re-map dealing range trước |

> [!tip]
> Nếu phải tóm gọn toàn bộ Best Practices thành một câu: **"Chuẩn bị trước, chờ đủ chuỗi, đo lường bằng số liệu — không phải cảm giác."**

---

## 9. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy một mảnh của mô hình
> Phải đủ chuỗi. Một FVG hay một MSS đơn lẻ KHÔNG phải là ICT 2022 Model.

### A. Context (HTF)
- [ ] Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] Draw on liquidity (target) đã xác định.
- [ ] Location đúng: discount (Long) / premium (Short).
- [ ] Pool sẽ bị sweep đã đánh dấu.

### B. Execution (LTF)
- [ ] Đã có liquidity sweep + reclaim.
- [ ] Có displacement phá cấu trúc (MSS) để lại FVG.
- [ ] FVG sạch, xác định CE; (lý tưởng) trùng OB/OTE.
- [ ] Entry ở retrace về FVG, không chase.
- [ ] Stop ngoài sweep / đầu kia FVG.
- [ ] Target pool rõ; R:R đạt kế hoạch; trong kill zone.

### C. Quy tắc "không có lệnh"
- [ ] Thiếu liquidity sweep → không trade.
- [ ] Không có displacement/FVG → không trade.
- [ ] Ngược bias / sai premium-discount → không trade.
- [ ] Chỉ có thể vào bằng chase (không retrace) → không trade.
- [ ] Ngoài kill zone / sát tin lớn → cân nhắc bỏ.

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bỏ qua liquidity sweep | Vào chỉ vì thấy FVG/MSS | Mất mắt xích quan trọng nhất | Bắt buộc có sweep trước displacement |
| Chase displacement | Vào ngay khi thấy nến lớn | Bỏ bước retrace, R:R xấu | Chờ giá retrace về FVG |
| Trade ngược bias | Long/Short ngược HTF | Target ngược, xác suất thấp | Chỉ trade đồng hướng Daily Bias |
| Sai premium/discount | Long ở premium, Short ở discount | Entry chase, R:R xấu | Long ở discount, Short ở premium |
| FVG không từ displacement | Gọi gap thường là FVG | Không có intent | Yêu cầu displacement phá cấu trúc |
| Bỏ qua kill zone | Vào giờ chết | Thanh khoản kém, whipsaw | Săn trong London/NY KZ |
| Stop tùy tiện | Không đặt ngoài sweep/FVG | Bị quét vô lý | Stop logic ngoài điểm sweep |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = pool liquidity đối diện |
| Vào khi thiếu chuỗi | Có vài bước, ép cho đủ | Setup yếu | Đủ 7 bước mới vào; nếu thiếu → No Trade |

---

## 11. Câu hỏi tự kiểm tra

- Mình có đọc thuộc chuỗi 7 bước (Bias→Liquidity→Sweep→Displacement/MSS→FVG→Entry→Target) không?
- Setup này đã đi qua đủ chuỗi chưa, đang thiếu bước nào?
- Đã có liquidity sweep trước displacement chưa?
- FVG có sạch, đúng premium/discount, đồng hướng bias không?
- Entry là retrace về FVG hay đang chase?
- Stop (ngoài sweep) và target (pool đối diện) ở đâu, R:R bao nhiêu?
- Có trong kill zone không?
- Nếu không trade, lý do "No Trade" rơi vào bước nào của mô hình?

---

## 12. Flashcards / Active Recall

### Q1
**Hỏi:** Chuỗi 7 bước của ICT 2022 Model là gì?
**Đáp:** Bias → Draw on liquidity → Liquidity Sweep → Displacement + MSS (để lại FVG) → FVG (POI) → Entry khi retrace về FVG → Target (pool liquidity đối diện).

### Q2
**Hỏi:** Mắt xích nào hay bị bỏ qua nhất và hậu quả?
**Đáp:** Liquidity Sweep (bước 3). Bỏ qua nó khiến trader vào chỉ vì thấy FVG/MSS, thường bị stop quét vì market còn muốn lấy thanh khoản.

### Q3
**Hỏi:** Displacement trong mô hình dùng để làm gì — vào lệnh hay xác nhận?
**Đáp:** Để XÁC NHẬN (phá cấu trúc + để lại FVG). Entry xảy ra ở bước retrace về FVG, KHÔNG chase displacement.

### Q4
**Hỏi:** Entry và stop của ICT 2022 Long đặt ở đâu?
**Đáp:** Entry tại FVG (quanh CE), ở discount; stop ngoài điểm sweep / dưới đầu kia FVG.

### Q5
**Hỏi:** Điều gì làm POI (FVG) của mô hình bị vô hiệu?
**Đáp:** Khi giá đóng nến xuyên qua FVG (acceptance) → FVG invalid; hoặc khi không có sweep/displacement tạo ra nó.

### Q6
**Hỏi:** Làm sao biết một setup KHÔNG phải ICT 2022 Model?
**Đáp:** Nếu thiếu liquidity sweep hoặc thiếu displacement/MSS để lại FVG, hoặc ngược bias / sai premium-discount → không đủ chuỗi → không phải mô hình.

### Q7
**Hỏi:** Mô hình ghép với Kill Zones và AMD ra sao?
**Đáp:** Kill Zones cho biết KHI NÀO săn (London/NY); AMD cho biết PHA (sweep ~ manipulation, displacement ~ distribution). A+ setup là giao điểm của cả ba.
---

## 14. Lesson Learned

### Bài học chính
- ICT 2022 Model là **một chuỗi có thứ tự**, không phải tập hợp tín hiệu rời.
- **Liquidity sweep (bước 3)** là mắt xích sống còn — thiếu nó là không có setup.
- Displacement để **xác nhận**; entry ở bước **retrace về FVG**, không chase.
- Luôn kiểm tra **bias + premium/discount** trước khi vào.
- Mạnh nhất khi có **confluence** (OB/OTE) + trong **kill zone** + đồng hướng **AMD distribution**.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ vào lệnh khi setup đi qua đủ 7 bước.
- [ ] Tôi luôn xác nhận có liquidity sweep trước displacement.
- [ ] Tôi vào ở retrace về FVG, không chase nến lớn.
- [ ] Tôi chỉ Long ở discount / Short ở premium, đồng hướng bias.
- [ ] Khi review thua lỗ, tôi ghi rõ bước nào bị bỏ qua (`missing_step`).

### Câu nhắc nhở khi trade
> **"Quét → Đẩy → Lùi → Vào → Chạy. Thiếu một mắt xích, tôi không có lệnh."**

---
