---
type: ict-concept
concept: Unicorn Model
aliases:
  - Unicorn Model
  - ICT Unicorn
  - Breaker + FVG Overlap
  - Unicorn Setup
tags:
  - trading/ict/model
  - trading/study
  - "#unicorn"
  - "#breaker"
  - "#fvg"
status: developing
category: Entry Model
timeframes:
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 2
last_reviewed: 2026-07-04
created: 2026-07-04
updated: 2026-07-04
related_concepts:
  - "[[04 - Breaker Block]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[25 - OB - Order Block]]"
  - "[[21 - Market Structure Shift]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[16 - Internal & External Range Liquidity (IRL & ERL)]]"
  - "[[27 - Premium Discount]]"
  - "[[40 - Macro Times]]"
prerequisites:
  - "[[04 - Breaker Block]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[21 - Market Structure Shift]]"
common_mistakes:
  - "[[Mistake - Enter before liquidity sweep]]"
  - "[[Mistake - Entry When MSS not in POI Zone]]"
---

# 07 - Unicorn Model

> [!info] Link
> [ICT Unicorn Model — Breaker Block & FVG Overlap Setup + Free PDF](https://innercircletrader.net/tutorials/ict-unicorn-model/)

> [!summary] Tóm tắt 1 câu
> **Unicorn Model là điểm vào xác suất cao xuất hiện khi một [[04 - Breaker Block|Breaker Block]] và một [[13 - FVG  - Fair Value Gap|Fair Value Gap]] CHỒNG LẤN trên cùng một vùng giá — vùng giao nhau đó ("unicorn") mang áp lực kép: vừa phải lấp imbalance (FVG), vừa là hỗ trợ/kháng cự cấu trúc (Breaker), nên mạnh hơn hẳn FVG đơn hay Breaker đơn.**

> [!important] Nguyên tắc cốt lõi
> **Không có chồng lấn = không có Unicorn.** Breaker và FVG phải *thực sự* chia sẻ cùng dải giá. Khi FVG nằm TRỌN bên trong Breaker, vùng mạnh "gấp đôi". Và **không bao giờ vào lệnh ngay tại khoảnh khắc MSS** — phải chờ giá HỒI về vùng unicorn (lý tưởng là 50% CE của FVG bên trong Breaker).

---

## 1. Định nghĩa

![[Unicorn-Advanced-Anatomy.svg|697]]

**Khái niệm:** Unicorn = sự **chồng lấn giá** giữa Breaker Block và FVG do cùng một cú displacement tạo ra. Vùng giao nhau là điểm vào. Nó hoạt động vì khi giá quay lại đây, nó chịu **hai lực đồng thời**:
- **Lấp imbalance** — FVG là vùng mất cân bằng, thuật toán có xu hướng rebalance nó.
- **Hỗ trợ/kháng cự cấu trúc** — Breaker (một [[25 - OB - Order Block|Order Block]] đã "thất bại" và đảo vai) là mức mà tổ chức đã để lại lệnh.

**Nó trả lời câu hỏi nào trên chart?**
- Trong nhiều FVG/Breaker rải rác, đâu là **POI có xác suất phản ứng cao nhất**?
- Điểm vào nào có **hai lớp lý do** thay vì một?
- Vùng nào đáng đặt **limit** với stop chặt và RR lớn?

### Unicorn KHÔNG phải là gì
- Không phải một FVG đơn lẻ, cũng không phải một Breaker đơn lẻ — bắt buộc **chồng lấn**.
- Không phải tín hiệu vào ngay khi MSS xảy ra — phải **retrace**.
- Không phải cái cớ để bỏ qua bias HTF — vẫn cần narrative + premium/discount đúng.

---

## 2. Cấu phần bắt buộc

**Breaker Block** (xem [[04 - Breaker Block]]): là **Order Block thất bại**. Bullish breaker = những nến giảm cuối cùng trước cú đẩy lên đã (a) quét một đáy (SSL) rồi (b) displacement lên phá swing high. Bearish breaker là ảnh gương: nến tăng cuối trước cú đẩy xuống sau khi quét đỉnh (BSL).

**Fair Value Gap** (xem [[13 - FVG  - Fair Value Gap]]): khe mất cân bằng để lại bởi chính cú displacement tạo MSS.

**Chồng lấn:** hai vùng trên phải cắt nhau về giá. Nếu FVG nằm trong Breaker → chất lượng cao nhất.

---

## 3. Chuỗi hình thành

![[Unicorn-Advanced-Formation-Sequence.svg|697]]

1. **Bias + Premium/Discount** — HTF bias rõ ([[27 - Premium Discount]]).
2. **Quét thanh khoản** — [[20 - Liquidity Sweep|sweep]] một đỉnh/đáy (inducement/stop hunt).
3. **Displacement + [[21 - Market Structure Shift|MSS]]** — cú đẩy mạnh phá cấu trúc, để lại **FVG** và hình thành **Breaker**.
4. **Chồng lấn** — FVG rơi vào trong Breaker = **vùng Unicorn**.
5. **Retrace entry** — chờ giá hồi về vùng, KHÔNG vào lúc MSS.

---

## 4. Bullish vs Bearish

![[Unicorn-Advanced-Bullish-vs-Bearish.svg|697]]

**Bullish Unicorn:** giá quét **SSL (đáy)** → displacement lên phá swing high → bullish breaker + BISI/FVG chồng lấn → mua khi hồi về vùng.
**Bearish Unicorn:** giá quét **BSL (đỉnh)** → displacement xuống phá swing low → bearish breaker + SIBI/FVG chồng lấn → bán khi hồi về vùng.

---

## 5. Hai bối cảnh: Reversal vs Continuation

![[Unicorn-Advanced-Reversal-vs-Continuation.svg|697]]

**Reversal Unicorn:** sau khi quét một đỉnh/đáy **lớn**, kỳ vọng đảo chiều — rủi ro cao hơn, cần bias HTF ủng hộ mạnh.
**Continuation Unicorn:** sau pullback/inducement **thuận** xu hướng đang chạy — xác suất cao hơn, ưu tiên.

---

## 6. Vào lệnh, Stop & Target

![[Unicorn-Advanced-Entry-CE.svg|697]]

- **Entry:** đặt **limit** tại vùng chồng lấn, lý tưởng là **50% CE** ([[10 - Consequent Encroachment (Mean Threshold)]]) của FVG nằm trong Breaker.
- **Stop:** vượt qua **wick của cú sweep** / cạnh xa của Breaker — không phải con số cố định.
- **Target:** [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL trước, ERL sau]]. Dời stop về BE sau khi chạm T1. RR thường lớn nhờ stop chặt.
- **Timing:** ưu tiên vùng hình thành trong [[18 - Kill Zones|killzone]] / [[40 - Macro Times|macro]].

---

## 7. Ví dụ chart

### Ví dụ đúng
![[Unicorn-Example-Correct.svg|697]]

**Mô tả:** FVG nằm trọn trong Breaker, thuận HTF bias, hình thành trong killzone, có SMT divergence xác nhận; limit tại 50% CE.

**Vì sao tốt:** overlap thật + displacement sạch + đúng bias + đúng thời gian + entry retrace (không đuổi).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lệnh thật: đánh dấu (1) mức thanh khoản bị quét, (2) nến displacement/MSS, (3) Breaker (tô cam) và FVG (tô xanh) và phần chồng lấn (tím), (4) điểm limit 50% CE, (5) T1/T2.*

### Ví dụ sai / dễ nhầm
![[Unicorn-Example-Wrong.svg|697]]

**Mô tả lỗi:** Breaker ở trên, FVG ở dưới, **tách rời** → không có vùng chồng lấn → **không phải Unicorn**. Hoặc vào ngay lúc MSS không chờ hồi, hoặc trade ngược bias.

**Bài học:** luôn **đo** phần chồng lấn; nếu không cắt nhau thì đây chỉ là FVG đơn / Breaker đơn, không phải setup unicorn.

---

## 8. Thực hành tốt nhất (Best Practices)

> [!tip] Quy tắc Unicorn
> 1. **Đo overlap thật** — nếu Breaker và FVG không cắt nhau về giá, bỏ qua.
> 2. **Yêu cầu displacement chất lượng** — nến đẩy mạnh, ít chồng lấn; nến yếu → hạ cấp setup.
> 3. **Thuận HTF bias + DOL** — unicorn ngược dòng tuần là bẫy.
> 4. **Ưu tiên timing** — killzone/macro (đặc biệt 09:50→10:10 NQ, 04:03 forex).
> 5. **Đặt limit, không chase** — vào tại 50% CE; nếu giá không hồi về, bỏ lệnh.

- Xếp hạng chất lượng: **A+** khi FVG nằm trọn trong Breaker + đúng premium/discount + có SMT + trong macro.
- **Invalid** khi giá đóng nến hẳn qua cạnh xa của Breaker mà không phản ứng.
- Kết hợp với các model khung ngày: [[08 - 08 30 AM NY Model]] và [[08 - 7 AM Liquidity Hunt + IFVG Entry]] thường tạo unicorn tại PD array sau MSS.

---

## 9. Checklist trước khi vào lệnh

- [ ] HTF bias rõ ràng, đúng hướng
- [ ] Giá ở Premium/Discount phù hợp
- [ ] Đã có sweep thanh khoản trước displacement
- [ ] Displacement tạo **MSS** rõ + FVG sạch
- [ ] Breaker hình thành và **chồng lấn** với FVG (đo được)
- [ ] Đặt limit tại **50% CE** của FVG trong Breaker
- [ ] Stop vượt wick sweep / cạnh xa Breaker
- [ ] T1 = IRL, T2 = ERL; RR đạt kế hoạch
- [ ] (Ưu tiên) trong killzone/macro + có SMT
- [ ] Không vào lúc MSS, không chase, không ngược bias

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Gọi nhầm FVG/Breaker đơn là unicorn | Không có phần chồng lấn | Đo overlap; bắt buộc cắt nhau về giá |
| Vào lúc MSS | Market order ngay nến displacement | Chờ hồi về 50% CE, đặt limit |
| Ngược bias | Setup đẹp nhưng ngược dòng tuần | Ưu tiên HTF narrative + DOL |
| Displacement yếu | Nến chồng lấn, không dứt khoát | Chỉ nhận displacement mạnh, có FVG rõ |
| Stop quá chặt/quá xa | Đặt tại MSS hoặc quá rộng | Stop vượt wick sweep / cạnh xa Breaker |

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Unicorn được tạo bởi sự kết hợp của gì?
**Đáp:** Breaker Block **chồng lấn** với FVG (do cùng cú displacement) → vùng unicorn.

### Q2
**Hỏi:** Vào lệnh ở đâu và khi nào?
**Đáp:** Limit tại **50% CE** của FVG bên trong Breaker, trên **nhịp hồi** sau MSS — không vào lúc MSS.

### Q3
**Hỏi:** Điều gì làm setup unicorn INVALID?
**Đáp:** Breaker và FVG không chồng lấn; hoặc giá đóng nến hẳn qua cạnh xa của Breaker mà không phản ứng.

---

## 12. Liên kết với Trade Journal

### Lệnh áp dụng đúng model này
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

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa | | |
| Nhận diện overlap trên chart | | |
| Vào đúng 50% CE | | |
| Kết hợp bias + timing | | |
| Áp dụng vào trade thực tế | | |

**Kế hoạch review tiếp theo:**
