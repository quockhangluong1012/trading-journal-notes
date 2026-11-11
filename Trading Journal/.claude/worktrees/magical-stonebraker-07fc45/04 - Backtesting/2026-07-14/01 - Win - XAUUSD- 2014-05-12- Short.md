---
type: backtest
backtest_date: 2026-07-14
trade_date: 2014-05-12
symbol:
  - XAUUSD
position: Short
result:
  - Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct:
  - Yes
poi_type: "[[13 - FVG  - Fair Value Gap|FVG]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1301.562
stop_loss: 1304.113
take_profit: 1294.173
r_planned: 2.9
r_multiple: 2.9
grade: A-
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2014-05-12 — XAUUSD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên XAUUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | XAUUSD         |
| Trade Date (dữ liệu) | 2014-05-12     |
| Position             | Short          |
| Result               | Win            |
| Session              | New York       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M1             |
| HTF Bias             | Bearish        |
| Bias Correct?        | Yes            |
| Entry                | 1301.562       |
| Stop Loss            | 1304.113       |
| Take Profit          | 1294.173       |
| R Planned            | 2.9            |
| R Multiple (kết quả) | 2.9            |
| Grade                | A-             |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

> [!check] Toàn vẹn dữ liệu — ĐÃ SỬA (2026-07-15)
> Note tạo bằng cách copy 1 lệnh cũ nên còn sót 2 điểm không khớp giữa frontmatter và Summary table; đã đối chiếu chart và lập luận trong mục 5 để sửa:
> 1. **Frontmatter `entry_price`**: 1300.5 → **1301.562** (khớp Summary table và cho R = 2.9; giá trị 1300.5 cũ chỉ cho R ≈ 1.75, mâu thuẫn `r_planned`).
> 2. **Summary table `Grade`**: A → **A-** (đồng bộ với frontmatter `grade: A-`; hạ điểm vì lỗi toàn vẹn dữ liệu + mơ hồ TF entry, theo lập luận mục 5.2).
>
> Quy trình phòng ngừa: xem Rule toàn vẹn dữ liệu ở mục 5.3.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
	  - Phía bên trái giá đã quét hết các lower high trong nhịp tăng sau đó sau đó tạo 1 đỉnh ( Long Term High)
	  - Trước nhịp tăng 31/12/2013, hình thành 1 cú quét thanh khoản, quét đáy trước sau đó đóng nên lại trong range và tăng (1)
	  - Nhịp tăng đồng thời tạo Displacement + Order Block (2)
	  - Tiếp sau đó là nhịp tăng Bullish với các HH/HL -> Thanh khoản tích tụ dần ở các đáy này
	  - Sau nhịp tạo đỉnh ( long term high) giá hình thành 1 Bearish MSS với nhịp displacement + FVG (3)
	  - Trong Dealing Range lớn giá đang trong vùng Premium (4)
	  - (1) + (2) + (3) + (4) => Bias Bearish
	  - Giá đang trong vùng Premium, thanh khoản Buy Side đã bị lấy, mục tiêu kế tiếp là Sell Side Liquidity và vùng Order Block
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: 
	  - D1 Dealing Range High: 1392.098
	  - Bearish Order Block: 1387.437
  - Sell-side liquidity:
	  - Dealing Range Low: 1182.661
	  - Old lows tạo ra trong nhịp giá tăng tạo Long Term High
	  - Order Block
	  - H1 Dealing Range Low

![[Pasted image 20260714063937.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- Sau Long Term High, giá hình thành Bearish MSS + Displacement (đồng bias với D1)
	- LH/LL, order flow đang giảm
- **Dealing Range (nhịp retrace cho setup Short)**: 
	- High: 1315.691 (swing high — fib 1.0)
	- Low: 1277.416 (swing low — fib 0.0)
	- Giá đang retrace lên vùng **Premium / OTE** cho setup Short
- **POI chính**: 
	- Bearish OB vùng ~0.786 (≈ 1308 – 1310)
	- Bearish FVG H1 (từ nhịp giảm 7/5) nằm trong vùng OTE
- **Liquidity cần chờ sweep**:
  - Buy-side: các internal high của consolidation + cạnh trên H1 FVG (gần CE của liquidity void)
  - Sau sweep → draw về Sell-side / OB phía dưới

### Phân Tích: 
- Phân tích context trước:
	- Sau khi quét SSL ngày 2/5/2014 19:00, giá tạo displacement và bắt đầu nhịp tăng với HH/HL và tạo thành 1 đỉnh ngày 5/5/2014 lúc 19:00
	- Sau khi tạo đỉnh giá bắt đầu đi ngang (consolidation)
	- Tới ngày 7/5/2014 14:00, giá hình thành các nến Bearish Displacement mạnh phá xuống đồng thời tạo thành các FVG trên đường giá
	- Tới ngày 8/5/2014 lúc 00:00 giá bắt đầu chững lại và đi ngang (Consolidation)
	- Sau đó tới ngày 12/5/2014 lúc 17:00 giá có 1 nến Bearish Displacement quét xuống các đáy cũ (của consolidation range) và đóng bên ngoài consilidation range, sau đó là các nến xanh đóng quay ngược trở lại
	- Đáy của nến quét thanh khoản đó hình thành H1 Dealing Range Low
	- Sau nhịp quét đó giá đang trong vùng Discount, tuy nhiên Bias lúc đó đang là Bearish -> Chờ giá retrace về vùng Premium
- Phân Tích lệnh:
	- Ngày 12/5/2014 lúc 19:00 giá tạo 1 cây nến displacement mạnh phá qua vùng cân bằng (50%) của Dealing Range và trờ lại vùng Premium
	- Sau đó giá quét lên trên 1 Bearish FVG (hình thành từ nhịp giảm ngày 7/5/2014 - FVG nằm trong Liquidity Void)
	- Giá quét râu nến lên trên cạnh trên của FVG ( cạnh trên gần bằng CE của vùng Liquidity Void của nhịp giảm ngày 7/5/2014)
	- Sau đó giá đóng nến ngay vào lại bên trong range (cùng cây nến quét đó)
	- Sau đó xuất hiện nến giảm sau cú quét đó
	- Xuống M5 quan sát

![[Pasted image 20260714074100.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Sau khi quét cạnh trên H1 FVG và tới CE của Liquidity void, giá bật ra đóng lại bên trong H1 FVG. Sau đó hình thành nến giảm
	- Trong khung M5, giá tạo các nến Bearish displacement
	- Sau đó tạo 1 đáy ngắn hạn (Short Term Low) lúc 12/05/2014 20:00
	- Nhịp displacement tiếp theo giá phá qua STL tạo thành 1 MSS với các nến Bearish Displacement
	- Tuy Nhiên khung M5 các bóng nến nhiều và chống lắp, không tạo FVG rõ -> Xuống M1 quan sát giá
	- Khung M1, giá hình thành 2 FVG:
		- FVG 1: 1302 - 1301 : Tuy nhiên lúc này là chân displacement giá chưa tạo MSS
		- FVG 2: 1301 - 1300: Đã có MSS
	- Entry khi giá retrace về CE của FVG 2
- **Entry trigger**:
	  - Liquidity Sweep: 
		  - Quét cạnh trên FVG
		  - Quét tới CE Liquidity Void
		  - Trong nọi bộ khung M1/M5 cũng có quét thanh khoản các đáy nội bộ tạo ra khi giá hình thành MSS
	  - MSS: Giá tạo MSS bằng các cây nến bullish displacement lúc 19:20
	  - Displacement: có displacement lúc 19:20-> tạo FVG
- **Entry reason**:
	  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là FVG H1)
	  - FVG nằm trong vùng giữa 50% và 0.618 (OTE)
- **Invalidation reason**:
	  - Giá đóng qua FVG H1
- **Tôi có chờ đủ điều kiện không?** Có

**M5:**
![[Pasted image 20260714075254.png]]

**M1:**
![[Pasted image 20260714075206.png]]

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
	  - Kiên nhẫn chờ H1 đồng Bias với khung D1 (Bearish)
	  - Chờ M5, M1 confirm Bias
	  - Chờ H1 retrace về vùng Premium / OTE
	  - Có quét thanh khoản + CISD
- **Thị trường có cho tín hiệu cảnh báo trước không?**
	  - Có Displacement
	  - Có MSS
	  - Có FVG
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90% 
- **Nếu được vào lại, tôi sẽ làm gì khác?**
	  - Cần thêm backtest để xem lúc nào nên vào tại cạnh và khi nào vào tại CE

---

## 5. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Setup Short chuẩn ICT 2022 (Sweep → Displacement → MSS → FVG entry trong OTE), quy trình top-down tốt; điểm yếu lớn nhất KHÔNG nằm ở kỹ thuật mà ở **nhiễm dữ liệu journal** (frontmatter/heading/số liệu lẫn từ một setup khác) — thứ đe doạ trực tiếp tính hợp lệ của mẫu backtest.

### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc chất lượng lệnh) — chỉ có MỘT:**
Kỷ luật tôn trọng **trọn vẹn chuỗi ICT 2022 theo đúng thứ tự** và KHÔNG ép entry ở khung không rõ ràng. Khi M5 cho các nến bóng dài chồng lấp, không có FVG sạch, tôi đã xuống M1 để tìm cấu trúc rõ (sweep nội bộ → MSS → FVG hợp lệ) thay vì đoán. Đây là gốc rễ khiến điểm vào rơi đúng OTE và SL gọn.

**Triệu chứng tích cực sinh ra từ root cause đó:**
- Entry nằm trong **OTE (0.5–0.618)**, RR 2.9 với SL chỉ ~2.5 giá.
- Phân biệt được **FVG1 (trước MSS → bỏ)** và **FVG2 (sau MSS → vào)** — chi tiết mà đa số trader sai nhất trong 2022 Model.
- Bias Bearish được dựng từ **4 tầng confluence** (sweep SSL → Displacement + OB → Bearish MSS + FVG → Premium của Dealing Range), không phải cảm tính.

**Cơ chế thị trường đã diễn ra (hiểu để lặp lại được):**
Sau khi lấy Buy-side ở Long Term High (~1392) và quét lên **CE của Bearish FVG H1** (tàn dư liquidity void của nhịp giảm 7/5), giá bị từ chối tại vùng Premium/OTE. Nhịp Bearish Displacement trên M1 tạo MSS + FVG; retrace về CE FVG2 là nơi smart money tiếp tục phân phối → giá đi tìm Sell-side / OB phía dưới. TP 1294 là mục tiêu thanh khoản gần (không phải OB D1 ~1200), nên đây là "partial draw", không phải toàn bộ draw on liquidity của D1.

**Điểm kỹ thuật CẦN xác minh thêm (đừng vội cho là đã đúng):**
- **"Quét CE của liquidity void" ≠ "quét liquidity pool".** CE/FVG là *PD array phản ứng*; liquidity thật là equal highs / swing high có stop nằm bên trên. Lần sau ghi rõ: đã quét POOL nào (giá bao nhiêu) hay chỉ phản ứng tại PD array.
- **Entry ở cạnh 0.618 trong khi POI H1 (OB) nằm cao hơn ở ~0.786:** OB chưa hề được test. Lệnh thắng nhờ LTF confirm sớm, nhưng nếu giá retrace sâu hơn về OB (~1308) thì SL 1304 đã bị quét trước. → SL đang neo theo **STH của M1**, KHÔNG neo theo invalidation của **POI H1**. Đây là đánh đổi "entry sớm, RR cao" vs "chờ POI chính, SL an toàn hơn". Cần thêm mẫu để biết khi nào chọn cái nào.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

1. **Nhiễm dữ liệu do copy-paste (nghiêm trọng nhất).** File này ban đầu bị lẫn nội dung của một setup **Long / NAS100** khác: `htf_bias: Bullish` (lệnh là Short/Bearish), heading "XAUUSD **Long**", Dealing Range **24,570 / 22,822** (số NAS100), POI OB **1.26642–1.26515** (giá EURUSD), câu "vùng **Discount** cho setup **Long**", và ngày tháng lẫn 2014 ↔ 2026. **Đã dọn sạch** (top + frontmatter hiện đúng instrument XAUUSD / Short / Bearish). Với backtest, **dữ liệu bẩn = mẫu thống kê vô nghĩa** → đây vẫn là rủi ro số 1 cho cả dự án nên giữ ghi chú này để cảnh giác.
2. **Outcome bias khi chấm điểm.** Grade A / khớp 90% một phần vì lệnh THẮNG. Quy trình tốt thật, nhưng file lỗi dữ liệu + mơ hồ TF entry → công bằng hơn là **A-** (đã hạ về A- trong cả frontmatter và Summary table). Chấm theo *process sạch*, không theo kết quả.
3. **`entry_timeframe`** đã sửa về **M1** (khung thực sự bấm entry), khớp cả frontmatter và Summary table — trước đây ghi nhầm M5 làm lệch thống kê "khung vào lệnh thực tế".

### 5.3. Rule cần thêm/cập nhật vào Playbook

- **R-BT-01 — Làm sạch file trước khi lưu:** mỗi backtest tạo từ template phải kiểm symbol / position / bias / số Dealing Range / POI khớp đúng instrument. Tuyệt đối không để số của instrument khác.
- **R-BT-02 — Bias khớp hướng lệnh:** `htf_bias` phải khớp hướng (Short → Bearish). `bias_correct` chỉ điền sau khi bias đã đúng instrument.
- **R-BT-03 — `entry_timeframe` = khung THỰC SỰ bấm entry** (ở đây M1), không phải khung dự định.
- **R-BT-04 — Tách bạch trong mục sweep:** luôn ghi rõ *quét POOL nào (giá)* vs *phản ứng PD array nào* — không gộp làm một.
- **R-BT-05 — Neo SL:** ghi rõ SL theo invalidation của POI (H1) hay theo STH của LTF entry; nếu lệch nhau, note lại đánh đổi RR/xác suất.
- **R-BT-06 — Thống nhất hệ ngày (UTC+7)** và năm dữ liệu replay; không lẫn 2014/2026 trong cùng file.

