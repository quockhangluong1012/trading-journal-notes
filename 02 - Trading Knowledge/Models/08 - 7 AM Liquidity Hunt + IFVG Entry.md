---
type: ict-concept
concept: 07:00 AM Liquidity Hunt + IFVG Entry
aliases:
  - 07:00 AM Liquidity Hunt + IFVG Entry
  - 7 AM IFVG Model
  - ICT 2024 Lecture 2 Model
  - AM Session IFVG
tags:
  - trading/ict/model
  - trading/study
  - "#ict2024"
  - "#ifvg"
  - "#ny-open"
status: developing
category: Entry Model
timeframes:
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
  - "[[17 - Inverse Fair Value Gap - iFVG]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[04 - Breaker Block]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[18 - Kill Zones]]"
  - "[[40 - Macro Times]]"
  - "[[31 - Standard Deviation]]"
  - "[[08 - 08 30 AM NY Model]]"
prerequisites:
  - "[[17 - Inverse Fair Value Gap - iFVG]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[21 - Market Structure Shift]]"
common_mistakes:
  - "[[Mistake - Enter before liquidity sweep]]"
  - "[[Mistake - Entry When MSS not in POI Zone]]"
---

# 08 - 07:00 AM Liquidity Hunt + IFVG Entry

> [!info] Link
> [ICT 2024 Mentorship Lecture 2 Notes — 07:00 AM IFVG Model + PDF](https://innercircletrader.net/tutorials/ict-2024/mentorship-lecture-2/)

> [!summary] Tóm tắt 1 câu
> **Mô hình 07:00 AM (ICT 2024, Lecture 2) chuyển entry từ mốc 08:30 sang nhịp hồi AM-session sau 07:00: giá hồi về range London, hunt relative equal highs/lows, tạo [[21 - Market Structure Shift|MSS]]; vào lệnh tại 50% CE ([[10 - Consequent Encroachment (Mean Threshold)|consequent encroachment]]) của [[17 - Inverse Fair Value Gap - iFVG|IFVG]] (FVG đầu tiên trước cú hunt) — hoặc breaker nếu không có IFVG; chốt lời bằng Fib -2/-2.5.**

> [!important] Nguyên tắc cốt lõi
> **IFVG là FVG ĐẦU TIÊN ngay trước cú stop-hunt** — sau MSS nó bị đảo vai (support↔resistance) và trở thành vùng nhạy nhất. Entry chuẩn là **50% CE của IFVG**, không phải vào lúc MSS. Và luôn nhớ **lưu ý 30 phút đầu**: sau 07:00/08:00/09:00 giá thường đi NGƯỢC bias để hunt thanh khoản trước.

---

## 1. Thời điểm & bối cảnh

![[AM0700IFVG-Advanced-Timeline.svg|697]]

- **Ngồi trước máy trước 07:00 NY.** Nếu mới, đừng nhìn gì trước đó; nếu có kinh nghiệm, chỉ xem **đỉnh & đáy phiên London** (= draw on liquidity).
- **Đặc tính đầu tiên của AM-session:** giá **hồi lại vào trong range London**.
- **Đừng dự đoán** — chờ giá tự in relative equal highs/lows trên **5m/1m**.
- **Khung thời gian:** 15m · 5m · 1m · thêm **15 giây** cho entry tinh.
- **Mốc giờ chính:** 07:00 · 08:00 · 09:00 (NY).

---

## 2. Định nghĩa chủ chốt

- **SIBI** = FVG down-closed (giảm); **BISI** = FVG up-closed (tăng).
- **IFVG** = [[17 - Inverse Fair Value Gap - iFVG|Inversion Fair Value Gap]] — FVG bị giá đóng xuyên qua sau MSS, đảo vai.
- **Breaker** = một [[25 - OB - Order Block|Order Block]] **thất bại** (dùng làm entry dự phòng khi không có IFVG).
- **Relative Equal High/Low** — đỉnh/đáy có swing đối diện thấp/cao hơn ở bên phải (swing failure).
- **Fractal** — tính lặp lại của hành vi giá trên mọi khung.
- **"Specific"** — **FVG đầu tiên ngay trước stop-hunt** là IFVG nhạy nhất.
- **Consequent Encroachment (CE)** — mức 50% (giữa) của một PD array. Xem [[10 - Consequent Encroachment (Mean Threshold)]].
- **Fibonacci inputs:** 0 · 0.5 · 1 · **-2** · **-2.5**.

---

## 3. IFVG — vì sao là entry nhạy nhất

![[AM0700IFVG-Advanced-IFVG-Concept.svg|697]]

Một FVG tăng (BISI) là **support** khi giá đi lên. Nhưng sau khi giá **hunt thanh khoản** rồi tạo **MSS** và **đóng xuyên** qua nó, FVG đó **đảo vai** thành **kháng cự** = **IFVG**. FVG **đầu tiên trước cú hunt** là IFVG nhạy nhất — đây chính là vùng ta canh **50% CE** để vào lệnh.

---

## 4. Kịch bản BEARISH

![[AM0700IFVG-Advanced-Bearish.svg|697]]

1. Giá hình thành và **grab relative equal highs** sau 07:00.
2. Chờ quay lại range và **đóng dưới swing low = MSS** xuống.
3. Đánh dấu **FVG đầu tiên trước cú hunt** làm **IFVG**, và **bearish breaker** sau khi phá swing low.
4. Vào **SELL** tại **50% CE của IFVG**. Nếu không có IFVG → vào **bearish breaker**.
5. **Stop trên swing high** hình thành post-07:00 hunt.
6. **TP:** next draw on liquidity, hoặc Fib từ **đỉnh post-07:00 → lowest low tại 07:00 (open)**, chốt tại **-2 / -2.5**.

---

## 5. Kịch bản BULLISH

![[AM0700IFVG-Advanced-Bullish.svg|697]]

1. Giá hình thành và **grab relative equal lows** sau 07:00.
2. Chờ quay lại range và **đóng trên swing high = MSS** lên.
3. Đánh dấu **FVG đầu tiên trước cú hunt** làm **IFVG**, và **bullish breaker**.
4. Vào **BUY** tại **50% CE của IFVG**. Nếu không có IFVG → vào **bullish breaker**.
5. **Stop dưới swing low** hình thành post-07:00 hunt.
6. **TP:** next DOL, hoặc Fib từ **đáy post-07:00 → highest high tại 07:00 (open)**, chốt tại **-2 / -2.5**.

---

## 6. Mục tiêu Fibonacci

![[AM0700IFVG-Advanced-Fib-Targets.svg|697]]

Dùng Fib với inputs **0 · 0.5 · 1 · -2 · -2.5**. Vẽ từ swing hình thành post-07:00 hunt **về** giá mở cửa 07:00. Chốt **theo bậc thang**: một phần tại **-2**, phần còn lại tại **-2.5** — đóng hết tại -2 sẽ bỏ lỡ phần lớn của move. Có thể thay bằng next draw on liquidity làm target. Liên hệ [[31 - Standard Deviation|Standard Deviation]] projections.

---

## 7. Lưu ý 30 phút đầu — kỳ vọng move NGƯỢC

![[AM0700IFVG-Advanced-30min-Reversal.svg|697]]

**Sau 07:00, 08:00 và 09:00, trong 30 phút đầu (pre-session range), giá thường đi NGƯỢC** với relative trend / relative equal H/L. Ví dụ: bias bullish nhưng 30 phút đầu giá đi bearish để hunt thanh khoản trước khi đảo. Đây là cảnh báo counter-move **có sẵn trong khung Lecture 2** — quên nó = vào ngược move thật.

---

## 8. Ví dụ chart

### Ví dụ đúng
![[AM0700IFVG-Example-Correct.svg|697]]

**Mô tả:** dùng London H/L làm DOL; hunt relative equal highs sau 07:00; MSS; đánh dấu IFVG (FVG đầu tiên); vào 50% CE; chốt Fib -2/-2.5.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp NQ/NAS100: đánh dấu (1) đỉnh/đáy London, (2) cú hunt sau 07:00, (3) MSS, (4) IFVG = FVG đầu tiên trước hunt + mức 50% CE khớp lệnh, (5) stop ngoài swing post-07:00, (6) Fib -2/-2.5. Ghi giờ ET.*

### Ví dụ sai / dễ nhầm
![[AM0700IFVG-Example-Wrong.svg|697]]

**Bài học:** các lỗi này được ICT nêu trực tiếp trong Lecture 2 — xem mục 10.

---

## 9. Thực hành tốt nhất (Best Practices)

> [!tip] Quy tắc 07:00 IFVG Model
> 1. **London H/L = DOL** — tham chiếu duy nhất cần từ trước 07:00.
> 2. **Không dự đoán** — chờ relative equal in ra, chờ hunt, chờ MSS.
> 3. **IFVG = FVG ĐẦU TIÊN trước hunt** — đánh dấu sai = entry kém nhạy.
> 4. **Vào 50% CE của IFVG** (breaker là dự phòng), không vào lúc MSS.
> 5. **Chốt bậc thang -2 / -2.5**, tôn trọng lưu ý 30 phút đầu.

- Ghép với [[40 - Macro Times|macro]] 07:00-liên quan (và 08:50/09:50) để tinh chỉnh thời điểm hunt/MSS.
- Nếu IFVG trùng breaker (chồng lấn) → thực chất là [[07 - Unicorn Model|Unicorn]], chất lượng A+.
- So với [[08 - 08 30 AM NY Model|mô hình 08:30]]: 08:30 vào PD array bất kỳ (OB/FVG/breaker) tại retest; 07:00 chuyên **50% CE của IFVG** + target Fib -2/-2.5.
- Ưu tiên NQ/ES cho precision; EU/GU cho nhịp hồi rõ vào range London; vàng quanh tin Mỹ.

---

## 10. Lỗi thường gặp (theo Lecture 2)

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Pre-position trước 07:00 | Vào khi chưa có hunt | Cú sweep post-07:00 mới là trigger |
| Sai IFVG | Đánh dấu FVG sau/trước không đúng | IFVG = FVG **đầu tiên** ngay trước hunt |
| Bỏ qua MSS | Vào bằng wick đơn thuần | MSS là bước xác nhận bắt buộc |
| Quên lưu ý 30 phút | Vào ngược move thật đầu giờ | Nhớ counter-move 30′ sau 07/08/09 |
| Stop quá chặt | Đặt tại pivot MSS | Stop ngoài toàn bộ swing post-07:00 |
| Chốt một phát | Đóng hết tại -2 | Chốt bậc thang -2 rồi -2.5 |

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** IFVG trong mô hình này là FVG nào?
**Đáp:** FVG **đầu tiên ngay trước cú stop-hunt** — sau MSS nó đảo vai, là vùng nhạy nhất.

### Q2
**Hỏi:** Vào lệnh tại đâu?
**Đáp:** **50% CE (consequent encroachment)** của IFVG; nếu không có IFVG thì vào breaker.

### Q3
**Hỏi:** TP được xác định thế nào?
**Đáp:** Next DOL, hoặc Fib (0/0.5/1/-2/-2.5) từ swing post-07:00 về open 07:00 — chốt bậc thang -2 rồi -2.5.

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
| Hiểu định nghĩa IFVG | | |
| Đánh dấu IFVG đầu tiên đúng | | |
| Vào đúng 50% CE | | |
| Dùng Fib -2/-2.5 | | |
| Áp dụng vào trade thực tế | | |

**Kế hoạch review tiếp theo:**
