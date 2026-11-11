---
type: case-study
id: CS-02
topic: edge-vs-ce-entry
lenh_lien_quan: 2
tags: [case-study, entry-method, hindsight, devils-advocate]
---

# CS-02 · Edge entry vs CE entry — "thắng dù sai"

## Bối cảnh

2 lệnh Win trong vault có `first_error_step: entry` — nghĩa là entry được thực hiện tại Edge (biên) hoặc điểm giữa Edge/CE của POI, không phải Consequent Encroachment (CE, điểm giữa chuẩn). Cả hai lệnh vẫn Hit TP. Case study này đo chi phí/lợi ích bằng số thật và đối chiếu với chuẩn CE lý tưởng.

![[CS-02-edge-vs-ce-cost-benefit.svg|760]]

## 2 lệnh

### [[../2026-07-11/01 - Win - EURUSD - 2013-11-21- Long|EURUSD 21/11/2013 (Long)]]

- POI: FVG/BPR, `entry_type` không rõ ràng ghi Edge.
- Entry: **1.34239**.
- BPR bounds trong note gốc: `1.34237 - 1.34-96` — **lỗi đánh máy** (thiếu số ở cạnh trên), khiến `fvg_high`/`fvg_low`/`ce_price` không thể tính được và bị để trống trong frontmatter.
- R đạt được: **3.18**, Grade **A** (giữ nguyên dù `first_error_step: entry`).
- **Không thể tính chi phí cơ hội** cho case này — chính lỗi đánh máy trong note nguồn là rào cản, không phải thiếu ý chí phân tích.

### [[../2026-07-12/01 - Win - GBPUSD- 2024-12-04- Long|GBPUSD 4/12/2024 (Long)]]

- POI: Order Block, `entry_type`: Edge/Between.
- FVG: high **1.26642**, low **1.26515** → CE = **1.265785**.
- Entry thực: **1.26615** — fill depth chỉ **21%** vào FVG (rất gần cạnh trên, xa CE).
- R đạt được: **3.4**.
- `rr_if_ce` (RR giả định nếu vào đúng CE): **5.31**.
- **Chi phí cơ hội đo được: ~1.9R** (5.31 − 3.4) — phần R "đáng lẽ được nhận thêm" nếu chờ giá về đúng CE và CE thực sự bị chạm.
- Grade: note **tự hạ A→B** cho loại lỗi này — đây là chuẩn nghiêm hơn được đề xuất làm baseline toàn vault (xem [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]] O8).

## Vì sao "thắng" không chứng minh Edge-entry là kỹ thuật đúng [HINDSIGHT]

Cả hai lệnh chỉ Win vì retrace **không đủ sâu** để thực sự kiểm định giả thuyết Edge vs CE — nếu giá đã tiếp tục retrace xuống chạm đúng CE trước khi đảo chiều, kết quả hai lệnh này (thắng/thua) không thay đổi gì so với việc chờ CE. Nói cách khác, outcome hiện tại **không phân biệt được** hai giả thuyết:

- **H1**: Edge-entry là một kỹ thuật hợp lệ, tận dụng được các lần giá không hồi đủ sâu.
- **H2**: Edge-entry là entry sớm không có cơ sở, và 2 lệnh này thắng nhờ may (giá không hồi đủ sâu để phạt sai lầm).

Biết trước rằng "giá chỉ hồi tới đó rồi đảo chiều" là thông tin chỉ có **sau** khi outcome xảy ra — dùng nó để biện minh cho quyết định Edge-entry tại thời điểm entry là hindsight kinh điển.

## Chi phí/lợi ích — bảng tổng hợp

| | R thực nhận (Edge) | R giả định nếu CE (rr_if_ce) | Chênh lệch |
|---|---|---|---|
| GBPUSD 4/12/2024 | 3.4 | 5.31 | **~1.9R cơ hội chưa nhận** (nếu H2 đúng lần này lại là H1) |
| EURUSD 21/11/2013 | 3.18 | không tính được (lỗi đánh máy BPR bounds) | N/A |

Với chỉ 2 mẫu và không có mẫu nào Edge-entry **thua**, không thể tính được cả 2 nửa của phương trình chi phí/lợi ích (chi phí chỉ tính được khi có mẫu Edge-entry thua vì entry sớm bị quét SL trước khi giá đi đúng hướng).

## Cách đo cho tương lai (theo Master Lesson Learned bài học #3, #5)

1. Mọi lệnh dùng Edge-entry phải ghi `rr_if_ce` tại thời điểm vào lệnh (không phải tính lại sau).
2. Ghi `fill_depth` (% vào FVG) làm biến liên tục, không chỉ nhãn Edge/CE nhị phân.
3. Cần ≥20 mẫu Edge-entry, bao gồm cả các lần entry sớm bị quét SL, để đo tỷ lệ sống sót thật của Edge so với CE — xem lộ trình validate ở [[../00 - Tong hop/02 - Master Lesson Learned|Master Lesson Learned]] mục (e).

## Kết luận case study

Cả 2 lệnh là **PASS về mặt R thực nhận**, nhưng **UNSUPPORTED** như bằng chứng cho "Edge-entry là kỹ thuật đáng tin cậy" — mẫu quá nhỏ (n=2, không mẫu thua) và chính outcome bị nghi ngờ là may, không phải kỹ năng, theo tiêu chuẩn hindsight ở hard right edge.

## Liên kết

- [[../00 - Tong hop/00 - Backtest Dashboard & Statistics|Dashboard]]
- [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]] — O6, O8
- [[../00 - Tong hop/02 - Master Lesson Learned|Master Lesson Learned]] — bài học #3
- Nguồn: [[../2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]], [[../2026-07-12/01 - Win - GBPUSD- 2024-12-04- Long]]
