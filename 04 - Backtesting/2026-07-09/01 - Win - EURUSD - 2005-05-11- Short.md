---
type: backtest
backtest_date: 2026-07-09
trade_date: 2005-05-11
symbol: EURUSD
position: Short
result: Win
session: New York AM
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: "Yes"
poi_type: FVG
poi_rank:
poi_timeframe: H1
poi_location: Premium
poi_in_ote: "No"
ce_ote_overlap: "No"
poi_stack: FVG+FVG (BPR)
fvg_high: 1.29884
fvg_low: 1.27889
ce_price: 1.29034
entry_type: CE
entry_precision: CE
limit_filled: "Yes"
fill_depth_pct:
missed_by:
step1_bias_ok: "Yes"
step2_draw_ok: "Yes"
step3_sweep_ok: "Yes"
step4_displacement_ok: "Yes"
step5_poi_ok: "Yes"
step6_entry_ok: "Yes"
step7_target_ok: "Yes"
first_error_step: none
missing_step: none
chained_fully: "Yes"
liquidity_swept: "Yes"
sweep_type: External
displacement: "Yes"
displacement_score:
mss: "Yes"
fvg_valid: "Yes"
confluence_score: 0
smt_confirm:
cisd_confirm:
in_macro_time:
nwog_ndog_align:
sd_target_align:
idm_swept:
correlated_asset:
entry_price: 1.28878
stop_loss: 1.29117
take_profit: 1.28123
r_planned: 3
rr_if_ce:
rr_if_ote:
r_multiple: 2.85
risk_percent:
spread_cost:
r_net:
grade: A
followed_plan: "Yes"
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2005-05-11 — EURUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi template (2026-07-17)
> File này được convert từ template backtest cũ sang **template POI & Step Decision**. Dữ liệu gốc (entry/SL/TP/result/lesson learned) được giữ nguyên. Một số điểm cần lưu ý khi convert:
> 1. **POI thực tế là Balance Price Range (BPR)** — hai FVG đối nghịch chồng lên nhau (Bullish FVG 04/05 bị Bearish FVG 06/05 xuyên qua). Từ vựng chuẩn hiện tại của template chưa có mục riêng cho "BPR", nên tạm xếp `poi_type: FVG` với `poi_stack: FVG+FVG (BPR)` — **đề xuất Khang cân nhắc bổ sung "BPR" vào từ vựng chuẩn** vì đây là POI xuất hiện lặp lại trong bộ backtest.
> 2. **Đã đối chiếu và sửa 1 lỗi tồn đọng**: bảng Backtest Summary bản gốc vẫn ghi R Multiple = 3.03, nhưng chính phần Lesson Learned gốc (mục 5.1) đã tự phát hiện và sửa con số đúng là **2.85R** (blended sau partial TP), khớp với `r_multiple: 2.85` đã có sẵn trong frontmatter. Bảng Summary bên dưới được cập nhật lại cho khớp — không đổi số liệu gốc, chỉ đồng bộ hai nơi đang mâu thuẫn nhau.
> 3. **Session** gốc ghi chung "New York", không có mốc giờ cụ thể → tạm map sang `New York AM` theo từ vựng chuẩn; đây là suy luận, không phải số liệu Khang đã log giờ chính xác.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5)                                       |
| Trade Date (dữ liệu)      | 2005-05-11                                                   |
| Position                  | Short                                                        |
| Result                    | Win                                                          |
| Session                   | New York AM (suy luận, không có mốc giờ gốc)                 |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | FVG (BPR — 2 FVG đối nghịch chồng nhau)                      |
| POI Rank (8.1)            | ngoài thang (BPR không nằm trong thang 8.1 gốc)              |
| POI Timeframe             | H1                                                           |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | none                                                         |
| R Planned (gross)         | 3                                                             |
| R Net (sau spread)        | —                                                             |
| R Multiple (kết quả)      | 2.85 (đã đồng bộ với frontmatter — bản gốc để 3.03)          |
| Confluence Score (0–8)    | 0 (không xác nhận SMT/CISD/macro time/NWOG/-2SD/IDM)         |
| Grade                     | A                                                             |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 đang trong nhịp giảm
  - Cấu trúc chuyển sang LH/LL
  - Giá hiện tại đang trong nhịp hồi, tạo 1 nến displacement lớn
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day/Week High
  - Sell-side liquidity: Giá đang hướng tới vùng
    - Equal Lows: 1.28238
    - Old low trung gian giữa EQL và Dealing Range low: 1.28116
    - Dealing Range Low (nhiều nến ngang nhau liên tiếp với bóng nến dài)

![[Pasted image 20260709140546.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: LH/LL, giá giảm mạnh sâu 1 vùng consolidation
- **Dealing Range**:
  - High: 1.29884
  - Low: 1.27889
  - Giá đang trong vùng BPR, BPR nằm trong vùng Premium => Điều kiện Zone (Premium/Discount) đã có
- **POI chính**: Balance Price Range (đặc biệt vùng CE)
- **Liquidity cần chờ sweep**: CE vùng Balance Price Range: 1.29034

### Phân Tích:

- Giảm mạnh với 1 nến displacement lớn sau đoạn consolidation
- Ngày 04 tháng 5 2005, giá displacement tăng với các nến bullish thân lớn tạo 1 Bullish FVG lớn. Sau đó giá đi ngang trong range
- Đến ngày 6 tháng 5 2005, giá xuất hiện các cây nến Bearish displacement thân lớn đâm xuyên qua Bullish FVG từ ngày 4 => Tạo thành 1 vùng Balance Price Range (BPR khung H1) => POI quan trọng nằm trên 50% range (vùng Premium) => POI chờ giá đã có
- Chờ giá retrace về vùng BPR
- Ngày 11 tháng 5 2005, giá retrace về tới vùng CE của BPR và bật mạnh ra (râu nến quét lên CE BPR và đóng nến gần xuống cạnh dưới) => Liquidity Sweep đã có
- Xuống M5 quan sát

![[Pasted image 20260709140256.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: Balance Price Range (2 FVG đối nghịch chồng nhau: Bullish FVG 04/05 bị Bearish FVG 06/05 xuyên qua) → mapped `poi_type: FVG`, `poi_stack: FVG+FVG (BPR)`
- **POI Rank (8.1)**: BPR không nằm gọn trong thang 1–5 gốc (FVG đơn → FVG+OB → Breaker → iFVG → Unicorn); ước lượng gần nhất là **giữa rank 1–2** vì là 2 lớp FVG chồng nhau nhưng không có OB/Breaker/iFVG đi kèm → để trống `poi_rank`, ghi chú riêng
- **POI hình thành trên khung**: H1 → `poi_timeframe: H1`
- **POI nằm ở**: Premium (đúng phía cho Short) → `poi_location: Premium`
- **POI stack**: FVG+FVG (BPR) — không có OB/Breaker/SMT đi kèm được ghi nhận
- **CE của FVG có trùng dải OTE 62–79% không?**: Không — bản gốc tự nhận "Giá không nằm trong vùng OTE" → `ce_ote_overlap: No`, `poi_in_ote: No`
- **Bounds & CE**: BPR High 1.29884 (`fvg_high`) · BPR Low 1.27889 (`fvg_low`) · CE 1.29034 (`ce_price`)

> [!note] Vì sao POI này mạnh dù thiếu OTE
> Setup này không cần OTE để có edge — sức mạnh đến từ **BPR (2 FVG đối nghịch) nằm đúng trong Premium**, không phải từ Fibonacci retracement. Đúng như Lesson Learned gốc đã chỉ ra: "entry model này neo vào FVG/CE, không phải Fibonacci retracement" — OTE chỉ là điểm cộng khi có, không phải điều kiện bắt buộc.

![[Pasted image 20260709140429.png]]

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: CE → `entry_type: CE` (entry tại CE của FVG M5, đồng thời trùng CE của BPR H1)
- **Entry Precision**: CE (đúng 50%) → `entry_precision: CE`
- **Limit có được khớp không?**: Yes → `limit_filled: Yes`
- **Giá đi sâu bao nhiêu vào FVG?**: không có số liệu FVG M5 cụ thể để tính % → để trống `fill_depth_pct`
- **RR ghi lại**: `r_planned` = 3 · thực nhận (blended sau partial) = 2.85R · `rr_if_ce`/`rr_if_ote` không tách riêng trong bản gốc

### M5 — Xác nhận và điểm vào lệnh (nguyên văn phân tích gốc)

- Giá quét qua CE vùng BPR sau đó bật tăng ra mạnh => Displacement đã có
- Giá tạo các nến displacement mạnh quét các higher low trước đó đồng thời tạo FVG => POI Entry đã có
- MSS đã có
- Stoploss đặt bên trên điểm sweep
- **Entry trigger**:
  - Liquidity Sweep: Quét qua 50% BPR khung H1 + Quét EQH: 1.28912
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - Tâm lý khi vào lệnh lúc đó hơi lo khi cây nến retrace về FVG là 1 nến lớn
- **Entry reason**: Giá hình thành Setup theo mô hình ICT 2022: Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là BPR H1)
- **Invalidation reason**: Giá đóng qua cạnh trên BPR và giữ bên trên
- **Tôi có chờ đủ điều kiện không?** Có

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? (`Yes/No/NA`) | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | D1 Bearish, LH/LL rõ ràng |
| 2 | Draw on Liquidity | Yes | SSL: EQL 1.28238 + Dealing Range Low xác định trước |
| 3 | Liquidity Sweep | Yes | Sweep buy-side qua CE BPR + EQH 1.28912 |
| 4 | Displacement + MSS | Yes | Displacement rõ + MSS xác nhận trên M5 |
| 5 | POI (FVG/OB...) | Yes | BPR đúng phía Premium |
| 6 | Entry (retrace) | Yes | Entry đúng tại CE FVG M5, không chase |
| 7 | Target | Yes | Hit TP, có partial hợp lý |

- **First Error Step**: `none` — cả 7 bước đều đúng tại thời điểm ra quyết định
- **Missing Step**: `none`
- **Đủ chuỗi 7 bước?**: Yes

> [!note] Lưu ý về nhãn Sweep vs MSS (đã tự phát hiện trong bản gốc)
> Lesson Learned gốc đã chỉ ra một lỗi nhãn: "quét các old lows" được ghi cho lệnh Short — với Short, sweep kích hoạt đúng phải là **buy-side sweep** (quét CE BPR + EQH), còn "phá qua các higher low" mới là **MSS**. Bảng 7-step ở trên đã áp dụng đúng phân loại này (sweep = buy-side, bước riêng MSS = phá higher low).

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE (pass/fail):**

- [x] Bias HTF rõ + draw xác định
- [x] Liquidity sweep TRƯỚC displacement + reclaim → sweep_type: External
- [x] Displacement hợp lệ
- [x] MSS hợp lệ
- [x] FVG/POI sạch + entry là retrace
- [x] Entry đúng Premium/Discount, đồng hướng bias
- [x] Stop có logic + target pool rõ + R:R ≥ kế hoạch

**GATE: PASS toàn bộ.**

**SCORE — mỗi confluence +1 (0–8):**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không | BPR không thuộc rank ≥3 trong thang gốc |
| 2 | CE∩OTE overlap | Không | Bản gốc tự nhận "giá không nằm trong vùng OTE" |
| 3 | SMT confirm | Không rõ | Không có dữ liệu gốc |
| 4 | CISD confirm | Không rõ | Không có dữ liệu gốc |
| 5 | In macro time | Không rõ | Không có dữ liệu gốc |
| 6 | NWOG/NDOG align | Không rõ | Không có dữ liệu gốc |
| 7 | −2SD/ERL target | Không rõ | Không có dữ liệu gốc |
| 8 | IDM swept | Không rõ | Không có dữ liệu gốc |

- `confluence_score`: 0

> [!important] Điểm SCORE thấp không mâu thuẫn với Grade A
> Bảng SCORE ở đây chỉ đo các confluence **nâng cao** (SMT, CISD, macro time, NWOG/NDOG, −2SD, IDM) — những thứ **không được ghi trong bản backtest gốc**, không phải vì chúng không tồn tại mà vì lúc đó chưa có thói quen check. Grade A ở mục 8 (Final Grade) đến từ **chất lượng GATE + kỷ luật chờ đủ chuỗi 7 bước**, là thước đo khác với confluence SCORE. Đây là gợi ý cho tương lai: bắt đầu ghi các confluence nâng cao này từ backtest tiếp theo để SCORE có ý nghĩa thống kê.

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP. Điểm cải thiện: Partial Take Profit khi giá quét xuống 1 đáy H1 (take 50% khi đạt 2.55R). Sau đó giá quét thêm 1 đoạn xuống 1 đỉnh cũ nữa (từ đáy TP1 đến đáy TP2 thêm 0.78R)
- **POI đã chọn có phải lựa chọn tốt nhất không?**
  - Có — BPR trong Premium là đúng loại POI mạnh nhất khả dụng ở đây, không có POI hạng cao hơn bị bỏ lỡ theo phân tích gốc.
- **Entry (Edge/CE/OTE) có tối ưu không?**
  - CE là lựa chọn hợp lý; không nằm trong OTE nhưng đây là entry model neo FVG/CE, OTE chỉ là điểm cộng phụ.
- **Fill**: Limit khớp đúng kỳ vọng.
- **Bước đầu tiên sai (nếu có)**: Không có — chuỗi 7 bước đầy đủ.
- **Chi phí (spread/slippage)**: Không có dữ liệu spread cụ thể → để trống.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 90% (giá không nằm trong vùng OTE)
- **Nếu vào lại, tôi sẽ làm gì khác?**
  - Cải thiện tâm lý giao dịch
  - Khi khung M5 giá quét CE BPR và tạo displacement ngược + FVG => entry tại FVG tôi đã khá lo khi giá retrace bằng 2 cây nến thân lớn, gần như không có bóng nến và consolidation 1 đoạn nhỏ trong khoảng CE và cạnh dưới của BPR

---

## 7. Lesson Learned

> [!summary] Kết luận 1 dòng
> Lệnh A-grade thắng nhờ **kiên nhẫn chờ sweep đúng POI Premium (CE của BPR H1) trước khi xuống M5** — đó mới là edge, không phải bản thân cây FVG M5. Vấn đề còn lại nằm ở **kỷ luật ghi nhận dữ liệu & tâm lý**, không nằm ở kỹ thuật đọc chart.

### 7.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**
Edge thật của setup này là **trình tự HTF → LTF được tôn trọng**: giá phải sweep POI cao cấp (CE của BPR H1, nằm trong Premium) *trước*, rồi mới tìm entry trigger trên M5. Việc chờ đúng chuỗi `Premium POI → buy-side sweep → bearish MSS → FVG entry` là nguyên nhân gốc khiến lệnh thắng — không phải vì cây FVG M5 đẹp.

Song song, root cause của những điểm **cần sửa** cũng chỉ có một: **thiếu kỷ luật trong việc định nghĩa và ghi nhận dữ liệu khách quan** (Draw on Liquidity mục tiêu cụ thể, phân biệt Sweep vs MSS, R thực nhận). Điều này không làm hỏng lệnh này, nhưng nếu lặp lại sẽ **phá tính hợp lệ thống kê của cả bộ backtest**.

**Triệu chứng (symptoms) — sinh ra từ root cause (đã sửa ở frontmatter hiện tại, giữ lại để tham chiếu):**
- **Mâu thuẫn bias** (đã sửa): frontmatter hiện đã đúng `htf_bias: Bearish`.
- **R lý tưởng hoá** (đã sửa): `r_multiple` hiện đã đúng 2.85 (blended sau partial), khớp với phần phân tích.
- **Nhầm nhãn Sweep/MSS trên M5**: đã áp dụng đúng ở mục 4 phía trên (sweep = buy-side, MSS = phá higher low).
- **DOL mơ hồ**: chỉ ghi chung "PDH/PDL"; không chỉ ra **một mục tiêu giá cụ thể** mà lệnh hướng tới ban đầu (dù sau đó mục Draw on Liquidity đã liệt kê SSL cụ thể).

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
Ngày 04/05 giá displacement tăng tạo **Bullish FVG**; ngày 06/05 giá displacement giảm xuyên qua chính FVG đó ⇒ hai FVG chồng lên nhau tạo **BPR (Balance Price Range)** trên H1, với **CE = 1.29034 nằm trong Premium** → đây là institutional reference cho phe bán. Khi giá retrace lên CE, râu nến **quét buy-side liquidity** (stop của phe bán sớm + lệnh mua breakout) rồi đóng cửa gần cạnh dưới ⇒ smart money từ chối giá Premium và bắt đầu reprice xuống sell-side. Trên M5, nhịp giảm phá các higher low gần nhất (**MSS**) để lại **Bearish FVG**; CE của FVG M5 là entry tối ưu. Cây nến thân lớn lấp FVG khiến bạn lo lắng thực chất là **dấu hiệu repricing mạnh (bullish cho luận điểm Short)**, không phải mối đe doạ — chỉ invalid nếu **đóng cửa trên cạnh trên BPR**.

### 7.2. Pattern lặp lại (điều cần để ý lần sau)

- **Tâm lý:** lo lắng khi giá retrace vào FVG bằng nến thân lớn/ít bóng nến. Cần chuẩn hoá phản xạ: nến thân lớn lấp FVG là **bình thường và thường là tín hiệu tốt**; chỉ hành động (cắt/không vào) khi giá **đóng qua ngưỡng invalidation** đã định trước, không phản ứng theo cảm giác.
- **Ghi R:** xu hướng log R "đẹp" thay vì R thực nhận. Lặp lại ⇒ expectancy backtest bị thổi phồng.
- **Nhãn khái niệm:** gộp Sweep và MSS. Cần tách bạch mỗi lần.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **Định nghĩa DOL trước khi vào lệnh:** viết rõ mục tiêu TP chính = tên pool + mức giá.
- [ ] **Tách Sweep vs MSS:** với Short, chỉ đánh dấu "Liquidity Sweep" cho **buy-side sweep**; phần phá cấu trúc xuống ghi riêng là **MSS**.
- [ ] **Log 2 con số R:** (a) R nếu giữ full tới TP, (b) **R thực nhận** sau partial. Đồng bộ `r_multiple` frontmatter = R thực nhận.
- [ ] **Chuẩn hoá quy tắc Partial TP:** nếu chọn chốt một phần tại intermediate liquidity, phải **định trước % và mức**, không tuỳ hứng. Backtest riêng để so expectancy giữa "hold full 3R" và "partial 50% @ intermediate + trail" trước khi coi là rule.
- [ ] **QC frontmatter:** trước khi lưu, `htf_bias` phải khớp cả hướng lệnh lẫn phần phân tích; `bias_correct` phải logic với hai giá trị đó.
- [ ] **Cân nhắc bổ sung "BPR" vào từ vựng chuẩn `poi_type`** của template mới — POI này xuất hiện lặp lại và hiện đang bị ép vào `poi_type: FVG` một cách không hoàn toàn chính xác.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 |
| POI Selection (đúng loại + hạng + P/D) | 9/10 |
| Liquidity Sweep | 9/10 |
| Displacement / MSS quality | 9/10 |
| Entry Precision & Fill (Edge/CE/OTE) | 8/10 (đúng CE, không đạt OTE — không phải điểm trừ nặng theo model này) |
| Risk Management (R net, RR) | 7/10 (partial TP hợp lý nhưng thiếu chuẩn hoá quy tắc %) |

**Overall Grade**: A

> [!tip] Chống curve-fitting
> Trigger (sweep buy-side + displacement + MSS + FVG hợp lệ trong Kill Zone) được nhận diện **trước** khi biết outcome, theo đúng trình tự đã ghi trong phần phân tích H1 → M5. Mẫu này hợp lệ để đưa vào thống kê edge.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[13 - FVG  - Fair Value Gap]] · [[04 - Breaker Block]] · [[07 - Unicorn Model]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[12 - Mistake - Log Data Mismatch - Backtest]] (tham chiếu lỗi mâu thuẫn dữ liệu đã tự sửa)
