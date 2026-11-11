---
type: backtest
backtest_date: 2026-07-10
trade_date: 2021-07-22
symbol:
  - EURUSD
position: Long
result:
  - Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct:
  - Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.17841
stop_loss: 1.17698
take_profit: 1.18244
r_planned: 2.86
r_multiple: 2.86
grade: B
followed_plan: No
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-05-02 — EURUSD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2021-07-22     |
| Position             | Long           |
| Result               | Win           |
| Session              | New York         |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bullish        |
| Bias Correct?        | Yes            |
| Entry                | 1.17841        |
| Stop Loss            | 1.17698        |
| Take Profit          | 1.18244        |
| R Planned            | 2.86           |
| R Multiple (kết quả) | 2.86             |
| Grade                | B              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
	  - Khung H1 ngày 21/05/2021 giá phá qua định ngày 24/02/2021 tạo thành Break Of Structure (BOS) -> Confirm bias Bullish vẫn tiếp diễn
	  - Sau khi phá cấu trúc giá hồi về vùng Discount
	  - Nhịp Pullback kết thúc ngày 21/07/2021 khi giá quay về 1 vùng FVG khung H1 và xuất hiện dấu hiệu Rejection sau 1 chuỗi các nến giảm lớn gần nhau khung D1
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: D1 Dealing Range High = 1.22649
  - Sell-side liquidity: H1 FVG (1.17966-1.17601), D1 Dealing Range Low (1.17054)

![[Pasted image 20260710132929.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- LH/LL
- **Dealing Range**: 
	- High: 1.18956
	- Low 1.17054
	- Giá đang trong vùng Discount cho setup Long
- **POI chính**: 
	- FVG: 1.17966 - 1.17601
	- FVG Nhịp đẩy: 1.17744 - 1.17683
- **Liquidity cần chờ sweep**:
  - Vùng FVG
  - FVG nhịp đẩy

### Phân Tích:
	- Giá đang trong Bearish Bias (ngược hướng với D1 Bias)
	- Tới ngày 7/7/2021 giá quay về tới FVG H1 được tạo từ ngày (21/05/2021) trong nhịp giá đẩy phá cấu trúc (BOS) khung D1
	- Giá di chuyển lên xuống quanh vùng FVG
	- Giá quét xuống cãnh dưới FVG, nhiều cây nến quét xuống (râu nến quét qua cạnh) nhưng đóng lại bên trong FVG
	- Ngày 21/7/2021 giá tạo 1 nhịp displacement mạnh tạo MSS đảo hướng
	- Đồng thời tạo FVG lớn trong nhịp đẩy giá
	- Tới ngày 22/07/2021 giá quay về retest FVG
	- Xuống khung M5 quan sát tín hiệu

![[Pasted image 20260710133055.png]]
Entry
![[Pasted image 20260710133021.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Giá retrace về FVG (nhịp đẩy H1) lúc 19:10 trong New York KillZone
	- Giá quét qua CE FVG nhưng đóng nến lên trên
	- Giá tạo nhịp displacement + FVG M5
	- Entry khi quá retest FVG M5
	- Stop loss cạnh dưới FVG H1
- **Entry trigger**:
  - Liquidity Sweep: Quét các old lows tạo ra trước đó + quét qua 50% FVG khung H1
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là FVG H1)
- **Invalidation reason**:
  - Giá đóng qua đáy sweep/Order Block
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260710141044.png]]

---

## 2. ICT 2022 Model — Entry Sequence

Đánh dấu theo đúng thứ tự checklist của mô hình:

- [x] **1. Liquidity Sweep** — giá quét thanh khoản (Equal H/L, swing, Asia range...)
  - Loại: Internal / External / Equal Highs / Equal Lows
- [x] **2. Displacement** — nến đẩy mạnh, tạo FVG, phá cấu trúc nội bộ
- [x] **3. Market Structure Shift (MSS)** — phá swing point ngược hướng sweep
- [x] **4. FVG / OB hợp lệ** hình thành trong displacement leg
- [x] **5. Entry** — limit trong FVG/OB (CE - Consequent Encroachment) trong Kill Zone
- [x] **6. Stop Loss** — phía trên/dưới điểm sweep (invalidation)
- [x] **7. Take Profit** — opposing liquidity / PD array kế tiếp

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ
- [x] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [x] Entry trong POI hợp lệ, không đua giá
- [x] SL ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng/thua?**
	  - Kiên nhẫn chờ H1 đồng Bias với khung D1 (Bullish)
	  - Chờ H1 quay về vùng Discount
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Có Displacement
  - Có MSS
  - Có FVG
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 80% 
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Chờ 3 tháng để có 1 lệnh -> Có vấn đề cần cải thiện

---

## 5. Lesson Learned

> [!summary] Tóm tắt
> Đây là một **lệnh chất lượng cao, đọc thị trường đúng** (Sweep → Displacement → MSS → FVG → retrace → entry, đúng Discount, đúng NY KillZone, đạt 2.86R). Không có lỗi kỹ thuật gây hại. Bài học lớn nhất nằm ở **kỷ luật ghi chép / định nghĩa tín hiệu** và **tần suất mẫu (selection & hindsight bias)** — hai thứ quyết định tính hợp lệ thống kê của cả bộ backtest, chứ không phải kết quả của riêng lệnh này.

### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**
Kỷ luật **data-integrity của file backtest** chưa chặt: metadata và mô tả không nhất quán với thực tế lệnh. Vì mục đích của bộ backtest là đạt **statistical validity**, một mẫu ghi sai sẽ làm hỏng toàn bộ số liệu tổng hợp trên dashboard — nguy hiểm hơn cả một lệnh thua.

**Triệu chứng (symptoms) — sinh ra từ root cause:**
- **Hướng lệnh sai nhãn**: tên file ghi *Short* nhưng đây là lệnh **Long** (SL 1.17698 *dưới* entry 1.17841, TP 1.18244 *trên* entry ⇒ Long). Frontmatter `position: Long` mới đúng.
- **Ngày tiêu đề sai**: header ghi "Backtest 2005-05-02" trong khi dữ liệu là **2021-07-22**.
- **`followed_plan: No` mâu thuẫn nội dung**: phần sau lệnh ghi "chờ đủ điều kiện: **Có**" và toàn bộ checklist đều tick ⇒ cần thống nhất Yes/No và nêu rõ rule nào bị phá (nếu No).
- **Mô tả SL không khớp số**: ghi "SL cạnh dưới FVG H1" nhưng 1.17698 nằm *bên trong* FVG H1 (1.17966–1.17601) và trong FVG nhịp đẩy (1.17744–1.17683). SL thực chất đặt dưới **sweep low M5**, không phải dưới FVG H1 — cần gọi đúng tên vùng invalidation.
- **TP không neo vào Draw on Liquidity đã ghi**: TP 1.18244 không trùng buy-side đã map (H1 range high 1.18956 / D1 range high 1.22649). 1.18244 gần **equilibrium H1** (~1.18005) — hợp lý như mục tiêu nội bộ, nhưng phải ghi rõ lý do thay vì để lệch với plan.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
- Nhịp 21/05 tạo **BOS bullish D1**, để lại **FVG H1 (1.17966–1.17601)** làm Discount POI cho continuation.
- Giá pullback **sâu về gần đáy dealing range** (discount cực đại), oscillate quanh FVG; nhiều nến **wick quét cạnh dưới FVG nhưng đóng lại bên trong** = dấu hiệu smart money hấp thụ sell-side liquidity, chưa cho displacement giảm.
- 21/07: **displacement + MSS** đảo hướng lên, để lại FVG lớn trong nhịp đẩy.
- 22/07: giá retrace về FVG H1 → xuống **M5 refine**: quét CE, tạo displacement + FVG M5 → entry limit. Đây là **fractal refinement chuẩn** (POI HTF → trigger LTF): giảm risk, tối ưu RR lên 2.86R.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)
- **Selection / hindsight bias**: từ 21/05 → 22/07 là ~2 tháng mới có 1 setup "đẹp". Khi replay dễ chỉ nhìn thấy mẫu hoàn hảo và bỏ qua các mẫu thật/entry hụt xảy ra ở giữa. Tần suất này quá thấp để bộ backtest đạt sample size kịp mốc **07/01/2027** nếu chỉ chạy 1 symbol.
- **Metadata ≠ nội dung**: lặp lại việc quên đối chiếu frontmatter/title với thực tế lệnh trước khi lưu.
- **Đặt tên vùng invalidation & mục tiêu lỏng lẻo**: SL/TP đúng về số nhưng mô tả sai vùng tham chiếu.

### 5.3. Rule cần thêm/cập nhật vào Playbook
- **Rule kiểm tra hướng lệnh**: trước khi lưu, xác nhận `SL < entry & TP > entry ⇒ Long` (và ngược lại). Đồng bộ tên file / title / frontmatter `position` / `result`.
- **Rule neo SL**: luôn ghi rõ SL neo vào đâu (*sweep low M5* / *dưới FVG H1* / *dưới OB*) và con số phải khớp mô tả.
- **Rule neo TP**: TP phải trỏ tới **một liquidity / PD array cụ thể đã map trong Draw on Liquidity**; nếu chốt tại internal liquidity/equilibrium thì ghi rõ "partial vào EQ, runner để BSL 1.18956".
- **Rule `followed_plan`**: chỉ đánh **No** khi nêu được cụ thể rule bị vi phạm; nếu không, đánh **Yes**.
- **Rule tần suất mẫu**: chạy backtest **song song nhiều symbol** (NAS100, GBPUSD, XAUUSD) và nhiều thời kỳ để tăng số mẫu 2022 Model hợp lệ/tuần, hướng tới sample size đủ cho statistical validity trước mốc readiness.

---
