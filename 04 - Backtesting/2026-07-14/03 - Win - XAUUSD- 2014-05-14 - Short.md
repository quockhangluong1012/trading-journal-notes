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

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

### 9.1. Quan hệ với [[2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short|lệnh Loss cùng ngày (RB, sáng)]]: re-entry, revenge, hay setup độc lập?

Đây là câu hỏi trọng tâm được giao riêng cho cặp lệnh 14/5. Dựng lại timeline bằng chính số liệu hai note:

| Mốc | Lệnh 02 (Loss, RB) | Lệnh 03 (Win, BPR) |
|---|---|---|
| Sweep/setup hình thành | 12/5 19:00 (đỉnh RB) → 14/5 15:00 retrace về RB | 14/5 19:20 Bullish Displacement phá đỉnh FVG H1 → tạo FVG mới |
| Entry | 14/5 17:55 (session London) | 14/5 20:35 (session New York, cách entry lệnh 02 **~2h40** SAU khi đã dính SL) |
| SL hit | có (~ngay sau entry theo mô tả "giá retrace lên chạm lại đáy RB") | không áp dụng (lệnh thắng) |
| POI dùng | H1 Rejection Block (0.618–0.705) | M5 BPR (2 FVG đối nghịch overlap), nằm CAO HƠN — ~1306.483–1307.322, tức ~0.786+ trên cùng H1 Dealing Range (1277.416–1315.691) |
| PD array cấp H1 tham chiếu | Rejection Block (mới học) | H1 FVG (từ nhịp giảm 7/5) — POI mà note 01 (12/5) ĐÃ dùng, không phải khái niệm mới |

**Kết luận về bản chất quan hệ**: Đây **không phải re-entry theo đúng nghĩa cơ học** (re-entry = vào lại đúng cùng một luận điểm/POI sau khi bị quét, kỳ vọng giá quay lại) — hai lệnh dùng hai PD array khác nhau, ở hai vùng giá khác nhau (RB ~1301–1304 vs BPR ~1306–1307, cao hơn RB khoảng 3-5 điểm, gần OB H1 0.786 mà chính lệnh 02 đã cảnh báo "chưa được test"). Về vị trí, entry lệnh 03 (1306.9) nằm rất gần vùng OB H1 (~1304.5-1306) mà lệnh 02 xác định là "POI sâu chưa test" — tức **lệnh 03 vô tình đã làm đúng điều mà lệnh 02 lẽ ra nên chờ** (ưu tiên/chờ test POI sâu hơn trước khi short từ POI nông).

**Không phải revenge trading theo dấu hiệu hành vi cổ điển** (tăng size, giảm tiêu chuẩn setup, vào ngay sau loss không chờ tín hiệu mới): khoảng cách thời gian ~2h40, có chuỗi Sweep→MSS+Displacement+FVG hoàn toàn mới (Bullish Displacement 19:20 → Bearish Displacement 20:00 tạo BPR), risk_percent không có ghi chú tăng so với lệnh 02. Về hình thức, đây đọc như **setup độc lập, tình cờ xảy ra cùng ngày cùng downtrend** — nhưng cần một Devil's Advocate riêng cho khẳng định "độc lập" này (xem mục 10).

**Điểm đáng ngờ nhất về tính độc lập**: cả hai lệnh đều dùng cùng bối cảnh D1/H1 bias (copy gần như nguyên văn đoạn "Lý do xác định bias" — xem cả hai note, câu chữ giống nhau ~90%). Điều này gợi ý phân tích D1/H1 được viết MỘT LẦN cho cả cụm ngày rồi tái dùng, chứ không phải đánh giá lại bias độc lập cho từng lệnh — một dạng anchoring nhẹ giữa các lệnh cùng cụm, dù không sai về bias (bias vẫn đúng ở cả hai).

### 9.2. Bản đồ Liquidity IRL↔ERL tại thời điểm entry

- **Pool đã bị lấy trước entry 20:35**: swing high tạo bởi Bullish Displacement 19:20 (internal, bị quét ngay khi tạo FVG mới); đỉnh FVG H1 gốc (từ nhịp giảm 7/5) — bị "quét lên trên và qua cạnh trên" theo mô tả mục 1, rồi đóng lại vào trong.
- **Pool CHƯA bị lấy khi entry khớp (1306.9)**: OB H1 ~0.786 (1308–1310) vẫn chưa test — SL 1308.39 nằm ngay dưới/trong vùng OB này. Đây là cùng loại rủi ro cấu trúc đã nêu ở lệnh 01 (12/5) và là nguyên nhân thua của lệnh 04 (19/5): SL nằm trên đường đi tới một POI sâu hơn chưa test. Ở đây SL 1308.39 gần trùng biên dưới của OB — tức SL đã được đặt SÁT hơn về phía POI sâu, khác với lệnh 02 (SL nằm giữa hai POI, cách xa OB).
- **SSL mục tiêu (TP 1302.477)**: nằm trong Discount, thuộc draw on liquidity D1 hợp lệ, chưa bị lấy tại thời điểm entry.

### 9.3. Chất lượng Displacement/MSS

- H1: giữ nguyên bối cảnh Bearish MSS + Displacement sau Long Term High — đồng nhất với lệnh 01, 02.
- M5: khác biệt quan trọng so với lệnh 02 — ở đây M5 tạo được ĐỦ hai displacement rõ (Bullish 19:20 tạo FVG, rồi Bearish 20:00 tạo FVG đối nghịch) → BPR là sản phẩm của HAI displacement thật, không phải một displacement + suy diễn. Đây là sự khác biệt cấu trúc thực chất với lệnh 02 (M5 "không tạo FVG rõ") và lệnh 04 (M5 "không tạo displacement/FVG sạch") — hai lệnh Loss trong cụm đều có điểm yếu tại đúng bước này, còn lệnh 03 (Win) đạt chuẩn tại đây.

### 9.4. Yếu tố thời gian

- Entry 20:35 (giờ dữ liệu) — note ghi session "New York", nhất quán với giờ trong ngày. Không có ghi chú Kill Zone cụ thể để xác nhận macro time.
- Tốc độ resolve: không ghi rõ thời gian hit TP.

### 9.5. Vị trí entry trong Dealing Range

- BPR 1307.322–1306.483 tương ứng khoảng 0.712–0.746 trên H1 DR (1277.416–1315.691) — nằm SÂU trong dải OTE thật (0.618–0.786), gần trung tâm sweet spot 0.705 — khác với lệnh 01 (entry ở mép 0.618) và lệnh 02 (RB ở 0.618–0.705, cũng mép ngoài). Đây có thể là yếu tố thật giải thích một phần vì sao lệnh 03 thắng: vị trí entry sâu hơn trong Premium, gần đúng nơi OB H1 0.786 "hút" thanh khoản tới, tức entry gần hơn với POI-mà-giá-thực-sự-hướng-tới.

### 9.6. So sánh với các lệnh cùng mẫu trong vault

- Cùng cụm 4 lệnh XAU liên tiếp: [[2026-07-14/01 - Win - XAUUSD- 2014-05-12- Short|Win 12/5 (FVG rank 1)]], [[2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short|Loss 14/5 sáng (RB)]], **lệnh này (Win 14/5 chiều, BPR)**, [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short|Loss 19/5 (Breaker)]]. Pattern rõ: 2 lệnh Win đều dùng FVG/BPR (khái niệm quen thuộc, không "mới học"), 2 lệnh Loss đều dùng khái niệm mới học lần đầu trong cụm (Rejection Block, Breaker Block) — khớp với nghi vấn "rule drift" được giao trong nhiệm vụ batch (xem mục 10 Devil's Advocate cho phân tích đối kháng đầy đủ).

![[XAUUSD-20140514-reentry-timeline.svg|760]]

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
type: devils-advocate
mode: REVIEW
instrument: XAUUSD
date: 2014-05-14 (chiều/tối, New York)
timeframes_provided: [D1/H4 (mô tả), H1 (mô tả), M5 (mô tả + 2 ảnh), M1 (mô tả + 1 ảnh)]
verdict: SURVIVES, WEAKENED
evidence_sufficiency: thin
opposite_case_strength: weaker but non-trivial
objections: {fatal: 0, material: 2, minor: 2}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base**: Mô tả bằng lời + số liệu frontmatter; ảnh không đọc được. `evidence_sufficiency = thin`.

**1. Thesis + load-bearing claim**: C1 Bias D1/H1 Bearish (kế thừa từ cụm). C2 M5 sweep swing high (Bullish Displacement 19:20) → Bearish Displacement 20:00 tạo MSS + FVG đối nghịch với FVG trước → BPR. C3 Entry tại CE BPR (1306.9), khớp gần tuyệt đối với entry thực (1306.9). C4 (từ C1+C2+C3) toàn bộ chuỗi 7 bước hợp lệ. C5 Đây là setup độc lập với lệnh Loss 02 cùng ngày, không phải revenge/re-entry. **Load-bearing: C2 (chất lượng displacement/BPR) — nếu BPR thực chất chỉ là một FVG đơn được "kể lại" hai lần (không phải hai displacement thật độc lập), grade A và claim "confluence mạnh hơn FVG đơn" (mục 7.1 gốc) sụp.**

**2. What survives**: C1 (bias, nhất quán toàn cụm, không mâu thuẫn). C3 — số học CE khớp entry thực gần như tuyệt đối (1306.9025 vs 1306.9, lệch 0.0025) — mức khớp cao nhất trong toàn bộ 5 note batch này, một tín hiệu tích cực thật về độ chính xác ghi chép.

**3. Objections**

**O1 · [METHOD] · material · attacks C5**
Claim (ngụ ý xuyên suốt note 03): đây là một setup hoàn toàn độc lập với lệnh Loss 02 cùng ngày.
Fails: cả hai note dùng đoạn văn bias D1/H1 gần như giống nhau (xem 9.1) — bias không được tái đánh giá độc lập cho từng lệnh trong ngày, tăng khả năng cùng một khung nhận thức (có thể bị ảnh hưởng bởi việc vừa thua) được mang sang lệnh sau, dù bản thân trigger LTF là mới.
Evidence: so sánh trực tiếp đoạn "Lý do xác định bias" ở note 02 và note 03 — trùng lặp nội dung cao.
Consequence: nếu bias bị "quán tính" từ lệnh trước thay vì đánh giá lại, C1 (bias) tại lệnh 03 có độ tin cậy thấp hơn khi đọc như một quan sát độc lập — dù kết luận bias (Bearish) không đổi.
Your best answer: "Bias D1 không thay đổi trong vài giờ nên tái dùng là hợp lý, không phải bias." Có lý — bias khung lớn không cần đánh giá lại mỗi giờ. Nhưng điều này không loại trừ khả năng chọn POI/entry ở M5-M1 bị ảnh hưởng bởi tâm lý sau loss (ví dụ: chọn một POI "chắc ăn hơn" — quen thuộc FVG/BPR — sau khi vừa thua với một khái niệm lạ RB) — objection giữ material, không fatal, vì không có ghi chú cảm xúc/tâm lý trong note để xác nhận trực tiếp.
Retracted by: một ghi chú tâm lý tại thời điểm gốc (không có trong note) xác nhận trạng thái tinh thần trước lệnh 03, hoặc bằng chứng cho thấy quy trình chọn POI M5 độc lập hoàn toàn với lệnh trước.

**O2 · [UNSUPPORTED] · material · attacks C2 (load-bearing)**
Claim: BPR = "2 FVG đối nghịch chồng nhau" tạo confluence mạnh hơn FVG đơn.
Fails: không có xác nhận rằng FVG nhịp tăng (19:20) và FVG nhịp giảm (20:00) thực sự OVERLAP theo đúng định nghĩa BPR (Balanced Price Range = vùng giao nhau của hai FVG đối nghịch), hay chỉ là hai FVG gần nhau được note tác giả gọi chung là BPR. Số liệu FVG riêng của từng nhịp không được nêu tách bạch (chỉ có số BPR gộp 1307.322–1306.483).
Evidence: mục 1 note "FVG nhịp tăng trước và FVG nhịp giảm này overlap → hình thành BPR" — không có 4 mức giá riêng (high/low của từng FVG) để verify overlap thật.
Consequence: nếu không overlap thật (chỉ là hai FVG liền kề, không giao nhau), "confluence mạnh hơn FVG đơn" là overcall — BPR thực chất chỉ là 1 FVG với một câu chuyện phụ.
Your best answer: đã tự flag ở khoảng trống vocabulary (ghi chú đầu file) rằng BPR bị "ép" về FVG trong controlled vocabulary — đây là dấu hiệu tốt về minh bạch, nhưng KHÔNG trả lời câu hỏi overlap có thật hay không, chỉ nói về vấn đề đặt tên field.
Retracted by: nêu 4 mức giá riêng (FVG tăng: high/low; FVG giảm: high/low) và xác nhận chúng thực sự giao nhau tại 1307.322–1306.483.

**O3 · [DOCTRINE] · minor · attacks C4**
Claim: "sweep cạnh trên FVG" (mục 1) được dùng làm cơ sở cho entry trigger.
Fails: đúng cảnh báo mà chính note 03 tự nêu ở mục 7.1 — "Quét cạnh trên FVG KHÔNG phải là một liquidity sweep — cạnh FVG không có stop nằm ở đó". Note đã tự sửa nhận thức này, objection chỉ xác nhận lại bằng ngôn ngữ DA, không thêm phát hiện.
Retracted by: đã tự nhận trong note gốc — giữ ở minor, không lặp lại nội dung.

**O4 · [ARITHMETIC] · minor · attacks C3**
Kiểm chứng lại: CE BPR = (1307.322+1306.483)/2 = 1306.9025, khớp entry thực 1306.9 (lệch 0.0025, trong biên làm tròn). RR = |1308.39-1306.9|/|1302.477-1306.9| = 1.49/4.423 = 2.968 ≈ r_planned 2.97. Không có lỗi arithmetic.
Retracted by: đã khớp, đóng ngay.

Drafted: 4. Cut: 1 (một nghi vấn về việc SL 1308.39 có thực nằm dưới OB hay đã chồng lên biên dưới OB — bị cắt vì không đủ số liệu OB range chính xác trong note 03, trong khi note 04 cùng cụm đã có ước tính OB ~1304.5-1306 áp dụng cho lệnh khác; dùng số đó suy sang đây là ngoại suy quá xa, không phải evidence trực tiếp của note 03).

**4. Opposite case (cùng evidence)**: Đọc ngược C5 — đây KHÔNG phải setup độc lập mà là "size-down revenge" tinh vi: sau thua ở một khái niệm mới lạ (RB), tác giả lùi về vùng giá AN TOÀN hơn về tâm lý (quen thuộc: FVG/BPR, gần với đúng loại POI đã thắng ở lệnh 01), tại đúng nơi mà lý thuyết cụm đã cảnh báo (OB 0.786 chưa test) — tức lệnh 03 "tình cờ đúng" vì nó vô thức lùi về gần điểm mà phân tích đã chỉ ra là terminal thật. Tự phản biện case ngược: nó không giải thích được vì sao BPR (một concept CŨNG tương đối mới, dùng lần đầu trong cụm theo ghi chú "mới lệnh vàng thứ 3") lại được chọn "vì quen thuộc" — BPR không hẳn "quen" hơn RB về mức độ mới lạ. **Strength: weaker but non-trivial** — case ngược có logic tâm lý hợp lý (loss aversion khiến trader lùi về gần vùng "chắc ăn" hơn) nhưng thiếu bằng chứng textual trực tiếp (không có ghi chú cảm xúc) và bị yếu bởi việc BPR cũng là concept mới.
Distinguishing observable: nhật ký cảm xúc/ghi chú tâm lý tại thời điểm 14/5 (nếu có ở nơi khác trong vault, ví dụ journal riêng) sẽ phân biệt được hai case; thiếu nó, không thể vượt qua ngưỡng "weaker but non-trivial".

**5. Verdict: SURVIVES, WEAKENED.** Load-bearing claim C2 (chất lượng BPR) không bị BROKEN nhưng O2 là material vì thiếu 4 mức giá riêng để verify overlap thật — điều này làm suy yếu claim "confluence mạnh hơn FVG đơn" xuống mức chưa kiểm chứng được, dù không đủ để đảo verdict. O1 (bias tái dùng, khả năng ảnh hưởng tâm lý sau loss) không đủ evidence để fatal nhưng đặt nghi vấn hợp lý về tính "độc lập tuyệt đối" của C5. `evidence_sufficiency=thin`. Điều DA này KHÔNG chứng minh: rằng nếu tách BPR ra thành hai FVG riêng và test lại logic entry, kết quả entry có đổi hay không.

**6. Falsification tests**:
1. Đối chiếu ảnh M5 gốc (`Pasted image 20260714125628.png`, `20260714125755.png`) để lấy 4 mức giá riêng của hai FVG cấu thành BPR — xác nhận có overlap thật hay không. Đóng O2.
2. Rà toàn vault các cặp lệnh cùng ngày (Win sau Loss hoặc Loss sau Win, cách nhau <6h) — so sánh xem POI được chọn ở lệnh thứ hai có xu hướng "quen thuộc hơn" (rank thấp/khái niệm cũ) so với lệnh đầu không; nếu pattern lặp lại ≥3 lần, O1 chuyển từ giả thuyết cá nhân sang finding cấp vault.
3. Đo % thân FVG BPR nằm trong dải OTE 0.618-0.786 thật (đã ước tính ~0.712–0.746 ở mục 9.5) — xác nhận lại bằng chart H1 gốc.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis**: Short XAUUSD 14/5 chiều/tối, POI là M5 Balanced Price Range (2 FVG đối nghịch overlap), entry tại CE BPR, nằm sâu trong OTE (H1 FVG context).

**Cần sửa** (load-bearing trước):
- C2 "BPR = 2 FVG đối nghịch overlap" — **AMBIGUOUS** (load-bearing) · doctrine gap thật: SKILL.md không có định nghĩa riêng cho BPR (bảng định nghĩa nhanh chỉ có FVG/OB/Breaker/Sweep...), và note gốc tự nhận field `poi_type` chuẩn không có BPR → không thể FAIL hay PASS một khái niệm mà chuẩn tham chiếu hiện có không định nghĩa; fork: nếu BPR = giao của 2 FVG thật (theo định nghĩa SMC phổ biến ngoài canon 2022 gốc) thì cần 4 mức giá xác nhận overlap (chưa có trong note); nếu chỉ cần "2 phản ứng FVG gần nhau" thì claim PASS nhưng khái niệm bị pha loãng khỏi định nghĩa BPR chuẩn.
- C-liên quan "sweep cạnh trên FVG" dùng làm sweep hợp lệ — **FAIL** (đã tự nhận ở mục 7.1 note gốc, không lặp phân tích, chỉ xác nhận trạng thái) · anchor: SKILL.md § Sweep — "không có reference level → UNSUPPORTED"; ở đây note tự nâng thành FAIL vì đã minh bạch tự nhận đây là nhầm lẫn thuật ngữ, không phải chỉ thiếu bằng chứng.

**PASS**: C1 (bias D1/H1, nhất quán với toàn cụm và với note 01/02/04) · C3 (CE = entry, khớp số học gần tuyệt đối) · C4-phần-cơ-học (MSS + Displacement kép M5 đạt chuẩn hình thức theo mô tả, tốt hơn note 02/04 vốn tự nhận M5 yếu).

**Verdict**: **INSUFFICIENT EVIDENCE** — load-bearing claim C2 rơi vào AMBIGUOUS do doctrine gap (BPR không có anchor canon rõ) kết hợp thiếu 4 mức giá riêng để tự verify overlap dù có anchor. Đây không phải NOT ALIGNED (không có FAIL ở load-bearing) nhưng cũng không đủ để DOCTRINE ALIGNED khi khái niệm trung tâm chưa được canon fix.

**Notes**: Doctrine gap được xác nhận lần 2 trong batch này (cùng loại gap đã nêu ở note 01 về ngưỡng tụt khung) — đề xuất bổ sung anchor riêng cho "Balanced Price Range" vào SKILL.md/doctrine.md: định nghĩa = giao hình học của 2 FVG đối nghịch liên tiếp, với yêu cầu evidence bar là 4 mức giá (high/low mỗi FVG) chứng minh chúng thực sự overlap, không chỉ liền kề.

---

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật

1. **BPR chỉ có giá trị confluence THẬT nếu 4 mức giá cấu thành nó được ghi tách bạch — gộp thành một cặp high/low duy nhất xóa mất khả năng verify overlap.** Ví dụ số thật: note chỉ ghi `fvg_high: 1307.322 / fvg_low: 1306.483` cho "BPR", không có số riêng của FVG tăng và FVG giảm. Tổng quát: mọi POI ghép (BPR, nested OB+FVG) cần lưu ĐỦ thành phần, không chỉ kết quả gộp.
2. **Vị trí entry trong dải OTE (không chỉ chạm biên) có thể là biến số phân biệt Win/Loss thật trong cụm này.** Ví dụ số thật: entry lệnh 03 ở ~0.712-0.746 (giữa sweet spot) trong khi lệnh 01 ở ~0.618 (mép) — cả hai đều thắng nhưng lệnh 03 gần hơn với vùng OB 0.786 mà giá thực sự hướng tới. Tổng quát hóa: khi có PD array sâu hơn (OB) chưa test, entry gần nó hơn (trong giới hạn OTE) có thể giảm rủi ro SL nằm trên đường thanh khoản dẫn tới POI đó — cần thêm mẫu để kiểm giả thuyết này (n hiện tại quá nhỏ).

### (b) Bài học quy trình/checklist

3. **Khi ghi log nhiều lệnh cùng ngày, tái sử dụng đoạn bias D1/H1 là hợp lý (bias không đổi theo giờ) — nhưng cần đánh dấu RÕ đó là bias kế thừa, không phải đánh giá lại, để tránh đọc nhầm thành 2 lần xác nhận độc lập.** Rule: thêm dòng "Bias kế thừa từ lệnh [[...]], không đánh giá lại" khi áp dụng.

### (c) Bài học tâm lý-hành vi

4. **Không có ghi chú tâm lý tại các thời điểm quan trọng (ngay sau một lệnh Loss, trước khi vào lệnh tiếp theo cùng ngày) là một lỗ hổng dữ liệu, không chỉ lỗi kỹ thuật.** Không thể loại trừ hoàn toàn giả thuyết "lùi về vùng quen thuộc sau thua" (xem Opposite case, mục 10) nếu không có ghi chú trạng thái tinh thần — điều này KHÔNG đồng nghĩa giả thuyết đó đúng, nhưng thiếu dữ liệu để bác nó dứt điểm.

### (d) Rule đề xuất cho Playbook

- [ ] **R-BD-07**: Với POI ghép (BPR, nested stack), luôn ghi 4 mức giá cấu thành riêng biệt trước khi ghi số gộp.
- [ ] **R-BD-08**: Khi log ≥2 lệnh cùng ngày, thêm 1 dòng ghi chú trạng thái tâm lý ngắn (bình thường/sau thua/sau thắng) tại thời điểm phân tích lệnh thứ 2+ — dữ liệu tối thiểu để loại trừ giả thuyết revenge/anchoring khi review sau.
- [ ] **R-BD-09**: Đề xuất thêm field `poi_type: Balanced Price Range (BPR)` vào controlled vocabulary của template (đã được note 03 gốc đề xuất ở ghi chú đầu file — nhắc lại như rule chính thức).

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG dùng grade A của lệnh này để kết luận "BPR luôn tốt hơn FVG đơn" — chưa verify được overlap thật (O2), và mẫu chỉ n=1 cho khái niệm BPR trong toàn vault.
- KHÔNG dùng cặp lệnh 02/03 (Loss sáng, Win chiều) để kết luận "cứ thua thì nên đổi sang POI quen thuộc hơn sẽ thắng" — đây là đúng dạng suy luận outcome-driven mà toàn bộ batch này đang cảnh báo; hai lệnh dùng bối cảnh D1/H1 giống nhau nhưng LTF hoàn toàn khác, không có cơ chế nhân-quả nào được xác lập giữa "vừa thua" và "lệnh sau thắng".
- KHÔNG coi việc CE khớp entry gần tuyệt đối (0.0025 lệch) là bằng chứng "kỹ thuật entry tốt hơn các lệnh khác trong batch" một cách tổng quát — đây có thể chỉ là ghi chép chính xác hơn ở riêng lệnh này, không phải năng lực entry được cải thiện qua thời gian (không có đủ mẫu theo trình tự thời gian để khẳng định xu hướng).


---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI: [[13 - FVG  - Fair Value Gap]] · [[03 - Balanced Price Range]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]]
- Dashboard: [[_Backtest Dashboard]]
