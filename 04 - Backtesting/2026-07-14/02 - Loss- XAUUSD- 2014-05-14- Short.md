---
type: backtest
backtest_date: 2026-07-14
trade_date: 2014-05-14
symbol: XAUUSD
position: Short
result: Loss
session: London
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct: Yes
poi_type: Rejection Block
poi_rank:
poi_timeframe: H1
poi_location: Premium
poi_in_ote: Yes
ce_ote_overlap: Yes
poi_stack: H1 Rejection Block (context POI) + M1 FVG (entry trigger, post-MSS)
fvg_high: 1301.676
fvg_low: 1301.225
ce_price: 1301.4505
entry_type: CE
entry_precision: CE
limit_filled: Yes
fill_depth_pct:
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: Yes
step5_poi_ok: No
step6_entry_ok: Yes
step7_target_ok: NA
first_error_step: poi
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
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: Yes
correlated_asset: none
entry_price: 1301.482
stop_loss: 1302.715
take_profit: 1297.51
r_planned: 3.22
rr_if_ce:
rr_if_ote:
r_multiple: -1
risk_percent:
spread_cost:
r_net:
grade: B-
followed_plan: Yes
confidence:
tags:
  - backtest
  - ICT2022
  - POI
  - Rejection Block
---

# Backtest 2014-05-14 — XAUUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi (2026-07-17)
> Chuyển từ template cũ sang **Backtest template - POI & Step Decision**. Toàn bộ phân tích gốc giữ nguyên. `first_error_step: poi` được chọn vì root cause thật sự (theo phân tích gốc) là **không xác định đúng invalidation thật của Rejection Block** khi đặt SL — bản chất là lỗi trong cách "dùng" POI, không phải lỗi chọn sai loại POI hay lỗi chase giá. ⚠️ Template 7-bước hiện KHÔNG có bước riêng cho "Stop Loss placement" (khác với checklist 7-bước bản cũ, vốn có mục SL riêng) — đây là khoảng trống đáng cân nhắc bổ sung vào template nếu bạn muốn tách bạch lỗi POI-selection khỏi lỗi SL-anchoring trong tương lai.
> ⚠️ `poi_rank` để trống vì Rejection Block không nằm trên thang 8.1 (chỉ có FVG/FVG+OB/Breaker/iFVG/Unicorn).
> ⚠️ `displacement_score`, `confidence`, `risk_percent`, `spread_cost`, `r_net`, `fill_depth_pct` không có căn cứ số trong bản gốc → để trống.
> `step7_target_ok: NA` vì lệnh dính SL trước khi tới target — target selection logic không được kiểm chứng bởi outcome này (TP 1297.51 chỉ được xác nhận đúng hướng ở mục 6, không phải bị "hit").

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | XAUUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5→M1)                                    |
| Trade Date (dữ liệu)      | 2014-05-14 16:17                                             |
| Position                  | Short                                                        |
| Result                    | Loss                                                         |
| Session                   | London                                                       |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | Rejection Block                                              |
| POI Rank (8.1)            | — (ngoài thang 8.1)                                          |
| POI Timeframe             | H1 (entry refine M1)                                         |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | poi (SL không neo đúng invalidation thật của POI)            |
| R Planned (gross)         | 3.22                                                         |
| R Net (sau spread)        | (chưa có dữ liệu)                                            |
| R Multiple (kết quả)      | -1                                                            |
| Confluence Score (0–8)    | 2                                                             |
| Grade                     | B-                                                            |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish · **Market Condition**: Trending
- **Lý do xác định bias**: (giống bối cảnh chung của cụm backtest XAUUSD tháng 5/2014) Phía trái đã quét hết lower high, tạo Long Term High; trước đó có sweep đáy + đóng lại trong range rồi tăng; nhịp tăng tạo Displacement + Order Block; sau đó HH/HL tích tụ thanh khoản ở đáy; hình thành Bearish MSS + Displacement + FVG tại đỉnh; giá đang trong Premium của Dealing Range lớn → Bias Bearish, target Sell Side Liquidity + Order Block.
- **Draw on Liquidity**: BSL — D1 Dealing Range High 1392.098, Bearish OB 1387.437. SSL — Dealing Range Low 1182.661, old lows, Order Block, H1 Dealing Range Low.

![[Pasted image 20260714063937.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Sau Long Term High, Bearish MSS + Displacement; LH/LL, order flow giảm.
- **Dealing Range**: High 1315.691 (fib 1.0) / Low 1277.416 (fib 0.0) → retrace lên Premium/OTE cho Short.
- **POI chính**: **Bearish Rejection Block 1304.109 – 1302.715**; Order Block 1308.146 – 1304.82 (nằm cao hơn, chưa dùng).
- **Liquidity cần chờ sweep**: internal high consolidation + cạnh trên H1 FVG.

### Phân tích

- **Context**: chuỗi sự kiện 2/5–12/5/2014 giống các backtest khác trong cụm (sweep SSL → tăng HH/HL → đỉnh → Bearish Displacement 7/5 → consolidation 8/5 → sweep đáy cũ 12/5 lúc 17:00, tạo H1 Dealing Range Low → chờ retrace Premium).
- **Lệnh**: 12/5/2014 19:00 displacement phá 50% Dealing Range vào Premium, tạo đỉnh với râu nến dài — vừa học Rejection Block nên đánh dấu râu nến này làm RB, chờ retrace. 14/5/2014 15:00 giá retrace về cạnh dưới RB với 2 nến Bullish Displacement mạnh; râu nến sau chạm đúng CE của RB rồi bật ra bằng 1 nến Bearish → xuống M5/M1 quan sát.

![[Pasted image 20260714111634.png]]

### M5/M1 — Xác nhận và điểm vào lệnh

- M5: sau khi chạm CE RB, nến Bearish H1 xuất hiện; M5 tạo nến Bearish liên tiếp có thân lớn, nhưng bóng nến overlap, không tạo FVG rõ → xuống M1.
- M1: MSS phá swing low (swing tạo đỉnh quét CE RB); displacement tạo FVG **1301.676 – 1301.225**. Entry khi giá retrace về CE FVG (≈1301.4505, thực khớp 1301.482). SL trên swing high (nến quét chạm CE RB) = 1302.715. TP dưới swing low gần nhất M5 (internal) = 1297.51, RR 1:3.22.
- **Entry trigger**: quét CE RB → giá phá swing low → tạo FVG từ nhịp MSS → retrace về CE FVG. MSS bằng nến Bearish displacement lúc 16:03; displacement lúc 16:03 tạo FVG.
- **Entry reason**: chuỗi Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là Rejection Block H1); RB nằm trong OTE 0.618–0.705 (sweet spot).
- **Invalidation (kế hoạch)**: giá đóng qua Rejection Block H1.
- **Chờ đủ điều kiện?** Có.

**M5:** ![[Pasted image 20260714121553.png]]
**M1:** ![[Pasted image 20260714121625.png]]

---

## 2. POI Profile

- **POI Type đã dùng**: Rejection Block (H1) — thử nghiệm thay cho OB/FVG quen dùng.
- **POI Rank (8.1)**: ngoài thang, không có rank số.
- **POI hình thành trên khung**: H1 (entry refine trên M1 FVG).
- **POI nằm ở**: Premium ✓ đúng phía cho Short.
- **POI stack**: H1 Rejection Block (context) + M1 FVG (entry trigger).
- **CE của FVG trùng OTE 62–79%?**: Yes — RB nằm trong 0.618–0.705.
- **Bounds & CE**: RB High 1304.109 / RB Low 1302.715; M1 FVG High 1301.676 / Low 1301.225, CE ≈1301.4505.

![[Pasted image 20260714121553.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE
- **Entry Precision**: CE (M1 FVG)
- **Limit có khớp?**: Yes
- **Giá đi sâu bao nhiêu vào FVG?**: không có số đo cụ thể trong bản gốc
- **RR ghi lại**: r_planned 3.22 (Risk 1.230 / Reward 3.975 theo phân tích lại ở mục 6)

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes | `step3_sweep_ok` |
| 4 | Displacement + MSS | Yes | `step4_displacement_ok` |
| 5 | POI (Rejection Block — invalidation) | **No** | `step5_poi_ok` |
| 6 | Entry (retrace, không chase) | Yes | `step6_entry_ok` |
| 7 | Target | NA (dính SL trước khi test) | `step7_target_ok` |

- **First Error Step**: **poi** — không neo SL theo invalidation thật của RB (đóng nến trên 1304.109), mà neo theo swing nhỏ M1 (1302.715 = RB low).
- **Missing Step**: none
- **Đủ chuỗi 7 bước?**: Yes (chuỗi đủ, nhưng bước POI bị dùng sai)

> [!warning] Chống hindsight bias
> Chỉ tick Yes nếu trigger nhận diện được TRƯỚC outcome. Ở đây bias/sweep/displacement/MSS/entry đều được xác lập trước khi biết kết quả; riêng việc SL nằm sai vị trí là một lỗi **quy trình xác định invalidation**, không phải hindsight.

---

## 5. Setup Quality & Confluence

**GATE**: Bias rõ · Sweep trước displacement · Displacement hợp lệ · MSS hợp lệ · FVG sạch + entry retrace · Đúng Premium · **SL không đặt trên invalidation thật → GATE này KHÔNG đạt** → theo đúng tinh thần GATE-trước-SCORE, đây lẽ ra đã là **No Trade** hoặc chí ít bị chặn trần grade.

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không áp dụng (ngoài thang) | *(suy từ poi_rank)* |
| 2 | CE FVG trùng OTE 62–79% | Có | `ce_ote_overlap` |
| 3 | SMT divergence | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | Không có ghi chú | `cisd_confirm` |
| 5 | Macro time | Chưa đánh giá | `in_macro_time` |
| 6 | NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | SD target align | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Có | `idm_swept` |

- **Score**: 2/8. **Grade B-** phản ánh đúng tinh thần Rule grading gốc: "Bất kỳ lệnh nào có SL nằm trong POI đều bị chặn trần grade ở mức B, bất kể R:R."

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit Stop Loss (-1R)

**Root cause đơn nhất**: SL đặt SAI vị trí — nằm ngay cạnh gần (proximal edge) của POI, tức bên trong vùng phản ứng còn hợp lệ của Rejection Block, chứ không phải trên điểm invalidation thật.

**Kiểm chứng bằng số học**:
- RB H1: 1302.715 (low) → 1304.109 (high), CE = 1303.412
- Invalidation thật (theo chính ghi chú Entry): "Giá đóng qua Rejection Block H1" → đóng nến trên 1304.109
- Entry (CE M1 FVG): 1301.485 — nằm dưới RB low, quanh fib 0.618 (1301.070)
- SL: 1302.715 = đúng RB low = mép dưới POI ≈ fib 0.618–0.705
- TP: 1297.51 → Risk 1.230 / Reward 3.975 = R 3.23
- Vấn đề: giá chỉ cần retrace từ 0.618 ngược lên chạm lại đáy RB (0.705) là quét SL — hành vi hoàn toàn bình thường bên trong OTE/POI, KHÔNG phá invalidation thật.
- Mâu thuẫn logic: định nghĩa invalidation theo H1 (đóng trên RB) nhưng đặt SL theo swing high nhỏ khung M1 — hai logic khác cấp độ bị trộn vào nhau.

**Cảnh báo trước có không?** Có, ít nhất 2:
1. M5 không tạo được FVG — "các bóng nến khung M5 overlap với nhau, không tạo FVG" — dấu hiệu phản ứng bán không sạch → đáng lẽ là tín hiệu đứng ngoài chờ.
2. 2 nến Bullish Displacement mạnh đẩy giá vào POI (14/5 lúc 15:00) — order flow ngắn hạn phía mua rất mạnh khi chạm vùng short.

**Setup khớp bao nhiêu % với mô hình chuẩn?** ~75–80%. Khớp tốt: HTF bias đúng, sweep SSL đã có, retrace Premium/OTE, chuỗi Sweep→MSS+Displacement+FVG→retrace tồn tại, TP đúng draw on liquidity. Lệch chuẩn: SL không đặt trên invalidation thật (nặng nhất); entry rơi xuống M1 sau khi M5 báo phản ứng yếu; vào lệnh khi displacement tăng đối nghịch chưa bị hấp thụ.

**Nếu vào lại, làm gì khác?**
1. Neo SL vào invalidation của POI (RB H1) trên 1304.109 + buffer (~1304.4). Reward 3.975/risk ~2.9 = ~1.35R — nếu không đủ hấp dẫn thì đó là tín hiệu vùng entry chưa tối ưu, nên bỏ lệnh, không phải lý do siết SL cho đẹp R:R.
2. Nếu giữ SL chật kiểu M1, phải chờ M1 MSS hình thành SAU khi giá thực sự rời khỏi POI, không phải trong lúc bulls vẫn đẩy vào vùng.
3. Coi "M5 không có FVG" là điều kiện loại (no-trade).
4. Xác minh trong Replay: sau khi quét SL, giá có xuống chạm TP 1297.51 không? Nếu có → xác nhận lỗi SL quá chật, sửa được. Nếu giá tiếp tục phá RB → luận điểm short vào quá sớm, cần xét lại cả timing.

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Bias đúng, phân tích top-down tốt — nhưng thua vì SL đặt ngay mép dưới POI (RB low) thay vì trên invalidation thật, nên một cú retrace bình thường trong OTE đã quét stop trước khi luận điểm short kịp chạy.

> [!warning] Ghi chú của mentor
> Đừng để R:R đẹp (3.22) đánh lừa: con số đó là sản phẩm phụ của một SL quá chật đặt sai chỗ, không phải bằng chứng setup chất lượng A. Một lệnh "R:R thấp nhưng SL đúng invalidation" tốt hơn nhiều một lệnh "R:R cao nhưng SL trong POI".

### 7.1. Bài học kỹ thuật

**Root cause (duy nhất)**: SL neo vào swing high nhỏ khung M1 (1302.715 = RB low) — mép gần của POI — thay vì trên invalidation thật của RB H1 (đóng trên 1304.109).

**Triệu chứng dễ nhầm là đúng**: R:R 3.22 hấp dẫn nhưng chính SL chật tạo ra nó và cũng giết lệnh; entry rất đẹp ở 0.618 nhưng cộng với SL ở mép POI = stop rơi vào no-man's-land; M1 MSS + FVG trông như trigger chuẩn nhưng chỉ là nhịp pullback nhiễu giữa lúc bulls đang displacement mạnh vào vùng.

**Cơ chế thị trường**: giá wick lên CE RB (~1303.4), phản ứng giảm nhẹ tạo M1 FVG quanh 0.618; RB chưa hoàn tất nhiệm vụ — đáy RB (0.705) vẫn là vùng dễ bị test lại; giá retrace ngược lên chạm mép dưới RB, quét SL, rồi (cần xác minh) mới đi theo hướng bias — kịch bản "stopped out on noise inside the POI".

**Cần xác minh thêm**: sau khi quét SL, giá có xuống TP 1297.51 không (quyết định lỗi SL hay lỗi timing); định nghĩa RB đã chuẩn chưa (thân nến bóng dài đúng nghĩa?); Kill Zone entry ~16:03 UTC+7 có còn trong London KZ không.

### 7.2. Pattern lặp lại

- Siết SL để làm đẹp R:R — ép SL vào mép POI thay vì trên invalidation thật. Pattern nguy hiểm nhất; liên kết [[Mistake - Stop loss đặt sai vị trí]] (tạo note nếu chưa có).
- Tụt khung để "moi" setup khi khung xác nhận (M5) đã báo phản ứng yếu/không FVG.
- Vào lệnh ngược displacement đối nghịch còn mạnh.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **Rule SL theo POI**: SL luôn neo trên invalidation của POI đang giao dịch + buffer, KHÔNG neo vào swing nhỏ khung entry. R do SL đúng quyết định có vào hay không, không phải ngược lại.
- [ ] **Rule confirmation**: khung trung gian (M5) không tạo displacement/FVG sạch → no-trade.
- [ ] **Rule momentum đối nghịch**: không short khi displacement tăng vào POI còn chưa bị hấp thụ.
- [ ] **Rule grading**: SL nằm trong POI → chặn trần grade ở mức B, bất kể R:R.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | (không có điểm chi tiết trong bản gốc) |
| POI Selection (invalidation) | thấp — root cause chính |
| Liquidity Sweep | — |
| Displacement/MSS quality | — |
| Entry Precision & Fill | — |
| Risk Management (SL placement) | thấp — root cause chính |

**Overall Grade**: **B-** (chặn trần vì SL nằm trong vùng phản ứng hợp lệ của POI).

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI: [[28 - Rejection Block]] · [[13 - FVG  - Fair Value Gap]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_Backtest Dashboard]]
