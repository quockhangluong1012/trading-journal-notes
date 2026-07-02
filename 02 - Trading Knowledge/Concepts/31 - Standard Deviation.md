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
status: seed
category: Time & Price
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[ICT 2022 Model]]"
importance: 4
confidence: 1
last_reviewed:
created: 2026-06-26
updated: 2026-06-26
related_concepts:
  - "[[19 - Liquidity]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[27 - Premium Discount]]"
  - "[[12 - Dealing Range]]"
  - "[[12 - Daily Bias]]"
  - "[[18 - Kill Zones]]"
prerequisites:
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[12 - Dealing Range]]"
common_mistakes: []
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

---

## 6. Ví dụ chart

### Ví dụ đúng
![[StandardDeviation-Example-Correct.png]]

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
![[StandardDeviation-Example-Wrong.png]]

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
![[StandardDeviation-Anatomy.png]]

**Mô tả:** Sơ đồ chú thích manipulation leg (anchor A→B), hướng displacement, và bộ mức -1/-2/-2.5/-3/-4 SD; đánh dấu mức nào trùng liquidity pool / FVG HTF làm target chính.

---

## 7. Entry model liên quan

- [[ICT 2022 Model]] — sweep → MSS → FVG entry; SD dùng để **đặt target** cho lệnh đã vào.
- [[20 - Liquidity Sweep]] — tạo manipulation leg để neo SD.
- [[21 - Market Structure Shift]] — xác nhận hướng expansion trước khi chiếu SD.
- [[Fair Value Gap]] — vừa là entry array (sau MSS) vừa là confluence cho mức SD target.
- [[19 - Liquidity]] — các pool (BSL/SSL) là nơi mức SD nên "hạ cánh".
- [[12 - Dealing Range]] / [[27 - Premium Discount]] — biên range thường trùng mức SD đáng tin.
- [[12 - Daily Bias]] — xác định hướng để chiếu SD đúng phía.

```text
[Chuỗi triển khai chuẩn — SD làm target]
1. HTF: Daily Bias + Dealing Range + đánh dấu draw on liquidity (BSL/SSL/FVG)
2. Chờ manipulation/Judas leg quét liquidity trong kill zone
3. Displacement + MSS xác nhận hướng → vào lệnh theo mô hình (sweep+MSS+FVG)
4. Neo SD vào manipulation leg; chiếu -1/-2/-2.5/-3/-4 SD
5. Đối chiếu mức SD với liquidity/FVG HTF → chọn target chính (confluence cao nhất)
6. TP từng phần tại các mức SD; dời SL BE sau -1 SD; runner tới -2.5/-3 SD nếu trending
```

> [!note]
> SD ghép tốt nhất với [[ICT 2022 Model]] ở **khâu quản trị lệnh / target**, không phải khâu entry. Entry do sweep + MSS + FVG quyết định; SD chỉ giúp biết chốt lời ở đâu cho hợp lý và khớp với draw on liquidity.

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
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

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

## 14. Mức độ thành thạo

| Tiêu chí | Điểm (1–5) | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa & cách chiếu | ____ | SD là target, không phải entry? |
| Neo đúng manipulation leg | ____ | Có chọn đúng swing đã sweep không? |
| Đọc confluence của mức SD | ____ | Có đối chiếu liquidity/FVG/PD-array HTF? |
| Quản trị TP theo SD | ____ | TP từng phần tại -1/-2/-2.5 SD? |
| Tích hợp vào ICT 2022 Model | ____ | Dùng ở khâu target, không phải entry? |
| Kỷ luật không trade mù tại SD | ____ | Có chờ cấu trúc xác nhận không? |

**Kế hoạch ôn tập:**
- [ ] Backtest 15–20 lần: neo SD vào manipulation leg và ghi mức nào giá thực sự dừng (NQ1/NAS100 & EURUSD).
- [ ] Thống kê tần suất giá dừng tại -1 / -2 / -2.5 / -3 SD theo từng market.
- [ ] Đối chiếu: mức SD có confluence vs không confluence — mức nào "ăn" hơn.
- [ ] Cập nhật [[01 - Roadmap]] và [[02 - Skill Metrics]].
- [ ] Review lại note này sau 2 tuần, cập nhật `confidence` & `last_reviewed`.

---

## Appendix — Standard Deviation Quick Reference Card

> [!abstract] Thẻ tra nhanh SD Projection
> - **Bản chất:** Công cụ TARGET — chiếu bội số đối xứng của một swing để dự phóng draw on liquidity. KHÔNG phải entry.
> - **Anchor (manipulation leg):** A [level] → B [level]  (đã sweep liquidity? Yes/No)
> - **Displacement + MSS xác nhận hướng:** Yes / No
> - **Bias / vị trí:** Bullish / Bearish · Premium / Discount
> - **Mức chiếu:** -1 [level] · -2 [level] · -2.5 [level] · -3 [level] · -4 [level]
> - **Confluence (mức nào trùng liquidity/FVG/PD-array HTF):** ____
> - **Target chính (confluence cao nhất):** [level]
> - **TP từng phần:** TP1 -1 SD [level] · TP2 -2 SD [level] · Runner -2.5/-3 SD
> - **SL (theo cấu trúc, KHÔNG theo SD):** [level]
> - **Kill zone:** London / NY = ____
> - **Quy tắc vàng:** Neo đúng manipulation leg · Chỉ tin mức có confluence · Không bao giờ vào lệnh mù tại mức SD
> - **Liên quan:** [[ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[Fair Value Gap]] · [[19 - Liquidity]] · [[12 - Dealing Range]] · [[27 - Premium Discount]] · [[12 - Daily Bias]]
