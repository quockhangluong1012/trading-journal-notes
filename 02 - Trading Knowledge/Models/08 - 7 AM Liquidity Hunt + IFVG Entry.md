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
  - 15m
  - 5m
  - 1m
  - 15s (entry tinh)
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
  - "[[17 - Inverse Fair Value Gap - iFVG]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[21 - Market Structure Shift]]"
  - "[[31 - Standard Deviation]]"
  - "[[40 - Macro Times]]"
prerequisites:
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[17 - Inverse Fair Value Gap - iFVG]]"
  - "[[21 - Market Structure Shift]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
common_mistakes:
  - Pre-position trước 07:00
  - Đánh dấu sai IFVG
  - Quên lưu ý 30 phút đầu
---

# 08 - 07:00 AM Liquidity Hunt + IFVG Entry

> [!info] Link
> [ICT 2024 Mentorship Lecture 2 Notes — 07:00 AM IFVG Model + PDF](https://innercircletrader.net/tutorials/ict-2024/mentorship-lecture-2/)

> [!summary] Tóm tắt 1 câu
> **Mô hình 07:00 AM (ICT 2024, Lecture 2) chuyển entry từ mốc 08:30 sang nhịp hồi AM-session sau 07:00: giá hồi về range London, hunt relative equal highs/lows, tạo [[21 - Market Structure Shift|MSS]]; vào lệnh tại 50% CE ([[10 - Consequent Encroachment (Mean Threshold)|consequent encroachment]]) của [[17 - Inverse Fair Value Gap - iFVG|IFVG]] (FVG đầu tiên trước cú hunt) — hoặc breaker nếu không có IFVG; chốt lời bằng Fib -2/-2.5.**

> [!important] Nguyên tắc cốt lõi
> **IFVG là FVG ĐẦU TIÊN ngay trước cú stop-hunt** — sau MSS nó bị đảo vai (support↔resistance) và trở thành vùng nhạy nhất. Entry chuẩn là **50% CE của IFVG**, không phải vào lúc MSS. Và luôn nhớ **lưu ý 30 phút đầu**: sau 07:00/08:00/09:00 giá thường đi NGƯỢC bias để hunt thanh khoản trước.

> [!tip] Bản đồ đọc note này
> Mục 1–2 = *thời điểm + định nghĩa*. Mục 3 = *WHY (vì sao IFVG nhạy)*. Mục 4–7 = *HOW (bearish/bullish, Fib, lưu ý 30')*. Mục 8–11 = *thị trường, so 08:30, ví dụ*. Mục 12–18 = *thực chiến & prop-firm*. Mới học: 1→7; đã trade: nhảy 8–12.

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

![[AM0700IFVG-WhyItWorks.svg|697]]

> [!important] Vì sao "FVG ĐẦU TIÊN trước hunt" chứ không phải FVG nào khác?
> FVG đầu tiên ngay trước cú stop-hunt là **dấu vết cuối cùng của dòng lệnh sai hướng** trước khi thuật toán đảo chiều. Đó là nơi tập trung nhiều lệnh mắc kẹt nhất. Khi giá đóng xuyên qua nó (đảo vai) rồi quay lại test, đây là mức phải được "giải quyết" → phản ứng nhạy và dứt khoát nhất. Đánh dấu FVG sau đó (đã nằm trong chân displacement) hoặc FVG trước đó (quá xa cú hunt) đều cho entry kém nhạy hơn.

> [!note] Vì sao AM session (sau 07:00) là bối cảnh lý tưởng
> Đặc tính đầu phiên AM là giá **hồi lại vào trong range London** — và range London (đỉnh/đáy) chính là draw on liquidity. Cú hồi này tạo ra hunt relative equal + IFVG một cách tự nhiên. Đây là lý do bạn *chờ giá hồi về range*, không đuổi theo cú mở phiên. Liên hệ [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]: đám đông đặt lệnh quanh relative equal → trở thành nhiên liệu cho cú hunt.

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

## 6. Mục tiêu Fibonacci + Entry CE

![[AM0700IFVG-Advanced-Fib-Targets.svg|697]]

Dùng Fib với inputs **0 · 0.5 · 1 · -2 · -2.5**. Vẽ từ swing hình thành post-07:00 hunt **về** giá mở cửa 07:00. Chốt **theo bậc thang**: một phần tại **-2**, phần còn lại tại **-2.5** — đóng hết tại -2 sẽ bỏ lỡ phần lớn của move. Có thể thay bằng next draw on liquidity làm target. Liên hệ [[31 - Standard Deviation|Standard Deviation]] projections.

![[AM0700IFVG-CE-Entry.svg|697]]

> [!example] Mẫu ghi nhanh — 07:00 IFVG (Bearish)
> ```text
> DOL: London H = [level], London L = [level]
> (1) Sau 07:00: giá hồi vào range, hunt relative equal highs @ [level]
> (2) MSS: đóng dưới [swing low] + displacement xuống
> (3) IFVG = FVG đầu tiên TRƯỚC hunt: [low]-[high], CE = [mid]
> (4) Entry SELL @ 50% CE [mid] (breaker dự phòng nếu không có IFVG)
> (5) Stop trên swing high post-07:00 @ [level]
> (6) Fib: 0=[swing high] → 1=[open 07:00]; T1 = -2, T2 = -2.5
> Macro: 07:00 / 08:50 / 09:50 | Lưu ý 30': counter-move đầu giờ
> Invalid: đóng nến trên swing high post-07:00
> ```

---

## 7. Lưu ý 30 phút đầu — kỳ vọng move NGƯỢC

![[AM0700IFVG-Advanced-30min-Reversal.svg|697]]

**Sau 07:00, 08:00 và 09:00, trong 30 phút đầu (pre-session range), giá thường đi NGƯỢC** với relative trend / relative equal H/L. Ví dụ: bias bullish nhưng 30 phút đầu giá đi bearish để hunt thanh khoản trước khi đảo. Đây là cảnh báo counter-move **có sẵn trong khung Lecture 2** — quên nó = vào ngược move thật.

> [!warning] Đây là "bộ lọc kiên nhẫn" của model
> Nhiều lệnh thua đến từ việc vào ngay khi thấy giá đi *đúng* bias trong 5–10 phút đầu — nhưng đó thường là counter-move sắp bị đảo. Hãy để 30 phút đầu **lộ ra cú hunt** (thường ngược bias), *sau đó* mới tìm MSS + IFVG theo hướng thật.

---

## 8. 07:00 IFVG so với 08:30 NY — chọn model nào?

![[AM0700IFVG-vs-0830.svg|697]]

Hai model cùng họ ICT 2024, cùng trình tự hunt → MSS, nhưng khác ở **vùng entry chính xác** và **cách định target**.

| Khía cạnh | 07:00 IFVG (Lecture 2) | 08:30 NY (Lecture 1) |
|---|---|---|
| DOL tham chiếu | Đỉnh/đáy **London** (giá hồi về range) | Từ **bias 15m** (BSL/SSL) |
| Trigger | 07:00 / 08:00 / 09:00 | Sau **08:30** (giờ tin Mỹ) |
| Vùng entry | **50% CE của IFVG** (breaker dự phòng) | PD array **đầu tiên** bất kỳ (OB/FVG/breaker) |
| Target | Next DOL hoặc **Fib -2 / -2.5** | Draw on liquidity kế (cấu trúc) |
| Điểm mạnh | Entry precision, target đo được | Linh hoạt PD array, đơn giản |
| Khi nào ưu tiên | Muốn precision cao, có IFVG rõ | Ngày có tin 08:30, PD array rõ |

> [!tip] Khi hai model hội tụ
> Nếu IFVG **trùng breaker** (chồng lấn) → thực chất là một [[07 - Unicorn Model|Unicorn]], chất lượng **A+**. Và nếu setup 07:00 chưa hoàn tất, một setup [[08 - 08 30 AM NY Model|08:30]] có thể "nối tiếp" cùng hướng ngay sau đó — nhiều ngày cho cả hai cơ hội.

---

## 9. Ví dụ chart

### Ví dụ đúng
![[AM0700IFVG-Example-Correct.svg|697]]

**Mô tả:** dùng London H/L làm DOL; hunt relative equal highs sau 07:00; MSS; đánh dấu IFVG (FVG đầu tiên); vào 50% CE; chốt Fib -2/-2.5.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp NQ/NAS100: đánh dấu (1) đỉnh/đáy London, (2) cú hunt sau 07:00, (3) MSS, (4) IFVG = FVG đầu tiên trước hunt + mức 50% CE khớp lệnh, (5) stop ngoài swing post-07:00, (6) Fib -2/-2.5. Ghi giờ ET.*

### Ví dụ sai / dễ nhầm
![[AM0700IFVG-Example-Wrong.svg|697]]

**Bài học:** các lỗi này được ICT nêu trực tiếp trong Lecture 2 — xem mục 11.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lần bạn đánh dấu sai IFVG (không phải FVG đầu tiên) hoặc vào ngược trong 30' đầu — đánh dấu vì sao. Tư liệu quý cho review.*

---

## 10. Thực hành tốt nhất (Best Practices)

> [!summary]
> Thói quen chuẩn prop-firm cho model 07:00 IFVG — phân biệt trader vào đúng 50% CE của IFVG thật với trader "thấy FVG nào cũng vào". Mục tiêu: đánh dấu đúng IFVG, tôn trọng lưu ý 30', chốt bậc thang Fib, và không front-run.

> [!tip] Quy tắc 07:00 IFVG Model (5 điều cốt lõi)
> 1. **London H/L = DOL** — tham chiếu duy nhất cần từ trước 07:00.
> 2. **Không dự đoán** — chờ relative equal in ra, chờ hunt, chờ MSS.
> 3. **IFVG = FVG ĐẦU TIÊN trước hunt** — đánh dấu sai = entry kém nhạy.
> 4. **Vào 50% CE của IFVG** (breaker là dự phòng), không vào lúc MSS.
> 5. **Chốt bậc thang -2 / -2.5**, tôn trọng lưu ý 30 phút đầu.

### Quy trình pre-session (trước 07:00 NY)
1. Đánh dấu **đỉnh & đáy phiên London** (DOL) — chỉ cần bấy nhiêu nếu bạn còn mới.
2. Kiểm tra lịch tin: có tin 08:30 (CPI/NFP) ngày đó không → ảnh hưởng biến động cú hunt.
3. Viết sẵn kịch bản: "*Nếu* giá hồi về range rồi hunt relative equal highs → chờ MSS xuống → SELL 50% CE của IFVG đầu tiên; Fib -2/-2.5."
4. Đặt sẵn ngưỡng **no-trade**: không hồi về range / không có IFVG rõ / chưa qua 30' hunt → đứng ngoài.

### Kỷ luật `missing_step` — nghi thức review tuần
- Với mỗi lệnh 07:00 thua/BE, bắt buộc điền `missing_step`: `prehunt` (front-run, chưa có hunt), `ifvg` (đánh dấu sai IFVG), `mss` (vào khi chưa MSS), `30min` (vào ngược trong 30' đầu), `ce` (vào lệch 50% CE), `target` (chốt hết tại -2 hoặc sai Fib), `stop` (stop trong swing thay vì ngoài).
- Cuối tuần ([[07 - Reviews]]): giá trị nào >40% lệnh thua = ưu tiên sửa; gắn `[[Mistake - ...]]`.

### Kỳ vọng thực tế
- **Không phải ngày nào cũng có IFVG rõ.** Nếu không hình thành IFVG "đầu tiên trước hunt" sạch, dùng breaker dự phòng — hoặc bỏ qua. Chỉ tính là setup khi đủ **hunt + MSS + IFVG/breaker theo hướng DOL**.
- Lưu ý 30' đầu là bộ lọc: đừng sốt ruột vào ngay đầu giờ.

### Scale size chỉ sau khi có dữ liệu
- Tối thiểu **≥30 mẫu backtest** 07:00 IFVG (tag frontmatter đầy đủ) qua [[04 - Backtesting|_Backtest Dashboard]], rồi forward-test 15–20 lệnh trước khi về ≤0.5%/lệnh. Backtest riêng: tỉ lệ đạt -2 vs -2.5 để tinh chỉnh cách chốt bậc thang.

### Amateur vs Professional

| Khía cạnh | Amateur | Professional (chuẩn prop-firm) |
|---|---|---|
| Trước 07:00 | Đoán hướng, vào sớm | Chỉ đánh dấu London H/L, chờ |
| 30 phút đầu | Vào ngay khi giá đi "đúng bias" | Chờ counter-move hunt lộ ra |
| Đánh dấu IFVG | FVG nào cũng nhận | Chỉ FVG **đầu tiên** ngay trước hunt |
| Entry | Market lúc MSS | Limit tại 50% CE của IFVG |
| Chốt lời | Đóng hết tại -2 | Bậc thang -2 (BE) rồi -2.5 |
| Stop | Trong swing MSS | Ngoài toàn bộ swing post-07:00 |
| Sau lệnh thua | Trade gỡ | Ghi `missing_step`, chờ setup thật |

> [!tip]
> Tóm một câu: **"London H/L làm mốc, chờ hunt sau 07:00, vào 50% CE của IFVG ĐẦU TIÊN, chốt bậc thang Fib — tôn trọng 30' đầu."**

---

## 11. Lỗi thường gặp (theo Lecture 2)

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Pre-position trước 07:00 | Vào khi chưa có hunt | Đoán mò, không trigger | Cú sweep post-07:00 mới là trigger |
| Sai IFVG | Đánh dấu FVG sau/trước không đúng | Entry kém nhạy, phản ứng yếu | IFVG = FVG **đầu tiên** ngay trước hunt |
| Bỏ qua MSS | Vào bằng wick đơn thuần | Chưa xác nhận đảo chiều | MSS là bước xác nhận bắt buộc |
| Quên lưu ý 30 phút | Vào ngược move thật đầu giờ | Bị counter-move quét | Nhớ counter-move 30′ sau 07/08/09 |
| Stop quá chặt | Đặt tại pivot MSS | Bị wick quét vô lý | Stop ngoài toàn bộ swing post-07:00 |
| Chốt một phát | Đóng hết tại -2 | Bỏ lỡ phần lớn move | Chốt bậc thang -2 rồi -2.5 |

---

## 12. Flashcards / Active Recall

**Q1 — IFVG trong mô hình này là FVG nào?**
FVG **đầu tiên ngay trước cú stop-hunt** — sau MSS nó đảo vai, là vùng nhạy nhất.

**Q2 — Vào lệnh tại đâu?**
**50% CE (consequent encroachment)** của IFVG; nếu không có IFVG thì vào breaker.

**Q3 — TP được xác định thế nào?**
Next DOL, hoặc Fib (0/0.5/1/-2/-2.5) từ swing post-07:00 về open 07:00 — chốt bậc thang -2 rồi -2.5.

**Q4 — Vì sao IFVG đầu tiên nhạy nhất?**
Vì nó là dấu vết cuối cùng của dòng lệnh sai hướng ngay trước khi đảo chiều; khi bị đóng xuyên rồi test lại, đây là nơi lệnh mắc kẹt phải được giải quyết.

**Q5 — Lưu ý 30 phút đầu là gì?**
Sau 07:00/08:00/09:00, 30' đầu giá thường đi NGƯỢC bias để hunt thanh khoản trước khi đảo — đừng vào vội theo move đầu giờ.

**Q6 — Khác biệt chính với 08:30 NY?**
07:00 chuyên **50% CE của IFVG** + target Fib -2/-2.5; 08:30 vào **PD array bất kỳ** (OB/FVG/breaker) tại retest + target theo DOL cấu trúc.

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
model: 0700-IFVG # 0700-IFVG | 0830-NY | Unicorn | ICT-2022 | MMBM | MMSM
bias: bearish # bullish | bearish
hunt: relEQ-highs # relEQ-highs | relEQ-lows (đã hunt gì post-07:00)
mss: true
entry_type: ifvg-ce # ifvg-ce | breaker (dự phòng)
ce_50: true # vào đúng 50% CE
fib_target: -2.5 # -2 | -2.5 | next-DOL
london_dol: true # dùng London H/L làm DOL
respected_30min: true # tôn trọng lưu ý 30 phút đầu
rr_planned: 5.0
missing_step: none # none | prehunt | ifvg | mss | 30min | ce | target | stop
```

> [!tip]
> Với lệnh thua, ghi `missing_step` — phổ biến nhất là `ifvg` (đánh dấu sai IFVG) và `30min` (vào ngược trong 30' đầu).

---

## 14. Lesson Learned

### Bài học chính
- IFVG = **FVG đầu tiên trước hunt**, đảo vai sau MSS → vùng nhạy nhất; vào **50% CE** (breaker dự phòng).
- **London H/L = DOL**; chờ giá hồi về range, hunt relative equal, rồi MSS.
- **Tôn trọng 30 phút đầu** — kỳ vọng counter-move hunt trước khi đảo thật.
- **Chốt bậc thang Fib -2 / -2.5** (không đóng hết tại -2); stop ngoài swing post-07:00.
- Khi IFVG trùng breaker → Unicorn A+.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ đánh dấu IFVG là **FVG đầu tiên** ngay trước hunt.
- [ ] Tôi chờ hết 30' đầu để hunt lộ ra, không vào vội.
- [ ] Tôi vào tại 50% CE, không vào lúc MSS.
- [ ] Tôi chốt bậc thang -2 rồi -2.5.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc khi trade
> **"London H/L làm mốc. Chờ hunt, chờ MSS, vào 50% CE của IFVG đầu tiên. Tôn trọng 30' đầu, chốt bậc thang Fib."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa IFVG | | Phân biệt FVG / IFVG / breaker? |
| Hiểu cơ chế (WHY) | | Vì sao FVG đầu tiên nhạy nhất? |
| Đánh dấu đúng IFVG | | Chọn đúng "FVG đầu tiên trước hunt"? |
| Chờ hunt + MSS, tôn trọng 30' | | Không front-run, không vào ngược 30' đầu? |
| Entry 50% CE + Fib target | | Vào đúng CE, chốt bậc thang? |
| Áp dụng vào trade thực tế | | Entry thật ở 50% CE của IFVG? |
| Review sau trade | | Có gắn `missing_step` + review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập ≥20–30 setup tag `[[07:00 AM Liquidity Hunt + IFVG Entry]]`.
- [ ] Review theo `missing_step`: hay sai ở `ifvg`, `30min`, hay `ce`.
- [ ] Thống kê win-rate theo `entry_type` (ifvg-ce vs breaker), `fib_target` (-2 vs -2.5), `respected_30min`.
- [ ] Cập nhật rule khi đủ mẫu; nâng `confidence` khi đạt mastery.
