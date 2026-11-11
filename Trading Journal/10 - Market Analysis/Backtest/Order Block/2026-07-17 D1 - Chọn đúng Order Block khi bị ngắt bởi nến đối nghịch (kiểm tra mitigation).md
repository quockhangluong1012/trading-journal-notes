---
type: market-analysis
status: backtest
date: 2026-07-17
symbol: chưa xác định (ảnh chart không có nhãn symbol)
timeframe: D1 (Daily); MSS xác nhận trên LTF (khung nhỏ hơn, không nhãn)
session: không rõ (ảnh không nhãn thời gian)
htf_bias: bearish (sau MSS xác nhận trên LTF)
setup: 2022 Model - xác định đúng nến Order Block tại vùng đỉnh trước displacement giảm, khi vùng đỉnh có nhiều nến bullish nhưng bị ngắt quãng bởi nến đối nghịch ở giữa
in_trade: false
draw_on_liquidity: chưa xác định (ảnh không nhãn giá)
key_poi: "Bearish OB = nến 2 (ứng viên chính, liền kề trực tiếp trước displacement, chưa bị test) | nến 1 (ứng viên phụ, cần kiểm tra mitigation trước khi dùng lại)"
invalidation: n/a (note phương pháp, không vào lệnh)
topic: quy tắc chọn đúng nến Order Block khi vùng đỉnh có nhiều nến cùng chiều bị ngắt quãng bởi nến đối nghịch ở giữa; phân biệt gộp OB hợp lệ vs sai; kiểm tra mitigation trước khi tái sử dụng một OB cũ
tags:
  - analysis
  - methodology
  - order-block
  - market-structure-shift
  - fair-value-gap
  - ict-2022
  - displacement
  - order-block-mitigation
---
![[Pasted image 20260717085033.png]]
# D1 — Chọn đúng Order Block khi bị ngắt bởi nến đối nghịch (kiểm tra mitigation) — 2026-07-17

> [!info] Trạng thái
> **METHODOLOGY — không vào lệnh.** Note này tổng hợp toàn bộ quá trình phân tích một chart Daily (không nhãn symbol/giá) để trả lời câu hỏi: "vùng đỉnh có 2 nến bullish (đánh dấu 1 và 2) ứng viên làm [[25-OB-Order-Block|Order Block]], chọn nến nào?" — và sửa một sai lầm ban đầu về quy tắc gộp OB khi phát hiện có nến đối nghịch xen giữa.

![[OB-choose-candle-mitigation-20260717.svg]]

> [!warning] Ảnh gốc
> Ảnh chart do  gửi trong chat chưa được lưu vào vault. Nếu muốn tham chiếu lại chính xác, kéo ảnh vào `10 - Market Analysis/Attachments/` (đặt tên gợi ý `OB-daily-case-20260717-1.png`) và thêm dòng `![[OB-daily-case-20260717-1.png]]` phía trên. Sơ đồ SVG ở trên là **minh họa nguyên lý**, không phải chart thật (không có giá cụ thể vì ảnh gốc không nhãn).

## 0. Tóm tắt tình huống

Chart Daily cho thấy: nhịp giảm → đảo chiều tăng (chuỗi nến xanh) → tạo vùng đỉnh có **2 nến xanh được đánh dấu (1 và 2)** → sau đó là displacement giảm mạnh để lại **2 FVG lớn**, và có **Bearish MSS xác nhận trên LTF**. Câu hỏi cốt lõi: nến nào là Order Block hợp lệ, và tại sao thân nến 2 nhỏ không tự động loại nó ra.

## 1. Sai lầm ban đầu — và vì sao nó sai

Ở lượt phân tích đầu, tôi đề xuất "gộp nến 1 và nến 2 thành một compound OB" vì cho rằng đây là một cụm consolidation tại đỉnh.  chỉ ra đúng vấn đề: **giữa nến 1 và nến 2 thực ra có 3 nến bearish**, không phải một chuỗi liền mạch cùng màu.

Đây là điểm mấu chốt cần nhớ như một quy tắc cứng:

> [!important] Quy tắc gộp Order Block
> **Chỉ gộp các nến CÙNG MÀU, LIÊN TIẾP, không bị gián đoạn bởi nến đối nghịch.** Lý do: chuỗi nến cùng chiều liên tục đại diện cho MỘT giai đoạn order flow chưa bị đối nghịch can thiệp — không có phe đối lập nào "dùng" bớt thanh khoản/lệnh còn tồn đọng ở giữa. Ngay khi có một hoặc nhiều nến đối nghịch xen vào, chuỗi đó bị cắt về mặt order-flow: đó là một nhịp phản ứng độc lập của phe đối lập, có thể đã **giao dịch ngược vào vùng của nến trước đó** và hấp thụ một phần lệnh còn sót. Gộp xuyên qua nến đối nghịch sẽ trộn lẫn "vùng lệnh mua chưa khớp" với "vùng lệnh bán đã khớp" — phá vỡ logic institutional footprint mà OB cố gắng mô tả.

Do đó: **không gộp nến 1 và nến 2** trong case này. Chúng phải được xét như hai ứng viên OB tách biệt.

## 2. Bốn tiêu chí xác thực một Order Block (áp dụng lại từ đầu)

| Tiêu chí | Câu hỏi | Áp dụng cho case này |
|---|---|---|
| Vị trí | Đây có phải nến ngược màu cuối cùng liền kề trước displacement không? | Nến 2 đạt — không có nến đối nghịch nào giữa nó và cú giảm mạnh |
| Imbalance | Displacement có để lại FVG không? | Đạt —  xác nhận **2 FVG lớn** |
| Xác nhận cấu trúc | Có MSS xác nhận đảo chiều không? | Đạt — **Bearish MSS trên LTF** |
| Tính "sạch" (chưa bị test) | Vùng này đã bị giá quay lại giao dịch xuyên qua trước displacement chưa? | Nến 2: **chưa** (liền kề trực tiếp). Nến 1: **cần kiểm tra** (xem mục 4) |

Với timeframe Daily, thân nến 2 nhỏ **không phải điều kiện loại bỏ** — quan trọng hơn là nó thỏa cả 4 tiêu chí trên, đặc biệt là tiêu chí "sạch". Thân nhỏ chỉ phản ánh conviction yếu về mặt tâm lý thị trường tại thời điểm đó, không phủ nhận vai trò OB của nó.

## 3. Vì sao nến 2 là POI chính

Nến 2 thỏa đồng thời cả 4 tiêu chí, đặc biệt là tiêu chí quan trọng nhất trong tình huống này: **không có nến đối nghịch nào chen giữa nó và displacement**, nên chưa có cơ hội để giá "dùng trước" thanh khoản ở đó. Kết hợp với 2 FVG lớn (xác nhận imbalance thật) và Bearish MSS trên LTF (xác nhận đảo chiều cấu trúc), nến 2 là **ứng viên Order Block đáng tin cậy nhất** để dùng làm POI khi backtest hoặc theo dõi retest.

## 4. Vai trò còn lại của nến 1 — câu hỏi cần  tự kiểm tra trên chart

Nến 1 tạo ra swing high thực sự của nhịp tăng — có khả năng là nơi buy-side liquidity cũ bị quét. Nhưng để biết nó còn giá trị gì không với vai trò OB dự phòng, cần trả lời một câu hỏi duy nhất:

> [!question] Câu hỏi mitigation
> Trong 3 nến bearish giữa nến 1 và nến 2, giá có **đóng cửa hoặc thân nến xuyên ngược vào thân (body) của nến 1** hay không?

- **Nếu có** → nến 1 coi như đã bị giao dịch xuyên qua một phần (lệnh mua còn tồn đọng ở đó đã bị hấp thụ một phần) → bỏ qua, chỉ dùng nến 2 làm POI.
- **Nếu không** (3 nến bearish chỉ retrace nhẹ, chưa chạm lại thân nến 1) → nến 1 vẫn là một OB dự phòng ở cấp cao hơn, hữu ích nếu sau này giá phá thủng nến 2 mà chưa đảo chiều hẳn (giá có thể phản ứng thêm lần nữa tại nến 1 trước khi tiếp tục giảm).

> [!note] Phân biệt với khái niệm Mitigation Block (MB) trong vault
> Câu hỏi ở trên dùng chữ "mitigate" theo nghĩa chung (giá đã giao dịch xuyên qua một vùng OB, hấp thụ bớt lệnh tồn đọng) — **khác** với khái niệm formal **[[22-Mitigation-Block|Mitigation Block]]** đã có trong vault. Mitigation Block là một loại POI cụ thể, sinh ra từ **failure swing KHÔNG có sweep** (đáy/đỉnh cũ giữ vững) rồi MSS xác nhận — một cấu trúc khác hẳn với tình huống đang xét ở đây (nến 1 tạo swing high mới, tức đã sweep, không phải failure swing). Đừng gọi nến 1 là "Mitigation Block" — ở đây chỉ đang kiểm tra xem nến 1 có bị **mitigated** (giao dịch xuyên qua, mất giá trị POI) theo nghĩa thông thường hay không.

## 5. Cách vẽ vùng entry cho nến 2 khi backtest

- **OB range**: high–low của riêng nến 2 (không gộp thêm nến nào khác, theo đúng quy tắc mục 1).
- **CE ([[10-Consequent-Encroachment-Mean-Threshold|Consequent Encroachment]], 50%)**: dùng làm mức entry tham chiếu chính, thay vì vào ngay tại high của toàn vùng OB.
- **Confluence**: đối chiếu CE của nến 2 với FVG gần nhất trong 2 FVG mà displacement để lại — nếu chúng trùng vùng (overlap), đó là điểm entry chất lượng cao (POI confluence), ưu tiên ghi nhận khi backtest.
- Xác nhận thêm bằng [[27-Premium-Discount|Premium/Discount]] của dealing range liên quan trước khi coi đây là setup đủ điều kiện log vào `04 - Backtesting/`.

## 6. Concept đã áp dụng

- [[25-OB-Order-Block]] — [[13-FVG-Fair-Value-Gap]] — [[21-Market-Structure-Shift]] — [[35-Aggressive-Displacement-Entry]]
- [[10-Consequent-Encroachment-Mean-Threshold]] — [[27-Premium-Discount]] — [[20-Liquidity-Sweep]] — [[22-Mitigation-Block]] (tham khảo phân biệt, không phải case này)
- [[01 - ICT 2022 Model]]

## 7. Bài học rút ra

1. **Chỉ gộp Order Block khi các nến cùng màu liên tiếp, không bị ngắt quãng.** Có nến đối nghịch xen giữa → tách thành các ứng viên riêng biệt, không gộp.
2. **Thân nến nhỏ không loại bỏ tính hợp lệ của một OB** trên Daily — điều quyết định là vị trí (liền kề trước displacement), imbalance (FVG), và xác nhận cấu trúc (MSS), không phải kích thước thân nến.
3. **Trước khi tái sử dụng một OB cũ (như nến 1) làm POI dự phòng, phải kiểm tra xem nó đã bị giao dịch xuyên qua (mitigated) bởi các nến đối nghịch phía sau chưa.** Nếu đã bị test, giá trị của nó giảm đáng kể.
4. **Phân biệt rõ "mitigated" (nghĩa chung, một OB bị giao dịch xuyên qua) với khái niệm formal [[22-Mitigation-Block|Mitigation Block]]** (một loại POI cụ thể từ failure swing không sweep) để tránh nhầm lẫn thuật ngữ khi ghi log.

## 8. Câu hỏi cần chốt (chưa xác nhận)

- **Symbol + khung thời gian chính xác** của chart (ảnh gốc không nhãn) — cần để log vào `04 - Backtesting/` nếu sau này setup này được test thật.
- **Kết quả kiểm tra mitigation ở mục 4**: 3 nến bearish giữa nến 1 và nến 2 có chạy ngược vào thân nến 1 hay không?  tự kiểm tra trên chart gốc và cho biết để cập nhật note này.
- Vị trí nến 2 so với **premium/discount** của dealing range liên quan (cần range high/low thật để tính).

## 9. Next steps

- Nếu  xác nhận mitigation ở mục 4 và có giá cụ thể, cập nhật note này hoặc tạo file backtest chi tiết trong `04 - Backtesting/`, cross-link ngược về note này.
- Nếu case này lặp lại nhiều lần (vùng đỉnh có consolidation bị ngắt bởi nến đối nghịch), cân nhắc viết thành một entry riêng trong `03 - Playbooks/` với checklist "khi nào gộp OB, khi nào tách".

---
*Ghi chú: ảnh gốc không nhãn symbol/giá/thời gian; đây là note phương pháp (methodology), không log backtest vì không vào lệnh. Sơ đồ SVG là minh họa nguyên lý theo đúng bố cục 2 nến (1 và 2) + 3 nến bearish xen giữa mà  mô tả, không phải chart thật.*


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
