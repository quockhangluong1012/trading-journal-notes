---
type: market-analysis
status: methodology
date: 2026-07-19
symbol: "chưa xác định — ảnh chart gốc không nhãn symbol; vùng giá 1.27–1.40 trong giai đoạn 08/2013–05/2014 gợi ý khả năng cao là EURUSD lịch sử, nhưng CẦN Khang xác nhận trước khi dùng số liệu này cho bất kỳ kết luận backtest nào"
timeframe: "chưa xác định — ảnh hiển thị nhiều tháng trên một màn hình, nhiều khả năng D1, cần Khang xác nhận"
session: không rõ (ảnh không nhãn phiên/giờ)
htf_bias: "bullish trong leg Feb'14 → May'14 (leg đang active, đây là leg Khang đang phân tích) → hiện đang trong nhịp retrace giảm, giá vừa cắt xuống dưới CE của leg này; bối cảnh lớn hơn từ Nov'13 vẫn là một chuỗi higher-lows liên tục cho tới khi Feb'14 low bị phá thật"
setup: "Không phải một setup entry — đây là methodology note trả lời câu hỏi: giữa nhiều đáy cạnh tranh (Nov'13 ~1.330 và Feb'14 1.34792), đáy nào là Dealing Range Low hợp lệ cho leg hiện tại, và đáy còn lại đóng vai trò gì (draw on liquidity hay chỉ là nhiễu)"
in_trade: false
draw_on_liquidity: "Ngắn hạn/hiện tại: SSL tại Feb'14 low 1.34792 (đáy Dealing Range đang dùng, chưa bị phá). Có điều kiện, nếu Feb'14 bị phá bởi một MSS giảm thật: draw kế tiếp hướng xuống — cần kiểm tra trước xem có pool nào nằm gần hơn giữa Feb'14 và Nov'13 hay không, rồi mới coi Nov'13 low (~1.330, ước lượng từ ảnh, cần Khang xác nhận giá chính xác) là target xa hơn."
key_poi: "CE (Equilibrium) của Dealing Range Feb'14–May'14 ≈ 1.37348 (tính từ (1.34792+1.39904)/2). Giá hiện tại theo đường giá trên platform ~1.37271, tức vừa lọt vào discount khoảng 7–8 pip. Chưa xác định được PD array cụ thể (FVG/OB) tại vùng này từ ảnh gốc — cần Khang bổ sung."
invalidation: "Đóng nến thân (không chỉ wick) dưới Feb'14 low 1.34792 kèm Market Structure Shift giảm trên khung phân tích — lúc đó Dealing Range hiện tại mới thực sự hết hiệu lực và cần vẽ lại, đồng thời Nov'13 low mới chính thức trở thành draw on liquidity chính thay vì chỉ là một pool dự phòng."
topic: "Khung quyết định 3 bước để chọn đúng Dealing Range Low khi có nhiều đáy cạnh tranh trong một chuỗi higher-lows; phân biệt đáy làm range-anchor hiện tại (MSS origin của leg đang active) với đáy chỉ là draw-on-liquidity ở degree cao hơn (locked swing); áp dụng cụ thể vào case Nov'13 vs Feb'14; tính lại Premium/Discount/CE cho leg đang active và xác định vị trí giá hiện tại"
tags:
  - analysis
  - methodology
  - dealing-range
  - premium-discount
  - draw-on-liquidity
  - liquidity-scale-alignment
  - market-structure
  - locked-swing
  - ict-2022
---

# Chọn Dealing Range Low giữa nhiều đáy cạnh tranh — Nov'13 vs Feb'14 — 2026-07-19

> [!info] Trạng thái
> **METHODOLOGY — không vào lệnh.** Note này tổng hợp toàn bộ buổi phân tích một chart lịch sử (không nhãn symbol/khung thời gian) mà Khang gửi trong chat, xoay quanh hai câu hỏi liên tiếp: *(1) Dealing Range đánh dấu trên chart (đỉnh 1.39904, đáy 1.34792) đã đúng chưa?* và *(2) giữa hai đáy cạnh tranh — SSL tại Nov'13 (~1.330) và swing low Feb'14 (1.34792) — nên chọn đáy nào làm Dealing Range Low, và đáy còn lại có phải target kế tiếp không?* Khung lý thuyết nền đã có sẵn trong vault tại [[12 - Dealing Range]] (đặc biệt mục 9 "Lỗi thường gặp" và mục A2 "Nested ranges") và [[16 - Internal & External Range Liquidity (IRL & ERL)]] (mục "tính phân dạng") — note này **áp dụng trực tiếp** hai bài đó vào case cụ thể, đồng thời **hệ thống hóa thành một khung quyết định 3 bước** mà vault chưa có ở dạng thao tác được (actionable), để Khang tái sử dụng cho mọi chart sau này có nhiều đáy/đỉnh cạnh tranh.

![[Pasted image 20260719145010.png]]

---

## 0. Tóm tắt tình huống

Chart Khang gửi cho thấy một chuỗi diễn biến giá trải dài khoảng 9 tháng (Aug 2013 → May 2014), với các mốc giá đã đọc được: đỉnh cao nhất toàn chart **1.39904** (chạm hai lần, khoảng tháng 3 và tháng 5/'14), một đáy sâu **1.34792** khoảng tháng 1–2/'14 ngay trước cú displacement tăng cực mạnh lên đỉnh trên, và một đường giá hiện tại quanh **1.37271**. Bên trái, khoảng tháng 11/'13, có một đáy sâu hơn (~1.330, ước lượng bằng mắt từ chart) mà giá chưa từng quay lại kiểm tra.

Khang đã tự vẽ Dealing Range với đỉnh = 1.39904, đáy = 1.34792, và đặt câu hỏi liệu range này đúng chưa, sau đó hỏi tiếp: nên chọn đáy Feb'14 hay đáy Nov'13 làm Dealing Range Low, và nếu Feb'14 bị phá thì đáy Nov'13 có tự động là target kế tiếp không.

**Kết luận ngắn gọn (chi tiết ở các mục dưới):** Dealing Range đánh dấu (1.34792 – 1.39904) là **đúng** cho leg hiện tại. Đáy Nov'13 **không phải** ứng viên cho range-anchor — nó là một pool thanh khoản ở degree cao hơn, hiện đang bị "khóa" phía sau một higher-low (Dec'13) chưa bị phá. Nó **có thể** trở thành draw on liquidity nếu Feb'14 bị phá thật, nhưng **không tự động** là target ngay lập tức — cần kiểm tra xem có pool nào gần hơn chưa được dọn giữa hai mốc.

![[DealingRange-CompetingLows-StructureMap-20260719.svg]]
*Sơ đồ 1: Toàn bộ chuỗi higher-lows từ Nov'13 tới Feb'14, cho thấy Dec'13 low (chưa bị phá) nằm giữa và "khóa" Nov'13 lại phía sau; Feb'14 mới là điểm khởi phát trực tiếp của leg tăng dẫn tới đỉnh hiện tại.*

---

## 1. Đọc lại cấu trúc giá trên chart

| Thời điểm (ước lượng) | Sự kiện | Vai trò |
|---|---|---|
| Cuối Jul – Aug '13 | Tích lũy dao động ~1.30–1.34 | Nền tảng trước khi có displacement rõ |
| ~Oct '13 | Rally lên một đỉnh (~1.362, ước lượng) | Swing high đầu tiên trong chuỗi |
| **~Nov '13** | **Đáy sâu ~1.330** (ước lượng) | SSL — nhưng **chưa từng bị test lại** sau đó |
| Cuối Nov '13 | Rally lên đỉnh cao hơn Oct | Higher-high, xác nhận xu hướng tăng tiếp diễn |
| **~Dec '13** | **Đáy ~1.352** (ước lượng) — **cao hơn đáy Nov'13** | Higher-low — đây là mắt xích quan trọng nhất của toàn bộ phân tích |
| Đầu '14 | Rally lên đỉnh cao hơn nữa | Higher-high tiếp theo |
| **~Feb '14** | **Đáy 1.34792** (giá đã xác nhận từ đường kẻ Khang vẽ) | Higher-low cuối cùng — điểm khởi phát displacement lớn |
| Mar – May '14 | Displacement tăng rất mạnh, gần như một mạch, đỉnh **1.39904** (chạm 2 lần) | Xác lập DR High hiện tại |
| Hiện tại | Sell-off mạnh, giá về **~1.3721–1.37271** | Đang retrace của leg Feb'14→May'14, vừa cắt xuống CE |

Điểm mấu chốt nằm ở dòng Dec '13: **đáy Dec'13 (~1.352) cao hơn đáy Nov'13 (~1.330) và chưa từng bị phá** trong suốt quãng thời gian từ đó tới hiện tại. Đây chính là "mắt xích khóa" quyết định toàn bộ câu trả lời ở mục 3.

---

## 2. Đánh giá lại Dealing Range đã đánh dấu (1.34792 – 1.39904)

Đối chiếu với "Ma trận nhận diện Dealing Range" trong [[12 - Dealing Range]] mục 3:

- **Đầu trên (1.39904):** là high cao nhất toàn chart, được test hai lần gần như đúng giá (Mar và May '14) trước khi có sell-off mạnh — dấu hiệu của một pool BSL dày (equal-highs, theo thang chấm "sức hút ERL" trong [[16 - Internal & External Range Liquidity (IRL & ERL)]] mục nâng cao, hai lần chạm = "double top", sức hút khá cao). Hợp lệ làm DR High.
- **Đầu dưới (1.34792):** là swing low ngay trước cú displacement lớn nhất trên chart — đúng định nghĩa "swing có ý nghĩa, tạo bởi displacement/BOS" theo mục 3 của [[12 - Dealing Range]]. Hợp lệ làm DR Low.
- **Tính thời sự:** cả hai đầu **chưa bị phá** — range vẫn còn hiệu lực, chưa cần re-map theo tiêu chí ở [[37 - Re-mapping Dealing Range sau Displacement]].
- **Vị trí giá hiện tại:** dưới CE ~7–8 pip → vừa lọt discount, xem mục 4.

**Kết luận:** Dealing Range Khang vẽ là đúng. Vấn đề duy nhất cần làm rõ — và cũng là lý do Khang đặt câu hỏi tiếp theo — là **tại sao không dùng đáy Nov'13 sâu hơn** để mở rộng range. Mục 3 trả lời trực tiếp câu này bằng một khung quyết định tái sử dụng được.

---

## 3. Khung quyết định 3 bước — chọn đúng Dealing Range Low khi có nhiều đáy cạnh tranh

Đây là phần mở rộng quan trọng nhất so với lý thuyết đã có trong vault: [[12 - Dealing Range]] đã dạy "chọn swing có ý nghĩa, đừng chọn quá cũ/quá nhỏ", nhưng chưa có một **bài test tuần tự cụ thể** để xử lý tình huống "có 2+ đáy nhìn đều hợp lý". Khung dưới đây lấp khoảng trống đó.

![[DealingRange-CompetingLows-3StepTest-20260719.svg]]
*Sơ đồ 2: So sánh trực tiếp — Nov'13 bị loại vì còn một higher-low (Dec'13) chưa bị phá nằm chắn giữa; Feb'14 được chọn vì không có higher-low nào chưa-bị-phá nằm giữa nó và đỉnh hiện tại.*

### Ba câu hỏi, phải hỏi đúng thứ tự

1. **Đáy này có phải điểm khởi phát MSS gần nhất không?** — Tức là: ngay sau đáy, giá có tạo một đợt displacement phá cấu trúc giảm trước đó và đổi sang tăng không? Cả Nov'13 và Feb'14 đều **pass** bài test này (cả hai đều mở ra một nhịp tăng), nên bước 1 không đủ để phân định — phải đi tiếp bước 2.
2. **Có đáy nào CAO HƠN nằm xen giữa đáy này và giá hiện tại, và đáy cao hơn đó CHƯA bị phá?** Đây là bước quyết định. Với Nov'13: có — đáy Dec'13 (~1.352) nằm giữa và chưa từng bị phá → Nov'13 bị "khóa" lại phía sau một tầng cấu trúc mới, **loại khỏi vai trò range-low hiện tại**. Với Feb'14: không có đáy nào cao hơn chưa-bị-phá nằm giữa nó và đỉnh hiện tại → **pass**, đi tiếp bước 3.
3. **Đáy còn lại (sau khi loại ở bước 2) có phải là đáy gần nhất, chưa mitigate, vừa làm bàn đạp cho leg đang mở rộng tới đỉnh hiện tại không?** Feb'14 pass — đây chính là DR Low hiện tại.

> [!important] Câu ghi nhớ
> **Range low luôn là đáy gần nhất trong chuỗi "higher-low" chưa bị phá, không phải đáy thấp nhất từng nhìn thấy trên màn hình.** Độ sâu của đáy không quan trọng bằng vị trí của nó trong chuỗi cấu trúc. Một đáy có thể "đúng sách" ở bước 1 (có MSS) nhưng vẫn bị loại ở bước 2 nếu nó đã bị khóa sau bởi một higher-low còn nguyên.

### Vai trò của Nov'13 sau khi bị loại: locked swing → pool ở degree cao hơn

Nov'13 không biến mất khỏi bản đồ — nó chuyển vai trò, đúng theo nguyên tắc "tính phân dạng" trong [[16 - Internal & External Range Liquidity (IRL & ERL)]]: cùng một mức giá, ở degree nhỏ (leg hiện tại) nó vô nghĩa vì đã bị khóa; nhưng ở degree lớn hơn (nhìn toàn bộ chuỗi từ Nov'13 tới nay) nó vẫn là một **SSL pool thật, chưa bị dọn**. Đây chính xác là loại tình huống mà [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]] mô tả: một mức thanh khoản có thể đồng thời là "không liên quan" ở khung đang trade và "target hợp lệ ở khung lớn hơn" — hai vai trò không mâu thuẫn, chỉ khác degree.

---

## 4. Premium / Discount / CE — vị trí giá hiện tại trên leg đang active

| Mốc | Giá |
|---|---|
| DR High (May'14) | **1.39904** |
| CE (Equilibrium, 50%) | **≈ 1.37348** |
| Giá hiện tại (đường giá platform) | **~1.37271** |
| DR Low (Feb'14) | **1.34792** |

Giá hiện tại nằm **ngay dưới CE khoảng 7–8 pip** — tức vừa cắt từ Premium (nơi giá vừa reject từ đỉnh 1.399) xuống Discount. Theo nguyên tắc trong [[27 - Premium Discount]] và mục A1 (Quadrant theory) của [[12 - Dealing Range]]: đây mới chỉ là **Discount nông (25–50%)**, chưa phải Deep Discount — vùng này "Long được nhưng cần confluence mạnh", không phải vùng OTE tối ưu. Việc giá cắt CE là một tín hiệu inflection đáng chú ý, nhưng **không phải trigger entry**: cần một PD array cụ thể (FVG/OB) trong discount kèm MSS xác nhận trên khung entry, đúng chuỗi reasoning ở mục 6.

---

## 5. Nov'13 có phải target kế tiếp không? — Đừng nhảy cóc

Đây là điểm Khang hỏi đúng và cần một câu trả lời có sắc thái, không phải "có/không" đơn giản. Theo nguyên tắc "external → internal → external" trong [[16 - Internal & External Range Liquidity (IRL & ERL)]]: draw on liquidity luôn nhắm vào **pool GẦN NHẤT chưa được dọn theo hướng di chuyển**, không nhảy thẳng tới pool xa nhất/sâu nhất nhìn thấy trên chart.

Áp dụng vào case này: nếu Feb'14 (1.34792) bị phá bởi một MSS giảm thật, câu hỏi bắt buộc phải hỏi trước khi kết luận "target là Nov'13" là: **giữa 1.34792 và ~1.330 có còn resting liquidity nào khác không** — ví dụ vùng tích lũy cuối Aug'13 (nếu có equal-lows quanh 1.32–1.34) hoặc bất kỳ đáy nhỏ nào khác chưa được nhắc tới trong buổi phân tích này. Nếu có, đó mới là draw ưu tiên trước; Nov'13 chỉ trở thành target khi các pool gần hơn đã bị dọn hoặc không tồn tại.

> [!question] Câu hỏi Khang cần tự trả lời trên chart thật
> Nhìn kỹ vùng giá giữa 1.34792 và 1.330: có cụm equal-lows hay đáy nhỏ nào khác không? Nếu không, Nov'13 là draw hợp lý kế tiếp. Nếu có, pool đó mới là target gần nhất — đừng bỏ qua nó chỉ vì Nov'13 "nhìn nổi bật hơn" trên chart tổng quan.

---

## 6. Reasoning chain đầy đủ áp dụng vào case này

Theo đúng chuỗi tư duy chuẩn của dự án (HTF bias → dealing range → liquidity → MSS confirmation → PD array entry → target):

| Bước | Trạng thái trong case này |
|---|---|
| **HTF Bias** | Bullish cho leg Feb'14→May'14 (leg đang active) → hiện trong nhịp retrace giảm, vừa cắt CE |
| **Dealing Range** | Feb'14 low (1.34792) – May'14 high (1.39904) — xác nhận đúng bằng khung quyết định 3 bước ở mục 3 |
| **Liquidity** | External hiện tại: BSL tại 1.39904 (đã test 2 lần, dày), SSL tại 1.34792 (chưa bị phá). Pool degree cao hơn: SSL Nov'13 ~1.330, hiện chưa liên quan tới leg đang active |
| **MSS Confirmation** | Chưa có — giá mới cắt CE, chưa xác nhận MSS giảm trên khung entry. Cần theo dõi thêm |
| **PD Array Entry** | Chưa xác định được FVG/OB cụ thể trong discount từ ảnh gốc — cần Khang bổ sung giá/ảnh chi tiết hơn nếu muốn tiến tới một setup thật |
| **Target** | Nếu tiếp tục giảm và phá Feb'14 với MSS thật: kiểm tra pool gần hơn trước, sau đó mới tới Nov'13 (~1.330, cần xác nhận giá) |

---

## 7. Checklist tổng hợp trước khi tin vào kết luận này

- [ ] Xác nhận symbol và khung thời gian chính xác của chart gốc (hiện: chưa xác định).
- [ ] Xác nhận giá chính xác của Nov'13 low và Dec'13 low (hiện: ước lượng bằng mắt từ ảnh).
- [ ] Kiểm tra có pool thanh khoản nào khác nằm giữa Feb'14 (1.34792) và Nov'13 (~1.330) không (mục 5).
- [ ] Theo dõi tiếp: giá có tạo MSS giảm xác nhận trên khung entry sau khi cắt CE không, hay chỉ là một cú nhúng kỹ thuật rồi tiếp tục tăng.
- [ ] Nếu Feb'14 bị phá: xác nhận đó là đóng nến thân dưới 1.34792 kèm MSS, không chỉ là wick xuyên qua.
- [ ] Nếu case "đáy bị khóa bởi higher-low" này lặp lại nhiều lần trong quá trình backtest, cân nhắc bổ sung khung 3 bước ở mục 3 thành một mục con mới trong [[12 - Dealing Range]] (hiện mục 9 "Lỗi thường gặp" có nói tới "chọn range quá cũ" nhưng chưa có bài test tuần tự cụ thể như ở đây).

---

## 8. Câu hỏi cần chốt (chưa xác nhận)

- **Symbol + khung thời gian chính xác** của chart — cần biết để log lại chính xác nếu case này sau này được đối chiếu với dữ liệu thật trong `04 - Backtesting/`.
- **Giá cụ thể** của Nov'13 low và Dec'13 low — hiện chỉ là ước lượng bằng mắt từ ảnh tổng quan, sai số có thể ảnh hưởng tới việc xác định "higher-low chưa bị phá" có thật sự đúng không.
- **Có pool thanh khoản nào khác** giữa Feb'14 và Nov'13 (mục 5) — quyết định target thực tế nếu Feb'14 bị phá.
- **Diễn biến các nến sau khung ảnh hiện tại** — cần biết liệu giá đã tạo MSS giảm xác nhận chưa, hay vẫn đang dao động quanh CE.

## 9. Next steps

- Khi có ảnh gốc rõ nét hơn (đủ trục giá chính xác cho Nov'13/Dec'13) hoặc symbol xác nhận, cập nhật lại frontmatter (`symbol`, `timeframe`, `draw_on_liquidity`) của note này.
- Nếu muốn lưu ảnh chart gốc, thêm file vào `10 - Market Analysis/Attachments/` theo tên gợi ý ở đầu note và embed lại.
- Theo dõi tiếp diễn biến quanh CE (1.37348) — nếu xuất hiện MSS giảm xác nhận trên khung entry kèm FVG/OB hợp lệ trong discount, đây có thể trở thành cơ sở cho một backtest thật trong `04 - Backtesting/` theo [[Backtest template - POI & Step Decision (ICT 2022)|template POI & Step Decision]], cross-link ngược về note này.
- Cân nhắc bổ sung khung quyết định 3 bước ở mục 3 vào concept note [[12 - Dealing Range]] như một mục con mới (ví dụ "9.x — Khi có nhiều đáy/đỉnh cạnh tranh") nếu tình huống này lặp lại trong các case tiếp theo.

---

## Liên kết

- Nền tảng: [[12 - Dealing Range]] · [[27 - Premium Discount]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]] · [[37 - Re-mapping Dealing Range sau Displacement]]
- Liquidity & cấu trúc: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- POI & entry: [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]]
- Model bối cảnh: [[01 - ICT 2022 Model]]
- Case liên quan trong vault: [[2026-07-17 - Re-map Dealing Range Low sau Sweep & Displacement (điều kiện remap, checklist)]]

---
*Ghi chú: date = ngày phân tích (VN, UTC+7). Note phương pháp (methodology) tổng hợp từ ảnh chart Khang gửi trong chat (paste trực tiếp, không phải file upload) — không log backtest vì không vào lệnh, ảnh gốc không nhãn symbol/giá đầy đủ, và các giá trị Nov'13/Dec'13 chỉ là ước lượng bằng mắt. 2 sơ đồ SVG minh họa nguyên lý và tương quan cấu trúc đã thảo luận, không phải chart thật — khi Khang bổ sung ảnh gốc rõ nét + giá chính xác, cập nhật lại các câu hỏi ở mục 8.*
