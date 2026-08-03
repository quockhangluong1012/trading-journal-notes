---
type: case-study
id: CS-05
topic: outcome-bias-hindsight
lenh_lien_quan: 5 (batch A) + toan vault
tags: [case-study, hindsight, outcome-bias, methodology]
---

# CS-05 · Outcome bias & hindsight trong backtest replay — vì sao 5 note đầu đều UNPROVEN

## Bối cảnh

Backtest replay (đọc lại một setup đã biết outcome) mang một rủi ro cấu trúc mà live trading không có: người viết **luôn** biết TP/SL đã hit trước khi viết bất kỳ dòng phân tích nào. 5 note đầu tiên của vault (07-01 → 07-07, batch A) là nơi rủi ro này thể hiện rõ nhất, vì đây là giai đoạn quy trình ghi chú còn thiếu cấu trúc tách bạch.

![[CS-05-outcome-bias-hindsight-timeline.svg|760]]

## 5 note batch A và vấn đề cụ thể

| Note | Vấn đề hindsight cụ thể |
|---|---|
| [[../2026-07-01/01 - Win - EURUSD - 2010-10-19 - Long\|EURUSD 19/10/2010]] | Câu đánh giá "thắng vì chờ đầy đủ điều kiện" viết trong replay sau khi biết Hit TP; không có bằng chứng đây là suy luận trước outcome |
| [[../2026-07-06/01 - Win - EURUSD - 2005-04-12 - Short\|EURUSD 12/4/2005]] | Cùng pattern — không tách phần "dự đoán" khỏi phần "diễn giải sau" |
| [[../2026-07-06/02 - Win - EURUSD - 2005-04-13 - Short\|EURUSD 13/4/2005]] | Cùng pattern |
| [[../2026-07-07/02 - Win - EURUSD - 2005-04-24 - Long\|EURUSD 24/4/2005]] | Cùng pattern, cộng thêm lỗi arithmetic Unicorn overlap (1.8 pip lệch) không được phát hiện lúc viết |
| [[../2026-07-07/02 - Win - EURUSD - 2005-04-27 - Long\|EURUSD 27/4/2005]] | Grade A giữ nguyên dù note tự nhận lỗi chốt 50% sớm ("quên Liquidity Void phá rất nhanh") — nhận lỗi thực thi nhưng không hạ Grade tương ứng |

Cả 5/5 note đều **thiếu hoàn toàn** field `entry_type`, `confluence_score`, `first_error_step` — nghĩa là ngay cả công cụ cấu trúc để tách bạch quy trình cũng chưa tồn tại ở giai đoạn này (xem [[../00 - Tong hop/00 - Backtest Dashboard & Statistics|Dashboard]] mục 4, schema drift).

## Vì sao đây là HINDSIGHT, không chỉ là "thiếu dữ liệu"

Phân biệt quan trọng: một note thiếu field là **UNSUPPORTED** (có thể đúng, chỉ thiếu bằng chứng). Một note dùng thông tin sau outcome để biện minh cho một nhãn/quyết định là **HINDSIGHT** (status khác, nghiêm trọng hơn theo taxonomy của `ict-doctrine`). Ba lý do cả 5 note batch A rơi vào HINDSIGHT chứ không chỉ UNSUPPORTED:

1. Toàn bộ note được viết **sau** khi biết outcome (đây là bản chất của backtest replay, không phải lỗi riêng của 5 note này).
2. Câu đánh giá chất lượng quyết định (bias đúng, MSS đáng tin, entry hợp lý) dùng thì hiện tại/khẳng định ("thắng vì...") mà không có đánh dấu thời điểm nào được viết trước khi xem nến sau điểm quyết định.
3. Không có cơ chế nào trong note (timestamp, section riêng "dự đoán trước outcome") để tách phần suy luận thật khỏi phần diễn giải lùi.

## Quy mô rủi ro

5/17 lệnh Win (~**29.4%** số lệnh Win, ~**22.7%** toàn mẫu 22 lệnh) mang rủi ro này ở mức cao nhất. Đây không phải lỗi có thể sửa hồi tố — outcome đã biết, không thể tái tạo trạng thái "chưa biết" cho các note đã viết. Điều duy nhất có thể làm là (a) không dùng các note này làm bằng chứng cho "quy trình nhận diện MSS/bias là đáng tin", (b) ngăn tái diễn ở các note tương lai.

## Quy trình ghi chép "tại hard right edge" đề xuất

Để một backtest note trong tương lai **không** rơi vào cùng vấn đề, cần tách vật lý (không chỉ tách bằng ý định) hai giai đoạn:

1. **Giai đoạn dự đoán** — ghi bias/draw/sweep/displacement/POI/entry dựa CHỈ trên trạng thái chart tại đúng nến quyết định (right edge), không xem nến sau đó. Lưu snapshot/ảnh chụp tại đúng thời điểm này.
2. **Giai đoạn replay** — sau khi biết outcome, viết phần đánh giá riêng, đối chiếu với giai đoạn 1. Bất kỳ khác biệt giữa 2 giai đoạn phải được ghi rõ, không hòa trộn.
3. Field `prediction_timestamp` (hoặc tương đương) đánh dấu rõ ranh giới giữa 2 giai đoạn trong mỗi note.

So sánh: các note batch E (07-16→07-17) đã tiến bộ ở khía cạnh **tự sửa lỗi số** (vd tự phát hiện và sửa 2 lỗi 6 pip ở [[../2026-07-17/01 - Win - GBPUSD - 2014-06-25 - Long|GBPUSD 14/7/2014]]) — nhưng đây là cải thiện về độ chính xác arithmetic, KHÔNG phải giải quyết được vấn đề hindsight cấu trúc, vì các note này vẫn được viết hoàn toàn sau outcome, không có snapshot tại right edge.

## Kết luận case study

Trạng thái đúng cho cả 5 note batch A là **HINDSIGHT** ở các claim đánh giá chất lượng quyết định (không phải ở các fact thuần túy như giá entry/SL/TP, vốn có thể verify độc lập). Đây là giới hạn cấu trúc của phương pháp backtest replay khi không có quy trình ghi chép tách bạch — không phải lỗi cá nhân của người viết 5 note này, và không nên dùng để hạ giá trị của toàn bộ nỗ lực backtest, chỉ nên dùng để hạn định phạm vi những gì WR/expectancy của vault có thể chứng minh.

## Liên kết

- [[../00 - Tong hop/00 - Backtest Dashboard & Statistics|Dashboard]]
- [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]] — O9
- [[../00 - Tong hop/02 - Master Lesson Learned|Master Lesson Learned]] — bài học #1
- Nguồn: `analysis_summaries/batchA.md` Pattern #1, #2, #4
