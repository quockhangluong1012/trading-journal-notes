---
type: backtest
backtest_date:
trade_date:
symbol:
position:
result:
session:
setup: ICT 2022 Model
model_variant:
entry_model:
entry_timeframe:
htf_bias:
bias_correct:
poi_type:
poi_rank:
poi_timeframe:
poi_location:
poi_in_ote:
ce_ote_overlap:
poi_stack:
fvg_high:
fvg_low:
ce_price:
entry_type:
entry_precision:
limit_filled:
fill_depth_pct:
missed_by:
step1_bias_ok:
step2_draw_ok:
step3_sweep_ok:
step4_displacement_ok:
step5_poi_ok:
step6_entry_ok:
step7_target_ok:
first_error_step:
missing_step:
chained_fully:
liquidity_swept:
sweep_type:
displacement:
displacement_score:
mss:
fvg_valid:
confluence_score:
smt_confirm:
cisd_confirm:
in_macro_time:
nwog_ndog_align:
sd_target_align:
idm_swept:
correlated_asset:
entry_price:
stop_loss:
take_profit:
r_planned:
rr_if_ce:
rr_if_ote:
r_multiple:
risk_percent:
spread_cost:
r_net:
grade:
followed_plan:
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest {{date}} — SYMBOL Position — POI & Step Decision

> [!info] Mục đích của template này
> Đây là biến thể backtest **xoay quanh POI + quyết định từng bước** của [[01 - ICT 2022 Model]]. Mỗi file = 1 setup. Ngoài việc chấm Win/Loss, template này ép bạn ghi lại: (1) **loại POI** đã chọn và hạng của nó, (2) **entry vào cạnh (Edge), CE hay OTE**, (3) **lệnh limit có được khớp không** và giá đi sâu bao nhiêu vào POI, (4) **từng bước trong chuỗi 7 bước đúng hay sai**, (5) **bước đầu tiên bị hỏng** (`first_error_step`). Sau ~30–50 mẫu, [[_POI Analytics Dashboard]] sẽ tự trả lời: *POI nào tôi áp dụng tốt nhất? Vào CE hay Edge cho expectancy cao hơn? Tôi hay sai ở bước nào?*

> [!important] Quy tắc điền frontmatter — ĐỌC TRƯỚC KHI LOG
> Dashboard chỉ tổng hợp đúng nếu bạn điền **giá trị vô hướng (scalar), không phải list**, và **đúng từ vựng chuẩn (controlled vocabulary)** bên dưới. Ba lỗi hay gặp cần tránh:
> 1. **KHÔNG** để `result:` thành list `[Win]` — viết thẳng `result: Win`. (Dataview so sánh chuỗi; list làm hỏng win-rate.)
> 2. **`poi_type` là LOẠI POI (Order Block / FVG / Breaker...), KHÔNG phải `[[01 - ICT 2022 Model]]`.** Đây là field quan trọng nhất của template này.
> 3. Mọi field Yes/No dùng đúng `Yes` hoặc `No` (viết hoa chữ đầu), không dùng `true/false/có/x`.

> [!note] Từ vựng chuẩn cho từng field (copy đúng chữ)
> - **model_variant**: `Standard` (D1/H4→H1→M5) · `LTF` (H1-M5-M1)
> - **symbol**: `NQ1` · `NAS100` · `US30` · `EURUSD` · `GBPUSD` · `XAUUSD`
> - **session**: `London` · `New York AM` · `New York PM` · `Asia`
> - **poi_type**: `Order Block` · `FVG` · `Breaker Block` · `Rejection Block` · `iFVG` · `Unicorn` · `Mitigation Block` · `Hidden OB` · `Vacuum Block` · `Implied FVG` · `NWOG` · `NDOG` · `Liquidity Void`
> - **poi_rank** (thang 8.1): `1`=FVG đơn · `2`=FVG+OB · `3`=Breaker · `4`=iFVG · `5`=Unicorn *(POI ngoài thang này để trống rank hoặc ước lượng gần nhất)*
> - **poi_timeframe**: `H4` · `H1` · `M15` · `M5` · `M1`
> - **poi_location**: `Discount` · `Premium` · `Equilibrium`
> - **entry_type**: `CE` (50% FVG) · `Edge` (first-touch mép gần) · `OTE` (vào tại dải 62–79%)
> - **entry_precision**: `Edge-top` (mép xa nhất) · `Between` (giữa mép và CE) · `CE` (đúng 50%) · `Deeper-than-CE` (sâu quá CE)
> - **limit_filled**: `Yes` (khớp đủ) · `Partial` (khớp một phần) · `No` (không chạm giá limit)
> - **sweep_type**: `Internal` · `External` · `Equal Highs` · `Equal Lows` · `Double`
> - **first_error_step**: `none` · `bias` · `draw` · `sweep` · `displacement` · `poi` · `entry` · `target`
> - **missing_step**: `none` · `sweep` · `displacement` · `retrace` · `target`
> - **correlated_asset**: `ES` · `GBPUSD` · `EURUSD` · `DXY` · `none`
> - **grade**: `A+` · `A` · `B` · `C` · `D` · `F`
> - Các field số: `poi_rank` 1–5 · `displacement_score` 0–4 · `confluence_score` 0–8 · `fill_depth_pct` 0–100 · `confidence` 1–5 · `risk_percent` (VD 0.5)

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | NQ1 / NAS100 / US30 / EURUSD / GBPUSD / XAUUSD              |
| Model Variant             | Standard (D1/H4→H1→M5) / LTF (H1-M5-M1)                     |
| Trade Date (dữ liệu)      |                                                             |
| Position                  | Long / Short                                                |
| Result                    | Win / Loss / BE                                             |
| Session                   | London / New York AM / New York PM / Asia                   |
| HTF Bias                  | Bullish / Bearish / Neutral                                 |
| Bias Correct?             | Yes / No                                                    |
| **POI Type**              | *(xem từ vựng chuẩn — đây là field lõi)*                    |
| POI Rank (8.1)            | 1–5                                                         |
| POI Timeframe             | H4 / H1 / M15 / M5 / M1                                     |
| POI Location              | Discount / Premium / Equilibrium                            |
| **Entry Type**            | CE / Edge / OTE                                             |
| **Limit Filled?**         | Yes / Partial / No                                          |
| **First Error Step**      | none / bias / draw / sweep / displacement / poi / entry / target |
| R Planned (gross)         |                                                             |
| R Net (sau spread)        |                                                             |
| R Multiple (kết quả)      |                                                             |
| Confluence Score (0–8)    |                                                             |
| Grade                     | A+ / A / B / C / D / F                                       |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

> [!note] Điều chỉnh theo `model_variant`
> - **Standard**: đọc bias trên D1/H4, POI/context trên H1/M15, execution M5/M1.
> - **LTF**: H1 = bias (lọc H4), M5 = POI/động cơ, M1 = refine entry.

- **Bias**: Bullish / Bearish / Neutral — *lý do (PD array, draw):*
  -
- **Dealing Range**: High ___ / Low ___ → **Premium / Discount** (entry phải đúng phía)
- **Draw on Liquidity (target cuối)**:
  - Buy-side (BSL): PDH / session high / equal highs @ ___
  - Sell-side (SSL): PDL / session low / equal lows @ ___

![[SYMBOL-YYYYMMDD-D1.png]]
![[SYMBOL-YYYYMMDD-H1.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

> [!important] Đây là phần lõi để trả lời "POI nào tôi áp dụng tốt"
> Ghi rõ POI **đã dùng để đặt entry**, hạng của nó theo thang chất lượng 8.1, và các POI khác **chồng cùng vùng** (poi_stack). Sau này dashboard so win-rate/expectancy giữa các `poi_type`.

- **POI Type đã dùng**: ______  → điền `poi_type` (VD `Order Block`, `Breaker Block`, `FVG`, `iFVG`, `Unicorn`...)
- **POI Rank (8.1)**: ___/5 → `poi_rank`
- **POI hình thành trên khung**: ______ → `poi_timeframe`
- **POI nằm ở**: Discount / Premium / Equilibrium → `poi_location` *(phải đúng phía: Long→Discount, Short→Premium)*
- **POI stack** (các POI khác chồng cùng dải giá): ví dụ `FVG+OB+OTE` → `poi_stack`
- **CE của FVG có trùng dải OTE 62–79% không?**: Yes / No → `ce_ote_overlap`; **POI có nằm trong OTE?** → `poi_in_ote`
- **Bounds & CE** (để đo độ sâu fill): FVG High ___ (`fvg_high`) · FVG Low ___ (`fvg_low`) · CE 50% ___ (`ce_price`)

> [!tip] Thang chất lượng POI (từ mục 8.1 của [[01 - ICT 2022 Model]])
> `1` FVG đơn → `2` [[25 - OB - Order Block|FVG+OB]] → `3` [[04 - Breaker Block|Breaker]] → `4` [[17 - Inverse Fair Value Gap - iFVG|iFVG]] → `5` [[07 - Unicorn Model|Unicorn]]. Ưu tiên POI **nhiều lý do trùng một dải giá**, không phải POI gần giá nhất.
> POI nâng cao khác: [[28 - Rejection Block]] · [[22 - Mitigation Block]] · [[44 - Hidden Order Block]] · [[34 - Vacuum Block]] · [[14 - Implied Fair Value Gap]] · [[23 - New Day Opening Gap|NDOG]] · [[24 - New Week Opening Gap|NWOG]] · [[21 - Liquidity Void]].

![[SYMBOL-YYYYMMDD-M5.png]]

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

> [!important] Trả lời "chạm FVG tại cạnh hay CE cho kết quả tốt" + "tỷ lệ khớp lệnh"
> Đây là hai câu hỏi thống kê riêng biệt:
> - **Chất lượng vị trí vào** (`entry_type` / `entry_precision`): vào càng sâu (CE/OTE) → RR càng cao nhưng **rủi ro không được fill** càng lớn.
> - **Fill-rate** (`limit_filled` / `fill_depth_pct`): giá có thực sự về tới limit của bạn không, và đi sâu bao nhiêu % vào FVG.

- **Entry Type**: CE / Edge / OTE → `entry_type`
- **Entry Precision** (chính xác vào đâu trong FVG): Edge-top / Between / CE / Deeper-than-CE → `entry_precision`
- **Limit có được khớp không?**: Yes / Partial / No → `limit_filled`
- **Giá đi sâu bao nhiêu vào FVG?**: ___% (0% = chỉ chạm mép gần; 50% = tới CE; 100% = chạm mép xa) → `fill_depth_pct`
  - *Cách tính (Long, POI dưới):* `fill_depth_pct = (fvg_high − giá thấp nhất chạm) / (fvg_high − fvg_low) × 100`
- **Nếu KHÔNG khớp (`limit_filled: No`)**: giá quay đầu cách limit bao xa? ___ pip/pt → `missed_by`
- **RR ghi lại**: thực tế `r_planned` ___ · nếu vào CE `rr_if_ce` ___ · nếu vào OTE `rr_if_ote` ___

> [!note] Vì sao ghi cả `rr_if_ce` và `rr_if_ote`
> Nếu bạn hay vào Edge vì "sợ không được fill", cột `rr_if_ce`/`rr_if_ote` cho thấy **RR bạn đã đánh đổi**. Sau đủ mẫu, dashboard so *fill-rate × expectancy* của CE vs Edge vs OTE → để **dữ liệu** quyết định rule, không phải cảm tính.

![[SYMBOL-YYYYMMDD-M1.png]]

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

> [!important] Đây là phần cho câu hỏi "khi tôi làm sai, tôi đã sai ở bước nào của chuỗi"
> Với **mỗi bước**, đánh giá quyết định của bạn **tại thời điểm ra quyết định** (không phải sau khi biết kết quả): `Yes` = làm đúng bước này, `No` = làm sai/bỏ qua, `NA` = không áp dụng. Sau đó ghi **`first_error_step`** = bước ĐẦU TIÊN bị hỏng (mắt xích gãy sớm nhất). Đây là field vàng cho thống kê.

| # | Bước | Câu hỏi kiểm tra | Đúng? (`Yes/No/NA`) | Field |
|---|---|---|---|---|
| 1 | **Bias** | Xác định đúng hướng HTF? | | `step1_bias_ok` |
| 2 | **Draw on Liquidity** | Chọn đúng pool target? | | `step2_draw_ok` |
| 3 | **Liquidity Sweep** | Có sweep + reclaim trước displacement? | | `step3_sweep_ok` |
| 4 | **Displacement + MSS** | Displacement hợp lệ (≥3/4 tiêu chí) + phá cấu trúc? | | `step4_displacement_ok` |
| 5 | **POI (FVG/OB...)** | Chọn đúng POI hợp lệ, đúng P/D? | | `step5_poi_ok` |
| 6 | **Entry (retrace)** | Vào ở retrace về POI, KHÔNG chase? | | `step6_entry_ok` |
| 7 | **Target** | Chọn đúng pool đối diện, R:R đạt kế hoạch? | | `step7_target_ok` |

- **First Error Step** (bước đầu tiên sai — mắt xích gãy sớm nhất): `none` nếu cả 7 đúng → `first_error_step`
- **Missing Step** (mắt xích bị bỏ qua, dùng cho lệnh Loss/BE): none / sweep / displacement / retrace / target → `missing_step`
- **Đủ chuỗi 7 bước?**: Yes / No → `chained_fully`

> [!warning] Chống hindsight bias
> Chỉ tick `Yes` cho một bước nếu **trigger nhận diện được TRƯỚC khi biết outcome**. Nếu bạn chỉ "thấy đúng" sau khi giá đã chạy → đánh dấu `No` và loại setup khỏi thống kê edge. Xem [[Mistake - Chase Displacement]] · [[Mistake - Skip Liquidity Sweep]] · [[Mistake - Trade Against Bias]].

---

## 5. Setup Quality & Confluence (GATE + SCORE)

> [!important] GATE (pass/fail — KHÔNG tính điểm)
> Bất kỳ mục nào fail → **No Trade**, không chấm SCORE.

- [ ] Bias HTF rõ + draw xác định (`step1`/`step2`)
- [ ] Liquidity sweep TRƯỚC displacement + reclaim → `liquidity_swept` · loại: `sweep_type`
- [ ] Displacement hợp lệ theo khung CLV/wick/acceptance/FVG → `displacement` · điểm `displacement_score` ___/4
- [ ] MSS hợp lệ → `mss`
- [ ] FVG/POI sạch + entry là **retrace** → `fvg_valid`
- [ ] Entry đúng Premium/Discount, đồng hướng bias
- [ ] Stop có logic + target pool rõ + R:R ≥ kế hoạch

**SCORE — mỗi confluence +1 (0–8) → `confluence_score`:**

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 (Breaker/iFVG/Unicorn), không phải FVG trơ | | *(suy từ `poi_rank`)* |
| 2 | CE của FVG trùng dải OTE 62–79% | | `ce_ote_overlap` |
| 3 | SMT divergence tại điểm sweep | | `smt_confirm` |
| 4 | CISD xác nhận flip delivery trên LTF | | `cisd_confirm` |
| 5 | Entry rơi trong macro time (không chỉ killzone) | | `in_macro_time` |
| 6 | Trùng NWOG/NDOG hoặc HTF PD array | | `nwog_ndog_align` |
| 7 | Target trùng −2SD projection và/hoặc ERL rõ | | `sd_target_align` |
| 8 | Có inducement bị quét trước POI | | `idm_swept` |

- **Cặp tương quan soi kèm**: ES / GBPUSD / EURUSD / DXY / none → `correlated_asset`
- **Quy đổi điểm → hạng**: ≥5 = **A+** · 3–4 = **A** · 2 = **B** · 0–1 = **C** (No Trade) → `grade`

> [!note] GATE luôn thắng SCORE. 8/8 điểm nhưng thiếu một mục GATE = vẫn No Trade. Chi tiết: mục 8.4 của [[01 - ICT 2022 Model]].

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP / Hit SL / BE / Manual Close → `result`
- **Tại sao thắng/thua?**
  -
- **POI đã chọn có phải lựa chọn tốt nhất không, hay có POI hạng cao hơn tôi đã bỏ lỡ?**
  -
- **Entry (Edge/CE/OTE) có tối ưu không? Nếu vào sâu hơn/nông hơn thì sao?**
  -
- **Fill**: limit khớp đúng như kỳ vọng chứ? (`limit_filled`, `fill_depth_pct`)
  -
- **Bước đầu tiên sai (nếu có)** và tôi đã có những lựa chọn nào tại bước đó:
  -
- **Chi phí (spread/slippage) ảnh hưởng R ròng thế nào?** (`spread_cost`, `r_net`)
  -
- **Setup khớp bao nhiêu % với mô hình chuẩn?** ___%
- **Nếu vào lại, tôi sẽ làm gì khác?**
  -

---

## 7. Lesson Learned

### Bài học kỹ thuật (đặc thù POI / bước)
-

### Pattern lặp lại (điều cần để ý lần sau)
-

### Rule cần thêm/cập nhật vào Playbook
- [ ]

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | /10 |
| POI Selection (đúng loại + hạng + P/D) | /10 |
| Liquidity Sweep | /10 |
| Displacement / MSS quality | /10 |
| Entry Precision & Fill (Edge/CE/OTE) | /10 |
| Risk Management (R net, RR) | /10 |

**Overall Grade**: A+ / A / B / C / D / F

> [!tip] Chống curve-fitting
> Trigger (sweep + displacement ≥3/4 + POI hợp lệ trong killzone) có nhận diện được **trước** khi biết outcome không? Nếu không → loại mẫu khỏi thống kê.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]] · [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]]
- POI ladder: [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]] · [[04 - Breaker Block]] · [[28 - Rejection Block]] · [[17 - Inverse Fair Value Gap - iFVG]] · [[07 - Unicorn Model]] · [[22 - Mitigation Block]] · [[44 - Hidden Order Block]] · [[34 - Vacuum Block]] · [[14 - Implied Fair Value Gap]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- Timing: [[18 - Kill Zones]] · [[40 - Macro Times]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[Mistake - Chase Displacement]] · [[Mistake - Skip Liquidity Sweep]] · [[Mistake - Trade Against Bias]]
