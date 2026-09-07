---
type: market-analysis
concept: Nested Draw on Liquidity (D1 vs H1)
aliases:
  - Nested DOL
  - DOL lồng nhau D1-H1
  - Bias vs DOL confusion
tags:
  - trading/ict/analysis
  - trading/study
  - "#draw-on-liquidity"
  - "#daily-bias"
status: developing
category: Liquidity / Bias
created: 2026-07-27
updated: 2026-07-27
related:
  - "[[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]"
  - "[[12-Daily-Bias]]"
  - "[[27-Premium-Discount]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[07-Buy-side-Liquidity]]"
  - "[[30 - Sell-side Liquidity]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[01 - ICT 2022 Model|ICT 2022 Model]]"
---

# Nested DOL — Áp dụng D1 → H1 → M5 vào Bias hiện tại (HH/HL + EQH/EQL + PDH/PDL/PWH/PWL)

> [!summary] Tóm tắt 1 câu
> **DOL không phải một điểm cố định duy nhất — mỗi khung thời gian có Bias riêng và do đó có DOL riêng; DOL của khung nhỏ (H1) chỉ là trạm dừng tạm thời trên đường tới DOL của khung lớn (D1), miễn là Bias D1 chưa bị vô hiệu hóa.**

---

## 1. Bối cảnh phân tích (case cụ thể)

- **D1:** cấu trúc Higher High / Higher Low được xác nhận → **Bias D1 = Bullish**.
- Phía trên giá hiện tại: một **EQH mới hình thành** (hai đỉnh gần bằng nhau, chưa bị chạm/virgin).
- Giá hiện tại đang trong một **nhịp retrace (pullback)**.
- **H1:** trong chính nhịp pullback này, cấu trúc H1 đang cho **Bias H1 = Bearish** (đúng bản chất của một pullback — nội tại nó là một leg giảm bên trong xu hướng tăng lớn hơn).
- Gần giá hiện tại, phía dưới, có một **EQL** — pullback đang di chuyển hướng tới đó.

**Câu hỏi cốt lõi cần trả lời:** EQH phía trên và EQL phía dưới — cái nào là DOL? DOL có được dùng để xác định Bias không?

---

## 2. Trả lời trực tiếp 3 câu hỏi

### Q1 — D1 Bullish (HH/HL), DOL = EQH phía trên?
**Đúng.** Bias D1 Bullish → DOL D1 luôn nằm **đối diện phía bias**, tức phía trên → chính là vùng **EQH virgin** đó (Buy-side Liquidity). Đây là target lớn nhất, mục tiêu cuối cùng mà cả nhịp D1 đang được dẫn tới.

### Q2 — DOL có dùng làm điều kiện xác định Bias không?
**Không — chiều nhân quả chỉ đi một chiều:**

```text
Market Structure (HH/HL/LH/LL, MSS/BOS)  →  Bias  →  Bias xác định DOL nằm bên nào
```

DOL là **output** của bias, không phải **input**. Nếu dùng ngược lại — "thấy EQH lớn phía trên nên nghiêng Bullish" — đó là suy luận đảo chiều, dễ rơi vào confirmation bias vì **lúc nào cũng có pool ở cả hai phía** (trên và dưới). Chỉ nên dùng vị trí liquidity làm yếu tố phụ (tie-breaker) khi cấu trúc thực sự mơ hồ (range, chưa rõ HH/HL) — không bao giờ thay thế tín hiệu cấu trúc khách quan.

### Q3 — EQL phía dưới là SSL, không phải DOL — đúng chưa?
**Đúng xét theo D1** — DOL D1 vẫn là EQH phía trên, EQL đó chỉ là SSL đối lập bias D1.

**Nhưng thêm một lớp quan trọng:** xét theo **H1**, vì Bias H1 hiện tại là Bearish (đúng như bạn nói), nguyên tắc DOL áp dụng y hệt cho khung H1 → **DOL của H1 (cho riêng nhịp pullback này) chính là EQL đó.** Hai điều đúng cùng lúc, không mâu thuẫn:

| Khung | Bias | DOL của khung đó |
|---|---|---|
| D1 | Bullish (HH/HL) | EQH phía trên (BSL) — **target cuối** |
| H1 | Bearish (pullback) | EQL phía dưới (SSL) — **target tạm, trạm dừng** |

---

## 3. Sơ đồ Nested DOL

![[DOL-Nested-D1-H1.svg]]

**Đọc sơ đồ:** đường liền nét là cấu trúc HH/HL đã hình thành trên D1; điểm cam là giá hiện tại đang pullback về vùng EQL (DOL H1, mũi tên đỏ). Đường nét đứt xám là đường dự phóng — chỉ hợp lệ **sau khi** H1 sweep EQL + có MSS Bullish xác nhận quay lại hướng D1 (mũi tên xanh tới EQH — DOL D1).

---

## 4. Timeframe nào làm gì trong workflow D1 → H1 → M5

| Khung | Vai trò | Công cụ đang dùng |
|---|---|---|
| **D1** | Xác định Bias chính + **DOL chính (External Range Liquidity)** — target lớn nhất | HH/HL/LH/LL, EQH/EQL D1, PDH/PDL, PWH/PWL |
| **H1** | Xác định **DOL trung gian (Internal Range Liquidity)** — trạm dừng giá phải quét trước; tìm POI (OB/FVG/Breaker) quanh đó | Session high/low, H1 EQH/EQL, H1 swing gần nhất |
| **M5** | **Xác nhận** — chờ sweep pool nhỏ tại POI, rồi MSS + FVG để entry | MSS, FVG (2022 Model) |

Nguyên lý nền: DOL có tính **phân tầng (nested/fractal)** — mỗi khung "rót" DOL xuống khung dưới làm target ngắn hạn, đây là lý do 2022 Model thiết kế top-down.

---

## 5. Quy trình theo dõi case này tiếp theo

1. **Chờ sweep thật sự** của EQL (không chỉ chạm) — quét qua rồi mới có ý nghĩa gom đối ứng.
2. **Chờ đóng nến rejection + MSS Bullish** trên H1 (hoặc M5 để xác nhận nhanh hơn) tại/ngay sau vùng EQL.
3. Nếu có → Bias D1 được củng cố, chuyển hướng chú ý trở lại DOL D1 (EQH).
4. Nếu **không có rejection**, giá phá thẳng EQL với displacement mạnh không phản ứng → cảnh báo: đây có thể không còn là pullback bình thường mà là dấu hiệu **Change of Character** — D1 có thể đang chuyển từ HH/HL sang LH/LL thật. Phải dừng lại đánh giá lại Bias D1, không mặc định giá sẽ bật lên.
5. Kiểm tra thêm điều kiện củng cố EQL là DOL H1 hợp lệ:
   - Có nằm trong vùng **discount** của dealing range D1 không (dưới/quanh 50%, lý tưởng OTE 62–79%)?
   - EQL có phải **virgin** (chưa từng bị test) không?

---

## 6. Ví dụ minh họa bằng số (giả định XAUUSD — không phải dữ liệu thật)

![[DOL-Worked-Example-D1-H1-M5.svg]]

- **D1:** range 3320 (PWL) → 3410 (PWH), equilibrium 3365, MSS Bullish tại 3350, EQH virgin 3404–3406 = **DOL D1**.
- **H1:** PDH 3396 là DOL trung gian; POI (FVG/OB) tại 3372–3376; inducement quanh 3368–3370.
- **M5:** sweep ~3370 → MSS → entry tại FVG, stop ngoài vùng sweep (≈3366), Target 1 = 3396 (scale-out), Target cuối = 3404–3406 (DOL D1).
- Đọc chất lượng đường đi: ít cản (FVG ngược/old high) giữa 3376→3404 → **LRLR**, giữ runner; nhiều cản → **HRLR**, chốt dần.

---

## 7. Checklist áp dụng nhanh

- [ ] Xác định Bias D1 bằng structure (HH/HL hay LH/LL) — **không** dùng vị trí liquidity để suy ra bias.
- [ ] DOL D1 = pool đối diện bias, ưu tiên pool virgin + trùng nhiều mốc (EQH + PWH...).
- [ ] Nếu đang trong pullback, xác định Bias H1 riêng của nhịp đó → DOL H1 = pool đối diện Bias H1 (thường là trạm dừng tạm).
- [ ] Chờ sweep + rejection + MSS tại DOL H1 trước khi tin nhịp pullback đã xong.
- [ ] Nếu phá DOL H1 mà không phản ứng (displacement không rejection) → nghi ngờ Change of Character, tái đánh giá Bias D1.
- [ ] Entry chỉ sau sweep + MSS + FVG trên M5, stop ngoài vùng sweep, target theo thứ tự DOL trung gian → DOL chính.

## 8. Lỗi thường gặp cần tránh trong case này

| Lỗi | Vì sao sai | Cách sửa |
|---|---|---|
| Dùng "có EQH lớn phía trên" làm lý do khẳng định Bias Bullish | Đảo chiều nhân-quả; luôn có pool ở cả hai phía | Bias phải đến từ structure trước, DOL chỉ là output |
| Coi EQL phía dưới là "không quan trọng" vì D1 đang Bullish | Bỏ qua DOL H1 — dễ vào lệnh sớm trước khi nhịp pullback thật sự kết thúc | Xác nhận sweep + MSS tại EQL trước khi tin tiếp diễn |
| Mặc định pullback luôn kết thúc tại EQL rồi bật lên | DOL là xác suất, không phải định mệnh — có thể phá thẳng nếu là Change of Character | Luôn kiểm tra phản ứng thật (rejection) trước khi kết luận |

---

## 9. Liên kết

- [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] — nền tảng lý thuyết DOL
- [[12-Daily-Bias]] — quy trình xác định bias D1
- [[27-Premium-Discount]] — vị trí giá trong dealing range
- [[16-Internal-External-Range-Liquidity-IRL-ERL]] — phân biệt IRL/ERL
- [[21-Market-Structure-Shift]] — điều kiện xác nhận MSS
- [[01 - ICT 2022 Model|ICT 2022 Model]] — chuỗi entry đầy đủ
