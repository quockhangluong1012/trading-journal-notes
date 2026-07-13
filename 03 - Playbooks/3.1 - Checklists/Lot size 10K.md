---
type: reference
title: FTMO 10K - Lot Size & Profit Calculator
account: FTMO 10K
tags: [risk-management, position-sizing, ftmo, expectancy]
created: 2026-07-13
updated: 2026-07-13
---

# FTMO 10K — Bảng Lot Size & Profit Calculator

> [!info] Về note này
> Phiên bản Markdown (tĩnh) của file Excel calculator. Các con số dưới đây tính sẵn cho **tài khoản $10,000**, risk **0.5% ($50/lệnh)** và **1% ($100/lệnh)**. Muốn đổi số dư hay risk% và để bảng tự tính lại, dùng file `[[FTMO 10K - Lot Size & Profit Calculator.xlsx]]` (ô vàng = ô nhập liệu).

## 1. Tham số & giả định

| Tham số | Giá trị |
|---|---|
| Số dư tài khoản | $10,000 |
| Risk thấp | 0.5% = **$50 / lệnh** |
| Risk cao | 1.0% = **$100 / lệnh** |
| Số lệnh / tháng | 20 (1 lệnh/ngày, ~4 tuần) |
| Cách tính lãi | Fixed risk (risk $ cố định trên balance gốc) |

**Giá trị 1.00 lot** (dùng để tính lot size — hãy đối chiếu MT5 → Market Watch → chuột phải → *Specification* cho đúng tài khoản FTMO của bạn):

| Cặp | Giá trị 1 lot | Đơn vị đo SL |
|---|---|---|
| EURUSD | $10 / pip (1 pip = 0.0001) | pip |
| GBPUSD | $10 / pip (1 pip = 0.0001) | pip |
| XAUUSD | $100 / 1.0 USD giá | USD giá (vd 5.0) |
| NAS100 | $1 / 1 point | point (index) |

Công thức nền: **Lot = Risk$ / (SL × giá trị 1 lot)**

## 2. Bảng Lot Size

### EURUSD (SL tính bằng PIP)

| SL (pip) | Lot @ 0.5% | Lot @ 1% |
|---|---|---|
| 10 | 0.50 | 1.00 |
| 15 | 0.33 | 0.67 |
| 20 | 0.25 | 0.50 |
| 25 | 0.20 | 0.40 |
| 30 | 0.17 | 0.33 |
| 40 | 0.13 | 0.25 |
| 50 | 0.10 | 0.20 |
| 75 | 0.07 | 0.13 |
| 100 | 0.05 | 0.10 |

### GBPUSD (SL tính bằng PIP)

| SL (pip) | Lot @ 0.5% | Lot @ 1% |
|---|---|---|
| 10 | 0.50 | 1.00 |
| 15 | 0.33 | 0.67 |
| 20 | 0.25 | 0.50 |
| 25 | 0.20 | 0.40 |
| 30 | 0.17 | 0.33 |
| 40 | 0.13 | 0.25 |
| 50 | 0.10 | 0.20 |
| 75 | 0.07 | 0.13 |
| 100 | 0.05 | 0.10 |

### XAUUSD / GOLD (SL tính bằng USD giá)

| SL (USD) | Lot @ 0.5% | Lot @ 1% |
|---|---|---|
| 2.0 | 0.25 | 0.50 |
| 3.0 | 0.17 | 0.33 |
| 5.0 | 0.10 | 0.20 |
| 7.0 | 0.07 | 0.14 |
| 10.0 | 0.05 | 0.10 |
| 15.0 | 0.03 | 0.07 |
| 20.0 | 0.03 | 0.05 |

### NAS100 (SL tính bằng POINT)

| SL (point) | Lot @ 0.5% | Lot @ 1% |
|---|---|---|
| 20 | 2.50 | 5.00 |
| 30 | 1.67 | 3.33 |
| 50 | 1.00 | 2.00 |
| 75 | 0.67 | 1.33 |
| 100 | 0.50 | 1.00 |
| 150 | 0.33 | 0.67 |
| 200 | 0.25 | 0.50 |

## 3. Profit Expectancy (Win% × RR)

Công thức: **Ký vọng/lệnh (R) = Win% × RR − (1 − Win%)** · **Profit/tháng = R × 20 lệnh × Risk$**

### A) Ký vọng (R / lệnh)

| RR \ Win% | 30% | 40% | 50% | 60% | 70% |
|---|---|---|---|---|---|
| **1 : 1** | −0.40 | −0.20 | 0.00 | 0.20 | 0.40 |
| **1 : 1.5** | −0.25 | 0.00 | 0.25 | 0.50 | 0.75 |
| **1 : 2** | −0.10 | 0.20 | 0.50 | 0.80 | 1.10 |
| **1 : 2.5** | 0.05 | 0.40 | 0.75 | 1.10 | 1.45 |
| **1 : 3** | 0.20 | 0.60 | 1.00 | 1.40 | 1.80 |

### B) Lợi nhuận / tháng ($) @ Risk CAO (1%)

| RR \ Win% | 30% | 40% | 50% | 60% | 70% |
|---|---|---|---|---|---|
| **1 : 1** | −800 | −400 | 0 | +400 | +800 |
| **1 : 1.5** | −500 | 0 | +500 | +1,000 | +1,500 |
| **1 : 2** | −200 | +400 | **+1,000** | +1,600 | +2,200 |
| **1 : 2.5** | +100 | +800 | +1,500 | +2,200 | +2,900 |
| **1 : 3** | +400 | **+1,200** | +2,000 | +2,800 | +3,600 |

### C) Lợi nhuận / tháng ($) @ Risk THẤP (0.5%)

| RR \ Win% | 30% | 40% | 50% | 60% | 70% |
|---|---|---|---|---|---|
| **1 : 1** | −400 | −200 | 0 | +200 | +400 |
| **1 : 1.5** | −250 | 0 | +250 | +500 | +750 |
| **1 : 2** | −100 | +200 | +500 | +800 | +1,100 |
| **1 : 2.5** | +50 | +400 | +750 | +1,100 | +1,450 |
| **1 : 3** | +200 | +600 | +1,000 | +1,400 | +1,800 |

> [!example] Hai ví dụ tham chiếu
> - **RR 1:2, thắng 50%** → R = 0.5 → @1%: **+$1,000/tháng (10%)** · @0.5%: +$500 (5%)
> - **RR 1:3, thắng 40%** → R = 0.6 → @1%: **+$1,200/tháng (12%)** · @0.5%: +$600 (6%)

## 4. Rủi ro & giới hạn FTMO 10K

| Chỉ tiêu | Giá trị | Ghi chú |
|---|---|---|
| Mục tiêu Phase 1 | $1,000 | 10% |
| Mục tiêu Phase 2 | $500 | 5% |
| Max daily loss | $500 | 5% trên số dư đầu ngày (balance gốc) |
| Max total loss | $1,000 | 10% trên balance gốc |
| Chuỗi thua LT chạm daily-limit @1% | **5 lệnh** | 5% / 1% |
| Chuỗi thua LT chạm daily-limit @0.5% | **10 lệnh** | 5% / 0.5% |

> [!warning] Mentor note — đọc kỹ hơn cả con số đẹp
> Đây là **kỳ vọng lý thuyết**, chưa trừ spread/commission/slippage và giả định phân phối thắng-thua đều. Điểm chí tử với FTMO không phải kỳ vọng dương, mà là **variance trong chuỗi thua**: ở **1% risk chỉ cần 5 lệnh thua liên tiếp trong 1 ngày là chạm daily loss limit** — với win rate 40–50%, chuỗi 5 thua xảy ra thường xuyên. Ở **0.5% bạn có đệm 10 lệnh**. Giai đoạn foundation nên khóa **0.5%**: mục tiêu là *sống qua variance*, ưu tiên **PROCESS hơn OUTCOME**. Chỉ RR ≥ 1:2 với win ≥ 40% mới có edge bền — hãy để **backtest của chính bạn** xác nhận cặp Win%/RR bạn thực sự đạt, đừng lấy ô đẹp nhất trong bảng làm kỳ vọng.

> [!summary] Nguồn thông số hợp đồng
> FTMO — [Points, pips and ticks](https://ftmo.com/en/blog/points-pips-and-ticks/) · [Symbols](https://ftmo.com/en/symbols/) · [Account specifications](https://ftmo.com/en/faq/what-are-the-account-specifications/)
