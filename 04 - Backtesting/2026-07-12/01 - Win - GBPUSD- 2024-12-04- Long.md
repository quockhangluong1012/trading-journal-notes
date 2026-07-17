---
type: backtest
backtest_date: 2026-07-12
trade_date: 2024-12-04
symbol: GBPUSD
position: Long
result: Win
session:
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: Order Block
poi_rank: 2
poi_timeframe: H1
poi_location: Discount
poi_in_ote: No
ce_ote_overlap: No
poi_stack: OB (H1, 1.26642-1.26515) + FVG (trên OB) + FVG (tại CE OB)
fvg_high: 1.26642
fvg_low: 1.26515
ce_price: 1.265785
entry_type: Edge
entry_precision: Between
limit_filled: Yes
fill_depth_pct: 21
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: Yes
step5_poi_ok: Yes
step6_entry_ok: No
step7_target_ok: Yes
first_error_step: entry
missing_step: none
chained_fully: Yes
liquidity_swept: Yes
sweep_type: Internal
displacement: Yes
displacement_score:
mss: Yes
fvg_valid: Yes
confluence_score: 2
smt_confirm:
cisd_confirm: Yes
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: Yes
correlated_asset: none
entry_price: 1.26615
stop_loss: 1.26494
take_profit: 1.27027
r_planned: 3.4
rr_if_ce: 5.31
rr_if_ote:
r_multiple: 3.4
risk_percent:
spread_cost:
r_net:
grade: B
followed_plan: Yes
confidence: 3
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2024-12-04 — GBPUSD Long — POI & Step Decision

> [!warning] Đã hạ Grade từ A xuống B khi convert — đọc lý do trước khi phản đối
> Bản gốc chấm **Grade: A**, nhưng chính bạn đã tự đề xuất trong "Rule cần thêm" của bản gốc: *"Nếu D1 bias còn 'tentative' (leg gần nhất ngược hướng)… grade tối đa = B cho tới khi H1 + M5 confirm… Lệnh này về bản chất là mua Discount trong một pullback của leg giảm gần nhất trên D1 — hợp lệ nhưng discretionary, nên grade A hiện đang hơi rộng tay."*
> Mình áp dụng đúng rule bạn tự đặt ra: D1 bias tại thời điểm phân tích được ghi là *"vẫn chưa được xác nhận chính xác, tạm thời tôi đang xác định là Bullish"* → theo rule, grade tối đa = **B**. Đây không phải đánh giá lại chủ quan của mình, mà là áp dụng nhất quán tiêu chuẩn bạn đã tự rút ra. Nếu bạn thấy rule này chưa nên áp dụng hồi tố, cứ sửa lại `grade` về A.
>
> Ngoài ra: `session` để **trống** (bản gốc chỉ ghi "New York" chung, giờ 16:00/16:05-16:50/16:30/16:40 không rõ timezone gốc nên không đủ căn cứ xác định AM/PM) — cần bạn xác nhận. `risk_percent`, `spread_cost`, `r_net`, `smt_confirm`, `in_macro_time`, `displacement_score` cũng để trống vì bản gốc chưa ghi.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | GBPUSD                                                      |
| Model Variant             | Standard (D1/H4→H1→M5)                                      |
| Trade Date (dữ liệu)      | 2024-12-04                                                  |
| Position                  | Long                                                        |
| Result                    | Win                                                         |
| Session                   | *(chưa xác nhận AM/PM)*                                      |
| HTF Bias                  | Bullish (tentative ở D1, confirm ở H1/M5)                   |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | Order Block (H1)                                             |
| POI Rank (8.1)            | 2 (FVG+OB — 2 FVG chồng lên OB)                              |
| POI Timeframe             | H1                                                            |
| POI Location              | Discount                                                     |
| **Entry Type**            | Edge (vào phía trên CE, không chờ về CE)                     |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | entry                                                         |
| R Planned (gross)         | 3.4                                                           |
| R Net (sau spread)        | *(chưa có)*                                                   |
| R Multiple (kết quả)      | 3.4                                                           |
| Confluence Score (0–8)    | 2 (`cisd_confirm` + `idm_swept`; các mục khác chưa đánh giá)  |
| Grade                     | **B** *(hạ từ A theo rule tự đặt — xem cảnh báo trên)*        |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

- **Bias**: Bullish — *lý do*:
  - Giá đang trong Order Block (tổng quát) Bullish, nhưng leg gần nhất là một Bearish displacement.
  - Sau đó giá có nhịp pullback hồi lên.
  - Giá vừa quét các old lows, phía trên còn 1 FVG D1 chưa mitigate.
  - **Bias tại thời điểm phân tích D1 chưa được xác nhận chắc chắn** — chỉ confirm khi H1 retrace về POI (OB) và M5 hình thành CISD nuốt trọn nhịp giảm quét OB.
- **Dealing Range (H1)**: High 1.27497 / Low 1.26164 → **Discount** (đúng phía cho Long).
- **Draw on Liquidity**:
  - Buy-side (BSL): H1 Dealing Range High (1.27497); D1 FVG (1.28586–1.27688).
  - Sell-side (SSL): old low vừa quét (1.24852); FVG bên dưới (1.24187–1.23954).

![[Pasted image 20260712160925.png]]
![[Pasted image 20260712161058.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: Order Block H1 (1.26642–1.26515), hình thành từ nhịp displacement lên đỉnh cũ lúc 9:00 AM ngày 04/12/2024. Giá retrace về vùng này lúc 16:00 cùng ngày.
- **POI Rank (8.1)**: 2/5 (FVG+OB — CISD để lại 2 FVG chồng lên OB: 1 FVG trên OB, 1 FVG ngay CE của OB).
- **POI hình thành trên khung**: H1.
- **POI nằm ở**: Discount — đúng phía cho Long.
- **POI stack**: OB (H1) + FVG (trên OB) + FVG (tại CE OB).
- **CE của FVG có trùng OTE 62–79%?**: No — bản gốc không đối chiếu fib Dealing Range, và entry thực tế (fib ~21% trong OB) nông hơn nhiều so với dải OTE.
- **Bounds & CE**: FVG/OB High 1.26642 · Low 1.26515 · CE 1.265785.

![[Pasted image 20260712161058.png]]

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: Edge → `entry_type: Edge` (entry 1.26615 nằm trên CE 1.265785, tức phía Edge-top của OB).
- **Entry Precision**: Between (entry cách top 0.00027, cách CE 0.000365 — nằm giữa Edge-top và CE, gần Edge hơn).
- **Limit có được khớp không?**: Yes.
- **Giá đi sâu bao nhiêu vào FVG/OB?**: `fill_depth_pct` ≈ 21% ((1.26642−1.26615)/(1.26642−1.26515)×100).
- **RR ghi lại**: `r_planned` thực tế = 3.4. Nếu vào đúng CE (1.265785, SL giữ nguyên 1.26494): `rr_if_ce` ≈ **5.31** — RR cao hơn đáng kể nếu chờ CE. `rr_if_ote` để trống (không có định nghĩa OTE rõ ràng cho riêng OB này trong bản gốc).

> [!important] Đây chính là lesson gốc: bạn chọn vào **trên CE** vì tin rằng "nhiều trader đặt limit tại CE nên lệnh của họ không được fill" — một giả thuyết **chưa có bằng chứng** (chính bạn ghi "tôi tự nghĩ, chưa có bằng chứng cụ thể"). Lệnh thắng, nhưng thắng không chứng minh giả thuyết đúng.

![[Pasted image 20260712162407.png]]

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? | Ghi chú |
|---|---|---|---|
| 1 | **Bias** | Yes | Confirm được trước entry qua chuỗi H1 retrace + M5 CISD, dù D1 ban đầu tentative. |
| 2 | **Draw on Liquidity** | Yes | BSL/SSL xác định đúng ở bước HTF. |
| 3 | **Liquidity Sweep** | Yes | Quét old lows + quét 50% OB H1. |
| 4 | **Displacement + MSS** | Yes | CISD (chuỗi nến bullish nuốt trọn nến bearish displacement) 16:05–16:50; displacement tạo FVG lúc 16:30 và 16:40. |
| 5 | **POI (FVG/OB...)** | Yes | OB H1 hợp lệ, đúng Discount. |
| 6 | **Entry (retrace)** | **No** | Vào trên CE dựa trên giả thuyết chưa kiểm chứng ("sợ lệnh không fill tại CE"), không phải rule đã backtest. |
| 7 | **Target** | Yes | TP 1.27027 đặt có buffer trước H1 DR High (1.27497) — hợp lý, không đua tới sát pool thanh khoản. |

- **First Error Step**: `entry` — mắt xích duy nhất bị hỏng trong chuỗi 7 bước.
- **Missing Step**: none.
- **Đủ chuỗi 7 bước?**: Yes.

> [!warning] Chống hindsight bias
> Checklist bản gốc từng tick "Bias D1/H4 rõ ràng, không mâu thuẫn H1" trong khi chính văn bản phân tích ghi "tạm thời, chưa xác nhận" — đây là **confirmation bias sau khi biết kết quả**. Template mới không lặp lại lỗi này: field `step1_bias_ok` ở đây được đánh giá dựa trên việc bias **có được confirm trước khi entry** (Yes), không phải "rõ ràng ngay từ D1" (điều này không đúng).

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE:**
- [x] Bias HTF (confirm trước entry) + draw xác định
- [x] Liquidity sweep TRƯỚC displacement + reclaim → `sweep_type: Internal`
- [x] Displacement hợp lệ (CISD nuốt trọn nến bearish) — `displacement_score` để trống, chưa chấm theo 4 tiêu chí
- [x] MSS/CISD hợp lệ
- [x] FVG/POI sạch, entry là retrace (dù ở Edge, không phải CE)
- [x] Entry đúng Discount, đồng hướng bias
- [x] Stop có logic (dưới OB) + target R:R 3.4 ≥ kế hoạch

**SCORE (0–8):**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 | No | Rank 2 |
| 2 | CE trùng OTE 62–79% | No | Không trùng, entry nông hơn CE |
| 3 | SMT divergence | *(chưa đánh giá)* | Không ghi nhận |
| 4 | CISD flip LTF | **Yes** | Chuỗi bullish nuốt trọn nến bearish displacement |
| 5 | Macro time | *(chưa đánh giá)* | Không rõ timezone giờ vào lệnh |
| 6 | NWOG/NDOG align | No | Không đề cập |
| 7 | −2SD/ERL target | No | TP là buffer trước DR High, không phải −2SD |
| 8 | Inducement bị quét trước POI | **Yes** | Quét old lows/50% OB trước reversal |

- **Confluence Score**: 2.
- **Correlated asset**: none.
- **Grade**: **B** (xem cảnh báo đầu file — áp dụng rule bias-tentative bạn tự đề xuất).

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP.
- **Tại sao thắng?**
  - Kiên nhẫn chờ H1 đồng bias với D1, chờ M5/H1 confirm bias, chờ H1 về Discount, có sweep + CISD.
- **POI đã chọn có phải lựa chọn tốt nhất không?**
  - OB H1 hợp lệ, nhưng lựa chọn **entry level** (trên CE) chưa có cơ sở dữ liệu — chỉ là cảm nhận cá nhân.
- **Entry (Edge/CE/OTE) có tối ưu không?**
  - Không rõ. `rr_if_ce` ≈ 5.31 cho thấy chi phí cơ hội nếu vào Edge thay vì CE là rất lớn (mất gần 2R tiềm năng). Cần backtest thêm để xác định pattern "giá không về CE sau CISD mạnh" có thật hay không.
- **Fill**: khớp đúng như kỳ vọng tại vùng Edge/Between.
- **Bước đầu tiên sai**: Entry — nên có rule khách quan (vd: đếm số mẫu lịch sử giá có về CE sau CISD mạnh hay không) thay vì quyết định bằng cảm giác.
- **Chi phí (spread/slippage)**: chưa ghi nhận.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 90%.
- **Nếu vào lại, tôi sẽ làm gì khác?**
  - Log thêm `entry_zone`/`ce_filled` qua ≥20–30 mẫu để so sánh win rate + expectancy giữa "vào cạnh" và "chờ CE" bằng dữ liệu, không phải cảm giác.

---

## 7. Lesson Learned

### Bài học kỹ thuật (đặc thù POI / bước)
**Root cause (nguyên nhân gốc):**
Đây là lệnh thắng và execution khá sạch, nhưng **điểm quyết định (và cũng là mắt xích yếu nhất)** là: quyết định entry-level (vào phía trên CE thay vì tại CE) được đưa ra bằng **cảm nhận chưa có dữ liệu backtest** ("giá hay quay đầu trước CE"). Lệnh thắng, nhưng thắng không chứng minh giả thuyết đúng — nó chỉ chưa phủ nhận.

**Triệu chứng (symptoms):**
- **Mâu thuẫn nội bộ trong journal gốc**: mục HTF Bias tự ghi "chưa xác nhận chính xác", nhưng Setup Quality Checklist lại tick "rõ ràng, không mâu thuẫn" → confirmation bias sau khi biết kết quả (đã sửa cách đánh giá trong mục 4 ở trên).
- **Narrative chưa có bằng chứng đóng vai "sự thật"**: giả định "nhiều trader đặt limit ở CE nên lệnh họ không fill" là **story chưa kiểm chứng**.
- **Chấm điểm theo RR thay vì theo tính hợp lệ của trigger**: bản gốc tự trừ xuống 90% chỉ vì giá không về CE — trong khi trigger (sweep + CISD + FVG + Discount) đã hợp lệ 100%.

**Cơ chế thị trường (hiểu để không lặp lại):**
Giá retrace về H1 OB (Discount) → nến bearish displacement đóng xuyên qua cạnh dưới OB kèm râu (= liquidity sweep) → chuỗi nến bullish CISD nuốt trọn nến đó (= MSS) → leg CISD để lại 2 FVG (một trên OB, một tại CE OB). Sau một CISD mạnh, delivery đã chuyển sang tìm premium, nên giá thường tiếp tục ngay từ FVG đầu tiên/cạnh gần POI chứ không nhất thiết retrace sâu về CE. Việc giá quay đầu trước CE là **hệ quả cơ học của một CISD mạnh**, không nhất thiết vì "limit trader khác ở CE".

### Pattern lặp lại (điều cần để ý lần sau)
- **"Lỡ lệnh vì chờ CE"**: pattern lặp lại ở nhiều backtest gần đây — cần định lượng bằng field `entry_type`/`limit_filled` qua ≥20–30 mẫu trước khi đổi rule.
- **Confirmation bias ở checklist**: xu hướng tick "bias rõ ràng" dù note tự nói chưa chắc — không được tick khi phân tích còn ghi "tạm thời/chưa xác nhận".
- **Gán narrative cho hành vi giá**: giữ mô tả ở mức cơ chế (sweep/CISD/FVG/premium-discount), không thêm story không kiểm chứng được.

### Rule cần thêm/cập nhật vào Playbook
- [ ] **Entry-level rule (chờ dữ liệu xác nhận)**: khi CISD tạo ≥2 FVG chồng lên POI, entry mặc định = CE của FVG gần POI nhất. Chỉ cho phép entry sớm hơn tại cạnh nếu backtest chứng minh fill-rate tại CE thấp — **bắt buộc log `entry_type` để đo**, không đổi rule bằng cảm giác.
- [ ] **Bias-grade rule**: nếu D1 bias còn "tentative" (leg gần nhất ngược hướng), grade tối đa = B cho tới khi H1+M5 confirm; cấm tick "bias rõ ràng" khi phân tích còn ghi "chưa xác nhận" (**đã áp dụng ngay trong file này — grade B**).
- [ ] **Kill-zone verify rule**: ghi rõ timezone của mọi mốc giờ (broker/GMT/ET) — chỉ tick "trong Kill Zone" sau khi quy đổi về ET.
- [ ] **Housekeeping**: điền `risk_percent` — vẫn còn thiếu ở bản convert này.

---

## 8. Final Grade

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| HTF Bias & Draw | 6/10 | Bias D1 tentative lúc phân tích, chỉ confirm muộn ở H1/M5 |
| POI Selection (đúng loại + hạng + P/D) | 8/10 | OB H1 hợp lệ, đúng Discount, rank 2 |
| Liquidity Sweep | 8/10 | Sweep + CISD rõ ràng |
| Displacement / MSS quality | 8/10 | CISD mạnh, nuốt trọn nhịp giảm |
| Entry Precision & Fill (Edge/CE/OTE) | 4/10 | Vào Edge dựa trên giả thuyết chưa kiểm chứng |
| Risk Management (R net, RR) | 6/10 | RR 3.4 tốt nhưng thiếu `risk_percent`/`r_net` |

**Overall Grade**: **B** (hạ từ A theo rule bias-tentative — xem cảnh báo đầu file)

> [!tip] Chống curve-fitting
> Trigger (sweep + CISD + FVG hợp lệ trong Discount) nhận diện được trước outcome — hợp lệ để tính vào thống kê edge, nhưng grade phản ánh chất lượng bias-tại-thời-điểm-phân-tích, không phải chỉ kết quả.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[25 - OB - Order Block]] · [[13 - FVG  - Fair Value Gap]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]

---

> [!important] Việc cần bạn bổ sung (không tự suy diễn khi convert)
> - `session`: xác nhận New York AM hay PM.
> - `rr_if_ote`: chưa có định nghĩa OTE band rõ ràng cho OB này.
> - `displacement_score`, `smt_confirm`, `in_macro_time`: cần xem lại chart gốc.
> - `risk_percent`, `spread_cost`, `r_net`: chưa từng được ghi ở bản gốc.
> - Xác nhận lại quyết định hạ **Grade A → B** — nếu không đồng ý, sửa lại `grade: A` trong frontmatter.
