---
type: weekly-trading-review
week: 
start_date: 
end_date: 
market_focus:
  - EURUSD
strategy:
  - ICT 2022 Model
status: Draft
tags:
  - trading
  - weekly-review
  - ICT
---

# Weekly Trading Review — {{date:GGGG-[W]WW}}

> [!quote] Mục tiêu của Weekly Review
> Không đánh giá bản thân bằng P&L trong một tuần.  
> Đánh giá bằng **chất lượng quyết định, mức độ tuân thủ hệ thống, khả năng kiểm soát tâm lý và tốc độ cải thiện lỗi lặp lại**.

---

## 0. Weekly Intent

### Trọng tâm tuần này
- **One Mistake to Eliminate:** 
- **One Skill to Train:** 
- **One Behavioral Rule:** 
- **One Process Metric to Improve:** 
- **Success Condition:** 

### Risk Limits của tuần
- Risk per trade: 
- Maximum daily loss: 
- Maximum weekly loss: 
- Maximum trades per day: 
- Maximum consecutive losses before stopping: 
- Mandatory cooldown after a loss: 
- Mandatory stop-trading condition: 

---

# 1. Weekly Performance Summary

| Metric | Result | Notes |
|---|---:|---|
| Total trades |  |  |
| Total valid setups seen |  |  |
| Total valid setups taken |  |  |
| Valid setups missed |  |  |
| Invalid trades taken |  |  |
| Net P&L |  |  |
| Net R |  |  |
| Win rate |  |  |
| Average win (R) |  |  |
| Average loss (R) |  |  |
| Largest win (R) |  |  |
| Largest loss (R) |  |  |
| Max drawdown (R) |  |  |
| Best trading day |  |  |
| Worst trading day |  |  |

## Weekly Narrative

- Tuần này thị trường chủ yếu ở trạng thái nào?
  - Trending / Ranging / High volatility / News-driven / Mixed
- Những ngày nào có điều kiện tốt nhất cho model của tôi?
- Tôi có cố gắng trade trong điều kiện không phù hợp không?
- P&L tuần này đến từ edge thực sự hay từ may mắn / lỗi execution?
- P&L tuần này bị ảnh hưởng bởi hệ thống hay bởi vi phạm rule?

> [!summary] Weekly Conclusion
> - **Kết quả tài chính:**  
> - **Chất lượng execution:**  
> - **Kết luận quan trọng nhất:**  

---

# 2. Decision Quality Review

> [!important] Nguyên tắc
> Một lệnh thắng không tự động là một lệnh tốt.  
> Một lệnh thua không tự động là một lệnh xấu.

| Trade Quality | Count | Total R | Meaning |
|---|---:|---:|---|
| Good Win |  |  | Setup hợp lệ, execution đúng, có lợi nhuận |
| Good Loss |  |  | Setup hợp lệ, execution đúng nhưng thị trường không đi theo kỳ vọng |
| Bad Win |  |  | Vi phạm rule nhưng vẫn thắng |
| Bad Loss |  |  | Sai analysis, execution hoặc kỷ luật |

## Phân tích chất lượng quyết định

### Good Wins
- Lệnh nào đại diện tốt nhất cho playbook?
- Điều gì cần được lặp lại?
- Những điều kiện nào xuất hiện nhiều nhất trong các lệnh thắng chất lượng cao?

### Good Losses
- Lệnh nào thua nhưng hoàn toàn đúng plan?
- Stop loss có đặt tại invalidation logic không?
- Tôi có cần sửa hệ thống hay chỉ cần chấp nhận distribution của kết quả?

### Bad Wins
- Tôi đã vi phạm rule gì nhưng vẫn thắng?
- Lệnh thắng đó có thể tạo ra niềm tin sai nào?
- Nếu lặp lại hành vi này 100 lần, kết quả kỳ vọng là gì?

### Bad Losses
- Rule nào bị vi phạm?
- Vi phạm đó có thể tránh được không?
- Chi phí thực tế của lỗi này là bao nhiêu R?

> [!summary] Decision Quality Verdict
> - Tôi đang mất tiền vì **edge chưa đủ tốt** hay vì **không tuân thủ edge hiện có**?
> - Hành vi nguy hiểm nhất tuần này là:  

---

# 3. ICT 2022 Model Compliance Audit

## 3.1 Higher Timeframe Narrative

| Condition | Yes/No | Notes |
|---|---|---|
| D1 bias được xác định trước phiên |  |  |
| D1 bias có narrative rõ ràng |  |  |
| H1 bias được xác định rõ |  |  |
| D1 và H1 đồng pha hoặc có lý do hợp lệ để lệch pha |  |  |
| H1 dealing range được vẽ trước khi tìm entry |  |  |
| Draw on Liquidity được xác định rõ |  |  |
| Premium/Discount được đánh dấu đúng trong dealing range |  |  |
| POI H1/D1 được xác định trước phiên |  |  |
| POI có chất lượng cao và chưa bị mitigated quá nhiều |  |  |

### HTF Narrative Quality
- Daily Bias: 
- H1 Bias: 
- H1 Dealing Range: 
- Draw on Liquidity: 
- Premium / Discount location: 
- Main POI: 
- Alternative scenario: 
- Điều gì đã làm thesis ban đầu bị invalid?

---

## 3.2 Entry Model Validation

| Entry Requirement | Count Valid | Count Invalid | Notes |
|---|---:|---:|---|
| Có liquidity sweep trước entry |  |  |  |
| MSS xảy ra sau liquidity sweep |  |  |  |
| MSS xảy ra trong / sát POI |  |  |  |
| Có displacement rõ ràng |  |  |  |
| Có FVG / entry model hợp lệ |  |  |  |
| Entry không chase giá |  |  |  |
| Entry nằm trong kill zone |  |  |  |
| Stop loss đặt tại invalidation logic |  |  |  |
| Target theo liquidity / opposing PD Array |  |  |  |
| R:R đạt mức tối thiểu theo rule |  |  |  |

### Hard Invalidations — Không được phép trade

- [ ] Không có liquidity sweep.
- [ ] MSS xảy ra ngoài POI.
- [ ] Không có HTF narrative rõ ràng.
- [ ] Trade ngược D1/H1 mà không có thesis cụ thể.
- [ ] Entry ngoài kill zone.
- [ ] R:R không đạt mức tối thiểu.
- [ ] Entry do FOMO / revenge / boredom.
- [ ] Đã chạm daily loss limit.
- [ ] Đã vượt số lệnh tối đa trong ngày.

> [!warning] Rule cứng
> Chỉ cần vi phạm **một Hard Invalidation**, lệnh được xếp là **Invalid Trade** — dù lệnh đó thắng hay thua.

---

## 3.3 Setup Quality Distribution

| Setup Grade | Criteria | Count | Result (R) | Notes |
|---|---|---:|---:|---|
| A+ | HTF narrative rõ + POI chuẩn + sweep + MSS trong POI + displacement + entry model hợp lệ |  |  |  |
| A | Có đầy đủ điều kiện chính, một vài confluence phụ yếu hơn |  |  |  |
| B | Setup có lý do nhưng thiếu một yếu tố chất lượng |  |  |  |
| Invalid | Vi phạm Hard Invalidation |  |  |  |

## Setup Grade Rules

### A+ Setup
- [ ] D1/H1 narrative rõ.
- [ ] Giá ở POI có chất lượng.
- [ ] Có liquidity sweep đúng hướng narrative.
- [ ] MSS xuất hiện sau sweep và trong/sát POI.
- [ ] Có displacement rõ.
- [ ] Có FVG / entry model có thể định nghĩa.
- [ ] Entry trong kill zone.
- [ ] Target có liquidity rõ ràng.
- [ ] Risk hợp lệ.

### No-Trade Conditions
- [ ] Giá ở giữa range, không ở POI.
- [ ] Chưa lấy liquidity.
- [ ] MSS không rõ hoặc không có displacement.
- [ ] D1/H1 conflict nhưng không có thesis phản biện.
- [ ] Sắp có high-impact news không nằm trong plan.
- [ ] Tôi đang mệt, nóng vội, muốn gỡ lỗ hoặc bị ám ảnh bởi P&L.

---

# 4. Mistake Frequency & Cost Analysis

## 4.1 Mistake Taxonomy

### A. Analysis Errors
- [[Mistake - Wrong Daily Bias]]
- [[Mistake - Wrong H1 Bias]]
- [[Mistake - Incorrect Dealing Range]]
- [[Mistake - Wrong Draw on Liquidity]]
- [[Mistake - POI Not High Quality]]
- [[Mistake - Wrong Premium Discount Location]]

### B. Confirmation Errors
- [[Mistake - No Liquidity Sweep]]
- [[Mistake - MSS Not In POI Zone]]
- [[Mistake - Weak Displacement]]
- [[Mistake - Entered Before Confirmation]]
- [[Mistake - FVG Not Valid]]
- [[Mistake - Ignored Market Structure Context]]

### C. Execution Errors
- [[Mistake - Chased Price]]
- [[Mistake - Early Entry]]
- [[Mistake - Late Entry]]
- [[Mistake - Stop Loss Too Tight]]
- [[Mistake - Stop Loss Too Wide]]
- [[Mistake - Moved Stop Loss]]
- [[Mistake - Took Partial Too Early]]
- [[Mistake - Closed Winner Too Early]]

### D. Psychology & Discipline Errors
- [[Mistake - Revenge Trade]]
- [[Mistake - FOMO Entry]]
- [[Mistake - Overtrading]]
- [[Mistake - Trade Outside Kill Zone]]
- [[Mistake - Ignored Daily Loss Limit]]
- [[Mistake - Trade When Emotionally Unstable]]
- [[Mistake - Boredom Trade]]
- [[Mistake - Hesitated On Valid Setup]]

---

## 4.2 Mistake Leaderboard

| Mistake | Frequency | Total Cost (R) | Trigger | Root Cause | Prevention Rule |
|---|---:|---:|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

### Root Cause Analysis — Top Mistake

- **Mistake:** 
- **Số lần lặp lại:** 
- **Tổng chi phí:** 
- **Trigger xảy ra trước lỗi:** 
- **Niềm tin / suy nghĩ sai tại thời điểm đó:** 
- **Cảnh báo sớm có thể nhận ra:** 
- **Rule phòng ngừa mới:** 
- **Cách kiểm tra việc tuân thủ rule vào tuần tới:** 

> [!danger] Focus Rule
> Không chọn quá nhiều lỗi để sửa trong cùng một tuần.  
> Chỉ chọn **một lỗi lặp lại gây thiệt hại lớn nhất** làm trọng tâm tuần tới.

---

# 5. Psychology & Discipline Audit

## 5.1 Trạng thái trước khi trade

| Factor | Score / State | Notes |
|---|---|---|
| Sleep quality | /5 |  |
| Energy level | /5 |  |
| Stress level | /5 |  |
| Focus level | /5 |  |
| Emotional state | Calm / Neutral / Anxious / Frustrated / Excited |  |
| Pressure to make money | Yes / No |  |
| Physical condition | Good / Average / Poor |  |

## 5.2 Hành vi trong lúc trade

| Question | Yes/No | Evidence / Example |
|---|---|---|
| Tôi có tuân thủ plan trước entry không? |  |  |
| Tôi có cảm thấy FOMO không? |  |  |
| Tôi có vào lệnh để gỡ lệnh trước không? |  |  |
| Tôi có vào lệnh do chán / muốn có hành động không? |  |  |
| Tôi có do dự ở A+ setup không? |  |  |
| Tôi có dời SL/TP vì cảm xúc không? |  |  |
| Tôi có nhìn P&L quá thường xuyên không? |  |  |
| Tôi có trade quá số lệnh đã định không? |  |  |
| Tôi có dừng đúng lúc khi rule yêu cầu không? |  |  |

## 5.3 Phản ứng với thắng và thua

- Cảm xúc sau lệnh thắng đầu tiên: 
- Cảm xúc sau lệnh thua đầu tiên: 
- Lệnh thua có làm thay đổi tiêu chuẩn entry tiếp theo không?
- Lệnh thắng có khiến tôi chủ quan hoặc tăng size không?
- Có lúc nào tôi cố chứng minh nhận định của mình thay vì đọc hành vi giá không?
- Tôi có phân biệt được “tự tin theo hệ thống” và “tự tin quá mức” không?

## 5.4 Discipline Score

| Discipline Metric | Target | Actual | Pass/Fail |
|---|---:|---:|---|
| Trades with full checklist | 100% |  |  |
| Trades with screenshot before entry | 100% |  |  |
| Complete journal after each trade | 100% |  |  |
| Invalid trades | 0 |  |  |
| Revenge trades | 0 |  |  |
| Trades outside kill zone | 0 |  |  |
| Daily loss limit violations | 0 |  |  |
| Max trades per day violations | 0 |  |  |

---

# 6. Circuit Breaker Review

> [!important] Mục tiêu
> Không dùng ý chí để chống revenge trading.  
> Dùng rule cơ học, thời gian nghỉ và giới hạn rủi ro.

## Circuit Breaker Rules

- [ ] Sau **2 lệnh thua liên tiếp đúng plan**: nghỉ tối thiểu 15 phút; chỉ quay lại khi có A+ setup.
- [ ] Sau **1 lệnh vi phạm rule**: nghỉ tối thiểu 30 phút; viết nguyên nhân trước khi mở chart lại.
- [ ] Sau **2 lệnh vi phạm rule trong ngày**: dừng trading cả ngày.
- [ ] Khi chạm **daily loss limit**: dừng trading cả ngày.
- [ ] Khi có dấu hiệu revenge: đóng order panel, ghi trigger, nghỉ tối thiểu 20 phút.
- [ ] Khi thấy bản thân mất tập trung / mệt / bực tức: chỉ quan sát hoặc chuyển sang replay.

## Circuit Breaker Compliance

| Situation | Did it happen? | Did I stop correctly? | Notes |
|---|---|---|---|
| 2 consecutive losses |  |  |  |
| Rule violation |  |  |  |
| Daily loss limit hit |  |  |  |
| Revenge impulse |  |  |  |
| Emotional instability |  |  |  |

---

# 7. Process Metrics

> [!tip] Process metrics là chỉ số dẫn dắt
> P&L trong một tuần có thể ngẫu nhiên.  
> Quy trình, mức độ tuân thủ và chất lượng setup mới là thứ tạo ra kết quả bền vững.

| Metric | Target | Actual | Trend | Notes |
|---|---:|---:|---|---|
| Total valid setups seen |  |  | ↑ / ↓ / → |  |
| Valid setups taken |  |  | ↑ / ↓ / → |  |
| Valid setups missed |  |  | ↑ / ↓ / → |  |
| Invalid trades taken | 0 |  | ↑ / ↓ / → |  |
| Trades with D1/H1 alignment |  |  | ↑ / ↓ / → |  |
| Trades with liquidity sweep | 100% |  | ↑ / ↓ / → |  |
| Trades with MSS in POI | 100% |  | ↑ / ↓ / → |  |
| Trades with full checklist | 100% |  | ↑ / ↓ / → |  |
| Trades fully journaled | 100% |  | ↑ / ↓ / → |  |
| Revenge impulses resisted |  |  | ↑ / ↓ / → |  |
| Trades skipped correctly |  |  | ↑ / ↓ / → |  |

## Process Score

- **Process Score:** __ / 10
- **Execution Score:** __ / 10
- **Analysis Score:** __ / 10
- **Discipline Score:** __ / 10
- **Psychology Score:** __ / 10

### Why these scores?
- Process:
- Execution:
- Analysis:
- Discipline:
- Psychology:

---

# 8. Best and Worst Trade Review

## 8.1 Best A+ Trade of the Week

- Trade link: 
- Symbol:
- Session / Kill Zone:
- Direction:
- D1 Bias:
- H1 Narrative:
- H1 Dealing Range:
- Draw on Liquidity:
- POI:
- Liquidity sweep:
- MSS:
- Displacement:
- Entry model:
- Stop loss logic:
- Target logic:
- Result:
- Why this was A+:
- What I executed well:
- What should be repeated:
- Screenshot before entry:
- Screenshot after result:

---

## 8.2 Best Loss of the Week

> [!note] A good loss is evidence of execution quality, not failure.

- Trade link:
- Symbol:
- Why the setup was valid:
- Which rules were followed:
- What invalidated the idea:
- Was the stop loss logical?
- Did I manage the trade correctly?
- What does this loss teach about distribution / market conditions?
- Screenshot:

---

## 8.3 Worst Rule Violation

- Trade link:
- Symbol:
- Broken rule:
- Was the trade invalid before entry? Why?
- Emotional trigger:
- What thought led to the action?
- Actual cost in R:
- Correct action should have been:
- Prevention rule:
- Screenshot:

---

## 8.4 Missed A+ Setup

- Symbol:
- Session:
- Why did this qualify as A+?
- Which visual clue did I fail to recognize?
- Why was it missed?
  - [ ] Hesitation
  - [ ] Lack of preparation
  - [ ] Not at screen
  - [ ] Analysis not completed
  - [ ] Fear after previous loss
  - [ ] Other:
- How will I prevent missing the same setup next time?
- Screenshot:

---

## 8.5 Best No-Trade Decision

- Market / Session:
- Why did I stay out?
- Which invalidation / no-trade condition was present?
- What loss or mistake did this avoidance prevent?
- Screenshot:

---

# 9. Knowledge & Playbook Development

## 9.1 Concept Studied This Week

- **Topic:** 
- **Definition in my own words:** 
- **Key insight:** 
- **How it applies to ICT 2022 model:** 
- **Example observed in replay or live market:** 
- **Counter-example / when the concept does not apply:** 
- **What misconception did I correct?** 
- **Rule added or refined:** 

---

## 9.2 Setup Added / Updated in Playbook

### Setup Name
- Market condition:
- HTF narrative:
- D1 bias:
- H1 role:
- Liquidity target:
- POI type:
- Entry timeframe:
- Trigger:
- Invalidation:
- Stop loss logic:
- Target model:
- Best session:
- Conditions to avoid:
- Screenshot before:
- Screenshot after:

### Counter-Example — Do NOT Take This Setup When
- 
- 
- 

---

## 9.3 Replay / Deliberate Practice

| Practice Item | Target | Completed | Key Finding |
|---|---:|---:|---|
| Review A+ examples |  |  |  |
| Replay missed setups |  |  |  |
| Replay invalid trades |  |  |  |
| Mark D1/H1 dealing ranges |  |  |  |
| Practice liquidity sweep identification |  |  |  |
| Practice MSS-in-POI filtering |  |  |  |

### One Pattern I Need to See Faster
- Pattern:
- Context:
- Visual trigger:
- Common false version:
- Replay exercise for next week:

---

# 10. Next Week Improvement Plan

## One Mistake to Eliminate
- **Mistake:** 
- **Why this matters:** 
- **Rule:** 
- **Measurement:** 
- **Pass condition:** 

## One Skill to Train
- **Skill:** 
- **Practice method:** 
- **Minimum repetitions:** 
- **Evidence required:** 
- **Pass condition:** 

## One Behavioral Rule
- **Rule:** 
- **Trigger:** 
- **Required action:** 
- **How I will track compliance:** 

## One Process Metric to Improve
- **Metric:** 
- **Current baseline:** 
- **Target:** 
- **How it will be measured:** 

## Next Week Non-Negotiables
- [ ] Không trade khi chưa có D1/H1 narrative.
- [ ] Không trade nếu chưa có liquidity sweep.
- [ ] Không trade MSS ngoài POI.
- [ ] Không vượt risk limit.
- [ ] Không trade để gỡ lỗ.
- [ ] Journal đầy đủ 100% lệnh.
- [ ] Chụp ảnh D1/H1/M5 trước entry.
- [ ] Dừng đúng khi circuit breaker kích hoạt.

> [!success] Weekly Commitment
> “Tuần tới, tôi ưu tiên thực hiện đúng hệ thống hơn là cố tạo P&L.  
> Tôi chỉ trade khi điều kiện A+/A hợp lệ xuất hiện; mọi setup không đủ chuẩn đều là no-trade.”

---

# 11. Final Reflection

## Ba điều tôi đã làm tốt
1. 
2. 
3. 

## Ba điều cần cải thiện
1. 
2. 
3. 

## Bài học quan trọng nhất tuần này
> 

## Một câu nhắc nhở cho tuần tới
> 

---

# 12. Links

## Trades Reviewed
```dataview
TABLE
  date as Date,
  symbol as Symbol,
  position as Position,
  pnl as "P&L",
  r_multiple as "R",
  Mistake as Mistake
FROM "Trading Journal"
WHERE date >= date(this.start_date) AND date <= date(this.end_date)
SORT date ASC
```

## Mistakes Mentioned This Week
```dataview
LIST
FROM "Mistakes"
WHERE contains(file.inlinks, this.file.link)
SORT file.name ASC
```

## Related Weekly Reviews
```dataview
LIST
FROM "Weekly Reviews"
WHERE file.name != this.file.name
SORT week DESC
LIMIT 8
```
