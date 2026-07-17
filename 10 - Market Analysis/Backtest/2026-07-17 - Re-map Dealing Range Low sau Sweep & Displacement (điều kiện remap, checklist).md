---
type: market-analysis
status: methodology
date: 2026-07-17
symbol: chưa xác định (ảnh chart không có nhãn symbol/giá)
timeframe: chưa xác định (ảnh không nhãn trục thời gian; cấu trúc gợi ý một khung HTF, có thể D1/H4 — cần Khang xác nhận)
session: không rõ (ảnh không nhãn thời gian)
htf_bias: "bearish trong distribution leg → đang xem xét đảo bullish sau sweep + displacement tại 'đường đỏ', chờ xác nhận MSS HTF trước khi kết luận"
setup: "Re-mapping Dealing Range Low sau Liquidity Sweep + Displacement — điều kiện để dời DR Low từ đáy gốc (gray box) lên vị trí đáy mới ('đường đỏ')"
in_trade: false
draw_on_liquidity: chưa xác định (ảnh không nhãn giá cụ thể — xem mục 9 câu hỏi cần chốt)
key_poi: "FVG/OB hình thành trong cây nến displacement ngay sau 'đường đỏ' — ứng viên POI của range mới, cần Khang xác nhận còn unmitigated bằng giá thật"
invalidation: "đóng nến (thân, không chỉ wick) dưới 'đường đỏ' sau khi swing low đã hình thành tại đó — vô hiệu hóa toàn bộ việc remap DR Low lên vị trí này"
topic: "điều kiện & quy trình remap Dealing Range Low sau liquidity sweep + displacement; phân biệt sweep thật vs đáy thấp nhất tình cờ; đồng bộ DR High khi remap; áp dụng khung quyết định Partially vs Fully Consumed; over-remap vs under-remap"
tags:
  - analysis
  - methodology
  - dealing-range
  - remap
  - liquidity-sweep
  - displacement
  - market-structure-shift
  - premium-discount
  - ict-2022
---

# Re-map Dealing Range Low sau Sweep + Displacement — 2026-07-17

> [!info] Trạng thái
> **METHODOLOGY — không vào lệnh.** Note này tổng hợp và đào sâu buổi phân tích một chart (không nhãn symbol/giá/khung thời gian) mà Khang gửi trong chat, xoay quanh câu hỏi cốt lõi: *"Điều kiện gì để tôi re-map Dealing Range Low hiện tại (đáy gốc, khoanh bằng box xám) lên vị trí 'đường kẻ đỏ' mà giá vừa quét rồi displacement mạnh?"* Toàn bộ khung lý thuyết áp dụng ở đây đã có sẵn trong vault tại [[12 - Dealing Range]] và đặc biệt [[37 - Re-mapping Dealing Range sau Displacement]] — note này **không lặp lại** hai bài đó mà **áp dụng trực tiếp** vào case cụ thể trên chart của Khang, đồng thời bổ sung một số góc phân tích sâu hơn (đồng bộ DR High, khung Partially/Fully Consumed, rủi ro over/under-remap) đặt trong đúng bối cảnh của case này.

---
![[DealingRange-RemapCase-20260717-1.png]]
## 0. Tóm tắt tình huống

Chart cho thấy một chuỗi diễn biến khá kinh điển của một nhịp **MMBM (Market Maker Buy Model, xem [[04 - Market Maker Buy Model – MMBM]]) tiếp nối bởi MMSM (xem [[06 - Market Maker Sell Model – MMSM]])**:

1. Một vùng tích lũy (accumulation) ở đáy — khoanh bằng **box màu xám** trên chart, đây là "vùng lệnh" trước khi có displacement lớn.
2. Một cú **displacement tăng mạnh** thoát khỏi box xám, xác lập **DR High gốc** (đường kẻ xám phía trên, nằm ngay trên toàn bộ biên độ dao động sau đó).
3. Sau khi chạm đỉnh, giá bước vào một **distribution leg xuống**: chuỗi lower-highs/lower-lows nối tiếp nhau, đặc trưng của MMSM.
4. Distribution leg kết thúc bằng một cú **quét xuống một mức cụ thể (đường kẻ đỏ)**, ngay sau đó là **một cây nến displacement tăng rất mạnh** đẩy giá bật lên khỏi đường đỏ.

Câu hỏi của Khang: đường đỏ đó có đủ điều kiện để **thay thế vai trò DR Low** (hiện đang là đường kẻ xám phía dưới, đáy của box tích lũy gốc) hay không — và điều kiện cụ thể là gì.

![[DealingRange-Remap-BeforeAfter-20260717.svg]]
*Sơ đồ 1: So sánh Before/After — dùng range CŨ (đáy = box xám gốc) cho ra vị trí premium/discount mập mờ; dùng range MỚI (đáy = đường đỏ, đỉnh = swing high ngay trước leg giảm cuối) cho ra vị trí rõ ràng hơn (discount, khớp với POI vừa hình thành).*

---

## 1. Đọc cấu trúc hiện tại — Range cũ vs điểm remap

| Thành phần trên chart | Vai trò hiện tại (range CŨ) | Vai trò sau remap (range MỚI, nếu đủ điều kiện) |
|---|---|---|
| Box xám (vùng tích lũy đáy) | DR Low gốc — external SSL đã bị lấy từ lâu (đầu chu kỳ) | Không còn liên quan — thuộc về một chu kỳ AMD đã kết thúc |
| Đường kẻ xám trên | DR High gốc | Vẫn có thể là external HTF còn ý nghĩa ở tầng cao hơn (D1/H4) — **không tự động mất hiệu lực**, xem mục 5 |
| Chuỗi lower-highs/lower-lows (distribution) | Đang di chuyển bên trong range CŨ, không tạo range mới | Là "chân đế" hình thành nên range MỚI — cần xác định đúng swing high nào làm DR High mới |
| Đường kẻ đỏ | Một điểm bất kỳ nằm giữa range CŨ | **Ứng viên DR Low MỚI** — chỉ hợp lệ nếu thỏa 6 điều kiện ở mục 3 |
| Cây nến displacement ngay sau đường đỏ | — | Nguồn gốc PD array mới (FVG/OB) — POI ứng viên cho range MỚI |

Đây chính xác là tình huống được mô tả trong [[12 - Dealing Range]] mục "Dealing Range bị vô hiệu (cần vẽ lại) khi": *"Displacement mạnh phá hẳn một đầu range và giữ acceptance bên ngoài"* — nhưng ở đây phức tạp hơn một chút, vì đường đỏ **không phá qua DR Low gốc** (nó nằm cao hơn đáy box xám rất nhiều). Nói cách khác: **đây không phải trường hợp "external range cũ bị lấy"**, mà là trường hợp thứ hai trong bảng "Ba tình huống kích hoạt re-mapping" của [[37 - Re-mapping Dealing Range sau Displacement]]: *"Swing point mới có ý nghĩa hình thành — sau sweep + MSS + displacement, giá tạo đáy/đỉnh mới rõ ràng."* Range CŨ (box xám) không "chết" theo nghĩa bị phá — nó chỉ đơn giản là **không còn phản ánh cấu trúc hiện tại**, vì toàn bộ vai trò của nó (làm bàn đạp cho nhịp tăng ban đầu) đã hoàn thành từ lâu.

> [!important] Phân biệt quan trọng
> Đừng nhầm "DR Low gốc chưa bị phá" với "range gốc vẫn còn hiệu lực để đo premium/discount hôm nay". Một range có thể *chưa bị phá* nhưng vẫn **hết tính thời sự** nếu thị trường đã đi qua nhiều chu kỳ AMD mới bên trong nó. Premium/Discount đo trên range gốc lúc này gần như vô nghĩa vì range đó quá lớn và quá cũ so với distribution leg vừa xảy ra — đây chính là lỗi "chọn range quá cũ" được cảnh báo trong [[12 - Dealing Range]] mục 9 (Lỗi thường gặp).

---

## 2. Vì sao phải xem xét remap (nhắc lại nguyên tắc, áp dụng ngay vào case)

Theo nguyên tắc cốt lõi của [[37 - Re-mapping Dealing Range sau Displacement]]: *"Sau mỗi nhịp displacement lấy external liquidity của range cũ, range cũ đã chết — phải vẽ lại dealing range trên swing mới để đo lại premium/discount, phân loại lại internal/external liquidity và tìm POI tiếp theo."*

Áp dụng vào case này: nếu Khang tiếp tục dùng range CŨ (đáy = box xám) để tính Equilibrium, thì vị trí giá ngay sau cây nến displacement tại đường đỏ sẽ rơi vào đâu đó **giữa range** — không rõ premium hay discount, R:R không đo được, và quan trọng nhất là **POI mới (FVG của cây displacement) sẽ không được nhận diện đúng vai trò**, vì nó không nằm ở "nửa range" nào có ý nghĩa trên bản đồ cũ. Đây đúng là bẫy được cảnh báo: *"OB cũ mitigate, không còn POI — sai ở đâu? POI không biến mất mà đổi dạng."* Ở case này POI không phải "OB cũ mitigate" mà là "đang dùng sai bản đồ nên không thấy vị trí thật của POI mới".

---

## 3. Sáu điều kiện bắt buộc để remap DR Low lên vị trí "đường đỏ"

Đây là phần mở rộng/cụ thể hóa nhất so với buổi trao đổi trước — ghép "Điều kiện bắt buộc" của [[37 - Re-mapping Dealing Range sau Displacement]] mục 3 với "Ma trận nhận diện Dealing Range" của [[12 - Dealing Range]] mục 3, áp dụng đúng vào hình dạng chart này (chuỗi giảm dần rồi sweep + displacement mạnh).

![[DealingRange-Remap-6Dieukien-20260717.svg]]
*Sơ đồ 2: 6 điều kiện đối chiếu trực tiếp lên đúng cấu trúc của case này — chuỗi lower-highs/lower-lows, sweep tại đường đỏ, displacement + MSS, FVG còn nguyên, không có nến phá ngược, và bối cảnh phiên.*

### 3.1 — Phải là Liquidity Sweep thật, không phải "đáy thấp nhất nhìn bằng mắt"

Đường đỏ phải nằm **dưới một pool thanh khoản nhận diện được trước khi giá chạm tới** — một đáy swing rõ ràng của chính distribution leg, một cụm equal lows, hoặc một old low cấp cao hơn. Theo checklist SSL sweep hợp lệ trong [[20 - Liquidity Sweep]] (và được nhắc lại trong case study [[2026-07-13 M15-M5-M1 - Internal Sweep tại CE của H1 FVG (Fractal Liquidity & cơ chế thanh khoản)]]):

1. Chỉ ra được **cụ thể** đáy/cụm equal lows nào đang bị quét — nếu không chỉ tay được vào một mức có tên, mặc định **không phải sweep**, chỉ là điểm thấp nhất tình cờ của một cú giảm liên tục.
2. Giá **thực sự lấy** mức đó (wick hoặc thân vượt qua).
3. **Reject nhanh + reclaim**: đóng nến quay trở lại trên mức vừa lấy — đây chính là hành vi Khang mô tả ("ngay sau khi chạm đường đỏ có nến đẩy giá lên rất dốc").

> [!question] Câu hỏi Khang cần tự trả lời trên chart gốc (có giá thật)
> Ngay bên trái đường đỏ, có một đáy swing rõ ràng hoặc cụm equal lows nào không? Nếu chuỗi giảm chỉ là một dốc liên tục không có đáy nào được test lại (không có equal lows), thì đường đỏ nhiều khả năng chỉ là điểm cực trị của một cú giảm, và cần hạ độ tin cậy của "sweep" xuống — vẫn có thể remap nhưng với ít bằng chứng structural hơn.

### 3.2 — Phải có Displacement + MSS xác nhận ngay sau sweep

Cây nến (hoặc chuỗi nến) đẩy giá lên sau đường đỏ phải đủ mạnh để **phá market structure ngắn hạn** — tức break qua ít nhất một **minor high** được tạo trong chính distribution leg trước đó (không phải break DR High gốc, việc đó thuộc mục 5). Đây là ranh giới sống còn giữa "reaction" và "MSS":

- Nếu cây nến chỉ phản ứng mạnh nhưng **không phá qua bất kỳ swing high nào** của distribution leg → đây mới là reaction, chưa phải MSS. **Chưa remap.**
- Nếu nó phá qua tối thiểu một minor high (như minh họa mục 2 trong sơ đồ 2) → MSS được xác nhận, điều kiện này đạt.

Tham chiếu mistake liên quan nếu bỏ qua bước này: [[06 - Mistake - Not Have Market Structure Shift]].

### 3.3 — Displacement phải để lại FVG/imbalance còn nguyên vẹn (CISD)

FVG tạo ra trong cây displacement là **PD array mới** — Consequent Encroachment ([[10 - Consequent Encroachment (Mean Threshold)]]) của nó sẽ là POI ứng viên cho lần retrace tiếp theo trong range MỚI. Nếu giá sau đó quay lại lấp **hoàn toàn** FVG này mà không phản ứng, tín hiệu MSS coi như bị vô hiệu và đường đỏ mất một phần lý do để làm DR Low mới. Xem thêm [[06 - Mistake - Not Have Market Structure Shift]] và [[10 - Mistake - FVG Not Valid]] cho các trường hợp FVG không đạt chuẩn (quá mỏng, bị lấp gần hết, hình thành từ nến do dự).

### 3.4 — Chưa có nến nào đóng thân dưới đường đỏ sau đó (invalidation)

Đây là điều kiện phủ quyết: nếu sau khi tạo swing low tại đường đỏ, xuất hiện bất kỳ nến nào **đóng thân** (không chỉ wick) bên dưới nó, DR Low mới này bị vô hiệu ngay lập tức — không phải "giảm độ tin cậy", mà là **loại bỏ hoàn toàn**, phải tìm đáy sâu hơn. Điều kiện này cần Khang tự theo dõi tiếp các nến ngoài khung ảnh hiện có.

### 3.5 — DR High phải được đồng bộ, không giữ nguyên đỉnh của range cũ

Đây là điểm hay bị bỏ sót nhất (chi tiết ở mục 4 riêng bên dưới) — remap Low mà không remap High tương ứng sẽ phá vỡ toàn bộ phép tính Equilibrium.

### 3.6 — Bối cảnh Kill Zone / phiên giao dịch phù hợp (điều kiện bổ trợ)

Không bắt buộc tuyệt đối, nhưng một sweep + MSS xảy ra trong London hoặc NY Kill Zone (xem [[18 - Kill Zones]]) có độ tin cậy thống kê cao hơn do đây là khung giờ order flow institutional hoạt động mạnh nhất. Nếu chuỗi sweep này rơi vào phiên Á thanh khoản thấp, nên hạ độ tin cậy của range mới và chờ xác nhận thêm ở phiên kế tiếp trước khi dùng nó làm cơ sở cho một entry thật.

### Bảng tổng hợp — điều kiện nào đã quan sát được từ ảnh, điều kiện nào cần Khang xác nhận thêm

| # | Điều kiện | Quan sát được từ ảnh Khang gửi | Cần xác nhận thêm bằng giá/dữ liệu thật |
|---|---|---|---|
| 1 | Sweep thật (có pool cụ thể bị lấy) | Có một wick/thân chạm xuống đường đỏ trước khi bật lên | Xác định chính xác pool nào bị quét (đáy swing/equal lows cụ thể) |
| 2 | Displacement + MSS | Có một cây nến rất mạnh ngay sau đường đỏ | Xác nhận nó phá qua minor high nào của distribution leg, ghi giá |
| 3 | FVG còn nguyên (CE) | Cây nến đủ lớn để khả năng cao có để lại FVG | Đo chính xác biên FVG (high/low), theo dõi có bị lấp lại không |
| 4 | Không invalidation sau đó | Trong khung ảnh, giá tiếp tục đi lên sau đường đỏ | Theo dõi các nến tiếp theo ngoài khung ảnh hiện tại |
| 5 | DR High đồng bộ | Có thể thấy một vài đỉnh nhỏ trong distribution leg | Chọn đúng swing high làm DR High mới, ghi giá cụ thể (mục 4) |
| 6 | Kill Zone phù hợp | Không xác định — ảnh không nhãn thời gian | Khang xác nhận phiên giao dịch tại thời điểm sweep |

---

## 4. Đồng bộ DR High — không chỉ remap Low

Nguyên tắc từ [[37 - Re-mapping Dealing Range sau Displacement]] mục "5 bước re-map": *"VẼ range mới: chọn swing low mới VÀ swing high mới có ý nghĩa làm hai đầu."* Rất nhiều trader chỉ chăm chăm remap đáy vì đó là nơi "vừa có chuyện xảy ra", rồi vô tình vẫn dùng đỉnh của range CŨ (quá xa, quá cũ) để tính Equilibrium — kết quả là Equilibrium bị kéo lệch lên rất cao, khiến gần như mọi mức giá đều bị đọc thành "discount" một cách giả tạo.

DR High mới hợp lệ trong case này nên là: **swing high gần nhất, chưa bị mitigate, được tạo ra ngay trước leg giảm cuối cùng dẫn tới đường đỏ** (không phải đỉnh tuyệt đối của toàn bộ nhịp tăng ban đầu). Nhìn vào sơ đồ 1 (Before/After): đỉnh này thường là một trong các đỉnh nhỏ (lower-high) gần cuối chuỗi distribution — không phải điểm cao nhất trong toàn bộ ảnh.

> [!tip] Quy tắc chọn nhanh DR High mới
> Hỏi: *"Đỉnh này có phải là điểm mà từ đó displacement giảm cuối cùng bắt nguồn không?"* Nếu đúng → đó là DR High mới. Nếu displacement giảm cuối cùng bắt nguồn từ một đỉnh khác thấp hơn, dùng đỉnh đó — đừng cố kéo DR High lên đỉnh cao nhất của cả nhịp tăng chỉ vì nó "nhìn nổi bật hơn".

Sau khi có cặp Low (đường đỏ) – High (swing mới), Equilibrium mới sẽ **thấp hơn đáng kể** so với Equilibrium của range gốc (vì cả hai đầu đều "co lại" gần vùng giá gần đây hơn nhiều so với box xám ở tận đáy). Điều này có nghĩa: vùng giá ngay sau displacement rất có thể đang ở **discount của range MỚI**, dù nó có thể đang ở premium hoặc equilibrium nếu tính trên range gốc — đây chính xác là lý do việc remap quan trọng, nó thay đổi hoàn toàn kết luận premium/discount cho quyết định entry tiếp theo.

---

## 5. Partially Consumed hay Fully Consumed? — khung quyết định nâng cao

![[DealingRange-Remap-PartialVsFullyConsumed-20260717.svg]]
*Sơ đồ 3: Remap chỉ ở tầng con (H1/M15) trong khi HTF (H4/D1) vẫn nguyên, hay phải cascade remap lên cả tầng cha — quyết định dựa trên "Ba tiêu chí phân định" của [[37 - Re-mapping Dealing Range sau Displacement]].*

Đây là câu hỏi thường bị bỏ qua nhưng lại quyết định quy mô ảnh hưởng của việc remap. Áp dụng "Ba tiêu chí phân định" từ [[37 - Re-mapping Dealing Range sau Displacement]] mục 4 vào case này:

1. **Khoảng cách từ đường đỏ tới external HTF thật (D1 High/D1 Low, PDH/PDL, hay đáy box xám gốc):** nếu đường đỏ chỉ là một internal swing low nằm giữa chừng, còn cách xa đáy box xám gốc một khoảng đáng kể (ước lượng >15–20% biên độ range gốc) → nghiêng về **Partially Consumed** — chỉ cần remap range con (H1/M15), HTF range phía trên vẫn giữ nguyên.
2. **Cấu trúc HTF (H4/D1) có break theo hướng lên không?** Nếu cây displacement chỉ tạo MSS trên khung nhỏ (M15/H1) mà cấu trúc H4/D1 chưa hình thành higher-high mới → vẫn là Partially Consumed. Nếu displacement đủ mạnh để phá luôn cấu trúc H4/D1 → **Fully Consumed**, cần cascade remap lên cả tầng cha, và cân nhắc nghiêm túc khả năng đảo hẳn bias từ bearish sang bullish ở khung lớn.
3. **FVG HTF (H4/D1) phía sau đường đỏ còn unmitigated không?** Nếu còn một FVG lớn ở khung cao hơn chưa bị lấp — nó vẫn là "lực hút ngược" hợp lý, ủng hộ Partially Consumed. Nếu FVG đó đã bị lấp ngay trong nhịp giảm dẫn tới đường đỏ → giảm bớt một điểm tựa cho continuation, nghiêng về Fully Consumed.

> [!warning] Khi ba tiêu chí cho tín hiệu trái chiều
> Nếu không rõ ràng (ví dụ khoảng cách gần external nhưng cấu trúc H4 vẫn chưa break) — mặc định giả định **Partially Consumed nhưng giảm size**: vẫn remap và theo dõi tiếp cùng hướng, nhưng không coi đây là xác nhận đảo bias hoàn toàn, đồng thời theo dõi sát các dấu hiệu đảo ở khung lớn hơn (sweep thất bại, MSS ngược trên LTF).

Không có đủ giá cụ thể từ ảnh hiện tại để kết luận chắc chắn thuộc trường hợp nào — đây là câu hỏi Khang cần tự đối chiếu trên chart thật có đầy đủ trục giá.

---

## 6. Reasoning chain đầy đủ áp dụng vào case này

Theo đúng chuỗi tư duy chuẩn của dự án (HTF bias → dealing range → liquidity → MSS confirmation → PD array entry → target):

| Bước | Trạng thái trong case này |
|---|---|
| **HTF Bias** | Ban đầu bullish (nhịp tăng gốc) → chuyển bearish trong distribution leg → đang xem xét đảo lại bullish *nếu* toàn bộ 6 điều kiện ở mục 3 được xác nhận bằng dữ liệu thật |
| **Dealing Range** | Range CŨ (đáy box xám) hết tính thời sự cho mục đích đo premium/discount hiện tại; range MỚI = [đường đỏ] – [swing high trước leg giảm cuối], còn chờ Khang xác nhận giá cụ thể |
| **Liquidity** | Cần xác định rõ pool nào bị quét tại đường đỏ (đáy swing/equal lows của chính distribution leg) — hiện là "chưa xác định" trong frontmatter, cần điền khi có giá thật |
| **MSS Confirmation** | Cây displacement sau đường đỏ cần được xác nhận phá qua minor high nào của distribution leg — ghi giá cụ thể khi log |
| **PD Array Entry** | FVG/OB hình thành trong cây displacement — POI ứng viên, cần xác nhận còn unmitigated và nằm ở discount của range MỚI |
| **Target** | Draw on liquidity tiếp theo — có thể là external phía trên (DR High mới, hoặc xa hơn là DR High gốc nếu case này là Fully Consumed) — cần Khang xác định bằng giá thật |

---

## 7. Checklist nhanh trước khi tin range mới (đối chiếu mục 9 của [[37 - Re-mapping Dealing Range sau Displacement]])

- [ ] Có displacement thật đã lấy một pool cụ thể tại đường đỏ (không phải chỉ điểm thấp nhất tình cờ).
- [ ] Displacement sau đó phá qua tối thiểu một minor high của distribution leg (MSS xác nhận).
- [ ] Có FVG/OB còn unmitigated do chính cây displacement để lại.
- [ ] Chưa có nến nào đóng thân dưới đường đỏ kể từ khi swing low hình thành.
- [ ] DR High mới đã được chọn lại (không giữ đỉnh của range cũ) và ghi giá cụ thể.
- [ ] Đã áp dụng khung Partially/Fully Consumed (mục 5) để biết có cần cascade remap lên H4/D1 hay không.
- [ ] HTF bias & draw on liquidity chính (nếu còn hiệu lực) không mâu thuẫn với việc remap này.

Nếu bất kỳ mục nào chưa xác nhận được — chưa nên coi range mới là cơ sở cho một entry thật, dù có thể tiếp tục theo dõi như một giả thuyết đang chờ xác nhận thêm.

---

## 8. Rủi ro hai đầu áp dụng vào case này: Over-remap vs Under-remap

| Thất bại | Biểu hiện nếu áp dụng sai vào case này | Cách tự kiểm tra |
|---|---|---|
| **Over-remap** | Vẽ lại range ngay khi thấy một nến xanh lớn bất kỳ trong distribution leg, chưa chờ xác nhận MSS thật — dễ nhầm một cú hồi kỹ thuật (pullback) trong xu hướng giảm với một điểm đảo chiều thật | Hỏi: "Cây nến vừa rồi có phá qua một minor high cụ thể không, có để lại FVG không?" Nếu không cả hai → chưa đủ điều kiện, đây vẫn là range CŨ |
| **Under-remap** | Bám mãi vào range CŨ (đáy box xám) dù đường đỏ đã cho đủ bằng chứng sweep + MSS + FVG — tiếp tục đo premium/discount trên một range đã hết tính thời sự, dẫn tới bỏ lỡ toàn bộ chuỗi lệnh tiếp theo nếu giả thuyết bullish mới là đúng | Hỏi: "Nếu tôi bỏ qua chuyện gì đã xảy ra trước đó và chỉ nhìn vào phần chart gần nhất, tôi có tự nhiên chọn đường đỏ làm đáy tham chiếu không?" Nếu có → nên remap |

---

## 9. Câu hỏi cần chốt (chưa xác nhận)

- **Symbol + khung thời gian chính xác** của chart — ảnh gốc không nhãn, cần biết để log vào `04 - Backtesting/` nếu case này về sau được test thật hoặc quan sát thành một trade.
- **Giá cụ thể** của: đường đỏ (DR Low mới), swing high được chọn làm DR High mới, biên FVG (high/low) của cây displacement, và minor high bị phá bởi MSS.
- **Pool thanh khoản cụ thể bị quét tại đường đỏ** — đáy swing nào, hay cụm equal lows nào? Cần chỉ tay được vào một mức có tên (mục 3.1).
- **Kết quả áp dụng khung Partially vs Fully Consumed** (mục 5) — cần giá thật của external HTF (D1/H4 high/low hoặc đáy box xám gốc) để so khoảng cách.
- **Phiên/Kill Zone** tại thời điểm sweep — ảnh không nhãn thời gian nên chưa thể đánh giá điều kiện 3.6.
- **Diễn biến các nến sau khung ảnh hiện tại** — cần biết liệu có nến nào đã đóng thân dưới đường đỏ hay chưa (điều kiện invalidation, mục 3.4).

## 10. Next steps

- Khi có ảnh gốc + giá cụ thể, cập nhật lại note này (điền đầy đủ frontmatter `symbol`, `timeframe`, `draw_on_liquidity`, `key_poi`) hoặc tạo một file backtest chi tiết trong `04 - Backtesting/` theo [[Backtest template - POI & Step Decision (ICT 2022)|template POI & Step Decision]] nếu case này thực sự dẫn tới một entry, cross-link ngược về note này.
- Nếu tình huống "sweep một internal low rồi displacement mạnh, nhưng đáy đó không phá external range gốc" lặp lại nhiều lần trong quá trình backtest, cân nhắc viết thành một mục riêng bổ sung vào [[37 - Re-mapping Dealing Range sau Displacement]] (case "swing point mới hình thành" — hiện bài đó mới có ví dụ cho trường hợp "external bị lấy", chưa có ví dụ chi tiết cho trường hợp "internal swing mới, external gốc chưa chạm tới").
- Theo dõi tiếp các nến ngoài khung ảnh hiện tại để trả lời điều kiện invalidation (mục 3.4) trước khi coi range mới là đáng tin cậy.

---

## Liên kết

- Nền tảng: [[12 - Dealing Range]] · [[37 - Re-mapping Dealing Range sau Displacement]] · [[27 - Premium Discount]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- Liquidity & cấu trúc: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- POI & entry: [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]] · [[35 - Aggressive Displacement Entry]]
- Model bối cảnh: [[01 - ICT 2022 Model]] · [[04 - Market Maker Buy Model – MMBM]] · [[06 - Market Maker Sell Model – MMSM]]
- Timing: [[18 - Kill Zones]]
- Case liên quan trong vault: [[2026-07-13 M15-M5-M1 - Internal Sweep tại CE của H1 FVG (Fractal Liquidity & cơ chế thanh khoản)]] · [[2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)]]
- Mistakes cần tránh: [[06 - Mistake - Not Have Market Structure Shift]] · [[10 - Mistake - FVG Not Valid]] · [[03 - Mistake - Entry When MSS not in POI Zone]] · [[08 - Mistake - Weak Displacement]]

---
*Ghi chú: date = ngày phân tích (VN, UTC+7). Note phương pháp (methodology) tổng hợp từ ảnh chart Khang gửi trong chat — không log backtest vì không vào lệnh và ảnh gốc không nhãn giá/symbol. 3 sơ đồ SVG minh họa nguyên lý, không phải chart thật. Khi Khang bổ sung ảnh gốc + giá cụ thể, cập nhật lại các câu hỏi ở mục 9.*
