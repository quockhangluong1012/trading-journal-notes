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

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

### 9.1. Bản đồ Liquidity IRL ↔ ERL tại thời điểm entry

- **Pool đã bị lấy trước entry (19:20, 12/5)**: BSL tại Long Term High (~1392, external, đã lấy từ nhịp tăng trước); SSL nội bộ tại đáy tạo H1 Dealing Range Low 1277.416 (lấy lúc 12/5 17:00, internal); swing high nhỏ trên M1 (nơi tạo FVG1 "chưa MSS") — internal, bị quét khi giá tạo MSS lúc 19:20.
- **Pool CHƯA bị lấy khi entry khớp (1301.562)**: SSL cấu trúc tại H1 DR Low 1277.416 (còn cách xa ~24 điểm — đây đúng là draw on liquidity mục tiêu, không phải nguy cơ); và quan trọng hơn — **OB H1 ~0.786 (≈1308–1310) chưa được test**. Note gốc tự nhận điều này ở mục 6 ("OB H1 (~0.786) chưa từng được test — lệnh thắng nhờ LTF confirm sớm hơn"). SL 1304.113 nằm GIỮA entry (1301.562, ~0.618) và OB 0.786 chưa test — nghĩa là nếu giá đã retrace sâu hơn tới OB trước khi giảm, SL đã bị quét bởi chính pool đó, giống chính xác cơ chế thua của [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short|lệnh Loss 19/5]] (BB nông bị quét trên đường tới OB sâu). Ở đây lệnh thắng — nhưng không phải vì cấu trúc an toàn hơn, mà vì giá không đi xa tới mức đó trước khi đảo chiều (may mắn tình huống, không phải ưu điểm hệ thống).
- **SL nằm phía nào so với pool chưa lấy?**: SL 1304.113 nằm GIỮA hai pool chưa lấy (OB 0.786 phía trên, H1 DR Low phía dưới) — không nằm chồng lên đường đi tới OB (đường đó là 1301.562→~1309, SL 1304.113 nằm trên đường này). Về logic thanh khoản, SL của lệnh này CŨNG lộ rủi ro tương tự BB/RB, chỉ là chưa bị hiện thực hóa.

### 9.2. Chất lượng Displacement/MSS

- H1: displacement rõ (nến 12/5 17:00 phá 50% DR, đóng ngoài range) → đủ chuẩn.
- M5: note gốc tự nhận "bóng nến chồng lấp, không tạo FVG rõ" — tức displacement M5 KHÔNG đạt chuẩn objective (không để lại imbalance 3-nến sạch). Đây là điểm yếu bị bỏ qua khi chấm A-: theo đúng logic đã áp dụng cho các lệnh Loss trong cụm (M5 không FVG → no-trade), lệnh này lẽ ra cũng phải dừng ở M5, nhưng lại tụt xuống M1 tìm trigger — cùng hành vi "tụt khung moi setup" mà chính vault đã gắn nhãn là pattern nguy hiểm ở 3 lệnh Loss khác trong cụm.
- M1: displacement 19:20 tạo MSS + FVG2 hợp lệ về hình thức (thân nến rõ, imbalance 3-nến).

### 9.3. Yếu tố thời gian

- Entry ước tính ~19:20–19:35 giờ dữ liệu (theo mô tả "nến displacement lúc 19:20"), quy đổi UTC+7 → khoảng 08:20–08:35 EDT nếu giờ gốc là UTC — sát mở NY AM Killzone, nhưng session ghi "New York AM" đã bị gắn cờ ⚠️ trong note gốc là suy luận, chưa xác nhận cứng.
- Tốc độ resolve: R=2.9 đạt trong khung thời gian không được ghi rõ trong note — không đánh giá được tốc độ hit TP.

### 9.4. Vị trí entry trong Dealing Range

- Entry 1301.562 rơi ngay dưới mốc 0.618 (1301.070) — theo tính toán lại, CE FVG2 ước tính (1300.5) nằm ở 0.578, THẤP HƠN biên OTE 0.618, tức theo số ước tính gốc, entry gần mép ngoài Premium, không hẳn "sweet spot" 0.618-0.786 mà note tự nhận. Với entry_price chính thức (1301.562), vị trí đúng là ~0.618 (biên dưới OTE) — khớp OTE nhưng ở mép, không ở giữa.

### 9.5. So sánh với các lệnh cùng mẫu trong vault

- Cùng dùng POI rank thấp (FVG rank 1) nhưng THẮNG, đối lập với [[2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short|Loss 14/5 sáng]] (Rejection Block, ngoài thang rank) và [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short|Loss 19/5]] (Breaker rank 3) — cả hai lệnh Loss dùng POI "hạng cao" hơn về danh xưng nhưng thua, còn lệnh FVG rank 1 lại thắng. Đây chính là nghịch lý được nêu trong nhiệm vụ batch: thang POI rank của note gốc gán rank cao cho RB/Breaker theo độ hiếm/độ "cao cấp" của khái niệm, không phải theo xác suất thắng thực nghiệm quan sát được trong 4 lệnh XAU này.
- Cùng ngày 14/5 với [[2026-07-14/03 - Win - XAUUSD- 2014-05-14 - Short|lệnh Win chiều 14/5 (BPR)]] — xem phân tích quan hệ chi tiết ở note đó.

![[XAUUSD-20140512-poi-rank-paradox.svg|760]]

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
type: devils-advocate
mode: REVIEW
instrument: XAUUSD
date: 2014-05-12
timeframes_provided: [D1/H4 (mô tả), H1 (mô tả + 1 ảnh không đọc được), M5 (mô tả + 1 ảnh), M1 (mô tả + 2 ảnh)]
verdict: SURVIVES, WEAKENED
evidence_sufficiency: thin
opposite_case_strength: weaker but non-trivial
objections: {fatal: 1, material: 2, minor: 1}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base**: Toàn bộ ảnh (`Pasted image ...png`) không đọc được từ text — chỉ có mô tả bằng lời + số liệu frontmatter. Evidence là "note tự thuật", không phải chart trực tiếp → mọi `[CHART]` objection dưới đây thực chất dựa trên số liệu do người dùng ghi, không phải quan sát độc lập. `evidence_sufficiency = thin` vì load-bearing claim (chất lượng displacement M5) không thể verify ngoài lời tự nhận của chính note.

**1. Thesis + load-bearing claim**: C1 Bias D1 Bearish (từ 4 tầng: sweep, OB, MSS, Premium). C2 H1 retrace vào Premium/OTE, đối diện H1 FVG. C3 M5 KHÔNG tạo FVG sạch (tự nhận). C4 (từ C3) tụt xuống M1 tìm trigger. C5 M1 tạo MSS + FVG2 hợp lệ hình thức. C6 (từ C1+C2+C5) Entry tại CE FVG2 hợp lệ theo chuỗi 7 bước. **Load-bearing: C6, nhưng C6 kế thừa trực tiếp từ C4 — nếu "M5 không FVG = no-trade" (rule mà chính vault áp dụng cho 3 lệnh Loss khác) thì C4→C6 sụp, bất kể M1 đẹp ra sao.**

**2. What survives**: C1, C2 — bias và context D1/H1 có 4 tầng lý do rõ, không mâu thuẫn nội tại. C5 — hình thức MSS+FVG M1 đạt chuẩn kỹ thuật (thân nến rõ, imbalance 3-nến theo mô tả).

**3. Objections**

**O1 · [METHOD] · fatal · attacks C4, C6 (load-bearing)**
Claim: "M5 bóng nến chồng lấp, không tạo FVG rõ → xuống M1" rồi vẫn entry.
Fails: quy trình tự-mâu-thuẫn — chính rule mà note author áp dụng để loại 3 lệnh Loss khác trong cùng cụm ("M5 không displacement/FVG sạch → no-trade", xem 9.4 của Loss 14/5 và Loss 19/5) không được áp dụng ở đây vì kết quả là Win.
Evidence: chính văn bản note mục 1 "M5 bóng nến chồng lấp, không tạo FVG rõ → xuống M1 quan sát".
Consequence: nếu rule "M5 không FVG = no-trade" đúng, lệnh này lẽ ra không được vào — không phải vì entry M1 sai kỹ thuật, mà vì toàn bộ quyết định tụt khung là một free parameter chỉ được giữ lại khi nó dẫn tới kết quả tốt.
Your best answer: "M1 vẫn có MSS+FVG sạch nên đủ điều kiện." Không cứu được — nếu tiêu chuẩn của bạn là M5 phải sạch trước khi tụt khung, thì M1 sạch không thay thế được điều đó; nó chỉ chứng minh bạn CÓ THỂ luôn tìm ra trigger ở M1 nếu tìm đủ lâu (đúng như cảnh báo trong Lesson Learned của Loss 19/5: "M1 luôn luôn có sweep+MSS+FVG ở đâu đó").
Retracted by: một quy tắc rõ ràng, viết TRƯỚC khi biết outcome, định nghĩa khi nào tụt khung từ M5 sang M1 là hợp lệ (vd: M5 phải có ít nhất phản ứng giá dù không tạo FVG hình học) — nếu quy tắc đó tồn tại và lệnh này thỏa nó, objection rút.

**O2 · [DOCTRINE] · material · attacks C6**
Claim: "CE của H1 FVG có trùng OTE 62–79%? Yes (H1 FVG nằm giữa 50–0.618)".
Fails: mâu thuẫn nội tại — 50–0.618 nằm NGOÀI dải OTE chuẩn (0.618–0.786/CE~0.705, xem SKILL.md § OTE). Tự thân câu văn vừa nói "nằm giữa 50-0.618" vừa gọi đó là "OTE 62-79%".
Evidence: mục 2 note gốc, dòng "CE của FVG có trùng OTE 62–79%?: Yes (H1 FVG nằm giữa 50–0.618)".
Consequence: nếu H1 FVG thực tế nằm ở biên 0.5-0.618 (dưới OTE), thì claim "đúng sweet spot OTE" là overcall — entry có thể đã diễn ra ở mép ngoài discount hơn của Premium, không phải sweet spot.
Your best answer: "0.618 là biên OTE nên coi là trùng." Yếu — 0.618 là biên NGOÀI của OTE (0.618–0.786), "nằm giữa 50-0.618" nghĩa là phần lớn dải đó vẫn ở dưới 0.618, tức dưới OTE.
Retracted by: xác nhận lại trên chart H1 rằng phần lớn thân FVG nằm trong 0.618–0.786, không chỉ chạm biên.

**O3 · [HINDSIGHT/outcome-as-evidence] · material · attacks C6**
Claim (mục 6): "POI đã chọn có phải lựa chọn tốt nhất? ... lệnh thắng nhờ LTF confirm sớm hơn, nhưng nếu giá retrace sâu hơn về OB, SL 1304 đã bị quét trước khi tới đó."
Fails: đây là self-acknowledged near-miss nhưng KHÔNG được tính vào grade (vẫn A-) hay vào first_error_step (vẫn "none"). Trigger có nhận diện được TRƯỚC outcome không? — Có (bias/MSS/FVG đều xác lập trước khi biết kết quả), nhưng "OB chưa test = rủi ro SL nằm trên đường thanh khoản" cũng nhận diện ĐƯỢC trước outcome (đúng cấu trúc như Loss 19/5) — và không được set thành cảnh báo/no-trade trong quy trình gốc.
Evidence: chính mục 6 của note.
Consequence: grade A- không phản ánh đúng rủi ro cấu trúc đã tồn tại tại thời điểm entry; nếu lệnh này thua theo đúng cách Loss 19/5 đã thua, note có thể đã gắn cùng root cause "POI nông trong khi POI sâu chưa test".
Your best answer: "Nhưng lệnh này thắng, nên rủi ro đó không hiện thực hóa." Đúng về outcome nhưng đó chính là outcome bias — quy trình đánh giá quality phải độc lập với việc SL có bị chạm hay không (nguyên tắc mà note Loss 19/5 chính nó nêu: "loss đúng hướng vẫn là -1R thật"; đối xứng: win có rủi ro cấu trúc vẫn là win có process yếu hơn nhãn A- thể hiện).
Retracted by: nếu chart H1 cho thấy OB 0.786 đã từng bị test-và-reject TRƯỚC lệnh 12/5 (tức không còn là pool "chưa lấy"), objection rút.

**O4 · [UNSUPPORTED] · minor · attacks C1**
Claim: `confluence_score: 2` nhưng grade A-.
Retracted by: một note riêng giải thích rõ trọng số grade không dựa trên confluence_score — note đã có giải thích này ("grade tổng A- phản ánh chất lượng process + kết quả thực tế") nên objection gần như đã tự giải; giữ ở minor vì cách viết vẫn mở khả năng đọc nhầm "A- = process tốt" thay vì "A- = process tốt + outcome tốt trộn lẫn".

Drafted: 5 objections. Cut: 1 (một objection về `sweep_type: Internal` không đủ evidence để phân biệt internal/external — bị cắt vì rebuttal test: note đã tự flag "Cần xác minh: Quét CE liquidity void ≠ quét liquidity pool" ở mục 7.1, tức đã tự nhận, ship lại là thừa).

**4. Opposite case (cùng evidence)**: Đọc ngược — M5 "không FVG" không phải dấu hiệu yếu mà là **absorption tại vùng cao**: giá không cần tạo imbalance mới vì phần lớn thanh khoản buy-side ngắn hạn đã bị hấp thụ từ trước (bởi chính nhịp tăng H1 tới CE FVG). M1 MSS+FVG khi đó là xác nhận CHÍNH XÁC, không phải trigger "moi" ra. Load-bearing của case ngược: cùng C3 (M5 không FVG) nhưng đổi vai trò từ "cảnh báo" thành "context tốt". Tự phản biện case này: nó không giải thích được vì sao đúng rule "M5 không FVG = no trade" lại được note tác giả dùng để LOẠI 3 lệnh khác — nếu absorption là lý do hợp lệ ở đây, nó phải được kiểm ở 3 lệnh Loss kia trước khi loại, và không có ghi chú nào cho thấy điều đó đã được làm. **Strength: weaker but non-trivial** — case ngược sống được về lý thuyết nhưng bị chính tiền lệ áp dụng rule trong vault phản bác.
Distinguishing observable: liệu tại các đỉnh M5 "không FVG" của 3 lệnh Loss, có dấu hiệu absorption tương tự (nến đối nghịch mạnh ngay trước) hay không — nếu có và chúng vẫn thua, absorption không phải biến số quyết định; nếu không có, nó có thể là yếu tố phân biệt thật.

**5. Verdict: SURVIVES, WEAKENED.** Load-bearing claim (C6, entry hợp lệ theo chuỗi 7 bước) không bị BROKEN bởi bằng chứng có trong note, nhưng O1 (tụt khung không nhất quán rule) và O3 (rủi ro cấu trúc SL-trên-đường-tới-OB chưa hiện thực hóa) là material — chúng không đảo verdict thắng/thua nhưng đặt nghi vấn thật lên độ tin cậy của process, độc lập với outcome. **evidence_sufficiency=thin nghĩa là "SURVIVES" ở đây yếu hơn nhãn thường: không có chart gốc để kiểm tra độc lập lời tự thuật.** Điều DA này KHÔNG chứng minh: rằng nếu chạy lại 100 lần setup tương tự (M5 không FVG, tụt M1), tỷ lệ thắng sẽ ra sao.

**6. Falsification tests**:
1. Thu thập ≥15 lệnh trong vault có `step4_displacement_ok=No` ở M5 nhưng vẫn entry M1: nếu winrate của nhóm này khác biệt rõ so với nhóm M5 sạch, O1 có cơ sở thống kê; nếu không khác biệt, rule "M5 không FVG = no-trade" của chính vault là chưa được kiểm chứng và cần nới. Đóng O1.
2. Đối chiếu lại ảnh H1 gốc (`Pasted image 20260714063937.png`) để xác định OB 0.786 đã bị test trước 12/5 chưa. Đóng O3.
3. Đo lại tỷ lệ % thân FVG H1 nằm trong dải 0.618–0.786 thật (không chỉ biên). Đóng O2.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis**: Short XAUUSD 12/5/2014 theo chuỗi Sweep(H1 internal)→MSS+Displacement(M1)→FVG(M1 FVG2)→retrace CE→Entry, trong Premium/OTE của H1 Dealing Range, bias D1 Bearish 4-tầng.

**Cần sửa** (load-bearing trước):
- C3 "M5 không tạo FVG rõ nhưng vẫn tụt xuống M1 tìm trigger" — **AMBIGUOUS** (load-bearing) · doctrine không cấm tụt timeframe khi TF trung gian yếu, nhưng cũng không tự động cho phép — đây là doctrine gap thật (SKILL.md không định nghĩa ngưỡng khi nào "M5 yếu" đủ để bỏ qua và tìm M1) → fork: đọc theo chuẩn "M5 phải sạch" thì bước 4 FAIL; đọc theo chuẩn "chỉ cần TF entry (M1) sạch" thì PASS. → fix: vault cần một rule viết trước (pre-registered), không quyết định sau khi thấy M1 đẹp.
- C2 "CE của FVG có trùng OTE 62–79%? Yes (H1 FVG nằm giữa 50–0.618)" — **FAIL** · why: 50–0.618 là dải NGOÀI OTE theo định nghĩa canon (OTE = 0.618–0.786, SKILL.md § OTE), tự mâu thuẫn khi gọi đó là "OTE 62-79%" → fix: đổi mô tả thành "entry ở biên OTE / gần 0.618" hoặc xác nhận lại trên chart rằng FVG thực chồng lấn vào 0.618–0.786.
- C6 (entry hợp lệ) — kế thừa từ C3, không tính lỗi riêng.

**PASS**: C1 (bias D1 4 tầng, đủ căn cứ mô tả) · C4/C5 (MSS+FVG M1, hình thức đạt chuẩn CISD/displacement theo mô tả, tuy không kiểm được trên chart).

**Verdict**: **INSUFFICIENT EVIDENCE** — load-bearing claim (C3, tụt khung có hợp lệ hay không) rơi vào AMBIGUOUS do doctrine gap, không phải vì thiếu evidence từ phía note (note đã mô tả rõ), mà vì canon chưa fix ranh giới "khi nào M5 yếu vẫn được phép tụt khung". Các claim phụ PASS không đủ để nâng verdict lên ALIGNED khi load-bearing còn treo.

**Notes**: Doctrine gap phát hiện — SKILL.md § Displacement/FVG không có ngưỡng rõ cho quyết định "bỏ qua TF trung gian yếu, dùng TF thấp hơn làm trigger". Đề xuất bổ sung: một rule dạng "TF trung gian không tạo FVG → chỉ được entry ở TF thấp hơn nếu có ≥1 yếu tố xác nhận độc lập khác (SMT, CISD rõ, hoặc absorption pattern được định nghĩa cụ thể)", tránh để quyết định này chỉ được biện minh sau khi biết outcome.

---

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật

1. **Rule tụt khung phải được viết TRƯỚC, không phải sau khi thấy kết quả.** Ví dụ số thật: M5 12/5 "bóng nến chồng lấp, không tạo FVG" → tụt M1 → thắng R=2.9. Tổng quát hóa: bất cứ khi nào TF xác nhận (thường M5 trong model Standard) không đạt chuẩn displacement, quyết định tụt khung cần một tiêu chí độc lập với outcome (vd: đã có SMT hay CISD ở TF đó) — nếu không, cùng hành vi này ở Loss 14/5 sáng và Loss 19/5 lại được gọi là "tụt khung moi setup, pattern nguy hiểm".
2. **OTE là một vùng, không phải một điểm chạm biên.** Ví dụ số thật: mô tả "H1 FVG nằm giữa 50–0.618" bị gọi nhầm là "trùng OTE 62-79%" trong khi 0.618 chỉ là biên ngoài dải OTE 0.618-0.786. Tổng quát: luôn đo % thân PD array nằm trong dải OTE thật, không chỉ kiểm nó có chạm biên hay không.

### (b) Bài học quy trình/checklist

3. **Rủi ro cấu trúc "SL nằm trên đường tới POI sâu chưa test" cần được đánh cờ TẠI THỜI ĐIỂM ENTRY, không chỉ ghi nhận sau (mục 6 "nếu vào lại...").** Ví dụ số thật: SL 1304.113 nằm giữa entry 1301.562 và OB H1 0.786 (~1308-1310) chưa test — đúng cấu trúc rủi ro như Loss 19/5, nhưng ở đây chỉ được nhắc tới SAU KHI biết lệnh thắng, dưới dạng "may đấy". Rule đề xuất: checklist entry phải có câu hỏi "POI sâu hơn cùng phía chưa test nằm ở đâu so với SL?" trả lời TRƯỚC khi bấm lệnh.

### (c) Bài học tâm lý-hành vi

4. **Outcome bias hai chiều**: note đã đúng khi hạ grade các lệnh Loss vì lỗi cấu trúc dù đúng hướng (Loss 19/5); nhưng CHƯA đối xứng khi giữ A- cho lệnh Win có cùng loại rủi ro cấu trúc (SL trên đường tới OB chưa test) chỉ vì nó không bị hiện thực hóa. Halo effect của kết quả thắng đang che một lỗ hổng quy trình giống hệt lỗ hổng đã bị phạt ở nơi khác.

### (d) Rule đề xuất cho Playbook

- [ ] **R-BD-01**: Khi TF xác nhận trung gian (M5) không tạo displacement/FVG sạch, chỉ cho phép tụt TF thấp hơn nếu có ≥1 xác nhận độc lập (SMT/CISD) — ghi rõ xác nhận đó TRƯỚC khi vào lệnh.
- [ ] **R-BD-02**: Checklist entry bắt buộc câu hỏi "POI cùng phía sâu hơn, chưa test, nằm cách SL bao xa?" — nếu SL nằm trên đường đi tới POI đó, ghi nhận rủi ro dù lệnh có thắng hay thua.
- [ ] **R-BD-03**: Khi mô tả CE/FVG trùng OTE, ghi % thân nằm trong dải 0.618–0.786 thật, không chỉ "chạm biên = trùng".

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG dùng lệnh này làm minh chứng rằng "tụt khung khi M5 yếu luôn ổn" — outcome win ở đây không kiểm định được tỷ lệ thắng dài hạn của hành vi đó, và chính vault đã phạt hành vi giống hệt ở 2 lệnh Loss khác.
- KHÔNG dùng grade A- này làm chuẩn neo cho confluence_score=2 — note gốc đã tự nói rõ điều này ("theo thang quy đổi rơi vào C về mặt điểm số thuần").
- KHÔNG kết luận rằng "SL giữa entry và POI sâu chưa test" là an toàn chỉ vì ở đây nó không bị quét — mẫu quá nhỏ (n=1) để tổng quát hóa, và cấu trúc rủi ro giống Loss 19/5 hoàn toàn.


---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI: [[13-FVG-Fair-Value-Gap]]
- Bước: [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]
- Timing: [[18-Kill-Zones]]
- Dashboard: [[_Backtest Dashboard]]
