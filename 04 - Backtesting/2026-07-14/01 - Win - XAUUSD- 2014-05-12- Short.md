---
type: backtest
backtest_date: 2026-07-14
trade_date: 2014-05-12
symbol: XAUUSD
position: Short
result: Win
session: New York AM
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct: Yes
poi_type: FVG
poi_rank: 1
poi_timeframe: M1
poi_location: Premium
poi_in_ote: Yes
ce_ote_overlap: Yes
poi_stack: H1 FVG (OTE) + M1 FVG2 (post-MSS)
fvg_high: 1301
fvg_low: 1300
ce_price: 1300.5
entry_type: CE
entry_precision: CE
limit_filled: Yes
fill_depth_pct:
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: Yes
step5_poi_ok: Yes
step6_entry_ok: Yes
step7_target_ok: Yes
first_error_step: none
missing_step: none
chained_fully: Yes
liquidity_swept: Yes
sweep_type: Internal
displacement: Yes
displacement_score:
mss: Yes
fvg_valid: Yes
confluence_score: 2
smt_confirm: No
cisd_confirm: No
in_macro_time: No
nwog_ndog_align: No
sd_target_align: No
idm_swept: Yes
correlated_asset: none
entry_price: 1301.562
stop_loss: 1304.113
take_profit: 1294.173
r_planned: 2.9
rr_if_ce:
rr_if_ote:
r_multiple: 2.9
risk_percent: 0.5%
spread_cost:
r_net:
grade: A-
followed_plan: Yes
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2014-05-12 — XAUUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi (2026-07-17)
> File này được chuyển từ bản backtest gốc (template cũ) sang **Backtest template - POI & Step Decision**. Toàn bộ phân tích gốc được giữ nguyên; các field mới (poi_rank, step-log, confluence_score...) được suy ra từ chính nội dung đã viết — **không bịa thêm dữ liệu**. Field nào không đủ căn cứ trong bản gốc được để trống hoặc gắn cờ ⚠️ bên dưới, thay vì đoán số.
>
> ⚠️ **Mâu thuẫn cần bạn đối chiếu lại chart**: văn bản gốc mô tả FVG2 (POI entry) ở khoảng **1301–1300** (CE ≈ 1300.5), nhưng `entry_price` chính thức (đã sửa ngày 2026-07-15 để khớp R=2.9) là **1301.562** — cao hơn hẳn dải ước tính này. Có thể FVG2 thực tế nằm cao hơn, hoặc entry là ở Edge-top chứ không phải đúng CE. `fvg_high/fvg_low/ce_price` bên trên là số ước tính từ mô tả gốc, không phải số đo lại từ chart — cần bạn xác nhận.
> ⚠️ `session` suy từ mốc giờ 19:00–19:20 (giờ VN, UTC+7) trong bài viết ≈ 08:00–08:20 EDT — sát giờ mở NY AM Kill Zone. Gốc chỉ ghi "New York" chung chung, chưa xác nhận có đúng NY AM không.
> ⚠️ `displacement_score`, `confidence`, `risk_percent`, `spread_cost`, `r_net`, `rr_if_ce`, `rr_if_ote`, `fill_depth_pct` không có căn cứ số trong bản gốc → để trống, không đoán.
> `confluence_score = 2` chỉ tính 2 mục có bằng chứng rõ trong bài viết (CE/OTE overlap + inducement bị quét); các mục còn lại (SMT, CISD, macro time, NWOG/NDOG, SD target) **không được đánh giá tại thời điểm log gốc** — không mặc định là "No tuyệt đối", chỉ là chưa có ghi chú xác nhận.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | XAUUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5→M1)                                    |
| Trade Date (dữ liệu)      | 2014-05-12                                                   |
| Position                  | Short                                                        |
| Result                    | Win                                                          |
| Session                   | New York AM ⚠️ (suy từ giờ, xem ghi chú chuyển đổi)          |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | FVG (M1 FVG2, nested trong H1 FVG/OTE)                       |
| POI Rank (8.1)            | 1 (FVG đơn)                                                  |
| POI Timeframe             | M1 (POI ngữ cảnh H1)                                         |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | none                                                         |
| R Planned (gross)         | 2.9                                                          |
| R Net (sau spread)        | (chưa có dữ liệu spread)                                     |
| R Multiple (kết quả)      | 2.9                                                          |
| Confluence Score (0–8)    | 2                                                             |
| Grade                     | A-                                                           |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

> [!check] Toàn vẹn dữ liệu — đã sửa ở bản gốc (2026-07-15)
> Note tạo bằng cách copy 1 lệnh cũ nên còn sót 2 điểm không khớp giữa frontmatter và Summary table; đã đối chiếu chart và lập luận để sửa: (1) `entry_price` 1300.5 → 1301.562 (khớp Summary table và cho R = 2.9); (2) `grade` A → A- (đồng bộ frontmatter, hạ điểm vì lỗi toàn vẹn dữ liệu + mơ hồ TF entry). Xem Rule R-BT-01 → R-BT-06 ở mục 7.3.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Phía bên trái giá đã quét hết các lower high trong nhịp tăng sau đó sau đó tạo 1 đỉnh (Long Term High)
  - Trước nhịp tăng 31/12/2013, hình thành 1 cú quét thanh khoản, quét đáy trước sau đó đóng nến lại trong range và tăng (1)
  - Nhịp tăng đồng thời tạo Displacement + Order Block (2)
  - Tiếp sau đó là nhịp tăng Bullish với các HH/HL → Thanh khoản tích tụ dần ở các đáy này
  - Sau nhịp tạo đỉnh (long term high) giá hình thành 1 Bearish MSS với nhịp displacement + FVG (3)
  - Trong Dealing Range lớn giá đang trong vùng Premium (4)
  - (1) + (2) + (3) + (4) => Bias Bearish
  - Giá đang trong vùng Premium, thanh khoản Buy Side đã bị lấy, mục tiêu kế tiếp là Sell Side Liquidity và vùng Order Block
- **Dealing Range**: High 1315.691 / Low 1277.416 → giá retrace lên **Premium / OTE** cho setup Short
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side (BSL): D1 Dealing Range High 1392.098 · Bearish Order Block 1387.437
  - Sell-side (SSL): Dealing Range Low 1182.661 · old lows tạo ra trong nhịp tăng Long Term High · Order Block · H1 Dealing Range Low

![[Pasted image 20260714063937.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Sau Long Term High, giá hình thành Bearish MSS + Displacement (đồng bias với D1); LH/LL, order flow đang giảm.
- **Dealing Range (nhịp retrace cho setup Short)**: High 1315.691 (fib 1.0) / Low 1277.416 (fib 0.0) — giá retrace lên vùng Premium/OTE.
- **POI chính (H1)**: Bearish OB vùng ~0.786 (≈1308–1310) · Bearish FVG H1 (từ nhịp giảm 7/5) nằm trong vùng OTE.
- **Liquidity cần chờ sweep**: internal high của consolidation + cạnh trên H1 FVG (gần CE của liquidity void). Sau sweep → draw về Sell-side/OB phía dưới.

### Phân tích

- **Context**: Sau khi quét SSL 2/5/2014 19:00 → displacement tăng, HH/HL tạo đỉnh 5/5/2014 19:00 → consolidation → 7/5/2014 14:00 Bearish Displacement mạnh tạo FVG → 8/5/2014 00:00 consolidation → 12/5/2014 17:00 nến Bearish Displacement quét đáy cũ, đóng ngoài range, tạo H1 Dealing Range Low → giá vào Discount nhưng bias vẫn Bearish → chờ retrace lên Premium.
- **Lệnh**: 12/5/2014 19:00 nến displacement mạnh phá 50% Dealing Range, trở lại Premium; giá quét lên cạnh trên Bearish FVG H1 (gần CE liquidity void 7/5), đóng nến lại trong range, xuất hiện nến giảm ngay sau đó → xuống M5 quan sát.

![[Pasted image 20260714074100.png]]

### M5/M1 — Xác nhận và điểm vào lệnh

- Sau sweep cạnh trên H1 FVG + chạm CE liquidity void, giá bật ra đóng lại trong H1 FVG, xuất hiện nến giảm.
- M5: nến Bearish displacement, tạo Short Term Low lúc 12/05/2014 20:00; nhịp displacement kế tiếp phá STL tạo MSS. M5 bóng nến chồng lấp, không tạo FVG rõ → xuống M1.
- M1: 2 FVG — FVG1 (1302–1301, chưa có MSS, loại) và **FVG2 (1301–1300, đã có MSS)** → entry tại CE FVG2.
- **Entry trigger**: quét cạnh trên FVG + CE liquidity void + sweep nội bộ đáy khi tạo MSS; MSS bằng nến displacement lúc 19:20; displacement tạo FVG.
- **Entry reason**: chuỗi Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là FVG H1), FVG nằm giữa 50%–0.618 (OTE).
- **Invalidation**: giá đóng qua FVG H1.
- **Chờ đủ điều kiện?** Có.

**M5:** ![[Pasted image 20260714075254.png]]
**M1:** ![[Pasted image 20260714075206.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: FVG (M1 FVG2), lồng trong bối cảnh H1 FVG/OTE
- **POI Rank (8.1)**: 1/5
- **POI hình thành trên khung**: M1 (bối cảnh H1)
- **POI nằm ở**: Premium ✓ (đúng phía cho Short)
- **POI stack**: H1 FVG (OTE 0.5–0.618) + M1 FVG2 (post-MSS)
- **CE của FVG có trùng OTE 62–79%?**: Yes (H1 FVG nằm giữa 50–0.618)
- **Bounds & CE (ước tính, ⚠️ xem cảnh báo đầu file)**: FVG High ≈1301 · FVG Low ≈1300 · CE ≈1300.5

![[Pasted image 20260714075254.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE
- **Entry Precision**: CE (theo mô tả gốc "Entry khi giá retrace về CE của FVG 2")
- **Limit có khớp không?**: Yes
- **Giá đi sâu bao nhiêu vào FVG?**: không đo được chính xác — số fvg_high/low chỉ là ước tính, không đối chiếu lại chart (xem cảnh báo)
- **RR ghi lại**: r_planned 2.9 · rr_if_ce/rr_if_ote không tách biệt trong bản gốc

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes | `step3_sweep_ok` |
| 4 | Displacement + MSS | Yes | `step4_displacement_ok` |
| 5 | POI (FVG) | Yes | `step5_poi_ok` |
| 6 | Entry (retrace) | Yes | `step6_entry_ok` |
| 7 | Target | Yes | `step7_target_ok` |

- **First Error Step**: none
- **Missing Step**: none
- **Đủ chuỗi 7 bước?**: Yes

---

## 5. Setup Quality & Confluence

**GATE**: Bias rõ · Sweep trước displacement · Displacement hợp lệ · MSS hợp lệ · FVG sạch, entry retrace · Đúng Premium/Discount · SL có logic + target rõ + RR ≥ kế hoạch → **PASS**.

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không (hạng 1) | *(suy từ poi_rank)* |
| 2 | CE FVG trùng OTE 62–79% | Có | `ce_ote_overlap` |
| 3 | SMT divergence tại sweep | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | Không có ghi chú | `cisd_confirm` |
| 5 | Entry trong macro time | Chưa đánh giá | `in_macro_time` |
| 6 | Trùng NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | Target trùng -2SD/ERL | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Có (sweep nội bộ) | `idm_swept` |

- **Score**: 2/8 → theo thang quy đổi rơi vào **C** về mặt điểm số thuần, nhưng grade tổng **A-** phản ánh chất lượng process + kết quả thực tế (win, followed plan), không chỉ điểm confluence. Ghi chú: các mục "chưa đánh giá" khác với "No xác nhận" — cần review lại chart nếu muốn chấm điểm confluence chính xác hơn.
- **Cặp tương quan soi kèm**: none (không ghi chú trong bản gốc)

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng?**
  - Kiên nhẫn chờ H1 đồng Bias với khung D1 (Bearish)
  - Chờ M5, M1 confirm Bias
  - Chờ H1 retrace về vùng Premium/OTE
  - Có quét thanh khoản + CISD (ghi chú gốc, chưa tách bạch kỹ thuật CISD)
- **Thị trường có cảnh báo trước không?**: Có Displacement, có MSS, có FVG
- **POI đã chọn có phải lựa chọn tốt nhất?**: OB H1 (~0.786) chưa từng được test — lệnh thắng nhờ LTF confirm sớm hơn, nhưng nếu giá retrace sâu hơn về OB, SL 1304 đã bị quét trước khi tới đó.
- **Fill**: khớp đúng kỳ vọng.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu vào lại, làm gì khác?**: Cần thêm backtest để biết khi nào nên vào tại cạnh và khi nào vào tại CE.

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Setup Short chuẩn ICT 2022 (Sweep → Displacement → MSS → FVG entry trong OTE), quy trình top-down tốt; điểm yếu lớn nhất KHÔNG nằm ở kỹ thuật mà ở **nhiễm dữ liệu journal** (frontmatter/số liệu lẫn từ một setup khác) — thứ đe doạ trực tiếp tính hợp lệ của mẫu backtest.

### 7.1. Bài học kỹ thuật

**Root cause (duy nhất)**: Kỷ luật tôn trọng trọn vẹn chuỗi ICT 2022 theo đúng thứ tự và KHÔNG ép entry ở khung không rõ ràng — khi M5 cho nến bóng dài chồng lấp, xuống M1 tìm cấu trúc rõ thay vì đoán.

**Triệu chứng tích cực**: Entry nằm trong OTE (0.5–0.618), RR 2.9 với SL chỉ ~2.5 giá; phân biệt được FVG1 (trước MSS → bỏ) và FVG2 (sau MSS → vào); Bias Bearish dựng từ 4 tầng confluence.

**Cơ chế thị trường**: Sau khi lấy Buy-side ở Long Term High (~1392) và quét lên CE của Bearish FVG H1, giá bị từ chối tại Premium/OTE. Nhịp Bearish Displacement M1 tạo MSS + FVG; retrace về CE FVG2 là nơi smart money tiếp tục phân phối → giá tìm Sell-side/OB phía dưới. TP 1294 là "partial draw", không phải toàn bộ draw D1 (~1200).

**Cần xác minh thêm**: "Quét CE của liquidity void" ≠ "quét liquidity pool" — cần ghi rõ đã quét POOL nào (giá) hay chỉ phản ứng PD array. Entry ở 0.618 trong khi POI H1 (OB) nằm ở 0.786 chưa được test — SL đang neo theo STH M1, không neo theo invalidation POI H1.

### 7.2. Pattern lặp lại

1. **Nhiễm dữ liệu do copy-paste (nghiêm trọng nhất)** — file gốc từng lẫn nội dung của setup Long/NAS100 khác; đã dọn sạch. Với backtest, dữ liệu bẩn = mẫu thống kê vô nghĩa → vẫn là rủi ro số 1 của dự án.
2. **Outcome bias khi chấm điểm** — Grade hạ về A- vì lỗi toàn vẹn dữ liệu + mơ hồ TF entry, chấm theo *process sạch*, không theo kết quả.
3. `entry_timeframe` xác nhận là **M1** (khung thực sự bấm entry).

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **R-BT-01** — Làm sạch file trước khi lưu: kiểm symbol/position/bias/số Dealing Range/POI khớp đúng instrument.
- [ ] **R-BT-02** — Bias khớp hướng lệnh (`htf_bias` khớp Short→Bearish).
- [ ] **R-BT-03** — `entry_timeframe` = khung THỰC SỰ bấm entry.
- [ ] **R-BT-04** — Tách bạch: quét POOL nào (giá) vs phản ứng PD array nào.
- [ ] **R-BT-05** — Neo SL theo invalidation POI (H1) hay STH LTF entry; ghi rõ đánh đổi RR/xác suất.
- [ ] **R-BT-06** — Thống nhất hệ ngày (UTC+7) và năm dữ liệu replay.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | (không có điểm chi tiết trong bản gốc) |
| POI Selection | — |
| Liquidity Sweep | — |
| Displacement/MSS quality | — |
| Entry Precision & Fill | — |
| Risk Management | — |

**Overall Grade**: **A-** (bản gốc không chấm điểm theo 6 tiêu chí chi tiết — chỉ có Overall Grade; không tự suy ra điểm thành phần để tránh bịa số liệu).

> [!tip] Chống curve-fitting
> Trigger (sweep + displacement + POI hợp lệ) nhận diện được trước outcome. Nhưng file này là bài học lớn nhất về **kỷ luật vệ sinh dữ liệu**, không chỉ về kỹ thuật entry.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI: [[13 - FVG  - Fair Value Gap]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- Timing: [[18 - Kill Zones]]
- Dashboard: [[_Backtest Dashboard]]
