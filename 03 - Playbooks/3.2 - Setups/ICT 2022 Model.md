---
type: setup
strategy: ICT 2022 Model
status: superseded-by-playbook
supersedes_note: "File này trước đây rỗng (0 byte) từ 2026-06-18 → 2026-09-07 nhưng được link tới 36 lần"
markets:
  - NAS100
  - EURUSD
created: 2026-06-18
updated: 2026-09-07
tags:
  - setup
  - ict-2022
  - index
---

# ICT 2022 Model — Setup (trang chỉ mục)

> [!important] Đặc tả thi hành đầy đủ nằm ở đây
> 👉 **[[2022 Model A+ Setup]]** — GATE 7 bước · SCORE 8 confluence · quy đổi hạng → size · biểu mẫu thi hành · 3 tầng invalidation · tham số định nghĩa đã khoá.
>
> File bạn đang đọc chỉ là **trang chỉ mục**, giữ lại vì đang có **36 link** trỏ tới nó từ trade note, backtest note và template. Đừng viết luật giao dịch vào đây — mọi luật sống ở playbook.

## Tóm tắt 7 bước (bản rút gọn — không dùng thay playbook)

| # | Bước | Điều kiện fail → No Trade |
|---|---|---|
| 1 | **Bias HTF + DOL** | Bias không rõ, hoặc DOL không phải pool có tên |
| 2 | **Premium/Discount** | Long ở premium, hoặc Short ở discount |
| 3 | **Liquidity sweep** | Chưa quét pool ngược hướng, hoặc quét rồi không từ chối |
| 4 | **MSS + Displacement** | MSS chỉ phá STH · phá bằng wick · displacement <3/4 tiêu chí |
| 5 | **POI sạch** | Không có FVG · FVG đã bị close-through |
| 6 | **Entry = retrace** | Phải chase mới vào được |
| 7 | **SL/TP/RR** | RR < 2.0 · target không phải pool có tên · risk > 0.5% |

> [!danger] GATE thắng SCORE
> Fail **một** bước bất kỳ = **No Trade**, bất kể điểm confluence cao đến đâu.

## Liên kết
- **Đặc tả đầy đủ:** [[2022 Model A+ Setup]]
- Lý thuyết mô hình: [[01 - ICT 2022 Model]]
- Checklist nhanh trước lệnh: [[ICT 2022 Entry Checklist]]
- Xuống khung thấp lúc nào: [[LTF Drop-Down Confirmation Checklist (Khi nao xuong khung thap tai OB H1)]]
- Rủi ro: [[Daily Risk & Circuit Breaker Checklist]] · [[43-Position-Sizing]]
