---
type: backtest
backtest_date: 2026-07-14
trade_date: 2014-05-14
symbol:
  - XAUUSD
position: Short
result:
  - Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct:
  - Yes
poi_type: "[[03 - Balanced Price Range|Balance Price Range]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1306.9
stop_loss: 1308.39
take_profit: 1302.477
r_planned: 2.97
r_multiple: 2.97
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2014-05-14 — XAUUSD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên XAUUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → BPR entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | XAUUSD         |
| Trade Date (dữ liệu) | 2014-05-14     |
| Position             | Short          |
| Result               | Win            |
| Session              | New York       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M1             |
| HTF Bias             | Bearish        |
| Bias Correct?        | Yes            |
| Entry                | 1306.90        |
| Stop Loss            | 1308.39        |
| Take Profit          | 1302.477       |
| R Planned            | 2.97           |
| R Multiple (kết quả) | 2.97           |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
	  - Phía bên trái giá đã quét hết các lower high trong nhịp tăng sau đó sau đó tạo 1 đỉnh ( Long Term High)
	  - Trước nhịp tăng 31/12/2013, hình thành 1 cú quét thanh khoản, quét đáy trước sau đó đóng nên lại trong range và tăng (1)
	  - Nhịp tăng đồng thời tạo Displacement + Order Block (2)
	  - Tiếp sau đó là nhịp tăng Bullish với các HH/HL -> Thanh khoản tích tụ dần ở các đáy này
	  - Sau nhịp tạo đỉnh ( long term high) giá hình thành 1 Bearish MSS với nhịp displacement + FVG (3)
	  - Trong Dealing Range lớn giá đang trong vùng Premium (4)
	  - (1) + (2) + (3) + (4) => Bias Bearish
	  - Giá đang trong vùng Premium, thanh khoản Buy Side đã bị lấy, mục tiêu kế tiếp là Sell Side Liquidity và vùng Order Block
	  - Giá đang trong nhịp đi ngang, tuy nhiên phía dưới vẫn còn nhiều Sell Side Liquidity
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: 
	  - D1 Dealing Range High: 1392.098
	  - Bearish Order Block: 1387.437
  - Sell-side liquidity:
	  - Dealing Range Low: 1182.661
	  - Old lows tạo ra trong nhịp giá tăng tạo Long Term High
	  - Order Block
	  - H1 Dealing Range Low

![[Pasted image 20260714125908.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- Sau Long Term High, giá hình thành Bearish MSS + Displacement (đồng bias với D1)
	- LH/LL, order flow đang giảm
- **Dealing Range (nhịp retrace cho setup Short)**: 
	- High: 1315.691 (swing high — fib 1.0)
	- Low: 1277.416 (swing low — fib 0.0)
	- Giá đang retrace lên vùng **Premium / OTE** cho setup Short
- **POI chính**: 
	- Bearish OB vùng ~0.786 (≈ 1308 – 1310)
	- Bearish FVG H1 (từ nhịp giảm 7/5) nằm trong vùng OTE
- **Liquidity cần chờ sweep**:
  - Buy-side: Đỉnh tạo ở nhịp tăng trước đó ngày 12/05/2014 lúc 19:00
  - Vùng FVG (nằm trong Liquidity void): 

### Phân Tích: 
- Phân tích context trước:
	- Sau khi quét SSL ngày 2/5/2014 19:00, giá tạo displacement và bắt đầu nhịp tăng với HH/HL và tạo thành 1 đỉnh ngày 5/5/2014 lúc 19:00
	- Sau khi tạo đỉnh giá bắt đầu đi ngang (consolidation)
	- Tới ngày 7/5/2014 14:00, giá hình thành các nến Bearish Displacement mạnh phá xuống đồng thời tạo thành các FVG trên đường giá
	- Tới ngày 8/5/2014 lúc 00:00 giá bắt đầu chững lại và đi ngang (Consolidation)
	- Sau đó tới ngày 12/5/2014 lúc 17:00 giá có 1 nến Bearish Displacement quét xuống các đáy cũ (của consolidation range) và đóng bên ngoài consilidation range, sau đó là các nến xanh đóng quay ngược trở lại
	- Đáy của nến quét thanh khoản đó hình thành H1 Dealing Range Low
	- Hiện tại giá đang trong vùng Premium
- Phân Tích lệnh:
	- Ngày 12/5/2014 lúc 19:00 giá tạo 1 cây nến displacement mạnh phá qua vùng cân bằng (50%) của Dealing Range và trờ lại vùng Premium
	- Giá retrace về vùng FVG (FVG của Liquidity void hình thành ngày 7/5/2014)
	- Giá quét lên trên và qua cạnh trên của FVG để lại râu nến dài. Sau đó giá đóng nến lại quay vào trong FVG và xuất hiện nến Bearish  displacement mạnh
	- Vào M5 quan sát

![[Pasted image 20260714125755.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Nhịp Bullis Displacement ngày 14/05/2014 lúc 19:20 phá qua đỉnh FVG khung H1 đồng thời để lại 1 FVG khung M5 từ cú displacement đó
	- Sau đó giá đóng nến quay ngước lại bên trong FVG H1, để lại bóng nến dài lên trên, các nến sau cũng có bóng nến quét lên cạnh trên FVG ( 2 - 3 nến tiếp theo)
	- Sau 2 - 3 nên tiếp theo, giá tạo 1 nến Bearish displacement mạnh, đồng thời để lại 1 FVG khung M5
	- FVG nhịp displacecment tăng trước đó và FVG nhịp displacement giảm này overlap với nhau và hình thành 1 vùng Balance Price Range (BPR) từ 1307.322 - 1306.483 -> Đây có thể là vùng tìm entry khung M5
	- Sau khi giảm giá retrace về BPR lúc 14/05/2014 lúc 20:35. Sau đó giá quét lên cạnh trên của BPR và đóng nến vào bên trong để lại râu nến dài và quay trờ lại vùng CE
	- Tôi entry tại vùng CE của BPR M5 này
	- Stoploss đặt ngoài cạnh trên FVG khung H1
- **Entry trigger**:
	  - Liquidity Sweep: 
		  - Quét cạnh trên FVG
		  - Giá quét 1 Swing High lớn trước khi về FVG
		  - Trong nọi bộ khung M1/M5 cũng có quét thanh khoản các đáy nội bộ tạo ra khi giá hình thành MSS
	  - MSS: Giá tạo MSS bằng các cây nến Bearish displacement lúc 20:00
	  - Displacement: có displacement lúc 19:20 (Bullish) và 20:00 (Bearish)
	  - 2 FVG trùng lắp tạo thành 1 Bearish BPR khung M5
- **Entry reason**:
	  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là FVG H1)
	  - FVG nằm trong vùng giữa 0.705 - 0.786 ( giữa sweet spot và cạnh trên)
	  - Khung M5 tạo 1 BPR, confluence mạnh hơn FVG
- **Invalidation reason**:
	  - Giá đóng qua FVG H1
- **Tôi có chờ đủ điều kiện không?** Có

**M5:**
![[Pasted image 20260714125628.png]]

**M1:**
![[Pasted image 20260714125516.png]]

---

## 2. ICT 2022 Model — Entry Sequence

Đánh dấu theo đúng thứ tự checklist của mô hình:

- [x] **1. Liquidity Sweep** — giá quét thanh khoản (Equal H/L, swing, Asia range...)
  - Loại: Internal / External / Equal Highs / Equal Lows
- [x] **2. Displacement** — nến đẩy mạnh, tạo FVG, phá cấu trúc nội bộ
- [x] **3. Market Structure Shift (MSS)** — phá swing point ngược hướng sweep
- [x] **4. FVG / OB hợp lệ** hình thành trong displacement leg
- [x] **5. Entry** — limit trong FVG/OB (CE - Consequent Encroachment) trong Kill Zone
- [x] **6. Stop Loss** — phía trên/dưới điểm sweep (invalidation)
- [x] **7. Take Profit** — opposing liquidity / PD array kế tiếp

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ
- [x] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [x] Entry trong POI hợp lệ, không đua giá
- [x] SL ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng/thua?**
	  - Kiên nhẫn chờ H1 đồng Bias với khung D1 (Bearish)
	  - Chờ M5, M1 confirm Bias
	  - H1 retrace về vùng Premium / OTE
	  - Giá có quét thanh khoản trên FVG
	  - Khung M5 có BPR, confluence mạnh. BPR khung M5 nằm ngay trên CE của H1 FVG
	
- **Thị trường có cho tín hiệu cảnh báo trước không?**
	  - Có Displacement
	  - Có MSS
	  - Có BPR khung M5 cho entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90% 
- **Nếu được vào lại, tôi sẽ làm gì khác?**
	  - Cần backtest nhiều hơn để biết cách vàng (XAUUSD) phản ứng tại các vùng giá, đặc điểm di chuyển (hay có những pha di chuyển mạnh bất chợt hay không)
	  - Đây chỉ mới là lệnh trade vàng thứ 3 nên chưa thật sự hiểu đặc tính của vàng vì tôi thường trade Nasdaq, EURUSD
	  - Ghi lại **chính xác điều gì là sweep**: thanh khoản thật bị quét là **swing high phía trên FVG**, không phải "cạnh trên FVG". Sửa lại mô tả entry trigger cho đúng khái niệm.
	  - Kiểm tra lại **buffer SL cho vàng**: SL sát ngay ngoài cạnh trên H1 FVG có nguy cơ bị wick quét trong môi trường live (spread/slippage vàng lớn). Backtest thêm để định lượng.

> [!check] Toàn vẹn dữ liệu — ĐÃ SỬA (2026-07-14)
> Note tạo bằng cách copy 1 lệnh cũ nên 3 trường số liệu bị sót/sai; đã đối chiếu chart M1 và sửa lại:
> 1. **Summary table (mục 0)**: Entry 1301.562 → **1306.90**, SL 1304.113 → **1308.39**, TP 1294.173 → **1302.477**, R 2.9 → **2.97**.
> 2. **Frontmatter `stop_loss`**: 1308.9 → **1308.39**; `r_planned`/`r_multiple` 2.9 → **2.97** (chart hiển thị Stop 1308.38, R/R 2.97). Lưu ý: SL 1308.9 cũ sẽ cho R chỉ ≈ 2.21.
> 3. **`trade_date`**: 2014-05-12 → **2014-05-14** (12/05 là ngày context tạo H1 Dealing Range Low; entry thật lúc ~20:35 giờ VN = ~09:35 ET, NY AM Kill Zone).
>
> Quy trình phòng ngừa: xem Rule toàn vẹn dữ liệu ở mục 5.3.

---

## 5. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Lệnh Grade A chất lượng thật nhờ **nested confluence** đúng bias (D1 Bearish → H1 Premium/OTE → H1 FVG là POI chính → M5 BPR tại CE làm điểm entry) — điểm cần siết lại là **độ chính xác thuật ngữ "sweep"** và **tính toàn vẹn dữ liệu** đã log.

### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc chất lượng lệnh) — chỉ có MỘT:**

Kiên nhẫn chờ giá về đúng **POI có nhiều lớp confluence chồng nhau (nested POI)** rồi mới entry, thay vì vào ngay ở lớp đầu tiên. Cụ thể: bias D1 Bearish → đợi H1 retrace lên vùng **Premium/OTE (0.705–0.786)** → xác định POI chính là **H1 FVG** → xuống M5 chờ **BPR** (overlap của 2 FVG ngược chiều) trùng ngay trên **CE của H1 FVG** → entry tại CE của BPR. Toàn bộ chất lượng lệnh đến từ việc *không entry sớm* và để confluence tự xếp chồng.

**Triệu chứng tích cực sinh ra từ root cause đó:**

- Chờ H1 đồng bias với D1 trước, không "đoán đỉnh" khi giá còn đi ngang.
- Chờ giá quét **một swing high thật** (buy-side liquidity) trước khi giảm — không vào khi chưa có sweep.
- Entry tại **CE** của POI, không đua giá ở cạnh ngoài.
- SL đặt ở vùng invalidation logic (trên đỉnh sweep / ngoài cạnh trên H1 FVG), không phải SL "cho có".
- RR ≈ 2.97, vượt ngưỡng tối thiểu 1:2 → rủi ro bất đối xứng đúng chất ICT 2022.

**Cơ chế thị trường đã diễn ra (hiểu để lặp lại được):**

Đây là chuỗi ICT 2022 kinh điển: **Sweep buy-side (quét swing high trong Premium) → Displacement giảm tạo MSS + FVG → giá retrace về FVG/BPR trong vùng Premium → tiếp diễn xuống draw on liquidity (SSL/FVG dưới)**. Stops của phe mua bị quét ở đỉnh cung cấp thanh khoản để "smart money" bán; sau displacement, FVG để lại là dấu vết mất cân bằng, và giá quay lại lấp một phần (retrace về CE) trước khi đi tiếp về mục tiêu SSL. BPR M5 mạnh hơn một FVG đơn vì nó là vùng hai FVG ngược chiều overlap → giá đã "reject" hai lần ở cùng vùng.

**Điểm kỹ thuật CẦN xác minh thêm (đừng vội cho là đã đúng):**

- ⚠️ **"Quét cạnh trên FVG" KHÔNG phải là một liquidity sweep.** Cạnh của FVG không phải là vùng thanh khoản (không có stop nằm ở đó). Thanh khoản thật bị quét là **swing high phía trên**. Cần tách bạch: *sweep = quét swing high*; việc râu nến vượt cạnh FVG rồi đóng lại chỉ là **rejection / return to FVG**, là tín hiệu xác nhận chứ không phải sweep. Ghi sai khái niệm này lặp lại nhiều lần sẽ làm hỏng thống kê "sweep → win rate".
- ⚠️ **Đặc tính XAUUSD với SL sát.** Đây mới là lệnh vàng thứ 3. Vàng thường có râu nến/spike bất chợt; SL đặt sát ngay ngoài cạnh trên H1 FVG có thể bị một wick quét ra trong môi trường live (spread + slippage của vàng lớn hơn NAS/EU). Cần thêm sample để biết buffer SL hợp lý cho vàng.
- ✅ **Số liệu đã hiệu chỉnh về đúng chart:** R = **2.97** (không phải 2.9), SL = **1308.39** (không phải 1308.9). Đây là mẫu **R ≈ 2.97**. Chi tiết sai lệch ban đầu xem callout ở mục 4.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- ✅ **Green pattern (tìm để lặp lại):** entry ở giao điểm **H1 FVG (POI chính) + M5 BPR tại CE** trong vùng Premium/OTE, sau một cú sweep swing high. Đây là mẫu confluence chồng đáng săn lùng — đánh dấu để so sánh win rate với các mẫu POI đơn lẻ.
- ⚠️ **Watch pattern (rủi ro quy trình):** thiếu chính xác về (a) thuật ngữ "sweep", và (b) số liệu nhập vào log. Với mục tiêu xây một mẫu backtest **thống kê có giá trị**, sai số dữ liệu = "garbage in, garbage out" — pattern này nếu lặp lại sẽ âm thầm phá giá trị của toàn bộ dataset.

### 5.3. Rule cần thêm/cập nhật vào Playbook

- **Rule thuật ngữ:** chỉ đánh dấu `liquidity_swept: Yes` khi giá quét một **swing high/low thật** (resting liquidity). Việc râu nến vượt cạnh FVG/OB rồi đóng lại ghi là "return to POI + rejection", KHÔNG tính là sweep.
- **Rule tách POI:** khi POI chính (H1 FVG) và POI confluence (M5 BPR) khác timeframe, ghi rõ tách biệt trong note — POI chính quyết định invalidation, POI confluence quyết định entry trigger.
- **Rule XAUUSD:** cần tối thiểu ~20 sample vàng trước khi tin vào logic SL sát; tạm thời cộng thêm buffer cho wick/spread khi backtest vàng và ghi lại xem có bị quét SL "oan" không.
- **Rule toàn vẹn dữ liệu (bắt buộc):** mỗi backtest, copy entry/SL/TP/R **trực tiếp từ chart**, và kiểm tra **Summary table (mục 0) = frontmatter** trước khi lưu. Xem [[Mistake - Sai lệch dữ liệu nhật ký]] (nếu đã có) hoặc tạo mới.
