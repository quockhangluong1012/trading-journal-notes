---
type: backtest
backtest_date: 2026-07-07
trade_date: 2005-04-24
symbol: EURUSD
position: Long
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[07 - Unicorn Model|Unicorn Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29582
stop_loss: 1.29451
take_profit: 1.29884
r_planned: 2.23
r_multiple: 2.23
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-24 — EURSUD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                 |
| -------------------- | ------------------------------------- |
| Symbol               | EURUSD                                |
| Trade Date (dữ liệu) | 2005-04-24                            |
| Position             | Long                                  |
| Result               | Win                                   |
| Session              | New York                              |
| Setup                | ICT 2022 Model                        |
| Entry Model          | [[07 - Unicorn Model\|Unicorn Model]] |
| Entry Timeframe      | M5                                    |
| HTF Bias             | Bullish                               |
| Bias Correct?        | Yes                                   |
| Entry                | 1.29582                               |
| Stop Loss            | 1.29451                               |
| Take Profit          | 1.29884                               |
| R Planned            | 2.23                                  |
| R Multiple (kết quả) | 2.23                                  |
| Grade                | A                                     |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang HH/HL
  - Nhịp displacement có tạo FVG khung D1
  - => Bias chuyển sang Bullish
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day/Week High
  - Sell-side liquidity: Previous Day/Week Low 
![[Pasted image 20260707061746.png]]
### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL
- **Dealing Range**: 
	- High: 1.31266
	- Low 1.28777
	- Giá đang di chuyển về vùng Discount (đúng theo bias Bullish)
- **POI chính**: 
	- Breaker Block : 1.29480 - 1.29357
	- FVG: 1.29595 - 1.29426
	- Vùng Unircorn (quan trọng - POI chính): vùng overlap giữa Breaker Block và FVG -> 1.29498 - 1.29433
- **Liquidity cần chờ sweep**:
  - Vùng FVG khung H1
  - Vùng Breaker Block
  - Đặc biệt quan sát giá phản ứng tại vùng Unicorn
### Phân Tích:
- 2 -3 ngày trước H1 vẫn đang trong xu hướng giảm (Bearish Bias) và hình thành OB trên khung H1 (khi đó tôi đang chờ giá quay lại và xem setup lệnh short hình thành)
- Ngày hôm sau giá bật lên mạnh (displacement) phá qua các swing high khung H1 (và swing high khung D1) -> dẫn đến khung D1 hình thành MSS + FVG
- Bias sau đó đổi sang Bullish
- Vùng Order Block ban đầu sau nhịp displacement phá qua trở thành Bullish Breaker Block
- Đồng thời trong nhịp đẩy giá mạnh (displacement) có hình thành FVG khung H1, trùng lắp 1 phần với Breaker Block
- Phần Overlap đó hình thành 1 vùng quan trọng là Unicorn khung H1
- Sau đó tôi chờ giá quay về vùng Unicorn này
- Unicorn này nằm đúng trong OTE - đặc biệt là nằm sát cạnh CE của OTE (sweet spot 0.705)
- Tuy nhiên phải chờ khá lâu để giá quay về vùng này (setup ngày 18, tới ngày 26 giá mới quay về)
- Giá quay về CE của vùng Unicorn và xuất hiện dấu hiệu rejection
- Xuống khung M5 quan sát
![[Pasted image 20260707061856.png]]
## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá chạm vùng Unicorn với các râu nến ( chạm vào bật ra và đóng bên ngoài 4 nến liền tiếp và có 1 nếm quét qua vùng CE)
- Sau đó giá bật lên với các nến lớn (displacement)
- Giá tạo MSS + FVG
- Entry tại FVG
- Stoploss đặt bên dưới điểm sweep (CE unicorn)
- **Entry trigger**:
  - Liquidity Sweep: Quét EQL, 50% Unicorn
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là Unicorn)
- **Invalidation reason**:
  - Giá đóng qua đáy sweep/qua unicorn
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260707062004.png]]
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

- **Result**: Đóng lệnh khi đạt 2.3R thay vì đợi hết TP
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone (New york)
  - Giá quét EQL (khung M5), quét tới CE unicorn
  - Giá đang trong vùng Discount và quan trọng là đang trong khu vực sweet spot OTE
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về discount -> Quét EQL + CE Unicorn -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- **Swing high/low M5 dùng làm TP thực chất là một vũng [[20 - Liquidity Sweep|BSL/SSL]]** — giá bị *draw* tới để **quét** rồi mới đảo, chứ không "hướng tới cái đỉnh". Vì vậy nên đặt TP **nhỉnh dưới đỉnh vài pip** (front-run liquidity) thay vì đặt ngay tại/vượt đỉnh → tăng tỉ lệ khớp TP và giải quyết đúng nỗi "giá gần chạm TP rồi quay đầu".
- **TP tại đỉnh M5 gần nhất chỉ tối ưu win rate**, nó cắt cụt các lệnh còn draw HTF cao hơn (đánh đổi *hit rate ↔ average R*). Lệnh này rơi đúng vào kịch bản đó: TP nằm ở **BSL trung gian** (đường đỏ dưới), còn một swing high cao hơn (đường đỏ trên) **chưa bị quét** → đáng lẽ nên giữ một phần làm runner.
- **Quyết định "cắt hết hay để runner" phải dựa trên bản đồ Draw on Liquidity đa khung** (đỉnh M5 là *điểm đến cuối* hay *trạm trung gian*?), lấy từ phân tích H1/D1 (draw = PDH/PWH), **không dựa vào cảm giác**.

### Pattern lặp lại (điều cần để ý lần sau)

- Xu hướng **chốt toàn bộ tại đỉnh M5 gần nhất** → khóa mọi lệnh thắng quanh ~2R, ép average R xuống dù win rate cao. Về dài hạn hệ thống ICT 2022 sống nhờ các cú runner; nén hết về 2R sẽ bào mòn expectancy.
- Note ghi *"Đóng khi đạt 2.3R thay vì đợi hết TP"* → cần phân biệt rõ: **chốt theo kế hoạch (2R rule)** hay **chốt vì sốt ruột**. Nếu là cái sau thì dù kết quả +2.3R, đây vẫn là **lỗi process** cần đánh dấu vì không lặp lại được một cách kỷ luật.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Đặt TP **nhỉnh dưới** swing high/low mục tiêu vài pip (front-run BSL/SSL), không đặt tại/vượt đỉnh.
- [ ] Áp dụng **scale-out**: chốt 50–70% tại BSL/SSL trung gian gần nhất → dời SL về **BE** → để phần còn lại chạy tới **draw HTF kế tiếp** (đỉnh xa hơn / PDH/PWH).
- [ ] Ghi thêm field **MFE (Maximum Favorable Excursion)** cho mỗi lệnh backtest (sau khi chạm đỉnh M5 gần nhất, giá còn đi thêm bao nhiêu R tới draw HTF kế tiếp trước khi retrace về BE) để **định lượng full-exit vs partial** sau 30–50 mẫu, thay vì quyết định bằng linh cảm.

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | /10 |
| POI Selection | /10 |
| Liquidity Sweep | /10 |
| MSS Confirmation | /10 |
| FVG / OB Entry | /10 |
| Risk Management (RR) | /10 |

**Overall Grade**: A

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
