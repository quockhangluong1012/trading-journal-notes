---
date: 2026-05-13
symbol: NDX
position: Long
result: Loss
session: London
setup: "[[Trading Journal/03 - Playbooks/3.2 - Setups/Venom Model]]"
entry_model: Venom Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,150.00
take_profit: 29,292.00
stop_loss: 29,085.60
pnl: -129
r_multiple:
risk_percent: 5%
mistakes:
  - "[[Mistake - Enter before liquidity sweep]]"
  - "[[Mistake - Risk more than 0.5% total account]]"
tags:
planned_rr: 2.2
---

# Trade 2026-05-13 - NDX Long Loss

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Loss                                              |
| Session         | London                                            |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M1                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           | 29,150.00                                         |
| Stop Loss       | 29,085.60                                         |
| Take Profit     | 29,292.00                                         |
| PnL             | -129                                              |
| R Multiple      | 2.60                                              |

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

![[Pasted image 20260620070643.png]]

---

### H1

Giá đang trên đường hồi về OB khung H1

- **Cấu trúc H1**: HH/HL
- **Dealing Range chính**:
  - High:
  - Low:
  - Premium / Discount: Discount
- **POI chính**:
  - Order Block:
  - FVG:
  - Breaker:
  - Other:
- **Liquidity cần chờ sweep**:
  - 
- **Kịch bản mong muốn**:
  - 

![[Pasted image 20260620070653.png]]

---

### M15 / M5
- Giá có 1 pha quét thanh khoản 1 đáy trước đó và hình thành MSS trong khung nhỏ, tuy nhiên giá chưa về tới OB
- Entry khi xuất hiện MSS và retrace

- **Giá đã vào POI chưa?** No
- **Có Liquidity Sweep chưa?** No
- **Sweep loại nào?**
  - Internal liquidity / External liquidity / Equal Highs / Equal Lows
- **Có Displacement chưa?** No
- **Có MSS chưa?** Yes / No
- **Có FVG hợp lệ chưa?** Yes / No
- **Entry có nằm trong POI không?** Yes / No

![[Pasted image 20260620070706.png]]

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
![[Pasted image 20260620070719.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [ ] Đã xác định Daily Bias rõ ràng
- [ ] Bias không mâu thuẫn với H1/M15
- [ ] Giá đã vào vùng POI hợp lệ
- [ ] Có Liquidity Sweep trước entry
- [ ] Có Displacement rõ ràng
- [ ] Có Market Structure Shift hợp lệ
- [ ] Entry nằm trong FVG / OB / PD Array hợp lệ
- [ ] Stop loss đặt ở vùng invalidation hợp lý
- [ ] RR tối thiểu đạt yêu cầu
- [ ] Đã kiểm tra tin tức quan trọng
- [ ] Không vào lệnh vì FOMO
- [ ] Không revenge trade
- [ ] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- 

### Điều tôi làm sai

- 

### Tâm lý khi vào lệnh

- Bình tĩnh / FOMO / Sợ lỡ kèo / Revenge trade / Không chắc chắn
- Ghi chú:
  - 

### Có tuân thủ plan không?

- **Yes / No**
- Nếu không, tôi đã phá rule nào?
  - 

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit TP / Hit SL / BE / Manual Close
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

- 

### Bài học tâm lý

- 

### Rule cần thêm/cập nhật

- [ ] 

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