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
  - 15m (bias + DOL)
  - 5m (structure)
  - 1m (trigger)
models:
  - ICT 2022 Model
  - Unicorn Model
markets:
  - NQ1/NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-07-05
created: 2026-07-04
updated: 2026-07-05
related_concepts:
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[18 - Kill Zones]]"
  - "[[40 - Macro Times]]"
  - "[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]"
prerequisites:
  - "[[12 - Daily Bias]]"
  - "[[21 - Market Structure Shift]]"
  - "[[25 - OB - Order Block]]"
  - "[[13 - FVG  - Fair Value Gap]]"
common_mistakes:
  - Pre-position trước 08:30
  - Bỏ qua MSS
  - Không có context 15m
---

# 08 - 08:30 AM NY Model

> [!info] Link
> [ICT 2024 Mentorship Lecture 1 Notes — 08:30 AM Model + PDF](https://innercircletrader.net/tutorials/ict-2024/lecture-1/)

> [!summary] Tóm tắt 1 câu
> **Mô hình 08:30 AM NY (ICT 2024, Lecture 1) là mô hình time-based: ngồi trước máy từ 08:00 NY, chờ SAU 08:30 giá RAID một cụm [[#2. Định nghĩa chủ chốt|relative equal highs/lows]], rồi tạo [[21 - Market Structure Shift|MSS]]; vào lệnh khi giá hồi về PD array (Order Block / BISI-SIBI / Breaker) mà displacement để lại, target là draw on liquidity kế tiếp.**

> [!important] Nguyên tắc cốt lõi
> **"Không phải giá đi ĐÂU, mà là KHI NÀO giá đi."** Cú raid post-08:30 là trigger; entry TRƯỚC 08:30 là front-run. MSS là bước xác nhận bắt buộc — raid không kèm MSS thì không có lệnh. 15m cho bias, 1m chỉ là trigger.

> [!tip] Bản đồ đọc note này
> Mục 1–2 = *khung giờ + định nghĩa*. Mục 2b = *WHY (vì sao 08:30)*. Mục 3–6 = *HOW (kịch bản, PD array, trình tự 9 bước, stop)*. Mục 7–9 = *thị trường, nested HTF, ví dụ*. Mục 10–16 = *thực chiến & prop-firm*. Mới học: đọc 1→6; đã trade: nhảy tới 8–11.

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

## 2b. Vì sao "08:30" hoạt động — cơ chế thời gian

![[NY0830-WhyItWorks.svg|697]]

> [!important] Đây là điểm khác biệt cốt lõi so với các model "dựa vào giá"
> Hầu hết trader cố *dự đoán* giá sẽ đi đâu. Model 08:30 lật ngược: nó xác định một **cửa sổ thời gian** nơi thanh khoản và biến động dồn lại, rồi *chờ thị trường tự lộ diện* bằng raid + MSS. Bạn giao dịch phản ứng, không giao dịch dự đoán.

**① Catalyst tin tức 08:30 ET.** Phần lớn dữ liệu kinh tế Mỹ quan trọng (CPI, NFP, PPI, Jobless Claims, Retail Sales) phát hành đúng **08:30 ET**. Tin tức tạo ra một cú tăng volume + biến động — đây là "cái cớ" hoàn hảo để giá **raid** cụm thanh khoản đã tích lũy từ 08:00→08:30. Ngay cả những ngày không có tin lớn, khung giờ này vẫn là mở màn NY AM nên vẫn có dòng lệnh tổ chức vào.

**② NY AM killzone + macro windows.** 08:30 nằm ở đầu [[18 - Kill Zones|NY AM killzone]]. Cú "giải quyết" (đảo chiều/displacement thật) thường trùng các [[40 - Macro Times|macro]] 08:50 và 09:50. **09:30 mở cửa NYSE** bơm thanh khoản cổ phiếu → displacement trên NQ/ES sạch và mạnh nhất trong ngày.

**③ Cơ chế build-up → raid → phản công.** Từ 08:00→08:30 giá thường in ra các **relative equal highs/lows** — đám đông đặt stop và lệnh chờ quanh đó. Sau 08:30, thuật toán **raid** cụm thanh khoản này (nạp nhiên liệu đối ứng cho lệnh tổ chức), rồi **đảo chiều tạo MSS**. Bạn vào theo cú phản công tại PD array mà displacement để lại.

> [!warning] Vì sao MSS bắt buộc
> Raid **không kèm** MSS = thanh khoản đã bị lấy nhưng thị trường chưa "cam kết" hướng. Vào chỉ vì "vừa raid" là đoán mò. MSS (đóng qua swing đối diện + displacement) là bằng chứng khách quan rằng cú raid đã hoàn thành nhiệm vụ và giá chuyển hướng. Xem [[41 - Change in State of Delivery]] và [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] để hiểu sâu vì sao đám đông bị bẫy đúng tại relative equal.

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

> [!tip] Khi ba PD array chồng lấn → Unicorn
> Nếu Breaker và FVG do cùng displacement **chồng lấn** nhau, PD array của bạn thực chất là một [[07 - Unicorn Model|Unicorn]] — grade A+. Đây là biến thể chất lượng cao nhất của entry 08:30: vào tại 50% CE của vùng overlap thay vì mép PD array.

**Thứ tự ưu tiên khi có nhiều lựa chọn:**

| Ưu tiên | PD array | Khi nào chọn |
|---|---|---|
| 1 | **Unicorn (Breaker+FVG overlap)** | Khi có overlap thật → stop chặt nhất, RR cao nhất |
| 2 | **FVG (BISI/SIBI) sạch** | FVG "first & clean" ngay sau MSS, ít chồng lấn |
| 3 | **Order Block** | Khi FVG bị lấp nhanh hoặc không rõ |
| 4 | **Breaker** | Entry dự phòng khi các lựa chọn trên không có |

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

![[NY0830-Stop-Logic.svg|697]]

> [!example] Mẫu ghi nhanh — 08:30 (Bearish)
> ```text
> Bias (15m): Bearish | DOL: SSL @ [level]
> (1) Relative equal highs @ [level] (build-up 08:00-08:30)
> (2) Raid BSL sau 08:30 @ [time]
> (3) MSS: đóng dưới [swing low] + displacement → SIBI/bearish breaker
> (4) PD array chọn: [SIBI/OB/breaker] range [low]-[high]
> (5) Entry retest @ [level] | Stop trên đỉnh post-08:30 @ [level]
> (6) T1 = IRL [..] (dời BE) → T2 = DOL kế [..]
> News 08:30: [CPI/NFP/none] | Macro: 08:50 / 09:50
> Invalid: đóng nến trên đỉnh post-08:30
> ```

---

## 7. Thị trường phù hợp

![[NY0830-CrossMarket.svg|697]]

Cùng trình tự raid → MSS → PD array, nhưng độ sạch và vai trò của tin 08:30 khác nhau giữa các thị trường bạn trade.

| Đặc tính | NQ1 / ES | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Độ precision 1m | Sạch nhất; 09:30 mở NYSE khuếch đại | Tốt, nhịp hồi rõ vào range | Thất thường quanh tin |
| Phụ thuộc tin 08:30 | Cao (index nhạy CPI/NFP) | Trung bình (ít phụ thuộc hơn) | Rất cao (displacement sạch quanh tin) |
| Relative equal | Rõ trong phiên | Thoai thoải, thanh khoản sâu | Có thể dồn vào vài phút |
| Rủi ro đặc thù | Whipsaw quanh 08:30 nếu tin bất ngờ | "Lình xình" nếu không có tin | Wick rất dài → stop dễ bị quét |
| Điều chỉnh | Ưu tiên PD array first & clean | Chờ nhịp hồi vào range rõ | Chờ MSS + FVG rõ; nới stop, giảm size |

- **Ngày có tin 08:30** (CPI/NFP/PPI) trên NQ/ES/XAU cho displacement sạch hơn — nhưng cũng biến động hơn; nếu chưa quen, đứng ngoài 1–2 phút đầu để tránh whipsaw phát hành tin.

---

## 8. Biến thể nâng cao — 08:30 phải đồng hướng DOL của 15m/H1 (Nested)

![[NY0830-Nested-HTF.svg|697]]

> [!important] 1m chỉ là trigger — 15m/H1 mới quyết định PHE
> Sai lầm nâng cao phổ biến: thấy một chuỗi raid + MSS đẹp trên 1m và vào, nhưng nó **ngược** với draw on liquidity của khung 15m/H1. Kết quả: bạn đang counter-trend cú đẩy lớn hơn và thường bị "nuốt".

**Quy trình đồng hướng (xem [[32 - Top-down Analysis (Multiple Timeframes)]]):**
1. **15m/H1:** xác định bias + DOL. Nếu DOL là BSL phía trên → sau 08:30 **chỉ tìm BUY**. Nếu DOL là SSL phía dưới → **chỉ tìm SELL**.
2. Chờ 08:30. Giá thường **raid ngược DOL trước** (ví dụ raid SSL trong ngày bullish) để nạp nhiên liệu — đây là bước "lấy thanh khoản đối ứng".
3. **Zoom 1m** sau raid: chờ MSS *theo hướng DOL 15m*, đánh dấu PD array, vào retest.
4. **Target = DOL của 15m/H1**, không chỉ IRL nhỏ trên 1m.

**Compound/lặp trong ngày:** một ngày trend mạnh có thể cho **nhiều** setup 08:30-style tại các macro kế tiếp (09:50, 10:00). Mỗi lần giá tạo relative equal mới → raid → MSS theo DOL là một cơ hội re-entry cùng hướng, miễn còn room tới DOL.

> [!warning] Bẫy nested
> Đừng short một MSS 1m khi 15m đang hướng lên một BSL chưa chạm tới. Cú "MSS xuống" đó thường chỉ là nhịp hồi kỹ thuật (raid SSL) *bên trong* một dòng chảy tăng lớn hơn.

---

## 9. Ví dụ chart

### Ví dụ đúng
![[NY0830-Example-Correct.svg|697]]

**Mô tả:** có bias 15m; chờ raid relative equal highs sau 08:30; MSS xác nhận; vào SIBI (PD array đầu tiên); stop ngoài toàn bộ range post-08:30.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp NQ/NAS100: đánh dấu (1) relative equal H/L, (2) cú raid sau 08:30, (3) nến MSS + PD array (OB/FVG/breaker), (4) entry retest, (5) stop ngoài range post-08:30, (6) TP tại DOL. Ghi giờ ET + có/không tin 08:30.*

### Ví dụ sai / dễ nhầm
![[NY0830-Example-Wrong.svg|697]]

**Bài học:** đây đều là các lỗi ICT nêu trực tiếp trong Lecture 1 (xem mục 11).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lần bạn pre-position trước 08:30 hoặc vào khi chưa có MSS — đánh dấu vì sao đó là front-run. Tư liệu quý cho review.*

---

## 10. Thực hành tốt nhất (Best Practices)

> [!summary]
> Đây là các thói quen chuẩn prop-firm — phân biệt trader chờ đúng trình tự time-based với trader "vào bừa lúc 08:30 vì có biến động". Mục tiêu: không front-run, không bỏ MSS, luôn đồng hướng DOL 15m, và sống sót qua ngày tin.

> [!tip] Quy tắc 08:30 Model (5 điều cốt lõi)
> 1. **Bias 15m trước tiên** — 1m chỉ là trigger, không phải bias.
> 2. **Chờ raid + MSS** — không bao giờ vào trước 08:30, không vào chỉ vì vừa raid.
> 3. **Vào PD array ĐẦU TIÊN** sau MSS, tại retest.
> 4. **Stop ngoài toàn bộ range post-08:30**, không chỉ tại swing MSS.
> 5. **TP theo DOL** — relative equal đối diện / H-L phiên trước.

### Quy trình pre-session (trước 08:00 NY)
1. **15m/H1:** viết ra bias hôm nay + DOL (BSL trên / SSL dưới) + đánh dấu FVG/inefficiency chưa lấp.
2. Đánh dấu các pool thanh khoản gần (relative equal, đỉnh/đáy phiên trước, NWOG/NDOG).
3. **Kiểm tra lịch tin 08:30** (CPI/NFP/PPI/FOMC ngày đó?) — nếu có tin lớn, chuẩn bị biến động cao & whipsaw.
4. Viết sẵn hai kịch bản: "*Nếu* raid BSL rồi MSS xuống → SELL tại [PD array]"; "*Nếu* raid SSL rồi MSS lên → BUY tại [PD array]".
5. Xác định ngưỡng **no-trade**: không có raid rõ / không MSS / ngược DOL 15m → đứng ngoài.

### Kỷ luật `missing_step` — nghi thức review tuần
- Với mỗi lệnh 08:30 thua/BE, bắt buộc điền `missing_step`: `raid` (front-run, chưa có raid), `mss` (vào khi chưa MSS), `context15m` (ngược DOL 15m), `pdarray` (đợi hồi quá sâu, sai PD array), `stop` (stop tại swing MSS thay vì ngoài range), `news` (bị whipsaw phát hành tin).
- Cuối tuần ([[07 - Reviews]]): giá trị nào >40% lệnh thua = ưu tiên sửa tuần sau; gắn `[[Mistake - ...]]`.

### Kỳ vọng thực tế
- **Không phải ngày nào 08:30 cũng cho setup A.** Ngày không tin, không có DOL rõ, hoặc range chặt → thường no-trade. Chỉ tính là một setup khi đủ **raid + MSS + PD array đồng hướng DOL**.
- Ngày có tin lớn = cơ hội displacement sạch, nhưng cũng rủi ro whipsaw — nếu chưa quen, chờ nến tin đầu tiên đóng xong.

### Scale size chỉ sau khi có dữ liệu
- Tối thiểu **≥30 mẫu backtest** 08:30 (tag frontmatter đầy đủ) qua [[04 - Backtesting|_Backtest Dashboard]], rồi forward-test 15–20 lệnh trước khi về ≤0.5%/lệnh. Backtest riêng ngày-có-tin vs ngày-không-tin — win-rate thường khác nhau đáng kể.

### Amateur vs Professional

| Khía cạnh | Amateur | Professional (chuẩn prop-firm) |
|---|---|---|
| Trước 08:30 | Đoán hướng, vào sớm | Chỉ map kịch bản, chờ trigger |
| Sau khi raid | Vào ngay vì "đã quét" | Chờ MSS xác nhận |
| Context 15m | Chỉ nhìn 1m | Chỉ đánh theo DOL 15m/H1 |
| Chọn PD array | Đợi hồi sâu nhất | Vào PD array đầu tiên sau MSS |
| Ngày có tin lớn | Vào ngay lúc phát hành | Chờ nến tin đóng, tránh whipsaw |
| Stop | Tại swing MSS | Ngoài toàn bộ range post-08:30 |
| Sau lệnh thua | Trade gỡ | Ghi `missing_step`, chờ setup thật |

> [!tip]
> Tóm một câu: **"Bias từ 15m, chờ raid + MSS sau 08:30, vào PD array đầu tiên đồng hướng DOL — không đoán, không front-run."**

---

## 11. Lỗi thường gặp (theo Lecture 1)

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Pre-position trước 08:30 | Vào lệnh khi chưa có cú raid | Đoán mò, không có trigger | Cú sweep post-08:30 mới là trigger |
| Bỏ qua MSS | Vào ngay khi vừa raid | Thanh khoản lấy rồi nhưng chưa đảo | MSS là bước xác nhận bắt buộc |
| Không có context 15m | Chỉ nhìn 1m | Dễ đánh ngược DOL lớn | Bias + DOL đến từ 15m; 1m chỉ trigger |
| Sai PD array | Đợi hồi quá sâu | Lỡ lệnh / entry xấu | Vào PD array đầu tiên sau MSS |
| Stop quá chặt | Đặt tại swing MSS | Bị wick quét vô lý | Stop ngoài toàn bộ range post-08:30 |
| Whipsaw tin | Vào đúng giây phát hành CPI/NFP | Nến tin quét cả hai chiều | Chờ nến tin đầu đóng xong |

---

## 12. Flashcards / Active Recall

**Q1 — Ba khung thời gian của mô hình và vai trò?**
15m = bias + DOL; 5m = cấu trúc; 1m = relative equal H/L + trigger.

**Q2 — Trình tự trigger cốt lõi là gì?**
Raid relative equal (sau 08:30) → MSS → vào PD array đầu tiên tại retest.

**Q3 — Stop đặt ở đâu?**
Ngoài toàn bộ range post-08:30 (trên đỉnh cho short / dưới đáy cho long), không chỉ tại swing MSS.

**Q4 — Vì sao khung giờ 08:30 đặc biệt?**
Trùng phát hành tin kinh tế Mỹ + đầu NY AM killzone → volume/biến động cao, "cớ" để raid thanh khoản rồi đảo chiều.

**Q5 — Vì sao phải đồng hướng DOL 15m?**
Vì 1m chỉ là trigger; một MSS 1m ngược DOL 15m thường chỉ là nhịp hồi (raid) bên trong dòng chảy lớn hơn — đánh theo nó là counter-trend.

**Q6 — PD array nào ưu tiên nhất?**
Unicorn (Breaker+FVG overlap) nếu có; kế đến FVG sạch, rồi OB, cuối cùng breaker.

---

## 13. Liên kết với Trade Journal

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

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: 0830-NY # 0830-NY | 0700-IFVG | Unicorn | ICT-2022 | MMBM | MMSM
bias: bearish # bullish | bearish (theo DOL 15m)
raid: BSL # BSL | SSL (đã raid gì post-08:30)
mss: true # đã có MSS xác nhận
pd_array: SIBI # OB | BISI | SIBI | breaker | unicorn
first_touch: true # vào PD array đầu tiên
news_0830: CPI # CPI | NFP | PPI | none
htf_dol_aligned: true # đồng hướng DOL 15m/H1
rr_planned: 3.0
missing_step: none # none | raid | mss | context15m | pdarray | stop | news
```

> [!tip]
> Với lệnh thua, ghi `missing_step` — phổ biến nhất là `mss` (vào khi chưa MSS) và `context15m` (ngược DOL 15m).

---

## 14. Lesson Learned

### Bài học chính
- 08:30 là mô hình **time-based**: chờ đúng cửa sổ, để thị trường tự lộ diện qua raid + MSS.
- **Bias từ 15m**, trigger từ 1m; luôn đồng hướng DOL 15m/H1.
- Vào **PD array đầu tiên** sau MSS (ưu tiên unicorn > FVG > OB > breaker), tại retest.
- **Stop ngoài toàn bộ range post-08:30**; target = DOL kế.
- Ngày có tin = displacement sạch nhưng whipsaw cao — chờ nến tin đóng.

### Quy tắc cá nhân rút ra
- [ ] Tôi không bao giờ vào trước 08:30 hay chỉ vì "vừa raid".
- [ ] Tôi luôn chờ MSS xác nhận.
- [ ] Tôi chỉ đánh theo DOL của 15m/H1.
- [ ] Tôi đặt stop ngoài toàn bộ range post-08:30.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc khi trade
> **"Không phải giá đi ĐÂU, mà là KHI NÀO. Chờ raid, chờ MSS, vào PD array đầu tiên đồng hướng DOL — rồi mới bấm lệnh."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa | | Relative equal, PD array, MSS? |
| Hiểu cơ chế thời gian (WHY) | | Vì sao 08:30 đặc biệt? |
| Nhận diện relative equal H/L | | Trong thời gian thực? |
| Chờ raid + MSS đúng | | Không front-run? |
| Chọn PD array đầu tiên đồng hướng DOL | | Không đợi hồi quá sâu, không ngược 15m? |
| Áp dụng vào trade thực tế | | Entry thật ở retest sau MSS? |
| Review sau trade | | Có gắn `missing_step` + review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập ≥20–30 setup tag `[[08:30 AM NY Model]]`.
- [ ] Review theo `missing_step`: hay sai ở `mss`, `context15m`, hay `pdarray`.
- [ ] Thống kê win-rate theo `news_0830` (ngày có tin vs không), `pd_array`, và `htf_dol_aligned`.
- [ ] Cập nhật rule khi đủ mẫu; nâng `confidence` khi đạt mastery.
