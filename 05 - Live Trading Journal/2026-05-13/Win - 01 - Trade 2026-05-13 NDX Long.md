---
date: 2026-05-13
symbol: NDX
position: Long
result: Win
session: New York
setup: "[[Trading Journal/03 - Playbooks/3.2 - Setups/Venom Model]]"
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,127.50
take_profit: 29,227.10
stop_loss: 28,962.00
pnl: 180
r_multiple:
risk_percent: 5%
mistakes:
  - "[[05 - Mistake - Not enough RR]]"
  - "[[07 - Mistake - Risk more than 0.5% total account]]"
tags:
planned_rr: 0.6
---

# Trade 2026-05-13 - NDX Long Win

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Win                                               |
| Session         | London                                            |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M1                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           | 29,127.50                                         |
| Stop Loss       | 28,962.00                                         |
| Take Profit     | 29,227.10                                         |
| PnL             | 180                                               |
| R Multiple      | 1.36                                              |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Bullish - Giá đang trong trend tăng sau nhịp hồi
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity:
  - Sell-side liquidity:
- **Ghi chú quan trọng**:
  - 

![[Pasted image 20260620064723.png]]

---

### H1

- **Cấu trúc H1**: HH/HL / LH/LL / Range
- **Dealing Range chính**:
  - High:
  - Low:
  - Premium / Discount:
- **POI chính**:
  - Order Block:
  - FVG:
  - Breaker:
  - Other:
- **Liquidity cần chờ sweep**:
  - Order Block trong vùng discount bên dưới
- **Kịch bản mong muốn**:
  - Quét order block và rejection

![[Pasted image 20260620064732.png]]

---

### M15 / M5

- Giá thực hiện 1 pha quét thanh khoản bên dưới OB và 1 đáy cũ quan trọng
- Giá quét xuống cạnh dưới Venom box (8:00 - 9:30 AM NY)
- Sau khi qua phản ứng tại OB, giá bật hồi lên
- Giá hình thành BPR theo mô hình Venom
- Entry khi giá retrace

- **Giá đã vào POI chưa?** Yes
- **Có Liquidity Sweep chưa?** Yes
- **Sweep loại nào?**
  - Internal liquidity
- **Có Displacement chưa?** Yes
- **Có MSS chưa?** Yes
- **Có FVG hợp lệ chưa?** Yes
- **Entry có nằm trong POI không?** Yes


![[Pasted image 20260620064740.png]]

---

### M1 Entry Timeframe

- **Entry trigger**:
  - Liquidity Sweep:
  - MSS:
  - Displacement:
  - FVG:
  - OB:
- **Entry reason**:
  - 
- **Invalidation reason**:
  - 
- **Tôi có chờ đủ điều kiện không?** Yes / No

![[Pasted image 20260620064749.png]]

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
- [ ] RR tối thiểu đạt yêu cầu
- [x] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [x] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng daily bias, vùng POI
- Xác định đúng Venum Box
- Chờ giá break 1 cạnh Venom box

### Điều tôi làm sai

- Giá không hình thành BPR của Setup Venom Model nhưng lại vào lệnh theo model này
- Giá tạo MSS + Displacement + FVG và sau đó retrace về FVG -> entry theo mô hình ICT 2022

### Tâm lý khi vào lệnh

- Bình tĩnh
- Ghi chú:
  - Đang học 1 chiến lược giao dịch mới

### Có tuân thủ plan không?

- **No**
- Nếu không, tôi đã phá rule nào?
  - Không chờ giá tạo BPR

---

## 4. Phân Tích Sau Lệnh

- **Result**: Manual Close
- **Mistake chính**:
  - [[Mistake - ]]
- **Nguyên nhân gốc rễ**:
  - 
- **Tại sao lệnh này thua/thắng?**
  - 
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - 
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - 

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Học thêm về Venom Model

### Bài học tâm lý

- Kiên nhẫn chờ setup hình thành

### Rule cần thêm/cập nhật

- [ ] Kiên nhẫn

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