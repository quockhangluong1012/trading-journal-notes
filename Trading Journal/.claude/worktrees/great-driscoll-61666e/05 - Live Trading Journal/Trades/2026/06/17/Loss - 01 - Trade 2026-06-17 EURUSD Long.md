---
date: 2026-06-18T17:36:00
symbol: EURUSD
position: Long
entry_price: 1.15907
take_profit: 1.16082
stop_loss: 1.15975
kill_zone:
  - London
pnl: -32
r_multiple:
mistakes: "[[Mistake - Not Have Market Structure Shift]]"
tags:
  - Discount
  - FVG
  - KillZones
  - OrderBlock
  - DealingRange
  - DailyBias
planned_rr:
result: Loss
session: London
---
# Trade 2026-06-17 - EURUSD Long Loss

## 1. Pre-market Bias
### D1  
- Bias:  Bullish
- Lý do:  giá đang trong nhịp tăng
![[EURUSD-20260617-D1.png]]
### H1  
- Khung H1 giá đang tạo Higher high/ Higer low
- Giá tạo Order Block khung H1
- OB nằm trong vùng Discount khung H1
- Chờ giá retrace về và vào khung nhỏ hơn kiểm tra
![[EURUSD-20260617-H1.png]]
### M5  
- Giá xuất hiện phản ứng khi di chuyển tới OB
- Hình thành các cây nến có râu dài, nến đó bên ngoài hoặc cạnh OB và râu xuyên vào OB gần tới 50% OB
- Xuống khung nhỏ hơn quan sát
![[EURUSD-20260617-M5.png]]
### M1
- Giá phản ứng khi vào vùng OB
- Giá có cú displacement và hình thành FVG
- Vào lệnh khi giá quay về vùng FVG
  ![[EURUSD-20260617-M1.png]]
## 2. Phân tích sau lệnh:
- **Result**: Hit ==stoploss==
- **Mistake**: [[Mistake - Not Have Market Structure Shift]]
- **Lý do**: Vào đuổi giá vì sợ lỡ mất nhịp giá. Khi dó giá chạm PD Array và xuất hiện displacement, tuy nhiên không có MSS. Tôi bỏ qua một điều kiện xác định quan trọng và vào lệnh Long trong khi các khung M15/M5 là nhịp giá giảm
- Không check các tin tức quan trọng của ngày