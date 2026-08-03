---
type: backtest
backtest_date: 2026-07-08
trade_date: 2005-05-02
symbol: EURUSD
position: Long
result: Loss
session: London
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: "Yes"
poi_type: Order Block
poi_rank: 2
poi_timeframe: H1
poi_location: Discount
poi_in_ote:
ce_ote_overlap:
poi_stack: OB+FVG (nhỏ)
fvg_high:
fvg_low:
ce_price:
entry_type: Edge
entry_precision: Edge-top
limit_filled: "Yes"
fill_depth_pct:
missed_by:
step1_bias_ok: "Yes"
step2_draw_ok: "Yes"
step3_sweep_ok: "Yes"
step4_displacement_ok: "No"
step5_poi_ok: "Yes"
step6_entry_ok: "No"
step7_target_ok: NA
first_error_step: displacement
missing_step: displacement
chained_fully: "No"
liquidity_swept: "Yes"
sweep_type: Internal
displacement: "No"
displacement_score: 0
mss: "No"
fvg_valid: "No"
confluence_score: 0
smt_confirm:
cisd_confirm:
in_macro_time:
nwog_ndog_align:
sd_target_align:
idm_swept:
correlated_asset:
entry_price: 1.28639
stop_loss: 1.28392
take_profit: 1.29304
r_planned: 2.76
rr_if_ce:
rr_if_ote:
r_multiple: -1
risk_percent:
spread_cost:
r_net:
grade: D
followed_plan: "No"
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2005-05-02 — EURUSD Long — POI & Step Decision

> [!info] Ghi chú chuyển đổi template (2026-07-17)
> File này được convert từ template backtest cũ sang **template POI & Step Decision** theo yêu cầu của . Toàn bộ dữ liệu gốc (entry/SL/TP/R/result/lesson learned) được **giữ nguyên 100%**. Các field mới của template (`poi_rank`, `entry_type`, `entry_precision`, `step1-7_ok`, `first_error_step`, `confluence_score`...) **không có sẵn** trong bản ghi gốc nên được **suy luận lại** từ phần phân tích tường thuật đã viết (theo yêu cầu của ). Field nào không đủ căn cứ trong bài viết gốc để suy luận (SMT, CISD, macro time, NWOG/NDOG, −2SD, IDM, fill_depth_pct, risk_percent...) được **để trống** thay vì đoán — không fabricate.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5)                                       |
| Trade Date (dữ liệu)      | 2005-05-02                                                   |
| Position                  | Long                                                         |
| Result                    | Loss                                                         |
| Session                   | London                                                       |
| HTF Bias                  | Bullish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | Order Block (H1)                                             |
| POI Rank (8.1)            | 2 (FVG+OB)                                                   |
| POI Timeframe             | H1                                                           |
| POI Location              | Discount                                                     |
| **Entry Type**            | Edge                                                         |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | displacement                                                 |
| R Planned (gross)         | 2.76                                                         |
| R Net (sau spread)        | —                                                             |
| R Multiple (kết quả)      | -1                                                            |
| Confluence Score (0–8)    | 0                                                             |
| Grade                     | D                                                             |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang HH/HL
  - Nhịp displacement có tạo FVG khung D1
  - => Bias chuyển sang Bullish
  - Giá đang trong nhịp Pullback -> Chờ tín hiệu Reversal khung H1
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity (BSL): Previous Day/Week High
  - Sell-side liquidity (SSL): Previous Day/Week Low

![[Pasted image 20260708075445.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**:
  - LH/LL
  - Giá đang trong Bearish Bias
  - Chờ tín hiệu Reversal tại các POI, D1 Bias đang là Bullish
- **Dealing Range**:
  - High: 1.31266
  - Low 1.27670: Giá đã phá Dealing Range Low con nằm bên trong dealing range lớn -> Dời Low xuống Dealing Range chính
  - Giá đang di chuyển trong vùng Discount (đúng theo bias Bullish), tuy nhiên cấu trúc vẫn là LH/LL
- **POI chính**:
  - Order Block: 1.28503 - 1.28249
- **Liquidity cần chờ sweep**:
  - Vùng Order Block
  - Vùng Breaker Block
  - Đặc biệt quan sát giá phản ứng tại vùng Unicorn

### Phân Tích:

- Ngày 15/04/2005 Giá có 1 nhịp đẩy mạnh với các nến displacement và đồng thời tạo MSS khung H1
- Chân cú displacement đó hình thành 1 Bullish Order Block
- Giá di chuyển mạnh lên tạo cấu trúc tăng (HH/HL) sau đó và tạo đỉnh dealing range ngày 21/04/2005
- Sau đó giá tạo MSS đảo chiều và retrace về Order Block (của ngày 15/04) vào ngày 02 tháng 5/2005
- Giá quét gần tới CE của Order Block và bật lên với 1 nến lớn và các nến nhỏ (nghi ngờ - không có displacement)
- Giá sau nhịp tăng fake đó đã quét xuống sâu hơn chạm CE với 1 nến lớn và ngày sau đó bật lên với 1 nến lớn khác
- Tuy nhiên nhịp tăng đó không tạo displacement và MSS
- Giá tiếp tục quét xuyên qua CE với nến lớn và đóng nến 1 phần bên dưới CE, sau đó giá tạo 4 nến nhỏ consolidate bên dưới CE 1 khoảng nhỏ, các râu nến quét lên CE
- Sau nhịp consolidation đó giá có 1 cú displacement mạnh phá lên các đỉnh (swing high) tạo ra trong các nhịp phản ứng giả trước đó
- Giá tạo MSS với các nến displacement mạnh
- Nhịp tăng đó tạo ra FVG (đây là entry tốt hội đủ các yếu tố)
- Giá retrace về FVG
- Xuống khung nhỏ quan sát

![[Pasted image 20260708075420.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

> [!important] Ghi chú suy luận
> Bản ghi gốc chưa tách riêng "POI dùng để entry" khỏi phần mô tả model chung. Dựa trên phần phân tích M5, POI dùng để entry là **Order Block khung H1** kèm 1 FVG nhỏ tại nhịp reject đầu tiên (không phải FVG chất lượng của nhịp displacement thật sau này). Xếp hạng 8.1 tạm ước lượng **2 (FVG+OB)**.

- **POI Type đã dùng**: Order Block (H1) + FVG nhỏ tại nhịp reject đầu tiên → `poi_type: Order Block`
- **POI Rank (8.1)**: ước lượng 2/5 (FVG+OB, không phải Breaker/iFVG/Unicorn) → `poi_rank: 2`
- **POI hình thành trên khung**: H1 → `poi_timeframe: H1`
- **POI nằm ở**: Discount (đúng phía cho Long) → `poi_location: Discount`
- **POI stack**: OB + FVG nhỏ (không đủ dữ liệu để xác nhận thêm confluence khác) → `poi_stack: OB+FVG (nhỏ)`
- **CE của FVG có trùng dải OTE 62–79% không?**: không có dữ liệu ghi lại → để trống (`ce_ote_overlap`, `poi_in_ote`)
- **Bounds & CE**: OB High 1.28503 / OB Low 1.28249 (FVG M5 nhỏ dùng để entry không được ghi số cụ thể trong bản gốc → để trống `fvg_high`/`fvg_low`/`ce_price`)

> [!warning] Điểm mấu chốt của lệnh này
> Entry giá 1.28639 nằm **cao hơn cả đỉnh Order Block (1.28503)** — nghĩa là giá còn chưa thực sự đi sâu vào vùng OB khi entry được kích hoạt trên nhịp reject đầu tiên. Đây chính là bằng chứng định lượng cho lỗi FOMO đã tự nhận trong Lesson Learned.

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: Edge → `entry_type: Edge` (vào trên nhịp reject đầu tiên tại rìa OB, chưa đi sâu tới CE)
- **Entry Precision**: Edge-top (mép xa nhất, entry còn ở trên cả đỉnh OB) → `entry_precision: Edge-top`
- **Limit có được khớp không?**: Yes (lệnh có khớp, sau đó dính stop) → `limit_filled: Yes`
- **Giá đi sâu bao nhiêu vào FVG?**: không đủ số liệu FVG M5 gốc để tính chính xác → để trống `fill_depth_pct`
- **RR ghi lại**: `r_planned` = 2.76 · `rr_if_ce`/`rr_if_ote` không có dữ liệu → để trống

![[Pasted image 20260708081410.png]]

### M5 — Xác nhận và điểm vào lệnh (nguyên văn phân tích gốc)

- Giá chạm Order Block khung H1 và xuất hiện dấu hiệu reject
- Stoploss đặt bên dưới điểm sweep
- **Entry trigger**:
  - Liquidity Sweep: Quét các old lows tạo ra trước đó + quét qua 50% Order Block khung H1
  - MSS: Giá tạo MSS (tại thời điểm FOMO entry KHÔNG có MSS — nhịp fake rejection lần 1)
  - Displacement: có displacement (tại thời điểm FOMO entry KHÔNG có displacement — nhịp fake rejection lần 1)
  - FVG: Giá tạo FVG
- **Entry reason**: Giá hình thành Setup theo mô hình ICT 2022: Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là Order Block H1)
- **Invalidation reason**: Giá đóng qua đáy sweep/Order Block
- **Tôi có chờ đủ điều kiện không?** Không

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? (`Yes/No/NA`) | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | D1 bias Bullish được xác nhận đúng, có MSS + displacement + FVG D1 |
| 2 | Draw on Liquidity | Yes | Target PDH/PDL hợp lý theo bias |
| 3 | Liquidity Sweep | Yes | Có quét old lows + 50% OB trước khi bật lên |
| 4 | Displacement + MSS | **No** | Tại thời điểm entry (nhịp reject đầu tiên) KHÔNG có displacement, KHÔNG có MSS — đây là mắt xích gãy |
| 5 | POI (FVG/OB...) | Yes | POI đúng loại (Order Block), đúng phía Discount |
| 6 | Entry (retrace) | No | Vào ngay trên nhịp reject đầu tiên (FOMO), không chờ retrace sau khi chuỗi hoàn tất |
| 7 | Target | NA | Lệnh dính stop trước khi tới target, không đánh giá được |

- **First Error Step**: `displacement` — mắt xích đầu tiên gãy là thiếu Displacement + MSS tại thời điểm entry
- **Missing Step**: `displacement`
- **Đủ chuỗi 7 bước?**: No

> [!warning] Chống hindsight bias
> Đúng như bản ghi gốc tự nhận: nhịp bật đầu tiên chỉ có nến thân nhỏ/doji, chưa phá swing point nào — tại thời điểm ra quyết định, KHÔNG có bằng chứng khách quan (displacement/MSS) để entry. Đánh giá `No` cho bước 4 và 6 là đúng với dữ liệu tại thời điểm đó, không phải nhìn lại sau kết quả.

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE (pass/fail):**

- [x] Bias HTF rõ + draw xác định
- [x] Liquidity sweep trước khi bật giá
- [ ] Displacement hợp lệ tại thời điểm entry — **FAIL** (nến thân nhỏ/doji)
- [ ] MSS hợp lệ tại thời điểm entry — **FAIL**
- [ ] FVG/POI sạch + entry là retrace — **FAIL** (FVG dùng entry không hợp lệ)
- [x] Entry đúng Premium/Discount, đồng hướng bias
- [ ] Stop có logic + target rõ + R:R ≥ kế hoạch — R:R kế hoạch có (2.76) nhưng entry trigger không hợp lệ

> [!danger] GATE FAIL → đúng ra là No Trade
> Setup này fail GATE ở đúng 3 mục cốt lõi (Displacement, MSS, FVG hợp lệ). Theo nguyên tắc "GATE luôn thắng SCORE", đây lẽ ra phải là **No Trade** — không cần chấm SCORE.

**SCORE — mỗi confluence +1 (0–8):**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không | POI chỉ là OB+FVG nhỏ, rank ước lượng 2 |
| 2 | CE∩OTE overlap | Không rõ | Không có dữ liệu gốc |
| 3 | SMT confirm | Không rõ | Không có dữ liệu gốc |
| 4 | CISD confirm | Không rõ | Không có dữ liệu gốc |
| 5 | In macro time | Không rõ | Không có dữ liệu gốc |
| 6 | NWOG/NDOG align | Không r

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

> [!info] Lưu ý dữ liệu: file gốc bị cắt cụt tại mục 5 (bảng SCORE dừng giữa dòng "NWOG/NDOG align | Không r..."), không có mục 6/7/8 và không có mục "Liên kết". Đây là tình trạng file gốc, không phải lỗi đọc — phần bổ sung dưới đây append thẳng sau nội dung đang có, không tái tạo phần bị mất.

![[EURUSD-20050502-fomo-edge-entry.svg|760]]

### 9.1. Bản đồ liquidity IRL ↔ ERL tại thời điểm entry

- **Entry thực tế**: 1.28639, nằm **TRÊN cả đỉnh Order Block** (1.28503) — xác nhận lại bằng số: `entry(1.28639) > ob_high(1.28503)`. Đây là ERL/IRL kiểu gì? Entry không nằm trong OB (IRL của bản thân POI) mà nằm ở vùng "hờ" phía trên nó — nghĩa là **tại thời điểm entry, giá còn chưa thực sự đi vào IRL POI**, tức chuỗi Sweep → Displacement → POI chưa hoàn tất (khớp đúng `first_error_step: displacement`).
- **Pool nào đã bị lấy trước entry?** Theo bước 3 (Yes) — có quét old lows + 50% OB. Nhưng đây là sweep của **nhịp fake rejection lần 1** (note tự ghi "tại thời điểm FOMO entry KHÔNG có MSS/displacement"), nên sweep này chỉ xác nhận thanh khoản ngắn hạn bị chạm, không xác nhận smart money đã "dùng" nó (reject với đủ lực).
- **SL 1.28392 nằm ở đâu so với đường đi tới pool tiếp theo?** SL nằm dưới CE ước lượng của OB (1.28376, tính lại = (1.28503+1.28249)/2), tức trong vùng OB — SL không neo vào một pool ERL cụ thể phía dưới, mà theo cấu trúc OB nội bộ. Không đủ dữ liệu về pool ERL sâu hơn (không có mô tả về SSL cấu trúc bên dưới OB) → **không thể khẳng định đây có cùng họ lỗi "Unswept Liquidity Path"** như 07-10/02 và 07-17/02 — khác biệt quan trọng: họ lỗi đó là *draw ngắn hạn ngược bias/SL cùng phía pool chưa quét*, còn lệnh này là **FOMO entry trước khi chuỗi 7-bước hoàn tất** (first_error=displacement, không phải draw/sweep). Hai họ lỗi khác nhau, không nên gộp.

### 9.2. Chất lượng displacement/MSS — số thật

- `displacement_score: 0`, `confluence_score: 0`, `mss: No`, `fvg_valid: No` — đây là **GATE fail 3/3 mục cốt lõi** đã ghi ở mục 5. Entry xảy ra trên "1 nến lớn và các nến nhỏ (nghi ngờ — không có displacement)" theo đúng lời tự nhận trong phần Phân Tích mục 1.
- Đối chiếu: displacement thật (tạo MSS + FVG hợp lệ) chỉ xuất hiện **sau đó**, ở nhịp "phá lên các đỉnh (swing high)" — nhưng lệnh đã vào TRƯỚC nhịp này, tại nhịp fake rejection đầu tiên.

### 9.3. Yếu tố thời gian

- Session ghi London — không có mốc giờ cụ thể trong note để xác nhận killzone chính xác → không đủ dữ liệu chấm điểm `in_macro_time`. Không suy diễn thêm.

### 9.4. Vị trí entry trong dealing range

- Dealing range H1: High 1.31266 / Low 1.27670. Entry 1.28639 → vị trí trong range = (1.28639-1.27670)/(1.31266-1.27670) ≈ 26.9%, tức Discount sâu — đúng phía cho Long về mặt vị trí thô, nhưng vị trí Discount đúng phía **không bù được** cho việc chuỗi 7 bước (sweep→displacement→MSS→FVG) chưa hoàn tất tại điểm bấm lệnh.

### 9.5. So sánh với lệnh khác cùng mẫu trong vault

- **[[01 - Win - GBPUSD - 2014-06-25 - Long]]** — lệnh Win nhưng entry "nóng" (theo ghi chú tại 07-17/02) — cùng nhóm lỗi "entry sớm, không chờ chuỗi hoàn tất" nhưng khác outcome. So sánh cho thấy outcome không phải bằng chứng cho process: cả hai đều có vấn đề entry timing, chỉ một thắng.
- **[[03 - Win - EURUSD - 2021-07-22 - Long]]** (note 07-10/03, cùng batch) — đối lập trực tiếp: first_error=none, đủ chuỗi 7 bước, kỷ luật chờ retest sau displacement thật. Cùng loại lệnh Long/Discount/FVG nhưng khác biệt duy nhất là **có chờ đủ điều kiện hay không** — minh chứng định lượng cho việc first_error=displacement ở note này là lỗi hành vi, không phải lỗi đọc chart.

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
mode: REVIEW
instrument: EURUSD
date: 2005-05-02
timeframes_provided: "D1/H4, H1, M5 — chỉ mô tả tường thuật + 3 ảnh PNG không đọc được (evidence không truy cập)"
verdict: BROKEN
evidence_sufficiency: thin
opposite_case_strength: not viable
objections: {fatal: 2, material: 1, minor: 1}
```

**0. Evidence base.** Không có ảnh chart đọc được — 3 file PNG (`Pasted image ...`) được note nhưng nội dung hình ảnh không truy cập được từ text. Toàn bộ fact base là mô tả tường thuật (prose) + frontmatter số liệu (entry/SL/TP, các cờ Yes/No). Vì load-bearing claim (chuỗi 7 bước có hoàn tất tại điểm entry hay không) được chính bản ghi tự thuật rất rõ và nhất quán với frontmatter (`step4_displacement_ok: No`, `displacement_score: 0`), evidence cho *riêng claim đó* đủ để đánh giá — nhưng evidence cho bất kỳ claim phụ nào cần đọc giá cụ thể trên chart (vd hình dạng nến chính xác, độ dài bấc) là `thin`.

**1. Thesis + load-bearing claim.**
- C1: HTF D1 bias Bullish, xác nhận bằng MSS + displacement + FVG D1 (mục 1).
- C2: H1 có Order Block hợp lệ tại 1.28503–1.28249, đúng phía Discount (C1 → C2).
- C3: Giá quét old lows + 50% OB trước khi "bật lên" (sweep, bước 3 = Yes).
- C4 **(load-bearing)**: Nhịp bật đầu tiên (nơi entry 1.28639 xảy ra) có đủ displacement + MSS để coi là entry trigger hợp lệ.
- C5: Entry là Edge-top (1.28639, trên cả đỉnh OB), followed_plan = No.
- C6: Kết quả Loss — quét SL trước khi tới TP.

Load-bearing claim là **C4** — toàn bộ grade D và toàn bộ bài học của note phụ thuộc vào việc C4 sai (không có displacement/MSS tại thời điểm entry thật).

**2. What survives.** C1, C2, C3 không bị note nào trong chính bối cảnh này phủ nhận — HTF bias và POI selection tự thân hợp lý theo mô tả. C6 là outcome đã biết, không tranh chấp.

**3. Objections**

**O1 · [SELF-CONTRADICTION] · fatal · attacks C4 (load-bearing)**
Claim: mục 3 "Entry reason" ghi chuỗi đầy đủ "Sweep → MSS + Displacement + FVG → retrace FVG → Entry", nhưng ngay dưới, cùng mục, tự ghi "tại thời điểm FOMO entry KHÔNG có MSS — nhịp fake rejection lần 1" và "tại thời điểm FOMO entry KHÔNG có displacement — nhịp fake rejection lần 1".
Fails: mâu thuẫn nội bộ trực tiếp — hai câu liền kề khẳng định và phủ định cùng một fact.
Evidence: chính văn bản mục 3 của note, hai câu liên tiếp.
Consequence: nếu đọc theo câu đầu (chuỗi đầy đủ) thì C4 PASS và grade D là quá khắt khe; nếu đọc theo câu sau (fake rejection, không MSS/displacement) thì C4 FAIL và grade D (thậm chí No Trade theo GATE) là đúng.
Your best answer: "câu đầu mô tả *setup tổng thể* (bao gồm cả nhịp displacement thật xảy ra sau), câu sau mô tả *riêng thời điểm bấm lệnh*." Điều này hợp lý và được chính 7-Step Log ở mục 4 xác nhận (`step4: No` tại thời điểm entry) — nên objection này **narrows** thành: ghi chép mục 3 lẫn hai tầng thời gian vào một câu duy nhất là lỗi trình bày, không phải lỗi phân tích; nhưng vẫn là fatal về mặt tài liệu vì độc giả không có 7-Step Log sẽ đọc sai.
Retracted by: tách rõ hai câu trong mục 3 theo mốc thời gian (nhịp 1 vs nhịp displacement thật sau đó) — hiện 7-Step Log mục 4 đã làm đúng điều này, nên objection HELD ở tầng trình bày, RETRACTED ở tầng phân tích thực chất.

**O2 · [ARITHMETIC] · material · attacks C5**
Claim: `r_planned: 2.76`.
Evidence: entry 1.28639, SL 1.28392, TP 1.29304 → risk = 0.00247, reward = 0.00665 → RR tính lại = 2.692, không phải 2.76.
Consequence: chênh ~0.07R trên một lệnh đã Loss không đổi outcome, nhưng nếu lệch số này lặp lại có hệ thống trong log R sẽ làm sai expectancy tổng của cohort.
Retracted by: xác nhận lại nguồn số TP/SL gốc (có thể TP/SL đã bị làm tròn khác với số ghi trong frontmatter).

**O3 · [METHOD] · material · attacks C4, C5**
Claim ngầm: "followed_plan: No" đã đủ để giải thích toàn bộ nguyên nhân Loss.
Fails: không có test phân biệt — nếu displacement/MSS đã xảy ra đúng lúc entry (giả sử ngược lại O1), lệnh vẫn có thể thua vì lý do khác (vd giống 07-10/02: draw ngắn hạn sai hướng) mà note không kiểm tra. Note không hỏi "nếu đợi đủ chuỗi 7 bước rồi mới vào ở nhịp displacement thật, kết quả có khác không?" — đây là câu hỏi phân biệt sống còn giữa "vấn đề timing entry" và "vấn đề chọn draw/pool" mà 2 note Loss khác trong batch này (07-10/02) có phân biệt rõ.
Consequence: nếu nguyên nhân thực chất còn có lớp draw-on-liquidity sai (như 07-10/02), thì rule sửa "chờ đủ 7 bước" chưa chắc đủ để tránh lỗi tương tự lần sau.
Retracted by: đọc lại chart tại nhịp displacement thật (sau fake rejection) — nếu draw/pool tại thời điểm đó hợp lý và không có unswept liquidity path nằm cùng phía SL, objection được retract.

**O4 · [UNSUPPORTED] · minor** — `poi_in_ote`, `ce_ote_overlap`, `fill_depth_pct`, `risk_percent` đều bỏ trống hợp lý (không có dữ liệu gốc) — không phải lỗi, ghi nhận để không lặp lại việc suy diễn số liệu không có căn cứ. Retracted by: không cần — đây là cách xử lý đúng của note gốc (`null` trung thực thay vì đoán).

Đã soạn 4 objections, cắt 0 (tất cả đạt bài test discharge/consequence/rebuttal — O1 sống sót nhờ narrow, không bị xóa vì vẫn có giá trị cảnh báo trình bày).

**4. Opposite case.** Từ cùng evidence, thử dựng case: "Đây thực chất KHÔNG PHẢI FOMO — đây là entry hợp lệ tại nhịp phản ứng đầu tiên của một OB đã được test nhiều lần (nhịp 1 phản ứng, nhịp 2 phản ứng lại gần CE), và displacement/MSS mà note yêu cầu là tiêu chuẩn quá khắt khe cho một OB đã chứng minh sức mạnh qua 2 lần chạm."
- Load-bearing claim của case này: "OB đã được test đủ để coi là 'chứng minh' trước cả khi có MSS xác nhận trên timeframe entry."
- Tự phản bác: doctrine ICT 2022 (xem mục 11) yêu cầu MSS/displacement là bước xác nhận entry riêng biệt, không thể thay bằng "đã test nhiều lần" — nhiều lần test một OB mà chưa có MSS mỗi lần chỉ tăng khả năng OB đó sẽ bị phá (absorption), không tăng khả năng nó giữ.
- Strength label: **not viable** — không có fact nào trong note support việc bỏ qua yêu cầu MSS/displacement; bản thân note đã tự nhận nhịp 1 là "fake" và nhịp phá lên sau đó mới có MSS thật.
- Distinguishing observable: nếu nhịp 1 (entry point) mà không hề có MSS/displacement nào xảy ra sau đó, và giá đảo chiều mạnh ngay tại đó thành công — thì case ngược sẽ mạnh hơn. Nhưng thực tế note ghi giá tiếp tục quét sâu hơn sau nhịp 1, khớp với thesis gốc.

**5. Verdict: BROKEN.**
Load-bearing claim C4 fails trên self-contradiction (O1) khi đọc ở tầng phân tích thời điểm entry — nhưng ĐÃ được chính 7-Step Log của note tự sửa đúng (`step4_displacement_ok: No`). Vì vậy "BROKEN" ở đây áp dụng cho **cách trình bày mục 3**, không phải cho verdict cuối của note (note đã tự đúng ở mục 4-8). Điều tôi thất bại không phá được: chuỗi lý luận displacement=0/MSS=No tại thời điểm entry — dữ liệu này nhất quán và không tìm được cách bẻ nó. Điều critique này không xác lập: không thể xác nhận đây có phải cùng họ lỗi Unswept Liquidity Path hay không (thiếu dữ liệu pool ERL sâu hơn); không đọc được chart gốc nên mọi nhận định về hình dạng nến là theo lời tự thuật, không phải quan sát độc lập.

**6. Falsification tests (tối đa 3)**
1. Đọc lại 3 ảnh PNG gốc (`Pasted image 20260708075445/075420/081410`): xác nhận nhịp 1 có thực sự không có body-close phá swing nào không. Nếu có → O1 đổi thành objection thật (không chỉ trình bày) và C4 cần re-đánh giá. Đóng O1.
2. Kiểm tra 10+ backtest khác trong vault có `first_error_step: displacement` — tính win rate riêng nhóm này so với nhóm `first_error: none`. Nếu nhóm displacement-fail vẫn có win rate đáng kể → nghi ngờ rule "GATE luôn thắng SCORE" cần nới, đóng O3 theo hướng khác.
3. Truy lại số TP/SL gốc trước khi convert template — xác nhận RR đúng là 2.76 hay 2.692. Đóng O2.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Lệnh Long tại Order Block H1 Discount, entry Edge-top ngay trên nhịp fake rejection đầu tiên, thiếu displacement + MSS tại thời điểm entry, dẫn tới Loss với followed_plan=No.

**Cần sửa** (load-bearing trước):
- C4 "entry tại nhịp displacement + MSS hợp lệ" — **FAIL** · nến thân nhỏ/doji không tạo body-close phá swing, không đạt tiêu chuẩn Displacement theo SKILL.md § Displacement ("Expansion một chiều, năng lượng cao, để lại imbalance. Move lệt bệt overlapping không phải displacement") → fix: gọi đúng tên nhịp 1 là "fake rejection / internal reaction", không dùng entry trigger đó làm cơ sở entry.  ← (load-bearing)
- C_MSS "MSS đã có tại entry" — **FAIL** · SKILL.md § MSS yêu cầu "phá swing ngược short-term move" với body close, kế thừa từ C4 (FAIL do cùng gốc) — không tính lỗi riêng.
- C_FVG "FVG entry hợp lệ" (`fvg_valid: No` đã tự ghi) — kế thừa từ C4, không tính lỗi riêng.
- C_sweep "Sweep bước 3 hợp lệ" — **UNSUPPORTED** · SKILL.md § Sweep yêu cầu "quét liquidity tại level có tên và được dùng (reject)"; note ghi "quét old lows + 50% OB" nhưng không nêu tên cụ thể level nào (PDH/PDL/EQL?) → fix: ghi rõ tên level bị quét để nâng từ UNSUPPORTED lên PASS.
- C_OTE "poi_in_ote/ce_ote_overlap" — không đánh giá được, để trống đúng cách, không phải AMBIGUOUS vì không có claim nào được đưa ra để kiểm.

**PASS:** C1 (D1 bias Bullish), C2 (OB Discount đúng phía) — không có vấn đề định nghĩa, có evidence tường thuật hỗ trợ.

**Verdict:** NOT ALIGNED — load-bearing claim (C4, entry trigger hợp lệ) FAIL theo định nghĩa Displacement/MSS canon; note tự đã nhận diện đúng điều này ở 7-Step Log (`step4: No`, GATE fail 3/3). Đây là trường hợp hiếm mà phân tích gốc *tự chấm đúng* theo doctrine — Doctrine check ở đây xác nhận lại, không phát hiện lỗi ẩn.

**Notes:** Doctrine gap nhỏ — SKILL.md không phân biệt rõ "sweep old lows" (không tên) khác gì với "sweep named level" về mức độ UNSUPPORTED vs FAIL; áp dụng nguyên tắc AMBIGUOUS/UNSUPPORTED theo doctrine gap rule (không tự đặt chuẩn khắt khe hơn canon).

---

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật

1. **Entry Edge-top (giá còn ở ngoài POI, chưa đi sâu tới CE) + thiếu displacement/MSS = FOMO có thể đo bằng số.** Ví dụ số thật: entry 1.28639 > OB high 1.28503 — chênh +13.6 pip **phía ngoài** OB, không phải sâu trong OB. Tổng quát hóa: bất kỳ lúc nào entry price nằm ngoài biên POI đã vẽ, đó là dấu hiệu khách quan (không cần cảm giác) rằng entry đến trước khi POI được "chạm" đúng nghĩa.
2. **RR đẹp trên giấy (2.76 hoặc 2.69 tính lại) không bù được entry trigger thiếu.** Cùng bài học đã thấy ở 07-10/02 (RR 3.39) và 07-17/02 (RR 3.40) — đây là pattern lặp lại ba lần trong vault: RR cao là biến độc lập với chất lượng entry trigger, không nên dùng để tăng confidence.

### (b) Bài học quy trình/checklist

- GATE fail ở đúng 3 mục cốt lõi (Displacement, MSS, FVG hợp lệ) lẽ ra phải chặn lệnh hoàn toàn ("No Trade") theo đúng nguyên tắc "GATE luôn thắng SCORE" mà các note khác trong vault (07-17/02) đã áp dụng nhất quán — note này KHÔNG có mục GATE/SCORE tách bạch như các note sau, đây là khác biệt template giữa các thời kỳ convert.
- `followed_plan: No` được ghi trung thực — đây là hành vi đúng cần giữ (thừa nhận vi phạm kỷ luật thay vì tick "Yes" cho đẹp), đối lập với 07-10/03 nơi `followed_plan` ban đầu ghi sai và phải sửa lại.

### (c) Bài học tâm lý-hành vi

- Đây là mẫu **FOMO tại lần chạm đầu tiên của một POI quan trọng** — đúng hành vi mà note 07-10/01 (Unicorn) tự đối chiếu và nói rõ "quá khứ tôi đã từng vào lệnh vội tại vùng CE khi thấy giá retrace về vùng POI quan trọng" (mục "Phân Tích", dòng về hành vi quan sát chứ không vào liền). Note 07-08/01 (file này) rất có thể chính là lệnh được nhắc tới đó — cùng một behavioral root cause, đã được sửa 5 ngày backtest sau (07-10 vs 07-08).
- `confidence: 3` (thang không rõ /5 hay /10) được ghi tại thời điểm entry sai — một dấu hiệu confidence không tương quan với chất lượng setup, cần theo dõi qua nhiều lệnh để xem có phải confidence cao thường đi cùng vi phạm quy trình hay không (n=1, chưa đủ kết luận).

### (d) Rule đề xuất cho Playbook

- [ ] Không entry nếu GATE fail ≥1 mục cốt lõi (Displacement/MSS/FVG hợp lệ), bất kể vị trí Discount/Premium đúng phía.
- [ ] Log entry price so với biên POI đã vẽ (trong/ngoài, cách bao nhiêu pip) làm field bắt buộc — dùng để phát hiện Edge-entry khách quan thay vì tự nhận cảm tính.
- [ ] Khi note tường thuật có 2 câu liền kề mô tả cùng một event theo 2 cách khác nhau (chuỗi đủ vs thiếu), bắt buộc tách theo mốc thời gian rõ ràng (nhịp nào, giờ nào) trước khi lưu.

### (e) Điều KHÔNG nên học từ lệnh này

- Đây là Loss — không có rủi ro outcome bias theo hướng "vì thắng nên hợp lý hóa", nhưng vẫn có rủi ro **ngược**: không nên kết luận "mọi entry Edge-top đều xấu" từ n=1 case này — cần đối chiếu với các entry Edge hợp lệ khác (nếu có trong vault) trước khi biến thành hard rule tuyệt đối thay vì soft flag.
- Không nên gộp lỗi này vào cùng nhóm "Unswept Liquidity Path" (07-10/02, 07-17/02) — root cause khác nhau (entry timing/FOMO vs draw-on-liquidity sai hướng). Gộp nhầm sẽ làm loãng rule sửa lỗi thực sự cần cho mỗi nhóm.
