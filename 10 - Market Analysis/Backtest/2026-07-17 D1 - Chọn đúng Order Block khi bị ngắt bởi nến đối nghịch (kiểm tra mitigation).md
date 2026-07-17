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
> **METHODOLOGY — không vào lệnh.** Note này tổng hợp toàn bộ quá trình phân tích một chart Daily (không nhãn symbol/giá) để trả lời câu hỏi: "vùng đỉnh có 2 nến bullish (đánh dấu 1 và 2) ứng viên làm [[25 - OB - Order Block|Order Block]], chọn nến nào?" — và sửa một sai lầm ban đầu về quy tắc gộp OB khi phát hiện có nến đối nghịch xen giữa.

![[OB-choose-candle-mitigation-20260717.svg]]

> [!warning] Ảnh gốc
> Ảnh chart do Khang gửi trong chat chưa được lưu vào vault. Nếu muốn tham chiếu lại chính xác, kéo ảnh vào `10 - Market Analysis/Attachments/` (đặt tên gợi ý `OB-daily-case-20260717-1.png`) và thêm dòng `![[OB-daily-case-20260717-1.png]]` phía trên. Sơ đồ SVG ở trên là **minh họa nguyên lý**, không phải chart thật (không có giá cụ thể vì ảnh gốc không nhãn).

## 0. Tóm tắt tình huống

Chart Daily cho thấy: nhịp giảm → đảo chiều tăng (chuỗi nến xanh) → tạo vùng đỉnh có **2 nến xanh được đánh dấu (1 và 2)** → sau đó là displacement giảm mạnh để lại **2 FVG lớn**, và có **Bearish MSS xác nhận trên LTF**. Câu hỏi cốt lõi: nến nào là Order Block hợp lệ, và tại sao thân nến 2 nhỏ không tự động loại nó ra.

## 1. Sai lầm ban đầu — và vì sao nó sai

Ở lượt phân tích đầu, tôi đề xuất "gộp nến 1 và nến 2 thành một compound OB" vì cho rằng đây là một cụm consolidation tại đỉnh. Khang chỉ ra đúng vấn đề: **giữa nến 1 và nến 2 thực ra có 3 nến bearish**, không phải một chuỗi liền mạch cùng màu.

Đây là điểm mấu chốt cần nhớ như một quy tắc cứng:

> [!important] Quy tắc gộp Order Block
> **Chỉ gộp các nến CÙNG MÀU, LIÊN TIẾP, không bị gián đoạn bởi nến đối nghịch.** Lý do: chuỗi nến cùng chiều liên tục đại diện cho MỘT giai đoạn order flow chưa bị đối nghịch can thiệp — không có phe đối lập nào "dùng" bớt thanh khoản/lệnh còn tồn đọng ở giữa. Ngay khi có một hoặc nhiều nến đối nghịch xen vào, chuỗi đó bị cắt về mặt order-flow: đó là một nhịp phản ứng độc lập của phe đối lập, có thể đã **giao dịch ngược vào vùng của nến trước đó** và hấp thụ một phần lệnh còn sót. Gộp xuyên qua nến đối nghịch sẽ trộn lẫn "vùng lệnh mua chưa khớp" với "vùng lệnh bán đã khớp" — phá vỡ logic institutional footprint mà OB cố gắng mô tả.

Do đó: **không gộp nến 1 và nến 2** trong case này. Chúng phải được xét như hai ứng viên OB tách biệt.

## 2. Bốn tiêu chí xác thực một Order Block (áp dụng lại từ đầu)

| Tiêu chí | Câu hỏi | Áp dụng cho case này |
|---|---|---|
| Vị trí | Đây có phải nến ngược màu cuối cùng liền kề trước displacement không? | Nến 2 đạt — không có nến đối nghịch nào giữa nó và cú giảm mạnh |
| Imbalance | Displacement có để lại FVG không? | Đạt — Khang xác nhận **2 FVG lớn** |
| Xác nhận cấu trúc | Có MSS xác nhận đảo chiều không? | Đạt — **Bearish MSS trên LTF** |
| Tính "sạch" (chưa bị test) | Vùng này đã bị giá quay lại giao dịch xuyên qua trước displacement chưa? | Nến 2: **chưa** (liền kề trực tiếp). Nến 1: **cần kiểm tra** (xem mục 4) |

Với timeframe Daily, thân nến 2 nhỏ **không phải điều kiện loại bỏ** — quan trọng hơn là nó thỏa cả 4 tiêu chí trên, đặc biệt là tiêu chí "sạch". Thân nhỏ chỉ phản ánh conviction yếu về mặt tâm lý thị trường tại thời điểm đó, không phủ nhận vai trò OB của nó.

## 3. Vì sao nến 2 là POI chính

Nến 2 thỏa đồng thời cả 4 tiêu chí, đặc biệt là tiêu chí quan trọng nhất trong tình huống này: **không có nến đối nghịch nào chen giữa nó và displacement**, nên chưa có cơ hội để giá "dùng trước" thanh khoản ở đó. Kết hợp với 2 FVG lớn (xác nhận imbalance thật) và Bearish MSS trên LTF (xác nhận đảo chiều cấu trúc), nến 2 là **ứng viên Order Block đáng tin cậy nhất** để dùng làm POI khi backtest hoặc theo dõi retest.

## 4. Vai trò còn lại của nến 1 — câu hỏi cần Khang tự kiểm tra trên chart

Nến 1 tạo ra swing high thực sự của nhịp tăng — có khả năng là nơi buy-side liquidity cũ bị quét. Nhưng để biết nó còn giá trị gì không với vai trò OB dự phòng, cần trả lời một câu hỏi duy nhất:

> [!question] Câu hỏi mitigation
> Trong 3 nến bearish giữa nến 1 và nến 2, giá có **đóng cửa hoặc thân nến xuyên ngược vào thân (body) của nến 1** hay không?

- **Nếu có** → nến 1 coi như đã bị giao dịch xuyên qua một phần (lệnh mua còn tồn đọng ở đó đã bị hấp thụ một phần) → bỏ qua, chỉ dùng nến 2 làm POI.
- **Nếu không** (3 nến bearish chỉ retrace nhẹ, chưa chạm lại thân nến 1) → nến 1 vẫn là một OB dự phòng ở cấp cao hơn, hữu ích nếu sau này giá phá thủng nến 2 mà chưa đảo chiều hẳn (giá có thể phản ứng thêm lần nữa tại nến 1 trước khi tiếp tục giảm).

> [!note] Phân biệt với khái niệm Mitigation Block (MB) trong vault
> Câu hỏi ở trên dùng chữ "mitigate" theo nghĩa chung (giá đã giao dịch xuyên qua một vùng OB, hấp thụ bớt lệnh tồn đọng) — **khác** với khái niệm formal **[[22 - Mitigation Block|Mitigation Block]]** đã có trong vault. Mitigation Block là một loại POI cụ thể, sinh ra từ **failure swing KHÔNG có sweep** (đáy/đỉnh cũ giữ vững) rồi MSS xác nhận — một cấu trúc khác hẳn với tình huống đang xét ở đây (nến 1 tạo swing high mới, tức đã sweep, không phải failure swing). Đừng gọi nến 1 là "Mitigation Block" — ở đây chỉ đang kiểm tra xem nến 1 có bị **mitigated** (giao dịch xuyên qua, mất giá trị POI) theo nghĩa thông thường hay không.

## 5. Cách vẽ vùng entry cho nến 2 khi backtest

- **OB range**: high–low của riêng nến 2 (không gộp thêm nến nào khác, theo đúng quy tắc mục 1).
- **CE ([[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment]], 50%)**: dùng làm mức entry tham chiếu chính, thay vì vào ngay tại high của toàn vùng OB.
- **Confluence**: đối chiếu CE của nến 2 với FVG gần nhất trong 2 FVG mà displacement để lại — nếu chúng trùng vùng (overlap), đó là điểm entry chất lượng cao (POI confluence), ưu tiên ghi nhận khi backtest.
- Xác nhận thêm bằng [[27 - Premium Discount|Premium/Discount]] của dealing range liên quan trước khi coi đây là setup đủ điều kiện log vào `04 - Backtesting/`.

## 6. Concept đã áp dụng

- [[25 - OB - Order Block]] — [[13 - FVG  - Fair Value Gap]] — [[21 - Market Structure Shift]] — [[35 - Aggressive Displacement Entry]]
- [[10 - Consequent Encroachment (Mean Threshold)]] — [[27 - Premium Discount]] — [[20 - Liquidity Sweep]] — [[22 - Mitigation Block]] (tham khảo phân biệt, không phải case này)
- [[01 - ICT 2022 Model]]

## 7. Bài học rút ra

1. **Chỉ gộp Order Block khi các nến cùng màu liên tiếp, không bị ngắt quãng.** Có nến đối nghịch xen giữa → tách thành các ứng viên riêng biệt, không gộp.
2. **Thân nến nhỏ không loại bỏ tính hợp lệ của một OB** trên Daily — điều quyết định là vị trí (liền kề trước displacement), imbalance (FVG), và xác nhận cấu trúc (MSS), không phải kích thước thân nến.
3. **Trước khi tái sử dụng một OB cũ (như nến 1) làm POI dự phòng, phải kiểm tra xem nó đã bị giao dịch xuyên qua (mitigated) bởi các nến đối nghịch phía sau chưa.** Nếu đã bị test, giá trị của nó giảm đáng kể.
4. **Phân biệt rõ "mitigated" (nghĩa chung, một OB bị giao dịch xuyên qua) với khái niệm formal [[22 - Mitigation Block|Mitigation Block]]** (một loại POI cụ thể từ failure swing không sweep) để tránh nhầm lẫn thuật ngữ khi ghi log.

## 8. Câu hỏi cần chốt (chưa xác nhận)

- **Symbol + khung thời gian chính xác** của chart (ảnh gốc không nhãn) — cần để log vào `04 - Backtesting/` nếu sau này setup này được test thật.
- **Kết quả kiểm tra mitigation ở mục 4**: 3 nến bearish giữa nến 1 và nến 2 có chạy ngược vào thân nến 1 hay không? Khang tự kiểm tra trên chart gốc và cho biết để cập nhật note này.
- Vị trí nến 2 so với **premium/discount** của dealing range liên quan (cần range high/low thật để tính).

## 9. Next steps

- Nếu Khang xác nhận mitigation ở mục 4 và có giá cụ thể, cập nhật note này hoặc tạo file backtest chi tiết trong `04 - Backtesting/`, cross-link ngược về note này.
- Nếu case này lặp lại nhiều lần (vùng đỉnh có consolidation bị ngắt bởi nến đối nghịch), cân nhắc viết thành một entry riêng trong `03 - Playbooks/` với checklist "khi nào gộp OB, khi nào tách".

---
*Ghi chú: ảnh gốc không nhãn symbol/giá/thời gian; đây là note phương pháp (methodology), không log backtest vì không vào lệnh. Sơ đồ SVG là minh họa nguyên lý theo đúng bố cục 2 nến (1 và 2) + 3 nến bearish xen giữa mà Khang mô tả, không phải chart thật.*
