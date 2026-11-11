---
date: 2026-04-20
symbol: NQ1
position: Long
result: Win
session: London
setup: NQ ICT 2022 AM Delivery
entry_model: Change of Character + Market Structure Shift + Sell-side Liquidity
entry_timeframe: 
higher_timeframe_bias: 
bias_correct: 
entry_price: 26,693.25
take_profit: 26,764
stop_loss: 26,672
exit_price: 26,764
pnl: 143
r_multiple: 3.33
planned_rr: 3.33
risk_percent: 
confidence: 4
mistakes: 
emotions:
  - Disciplined
tags:
  - ChangeOfCharacter
  - MarketStructureShift
  - SellSideLiquidity
  - FairValueGap
  - KillZones
  - PremiumVsDiscount
  - JudasSwing
source_id: 2010
da_verdict: SURVIVES, WEAKENED
da_evidence_sufficiency: thin
da_objections: {fatal: 0, material: 1, minor: 2}
da_opposite_case: "weaker but non-trivial"
---
# Trade 2026-04-20 - NQ1 Long Win

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NQ1 |
| Position | Long |
| Result | Win |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Change of Character + Market Structure Shift + Sell-side Liquidity |
| HTF Bias |  |
| Premium/Discount |  |
| Power of 3 |  |
| Confidence | 4/5 (High) |
| Entry | 26,693.25 |
| Stop Loss | 26,672 |
| Take Profit | 26,764 |
| Exit | 26,764 |
| PnL | 143.0 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-04-20 01:02:46 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: N/A
- **Premium/Discount**: N/A
- **Power of 3 Phase**: N/A

============= D1 ==============

- Daily bias: Bullish
- Giá vẫn đang trong trend tăn mạnh với 1 series nến xanh liên tiếp
- Giá mở cửa tạo 1 khoản GAP lớn ( giá có thể quay lại lắp đầy GAP này )
- => Chờ setup Long
============= H1 ==============

- Phiên Á giá đi ngang (consolidate)
- Giá quét thanh khoản 1 đáy cũ sau đó tăng lại
- Phiên London mở cửa, giá tạo 1 Judas Swing đầy giá xuống dưới quét thanh khoản đáy cũ, giá tạo dâu nến dài
============= M15 ==============

- Sau khi quét thanh khoản giá bật quay ngược lại tạo displacement + FVG trên đường giá di chuyển
- Chờ giá retrace về FVG vừa tạo
============= M5 ==============

- Giá retrace về FVG lúc 17:00 => quan sát có rejection không
- Xuất hiện tín hiệu rejection khi giá chạm cạnh trên FVG
- Vào lệnh long

Target: trước khi giá tạo GAP, giá đã có 1 vùng consolidation với nhiều đáy gần ngang nhau. Target tới những đáy này (50% GAP) - **26764.65**

Stoploss: **26,672.00**, đặt ở cạnh dưới FVG + buffer (tránh giá quét stoploss)

Notes: đã vào lệnh khi giá chạm vào Cạnh trên FVG khi xuất hiện dấu hiệu rejection.
Suggestion: Xuống khung M1 để tối ưu điểm vào lệnh, hoạch chờ giá retrace về Mean Threshold (50%) và reject

### Charts

![[NQ1-20260420-2010-1.png]]
![[NQ1-20260420-2010-2.png]]
![[NQ1-20260420-2010-3.png]]
![[NQ1-20260420-2010-4.png]]
![[NQ1-20260420-2010-5.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Break of Structure (BOS) or Change of Character (CHOCH) confirmed
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Market Structure Shift + Displacement
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Clear liquidity target identified (buy-side or sell-side)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Risking no more than 0.5% of account equity
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Risk-to-reward ratio is at least 1:3 (ICT standard)
- [x] Partial take-profit levels are planned (1R, 2R, runner)
- [x] Not exceeding daily loss limit -- will stop trading if hit
- [x] Rejection Validation When Enter PD Array Zones

---

## 3. Execution Review

Giá di chuyển về lắp GAP

**Emotions**: Disciplined

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit) — *khớp dữ kiện: exit_price (26,764) = take_profit field (26,764), khác với 2 file trước trong batch này (04-01, 04-02) nơi nhãn "Hit TP" không khớp exit thực tế.*
- **Mistake chính**:
  - [[Mistake - ]] *(trống — không có mistake nào để gắn dựa trên dữ kiện có trong file; không suy diễn thêm)*
- **Nguyên nhân gốc rễ** *(suy luận có điều kiện — cần chart xác nhận)*:
  - Theo Execution Review (chỉ 1 câu): "Giá di chuyển về lắp GAP" — khớp với target đã định trước ("giá có thể quay lại lắp đầy GAP này", mục 1, D1). Đây là trường hợp hiếm trong batch nơi kế hoạch (target = đáy consolidation trước GAP) và kết quả thực tế (exit = TP) khớp nhau hoàn toàn về số.

---

## 5. Lesson Learned

**Bài học kỹ thuật** (liên kết O1)
- Đây là lệnh có checklist đầy nhất trong 5 file batch này (15/15 tick, bao gồm cả "RR ≥ 1:3" — điều không xuất hiện ở các checklist khác) và cũng là lệnh duy nhất có TP field khớp chính xác với exit_price — không có lệnh nào khác trong batch 5 file này đạt cả hai điều kiện đồng thời.
- Tuy vậy, bước MSS/CHOCH (load-bearing của toàn bộ entry) vẫn được mô tả bằng lời, không kèm giá cụ thể cho swing bị phá — giống pattern đã thấy ở 04-02 (O3 file đó): "giá tạo 1 Judas Swing đẩy giá xuống dưới quét thanh khoản đáy cũ" không nêu mức giá đáy cũ đó là bao nhiêu.

**Bài học tâm lý**
- Execution Review chỉ 1 câu ngắn, không mô tả trạng thái tâm lý trong khi giữ lệnh (khác 04-01, 04-02 có mô tả chi tiết cảm xúc lúc đóng lệnh) — thiếu dữ kiện để đánh giá liệu "Disciplined" (emotions field) có phản ánh đúng một quá trình giữ lệnh không dao động, hay chỉ đơn giản vì lệnh đóng nhanh & thuận nên không có gì để dao động.

**Bài học quy trình & risk**
- Field `risk_percent`, `r_multiple`, `planned_rr` ở bảng mục 0 để trống dù frontmatter có đủ (`r_multiple: 3.33`, `planned_rr: 3.33`) — không đổi kết luận nhưng là cùng lỗi copy-bảng-không-đồng-bộ-frontmatter thấy ở toàn bộ 5 file batch này.

**Rule cần thêm/cập nhật**
- Rule kiểm tra được: khi mô tả "Judas Swing quét thanh khoản đáy cũ" làm cơ sở CHOCH/MSS, phải kèm giá cụ thể của "đáy cũ" đó — không có số thì không tick "BOS/CHOCH confirmed" (liên kết O1).
- Rule kiểm tra được: mọi bảng mục 0 (Trade Summary) phải copy tự động từ frontmatter, không để trống thủ công khi frontmatter đã có giá trị — tránh sai lệch tra cứu khi đọc riêng bảng mà không đọc frontmatter.

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, 5 chart Obsidian không đọc được. Sufficiency: **thin** — nhưng đây là file có mô tả đa-timeframe (D1→H1→M15→M5) chi tiết nhất trong 5 file batch, với 2 mức giá cụ thể (target 26,764.65 và SL 26,672.00) — chỉ thiếu giá cụ thể duy nhất ở bước MSS/CHOCH (đáy cũ bị quét).

**Thesis & claims**:
- C1: D1 bias bullish, trong trend tăng mạnh, có gap cần lấp — cơ sở toàn bộ hướng long.
- C2: H1 — Á giá consolidate, London mở cửa tạo Judas Swing quét thanh khoản đáy cũ (chưa nêu giá), tạo râu nến dài.
- C3 (load-bearing): M15 — sau sweep, giá tạo displacement + FVG; entry M5 tại rejection cạnh trên FVG (26,693.25) — chuỗi CHOCH+MSS+sweep+FVG+rejection đầy đủ theo checklist 15/15.
- C4: Target = 50% GAP tại vùng đáy consolidation trước gap (26,764.65 ≈ TP field 26,764) — target có cơ sở structure cụ thể (không phải số tròn tuỳ ý).
- C5: SL = cạnh dưới FVG + buffer (26,672.00) — có cơ sở PD array cụ thể.
- Suy luận: C1+C2+C3 → entry hợp lệ với RR 3.33 → C4 (target đạt) → Win đúng theo kế hoạch, không lệch giữa Result label và exit thực tế (khác 2 file trước trong batch).

**Điều gì đứng vững**:
- Result label khớp hoàn toàn với dữ kiện số: exit_price = TP field = 26,764 — không có mâu thuẫn self-contradiction nào ở đây, khác 04-01 và 04-02.
- Arithmetic RR: risk = |26,693.25−26,672| = 21.25; reward = |26,764−26,693.25| = 70.75; RR = 70.75/21.25 = 3.329 ≈ planned_rr/r_multiple field 3.33 — khớp cả hai chiều (kế hoạch và thực nhận giống nhau vì Hit TP đúng nghĩa).
- Cả target (26,764.65, dựa trên đáy consolidation trước gap) và SL (26,672, dựa trên cạnh dưới FVG + buffer) đều có cơ sở PD array cụ thể được nêu tên trong mục 1 — không phải số tròn chọn tuỳ ý, đây là điểm khác biệt tích cực so với GBPUSD 06-17 trong cross-setup findings (CS-O5, SL siết không có cơ sở).
- Risk-to-reward ≥1:3 được tick rõ và đạt đúng — không như 3 lệnh RR thấp trong CS-O6 (0.6, 0.89, 1.04) tick unchecked nhưng vẫn Win.

**Objections**:

**O1 · [UNSUPPORTED] · material · attacks C3 (load-bearing)**
Claim: checklist tick "Break of Structure (BOS) or Change of Character (CHOCH) confirmed" và "Market Structure Shift + Displacement" cho chuỗi H1 "Judas Swing quét thanh khoản đáy cũ".
Fails: mô tả H1 chỉ nói "giá quét thanh khoản 1 đáy cũ sau đó tăng lại" và "tạo 1 Judas Swing đẩy giá xuống dưới quét thanh khoản đáy cũ" — không nêu giá cụ thể của "đáy cũ" này ở đâu, trong khi target (26,764.65) và SL (26,672.00) đều có số cụ thể. Đây là bước duy nhất trong toàn chuỗi 4-timeframe thiếu giá — và đây chính là bước MSS/CHOCH, tức load-bearing claim của toàn bộ entry.
Evidence: không có số giá nào cho "đáy cũ" trong toàn mục 1; đối chiếu với 2 mức giá cụ thể khác (target, SL) cùng xuất hiện trong văn bản.
Consequence: nếu "đáy cũ" đó thực chất là một swing nhỏ, không structurally significant (theo doctrine, "structurally significant" yêu cầu swing đủ ý nghĩa trong cấu trúc, không phải mọi đáy nhỏ), thì CHOCH/MSS được tick có thể là overcall một internal pullback thành reversal signal — không kiểm được từ file.
Your best answer: "Target và SL đều đúng, nên MSS chắc cũng đúng — nếu không thì Win không giải thích được." — Không cứu được: đây chính là outcome-as-evidence bị brief cấm rõ (mode REVIEW) — Win không chứng minh MSS đã xảy ra đúng, có thể giá đơn giản đi đúng hướng D1 bias (bullish, đang lấp gap) độc lập với việc MSS tại H1 có chuẩn hay không.
Retracted by: chart H1 gốc cho thấy giá cụ thể của đáy cũ bị quét và xác nhận đây là một swing có ý nghĩa cấu trúc (không phải nhiễu nhỏ) — hiện không có.

**O2 · [DOCTRINE] · minor**
"Price is in a premium zone (shorts) or discount zone (longs)" tick `[x]` nhưng không có mô tả dealing range nào (không nêu swing-to-swing range, không nêu midpoint) để tính premium/discount — chỉ có target dựa trên "50% GAP" (khác khái niệm với 50% dealing range trong doctrine premium/discount). Hai khái niệm "50%" khác nhau (50% của GAP vs midpoint của dealing range) có thể đang bị dùng lẫn. Retracted by: mô tả dealing range cụ thể (swing cao/thấp dùng để tính premium/discount) — hiện không có, chỉ có "50% GAP".

**O3 · [ARITHMETIC] · minor**
Target text nêu "26764.65" nhưng TP field = 26,764 — chênh 0.65 điểm, khả năng do rounding, không ảnh hưởng RR (3.329 vs 3.33 làm tròn khớp cả hai). Retracted by: không cần — chênh lệch quá nhỏ để đổi kết luận, chỉ nêu vì brief yêu cầu soi arithmetic outcome vs pnl.

Drafted 4, cut 1 (một draft về "consolidation trước GAP có thực sự tạo ra level 26764.65 hay đó là số chọn ngược từ TP đã biết" bị cắt vì không phân biệt được với hindsight thường — target được nêu *trước* Execution Review, cùng lúc với kế hoạch, không phải hồi tố).

**Verdict: SURVIVES, WEAKENED.**
Load-bearing claim C3 không FAIL, nhưng O1 hạ nó xuống UNSUPPORTED ở đúng bước quan trọng nhất (CHOCH/MSS thiếu giá). Đây là file có evidence tốt nhất trong batch 5 (target và SL đều có cơ sở PD array cụ thể, Result label khớp chính xác dữ kiện số) nhưng vẫn không đạt "full" vì thiếu đúng một mắt xích.

Tôi đã tấn công: cơ sở CHOCH/MSS, khái niệm premium/discount, arithmetic target — arithmetic RR và Result label không bị phá, đây là 2 điểm mạnh thật của file này so với các file khác trong batch.

Critique này KHÔNG xác lập: (1) rằng MSS/CHOCH chắc chắn sai — chỉ nói chưa đủ evidence để PASS; (2) rằng lệnh này "đáng" Win nhờ may rủi — ngược lại, đây là file có nhiều dấu hiệu process tốt nhất trong batch, nhưng process tốt không đồng nghĩa mọi claim đều verified.

---

## 9. Opposite Case (Counter-Argument)

Đổi narrative role: điều gì nếu "Judas Swing quét thanh khoản đáy cũ" tại H1 không phải là một sweep dẫn tới MSS thật, mà chỉ là **một nhịp điều chỉnh bình thường trong trend tăng D1** — và giá đơn giản tiếp tục trend tăng đã có từ trước (D1 bullish, "series nến xanh liên tiếp") mà không cần bất kỳ MSS/CHOCH nào tại H1 để giải thích move lên sau đó?

Load-bearing claim của kèo ngược: move tăng sau "Judas Swing" là continuation của trend D1 đã tồn tại từ trước (không phải reversal cần MSS xác nhận), nên "MSS" được gọi tên ở đây thực chất là một cách gọi tên lại một pullback-and-continue bình thường.

Strongest self-objection (tự đánh kèo ngược): mục 1 mô tả rõ trình tự "giá quét thanh khoản 1 đáy cũ sau đó tăng lại" và "phiên London mở cửa, giá tạo 1 Judas Swing đẩy giá xuống dưới quét thanh khoản đáy cũ, giá tạo dâu nến dài" — mô tả một wick dài (rejection rõ) ngay sau sweep, đúng pattern Judas Swing chuẩn (một sweep giả hướng đối lập trend chính trước khi tiếp diễn) — đây là cách đọc *phù hợp với chính thesis gốc* (Judas Swing là một dạng liquidity grab trong trend, không mâu thuẫn với continuation). Kèo ngược ở đây thực ra không thực sự "ngược" — nó gần như là một cách diễn giải khác của cùng cơ chế (Judas Swing = internal liquidity grab trong continuation, không cần là reversal MSS thật).
Vì kèo ngược tự nó không tạo ra một load-bearing claim khác biệt rõ với thesis gốc (cả hai đều dẫn tới long), sức nặng của nó thấp.

Strength label: **weaker but non-trivial**. Không có fact nào mà thesis gốc không giải thích được — sự khác biệt chỉ là tên gọi (MSS reversal thật vs continuation-pullback có Judas Swing) trong khi hướng giao dịch (long) không đổi ở cả hai reading. Nếu có giá cụ thể của "đáy cũ" cho thấy đó là một swing nhỏ không đáng kể trong cấu trúc lớn, kèo ngược ("chỉ là pullback, gọi MSS là overcall") sẽ sống mạnh hơn.

Observable duy nhất phân biệt hai reading: liệu "đáy cũ" bị quét có phải là một swing low structurally significant trong cấu trúc H1 (đủ để một break qua nó tính là MSS reversal) hay chỉ là một đáy nhỏ nội bộ trong nhịp điều chỉnh của trend tăng lớn hơn — quyết định này cần giá cụ thể của swing đó, hiện không có trong file.

---

## 10. Falsification Tests

**Test 1** — Thu thập chart H1 gốc quanh phiên Á/London 2026-04-20 để lấy giá cụ thể của "đáy cũ" bị Judas Swing quét, và xác định liệu swing đó có structurally significant trong cấu trúc H1 lớn hơn. Nếu có, O1 được retract (MSS supported); nếu chỉ là nhiễu nhỏ, O1 giữ nguyên và note thêm rằng đây có thể là continuation được gọi tên MSS. Đóng: O1.

**Test 2** — Đối chiếu tất cả các lệnh trong sample có target dựa trên "lắp GAP" hoặc mức consolidation cụ thể trước gap (nếu có lệnh khác cùng cấu trúc) — xem tỷ lệ đạt target đúng của nhóm "target có cơ sở PD array cụ thể" so với nhóm "target là số tròn không giải thích". Nếu nhóm có cơ sở cụ thể đạt target cao hơn rõ rệt, đây là evidence ủng hộ giá trị của việc nêu structure cụ thể khi đặt target — không đóng objection nào cụ thể, chỉ là test bổ trợ cho lesson kỹ thuật.

**Test 3** — Kiểm định nghĩa "50% GAP" trong toàn bộ journal (có bao nhiêu lệnh khác dùng đúng khái niệm này) để xác định liệu đây là một khái niệm riêng khác với "premium/discount midpoint" hay đang bị dùng lẫn (O2). Nếu luôn tách biệt rõ trong các lệnh khác, O2 được narrow xuống chỉ là ghi chú thuật ngữ, không phải nhầm lẫn khái niệm. Đóng: O2.
