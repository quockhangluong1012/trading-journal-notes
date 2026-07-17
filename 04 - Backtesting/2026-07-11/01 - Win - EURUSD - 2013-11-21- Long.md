---
type: backtest
backtest_date: 2026-07-11
trade_date: 2013-11-21
symbol: EURUSD
position: Long
result: Win
session:
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: FVG
poi_rank: 2
poi_timeframe: M5
poi_location: Discount
poi_in_ote:
ce_ote_overlap:
poi_stack: OB (H1, 1.34083-1.33909) + FVG Bullish (M5) + FVG Bearish (M5) = BPR
fvg_high:
fvg_low:
ce_price:
entry_type: Edge
entry_precision: Edge-top
limit_filled: Yes
fill_depth_pct: 0
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: Yes
step5_poi_ok: Yes
step6_entry_ok: No
step7_target_ok: No
first_error_step: entry
missing_step: none
chained_fully: Yes
liquidity_swept: Yes
sweep_type: Internal
displacement: Yes
displacement_score:
mss: Yes
fvg_valid: Yes
confluence_score: 1
smt_confirm:
cisd_confirm: No
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: Yes
correlated_asset: none
entry_price: 1.34239
stop_loss: 1.34085
take_profit: 1.34728
r_planned: 3.18
rr_if_ce:
rr_if_ote:
r_multiple: 3.18
risk_percent:
spread_cost:
r_net:
grade: A
followed_plan: Yes
confidence: 4
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2013-11-21 — EURUSD Long — POI & Step Decision

> [!warning] Đã sửa lỗi dữ liệu khi convert từ template cũ
> - `r_planned` frontmatter cũ ghi **3.41**, sai lệch với bảng Summary cũ (3.18) và với chính giá entry/SL/TP. Tính lại: (1.34728−1.34239)/(1.34239−1.34085) = **3.18** → đã sửa theo đúng con số này (đây chính là lỗi mà bạn tự ghi trong "Rule Data Hygiene" của bản gốc).
> - Tiêu đề bản gốc ghi nhầm ngày "2013-05-02" — đã sửa lại đúng `trade_date` 2013-11-21.
> - `session` để **trống** — bản gốc chỉ ghi "New York" chung chung, không đủ căn cứ để xác định New York AM hay PM (giờ MSS 16:20 / displacement 15:35 ngày 21/11/2013 không rõ timezone gốc). Bạn cần xem lại chart và điền `New York AM` hoặc `New York PM`.
> - `poi_type` gốc ghi sai (link tới `[[01 - ICT 2022 Model]]` — đây là **tên model**, không phải loại POI). Đã đổi thành `FVG` (gần nhất với BPR thực tế đã dùng để entry — xem mục 2).
> - Các field mới hoàn toàn của template (`fvg_high/low`, `smt_confirm`, `in_macro_time`, `displacement_score`, `risk_percent`, `spread_cost`, `r_net`, `missed_by`) **để trống** vì bản backtest gốc không ghi đủ dữ liệu — không suy diễn để tránh làm sai lệch dashboard. Xem danh sách đầy đủ ở cuối file.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                      |
| Model Variant             | Standard (D1/H4→H1→M5)                                      |
| Trade Date (dữ liệu)      | 2013-11-21                                                  |
| Position                  | Long                                                        |
| Result                    | Win                                                         |
| Session                   | *(chưa xác nhận AM/PM — xem cảnh báo trên)*                 |
| HTF Bias                  | Bullish                                                     |
| Bias Correct?             | Yes                                                         |
| **POI Type**              | FVG (thực chất là BPR: OB H1 + 2 FVG M5 chồng nhau)         |
| POI Rank (8.1)            | 2 (FVG+OB)                                                  |
| POI Timeframe             | M5 (bối cảnh H1)                                            |
| POI Location              | Discount                                                    |
| **Entry Type**            | Edge (không chờ về CE)                                      |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | entry                                                        |
| R Planned (gross)         | 3.18                                                         |
| R Net (sau spread)        | *(chưa có — cần `risk_percent`/spread thực)*                |
| R Multiple (kết quả)      | 3.18                                                         |
| Confluence Score (0–8)    | 1 *(chỉ tính được `idm_swept`; các mục khác chưa được đánh giá ở bản gốc)* |
| Grade                     | A                                                            |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

> [!note] model_variant = Standard: bias trên D1/H4, POI/context trên H1, execution M5.

- **Bias**: Bullish — *lý do*:
  - Giá đang trong trend tăng với các HH/HL.
  - BOS ngày 18/09/2013 xác nhận Bullish.
  - Nhịp Pullback từ 28/10/2013 đến 20/11/2013 kết thúc bằng một CISD phá qua chuỗi nến giảm.
- **Dealing Range**: High 1.35787 / Low 1.32927 → **Discount** (đúng phía cho Long).
- **Draw on Liquidity (target cuối)**:
  - Buy-side (BSL): Liquidity Void / FVG D1 1.35938–1.36970.
  - Sell-side (SSL): Old low 1.32927.

![[Pasted image 20260711155108.png]]
![[Pasted image 20260711155048.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: OB H1 (1.34083–1.33909) là bối cảnh; entry thực tế nằm trong **BPR M5** hình thành từ 1 FVG Bullish chồng lên 1 FVG Bearish của nhịp giảm trước đó → `poi_type: FVG`, `poi_stack: OB(H1)+FVG Bull(M5)+FVG Bear(M5)=BPR`.
- **POI Rank (8.1)**: 2/5 (FVG+OB).
- **POI hình thành trên khung**: M5 (trong bối cảnh OB H1).
- **POI nằm ở**: Discount — đúng phía cho Long.
- **CE của FVG có trùng OTE 62–79%?**: chưa xác nhận (`ce_ote_overlap` để trống — bản gốc không đối chiếu với Dealing Range fib).
- **Bounds & CE**: BPR gốc ghi "1.34237 - 1.34-96" (lỗi đánh máy, không đọc được số chính xác) → `fvg_high`/`fvg_low`/`ce_price` **để trống**, cần bạn xem lại chart gốc để điền chính xác.

![[Pasted image 20260711155048.png]]

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: Edge → `entry_type: Edge`.
- **Entry Precision**: Edge-top (vào ngay cạnh trên BPR, entry 1.34239 khớp sát cạnh, thay vì chờ về CE).
- **Limit có được khớp không?**: Yes (giá chạm đúng cạnh, lệnh khớp).
- **Giá đi sâu bao nhiêu vào FVG?**: ~0% (`fill_depth_pct: 0` — vào ngay tại mép gần, chưa đi vào sâu như một entry tại CE).
- **RR ghi lại**: `r_planned` thực tế = 3.18. `rr_if_ce` **để trống** vì bounds BPR bị lỗi đánh máy trong bản gốc, không tính được chính xác nếu vào CE thay vì Edge — cần bạn bổ sung số liệu chart.

> [!note] Đây chính là lesson gốc bạn đã tự ghi: quyết định "bắt cạnh" thay vì chờ CE là *reactive* (do cảm giác "tưởng đã lỡ nhịp"/FOMO), không phải theo một rule A/B định trước — xem mục 6 và 7.

![[Pasted image 20260711154943.png]]

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? | Ghi chú |
|---|---|---|---|
| 1 | **Bias** | Yes | D1 bias Bullish rõ ràng, xác nhận bằng BOS + CISD trên pullback. |
| 2 | **Draw on Liquidity** | Yes | DOL xác định đúng ở bước HTF (FVG D1 1.35938–1.36970 / SSL 1.32927). |
| 3 | **Liquidity Sweep** | Yes | Quét inducement (swing low trên OB) + quét vào OB H1. |
| 4 | **Displacement + MSS** | Yes | Displacement tăng mạnh tạo FVG + MSS lúc 16:20 ngày 21/11/2013. |
| 5 | **POI (FVG/OB...)** | Yes | OB H1 hợp lệ, đúng Discount; BPR M5 hình thành hợp lệ trong displacement leg. |
| 6 | **Entry (retrace)** | **No** | Vào tại cạnh BPR thay vì chờ CE — quyết định *in-the-moment* do FOMO, không theo rule định trước. |
| 7 | **Target** | **No** | TP đặt tại internal liquidity M5 (bearish OB gần), **không tham chiếu** DOL đã xác định ở mục 1 (FVG D1 xa hơn nhiều) — "chốt non" so với bias. |

- **First Error Step**: `entry` — đây là mắt xích gãy sớm nhất (bước 6); bước 7 là hệ quả tiếp theo (chọn target gần vì đã thoát sớm theo kiểu trade intraday).
- **Missing Step**: none — chuỗi không thiếu bước nào, chỉ là chất lượng thực thi ở bước 6–7 chưa tối ưu.
- **Đủ chuỗi 7 bước?**: Yes.

> [!warning] Chống hindsight bias
> Sweep/Displacement/MSS/POI đều được nhận diện **trước** khi biết outcome nên giữ Yes. Bước Entry/Target được đánh giá No vì chính bạn đã tự nhận diện đây là quyết định phản ứng (reactive), không phải kế hoạch — xem [[Mistake - Chase Displacement]].

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE:**
- [x] Bias HTF rõ + draw xác định
- [x] Liquidity sweep TRƯỚC displacement + reclaim → `sweep_type: Internal`
- [x] Displacement hợp lệ (mô tả: nến đẩy mạnh + phá cấu trúc + tạo FVG) — `displacement_score` để trống, bản gốc không chấm điểm theo 4 tiêu chí CLV/wick/acceptance/FVG.
- [x] MSS hợp lệ
- [x] FVG/POI sạch, entry là retrace (dù tại Edge chứ không phải CE)
- [x] Entry đúng Discount, đồng hướng bias
- [x] Stop có logic (dưới cạnh BPR) + target có R:R ≥ kế hoạch (3.18)

**SCORE (0–8) — chỉ tính được các mục có bằng chứng rõ trong bản gốc:**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 | No | Rank 2 (FVG+OB) |
| 2 | CE trùng OTE 62–79% | *(chưa đánh giá)* | Bản gốc không đối chiếu |
| 3 | SMT divergence | *(chưa đánh giá)* | Không có ghi nhận |
| 4 | CISD flip LTF | No | Bản gốc dùng MSS, không phải CISD cho leg này |
| 5 | Macro time | *(chưa đánh giá)* | Không rõ khung giờ chính xác |
| 6 | NWOG/NDOG align | No | Không đề cập |
| 7 | −2SD / ERL target | No | TP là internal liquidity, không phải −2SD |
| 8 | Inducement bị quét trước POI | **Yes** | Sweep swing low trên OB trước khi vào OB |

- **Confluence Score**: 1 (chỉ đếm mục có bằng chứng — các mục "chưa đánh giá" cần bạn xem lại chart để chấm dứt điểm chính xác, không nên mặc định Yes/No).
- **Correlated asset**: none (không ghi nhận trong bản gốc).
- **Grade**: A (giữ nguyên theo bản gốc).

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP.
- **Tại sao thắng?**
  - Kiên nhẫn chờ H1 đồng Bias với D1 (Bullish).
  - Chờ H1 quay về Discount trước khi tìm entry.
- **POI đã chọn có phải lựa chọn tốt nhất không?**
  - Có POI hạng cao hơn khả dụng (OB H1 tại CE ~65% vào vùng) nhưng bạn chọn vào sớm hơn tại cạnh BPR — đánh đổi fill-probability lấy RR thấp hơn.
- **Entry (Edge/CE/OTE) có tối ưu không?**
  - Không hẳn — nếu chờ về CE của BPR, RR sẽ cao hơn 3.18 hiện tại, nhưng rủi ro không được fill tăng lên. Đây là trade-off cần được **backtest thêm để lượng hoá**, không quyết định bằng cảm giác.
- **Fill**: khớp đúng như kỳ vọng tại Edge.
- **Bước đầu tiên sai**: Entry — lựa chọn khả dĩ khác tại thời điểm đó là kiên nhẫn chờ giá về đúng CE của BPR theo rule đã định trước (nếu có).
- **Chi phí (spread/slippage)**: chưa ghi nhận `spread_cost`/`r_net` — cần bổ sung.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 90% (giá không quay về CE cho RR cao hơn).
- **Nếu vào lại, tôi sẽ làm gì khác?**
  - Cần thêm backtest để xác định khi nào nên vào cạnh, khi nào nên chờ CE.

---

## 7. Lesson Learned

### Bài học kỹ thuật (đặc thù POI / bước)
**Root cause (nguyên nhân gốc) — chỉ có MỘT:**
Quyết định điểm entry **không dựa trên một rule đã định nghĩa TRƯỚC lệnh**. Việc chuyển từ "chờ CE" sang "bắt cạnh trên BPR" được quyết định *in-the-moment*, một phần vì cảm giác "tưởng mình đã lỡ nhịp" (FOMO) khi giá bật ra khỏi BPR — chứ không theo một tiêu chí chọn kịch bản A/B cố định. Lệnh thắng, nhưng lý do vào lệnh là *reactive*, không phải *planned*.

**Triệu chứng (symptoms):**
- Bỏ qua lần chạm FVG đầu tiên vì chưa có MSS → **đúng và kỷ luật**. Nhưng khi giá displacement ra khỏi BPR, tâm lý "đã lỡ" xuất hiện → chuyển sang bắt cạnh khi giá quay lại.
- Checklist cũ tick "Entry tại CE" nhưng thực tế entry tại **cạnh trên BPR (1.34239)** → self-report không khớp hành động thực (đã sửa trong template mới bằng field `entry_precision` bắt buộc).
- TP đặt tại **internal liquidity M5** trong khi Draw on Liquidity đã tự xác định ở mục HTF là **FVG D1 1.35938–1.36970** (cao hơn nhiều) → TP không tham chiếu DOL đã ghi. Giá đi tiếp mạnh sau khi thoát.

**Cơ chế thị trường (hiểu để không lặp lại):**
Sweep inducement (swing low phía trên OB) + quét vào OB H1 → rejection tại CE của OB → displacement tăng tạo FVG + MSS trên M5. Nhịp giảm trước để lại Bearish FVG, nhịp tăng để lại Bullish FVG → chồng lên nhau thành **BPR** — vùng imbalance đã "cân bằng", đóng vai trò institutional reference point. Retrace về cạnh trên BPR vẫn hợp lệ về logic; nhưng entry tại CE cho SL chặt hơn và RR cao hơn đáng kể. Đây là đánh đổi **fill-probability vs RR**, cần được *chọn có chủ đích*, không phải do cảm xúc.

### Pattern lặp lại (điều cần để ý lần sau)
- **"Bắt cạnh vì sợ lỡ"**: khi giá rời POI rồi quay lại, có xu hướng vào aggressive để không bỏ lỡ. Cần tách bạch: đây là *aggressive entry hợp lệ* hay *FOMO đội lốt lý luận EV*? Lần này thắng → rủi ro **outcome bias** củng cố một hành vi chưa được backtest validate.
- **TP thiên về internal liquidity gần**, chưa kéo tới HTF draw đã xác định → hệ thống có xu hướng "chốt non" so với bias.

### Rule cần thêm/cập nhật vào Playbook
- [ ] **Rule Entry (A/B định trước lệnh)**: trước khi vào, ghi rõ 2 kịch bản — **(A) CE-entry**: limit tại CE, SL dưới sweep, ưu tiên RR; **(B) Aggressive-entry**: market tại cạnh BPR/FVG *chỉ khi* MSS đã xác nhận. Điều kiện chọn A vs B phải khách quan (vd: khoảng cách tới CE, thời gian còn lại trong Kill Zone), không quyết định theo cảm xúc "sợ lỡ".
- [ ] **Rule TP**: TP mặc định tham chiếu DOL đã xác định ở mục HTF. Nếu trade intraday và DOL ở xa → partial tại internal liquidity + để runner hướng DOL, hoặc đóng cuối phiên; ghi rõ lý do nếu chốt sớm hơn DOL.
- [ ] **Rule Data Hygiene**: đối chiếu frontmatter khớp bảng Summary trước khi lưu (đặc biệt `r_planned`, `trade_date`, tiêu đề) — bản gốc từng sai cả hai, nay đã sửa khi convert.

---

## 8. Final Grade

| Tiêu chí | Điểm | Ghi chú |
|---|---|---|
| HTF Bias & Draw | 9/10 | Bias rõ, DOL xác định đúng ngay từ đầu |
| POI Selection (đúng loại + hạng + P/D) | 7/10 | Rank 2, đúng Discount, nhưng chọn cạnh BPR thay vì chờ setup hạng cao hơn |
| Liquidity Sweep | 9/10 | Sweep + reclaim rõ ràng trước displacement |
| Displacement / MSS quality | 8/10 | Mô tả mạnh nhưng chưa chấm điểm theo 4 tiêu chí |
| Entry Precision & Fill (Edge/CE/OTE) | 5/10 | Vào Edge do FOMO, không theo rule định trước |
| Risk Management (R net, RR) | 7/10 | RR 3.18 tốt nhưng thiếu `risk_percent`/`r_net` để xác nhận đúng ≤0.5%/lệnh |

**Overall Grade**: A (giữ nguyên — kết quả và chuỗi 5 bước đầu tốt, dù entry/target chưa tối ưu)

> [!tip] Chống curve-fitting
> Trigger (sweep + displacement + POI hợp lệ) nhận diện được **trước** khi biết outcome — hợp lệ để tính vào thống kê edge.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[Mistake - Chase Displacement]] · [[Mistake - Skip Liquidity Sweep]]

---

> [!important] Việc cần bạn bổ sung (không tự suy diễn khi convert)
> - `session`: xác nhận New York AM hay PM.
> - `fvg_high` / `fvg_low` / `ce_price`: bounds chính xác của BPR (bản gốc bị lỗi đánh máy "1.34-96").
> - `rr_if_ce`: tính lại sau khi có bounds chính xác.
> - `displacement_score` (0–4), `smt_confirm`, `in_macro_time`: cần xem lại chart gốc.
> - `risk_percent`, `spread_cost`, `r_net`: chưa từng được ghi ở bản gốc.
