---
type: ict-concept
concept: Aggressive Displacement Entry
aliases:
  - Aggressive Displacement
  - Shallow Retrace Entry
  - Entry Refinement on Strong Displacement
tags:
  - trading/ict/concept
  - trading/study
  - "#AggressiveDisplacement"
status: developing
category: Entry Model
timeframes:
  - M5
  - M1
models:
  - "[[ICT 2022 Model]]"
markets:
  - NDX/NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 4
confidence: 2
last_reviewed: 2026-06-29
created: 2026-06-29
updated: 2026-07-03
related_concepts:
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[17 - Inverse Fair Value Gap - iFVG]]"
  - "[[25 - OB - Order Block]]"
  - "[[26 - OTE - Optimal Trade Entry]]"
prerequisites:
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[13 - FVG  - Fair Value Gap]]"
common_mistakes: []
---

# Aggressive Displacement Entry

> [!summary] Tóm tắt 1 câu
> Khi giá quét liquidity → tạo MSS → **displacement rất mạnh**, giá thường KHÔNG retrace sâu về FVG đầu tiên/to nhất; entry thật nằm **cao hơn và phải refine ở khung nhỏ hơn (CE, M1 FVG/OB)** — displacement càng mạnh thì retrace càng nông.

> [!important] Nguyên tắc cốt lõi
> Displacement mạnh = institutional sponsorship lớn = smart money KHÔNG cho giá rẻ lại. Đây là **efficient delivery**, không phải lỗi của mình. Phản xạ chờ fill sâu vào FVG thấp/to là lý do bỏ lỡ lệnh. Vùng entry hợp lý nằm cao hơn mình nghĩ: **CE của FVG**, hoặc một **FVG/OB nhỏ hơn ở M1** trong leg retrace nông.

---

## 1. Định nghĩa

**Khái niệm:**
Aggressive Displacement Entry là cách tìm điểm vào lệnh khi sau chuỗi **liquidity sweep → MSS → displacement**, cú đẩy giá có lực bất thường (body lớn liên tiếp, ít/không có pullback) và giá **chỉ retrace rất nông** rồi tiếp tục đi về phía draw on liquidity — thay vì quay lại lấp đầy FVG đầu tiên mà trader đánh dấu.

**Mục đích trong ICT:**
- Giải quyết tình huống "FVG không được chạm" — một trong những lý do bỏ lỡ lệnh phổ biến nhất sau khi đọc đúng narrative.
- Chuyển từ tư duy "chờ fill sâu" sang tư duy "**refine entry ở khung nhỏ hơn + dùng CE**".
- Giữ kỷ luật R:R: entry nông hợp lý vẫn tốt hơn chase ở giá xấu.

**Vì sao khái niệm này quan trọng:**
Đọc đúng bias, đúng sweep, đúng MSS — nhưng vẫn lỗ cơ hội vì đặt limit ở FVG quá thấp. Bản thân việc giá không retrace sâu là **một tín hiệu** (move hiệu quả, có sponsorship), không phải tín hiệu nên bỏ. Hiểu điều này giúp định vị entry đúng nơi smart money thực sự cho phép vào.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Vì sao FVG mình đánh dấu không được giá quay về?
- Trong move mạnh, vùng retrace tối đa thực tế là tới đâu?
- Nên hạ khung nào để tìm entry refine?
- Nếu đã lỡ lệnh thì chờ cấu trúc tiếp theo ở đâu, thay vì đuổi giá?

### Aggressive Displacement Entry không phải là gì
- Không phải lý do để **chase** entry market ngay tại đỉnh leg.
- Không phải phủ định FVG — mà là chọn **FVG/PD array đúng vị trí** (cao hơn, nhỏ hơn).
- Không phải bỏ stop logic — stop vẫn dưới swing/điểm sweep gần nhất.
- Không phải mọi displacement đều "aggressive" — chỉ áp dụng khi lực đẩy thật sự mạnh và retrace nông.

### Cơ sở Order Flow / Auction Market

![[AggressiveDisplacement-Anatomy-Comparison.png]]
*Chú thích: đây là sơ đồ minh hoạ/khái niệm (KHÔNG phải chart thật) — hãy vẽ lại hoặc dán ảnh chụp có chú thích thật của bạn. Bố cục gợi ý: bên trái vẽ một move "retrace bình thường" quay đầy đủ về đáy FVG; bên phải vẽ một move "aggressive displacement" với chuỗi nến thân lớn liên tiếp, retrace chỉ chạm CE rồi tiếp tục đi — dùng cùng một trục giá để đối chiếu trực quan độ nông/sâu của hai kiểu retrace.*

**Vì sao displacement mạnh tạo ra retrace nông — nhìn qua lăng kính order flow:**

Theo lý thuyết thị trường đấu giá (Auction Market Theory), mỗi mức giá chỉ "được xác nhận" là hợp lý khi có đủ hai bên đồng ý giao dịch tại đó (thể hiện qua khối lượng khớp lệnh). Một displacement aggressive là hệ quả của sự **mất cân bằng thanh khoản nghỉ (resting liquidity)** giữa hai phía order book:

- **Lệnh thị trường (market orders) áp đảo một chiều:** khi sweep xảy ra và MSS xác nhận, dòng lệnh market mua/bán dồn dập theo một hướng, "ăn" hết các lệnh giới hạn (limit orders) đang chờ ở phía đối diện (offers khi tăng, bids khi giảm) qua nhiều mức giá liên tiếp mà không có đủ thanh khoản đối ứng để hấp thụ hết lực đẩy — dẫn tới các nến thân lớn, ít wick đối nghịch.
- **Delivery giá "một chiều" và không hiệu quả (inefficient one-sided delivery):** vì lệnh limit hai chiều không đủ dày ở các mức trung gian, giá "nhảy" qua các vùng đó để lại FVG/imbalance — đây chính là dấu hiệu thị trường **chấp nhận một mức chiết khấu (discount) hoặc premium lớn hơn bình thường** chỉ trong một nhịp, thay vì thương lượng dần từng bước như trong một move "bình thường".
- **Hệ quả cho retrace:** vì phần lớn thanh khoản giới hạn hai chiều đã bị quét sạch trong chính cú displacement, không còn nhiều lệnh chờ "kéo" giá quay lại sâu vào vùng FVG gốc. Giá chỉ cần lùi về **CE** — nơi đại diện cho "giá trị hợp lý trung bình" của cú đẩy — là đã đủ để bên tổ chức tiếp tục nhiệm vụ chính: dẫn giá về draw on liquidity. Đây là lý do tại sao "chờ fill sâu" thường vô nghĩa trong bối cảnh này.

> [!info] Diễn giải ngắn gọn
> Retrace nông không phải "may mắn" — nó là hệ quả trực tiếp của việc thanh khoản đối ứng đã bị tiêu thụ gần hết ngay trong cú displacement. Thị trường không cần trả giá về vùng cũ vì không còn nhiều ai chờ giao dịch ở đó.

---

## 2. Bối cảnh sử dụng

### Khi nào khái niệm này có giá trị cao?
- [ ] Đã có **SSL/BSL sweep + MSS** đúng sequence, cùng Daily Bias.
- [ ] Displacement leg gồm nhiều nến body lớn liên tiếp, **ít pullback nội bộ**.
- [ ] Giá retrace **rất nông** (không chạm FVG to/thấp nhất) rồi tiếp tục đi tiếp.
- [ ] Vẫn còn draw on liquidity rõ ràng phía trước → còn room cho R:R.
- [ ] Đang trong kill zone / cửa sổ có edge.

### Khi nào nên bỏ qua?
- [ ] Displacement yếu / nến chồng lấp nhiều → đây là move bình thường, cứ chờ FVG fill như thường.
- [ ] Giá đã chạy gần hết tới target, room còn lại quá ít.
- [ ] Không xác định được FVG/OB nào ở M1 để refine → entry trở thành đoán.
- [ ] Sweep/MSS chưa rõ ràng — đừng dùng concept này để hợp lý hóa việc chase.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Displacement mạnh bất thường:** chuỗi body lớn, momentum dốc, gap/imbalance liên tiếp.
2. **Retrace nông:** pullback không chạm FVG đầu tiên (thường là FVG to/thấp nhất), thường dừng ở mép trên hoặc CE của một FVG cao hơn.
3. **Tiếp tục mở rộng:** sau retrace nông, giá đi tiếp về phía draw on liquidity, để lại FVG mới ở khung nhỏ.

### Điều kiện bắt buộc
- [ ] Có sweep + MSS hợp lệ trước displacement (xem [[21 - Market Structure Shift]], [[20 - Liquidity Sweep]]).
- [ ] Displacement có chất lượng "aggressive" (body close mạnh, urgency, ít hồi).
- [ ] Xác định được một PD array hợp lệ ở vị trí retrace nông (CE của FVG M5, hoặc FVG/OB M1).

### Điều kiện tăng xác suất
- [ ] M1 cho thấy một micro sweep + micro MSS ngay tại vùng retrace nông (cùng câu chuyện, phóng to).
- [ ] Vùng entry trùng với **CE (50%)** của FVG M5 — xem [[10 - Consequent Encroachment (Mean Threshold)]].
- [ ] Còn external liquidity rõ ràng phía trước cho R:R tốt.

### Điều kiện làm setup yếu đi
- Displacement thực ra yếu (nến nhỏ, chồng lấp) → không phải tình huống aggressive.
- Không có FVG/OB nào ở M1 để bấu víu → entry thiếu logic.
- Giá đã đi quá xa, retrace nông vẫn cho R:R kém.

### Sắc thái theo từng thị trường (NQ1/NDX vs EURUSD/GBPUSD vs XAUUSD)

![[AggressiveDisplacement-Recognition.png]]
*Chú thích: sơ đồ minh hoạ/khái niệm (KHÔNG phải chart thật) — hãy thay bằng ảnh chụp thật của bạn. Gợi ý bố cục: một chart annotated với 3-4 nến thân lớn liên tiếp được khoanh vùng, ghi chú "body ≥ X × ATR", đường CE kẻ ngang đậm tại 50% của FVG lớn, và một mũi tên nhỏ đánh dấu điểm retrace nông dừng lại đúng tại CE — kèm ô chú thích "micro sweep + micro MSS tại đây" nếu có.*

"Aggressive" không có một ngưỡng cố định — nó phụ thuộc vào đặc tính biến động và cấu trúc phiên của từng thị trường. Dưới đây là kim chỉ nam thực chiến cho 4 thị trường trong phạm vi giao dịch:

| Thị trường | Bối cảnh sinh displacement mạnh | Ngưỡng gợi ý để gọi là "aggressive" | Lưu ý thực chiến |
|---|---|---|---|
| **NQ1 / NDX (NAS100)** | Spike do thuật toán/tin tức trong Kill Zone London/NY, phá cấu trúc quanh mở cửa RTH | Thân nến (body) **≥ 1.5× ATR(14) trên M5**; chuỗi ≥2-3 nến cùng hướng, wick đối nghịch rất nhỏ | Biến động cao, dễ có nến "outlier" do thanh khoản mỏng — luôn đối chiếu với volume/tick nếu có; retrace thường nông nhất trong 3 thị trường vì tốc độ thuật toán cao |
| **EURUSD / GBPUSD** | Momentum bùng nổ theo phiên, đặc biệt quanh **London Open** hoặc tin vĩ mô (NFP, CPI, lãi suất) | Thân nến **≥ 1.2–1.3× ATR(14) trên M5**; đủ để vượt trội rõ rệt so với biến động trung bình phiên Á trước đó | Move mạnh ở FX chính thường "sạch" hơn (ít nhiễu) nhưng biên độ tuyệt đối nhỏ hơn NQ1 — cần nhìn tương quan ATR chứ không nhìn số pip tuyệt đối |
| **XAUUSD (Gold)** | Spike quanh CPI/NFP/FOMC hoặc risk-off/risk-on đột ngột; average true range/ngày vốn đã lớn hơn nhiều so với FX | Thân nến **≥ 1.5–2× ATR(14) trên M5** vì range nền đã rộng — ngưỡng thấp hơn dễ nhầm biến động thường ngày với "aggressive" thật | Spread giãn mạnh quanh tin; chờ nến đóng cửa ổn định trước khi tin vào retrace nông là thật, tránh nhầm spike thanh khoản mỏng với displacement có sponsorship thật |

> [!warning] Ngưỡng ATR chỉ là điểm khởi đầu, không phải luật cứng
> Các hệ số ATR trên là gợi ý để bắt đầu backtest cá nhân — hãy tự đo lại trên dữ liệu thật của từng thị trường/khung giờ bạn giao dịch và điều chỉnh. Đừng áp dụng máy móc một con số cho mọi phiên hay mọi giai đoạn biến động.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình refine khi displacement quá mạnh
> 1. **Move này có thực sự aggressive không?** (body lớn liên tiếp, retrace nông)
> 2. **CE của FVG M5 ở đâu?** — đặt đó làm vùng entry kỳ vọng thay vì đáy FVG.
> 3. **Hạ M1 tại leg retrace** — có FVG/OB nhỏ hơn nằm cao hơn không?
> 4. **Còn room tới draw on liquidity không?** Nếu không → bỏ.

### D1 / H4 — Bias & Narrative
- Xác nhận Daily Bias và draw on liquidity (move mạnh thường đang chạy về một external pool HTF).
- Move aggressive thường đồng pha với HTF bias — đó là lý do nó mạnh.

### H1 / M15 — POI & Context
- Đánh dấu FVG/OB M5 sinh ra từ displacement leg.
- Tính sẵn **CE (mức 50%)** của FVG đó — đây là vùng retrace tối đa kỳ vọng trong move mạnh.

### M5 / M1 — Confirmation & Entry
- **Hạ M1** ngay tại leg retrace nông: tìm FVG hoặc Order Block nhỏ hơn, nằm **cao hơn** so với FVG M5 to.
- Lý tưởng: M1 tạo một micro sweep + micro MSS tại vùng đó → xác nhận entry.
- Đặt limit tại **CE của FVG M5** hoặc tại M1 FVG/OB; stop dưới swing/điểm sweep gần nhất.
- Nếu giá không chạm CE → move quá mạnh, **không đuổi**, chờ leg tiếp theo.

### Trường hợp không có M1 PD Array & tương tác với CE / iFVG

![[AggressiveDisplacement-MTF-Refine-Flow.png]]
*Chú thích: sơ đồ flow từng bước (KHÔNG phải chart thật) — hãy thay bằng lưu đồ/ảnh chụp thật của bạn. Gợi ý bố cục dạng flowchart dọc: Khối 1 "Xác nhận displacement aggressive" → Khối 2 "Tính CE của FVG M5" → Khối 3 rẽ nhánh "Có M1 FVG/OB trong leg retrace?" → nhánh YES dẫn tới "Refine entry tại M1 PD array + micro MSS", nhánh NO dẫn tới khối quyết định ở phần mô tả bên dưới (chờ leg tiếp theo / chấp nhận FVG sâu hơn) → khối cuối "Entry hoặc No-trade".*

Có những leg retrace nông đến mức **không để lại bất kỳ FVG hay Order Block nào ở M1** — toàn bộ cú hồi chỉ là 1-2 nến nhỏ không tạo imbalance rõ ràng. Đây là tình huống dễ khiến trader "đoán mò" một vùng entry không có cơ sở. Cây quyết định xử lý:

1. **Kiểm tra lại CE của FVG M5 trước tiên.** Nếu giá đã chạm hoặc đi vào vùng lân cận CE mà không có M1 PD array, CE vẫn có thể dùng làm vùng entry độc lập (không bắt buộc phải có xác nhận M1) — miễn là đã có sweep + MSS hợp lệ trước đó. Đây là lựa chọn ưu tiên nếu CE nằm ở vị trí hợp lý về R:R.
2. **Nếu giá còn cách CE khá xa và không có M1 PD array:** đừng vào lệnh dựa trên "cảm giác" — hai lựa chọn hợp lệ:
   - **(a) Chờ leg tiếp theo:** đứng ngoài, để giá tiếp tục di chuyển; một leg đẩy mới thường sẽ để lại một FVG/OB mới rõ ràng hơn để refine. Đây là lựa chọn kỷ luật mặc định khi không chắc chắn.
   - **(b) Chấp nhận một FVG sâu hơn nhưng vẫn hợp lệ:** nếu có một FVG ở khung M5 (không phải M1) nằm gần CE và vẫn còn "trẻ" (chưa bị lấp một phần đáng kể), có thể dùng FVG đó thay vì cố tìm một PD array M1 không tồn tại — miễn là entry vẫn nằm **trên/dưới CE theo đúng hướng an toàn hơn** (tức không sâu hơn đáy FVG M5 gốc) và R:R vẫn đạt tối thiểu theo kế hoạch.
   - **Không hợp lệ:** tự vẽ một "FVG" giả hoặc dùng một mức giá bất kỳ chỉ vì "nhìn có vẻ đẹp" — đây là hành vi đoán, không phải phân tích.

**Tương tác với [[10 - Consequent Encroachment (Mean Threshold)]]:**
CE là ngưỡng entry kỳ vọng tối thiểu trong toàn bộ concept này. Khi không có M1 PD array, CE trở thành **tuyến phòng thủ chính** — nếu giá không chạm được cả CE, đó là bằng chứng move quá mạnh để tham gia bằng limit order, và quy tắc "không đuổi" áp dụng nghiêm ngặt.

**Tương tác với [[17 - Inverse Fair Value Gap - iFVG]]:**
Có một tình huống nâng cao đáng chú ý: nếu giá **chạm CE nhưng sau đó đóng nến xuyên ngược qua CE** (tức thất bại giữ vùng entry kỳ vọng) và tiếp tục đóng cửa ở phía "sai" của FVG M5 gốc, bản thân FVG đó có thể **đảo vai trò**:
- Nếu giá không chỉ chạm CE mà còn đóng cửa xuyên qua **toàn bộ FVG** theo hướng ngược lại với bias ban đầu, FVG gốc (vốn được kỳ vọng là vùng nâng đỡ/kháng cự) có thể **flip thành iFVG** — nghĩa là vùng đó bây giờ đóng vai trò ngược lại (kháng cự nếu trước đó là hỗ trợ, và ngược lại).
- Về logic quyết định: (1) nếu chỉ chạm/xuyên nhẹ CE rồi bật lại đúng hướng ban đầu → vẫn là retrace nông hợp lệ, cứ theo kế hoạch entry gốc; (2) nếu đóng cửa dứt khoát xuyên qua toàn bộ FVG và giữ giá ở phía đối diện → coi setup gốc **đã bị vô hiệu hóa (invalidated)**, và đánh giá lại toàn bộ FVG đó như một iFVG/breaker tiềm năng cho hướng ngược lại — cần một MSS mới theo hướng ngược để xác nhận, không tự động đảo lệnh chỉ vì giá xuyên qua.
- Không nhầm lẫn "test CE rồi tiếp diễn" (bình thường, dự kiến được) với "đóng cửa xuyên hẳn FVG" (invalidation thật) — ranh giới là **acceptance** (đóng nến ổn định phía bên kia), không phải một wick xuyên qua tạm thời.

> [!warning] Đừng tự động đảo lệnh khi CE thất bại
> CE thất bại không tự động nghĩa là "vào lệnh ngược". Nó nghĩa là **thoát khỏi setup gốc** và chờ cấu trúc mới (MSS ngược hướng) xác nhận trước khi coi vùng đó là iFVG/breaker khả dụng.

```text
Mẫu ghi nhanh — Aggressive Displacement (Long)
Bias: Bullish | Draw on liquidity: BSL [level]
Sweep SSL [đáy] → MSS phá lower-high → displacement mạnh
FVG M5 (to/thấp): [zone]  → CE (50%): [level]  ← vùng entry kỳ vọng
Retrace nông dừng tại: [level] (chưa chạm đáy FVG M5)
M1 refine: FVG/OB tại [zone cao hơn] + micro MSS xác nhận
Entry: CE FVG M5 / M1 FVG  | Stop: dưới swing gần nhất | Target: BSL [level]
No-trade: displacement yếu / hết room / không có M1 PD array
```

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Entry được xem là hợp lệ khi
- [ ] Có sweep + MSS + displacement aggressive đúng sequence.
- [ ] Entry đặt tại **CE FVG M5** hoặc **M1 FVG/OB** nằm trong leg retrace nông.
- [ ] Có stop logic (dưới swing/điểm sweep) và còn room tới target.

### Setup bị vô hiệu khi
- [ ] Giá đóng acceptance ngược lại qua MSS level → failed shift, không phải retrace.
- [ ] Displacement hóa ra yếu / giá lấp đầy ngược trở lại sâu hơn cả FVG M5.
- [ ] Không có PD array M1 nào để vào → đứng ngoài thay vì đoán.

---

## 6. Ví dụ chart

### Ví dụ đúng — SSL sweep → MSS → displacement mạnh, retrace nông
![[AggressiveDisplacement-Example-Correct-ShallowRetrace.png]]

**Mô tả:**
Giá quét SSL (đáy, blue line), tạo MSS phá lower-high bằng displacement rất mạnh. FVG M5 to/thấp được đánh dấu nhưng giá **không quay về** — chỉ retrace nông tới CE của một FVG cao hơn rồi tiếp tục mở rộng lên. Entry hợp lý là CE FVG M5 / M1 FVG, không phải đáy FVG to.

**Vì sao đây là ví dụ tốt:**
- Move hiệu quả có sponsorship → retrace nông là điều dự kiến được.
- Entry refine ở M1/CE cho stop chặt và R:R tốt hơn chờ fill sâu.
- Không chase tại đỉnh leg.

### Ví dụ sai / dễ nhầm — chờ fill sâu vào FVG to nhất
![[AggressiveDisplacement-Example-Wrong-WaitedFullFVG.png]]

**Mô tả lỗi:**
Đặt limit ở đáy FVG to/thấp nhất ngay sau MSS. Giá chỉ retrace nông rồi đi tiếp → limit không bao giờ được khớp → bỏ lỡ một move đúng narrative. Sau đó FOMO chase ở giá xấu.

**Bài học:**
- FVG to/thấp = entry "an toàn" về cảm giác nhưng thường không được chạm trong move mạnh.
- Displacement càng mạnh → entry càng phải cao hơn và refine khung nhỏ hơn.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[13 - FVG  - Fair Value Gap]]
- [[10 - Consequent Encroachment (Mean Threshold)]]
- [[17 - Inverse Fair Value Gap - iFVG]]
- [[25 - OB - Order Block]]
- [[26 - OTE - Optimal Trade Entry]]

### Sequence mẫu
```text
HTF Bias → Sweep (SSL/BSL) → MSS → Displacement MẠNH
→ Retrace NÔNG (không chạm FVG to)
→ Refine: CE của FVG M5  HOẶC  hạ M1 tìm FVG/OB + micro MSS
→ Entry tại CE / M1 PD array → Stop dưới swing → Target: draw on liquidity
→ Nếu không chạm CE: KHÔNG đuổi, chờ leg tiếp theo
```

---

## 8. Best Practices

> [!tip] Pre-plan khả năng displacement aggressive TRƯỚC khi nó xảy ra
> Trader chuyên nghiệp không đợi thấy displacement mạnh rồi mới nghĩ cách xử lý — họ chuẩn bị sẵn **hai kịch bản entry** ngay từ lúc đánh dấu POI, trước khi biết move sẽ mạnh hay yếu:
> - **Kịch bản A (di sản/mặc định):** limit tại đáy FVG M5 nếu displacement chỉ ở mức bình thường.
> - **Kịch bản B (contingency cho aggressive):** limit dự phòng tại **CE của FVG M5**, cộng kế hoạch hạ M1 để tìm FVG/OB refine nếu retrace nông hơn dự kiến.
> Việc chuẩn bị sẵn cả hai giúp loại bỏ độ trễ ra quyết định — khi retrace thực sự nông, trader không mất thời gian "nghĩ lại từ đầu" mà chuyển thẳng sang kịch bản B đã lên sẵn.

**Bảng pre-plan trước khi displacement xảy ra:**

| Bước chuẩn bị | Nội dung | Thời điểm thực hiện |
|---|---|---|
| 1. Đánh dấu FVG M5 gốc | Xác định range đầy đủ ngay khi displacement leg hình thành | Ngay sau khi MSS được xác nhận |
| 2. Tính sẵn CE | Tính CE (50%) của FVG M5 làm limit dự phòng | Cùng lúc với bước 1, không chờ retrace xảy ra |
| 3. Xác định vùng "quan sát M1" | Khoanh vùng giá (giữa đỉnh leg và CE) sẽ hạ M1 nếu retrace nông | Trước khi giá bắt đầu retrace |
| 4. Đặt ngưỡng "aggressive" cá nhân | Dùng bảng ATR theo thị trường (xem mục 3) để biết khi nào chuyển sang kịch bản B | Trong giai đoạn phân tích HTF, trước phiên |
| 5. Quyết định trước "điểm bỏ cuộc" | Xác định trước: nếu giá không chạm cả CE thì bỏ, không đuổi | Trước khi vào lệnh, không phải lúc đang hồi hộp chờ fill |

**Position-management nuance — entry nông thay đổi bài toán R:R và size như thế nào:**

Vì entry tại CE/M1 PD array nằm **cao hơn (gần đỉnh leg hơn)** so với entry tại đáy FVG M5, khoảng cách từ entry tới stop (dưới swing/điểm sweep) **ngắn hơn** so với kịch bản chờ fill sâu. Điều này có hệ quả trực tiếp lên quản lý vị thế — xem thêm cách tính pip/lot/margin cụ thể tại [[36 - Forex CFD Basics ( Pip, Lot, Spread, Swap, Leverage, Margin )]]:

| Yếu tố | Entry tại đáy FVG (giả định, thường KHÔNG khớp trong move aggressive) | Entry tại CE / M1 refine (thực tế trong move aggressive) |
|---|---|---|
| Khoảng cách entry → stop | Rộng hơn (entry thấp, stop vẫn ở cùng một mức dưới swing) | **Hẹp hơn** (entry cao hơn, cùng mức stop) |
| R:R tại cùng một target | Thấp hơn (mẫu số R rộng hơn) | **Cao hơn** (mẫu số R hẹp hơn, cùng khoảng cách tới target) |
| Position size ở cùng mức rủi ro ≤0.5% | Size nhỏ hơn (SL rộng hơn tính theo pip/point) | **Size có thể lớn hơn** một chút cho cùng mức rủi ro tiền tệ, vì SL tính theo pip/point hẹp hơn — nhưng vẫn phải tuân thủ trần rủi ro ≤0.5%/lệnh, không "tận dụng" SL hẹp để tăng risk% |
| Độ nhạy với slippage | Thấp hơn tương đối (biên rộng hơn) | Cao hơn tương đối — SL hẹp hơn dễ bị ảnh hưởng bởi spread/slippage, đặc biệt trên XAUUSD hoặc quanh tin |

> [!warning] SL hẹp hơn không có nghĩa là "risk tự do tăng size"
> Nhiều trader nhầm lẫn: vì SL (tính theo pip) hẹp hơn khi entry ở CE/M1, họ tăng size để "risk vẫn ra cùng số tiền nhưng khối lượng lớn hơn". Điều này đúng về mặt toán học miễn là **vẫn tuân thủ đúng ≤0.5% vốn/lệnh** — tuyệt đối không tăng risk% chỉ vì SL hẹp hơn, và luôn cộng thêm biên an toàn cho spread/slippage khi tính size trên SL hẹp.

**Checklist backtest dành riêng cho Aggressive Displacement Entry:**

| Trường log | Mô tả |
|---|---|
| Tỉ lệ body/range của nến displacement | Đo body-to-range ratio của (các) nến displacement chính — dùng để định lượng "mức độ aggressive" thay vì đánh giá cảm tính |
| Độ sâu retrace (%) | Retrace dừng lại ở bao nhiêu % của FVG M5 (0% = không hồi, 50% = đúng CE, 100% = lấp hết) |
| CE hay M1 array được dùng | Ghi rõ entry cuối cùng dựa trên CE của FVG M5 hay một FVG/OB ở M1 |
| Có micro sweep + micro MSS ở M1 không | Có/không — dùng để đánh giá chất lượng xác nhận entry |
| Kết quả | Thắng/Thua/BE, R đạt được, có vi phạm checklist nào không |

**Trường dữ liệu khuyến nghị đưa vào nhật ký (journaling fields):**
- Thị trường, khung hình thành displacement, khung entry thực tế (CE M5 hay M1).
- Body-to-range ratio của nến displacement chính, và hệ số so với ATR(14) tại thời điểm đó (đối chiếu bảng ở mục 3).
- Độ sâu retrace thực tế (%) so với FVG M5 gốc.
- Có/không có M1 PD array; nếu không có, đã chọn nhánh nào trong cây quyết định ở mục 4 (chờ leg tiếp theo hay chấp nhận FVG sâu hơn).
- R:R kế hoạch vs R:R thực tế, và size lệnh so với mức rủi ro ≤0.5%.
- Liên kết [[06 - Mistake Database]] nếu có vi phạm (chase, dời SL, vào không có xác nhận...).

**Bảng đối chiếu: thói quen nghiệp dư vs thói quen chuyên nghiệp khi move không quay về FVG rõ ràng**

| Tình huống | Thói quen nghiệp dư | Thói quen chuyên nghiệp |
|---|---|---|
| Giá không hồi về FVG M5 như kỳ vọng | Tiếp tục chờ, hi vọng giá sẽ quay lại | Nhận diện ngay đây có thể là displacement aggressive, chuyển sang kịch bản B (CE/M1) đã pre-plan |
| Thấy giá đã chạy xa mà chưa vào lệnh | FOMO chase market ngay tại thời điểm phát hiện | Chờ leg tiếp theo hoặc chấp nhận bỏ lệnh, không đuổi giá |
| Không có FVG/OB ở M1 trong leg retrace | Tự vẽ một vùng "nhìn có vẻ hợp lý" để có lý do vào lệnh | Áp dụng cây quyết định ở mục 4: dùng CE độc lập, chờ leg mới, hoặc chấp nhận FVG M5 sâu hơn có kiểm soát |
| Tính size lệnh khi SL hẹp hơn (entry tại CE/M1) | Giữ nguyên số lot cố định mọi lúc, không tính lại risk% | Tính lại size theo khoảng cách SL mới, giữ đúng rủi ro ≤0.5%, có biên an toàn cho slippage |
| CE thất bại (giá xuyên ngược qua CE) | Vẫn cố giữ lệnh hoặc vào ngược ngay lập tức mà không chờ xác nhận | Thoát khỏi setup gốc, chờ MSS ngược hướng xác nhận trước khi coi vùng đó là iFVG/breaker (xem mục 4) |
| Backtest concept này | Chỉ nhớ vài lần "đúng đẹp" rồi tin tưởng tuyệt đối | Log đầy đủ body-to-range ratio, độ sâu retrace, loại PD array dùng, và kết quả theo bảng ở trên |

---

## 9. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy displacement mạnh
> Aggressive Displacement Entry chỉ hợp lệ trong đúng context sweep + MSS + còn room. Đừng dùng nó để biện minh cho việc chase.

- [ ] Daily Bias rõ ràng, displacement cùng hướng bias.
- [ ] Đã có sweep + MSS hợp lệ trước displacement.
- [ ] Displacement thật sự aggressive (body lớn liên tiếp, retrace nông).
- [ ] Đã tính CE của FVG M5 và đặt đó làm vùng entry kỳ vọng.
- [ ] Đã hạ M1 tìm FVG/OB refine; lý tưởng có micro MSS xác nhận.
- [ ] Entry có stop logic; còn liquidity target rõ ràng cho R:R đủ.
- [ ] Nếu giá không chạm CE → chấp nhận bỏ lệnh, không FOMO.

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Chờ fill sâu vào FVG to/thấp | Limit ở đáy FVG không bao giờ khớp | Dùng CE (50%) làm vùng entry, hoặc M1 FVG cao hơn |
| Đánh dấu sai FVG | Chọn FVG to/thấp thay vì FVG ngay tại nến MSS | Ưu tiên FVG hình thành ngay tại displacement/MSS candle |
| Chase sau khi lỡ | FOMO vào market ở đỉnh leg | Không đuổi; chờ leg tiếp theo (sweep nội bộ + FVG M1 mới) |
| Không hạ khung | Chỉ nhìn M5 cho một move quá mạnh | Drop M1 để phóng to leg retrace, tìm entry refine |
| Bỏ qua failed shift | Coi mọi pullback là retrace để mua | Acceptance ngược MSS level = invalidation, không vào |

---

## 11. Câu hỏi tự kiểm tra

- Move này thật sự aggressive (body lớn, retrace nông) hay chỉ là displacement bình thường?
- CE của FVG M5 nằm ở đâu, và giá có khả năng chạm tới đó không?
- Trên M1, có FVG/OB nào nằm cao hơn để refine entry không?
- Còn đủ room tới draw on liquidity để R:R đạt kế hoạch không?
- Nếu giá không chạm CE, tôi có kỷ luật đứng ngoài thay vì chase không?

---

## 12. Flashcards / Active Recall

### Q1
**Hỏi:** Vì sao trong displacement mạnh, FVG to/thấp thường không được giá quay về?
**Đáp:** Vì có institutional sponsorship lớn — smart money không cho giá rẻ lại (efficient delivery). Retrace nông là tín hiệu của move mạnh, không phải lỗi.

### Q2
**Hỏi:** Entry refine nên tìm ở đâu khi retrace quá nông?
**Đáp:** Tại CE (50%) của FVG M5, hoặc hạ M1 tìm FVG/OB nhỏ hơn nằm cao hơn, lý tưởng có micro sweep + micro MSS xác nhận.

### Q3
**Hỏi:** Lỗi phổ biến nhất với tình huống này là gì?
**Đáp:** Đặt limit ở đáy FVG to/thấp → không được chạm → bỏ lỡ → FOMO chase ở giá xấu.

---

## 13. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

---

## 14. Lesson Learned

### Bài học chính
- Displacement càng mạnh → retrace càng nông → entry càng phải **cao hơn và refine ở khung nhỏ hơn**.
- FVG to/thấp = entry "an toàn" nhưng thường không được chạm.
- Thà entry nông tại CE + xác nhận M1 còn hơn chờ fill sâu không bao giờ tới.

### Quy tắc cá nhân rút ra
- [ ] Tôi tính CE của FVG M5 trước, dùng nó làm vùng entry kỳ vọng thay vì đáy FVG.
- [ ] Khi move quá mạnh, tôi hạ M1 tìm FVG/OB refine, không bám FVG M5 to.
- [ ] Nếu giá không chạm vùng entry hợp lý, tôi đứng ngoài, không chase.

### Câu nhắc nhở khi trade
> **"Displacement mạnh không cho giá rẻ. Entry nằm cao hơn mình nghĩ — refine, đừng chờ fill sâu, đừng chase."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt được move aggressive vs displacement thường? |
| Nhận diện trên chart |  | Có nhận ra retrace nông sớm và tính CE không? |
| Biết khi nào bỏ qua |  | Có đứng ngoài khi hết room / không có M1 PD array không? |
| Kết hợp với context HTF |  | Move có luôn đồng pha draw on liquidity HTF không? |
| Áp dụng vào trade thực tế |  | Entry thực sự ở CE/M1, không chase đỉnh leg? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập các setup displacement mạnh, gắn tag `[[Aggressive Displacement Entry]]`.
- [ ] So sánh win rate giữa entry "CE/M1 refine" vs "chờ fill FVG to".
- [ ] Thống kê tỉ lệ FVG to/thấp được chạm trong các move mạnh để định lượng rule.
