---
type: ict-concept
concept: Internal & External Range Liquidity
aliases:
  - IRL
  - ERL
  - Internal Range Liquidity
  - External Range Liquidity
tags:
  - trading/ict/concept
  - trading/study
  - "#IRL-ERL"
status: developing
category: Liquidity
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
importance: 5
confidence: 1
last_reviewed: 2026-06-23
created: 2026-06-23
updated: 2026-07-03
common_mistakes:
  - "[[Mistake - Target Past Unfilled IRL]]"
  - "[[Mistake - Ignore Draw On Liquidity]]"
---

# Internal & External Range Liquidity (IRL & ERL)

> [!summary] Tóm tắt 1 câu
> **Trong một dealing range, External Range Liquidity (ERL) là thanh khoản nằm ở HAI CỰC range (đỉnh = BSL, đáy = SSL — các old high/low), còn Internal Range Liquidity (IRL) là các inefficiency / PD array NẰM BÊN TRONG range (FVG, Order Block) mà giá muốn rebalance; thuật toán ICT luân chuyển giá qua lại giữa hai loại này: external → internal → external.**

> [!important] Nguyên tắc cốt lõi
> **Giá luôn di chuyển từ một loại thanh khoản tới loại đối diện: "external to internal, internal to external". Khi giá vừa lấy ERL (quét đỉnh/đáy), draw tiếp theo thường là một IRL (FVG/OB chưa lấp) bên trong. Khi giá vừa phản ứng tại IRL, draw tiếp theo thường là ERL đối diện.**
> Định target mà bỏ qua IRL còn dang dở trên đường đi = đặt TP không thực tế. Giá phải "dọn dẹp" IRL trước khi với tới ERL.

---

## 1. Định nghĩa

**Khái niệm:**  
Mọi phân tích ICT đều diễn ra bên trong một [[12 - Dealing Range]] (vùng giao dịch xác định bởi một swing high và một swing low có ý nghĩa). Bên trong và xung quanh range đó tồn tại hai loại thanh khoản:

- **External Range Liquidity (ERL):** thanh khoản nằm ở **hai cực của range** — đỉnh range chứa [[07 - Buy-side Liquidity|Buy-side Liquidity (BSL)]] (stop của short + buy stop trên các old highs / equal highs), đáy range chứa [[30 - Sell-side Liquidity|Sell-side Liquidity (SSL)]] (stop của long + sell stop dưới các old lows / equal lows). Đây là thanh khoản "lộ thiên" ở biên.
- **Internal Range Liquidity (IRL):** các **inefficiency / PD array nằm BÊN TRONG range** — chủ yếu là [[Fair Value Gap|FVG]] chưa lấp, [[Order Block]], imbalance. Giá có xu hướng quay lại **rebalance** các vùng này. IRL là thanh khoản "ẩn" bên trong, không phải ở biên.

**Bản chất:** ICT mô tả delivery của giá như một thuật toán dao động giữa hai cực thanh khoản. Sau khi giá lấy ERL (ví dụ quét một old high), nó có xu hướng quay vào trong để rebalance một IRL (lấp một FVG); sau khi rebalance IRL xong, nó lại hướng ra ERL đối diện (old low). Vòng lặp **ERL → IRL → ERL** này là khung xương để đọc "draw on liquidity" — câu hỏi "giá đang bị hút về đâu tiếp theo?"

**Quan hệ với premium/discount:** ERL ở đỉnh nằm trong vùng [[27 - Premium Discount|premium]]; ERL ở đáy nằm trong discount; equilibrium (50%) chia range. IRL có thể nằm ở premium hoặc discount tùy vị trí FVG/OB. Kết hợp IRL/ERL với premium/discount cho phép xác định: *target nào hợp lý cho hướng trade, và entry nào nằm đúng phía rẻ/đắt.*

**Mục đích trong ICT:**  
- **Xác định DRAW on liquidity (target):** loại thanh khoản đối diện là nơi giá có xu hướng đi tới — đó là target logic.
- **Định trình tự delivery:** dự đoán giá sẽ đi external → internal hay internal → external tiếp theo.
- **Lọc target không thực tế:** nếu còn IRL (FVG) chưa lấp trên đường đi tới ERL, giá thường xử lý IRL trước → đừng đặt TP vượt qua nó một cách ngây thơ.
- **Hỗ trợ [[12 - Daily Bias]]:** bias cho biết hướng ưu tiên; IRL/ERL cho biết các "trạm dừng" thanh khoản trên đường đi.

**Vì sao khái niệm này quan trọng:**  
IRL/ERL là bản đồ "giá đi từ đâu tới đâu". Không có nó, trader đặt target tùy hứng và bị reject tại các FVG nội bộ mà họ không thấy. Nó biến câu hỏi mơ hồ "giá sẽ đi đâu?" thành một logic rõ: *vừa lấy gì → sẽ hút về cái đối diện*.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá vừa lấy thanh khoản loại nào (ERL hay IRL)?
- Draw tiếp theo là IRL (FVG nội bộ) hay ERL (đỉnh/đáy range)?
- Còn IRL nào chưa lấp chặn đường tới ERL không?
- Target hợp lý cho hướng trade này nằm ở đâu?

### IRL & ERL không phải là gì
- Không phải là tín hiệu entry độc lập — nó là khung để đọc draw / target.
- Không phải mọi FVG nội bộ đều bắt buộc bị lấp — chỉ những cái nằm trên đường delivery hợp narrative.
- ERL không phải lúc nào cũng đảo chiều — quét ERL có thể chỉ là lấy thanh khoản rồi tiếp tục.
- IRL không phải là "đáy/đỉnh" — nó là vùng inefficiency bên trong, không phải biên range.
- Không thay thế dealing range — phải xác định đúng range trước thì IRL/ERL mới có nghĩa.

![[IRL-ERL-Advanced-Anatomy.svg|697]]
*Giải phẫu một dealing range hoàn chỉnh: ERL đỉnh (BSL, old highs) và ERL đáy (SSL, old lows) đóng vai trò hai cực; một FVG (IRL) nằm bên trong range. Vòng xoay delivery được đánh số ① giá quét ERL đỉnh (lấy BSL) → ② quay vào rebalance IRL (FVG nội bộ) → ③ tiếp tục hướng ra ERL đáy (lấy SSL), minh họa đúng nguyên tắc "external → internal → external".*

---

## 2. Bối cảnh sử dụng

### Phân loại IRL vs ERL

| Tiêu chí | External Range Liquidity (ERL) | Internal Range Liquidity (IRL) |
|---|---|---|
| **Vị trí** | Hai cực range (đỉnh = BSL, đáy = SSL) | Bên trong range |
| **Hình thức** | Old highs/lows, equal highs/lows | FVG chưa lấp, Order Block, imbalance |
| **Loại thanh khoản** | Pool stop lộ thiên ở biên | Inefficiency cần rebalance |
| **Vai trò** | Target "cuối" của một leg; nơi giá quét | "Trạm dừng" giữa đường; nơi giá phản ứng |
| **Premium/Discount** | ERL đỉnh = premium; ERL đáy = discount | Tùy vị trí FVG/OB trong range |
| **Tín hiệu** | Sweep ERL → có thể đảo (kèm MSS) | Phản ứng tại IRL → tiếp tục hoặc đảo nhỏ |

> [!tip]
> Câu thần chú: **"External to internal, internal to external."** Mỗi khi giá làm một việc (quét ERL hoặc rebalance IRL), hãy hỏi ngay: *cái đối diện là gì, và nó nằm ở đâu?* Đó chính là draw tiếp theo và là target ứng viên.

### Khi nào khái niệm này có giá trị cao?
- [ ] Đã xác định đúng một [[12 - Dealing Range]] có ý nghĩa (swing high/low rõ).
- [ ] Có [[12 - Daily Bias]] để biết hướng ưu tiên trong vòng xoay IRL/ERL.
- [ ] Có FVG/OB nội bộ (IRL) chưa lấp rõ ràng.
- [ ] Có old highs/lows hoặc equal highs/lows (ERL) rõ ràng ở hai cực.
- [ ] Cần định target / draw on liquidity cho một setup.

### Khi nào nên bỏ qua?
- [ ] Không xác định được dealing range (giá đang trong nhiễu / range chồng chéo).
- [ ] Không có IRL rõ (FVG/OB) lẫn ERL rõ — không có "hai cực" để luân chuyển.
- [ ] Đang dùng IRL/ERL như tín hiệu vào lệnh đơn lẻ thay vì khung target.
- [ ] HTF không có narrative — không biết hướng ưu tiên.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Xác định dealing range:** chọn swing high và swing low có ý nghĩa làm biên.
2. **Đánh dấu ERL:** old highs (BSL) ở trên, old lows (SSL) ở dưới; chú ý equal highs/lows (pool dày).
3. **Đánh dấu IRL:** các FVG chưa lấp và OB nằm bên trong range.
4. **Xác định giá vừa lấy gì:** vừa quét ERL hay vừa rebalance IRL?
5. **Suy ra draw tiếp theo:** cái đối diện (external ↔ internal).

### Bản đồ vòng xoay delivery

| Giá vừa làm gì | Draw tiếp theo (ứng viên) | Đọc thực chiến |
|---|---|---|
| Quét ERL đỉnh (lấy BSL) | IRL bên trong (FVG/OB) hoặc ERL đáy | Sau khi lấy BSL, thường rebalance về FVG nội bộ |
| Quét ERL đáy (lấy SSL) | IRL bên trong (FVG/OB) hoặc ERL đỉnh | Sau khi lấy SSL, thường rebalance về FVG nội bộ |
| Phản ứng / lấp một IRL (FVG) | ERL đối diện | Sau khi xử lý FVG, hướng ra đỉnh/đáy range |
| Lấp hết IRL, không còn inefficiency | ERL đối diện trực tiếp | Đường tới ERL "thông thoáng" hơn |

### Điều kiện bắt buộc
- [ ] Dealing range được định rõ (swing high & swing low).
- [ ] Đánh dấu được ít nhất một ERL và một IRL.
- [ ] Xác định được giá đang vừa lấy thanh khoản loại nào.
- [ ] Biết equilibrium (50%) để gắn premium/discount.

### Điều kiện tăng xác suất
- [ ] Vòng xoay IRL/ERL đồng hướng [[12 - Daily Bias]].
- [ ] IRL là FVG sinh từ displacement (chất lượng cao), không phải gap ngẫu nhiên.
- [ ] ERL là equal highs/lows (pool dày → draw mạnh hơn).
- [ ] IRL nằm đúng premium/discount cho hướng trade (entry tại IRL discount để Long).
- [ ] Có [[20 - Liquidity Sweep]] tại ERL kèm [[21 - Market Structure Shift|MSS]] để xác nhận đảo.

### Điều kiện làm setup yếu đi
- Dealing range mơ hồ / chọn sai swing.
- Quá nhiều IRL chồng chéo → không rõ cái nào là draw chính.
- ERL đã bị lấy nhiều lần (pool mỏng dần).
- Đặt target vượt qua IRL chưa lấp mà không tính tới nó.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng IRL/ERL
> 1. **Dealing range của tôi là gì (swing high/low nào)?**
> 2. **ERL ở đâu (đỉnh/đáy) và IRL ở đâu (FVG/OB nội bộ)?**
> 3. **Giá vừa lấy thanh khoản loại nào — nên draw tiếp theo là external hay internal?**
> 4. **Còn IRL nào chưa lấp chặn đường tới ERL target của tôi không?**

### D1 / H4 — Bias & Narrative
- Bias hiện tại: Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]).
- HTF dealing range: swing high/low nào định range?
- ERL HTF: old highs (BSL) / old lows (SSL) lớn nhất ở đâu? → target chính.
- IRL HTF: có FVG/OB D1-H4 chưa lấp nào là draw nội bộ không?
- Vị trí giá: premium hay discount của range?

### H1 / M15 — IRL/ERL & Context
- Đánh dấu chi tiết IRL (FVG/OB H1-M15) và ERL (đỉnh/đáy) trong range.
- Giá vừa quét ERL hay vừa phản ứng tại IRL? → suy ra draw tiếp theo.
- Ghi rõ: `Giá vừa quét SSL đáy range → draw nội bộ là H1 bullish FVG [low]–[high] → sau đó ERL đỉnh là BSL [level]`.
- Kiểm tra IRL còn dang dở trên đường tới ERL target.

### M5 / M1 — Confirmation & Entry
- Sau khi giá tới một IRL hoặc ERL, có [[21 - Market Structure Shift|MSS]] / displacement xác nhận không?
- Entry refine trong IRL (FVG/OB nội bộ) đúng premium/discount.
- Target: IRL kế tiếp trước (partial), ERL đối diện sau (full).

```text
Mẫu ghi nhanh — Long theo vòng xoay IRL/ERL
HTF Bias: Bullish | Dealing range: [low] – [high]
Giá vừa làm: quét ERL đáy (lấy SSL) tại [level]
Draw nội bộ (IRL): bullish FVG [low]–[high] ở discount → entry zone
Draw external (ERL): BSL đỉnh range tại [level] → target chính
IRL chặn đường: kiểm tra FVG/OB bearish nào trên đường lên?
Entry: tại IRL FVG sau M5 MSS bullish
Stop: dưới đáy ERL vừa quét
Target: IRL/OB kế tiếp (partial) → ERL BSL (full)
Invalid: giá đóng nến xuyên xuống dưới đáy ERL đã quét
```

> [!warning]
> **ERL đối diện là target hấp dẫn, nhưng đừng nhảy cóc qua IRL.** Nếu giữa giá và ERL target còn một FVG (IRL) chưa lấp, giá thường rebalance FVG đó trước — TP đặt vượt qua nó có thể không bao giờ chạm tới trước khi giá quay đầu.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Dealing range rõ; ERL và IRL được đánh dấu chính xác.
- [ ] Vòng xoay IRL/ERL đồng hướng Daily Bias.
- [ ] Giá vừa lấy một loại thanh khoản → draw tiếp theo là loại đối diện logic.
- [ ] Entry tại IRL (FVG/OB) đúng premium/discount cho hướng trade.
- [ ] Có MSS/displacement xác nhận tại điểm phản ứng.
- [ ] Target được đặt tới thanh khoản thật (IRL kế tiếp / ERL), có tính tới IRL chặn đường.

### Setup bị vô hiệu khi
- [ ] Giá phá hẳn biên dealing range theo hướng ngược → range cũ không còn hiệu lực, vẽ lại.
- [ ] Đặt target vượt qua IRL chưa lấp mà bỏ qua nó.
- [ ] Dùng "chạm ERL" làm lý do đảo lệnh khi không có MSS xác nhận.
- [ ] Dealing range chọn sai → toàn bộ bản đồ IRL/ERL sai theo.

### So sánh trạng thái draw

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Giá vừa quét ERL, còn FVG (IRL) chưa lấp bên trong | External → Internal | Draw tiếp theo là IRL; chờ phản ứng tại FVG |
| Giá vừa phản ứng tại IRL, ERL đối diện còn nguyên | Internal → External | Draw tiếp theo là ERL; đó là target |
| Giá quét ERL nhưng đóng nến chấp nhận ra ngoài | Range mở rộng | Range cũ thất bại; xác định range mới |
| Nhiều IRL chồng chéo giữa giá và ERL | Đường đi "nghẽn" | Chia target theo từng IRL; giảm kỳ vọng TP xa |

### Nâng cao — Equal highs/lows vs single old high: sức hút ERL khác nhau thế nào

Không phải mọi ERL có sức hút như nhau. Một **single old high/low** (đỉnh/đáy đơn, chỉ một lần chạm) chứa một lớp stop mỏng — vài lệnh short-stop hoặc buy-stop nằm rải rác quanh đó. Ngược lại, **equal highs/equal lows** (hai hay nhiều lần giá chạm cùng một vùng mà không phá qua) tạo ra một **resting liquidity pool** dày đặc: mỗi lần retest thất bại lại có thêm trader đặt stop mới NGAY TẠI/NGAY TRÊN vùng đó (vì "đỉnh này đã giữ hai lần rồi, chắc là kháng cự mạnh"), cộng dồn lên lớp stop cũ chưa bị quét. Đó là lý do thuật toán/order flow tổ chức ưu tiên target các pool bị stack nhiều lần: quét một vùng có nhiều stop xếp chồng cho phép fill một khối lượng lớn hiệu quả hơn nhiều so với quét một single high chỉ có vài lệnh rải rác — chi phí trượt giá (slippage) trên mỗi đơn vị thanh khoản lấy được thấp hơn.

Thang chấm sức hút ERL theo số lần chạm:

| Loại ERL | Số lần chạm | Sức hút | Xác suất bị quét trong phiên |
|---|---|---|---|
| Single wick top/bottom | 1 lần (chỉ bóng nến) | Thấp | Thấp — dễ bị bỏ qua, không đủ hấp dẫn |
| Old high/low rõ (1 lần chạm bằng body) | 1 lần | Trung bình | Trung bình |
| Double top/bottom (2 lần chạm) | 2 lần | Khá cao | Khá cao — đã có "niềm tin" kháng cự/hỗ trợ |
| Equal highs/lows (3+ lần chạm) | 3 lần trở lên | Rất cao | Cao — pool dày, gần như luôn nằm trong watch-list draw on liquidity |

> [!tip]
> Khi có nhiều ứng viên ERL trên chart, ưu tiên equal highs/lows làm target chính thay vì một single old high gần hơn nhưng mỏng. Ghi lại số lần chạm của ERL vào ghi chú setup (`erl_target` kèm số lần chạm) — sau một khoảng thời gian bạn sẽ thấy các lệnh nhắm vào equal highs/lows có tỉ lệ chạm target cao hơn rõ rệt so với single high/low.

### Nâng cao — Tính phân dạng (fractal nesting) của IRL/ERL: một ERL lớn chứa bên trong nó một dealing range nhỏ hơn

IRL/ERL không phải một cấu trúc cố định gắn chết vào một khung thời gian — nó **phân dạng (fractal)**: cùng một vùng giá, ở khung lớn có thể là ERL (biên ngoài của dealing range D1), nhưng khi zoom vào H1/M15 ngay tại vùng đó, bạn sẽ thấy nó tự nó là biên của một **dealing range nhỏ hơn**, với IRL và ERL riêng nằm bên trong. Nói cách khác: cái mà D1 gọi là "đỉnh range" chỉ là điểm zoom-in để bắt đầu một chu kỳ ERL → IRL → ERL mới ở khung nhỏ hơn.

Kỹ thuật thực chiến: khi giá tiếp cận một ERL lớn (HTF) mà bạn muốn Long/Short phản ứng tại đó, đừng vào lệnh ngay tại biên HTF một cách thô — hãy **zoom vào H1/M15/M5** ngay tại vùng ERL đó để tìm dealing range nội bộ mới, xác định IRL/ERL riêng của nó, và tìm entry tinh chỉnh hơn (ví dụ Short tại ERL đỉnh D1, nhưng entry thực tế đặt tại IRL — một FVG H1 — bên trong dealing range nhỏ ngay dưới đỉnh D1 đó).

| Khung thời gian | Vai trò | IRL bên trong | ERL bên trong | Mục đích sử dụng |
|---|---|---|---|---|
| D1 (HTF) | Toàn bộ dealing range lớn | FVG/OB D1-H4 chưa lấp | Đỉnh/đáy D1 (BSL/SSL chính) | Xác định bias, target chính, draw tổng thể |
| H1 (nested trong ERL D1) | Dealing range con ngay tại vùng ERL D1 | FVG/OB H1 mới hình thành khi giá tiếp cận ERL D1 | Đỉnh/đáy H1 nội bộ (có thể chỉ là vài chục pip) | Tìm entry tinh chỉnh, stop ngắn hơn, R:R tốt hơn |
| M15/M5 (nested trong ERL H1) | Dealing range con nhỏ hơn nữa | FVG/OB M15-M5 | Đỉnh/đáy M5 nội bộ | Xác nhận MSS/displacement LTF trước khi bấm lệnh |

> [!note]
> Cấu trúc phân dạng này chính là lý do phân tích đa khung thời gian (top-down) hiệu quả: bạn không "bỏ" logic IRL/ERL khi chuyển từ D1 xuống M15 — bạn chỉ đang **áp lại đúng logic đó ở một tỉ lệ nhỏ hơn**, ngay bên trong vùng mà khung lớn hơn gọi là ERL.

![[IRL-ERL-Advanced-Nested-Fractal.svg|697]]
*Bên trái là dealing range HTF với ERL đỉnh/đáy riêng của nó. Ô "zoom" nét đứt phóng to đúng vùng ERL đỉnh HTF sang bên phải, cho thấy bên trong vùng đó tồn tại một dealing range LTF hoàn toàn riêng — với ERL và IRL (FVG) của chính nó. Đây là bằng chứng trực quan cho tính phân dạng: "ERL" chỉ là tên gọi phụ thuộc khung thời gian đang xét, không phải một thuộc tính cố định của vùng giá.*

### Nâng cao — Khi không có IRL: liquidity void và cú chạy thẳng (news / low-inefficiency conditions)

Quy tắc "external → internal → external" giả định luôn tồn tại một IRL (FVG/OB) có ý nghĩa nằm giữa hai cực ERL. Nhưng thực tế có những trường hợp **không hề có IRL đáng kể** giữa đường: một dealing range "sạch" hiếm inefficiency, hoặc một nhịp mở rộng nhanh do tin tức (news) tạo ra các nến thân dài, ít overlap, gần như không để lại FVG/OB nào làm điểm dừng. Khi đó giá không "ghé" IRL nào cả — nó chạy thẳng một mạch từ ERL này sang ERL đối diện. Đây gọi là **liquidity void / cú chạy thẳng**, và nó phá vỡ kỳ vọng "sẽ có trạm dừng giữa đường" nếu bạn áp dụng máy móc mô hình external-internal-external.

Cách nhận diện trước khi nó xảy ra:
- **Thân nến mỏng, ít overlap wick:** nhìn dọc theo đường đi dự kiến tới ERL target — nếu phần lớn nến có thân nhỏ và các wick không chồng lấn nhau nhiều, đó là dấu hiệu thiếu ứng viên Order Block (OB cần một cụm nến ngược chiều rõ ràng để hình thành).
- **Không có FVG nào rõ:** quét kỹ khung phân tích — nếu không tìm được một FVG 3 nến rõ ràng nào nằm giữa giá hiện tại và ERL target, khả năng cao đây là một dealing range không có IRL thật.
- **Bối cảnh tin tức / thanh khoản mỏng:** các phiên tin tức lớn (NFP, FOMC, CPI) hoặc thanh khoản mỏng (rollover, lễ) thường tạo displacement liên tục không để lại imbalance để rebalance ngay — giá "nợ" việc rebalance đó cho một phiên sau.

Điều này thay đổi kỳ vọng entry/target ra sao: **đừng cố ép một entry limit tại một IRL không tồn tại** chỉ vì mô hình lý thuyết nói "phải có trạm dừng". Nếu không xác định được IRL thật trên đường đi, có hai lựa chọn hợp lý: (1) chờ một **market-structure-shift entry** — vào theo xác nhận MSS/displacement LTF tại thời điểm giá phản ứng thực tế, thay vì đặt lệnh chờ tại một vùng "lý thuyết"; hoặc (2) chấp nhận không có partial-TP giữa đường và đặt kế hoạch quản trị lệnh cho khả năng giá chạy thẳng tới ERL đối diện mà không hồi.

> [!warning]
> Đừng vẽ một FVG/OB gượng ép chỉ để "có IRL cho đủ mô hình". Một liquidity void thật sự không có PD array nào đáng tin cậy nằm giữa hai ERL — cố nhồi nhét một vùng entry limit vào đó thường dẫn tới việc bỏ lỡ hoàn toàn cú chạy thẳng (giá không bao giờ hồi về "IRL" tưởng tượng), hoặc vào lệnh tại một vùng không có cơ sở thống kê. Khi nghi ngờ có liquidity void, ưu tiên xác nhận bằng MSS thay vì limit order tại một mức "IRL" không tồn tại.

![[IRL-ERL-Advanced-Liquidity-Void.svg|697]]
*So sánh hai kịch bản: panel trái là một dealing range bình thường với một FVG (IRL) rõ ràng — giá dừng lại, phản ứng, rebalance trước khi tiếp tục tới ERL đối diện. Panel phải là một liquidity void — không có FVG/OB nào đáng kể giữa hai ERL — nên giá chạy thẳng một mạch từ ERL này sang ERL kia mà không dừng, đúng như đặc điểm của một cú chạy thẳng do tin tức hoặc range không hiệu suất thấp (low-inefficiency).*

---

## 6. Ví dụ chart

### Ví dụ đúng
![[IRL-ERL-Example-Correct.svg|697]]

**Mô tả:**  
Một dealing range rõ với ERL ở đỉnh (BSL) và đáy (SSL), một FVG (IRL) nằm giữa. Giá bắt đầu từ ERL đỉnh, đi vào trong rebalance IRL (FVG), phản ứng tại đó, rồi tiếp tục xuống quét ERL đáy (SSL). Sau khi lấy SSL, giá xoay ngược lên hướng về ERL đỉnh (BSL). Vòng xoay **ERL → IRL → ERL** được đọc rõ, mỗi bước cho một draw / target hợp lý.

**Vì sao đây là ví dụ tốt:**
- ERL được đánh dấu ở đúng hai cực range; IRL là FVG nội bộ rõ ràng.
- Trình tự external → internal → external diễn ra đúng logic.
- Mỗi loại thanh khoản đã lấy đều dẫn tới draw đối diện → target có cơ sở.
- Không nhảy cóc: giá xử lý IRL trước khi với tới ERL đối diện.

### Ví dụ sai / dễ nhầm
![[IRL-ERL-Example-Wrong.svg|697]]

**Mô tả lỗi:**  
Trader Long từ đáy range và đặt target thẳng lên ERL đỉnh (BSL), nhưng bỏ qua một **bearish FVG (IRL) chưa lấp** nằm chặn đường đi lên. Giá rally tới IRL đó, bị reject ngay tại FVG nội bộ, rồi quay đầu xuống — TP tại ERL đỉnh không bao giờ chạm tới. Lệnh đáng lẽ chốt một phần tại IRL lại thành lệnh hòa hoặc thua.

**Bài học:**
- Luôn quét đường đi tới ERL target xem có IRL chưa lấp nào chặn không.
- IRL nội bộ là "trạm dừng" — giá thường phản ứng tại đó trước khi với tới ERL.
- Chia target theo IRL kế tiếp (partial) rồi mới tới ERL (full).

---
### Sequence mẫu — Long theo vòng xoay (External → Internal → External)
```text
HTF Bullish Bias
→ Xác định Dealing Range (swing high/low)
→ Giá quét ERL đáy (lấy SSL) — external taken
→ Draw nội bộ = bullish FVG (IRL) ở discount
→ Giá vào IRL → M5 MSS bullish + displacement
→ Entry tại IRL (FVG) đúng discount
→ Stop dưới đáy ERL vừa quét
→ Target: IRL/OB kế tiếp (partial) → ERL đỉnh BSL (full) — internal → external
```

### Sequence mẫu — Short theo vòng xoay
```text
HTF Bearish Bias
→ Xác định Dealing Range (swing high/low)
→ Giá quét ERL đỉnh (lấy BSL) — external taken
→ Draw nội bộ = bearish FVG (IRL) ở premium
→ Giá vào IRL → M5 MSS bearish + displacement
→ Entry tại IRL (FVG) đúng premium
→ Stop trên đỉnh ERL vừa quét
→ Target: IRL/OB kế tiếp (partial) → ERL đáy SSL (full) — internal → external
```

> [!note]
> IRL/ERL là khung target tổng quát, ghép tốt với mọi entry model: [[Order Block]], [[Fair Value Gap]], [[Optimal Trade Entry]]. Entry model cho biết VÀO ở đâu; IRL/ERL cho biết giá ĐI tới đâu (draw / t