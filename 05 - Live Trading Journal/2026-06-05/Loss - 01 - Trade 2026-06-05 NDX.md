---
date: 2026-06-05
symbol: NDX
position: Long
result: Loss
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,782.00
take_profit: 30,000.00
stop_loss: 29,672.60
pnl: -244
r_multiple:
risk_percent: 0.5%
mistakes:
  - "[[09 - Mistake - Wrong daily bias]]"
  - "[[06 - Mistake - Not Have Market Structure Shift]]"
  - "[[02 - Mistake - Enter before liquidity sweep]]"
tags:
planned_rr: 1.99
---

# Trade 2026-06-05 - NDX Long Loss

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Loss |
| Session | New York |
| Setup | ICT 2022 Model |
| Entry Model | Liquidity Sweep + MSS + FVG |
| Entry Timeframe | M5 |
| HTF Bias | Bullish |
| Bias Correct? | No |
| Entry | 29,782.00 |
| Stop Loss | 29,672.60 |
| Take Profit | 30,000.00 |
| PnL | -244 |
| R Multiple | 1.99 |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Pullback
- **Lý do xác định bias**:
  - Giá đang trong nhịp hồi khung D1
  - Bias nên là Bearish thay vì Bullish

- **Liquidity mục tiêu D1**:
  - Buy-side liquidity: 30,509
  - Sell-side liquidity: 28,803
- **Ghi chú quan trọng**:
  - Vấn đề là intraday tuy nhiên lại xác định bias dựa trên bức tranh quá lớn

![[NDX-20260605-D1.png]]

---

### H1

- **Cấu trúc H1**:  LH/LL
- **Dealing Range chính**:
  - High: 30,537
  - Low: 29,712
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block: vùng 29,745
  - FVG: vùng 29,982
  - Breaker: không có
  - Other: không có
- **Liquidity cần chờ sweep**:
  - 29,982 : FVG
- **Kịch bản mong muốn**:
  - Giá quay về vùng Order block và xuất hiện phản ứng
  - Xuống khung M5 xem giá phản ứng khi đó

![[NDX-20260605-H1.png]]

---

### M15 / M5

Notes:
- Giá bật lên cới các nến xanh liên tiếp
- Tuy nhiên không có MSS + FVG
- Nến xanh cũng không phải displacement
- Vào lệnh khi giá retrace sau nhịp tăng. Thời điểm đó entry không nằm trong FVG ( theo mô hình ICT 2022 - MSS + displacement + FVG)

- **Giá đã vào POI chưa?** Yes
- **Có Liquidity Sweep chưa?** Yes 
- **Sweep loại nào?**
  - Internal liquidity - Order Block
- **Có Displacement chưa?** No
- **Có MSS chưa?** No
- **Có FVG hợp lệ chưa?** No
- **Entry có nằm trong POI không?** Yes

![[NDX-20260605-M15.png]]

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
	- Tôi đã vào lệnh khi chưa đủ điều kiện xác nhận
---

## 2. Checklist Trước Khi Vào Lệnh

- [ ] Đã xác định Daily Bias rõ ràng
- [ ] Bias không mâu thuẫn với H1/M15
- [x] Giá đã vào vùng POI hợp lệ
- [ ] Có Liquidity Sweep trước entry
- [ ] Có Displacement rõ ràng
- [ ] Có Market Structure Shift hợp lệ
- [ ] Entry nằm trong FVG / OB / PD Array hợp lệ
- [x] Stop loss đặt ở vùng invalidation hợp lý
- [ ] RR tối thiểu đạt yêu cầu
- [ ] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [ ] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng Dealing Range
- Xác định đúng Order Block, FVG

### Điều tôi làm sai

- Xác định sai Daily Bias
- Cố vào lện khi không có MSS + displacement + FVG

### Tâm lý khi vào lệnh

- Sợ lỡ kèo
- Ghi chú:
  - Sợ bỏ lõ kèo vì cả ngày không tìm thấy setup nên vào cố dẫn đến stoploss

### Có tuân thủ plan không?

- **No**
- Nếu không, tôi đã phá rule nào?
  - Cố vào lệnh khi không có bất cứ confluence nào
  - Xác định sai bias -> chỉ tập trung vào các setup bullish -> chỉ tập trung MSS -> không chờ MSS mà đã vào lệnh khi giá chỉ quay đầu tăng nhẹ và retrace

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit SL
- **Mistake chính**:
  - [[09 - Mistake - Wrong daily bias]]
  - [[06 - Mistake - Not Have Market Structure Shift]]
- **Nguyên nhân gốc rễ**:
  - Xác định sai Daily bias dẫn đến chỉ tìm những setup bullish trong khi bias đúng ra là Bearish
- **Tại sao lệnh này thua?**
  - Cố vào lệnh khi không có setup
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - Giá không có MSS -> sau đó giá giảm tiếp xuống dưới các đáy
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Xác định bias cho chuẩn
  - Đánh dấu các vùng POI để tránh bị bẫy giá tạo MSS nhưng không nào trong vùng POI
  - Chờ MSS + Displacement + FVG
  - Chờ giá retrace về đúng FVG

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Quan trọng nhất là xác định đúng daily bias, có thể thay đổi bias nếu điều kiện thị trường khi đó đã thay đổi

### Bài học tâm lý

- Không cố vào lệnh khi không có setup
- Nếu 1 ngày không có lệnh nào cũng không sao -> TUYỆT ĐỐI KHÔNG VÀO LỆNH KHI KHÔNG ĐÚNG SETUP

### Rule cần thêm/cập nhật

- [ ] Tránh FOMO

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
| Daily Bias       | 0/10 |
| POI Selection    | 5/10 |
| Liquidity Sweep  | 4/10 |
| MSS Confirmation | 0/10 |
| Entry Execution  | 0/10 |
| Risk Management  | 8/10 |
| Psychology       | 4/10 |

**Overall Grade**: 2/10

**Trade Quality**: F