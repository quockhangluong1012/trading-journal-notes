---
type: backtest
backtest_date: 2026-07-10
trade_date: 2021-05-03
symbol:
  - EURUSD
position: Short
result:
  - Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct:
  - Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.2065
stop_loss: 1.20764
take_profit: 1.20408
r_planned: 3.075
r_multiple: 3.075
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2021-05-03 — EURUSD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2021-05-03     |
| Position             | Short          |
| Result               | Win            |
| Session              | New York       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bearish        |
| Bias Correct?        | Yes            |
| Entry                | 1.20650         |
| Stop Loss            | 1.20764        |
| Take Profit          | 1.20408, 1.20191|
| R Planned            | 3.075          |
| R Multiple (kết quả) | 3.075          |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 đang trong trend giảm
  - Hình thành các LH/LL
  - Sau đó có 1 nhịp Pullback lớn, tuy nhiên chưa phá được protected high -> chưa đổi bias, chỉ là pullback 
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: 
	  - Dealing Range High = 1.23473 ( xa giá hiện tại)
	  - EQH = 1.21751 (gần giá hơn) có khả năng quét EQH hày trước khi đi xuống tiếp. EQH này nằm trong vùng Premium
  - Sell-side liquidity: Giá đang hướng tới vùng
	  - Swing low: 1.17149 (Swing low quan trọng)
	  - Bullish Order Block: 1.16576 - 1.16197
	  - EQL dưới OB: 1.16045

![[Pasted image 20260710092400.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- LH/LL
- **Dealing Range**: 
	- High: 1.21058
	- Low 1.19436
- **POI chính**: 
	- Breaker Block: 1.20750 - 1.20616 (Hình thành thừ Order block ngày 24/04/2021 và bị invalidate ngày 30/04/2021 với 1 nến displacement mạnh - thân nến rất lớn đóng qua Order block và quét luôn các old lows bên dưới tới 1.20142)
	- Nhịp displacement mạnh tạo ra 1 FVG rất lớn (1.20688 - 1.20430)
	- Quan trọng FVG trùng lắp 1 phần với Breaker Block hình thành vùng Unicorn: 1.20680 - 1.20616 -> Đã có POI quan trọng confluence
- **Liquidity cần chờ sweep**:
	  - Vùng unicorn
	  - Lắp FVG
	  - Kỳ vọng phản ứng sau khi quét qua unicorn (quan sát thường thấy giá quét qua ngoài vùng unicorn để trader vào lệnh sớm đặt stoploss ngoài vùng vị quét)
	  
### Phân Tích:
	- Ngày 24/04-2021 giá tạo 1 Order Block (1.20750 - 1.20616), sau đó 1 nhịp đẩy giá mạnh với displacement kèm FVG
	- Sau nhịp đẩy giá tạo Swing High (đĩnh của range)
	- Sau đó giá bắt đầu các nhịp giảm
	- Ngày 30/04/2021, Giá tạo các nến displacement thân lớn quét qua Order Block và các Old Lows
	- Nhịp displacement phá OB đó hình thành Break Block đồng thời kèm 1 FVG lớn (do nến displacement thân lớn, vùng không chồng lắp lớn)
	- Đồng thời FVG overlap với Breaker Block hình thành vùng Unicorn (1.20680 - 1.20616)
	- Vùng Unicorn nằm trong Premium -> đã có Premium/Discount confulence
	- Giá consolidation sau nhịp displacement mạnh (khả năng là phân phối giá)
	- Sau nhịp đi ngang tới ngày 3 tháng 5 2021, giá bắt đầu retrace về vùng Unicorn với các nến lớn
	- Khi giá quay về vùng Unicorn tôi quan sát chú không vào liền tại vùng CE (quá khứ tôi đã từng vào lệnh vội tại vùng CE khi thấy giá retrace về vùng POI quan trọng)
	- Đúng như kỳ vọng, giá quét lên cạnh trên vùng Unicorn 1 đoạn (đóng nến tăng) 
	- chỗ này có 2 khả năng: 
		- 1 là giá đã đóng bên ngoài, nến nến sau tăng tiếp giá giữ bên ngoài thì Unicorn bị invalidate -> bỏ Setup
		- 2 là giá quét sâu để quét stoploss các trader FOMO vào lệnh sớm khi giá chạm Unicorn hoặc CE (như tôi lần trước)
	- Sau khi giá đóng nến bên ngoài thì xuất hiện nến reject mạnh quay lại trong vùng Unicorn và đóng bên dưới vùng
	- Sau đó giá retrace về đúng vùng CE
	- Xuống khung M5 quan sát giá phản ứng tại 

![[Pasted image 20260710092549.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Nhịp giá đóng nến mạnh khung H1 quay lại vùng Unicorn tạo thành 2 FVG trên khung M5. 1 FVG nằm đúng ngay vùng CE 
- CE của FVG (gần giá khung M5) trùng với CE Unicorn -> chú ý quan sát
- Chờ giá retrace về FVG
- Giá quay về FVG nhịp 1 và bật ra mạnh -> Tôi entry nhịp này
- MSS Đã có trong nhịp giá giảm mạnh từ đỉnh (giá quay lại sau khi đóng nến ngoài Unicorn)
- Stoploss đặt bên trên điểm sweep (1.20763)
- **Entry trigger**:
  - Liquidity Sweep: 
	  - Quét qua vùng Unicorn để bẫy những trader vào sớm
	  - Quét qua FVG/CE của FVG tạo thành từ nhịp displacement quay lại vùng
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - Tâm lý khi vào lệnh lúc đó còn hơi sợ khi giá quét lên FVG thêm 2 nhịp (vẫn nằm trong vùng Unicorn)
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là Unicorn H1)
- **Invalidation reason**:
  - Giá đóng qua cạnh trên BPR và giữ bên trên
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260710092729.png]]

- Zoom M5

![[Pasted image 20260710092800.png]]


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

- **Result**: 
	- Hit TP
	- Điểm cải thiện: 
		- Partial Take Profit khi giá quét xuống 1 Short term Low H1 (take 50% khi đạt 2.1R). Sau đó giá quét thêm 1 đoạn xuống 1 đáy cũ nữa ( trelative EQL TP2 thêm 2R)
- **Tại sao lệnh thắng/thua?**
	  - Kiên nhẫn chờ setup hình thành, đúng context, đúng vị trí Premium/Discount
	  - Lệnh này tôi không vội vào tại CE khi giá về vùng POI
	  - POI có các confluence mạnh (Unicorn)
	  - Tôi chờ các điều kiện đầy đủ trước khi entry: Sweep -> Displacement -> MSS -> FVG -> M5 retrace
- **Thị trường có cho tín hiệu cảnh báo trước không?**
	  - Có Displacement
	  - Có MSS
	  - FVG hợp lệnh, tạo từ nến thân lớn sau 1 nhịp quét Unicorn
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 
	- 90%
	- Giá không nằm trong vùng OTE
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Cải thiện tâm lý giao dịch

---

## 5. Lesson Learned

> [!summary] Bài học cốt lõi của lệnh này
> Đây là một lệnh **process A-grade**: thắng vì *quy trình đúng*, không phải vì may. Giá trị lớn nhất không nằm ở +3.07R mà ở chỗ nó chứng minh mình đã **sửa được lỗi FOMO cũ** (không vào tại CE lần chạm đầu). Nhiệm vụ bây giờ là *đóng gói* hành vi đúng đó thành rule định lượng để lặp lại được, thay vì để nó phụ thuộc vào tâm trạng.

### 5.1. Bài học kỹ thuật

- **Confluence chồng lớp mới là POI hạng A.** Không phải FVG đơn lẻ, mà là **Unicorn = Breaker Block ⊕ FVG**, lại nằm trong **Premium** (equilibrium H1 = 1.20247, entry 1.2065 nằm trên → đúng vùng bán). Ba lớp cùng chỉ về một hướng → đây là lý do phản ứng mạnh và sạch.
- **Kiên nhẫn = để thị trường tự chứng minh trước khi cam kết vốn.** Chờ purge cạnh trên Unicorn → reject → M5 MSS + FVG rồi mới entry. Đây là hành vi cần *tái lập*, không phải ăn may một lần.
- **SL theo invalidation, không theo R mong muốn.** SL trên điểm sweep (1.20764) trả lời câu hỏi "khi nào luận điểm sai", chứ không phải "đặt đâu cho R đẹp". Giữ nguyên tư duy này.

**Triệu chứng (symptoms) — sinh ra từ root cause:**

- Lúc vào lệnh *"còn hơi sợ khi giá quét lên FVG thêm 2 nhịp (vẫn trong Unicorn)"*. → **Root cause:** entry đang là *reaction entry* mang tính discretionary, chưa có **tiêu chí trigger objective** (đóng nến hay chỉ wick? bao nhiêu nến xác nhận?). Không có tiêu chí cứng → còn chỗ cho nỗi sợ và do dự.
- Tick "đạt Kill Zone" nhưng **không ghi giờ vào lệnh**. → **Root cause:** thiếu kỷ luật logging timestamp; một tiêu chí được đánh dấu "đạt" mà không có bằng chứng kiểm chứng.
- `r_planned` = `r_multiple` = 3.075. → **Root cause:** R kế hoạch điền *sau* khi biết kết quả (hindsight), làm mất khả năng đo "mức chấp hành kế hoạch" khi mẫu lớn dần.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**

1. 24/04: hình thành OB tại 1.20616–1.20750, nhịp displacement + FVG đẩy giá tạo swing high (đỉnh range).
2. 30/04: nến displacement thân lớn **phá OB + quét old lows** xuống 1.20142 → OB bị invalidate → biến thành **Breaker**, đồng thời để lại **FVG lớn** (không overlap nhiều do nến thân lớn). Breaker ⊕ FVG = **Unicorn**, nằm trong Premium.
3. Giai đoạn đi ngang sau displacement = **re-distribution** (smart money nạp lệnh bán).
4. 03/05: giá retrace về Unicorn, **quét nhẹ ra ngoài cạnh trên** để gom BSL + stoploss của short vào sớm → reject → displacement xuống → chạy về SSL/EQL mục tiêu. Đây là mẫu kinh điển "return to breaker/FVG rồi tiếp diễn".

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- **"Giá ló ra ngoài rìa POI 1 đoạn rồi mới đảo chiều"** là pattern lặp lại của SM (purge liquidity sát POI trước khi đi). ⇒ Đừng vội invalidate ngay khi giá vừa ló ra ngoài vùng — nhưng *phải có ranh giới định lượng* để phân biệt purge với invalidation thật (xem 5.3).
- **FOMO tại CE lần chạm đầu = lỗi cũ.** Lần này đã tránh được → cần duy trì. Đây là hành vi đáng theo dõi thành một metric riêng ("số lệnh vào sớm sai vs vào đúng nhịp").
- **Hindsight bias khi kể chuyện "đó là cú trap".** Cùng price action, nếu thua mình sẽ gọi là "invalidation". Cảnh giác: chỉ được gọi là trap nếu tiêu chí objective (đã định trước) cho phép, không phải vì đã biết kết quả.

### 5.3. Rule cần thêm/cập nhật vào Playbook

1. **Rule vào lệnh tại POI quan trọng:** KHÔNG entry tại CE lần chạm đầu. Bắt buộc đủ chuỗi: (a) liquidity sweep ra ngoài rìa POI → (b) reject candle **đóng cửa lại trong vùng** → (c) xuống M5 chờ **MSS + FVG hợp lệ** → (d) entry tại **CE của FVG M5** (ghi rõ ranh giới FVG).
2. **Rule invalidation định lượng:** bỏ setup nếu giá **đóng ≥ 1 nến H1 (hoặc 2 nến M5)** trên cạnh trên BPR/Unicorn *và* nến kế tiếp không quay lại vùng. Thay "giữ bên trên" mơ hồ bằng số nến cụ thể.
3. **Rule logging bắt buộc:** luôn ghi **entry timestamp (giờ VN + ET)** để verify Kill Zone, và **ranh giới FVG M5** để xác nhận entry = CE. Không có 2 dữ liệu này thì setup **không tính vào thống kê**.
4. **Rule tách R:** ghi `r_planned` *trước* khi biết kết quả (theo TP dự kiến), `r_multiple` là kết quả thực. Cập nhật frontmatter `take_profit` đủ cả 2 mức (1.20408 + 1.20191).
5. **Rule chấm điểm confluence:** OTE là *điểm cộng khi có*, KHÔNG trừ điểm setup 2022 Model khi thiếu OTE (entry model này neo vào FVG/CE, không phải Fibonacci retracement).
6. **Rule TP chuẩn hoá:** partial TP1 50% tại short-term low gần nhất (~2R), runner tới EQL/SSL kế tiếp — đúng như lệnh này đã làm (blended 3.07R). Biến thành mặc định thay vì tuỳ hứng.

---
