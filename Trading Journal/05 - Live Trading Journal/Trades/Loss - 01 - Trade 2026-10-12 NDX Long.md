---
date: 2026-10-12
symbol: NDX
position: Long
result: Loss
session: New York
kill_zone:
  - New York
setup: ICT 2022 Model
entry_model: Liquidity Sweep + MSS + FVG
entry_timeframe: M1
higher_timeframe_bias: Bullish
bias_correct: No
entry_price: 30664
exit_price: 30627.9
take_profit: 30796.3
stop_loss: 30627.9
pnl:
r_multiple: -1
planned_rr: 3.66
risk_percent:
confidence:
emotions:
mistakes:
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[05-Mistake-Not-enough-RR]]"
  - "[[14-Mistake-No-Trade-Management-Round-Trip]]"
mfe_r: 2.47
mae_r: -0.91
time_of_mfe: "12:00 NY"
first_obstacle_r: 1.18
management: none
first_error_step: draw
missing_step: MSS hợp lệ (M5, mức đánh dấu trước) + H1 POI/pool viết trước
followed_plan: No
grade: D
tags:
  - DailyBias
  - LiquiditySweep
  - MarketStructureShift
  - FairValueGap
  - KillZones
  - Discount
  - TradeManagement
---

# Trade 2026-10-12 - NDX Long Loss

> [!warning] Trường cần bạn tự điền (không suy đoán)
> `pnl` (tiền thật) · `risk_percent` · `confidence` · `emotions` · giờ khớp lệnh chính xác · slippage khi chạm SL (`exit_price` đang ghi bằng SL 30,627.9) · ảnh M1 `NDX-20261012-M1.png`.

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX (Spreadex US Tech 100 CFD) |
| Position | Long |
| Result | Loss (Hit SL) |
| Session | New York (entry ~10:16–10:20 NY = ~21:16–21:20 VN) |
| Setup | ICT 2022 Model |
| Entry Model | Liquidity Sweep + MSS + FVG |
| Entry Timeframe | M1 |
| HTF Bias | Bullish (D1) |
| Bias Correct? | No — chấm ex-ante: D1 bullish vĩ mô đúng, nhưng không có Context Note và DOL trong ngày là SSL 30,554.6 |
| Entry | 30,664 |
| Stop Loss | 30,627.9 (risk 36.1 điểm) |
| Take Profit | 30,796.3 (planned RR 3.66) |
| PnL | _(điền)_ |
| R Multiple | −1R |
| MFE / MAE | +2.47R (30,753) / −0.91R (30,631) |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Pullback (đang hồi từ ATH 31,369 ngày 6/10)
- **Lý do xác định bias**:
  - HH/HL rõ: đáy tháng 4 ~22,800 → đỉnh tháng 6 ≈30,700 → HL tháng 8 27,077 → HH 31,369 (6/10).
  - Giá đang retest vùng đỉnh tháng 6 / vùng breakout ≈30,600–30,700.
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity: 31,369 (ATH) — DOL vĩ mô, cách entry ~705 điểm.
  - Sell-side liquidity: **30,554.6** (đáy 8/10, đáy range, chưa bị lấy lúc vào lệnh) · 30,093 (đáy 29/9 = protected low).
- **Ghi chú quan trọng** (review):
  - Thiếu protected low và invalidation: D1 close < 30,093.
  - Dealing range D1 operative 30,093 → 31,369, EQ 30,731 → entry z ≈ 0.45 (sát EQ, không phải discount rõ). Range 28,773 → 31,369 cho z ≈ 0.73 (premium) → hai range mâu thuẫn → confidence thấp.
  - Pool đối diện gần (30,554.6) còn nguyên = điểm yếu số 1 của bias tăng.

![[NDX-20261012-D1.png]]

---

### H1

- **Cấu trúc H1**: LH/LL (sau ATH)
- **Dealing Range chính**:
  - High: 31,368.8 (6/10)
  - Low: 30,554.6 (8/10)
  - Premium / Discount: EQ ≈30,960 → giá ở discount sâu (z ≈ 0.13)
- **POI chính**:
  - Order Block: —
  - FVG: —
  - Breaker: —
  - Other: "OTE 0.79–1" đo trên range trên. **Review:** đáy hình thành *sau* đỉnh → đây là nhịp giảm, OTE cho lệnh long đo sai chiều (xem §4).
- **Liquidity cần chờ sweep**:
  - Ghi lúc vào lệnh: đáy 8/10 (30,654 — HL M15 lúc 15:15 NY).
  - Review: pool cần chờ là **30,554.6** (external). 30,654 chỉ là internal / inducement.
- **Kịch bản mong muốn**:
  - Giá quét đáy rồi đảo lên theo bias D1.

Swing map H1 (review):

| Swing | Giá | Ý nghĩa |
|---|---|---|
| HL 5/10 | 30,709 | Gốc nhịp cuối lên ATH — **bị phá 8/10 bằng displacement → H1 MSS giảm** |
| ATH 6/10 | 31,369 | BSL ngoài |
| LH 7–8/10 | 31,218 | Lower high đầu tiên |
| LL 8/10 | 30,554.6 | Đáy range — SSL ngoài |
| LH 9/10 | 31,036 | — |
| HL nội bộ 9/10 | 30,765 | PDL — bị phá 09:30 NY ngày 12/10, 2 thân nến M15 đóng dưới (acceptance) |
| 11–12/10 | 31,062 | Quét BSL 31,036 rồi đảo xuống — vẫn là LH |

![[NDX-20261012-H1.png]]

![[NDX-20261012-H1-2.png]]
*Ảnh chú thích (review): swing map, H1 MSS 8/10, Range B (31,062 → 30,555, EQ 30,808), SSL ngoài chưa bị lấy nằm dưới SL.*

---

### M15 / M5

- **Giá đã vào POI chưa?** No — không có H1 POI viết trước (vùng D1 retest đỉnh tháng 6 thì có).
- **Có Liquidity Sweep chưa?** Yes — quét 30,648.5 / 30,654.
- **Sweep loại nào?**
  - Internal liquidity (HL M15 15:15 ngày 8/10). External 30,554.6 chưa bị lấy.
- **Có Displacement chưa?** Yes trên M1 · No trên M15 tại thời điểm entry.
- **Có MSS chưa?** No (theo định nghĩa v0.2) — xem §M1.
- **Có FVG hợp lệ chưa?** Yes trên M1 (30,663–30,674).
- **Entry có nằm trong POI không?** No

> [!warning] Ex-ante vs ex-post
> Nến M15 10:15 (O 30,662 · H 30,706 · L 30,631 · C 30,670) — "râu quét dài rồi đóng trở lại" — **đóng sau khi lệnh đã khớp**. Bằng chứng M15 có thật tại lúc vào lệnh là nến 10:00: thân giảm, low ≈30,640, đóng 30,662 (chỉ đóng trên 30,654 khoảng 8 điểm).

![[NDX-20261012-M15-1.png]]

![[NDX-20261012-M15-2.png]]

![[NDX-20261012-M15-3.png]]
*Ảnh chú thích (review): FVG giảm 30,706–30,722 và 30,780–30,813, PDL 30,763, đỉnh nến 10:00 ≈30,750, EQ nhịp NY ≈30,742, entry/SL/TP, MAE/MFE, điểm chạm SL.*

---

### M1 Entry Timeframe

- **Entry trigger**:
  - Liquidity Sweep: đáy ≈30,640 (10:00–10:14 NY), quét 30,648.5 / 30,654.
  - MSS: nến M1 10:15 (O 30,662 · H 30,697 · L 30,662 · C 30,691) đóng qua đỉnh M1 10:11 (O 30,669 · H 30,677 · L 30,653 · C 30,656).
  - Displacement: thân 29/35 điểm = 83%, CLV 0.83.
  - FVG: 30,663–30,674.
  - OB: —
- **Entry reason**:
  - Limit tại FVG M1 sau MSS, 30,664.
- **Invalidation reason**:
  - SL 30,627.9 = dưới đáy sweep + buffer.
- **Tôi có chờ đủ điều kiện không?** No
  - Swing bị phá (30,677) là swing vi mô (L1). Nó chỉ lấy lại ≈27% nhịp giảm NY (30,852 → ≈30,640).
  - Mức MSS đúng theo v0.2 (gốc nhịp vào sweep, ITH M5) ≈30,750 (đỉnh nến 10:00) — giá chưa bao giờ đóng thân trên mức này.
  - FVG nằm **dưới** mức bị phá 30,677: muốn khớp, giá phải quay lại dưới mức MSS.
  - Sau khi khớp, giá tạo đáy mới 30,631 < đáy trước MSS ≈30,640 → MSS thất bại về cấu trúc. Lệnh sống sót nhờ còn cách SL 3.1 điểm.
  - Dùng M1 thay vì M5 → lệch khỏi framework D1 → H1 → M5.

_(chưa có ảnh M1 — bổ sung `NDX-20261012-M1.png` vào `Screenschots/2026/10/12/`)_

---

## 2. Checklist Trước Khi Vào Lệnh

- [ ] Đã xác định Daily Bias rõ ràng — _chỉ có HH/HL; thiếu DOL, pool đối diện, invalidation_
- [ ] Bias không mâu thuẫn với H1/M15 — _H1 LH/LL, PDL bị phá có acceptance_
- [ ] Giá đã vào vùng POI hợp lệ — _không có H1 POI viết trước; OTE đo sai chiều_
- [x] Có Liquidity Sweep trước entry — _nhưng là internal (30,654); external 30,554.6 còn nguyên_
- [x] Có Displacement rõ ràng — _trên M1_
- [ ] Có Market Structure Shift hợp lệ — _phá swing vi mô, không phải gốc nhịp vào sweep_
- [x] Entry nằm trong FVG / OB / PD Array hợp lệ — _FVG M1, nhưng nằm dưới mức MSS_
- [ ] Stop loss đặt ở vùng invalidation hợp lý — _SL nằm phía trên SSL ngoài 30,554.6_
- [ ] RR tối thiểu đạt yêu cầu — _R tới vật cản đầu tiên (FVG giảm 30,706.5) = 1.18_
- [ ] Đã kiểm tra tin tức quan trọng — _(điền)_
- [ ] Không vào lệnh vì FOMO — _(điền)_
- [ ] Không revenge trade — _(điền)_
- [ ] Không vào lệnh ngoài kế hoạch — _không có kế hoạch viết trước_

---

## 3. Execution Review

### Điều tôi làm đúng

- Vào lệnh trong killzone chỉ số NY AM (08:30–11:00 NY) và cửa sổ 10:00–11:00.
- Đúng vùng giá: retest đỉnh tháng 6, discount sâu trên H1.
- Chờ có displacement + FVG rồi đặt limit, không đuổi giá.
- Có SL, có buffer.

### Điều tôi làm sai

- Dịch "D1 bullish" thành "hôm nay mua" trong khi H1 và dòng chảy trong ngày đang giảm.
- Bỏ qua SSL ngoài 30,554.6 — chính đáy range mình tự vẽ — nằm ngay dưới SL.
- Gọi một cú phá đỉnh M1 vi mô là MSS.
- Đo OTE trên một nhịp giảm.
- Target lấy từ fib, nằm trong FVG giảm 30,780–30,813 và trên PDL 30,763 đã bị phá.
- Không có luật quản lý: không chốt một phần, không dời BE, không đóng theo giờ. Giữ lệnh qua NY lunch và phiên chiều trong lúc đi ngủ.
- Ghi chép trộn bằng chứng ex-post (nến M15 10:15) vào lý do vào lệnh.

### Tâm lý khi vào lệnh

- _(điền: Bình tĩnh / FOMO / Sợ lỡ kèo / Revenge trade / Không chắc chắn)_
- Ghi chú:
  - Bạn tự nhận "không chắc đây có phải MSS tốt" → sự không chắc này lẽ ra phải dẫn tới No Trade hoặc size nhỏ hơn.

### Có tuân thủ plan không?

- **No**
- Nếu không, tôi đã phá rule nào?
  - Không có Context Note / H1 Handoff viết trước (v0.2 R2).
  - §21 Disqualifying: pool đối diện quan trọng hơn còn nguyên phía SL.
  - §26 / §33: MSS phá STH thay vì ITH M5 đã đánh dấu trước.
  - §31: R(T1) thực tế < 2.
  - [[ICT 2022 Entry Checklist]]: "1R → chốt 50% + dời SL về BE" — không áp dụng.

---

## 4. Phân Tích Sau Lệnh

- **Result**: Hit SL (~14:45 NY = 01:45 VN ngày 13/10)
- **Mistake chính**:
  - [[13-Mistake-Trading-Into-Unswept-Liquidity]] — SSL 30,554.6 cùng phía SL (first error: draw)
  - [[06-Mistake-Not-Have-Market-Structure-Shift]] — biến thể B: gọi nhầm cú phá swing vi mô là MSS
  - [[05-Mistake-Not-enough-RR]] — RR 3.66 trên giấy, RR thật tới vật cản đầu tiên 1.18
  - [[14-Mistake-No-Trade-Management-Round-Trip]] — MFE +2.47R → −1R
  - Liên quan: [[09-Mistake-Wrong-daily-bias]] (biến thể: đúng bias D1 nhưng đọc sai DOL trong ngày)
- **Nguyên nhân gốc rễ**:
  - Không có bước "định vị pool chưa bị lấy ở cả hai phía + đọc dòng chảy H1" trước khi mở khung thấp. Thấy sweep + displacement trên M1 nên đi tiếp.
- **Tại sao lệnh này thua?**
  - Đúng vùng, sai pool, sai xác nhận. Lệnh ngược dòng chảy H1 có nhịp hồi ngắn: nó dừng đúng ở cụm kháng cự rồi quay về.
  - Không có luật quản lý, nên +2.47R biến thành −1R.
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?** (đều biết trước lúc vào lệnh)
  - Đêm 11/10 quét BSL 31,036 rồi đảo xuống → hồ sơ ngày giảm.
  - 09:30 NY: displacement giảm phá PDL 30,763; 2 thân M15 đóng dưới (acceptance).
  - SSL ngoài 30,554.6 còn nguyên, cách entry ~110 điểm.
  - Cụm kháng cự phía trên: FVG giảm 30,706–30,722 · đỉnh nến 10:00 ≈30,750 · EQ nhịp NY ≈30,742 · PDL 30,763 · FVG giảm 30,780–30,813.
  - 11:45–12:00: râu lên 30,749 / 30,753 qua đỉnh nến 10:00, thân đóng lại ≈30,729 → quét BSL nội bộ, đúng lúc vào NY lunch (11:30–13:00 NY theo [[18-Kill-Zones]]).
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Lựa chọn 1 — Core: **không long** trước khi 30,554.6 bị quét + giá lấy lại mức trong killzone, hoặc trước khi có H1 MSS tăng. Sau đó tìm MSS M5 qua gốc nhịp vào sweep.
  - Lựa chọn 2 — scalp ngược dòng chảy (spec riêng, size ½): TP ≤ 30,705 (vật cản đầu tiên), hoặc chia 50% tại 30,705 + 50% tại 30,745. Đóng theo giờ lúc 12:00 NY. Không giữ khi đi ngủ.

> [!info] Ex-post — không dùng để chấm quyết định
> 19:00–20:00 NY, giá quét 30,554.6 xuống ~30,505. Điều này *nhất quán* với giả thuyết DOL = 30,554.6, nhưng một lần xảy ra không chứng minh được gì.

### Mô phỏng quản lý lệnh (một đường giá, có hindsight — minh họa, không dùng để chọn luật)

| Luật (giả định viết trước) | Kết quả |
|---|---|
| Như đã làm | −1.00R |
| Checklist: 50% tại +1R + dời BE | +0.50R |
| Thoát hết tại 30,705 (mép FVG giảm) | +1.14R |
| Thoát hết tại 30,745 (trước đỉnh nến 10:00) | +2.24R |
| Đóng theo giờ lúc 12:00 NY | +1.86R |
| 50% tại 30,705 + 50% tại 30,745 | +1.69R |

### Thang target (biết trước lúc vào lệnh)

| Mức | Nguồn gốc | R |
|---|---|---|
| 30,700 | +1R | 1.00 |
| 30,706.5–30,722 | FVG giảm M15 09:45–10:15 — **vật cản đầu tiên** | 1.18–1.61 |
| ≈30,742–30,746 | EQ nhịp NY (30,852 → đáy) | ≈2.15 |
| ≈30,750 | Đỉnh nến 10:00 = gốc nhịp vào sweep / BSL nội bộ | 2.33 |
| 30,763 | PDL (đã bị phá) | 2.74 |
| 30,780–30,813 | FVG giảm 09:15–09:45 | ≥ 3.2 |
| 30,796.3 | TP đã đặt (fib 0.705) — nằm **trong** FVG giảm | 3.66 |

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Vùng đúng ≠ pool đúng ≠ xác nhận đúng ≠ target đúng ≠ quản lý đúng.
- Bias D1 là chính sách cấp phép, không phải hướng lệnh trong ngày. Phải đọc DOL trong ngày + dòng chảy H1 trước.
- OTE chỉ đo trên nhịp impulse **cùng hướng** lệnh: đáy trước, đỉnh sau cho lệnh long.
- Mức MSS = gốc nhịp vào sweep (ITH M5), đánh dấu trước sweep. Swing M1 gần nhất không phải mức MSS.
- Target = thanh khoản, đặt trước PD array đối nghịch đầu tiên. R:R là kết quả, không phải đầu vào.
- Khi xác nhận đúng chuẩn (MSS M15 lúc 11:30) đến, R chỉ còn < 1 → bản thân hình học rủi ro của lệnh long này đã kém.

### Bài học tâm lý

- "Không chắc MSS có tốt không" là một tín hiệu: chuyển thành No Trade hoặc size nhỏ hơn, không chuyển thành hy vọng.
- Đi ngủ với lệnh mở và không có luật = giao kết quả cho may rủi.

### Rule cần thêm/cập nhật

- [ ] Draw gate: trước khi mở khung entry, ghi pool chưa bị lấy gần nhất ở **cả hai phía** + khoảng cách từ SL tới pool đối diện theo R (HEURISTIC: < 3R → loại)
- [ ] T-02: R tính tới min(T1, mép gần của FVG đối nghịch mới / PDH-PDL vừa bị phá đầu tiên)
- [ ] M-12: log `mss_leg_ratio` (phần trăm nhịp impulse được lấy lại); HEURISTIC ≥ 0.5
- [ ] MG-01 → MG-04 (xem [[14-Mistake-No-Trade-Management-Round-Trip]]): TP đặt sẵn, `management:` ghi trước, đóng theo giờ lúc 12:00 NY, không để rủi ro mở khi vắng mặt
- [ ] Tách cột ex-ante / ex-post trong trade note

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep — **và phân loại internal / external**
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone
- [ ] Viết Context Note D1 (bias, DOL, pool đối diện, invalidation) trước 08:30 NY
- [ ] Dùng M5 (không phải M1) cho MSS theo framework D1 → H1 → M5
- [ ] Liệt kê thang vật cản + R tới từng mức trước khi đặt TP
- [ ] Đóng theo giờ lúc 12:00 NY (23:00 VN khi EDT · 00:00 VN khi EST từ 1/11)
- [ ] Log `mfe_r`, `mae_r`, `time_of_mfe`, `first_obstacle_r` cho mọi lệnh
- [ ] Replay 40 ngày NDX: những ngày "quét BSL + phá PDL có acceptance" — đo nhịp hồi phiên sáng đi tới đâu (HYP-24)

---

## 7. Final Grade

_(chấm theo review; Psychology để bạn tự chấm)_

| Tiêu chí | Điểm |
|---|---|
| Daily Bias | 4/10 |
| POI Selection | 3/10 |
| Liquidity Sweep | 4/10 |
| MSS Confirmation | 3/10 |
| Entry Execution | 6/10 |
| Risk Management | 2/10 |
| Psychology | /10 |

**Overall Grade**: ~3.7/10 (6 tiêu chí đã chấm)

**Trade Quality**: D — bad loss. Kể cả nếu chạm TP, đây vẫn là một "bad win" về quy trình.

---

## 8. Liên kết

- Concepts: [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[15-Inducement]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[26-OTE-Optimal-Trade-Entry]] · [[12-Dealing-Range]] · [[59-Daily-Bias]] · [[18-Kill-Zones]] · [[33-Turtle-Soup]] · [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]]
- Model: [[01 - ICT 2022 Model]] · [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] · [[13 - Intraday Profiles]]
- Playbook: [[ICT 2022 Entry Checklist]] · [[ICT 2022 State Machine Gate Checklist]]
