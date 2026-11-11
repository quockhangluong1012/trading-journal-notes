---
type: backtest
backtest_date:
trade_date:
symbol:
position:
result:
session:
setup: ICT 2022 Model
entry_model:
entry_timeframe:
htf_bias:
bias_correct:
poi_type:
liquidity_swept:
displacement:
mss:
fvg_valid:
entry_price:
stop_loss:
take_profit:
r_planned:
r_multiple:
entry_type:
rr_if_ce:
grade:
followed_plan:
tags: [backtest, ICT2022]
---

# Backtest {{date}} — SYMBOL Position

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên Indices (NAS100 / US30). Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value                                             |
| -------------------- | ------------------------------------------------- |
| Symbol               | NAS100 / US30 / Other                             |
| Trade Date (dữ liệu) |                                                   |
| Position             | Long / Short                                      |
| Result               | Win / Loss / BE                                   |
| Session              | London / NY AM / NY PM / Asia                     |
| Setup                | ICT 2022 Model                                    |
| Entry Model          | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe      | M1 / M5 / M15                                     |
| HTF Bias             | Bullish / Bearish / Neutral                       |
| Bias Correct?        | Yes / No                                          |
| Entry                |                                                   |
| Stop Loss            |                                                   |
| Take Profit          |                                                   |
| R Planned            |                                                   |
| R Multiple (kết quả) |                                                   |
| Entry Type           | CE / Edge                                         |
| RR nếu vào CE        |                                                   |
| Grade                | A / B / C / D / F                                 |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

> [!note] Cách điền Entry Type & RR nếu vào CE
> - **`entry_type`**: `CE` nếu vào tại Consequent Encroachment (50% FVG); `Edge` nếu vào first-touch nửa trên FVG (giữa CE và cạnh trên) vì giá khả năng cao không về CE.
> - **`r_planned`** = RR *thực tế* tại điểm vào (ví dụ Edge = 2.7). **`rr_if_ce`** = RR *giả định nếu* vào ở CE (ví dụ 3.65). Nếu vào đúng CE thì `rr_if_ce` = `r_planned`.
> - Mục đích: sau ~20–30 mẫu, dashboard tự so sánh **fill-rate + expectancy** của CE vs Edge → để *dữ liệu* quyết định rule, không phải cảm tính. Quy tắc bất biến: chỉ chấp nhận Edge khi RR thực ≥ **RR floor** đã đặt trước.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish / Bearish / Neutral
- **Market Condition**: Trending / Pullback / Range / Consolidation
- **Lý do xác định bias** (PD array, draw on liquidity):
  - 
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity:
  - Sell-side liquidity:

![[SYMBOL-YYYYMMDD-D1.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: HH/HL / LH/LL / Range
- **Dealing Range**: High ___ / Low ___ → Premium / Discount
- **POI chính**: Order Block / FVG / Breaker / ___
- **Liquidity cần chờ sweep**:
  - 

![[SYMBOL-YYYYMMDD-H1.png]]

## M5 - Confirmation & Entry
- 
---

## 2. ICT 2022 Model — Entry Sequence

Đánh dấu theo đúng thứ tự checklist của mô hình:

- [ ] **1. Liquidity Sweep** — giá quét thanh khoản (Equal H/L, swing, Asia range...)
  - Loại: Internal / External / Equal Highs / Equal Lows
- [ ] **2. Displacement** — nến đẩy mạnh, tạo FVG, phá cấu trúc nội bộ
- [ ] **3. Market Structure Shift (MSS)** — phá swing point ngược hướng sweep
- [ ] **4. FVG / OB hợp lệ** hình thành trong displacement leg
- [ ] **5. Entry** — limit trong FVG/OB (CE - Consequent Encroachment) trong Kill Zone
- [ ] **6. Stop Loss** — phía trên/dưới điểm sweep (invalidation)
- [ ] **7. Take Profit** — opposing liquidity / PD array kế tiếp

![[SYMBOL-YYYYMMDD-M5.png]]

![[SYMBOL-YYYYMMDD-M1.png]]

---

## 3. Setup Quality Checklist

- [ ] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [ ] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [ ] Có Liquidity Sweep trước entry
- [ ] Có Displacement rõ ràng (không phải nến yếu)
- [ ] Có MSS hợp lệ
- [ ] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [ ] Entry trong POI hợp lệ, không đua giá
- [ ] SL ở vùng invalidation hợp lý
- [ ] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP / Hit SL / BE / Manual Close
- **Tại sao lệnh thắng/thua?**
  - 
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - 
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** ___%
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - 

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
