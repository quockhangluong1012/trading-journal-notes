---
date: 2026-06-17T08:35:00
symbol: NDX
position: Long
result: Loss
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 30,079.3
take_profit: 30,428.3
stop_loss: 29,931.1
pnl: -44.46
r_multiple:
risk_percent: 0.5%
mistakes:
  - "[[Mistake - Wrong daily bias]]"
  - "[[Mistake - Not Have Market Structure Shift]]"
  - "[[Mistake - Entry When MSS not in POI Zone]]"
tags:
planned_rr: 2.35
---

# Trade 17-06-2026 - SYMBOL Position Result

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Loss |
| Session |  New York |
| Setup | ICT 2022 Model |
| Entry Model | MSS + FVG |
| Entry Timeframe | M5 |
| HTF Bias | Bullish |
| Bias Correct? | No |
| Entry | 30,079.3 |
| Stop Loss | 29,931.1 |
| Take Profit | 30,428.3 |
| PnL | -44.46 |
| R Multiple | 1.75 |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Pullback
- **Lý do xác định bias**:
  - Nhìn trend tổng thể xác định bias. Tuy nhiên model là intraday thì nên tập trung vào những cây nến gần đây
  - Giá break xuống dưới Previous Day Low -> daily bias nên là Bearish thay vì Bullish
  - Xác định sai bias dẫn đến vào lệnh counter trend
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity: 30,679 - LTH
  - Sell-side liquidity: 29,981 - ITL
- **Ghi chú quan trọng**:
  - Giá hình thành 1 GAP lớn vào ngày thứ 2 (Opening Week Gap), giá có khả năng quay về lắp GAP


![[NDX-20260617-D1.png]]

---

### H1

- **Cấu trúc H1**: LH/LL
- **Dealing Range chính**: 
  - High: 30,647.8
  - Low: 29,948
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block:
  - FVG:  
  - Breaker: Không có
  - Other:
- **Liquidity cần chờ sweep**:
  - SSL
- **Kịch bản mong muốn**:
  - Quét SSl xong retrace về FVG

![[NDX-20260617-H1.png]]

---

### M15 / M5

- **Giá đã vào POI chưa?** No
- **Có Liquidity Sweep chưa?**  No
- **Sweep loại nào?**
  - Chưa Sweep
- **Có Displacement chưa?** No
- **Có MSS chưa?** No
- **Có FVG hợp lệ chưa?** No
- **Entry có nằm trong POI không?** No

![[NDX-20260617-M5.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [ ] Đã xác định Daily Bias rõ ràng
- [ ] Bias không mâu thuẫn với H1/M15
- [ ] Giá đã vào vùng POI hợp lệ
- [ ] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng
- [x] Có Market Structure Shift hợp lệ
- [ ] Entry nằm trong FVG / OB / PD Array hợp lệ
- [ ] Stop loss đặt ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt yêu cầu
- [ ] Đã kiểm tra tin tức quan trọng
- [ ] Không vào lệnh vì FOMO
- [ ] Không revenge trade
- [ ] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đính Dealing Range

### Điều tôi làm sai

- Xác định sai Daily Bias
- Tập trung vào tìm MSS trong khi giá đang không năm trong vùng POI
- Vào lệnh đuổi giá (FOMO)
### Tâm lý khi vào lệnh

- FOMO / 
- Revenge trade
- Không chắc chắn
- Ghi chú:
  - 

### Có tuân thủ plan không?

- **No**
- Nếu không, tôi đã phá rule nào?
  - Xác định sai Bias
  - Không chờ MSS
  - Không chờ Liquidity Sweep
  - FOMO

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit SL
- **Mistake chính**:
  - [[Mistake - Wrong daily bias]]
  - [[Mistake - Entry When MSS not in POI Zone]]
  - [[Mistake - Emotional revenge trade]]
- **Nguyên nhân gốc rễ**:
  - Revenge trade, cố gắng vào lệnh để gỡ lại 2 lệnh thua trước đó
- **Tại sao lệnh này thua/thắng?**
  - Xác định sai Bias
  - Không chờ MSS
  - Không chờ Liquidity Sweep
  - FOMO
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - Giá giao dịch dưới Previous Day Low -> Bearish Bias thay vì bullish khi nhìn quá rộng
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Xác định bias cho đúng
  - Xác định Dealing Range, đánh dấu các vùng POI dựa trên Bias
  - Nếu giá cho tín hiệu break bias thì nên chuyển đổi bias theo context hiện tại, không cố bám vào bias ban đầu
  - Chờ Liquidity Sweep rõ ràng
  - Chờ MSS hợp lệ, giá phải break ITH/TML

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Học lại cách xác định daily bias
- Cần thay đổi bias linh hoạt theo điều kiện thị trường thời điểm đó. Không cố giữ bias khi đã invalid

### Bài học tâm lý

- Không FOMO sợ bỏ lỡ kèo. 
	- Nếu setup đẹp mà lỡ nhịp -> Bỏ
	- Nếu chưa đủ các điều kiện cần thiết -> Bỏ
- Không cố trade để trả thủ/gỡ lại các lệnh thua. Mỗi lệnh là độc lập
### Rule cần thêm/cập nhật

- [ ] Xem mỗi lệnh là độc lập, không liên qua tới lệnh cũ
- [ ] Thay đổi bias tùy theo tình huống

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
| POI Selection    | 0/10 |
| Liquidity Sweep  | 0/10 |
| MSS Confirmation | 5/10 |
| Entry Execution  | 5/10 |
| Risk Management  | 8/10 |
| Psychology       | 4/10 |

**Overall Grade**: 3/10

**Trade Quality**: F