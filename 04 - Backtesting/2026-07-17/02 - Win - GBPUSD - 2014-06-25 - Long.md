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

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- Khái niệm: [[13 - FVG  - Fair Value Gap|FVG]] · [[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment]] · [[21 - Market Structure Shift|MSS]] · [[20 - Liquidity Sweep|Liquidity Sweep]] · [[27 - Premium Discount|Premium Discount]] · [[12 - Dealing Range|Dealing Range]] · [[18 - Kill Zones|Kill Zones]]
- Dashboard: [[_Backtest Dashboard]]
- Template: [[Backtest template - POI & Step Decision (ICT 2022)]]
- Mistake liên quan: *(đề xuất mới — xem mục 7.2: "Entry nông nửa trên POI")*
