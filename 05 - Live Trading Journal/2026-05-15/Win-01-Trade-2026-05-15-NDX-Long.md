---
date: 2026-05-15
symbol: NDX
position: Long
result: Win
session: New York
setup: NQ ICT 2022 AM Delivery
entry_model: Market Structure Shift + Sell-side Liquidity + Liquidity Sweep/Stop Hunt
entry_timeframe: 
higher_timeframe_bias: Bullish
bias_correct: 
entry_price: 29,368.1
take_profit: 29,420.6
stop_loss: 29,340.8
exit_price: 29,420.6
pnl: 105
r_multiple: 1.92
planned_rr: 1.92
risk_percent: 
confidence: 4
mistakes: 
emotions:
  - Disciplined
tags:
  - MarketStructureShift
  - SellSideLiquidity
  - LiquiditySweepStopHunt
  - OrderBlocks
  - FairValueGap
  - Displacement
  - PremiumVsDiscount
  - KillZones
  - OptimalTradeEntry
  - DailyBias
  - Discount
source_id: 2023
da_verdict: UNPROVEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 0, minor: 1}
da_opposite_case: undecidable from this evidence
---
# Trade 2026-05-15 - NDX Long Win

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Win |
| Session | New York |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Market Structure Shift + Sell-side Liquidity + Liquidity Sweep/Stop Hunt |
| HTF Bias | Bullish |
| Premium/Discount | Discount |
| Power of 3 | Manipulation |
| Confidence | 4/5 (High) |
| Entry | 29,368.1 |
| Stop Loss | 29,340.8 |
| Take Profit | 29,420.6 |
| Exit | 29,420.6 |
| PnL | 105.0 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-05-14 03:56:00 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: Bullish
- **Premium/Discount**: Discount
- **Power of 3 Phase**: Manipulation

================= D1 =================

- Daily bias: Bullish - Giá đang trong trend tăng
================= H1 =================

- H1 Bias: Giá trong nhịp hồi - Bearish
- Chờ giá retrace về các vùng PD Array và tìm setup Long lên
- Giá tạo 1 Order Block khung H1 từ phiên New York hôm trước
================= M15 =================

- Giá retrace về vùng OB H1
- Chờ giá xuyên qua OB -> ko vào lệnh ngay khi giá chạm
- Vào khung M1 tìm tín hiệu MSS
================= M1 =================

- Giá quét qua vùng 50% (mean threshold) của OB
- Giá bật lên tạo thành 1 MSS
- Đồng thời giá tạo FVG trên đường di chuyển displacement
- Chờ giá hồi về vùng FVG
- Entry khi giá bật lên sau khi fill 50% FVG

================= Result =================

- Giá đi đúng mô hình ICT 2022
- Chốt lời ở đỉnh cũ tỷ lệ 1:2R

### Charts

![[NDX-20260515-2023-1.png]]
![[NDX-20260515-2023-2.png]]
![[NDX-20260515-2023-3.png]]
![[NDX-20260515-2023-4.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Break of Structure (BOS) or Change of Character (CHOCH) confirmed
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Market Structure Shift + Displacement
- [x] Entry is within the Optimal Trade Entry (OTE) zone (62-79% fib)
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Clear liquidity target identified (buy-side or sell-side)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Rejection Validation When Enter PD Array Zones
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Partial take-profit levels are planned (1R, 2R, runner)
- [x] Risking no more than 0.5% of account equity
- [x] Not exceeding daily loss limit -- will stop trading if hit

---

## 3. Execution Review

- Giá đi đúng theo mô hình ICT
- Quan trọng là kiên nhẫn chờ setup

**Emotions**: Disciplined

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit)
- **Mistake chính**:
  - [[Mistake - ]]
- **Nguyên nhân gốc rễ**:
  - (không có dữ kiện trong file để điền — không suy diễn thêm)

---

## 5. Lesson Learned

### Bài học kỹ thuật

- (Bản gốc để trống. Bản `Win-01-Trade-2026-05-15-NDX.md` — cùng lệnh, template phong phú hơn — đã ghi: "Chốt lời từng phần" liên kết O2 tại file đó.)

### Bài học tâm lý

- (Bản gốc để trống. Xem file kia: "Kiên nhẫn chờ setup hình thành".)

### Bài học quy trình & risk

- **risk_percent trống** trong file này (khác với bản kia ghi rõ `5%` + mistake tag 07) — đây chính là khác biệt duy nhất giữa hai bản đáng lưu ý ở đây, không phải bổ sung phân tích trùng lặp. Không có gì trong bản này để kiểm tra risk% thật.
- Checklist ở đây tick "Risking no more than 0.5% of account equity" = `[x]` — nếu đây là CÙNG một lệnh với bản kia (risk 5%, mistake tag breach), thì tick này tự mâu thuẫn với sự thật đã ghi ở bản song song. Ghi nhận nhưng KHÔNG tính là objection riêng của file này — đã tính trong CS-O0′ (trích).

### Rule cần thêm/cập nhật

- [ ] Khi có hai bản ghi cho cùng một lệnh bằng hai template khác nhau, một trong hai PHẢI trỏ về bản kia (backlink) — điều kiện đo: field frontmatter `duplicate_of:` bắt buộc khi entry/SL/TP/pnl trùng tuyệt đối với file khác trong cùng ngày.

---

## 6. Action Items Cho Các Lệnh Sau

(Không có mục 6 trong bản gốc — giữ nguyên, không bổ sung.)

## 7. Final Grade

(Không có mục 7 trong bản gốc — giữ nguyên, không bổ sung.)

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Ghi chú trùng lệnh:** File này và `Win-01-Trade-2026-05-15-NDX.md` là **cùng một lệnh** — entry 29,368.1 / SL 29,340.8 / TP 29,420.6 / pnl 105 khớp tuyệt đối từng số (**CS-O0′ · [ARITHMETIC] · material**, trích từ cross-setup findings). Phân tích ĐẦY ĐỦ (thesis, load-bearing claim C1-C4, objections O1-O4, opposite case, falsification tests) đã thực hiện tại `Win-01-Trade-2026-05-15-NDX.md` — tham chiếu file đó để xem toàn bộ lập luận. Phần dưới đây CHỈ phản biện nội dung khác biệt giữa hai bản.

**Evidence base**: Prose + frontmatter only, không chart. Sufficiency: **thin** (giống bản kia).

**Khác biệt nội dung giữa hai bản** (đây là toàn bộ phạm vi phản biện riêng của file này):
1. `risk_percent` trống ở đây vs `5%` + mistake tag 07 ở bản kia.
2. Checklist ở đây dùng format "Yes/No" tiếng Anh đầy đủ 15 dòng (bao gồm cả "Risking no more than 0.5%" tick `[x]`) — bản kia dùng checklist tiếng Việt 13 dòng.
3. `entry_model` ở đây ghi "Market Structure Shift + Sell-side Liquidity + Liquidity Sweep/Stop Hunt" (cụ thể hơn) vs "ICT 2022 Model" (chung) ở bản kia.
4. Có 4 dòng link chart Obsidian (`NDX-20260515-2023-*.png`) — không tồn tại trong dataset, không đổi sufficiency nhưng xác nhận lại nguyên tắc cấm [CHART].
5. Section 4 và 5 ở bản này gần như trống hoàn toàn — bản kia có nội dung đầy hơn nhiều (đây chính là lý do bản kia được chọn phân tích đầy đủ theo brief).

**Objections** (chỉ trên phần khác biệt):

**O1 · [SELF-CONTRADICTION] · fatal · attacks tính nhất quán giữa hai bản**
Claim: checklist "Risking no more than 0.5% of account equity" = `[x]` (tick đạt chuẩn) ở bản này mô tả đúng thực tế risk của lệnh.
Fails: bản song song của CÙNG lệnh này (`Win-01-Trade-2026-05-15-NDX.md`) ghi `risk_percent: 5%` và tự gắn mistake tag 07 "Risk more than 0.5% total account". Một lệnh không thể vừa tick "đạt chuẩn ≤0.5%" vừa tự nhận breach 5% ở bản ghi khác của chính nó.
Consequence: tick checklist trong bản này không đáng tin cậy như một bản ghi độc lập của risk thật — nó có thể là tick mẫu/default chưa cập nhật theo thực tế, không phải xác nhận tại thời điểm entry.
Your best answer: "hai bản ghi hai thời điểm khác nhau, risk có thể thay đổi." — Không cứu được: entry/SL/TP/pnl giống tuyệt đối, không có gì gợi ý đây là hai sự kiện risk khác nhau.
Retracted by: xác nhận từ user rằng risk% đã thay đổi giữa hai lần ghi log của cùng một lệnh — hiện không có.

**Minor:**
- **O2 · [METHOD] · minor · attacks quy trình ghi log** — thiếu field `duplicate_of` hoặc backlink giữa hai bản khiến bất kỳ thống kê nào (win rate, expectancy) tính trên toàn bộ dataset có nguy cơ đếm lệnh này hai lần nếu không dedupe thủ công (đã dedupe đúng ở cross_setup_findings, N=25). Retracted by: thêm field liên kết hai file.

Drafted 3, cut 1 (một draft về khác biệt entry_model "cụ thể hơn" bị cắt vì không ảnh hưởng consequence — cả hai đều mô tả cùng chuỗi Sweep→MSS→FVG, chỉ khác mức chi tiết diễn đạt).

**Verdict: UNPROVEN.**
Evidence base thin (prose-only, không chart) khiến MSS/FVG/Displacement không kiểm được từ cả hai bản — giống hệt giới hạn đã nêu ở bản kia. Tôi tấn công riêng sự khác biệt giữa hai bản (risk% trống vs 5%, checklist tick 0.5% vs breach thật) và không phá được thành FAIL dứt điểm — chỉ có thể nêu tự mâu thuẫn (O1, fatal) chứng minh MỘT trong hai bản đang ghi sai risk thật.
Critique này KHÔNG xác lập: (1) bản nào giữa hai bản là "đúng" về risk% — chỉ nêu rằng ít nhất một trong hai sai; (2) toàn bộ phân tích thesis (MSS, Displacement, FVG) — đã xử lý đầy đủ ở file kia, không lặp lại ở đây.

## 9. Opposite Case (Counter-Argument)

Không dựng opposite case riêng cho file này — thesis kỹ thuật (MSS/Displacement/FVG) giống tuyệt đối với bản đã phân tích tại `Win-01-Trade-2026-05-15-NDX.md` mục 9. Tham chiếu file đó.

Strength label: **undecidable from this evidence** (áp dụng cho phần khác biệt risk% — không đủ dữ kiện để nói bản nào đúng).

Observable phân biệt: xác nhận log risk thật (broker/prop-firm) tại thời điểm entry của lệnh 29,368.1 — sẽ cho biết bản nào (risk% trống hay 5%) khớp thực tế.

## 10. Falsification Tests

1. **Test dedupe hệ thống** (đóng O2): rà toàn bộ dataset tìm cặp entry/SL/TP/pnl trùng tuyệt đối khác ngoài 2 cặp đã biết (05-13, 05-15) — nếu tìm thêm ≥1 cặp, cần quy trình dedupe chính thức trước khi tính bất kỳ thống kê nào.
2. **Test risk thật** (đóng O1, dùng chung với file kia): xác nhận từ log broker risk% thật của lệnh 29,368.1 ngày 05-15.
