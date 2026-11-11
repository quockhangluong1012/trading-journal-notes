---
type: backtest
backtest_date: 2026-07-17
trade_date: 2014-07-14
symbol: GBPUSD
position: Long
result: Win
session: New York (sau NY Open KZ)
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model (FVG POI + FVG Entry)
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: FVG
poi_rank: 3
poi_timeframe: H1
poi_location: Discount
poi_in_ote: Partial
ce_ote_overlap: Yes
poi_stack: H1 FVG 1.70833-1.70591 (spans EQ->OTE) + M5 FVG (entry CE 1.70837)
fvg_high: 1.70833
fvg_low: 1.70591
ce_price: 1.70712
entry_type: CE
entry_precision: CE
entry_in_ote: No
limit_filled: Yes
fill_depth_pct:
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: Yes
step5_poi_ok: Yes
step6_entry_ok: Partial
step7_target_ok: Yes
first_error_step: 6
missing_step: none
chained_fully: Yes
liquidity_swept: Yes
sweep_type: Internal
displacement: Yes
displacement_score:
mss: Yes
fvg_valid: Yes
confluence_score: 3
smt_confirm: No
cisd_confirm: No
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: No
correlated_asset: none
entry_price: 1.70837
stop_loss: 1.70576
take_profit: 1.71444
r_planned: 2.33
rr_if_ce: 2.33
rr_if_ote: 5.0
r_multiple: 2.33
risk_percent:
spread_cost:
r_net:
grade: B
followed_plan: Yes
confidence: 3
confirmation_type: MSS
tp2_extended_target:
tags:
  - backtest
  - ICT2022
  - POI
  - MSS
  - FVG
  - entry-location
---

# Backtest 2014-07-14 — GBPUSD Long — FVG POI & FVG Entry (ICT 2022 Model)

> [!warning] Dọn "vết clone" — file này trước đó là của một lệnh Order Block khác (vùng 1.69xxx). Toàn bộ đã được viết lại theo lệnh FVG 1.70xxx thật của bạn.
> Ngoài ra **tên file (`2014-06-25`) không khớp ngày lệnh (`2014-07-14`)** — nên đổi tên file thành `02 - Win - GBPUSD - 2014-07-14 - Long.md` cho đúng convention. Tôi chưa tự đổi tên (chờ bạn xác nhận). Chart hiển thị "Mon 14 Jul '14" (dữ liệu replay 2014); bạn ghi "14/7/2026" trong mô tả — `trade_date` tôi để theo chart là `2014-07-14`, `backtest_date` = ngày bạn backtest `2026-07-17`.

---

## 0. Backtest Summary

| Field                  | Value                                                             |
| ---------------------- | ---------------------------------------------------------------- |
| Symbol                 | GBPUSD                                                            |
| Model Variant          | Standard (D1 → H1 → M5)                                           |
| Trade Date (dữ liệu)   | 2014-07-14                                                        |
| Position               | Long                                                             |
| Result                 | Win (hit TP 1.71444)                                             |
| Session                | New York (entry ~21:50 UTC+7)                                    |
| HTF Bias               | Bullish                                                          |
| Bias Correct?          | Yes                                                             |
| **POI Type**           | FVG (H1, Discount) — trải EQ → OTE                               |
| POI Rank (8.1)         | 3 (FVG + OTE overlap) — *cần đối chiếu bảng 8.1 của bạn*         |
| POI Timeframe          | H1 (entry refine M5)                                             |
| POI Location           | Discount ✓ nhưng entry nằm ở **nửa nông** (giữa 0.5 và 0.618)   |
| **Entry Type**         | CE của FVG M5 = 1.70837                                          |
| **Limit Filled?**      | Yes                                                             |
| **First Error Step**   | Step 6 — Entry hợp lệ nhưng **vị trí quá nông** (không phải sai chuỗi) |
| R Planned              | 2.33 (đã verify: risk 26.1 pip / reward 60.7 pip)               |
| R Multiple (kết quả)   | 2.33 (hit TP đầy đủ)                                             |
| R nếu entry sweet spot | ~5.0 (illustrative — xem mục 3 & 6)                              |
| Confluence Score       | 3/8                                                             |
| Grade                  | **B** (đề xuất)                                                  |

> [!info] Các con số đã được kiểm tra lại (mục quan trọng)
> - **CE FVG H1 = 1.70712**, KHÔNG phải 1.70771 như bạn ghi. (1.70833 + 1.70591) / 2 = 1.70712 — lệch ~6 pip, cần sửa lại trong phân tích của bạn.
> - **EQ (0.5) = 1.70956**, không phải 1.70964 (chart hiển thị 0.5 = 1.70956). Lệch nhỏ nhưng nên dùng số đúng.
> - **OTE**: 0.618 = 1.70748 · 0.705 = 1.70594 · 0.786 = 1.70451 (khớp chart, số của bạn đúng).
> - **RR 2.33 ✓ đúng.**

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 — Daily Bias

- **Bias**: Bullish · **Market Condition**: Trending.
- **Lý do**: cấu trúc D1 tạo HH/HL liên tục; nhịp expansion tăng mạnh có displacement rõ, kèm **DOB (Displacement Order Block)** xác nhận bias Bullish. Không có tín hiệu đảo chiều D1 tại thời điểm setup.
- **Draw on Liquidity**: Buy-side — mục tiêu hướng lên (BSL phía trên). Dealing range D1/H1 nằm gọn trong nhịp tăng nên bias Long và draw-on-liquidity thẳng hàng, không mâu thuẫn khung.

> [!check] Đánh giá phân tích D1 của bạn: **Chính xác và đầy đủ.** HH/HL + displacement + DOB là chuỗi lý luận bias đúng chuẩn. Không thiếu gì ở khung này.

![[Pasted image 20260717130956.png]]

### H1 — Cấu trúc, Dealing Range & POI

- **Dealing Range H1**: High **1.71838** / Low **1.70074** → **EQ (0.5) = 1.70956**.
- **OTE (fib retrace từ đáy range)**: 0.618 = **1.70748** · 0.705 (sweet spot) = **1.70594** · 0.786 = **1.70451**.
- **H1 POI = FVG Bullish 1.70833 – 1.70591**, **CE = 1.70712**.
- **Vị trí FVG trong range** (điểm cốt lõi của cả lệnh này):
  - **Cạnh trên FVG (1.70833)** nằm **giữa 0.5 (EQ) và 0.618** → vùng *discount nông*, chưa vào OTE.
  - **CE FVG (1.70712)** nằm ngay dưới 0.618 → **vừa chạm mép trên OTE**.
  - **Cạnh dưới FVG (1.70591)** ≈ **0.705 sweet spot** → *discount sâu*, vùng tài trợ thật.
  - ⇒ FVG **bị EQ/OTE cắt làm hai nửa xác suất khác nhau**: nửa trên (nông) không phải nơi smart money nạp lệnh; nửa dưới (0.618 → 0.705) mới là vùng hội tụ.
- **Diễn biến**: giá retrace vào FVG lúc ~19:00 (14/7), đi trong FVG; đến ~21:50 quét qua CE FVG và tạo MSS + displacement + FVG trên M5.

> [!check] Đánh giá phân tích H1 của bạn:
> - Dealing range, OTE: **đúng**.
> - **Sai số cần sửa**: CE FVG (bạn ghi 1.70771 → đúng là **1.70712**); EQ (1.70964 → **1.70956**).
> - **Nhận định "50% dưới FVG trong OTE, 50% trên nằm giữa EQ–OTE" của bạn là CHÍNH XÁC** — và đây chính là mấu chốt giải thích vì sao giá còn quét xuống (xem mục 6).

![[Pasted image 20260717131030.png]]

---

## 2. POI Profile

- **POI Type**: FVG (H1), Discount.
- **POI Rank (8.1)**: 3 — FVG + OTE overlap (đối chiếu lại bảng xếp hạng 8.1 của bạn để chốt số).
- **POI hình thành trên khung**: H1 (entry refine M5).
- **POI nằm ở**: Discount ✓ — nhưng **entry thực tế nằm ở nửa nông** (giữa 0.5 và 0.618), không ở nửa OTE sâu.
- **POI stack**: H1 FVG (1.70833–1.70591) chứa M5 FVG entry (CE 1.70837).
- **CE FVG H1 trùng OTE?**: CE = 1.70712 → **có**, nằm sát mép trên OTE (0.618 = 1.70748). Nhưng **giá entry của bạn (1.70837) ở TRÊN cả CE lẫn 0.618** → tức entry chưa chạm OTE.
-
![[Pasted image 20260717131030.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE của **FVG M5** = **1.70837**.
- **Vị trí entry trong POI H1**: sát **cạnh trên FVG H1 (1.70833)** → điểm **nông nhất** của POI, thậm chí nông hơn CE FVG H1 (1.70712).
- **Stop Loss**: **1.70576** (dưới cạnh dưới FVG 1.70591 + buffer ~1.5 pip).
- **Take Profit**: **1.71444** (BSL phía trên).
- **RR**: **2.33** (đã verify).

### M5 — Xác nhận & Điểm vào lệnh

1. Giá vào FVG H1, quét qua CE FVG H1.
2. **MSS + Displacement + FVG (Bullish)** hình thành trên M5 lúc ~21:50.
3. Giá retrace về FVG M5 → **entry tại CE của FVG M5 = 1.70837**.
4. **Sau entry, giá quét tiếp xuống cạnh dưới FVG H1 (~1.70591 / 0.705)** — sát SL 1.70576 (chỉ cách ~1.5 pip) → rồi mới bật lên chạy tới TP.

> [!warning] Điểm chí mạng: **MSS M5 xuất hiện khi giá mới chỉ tap NÔNG vào FVG H1.** Một MSS trên LTF sau cú tap nông của POI HTF là **MSS "sớm"** — nó có thể chính là một nhịp inducement/quét thanh khoản của LTF, chưa phải shift thật của HTF. Đây là lý do bạn vào lệnh đúng quy trình nhưng ở **vị trí kém tối ưu**.

**Entry trigger**: Retrace vào FVG H1 → quét CE → MSS + displacement + FVG M5 → entry CE FVG M5.
**Invalidation**: giá đóng nến dưới cạnh dưới FVG H1 / dưới SL 1.70576 → luận điểm Long vô hiệu.

![[Pasted image 20260717131045.png]]

### Minh họa lỗi vị trí entry (SVG)

![[GBPUSD-20140714-entry-location.svg|697]]

> So sánh RR: **Entry nông** (của bạn) risk ~26 pip → **RR 2.33**. **Entry sweet spot** (0.705 ≈ cạnh dưới FVG) risk ~16 pip → **RR ~5.0** với cùng TP. Vào sâu hơn cho SL ngắn hơn, RR gấp đôi, và độ tin cậy cao hơn vì đợi POI được "dùng xong" thanh khoản.

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | D1 Bullish, HH/HL + DOB |
| 2 | Draw on Liquidity | Yes | BSL phía trên (TP 1.71444) |
| 3 | Liquidity Sweep | Yes | quét CE FVG H1 (internal) |
| 4 | Displacement + MSS | Yes | MSS + displacement + FVG M5 (nhưng trên tap NÔNG) |
| 5 | POI (FVG, Discount) | Yes | FVG H1 đúng phía discount |
| 6 | Entry (CE FVG M5) | **Partial** | hợp lệ nhưng **vị trí quá nông** (nửa trên FVG, chưa vào OTE) |
| 7 | Target | Yes | hit TP 1.71444, RR 2.33 |

- **First Error Step**: **6** — không phải lỗi *chuỗi* (chain đủ), mà lỗi **chất lượng vị trí entry**: vào ở nửa nông của POI thay vì đợi vùng OTE sâu.
- **Chained fully?**: Yes.

---

## 5. Setup Quality & Confluence

- [x] Bias D1 rõ ràng, không mâu thuẫn H1 — Bullish.
- [x] Giá trong session/Kill Zone — New York.
- [x] Có Liquidity Sweep trước entry — quét CE FVG H1.
- [x] Có Displacement rõ ràng — nhịp bật tạo FVG M5.
- [x] Có MSS hợp lệ — nhưng trên **tap nông** (giảm độ tin cậy).
- [x] FVG nằm trong Discount (buy) — dưới EQ 1.70956.
- [ ] **Entry nằm trong OTE (0.618–0.786)** — **KHÔNG**: entry 1.70837 ở giữa 0.5 và 0.618.
- [ ] **SL có biên an toàn hợp lý** — chỉ ~1.5 pip trên vùng bị quét → **sống sót nhờ may nhiều hơn thiết kế**.
- [x] RR ≥ 1:2 — 2.33.

| # | Confluence | +1? |
|---|---|---|
| 1 | POI rank ≥ 3 | Có (rank 3) |
| 2 | CE FVG trùng OTE 62–79% | Có (CE 1.70712 sát 0.618) |
| 3 | SMT divergence | Không đánh giá |
| 4 | CISD xác nhận | Không |
| 5 | Macro time | Chưa đánh giá |
| 6 | NWOG/NDOG | Không |
| 7 | SD target align | Không |
| 8 | Inducement bị quét trước POI | Có (giá quét CE FVG trước khi shift) |

- **Score**: **3/8**.

---

## 6. Phân tích sau lệnh (Replay)

**Result**: Win — hit TP 1.71444, RR 2.33.

### Tại sao lệnh thắng (root cause thật)
Bias HTF đúng và POI H1 nằm đúng phía discount — nên **hướng lệnh và vùng vào đều đúng**. Lệnh thắng vì **luận điểm gốc đúng**, KHÔNG phải vì thời điểm entry tối ưu. Cần tách bạch: *đúng hướng* (thực lực) và *đúng vị trí* (chưa đạt) là hai chuyện khác nhau.

### Vấn đề thật cần mổ xẻ: vì sao giá còn quét xuống cạnh dưới FVG sau khi đã có MSS?
Ba cách diễn giải bổ trợ nhau:

1. **FVG bị EQ/OTE cắt đôi.** Entry của bạn (1.70837) nằm ở **nửa nông** (giữa 0.5 và 0.618) — vùng discount kỹ thuật nhưng *chưa phải nơi smart money nạp lệnh lớn*. Thị trường có xu hướng **rebalance TOÀN BỘ** imbalance, tức kéo xuống tận cạnh dưới FVG (0.705) trước khi expansion.
2. **Thanh khoản nằm dưới.** Dưới cạnh dưới FVG / quanh 0.705 là pool sell-stops (equal lows + stop của những long vào sớm — trong đó có chính lệnh của bạn). Algo cần quét sạch pool này trước khi đẩy lên. MSS M5 đầu tiên tạo ra một cụm long → stop của họ trở thành thanh khoản cho cú quét thứ hai.
3. **MSS M5 sớm = có thể là LTF inducement.** MSS xuất hiện sau cú tap nông không đảm bảo HTF POI đã xong việc. MSS "thật đáng tin" là MSS xuất hiện *sau khi giá đã chạm vùng sweet spot*, không phải ngay lần chạm mép trên POI.

### "Giả sử giá đi luôn tại FVG tôi entry thì sao?"
Thì bạn vẫn thắng — nhưng với **RR thấp hơn (2.33)** so với entry sweet spot (~5.0). Vấn đề là: **bạn không thể biết trước** giá sẽ đi luôn hay quét sâu thêm. Đây là đánh đổi cốt lõi:
- **Vào nông (như lần này)**: bắt được nhiều lệnh hơn (không sợ miss), nhưng RR thấp hơn và **rủi ro bị quét SL cao hơn** — lần này SL sống sót trong gang tấc.
- **Đợi sweet spot (0.618–0.705)**: RR cao hơn, SL ngắn hơn, tin cậy hơn — nhưng **thỉnh thoảng miss** những lệnh chạy luôn không quay lại.

Câu trả lời đúng đắn KHÔNG phải "luôn đợi OTE sâu" từ một lệnh này — mà là **để backtest quyết định**: gắn field phân loại độ sâu entry, chạy vài chục mẫu, so expectancy hai kiểu.

### Entry của tôi: hợp lệ nhưng chưa tối ưu, hay sai?
**Hợp lệ nhưng chưa tối ưu vị trí** — không phải sai. Quy trình đúng (bias → POI discount → sweep → MSS → FVG entry), nhưng vào ở **nửa nông** khi POI H1 còn "nợ" một nhịp quét xuống OTE sâu.

### Nếu vào lại, làm gì khác?
- Khi FVG H1 trải EQ → OTE: **ưu tiên đặt entry ở nửa OTE (0.618 → 0.705)**, không vào ở nửa trên EQ–0.618.
- Hoặc **chia lệnh (scale-in)**: 1/2 tại CE FVG H1, 1/2 tại 0.705 — trung hòa rủi ro miss vs rủi ro quét sâu.
- Chỉ tin MSS M5 **sau khi giá đã chạm vùng sweet spot**, không tin MSS trên tap nông.
- Đặt SL dựa trên **cạnh dưới thật của FVG H1 + buffer** ngay từ đầu (bạn đã làm đúng SL 1.70576) — chứ không dựa trên cấu trúc M5 nông.

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Lệnh thắng nhờ **đúng bias + đúng POI discount**, nhưng entry vào **nửa nông của FVG (giữa 0.5–0.618)** thay vì OTE sweet spot → RR chỉ 2.33 (đáng lẽ ~5) và SL suýt bị quét — thắng nhưng chưa tối ưu.

> [!warning] Ghi chú của mentor
> "Process over outcome": **kết quả Win che giấu một lỗi vị trí entry thật**. Đừng để cú thắng này củng cố thói quen vào lệnh ở nửa nông của POI. Cú quét xuống cạnh dưới FVG là *dự đoán được* (FVG trải EQ→OTE + thanh khoản dưới), không phải xui rủi.

### 7.1. Bài học kỹ thuật
- **FVG trải EQ → OTE = FVG hai nửa xác suất.** Nửa trên (EQ–0.618) là bẫy vào sớm; nửa dưới (0.618–0.705) mới là vùng tài trợ. Luôn xác định FVG rơi vào đâu trong OTE trước khi chọn điểm vào.
- **MSS trên tap nông = MSS sớm**, có thể là LTF inducement. Đợi giá chạm sweet spot rồi mới tin shift.
- **SL sống sót ≠ SL được thiết kế tốt.** Biên 1.5 pip là may. Nếu quét sâu thêm 2 pip là -1R.

### 7.2. Pattern lặp lại (cần theo dõi)
- **Vào lệnh ở nửa nông của POI khi POI trải EQ→OTE** — kiểm tra các backtest khác trong `04 - Backtesting/` xem đã lặp mấy lần. Nếu ≥3 lần → tạo `06 - Mistake Database/Mistake - Entry nông nửa trên POI (chưa vào OTE).md`.
- **Sai số học khi tính CE/EQ** (CE ghi 1.70771 vs 1.70712) — lỗi data hygiene, dễ dẫn tới đánh giá vị trí sai. Luôn tính lại CE = (high+low)/2.

### 7.3. Rule cần thêm/cập nhật vào Playbook
- [ ] Rule: khi FVG POI trải EQ→OTE, **entry ưu tiên vùng 0.618–0.705**; không vào nửa EQ–0.618 trừ khi có confluence mạnh khác.
- [ ] Rule: chỉ vào theo MSS LTF **sau khi giá chạm sweet spot của POI HTF**.
- [ ] Thêm field `entry_in_ote` (Yes/No) và `entry_depth` (nông/sâu) vào schema backtest để lượng hóa.
- [ ] Cân nhắc rule scale-in (½ CE + ½ sweet spot) và backtest so sánh expectancy.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 — D1 Bullish + DOB, draw-on-liquidity thẳng hàng |
| POI Selection (FVG discount, đúng phía) | 8/10 — POI đúng, nhưng FVG trải EQ→OTE cần chọn nửa sâu |
| Liquidity Sweep | 8/10 — quét CE FVG (internal) hợp lệ |
| Displacement / MSS quality | 6/10 — MSS thật nhưng trên **tap nông** (sớm) |
| Entry Precision & Location | **5/10** — CE FVG M5 chính xác về kỹ thuật, nhưng **vị trí trong POI quá nông** (chưa vào OTE) |
| Risk Management (RR & SL) | 6/10 — SL logic đúng nhưng **biên 1.5 pip = may**; RR 2.33 bỏ lỡ ~5R |

**Overall Grade**: **B** — lệnh thắng, quy trình đúng hướng, nhưng lỗi **vị trí entry nông** và **SL suýt bị quét** kéo điểm xuống. Đây là cú thắng cần học nhiều hơn một cú thua sạch.

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

> [!important] Xác minh lại premise của brief trước khi so sánh
> Brief mô tả note này là "bản phân tích thứ 2 của CÙNG lệnh GBPUSD 2014-06-25" so với `2026-07-16/02`. Kiểm tra frontmatter: note này có `trade_date: 2014-07-14`, không phải `2014-06-25`. Chính callout đầu file cũng tự thừa nhận: "tên file (`2014-06-25`) không khớp ngày lệnh (`2014-07-14`)" và đề xuất đổi tên nhưng **chưa đổi**. Vậy đây là **hai lệnh GBPUSD Long khác nhau** (cách nhau 19 ngày trong dữ liệu lịch sử 2014), vô tình mang tên file giống hệt do lỗi đặt tên chưa sửa ở note này — không phải cùng một lệnh được backtest hai lần. Phần "self-consistency" theo yêu cầu brief được viết lại bên dưới thành **so sánh rule drift giữa hai lệnh cùng biến thể** (khác với self-consistency thật của 1 lệnh) — bản thân phát hiện này là finding quan trọng nhất của cặp note 2–3.

**Bảng khác biệt đầy đủ giữa 2 bản (mỗi dòng = 1 finding):**

| # | Khía cạnh | Note `2026-07-16/02` (2014-06-25) | Note này `2026-07-17/01` (2014-07-14) | Nhận xét |
|---|---|---|---|---|
| 1 | **Đối tượng thật** | Lệnh GBPUSD Long 2014-06-25 | Lệnh GBPUSD Long 2014-07-14 (filename sai, tự flag) | Đây là root finding — hai note không cùng 1 lệnh |
| 2 | Công cụ xác nhận LTF | CISD (open/close, full-leg reclaim) | MSS (wick-based) | Rule drift: cùng vault, hai biến thể xác nhận khác nhau được áp dụng tùy lệnh, không có tiêu chí chọn trước khi nào dùng CISD/khi nào dùng MSS |
| 3 | Khung đánh giá vị trí POI | Discount/Premium/Equilibrium (không dùng OTE fib, note tự giải thích lý do) | OTE fib 0.618/0.705/0.786 chi tiết | Hai note dùng hai thước đo khác nhau cho cùng khái niệm "vị trí POI trong range" — không so sánh chéo được trực tiếp nếu không quy đổi |
| 4 | Độ sâu tap/entry vào POI | Tap NÔNG vào OB (không chạm CE/low OB) | Entry ở NỬA NÔNG của FVG (giữa EQ 0.5 và 0.618, chưa vào OTE) | Cả hai đều "nông" nhưng note 2 không coi đây là red flag còn note 3 coi đây là **first_error_step (bước 6)** — chuẩn đánh giá "nông" bị áp dụng không nhất quán |
| 5 | `first_error_step` | `none` — lỗi thật (quản lý runner) nằm ngoài 7 bước | `6` — lỗi nằm trong 7 bước, dù kết quả Win | Note này khắt khe hơn với chính khái niệm "lỗi trong chuỗi" so với note kia dù cả hai đều Win và đều "nông" |
| 6 | Xử lý confluence_score thấp | Tự miễn trừ: "không nên đọc điểm số 1/8 là confluence yếu" | Không tự miễn trừ, giữ nguyên 3/8 là điểm thật, dùng để trừ vào Grade | Drift trong triết lý chấm điểm: note 2 bảo vệ điểm thấp, note 3 chấp nhận điểm thấp phản ánh chất lượng thật |
| 7 | Arithmetic RR | `r_planned: 2.47` nhưng tính lại từ entry/SL/TP ra 2.373 (lệch ~0.1R, KHÔNG được note tự phát hiện) | `r_planned: 2.33` được note **tự verify bằng số** và khớp đúng (risk 26.1 pip / reward 60.7 pip = 2.33) | Note này có kỷ luật verify số tốt hơn — có hẳn callout "Các con số đã được kiểm tra lại"; note 2 không có bước verify tương đương và để lọt một sai lệch |
| 8 | Cách trình bày lỗi trong note | Callout `[!warning]` của "mentor" nhấn mạnh không để Win che giấu lỗi runner | Cảnh báo "Điểm chí mạng" ngay trong mục 3, đồng thời có SVG minh họa RR đánh đổi (`GBPUSD-20140714-entry-location.svg`) | Note này có hình ảnh minh họa định lượng (RR 2.33 vs ~5.0), note 2 không có minh họa tương đương cho vấn đề runner |
| 9 | Grade cuối | B+ | B | Chấm điểm khắt khe hơn ở note có lỗi entry nằm trong 7 bước, dù cùng là Win — nhất quán về logic (lỗi trong chuỗi bị phạt nặng hơn lỗi ngoài chuỗi ở quản lý lệnh) nhưng cần nêu rõ đây là 2 tiêu chí phạt khác nhau, không so sánh ngang hàng được |
| 10 | Khuyến nghị rule tương lai | Viết rule quản lý runner (breakeven sau TP1, đóng theo tín hiệu cụ thể) | Viết rule vào entry ưu tiên vùng 0.618–0.705, chỉ tin MSS sau khi giá chạm sweet spot | Hai rule nhắm vào hai giai đoạn khác nhau của trade (exit vs entry) — bổ sung nhau, không mâu thuẫn, nhưng cả hai đều cùng gốc từ hiện tượng "nông" chưa được note nào liên kết thành 1 pattern chung |

**Pattern xuyên hai lệnh chưa được note nào chỉ ra:** cả hai lệnh đều có yếu tố "nông" (tap nông vào OB ở note 2; entry nông trong FVG ở note 3) và cả hai đều **vẫn Win** — nhưng phản ứng đánh giá lại khác nhau (note 2 không phạt, note 3 phạt qua first_error_step + Grade). Đây chính là **rule drift** thật sự: nếu tiêu chí "tap/entry nông = giảm điểm" được áp dụng nhất quán, note 2 lẽ ra phải có ít nhất một dòng trừ điểm tương ứng ở Entry Precision hoặc Liquidity Sweep — hiện tại POI Selection của note 2 chỉ trừ nhẹ (8/10, ghi "tap nông, chưa chạm CE/low OB") trong khi note 3 trừ mạnh hơn nhiều cho hiện tượng tương tự (Entry Precision 5/10, "vị trí trong POI quá nông").

**Bản đồ liquidity IRL↔ERL bổ sung cho lệnh 2014-07-14 (note này).** H1 FVG (1.70833–1.70591) là IRL, trải từ EQ (0.5) tới gần sweet spot OTE (0.705) — nghĩa là bản thân IRL này bị cắt làm 2 nửa xác suất khác nhau (note gốc đã tự phân tích rất kỹ ở mục 6, không lặp lại ở đây). Điểm bổ sung: SSL/ERL gần nhất phía dưới không được note xác định rõ (không có mức giá cụ thể cho "range low" của D1/H1 rộng hơn EQ 1.70074–1.71838) — nếu ERL đó cũng chưa bị quét tại thời điểm MSS M5 xuất hiện (giống hệt cơ chế Loss ở note 4: [[02 - Loss - GBPUSD - 2014-07-17 - Long]]), thì "MSS sớm" ở đây có thể mang cùng bản chất rủi ro, chỉ khác là lần này giá không tiếp tục quét xuyên qua SL. Note gốc mục 6 đã tự nhận diện đúng cơ chế MSS sớm nhưng không đối chiếu với ERL cấu trúc rộng hơn — khoảng trống phân tích giống hệt note 4 nhưng ở đây may mắn không trả giá.

**So sánh với note 4 (Loss cùng batch).** Cùng dùng khung OTE fib + FVG POI + MSS wick, cùng hiện tượng "MSS sớm trên tap/entry nông" — khác biệt duy nhất về outcome là note 3 (win) giá không quét tiếp xuống sâu hơn còn note 4 (loss) giá quét xuyên toàn bộ range. Đây là bằng chứng ủng hộ giả thuyết ở note 4 mục 9 rằng "MSS sớm" là một họ rủi ro thật (không phải chỉ 1 lần thua ngẫu nhiên) — vì cùng cơ chế xuất hiện ở cả 1 Win (nhẹ, may mắn không bị quét sâu) và 1 Loss (nặng, quét xuyên range). Tăng thêm 1 điểm dữ liệu cho pattern "MSS sớm" nhưng vẫn chưa đủ mẫu để thành rule cứng (n=2 nếu tính cả note 3 và note 4).

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
type: devils-advocate
mode: REVIEW
instrument: GBPUSD
date: 2014-07-14
timeframes_provided: [D1, H1, M5] (mô tả + số liệu đã verify bằng lời, ảnh PNG không đọc được)
verdict: SURVIVES, WEAKENED
evidence_sufficiency: partial
opposite_case_strength: equally viable
objections: {fatal: 0, material: 3, minor: 2}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN, O5 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base.** Ảnh PNG không đọc được, nhưng note này có mức verify số liệu cao hơn 2 note kia (callout riêng "Các con số đã được kiểm tra lại" với CE/EQ/OTE tính sẵn) — nâng `evidence_sufficiency` lên `partial` thay vì `thin`, vì phần load-bearing (vị trí entry trong OTE) được xác lập bằng arithmetic độc lập với ảnh, không chỉ bằng mô tả định tính.

**1. Thesis + load-bearing claim.**
- C1: HTF bias Bullish (D1 HH/HL + DOB) — mô tả định tính.
- C2: H1 FVG (1.70833–1.70591) là POI Discount hợp lệ, CE = 1.70712 (verify khớp).
- C3: FVG bị cắt bởi EQ/OTE thành 2 nửa — nửa trên (EQ–0.618) là "bẫy", nửa dưới (0.618–0.705) là "vùng tài trợ thật" (**load-bearing** — toàn bộ lesson và grade B dựa trên phân loại 2 nửa này).
- C4: Entry 1.70837 nằm ở nửa trên (nông) → first_error_step = 6, dù chuỗi 7 bước "chained fully".
- C5: MSS M5 xuất hiện trên tap nông = "MSS sớm", có thể là LTF inducement.
- Inference: C2+C3 → C4 (định vị lỗi); C3+C5 → giải thích tại sao giá quét tiếp xuống sau entry.

**2. Điều gì survive.** Việc tự phát hiện và verify lại 2 lỗi số (CE FVG 1.70771→1.70712, EQ 1.70964→1.70956) là kỷ luật số liệu tốt nhất trong cả 3 note win đã xem ở batch này. Phân loại "FVG bị EQ/OTE cắt 2 nửa xác suất" là một khung khái niệm rõ ràng, nhất quán nội bộ, và tự thừa nhận không nên khái quát hóa vội ("để backtest quyết định... chạy vài chục mẫu").

**3. Objections.**

**O1 · [METHOD] · fatal · attacks C3**
Claim: "Nửa trên (EQ–0.618) không phải nơi smart money nạp lệnh; nửa dưới (0.618–0.705) mới là vùng hội tụ."
Fails: Đây là một phân loại nhị phân được **rút ra sau khi biết** giá quét tiếp xuống nửa dưới rồi mới đảo chiều lên — nếu giá đã chạy thẳng từ nửa trên mà không quét thêm (khả năng hoàn toàn có thể xảy ra, note tự thừa nhận ở phần "Giả sử giá đi luôn tại FVG tôi entry thì sao?"), khung phân loại 2 nửa này liệu có được viết lại thành "cả 2 nửa đều hợp lệ, entry nông cũng ổn"? Đây chính là outcome-as-evidence-cho-process mà mode REVIEW với lệnh Win phải săn theo brief.
Consequence: Nếu C3 chỉ là mô tả hậu-kiểm chứ không phải quy luật xác lập trước, thì "first_error_step = 6" (bước 6 sai vì vào nửa nông) là một phán quyết được đưa ra *biết trước kết quả rằng giá đã quét thêm* — một dạng hindsight tinh vi hơn: không phải "biết TP sẽ đạt" mà là "biết đường đi cụ thể của giá sau entry" để phân loại lại chất lượng của chính quyết định entry.
Your best answer: Note tự trả lời khá tốt ở đoạn "Câu trả lời đúng đắn KHÔNG phải 'luôn đợi OTE sâu' từ một lệnh này — mà là để backtest quyết định" — nghĩa là tác giả *đã* nhận thức được giới hạn n=1, nhưng vẫn dùng chính n=1 đó để gán `first_error_step: 6` và trừ điểm Entry Precision xuống 5/10 trong bảng Final Grade — hai hành động này không nhất quán với sự thận trọng đã tuyên bố.
Retracted by: Không thể — đây là giới hạn cấu trúc của backtest đơn lẻ. Chỉ giảm nhẹ (không xóa) khi có ≥15 mẫu FVG-trải-EQ-OTE để xác nhận nửa nông thực sự có win rate/expectancy thấp hơn nửa sâu.

**O2 · [SELF-CONTRADICTION] · material · attacks C4**
Claim: `chained_fully: Yes` (mục 4) đồng thời với `first_error_step: 6`.
Evidence: Note tự giải thích đây "không phải lỗi chuỗi... mà lỗi chất lượng vị trí entry" — về mặt khái niệm hợp lý, nhưng tạo ra một mâu thuẫn hình thức trong chính schema: nếu bước 6 có lỗi (`step6_entry_ok: Partial`) thì theo định nghĩa 7-step, chuỗi không thể vừa "đủ" vừa "có lỗi ở giữa" cùng lúc trừ khi template phân biệt rõ "lỗi chất lượng" và "lỗi thiếu bước" — điều mà note không làm rõ bằng field riêng.
Consequence: Dashboard tổng hợp dùng `chained_fully` để lọc "setup hoàn chỉnh" có thể vô tình gộp chung các lệnh có lỗi chất lượng entry vào nhóm "chuỗi đủ, không lỗi" nếu chỉ đọc field đó mà bỏ qua `first_error_step`.
Your best answer: Đây là hạn chế của template hai-field (chained_fully + first_error_step) không phải lỗi lý luận của tác giả — nhưng vẫn là một khoảng xám cần chuẩn hóa.
Retracted by: Thêm field `error_type: chain-break | quality-flaw | none` để tách rõ hai loại lỗi.

**O3 · [ARITHMETIC] · minor**
Đã verify: CE FVG H1 = (1.70833+1.70591)/2 = 1.70712 (khớp số đã sửa trong note, không khớp số gốc sai 1.70771 — note đã tự sửa đúng). EQ = (1.70074+1.71838)/2 = 1.70956 (khớp). RR = |1.71444−1.70837|/|1.70837−1.70576| = 2.326 ≈ 2.33 (khớp, sai số làm tròn không đáng kể).
Retracted by: n/a — mọi con số khớp, ghi nhận đây là note có chất lượng arithmetic tốt nhất trong 3 note win của batch.

**O4 · [UNSUPPORTED] · material · attacks C1**
Claim: "cấu trúc D1 tạo HH/HL liên tục; nhịp expansion tăng mạnh có displacement rõ, kèm DOB."
Evidence: Không có OHLC hay ảnh đọc được để xác nhận "DOB" (Displacement Order Block) — khái niệm này không nằm trong bảng định nghĩa nhanh của SKILL.md ict-doctrine, nên không thể kiểm tra tiêu chuẩn.
Consequence: Nếu DOB không đúng chuẩn OB gốc (nến gây imbalance + phá structure), C1 vẫn có thể đúng về bias nhưng "DOB xác nhận" là một khẳng định thừa không kiểm chứng được.
Retracted by: Cung cấp OHLC/ảnh D1 và định nghĩa DOB được dùng.

**O5 · [UNSUPPORTED] · minor**
Callout đánh giá D1 ghi "Chính xác và đầy đủ. Không thiếu gì ở khung này" — một khẳng định mạnh không kèm tiêu chí cụ thể nào được liệt kê để đo "đầy đủ".
Retracted by: Checklist các mục D1 bắt buộc và xác nhận từng mục đã đạt.

Bộ lọc: 7 objection nháp, cắt 2 (một về "session không có timestamp entry rõ", một về "không có SMT confirm" — cả hai không đổi kết luận, hạ xuống minor rồi bị cắt vì trùng lặp với O4/O5) → còn 5.

**4. Opposite case.** Đọc ngược cùng evidence: FVG không hề "bị cắt 2 nửa xác suất" — toàn bộ FVG (1.70833–1.70591) là một vùng tài trợ đồng nhất, và cú quét xuống cạnh dưới sau entry chỉ là biến động nhiễu bình thường trong biên độ POI, không phải bằng chứng cho một quy luật "nửa trên là bẫy". Theo case này, entry tại 1.70837 hoàn toàn hợp lệ và "may mắn" duy nhất là RR thấp hơn tối đa có thể đạt (2.33 thay vì ~5.0), không phải rủi ro bị quét SL cao hơn như note gốc khẳng định — vì SL vẫn đặt dưới toàn bộ FVG, không phụ thuộc vào entry nằm ở nửa nào. Tự phản biện case ngược: nó không giải thích được tại sao SL sống sót chỉ với biên 1.5 pip (theo mục 6 note gốc) — nếu FVG đồng nhất, không có lý do đặc biệt để giá test sát biên dưới đến vậy trước khi đảo chiều; case gốc (2 nửa xác suất) giải thích hiện tượng "test sát biên" tự nhiên hơn (giá cần lấy thanh khoản pool dưới trước). Nhãn: **equally viable** — cả hai case đều giải thích được outcome (Win), khác nhau ở việc case gốc giải thích tốt hơn *tại sao* SL suýt bị chạm còn case ngược đơn giản hơn nhưng bỏ sót chi tiết đó. Observable phân biệt: nếu backtest ≥15 mẫu FVG trải EQ→OTE cho thấy entry nửa trên có tỷ lệ "test gần SL" cao hơn rõ rệt so với entry nửa dưới, case gốc thắng; nếu tỷ lệ tương đương, case ngược (FVG đồng nhất) thắng.

**5. Verdict: SURVIVES, WEAKENED.** Load-bearing claim C3 (FVG 2 nửa xác suất) không bị BROKEN bởi chart hay doctrine, nhưng O1 (method, fatal) cho thấy nó được xác lập theo cách khó tách khỏi việc đã biết đường đi thực tế của giá sau entry — đây là lỗ hổng phương pháp thật sự làm giảm độ tin cậy của phán quyết "first_error_step = 6", dù không phá được toàn bộ thesis (bias, POI, entry mechanics vẫn đúng chuẩn). Điều tôi không phá được: arithmetic (O3 xác nhận mọi số đúng) và chuỗi entry cơ học. Điều critique này không xác lập: rằng khung "FVG 2 nửa xác suất" là sai — chỉ là chưa đủ mẫu để tách nó khỏi khả năng là một cách kể chuyện hậu-kiểm hợp lý.

**6. Falsification tests.**
1. Backtest ≥15 mẫu FVG H1 trải EQ→OTE (như cấu trúc note này); phân loại entry ở nửa EQ–0.618 so với nửa 0.618–0.705; so sánh (a) tỷ lệ giá quét gần SL trước khi đạt TP, và (b) win rate/expectancy hai nhóm. Nếu nhóm nửa trên có tỷ lệ test-gần-SL cao hơn rõ rệt VÀ expectancy thấp hơn, đóng O1 (giữ C3); nếu không khác biệt, C3 bị hạ xuống UNSUPPORTED.
2. Đối chiếu chéo với note 4 ([[02 - Loss - GBPUSD - 2014-07-17 - Long]]) và tìm thêm ≥5 mẫu "MSS trên tap/entry nông" khác trong vault — đo tỷ lệ Win/Loss của riêng nhóm "MSS sớm" để tách khỏi n=2 hiện tại (note 3 + note 4).
3. Thêm field `error_type` (chain-break/quality-flaw/none) vào schema và áp dụng hồi tố cho toàn vault — kiểm tra xem có bao nhiêu note khác cũng có mâu thuẫn hình thức `chained_fully=Yes` + `first_error_step≠none` như O2 nêu.

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Chuỗi Bias(Bullish D1) → Discount FVG POI(H1, trải EQ→OTE) → Sweep(quét CE FVG H1) → MSS+Displacement(M5) → FVG entry là một setup Long hợp lệ, nhưng vị trí entry (nửa trên FVG) là điểm yếu chất lượng.

**Cần sửa** (load-bearing trước):
- C3 (FVG "2 nửa xác suất", nửa dưới mới là vùng tài trợ thật) — **AMBIGUOUS** · why: SKILL.md § FVG chỉ định nghĩa FVG là "sản phẩm của displacement leg + imbalance thật (3-candle)", không phân biệt "nửa nào trong FVG đáng tin hơn" khi FVG trải qua nhiều mức OTE — đây là doctrine gap thật (không phải lỗi tác giả) → không tự chế chuẩn khắt khe hơn canon để FAIL claim này; giữ AMBIGUOUS và đề xuất bổ sung doctrine.
- C5 (MSS trên tap nông = "MSS sớm"/LTF inducement) — **UNSUPPORTED** · why: SKILL.md § MSS yêu cầu "phá swing ngược short-term move, thường sau sweep + displacement" — note không cung cấp OHLC M5 để xác nhận MSS này có body close hợp lệ hay chỉ là wick → fix: đính kèm ảnh/OHLC M5 quanh 21:50.
- C1 (D1 HH/HL + DOB) — **UNSUPPORTED** · why: không có OHLC D1 → fix: cung cấp số liệu.

**PASS:** C2 (CE FVG H1 = 1.70712, EQ = 1.70956, OTE 0.618/0.705/0.786 đều verify khớp arithmetic — đây là note có PASS arithmetic tốt nhất batch), C4-phần-cơ-học (entry đúng CE của FVG M5, không đua giá — retrace logic hợp lệ theo doctrine, độc lập với việc CE đó nằm ở nửa nào của H1 FVG).

**Verdict: PARTIALLY ALIGNED** — load-bearing claim C3 rơi vào AMBIGUOUS (doctrine gap, không phải FAIL), C1/C5 UNSUPPORTED vì thiếu chart, nhưng C2 (arithmetic nền tảng) và phần cơ học của C4 đều PASS vững chắc. Không có FAIL trực tiếp nào (không gọi sai tên hiện tượng) nên không rơi xuống NOT ALIGNED.

**Notes:** Doctrine drift giữa case 2 và case này (batch-level finding): note `2026-07-16/02` dùng khung Discount/Premium/Equilibrium thuần túy (không OTE fib) để đánh giá vị trí POI, còn note này dùng khung OTE fib chi tiết cho cùng loại đánh giá — cả hai cách đều nằm trong doctrine (không mâu thuẫn định nghĩa gốc), nhưng người dùng áp dụng hai chuẩn đo khác nhau cho cùng một loại quyết định (đánh giá "độ sâu"/"độ đẹp" của vị trí entry trong POI) tùy theo note, không có tiêu chí chọn trước khi nào dùng chuẩn nào — đây là drift cấp phương pháp cần chuẩn hóa trong Playbook, không phải lỗi doctrine của từng note riêng lẻ.

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật
1. **FVG trải qua nhiều mức OTE cần được chia nhỏ trước khi chọn entry.** Ví dụ số thật: FVG H1 1.70833–1.70591 trải từ EQ (1.70956, thực ra FVG nằm dưới EQ) qua 0.618 (1.70748) tới gần 0.705 (1.70594) — cạnh trên FVG (1.70833) nằm giữa EQ và 0.618 (nửa nông), cạnh dưới (1.70591) gần 0.705 (nửa sâu). Tổng quát hóa: khi POI HTF trải nhiều mức fib, xác định trước nửa nào là ưu tiên trước khi retrace xảy ra, không phải sau khi thấy entry nào khớp CE M5.
2. **Verify số bằng công thức, không tin số ghi tay.** Ví dụ số thật: CE FVG ghi tay là 1.70771, tính lại đúng là 1.70712 — lệch 6 pip, đủ để đổi phân loại "entry có nằm trong OTE hay không". Tổng quát hóa: mọi CE, EQ, OTE phải được tính lại bằng công thức trước khi dùng để phân loại chất lượng entry.
3. **`chained_fully: Yes` và `first_error_step ≠ none` có thể cùng đúng nếu phân biệt rõ lỗi thiếu-bước và lỗi chất-lượng-bước** (xem O2 Devil's Advocate) — nhưng schema hiện tại không có field tách biệt, dễ gây hiểu lầm khi đọc dashboard.

### (b) Bài học quy trình/checklist
- Note này có callout riêng "Các con số đã được kiểm tra lại" — nên chuẩn hóa thành bước bắt buộc cho MỌI note trong vault, không chỉ note này (note 2 batch này thiếu bước này và để lọt sai lệch RR).
- Thiếu tiêu chí viết trước để chọn khung đánh giá vị trí POI (Discount/Premium thuần vs OTE fib chi tiết) — hiện đang chọn tùy note, gây khó so sánh chéo giữa các lệnh.

### (c) Bài học tâm lý-hành vi
- Nguy cơ lớn nhất của chính note này: dùng đường đi cụ thể của giá SAU entry (quét xuống nửa dưới rồi mới lên) để đóng khung lại "entry của tôi ở nửa nông là sai" — trong khi tại thời điểm entry, không có gì đảm bảo giá sẽ quét thêm hay chạy thẳng (note tự thừa nhận). Đây là dạng hindsight tinh vi: không nói "tôi biết TP sẽ đạt" mà nói "tôi biết cần đợi vùng sâu hơn" — cả hai đều dùng thông tin chỉ có sau entry.
- Tuy nhiên cần công nhận: note đã tự nhận thức rất rõ giới hạn này ("để backtest quyết định... không phải luôn đợi OTE sâu từ một lệnh này") — mức độ tự nhận thức cao hơn hẳn note 2, dù hành động cụ thể (gán first_error_step=6, trừ điểm) vẫn chưa hoàn toàn nhất quán với nhận thức đó.

### (d) Rule đề xuất cho Playbook
- [ ] Khi FVG/POI HTF trải nhiều mức OTE, xác định TRƯỚC (không phải sau khi entry) mức fib mục tiêu ưu tiên cho entry — ghi vào kế hoạch trước khi giá retrace tới.
- [ ] Bắt buộc mọi note có CE/EQ/OTE phải kèm callout verify bằng công thức, đối chiếu số ghi tay vs số tính lại.
- [ ] Chuẩn hóa MỘT khung đánh giá vị trí POI cho toàn vault (đề xuất: luôn dùng OTE fib chi tiết làm chuẩn chính, Discount/Premium là phân loại thô bổ sung) — chấm dứt tình trạng note tùy chọn khung đánh giá.
- [ ] Thêm field `error_type` (chain-break/quality-flaw/none) để tách rõ ý nghĩa của `first_error_step` khi `chained_fully = Yes`.

### (e) Điều KHÔNG nên học từ lệnh này (chống overfitting/outcome bias)
- **Không nên** coi "nửa trên FVG là bẫy, nửa dưới là vùng tài trợ thật" là quy luật đã xác lập — đây là cách đọc lại một lệnh SAU KHI biết giá quét xuống nửa dưới rồi mới lên; nếu giá đã chạy thẳng từ nửa trên, khung này rất có thể sẽ không được viết ra.
- **Không nên** dùng RR "nếu vào sweet spot ~5.0" như một con số đã bỏ lỡ chắc chắn — đây là RR **giả định** dựa trên SL ngắn hơn, không phải RR đã từng đạt được thật; nó minh họa đánh đổi lý thuyết, không phải cơ hội bị bỏ lỡ đã được chứng minh.
- **Không nên** dùng lệnh Win + SL "sống sót trong gang tấc" (1.5 pip) để kết luận toàn bộ setup là hợp lệ — note gốc đã đúng khi tự cảnh báo "SL sống sót ≠ SL được thiết kế tốt", giữ nguyên quan điểm đó.

---

### Liên kết bổ sung
- Filename thật nên là: `02 - Win - GBPUSD - 2014-07-14 - Long.md` (xem callout đầu file) — KHÔNG đổi trong batch này theo đúng ràng buộc "không sửa/xóa", chỉ ghi nhận lại.
- So sánh rule drift đầy đủ: [[02 - Win - GBPUSD - 2014-06-25 - Long]] (lệnh khác, 2014-06-25, dùng CISD/BPR + khung Discount-Premium) — xem bảng 10 mục ở phần 9 phía trên.
- Cùng họ "MSS sớm": [[02 - Loss - GBPUSD - 2014-07-17 - Long]] (n=2 cho pattern MSS-trên-tap-nông, một Win một Loss).

![[GBPUSD-driftcompare-020714-vs-020625.svg|760]]

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- Khái niệm: [[13-FVG-Fair-Value-Gap|FVG]] · [[10-Consequent-Encroachment-Mean-Threshold|Consequent Encroachment]] · [[21-Market-Structure-Shift|MSS]] · [[20-Liquidity-Sweep|Liquidity Sweep]] · [[27-Premium-Discount|Premium Discount]] · [[12-Dealing-Range|Dealing Range]] · [[18-Kill-Zones|Kill Zones]]
- Dashboard: [[_Backtest Dashboard]]
- Template: [[Backtest template - POI & Step Decision (ICT 2022)]]
- Mistake liên quan: *(đề xuất mới — xem mục 7.2: "Entry nông nửa trên POI")*
