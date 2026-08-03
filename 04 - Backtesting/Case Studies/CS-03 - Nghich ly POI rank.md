---
type: case-study
id: CS-03
topic: poi-rank-paradox
lenh_lien_quan: 4
tags: [case-study, poi-rank, breaker, rejection-block, devils-advocate]
---

# CS-03 · Nghịch lý POI rank — Breaker/RB thua trong khi FVG/OB thắng

## Bối cảnh

Thang POI rank trong vault (theo `SKILL.md` § 8.1) xếp hạng độ "cao cấp" của các loại POI, với giả định ngầm rằng cấp cao hơn = ít false-positive hơn = chất lượng tốt hơn. Dữ liệu 22 lệnh cho kết quả ngược lại với giả định đó ở 2 loại POI cao cấp.

![[CS-03-poi-rank-paradox-summary.svg|760]]

## Số liệu

| POI type | Rank (8.1) | Win | Loss | Ghi chú |
|---|---|---|---|---|
| FVG (kể cả BPR gộp — xem O11) | 1 (cơ bản nhất) | 8 | 1 | Nhóm thắng nhiều nhất |
| Order Block | 2 | 6 | 2 | |
| Breaker Block | 3 | 0 | 1 | [[../2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short\|XAUUSD 19/5/2014]] — 100% Loss |
| Rejection Block | 3b (không có trên scale 8.1 chuẩn) | 0 | 1 | [[../2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short\|XAUUSD 14/5 sáng]] — 100% Loss |
| Unicorn / IFVG | 4 (cao cấp nhất) | 2 | 0 | |

## Hai cách đọc — cả hai đều chưa được chứng minh ở n hiện có

### Giả thuyết A: bản chất khái niệm

Breaker và Rejection Block vốn là khái niệm yêu cầu chuỗi sự kiện phức tạp hơn (OB gốc thất bại + liquidity bị lấy + structure bị phá bởi thất bại đó) — càng nhiều điều kiện, càng nhiều điểm có thể sai, nên tỷ lệ thất bại thực sự cao hơn FVG/OB đơn giản. Không có tài liệu doctrine nào trong vault khẳng định điều này trực tiếp — đây là suy luận hợp lý nhưng chưa kiểm chứng.

### Giả thuyết B: quy trình gán nhãn lỏng lẻo (được ủng hộ trực tiếp bởi 2 case cụ thể)

Cả 2 lệnh Loss dùng POI cao cấp đều có lỗi gán nhãn cụ thể, không chỉ "khái niệm khó":

- **XAUUSD 14/5 sáng** — invalidation ghi là "đóng qua RB high **1304.109**" nhưng SL thực tế đặt tại **1302.715** (RB low) — lệch **~1.4 điểm** so với chính invalidation mà note công bố. Đây là self-contradiction, không phải vấn đề của khái niệm Rejection Block.
- **XAUUSD 19/5/2014** — Breaker được gán bằng vị trí Fib 0.618 (1300.545–1301.645) trong khi OB 0.786 (~1304.5–1306) phía trên **chưa từng được test** — thiếu ít nhất 1/3 mắt xích chuỗi sự kiện bắt buộc cho nhãn Breaker theo canon.

Cả hai lỗi này đều xảy ra ở giai đoạn note "vừa học" khái niệm cao cấp (batch D, giữa quá trình backtest) — phù hợp với giả thuyết rằng vấn đề là **thao tác gán nhãn còn non**, không phải bản chất khái niệm Breaker/RB kém tin cậy hơn FVG/OB.

## Vì sao chưa thể phân xử ở n=1/nhóm

Với đúng 1 lệnh mỗi loại (Breaker: 1 Loss, Rejection Block: 1 Loss), không có cách nào tách được "khái niệm yếu" khỏi "gán nhãn sai lần này" bằng thống kê — cả hai giả thuyết giải thích dữ liệu quan sát được ngang nhau. Đây là tình huống evidence underdetermine theo nguyên tắc 6 của `ict-doctrine`: từ cùng bằng chứng, hai kết luận đối lập đều hợp lệ ngang.

## Cách phân xử (falsification test)

Thu thập ≥10 lệnh dùng nhãn Breaker/Rejection Block, chia theo có/không đủ 3 mắt xích chuỗi sự kiện bắt buộc (OB gốc bị nêu tên + liquidity bị lấy bị nêu tên + giá đóng nến xác nhận phá structure):

- Nếu nhóm **đủ 3 mắt xích** có WR cao hơn rõ rệt so với nhóm chỉ gán bằng vị trí Fib/hình dạng → **Giả thuyết B được xác nhận**, vấn đề là quy trình gán nhãn.
- Nếu WR tương đương giữa 2 nhóm dù đủ hay thiếu mắt xích → cần tìm biến khác giải thích, Giả thuyết A không bị loại nhưng cũng không được xác nhận thêm.

## Kết luận case study

Nhãn hiện tại của cả 2 case Loss là **FAIL theo doctrine** (thiếu chuỗi sự kiện bắt buộc / mâu thuẫn invalidation-SL), không phải bằng chứng cho "Breaker/RB kém tin cậy hơn về khái niệm". Kết luận cấp-khái-niệm ("POI cao cấp có tỷ lệ thắng thấp hơn") là **UNSUPPORTED** ở cả hai chiều — n=1/nhóm không đủ để khẳng định hoặc bác bỏ.

## Liên kết

- [[../00 - Tong hop/00 - Backtest Dashboard & Statistics|Dashboard]]
- [[../00 - Tong hop/02 - Master Lesson Learned|Master Lesson Learned]] — bài học #4, gate "chuỗi sự kiện Breaker/RB"
- Nguồn: [[../2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short]], [[../2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short]]
