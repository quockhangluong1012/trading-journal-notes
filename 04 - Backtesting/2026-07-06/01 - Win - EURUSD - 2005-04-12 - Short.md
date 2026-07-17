---
type: backtest
backtest_date: 2026-01-07
trade_date: 2005-04-12
symbol: EURUSD
position: Short
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[25 - OB - Order Block|OB]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.29729
stop_loss: 1.30164
take_profit: 1.28811
r_planned: 2.1
r_multiple: 2.1
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-04-12 — EURSUD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | EURUSD                                            |
| Trade Date (dữ liệu) | 2005-04-12                                        |
| Position             | Short                                              |
| Result               | Win                                               |
| Session              | New York                                            |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M5                                                |
| HTF Bias             | Bearish                                           |
| Bias Correct?        | Yes                                               |
| Entry                | 1.29729                                           |
| Stop Loss            | 1.30164                                           |
| Take Profit          | 1.28811                                           |
| R Planned            | 2.1                                              |
| R Multiple (kết quả) | 2.1                                              |
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
  - Buy-side liquidity: Previous Day High (1.30009)
  - Sell-side liquidity: Previous Day Low (1.29090)

![[Pasted image 20260706051516.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL 
- **Dealing Range**: 
	- High: 1.30585 
	- Low 1.28001
	- Giá đang di chuyển về vùng Premium (đúng theo bias Bearish)
- **POI chính**: 
	- Order Block : 1.30110 - 1.29573
- **Liquidity cần chờ sweep**:
  - Old Highs: Giá hình thành 1 Equal high khung H1 bên trong Order Block (1.30033)
  - Cạnh trên Order Block
### Phân Tích:
- Giá hình thành 1 BPR lớn bên dưới vùng discount sau 1 nhịp giá tăng mạnh (Target)
- Giá quay lại vùng Premium
- Tạo 1 Equal High rõ
- Giá Quét qua vùng equal high và cạnh trên của OB sau đó giá quay lại đóng nến vào trong OB

![[Pasted image 20260706051548.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá tạo displacement + FVG sau khi quét lên cạnh trên OB và EH
- Giá hình thành MSS
- FVG hình thành trùng lắp với OB khung H1
- Giá retrace gần tới FVG -> Entry
- Stoploss đặt trên điểm sweep
- POI đang nằm trong vùng OTE
- **Entry trigger**:
  - Liquidity Sweep: Quét qua OB + QH
  - MSS: Giá tạo MSS
  - Displacement: có displacement
  - FVG: Giá tạo FVG
  - OB: Có
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry
- **Invalidation reason**:
  - Giá đóng qua đỉnh swing high đã quét trước đó
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260706052036.png]]
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
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Giá về premium -> Quét OB + EQH -> MSS + Displacement + FVG -> Giá retrace FVG -> Entry
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Partial take profit

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Confluence mạnh nhất của lệnh này là **FVG M5 trùng lắp với Order Block H1**, và toàn bộ POI nằm trong vùng **Premium + OTE**. Đây là loại chồng lớp (HTF POI × LTF FVG × Premium × OTE) cần ưu tiên săn khi backtest — một FVG M5 đơn lẻ không gối lên POI HTF thì giá trị thống kê thấp hơn hẳn.
- Việc chờ giá quét **cả EQH H1 (thanh khoản quan trọng) lẫn cạnh trên OB** rồi mới xuất hiện MSS là bước lọc entry chất lượng. Sweep đúng thanh khoản mục tiêu (draw on liquidity) trước MSS là điều kiện, không phải tùy chọn.
- Tín hiệu **nến quét xong quay lại đóng vào trong OB** (close back inside OB) là dấu hiệu sớm, xuất hiện *trước* MSS trên M5 — có thể dùng làm cảnh báo "chuẩn bị vào vùng quan sát".

### Pattern lặp lại (điều cần để ý lần sau)

- **EQH nằm bên trong một OB lớn = nam châm thanh khoản.** Giá gần như luôn quét EQH đó trước khi đảo chiều. Khi thấy Equal Highs bên trong POI, mặc định là *chờ quét rồi mới tính entry*, đừng đón đầu.
- Chuỗi 2022 Model đã khớp gần như sách giáo khoa: Premium → sweep (OB + EQH) → MSS + displacement + FVG → retrace CE → entry. Ghi nhớ đúng trình tự này để nhận diện nhanh lần sau.

### Rule cần thêm/cập nhật vào Playbook

- [ ] Chỉ vào 2022 Model khi **FVG entry M5 trùng/nằm trong POI HTF** (OB hoặc FVG H1). FVG M5 không có confluence HTF → bỏ qua.
- [ ] Khi kế hoạch RR > 2R, **lập kế hoạch partial TP từ trước khi vào lệnh** (ví dụ chốt 50% tại 1R hoặc tại PD array trung gian). Đây là điểm "nếu vào lại" đã tự nhận ra — biến nó thành rule thay vì tiếc nuối sau lệnh.

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias | 9/10 |
| POI Selection | 9/10 |
| Liquidity Sweep | 9/10 |
| MSS Confirmation | 8/10 |
| FVG / OB Entry | 9/10 |
| Risk Management (RR) | 7/10 |

**Overall Grade**: A

---

### Liên kết

- Concept: [[Trading Journal/03 - Playbooks/3.2 - Setups/ICT 2022 Model]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[26 - OTE - Optimal Trade Entry]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - ]]
