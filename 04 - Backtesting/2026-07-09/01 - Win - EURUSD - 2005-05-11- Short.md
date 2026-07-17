---
type: backtest
backtest_date: 2026-07-09
trade_date: 2005-05-11
symbol: EURUSD
position: Short
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.28878
stop_loss: 1.29117
take_profit: 1.28123
r_planned: 3
r_multiple: 2.85
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-05-11 — EURUSD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2005-05-11     |
| Position             | Short          |
| Result               | Win            |
| Session              | New York       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bearish        |
| Bias Correct?        | Yes            |
| Entry                | 1.28878        |
| Stop Loss            | 1.29117        |
| Take Profit          | 1.28123        |
| R Planned            | 3              |
| R Multiple (kết quả) | 3.03           |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 đang trong nhịp giảm
  - Cấu trúc chuyển sang LH/LL
  - Giá hiện tại đang trong nhịp hồi, tạo 1 nến displacement lớn
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day/Week High
  - Sell-side liquidity: Giá đang hướng tới vùng
	  - Equal Lows: 1.28238
	  - old low trung gian giữa EQL và Dealing Range low 1.28116
	  - Dealing Range Low (nhiều nến ngang nhau liên tiếp với bóng nến dài)
![[Pasted image 20260709140546.png]]
### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- LH/LL
	- Giá giảm mạnh sâu 1 vùng consolidation
- **Dealing Range**: 
	- High: 1.29884
	- Low 1.27889
	- Giá đang trong vùng BPR, BPR nằm trong vùng Premium => Điều kiện Zone (Premium/Discount) đã có
- **POI chính**: 
	- Balance Price Range (đặc biệt vùng CE)
- **Liquidity cần chờ sweep**:
  - CE vùng Balance Price Range: 1.29034
### Phân Tích:
- Giảm mạnh với 1 nến displacement lớn sau đoạn consilidation
	- Ngày 04 tháng 5 2005, giá displacement tăng với các nến bullish thân lớn tạo 1 Bullish FVG lớn. Sau đó giá đi ngang trong range
	- Đến ngày 6 tháng 5 2005, giá xuất hiện các cây nến Bearish displacement thân lớn đón xuyên qua Bullish FVG từ ngày 4 => Tạo thành 1 vùng Balance Price Range (BPR khung H1) => POI quan trọng nằm trên 50% range ( vùng Premium) => POI chờ giá đã có
	- Chờ giá retrace về vùng BPR
	- Ngày 11 tháng 5 2005, giá retrace về tới vùng CE của BPR và bật mạnh ra (râu nến quét lên CE BPR và đóng nến gần xuống cạnh dưới ) => Liquidity Sweep đã có
	- Xuống M5 quan sát
![[Pasted image 20260709140256.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá quét qua CE vùng BPR sau đó bật tăng ra mạnh => Displacement đã có
- Giá tạo các nến displacement mạnh quét các higher low trước đó đồng thời tạo FVG => POI Entry đã có
- MSS Đã có
- Stoploss đặt bên trên điểm sweep
- **Entry trigger**:
  - Liquidity Sweep: 
	  - Quét qua 50% BPR khung H1
	  - Quét EQH: 1.28912
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - Tâm lý khi vào lệnh lúc đó hơi lo khi cây nến retrace về FVG là 1 nến lớn
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là BPR H1)
- **Invalidation reason**:
  - Giá đóng qua cạnh trên BPR và giữ bên trên
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260709140429.png]]
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

- **Result**: 
	- Hit TP
	- Điểm cải thiện: Partial Take Profit khi giá quét xuống 1 đáy H1 (take 50% khi đạt 2.55R). Sau đó giá quét thêm 1 đoạn xuống 1 định cũ nữa ( từ đáy TP1 đến đáy TP2 thêm 0.78R)
- **Tại sao lệnh thắng/thua?**
  - Kiên nhẫn chờ giá di chuyển ra khỏi vùng Consolidation sau đó hình thành BPR khung H1
  - Giá retrace về CE BPR và bật ra mạnh, râu nến quét qua CE nhưng giá đóng gần cạnh dưới cách xa CE
  - Cú quét thanh khoản và bật ra đó có kèm displacement và FVG đồng thời tạo MSS (phá qua các higher lows)
  - Giá trong vùng Premium cho setup Short
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Có Displacement
  - Có MSS
  - FVG hợp lệnh, tạo từ nến thân lớn sau 1 nhịp quét CE BPR
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 
	- 90%
	- Giá không nằm trong vùng OTE
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Cải thiện tâm lý giao dịch
  - Khi khung M5 giá quét CE BPR và tạo displacement ngược + FVG => entry tại FVG tôi đã khá lo khi giá retrace bằng 2 cây nến thân lớn, gần như không có bóng nến và consolidation 1 đoạn nhỏ trong khoản CE và cạnh dưới của BPR

---

## 5. Lesson Learned

> [!summary] Kết luận 1 dòng
> Lệnh A-grade thắng nhờ **kiên nhẫn chờ sweep đúng POI Premium (CE của BPR H1) trước khi xuống M5** — đó mới là edge, không phải bản thân cây FVG M5. Vấn đề còn lại nằm ở **kỷ luật ghi nhận dữ liệu & tâm lý**, không nằm ở kỹ thuật đọc chart.

### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**
Edge thật của setup này là **trình tự HTF → LTF được tôn trọng**: giá phải sweep POI cao cấp (CE của BPR H1, nằm trong Premium) *trước*, rồi mới tìm entry trigger trên M5. Việc chờ đúng chuỗi `Premium POI → buy-side sweep → bearish MSS → FVG entry` là nguyên nhân gốc khiến lệnh thắng — không phải vì cây FVG M5 đẹp.

Song song, root cause của những điểm **cần sửa** cũng chỉ có một: **thiếu kỷ luật trong việc định nghĩa và ghi nhận dữ liệu khách quan** (Draw on Liquidity mục tiêu cụ thể, phân biệt Sweep vs MSS, R thực nhận). Điều này không làm hỏng lệnh này, nhưng nếu lặp lại sẽ **phá tính hợp lệ thống kê của cả bộ backtest**.

**Triệu chứng (symptoms) — sinh ra từ root cause:**
- **Mâu thuẫn bias:** frontmatter `htf_bias: Bullish` nhưng phần phân tích D1 lại là **Bearish**. Với một lệnh Short thắng, bias đúng phải là **Bearish** → cần sửa frontmatter (nếu để Bullish thì `bias_correct: Yes` là vô lý và dashboard sẽ sai).
- **R lý tưởng hoá:** log `r_multiple: 3` nhưng RR hình học thực tế là **~3.16R** (risk 23.9 pip, reward 75.5 pip). Hơn nữa đã partial 50% tại 2.55R ⇒ **R thực nhận blended ≈ 2.85R**, không phải 3.
- **Nhầm nhãn Sweep/MSS trên M5:** ghi "Liquidity Sweep = quét các old lows" cho một lệnh **Short**. Với Short, sweep kích hoạt phải là **buy-side sweep** (quét thanh khoản phía trên — chính là cú sweep CE của BPR H1). Việc "phá qua các higher low" là **MSS**, không phải sweep. Hai khái niệm bị gộp làm một.
- **DOL mơ hồ:** chỉ ghi chung "PDH/PDL"; không chỉ ra **một mục tiêu giá cụ thể** mà lệnh hướng tới (sell-side pool nào, mức bao nhiêu).

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
Ngày 04/05 giá displacement tăng tạo **Bullish FVG**; ngày 06/05 giá displacement giảm xuyên qua chính FVG đó ⇒ hai FVG chồng lên nhau tạo **BPR (Balance Price Range)** trên H1, với **CE = 1.29034 nằm trong Premium** → đây là institutional reference cho phe bán. Khi giá retrace lên CE, râu nến **quét buy-side liquidity** (stop của phe bán sớm + lệnh mua breakout) rồi đóng cửa gần cạnh dưới ⇒ smart money từ chối giá Premium và bắt đầu reprice xuống sell-side. Trên M5, nhịp giảm phá các higher low gần nhất (**MSS**) để lại **Bearish FVG**; CE của FVG M5 là entry tối ưu. Cây nến thân lớn lấp FVG khiến bạn lo lắng thực chất là **dấu hiệu repricing mạnh (bullish cho luận điểm Short)**, không phải mối đe doạ — chỉ invalid nếu **đóng cửa trên cạnh trên BPR**.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- **Tâm lý:** lo lắng khi giá retrace vào FVG bằng nến thân lớn/ít bóng nến. Cần chuẩn hoá phản xạ: nến thân lớn lấp FVG là **bình thường và thường là tín hiệu tốt**; chỉ hành động (cắt/không vào) khi giá **đóng qua ngưỡng invalidation** đã định trước, không phản ứng theo cảm giác.
- **Ghi R:** xu hướng log R "đẹp" thay vì R thực nhận. Lặp lại ⇒ expectancy backtest bị thổi phồng.
- **Nhãn khái niệm:** gộp Sweep và MSS. Cần tách bạch mỗi lần.

### 5.3. Rule cần thêm/cập nhật vào Playbook

1. **Định nghĩa DOL trước khi vào lệnh:** viết rõ mục tiêu TP chính = tên pool + mức giá (vd "sell-side: đáy H1 ngày 06/05 @ 1.28xxx").
2. **Tách Sweep vs MSS:** với Short, chỉ đánh dấu "Liquidity Sweep" cho **buy-side sweep**; phần phá cấu trúc xuống ghi riêng là **MSS**.
3. **Log 2 con số R:** (a) R nếu giữ full tới TP, (b) **R thực nhận** sau partial. Đồng bộ `r_multiple` frontmatter = R thực nhận (ở lệnh này ≈ 2.85R).
4. **Chuẩn hoá quy tắc Partial TP:** nếu chọn chốt một phần tại intermediate liquidity (đáy H1), phải **định trước % và mức**, không tuỳ hứng. Backtest riêng để so expectancy giữa "hold full 3R" và "partial 50% @ intermediate + trail" trước khi coi là rule.
5. **QC frontmatter:** trước khi lưu, `htf_bias` phải khớp cả hướng lệnh lẫn phần phân tích; `bias_correct` phải logic với hai giá trị đó.

---
