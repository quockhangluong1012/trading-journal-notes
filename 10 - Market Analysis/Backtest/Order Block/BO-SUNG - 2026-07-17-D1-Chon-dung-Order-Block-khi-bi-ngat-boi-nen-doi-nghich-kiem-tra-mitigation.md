---
case_title: "2026-07-17-D1-Chon-dung-Order-Block-khi-bi-ngat-boi-nen-doi-nghich-kiem-tra-mitigation"
type: audit-addendum-standalone
audit_date: 2026-08-02
note_status_suggestion: "methodology"
evidence_tier_suggestion: 0
---

# 🔍 Bổ sung audit cho: 2026-07-17-D1-Chon-dung-Order-Block-khi-bi-ngat-boi-nen-doi-nghich-kiem-tra-mitigation

> [!warning] File gốc không có trong phiên làm việc này
> File note gốc "2026-07-17-D1-Chon-dung-Order-Block-khi-bi-ngat-boi-nen-doi-nghich-kiem-tra-mitigation" không nằm trong các file được tải lên phiên fork này (chỉ 10/15 file gốc có sẵn). Nội dung dưới đây được trích từ bản audit tổng — dán trực tiếp vào cuối file gốc trong vault Obsidian của cậu để hoàn tất việc bổ sung cho case này. Đồng thời sửa frontmatter `status:` thành `methodology` và thêm `evidence_tier: 0`.

> [!info] Nguồn
> Phần dưới đây được trích trực tiếp từ bản audit tổng [[2026-08-02 - Deep Audit 15 Case Studies - Doctrine v2]] (mục 4, case #9/15) và tách vào ngay file gốc để không phải mở file tổng mỗi lần tra cứu. Bảng tra cứu đầy đủ 15 case và các phần audit hệ thống/tranh biện/doctrine dùng chung vẫn nằm ở file tổng.

**Tóm tắt:** Không lệnh (`status: backtest` gắn sai — taxonomy §3.5). Vấn đề: vùng top có 2 nến bullish (1, 2) bị ngắt bởi 3 nến bearish ở giữa — nến nào là OB thật? Quy tắc: chỉ gộp nến cùng màu, liên tiếp, không bị ngắt bởi nến đối nghịch. 4 tiêu chí validate OB (vị trí, imbalance, xác nhận cấu trúc, sạch/chưa mitigate). Kết luận: nến 2 là POI chính, nến 1 là dự phòng.

**Điểm mạnh:** quy tắc "không gộp qua nến đối nghịch" là một điều chỉnh kỹ thuật rất cụ thể, dễ áp dụng, giải quyết một lỗi phổ biến (vẽ OB quá rộng bằng cách gộp nhiều nến cùng hướng bỏ qua nến ngắt ở giữa); phân biệt đúng khái niệm không chính thức "mitigated" (do note tự dùng) với khái niệm chính thức [[22-Mitigation-Block]] (một cấu trúc khác hẳn — failure swing không cần sweep) — tránh nhầm lẫn thuật ngữ.

**Lỗ hổng/điểm mù:** đây chính là note không xác định được symbol/timeframe của chart gốc — một trong ba note "vô danh" nhất trong tập 15 file (cùng nhóm với case 4.10 và 4.11). Quy tắc "chọn nến 2 thay vì nến 1" dựa trên tiêu chí "liền kề displacement hơn" — nhưng note không thảo luận trường hợp ngược: nếu nến 1 có FVG/imbalance rõ hơn nến 2 thì sao? Bốn tiêu chí được liệt kê nhưng không có thứ tự ưu tiên khi chúng mâu thuẫn nhau (ví dụ nến 1 thắng tiêu chí "imbalance", nến 2 thắng tiêu chí "vị trí liền kề" — chọn theo tiêu chí nào trước?).

> [!question] Tranh biện Devil's Advocate
> **Luận điểm ban đầu:** nến 2 (liền kề displacement, chưa bị mitigate) là POI chính; nến 1 là dự phòng.
>
> **Phản biện vòng 1:** "Liền kề displacement" có thực sự luôn là tiêu chí mạnh nhất? Trong nhiều tài liệu ICT, OB "mạnh nhất" thường được định nghĩa là nến cuối cùng TRƯỚC displacement mạnh nhất — nhưng "mạnh nhất" đôi khi lại là nến xa hơn (nến 1) nếu nó là nến có khối lượng/thân nến lớn hơn, biểu thị vùng tích lũy lệnh tổ chức nhiều hơn nến 2 (một nến nhỏ, sát displacement). Note chưa loại trừ khả năng này vì không đề cập tới kích thước thân nến như một tiêu chí.
>
> **Phản-phản biện:** 4 tiêu chí gốc (vị trí, imbalance, xác nhận cấu trúc, sạch) đã bao hàm phần lớn logic ICT chuẩn — kích thước thân nến là một biến phụ (ICT gốc không coi đây là tiêu chí bắt buộc, thường chỉ là "confluence" phụ).
>
> **Phản biện vòng 2:** Đồng ý kích thước không bắt buộc, nhưng vấn đề cốt lõi vẫn còn nguyên: khi 4 tiêu chí chính thức mâu thuẫn nhau giữa hai ứng viên OB, note không có cơ chế phân xử. Đây không phải vấn đề nhỏ — nó sẽ tái diễn ở MỌI case tương lai có ≥2 nến ứng viên, tức là một tình huống rất phổ biến trong thực chiến, không phải edge case hiếm gặp.
>
> **Phán quyết:** quy tắc "không gộp qua nến đối nghịch" đúng và nên giữ (Tier 0 vững, gần như tiên đề định nghĩa), nhưng thiếu thứ tự ưu tiên khi 4 tiêu chí mâu thuẫn — đây là khoảng trống thật, cần bổ sung.

**Hành động:** bổ sung thứ tự ưu tiên tường minh cho 4 tiêu chí OB: (1) xác nhận cấu trúc (MSS) > (2) sạch/chưa mitigate > (3) vị trí liền kề displacement > (4) imbalance/FVG đi kèm — thứ tự này là **đề xuất suy luận của tôi** dựa trên nguyên tắc ICT gốc ưu tiên bằng chứng cấu trúc trước bằng chứng hình thái, cần cậu tự xác nhận lại hoặc điều chỉnh khi có dữ liệu, không phải trích từ note gốc.

**Đề xuất field đo lường:** `ob_candidate_count` (số nến ứng viên OB trong vùng), `ob_selection_criteria_conflict` (có/không — các tiêu chí có mâu thuẫn khi chọn không), `ob_selected_rank` (nến được chọn xếp thứ mấy theo thứ tự ưu tiên).

### Rule liên quan (Doctrine v2)

### Rule 15 — Taxonomy `status` tách 4 giá trị, đồng bộ với `in_trade`
**Phát biểu:** `status: analysis | watchlist | backtest | live`; `status: backtest` hoặc `live` bắt buộc `in_trade: true` kèm entry/SL/TP/R-multiple; `in_trade: false` chỉ được đi với `analysis` hoặc `watchlist`.
**Tier hiện tại:** N/A (quy ước vận hành, không phải rule thị trường).
**Nguồn:** §3.5.


### Rule 9 — 4 tiêu chí chọn Order Block, có thứ tự ưu tiên
**Phát biểu:** khi ≥2 nến ứng viên OB tồn tại (ví dụ bị ngắt bởi nến đối nghịch), ưu tiên theo thứ tự: (1) xác nhận cấu trúc/MSS > (2) sạch/chưa mitigate > (3) vị trí liền kề displacement > (4) imbalance/FVG đi kèm. Không gộp 2 nến cùng màu bị ngắt bởi nến đối nghịch thành một OB.
**Tier hiện tại:** Tier 0 cho quy tắc không-gộp (gần tiên đề định nghĩa); Tier 0 cho thứ tự ưu tiên (đề xuất suy luận, chưa test).
**Nguồn:** case 4.9 (Chọn OB 07-17).
