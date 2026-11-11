---
type: ict-concept
concept: Draw on Liquidity (DOL) — Ontology, Candidate Selection, Failure Model & Backtest Design
aliases:
  - DOL Ontology
  - Candidate DOL
  - DOL Failure Model
  - Pool vs DOL
  - DOL Prospectively
tags:
  - trading/ict/concept
  - trading/deep-dive
  - liquidity
  - market-microstructure
  - bias
  - d1-h1-m5
  - 2022-model
  - quantitative
  - backtest
status: developing
category: Liquidity
timeframes:
  - D1
  - H1
  - M5
models:
  - ICT 2022 Model
  - PO3/AMD
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-09-28
created: 2026-09-28
updated: 2026-09-28
prerequisites:
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[12-Dealing-Range]]"
  - "[[59-Daily-Bias]]"
  - "[[27-Premium-Discount]]"
  - "[[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]"
  - "[[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]"
  - "[[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]"
common_mistakes:
  - gọi mọi pool là DOL
  - xác định DOL sau khi giá đã chạy rồi tưởng là phân tích
  - dùng DOL làm entry trigger
  - "circular reasoning: DOL suy ra bias rồi bias xác nhận DOL"
  - đổi candidate set giữa chừng không ghi lý do
  - nhầm descriptive draw với predictive draw
run_tag: dol-ontology-candidate-failure-56
---

> [!summary] Tóm tắt 1 câu
> **DOL không phải một vật thể trên chart — nó là một mệnh đề xác suất có điều kiện, được phát biểu tại một thời điểm cutoff, so sánh ít nhất hai candidate ở hai phía, và tự động hết hiệu lực khi candidate thắng đổi.** Mọi cách dùng DOL không viết ra được (cutoff + candidate set + đối thủ + horizon + invalidation) đều không phải DOL — đó là nhãn dán sau khi biết kết quả.

> [!warning] Giới hạn bằng chứng của bài này — đọc trước khi tin bất kỳ con số nào
> **PDF fetch trong môi trường này vẫn hỏng** (lỗi `Binary PDF garbage in content` trên cả arXiv lẫn New York Fed — cùng lỗi mà [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] đã ghi nhận). Hệ quả cụ thể:
> - Các bài học thuật dưới đây được đọc từ **abstract, trang tóm tắt của nhà xuất bản, và metadata API** (OpenAlex/Crossref) — **không phải toàn văn**.
> - Những gì bài nói về **cơ chế** (stop orders cụm quanh round number; take-profit và stop-loss hành xử ngược nhau) là **chắc chắn** — nhiều nguồn độc lập mô tả giống nhau và đã verify được abstract gốc.
> - Những gì bài nói về **con số tỷ lệ phần trăm cụ thể** là **đọc từ abstract, chưa mở được bảng biểu gốc**. Đã đánh dấu rõ ở từng chỗ.
> - Toàn bộ phần định lượng (§18–§20) là **thiết kế đề xuất**, không phải kết quả đã chạy. Không có backtest nào trong bài này.

> [!info] Bài này bổ sung gì cho 52 / 53 / 54
> Ba note cũ đã trả lời tốt các câu hỏi khác. Đừng đọc lại chúng ở đây:
> - [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] → **DOL là gì, SOP đầu ngày 7 bước, confluence, case NQ, checklist journal.** Bài này KHÔNG lặp lại SOP.
> - [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] → **chọn draw khi cấu trúc dày swing; Judas fuel vs bearish DOL.** Bài này chỉ mở rộng phần *điều kiện biến pool thành candidate*.
> - [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] → **thuật toán phát hiện swing (N-bar pivot, DC, ZigZag lookahead).** Bài này dùng lại kết luận đó, không trình bày lại.
> - [[dol-ict-deep-dive]] → **ontology nền + market mechanism + backtest framework bản đầu.**
>
> **Phần mới thực sự của bài này:** (a) ontology tách 4 tầng *pool → candidate → DOL → target*; (b) bảng phân biệt **liquidity-ICT vs liquidity-microstructure** theo 3 cột quan sát được / suy luận được / không thể biết; (c) **epistemic ladder 6 bậc** với 5 ví dụ; (d) điều kiện biến **pool → candidate DOL** viết dưới dạng điều kiện kiểm tra được; (e) bảng **structural event → tác động lên DOL**; (f) **failure model 3 lớp** + **8 trap patterns** có tiêu chí phân loại; (g) **look-ahead checklist 9 mục** cho backtest; (h) **decision tree 13 bước**.

---

# 1. Executive Summary

Mười tám bullet dưới đây là toàn bộ mental model. Phần còn lại của bài chỉ là chứng minh, mở rộng, và biến chúng thành quy tắc kiểm tra được.

1. **DOL là một mệnh đề, không phải một mức giá.** Phát biểu đầy đủ có dạng: *"Tại cutoff $t$, trong horizon $H$, candidate $X$ có xác suất được chạm trước candidate đối thủ $Y$ cao hơn."* Thiếu bất kỳ thành phần nào → không phải DOL.
2. **"Draw" là một từ mô tả quan hệ, không mô tả lực.** Không có lực nào kéo giá. Có một phân phối kết quả nghiêng về một phía vì cấu trúc lệnh chờ và độ sâu thị trường không đối xứng. `[MARKET MECHANICS]`
3. **Descriptive draw ≠ predictive draw.** *"Giá đã đi tới X"* là sự kiện quan sát được. *"X là DOL"* là mệnh đề dự báo. Cái thứ nhất **không** chứng minh cái thứ hai. Đây là lỗi trung tâm của toàn bộ phương pháp. `[INTERPRETATION]`
4. **Pool ≠ candidate DOL ≠ DOL.** Pool là **dữ liệu**. Candidate là pool **đã qua bộ lọc cấu trúc**. DOL là candidate **thắng trong so sánh hai phía**. Target là mức giá **vận hành** của DOL. Bốn tầng, ba lần loại bỏ.
5. **Mọi BSL/SSL đều là pool. Không phải mọi pool là candidate. Không phải mọi candidate là DOL.** Tỉ lệ thu hẹp thực tế điển hình trên D1 là khoảng **10–20 pool → 3–5 candidate → 1 DOL mỗi phía → 1 target**.
6. **Điều kiện biến pool thành candidate DOL** (§3.3): nằm cùng phía với structural state hiện tại **và** reachable trong horizon **và** chưa bị tiêu thụ. Ba điều kiện, kiểm tra được, không cần phán đoán.
7. **Thứ tự chọn không phải "pool nào quan trọng nhất" mà là "pool nào thắng pool đối thủ".** Không có câu hỏi "DOL là gì" tách rời câu hỏi "DOL thay thế cái gì". Một DOL không có đối thủ là một nhận định chưa được kiểm tra.
8. **Neutral là output hợp lệ và phải xuất hiện thường xuyên.** Nếu mô hình của bạn chưa bao giờ trả về neutral, nó không phải mô hình — nó là thói quen. `[INTERPRETATION]`
9. **Hai tầng DOL cùng tồn tại, không mâu thuẫn: intermediate objective và final objective.** D1 chọn final; H1 chọn intermediate trên đường đi. Mâu thuẫn D1↔H1 phần lớn là do gộp hai tầng làm một.
10. **DOL không phải entry trigger.** DOL trả lời *đi đâu*. Entry trả lời *vào ở đâu, khi nào*. Gộp hai câu này là nguồn gốc của phần lớn lệnh thua trong mô hình DOL. `[ICT FRAMEWORK]`
11. **Trong ICT gốc, DOL là destination; PD array (FVG/OB/OTE) là entry.** Thứ tự là sweep → MSS → displacement → FVG retrace → entry, và DOL nằm ở **cuối** chuỗi đó, không phải đầu. `[ICT FRAMEWORK]`
12. **Cơ chế vi mô có thật nhưng yếu hơn narrative.** Stop orders cụm quanh round number, và stop-loss orders hành xử **ngược** take-profit orders — đây là cơ sở vững cho việc level có thể vừa đảo chiều vừa tăng tốc. `[MARKET MECHANICS]`
13. **Base rate là kẻ thù lớn nhất.** Round-crossing xảy ra nhiều lần mỗi ngày; cascade thật chỉ khoảng một lần mỗi tuần. Nghĩa là **phần lớn lần chạm pool là nhiễu** — mô hình phải có cơ chế lọc, không chỉ có cơ chế gọi tên. `[MARKET MECHANICS]`
14. **Chart OHLC không chứa thông tin về lượng lệnh, ý định, hay absorption.** Nó chứa **giá, thời gian, và cấu trúc**. Mọi kết luận về "ai đang làm gì" đều là suy luận, và phải được dán nhãn là suy luận.
15. **Daily Bias không được suy ra từ DOL.** DOL suy ra bias rồi bias xác nhận DOL là circular reasoning. Model đúng là *structure + liquidity + location → directional hypothesis → candidate selection* (§10).
16. **DOL là biến trạng thái, có ba trạng thái: projected / active / resolved-or-invalidated.** Không đóng băng DOL cả ngày, nhưng cũng không được đổi nó mà không có sự kiện cấu trúc — mọi lần đổi phải ghi lý do.
17. **Look-ahead bias trong DOL tinh vi hơn trong indicator.** Swing chỉ tồn tại sau N nến; dealing range chỉ rõ sau khi đóng băng; "level quan trọng" chỉ rõ sau khi có phản ứng. Cả ba đều là đường dẫn thông tin tương lai vào quá khứ (§16, §19).
18. **H0 mặc định là: DOL identification KHÔNG có predictive advantage.** Nghĩa vụ của người dùng DOL là bác bỏ H0, không phải xác nhận H1. Cho tới khi làm được điều đó, DOL là **công cụ tổ chức tư duy**, không phải **edge đã kiểm chứng**.

> [!important] Câu chốt của toàn bài
> **Một pool mà giá cuối cùng đã chạm tới KHÔNG tự động là bằng chứng rằng nó là DOL trước khi giá di chuyển.**
> Một **narrative ICT hợp lý KHÔNG tự động là một lợi thế giao dịch có thể dự báo.**
> Toàn bộ bài này là nỗ lực phân biệt **câu chuyện hồi tố** với **thông tin tiên nghiệm**.

---

# 2. Direct Answer

## 2.1 DOL là gì

**DOL là một mệnh đề xác suất có điều kiện về thứ tự chạm của hai nhóm mức giá.**

Phát biểu tối thiểu đủ chặt:

> Tại cutoff $t$, xét candidate set $C = \{U_1, U_2, \dots\} \cup \{L_1, L_2, \dots\}$ chỉ chứa thông tin có sẵn tại $t$. Trong horizon $H$, **DOL là candidate $X \in C$ có $P(\text{X chạm trước mọi candidate đối thủ cùng tầng})$ cao nhất.**

Ba hệ quả trực tiếp:

- **DOL luôn có đối thủ.** Chọn U mà không xét L không phải chọn DOL — đó là chọn thiên kiến.
- **DOL luôn có hạn.** Không có horizon thì không có dự báo, chỉ có niềm tin.
- **DOL luôn có cutoff.** Không có cutoff thì mệnh đề không thể sai, và cái gì không thể sai thì không phải dự báo.

## 2.2 DOL KHÔNG phải gì

| DOL **là** | DOL **KHÔNG phải** |
|---|---|
| Mệnh đề so sánh hai phía | Một mức giá đơn lẻ |
| Kết quả của bộ lọc cấu trúc | Bất kỳ BSL/SSL nào |
| Destination / objective | Entry trigger |
| Biến trạng thái có hạn dùng | Nhãn cố định cả ngày |
| Xác suất có điều kiện | Đảm bảo / "nam châm" |
| Có thể bị bác bỏ (falsifiable) | Narrative giải thích mọi kết cục |
| Target và directional context | Lý do để vào lệnh |
| Đối tượng nghiên cứu định lượng được | Bằng chứng về ý định của participant |

## 2.3 Ba câu hỏi ontology phải trả lời dứt khoát

**Câu 1: DOL là một level, một zone, một pool, một hướng, hay một kỳ vọng?**

Đây là **câu hỏi giả**. Nó giả định DOL là một loại vật thể. DOL là một **mệnh đề** — và mệnh đề cần một **mức giá tham chiếu** để vận hành. Cách phân giải:

- **Về bản thể:** DOL là một **kỳ vọng có hướng** (directional expectation).
- **Về vận hành:** DOL được **biểu diễn** bằng một mức giá cụ thể (hoặc một zone với tolerance định trước), vì không có mức giá thì không thể đo, không thể target, không thể backtest.
- **Về nguồn gốc:** mức giá đó thường **là** một liquidity pool, nhưng không bắt buộc — nó có thể là một imbalance boundary, hoặc một mức cấu trúc không phải pool (ví dụ midpoint của dealing range trong trường hợp rebalance).

Nói "DOL là pool X" là **viết tắt** cho "mệnh đề DOL được biểu diễn tại mức giá của pool X". Viết tắt này tiện nhưng là nguồn gốc của lỗi pool-equals-DOL.

**Câu 2: DOL có nhất thiết là liquidity pool không?**

**Không.** `[ICT FRAMEWORK]` Trong ICT, hai họ destination được nêu: **stops/liquidity** và **imbalance/inneficiency**. Một unfilled FVG hoặc một volume imbalance có thể là destination mà không chứa stop cluster nào. Vì vậy:

- Pool là **tập con** của các destination khả dĩ, không phải toàn bộ.
- Một sự kiện imbalance (gap mở cửa tuần/ngày, liquidity void sau tin) có cơ chế khác hẳn pool: nó hút giá về **vùng giá chưa được giao dịch nhiều**, không phải về **nơi có lệnh chờ**.
- Hệ quả thực hành: **hai loại DOL này có hành vi khác nhau khi chạm** — pool thường sweep-rồi-đảo hoặc run-rồi-tiếp; imbalance thường fill-rồi-tiếp. Dùng một kỳ vọng hành vi cho cả hai là lỗi.

**Câu 3: DOL có thay đổi khi market state thay đổi không?**

**Có, và đây là điều kiện để mô hình trung thực.** Nếu DOL không bao giờ đổi, nó không phải mệnh đề về thị trường — nó là định kiến. Ba trạng thái:

| Trạng thái | Điều kiện chuyển | Hành động |
|---|---|---|
| **Projected** | Chọn tại cutoff, chưa có xác nhận delivery | Cho phép lập kế hoạch, chưa cho phép entry |
| **Active** | Opposing-side raid đã xảy ra HOẶC displacement đang chạy theo hướng target | Cho phép execution theo template |
| **Resolved / Invalidated** | Target chạm (resolved) HOẶC close vượt invalidation (invalidated) | Bắt buộc xây candidate set mới; cấm dùng lại pool cũ làm nam châm |

---

# 3. Ontology của DOL

## 3.1 Chuỗi bốn tầng

```
LIQUIDITY (khái niệm chung)
    ↓ quan sát + phân loại
LIQUIDITY POOL (pool cụ thể, có giá)
    ↓ lọc cấu trúc + reachability + freshness
CANDIDATE DOL (ứng viên hợp lệ)
    ↓ so sánh hai phía + chọn
DOL (mệnh đề thắng)
    ↓ lượng hoá vận hành
TARGET (mức giá vào lệnh/thoát lệnh)
```

Đây không phải bốn tên gọi cho cùng một thứ. Đây là **ba lần loại bỏ liên tiếp**, và mỗi lần loại bỏ phải có tiêu chí viết ra được.

![[DOL-Ontology-Chuoi-Bon-Tang.svg|697]]

*Hình 1 — Chuỗi bốn tầng với ba cổng lọc. Chú ý bốn lỗi nhầm tầng ở khối cuối: gọi mọi pool là DOL, nhảy thẳng pool → target, coi DOL là mức giá cố định, và dùng DOL làm entry trigger.*

## 3.2 Liquidity Pool — tầng dữ liệu

### Layer 1 — Giải thích đơn giản
Pool là **một chỗ trên chart mà nhiều người có thể đã đặt lệnh chờ**. Giống như một dãy máy ATM trên cùng một con phố: bạn không biết chính xác có bao nhiêu người, nhưng bạn biết nếu đi tới đó thì sẽ gặp dòng người.

### Layer 2 — Định nghĩa kỹ thuật
Một **pool** là một tập mức giá trong một cửa sổ tolerance quanh một cực trị cấu trúc, nơi tồn tại khả năng tập trung các conditional order (stop, breakout, limit) do tính dễ thấy của cực trị đó.

### Layer 3 — Diễn giải ICT
`[ICT FRAMEWORK]` Trong ICT, pool được chia thành **Buy-Side Liquidity (BSL)** — nằm trên các đỉnh cũ, equal highs, PDH, PWH — và **Sell-Side Liquidity (SSL)** — nằm dưới các đáy cũ, equal lows, PDL, PWL. Cách phân loại này là **theo vị trí**, không theo ai đặt lệnh.

### Layer 4 — Hàm ý phân tích
Pool là **nguyên liệu thô**. Bước này được phép rộng rãi: mark nhiều pool, không cần phân xử. Sai lầm chỉ bắt đầu khi bước này bị nhầm với bước sau.

### Layer 5 — Giới hạn
> [!warning] Điều pool KHÔNG cho phép kết luận
> Pool cho biết **nơi lệnh có thể tập trung**. Nó **không** cho biết: có bao nhiêu lệnh, loại lệnh gì, ai đặt, còn hiệu lực không, hay giá sẽ tới đó. Bốn thứ đó **không quan sát được từ OHLC** (§4).

### Pool quan sát được vs pool suy luận

| Loại pool | Ví dụ | Mức độ khách quan |
|---|---|---|
| **Định nghĩa số học** | PDH, PDL, PWH, PWL, session H/L | **Khách quan** — tính được từ dữ liệu |
| **Định nghĩa có tham số** | Equal highs/lows (cần $\varepsilon$), swing (cần N hoặc DC threshold) | **Bán khách quan** — khách quan *sau khi* chốt tham số |
| **Định nghĩa phán đoán** | "Đỉnh quan trọng", "vùng cung rõ ràng" | **Chủ quan** — không tái lập được |
| **Không quan sát được** | Lượng stop thật, depth thật, iceberg | **Không thể biết** từ chart |

## 3.3 Điều kiện biến Pool → Candidate DOL

Đây là phần protocol yêu cầu xây dựng, và là đóng góp vận hành chính của bài này. Một pool $P$ trở thành **candidate DOL** khi và chỉ khi thỏa **cả ba** điều kiện sau, tại cutoff $t$:

**Điều kiện 1 — Alignment (cùng phía với structural state)**
$P$ nằm cùng phía với hướng của **structural event gần nhất đã được xác nhận** (BOS, MSS, hoặc sweep có reclaim). Cụ thể:
- Nếu structural state là *bullish continuation* (BOS lên + HL được giữ) → chỉ **BSL** phía trên là candidate.
- Nếu structural state là *bearish continuation* → chỉ **SSL** phía dưới là candidate.
- Nếu structural state là *reversal sau sweep có reclaim* → candidate nằm **ngược** phía vừa bị sweep.
- Nếu structural state **không xác định** (giá giữa range, nến chồng lấn) → **không có candidate nào**. Đây là trạng thái neutral hợp lệ.

**Điều kiện 2 — Reachability (tầm với trong horizon)**
$\text{distance}(P, \text{price}_t) \le \lambda \cdot \text{ADR}$(hoặc ATR-tương ứng horizon), với $\lambda$ chốt trước (khởi điểm hợp lý: $\lambda \approx 0{,}8\text{–}1{,}0$ cho intraday). Pool vượt ngưỡng **không bị xoá** — nó được **hạ xuống final objective** của horizon dài hơn. Đây chính là cơ chế tạo ra tầng DOL (§8).

**Điều kiện 3 — Freshness (chưa tiêu thụ)**
$P$ chưa bị trade-through kể từ khi được xác nhận. Pool đã bị xuyên qua **có thể** còn giá trị như một *mức cấu trúc* (ví dụ old high trở thành resistance) nhưng **hết giá trị như một pool** — vì thành phần conditional order tại đó đã bị tiêu thụ.

> [!important] Điều kiện ẩn thứ tư — Đối thủ
> Một candidate chỉ có nghĩa khi **tồn tại ít nhất một candidate đối thủ ở phía kia của cùng tầng**. Nếu chỉ có một phía có candidate, không phải vì "DOL đã rõ" — mà vì **bạn chưa mark đủ phía bên kia**. Đây là phép thử thực dụng mạnh nhất: trước khi tuyên bố DOL, phải viết được candidate đối thủ và lý do nó yếu hơn.

**Công thức vận hành:**

```
Candidate(P) ⟺ Alignment(P) ∧ Reachability(P) ∧ Freshness(P)
DOL ⟺ argmax_{P ∈ Candidates} Score(P)  |  có ≥1 đối thủ mỗi phía
```

Toàn bộ `Score` là **[HYPOTHESIS — BACKTEST REQUIRED]** (xem §13.3 và §18). Điều kiện 1–3 không phải hypothesis — chúng là định nghĩa vận hành, và có thể sai với tư cách định nghĩa (tức là: có thể không hữu ích), nhưng không thể sai với tư cách logic.

![[DOL-Dieu-Kien-Candidate-Va-Phep-Thu-Doi-Thu.svg|697]]

*Hình 2 — Ba điều kiện và điều kiện ẩn thứ tư. Phép thử thực dụng mạnh nhất nằm ở nhánh phải: nếu không viết được candidate đối thủ, bạn chưa có DOL — bạn có thiên kiến.*

## 3.4 Mười bốn câu hỏi ontology — trả lời trực tiếp

| # | Câu hỏi | Trả lời | Loại |
|---|---|---|---|
| 1 | DOL là gì? | Mệnh đề xác suất có điều kiện về thứ tự chạm, phát biểu tại cutoff | `[ANALYTICAL FRAMEWORK]` |
| 2 | "Draw" nghĩa là gì? | Quan hệ bất đối xứng trong phân phối kết quả, không phải lực | `[INTERPRETATION]` |
| 3 | Level / zone / pool / objective / expectation? | **Kỳ vọng có hướng**, biểu diễn bằng mức giá | `[ANALYTICAL FRAMEWORK]` |
| 4 | Có nhất thiết là pool không? | **Không** — imbalance cũng là destination | `[ICT FRAMEWORK]` |
| 5 | Pool khác DOL thế nào? | Pool = dữ liệu; DOL = kết luận sau lọc + so sánh | `[ANALYTICAL FRAMEWORK]` |
| 6 | Liquidity Target khác DOL thế nào? | Target = mức giá vận hành của DOL, có thể là mức gần hơn (intermediate) | `[ANALYTICAL FRAMEWORK]` |
| 7 | External Liquidity ≡ DOL? | **Không** — external là phân loại vị trí; DOL là mệnh đề ưu tiên. External thường *được chọn làm* final DOL, nhưng không đồng nghĩa | `[ANALYTICAL FRAMEWORK]` |
| 8 | Mọi BSL/SSL là DOL? | **Không** — hầu hết là pool không qua được bộ lọc | `[ANALYTICAL FRAMEWORK]` |
| 9 | Previous high/low luôn là DOL? | **Không** — nhưng là pool **khách quan nhất** và có cơ sở vi mô rõ nhất | `[MARKET MECHANICS]` |
| 10 | Equal highs/lows luôn là DOL? | **Không** — là *dấu hiệu* khả năng tập trung lệnh; độ mạnh phụ thuộc $\varepsilon$, số touch, và cấu trúc | `[HYPOTHESIS]` |
| 11 | Swing high/low luôn là DOL? | **Không** — chỉ structural swing mới đủ tư cách; inventory swing là fuel | `[ANALYTICAL FRAMEWORK]` |
| 12 | Nhiều candidate cùng lúc? | **Có, và bắt buộc** — mỗi phía tối thiểu một candidate | `[ANALYTICAL FRAMEWORK]` |
| 13 | Có primary / secondary không? | **Có** — nhưng "secondary" phải định nghĩa là *intermediate objective*, không phải "target dự phòng khi target chính fail" | `[ANALYTICAL FRAMEWORK]` |
| 14 | DOL đổi khi state đổi? | **Có** — ba trạng thái; đổi không ghi lý do = narrative dịch chuyển | `[ANALYTICAL FRAMEWORK]` |

> [!danger] Câu 13 là cái bẫy tinh vi nhất
> "Primary DOL" và "secondary DOL" là terminology **chúng ta tự xây**, không phải ICT gốc. Vấn đề: nếu secondary được hiểu là *"pool kia phòng khi primary không tới"*, thì mô hình **luôn đúng** — vì mọi kết cục đều khớp với một trong hai. Secondary chỉ hợp lệ khi được hiểu là **intermediate objective trên đường tới final objective**: tức là cả hai phải **cùng hướng**, chỉ khác thứ tự và khoảng cách.

---

# 4. Market Microstructure

Mục tiêu của chương này: tách **cơ chế quan sát được** khỏi **ý định được gán**. Đây là chương mà lỗi `ICT narrative → market fact` xảy ra thường xuyên nhất.

![[DOL-Ba-Cot-Hieu-Biet-Quan-Sat-Suy-Luan-Khong-The-Biet.svg|697]]

*Hình 3 — Ba cột hiểu biết. DOL được phép bắc cầu từ cột 1 sang cột 2, **không bao giờ** sang cột 3. Khối cuối minh hoạ vì sao: cùng một cây nến cho hai cách đọc trái ngược mà không cách nào bị phủ định.*

## 4.1 Bảng phân biệt trung tâm: liquidity-ICT vs liquidity-microstructure

Protocol hỏi: *"Liquidity trong ICT chart terminology có giống 'liquidity' trong market microstructure hay không?"* Trả lời: **chồng lấn một phần, khác về bản chất, và khác ở đúng chỗ nguy hiểm nhất.**

| Khái niệm | Trong microstructure | Trong ICT | Quan hệ |
|---|---|---|---|
| **Liquidity** | Khả năng khớp lệnh nhanh, chi phí thấp, ít làm dịch giá | **Các mức giá nơi có lệnh chờ** | **Khác bản chất.** Micro = thuộc tính của *thị trường*; ICT = *toạ độ* trên chart |
| **Resting liquidity** | Limit orders nằm trên book, quan sát được (nếu có L2) | Các mức hỗ trợ/kháng cự "có lệnh" | **Chồng lấn** — nhưng ICT suy từ chart, micro đo từ book |
| **Stop orders** | **Latent aggressive flow** — trở thành market order khi trigger | "Liquidity" (thanh khoản) | **Xung đột thuật ngữ.** Stop *tiêu thụ* liquidity, không *cung cấp* | 
| **Liquidity demand** | Nhu cầu khớp ngay (market orders) | — | ICT không có khái niệm tương ứng |
| **Liquidity supply** | Cung lệnh chờ (limit orders) | Ngầm hiểu trong "pool" | **Chồng lấn một phần** |
| **Visible liquidity** | Depth hiển thị trên book | Mức giá "ai cũng thấy" (PDH, equal highs) | **Chồng lấn về ý tưởng**, khác về đơn vị |
| **Hidden liquidity** | Iceberg, reserve orders, dark pools | "Smart money ẩn" | **Khác hoàn toàn.** Hidden liquidity là khái niệm kỹ thuật đo được; "smart money ẩn" là suy luận |
| **Order-book liquidity** | Depth theo từng tick | — | **Không có tương ứng trên chart** |
| **Chart-derived pool** | — | PDH/PDL, equal highs/lows, swing | **Trừu tượng hoá** — không đo lường, chỉ suy |

### Ba kết luận từ bảng này

**Kết luận 1 — "Stops là liquidity" là shorthand sai về mặt kỹ thuật.** `[MARKET MECHANICS]` Stop order khi trigger **trở thành market order**. Nó **tiêu thụ** thanh khoản chờ, không **cung cấp** thanh khoản. Phía cung cấp thật sự là limit orders đối ứng. Câu ICT "giá đi lấy thanh khoản của retail" mô tả đúng *hệ quả* (có aggressive flow được giải phóng) nhưng sai *cơ chế* (stops không phải là nguồn thanh khoản).

**Kết luận 2 — Pool trên chart là proxy, không phải phép đo.** `[INTERPRETATION]` Equal highs trên chart chỉ nói rằng *có khả năng* lệnh tập trung ở đó. Nó không nói có bao nhiêu, loại gì, hay còn hiệu lực không.

**Kết luận 3 — Trên spot FX, ngay cả phép đo cũng không tồn tại.** `[MARKET MECHANICS]` FX là thị trường OTC phân tán nhiều venue; không có một central order book mà retail nhìn thấy. Với FX, "pool" là suy luận thuần tuý. Với futures (NQ/ES), book tập trung hơn, nhưng stop orders vẫn **không hiển thị** như resting liquidity trước khi trigger.

## 4.2 Bar phân loại: Quan sát được / Suy luận được / Không thể biết

Đây là công cụ thực dụng nhất của cả bài. Mọi phát biểu về DOL nên được phân loại vào một trong ba cột này **trước khi** đưa vào trade plan.

| Quan sát được từ OHLC + volume | Suy luận được (có cơ sở) | Không thể biết từ chart |
|---|---|---|
| Giá cao nhất/thấp nhất | Nơi lệnh **có thể** tập trung | Lượng lệnh thật tại một mức |
| Thứ tự thời gian của các cực trị | Hướng của order-flow imbalance gần đây | Ý định của bất kỳ participant nào |
| Close / open / body / wick | Mức độ "sạch" hay "nhiễu" của một move | Đã có absorption hay chưa |
| Volume (nếu có) | Volatility regime | Ai mua, ai bán, vì sao |
| Cấu trúc swing (HH/HL/LH/LL) | Độ trễ xác nhận của cấu trúc | Stop ở đâu, bao nhiêu |
| Khoảng cách giữa các mức | Reachability tương đối | "Smart money" đang làm gì |
| Session boundaries, gap | Regime phân bố theo giờ | Có thuật toán nào đang điều khiển không |
| **Đã chạm mức nào, lúc nào** | **Xác suất tương đối (sau khi có base rate)** | **Liệu mức đó "được nhắm tới" hay không** |

> [!important] Dòng cuối cùng của bảng là toàn bộ vấn đề
> Cột 1 cho biết **cái gì đã xảy ra**. Cột 3 chứa **cái mà narrative ICT thường tuyên bố**. DOL là nỗ lực xây một cây cầu từ cột 1 sang cột 2 — **không bao giờ sang cột 3**. Mọi phát biểu nhảy sang cột 3 phải bị đánh dấu là `[INTERPRETATION]` và không được dùng làm cơ sở duy nhất cho lệnh.

## 4.3 Cơ chế có thể tạo ra "price moving toward clustered orders"

Protocol yêu cầu: không lặp lại lời giải thích ICT, mà nêu các cơ chế thị trường **có thể** tạo ra hiện tượng này. Có năm cơ chế, xếp theo mức độ bằng chứng.

**Cơ chế 1 — Stop clustering quanh round number** `[MARKET MECHANICS]`
Bằng chứng mạnh nhất hiện có. Nghiên cứu của Carol Osler trên dữ liệu order của một ngân hàng FX lớn ([Staff Report 125](https://www.newyorkfed.org/research/staff_reports/sr125.html), bản công bố trên *Journal of Finance* 58(5), 2003) kết luận: **requested execution rates của cả stop-loss và take-profit orders tập trung mạnh quanh round numbers**, và — quan trọng hơn — **pattern clustering của stop-loss và take-profit khác nhau rõ rệt**, cũng như giữa stop-loss-buy và stop-loss-sell. Tác giả trình bày đây là **giải thích vi mô cho hai dự đoán quen thuộc của technical analysis**: (1) trend có xu hướng **đảo** tại support/resistance dự đoán được, và (2) trend **tăng tốc** sau khi xuyên qua các mức đó.

Đây là điểm tựa vững nhất cho toàn bộ khái niệm pool: **cùng một mức giá có thể vừa đảo chiều vừa tăng tốc, và cả hai đều hợp lý** — vì take-profit orders và stop-loss orders nằm ở hai phía của mức đó và hành xử ngược nhau.

![[DOL-Microstructure-Stop-Loss-vs-Take-Profit.svg|697]]

*Hình 4 — Cơ chế vi mô của hai kết cục trái ngược trên cùng một mức giá. Khối dưới là chỗ bằng chứng **tự mâu thuẫn**: cơ chế được hỗ trợ, nhưng base rate (round-crossing ~5/ngày so với cascade ~1/tuần) buộc ta phải coi phần lớn lần chạm pool là nhiễu.*

> [!warning] Con số cụ thể — chưa verify được toàn văn
> [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] dẫn các con số: buy stops tập ở digits 01–10 gấp đôi vùng đối xứng (14,3% so với 6,9%); giá chạm round number đảo chiều 59,3% so với 54,8%; reversal do TP đóng trong <30 phút, acceleration do crossing kéo dài ≥2 giờ. **Các con số này đọc từ abstract/tóm tắt, chưa mở được bảng biểu gốc trong phiên này.** Dùng chúng như *gợi ý về độ lớn*, không phải như hằng số.

**Cơ chế 2 — Cascades tự củng cố** `[MARKET MECHANICS]`
Osler ([Staff Report 150](https://www.newyorkfed.org/research/staff_reports/sr150.html)) cung cấp bằng chứng rằng currency stop-loss orders **đóng góp vào các move nhanh, tự củng cố** ("rapid, self-reinforcing"). Cơ chế: stop bị trigger → market order → đẩy giá → trigger stop tiếp theo → cascade. Đây là cơ sở cho hiện tượng "displacement" sau khi xuyên một mức.

**Cơ chế 3 — Depth mỏng làm price impact tăng** `[MARKET MECHANICS]`
Nghiên cứu order book ([Cont, Kukanov & Stoikov](https://arxiv.org/abs/1011.6402)) cho thấy price change ngắn hạn liên hệ mạnh với order-flow imbalance, và **tác động giá lớn hơn khi market depth mỏng**. Hệ quả: cùng một lượng aggressive flow, ở vùng depth mỏng (pre-news, holiday, ngoài session) tạo displacement lớn hơn nhiều — và **kém bền hơn**.

**Cơ chế 4 — Attention/predictability tạo focal point** `[INTERPRETATION]`
Các mức dễ thấy (PDH, round number, equal highs) là focal points. Không cần giả định ai "nhắm" tới chúng: chỉ cần nhiều participant độc lập **đặt cùng loại lệnh ở cùng một chỗ** vì cùng một lý do (level hiển nhiên, thầy dạy giống nhau, indicator tự động). Kết quả là một cụm lệnh — nhưng **không có ai chủ ý tạo ra nó**. Đây là cơ chế quan trọng nhất để hiểu DOL **mà không cần** giả định một dealer toàn năng.

**Cơ chế 5 — Informed flow hội tụ** `[HYPOTHESIS]`
Nếu nhiều participant có cùng thông tin (ví dụ cùng đọc một mức cấu trúc), họ có thể cùng giao dịch về một hướng — tạo ra move "trông như có chủ đích". Cơ chế này **không thể phân biệt** với cơ chế 4 bằng dữ liệu giá. `[BACKTEST REQUIRED]`

## 4.4 Điều gì KHÔNG THỂ biết chỉ từ OHLC chart

Danh sách này phải được đọc như một danh sách **cấm kết luận**, không phải danh sách "khó":

1. **Lượng lệnh tại một mức.** Chart cho biết giá đã ở đó; không cho biết bao nhiêu lệnh chờ.
2. **Loại lệnh.** Không phân biệt được stop, limit, hay market order từ nến.
3. **Ai giao dịch.** Không có thông tin định danh. "Institution" và "retail" không phân biệt được trên chart.
4. **Absorption.** Một wick dài qua mức rồi quay lại **không** chứng minh có lệnh lớn hấp thụ; nó chỉ chứng minh giá đã giao dịch ở đó và sau đó không duy trì được.
5. **Inventory transfer.** Không biết hàng đã đổi tay hay chưa.
6. **Ý định.** Không suy ra được từ giá. Một "sweep" và một "breakout thất bại" có **cùng chữ ký giá** và khác nhau chỉ ở *kết quả sau đó* — và kết quả sau đó là tương lai.
7. **Hidden liquidity.** Iceberg/reserve orders không hiển thị; "hidden" trong microstructure là khái niệm kỹ thuật, không phải suy luận về ý định.
8. **Lý do của một move.** Move có thể do information, do flow kỹ thuật, do rebalancing, hoặc do noise — chart không phân biệt.

> [!danger] Lỗi nguy hiểm nhất trong chương này
> **Suy luận ý định của participant từ price chart.** Protocol cấm rõ điều này, và lý do rất cụ thể: với một tập dữ liệu giá duy nhất, có **vô số** cấu hình ý định tương thích. Nếu mô hình của bạn có thể giải thích mọi kết cục bằng cách gán một ý định khác nhau, mô hình đó **không có nội dung dự báo** — nó chỉ là một ngôn ngữ mô tả.

---

# 5. ICT Framework — gốc và diễn giải cộng đồng

## 5.1 ICT gốc đặt DOL ở đâu trong chuỗi

`[ICT FRAMEWORK]` Theo dòng Mentorship 2022, logic được trình bày theo chuỗi: xác định **weekly expectation** → dùng **daily** tìm swing highs/lows → quan sát **stops hoặc imbalance** mà giá có thể hướng tới → xuống lower timeframe tìm **stop run** và **structure shift** → vào lệnh tại PD array.

Điểm phải ghi nhận chính xác: **DOL nằm ở đầu chuỗi phân tích nhưng ở cuối chuỗi thực thi.** Nó là *destination* được đặt tên trước, và là *target* được chạm sau. Nó **không** nằm ở giữa như một điều kiện vào lệnh.

Mô hình cô đọng:

```
HTF expectation (weekly/daily)
    → destination (stops hoặc imbalance)
    → opposing liquidity raid (điều kiện)
    → MSS + displacement (xác nhận)
    → FVG / PD array (vị trí entry)
    → TARGET = destination ban đầu
```

Sai lệch phổ biến nhất của người học so với chuỗi này là **đảo vị trí DOL và MSS**: dùng DOL như điều kiện xác nhận ("giá đang hướng tới PDH nên tôi mua") thay vì như destination.

## 5.2 Bốn chỗ ICT gốc và cộng đồng diễn giải khác nhau

| Vấn đề | ICT gốc (theo dòng Mentorship 2022) | Diễn giải cộng đồng phổ biến | Đánh giá |
|---|---|---|---|
| **"Draw"** | Kỳ vọng có hướng, có thể không được chạm | "Nam châm" — giá *sẽ* tới | Cộng đồng biến heuristic thành định luật |
| **Vai trò** | Destination, có thể không hit vẫn có lệnh lời | Điều kiện xác nhận entry | Đảo ngược vị trí trong chuỗi |
| **Phạm vi** | Rộng: stops **và** imbalance | Thường chỉ nói về stops/BSL/SSL | Thu hẹp khái niệm, mất một nửa |
| **Tính tất yếu** | Xác suất, phụ thuộc context | "Giá luôn đi tìm liquidity" | Chuyển từ heuristic sang ontology |

> [!warning] Không được mặc định một explanation phổ biến là "official ICT definition"
> Cụm từ **"liquidity engineering"**, **"Judas swing"**, **"DOL hierarchy"** xuất hiện với nghĩa khác nhau ở các nguồn khác nhau. Khi đọc một nguồn thứ cấp, luôn hỏi: đây là **trích dẫn ICT**, hay là **diễn giải của tác giả**? Sự khác biệt này quyết định việc bạn có được phép coi nó là chuẩn hay không.
>
> Nếu các nguồn mâu thuẫn: **ghi nhận mâu thuẫn, không tự hoà giải.** Ví dụ [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] ghi nhận hai phe rõ rệt về chọn DOL — *nearest-first* vs *furthest-magnet* — và cách resolve trong note đó là **suy luận hoà giải của người viết, không phải đồng thuận nguyên văn**. Đó là cách trình bày trung thực.

## 5.3 Ba mệnh đề ICT cần dịch sang ngôn ngữ kiểm chứng được

Đây là bài tập dịch quan trọng nhất của chương. Mỗi mệnh đề ICT phải được dịch thành một mệnh đề **có thể sai**.

| Mệnh đề ICT | Dịch sang mệnh đề kiểm chứng được | Cách test |
|---|---|---|
| "Price is drawn to liquidity" | Sau khi một mức dễ thấy được hình thành, xác suất giá chạm mức đó trong $H$ cao hơn xác suất chạm một mức ngẫu nhiên cùng khoảng cách | So sánh hit rate của pool thật vs pool giả (cùng distance bucket) |
| "Judas quét ngược draw" | Trong các ngày có displacement một hướng, xác suất có một sweep phía đối diện **trước** displacement cao hơn base rate | Đếm conditional probability, so với base rate của sweep |
| "External liquidity là final objective" | Trong horizon dài, xác suất chạm external > xác suất chạm internal, **sau khi kiểm soát khoảng cách** | Competing-risks model có distance là covariate |

Chú ý dòng thứ ba: **"sau khi kiểm soát khoảng cách"** là phần dễ bị bỏ qua nhất. External thường xa hơn internal, nên nếu không kiểm soát distance, mọi kết quả đều bị confound.

---

# 6. DOL Causal / Decision Model

## 6.1 Đường đi từ dữ liệu tới quyết định

```
PRICE LOCATION
    ↓ (dữ liệu)
CURRENT MARKET STRUCTURE          ← cái gì vừa bị phá, cái gì đang được giữ
    ↓
DEALING RANGE (đóng băng)         ← khung quy chiếu cho mọi thứ phía sau
    ↓
AVAILABLE LIQUIDITY               ← mark TẤT CẢ pool, rộng rãi, chưa phán xử
    ↓ lọc Alignment + Freshness
STRUCTURAL SIGNIFICANCE           ← pool nào là structural, pool nào là inventory
    ↓ lọc Reachability
CANDIDATE DOLs                    ← 2–5 ứng viên, CÓ CẢ HAI PHÍA
    ↓ so sánh + chọn
RELATIVE DOL PRIORITY             ← candidate nào thắng, vì sao
    ↓
DIRECTIONAL EXPECTATION           ← hướng ưu tiên (có thể neutral)
    ↓ tách tầng
INTERMEDIATE OBJECTIVE            ← mức gần, trên đường đi
FINAL OBJECTIVE                   ← mức xa, kết thúc leg
    ↓
EXECUTION PLAN                    ← POI, entry, stop, size
    ↓
INVALIDATION                      ← sự kiện phá vỡ mệnh đề
    ↓
BACKTEST                          ← mệnh đề có sống sót ngoài mẫu không
```

## 6.2 Ba đặc tính bắt buộc của mô hình này

**Tính 1 — Thứ tự không được đảo.** Cụ thể: **dealing range phải được đóng băng trước khi mark pool.** Nếu mark pool trước rồi chọn range để phù hợp với pool muốn chọn, mọi kết luận sau đó đều bị nhiễm.

**Tính 2 — Mỗi bước phải có output viết ra được.** Không có bước nào được phép kết thúc bằng một cảm nhận. Dealing range phải là hai con số. Candidate phải là danh sách có giá. Invalidation phải là một sự kiện quan sát được.

**Tính 3 — Có ít nhất ba điểm dừng (no-trade).** Sau khi đóng băng range (nếu không đóng băng được → dừng), sau khi lọc candidate (nếu không có candidate hai phía → dừng), sau khi so sánh (nếu không có asymmetry → dừng).

## 6.3 Mô hình nhân quả — viết lại cho trung thực

**Cách viết SAI (nhân quả hoá narrative):**
> "Giá di chuyển vì nó tìm kiếm liquidity. Smart money đẩy giá tới pool để lấy stops của retail."

Vấn đề: (a) gán ý định cho một tác nhân không quan sát được; (b) biến một heuristic mô tả thành định luật nhân quả; (c) không thể sai — mọi kết cục đều khớp.

**Cách viết ĐÚNG (cơ chế + xác suất):**
> "Một số mức giá dễ dự đoán có thể tập trung conditional order flow. Khi giá tiếp cận và xuyên qua mức đó, các triggered orders, việc huỷ lệnh, độ sâu thị trường, và informed flow tương tác để tạo ra **hoặc** continuation **hoặc** rejection. DOL là dự báo thống kê về destination phát sinh từ cấu trúc bất đối xứng đó — và có thể sai."

Khác biệt then chốt: cách viết đúng **thừa nhận hai kết cục** và **thừa nhận khả năng sai**. Một mô hình không thừa nhận khả năng sai không phải mô hình — nó là tín ngưỡng.

## 6.4 Điểm khác biệt giữa DOL và các khái niệm gần nhất

| Khái niệm | Trả lời câu hỏi | Quan hệ với DOL |
|---|---|---|
| **DOL** | Đi đâu, và vì sao X thay vì Y | — |
| **Liquidity pool** | Ở đâu có thể có lệnh chờ | Nguyên liệu thô |
| **POI** | Vào lệnh ở đâu | Khác trục — POI nằm *trên đường* tới DOL |
| **Inducement (IDM)** | Cái gì bị quét trước để dụ | **Ngược hướng** DOL, là nhiên liệu |
| **PD array** | Vùng giá cụ thể để execute | Khác trục |
| **Daily Bias** | Hôm nay đứng phía nào | Tổng hợp, không đồng nhất (§10) |
| **Dealing range** | Khung quy chiếu | Điều kiện tiên quyết (§9) |
| **Target** | Chốt lời ở đâu | Lượng hoá vận hành của DOL |

> [!tip] Phép thử phân biệt nhanh nhất
> **POI là nơi bạn MUỐN giá tới. DOL là nơi bạn NGHĨ giá sẽ tới. IDM là nơi giá tới TRƯỚC đó.**
> Nếu một mức đóng cả ba vai trò trong cùng một kế hoạch, bạn đã nhầm — và thường là nhầm vì muốn có lệnh.

---

# 7. DOL Identification Framework

Framework gồm 19 thuộc tính. Với mỗi thuộc tính: **định nghĩa → cách đo quan sát được → diễn giải tiềm năng → giới hạn → khách quan/chủ quan → có test được không.**

Ký hiệu phân loại: **[O]** khách quan (tính được từ dữ liệu + tham số đã chốt) · **[S]** bán khách quan (khách quan sau khi chốt tham số, cần ghi tham số) · **[J]** chủ quan (phán đoán) · **[U]** không biết từ chart.

## 7.1 Nhóm cấu trúc

**1. Structural significance** [S]
- *Định nghĩa:* pool có phải là mốc mà MSS/BOS tham chiếu, hoặc là cực trị của dealing range đang hoạt động.
- *Đo:* kiểm tra nhị phân — "nếu mức này bị phá, cấu trúc có đổi không?" Có = structural.
- *Diễn giải:* pool structural là ứng viên DOL hợp lệ; inventory pool là fuel.
- *Giới hạn:* câu hỏi này dễ bị trả lời "có" cho quá nhiều mức nếu dealing range chưa đóng băng.
- *Test:* so hit rate của structural vs inventory pool trong cùng distance bucket.

**2. Higher-timeframe relevance** [S]
- *Định nghĩa:* pool được tạo trên timeframe nào và còn hiệu lực ở timeframe nào.
- *Đo:* gán nhãn timeframe nguồn (D1/H1/M5) + đếm số timeframe cùng chỉ về mức đó (stacking).
- *Diễn giải:* HTF pool thắng LTF pool khi xung đột (veto + size), nhưng không thay thế T1 của timeframe đang trade.
- *Giới hạn:* stacking nhiều timeframe **không** phải nhiều bằng chứng độc lập — cùng một sự kiện giá nhìn qua nhiều khung.
- *Test:* hit rate theo số timeframe stack; kiểm tra có vượt baseline distance không.

**3. External vs internal** [O sau khi range đóng băng]
- *Định nghĩa:* pool nằm ngoài hay trong hai endpoint của frozen dealing range.
- *Đo:* so sánh giá pool với range high/low đã chốt.
- *Diễn giải:* external = final objective; internal = intermediate.
- *Giới hạn:* **chỉ có nghĩa nếu range đóng băng trước**. Đổi range = đổi nhãn.
- *Test:* độ ổn định của nhãn dưới các phương pháp chọn range khác nhau (robustness test bắt buộc).

**4. Market structure alignment** [S]
- *Định nghĩa:* pool nằm cùng phía với structural event gần nhất.
- *Đo:* xác định event gần nhất (BOS/MSS/sweep) đã confirm, lấy dấu của nó.
- *Diễn giải:* đây là **điều kiện 1** của candidate.
- *Giới hạn:* nếu không có event confirm nào → không có candidate, đây là neutral.
- *Test:* so hit rate khi alignment đúng vs ngược.

## 7.2 Nhóm vị trí & khoảng cách

**5. Distance** [O]
- *Định nghĩa:* khoảng cách từ giá hiện tại tới pool, chuẩn hoá.
- *Đo:* `d = |price − level| / ATR_n` hoặc `/ ADR`.
- *Diễn giải:* reachability; distance ngắn → xác suất chạm cao hơn **một cách tầm thường**.
- *Giới hạn:* ⚠️ **đây là confounder lớn nhất của toàn bộ nghiên cứu DOL.** Distance ngắn làm tăng hit rate mà không cần bất kỳ edge nào. Mọi so sánh **bắt buộc** phải trong cùng distance bucket.
- *Test:* hit rate theo distance decile — nếu edge chỉ tồn tại ở decile gần nhất, "edge" đó là distance, không phải DOL.

**6. Dealing-range position** [O sau khi range đóng băng]
- *Định nghĩa:* vị trí tương đối trong range, biểu diễn bằng % hoặc z-score.
- *Đo:* `pos = (price − range_low) / (range_high − range_low)`.
- *Diễn giải:* thông tin **về vị trí**, không phải về hướng (§9).
- *Giới hạn:* không suy ra hướng. Discount không có nghĩa là bullish.
- *Test:* tương tác giữa pos và hướng DOL — có phải edge chỉ tồn tại khi pos cực trị?

**7. Premium / discount** [O]
- *Định nghĩa:* nhãn nhị phân từ `pos` với ngưỡng 50% (hoặc OTE bands).
- *Đo:* `premium ⟺ pos > 0.5`.
- *Diễn giải:* bộ lọc vị trí cho phép/không cho phép tìm entry theo hướng.
- *Giới hạn:* phụ thuộc hoàn toàn vào anchor range. Cùng một giá là premium trong range này và discount trong range khác.
- *Test:* độ nhạy của kết quả theo cách chọn anchor.

**8. Relative location of competing liquidity** [O]
- *Định nghĩa:* khoảng cách và chất lượng của candidate đối thủ gần nhất phía bên kia.
- *Đo:* `competitor_distance`, `competitor_quality`.
- *Diễn giải:* DOL là bài toán so sánh. Candidate mạnh đối thủ yếu = asymmetry cao.
- *Giới hạn:* chất lượng đối thủ dùng cùng score → circular nếu không cẩn thận.
- *Test:* đây là **feature trung tâm** — test riêng như một predictor.

## 7.3 Nhóm chất lượng pool

**9. Age of liquidity** [O]
- *Định nghĩa:* số bars kể từ khi pool được hình thành (hoặc từ lần cuối được xác nhận).
- *Đo:* `bars_since_formation`, đo từ thời điểm pool **được biết**, không phải từ bar swing.
- *Diễn giải:* hai giả thuyết đối lập — pool cũ có thể tích luỹ nhiều lệnh hơn (mạnh hơn), hoặc đã bị test nhiều và mòn (yếu hơn). **Không được giả định trước.**
- *Giới hạn:* pool cũ thường ở xa hơn → confound với distance.
- *Test:* hit rate theo age bucket, **trong cùng distance bucket**.

**10. Number of touches** [O]
- *Định nghĩa:* số lần giá tiếp cận pool (trong tolerance) mà không xuyên qua.
- *Đo:* đếm số bar có high/low nằm trong $[level - \varepsilon, level + \varepsilon]$, gộp cluster.
- *Diễn giải:* nhiều touch → nhiều lệnh tích luỹ → pool dày hơn; HOẶC nhiều touch → phản ứng mòn → dễ phá hơn. Hai giả thuyết đối lập.
- *Giới hạn:* phụ thuộc $\varepsilon$; nhạy với data convention. Touch phụ thuộc timeframe.
- *Test:* so sánh hai giả thuyết — một chiều (monotonic) hay chữ U?

**11. Equalness / clustering** [S]
- *Định nghĩa:* có bao nhiêu cực trị trong cùng một cửa sổ tolerance, tolerance rộng bao nhiêu.
- *Đo:* `|high_i − high_j| < ε · ATR` với ε chốt trước. Đếm số cực trị trong cụm.
- *Diễn giải:* equal highs/lows là **dấu hiệu** khả năng tập trung lệnh và là mức rất dễ thấy.
- *Giới hạn:* ⚠️ **"imperfect" equal highs** (chênh vài tick) phụ thuộc hoàn toàn vào ε. Đổi ε đổi số pool → đổi DOL. Đây là một trong những tham số nguy hiểm nhất.
- *Test:* sensitivity analysis trên ε bắt buộc; nếu kết quả đảo khi ε đổi ±50%, edge là artifact của tham số.

**12. Swept / unswept / partially swept** [O]
- *Định nghĩa:* trạng thái tiêu thụ của pool.
- *Đo:* `max(high) sau khi hình thành > level + buffer` → swept. "Partial" cần định nghĩa riêng (ví dụ: wick vượt nhưng không có close vượt).
- *Diễn giải:* unswept = còn tiềm năng; swept = hết vai trò pool.
- *Giới hạn:* "partially swept" là khái niệm mơ hồ — phải định nghĩa trước.
- *Test:* ba định nghĩa (wick-only / close / time-limited reclaim) phải test **riêng**, không gộp.

**13. Swing magnitude** [O]
- *Định nghĩa:* độ lớn của leg tạo ra cực trị.
- *Đo:* `(swing_high − prior_swing_low) / ATR`.
- *Diễn giải:* swing lớn = cấu trúc quan trọng hơn, nhiều stop hơn.
- *Giới hạn:* tương quan cao với structural significance → hai feature không độc lập.
- *Test:* xem có thêm information sau khi đã có structural significance (ablation).

**14. Displacement from level** [O]
- *Định nghĩa:* tốc độ và độ lớn của move rời khỏi pool lần cuối.
- *Đo:* `body/ATR`, `TR/median_TR`, số bars để đi được X ATR, có FVG hay không.
- *Diễn giải:* displacement rời pool cho thấy phản ứng mạnh → pool quan trọng.
- *Giới hạn:* displacement cũng là **hệ quả** của việc pool bị tiêu thụ — không phải bằng chứng độc lập về chất lượng pool.
- *Test:* displacement như quality filter cho MSS signal (§20, ablation).

**15. Mitigation state** [S]
- *Định nghĩa:* nếu pool trùng với một PD array (FVG/OB), array đó đã được mitigate chưa.
- *Đo:* giá đã quay lại chạm array chưa (theo rule).
- *Diễn giải:* unmitigated array tại pool → phản ứng mạnh hơn.
- *Giới hạn:* phụ thuộc định nghĩa mitigation (chạm CE? full fill? close vào?).
- *Test:* so hit rate unmitigated vs mitigated, cùng distance.

## 7.4 Nhóm bối cảnh

**16. Timeframe alignment** [O]
- *Định nghĩa:* mức độ D1, H1, M5 cùng chỉ về một hướng.
- *Đo:* đếm số timeframe đồng thuận (0–3).
- *Diễn giải:* alignment cao → conviction cao hơn; LTF đẹp mà HTF ngược → skip.
- *Giới hạn:* **không phải nhiều bằng chứng độc lập** — cùng một dữ liệu giá nhìn qua nhiều khung. Đếm 3 = double/triple counting.
- *Test:* nếu alignment không thêm information sau khi có HTF structure, nó là redundant.

**17. Market regime** [S]
- *Định nghĩa:* trạng thái phân phối hiện tại: trending / ranging / expansion / compression / event-driven.
- *Đo:* phân loại bằng rule (ví dụ: ADX-like, ATR percentile, hiệu quả của trend qua tỷ lệ net move / tổng move).
- *Diễn giải:* DOL behavior khác nhau hoàn toàn theo regime — trong trend, pool thường bị phá; trong range, pool thường tạo phản ứng.
- *Giới hạn:* phân loại regime là **ex-post** dễ hơn ex-ante. Phải dùng rule causal.
- *Test:* regime là **stratifier bắt buộc** trong mọi báo cáo.

**18. Session / timing context** [O]
- *Định nghĩa:* pool nằm trong session nào; thời điểm hiện tại so với killzone.
- *Đo:* gán nhãn Asia/London/NY; phút so với open và so với release.
- *Diễn giải:* session H/L là pool khách quan; delivery thường tập trung trong killzone.
- *Giới hạn:* session definition phụ thuộc timezone/DST — nguồn lỗi dữ liệu phổ biến. Index futures còn phụ thuộc RTH vs ETH.
- *Test:* stratify theo session; kiểm tra edge có phải chỉ là session effect.

**19. Distance to opposing liquidity** [O]
- *Định nghĩa:* khoảng cách tới candidate đối thủ mạnh nhất phía bên kia.
- *Đo:* `d_opp` chuẩn hoá, và `d_own / d_opp` (tỷ lệ bất đối xứng).
- *Diễn giải:* tỷ lệ này là **biến gần nhất với chính khái niệm DOL**. Nếu DOL có nội dung, nó phải nằm ở đây.
- *Giới hạn:* — 
- *Test:* ⭐ **đây nên là feature số 1 được test.** Baseline tự nhiên: nếu chỉ dùng nearest-first rule, tỷ lệ này ≈ 1 luôn.

> [!important] Hai feature có khả năng mang information cao nhất
> Nếu chỉ được test ba feature, chọn: **#8/#19 (bất đối xứng hai phía)**, **#12 (freshness)**, **#2 (HTF relevance)**. Lý do: đây là ba feature mà mô hình DOL tuyên bố *khác* baseline nearest-first. Các feature còn lại phần lớn là biến thể của distance hoặc của salience.

---

# 8. DOL Hierarchy

> [!note] Nhãn phân loại
> Toàn bộ "hierarchy" trong chương này là **[ANALYTICAL FRAMEWORK]** — khung do chúng ta xây, **không phải terminology chính thức của ICT**. ICT nói về destination ở các timeframe khác nhau; việc đặt tên **Primary / Secondary / Intermediate / Final** và gán quan hệ thứ bậc là cấu trúc phân tích của bài này.

## 8.1 Thứ bậc hai trục

Sai lầm phổ biến là dùng một trục duy nhất. Thực tế có **hai trục độc lập**:

![[DOL-Hierarchy-Hai-Truc-Timeframe-Va-Vai-Tro.svg|697]]

*Hình 5 — Hai trục tách biệt. Khối dưới liệt kê bốn chế độ phân giải conflict hợp lệ, và chế độ thứ năm bị cấm: "giữ nguyên DOL cũ nhưng diễn giải lại".*

**Trục A — Timeframe (ai có quyền phủ quyết)**
```
Monthly / Weekly DOL   ← quyền phủ quyết về HƯỚNG và SIZE
        ↓
Daily DOL              ← chọn final objective của ngày
        ↓
H1 DOL                 ← chọn intermediate objective
        ↓
M5 DOL                 ← chỉ timing, gần như không có quyền
```

**Trục B — Vai trò trong leg (cái gì chạm trước)**
```
Intermediate objective  ← pool gần, chạm trước, dùng partial
        ↓
Final objective         ← pool xa, kết thúc leg, dùng runner
```

**Điểm mấu chốt:** hai trục này **không đồng nhất**. Một intermediate objective có thể là D1 DOL (nếu nó gần), và một final objective có thể là H1 DOL (nếu H1 range lớn). Gộp hai trục là nguồn gốc của phần lớn nhầm lẫn về "DOL hierarchy".

## 8.2 Cấu trúc chuẩn

| Tầng | Nguồn | Vai trò | Horizon | Chốt lời |
|---|---|---|---|---|
| **HTF DOL** (W/D1) | PWH/PWL, D1 swing, D1 FVG | Final objective; veto hướng và size | Nhiều ngày → nhiều tuần | Runner, không partial |
| **Intermediate DOL** (H1) | PDH/PDL, H1 swing, session extremes | Intermediate objective; xác nhận path | Trong ngày | Partial chính (ví dụ 50%) |
| **LTF DOL** (M5) | M5 equal highs/lows, intraday extremes | Waypoint; dùng để quản lý | Trong session | Partial nhỏ, hoặc chỉ để trail |

## 8.3 Sáu câu hỏi bắt buộc — trả lời

**Hỏi 1: Khi nào HTF và LTF DOL cùng hướng?**
Khi structural state ở cả hai tầng nhất quán: ví dụ D1 vừa BOS lên và giữ HL, H1 cũng đang trong leg tăng với HL được giữ. Đây là trường hợp **alignment cao** — nhưng phải nhớ nó **không phải nhiều bằng chứng độc lập** (feature #16).

**Hỏi 2: Khi nào conflict?**
Ba dạng conflict khác nhau, **không được gộp**:
- **Conflict thật:** D1 yêu cầu tiếp tục lên, H1 vừa MSS xuống với displacement. → HTF veto: chỉ T1, nửa size, hoặc no-trade.
- **Conflict biểu kiến (path vs destination):** D1 DOL ở trên, H1 DOL ở dưới. → **Không phải conflict** — lower là path event trước upper destination. Đây là trường hợp phổ biến nhất và bị gọi nhầm là conflict nhiều nhất.
- **Conflict do chọn range khác nhau:** hai tầng dùng hai dealing range khác nhau nên cùng một mức được gán nhãn khác nhau. → Lỗi phương pháp, không phải thông tin thị trường.

**Hỏi 3: Khi nào HTF context override LTF objective?**
Ba điều kiện, cần **cả ba**: (a) LTF candidate đi ngược structural state của HTF đã confirm; (b) LTF candidate không phải là một phần của path hợp lệ tới HTF DOL; (c) có sự kiện cấu trúc HTF mới (close vượt boundary) chứ không chỉ wick. Nếu thiếu (c), phần lớn trường hợp là conflict biểu kiến.

**Hỏi 4: Khi nào LTF liquidity chỉ là temporary objective?**
Mặc định. LTF pool **luôn** là temporary trừ khi nó trùng với một HTF pool (stacking) hoặc trùng endpoint của HTF dealing range.

**Hỏi 5: Khi nào liquidity gần trở thành intermediate objective?**
Khi nó qua được Alignment + Freshness (hai điều kiện không phụ thuộc khoảng cách). **Gần không làm nó thành objective** — gần chỉ làm nó *dễ chạm*, mà dễ chạm thì không cần mô hình.

**Hỏi 6: Khi nào external liquidity trở thành final objective?**
Khi: (a) nó là endpoint của HTF dealing range đang hoạt động; (b) reachability trong horizon của tầng đó (có thể là nhiều ngày, không phải intraday); (c) không có opposing HTF POI chặn giữa đường. Nếu (b) fail, nó **không bị xoá** — nó chỉ chuyển sang horizon dài hơn. Đây chính là cơ chế tạo ra hierarchy.

## 8.4 Bốn chế độ phân giải conflict — dùng khi bối rối

| Chế độ | Điều kiện áp dụng | Hành động |
|---|---|---|
| **A — Path split** | Hai tầng khác hướng nhưng cùng phục vụ một leg HTF | Chấp nhận cả hai: LTF là path event, HTF là destination. Ghi rõ **thứ tự kỳ vọng** |
| **B — HTF veto** | LTF ngược HTF structure đã confirm | Chỉ T1, nửa size, hoặc no-trade |
| **C — Neutral** | Hai phía tương đương về chất lượng và khoảng cách | **No-trade.** Đây là output hợp lệ |
| **D — Re-select** | Có structural event mới (close vượt boundary, MSS HTF) | Xây lại candidate set từ đầu; candidate cũ hết hiệu lực |

> [!danger] Cấm chế độ thứ năm
> Chế độ ẩn thường được dùng: **"giữ nguyên DOL cũ nhưng diễn giải lại"** — tức là D1 DOL vẫn ở trên, nhưng vì giá đi xuống nên ta gọi move xuống là "liquidity engineering" và DOL trên vẫn còn hiệu lực. Đây không phải phân tích, đây là **narrative tự chữa mình**. Nếu giá đi ngược DOL và vượt invalidation, DOL **sai**. Ghi vào journal là sai, rồi xây lại.

---

# 9. DOL + Dealing Range

## 9.1 Quan hệ bốn chiều

```
DEALING RANGE  ──── định nghĩa ────→  PREMIUM / DISCOUNT
      │                                      │
      │ định nghĩa                           │ lọc vị trí
      ↓                                      ↓
EXTERNAL / INTERNAL                    ENTRY PERMISSION
      │                                      │
      └──────────→  LIQUIDITY  ←─────────────┘
                       │
                       ↓
                 CANDIDATE DOL
```

Dealing range **không** dự báo hướng. Nó làm ba việc: (1) phân loại external/internal; (2) cung cấp anchor cho premium/discount; (3) cung cấp mức invalidation tự nhiên.

## 9.2 Điều kiện tiên quyết: đóng băng range

> [!warning] Không có range đóng băng thì không có phân tích DOL
> Đây là **điều kiện tiên quyết**, không phải bước tùy chọn. Nếu range được redraw trong ngày, mọi nhãn external/internal và premium/discount **mất tính khách quan** — và tệ hơn, trader sẽ vô thức redraw cho tới khi nhãn phù hợp với lệnh muốn vào. Đó là **look-ahead bias ở dạng thuần tuý nhất**.

**Rule đề xuất:**
1. Range dùng **confirmed swing endpoints** hoặc **fixed lookback** đã định trước. Ghi phương pháp vào journal.
2. Range **không** được redraw trong ngày, trừ khi endpoint bị **đóng cửa (close)** phá vỡ theo rule đã viết.
3. External = ngoài hai endpoint. Mọi target giữa endpoint là internal/intermediate.
4. Nếu không xác định được range ổn định → **no-trade**.

## 9.3 Bốn case — phân tích đầy đủ

Protocol yêu cầu phân tích bốn case với: liquidity map, structural context, candidate DOLs, cái gì ủng hộ, cái gì phản bác, và thông tin còn thiếu. Đây là phần phải đọc chậm.

> [!warning] Không được giả định
> **Discount → bullish.** **Premium → bearish.** Cả hai đều **sai** như quy tắc. Premium/discount là **thông tin về vị trí**, không phải về hướng. Nó trả lời "chỗ này có lợi cho entry theo hướng nào", không trả lời "hướng nào sẽ xảy ra".

### Case A — Price in discount + BSL above

| | |
|---|---|
| **Liquidity map** | BSL phía trên (PDH, equal highs, D1 swing high). SSL phía dưới (session low, PDL, D1 swing low). |
| **Structural context** | Cần xác định: structural state hiện tại là gì? Nếu bullish (BOS lên, HL giữ) → BSL là candidate aligned, SSL là fuel. Nếu bearish → SSL là candidate aligned, và discount chỉ là **waypoint** trên đường tiếp tục xuống. |
| **Candidate DOLs** | (A1) BSL trên nếu structural state bullish. (A2) SSL dưới nếu structural state bearish. |
| **Ủng hộ A1** | Vị trí discount ủng hộ **entry long** (không phải ủng hộ destination). Nếu có SSL vừa bị sweep + reclaim → A1 mạnh. |
| **Ủng hộ A2** | Nếu D1 vừa close dưới range low → discount chỉ là điểm giữa của leg giảm; A2 aligned và A1 bị loại bởi Alignment. |
| **Phản bác A1** | Nếu BSL trên là *imbalance* hoặc đã bị test nhiều lần; nếu opposing HTF POI nằm ngay dưới BSL. |
| **Phản bác A2** | Nếu không có structural event bearish nào confirm; nếu SSL dưới đã bị swept (hết freshness). |
| **Thông tin còn thiếu** | (1) Structural event gần nhất là gì? (2) BSL trên đã bị test bao nhiêu lần? (3) Có SSL vừa bị sweep không? (4) Anchor range là D1 hay H1? |
| **Kết luận vận hành** | **Discount không quyết định gì cả.** Case A chỉ trở thành bullish khi Alignment (BSL trên + structural state bullish) thỏa. Nếu structural state bearish, discount là **bẫy trực giác** phổ biến nhất. |

### Case B — Price in discount + SSL below

| | |
|---|---|
| **Liquidity map** | SSL phía dưới gần (session low, equal lows). BSL phía trên xa hơn. |
| **Structural context** | Đây là case **nguy hiểm nhất về mặt trực giác**: giá ở discount (trông rẻ) nhưng SSL ở ngay dưới (trông như sẽ bị quét). |
| **Candidate DOLs** | (B1) BSL trên nếu SSL dưới là fuel cho một reversal long. (B2) SSL dưới nếu structural state bearish. |
| **Ủng hộ B1** | Vị trí discount + bullish HTF structure + SSL dưới là pool gần, nhỏ, kiểu **inducement**. Trong mô hình AMD, manipulation đi xuống lấy SSL rồi mới distribution lên. |
| **Ủng hộ B2** | D1/H1 đang trong leg giảm có displacement; SSL dưới là **continuation target** chứ không phải manipulation. |
| **Phản bác B1** | Discount mà structural state chưa bullish = chưa có Alignment. "Rẻ" không phải lý do. |
| **Phản bác B2** | SSL đã bị test nhiều lần (mòn); hoặc có bullish HTF POI ngay tại SSL (SSL là POI, không phải target). |
| **Thông tin còn thiếu** | ⭐ **Phân biệt quyết định:** SSL dưới là **inducement** (nhỏ, gần, trước POI thật) hay **target** (là điểm kết thúc của leg)? Câu trả lời nằm ở **vị trí POI** — nếu có POI chất lượng ngay dưới SSL, SSL là inducement; nếu không, SSL là target. |
| **Kết luận vận hành** | Case B là nơi **hai DOL cạnh tranh thật sự** — không thể giải bằng vị trí, chỉ giải bằng cấu trúc + POI location. |

### Case C — Price in premium + BSL above

| | |
|---|---|
| **Liquidity map** | BSL trên (gần). SSL dưới (xa hơn, thường là external). |
| **Structural context** | Premium + BSL gần trên — trực giác là "còn lên nữa để lấy đỉnh". Nhưng premium là vùng **bất lợi cho entry long** trong mô hình premium/discount. |
| **Candidate DOLs** | (C1) BSL trên — continuation. (C2) SSL dưới — reversal/rebalance. |
| **Ủng hộ C1** | Structural state bullish mạnh (D1 BOS, compression vào level). Trong trend mạnh, premium **không** ngăn continuation — đây là điểm mà mô hình premium/discount thuần tuý thất bại. |
| **Ủng hộ C2** | Nếu giá vừa vào một HTF bearish POI trong premium; nếu BSL trên đã bị test nhiều lần; nếu approach vào BSL là "vertical/exhaustive". |
| **Phản bác C1** | Entry long từ premium có R:R xấu; không có discount POI để entry. |
| **Phản bác C2** | Không có structural event bearish nào; fade một trend đang mạnh chỉ vì "đang ở premium". |
| **Thông tin còn thiếu** | (1) Approach structure là compression hay exhaustion? (2) BSL trên có phải là external endpoint của HTF range không? (3) Có HTF POI tại vùng premium hiện tại không? |
| **Kết luận vận hành** | **Case C là nơi mô hình premium/discount thuần tuý thất bại thường xuyên nhất.** Premium chỉ chặn *entry permission*, không chặn *destination*. Nếu structural state bullish, BSL trên vẫn là DOL — chỉ là **entry sẽ ở chỗ khác** (chờ pullback về discount, hoặc chấp nhận continuation entry với R:R thấp hơn). |

### Case D — Price in premium + SSL below

| | |
|---|---|
| **Liquidity map** | SSL dưới (xa). BSL trên (gần hoặc đã tiêu thụ). |
| **Structural context** | Đây là cấu hình **bearish chuẩn** theo mô hình: premium + SSL dưới = short. Nhưng cũng có thể là **bullish pullback** trong trend tăng. |
| **Candidate DOLs** | (D1) SSL dưới — nếu bearish structural state. (D2) BSL trên mới — nếu SSL dưới là pullback trong trend tăng. |
| **Ủng hộ D1** | Premium + bearish event (MSS xuống, close dưới HL) + SSL dưới là external hoặc equal lows chưa quét. |
| **Ủng hộ D2** | HTF bullish structure nguyên vẹn; premium chỉ là điểm hồi của leg tăng; SSL dưới là **discount POI** cho long tiếp. |
| **Phản bác D1** | SSL dưới đã bị swept; hoặc HTF structure vẫn bullish (D1 vẫn HH/HL). |
| **Phản bác D2** | Không có bullish POI ở SSL; SSL xa và không reachable trong horizon. |
| **Thông tin còn thiếu** | ⭐ Lần quét gần nhất ở phía nào, và có reclaim không? Nếu BSL trên vừa bị swept + reclaim xuống → D1 mạnh. Nếu SSL dưới vừa bị swept + reclaim lên → D2 mạnh. |
| **Kết luận vận hành** | Trong case D, **premium/discount và DOL thường cùng hướng** → đây là case dễ nhất về vị trí, và vì thế cũng là case mà trader **bỏ qua việc kiểm tra Alignment nhiều nhất**. Kỷ luật: vẫn phải kiểm tra structural event. |

> [!summary] Bảng tổng hợp bốn case — điều duy nhất cần nhớ
> | Case | Vị trí | Trực giác sai | Điều quyết định thật |
> |---|---|---|---|
> | A | Discount + BSL trên | "Discount → long" | Structural state, không phải vị trí |
> | B | Discount + SSL dưới | "Discount → long, SSL sẽ bị quét" | SSL là inducement hay target (POI location) |
> | C | Premium + BSL trên | "Premium → short" | Trend mạnh vượt qua premium; entry ở chỗ khác |
> | D | Premium + SSL dưới | "Premium → short, chắc chắn" | Vẫn phải kiểm Alignment |
>
> **Điều duy nhất cả bốn case dạy:** vị trí trong dealing range là **bộ lọc entry**, không phải **bộ dự báo hướng**. Nó không bao giờ trả lời "đi đâu" — chỉ trả lời "vào ở đây có hợp lý không".

![[DOL-Bon-Case-Dealing-Range-Premium-Discount.svg|697]]

*Hình 9 — Bốn case dạng bảng 2×2. Case B (discount + SSL dưới) và Case C (premium + BSL trên) là hai chỗ mà trực giác sai thường xuyên nhất, và cũng là hai chỗ mô hình premium/discount thuần tuý thất bại.*

---

# 10. DOL + Daily Bias

## 10.1 Ba model — không được mặc định chiều nhân quả

![[DOL-Ba-Model-Bias-Va-Circular-Reasoning.svg|697]]

*Hình 6 — Ba model và chỗ circular reasoning xuất hiện. Model C là dạng duy nhất không circular về logic, nhưng khối cuối chỉ ra nó vẫn có thể bị biến thành circular bằng cách lặp vô hạn — và kết quả "khớp" đó là artifact của việc lặp.*

**Model A — DOL → directional expectation → Daily Bias**

*Logic:* nhìn thấy pool rõ nhất, suy ra giá sẽ tới đó, từ đó có bias.

*Điểm mạnh:* nhanh, dùng được ngay khi chỉ có một destination nổi bật.

*Điểm chết:* **circular.** Trong thực hành, bước "chọn pool rõ nhất" gần như luôn được thực hiện **sau khi** đã có cảm nhận về hướng. Trader bullish sẽ thấy BSL "rõ" hơn SSL. Model A không có cơ chế phát hiện điều này, vì nó **không yêu cầu** so sánh hai phía — mà không so sánh thì không có gì để kiểm tra.

**Model B — Daily Bias → candidate DOL selection**

*Logic:* xác định bias trước từ HTF structure, rồi chọn DOL phù hợp với bias.

*Điểm mạnh:* tránh circular ở dạng thô; bias có nguồn gốc độc lập.

*Điểm chết:* **confirmation bias có cấu trúc.** Nếu bias được chốt trước mà không có tiêu chí bác bỏ, bước chọn DOL chỉ còn là hợp lý hoá. Bias "bullish" sẽ luôn tìm được một BSL nào đó để gọi là DOL — trên chart nào cũng có đỉnh. Model B cần một **cơ chế bác bỏ**: nếu sau khi chọn DOL mà không viết được candidate đối thủ mạnh, bias phải bị nghi ngờ.

**Model C — Market Structure + Liquidity + Dealing Range → directional hypothesis → DOL selection**

*Logic:* ba nguồn **độc lập về mặt dữ liệu** cùng tạo ra một hypothesis có xác suất; sau đó DOL được chọn như **hệ quả** của hypothesis, và hypothesis phải chịu kiểm tra coherence với DOL.

*Điểm mạnh:* đây là dạng duy nhất **không circular về mặt logic**, vì bias và DOL được suy ra từ **cùng một tập dữ liệu quá khứ** như hai output song song, không phải output này từ output kia.

*Điểm chết:* vẫn có thể **iterative circularity** — chọn bias sơ bộ → thấy DOL không hợp → sửa bias → thấy DOL hợp. Vấn đề này có thật nhưng **kiểm soát được** bằng stopping rule (§10.3).

## 10.2 Đánh giá: Model C là coherent nhất

**Lý do 1 — Cấu trúc nhân quả.** Model A và B đều đặt một output làm input của output kia. Model C đặt cả hai là output của một tập input chung. Về mặt logic, chỉ C là một **hệ phương trình** thay vì một **vòng lặp**.

**Lý do 2 — Có thể bác bỏ.** Model C cho phép phát biểu: "Nếu structure không phải X, hoặc liquidity không ở Y, thì bias sai." Model A không cho phép điều đó vì bias được định nghĩa *bằng* DOL.

**Lý do 3 — Khớp với cấu trúc D1/H1/M5 của framework.** Trong framework này, D1 cung cấp cả structure **và** liquidity **và** range. Ba thứ đó cùng có sẵn ở cùng một tầng — nên Model C không cần thêm dữ liệu, chỉ cần thay đổi **thứ tự xử lý**.

## 10.3 Stopping rule chống iterative circularity

Đây là phần vận hành quan trọng nhất của chương. Vấn đề: dù dùng Model C, trader vẫn có thể lặp vô hạn giữa bias và DOL cho tới khi hai thứ khớp nhau — và kết quả khớp đó là **artifact của việc lặp**, không phải thông tin thị trường.

**Rule đề xuất — chỉ được lặp một lần:**

1. **Vòng 1 (bắt buộc, viết ra trước):** từ structure + range + liquidity map, viết ra (a) directional hypothesis thô, (b) candidate hai phía, (c) asymmetry sơ bộ. Không được sửa.
2. **Coherence check:** hypothesis và asymmetry có nhất quán không? Cụ thể: nếu hypothesis là bullish nhưng candidate mạnh nhất lại ở phía dưới, có **lý do cấu trúc** nào giải thích không (ví dụ: candidate trên đã bị swept, hoặc lower candidate là external endpoint)?
3. **Vòng 2 (cho phép, tối đa một lần):** nếu coherence fail, được phép sửa **một trong hai** — hypothesis hoặc candidate set — và phải **ghi rõ lý do sửa**. Không được sửa cả hai.
4. **Sau vòng 2:** nếu vẫn không coherence → **neutral**. Đây không phải thất bại; đây là output đúng. Neutral phải xuất hiện thường xuyên (mục tiêu tham khảo: ≥25–30% số ngày) — nếu không, mô hình đang tự bịa ra bias.

## 10.4 Điều không thể xác định từ price data

> [!warning] Nói rõ giới hạn
> **Không thể xác định chiều nhân quả giữa Daily Bias và DOL từ dữ liệu giá.** Lý do: dữ liệu giá chỉ chứa **kết quả**, không chứa **quá trình ra quyết định**. Cả ba model đều có thể tạo ra cùng một bộ quan sát.
>
> Điều **có thể** xác định: model nào **vận hành tốt hơn** — đo bằng (a) tỷ lệ bias đúng trên out-of-sample, (b) tỷ lệ circular reasoning phát hiện được trong journal, (c) calibration của confidence. Đó là câu hỏi empirical, không phải câu hỏi logic.
>
> Nói cách khác: **Model C coherent hơn về logic. Nhưng "coherent hơn" không đồng nghĩa "có edge hơn".** Đây là chỗ phải tách `[INTERPRETATION]` khỏi `[HYPOTHESIS]`.

---

# 11. DOL + Market Structure

Nguyên tắc trung tâm: **DOL không được phân tích độc lập với structural state.** Market structure trả lời *delivery hiện tại đã phá vỡ điều gì*; DOL trả lời *delivery có thể hướng tới đâu*. Hai câu hỏi khác nhau, nhưng câu thứ hai vô nghĩa nếu không có câu thứ nhất.

![[DOL-Epistemic-Ladder-Sau-Bac.svg|697]]

*Hình 7 — Epistemic ladder sáu bậc. Ba kiểu nhảy bậc sai ở panel phải là cách ladder bị vi phạm trong thực hành: intent leap (2→5), label leap (1→3), và confirm leap (6→5).*

## 11.1 Bảng: structural event → tác động lên DOL

| Sự kiện | Định nghĩa vận hành | Tác động lên candidate set | Loại |
|---|---|---|---|
| **BOS continuation** | Close vượt swing gần nhất **cùng** hướng với leg hiện tại | **Củng cố** candidate cùng hướng. Thêm pool mới (đỉnh/đáy vừa tạo) | `[ICT FRAMEWORK]` |
| **MSS** | Close vượt swing ngược hướng leg vừa sweep | **Tạo** candidate mới ngược phía vừa sweep. Candidate cũ cùng phía sweep bị hạ ưu tiên | `[ICT FRAMEWORK]` |
| **External shift** | Close vượt dealing-range boundary | **Invalidate** range cũ. Bắt buộc re-select toàn bộ. Range mới phải được đóng băng lại | `[ANALYTICAL FRAMEWORK]` |
| **Liquidity sweep (có reclaim)** | Vượt level rồi close trở lại trong range | **Củng cố** candidate phía đối diện. Pool vừa bị sweep chuyển sang trạng thái spent | `[ICT FRAMEWORK]` |
| **Liquidity sweep (không reclaim)** | Vượt level và giữ phía ngoài | **Củng cố** candidate tiếp theo **cùng hướng** (continuation), không phải reversal | `[INTERPRETATION]` |
| **Displacement** | Leg nhanh, body lớn, để lại FVG | **Quality filter** cho event ở trên, không phải event độc lập | `[ICT FRAMEWORK]` |
| **Consolidation mới** | Nhiều bar chồng lấn, không có cực trị mới | **Không tác động** candidate HTF, nhưng tạo pool LTF mới (thường là noise) | `[INTERPRETATION]` |
| **Sweep kép hai phía** | Cả BSL và SSL bị swept trong thời gian ngắn | **Reset** narrative. Ghi rõ rule: sweep thứ nhất có hủy setup không? | `[ANALYTICAL FRAMEWORK]` |

## 11.2 Bốn tác động, không phải hai

Protocol yêu cầu phân tích bốn loại tác động. Điểm quan trọng: **chúng không phải hai cặp đối xứng**, mà là bốn loại logic khác nhau:

**1. Strengthen (củng cố)** — BOS cùng hướng candidate, hoặc sweep có reclaim phía đối diện. *Cơ chế:* cấu trúc xác nhận delivery đang đi đúng hướng.

**2. Weaken (làm yếu)** — pool bị test nhiều lần mà không phá; displacement giảm dần khi tiến gần candidate; opposing POI mới xuất hiện trên đường. *Cơ chế:* phản ứng mòn hoặc có vật cản mới.

**3. Invalidate (vô hiệu hoá)** — close vượt invalidation đã viết trước; hoặc external shift. *Cơ chế:* mệnh đề DOL đã bị dữ liệu mới phủ định. **Không được diễn giải lại — phải đóng và xây lại.**

**4. Create new candidate (tạo candidate mới)** — không chỉ là hệ quả của invalidate. Một MSS có thể tạo candidate mới **mà không** vô hiệu hoá candidate HTF cũ (nếu candidate HTF nằm xa hơn, ngoài horizon). Đây là cơ chế tạo ra **path split** ở §8.4 chế độ A.

## 11.3 Ranh giới cứng: close so với wick

Toàn bộ chương này phụ thuộc vào một quyết định định nghĩa: **break được xác nhận bằng close hay bằng wick?**

- **Close-based:** ít tín hiệu giả, xác nhận muộn hơn, mất phần đầu của move.
- **Wick-based:** nhạy hơn, nhiều tín hiệu giả, và **không tái lập được** (phụ thuộc tick data).

Hai lựa chọn này tạo ra **hai mô hình khác nhau**, không phải hai tham số của cùng một mô hình. Không được trộn trong cùng một backtest — và phải tuyên bố chọn cái nào **trước** khi xem kết quả.

> [!tip] Khuyến nghị thực dụng
> Dùng **close-based** cho structural event (BOS/MSS/external shift) và **wick-based** cho sweep detection. Lý do: một cấu trúc chỉ thực sự đổi khi thị trường **chấp nhận** mức mới (close), trong khi một sweep chỉ cần **chạm** để tiêu thụ lệnh chờ (wick đủ). Đây là `[INTERPRETATION]`, và bản thân lựa chọn này là một biến cần test.

---

# 12. D1 → H1 → M5 Application

Chương này trả lời câu hỏi trung tâm: **DOL dùng cho ENTRY hay TARGET?**
Trả lời ngắn: **TARGET và DIRECTIONAL CONTEXT. Không bao giờ là entry trigger.**
Trả lời đầy đủ: DOL đóng **bốn vai trò khác nhau ở bốn bước khác nhau**, và không vai trò nào là entry trigger.

## 12.1 Bảng 13 bước

| Bước | Hành động | DOL đóng vai trò gì | Output phải viết ra |
|---|---|---|---|
| **1** | D1 structure | Chưa tham gia. Chỉ đọc HH/HL/LH/LL | Structural state (bullish/bearish/undefined) |
| **2** | D1 dealing range | Chưa tham gia. Nhưng **quyết định** external/internal sau này | 2 con số: range high, range low + phương pháp |
| **3** | D1 liquidity map | DOL **chưa** xuất hiện — chỉ mark pool rộng rãi | Danh sách pool có giá, cả hai phía |
| **4** | Candidate DOL | **Vai trò 1: lọc + so sánh.** Pool → candidate → DOL | Upper DOL, lower competitor, invalidation |
| **5** | H1 structure | Kiểm tra path: đường tới DOL có sạch? | Path assessment + opposing POI list |
| **6** | H1 liquidity refinement | **Vai trò 2: phân tầng.** Chọn intermediate objective | T1 (intermediate), T2 (final) |
| **7** | H1 POI | DOL **không** tham gia tại đây | POI level + entry-side liquidity cần raid |
| **8** | Price approaches POI | **Vai trò 3: kiểm tra coherence.** Approach có phù hợp với DOL không? | Re-assessment: DOL còn hiệu lực? |
| **9** | M5 liquidity event | DOL **im lặng**. Sweep là điều kiện setup | Sweep confirmed (close verdict) |
| **10** | MSS | DOL **im lặng**. MSS là structural event | MSS confirmed với pivot pre-defined |
| **11** | Displacement | DOL **im lặng**. Displacement là quality filter | Displacement metrics |
| **12** | FVG / Entry | **Vai trò 4: kiểm tra R:R.** DOL quyết định target, không quyết định entry | Entry, stop, net R tới T1 |
| **13** | Target | DOL **là** target | Chốt lời theo tầng |

## 12.2 Bốn vai trò, tách bạch rõ

**Vai trò 1 — Directional context (Bước 4).** DOL trả lời *"ưu tiên phía nào"*. Đây là vai trò duy nhất nó chia sẻ với bias.

**Vai trò 2 — Target selection (Bước 6, 13).** DOL trả lời *"chốt ở đâu"*. Đây là vai trò chính.

**Vai trò 3 — Coherence check (Bước 8).** DOL trả lời *"approach này có phù hợp với kỳ vọng không"*. Đây là vai trò ít được nhận ra nhất và hữu ích nhất — nó là **cơ chế tự bác bỏ** ở giữa quy trình.

**Vai trò 4 — R:R filter (Bước 12).** DOL trả lời *"khoảng cách còn lại có đủ trả cho risk không"*. Nếu DOL đã gần, hoặc target nằm ngay trước opposing POI, setup bị loại — **dù DOL đúng**.

## 12.3 Bốn khái niệm không được trộn

Protocol yêu cầu phân biệt rõ bốn thứ. Đây là bảng phân biệt:

| | Câu hỏi | Nguồn | Kiểm tra được? |
|---|---|---|---|
| **Directional context** | Đi phía nào? | D1 structure + range + candidate asymmetry | Có — qua coherence check |
| **Target selection** | Chốt ở đâu? | DOL tầng tương ứng | Có — reachability + R:R |
| **Entry location** | Vào ở đâu? | H1/M5 POI (FVG/OB/OTE) | Có — định nghĩa array |
| **Invalidation** | Cái gì làm mệnh đề sai? | Structural event ngược | Có — phải viết trước |

> [!danger] Lỗi chí mạng: biến DOL thành entry trigger
> Cách dùng sai: *"PDH là DOL nên tôi mua ở đây để giá đi lên PDH."* Vấn đề không nằm ở việc PDH có phải DOL hay không. Vấn đề là **câu đó không nói gì về entry**. Không có POI, không có sweep, không có xác nhận cấu trúc — chỉ có một destination và một lệnh.
>
> DOL là lý do để **giữ lệnh**, không phải lý do để **mở lệnh**. Nếu bạn vào lệnh vì DOL, bạn đang dùng một công cụ chọn target như một công cụ chọn timing — và timing sai thì target đúng vẫn thua.

## 12.4 Hai template, không được trộn

| | **Reversal-to-DOL** | **Continuation-to-DOL** |
|---|---|---|
| **Điều kiện** | Opposing liquidity raid + reclaim | Price đã displacement theo hướng DOL, pullback nông |
| **Sweep bắt buộc?** | Có | Không |
| **MSS** | Ngược leg vừa raid | Theo continuation |
| **POI** | Discount POI sau raid | HTF FVG/OB trên đường |
| **Rủi ro chính** | Morph thành continuation (raid thất bại) | Morph thành exhaustion (pullback quá sâu) |
| **Bỏ sót gì nếu dùng nhầm** | Nếu dùng continuation logic cho reversal day: vào lệnh trước raid, bị quét | Nếu dùng reversal logic cho continuation day: short vào sweep trong trend, thua liên tục |

Lỗi phổ biến nhất trong thực hành: **dùng reversal logic trong continuation regime** — thấy bất kỳ high nào bị sweep là short, dù HTF DOL vẫn cao hơn và giá đang accept trên high.

---

# 13. Multiple Liquidity Pools — FILTER → RANK → SELECT

## 13.1 Ví dụ so sánh năm candidate

Bảng dưới minh hoạ **cách điền**, không phải kết quả thị trường. Giá trị là **thang điểm tương đối trong cùng một lần đánh giá**, không phải điểm tuyệt đối.

| Feature | L1 (PDH) | L2 (equal highs H1) | L3 (D1 swing high) | L4 (PWH) | L5 (session high) |
|---|---|---|---|---|---|
| HTF relevance | Trung | Thấp | Cao | Cao nhất | Thấp |
| Structural significance | Trung | Thấp | Cao | Cao | Thấp |
| Distance (ATR) | 0,6 | 0,3 | 1,4 | 2,1 | 0,2 |
| External / Internal | Internal | Internal | External | External | Internal |
| Age (bars) | 1 ngày | 6 giờ | 5 ngày | 8 ngày | 4 giờ |
| Touch count | 1 | 3 | 1 | 0 | 4 |
| Sweep status | Unswept | Unswept | Unswept | Unswept | Partially |
| Dealing-range relevance | Trong range | Trong range | Cận boundary | Ngoài range | Trong range |
| Opposing liquidity | SSL dưới xa | SSL dưới xa | SSL dưới xa | SSL dưới xa | SSL dưới gần |
| **Nhãn vận hành** | **T1 candidate** | Fuel/waypoint | Final objective | Multi-day objective | **Không đủ tư cách** |

**Đọc bảng này thế nào:**
- **L5 bị loại ngay** — touch count cao (4) + partially swept + HTF relevance thấp. Đây là pool đã mòn.
- **L2 bị hạ xuống fuel** — touch count 3, HTF relevance thấp, structural significance thấp. Nó là **inducement**, không phải target.
- **L1 là T1** — distance gần nhất trong nhóm candidate hợp lệ, internal, unswept. Nhưng phải nhớ: **gần không phải lý do để nó được chọn** — nó được chọn vì nó là candidate hợp lệ gần nhất, và điều đó chỉ có nghĩa là xác suất chạm cao một cách tầm thường.
- **L3 và L4 là final objectives** ở hai horizon khác nhau.

## 13.2 FILTER — loại trước khi chấm điểm

**Đây là bước quan trọng nhất và bị bỏ qua nhiều nhất.** Chấm điểm trước khi lọc là cách chắc chắn nhất để tạo ra một ranking vô nghĩa.

**Bộ lọc loại cứng (hard filters) — không qua = loại, không được cộng điểm bù:**

| # | Điều kiện loại | Lý do |
|---|---|---|
| F1 | Pool không phải structural swing | Inventory swing là fuel, không phải target |
| F2 | Pool đã bị trade-through (swept + displacement rời đi) | Hết freshness, thành phần lệnh đã tiêu thụ |
| F3 | Pool ngược hướng với structural state đã confirm | Fail Alignment (điều kiện 1) |
| F4 | Pool vượt reachability của horizon | Không phải candidate của horizon này (xem §8) |
| F5 | Pool nằm ngoài session được nghiên cứu | Ngoài phạm vi mô hình |
| F6 | Pool hình thành trong news spike mà không có xác nhận | Nhiễu repricing, không phải cấu trúc |
| F7 | Không xác định được dealing range ổn định | **Điều kiện tiên quyết fail → no-trade toàn bộ** |

**Bộ lọc mềm (soft filters) — qua được nhưng bị hạ ưu tiên và ghi nhận:**
- Touch count cao (>2): hạ ưu tiên, không loại (vì giả thuyết "mòn" chưa được test).
- Age rất cao (>20 bars HTF): hạ ưu tiên.
- Pool trùng khu vực có opposing HTF POI: hạ ưu tiên nặng.

## 13.3 RANK — mô hình chấm điểm

> [!danger] [HYPOTHESIS — BACKTEST REQUIRED]
> **Toàn bộ mô hình scoring dưới đây là GIẢ THUYẾT.** Không có bằng chứng nào cho thấy các trọng số này có predictive power. Mục đích của nó là **thu thập dữ liệu có cấu trúc**, không phải tạo ra edge. Nếu bạn dùng nó để vào lệnh trước khi backtest, bạn đang tin vào một bảng tính chưa được kiểm chứng.

| Thành phần | Khoảng điểm | Cơ sở lý thuyết | Confounder chính |
|---|---|---|---|
| HTF alignment | 0 đến +2 | Pool ở tầng cao hơn có nhiều lệnh hơn | Tương quan với distance |
| Externality trong frozen range | 0 đến +2 | External là final objective | Phụ thuộc phương pháp chọn range |
| Freshness | 0 đến +2 | Pool chưa tiêu thụ còn lệnh chờ | Tương quan nghịch với touch count |
| Salience / objectivity | 0 đến +2 | Level dễ thấy → nhiều lệnh (cơ chế focal point) | **Có thể là artifact của chính mô hình ICT** |
| Reachability (ATR/ADR) | 0 đến +2 | Gần → dễ chạm (tầm thường) | ⚠️ Chính là distance confound |
| Path obstruction | 0 đến −2 | Có opposing POI trên đường | Định nghĩa POI |
| Opposite candidate strength | 0 đến −2 | Đối thủ mạnh → asymmetry thấp | Circular nếu dùng cùng score |
| News / regime penalty | 0 đến −2 | Regime khác → mô hình khác | Gán nhãn chủ quan |

**Tổng:** −8 đến +12.

**Ba cảnh báo bắt buộc về score này:**

1. **"Reachability" và "distance" là cùng một thứ.** Nếu score có cả `Distance` và `Reachability`, bạn đang đếm hai lần. Chọn một.
2. **"Salience" có thể chỉ là artifact.** Một level "dễ thấy" đối với **người học ICT** không nhất thiết dễ thấy với toàn thị trường. Nếu edge chỉ tồn tại ở các level mà ICT dạy là quan trọng, đó có thể là **self-fulfilling ở quy mô nhỏ** hoặc là **overfitting vào giáo trình**.
3. **"Opposite candidate strength" dùng cùng score → đệ quy.** Phải dùng một phiên bản **rút gọn** của score cho đối thủ, hoặc dùng một proxy độc lập (ví dụ: distance tới đối thủ, HTF relevance của đối thủ).

**Threshold khởi điểm (chỉ để bắt đầu thu thập dữ liệu):**
- Chênh lệch tổng điểm giữa DOL và đối thủ < 2 → **neutral, no-trade**.
- Chênh lệch ≥ 3 → có asymmetry, cho phép lập kế hoạch.
- **Các ngưỡng này KHÔNG có cơ sở thực nghiệm.** Chúng là điểm khởi đầu để calibration sau.

## 13.4 SELECT — quy tắc quyết định

```
1. Áp hard filters F1–F7  →  còn lại candidate set
2. Nếu candidate set rỗng ở MỘT phía  →  kiểm tra lại việc mark pool (thường là lỗi mark)
3. Nếu candidate set rỗng ở CẢ HAI phía  →  NO-TRADE (neutral)
4. Chấm điểm (score) cả hai phía
5. Tính asymmetry = best_upper_score − best_lower_score
6. Nếu |asymmetry| < threshold  →  NO-TRADE (neutral)
7. Nếu không  →  DOL = phía có score cao hơn
8. Gán tầng: candidate gần nhất hợp lệ cùng hướng = intermediate (T1)
              candidate xa nhất hợp lệ cùng hướng = final (T2)
9. Viết invalidation: sự kiện nào làm bước 7 sai?
```

**Điểm mấu chốt ở bước 8:** T1 và T2 **phải cùng hướng**. Nếu "T1" và "T2" nằm hai phía, đó không phải hai tầng target — đó là hai kịch bản trái ngược, và mô hình đang tự bảo hiểm để luôn đúng.

---

# 14. Failure Model

## 14.1 Ba lớp failure — phân biệt bằng tiêu chí

Protocol yêu cầu phân biệt ba loại. Sự phân biệt này quan trọng vì **cách sửa khác nhau hoàn toàn**.

| | **Type 1 — Prediction failed** | **Type 2 — Interpretation invalid** | **Type 3 — Thesis obsolete** |
|---|---|---|---|
| **Định nghĩa** | Candidate được xác định **hợp lý** theo mô hình, nhưng giá không tới trong horizon | Candidate được chọn dựa trên **reasoning sai ngay từ đầu** | Candidate **từng** hợp lý, nhưng market state đổi làm nó hết hiệu lực |
| **Dấu hiệu nhận biết** | Quy trình đúng; candidate qua hết filter; có đối thủ; invalidation không bị chạm; giá đi ngang hoặc tới candidate khác | Kiểm tra lại tại cutoff: candidate **không** qua được filter, hoặc **không có** đối thủ, hoặc dealing range không đóng băng được | Có một sự kiện cấu trúc rõ ràng **sau** cutoff làm đổi state |
| **Đây có phải lỗi?** | **Không.** Đây là chi phí bình thường của dự báo xác suất | **Có.** Lỗi quy trình | **Không**, nếu đã re-select đúng lúc. **Có**, nếu vẫn giữ thesis cũ |
| **Cách sửa** | Không sửa mô hình vì một mẫu. Đo base rate | Sửa **quy trình lọc**, thêm filter, viết rule chặt hơn | Sửa **quy tắc cập nhật** — định nghĩa rõ sự kiện nào trigger re-select |
| **Nguy hiểm nếu chẩn đoán sai** | Chẩn đoán Type 1 thành Type 2 → overfit mô hình vào noise | Chẩn đoán Type 2 thành Type 1 → **không bao giờ sửa được lỗi hệ thống** | Chẩn đoán Type 3 thành Type 1 → giữ thesis đã chết ("narrative tự chữa mình") |

> [!danger] Type 2 là loại nguy hiểm nhất vì nó vô hình
> Type 2 không tạo ra dấu hiệu nào ở thời điểm xảy ra — nó chỉ là một quyết định tồi trông giống một quyết định tốt. Cách duy nhất phát hiện: **audit lại quyết định tại cutoff, không nhìn kết quả.** Đây là lý do journal phải lưu **snapshot bất biến** tại cutoff — nếu bạn chỉ lưu ảnh sau khi trade xong, Type 2 là không thể chẩn đoán.

![[DOL-Failure-Model-Ba-Lop.svg|697]]

*Hình 8 — Ba lớp failure và thứ tự audit đúng. Khối cuối là hệ quả vận hành quan trọng nhất: nếu chỉ lưu ảnh sau khi trade xong, Type 2 là **không thể** chẩn đoán.*

## 14.2 Chín nguyên nhân — và chúng thuộc lớp nào

| Nguyên nhân | Mô tả | Thường là lớp nào |
|---|---|---|
| **Opposite liquidity taken first** | Phía đối diện bị quét trước rồi giá mới đi | Type 1 hoặc 3 |
| **Structural shift** | BOS/MSS ngược hướng xuất hiện sau cutoff | Type 3 (nếu có event rõ) / Type 1 (nếu là noise) |
| **New liquidity formation** | Pool mới hình thành gần hơn, hấp thụ draw | Type 3 |
| **Regime change** | Trending → ranging (hoặc ngược) | Type 3 |
| **Consolidation** | Giá đi ngang, không tới đâu | Type 1 |
| **Volatility shock** | ATR tăng vọt, target cũ trở nên quá gần hoặc quá xa | Type 3 |
| **News repricing** | Thông tin làm giá nhảy qua cả hai phía | Type 3 (và là lý do phải có news filter) |
| **POI failure** | POI dự kiến không tạo phản ứng | **Type 2** nếu POI được chọn bằng hindsight; Type 1 nếu POI hợp lệ |
| **Liquidity losing structural relevance** | Pool già đi, cấu trúc xung quanh đổi, pool không còn là mốc | Type 3 |

## 14.3 Điều quan trọng nhất về failure model

**Phần lớn failure trong thực hành không phải Type 1.** Khi audit lại, đa số trường hợp "DOL không hit" thực ra là **Type 2 (reasoning sai từ đầu) hoặc Type 3 (thesis đã chết nhưng không được cập nhật)**. Lý do rất đơn giản: Type 1 đòi hỏi toàn bộ quy trình phải đúng — và quy trình đúng là điều hiếm.

Hệ quả thực hành:

> [!important] Câu hỏi audit đúng
> Đừng hỏi *"tại sao DOL không hit?"* — câu đó mời gọi một câu chuyện.
> Hỏi: **"Tại cutoff, candidate này có qua được cả ba điều kiện Alignment / Reachability / Freshness không, và tôi có viết đối thủ của nó ra không?"**
> Nếu câu trả lời là **không** → Type 2. Không cần phân tích thêm gì về thị trường.
> Nếu **có**, hỏi tiếp: **"Có sự kiện cấu trúc nào sau cutoff làm đổi state không?"**
> Nếu **có** → Type 3. Nếu **không** → Type 1. Chỉ khi đó mới bắt đầu phân tích thị trường.

---

# 15. Case Studies

> [!warning] Đọc trước — đây là gì và không là gì
> **Sáu case dưới đây không phải trade lịch sử.** Không có ngày, không có giá thật, không có P&L. Chúng là **case templates cấu trúc** — mô tả *hình dạng* của một tình huống và *chuỗi lập luận* áp dụng cho nó.
>
> Lý do: protocol cấm tạo case study chỉ để minh hoạ một câu chuyện đẹp, và vault có house rule **không được bịa dữ liệu trade**. Một case study có giá thật nhưng không có screenshot thật sẽ là dữ liệu bịa — dù trông chuyên nghiệp hơn.
>
> **Cách dùng đúng:** đọc case như một **khuôn lập luận**, rồi tự điền dữ liệu thật từ chart của bạn vào cùng khuôn đó. Khi bạn điền được, bạn đã hiểu khuôn. Mục tiêu cuối cùng của chương này không phải sáu case — mà là **bảng discriminating features ở §15.7**.

## 15.1 Bullish case 1 — Reversal sau raid, DOL là PDH

**Market state:** D1 structural state bullish (BOS lên đã confirm, HL gần nhất được giữ). Giá đang ở nửa dưới frozen D1 range (discount). Asia hình thành range hẹp, low nằm ngay dưới một H1 bullish FVG.

**Liquidity map:** SSL: Asia low, một equal low H1, PDL (đã swept hôm trước). BSL: PDH, equal highs H1, một D1 swing high xa hơn.

**Candidate DOLs:**
- Upper: PDH (distance ~0,7 ADR, internal nhưng gần boundary, unswept, structural reference cho H1) → **T1**
- Upper: D1 swing high (distance ~1,8 ADR) → **T2**
- Lower: Asia low (distance ~0,2 ADR) → **bị loại khỏi target vì ngược Alignment** → chuyển vai trò thành **Judas fuel**

**Selection reasoning:** Chỉ phía trên có candidate hợp lệ. Asia low **không** phải candidate DOL — nó là entry-side liquidity. Đây là điểm phân biệt quan trọng nhất của case: **cùng một pool, hai vai trò khác nhau, không được lẫn.**

**Structural confirmation:** London sweep Asia low → close reclaim trong 2 nến → M5 break một **pre-confirmed** swing high (được xác nhận bằng N-bar pivot trước đó, không phải pivot chọn sau) → displacement với body > 70% range → bullish FVG hình thành.

**Execution:** Entry tại first retracement vào FVG. Stop dưới wick của cú sweep (không phải dưới FVG — vì luận điểm cấu trúc là "Asia low đã bị lấy và giữ"). Target: T1 = PDH (partial 50%), T2 = D1 swing high (runner).

**Invalidation:** M5/H1 close trở lại dưới Asia low **mà không reclaim**, hoặc D1 close dưới HL gần nhất.

## 15.2 Bullish case 2 — Continuation, không có opposing sweep

**Market state:** D1 vừa có bullish expansion close qua một external high. Structural state bullish mạnh. Giá đang ở premium của range **cũ** (đã bị vượt).

**Liquidity map:** BSL phía trên: weekly high (distance ~1,2 ADR), một D1 FVG chưa fill. SSL phía dưới: D1 FVG vừa tạo bởi expansion (chưa fill).

**Candidate DOLs:**
- Upper: weekly high (external, unswept, cao nhất về HTF relevance) → **final objective**
- Lower: D1 FVG vừa tạo → **bị loại khỏi target — nó là POI, không phải destination**

**Selection reasoning:** Sau expansion, FVG vừa tạo là **POI cho pullback**, không phải target. Nhầm nó thành target là lỗi staging phổ biến ("chốt ở cú lấp FVG trong khi delivery thật nằm ở weekly high").

**Structural confirmation:** H1 pullback **nông** vào FVG (không reach Asia low, không sweep bất cứ gì) → M5 compression highs → close qua intraday high bằng displacement → M5 FVG mới.

**Execution:** Entry first retracement vào M5 FVG. Stop dưới low của pullback. Target: weekly high.

**Điểm phân biệt của case:** **không có sweep đối nghịch nào cả.** Ép buộc "phải sweep sell-side trước khi long" là lỗi mô hình — nó bỏ lỡ toàn bộ continuation day và khiến trader short sai sau mỗi micro high sweep.

**Invalidation:** H1 close trở lại dưới đáy của FVG đã dùng làm POI (mitigation fail), hoặc pullback vượt quá 100% của expansion leg.

## 15.3 Bullish case 3 — Old DOL chết, candidate mới xuất hiện

**Market state:** D1 bullish nhưng đã **bị tiêu thụ** — PDH bị swept trong phiên trước với displacement rời đi. Range cũ đã bị vượt.

**Liquidity map:** BSL: mức cao nhất của expansion (vừa tạo), một D1 FVG chưa fill phía trên. SSL: chân của expansion (đã bị swept).

**Candidate DOLs:**
- Upper: high của expansion vừa tạo → **candidate mới**
- Lower: chân expansion → **bị loại: đã swept** (Freshness fail)

**Selection reasoning:** Sau khi PDH bị tiêu thụ, PDH **không còn là DOL**. Đây là rule "swept = spent". Cần xây candidate set mới — và candidate mới **không được lấy từ pool cũ đã swept**, dù nó trông vẫn "quan trọng".

**Structural confirmation:** H1 retrace không reclaim swept high → tạo HL mới → M5 MSS lên + displacement + FVG.

**Execution:** Entry FVG retracement. Stop dưới HL mới. Target: high của expansion.

**Invalidation:** Giá close trở lại **dưới** swept high và giữ ở đó → có thể là bearish acceptance, không phải continuation.

**Bài học:** việc re-select candidate **không phải** thất bại của mô hình — đó là mô hình đang hoạt động đúng.

## 15.4 Bearish case 1 — Reversal sau raid, DOL là PDL

**Market state:** D1 structural state bearish (BOS xuống confirm, LH gần nhất được giữ). Giá ở premium của frozen D1 range. H1 có bearish FVG gần Asia high.

**Liquidity map:** BSL: Asia high, equal highs H1, PDH (đã swept). SSL: PDL, equal lows H1, một D1 swing low xa hơn.

**Candidate DOLs:**
- Lower: PDL (distance ~0,6 ADR, unswept, internal) → **T1**
- Lower: D1 swing low (distance ~1,6 ADR, external) → **T2**
- Upper: Asia high → **Judas fuel** (ngược Alignment)

**Structural confirmation:** NY raid Asia high → close trở lại dưới high → M5 break **pre-confirmed** M5 swing low → displacement xuống → bearish FVG.

**Execution:** Entry first retracement vào FVG. Stop trên wick của raid. Target: T1 = PDL (partial), T2 = D1 swing low.

**Invalidation:** M5/H1 acceptance trên Asia high + chuỗi HL tiếp tục. **Một wick quay lại dưới high mà không có bearish displacement chưa đủ.**

## 15.5 Bearish case 2 — Buy-side consumed, DOL chuyển xuống PWL

**Market state:** PDH và một D1 old high bị xuyên vào bearish D1 POI, nhưng daily close **thất bại** và trở lại dưới old high. H1 phá higher-low cuối bằng close quyết định.

**Liquidity map:** BSL: PDH (đã swept). SSL: PDL, PWL (external, unswept, HTF relevance cao nhất).

**Candidate DOLs:**
- Lower: PDL (internal) → **T1**
- Lower: PWL (external, weekly relevance) → **T2 / final**
- Upper: PDH → **bị loại: đã swept**

**Selection reasoning:** Đây là case **"sweep + fail to accept"** — distinction trung tâm. "High bị sweep" **chỉ là điều kiện cần**. Điều kiện đủ là **inability to re-accept above**: close thất bại, không reclaim được trong N nến.

**Structural confirmation:** H1 retrace không reclaim swept high → M5 raid một internal high trong premium → bearish MSS + displacement + FVG → short.

**Execution:** Entry bearish FVG retracement. Stop trên internal high vừa raid. Target T1 = PDL, T2 = PWL.

**Invalidation:** H1 close trở lại **trên** swept high. Lúc đó luận điểm "fail to accept" đã bị phủ định.

## 15.6 Bearish case 3 — Continuation sau bearish expansion

**Market state:** D1 đã close dưới prior range low (external shift bearish). Lower DOL kế tiếp còn cách xa. H1 pullback vào SIBI/bearish FVG nhưng **không** chạm session high.

**Liquidity map:** SSL: prior range low (đã swept), lower external liquidity (distance ~1,1 ADR). BSL: session high (chưa chạm).

**Candidate DOLs:**
- Lower: external liquidity phía dưới → **final objective**
- Upper: session high → **không đủ tư cách** (không phải structural swing, chỉ là intraday extreme)

**Structural confirmation:** M5 tạo lower high → phá intraday low bằng displacement → để lại bearish FVG.

**Execution:** Short tại FVG retracement. Stop trên lower high. Target: external liquidity.

**Điểm phân biệt:** **Không cần dựng một buy-side sweep giả trên M1/M5.** Continuation structure phù hợp với D1 acceptance có thể mạnh hơn một reversal signature nhỏ — và việc đi tìm sweep ở khung quá nhỏ là dấu hiệu đang cố hợp lý hoá một lệnh đã muốn vào.

## 15.7 Sáu counterexample — setup trông hợp lệ nhưng KHÔNG nên trade

Đây là phần có giá trị nhất của chương. Mỗi counterexample phải có: setup trông thế nào → tại sao trông hợp lệ → tại sao thực tế không nên trade → **feature phân biệt**.

| # | Setup trông thế nào | Tại sao trông hợp lệ | Tại sao KHÔNG trade | ⭐ Feature phân biệt |
|---|---|---|---|---|
| **CE1** | Sell-side sweep + micro bullish MSS trong khi D1 đang bearish expansion và vừa close dưới old low | Có sweep, có MSS, có FVG — đủ bộ ba ICT | Equal low M5 là **internal waypoint**; D1/H1 đang **accept** dưới range. Micro break không phá H1 bearish delivery | **Structural state của tầng trên**: nếu HTF chưa reclaim external low, "sweep" chỉ là pause trước continuation |
| **CE2** | Buy-side sweep tại equal highs trong compression breakout, sau đó short vì "liquidity taken" | Có sweep rõ, có level rõ, có vẻ hết đà | Approach structure là **compression + acceptance**, không phải exhaustion. Compression vào level → continuation xác suất cao hơn fade | ⭐ **Approach structure**: compression (pullback nông, HL nâng dần) vs exhaustion (vertical, dùng hết range) |
| **CE3** | MSS được "xác nhận" bởi một micro pivot chỉ 2 nến trước đó; body nhỏ, không FVG | Có break, có nhãn MSS | Pivot **không được xác nhận trước** break (hindsight pivot); không displacement | ⭐ **Pivot có pre-confirmed không** (N-bar pivot với N chốt trước, timestamp tại lúc biết) |
| **CE4** | Setup đẹp (raid + MSS + FVG) vài phút trước CPI/NFP/FOMC | Mọi thành phần ICT đều đủ | News làm **depth giảm, spread tăng, volatility tăng**; repricing do thông tin khác cơ chế với liquidity event | ⭐ **News flag + exclusion window**; đây là regime khác, không phải setup xấu |
| **CE5** | DOL đúng hướng nhưng chỉ cách entry chưa tới một structural stop; hoặc target nằm ngay trước fresh opposing POI | Dự báo đúng | Prediction edge ≠ execution edge. R:R sau costs không đủ | ⭐ **Net R sau costs tới T1** — không phải gross |
| **CE6** | Giá giữa dealing range, upper và lower candidate tương đương; M5 sweep hai phía liên tục; trader đổi bias theo MSS cuối cùng | Luôn có MSS mới để theo | Không có asymmetry → neutral. M5 structure dễ whipsaw | ⭐ **Asymmetry score giữa hai phía** — nếu < threshold, no-trade bất kể M5 nói gì |

> [!important] Bốn feature phân biệt rút ra từ sáu counterexample
> Tổng hợp CE1–CE6, bốn feature xuất hiện lặp lại như yếu tố phân biệt **thật sự**:
> 1. **Structural state của tầng trên** (CE1) — không phải hình dạng của M5.
> 2. **Approach structure** — compression vs exhaustion (CE2). Đây là feature **bị đánh giá thấp nhất** trong thực hành.
> 3. **Pre-confirmation của pivot** (CE3) — thuộc về quy trình, không thuộc về chart.
> 4. **Asymmetry hai phía** (CE6) — điều kiện tiên quyết, không phải yếu tố cộng thêm.
>
> Chú ý: **không feature nào trong bốn cái này là một mẫu hình nến.** Cả bốn đều là **thuộc tính của bối cảnh hoặc của quy trình**. Đây là bằng chứng mạnh nhất cho luận điểm trung tâm của bài: edge (nếu có) nằm ở **bối cảnh và kỷ luật quy trình**, không nằm ở **pattern recognition**.

![[DOL-Tam-Trap-Pattern-Va-Bon-Feature-Phan-Biet.svg|697]]

*Hình 10 — Tám trap pattern và bốn feature phân biệt. Khối kết luận là luận điểm trung tâm của toàn bộ nghiên cứu: không feature phân biệt nào nhận diện được bằng mắt.*

---

# 16. Cognitive Errors

## 16.1 Vì sao DOL đặc biệt dễ bị hindsight bias

Protocol hỏi trực tiếp câu này. Có **năm** lý do cấu trúc, và chúng cộng dồn:

**Lý do 1 — Tính lưỡng trị của mọi kết cục.** Với DOL, mọi kết quả đều có thể được đọc là "đúng":
- Giá đi lên → "BSL là DOL" ✓
- Giá đi xuống → "SSL là DOL" ✓
- Giá lên rồi xuống → "sweep BSL rồi đảo" ✓
- Giá xuống rồi lên → "Judas quét SSL rồi distribution" ✓
- Giá đi ngang → "accumulation, chưa distribution" ✓

Năm kết cục, năm lời giải thích, **không có kết cục nào bị loại**. Một hệ thống không loại được kết cục nào thì không có nội dung dự báo.

**Lý do 2 — Pool ở khắp nơi.** Trên bất kỳ chart nào, luôn tồn tại một đỉnh và một đáy ở mọi phía. Nghĩa là **luôn có sẵn một pool để gọi là DOL** sau khi biết hướng đi. Không giống một indicator có ngưỡng, DOL không có "không có tín hiệu" — trừ khi bạn tự định nghĩa nó.

**Lý do 3 — Swing chỉ tồn tại sau khi xác nhận.** Một cực trị chỉ là swing sau N nến (hoặc sau khi DC threshold bị vượt). Trên chart đã hoàn thành, mọi swing đều hiển nhiên. Trong real-time, tại thời điểm quyết định, **bạn không biết** cực trị nào sẽ trở thành swing. Đây là look-ahead bias ở dạng cấu trúc — không thể sửa bằng cách "cẩn thận hơn".

**Lý do 4 — Dealing range có thể chọn sau.** Cùng một chart cho phép nhiều dealing range hợp lý. Chọn range sau khi biết kết quả cho phép gán nhãn external/internal theo ý muốn. Đây là **độ tự do tham số ẩn** lớn nhất của phương pháp.

**Lý do 5 — Không có cơ chế chấm điểm độc lập.** Với một indicator, bạn có thể tính lại và kiểm tra. Với DOL, nếu không có snapshot bất biến, **không ai** — kể cả chính bạn — biết được lúc đó bạn thực sự nghĩ gì.

## 16.2 Phân biệt hai câu — vấn đề phương pháp trung tâm

Protocol yêu cầu phân biệt rõ:

**"I found the DOL after price moved."**
- Đây là **mô tả hồi tố**. Nó có giá trị học tập (hiểu cấu trúc) nhưng **không có giá trị thống kê**.
- Nếu bạn thu thập 100 mẫu theo cách này, bạn có 100 mẫu mà **mỗi mẫu đều biết đáp án trước khi được gán nhãn**. Hit rate tính ra sẽ tiến về 100% một cách vô nghĩa.
- Đây là **survivorship bias** ở dạng thuần tuý: bạn chỉ nhớ những lần nó "hoạt động".

**"I identified the DOL before price moved."**
- Đây là **dự báo**. Có giá trị thống kê **chỉ khi** có timestamp, snapshot, và candidate set viết trước.
- Đòi hỏi: cutoff, candidate set gồm **cả hai phía**, đối thủ, horizon, invalidation — viết ra **trước**.
- Đây là điều kiện duy nhất để bất kỳ số liệu nào về DOL có ý nghĩa.

> [!danger] Phép thử duy nhất đủ mạnh
> **Bạn có thể chứng minh mình đã xác định DOL trước khi giá di chuyển không — bằng một artifact có timestamp, được tạo trước khi biết kết quả?**
> Nếu câu trả lời là không, dữ liệu đó **không dùng được** cho bất kỳ kết luận nào về edge. Không phải "yếu" — mà là **không dùng được**. Đây là tiêu chuẩn nhị phân, không phải thang điểm.

## 16.3 Mười cognitive bias — biểu hiện cụ thể trong DOL

| Bias | Biểu hiện cụ thể trong thực hành DOL | Cách giảm thiểu |
|---|---|---|
| **Hindsight** | Gọi tên DOL sau khi biết hướng; "tôi đã thấy nó rồi" | Snapshot bất biến tại cutoff (§16.4) |
| **Confirmation** | Chọn bias trước rồi chỉ mark pool phía đó | Bắt buộc mark cả hai phía + viết đối thủ |
| **Narrative** | Câu chuyện "smart money đang accumulation" thay thế cho dữ liệu | Phân loại mọi claim theo `[MARKET MECHANICS]` / `[INTERPRETATION]` |
| **Selection** | Chỉ lưu lại các setup thắng, bỏ qua no-signal | Journal ghi cả **no-signal và no-trade** |
| **Survivorship** | Học từ các ví dụ nổi tiếng (đã biết kết quả) | Chỉ dùng out-of-sample và forward test |
| **Look-ahead** | Dùng ZigZag/swing xác nhận sau; range chọn sau | N-bar pivot causal; timestamp level tại lúc **được biết** |
| **Overfitting** | Thử nhiều định nghĩa swing/ε/session tới khi ra kết quả đẹp | Báo cáo số trials; PBO/Deflated Sharpe |
| **Anchoring** | Neo vào mức đã mark đầu ngày dù cấu trúc đã đổi | Rule re-select rõ ràng; DOL là biến trạng thái |
| **Recency** | Dùng regime của tuần trước làm mặc định tuần này | Stratify theo regime trong mọi báo cáo |
| **Outcome** | Đánh giá quyết định bằng kết quả ("lệnh thắng nên phân tích đúng") | Grade **quy trình** tách khỏi grade **kết quả** |

## 16.4 Snapshot bất biến — cơ chế phòng vệ duy nhất hiệu quả

Đây là đề xuất vận hành quan trọng nhất của chương. Không có nó, mọi biện pháp khác đều vô hiệu.

**Tại cutoff, lưu một file bất biến (không được sửa, chỉ được append) chứa:**

```
1. Timestamp chính xác (timezone rõ)
2. Snapshot dữ liệu: giá, range endpoints + phương pháp chọn, ATR/ADR
3. Candidate set ĐẦY ĐỦ cả hai phía (kể cả cái sẽ bị loại), kèm lý do loại
4. Chosen DOL + score + confidence bucket
5. Competitor (đối thủ) + lý do nó yếu hơn
6. Invalidation: sự kiện quan sát được nào làm mệnh đề sai
7. Model dự kiến: reversal hay continuation
8. Điều kiện entry: POI, entry-side liquidity cần raid, confirmation cần thấy
9. Hành động dự kiến: trade / no-trade (và lý do nếu no-trade)
```

**Hai thuộc tính bắt buộc của snapshot:**
- **Bất biến:** sau khi ghi, không sửa. Nếu phải cập nhật, ghi **thêm** một entry mới với timestamp mới và lý do — không overwrite.
- **Có timestamp:** phải chứng minh được nó được tạo trước khi biết kết quả. Với file, điều này tự động đúng. Với ghi chú tay, ghi giờ cụ thể.

> [!important] Giá trị kép của snapshot
> Nó không chỉ chống hindsight bias. Nó là **nguồn dữ liệu duy nhất hợp lệ** cho backtest forward. Nếu bạn duy trì snapshot trong 6 tháng, bạn có một dataset mà **không ai** có thể nói là look-ahead — kể cả chính bạn. Đây là tài sản nghiên cứu lớn hơn bất kỳ kết quả backtest nào.

---

# 17. Objective vs Subjective

## 17.1 Định nghĩa bốn mức phân loại

| Mức | Định nghĩa | Tiêu chí kiểm tra |
|---|---|---|
| **[O] Objective** | Hai người, cùng dữ liệu, cùng bộ rule đã viết, cho **cùng kết quả** | Tái lập được bởi người khác không cần hỏi bạn |
| **[S] Semi-objective** | Khách quan **sau khi** chốt tham số; tham số là lựa chọn của con người | Tái lập được **nếu biết tham số**; phải ghi tham số |
| **[J] Subjective** | Phán đoán; hai người có thể khác nhau hợp lý | Không tái lập được; chỉ dùng được như context |
| **[U] Unknown from chart** | Không thể biết từ OHLC, ở bất kỳ mức độ chính xác nào | Không được dùng làm cơ sở duy nhất cho lệnh |

> [!important] Mục tiêu không phải biến mọi thứ thành [O]
> Mục tiêu là **giảm diễn giải tuỳ nghi mà không giả vờ rằng mọi khái niệm ICT đều có thể trở nên hoàn toàn khách quan**. Một số thứ căn bản là chủ quan; việc dán nhãn [J] cho chúng là **trung thực và hữu ích**, không phải thất bại. Cái nguy hiểm là **dán nhãn [O] cho một thứ thực chất là [J]** — vì lúc đó bạn tin vào nó như một sự thật.

## 17.2 Bảng phân loại DOL framework

| Thành phần | [O] | [S] | [J] | [U] | Ghi chú |
|---|---|---|---|---|---|
| **PDH / PDL / PWH / PWL** | ✅ | | | | Số học thuần tuý; phụ thuộc data convention (RTH/ETH) |
| **Session high/low** | ✅ | | | | Phụ thuộc định nghĩa session |
| **Round numbers** | | ✅ | | | Khách quan sau khi chốt bước giá |
| **Swing high/low (N-bar pivot)** | | ✅ | | | Khách quan sau khi chốt N |
| **Swing theo mắt thường** | | | ✅ | | Không tái lập — đây là vấn đề gốc |
| **Equal highs/lows** | | ✅ | | | Khách quan sau khi chốt ε |
| **"Imperfect" equal highs** | | | ✅ | | ε do người chọn; nhạy cực cao |
| **Structural vs inventory swing** | | ✅ | | | Khách quan sau khi chốt rule "cấu trúc có đổi không" |
| **Dealing range endpoints** | | ✅ | | | Phụ thuộc phương pháp; **phải ghi phương pháp** |
| **External / internal** | ✅ | | | | Khách quan **sau khi** range đóng băng |
| **Premium / discount** | ✅ | | | | Số học; nhưng phụ thuộc anchor |
| **BOS** | | ✅ | | | Khách quan sau khi chốt close-vs-wick và swing definition |
| **MSS** | | ✅ | | | Như trên, cộng định nghĩa "swing ngược leg" |
| **Displacement** | | ✅ | | | Khách quan sau khi chốt threshold (body/ATR...) |
| **FVG** | ✅ | | | | Ba nến, rule rõ ràng — nhưng phụ thuộc tick minimum |
| **POI** | | | ✅ | | Chọn array nào là "POI thật" thường là phán đoán |
| **Mitigation state** | | ✅ | | | Sau khi chốt định nghĩa mitigation |
| **Reachability** | | ✅ | | | Sau khi chốt λ và ADR/ATR |
| **"Structural significance"** | | | ✅ | | Câu hỏi "mức này có quan trọng không" |
| **Approach structure (compression/exhaustion)** | | | ✅ | | Rất hữu ích nhưng hiện chưa có định nghĩa chuẩn |
| **Regime classification** | | ✅ | | | Sau khi chốt rule; nhưng ex-ante khó |
| **Lượng lệnh tại một mức** | | | | ✅ | Không quan sát được từ OHLC |
| **Ý định của participant** | | | | ✅ | Không suy ra được từ giá |
| **Absorption / inventory transfer** | | | | ✅ | Không suy ra được từ nến |
| **Smart money vs retail** | | | | ✅ | Không có thông tin định danh |

## 17.3 Đọc bảng này thế nào

**Quan sát 1 — Phần lớn DOL framework là [S], không phải [O].** Điều này tốt hơn vẻ ngoài của nó: [S] có nghĩa là **có thể backtest**, miễn là **ghi tham số**. Vấn đề của ngành này không phải thiếu tính khách quan — mà là **không ai ghi tham số**.

**Quan sát 2 — Bốn ô [U] ở cuối bảng chính là bốn thứ mà narrative ICT hay tuyên bố nhất.** "Smart money đang accumulation", "institutions đang lấy stops" — tất cả đều [U]. Đây không phải trùng hợp: **những thứ không quan sát được chính là những thứ dễ kể chuyện nhất**, vì chúng không thể bị phủ định.

**Quan sát 3 — Có đúng hai ô [J] thực sự gây hại.** `Structural significance` và `Approach structure`. Cả hai đều quan trọng, cả hai đều chủ quan, và cả hai đều **có thể bán khách quan hoá** — structural significance bằng rule "cấu trúc có đổi không", approach structure bằng metric định lượng (ví dụ: tỷ lệ pullback depth / leg size, số HL liên tiếp). Đây là hai hạng mục **đáng đầu tư công sức nhất** để giảm tính tuỳ nghi.

**Quan sát 4 — Ưu tiên cải thiện.** Thứ tự giảm tính chủ quan theo giá trị:
1. **Swing definition** → N-bar pivot hoặc DC threshold (đã có giải pháp, xem [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]).
2. **Dealing range** → fixed lookback hoặc rule đóng băng.
3. **Approach structure** → metric định lượng.
4. **ε cho equal highs** → sensitivity analysis.
5. **POI selection** → hạ xuống thành "array nào chứa entry", không phải "array nào là POI thật".

---

# 18. Quantification

## 18.1 Ba nhóm feature

**Nhóm A — Liquidity features** (thuộc tính của pool)

| Feature | Cách tính | Kỳ vọng | Confounder |
|---|---|---|---|
| `dist_atr` | `\|price − level\| / ATR_n` | Gần → hit rate cao hơn (tầm thường) | ⚠️ Chính nó là confounder của mọi thứ khác |
| `age_bars` | Bars kể từ lúc pool **được biết** | Không rõ chiều (xem #9) | Tương quan với distance |
| `touch_count` | Số lần tiếp cận trong ε | Chữ U hoặc đơn điệu — chưa biết | Phụ thuộc ε, timeframe |
| `swing_mag` | Leg size tạo cực trị / ATR | Lớn → quan trọng hơn | Tương quan với structural significance |
| `equalness_n` | Số cực trị trong cụm | Nhiều → dày hơn | Phụ thuộc ε |
| `equalness_eps` | Độ tản của cụm / ATR | Nhỏ → "bằng nhau" hơn | Như trên |
| `displacement` | Body/ATR, TR/median_TR khi rời pool | Lớn → pool quan trọng | Là hệ quả, không phải nguyên nhân |
| `timeframe_src` | Timeframe tạo pool | HTF → quan trọng hơn | Tương quan với distance |
| `is_external` | Ngoài frozen range? | External → final objective | Phụ thuộc phương pháp chọn range |
| `swept_state` | 0 / partial / full | Unswept → còn giá trị | Định nghĩa partial mơ hồ |
| `mitigation` | Array tại pool đã mitigate? | Unmitigated → phản ứng mạnh | Định nghĩa mitigation |

**Nhóm B — Context features** (thuộc tính của bối cảnh)

| Feature | Cách tính | Kỳ vọng | Confounder |
|---|---|---|---|
| `htf_trend` | Dấu của structural state D1 | Trend mạnh → continuation | Phụ thuộc định nghĩa trend |
| `range_pos` | `(p − low)/(high − low)` | Tương tác với hướng DOL | Anchor range |
| `is_premium` | `range_pos > 0.5` | Entry permission | Như trên |
| `atr_pct` | ATR percentile trong lookback | Regime | Cửa sổ lookback |
| `realized_vol` | Std của returns | Regime | Như trên |
| `session` | Asia/London/NY | Delivery tập trung trong killzone | Định nghĩa session, DST |
| `minutes_to_close` | Phút tới session close | Ít thời gian → ít khả năng tới target | — |
| `regime` | trending/ranging/expansion | Stratifier | Ex-post dễ, ex-ante khó |
| `dist_opposing` | Khoảng cách tới đối thủ mạnh nhất | ⭐ Feature trung tâm | — |
| `asymmetry_ratio` | `dist_own / dist_opposing` | ⭐ Tỷ lệ này là "DOL-ness" | — |
| `news_flag` | Có release trong horizon? | Regime khác | Lịch release, timezone |

**Nhóm C — Structural features**

| Feature | Cách tính | Kỳ vọng | Confounder |
|---|---|---|---|
| `bos_recent` | Bars kể từ BOS cuối | Gần → delivery mạnh | Định nghĩa BOS |
| `mss_recent` | Bars kể từ MSS cuối | Gần → reversal mới | Định nghĩa MSS |
| `displacement_flag` | Displacement tại event? | Có → chất lượng cao hơn | Threshold |
| `swing_strength` | Số bars hai bên confirm (N) | Lớn → quan trọng hơn | Trễ nhiều hơn |
| `struct_protection` | Có swing bảo vệ giữa giá và target? | Có → đường khó đi | Định nghĩa "bảo vệ" |
| `hl_streak` | Số HL liên tiếp | Dài → trend mạnh | — |
| `pullback_depth` | Pullback / leg size | Nông → continuation | ⭐ Proxy cho "compression" |

## 18.2 Ba feature được đánh giá cao nhất — và lý do

Nếu chỉ test được ba feature:

**1. `asymmetry_ratio` = `dist_own / dist_opposing`** — đây là **biến gần nhất với chính định nghĩa DOL**. Nếu DOL có nội dung, nó phải nằm ở đây. Baseline tự nhiên: nearest-first rule cho tỷ lệ ≈ 1 luôn.

**2. `swept_state` / freshness** — đây là feature mà mô hình tuyên bố **khác** baseline. Nearest-first không quan tâm pool đã bị swept hay chưa; DOL thì có.

**3. `htf_relevance` / `timeframe_src`** — đây là feature thứ ba tuyên bố khác baseline.

Ba feature này là **tuyên bố cốt lõi của mô hình DOL**. Nếu chúng không mang information, phần còn lại của framework chỉ là cách diễn đạt lại của distance và salience.

## 18.3 Điều bắt buộc trong mọi báo cáo feature

> [!warning] Ba quy tắc không được vi phạm
> 1. **Mọi so sánh phải trong cùng distance bucket.** Nếu không, bạn đang đo distance và gọi nó là DOL.
> 2. **Mọi kết quả phải stratified theo regime và instrument.** Edge ở NQ trending không nói gì về EURUSD ranging.
> 3. **Mọi feature phải được timestamp tại lúc nó ĐƯỢC BIẾT**, không phải tại bar nó xảy ra. Swing biết sau N bars; MSS biết sau close; range biết sau khi endpoint confirm.

---

# 19. Backtesting

## 19.1 Câu hỏi đúng — và câu hỏi sai

**Câu hỏi SAI:** *"Giá có cuối cùng chạm liquidity không?"*
Vấn đề: câu trả lời gần như luôn là **có**, vì giá dao động và mọi mức đều có xác suất bị chạm tăng dần theo thời gian. Test này sẽ "thành công" một cách vô nghĩa. Đây là dạng test **không thể thất bại** — và do đó không có giá trị.

**Câu hỏi ĐÚNG:** *"DOL identification có cung cấp thông tin dự báo VƯỢT TRỘI so với các baseline chọn liquidity đơn giản không?"*
Đây là câu hỏi so sánh, có thể thất bại, và trả lời được bằng số.

## 19.2 Bài toán competing risks — khung đúng

Biến bài toán thành: **trong horizon H, upper target U hay lower target L được chạm trước?**

```
Label = +1   nếu U chạm trước
        −1   nếu L chạm trước
         0   nếu không cái nào chạm trước khi hết H
       tie   nếu cả hai trong cùng một bar (intrabar order không biết)
```

**Xử lý `tie` — quan trọng và hay bị làm sai:**
- Với bar data, `tie` phải được xử lý **conservative**: tính là "không xác định" và loại khỏi mẫu, HOẶC dùng lower timeframe để resolve, HOẶC gán cho phía **bất lợi** cho mô hình.
- **Không bao giờ** giả định target thuận lợi bị chạm trước. Đây là look-ahead bias ở dạng thô nhất.

![[DOL-Competing-Risks-U-vs-L-Cham-Truoc.svg|697]]

*Hình 12 — Bốn kết cục của bài toán competing risks, kèm `d_own` và `d_opp`. Panel phải nhấn mạnh hai metric quyết định: `asymmetry_ratio` và target-before-opposite-target.*

## 19.3 Baselines — năm baseline bắt buộc

Không có baseline thì không có kết quả. Baseline phải được chạy trên **cùng mẫu**, cùng horizon, cùng cách xử lý tie.

| # | Baseline | Định nghĩa | Nó kiểm soát cái gì |
|---|---|---|---|
| **B1** | Nearest liquidity | Chọn pool gần nhất mỗi phía | Kiểm soát distance confound |
| **B2** | Random candidate | Chọn ngẫu nhiên từ candidate set, cùng class balance | Kiểm soát base rate |
| **B3** | Nearest external | Chọn pool external gần nhất | Kiểm soát "external luôn thắng" |
| **B4** | Simple trend-based target | Ví dụ: luôn chọn PDH nếu open > prior close | Kiểm soát trend/momentum effect |
| **B5** | No-MSS / no-FVG variant | Cùng DOL model nhưng bỏ MSS hoặc FVG | Ablation — kiểm soát từng component |

> [!important] Baseline B1 là baseline quan trọng nhất
> Nếu mô hình DOL **không vượt được nearest liquidity**, toàn bộ phần "chọn DOL" không có giá trị — vì nearest-first là quy tắc mà một đứa trẻ cũng làm được. Đây là phép thử khắc nghiệt nhất và phải được báo cáo **đầu tiên**, không phải cuối cùng.

## 19.4 Metrics — tách ba nhóm

**Forecast metrics** (chất lượng dự báo — độc lập với giao dịch):
- First-touch accuracy
- Balanced accuracy (vì class balance có thể lệch)
- **Brier score / log loss** — quan trọng vì DOL là bài toán probability
- **Calibration by decile** — nhóm dự báo 60% có thật sự hit ~60%?
- Coverage (bao nhiêu % cutoff có DOL được chọn — nếu coverage thấp, mô hình chỉ giỏi ở việc nói "neutral")
- Average time-to-hit

**Trade metrics** (chất lượng giao dịch):
- Expectancy **sau costs**
- Win rate, average win/loss, profit factor
- Max drawdown
- **MAE / MFE** — critical vì một DOL đúng vẫn có thể có MAE lớn hơn stop
- Time in trade
- Tail loss distribution (không chỉ mean)

**Path metrics** (cấu trúc đường đi):
- P(opposing sweep trước DOL)
- P(DOL hit | có valid MSS)
- Front-run rate (giá đảo trước target trong ε)
- Overshoot distribution (vượt target bao xa)
- **P(U trước L) vs P(L trước U)** — chính là câu hỏi trung tâm

## 19.5 Sáu metric mà protocol yêu cầu — và một cảnh báo

Protocol liệt kê: hit rate, target achievement rate, MAE, MFE, time-to-target, expectancy, R multiple, false-target rate, **target-before-opposite-target**, drawdown, regime dependency.

**Hai metric quan trọng nhất và ít được dùng nhất:**

1. **Target-before-opposite-target** — đây là metric **duy nhất** trả lời trực tiếp câu hỏi "X thay vì Y". Hit rate thuần tuý không trả lời được, vì một target có thể có hit rate 70% nhưng target đối diện có hit rate 75%. **Chỉ metric này mới đo được DOL như một mệnh đề so sánh.**

2. **False-target rate** — tỷ lệ target được chạm nhưng **sau khi** đã chạm invalidation. Đây là metric phát hiện narrative tự chữa mình: nếu bạn vẫn tính là "thắng" khi invalidation đã bị chạm trước đó, mô hình của bạn đang tự bảo hiểm.

**Cảnh báo về hit rate:** hit rate **không có ý nghĩa** nếu không kèm distance bucket. Một mô hình chọn target gần sẽ luôn có hit rate cao hơn mô hình chọn target xa — và điều đó không nói gì về chất lượng mô hình.

## 19.6 Bảy loại look-ahead bias và cách phòng

Protocol yêu cầu liệt kê các cách backtest DOL vô tình dùng thông tin tương lai. Đây là danh sách đầy đủ, kèm cách chặn:

![[DOL-Look-Ahead-Bias-Bay-Duong-Dan.svg|697]]

*Hình 13 — Bảy đường dẫn look-ahead và cách chặn từng loại. Khối cơ chế minh hoạ số học của L7: cùng một mẫu, hit rate đi từ ~20% lên ~100% chỉ bằng việc "dọn dữ liệu" — không có gì về thị trường thay đổi.*

| # | Dạng look-ahead | Biểu hiện | Cách chặn |
|---|---|---|---|
| **L1** | **Swing chỉ rõ sau xác nhận** | Chọn swing bằng mắt trên chart đã hoàn thành | N-bar pivot causal; **timestamp level tại lúc biết**, không tại bar swing |
| **L2** | **Dùng cấu trúc tương lai để phân loại cấu trúc hiện tại** | Gọi một break là "BOS" vì sau đó giá tiếp tục | Chỉ dùng dữ liệu ≤ t để phân loại; rule phải viết trước |
| **L3** | **Biết liquidity nào cuối cùng bị lấy** | Vô thức ưu tiên pool "trông sẽ bị lấy" | Candidate set phải được **lưu snapshot** tại t; không được sửa |
| **L4** | **Định nghĩa dealing range hồi tố** | Chọn range để nhãn external/internal khớp ý muốn | Rule đóng băng range viết trước; sensitivity analysis trên phương pháp |
| **L5** | **Chọn "liquidity quan trọng" dựa trên phản ứng cuối cùng** | Gọi một level là "quan trọng" vì giá đã phản ứng ở đó | Salience phải định nghĩa bằng thuộc tính **tại t**, không bằng phản ứng sau |
| **L6** | **Dùng displacement/MSS/POI validity tương lai** | Xác nhận MSS bằng FVG hình thành sau; xác nhận POI bằng phản ứng của nó | Chỉ dùng event đã close; phân biệt "signal" và "confirmation" trong timestamp |
| **L7** | **Loại candidate fail sau khi thấy kết quả** | Bỏ khỏi mẫu những candidate "rõ ràng là sai" | **Mọi candidate phải được giữ**, kể cả cái bị loại — kèm lý do loại tại t |

> [!danger] L7 là dạng nguy hiểm nhất vì nó vô hình
> Loại bỏ candidate sau khi biết kết quả **không cảm thấy** như gian lận. Nó cảm thấy như "dọn dữ liệu". Nhưng nó biến một mẫu có 5 candidate thành một mẫu chỉ có candidate đúng — và hit rate tăng vọt một cách giả tạo.
>
> **Quy tắc:** mọi candidate được mark tại cutoff phải ở lại trong dataset, kèm cờ `selected: true/false` và lý do. Số candidate bị loại là một **metric chất lượng mô hình**, không phải rác.

## 19.7 Quy trình event study

```
1. Chốt cutoff, horizon, và tất cả tham số TRƯỚC khi xem dữ liệu
2. Tại mỗi cutoff: xây candidate set CHỈ bằng data ≤ t
3. Lưu snapshot bất biến: levels, scores, chosen DOL, competitor, invalidation
4. Theo dõi: target nào hit trước (xử lý tie conservative)
5. Ghi path events: opposing sweep, MSS, displacement, FVG, entry fill
6. Ghi cả NO-SIGNAL và NO-TRADE — không chỉ trade đã vào
7. Tách target study khỏi execution study
```

> [!important] Unit of analysis là session-day, không phải bar
> Nếu mỗi bar là một observation, một ngày sẽ tạo ra hàng chục observation **tương quan cao với nhau** (cùng một ngày, cùng một cấu trúc). Điều này làm sai mọi confidence interval. Dùng **session-day** làm đơn vị, hoặc dùng block bootstrap theo ngày/tuần.

## 19.8 Train / validation / OOS

```
Development period   → định nghĩa features, giới hạn model family
Validation period    → chọn RẤT ÍT hyperparameters
Locked OOS period    → chạy MỘT LẦN
Forward paper-trade  → xác minh data pipeline và fill assumptions
Live micro-size      → kiểm tra slippage và hành vi thực thi
```

**Chia theo thời gian (chronological), không shuffle.** Với dữ liệu tài chính, random shuffle tạo ra look-ahead bias vì thông tin từ tương lai rò vào training set.

## 19.9 Execution assumptions

Đây là nơi phần lớn backtest ICT thất bại. Các giả định bắt buộc:

- **Entry limit chỉ tính fill khi market thực sự giao dịch qua giá.** Với bar data mơ hồ, dùng conservative fill (giả định fill xấu hơn).
- **Stop và target cùng trong một bar** → resolve bằng lower timeframe hoặc **worst-case** (giả định stop chạm trước).
- **Cộng commission, spread, slippage** theo session và volatility bucket — không dùng một con số trung bình.
- **Stop slippage phải stress test:** stop trigger **không bảo đảm** execution price, đặc biệt trong fast market. Đây là lý do nhiều backtest ICT đẹp trên giấy nhưng thua thực tế.
- **Không dùng final continuous-contract price** nếu đó không phải giá execute được. Contract roll tạo artifact trong equal highs và FVG.
- **CFD/spot feed khác nhau về high/low** — DOL dựa trên vài tick phải test trên execution feed thực tế.

## 19.10 Ablation study

Bắt đầu từ đơn giản nhất, thêm từng component:

| Bước | Model | Câu hỏi nó trả lời |
|---|---|---|
| 0 | Nearest liquidity baseline | Chuẩn so sánh |
| 1 | + D1 DOL selection (asymmetry) | DOL selection có thêm gì không? |
| 2 | + H1 context (path, POI) | Path analysis có thêm gì không? |
| 3 | + Opposing sweep requirement | Sweep có thêm gì không? |
| 4 | + MSS | MSS có thêm gì không? |
| 5 | + Displacement filter | Displacement có thêm gì không? |
| 6 | + FVG entry | FVG entry có thêm gì không? |
| 7 | + Session / news filters | Filter có thêm gì không? |

> [!tip] Câu trả lời quan trọng nhất từ ablation
> Nếu FVG **không** cải thiện expectancy sau khi đã có displacement, thì FVG chỉ là một cách **parameterize retracement** — không phải nguồn edge riêng. Điều này không làm FVG vô dụng (nó vẫn là cách entry có kỷ luật), nhưng nó thay đổi cách bạn **đếm evidence**: FVG không phải xác nhận độc lập thứ ba.

---

# 20. Falsification

## 20.1 Thiết kế theo falsification

Protocol yêu cầu chủ động tìm cách **bác bỏ** DOL, không chỉ xác nhận nó.

> [!important] H0 là mặc định
> **H0:** DOL identification **không** cung cấp lợi thế dự báo nào vượt baseline.
> **H1:** DOL identification cung cấp lợi thế dự báo đo lường được.
>
> **Nghĩa vụ chứng minh thuộc về H1.** Không tìm thấy bằng chứng bác bỏ H0 **không** phải bằng chứng ủng hộ H1 — nó chỉ có nghĩa là bạn chưa test đủ mạnh.

## 20.2 Chuỗi giả thuyết cụ thể

Không test "ICT có đúng không" như một khối. Tách thành các mệnh đề bác bỏ được:

| # | Giả thuyết | Phép thử bác bỏ | Nếu bị bác bỏ |
|---|---|---|---|
| H1 | Candidate score cao nhất có P(first-touch) > nearest-level baseline | So sánh trong cùng distance bucket | Chọn DOL không có giá trị gia tăng |
| H2 | D1-aligned DOL hit rate > D1-opposed, cùng distance | Stratify theo alignment | Alignment không mang information |
| H3 | Opposing sweep + reclaim cải thiện P(DOL hit) | So có/không sweep | Sweep chỉ là noise |
| H4 | MSS có displacement > MSS không displacement | So hai nhóm | Displacement filter vô ích |
| H5 | FVG retracement entry cải thiện expectancy vs market entry tại MSS close | So hai entry rule | FVG chỉ là cách vào muộn hơn |
| H6 | News regime làm đổi dấu (hoặc giảm) edge | Stratify theo news flag | News filter thừa |
| H7 | External targets có reward lớn hơn nhưng time-to-hit dài hơn | So internal vs external | Phân tầng target vô nghĩa |
| **H8** | ⭐ **`asymmetry_ratio` mang information về hướng** | Logistic/competing-risks với distance là covariate | **Toàn bộ khái niệm DOL-as-comparison sụp đổ** |
| **H9** | ⭐ **Freshness (unswept) mang information** | So swept vs unswept, cùng distance | Rule "swept = spent" là sai |

**H8 và H9 là hai giả thuyết quan trọng nhất.** Chúng là hai tuyên bố duy nhất mà mô hình DOL đưa ra **khác** baseline nearest-first. Nếu cả hai bị bác bỏ, phần còn lại của framework chỉ là **cách diễn đạt lại** của distance và salience — hữu ích như ngôn ngữ mô tả, vô dụng như công cụ dự báo.

## 20.3 Statistical pitfalls

Đây là phần protocol yêu cầu phân tích, và là nơi các backtest ICT thất bại về mặt thống kê.

**1. Multiple testing / data snooping.** Bạn sẽ thử nhiều định nghĩa swing, nhiều ε, nhiều session window, nhiều displacement threshold. Với đủ nhiều lần thử, **một cái gì đó sẽ trông có ý nghĩa** ngay cả trên dữ liệu ngẫu nhiên.
→ *Chặn:* báo cáo **số trials**. Dùng Deflated Sharpe hoặc PBO (Probability of Backtest Overfitting) — nghiên cứu PBO cho thấy configuration tốt nhất in-sample có thể rơi **xuống dưới median** out-of-sample.

**2. P-hacking.** Chọn horizon, metric, hoặc subsample sau khi thấy kết quả.
→ *Chặn:* mọi tham số chốt trước, ghi lại, không đổi.

**3. Selection bias.** Chỉ nghiên cứu các ngày có setup rõ ràng.
→ *Chặn:* bao gồm no-trade và neutral trong mẫu; báo cáo coverage.

**4. Non-stationarity.** Edge có thể tồn tại trong một giai đoạn regime và mất đi.
→ *Chặn:* walk-forward, regime stratify, báo cáo theo năm.

**5. Regime dependence.** Edge chỉ tồn tại trong trending.
→ *Chặn:* stratify bắt buộc; không gộp regime.

**6. Autocorrelation.** Trades trong cùng ngày tương quan cao.
→ *Chặn:* block bootstrap theo ngày/tuần, không bootstrap từng trade.

**7. Overfitting.** Nhiều tham số, ít dữ liệu.
→ *Chặn:* giới hạn model family; báo cáo parameter stability; kiểm tra sensitivity quanh giá trị đã chọn.

**8. Base rate neglect.** Đây là pitfall **đặc thù nhất** của DOL.
→ *Chặn:* luôn so với base rate; luôn stratify theo distance.

## 20.4 Sample size — hướng dẫn thực dụng

- Unit of analysis là **session-day**. Một năm giao dịch ≈ 250 session-days.
- Với mẫu nhỏ (dưới ~100 observations), **không** nên tách nhiều regime/stratum. Ưu tiên test **một** giả thuyết chính (H8 hoặc H9) trên toàn mẫu.
- Confidence interval cho hit rate: với n=100 và hit rate 55%, CI 95% xấp xỉ ±10 điểm phần trăm. Nghĩa là **bạn không thể phân biệt 55% với 50%** ở cỡ mẫu đó. Đây là lý do phần lớn backtest ICT cá nhân không kết luận được gì.
- Với expectancy: phương sai của R-multiple thường lớn (nhiều lệnh −1R, ít lệnh +3R). Cần cỡ mẫu **lớn hơn nhiều** so với test hit rate.

## 20.5 Cross-asset validation

Test trên ít nhất 3 instrument thuộc 2 lớp khác nhau, ví dụ: NQ1 (index futures), EURUSD + GBPUSD (FX), XAUUSD (commodity).

**Điều này bác bỏ được gì:** nếu edge chỉ tồn tại ở NQ, đó có thể là artifact của:
- Data convention (RTH/ETH, contract roll).
- Volatility regime đặc thù.
- Overfitting vào một instrument.

**Điều này KHÔNG bác bỏ được gì:** một edge thật có thể **thực sự** khác nhau giữa các instrument vì cấu trúc vi mô khác nhau (futures tập trung vs FX OTC). Vì vậy cross-asset validation không thành công **không** tự động bác bỏ giả thuyết — nó chỉ loại bỏ tuyên bố phổ quát.

## 20.6 Điều kiện để kết luận "DOL không có edge"

Để kết luận trung thực rằng DOL không có edge, cần **tất cả** những điều sau:

1. H8 bị bác bỏ: `asymmetry_ratio` không mang information sau khi kiểm soát distance.
2. H9 bị bác bỏ: freshness không mang information.
3. Mô hình đầy đủ (ablation bước 7) **không** vượt baseline B1 (nearest liquidity) sau costs.
4. Kết quả ổn định qua walk-forward và qua ít nhất 3 instrument.
5. Số trials được báo cáo và PBO chấp nhận được.
6. Kết quả không đảo khi sensitivity analysis trên ε, N, λ, session window.

Nếu **bất kỳ** điều nào ở trên không đạt, kết luận trung thực là: **"chưa xác định"** — không phải "có edge", và cũng không phải "không có edge".

> [!important] "Chưa xác định" là kết quả hợp lệ và phổ biến nhất
> Phần lớn nghiên cứu độc lập về phương pháp discretionary sẽ kết thúc ở "chưa xác định" vì cỡ mẫu không đủ. Điều này **không** có nghĩa là phương pháp vô dụng — nó có nghĩa là **bạn không biết**. Sự khác biệt giữa "tôi không biết" và "tôi tin" là toàn bộ giá trị của nghiên cứu này.

---

# 21. Decision Framework

## 21.1 Decision tree 13 bước

```
STEP 1 — Where is price?
    ├─ Xác định: giá hiện tại, so với open, so với prior day
    └─ Nếu không xác định được session/timezone → DỪNG

STEP 2 — What is current HTF structure?
    ├─ HH/HL, LH/LL, hay undefined (overlapping bars)?
    └─ Nếu undefined → DỪNG (neutral)

STEP 3 — What is the active dealing range?
    ├─ Chốt 2 con số + phương pháp; ĐÓNG BĂNG
    └─ Nếu không chốt được → DỪNG

STEP 4 — What liquidity exists?
    ├─ Mark rộng rãi, CẢ HAI PHÍA, có giá
    └─ Nếu chỉ mark được một phía → mark lại

STEP 5 — Which liquidity is structurally significant?
    ├─ Áp hard filters F1–F7
    └─ Nếu candidate set rỗng → DỪNG (neutral)

STEP 6 — What are the candidate DOLs?
    ├─ Candidate = Alignment ∧ Reachability ∧ Freshness
    └─ Có ≥1 mỗi phía

STEP 7 — What evidence supports each candidate?
    └─ Viết ra, không cảm nhận

STEP 8 — What evidence contradicts each candidate?
    └─ BẮT BUỘC — nếu bỏ bước này, bước 9 vô nghĩa

STEP 9 — Which candidate has the strongest pre-move evidence?
    ├─ Tính asymmetry
    └─ Nếu |asymmetry| < threshold → DỪNG (neutral)

STEP 10 — What is the intermediate objective?
    └─ Candidate gần nhất hợp lệ, CÙNG HƯỚNG → T1

STEP 11 — What is the final objective?
    └─ Candidate xa nhất hợp lệ, CÙNG HƯỚNG → T2

STEP 12 — What invalidates the thesis?
    └─ Viết TRƯỚC khi vào lệnh, dạng sự kiện quan sát được

STEP 13 — How should H1/M5 execution respond?
    ├─ Chọn model: reversal hay continuation
    ├─ Chờ điều kiện: raid / POI hold
    ├─ Chờ xác nhận: MSS (pre-confirmed pivot) + displacement
    ├─ Entry: FVG retracement, first touch
    └─ Kiểm R:R sau costs tới T1; nếu không đạt → DỪNG
```

![[DOL-Decision-Framework-13-Buoc.svg|697]]

*Hình 11 — Decision framework dạng bảng. Năm điểm dừng nằm ở bước 2, 3, 5, 9 và 13; bốn output hợp lệ nằm ở khối giữa — trong đó Neutral có mục tiêu tham khảo ≥25–30% số ngày.*

## 21.2 Bốn output hợp lệ — không chỉ hai

| Output | Khi nào | Tần suất tham khảo |
|---|---|---|
| **Long plan** | Asymmetry nghiêng upper rõ rệt | — |
| **Short plan** | Asymmetry nghiêng lower rõ rệt | — |
| **Neutral — no-trade** | Asymmetry không đủ; hoặc structure undefined; hoặc range không chốt được | **≥25–30% số ngày** |
| **Wait — re-assess** | Có candidate nhưng chưa đến điều kiện entry (chưa raid, chưa tới POI) | Phần lớn thời gian trong ngày |

> [!danger] Nếu mô hình của bạn chưa bao giờ trả về Neutral
> Đó là dấu hiệu chắc chắn nhất rằng bạn đang **kể chuyện**, không phải **phân tích**. Một mô hình không bao giờ nói "không" thì không có nội dung — nó chỉ là một ngôn ngữ để diễn đạt điều bạn đã muốn làm.

## 21.3 Ba câu hỏi kiểm tra trước khi bấm nút

1. **Tôi có viết được candidate đối thủ không?** Nếu không → chưa có DOL, chỉ có thiên kiến.
2. **Tôi có viết được invalidation dạng sự kiện quan sát được không?** Nếu không → đây là niềm tin, không phải kế hoạch.
3. **Nếu DOL này hit, tôi có biết mình sẽ chốt ở đâu không?** Nếu không → entry chưa có target, chỉ có hy vọng.

Một câu "Không" → không vào lệnh.

---

# 22. Final Mental Model

## 22.1 Mười lăm câu trả lời

**1. What is DOL?**
DOL là một **mệnh đề xác suất có điều kiện** về việc candidate nào sẽ bị chạm trước, phát biểu tại một cutoff xác định, trong một horizon xác định, đối chiếu ít nhất hai phía. Nó được **biểu diễn** bằng một mức giá để vận hành được, nhưng bản chất nó không phải là mức giá đó.

**2. What is DOL NOT?**
Không phải entry trigger. Không phải mọi pool. Không phải một mức giá cố định cả ngày. Không phải đảm bảo. Không phải bằng chứng về ý định. Không phải một narrative giải thích được mọi kết cục.

**3. How is DOL different from liquidity?**
Liquidity (pool) là **dữ liệu**: một mức giá nơi lệnh có thể tập trung. DOL là **kết luận**: sau khi lọc qua bối cảnh cấu trúc và so sánh hai phía, phía nào có ưu thế. Pool là câu hỏi "ở đâu". DOL là câu trả lời "phía nào, và vì sao X thay vì Y".

**4. Can DOL be identified prospectively?**
**Về mặt cấu trúc, có** — với điều kiện có ba thứ: cutoff cố định, candidate set đầy đủ cả hai phía lưu trước, và invalidation viết trước. **Về mặt thống kê, chưa biết** — điều đó là câu hỏi empirical chưa được trả lời. Cái **chắc chắn** là: nếu không có ba thứ đó, DOL chỉ có thể xác định được một cách hồi tố, và mọi con số tính ra đều vô nghĩa.

**5. What evidence makes liquidity pool X more plausible than Y?**
Theo thứ tự sức mạnh:
1. **Alignment với structural state đã confirm** — X cùng phía với delivery hiện tại, Y ngược lại.
2. **Freshness** — X chưa bị tiêu thụ, Y đã swept.
3. **Asymmetry tương đối** — khoảng cách và chất lượng của X so với đối thủ phía kia.
4. **HTF relevance** — X là mức của tầng cao hơn.
5. **Path cleanliness** — không có opposing POI chất lượng trên đường tới X.
6. **Approach structure** — compression ủng hộ continuation; exhaustion ủng hộ reversal.

**6. What changes DOL?**
Ba loại sự kiện: (a) target bị tiêu thụ; (b) structural event ngược hướng đã confirm (close-based); (c) external shift làm dealing range cũ hết hiệu lực. Trong cả ba trường hợp, phải **xây lại candidate set**, không được diễn giải lại candidate cũ.

**7. What invalidates DOL?**
**Một sự kiện quan sát được, viết trước, ở dạng close** — ví dụ: "D1 close dưới HL gần nhất", "H1 close trở lại trên swept high", "M5/H1 acceptance trên mức invalidation". Invalidation không phải là "giá đi ngược một chút" — move ngược trong pha manipulation **không** phải invalidation. Đó là lý do invalidation phải được viết **trước** khi vào lệnh, dạng điều kiện, không dạng cảm nhận.

**8. How does DOL interact with HTF structure?**
HTF structure có **quyền phủ quyết**, không có **quyền thay thế**. Khi D1 và H1 xung đột: D1 quyết định hướng và size; H1 quyết định intermediate objective và entry. Nhưng phần lớn "xung đột" thực ra là **path split** — lower DOL là waypoint trên đường tới upper DOL, không phải mâu thuẫn.

**9. How does DOL influence Daily Bias?**
DOL **nuôi** bias như một input, không **đồng nhất** với bias. Model coherent nhất: *structure + liquidity + dealing range → directional hypothesis → candidate selection*, với stopping rule chỉ cho phép lặp một lần. DOL suy ra bias rồi bias xác nhận DOL là circular reasoning.

**10. How does DOL influence target selection?**
Đây là vai trò **chính** của DOL. DOL xác định **final objective** (T2) và, qua phân tầng, **intermediate objective** (T1). Nó không xác định entry — entry đến từ POI + confirmation. Và nó phải qua bộ lọc R:R sau costs: DOL đúng nhưng quá gần vẫn là no-trade.

**11. What part of DOL is objective?**
PDH/PDL/PWH/PWL, session extremes, FVG boundaries, external/internal **sau khi** range đóng băng, premium/discount **sau khi** chốt anchor, reachability **sau khi** chốt λ. Phần lớn framework là **[S] semi-objective** — khách quan sau khi ghi tham số. Đây là tin tốt: nó **có thể backtest được**.

**12. What part is subjective?**
Hai thứ chính: **structural significance** ("mức này có quan trọng không") và **approach structure** (compression hay exhaustion). Cộng thêm: chọn dealing range, ε cho equal highs, và chọn POI. Đây là những chỗ **đáng đầu tư công sức nhất** để bán khách quan hoá.

**13. What can price data actually prove?**
Price data chứng minh được: **cái gì đã xảy ra, theo thứ tự nào, với cấu trúc nào, trong bao lâu**. Nó chứng minh được các quan hệ thống kê trên mẫu đủ lớn (với đủ kỷ luật thống kê). Nó **không** chứng minh được: lượng lệnh, loại lệnh, ai giao dịch, absorption, inventory transfer, hay ý định.

**14. What remains hypothesis?**
(a) DOL identification có predictive advantage (H1). (b) `asymmetry_ratio` mang information về hướng (H8). (c) Freshness mang information (H9). (d) Scoring model có predictive power. (e) Nhóm lệnh quanh level **có đủ lớn** để tạo edge có thể khai thác sau costs. (f) Các quy tắc phân tầng target (T1/T2) cải thiện risk-adjusted return.

**15. How would we test it?**
Competing-risks event study trên unit **session-day**, với: candidate set lưu snapshot tại cutoff; năm baseline (đặc biệt nearest-liquidity); **mọi so sánh trong cùng distance bucket**; stratified theo regime, session, instrument; walk-forward và locked OOS; báo cáo số trials và PBO; và metric trung tâm là **target-before-opposite-target**, không phải hit rate.

## 22.2 Mental model cô đọng

> [!summary] Nếu chỉ nhớ một đoạn
> **Giá không bị kéo đi đâu cả.** Có một **phân phối kết quả không đối xứng**, phát sinh từ việc một số mức giá dễ thấy có thể tập trung lệnh có điều kiện, và từ việc độ sâu thị trường thay đổi khi giá tiếp cận chúng.
>
> **DOL là tên của sự bất đối xứng đó**, được phát biểu trước khi biết kết quả, dưới dạng so sánh giữa hai phía.
>
> Việc bạn **gọi tên** một pool là DOL không làm giá đi tới đó. Việc bạn **so sánh đúng** hai phía có thể cải thiện quyết định — nhưng điều đó **chưa được chứng minh**, và nghĩa vụ chứng minh thuộc về bạn.
>
> **Ba thứ biến DOL từ huyền thoại thành công cụ:**
> 1. **Viết ra trước** — cutoff, candidate cả hai phía, đối thủ, horizon, invalidation.
> 2. **So sánh, đừng khẳng định** — không có đối thủ thì không có DOL.
> 3. **Đo lại** — trong cùng distance bucket, có baseline, có OOS.
>
> **Và một thứ biến nó trở lại thành huyền thoại:** diễn giải lại mệnh đề sau khi biết kết quả.

---

# 23. Research Gaps

## 23.1 Bảng tổng hợp

| Category | What we know | Confidence | Evidence |
|---|---|---|---|
| **Established market mechanics** | Price change ngắn hạn gắn với order-flow imbalance; price impact lớn hơn khi depth mỏng | **Cao** | Cont, Kukanov & Stoikov — [order book events](https://arxiv.org/abs/1011.6402) |
| **Established market mechanics** | Stop-loss orders cụm quanh round numbers; clustering pattern của stop-loss khác take-profit rõ rệt, và khác giữa stop-buy và stop-sell | **Cao** | Osler — [NY Fed SR125](https://www.newyorkfed.org/research/staff_reports/sr125.html) / *Journal of Finance* 58(5) |
| **Established market mechanics** | Stop-loss orders đóng góp vào các move nhanh, tự củng cố (cascades) | **Trung bình–cao** | Osler — [NY Fed SR150](https://www.newyorkfed.org/research/staff_reports/sr150.html) |
| **Established market mechanics** | Nhóm lệnh quanh round number giải thích được **cả hai** dự đoán TA: đảo tại level, và tăng tốc khi xuyên level | **Trung bình–cao** | Osler SR125 (abstract xác nhận trực tiếp) |
| **Established market mechanics** | Chase lệnh stop trong fast market có rủi ro execution khác trigger price | **Cao** | FINRA Notice 16-19; SEC Trading Basics |
| **Established market mechanics** | Stop orders **không** hiển thị như resting liquidity trước khi trigger; chúng trở thành market order | **Cao** | CME order types; SEC |
| **Established market mechanics** | FX spot là OTC phân tán; không có central order book quan sát được cho retail | **Cao** | BIS Triennial Survey |
| **Established market mechanics** | News làm depth giảm, spread tăng, volatility tăng | **Trung bình–cao** | NY Fed SR590 và các nghiên cứu announcement |
| **ICT framework** | DOL là destination, tồn tại ở hai họ: stops/liquidity và imbalance | **Cao (là ICT)** | Mentorship 2022 Ep. 2, Ep. 3, Ep. 22 |
| **ICT framework** | Trong chuỗi thực thi, DOL đứng **sau** MS/Sweep/Displacement; PD array là entry | **Cao (là ICT)** | Mentorship 2022 |
| **ICT framework** | External/internal chỉ có nghĩa sau khi dealing range được xác định | **Cao (là ICT)** | Ep. 3 (Internal Range Liquidity) |
| **Interpretation** | Cơ chế **focal point** (nhiều participant độc lập đặt cùng loại lệnh vì cùng lý do) giải thích clustering **mà không cần** giả định ý định | **Trung bình** | Suy luận từ Osler + tính dễ thấy của level |
| **Interpretation** | Phần lớn move chạm pool là noise, không phải cascade | **Trung bình** | Osler ghi nhận round-crossings ~5/ngày nhưng cascade thật ~1/tuần |
| **Interpretation** | "Stops là liquidity" là shorthand sai kỹ thuật — stops tiêu thụ liquidity, không cung cấp | **Cao** | Định nghĩa stop order (CME/SEC) |
| **Interpretation** | Model C (structure + liquidity + range → hypothesis → DOL) coherent hơn Model A/B về logic | **Trung bình** | Lập luận logic, không phải dữ liệu |
| **Interpretation** | Approach structure (compression vs exhaustion) là feature phân biệt mạnh | **Thấp–trung bình** | Rút ra từ counterexample; chưa định lượng |
| **Hypothesis** | DOL identification có predictive advantage vượt nearest-liquidity baseline | **Chưa biết** | Chưa test |
| **Hypothesis** | `asymmetry_ratio` mang information về hướng sau khi kiểm soát distance | **Chưa biết** | Chưa test — ⭐ ưu tiên cao nhất |
| **Hypothesis** | Freshness (unswept) mang information | **Chưa biết** | Chưa test — ⭐ ưu tiên cao thứ hai |
| **Hypothesis** | HTF relevance mang information vượt distance | **Chưa biết** | Chưa test |
| **Hypothesis** | Opposing sweep + reclaim cải thiện P(DOL hit) | **Chưa biết** | Chưa test |
| **Hypothesis** | Displacement filter cải thiện chất lượng MSS signal | **Chưa biết** | Chưa test |
| **Hypothesis** | FVG entry cải thiện expectancy vượt market entry tại MSS close | **Chưa biết** | Chưa test |
| **Hypothesis** | Scoring model có predictive power | **Chưa biết** | Chưa test — mặc định H0 |
| **Hypothesis** | Equalness (ε) mang information | **Chưa biết** | Chưa test; nhạy tham số cao |
| **Unknown** | Lượng lệnh thật tại một mức cụ thể | **Không biết** | Không quan sát được từ OHLC (trừ khi có L2 futures) |
| **Unknown** | Ý định của participant | **Không biết** | **Không thể suy ra từ price data** — nguyên tắc |
| **Unknown** | Absorption / inventory transfer đã xảy ra hay chưa | **Không biết** | Cần order flow data (futures) |
| **Unknown** | Cascade xảy ra do liquidity event hay do informed flow | **Không biết** | Cần phân tách order flow |
| **Requires backtest** | Toàn bộ identification framework §7 | — | Event study competing-risks |
| **Requires backtest** | Cả bốn case ở §9 (đặc biệt Case B và C, nơi trực giác hay sai) | — | Stratified theo `range_pos` × alignment |
| **Requires backtest** | Hai template reversal vs continuation ở §12.4 | — | So expectancy hai template theo regime |
| **Requires backtest** | Ngưỡng asymmetry và threshold của score | — | Calibration trên validation set |
| **Requires backtest** | Reachability λ cho từng instrument | — | Grid có giới hạn trước, báo cáo stability |
| **Requires further research** | Định nghĩa định lượng cho "approach structure" | — | Feature engineering + validity check |
| **Requires further research** | Ngưỡng "structural significance" bán khách quan hoá | — | Thử rule "cấu trúc có đổi không" dạng binary |

## 23.2 Sáu kết luận về trạng thái hiểu biết

**1. Điều chúng ta biết tương đối chắc chắn.**
Cơ chế vi mô đằng sau việc "level có thể hoạt động": stop orders cụm ở một số mức, và stop-loss/take-profit hành xử **ngược nhau** — điều này giải thích tại sao **cùng một mức** vừa có thể đảo chiều vừa có thể tăng tốc. Đây là nền tảng vững nhất và nó **không** cần giả định về ý định.

**2. Điều thuộc ICT framework.**
DOL là destination; tồn tại hai họ destination (stops và imbalance); DOL nằm ở cuối chuỗi thực thi chứ không phải điều kiện vào lệnh; external/internal cần dealing range. Đây là **định nghĩa và quy ước**, không phải phát hiện về thị trường — nhưng chúng hữu ích và nhất quán.

**3. Điều chỉ là interpretation.**
Cơ chế focal point; việc phần lớn lần chạm pool là noise; Model C coherent hơn; approach structure là feature mạnh. Đây là những suy luận **hợp lý nhưng chưa được test**.

**4. Điều chưa thể xác nhận.**
Lượng lệnh tại một mức; ý định của participant; absorption; inventory transfer. Bốn thứ này **không thể** suy ra từ OHLC — đây là giới hạn cấu trúc, không phải giới hạn công cụ.

**5. Điều cần empirical testing.**
H1, H8, H9 và toàn bộ identification framework. Ưu tiên: **H8 (asymmetry) và H9 (freshness)** — vì đây là hai tuyên bố duy nhất mà mô hình DOL đưa ra **khác** baseline.

**6. Điều cần nghiên cứu thêm.**
Định nghĩa định lượng cho "approach structure" (compression vs exhaustion) — đây là feature được đánh giá cao nhất trong counterexample nhưng **chưa có định nghĩa chuẩn**. Và bán khách quan hoá "structural significance" thành rule binary.

## 23.3 Điều kiện thành công của nghiên cứu này

Theo tiêu chí thành công của protocol: sau khi đọc xong, có thể nhìn vào một chart **chưa biết kết quả** và trả lời một cách hệ thống:

| Câu hỏi | Trả lời được? | Dựa trên |
|---|---|---|
| Where is price? | ✅ | §21 bước 1 |
| What structural state? | ✅ | §11, §21 bước 2 |
| What liquidity exists? | ✅ | §7, §21 bước 4 |
| Which pools matter structurally? | ✅ | §7.1, hard filters §13.2 |
| Which candidate is the DOL? | ✅ | §3.3, §13 |
| Why X instead of Y? | ✅ | §13.3–13.4 asymmetry |
| Intermediate vs final objective? | ✅ | §8, §21 bước 10–11 |
| What invalidates? | ✅ | §22 câu 7 |
| **Can this be known before the move?** | ⚠️ **Cấu trúc: có. Thống kê: chưa biết** | §16.4 snapshot; §20 falsification |
| **Can it be tested?** | ✅ | §19, §20 |

> [!important] Chỗ duy nhất còn để ngỏ — và nó là chỗ quan trọng nhất
> Câu hỏi **"Can this be known before the move?"** không có câu trả lời dứt khoát, và **bài này không cố giả vờ rằng nó có**.
>
> Điều bài này làm được: chỉ ra **điều kiện cần** để câu hỏi đó trở nên trả lời được — snapshot bất biến, candidate hai phía, so sánh trong cùng distance bucket, baseline nearest-liquidity, và metric target-before-opposite-target.
>
> Điều bài này **không** làm được — và **không ai** làm được bằng reasoning thuần tuý: chứng minh rằng DOL có edge. Đó là câu hỏi empirical. Mọi bài viết nói ngược lại — dù ủng hộ hay phản đối ICT — đều đang bán cho bạn một kết luận mà họ chưa có dữ liệu để đưa ra.

---

## Liên kết

- [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] — SOP đầu ngày 7 bước, confluence tiers, case NQ, checklist journal
- [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] — chọn draw khi cấu trúc dày swing, Judas fuel vs bearish DOL
- [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] — N-bar pivot, Directional Change, ZigZag lookahead
- [[dol-ict-deep-dive]] — ontology nền, market mechanism, backtest framework bản đầu
- [[19-Liquidity]] · [[19-Liquidity#7. Buy-Side Liquidity (BSL)|Buy-side Liquidity]] · [[19-Liquidity#8. Sell-Side Liquidity (SSL)|Sell-side Liquidity]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]]
- [[12-Dealing-Range]] · [[59-Daily-Bias]] · [[27-Premium-Discount]] · [[15-Inducement]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]]

## References

Các nguồn học thuật dưới đây được truy cập qua abstract/trang tóm tắt nhà xuất bản trong phiên này (PDF fetch hỏng — xem callout đầu bài). Những mục không có trong phiên này được kế thừa từ [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] và [[dol-ict-deep-dive]], nơi chúng đã được dẫn với URL đầy đủ.

1. [Currency Orders and Exchange-Rate Dynamics: Explaining the Success of Technical Analysis — NY Fed Staff Report 125](https://www.newyorkfed.org/research/staff_reports/sr125.html) — Carol L. Osler. Abstract xác nhận trực tiếp: stop-loss và take-profit orders cụm mạnh quanh round numbers; pattern clustering khác nhau giữa hai loại và giữa stop-buy/stop-sell; đây là giải thích vi mô cho **cả hai** dự đoán TA (đảo tại level, tăng tốc khi xuyên level). Bản công bố: *Journal of Finance* 58(5), 2003.
2. [Stop-Loss Orders and Price Cascades in Currency Markets — NY Fed Staff Report 150](https://www.newyorkfed.org/research/staff_reports/sr150.html) — Carol L. Osler. Bằng chứng stop-loss orders đóng góp vào các move nhanh, tự củng cố.
3. [The Price Impact of Order Book Events](https://arxiv.org/abs/1011.6402) — Cont, Kukanov & Stoikov. Price change ngắn hạn gắn với order-flow imbalance; price impact lớn hơn khi depth mỏng.
4. [Futures Order Types — CME Group](https://www.cmegroup.com/education/courses/things-to-know-before-trading-cme-futures/futures-order-types) — stop order không xuất hiện tức thời trên book; chỉ kích hoạt khi thị trường giao dịch tại trigger price.
5. [Trading Basics — SEC](https://www.sec.gov/files/trading101basics.pdf) — stop order trở thành market order khi trigger.
6. [Regulatory Notice 16-19 — FINRA](https://www.finra.org/rules-guidance/notices/16-19) — hướng dẫn về stop orders trong điều kiện thị trường biến động mạnh; rủi ro execution.
7. [OTC foreign exchange turnover — BIS Triennial Central Bank Survey](https://www.bis.org/publications/202210-commentary-otc-derivatives) — FX là thị trường OTC phân tán.
8. [Liquidity, Volatility and Flights to Safety in the U.S. Treasury Market — NY Fed SR590](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr590.html) — depth giảm và volatility tăng quanh các mốc công bố.
9. [2022 ICT Mentorship Episode 3 — Internal Range Liquidity & Market Structure Shifts](https://www.youtube.com/watch?v=vJWdXPe8Reo) — nguồn ICT gốc cho IRL/ERL và MSS.
10. [2022 ICT Mentorship Episode 22](https://www.youtube.com/watch?v=QKc_i90chVg) — relative equal lows như DOL.
11. [ICT 2022 Mentorship: How to Build a Narrative for Bias and Identify Draw on Liquidity](https://www.youtube.com/watch?v=FSSr7rg1vXw) — ICT gốc về narrative và DOL.

> [!note] Về các nguồn thứ cấp
> Các nguồn dạng blog/YouTube tutorial (innercircletrader.net, TTrades, LiquidityScan và tương tự) được dùng trong [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] như **thực hành từ nguồn thứ cấp**, không phải định nghĩa ICT gốc. Bài này kế thừa phân loại đó và không nâng cấp chúng thành nguồn chuẩn. Mọi ngưỡng số đến từ các nguồn đó (reach phiên, kích thước FVG, tỷ lệ size) **phải tự kiểm chứng** trên dữ liệu của bạn.
