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

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL tại thời điểm entry (1.26615):**
- Đã bị lấy (ERL): old lows (1.24852) và 50% của OB H1 — quét trước reversal, dùng làm sweep hợp lệ.
- **Chưa bị lấy (IRL, trên đường từ entry tới SL 1.26494)**: khoảng cách entry (1.26615) → CE (1.265785) → SL (1.26494) không có internal liquidity pool riêng được note ghi nhận — CE nằm giữa, SL nằm dưới đáy OB. Entry tại Between (fill_depth 21%) nghĩa là 79% chiều sâu OB (bao gồm toàn bộ vùng CE) *chưa được test* trước khi lệnh này coi là "đã xác nhận".
- DOL chưa bị lấy: H1 DR High (1.27497), D1 FVG (1.28586–1.27688) — TP 1.27027 dừng trước cả DR High, hợp lý và có buffer, khác với case EURUSD (07-11) chốt quá gần.

**Chất lượng displacement/MSS**: CISD (chuỗi nến bullish nuốt trọn nến bearish displacement) 16:05–16:50, tạo 2 FVG chồng OB — mô tả rõ hơn EURUSD nhưng vẫn thiếu `displacement_score` định lượng.

**Yếu tố thời gian**: `session` để trống — không xác nhận được AM/PM cho giờ 16:00–16:50. Note tự cảnh báo cần quy đổi timezone trước khi tick "trong Kill Zone".

**Vị trí entry trong dealing range**: Discount đúng phía, nhưng entry nông hơn CE khá rõ — `ce_ote_overlap: No`, entry ở fib ~21% trong OB, không trùng OTE 62-79%. Đây là entry Edge (trên CE) chứ không phải OTE-refine.

**So sánh với các lệnh CE chuẩn trong vault**: đối chiếu [[01 - Win - EURUSD - 2021-05-03- Short]] và [[01 - Win - GBPUSD - 2014-06-25 - Long]] (entry_type: CE, CE 1.70712, first_error_step: 6 nhưng ghi khác ngữ cảnh — cần đối chiếu thận trọng, không đồng nhất tự động). Điểm khác biệt cốt lõi với GBPUSD hiện tại: `rr_if_ce` = 5.31 tức RR *lẽ ra* cao hơn gần gấp đôi (3.4→5.31) nếu chờ đúng CE — đây là chi phí cơ hội đo được bằng số, không phải suy đoán, khác với case EURUSD (07-11) không tính được do lỗi bounds. Xem SVG so sánh ở mục 10.

![[MULTI-20260803-edge-vs-ce-entry.svg|760]]

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

**Evidence base**: chỉ có text note, không truy cập ảnh PNG đính kèm. `evidence_sufficiency: partial` — số liệu entry/CE/SL/TP đầy đủ và tính lại khớp (xem xác minh arithmetic), nhưng cấu trúc chart HTF (D1) không truy cập được để kiểm độc lập nhãn "tentative bias".

**Claim graph:**
- C1: Bias D1 "tentative" tại thời điểm phân tích, chỉ confirm bằng H1 retrace + M5 CISD.
- C2: Sweep old lows + 50% OB + CISD + FVG hợp lệ trong Discount.
- C3: Entry tại **trên CE** (Between, fill_depth 21%) dựa trên giả thuyết "nhiều trader đặt limit tại CE nên lệnh không được fill" — note tự ghi giả thuyết này **chưa có bằng chứng**. **Load-bearing**, vì đây là claim mà toàn bộ lesson và cả quyết định hạ Grade A→B của chính note xoay quanh.
- C4: TP có buffer trước DR High — PASS, tốt hơn EURUSD (07-11).
- C5 (từ C3): rr_if_ce = 5.31 vs r_planned thực nhận 3.4 → chi phí cơ hội đo được ~1.9R.

**Điều gì survives**: C2 (sweep+CISD+FVG) và C4 (target có buffer) đều có evidence và logic mạch lạc, không phụ thuộc outcome. C1 cũng được xử lý minh bạch — note đã tự nhận diện mâu thuẫn nội bộ (checklist tick "rõ ràng" nhưng văn bản ghi "tạm thời") và tự sửa cách đánh giá.

**Objections:**

**O1 · [METHOD] · fatal · attacks C3**
Claim: "Vào trên CE vì tin lệnh limit ở CE sẽ không được fill — một giả thuyết hợp lý."
Fails: đây là một free parameter chọn *sau khi có cảm giác*, không kiểm định trước, và chính note gọi nó là "story chưa kiểm chứng". Test outcome (Win) không thể xác nhận hay phủ nhận giả thuyết vì N=1.
Evidence: mục 3 "> [!important] ... một giả thuyết chưa có bằng chứng (chính bạn ghi 'tôi tự nghĩ, chưa có bằng chứng cụ thể')."
Consequence: nếu giả thuyết sai, `rr_if_ce` = 5.31 cho thấy chi phí cơ hội gần 2R mỗi lần lặp lại hành vi này — một sai lệch hệ thống, không phải nhiễu ngẫu nhiên.
Retracted by: ≥20-30 mẫu đo fill-rate tại CE vs tại Edge cùng loại POI-stack (CISD tạo 2 FVG chồng OB) — nếu fill-rate tại CE thấp hơn đáng kể (ví dụ <60%) so với Edge, giả thuyết được nâng lên PASS.
Your best answer: "lệnh đã Win, nên giả thuyết ít nhất không sai lần này." Không cứu được — outcome không phải evidence cho một quy luật fill-rate; một lần fill thành công tại Edge không nói gì về việc CE có fill được hay không, vì CE chưa từng được test trong sample này.

**O2 · [SELF-CONTRADICTION] · material · attacks C1**
Claim gốc tick "Bias D1/H4 rõ ràng, không mâu thuẫn H1" trong checklist Setup Quality.
Fails: mâu thuẫn trực tiếp với chính văn bản HTF Context ghi "Bias tại thời điểm phân tích D1 chưa được xác nhận chính xác... tạm thời tôi đang xác định là Bullish."
Evidence: mục 1 (narrative) vs mục 5 GATE checklist (tick).
Consequence: đây chính là lý do note tự hạ Grade A→B — objection này đã được note *chính nó* xử lý minh bạch, không cần phản biện thêm, chỉ cần xác nhận rule đã áp dụng đúng.
Retracted by: đã retracted — note tự sửa cách đánh giá tại mục 4, dùng "bias confirm trước entry" thay vì "bias rõ ràng ngay từ D1". Ghi nhận là objection đã đóng (không phải đang mở).

**O3 · [ARITHMETIC] · minor · attacks C5**
`rr_if_ce` = 5.31 tính từ CE 1.265785 (đúng công thức (fvg_high+fvg_low)/2 = 1.265785) và SL giữ nguyên 1.26494 — verify: (1.27027−1.265785)/(1.265785−1.26494) = 5.308 ≈ 5.31, khớp. Không có sai số đáng kể. Retracted by: đã tự retracted qua verify, ghi nhận số liệu note đúng.

**Filter**: soạn 3, cắt 0 — cả 3 đều thỏa discharge/consequence/rebuttal test; không có objection nào bị loại vì tất cả liên quan trực tiếp tới load-bearing claim hoặc đã tự đóng minh bạch.

**Opposite case (từ cùng evidence)**: Entry trên CE (Between, không phải Edge cực đoan) có thể đọc như *entry hợp lý dựa trên tốc độ resolve của CISD mạnh* — note tự đưa ra cơ chế thay thế ở mục 7 Lesson: "sau một CISD mạnh, delivery đã chuyển sang tìm premium, giá thường tiếp tục ngay từ FVG đầu tiên/cạnh gần POI chứ không nhất thiết retrace sâu về CE." Đây là một cơ chế thị trường khả dĩ (đọc CISD-momentum), khác với giả thuyết ban đầu (sợ limit trader khác). Self-objection: cơ chế "CISD mạnh → giá không về CE" là diễn giải *sau* khi thấy note gốc tự sửa, không phải điều được note dùng để quyết định entry tại thời điểm đó — nên dù plausible hơn giả thuyết gốc, nó cũng chưa được kiểm định trước outcome. **Strength: equally viable** — cả hai cách đọc (giả thuyết gốc "sợ limit trader" và cơ chế thay thế "CISD-momentum") đều unfalsifiable từ 1 mẫu.
**Distinguishing observable**: đo tốc độ retrace (số nến từ CISD tới điểm entry) trên ≥20 mẫu CISD-mạnh — nếu giá hệ thống không về CE sau CISD "mạnh" (định nghĩa được bằng % nến nuốt trọn), cơ chế CISD-momentum được ủng hộ hơn giả thuyết limit-trader.

**Verdict**: **SURVIVES, WEAKENED** — C2/C4 (setup chain + target) đứng vững; C3 (load-bearing, entry-level) bị suy yếu nghiêm trọng bởi O1 nhưng không "BROKEN" vì không có FAIL định nghĩa, chỉ là UNSUPPORTED được chính note gán đúng. `evidence_sufficiency: partial`.

**Falsification tests**:
1. Thu thập ≥20-30 mẫu "CISD tạo ≥2 FVG chồng lên POI" — đo % giá có về CE trước khi tiếp diễn. Nếu <40% về CE → giả thuyết CISD-momentum được ủng hộ hơn "sợ limit trader"; nếu ≥60% về CE → Edge/Between-entry ở đây có thể là may rủi. Đóng O1 + phần opposite case.
2. So sánh win-rate/expectancy giữa `entry_precision: CE` và `entry_precision: Between/Edge` trên toàn vault (đã có sẵn field, chỉ cần truy vấn) — nếu Between/Edge có expectancy thấp hơn CE dù win-rate ngang nhau, O1 được xác nhận bằng dữ liệu thật của chính vault.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis**: Bias D1 tentative, confirm bằng H1 sweep + M5 CISD, entry tại Between (trên CE của OB H1), TP có buffer trước DR High.

**Cần sửa** (load-bearing trước):
- C3 Entry "Between" trên CE dựa trên giả thuyết fill-rate — **UNSUPPORTED** · SKILL.md § Consequent Encroachment: doctrine không cấm entry trên CE, nhưng note không có rule khách quan biện minh cho việc bỏ qua CE để vào sớm hơn, chỉ có giả thuyết tự nhận "chưa có bằng chứng" → cần dữ liệu fill-rate CE để nâng lên PASS. **(load-bearing)**
- C1 Bias D1 "rõ ràng" (checklist gốc) — **FAIL** đã tự sửa · SKILL.md § không có mục riêng nhưng nguyên tắc chung: label không được mâu thuẫn với chính văn bản mô tả nó → note đã tự phát hiện và sửa cách đánh giá (ghi nhận là đã fix, không phải lỗi đang mở).

**PASS**: C2 (sweep old lows + 50% OB + CISD + FVG hợp lệ trong Discount — SKILL.md § CISD, § Sweep), C4 (TP có buffer trước DR High, không đua vào pool — SKILL.md § Liquidity/Target).

**Verdict**: **PARTIALLY ALIGNED** — load-bearing claim entry (C3) UNSUPPORTED (không FAIL định nghĩa), một claim phụ (C1 bias-label) đã FAIL nhưng đã được note tự sửa trong quá trình viết — verdict không được nâng lên ALIGNED chỉ vì tác giả tự sửa, vì claim entry vẫn treo.

**Notes**: Doctrine gap giống EURUSD (07-11) — canon không định nghĩa "khi nào Edge/Between-entry hợp lệ ngang CE". Batch-level: cả 2 note Edge (07-11, 07-12) đều dùng chuẩn khác nhau để tự đánh giá — 07-11 tự chấm Entry Precision 5/10 và giữ Grade A; 07-12 tự chấm Entry Precision 4/10 và hạ Grade A→B. Đây là **doctrine drift giữa 2 case cùng batch**: cùng một loại lỗi (`first_error_step: entry`, Edge/Between-entry chưa kiểm định) nhưng được phản chiếu vào Overall Grade khác nhau. 07-12 áp dụng rule nghiêm hơn (hạ cả Overall Grade) — nên dùng chuẩn 07-12 làm baseline và note lại 07-11 nên được cân nhắc hạ tương tự (không tự sửa ở đây theo ràng buộc "chỉ append").

---

## 12. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật:**
- *Ví dụ số thật*: entry 1.26615 (Between, fill_depth 21%) vs CE lý thuyết 1.265785 → `rr_if_ce` = 5.31 so với `r_multiple` thực nhận 3.4 — chênh ~1.9R mỗi lần lặp lại hành vi "vào trên CE vì sợ không fill". Xem SVG `[[MULTI-20260803-edge-vs-ce-entry.svg]]`.
- *Tổng quát hóa*: sau một CISD/displacement mạnh, tồn tại 2 giả thuyết cạnh tranh về hành vi giá — (1) giá không về CE vì cạnh tranh limit order khác, (2) giá không về CE vì momentum của CISD mạnh đẩy delivery sang premium ngay. Cả hai chưa phân biệt được bằng 1 mẫu.

**(b) Bài học quy trình/checklist:**
- Không tick "bias rõ ràng" khi văn bản phân tích cùng lúc ghi "tạm thời/chưa xác nhận" — nguồn gốc trực tiếp của self-contradiction ở note này.
- Đối chiếu `entry_precision` thực tế (Between/Edge/CE) với `rr_if_ce` mỗi lệnh để tích lũy dữ liệu chi phí cơ hội, không chỉ ghi RR đạt được.

**(c) Bài học tâm lý-hành vi:**
- Giả thuyết "trader khác cạnh tranh limit tại CE" là một narrative tự tạo ra cảm giác kiểm soát/lý trí cho một quyết định vốn là phản ứng cảm tính — pattern này giống hệt FOMO ở note EURUSD (07-11) nhưng đội lốt lý luận EV chặt chẽ hơn, nên khó nhận ra hơn.
- Note tự trừ điểm setup "chỉ vì giá không về CE" trong khi trigger (sweep+CISD+FVG+Discount) vẫn hợp lệ 100% — cần tách bạch: chấm điểm theo tính hợp lệ của trigger, không theo RR đạt được.

**(d) Rule đề xuất cho Playbook:**
- [ ] Entry-level mặc định = CE khi CISD tạo ≥2 FVG chồng POI; chỉ cho phép vào sớm hơn nếu có ≥20 mẫu backtest xác nhận fill-rate tại CE thấp hơn đáng kể.
- [ ] Cấm tick "bias rõ ràng" nếu văn bản mô tả cùng lệnh còn dùng từ "tạm thời/chưa xác nhận/tentative".
- [ ] Áp dụng nhất quán rule hạ Grade A→B cho mọi lệnh `first_error_step: entry` chưa kiểm định — bao gồm cả các lệnh trong batch này đã lỡ giữ Grade A (xem Doctrine check mục 11, Notes).

**(e) Điều KHÔNG nên học từ lệnh này:**
- KHÔNG nên học rằng "vào trên CE khi nghi ngờ CE bị cạnh tranh" là một entry rule đáng tin. Outcome Win + RR 3.4 (vẫn tốt) có thể khiến hành vi này *cảm thấy* được xác nhận, dù chính note nói rõ nó chỉ "chưa bị phủ nhận", không phải "đã được chứng minh". Nếu giá retrace đủ sâu để chạm CE trước khi tiếp diễn (không xảy ra ở đây), một Edge/Between-entry với SL cùng vị trí vẫn sống — nhưng nếu retrace vượt qua CE rồi mới quay đầu, Edge/Between-entry có thể đã bị stop trước khi CE-entry kịp fill và hưởng lợi từ đúng cú quay đầu đó.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[25-OB-Order-Block]] · [[13-FVG-Fair-Value-Gap]]
- Entry refine: [[10-Consequent-Encroachment-Mean-Threshold]] · [[26-OTE-Optimal-Trade-Entry]] · [[27-Premium-Discount]]
- Bước: [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]

---

> [!important] Việc cần bạn bổ sung (không tự suy diễn khi convert)
> - `session`: xác nhận New York AM hay PM.
> - `rr_if_ote`: chưa có định nghĩa OTE band rõ ràng cho OB này.
> - `displacement_score`, `smt_confirm`, `in_macro_time`: cần xem lại chart gốc.
> - `risk_percent`, `spread_cost`, `r_net`: chưa từng được ghi ở bản gốc.
> - Xác nhận lại quyết định hạ **Grade A → B** — nếu không đồng ý, sửa lại `grade: A` trong frontmatter.
