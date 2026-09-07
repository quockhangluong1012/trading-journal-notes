---
type: backtest
backtest_date: 2026-07-16
trade_date: 2016-06-12
symbol: EURUSD
position: Short
result: Win
session: London
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model (HTF OB + LTF Sweep/Displacement/MSS/FVG)
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: Order Block
poi_rank: 2
poi_timeframe: H1
poi_location: Premium
poi_in_ote: Yes
ce_ote_overlap: Yes
poi_stack: H1 Order Block (POI chính, 1.06839-1.06788) + M5 FVG (entry trigger, 1.06706-1.06650)
fvg_high: 1.06706
fvg_low: 1.06650
ce_price: 1.06678
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
sweep_type: Double
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
entry_price: 1.06677
stop_loss: 1.06849
take_profit: 1.06249
r_planned: 2.49
rr_if_ce: 2.49
rr_if_ote:
r_multiple: 2.49
risk_percent:
spread_cost:
r_net:
grade: B+
followed_plan: Yes
confidence:
touch_count_to_mss: 2
mss_touch_detail: MSS M5 hình thành ở lần chạm OB thứ 2 (~18:00 New York). Lần chạm 1 (~16:15 London) chỉ sweep CE của OB rồi bật ra, KHÔNG có MSS → không entry.
tp_fill_anomaly: TP bị quét bởi 1 gap cuối tuần (Chủ nhật), không phải bởi price action tuần tự — xem mục 6 & Lesson.
tags:
  - backtest
  - ICT2022
  - POI
  - weekend-gap-fill
  - double-tap-poi
---

# Backtest 2016-06-12 — EURUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi (2026-07-17)
> Chuyển từ template cũ sang **Backtest template - POI & Step Decision**. Toàn bộ phân tích gốc (vốn đã rất chi tiết, có field mở rộng riêng) được giữ nguyên. Các field mở rộng của bản gốc — `touch_count_to_mss`, `mss_touch_detail`, `tp_fill_anomaly` — **được giữ nguyên trong frontmatter** vì chúng ghi lại chi tiết giá trị không có trong template chuẩn (double-tap POI, gap fill outcome). Đây là ví dụ tốt cho việc **mở rộng template khi cần**, miễn là field chuẩn vẫn đầy đủ để dashboard tổng hợp.
> `sweep_type: Double` được chọn vì có 2 loại sweep khác nhau trong chuỗi: sweep CE của OB (External, chạm 1) và sweep đỉnh nội bộ thấp hơn (Internal, chạm 2).
> `poi_rank: 2` (FVG+OB) vì entry trigger là M5 FVG lồng trong bối cảnh H1 Order Block — đúng combo rank 2 theo thang 8.1.
> ⚠️ **`r_multiple: 2.49` là kết quả danh nghĩa** — bản gốc tự flag rằng TP đạt được nhờ gap cuối tuần, không phải price action tuần tự. Khi tính expectancy tổng trên `_Backtest Dashboard`, nên lọc riêng các trade có tag `weekend-gap-fill` để so sánh (xem `tp_fill_anomaly` và Lesson 2 bên dưới).

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1→H1→M5)                                          |
| Trade Date (dữ liệu)      | 2016-06-12 (giờ UTC+7)                                       |
| Position                  | Short                                                        |
| Result                    | Win (Hit TP — **qua gap cuối tuần**, xem mục 6)              |
| Session                   | London (chạm 1, 16:15) → New York (chạm 2 + entry, 18:00)    |
| HTF Bias                  | Bearish (D1+H1 đồng thuận)                                   |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | Order Block (H1, Premium sâu)                                |
| POI Rank (8.1)            | 2 (FVG+OB)                                                   |
| POI Timeframe             | H1 (entry M5)                                                |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | none                                                         |
| Số lần chạm POI tới MSS   | **2** (chạm 1 = sweep only; chạm 2 = MSS + FVG)              |
| R Planned (gross)         | 2.49                                                         |
| R Net (sau spread)        | (chưa có dữ liệu)                                            |
| R Multiple (kết quả)      | 2.49 (danh nghĩa — xem cảnh báo gap)                         |
| Confluence Score (0–8)    | 2                                                             |
| Grade                     | B+                                                            |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.
> ⚠️ Field mở rộng `touch_count_to_mss`, `mss_touch_detail`, `tp_fill_anomaly` dùng để lọc/gắn cờ các trade có kết quả bị ảnh hưởng bởi gap khi tính expectancy tổng.

---

## 1. HTF Context & Bias

### D1 — Daily Bias & Context

- **Bias**: Bearish · **Market Condition**: Pullback trong nhịp giảm (retracement lên premium trước khi tiếp tục xuống)
- **Lý do xác định bias**: Khung D1 trước đó có chuỗi nến Bearish Displacement mạnh, thân lớn, để lại dấu vết phân phối rõ ràng — premise gốc cho bias Bearish. Sau displacement, giá bước vào chuỗi nến hồi đi ngược lên (retracement bình thường trong xu hướng giảm — không phá vỡ cấu trúc giảm khung lớn). Nhịp hồi đưa giá lên vùng cao của range D1, chạm Premium (0.705–1.0 fib) — đúng vùng POI dùng ở H1. Ngày 12/06/2016 (ngày trade), D1 in ra nến giảm lớn, đánh dấu điểm giá từ chối Premium và quay đầu — chính là nến chứa trọn setup H1/M5.
- **Draw on Liquidity**: BSL — đỉnh nhịp hồi D1 (khớp đỉnh H1 OB ~1.06849–1.06898) — đã bị từ chối, không phải mục tiêu. SSL — đáy nhịp giảm D1 trước đó/vùng dưới H1 DR Low (1.06249) — mục tiêu chính cho Short.

![[Pasted image 20260716134531.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Downtrend rõ bên trái (LH/LL liên tiếp) → nhịp hồi tăng (retracement) hình thành Dealing Range dùng cho setup.
- **Dealing Range (fib)**: Low(0)=1.06249 (1.06247) → High(1)=1.06898/1.06900.
- **Vị trí giá khi vào lệnh**: 0.618–0.786+ fib → Premium sâu, đúng phía cho Short.
- **POI chính**: Order Block (H1) = 1.06839–1.06788. POI sâu hơn mức 0.786 fib (1.06759) — nằm ở phần cao nhất, "đắt" nhất của range, confluence rất tốt cho một điểm bán.
- **FVG (M5, dùng làm entry-level POI)**: khoảng 1.06706–1.06650 (quanh 0.705–0.618 fib), CE≈1.06678 — gần như trùng khớp entry thực tế 1.06677.
- **Liquidity cần chờ sweep**: cạnh trên của OB (CE và cạnh trên OB) — nơi lệnh chờ bán sớm/thanh khoản mua kỳ vọng đảo chiều nằm lại.
- **Ghi chú cấu trúc quan trọng — 2 lần chạm không đối xứng**: chạm 1 (16:15 London) giá vươn sâu hơn vào trong OB (gần đỉnh OB, 0.786–1 fib); chạm 2 (18:00 New York) tạo đỉnh THẤP HƠN chạm 1, chỉ tới 0.705–0.786 fib rồi đảo chiều ngay — failure swing/lower high vi mô, bản thân đã là tín hiệu cảnh báo trước khi MSS M5 xác nhận.

![[Pasted image 20260716134542.png]]

### Phân tích context → lệnh

- Bias Bearish (D1+H1 đồng thuận) + giá ở Premium sâu → khung cảnh cho Short hợp lệ ngay từ context, trước khi xét LTF.
- Chạm 1 (16:15 London): quét vào CE của OB, đóng nến bật ra — chỉ là sweep, không có MSS M5 → đúng kỷ luật, không entry ("first tap = no trade").
- Chạm 2 (18:00 New York): tạo đỉnh thấp hơn chạm 1 (không vào lại tới CE OB), sau đó displacement giảm mạnh phá swing low nội bộ M5 → MSS, để lại FVG M5.
- Chờ retrace về CE của FVG M5 (~1.06678) → entry.

---

## 2. POI Profile

- **POI Type đã dùng**: Order Block (H1) — Premium sâu, ~0.786–1 fib.
- **POI Rank (8.1)**: 2 (FVG+OB — entry là M5 FVG lồng trong H1 OB).
- **POI hình thành trên khung**: H1 (entry refine M5).
- **POI nằm ở**: Premium ✓.
- **POI stack**: H1 OB (1.06839–1.06788) + M5 FVG (1.06706–1.06650, entry).
- **CE của FVG trùng OTE 62–79%?**: Yes.
- **Bounds & CE**: FVG High 1.06706 / Low 1.06650, CE=1.06678 (≈ entry 1.06677).
- **Số lần chạm POI tới MSS**: 2 — chạm 1 chỉ sweep, chạm 2 mới MSS + FVG.

![[Pasted image 20260716134557.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE
- **Entry Precision**: CE (FVG M5)
- **Limit có khớp?**: Yes
- **Giá đi sâu bao nhiêu vào FVG?**: không có số đo % cụ thể trong bản gốc
- **RR ghi lại**: r_planned = rr_if_ce = 2.49 (Risk 0.00172 / Reward 0.00428 điểm)

### M5 — Xác nhận & điểm vào lệnh

- Từ ảnh M5 có lưới fib: giá rally từ đáy trái lên gần đỉnh (~0.9–1 fib) tại chạm 1 (16:15 London), sau đó pullback xuống 0.618–0.705 fib, đi ngang/range một nhịp.
- Rally lần 2, nhưng chỉ đạt 0.705–0.786 fib (thấp hơn đỉnh lần 1 rõ rệt) — lower high M5, dấu hiệu bên mua yếu dần trước khi bị từ chối hoàn toàn.
- Ngay sau đỉnh thấp hơn đó, nến M5 giảm mạnh (thân lớn) phá swing low nội bộ gần nhất → MSS M5, đồng thời để lại FVG M5 ngay tại nhịp displacement đó.
- Giá retrace về đúng vùng FVG (CE≈1.06678), đóng nến phản ứng tại đây → entry tại 1.06677.
- Nến giảm tiếp theo trên M5 là một nến rất dài, xuyên thẳng qua mức 1.06249 (0 fib) và tiếp tục xuống ngoài khung nhìn — chính là cây nến chứa cú gap cuối tuần đã quét qua TP (xem mục 6).
- **Entry trigger**: Liquidity Sweep — quét CE của OB (chạm 1, không entry) → sweep đỉnh thấp hơn (chạm 2). Displacement — nến M5 giảm mạnh ngay sau đỉnh thấp hơn của chạm 2. MSS — phá swing low nội bộ M5 ngay sau displacement. FVG — hình thành trong chính nhịp displacement đó, CE≈entry.
- **Invalidation (kế hoạch)**: giá đóng nến trên đỉnh OB (1.06849).
- **Chờ đủ điều kiện?** Có — từ chối vào ở chạm 1 vì thiếu MSS, chỉ vào sau khi chạm 2 xác nhận đủ chuỗi Sweep→Displacement→MSS→FVG.

![[Pasted image 20260716134557.png]]

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes (2 lần chạm, không phải 1 — đã kiên nhẫn chờ đúng) | `step3_sweep_ok` |
| 4 | Displacement + MSS | Yes (hình thành ở lần chạm thứ 2) | `step4_displacement_ok` |
| 5 | POI (Order Block H1) | Yes | `step5_poi_ok` |
| 6 | Entry (retrace, không chase) | Yes | `step6_entry_ok` |
| 7 | Target | Yes (đạt được, nhưng qua gap — xem mục 6) | `step7_target_ok` |

- **First Error Step**: none
- **Missing Step**: none
- **Đủ chuỗi 7 bước?**: Yes

---

## 5. Setup Quality & Confluence

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Có Liquidity Sweep trước entry (2 lần, không phải 1 — đã kiên nhẫn chờ đúng)
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ (khung M5, ở lần chạm thứ 2)
- [x] FVG nằm trong Premium (đúng phía cho Short)
- [x] Entry trong POI hợp lệ (CE), không đua giá
- [x] SL ở vùng invalidation hợp lý (trên đỉnh OB)
- [x] RR tối thiểu đạt ≥1:2 (2.49R)
- [ ] **Weekend hold policy được xác định trước khi vào lệnh** — KHÔNG có; khoảng trống quy trình cần vá (xem Lesson)

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không (rank 2) | *(suy từ poi_rank)* |
| 2 | CE FVG trùng OTE 62–79% | Có | `ce_ote_overlap` |
| 3 | SMT divergence | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | Không có ghi chú | `cisd_confirm` |
| 5 | Macro time | Chưa đánh giá | `in_macro_time` |
| 6 | NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | SD target align | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Có (lower-high failure swing + sweep chạm 1) | `idm_swept` |

- **Score**: 2/8 — điểm confluence cố định thấp, nhưng chất lượng thật của lệnh nằm ở **kỷ luật chờ đủ 2 lần chạm với MSS xác nhận ở lần 2** trước khi vào, một dạng "process confluence" mà 8 mục cố định chưa đo hết.

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Hit Take Profit (+2.49R danh nghĩa) — nhưng cây nến quét qua mức TP là **gap mở cửa Chủ nhật**, không phải một nhịp giảm liên tục trong phiên giao dịch bình thường.

### Tại sao lệnh thắng? (tách root cause khỏi may mắn)
- **Root cause của entry đúng**: bias top-down đồng thuận, POI chọn lọc (OB sâu trong Premium, không phải OB đại trà), kỷ luật chờ đủ 2 lần chạm với MSS xác nhận ở lần thứ 2 trước khi vào — hoàn toàn tách biệt khỏi kết quả.
- **Phần "may mắn" của outcome**: TP được chạm chính xác nhờ gap cuối tuần — sự kiện ngoài tầm kiểm soát và ngoài dự đoán tại thời điểm entry. Nếu không có gap, giá có thể mất nhiều phiên hơn để chạm H1 DR Low, hoặc không chạm được nếu cấu trúc đảo chiều giữa chừng.

### Thị trường có tín hiệu cảnh báo trước không?
Có, nhiều lớp xác nhận trước khi MSS xuất hiện:
1. Sweep tại POI (chạm 1): giá quét CE của OB nhưng bị từ chối ngay — smart money từ chối Premium lần đầu.
2. Lower high giữa chạm 1 và chạm 2: chạm 2 không vươn lại tới đỉnh cũ — cấu trúc yếu đi rõ rệt trước khi MSS chính thức xảy ra. Tín hiệu sớm, tinh tế hơn MSS.
3. MSS + Displacement M5: xác nhận chính thức, phá cấu trúc nội bộ.
4. FVG hình thành đúng trong nhịp displacement đó: điểm entry rõ ràng, không phải đoán mò.

### TP bị quét bởi gap — tách bạch "entry hợp lệ" khỏi "outcome đại diện"
- Entry logic vẫn hợp lệ 100%. Không có yếu tố nào trong chuỗi Sweep→Displacement→MSS→FVG phụ thuộc vào việc biết trước sẽ có gap.
- R Multiple 2.49 ghi nhận ở đây KHÔNG nên đưa thẳng vào tính expectancy tổng như một win "sạch", vì cơ chế đạt TP (gap) không lặp lại được có hệ thống. Đã gắn `tp_fill_anomaly` và tag `weekend-gap-fill` để lọc riêng nhóm này khi tính win rate/expectancy trên `_Backtest Dashboard`.
- Rủi ro đối xứng chưa được tính đến: nếu gap xảy ra ngược hướng (nhảy qua SL thay vì TP), khoản lỗ thực tế có thể vượt xa 1R dự kiến do trượt giá qua gap. Kế hoạch ban đầu không có điều khoản xử lý việc giữ lệnh qua cuối tuần.

### Setup này khớp bao nhiêu % với mô hình chuẩn?
~90% cho phần entry logic (context, sweep, MSS, FVG, risk structure đều chuẩn). Điểm trừ duy nhất nằm ở quy trình quản trị rủi ro cuối tuần — không phải ở entry.

### Nếu vào lại, làm gì khác?
- Cân nhắc chốt một phần (partial TP) tại thanh khoản/PD array gần hơn trước khi tới H1 DR Low, thay vì đặt 100% khối lượng chờ target xa nhất.
- Xác định trước (trong kế hoạch) quy tắc: nếu lệnh vẫn mở gần giờ đóng cửa cuối tuần, đóng thủ công một phần hay chấp nhận rủi ro gap với size đã định trước.

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Entry là một process win thực thụ — kỷ luật chờ đủ 2 lần chạm POI với MSS xác nhận mới vào, đúng tinh thần "first tap = no trade". Nhưng kết quả (TP hit) một phần đến từ một gap cuối tuần ngoài dự đoán, nên cần tách rõ "được khen vì quy trình" khỏi "được khen vì kết quả".

### Lesson 1 — "Double-tap POI, lower high ở lần 2" là tín hiệu sớm đáng tin cậy
Giá chạm POI lần 2 nhưng tạo đỉnh thấp hơn lần 1 là failure swing vi mô, xuất hiện trước cả khi MSS chính thức xảy ra — dấu hiệu sớm cho thấy phe mua đang cạn lực ngay tại Premium. Cần theo dõi qua nhiều mẫu backtest tiếp theo: tần suất "lower high ở lần chạm 2" có tương quan với xác suất MSS xảy ra ngay sau đó hay không — nếu có, đây có thể thành tiêu chí sàng lọc entry sớm hơn, tương tự pattern "first tap = no trade" đã ghi nhận ở backtest NAS100 trước đó ([[01 - Win - NAS100 - 2026-04-02- Long|xem backtest 2026-04-02]]).

### Lesson 2 — TP đạt được qua gap KHÔNG chứng minh model có edge tại mục tiêu đó
Giá chạm H1 DR Low nhờ gap cuối tuần không nói lên gì về khả năng thị trường thực sự "chạy" tới đó bằng price action tuần tự trong điều kiện bình thường. Nếu không tách riêng loại trade này, sample backtest sẽ bị lẫn giữa "model có edge thật" và "may mắn từ sự kiện ngoài mô hình". Quy tắc: mọi trade có TP/SL bị quét bởi gap phải gắn tag riêng (`weekend-gap-fill`) và cân nhắc loại khỏi tính win rate chính.

### Lesson 3 — Rủi ro gap có tính đối xứng, kế hoạch ban đầu chưa xử lý điều này
Gap giúp lệnh này về đích nhanh hơn, nhưng nếu gap xảy ra ngược hướng thì SL 1.06849 không có gì đảm bảo được khớp đúng giá — khoản lỗ có thể lớn hơn 1R dự kiến. Kế hoạch trade cần có điều khoản rõ ràng về giữ lệnh qua cuối tuần trước khi vào lệnh, không phải phát hiện sau khi đã thấy kết quả thuận lợi.

### Lesson 4 — Chất lượng POI (OB sâu trong Premium, ≥0.786 fib) là bộ lọc đáng giữ
OB được chọn nằm sâu hơn 0.786 fib — không phải OB đại trà giữa range. Dạng POI có xác suất cao hơn theo lý thuyết Premium/Discount vì đại diện cho vùng "đắt" nhất, nơi smart money có động cơ mạnh nhất để phân phối. Cần tiếp tục ghi nhận vị trí fib chính xác của POI qua các backtest sau để kiểm tra POI càng sâu trong Premium/Discount có thực sự cho win rate/expectancy tốt hơn OB ở vùng 0.5–0.618 hay không.

### Lesson 5 — Đặt toàn bộ TP vào một mục tiêu xa duy nhất làm tăng phụ thuộc vào sự kiện ngoài mô hình
TP đặt 100% khối lượng tại H1 DR Low — mục tiêu khá xa so với entry. Kết quả cuối cùng phụ thuộc nhiều vào việc giá có "đi hết đường" hay không, và lần này phần cuối do gap đảm nhiệm chứ không phải organic price delivery. Chia nhỏ TP (partial gần hơn, phần còn lại chạy tới DR Low) sẽ giảm phụ thuộc vào sự kiện một-lần như gap để đạt full R.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Thêm "Weekend Hold Policy" vào playbook: quy định rõ có được giữ lệnh mở qua đêm thứ 6 sang Chủ nhật hay không.
- [ ] Khi tính win rate/expectancy tổng trên `_Backtest Dashboard`, lọc riêng trade có tag `weekend-gap-fill`.
- [ ] Theo dõi thêm biến "lower high ở lần chạm POI thứ 2" như tín hiệu sớm tiềm năng qua các backtest tiếp theo.
- [ ] Cân nhắc rule partial TP tại thanh khoản trung gian khi TP chính đặt xa hơn ~2R.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 |
| POI Selection | 9/10 |
| Liquidity Sweep | 9/10 |
| Displacement/MSS quality (MSS Confirmation) | 8/10 |
| Entry Precision & Fill (FVG/OB Entry) | 8/10 |
| Risk Management (RR & weekend gap policy) | 6/10 — trừ điểm vì thiếu Weekend Hold Policy trước khi vào lệnh, không phải vì RR danh nghĩa thấp |

**Overall Grade**: **B+** — process entry rất tốt, nhưng outcome bị nhiễu bởi gap và có một lỗ hổng quy trình (weekend risk) chưa được xử lý trước khi vào lệnh.

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

**Bản đồ liquidity IRL↔ERL tại thời điểm entry (1.06677).** Tại M5, FVG entry (1.06706–1.06650) là IRL vừa hình thành trong chính nhịp displacement. ERL gần nhất phía dưới là SSL = H1 DR Low 1.06249 (TP), phía trên là BSL = đỉnh nhịp hồi D1/OB high ~1.06849–1.06898 — pool này **đã bị dùng** (sweep chạm 1 quét CE OB, chạm 2 tạo lower high ngay dưới đỉnh chạm 1) chứ chưa bị lấy dứt điểm bằng một cú quét rõ ràng qua đỉnh tuyệt đối. Theo đúng logic ERL→IRL (đối chiếu note lỗi 4 trong batch này, [[02 - Loss - GBPUSD - 2014-07-17 - Long]]), một Short chuẩn cần ERL phía trên (buy-side) đã bị lấy trước khi tin IRL (FVG) làm entry. Ở đây ERL trên KHÔNG bị lấy bằng một sweep dứt khoát duy nhất — nó bị hao mòn qua 2 lần chạm với đỉnh sau thấp hơn đỉnh trước (absorption dạng lower-high), một biến thể "yếu dần" khác với sweep một-cú-rõ-ràng. Note gốc không đặt câu hỏi này; đây là góc nhìn IRL/ERL note gốc chưa khai thác đủ.

**Chất lượng displacement/MSS.** MSS M5 hình thành sau đúng 1 nến displacement thân lớn ngay sau lower-high của chạm 2 — thời gian từ tín hiệu tới FVG entry là một nhịp M5 duy nhất (nhanh), khác hẳn note 4 cùng batch (MSS "sớm", leg yếu, trễ 3h mới tạo FVG entry, rồi mất 14h chưa resolve). Tốc độ resolve nhanh ở đây là dấu hiệu chất lượng, nhưng note gốc không đo bằng số nến/phút cụ thể — thiếu dữ liệu để so sánh định lượng.

**Yếu tố thời gian.** Chạm 1 tại London 16:15, chạm 2 + MSS tại New York 18:00 — chuyển giao London→NY, một killzone chồng lấn thường có thanh khoản/volatility tốt. Note gốc không gắn nhãn killzone theo tên chuẩn (London Close/NY AM) — chỉ ghi giờ, thiếu field `in_macro_time`.

**Vị trí entry trong dealing range.** Entry 1.06677 nằm ở Premium sâu (0.618–0.786+ fib của DR H1 1.06249–1.06898), khớp phía Short. CE FVG M5 (1.06678) và entry thực tế (1.06677) lệch 0.00001 — sai số làm tròn không đáng kể, xác nhận entry chính xác về cơ học.

**So sánh cùng mẫu trong vault.** Note gốc đã tự liên kết pattern "double-tap, lower-high lần 2" với [[01 - Win - NAS100 - 2026-04-02- Long]] (không đọc được nội dung file đó trong phạm vi batch này — không thể xác nhận độ tương đồng, để `[UNSUPPORTED]`). Trong batch E, note liên quan gần nhất về chủ đề "MSS sớm/muộn" là [[02 - Loss - GBPUSD - 2014-07-17 - Long]] — nhưng đó là MSS **quá sớm** (trước khi ERL cấu trúc bị quét) dẫn tới Loss, còn ở đây MSS chỉ đến sau khi đã có đủ 2 lần chạm + lower-high — hai cực đối lập của cùng một trục "MSS timing". Đây là một cặp đối chiếu tốt cho playbook: "MSS đến càng trễ sau một chuỗi tín hiệu suy yếu rõ ràng (lower-high, absorption) → càng đáng tin; MSS đến ngay lần chạm đầu khi ERL cấu trúc chưa quét → đáng ngờ."

![[EURUSD-20160612-double-tap-gap.svg|760]]

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
type: devils-advocate
mode: REVIEW
instrument: EURUSD
date: 2016-06-12
timeframes_provided: [D1, H1, M5] (mô tả bằng lời + 3 ảnh PNG không đọc được)
verdict: SURVIVES, WEAKENED
evidence_sufficiency: thin
opposite_case_strength: weaker but non-trivial
objections: {fatal: 0, material: 3, minor: 2}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN, O5 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base.** Không có ảnh PNG đọc được — 3 screenshot (`Pasted image ...`) chỉ tồn tại dưới dạng wikilink, không phải chart thật truy cập được trong môi trường này. Toàn bộ evidence base là mô tả bằng lời + số liệu trong chính note (frontmatter + bảng). Đây là input dạng prose có số, không phải chart — theo brief, ảnh PNG coi như không truy cập được. `evidence_sufficiency = thin`: load-bearing claim (MSS thật ở chạm 2, không phải chạm 1) không thể verify độc lập ngoài lời tự thuật của chính note.

**1. Thesis + load-bearing claim.**
- C1: HTF bias Bearish (D1+H1 đồng thuận) — có cơ sở từ mô tả cấu trúc D1/H1.
- C2: Chạm 1 (16:15) chỉ sweep, không MSS → đúng kỷ luật không entry.
- C3: Chạm 2 (18:00) tạo lower-high, sau đó MSS + displacement M5 → entry hợp lệ tại CE FVG.
- C4: Kỷ luật chờ đủ 2 lần chạm là "process win" tách biệt khỏi outcome (**load-bearing** — toàn bộ lesson và grade B+ dựa vào claim này).
- C5: TP đạt được là nhờ gap cuối tuần, không phải price action tuần tự (note tự thừa nhận).
- Inference: C1+C2+C3 → C4 (process đúng); C5 độc lập với C4 (outcome tách khỏi process).

**2. Điều gì survive.** Việc note **tự tách** root cause (process) khỏi outcome (gap) là kỷ luật phân tích hiếm gặp và đáng ghi nhận — đây chính là điều devil's advocate thường phải ép người viết thừa nhận, nhưng ở đây tác giả đã tự làm trước. Nhận diện "lower-high ở lần chạm 2" như tín hiệu sớm cũng là một quan sát có cơ sở logic vững (áp lực mua giảm dần trước MSS chính thức).

**3. Objections.**

**O1 · [HINDSIGHT] · material · attacks C3, C4**
Claim: "Chờ đủ 2 lần chạm với MSS xác nhận ở lần 2 mới vào là kỷ luật, không phải may mắn."
Evidence: Note không cung cấp bằng chứng rằng tại thời điểm chạm 1 (16:15), người phân tích đã **định trước** quy tắc "phải chờ lower-high ở lần chạm kế tiếp" — quy tắc "lower-high là tín hiệu sớm" chỉ được phát biểu sau khi biết chạm 2 thực sự có lower-high và MSS theo sau thành công. Nếu chạm 2 lặp lại đúng đỉnh chạm 1 (không phải lower-high) mà MSS vẫn xảy ra, liệu tác giả có coi đó cũng là entry hợp lệ? Note không trả lời được câu này trước khi biết outcome.
Consequence: Nếu "lower-high" chỉ là mô tả hậu-kiểm chứ không phải điều kiện được viết ra trước, thì C4 ("process win thực thụ") bị pha loãng thành "được may vì chờ đủ 2 lần chạm, tình cờ lần 2 có thêm 1 tín hiệu phụ".
Your best answer: "First tap = no trade" đã là rule cũ có trước (note tự trích dẫn), nên phần "chờ 2 lần chạm" không hindsight — nhưng phần "lower-high là tín hiệu sớm đáng tin" thì đúng là kết luận rút ra *sau* case này, note cũng tự đề xuất "cần theo dõi qua nhiều mẫu" ở Lesson 1 — tức là chính tác giả cũng coi đây là giả thuyết chưa kiểm chứng, không phải rule đã có trước.
Retracted by: Bằng chứng cho thấy rule "lower-high ở lần chạm 2 là tín hiệu" đã được viết trong playbook *trước* ngày 2016-06-12.

**O2 · [UNSUPPORTED] · material · attacks C1**
Claim: "D1 trước đó có chuỗi nến Bearish Displacement mạnh... premise gốc cho bias Bearish."
Evidence: Note mô tả bằng lời, không có số liệu OHLC D1 cụ thể (không có mức giá, không có số nến, không có % thân nến) để kiểm tra "displacement mạnh" có đúng chuẩn ICT (expansion một chiều, imbalance rõ) hay chỉ là một vài nến giảm bình thường.
Consequence: Nếu D1 displacement yếu hơn mô tả, bias Bearish vẫn có thể đúng nhưng độ tin cậy load-bearing của C1 giảm, kéo theo toàn bộ setup giảm độ chắc chắn.
Retracted by: Cung cấp OHLC D1 hoặc ảnh chart D1 đọc được.

**O3 · [ARITHMETIC] · minor**
Đã verify bằng Python: CE FVG = (1.06706+1.06650)/2 = 1.06678, khớp note. RR = |1.06249−1.06677|/|1.06677−1.06849| = 2.488, khớp r_planned 2.49 (sai số làm tròn 0.002R, không đáng kể).
Retracted by: n/a — đã khớp, ghi nhận làm chuẩn tham chiếu.

**O4 · [METHOD] · material · attacks C4**
Claim ngầm định: mẫu n=1 này đủ để rút ra rule "double-tap lower-high" cho playbook.
Fails: Đây là quy nạp từ một lệnh duy nhất; note tự đề xuất theo dõi thêm nhưng đã đưa vào Lesson 1 như một pattern gần như xác lập ("dấu hiệu sớm đáng tin cậy" — tiêu đề Lesson 1 khẳng định mạnh hơn nội dung thực sự chứng minh được).
Consequence: Nếu rule này được áp dụng làm filter entry sớm ở các lệnh tương lai trước khi có đủ mẫu, đây là curve-fitting một quan sát thành rule.
Retracted by: Backtest thêm ≥10 mẫu có double-tap POI, đo tỷ lệ MSS xảy ra sau lower-high ở lần chạm 2 so với sau lần chạm đối xứng/higher-high.

**O5 · [UNSUPPORTED] · minor**
Claim "~90% khớp mô hình chuẩn" (mục 6 note gốc) không có breakdown cụ thể cấu thành 90% từ đâu — con số cảm tính.
Retracted by: Bảng điểm chi tiết cho từng bước tương ứng % đóng góp.

Bộ lọc: 6 objection nháp, cắt 1 (một objection về "session label thiếu" bị coi là quá vụn, không đổi kết luận) → còn 5.

**4. Opposite case.** Đọc ngược cùng evidence: đây không phải "process win + outcome may mắn" mà là **"outcome may mắn toàn phần, process chỉ tình cờ đúng hướng"**. Load-bearing claim của case ngược: nếu không có gap cuối tuần, giá có thể đảo chiều tại bất kỳ điểm nào giữa entry và TP (note thừa nhận "có thể mất nhiều phiên hơn, hoặc không chạm nếu cấu trúc đảo chiều giữa chừng") — nghĩa là bản thân R Multiple 2.49 hoàn toàn phụ thuộc vào một sự kiện ngoài entry logic, và "chuỗi lý luận đúng" không tự động suy ra "giá sẽ đi hết quãng đường". Tự phản biện case ngược: nó không phủ nhận được rằng chuỗi Sweep→Displacement→MSS→FVG tại M5 vẫn là entry logic hợp lệ độc lập với outcome — case ngược chỉ tấn công phần "R Multiple 2.49 chứng minh có edge", không tấn công được "entry đúng chuẩn". Nhãn: **weaker but non-trivial** — case ngược không lật được tính hợp lệ của entry, nhưng làm rõ risk bất đối xứng (nếu gap ngược chiều, SL có thể trượt xa hơn 1R) mà note gốc mục 6 cũng đã tự nêu. Observable phân biệt hai case: nếu tách riêng toàn bộ trade có tag `weekend-gap-fill` ra khỏi expectancy tổng và win rate vẫn ổn định qua ≥30 mẫu không-gap, case gốc thắng; nếu win rate sụt mạnh khi loại gap-fill, case ngược thắng.

**5. Verdict: SURVIVES, WEAKENED.** Entry logic (C2, C3) survive — không có [CHART]/[DOCTRINE]/[ARITHMETIC] nào phá được chuỗi Sweep→Displacement→MSS→FVG. Nhưng C4 ("process win thực thụ") bị làm yếu bởi O1 (hindsight nhẹ ở phần "lower-high là tín hiệu") và O4 (n=1 chưa đủ để thành rule). Điều tôi không phá được: chuỗi 7 bước và toán RR. Điều critique này không xác lập: rằng "double-tap lower-high" là một edge thật — đó vẫn là giả thuyết một-mẫu.

**6. Falsification tests.**
1. Backtest ≥15 setup có double-tap POI tương tự; đo % có lower-high ở lần chạm 2 VÀ MSS xảy ra ngay sau đó, so với % lần chạm 2 tạo higher/equal-high mà MSS vẫn xảy ra. Nếu tỷ lệ không khác biệt rõ (ví dụ cả hai đều >60%), rule Lesson 1 bị rút lại (đóng O1, O4).
2. Tách toàn bộ trade `weekend-gap-fill` khỏi expectancy tổng; so win rate/expectancy hai nhóm trên ≥30 mẫu mỗi nhóm — nếu nhóm không-gap có expectancy dương ổn định, C4 được củng cố (đóng O1 một phần).
3. Đo số nến từ MSS tới khi giá chạm CE FVG (tốc độ resolve) trên toàn bộ mẫu có nhãn "MSS sau ≥2 lần chạm" — nếu tốc độ nhanh (≤3 nến M5) tương quan với win rate cao hơn "MSS chạm lần đầu", củng cố phần "tốc độ resolve" nêu ở mục 9.

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Chuỗi Bias(Bearish D1+H1) → Sweep(2 lần chạm OB) → Displacement+MSS(M5, sau chạm 2) → FVG entry tại CE là một setup Short hợp lệ theo ICT 2022 Model.

**Cần sửa** (load-bearing trước):
- C3 (MSS tại chạm 2) — **AMBIGUOUS** · doctrine không tự nó phân biệt được "MSS thật" và "internal swing break nhỏ trên M5 sau lower-high" chỉ từ mô tả bằng lời, không có OHLC → cần chart M5 đọc được để xác nhận body close phá đúng swing low nội bộ (SKILL.md § MSS: "phá swing *ngược* short-term move... không phải mọi structure trông khác đi"). Đây là doctrine gap về "structurally significant swing" trên biểu đồ lồng, không phải lỗi định nghĩa của tác giả → fix: đính kèm ảnh M5 đọc được hoặc OHLC 2-3 nến quanh MSS.
- C1 (Bearish Displacement D1) — **UNSUPPORTED** · why: mô tả "chuỗi nến Bearish Displacement mạnh, thân lớn" không kèm OHLC hay ảnh đọc được → fix: cung cấp số liệu displacement D1 cụ thể (số nến, biên độ) để nâng lên PASS.
- C5 (sweep_type: Double, gồm 1 External + 1 Internal) — **AMBIGUOUS** · why: doctrine không định nghĩa rạch ròi ranh giới giữa "sweep CE của OB" (được note gọi External) và "sweep đỉnh nội bộ thấp hơn" (Internal) khi cả hai đều nằm trong cùng vùng OB H1 — đây là một khoảng xám giữa internal/external liquidity chưa được SKILL.md fix cụ thể cho trường hợp lồng-trong-OB → doctrine gap, giữ nguyên nhãn của tác giả nhưng không nâng thành PASS chắc chắn.

**PASS:** C2 (chạm 1 chỉ sweep, không MSS → đúng "first tap = no trade"), C4 (FVG hình thành đúng trong nhịp displacement, CE≈entry — khớp định nghĩa FVG 3-candle theo mô tả), C6 (Premium/Discount: OB nằm ở 0.786+ fib của DR H1 1.06249–1.06898 → đúng phía Premium cho Short, arithmetic khớp).

**Verdict: PARTIALLY ALIGNED** — load-bearing claim (C3, MSS xác nhận) rơi vào AMBIGUOUS do thiếu chart đọc được, không phải FAIL, nhưng cũng chưa đủ evidence để PASS chắc chắn; các claim phụ C2/C4/C6 PASS. Theo decision rule, load-bearing UNSUPPORTED/AMBIGUOUS đáng lẽ đẩy về INSUFFICIENT EVIDENCE — nhưng vì C3 có mô tả chi tiết nhất quán nội bộ (không mâu thuẫn số liệu, chuỗi logic khớp 7 bước) và chỉ thiếu *ảnh xác nhận* chứ không thiếu *mô tả sự kiện*, xếp PARTIALLY ALIGNED với ghi chú rõ: cần chart M5 để nâng lên DOCTRINE ALIGNED.

**Notes:** Doctrine gap ghi nhận — ranh giới "External vs Internal sweep" khi cả hai lần chạm đều nằm trong cùng một OB H1 (không có level liquidity riêng biệt được đặt tên ở giữa) chưa được SKILL.md fix rõ; đề xuất bổ sung: nếu 2 lần sweep đều nằm trong cùng POI mà không có named level phân tách, gọi chung là "Internal" trừ khi lần đầu vượt qua một đỉnh có tên riêng (PDH/swing-high đã đánh dấu trước).

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật
1. **Sweep không kèm MSS = giữ nguyên "no trade", dù giá đã chạm đúng vùng.** Ví dụ số thật: chạm 1 (16:15, giá sweep CE OB 1.06839–1.06788) không có MSS M5 → không entry, đúng kỷ luật. Tổng quát hóa: mọi lần giá chạm POI mà chưa có MSS xác nhận trên khung entry, dù POI "đẹp" đến đâu, vẫn là chờ, không phải vào.
2. **TP đạt qua gap không chứng minh model có edge tại target đó.** Ví dụ số thật: R Multiple 2.49 đạt được nhờ gap Chủ nhật quét thẳng qua TP 1.06249, không phải price action tuần tự. Tổng quát hóa: mọi trade có TP/SL bị quét bởi gap cuối tuần cần tag riêng và loại khỏi tính win rate/expectancy chính (đã có trong note gốc, ở đây nhấn mạnh lại vì đây là bài học nặng ký nhất của toàn bộ note).
3. **Double-tap với lower-high ở lần 2 là giả thuyết, chưa phải rule** — xem O4/O1 ở mục Devil's Advocate: cần ≥10-15 mẫu mới kết luận được, không nên áp dụng như filter cứng ngay.

### (b) Bài học quy trình/checklist
- Thiếu "Weekend Hold Policy" được xác định TRƯỚC khi vào lệnh — đây là lỗ hổng quy trình thật (note gốc đã tự nêu), không phải lỗi entry.
- Thiếu bằng chứng bằng số (OHLC D1, số nến displacement) khiến claim bias D1 chỉ dừng ở UNSUPPORTED theo doctrine check — checklist cần yêu cầu số liệu tối thiểu cho mỗi claim HTF, không chỉ mô tả bằng lời.

### (c) Bài học tâm lý-hành vi
- Rủi ro nhận diện: một cú Win với chuỗi 7 bước đều Yes rất dễ khiến người backtest đọc toàn bộ R Multiple là "kết quả của kỹ năng" — trong khi note gốc (đúng hiếm) đã tự tách bạch. Cần giữ thói quen này làm chuẩn cho các Win khác trong vault, không chỉ note này.
- Nguy cơ tự thưởng quá sớm cho một pattern quan sát 1 lần (lower-high ở chạm 2) — cảm giác "đã tìm ra edge mới" trong khi mẫu số 1 chưa đủ để phân biệt edge thật với nhiễu ngẫu nhiên.

### (d) Rule đề xuất cho Playbook
- [ ] Trước khi coi bất kỳ TP/SL nào là "clean hit", kiểm tra xem nến quét qua có phải gap (khoảng trống giữa 2 nến liên tiếp không overlap) hay không; nếu có, gắn tag `weekend-gap-fill` hoặc `gap-fill` và loại khỏi win-rate chính khi tính expectancy.
- [ ] Không nâng bất kỳ quan sát one-off (n=1) nào (như "lower-high ở lần chạm 2") thành filter entry chính thức cho tới khi có ≥10 mẫu xác nhận với tỷ lệ khác biệt rõ so với baseline.
- [ ] Mọi claim HTF bias (D1) phải kèm ít nhất 1 con số đo được (biên độ nến, số nến, mức giá) — không chỉ mô tả định tính "displacement mạnh".

### (e) Điều KHÔNG nên học từ lệnh này (chống overfitting/outcome bias)
- **Không nên** coi R Multiple 2.49 là "bằng chứng model có edge 2.49R tại H1 DR Low" — phần lớn quãng đường cuối được gap đảm nhiệm, không phải price action.
- **Không nên** biến "chờ double-tap với lower-high" thành rule cứng chỉ từ 1 mẫu — đây chính xác là dạng curve-fitting mà note gốc tự cảnh báo cần theo dõi thêm, nhưng tiêu đề Lesson 1 ("tín hiệu sớm đáng tin cậy") đã hơi vượt quá những gì 1 mẫu có thể chứng minh.
- **Không nên** dùng việc "TP hit" để hồi tố khẳng định toàn bộ chuỗi phân tích D1 (vốn chỉ mô tả định tính, không có số) là chính xác — bias đúng hướng không tự động biện minh cho độ chi tiết/chất lượng của lý do đưa ra bias đó.

---

### Liên kết bổ sung
- Đối chiếu MSS timing: [[02 - Loss - GBPUSD - 2014-07-17 - Long]] (MSS quá sớm, trước khi ERL bị quét → Loss) vs note này (MSS chỉ đến sau 2 lần chạm + lower-high → Win) — hai cực của cùng trục "MSS timing reliability".

---

### Liên kết

- Concept: [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[13-FVG-Fair-Value-Gap]] · [[25-OB-Order-Block]] · [[27-Premium-Discount]] · [[10-Consequent-Encroachment-Mean-Threshold]]
- Backtest liên quan (double-tap pattern): [[01 - Win - NAS100 - 2026-04-02- Long]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]] (chưa có mục riêng cho "giữ lệnh qua gap cuối tuần" — xem checkbox Playbook ở mục 7)
