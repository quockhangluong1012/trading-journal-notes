---
date: 2026-06-18T21:31:00
symbol: NDX
position: Short
entry_price: 30,214.9
take_profit: 29,989.2
stop_loss: 30,323.0
kill_zone:
  - New York
pnl: -32.43
r_multiple:
mistakes: "[[03 - Mistake - Entry When MSS not in POI Zone]]"
tags:
  - DailyBias
  - KillZones
  - LiquiditySweep
  - OrderBlock
  - FVG
  - Premium
planned_rr: 2.09
result: Loss
session: New York
---
# Trade 2026-06-17 - EURUSD Long Loss

## 1. Pre-market Bias
### D1  
- Bias:  Bearish
- Lý do:  giá đang trong nhịp Pullback và đang giao dịch bên trong thân nến ngày trước đó
![[NDX-20260618-D1.png]]
### H1  
- Giá tạo quét đỉnh ( Liquidity Sweep), asu đó giá quay ngược trở lại vào range

![[NDX-20260618-H1.png]]

### M5  
-  tôi đã mắc sai lầm khi chỉ chú ý giá quay ngược lại range + displacement + FVG
- Lỗi nghiêm trọng: giá quét thanh khoản tại 1 vùng không có bất kỳ POI nào ( OB, FVG, ..)
![[NDX-20260618-M5.png]]
## 2. Phân tích sau lệnh:
- **Result**: Hit ==stoploss==
- **Mistake**: [[06 - Mistake - Not Have Market Structure Shift]]
- **Lý do**: Thấy giá quét thanh khoản khung H1 khi đó tôi đã xuống ngay khung thời gian nhỏ hơn để tìm điểm vào lệnh mà quên mất ngay vùng đó không có bất kỳ 1 POI nào -> Quá tập trung tìm MSS mà quên mất phải chờ giá retrace về vùng POI sau đó tìm xác nhận