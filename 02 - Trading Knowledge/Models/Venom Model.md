---
type: ict-concept
concept: Venom Model
aliases:
  - Venom Model
  - Venom
  - The Venom Model
  - ICT Venom Model
tags:
  - trading/ict/concept
  - trading/study
  - "#Venom"
status: developing
category: Entry Model
timeframes:
  - D1
  - H1
  - M15
  - M5
  - M1
markets:
  - NDX
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
models:
  - ICT 2022
  - Silver Bullet
  - OTE
  - AMD
importance: 4
confidence: 2
last_reviewed: 2026-06-24
created: 2026-06-24
updated: 2026-06-24
related_concepts:
  - "[[18 - Kill Zones]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
prerequisites:
  - "[[18 - Kill Zones]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
common_mistakes:
  - "[[Mistake - Skip Liquidity Sweep]]"
  - "[[Mistake - Chase Displacement]]"
  - "[[Mistake - Overtrading]]"
---

# Venom Model

> [!summary] Tóm tắt 1 câu
> **Venom Model là một entry model dựa trên THỜI GIAN: trong cửa sổ kill zone (đặc biệt quanh NY open), giá quét thanh khoản của một phiên trước đó (Asia/London hoặc đỉnh/đáy session), rồi displacement phá cấu trúc để lại FVG — mình vào khi giá retrace về FVG, target là pool liquidity đối diện.**

> [!important] Nguyên tắc cốt lõi
> **Venom = TIME + LIQUIDITY SWEEP + DISPLACEMENT. Sức mạnh nằm ở việc "tiêm nọc" vào đúng cửa sổ thời gian: chờ giá quét liquidity của phiên trước trong kill zone, rồi mới displacement theo bias. Sai thời gian (ngoài cửa sổ) hoặc thiếu sweep = không phải Venom.**
> Đây là một biến thể time-based gần với Silver Bullet: cùng logic ICT 2022 (sweep → MSS → FVG) nhưng neo chặt vào khung giờ và liquidity của session.

---

## 1. Định nghĩa

**Khái niệm:**
Venom Model là **mô hình entry theo thời gian (time-based)** trong hệ ICT, tập trung vào việc khai thác **liquidity của các phiên trước** (Asia, London) hoặc đỉnh/đáy session ngay trong một **cửa sổ kill zone**, đặc biệt quanh **New York open**. Khi giá "tiêm nọc" — tức quét pool liquidity của session — và sau đó **displacement** theo bias để lại FVG, đó là tín hiệu vào lệnh. Về cơ chế, Venom dùng đúng chuỗi [[ICT 2022 Model]] nhưng đặt nó trong một khung thời gian và một bộ liquidity reference cụ thể của phiên.

**Chuỗi điển hình của Venom:**
1. **Bias / khung tham chiếu:** xác định hướng (HTF bias) và các pool liquidity của phiên trước (Asia high/low, London high/low, PDH/PDL).
2. **Time window (cửa sổ Venom):** chỉ săn trong kill zone — phổ biến là quanh NY open / NY AM (xem [[18 - Kill Zones]]).
3. **Liquidity sweep ("venom strike"):** trong cửa sổ đó, giá quét một pool session (ví dụ quét London low) rồi reclaim.
4. **Displacement + MSS:** một move mạnh phá cấu trúc theo bias, để lại FVG.
5. **Entry tại FVG:** giá retrace về FVG (quanh CE), vào lệnh.
6. **Target:** pool liquidity đối diện (session high/low ngược phía, PDH/PDL).

**Bản chất:** Venom mã hóa quan sát rằng tại NY open, market maker thường **quét thanh khoản tích tụ từ phiên Á/Âu** trước khi chạy hướng thật trong ngày. Nó kết hợp **time** (chỉ trong cửa sổ) với **liquidity của session** làm reference, giúp lọc nhiễu và tập trung vào thời điểm xác suất cao nhất.

**Mục đích trong ICT:**
- Cho một **khung giờ + reference liquidity** cụ thể để chờ setup, thay vì săn cả ngày.
- Tận dụng động lực của **NY open** (volume, manipulation đầu phiên).
- Định nghĩa rõ pool nào để quét và pool nào làm target trong ngày.

**Vì sao khái niệm này quan trọng:**
Nhiều trader thua vì giao dịch **sai thời điểm** (giữa phiên chết, hoặc trước khi liquidity của session bị quét). Venom buộc bạn chỉ hành động trong cửa sổ chất lượng cao, sau khi "nọc" đã được tiêm (sweep).

**Nó giúp trả lời câu hỏi nào trên chart?**
- Đang ở trong cửa sổ Venom (kill zone) chưa?
- Giá đã quét liquidity của phiên trước (Asia/London/PD) chưa?
- Có displacement + FVG theo bias sau cú quét không?
- Pool đối diện nào là target trong ngày?

### Venom không phải là gì
- Không phải tín hiệu vào bất kỳ lúc nào — nó neo vào **time window**.
- Không phải "thấy FVG là vào" — phải có sweep liquidity session trước.
- Không phải bỏ qua HTF bias / premium-discount.
- Không phải scalping bừa quanh NY open mà không có reference.
- Không đảm bảo thắng; vẫn cần risk management.

---

## 2. Bối cảnh sử dụng

### Các bước & khái niệm tương ứng

| Bước | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| 1 | Bias + reference | [[12 - Daily Bias]], [[19 - Liquidity]] | Hướng gì? Pool session nào? |
| 2 | Time window | [[18 - Kill Zones]] | Đang trong cửa sổ Venom (NY open) chưa? |
| 3 | Liquidity sweep | [[20 - Liquidity Sweep]] | Đã quét Asia/London/PD pool chưa? |
| 4 | Displacement + MSS | [[Displacement]], [[21 - Market Structure Shift]] | Có phá cấu trúc + FVG không? |
| 5 | FVG entry | [[Fair Value Gap]], [[Optimal Trade Entry]] | FVG/CE ở đâu, đúng PD không? |
| 6 | Target | [[19 - Liquidity]] | Pool đối diện ở đâu? |

### Biến thể thường gặp
- **+ Silver Bullet:** Venom rất gần Silver Bullet — chạy chuỗi trong cửa sổ 1 giờ của kill zone ([[18 - Kill Zones]]).
- **+ ICT 2022 Model:** lõi entry chính là chuỗi [[ICT 2022 Model]] đặt trong time window.
- **+ OTE:** tinh chỉnh entry bằng OTE 62–79% trùng FVG ([[Optimal Trade Entry]]).
- **+ AMD:** sweep đầu NY ~ pha manipulation; displacement ~ distribution ([[02 - AMD]]).

> [!tip]
> Cách nhớ nhanh Venom: **"Đúng giờ → Tiêm nọc (sweep session) → Đẩy (displacement) → Vào FVG → Chạy về pool đối diện."** Thiếu "đúng giờ" hoặc "tiêm nọc" thì không phải Venom.

### Khi nào mô hình này có giá trị cao?
- [ ] Đang trong cửa sổ Venom (NY open / NY AM kill zone).
- [ ] Có pool liquidity session rõ (Asia/London high-low, PDH/PDL).
- [ ] HTF bias rõ ràng + giá ở premium/discount phù hợp.
- [ ] Sweep session + displacement để lại FVG sạch.
- [ ] Pool đối diện làm target có room.

### Khi nào nên bỏ qua?
- [ ] Ngoài cửa sổ thời gian (giữa phiên chết).
- [ ] Chưa quét liquidity session nào.
- [ ] Bias mơ hồ / ngược premium-discount.
- [ ] Sát tin tức lớn (làm nhiễu displacement đầu phiên).
- [ ] Không có target pool rõ.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Reference session pools:** Asia high/low, London high/low, PDH/PDL đánh dấu sẵn.
2. **Time window:** giá đang ở trong cửa sổ NY open / kill zone.
3. **Sweep session ("venom strike"):** giá quét một pool session rồi reclaim.
4. **Displacement + MSS:** move mạnh phá cấu trúc, để lại FVG.
5. **Retrace về FVG:** điểm vào (quanh CE), đúng PD.

### Ma trận nhận diện Venom (Long)

| Bước | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Bias | HTF bullish, target BSL | Bias mơ hồ → bỏ |
| Time | Trong cửa sổ NY open | Ngoài cửa sổ → không phải Venom |
| Sweep | Quét session low (Asia/London) + reclaim | Không sweep → bỏ |
| Displacement/MSS | Phá swing high + bullish FVG | Move yếu → bỏ |
| Entry | FVG ở discount | Ở premium → sai chỗ |
| Target | Session high / PDH | Không pool rõ → R:R kém |

### Điều kiện bắt buộc
- [ ] Đang trong cửa sổ thời gian Venom (kill zone).
- [ ] Đã quét một pool liquidity session.
- [ ] Có displacement + MSS để lại FVG theo bias.
- [ ] Xác định FVG/CE + invalidation.
- [ ] Pool đối diện làm target rõ.

### Điều kiện tăng xác suất
- [ ] FVG trùng OTE 62–79% / OB (confluence).
- [ ] Sweep đúng pool session quan trọng (London low/high).
- [ ] Đồng hướng HTF bias + AMD distribution.
- [ ] Target có room lớn (R:R cao).

### Điều kiện làm setup yếu đi
- Sweep mờ / không reclaim rõ.
- Displacement không dứt khoát, FVG bị lấp nhanh.
- Gần cuối cửa sổ thời gian (động lực cạn).
- Vướng tin tức cùng phiên.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Venom
> 1. **Đang trong cửa sổ Venom (NY open/kill zone) chưa?**
> 2. **Giá đã quét pool liquidity session nào chưa?**
> 3. **Có displacement + MSS để lại FVG theo bias không?**
> 4. **Entry/stop/target ở đâu, R:R bao nhiêu?**

### D1 / H1 — Bias & Reference
- **Bias:** Bullish / Bearish (xem [[12 - Daily Bias]]).
- **Reference pools:** Asia/London high-low, PDH/PDL.
- **Premium/Discount:** xác định vùng vào phù hợp với bias.

### M15 — Setup & Context
- **Pool sẽ bị sweep:** chọn pool session ngược hướng bias.
- **Chờ sweep + reclaim:** trong cửa sổ thời gian.
- **MSS + FVG:** ghi range FVG + CE, ví dụ `M15 bullish FVG 17840–17865, CE 17852`.

### M5 / M1 — Confirmation & Entry
- **Refine:** chờ M5/M1 retrace về FVG; có thể chờ M1 MSS xác nhận.
- **Entry:** tại FVG (quanh CE) / OTE trùng FVG.
- **Stop:** ngoài điểm sweep / đầu kia FVG.
- **Target:** pool session đối diện / PDH-PDL.

```text
Mẫu ghi nhanh — Venom Long
Bias (HTF): Bullish | Target: session high / PDH @ [level]
Time window: NY open / NY AM kill zone
(1) Sweep: session low (Asia/London) @ [level] + reclaim
(2) Displacement + MSS phá [swing high] → FVG
(3) FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop dưới sweep
(5) Target: session high / PDH [..]
Invalid: ngoài cửa sổ / đóng nến dưới FVG
```

> [!warning]
> **Time là một bộ lọc bắt buộc, không phải tùy chọn.** Một setup "đẹp" nhưng nằm ngoài cửa sổ Venom thì không phải Venom — động lực và xác suất của NY open chính là phần "nọc" của mô hình.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Trong cửa sổ thời gian Venom (kill zone).
- [ ] Có sweep pool liquidity session + reclaim.
- [ ] Displacement + MSS để lại FVG theo bias.
- [ ] Entry tại FVG (retrace), đúng premium/discount.
- [ ] Stop ngoài sweep; target pool đối diện rõ; R:R đạt.

### Setup bị vô hiệu khi
- [ ] Ngoài cửa sổ thời gian → không phải Venom.
- [ ] Chưa quét liquidity session.
- [ ] Displacement yếu / không để lại FVG.
- [ ] Giá **đóng nến xuyên qua FVG** (acceptance) → POI invalid.
- [ ] Entry ngược bias / sai premium-discount / chase.

### Mức độ "đủ điều kiện"

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Trong cửa sổ + sweep + displacement + FVG | **A+ Venom** | Thực thi theo plan |
| Có sweep + displacement nhưng FVG đã lấp | **Chờ POI khác** | Tìm FVG/OB tiếp theo |
| Setup đẹp nhưng ngoài cửa sổ | **Không phải Venom** | Bỏ hoặc xét model khác |
| Chưa quét session pool | **Chưa đủ** | Chờ "nọc" được tiêm |

> [!note]
> Venom là Silver Bullet "có chủ đích về liquidity session": ngoài time window, nó nhấn mạnh việc quét đúng pool của phiên trước. Khi bí, kiểm tra hai thứ: **đúng giờ chưa** và **đã quét session pool chưa**.

---

## 6. Ví dụ chart

### Ví dụ đúng — NY open: sweep London low → displacement → FVG entry → session high
![[paste-image-here.png]]

**Mô tả:**
HTF bias Bullish, target là session high / PDH. **(1)** Vào **NY open kill zone**, giá **quét London low** (liquidity session) rồi reclaim. **(2)** **Displacement tăng + MSS** phá swing high, để lại bullish FVG. **(3)** Giá retrace về FVG (quanh CE) → **entry**, stop dưới điểm sweep. **(4)** Giá chạy về **session high / PDH target**.

**Vì sao đây là ví dụ tốt:**
- Đúng cửa sổ thời gian (NY open) + quét đúng session pool.
- Đủ chuỗi sweep → displacement → FVG retrace.
- Entry ở discount, không chase; target pool rõ.

### Ví dụ sai / dễ nhầm — Vào ngoài cửa sổ, chưa quét session pool
![[paste-image-here.png]]

**Mô tả lỗi:**
Trader thấy một FVG đẹp **giữa phiên chết** (ngoài cửa sổ Venom) và vào ngay, dù **chưa có cú quét liquidity session** nào. Thiếu cả "đúng giờ" lẫn "tiêm nọc", giá đi loanh quanh rồi quét stop.

**Bài học:**
- Ngoài cửa sổ thời gian → không phải Venom, dù FVG có đẹp.
- Phải có sweep session pool trước displacement.
- Time + liquidity session là hai bộ lọc không thể bỏ.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[20 - Liquidity Sweep]]
- [[Displacement]]
- [[21 - Market Structure Shift]]
- [[Fair Value Gap]]
- [[Optimal Trade Entry]]
- [[27 - Premium Discount]]
- [[18 - Kill Zones]]
- [[02 - AMD]]
- [[ICT 2022 Model]]
- [[One Shot One Kill Trading Model]]

### Sequence mẫu — Venom Long (đầy đủ)
```text
(1) HTF Bullish bias + reference pools (Asia/London/PD)
(2) Trong cửa sổ Venom (NY open / NY AM kill zone)
(3) Sweep session low (+ reclaim) = "venom strike"
(4) Displacement tăng + MSS → bullish FVG
(5) Entry: retrace về FVG (quanh CE), lý tưởng trùng OTE/OB
(6) Stop dưới điểm sweep; Target: session high / PDH
(+ đồng hướng AMD distribution)
```

> [!note]
> Venom, Silver Bullet và [[ICT 2022 Model]] dùng chung lõi (sweep → MSS → FVG). Điểm khác của Venom là **neo vào time window NY open + liquidity của session trước**. Kết hợp tốt với [[One Shot One Kill Trading Model]] khi muốn chọn một phát chất lượng trong ngày.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy FVG đẹp
> Venom đòi hỏi ĐÚNG GIỜ + ĐÃ QUÉT SESSION POOL. Thiếu một trong hai thì không phải Venom.

### A. Context (HTF + session)
- [ ] Bias đã rõ: Bullish / Bearish.
- [ ] Reference pools (Asia/London/PD) đã đánh dấu.
- [ ] Location đúng premium/discount.
- [ ] Đang trong cửa sổ thời gian Venom.

### B. Execution (LTF)
- [ ] Đã có sweep session pool + reclaim.
- [ ] Có displacement + MSS để lại FVG.
- [ ] FVG sạch, xác định CE; lý tưởng trùng OTE/OB.
- [ ] Entry ở retrace về FVG, không chase.
- [ ] Stop ngoài sweep; target pool đối diện; R:R đạt.

### C. Quy tắc "không có lệnh"
- [ ] Ngoài cửa sổ thời gian → không trade.
- [ ] Chưa quét session pool → không trade.
- [ ] Ngược bias / sai premium-discount → không trade.
- [ ] Chỉ vào được bằng chase → không trade.
- [ ] Sát tin lớn → cân nhắc bỏ.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bỏ qua time window | Vào giữa phiên chết | Mất phần "nọc" của mô hình | Chỉ săn trong cửa sổ NY open |
| Không quét session pool | Vào trước khi có sweep | Thiếu trigger | Chờ sweep Asia/London/PD |
| Chase displacement | Vào ngay khi thấy nến lớn | Bỏ retrace, R:R xấu | Chờ giá về FVG |
| Trade ngược bias | Long/Short ngược HTF | Xác suất thấp | Đồng hướng Daily Bias |
| Sai premium/discount | Long ở premium, Short ở discount | Entry chase | Long discount, Short premium |
| FVG không từ displacement | Gọi gap thường là FVG | Không có intent | Yêu cầu displacement phá cấu trúc |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = session pool đối diện |

---

## 10. Câu hỏi tự kiểm tra

- Mình có đang ở trong cửa sổ thời gian Venom không?
- Giá đã quét pool liquidity session nào chưa?
- Có displacement + MSS để lại FVG theo bias không?
- FVG có sạch, đúng premium/discount không?
- Entry là retrace về FVG hay đang chase?
- Stop (ngoài sweep) và target (pool đối diện) ở đâu, R:R bao nhiêu?
- Nếu không trade, lý do "No Trade" là time, sweep, hay bias?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Ba thành phần cốt lõi của Venom Model là gì?
**Đáp:** Time (cửa sổ kill zone, đặc biệt NY open) + Liquidity sweep của session trước + Displacement (để lại FVG).

### Q2
**Hỏi:** Venom khác Silver Bullet / ICT 2022 ở điểm nào?
**Đáp:** Cùng lõi sweep→MSS→FVG, nhưng Venom neo chặt vào time window NY open và dùng liquidity của session trước (Asia/London/PD) làm reference.

### Q3
**Hỏi:** "Venom strike" nghĩa là gì?
**Đáp:** Cú quét pool liquidity session (ví dụ London low/high) trong cửa sổ thời gian — bước trigger trước displacement.

### Q4
**Hỏi:** Điều gì làm một setup KHÔNG phải Venom dù FVG đẹp?
**Đáp:** Nếu nằm ngoài cửa sổ thời gian hoặc chưa quét session pool → không phải Venom.

### Q5
**Hỏi:** Entry và stop của Venom Long đặt ở đâu?
**Đáp:** Entry tại FVG (quanh CE) ở discount; stop dưới điểm sweep / dưới đầu kia FVG.

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
> Nếu vault có folder riêng như `Trades`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: Venom # Venom | ICT-2022 | OSOK | MMBM | MMSM
bias: bullish # bullish | bearish
time_window: NY-open # cửa sổ thời gian
session_pool_swept: London-low # Asia/London/PDH/PDL
displacement_mss: true
fvg_entry: true
entry_location: Discount
target: session-high # session high/low, PDH/PDL
rr_planned: 3.0
missing_step: none # none | time | sweep | displacement | retrace
```

> [!tip]
> Với các lệnh Venom thua, ghi `missing_step` — thường lỗi rơi vào `time` (ngoài cửa sổ) hoặc `sweep` (chưa quét session pool).

---

## 13. Lesson Learned

### Bài học chính
- Venom là entry model **time-based**: đúng cửa sổ NY open + quét đúng session pool.
- Lõi vẫn là chuỗi **sweep → displacement/MSS → FVG → entry → target**.
- **Time và liquidity session** là hai bộ lọc bắt buộc, không bỏ.
- Entry ở **retrace về FVG**, không chase; stop ngoài sweep.
- Mạnh nhất khi đồng hướng HTF bias, có confluence OTE/OB.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ săn Venom trong cửa sổ thời gian (NY open/kill zone).
- [ ] Tôi chờ giá quét session pool trước khi vào.
- [ ] Tôi vào ở retrace về FVG, không chase.
- [ ] Tôi đặt stop ngoài điểm sweep.
- [ ] Khi thua, tôi ghi `missing_step` để biết lỗi time hay sweep.

### Câu nhắc nhở khi trade
> **"Đúng giờ, tiêm nọc, rồi mới bắn. Ngoài cửa sổ thì không phải Venom."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Nắm time + sweep + displacement chưa? |
| Nhận diện trên chart |  | Xác định đúng cửa sổ + session pool? |
| Biết khi nào bỏ qua |  | Dám bỏ FVG đẹp ngoài cửa sổ? |
| Kết hợp với context HTF |  | Ghép bias + premium/discount + time? |
| Áp dụng vào trade thực tế |  | Entry có thật sự ở retrace FVG không? |
| Review sau trade |  | Có gắn `missing_step` và review dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup tag `[[Venom Model]]`.
- [ ] Review theo `missing_step` (time vs sweep).
- [ ] Thống kê win rate theo `time_window` và `session_pool_swept`.
- [ ] Cập nhật rule khi đủ mẫu.

---

## Appendix — Venom Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Bias:** Bullish / Bearish
> **Reference pools:** Asia ____ / London ____ / PDH-PDL ____
> **Time window:** NY open / NY AM kill zone
> **Location:** Premium / Discount
> **(1) Venom strike (sweep session):** pool ____ @ ____ — reclaim? Yes/No
> **(2) Displacement + MSS:** phá ____ → FVG? Yes/No
> **(3) FVG (POI):** [low]–[high], CE ____ ; OTE/OB? ____
> **(4) Entry:** ____ ; Stop (ngoài sweep): ____
> **(5) Target:** session pool đối diện / PD ____
> **Đúng cửa sổ + đã quét session pool?** Yes / No
> **R:R dự kiến:**
> **No-trade condition:**
