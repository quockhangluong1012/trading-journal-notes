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
> Đã viết tiếp phần bị cắt: nốt mục 6 (Phân tích sau lệnh), mục 7 (Lesson Learned) và mục 8 (Final Grade — lý giải vì sao `grade: C+` dù kết quả Win, RR 2.09). Toàn bộ phần bổ sung được suy luận **hoàn toàn từ dữ liệu đã có sẵn trong chính file này** (frontmatter, bảng 7-Step, Setup Quality checklist, Confluence 2/8) — không có số liệu giá/PnL mới nào bị bịa ra. Các cảnh báo ⚠️ gốc ở trên (mâu thuẫn CE/Edge, TP 1.05882 vs 1.05886, năm 2026/2016 lẫn lộn) vẫn còn nguyên và **chưa được  xác nhận** — phần Lesson Learned/Final Grade bên dưới có nhắc lại các điểm này như một phần bài học về kỷ luật ghi chép.

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

> [!warning] Đây là lesson rút ra từ dữ liệu backtest đã ghi, không phải nhật ký cảm xúc giao dịch thật (đây là backtest, không phải live trade).  nên đọc lại và chỉnh sửa nếu cách diễn giải không khớp với những gì đã thấy trên chart.

**1. Một kết quả Win không tự động chứng minh setup tốt — đây là ví dụ giáo khoa của "process vs outcome".**
Lệnh này thắng +2.09R, nhưng confluence chỉ 2/8, displacement bị chính người phân tích gán nhãn "marginal", và entry precision còn mâu thuẫn chưa giải quyết. Nếu coi đây là bằng chứng "công thức này hiệu quả",  sẽ vô tình học sai bài học — cái thắng ở đây đến từ bias/target đúng hướng (yếu tố vĩ mô), không phải từ một chuỗi xác nhận vi mô sắc bén. **Không tăng cỡ vị thế hay độ tự tin cho các setup có confluence tương tự (~2/8) dựa trên lệnh này.**

**2. Kỷ luật ghi chép ảnh hưởng trực tiếp đến chất lượng dữ liệu backtest — và dữ liệu backtest là thứ sẽ quyết định  có đủ điều kiện mua challenge hay không.**
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

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

### 9.1. Xác minh lại arithmetic — phát hiện RR discrepancy THẬT (không phải làm tròn)

Chạy lại phép tính độc lập từ chính số liệu frontmatter:

```
CE FVG = (1.06453 + 1.06414) / 2 = 1.064335   → khớp ce_price (1.064335), lệch 0.00001 so với entry_price 1.06434 (làm tròn bình thường)
Risk  = |entry_price - stop_loss| = |1.06434 - 1.06668| = 0.00234
Reward (dùng TP frontmatter 1.05882) = |1.06434 - 1.05882| = 0.00552
RR    = 0.00552 / 0.00234 = 2.359

Reward (dùng TP bảng Summary 1.05886) = |1.06434 - 1.05886| = 0.00548
RR    = 0.00548 / 0.00234 = 2.342
```

Cả hai cách tính đều cho RR ≈ **2.34–2.36**, không phải `r_planned: 2.09` như frontmatter ghi. Đây **không phải sai số làm tròn** (chênh lệch ~0.25-0.27, quá lớn để là lỗi hiển thị thập phân) — là một **[ARITHMETIC] discrepancy thật** chưa được note gốc phát hiện, dù note gốc đã rất kỹ tính trong việc tự phát hiện mâu thuẫn TP 1.05882 vs 1.05886 (mục đầu file) và mâu thuẫn CE vs Edge. Khả năng cao: `stop_loss` hoặc `entry_price` dùng để tính `r_planned` gốc khác với giá trị hiện đang lưu trong frontmatter — hoặc `r_planned` được tính cho leg H1 OB dự kiến (entry 1.06624, SL xa hơn) rồi không cập nhật lại khi chỉ leg M5 FVG khớp lệnh.

**Giả thuyết khớp nhất với dữ liệu**: nếu dùng entry dự kiến ở H1 OB high (1.06624) thay vì entry M5 FVG (1.06434) làm risk base: Risk = |1.06624-1.06668| = 0.00044 → quá nhỏ, RR sẽ quá lớn, không khớp 2.09. Thử ngược: nếu SL kế hoạch ban đầu khác 1.06668 — ví dụ SL ở đỉnh OB cũ hơn — Risk cần ~0.00264 để ra RR=2.09 với Reward 0.00552 (0.00552/2.09=0.00264, tức SL≈1.06434+0.00264=1.06698, lệch ~0.0003 so với SL hiện tại, quá nhỏ để giải thích trọn vẹn). Không có cách nào tái tạo chính xác 2.09 từ các số hiện có trong file — **kết luận: `r_planned: 2.09` là con số không truy nguyên được từ dữ liệu hiện tại, cần coi là lỗi ghi chép cần xác minh lại từ chart gốc, không phải tự suy ra thêm ở đây** (đúng nguyên tắc không bịa evidence).

### 9.2. Bản đồ Liquidity IRL↔ERL tại thời điểm entry

- **Pool đã bị lấy trước entry (13:40)**: đỉnh OB H1 (sweep 1 — giá quét lên cạnh trên OB rồi đóng ngược vào trong); minor high tạo MSS M5 lúc 12:15 (sweep nội bộ, không có tên/level cụ thể — cùng vấn đề `[UNSUPPORTED]` như đã thấy ở note 01/02 trong batch XAU).
- **Pool CHƯA bị lấy khi entry khớp**: EQL 1.05205 (SSL D1, mục tiêu draw), FVG 1.10036-1.09527 phía trên (không liên quan hướng Short này). TP 1.05882 nằm trên EQL — tức TP là điểm dừng TRƯỚC pool cuối cùng, một phần hợp lý (không tham lam tới tận đáy) nhưng cũng khiến RR thực nhận thấp hơn tiềm năng tối đa nếu tính tới EQL thật.
- **SL 1.06668 nằm sát mốc OTE 0.786 (1.06668 theo chính bảng H1 trong note)** — SL trùng khít với vùng OTE cao nhất, nghĩa là SL không đặt "xa tùy ý" mà đặt ĐÚNG BIÊN của dải OTE hợp lệ — một điểm neo có cơ sở hơn là bị "bóp bởi SL xa" như note gốc tự nhận xét (mục 7.4) mô tả cảm giác chủ quan, nhưng về cấu trúc SL vẫn nằm đúng biên OTE, không phải một mức tùy tiện.

### 9.3. Chất lượng Displacement/MSS

Đồng ý với tự đánh giá gốc (mục 6): "marginal, xa stoploss". Đối chiếu với 4 lệnh XAU cùng batch: đây là displacement M5 yếu thứ 3 (sau note 02 và note 04, cả hai đều Loss) — nhưng lệnh này vẫn Win. Điều này củng cố thêm luận điểm chính của batch (xem tổng hợp cross-trade, mục 10): chất lượng displacement M5 KHÔNG phải biến số phân tách rõ ràng Win/Loss trong mẫu 5 lệnh này — bias D1/H1 + vị trí POI có vẻ là yếu tố chi phối mạnh hơn.

### 9.4. Yếu tố thời gian

Entry 13:40 giờ dữ liệu gốc — note tự nhận chưa quy đổi UTC+7 và chưa xác nhận có còn trong London Kill Zone chính hay không (đánh dấu `[~]`, mục 5). Không thêm được thông tin mới ngoài việc xác nhận lại đây là một trường UNSUPPORTED thật (không có giờ quy đổi cụ thể để kiểm).

### 9.5. Vị trí entry trong Dealing Range

H1 DR (1.05653–1.06873): entry 1.06434 tương ứng (1.06434-1.05653)/(1.06873-1.05653) = 0.640 — nằm trong dải OTE (0.618-0.786) nhưng ở phần thấp, gần mép 0.618 hơn là sweet spot 0.705, khớp với tự đánh giá gốc ("CE≈OTE chỉ sát biên 0.618").

### 9.6. So sánh với vault

Batch này không có lệnh EURUSD nào khác để so sánh trực tiếp — so sánh chéo instrument với 4 lệnh XAU (xem mục 10 cho phân tích cross-trade đầy đủ). Về mặt cấu trúc split-entry (0.5/0.5), đây là lệnh duy nhất trong batch dùng kỹ thuật này — không có tiền lệ trong cụm để đối chiếu independent confirmation cho từng leg.

![[EURUSD-20161130-rr-discrepancy.svg|760]]

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
type: devils-advocate
mode: REVIEW
instrument: EURUSD
date: 2016-11-30
timeframes_provided: [D1 (mô tả + 2 ảnh không đọc được), H1 (mô tả + 1 ảnh), M5 (mô tả + 2 ảnh), M1 (không có)]
verdict: SURVIVES, WEAKENED
evidence_sufficiency: partial
opposite_case_strength: weaker
objections: {fatal: 0, material: 3, minor: 2}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN, O5 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base**: `evidence_sufficiency = partial` — cao hơn 4 lệnh XAU trong batch vì note gốc (2026-07-17) đã tự làm phần lớn công việc phản biện nội bộ (tự tính % khớp mô hình lý tưởng ~55-60%, tự liệt kê "Không đạt chuẩn/chưa xác minh"), giảm bớt phần việc DA phải tự phát hiện từ đầu. Vẫn không có ảnh đọc được.

**1. Thesis + load-bearing claim**: C1 Bias D1/H1 Bearish. C2 Sweep kép (đỉnh OB rồi cạnh FVG) + MSS M5 12:15 + FVG 12:10 → entry CE FVG 13:40. C3 TP đặt tại draw on liquidity thật (gần EQL Discount). C4 (từ C1+C2+C3) lệnh thắng vì bias/target đúng hướng lớn, không phải vì chuỗi xác nhận vi mô sắc bén — đây là **claim tự chẩn đoán của chính note gốc**, không phải điều DA này phát hiện ra. C5 `r_planned: 2.09`. **Load-bearing: C1 (bias) — nếu bias sai, toàn bộ "thắng nhờ đúng hướng lớn" sụp, vì đó là lý do duy nhất note gốc đưa ra để giải thích tại sao một setup confluence 2/8 lại thắng.**

**2. What survives**: C1 — bias có cơ sở rõ (Consolidation → Bearish Displacement → MSS H1, EQH/EQL xác định draw hai chiều) và outcome (Hit TP) không mâu thuẫn. C3 — TP đặt trước EQL (không tham lam tới tận đáy) là một quyết định risk-conscious hợp lý, giữ nguyên. Đặc biệt: note gốc TỰ đã hoàn thành phần lớn công việc "hunt hindsight/outcome-as-evidence" mà brief yêu cầu — mục 7 Lesson #1 viết thẳng "Một kết quả Win không tự động chứng minh setup tốt" và Final Grade mục 8 tự cho C+ dù Win. Đây là ví dụ hiếm trong toàn batch nơi tác giả đã tự áp dụng đúng kỷ luật "process over outcome" TRƯỚC khi DA vào cuộc.

**3. Objections**

**O1 · [ARITHMETIC] · material · attacks C5**
Claim: `r_planned: 2.09`.
Fails: tính lại từ chính entry/SL/TP trong frontmatter cho RR ≈ 2.34-2.36 (xem mục 9.1), không khớp 2.09 dù dùng TP nào trong hai giá trị mâu thuẫn đã biết. Đây là phát hiện MỚI của DA này — note gốc đã tự bắt được 2 mâu thuẫn khác (CE/Edge, TP 1.05882/1.05886) nhưng KHÔNG bắt được mâu thuẫn RR này.
Evidence: phép tính ở mục 9.1 — Risk=0.00234, Reward=0.00552 (hoặc 0.00548), RR=2.359 (hoặc 2.342), cả hai đều lệch xa 2.09.
Consequence: `grade: C+` đã dựa một phần vào nhận xét "RR đạt chuẩn ≥1:2 nhưng SL-driven, không phải reward-driven" (mục 8 gốc) — nếu RR thực là 2.34-2.36 thay vì 2.09, đây vẫn ≥1:2 nên không đổi kết luận qualitative, nhưng làm dấy nghi vấn về độ tin cậy của TOÀN BỘ trường số học trong file (đã có 2 mâu thuẫn khác), và ảnh hưởng trực tiếp tới bất kỳ dashboard tổng hợp R-multiple nào dùng field `r_planned`/`r_multiple` (đều ghi 2.09).
Your best answer: "2.09 có thể tính từ leg H1 OB dự kiến trước khi biết leg nào khớp." Đã thử tái tạo ở mục 9.1 — không khớp được chính xác bằng phép thử ngược đơn giản; không loại trừ khả năng này nhưng không đủ dữ liệu để xác nhận, nên vẫn treo là discrepancy chưa giải thích được.
Retracted by: đối chiếu lại chart gốc hoặc log tính toán ban đầu (nếu còn giữ) để xác nhận `r_planned` được tính từ cặp entry/SL/TP nào — nếu nó dùng một bộ số khác (ví dụ leg OB dự kiến), objection đóng với ghi chú rõ nguồn gốc con số.

**O2 · [HINDSIGHT/outcome-as-evidence] · material · attacks C2, C4**
Claim: "Thị trường có tín hiệu xác nhận trước entry — ít nhất 3" (mục 6 gốc, liệt kê sweep kép, MSS, sweep FVG).
Fails: cần kiểm nghiêm ngặt liệu 3 tín hiệu này có thực sự "trước entry và đủ để hành động" hay đang được liệt kê SAU KHI biết kết quả thắng, khiến chúng trông thuyết phục hơn thực tế tại thời điểm quyết định. Đặc biệt tín hiệu #1 "sweep kép... smart money từ chối Premium" là một diễn giải theo hướng có lợi cho kết luận thắng — nếu lệnh thua, cùng dữ liệu "giá quét lên rồi mới giảm 2 lần" có thể được đọc là "thị trường lưỡng lự, tín hiệu yếu" (chính note gốc cũng tự thừa nhận cách đọc thứ hai này ở Lesson #4: "đừng nhầm nhiều xác nhận với xác nhận chất lượng cao").
Evidence: mục 6 gốc dùng ngôn ngữ khẳng định mạnh ("smart money từ chối Premium") cho cùng một sự kiện mà Lesson #4 sau đó tự gọi là dấu hiệu "lưỡng lự".
Consequence: nếu tín hiệu xác nhận thực chất yếu hơn cách mục 6 trình bày, C4 (thắng vì bias/target, không phải vi mô) càng được củng cố — tức objection này KHÔNG đe dọa kết luận cuối, mà thực ra ủng hộ nó; nhưng nó cho thấy chính mục 6 của note gốc chưa hoàn toàn nhất quán về mức độ tự tin khi mô tả cùng một sự kiện ở hai chỗ khác nhau trong file.
Your best answer: mục 6 và Lesson #4 có thể đọc là bổ sung nhau (mục 6 mô tả sự kiện, Lesson #4 phản biện cách diễn giải) chứ không mâu thuẫn — nếu vậy đây là note tự chứa cả claim và phản biện của chính nó, một điểm mạnh hiếm gặp. Giữ material vì ngôn ngữ ở mục 6 vẫn hơi mạnh so với mức độ chắc chắn thực tế tại M5.
Retracted by: không cần "đảo ngược" gì thêm — ghi nhận rằng note gốc đã tự làm việc này, hạ objection xuống một dòng ghi chú khi trình bày lại thay vì coi là lỗi chưa được xử lý.

**O3 · [UNSUPPORTED] · material · attacks C2**
Claim: `idm_swept: Yes`, "sweep đỉnh OB rồi cạnh trên FVG" — cả hai đều không có tên level liquidity cụ thể ngoài mô tả hình dạng giá.
Fails: giống hệt pattern đã lặp lại ở note 01/02 trong batch XAU — SKILL.md § Sweep đòi hỏi level CÓ TÊN (không chỉ "đỉnh OB", "cạnh FVG" — đây là cạnh của PD array, không phải resting liquidity pool có tên).
Evidence: mục 3 note gốc "giá quét lên cạnh trên của Order Block... sau khi tạo đỉnh và đóng nến lại trong OB (Sweep)" — không có tên level (không phải EQH/PDH/session high).
Consequence: `idm_swept=Yes` (+1 confluence, 1/2 điểm confluence hiện có) có thể là overcall — nếu đúng theo canon chặt, confluence_score thực có thể chỉ 1/8, không phải 2/8, khiến grade D+ cho Confluence càng thấp hơn.
Your best answer: đây là pattern lặp lại toàn batch (xem cross-trade note trong summary), không riêng lệnh này — bản thân việc lặp lại nhất quán một cách hiểu "sweep = quét cạnh PD array" (thay vì đúng nghĩa canon "quét resting liquidity có tên") gợi ý đây là rule drift hệ thống trong cách ghi log của tác giả, không phải lỗi ngẫu nhiên một lệnh.
Retracted by: xác nhận có level liquidity có tên (EQH, session high, PDH...) trùng với "đỉnh OB"/"cạnh FVG" được nêu.

**O4 · [DOCTRINE] · minor · attacks execution mechanics**
Claim: split-entry 0.5/0.5 cho 2 POI khác cấp (H1 OB + M5 FVG).
Fails: đã tự nhận đầy đủ ở Lesson #3 gốc ("leg OB thực chất là một cược dự phòng hơn là entry có cơ sở") — không có gì để DA thêm vào, giữ ở minor chỉ để hoàn thiện ledger.
Retracted by: đã xử lý trong note gốc.

**O5 · [UNSUPPORTED] · minor · attacks C1**
Claim: mốc ngày "24/7/2026 – 9/11/2016" trong mô tả Consolidation D1.
Fails: đã tự flag ⚠️ trong note gốc (lẫn lộn năm 2026/2016) — chỉ ghi nhận lại, không đổi gì thêm.
Retracted by: đã xử lý trong note gốc (cần xác nhận từ chart nhưng không ảnh hưởng tới load-bearing claim).

Drafted: 5. Cut: 0.

**4. Opposite case (cùng evidence)**: Đọc ngược C4 — thay vì "thắng nhờ bias/target đúng hướng lớn", đọc là "thắng MAY MẮN nhờ chỉ một trong hai leg split-entry khớp lệnh (leg có RR tốt hơn), trong khi leg kia (H1 OB, RR sẽ tệ hơn/rủi ro hơn theo chính point 9.1 nếu SL phải đặt xa hơn) không khớp — nếu cả hai leg đều khớp, kết quả tổng hợp có thể khác." Tự phản biện case ngược: đây gần trùng với chính Lesson #3 gốc đã nêu ("may mắn, vì nếu cả hai leg đều khớp, rủi ro thực nhận sẽ là 1R đầy đủ") — tức note gốc ĐÃ tự nêu ra chính khả năng này, không phải một phát hiện độc quyền của DA. **Strength: weaker** — không thêm insight mới ngoài những gì note gốc đã tự thừa nhận, và không đủ dữ liệu (không biết leg H1 OB nếu khớp sẽ có RR/outcome gì) để định lượng thêm.
Distinguishing observable: không có — đây là một counterfactual không thể kiểm chứng từ dữ liệu lịch sử đã cố định (leg OB không khớp, không có dữ liệu giá tiếp theo cho kịch bản đó).

**5. Verdict: SURVIVES, WEAKENED.** Load-bearing claim C1 (bias) không bị đe dọa bởi bất kỳ objection nào. Nhưng phát hiện MỚI thật sự (O1, RR discrepancy 2.09 vs 2.34-2.36) là một lỗ hổng ghi chép mà ngay cả note gốc — vốn đã rất kỹ trong tự phê bình — cũng bỏ sót. Kết hợp O3 (sweep không có tên level, pattern lặp lại toàn batch), verdict giữ ở WEAKENED thay vì SURVIVES THIS ATTACK trơn, vì độ tin cậy của các trường số học/confluence trong file cần được xác minh lại toàn diện, không chỉ 2 điểm mà note gốc đã tự bắt.

**6. Falsification tests**:
1. Đối chiếu chart H1/M5 gốc để xác định `r_planned: 2.09` được tính từ cặp entry/SL/TP nào — đóng O1.
2. Xác nhận tên cụ thể của level liquidity bị "sweep" (đỉnh OB, cạnh FVG) — có phải EQH/session high/PDH nào không — đóng O3.
3. Rà toàn vault kiểm tra xem field `r_planned`/`r_multiple` có discrepancy tương tự ở các lệnh khác ngoài batch này không — nếu có, đây là lỗi hệ thống trong quy trình tính RR, không phải lỗi cá biệt của lệnh EURUSD này.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis**: Short EURUSD 30/11/2016, bias D1/H1 Bearish, split-entry 0.5/0.5 (H1 OB không khớp + M5 FVG khớp), sweep kép + MSS M5 + FVG → entry CE, TP tại draw on liquidity Discount, Hit TP +RR (số RR thực tế cần xác minh lại — xem mục 9-10).

**Cần sửa** (load-bearing trước):
- C-RR "`r_planned: 2.09`" — **FAIL** (không load-bearing về hướng bias, nhưng load-bearing cho tính toàn vẹn số học của record) · why: arithmetic không khớp — RR tính lại từ entry/SL/TP frontmatter cho 2.34-2.36, không phải 2.09; đây là mâu thuẫn arithmetic thực sự (anchor: SKILL.md nguyên tắc chung về kiểm arithmetic trước khi chấp nhận claim) → fix: đối chiếu chart gốc để xác định con số đúng, cập nhật `r_planned`/`r_multiple` hoặc giải thích rõ cơ sở tính 2.09 nếu nó dùng cặp giá khác.
- C-sweep "idm_swept=Yes / sweep đỉnh OB, cạnh FVG" — **UNSUPPORTED** · anchor: SKILL.md § Sweep ("Quét liquidity tại level có tên... không có reference level → UNSUPPORTED") — không có tên level cụ thể → fix: nêu tên level liquidity (EQH/session high...) hoặc hạ xuống không tính confluence.
- C-entry "CE vs Edge" — đã tự xử lý đầy đủ ở note gốc (ghi chú ⚠️ đầu file), không lặp lại, chỉ xác nhận: theo số học CE khớp gần tuyệt đối (lệch 0.00001) → nếu phải chọn 1 nhãn theo canon, **CE** đúng hơn Edge theo bằng chứng số, dù lời văn gọi "cạnh FVG".

**PASS**: C1 (bias D1/H1 Bearish, đồng thuận, draw on liquidity xác định rõ hai chiều) · C-target (TP tại draw on liquidity Discount hợp lệ, không tham lam quá mức) · C-MSS (MSS M5 12:15 phá swing low, mô tả đủ điều kiện hình thức).

**Verdict**: **INSUFFICIENT EVIDENCE** — không phải NOT ALIGNED vì bias/structure chính (load-bearing về hướng) đều PASS, nhưng hai claim phụ quan trọng (RR, sweep) rơi vào FAIL/UNSUPPORTED làm giảm độ tin cậy tổng thể của record đủ để không thể chấm DOCTRINE ALIGNED hay thậm chí PARTIALLY ALIGNED một cách thoải mái — RR sai không phải lỗi kế thừa từ bias, nó độc lập và ảnh hưởng tới tính đúng đắn của toàn bộ log số liệu.

**Notes**: Sweep-không-có-tên-level là pattern lặp lại ở ÍT NHẤT 3/5 lệnh trong batch này (note 01, 02, và note 05) — đây không còn là lỗi cá biệt mà là **rule drift hệ thống**: tác giả nhất quán dùng "sweep" để chỉ "quét cạnh của một PD array" thay vì đúng nghĩa canon "quét resting liquidity tại level có tên". Đề xuất bổ sung vào SKILL.md một cảnh báo misuse pattern cụ thể cho § Sweep: "quét cạnh OB/FVG/Breaker không tự động là sweep — chỉ là việc giá chạm biên PD array, trừ khi biên đó trùng với một liquidity pool có tên độc lập".

---

## 12. Lesson Learned (bản đầy đủ)

> Phần này CHỈ mở rộng — không lặp lại nội dung mục 6-8 gốc (đã có Lesson Learned + Final Grade rất đầy đủ, bao gồm đúng cảnh báo "process over outcome").

### (a) Bài học kỹ thuật

1. **Một record có TP mâu thuẫn ở 2 nơi thường có nguy cơ mâu thuẫn ở field số khác chưa bị phát hiện — cần audit TOÀN BỘ field số khi phát hiện 1 mâu thuẫn, không chỉ sửa chỗ đã thấy.** Ví dụ số thật: note gốc tự bắt TP 1.05882 vs 1.05886, nhưng KHÔNG bắt được `r_planned: 2.09` sai lệch với RR tính lại 2.34-2.36 (mục 9.1/O1). Tổng quát: khi phát hiện 1 lỗi ghi chép số học, chạy lại TOÀN BỘ phép tính phái sinh (RR, CE, OTE) trong file đó, không dừng ở lỗi đã thấy.
2. **"Sweep" cần một level có tên để tính confluence — quét cạnh của một PD array khác (OB, FVG) không tự động là sweep.** Ví dụ số thật: "sweep đỉnh OB" và "sweep cạnh FVG" trong note này không có tên level, giống hệt pattern ở 2 lệnh XAU khác trong batch. Tổng quát: chỉ tick `idm_swept`/`liquidity_swept` khi có tên level cụ thể (EQH, PDH, session high...).

### (b) Bài học quy trình/checklist

3. **Split-entry cần tiêu chí rõ ràng cho từng leg TRƯỚC khi đặt lệnh, không chỉ là cách né quyết định — đã tự nêu đầy đủ ở Lesson #3 gốc, chỉ nhấn mạnh thêm: tiêu chí này nên là một checkbox có thể tick TRƯỚC entry, không phải nhận xét viết SAU khi biết leg nào khớp** (tránh rơi vào hindsight khi tự đánh giá quyết định split-entry).

### (c) Bài học tâm lý-hành vi

4. **Ngôn ngữ mô tả tín hiệu xác nhận có xu hướng mạnh hơn (confident hơn) khi viết SAU khi biết kết quả thắng — ngay cả trong một note đã rất kỷ luật về "process over outcome".** Ví dụ: mục 6 gốc gọi sweep kép là "smart money từ chối Premium" (khẳng định mạnh), trong khi Lesson #4 cùng file gọi chính sự kiện đó là dấu hiệu "lưỡng lự" (khẳng định yếu hơn) — hai cách mô tả cùng một dữ kiện, khác nhau về mức độ tự tin, mà không có ghi chú nào giải thích tại sao ngôn ngữ đổi giữa hai mục. Đây là dấu hiệu vi mô của outcome bias dù tổng thể note đã cố gắng tránh nó.

### (d) Rule đề xuất cho Playbook

- [ ] **R-BD-13**: Khi phát hiện ≥1 mâu thuẫn số học trong một note, bắt buộc chạy lại toàn bộ chuỗi tính CE/RR/OTE bằng công thức độc lập trước khi đóng note đó.
- [ ] **R-BD-14**: `idm_swept`/`liquidity_swept` chỉ = Yes khi ghi kèm tên level cụ thể (áp dụng chung cho toàn vault, không chỉ batch này — đã đề xuất tương tự ở note 01/02, nhắc lại ở đây vì lặp lại lần thứ 3 trong cùng batch).
- [ ] **R-BD-15**: Khi mô tả "tín hiệu xác nhận" trong mục Replay, dùng ngôn ngữ ở mức độ chắc chắn NHẤT QUÁN với mục Lesson Learned cùng file — nếu hai mục mô tả cùng sự kiện khác mức độ tự tin, thêm một dòng giải thích lý do (ví dụ "mục Replay mô tả theo góc nhìn lúc đó, Lesson phản biện lại sau").

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG dùng RR đã sửa lại (2.34-2.36, nếu xác nhận đúng) để nâng grade C+ lên cao hơn — grade C+ của note gốc dựa trên nhiều tiêu chí khác (confluence 2/8, POI rank 1, kill zone chưa xác nhận) không liên quan tới con số RR; sửa RR chỉ ảnh hưởng tính toàn vẹn dữ liệu, không tự động cải thiện chất lượng quy trình.
- KHÔNG kết luận "confluence 2/8 vẫn thắng nên ngưỡng confluence tối thiểu có thể hạ" — đây chính là cảnh báo đã có sẵn ở Final Grade gốc ("Không dùng lệnh này làm căn cứ để hạ chuẩn confluence tối thiểu"), nhắc lại nguyên văn tinh thần đó ở đây vì đây là lệnh Win duy nhất ngoài cụm XAU trong batch, dễ bị dùng sai làm "bằng chứng ngoài mẫu" củng cố xu hướng chọn confluence thấp.
- KHÔNG dùng pattern "displacement M5 yếu nhưng vẫn thắng" (giống note 01, 03 trong cụm XAU) để kết luận tổng quát "chất lượng displacement M5 không quan trọng" — mẫu quá nhỏ (n=5, không đồng nhất instrument/thời gian) để rút ra quy luật, đây chỉ là một quan sát cần theo dõi thêm.


---

### Liên kết

> Mục Liên kết không tồn tại trong file gốc. Gợi ý liên kết dựa trên nội dung đã đọc: [[01 - ICT 2022 Model]] · [[25-OB-Order-Block]] · [[13-FVG-Fair-Value-Gap]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[_Backtest Dashboard]]
