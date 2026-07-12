---
type: backtest
backtest_date:
trade_date:
symbol:
position:
result:
session:
setup: ICT 2022 Model - LTF (H1-M5-M1)
entry_model: ICT 2022 LTF
entry_timeframe: M1
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
killzone_gate:
macro_window:
h4_conflict:
m5_displacement_score:
spread_cost:
r_net:
tags: [backtest, ICT2022, LTF]
---

# Backtest {{date}} — SYMBOL Position — ICT 2022 LTF (H1→M5→M1)

> [!info] Mục đích backtest biến thể LTF
> Replay dữ liệu quá khứ để luyện nhận diện **[[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]]** trên **NQ1/NAS100 và EURUSD/GBPUSD**. Mỗi file = 1 setup. Ở khung thấp, mục tiêu bổ sung: xác nhận biến thể có **expectancy ròng dương *sau khi trừ spread/commission*** — chứ không phải chỉ R lý thuyết. KHÔNG giả định thống kê từ khung gốc D1→H1→M5 chuyển sang.

> [!important] Bộ ba khung của biến thể — điền đúng vai trò
> **H1 (lọc H4) = Bias/Draw** · **M5 = POI/Sweep/Displacement (động cơ)** · **M1 = Entry refine (vô-lăng)**. Displacement/MSS chấm điểm trên **M5**, KHÔNG phải M1. M1 chỉ để tinh chỉnh điểm vào quanh CE.

---

## 0. Backtest Summary

| Field                     | Value                                              |
| ------------------------- | -------------------------------------------------- |
| Symbol                    | NQ1 / NAS100 / EURUSD / GBPUSD                      |
| Trade Date (dữ liệu)      |                                                    |
| Position                  | Long / Short                                       |
| Result                    | Win / Loss / BE                                    |
| Session                   | London / New York (AM)                             |
| **Killzone GATE**         | **Pass / Fail** (Fail → No Trade, không chấm tiếp) |
| **Macro window (ET)**     | 02:33–03:00 / 04:03–04:30 / 09:50–10:10 / 10:50–11:10 |
| Setup                     | ICT 2022 Model - LTF (H1-M5-M1)                    |
| Entry Model               | M5 Sweep + M5 Displacement/MSS + M5 FVG            |
| Entry Timeframe           | M1 (refine) trong M5 FVG                            |
| HTF Bias (H1)             | Bullish / Bearish / Neutral                        |
| H4 Conflict?              | No / Yes (ngược trend lớn → hạ cấp)                |
| Bias Correct?             | Yes / No                                           |
| Entry                     |                                                    |
| Stop Loss                 |                                                    |
| Take Profit               |                                                    |
| **Spread + commission**   | ___ pip/pt (đo tại thời điểm vào)                  |
| R Planned (gross)         |                                                    |
| **R Net (sau spread)**    |                                                    |
| R Multiple (kết quả)      |                                                    |
| Entry Type                | CE / Edge                                          |
| RR nếu vào CE             |                                                    |
| M5 Displacement Score     | ___/4 (CLV · body-wick · acceptance · FVG)         |
| Grade                     | A / B / C / D / F                                  |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** để Dataview dashboard tự tổng hợp. Các field LTF mới (`killzone_gate`, `macro_window`, `h4_conflict`, `m5_displacement_score`, `spread_cost`, `r_net`) là **bổ sung** — không thay thế field cũ.

> [!warning] Đo R *ròng*, không chỉ R lý thuyết
> Ở khung thấp target nhỏ → spread + commission chiếm tỷ trọng lớn trong R. Luôn tính **`r_net` = R sau khi trừ chi phí vào lệnh**. Một setup "3R trên giấy" có thể chỉ còn ~2R ròng. Nếu `r_net` < RR floor đã đặt → đánh dấu No Trade dù giá "chạy đúng".

> [!note] Entry Type & RR nếu vào CE (giữ như khung gốc)
> - **`entry_type`**: `CE` nếu vào tại Consequent Encroachment (50% M5 FVG); `Edge` nếu vào first-touch nửa trên FVG.
> - **`r_planned`** = RR thực tế tại điểm vào; **`rr_if_ce`** = RR giả định nếu vào ở CE.
> - Sau ~20–30 mẫu, dashboard so sánh fill-rate + expectancy CE vs Edge → để *dữ liệu* quyết định rule.

---

## 1. HTF Context & Bias

### H4 — Bộ lọc trend lớn (chỉ để loại, không sinh setup)

- **H4 direction**: Up / Down / Range
- **Có ngược gay gắt với hướng định trade không?**: No / Yes → nếu Yes, hạ cấp hoặc bỏ.

![[SYMBOL-YYYYMMDD-H4.png]]

### H1 — Bias & Draw on Liquidity (tầng context)

- **Bias**: Bullish / Bearish / Neutral
- **Market Condition**: Trending / Pullback / Range
- **Dealing Range H1**: High ___ / Low ___ → **Premium / Discount** (entry phải đúng phía)
- **Draw on Liquidity (target cuối)**:
  - Buy-side (BSL): PDH / session high / equal highs @ ___
  - Sell-side (SSL): PDL / session low / equal lows @ ___
- **Lý do bias** (PD array, draw):
  -

![[SYMBOL-YYYYMMDD-H1.png]]

---

## 2. ICT 2022 LTF — Entry Sequence (động cơ trên M5, refine trên M1)

Đánh dấu theo đúng thứ tự. **Displacement + MSS phải xác nhận trên M5.**

- [ ] **GATE — Killzone/Macro**: đang trong London Open / NY AM (macro: ______ ET). *Fail → dừng, No Trade.*
- [ ] **1. M5 Liquidity Sweep** — quét pool (Asian range / equal H-L / session H-L) + **reclaim**
  - Loại: Internal / External / Equal Highs / Equal Lows
  - Có double-sweep không? (M5 hay quét 2 lần): ___
- [ ] **2. M5 Displacement** — nến M5 đẩy mạnh, để lại **M5 FVG**, phá cấu trúc M5
  - Score 4 tiêu chí: CLV ≥0.7 [ ] · body ≥70% [ ] · acceptance (nến M5 không lấp lại) [ ] · FVG sạch [ ]  → **___/4** (cần ≥3/4)
- [ ] **3. M5 MSS** — phá swing point M5 ngược hướng sweep
- [ ] **4. M5 FVG / OB hợp lệ** trong displacement leg — đo độ rộng: ___ pip/pt (so spread ___)
- [ ] **5. Entry (M1 refine)** — limit quanh CE của M5 FVG / M1 FVG bên trong; (tùy chọn) chờ M1 MSS xác nhận
- [ ] **6. Stop Loss** — ngoài điểm M5 sweep + **buffer wick** (đặc biệt NQ1)
- [ ] **7. Take Profit** — internal M5 liquidity → external H1 pool

![[SYMBOL-YYYYMMDD-M5.png]]

![[SYMBOL-YYYYMMDD-M1.png]]

---

## 3. Setup Quality Checklist (LTF)

- [ ] **GATE killzone Pass** (bắt buộc — ngoài KZ = noise)
- [ ] Bias H1 rõ ràng + H4 không ngược gay gắt
- [ ] Có **M5** Liquidity Sweep + reclaim trước entry
- [ ] M5 Displacement score ≥ 3/4 (không phải nến to bấc dài do spike)
- [ ] Có M5 MSS hợp lệ
- [ ] M5 FVG / OB nằm trong Discount (buy) / Premium (sell) của range H1
- [ ] Độ rộng M5 FVG > spread + commission (không bị phí nuốt gap)
- [ ] Entry là **retrace** (M1 refine), không chase M5 displacement
- [ ] SL ngoài invalidation + buffer wick
- [ ] **R Net (sau spread) ≥ RR floor** (không chỉ R gross)
- [ ] (FX) SMT EURUSD↔GBPUSD↔DXY xác nhận tại sweep — [[42 - SMT Divergence]]

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP / Hit SL / BE / Manual Close
- **Tại sao lệnh thắng/thua?**
  -
- **Chi phí (spread/slippage) ảnh hưởng thế nào tới kết quả?**
  -
- **M5 displacement có phải thật, hay là noise mình nâng M1 lên?**
  -
- **Setup khớp bao nhiêu % với biến thể chuẩn?** ___%
- **Nếu vào lại, tôi sẽ làm gì khác?**
  -

---

## 5. Lesson Learned

### Bài học kỹ thuật (đặc thù khung thấp)

-

### Pattern lặp lại (điều cần để ý lần sau)

-

### Rule cần thêm/cập nhật vào Playbook / note biến thể

- [ ]

---

## 6. Final Grade

| Tiêu chí | Điểm |
|---|---|
| Killzone/Macro Timing (GATE) | /10 |
| HTF Bias (H1 + lọc H4) | /10 |
| M5 POI Selection | /10 |
| M5 Liquidity Sweep | /10 |
| M5 Displacement/MSS quality | /10 |
| M1 Entry refine & Risk (R net) | /10 |

**Overall Grade**: A / B / C / D / F

> [!tip] Chống curve-fitting trên khung thấp
> LTF có rất nhiều nến → dễ "chọn đẹp" sau khi biết kết quả. Kiểm tra: trigger (M5 sweep + M5 displacement ≥3/4 + trong killzone) có nhận diện được **trước** khi biết outcome không? Nếu không → loại mẫu này khỏi thống kê.

---

### Liên kết

- Model: [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]] · [[01 - ICT 2022 Model]]
- Layering/nhiễu: [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]] · [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[26 - OTE - Optimal Trade Entry]]
- Timing: [[18 - Kill Zones]] · [[40 - Macro Times]]
- Dashboard: [[_Backtest Dashboard]]
- Mistake liên quan: [[Mistake - Chase Displacement]] · [[Mistake - Skip Liquidity Sweep]]
