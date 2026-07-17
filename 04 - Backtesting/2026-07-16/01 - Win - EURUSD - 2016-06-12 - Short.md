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

### Liên kết

- Concept: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]] · [[27 - Premium Discount]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- Backtest liên quan (double-tap pattern): [[01 - Win - NAS100 - 2026-04-02- Long]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]] (chưa có mục riêng cho "giữ lệnh qua gap cuối tuần" — xem checkbox Playbook ở mục 7)
