---
type: ict-concept
concept: "Internal & External Range Liquidity"
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
  - "[[Trading Journal/02 - Trading Knowledge/Models/ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-23
created: 2026-06-23
updated: 2026-06-23
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

---

## 6. Ví dụ chart

### Ví dụ đúng
![[IRL-ERL-Example-Correct.svg]]

**Mô tả:**  
Một dealing range rõ với ERL ở đỉnh (BSL) và đáy (SSL), một FVG (IRL) nằm giữa. Giá bắt đầu từ ERL đỉnh, đi vào trong rebalance IRL (FVG), phản ứng tại đó, rồi tiếp tục xuống quét ERL đáy (SSL). Sau khi lấy SSL, giá xoay ngược lên hướng về ERL đỉnh (BSL). Vòng xoay **ERL → IRL → ERL** được đọc rõ, mỗi bước cho một draw / target hợp lý.

**Vì sao đây là ví dụ tốt:**
- ERL được đánh dấu ở đúng hai cực range; IRL là FVG nội bộ rõ ràng.
- Trình tự external → internal → external diễn ra đúng logic.
- Mỗi loại thanh khoản đã lấy đều dẫn tới draw đối diện → target có cơ sở.
- Không nhảy cóc: giá xử lý IRL trước khi với tới ERL đối diện.

### Ví dụ sai / dễ nhầm
![[IRL-ERL-Example-Wrong.svg]]

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
> IRL/ERL là khung target tổng quát, ghép tốt với mọi entry model: [[Order Block]], [[Fair Value Gap]], [[Optimal Trade Entry]]. Entry model cho biết VÀO ở đâu; IRL/ERL cho biết giá ĐI tới đâu (draw / target) và còn trạm dừng nào trên đường.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> IRL/ERL chỉ có giá trị khi đặt trong **dealing range đúng + bias rõ + đánh dấu đầy đủ hai loại thanh khoản**.

### A. Context (HTF)
- [ ] Dealing range được định rõ (swing high/low có ý nghĩa).
- [ ] Daily Bias rõ: `Bullish / Bearish / Neutral`.
- [ ] ERL đánh dấu ở hai cực (BSL đỉnh, SSL đáy).
- [ ] IRL đánh dấu bên trong (FVG/OB chưa lấp).
- [ ] Xác định giá vừa lấy thanh khoản loại nào → draw tiếp theo.
- [ ] Gắn premium/discount qua equilibrium.

### B. Execution (LTF)
- [ ] Entry tại IRL đúng premium/discount cho hướng trade.
- [ ] Có MSS/displacement xác nhận tại IRL/ERL.
- [ ] Đã quét đường đi tới ERL target xem có IRL chặn không.
- [ ] Stop logic: ngoài ERL/IRL vừa phản ứng.
- [ ] Target chia theo IRL kế tiếp (partial) → ERL (full).
- [ ] R:R đạt kế hoạch tính tới IRL chặn đường.

### C. Quy tắc "không có lệnh"
- [ ] Không xác định được dealing range → không trade.
- [ ] Không rõ draw tiếp theo (external hay internal) → không trade.
- [ ] Target phải nhảy cóc qua IRL chưa lấp → điều chỉnh hoặc không trade.
- [ ] Dùng IRL/ERL như tín hiệu đơn lẻ không có entry model → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bỏ qua IRL trên đường tới ERL | Đặt TP tại ERL, lờ FVG nội bộ chặn đường | Giá reject tại IRL trước khi tới ERL | Quét IRL chưa lấp; chia target theo IRL trước |
| Chọn sai dealing range | Lấy swing quá nhỏ/cũ làm biên | Toàn bộ bản đồ IRL/ERL sai | Chọn swing tạo displacement/BOS rõ |
| Coi mọi chạm ERL là đảo chiều | Đảo lệnh ngay khi giá chạm đỉnh/đáy | ERL có thể bị quét rồi tiếp tục | Chờ sweep + MSS xác nhận mới đảo |
| Không xác định draw tiếp theo | Không biết external hay internal kế tiếp | Target tùy hứng, không logic | Hỏi "vừa lấy gì → đối diện là gì" |
| Nhầm IRL với ERL | Coi FVG nội bộ là target cuối / coi đỉnh là IRL | Sai bản chất → target/stop sai | IRL = inefficiency bên trong; ERL = biên range |
| Target ERL quá xa khi nhiều IRL | TP tại ERL khi range "nghẽn" FVG | Kỳ vọng phi thực tế | Giảm kỳ vọng; chốt từng IRL |
| Quên premium/discount của IRL | Long ở IRL premium, Short ở IRL discount | Entry thành chase | Long tại IRL discount, Short tại IRL premium |

---

## 10. Câu hỏi tự kiểm tra

- Mình giải thích "external to internal, internal to external" trong 30 giây không?
- Dealing range hiện tại là gì, và ERL/IRL nằm ở đâu?
- Giá vừa lấy thanh khoản loại nào → draw tiếp theo là gì?
- Còn IRL (FVG) chưa lấp nào chặn đường tới ERL target không?
- IRL entry của mình nằm ở premium hay discount?
- ERL đối diện có phải là target thực tế không, hay cần chốt sớm tại IRL?
- Nếu giá phá biên range, range mới của mình là gì?
- Setup nào trong journal mình đặt TP vượt qua IRL và bị reject?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** ERL và IRL khác nhau ở đâu?  
**Đáp:** ERL (External Range Liquidity) = thanh khoản ở HAI CỰC range (đỉnh BSL, đáy SSL — old highs/lows). IRL (Internal Range Liquidity) = inefficiency BÊN TRONG range (FVG, OB) cần rebalance.

### Q2
**Hỏi:** Câu cốt lõi mô tả vòng xoay delivery là gì?  
**Đáp:** "External to internal, internal to external" — giá luân chuyển: lấy ERL → rebalance IRL → lấy ERL đối diện, lặp lại.

### Q3
**Hỏi:** Sau khi giá quét ERL đáy (lấy SSL), draw tiếp theo thường là gì?  
**Đáp:** Một IRL bên trong (thường là FVG chưa lấp ở discount) để rebalance, rồi sau đó hướng ra ERL đỉnh (BSL).

### Q4
**Hỏi:** Vì sao không nên đặt target nhảy cóc qua một IRL chưa lấp?  
**Đáp:** Vì giá có xu hướng rebalance IRL (FVG) trên đường đi trước; TP đặt vượt qua nó có thể không chạm tới trước khi giá quay đầu tại IRL đó.

### Q5
**Hỏi:** IRL/ERL chủ yếu giúp xác định điều gì — entry hay target?  
**Đáp:** Chủ yếu là DRAW on liquidity / target và trình tự delivery. Nó là khung target, không phải tín hiệu entry đơn lẻ.

### Q6
**Hỏi:** ERL đỉnh và đáy gắn với premium/discount thế nào?  
**Đáp:** ERL đỉnh nằm trong vùng premium; ERL đáy nằm trong vùng discount; equilibrium (50%) chia range.

---

## 12. Liên kết với Trade Journal

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

> [!note]
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "03 - Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
dealing_range: "1.0800 → 1.0920" # biên range
draw_state: external-to-internal # external-to-internal | internal-to-external
liquidity_just_taken: SSL # ERL/IRL vừa lấy: BSL | SSL | IRL-FVG
irl_entry: "1.0840 → 1.0855" # vùng IRL (FVG/OB) làm entry
erl_target: 1.0920 # ERL target chính
irl_blocking_path: false # có IRL chưa lấp chặn đường tới ERL không
```

> [!tip]
> Sau 30–50 lệnh, so sánh: lệnh có `irl_blocking_path: true` (đặt TP vượt IRL chưa lấp) vs `false`. Mục tiêu là kiểm chứng rằng chia target theo IRL trước ERL cải thiện tỉ lệ chạm TP và R thực tế.

---

## 13. Lesson Learned

### Bài học chính
- Giá luân chuyển: **external → internal → internal → external**; biết "vừa lấy gì" là biết "draw tiếp theo".
- ERL = biên range (BSL/SSL); IRL = inefficiency bên trong (FVG/OB) cần rebalance.
- Đừng nhảy cóc qua IRL chưa lấp — giá thường xử lý nó trước khi với tới ERL.
- IRL/ERL là khung TARGET, ghép với entry model để biết VÀO đâu và ĐI tới đâu.
- Gắn IRL/ERL với premium/discount để entry đúng phía rẻ/đắt.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn định dealing range trước, rồi đánh dấu ERL (2 cực) và IRL (nội bộ).
- [ ] Tôi xác định "giá vừa lấy gì" để suy ra draw tiếp theo.
- [ ] Tôi quét đường đi tới ERL target xem có IRL chưa lấp chặn không.
- [ ] Tôi chia target: IRL kế tiếp (partial) → ERL đối diện (full).
- [ ] Tôi chỉ entry tại IRL đúng premium/discount cho hướng trade.

### Câu nhắc nhở khi trade
> **"Giá đi từ thanh khoản này tới thanh khoản kia — tôi luôn hỏi: vừa lấy gì, đối diện là gì, và có IRL nào chặn đường không."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt rõ IRL vs ERL và vòng xoay không? |
| Nhận diện trên chart |  | Đánh dấu đúng ERL (2 cực) và IRL (nội bộ) không? |
| Biết khi nào bỏ qua |  | Có dừng khi không xác định được range/draw không? |
| Kết hợp với context HTF |  | IRL/ERL có gắn bias + premium/discount không? |
| Áp dụng vào trade thực tế |  | Target có tính tới IRL chặn đường không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập 20–30 setup gắn tag `[[Internal & External Range Liquidity (IRL & ERL)]]`.
- [ ] Review riêng: target có IRL chặn vs không; tỉ lệ chạm ERL target.
- [ ] Thống kê R thực tế theo `draw_state` và `irl_blocking_path`.

---

## Appendix — IRL & ERL Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**  
> **Daily Bias:** Bullish / Bearish / Neutral  
> **Dealing range (low → high):** ____  
> **ERL đỉnh (BSL):** ____ | **ERL đáy (SSL):** ____  
> **IRL nội bộ (FVG/OB chưa lấp):** ____  
> **Equilibrium (50%):**  
> **Giá vừa lấy thanh khoản loại nào:** BSL / SSL / IRL  
> **Draw tiếp theo:** external → internal / internal → external  
> **IRL chặn đường tới ERL target?** Yes / No — vùng: ____  
> **Entry zone (IRL, đúng premium/discount):**  
> **Target:** IRL kế tiếp (partial) → ERL (full)  
> **Stop logic:**  
> **Invalidation (phá biên range tại):**  
> **Kill zone permitted:** London / NY AM / NY PM  
> **No-trade condition:** range mơ hồ / draw không rõ
