---
type: market-analysis
status: backtest
date: 2026-07-12
symbol: NAS100
timeframe: D1 / H1
session: replay
htf_bias: bearish (context sau MSS) / bullish retrace ngắn hạn
setup: 2022 Model - chờ retrace về bearish OB premium để short
in_trade: false
draw_on_liquidity: SSL dưới 1974.6 (đã quét) · ngắn hạn hồi lên BSL/OB ~2242.9 · dài hạn BSL 2440
key_poi: Bearish Order Block / FVG 2210–2242.9 (premium)
invalidation: đóng H1 trên 2242.9 (hủy kịch bản short)
tags:
  - analysis
  - watchlist
  - NAS100
  - ict-2022
  - order-block
  - draw-on-liquidity
  - premium-discount
  - daily-bias
---

# NAS100 D1/H1 — Draw on Liquidity & Daily Bias — 2026-07-12

> [!info] Trạng thái
> **WATCHING — không vào lệnh.** Bối cảnh HTF nghiêng **bearish** sau khi giá phá cấu trúc, nhưng hiện đang trong **nhịp hồi tăng**. Kế hoạch: **chờ giá hồi lên bearish OB/FVG 2210–2242.9 (premium)** rồi tìm xác nhận LTF để short. Không vào giữa range tại 2157.

![[NAS100-20260712-D1-1.png]]
![[NAS100-20260712-H1-1.png]]

> [!warning] Screenshot
> Ảnh chưa được lưu dạng file. Hãy kéo hai chart (D1, H1) vào `10 - Market Analysis/Attachments/` với tên `NAS100-20260712-D1-1.png` và `NAS100-20260712-H1-1.png` để embed ở trên hoạt động.

## 1. Bối cảnh — HTF → [[12 - Dealing Range]] → [[19 - Liquidity]]

Trên D1, giá đi trend tăng từ ~2.050 lên đỉnh **2.440** (old high / equal highs, [[07 - Buy-side Liquidity|BSL]] lớn nhất). Từ 2.440 xuất hiện một cú **displacement giảm mạnh** xuyên thủng mức hỗ trợ chủ chốt **2.242,9**, kéo xuống wick chạm đáy **1.974,6** rồi bật lên mạnh về giá hiện tại **2.157,6**.

Cú phá xuống 2.242,9 là một **[[21 - Market Structure Shift|MSS]] giảm trên khung lớn** → bối cảnh HTF **bearish**. Cây nến bật từ 1.974,6 đã **[[20 - Liquidity Sweep|quét SSL]]** dưới đáy (thanh khoản bán đã bị ăn một lần) và tạo nhịp hồi tăng nội bộ trên H1 — đây là **retracement leg bên trong cấu trúc HTF giảm**, chưa phải đảo chiều.

Dealing range tham chiếu: **2.440 (high) → 1.974,6 (low)**.

## 2. [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]] — bản đồ thanh khoản

**Buyside (phía trên):**

- **~2.440** — BSL lớn nhất (HTF), old high / equal highs. Mục tiêu xa nhất nếu đảo chiều tăng.
- **2.242,9** — BSL trung hạn + old support-turned-resistance; ngay dưới là bearish OB/FVG. Đây là **DOL gần nhất phía trên**.
- BSL nội bộ tại swing high H1 ~2.170–2.180.

**Sellside (phía dưới):**

- **1.974,6** — SSL **đã bị quét** (wick D1). Liquidity grab / stop hunt.
- SSL nội bộ dưới đáy range H1 (~2.000 và ~2.075).

→ SSL dưới 1.974,6 vừa bị lấy + phản ứng bằng displacement tăng → **draw ngắn hạn nghiêng LÊN**, về phía imbalance chưa lấp và 2.242,9 (logic "purge and rebalance"). Draw dài hạn theo HTF vẫn là sellside.

## 3. PD Arrays (từ premium xuống discount)

- **Bearish OB / FVG 2.210 – 2.242,9** (ô xám trên H1) — PD array quan trọng nhất. Hình thành *ngay tại điểm phá 2.242,9* → supply chưa mitigate + FVG chưa lấp. Nằm trong **premium**.
- **2.242,9** — S/R flip, biên trên OB, "trần" của cú hồi.
- **EQ ~2.207** — ranh giới premium/discount.
- **Giá hiện tại 2.157,6** — discount, ngay trên imbalance H1 vừa nhảy qua.
- **Discount arrays dưới** — FVG/OB tăng trong nhịp bounce (~2.040–2.080).

## 4. [[27 - Premium Discount]] — vị trí hiện tại

Dealing range 1.974,6 → 2.440:

| Mốc | Giá |
|---|---|
| Range high (BSL) | ~2.440 |
| **Bearish OB / FVG (POI chính)** | **2.210 – 2.242,9** |
| S/R flip | 2.242,9 |
| **Equilibrium (50%)** | **~2.207** |
| Giá hiện tại | **2.157,6** |
| SSL đã quét / đáy | 1.974,6 |

Giá hiện tại **2.157,6 nằm DƯỚI equilibrium → DISCOUNT**. Với ý định short (thuận HTF), ICT yêu cầu **bán ở PREMIUM** — nghĩa là phải chờ giá hồi lên ~50–85 điểm vào vùng OB 2.210–2.242,9. Short ngay tại 2.157 giữa range = bán rẻ, không có PD array chất lượng tại giá, RR xấu.

## 5. Cấu trúc — [[09 - Change of Character|CHoCH]] / [[21 - Market Structure Shift|MSS]]

Ta đang ở **giao lộ**, phải đọc cả hai chiều thay vì cưỡng ép một mũi tên:

- **HTF (D1):** displacement giảm phá 2.242,9 → shift cấu trúc **giảm** → context bearish.
- **LTF (H1):** sau quét 1.974,6, giá tạo higher-low nội bộ, đang bò lên → **nhịp hồi tăng trong xu hướng giảm HTF**, chưa xác nhận đảo chiều.

## 6. Daily Bias — hai kịch bản khách quan

> [!summary] Bias trung thực
> **HTF context bearish, đang trong nhịp hồi tăng; daily bias = "bearish có điều kiện", điểm quyết định nằm ở cụm OB 2.210 – 2.242,9.** Không đọc thành "chắc chắn tăng" hay "chắc chắn giảm".

- **A (ưu tiên — bearish continuation):** giá hồi lên **premium**, vào bearish OB/FVG 2.210–2.242,9 → chờ **MSS giảm LTF** + rejection → short. Target: quét lại SSL dưới **1.974,6**. Ưu điểm logic: short zone ở premium, target ở discount.
	- *Invalidation A:* đóng H1 dứt khoát **trên 2.242,9** và giữ được.
- **B (phụ — bullish reversal):** wick 1.974,6 = liquidity grab tạo đáy; nếu phá & giữ **trên 2.242,9** (OB thành breaker) → draw đổi hướng lên **2.440**. Bias mới flip bullish.
	- *Invalidation B:* bị từ chối tại 2.210–2.242,9 rồi tạo lower-low → quay về A.

## 7. Kế hoạch — chờ về Bearish OB ([[01 - ICT 2022 Model]])

> [!summary] Setup chờ
> **POI:** Bearish OB / FVG **2.210 – 2.242,9** (premium). Refine bằng [[10 - Consequent Encroachment (Mean Threshold)|CE]] của OB/FVG.
> **Trigger vào (bắt buộc):** giá retrace vào POI → tụt M5/M1 → **sweep nội bộ + displacement + MSS giảm + FVG entry**. Quy trình chi tiết: [[LTF Drop-Down Confirmation Checklist (Khi nao xuong khung thap tai OB H1)]].
> **Target:** SSL dưới 1.974,6 (external liquidity). **RR ≥ 2.0**.
> **Invalidation:** đóng H1 trên 2.242,9.

## 8. Kỷ luật

Vùng **2.210 – 2.242,9 là "decision zone"** của cả chart này — đừng đoán trước phản ứng, để giá *chạm vào* rồi mới đọc LTF. Giá hiện tại 2.157 là "no man's land" giữa range: không PD array tại giá, RR xấu, dễ whipsaw. Trong nhịp hồi, việc đúng nhất thường là **chờ POI**, không phản ứng từng nến.

## 9. Câu hỏi cần chốt (nâng độ tin cậy bias)

Cú giảm từ 2.440 **đã quét BSL / equal highs nào ở trên** trước khi đổ xuống chưa? Nếu đỉnh 2.440 là một cú quét BSL rõ ràng rồi mới displacement giảm → kịch bản A (bearish) đáng tin hơn. Đồng thời, cần xem chart rộng hơn bên trái đáy 1.974,6: dưới đó còn SSL/old low nào làm target tiếp theo không.

---
*Ghi chú: phiên replay; ngày chart thật không rõ (chart chỉ ghi tay D1/H1); `date` = ngày capture (VN, UTC+7). Không log backtest vì không vào lệnh — đây là note phân tích/watchlist.*
