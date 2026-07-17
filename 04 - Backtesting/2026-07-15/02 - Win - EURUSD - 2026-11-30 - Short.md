---
type: backtest
backtest_date: 2026-07-15
trade_date: 2016-11-30
symbol: EURUSD
position: Short
result: Win
session: London
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
poi_stack: H1 Order Block 1.06624-1.06563 (không khớp lệnh) + M5 FVG 1.06453-1.06414 (khớp lệnh, entry)
fvg_high: 1.06453
fvg_low: 1.06414
ce_price: 1.064335
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
entry_price: 1.06434
stop_loss: 1.06668
take_profit: 1.05882
r_planned: 2.09
rr_if_ce:
rr_if_ote:
r_multiple: 2.09
risk_percent:
spread_cost:
r_net:
grade: C+
followed_plan: Yes
confidence:
tags:
  - backtest
  - ICT2022
  - POI
  - split-entry
---

# Backtest 2016-11-30 — EURUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi khác (2026-07-17)
> - `entry_type`/`entry_precision` = CE: bảng Summary gốc ghi entry là "cạnh của FVG M5" và mục M5/M1 viết "Entry khi giá quay về cạnh dưới FVG" (ngụ ý Edge), nhưng về số học, entry 1.06434 gần như trùng khít CE của FVG (1.064335, lệch 0.00001) — mình ưu tiên số liệu khách quan hơn cách gọi tên trong lời văn. ⚠️ Cần bạn xác nhận lại đây là CE hay thực sự là Edge bị ghi nhầm số.
> - Lệnh này dùng **split-entry 0.5 slot**: 1 limit tại H1 OB (1.06624–1.06563, không khớp) + 1 limit tại M5 FVG (1.06453–1.06414, khớp). `poi_type`/`poi_stack` phản ánh cả 2, nhưng field số (entry/SL/TP/R) chỉ tính cho leg đã khớp (M5 FVG), đúng như bản gốc.
> - **Mâu thuẫn nhỏ về TP**: frontmatter gốc ghi `take_profit: 1298.732`... à nhầm, đây là EURUSD — frontmatter gốc ghi `take_profit: 1.05882`, nhưng bảng Summary (mục 0) ghi TP = **1.05886**. Mình giữ theo frontmatter gốc (1.05882) vì đó là nguồn Dataview đọc, nhưng bạn nên đối chiếu lại chart để biết số nào đúng.
> - `poi_rank` = 1 vì FVG đơn không nằm ở rank cao hơn dù có OB đi kèm (OB không khớp lệnh nên không tính vào poi_stack rank).

> [!success] Đã bổ sung phân tích (2026-07-17)
> Đã viết tiếp phần bị cắt: nốt mục 6 (Phân tích sau lệnh), mục 7 (Lesson Learned) và mục 8 (Final Grade — lý giải vì sao `grade: C+` dù kết quả Win, RR 2.09). Toàn bộ phần bổ sung được suy luận **hoàn toàn từ dữ liệu đã có sẵn trong chính file này** (frontmatter, bảng 7-Step, Setup Quality checklist, Confluence 2/8) — không có số liệu giá/PnL mới nào bị bịa ra. Các cảnh báo ⚠️ gốc ở trên (mâu thuẫn CE/Edge, TP 1.05882 vs 1.05886, năm 2026/2016 lẫn lộn) vẫn còn nguyên và **chưa được Khang xác nhận** — phần Lesson Learned/Final Grade bên dưới có nhắc lại các điểm này như một phần bài học về kỷ luật ghi chép.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1→H1→M5)                                          |
| Trade Date (dữ liệu)      | 2016-11-30 13:55 (UTC+7)                                     |
| Position                  | Short                                                        |
| Result                    | Win (Hit TP)                                                 |
| Session                   | London Open                                                  |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes (giá cuối cùng chạm TP)                                  |
| **POI Type**              | FVG (M5, leg khớp lệnh) — H1 OB đi kèm không khớp            |
| POI Rank (8.1)            | 1                                                             |
| POI Timeframe             | M5 (bối cảnh H1)                                             |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE ⚠️ (lời văn gốc gọi là "cạnh FVG" — xem ghi chú)          |
| **Limit Filled?**         | Yes (leg M5 FVG) — leg H1 OB **không khớp**                  |
| **First Error Step**      | none                                                          |
| R Planned (gross)         | 2.09                                                         |
| R Net (sau spread)        | (chưa có dữ liệu)                                            |
| R Multiple (kết quả)      | 2.09                                                         |
| Confluence Score (0–8)    | 2                                                             |
| Grade                     | C+ (lý do chi tiết — xem mục 8. Final Grade)                 |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 — Daily Bias & Context

- **Bias**: Bearish · **Market Condition**: HL/LL
- **Lý do xác định bias**: Giá đang trong nhịp hồi sau các cây nến Bearish Displacement mạnh. Có 1 nhịp Consolidation từ 24/7/2026 – 9/11/2016 (⚠️ khoảng ngày lẫn 2026/2016 trong bản gốc — giữ nguyên như đã viết, cần bạn xác nhận lại năm). Ngày 9/11/2016 giá có 1 cây nến lớn quét lên trên các old high tạo EQH, sau đó giảm mạnh tạo Bearish Displacement + FVG trên đường giá.
- **Draw on Liquidity**: BSL — EQH 1.12905, FVG 1.10036–1.09527. SSL — EQL 1.05205. Thiên hướng Short intraday.

![[Pasted image 20260715141103.png]]
![[Pasted image 20260715140520.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Dealing range Low(0)=1.05653 → High(1)=1.06873. Nhịp displacement giảm tạo MSS khung H1 → Bias H1 Bearish.
- **PD Array trong Premium**: Order Block (OB) 1.06624–1.06563 — POI sâu hơn, nằm cao hơn trong Premium.
- **Fib OTE levels**: 0.618=1.06414 · 0.705=1.06512 · 0.786=1.06668.
- **Liquidity cần chờ sweep**: sweep lên cạnh trên của OB.

![[Pasted image 20260715141948.png]]

### Phân tích context → lệnh

- Bias Bearish (D1+H1 đồng thuận), giá đã quét SSL Discount và đang retrace lên Premium → khung cảnh cho Short hợp lệ.
- 28/11/2016 giá tạo nhiều nến Bullish Displacement thân lớn → quét hết old low bên trái → tạo đỉnh và reject (râu dài, thân nhỏ → khả năng Rejection Block). Sau đó Consolidation 28/11/2016 2:00–19:00 (New York Session). Khi New York Open, Bearish Displacement phá xuống khỏi Consolidation. Nhịp giảm tạo đáy, hồi lên FVG H1 (từ displacement), giảm tiếp hình thành Equal Low. Sau EQL, giá tăng mạnh (displacement) thân lớn. Retrace về vùng POI lúc 11:00 ngày 30/11/2016. Xuống M5 quan sát — không tìm entry vội vì chưa vào Killzone (London, New York).

---

## 2. POI Profile

- **POI Type đã dùng**: FVG (M5, leg khớp lệnh); H1 Order Block đi kèm nhưng **không khớp lệnh**.
- **POI Rank (8.1)**: 1 (FVG đơn — OB không tính vào rank vì không khớp).
- **POI hình thành trên khung**: M5 (bối cảnh H1).
- **POI nằm ở**: Premium ✓.
- **POI stack**: H1 OB 1.06624–1.06563 (không khớp) + M5 FVG 1.06453–1.06414 (khớp, entry).
- **CE của FVG trùng OTE 62–79%?**: CE ≈1.064335 nằm sát mốc 0.618 (1.06414) — biên dưới của OTE.
- **Bounds & CE**: FVG High 1.06453 / Low 1.06414, CE = 1.064335 (≈ entry thực tế 1.06434).

---

## 3. Entry Precision & Fill

- **Entry Type**: CE (⚠️ xem ghi chú về mâu thuẫn lời văn "cạnh FVG")
- **Entry Precision**: CE
- **Limit có khớp?**: Yes cho leg M5 FVG; **No** cho leg H1 OB (giá không retrace đủ sâu về OB)
- **Giá đi sâu bao nhiêu vào FVG?**: không có số đo % cụ thể trong bản gốc
- **RR ghi lại**: r_planned 2.09 (Risk 0.00254 / Reward 0.00532 điểm)

### M5/M1 — Xác nhận & điểm vào lệnh

- Xuống M5 khi giá retrace về vùng POI. Giá quét lên cạnh trên của Order Block, đóng nến ngược trở lại vào trong OB. Sau sweep đó giá bật mạnh khỏi OB tạo swing low liên tiếp. Giá quét cây nến trước và đóng nến xanh mạnh lên qua đỉnh sweep trước đó (một nhịp sweep lúc 11:15). Sau khi tạo đỉnh và đóng nến lại trong OB (Sweep), giá quay đầu giảm mạnh tạo Bearish MSS lúc 12:15. Nhịp displacement tạo MSS để lại FVG lúc 12:10 (1.06453–1.06414). Chờ giá retrace về vùng FVG này. Lúc 13:40 giá quét lên vùng FVG với 1 nến xanh đóng bên trong FVG và râu dài lên phía trên (Sweep). Entry khi giá quay về cạnh dưới FVG, stoploss đỉnh sweep OB (Stoploss xa).
- **Entry trigger**: Liquidity Sweep quét minor high FVG M5; MSS phá swing low lúc 12:15; Displacement → tạo M5 FVG lúc 12:10; Retrace về FVG → khớp lệnh.
- **Invalidation (kế hoạch)**: giá đóng nến trên đỉnh sweep của OB.
- **Chờ đủ điều kiện?** Có — khi giá tạo FVG ngay gần đáy displacement, dựng 2 kịch bản (giá về FVG, hoặc retrace sâu về OB). Tách lệnh làm 2 (0.5 slot mỗi lệnh), vào tại 2 vị trí → giá chỉ quay về FVG rồi đảo chiều giảm tới TP → khớp 1 lệnh.

M5 (ban đầu): ![[Pasted image 20260715141405.png]]
Result: ![[Pasted image 20260715141347.png]]

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes (sweep kép: đỉnh OB rồi cạnh trên FVG) | `step3_sweep_ok` |
| 4 | Displacement + MSS | Yes (chất lượng marginal, xa stoploss — theo ghi chú gốc) | `step4_displacement_ok` |
| 5 | POI (FVG, H1 OB đi kèm) | Yes | `step5_poi_ok` |
| 6 | Entry (retrace) | Yes | `step6_entry_ok` |
| 7 | Target | Yes | `step7_target_ok` |

- **First Error Step**: none
- **Missing Step**: none
- **Đủ chuỗi 7 bước?**: Yes

---

## 5. Setup Quality & Confluence

- [x] Bias D1 rõ ràng, không mâu thuẫn H1
- [ ] **POI selection tối ưu** — tách lệnh làm 2 để cân bằng tỷ lệ khớp lệnh (OB và FVG); không tối ưu tuyệt đối nhưng có lý do rõ
- [~] Giá nằm trong Kill Zone — cần xác minh (giờ entry có thể đã trôi khỏi London KZ chính)
- [x] Có Liquidity Sweep trước entry (M1/M5)
- [x] Displacement rõ ràng — M5 không tạo FVG thật sự rõ, tuy nhiên xa stoploss nên chấp nhận được
- [x] Có MSS hợp lệ
- [x] POI nằm trong Premium (đúng phía cho Short)
- [x] Entry trong POI hợp lệ, không đua giá
- [x] SL ở vùng invalidation hợp lý — SL đặt trên đỉnh sweep
- [x] RR ≥ 1:2 (2.09 — bị bóp bởi SL xa)

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không (rank 1) | *(suy từ poi_rank)* |
| 2 | CE FVG trùng OTE 62–79% | Sát biên (0.618) | `ce_ote_overlap` |
| 3 | SMT divergence | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | Không có ghi chú | `cisd_confirm` |
| 5 | Macro time | Chưa đánh giá | `in_macro_time` |
| 6 | NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | SD target align | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Có (sweep OB trước MSS) | `idm_swept` |

- **Score**: 2/8.

---

## 6. Phân tích sau lệnh (Replay)

> [!info] "Result" và hai mục đầu (root cause thắng, tín hiệu xác nhận) là phần cuối cùng còn sót lại của file gốc trước khi bị cắt cụt. Hai mục "Setup khớp bao nhiêu %" và "Nếu vào lại" bên dưới là phần bổ sung mới (2026-07-17).

- **Result**: **Hit Take Profit (+2.09R)** — leg vào tại M5 FVG khớp; leg limit tại H1 OB **không khớp** (giá không retrace đủ sâu về OB).

### Điều gì thực sự khiến lệnh THẮNG? (root cause thật)
- Bias top-down đồng thuận (D1+H1 Bearish) + giá retrace vào Premium đúng phía → xác suất Short cao ngay từ context.
- Chuỗi 2022 Model trên M5 hoàn chỉnh: Sweep đỉnh OB → Displacement giảm → MSS (12:15) → FVG (12:10) → retrace entry. Đây mới là leg tạo lợi nhuận — không phải leg OB.
- TP đặt tại draw on liquidity thật (SSL/EQL Discount ~1.05882) → giá có "nam châm" để chạy tới.

### Thị trường có tín hiệu xác nhận trước entry không? Có — ít nhất 3:
1. Sweep kép tại POI: quét đỉnh OB (H1) rồi đóng nến ngược trở lại — smart money từ chối Premium.
2. MSS M5 rõ lúc 12:15 phá swing low → chuyển hướng cấu trúc nội tại.
3. Sweep cạnh trên M5 FVG lúc 13:40 (nến xanh râu dài, đóng trong FVG) trước khi quay đầu — đúng "mồi" của FVG entry.

### Setup khớp bao nhiêu % so với mô hình 2022 lý tưởng?

Nhìn thuần theo 7-Step Decision Log, lệnh này *đủ chuỗi* (7/7 bước = Yes) — về giấy tờ đây là một setup "sạch". Nhưng "đủ bước" và "chất lượng từng bước" là hai chuyện khác nhau, và đây chính là chỗ khoảng cách giữa **outcome** và **process** lộ ra rõ nhất:

- **Đạt chuẩn cao**: Bước 1 (Bias), Bước 2 (Draw on Liquidity), Bước 7 (Target đặt đúng draw on liquidity thật — SSL/EQL Discount). Đây là phần "khung" — top-down đúng và có lý do.
- **Đạt chuẩn nhưng có tì vết**: Bước 3 (Sweep) là sweep kép hai tầng (đỉnh OB rồi cạnh FVG) — về bản chất là tốt (2 lần từ chối Premium), nhưng cũng là dấu hiệu thị trường "lưỡng lự", không phải một cú sweep dứt khoát một lần. Bước 4 (Displacement) tự bản thân ghi chú gốc đã nói thẳng: "chất lượng marginal, xa stoploss" — tức đây không phải một displacement đẹp theo tiêu chuẩn ICT (thân nến lớn, ít wick, tạo FVG rõ ràng), mà là loại "chấp nhận được vì SL đã đặt xa sẵn", chứ không phải "tốt vì bản thân nó rõ".
- **Không đạt chuẩn / chưa xác minh được**: Bước 5 (POI) hợp lệ về vị trí (Premium, CE≈OTE 0.618) nhưng `poi_rank = 1` — nghĩa là đây là một FVG đơn, không có xác nhận đa tầng thật sự (OB đi kèm không khớp nên không được tính). Bước 6 (Entry) có mâu thuẫn nội bộ chưa giải quyết: lời văn Summary/M5 gọi đây là entry ở "cạnh dưới FVG" (Edge), nhưng số học lại khớp gần như tuyệt đối với CE — nếu đúng là Edge, đây là entry **kém chính xác hơn** so với những gì frontmatter đang ghi nhận.
- **Confluence rất mỏng**: 2/8 — chỉ có CE≈OTE (sát biên, không phải trùng khít) và Inducement bị quét. Không có SMT, không có CISD, chưa xác nhận Macro Time, không có NWOG/NDOG, không có SD target alignment.

**Ước lượng khớp mô hình lý tưởng**: khoảng **55–60%**. Đủ điều kiện tối thiểu để vào lệnh (không phải lệnh phạm quy), nhưng đây là một setup ở **ngưỡng dưới** của "A-grade 2022 Model" — thắng nhờ đúng hướng lớn (bias D1/H1 + target hợp lý) nhiều hơn là nhờ một chuỗi xác nhận vi mô chặt chẽ.

### Nếu vào lại — sẽ làm gì khác?

1. **Chốt lại entry_type trước khi log, không để mơ hồ CE/Edge.** Đây là việc phải làm *ngay tại thời điểm phân tích*, không phải đợi review sau — vì nó ảnh hưởng trực tiếp đến cách tính `entry_precision` và độ tin cậy của toàn bộ mẫu backtest 2022 Model.
2. **Xem lại logic split-entry 0.5/0.5 cho case "OB + FVG cùng hướng".** Ở đây leg xa (H1 OB) không khớp — may mắn, vì nếu cả hai leg đều khớp, rủi ro thực nhận sẽ là 1R đầy đủ thay vì 0.5R, trong khi phần lý do chọn OB (POI rank cao hơn) lại không có xác nhận M5 riêng cho nó. Cần một quy tắc rõ ràng: chỉ split khi cả hai POI đều có xác nhận đa khung độc lập, không phải chỉ vì "không chắc giá về đâu".
3. **Xác nhận Kill Zone bằng giờ UTC+7 cụ thể trước khi log, không để dấu `[~]` treo.** Entry lúc 13:40 (giờ dữ liệu gốc — cần quy đổi chính xác sang UTC+7) đang ở trạng thái chưa xác minh có còn nằm trong London Kill Zone chính hay đã trôi sang giai đoạn thấp thanh khoản.
4. **Không nới lỏng tiêu chuẩn Displacement chỉ vì SL đã xa.** SL xa là hệ quả của một quyết định khác (đặt trên đỉnh sweep OB), không phải lý do để hạ chuẩn đánh giá chất lượng displacement. Hai tiêu chí này cần được chấm độc lập.

---

## 7. Lesson Learned

> [!warning] Đây là lesson rút ra từ dữ liệu backtest đã ghi, không phải nhật ký cảm xúc giao dịch thật (đây là backtest, không phải live trade). Khang nên đọc lại và chỉnh sửa nếu cách diễn giải không khớp với những gì đã thấy trên chart.

**1. Một kết quả Win không tự động chứng minh setup tốt — đây là ví dụ giáo khoa của "process vs outcome".**
Lệnh này thắng +2.09R, nhưng confluence chỉ 2/8, displacement bị chính người phân tích gán nhãn "marginal", và entry precision còn mâu thuẫn chưa giải quyết. Nếu coi đây là bằng chứng "công thức này hiệu quả", Khang sẽ vô tình học sai bài học — cái thắng ở đây đến từ bias/target đúng hướng (yếu tố vĩ mô), không phải từ một chuỗi xác nhận vi mô sắc bén. **Không tăng cỡ vị thế hay độ tự tin cho các setup có confluence tương tự (~2/8) dựa trên lệnh này.**

**2. Kỷ luật ghi chép ảnh hưởng trực tiếp đến chất lượng dữ liệu backtest — và dữ liệu backtest là thứ sẽ quyết định Khang có đủ điều kiện mua challenge hay không.**
Có ít nhất hai mâu thuẫn nội bộ trong chính file này: (a) entry được gọi là "cạnh FVG" trong lời văn nhưng lại khớp số học với CE; (b) TP trong bảng Summary (1.05886) lệch với TP trong frontmatter (1.05882) — Dataview chỉ đọc frontmatter, nên nếu con số trong bảng mới là đúng, toàn bộ R-multiple của lệnh này đang bị tính sai một chút trong mọi dashboard tổng hợp. Bài học thực dụng: **chốt số liệu tại thời điểm phân tích, không để "sẽ xác nhận sau" — vì "sau" hiếm khi quay lại.**

**3. Split-entry (0.5/0.5 slot) là một quyết định quản trị rủi ro hợp lý về mặt lý thuyết, nhưng ở đây nó cũng là dấu hiệu thiếu một quyết định dứt khoát.**
Tách lệnh vì "không chắc giá về FVG hay về sâu tới OB" là hợp lý khi cả hai POI đều mạnh ngang nhau và có xác nhận độc lập. Ở đây OB không có xác nhận M5 riêng của nó (không có MSS/FVG M5 gắn với OB) — nghĩa là leg OB thực chất là một "cược dự phòng" hơn là một entry có cơ sở. Bài học: **split-entry cần một tiêu chí rõ ràng (cả hai leg đều pass đủ 7 bước độc lập), không phải một cách để né việc phải chọn.**

**4. Sweep kép (đỉnh OB rồi cạnh FVG) là tín hiệu tốt nhưng đừng nhầm "nhiều xác nhận" với "xác nhận chất lượng cao".**
Hai lần bị từ chối ở Premium là dữ liệu tốt cho bias Bearish, nhưng nó cũng có thể đọc theo hướng khác: thị trường mất hai lần thử mới xác nhận hướng, tức là độ "sạch" của cấu trúc thấp hơn một cú sweep — MSS — FVG diễn ra gọn trong một nhịp duy nhất. Khi review các lệnh tương lai, tách riêng hai khái niệm "số lượng xác nhận" và "độ sắc bén của xác nhận" khi chấm confluence, đừng gộp chung.

**5. RR 2.09 "trông đẹp trên giấy" nhưng bị nén bởi SL xa, không phải vì Reward lớn bất thường.**
Checklist mục 5 tự ghi nhận điều này ("RR ≥ 1:2 — bị bóp bởi SL xa"). Một RR đạt chuẩn vì SL buộc phải đặt xa (trên đỉnh sweep OB, ngoài toàn bộ vùng OB) là một RR *yếu hơn* một RR đạt chuẩn vì SL chặt và Reward tự nhiên lớn từ draw on liquidity xa. Cùng là "≥1:2" nhưng chất lượng rủi ro khác nhau — cần một cách đánh dấu riêng cho hai loại RR này trong các backtest sau (ví dụ thêm ghi chú `rr_quality: SL-driven` vs `reward-driven`).

---

## 8. Final Grade

> [!info] Bảng điểm dưới đây được suy ra từ dữ liệu đã có trong chính file (7-Step Log, Setup Quality checklist, Confluence 2/8, các ghi chú "marginal"/"bị bóp bởi SL xa" đã có sẵn) — không dùng thông tin ngoài file.

| Tiêu chí | Đánh giá | Ghi chú |
|---|---|---|
| HTF Bias & Context (D1→H1) | **A-** | Bias đồng thuận, draw on liquidity xác định rõ; duy nhất điểm trừ nhỏ là mốc ngày 2026/2016 lẫn lộn chưa xác nhận |
| 7-Step chain (đủ chuỗi) | **B** | Đủ cả 7 bước, nhưng Bước 4 (Displacement) tự nhận "marginal", Bước 3 là sweep kép (2 lần thử, không dứt khoát) |
| POI quality | **C+** | `poi_rank = 1` — FVG đơn, OB đi kèm không có xác nhận M5 riêng nên không tính; CE≈OTE chỉ sát biên 0.618, không trùng khít vùng giữa OTE |
| Entry precision & documentation | **C** | Mâu thuẫn CE vs "Edge" chưa xác nhận; TP 1.05882 (frontmatter) vs 1.05886 (bảng Summary) chưa đối chiếu — cả hai đều là lỗi kỷ luật ghi chép, không phải lỗi đọc chart |
| Risk/Reward structure | **C+** | RR 2.09 đạt chuẩn ≥1:2, nhưng do SL bị đẩy xa (ngoài toàn bộ OB) chứ không phải do Reward tự nhiên lớn — RR "SL-driven", không phải RR "reward-driven" |
| Kill Zone timing | **C** | Chưa xác minh entry (13:40 giờ dữ liệu gốc) có còn nằm trong London Kill Zone chính hay đã trôi ra ngoài — đánh dấu `[~]` trong checklist chưa được giải quyết |
| Confluence Score | **D+** | 2/8 — chỉ có CE≈OTE (sát biên) và Inducement bị quét; thiếu SMT, CISD, Macro Time, NWOG/NDOG, SD target align |
| Execution mechanics (split-entry) | **B-** | Quản trị rủi ro hợp lý về nguyên tắc, nhưng leg OB thiếu cơ sở xác nhận độc lập — mang tính dự phòng hơn là quyết định có luận cứ |

**Trọng số ngầm định**: quy trình vào lệnh (bias, 7-step, POI, entry, RR, timing, confluence, execution) được coi trọng hơn kết quả (Win/Loss) — đúng nguyên tắc "process over outcome" của nhật ký này. Outcome (+2.09R, Hit TP) không được tính là một tiêu chí chấm điểm riêng.

**Overall Grade**: **C+** — khớp với frontmatter gốc. Đây là một lệnh **thắng nhờ đúng hướng lớn (bias + target), không thắng nhờ một quy trình vi mô sắc bén**. Confluence 2/8 và các mâu thuẫn ghi chép chưa giải quyết là lý do chính kéo điểm xuống mức C+ dù kết quả là Win — đúng tinh thần "một lệnh thắng tồi (process yếu) không nên được đối xử tốt hơn một lệnh thua tốt (process chuẩn)". Không dùng lệnh này làm căn cứ để hạ chuẩn confluence tối thiểu cho các setup 2022 Model sau này.

---

### Liên kết

> Mục Liên kết không tồn tại trong file gốc. Gợi ý liên kết dựa trên nội dung đã đọc: [[01 - ICT 2022 Model]] · [[25 - OB - Order Block]] · [[13 - FVG  - Fair Value Gap]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[_Backtest Dashboard]]
