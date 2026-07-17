---
type: backtest
backtest_date: 2026-07-10
trade_date: 2021-05-03
symbol: EURUSD
position: Short
result: Win
session: New York AM
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: "Yes"
poi_type: Unicorn
poi_rank: 5
poi_timeframe: H1
poi_location: Premium
poi_in_ote: "No"
ce_ote_overlap: "No"
poi_stack: Breaker+FVG (Unicorn)
fvg_high: 1.20680
fvg_low: 1.20616
ce_price: 1.20648
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
sweep_type: External
displacement: "Yes"
displacement_score:
mss: "Yes"
fvg_valid: "Yes"
confluence_score: 1
smt_confirm:
cisd_confirm:
in_macro_time:
nwog_ndog_align:
sd_target_align:
idm_swept:
correlated_asset:
entry_price: 1.2065
stop_loss: 1.20764
take_profit: 1.20408
r_planned: 3.075
rr_if_ce:
rr_if_ote:
r_multiple: 3.075
risk_percent:
spread_cost:
r_net:
grade: A
followed_plan: "Yes"
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2021-05-03 — EURUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi template (2026-07-17)
> Convert từ template backtest cũ sang **template POI & Step Decision**. Dữ liệu gốc (entry/SL/TP/result/lesson learned) giữ nguyên. `poi_type: Unicorn` là field lõi của lệnh này — đây là lệnh có confluence rõ ràng nhất trong 5 file được convert đợt này (Breaker Block ⊕ FVG = Unicorn, nằm trong Premium). `ce_price` (1.20648) là **ước lượng trung điểm** của vùng Unicorn 1.20680–1.20616 vì bản gốc không ghi số CE chính xác riêng — entry thực tế 1.2065 nằm rất sát trung điểm này nên khớp với phân loại `entry_type: CE`.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5)                                       |
| Trade Date (dữ liệu)      | 2021-05-03                                                   |
| Position                  | Short                                                        |
| Result                    | Win                                                          |
| Session                   | New York AM (suy luận, không có mốc giờ gốc)                 |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | Unicorn (Breaker Block ⊕ FVG)                                |
| POI Rank (8.1)            | 5/5                                                          |
| POI Timeframe             | H1                                                           |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | none                                                         |
| R Planned (gross)         | 3.075                                                        |
| R Net (sau spread)        | —                                                             |
| R Multiple (kết quả)      | 3.075                                                        |
| Confluence Score (0–8)    | 1 (POI hạng ≥3)                                              |
| Grade                     | A                                                             |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Khung D1 đang trong trend giảm
  - Hình thành các LH/LL
  - Sau đó có 1 nhịp Pullback lớn, tuy nhiên chưa phá được protected high -> chưa đổi bias, chỉ là pullback
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity:
    - Dealing Range High = 1.23473 (xa giá hiện tại)
    - EQH = 1.21751 (gần giá hơn), có khả năng quét EQH này trước khi đi xuống tiếp. EQH này nằm trong vùng Premium
  - Sell-side liquidity: Giá đang hướng tới vùng
    - Swing low: 1.17149 (Swing low quan trọng)
    - Bullish Order Block: 1.16576 - 1.16197
    - EQL dưới OB: 1.16045

![[Pasted image 20260710092400.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: LH/LL
- **Dealing Range**: High 1.21058 · Low 1.19436
- **POI chính**:
  - Breaker Block: 1.20750 - 1.20616 (hình thành từ Order Block ngày 24/04/2021, bị invalidate ngày 30/04/2021 với 1 nến displacement mạnh — thân nến rất lớn đóng qua Order Block và quét luôn các old lows bên dưới tới 1.20142)
  - Nhịp displacement mạnh tạo ra 1 FVG rất lớn (1.20688 - 1.20430)
  - Quan trọng: FVG trùng lắp 1 phần với Breaker Block hình thành vùng **Unicorn: 1.20680 - 1.20616** → đã có POI quan trọng confluence
- **Liquidity cần chờ sweep**:
  - Vùng Unicorn
  - Lấp FVG
  - Kỳ vọng phản ứng sau khi quét qua Unicorn (quan sát thường thấy giá quét qua ngoài vùng Unicorn để trader vào lệnh sớm đặt stoploss ngoài vùng vừa quét)

### Phân Tích:

- Ngày 24/04/2021 giá tạo 1 Order Block (1.20750 - 1.20616), sau đó 1 nhịp đẩy giá mạnh với displacement kèm FVG
- Sau nhịp đẩy giá tạo Swing High (đỉnh của range)
- Sau đó giá bắt đầu các nhịp giảm
- Ngày 30/04/2021, giá tạo các nến displacement thân lớn quét qua Order Block và các Old Lows
- Nhịp displacement phá OB đó hình thành Breaker Block đồng thời kèm 1 FVG lớn (do nến displacement thân lớn, vùng không chồng lắp lớn)
- Đồng thời FVG overlap với Breaker Block hình thành vùng Unicorn (1.20680 - 1.20616)
- Vùng Unicorn nằm trong Premium -> đã có Premium/Discount confluence
- Giá consolidation sau nhịp displacement mạnh (khả năng là phân phối giá)
- Sau nhịp đi ngang tới ngày 3 tháng 5 2021, giá bắt đầu retrace về vùng Unicorn với các nến lớn
- Khi giá quay về vùng Unicorn tôi quan sát chứ không vào liền tại vùng CE (quá khứ tôi đã từng vào lệnh vội tại vùng CE khi thấy giá retrace về vùng POI quan trọng)
- Đúng như kỳ vọng, giá quét lên cạnh trên vùng Unicorn 1 đoạn (đóng nến tăng)
- Chỗ này có 2 khả năng: (1) giá đã đóng bên ngoài, nến sau tăng tiếp giá giữ bên ngoài thì Unicorn bị invalidate -> bỏ Setup; (2) giá quét sâu để quét stoploss các trader FOMO vào lệnh sớm khi giá chạm Unicorn hoặc CE (như tôi lần trước)
- Sau khi giá đóng nến bên ngoài thì xuất hiện nến reject mạnh quay lại trong vùng Unicorn và đóng bên dưới vùng
- Sau đó giá retrace về đúng vùng CE
- Xuống khung M5 quan sát giá phản ứng

![[Pasted image 20260710092549.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: Unicorn (Breaker Block 1.20750–1.20616 ⊕ FVG 1.20688–1.20430) → `poi_type: Unicorn`
- **POI Rank (8.1)**: 5/5 — cao nhất trong thang chất lượng → `poi_rank: 5`
- **POI hình thành trên khung**: H1 → `poi_timeframe: H1`
- **POI nằm ở**: Premium (đúng phía cho Short) → `poi_location: Premium`
- **POI stack**: Breaker Block + FVG = Unicorn, đồng thời nằm trong Premium (3 lớp confluence) → `poi_stack: Breaker+FVG (Unicorn)`
- **CE của FVG có trùng dải OTE 62–79% không?**: Không — bản gốc tự nhận "giá không nằm trong vùng OTE" → `ce_ote_overlap: No`, `poi_in_ote: No`
- **Bounds & CE**: Unicorn High 1.20680 (`fvg_high`) · Unicorn Low 1.20616 (`fvg_low`) · CE ước lượng ~1.20648 (`ce_price`, trung điểm — không có số CE tách riêng trong bản gốc)

> [!tip] Đây là POI hạng A đúng nghĩa
> Ba lớp confluence cùng chỉ về một hướng: **Breaker Block** (đã invalidate OB cũ bằng displacement thật) **⊕ FVG lớn** (cùng nhịp displacement) **⊕ nằm trong Premium** (đúng phía cho Short). Đây là lý do phản ứng mạnh và sạch — không phải may mắn.

![[Pasted image 20260710092729.png]]

*(Zoom M5)*
![[Pasted image 20260710092800.png]]

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: CE → `entry_type: CE` (entry 1.2065 nằm sát trung điểm vùng Unicorn 1.20680–1.20616)
- **Entry Precision**: CE (đúng 50%) → `entry_precision: CE`
- **Limit có được khớp không?**: Yes → `limit_filled: Yes`
- **Giá đi sâu bao nhiêu vào FVG?**: không có số liệu FVG M5 cụ thể để tính chính xác % → để trống `fill_depth_pct`
- **RR ghi lại**: `r_planned` = `r_multiple` = 3.075 (theo TP đã đạt)

### M5 — Xác nhận và điểm vào lệnh (nguyên văn phân tích gốc)

- Nhịp giá đóng nến mạnh khung H1 quay lại vùng Unicorn tạo thành 2 FVG trên khung M5. 1 FVG nằm đúng ngay vùng CE
- CE của FVG (gần giá khung M5) trùng với CE Unicorn -> chú ý quan sát
- Chờ giá retrace về FVG
- Giá quay về FVG nhịp 1 và bật ra mạnh -> Tôi entry nhịp này
- MSS đã có trong nhịp giá giảm mạnh từ đỉnh (giá quay lại sau khi đóng nến ngoài Unicorn)
- Stoploss đặt bên trên điểm sweep (1.20763)
- **Entry trigger**:
  - Liquidity Sweep: Quét qua vùng Unicorn để bẫy những trader vào sớm + Quét qua FVG/CE của FVG tạo thành từ nhịp displacement quay lại vùng
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - Tâm lý khi vào lệnh lúc đó còn hơi sợ khi giá quét lên FVG thêm 2 nhịp (vẫn nằm trong vùng Unicorn)
- **Entry reason**: Giá hình thành Setup theo mô hình ICT 2022: Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là Unicorn H1)
- **Invalidation reason**: Giá đóng qua cạnh trên Unicorn và giữ bên trên
- **Tôi có chờ đủ điều kiện không?** Có

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? (`Yes/No/NA`) | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | D1 Bearish, pullback chưa phá protected high |
| 2 | Draw on Liquidity | Yes | SSL cụ thể (swing low, Bullish OB, EQL) xác định trước |
| 3 | Liquidity Sweep | Yes | Quét ra ngoài cạnh trên Unicorn để bẫy FOMO, sau đó reject |
| 4 | Displacement + MSS | Yes | Displacement rõ + MSS xác nhận trên M5 |
| 5 | POI (FVG/OB...) | Yes | Unicorn đúng phía Premium |
| 6 | Entry (retrace) | Yes | Không vào tại CE lần chạm đầu — đã sửa lỗi FOMO cũ, chờ đủ chuỗi mới entry |
| 7 | Target | Yes | Hit TP, partial hợp lý |

- **First Error Step**: `none`
- **Missing Step**: `none`
- **Đủ chuỗi 7 bước?**: Yes

> [!tip] Hành vi đáng ghi nhận nhất của lệnh này
> Bước 6 (Entry) là điểm khác biệt lớn nhất so với file 2026-07-08 (lệnh Loss FOMO): lần này **không vào tại lần chạm CE đầu tiên**, mà chờ giá quét ra ngoài rồi reject rồi mới xuống M5 tìm entry. Đây chính xác là hành vi ngược lại với root cause FOMO đã ghi nhận ở lệnh Loss trước đó.

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE (pass/fail):**

- [x] Bias HTF rõ + draw xác định
- [x] Liquidity sweep TRƯỚC displacement + reclaim → sweep_type: External
- [x] Displacement hợp lệ
- [x] MSS hợp lệ
- [x] FVG/POI sạch + entry là retrace
- [x] Entry đúng Premium/Discount, đồng hướng bias
- [x] Stop có logic + target pool rõ + R:R ≥ kế hoạch

**GATE: PASS toàn bộ.**

**SCORE — mỗi confluence +1 (0–8):**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 (Breaker/iFVG/Unicorn) | **Có (+1)** | Unicorn = rank 5, cao nhất thang |
| 2 | CE∩OTE overlap | Không | Bản gốc tự nhận không nằm trong OTE |
| 3 | SMT confirm | Không rõ | Không có dữ liệu gốc |
| 4 | CISD confirm | Không rõ | Không có dữ liệu gốc |
| 5 | In macro time | Không rõ | Không có dữ liệu gốc |
| 6 | NWOG/NDOG align | Không rõ | Không có dữ liệu gốc |
| 7 | −2SD/ERL target | Không rõ | Không có dữ liệu gốc |
| 8 | IDM swept | Không rõ | Nhịp quét ra ngoài Unicorn để bẫy FOMO **có thể** tính là IDM sweep nhưng không đủ căn cứ để khẳng định chắc chắn — để trống thay vì đoán |

- `confluence_score`: 1
- **Quy đổi điểm → hạng**: 0–1 = C theo bảng quy đổi thuần SCORE — nhưng Grade tổng thể ở mục 8 vẫn là **A** vì GATE pass 100% và chất lượng thực thi (kiên nhẫn, đúng chuỗi 7 bước) là yếu tố quyết định hơn số lượng confluence nâng cao được ghi nhận.

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP. Điểm cải thiện: Partial Take Profit khi giá quét xuống 1 Short-term Low H1 (take 50% khi đạt 2.1R). Sau đó giá quét thêm 1 đoạn xuống 1 đáy cũ nữa (relative EQL, TP2 thêm 2R)
- **POI đã chọn có phải lựa chọn tốt nhất không?**
  - Có — Unicorn là POI hạng cao nhất khả dụng, không có POI nào tốt hơn bị bỏ lỡ.
- **Entry (Edge/CE/OTE) có tối ưu không?**
  - CE là lựa chọn hợp lý và đã tránh lỗi vào lệnh tại lần chạm đầu (root cause FOMO cũ).
- **Fill**: Limit khớp đúng như kỳ vọng.
- **Bước đầu tiên sai (nếu có)**: Không có.
- **Chi phí (spread/slippage)**: không có dữ liệu spread cụ thể → để trống.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 90% (giá không nằm trong vùng OTE)
- **Nếu vào lại, tôi sẽ làm gì khác?** Cải thiện tâm lý giao dịch

---

## 7. Lesson Learned

> [!summary] Bài học cốt lõi của lệnh này
> Đây là một lệnh **process A-grade**: thắng vì *quy trình đúng*, không phải vì may. Giá trị lớn nhất không nằm ở +3.07R mà ở chỗ nó chứng minh mình đã **sửa được lỗi FOMO cũ** (không vào tại CE lần chạm đầu). Nhiệm vụ bây giờ là *đóng gói* hành vi đúng đó thành rule định lượng để lặp lại được, thay vì để nó phụ thuộc vào tâm trạng.

### 7.1. Bài học kỹ thuật

- **Confluence chồng lớp mới là POI hạng A.** Không phải FVG đơn lẻ, mà là **Unicorn = Breaker Block ⊕ FVG**, lại nằm trong **Premium** (equilibrium H1 = 1.20247, entry 1.2065 nằm trên → đúng vùng bán). Ba lớp cùng chỉ về một hướng → đây là lý do phản ứng mạnh và sạch.
- **Kiên nhẫn = để thị trường tự chứng minh trước khi cam kết vốn.** Chờ purge cạnh trên Unicorn → reject → M5 MSS + FVG rồi mới entry. Đây là hành vi cần *tái lập*, không phải ăn may một lần.
- **SL theo invalidation, không theo R mong muốn.** SL trên điểm sweep (1.20764) trả lời câu hỏi "khi nào luận điểm sai", chứ không phải "đặt đâu cho R đẹp". Giữ nguyên tư duy này.

**Triệu chứng (symptoms) — sinh ra từ root cause:**

- Lúc vào lệnh *"còn hơi sợ khi giá quét lên FVG thêm 2 nhịp (vẫn trong Unicorn)"*. → **Root cause:** entry đang là *reaction entry* mang tính discretionary, chưa có **tiêu chí trigger objective** (đóng nến hay chỉ wick? bao nhiêu nến xác nhận?). Không có tiêu chí cứng → còn chỗ cho nỗi sợ và do dự.
- Tick "đạt Kill Zone" nhưng **không ghi giờ vào lệnh**. → **Root cause:** thiếu kỷ luật logging timestamp; một tiêu chí được đánh dấu "đạt" mà không có bằng chứng kiểm chứng.
- `r_planned` = `r_multiple` = 3.075. → **Root cause:** R kế hoạch điền *sau* khi biết kết quả (hindsight), làm mất khả năng đo "mức chấp hành kế hoạch" khi mẫu lớn dần.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**

1. 24/04: hình thành OB tại 1.20616–1.20750, nhịp displacement + FVG đẩy giá tạo swing high (đỉnh range).
2. 30/04: nến displacement thân lớn **phá OB + quét old lows** xuống 1.20142 → OB bị invalidate → biến thành **Breaker**, đồng thời để lại **FVG lớn** (không overlap nhiều do nến thân lớn). Breaker ⊕ FVG = **Unicorn**, nằm trong Premium.
3. Giai đoạn đi ngang sau displacement = **re-distribution** (smart money nạp lệnh bán).
4. 03/05: giá retrace về Unicorn, **quét nhẹ ra ngoài cạnh trên** để gom BSL + stoploss của short vào sớm → reject → displacement xuống → chạy về SSL/EQL mục tiêu. Đây là mẫu kinh điển "return to breaker/FVG rồi tiếp diễn".

### 7.2. Pattern lặp lại (điều cần để ý lần sau)

- **"Giá ló ra ngoài rìa POI 1 đoạn rồi mới đảo chiều"** là pattern lặp lại của SM (purge liquidity sát POI trước khi đi). ⇒ Đừng vội invalidate ngay khi giá vừa ló ra ngoài vùng — nhưng *phải có ranh giới định lượng* để phân biệt purge với invalidation thật (xem 7.3).
- **FOMO tại CE lần chạm đầu = lỗi cũ.** Lần này đã tránh được → cần duy trì. Đây là hành vi đáng theo dõi thành một metric riêng ("số lệnh vào sớm sai vs vào đúng nhịp").
- **Hindsight bias khi kể chuyện "đó là cú trap".** Cùng price action, nếu thua mình sẽ gọi là "invalidation". Cảnh giác: chỉ được gọi là trap nếu tiêu chí objective (đã định trước) cho phép, không phải vì đã biết kết quả.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **Rule vào lệnh tại POI quan trọng:** KHÔNG entry tại CE lần chạm đầu. Bắt buộc đủ chuỗi: (a) liquidity sweep ra ngoài rìa POI → (b) reject candle **đóng cửa lại trong vùng** → (c) xuống M5 chờ **MSS + FVG hợp lệ** → (d) entry tại **CE của FVG M5** (ghi rõ ranh giới FVG).
- [ ] **Rule invalidation định lượng:** bỏ setup nếu giá **đóng ≥ 1 nến H1 (hoặc 2 nến M5)** trên cạnh trên Unicorn *và* nến kế tiếp không quay lại vùng. Thay "giữ bên trên" mơ hồ bằng số nến cụ thể.
- [ ] **Rule logging bắt buộc:** luôn ghi **entry timestamp (giờ VN + ET)** để verify Kill Zone, và **ranh giới FVG M5** để xác nhận entry = CE. Không có 2 dữ liệu này thì setup **không tính vào thống kê**.
- [ ] **Rule tách R:** ghi `r_planned` *trước* khi biết kết quả (theo TP dự kiến), `r_multiple` là kết quả thực.
- [ ] **Rule chấm điểm confluence:** OTE là *điểm cộng khi có*, KHÔNG trừ điểm setup 2022 Model khi thiếu OTE (entry model này neo vào FVG/CE, không phải Fibonacci retracement).
- [ ] **Rule TP chuẩn hoá:** partial TP1 50% tại short-term low gần nhất (~2R), runner tới EQL/SSL kế tiếp — đúng như lệnh này đã làm (blended 3.07R). Biến thành mặc định thay vì tuỳ hứng.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 |
| POI Selection (đúng loại + hạng + P/D) | 10/10 |
| Liquidity Sweep | 9/10 |
| Displacement / MSS quality | 9/10 |
| Entry Precision & Fill (Edge/CE/OTE) | 8/10 |
| Risk Management (R net, RR) | 8/10 (thiếu chuẩn hoá % partial TP) |

**Overall Grade**: A

> [!tip] Chống curve-fitting
> Trigger (purge cạnh Unicorn + reject + M5 MSS + FVG hợp lệ) được nhận diện **trước** khi biết outcome — người viết đã chủ động chờ, không hindsight. Mẫu này hợp lệ để đưa vào thống kê edge.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[04 - Breaker Block]] · [[13 - FVG  - Fair Value Gap]] · [[07 - Unicorn Model]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
