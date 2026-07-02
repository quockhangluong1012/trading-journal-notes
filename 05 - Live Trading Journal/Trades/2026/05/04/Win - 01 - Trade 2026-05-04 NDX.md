---
date: 2026-05-04
symbol: NDX
position: Long
result: Win
session: New York
setup: "[[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model|ICT 2022 Model]]"
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 27,689.00
take_profit: 27,769.60
stop_loss: 27,642.97
pnl: 155.4
r_multiple:
risk_percent: 5%
mistakes:
tags:
  - MarketStructureShift
  - LiquiditySweep
  - FVG
  - SSL
  - OTE
  - KillZones
  - DailyBias
planned_rr: 1.75
---

# Trade 2026-05-04 - SYMBOL Position Result

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Win                                               |
| Session         | New York                                          |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M5                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           | 27,689.00                                         |
| Stop Loss       | 27,642.97                                         |
| Take Profit     | 27,769.60                                         |
| PnL             | 155.4                                             |
| R Multiple      | 1.7                                               |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Thị trường đang trong xu hướng tăng với các đỉnh và đáy cao hơn
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity:
  - Sell-side liquidity:
- **Ghi chú quan trọng**:
  - 

![[NDX-20260504-D1.png]]

---

### H1

- **Cấu trúc H1**: HH/HL / LH/LL / Range
- **Dealing Range chính**:
  - High: 
  - Low:
  - Premium / Discount:
- **POI chính**:
  - Order Block: Có
  - FVG:
  - Breaker:
  - Other:
- **Liquidity cần chờ sweep**:
  - 
- **Kịch bản mong muốn**:
  - Giá thực hiện 1 pha quét sâu qua 1 đáy cũ ( vùng 26659) - Phiên London
  - Giá quét rất sâu với râu nến rất dài
  - Đồng thời vùng đang quét là 1 FVG trên khung H1, quét xuyên qua FVG để lấy những stoploss lên dưới 50% và dưới cạnh dưới FVG
  - Sau khi quét giá rút râu và bật lên sau đó
  - Xuống khung M15 kiểm tra tiếp


![[NDX-20260504-H1.png]]
![[NDX-20260504-H1-2.png]]
---

### M15 / M5

- Giá đang trong phạm vi FVG và đồng thời cũng nằm trong OTE
- Giá bật ngược lại mạnh sâu khi quét (displacement)

- **Giá đã vào POI chưa?** Yes
- **Có Liquidity Sweep chưa?** Yes
- **Sweep loại nào?**
  - Internal liquidity
- **Có Displacement chưa?** Yes
- **Có MSS chưa?** No
- **Có FVG hợp lệ chưa?** Yes / No
- **Entry có nằm trong POI không?** Yes / No

![[NDX-20260504-M15.png]]

---

### M1 Entry Timeframe

- **Entry trigger**:
  - Liquidity Sweep:
  - MSS:
  - Displacement:
  - FVG: Giá tạo FVG
  - OB:
- **Entry reason**:
  - Giá tạo MSS + FVG trên đường di chuyển
  - Entry khi giá retrace về FVG
- **Invalidation reason**:
  - 
- **Tôi có chờ đủ điều kiện không?** No

![[NDX-20260504-M5.png]]

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
- [ ] RR tối thiểu đạt yêu cầu
- [x] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [x] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng Bias
- Xác định đúng vùng POI
- Chờ giá quét thanh khoản
- Chờ giá retrace trước khi vào lệnh

### Điều tôi làm sai

- Chưa chờ MSS hình thành mà đã vào lệnh

### Tâm lý khi vào lệnh

- Vội vàng vào lệnh khi MSS chưa hình thành
- Ghi chú:
  - Cần follow theo checklist that vì vào lệnh chỉ vì displacement + FVG

### Có tuân thủ plan không?

- No**
- Nếu không, tôi đã phá rule nào?
  - Không có MSS

---

## 4. Phân Tích Sau Lệnh

- **Result**: Manual Close
- **Mistake chính**:
  - [[Mistake - Not Have Market Structure Shift]]
- **Nguyên nhân gốc rễ**:
  - [[Mistake - Not Have Market Structure Shift]]
  - [[Mistake - Risk more than 0.5% total account]]
- **Tại sao lệnh này thua/thắng?**
  - Lệnh này thắng 1 phần là do may mắn. Tuy đã đúng hầu hết các confluence, nhưng thiếu 1 điều kiện quan trọng là MSS
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - Không có MSS
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Chờ MSS để đúng setup

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Chờ MSS

### Bài học tâm lý

- Cần kiên nhẫn chờ setup hình thành
- Không vội vàng vào lệnh khi chưa đủ confluence

### Rule cần thêm/cập nhật

- [ ] Cần MSS xác nhận

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone

---

## 7. Final Grade

| Tiêu chí | Điểm |
|---|---|
| Daily Bias | /10 |
| POI Selection | /10 |
| Liquidity Sweep | /10 |
| MSS Confirmation | /10 |
| Entry Execution | /10 |
| Risk Management | /10 |
| Psychology | /10 |

**Overall Grade**: /10

**Trade Quality**: A / B / C / D / F