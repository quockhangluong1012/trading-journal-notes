---
date: 2026-06-02
symbol: NDX
position: Long
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 30,515.50
take_profit: 30,634.10
stop_loss: 30,475.10
pnl: 265
r_multiple:
risk_percent: 5%
mistakes:
  - "[[07 - Mistake - Risk more than 0.5% total account]]"
tags:
  - BOS
  - DailyBias
  - LiquiditySweep
  - FVG
  - SSL
  - Discount
  - KillZones
planned_rr: 2.94
---

# Trade 2026-06-02 - SYMBOL Position Result

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Win                                               |
| Session         | New York                                          |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M1                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           | 30,515.50                                         |
| Stop Loss       | 30,475.10                                         |
| Take Profit     | 30,634.10                                         |
| PnL             | 265.00                                            |
| R Multiple      | 2.94                                              |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: PullBack
- **Lý do xác định bias**:
  - Giá đang trong trend tăng, tuy nhiên hiện tại đang trong nhịp Pullback
  - Khung H1 đang trong trend tăng
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity: 30,739
  - Sell-side liquidity: 30,369
- **Ghi chú quan trọng**:
  - Scalping ngắn vì D1 đang trong nhịp Pullback nên khung H1 sẽ có nhịp giảm để đồng pha với khung D1
  - Lệnh này vào khung M1 nên xác định bias dụa trên khung H1. 
  - H1 -> M15 -> M1

![[NDX-20260602-D1.png]]

---

### H1

- **Cấu trúc H1**: HH/HL / LH/LL / Range
- **Dealing Range chính**:
  - High: 30,739
  - Low: 30,369
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block: Vùng 30,506
  - FVG: 
  - Breaker:
  - Other:
- **Liquidity cần chờ sweep**:
  - Chờ giá quét thanh khoản vùng Order Block và vùng old low (30,265)
- **Kịch bản mong muốn**:
  - Sau khi quét OB và old low, giá bật lên tạo MSS + Displacement + FVG trên khung M15

![[NDX-20260602-H1.png]]

---

### M15 / M5

- **Giá đã vào POI chưa?** Yes
- **Có Liquidity Sweep chưa?** Yes 
- **Sweep loại nào?**
  - External liquidity
- **Có Displacement chưa?** Yes
- **Có MSS chưa?** No
- **Có FVG hợp lệ chưa?** No
- **Entry có nằm trong POI không?** Yes

![[NDX-20260602-M15.png]]

---

### M1 Entry Timeframe

- **Entry trigger**:
  - Liquidity Sweep: Quét qua OB + old low
  - MSS: Giá không tạo MSS
  - Displacement: có displacement
  - FVG: Giá không tạo FVG
  - OB:
- **Entry reason**:
  - Giá phản ứng khi chạm OB và bật ra
- **Invalidation reason**:
  - Giá đóng qua đáy cũ
- **Tôi có chờ đủ điều kiện không?** No - Không có MSS + FVG

![[NDX-20260602-M1.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [x] Đã xác định Daily Bias rõ ràng
- [x] Bias không mâu thuẫn với H1/M15
- [x] Giá đã vào vùng POI hợp lệ
- [x] Có Liquidity Sweep trước entry
- [ ] Có Displacement rõ ràng
- [ ] Có Market Structure Shift hợp lệ
- [ ] Entry nằm trong FVG / OB / PD Array hợp lệ
- [x] Stop loss đặt ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt yêu cầu
- [ ] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [x] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng bias H1 do vào lệnh khung M1
- Xác định đúng Order block

### Điều tôi làm sai

- Không có MSS xác định reversal
- Vào lệnh khi giá vừa retrace mà không có MSS + FVG -> entry phải nằm trong FVG của MSS hợp lệ
- Dùng H1 bias thay vì Daily bias để consistence với các lệnh khác
- FOMO
- Ăn may lệnh này, out sớm trước khi giá di chuyển đóng xuống dưới đáy cũ

### Tâm lý khi vào lệnh

- Sợ lỡ kèo
- Ghi chú:
  - Vội vàng

### Có tuân thủ plan không?

- **Yes / No**
- Nếu không, tôi đã phá rule nào?
  - 

---

## 4. Phân Tích Sau Lệnh

- **Result**: Manual Close - Đạt profit tuy nhiên đây xét các yếu tố thì là lệnh ăn may, thoát sớm trước khi giá đảo chiều theo dialy bias và đóng xuống dưới OB và đáy cũ
- **Mistake chính**:
  - [[06 - Mistake - Not Have Market Structure Shift]]
- **Nguyên nhân gốc rễ**:
  - [[09 - Mistake - Wrong daily bias]]
- **Tại sao lệnh này thua/thắng?**
  - Lệnh này thắng do ăn may, thoát lệnh trước khi giá đồng pha (align) với khung D1
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - Không có MSS, daily bias và H1 bias ngược nhau
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Tuy là 1 lệnh thắng tuy nhiên nếu được làm lại tôi sẽ giao dịch đúng theo daily bias -> bearish và tìm các conflence cho lệnh Short. Giá quay lại vùng FVG sau khi phá đáy có thể cân nhắc short thay vì long như lệnh gốc

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Follow Daily bias nếu thị trường chưa đổi cấu trúc
- Chờ MSS (Quan trọng) + Displacement + FVG
- Chỉ entry khi giá retrace về FVG hợp lệ

### Bài học tâm lý

- Không FOMO, sợ bỏ lỡ kèo
- Xác định bias cho kỹ

### Rule cần thêm/cập nhật

- [ ] Xác định Daily Bias

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone

---

## 7. Final Grade

| Tiêu chí         | Điểm |
| ---------------- | ---- |
| Daily Bias       | 4/10 |
| POI Selection    | 8/10 |
| Liquidity Sweep  | 8/10 |
| MSS Confirmation | 0/10 |
| Entry Execution  | 4/10 |
| Risk Management  | 4/10 |
| Psychology       | 4/10 |

**Overall Grade**: 4.5/10

**Trade Quality**: D