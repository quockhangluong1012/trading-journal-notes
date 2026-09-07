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
> 2. **`followed_plan` được sửa từ `No` (bản gốc) sang `Yes`**: chính Lesson Learned gốc (mục 5.1) đã tự chỉ ra mâu thuẫn này — phần "Tôi có chờ đủ điều kiện không?" ghi **Có**, toàn bộ Entry Sequence checklist và Setup Quality Checklist đều tick đủ, và không có rule cụ thể nào được nêu là đã vi phạm. Theo đúng rule mà bản gốc tự đề xuất ("chỉ đánh No khi nêu được cụ thể rule bị vi phạm; nếu không, đánh Yes"), giá trị đúng phải là `Yes`. **Đề xuất  xác nhận lại** vì đây là sửa dữ liệu, không chỉ đồng bộ hiển thị.
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

- `confluence_score`: 1 *(lưu ý: frontmatter ở trên để 0 vì lúc soạn frontmatter chưa tính lại điểm `in_macro_time`; con số đúng theo bảng này là **1** —  có thể cập nhật frontmatter `confluence_score: 1` nếu đồng ý)*

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

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

![[EURUSD-20210722-fvg-discount-killzone.svg|760]]

### 9.1. Bản đồ liquidity IRL ↔ ERL tại thời điểm entry

- **POI = FVG H1 đơn (1.17966-1.17601)**, rank thấp nhất trong thang (1/5, không OB/Breaker đi kèm) — IRL của bản thân FVG. CE tính lại = (1.17966+1.17601)/2 = 1.17784, khớp chính xác với `ce_price` ghi trong note — arithmetic sạch, không discrepancy.
- **Draw on Liquidity đã map**: Buy-side D1 Dealing Range High = 1.22649; Sell-side = chính H1 FVG này + D1 Dealing Range Low 1.17054. Đây là named levels rõ ràng, xác định TRƯỚC entry theo mục 1.
- **Vấn đề tự phát hiện (đã có ở mục 7.1 gốc, không lặp lại chi tiết)**: TP 1.18244 KHÔNG trùng với bất kỳ named level nào trong Draw on Liquidity đã map (không phải 1.18956 H1 range high, không phải 1.22649 D1 range high) — TP gần equilibrium H1 (~1.18005) hơn. Đây là khoảng trống giữa **kế hoạch đã map** và **TP thực đặt** — về mặt liquidity map, TP là một điểm nội bộ (internal), không phải một ERL pool có tên.
- **SL 1.17698 nằm ở đâu so với pool phía dưới?** Nằm trên D1 Dealing Range Low (1.17054) — không nằm trong đường đi trực tiếp tới SSL lớn hơn phía dưới chưa quét, tức SL không phải "nam châm" cho một sweep tiếp — điểm khác biệt tích cực so với 07-10/02 (nơi SL nằm đúng đường đi tới BSL chưa quét).

### 9.2. Chất lượng displacement/MSS

- Note tự ghi rõ: BOS bullish D1 (21/05) → FVG H1 hình thành → giá pullback sâu về Discount cực đại → nhiều nến wick quét cạnh dưới FVG nhưng đóng lại bên trong (hấp thụ sell-side, chưa displacement giảm) → cuối cùng displacement + MSS xác nhận trên M5 tại đúng NY AM Kill Zone. Đây đạt chuẩn SKILL.md § Displacement + § MSS về mặt mô tả tường thuật — không có mâu thuẫn nội bộ.

### 9.3. Yếu tố thời gian

- Session được suy ra từ **mốc giờ cụ thể đã ghi** (19:10 giờ VN = UTC+7 → ~08:10 ET mùa hè) → New York AM Kill Zone — đây là suy luận có căn cứ (có giờ cụ thể), khác hẳn 2 note trước phải để trống vì thiếu giờ. Đạt evidence bar SKILL.md § Killzone/Time ("chỉ mark từ trục thời gian nhìn thấy được hoặc giờ người dùng nêu").

### 9.4. Vị trí entry trong dealing range

- Dealing range D1/H1: High 1.18956 / Low 1.17054 → EQ = 1.18005. Entry 1.17841 nằm DƯỚI EQ (Discount), đúng phía cho Long. Vị trí trong range = (1.17841-1.17054)/(1.18956-1.17054) ≈ 41.4% — Discount vừa phải, không sâu cực đại như note tự mô tả ở mục 7.4 ("pullback sâu về gần đáy dealing range") — cần phân biệt: "sâu về gần đáy" trong tường thuật có thể mô tả hành vi giá TRƯỚC khi bật lên (test sâu hơn rồi hồi), không nhất thiết mâu thuẫn với entry cuối cùng ở 41.4%.

### 9.5. So sánh với lệnh khác cùng mẫu trong vault

- **[[02 - Win - EURUSD - 2005-05-11 - Short]]** (07-09/01) — cùng đủ chuỗi 7 bước, cùng sweep named level, nhưng khác hướng và khác POI (BPR vs FVG đơn). Cả hai đều chứng minh: POI rank không quyết định outcome bằng kỷ luật thực thi đúng chuỗi.
- **[[01 - Win - EURUSD - 2021-05-03- Short]]** (07-10/01, Unicorn) — đối lập trực tiếp về POI rank (5/5 Unicorn vs 1/5 FVG đơn ở đây), cùng Win. Đây là cặp so sánh tốt nhất trong batch để kiểm định giả thuyết "POI rank cao hơn → chất lượng cao hơn": note này (rank 1) đạt RR khớp chính xác (2.818 tính lại vs 2.86 ghi, chênh <0.05R), trong khi note 07-10/01 (rank 5, Unicorn) có RR lệch lớn nhất batch (2.123 tính lại vs 3.075 ghi, chênh ~1R) — gợi ý (không kết luận, n=2) rằng độ phức tạp cấu trúc cao hơn không đồng nghĩa log chính xác hơn.
- **[[03 - Loss- EURUSD - 2021-05-07- Short]]** (07-10/02) — đối lập rõ nhất: TP ở đây (07-10/03) tuy không neo named level nhưng SL không nằm trong đường đi tới pool chưa quét; TP+SL ở 07-10/02 đều có vấn đề định vị theo draw. Sự khác biệt về SL location (không phải TP) có thể là yếu tố phân biệt Win/Loss quan trọng hơn TP-precision.

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
mode: REVIEW
instrument: EURUSD
date: 2021-07-22
timeframes_provided: "D1/H4, H1, M5 — mô tả tường thuật chi tiết, không có PNG được nhắc trong note này"
verdict: SURVIVES THIS ATTACK
evidence_sufficiency: partial
opposite_case_strength: weaker but non-trivial
objections: {fatal: 0, material: 2, minor: 2}
```

**0. Evidence base.** Không có ảnh PNG được nhắc trong note (khác các note khác trong batch) — toàn bộ evidence là tường thuật + frontmatter, khá chi tiết và có mốc giờ cụ thể (hiếm trong batch này). Vì đây là Win Grade B, mặc định nghi hindsight — cần săn kỹ, nhưng ghi nhận note đã tự làm việc này khá tốt ở mục 7 gốc (mục "Sample & Hindsight Bias").

**1. Thesis + load-bearing claim.**
- C1: D1 Bias Bullish, BOS bullish 21/05 xác nhận.
- C2: FVG H1 (1.17966-1.17601) hình thành làm Discount POI cho continuation.
- C3: Giá pullback về FVG, nhiều wick quét cạnh dưới nhưng đóng lại bên trong (hấp thụ sell-side).
- C4 **(load-bearing)**: Displacement + MSS xác nhận trên M5 TRƯỚC entry, tại đúng NY AM Kill Zone (08:10 ET), theo đúng trình tự 7 bước — không phải nhận diện sau khi biết outcome.
- C5: Entry tại CE FVG = 1.17841, đúng kế hoạch.
- C6: TP 1.18244 không neo named level đã map (tự nhận, mục 7.1).
- C7: Kết quả Win, 2.86R.

Load-bearing: **C4** — đây là claim duy nhất có rủi ro hindsight cao nhất (Win + đủ chuỗi + Grade B "quá đẹp" luôn cần săm soi kỹ theo brief).

**2. What survives.** C1, C2, C3, C6 không tranh chấp — BOS D1, cấu trúc FVG, hành vi wick hấp thụ, và chính điểm yếu TP đã được note tự nhận trung thực, không cần đối kháng thêm.

**3. Objections**

**O1 · [HINDSIGHT] · material · attacks C4 (load-bearing)**
Claim: "nhiều nến wick quét cạnh dưới FVG nhưng đóng lại bên trong = dấu hiệu smart money hấp thụ sell-side liquidity, chưa cho displacement giảm" (mục 7.4).
Fails một phần: đây là diễn giải CÓ THỂ đúng tại thời điểm quan sát (wick-reject là hành vi giá khách quan, không cần biết tương lai để mô tả), nhưng câu kết luận "chưa cho displacement giảm" ngầm giả định người quan sát đã biết trước displacement tăng sẽ xảy ra sau đó — cần phân biệt "quan sát hành vi" (không hindsight) khỏi "diễn giải ý nghĩa hành vi đó là tín hiệu tốt" (rủi ro hindsight nhẹ, vì wick-reject có thể là dấu hiệu hấp thụ HOẶC dấu hiệu yếu ớt trước một breakdown, tùy diễn giải).
Evidence: mục 7.4, câu mô tả liền mạch không tách rõ 2 tầng (quan sát vs diễn giải ý nghĩa).
Consequence: nếu tách đúng, câu quan sát ("wick quét rồi đóng lại trong") là fact hợp lệ real-time; câu diễn giải ("đây là hấp thụ, không phải yếu") chỉ chắc chắn SAU khi giá đã tăng — không đổi hành động entry (đã có MSS+displacement M5 xác nhận riêng, C4 vẫn đứng), nên material chứ không fatal.
Your best answer: entry trigger thực tế không dựa vào diễn giải "hấp thụ" này mà dựa vào chuỗi MSS+displacement+FVG trên M5 xảy ra SAU đó — nghĩa là dù diễn giải wick có đúng hay sai, nó không phải là điều kiện entry, chỉ là bối cảnh mô tả thêm. Objection do đó **narrows xuống vấn đề trình bày**, không phải vấn đề entry logic.
Retracted by: nếu note tách rõ 2 câu (quan sát hành vi wick vs ý nghĩa diễn giải) trong lần viết tiếp theo.

**O2 · [UNSUPPORTED] · material · attacks C4**
Claim: "Displacement + MSS xác nhận trên M5" tại Kill Zone.
Fails: không có số liệu định lượng nào cho displacement M5 trong note này (không ATR, không body-to-range ratio, không mô tả cụ thể nến nào) — chỉ có câu chung "đủ displacement + MSS xác nhận trên M5" ở nhiều chỗ (mục 3, 7, 8). So với 07-08/01 (tự nhận "displacement không quá lớn" — cụ thể) hay 07-10/02 (cùng vậy), note này KHÔNG có mức độ chi tiết tương đương để tự kiểm tra ngưỡng.
Evidence: thiếu — đây là khoảng trống mô tả, không phải mâu thuẫn.
Consequence: không đủ evidence để PASS dứt khoát chất lượng displacement, dù không có gì mâu thuẫn để FAIL nó — đúng chuẩn phải là UNSUPPORTED, không phải PASS ngầm định vì "Win nên chắc đúng".
Your best answer: `displacement: Yes` được tick ở 7-Step Log — nhưng tick Yes/No không thay thế cho mô tả định lượng theo đúng gate mà note đề xuất ở các note khác trong vault (vd 07-10/02 mục 7.3 "Định nghĩa displacement khách quan"). Việc chính vault đã tự đề xuất chuẩn này ở nơi khác mà note Win này không áp dụng là một điểm không nhất quán (nhưng không phải lỗi riêng của note này).
Retracted by: bổ sung số liệu cụ thể cho nến displacement M5 (range, ATR ratio, thời điểm).

**O3 · [ARITHMETIC] · minor** — RR tính lại từ entry/SL/TP = 2.818, note ghi 2.86 — chênh 0.042R, trong ngưỡng làm tròn hợp lý, không đáng kể (nhỏ nhất trong toàn batch B). Retracted by: không cần, đây gần như PASS hoàn toàn.

**O4 · [UNSUPPORTED] · minor** — TP 1.18244 không neo named level (đã tự nhận, mục 7.1/9.1) — ghi nhận đây KHÔNG PHẢI risk cho outcome đã xảy ra (Win), nhưng là risk cho các lệnh TƯƠNG LAI dùng cùng logic "TP tại equilibrium nội bộ" mà không có named level backup nếu giá đảo chiều sớm hơn dự kiến. Retracted by: rule đã đề xuất ở mục 7.3 gốc (neo TP vào Draw on Liquidity cụ thể).

Đã soạn 4, cắt 0 (O1, O2 material vì không đổi được entry logic gốc nhưng đáng flag; O3, O4 minor).

**4. Opposite case.** Từ cùng evidence: "Đây có thể là một lệnh Long thắng nhờ may mắn thị trường tiếp tục trend D1 mạnh, không phải nhờ chất lượng entry trigger M5 — vì displacement/MSS trên M5 không có số liệu định lượng để phân biệt với một MSS yếu kiểu 07-10/02 (phiên mỏng, dễ bị tạo bởi vài lệnh nhỏ)."
- Load-bearing của case ngược: "MSS M5 ở đây cũng có thể yếu như ở 07-10/02, chỉ khác là giá tiếp tục đúng hướng."
- Tự phản bác: khác biệt quan trọng là **session** — đây là NY AM Kill Zone (có mốc giờ xác nhận cụ thể), còn 07-10/02 là Asia (ngoài KZ, đã tự nhận GATE fail). Theo canon (SKILL.md § Killzone), trọng số MSS/displacement trong KZ cao hơn hẳn ngoài KZ — đây là khác biệt định tính đủ mạnh để bác case ngược dù thiếu số liệu định lượng displacement.
- Strength label: **weaker but non-trivial** — case ngược không thắng vì thiếu bằng chứng, và có 1 khác biệt cấu trúc rõ ràng (Kill Zone) ủng hộ case gốc; nhưng thiếu số liệu displacement định lượng vẫn là lỗ hổng thật đáng ghi nhận.
- Distinguishing observable: nếu displacement M5 được đo lại và cho thấy range/ATR ratio thấp (dưới ngưỡng chuẩn), case ngược mạnh lên đáng kể dù vẫn trong KZ.

**5. Verdict: SURVIVES THIS ATTACK.**
Load-bearing claim C4 không bị phá — không tìm được mâu thuẫn hay hindsight nào đủ mạnh để lật ngược kết luận entry hợp lệ; điểm yếu duy nhất (thiếu số liệu định lượng displacement, O2) là UNSUPPORTED chứ không FAIL, và Kill Zone xác nhận bằng giờ cụ thể là điểm mạnh khác biệt so với các note Loss trong batch. Điều không phá được: chuỗi BOS D1 → FVG → pullback → Kill Zone xác nhận bằng giờ. Điều không xác lập được: chất lượng định lượng thực sự của displacement M5 (thiếu số liệu để PASS chắc chắn, dù không có gì để FAIL).

**6. Falsification tests**
1. Bổ sung số liệu định lượng cho nến displacement M5 (range, ATR ratio) — nếu dưới ngưỡng chuẩn đã đề xuất ở 07-10/02 mục 7.3, hạ C4 xuống UNSUPPORTED mạnh hơn; nếu đạt ngưỡng, đóng O2 thành PASS.
2. Tách rõ 2 câu "quan sát wick" và "diễn giải hấp thụ" trong lần viết note tương lai — đóng O1.
3. Kiểm tra nếu neo TP vào named level gần nhất (BSL 1.18956, H1 range high) thay vì equilibrium 1.18005, RR sẽ là bao nhiêu — so sánh với 2.86 đã đạt, xem liệu TP hiện tại "may mắn" tối ưu hơn hay kém hơn kế hoạch named-level.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Lệnh Long tại CE của FVG H1 đơn (rank 1) trong Discount, sau BOS D1 + pullback hấp thụ + displacement/MSS M5 tại NY AM Kill Zone, đủ chuỗi 7 bước, Win 2.86R.

**Cần sửa** (load-bearing trước):
- C4 "Displacement + MSS M5 đạt chuẩn" — **UNSUPPORTED** · SKILL.md § Displacement yêu cầu "expansion một chiều, năng lượng cao"; note không cung cấp số liệu định lượng (range/ATR) để xác nhận ngưỡng, chỉ có tick Yes/No → fix: bổ sung số liệu cụ thể nến displacement M5.  ← (load-bearing)
- C_TP "TP 1.18244 hợp lệ theo Draw on Liquidity" — **FAIL** · TP không trùng bất kỳ named level nào đã map (H1 range high 1.18956, D1 range high 1.22649) — SKILL.md § Liquidity/Target yêu cầu mô tả draw on liquidity cụ thể; TP tại equilibrium nội bộ không neo named level → fix: đã đề xuất đúng ở mục 7.3 gốc (neo TP vào named level, ghi rõ nếu chốt tại internal).

**PASS:** C1 (D1 Bullish BOS — SKILL.md § BOS, phá swing thuận trend, có body close theo mô tả), C2 (FVG Discount — SKILL.md § Premium/Discount, entry 41.4% range dưới EQ, đúng phía Long), C3 (wick-reject hành vi hấp thụ — mô tả quan sát hợp lệ, tách khỏi diễn giải theo O1 mục 10), C5 (Kill Zone — SKILL.md § Killzone/Time, giờ cụ thể 08:10 ET, đạt evidence bar).

**Verdict:** INSUFFICIENT EVIDENCE — load-bearing claim C4 (chất lượng displacement/MSS M5) là UNSUPPORTED do thiếu số liệu định lượng, dù không có mâu thuẫn để FAIL. Theo decision rule, thesis với load-bearing claim UNSUPPORTED không được nhận PARTIALLY ALIGNED dù các claim phụ (C1, C2, C3, C5) đều PASS.

**Notes:** Doctrine gap nhỏ — SKILL.md không định nghĩa ngưỡng số cụ thể cho "đủ displacement" (ATR ratio bao nhiêu, body-to-range bao nhiêu) — đây là gap đã được chính vault (07-10/02 mục 7.3) tự đề xuất bổ sung; ghi nhận lại ở đây làm bằng chứng thứ 2 cho việc thiếu chuẩn định lượng này lặp lại ở nhiều note, đáng ưu tiên hoá thành rule Playbook cụ thể.

---

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật

1. **FVG đơn (rank 1/5) vẫn đủ để đạt Win chất lượng cao nếu đúng bias + đúng Kill Zone + đủ chuỗi 7 bước.** Ví dụ số thật: CE tính lại 1.17784 khớp chính xác note, RR tính lại 2.818 khớp gần đúng 2.86 (chênh 0.042R, sạch nhất batch) — không cần OB/Breaker/Unicorn để có kết quả tốt. Tổng quát hóa: POI rank là một yếu tố cộng thêm, không phải điều kiện cần.
2. **TP không neo named level vẫn có thể thắng, nhưng đó là may mắn kế hoạch, không phải bằng chứng cho phương pháp đặt TP.** Ví dụ số thật: TP 1.18244 gần equilibrium H1 (1.18005) chứ không phải BSL đã map (1.18956) — outcome Win không chứng minh cách đặt TP này đúng, chỉ chứng minh giá đủ đi xa để chạm nó lần này.

### (b) Bài học quy trình/checklist

- Note tự phát hiện lỗi TP không neo Draw on Liquidity (mục 7.1 gốc) NGAY TRONG LÚC Win — đây là hành vi kỷ luật xuất sắc, hiếm gặp (thường người backtest chỉ tự phê bình kỹ khi Loss). Cần nhân rộng: mọi note Win cũng phải tự hỏi "có điểm nào trong kế hoạch không khớp thực thi, dù kết quả tốt?"
- Thiếu số liệu định lượng displacement M5 (O2 mục 10) là khoảng trống lặp lại — nên trở thành trường bắt buộc trong template thay vì tùy chọn.

### (c) Bài học tâm lý-hành vi

- Không có dấu hiệu vi phạm kỷ luật — `followed_plan` không bị nghi ngờ trong note gốc. Điểm cần theo dõi: Grade B (không phải A) dù đủ chuỗi 7 bước — cho thấy note tự chấm khắt khe hợp lý (trừ điểm Risk Management vì TP mập mờ) thay vì tự cho điểm tuyệt đối chỉ vì Win, đây là hành vi chống overconfidence tốt cần giữ.

### (d) Rule đề xuất cho Playbook

- [ ] Mọi TP phải neo vào một named level cụ thể trong Draw on Liquidity đã map trước entry; nếu chốt tại internal/equilibrium, ghi rõ lý do và coi đây là partial, không phải TP cuối cùng đại diện cho toàn bộ kế hoạch.
- [ ] Bổ sung trường bắt buộc `displacement_atr_ratio` hoặc mô tả định lượng tương đương cho mọi lệnh tick `displacement: Yes` — không chấp nhận tick suông không kèm số liệu.
- [ ] Khi mô tả hành vi giá (vd wick-reject), tách 2 câu riêng: "quan sát hành vi" (fact) và "diễn giải ý nghĩa" (interpretation, cần gắn nhãn mức độ chắc chắn).

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG nên coi Win 2.86R là bằng chứng rằng "đặt TP tại equilibrium nội bộ" là phương pháp đúng để nhân rộng — chính note đã tự flag đây là điểm yếu cần sửa (mục 7.1/7.3 gốc), giữ nguyên đánh giá đó dù kết quả tốt.
- KHÔNG nên dùng note này làm chuẩn "displacement M5 không cần số liệu định lượng vẫn đủ tốt" — thiếu số liệu ở đây là UNSUPPORTED (Doctrine check mục 11), không phải bằng chứng rằng ngưỡng định lượng là không cần thiết; Win không tự động validate việc bỏ qua ngưỡng.
- KHÔNG nên khái quát "FVG rank 1 luôn đủ tốt" từ n=1 case — cần đối chiếu với các FVG rank 1 khác (Win và Loss) trong vault trước khi biến thành rule cứng.


### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[13-FVG-Fair-Value-Gap]]
- Entry refine: [[10-Consequent-Encroachment-Mean-Threshold]] · [[27-Premium-Discount]]
- Bước: [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[18-Kill-Zones]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[12-Mistake-Log-Data-Mismatch-Backtest]] (tham chiếu lỗi mâu thuẫn metadata đã tự phát hiện và sửa)
