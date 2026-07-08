---
type: ict-concept
concept: Macro Times
aliases:
  - Macro Times
  - ICT Macros
  - Macro Time Windows
  - Cửa sổ Macro
  - Silver Bullet Macro
tags:
  - trading/ict/concept
  - trading/study
  - "#time-and-price"
  - "#macro"
status: developing
category: Time & Price
timeframes:
  - D1
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
  - "[[08 - 08 30 AM NY Model]]"
  - "[[08 - 7 AM Liquidity Hunt + IFVG Entry]]"
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
  - "[[18 - Kill Zones]]"
  - "[[02 - AMD]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[12 - Daily Bias]]"
  - "[[16 - Internal & External Range Liquidity (IRL & ERL)]]"
  - "[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]"
prerequisites:
  - "[[18 - Kill Zones]]"
  - "[[02 - AMD]]"
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
common_mistakes:
  - "[[02 - Mistake - Enter before liquidity sweep]]"
  - "[[03 - Mistake - Entry When MSS not in POI Zone]]"
---

# Macro Times

> [!summary] Tóm tắt 1 câu
> **Macro Times là những cửa sổ thời gian ngắn (~5–20 phút) NẰM BÊN TRONG killzone, nơi thuật toán IPDA thực sự "khai hỏa" chu kỳ repricing — quét thanh khoản và/hoặc tạo displacement (FVG) làm bệ phóng cho chân giao dịch kế tiếp.** Killzone cho biết *khoảng thời gian được phép săn*; macro cho biết *đúng phút thuật toán bóp cò*.

> [!important] Nguyên tắc cốt lõi
> Macro **không phải** là tín hiệu để vào lệnh một cách máy móc theo đồng hồ. Macro chỉ cho biết **thuật toán đang hoạt động**; việc có trade hay không phụ thuộc vào **Daily Bias + PD array hợp lệ trong đúng vùng dealing range + xác nhận MSS**. Câu thần chú: *"Đồng hồ cho biết KHI NÀO nhìn chart; chart cho biết CÓ hay KHÔNG có lệnh."*

---

## 1. Định nghĩa

**Khái niệm:**
**Macro Time** là một khoảng phút cố định trong ngày khi thuật toán giao dịch của tổ chức (IPDA) chạy **chu kỳ repricing**: nó (a) đi tìm thanh khoản — chạy stop, quét một mức equal high/low — để lấy đối ứng khớp lệnh, và/hoặc (b) định giá lại "fair value" bằng một cú [[21 - Market Structure Shift|displacement]] để lại một [[13 - FVG  - Fair Value Gap|Fair Value Gap]]. FVG đó trở thành bệ phóng cho chân giao dịch kế tiếp hướng về [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw on liquidity]] trong ngày.

**Nguồn gốc tư duy:** Xuất phát từ luận điểm của Michael Huddleston rằng thị trường **không** được vận hành bởi cung–cầu ngẫu nhiên mà bởi một **thuật toán giao price theo lịch**. Lịch đó có cấp độ macro rộng (chính là [[18 - Kill Zones|killzone]]) và cấp độ micro chính xác (chính là các macro time) bên trong killzone.

![[MacroTimes-Advanced-FullDayMap.svg|697]]

*Bản đồ 9 macro cổ điển của ICT trong một ngày. Dải rộng = killzone; vạch = macro. Macro 09:50–10:10 (lõi Silver Bullet) là cửa sổ xác suất cao nhất cho NQ/ES; 04:03–04:30 là tương đương cho forex/vàng ở phiên London.*

**Nó giúp trả lời câu hỏi nào trên chart?**
- Trong killzone đang chạy, **đúng phút nào** thuật toán có xác suất tạo sweep/MSS/FVG cao nhất?
- Khi nào **nên ngừng nhìn** chart (khoảng drift giữa các macro)?
- Cú displacement vừa rồi có rơi đúng vào macro window không — hay chỉ là nhiễu giữa hai macro?

### Macro Times KHÔNG phải là gì
- **Không phải killzone.** Đây là nhầm lẫn phổ biến nhất — xem mục 2.
- **Không phải setup được đảm bảo.** Macro chạy ngược bias = *failed macro*, chỉ là thông tin, không phải lệnh.
- **Không thay thế** phân tích killzone/bias — nó **tinh chỉnh** entry bên trong killzone.
- **Không phải** thời điểm bắt buộc phải có lệnh mỗi ngày; có ngày macro "im lặng".

---

## 2. Killzone vs Macro — phân biệt sống còn

![[MacroTimes-Advanced-vs-Killzone.svg|697]]

[[18 - Kill Zones|Killzone]] là **khung phiên rộng** (ví dụ NY AM 08:30–11:00 ET, London 02:00–05:00 ET) — nơi *được phép* giao dịch. **Macro** là những **phút chính xác** bên trong killzone nơi thuật toán khai hỏa. Ví von: killzone là *khoảng thời gian đi săn*, macro là *khoảnh khắc bóp cò*.

> [!warning] Quy tắc bất di bất dịch
> Bạn **không** thể trade macro 10:10 nếu đang ở NGOÀI killzone NY. Một macro rơi ngoài killzone đang hoạt động là **xác suất thấp** và thường không đáng trade. Macro là *sự tinh chỉnh trong killzone*, không phải thứ thay thế killzone.

---

## 3. Lịch Macro đầy đủ (giờ New York / ET)

> [!info] 9 Macro cổ điển của ICT
> **London:** 02:33–03:00 · 04:03–04:30
> **New York AM:** 08:50–09:10 · 09:50–10:10 · 10:50–11:10
> **New York Lunch:** 11:50–12:10
> **New York PM:** 13:10–13:40 · 14:50–15:10 · 15:15–15:45

Một số trader thực chiến dùng biến thể **rút gọn** (điểm mốc thay vì dải): 2:33, 4:03, 8:50, 9:50, 10:10, 11:00, 2:00, 2:10. Ý nghĩa không đổi — đây chỉ là cách ghi nhớ điểm giữa của cửa sổ.

| Macro | Giờ (ET) | Vai trò chính |
|---|---|---|
| London 1 | 02:33–03:00 | Khởi động Judas London (thường mới là *nến tiếp cận*) |
| London 2 | 04:03–04:30 | ★ Cửa sổ London xác suất cao nhất — hoàn tất sweep + MSS |
| NY AM 1 | 08:50–09:10 | Hoàn tất range pre-market, gom BSL/SSL cho open 09:30 |
| NY AM 2 | 09:50–10:10 | ★ Lõi Silver Bullet (NQ/ES) — MSS + FVG entry |
| NY AM 3 | 10:50–11:10 | Kết thúc phân phối buổi sáng, thường chạm T1 (IRL) |
| NY Lunch | 11:50–12:10 | Thanh khoản mỏng, dễ bẫy — giảm size hoặc nghỉ |
| NY PM 1 | 13:10–13:40 | Mở chu kỳ phân phối buổi chiều, quét đỉnh/đáy phiên AM |
| NY PM 2 | 14:50–15:10 | Repricing chiều; **FOMC → macro biến động nhất năm** |
| NY PM 3 | 15:15–15:45 | Macro đóng cửa, hướng về ERL / đóng tuần |

---

## 4. DST — múi giờ đổi hai lần mỗi năm

> [!warning] Bẫy Daylight Saving Time
> Mọi macro time đều tính theo **New York (ET)**. ET = **UTC-4 vào mùa hè** (DST: Chủ nhật thứ 2 của tháng 3 → Chủ nhật đầu tháng 11) và **UTC-5 vào mùa đông**. Nếu bạn ở múi giờ khác, **luôn quy đổi từ ET**, không từ UTC — nếu không sẽ lệch 1 giờ trong các tuần chuyển mùa khi Mỹ đổi lịch nhưng châu Âu/Anh chưa (hoặc ngược lại).

| Macro (ET) | UTC (Hè) | UTC (Đông) | VN (UTC+7) Hè | VN (UTC+7) Đông |
|---|---|---|---|---|
| 02:33 | 06:33 | 07:33 | 13:33 | 14:33 |
| 04:03 | 08:03 | 09:03 | 15:03 | 16:03 |
| 08:50 | 12:50 | 13:50 | 19:50 | 20:50 |
| 09:50 | 13:50 | 14:50 | 20:50 | 21:50 |
| 10:10 | 14:10 | 15:10 | 21:10 | 22:10 |
| 13:10 | 17:10 | 18:10 | 00:10 | 01:10 |
| 14:50 | 18:50 | 19:50 | 01:50 | 02:50 |

> [!tip] Giải pháp gọn nhất
> Đặt **đồng hồ phụ (secondary clock)** trên nền tảng chart về New York time và không bao giờ quy đổi tay nữa. Với trader Việt Nam: macro 10:10 ET ≈ **21:10 (hè) / 22:10 (đông)** — rất tiện vì rơi vào buổi tối.

---

## 5. Vì sao Macro tồn tại — chu kỳ repricing

![[MacroTimes-Advanced-RepricingCycle.svg|697]]

Thuật toán vận hành theo **lịch giao price**: nó có một mục tiêu (draw on liquidity trong ngày) và di chuyển tới đó bằng chuỗi **mở rộng ↔ co lại**. Mỗi chân mở rộng được mở đầu bằng một **khoảnh khắc repricing**: quét thanh khoản gần đó (kích hoạt stop = đối ứng) → tạo displacement để lại FVG → dùng FVG làm bệ phóng cho chân kế.

Macro chính là **khi** các khoảnh khắc repricing này xảy ra. Chúng **dồn quanh thời điểm chuyển giao phiên** (London open, NY open, PM open) vì đó là lúc lệnh tổ chức chuyển tay giữa các desk và khối lượng đơn-thời-điểm lớn nhất — mà **thanh khoản cao nhất chính là lúc thuật toán cần để đẩy giá**.

> [!info] Hệ quả then chốt
> Giá **không** di chuyển đều trong suốt killzone. Trong 90 phút NY AM (08:30–10:00), phần lớn hoạt động định hướng dồn vào các cửa sổ 5–15 phút quanh 08:50, 09:50, 10:10. Khoảng giữa thường là **drift** vận tốc thấp. Chờ đúng macro window để trade sẽ giảm setup giả và tăng chất lượng entry.

---

## 6. Macro trong chu kỳ AMD

![[MacroTimes-Advanced-AMD-Placement.svg|697]]

Mỗi macro thuộc một pha của [[02 - AMD|chu kỳ AMD]] trong ngày. Biết macro thuộc pha nào = biết vai trò của nó và nên **quan sát** hay **vào lệnh**.

**Accumulation (Á):** *KHÔNG* có macro (cố ý). Pha tích lũy (≈20:00–02:00 ET) là lúc thuật toán gom vị thế, không repricing → đây là lý do ICT dạy **không trade phiên Á**.

**Manipulation macro (02:33 · 04:03 · 08:50 · 09:50):** thuộc pha thao túng — Judas Swing và cú giải quyết nó. **Không vào lệnh** ở đây; bạn *quan sát*, đánh dấu FVG chúng tạo ra, và **chờ MSS** báo hiệu thao túng đã xong.

**Distribution macro (10:10 · 10:50 · 13:10 · 14:50):** 10:10 là macro entry phân phối chính — khi thao túng đã xác nhận xong và chân định hướng thật bắt đầu. 10:50–11:10 đóng pha phân phối sáng. PM macro mở/khẳng định phân phối chiều. **Entry được lấy trong macro phân phối**, không phải macro thao túng.

---

## 7. Cách trade Macro — quy trình 4 bước

![[MacroTimes-Advanced-Entry-Sequence.svg|697]]

*Chuỗi mẫu bearish trên NQ: 08:50 kéo dài đỉnh pre-market (gom BSL) → 09:30 open Judas quét BSL → 09:50 macro MSS + FVG hình thành → 10:00–10:10 giá hồi về FVG → 10:10 limit sell khớp tại 50% CE → phân phối về T1 (IRL) quanh 11:00.*

**Bước 1 — Xác nhận [[12 - Daily Bias|Daily Bias]] TRƯỚC mọi macro.** Bias quyết định macro phải khai hỏa hướng nào mới tradeable. Ngày bearish: macro 10:10 đẩy lên trên một đỉnh rồi đảo xuống = hợp lệ. Nếu đẩy xuống rồi đảo lên → *failed macro* hoặc chỉ là dao động vặt. **Không bao giờ trade macro ngược bias.**

**Bước 2 — Đánh dấu PD array/FVG TRƯỚC khi macro khai hỏa.** Với macro 10:10, vùng entry thường là FVG/OB tạo ra trong MSS 09:50 (hoặc mức chưa mitigate từ phiên trước). Với macro 04:03, đánh dấu FVG từ MSS 02:33 (nếu có). **Phải có mức entry ghi sẵn trước khi cửa sổ mở.**

**Bước 3 — Quan sát chủ động ±5 phút và đặt limit tại 50% CE.** Từ 10:05–10:20, theo dõi từng nến M1. Giá có hồi vào FVG đã đánh dấu? Có chạm mức [[10 - Consequent Encroachment (Mean Threshold)|50% Consequent Encroachment]] không? Đặt **limit** tại 50% CE của FVG **trước** khi cửa sổ mở. Khớp trong cửa sổ macro = lệnh hợp lệ. Nếu tới 10:20 giá chưa chạm → cơ hội đã trôi.

**Bước 4 — Stop & target theo cấu trúc macro.** Stop **vượt qua wick của nến Judas macro** (không phải con số cố định). T1 = [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL]] theo hướng phân phối (thường chạm ở macro kế, ví dụ 10:50–11:10 cho entry 10:10). T2 = ERL = draw on liquidity trong ngày.

---

## 8. Ví dụ chart

### Ví dụ đúng
![[MacroTimes-Example-Correct.svg|697]]

**Mô tả:** Bias bearish (HTF premium). 09:30 quét BSL (Judas) → 09:50 MSS xuống để lại FVG → giá hồi về **50% CE** của FVG đúng cửa sổ 10:10 → limit sell khớp → phân phối về T1 (IRL).

**Vì sao đây là ví dụ tốt:**
- Macro khai hỏa **thuận** Daily Bias.
- Entry tại retrace (50% CE), **không** đuổi nến macro.
- Đủ chuỗi xác nhận: sweep → MSS → FVG hợp lệ → trong macro window.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lệnh NQ/NAS100 thật: đánh dấu (1) đỉnh/đáy bị quét, (2) nến MSS 09:50 và FVG, (3) điểm limit 50% CE khớp trong 10:05–10:20, (4) T1/T2. Ghi rõ giờ ET của từng mốc.*

### Ví dụ sai / dễ nhầm
![[MacroTimes-Example-Wrong.svg|697]]

**Mô tả lỗi:** (A) Trade **ngược** Daily Bias — long ở macro bullish trong ngày bias bearish (đánh nhầm micro-Judas / ngược dòng tuần). (B) **Market order ngay trên nến macro** thay vì chờ hồi về 50% CE → stop rộng, RR xấu. (C) **Ép lệnh** khi macro không thực sự khai hỏa.

**Bài học:**
- Bias filter là **bắt buộc** ở macro y như mọi lúc khác.
- Nến macro **tạo ra** vùng entry, nó **không phải** entry.
- Không có displacement ở macro = không có setup; đóng chart.

---

## 9. Macro trên NQ vs Forex vs Vàng

| Thị trường | Macro chủ đạo | Đặc điểm |
|---|---|---|
| **NQ / ES** | 08:50 · 09:50 · **10:10** | Pre-market 07:00–09:30 tạo range tích lũy; open cứng 09:30 tạo Judas đáng tin; 10:10 là cửa sổ 1-phút xác suất cao nhất trong khung ICT. Beta NQ cao → Judas kéo dài 20–50 điểm. |
| **Forex (EU/GU)** | **02:33 · 04:03** | Không có "open cứng" như chứng khoán → macro London quan trọng hơn NY. 04:03 trên EURUSD tương đương 10:10 trên NQ. |
| **Vàng (XAUUSD)** | 02:33 · 04:03 & 14:50 | Phản ứng cả hai bộ macro; 04:03 cho move London lớn nhất (Judas 200–400 pip); macro 14:50 cực mạnh quanh CPI/NFP/FOMC. |

---

## 10. Failed macro & ngày không có macro

**Macro chạy ngược bias (ví dụ 10:10 bullish trong ngày bearish):** có 2 khả năng — (1) *bias sai*, cần xem lại; hoặc (2) đây là **micro-Judas** (thao túng trong pha phân phối) tạo điểm short **cao hơn, đẹp hơn** trước khi đảo. Phân biệt: nếu nó **quét một mức BSL có ý nghĩa** rồi đảo kèm MSS → micro-Judas, short ở retrace từ mức cao hơn. Nếu chỉ drift lên không lấy mức nào → xem lại bias.

**Không có macro nào khai hỏa:** ngày lễ, thứ Sáu mùa hè, tin cực mạnh, hoặc bias tuần quá mạnh (không cần sweep trước khi phân phối). **Ép một setup macro khi nó không tồn tại là lỗi phổ biến nhất.** Nếu 10:10 trôi qua không có price action ý nghĩa → đóng chart, chờ ngày mai.

---

## 11. Thực hành tốt nhất (Best Practices)

> [!tip] 5 quy tắc Macro
> 1. **Mọi giờ đều là ET** — chỉnh DST hai lần/năm (đặt đồng hồ phụ về New York).
> 2. **Macro ≠ killzone** — macro là các phút bên trong killzone khi thuật toán khai hỏa.
> 3. **Đánh dấu FVG từ macro thao túng TRƯỚC khi macro phân phối mở.**
> 4. **Vào tại 50% CE của FVG trên nhịp hồi** trong macro phân phối — không market order trên nến macro.
> 5. **Không bao giờ trade macro ngược Daily Bias** — macro ngược hướng là *failed macro*, không phải setup.

- Vẽ **đường dọc** đánh dấu macro trên chart; chỉ tập trung ±5 phút quanh mỗi macro → giảm ~60% thời gian nhìn màn hình và loại phần lớn entry giả.
- Ưu tiên macro **có confluence tối đa**: đúng bias + đúng vùng premium/discount + có **SMT divergence** (NQ tạo cực trị mới, ES không) + FVG sạch.
- Ghép macro với các model có sẵn: [[08 - 08 30 AM NY Model]], [[08 - 7 AM Liquidity Hunt + IFVG Entry]], và bộ khung [[01 - ICT 2022 Model]].
- Chốt lệnh **theo cấu trúc**: T1 tại IRL (thường chạm ở macro kế), T2 tại ERL — dời stop về BE sau T1.
- Ghi nhật ký theo macro: mỗi lệnh backtest/live nên gắn nhãn *đã khớp ở macro nào* để đo edge của từng cửa sổ theo thời gian.

---

## 12. Checklist trước khi trade một Macro

> [!warning] Không trade chỉ vì "đến giờ macro"
> Đồng hồ cho biết KHI NÀO nhìn chart; chart cho biết CÓ hay KHÔNG có lệnh.

- [ ] Daily Bias rõ ràng (D1/H4)
- [ ] Đang trong **killzone** phù hợp, không chỉ đúng phút macro
- [ ] Giá ở Premium/Discount đúng hướng trade
- [ ] Đã đánh dấu FVG/PD array từ macro thao túng **trước** khi cửa sổ mở
- [ ] Đã có **MSS** xác nhận thao túng kết thúc
- [ ] Có displacement thật tạo FVG (không phải nến yếu/chồng lấn)
- [ ] Đặt **limit tại 50% CE**, không market order trên nến macro
- [ ] Stop vượt wick Judas macro; T1 = IRL, T2 = ERL
- [ ] (Ưu tiên) có SMT divergence xác nhận
- [ ] Không ép lệnh nếu macro không khai hỏa

---

## 13. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Nhầm macro với killzone | Chuyển hẳn sang "chỉ nhìn macro", bỏ phân tích killzone | Macro là tinh chỉnh *bên trong* killzone, không thay thế |
| Vào ngay nến macro | Market order lúc nến displacement đóng | Chờ hồi về FVG 50% CE, đặt limit |
| Trade ngược bias | MSS đẹp nhưng ngược hướng ngày | Bias filter bắt buộc; macro ngược = failed macro |
| Ép lệnh mỗi khung giờ | "Đến 10:10 nên phải có lệnh" | Không displacement = không setup; đóng chart |
| Sai giờ do DST | Lệch 1 giờ vào tuần chuyển mùa | Đặt đồng hồ phụ về New York; quy đổi từ ET |
| Stop quá chặt | Đặt stop tại swing MSS | Stop vượt toàn bộ wick Judas macro |

---

## 14. Câu hỏi tự kiểm tra

- Tôi giải thích được khác biệt killzone vs macro trong 30 giây không?
- Macro nào là xác suất cao nhất cho NQ? Cho forex/vàng?
- Macro này thuộc pha AMD nào — thao túng hay phân phối?
- Điều gì biến một macro thành *failed macro*?
- Lệnh nào trong journal của tôi khớp đúng macro window, lệnh nào không — edge khác nhau ra sao?

---

## 15. Flashcards / Active Recall

### Q1
**Hỏi:** Macro Time là gì trong 1 câu?
**Đáp:** Cửa sổ ~5–20 phút bên trong killzone khi thuật toán chạy chu kỳ repricing (sweep + tạo FVG) cho chân giao dịch kế tiếp.

### Q2
**Hỏi:** Macro nào là lõi Silver Bullet cho NQ/ES và vào lệnh thế nào?
**Đáp:** 10:10 ET; đánh dấu FVG từ MSS 09:50, đặt limit tại 50% CE, khớp trong 10:05–10:20.

### Q3
**Hỏi:** Xử lý ra sao khi macro khai hỏa ngược Daily Bias?
**Đáp:** Coi là failed macro — hoặc bias sai (xem lại), hoặc là micro-Judas tạo entry đẹp hơn nếu nó quét mức BSL/SSL ý nghĩa rồi đảo kèm MSS.

---

## 16. Liên kết với Trade Journal

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
> Nếu vault dùng path riêng cho trades, thay `FROM ""` bằng ví dụ `FROM "05 - Live Trading Journal/Trades"`.

---

## 17. Nguồn tham khảo
- ICT 2024 Mentorship — khái niệm time-based (Lecture 1 & 2).
- ICT Macro Times — schedule & DST (giờ ET).
- Silver Bullet / IPDA — chu kỳ repricing của thuật toán.

---

## 18. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa | | |
| Phân biệt killzone vs macro | | |
| Nhớ lịch macro + DST | | |
| Vào lệnh đúng 50% CE trong macro | | |
| Áp dụng vào trade thực tế | | |

**Kế hoạch review tiếp theo:**
