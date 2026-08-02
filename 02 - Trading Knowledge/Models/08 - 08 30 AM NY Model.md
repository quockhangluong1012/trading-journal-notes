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
last_reviewed: 2026-07-05
created: 2026-07-04
updated: 2026-07-28
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

## Phản biện & Giới hạn của mô hình

![[NY0830-Advanced-Critique-NewsVsModel.svg|720]]

> [!info] Mô tả hình
> Hai narrative song song cho cùng một cú di chuyển sau 08:30: (trái) "smart money raid thanh khoản rồi đảo chiều theo IPDA" — narrative ICT; (phải) "volatility clustering quanh tin kinh tế tạo overshoot rồi mean-revert" — narrative auction market/thống kê. Cùng một chart giá, hai lời giải thích không thể phân biệt bằng mắt thường.

> [!important] Vấn đề epistemic — vì sao khó kiểm chứng "IPDA raid thanh khoản 08:30"
> Mô hình 08:30 gắn chặt với ý tưởng "thuật toán/tổ chức cố tình raid relative equal đúng khung giờ tin ra". Đây là diễn giải **không thể kiểm chứng trực tiếp** — không ai truy được lệnh của "smart money". Bốn lời giải thích thay thế cùng khớp với dữ liệu quan sát được:
> - **Auction Market Theory:** 08:30 chỉ là điểm tái định giá khi thông tin mới (CPI/NFP) được đưa vào; giá "tìm kiếm" vùng cân bằng mới — không cần khái niệm "thanh khoản bị săn".
> - **Mean-reversion quanh tin:** dữ liệu thống kê thị trường tài chính cho thấy giá thường overshoot khi tin ra rồi điều chỉnh lại một phần — hiện tượng phổ biến ở nhiều tài sản, không riêng gì khung 08:30 hay riêng ICT.
> - **Volatility clustering:** biến động cao có xu hướng đi theo cụm (hiện tượng thống kê đã biết trong tài chính định lượng từ lâu, không cần lý thuyết IPDA); 08:30 chỉ là một trong các mốc lịch tin cố định gây volatility clustering.
> - **Self-fulfilling vì đông người trade cùng ý tưởng:** khi đủ đông trader ICT cùng chờ "raid relative equal rồi MSS" tại 08:30, hành vi đặt lệnh tập thể có thể tự tạo ra một phần cấu trúc đó — không chứng minh được "tổ chức lớn cố ý", chỉ chứng minh được "đám đông phản ứng giống nhau".
>
> Không có narrative nào trong bốn cái trên phủ nhận việc mô hình có thể vẫn "work" — nhưng nó nghĩa là đừng lấy "tổ chức đang điều phối" làm lý do tin tưởng mù quáng.

> [!warning] Rủi ro thống kê khi backtest mô hình 08:30
> - **Hindsight bias:** nhìn lại chart đã đóng nến, relative equal nào cũng "thấy rõ", MSS nào cũng "thấy rõ". Lúc live, cùng một chart đang chạy có thể mơ hồ hơn nhiều.
> - **Degrees of freedom quá nhiều:** chọn cụm relative equal nào ("gần bằng" là bao nhiêu tick?), chọn swing nào làm mốc MSS, chọn PD array nào coi là "đầu tiên" — mỗi lựa chọn đều có thể điều chỉnh ngược để chart khớp kết luận mong muốn → dễ overfit vào dữ liệu đã biết.
> - **Sample size:** một chuỗi thắng 5-10 lệnh không đủ để kết luận winrate thật; cần tối thiểu ~100 mẫu/thị trường/regime (có tin vs không tin) để số liệu có ý nghĩa thống kê.
> - **Survivorship của case chia sẻ:** các ví dụ "08:30 đẹp" lan truyền trên mạng xã hội/khóa học luôn là case đã thắng, đã đẹp — không ai đăng 20 lần range chết hoặc raid không kèm MSS. Nhìn vào các case này một cách ngây thơ sẽ đánh giá quá cao winrate thật.

> [!warning] Điều kiện thị trường làm mô hình 08:30 gãy
> - **Ngày không có tin lớn kèm thanh khoản mỏng** (giữa tuần lễ hè, ngày lễ Mỹ rút gọn): relative equal hình thành nhưng không có đủ dòng lệnh để raid dứt khoát → nhiều false MSS, range chết kéo dài qua cả 08:30-09:30.
> - **Regime trend cực mạnh một chiều (trending day):** giá không quay lại raid relative equal kiểu "hai chiều" mà chạy thẳng — model chờ raid + MSS ngược hướng sẽ đứng ngoài cả ngày trong khi thị trường đang cho một trend liền mạch.
> - **Ngày risk-off toàn cầu / gap sự kiện vĩ mô lớn (khủng hoảng, thay đổi chính sách đột ngột):** biến động không còn tuân theo nhịp "build-up 08:00-08:30 → raid → MSS" thông thường, mà là một chiều dội liên tục — cấu trúc PD array bị phá vỡ nhanh hơn tốc độ xác nhận.

> [!tip] Cách tự kiểm định khách quan
> 1. **Pre-registration:** viết quy tắc cứng (định nghĩa "relative equal" bằng số tick cụ thể, định nghĩa MSS bằng đóng nến hay chỉ cần chạm) TRƯỚC khi backtest, không sửa quy tắc giữa chừng khi thấy kết quả xấu.
> 2. **Forward test** 15-20 lệnh sau backtest, trước khi tin vào con số.
> 3. **Đếm cả setup bị bỏ lỡ** (đủ điều kiện nhưng không vào) để không chỉ nhìn vào các lệnh đã chọn — tránh confirmation bias khi chỉ backtest "case mình thích".
> 4. **Walk-forward:** chia dữ liệu theo thời gian, test trên đoạn sau bằng quy tắc rút ra từ đoạn trước, không test và tối ưu trên cùng một đoạn.
> 5. **Tối thiểu 100+ mẫu/regime** (ngày có tin vs không tin, thị trường trend vs range) trước khi kết luận model "work" hay "không work" trong regime đó.

> [!important] Phản biện đặc thù mô hình 08:30
> - **"08:30 đặc biệt vì trùng tin kinh tế Mỹ"** — đúng về mặt lịch tin, nhưng phần lớn ngày giao dịch trong năm KHÔNG có CPI/NFP/PPI đúng ngày đó; những ngày này 08:30 chỉ còn lại "hiệu ứng mở màn NY AM" chung chung, một hiệu ứng cũng tồn tại mà không cần gắn riêng cho phút 08:30. Cần backtest tách bạch: winrate ngày-có-tin có thực sự khác ngày-không-tin, hay chỉ là noise thống kê với sample nhỏ?
> - **"Relative equal H/L là nơi thanh khoản tổ chức đặt lệnh"** — không thể xác minh trực tiếp đây là lệnh tổ chức hay đơn giản là điểm swing failure ngẫu nhiên mà bất kỳ trader retail nào cũng đặt stop quanh đó (self-fulfilling).
> - **Ranh giới giữa "raid do tin" và "raid ngẫu nhiên do range hẹp"** rất mờ trên các cặp ít thanh khoản hoặc ngày volatility thấp — dễ gán nhãn "đây là raid 08:30 chuẩn" cho một cú nhiễu giá bình thường.
> - **Model dựa nhiều vào "cảm giác" đọc relative equal** (bao nhiêu pip/tick được coi là "gần bằng") — nếu không định nghĩa cứng bằng số, hai trader nhìn cùng một chart có thể ra hai kết luận khác nhau, làm giảm khả năng tái lập của model.

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

## Chuyên sâu A — Edge cases & Failure modes (thực chiến 08:30 NY)

![[NY0830-Advanced-EdgeCase-Matrix.svg|720]]

Model 08:30 chỉ có vài mắt xích — bias 15m, raid, MSS, PD array — nhưng phần lớn lệnh thua **không** đến từ việc *không biết* trình tự, mà từ những ca biên (edge case) khiến ta ép một mắt xích chưa chín. Sáu ca dưới đây lặp lại nhiều nhất khi trade/backtest phiên 08:30; mỗi ca theo cấu trúc **dấu hiệu → cơ chế → xử lý**.

**① Pre-position trước 08:30 (front-run)**
- *Dấu hiệu:* đặt lệnh trước 08:30 khi chưa có một cú raid nào.
- *Cơ chế:* ta đang **đoán** hướng thay vì phản ứng với thanh khoản đã bị quét — chưa có xác nhận time-based nào.
- *Xử lý:* cấm mọi entry trước 08:30; luôn chờ raid thật xảy ra rồi mới đọc cấu trúc.

**② Vào ngay khi vừa raid, CHƯA có MSS**
- *Dấu hiệu:* thấy giá quét relative equal highs/lows là nhảy vào ngay.
- *Cơ chế:* raid mới chỉ là "mồi"; nó **chưa cam kết** hướng — giá hoàn toàn có thể tiếp tục theo chiều raid.
- *Xử lý:* chờ MSS + displacement xác nhận đảo chiều rồi mới tính entry.

**③ MSS 1m NGƯỢC DOL 15m/H1 (bẫy nested)**
- *Dấu hiệu:* 1m cho một cú MSS rất đẹp nhưng ngược hướng DOL 15m/H1.
- *Cơ chế:* cú MSS 1m đó thường chỉ là một nhịp hồi (raid) **bên trong** dòng chảy lớn hơn — không phải đảo chiều thật.
- *Xử lý:* bỏ; chỉ trade khi MSS 1m **đồng hướng** DOL 15m.

**④ Đợi hồi quá sâu → lỡ PD array đầu tiên / entry xấu**
- *Dấu hiệu:* bỏ qua PD array đầu tiên sau MSS, chờ giá về sâu hơn cho "giá đẹp".
- *Cơ chế:* sau displacement, giá thường đi luôn từ PD array đầu tiên; đợi sâu hơn = lỡ chuyến hoặc phải vào entry xấu, trễ.
- *Xử lý:* vào **PD array đầu tiên** sau MSS (ưu tiên Unicorn > FVG > OB > breaker).

**⑤ Whipsaw ngay giây phát hành tin CPI/NFP**
- *Dấu hiệu:* đúng giây ra tin, nến quét **cả hai chiều** trước khi đi hướng thật.
- *Cơ chế:* thanh khoản hai đầu bị spike quét sạch stop chỉ trong vài giây.
- *Xử lý:* chờ nến tin **đầu** đóng xong rồi mới đọc raid/MSS; không giữ stop sát trong lúc tin ra.

**⑥ Stop tại swing MSS (quá chặt)**
- *Dấu hiệu:* đặt stop ngay sát swing của cú MSS.
- *Cơ chế:* biến động post-08:30 rất rộng; wick dễ quét cái swing đó dù hướng cuối cùng đúng.
- *Xử lý:* đặt stop **ngoài toàn bộ range post-08:30**, không chỉ tại swing MSS.

### Sáu ca mở rộng (thực chiến/backtest nâng cao)

**⑦ Ngày CPI/NFP spike hai chiều rồi mới chọn hướng thật (double-sided spike)**
- *Dấu hiệu:* đúng 08:30:00-08:30:15, nến 1m/5s quét mạnh một chiều rồi đảo ngược quét chiều kia trước khi mới bắt đầu đi hướng thật.
- *Cơ chế:* thanh khoản ở cả hai phía bị dọn sạch gần như đồng thời do lệnh thị trường ồ ạt phản ứng với con số tin — không phải "raid rồi MSS" theo trình tự sạch như lý thuyết, mà là hai cú raid gần như chồng lên nhau.
- *Xử lý:* không đọc MSS trên khung giây/1m ngay trong 30-60 giây đầu sau tin; chờ ít nhất 1-2 nến 1m đóng ổn định rồi mới xác định đâu là raid thật, đâu là MSS thật.
- *Bài học:* "raid" đầu tiên nhìn thấy trong 15 giây đầu sau tin thường không phải là raid có ý nghĩa cấu trúc — chỉ là nhiễu thanh khoản hai chiều.

**⑧ 08:30 không có tin lớn → range chết (dead range)**
- *Dấu hiệu:* không có CPI/NFP/PPI/Jobless Claims ngày đó; sau 08:30 giá đi ngang biên độ rất hẹp, không có build-up relative equal rõ ràng.
- *Cơ chế:* thiếu catalyst tin tức, dòng lệnh tổ chức tham gia ít hơn hẳn — thị trường chỉ "lăn tăn" quanh giá mở, chưa đủ năng lượng tạo raid + MSS sạch.
- *Xử lý:* không ép setup; coi đây là ngày no-trade mặc định trừ khi có raid + MSS rõ ràng xuất hiện muộn hơn (macro 09:50/10:00).
- *Bài học:* không phải ngày nào cũng có setup A — lịch tin trống là tín hiệu hạ kỳ vọng ngay từ đầu phiên, không phải lý do cố tìm setup.

**⑨ Double distribution: sweep 08:30 xong, 09:30 sweep ngược lại**

![[NY0830-Advanced-DoubleDistribution.svg|720]]

> [!info] Mô tả hình
> Timeline hai pha trong buổi sáng: pha 1 tại 08:30 raid + MSS lên, giá chạy có lãi tới T1; pha 2 tại 09:30 (mở NYSE) giá tạo đỉnh phụ rồi sweep ngược lại tạo MSS đối nghịch — minh họa việc thị trường có thể "phân phối" hai lần độc lập trong cùng buổi sáng.

- *Dấu hiệu:* raid + MSS tại 08:30 cho một hướng, trade chạy có lãi; nhưng đến 09:30 (mở cửa NYSE) giá lại sweep ngược hướng, tạo MSS đối nghịch.
- *Cơ chế:* 09:30 bơm một lượng thanh khoản cổ phiếu độc lập với logic 08:30 — thị trường có thể "phân phối lại" theo hai giai đoạn khác nhau trong buổi sáng (hai lần phân phối/distribution), đặc biệt trên NQ/ES.
- *Xử lý:* nếu đã chốt một phần tại T1 theo kế hoạch trước 09:30, phần còn lại nên có quy tắc: dời BE sau T1, không giữ full size xuyên qua 09:30 nếu chưa đạt T2 rõ ràng; coi 09:30 như một mốc đánh giá lại, không mặc định "còn chạy tiếp".
- *Bài học:* trade 08:30 không tự động "an toàn" xuyên suốt tới 09:30 — cửa sổ mở NYSE có thể là một chu kỳ raid/MSS độc lập, không phải phần nối tiếp của chu kỳ 08:30.

**⑩ Spread/slippage giãn đúng tại giây 08:30:00**
- *Dấu hiệu:* lệnh limit hoặc market đặt sát 08:30:00 khớp giá xấu hơn đáng kể so với giá hiển thị trên chart, đặc biệt trên CFD/spread-bet hoặc broker retail.
- *Cơ chế:* broker/thanh khoản liên ngân hàng thường nới spread trong vài giây quanh mốc phát hành tin lớn để tự bảo vệ — đây là chi phí giao dịch thật, không phải "trượt giá xui rủi".
- *Xử lý:* tránh đặt lệnh market đúng khung 08:30:00-08:30:10 nếu có tin lớn; nếu vào bằng limit tại PD array, chấp nhận khả năng không khớp hoặc khớp trượt vài tick, và tính spread rộng hơn vào R:R dự kiến cho riêng phút đầu tiên.
- *Bài học:* số liệu backtest lấy giá đóng nến lý tưởng luôn đẹp hơn giá khớp lệnh live tại đúng giây tin ra — đừng kỳ vọng backtest và live giống hệt nhau ở khung 08:30:00.

**⑪ Ngày half-day / holiday rút ngắn phiên Mỹ**
- *Dấu hiệu:* các ngày trước/sau lễ Mỹ (ví dụ áp Lễ Tạ ơn, áp Giáng sinh) NYSE đóng cửa sớm; thanh khoản buổi sáng đã mỏng sẵn dù vẫn có 08:30.
- *Cơ chế:* dòng lệnh tổ chức tham gia ít hơn ngày thường vì nhiều bàn giao dịch nghỉ sớm hoặc giảm size — build-up 08:00-08:30 có thể hình thành nhưng raid sau đó thiếu lực đi tiếp, dễ tạo MSS giả rồi quay đầu.
- *Xử lý:* tra lịch half-day trước phiên; nếu trùng, giảm size mặc định hoặc đứng ngoài, không áp dụng kỳ vọng biến động như ngày thường.
- *Bài học:* "có 08:30" không đồng nghĩa "có đủ thanh khoản tổ chức" — lịch giao dịch rút ngắn làm gãy toàn bộ giả định về dòng lệnh của model.

**⑫ DST (giờ mùa) làm lệch khoảng cách 08:30 NY với London/killzone khác**
- *Dấu hiệu:* trong giai đoạn Mỹ và châu Âu đổi giờ mùa (DST) lệch nhau vài tuần (khoảng cuối tháng 3 và cuối tháng 10 hằng năm), khoảng cách giờ giữa 08:30 NY và London open/killzone bị xê dịch 1 tiếng so với bình thường.
- *Cơ chế:* nếu trader dùng đồng hồ broker hoặc lịch tin không tự cập nhật DST, macro time 08:50/09:50 và cả mốc 08:30 tự nó có thể bị lệch 1 tiếng trên chart — dẫn tới quan sát sai giai đoạn build-up hoặc raid.
- *Xử lý:* luôn chốt lại giờ theo NY time (ET) thực tế qua nguồn tin cậy vào các tuần chuyển giao DST; đối chiếu giờ tin kinh tế (thường theo ET) với giờ hiển thị trên nền tảng trước khi trade.
- *Bài học:* hai tuần chuyển giao DST mỗi năm là giai đoạn dễ đọc sai khung giờ nhất — kiểm tra timezone của chart là bước pre-session bắt buộc, không phải mặc định.

> [!note] Nguyên tắc xuyên suốt
> Khi nghi ngờ bất kỳ mắt xích nào (raid / MSS / context 15m / PD array / stop / news), hãy **hạ cấp về "chờ xác nhận"** thay vì ép entry. Thiếu một mắt xích cốt lõi = **No-Trade**. Một lệnh bỏ lỡ luôn rẻ hơn một lệnh sai quy trình.

---

## Chuyên sâu B — Kinh nghiệm live/backtest thực chiến

![[NY0830-Advanced-Experience.svg|720]]

Những bài học dưới đây chắt ra từ live + backtest phiên 08:30, kèm cách biến chúng thành số liệu review được.

1. **Bias đến từ 15m/H1; 1m chỉ là trigger.** Viết bias + DOL (BSL trên / SSL dưới) *trước* phiên; 1m chỉ dùng để canh giờ vào. Mọi entry phải **đồng hướng DOL 15m**.
2. **Chờ raid + MSS — không vào chỉ vì "vừa raid".** Raid là mồi; MSS + displacement mới xác nhận hướng thật.
3. **Vào PD array đầu tiên sau MSS** (ưu tiên **Unicorn > FVG > OB > breaker**) — chi tiết về Unicorn xem [[07 - Unicorn Model]].
4. **Khác biệt theo market:** NQ1/ES sạch nhất — 09:30 mở NYSE khuếch đại displacement; EURUSD/GBPUSD hay cho nhịp hồi vào range; XAUUSD wick dài → nới stop, **giảm size**.
5. **Ngày CÓ tin cho displacement sạch nhưng whipsaw cao** — chờ **nến tin đầu đóng** rồi mới đọc MSS.
6. **Compound trong ngày trend:** một ngày trend mạnh cho **nhiều** setup 08:30-style tại các macro kế tiếp (09:50, 10:00) **cùng hướng DOL** — mỗi lần tạo relative equal mới → raid → MSS là một cơ hội re-entry. Cùng gia đình logic với [[08 - 7 AM Liquidity Hunt + IFVG Entry]].
7. **Kỷ luật `missing_step`:** với mỗi lệnh thua/BE, ghi `missing_step` (`raid` / `mss` / `context15m` / `pdarray` / `stop` / `news`) và **thống kê hằng tuần** ([[07 - Reviews]]). Cần **≥30 mẫu**, backtest riêng ngày-có-tin vs ngày-không-tin. Nền tảng đọc đa khung: [[32 - Top-down Analysis (Multiple Timeframes)]]; định nghĩa MSS: [[21 - Market Structure Shift]].
8. **Spread/slippage thật tại đúng giờ mô hình khác giá backtest.** Backtest thường lấy giá đóng nến lý tưởng; live tại 08:30:00-08:30:10 spread thực tế trên nhiều broker retail/CFD giãn rõ (đặc biệt vàng, chỉ số CFD) so với khung giờ bình thường. Nên **ghi riêng** slippage trung bình tại phút đầu tiên sau tin và cộng vào chi phí kỳ vọng thay vì so backtest với live như hai tập dự liệu tương đương.
9. **Demo / live / tài khoản funded không phải cùng một trải nghiệm.** Demo thường khớp lý tưởng, không requote; live tài khoản cá nhân có slippage thật nhưng tâm lý ít bị bóp bởi luật drawdown ngày; **tài khoản funded/prop** thêm một lớp biến dạng hành vi — luật max daily drawdown khiến trader dễ **thoát sớm trước TP** hoặc **bỏ setup A+ muộn phiên** vì đã gần chạm ngưỡng lỗ ngày — hai hành vi này không xuất hiện khi backtest trên dự liệu lịch sử thuần. Khi so sánh kỳ vọng backtest với kết quả tài khoản funded, phải tách biệt rõ đâu là lỗi đọc model, đâu là hậu quả của luật quản lý rủi ro bị áp thêm.
10. **Tâm lý sau 2-3 lệnh thua liên tiếp** là giai đoạn dễ vỡ quy tắc nhất: xu hướng tăng size để "gỡ lại" hoặc siết stop quá chặt vì sợ thua tiếp — cả hai đều phá vỡ đúng thứ quy tắc đã giúp chuỗi đúng ở điểm 1-6. Nên có quy tắc cứng: sau 3 lệnh thua liên tiếp trong cùng tuần, **giảm size 50%** cho đến khi có ≥1 lệnh thắng đúng quy trình.
11. **Chuỗi thua liên tiếp là toán học, không phải điềm xấu.** Với một hệ thống có win-rate thật sự 45-55% (mức phổ biến của setup 08:30 sau khi lọc đủ điều kiện), xác suất gặp **một chuỗi ≥4 lệnh thua liên tiếp** trong mỗi 30 lệnh là điều bình thường về mặt phân phối nhị thức (binomial), không phải dấu hiệu "model hỏng". Trước khi kết luận model không còn edge, hãy đặt câu hỏi: chuỗi thua này có nằm trong biên dị thường thống kê của win-rate hiện tại không, hay tất cả đều có cùng `missing_step`?
12. **Tần suất setup A+ thật thập hơn kỳ vọng ban đầu.** Sau khi lọc đủ raid + MSS + displacement + đồng hướng DOL 15m + không rơi vào edge case ở trên, số ngày có setup A+ thật sự tại đúng khung 08:30 thường chỉ rơi vào khoảng **2-3 ngày/tuần** (ưu thế rõ hơn vào ngày có CPI/NFP/FOMC/PCE) — kỳ vọng "ngày nào cũng có A+" là nguyên nhân phổ biến nhất khiến trader hạ chuẩn vào lệnh B/C.
13. **Chỉ tăng size khi đạt đủ 3 điều kiện:** (a) ≥ 30 mẫu liên tục với `missing_step: none` chiếm tỷ lệ ổn định qua ≥ 4 tuần review; (b) đã tách biệt kết quả theo ngày-có-tin/không-tin và không phụ thuộc hoàn toàn vào một vài outlier R lớn; (c) đang **không** trong chuỗi thua gần nhất (mục 10). Thiếu một trong ba điều kiện → giữ nguyên size, không "thử tăng để xem".

> [!tip]
> 15m quyết định **có nên** trade, 1m quyết định **khi nào** vào — đảo thứ tự này là gốc của phần lớn lệnh thua 08:30.

> [!warning] Toán học chuỗi thua (tham khảo nhanh)
> Với win-rate 50% và số lệnh đủ lớn, xác suất xuất hiện ≥ 1 chuỗi **5 lệnh thua liên tiếp** trong 50 lệnh là hiện tượng phổ biến, không phải hiếm. Đừng dùng một chuỗi thua để kết luận về edge nếu chưa đủ ≥100 mẫu/regime thị trường để so sánh (xem thêm phần Phản biện & Giới hạn mô hình).

---

## Chuyên sâu C — Case studies mổ xẻ chuyên sâu (kịch bản minh họa)

> [!info] Đọc thế nào
> Bảy ca dưới đây là **kịch bản minh họa (hypothetical)** — dùng để luyện *nhận diện chuỗi*, không phải tín hiệu giao dịch. Chấm điểm bằng **chất lượng process**, không bằng P&L: một lệnh thua đúng quy trình vẫn hơn một lệnh thắng sai quy trình. **Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa** — không phải giao dịch thật của một ngày cụ thể; các sự kiện tin tức được nêu (CPI, NFP...) chỉ mô tả đặc điểm chung, không gắn với ngày/giá trị xác thực nào.

### Case 1 — NQ1 Win (đúng chuẩn)

![[NY0830-Advanced-CaseStudy-Win.svg|720]]

**Chuỗi:** bias 15m bearish (DOL = SSL dưới); build-up 08:00–08:30 dựng relative equal highs; sau 08:30 raid BSL; MSS xuống + displacement để lại SIBI; vào PD array đầu tiên (SIBI) tại retest; stop ngoài đỉnh post-08:30; TP tại DOL kế (SSL / đáy phiên trước).
**Chẩn đoán:** đủ raid + MSS + PD array và **đồng hướng DOL 15m** → `missing_step: none`. Đây là chuỗi chuẩn của [[21 - Market Structure Shift]] trong phiên 08:30.
**Bài học:** hình mẫu A+; khi chuỗi đúng thì kể cả một lần thua vẫn là "good loss".

### Case 2 — Loss (front-run / vào khi chưa MSS)

![[NY0830-Advanced-CaseStudy-Loss.svg|720]]

**Chuỗi (gãy):** thấy giá raid relative equal highs là vào SELL ngay, **chưa** chờ MSS; giá tiếp tục lên phá đỉnh (raid chưa "cam kết" hướng) và quét stop.
**Chẩn đoán:** `missing_step: mss` — bỏ hẳn bước xác nhận đảo chiều, không có displacement, không có PD array, không có edge.
**Bài học:** raid chỉ là mồi; MSS + displacement mới cho biết hướng thật.

### Case 3 — Nested trap (MSS 1m ngược DOL 15m)

![[NY0830-Advanced-CaseStudy-Nested-Trap.svg|720]]

**Chuỗi (gãy):** 1m cho một chuỗi raid + MSS xuống rất đẹp, trader short; nhưng 15m đang hướng **LÊN** một BSL chưa chạm → cú "MSS xuống" đó chỉ là nhịp hồi (raid SSL) trong dòng tăng lớn hơn; giá đảo lên quét stop.
**Chẩn đoán:** `missing_step: context15m`.
**Bài học:** 1m chỉ là trigger; chỉ trade MSS 1m khi **đồng hướng DOL 15m** — bảo vệ bằng đọc top-down ([[32 - Top-down Analysis (Multiple Timeframes)]]).

### Case 4 — No-Trade đúng (không tin, range chặt, không raid rõ)

![[NY0830-Advanced-CaseStudy-NoTrade.svg|720]]

**Chuỗi:** ngày không có tin 08:30, không có DOL rõ; sau 08:30 giá đi ngang chặt, không raid sạch biên nào → trader đứng ngoài.
**Chẩn đoán:** thiếu raid + MSS → **no-trade đúng**.
**Bài học:** đứng ngoài cũng là một quyết định process A+; bảo toàn vốn cho ngày có setup A+ quan trọng hơn việc "phải giao dịch".

### Case 5 — Win: chờ nến tin ổn định qua double-sided spike (CPI)

![[NY0830-Advanced-CaseStudy-NewsSpikeWin.svg|720]]

**Bối cảnh HTF:** ngày có CPI 08:30; bias 15m nghiêng bearish (đỉnh 15m đã hình thành trước phiên Á/London, chưa có BSL nào bị chạm).
**Diễn biến từng bước:**
- 08:29 — giá nằm trong build-up hẹp, chưa raid biên nào.
- 08:30:00-08:30:12 — CPI ra, nến 5s/1m quét hai chiều liên tiếp (lên rồi xuống) trong vài giây, spread giãn tạm thời.
- 08:30:15-08:31:00 — chờ 1-2 nến 1m đóng ổn định; nến ổn định cho thấy quét lên chỉ là raid BSL tạm, giá quay đầu xuống mạnh với MSS xuống + displacement rõ, để lại FVG.
- 08:32 — vào SELL tại retest FVG, stop trên đỉnh của toàn bộ range 08:30-08:32.
**Quyết định & lý do:** không vào lệnh trong 15 giây đầu (tránh nhiễu hai chiều); chỉ vào sau khi MSS xác nhận trên nến đã đóng ổn định, đồng hướng bias 15m.
**Kết quả (R):** minh họa +2.2R tại DOL kế tiếp (đáy phiên trước).
**Mổ xẻ:** điểm đúng — tách bạch được "raid nhiễu do tin" và "MSS thật"; không bị cuốn theo cây nến đầu tiên nhìn có vẻ hấp dẫn nhất.
**Bài học thành rule:** trên các ngày có CPI/NFP/PPI, **không đọc cấu trúc trên khung giây/1m trong 30-60 giây đầu sau giờ tin** — quy tắc cứng, không phải gợi ý.

### Case 6 — Loss: entry market đúng 08:30:00 dính spread giãn (XAUUSD, NFP)

![[NY0830-Advanced-CaseStudy-SpreadSlippageLoss.svg|720]]

**Bối cảnh HTF:** ngày NFP; bias 15m bullish rõ (DOL = BSL phía trên chưa chạm); build-up 08:00-08:30 hình thành đáy tương đối.
**Diễn biến từng bước:**
- 08:30:00 — NFP ra đúng lúc giá vừa raid đáy tương đối; nến đầu tiên có vẻ xác nhận MSS lên ngay lập tức.
- 08:30:02 — vào lệnh BUY bằng market ngay khi thấy "MSS", không chờ xác nhận độ rộng spread.
- 08:30:05 — lệnh khớp nhưng giá khớp thật thấp hơn giá hiển thị trên chart 15-25 pip do spread giãn tại broker retail (XAUUSD phản ứng NFP luôn giãn mạnh).
- 08:33 — giá hồi nhẹ đúng như phân tích hướng, nhưng do entry đã xấu, SL (đặt theo giá chart, không theo giá khớp thật) bị chạm trước khi giá đi đúng hướng dự kiến.
**Quyết định & lý do:** ưu tiên tốc độ vào lệnh hơn kiểm soát chi phí giao dịch — sai lầm chính là dùng market order đúng giây tin ra trên một cặp có spread nhạy tin (vàng).
**Kết quả (R):** minh họa -1R (thua dù hướng phân tích sau đó đúng).
**Mổ xẻ:** lỗi không nằm ở đọc cấu trúc mà ở **thực thi** — market order tại đúng 08:30:00 trên tài sản có spread giãn mạnh với tin, cộng với SL tính theo giá chart lý tưởng thay vì giá khớp thật.
**Bài học thành rule:** với vàng/chỉ số quanh giờ tin lớn, ưu tiên **limit order tại PD array** hoặc chờ 10-15 giây đầu ổn định; luôn tính thêm buffer spread vào khoảng cách SL cho riêng phút đầu tiên.

### Case 7 — No-Trade đúng: half-day trước lễ, thanh khoản mỏng bất thường

![[NY0830-Advanced-CaseStudy-HalfDayNoTrade.svg|720]]

**Bối cảnh HTF:** ngày trước Lễ Tạ ơn (NYSE đóng cửa sớm theo lịch half-day); bias 15m không rõ ràng, dao động nhẹ suốt phiên Á/London.
**Diễn biến từng bước:**
- 08:00-08:30 — build-up hình thành nhưng biên độ hẹp hơn trung bình rõ rệt so với các ngày thường.
- 08:30-08:35 — có một cú raid biên nhưng lực rất yếu, giá quay lại range ngay, không để lại displacement hay FVG đáng kể.
- 08:35-09:00 — giá tiếp tục dao động trong range cũ, không hình thành MSS sạch nào.
**Quyết định & lý do:** trước phiên đã tra lịch và biết đây là ngày half-day; kết hợp với raid yếu + không MSS rõ, quyết định đứng ngoài hoàn toàn thay vì ép setup theo đúng "giờ 08:30".
**Kết quả (R):** 0R — không giao dịch.
**Mổ xẻ:** điểm đúng — nhận diện được tín hiệu thanh khoản mỏng từ trước (lịch nghỉ) và xác nhận thêm bằng raid yếu tại chỗ, không để "đến giờ là phải vào".
**Bài học thành rule:** luôn kiểm tra lịch half-day/holiday trước phiên; nếu trùng, tự động hạ kỳ vọng edge của toàn bộ model 08:30 cho ngày đó, coi no-trade là kết quả mặc định hợp lý.

> [!summary] Bảy ca — một thông điệp
> Từ Case 1-4 (chuỗi cấu trúc cơ bản: Win, Loss, Nested trap, No-Trade) đến Case 5-7 (biến số thực chiến: nhiễu tin hai chiều, spread/slippage tại đúng giờ tin, thanh khoản mỏng ngày half-day) — tất cả chỉ khác nhau ở **một hoặc hai mắt xích trong chuỗi hoặc trong thực thi**. Điểm số nằm ở việc *chuỗi có đủ, đồng hướng DOL 15m, và thực thi có tính đến chi phí giao dịch thật hay không* — không nằm ở kết quả P&L của một lệnh đơn lẻ. Ghi `missing_step` cho mọi lệnh không-Win và soi lại hằng tuần ([[07 - Reviews]]).

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
