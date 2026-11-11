---
type: backtest
backtest_date: 2026-07-15
trade_date: 2016-11-30
symbol:
  - EURUSD
position: Short
result:
  - Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct:
  - Yes
poi_type: "[[13 - FVG  - Fair Value Gap|FVG]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.06434
stop_loss: 1.06668
take_profit: 1.05882
r_planned: 2.09
r_multiple: 2.09
grade: C+
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2016-11-30 — EURUSD Short

> [!info] Mục đích backtest
> Dùng ** Order Block** làm POI trong chuỗi ICT 2022 Model. Cấu trúc: HTF POI → LTF (M1/M5) Sweep + Displacement + FVG → entry retrace FVG. Đây là lệnh vào tại 1 FVG nơi gần đáy của nhịp Displacement của MSS khung M5. Tôi vào bằng 0.5 slot (50% của 1 lệnh bình thường) và chập nhận việc stoploss xa. Phía trên còn 1 OB entry đẹp hơn tuy nhiên giá không quay lại tới OB này

> [!important] Kết quả tóm gọn
> Giá quét qua cạnh trên FVG bằng **Bearish Displacement** . **Sau đó** giá mới retrace lên FVG tại đáy Displacement, quét qua cạnh trên sau đó quy đầu giảm mạnh hit TP

---

## 0. Backtest Summary

| Field                | Value                                   |
| -------------------- | --------------------------------------- |
| Symbol               | EURUSD                                  |
| Trade Date (dữ liệu) | 2016-11-30 13:55 (UTC+7)                |
| Position             | Short                                   |
| Result               | Win (Hit TP)                            |
| Session              | London Open                             |
| Setup                | ICT 2022 Model                          |
| Entry Model          | HTF OB POI + LTF Sweep/Displacement/FVG |
| Entry Timeframe      | M5 (refine trong M5 FVG)                |
| HTF Bias             | Bearish                                 |
| Bias Correct?        | Yes (giá cuối cùng chạm TP)             |
| POI dùng (leg khớp)  | M5 FVG 1.06453–1.06414 (~OTE 0.618)     |
| Entry                | 1.06434 (cạnh của FVG M5)               |
| Stop Loss            | 1.06668 (trên cây nến sweep BSL)        |
| Take Profit          | 1.05886                                 |
| Risk (points)        | 0.00254                                 |
| Reward (points)      | 0.00532                                 |
| R Planned            | 2.09                                    |
| R Multiple (kết quả) | 2.09                                    |
| Grade                | C+                                      |
| Followed Plan?       | Yes                                     |

---

## 1. HTF Context & Bias

### D1 — Daily Bias & Context

- **Bias**: Bearish
- **Market Condition**: HL/LL
- **Lý do xác định bias (PD array, draw on liquidity)**:
	- Giá đang trong nhịp hồi sau các cây nến Bearish Displacement mạnh
	- Giá có 1 nhịp Consolidation từ ngày 24/7/2026 - 9/11/2016
	- Ngày 9/11/2026 giá có 1 cây nến lớn quét lên trên các old high tạo thành EQH sau đó giảm mạnh tại thành Bearish Displacement + FVG trên đường giá
- **Draw on Liquidity**:
	- Buy-side (BSL):
		- EQH: 1.12905
		- FVG: 1.10036 - 1.09527
	- Sell-side (SSL): 
		- EQL: 1.05205
	- Thiên hướng Short intraday**.

![[Pasted image 20260715141103.png]]

![[Pasted image 20260715140520.png]]
### H1 — Cấu trúc & POI

- **Cấu trúc H1**:
	- Xác định dealing range cho setup bằng fib: **Low (0) = 1.05653 → High (1) = 1.06873**.
	- Giá có 1 nhịp displacement giảm trạng MSS khung H1 -> Bias H1 Bearish
- **Hai PD Array (POI) trong Premium — điểm mấu chốt của bài học**:
	- **Order Block (OB)**: 1.06624 - 1.06563. *POI sâu hơn, nằm cao hơn trong Premium.*
- **Fib OTE levels**: 
	- 0.618 = 1.06414
	- 0.705 = 1.06512 
	- 0.786 = 1.06668
- **Liquidity cần chờ sweep**: 
	- Sweep lên cạnh trên của OB

![[Pasted image 20260715141948.png]]

### Phân tích context → lệnh

- Bias Bearish (D1 + H1 đồng thuận), giá đã quét SSL vùng Discount và đang retrace lên Premium → **khung cảnh cho một lệnh Short là hợp lệ**.
- Ngày 28/11/2016 giá tạo nhiểu cây nến Bullish Displcement với thân nến lớn -> Quét hết các old low bên trái -> Sau đó tạo 1 đỉnh và reject (nến để lại râu dài thân nến nhỏ -> Khả năng Rejection Block)
- Sau đó giá đi ngang hình thành 1 vùng Consolidation từ 28/11/2016 2:00 - 28/11/2016 19:00 ( New York Session)
- Khi New York Open giá hình thành các cây nến Bearish Displacement phá xuống ra khỏi khung Consolidation
- Nhịp displacement giảm tạo thành 1 đáy sau đó hồi lên vùng FVG H1 (tạo từ nhịp displacement), sau đó giảm tiếp và hình thành 1 Equal Low
- Sau khi hình thành EQL, giá tăng mạnh (displacement) với các nến thân lớn
- Giá retrace về vùng POI lúc 11:00 ngày 30/11/2016
- Xuống khung M5 quan sat phản ứng. Không tìm entry vội vì đang không trong Killzone (London, New York)

---

## M5 / M1 — Xác nhận & điểm vào lệnh

### Phân tích:
- Xuống khung M5 quan sát khi giá retrace về tới vùng POI
- Giá quét lên cạnh trên của Order Block. Giá quét lên trên nhưng sau đó đóng nến nược trở lại vào trong OB
- Sau nhịp sweep đó giá bật mạnh ra khỏi vùng OB tạo thành các swing low liên tiếp
- Giá quét cây nến trước và đóng nến xanh mạnh lên quá qua đỉnh sweep trước đó, tuy nhiên đây cũng là 1 nhịp sweep lúc 11:15 ngày 30/11/2026
- Sau khi tạo đỉnh và đóng nến lại trong OB (Sweep) giá quay đầu giảm mạnh tạo thành Bearish MSS lúc 12:15 30/11/2026
- Nhịp displacement tạo MSS đó để lại 1 FVG lúc 12:10 (1.06453 - 1.06414)
- Chờ giá retrace về vùng FVG này
- Lúc 13:40 giá quét lên vùng FVG với 1 nến xanh đóng bên trong FVG và râu dài lên phía trên (Sweep)
- Entry khi giá quay về cạnh dưới FVG, stoploss đỉnh sweep OB (Stoploss xa)
- **Entry trigger**:
	- Liquidity Sweep: quét minor high FVG M5
	- MSS: M5 phá swing low lúc 12:15 30/11/2026
	- Displacement → tạo M5 FVG lúc 12:10 30/11/2026
	- Retrace về FVG → khớp lệnh.
- **Invalidation (theo kế hoạch)**: giá đóng nến trên đỉnh sweep của OB.
- **Tôi có chờ đủ điều kiện không?** Có (theo đúng plan đã định). khi giá tạo FVG ngay gần đáy displacement tôi dựng lên 2 kịch bản giá về FVG và quay đầu với giá retrace sâu về OB. Tôi tách lệnh ra làm 2 (0.5 slot mỗi lệnh) và vào tại 2 vị trì -> Giá chì quay về FVG sau đó đả chiều giảm tới TP -> tôi khớp 1 lệnh

M5: (ban đầu)
![[Pasted image 20260715141405.png]]

Result:
![[Pasted image 20260715141347.png]]
---

## 2. ICT 2022 Model — Entry Sequence

- [x] **1. Liquidity Sweep** — M5 quét đỉnh OB (BSL) rồi đóng nến ngược lại; sau đó sweep cạnh trên M5 FVG lúc 13:40
- [x] **2. Displacement** — nến M5 giảm sau MSS, tạo FVG (chất lượng marginal — xem Lesson)
- [x] **3. Market Structure Shift (MSS)** — M5 phá swing low lúc 12:15 ngược hướng sweep
- [x] **4. FVG hợp lệ** — M5 FVG 1.06453 – 1.06414 (tạo lúc 12:10)
- [x] **5. Entry** — tại cạnh dưới M5 FVG (1.06434)
- [x] **6. Stop Loss** — trên đỉnh sweep OB + buffer (1.06668) — *SL xa, xem Lesson*
- [x] **7. Take Profit** — SSL/EQL vùng Discount (1.05882)


---

## 3. Setup Quality Checklist

- [x] Bias D1 rõ ràng, không mâu thuẫn H1
- [ ] **POI selection tối ưu** — Tách lệnh làm 2 để cân bằng tỷ lệ khớp lệnh (OB và FVG)
- [~] Giá nằm trong Kill Zone — **cần xác minh** (17:55 UTC+7 có thể đã trôi khỏi London KZ chính; xem Lesson)
- [x] Có Liquidity Sweep trước entry (M1)
- [x] **Displacement rõ ràng** — M5 không FVG rõ, tuy nhiên xa stoploss
- [x] Có MSS hợp lệ (M1)
- [x] POI nằm trong Premium (đúng phía cho Short)
- [x] **Entry trong POI hợp lệ, không đua giá**
- [x] **SL ở vùng invalidation hợp lý** — SL đặt trên đỉnh sweep
- [x] RR ≥ 1:2 (R planned 2.09 — nhưng bị bóp bởi SL xa, xem Lesson)

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: **Hit Take Profit (+2.09R)** — leg vào tại M5 FVG khớp; leg limit tại H1 OB **không khớp** (giá không retrace đủ sâu về OB).

### Điều gì thực sự khiến lệnh THẮNG? (root cause thật)
- Bias top-down đồng thuận (D1 + H1 Bearish) + giá retrace vào **Premium** đúng phía → xác suất Short cao ngay từ context.
- Chuỗi 2022 Model trên M5 hoàn chỉnh: **Sweep đỉnh OB → Displacement giảm → MSS (12:15) → FVG (12:10) → retrace entry**. Đây mới là leg tạo lợi nhuận — **không phải** leg OB.
- TP đặt tại **draw on liquidity** thật (SSL/EQL Discount ~1.05882) → giá có "nam châm" để chạy tới.

### Thị trường có cho tín hiệu xác nhận trước entry không? Có — ít nhất 3:
1. **Sweep kép tại POI**: quét đỉnh OB (H1) rồi đóng nến ngược trở lại — smart money từ chối Premium.
2. **MSS M5 rõ** lúc 12:15 phá swing low → chuyển hướng cấu trúc nội tại.
3. **Sweep cạnh trên M5 FVG** lúc 13:40 (nến xanh râu dài, đóng trong FVG) trước khi quay đầu — đúng "mồi" của FVG entry.

### Setup khớp bao