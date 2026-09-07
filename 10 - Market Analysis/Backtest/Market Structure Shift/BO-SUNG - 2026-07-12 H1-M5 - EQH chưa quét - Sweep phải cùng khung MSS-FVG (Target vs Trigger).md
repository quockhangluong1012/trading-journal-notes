---
case_title: "2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)"
type: audit-addendum-standalone
audit_date: 2026-08-02
note_status_suggestion: "methodology"
evidence_tier_suggestion: 0
---

# 🔍 Bổ sung audit cho: 2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)

> [!warning] File gốc không có trong phiên làm việc này
> File note gốc "2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)" không nằm trong các file được tải lên phiên fork này (chỉ 10/15 file gốc có sẵn). Nội dung dưới đây được trích từ bản audit tổng — dán trực tiếp vào cuối file gốc trong vault Obsidian của cậu để hoàn tất việc bổ sung cho case này. Đồng thời sửa frontmatter `status:` thành `methodology` và thêm `evidence_tier: 0`.

> [!info] Nguồn
> Phần dưới đây được trích trực tiếp từ bản audit tổng [[2026-08-02 - Deep Audit 15 Case Studies - Doctrine v2]] (mục 4, case #6/15) và tách vào ngay file gốc để không phải mở file tổng mỗi lần tra cứu. Bảng tra cứu đầy đủ 15 case và các phần audit hệ thống/tranh biện/doctrine dùng chung vẫn nằm ở file tổng.

**Tóm tắt:** Review một lệnh MISS (không phải lệnh thắng/thua). Giá đảo chiều ngay tại OB H1 nhưng vì đang chờ EQH phía trên bị quét, không vào dù M5 đã cho MSS. Chẩn đoán: lỗi lệch khung (scale mismatch) — sweep cho trigger M5 phải cùng khung M5, không phải bể EQH cấp H1.

**Điểm mạnh:** đây là note có chất lượng tranh biện nội tại tốt nhất trong 15 file — tự đặt ra chính xung đột ("purge EQH trước hay không") rồi giải quyết bằng nguyên tắc phân xử theo bằng chứng thời gian thực (mục 4: "để M5 phân xử") thay vì chọn phe cố định; ba War Story (W1, W2, W3) vẽ ranh giới hai chiều sai rất khéo — không chỉ sửa lỗi gốc mà còn cảnh báo lỗi over-correction (W2: chase sau miss).

**Lỗ hổng/điểm mù:** đây cũng là note duy nhất tường minh nói ra tại sao khái niệm "EQH = target không phải trigger" có thể tự mâu thuẫn (mục 5: "nếu giá thật sự lên quét EQH, OB có thể đã bị phá và setup không còn giá trị") nhưng KHÔNG đưa ra cách giải quyết mâu thuẫn đó ngoài "kiểm chứng bằng cách kéo chart sang phải xem sau" — tức là chấp nhận đây là một câu hỏi mở, chưa có quy tắc quyết định trước (ex-ante), chỉ có thể đánh giá sau (ex-post).

> [!question] Tranh biện Devil's Advocate (đa vòng)
> **Luận điểm ban đầu:** "M5 luôn là trọng tài cuối cùng — sweep + MSS cùng khung tại OB là đủ, không cần chờ EQH."
>
> **Phản biện vòng 1:** Nguyên tắc này ưu tiên khung entry (M5) hơn khung target (H1/D1) một cách gần như tuyệt đối. Nhưng nếu bể EQH thực sự "béo" (4 đỉnh ngang, nhiều tuần tích lũy) và OB H1 chỉ là một phản ứng nhỏ mới hình thành, há chẳng phải bể lớn hơn có "trọng lượng hấp dẫn" market-maker mạnh hơn một MSS M5 đơn lẻ? W1 trong chính note này thừa nhận đúng kịch bản này có thể xảy ra ("đôi khi thị trường thực sự cần dọn sạch cả bể xa mới đủ nhiên liệu cho một cú đảo chiều xứng tầm").
>
> **Phản-phản biện:** Đúng, nhưng W1 cũng nói rõ: "cái phân xử duy nhất là bằng chứng M5 tại lần chạm đầu: có hay không có" — nghĩa là nguyên tắc không phải "M5 luôn thắng bất kể", mà là "M5 là bằng chứng CÓ SẴN duy nhất tại thời điểm quyết định TRƯỚC KHI biết bể xa có bị dọn hay không". Đây là khác biệt quan trọng giữa "M5 luôn đúng" (sai) và "M5 là bằng chứng duy nhất khả dụng ex-ante" (đúng, khiêm tốn hơn).
>
> **Phản biện vòng 2:** Nhưng nếu vậy, hai kịch bản (M5 xác nhận tại OB gần / M5 không xác nhận, giá chạy tới EQH xa) đều đúng-về-sau theo cách chính bằng chứng chúng tạo ra — nói cách khác nguyên tắc này không thể sai được bằng thiết kế (unfalsifiable trong ngắn hạn), vì bất kỳ kết quả nào cũng "giải thích được" sau khi nó xảy ra. Đây là dấu hiệu cảnh báo kinh điển của một framework có vẻ chặt chẽ nhưng thực chất mô tả lại quá khứ tốt hơn là dự đoán tương lai.
>
> **Phản-phản biện cuối:** Điểm này đúng về mặt triết học khoa học, nhưng không làm framework vô dụng — nó chỉ có nghĩa framework này thuộc nhóm "quy tắc quyết định hành động tại thời điểm t" (what to do NOW, given evidence NOW), không phải "mô hình dự đoán xác suất". Với một quy tắc hành động (không phải dự đoán), tiêu chuẩn đánh giá đúng không phải "có dự đoán đúng bể nào sẽ bị dọn" mà là "hành động dựa trên nó có nhất quán và có kỷ luật hay không qua nhiều lần lặp lại" — đó là câu hỏi Tier 1 (cần n≥20), chưa trả lời được ở đây.
>
> **Phán quyết:** Nguyên tắc "M5 là trọng tài, đánh giá bằng chứng thời điểm hiện tại thay vì đoán trước" là một **quy tắc quyết định hợp lý về logic** (không unfalsifiable theo nghĩa xấu — nó chỉ đơn giản là một chính sách hành động, không phải một tiên đoán) nhưng **hiệu quả thực của chính sách này (so với các chính sách khác như "luôn chờ bể lớn nhất") chưa được đo** — cần backtest so sánh 2 chính sách trên cùng bộ setup.

**Hành động:** thêm case này vào backlog thu thập dữ liệu Tier 1 — so sánh 2 chính sách (a) vào ngay khi M5 xác nhận tại bể gần vs (b) luôn chờ bể HTF xa bị quét, trên cùng ≥20 setup dạng "OB có bể HTF ngay phía trên".

**Đề xuất field đo lường:** `m5_confirmed_at_first_tap`, `htf_pool_intervened`, `missed_valid_setup`, `chased_after_miss`, `liquidity_layers_mapped` — cả 5 field đã đề xuất sẵn trong note gốc, đưa thẳng vào schema Doctrine v2 §6 Rule 14.

![[liquidity-fractal-scale-alignment-20260802.svg]]


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


### 5.4 — "HTF pool = target không phải trigger" (note EQH 07-12) vs "external sweep = narrative confirmation" (note 07-20)

**Bề mặt có vẻ mâu thuẫn:** note EQH 07-12 nói dứt khoát: EQH cấp HTF là TARGET (draw tương lai), không phải điều kiện vào lệnh — đừng chờ nó bị quét mới trigger. Note EURUSD 07-20 lại dùng chính việc "external BSL 1.16874/1.16919 đã bị quét" như một phần bằng chứng CỦNG CỐ narrative bearish, gần như một điều kiện hỗ trợ cho quyết định vào lệnh.

> [!question] Tranh biện đa vòng
> **Vòng 1:** Nếu external sweep đã xảy ra (BSL 1.16874/1.16919 bị quét ở note 07-20) được dùng để "củng cố narrative", vậy nó đang đóng vai trò gần giống một ĐIỀU KIỆN HỖ TRỢ cho quyết định vào lệnh — về bản chất khác gì "chờ EQH bị quét" mà note EQH 07-12 phê phán?
>
> **Vòng 2 — Phân biệt THỜI ĐIỂM sử dụng bằng chứng:** Khác biệt cốt lõi nằm ở THỜI ĐIỂM đánh giá: note EQH 07-12 phê phán việc CHỜ (tương lai, chưa xảy ra) một sự kiện HTF làm điều kiện TRIGGER bắt buộc trước khi hành động. Note 07-20 dùng một sự kiện HTF ĐÃ XẢY RA (quá khứ, external sweep đã hoàn tất) như một mảnh bằng chứng bổ sung cho bức tranh tổng thể, không phải điều kiện phải chờ thêm. Nói cách khác: "external sweep đã xảy ra, đây là một phần bằng chứng của bối cảnh hiện tại" (hợp lệ, không mâu thuẫn với note EQH) khác với "tôi sẽ không vào lệnh cho tới khi external sweep xảy ra" (đây mới là điều bị phê phán).
>
> **Vòng 3 — Phản biện lại sự phân biệt trên:** Nhưng ranh giới giữa "dùng làm bối cảnh" và "dùng làm điều kiện chờ" có thể rất mỏng trong thực hành. Nếu note 07-20 viết narrative theo kiểu "vì external sweep đã xác nhận, tôi tự tin hơn với hướng bearish" — điều gì ngăn cản, ở một setup TƯƠNG LAI mà external sweep CHƯA xảy ra, cùng logic đó bị lật thành "tôi cần chờ external sweep xảy ra trước khi tự tin đủ để vào lệnh" — đúng chính xác cái bẫy mà note EQH 07-12 cảnh báo?
>
> **Vòng 4 — Giải quyết bằng quy tắc thời gian tường minh:** Ranh giới đúng không nằm ở "đã xảy ra hay chưa" một cách chung chung, mà ở việc quy tắc entry (trigger) có PHỤ THUỘC logic vào sự kiện HTF đó hay không. Nếu trigger thực sự là "Sweep M5 + MSS M5 + FVG M5 tại POI" (như note EQH 07-12 định nghĩa) và external sweep HTF chỉ là một dòng ghi chú bối cảnh KHÔNG NẰM trong điều kiện trigger chính thức, thì việc nó "đã xảy ra hay chưa" không ảnh hưởng quyết định vào/không vào — chỉ ảnh hưởng CONFIDENCE/SIZE. Đây chính là điều note 07-20 đang làm đúng: external sweep dùng để tăng/giảm độ tự tin, KHÔNG phải một điều kiện trong checklist trigger chính thức của nó (checklist trigger vẫn là M15 sweep→MSS→displacement, độc lập với external sweep).
>
> **Phán quyết:** Không mâu thuẫn thật khi trigger chính thức được định nghĩa tách bạch khỏi bằng chứng bối cảnh — nhưng đây là ranh giới DỄ BỊ XÓA NHÒA trong thực hành nếu không viết tường minh. Rủi ro thật: nếu một ngày nào đó cậu viết narrative kiểu "chờ external sweep rồi mới chắc" cho một setup TƯƠNG LAI (external sweep chưa xảy ra), đó là lúc quy tắc EQH 07-12 bị vi phạm thật.

**Hành động (Doctrine v2 Rule 4):** trong mọi note tương lai, tách rõ 2 mục trong phần setup: "Trigger chính thức" (điều kiện đủ + cần để vào lệnh, luôn ở khung entry) và "Bối cảnh hỗ trợ" (bao gồm external HTF sweep đã xảy ra, SMT divergence...) — không để hai mục này trộn lẫn trong cùng một đoạn văn xuôi.



### Rule liên quan (Doctrine v2)

### Rule 15 — Taxonomy `status` tách 4 giá trị, đồng bộ với `in_trade`
**Phát biểu:** `status: analysis | watchlist | backtest | live`; `status: backtest` hoặc `live` bắt buộc `in_trade: true` kèm entry/SL/TP/R-multiple; `in_trade: false` chỉ được đi với `analysis` hoặc `watchlist`.
**Tier hiện tại:** N/A (quy ước vận hành, không phải rule thị trường).
**Nguồn:** §3.5.


### Rule 3 — Sweep phải cùng khung (scale) với MSS/FVG; HTF pool là target, không phải trigger
**Phát biểu:** trigger cho một entry (Sweep + MSS + FVG) phải xảy ra cùng cấp độ (scale) với khung entry đã chọn; một bể liquidity ở khung cao hơn (EQH/EQL H1/D1) chỉ đóng vai trò TARGET (draw tương lai), không được dùng làm điều kiện chờ trước khi trigger khung entry được kích hoạt. Khi zoom xuống khung nhỏ hơn để xác nhận sweep "ẩn" trong một wick khung lớn, bắt buộc áp đủ 5 điều kiện sweep checklist tại khung đã zoom.
**Tier hiện tại:** Tier 0 (giả thuyết hợp lý, có 1 case minh họa dạng miss — không có lệnh thật để đo).
**Điều kiện nâng tier:** ≥20 setup dạng "OB có bể HTF ngay phía trên", so sánh 2 chính sách (vào khi M5 xác nhận tại bể gần / chờ bể xa bị quét).
**Nguồn:** case 4.6 (EQH 07-12), case 4.7 (Internal Sweep 07-13), §5.3.
