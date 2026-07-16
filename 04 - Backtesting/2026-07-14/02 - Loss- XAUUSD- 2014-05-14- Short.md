---
type: backtest
backtest_date: 2026-07-14
trade_date: 2014-05-14
symbol:
  - XAUUSD
position: Short
result:
  - Loss
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct:
  - Yes
poi_type: "[[28 - Rejection Block|Rejection Block]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1301.482
stop_loss: 1302.715
take_profit: 1297.51
r_planned: 3.22
r_multiple: -1
grade: B-
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2014-05-14 — XAUUSD Short

> [!info] Mục đích backtest
> Vừa mới học lý thuyết Rejection Block, backtest này apply Rejection Block vào vị trí POI (thay cho FVG/OB hay dùng) trong chuỗi ICT 2022 Model

---

## 0. Backtest Summary

| Field                | Value            |
| -------------------- | ---------------- |
| Symbol               | XAUUSD           |
| Trade Date (dữ liệu) | 2014-05-14 16:17 |
| Position             | Short            |
| Result               | Loss             |
| Session              | London           |
| Setup                | ICT 2022 Model   |
| Entry Model          | ICT 2022 Model   |
| Entry Timeframe      | M1               |
| HTF Bias             | Bearish          |
| Bias Correct?        | Yes              |
| Entry                | 1301.482         |
| Stop Loss            | 1302.715         |
| Take Profit          | 1297.51          |
| R Planned            | 3.22             |
| R Multiple (kết quả) | -1               |
| Grade                | B-               |

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
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: 
	  - D1 Dealing Range High: 1392.098
	  - Bearish Order Block: 1387.437
  - Sell-side liquidity:
	  - Dealing Range Low: 1182.661
	  - Old lows tạo ra trong nhịp giá tăng tạo Long Term High
	  - Order Block
	  - H1 Dealing Range Low

![[Pasted image 20260714063937.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- Sau Long Term High, giá hình thành Bearish MSS + Displacement (đồng bias với D1)
	- LH/LL, order flow đang giảm
- **Dealing Range (nhịp retrace cho setup Short)**: 
	- High: 1315.691 (swing high — fib 1.0)
	- Low: 1277.416 (swing low — fib 0.0)
	- Giá đang retrace lên vùng **Premium / OTE** cho setup Short
- **POI chính**: 
	- Bearish Rejection Block: 1304.109 - 1302.715
	- Order Block: 1308.146 - 1304.82
- **Liquidity cần chờ sweep**:
  - Buy-side: các internal high của consolidation + cạnh trên H1 FVG (gần CE của liquidity void)
  - Sau sweep → draw về Sell-side / OB phía dưới

### Phân Tích: 
- Phân tích context trước:
	- Sau khi quét SSL ngày 2/5/2014 19:00, giá tạo displacement và bắt đầu nhịp tăng với HH/HL và tạo thành 1 đỉnh ngày 5/5/2014 lúc 19:00
	- Sau khi tạo đỉnh giá bắt đầu đi ngang (consolidation)
	- Tới ngày 7/5/2014 14:00, giá hình thành các nến Bearish Displacement mạnh phá xuống đồng thời tạo thành các FVG trên đường giá
	- Tới ngày 8/5/2014 lúc 00:00 giá bắt đầu chững lại và đi ngang (Consolidation)
	- Sau đó tới ngày 12/5/2014 lúc 17:00 giá có 1 nến Bearish Displacement quét xuống các đáy cũ (của consolidation range) và đóng bên ngoài consilidation range, sau đó là các nến xanh đóng quay ngược trở lại
	- Đáy của nến quét thanh khoản đó hình thành H1 Dealing Range Low
	- Sau nhịp quét đó giá đang trong vùng Discount, tuy nhiên Bias lúc đó đang là Bearish -> Chờ giá retrace về vùng Premium
- Phân Tích lệnh:
	- Ngày 12/5/2014 lúc 19:00 giá tạo 1 cây nến displacement mạnh phá qua vùng cân bằng (50%) của Dealing Range và trờ lại vùng Premium
	- Cú displacement này tạo đỉnh với 1 râu nến dài. Do vừa học lý thuyết Rejection Block nên tôi muốn thử áp dụng vào mô hình ICT 2022
	- Tôi đánh dấu râu nến dài phía trên đĩnh là Rejection Block và chờ giá retrace về
	- Ngày 14/5/2014 lúc 15:00 giá retrace về tới cạnh dưới RB với 2 nến Bullish Displacement mạnh
	- Râu nến của nến sau chạm đúng vùng CE của Rejection Block và bật ra bằng 1 nến Bearish
	- Xuống khung M5/M1 quan sát phản ứng

![[Pasted image 20260714111634.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Sau khi giá chạm CE của Rejection Block, giá bật ra với 1 nến Bearish khung H1 -> Tiếp tục quan sát phản ứng giá dưới khung thấp hơn M1/M5
	- Khung M5 giá tạo các cây nến Bearish liên tiếp có 1 nến thân lớn. Tuy nhiên các bóng nến của các cây nến khung M5 overlap với nhau, không tạo FVG
	- Tôi xuống khung M1 quan sát giá
	- Tại khung M1 giá tạo MSS phá qua swing low (swing tạo đỉnh quét CE của RB) và nến displacement có tạo 1 FVG tại nhịp phá swing low
	- FVG tại: 1301.676 - 1301.225
	- Tôi Entry khi quá retrace về vùng CE của FVG khung H1 này 1301.485
	- Stop loss đặt trên swing high (cây nến quét chạm CE của RB)
	- Take Profit đặt dưới Swing low của gần nhất khung M5 (internal, tôi định take partial tại đây) - tỉ lệ RR: 1:3.22
- **Entry trigger**:
	  - Liquidity Sweep: 
		  - Quét CE của RB
		  - Giá phá qua swing low (low tạo đỉnh chạm tới CE RB)
		  - Giá tạo FVG từ nhịp MSS đó
		  - Giá retrace về CE FVG
	  - MSS: Giá tạo MSS bằng các cây nến Bearish displacement lúc 16:03
	  - Displacement: có displacement lúc 16:03 -> tạo FVG
- **Entry reason**:
	  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là Rejection Block H1)
	  - RB nằm trong OTE (0.618 - 0.705 - sweet spot)
- **Invalidation reason**:
	  - Giá đóng qua Rejection Block H1
- **Tôi có chờ đủ điều kiện không?** Có

**M5:**
![[Pasted image 20260714121553.png]]

**M1:**

![[Pasted image 20260714121625.png]]
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

- **Result**: Hit Stop loss

- **Tại sao lệnh thua? (root cause thật)**
	- **Root cause đơn nhất: Stop Loss đặt SAI vị trí — nằm ngay cạnh gần (proximal edge) của POI, tức là *bên trong* vùng phản ứng còn hợp lệ của Rejection Block, chứ không phải trên điểm invalidation thật.**
	- Kiểm chứng bằng số học:
		- Rejection Block H1: 1302.715 (low) → 1304.109 (high), CE = **1303.412**
		- Invalidation thật của RB (theo chính ghi chú Entry của tôi): *"Giá đóng qua Rejection Block H1"* → tức là đóng nến **trên 1304.109**
		- Entry (CE của M1 FVG): **1301.485** — nằm **dưới** RB low, quanh mức fib **0.618 (1301.070)**
		- SL: **1302.715** = **đúng RB low = mép dưới POI** ≈ fib 0.618–0.705
		- TP: 1297.51 → Risk 1.230 / Reward 3.975 = **R 3.23**
	- Vấn đề: giá chỉ cần retrace từ 0.618 ngược lên chạm lại **đáy RB (0.705)** là quét SL. Nhưng một cú wick trở lại mép dưới RB là hành vi **hoàn toàn bình thường** bên trong OTE/POI — nó **KHÔNG** phá invalidation (chưa hề đóng nến trên 1304.109). Nói cách khác, tôi đã đặt SL vào giữa vùng "chop" mà chính tôi kỳ vọng giá sẽ còn dao động.
	- Mâu thuẫn logic cốt lõi: tôi **định nghĩa invalidation theo H1** (đóng trên RB) nhưng lại **đặt SL theo một swing high nhỏ khung M1** (1302.715). Hai logic khác cấp độ bị trộn vào nhau → SL không bảo vệ được luận điểm H1.

- **Thị trường có cho tín hiệu cảnh báo trước không?** Có, ít nhất 2 cảnh báo rõ:
	1. **M5 không tạo được FVG** — tôi tự ghi *"các bóng nến khung M5 overlap với nhau, không tạo FVG"*. Đây là dấu hiệu phản ứng bán **KHÔNG sạch / không có displacement thực**. Đáng lẽ đây là tín hiệu *đứng ngoài chờ*, không phải tín hiệu *tụt xuống M1 để tìm setup*.
	2. **2 nến Bullish Displacement mạnh đẩy giá vào POI** (14/5 lúc 15:00). Order flow ngắn hạn phía mua đang **rất mạnh** khi chạm vùng short. Bán ngược một dòng displacement tăng mạnh trên khung thấp = rủi ro cao bị đẩy xuyên qua một SL chật.

- **Setup này khớp bao nhiêu % với mô hình chuẩn?** ~**75–80%**.
	- Khớp tốt (context): HTF bias Bearish đúng; đã có sweep SSL; giá retrace về Premium/OTE; chuỗi Sweep → MSS + Displacement + FVG → retrace có tồn tại; TP về đúng draw on liquidity phía dưới.
	- Lệch chuẩn (execution): (a) **SL không đặt trên invalidation thật** của POI — đây là điểm sai nặng nhất, làm hỏng cả setup dù bias đúng; (b) entry rơi xuống tận M1 sau khi M5 đã báo phản ứng yếu (thiếu confirmation sạch); (c) vào lệnh khi displacement tăng đối nghịch còn chưa bị hấp thụ.

- **Nếu được vào lại, tôi sẽ làm gì khác?**
	1. **Neo SL vào invalidation của POI đang giao dịch (RB H1)**, tức trên **1304.109 + buffer** (vd ~1304.4). Chấp nhận R thấp hơn: reward 3.975 / risk ~2.9 = **~1.35R**. Nếu R đó không đủ hấp dẫn → **đó là tín hiệu vùng entry chưa tối ưu, nên bỏ lệnh, không phải lý do siết SL cho đẹp R:R**.
	2. **Nếu muốn giữ SL chật kiểu M1**, thì phải chờ M1 MSS hình thành **SAU khi giá đã thực sự rời khỏi POI** và tạo cấu trúc giảm sạch, không phải trong lúc bulls vẫn đang đẩy vào vùng.
	3. **Coi "M5 không có FVG" là điều kiện loại (no-trade)**: nếu khung xác nhận trung gian không sạch thì không tụt sâu hơn để "moi" tín hiệu.
	4. **Xác minh trong Replay: sau khi quét SL, giá có đi xuống chạm TP 1297.51 không?** Nếu CÓ → xác nhận đây thuần là lỗi SL quá chật (đúng hướng, sai vị trí dừng lỗ), là lỗi execution sửa được. Nếu giá tiếp tục đi lên phá RB → luận điểm short bị vào **quá sớm** và cần xét lại cả timing chứ không chỉ SL.


---

## 5. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Bias đúng, phân tích top-down tốt — nhưng thua vì **SL đặt ngay mép dưới POI (RB low) thay vì trên invalidation thật**, nên một cú retrace bình thường trong OTE đã quét stop trước khi luận điểm short kịp chạy.

> [!warning] Ghi chú của mentor
> Đừng để **R:R đẹp (3.22)** đánh lừa: con số đó là *sản phẩm phụ* của một SL quá chật đặt sai chỗ, không phải bằng chứng setup chất lượng A. Grade A- đang **quá hào phóng** cho một lệnh có SL nằm trong vùng chop. Một lệnh "R:R thấp nhưng SL đúng invalidation" tốt hơn nhiều một lệnh "R:R cao nhưng SL trong POI". Cân nhắc hạ grade xuống **B/B-**.

### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc chất lượng lệnh) — chỉ có MỘT:**
Stop Loss được neo vào một **swing high nhỏ khung M1 (1302.715 = RB low)** — tức mép gần của POI — thay vì trên **invalidation thật của Rejection Block H1 (đóng trên 1304.109)**. SL nằm *bên trong* vùng phản ứng còn hợp lệ, nên bị quét bởi nhiễu bình thường chứ không phải bởi một tín hiệu phủ định luận điểm.

**Triệu chứng tích cực sinh ra từ root cause đó (dễ nhầm là "đúng"):**
- **R:R 3.22 trông rất hấp dẫn** và khiến lệnh được chấm grade A- — nhưng chính SL chật là thứ tạo ra R:R đó và cũng chính là thứ giết lệnh.
- **Entry giá rất đẹp ở 0.618** (deep discount-of-premium) — cảm giác "mua/bán được giá tốt", nhưng entry sâu dưới POI cộng với SL ở mép POI = stop rơi vào đúng giữa no-man's-land.
- **M1 MSS + FVG trông như một entry trigger ICT 2022 chuẩn** — nhưng trên M1, giữa lúc bulls đang displacement mạnh vào vùng, nó chỉ là một nhịp pullback nhiễu bị nhầm thành structure shift thực.

**Cơ chế thị trường đã diễn ra (hiểu để lặp lại được):**
Giá wick lên chạm **CE của RB (~1303.4)**, phản ứng giảm nhẹ tạo M1 FVG quanh 0.618. Nhưng vùng RB **chưa hoàn tất nhiệm vụ** — đáy RB (0.705) vẫn là thanh khoản/vùng giá dễ được test lại. Giá retrace ngược lên chạm lại mép dưới RB (hành vi bình thường của một POI đang được "mài"), quét SL đặt ở đó, rồi (cần xác minh trong replay) mới thực sự đi theo hướng bias. Đây là kịch bản kinh điển **"stopped out on noise inside the POI"**.

**Điểm kỹ thuật CẦN xác minh thêm (đừng vội cho là đã đúng):**
- Sau khi quét SL, giá có xuống TP 1297.51 không? (quyết định đây là lỗi SL hay lỗi timing — xem mục 4).
- **Định nghĩa Rejection Block của tôi đã chuẩn chưa?** RB đúng nghĩa được vẽ từ *thân* các nến có bóng dài từ chối; cần xác minh 1304.109–1302.715 là vùng thân-đến-bóng đúng, và CE dùng để canh entry/SL có nhất quán không.
- Kill Zone: entry ~16:03 (UTC+7). Cần xác minh mốc này còn nằm trong London KZ hay đã trôi ra ngoài — nếu ngoài KZ thì đây là một điểm trừ chất lượng nữa.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)
- **Siết SL để làm đẹp R:R** — ép SL vào mép POI thay vì trên invalidation thật. Đây là pattern nguy hiểm nhất; liên kết tới [[Mistake - Stop loss đặt sai vị trí]] (tạo note nếu chưa có).
- **Tụt khung để "moi" setup** khi khung xác nhận (M5) đã báo phản ứng yếu/không có FVG, thay vì đứng ngoài.
- **Vào lệnh ngược displacement đối nghịch còn mạnh** — bán khi 2 nến bullish displacement vừa đẩy vào vùng.

### 5.3. Rule cần thêm/cập nhật vào Playbook
1. **Rule SL theo POI:** SL luôn neo trên invalidation của POI *đang giao dịch* (RB/OB) + buffer, KHÔNG neo vào swing nhỏ khung entry. Nếu entry sâu (LTF) làm khoảng cách tới invalidation lớn → tính lại R theo SL đúng; **R do SL đúng quyết định có vào hay không, không phải ngược lại**.
2. **Rule confirmation:** Nếu khung trung gian (M5) không tạo displacement/FVG sạch → **no-trade**, không tụt xuống M1 để tìm tín hiệu.
3. **Rule momentum đối nghịch:** Không short khi displacement tăng vào POI còn chưa bị hấp thụ; chờ nến bearish displacement sạch phá cấu trúc rồi mới tìm entry retrace.
4. **Rule grading:** Bất kỳ lệnh nào có SL nằm *trong* POI đều bị chặn trần grade ở mức B, bất kể R:R.

