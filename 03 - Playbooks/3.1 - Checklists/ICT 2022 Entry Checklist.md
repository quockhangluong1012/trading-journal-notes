---
type: checklist
category: pre-trade
strategy: ICT 2022 Model
markets:
  - NAS100
  - EURUSD
created: 2026-06-18
updated: 2026-09-07
tags:
  - checklist
  - pre-trade
  - ict-2022
---

# ICT 2022 Entry Checklist — thẻ nhanh trước lệnh

> [!info] Đây là thẻ nhanh, không phải đặc tả
> Dùng để **bấm nhanh tại hard right edge** khi setup đang hình thành. Đặc tả đầy đủ (ngưỡng số, cách chấm điểm, biểu mẫu log) nằm ở **[[2022 Model A+ Setup]]** — đọc file đó **trước phiên**, dùng file này **trong phiên**.

---

## A. GATE — 7 ô, thiếu một ô là No Trade

- [ ] **1. Bias HTF rõ** (Long / Short — không phải "không rõ") + **DOL là pool có tên, có giá**
- [ ] **2. Đúng phía P/D** — Long ở **discount**, Short ở **premium** (midpoint 50%, không có vùng đệm)
- [ ] **3. Sweep ĐÃ xảy ra** — quét pool ngược hướng **rồi từ chối**, trước displacement
- [ ] **4. MSS phá ITH bằng CLOSE** + giữ 3–5 nến + **displacement ≥3/4 tiêu chí** + MSS nằm trong POI
- [ ] **5. POI sạch** — FVG từ displacement, chưa bị **close-through**
- [ ] **6. Entry là RETRACE** — limit tại CE, **không chase**
- [ ] **7. SL ngoài cú sweep · TP là pool có tên · RR ≥ 2.0 · risk ≤ 0.5%**

> [!danger] Ba ô hay bị bỏ qua nhất
> **Ô 3 (sweep)** — thiếu sweep thì đây không phải ICT 2022 Model.
> **Ô 4 (ITH không phải STH)** — phá swing 3-nến nội bộ là nhiễu, không phải MSS.
> **Ô 6 (retrace)** — chase là No Trade, không có ngoại lệ.

## B. SCORE — chấm sau khi GATE pass

1.POI≥3 ☐ · 2.CE∩OTE ☐ · 3.SMT ☐ · 4.CISD ☐ · 5.Macro ☐ · 6.NWOG/HTF ☐ · 7.SD/ERL ☐ · 8.IDM ☐

**Tổng ___/8** → ≥5 = **A+** (≤0.5%) · 3–4 = **A** (0.3–0.5%) · 2 = **B** (≤0.25%) · 0–1 = **C → No Trade**

## C. Chặn cuối trước khi bấm

- [ ] Chưa đủ 2 lệnh hôm nay
- [ ] Chưa chạm daily stop −1%
- [ ] Chưa thua 2 lệnh liên tiếp hôm nay
- [ ] Đang trong killzone (20:30–23:00 VN)
- [ ] Không sát giờ tin đỏ
- [ ] **Không đang mệt / tức giận / muốn gỡ lệnh trước**

## D. Sau lệnh — bắt buộc

- [ ] 1R → chốt 50% + dời SL về BE
- [ ] Ghi `exit_price` **đo thật**, `spread_cost`, `r_net` (không copy từ TP kế hoạch)
- [ ] **Ghi cả setup bị loại** hôm nay và bị loại ở bước nào

## Liên kết
- Đặc tả đầy đủ: [[2022 Model A+ Setup]]
- Lý thuyết: [[01 - ICT 2022 Model]]
- Xuống khung thấp lúc nào: [[LTF Drop-Down Confirmation Checklist (Khi nao xuong khung thap tai OB H1)]]
- Chống bẫy đám đông: [[Anti-Crowd-Trap Checklist (Chống bẫy đám đông ICT)]]
- Rủi ro: [[Daily Risk & Circuit Breaker Checklist]]
