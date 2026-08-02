---
tags:
  - trading/study
  - "#SeekAndDestroy"
status: developing
category: Time & Price
last_reviewed: 2026-07-28
created: 2026-07-28
updated: 2026-07-28

---

# Seek and Destroy Friday

> [!info] Link
> Nguồn gốc: [ICT Seek and Destroy Friday: Profile, Setup & How to Trade It](https://innercircletrader.net/tutorials/ict-seek-and-destroy-friday/)

> [!summary] Tóm tắt 1 câu
> **Seek and Destroy Friday là một weekly profile "trung tính/xác suất thấp": giá đi ngang (chop) từ Thứ Hai tới Thứ Năm trước một tin lớn (NFP/FOMC/CPI), rồi vào Thứ Sáu (hoặc ngày có tin) quét thanh khoản CẢ HAI phía của range đó trước khi thật sự chạy theo hướng weekly order flow — giá trị chính của mô hình là biết ĐỨNG NGOÀI cho tới khi tin ra và sweep xác nhận, không phải một setup entry cầu kỳ.**

> [!important] Nguyên tắc cốt lõi
> **Cardinal rule: KHÔNG trade trước khi tin ra, không có ngoại lệ.** Trước tin, thị trường coil (siết) tại đỉnh/đáy của range Mon–Thu để engineering liquidity hai phía — buy-side liquidity (BSL) phía trên range high, sell-side liquidity (SSL) phía dưới range low. Sau tin, giá quét MỘT phía trước (thường ngược với weekly bias), rồi displace mạnh theo đúng hướng weekly order flow. Chỉ cú di chuyển SAU sweep + xác nhận cấu trúc mới là "cái trade" — không phải cú sweep, và tuyệt đối không phải bất cứ điều gì xảy ra trước tin.

---

## 1. Định nghĩa

**Seek and Destroy Friday** là một trong các weekly profile của ICT, mô tả tuần giao dịch mà giá KHÔNG có hướng rõ ngay từ đầu tuần (khác với các weekly profile có bias mở đầu tuần), mà thay vào đó dành Thứ Hai–Thứ Năm để tích lũy (consolidate) ngay trước một sự kiện kinh tế có tác động lớn — phổ biến nhất là **NFP** (Non-Farm Payroll, Thứ Sáu đầu tháng, 08:30 NY) hoặc **FOMC** (8 lần/năm, thường Thứ Tư 14:00 NY). Đến ngày có tin, giá quét cả hai phía của range Mon–Thu — đầu tiên là phía đối lập với hướng thật, sau đó displace mạnh theo hướng weekly order flow — trước khi tiếp tục theo hướng đó.

Trong ngôn ngữ ICT: đây là **Power of 3 nén vào một phiên**. Accumulation đã xảy ra suốt Mon–Thu; Thứ Sáu (hoặc ngày có tin) là **manipulation day** — cú sweep hai phía là hành vi thao túng liquidity thuần túy, không phải move thật; distribution là cú displace sau sweep, đi theo hướng weekly bias thật ([[02 - AMD]]).

![[SeekDestroy-PowerOf3-Frame.svg|720]]
> [!info] Mô tả hình
> 3 khối nối tiếp theo màu: Accumulation (Mon–Thu, xanh dương), Manipulation (Friday @ tin, cam), Distribution (sau sweep, xanh lá) — Power of 3 nén vào đúng một phiên duy nhất.

> [!info] Không phải mọi tuần có tin đều là Seek and Destroy
> Đây là một profile CÓ ĐIỀU KIỆN, không phải quy luật cứng mỗi tuần có NFP/FOMC. Cần đủ 3 dấu hiệu ở mục 5 mới coi là "S&D week" — nếu thiếu, đây chỉ là một tuần bình thường có tin, không nên ép khung.

---

## 2. Bối cảnh sử dụng

- **Thị trường phù hợp:** FX majors (EURUSD, GBPUSD, USDJPY…), chỉ số (NQ1/ES, DXY), vàng (XAU) — mọi instrument nhạy với USD macro data.
- **Khi nào xuất hiện:** phổ biến nhất là tuần NFP (Thứ Sáu đầu tháng), tuần có FOMC (thường Thứ Tư), và các tuần có CPI, quyết định lãi suất ngân hàng trung ương lớn, hoặc sự kiện chính trị lớn đã biết trước. Yếu tố chung: **mức độ bất định lớn tới mức các desk tổ chức không muốn định vị trước khi số liệu ra**, nên họ để giá coil và engineering liquidity ở hai đầu range trong lúc chờ.
- **Không phù hợp:** những tuần không có lịch tin lớn nào rơi vào cuối tuần, hoặc những tuần daily action đã có hướng rõ ràng từ đầu tuần (đó là profile khác, ví dụ trending week thông thường).
- **Liên hệ với các mô hình khác trong vault:** đây là một biến thể đặc biệt của tư duy [[20 - Liquidity Sweep]] + [[21 - Market Structure Shift|MSS]]/CISD áp trên khung thời gian tuần, và có quan hệ trực tiếp với [[05 - Friday Profit Taking]] — cả hai đều nói về "ngoại lệ" của thứ Sáu, nhưng theo hai cơ chế hoàn toàn khác nhau (xem mục Bối cảnh sử dụng ở phần liên kết chéo cuối bài).

---

## 3. Cấu trúc nhận diện trên chart

![[SeekDestroy-Mechanism.svg|720]]
> [!info] Mô tả hình
> Sơ đồ AMD nén vào 1 tuần: range Mon–Thu (accumulation) với BSL phía trên, SSL phía dưới; mốc tin lớn; sweep phía đối lập bias trước (manipulation); MSS/CISD; move thật đi theo weekly bias (distribution).

Ba thành phần cấu trúc bắt buộc phải nhận ra trên chart:

1. **Range Mon–Thu (hoặc Mon–Wed nếu tin là FOMC giữa tuần).** Range high = pool buy-side liquidity (BSL); range low = pool sell-side liquidity (SSL). Range này thường không đẹp và "sạch" như range của các mô hình khác — có thể có higher-highs kèm lower-lows bất thường (irregular swing), không nhất thiết đi ngang phẳng.
2. **Cú sweep hai phía tại/ngay sau tin.** Phía bị quét TRƯỚC luôn ngược với hướng weekly bias thật — đây là cú Judas kinh điển ở cấp độ tuần. Phía còn lại chỉ bị test/không bị quét, hoặc bị quét nhẹ hơn nhiều.
3. **MSS/CISD trên LTF (5m hoặc 15m) ngay sau sweep, cùng hướng weekly bias.** Đây là xác nhận bắt buộc — không có nó thì cú sweep chỉ là một cú quét đơn thuần, chưa phải "trade".

![[SeekDestroy-Bullish-Bearish-Symmetry.svg|720]]
> [!info] Mô tả hình
> So sánh song song 2 cột: bullish market (sweep SSL trước → MSS/CISD lên → target HTF draw trên) và bearish market (sweep BSL trước → MSS/CISD xuống → target HTF draw dưới) — cùng cơ chế, đối xứng hướng.

Cơ chế hoàn toàn đối xứng theo hướng bias:

- **Weekly bias bullish:** phase chop Mon–Thu thường có higher-highs kèm lower-lows bất thường. Sau tin, giá quét **SSL** (sell-side, dưới range low) trước — càn stop của người mua sớm — rồi displace mạnh lên, MSS/CISD 5m/15m lên xác nhận, đi tới HTF draw phía trên.
- **Weekly bias bearish:** phase chop Mon–Thu thường có lower-lows kèm higher-highs bất thường. Sau tin, giá quét **BSL** (buy-side, trên range high) trước — càn stop của người bán sớm — rồi displace mạnh xuống, MSS/CISD 5m/15m xuống xác nhận, đi tới HTF draw phía dưới.

---

## 4. Bối cảnh sử dụng nâng cao — vì sao mô hình hình thành

Seek and Destroy week hình thành khi thị trường chờ một sự kiện đủ lớn để reset toàn bộ positioning hiện tại:

- **NFP** — Thứ Sáu đầu tháng, 08:30 NY. Tác động mạnh lên các cặp USD và chỉ số Mỹ.
- **FOMC** — 8 lần/năm, thường Thứ Tư 14:00 NY. Tạo dynamic sweep tương tự nhưng sớm hơn trong tuần (Mon–Wed range thay vì Mon–Thu).
- **Khác:** CPI, quyết định lãi suất ngân hàng trung ương lớn (Fed, ECB, BOE…), sự kiện chính trị lớn đã lên lịch trước.

Điểm chung: mức độ bất định đủ lớn khiến các desk tổ chức **không muốn định vị trước khi số liệu ra**, nên để giá coil trong lúc engineering liquidity ở cả hai đầu range — cao của range trở thành pool BSL, thấp của range trở thành pool SSL, và Thứ Sáu (hoặc ngày tin) có "nhiệm vụ" lấy cả hai trước khi move thật bắt đầu.

---

## 5. Quy trình đa khung — nhận diện & giao dịch

Đọc theo trình tự: **xác nhận profile bằng HTF trước Thứ Sáu → mốc lịch tin → range Mon–Thu → LTF sau tin**.

### A. Ba dấu hiệu xác nhận Seek and Destroy week (nhận ra được từ Thứ Tư/Thứ Năm)

![[SeekDestroy-Identification-Signals.svg|720]]
> [!info] Mô tả hình
> 3 ô dấu hiệu nối tiếp: lịch tin high-impact vào Thứ Sáu, Mon–Thu đi ngang/nhiễu, divergence giữa weekly bias rõ và daily action không theo — đủ cả ba thì coi là S&D week; kèm cảnh báo tỷ lệ dương tính giả cao.

1. **Có tin high-impact đánh dấu đỏ vào (hoặc ngay trước) Thứ Sáu** — kiểm tra lịch kinh tế (Forex Factory hoặc lịch của broker).
2. **Mon–Thu đi ngang hoặc có swing bất thường** — higher-highs kèm lower-lows, hoặc các nến range hẹp qua lại, thay vì một cú đẩy có hướng sạch.
3. **Weekly order flow HTF có bias RÕ, nhưng daily candles KHÔNG honor bias đó.** Chính sự lệch pha (divergence) giữa "HTF biết hướng" và "LTF chưa đi theo" là tín hiệu then chốt.

Nếu đủ cả ba, coi cả phần còn lại của tuần là Seek and Destroy: **không** counter-trend entry giữa tuần, **không** đu theo các fakeout giữa range — chỉ đợi tới ngày có tin.

### B. Quy trình xử lý sau khi tin ra (chuỗi thống nhất, áp cho cả 2 hướng)

1. **Xác nhận profile trước Thứ Năm đóng cửa** — tin lớn + Mon–Thu range-bound + weekly bias HTF rõ.
2. **Đánh dấu range high (BSL) và range low (SSL) của Mon–Thu** — đây là hai pool thanh khoản sẽ bị nhắm tới.
3. **Đứng ngoài tuyệt đối cho tới giờ tin ra.** Không pre-position. Không "scalp cái chop".
4. **Quan sát phía nào bị sweep TRƯỚC sau tin.** Phía đối diện là hướng entry của bạn.
5. **Chờ giá trade NGƯỢC LẠI vào trong range** — cú sweep cần có một nhịp hồi trở lại giữa range, đây là "dấu tay" tổ chức.
6. **Xuống 5m hoặc 15m, tìm MSS hoặc CISD** ngược hướng cú sweep (tức đồng hướng weekly bias).
7. **Entry tại đóng nến MSS/CISD hoặc một retest sạch.** Stop ngay ngoài điểm cực trị bị sweep. Target là HTF draw kế tiếp (đỉnh/đáy đáng kể gần nhất, đỉnh/đáy tuần trước, hoặc target order flow daily/weekly).

> [!tip] Pro tip từ nguồn gốc
> Setup mạnh nhất là khi cú displacement sau sweep để lại một FVG hoặc breaker sạch trên đường quay lại vào range. Nếu giá hồi về lấp khoảng trống đó trước khi tiếp tục, bạn có một entry thứ hai với R:R còn tốt hơn. Bỏ qua tuần Seek and Destroy nào mà weekly order flow HTF không rõ — không có target rõ thì không có lý do vào lệnh.

> [!example] Mẫu ghi nhanh — một phiên Seek and Destroy Friday
> ```text
> Lịch tin: [NFP/FOMC/CPI/khác] @ [giờ NY]
> Weekly bias HTF: [bullish/bearish], D1/H4 confirm
> Mon–Thu range: high [level] (BSL) / low [level] (SSL)
> 3 dấu hiệu xác nhận: lịch tin ✔ / chop Mon-Thu ✔ / divergence HTF-LTF ✔
> Sweep 1 (phía đối lập bias) @ [giờ, level]
> Hồi lại vào range: ✔/✗
> LTF trigger: MSS/CISD [5m/15m] @ [giờ] hướng [lên/xuống]
> Entry: [giá] | Stop: ngoài [điểm cực trị bị sweep] | Target: HTF draw @ [level]
> Risk: 0.5–1% | R:R dự kiến: [x]
> ```

---

## 6. Quy tắc xác nhận / vô hiệu hóa

| Trạng thái | Điều kiện | Hành động |
|---|---|---|
| **Xác nhận Long** | Weekly bias bullish + đủ 3 dấu hiệu S&D + sweep SSL sau tin + MSS/CISD LTF lên | Vào Long tại đóng nến MSS/CISD hoặc retest, stop dưới đáy sweep |
| **Xác nhận Short** | Weekly bias bearish + đủ 3 dấu hiệu S&D + sweep BSL sau tin + MSS/CISD LTF xuống | Vào Short tại đóng nến MSS/CISD hoặc retest, stop trên đỉnh sweep |
| **Chưa đủ (chờ)** | Đã sweep một phía nhưng CHƯA có MSS/CISD LTF | Đứng ngoài, chờ xác nhận cấu trúc — không vào tại nến sweep |
| **Vô hiệu (skip)** | Weekly bias không rõ / không đủ 3 dấu hiệu / range Mon-Thu không tồn tại rõ | Không coi đây là Seek and Destroy week, không áp mô hình |
| **Vô hiệu sau entry** | Giá đóng lại qua điểm cực trị bị sweep theo hướng ngược, hoặc MSS/CISD bị phá ngược | Cắt lệnh, không dời stop chạy theo hy vọng |
| **Tránh (điều kiện xấu)** | Trade TRƯỚC giờ tin dù giá "trông như" đang breakout | Tuyệt đối không vào — đây là vi phạm cardinal rule |

---

## 7. Ví dụ đúng/sai

### Ví dụ ĐÚNG — NFP Friday, sweep SSL rồi displace lên

![[SeekDestroy-Example-Correct.svg|720]]

Mon–Thu chop trong range rõ, weekly bias bullish đã xác nhận trên D1/H4. Đúng 08:30 NY, NFP ra tin. Giá quét SSL (dưới range low) trước — cú Judas cấp tuần — rồi hồi lại vào trong range. Trên 15m, giá đóng trên swing high nội phiên kèm displacement = **MSS/CISD lên**. Trader chờ retest vào FVG vừa hình thành, entry **Long**, stop dưới đáy sweep. Giá đi thẳng tới HTF draw phía trên. `missing_step: none`.

### Ví dụ SAI — vào lệnh trong chop Mon–Thu trước khi tin ra

![[SeekDestroy-Example-Wrong.svg|720]]

Trong lúc Mon–Thu đang chop (đã có đủ 3 dấu hiệu S&D week), trader thấy một cú đẩy nhìn giống breakout giữa range và vào lệnh — **trước khi tin ra**. Ngay sau đó tin thật xuất hiện, giá quét stop của lệnh này (Sweep 1), rồi tiếp tục quét cả phía đối diện (Sweep 2) trước khi mới thật sự đi theo đúng hướng ban đầu trader dự đoán. Đây là ví dụ kinh điển của việc vi phạm cardinal rule — bị "knife" qua cả hai stop chỉ vì vào sớm. `missing_step: pre-news-entry`.

---

## 8. Sequence mẫu

1. Thứ Hai–Thứ Tư: theo dõi range hình thành, KHÔNG trade counter-trend, chỉ đánh dấu high/low.
2. Thứ Năm đóng cửa: chốt xác nhận đủ 3 dấu hiệu S&D week hay không — nếu không đủ, bỏ khung này cho tuần đó.
3. Sáng ngày có tin: không mở lệnh mới, không "scalp cái chop" dù giá trông hấp dẫn.
4. Giờ tin ra: quan sát, không hành động ngay tại nến tin.
5. Sau tin vài phút–vài chục phút: xác định phía đã bị sweep, chờ giá hồi lại vào range.
6. Xuống 5m/15m: chờ MSS/CISD đúng hướng ngược sweep.
7. Entry tại đóng nến xác nhận hoặc retest sạch, stop ngoài điểm cực trị, target HTF draw.
8. Review cuối tuần: ghi `htf_bias`, `sweep_side`, `mss_ltf`, `missing_step` ([[07 - Reviews]]).

---

## Chuyên sâu A — Edge cases & Failure modes (thực chiến Seek and Destroy Friday)

![[SeekDestroy-EdgeCase-Matrix.svg|720]]
> [!info] Mô tả hình
> Ma trận 8 ô edge case, mỗi ô một icon vòng tròn màu riêng: chỉ sweep 1 phía, FOMC giữa tuần, không FVG hồi, tin ra ngoài giờ, weekly bias mù mờ, double sweep 1 phía, NFP trùng OPEX, trùng thứ Sáu Profit-Taking.

Tám tình huống dưới đây là những chỗ giả định "sweep 2 phía rồi đi theo bias" hay gãy nhất trong thực chiến — mỗi ca đọc theo mạch **hiện tượng → cách nhận diện sớm → hành động đúng → bài học**.

**① Chỉ sweep một phía, không có phía đối lập.**
*Hiện tượng:* sau tin, giá chỉ quét một pool (ví dụ SSL) rồi displace luôn, không hề chạm lại phía BSL — hoặc chỉ test nhẹ mà không thật sự sweep. *Cách nhận diện sớm:* theo dõi cả hai mức range high/low ngay sau tin; nếu qua 15–30 phút chỉ một phía bị chạm rõ, nghi ngờ đây không phải S&D "chuẩn" hai phía. *Hành động đúng:* vẫn có thể trade theo sweep đã xảy ra + MSS/CISD xác nhận — chỉ một phía bị sweep không tự động vô hiệu hóa setup, miễn cấu trúc LTF vẫn xác nhận đúng hướng weekly bias. *Bài học:* mô tả "sweep cả hai phía" là mẫu hình lý tưởng, không phải điều kiện bắt buộc tuyệt đối cho mọi entry hợp lệ — MSS/CISD LTF mới là điều kiện cứng.

**② FOMC rơi vào giữa tuần (Thứ Tư) làm lệch khung Mon–Thu.**
*Hiện tượng:* FOMC luôn vào Thứ Tư 14:00 NY, khiến sweep dynamic có thể xảy ra sớm hơn — Mon–Wed mới là "range accumulation", còn Thứ Năm–Sáu diễn biến theo logic khác (có thể tiếp tục trend, hoặc tạo một S&D nhỏ khác quanh NFP nếu tuần đó trùng đầu tháng). *Cách nhận diện sớm:* kiểm tra lịch FOMC TRƯỚC khi mặc định "range luôn là Mon–Thu" — nếu FOMC rơi vào Thứ Tư, range cần đánh dấu là Mon–Tue (hoặc Mon–Wed sáng). *Hành động đúng:* dùng chính khung Mon-đến-ngay-trước-giờ-FOMC làm range, áp cùng logic sweep 2 phía + MSS/CISD, không cứng nhắc chờ tới Thứ Sáu. *Bài học:* "Seek and Destroy Friday" là tên gọi phổ biến nhất, nhưng cơ chế áp được cho BẤT KỲ ngày nào có tin lớn đủ điều kiện — không riêng Thứ Sáu.

**③ Sweep xảy ra nhưng không để lại FVG/breaker sạch để hồi vào.**
*Hiện tượng:* displacement sau sweep đi quá mượt, không tạo khoảng trống rõ nào để làm điểm retest — giá cứ thế chạy thẳng. *Cách nhận diện sớm:* ngay sau MSS/CISD, kiểm tra ngay có FVG/breaker hay không; nếu không, entry retest "đẹp" theo Pro Tip sẽ không tồn tại. *Hành động đúng:* vào tại đóng nến MSS/CISD luôn (không chờ retest hoàn hảo không tồn tại), hoặc chấp nhận bỏ lỡ nếu risk quá cao mà không có điểm entry rõ. *Bài học:* Pro Tip về FVG là ĐIỀU KIỆN TỐT HƠN, không phải điều kiện bắt buộc — thiếu nó thì entry vẫn hợp lệ, chỉ R:R kém hấp dẫn hơn.

**④ Tin ra ngoài giờ kill zone chính, thanh khoản mỏng khi sweep xảy ra.**
*Hiện tượng:* một số CPI/số liệu phụ ra vào giờ khác 08:30 NY chuẩn, hoặc rơi vào giờ thanh khoản liên ngân hàng thấp (ví dụ dữ liệu châu Á/châu Âu ảnh hưởng chéo). *Cách nhận diện sớm:* luôn kiểm tra giờ chính xác của tin trên lịch kinh tế, không giả định mọi tin đều là 08:30 NY. *Hành động đúng:* nếu thanh khoản mỏng bất thường tại giờ tin, nới stop hoặc giảm size — whipsaw dễ xảy ra hơn tin chính giờ NY-AM. *Bài học:* "giờ tin" không phải hằng số — luôn xác nhận cụ thể, đừng suy đoán từ thói quen NFP.

**⑤ Weekly bias mù mờ nhưng vẫn có đủ 2 dấu hiệu còn lại.**
*Hiện tượng:* có tin lớn Thứ Sáu, Mon–Thu chop rõ — nhưng dấu hiệu thứ ba (divergence HTF rõ ↔ LTF chưa theo) không tồn tại vì D1/H4 chính nó cũng đang đi ngang, không có bias nào để "chưa theo". *Cách nhận diện sớm:* kiểm tra kỹ dấu hiệu ③ (không chỉ 2 dấu hiệu đầu) — nếu HTF cũng mù mờ, đây không phải S&D week đủ điều kiện. *Hành động đúng:* không coi đây là S&D week; không có bias nghĩa là không có target, và Bonus Tip trong nguồn gốc đã nói rõ "không target = không trade". *Bài học:* đủ 2/3 dấu hiệu không phải là "gần đủ" — thiếu dấu hiệu bias là thiếu điều kiện quan trọng nhất, không thể bỏ qua.

**⑥ Double sweep cùng một phía trước khi có sweep phía đối diện.**
*Hiện tượng:* giá quét pool SSL, hồi nhẹ, rồi quét thêm một pool SSL khác thấp hơn (chưa hề chạm BSL) trước khi mới thật sự đảo hướng. *Cách nhận diện sớm:* tương tự Chuyên sâu A⑦ của [[10 - Bread and Butter Sell-Setup]] — một pool liquidity đơn lẻ có thể không đủ cho lệnh tổ chức, cần gộp thêm. *Hành động đúng:* không hoảng khi lần sweep đầu không đảo ngay; nếu chưa có MSS/CISD, tiếp tục chờ, dời điểm tham chiếu stop sang lần sweep sau cùng. *Bài học:* "sweep 2 phía" đôi khi thực chất là "sweep 3 lần cùng phía trước, rồi 1 lần phía đối diện" — số lần chạm không quan trọng, MSS/CISD mới là tín hiệu.

**⑦ NFP Friday trùng đúng ngày OPEX (đáo hạn phái sinh).**
*Hiện tượng:* thị trường vừa có NFP buổi sáng vừa có áp lực gamma pinning của OPEX buổi chiều — hai cơ chế chồng lên nhau, làm move sau tin có thể bị "kéo lại" bất thường vào buổi chiều dù sáng đã đi đúng hướng dự kiến. *Cách nhận diện sớm:* kiểm tra lịch phái sinh hàng quý/tháng bên cạnh lịch tin vĩ mô — NFP đầu tháng đôi khi trùng chu kỳ OPEX tháng. *Hành động đúng:* nếu đã vào đúng lệnh theo NFP buổi sáng và đạt target hợp lý, chốt sớm hơn thường lệ; đừng kỳ vọng giá tiếp tục trend sạch cả buổi chiều khi OPEX có thể ghì giá lại. *Bài học:* hai profile cùng ngày không cộng dồn sức mạnh — chúng có thể triệt tiêu nhau ở giai đoạn sau, xem thêm Case 5 của [[05 - Friday Profit Taking]].

**⑧ Trùng lịch với "Friday Profit-Taking" thông thường — hai hiện tượng dễ gây nhầm lẫn.**
*Hiện tượng:* trader mới dễ nhầm "hôm nay là NFP Friday, chắc sẽ giống mọi Friday khác — chờ reversion về weekly open". *Cách nhận diện sớm:* xem ngay bảng phân loại trong [[05 - Friday Profit Taking]] mục Phản biện — Friday NFP và Friday thường có động lực khác hẳn, không nên gộp một tỷ lệ thống kê. *Hành động đúng:* khi có tin lớn rơi vào Thứ Sáu, ưu tiên khung Seek and Destroy (đợi sweep 2 phía + MSS) thay vì khung reversion-về-weekly-open thông thường — hai mô hình cho ra hành động khác nhau, không thể áp cả hai cùng lúc. *Bài học:* luôn xác định "loại Thứ Sáu" nào đang diễn ra TRƯỚC khi chọn khung phân tích — nhầm khung là nguyên nhân phổ biến của các lệnh thua khó hiểu.

> [!note] Nguyên tắc chung khi nghi ngờ
> Khi bất kỳ ô nào ở trên xuất hiện, **hạ kỳ vọng và ưu tiên giữ tiền**. Trước mỗi lệnh, xác nhận lại đúng ba thứ theo thứ tự: **weekly bias rõ → đủ 3 dấu hiệu S&D → sweep + MSS/CISD LTF**. Thiếu một trong ba là đủ để đứng ngoài — một "good skip" luôn tốt hơn một "bad entry" trước tin.

---

## Chuyên sâu B — Kinh nghiệm live/backtest thực chiến

![[SeekDestroy-Experience.svg|720]]
> [!info] Mô tả hình
> 6 ô kinh nghiệm: chờ đủ 3 dấu hiệu, không pre-position, MSS/CISD là trigger không phải wick, target = HTF draw không cố định pip, tách log theo loại tin, false positive rate cao.

Đây là những bài học "trả giá bằng lệnh thật" — thứ mà mô tả lý thuyết Seek and Destroy Friday không nhấn đủ mạnh, nhưng lặp lại đủ nhiều trong live/backtest để trở thành quy tắc.

1. **Cardinal rule "không trade trước tin" là điều duy nhất KHÔNG được thương lượng.** Mọi vi phạm khác trong mô hình này có thể sửa được bằng kỷ luật quản lý lệnh; vi phạm cardinal rule thì không — bạn đã tự đặt mình vào đúng phạm vi bị "seek and destroy".

2. **MSS/CISD là trigger thật; wick sweep chỉ là zone quan tâm.** Rất nhiều lệnh thua đến từ việc vào ngay tại nến sweep vì "sợ lỡ sóng". Không có xác nhận cấu trúc LTF thì cú sweep chỉ là một cú quét đơn thuần, chưa chắc đã đảo hướng.

3. **Target là HTF draw on liquidity, không phải một số pip cố định.** Vì mỗi tuần có một range Mon–Thu khác nhau về độ rộng, gán cứng "20 pips" hay "50 pips" cho mọi Seek and Destroy week là bỏ qua ngữ cảnh; luôn xác định target bằng cấu trúc (đỉnh/đáy đáng kể tiếp theo), không bằng con số tuyệt đối.

4. **Tách log theo loại tin (NFP/FOMC/CPI/khác) trước khi tính bất kỳ tỷ lệ % nào.** Winrate của setup quanh NFP có thể khác đáng kể so với quanh FOMC hoặc CPI — do độ lớn phản ứng thị trường, thời điểm trong tuần, và mức thanh khoản nền khác nhau. Gộp chung sẽ cho một con số không đại diện cho bất kỳ loại tin cụ thể nào.

5. **Tỷ lệ dương tính giả của việc nhận diện S&D week TRƯỚC Thứ Sáu là cao hơn cảm giác chủ quan.** Nhiều tuần có đủ vẻ 2/3 dấu hiệu (có tin + có chop) nhưng thực tế Thứ Sáu không hề sweep sạch hai phía, hoặc chạy thẳng một chiều không hồi — coi nhận diện sớm là một GIẢ THUYẾT, không phải xác nhận, tới khi sweep + MSS/CISD thật sự xảy ra.

6. **Kỳ vọng thực tế về tần suất: mô hình này không xảy ra mỗi tuần.** Chỉ áp dụng được khi có tin lớn đủ điều kiện — trung bình khoảng 1 lần/tháng quanh NFP, cộng thêm các tuần FOMC/CPI khác. Không cố "tìm" Seek and Destroy trong những tuần không có lịch tin phù hợp.

7. **Xung đột tâm lý là rào cản lớn nhất, không phải kỹ thuật đọc chart.** Mô hình yêu cầu bạn đứng ngoài đúng lúc thị trường "trông như" đang có cơ hội rõ ràng nhất (một cú breakout giữa chop trước tin) — với trader có xu hướng muốn hành động, đây là bài kiểm tra kỷ luật khó hơn nhiều so với đọc đúng cấu trúc kỹ thuật.

8. **Demo vs live khác biệt rõ nhất ở khâu "chờ".** Trên demo, đứng ngoài không có cảm giác mất mát cơ hội; trên live, mỗi phút chờ trong lúc giá "trông như" đang chạy tạo áp lực tâm lý muốn nhảy vào — đây là lý do phần lớn vi phạm cardinal rule xảy ra trên tài khoản live/funded, hiếm khi trên demo.

9. **Chuỗi "đứng ngoài đúng" không tạo cảm giác thành tích — dễ bị đánh giá thấp trong journal.** Vì không có P&L để ghi nhận, nhiều trader không log lại các tuần đã đúng khi bỏ qua — điều này làm méo cảm nhận về tần suất thật của "good skip" so với "good trade", nên vẫn cần ghi log cả những tuần chọn không trade.

10. **Cần ≥20–30 mẫu tách riêng theo loại tin trước khi tin vào một con số winrate cụ thể.** Với tần suất thấp (khoảng 1 S&D week hợp lệ/tháng), tích lũy đủ mẫu cho một loại tin cụ thể (chỉ riêng NFP, chẳng hạn) có thể cần 1.5–2 năm dữ liệu — đây là mô hình cần kiên nhẫn dài hơn nhiều so với các mô hình giao dịch hàng ngày khác trong vault.

> [!tip]
> Một câu gói lại: **đủ 3 dấu hiệu → đứng ngoài tới giờ tin → sweep phía đối lập bias → hồi vào range → MSS/CISD LTF → entry retest → target HTF draw; giá trị lớn nhất của mô hình là nói KHÔNG trước tin, không phải một kỹ thuật entry phức tạp.**

---

## Chuyên sâu C — Case studies mổ xẻ chuyên sâu (kịch bản minh họa)

> [!info] Đọc đúng tinh thần 4 ca dưới đây
> Cả bốn ca đều là **kịch bản tái dựng từ pattern lặp lại trong backtest, số liệu minh họa (hypothetical)**, KHÔNG phải lệnh thật và không dùng số liệu giá thật gắn ngày cụ thể. Mục đích là luyện phản xạ đọc bối cảnh: **chấm điểm bằng process (đúng quy trình hay không), không bằng P&L** của từng ca.

### Case 1 — WIN: FOMC Wednesday sweep, đúng chuẩn CISD

![[SeekDestroy-Advanced-CaseStudy-Win.svg|720]]

**Bối cảnh HTF:** D1 + H4 xác nhận weekly bias bearish rõ từ đầu tuần, nhưng daily action Mon–Tue chỉ đi ngang trong một range hẹp — đúng dấu hiệu divergence HTF↔LTF.

**Diễn biến theo mốc giờ:** Thứ Ba, giá tiếp tục chop trong range đã đánh dấu. 14:00 NY Thứ Tư, FOMC ra quyết định lãi suất. Ngay sau đó giá quét BSL (đỉnh range) — cú Judas cấp tuần đúng hướng ngược bias — rồi hồi lại vào trong range. Trên 5m, giá đóng dưới swing low nội phiên kèm displacement rõ = CISD xuống.

**Quyết định & lý do:** Entry Short tại retest vùng vừa hình thành sau CISD, vì đủ cả ba điều kiện: weekly bias bearish, sweep BSL đúng phía dự kiến, CISD LTF xác nhận đồng hướng bias. Stop đặt ngay trên đỉnh của cú sweep.

**Kết quả (R):** Giá đi thẳng về HTF discount array kế tiếp, chốt tại **+1.8R**.

**Mổ xẻ lỗi/điểm đúng:** Không có lỗi — chuỗi điều kiện được tuân thủ đầy đủ theo đúng thứ tự: profile xác nhận trước, đứng ngoài tới giờ tin, chờ sweep, chờ CISD, mới entry.

**Bài học thành rule:** Khi FOMC rơi vào giữa tuần, coi Mon-đến-ngay-trước-14:00-Thứ-Tư là "range Mon–Thu" tương đương — cơ chế sweep 2 phía áp dụng nguyên vẹn, chỉ khung thời gian dịch sớm hơn (edge case ②).

### Case 2 — LOSS: Entry tại nến sweep, không chờ CISD (NFP Friday)

![[SeekDestroy-Advanced-CaseStudy-Loss.svg|720]]

**Bối cảnh HTF:** Weekly bias bullish rõ, Mon–Thu chop hợp lệ, đủ 3 dấu hiệu S&D week xác nhận từ Thứ Năm.

**Diễn biến theo mốc giờ:** 08:30 NY Thứ Sáu, NFP ra tin. Giá quét SSL (đáy range) đúng hướng dự kiến (sweep phía ngược bias trước). Ngay tại nến sweep, trader vào Long **vì sợ lỡ sóng** — chưa hề chờ MSS/CISD 5m/15m xác nhận.

**Quyết định & lý do (gãy):** Quyết định vào lệnh dựa trên "giá đã chạm đúng vùng dự đoán", bỏ qua bước bắt buộc là chờ xác nhận cấu trúc sau sweep.

**Kết quả (R):** Giá tiếp tục quét thêm về hướng cũ trước khi mới thật sự đảo, quét stop của lệnh **trước khi** đi đúng hướng ban đầu trader đã dự đoán đúng — thua khoảng **-1R**.

**Mổ xẻ lỗi/điểm đúng:** Bias đúng, phía sweep dự đoán đúng — nhưng **thời điểm entry sai**. Đây là lỗi "chạm đúng vùng ≠ entry" tương tự lỗi trong Bread and Butter Sell ([[10 - Bread and Butter Sell-Setup]] Chuyên sâu A③), chỉ khác cấp độ khung thời gian (tuần thay vì phiên). `missing_step: mss_confirmation`.

**Bài học thành rule:** Dù bias và phía sweep đã đúng, KHÔNG entry tại chính nến sweep — luôn chờ MSS/CISD LTF đóng nến xác nhận trước khi vào, kể cả khi cảm giác "chắc chắn đã đúng hướng".

### Case 3 — No-Trade đúng: chỉ sweep một phía, weekly bias mù mờ

![[SeekDestroy-Advanced-CaseStudy-NoTrade.svg|720]]

**Bối cảnh HTF:** D1/H4 đi ngang không rõ hướng suốt từ đầu tuần — không có bias nào để nói "chưa được honor". Mon–Thu vẫn chop trong range, và có tin CPI rơi vào Thứ Sáu 08:30 NY.

**Diễn biến theo mốc giờ:** Sau tin, giá quét BSL (đỉnh range) một lần, hồi nhẹ lại, nhưng sau đó tiếp tục loay hoay trong chính range cũ — không hề có MSS/CISD rõ ràng theo bất kỳ hướng nào.

**Quyết định & lý do:** Trader nhận ra ngay từ đầu tuần rằng dấu hiệu thứ ba (divergence HTF↔LTF) không tồn tại vì bản thân HTF cũng mù mờ — nên coi đây KHÔNG phải Seek and Destroy week đủ điều kiện ngay từ đầu, và không kỳ vọng bất kỳ entry nào dù có tin và có sweep một phía.

**Kết quả (R):** Không vào lệnh — 0R, đúng theo kế hoạch.

**Mổ xẻ lỗi/điểm đúng:** Không sai — đây là skip đúng theo Bonus Tip của nguồn gốc: "không có target rõ (vì không có bias rõ) thì không có lý do trade". `missing_step: none`.

**Bài học thành rule:** Luôn kiểm tra ĐỦ BA dấu hiệu, không chỉ hai đầu (lịch tin + chop) — thiếu dấu hiệu weekly bias rõ là thiếu điều kiện quan trọng nhất, và một cú sweep một phía không kèm bias rõ không đủ để cấu thành setup.

### Case 4 — WIN: NFP trùng OPEX, chốt sớm hơn thường lệ khi thấy dấu hiệu ghì giá

**Bối cảnh HTF:** Weekly bias bearish rõ từ D1/H4. Mon–Thu chop hợp lệ, đủ 3 dấu hiệu S&D week — và trader còn kiểm tra thêm lịch phái sinh, phát hiện Thứ Sáu đó cũng là ngày OPEX tháng (edge case ⑦).

**Diễn biến theo mốc giờ:** 08:30 NY, NFP ra tin gây bất ngờ so với kỳ vọng. Giá quét BSL (đỉnh range) trước, hồi lại vào range, rồi 15m MSS xuống xác nhận. Trader vào Short tại retest, stop trên đỉnh sweep. Lệnh chạy thuận lợi tới giữa buổi sáng, đạt gần **+2R**. Sang đầu giờ chiều, biết trước có áp lực OPEX gamma-pinning tiềm năng, trader chủ động chốt phần lớn vị thế thay vì chờ target HTF xa hơn.

**Quyết định & lý do:** Chốt sớm hơn kế hoạch gốc, dựa trên edge case ⑦ (NFP trùng OPEX) — nhận định rằng buổi chiều có khả năng bị ghì giá, làm move tiếp tục kém hiệu quả hơn buổi sáng.

**Kết quả (R):** Chốt tại **+1.9R** giữa trưa; giá buổi chiều đúng như dự đoán đi ngang hẹp, không mở rộng thêm về target HTF xa ban đầu.

**Mổ xẻ lỗi/điểm đúng:** Không có lỗi — đây là ví dụ chủ động điều chỉnh kỳ vọng khi nhận ra hai profile (Seek and Destroy + OPEX pin) chồng lên nhau, tương tự Case 5 của [[05 - Friday Profit Taking]].

**Bài học thành rule:** Khi NFP Friday trùng lịch OPEX, hạ kỳ vọng cho phần di chuyển buổi chiều và ưu tiên chốt lời theo diễn biến buổi sáng — đừng áp target HTF "tiêu chuẩn" như một tuần NFP thông thường không có OPEX.

> [!summary] Bốn ca — một thông điệp
> Cardinal rule (không trade trước tin) chỉ là điều kiện cần đầu tiên; thứ quyết định thắng/thua thật sự nằm ở việc có chờ đủ **MSS/CISD LTF** sau sweep hay không (Case 1 vs Case 2), có xác nhận đủ **cả ba dấu hiệu** trước khi coi đây là S&D week hay không (Case 3), và có nhận ra khi hai profile chồng lấp cần điều chỉnh kỳ vọng hay không (Case 4). Ghi `htf_bias`, `sweep_side`, `mss_ltf`, `calendar_exception`, `missing_step` mỗi tuần có tin lớn ([[07 - Reviews]]) để biến bốn kịch bản này thành phản xạ.

---

## Phản biện & Giới hạn của mô hình

> [!warning] Đọc trước khi tin tuyệt đối vào Seek and Destroy Friday
> Phần này không phủ nhận giá trị của mô hình — nó tồn tại để bạn dùng Seek and Destroy Friday đúng với bản chất: một **khung tư duy về tần suất thấp, giá trị chính nằm ở việc đứng ngoài**, không phải một cỗ máy tạo tín hiệu entry đáng tin cậy cao.

### 1. Đây là profile "trung tính/xác suất thấp" — điều này thường bị đánh giá thấp

Chính nguồn gốc mô tả mô hình này là **"neutral to low-probability profile"** — khác hẳn các mô hình khác trong vault (ICT 2022 Model, Bread and Butter…) vốn được trình bày với một chuỗi bước dẫn tới entry rõ ràng. Ở đây, phần lớn "giá trị" thực chất là một quy tắc phủ định: **đừng trade**. Nhiều trader mới tiếp cận mô hình này với kỳ vọng sai — coi nó như một setup entry tần suất cao khác — và thất vọng khi nhận ra phần lớn thời gian áp dụng đúng mô hình là… không làm gì cả.

**Mâu thuẫn tâm lý cố hữu:** hầu hết trader tìm đến các mô hình ICT vì muốn hành động, muốn có setup, muốn vào lệnh. Seek and Destroy Friday yêu cầu điều ngược lại đúng vào lúc trực giác thị trường "hấp dẫn nhất" (một cú đẩy giữa chop trước tin trông như breakout). Đây không phải một giới hạn kỹ thuật của mô hình mà là **giới hạn tâm lý của người áp dụng nó** — và là lý do phần lớn thất bại với mô hình này đến từ vi phạm cardinal rule, không đến từ đọc sai cấu trúc.

### 2. Tỷ lệ dương tính giả khi nhận diện S&D week trước Thứ Sáu

![[SeekDestroy-FalsePositive-Diagram.svg|720]]

Ba dấu hiệu ở mục 5A giúp nhận diện SỚM (trước khi tin ra), nhưng đây là một **dự đoán có điều kiện, không phải xác nhận**. Trên thực tế:

- Nhiều tuần "trông giống" S&D week (đủ 2/3, hoặc thậm chí đủ cả 3 dấu hiệu bề mặt) nhưng khi tin thật ra, giá chỉ sweep một phía rồi chạy thẳng không hồi lại range — không hề có "cú sweep thứ hai" hay MSS/CISD rõ theo đúng mẫu hình.
- Ngược lại, cũng có những tuần không có đủ 3 dấu hiệu rõ ràng trước Thứ Sáu nhưng vẫn diễn ra đúng mẫu S&D vào phiên tin — nhận diện sớm không phải điều kiện cần tuyệt đối để mô hình xảy ra, nó chỉ tăng xác suất bạn CHỦ ĐỘNG chuẩn bị đúng.
- Việc coi 3 dấu hiệu là "xác nhận chắc chắn" rồi lơ là kiểm tra lại vào chính Thứ Sáu là một lỗi phổ biến — luôn xác nhận LẠI bằng sweep + MSS/CISD thật diễn ra, không dừng ở bước dự đoán.

**Hệ quả thực hành:** giữ hai trạng thái tư duy tách biệt — "tôi nghĩ đây có thể là S&D week" (giả thuyết, dựa vào 3 dấu hiệu) và "đây LÀ S&D week, tôi có setup" (xác nhận, dựa vào sweep 2 phía + MSS/CISD LTF thật). Chỉ trạng thái thứ hai mới cho phép hành động.

### 3. Rủi ro thống kê khi backtest Seek and Destroy Friday

- **Hindsight bias đặc biệt nghiêm trọng với mô hình này:** vì tần suất thấp (~1 lần/tháng), khi nhìn lại một tháng backtest, mắt bạn dễ tự động "thấy" mẫu hình sweep-2-phía ở hầu hết các tuần có tin — trong khi thực tế nhiều tuần đó chỉ trend thẳng hoặc sweep một phía yếu. Chỉ đánh giá bar-by-bar mới cho số liệu đáng tin.
- **Degrees of freedom trong việc chọn "range Mon–Thu":** với những tuần có swing bất thường (higher-highs kèm lower-lows), việc chọn chính xác đâu là "range high/low hợp lệ" có nhiều lựa chọn chủ quan — dễ chọn ngược từ kết quả đã biết (chọn mức khớp đẹp với cú sweep đã xảy ra) thay vì chọn trước khi biết kết quả.
- **Cỡ mẫu rất nhỏ theo bản chất mô hình:** với tần suất ~1 S&D week hợp lệ/tháng, một năm backtest chỉ cho ≈10–14 mẫu — quá ít để tách riêng theo loại tin (NFP vs FOMC vs CPI) và rút ra kết luận có ý nghĩa thống kê cho từng nhóm. Cần nhiều năm dữ liệu mới đạt ngưỡng mẫu đáng tin.
- **Survivorship của case chia sẻ công khai:** các ví dụ "Seek and Destroy thành công" lưu hành trên mạng gần như luôn là các tuần sweep đẹp cả hai phía — không ai chia sẻ các tuần "tưởng là S&D" nhưng thực ra chỉ trend thẳng hoặc sweep lệch, khiến người mới đánh giá quá cao tần suất mẫu hình xảy ra đúng chuẩn.

### 4. Điều kiện thị trường làm mô hình gãy

- **Tin ra nhưng thị trường đã "price-in" trước:** nếu số liệu không gây bất ngờ (khớp kỳ vọng thị trường), phản ứng giá có thể rất yếu — không đủ lực tạo displacement rõ để hình thành MSS/CISD, dù range Mon–Thu vẫn tồn tại đúng mẫu.
- **Nhiều sự kiện lớn chồng chéo trong cùng ngày** (ví dụ NFP + phát biểu ngân hàng trung ương cùng buổi sáng): phản ứng giá có thể phức tạp hơn một cú sweep hai phía đơn giản — nhiều đợt sweep chồng lấp khó phân biệt đâu là "sweep chính".
- **Thị trường đang trong một trend vĩ mô rất mạnh (ví dụ giai đoạn khủng hoảng, thắt chặt tiền tệ liên tục):** tin lớn có thể chỉ củng cố thêm trend đang có, khiến giá không cần "coil" trước — chạy thẳng luôn theo hướng trend mà không hình thành range Mon–Thu rõ để sweep.
- **Thanh khoản mỏng bất thường quanh kỳ nghỉ lễ trùng tuần có tin:** làm biến dạng cả pha coil (range méo) và pha sweep (whipsaw mạnh hơn dự kiến, có thể quét qua cả entry và stop hợp lệ).

### 5. Phản biện điểm-theo-điểm với các tuyên bố cụ thể của mô hình

- **"Smart Money engineering liquidity có chủ đích":** đây là một **narrative** diễn giải hành vi giá, không phải cơ chế đã được xác nhận công khai bởi bất kỳ tổ chức nào. Một cách giải thích thay thế hợp lý không kém: trước tin lớn, nhiều participant tổ chức ĐỘC LẬP đều giảm rủi ro/đóng vị thế theo cùng logic phòng ngừa rủi ro tin tức — hành vi tập thể này tự nhiên tạo ra consolidation, và phản ứng mạnh hai chiều sau tin chỉ là hệ quả của thanh khoản dồn nén được giải phóng đồng loạt, không cần giả định một "ý đồ" thống nhất.
- **"Phía bị sweep trước luôn là phía ngược weekly bias":** đây là mẫu hình phổ biến NHẤT, nhưng không phải quy luật tuyệt đối — thị trường vẫn có thể sweep đúng phía cùng hướng bias trước (do phản ứng tin phức tạp hơn một chiều), khiến việc "đoán trước phía sweep" chỉ nên là một kỳ vọng có xác suất cao hơn ngẫu nhiên, không phải điều chắc chắn để đặt lệnh chờ (pending order) trước tin.
- **"Đây luôn là Power of 3 nén 1 tuần":** khung Power of 3 là một cách ĐỌC LẠI sau khi biết kết quả rất thuyết phục, nhưng không phải mọi Seek and Destroy week đều tuân theo đúng 3 giai đoạn tách bạch — đôi khi accumulation và distribution chồng lấp, hoặc manipulation kéo dài qua nhiều giờ thay vì một cú sweep gọn.

### 6. Cách tự kiểm định khách quan

1. **Pre-registration quy tắc "3 dấu hiệu":** viết cố định trước (không sửa sau khi biết kết quả) ngưỡng cụ thể cho "chop bất thường" và "divergence HTF-LTF" — tránh co giãn định nghĩa để khớp với tuần đã biết kết quả.
2. **Log riêng cả "dự đoán đúng nhưng không trade được"** (ví dụ: dự đoán đúng S&D week nhưng sweep không để lại MSS/CISD rõ) — phân biệt "dự đoán sai" và "dự đoán đúng nhưng không đủ điều kiện entry" là hai loại lỗi khác nhau, cần sửa khác nhau.
3. **Forward test theo từng loại tin riêng biệt** (NFP riêng, FOMC riêng) trước khi gộp chung kết luận về "mô hình Seek and Destroy" nói chung.
4. **Đếm cả các tuần bị bỏ qua đúng (no-trade) như Case 3** — nếu số tuần "đứng ngoài đúng" áp đảo số tuần "vào lệnh", đó là dấu hiệu khỏe của một mô hình tần suất thấp, không phải bằng chứng mô hình vô dụng.
5. **Walk-forward theo năm** (không theo quý, vì mẫu quá ít) — với tần suất ~10–14 mẫu/năm, cần tối thiểu 2–3 năm dữ liệu mới có đủ cơ sở walk-forward có ý nghĩa.

> [!tip] Một câu gói lại phần này
> Seek and Destroy Friday là mô hình mà **giá trị lớn nhất nằm ở kỷ luật KHÔNG hành động**, không phải ở độ phức tạp của bước entry — nếu bạn thấy mình liên tục "tìm cách" để có một lệnh trong tuần có tin lớn, đó là dấu hiệu đang hiểu sai tinh thần của chính mô hình này.

---

## Best Practices

> [!summary]
> Thói quen ở mức chuyên nghiệp khi áp dụng Seek and Destroy Friday — thứ phân biệt trader dùng mô hình này như một bộ lọc kỷ luật, với trader chỉ biết lý thuyết nhưng vẫn tự ép mình có lệnh mỗi tuần có tin.

### Quy trình pre-week — xác nhận hoặc loại trừ profile TRƯỚC khi tuần diễn ra

- Đầu mỗi tuần (Chủ Nhật tối hoặc sáng Thứ Hai), kiểm tra lịch kinh tế: có tin high-impact nào rơi vào cuối tuần hoặc giữa tuần không.
- Nếu có, đặt "cờ nghi ngờ S&D week" ngay từ đầu tuần và theo dõi 3 dấu hiệu chủ động — không chờ tới Thứ Năm mới bắt đầu quan sát.
- Đánh dấu sẵn range high/low ngay khi range bắt đầu rõ hình dạng (thường từ giữa Thứ Ba), cập nhật liên tục tới trước giờ tin.
- Viết sẵn kịch bản Long và Short trước giờ tin — kể cả kịch bản bạn cho là ít khả năng hơn — để không phải phân tích trong áp lực thời gian thực ngay sau khi tin ra.

### Kỷ luật "không hành động" cần được luyện tập như một kỹ năng riêng

- Coi mỗi lần đứng ngoài đúng theo cardinal rule là một "thắng lợi kỷ luật" đáng ghi log, không phải một khoảng trống không có gì để ghi.
- Nếu cảm thấy áp lực muốn vào lệnh giữa chop trước tin, đó chính là tín hiệu đang ở đúng giữa một Seek and Destroy week — coi cảm giác đó như một xác nhận thêm, không phải lý do để hành động.

### Amateur habits vs. Professional habits với Seek and Destroy Friday

| Khía cạnh | Amateur (nghiệp dư) | Professional (chuyên nghiệp) |
|---|---|---|
| Trước tin | Vào lệnh vì "trông như breakout" giữa chop | Đứng ngoài tuyệt đối, chỉ quan sát và đánh dấu range |
| Sau sweep | Vào ngay tại nến sweep vì sợ lỡ sóng | Chờ MSS/CISD LTF đóng nến xác nhận |
| Target | Đặt số pip cố định | Xác định bằng HTF draw on liquidity thực tế |
| Nhận diện S&D week | Coi 3 dấu hiệu là xác nhận chắc chắn | Coi 3 dấu hiệu là giả thuyết, xác nhận lại bằng sweep + MSS thật |
| Weekly bias mù mờ | Vẫn cố tìm setup vì "có tin lớn" | Bỏ hoàn toàn, không coi đây là S&D week |
| Review | Chỉ nhớ các lệnh đã vào | Ghi cả những tuần đứng ngoài đúng, không chỉ P&L |
| Tần suất | Cố ép có lệnh mỗi tuần có tin | Chấp nhận nhiều tuần không có entry hợp lệ |

> [!tip]
> Nếu phải tóm gọn Best Practices thành một câu: **"Chuẩn bị range trước, xác nhận bằng sweep + MSS/CISD thật, và coi việc không hành động trước tin là một kỹ năng — không phải một khoảng trống."**

---

## Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì có tin lớn trong tuần
> Phải đủ chuỗi: tin lớn + chop Mon–Thu + weekly bias rõ + sweep 2 phía (hoặc ít nhất 1 phía rõ) + MSS/CISD LTF. Một tin lớn đơn lẻ KHÔNG phải là Seek and Destroy Friday.

### A. Context (trước Thứ Sáu / trước giờ tin)
- [ ] Có tin high-impact xác định trên lịch kinh tế.
- [ ] Mon–Thu (hoặc Mon-đến-trước-giờ-tin) đi ngang/chop hoặc swing bất thường.
- [ ] Weekly bias HTF (D1/H4) rõ, đang chưa được daily action honor (divergence).
- [ ] Range high (BSL) và range low (SSL) đã đánh dấu rõ.

### B. Execution (sau tin)
- [ ] Không vào lệnh nào trước giờ tin (cardinal rule).
- [ ] Đã xác định phía nào bị sweep trước (đúng dự kiến: ngược weekly bias).
- [ ] Giá đã hồi trở lại vào trong range sau sweep.
- [ ] Có MSS/CISD trên 5m/15m đồng hướng weekly bias.
- [ ] Entry tại đóng nến xác nhận hoặc retest sạch, không chase.
- [ ] Stop ngoài điểm cực trị bị sweep; target là HTF draw rõ.

### C. Quy tắc "không có lệnh"
- [ ] Weekly bias không rõ → không trade.
- [ ] Không đủ 3 dấu hiệu S&D week → không áp mô hình này.
- [ ] Chưa có MSS/CISD sau sweep → chưa vào, tiếp tục chờ.
- [ ] Chỉ có thể vào bằng cách chase ngay tại nến sweep → không trade.
- [ ] Range Mon–Thu không tồn tại rõ (giá đã trend thẳng từ đầu tuần) → không áp mô hình.

---

## Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade trước tin | Vào lệnh giữa chop vì "trông như breakout" | Vi phạm cardinal rule, dễ bị knife 2 phía | Đứng ngoài tuyệt đối tới giờ tin |
| Entry tại nến sweep | Vào ngay khi thấy wick quét pool | Chưa có xác nhận cấu trúc, dễ bị stop trước move thật | Chờ MSS/CISD LTF đóng nến |
| Coi 3 dấu hiệu là xác nhận | Không kiểm tra lại vào chính Thứ Sáu | Tỷ lệ dương tính giả cao (xem Phản biện) | Giữ ở trạng thái giả thuyết, xác nhận lại bằng sweep thật |
| Gán target pip cố định | Đặt TP theo số pip có sẵn từ mô hình khác | Bỏ qua độ rộng range thực tế của tuần đó | Target = HTF draw on liquidity theo cấu trúc |
| Áp dụng khi bias mù mờ | Vẫn cố tìm setup vì "có tin lớn" | Không có target rõ = không có lý do trade | Bỏ hoàn toàn nếu HTF không rõ hướng |
| Nhầm với Friday Profit-Taking | Áp khung reversion-về-weekly-open cho tuần có tin lớn | Hai mô hình cho hành động khác nhau, dễ nhầm | Xác định loại Thứ Sáu trước khi chọn khung ([[05 - Friday Profit Taking]]) |
| Gộp chung log mọi loại tin | Tính một tỷ lệ thắng chung cho NFP+FOMC+CPI | Con số không đại diện cho bất kỳ loại tin nào | Tách log theo loại tin trước khi kết luận |

---

## Câu hỏi tự kiểm tra

- Mình đã xác nhận đủ 3 dấu hiệu S&D week trước Thứ Năm đóng cửa chưa, hay đang chỉ đoán?
- Weekly bias HTF của mình rõ chưa — nếu không, mình có target nào để trade không?
- Mình có đang định vào lệnh TRƯỚC giờ tin không? Nếu có, dừng lại ngay.
- Phía nào đã bị sweep — có đúng là phía ngược weekly bias không?
- Giá đã hồi lại vào trong range sau sweep chưa, hay vẫn đang chạy thẳng?
- Đã có MSS/CISD LTF thật sự đóng nến xác nhận chưa, hay mình mới thấy một wick?
- Target của mình là một HTF draw cụ thể, hay một số pip mình tự đặt theo cảm giác?
- Nếu không trade, lý do "No Trade" của mình rơi vào điều kiện nào ở Checklist phần C?

---

## Flashcards

### Q1
**Hỏi:** Seek and Destroy Friday là gì, định nghĩa ngắn gọn?
**Đáp:** Weekly profile trong đó giá chop Mon–Thu trước một tin lớn (NFP/FOMC/CPI), rồi Thứ Sáu (hoặc ngày có tin) sweep cả hai phía của range đó trước khi displace theo đúng hướng weekly order flow.

### Q2
**Hỏi:** Cardinal rule của mô hình là gì?
**Đáp:** Không trade trước khi tin ra, không có ngoại lệ.

### Q3
**Hỏi:** Ba dấu hiệu nhận diện S&D week trước Thứ Sáu là gì?
**Đáp:** (1) Có tin high-impact đánh dấu Thứ Sáu, (2) Mon–Thu đi ngang/swing bất thường, (3) weekly bias HTF rõ nhưng daily action chưa honor (divergence).

### Q4
**Hỏi:** Phía nào bị sweep trước trong một tuần weekly bias bullish?
**Đáp:** SSL (sell-side liquidity, dưới range low) — phía ngược với hướng thật, trước khi displace lên.

### Q5
**Hỏi:** Trigger entry chính xác sau sweep là gì?
**Đáp:** MSS (Market Structure Shift) hoặc CISD (Change in State of Delivery) trên khung 5m/15m, đồng hướng weekly bias — không entry ngay tại nến sweep.

### Q6
**Hỏi:** Target của mô hình được xác định như thế nào?
**Đáp:** HTF draw on liquidity kế tiếp (đỉnh/đáy đáng kể gần nhất, đỉnh/đáy tuần trước, hoặc target order flow daily/weekly) — không phải một số pip cố định.

### Q7
**Hỏi:** Vì sao mô hình được gọi là "trung tính/xác suất thấp"?
**Đáp:** Vì phần lớn giá trị thực hành nằm ở việc đứng ngoài (không hành động) trong đa số thời gian, chỉ hành động khi đủ điều kiện xác nhận rất hẹp — không phải một setup entry tần suất cao.

### Q8
**Hỏi:** Điểm khác biệt cốt lõi giữa Seek and Destroy Friday và Friday Profit-Taking?
**Đáp:** Seek and Destroy Friday xảy ra khi có tin lớn và dựa trên sweep 2 phía + MSS/CISD; Friday Profit-Taking là hiện tượng reversion-về-weekly-open của thứ Sáu THÔNG THƯỜNG (không tin lớn) — hai cơ chế khác nhau, không nên áp cùng khung ([[05 - Friday Profit Taking]]).

---

## Schema logging & backtest — biến mỗi lệnh thành dữ liệu

> [!important] Vì sao mục này tồn tại
> Vì Seek and Destroy Friday có tần suất thấp (~1 lần/tháng), mỗi mẫu dữ liệu quý hơn nhiều so với các mô hình giao dịch hằng ngày trong vault — ghi thiếu hoặc ghi sai một trường có thể làm chậm việc tích lũy đủ mẫu thêm nhiều tháng.

### Frontmatter tối thiểu cho một lệnh/quan sát Seek and Destroy

```yaml
type: backtest              # hoặc trade (live)
symbol: EURUSD               # EURUSD | GBPUSD | NAS100 | XAUUSD | DXY
setup: Seek and Destroy Friday
news_type: NFP                # NFP | FOMC | CPI | other
news_time_ny: "08:30"
htf_bias: Bearish             # Bullish | Bearish | Unclear
sign1_news_calendar: Yes      # dấu hiệu 1: tin lớn xác định trên lịch
sign2_chop_monthu: Yes        # dấu hiệu 2: Mon-Thu chop/irregular
sign3_divergence: Yes         # dấu hiệu 3: HTF rõ nhưng LTF chưa honor
confirmed_sd_week: Yes        # xác nhận thật (sau khi thấy sweep) hay chỉ dự đoán ban đầu
sweep_side_first: BSL         # BSL | SSL — phía bị sweep trước
swept_back_into_range: Yes
mss_cisd_ltf: Yes             # có MSS/CISD LTF xác nhận không
mss_timeframe: 15m            # 5m | 15m
entry_type: retest            # retest | mss-close | none
calendar_exception: none      # OPEX | FOMC-midweek | none | other
position: Short
result: Win                   # Win | Loss | BE | NoTrade
r_multiple: 1.8
risk_percent: 0.5
missing_step: none            # pre-news-entry | mss_confirmation | bias_unclear | none
followed_plan: Yes
```

> [!warning] Ba luật ghi dữ liệu để số liệu không bị "bẩn"
> 1. **Không fabricate.** Trường nào không đủ căn cứ quan sát thật thì để trống — trống tốt hơn đoán sai.
> 2. **`missing_step` là bắt buộc ở MỌI lệnh thua/BE, và ở MỌI lần vi phạm cardinal rule dù kết quả cuối là gì.** Vi phạm "pre-news-entry" cần được ghi lại kể cả khi lệnh đó tình cờ thắng — thắng nhờ vi phạm quy trình không phải bằng chứng quy trình đó ổn.
> 3. **Ghi cả các tuần `result: NoTrade`.** Đây là dữ liệu quan trọng nhất của mô hình này — không ghi lại các lần đứng ngoài đúng sẽ làm mất khả năng đánh giá tần suất "good skip" thật của bạn.

### Weekly/Monthly Review đọc schema này thế nào

1. Cuối mỗi tháng (vì tần suất thấp, review theo tháng hợp lý hơn theo tuần), lọc toàn bộ quan sát có `sign1/2/3` đều Yes, so với số quan sát có `confirmed_sd_week: Yes` — tỷ lệ này chính là **tỷ lệ dương tính giả thật của bạn** trên chính thị trường đang trade.
2. Tách `result` và `r_multiple` theo `news_type` (NFP riêng, FOMC riêng) — không gộp chung.
3. Đếm tần suất `missing_step: pre-news-entry` theo thời gian — nếu không giảm dần sau vài tháng, đây là dấu hiệu kỷ luật cardinal rule chưa cải thiện, ưu tiên sửa số 1.
4. Tổng hợp `calendar_exception` riêng để dần xây một bảng ngoại lệ cá nhân hóa (giống mục Phản biện & Giới hạn ở [[05 - Friday Profit Taking]]).

> [!tip] Con số mục tiêu để dữ liệu "biết nói"
> Vì tần suất thấp, cần **≥1.5–2 năm dữ liệu** để tích lũy 20–30 mẫu cho riêng một loại tin (ví dụ chỉ NFP) — đừng vội kết luận từ 3–5 lần quan sát đầu tiên, dù cảm giác "đã đủ hiểu mô hình".


---

## Lesson Learned

### Bài học chính
- Seek and Destroy Friday là **một profile trung tính/xác suất thấp** — giá trị chính nằm ở việc đứng ngoài đúng lúc, không phải một chuỗi entry tần suất cao.
- **Cardinal rule (không trade trước tin)** là điều kiện duy nhất tuyệt đối không thương lượng trong toàn bộ mô hình.
- **MSS/CISD LTF sau sweep** là trigger thật; cú sweep chỉ là zone quan tâm, không phải lý do để vào lệnh.
- Ba dấu hiệu nhận diện sớm là **giả thuyết**, không phải xác nhận — luôn xác nhận lại bằng sweep + MSS/CISD thật diễn ra.
- Target luôn là **HTF draw on liquidity theo cấu trúc**, không phải một số pip cố định copy từ mô hình khác.

### Quy tắc cá nhân rút ra
- [ ] Tôi không bao giờ vào lệnh trước giờ tin, dù giá "trông như" đang breakout.
- [ ] Tôi luôn chờ MSS/CISD LTF đóng nến trước khi entry, không vào tại nến sweep.
- [ ] Tôi coi 3 dấu hiệu nhận diện sớm là giả thuyết, xác nhận lại bằng sweep thật.
- [ ] Tôi ghi log cả những tuần đứng ngoài đúng, không chỉ các lệnh đã vào.
- [ ] Tôi tách thống kê theo loại tin (NFP/FOMC/CPI) trước khi kết luận bất kỳ tỷ lệ % nào.

### Câu nhắc nhở khi trade
> **"Chop → Tin → Sweep → Hồi → MSS/CISD → Vào → HTF draw. Trước tin, tôi không tồn tại trên chart."**

---

## Liên kết chéo

- [[05 - Friday Profit Taking]] — phân biệt rõ Thứ Sáu "thường" (reversion) với Thứ Sáu "Seek and Destroy" (sweep 2 phía do tin lớn); xem Case 5 của bài đó cho tình huống NFP/OPEX chồng lấp.
- [[01 - ICT 2022 Model]] — chuỗi Bias → Liquidity → Sweep → Displacement/MSS → FVG → Entry → Target là khung gốc mà Seek and Destroy Friday áp dụng ở cấp độ tuần.
- [[10 - Bread and Butter Sell-Setup]] / [[11 - Bread and Butter Buy-Setup]] — cùng chung logic "premium/discount sweep rồi MSS xác nhận", nhưng ở cấp độ phiên trong ngày thay vì cấp độ tuần.
- [[12 - Consolidation Trading Strategy]] — tư duy đọc range tích lũy trước một cú breakout có liên hệ trực tiếp tới cách đọc range Mon–Thu trong mô hình này.

---

## Nguồn

- [ICT Seek and Destroy Friday: Profile, Setup & How to Trade It](https://innercircletrader.net/tutorials/ict-seek-and-destroy-friday/) — nguồn gốc chính, Inner Circle Trader / Ayub Rana.
