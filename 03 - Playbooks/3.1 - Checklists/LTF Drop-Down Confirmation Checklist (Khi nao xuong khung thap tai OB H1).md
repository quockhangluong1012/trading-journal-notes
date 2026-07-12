---
type: checklist
category: entry-timing
strategy: ICT 2022 Model
tags:
  - timeframe-layering
  - confirmation
  - entry-timing
  - rejection
---

# LTF Drop-Down Confirmation Checklist (Khi nào xuống khung thấp tại OB H1)

> [!info] Mục đích
> Checklist này trả lời một câu hỏi timing cụ thể: **khi giá retrace về OB/FVG khung H1, chính xác lúc nào được phép xuống khung thấp (M5/M1) để soi tín hiệu rejection — và tín hiệu đó phải trông như thế nào để được coi là hợp lệ.** Nó chống lại hai lỗi ngược nhau: xuống LTF quá sớm rồi bị nhiễu (noise) làm mất kiên nhẫn, và coi một cái wick dài là "rejection" mà vào lệnh không xác nhận. Nền tảng lý thuyết: [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]] và [[32 - Top-down Analysis (Multiple Timeframes)]].

> [!danger] Nguyên tắc vàng
> **Giá chạm POI là điều kiện "ARM" (lên nòng) — KHÔNG phải "TRIGGER" (bóp cò).** H1 OB chỉ cho biết *vào ở đâu*, không bao giờ cho biết *vào lúc nào*. Thời điểm chỉ đến từ một chuỗi xác nhận trên khung thấp: **sweep nội bộ → displacement + MSS → FVG entry.** Một cái wick dài trên H1 chỉ là *hệ quả* in ra SAU KHI chuỗi này đã xảy ra ở khung nhỏ — nó không phải tín hiệu để bạn vào.

---

## 1. Cổng ARM — chỉ được xuống LTF khi TẤT CẢ đúng

> [!warning] Chưa đủ các mục dưới đây → giữ nguyên H1, KHÔNG mở M5/M1
- [ ] Context ủng hộ: OB/FVG này **đồng hướng [[12 - Daily Bias|bias HTF]]** và là POI hợp lệ, không nằm giữa range
- [ ] OB nằm đúng phía của dealing range (short → OB ở **premium**; long → OB ở **discount**) — xem [[27 - Premium Discount]]
- [ ] Giá đã **vật lý chạm** đúng phần của OB, không phải "còn gần":
	- [ ] Bảo thủ: tag **proximal edge** (biên gần nhất của OB)
	- [ ] Chuẩn: tag **CE — Consequent Encroachment (50% của OB/FVG)** — xem [[10 - Consequent Encroachment (Mean Threshold)]]
- [ ] Đang trong **[[18 - Kill Zones|Kill Zone]]** (London / NY). Ngoài Kill Zone → hạ độ tin cậy, cân nhắc chờ phiên sau
- [ ] Tôi đã đặt **price alert tại proximal edge và CE** thay vì dán mắt màn hình (kỷ luật chống xuống LTF quá sớm)

> [!tip] Vì sao dùng alert
> Xuống LTF khi giá còn cách 20–30 điểm khiến bạn nhìn nhiễu quá lâu, mất kiên nhẫn và **front-run** setup. Alert kêu mới mở khung nhỏ = bạn chỉ tiêu tốn sự chú ý đúng lúc nó đáng giá.

---

## 2. Cổng CONFIRM trên LTF — chuỗi 2022 Model (không có = không vào)

> [!warning] Sau khi mở M5/M1, chờ ĐÚNG chuỗi này — không vào chỉ vì "thấy nến đỏ/xanh"
- [ ] **Sweep nội bộ:** giá quét một đỉnh/đáy nhỏ *bên trong* OB, hút nốt thanh khoản cuối (mini [[33 - Turtle Soup]]) — xem [[20 - Liquidity Sweep]], [[02 - Mistake - Enter before liquidity sweep]]
- [ ] **Displacement thật:** nến đi mạnh, dứt khoát, **để lại FVG** cùng hướng — không phải nhịp mồi rồi hồi ngay; tránh [[08 - Mistake - Weak Displacement]]
- [ ] **MSS/CHoCH** phá gãy cấu trúc gần nhất của LTF, **cùng hướng bias HTF** — xem [[21 - Market Structure Shift]], [[06 - Mistake - Not Have Market Structure Shift]]
- [ ] MSS nằm **trong vùng POI**, không phải MSS giả giữa range — xem [[03 - Mistake - Entry When MSS not in POI Zone]]

> [!summary] Định nghĩa "rejection hợp lệ"
> Rejection KHÔNG phải một cái wick dài. **Rejection hợp lệ = sweep + displacement + MSS trên LTF.** Nếu chỉ thấy wick mà không có chuỗi này → đó là bật cơ học, không phải tín hiệu.

---

## 3. Cổng ENTRY — refine điểm vào

- [ ] Entry tại **FVG / OB nhỏ do displacement vừa tạo**, refine bằng **CE** của array đó — xem [[13 - FVG  - Fair Value Gap]], [[25 - OB - Order Block]]
- [ ] **SL** đặt ngoài đỉnh/đáy của cú sweep (ngoài vùng invalidation), **risk ≤ 0.5%**
- [ ] **Target = DOL đã xác định trước** (BSL/SSL phía đối diện), **RR ≥ 2.0** — xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]], [[05 - Mistake - Not enough RR]]
- [ ] Không high-impact news sát giờ entry

---

## 4. Khi giá "bật ra ngay" — xử lý tình huống lỡ

> [!danger] Đây là đánh đổi cốt lõi — chọn MỘT trường phái, không trộn
> - **Trường phái A — Confirmation entry (mặc định cho foundation/backtest):** chờ MSS trên LTF. An toàn hơn, SL nhỏ hơn, khớp đúng luật [[01 - ICT 2022 Model]]. **Cái giá:** lỡ những cú rejection V-shape tức thời. **Chấp nhận được** — một cú lỡ tốn 0 đồng.
> - **Trường phái B — POI/Limit entry:** đặt limit tại CE, SL theo H1. Bắt được cú bật tức thời nhưng **không có xác nhận**, dễ bị OB "ăn qua". Chỉ dùng khi đã backtest riêng và conviction HTF rất cao.
- [ ] Nếu lỡ → **KHÔNG đuổi lệnh (chase)**. Đánh dấu, chờ retest FVG/OB mới hoặc setup kế tiếp
- [ ] Không đổi sang trường phái B giữa chừng chỉ vì tiếc một cú lỡ — đó là curve-fitting ẩn, pha loãng edge

---

## 5. Cổng cuối cùng (Final gate)

> [!danger] Chỉ vào lệnh khi TẤT CẢ đều đúng
> - [ ] Mục 1: đã ARM đúng (chạm CE/proximal, trong Kill Zone, context ủng hộ)
> - [ ] Mục 2: có đủ **sweep + displacement + MSS** trên LTF, trong POI
> - [ ] Mục 3: entry tại FVG/CE, SL ngoài sweep, risk ≤ 0.5%, RR ≥ 2.0
> - [ ] Mục 4: nếu lỡ thì chấp nhận, không chase, không đổi style

> [!summary] Câu nhắc nhở khi trade
> **"Chạm OB là lên nòng, không phải bóp cò. Tôi chỉ vào khi khung nhỏ in ra sweep + displacement + MSS. Không có MSS = không có lệnh, dù cái wick có đẹp đến đâu."**

---

> [!note] Liên kết
> Nền lý thuyết: [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]] · [[32 - Top-down Analysis (Multiple Timeframes)]] · [[10 - Consequent Encroachment (Mean Threshold)]] · Dùng chồng lên [[ICT 2022 Entry Checklist]], [[Daily Risk & Circuit Breaker Checklist]] và [[Anti-Crowd-Trap Checklist (Chống bẫy đám đông ICT)]] · Model gốc: [[01 - ICT 2022 Model]].
