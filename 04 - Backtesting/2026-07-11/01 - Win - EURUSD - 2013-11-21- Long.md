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

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL tại thời điểm entry (1.34239):**
- Đã bị lấy (ERL, external): SSL inducement (swing low phía trên OB H1) — quét trước displacement, dùng làm sweep hợp lệ ở bước 3.
- Đã bị lấy (ERL): quét vào OB H1 (1.34083–1.33909) — rejection tại vùng CE của OB tạo displacement.
- **Chưa bị lấy (IRL, nằm trên đường đi từ entry tới SL 1.34085)**: không có swing low nội bộ nào giữa entry (1.34239) và SL, ngoài chính đáy OB — đây chính là "VUNG TRONG" mà `[[GBPUSD-20140717-liquidity-buffer.svg]]` mô tả cho một pattern khác trong vault: entry tại Edge mà không có liquidity đệm nội bộ giữa entry và SL khiến khoảng cách entry→SL "trống", giá có thể đâm thẳng qua nếu retrace mạnh hơn.
- DOL chưa bị lấy: BSL D1 FVG 1.35938–1.36970 (target thật theo bias) — TP thực tế (internal liquidity M5) nằm rất gần, chưa chạm DOL này khi lệnh đóng.

**Chất lượng displacement/MSS**: displacement tăng + MSS 16:20 21/11/2013 được note mô tả mạnh nhưng không có `displacement_score` (0–4 theo CLV/wick/acceptance/FVG) — không đánh giá được độ "sạch" thực sự, chỉ có nhãn định tính.

**Yếu tố thời gian**: `session` để trống trong frontmatter — note không xác nhận được New York AM/PM cho giờ MSS 16:20. Không thể đánh giá killzone timing có đúng chuẩn hay chỉ là ngẫu nhiên nằm trong giờ hoạt động cao.

**Vị trí entry trong dealing range**: Discount đúng phía. Nhưng entry tại Edge-top của BPR (0% fill depth) nghĩa là giá gần như không đi vào POI — mức xác nhận "giá tôn trọng POI" yếu hơn một CE-entry nơi giá đã đi tới đúng 50% imbalance.

**So sánh với các lệnh CE chuẩn trong vault**: đối chiếu [[01 - Win - EURUSD - 2021-05-03- Short]] (entry_type: CE, entry tại đúng CE 1.20648, fill_depth ngụ ý 50%, first_error_step: none, grade A) và [[01 - Win - XAUUSD- 2014-05-12- Short]] (entry_type: CE, CE 1300.5, first_error_step: none). Cả hai đạt `first_error_step: none` vì entry đợi đúng CE — khác với note này, nơi `first_error_step: entry` dù outcome cũng Win. Điểm chung của 3 lệnh CE-chuẩn: SL luôn còn "đệm" giữa CE và cạnh xa của POI, tạo buffer chịu được retrace sâu hơn Edge-entry. Xem SVG so sánh số thật ở mục 10.

![[MULTI-20260803-edge-vs-ce-entry.svg|760]]

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

**Evidence base**: chỉ có text note (frontmatter + bảng + narrative), không truy cập được ảnh PNG đính kèm (`Pasted image ...`) — coi các claim structure/POI như mô tả bằng lời của người dùng, không phải evidence hình ảnh độc lập. `evidence_sufficiency: thin` — load-bearing claim (chất lượng entry Edge-top) không thể đối chiếu với chart thật, chỉ với số liệu note tự ghi.

**Claim graph:**
- C1: HTF bias Bullish đúng (BOS 18/09 + CISD trên pullback) — PASS theo tự-báo cáo.
- C2: Sweep + displacement + MSS + POI (OB H1 + BPR M5) hợp lệ, nhận diện trước outcome.
- C3: Entry tại Edge-top của BPR (1.34239) là quyết định *in-the-moment* do FOMO, không theo rule A/B định trước — **load-bearing**, vì đây là claim mà toàn bộ lesson của note xoay quanh.
- C4 (từ C3): Vì lệnh Win, tác giả tự chấm Overall Grade A mà không hạ điểm cho C3.
- C5: TP đặt tại internal liquidity M5, không tham chiếu DOL D1 đã xác định ở bước 1 → "chốt non".

**Điều gì survives**: C1, C2 được note tự nhận diện trước outcome (sweep/displacement/MSS đều ghi Yes trước khi biết TP có bị hit) — không có dấu hiệu hindsight rõ ràng ở các bước này.

**Objections:**

**O1 · [METHOD] · fatal · attacks C3, C4**
Claim: "Lệnh Win nên Overall Grade giữ A dù entry tại Edge do FOMO."
Fails: quy trình tự chấm điểm dùng outcome (Win) để giữ nguyên grade cho một quyết định entry mà chính note gọi là *reactive*, không phải *planned* — đây là outcome-as-evidence kinh điển: không có gì trong quy trình ra quyết định lúc entry (16:20 21/11/2013) biết trước rằng giá sẽ không retrace sâu hơn.
Evidence: note tự thừa nhận "Lệnh thắng, nhưng lý do vào lệnh là reactive, không phải planned" (mục 7) và cảnh báo riêng "outcome bias" (mục Pattern lặp lại).
Consequence: nếu tách outcome ra khỏi grade, Entry Precision đã tự chấm 5/10 (mục 8) — phần này đúng, nhưng Overall Grade A thì không phản chiếu đúng điểm yếu này, tạo lệch giữa sub-score và overall.
Retracted by: một rule tường minh, viết trước lệnh, định nghĩa khi nào Edge-entry được phép override CE-entry (note tự đề xuất rule này ở mục 7 nhưng chưa áp dụng hồi tố cho grade).
Your best answer: "5 bước đầu (bias→POI) đều đúng và đó là phần lớn edge, entry chỉ là 1/7 bước." Không cứu được: chính note đặt `first_error_step: entry` là điểm gãy sớm nhất được công nhận, và bước 7 (target) là hệ quả trực tiếp của bước 6 — 2/7 bước sai vẫn đủ để hạ Entry Precision + Risk Management, y như cách GBPUSD (07-12) đã bị hạ Grade A→B cho một lỗi entry tương tự.

**O2 · [HINDSIGHT] · material · attacks C3**
Claim: "Đây là aggressive entry hợp lệ, đánh đổi fill-probability lấy RR thấp hơn — một trade-off có chủ đích."
Fails: không có gì trong note cho thấy trade-off này được *cân nhắc trước* lúc entry; nó chỉ được *diễn giải lại thành hợp lý* sau khi biết lệnh Win. Note tự ghi lý do thực là FOMO ("tưởng đã lỡ nhịp"), không phải một phép tính EV có chủ đích.
Evidence: mục 6 "Entry... có tối ưu không? Không hẳn... Đây là trade-off cần được backtest thêm để lượng hoá, không quyết định bằng cảm giác" — tự note đã phân biệt rõ cảm giác vs rule.
Consequence: nếu coi đây là "trade-off có chủ đích" thì sample này bị đưa vào thống kê edge như một *entry rule đã kiểm định*, trong khi thực chất là một lần ngoại lệ chưa kiểm định.
Retracted by: log ≥20-30 mẫu Edge-vs-CE cùng POI-stack để xác nhận Edge-entry có thật sự có edge riêng hay chỉ là biến thể của may rủi (chính note tự đề xuất ở Rule cần thêm).
Your best answer: không có phản bác mạnh — note đã tự nhận đây chưa kiểm định.

**O3 · [ARITHMETIC] · minor · attacks C3**
Note không có `fvg_high`/`fvg_low`/`ce_price` do lỗi typo bounds gốc ("1.34-96") nên **không thể tính CE thật của BPR** — mọi khẳng định "Edge-entry có RR cao hơn nếu chờ CE" trong note chỉ là suy luận định tính, chưa có số. Retracted by: bổ sung bounds BPR chính xác từ chart gốc.

**Filter**: soạn 4, cắt 1 (một objection về "POI rank 2 thấp" bị loại vì không đổi kết luận — cả rank cao/thấp đều không phải load-bearing so với vấn đề entry timing).

**Opposite case (từ cùng evidence)**: Edge-entry tại BPR sau MSS xác nhận có thể đọc như *aggressive continuation entry hợp lệ* — vì MSS + displacement đã xảy ra, giá quay lại test cạnh BPR (không phải retest ngẫu nhiên) có thể coi là "second touch xác nhận" giống pattern NAS100 (07-13) chờ nhịp thứ hai. Đối lập tự-kiểm: pattern NAS100 chờ nhịp thứ hai *có thêm* sweep+MSS+FVG mới trên M5 trước khi vào; note này không có nhịp xác nhận mới, chỉ là "giá bật ra rồi bắt cạnh" — nên self-objection này khiến case yếu đi. **Strength: weaker but non-trivial** — nếu note có ghi nhận một MSS/sweep M5 riêng tại thời điểm bắt cạnh (chưa có trong note hiện tại) thì case sẽ mạnh lên đáng kể.
**Distinguishing observable**: có hay không một swing/sweep M5 riêng ngay trước lúc bắt Edge — note hiện tại không ghi nhận điều này.

**Verdict**: **SURVIVES, WEAKENED** — load-bearing claim (C1, C2: bias & setup chain) đứng vững, nhưng claim entry (C3) và hệ quả grade (C4) bị suy yếu bởi O1/O2. `evidence_sufficiency: thin` (chỉ có text, không có chart) nên không thể nâng lên SURVIVES THIS ATTACK.

**Falsification tests** (tối đa 3):
1. Thu thập ≥20 Edge-entry và ≥20 CE-entry cùng POI-stack (OB+FVG chồng BPR), đo win rate + RR thực nhận. Nếu Edge-entry RR trung bình thấp hơn CE-entry ≥1R mà win rate không cao hơn đáng kể (≥15pp) → O1/O2 được xác nhận, Edge-entry không có edge độc lập ngoài may rủi. Đóng O1, O2.
2. Với các Edge-entry Loss trong vault (nếu có), kiểm retrace đã đi sâu bao nhiêu trước khi hit SL — nếu thường xuyên đi qua vùng CE trước khi quay đầu thắng, giả thuyết "Edge chết trước CE" được ủng hộ.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis**: Bullish bias D1, sweep+displacement+MSS hợp lệ trên OB H1/BPR M5, entry tại Edge-top của BPR, TP tại internal liquidity M5.

**Cần sửa** (load-bearing trước):
- C3 Entry "Edge" tại cạnh trên BPR — **UNSUPPORTED** (không FAIL định nghĩa) · SKILL.md § CE/Entry refine không cấm Edge-entry, nhưng note không đưa ra rule khách quan đã dùng để chọn Edge thay vì CE, chỉ có tường thuật cảm giác → không đủ evidence để PASS như một entry-rule có chủ đích → cần backtest ≥20-30 mẫu để nâng lên PASS. **(load-bearing)**
- C5 TP tại internal liquidity M5, không tham chiếu DOL D1 — **FAIL** · SKILL.md § Liquidity/Target: TP nên mô tả draw on liquidity đã xác định, ở đây DOL D1 (FVG 1.35938–1.36970) bị bỏ qua hoàn toàn cho một target gần hơn không có tên rõ ràng → fix: khi trade theo bias D1, TP mặc định nên tham chiếu lại DOL đã ghi ở bước 1, hoặc ghi rõ lý do partial sớm.
- C6 (`poi_stack` BPR = OB H1 + FVG Bull M5 + FVG Bear M5) — kế thừa từ thiếu bounds chính xác (không FAIL riêng, chỉ AMBIGUOUS vì bounds bị lỗi typo, không kiểm được CE thật).

**PASS**: C1 (HTF bias Bullish, BOS+CISD), C2 (sweep internal + displacement + MSS + POI OB/BPR hợp lệ trong Discount).

**Verdict**: **PARTIALLY ALIGNED** — load-bearing claim entry (C3) không FAIL định nghĩa nhưng UNSUPPORTED vì thiếu rule khách quan; C5 (TP) FAIL rõ theo doctrine liquidity target.

**Notes**: Doctrine gap — canon không fix cứng "khi nào Edge-entry được coi là hợp lệ ngang CE-entry"; đây là điểm mà cả 2 note Edge trong batch này (07-11, 07-12) đều rơi vào cùng một AMBIGUOUS fork, cần một rule Playbook riêng thay vì phán từng lệnh.

---

## 12. Lesson Learned (bản đầy đủ)

**(a) Bài học kỹ thuật:**
- *Ví dụ số thật*: Edge-entry tại 1.34239 (Edge-top của BPR) đạt RR 3.18 thực nhận; nếu retrace đủ sâu để chạm CE thật của BPR (chưa tính được do lỗi bounds), RR lẽ ra cao hơn nhưng SL không có đệm liquidity nội bộ giữa entry và đáy OB (1.33909) — xem SVG `[[MULTI-20260803-edge-vs-ce-entry.svg]]`.
- *Tổng quát hóa*: Edge-entry luôn đánh đổi "RR cao hơn + fill-probability thấp hơn" lấy "fill chắc hơn + RR thấp hơn + SL kém đệm hơn". Không có công thức nào đúng tuyệt đối — cần dữ liệu để biết khi nào đánh đổi này có lợi.

**(b) Bài học quy trình/checklist:**
- Cần field `entry_decision_rule` ghi rõ *trước* lệnh: chọn Edge hay CE theo tiêu chí nào (không phải điền sau khi đã biết outcome).
- TP luôn phải đối chiếu lại với DOL đã ghi ở bước 1 trước khi chốt — nếu chốt sớm hơn, ghi rõ lý do bằng số (khoảng cách còn lại, thời gian killzone còn lại).

**(c) Bài học tâm lý-hành vi:**
- FOMO ("tưởng đã lỡ nhịp") là động cơ thật của quyết định entry, được note tự thừa nhận. Nguy cơ: lệnh Win lần này có thể *tăng cường* hành vi FOMO-entry ở các lệnh sau (biến một sai lầm tâm lý thành "kinh nghiệm" giả).

**(d) Rule đề xuất cho Playbook:**
- [ ] Trước mỗi lệnh, ghi rõ 2 kịch bản A (CE-limit) / B (Edge-aggressive) và điều kiện chọn khách quan (khoảng cách tới CE tính bằng ATR hoặc %, thời gian còn lại trong killzone) — không quyết định bằng cảm giác.
- [ ] TP mặc định = DOL HTF đã ghi ở bước 1; nếu chốt sớm hơn, bắt buộc ghi lý do định lượng.
- [ ] Grade tối đa = B cho mọi lệnh có `first_error_step: entry`, bất kể outcome, cho tới khi có ≥20 mẫu Edge-entry xác nhận edge riêng (đồng nhất với rule GBPUSD 07-12 đã tự đề ra).

**(e) Điều KHÔNG nên học từ lệnh này:**
- KHÔNG nên học rằng "bắt cạnh khi giá rời POI rồi quay lại" là một entry rule đáng tin — outcome Win ở đây là 1 mẫu, không phải kiểm định. Nếu retrace lần này sâu hơn vài pip nữa (không có liquidity đệm nội bộ giữa entry và đáy OB), Edge-entry có thể đã chết trước khi giá chạm CE — điều mà lệnh CE-entry cùng POI-stack (ví dụ [[01 - Win - EURUSD - 2021-05-03- Short]]) sẽ không gặp phải vì SL của CE-entry vốn đã tính đến khoảng đó.

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
