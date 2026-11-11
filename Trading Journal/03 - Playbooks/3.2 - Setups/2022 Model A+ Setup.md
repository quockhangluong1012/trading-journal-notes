---
type: setup
strategy: ICT 2022 Model
status: active
version: 1.0
markets:
  - NAS100
  - EURUSD
timeframes:
  htf: D1/H4
  mtf: H1/M15
  ltf: M5/M1
killzone: NY AM 20:30–23:00 (giờ VN)
max_risk_percent: 0.5
max_trades_per_day: 2
daily_stop_percent: -1.0
min_rr: 2.0
created: 2026-09-07
updated: 2026-09-07
tags:
  - playbook
  - setup
  - ict-2022
  - a-plus
---

# Playbook A+ — ICT 2022 Model

> [!danger] Luật số 1 của toàn bộ file này
> **GATE luôn thắng SCORE.** Thiếu **một** mục GATE = **No Trade**, bất kể 8/8 điểm confluence. Không có ngoại lệ, không có "nhưng lần này...".
>
> Điểm confluence chỉ trả lời *"lệnh này đáng bao nhiêu size"*. Nó **không bao giờ** trả lời *"có được vào không"*.

> [!info] File này dùng khi nào
> Mở file này **trước mỗi phiên** và giữ nó bên cạnh chart. Mọi ô checkbox phải được tick **tại thời điểm ra quyết định** (hard right edge), không phải tick lại sau khi biết kết quả.
>
> Định nghĩa dùng trong file này là **định nghĩa đã khoá** — xem [[#Phụ lục A — Tham số định nghĩa đã khoá]]. Không dùng định nghĩa khác từ nguồn ngoài; đó chính là nguyên nhân của phần lớn tranh cãi nội tâm giữa phiên.

---

## 0. Bối cảnh cố định (không đổi giữa phiên)

| Hạng mục | Giá trị đã chốt |
|---|---|
| Thị trường | **Chỉ NAS100 và EURUSD.** Không mở symbol khác |
| Killzone | **NY AM 20:30–23:00 giờ VN** (08:30–11:00 ET) |
| Risk/lệnh | **≤ 0.5%** — không ngoại lệ, kể cả A+ |
| Số lệnh tối đa/ngày | **2** |
| Daily stop cá nhân | **−1%** → chạm là tắt máy |
| RR tối thiểu | **2.0** — dưới ngưỡng này bỏ lệnh dù setup đẹp |
| Khung phân tích | D1/H4 → bias · H1/M15 → POI · M5/M1 → trigger |

> [!warning] Vì sao risk 0.5% là bất khả xâm phạm
> Trong 28 lệnh live đã log, **7 lệnh ghi `risk_percent: 5%`** — gấp 10 lần luật. Dưới luật quỹ (daily 5% / total 10%), mức đó kết thúc challenge sau **~2 lệnh thua liên tiếp**. Xem [[07-Mistake-Risk-more-than-0.5-total-account]].
>
> Ở risk 0.5%: cần **20 lệnh thua liên tiếp** mới chạm max loss 10%. Xác suất cháy vì thị trường ≈ 0. Chỉ có thể cháy vì phá luật này.

---

## 1. PHIÊN CHUẨN BỊ — 19:00–20:15 giờ VN (trước killzone)

> [!important] Nguyên tắc: mọi quyết định lớn được ra **trước khi** killzone mở
> Vào phiên chỉ còn việc thi hành kịch bản đã viết. Nếu bạn đang *quyết định* trong lúc nến đang chạy, bạn đã sai quy trình.

### 1.1 — Xác định Dealing Range D1 (bắt buộc, làm trước tiên)

- [ ] Xác định **protected swing high** và **protected swing low** trên D1
  - Biên dealing range lấy theo **protected_swing (LTH)**, **KHÔNG** lấy swing gần nhất
  - *Lý do đã khoá:* lấy "nearest swing" làm midpoint thay đổi theo nhiễu gần nhất → premium/discount nhảy lung tung
- [ ] Ghi lại: `DR_high = ______` · `DR_low = ______`
- [ ] Tính **midpoint = (DR_high + DR_low) / 2 = ______**
- [ ] Giá hiện tại **______** → nằm ở **☐ Premium (trên midpoint)** hay **☐ Discount (dưới midpoint)**

> [!note] Equilibrium band = 0%
> Dùng **hard midpoint 50%**. Không có vùng đệm "gần giữa thì tính là equilibrium". Trên midpoint = premium. Dưới = discount. Chấm hết. Điều này để hai người nhìn cùng một chart phải ra cùng một kết luận.

### 1.2 — Bias D1/H4

- [ ] Cấu trúc D1 hiện tại: ☐ Bullish (chuỗi HH/HL) ☐ Bearish (chuỗi LH/LL) ☐ **Không rõ**
- [ ] Đã có **MSS trên D1** chưa? Nếu có, nó phá **ITH** hay chỉ phá **STH**?
  - Phá **STH** = nhiễu nội bộ, **KHÔNG** đổi bias
  - Phá **ITH** bằng **close** + giữ 3–5 nến = MSS hợp lệ
  - Phá **LTH (protected)** = **đổi bias thật**
- [ ] Kết luận bias: ☐ **Chỉ Long** ☐ **Chỉ Short** ☐ **ĐỨNG NGOÀI**

> [!danger] "Đứng ngoài" là một vị thế hợp lệ
> Bias không rõ = **không trade hôm nay**. Đây không phải thất bại của ngày. `09-Mistake-Wrong-daily-bias` được link **13 lần** từ lệnh live — đây là lỗi tốn kém thứ hai của bạn.

### 1.3 — Draw on Liquidity (DOL) — mục tiêu đi tới

- [ ] Pool thanh khoản **cùng hướng bias** gần nhất: `______` (giá)
- [ ] Loại pool: ☐ Old high/low rõ ☐ Equal highs/lows (trong **10 pips / ~0.08%**) ☐ FVG D1 chưa lấp
- [ ] Pool này có **tên và giá cụ thể** chứ không phải "vùng phía trên"? ☐ Có ☐ Không

> [!warning] Không có DOL = không có target = không vào lệnh
> Target phải là **pool có tên**. "Chạy tiếp lên" không phải target. Xem [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]].

### 1.4 — Thanh khoản ngược hướng (nơi sẽ xảy ra sweep)

- [ ] Pool ngược bias mà giá cần quét **trước khi** đi theo bias: `______`
- [ ] Đây là nơi tôi **chờ sweep**, không phải nơi tôi vào lệnh ngược

### 1.5 — Lịch tin & kịch bản

- [ ] Đã check lịch tin đỏ (ForexFactory). Giờ tin: `______`
- [ ] Viết **2 kịch bản "nếu–thì"** trước khi vào phiên:
  - **Nếu** giá quét `______` rồi có MSS M5 → **thì** tìm entry FVG hướng `______`, target `______`
  - **Nếu** giá đi thẳng tới `______` mà không sweep → **thì** **KHÔNG trade**, chờ phiên sau
- [ ] Đặt price alert tại vùng POI dự kiến — **không dán mắt màn hình**

---

## 2. GATE — 7 bước bắt buộc (pass/fail, không tính điểm)

> [!danger] Đây là cổng. Fail bất kỳ mục nào → No Trade. Không chấm điểm tiếp.

### Bước 1 — Bias HTF rõ + DOL xác định
- [ ] Bias là **Long hoặc Short** (không phải "không rõ")
- [ ] DOL là một **pool có tên, có giá**

### Bước 2 — Giá ở đúng phía Premium/Discount
- [ ] Long → giá đang ở **discount** của dealing range
- [ ] Short → giá đang ở **premium** của dealing range
- [ ] *Vi phạm mục này là lỗi doctrine nặng nhất của người mới.* Xem [[27-Premium-Discount]]

### Bước 3 — Liquidity sweep ĐÃ xảy ra TRƯỚC displacement ⚠️
- [ ] Giá đã **quét qua** một pool thanh khoản ngược hướng (đâm qua đỉnh/đáy có tên)
- [ ] Sau khi quét, giá **từ chối** (quay lại vào trong range)
- [ ] Pool bị quét là pool **có tên** (old high/low hoặc equal levels trong 10 pips), không phải "một cái đỉnh nào đó"

> [!danger] Đây là bước bị bỏ qua nhiều nhất — và tốn kém nhất
> `06-Mistake-Not-Have-Market-Structure-Shift` được link **32 lần** từ lệnh live (lỗi #1). `02-Mistake-Enter-before-liquidity-sweep` link 7 lần. `13-Mistake-Trading-Into-Unswept-Liquidity` link 9 lần từ backtest.
>
> **Thiếu sweep → KHÔNG PHẢI ICT 2022 Model.** Đó là một mô hình khác, và bạn chưa backtest nó.

**Phân biệt Sweep vs Break thật:**

| | Sweep (đúng bước 3) | Break thật (KHÔNG phải sweep) |
|---|---|---|
| Cách xuyên qua | **Wick** xuyên, thân không giữ được | **Close** vượt và **giữ** bên ngoài |
| Nến sau | Quay lại vào trong range | Tiếp tục đi, không lấp lại |
| Ý nghĩa | Hút thanh khoản rồi đảo | Cấu trúc đã đổi thật |
| Hành động | ✅ Đây là tín hiệu chờ MSS | ❌ Bias có thể đã sai — xét lại |

### Bước 4 — MSS/CISD kèm Displacement, đúng hướng bias ⚠️

- [ ] Có **MSS** sau sweep, **ngược hướng cú sweep** và **cùng hướng bias HTF**
- [ ] MSS phá một **ITH (intermediate swing)** — **KHÔNG** phải STH
- [ ] Phá bằng **close**, không phải wick
- [ ] Giữ được **3–5 nến** không bị reclaim
- [ ] MSS nằm **TRONG vùng POI**, không phải giữa range → xem [[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]

> [!important] Phân loại swing 3 tầng — định nghĩa đã khoá, đây là chỗ hay sai nhất
> - **STH (Short Term High/Low)** = 3 nến: đỉnh giữa cao hơn đỉnh trái và phải (tính wick). Đây là **nhiễu nội bộ**. Phá STH **KHÔNG đủ điều kiện MSS**.
> - **ITH (Intermediate)** = một STH có **STH thấp hơn ở cả hai bên**. Phá ITH = **MSS chất lượng**. ✅ Đây là mức bạn cần.
> - **LTH (Long Term / protected)** = một ITH có **ITH thấp hơn ở cả hai bên**, tại HTF PD Array. Phá LTH = **đổi bias**.
>
> *Lý do đã khoá (2026-08-23):* fractal N cố định (2 hoặc 3 bar mỗi bên) bị loại vì **cùng một mức giá nhưng tier khác nhau sẽ bị gom nhầm** — và vì nó tính sweep thành break.

**Displacement — chấm 4 tiêu chí, cần ≥ 3/4:**

| # | Tiêu chí | Ngưỡng hợp lệ | Đạt? |
|---|---|---|---|
| 1 | **CLV** = (Close−Low)/(High−Low) cho nến tăng | **≥ 0.7–0.8** | ☐ |
| 2 | **Body/range** | Thân **≥ 65–70%** range; bấc đối lập nhỏ | ☐ |
| 3 | **Phá swing + acceptance** | Nến sau **không** đóng lại vào trong vùng vừa phá | ☐ |
| 4 | **Để lại FVG** | **≥ 1 FVG** sạch 3 nến | ☐ |

- **≥3/4 → displacement hợp lệ**, đi tiếp
- **1–2/4 → hạ cấp thành "chờ xác nhận thêm"**, KHÔNG vào lệnh
- **Tiêu chí 4 là bắt buộc tuyệt đối:** displacement không tạo FVG thì không có POI để vào → tự động fail

### Bước 5 — POI sạch từ displacement
- [ ] Có **FVG hợp lệ** (3 nến, high nến 1 và low nến 3 không chồng lấn)
- [ ] FVG **chưa bị close-through** (xem invalidation ở mục 6)
- [ ] FVG nằm **đúng phía P/D** và **đồng hướng bias**

### Bước 6 — Entry là RETRACE, không chase ⚠️
- [ ] Tôi đang **chờ giá quay lại** POI, không phải đuổi theo nến displacement
- [ ] Đã đặt **limit order** tại CE, không phải market order

> [!danger] Chase = tự động No Trade
> Xem [[04-Mistake-FOMO-Entry]]. Nếu giá đã đi khỏi POI và không quay lại — **để nó đi**. Sẽ có setup khác. Không có setup nào đáng để phá luật này.

### Bước 7 — Stop có logic + Target là pool rõ + RR ≥ 2.0
- [ ] **SL** đặt ngoài đỉnh/đáy của **cú sweep** (+ buffer spread)
- [ ] **TP** là pool thanh khoản **có tên** (DOL đã xác định ở 1.3)
- [ ] **RR tính ra ≥ 2.0** — tính bằng số, không ước lượng bằng mắt
- [ ] Risk ≤ **0.5%** → khối lượng lot đã tính, không nhẩm

> [!summary] Kết quả GATE
> **Tất cả 7 bước pass** → sang mục 3 chấm điểm.
> **Bất kỳ bước nào fail** → **No Trade.** Ghi vào nhật ký là "setup bị loại ở bước N" — đây là dữ liệu quý (xem mục 8.2).

---

## 3. SCORE — chấm điểm confluence (chỉ sau khi GATE pass)

Mỗi mục có mặt **tại thời điểm ra quyết định** = **+1 điểm**.

| # | Confluence | Điều kiện cụ thể | +1 |
|---|---|---|---|
| 1 | **POI hạng ≥3** | Breaker / iFVG / Unicorn — không phải FVG trơ | ☐ |
| 2 | **CE ∩ OTE** | CE (50% FVG) rơi trúng dải OTE **62–79%** của chân displacement | ☐ |
| 3 | **SMT divergence** | Xác nhận tại điểm sweep (NAS100↔ES · EURUSD↔GBPUSD/DXY) | ☐ |
| 4 | **CISD** | Xác nhận flip delivery trên LTF | ☐ |
| 5 | **Macro time** | Entry rơi trong macro, không chỉ killzone. Mạnh nhất: **21:50–22:10 giờ VN** (09:50–10:10 ET) | ☐ |
| 6 | **NWOG/NDOG hoặc HTF PD array** | FVG entry trùng gap tuần/ngày hoặc FVG/OB khung lớn | ☐ |
| 7 | **Target trùng −2SD và/hoặc ERL rõ** | Không phải target "lửng lơ" giữa range | ☐ |
| 8 | **Inducement đã bị quét trước POI** | Bẫy đám đông đã xong trước khi tới POI của mình | ☐ |

**Tổng điểm: `____ / 8`**

### Quy đổi điểm → hạng → size

| Điểm | Hạng | Hành động & Size |
|---:|---|---|
| **≥ 5** | **A+** | Full size **≤0.5%**. Ưu tiên cao nhất |
| **3–4** | **A** | Size 0.3–0.5%. Vào nếu RR tốt |
| **2** | **B** | Half-size **≤0.25%** — hoặc **bỏ nếu ngoài killzone** |
| **0–1** | **C** | **No Trade.** Chỉ quan sát và ghi chép |

> [!warning] Ba luật chống lạm dụng điểm
> 1. **Không "chế" điểm.** Chỉ tick khi confluence thực sự có mặt lúc quyết định — không tick lại sau khi giá đã chạy.
> 2. **GATE luôn thắng SCORE.** 8/8 điểm mà thiếu một mục GATE = No Trade.
> 3. **Điểm cao không cho phép phá risk.** A+ vẫn ≤0.5% và vẫn tuân thủ daily stop + tối đa 2 lệnh/ngày.

### Khác biệt theo thị trường

**NAS100:**
- Confluence #3 (SMT với ES) và #5 (macro 21:50–22:10 VN) là hai điểm **dễ đạt và giá trị nhất** → ưu tiên săn A+ trong cửa sổ này
- Do biến động nhanh: setup chỉ **B (2 điểm) ngoài macro time nên BỎ** thay vì half-size — slippage và wick dài dễ ăn stop
- Stop cần buffer rộng hơn EURUSD

**EURUSD:**
- Confluence #3 (SMT với GBPUSD/DXY) và #6 (NWOG) rất mạnh nhờ thanh khoản sâu và tương quan chặt
- Sweep "sạch" hơn NAS100 → khi có SMT + macro time, độ tin cậy A+ cao
- Kiên nhẫn chờ đúng phiên handoff London→NY

---

## 4. Chọn POI khi có nhiều lựa chọn chồng nhau

Xếp hạng từ yếu → mạnh:

| Hạng | Loại POI | Vì sao mạnh hơn |
|---|---|---|
| 1 | **FVG đơn thuần** | Chỉ là imbalance 3 nến — POI cơ bản nhất |
| 2 | **FVG + Order Block** | Vừa có imbalance vừa có vùng lệnh tổ chức |
| 3 | **Breaker Block** | OB đã fail + flip polarity |
| 4 | **iFVG** | FVG bị close-through và đảo cực |
| 5 | **Unicorn (Breaker ∩ FVG)** | Hai loại POI độc lập cùng chỉ một mức giá |

> [!tip] Quy tắc chọn
> Ưu tiên POI có **nhiều lý do trùng nhau tại cùng dải giá**, **không phải POI gần giá nhất**.
> Thứ tự: **Unicorn > iFVG/Breaker có FVG hỗ trợ > FVG+OB > FVG đơn.**
> POI hạng cao nằm sâu hơn nhưng RR vẫn ≥2.0 → **chọn nó** thay vì FVG nông trơ trọi.

> [!warning] Bẫy "POI đẹp quá"
> POI trông sạch và rõ (FVG đẹp, OB rõ, equal highs ngay trên) chính là nơi **đám đông cũng nhìn thấy** → cụm stop retail dồn về đó → trở thành pool để smart money quét ngược.
> **Đối phó:** đừng đặt entry/stop tại mép POI hiển nhiên; ưu tiên POI có **inducement bị quét trước nó**. Xem [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]].

### Refine điểm vào trong POI

- **CE (Consequent Encroachment) = 50% của FVG** → mức đặt limit chuẩn. Giá phản ứng quanh CE nhiều hơn mép FVG
- **OTE 62–79%** (sweet spot 70.5%) → đo trên **toàn nhịp displacement**, từ điểm sweep tới đỉnh/đáy displacement
- **Entry mạnh nhất = CE rơi trúng dải OTE** → đây là confluence #2, +1 điểm

---

## 5. Thi hành & quản lý lệnh

### 5.1 — Đặt lệnh
- [ ] **Limit order tại CE** của POI đã chọn
- [ ] SL ngoài đỉnh/đáy cú sweep + buffer spread
- [ ] TP1 = pool gần nhất · TP2 = DOL HTF
- [ ] Khối lượng lot **đã tính bằng công thức**, risk ≤0.5% → xem [[43-Position-Sizing]]

### 5.2 — Quản lý sau khi khớp
- [ ] Giá đi được **1R** → chốt **50%** + dời SL về **breakeven**
- [ ] **KHÔNG** dời SL rộng ra. Bao giờ cũng vậy
- [ ] **KHÔNG** trung bình giá
- [ ] **KHÔNG** gồng quá DOL đã định

### 5.3 — Kết thúc phiên
- [ ] Hết killzone = **hết ngày**, kể cả chưa có lệnh nào
- [ ] **Ngày không lệnh là ngày TỐT** nếu không có setup đạt GATE
- [ ] 23:15 — ghi nhật ký 10 phút, chụp chart, chấm điểm tuân thủ
- [ ] **Không mở lại chart sau đó**

---

## 6. Invalidation — 3 tầng, TUYỆT ĐỐI không trộn lẫn

> [!danger] Định nghĩa đã khoá: ba tầng này phải được giữ tách biệt
> Trộn ba tầng lại là nguyên nhân của hai lỗi ngược nhau: thoát lệnh khi chỉ có setup hỏng (chứ bias vẫn đúng), và giữ bias khi nó đã chết thật.

| Tầng | Nghĩa | Điều kiện | Hành động |
|---|---|---|---|
| **trade_invalidation** | Vị thế cụ thể phải đóng | Giá chạm SL (ngoài cú sweep) | Đóng lệnh. Hết. Không mở lại cùng ý tưởng trong ngày |
| **setup_invalidation** | POI/mẫu xác nhận hết dùng được | Giá **close xuyên toàn bộ FVG** (close_through) | POI này chết. Tìm POI khác — **bias vẫn còn nguyên** |
| **bias_invalidation** | Giả thuyết hướng của khung đó không còn đúng | Phá **LTH (protected swing)** bằng close | **Bias đổi.** Vẽ lại dealing range, làm lại từ mục 1 |

> [!note] FVG chỉ invalidate khi **close** xuyên, không phải wick
> *Lý do đã khoá:* dùng wick_through sẽ khiến FVG bị invalidate quá sớm bởi các cú quét bình thường.
> **iFVG** cần thêm: **retest + hold** — Bullish iFVG: retest FVG rồi close vượt High **và giữ bên trên**.

---

## 7. Danh sách NO-TRADE — gặp bất kỳ mục nào là dừng

- [ ] Bias HTF không rõ
- [ ] Chưa có liquidity sweep
- [ ] Displacement chỉ đạt ≤2/4 tiêu chí
- [ ] Displacement không để lại FVG
- [ ] MSS chỉ phá STH (nhiễu nội bộ), chưa phá ITH
- [ ] MSS nằm giữa range, không trong POI
- [ ] Giá sai phía Premium/Discount so với hướng lệnh
- [ ] Đã lỡ entry, phải chase mới vào được
- [ ] RR < 2.0
- [ ] Điểm confluence ≤1 (hạng C)
- [ ] Đã đủ **2 lệnh trong ngày**
- [ ] Đã chạm **daily stop −1%**
- [ ] Đã thua **2 lệnh liên tiếp** hôm nay
- [ ] Ngoài killzone
- [ ] Sát giờ tin đỏ (±2 phút quanh tin — bắt buộc với The5ers)
- [ ] Đang mệt / mất ngủ / tức giận / muốn gỡ lệnh trước

> [!danger] Mục cuối cùng là mục hay bị bỏ qua nhất
> `01-Mistake-Emotional-revenge-trade` link 5 lần từ lệnh live. Cụm 4 lệnh thua trong ngày **2026-06-17** rồi lệnh thứ 5 thua ngày 06-18 — sau đó dừng trade hẳn 11 tuần. Đó là cái giá của việc bỏ qua mục này.

---

## 8. Biểu mẫu thi hành (copy vào note mỗi setup)

### 8.1 — Setup có vào lệnh

```markdown
## Setup — [SYMBOL] [DATE] [TIME VN]

### Pre-registration (viết TRƯỚC khi biết kết quả)
- Thesis: 
- Invalidation (giá nào thì tôi sai): 
- Target có tên (pool nào): 
- RR tính được: 

### GATE (7/7 bắt buộc)
- [ ] 1. Bias rõ + DOL xác định        → bias: ____  DOL: ____
- [ ] 2. Đúng phía P/D                  → DR: ____–____  mid: ____  giá: ____
- [ ] 3. Sweep đã xảy ra trước          → pool bị quét: ____
- [ ] 4. MSS phá ITH + displacement     → displacement ___/4 tiêu chí
- [ ] 5. POI sạch từ displacement       → loại POI: ____
- [ ] 6. Entry là retrace (limit tại CE) → CE: ____
- [ ] 7. SL logic + TP pool rõ + RR≥2   → SL: ____  TP: ____  RR: ____

### SCORE
1.POI≥3 ☐  2.CE∩OTE ☐  3.SMT ☐  4.CISD ☐  5.Macro ☐  6.NWOG/HTF ☐  7.SD/ERL ☐  8.IDM ☐
**Tổng: ___/8 → Hạng: ___ → Size: ___%**

### Kết quả (điền SAU)
- Exit price thật: ____  |  Spread cost: ____  |  r_net: ____
- Có tuân thủ 100% playbook không? ☐ Có ☐ Không — lệch ở đâu: ____
- first_error_step (nếu thua): ____
```

### 8.2 — Setup bị loại (BẮT BUỘC ghi — đây là dữ liệu quý nhất)

```markdown
## No-Trade — [SYMBOL] [DATE] [TIME VN]
- Bị loại ở bước GATE số: ____
- Lý do cụ thể: ____
- Nếu vào thì kết quả sẽ ra sao (điền sau khi giá chạy xong): ____
```

> [!important] Vì sao phải ghi setup bị loại
> Bản audit devil's advocate của chính bạn đã bắt được **objection O1, mức fatal**: không có nhật ký survivorship. Không ai biết đã xem xét bao nhiêu setup trước khi 22 note kia được viết.
>
> Nếu chỉ ghi lệnh đã vào, **WR không đo được gì** — nó đo "khả năng nhận ra setup rõ khi nhìn lại", không đo edge tại hard right edge. Dòng "setup bị loại" là **thuốc giải duy nhất**.

### 8.3 — Frontmatter để log & thống kê

```yaml
setup: ICT 2022 Model
entry_model: 2022 Model A+ Setup
gate_passed: true
gate_failed_at_step:        # nếu No-Trade thì điền số bước
confluence_score: 5
grade: A+                   # A+ | A | B | C
poi_type: Unicorn           # FVG | FVG+OB | Breaker | iFVG | Unicorn
poi_rank: 5
entry_type: CE
ce_ote_overlap: true
smt_confirm: true
cisd_confirm: true
in_macro_time: true
nwog_ndog_align: false
sd_target_align: true
idm_swept: true
swing_broken_tier: ITH      # STH | ITH | LTH
displacement_criteria_met: 4  # 0-4, cần >=3
entry_price:
exit_price:                 # ĐO THẬT, không copy từ TP kế hoạch
spread_cost:
r_planned:
r_net:                      # đo thật — nếu bằng r_planned thì bạn chưa đo
followed_plan: true
first_error_step:           # bias|draw|sweep|displacement|poi|entry|target
```

> [!danger] `r_net` phải khác `r_planned`
> Trong 22 backtest hiện có, **16/18 lệnh thắng có `r_multiple` bằng đúng `r_planned`**, 0 lệnh BE, spread trống. Đó là ghi lại kế hoạch, không phải đo kết quả. Xem [[12-Mistake-Log-Data-Mismatch-Backtest]].
>
> Một mẫu chỉ được tính vào mục tiêu 200 khi có **exit_price đo thật + spread_cost + r_net**.

---

## 9. Đối chiếu chống lỗi — playbook này chặn lỗi nào

| Lỗi (số lần link từ lệnh live) | Bước nào trong playbook chặn nó |
|---|---|
| [[06-Mistake-Not-Have-Market-Structure-Shift]] — **32** | GATE bước 4 + phân loại STH/ITH/LTH |
| [[09-Mistake-Wrong-daily-bias]] — **13** | Mục 1.2, cho phép kết luận "ĐỨNG NGOÀI" |
| [[07-Mistake-Risk-more-than-0.5-total-account]] — **11** | Mục 0 + GATE bước 7, risk ≤0.5% bất khả xâm phạm |
| [[02-Mistake-Enter-before-liquidity-sweep]] — 7 | GATE bước 3 |
| [[03-Mistake-Entry-When-MSS-not-in-POI-Zone]] — 8 | GATE bước 4, MSS phải trong POI |
| [[05-Mistake-Not-enough-RR]] — 2 | GATE bước 7, RR ≥2.0 |
| [[01-Mistake-Emotional-revenge-trade]] — 5 | Mục 7, daily stop + 2 lệnh thua liên tiếp |
| [[08-Mistake-Weak-Displacement]] | GATE bước 4, ≥3/4 tiêu chí |
| [[13-Mistake-Trading-Into-Unswept-Liquidity]] — 9 (backtest) | GATE bước 3 + mục 1.4 |
| [[04-Mistake-FOMO-Entry]] | GATE bước 6, chase = No Trade |
| [[10-Mistake-FVG-Not-Valid]] | GATE bước 5 + mục 6 close_through |

---

## Phụ lục A — Tham số định nghĩa đã khoá

> [!info] Nguồn: `AI Trading Research Lab/definitions/ict_definitions.json` — 12 term `CONFIRMED`, khoá ngày 2026-08-23
> Các tham số này **đã được quyết định và có lý do ghi lại**. Không đổi giữa phiên. Muốn đổi phải qua quy trình lock-in và ghi vào change log.

| Term | Tham số đã khoá | Đã loại bỏ (và vì sao) |
|---|---|---|
| **swing_point** | 3 tầng **STH/ITH/LTH** theo ICT Advanced Market Structure | Fractal N cố định 2 hoặc 3 bar — cùng price nhưng tier khác nhau bị gom nhầm |
| **BOS** | Xác nhận bằng **close** | wick |
| **MSS** | **close** vượt **ITH** + displacement + giữ **3–5 nến** | wick (tính sweep thành break) · STH (nhiễu) · chỉ LTH (quá chặt, bỏ lỡ MSS hợp lệ) |
| **displacement** | Định tính + tạo **≥1 FVG** | Ratio 1.5x/2x cứng — **chưa backtest**, sẽ khoá sau |
| **FVG** | Invalidate bằng **close_through** toàn vùng | wick_through — invalidate quá sớm |
| **IFVG** | **close_through + retest + hold** | close_through đơn thuần · wick_through |
| **order_block** | **Bắt buộc có FVG ngay sau**; breaker tách riêng | Nến đơn lẻ cũng tính OB |
| **liquidity_pool** | Equal levels trong **10 pips / ~0.08%** | 0 pips (quá chặt) · 20+ pips (gom nhầm swing) |
| **dealing_range** | Biên lấy **protected_swing (LTH)** | Nearest swing — midpoint nhảy theo nhiễu |
| **premium_discount** | Hard midpoint **50%**, equilibrium band **0%** | ±5% band — biến discount thành equilibrium |
| **BPR** | Vùng overlap giữa FVG và IFVG kề nhau | Định nghĩa rộng gồm mọi overlap |
| **invalidation** | **3 tầng tách biệt** (trade/setup/bias) | Trộn chung |

> [!warning] Hai term CHƯA khoá — không được dùng để phán quyết
> **CHOCH** và **DOL** đang ở `DRAFT_NEEDS_CONFIRMATION`. Mọi kết luận dựa trên hai term này là **post hoc**. Nếu một setup phụ thuộc vào chúng, ghi rõ là doctrine gap và phân xử bằng backtest có tiêu chí ex-ante — **không tự chế chuẩn giữa phiên để thắng lập luận**.

---

## Phụ lục B — Nhịp một ngày (giờ VN)

| Giờ | Việc |
|---|---|
| **19:00–20:15** | Chuẩn bị: dealing range D1 → bias → DOL → pool ngược hướng → lịch tin → 2 kịch bản nếu–thì → đặt alert |
| **20:30–23:00** | Killzone NY AM. Chỉ chờ đúng kịch bản. **Tối đa 2 lệnh** |
| **21:50–22:10** | Macro time mạnh nhất (Silver Bullet 09:50–10:10 ET) — ưu tiên săn A+ ở đây, đặc biệt NAS100 |
| **23:15** | Nhật ký 10 phút · chụp chart · chấm tuân thủ · ghi cả setup bị loại |
| **Sau 23:15** | **Không mở lại chart** |

---

## Liên kết
- Mô hình gốc: [[01 - ICT 2022 Model]]
- Checklist ARM/CONFIRM/ENTRY khung thấp: [[LTF Drop-Down Confirmation Checklist (Khi nao xuong khung thap tai OB H1)]]
- Chống bẫy đám đông: [[Anti-Crowd-Trap Checklist (Chống bẫy đám đông ICT)]]
- Rủi ro & circuit breaker: [[Daily Risk & Circuit Breaker Checklist]]
- Position sizing: [[43-Position-Sizing]]
- Lộ trình: [[01 - Roadmap]] · Phương pháp luyện tập: [[04 - Phương pháp luyện tập, vòng lặp AI & giữ động lực]]
