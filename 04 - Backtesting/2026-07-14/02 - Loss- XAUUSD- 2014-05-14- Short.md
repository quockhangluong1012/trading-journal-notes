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

- Siết SL để làm đẹp R:R — ép SL vào mép POI thay vì trên invalidation thật. Pattern nguy hiểm nhất; liên kết [[13 - Mistake - Trading Into Unswept Liquidity]] (note tổng hợp đã tạo 2026-07-18, bao trùm cả biến thể "SL trong POI" này).
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

## 9. Phân tích bổ sung chuyên sâu (2026-07-18)

### 9.1. Các khái niệm ICT bị áp dụng SAI

| Khái niệm | Tôi đã dùng như thế nào (SAI) | Cách dùng ĐÚNG | Ảnh hưởng |
|---|---|---|---|
| [[28 - Rejection Block]] | Vừa học xong đã dùng ngay làm **POI chính**, và neo SL ở RB low (1302.715) — tức mép GẦN của vùng | Invalidation của RB = **đóng nến qua cực trị của râu** (RB high 1304.109), vì toàn bộ chiều dài râu là vùng lệnh tổ chức đã bán. SL phải nằm trên RB high + buffer. Ngoài ra RB vốn là POI **phụ trợ** — dùng kèm OB/FVG để tinh chỉnh, hiếm khi standalone | Chí mạng — first_error |
| [[10 - Consequent Encroachment (Mean Threshold)]] | Hiểu "giá chạm CE RB rồi bật ra" = RB đã hoàn thành nhiệm vụ, có thể entry với SL chặt | CE bị chạm chỉ nghĩa là **một nửa vùng** đã được lấp. Nửa còn lại (CE → RB high, và cả vùng đáy RB 0.705) vẫn là nơi lệnh tổ chức có thể tiếp tục fill — tức vùng test lại HỢP LỆ, không phải vùng cấm | Nặng |
| [[26 - OTE - Optimal Trade Entry]] | Đặt SL (1302.715) ngay tại ~0.705 → biến rotation bình thường BÊN TRONG OTE thành "invalidation" | OTE 0.618–0.786 là **một vùng nạp lệnh**, không phải một mức. Giá xoay 0.618↔0.705↔0.786 trong vùng là hành vi mặc định. SL đặt trong lòng OTE = tự nguyện bị quét bởi nhiễu | Chí mạng |
| [[32 - Top-down Analysis (Multiple Timeframes)]] + [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]] | **Trộn cấp độ**: invalidation định nghĩa trên H1 ("đóng qua RB H1") nhưng SL đặt theo swing high M1 | Mỗi lớp phải nhất quán: POI H1 → invalidation H1 → SL neo theo H1 (+buffer). M1 chỉ được quyết định *entry timing*, không được quyết định *nơi luận điểm chết* | Chí mạng |
| [[21 - Market Structure Shift]] | Tin MSS M1 hình thành ngay khi 2 nến Bullish Displacement H1 còn đang đẩy mạnh vào vùng | MSS cấp M1 ngược một displacement cấp H1 chưa bị hấp thụ = tín hiệu cấp thấp cãi lại order flow cấp cao — trọng số gần bằng 0. Chờ dấu hiệu hấp thụ (nến H1 đóng ngược) rồi mới đếm MSS LTF | Nặng |
| [[13 - FVG  - Fair Value Gap]] | M5 không in được FVG (wick overlap) nhưng vẫn tụt xuống M1 để "moi" trigger | Không có FVG ở khung xác nhận = displacement chưa đủ mạnh = no-trade ([[08 - Mistake - Weak Displacement]] · [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]]) | Nặng |

### 9.2. Những điều tôi NGHĨ là đúng nhưng thật ra SAI

1. **"SL trên swing high M1 là chặt chẽ, khoa học."** SAI: swing M1 đó nằm **bên trong POI H1**. "Chặt" không đồng nghĩa "đúng" — SL phải đặt tại nơi **luận điểm chết** (đóng trên RB high), không phải tại cấu trúc nhỏ gần nhất tiện cho R:R. Một SL chặt đặt trong vùng phản ứng hợp lệ của POI là một SL được thiết kế để bị quét.
2. **"R:R 3.22 chứng tỏ setup chất lượng."** SAI: R:R này là **sản phẩm phụ của chính cái SL sai** — SL càng chật sai chỗ, R:R trên giấy càng đẹp. Phép thử đúng: đặt SL tại invalidation thật (trên 1304.109) rồi tính lại R:R (~1.35) — nếu con số thật không đủ hấp dẫn thì vùng entry chưa tối ưu, đáp án là BỎ LỆNH chứ không phải siết SL.
3. **"Giá bật ra từ CE RB bằng 1 nến bearish = RB đang hoạt động, entry được ngay."** SAI: phản ứng đầu tiên tại một vùng thường chỉ là phản xạ (các limit order đầu tiên khớp). RB "hoạt động thật" = giữ được giá SAU khi vùng được test đủ sâu và có displacement rời vùng. Một nến bearish đơn lẻ giữa lúc bulls còn displacement mạnh chưa chứng minh điều gì.
4. **"M5 yếu thì xuống M1 sẽ thấy rõ hơn."** SAI về hướng: tụt khung khi khung xác nhận báo yếu là **tăng nhiễu chứ không tăng thông tin**. M1 luôn luôn có "sweep + MSS + FVG" ở đâu đó nếu tìm đủ lâu — đó là lý do nó không được phép thay thế xác nhận M5.
5. **"Concept mới học, thấy khớp chart là áp dụng được ngay."** SAI ở tầng meta: một khái niệm mới (RB) cần được backtest RIÊNG (nhận diện, invalidation, cách đặt SL) trước khi cho vào quyết định có rủi ro. Lệnh này về bản chất là một "thí nghiệm concept" nhưng được thực hiện với kỳ vọng và cách chấm của một setup đã validate.

### 9.3. Đào sâu: vì sao đây là biến thể "nội bộ" của họ lỗi Unswept Liquidity

Ba lệnh thua kia bị quét bởi pool nằm **ngoài** entry (ERL của GBPUSD 17/7, OB sâu của XAU 19/5, BSL external của EURUSD 7/5). Lệnh này tinh vi hơn: pool chưa-bị-lấy chính là **phần thân còn lại của chính POI bạn đang giao dịch** — đoạn từ đáy RB (0.705) lên CE và RB high. Cụm buy-stop của những người short sớm (trong đó có SL của bạn tại đúng đáy RB) là thanh khoản nằm NGAY trên đường giá cần đi để hoàn tất việc test vùng. Câu hỏi gate vẫn y hệt: *"pool chưa-bị-lấy gần nhất nằm phía nào so với SL?"* — ở đây câu trả lời là "ngay trên SL, cách 0 pip" — và đáng lẽ nó chặn lệnh này từ trước khi bấm. Phân tích tổng hợp cả 4 lệnh + checklist gate: [[13 - Mistake - Trading Into Unswept Liquidity]].

Một hệ quả thực nghiệm cần làm (đã ghi ở 6. mục 4 nhưng nhấn lại vì quyết định bản chất lỗi): **kéo replay sau thời điểm SL** — nếu giá lên test RB high/OB rồi giảm về 1297.51 → xác nhận thuần lỗi SL placement (như XAU 19/5); nếu giá đóng nến trên RB high → lỗi kép (cả timing lẫn SL). Kết quả này quyết định lệnh được đếm vào nhóm lỗi nào trong thống kê.

---

**Bản đồ liquidity IRL↔ERL.** Draw on liquidity D1 nêu rõ: Buy-side = PDH 1.30009, Sell-side = PDL 1.29090. Entry Short 1.29729 nằm giữa hai mốc này. TP 1.28811 nằm dưới PDL (1.29090) khoảng 27.9 pip — nghĩa là TP đi *xuyên qua* PDL, một external liquidity pool, trước khi tới đích — về doctrine, PDL vốn là draw on liquidity của chính setup này (SSL), nên TP hợp lý về hướng nhưng đi ngang qua chính target đã định nghĩa ban đầu (PDL) rồi mới dừng — đáng nêu vì có thể TP thực tế lấy risk cao hơn cần thiết nếu PDL đã đủ là draw. SL 1.30164 nằm trên EQH khung H1 (1.30033) khoảng 13.1 pip và trên cạnh trên OB (1.30110) khoảng 5.4 pip — buffer khá mỏng so với biên độ trung bình di chuyển của cặp tiền, nhưng đủ để tránh bị quét bởi chính điểm sweep vừa xảy ra.

**Chất lượng displacement/MSS.** Note mô tả trình tự chuẩn: quét EQH H1 + cạnh trên OB → displacement M5 tạo FVG → MSS. Điểm mạnh: sweep target có TÊN cụ thể (EQH H1 tại 1.30033), không phải sweep mơ hồ — đây là điểm khác biệt tích cực so với note 1 (2010-10-19).

**Yếu tố thời gian.** Session New York, không có giờ cụ thể trong note gốc (không có mốc HH:MM). Killzone claim vẫn ở mức tick checklist, không dẫn chứng giờ.

**Vị trí entry trong dealing range H1.** High 1.30585 / Low 1.28001, mid = 1.29293. Entry 1.29729 nằm ở phía Premium (retracement từ high ≈ 0.331 tính từ đỉnh) — khớp với bias Bearish (short từ premium). Entry nằm trong OB (1.29573–1.30110) — đúng vị trí POI đã định nghĩa.

**So sánh với lệnh cùng mẫu.** So với [[2026-07-06/02 - Win - EURUSD - 2005-04-13 - Short]] (ngày kế tiếp, cùng session/bias) — note 13/04 có phân tích lớp thanh khoản sâu hơn nhiều (CE FVG → EQH tại CE → inducement, quét 2 lần trước khi entry thật), trong khi note 12/04 chỉ có 1 lớp sweep (EQH + cạnh OB) rồi entry ngay. Đây có thể là bias người viết: ngày sau (13/04) rút được lesson "chờ inducement" — báo hiệu note 12/04 có khả năng vào sớm hơn tiêu chuẩn mà note sau mới áp dụng.

![[EURUSD-20050412-sweep-sequence.svg|760]]

## 10. Phản biện chuyên sâu (Devil's Advocate)

**Mode: REVIEW.** Evidence base: text note + 3 screenshot không đọc được (ảnh PNG). **evidence_sufficiency: thin** — không xem được ảnh M5/H1 gốc để verify MSS/displacement độc lập.

**Claim graph:**
- C1: D1 bias Bearish do MSS + displacement lớn phá swing low, tạo Liquidity Void.
- C2: H1 dealing range 1.30585–1.28001, giá ở Premium.
- C3: POI = OB H1 1.30110–1.29573, chứa EQH 1.30033 bên trong.
- C4: Giá quét EQH + cạnh trên OB, đóng nến vào trong OB → "respect OB".
- C5 (**load-bearing**): M5 hình thành displacement + FVG + MSS sau sweep, overlap OB H1 → entry hợp lệ tại 1.29729.
- C6 (từ C5): Setup ICT 2022 Model chuẩn 90%, Grade A.

**Load-bearing: C5** — nếu MSS/displacement M5 không đạt chuẩn (chỉ retrace bình thường), phần còn lại chỉ là short tại vùng cung ngẫu nhiên trùng hướng bias.

**Những gì còn đứng:** C1–C4 nhất quán nội bộ và có số liệu cụ thể (EQH 1.30033, OB range rõ) — mạnh hơn hẳn note 1 về độ cụ thể. Arithmetic RR khớp gần đúng (tính lại 2.11 vs note ghi 2.1, do rounding).

**O1 · [HINDSIGHT] · material · attacks C6**
Claim: "Setup này khớp 90% với mô hình chuẩn", Grade A — chấm trong phần replay sau khi biết Hit TP.
Fails: không có ghi chép nào tại/trước điểm entry về mức độ tin tưởng hay điều kiện invalidation cụ thể ngoài "giá đóng qua đỉnh swing high đã quét" — điều kiện này là invalidation chuẩn, không phải bằng chứng process được đánh giá độc lập với outcome.
Evidence: mục 4 viết "Lệnh thắng vì chờ đầy đủ điều kiện" — câu này chỉ có thể viết sau khi biết kết quả Hit TP.
Consequence: 90%-match và Grade A có thể phản ánh outcome (Hit TP → cảm thấy quy trình tốt) hơn là một đánh giá process độc lập.
Your best answer: "Checklist mục 2/3 tick đủ 9/9, đây là process-based, không phải outcome-based." Không đủ: checklist được tick khi viết note đầy đủ (backtest replay), sau khi đã biết outcome — thứ tự ghi chép không được ghi rõ.
Retracted by: bằng chứng cho thấy checklist được điền trước khi xem tiếp phần giá đi sau entry (ví dụ timestamp ghi chú, hoặc note dạng LIVE).

**O2 · [UNSUPPORTED] · material · attacks C5**
Claim: "Giá tạo MSS" trên M5 (không nêu swing point cụ thể bị phá hay giá đóng nến).
Fails: doctrine MSS đòi hỏi phá swing point ngược hướng sweep bằng body close (SKILL.md § MSS) — note không cho số liệu để verify điều này, chỉ nói "giá hình thành MSS".
Evidence: mục M5 "Phân tích" chỉ liệt kê hiện tượng theo tên, không có giá cụ thể của swing bị phá hoặc giá đóng nến breaking candle.
Consequence: Không thể xác nhận độc lập rằng cú phá cấu trúc M5 là MSS thật (structurally significant) hay chỉ là một internal swing nhỏ bị phá do noise.
Your best answer: "Checklist mục 2 tick MSS = có." Không đủ: tick checklist là tự khai báo, không phải evidence quan sát được (giá, nến).
Retracted by: ảnh M5 gốc hoặc mô tả bằng số của swing point bị phá + giá đóng nến breaking candle.

**O3 · [METHOD] · minor** — Setup Quality Checklist 9/9 mục tick "có" đồng loạt cho mọi tiêu chí kể cả RR ≥1:2 (đúng, RR=2.1) — không có tiêu chí nào KHÔNG đạt, khác thường cho một checklist thật (checklist luôn pass hoàn hảo có thể là dấu hiệu điền theo outcome). Retracted by: một note Win khác trong vault có ít nhất 1 mục checklist không tick — nếu tồn tại, giảm nghi ngờ pattern điền checklist theo outcome.

**Filter:** 4 objection nháp, cắt 1 (nghi ngờ về EQH 1.30033 nằm "bên trong" OB — không rõ ràng gây thay đổi kết luận, và note có nêu rõ số liệu nên rebuttal test dễ vượt qua → xóa). Còn 3: 1 material hindsight, 1 material unsupported, 1 minor method.

**Opposite case.** Từ cùng evidence: cú quét EQH + cạnh trên OB có thể chỉ là một liquidity grab tạm thời trong continuation tăng (giá vẫn có thể tiếp tục lên sau khi lấy EQH, vì EQH đơn lẻ không đảm bảo đảo chiều) — và "MSS" trên M5 chỉ là một pullback nhỏ bị hiểu nhầm thành structural shift. Tự phản biện inverse: nếu chỉ là liquidity grab tạm thời, giá thường tiếp tục breakout mới sau khi lấy EQH thay vì tạo cả displacement + FVG + retrace đúng chuẩn — chuỗi hiện tượng đầy đủ này khó giải thích bằng inverse thuần túy. Nhãn: **weaker but non-trivial** — inverse chỉ sống được nếu MSS M5 không có body close thật.

Distinguishing observable: giá đóng nến của candle phá swing high M5 — nếu đóng rõ dưới swing (không phải wick), MSS hợp lệ và inverse yếu hẳn.

**Verdict: UNPROVEN.** Evidence sufficiency thin. Load-bearing C5 không FAIL nhưng cũng UNSUPPORTED độc lập với outcome bias — dừng ở UNPROVEN.

**Điều tôi không phá được:** cấu trúc HTF (D1 bias, H1 OB + EQH cụ thể) tự nhất quán, có số liệu rõ, mạnh hơn note 1.

**Điều critique này không xác lập:** không xác lập MSS M5 có đúng canon hay không (thiếu ảnh); không xác lập Grade A có bị outcome bias hay không một cách dứt điểm.

**Falsification tests:**
1. Kiểm ảnh M5 gốc: swing point bị phá bởi MSS có giá cụ thể + đóng nến rõ dưới swing không? → đóng O2 nếu xác nhận.
2. Rà toàn vault: đếm % note Win có Setup Quality Checklist tick 9/9 hoàn hảo so với note Loss — nếu tỷ lệ 9/9 áp đảo ở Win, O3 được nâng severity.
3. Tìm bằng chứng thời điểm ghi chú (timestamp) để xác định checklist được điền trước hay sau khi biết outcome, đóng O1 nếu có bằng chứng LIVE.

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Short EURUSD 12/04/2005 — sweep EQH H1 + cạnh trên OB → MSS + displacement + FVG M5 → entry tại retrace, Grade A.

**Cần sửa** (load-bearing trước):
- C5 (MSS M5, load-bearing) — **UNSUPPORTED** · không có giá swing point bị phá hoặc giá đóng nến breaking candle (SKILL.md § MSS: cần body close phá swing ngược hướng sweep) → bổ sung số liệu từ ảnh M5 gốc.
- C4 (OB "respect", đóng nến vào trong OB) — **UNSUPPORTED** · không có giá đóng nến cụ thể của candle phản ứng → ghi rõ giá đóng để verify đóng nến nằm trong OB range (1.29573–1.30110).

**PASS:** C1 (D1 bias Bearish, có mô tả MSS + displacement + Liquidity Void — đủ mô tả định tính để PASS ở mức bias, dù thiếu giá cụ thể); C2 (dealing range H1 arithmetic hợp lệ: High 1.30585 > Low 1.28001, mid 1.29293, entry 1.29729 ở Premium — khớp tính toán); C3 (EQH nằm trong OB, cấu trúc POI hợp lý theo doctrine OB — nến gốc tạo imbalance).

**Verdict: INSUFFICIENT EVIDENCE** — load-bearing C5 (MSS M5) ở UNSUPPORTED; các claim phụ PASS không đủ nâng verdict lên PARTIALLY ALIGNED.

**Notes:** Không có doctrine drift so với note 1 — cùng một khoảng trống UNSUPPORTED cho MSS M5 (thiếu evidence giá cụ thể), là pattern lặp lại của cả batch note sớm, không riêng lệ.

## 12. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật**
- Ví dụ số thật: EQH H1 tại 1.30033 nằm trong OB 1.29573–1.30110 — một target sweep có TÊN và giá cụ thể, khác note 1 (2010-10-19) chỉ nói "old lows" mơ hồ. Tổng quát hóa: mọi sweep claim nên gắn với một mốc giá cụ thể (EQH/EQL/PDH/PDL), không mô tả chung.
- Ví dụ số thật: SL 1.30164 chỉ cách cạnh trên OB (1.30110) 5.4 pip — buffer mỏng. Tổng quát hóa: buffer SL trên điểm sweep nên tính theo ATR hoặc pip trung bình của khung thời gian, không phải khoảng cách cố định tùy cảm giác.

**(b) Bài học quy trình/checklist**
- Setup Quality Checklist 9/9 tick hoàn hảo, không một mục nào chưa đạt — cần cẩn trọng vì một checklist luôn hoàn hảo cho Win có thể phản ánh thiên kiến điền lại sau khi biết outcome hơn là đánh giá khách quan tại thời điểm quyết định.
- Lesson Learned tự nhận "RR > 2R nên lập kế hoạch partial TP trước" — đây là insight tốt nhưng chỉ xuất hiện *sau* lệnh, cần biến thành rule được kiểm tra TRƯỚC lệnh kế tiếp (không chỉ ghi nhận).

**(c) Bài học tâm lý-hành vi**
- Việc chấm Grade A và 90% match trong khi chưa xác nhận độc lập MSS M5 (chỉ mô tả bằng lời) cho thấy khả năng grade bị neo vào outcome (Hit TP) nhiều hơn vào chất lượng bằng chứng thực tế có trong note.

**(d) Rule đề xuất cho Playbook**
- [ ] Mọi sweep claim phải ghi rõ mốc giá cụ thể (EQH/EQL/PDH/PDL) — không dùng mô tả mơ hồ như "old lows".
- [ ] Setup Quality Checklist: nếu tick 9/9 hoàn hảo, thêm 1 dòng giải trình ngắn cho tiêu chí có khả năng bị điền theo outcome cao nhất (MSS, Displacement).
- [ ] RR kế hoạch > 2R → bắt buộc ghi kế hoạch partial TP TRƯỚC khi vào lệnh (không chỉ note lại sau).

**(e) Điều KHÔNG nên học từ lệnh này**
- Không nên coi checklist 9/9 hoàn hảo là chuẩn benchmark cho mọi lệnh sau — cần so sánh với các lệnh Loss để biết checklist có phân biệt được Win/Loss hay chỉ đơn giản luôn tick cao cho Win.
- Không nên dùng "giá đóng nến vào trong OB → respect OB" như một quy luật chắc chắn chỉ từ 1 mẫu — cần kiểm n≥20-30 để biết tỷ lệ OB thật sự được respect khi có đóng nến ngược.
- Không nên lấy Grade A của lệnh này làm chuẩn xác nhận rằng "EQH lồng trong OB" luôn là điểm sweep chất lượng — cần thống kê nhiều mẫu.


---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI: [[28 - Rejection Block]] · [[13 - FVG  - Fair Value Gap]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_Backtest Dashboard]]
