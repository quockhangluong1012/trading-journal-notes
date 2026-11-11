---
type: reference
title: The5ers 10K - Lot Size & Profit Calculator
account: The5ers 10K (High Stakes)
tags: [risk-management, position-sizing, the5ers, expectancy]
created: 2026-07-15
updated: 2026-07-15
---

# The5ers 10K — Bảng Lot Size & Profit Calculator

> [!info] Về note này
> Phiên bản Markdown (tĩnh) cho tài khoản **The5ers 10K — High Stakes (2-step)**. Các con số dưới tính sẵn cho **balance $10,000**, risk **0.5% ($50/lệnh)** và **1% ($100/lệnh)**. Phần **Lot Size (mục 2)** và **Expectancy (mục 3)** là toán thuần, **giống hệt** file `[[Lot size 10K]]` (FTMO) — vì lot size chỉ phụ thuộc risk$ và SL, không phụ thuộc quỹ. Phần **khác nhau nằm ở mục 4 (luật rủi ro)**: The5ers tính daily loss theo **equity/balance đầu ngày (số lớn hơn)** và bắt buộc **tối thiểu 3 ngày lãi**, khác hẳn FTMO.

## 1. Tham số & giả định

| Tham số | Giá trị |
|---|---|
| Số dư tài khoản | $10,000 |
| Risk thấp | 0.5% = **$50 / lệnh** |
| Risk cao | 1.0% = **$100 / lệnh** |
| Số lệnh / tháng | 20 (1 lệnh/ngày, ~4 tuần) |
| Cách tính lãi | Fixed risk (risk $ cố định trên balance gốc) |

**Giá trị 1.00 lot** (dùng để tính lot size — đối chiếu MT5 → Market Watch → chuột phải → *Specification* cho đúng server The5ers của bạn):

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

Công thức: **Kỳ vọng/lệnh (R) = Win% × RR − (1 − Win%)** · **Profit/tháng = R × 20 lệnh × Risk$**

### A) Kỳ vọng (R / lệnh)

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

> [!example] Đối chiếu với target The5ers (Phase 1 = 8% = $800)
> - **RR 1:2, thắng 50%** → R = 0.5 → @1%: **+$1,000/tháng (10%)** → đủ vượt Phase 1 · @0.5%: +$500 (5%) → ~1.6 tháng mới đạt.
> - **RR 1:3, thắng 40%** → R = 0.6 → @1%: **+$1,200/tháng (12%)** · @0.5%: +$600 (6%).
> Lưu ý: The5ers **không có giới hạn thời gian** ở High Stakes, nên chạy 0.5% chậm hơn nhưng an toàn hơn — không bị ép "cày" cho kịp deadline như một số quỹ khác.

## 4. Rủi ro & giới hạn The5ers 10K (High Stakes, 2-step)

| Chỉ tiêu | Giá trị | Ghi chú |
|---|---|---|
| Mục tiêu Phase 1 | $800 | **8%** trên balance gốc |
| Mục tiêu Phase 2 | $500 | **5%** trên balance gốc |
| **Số ngày lãi tối thiểu** | **3 ngày** | Mỗi phase; 1 ngày lãi = tổng lệnh đóng trong ngày **≥ 0.5% = ≥ $50** |
| Max daily loss | $500 (đầu chặng) | **5% của số LỚN HƠN giữa equity đầu ngày và balance đầu ngày**, tính theo giờ MT5 server (GMT+2/+3) |
| Max total loss | $1,000 | **10% trên balance gốc** — mức tuyệt đối, cố định |
| Hết hạn do không hoạt động | 30 ngày | Không giao dịch >30 ngày liên tục → account expire |
| Chuỗi thua LT chạm daily-limit @1% | **5 lệnh** | 5% / 1% |
| Chuỗi thua LT chạm daily-limit @0.5% | **10 lệnh** | 5% / 0.5% |

> [!warning] Mentor note — The5ers "chơi khác luật" FTMO, đừng lẫn
> Ba điểm chí tử khiến một thói quen hợp FTMO có thể **rớt** The5ers:
> 1. **Daily loss neo vào "số lớn hơn của equity/balance đầu ngày", không phải balance gốc.** Khi tài khoản đã lãi (balance/equity đầu ngày cao hơn), hạn mức lỗ ngày cũng **nới lên** — đây là ưu điểm. Nhưng ngược lại, nếu bạn để **floating profit lớn qua đêm**, equity đầu ngày cao → sáng ra một cú retrace mạnh có thể ăn vào buffer nhanh hơn bạn tưởng. Đừng ôm lệnh floating lớn qua reset ngày.
> 2. **Bắt buộc ≥ 3 ngày lãi, mỗi ngày ≥ $50 (0.5%).** Đây KHÔNG phải "min trading days" như FTMO. Nghĩa là bạn không thể pass bằng 1 lệnh to ăn cả target — phải có **ít nhất 3 phiên khác nhau chốt lời thực ≥ $50**. Điều này thưởng cho **tính nhất quán (consistency)**, đúng triết lý PROCESS > OUTCOME. Ở 0.5% risk, RR 1:2 thì 1 lệnh thắng = +$100 ≥ ngưỡng $50 → 1 lệnh thắng/ngày là đủ tính "ngày lãi".
> 3. **Variance trong chuỗi thua vẫn là kẻ giết người.** Ở **1% risk chỉ cần 5 lệnh thua liên tiếp trong 1 ngày là chạm daily loss** — với win rate 40–50% chuỗi 5 thua xảy ra thường xuyên. Ở **0.5% bạn có đệm 10 lệnh**. Giai đoạn foundation nên **khóa 0.5%**: mục tiêu là *sống qua variance* và tích đủ 3 ngày lãi, không phải về đích nhanh.
>
> Đây là **kỳ vọng lý thuyết**, chưa trừ spread/commission/slippage và giả định phân phối thắng-thua đều. Chỉ RR ≥ 1:2 với win ≥ 40% mới có edge bền — hãy để **backtest của chính bạn** xác nhận cặp Win%/RR bạn thực sự đạt, đừng lấy ô đẹp nhất trong bảng làm kỳ vọng.

> [!summary] Nguồn thông số hợp đồng
> The5ers — [General rules – High Stakes](https://help.the5ers.com/what-are-the-general-rules-for-the-high-stakes-program/) · [Drawdown rule – High Stakes](https://help.the5ers.com/what-is-the-drawdown-rule-for-high-stakes/) · [Max & daily loss – High Stakes](https://help.the5ers.com/what-is-the-maximum-loss-and-the-maximum-daily-loss-in-the-high-stakes-program/) · [High Stakes program](https://the5ers.com/high-stakes/)

---

> [!tip] Liên kết
> So sánh song song với track FTMO: `[[Lot size 10K]]`. Hai quỹ chạy **song song, không tuần tự** — giữ hai bộ luật tách biệt trong đầu.
