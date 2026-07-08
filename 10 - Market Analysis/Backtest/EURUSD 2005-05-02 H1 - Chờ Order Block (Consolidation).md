---
type: market-analysis
status: backtest
date: 2026-07-08
symbol: EURUSD
timeframe: H1
session: replay (FXReplay / OANDA)
htf_bias: bullish (nội bộ, chưa xác nhận trend)
setup: 2022 Model - chờ retrace về Order Block discount
in_trade: false
draw_on_liquidity: BSL đỉnh range (~1.298) → old high 1.31200
key_poi: Order Block 1.288–1.289 (discount)
invalidation: đóng H1 dưới 1.28520
tags:
  - analysis
  - watchlist
  - EURUSD
  - ict-2022
  - order-block
  - consolidation
  - premium-discount
---

# EURUSD H1 — Chờ Order Block (Consolidation) — 2026-07-08

> [!info] Trạng thái
> **WATCHING — không vào lệnh.** Giá đang consolidation trong vùng đỏ. Kế hoạch: **chờ giá retrace về Order Block discount (1.288–1.289)** rồi tìm xác nhận LTF. Không đuổi giá trong range.

![[Pasted image 20260708134519.png]]

> [!warning] Screenshot
> Ảnh chưa được lưu dạng file. Hãy kéo ảnh chart vào `05 - Live Trading Journal/Screenschots/2026/07/` với tên `EURUSD-20260708-H1-1.png` để embed ở trên hoạt động.

## 1. Bối cảnh — HTF → [[12 - Dealing Range]] → [[19 - Liquidity]]

Cấu trúc chủ đạo trên H1 là **bearish**: giá giảm từ **1.31200** (old high, [[07 - Buy-side Liquidity|BSL]] lớn) xuống đáy **1.28520** (support kiêm [[30 - Sell-side Liquidity|SSL]]).

Từ đáy 1.285 xuất hiện một cú **displacement tăng** mạnh (chuỗi nến xanh thân dài). Cây này làm 3 việc cùng lúc:

- **[[20 - Liquidity Sweep|Quét SSL]]** quanh đáy 1.285.
- Tạo **[[21 - Market Structure Shift|MSS]]** tăng nội bộ khung.
- Để lại PD Array: **[[25 - OB - Order Block|Order Block]]** (nhãn "OB" ~1.288–1.289) và một **[[13 - FVG  - Fair Value Gap|FVG]]** trong thân cây đẩy.

→ **Bias nội bộ nghiêng bullish**, [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw on liquidity]] kỳ vọng: BSL đỉnh range (~1.298) → old high **1.31200**. **Cảnh báo trung thực:** đây mới là *intent*, chưa xác nhận trend. Vẫn có thể là raid-rồi-tái-phân-phối để đi tiếp xuống.

## 2. Vùng đỏ = Consolidation / Re-accumulation

Range đang xây thanh khoản hai đầu ([[16 - Internal & External Range Liquidity (IRL & ERL)|IRL/ERL]]):

- **Range high ~1.298** = BSL (stop short nội range + breakout buyers).
- **Range low ~1.292** = SSL (stop long nội range).
- Cụm xám không nhãn ~1.293–1.294 = FVG/OB nội bộ, giá đỡ tạm.

Nguyên tắc: **không giao dịch giữa range** — spread ăn mòn, dễ bị quét hai chiều, RR xấu. Đây là vùng smart money gom lệnh.

## 3. Premium / Discount — lý do không vào lúc này

Dealing range 1.28520 → 1.298:

| Mốc | Giá |
|---|---|
| Range high (BSL) | ~1.298 |
| **Equilibrium (50%)** | **~1.2916** |
| Giá hiện tại | **1.29492** |
| FVG/OB nội bộ | ~1.293–1.294 |
| **Order Block (POI chính)** | **1.288–1.289** |
| Đáy / SSL | 1.28520 |

Giá hiện tại **1.29492 nằm trên equilibrium → PREMIUM**. Với bias bullish, [[27 - Premium Discount|ICT]] yêu cầu **mua ở DISCOUNT**. Vào long bây giờ = mua đắt, ngay dưới BSL → tự biến mình thành thanh khoản cho cú quét đỉnh range. Cụm xám 1.293–1.294 cũng sát equilibrium, **chưa đủ chiết khấu**.

## 4. Kế hoạch — chờ về Order Block

> [!summary] Setup chờ ([[01 - ICT 2022 Model]])
> **POI:** Order Block **1.288–1.289** (discount thật, là gốc displacement → A+). Thay thế: [[10 - Consequent Encroachment (Mean Threshold)|CE]] của FVG nếu giá không về sâu.
> **Trigger vào (bắt buộc có trước khi vào):** giá retrace về POI → tụt M5/M1 → **sweep nhỏ + MSS tăng + FVG entry**.
> **Target:** range high 1.298 (BSL) → mở rộng 1.31200.
> **Invalidation:** đóng H1 **dưới 1.28520** → hủy kịch bản bullish, đọc lại là tiếp diễn giảm.

Ba kịch bản khách quan:

- **A (ưu tiên):** retrace về OB 1.288–1.289 / CE của FVG → xác nhận LTF → long. Mua discount, thuận bias, sau xác nhận.
- **B:** [[33 - Turtle Soup|quét SSL range (~1.292)]] rồi displacement tăng ngược → thường trùng với việc về đúng OB bên dưới → hợp nhất với A.
- **C (cảnh giác):** quét BSL đỉnh range (~1.298) rồi MSS giảm → range chưa resolve theo hướng tăng; **không ôm long "hy vọng breakout"**.

## 5. Kỷ luật

Trong consolidation, việc đúng nhất thường là **không làm gì**. Edge của mô hình 2022 nằm ở *external liquidity raid → displacement → retrace về PD array*, không phải phản ứng từng nến trong range. Note này chỉ chuyển thành trade khi một trong ba trigger trên xuất hiện.

## 6. Câu hỏi cần chốt (để nâng độ tin cậy bias)

Cú displacement từ 1.285 **đã quét SSL/equal lows nào chưa**, hay xuất phát từ giữa hư không? Nếu ngay dưới 1.285 có đáy cũ bị lấy → kịch bản A/B đáng tin hơn. Nếu không có gì để quét → nghiêng về C. *(Cần xem chart rộng hơn về bên trái đáy 1.285.)*

---
*Ghi chú: phiên FXReplay, ngày chart thật không rõ; date = ngày capture (VN, UTC+7). Không log backtest vì không vào lệnh.*
