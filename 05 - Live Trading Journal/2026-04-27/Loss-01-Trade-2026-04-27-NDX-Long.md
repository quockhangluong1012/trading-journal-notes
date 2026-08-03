---
date: 2026-04-27
symbol: NDX
position: Long
result: Loss
session: London
setup: NQ ICT 2022 AM Delivery
entry_model: Sell-side Liquidity + Order Blocks + Fair Value Gap
entry_timeframe: 
higher_timeframe_bias: 
bias_correct: 
entry_price: 27,263.4
take_profit: 27,427
stop_loss: 27,212.8
exit_price: 27,195.8
pnl: -67.6
r_multiple: -1.34
planned_rr: 3.23
risk_percent: 
confidence: 4
mistakes: 
emotions:
  - Greedy
  - Confident
tags:
  - SellSideLiquidity
  - OrderBlocks
  - FairValueGap
  - KillZones
  - PremiumVsDiscount
  - Displacement
  - JudasSwing
  - DailyBias
source_id: 2011
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 2, material: 1, minor: 0}
da_opposite_case: weaker but non-trivial
---
# Trade 2026-04-27 - NDX Long Loss

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Loss |
| Session | London |
| Setup | NQ ICT 2022 AM Delivery |
| Entry Model | Sell-side Liquidity + Order Blocks + Fair Value Gap |
| HTF Bias |  |
| Premium/Discount |  |
| Power of 3 |  |
| Confidence | 4/5 (High) |
| Entry | 27,263.4 |
| Stop Loss | 27,212.8 |
| Take Profit | 27,427 |
| Exit | 27,195.8 |
| PnL | -67.6 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-04-27 06:21:39 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: N/A
- **Premium/Discount**: N/A
- **Power of 3 Phase**: N/A

============= D1 =============

- Daily bias: Bullish (giá vẫn đang trong trend tăng mạnh)
- Có Market Structure Shift trên khung ngày
============= H1 =============

- Giá retrace về OB trên khung H1 kèm với 1 Judas Swing
- Giá tạo bóng nến dài, giá đang giảm và quét thanh khoản sau đó đóng nến tăng

- Tuy nhiên giá chưa quét swing low cũ

============= M15 =============

- Giá tăng mạnh sau khi chạm OB, kèm với displacement + FVG
- Vào setup long
- Stoploss: 27,227
- Target: 27404
- RR: 1:5.61

- Tỷ lệ RR quá cao cho 1 setup chưa quét hết đáy cũ

============= M5 =============

- Chưa phân tích khung M5 để tìm entry tối ưu

============= Result =============

- Giá quay về lắp FVG (tạo ra trên đường giá di chuyển khi tạo Judas Swing khi phiên London mở cửa)
- Leason Learn:

- Cẩn thận khi giá chưa quét hết đáy cũ
- Giá quay về các PD Arrays, cần xem xét tính hiệu đảo chiều và chốt lời
- Giá quay về FVG, tỷ lệ RR đã là 1:2.63. Tỷ lệ đã đủ tốt để chốt lời => tuy nhiên do **tham **nên vẫn để giá chạy đến đỉnh cũ (1:5.61 RR), tỷ lệ RR đỉnh cũ quá cao

### Charts

![[NDX-20260427-2011-1.png]]
![[NDX-20260427-2011-2.png]]
![[NDX-20260427-2011-3.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Market Structure Shift + Displacement
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Break of Structure (BOS) or Change of Character (CHOCH) confirmed
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Clear liquidity target identified (buy-side or sell-side)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Not exceeding daily loss limit -- will stop trading if hit

---

## 3. Execution Review

- Hit stop loss sau khi không chốt lời ở FVG mà để giá chạy đến đỉnh cũ
- Giá chạm 50% FVG và đã chiều quét stoploss
- Lệnh thất bại do lòng tham, chưa phân tích kỹ các yếu tố ban đầu

**Emotions**: Greedy, Confident

---

## 4. Phân Tích Sau Lệnh

- **Result**: Loss (Hit Stop Loss)
- **Mistake chính**:
  - [[Mistake - ]] *(trống trong bản gốc — dựa trên nội dung mục 1 và 3, mistake phù hợp nhất là "chưa quét hết swing low cũ trước khi entry" + "không chốt lời tại FVG khi RR đã đạt 1:2.63" (suy luận có điều kiện — cần chart xác nhận vì không có screenshot trong dataset))*
- **Nguyên nhân gốc rễ**:
  - *(trống trong bản gốc)* Hai nguyên nhân tự nêu trong mục 1/3: (a) vào lệnh khi "chưa quét hết đáy cũ" — tự nhận ngay trong lúc phân tích ("Tỷ lệ RR quá cao cho 1 setup chưa quét hết đáy cũ"), nghĩa là user đã thấy rủi ro NHƯNG vẫn entry; (b) không chốt lời khi giá chạm FVG (RR thực tế đã đạt 1:2.63) mà để giá chạy tới đỉnh cũ (RR kế hoạch 1:5.61) do lòng tham — đây là quản lý lệnh sau entry, không phải lỗi tại điểm entry *(suy luận có điều kiện — cần chart xác nhận vị trí FVG/đỉnh cũ)*.

---

## 5. Lesson Learned

**Bài học kỹ thuật**
- Setup long được vào khi tự thân narrative đã ghi nhận "giá chưa quét swing low cũ" — nghĩa là DOL (draw on liquidity) phía dưới entry chưa được thỏa mãn trước khi user coi Judas Swing + OB + FVG là đủ điều kiện đảo chiều. Liên kết O2 (load-bearing, [DOCTRINE] fatal).
- RR kế hoạch 1:5.61 (M15) không khớp với RR frontmatter 1:3.23 (entry 27,263.4 / SL 27,212.8 / TP 27,427) — hai con số RR khác nhau cho cùng một lệnh, không rõ cái nào được dùng để quyết định size. Liên kết O1 ([ARITHMETIC] fatal).

**Bài học tâm lý**
- Tự nhận "tham" (Greedy) là nguyên nhân không chốt lời tại điểm RR 1:2.63 đã đủ tốt theo tự đánh giá của chính user — đây là claim tâm lý hợp lệ về sau (post-hoc), không đổi được nhãn Loss/thiếu invalidation tại thời điểm entry. Liên kết O3.
- Confidence tự chấm 4/5 (High) đồng thời với emotion "Confident" + "Greedy" trên một setup mà chính narrative tự nêu rủi ro (chưa quét đáy cũ) — độ tự tin không tương xứng với chất lượng evidence đã tự mô tả.

**Bài học quy trình & risk**
- `risk_percent` để trống — không thể kiểm lệnh này có tuân 0.5% rule hay không (đối chiếu CS-O1: 8/25 lệnh toàn sample risk 5%, nhưng field này rỗng nên không xếp vào nhóm đó hay nhóm 0.5%). Đây là data gap, không phải finding kết luận được.
- `higher_timeframe_bias` và `bias_correct` đều trống trong frontmatter dù mục 1 khẳng định "Daily bias: Bullish" — thiếu chuẩn hóa field, làm bảng rule-drift bias TF (mục 2, cross_setup) không thể đối chiếu lệnh này.

**Rule cần thêm/cập nhật** *(mỗi rule = điều kiện đo lường được)*
- Rule 1: Không entry long nếu narrative pre-trade tự ghi nhận "chưa quét hết đáy cũ/swing low quan trọng phía dưới entry" — điều kiện đo: tồn tại câu văn tự mâu thuẫn giữa nhận định rủi ro và hành động entry trong cùng file. Liên kết O2.
- Rule 2: Khi hai giá trị RR khác nhau cùng xuất hiện trong một file (narrative M15 vs frontmatter), phải ghi rõ RR nào dùng để tính size trước khi entry — điều kiện đo: field `planned_rr` phải khớp số trong narrative, sai lệch >5% phải có ghi chú giải thích. Liên kết O1.
- Rule 3: Định nghĩa trước ngưỡng chốt lời từng phần (partial TP) tại RR cụ thể (ví dụ 1:2) độc lập với cảm giác "đủ tốt" tại thời điểm giữ lệnh — điều kiện đo: có price/RR level ghi trước entry, không viết sau khi đã thấy kết quả. Liên kết O3.

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, không có screenshot chart nào khả dụng (link `![[...]]` là Obsidian embed không tồn tại trong dataset) → cấm tier [CHART]. Mọi "MSS", "Judas Swing", "OB", "FVG", "displacement" nêu trong file là **claim của user**, không phải evidence đã xác nhận. Sufficiency: **thin** — load-bearing claim (liquidity sweep đã đủ điều kiện chưa) không thể kiểm ngoài lời tự thuật, và chính lời tự thuật đã tự mâu thuẫn (xem C3).

**Thesis & claims**:
- C1: D1 bias bullish + có MSS trên D1 → khung lớn hỗ trợ long.
- C2: H1 có Judas Swing + quét thanh khoản (wick dài) + đóng nến tăng tại OB → tín hiệu đảo chiều H1 hợp lệ, NHƯNG "giá chưa quét swing low cũ" (tự ghi nhận ngay trong C2).
- C3: M15 có displacement + FVG sau khi chạm OB → xác nhận entry long. **Load-bearing**: C3 phụ thuộc C2 đã đủ điều kiện; nhưng chính C2 tự phủ nhận điều đó ("Tỷ lệ RR quá cao cho 1 setup chưa quét hết đáy cũ" — câu này nằm ngay dưới phần lý do vào lệnh, viết TRƯỚC khi biết kết quả theo cấu trúc file).
- C4 (hệ quả C1-C3): Entry long tại 27,263.4, SL 27,212.8, TP 27,427 là quyết định có cơ sở đầy đủ theo ICT 2022 model.
- C5: Nguyên nhân thua là do "lòng tham" không chốt lời sớm tại FVG (RR 1:2.63) — tách biệt khỏi câu hỏi entry có hợp lệ hay không.

**Điều gì đứng vững**: Cấu trúc timeframe nesting D1→H1→M15 được trình bày đúng thứ tự (không nhảy TF), và checklist tick đủ 11/11 khớp với các mục claim nêu trong narrative (không có tick unchecked mâu thuẫn với văn bản, khác với case CS-O9 trong cross-setup). Việc user tự nhận lòng tham gây giữ lệnh quá lâu (C5) là một quan sát tự phê hợp lý, không cần phản biện.

**Objections**:

**O1 · [ARITHMETIC] · fatal · attacks C4**
Claim: RR kế hoạch của lệnh là 1:3.23 (frontmatter `planned_rr: 3.23`, khớp entry/SL/TP: risk 50.6 điểm, reward 163.6 điểm → 3.233).
Fails: narrative M15 (mục 1) nêu một bộ số khác — "Stoploss: 27,227 / Target: 27404 / RR: 1:5.61" — risk 36.4 điểm, reward 140.6 điểm → 3.86, KHÔNG khớp cả với 5.61 nêu trong narrative lẫn với 3.23 frontmatter. Ba con số RR (5.61 tự ghi, 3.86 tính lại từ SL/TP tự ghi, 3.23 frontmatter) không đồng nhất cho cùng một lệnh.
Evidence: tính tay — (27,404-27,263.4)/(27,263.4-27,227) = 140.6/36.4 = 3.86, không phải 5.61 như narrative tự ghi; frontmatter dùng SL/TP khác (27,212.8 / 27,427) cho ra 3.23.
Consequence: không rõ SL/TP thật sự dùng để size lệnh là bộ nào — nếu SL thật là 27,227 (sát hơn), risk thật khi entry có thể khác con số dùng để tính pnl/r_multiple đã log. Điều này làm r_multiple -1.34 đã ghi trong frontmatter không kiểm chứng được là tính trên SL nào.
Your best answer: "27,227 chỉ là mức dự kiến ban đầu, SL thật đã dời sang 27,212.8 trước khi entry." — Có thể đúng, nhưng file không ghi nhận việc dời SL này ở đâu cả; nếu đúng thì đây là một quyết định quản lý risk quan trọng bị thiếu log, tự nó là một gap quy trình khác.
Retracted by: một dòng ghi chú xác nhận SL đã được dời từ 27,227 sang 27,212.8 trước lúc entry (hiện không có trong file).

**O2 · [SELF-CONTRADICTION] · fatal · attacks C2, C3 (load-bearing)**
Claim: setup H1/M15 (Judas Swing + quét thanh khoản + OB + FVG) đủ điều kiện xác nhận đảo chiều để entry long.
Fails: ngay trong phần lý do entry (mục 1, dưới M15), user tự viết "Tỷ lệ RR quá cao cho 1 setup chưa quét hết đáy cũ" — đây là một cảnh báo tự nhận về thiếu sót cấu trúc (swing low cũ chưa bị quét), xuất hiện TRƯỚC phần "Result", nghĩa là nó không phải hindsight sau khi biết thua — nó là một nghi ngờ đã có tại thời điểm phân tích nhưng bị bỏ qua khi entry.
Evidence: quote trực tiếp mục 1: "- Tuy nhiên giá chưa quét swing low cũ" (dưới H1) và "- Tỷ lệ RR quá cao cho 1 setup chưa quét hết đáy cũ" (dưới M15) — cả hai câu đứng cùng khối với lý do entry, không phải trong khối "Result"/lesson learned.
Consequence: load-bearing claim của cả thesis (setup đủ điều kiện đảo chiều) tự mang một điều kiện chưa thỏa (chưa quét đáy cũ) do chính user xác nhận — đây không phải một finding cần dựng lại từ chart, nó nằm ngay trong văn bản gốc.
Your best answer: "Judas Swing + OB + FVG trên H1/M15 vẫn là đủ điều kiện entry mà không cần chờ quét đáy cũ, vì đó là hai cơ chế xác nhận độc lập." — Có thể đúng theo một số biến thể diễn giải ICT, nhưng chính user đặt câu "tuy nhiên" ngay sau, tức là bản thân user KHÔNG coi hai điều kiện đó là độc lập/đủ tại thời điểm phân tích — mâu thuẫn là với chính tiêu chuẩn user tự áp, không phải với một tiêu chuẩn ngoài áp vào.
Retracted by: một câu xác nhận rằng "chưa quét đáy cũ" chỉ là quan sát phụ, không phải điều kiện invalidation user tự đặt ra cho setup này — hiện văn bản đọc ngược lại.

**O3 · [HINDSIGHT] · material · attacks C5**
Claim: nguyên nhân thua là "lòng tham" không chốt lời tại FVG khi RR đã đạt 1:2.63.
Fails: câu "Tỷ lệ RR đã là 1:2.63. Tỷ lệ đã đủ tốt để chốt lời" là một tiêu chuẩn được phát biểu SAU khi đã biết giá đảo chiều và quét SL — không có ghi nhận nào trong phần Pre-market/Setup rằng 1:2.63 là ngưỡng partial-TP đã định trước lúc entry.
Evidence: mục "Result" (nơi câu này xuất hiện) nằm sau phần mô tả giá đã quay đầu và lấp FVG — đúng cấu trúc REVIEW mode, tiêu chuẩn "đủ tốt" được suy ra từ biết kết quả, không phải từ một rule đã viết trước.
Consequence: "lòng tham" là nhãn tâm lý hợp lý để ghi nhận CHO MỤC ĐÍCH HỌC, nhưng không thể dùng để khẳng định "nếu không tham thì đã lãi" — vì ngưỡng 1:2.63 chỉ trở thành "đủ tốt" sau khi nhìn thấy giá đảo chiều đúng tại đó; một lần khác giá có thể tiếp tục chạy qua FVG mà không đảo chiều, và cùng hành vi "giữ lệnh" đó sẽ được ghi là "kỷ luật" chứ không phải "tham".
Your best answer: không có phản hồi nào cứu được claim này thành non-hindsight, vì file không có ghi chú TP từng phần định trước entry — chính lesson gốc "Follow rules đã đề ra" (tương tự case khác trong sample) hàm ý CHƯA có rule bằng văn bản để follow tại thời điểm này.
Retracted by: một dòng trong mục Pre-market Bias ghi rõ kế hoạch partial TP tại RR cụ thể trước khi entry — hiện không có.

Drafted 4, cut 1 (một draft về "confidence 4/5 không tương xứng" bị cắt vì không đổi kết luận verdict, đã gộp vào bullet tâm lý ở mục 5 thay vì đứng riêng thành objection).

**Verdict: BROKEN.** Load-bearing claim C2/C3 (setup H1/M15 đủ điều kiện đảo chiều) tự mâu thuẫn ngay trong văn bản gốc (O2, fatal) — cùng lúc RR dùng để tính risk/size không xác định được vì ba con số khác nhau cho cùng lệnh (O1, fatal). Tôi đã tấn công nhưng không phá được: (a) trình tự timeframe D1→H1→M15 đúng thứ tự, không có bằng chứng nhảy cóc; (b) 11/11 checklist tick không mâu thuẫn với narrative (khác pattern CS-O9). Critique này KHÔNG xác lập: (1) liệu Judas Swing/OB/FVG có thật trên chart hay không — không có ảnh để kiểm; (2) liệu nếu SL thật là 27,212.8 (không phải 27,227) thì setup có "tốt hơn" — chỉ nêu là con số không nhất quán.

---

## 9. Opposite Case (Counter-Argument)

Đổi vai trò cùng fact: câu "chưa quét hết đáy cũ" (mà thesis gốc coi là nhược điểm bị bỏ qua) có thể đọc thành **DOL còn nguyên phía dưới, nghĩa là buy-side liquidity phía trên (đỉnh cũ 27,404/27,427) mới là target hợp lý, và Judas Swing H1 + FVG M15 là một internal move chưa đủ để đảo chiều toàn bộ cấu trúc** — tức FVG này chỉ là một continuation pullback trong nhịp giảm lớn hơn, không phải điểm khởi đầu của một leg tăng mới. Dưới reading này, giá "quay về lắp FVG" (mô tả trong Result) không phải là "entry đúng nhưng tham giữ quá lâu" — mà là **FVG bị lấp lại đúng như một pullback trong xu hướng chưa đảo, và cú giảm tiếp theo quét SL chính là phần tiếp diễn của xu hướng giảm mà "chưa quét đáy cũ" đã cảnh báo trước**.

Load-bearing claim của kèo ngược: FVG M15 là continuation-gap trong nhịp giảm chưa kết thúc, không phải reversal-gap của một leg tăng mới.

Tự đánh kèo ngược (strongest self-objection): kèo ngược này dùng đúng câu tự nhận "chưa quét đáy cũ" làm bằng chứng chính — nhưng đó cũng chính là câu evidence duy nhất của thesis gốc (O2). Không có fact THỨ HAI độc lập nào trong file phân biệt được hai reading — cả hai đều giải thích được "giá lấp FVG rồi giảm tiếp".

**Strength label: weaker but non-trivial.** Kèo ngược không giải thích tốt hơn thesis gốc vì thiếu chart để xác nhận cấu trúc D1/H1 rộng hơn, nhưng nó là một cách đọc hợp lệ không cần thêm fact — sẽ trở nên "sống" (live) nếu có chart H1 cho thấy đỉnh cũ 27,404 KHÔNG bị phá bằng body close trước cú giảm cuối.

**Observable phân biệt hai reading**: liệu swing low cũ phía dưới entry có bị quét bằng body close (không chỉ wick) TRƯỚC khi FVG M15 hình thành hay không — nếu có, thesis gốc (reversal) đứng; nếu không, kèo ngược (continuation) đứng.

---

## 10. Falsification Tests

1. **Test đóng O1**: xác nhận SL thực sự dùng để entry là 27,212.8 (frontmatter) hay 27,227 (narrative M15) — nếu có log lệnh gốc (broker) khớp đúng 27,212.8, O1 đóng theo hướng "narrative ghi nhầm, không phải lỗi size"; nếu khớp 27,227, O1 giữ nguyên và r_multiple đã log cần tính lại.
2. **Test đóng O2**: kiểm swing low cũ phía dưới entry (mức giá cụ thể, không có trong file) có bị quét bằng body close trước khi FVG hình thành hay không — có → nới O2 xuống material; không có → O2 giữ fatal.
3. **Test đóng O3**: tìm bất kỳ file lệnh khác trước ngày 2026-04-27 trong journal có ghi ngưỡng partial-TP bằng RR cụ thể TRƯỚC entry (không phải trong phần Result) — có → O3 chuyển từ fatal-adjacent xuống minor (đã có rule, chỉ là vi phạm rule cũ); không có (như hiện tại) → O3 giữ nguyên là hindsight-labeled lesson, chưa phải rule breach.
