---
case_title: "2026-07-13 M15-M5-M1 - Internal Sweep tại CE của H1 FVG (Fractal Liquidity & cơ chế thanh khoản)"
type: audit-addendum-standalone
audit_date: 2026-08-02
note_status_suggestion: ""
evidence_tier_suggestion: 0
---

# 🔍 Bổ sung audit cho: 2026-07-13 M15-M5-M1 - Internal Sweep tại CE của H1 FVG (Fractal Liquidity & cơ chế thanh khoản)

> [!warning] File gốc không có trong phiên làm việc này
> File note gốc "2026-07-13 M15-M5-M1 - Internal Sweep tại CE của H1 FVG (Fractal Liquidity & cơ chế thanh khoản)" không nằm trong các file được tải lên phiên fork này (chỉ 10/15 file gốc có sẵn). Nội dung dưới đây được trích từ bản audit tổng — dán trực tiếp vào cuối file gốc trong vault Obsidian của cậu để hoàn tất việc bổ sung cho case này. Đồng thời thêm `evidence_tier: 0` vào frontmatter.

> [!info] Nguồn
> Phần dưới đây được trích trực tiếp từ bản audit tổng [[2026-08-02 - Deep Audit 15 Case Studies - Doctrine v2]] (mục 4, case #7/15) và tách vào ngay file gốc để không phải mở file tổng mỗi lần tra cứu. Bảng tra cứu đầy đủ 15 case và các phần audit hệ thống/tranh biện/doctrine dùng chung vẫn nằm ở file tổng.

**Tóm tắt:** Note phương pháp thuần (không lệnh). Giải quyết nghịch lý "sweep không có SSL rõ tại CE" bằng khái niệm Fractal Liquidity — zoom xuống M1/M5 lộ ra các equal-low/swing-low nội bộ nằm trong cây wick dài trên M15. Đưa ra sweep checklist 5 điểm và phân biệt FVG (nơi phản ứng) khỏi Liquidity (nhiên liệu di chuyển).

**Điểm mạnh:** phân biệt FVG ≠ Liquidity là một làm rõ khái niệm quan trọng, tránh lẫn lộn phổ biến ở trader mới; mục 5 "cơ chế tích tụ thanh khoản" đưa ra một tuyên bố táo bạo và có thể kiểm định: thanh khoản KHÔNG tích lũy dần theo thời gian mà đặt gần như tức thì khi một mức giá trở thành điểm tham chiếu nhìn thấy được (Schelling point).

**Lỗ hổng/điểm mù:** tuyên bố "thanh khoản đặt tức thì" (mục 5) là một khẳng định về **cơ chế vi mô của order flow** (khi nào lệnh dừng lỗ/chờ thực sự được đặt vào sổ lệnh) — đây là loại tuyên bố gần như không thể verify được bằng phân tích chart thông thường (chart không hiển thị sổ lệnh thật), nên về bản chất đây là suy luận triết học về hành vi thị trường, không phải quan sát trực tiếp. Không note nào khác trong 15 file minh bạch phản bác hoặc ủng hộ quan điểm "tích lũy dần theo thời gian" — tôi không tìm thấy bằng chứng về một mâu thuẫn trực tiếp với note khác trong tập 15 file này (cần nói rõ: đây là **suy luận của tôi**, không phải trích dẫn — nếu một mâu thuẫn như vậy tồn tại, nó nằm ở note khác ngoài phạm vi 15 file được audit).

> [!question] Tranh biện Devil's Advocate
> **Luận điểm ban đầu:** liquidity không tích lũy dần mà đặt tức thì ngay khi một mức trở thành Schelling point nhìn thấy được (ví dụ ngay khi nến in ra một swing low rõ ràng).
>
> **Phản biện vòng 1:** Nếu đúng vậy, tại sao ICT gốc và hầu hết tài liệu SMC vẫn thường mô tả các bể liquidity "lớn dần" theo thời gian một range tồn tại (nhiều lần test không phá = nhiều stop tích lũy thêm ở đó)? Có vẻ hai mô hình (tức thì vs tích lũy dần) không nhất thiết loại trừ nhau — có thể ĐÚNG cả hai cùng lúc: một lượng stop đặt tức thì tại thời điểm swing low hình thành (từ các trader đã tham gia đúng lúc đó), CỘNG THÊM một lượng tích lũy dần khi swing low đó tồn tại lâu và ngày càng nhiều trader mới nhìn thấy nó trên chart và đặt SL/lệnh chờ mới tại đó.
>
> **Phản-phản biện:** Note không phủ nhận khả năng "thêm dần" này — mục 5 chỉ nói phần tích lũy BAN ĐẦU (khối lượng khởi tạo) là tức thì, không phải "phải chờ nhiều ngày mới có đủ thanh khoản để sweep". Nói cách khác, đây có thể không phải một mâu thuẫn thật mà là hai lớp cùng tồn tại: base tức thì + bồi thêm dần theo thời gian nhìn thấy.
>
> **Phán quyết:** đây là một tuyên bố Tier 0 hợp lý, không có mâu thuẫn xác nhận được với note khác trong tập 15 file, nhưng KHÔNG kiểm định được bằng công cụ chart thông thường — nên giá trị thực dụng của nó nằm ở việc thay đổi *cách đọc chart* (không chờ "đủ thời gian" mới coi một mức là bể thanh khoản hợp lệ) hơn là một quy tắc có thể đo trực tiếp bằng entry/exit.

**Hành động:** giữ nguyên như một nguyên tắc đọc chart (Tier 0, không cần backtest riêng vì không sinh ra một biến quyết định entry/exit cụ thể) — không đưa vào Doctrine v2 như một rule số, chỉ giữ như ghi chú diễn giải trong Rule liên quan tới Liquidity Sweep.

**Đề xuất field đo lường:** `sweep_tier_confirmed_by_htf_poi`, `consecutive_internal_sweeps_before_entry`, `pre_session_poi_map`, `decision_made_from_preplan` — 4 field từ note gốc, vào schema chung.


### Tranh biện chéo liên quan

### 5.3 — "Sweep phải cùng khung MSS" (note EQH 07-12) vs "Fractal Liquidity: M15 wick = M1 sweep" (note 07-13)

**Bề mặt có vẻ mâu thuẫn:** note EQH 07-12 nhấn mạnh sweep cho trigger PHẢI cùng khung với MSS/FVG (không lấy bể HTF làm trigger cho MSS LTF). Note 07-13 (Fractal Liquidity) lại nói một wick M15 dài, nhìn không có SSL rõ, thực chất chứa nhiều sweep nội bộ M1/M5 bên trong nó — ngụ ý rằng "khung" nơi sweep xảy ra có thể MƠ HỒ/lồng nhau (một sự kiện M15 = nhiều sự kiện M1).

> [!question] Tranh biện đa vòng
> **Vòng 1:** Nếu sweep M1 "ẩn" bên trong một wick M15, và MSS được xác nhận trên M5, vậy sweep đó có được coi là "cùng khung" với MSS M5 hay không? Về mặt hình thức nhìn từ M15, sự kiện chỉ là "một cái râu nến" (theo đúng câu note 07-13 dùng) — không có sweep M15 riêng biệt để đối chiếu "cùng khung" với MSS M5.
>
> **Vòng 2 — Giải quyết bằng định nghĩa "khung":** Hai note thực ra không mâu thuẫn nếu định nghĩa "khung" đúng là KHUNG ENTRY (nơi MSS được xác nhận), không phải khung mà ta ĐANG NHÌN chart. Note EQH 07-12 nói: sweep phải cùng khung với khung MSS/FVG xác nhận (ví dụ nếu MSS xác nhận trên M5, sweep dùng làm trigger cũng phải là sweep cấp M5, dù ta có thể đang xem chart M15 để có bối cảnh). Note 07-13 chỉ ra: đôi khi để THẤY sweep cấp M5 đó, ta phải zoom vào M1/M5 vì M15 không đủ độ phân giải để hiển thị nó rõ — đây là vấn đề CÔNG CỤ QUAN SÁT (resolution), không phải vấn đề ĐỊNH NGHĨA KHUNG (scale). Hai note đang nói về hai trục khác nhau: EQH 07-12 nói về "sweep phải cùng CẤP ĐỘ (scale) với MSS", 07-13 nói về "để thấy sweep đúng cấp độ, có khi phải đổi khung NHÌN (viewing timeframe) xuống thấp hơn".
>
> **Vòng 3 — Phản biện lại sự "giải quyết" này:** Nhưng nếu phải liên tục đổi khung nhìn xuống M1 để "tìm ra" sweep ẩn bên trong mọi wick M15 nghi ngờ, quy tắc "sweep cùng khung MSS" trở nên gần như luôn luôn ĐÚNG BẰNG ĐỊNH NGHĨA (tautological) — vì bất kỳ MSS nào cũng có thể "tìm thấy" một sweep tương ứng nếu ta đủ kiên nhẫn zoom sâu đủ mức. Điều này làm giảm giá trị phân loại/loại trừ (falsifiability) của quy tắc: nếu không có trường hợp nào mà "sweep cùng khung" có thể bị coi là KHÔNG thỏa mãn (vì luôn tìm ra ở khung đủ nhỏ), quy tắc mất khả năng giúp loại bỏ setup tồi.
>
> **Vòng 4 — Phản-phản biện, khôi phục falsifiability:** Đây là lo ngại hợp lý nhưng note 07-13 tự đưa ra giới hạn: sweep checklist 5 điểm (bể xác định trước, giá thực breach, reject nhanh, tại POI, có displacement/MSS xác nhận SAU) — không phải bất kỳ nhiễu nào trên M1 cũng được tính là "sweep hợp lệ", chỉ những gì thỏa 5 điều kiện đó. Vậy quy tắc vẫn falsifiable: nếu zoom vào M1 mà KHÔNG tìm thấy cấu trúc thỏa 5 điều kiện (chỉ là nhiễu ngẫu nhiên không có pool xác định trước), sweep "cùng khung" thực sự không tồn tại, và MSS đó phải bị coi là thiếu trigger hợp lệ.
>
> **Phán quyết:** Hai note KHÔNG mâu thuẫn về bản chất — chúng nói về hai trục khác nhau (scale của sự kiện vs resolution của công cụ quan sát) — nhưng nếu áp dụng cẩu thả (luôn "tìm ra" sweep bất kể zoom bao sâu), quy tắc có nguy cơ trở thành tautological. Điều kiện phòng vệ: sweep checklist 5 điểm PHẢI được áp dụng nghiêm ngặt ở khung zoom-in, không chỉ "thấy có wick, kết luận có sweep".

**Hành động (Doctrine v2 Rule 3):** khi zoom xuống khung nhỏ hơn để tìm sweep "ẩn" bên trong một wick khung lớn, bắt buộc chấm đủ 5 điều kiện sweep checklist tại khung đã zoom — không được kết luận "có sweep" chỉ vì "có thể zoom vào và thấy một chỗ giá đảo nhẹ".



### Rule liên quan (Doctrine v2)

### Rule 13 — War Story illustrative không được dùng làm bằng chứng nâng tier
**Phát biểu:** mọi War Story gắn `war_story_type: illustrative` bị cấm dùng để đổi hoặc nâng tier bất kỳ rule nào trong Doctrine v2; chỉ War Story `real` (có ngày/giá thật, đã xảy ra với chính người viết) mới tính là dữ liệu, và ngay cả vậy vẫn chỉ n=1.
**Tier hiện tại:** Tier 0 (meta-rule quản trị bằng chứng).
**Nguồn:** §3.4.
