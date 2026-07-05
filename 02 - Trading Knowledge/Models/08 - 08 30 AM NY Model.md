---
type: ict-concept
concept: 08:30 AM NY Model
aliases:
  - 08:30 AM NY Model
  - 0830 NY Model
  - ICT 2024 Lecture 1 Model
  - Post-08:30 Model
tags:
  - trading/ict/model
  - trading/study
  - "#ict2024"
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
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[04 - Breaker Block]]"
  - "[[25 - OB - Order Block]]"
  - "[[18 - Kill Zones]]"
  - "[[40 - Macro Times]]"
  - "[[12 - Daily Bias]]"
  - "[[24 - New Week Opening Gap]]"
  - "[[08 - 7 AM Liquidity Hunt + IFVG Entry]]"
prerequisites:
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[13 - FVG  - Fair Value Gap]]"
common_mistakes:
  - "[[Mistake - Enter before liquidity sweep]]"
  - "[[Mistake - Entry When MSS not in POI Zone]]"
---

# 08 - 08:30 AM NY Model

> [!info] Link
> [ICT 2024 Mentorship Lecture 1 Notes — 08:30 AM Model + PDF](https://innercircletrader.net/tutorials/ict-2024/lecture-1/)

> [!summary] Tóm tắt 1 câu
> **Mô hình 08:30 AM NY (ICT 2024, Lecture 1) là mô hình time-based: ngồi trước máy từ 08:00 NY, chờ SAU 08:30 giá RAID một cụm [[#2. Định nghĩa chủ chốt|relative equal highs/lows]], rồi tạo [[21 - Market Structure Shift|MSS]]; vào lệnh khi giá hồi về PD array (Order Block / BISI-SIBI / Breaker) mà displacement để lại, target là draw on liquidity kế tiếp.**

> [!important] Nguyên tắc cốt lõi
> **"Không phải giá đi ĐÂU, mà là KHI NÀO giá đi."** Cú raid post-08:30 là trigger; entry TRƯỚC 08:30 là front-run. MSS là bước xác nhận bắt buộc — raid không kèm MSS thì không có lệnh. 15m cho bias, 1m chỉ là trigger.

---

## 1. Khung thời gian & thời điểm

![[NY0830-Advanced-Timeline.svg|697]]

- **Vào bàn trước 08:00 NY** (để chứng kiến quá trình build-up 08:00→08:30).
- **Chỉ tập trung SAU 08:30 NY** — đây là cửa sổ setup.
- **Ba khung (bỏ mọi thứ khác nếu bạn còn mới):**
  - **15 phút** — chart mẹ: [[12 - Daily Bias|bias]] + [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw on liquidity]] + inefficiency.
  - **5 phút** — bối cảnh cấu trúc.
  - **1 phút** — quan sát relative equal H/L và trigger entry.

> [!tip] Liên hệ Macro
> 08:30 rơi trong [[18 - Kill Zones|NY AM killzone]]; cú giải quyết thường trùng [[40 - Macro Times|macro]] 08:50 và 09:50. 09:30 (mở NYSE) khuếch đại setup trên NQ/ES.

---

## 2. Định nghĩa chủ chốt

![[NY0830-Advanced-Definitions.svg|697]]

- **Relative Equal High:** một đỉnh có swing high **thấp hơn** ở bên phải — hình thành do swing failure, tiềm năng đảo chiều (thanh khoản nằm trên nó = BSL).
- **Relative Equal Low:** một đáy có swing low **cao hơn** ở bên phải (thanh khoản nằm dưới = SSL).
- **Displacement:** cú đi **ngược** một swing của pre-session/pre-day (cú phản công).
- **Order Block:** vùng tổ chức khớp lượng lớn lệnh, giá bật mạnh khỏi đó.
- **Breaker Block:** khi giá quét thanh khoản của một đáy/relative equal lows rồi đảo lên phá swing high — các **nến tăng** trước cú quét là bullish breaker; **nến cuối** cùng màu là nhạy nhất (bearish breaker là ảnh gương).
- **BISI:** FVG **up-closed** (tăng). **SIBI:** FVG **down-closed** (giảm).
- **NWOG:** [[24 - New Week Opening Gap|New Week Opening Gap]] — gap giữa giá đóng cửa thứ Sáu và mở cửa Chủ nhật.

---

## 3. Kịch bản BEARISH

![[NY0830-Advanced-Bearish.svg|697]]

1. Giá hình thành và **grab relative equal highs** (raid BSL) sau 08:30.
2. Chờ giá quay lại range và **đóng dưới swing low = MSS** xuống.
3. Đánh dấu **bearish OB**, **SIBI** trong chân giảm, và **bearish breaker** hình thành sau khi phá swing low.
4. Khi giá hồi về OB / SIBI / breaker → **SELL**.
5. **Stop trên đỉnh** hình thành post-08:30.
6. **TP = draw on liquidity kế tiếp:** relative equal lows / đáy phiên trước.

---

## 4. Kịch bản BULLISH

![[NY0830-Advanced-Bullish.svg|697]]

1. Giá hình thành và **grab relative equal lows** (raid SSL) sau 08:30.
2. Chờ giá quay lại range và **đóng trên swing high = MSS** lên.
3. Đánh dấu **bullish OB**, **BISI** trong chân tăng, và **bullish breaker** sau khi phá swing high.
4. Khi giá hồi về OB / BISI / breaker → **BUY**.
5. **Stop dưới đáy** hình thành post-08:30.
6. **TP = draw on liquidity kế tiếp:** relative equal highs / đỉnh phiên trước.

---

## 5. Chọn PD array sau MSS

![[NY0830-Advanced-PDArray-Choice.svg|697]]

Displacement để lại **ba lựa chọn** entry: **Order Block**, **BISI/SIBI (FVG)**, **Breaker Block**. Nguyên tắc: **vào PD array ĐẦU TIÊN** giá chạm sau MSS — chờ nhịp hồi sâu nhất thường lỡ lệnh.

---

## 6. Trình tự giao dịch (9 bước)

1. Vào bàn **trước 08:00 NY**; theo dõi build-up 08:00→08:30.
2. **Chart 15m:** đánh dấu inefficiency (FVG) và draw-on-liquidity trên/dưới giá.
3. **Chart 1m:** quan sát relative equal highs (bearish) / relative equal lows (bullish) hình thành.
4. **Chờ raid sau 08:30** — giá phải lấy mức relative equal đó.
5. **Chờ MSS** — đóng dưới swing low (bearish) / trên swing high (bullish).
6. **Đánh dấu PD array** — OB / BISI-SIBI / breaker do displacement để lại.
7. **Vào lệnh tại retest** PD array đầu tiên.
8. **Đặt stop** — trên đỉnh (short) / dưới đáy (long) hình thành post-08:30.
9. **Chốt lời tại DOL kế** — relative equal đối diện / đỉnh-đáy phiên trước.

---

## 7. Thị trường phù hợp

- **NQ / ES** — precision 1m sạch nhất (mở NYSE 09:30 khuếch đại setup 08:30).
- **GBP/USD, EUR/USD** — overlap London muộn + NY open.
- **XAU/USD** — displacement sạch quanh tin Mỹ 08:30 (CPI/NFP/PPI).

---

## 8. Ví dụ chart

### Ví dụ đúng
![[NY0830-Example-Correct.svg|697]]

**Mô tả:** có bias 15m; chờ raid relative equal highs sau 08:30; MSS xác nhận; vào SIBI (PD array đầu tiên); stop ngoài toàn bộ range post-08:30.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp NQ/NAS100: đánh dấu (1) relative equal H/L, (2) cú raid sau 08:30, (3) nến MSS + PD array (OB/FVG/breaker), (4) entry retest, (5) stop ngoài range post-08:30, (6) TP tại DOL. Ghi giờ ET.*

### Ví dụ sai / dễ nhầm
![[NY0830-Example-Wrong.svg|697]]

**Bài học:** đây đều là các lỗi ICT nêu trực tiếp trong Lecture 1 (xem mục 10).

---

## 9. Thực hành tốt nhất (Best Practices)

> [!tip] Quy tắc 08:30 Model
> 1. **Bias 15m trước tiên** — 1m chỉ là trigger, không phải bias.
> 2. **Chờ raid + MSS** — không bao giờ vào trước 08:30, không vào chỉ vì vừa raid.
> 3. **Vào PD array ĐẦU TIÊN** sau MSS, tại retest.
> 4. **Stop ngoài toàn bộ range post-08:30**, không chỉ tại swing MSS.
> 5. **TP theo DOL** — relative equal đối diện / H-L phiên trước.

- Ưu tiên ngày có **tin 08:30** (CPI/NFP/PPI) trên NQ/ES/XAU — displacement sạch hơn.
- Ghép với [[40 - Macro Times|macro]] 08:50 & 09:50 để tinh chỉnh thời điểm MSS.
- Nếu PD array trùng thành [[07 - Unicorn Model|Unicorn]] (Breaker + FVG chồng lấn) → chất lượng A+.
- So sánh với [[08 - 7 AM Liquidity Hunt + IFVG Entry|mô hình 07:00 AM]]: 08:30 vào tại PD array bất kỳ (OB/FVG/breaker); 07:00 chuyên vào **50% CE của IFVG**.

---

## 10. Lỗi thường gặp (theo Lecture 1)

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Pre-position trước 08:30 | Vào lệnh khi chưa có cú raid | Cú sweep post-08:30 mới là trigger |
| Bỏ qua MSS | Vào ngay khi vừa raid | MSS là bước xác nhận bắt buộc |
| Không có context 15m | Chỉ nhìn 1m | Bias + DOL đến từ 15m; 1m chỉ trigger |
| Sai PD array | Đợi hồi quá sâu | Vào PD array đầu tiên sau MSS |
| Stop quá chặt | Đặt tại swing MSS | Stop ngoài toàn bộ range post-08:30 |

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Ba khung thời gian của mô hình và vai trò?
**Đáp:** 15m = bias + DOL; 5m = cấu trúc; 1m = relative equal H/L + trigger.

### Q2
**Hỏi:** Trình tự trigger cốt lõi là gì?
**Đáp:** Raid relative equal (sau 08:30) → MSS → vào PD array đầu tiên tại retest.

### Q3
**Hỏi:** Stop đặt ở đâu?
**Đáp:** Ngoài toàn bộ range post-08:30 (trên đỉnh cho short / dưới đáy cho long), không chỉ tại swing MSS.

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
| Nhận diện relative equal H/L | | |
| Chờ raid + MSS đúng | | |
| Chọn PD array đầu tiên | | |
| Áp dụng vào trade thực tế | | |

**Kế hoạch review tiếp theo:**
