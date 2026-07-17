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
> File này được convert từ template backtest cũ sang **template POI & Step Decision** theo yêu cầu của Khang. Toàn bộ dữ liệu gốc (entry/SL/TP/R/result/lesson learned) được **giữ nguyên 100%**. Các field mới của template (`poi_rank`, `entry_type`, `entry_precision`, `step1-7_ok`, `first_error_step`, `confluence_score`...) **không có sẵn** trong bản ghi gốc nên được **suy luận lại** từ phần phân tích tường thuật đã viết (theo yêu cầu của Khang). Field nào không đủ căn cứ trong bài viết gốc để suy luận (SMT, CISD, macro time, NWOG/NDOG, −2SD, IDM, fill_depth_pct, risk_percent...) được **để trống** thay vì đoán — không fabricate.

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