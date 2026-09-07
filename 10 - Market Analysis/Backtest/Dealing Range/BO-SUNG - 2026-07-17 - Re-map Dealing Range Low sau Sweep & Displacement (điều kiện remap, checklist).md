---
case_title: "2026-07-17 - Re-map Dealing Range Low sau Sweep & Displacement (điều kiện remap, checklist)"
type: audit-addendum-standalone
audit_date: 2026-08-02
note_status_suggestion: ""
evidence_tier_suggestion: 0
---

# 🔍 Bổ sung audit cho: 2026-07-17 - Re-map Dealing Range Low sau Sweep & Displacement (điều kiện remap, checklist)

> [!warning] File gốc không có trong phiên làm việc này
> File note gốc "2026-07-17 - Re-map Dealing Range Low sau Sweep & Displacement (điều kiện remap, checklist)" không nằm trong các file được tải lên phiên fork này (chỉ 10/15 file gốc có sẵn). Nội dung dưới đây được trích từ bản audit tổng — dán trực tiếp vào cuối file gốc trong vault Obsidian của cậu để hoàn tất việc bổ sung cho case này. Đồng thời thêm `evidence_tier: 0` vào frontmatter.

> [!info] Nguồn
> Phần dưới đây được trích trực tiếp từ bản audit tổng [[2026-08-02 - Deep Audit 15 Case Studies - Doctrine v2]] (mục 4, case #10/15) và tách vào ngay file gốc để không phải mở file tổng mỗi lần tra cứu. Bảng tra cứu đầy đủ 15 case và các phần audit hệ thống/tranh biện/doctrine dùng chung vẫn nằm ở file tổng.

**Tóm tắt:** Note phương pháp thuần, không lệnh, chart không nhãn symbol/giá/khung. Xây khung 6 điều kiện remap DR Low (sweep thật, displacement+MSS xác nhận, FVG/CISD còn nguyên, VETO nếu có nến đóng cửa dưới red line, DR High phải resync, KZ là điều kiện hỗ trợ). Thêm khung "Partially vs Fully Consumed" (3 tiêu chí) và bảng rủi ro Over-remap vs Under-remap.

**Điểm mạnh:** đây là framework có cấu trúc logic chặt nhất trong 15 file — điều kiện 3.4 (VETO nếu có nến đóng cửa dưới red line) là một quy tắc phủ quyết rõ ràng, không mơ hồ; điều kiện 3.5 (phải resync DR High cùng lúc) chỉ ra một lỗi cực kỳ phổ biến và dễ mắc (remap Low nhưng quên High, làm lệch toàn bộ EQ) — đây là một phát hiện có giá trị thực tế cao bất kể tier bằng chứng.

**Lỗ hổng/điểm mù:** đã nêu ở Tóm tắt điều hành #6 — toàn bộ 6 điều kiện phức tạp này được xây trên nền dữ liệu mỏng nhất: không biết symbol, không biết giá, không biết khung thời gian thật. Đây là rủi ro over-engineering kinh điển: xây một hệ thống luật chi tiết, nhiều tầng, trên một quan sát không thể xác minh lại.

> [!question] Tranh biện Devil's Advocate (đa vòng — vì đây là rủi ro over-engineering rõ nhất trong tập)
> **Luận điểm ban đầu:** 6 điều kiện remap là một checklist chặt chẽ, đảm bảo chỉ remap khi có đủ bằng chứng cấu trúc.
>
> **Phản biện vòng 1:** Một framework có 6 điều kiện + 1 VETO + 1 sub-framework 3 tiêu chí (Partially vs Fully Consumed) + 1 bảng rủi ro riêng — tổng cộng tương đương 10 quyết định nhị phân/đa trị cần đánh giá cho MỖI lần cân nhắc remap. Với độ phức tạp này, câu hỏi hợp lý là: có bằng chứng nào cho thấy một checklist đơn giản hơn (ví dụ chỉ 2-3 điều kiện cốt lõi: sweep thật + MSS xác nhận + chưa có nến đóng cửa ngược) sẽ cho kết quả tệ hơn không? Nếu không có bằng chứng so sánh, sự phức tạp thêm vào (điều kiện 3.3, 3.5, 3.6, khung Partially/Fully Consumed) có thể là **phức tạp hóa không cần thiết (unnecessary complexity)** — dễ tạo cảm giác kiểm soát chặt chẽ hơn thực tế, một dạng "illusion of rigor".
>
> **Phản-phản biện:** Điều kiện 3.5 (resync DR High) không phải phức tạp hóa — nó sửa một lỗi thật, cụ thể, dễ hình dung (quên đồng bộ High khi remap Low). Đây không phải một điều kiện "cho vui" mà là một lỗi vận hành đã biết trước sẽ xảy ra nếu không có nó.
>
> **Phản biện vòng 2:** Chấp nhận 3.5 là cần thiết và cụ thể. Nhưng điều đó không cứu được toàn bộ framework — vấn đề là 3.5 hợp lý ở mức MICRO (một lỗi thao tác cụ thể) trong khi 3.6 (KZ điều kiện hỗ trợ) và cả khung Partially/Fully Consumed lại hợp lý ở mức MACRO (triết lý phân loại market state) — hai loại "điều kiện" này khác bản chất nhưng bị xếp chung một danh sách phẳng 6 mục, khiến người dùng checklist khó phân biệt "cái này là lỗi thao tác phải luôn kiểm tra" với "cái này là một phán đoán định tính cần kinh nghiệm". Gộp chúng vào cùng cấp bậc là chỗ thực sự có vấn đề, không phải bản thân từng điều kiện riêng lẻ.
>
> **Phán quyết:** Framework có giá trị thật (đặc biệt 3.4 VETO và 3.5 resync) nhưng đang trộn lẫn hai lớp khác bản chất (lỗi thao tác cụ thể vs phán đoán định tính) và được xây trên dữ liệu không thể xác minh. Đề xuất: tách 2 lớp — "Checklist thao tác bắt buộc" (3.1, 3.2, 3.4, 3.5 — có thể kiểm tra khách quan, gần như nhị phân) và "Khung phán đoán hỗ trợ" (3.3, 3.6, Partially/Fully Consumed — cần đánh giá định tính, không nhị phân).

**Hành động:** viết lại note gốc (hoặc bổ sung một mục mới) tách rõ 2 lớp trên; tối thiểu, lần tới áp dụng framework này, ghi rõ symbol/giá/khung thời gian thật để có thể xác minh lại — không lặp lại lỗi ẩn danh hóa dữ liệu.

**Đề xuất field đo lường:** `remap_condition_met_count` (số điều kiện trong 6 điều kiện thỏa mãn, 0-6), `remap_veto_triggered` (có/không — điều kiện 3.4 có bị vi phạm), `dr_high_resynced` (có/không).

![[remap-dealing-range-flow-20260802.svg]]


### Tranh biện chéo liên quan

### 5.5 — Remap bắt buộc (07-17, 07-19) vs nguy cơ Over-remap

Đã audit khá đầy đủ ở case 4.10 (Over/Under-remap risk table gốc trong chính note 07-17). Bổ sung một vòng tranh biện xuyên-note không có ở case 4.10: **note 07-19 (Nov'13 vs Feb'14) áp dụng khung 3 bước chọn Low — về bản chất đây CŨNG là một dạng quyết định remap (chọn lại đáy nào là "đáy quan trọng"), nhưng không hề tham chiếu 6 điều kiện remap của note 07-17, dù cả hai được viết cách nhau chỉ 2 ngày.**

> [!question] Tranh biện: đây có phải là 2 framework cạnh tranh cho cùng một quyết định?
> **Luận điểm:** khung 3 bước (07-19) trả lời câu hỏi "đáy NÀO là DR Low đúng, giữa nhiều đáy có sẵn trên chart" — một câu hỏi KHÔNG GIAN (spatial, chọn giữa các điểm đã tồn tại). Khung 6 điều kiện (07-17) trả lời câu hỏi "KHI NÀO nên cập nhật DR Low sang một mức MỚI sau một sự kiện sweep+displacement" — một câu hỏi THỜI GIAN (temporal, có nên đổi mức đang dùng hay không sau một sự kiện mới). Về lý thuyết, đây là hai câu hỏi bổ trợ nhau (không cạnh tranh): khung 3 bước dùng để CHỌN đúng đáy tại một thời điểm tĩnh; khung 6 điều kiện dùng để QUYẾT ĐỊNH có nên chuyển sang đáy khác sau khi có displacement mới.
>
> **Phản biện:** Nhưng trong thực hành, không có gì đảm bảo hai framework luôn cho cùng kết quả nếu áp dụng độc lập cho cùng một tình huống. Ví dụ: khung 3 bước có thể chọn Feb'14 làm DR Low (vì nó là "đáy chưa bị phá gần nhất theo chuỗi higher-low"), trong khi khung 6 điều kiện, áp cho cùng dữ liệu, có thể nói "chưa đủ điều kiện remap sang Feb'14 vì DR High chưa được resync" (điều kiện 3.5) — hai framework độc lập, không tham chiếu nhau, có nguy cơ đưa ra kết luận không nhất quán khi áp cho cùng một bộ dữ liệu.
>
> **Phán quyết:** hai framework KHÔNG cạnh tranh về mặt lý thuyết (giải quyết câu hỏi khác nhau) nhưng THIẾU một lớp tích hợp nối chúng lại — hiện tại chúng tồn tại như hai bài tập độc lập, và không note nào chỉ ra thứ tự áp dụng đúng (framework 3 bước trước để CHỌN ứng viên, sau đó framework 6 điều kiện để XÁC NHẬN có nên chính thức remap sang ứng viên đó hay chưa).

**Hành động (Doctrine v2 Rule 8, xem thêm §6):** hợp nhất 2 framework theo thứ tự: Bước 1 — dùng khung 3 bước (07-19) để xác định ứng viên DR Low hợp lý nhất trong số các đáy hiện có trên chart; Bước 2 — dùng khung 6 điều kiện (07-17) để xác nhận liệu có ĐỦ bằng chứng sweep+displacement MỚI để chính thức chuyển DR Low hiện hành sang ứng viên đó hay chưa. Không dùng riêng lẻ một trong hai.



### Rule liên quan (Doctrine v2)

### Rule 8 — Trình tự hợp nhất 2 framework Dealing Range (Chọn Low + Remap)
**Phát biểu:** Bước 1 — dùng khung 3 bước (là gốc MSS gần nhất? có higher-low chưa phá chắn giữa? là bệ phóng gần nhất chưa mitigate?) để chọn ứng viên DR Low. Bước 2 — dùng khung 6 điều kiện remap (sweep thật, displacement+MSS, FVG/CISD còn nguyên, VETO nếu có nến đóng cửa ngược, resync DR High, KZ hỗ trợ) để xác nhận có nên chính thức chuyển sang ứng viên đó.
**Tier hiện tại:** Tier 0 (cả 2 framework thành phần đều Tier 0, note nguồn dùng dữ liệu chưa verify/vô danh).
**Điều kiện nâng tier:** verify lại toàn bộ giá ước lượng trong case Nov'13/Feb'14; áp dụng trình tự hợp nhất lên ≥10 tình huống remap thật, log kết quả đúng/sai.
**Nguồn:** case 4.10 (Re-map 07-17), case 4.11 (Nov'13 vs Feb'14 07-19), §5.5.
