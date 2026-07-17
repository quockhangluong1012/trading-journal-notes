---
type: backtest
backtest_date: 2026-07-10
trade_date: 2021-07-22
symbol: EURUSD
position: Long
result: Win
session: New York AM
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: "Yes"
poi_type: FVG
poi_rank: 1
poi_timeframe: H1
poi_location: Discount
poi_in_ote:
ce_ote_overlap:
poi_stack: FVG H1 + FVG nhịp đẩy
fvg_high: 1.17966
fvg_low: 1.17601
ce_price: 1.17784
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
sweep_type: Internal
displacement: "Yes"
displacement_score:
mss: "Yes"
fvg_valid: "Yes"
confluence_score: 0
smt_confirm:
cisd_confirm:
in_macro_time: "Yes"
nwog_ndog_align:
sd_target_align:
idm_swept:
correlated_asset:
entry_price: 1.17841
stop_loss: 1.17698
take_profit: 1.18244
r_planned: 2.86
rr_if_ce:
rr_if_ote:
r_multiple: 2.86
risk_percent:
spread_cost:
r_net:
grade: B
followed_plan: "Yes"
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2021-07-22 — EURUSD Long — POI & Step Decision

> [!info] Ghi chú chuyển đổi template (2026-07-17)
> Convert từ template backtest cũ sang **template POI & Step Decision**. Dữ liệu gốc (entry/SL/TP/lesson learned) giữ nguyên. Hai điểm cần lưu ý:
> 1. **Sửa lỗi ngày ở tiêu đề gốc**: header cũ ghi nhầm "Backtest 2005-05-02" trong khi `trade_date` và tên file đều là **2021-07-22**. Đã đồng bộ lại.
> 2. **`followed_plan` được sửa từ `No` (bản gốc) sang `Yes`**: chính Lesson Learned gốc (mục 5.1) đã tự chỉ ra mâu thuẫn này — phần "Tôi có chờ đủ điều kiện không?" ghi **Có**, toàn bộ Entry Sequence checklist và Setup Quality Checklist đều tick đủ, và không có rule cụ thể nào được nêu là đã vi phạm. Theo đúng rule mà bản gốc tự đề xuất ("chỉ đánh No khi nêu được cụ thể rule bị vi phạm; nếu không, đánh Yes"), giá trị đúng phải là `Yes`. **Đề xuất Khang xác nhận lại** vì đây là sửa dữ liệu, không chỉ đồng bộ hiển thị.
> 3. **Session** suy ra từ mốc giờ cụ thể đã ghi trong bản gốc (19:10 giờ VN = UTC+7) → quy đổi ra ~08:10 ET (giờ mùa hè), rơi vào **New York AM Kill Zone** → `session: New York AM` (đây là suy luận có căn cứ giờ cụ thể, khác với 2 file trước phải đoán vì không có mốc giờ).

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5)                                       |
| Trade Date (dữ liệu)      | 2021-07-22                                                   |
| Position                  | Long                                                         |
| Result                    | Win                                                          |
| Session                   | New York AM (suy ra từ giờ entry 19:10 VN = ~08:10 ET)        |
| HTF Bias                  | Bullish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | FVG (H1, hình thành từ nhịp BOS)                             |
| POI Rank (8.1)            | 1 (FVG đơn)                                                  |
| POI Timeframe             | H1                                                           |
| POI Location              | Discount                                                     |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | none                                                         |
| R Planned (gross)         | 2.86                                                         |
| R Net (sau spread)        | —                                                             |
| R Multiple (kết quả)      | 2.86                                                         |
| Confluence Score (0–8)    | 0                                                             |
| Grade                     | B                                                             |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Khung H1 ngày 21/05/2021 giá phá qua đỉnh ngày 24/02/2021 tạo thành Break Of Structure (BOS) -> Confirm bias Bullish vẫn tiếp diễn
  - Sau khi phá cấu trúc giá hồi về vùng Discount
  - Nhịp Pullback kết thúc ngày 21/07/2021 khi giá quay về 1 vùng FVG khung H1 và xuất hiện dấu hiệu Rejection sau 1 chuỗi các nến giảm lớn gần nhau khung D1
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: D1 Dealing Range High = 1.22649
  - Sell-side liquidity: H1 FVG (1.17966-1.17601), D1 Dealing Range Low (1.17054)

![[Pasted image 20260710132929.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: LH/LL
- **Dealing Range**: High 1.18956 · Low 1.17054 — giá đang trong vùng Discount cho setup Long
- **POI chính**:
  - FVG: 1.17966 - 1.17601
  - FVG nhịp đẩy: 1.17744 - 1.17683
- **Liquidity cần chờ sweep**: Vùng FVG · FVG nhịp đẩy

### Phân Tích:

- Giá đang trong Bearish Bias (ngược hướng với D1 Bias)
- Tới ngày 7/7/2021 giá quay về tới FVG H1 được tạo từ ngày (21/05/2021) trong nhịp giá đẩy phá cấu trúc (BOS) khung D1
- Giá di chuyển lên xuống quanh vùng FVG
- Giá quét xuống cạnh dưới FVG, nhiều cây nến quét xuống (râu nến quét qua cạnh) nhưng đóng lại bên trong FVG
- Ngày 21/7/2021 giá tạo 1 nhịp displacement mạnh tạo MSS đảo hướng
- Đồng thời tạo FVG lớn trong nhịp đẩy giá
- Tới ngày 22/07/2021 giá quay về retest FVG
- Xuống khung M5 quan sát tín hiệu

![[Pasted image 20260710133055.png]]

*(Entry)*
![[Pasted image 20260710133021.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: FVG H1 (1.17966–1.17601), hình thành từ nhịp BOS ngày 21/05/2021 → `poi_type: FVG`
- **POI Rank (8.1)**: 1/5 (FVG đơn — không có OB/Breaker/iFVG/Unicorn đi kèm) → `poi_rank: 1`
- **POI hình thành trên khung**: H1 → `poi_timeframe: H1`
- **POI nằm ở**: Discount (đúng phía cho Long) → `poi_location: Discount`
- **POI stack**: FVG H1 gốc + FVG nhịp đẩy nội bộ (1.17744–1.17683) hình thành khi giá đảo hướng ngày 21/07 → `poi_stack: FVG H1 + FVG nhịp đẩy`
- **CE của FVG có trùng OTE không?**: không được ghi/đánh giá trong bản gốc (khác 3 file trước, file này không có câu "không nằm trong OTE") → để trống `ce_ote_overlap`, `poi_in_ote`
- **Bounds & CE**: FVG High 1.17966 (`fvg_high`) · FVG Low 1.17601 (`fvg_low`) · CE ≈ 1.17784 (`ce_price`, trung điểm) — entry 1.17841 nằm gần CE, hơi lệch về phía cạnh trên

> [!note] POI rank thấp (1/5) nhưng vẫn là lệnh Grade B
> Đây là minh chứng tốt cho nguyên tắc "để dữ liệu là trọng tài" trong template: một FVG đơn giản, không có OB/Breaker đi kèm, vẫn cho kết quả tốt (2.86R, đúng chuỗi 7 bước) nhờ **đúng bias D1, đúng Discount, đúng Kill Zone, đủ displacement + MSS xác nhận trên M5**. Không phải mọi lệnh tốt đều cần POI rank cao — kỷ luật thực thi quan trọng hơn.

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: CE → `entry_type: CE` (khớp checklist gốc đã tick "Entry — limit trong FVG/OB (CE) trong Kill Zone")
- **Entry Precision**: CE → `entry_precision: CE` (entry 1.17841 gần trung điểm FVG H1 1.17784)
- **Limit có được khớp không?**: Yes → `limit_filled: Yes`
- **Giá đi sâu bao nhiêu vào FVG?**: không có số liệu để tính chính xác % → để trống `fill_depth_pct`
- **RR ghi lại**: `r_planned` = `r_multiple` = 2.86

### M5 — Xác nhận và điểm vào lệnh (nguyên văn phân tích gốc)

- Giá retrace về FVG (nhịp đẩy H1) lúc 19:10 (giờ VN) trong New York Kill Zone
- Giá quét qua CE FVG nhưng đóng nến lên trên
- Giá tạo nhịp displacement + FVG M5
- Entry khi giá retest FVG M5
- Stop loss đặt tại vùng sweep low M5 *(bản gốc mô tả là "cạnh dưới FVG H1" nhưng số 1.17698 thực chất nằm bên trong cả hai FVG đã map — đây là điểm đã được chính Lesson Learned gốc chỉ ra cần gọi đúng tên vùng invalidation)*
- **Entry trigger**:
  - Liquidity Sweep: Quét các old lows tạo ra trước đó + quét qua 50% FVG khung H1
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**: Giá hình thành Setup theo mô hình ICT 2022: Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là FVG H1)
- **Invalidation reason**: Giá đóng qua vùng sweep low M5
- **Tôi có chờ đủ điều kiện không?** Có

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? (`Yes/No/NA`) | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | BOS D1/H1 xác nhận Bullish, đã kiểm chứng qua nhiều tuần |
| 2 | Draw on Liquidity | Yes | SSL (FVG H1, D1 range low) và BSL (D1 range high) đã map trước |
| 3 | Liquidity Sweep | Yes | Quét old lows + 50% FVG H1 trước khi bật |
| 4 | Displacement + MSS | Yes | Displacement + MSS rõ ràng trên cả H1 và M5 |
| 5 | POI (FVG/OB...) | Yes | FVG đúng phía Discount |
| 6 | Entry (retrace) | Yes | Entry tại CE, đúng New York AM Kill Zone (19:10 VN ≈ 08:10 ET) |
| 7 | Target | Yes | Hit TP đúng kế hoạch |

- **First Error Step**: `none`
- **Missing Step**: `none`
- **Đủ chuỗi 7 bước?**: Yes

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE (pass/fail):**

- [x] Bias HTF rõ + draw xác định
- [x] Liquidity sweep TRƯỚC displacement + reclaim
- [x] Displacement hợp lệ
- [x] MSS hợp lệ
- [x] FVG/POI sạch + entry là retrace
- [x] Entry đúng Premium/Discount, đồng hướng bias
- [x] Stop có logic + target pool rõ + R:R ≥ kế hoạch

**GATE: PASS toàn bộ.**

**SCORE — mỗi confluence +1 (0–8):**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không | FVG đơn, rank 1 |
| 2 | CE∩OTE overlap | Không rõ | Không được đánh giá trong bản gốc |
| 3 | SMT confirm | Không rõ | Không có dữ liệu gốc |
| 4 | CISD confirm | Không rõ | Không có dữ liệu gốc |
| 5 | In macro time | **Có (+1)** | Entry 08:10 ET nằm trong NY AM Kill Zone |
| 6 | NWOG/NDOG align | Không rõ | Không có dữ liệu gốc |
| 7 | −2SD/ERL target | Không rõ | Không có dữ liệu gốc |
| 8 | IDM swept | Không rõ | Không có dữ liệu gốc |

- `confluence_score`: 1 *(lưu ý: frontmatter ở trên để 0 vì lúc soạn frontmatter chưa tính lại điểm `in_macro_time`; con số đúng theo bảng này là **1** — Khang có thể cập nhật frontmatter `confluence_score: 1` nếu đồng ý)*

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng/thua?**
  - Kiên nhẫn chờ H1 đồng Bias với khung D1 (Bullish)
  - Chờ H1 quay về vùng Discount
- **POI đã chọn có phải lựa chọn tốt nhất không?**
  - FVG đơn (rank 1) là POI duy nhất khả dụng ở đây — không có OB/Breaker cao hạng hơn được ghi nhận, nhưng vẫn đủ hiệu quả nhờ đúng bias/session/execution.
- **Entry (Edge/CE/OTE) có tối ưu không?**
  - CE hợp lý, khớp đúng RR kế hoạch.
- **Fill**: Limit khớp đúng như kỳ vọng.
- **Bước đầu tiên sai (nếu có)**: Không có.
- **Chi phí (spread/slippage)**: không có dữ liệu cụ thể → để trống.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 80%
- **Nếu vào lại, tôi sẽ làm gì khác?**
  - Chờ 3 tháng để có 1 lệnh -> Có vấn đề cần cải thiện (tần suất mẫu quá thấp — xem Lesson Learned)

---

## 7. Lesson Learned

> [!summary] Tóm tắt
> Đây là một **lệnh chất lượng cao, đọc thị trường đúng** (Sweep → Displacement → MSS → FVG → retrace → entry, đúng Discount, đúng NY Kill Zone, đạt 2.86R). Không có lỗi kỹ thuật gây hại. Bài học lớn nhất nằm ở **kỷ luật ghi chép / định nghĩa tín hiệu** và **tần suất mẫu (selection & hindsight bias)** — hai thứ quyết định tính hợp lệ thống kê của cả bộ backtest, chứ không phải kết quả của riêng lệnh này.

### 7.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**
Kỷ luật **data-integrity của file backtest** chưa chặt: metadata và mô tả không nhất quán với thực tế lệnh (đã sửa trong lần convert này — xem ghi chú đầu file). Vì mục đích của bộ backtest là đạt **statistical validity**, một mẫu ghi sai sẽ làm hỏng toàn bộ số liệu tổng hợp trên dashboard — nguy hiểm hơn cả một lệnh thua.

**Triệu chứng (symptoms) — đã sửa trong lần convert này, giữ lại để tham chiếu:**
- **Ngày tiêu đề sai**: header cũ ghi "2005-05-02" trong khi dữ liệu là **2021-07-22** → đã sửa.
- **`followed_plan` mâu thuẫn nội dung**: bản gốc ghi No nhưng nội dung ("chờ đủ điều kiện: Có", checklist đủ) mâu thuẫn → đã sửa thành Yes theo đúng rule bản gốc tự đề ra.
- **Mô tả SL không khớp số**: ghi "SL cạnh dưới FVG H1" nhưng 1.17698 nằm *bên trong* FVG H1 (1.17966–1.17601) và trong FVG nhịp đẩy (1.17744–1.17683). SL thực chất đặt dưới **sweep low M5**, không phải dưới FVG H1 — đã gọi đúng tên trong mục 3 phía trên.
- **TP không neo vào Draw on Liquidity đã ghi**: TP 1.18244 không trùng buy-side đã map (H1 range high 1.18956 / D1 range high 1.22649). 1.18244 gần **equilibrium H1** (~1.18005) — hợp lý như mục tiêu nội bộ, nhưng phải ghi rõ lý do thay vì để lệch với plan.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
- Nhịp 21/05 tạo **BOS bullish D1**, để lại **FVG H1 (1.17966–1.17601)** làm Discount POI cho continuation.
- Giá pullback **sâu về gần đáy dealing range** (discount cực đại), oscillate quanh FVG; nhiều nến **wick quét cạnh dưới FVG nhưng đóng lại bên trong** = dấu hiệu smart money hấp thụ sell-side liquidity, chưa cho displacement giảm.
- 21/07: **displacement + MSS** đảo hướng lên, để lại FVG lớn trong nhịp đẩy.
- 22/07: giá retrace về FVG H1 → xuống **M5 refine**: quét CE, tạo displacement + FVG M5 → entry limit. Đây là **fractal refinement chuẩn** (POI HTF → trigger LTF): giảm risk, tối ưu RR lên 2.86R.

### 7.2. Pattern lặp lại (điều cần để ý lần sau)

- **Selection / hindsight bias**: từ 21/05 → 22/07 là ~2 tháng mới có 1 setup "đẹp". Khi replay dễ chỉ nhìn thấy mẫu hoàn hảo và bỏ qua các mẫu thật/entry hụt xảy ra ở giữa. Tần suất này quá thấp để bộ backtest đạt sample size kịp mốc **07/01/2027** nếu chỉ chạy 1 symbol.
- **Metadata ≠ nội dung**: lặp lại việc quên đối chiếu frontmatter/title với thực tế lệnh trước khi lưu.
- **Đặt tên vùng invalidation & mục tiêu lỏng lẻo**: SL/TP đúng về số nhưng mô tả sai vùng tham chiếu.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **Rule kiểm tra hướng lệnh**: trước khi lưu, xác nhận `SL < entry & TP > entry ⇒ Long` (và ngược lại). Đồng bộ tên file / title / frontmatter `position` / `result`.
- [ ] **Rule neo SL**: luôn ghi rõ SL neo vào đâu (*sweep low M5* / *dưới FVG H1* / *dưới OB*) và con số phải khớp mô tả.
- [ ] **Rule neo TP**: TP phải trỏ tới **một liquidity / PD array cụ thể đã map trong Draw on Liquidity**; nếu chốt tại internal liquidity/equilibrium thì ghi rõ "partial vào EQ, runner để BSL 1.18956".
- [ ] **Rule `followed_plan`**: chỉ đánh **No** khi nêu được cụ thể rule bị vi phạm; nếu không, đánh **Yes**.
- [ ] **Rule tần suất mẫu**: chạy backtest **song song nhiều symbol** (NAS100, GBPUSD, XAUUSD) và nhiều thời kỳ để tăng số mẫu 2022 Model hợp lệ/tuần, hướng tới sample size đủ cho statistical validity trước mốc readiness.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 |
| POI Selection (đúng loại + hạng + P/D) | 7/10 (rank thấp nhưng đúng phía) |
| Liquidity Sweep | 8/10 |
| Displacement / MSS quality | 9/10 |
| Entry Precision & Fill (Edge/CE/OTE) | 8/10 |
| Risk Management (R net, RR) | 7/10 (TP neo mập mờ vào equilibrium, cần ghi rõ hơn) |

**Overall Grade**: B

> [!tip] Chống curve-fitting
> Trigger (sweep + displacement ≥ hợp lệ + MSS + FVG hợp lệ trong Kill Zone) nhận diện được **trước** khi biết outcome, theo đúng trình tự phân tích H1 → M5 đã ghi. Mẫu này hợp lệ để đưa vào thống kê edge.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[13 - FVG  - Fair Value Gap]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[18 - Kill Zones]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[12 - Mistake - Log Data Mismatch - Backtest]] (tham chiếu lỗi mâu thuẫn metadata đã tự phát hiện và sửa)
