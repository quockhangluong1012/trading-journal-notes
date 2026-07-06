---
type: backtest
backtest_date: 2026-01-07
trade_date: 2005-04-13
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
poi_type: "[[25 - OB - Order Block|OB]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29239
stop_loss: 1.29545
take_profit: 1.28404
r_planned: 2.78
r_multiple: 2.78
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-13 — EURSUD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | EURUSD                                            |
| Trade Date (dữ liệu) | 2005-04-13                                        |
| Position             | Short                                             |
| Result               | Win                                               |
| Session              | New York                                          |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M5                                                |
| HTF Bias             | Bullish                                           |
| Bias Correct?        | Yes                                               |
| Entry                | 1.29239                                           |
| Stop Loss            | 1.29545                                           |
| Take Profit          | 1.28404                                           |
| R Planned            | 2.78                                              |
| R Multiple (kết quả) | 2.78                                              |
| Grade                | A                                                 |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang LH/LL
  - Nhịp displacement có tạo Liquidity Void
  - => Bias chuyển sang Bearish
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day High
  - Sell-side liquidity: Previous Day Low 

![[Pasted image 20260706054317.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: :H/:: 
- **Dealing Range**: 
	- High: 1.30153 
	- Low 1.28082
	- Giá đang di chuyển về vùng Premium (đúng theo bias Bearish)
- **POI chính**: 
	- Order Block : 1.29907 - 1.29741
	- FVG: 1.29743 - 1.29321
- **Liquidity cần chờ sweep**:
  - Vùng FVG khung H1
  - Order Block
### Phân Tích:
- Hình thành FVG sau nhịp giảm mạnh của ngày 12 để lại 1 FVG khung H1 lớn, phía trên cạnh FVG là Order Block (Bearish)
- FVG và OB nằm trong vùng OTE H1
- Giá retrace về vùng FVG (50%)
- Giá quét qua vùng CE H1 và đóng nến xuống bên dưới (2 lần) -> FVG mạnh
- Có dấu hiệu reject vùng CE, xuống khung M5 quan sát
![[Pasted image 20260706054350.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá di chuyển tới vùng CE của FVG, quét qua và sau đó đóng nến lại bên dưới
- Sau vài nến giá lại quay về đúng CE tạo thành EQH 
- Sau đó giá bật ra với các nến lớn, tuy nhiên râu nến trùng lắp -> không tạo FVG -> Quan sát tiếp không vào vội vì khả năng sẽ quét EQH
- Giá di chuyển ra khỏi FVG sau đó có các nến displacement mạnh phá lên lại FVG, quét cái đỉnh nhỏ và EQH ( quét các inducement)
- Sau khi quét giá bật xuống mạnh kèm nến displacement rất lớn tạo Liquidity Void (có nhiều FVG)
- Sau đó vào New York Killzone giá retrace về CE của FVG mới tạo của nhịp displacement
- Entry tại CE, stoploss đặt trên đỉnh cây nến quét EQH trước đó
- Bên dưới có vùng FVG trùng với Bullish Order BLock => Target tới vùng Overlap
- **Entry trigger**:
  - Liquidity Sweep: Quét qua FVG ( tới CE) + EQH + Inducement
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry
- **Invalidation reason**:
  - Giá đóng qua đỉnh swing high đã quét trước đó
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260706054240.png]]
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
  - Lệnh thắng vì chờ đầy đủ các điều kiện trước khi setup hình thành, không vào vội
  - Setup nằm trong KillZone (New york)
  - Giá quét EQH (khung H1 - quan trọng), quét OB
  - Giá đang trong vùng Premium và quan trọng là đang trong khu vực OTE
  - Quan trọng là giá đã quét vung CE FVG lớn và bật ra với nến lớn tuy nhiên không tạo FVG -> Khả năng sẽ còn quét
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về premium -> Quét OB + EQH -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
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

**Overall Grade**: A

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
