---
type: backtest
backtest_date: 2026-07-16
trade_date: 2016-06-12
symbol: EURUSD
position: Short
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[25 - OB - Order Block|Order Block]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.06677
stop_loss: 1.06849
take_profit: 1.06249
entry_type: CE
r_planned: 2.49
rr_if_ce: 2.49
r_multiple: 2.49
grade: B+
followed_plan: Yes
touch_count_to_mss: 2
mss_touch_detail: MSS M5 hình thành ở lần chạm OB thứ 2 (~18:00 New York). Lần chạm 1 (~16:15 London) chỉ sweep CE của OB rồi bật ra, KHÔNG có MSS → không entry.
tp_fill_anomaly: TP bị quét bởi 1 gap cuối tuần (Chủ nhật), không phải bởi price action tuần tự — xem mục 4 & Lesson 2/3.
tags:
  - backtest
  - ICT2022
  - weekend-gap-fill
  - double-tap-poi
---

# Backtest 2016-06-12 — EURUSD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. POI là **H1 Order Block nằm sâu trong Premium**, entry tại **CE của FVG M5** sau khi POI bị chạm **2 lần** (lần 1 chỉ sweep, lần 2 mới tạo MSS). Setup này có một chi tiết đặc biệt cần mổ xẻ: TP bị quét bởi **gap cuối tuần** chứ không phải bởi price action liên tục — xem mục 4 để tách bạch "entry hợp lệ" khỏi "kết quả có đại diện cho edge hay không".

> [!important] Kết quả tóm gọn
> Giá retrace vào H1 OB (Premium sâu, 0.705–1.0 fib), bị sweep 2 lần. Lần chạm thứ 2 tạo **Displacement + MSS khung M5**, để lại FVG. Entry tại **CE của FVG M5 (≈1.06677)**, SL trên đỉnh OB (1.06849), TP tại H1 Dealing Range Low (1.06249). Giá **hit TP (+2.49R)**, nhưng cây nến quét qua TP là **gap mở cửa Chủ nhật**, không phải một nhịp giảm tuần tự trong phiên.

---

## 0. Backtest Summary

| Field                     | Value                                                  |
| ------------------------- | ------------------------------------------------------- |
| Symbol                    | EURUSD                                                  |
| Trade Date (dữ liệu)      | 2016-06-12 (giờ UTC+7)                                  |
| Position                  | Short                                                    |
| Result                    | Win (Hit TP — **qua gap cuối tuần**, xem mục 4)          |
| Session                   | London (chạm 1, 16:15) → New York (chạm 2 + entry, 18:00) |
| Setup                     | ICT 2022 Model                                          |
| Entry Model               | HTF OB POI (Premium) + LTF Sweep/Displacement/MSS/FVG    |
| Entry Timeframe           | M5 (CE của FVG M5)                                       |
| HTF Bias                  | Bearish (D1 + H1 đồng thuận)                            |
| Bias Correct?             | Yes                                                      |
| POI chính (H1)            | Order Block 1.06839 – 1.06788 (Premium sâu, ~0.786–1 fib) |
| POI entry (M5)            | FVG ≈ 1.06706 – 1.06650, CE ≈ 1.06678                    |
| Số lần chạm POI tới MSS   | **2** (chạm 1 = sweep only; chạm 2 = MSS + FVG)          |
| Entry                     | 1.06677 (≈ CE của FVG M5)                                |
| Stop Loss                 | 1.06849 (trên đỉnh OB)                                  |
| Take Profit               | 1.06249 (H1 Dealing Range Low)                          |
| Risk (points)             | 0.00172                                                  |
| Reward (points)           | 0.00428                                                  |
| R Planned                 | 2.49                                                    |
| R Multiple (kết quả)      | 2.49 (danh nghĩa — xem cảnh báo gap ở mục 4)             |
| Entry Type                | CE                                                       |
| Grade                     | B+                                                      |
| Followed Plan?            | Yes                                                      |

> ⚠️ Field mới bổ sung trong frontmatter: `touch_count_to_mss`, `mss_touch_detail`, `tp_fill_anomaly` — dùng để lọc/gắn cờ các trade có kết quả bị ảnh hưởng bởi gap khi tính expectancy tổng trên `_Backtest Dashboard`. Không thay thế field cũ.

---

## 1. HTF Context & Bias

### D1 — Daily Bias & Context

- **Bias**: Bearish
- **Market Condition**: Pullback trong nhịp giảm (retracement lên premium trước khi tiếp tục xuống)
- **Lý do xác định bias (PD array, draw on liquidity)**:
	- Khung D1 trước đó có 1 (hoặc chuỗi) nến **Bearish Displacement mạnh**, thân lớn, để lại dấu vết phân phối rõ ràng — đây là premise gốc cho toàn bộ bias Bearish của setup.
	- Sau nhịp displacement đó, giá bước vào một chuỗi nến hồi (phần lớn là nến tăng) đi ngược lên, đúng như một retracement bình thường trong xu hướng giảm — **không phá vỡ** cấu trúc giảm khung lớn.
	- Nhịp hồi này đưa giá lên vùng cao của range D1, chạm vào vùng Premium (0.705–1.0 fib của dealing range đang xét) — đúng vùng POI đã dùng ở H1.
	- Ngày 12/06/2016 (ngày trade), D1 in ra một nến giảm lớn, đánh dấu điểm giá **từ chối Premium và quay đầu** — đây chính là nến chứa trọn setup H1/M5 bên dưới.
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
	- Buy-side liquidity: đỉnh của nhịp hồi D1 (khớp với đỉnh H1 OB ~1.06849–1.06898) — đã bị từ chối, không phải mục tiêu.
	- Sell-side liquidity: đáy của nhịp giảm D1 trước đó / vùng dưới H1 Dealing Range Low (1.06249) — mục tiêu chính cho Short.

![[Pasted image 20260716134531.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Downtrend rõ ràng bên trái (LH/LL liên tiếp) → sau đó một nhịp hồi tăng (retracement) hình thành **Dealing Range** dùng cho setup.
- **Dealing Range (fib)**: Low (0) = **1.06249 (1.06247)** → High (1) = **1.06898/1.06900**.
- **Vị trí giá khi vào lệnh**: nằm ở vùng **0.618–0.786+ fib → Premium sâu**, đúng phía cho Short.
- **POI chính**: **Order Block (H1)** = 1.06839 – 1.06788. Đây là POI *sâu hơn* mức 0.786 fib (1.06759) — tức nằm ở phần cao nhất, "đắt" nhất của range, confluence rất tốt cho một điểm bán.
- **FVG (M5, dùng làm entry-level POI)**: khoảng 1.06706 – 1.06650 (quanh 0.705–0.618 fib), CE ≈ **1.06678** — gần như trùng khớp với entry thực tế 1.06677.
- **Liquidity cần chờ sweep**: cạnh trên của OB (CE và cạnh trên OB) — nơi các lệnh chờ bán sớm / thanh khoản mua kỳ vọng đảo chiều nằm lại.
- **Ghi chú cấu trúc quan trọng — 2 lần chạm không đối xứng**: lần chạm 1 (16:15 London) giá vươn *sâu hơn* vào trong OB (gần đỉnh OB, khu vực 0.786–1 fib); lần chạm 2 (18:00 New York) tạo một **đỉnh THẤP HƠN** lần 1, chỉ tới vùng 0.705–0.786 fib rồi đảo chiều ngay. Đây là một **failure swing / lower high** vi mô — bản thân nó đã là tín hiệu cảnh báo trước khi MSS M5 xác nhận, chứ không phải MSS là tín hiệu duy nhất.

![[Pasted image 20260716134542.png]]

### Phân tích context → lệnh

- Bias Bearish (D1 + H1 đồng thuận) + giá đang ở Premium sâu của Dealing Range → khung cảnh cho Short hợp lệ ngay từ context, trước khi xét đến LTF.
- Giá retrace lên vùng OB lúc 16:15 (London): quét vào CE của OB, đóng nến bật ra — **đây là chạm lần 1, chỉ là sweep, không có MSS khung M5** → đúng kỷ luật, không entry ("first tap = no trade").
- Giá quay lại retest lần 2 lúc 18:00 (New York): lần này tạo đỉnh thấp hơn lần 1 (không vào lại tới CE OB), sau đó displacement giảm mạnh phá swing low nội bộ khung M5 → **MSS**, để lại **FVG M5**.
- Chờ giá retrace về CE của FVG M5 (~1.06678) → entry.

---

## M5 — Xác nhận & điểm vào lệnh

### Phân tích:

- Từ ảnh M5 có lưới fib: giá rally từ đáy bên trái lên gần đỉnh (~0.9–1 fib) tại lần chạm 1 (16:15 London), sau đó pull back xuống vùng 0.618–0.705 fib, đi ngang/range một nhịp.
- Giá rally lần 2 lên lại, nhưng **chỉ đạt tới vùng 0.705–0.786 fib** (thấp hơn đỉnh lần 1 rõ rệt) — lower high trên M5, dấu hiệu bên mua đang yếu dần trước khi bị từ chối hoàn toàn.
- Ngay sau đỉnh thấp hơn đó, một nến M5 giảm mạnh (thân lớn) phá swing low nội bộ gần nhất → **Market Structure Shift (MSS)** khung M5, đồng thời để lại **FVG M5** ngay tại nhịp displacement đó.
- Giá retrace về đúng vùng FVG này (CE ≈ 1.06678), đóng nến phản ứng tại đây → entry tại **1.06677**.
- Nến giảm tiếp theo trên M5 (nhìn thấy trong ảnh) là một nến rất dài, xuyên thẳng qua mức 1.06249 (0 fib) và tiếp tục xuống dưới ngoài khung nhìn — đây chính là cây nến chứa cú **gap cuối tuần** đã quét qua TP (xem phân tích mục 4).
- **Entry trigger**:
	- Liquidity Sweep: quét CE của OB (chạm 1, không entry) → sweep đỉnh thấp hơn (chạm 2)
	- Displacement: nến M5 giảm mạnh ngay sau đỉnh thấp hơn của chạm 2
	- MSS: phá swing low nội bộ M5 ngay sau displacement
	- FVG: hình thành trong chính nhịp displacement đó, CE ≈ entry
- **Invalidation (theo kế hoạch)**: giá đóng nến trên đỉnh OB (1.06849).
- **Tôi có chờ đủ điều kiện không?** Có — từ chối vào ở chạm 1 vì thiếu MSS, chỉ vào sau khi chạm 2 xác nhận đủ chuỗi Sweep → Displacement → MSS → FVG.

![[Pasted image 20260716134557.png]]

---

## 2. ICT 2022 Model — Entry Sequence

- [x] **1. Liquidity Sweep** — chạm 1 (16:15 London) sweep CE của H1 OB; chạm 2 (18:00 NY) sweep đỉnh thấp hơn (internal high) trước khi đảo chiều
  - Loại: Internal (đỉnh thấp hơn khung M5) + External (CE của OB khung H1)
  - **Số lần chạm POI tới khi có MSS: 2** (xem `touch_count_to_mss` trong frontmatter)
- [x] **2. Displacement** — nến M5 giảm mạnh ngay sau đỉnh của chạm 2, thân lớn, để lại FVG rõ
- [x] **3. Market Structure Shift (MSS)** — phá swing low nội bộ M5 ngay sau displacement — **hình thành ở chạm thứ 2**, KHÔNG phải chạm 1
- [x] **4. FVG hợp lệ** — FVG M5 ≈ 1.06706 – 1.06650, CE ≈ 1.06678
- [x] **5. Entry** — tại CE của FVG M5 (1.06677), trong phiên New York
- [x] **6. Stop Loss** — trên đỉnh OB + buffer (1.06849)
- [x] **7. Take Profit** — H1 Dealing Range Low (1.06249) — **đạt được, nhưng qua gap, xem mục 4**

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Có Liquidity Sweep trước entry (2 lần, không phải 1 — đã kiên nhẫn chờ đúng)
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ (khung M5, ở lần chạm thứ 2)
- [x] FVG nằm trong Premium (đúng phía cho Short)
- [x] Entry trong POI hợp lệ (CE), không đua giá
- [x] SL ở vùng invalidation hợp lý (trên đỉnh OB)
- [x] RR tối thiểu đạt ≥ 1:2 (2.49R)
- [ ] **Weekend hold policy được xác định trước khi vào lệnh** — KHÔNG có; đây là khoảng trống quy trình cần vá (xem Lesson 3)

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: **Hit Take Profit (+2.49R danh nghĩa)** — nhưng cây nến quét qua mức TP là **gap mở cửa Chủ nhật**, không phải một nhịp giảm liên tục trong phiên giao dịch bình thường.

### Tại sao lệnh thắng? (tách root cause khỏi may mắn)

- **Root cause của entry đúng**: bias top-down đồng thuận (D1 + H1 Bearish), POI chọn lọc (OB sâu trong Premium, không phải OB đại trà), kỷ luật chờ đủ 2 lần chạm với MSS xác nhận ở lần thứ 2 trước khi vào — đây là phần **quy trình**, hoàn toàn tách biệt khỏi kết quả.
- **Phần "may mắn" của outcome**: việc TP được chạm *chính xác* nhờ một gap cuối tuần là một sự kiện **ngoài tầm kiểm soát và ngoài dự đoán** tại thời điểm entry. Nếu không có gap, giá có thể mất nhiều phiên hơn để chạm H1 DR Low, hoặc thậm chí không chạm được nếu cấu trúc đảo chiều giữa chừng.

### Thị trường có tín hiệu cảnh báo trước không?

Có, và đáng chú ý là có **nhiều lớp xác nhận trước khi tín hiệu MSS xuất hiện**, không chỉ một:

1. **Sweep tại POI (chạm 1)**: giá quét CE của OB nhưng bị từ chối ngay — smart money từ chối Premium lần đầu.
2. **Lower high giữa chạm 1 và chạm 2**: chạm 2 không vươn lại tới đỉnh cũ — cấu trúc yếu đi rõ rệt trước khi MSS chính thức xảy ra. Đây là tín hiệu sớm, tinh tế hơn MSS.
3. **MSS + Displacement M5**: xác nhận chính thức, phá cấu trúc nội bộ.
4. **FVG hình thành đúng trong nhịp displacement đó**: cho một điểm entry rõ ràng, không phải đoán mò.

### TP bị quét bởi gap — tách bạch "entry hợp lệ" khỏi "outcome đại diện"

Đây là phần quan trọng nhất của bài phân tích này, tiếp nối đánh giá trước đó:

- **Entry logic vẫn hợp lệ 100%.** Không có yếu tố nào trong chuỗi Sweep → Displacement → MSS → FVG phụ thuộc vào việc biết trước sẽ có gap. Quyết định vào lệnh được đưa ra dựa trên thông tin objectively quan sát được tại M5, trước khi biết kết quả.
- **Nhưng R Multiple 2.49 ghi nhận ở đây KHÔNG nên được đưa thẳng vào tính expectancy tổng của model** như một win "sạch", vì cơ chế đạt TP (gap) không lặp lại được một cách có hệ thống. Đã gắn `tp_fill_anomaly` và tag `weekend-gap-fill` trong frontmatter để sau này lọc riêng nhóm trade này khi tính win rate/expectancy trên `_Backtest Dashboard` — so sánh xem con số expectancy có thay đổi đáng kể khi loại các trade dạng này hay không.
- **Rủi ro đối xứng chưa được tính đến trong kế hoạch**: nếu gap xảy ra *ngược hướng* (nhảy qua SL thay vì TP), khoản lỗ thực tế có thể vượt xa 1R dự kiến do trượt giá qua gap — không có gì đảm bảo SL được khớp đúng 1.06849. Kế hoạch ban đầu không có điều khoản nào xử lý việc giữ lệnh qua cuối tuần.

### Setup này khớp bao nhiêu % với mô hình chuẩn?

**~90%** cho phần entry logic (context, sweep, MSS, FVG, risk structure đều chuẩn). Điểm trừ duy nhất nằm ở quy trình quản trị rủi ro cuối tuần — không phải ở entry.

### Nếu được vào lại, tôi sẽ làm gì khác?

- Cân nhắc **chốt một phần (partial TP)** tại thanh khoản/PD array gần hơn trước khi tới H1 DR Low, thay vì đặt 100% khối lượng chờ target xa nhất — giảm phụ thuộc vào một cú gap may mắn để đạt full R.
- Xác định trước (trong kế hoạch, không phải sau khi thấy kết quả) quy tắc: nếu lệnh vẫn đang mở gần giờ đóng cửa thị trường cuối tuần, có đóng thủ công một phần hay chấp nhận rủi ro gap với size đã định trước.

---

## 5. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Entry là một **process win thực thụ** — kỷ luật chờ đủ 2 lần chạm POI với MSS xác nhận mới vào, đúng tinh thần "first tap = no trade". Nhưng **kết quả (TP hit) một phần đến từ một gap cuối tuần ngoài dự đoán**, nên cần tách rõ "được khen vì quy trình" khỏi "được khen vì kết quả" — hai việc khác nhau.

### Lesson 1 — "Double-tap POI, lower high ở lần 2" là một tín hiệu sớm đáng tin cậy

Việc giá chạm POI lần 2 nhưng tạo đỉnh **thấp hơn** lần 1 là một failure swing vi mô, xuất hiện *trước cả khi* MSS chính thức xảy ra. Đây là dấu hiệu sớm cho thấy phe mua đang cạn lực ngay tại vùng Premium. Cần theo dõi qua nhiều mẫu backtest tiếp theo: tần suất "lower high ở lần chạm 2" có tương quan với xác suất MSS xảy ra ngay sau đó hay không — nếu có, đây có thể trở thành một tiêu chí sàng lọc entry sớm hơn (tăng độ tin cậy trước khi MSS hình thành), tương tự pattern "first tap = no trade" đã ghi nhận ở backtest NAS100 trước đó ([[01 - Win - NAS100 - 2026-04-02- Long|xem backtest 2026-04-02]]).

### Lesson 2 — TP đạt được qua gap KHÔNG chứng minh model có edge tại mục tiêu đó

Việc giá chạm H1 DR Low nhờ một cú nhảy giá cuối tuần không nói lên được gì về khả năng thị trường thực sự "chạy" tới đó bằng price action tuần tự trong điều kiện bình thường. Nếu không tách riêng loại trade này, sample backtest sẽ bị lẫn giữa "model có edge thật" và "may mắn từ sự kiện ngoài mô hình" — làm sai lệch expectancy tính được. Quy tắc: mọi trade có TP/SL bị quét bởi gap phải được gắn tag riêng (`weekend-gap-fill`) và cân nhắc loại khỏi tính win rate chính, chỉ giữ lại để tham khảo.

### Lesson 3 — Rủi ro gap có tính đối xứng, và kế hoạch ban đầu chưa xử lý điều này

Gap giúp lệnh này về đích nhanh hơn, nhưng nếu gap xảy ra ngược hướng thì SL 1.06849 không có gì đảm bảo được khớp đúng giá — khoản lỗ có thể lớn hơn 1R dự kiến do trượt giá. Đây là một lỗ hổng quy trình thực sự (không phải chỉ là "biết ơn may mắn"): kế hoạch trade cần có điều khoản rõ ràng về việc giữ lệnh qua cuối tuần trước khi vào lệnh, không phải phát hiện ra sau khi đã thấy kết quả thuận lợi.

### Lesson 4 — Chất lượng POI (OB sâu trong Premium, ≥0.786 fib) là một bộ lọc đáng giữ

OB được chọn ở đây nằm sâu hơn mức 0.786 fib — không phải một OB đại trà ở giữa range. Đây là dạng POI có xác suất cao hơn theo lý thuyết Premium/Discount vì nó đại diện cho vùng "đắt" nhất, nơi smart money có động cơ mạnh nhất để phân phối. Cần tiếp tục ghi nhận vị trí fib chính xác của POI (không chỉ ghi "Premium" chung chung) qua các backtest sau để kiểm tra xem POI càng sâu trong Premium/Discount có thực sự cho win rate/expectancy tốt hơn OB ở vùng 0.5–0.618 hay không.

### Lesson 5 — Đặt toàn bộ TP vào một mục tiêu xa duy nhất làm tăng phụ thuộc vào các sự kiện ngoài mô hình

TP được đặt 100% khối lượng tại H1 DR Low — một mục tiêu khá xa so với entry. Điều này khiến kết quả cuối cùng phụ thuộc nhiều vào việc giá có "đi hết đường" hay không, và trong trường hợp này, phần cuối của quãng đường đó do gap đảm nhiệm chứ không phải organic price delivery. Việc chia nhỏ TP (partial tại thanh khoản gần hơn, phần còn lại chạy tới DR Low) sẽ giảm phụ thuộc vào các sự kiện một-lần như gap để đạt full R, đồng thời vẫn giữ được RR tốt cho phần chạy xa.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Thêm **"Weekend Hold Policy"** vào playbook: quy định rõ có được giữ lệnh mở qua đêm thứ 6 sang Chủ nhật hay không; nếu có, giảm size hoặc chấp nhận rủi ro gap tường minh trong kế hoạch trade (không phải phát hiện sau khi vào lệnh).
- [ ] Khi tính win rate/expectancy tổng trên `_Backtest Dashboard`, lọc riêng các trade có tag `weekend-gap-fill` để so sánh expectancy có/không có nhóm này.
- [ ] Theo dõi thêm biến "lower high ở lần chạm POI thứ 2" như một tín hiệu sớm tiềm năng qua các backtest tiếp theo (liên quan Lesson 1).
- [ ] Cân nhắc rule partial TP tại thanh khoản trung gian khi TP chính đặt xa hơn ~2R (liên quan Lesson 5).

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | 9/10 |
| POI Selection | 9/10 |
| Liquidity Sweep | 9/10 |
| MSS Confirmation | 8/10 |
| FVG / OB Entry | 8/10 |
| Risk Management (RR) | 6/10 — trừ điểm vì thiếu Weekend Hold Policy trước khi vào lệnh, không phải vì RR danh nghĩa thấp |

**Overall Grade**: B+ — process entry rất tốt, nhưng outcome bị nhiễu bởi gap và có một lỗ hổng quy trình (weekend risk) chưa được xử lý trước khi vào lệnh.

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]] · [[27 - Premium Discount]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- Backtest liên quan (double-tap pattern): [[01 - Win - NAS100 - 2026-04-02- Long]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]] (chưa có mục riêng cho "giữ lệnh qua gap cuối tuần" — xem checkbox Playbook ở mục 5)
