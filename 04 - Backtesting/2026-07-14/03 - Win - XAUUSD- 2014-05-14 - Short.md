---
type: backtest
backtest_date: 2026-07-14
trade_date: 2014-05-14
symbol: XAUUSD
position: Short
result: Win
session: New York
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: FVG
poi_rank: 1
poi_timeframe: M5
poi_location: Premium
poi_in_ote: Yes
ce_ote_overlap: Yes
poi_stack: H1 FVG (context/OTE) + M5 BPR (2 FVG đối nghịch overlap, entry)
fvg_high: 1307.322
fvg_low: 1306.483
ce_price: 1306.9025
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
sweep_type: External
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
entry_price: 1306.9
stop_loss: 1308.39
take_profit: 1302.477
r_planned: 2.97
rr_if_ce:
rr_if_ote:
r_multiple: 2.97
risk_percent:
spread_cost:
r_net:
grade: A
followed_plan: Yes
confidence:
tags:
  - backtest
  - ICT2022
  - POI
  - BPR
---

# Backtest 2014-05-14 — XAUUSD Short — POI & Step Decision (BPR)

> [!info] Ghi chú chuyển đổi (2026-07-17)
> Chuyển từ template cũ sang **Backtest template - POI & Step Decision**. Toàn bộ phân tích gốc giữ nguyên.
> ⚠️ **Khoảng trống controlled vocabulary**: `poi_type` gốc là "Balance Price Range (BPR)" — nhưng danh sách `poi_type` chuẩn của template mới KHÔNG có BPR (chỉ có Order Block/FVG/Breaker/Rejection Block/iFVG/Unicorn/Mitigation/Hidden OB/Vacuum/Implied FVG/NWOG/NDOG/Liquidity Void). Vì BPR về bản chất là 2 FVG đối nghịch chồng nhau, mình tạm set `poi_type: FVG` và ghi rõ BPR trong `poi_stack`. **Đề xuất**: thêm "Balanced Price Range" vào danh sách `poi_type` chuẩn của template nếu bạn dự định log nhiều mẫu BPR — nếu không sẽ luôn phải "ép" BPR về FVG khi thống kê, làm mất khả năng so sánh riêng BPR vs FVG đơn.
> ⚠️ **Đã sửa `entry_timeframe`**: frontmatter gốc ghi M1, nhưng toàn bộ phân tích (POI, entry, ảnh) đều mô tả BPR và entry trên khung **M5** ("Tôi entry tại vùng CE của BPR M5 này"). Mình đã đổi `entry_timeframe` → M5 cho khớp nội dung — **cần bạn xác nhận đây đúng là M5, không phải lỗi gõ M1→M5 ngược lại**.
> ⚠️ `displacement_score`, `confidence`, `risk_percent`, `spread_cost`, `r_net`, `fill_depth_pct` không có căn cứ số trong bản gốc → để trống.
> `confluence_score = 2` chỉ tính theo 8 mục cố định của template (SMT/CISD/macro time/NWOG.../idm swept). Điểm mạnh thật sự của lệnh này — **2 POI khác timeframe chồng đúng một vùng giá (H1 FVG + M5 BPR)** — được ghi nhận qua `poi_stack`, KHÔNG nằm trong 8 mục confluence cố định. Đừng chỉ nhìn confluence_score=2 mà đánh giá thấp lệnh này; grade A phản ánh đúng chất lượng nested-POI đã phân tích ở mục 7.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | XAUUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5)                                       |
| Trade Date (dữ liệu)      | 2014-05-14                                                   |
| Position                  | Short                                                        |
| Result                    | Win                                                          |
| Session                   | New York                                                     |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | FVG (BPR — 2 FVG overlap, xem ghi chú vocab)                 |
| POI Rank (8.1)            | 1 (FVG đơn — BPR chưa có hạng riêng trên thang)              |
| POI Timeframe             | M5 (bối cảnh H1)                                             |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | none                                                         |
| R Planned (gross)         | 2.97                                                         |
| R Net (sau spread)        | (chưa có dữ liệu)                                            |
| R Multiple (kết quả)      | 2.97                                                         |
| Confluence Score (0–8)    | 2 (xem ghi chú — nested POI không nằm trong 8 mục cố định)   |
| Grade                     | A                                                             |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.

> [!check] Toàn vẹn dữ liệu — đã sửa ở bản gốc (2026-07-14)
> Note tạo bằng cách copy 1 lệnh cũ nên 3 trường số liệu bị sót/sai; đã đối chiếu chart M1 và sửa: Entry 1301.562→1306.90, SL 1304.113→1308.39, TP 1294.173→1302.477, R 2.9→2.97; `trade_date` 2014-05-12→2014-05-14.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish · **Market Condition**: Trending
- **Lý do xác định bias**: (bối cảnh chung cụm backtest XAUUSD 5/2014) sweep lower high → Long Term High → sweep đáy trước đó rồi tăng + Displacement + OB → HH/HL tích tụ thanh khoản đáy → Bearish MSS + Displacement + FVG tại đỉnh → Premium của Dealing Range lớn → Bias Bearish. Giá đang đi ngang nhưng phía dưới vẫn còn nhiều Sell Side Liquidity.
- **Draw on Liquidity**: BSL — D1 DR High 1392.098, Bearish OB 1387.437. SSL — DR Low 1182.661, old lows, OB, H1 DR Low.

![[Pasted image 20260714125908.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Bearish MSS + Displacement sau Long Term High; LH/LL, order flow giảm.
- **Dealing Range**: High 1315.691 (fib 1.0) / Low 1277.416 (fib 0.0) → Premium/OTE.
- **POI chính**: Bearish OB ~0.786 (≈1308–1310) · Bearish FVG H1 (từ nhịp giảm 7/5) nằm trong OTE.
- **Liquidity cần chờ sweep**: đỉnh nhịp tăng 12/05/2014 19:00; vùng FVG (trong Liquidity Void).

### Phân tích

- **Context**: chuỗi sự kiện giống cụm backtest cùng ngày (sweep SSL 2/5 → tăng tạo đỉnh 5/5 → consolidation → Bearish Displacement 7/5 tạo FVG → consolidation 8/5 → sweep đáy 12/5 lúc 17:00 tạo H1 DR Low) → hiện tại giá đang trong Premium.
- **Lệnh**: 12/5/2014 19:00 displacement phá 50% Dealing Range vào Premium; giá retrace về vùng FVG (Liquidity Void 7/5); quét lên trên và qua cạnh trên FVG để lại râu nến dài, đóng nến lại quay vào trong FVG, xuất hiện nến Bearish displacement mạnh → vào M5 quan sát.

![[Pasted image 20260714125755.png]]

### M5 — Xác nhận và điểm vào lệnh

- Nhịp Bullish Displacement 14/05/2014 19:20 phá qua đỉnh FVG H1, để lại FVG M5 từ cú displacement đó.
- Giá đóng nến quay ngược lại bên trong FVG H1, để lại bóng nến dài lên trên (2–3 nến tiếp theo cũng quét lên cạnh trên FVG).
- Sau 2–3 nến, giá tạo 1 nến Bearish displacement mạnh, để lại FVG M5.
- **FVG nhịp tăng trước** và **FVG nhịp giảm này overlap** → hình thành **Balance Price Range (BPR) 1307.322 – 1306.483**.
- Giá retrace về BPR lúc 14/05/2014 20:35, quét lên cạnh trên BPR, đóng nến vào bên trong (râu nến dài) rồi quay trở lại CE. Entry tại CE của BPR M5. SL đặt ngoài cạnh trên FVG khung H1.
- **Entry trigger**: quét cạnh trên FVG + quét 1 swing high lớn trước khi về FVG + sweep nội bộ các đáy khi hình thành MSS. MSS bằng nến Bearish displacement lúc 20:00; displacement lúc 19:20 (Bullish) và 20:00 (Bearish); 2 FVG trùng lắp tạo Bearish BPR M5.
- **Entry reason**: chuỗi Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là FVG H1); FVG nằm giữa 0.705–0.786 (giữa sweet spot và cạnh trên); M5 tạo BPR — confluence mạnh hơn FVG đơn.
- **Invalidation**: giá đóng qua FVG H1.
- **Chờ đủ điều kiện?** Có.

**M5:** ![[Pasted image 20260714125628.png]]
**M1:** ![[Pasted image 20260714125516.png]]

---

## 2. POI Profile

- **POI Type đã dùng**: FVG/BPR (2 FVG đối nghịch chồng nhau, khung M5).
- **POI Rank (8.1)**: 1 (chưa có hạng riêng cho BPR).
- **POI hình thành trên khung**: M5 (bối cảnh H1 FVG).
- **POI nằm ở**: Premium ✓.
- **POI stack**: H1 FVG (OTE 0.705–0.786) + M5 BPR — BPR nằm ngay trên CE của H1 FVG.
- **CE FVG trùng OTE 62–79%?**: Yes.
- **Bounds & CE**: BPR High 1307.322 / Low 1306.483, CE = 1306.9025 (≈ entry thực tế 1306.90 — khớp gần như tuyệt đối).

![[Pasted image 20260714125628.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE
- **Entry Precision**: CE (BPR M5)
- **Limit có khớp?**: Yes
- **Giá đi sâu bao nhiêu vào FVG/BPR?**: không có số đo % cụ thể trong bản gốc
- **RR ghi lại**: r_planned 2.97

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes | `step3_sweep_ok` |
| 4 | Displacement + MSS | Yes | `step4_displacement_ok` |
| 5 | POI (FVG/BPR) | Yes | `step5_poi_ok` |
| 6 | Entry (retrace) | Yes | `step6_entry_ok` |
| 7 | Target | Yes | `step7_target_ok` |

- **First Error Step**: none
- **Missing Step**: none
- **Đủ chuỗi 7 bước?**: Yes

---

## 5. Setup Quality & Confluence

**GATE**: Bias rõ · Sweep trước displacement · Displacement hợp lệ · MSS hợp lệ · FVG sạch + entry retrace · Đúng Premium · SL logic + target rõ + RR ≥ kế hoạch → **PASS**.

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không (rank 1, BPR ngoài thang) | *(suy từ poi_rank)* |
| 2 | CE FVG trùng OTE 62–79% | Có | `ce_ote_overlap` |
| 3 | SMT divergence | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | Không có ghi chú | `cisd_confirm` |
| 5 | Macro time | Chưa đánh giá | `in_macro_time` |
| 6 | NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | SD target align | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Có (sweep swing high trước FVG) | `idm_swept` |

- **Score**: 2/8 theo 8 mục cố định — nhưng **chất lượng thật của lệnh nằm ở nested confluence giữa H1 FVG và M5 BPR**, một dạng confluence mà thang 8 mục hiện chưa đo được trực tiếp. Grade A phản ánh điều này.

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng?**: Kiên nhẫn chờ H1 đồng Bias với D1 (Bearish); chờ M5/M1 confirm Bias; H1 retrace về Premium/OTE; giá quét thanh khoản trên FVG; M5 có BPR, confluence mạnh — BPR nằm ngay trên CE của H1 FVG.
- **Cảnh báo trước có không?**: Có Displacement, có MSS, có BPR M5 cho entry.
- **Setup khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu vào lại, làm gì khác?**: Cần backtest nhiều hơn để hiểu đặc tính XAUUSD (đây mới là lệnh vàng thứ 3, thường trade Nasdaq/EURUSD); ghi lại chính xác điều gì là sweep — thanh khoản thật bị quét là swing high phía trên FVG, không phải "cạnh trên FVG"; kiểm tra buffer SL cho vàng (SL sát ngoài cạnh trên H1 FVG có nguy cơ bị wick quét trong live do spread/slippage vàng lớn).

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Lệnh Grade A chất lượng thật nhờ nested confluence đúng bias (D1 Bearish → H1 Premium/OTE → H1 FVG là POI chính → M5 BPR tại CE làm điểm entry) — điểm cần siết lại là độ chính xác thuật ngữ "sweep" và tính toàn vẹn dữ liệu đã log.

### 7.1. Bài học kỹ thuật

**Root cause (duy nhất)**: Kiên nhẫn chờ giá về đúng POI có nhiều lớp confluence chồng nhau (nested POI) rồi mới entry, thay vì vào ngay ở lớp đầu tiên — bias D1 Bearish → đợi H1 retrace lên Premium/OTE (0.705–0.786) → xác định POI chính là H1 FVG → xuống M5 chờ BPR (overlap 2 FVG ngược chiều) trùng ngay trên CE của H1 FVG → entry tại CE của BPR.

**Triệu chứng tích cực**: chờ H1 đồng bias với D1 trước; chờ giá quét một swing high thật trước khi giảm; entry tại CE, không đua giá ở cạnh ngoài; SL đặt ở vùng invalidation logic; RR ≈2.97 vượt ngưỡng tối thiểu 1:2.

**Cơ chế thị trường**: chuỗi kinh điển Sweep buy-side (quét swing high trong Premium) → Displacement giảm tạo MSS + FVG → retrace về FVG/BPR trong Premium → tiếp diễn xuống draw on liquidity (SSL/FVG dưới). BPR M5 mạnh hơn FVG đơn vì là vùng hai FVG ngược chiều overlap → giá "reject" hai lần cùng vùng.

**Cần xác minh thêm**: "Quét cạnh trên FVG" KHÔNG phải là một liquidity sweep — cạnh FVG không có stop nằm ở đó, thanh khoản thật bị quét là swing high phía trên; đặc tính XAUUSD với SL sát (mới lệnh vàng thứ 3, cần thêm sample để định lượng buffer SL).

### 7.2. Pattern lặp lại

- ✅ **Green pattern**: entry ở giao điểm H1 FVG (POI chính) + M5 BPR tại CE trong vùng Premium/OTE, sau một cú sweep swing high — đánh dấu để so sánh win rate với các mẫu POI đơn lẻ.
- ⚠️ **Watch pattern**: thiếu chính xác về thuật ngữ "sweep" và số liệu nhập log — sai số dữ liệu = "garbage in, garbage out", âm thầm phá giá trị toàn bộ dataset nếu lặp lại.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **Rule thuật ngữ**: chỉ đánh dấu `liquidity_swept: Yes` khi giá quét một swing high/low thật (resting liquidity); râu nến vượt cạnh FVG/OB rồi đóng lại ghi là "return to POI + rejection", KHÔNG tính là sweep.
- [ ] **Rule tách POI**: khi POI chính (H1 FVG) và POI confluence (M5 BPR) khác timeframe, ghi rõ tách biệt — POI chính quyết định invalidation, POI confluence quyết định entry trigger.
- [ ] **Rule XAUUSD**: cần tối thiểu ~20 sample vàng trước khi tin logic SL sát; tạm cộng buffer cho wick/spread khi backtest vàng.
- [ ] **Rule toàn vẹn dữ liệu**: mỗi backtest copy entry/SL/TP/R trực tiếp từ chart, kiểm tra Summary table = frontmatter trước khi lưu.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | (không có điểm chi tiết trong bản gốc) |
| POI Selection (nested H1 FVG + M5 BPR) | cao — root cause chính của win |
| Liquidity Sweep | — |
| Displacement/MSS quality | — |
| Entry Precision & Fill (CE, khớp gần tuyệt đối) | cao |
| Risk Management | — |

**Overall Grade**: **A**

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI: [[13 - FVG  - Fair Value Gap]] · [[03 - Balanced Price Range]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_Backtest Dashboard]]
