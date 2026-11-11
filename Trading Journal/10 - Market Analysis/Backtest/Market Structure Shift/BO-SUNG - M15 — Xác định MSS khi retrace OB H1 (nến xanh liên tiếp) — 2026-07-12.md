---
case_title: "M15 — Xác định MSS khi retrace OB H1 (nến xanh liên tiếp) — 2026-07-12"
type: audit-addendum-standalone
audit_date: 2026-08-02
note_status_suggestion: "methodology"
evidence_tier_suggestion: 0
---

# 🔍 Bổ sung audit cho: M15 — Xác định MSS khi retrace OB H1 (nến xanh liên tiếp) — 2026-07-12

> [!warning] File gốc không có trong phiên làm việc này
> File note gốc "M15 — Xác định MSS khi retrace OB H1 (nến xanh liên tiếp) — 2026-07-12" không nằm trong các file được tải lên phiên fork này (chỉ 10/15 file gốc có sẵn). Nội dung dưới đây được trích từ bản audit tổng — dán trực tiếp vào cuối file gốc trong vault Obsidian của cậu để hoàn tất việc bổ sung cho case này. Đồng thời sửa frontmatter `status:` thành `methodology` và thêm `evidence_tier: 0`.

> [!info] Nguồn
> Phần dưới đây được trích trực tiếp từ bản audit tổng [[2026-08-02 - Deep Audit 15 Case Studies - Doctrine v2]] (mục 4, case #5/15) và tách vào ngay file gốc để không phải mở file tổng mỗi lần tra cứu. Bảng tra cứu đầy đủ 15 case và các phần audit hệ thống/tranh biện/doctrine dùng chung vẫn nằm ở file tổng.

**Tóm tắt:** Không lệnh. Vấn đề: chuỗi nến xanh liên tiếp không có swing low rõ để xác nhận MSS. Giải pháp: định nghĩa STL bằng fractal 3-nến, quy trình 3 bước (STL hình thành → reject từ OB → đóng thân nến phá STL = MSS), và "drop xuống M5/M1" khi M15 không đủ chi tiết.

**Điểm mạnh:** quy trình 3 bước rất rõ ràng, đo được, có thể dùng làm checklist trực tiếp (đã đưa vào Checklist §7); phân biệt đúng "MSS chưa tồn tại" với "tôi tìm không ra" — một phân biệt tinh tế và quan trọng, tránh việc cố "thấy" MSS ở nơi chưa có.

**Lỗ hổng/điểm mù:** hai War Story ở cuối (composite/illustrative) dùng để minh họa "trend day" và "STL M1 giả" — nhưng bản thân quy trình 3 bước chính KHÔNG có bước nào kiểm tra "đây có phải trend day không" TRƯỚC khi bắt đầu tìm MSS — kiểm tra đó chỉ xuất hiện trong phần bài học phụ (War Story), chưa được tích hợp vào quy trình chính 3 bước.

> [!question] Tranh biện Devil's Advocate
> **Luận điểm ban đầu:** quy trình 3 bước (STL → reject → close phá STL) là đủ để xác nhận MSS ở bất kỳ đâu có OB H1 đang được retrace.
>
> **Phản biện vòng 1:** Chính War Story W1 trong note này mô tả trường hợp quy trình 3 bước này liên tục cho tín hiệu SAI trong ngày trend mạnh (LTF liên tục tạo STL mới rồi bị xuyên qua ngay, không bao giờ có MSS thật) — nếu quy trình 3 bước không tự nó phát hiện được "tôi đang ở trend day", nó sẽ liên tục tạo tín hiệu giả dương (false positive) đúng vào lúc thị trường nguy hiểm nhất để đánh ngược trend.
>
> **Phản-phản biện:** Field `session_type` được đề xuất chính là cơ chế phòng vệ cho vấn đề này — không phải quy trình 3 bước tự thân đủ, mà quy trình 3 bước CỘNG với field `session_type` đã lấp đủ khoảng trống.
>
> **Phản biện vòng 2:** Nhưng field đó chỉ tồn tại trong phần War Story (illustrative, theo quy tắc §3.4 không được tính là bằng chứng), chưa được đưa vào quy trình chính thức 3 bước ở mục 3-4 của note — nghĩa là về mặt structure, hai phần này (quy trình chính + field phòng vệ) đang tồn tại tách rời, không đảm bảo người áp dụng checklist sẽ luôn nhớ chấm `session_type` trước khi tin MSS.
>
> **Phán quyết:** quy trình 3 bước đúng nhưng chưa đầy đủ khi đứng một mình — cần hợp nhất field `session_type` làm **bước 0** bắt buộc trước bước 1, không để nó là một ghi chú phụ dễ bị bỏ qua.

**Hành động:** nâng field `session_type` thành Bước 0 bắt buộc trong Checklist §7, trước khi bắt đầu tìm STL.

**Đề xuất field đo lường:** `session_type` (AMD bình thường / trend day nghi ngờ / không rõ) + `stl_has_reaction_context` (có/không) — cả hai đã đề xuất trong note gốc, chính thức hóa vào schema chung.

### Rule liên quan (Doctrine v2)

### Rule 15 — Taxonomy `status` tách 4 giá trị, đồng bộ với `in_trade`
**Phát biểu:** `status: analysis | watchlist | backtest | live`; `status: backtest` hoặc `live` bắt buộc `in_trade: true` kèm entry/SL/TP/R-multiple; `in_trade: false` chỉ được đi với `analysis` hoặc `watchlist`.
**Tier hiện tại:** N/A (quy ước vận hành, không phải rule thị trường).
**Nguồn:** §3.5.


### Rule 13 — War Story illustrative không được dùng làm bằng chứng nâng tier
**Phát biểu:** mọi War Story gắn `war_story_type: illustrative` bị cấm dùng để đổi hoặc nâng tier bất kỳ rule nào trong Doctrine v2; chỉ War Story `real` (có ngày/giá thật, đã xảy ra với chính người viết) mới tính là dữ liệu, và ngay cả vậy vẫn chỉ n=1.
**Tier hiện tại:** Tier 0 (meta-rule quản trị bằng chứng).
**Nguồn:** §3.4.


### Rule 10 — MSS 3 bước + session_type là Bước 0 bắt buộc
**Phát biểu:** Bước 0 (mới, bắt buộc trước khi bắt đầu) — xác định `session_type` (AMD bình thường / trend day nghi ngờ / không rõ); nếu trend day nghi ngờ, không săn MSS đảo chiều. Bước 1 — chờ pullback tạo STL (fractal 3-nến). Bước 2 — xác nhận lower-high/rejection từ OB. Bước 3 — displacement đóng thân nến qua STL = MSS xác nhận (wick không tính).
**Tier hiện tại:** Tier 0 (framework hợp lý, War Story minh họa, chưa test số liệu thật).
**Nguồn:** case 4.5 (MSS no-swing-low 07-12).
