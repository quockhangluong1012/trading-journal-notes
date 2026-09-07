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
> 1. **POI thực tế là Balance Price Range (BPR)** — hai FVG đối nghịch chồng lên nhau (Bullish FVG 04/05 bị Bearish FVG 06/05 xuyên qua). Từ vựng chuẩn hiện tại của template chưa có mục riêng cho "BPR", nên tạm xếp `poi_type: FVG` với `poi_stack: FVG+FVG (BPR)` — **đề xuất  cân nhắc bổ sung "BPR" vào từ vựng chuẩn** vì đây là POI xuất hiện lặp lại trong bộ backtest.
> 2. **Đã đối chiếu và sửa 1 lỗi tồn đọng**: bảng Backtest Summary bản gốc vẫn ghi R Multiple = 3.03, nhưng chính phần Lesson Learned gốc (mục 5.1) đã tự phát hiện và sửa con số đúng là **2.85R** (blended sau partial TP), khớp với `r_multiple: 2.85` đã có sẵn trong frontmatter. Bảng Summary bên dưới được cập nhật lại cho khớp — không đổi số liệu gốc, chỉ đồng bộ hai nơi đang mâu thuẫn nhau.
> 3. **Session** gốc ghi chung "New York", không có mốc giờ cụ thể → tạm map sang `New York AM` theo từ vựng chuẩn; đây là suy luận, không phải số liệu  đã log giờ chính xác.

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

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

![[EURUSD-20050511-bpr-premium-sweep.svg|760]]

### 9.1. Bản đồ liquidity IRL ↔ ERL tại thời điểm entry

- **POI = BPR (Balance Price Range) H1** — 2 FVG đối nghịch chồng lên nhau, tự thân là IRL. CE = 1.29034 (ghi trong note; tính lại trung điểm hình học của FVG bounds 1.29884/1.27889 cho ra 1.28886 — **lệch ~14.8 pip so với ce_price ghi trong frontmatter**, xem O2 mục 10 để phân tích). Dù dùng số nào, cả hai đều nằm trong Premium của dealing range H1 (High 1.29884 / Low 1.27889 → EQ = 1.28887) — vị trí phía so với midpoint không đổi.
- **Pool đã bị lấy trước entry**: sweep buy-side qua CE BPR + EQH 1.28912 — đây là **ERL** (external, có tên cụ thể: EQH). Đúng chuẩn "named level" mà 07-08/01 còn thiếu.
- **SL 1.29117 nằm ở đâu so với pool tiếp theo phía trên?** Không có mô tả về pool BSL cụ thể nào nằm giữa SL và cạnh trên BPR (1.29884) trong note — đây là khoảng trống dữ liệu. Không đủ căn cứ để xác nhận SL có nằm "trong đường đi tới pool chưa quét" hay không (khác 07-10/02, nơi dữ liệu này rõ). Không suy diễn thêm.
- **Draw ngắn hạn**: SSL = EQL 1.28238 + old low trung gian 1.28116 + Dealing Range Low — đây là pool phía **cùng hướng với TP**, không cùng phía SL. Đây chính xác là điều kiện ngược với lỗi ở 07-10/02 (nơi draw ngắn hạn ngược hướng, cùng phía SL) — một minh chứng thực tế "tốt" cho khái niệm draw gate.

### 9.2. Chất lượng displacement/MSS theo canon

- Cả 2 lớp FVG tạo BPR đều sinh ra từ nến displacement thân lớn (04/05 bullish, 06/05 bearish) — đạt chuẩn "expansion một chiều, để lại imbalance" (SKILL.md § Displacement). MSS trên M5 phá higher low gần nhất, tách bạch đúng với Sweep (đã tự sửa lỗi nhãn Sweep/MSS ở mục 4).

### 9.3. Yếu tố thời gian

- Session New York AM là **suy luận** (note tự nhận, không có mốc giờ gốc) → không đủ để chấm `in_macro_time`, đã để trống đúng cách. Tốc độ resolve: không có timestamp entry→TP cụ thể để đo, chỉ biết có partial TP + runner. Không suy diễn thêm số giờ.

### 9.4. Vị trí entry trong dealing range

- Entry 1.28878 trong range H1 [1.27889, 1.29884]: vị trí = (1.28878-1.27889)/(1.29884-1.27889) ≈ 49.5% — **gần đúng giữa range**, không phải Premium sâu như OTE 0.618-0.786 đòi hỏi. Đây khớp với việc note tự nhận `poi_in_ote: No`. Điểm mạnh không đến từ vị trí Fib mà từ cấu trúc BPR (2 FVG chồng), đúng như ghi chú "OTE chỉ là điểm cộng khi có, không phải điều kiện bắt buộc" — nhất quán nội bộ.

### 9.5. So sánh với lệnh khác cùng mẫu trong vault

- **[[03 - Win - EURUSD - 2021-07-22- Long]]** — cùng entry_type CE, cùng follow đủ 7 bước, nhưng POI rank thấp hơn (FVG đơn, rank 1) mà vẫn Grade B; note này rank BPR (ngoài thang, ước lượng giữa 1-2) nhưng Grade A — chênh lệch grade giữa hai lệnh không đến từ rank POI mà từ chất lượng GATE + kỷ luật, khớp với ghi chú tại mục 5 của cả hai note.
- **[[01 - Win - EURUSD - 2021-05-03- Short]]** (Unicorn, note 07-10/01) — cùng hướng Short, cùng chờ đủ chuỗi 7 bước, nhưng POI rank cao hơn hẳn (Unicorn = 5/5). Cả hai đều win — không đủ mẫu (n=2) để nói rank POI quan trọng hay không so với kỷ luật chờ chuỗi.

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
mode: REVIEW
instrument: EURUSD
date: 2005-05-11
timeframes_provided: "D1/H4, H1, M5 — chỉ mô tả tường thuật + 3 ảnh PNG không đọc được"
verdict: SURVIVES, WEAKENED
evidence_sufficiency: thin
opposite_case_strength: weaker but non-trivial
objections: {fatal: 0, material: 2, minor: 2}
```

**0. Evidence base.** Không có chart đọc được (3 PNG không truy cập nội dung). Fact base = tường thuật + frontmatter. Vì đây là lệnh Win/Grade A, mặc định nghi hindsight cao hơn (theo brief) — cần săn kỹ outcome-as-evidence.

**1. Thesis + load-bearing claim.**
- C1: D1 bias Bearish (LH/LL, nhịp hồi tạo 1 nến displacement lớn).
- C2: H1 hình thành BPR (Bullish FVG 04/05 bị Bearish FVG 06/05 xuyên) nằm trong Premium.
- C3 **(load-bearing)**: Giá retrace về CE BPR, sweep buy-side (CE + EQH 1.28912) rồi bật giảm với displacement + MSS trên M5, tạo FVG entry hợp lệ.
- C4: Entry tại CE FVG M5 = 1.28878, đúng chuỗi 7 bước, không chase.
- C5: Kết quả Win, r_multiple 2.85 (blended, đã tự sửa từ 3.03 sai).

Load-bearing claim: **C3** — toàn bộ Grade A phụ thuộc vào sweep+displacement+MSS trên M5 thật sự xảy ra TRƯỚC entry, không phải được kể lại sau khi biết kết quả thắng.

**2. What survives.** C1, C2 không bị tranh chấp — cấu trúc BPR + Premium là mô tả nhất quán, không cần thông tin tương lai để xác định.

**3. Objections**

**O1 · [HINDSIGHT] · material · attacks C3 (load-bearing)**
Claim: "Cây nến thân lớn lấp FVG khiến bạn lo lắng thực chất là dấu hiệu repricing mạnh (bullish cho luận điểm Short), không phải mối đe doạ" (mục 7.1, cơ chế thị trường).
Fails: đây là diễn giải được viết SAU khi biết lệnh thắng. Tại thời điểm entry, chính note tự ghi "tâm lý khi vào lệnh lúc đó hơi lo khi cây nến retrace về FVG là 1 nến lớn" — nỗi lo là fact tại thời điểm quyết định; câu giải thích "đó là dấu hiệu tốt" chỉ được khẳng định chắc chắn sau khi giá đã đi đúng hướng.
Evidence: mục 3 (nỗi lo tại thời điểm entry) vs mục 7.1 (diễn giải post-hoc khẳng định chắc).
Consequence: nếu coi "nến lớn lấp FVG = dấu hiệu tốt" là một rule tổng quát rút ra từ đây, đó là outcome-as-evidence — cùng một nến lớn lấp FVG có thể là dấu hiệu absorption thất bại nếu lệnh thua ở case khác.
Your best answer: "invalidation rõ ràng đã định trước (đóng qua cạnh trên BPR) — nến lớn không phải invalidation, nên không có lý do dừng theo kế hoạch đã lập." Điều này đúng và làm objection **narrow**: nỗi lo không vi phạm invalidation criteria đã định trước, nhưng câu "đó là dấu hiệu bullish cho short" (tích cực hóa) vẫn là điều chỉ có thể nói chắc sau outcome — giữ ở mức material, không fatal vì không đổi hành động entry.
Retracted by: nếu note có ghi trước một quy tắc khách quan (vd "nến lấp FVG không kèm đóng qua invalidation = tiếp tục giữ lệnh") được viết TRƯỚC lệnh này, objection được retract hoàn toàn.

**O2 · [ARITHMETIC] · material · attacks C2, C4**
Claim: `ce_price: 1.29034` cho BPR bounds `fvg_high: 1.29884` / `fvg_low: 1.27889`.
Fails: CE = (1.29884+1.27889)/2 = 1.28886 theo công thức chuẩn CE (SKILL.md/mean threshold), không phải 1.29034. Chênh 14.8 pip.
Evidence: tính toán trực tiếp từ 2 số đã ghi trong chính frontmatter.
Consequence: nếu CE thật là 1.28886 (gần EQ range 1.28887 hơn), thì vị trí entry 1.28878 gần CE *đúng* (chênh chỉ 0.08 pip) — thực ra CHẶT hơn note tự nhận, không phải lỗi làm yếu thesis, nhưng cho thấy `ce_price` ghi trong frontmatter (1.29034) là không tự-generate từ bounds mà có thể lấy từ nguồn khác (vd CE nội bộ của chỉ riêng nhánh Bearish FVG 06/05, không phải toàn BPR) — cần minh định nguồn gốc con số.
Retracted by: xác nhận `ce_price` là CE của BPR toàn phần hay CE riêng của FVG 06/05 — nếu là cái sau, công thức và số đều đúng, chỉ cần ghi rõ trong note.

**O3 · [UNSUPPORTED] · minor** — `confluence_score: 0` nhưng Grade A: hợp lý theo giải thích mục 5 (SCORE đo confluence nâng cao chưa được log thói quen, không phải bằng chứng thiếu chất lượng). Retracted by: không cần, note đã tự giải thích rõ khoảng cách này.

**O4 · [METHOD] · minor** — Partial TP % (50% tại 2.55R) không được định trước bằng rule cụ thể (note tự nhận ở mục 7.3 "chuẩn hoá quy tắc Partial TP" là rule còn thiếu) → r_multiple 2.85 phụ thuộc một phần vào quyết định discretionary tại thời điểm, chưa đủ để coi là thành phần cố định của edge. Retracted by: backtest 20+ lệnh partial-50%-tại-intermediate so với hold-full, xem 7.3 rule đề xuất.

Đã soạn 4, cắt 0 (tất cả qua bộ lọc discharge/consequence/rebuttal — O3, O4 xuống minor vì không đổi kết luận).

**4. Opposite case.** Từ cùng evidence: "Đây thực chất là một lệnh Short hên vì Premium BPR chỉ là một reaction zone tạm, sweep EQH 1.28912 chỉ là internal liquidity nông (giống 07-10/02), và MSS M5 chỉ được xác nhận NHỜ nhìn lại (giá đã giảm) — nếu bối cảnh khác (killzone khác/session khác) chưa chắc sweep đó đủ trọng lượng."
- Load-bearing của case ngược: "sweep CE BPR + EQH không phải external/structural thật."
- Tự phản bác: EQH là named level cụ thể (1.28912) đã được xác định TRƯỚC trong Draw on Liquidity (mục 1) — không giống 07-10/02, nơi "cạnh trên OB" không có tên cụ thể trước khi bị coi là sweep. Đây khác biệt định lượng rõ ràng.
- Strength label: **weaker but non-trivial** — case ngược không thắng được vì thiếu evidence (EQH đã named trước), nhưng chỉ ra rằng nếu EQH này thực ra không quan trọng bằng buy-side khác cao hơn (note không kiểm tra có pool nào cao hơn EQH 1.28912 chưa bị lấy hay không), case ngược có thể mạnh hơn.
- Distinguishing observable: nếu có một pool BSL named khác nằm giữa entry và SL 1.29117 mà chưa bị lấy tại thời điểm entry — case ngược thắng. Note không cung cấp đủ dữ liệu để loại trừ khả năng này.

**5. Verdict: SURVIVES, WEAKENED.**
Load-bearing claim C3 (sweep EQH named + displacement + MSS) giữ vững — không tìm được cách phá nó bằng evidence có sẵn. Bị làm yếu bởi O1 (hindsight trong diễn giải tâm lý) và O2 (lệch CE arithmetic 14.8 pip cần minh định nguồn). Điều tôi thất bại không phá được: chuỗi sweep(named EQH)→displacement→MSS→FVG trên M5 đúng trình tự canon. Điều critique này không xác lập: liệu có pool BSL named nào khác cao hơn EQH 1.28912 chưa bị lấy tại thời điểm entry (thiếu dữ liệu để loại trừ hoàn toàn opposite case).

**6. Falsification tests**
1. Đọc lại 3 ảnh PNG gốc, xác nhận có pool BSL named nào giữa entry và SL 1.29117 không bị đề cập trong tường thuật. Nếu có → nâng opposite case lên equally viable. Đóng phần "distinguishing observable" ở mục 4.
2. Xác nhận nguồn `ce_price: 1.29034` — hỏi/tra lại xem đây là CE của BPR toàn phần hay của riêng 1 lớp FVG. Đóng O2.
3. Trước lệnh Short/Long tương tự tiếp theo có "nến lớn lấp FVG gây lo lắng", ghi lại rule khách quan TRƯỚC khi biết outcome (đóng qua invalidation hay không) — nếu 5 case tiếp theo áp dụng đúng rule mà không cần hindsight diễn giải "dấu hiệu tốt/xấu" sau đó, đóng O1.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Lệnh Short tại CE của Balance Price Range (BPR) H1 trong Premium, sau khi sweep EQH named + displacement + MSS trên M5, đủ chuỗi 7 bước, Win 2.85R.

**Cần sửa** (load-bearing trước):
- C_CE "ce_price = 1.29034 là CE hợp lệ của BPR" — **AMBIGUOUS** · doctrine (SKILL.md § BPR/CE) không nêu công thức riêng cho CE của BPR (chỉ có CE cho FVG đơn qua Consequent Encroachment) — không rõ 1.29034 tính theo bounds nào → fix: minh định công thức/nguồn số trước khi coi PASS.
- C_rank "BPR không nằm trong thang poi_rank 1-5 gốc" — note đã tự nhận và để trống, xử lý đúng cách (không tự chế rank).

**PASS:** C1 (D1 Bearish LH/LL), C2 (BPR Premium — SKILL.md § Premium/Discount, đúng theo midpoint EQ 1.28887 tính lại, khớp hướng Premium ghi trong note), C3 (Sweep — SKILL.md § Sweep, có named level EQH 1.28912, đạt evidence bar "level có tên và được dùng"), C4 (MSS — SKILL.md § MSS, phá higher low, tách bạch đúng khỏi Sweep), C5 (Displacement — nến thân lớn, imbalance rõ).

**Verdict:** DOCTRINE ALIGNED — load-bearing claim (sweep+displacement+MSS trình tự) PASS đầy đủ theo canon, không claim nào FAIL/HINDSIGHT ở tầng cấu trúc (chỉ có 1 AMBIGUOUS phụ về công thức CE của BPR — chưa có trong bảng thuật ngữ chuẩn). ALIGNED ở đây nghĩa là đúng luật với evidence đã đưa, không phải xác nhận "sẽ luôn thắng".

**Notes:** Doctrine gap — SKILL.md chưa có mục riêng cho "BPR" (chính note gốc mục info đầu file cũng đã tự đề xuất bổ sung); công thức CE cho BPR (2 FVG chồng) chưa được canon hóa — đề xuất bổ sung định nghĩa: CE của BPR = trung điểm của phần chồng lắp giữa 2 FVG, không phải trung điểm toàn bộ bounds ngoài cùng.

---

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật

1. **BPR (2 FVG đối nghịch chồng nhau) là POI mạnh dù không có Fib OTE.** Ví dụ số thật: CE tính lại 1.28886 (hoặc 1.29034 theo note) đều nằm trong Premium của range 1.27889-1.29884 (EQ=1.28887) — sức mạnh không đến từ 0.618-0.786 mà từ chính sự chồng lắp FVG. Tổng quát hóa: với entry model neo FVG/CE (không phải Fibonacci-based), OTE là bonus, không phải điều kiện.
2. **Sweep phải neo vào named level để tính là external/structural.** Ví dụ số thật: EQH 1.28912 đã được xác định TRƯỚC (trong Draw on Liquidity mục 1), không phải gọi tên sau khi thấy giá phản ứng — đối lập trực tiếp với lỗi ở 07-10/02 (sweep "cạnh trên OB" không tên cụ thể trước).

### (b) Bài học quy trình/checklist

- Note tự phát hiện và sửa 2 lỗi log data (R Multiple 3.03→2.85, nhãn Sweep/MSS bị gộp) TRƯỚC KHI hoàn thiện — đây là hành vi kỷ luật ghi chép tốt, cần nhân rộng làm chuẩn quy trình review trước khi đóng file.
- `confluence_score: 0` không mâu thuẫn Grade A — bài học meta: SCORE (confluence nâng cao) và GATE (điều kiện cốt lõi) là 2 thước đo độc lập, không nên gộp lẫn khi đọc dashboard.

### (c) Bài học tâm lý-hành vi

- Nỗi lo tại thời điểm entry ("hơi lo khi cây nến retrace về FVG là 1 nến lớn") được note xử lý ĐÚNG cách: không hành động theo cảm giác, chỉ hành động khi vi phạm invalidation đã định trước. Đây là hành vi kỷ luật cần nhân rộng — đối lập với 07-08/01 nơi cảm giác FOMO thắng invalidation criteria.
- Rủi ro hindsight: diễn giải "nến lớn lấp FVG là dấu hiệu tốt" (mục 7.1) chỉ nói được chắc chắn SAU khi biết outcome — cần tách rõ "cảm giác tại thời điểm" (lo lắng, đúng) và "diễn giải sau khi biết kết quả" (dấu hiệu tốt, cần cẩn trọng) trong lần viết note tiếp theo.

### (d) Rule đề xuất cho Playbook

- [ ] Định nghĩa công thức CE cho BPR = trung điểm phần chồng lắp giữa 2 FVG, khác với CE của FVG đơn — bổ sung vào từ vựng chuẩn `poi_type`.
- [ ] Mọi claim "sweep" phải trỏ tới named level (EQH/EQL/PDH/PDL/OB cụ thể) được xác định TRƯỚC khi entry, không phải gọi tên sau khi thấy phản ứng giá.
- [ ] Khi ghi lại tâm lý tại thời điểm entry, tách 2 trường riêng: "cảm giác lúc đó" và "diễn giải sau kết quả" — không gộp một câu.
- [ ] Chuẩn hoá % và mức partial TP TRƯỚC khi vào lệnh (xem rule đã đề xuất ở mục 7.3 gốc).

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG nên kết luận "nến lớn lấp FVG luôn là dấu hiệu tốt cho hướng lệnh" — đây là outcome-as-evidence điển hình (O1). Nến lớn lấp FVG chỉ có ý nghĩa trong bối cảnh không vi phạm invalidation đã định trước, không phải một quy tắc dự đoán hướng độc lập.
- KHÔNG nên coi Grade A + Win + đủ chuỗi 7 bước là bằng chứng rằng CE của BPR luôn tính đúng theo công thức trung điểm bounds toàn phần — số liệu ce_price trong note (1.29034) không khớp phép tính (1.28886), cần làm rõ trước khi dùng làm chuẩn cho các BPR khác.


### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[13-FVG-Fair-Value-Gap]] · [[04-Breaker-Block]] · [[07 - Unicorn Model]]
- Entry refine: [[10-Consequent-Encroachment-Mean-Threshold]] · [[27-Premium-Discount]]
- Bước: [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[12-Mistake-Log-Data-Mismatch-Backtest]] (tham chiếu lỗi mâu thuẫn dữ liệu đã tự sửa)
