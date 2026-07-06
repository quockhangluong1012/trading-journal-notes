---
type: ict-concept
concept: Standard Deviation
aliases:
  - Standard Deviation
  - SD
  - Standard Deviation Projection
  - SD Projection
tags:
  - trading/ict/concept
  - trading/study
  - "#StandardDeviation"
status: developing
category: Time & Price
last_reviewed:
created: 2026-06-26
updated: 2026-07-03
---

# Standard Deviation

> [!summary] Tóm tắt 1 câu
> **Standard Deviation (SD) Projection là công cụ DỰ PHÓNG nơi giá có khả năng đi tới (target / draw on liquidity) sau một swing đã xác định: đo một đoạn tham chiếu — thường là chân manipulation/Judas swing đã quét thanh khoản trước displacement — rồi chiếu các bội số độ lệch chuẩn (-1, -2, -2.5, -3, -4 SD) ra ngoài đoạn đó để ước lượng nơi nhịp mở rộng có thể kết thúc, đặc biệt khi mức SD trùng với liquidity pool hoặc PD-array khung lớn.**

> [!important] Nguyên tắc cốt lõi
> - **SD là công cụ TARGET / projection, KHÔNG phải tín hiệu entry.** Nó trả lời "giá đi tới đâu", không phải "vào lệnh ở đâu".
> - **Neo (anchor) phải đặt đúng vào đoạn manipulation/swing đã quét thanh khoản trước displacement.** Neo sai swing → mọi mức chiếu vô nghĩa.
> - **Một mức SD chỉ đáng tin khi có confluence**: trùng liquidity pool, FVG đối nghịch, hoặc PD-array HTF. Mức SD đứng một mình có giá trị thấp.
> - **Không coi mức SD là điểm đảo chiều chắc chắn.** Nó là vùng kỳ vọng giá phản ứng; phải chờ xác nhận cấu trúc, không bao giờ "đặt lệnh mù" tại một mức SD.

---

## 1. Định nghĩa

### Khái niệm
**Standard Deviation Projection** là kỹ thuật lấy một đoạn giá tham chiếu (reference range / leg) đã hoàn tất, rồi **chiếu (project) các bội số của chính đoạn đó** ra phía trước theo hướng giá đang mở rộng. Mỗi bội số gọi là một "độ lệch chuẩn" (standard deviation) — không phải theo nghĩa thống kê chặt chẽ, mà là **bội số đối xứng của biên độ swing gốc**. Các mức thường dùng: **-1, -2, -2.5, -3, -4 SD** (dùng công cụ fib "trend-based extension" / projection).

Đoạn tham chiếu được neo phổ biến nhất là **chân manipulation / Judas swing**: đoạn giá quét thanh khoản (consolidation high → low, hoặc swing đã sweep liquidity) **ngay trước** cú displacement phá cấu trúc. Logic: thị trường thường mở rộng (expansion) một cách **đối xứng** với đoạn manipulation đó — biết được biên độ "đánh lừa" thì ước lượng được biên độ "thật".

### Bản chất
- SD không sinh ra một mức S/R "vật lý" như Order Block hay FVG; nó là **một phép đo đối xứng** — lấy khoảng cách của leg gốc rồi nhân lên thành các mốc kỳ vọng.
- Vì đo từ manipulation leg, SD biến **độ sâu của cú lừa** thành **tầm với của cú đẩy thật**. Cú manipulation càng "ngọt" thì các mức chiếu càng có ý nghĩa.
- SD đáng tin nhất khi một mức chiếu **rơi đúng vào** một liquidity pool đã có sẵn, một FVG khung lớn, hoặc biên premium/discount của [[12 - Dealing Range]] — lúc đó projection và draw on liquidity củng cố nhau.

### Cách đo & chiếu (workflow vẽ)
1. Xác định **đoạn tham chiếu**: chân manipulation/Judas swing đã quét thanh khoản, ngay trước displacement (ví dụ: consolidation high → low của phiên, hoặc swing high → swing low đã sweep [[19 - Liquidity]]).
2. Dùng công cụ **fib "trend-based extension" / projection** (3 điểm) hoặc tự đặt mức: neo điểm đầu và điểm cuối của leg tham chiếu.
3. Điểm chiếu (-1 SD) = phản chiếu đối xứng của leg sang phía mở rộng; các mức tiếp theo (-2, -2.5, -3, -4 SD) là bội số tăng dần.
4. Đánh dấu các mức **-1, -2, -2.5, -3, -4 SD** và **đối chiếu từng mức với liquidity / FVG / PD-array HTF** để tìm mức nào có confluence.
5. Mức có confluence cao nhất = **draw on liquidity / target chính**; các mức còn lại = TP từng phần (partials).

```text
[Đoạn tham chiếu = chân manipulation/Judas swing đã sweep liquidity]

   Manipulation High ─────●  (điểm A)
                          │  leg tham chiếu (1 đơn vị SD)
   Manipulation Low  ─────●  (điểm B) → từ đây giá displacement đi xuống/lên
                          │
   ── -1 SD ─────────────────  ← target gần nhất
   ── -2 SD ─────────────────  ← thường trùng draw on liquidity chính
   ── -2.5 SD ───────────────
   ── -3 SD ─────────────────  ← target mở rộng / phiên trending mạnh
   ── -4 SD ─────────────────  ← cực đoan, chỉ khi có confluence HTF
```

### Mục đích trong ICT
- **Đặt target thực tế** sau khi đã có [[21 - Market Structure Shift]] + displacement: biết chốt lời ở đâu thay vì "đoán đỉnh/đáy".
- **Dự đoán nơi nhịp expansion kết thúc**: phiên trending thường dừng quanh -2 / -2.5 SD nếu trùng liquidity.
- **Tạo confluence**: khi một mức SD lined up với liquidity pool / FVG HTF → đó là draw on liquidity xác suất cao.

### Vì sao quan trọng
- Phần lớn lỗi quản trị lệnh ICT nằm ở **chốt lời quá sớm hoặc giữ quá lâu**. SD cho một khung target khách quan dựa trên chính cấu trúc của thị trường (manipulation leg), không phải con số tròn tùy hứng.
- Nó kết nối **manipulation (Judas)** với **expansion (target)** — đúng tinh thần AMD/PO3 (accumulation → manipulation → distribution).

### Nó giúp trả lời câu hỏi nào trên chart?
- Sau displacement, **giá có khả năng draw tới đâu** (target / liquidity)?
- Nhịp expansion này **còn dư địa** tới mức nào trước khi cạn?
- Mức target nào có **confluence** (trùng liquidity/FVG/PD-array HTF) để ưu tiên?
- Nên đặt **TP từng phần** ở đâu (-1, -2, -2.5 SD…)?

### Standard Deviation không phải là gì
- **Không phải** tín hiệu entry — nó là công cụ **target/projection**, không cho phép vào lệnh.
- **Không phải** độ lệch chuẩn thống kê (Bollinger Bands) — đây là **bội số đối xứng của một swing**, vẽ thủ công, không tính từ phân phối dữ liệu.
- **Không phải** mức đảo chiều chắc chắn — giá có thể xuyên qua hoặc dừng sớm; cần xác nhận cấu trúc.
- **Không phải** thứ dùng được trong range/choppy — chỉ có ý nghĩa khi có manipulation leg + displacement rõ ràng.
- **Không phải** mức neo tùy ý — neo sai swing thì mọi mức chiếu sai theo.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái

| Mức SD | Ý nghĩa thực chiến | Hàm ý |
|---|---|---|
| **-1 SD** | Target gần nhất, đối xứng 1:1 với manipulation leg | TP1 an toàn; thường đạt cả trong phiên thường |
| **-2 SD** | Target "tiêu chuẩn" của một nhịp expansion lành mạnh | TP chính; hay trùng draw on liquidity HTF |
| **-2.5 SD** | Mở rộng nhẹ; phiên có động lượng tốt | TP2 / runner một phần |
| **-3 SD** | Phiên trending mạnh, displacement lớn | Chỉ kỳ vọng khi có news/expansion rõ |
| **-4 SD** | Cực đoan, hiếm | Chỉ tin khi trùng PD-array/liquidity HTF mạnh |

### Khi nào giá trị cao? (checklist)
- [ ] Đã có **manipulation leg rõ** (Judas swing quét [[19 - Liquidity]]) để neo.
- [ ] Đã có **displacement + [[21 - Market Structure Shift]]** xác nhận hướng.
- [ ] Một mức SD **trùng** liquidity pool / [[Fair Value Gap]] HTF / biên [[12 - Dealing Range]].
- [ ] Đồng hướng [[12 - Daily Bias]] và đúng phía [[27 - Premium Discount]].
- [ ] Nhịp diễn ra trong [[18 - Kill Zones]] (London / NY) — expansion đáng tin hơn.

### Khi nào bỏ qua? (checklist)
- [ ] Không có manipulation leg rõ để neo (giá đi loằng ngoằng, không sweep).
- [ ] Thị trường đang **range/choppy**, không có displacement.
- [ ] Không mức SD nào trùng liquidity/PD-array → projection treo lơ lửng, ít nghĩa.
- [ ] Đang định dùng SD để **vào lệnh** (sai mục đích — SD là target).
- [ ] Neo phải "ép" vào một swing tùy ý để các con số đẹp lên.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Manipulation leg xác định**: một swing đã quét thanh khoản (high/low) ngay trước displacement.
2. **Displacement + MSS**: nhịp mạnh phá cấu trúc, xác nhận hướng expansion.
3. **Bộ mức SD được chiếu** (-1, -2, -2.5, -3, -4) từ leg tham chiếu.
4. **Confluence**: ít nhất một mức SD trùng liquidity pool / FVG HTF / biên dealing range.
5. **Phản ứng lịch sử** quanh các mức tương tự (giá hay dừng/đảo gần -2 SD trong market đó).

### Ma trận nhận diện

| Yếu tố | SD projection đáng tin | SD projection yếu / bỏ qua |
|---|---|---|
| Đoạn neo | Manipulation/Judas leg rõ, có sweep | Swing tùy ý, không sweep |
| Displacement | Mạnh, kèm MSS | Không có displacement / range |
| Confluence | Mức SD trùng liquidity/FVG/PD-array HTF | Mọi mức treo giữa khoảng trống |
| Vị trí | Đúng premium/discount cho hướng | Sai phía dealing range |
| Bias | Đồng hướng Daily Bias | Ngược bias chưa đổi |
| Thời điểm | Expansion trong kill zone | Ngoài kill zone / thanh khoản thấp |

### Điều kiện bắt buộc (must-have)
- [ ] Xác định đúng **manipulation leg** (sweep liquidity) làm đoạn tham chiếu.
- [ ] Có **displacement + MSS** xác nhận hướng trước khi chiếu SD.
- [ ] Chiếu đủ bộ mức **-1, -2, -2.5, -3, -4 SD** và đánh dấu rõ.

### Tăng xác suất (nice-to-have)
- [ ] Một mức SD trùng [[19 - Liquidity]] pool (BSL/SSL) đã thấy trước.
- [ ] Mức SD trùng [[Fair Value Gap]] HTF hoặc Order Block đối nghịch.
- [ ] Mức SD trùng biên premium/discount của [[12 - Dealing Range]].
- [ ] Đồng hướng [[12 - Daily Bias]]; expansion trong [[18 - Kill Zones]].

### Làm yếu đi (warning)
- [ ] Neo vào swing không sweep / tùy ý.
- [ ] Không mức SD nào có confluence.
- [ ] Thị trường range, displacement yếu.
- [ ] News lớn override khiến giá chạy bất chấp các mức chiếu.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Bias & Narrative
1. Xác định [[12 - Daily Bias]] và [[12 - Dealing Range]] HTF; giá đang premium hay discount (xem [[27 - Premium Discount]]).
2. Đánh dấu **draw on liquidity HTF** (BSL/SSL, FVG lớn) — đây là nơi SD nên "hạ cánh".
3. Ghi nhận manipulation leg cấp HTF nếu có (ví dụ Judas của phiên/ngày) để chiếu SD khung lớn làm target tổng.

### H1 / M15 — POI & Lập kế hoạch target
1. Khi displacement + MSS xuất hiện, **neo SD vào manipulation leg** vừa quét thanh khoản.
2. Chiếu -1, -2, -2.5, -3, -4 SD; **đối chiếu từng mức với liquidity/FVG HTF** đã đánh dấu ở bước D1/H4.
3. Chốt mức confluence cao nhất làm **target chính**; các mức khác làm TP từng phần.

### M5 / M1 — Quản trị lệnh theo SD
1. Entry vẫn theo mô hình chuẩn ([[20 - Liquidity Sweep]] → MSS → [[Fair Value Gap]]/OB) — **SD không quyết định entry**.
2. Đặt **TP từng phần** tại -1 / -2 / -2.5 SD; dời SL về BE sau -1 SD.
3. Tại mỗi mức SD trùng liquidity, quan sát phản ứng (rejection / chậm lại) để quyết định chốt nốt hay giữ runner.

```text
[LONG — chiếu SD sau MSS bullish]
- HTF: bias bullish, giá ở discount; draw on liquidity là BSL/FVG phía trên [level]
- Manipulation leg (anchor): sweep SSL → low [level] → high [level]
- Entry: theo mô hình (sweep + MSS + FVG), KHÔNG vào tại mức SD
- Chiếu SD lên: -1 SD [level] | -2 SD [level] | -2.5 SD [level] | -3 SD [level]
- Confluence: -2 SD trùng BSL/FVG HTF [level] = target chính
- TP1: -1 SD [level]  TP2: -2 SD [level]  Runner: -2.5/-3 SD nếu trending
- SL: dưới điểm sweep / swing low [level]
```

```text
[SHORT — chiếu SD sau MSS bearish]
- HTF: bias bearish, giá ở premium; draw on liquidity là SSL/FVG phía dưới [level]
- Manipulation leg (anchor): sweep BSL → high [level] → low [level]
- Entry: theo mô hình (sweep + MSS + FVG), KHÔNG vào tại mức SD
- Chiếu SD xuống: -1 SD [level] | -2 SD [level] | -2.5 SD [level] | -3 SD [level]
- Confluence: -2 SD trùng SSL/FVG HTF [level] = target chính
- TP1: -1 SD [level]  TP2: -2 SD [level]  Runner: -2.5/-3 SD nếu trending
- SL: trên điểm sweep / swing high [level]
```

> [!warning]
> SD là công cụ **target**, không phải entry. Tuyệt đối **không đặt lệnh limit mù tại một mức SD** với kỳ vọng nó đảo chiều. Mọi entry vẫn phải qua chuỗi sweep → MSS → FVG/OB. SD chỉ trả lời "đi tới đâu", không trả lời "vào ở đâu".

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup hợp lệ (✓) — để DÙNG SD làm target
- [ ] Có manipulation leg rõ (sweep liquidity) để neo.
- [ ] Có displacement + [[21 - Market Structure Shift]] xác nhận hướng.
- [ ] Ít nhất một mức SD có **confluence** (liquidity/FVG/PD-array HTF).
- [ ] Đồng hướng [[12 - Daily Bias]], đúng premium/discount.
- [ ] Entry độc lập đã hợp lệ (SD chỉ dùng để đặt target/TP).

### Projection bị vô hiệu (✗)
- [ ] Neo vào swing không sweep / tùy ý → mức chiếu vô nghĩa.
- [ ] Không mức nào có confluence → projection treo lơ lửng.
- [ ] Giá đóng nến **xuyên qua mức SD + draw on liquidity** mà không phản ứng → target đó "hết hiệu lực", chuyển sang mức kế tiếp.
- [ ] Thị trường range / displacement yếu → không chiếu SD.
- [ ] News lớn làm giá chạy bất chấp các mức.

| Tiêu chí | Giữ projection (hợp lệ) | Hủy / chuyển mức |
|---|---|---|
| Đoạn neo | Manipulation leg có sweep | Swing tùy ý, không sweep |
| Confluence | SD trùng liquidity/FVG/PD-array | Treo giữa khoảng trống |
| Phản ứng tại mức | Rejection / chậm lại rõ | Đóng nến xuyên thẳng |
| Bias / vị trí | Đồng hướng, đúng P/D | Ngược bias / sai phía |

> [!note]
> Một mức SD bị "xuyên qua" **không có nghĩa projection sai** — nó có nghĩa target dịch sang **mức SD kế tiếp** (ví dụ -2 SD bị phá → kỳ vọng -2.5 / -3 SD). Đây là lý do nên chiếu cả bộ mức ngay từ đầu thay vì chỉ một mức.

### Nâng cao — Chọn đúng manipulation leg khi có NHIỀU ứng viên (session Judas vs daily Judas vs weekly Judas)

Trên cùng một chart, tại cùng một thời điểm, thường tồn tại **nhiều manipulation leg lồng nhau ở nhiều quy mô khác nhau**: một cú Judas swing nhỏ quanh giờ mở phiên trên M15, một cú Judas cấp ngày trên H1 (quét thanh khoản của ngày hôm trước), và một cú Judas cấp tuần trên H4/D1 (quét thanh khoản của tuần trước). Cả ba đều là manipulation leg "hợp lệ" theo định nghĩa (đều có sweep + displacement sau đó) — nhưng chúng **không tương đương nhau**, và neo SD vào sai tầng sẽ cho ra các mức chiếu chênh lệch nhau rất lớn, thậm chí mâu thuẫn hướng kỳ vọng ngắn hạn so với dài hạn.

Vấn đề thực chiến: một trader đang tìm entry intraday (giữ lệnh vài giờ trong phiên) nhưng lại chiếu SD từ manipulation leg cấp tuần sẽ nhận về các mức target cách xa hàng trăm point — không bao giờ đạt được trong phiên, khiến TP đặt sai và quản trị lệnh rối loạn. Ngược lại, một trader đang giữ swing đa ngày nhưng chỉ chiếu SD từ Judas leg của một phiên London sẽ có target quá gần, chốt lời non trong khi cấu trúc lớn còn nhiều dư địa.

**Quy tắc phân tầng: quy mô anchor phải khớp quy mô trade đang cầm.** Nếu bạn đang trade intraday (vào và thoát trong ngày), neo SD vào manipulation leg cấp session (Judas quét thanh khoản đầu phiên Á/London/NY trên M15-M5). Nếu bạn đang trade theo cấu trúc trong ngày nhưng kỳ vọng giữ 1-2 ngày, neo vào Judas cấp ngày (quét PDH/PDL trên H1). Nếu bạn đang trade swing đa ngày/tuần theo bias HTF, neo vào Judas cấp tuần (quét thanh khoản tuần trước trên H4/D1).

![[StandardDeviation-Advanced-Manipulation-Tiers.svg]]
*Ba manipulation leg lồng nhau trên cùng một price path: leg session (đỏ, M15) cho ladder SD nhỏ dùng cho target intraday; leg daily (cam, H1) cho ladder trung bình dùng cho target swing 1-2 ngày; leg weekly (xanh, H4/D1) cho ladder lớn dùng cho target đa ngày/tuần. Chọn sai tầng anchor sẽ cho target lệch hẳn quy mô trade đang cầm.*

| Trade horizon | Manipulation leg nên anchor | Khung thời gian xem leg | Typical SD target scale |
|---|---|---|---|
| Scalp / intraday (thoát trong phiên) | Session Judas (quét liquidity đầu phiên Á/London/NY) | M15 / M5 | Vài chục point NQ1, vài pip EURUSD — target trong phiên |
| Day trade giữ 1-2 ngày | Daily Judas (quét PDH/PDL, liquidity ngày hôm trước) | H1 | Trăm point NQ1, vài chục pip — target qua đêm/vài phiên |
| Swing đa ngày / theo tuần | Weekly Judas (quét liquidity tuần trước, thường quanh Sunday/Monday range) | H4 / D1 | Vài trăm đến nghìn point NQ1, hàng chục-trăm pip — target đa ngày/tuần |

> [!tip]
> Khi không chắc nên dùng tầng nào, hỏi: **"Tôi định giữ lệnh này bao lâu?"** — câu trả lời quyết định tầng manipulation leg cần neo. Ghi rõ `anchor_scale: session|daily|weekly` trong journal để sau này đối chiếu xem tầng nào cho tỷ lệ giá "tới đích" cao nhất với phong cách trade của bạn.

### Nâng cao — SD kết hợp với Liquidity Void: đoạn giá đi nhanh qua vùng trống thanh khoản

Một chi tiết hay bị bỏ qua khi quản trị lệnh theo SD: **tốc độ giá tiếp cận một mức SD phụ thuộc vào cấu trúc giá nằm giữa entry và mức đó**, không chỉ vào bản thân mức SD. Khi một mức chiếu (ví dụ -2 SD) rơi vào hoặc ngay sau một **liquidity void** — một FVG lớn hoặc một vùng gần như không có nến/wick cũ (ít lệnh chờ, ít người mắc kẹt) — giá thường **lướt qua rất nhanh và ít bị cản** so với khi phải "cày" qua một vùng dày đặc cấu trúc cũ (consolidation, nhiều wick, nhiều order block chồng lấn).

Hệ quả: một nhịp displacement hướng tới mức -2/-2.5 SD nằm sau một liquidity void thường trông như một cú "tăng tốc đột ngột" thay vì một nhịp trườn đều. Nhiều trader mới thấy giá chạy nhanh bất thường liền hoảng và **chốt lời non** vì nghĩ "giá chạy quá nhanh chắc sắp đảo" — trong khi thực ra đó chỉ là hành vi bình thường khi đi qua vùng trống thanh khoản, và target thật (nơi có confluence) còn ở xa hơn.

Hàm ý quản trị lệnh cụ thể:
- **Trước khi hoảng vì tốc độ giá, kiểm tra cấu trúc phía trước:** nếu đoạn giữa giá hiện tại và mức SD mục tiêu là một liquidity void / FVG lớn chưa lấp, kỳ vọng một cú di chuyển nhanh là BÌNH THƯỜNG — không phải tín hiệu đảo chiều.
- **Ngược lại, nếu giá phải đi qua vùng dày cấu trúc cũ** (nhiều đỉnh/đáy nội bộ, order block chồng lấn) mà lại **chậm lại hoặc dừng sớm** trước khi chạm mức SD kỳ vọng, đó mới là dấu hiệu đáng chú ý — có thể là exhaustion, nên cân nhắc chốt một phần thay vì chờ đủ mức.
- **Đừng dùng "tốc độ giá" một mình làm lý do thoát lệnh.** Luôn đối chiếu với: (1) đoạn phía trước là void hay dense structure, (2) đã có phản ứng thật (rejection/MSS ngược) tại mức nào chưa.

| Cấu trúc phía trước mức SD | Kỳ vọng tốc độ | Hành vi quản trị lệnh hợp lý |
|---|---|---|
| Liquidity void / FVG lớn chưa lấp | Nhanh, ít cản trở | Giữ runner, không hoảng vì tốc độ; target thật vẫn ở xa hơn |
| Vùng dày đặc cấu trúc cũ (consolidation, nhiều OB) | Chậm, dễ giằng co | Bình thường nếu vẫn tiến; đáng ngờ nếu dừng hẳn giữa chừng |
| Giá chậm lại sớm bất thường trong một void | Không khớp kỳ vọng | Cảnh báo exhaustion — cân nhắc chốt một phần |
| Giá tăng tốc bất thường qua vùng dày cấu trúc | Không khớp kỳ vọng (hiếm, thường do tin tức) | Kiểm tra news; có thể là breakout thật, không phải nhiễu |

> [!warning]
> Đừng nhầm "giá đi nhanh" với "giá sắp hết đà". Một cú di chuyển nhanh qua liquidity void là dấu hiệu **market đang làm đúng việc nó nên làm** (không có ai chặn đường); nó không tự động có nghĩa là gần target. Chỉ tin vào phản ứng thật (rejection có cấu trúc) tại một mức SD có confluence, không tin vào cảm giác "chạy nhanh quá rồi".

### Nâng cao — SD Projection vs Fibonacci Extension truyền thống: giống và khác nhau ở đâu

Về mặt cơ chế, SD Projection của ICT gần như giống hệt một **Fibonacci trend-based extension** cổ điển: cả hai đều lấy một đoạn giá tham chiếu (leg) rồi chiếu các bội số của nó ra phía trước để ước lượng target. Công cụ vẽ trên phần mềm charting thậm chí thường là cùng một công cụ ("trend-based Fib extension" / "Fib projection"). Vì vậy nhiều người mới học dễ nghĩ SD chỉ là "fib extension đổi tên".

**Khác biệt cốt lõi nằm ở việc CHỌN LEG NÀO làm tham chiếu, chứ không nằm ở phép toán.** Fib extension truyền thống thường lấy **nhịp swing gần nhất, dễ thấy nhất** của cú di chuyển hiện tại (ví dụ: swing A-B-C gần đây nhất trên chart) — tiêu chí chọn chủ yếu là **độ rõ ràng và độ mới** của swing. Trong khi đó, SD Projection của ICT **cố tình neo vào manipulation/Judas leg** — đoạn giá đại diện cho "lời nói dối" trước khi thị trường tiết lộ "sự thật" (displacement thật). Tiêu chí chọn ở đây không phải là swing to nhất hay mới nhất, mà là swing **có ý nghĩa tường thuật** (narrative): nó phải là đoạn quét thanh khoản, gài bẫy phe yếu, trước khi giá đảo hướng thật.

Vì hai công cụ đo cùng một kiểu bội số nhưng trên hai đoạn tham chiếu khác nhau, chúng thường cho ra **các mức target khác nhau** trên cùng một chart. Một số trader ICT tận dụng chính sự khác biệt này: **vẽ cả hai** — một fib extension cổ điển trên nhịp swing gần nhất VÀ một SD projection trên manipulation leg — rồi xem hai bộ mức có **trùng nhau ở đâu**. Vùng mà cả hai ladder hội tụ (thường lệch nhau một chút vì đo trên hai leg khác nhau, nhưng có thể rơi gần nhau) được xem là **confluence rất mạnh**, vì hai phương pháp đo độc lập cùng chỉ về một vùng giá.

![[StandardDeviation-Advanced-vs-FibExtension.svg]]
*Hai ladder chiếu trên cùng một price path: "Fib Extension" (xanh lá, neo trên nhịp swing gần nhất — tiêu chí là độ mới/độ rõ) và "ICT SD Projection" (xanh dương, neo trên manipulation/Judas leg — tiêu chí là ý nghĩa liquidity engineering). Vùng hai ladder gần trùng nhau (khung vàng) là confluence mạnh hơn hẳn so với khi chỉ một công cụ đứng riêng lẻ.*

| Tiêu chí | Fibonacci Extension truyền thống | ICT SD Projection |
|---|---|---|
| Logic đo | Bội số đối xứng của một leg tham chiếu | Bội số đối xứng của một leg tham chiếu (giống) |
| Tiêu chí chọn leg | Swing gần nhất / rõ nhất của nhịp hiện tại | Manipulation/Judas leg — đoạn quét thanh khoản trước displacement thật |
| Ý nghĩa của leg | Kỹ thuật thuần túy (kích thước, vị trí) | Narrative (liquidity engineering — "lie" trước "truth") |
| Use-case điển hình | Target cho bất kỳ nhịp trending nào | Target sau khi đã xác nhận AMD (accumulation-manipulation-distribution) |
| Cách dùng kết hợp | Vẽ song song với SD, tìm vùng hai ladder trùng nhau | Vẽ song song với fib ext, ưu tiên mức có cả hai xác nhận |

> [!example]
> Nếu -2 SD (neo trên manipulation leg) và mức fib 1.618 extension (neo trên nhịp swing gần nhất) cùng rơi vào một vùng giá cách nhau vài point/pip, đó là tín hiệu confluence mạnh hơn nhiều so với việc chỉ có một trong hai mức đứng đơn độc — ghi lại các trường hợp này trong journal để đo xem confluence kép có thực sự nâng cao win-rate so với chỉ dùng một công cụ.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[StandardDeviation-Example-Correct.svg]]

**Mô tả:**
- Trong NY KZ, giá quét SSL (Judas swing xuống) tạo manipulation leg từ high [level] → low [level], rồi displacement tăng + MSS bullish.
- Neo SD vào chính manipulation leg đó; chiếu -1, -2, -2.5, -3 SD lên trên.
- **-2 SD trùng** một BSL/FVG HTF chưa lấp [level] → đặt làm target chính.
- Entry thực hiện theo mô hình (sweep + MSS + FVG), TP1 tại -1 SD [level], TP2 tại -2 SD [level].

**Vì sao đây là ví dụ tốt:**
- Neo đúng vào manipulation leg đã sweep liquidity, không phải swing tùy ý.
- Có displacement + MSS xác nhận hướng trước khi chiếu SD.
- Target chính (-2 SD) có **confluence** với draw on liquidity HTF.
- SD chỉ dùng để **đặt TP**, entry vẫn theo cấu trúc — đúng vai trò của công cụ.

### Ví dụ sai
![[StandardDeviation-Example-Wrong.svg]]

**Mô tả:**
- Trader neo SD vào một swing **không hề sweep liquidity** (chọn đại một đoạn để con số "đẹp").
- Đặt lệnh limit mù tại -2 SD kỳ vọng giá đảo chiều, không chờ MSS/xác nhận.
- Giá đóng nến **xuyên thẳng qua -2 SD và -3 SD** vì không mức nào có confluence; lệnh dính SL.

**Bài học:**
- Neo SAI swing (không sweep) → mọi mức chiếu vô nghĩa.
- SD là **target**, không phải entry — không đặt limit mù tại mức SD.
- Mức SD không có confluence (liquidity/FVG/PD-array) thì không đáng tin.
- Luôn chờ cấu trúc (sweep + MSS) xác nhận trước khi tin vào projection.

### Giải phẫu SD Projection
![[StandardDeviation-Anatomy.svg]]

**Mô tả:** Sơ đồ chú thích manipulation leg (anchor A→B), hướng displacement, và bộ mức -1/-2/-2.5/-3/-4 SD; đánh dấu mức nào trùng liquidity pool / FVG HTF làm target chính.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning]
> SD chỉ dùng khi đã có manipulation leg + displacement. Không có anchor hợp lệ → **không chiếu SD**, và không bao giờ dùng SD làm tín hiệu vào lệnh.

### A. Context (anchor & hướng)
- [ ] Có manipulation/Judas leg đã **sweep liquidity** để neo.
- [ ] Có displacement + [[21 - Market Structure Shift]] xác nhận hướng.
- [ ] [[12 - Daily Bias]] rõ ràng, đúng phía [[27 - Premium Discount]].
- [ ] Đã đánh dấu draw on liquidity HTF (BSL/SSL/FVG).

### B. Projection & target
- [ ] Neo SD đúng vào manipulation leg (không tùy ý).
- [ ] Chiếu đủ bộ -1, -2, -2.5, -3, -4 SD.
- [ ] Ít nhất một mức SD **trùng liquidity/FVG/PD-array HTF** → target chính.
- [ ] Kế hoạch TP từng phần theo các mức SD; SL theo cấu trúc (không theo SD).

### C. "Không dùng SD" khi
- [ ] Không có manipulation leg / không sweep.
- [ ] Thị trường range, displacement yếu.
- [ ] Không mức nào có confluence.
- [ ] Đang định dùng SD để **vào lệnh** (sai mục đích).

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Neo sai swing | Chọn đại một đoạn để số "đẹp" | Mọi mức chiếu vô nghĩa | Chỉ neo vào manipulation leg đã sweep liquidity |
| Dùng SD làm entry | Đặt limit mù tại mức SD | SD là target, không phải tín hiệu vào | Entry qua sweep+MSS+FVG; SD chỉ để TP |
| Coi mức SD là đảo chiều chắc chắn | Kỳ vọng giá phải quay đầu tại -2 SD | Giá có thể xuyên qua | Chờ xác nhận cấu trúc; chuyển mức kế nếu phá |
| Bỏ qua confluence | Tin mức SD treo giữa khoảng trống | Xác suất thấp | Chỉ ưu tiên mức trùng liquidity/FVG/PD-array HTF |
| Bỏ qua context HTF | Chiếu SD ngược bias / sai P/D | Target đi ngược draw thật | Luôn đặt SD trong bias + dealing range HTF |
| Over-project trong range | Chiếu -3/-4 SD khi thị trường đi ngang | Target ảo, không bao giờ tới | Chỉ chiếu khi có displacement rõ |
| Chỉ vẽ một mức | Chỉ đánh dấu -2 SD | Mất bản đồ khi giá phá mức đó | Chiếu cả bộ -1→-4 để biết mức kế tiếp |

---

## 10. Câu hỏi tự kiểm tra
- SD là công cụ để **vào lệnh** hay để **đặt target**? Vì sao?
- Đoạn nào nên được chọn làm anchor khi chiếu SD, và vì sao là đoạn đó?
- Các mức SD thường dùng là gì, và -2 SD thường mang ý nghĩa thực chiến nào?
- Điều gì biến một mức SD từ "treo lơ lửng" thành "đáng tin"?
- Khi giá đóng nến xuyên qua -2 SD, điều đó nói lên gì về target?
- Vì sao không nên dùng SD trong thị trường range/choppy?
- SD ghép vào [[ICT 2022 Model]] ở khâu nào — entry hay quản trị lệnh?

---

## 11. Flashcards / Active Recall
- **Q1:** Standard Deviation Projection dùng để làm gì?
  → A1: DỰ PHÓNG nơi giá có khả năng đi tới (target / draw on liquidity) sau một swing đã xác định; là công cụ target, không phải entry.
- **Q2:** Anchor (đoạn tham chiếu) nên đặt vào đâu?
  → A2: Vào chân manipulation/Judas swing đã quét thanh khoản, ngay trước displacement.
- **Q3:** Các mức SD thường dùng?
  → A3: -1, -2, -2.5, -3, -4 SD (chiếu bằng fib trend-based extension / projection).
- **Q4:** Điều gì làm một mức SD đáng tin?
  → A4: Khi mức đó trùng (confluence) với liquidity pool, FVG đối nghịch, hoặc PD-array / biên dealing range HTF.
- **Q5:** Khi giá xuyên qua một mức SD thì sao?
  → A5: Target dịch sang mức SD kế tiếp (vd -2 SD phá → kỳ vọng -2.5/-3 SD); projection không "sai", chỉ chuyển mức.
- **Q6:** Ba lỗi chí mạng khi dùng SD?
  → A6: (1) neo sai swing không sweep; (2) dùng SD làm entry/đặt limit mù; (3) tin mức SD không có confluence.
---

## 13. Lesson Learned
> [!example] Ghi nhận khi áp dụng thực tế
> - Bối cảnh: ____
> - Manipulation leg neo (A→B): [level] → [level]
> - Các mức SD chiếu (-1/-2/-2.5/-3): [level] / [level] / [level] / [level]
> - Mức SD có confluence (target chính): [level]
> - Phản ứng quan sát được tại các mức: ____
> - Kết quả (R-multiple): ____
> - Điều làm đúng: ____
> - Điều cần sửa: ____
> - Liên kết tới [[Mistake - ...]] nếu có: ____

---

## Best Practices

> [!success] Nguyên tắc vàng
> **SD chỉ trả lời "giá đi tới đâu", không bao giờ trả lời "vào lệnh ở đâu."** Toàn bộ giá trị của công cụ này sụp đổ nếu neo sai swing (không sweep) hoặc nếu bạn biến nó thành tín hiệu entry — hai lỗi này gộp lại là nguyên nhân của gần như mọi lệnh thua liên quan đến SD trong journal. Chỉ tin một mức SD khi nó vừa được neo đúng vào manipulation leg, vừa có confluence thật với liquidity/FVG/PD-array.

1. **Không bao giờ dùng SD như tín hiệu entry.** SD là công cụ target/projection — nó cho biết nơi giá có khả năng đi tới, không phải nơi nên vào lệnh. Entry luôn phải đến từ chuỗi sweep → [[21 - Market Structure Shift]] → [[Fair Value Gap]]/OB độc lập với các mức SD. Đặt lệnh limit mù tại một mức SD (như trong "Ví dụ sai" ở mục 6) là lỗi khiến trader bỏ qua toàn bộ xác nhận cấu trúc.

2. **Luôn neo vào một manipulation leg đã thực sự quét thanh khoản — không bao giờ là một swing tiện tay.** Trước khi vẽ SD, tự hỏi: đoạn A→B này có sweep [[19 - Liquidity]] (BSL/SSL) thật không, hay mình chỉ đang chọn một đoạn để các con số "nhìn đẹp"? Nếu không chắc, chạy phép thử tương tự phép thử sweep dùng trong [[22 - Mitigation Block]] và [[04 - Breaker Block]]: xem body/close có thực sự vượt qua đỉnh/đáy cũ hay chỉ là wick.

3. **Khớp quy mô anchor với quy mô trade đang cầm** (xem mục "Nâng cao — Chọn đúng manipulation leg" ở mục 5). Trade intraday neo vào Judas leg cấp session; trade giữ 1-2 ngày neo vào Judas cấp ngày; swing đa ngày/tuần neo vào Judas cấp tuần. Ghi trường `anchor_scale` trong journal để không lẫn lộn giữa các quy mô khi review.

4. **Chỉ tin những mức SD có confluence thật — bỏ qua các mức "treo lơ lửng".** Một mức SD đứng một mình giữa khoảng trống giá không có giá trị dự báo cao hơn một con số tròn ngẫu nhiên. Chỉ nâng mức đó lên thành target chính khi nó trùng với một liquidity pool, một [[Fair Value Gap]] đối nghịch, hoặc biên [[12 - Dealing Range]] / [[27 - Premium Discount]] đã đánh dấu từ trước ở khung HTF.

5. **Nhận diện liquidity void trước khi phản ứng với tốc độ giá.** Khi giá lướt nhanh bất thường về phía một mức SD xa, kiểm tra xem đoạn phía trước có phải một FVG lớn / vùng trống thanh khoản hay không (xem mục "Nâng cao — SD kết hợp với Liquidity Void"). Di chuyển nhanh qua void là bình thường; đừng chốt lời non chỉ vì giá "chạy nhanh quá". Ngược lại, dừng sớm bất thường khi đi qua vùng dày cấu trúc mới là tín hiệu đáng ngờ.

6. **Luôn chiếu cả bộ ladder (-1 đến -4 SD) ngay từ đầu, không chỉ một mức.** Khi một mức bị đóng nến xuyên qua mà không có phản ứng, target không "sai" — nó dịch sang mức kế tiếp. Có sẵn cả bộ mức giúp bạn phản ứng ngay (dời TP, giữ runner) thay vì phải vẽ lại giữa lúc thị trường đang di chuyển.

7. **Cân nhắc vẽ thêm một fib extension cổ điển trên nhịp swing gần nhất để đối chiếu** (xem mục "Nâng cao — SD Projection vs Fibonacci Extension"). Vùng mà cả hai công cụ đo độc lập cùng hội tụ là confluence mạnh hơn một công cụ đứng một mình — đặc biệt hữu ích khi manipulation leg không thật sự rõ ràng.

8. **Backtest tối thiểu 15-20 mẫu trước khi tin cậy hoàn toàn vào SD**, ghi lại trong journal: chất lượng anchor leg (có sweep rõ hay mơ hồ), mức SD nào thực sự có confluence, và mức SD nào giá thực sự dừng/đảo. Thống kê theo từng thị trường (NQ1/NDX, EURUSD, GBPUSD, XAUUSD) vì hành vi tại các mức SD có thể khác nhau đáng kể giữa index và forex. Đối chiếu kết quả với [[02 - Skill Metrics]] và cập nhật `confidence` của note này sau mỗi đợt review.