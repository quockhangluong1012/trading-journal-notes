---
type: backtest
backtest_date: 2026-01-07
trade_date: 2010-10-19
symbol:
  - EURUSD
position: Long
result:
  - Win
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct:
  - Yes
poi_type: "[[25 - OB - Order Block|OB]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.39086
stop_loss: 1.38801
take_profit: 1.39521
r_planned: 1.53
r_multiple:
grade:
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2010-10-19 — EURSUD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | EURUSD                                            |
| Trade Date (dữ liệu) | 2010-10-19                                        |
| Position             | Long                                              |
| Result               | Win                                               |
| Session              | London                                            |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M5                                                |
| HTF Bias             | Bullish                                           |
| Bias Correct?        | Yes                                               |
| Entry                | 1.39086                                           |
| Stop Loss            | 1.38801                                           |
| Take Profit          | 1.39521                                           |
| R Planned            | 1.53                                              |
| R Multiple (kết quả) | 1.53                                              |
| Grade                | B                                                 |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - D1 đang trong nhịp tăng mạnh (treding)
  - HH/HL
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day High
  - Sell-side liquidity: Previous Day Low

![[Pasted image 20260701075001.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL 
- **Dealing Range**: 
	- High: 1.14594 
	- Low 1.38319 
	- Giá đang trong vùng Discount
- **POI chính**: 
	- Order Block : 1.3914 - 1.38869
- **Liquidity cần chờ sweep**:
  - Old lows: 1.38890
  - Cạnh dưới Order Block để quét những người vào lệnh sớm
### Phân Tích:
- Giá đang nằm trong vùng Discount của dealing range
- Giá đã quét thanh khoản và tạo 1 Order Block trước đó
- Hiện tại giá đang retrace về vùng Order Block
- Chờ Giá fill Order Block và xem phản ứng
- Giá quét xuống cạnh dưới của order block và quay lên đóng nến trên 50% -> Respect Order Block
- Sau đó xuống khung M5 quan sát phản ứng

![[Pasted image 20260701131425.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá tạo displacement + FVG sau khi quét xuống cạnh dưới OB
- Giá phá qua đỉnh trước đó tạo thành MSS
- FVG hình thành trùng lắp với OB khung H1
- Giá retrace về 50% FVG -> Entry
- Stoploss đặt dưới order block
- **Entry trigger**:
  - Liquidity Sweep: Quét qua OB + old low
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - OB: Có
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG 50% -> Entry
- **Invalidation reason**:
  - Giá đóng qua đáy cũ
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260701131752.png]]
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
- [ ] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP / Hit SL / BE / Manual Close
- **Tại sao lệnh thắng/thua?**
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về discount -> Quét OB + Old lows -> MSS + Displacement + FVG -> Giá retrace 50% FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- 

### Pattern lặp lại (điều cần để ý lần sau)

- 

### Rule cần thêm/cập nhật vào Playbook

- [ ] 

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

**Overall Grade**: A / B / C / D / F

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
