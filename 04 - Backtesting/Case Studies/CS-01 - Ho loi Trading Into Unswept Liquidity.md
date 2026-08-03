---
type: case-study
id: CS-01
topic: ho-loi-unswept-liquidity
lenh_lien_quan: 4
tags: [case-study, unswept-liquidity, devils-advocate]
---

# CS-01 · Họ lỗi "Trading Into Unswept Liquidity" — 4 lệnh Loss

## Bối cảnh

Note [[../2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long|GBPUSD 17/7/2014]] (note tham chiếu chính của batch backtest) tự phát hiện, ở mục 9.3 của chính nó, rằng **4 lệnh Loss** trong vault có chung một đặc điểm mô tả: SL nằm trong đường đi tới một pool thanh khoản **chưa bị quét** tại thời điểm entry. Case study này trình bày lại 4 lệnh đó bằng số thật, sau đó áp đúng bài kiểm Devil's Advocate mà chính note gốc đã tự chạy (mục 10), mở rộng thêm hướng kiểm chứng bằng nhóm đối chứng Win.

![[CS-01-unswept-liquidity-4-loss-family.svg|760]]

## 4 lệnh trong họ lỗi

| Lệnh | first_error_step | Pool chưa bị quét | Entry | SL | Khoảng cách SL→pool |
|---|---|---|---|---|---|
| [[../2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long\|GBPUSD 17/7/2014]] | sweep | ERL Range Low 1.70592 | (FVG 1.70873–1.71103) | 1.70840 | SL nằm phía trong ERL, ERL chưa bị chạm |
| [[../2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short\|XAUUSD 19/5/2014]] | poi | OB 0.786 (~1304.5–1306) | 1301.167 | 1301.789 | OB phía trên chưa từng được test trước khi vào Breaker 0.618 |
| [[../2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short\|XAUUSD 14/5 sáng]] | poi | RB high 1304.109 (invalidation đúng) | 1301.482 | 1302.715 (RB low, lệch ~1.4 điểm so với invalidation ghi) | SL thực đặt trong vùng RB, không đúng cạnh invalidation đã công bố |
| [[../2026-07-10/02 - Loss- EURUSD - 2021-05-07- Short\|EURUSD 7/5/2021]] | draw | BSL/OB 1.21296–1.21227 | 1.20805 | 1.20931 | SL nằm trong đường đi tới OB đối lập phía trên |

Số liệu entry/SL trích trực tiếp từ frontmatter mỗi note; cột "Khoảng cách SL→pool" là mô tả định tính từ chính note gốc, chưa được đo bằng đơn vị pip/% range nhất quán (xem Fix ở mục Devil's Advocate).

## Phản biện narrative-fitting (đã có sẵn trong note gốc, tái hiện + mở rộng ở đây)

**Vấn đề cốt lõi**: định nghĩa "SL nằm trong đường đi tới một pool thanh khoản chưa bị quét" gần như là mô tả **mặc định** của bất kỳ lệnh thua nào đọc qua lens ICT. Thị trường luôn có một cấu trúc PD-array nào đó phía ngoài SL — hỏi "có pool nào chưa bị lấy trên đường đi của SL không" cho một lệnh đã biết kết quả thua gần như chắc chắn sẽ tìm được câu trả lời "có", bất kể lệnh đó thua vì lý do gì thật sự.

Ba lỗ hổng cụ thể:
1. **Mẫu số không công bố.** "4 lệnh" là toàn bộ 4/5 Loss quan sát được (không tính EURUSD 2/5/2005 — lỗi displacement khác gốc). Không rõ đây là 4/4 khả dĩ (100%) hay có case Loss khác không khớp mà chưa được xem xét.
2. **Chưa test chéo trên nhóm Win.** Nếu áp đúng tiêu chí này lên 17 lệnh Win, và tỷ lệ khớp tương đương, "họ lỗi" này không có sức phân loại — nó chỉ là một cách diễn đạt lại "đã thua" bằng từ vựng ICT.
3. **Đơn vị đo không nhất quán.** "Khoảng cách SL→pool" hiện được mô tả bằng lời ("nằm trong đường đi", "chưa test"), không bằng pip/% dealing range cụ thể — khiến 4 case không so sánh được với nhau về độ nghiêm trọng.

## Cách kiểm chứng bằng nhóm đối chứng Win

Đề xuất quy trình đo lường được (đã liệt kê là falsification test #2 ở [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]]):

1. Định nghĩa ngưỡng cụ thể trước khi chạy: "SL nằm trong đường đi tới pool chưa quét" = có một PD-array/level có tên (không phải bất kỳ giá nào) nằm giữa SL và hướng đối lập của trade, trong khoảng ≤ X% của dealing range D1.
2. Áp đúng ngưỡng đó lên toàn bộ 17 lệnh Win có đủ dữ liệu SL.
3. So sánh tỷ lệ khớp giữa nhóm Win và nhóm Loss.

**Kết quả kỳ vọng nếu C4 đúng**: tỷ lệ khớp ở nhóm Win phải thấp rõ rệt (đề xuất ngưỡng phân biệt: <15%) so với nhóm Loss (hiện tại 4/4 = 100% trong mẫu quan sát). **Kết quả nếu tỷ lệ tương đương** (ví dụ ≥40% Win cũng khớp): họ lỗi này bị bác — nó là mô tả lại outcome, không phải nguyên nhân.

## Kết luận case study

Pattern có thật ở mức **mô tả** (4/4 lệnh Loss quan sát được đều khớp đặc điểm này) nhưng **chưa được validate thành một họ lỗi thống kê**. Trạng thái đúng là **UNSUPPORTED**, không phải FAIL (định nghĩa không sai theo doctrine — "trading into unswept liquidity" là một rủi ro thật trong ICT model) và không phải PASS (thiếu bằng chứng đối chứng). Xem [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]] mục O2 cho ruling đầy đủ.

## Liên kết

- [[../00 - Tong hop/00 - Backtest Dashboard & Statistics|Dashboard]]
- [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]] — O2
- [[../00 - Tong hop/02 - Master Lesson Learned|Master Lesson Learned]] — bài học #4, gate "chuỗi sự kiện Breaker/RB"
- Nguồn: [[../2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] mục 9.3, 10
