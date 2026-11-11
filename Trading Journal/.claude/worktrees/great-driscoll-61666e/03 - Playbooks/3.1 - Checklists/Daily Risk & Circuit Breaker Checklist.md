---
type: checklist
category: risk-management
strategy: ICT 2022 Model
tags:
  - risk
  - circuit-breaker
  - discipline
---

# Daily Risk & Circuit Breaker Checklist

> [!info] Mục đích
> Bảo vệ tài khoản trước khi nghĩ đến lợi nhuận. Checklist này ép tuân thủ **rule rủi ro cứng** và **dừng đúng lúc**. Một "lệnh thua đẹp" (đúng quy trình) tốt hơn một "lệnh thắng xấu" (phá rule).

## Rule rủi ro cứng (không thương lượng)

> [!danger] Giới hạn bắt buộc
> - **≤ 0.5% tài khoản / lệnh.** Vượt 0.5% là VI PHẠM — xem [[Mistake - Risk more than 0.5% total account]].
> - **Daily loss limit: -1% / ngày** (tương đương ~2 lệnh thua full SL). Chạm là **DỪNG hết ngày**.
> - **Weekly loss limit: -3% / tuần.** Chạm là **DỪNG hết tuần**, chuyển sang backtest/review.
> - **Tối đa 2 lệnh thua liên tiếp** → đóng máy, không vào thêm.
> - **Tối đa 3 lệnh / ngày.** Không "gỡ", không nhồi lệnh.

---

## 1. Trước phiên (Pre-session)

- [ ] Đã xác định **Daily Bias** rõ ràng, không mâu thuẫn H1/M15 — xem [[Mistake - Wrong daily bias]]
- [ ] Đã đánh dấu liquidity mục tiêu (BSL/SSL) và POI hợp lệ
- [ ] Đã kiểm tra **high-impact news** trong phiên (tránh entry sát giờ tin)
- [ ] Đã xác định **rủi ro $ cho 0.5%** dựa trên SL dự kiến (tính lot/size trước, không tính vội khi vào lệnh)
- [ ] Chỉ trade thị trường trong kế hoạch (ưu tiên **NQ1/NDX**); không "đi lạc" sang EU/GU/Gold ngoài plan — xem [[Mistake - Emotional revenge trade]]
- [ ] Trạng thái tâm lý ổn định (ngủ đủ, không cay cú từ hôm trước)

---

## 2. Cổng vào lệnh (Per-trade gate)

> [!warning] Chỉ vào lệnh khi **TẤT CẢ** đều ✅
> - [ ] HTF Bias rõ ràng, giá đang ở vùng **POI hợp lệ**
> - [ ] Có **Liquidity Sweep** trước entry — xem [[Mistake - Enter before liquidity sweep]]
> - [ ] Có **Displacement** + **MSS** hợp lệ — xem [[Mistake - Not Have Market Structure Shift]]
> - [ ] MSS nằm **trong vùng POI** (không entry khi MSS ngoài POI) — xem [[Mistake - Entry When MSS not in POI Zone]]
> - [ ] Entry trong FVG / OB / PD Array hợp lệ
> - [ ] SL ngoài vùng invalidation; **risk ≤ 0.5%**
> - [ ] **RR tối thiểu ≥ 2.0** — xem [[Mistake - Not enough RR]]
> - [ ] Không FOMO, không vào lệnh ngoài kế hoạch

---

## 3. Circuit Breaker (Bộ ngắt mạch)

> [!danger] DỪNG NGAY khi chạm bất kỳ điều kiện nào
> - [ ] Đã thua **2 lệnh** trong ngày → **đóng máy hết ngày**
> - [ ] Lỗ ngày chạm **-1%** → **đóng máy hết ngày**
> - [ ] Lỗ tuần chạm **-3%** → **dừng hết tuần**, chuyển sang backtest + weekly review
> - [ ] Đã vào đủ **3 lệnh** trong ngày → dừng, bất kể thắng/thua
> - [ ] Cảm thấy muốn "gỡ" / cay cú / vào lệnh không có setup → **đứng dậy 15 phút**, xem [[Mistake - Emotional revenge trade]]

> [!summary] Sau khi circuit breaker kích hoạt
> Không bàn cãi với chính mình. Ghi lại lý do dừng vào daily note, screenshot trạng thái, và để lại cho weekly review. Việc dừng đúng lúc **là** một quyết định thắng.

---

## 4. Cuối ngày (End-of-day)

- [ ] Tổng risk hôm nay ≤ giới hạn? (mỗi lệnh ≤ 0.5%, ngày ≤ -1%)
- [ ] Có lệnh nào phá rule không? Nếu có → tạo/đính kèm `[[Mistake - ...]]`
- [ ] Đã log đầy đủ frontmatter cho mọi lệnh (result, pnl, r_multiple, planned_rr, mistakes)?
- [ ] 1 dòng bài học cho ngày mai

> [!note] Liên kết
> Rule này phục vụ mục tiêu [[Cut my top 3 repeated mistakes]] và [[Hold daily journaling and process discipline]].
