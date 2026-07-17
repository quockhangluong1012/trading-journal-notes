---
type: backtest
backtest_date: 2026-07-07
trade_date: 2005-04-27
symbol: EURUSD
position: Long
result: Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[17 - Inverse Fair Value Gap - iFVG|IFVG]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29165
stop_loss: 1.29042
take_profit: 1.29467
r_planned: 2.48
r_multiple: 2.48
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-27 — EURUSD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2005-04-27     |
| Position             | Long           |
| Result               | Win            |
| Session              | London         |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bullish        |
| Bias Correct?        | Yes            |
| Entry                | 1.29165        |
| Stop Loss            | 1.29042        |
| Take Profit          | 1.29467        |
| R Planned            | 2.48           |
| R Multiple (kết quả) | 2.48           |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang HH/HL
  - Nhịp displacement có tạo FVG khung D1
  - => Bias chuyển sang Bullish
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day/Week High
  - Sell-side liquidity: Previous Day/Week Low 
![[Pasted image 20260707075638.png]]
### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL
- **Dealing Range**: 
	- High: 1.31266
	- Low 1.28777
	- Giá đang di chuyển về vùng Discount (đúng theo bias Bullish)
- **POI chính**: 
	- Balance Price Range (BPR): 1.29084 - 1.28927
- **Liquidity cần chờ sweep**:
  - Giá lắp Bullish Liquidity Void khung H1 (2005-04-18)
  - Giá phản ứng tại BPR khung H1
### Phân Tích:
- Ngày 18/2/2005 Giá tạo 1 bearish FVG ( khi đó vần là Bias Bearish).
- Sau đó vài cây nến giá tạo 1 nhịp giá displacement với các nến bullish lớn, đồng thời tạo FVG trùng lắp với iFVG (Bearish FVG của nhịp giá trước bị phá lên trên hình thành IFVG) tạo thành 1 vùng BPR
- Nhịp giá tạo BPR này đồng thời hình thành MSS + FVG trên khung D1
- Đồng thời nhịp displacement cũng tạo Liquidity Void
- Sau đó vài ngày giá quay lại fill Liquidity Void đó và retest vùng BPR
- Khung H1, xuất hiện phản ứng ngay sau đó giá di vào khoảng 1/4 vùng với cây nến xanh lớn
- Xuống khung M5 quan sát
![[Pasted image 20260707075743.png]]
## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá phản ứng khi vào vùng BPR (chưa tới CE)
- Giá tạo MSS + FVG với các nến tăng lớn
- Giá quá qua swing high cũ sau đó retrace về vùng FVG
- Entry khi giá vào 50% FVG
- Stoploss: swing low trước đó của nhịp quét ( giữa cạnh trên và CE BPR)
- **Entry trigger**:
  - Liquidity Sweep: Giá lắp Liquidity Void + vùng BPR
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là BPR)
- **Invalidation reason**:
  - Giá đóng qua đáy sweep/ qua BPR
- **Tôi có chờ đủ điều kiện không?** Có
![[Pasted image 20260707075820.png]]

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
	- Đóng 50% lệnh khi giá lắp tới CE của 1 Bearish Liquidity Void phía trên (chỗ này tôi quên mất khi giá quét lên Liquidity Void thường phá rất nhanh mà out sớm mất 50%) - tỉ lệ 2.48R
	- Đóng 50% còn lại khi giá quét qua đỉnh tạo Liquidity Void ( giá quét đúng râu nến qua và đóng lại bên dưới) - tỉ lệ nếu từ gốc lên là 4.2R, từ điểm take partial là 1.72R
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone (London)
  - Giá fill Bullish Liquidity Void (18/04/2005)
  - Giá đang trong vùng Discount
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về discount -> Quét EQL + CE Unicorn -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 80%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
	- Cần nhắc quan sát thêm khung M1 khi giá retrace về FVG M5

---

## 5. Lesson Learned

### Bài học kỹ thuật

> [!summary] POI sâu hơn OTE — lợi thế RR hay bẫy sweep?
> - **POI (BPR) nằm ở ~0.88 – 0.94 retracement của Dealing Range H1** (High `1.31266` / Low `1.28777`), Entry ở ~0.84 — đều **sâu hơn OTE (0.62 – 0.79)**. Về bản chất, vào sâu trong Discount là **tốt cho RR** (mua "rẻ"), KHÔNG phải lỗi.
> - **Nguy hiểm thật nằm ở external liquidity chưa quét:** đáy Dealing Range `1.28777` (external SSL) vẫn còn **~15 pip NẰM DƯỚI đáy BPR (`1.28927`)**. Một POI nằm *phía trên* vũng thanh khoản chưa bị lấy luôn có rủi ro bị **sweep trước** — nếu draw of liquidity thật của phiên là đáy range thì SL `1.29042` bị càn qua trước khi giá đi đúng hướng.
> - **Vì sao lệnh này vẫn thắng:** độ sâu **trùng khớp** với chỗ thuật toán cần lấy thanh khoản — fill **Bullish Liquidity Void (18/04)** + quét EQL — và tôi vào bằng **confirmation M5 (phản ứng → MSS → displacement → FVG → retrace 50%)**, KHÔNG đặt limit mù ở POI sâu. Chính hai yếu tố này trung hoà rủi ro độ sâu.
> - **Phân biệt 2 phép đo fib (điểm dễ nhầm nhất):** OTE đo trên **displacement leg**; Premium/Discount đo trên **Dealing Range**. "Sâu hơn OTE" trên dealing range = tốt (rẻ); nhưng nếu nhịp *displacement* bị retrace > 0.79 thì đó là **cờ vàng cho bias** (nhịp tăng gần bị negate → nghi ngờ order flow).

### Pattern lặp lại (điều cần để ý lần sau)

- **Xu hướng chọn POI rất sâu, sát đáy range.** Lần sau khi POI sâu hơn 0.79 → phản xạ đầu tiên phải là: *"còn external liquidity nào chưa quét nằm dưới POI không?"*
- **Out sớm 50% khi giá quét Liquidity Void** (đã ghi ở mục 4): giá thường phá Void **rất nhanh** → cân nhắc để runner chạy qua Void thay vì chốt tại CE của Void.

### Rule cần thêm/cập nhật vào Playbook

- [ ] **Rule "Deep POI":** Khi POI (BPR/FVG/OB) nằm **sâu hơn 0.79 của Dealing Range** → bắt buộc kiểm tra external liquidity chưa quét bên dưới. Nếu còn → **hoặc** chờ giá quét nốt vũng đó rồi mới tìm entry, **hoặc** giảm size; và **bắt buộc** vào bằng confirmation LTF (M5/M1), cấm limit mù.
- [ ] **Rule ghi log:** luôn ghi rõ đang neo fib vào **displacement leg** (cho OTE) hay **Dealing Range** (cho Premium/Discount) để tránh lẫn khung.
- [ ] **Backtest tag:** đánh tag riêng nhóm lệnh `POI-deeper-than-OTE` để **win rate + expectancy của nhóm** tự phán xử — đừng để 1 lệnh Win "phong thánh" cho kiểu entry này (cảnh giác curve-fitting, đây mới là 1 mẫu).

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | /10 |
| POI Selection | /10 |
| Liquidity Sweep | /10 |
| MSS Confirmation | /10 |
| FVG / OB Entry | /10 |
| Risk Management (RR) | /10 |

**Overall Grade**: A

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
