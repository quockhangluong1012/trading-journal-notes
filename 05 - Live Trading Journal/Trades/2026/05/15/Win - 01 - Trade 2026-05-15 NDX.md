---
date: 2026-05-15
symbol: NDX
position: Long
result: Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,368.10
take_profit: 29,420.60
stop_loss: 29,340.80
pnl: 105
r_multiple:
risk_percent: 5%
mistakes:
  - "[[07 - Mistake - Risk more than 0.5% total account]]"
tags:
planned_rr: 1.92
---

# Trade 2026-05-15 - SYMBOL Position Result

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Win                                               |
| Session         | London                                            |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M5                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           |                                                   |
| Stop Loss       |                                                   |
| Take Profit     |                                                   |
| PnL             |                                                   |
| R Multiple      |                                                   |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Bullish - Giá đang trong trend tăng
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity:
  - Sell-side liquidity:
- **Ghi chú quan trọng**:
  - 

![[Pasted image 20260620062648.png]]

---

### H1

- H1 Bias: Giá trong nhịp hồi - Bearish. Chờ H1 align với khung D1
- Giá tạo 1 Order Block khung H1 từ phiên New York hôm trước

- **Cấu trúc H1**: HH/HL
- **Dealing Range chính**:
  - High: 
  - Low:
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block: Có
  - FVG: Có
  - Breaker:
  - Other: 
- **Liquidity cần chờ sweep**:
  - Chờ quét OB + old lows
- **Kịch bản mong muốn**:
  - Sau khi quét old lows, giá đảo chiều với MSS
  - MSS + Dsiplacement và quan trọng là có FVG
  - Giá retrace về FVG và tăng mạnh

![[Pasted image 20260620062706.png]]

---

### M15 / M5
- Giá retrace về vùng OB H1
- Chờ giá xuyên qua OB -> ko vào lệnh ngay khi giá chạm
- Vào khung M1 tìm tín hiệu MSS

- **Giá đã vào POI chưa?** Yes 
- **Có Liquidity Sweep chưa?** Yes
- **Sweep loại nào?**
  - Internal liquidity
- **Có Displacement chưa?** Yes
- **Có MSS chưa?** Yes
- **Có FVG hợp lệ chưa?** Yes
- **Entry có nằm trong POI không?** Yes

![[Pasted image 20260620062725.png]]

---

### M1 Entry Timeframe

- Giá quét qua vùng 50% (mean threshold) của OB
- Giá bật lên tạo thành 1 MSS
- Đồng thời giá tạo FVG trên đường di chuyển displacement
- Chờ giá hồi về vùng FVG
- Entry khi giá bật lên sau khi fill 50% FVG

- **Entry trigger**:
  - Liquidity Sweep: Quét OB
  - MSS: Có
  - Displacement: Có
  - FVG: Có
  - OB: Có
- **Entry reason**:
  - Có MSS + Dsiplacement + FVG
  - Giá retrace về FVG
- **Invalidation reason**:
  - 
- **Tôi có chờ đủ điều kiện không?** Yes
![[Pasted image 20260620062747.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [x] Đã xác định Daily Bias rõ ràng
- [x] Bias không mâu thuẫn với H1/M15
- [x] Giá đã vào vùng POI hợp lệ
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng
- [x] Có Market Structure Shift hợp lệ
- [x] Entry nằm trong FVG / OB / PD Array hợp lệ
- [x] Stop loss đặt ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt yêu cầu
- [x] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [x] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng Bias
- Xác định đúng POI khung H1
- Kiên nhẫn chờ H1 bias và D1 bias align
- Kiên nhẫn chờ giá quay về vùng POI
- Xuống khung M1 quan sát, kiên nhẫn chờ MSS + FVG hợp lệ
- Vào lệnh khi giá reject tại FVG mới tạo thay vì vào đuổi lệnh

### Điều tôi làm sai

- Chốt lời tất cả tại 1 điểm thay vè chốt từng phần

### Tâm lý khi vào lệnh

- Bình tĩnh
- Ghi chú:
  - Vào lệnh đúng setup
  - Kiên nhẫn chờ setup hình thành

### Có tuân thủ plan không?

- **Yes 
- Nếu không, tôi đã phá rule nào?
  - 

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit TP
- **Mistake chính**:
  
- **Nguyên nhân gốc rễ**:
  - 
- **Tại sao lệnh này thua/thắng?**
  - Kiên nhẫn chờ setup hình thành
  - vào lệnh khi có đủ các điều kiện
  - Không FOMO đuổi theo lệnh
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - 
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Chố lời từng phần

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Chốt lời từng phần (Partially Take Profit)
### Bài học tâm lý

- Kiên nhẫn chờ setup hình thành (Patience)

### Rule cần thêm/cập nhật

- [ ] Partially take profit

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone

---

## 7. Final Grade

| Tiêu chí         | Điểm  |
| ---------------- | ----- |
| Daily Bias       | 8/10  |
| POI Selection    | 10/10 |
| Liquidity Sweep  | 8/10  |
| MSS Confirmation | 10/10 |
| Entry Execution  | 10/10 |
| Risk Management  | 7/10  |
| Psychology       | 8/10  |

**Overall Grade**: 8.7/10

**Trade Quality**: A