---
type: ict-concept
concept: Redelivered Rebalanced Price Range
aliases:
  - Redelivered Rebalanced Price Range
  - RDRB
  - RRPR
tags:
  - trading/ict/concept
  - trading/study
  - "#pd-array"
status: seed
category: PD Array
last_reviewed: 2026-07-09
created: 2026-07-09
updated: 2026-07-09
---

# Redelivered Rebalanced Price Range

> [!summary] Tóm tắt 1 câu
> **RDRB (Redelivered Rebalanced Price Range) là một PD array "ẩn" gồm HAI nến — giá deliver một chiều, kéo lại để lại một wick rồi redeliver tiếp cùng chiều — không để lại FVG nhìn thấy được, nhưng vùng giá giữa wick của nến TRƯỚC và nến SAU cặp đó vẫn hoạt động như support (bull) / resistance (bear).**

> [!important] Nguyên tắc cốt lõi
> Điểm mấu chốt của RDRB **không** nằm ở hai nến RDRB, mà ở cách **đánh dấu**: bỏ qua hai nến RDRB, đánh dấu **wick của nến ngay trước** và **wick của nến ngay sau** cặp đó — khoảng giá giữa hai wick này chính là RDRB price range. Vì delivery ở đây "cân bằng hiệu quả" (không có delay để lại imbalance), mắt thường không thấy gap, nhưng smart money vẫn để lại dấu chân ở vùng đó và bảo vệ nó khi giá quay lại. RDRB là **PD array**, dùng đúng như [[13 - FVG  - Fair Value Gap]] hay [[25 - OB - Order Block]]: chờ retest + xác nhận, không phải nút bấm.

---

## 1. Định nghĩa

**Khái niệm:** RDRB (còn gọi **RRPR** — Redelivered Rebalanced Price Range) là một **hidden PD array** cấu thành từ **hai nến liên tiếp**. Cơ chế: nến đầu **deliver** (đẩy giá) về một phía rồi **quay lại**, đóng nến với một **wick** ở phía đóng; nến thứ hai **mở ra và redeliver** tiếp **cùng chiều**, đóng ở mức đã đẩy tới. Vì giá được giao (deliver) rồi giao lại (redeliver) một cách trơn tru, **không có imbalance/FVG hiển thị** — nhưng vùng đó vẫn là một PD array hợp lệ.

**Mục đích trong ICT:** cho bạn thêm một **điểm phản ứng (POI)** ở những chân giá "sạch" mà FVG không xuất hiện — nơi đa số trader nghĩ "không có gì để vào". Đây là biến thể **hiếm và ít người nhận ra** của họ PD array, bổ sung cho FVG (biến thể hiển thị) khi chart không cho bạn một gap rõ ràng.

![[RDRB-Advanced-Anatomy.svg|697]]

*Giải phẫu RDRB: nến A deliver lên rồi kéo lại để lại upper wick khi đóng; nến B mở ra redeliver tiếp lên. Bỏ qua A và B — đánh dấu wick của **nến trước A** và **nến sau B**; khoảng giữa hai wick đó là RDRB price range (vùng support khi giá retest trong bối cảnh bull).*

**Nó giúp trả lời câu hỏi nào trên chart?**

- Chân giá này "sạch" không có FVG — vậy còn POI nào để canh entry không?
- Vùng nào trong đợt đẩy vừa rồi smart money sẽ bảo vệ khi giá quay lại?
- Tôi có một PD array hợp lệ để phân tầng entry/stop/target ở đây không?

### RDRB KHÔNG phải là gì

- **Không phải** FVG — FVG là imbalance 3 nến có **gap nhìn thấy** (wick nến 1 và nến 3 không chồng); RDRB là mẫu 2 nến deliver–redeliver **không có gap** (xem mục 6).
- **Không phải** vùng đánh dấu trên hai nến RDRB — range nằm giữa wick của **nến trước và nến sau** (đánh dấu sai sẽ đảo ngược vùng — xem mục 3).
- **Không phải** trigger vào lệnh — chạm range chỉ là *alert*; entry cần **LTF MSS** xác nhận.
- **Không phải** mọi cú tiếp diễn 2 nến — phải đúng chuỗi **deliver → pullback để lại wick → redeliver cùng chiều**.

---

## 2. Cơ chế sâu — vì sao vùng "cân bằng" vẫn là PD array

Đây là phần "why" ít người giải thích. Hiểu cơ chế mới phân biệt được RDRB thật với một cú tiếp diễn 2 nến tình cờ.

**(a) Delivery và redelivery là hành vi có chủ đích.** Trong mô hình ICT, giá được các market maker "giao" (deliver) quanh các mức thanh khoản. Ở một FVG, engine đẩy nhanh đến mức **để lại delay** (khoảng trống chưa giao) — đó là imbalance. Ở RDRB, engine đẩy (deliver), **rút lại để cân bằng** (rebalance — chính là cái wick pullback), rồi **giao lại** (redeliver) cùng chiều. Kết quả là một vùng được giao **hai lần**, "no visible imbalance" — nhưng chính việc **cân bằng rồi tái giao ngay tại chỗ** đánh dấu vùng đó là nơi engine cam kết giá.

**(b) Cái wick pullback = dấu vân tay.** Wick mà nến đầu để lại khi kéo về không phải nhiễu — nó là **bằng chứng có lực đối ứng** tại đó, và việc nến sau **mở ra redeliver ngay cùng chiều** cho thấy lực đối ứng đó đã bị hấp thụ và bên thắng tiếp tục. Vùng giữa wick trước và wick sau vì thế là **vùng giá mà cả hai phía đã "đồng thuận"** — khi giá quay lại, smart money có động cơ bảo vệ nó (mua lại ở support bull / bán lại ở resistance bear).

**(c) Vì sao đánh dấu bằng wick nến bao quanh, không phải nến RDRB.** Hai nến RDRB là phần "đã giao xong" (đã cân bằng). Vùng **chưa được test lại** — vùng còn "mở" về mặt order flow — nằm ở **rìa**: wick của nến ngay trước (điểm khởi phát delivery) và wick của nến ngay sau (điểm kết thúc redelivery). Đánh dấu trên thân hai nến RDRB sẽ trỏ nhầm vào vùng đã cân bằng, làm lệch cả entry lẫn stop.

> [!info] RDRB so với các PD array khác
> FVG nói "có delay chưa giao, giá sẽ quay lại lấp". RDRB nói "vùng này đã được giao rồi giao lại trơn tru — nhưng vẫn là mốc engine cam kết, giá sẽ tôn trọng khi quay lại". Cùng họ hàng với [[03 - Balanced Price Range]] và [[41 - Change in State of Delivery]] ở chỗ đều đọc **cách giá được giao (delivery)**, không chỉ nhìn hình nến. RDRB là mảnh hiếm nên đừng ép nó xuất hiện ở mọi nơi.

---

## 3. Cách đánh dấu ĐÚNG (điểm mấu chốt)

![[RDRB-Advanced-Marking.svg|697]]

Đây là lỗi số 1 và cũng là toàn bộ độ khó của RDRB.

**SAI (bên trái):** đánh dấu range trên **hai nến RDRB** → vùng bị **đảo ngược**, entry và stop sai chỗ.

**ĐÚNG (bên phải):** đánh dấu **wick của nến ngay TRƯỚC** cặp RDRB và **wick của nến ngay SAU** cặp RDRB. Khoảng giá giữa hai wick này là RDRB price range.

Quy tắc thao tác:

1. Xác định cặp 2 nến RDRB (deliver → pullback wick → redeliver cùng chiều).
2. Nhìn sang **nến liền trước** cặp: lấy **wick** của nó.
3. Nhìn sang **nến liền sau** cặp: lấy **wick** của nó.
4. Vẽ box từ wick này đến wick kia — đó là vùng để canh retest.

> [!warning] Kiểm tra nhanh trước khi tin
> Nếu bạn vẽ box mà thấy nó **trùng khít thân hai nến RDRB**, bạn đã đánh dấu sai. Vùng đúng luôn tham chiếu **nến bao quanh**, không phải cặp ở giữa.

---

## 4. Bối cảnh sử dụng

### Khi nào RDRB có giá trị cao?

- [ ] **Thuận HTF bias** (Daily/H4) — xem [[12 - Daily Bias]]; RDRB ngược trend hit-rate thấp hẳn
- [ ] Nằm trong một **chân đẩy có hướng rõ** (directional leg), không phải giữa vùng đi ngang
- [ ] Ở đúng vùng **Premium/Discount** phù hợp hướng vào ([[27 - Premium Discount]])
- [ ] Xuất hiện trong **killzone / macro** ([[18 - Kill Zones]], [[40 - Macro Times]])
- [ ] Có **draw on liquidity** rõ làm target ([[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]])
- [ ] Có kế hoạch chờ **LTF MSS** khi giá retest (không vào mù)

### Khi nào nên bỏ qua?

- [ ] **Không có HTF bias** hoặc RDRB ngược bias không narrative mạnh
- [ ] Nằm **giữa range**, xa mọi pool thanh khoản
- [ ] Chỉ là **cú tiếp diễn 2 nến** thường, thiếu chuỗi deliver–pullback–redeliver
- [ ] Chart đã có **FVG rõ ràng** ở cùng vùng → dùng FVG (dễ đánh dấu, phổ biến hơn)
- [ ] Retest tới range nhưng **không có** LTF MSS xác nhận

---

## 5. Bullish vs Bearish RDRB

![[RDRB-Advanced-BullBear.svg|697]]

**Bullish RDRB:** thị trường đẩy về **buy side** nhưng retrace, để lại **upper wick** khi nến đầu đóng; nến sau mở ra tiếp tục lên, redeliver buy side và đóng ở mức cao. Khi giá quay lại range → **support** → tìm **long**.

**Bearish RDRB:** giá đẩy về **sell side** nhưng pullback trước khi đóng, để lại **lower wick**; nến sau mở ra tiếp tục xuống, đóng gần/tại đáy. Khi giá quay lại range → **resistance** → tìm **short**.

> [!tip] Cách nhớ chiều của wick
> Wick pullback luôn ở **phía ngược hướng delivery**: bull deliver lên → wick ở **trên**; bear deliver xuống → wick ở **dưới**. Nếu wick nằm cùng phía với hướng đi, đó không phải mẫu deliver–pullback–redeliver hợp lệ.

---

## 6. RDRB vs Fair Value Gap

![[RDRB-Advanced-vs-FVG.svg|697]]

Nhìn thoáng qua RDRB giống FVG, nhưng **cơ chế và cách đánh dấu khác hẳn**.

| Tiêu chí | Fair Value Gap (FVG) | RDRB |
|---|---|---|
| Số nến | **3 nến** | **2 nến** (deliver–redeliver) |
| Gap nhìn thấy? | **Có** — wick nến 1 & nến 3 không chồng | **Không** — delivery cân bằng, no visible gap |
| Đánh dấu vùng | Giữa wick nến 1 và nến 3 | Giữa wick **nến trước** và **nến sau** cặp RDRB |
| Bản chất | Imbalance (delay chưa giao) | Redelivered/rebalanced (đã giao rồi giao lại) |
| Độ phổ biến | Phổ biến, dễ thấy | **Hiếm**, ẩn, ít người nhận ra |
| Vai trò | PD array | PD array |

Cả hai đều là PD array — support (bull) / resistance (bear). RDRB là biến thể **ẩn** cho những chân giá không để lại FVG; FVG là biến thể **hiển thị**. Khi có FVG rõ ở cùng vùng, ưu tiên FVG vì dễ đánh dấu và phổ biến hơn.

---

## 7. Quy trình vào lệnh

![[RDRB-Advanced-TradeFlow.svg|697]]

**Bước 1 — HTF bias.** Xác định bias trên **Daily & H4** (bull/bear). Chỉ tìm RDRB thuận bias.

**Bước 2 — Nhận diện cặp RDRB.** Tìm 2 nến: deliver một chiều → pullback để lại wick khi đóng → nến sau redeliver cùng chiều.

**Bước 3 — Đánh dấu range đúng.** Lấy wick **nến trước** và wick **nến sau** cặp; box giữa chúng là RDRB price range (mục 3).

**Bước 4 — Xác nhận bias alignment + P/D.** RDRB thuận bias, ở đúng vùng Premium/Discount. Ngược bias thì bỏ.

**Bước 5 — Chờ retest.** Giá phải **quay lại** vào trong range. Chưa retest thì chưa có gì để làm.

**Bước 6 — Hạ khung.** Xuống **M5/M1** khi giá vào range.

**Bước 7 — Chờ LTF MSS.** Một **Market Structure Shift** ([[21 - Market Structure Shift]]) sạch bên trong range xác nhận phản ứng. Đây là *signal*.

**Bước 8 — Entry.** Buy tại bullish RDRB / sell tại bearish RDRB, sau MSS.

**Bước 9 — Stop.** **Vượt hẳn mép ĐỐI DIỆN** của RDRB range + một buffer nhỏ. Không parked ở thân nến RDRB (bị wick quét — xem mục Lỗi thường gặp). Tôn trọng **risk ≤0.5%/lệnh** ([[43 - Position Sizing]]).

**Bước 10 — Target.** Draw on liquidity kế tiếp: old high/low, relative equal highs/lows, HTF FVG. Phân tầng theo [[16 - Internal & External Range Liquidity (IRL & ERL)]]: **T1 = IRL**, **T2 = ERL / external draw** ([[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]).

---

## 8. Ví dụ chart

### Ví dụ đúng

![[RDRB-Example-Correct.svg|697]]

**Mô tả:** Bias bull, trong một chân đẩy lên ở discount xuất hiện **bullish RDRB** (deliver lên → upper wick → redeliver lên). Đánh dấu range bằng wick nến trước & nến sau. Giá **retest** vào range (①), ở M5 in **MSS lên** (②) → **Entry Long** (③), stop dưới mép đối diện của range, target **old high / BSL** (④).

**Vì sao đây là ví dụ tốt:**

- **Thuận HTF bias bull**, ở **discount** — đúng bối cảnh.
- Đánh dấu range **đúng** (wick nến bao quanh, không phải nến RDRB).
- Có **LTF MSS** trong range = confirmation, không vào mù.
- **Stop vượt mép đối diện** (không bị wick retest quét), R:R lành mạnh (T1=IRL, T2=ERL).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp chart NQ/ES/EURUSD/XAUUSD: đánh dấu (1) cặp 2 nến RDRB, (2) wick nến trước & nến sau + box range, (3) HTF bias & vùng P/D, (4) retest + LTF MSS, (5) entry/stop/target.*

### Ví dụ sai / dễ nhầm

![[RDRB-Example-Wrong.svg|697]]

**Mô tả lỗi:** (①) Đánh dấu range **trên chính hai nến RDRB** → vùng đảo ngược. (②) Thực ra chỉ là **cú tiếp diễn 2 nến thường**, thiếu chuỗi deliver–pullback–redeliver. (③) Vào **ngược bias**, giữa range, **không** chờ LTF MSS; stop parked ở thân nến RDRB → bị wick quét.

**Bài học:**

- Range luôn tham chiếu **wick nến trước & sau**, không phải cặp RDRB.
- Phải đúng mẫu **deliver → pullback wick → redeliver**; không thì không phải RDRB.
- **Thuận bias + LTF MSS** mới vào; stop **vượt mép đối diện**, không ở thân nến.

---

## 9. Thực hành tốt nhất (Best Practices)

> [!tip] 7 quy tắc RDRB
> 1. **Đánh dấu bằng wick nến TRƯỚC & SAU** cặp RDRB — không bao giờ dùng thân hai nến RDRB.
> 2. **Chỉ trade thuận HTF bias** — RDRB ngược bias hit-rate thấp.
> 3. **RDRB là PD array, không phải trigger** — chờ retest + **LTF MSS** mới vào.
> 4. **Phân biệt với FVG** — 2 nến no-gap (RDRB) vs 3 nến có gap (FVG); có FVG rõ thì ưu tiên FVG.
> 5. **Stop vượt mép đối diện của range** + buffer — đừng parked ở thân nến (bị wick quét).
> 6. **Đúng mẫu mới tính** — deliver → pullback wick → redeliver cùng chiều; loại các cú 2 nến thường.
> 7. **Lọc theo P/D + killzone/macro** — bull ở discount, bear ở premium, trong giờ chất lượng.

- RDRB rõ nhất trên **NQ & ES** (M1/M5, hành động nhanh làm mẫu 2 nến dễ thấy), **GBPUSD & EURUSD** trong các chân London killzone sạch, **XAUUSD** ở các chân tin retest phiên sau. Macro **09:50 NY-AM** thường in RDRB được retest sau đó cùng phiên NY.
- Ghi nhật ký mỗi RDRB: có đánh dấu đúng wick bao quanh không, có LTF MSS không, kết quả — để đo edge của riêng biến thể này.
- Vì RDRB **hiếm**, hãy coi nó là "bonus POI" bổ sung cho bộ setup chính (2022 Model), không phải setup săn hằng ngày.

> [!warning] Bối cảnh prop-firm (FTMO & The5ers)
> RDRB là một PD array **hiếm** — cạm bẫy lớn nhất là **ép nó xuất hiện** để có cớ vào lệnh.
> - **FTMO 10K:** daily loss đo theo **balance cố định** đầu ngày, reset mỗi ngày; có yêu cầu **số ngày giao dịch tối thiểu**. Đừng dùng "thấy RDRB" để overtrade cho đủ ngày — số ngày là điều kiện, không phải lý do vào lệnh kém chất lượng.
> - **The5ers 10K:** logic loss tham chiếu **equity đóng cửa hôm trước**; cần **số ngày có lãi tối thiểu** (~0.5%+/ngày). Cạm bẫy: cố nặn một RDRB mờ để "kiếm một ngày xanh" — đây đúng là kiểu ép lệnh phá kỷ luật.
> - **Không trộn lẫn hai bộ luật.** RDRB không đổi luật của firm nào; nó chỉ là thêm một POI chất lượng *khi hội đủ điều kiện*.
> **Process > outcome, risk ≤0.5%/lệnh.** Trong giai đoạn **foundation/backtesting** hiện tại: gom một mẫu RDRB đủ lớn, đánh dấu **đúng chuẩn wick bao quanh**, và đo win-rate/expectancy **tách riêng** trước khi cho nó vào playbook thật.

---

## 10. Checklist trước khi dùng

> [!warning] RDRB không phải nút "mua/bán"
> Chạm range chỉ là alert. Entry cần đánh dấu đúng + thuận bias + LTF MSS.

- [ ] Đúng mẫu **deliver → pullback wick → redeliver** cùng chiều
- [ ] Đánh dấu range bằng **wick nến trước & nến sau** (không phải nến RDRB)
- [ ] **Thuận HTF bias** và đúng vùng **Premium/Discount**
- [ ] Nằm trong **chân giá có hướng**, không giữa range
- [ ] Giá đã **retest** vào range
- [ ] Có **LTF MSS** xác nhận trong range
- [ ] **Stop** vượt hẳn mép đối diện của range + buffer
- [ ] **Target** rõ (T1=IRL, T2=ERL / draw on liquidity)
- [ ] Trong killzone/macro; instrument thanh khoản tốt
- [ ] **Risk ≤0.5%**, tuân daily/weekly loss limit của firm

---

## 11. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Đánh dấu sai nến | Box trùng thân 2 nến RDRB, vùng đảo ngược | Luôn dùng wick **nến trước & nến sau** cặp |
| Trade không bias | Vào theo cảm giác, ngược cấu trúc | Xác định Daily Bias trước; chỉ trade thuận bias |
| Thiếu LTF MSS | Vào ngay khi giá chạm range | Range = alert; chờ MSS trong range mới vào |
| Nhầm với FVG | Đếm 3 nến / tìm gap ở RDRB | FVG = 3 nến có gap; RDRB = 2 nến no-gap |
| Stop quá sát | Parked ở thân nến RDRB, bị wick quét | Đặt stop vượt mép **đối diện** của range + buffer |
| Nhầm mọi cú 2 nến là RDRB | Thấy 2 nến cùng chiều là vào | Phải đúng deliver–pullback wick–redeliver |
| Ép RDRB để có cớ vào | "Cố" nặn range mờ để trade | RDRB hiếm; không đủ điều kiện thì bỏ |

---

## 12. Câu hỏi tự kiểm tra

- Tôi giải thích RDRB trong 30 giây và phân biệt với FVG được không?
- Cơ chế "why": vì sao một vùng "cân bằng, no gap" vẫn là PD array?
- Đánh dấu range ở đâu — trên nến RDRB hay wick nến bao quanh? Vì sao?
- Mẫu 3 điều kiện của một RDRB hợp lệ là gì?
- RDRB là bias, POI, entry hay target? Tôi dùng nó ở bước nào?
- Vì sao stop không parked ở thân nến RDRB?
- Trong journal của tôi, RDRB thuận bias + LTF MSS cho expectancy khác nhóm còn lại ra sao?

---

## 13. Flashcards / Active Recall

### Q1
**Hỏi:** RDRB là gì trong 1 câu?
**Đáp:** PD array ẩn gồm 2 nến deliver–pullback wick–redeliver cùng chiều, không có gap nhìn thấy; range = vùng giữa wick nến trước và nến sau cặp, hoạt động như support (bull) / resistance (bear).

### Q2
**Hỏi:** Đánh dấu RDRB price range ở đâu?
**Đáp:** Giữa **wick của nến ngay trước** và **wick của nến ngay sau** cặp RDRB — KHÔNG phải trên hai nến RDRB (đánh dấu trên nến RDRB sẽ đảo ngược vùng).

### Q3
**Hỏi:** RDRB khác FVG thế nào?
**Đáp:** FVG = imbalance 3 nến có gap nhìn thấy (wick nến 1 & 3 không chồng). RDRB = mẫu 2 nến deliver–redeliver không có gap; range nằm giữa wick nến bao quanh. RDRB là biến thể ẩn, hiếm.

### Q4
**Hỏi:** Ba điều kiện của một RDRB hợp lệ?
**Đáp:** (1) nến deliver một chiều rồi pullback để lại wick; (2) nến sau mở ra redeliver cùng chiều, đóng ở mức đã đẩy; (3) không có gap hiển thị (delivery cân bằng).

### Q5
**Hỏi:** RDRB có phải trigger vào lệnh không?
**Đáp:** Không. Nó là PD array. Vào lệnh cần: thuận bias + retest vào range + **LTF MSS** xác nhận.

### Q6
**Hỏi:** Stop đặt ở đâu và vì sao?
**Đáp:** Vượt hẳn **mép đối diện** của RDRB range + buffer. Parked ở thân nến RDRB bị wick retest quét oan.

### Q7
**Hỏi:** Vì sao vùng "cân bằng, no gap" vẫn là PD array?
**Đáp:** Vì delivery ở đó được giao rồi giao lại (redelivered/rebalanced) ngay tại chỗ — engine cam kết giá tại vùng đó; wick pullback là dấu vân tay của lực đối ứng đã bị hấp thụ, nên smart money bảo vệ vùng khi giá quay lại.

### Q8
**Hỏi:** Cạm bẫy prop-firm lớn nhất với RDRB?
**Đáp:** Ép nó xuất hiện để có cớ vào lệnh (vì nó hiếm) → overtrade phá daily loss (FTMO: balance cố định) hoặc cố "kiếm ngày xanh" (The5ers: cần ngày có lãi ~0.5%). Không trộn hai bộ luật; risk ≤0.5%.

---

## 14. Lesson Learned

- **RDRB nằm ở wick nến bao quanh, không ở cặp nến RDRB.** Một câu này quyết định đúng/sai toàn bộ setup.
- **Hiếm không có nghĩa là phải săn.** RDRB là bonus POI khi hội đủ điều kiện, không phải setup vào hằng ngày — ép nó = overtrade.
- **PD array ≠ trigger.** Không LTF MSS trong range thì range chỉ là alert; đừng vào mù.
- **Stop vượt mép đối diện, không ở thân nến** — né wick retest quét oan.
- **Foundation phase:** đánh dấu chuẩn, gom mẫu, đo expectancy tách riêng — để RDRB được vào playbook bằng dữ liệu, không bằng cảm giác.

---

> [!cite] Nguồn
> [ICT Redelivered Rebalanced Price Range (RDRB) — Hidden PD Array](https://innercircletrader.net/tutorials/ict-redelivered-rebalanced-price-range/)
