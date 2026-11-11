---
type: ict-concept
concept: Dealing Range
aliases:
  - Dealing Range
  - Trading Range
tags:
  - trading/ict/concept
  - trading/study
  - "#DealingRange"
status: developing
category: Market Structure
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-11-03
created: 2026-06-22
updated: 2026-10-06
common_mistakes:
  - "[[Mistake - Wrong Dealing Range]]"
  - "[[Mistake - Premium Discount Off Wrong Range]]"
  - "[[Mistake - Buying Premium Selling Discount]]"
---

# Dealing Range

> [!summary] Tóm tắt 1 câu
> **Dealing Range là một hệ tọa độ neo vào hai swing có hệ quả cấu trúc — origin (protected) và termination — dùng để đo vị trí của giá (premium / discount / EQ), chia liquidity thành internal / external và xác định điểm invalidation. Nó là bộ lọc vị trí, không phải nguồn edge: vị trí chỉ khuếch đại một directional edge độc lập, nếu edge đó tồn tại.**

> [!info] Note này — phiên bản v0.2 (2026-10-06)
> - **v0.2 gộp** phần concept cũ (§1–17) và *Structural Framework v0.1* (§18 cũ) thành **một** note: mỗi chủ đề chỉ được trình bày đầy đủ ở một chỗ, các chỗ khác trỏ link. Các callout "Cập nhật v0.1" đã được viết lại thành nội dung chính. Changelog chi tiết: [[#20.4. Changelog v0.1 → v0.2|§20.4]].
> - **Mới trong v0.2:** nghiên cứu thực nghiệm trên dữ liệu OHLC thật ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]]), 5 chart dựng từ dữ liệu thật EURUSD H1 (§4, §5, §6), 6 sơ đồ kết quả, register giả thuyết cập nhật trạng thái (§20.1).
> - **Note liên quan:** [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest|57 — DR research (VALID / REFINED / SUSPENDED / REPLACED)]] · [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong|54 — Directional Change]] · [[37-Re-mapping-Dealing-Range-sau-Displacement|37 — Re-mapping]] · [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c — State machine D1-H1-M5]].
> - Ba kết luận nền của note 57 được giữ nguyên: (1) không tồn tại định nghĩa canon cho "dealing range"; (2) wick không invalidate range — chỉ body-close mới invalidate; (3) range validity ≠ directional thesis.

> [!important] Nguyên tắc cốt lõi
> 1. **Mọi con số premium / discount / OTE chỉ có nghĩa trên một range được chọn bằng quy tắc viết trước** — anchor có hệ quả cấu trúc, có `known_at`, range ở state ACTIVE. Range sai thì vị trí sai: mua premium mà tưởng là discount.
> 2. **Nhưng range đúng không tự tạo edge.** Dưới martingale, mọi vị trí có E[R] = 0 ([[#14.3. Equilibrium|§14.3]]); trên dữ liệu thật, vị trí trong leg DR không cho expectancy khác null một cách robust ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]]). Range là điều kiện cần cho **kỷ luật vị trí và invalidation**, không phải lý do để vào lệnh.

> [!abstract]- 12 kết luận khái niệm + 6 kết quả thực nghiệm (bấm để mở)
> **Khái niệm (v0.1, vẫn giữ):**
> 1. DR là **hệ tọa độ, không phải lực** — premium/discount/EQ là tọa độ; giá trị dự báo (nếu có) đến từ anchor có hệ quả cấu trúc (§1.3).
> 2. Chất lượng DR = chất lượng anchor = **structural consequence** của swing; mọi anchor có `known_at` (§3.3–§3.4).
> 3. **Ba họ range** — Leg / Container / Lookback (IPDA) — trả lời ba câu hỏi khác nhau (§1.2).
> 4. Internal/external là **quan hệ**; micro → HTF là **scale** — hai trục độc lập (§3.2).
> 5. **Martingale null:** không có drift thì E[R] = (q − p)/p = 0 tại mọi vị trí (§14.3).
> 6. Câu hỏi kiểm chứng đúng: vị trí + cấu trúc có làm xác suất thắng vượt **null cùng cách đo** và baseline anchor ngây thơ không (§19).
> 7. Vòng đời range là **state machine**; sweep ≠ invalidation; completion ≠ invalidation (§5.2).
> 8. **Ý nghĩa thuộc về swing bị phá**, không thuộc timeframe đang nhìn — H1 không override D1 trừ khi phá swing cấp D1 (§4.2, R7).
> 9. **LRI** — tính location trên mọi candidate hợp lệ; LRI thấp = không có location edge (§4.4).
> 10. Random walk cũng tạo swing, range và "sweep" — cấu trúc không phải bằng chứng (§3.2, §16).
> 11. "Range được chọn đúng" phải là một hàm xác định viết **trước** khi test (§19.4).
> 12. Có những lúc **không dùng DR** (§2 — Khi nào nên bỏ qua?).
>
> **Thực nghiệm (v0.2 — exploratory, chưa phải instrument mục tiêu, chưa trừ phí; §19.3):**
> 13. Gradient MEHR theo vị trí **xuất hiện y hệt trên random walk** → artifact của theo dõi rời rạc / gap. Phải đo bằng P/W hoặc so với null cùng cách theo dõi.
> 14. P/W theo vị trí ≈ 0 ở mọi bin, mọi θ ∈ {1.5, 2, 3}; structural ≈ IPDA-20 ≈ anchor ngẫu nhiên.
> 15. Chênh lệch discount − premium: chỉ θ = 1.5 / structural có CI vừa đủ trên 0 (+0.024 W ≈ +0.08R trước phí) → **WEAK EVIDENCE**, không robust theo θ.
> 16. **Sweep protected origin** hạ P(EXTENDED) từ ~0.58 xuống ~0.24–0.28 (null 0.17–0.18) → là *cảnh báo base-rate*, không phải xác nhận continuation.
> 17. INVALIDATED theo nghĩa "close xuyên origin mà chưa có MSS ngược chiều" chỉ ~1%: thất bại gần như luôn hiện ra dưới dạng **MSS ngược chiều cùng scale** (REVERSED), ~một nửa trong số đó khi origin còn nguyên.
> 18. Bốn định nghĩa range (leg θ = 1.5 / 2 / 3, IPDA-20) chỉ đồng thuận premium/discount ở **54–70% số bar — bằng null**: LRI thấp là trạng thái bình thường, không phải bất thường.

> [!info]- Hệ thống nhãn bằng chứng dùng trong note
> | Nhãn | Ý nghĩa | Mức tin cậy mặc định |
> |---|---|---|
> | **[MATHEMATICAL]** | Đúng theo định nghĩa hoặc chứng minh toán học (ví dụ EQ = 50%) | Cao — nhưng chỉ nói về *hình học*, không nói về *hành vi giá* |
> | **[MARKET MECHANICS]** | Giải thích được bằng order matching, liquidity, price discovery, auction; hoặc có bằng chứng thực nghiệm đã công bố | Cao → trung bình |
> | **[ICT FRAMEWORK]** | Cách ICT / cộng đồng ICT định nghĩa hoặc dùng khái niệm | Cao về *định nghĩa*, không nói gì về *hiệu quả* |
> | **[INTERPRETATION]** | Cách giải thích hợp lý nhưng không chứng minh trực tiếp được từ OHLC | Trung bình → thấp |
> | **[HYPOTHESIS]** | Giả thuyết kiểm chứng được | Chưa biết |
> | **[BACKTEST REQUIRED]** | Không coi là edge cho tới khi test đúng phương pháp | — |
> | **[EMPIRICAL v0.2]** | Kết quả từ nghiên cứu thực nghiệm của chính note này (§19.3) — exploratory | Thấp → trung bình; xem giới hạn §19.3.7 |
> | **HEURISTIC** | Ngưỡng số đặt ra để vận hành, chưa tối ưu, chưa validate | — |
>
> **Về nguồn ICT:** giáo trình gốc của ICT chủ yếu ở dạng video/mentorship, không có văn bản định nghĩa chính thức. "[ICT FRAMEWORK]" trong note là *cách hiểu phổ biến trong tài liệu cộng đồng* (Tier 3–4). Note không trích nguyên văn ICT và không gán cho ICT những câu chưa kiểm chứng.

![[Dealing-Range-v02-00-Note-Map.svg|760]]
*Sơ đồ: bản đồ note v0.2 — bốn lớp (khái niệm → cơ chế → phản biện & ngoại lệ → bằng chứng) và hai lộ trình đọc.*

> [!note]- Mục lục
> - [[#1. Định nghĩa|1. Định nghĩa]]
> - [[#2. Bối cảnh sử dụng|2. Bối cảnh sử dụng]]
> - [[#3. Cấu trúc nhận diện trên chart|3. Cấu trúc nhận diện trên chart]]
> - [[#4. Quy trình phân tích đa khung thời gian|4. Quy trình phân tích đa khung thời gian]]
> - [[#5. Quy tắc xác nhận / vô hiệu hóa|5. Quy tắc xác nhận / vô hiệu hóa]]
> - [[#6. Ví dụ chart|6. Ví dụ chart]]
> - [[#7. Entry model liên quan|7. Entry model liên quan]]
> - [[#8. Checklist trước khi áp dụng vào trade|8. Checklist trước khi áp dụng vào trade]]
> - [[#9. Lỗi thường gặp|9. Lỗi thường gặp]]
> - [[#10. Câu hỏi tự kiểm tra|10. Câu hỏi tự kiểm tra]]
> - [[#11. Flashcards / Active Recall|11. Flashcards / Active Recall]]
> - [[#12. Lesson Learned|12. Lesson Learned]]
> - [[#13. Mức độ thành thạo|13. Mức độ thành thạo]]
> - [[#14. Cơ chế thị trường & các lăng kính diễn giải|14. Cơ chế thị trường & các lăng kính diễn giải]]
> - [[#15. Phản biện & giới hạn (Critique)|15. Phản biện & giới hạn (Critique)]]
> - [[#16. Edge Cases & Counterexamples — catalog đã gộp|16. Edge Cases & Counterexamples — catalog đã gộp]]
> - [[#17. Case Studies|17. Case Studies]]
> - [[#18. Khung định lượng & thuật toán|18. Khung định lượng & thuật toán]]
> - [[#19. Backtest & bằng chứng thực nghiệm|19. Backtest & bằng chứng thực nghiệm]]
> - [[#20. Hypothesis register & câu hỏi nghiên cứu|20. Hypothesis register & câu hỏi nghiên cứu]]
> - [[#Tài liệu tham khảo|Tài liệu tham khảo]]

---

## 1. Định nghĩa

**Khái niệm (bản dùng hằng ngày):**
Dealing Range là **khoảng giá giữa hai swing đối nghịch có quan hệ cấu trúc với nhau**, mà giá hiện tại được đọc *tương đối* so với nó. Trong dạng phổ biến nhất (leg DR), anchor thứ nhất là **origin** của leg vừa tạo structural break (BOS/MSS) — chính là *protected swing* và là điểm invalidation của câu chuyện; anchor thứ hai là **termination** — cực trị mà leg đó đạt được. Trên cặp anchor này ta đặt hệ tọa độ: EQ = 50%, nửa phía origin là discount (bullish) / premium (bearish), nửa phía termination là phía ngược lại.

Việc một anchor *đã quét liquidity* (sweep một đỉnh/đáy cũ trước khi đảo) là **bằng chứng hỗ trợ**, không phải điều kiện định nghĩa: liquidity tại boundary là biến ẩn, không quan sát được trên OHLC ([[#14.5. Liquidity Relationship|§14.5]]). Điều kiện định nghĩa là **hệ quả cấu trúc** — từ anchor đó giá đã phá một swing đối diện cùng cấp ([[#3.3. How to Select Meaningful Swings|§3.3]]).

**Mục đích trong ICT:**
- **Đo vị trí:** premium / discount / equilibrium và OTE (retracement 62–79%) đều là tọa độ trên range. Xem [[27-Premium-Discount]] và [[26-OTE-Optimal-Trade-Entry|OTE]].
- **Phân vùng liquidity:** *external range liquidity* (ERL — vùng ngoài hai boundary, nơi có thể có BSL/SSL) và *internal range liquidity* (IRL — FVG, OB, equal highs/lows nhỏ bên trong). Xem [[16-Internal-External-Range-Liquidity-IRL-ERL]].
- **Khung cho draw on liquidity:** DOL thường là một boundary hoặc một mức ngoài range; range cho biết đường đi tới đó dài bao nhiêu và còn bao nhiêu liquidity đối diện ([[#14.6. Draw on Liquidity Relationship|§14.6]]).
- **Định nghĩa invalidation:** protected anchor là nơi câu chuyện cấu trúc chết — đặt stop có cơ sở thay vì đặt theo cảm giác.
- **Nền cho Daily Bias:** bias dùng vị trí trong range + DOL + structure; xem [[59-Daily-Bias]].

**Vì sao quan trọng:** premium/discount, OTE và EQ đều là **tỷ lệ phần trăm đo trên một range** — range sai thì mọi con số phái sinh sai. Nhưng điều ngược lại không đúng: range đúng **không** đảm bảo con số đó có giá trị dự báo. Phân biệt hai điều này là trục chính của cả note.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đang ở premium hay discount — **của range nào, scale nào, chọn bằng quy tắc nào?**
- Protected anchor ở đâu — câu chuyện cấu trúc chết ở mức giá nào?
- External liquidity nào còn mở để làm DOL; internal liquidity (FVG/OB) nào nằm đúng phía location?
- Range đang ở state nào (FORMING / ACTIVE / SWEPT / EXTENDED / COMPLETED / INVALIDATED / CONSOLIDATING)?
- Các range hợp lệ khác nhau có đồng thuận về location không (LRI)?

### 1.1. Định nghĩa bốn cấp

#### 1.1.1 Level 1 — Beginner

> **Dealing Range là khoảng giá giữa một swing high quan trọng và một swing low quan trọng gần đây, bên trong đó giá đang "thương lượng".** Ta chia nó làm đôi: nửa trên là **premium** (đắt), nửa dưới là **discount** (rẻ), đường giữa là **equilibrium** (cân bằng).

Ví dụ: swing low 1.0800, swing high 1.1000. EQ = 1.0900. Giá 1.0850 nằm ở 25% range → discount.

#### 1.1.2 Level 2 — Structural

> **Dealing Range là một cặp anchor (A_low, A_high) gồm hai swing đối nghịch có quan hệ cấu trúc với nhau — thường là: một swing là *origin* (điểm xuất phát) của leg đã tạo ra structural break gần nhất, swing kia là *termination* (cực trị mà leg đó đạt được) — và giá hiện tại đang được diễn giải tương đối so với cặp này.**

Ba điều kiện cấu trúc tối thiểu:

1. **Liên kết (connectedness):** hai anchor thuộc cùng một leg hoặc cùng một container — không phải hai điểm bất kỳ.
2. **Hệ quả (consequence):** ít nhất một anchor (origin) có structural consequence — từ nó giá đã phá một swing đối diện cùng cấp.
3. **Sống (liveness):** anchor "protected" chưa bị invalidate.

#### 1.1.3 Level 3 — ICT Framework

**[ICT FRAMEWORK]** Trong cách dùng phổ biến của cộng đồng ICT:

- DR được xác định bởi một swing high và swing low; **equilibrium** = 50%; phía trên = **premium**, phía dưới = **discount**.
- Trong bối cảnh bullish, tìm **bullish PD arrays** (FVG, Order Block, Breaker, …) nằm ở **discount**; trong bối cảnh bearish, tìm bearish PD arrays ở **premium**. (Khung phân loại này thường được gọi là *PD Array Matrix*.)
- **External Range Liquidity (ERL):** buy stops phía trên range high (BSL), sell stops phía dưới range low (SSL).
- **Internal Range Liquidity (IRL):** các yếu tố bên trong range — chủ yếu là FVG, cùng với order block và equal highs/lows nhỏ trong leg.
- Nguyên lý luân phiên được mô tả: *sau khi external liquidity bị lấy, DOL tiếp theo thường là internal (quay lại range để "rebalance" inefficiency); khi internal được lấp, kỳ vọng chuyển ra phía extreme đối diện* (theo mô tả của LuxAlgo Library).
- **IPDA Data Ranges:** nhìn lại 20, 40, 60 trading days trên D1, đánh dấu highest high / lowest low của mỗi cửa sổ làm boundary tham chiếu cho ngắn/trung/dài hạn; cửa sổ trượt theo thời gian.
- **OTE (Optimal Trade Entry):** vùng retracement 62%–79% của leg (70.5% là mức giữa thường được nhắc) — tức nằm sâu trong discount của leg DR đối với setup bullish.
- Trong **ICT 2022 Model**, sau liquidity sweep + MSS có displacement, range thường được vẽ từ extreme của sweep đến extreme của displacement leg; entry tìm ở FVG trong discount (bullish) / premium (bearish) của leg đó.

**Lưu ý phê phán:** Các nguồn cộng đồng thống nhất về *công thức* (50%) nhưng **không thống nhất về quy tắc chọn anchor**. Đó chính là khoảng trống mà note này cố lấp.

#### 1.1.4 Level 4 — Quantitative

Một Dealing Range tại thời điểm t, trên timeframe TF, được định nghĩa là một bộ:

```text
DR_t = {
  TF,                      # timeframe gốc
  family,                  # LEG | CONTAINER | LOOKBACK
  direction,               # BULL | BEAR | NEUTRAL (container)
  L*, t_L,                 # giá & thời điểm của anchor dưới
  H*, t_H,                 # giá & thời điểm của anchor trên
  origin_side,             # anchor nào là origin/protected
  known_at,                # thời điểm sớm nhất range xác định được KHÔNG dùng future data
  scale_k,                 # cấp độ (theta* bin) của anchors
  state,                   # FORMING | ACTIVE | EXTENDED | SWEPT_H | SWEPT_L | COMPLETED | INVALIDATED | CONSOLIDATING
}
```

Các đại lượng dẫn xuất:

$$W = H^* - L^*, \qquad EQ = \frac{H^* + L^*}{2}, \qquad p_t = \frac{P_t - L^*}{W}$$

- Discount: p < 0.5; Premium: p > 0.5; OTE (bullish leg): 0.21 ≤ p ≤ 0.38 (tương đương retracement 62–79%).
- Chuẩn hóa theo volatility: W_ATR = W / ATR_TF(n).

Và quan trọng nhất: **anchors là output của một hàm xác định**

$$(L^*, H^*) = A(\text{OHLC}_{\le t};\ \theta)$$

trong đó A chỉ dùng dữ liệu đến t và θ là bộ tham số được cố định trước khi test.

#### 1.1.5 Mathematical range vs Structural DR vs ICT DR

| Chiều | Mathematical range | Structural dealing range | ICT dealing range |
|---|---|---|---|
| Định nghĩa | max(High) − min(Low) trên một cửa sổ bất kỳ | Cặp anchor có quan hệ cấu trúc & hệ quả | Structural DR + lớp diễn giải liquidity/PD array/DOL |
| Luôn tồn tại? | Có, với mọi cửa sổ | Không — cần điều kiện cấu trúc | Không |
| Phụ thuộc lựa chọn | Độ dài cửa sổ | Định nghĩa swing, scale, break rule | Như structural + diễn giải |
| Khách quan? | Hoàn toàn | Có thể formalize | Phần diễn giải khó formalize |
| Mang thông tin gì | Biên độ đã xảy ra | Vị trí so với leg/container đang chi phối | Vị trí + giả thuyết về đích đến |
| Ví dụ | High/low của 37 bar gần nhất | Protected low → high sau BOS | Như bên trái + "SSL dưới low, tìm FVG discount" |

**Kết luận:** mọi ICT DR là một mathematical range, nhưng không phải mọi mathematical range là structural DR, và không phải mọi structural DR có diễn giải ICT hợp lệ. IPDA lookback là trường hợp đặc biệt thú vị: nó là *mathematical range* (cửa sổ cố định) được *dùng như* ICT range — nên nó là baseline khách quan tốt nhất.

### 1.2. Ba họ Dealing Range

Phần lớn tranh cãi "range nào mới đúng" đến từ việc trộn ba vật thể khác nhau dưới cùng một cái tên:

| Họ | Anchors | Trả lời câu hỏi | Khi hữu ích nhất |
|---|---|---|---|
| **Leg DR** (impulse range) | Origin → termination của leg gần nhất đã tạo BOS/MSS hợp lệ | "Pullback hiện tại rẻ hay đắt so với impulse vừa xảy ra?" | Trend, ICT 2022 Model, OTE |
| **Container DR** (external range) | Swing high và swing low *chưa bị phá* gần nhất ở cấp ≥ k đang bao quanh giá | "Liquidity bên ngoài nằm đâu ở hai phía, giá đang ở đâu trong hộp?" | Consolidation, bản đồ DOL |
| **Lookback DR** (IPDA 20/40/60) | Highest high / lowest low trong N phiên | "Trong cửa sổ thời gian chuẩn, giá đang ở đâu?" | Baseline khách quan, HTF context |

![[Dealing-Range-v01-02-Ba-Ho-Range.svg|760]]
*Sơ đồ: ba họ Dealing Range — leg, container, lookback — và câu hỏi mỗi họ trả lời.*

Ba hệ quả thực hành:

1. **Một câu "giá đang ở discount" phải kèm tên họ range.** Cùng một bar có thể là discount của leg DR và premium của container — cả hai đều "đúng" theo câu hỏi của chúng ([[#4.4. Bài toán quá nhiều range và LRI|§4.4]], Real 4).
2. **Lookback DR là baseline khách quan nhất** — IPDA 20 ngày chính là Donchian channel 20 ([[#14.8. Alternative Interpretations|§14.8]]). Mọi quy tắc chọn anchor "thông minh" phải chứng minh nó tốt hơn baseline này; trên dữ liệu v0.2 nó **chưa** chứng minh được ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]]).
3. **"Internal / External" là quan hệ, không phải thuộc tính.** Một swing chỉ internal hay external *so với một range cụ thể*; còn "micro → HTF" là trục *scale*. Hai trục độc lập — xem phân loại hai trục ở [[#3.2. Swing Classification|§3.2]].

### 1.3. Mental Model of Dealing Range

#### 1.3.1 Phép ẩn dụ: cây thước đặt lên bản đồ

Hãy tưởng tượng chart là một địa hình. Dealing Range là **cây thước** bạn đặt lên địa hình đó, hai đầu thước chạm vào hai mốc địa hình (một đỉnh, một đáy).

- Vạch 50% là **trung điểm của cây thước**, không phải thuộc tính của địa hình.
- Nếu bạn đặt thước lệch sang một mốc khác, vạch 50% dời đi — dù địa hình không đổi một centimet.
- Thước chỉ hữu ích nếu hai mốc là **mốc thật** (đỉnh núi, đáy thung lũng) chứ không phải hòn sỏi.

**Giới hạn của ẩn dụ:** địa hình không "nhìn thấy" thước của bạn, còn thị trường thì có thể — nếu đủ nhiều người tham gia dùng cùng một loại thước (cùng swing, cùng Fibonacci 50%), lệnh của họ có thể tập trung quanh các vạch đó và tạo ra hiệu ứng tự thực hiện (reflexivity). Đây là lý do duy nhất hợp lý để một mức "hình học" có thể có hệ quả "hành vi" — và nó là [HYPOTHESIS], không phải fact.

#### 1.3.2 Ba câu hỏi — ba công cụ khác nhau

```text
WHERE AM I?          → Dealing Range  (location / tọa độ)
WHERE AM I GOING?    → Draw on Liquidity  (destination / mục tiêu)
WHAT CONFIRMS IT?    → PD Array + LTF trigger  (evidence + trigger)
```

Một lỗi rất phổ biến là dùng một công cụ để trả lời câu hỏi của công cụ khác: dùng DR để quyết định hướng ("giá đang ở discount nên sẽ lên"), hoặc dùng DOL để quyết định entry ("DOL ở trên nên mua ngay").

#### 1.3.3 Pipeline nhận thức

![[Dealing-Range-v01-01-Pipeline.svg|760]]
*Sơ đồ: pipeline phân tích — swings → significance → structure → anchors → DR → coordinates → location filter; direction / evidence / trigger là ba đầu vào riêng.*

Thứ tự này có chủ đích: **swing được xác định trước range**, không phải ngược lại. Nếu bạn chọn range trước rồi mới gán nhãn internal/external cho swing, bạn đã tạo ra lập luận vòng tròn (mục 14.7).

#### 1.3.4 Một câu tóm tắt

> **Dealing Range là hệ tọa độ được neo vào hai swing có hệ quả cấu trúc; nó cho biết giá đang "rẻ hay đắt" *so với leg/container mà ta tin là đang chi phối*, và giá trị của nó hoàn toàn phụ thuộc vào (1) việc anchors có thật sự quan trọng không và (2) có một directional edge độc lập để khuếch đại hay không.**

### 1.4. Conceptual Foundation

#### 1.4.1 Tại sao giá tạo ra swing? (intuition)

Giá không đi thẳng. Nó di chuyển theo nhịp: đẩy (impulse) → nghỉ/hồi (correction) → đẩy tiếp hoặc đảo chiều. Mỗi lần đổi nhịp để lại một điểm cực trị cục bộ — **swing high** hoặc **swing low**.

**[MARKET MECHANICS]** Về cơ chế, một swing high là mức giá mà tại đó, trong cửa sổ quan sát, lực mua chủ động (aggressive buyers dùng market order) không còn tìm được đủ người bán ở giá cao hơn để đẩy giá tiếp — hoặc lực bán chủ động xuất hiện áp đảo. Điều *quan sát được* là: giá đã thử mức đó và quay lại. Điều *không quan sát được* từ OHLC: ai bán, tại sao, bao nhiêu lệnh còn nằm chờ phía trên.

#### 1.4.2 Tại sao cần khái niệm "range"?

Vì mọi đánh giá "rẻ" hay "đắt" đều **tương đối**. Không có mức giá nào tự nó là rẻ. Một cổ phiếu 100 USD rẻ nếu tháng trước giao dịch 80–140, đắt nếu tháng trước giao dịch 60–105. Range là cách chuẩn hóa: đặt giá hiện tại vào tỷ lệ 0–1 giữa hai mốc tham chiếu.

**[MARKET MECHANICS] — góc nhìn Auction Market Theory:** Thị trường là một cuộc đấu giá liên tục tìm mức giá tạo thuận lợi cho giao dịch hai chiều. Khi giá dao động trong một vùng mà cả hai phía đều chấp nhận giao dịch, thị trường ở trạng thái **balance** (tương ứng với một range). Khi một phía áp đảo và giá rời vùng cân bằng để tìm mức mới, thị trường ở trạng thái **imbalance** (tương ứng với impulse / displacement). Boundaries của balance là nơi cuộc đấu giá từng "bị từ chối" (excess). Đây là nền tảng lý thuyết (không phải ICT) giải thích *tại sao* range boundaries có thể quan trọng: chúng đánh dấu giới hạn mà một phía đã từng không thể vượt qua.

#### 1.4.3 Tại sao midpoint có vẻ quan trọng?

**[MATHEMATICAL]** Midpoint là điểm duy nhất mà khoảng cách đến hai boundary bằng nhau. Nếu hai boundary là hai mục tiêu tiềm năng (hai pool liquidity), thì tại EQ, phần thưởng đi về hai phía là cân xứng. Dưới EQ, khoảng cách đến boundary trên lớn hơn khoảng cách đến boundary dưới — nghĩa là một lệnh Buy "nhắm high, stop dưới low" có R:R > 1.

**[INTERPRETATION]** ICT diễn giải phía dưới EQ là "discount" (nơi giá rẻ so với range, nơi nên tìm cơ hội mua *nếu* bối cảnh bullish) và phía trên là "premium". Đây là một diễn giải *có điều kiện*: nó chỉ có nghĩa khi đi kèm một hướng.

#### 1.4.4 Bốn tầng hiểu — cách note này tiến triển

```text
Intuition        → "Cái hộp giữa đỉnh và đáy quan trọng gần nhất."
Simple example   → Low 100, High 110, EQ 105, giá 103 = discount 30%.
Technical def.   → Frame neo vào protected swing + termination swing, có state & known_at.
Advanced interp. → Frame là location filter khuếch đại directional edge; vô giá trị dưới martingale.
```

### 1.5. Dealing Range không phải là gì

- **Không phải mọi cặp swing high/low gần giá.** Anchor phải có hệ quả cấu trúc ở scale đang xét; swing "nhìn rõ" hay "gần giá" không đủ ([[#3.3. How to Select Meaningful Swings|§3.3]]).
- **Không phải một lực.** Thước đo không đẩy giá; EQ không có giá trị dự báo nội tại ([[#14.3. Equilibrium|§14.3]]).
- **Không phải tín hiệu vào lệnh.** DR nói "nếu định mua, ở đây rẻ hơn so với leg đang chi phối" — không nói "mua ở đây". Entry cần evidence (PD array) + trigger (sweep / MSS / displacement) ([[#7. Entry model liên quan|§7]]).
- **Không phải khung cố định.** Range có vòng đời; cập nhật theo **event**, không theo cảm giác ([[#5.3. Range Updating|§5.3]]).
- **Không phải directional thesis.** Range còn VALID không có nghĩa hướng còn đúng, và ngược lại — hai biến khác nhau. Gộp chúng là nguồn gốc của lỗi "đảo bias ở đáy pullback".
- **Không phải thứ chọn lại sau khi thấy kết quả.** Range vẽ lại sau khi biết giá đi đâu là hindsight, không phải phân tích ([[#5.5. Hindsight Bias|§5.5]]).
- **Không phải lý do để đo premium/discount bằng range của timeframe khác với narrative.** Range M5 dùng cho execution; location của bias đo trên range của scale quyết định ([[#4. Quy trình phân tích đa khung thời gian|§4]]).

---

## 2. Bối cảnh sử dụng

### 2.1. Why Dealing Range Matters

#### 2.1.1 Range đại diện cho điều gì?

**[INTERPRETATION]** Range đại diện cho **biên của quá trình price discovery gần nhất ở một scale nhất định**: vùng giá mà thị trường đã khám phá và chấp nhận giao dịch, giới hạn bởi hai mức mà tại đó một phía đã từng bị từ chối.

#### 2.1.2 Premium / Discount: tuyệt đối hay tương đối?

**Tương đối hoàn toàn.** [MATHEMATICAL] Vì p = (P − L*)/W, cùng một P cho ra p khác nhau với anchors khác nhau. Ví dụ:

| Range | L* | H* | EQ | p tại P = 116 | Nhãn |
|---|---|---|---|---|---|
| Leg E–F | 112 | 125 | 118.5 | 0.31 | Discount |
| Leg C–F | 105 | 125 | 115.0 | 0.55 | Premium |
| Trend A–F | 100 | 125 | 112.5 | 0.64 | Premium |

Cùng một giá, ba nhãn. Không có "premium thật". Chỉ có "premium *so với range X*". Vì vậy câu "giá đang ở discount" là câu **chưa đầy đủ** cho đến khi bạn nói "discount của range nào, ở scale nào, được chọn bằng quy tắc nào".

#### 2.1.3 Equilibrium có predictive value không?

**Không có predictive value nội tại.** [MATHEMATICAL] EQ là trung điểm của một đoạn thẳng. Nếu nó có giá trị dự báo, giá trị đó phải đến từ: (a) anchors thực sự quan trọng, và (b) người tham gia thị trường hành xử khác biệt quanh mức đó (reflexivity, retracement statistics). Cả hai là [HYPOTHESIS] — mục 14.3 thiết kế test.

#### 2.1.4 Lợi ích thực sự (không huyền bí) của DR

1. **Chuẩn hóa location** — so sánh được giữa các instrument và thời điểm (p là unitless).
2. **Hình học R:R** — [MATHEMATICAL] Với lệnh Buy tại p, stop tại L*, target tại H*: R:R = (1−p)/p, break-even win rate = p. Discount *đảm bảo* R:R > 1 nếu target là range high. Đây là lợi ích **cơ học**, không phải dự báo.
3. **Phân vùng liquidity** — chia liquidity thành internal/external để lập mô hình DOL.
4. **Lọc và xếp hạng POI** — chỉ giữ POI cùng phía location với direction.
5. **Định nghĩa invalidation** — protected anchor là điểm mà câu chuyện cấu trúc chết.

#### 2.1.5 Hệ quả quan trọng — Martingale Null (phiên bản trực giác)

Nếu bạn tung đồng xu công bằng để di chuyển giá lên/xuống từng bước nhỏ, và bạn mua ở 25% của range (stop ở đáy, target ở đỉnh), bạn có R:R = 3:1 — nhưng xác suất đến đỉnh trước đáy chỉ là 25%. Expectancy = 0.25 × 3 − 0.75 × 1 = 0. Mua ở 10%? R:R 9:1, xác suất 10%, expectancy vẫn = 0. **Hình học không tạo ra tiền. Chỉ có sự lệch khỏi ngẫu nhiên mới tạo ra tiền.** (Phiên bản đầy đủ: mục 14.3–14.4.)

### 2.2. Các thành phần bên trong một Dealing Range

| Thành phần | Vị trí | Ý nghĩa thực chiến | Nhãn bằng chứng |
|---|---|---|---|
| **Termination** (bullish: range high) | Đầu phía impulse | Mục tiêu tự nhiên của leg; vượt bằng close + acceptance = BOS/EXTENDED (completion, không phải thất bại) | [MATHEMATICAL] về vị trí; DOL là [HYPOTHESIS] |
| **Origin / protected** (bullish: range low) | Đầu phía khởi phát | Điểm invalidation của câu chuyện cấu trúc; nơi đặt stop có cơ sở | [ICT FRAMEWORK] + định nghĩa structure |
| **External liquidity (ERL)** | Ngoài hai boundary | Có thể có buy stops trên high (BSL) và sell stops dưới low (SSL) — ứng viên DOL | [INTERPRETATION] — biến ẩn |
| **Internal liquidity (IRL)** | FVG / OB / equal highs-lows nhỏ bên trong | Vùng giá có thể quay về rebalance trước khi đi tiếp; nơi tìm POI | [ICT FRAMEWORK] → [HYPOTHESIS] (HYP-DR-008) |
| **Equilibrium (50%)** | Giữa range | Ranh giới hình học giữa hai nửa; quanh đây R:R tới boundary ≈ 1:1 | [MATHEMATICAL]; mọi claim hành vi tại EQ là [HYPOTHESIS] (HYP-DR-005) |
| **Nửa phía origin** (bullish: discount) | bullish: 0 ≤ p < 0.5 · bearish: 0.5 < p ≤ 1 | Vùng *được phép* tìm entry theo hướng leg — là **bộ lọc**, không phải tín hiệu | Không có edge riêng trên dữ liệu v0.2 (§19.3) |
| **Nửa phía termination** (bullish: premium) | phần còn lại của range | Vùng không mở lệnh mới theo hướng leg; vùng chốt lời | — |

> [!tip] Đỉnh/đáy range và liquidity — đọc đúng mức bằng chứng
> "Đỉnh range là nơi buy stops nằm" là **[INTERPRETATION]** hợp lý (stop của người short + lệnh breakout), không phải fact. Bằng chứng thực nghiệm mạnh nhất về tập trung lệnh — Osler (2003), FX — nói về **số tròn**, không trực tiếp về swing high/low; stop orders thường **không hiển thị** trong displayed order book. Boundary là *ứng viên* liquidity; độ hợp lý tăng theo mức hiển nhiên (equal highs/lows, PDH/PDL), tuổi và số lần test ([[#14.5. Liquidity Relationship|§14.5]]).

### Khi nào khái niệm này có giá trị cao?
- [ ] Có một **directional thesis độc lập** với range (D1 structure + DOL) — vì location chỉ *khuếch đại* edge, không tạo ra edge ([[#14.3. Equilibrium|§14.3]]).
- [ ] Anchor có **hệ quả cấu trúc rõ** ở đúng scale của quyết định (origin của BOS/MSS, θ\* đủ lớn, `known_at` đã qua).
- [ ] Range ở state **ACTIVE** (termination đã đóng bằng một nhịp hồi đạt ngưỡng), không FORMING, không CONSOLIDATING.
- [ ] Các candidate range hợp lệ **đồng thuận** về location (LRI cao) — hoặc conflict đã được ghi nhận và xử lý bằng R1–R7 ([[#4.2. Range Hierarchy|§4.2]]).
- [ ] Range **đủ rộng** so với stop (W ≥ c1 × stop) và không quá nhỏ so với hành trình đến DOL (M_ratio hợp lý).
- [ ] Có POI (FVG/OB) nằm đúng nửa location cho hướng trade và có kế hoạch trigger trên LTF.
- [ ] Thị trường/phiên có dữ liệu đáng tin (feed chuẩn, không trong cửa sổ tin lớn khi anchor hình thành).

### Khi nào nên bỏ qua?
- [ ] Không viết ra được **origin / termination / known_at / state** của range đang dùng.
- [ ] Giá quanh EQ, hoặc range đang FORMING (p ≈ 1 liên tục — "discount" trên chart đã chạy xong là ảo giác hindsight).
- [ ] LRI thấp và không có quy tắc phân xử → location không xác định = không có location edge.
- [ ] Vừa có **sweep protected origin** mà chưa có trigger LTF theo hướng leg — base-rate continuation sau sweep chỉ ~0.24–0.28 trên dữ liệu v0.2 ([[#5.4. Sweep vs phá range thật & re-mapping|§5.4]]).
- [ ] Đang đo premium/discount trên range của timeframe không khớp narrative.

Bảng tổng hợp các tình huống *không* dùng DR (và dùng gì thay thế):

| Tình huống | Vì sao | Thay thế |
|---|---|---|
| Direction UNDEFINED ở scale đang xét | Không có protected anchor → leg DR không tồn tại | Container (mean-reversion hypothesis) hoặc đứng ngoài |
| Range FORMING | Termination chưa đóng; p ≈ 1 | Chờ |
| LRI thấp | Location phụ thuộc lựa chọn anchor | Đứng ngoài hoặc log research |
| Range nhỏ hơn stop × c1 | Location không ảnh hưởng rủi ro | Parent range |
| M_ratio quá lớn | Range quá nhỏ so với hành trình đến DOL | Parent range |
| Anchor là news spike / data artifact | Anchor không đại diện auction bình thường | Anchor body / chờ range mới |
| Price discovery (ví dụ all-time high) | Không có external liquidity phía trên để làm boundary; "premium" luôn đúng và vô nghĩa | Công cụ khác (ngoài phạm vi note này) |
| HTF đang chuyển trạng thái (location blackout) | Không có frame ACTIVE ở scale quyết định | Chờ range mới ACTIVE |
| Range stale (temporal/context invalidation) | Tọa độ không còn phản ánh định giá hiện tại | Range mới |

### 2.3. Khác biệt theo điều kiện thị trường

> [!warning] Mức bằng chứng của mục 2.3
> Các nhận định theo loại thị trường dưới đây là **kinh nghiệm thực hành [INTERPRETATION]**, chưa có dataset trong vault kiểm chứng. Hai điểm có cơ sở hơn: (1) futures có displayed order book còn FX spot thì không; (2) CFD có thể thiếu dữ liệu ngoài giờ so với futures gốc — kiểm tra được bằng cách đối chiếu hai feed ([[#16.1. Nhóm A — Anchor, dữ liệu và feed|§16.1]]).

#### 2.3.1 Điều kiện làm concept mạnh lên / yếu đi

- **Regime trending vs ranging:** trong ranging, Dealing Range hoạt động gần như lý tưởng — giá tôn trọng cả hai đầu nhiều lần, EQ là trục dao động rõ. Trong trending mạnh, range "trượt" liên tục theo hướng trend (xem §4.1 và W3 ở §16.2); range cũ nhanh chóng lỗi thời và "discount" của range cũ trở thành bẫy bắt dao rơi.
- **Volatility cao/thấp:** volatility cao (quanh CPI/FOMC, mở phiên NY) làm swing hình thành nhanh nhưng cũng dễ bị false break — cần chờ acceptance rõ hơn là chỉ wick. Volatility thấp (Á lồng, thứ Sáu chiều) làm range hẹp bất thường, phép đo % trở nên nhiễu vì độ rộng range nhỏ hơn spread/nhiễu bình thường của thị trường.
- **Session:** range hình thành trong London/NY overlap (FX) hoặc RTH (futures) đáng tin hơn nhiều so với range hình thành trong phiên Á mỏng thanh khoản hoặc phiên ETH overnight của futures.
- **Loại tài sản:** FX majors có thanh khoản sâu và ổn định nhất → range bền, EQ đáng tin cao. Index futures có range rõ trong RTH nhưng dễ nhiễu ở phần ETH (overnight) nếu dùng feed CFD thiếu dữ liệu. Crypto giao dịch 24/7 không có "phiên đóng cửa" rõ ràng để chốt một range chính thức, khiến range dễ bị coi là "chưa hoàn thành" liên tục và funding time tạo các nhịp expansion giả định kỳ.

#### 2.3.2 Bảng so sánh ba loại thị trường

| Tiêu chí | FX majors (EURUSD, GBPUSD) | Index Futures (NQ/ES) | Crypto (BTC/ETH) |
|---|---|---|---|
| **Độ ổn định EQ** | Cao — ít bị "trôi" trong phiên, đáng tin để đặt limit trước | Trung bình — EQ RTH ổn định, nhưng gap qua đêm làm EQ D1 nhảy | Thấp hơn — không có giờ đóng cửa chính thức, range D1 phụ thuộc mốc UTC 00:00 quy ước |
| **Chênh lệch feed giữa broker** | Nhỏ (vài pip) nếu dùng broker uy tín, liquidity provider tốt | Lớn nếu so CFD vs futures CME thật (thiếu range overnight) | Rất lớn — Binance, Coinbase, Bybit có thể lệch range hàng trăm USD trên BTC quanh sự kiện thanh lý |
| **Tần suất re-map cần thiết** | Thấp, vài phiên một lần với range H4/D1 | Trung bình, theo phiên RTH/ETH và ngày đáo hạn hợp đồng | Cao — funding 3 lần/ngày và đòn bẩy cao tạo expansion/liquidation cascade thường xuyên |
| **Rủi ro chọn sai range** | Vẫn tồn tại (anchor ambiguity) nhưng ít bị khuếch đại bởi vấn đề feed | Cao nếu dùng CFD thay vì futures gốc để vẽ range | Cao nhất — không có "nguồn sự thật" duy nhất như CME cho futures |
| **Khi nào range đáng tin nhất** | London/NY overlap, tránh tuần lễ mỏng (Giáng sinh, Tết Mỹ) | RTH (9:30-16:00 ET), tránh tuần đáo hạn hợp đồng (rollover) | Sau các đợt liquidation lớn đã hấp thụ xong, tránh đúng giờ funding |

---

## 3. Cấu trúc nhận diện trên chart

> [!note] Cách đọc mục 3
> Phần "dùng nhanh" (Dấu hiệu chính → Điều kiện làm setup yếu đi) tóm tắt quy trình. Các tiểu mục 3.1–3.6 là nền tảng đầy đủ theo đúng thứ tự logic: **structure → phân loại swing → chọn swing có ý nghĩa → chọn anchor → dựng range → external/internal**. Swing được xác định *trước* range — làm ngược lại là lập luận vòng tròn ([[#14.7. Market Structure Relationship|§14.7]]).

### Dấu hiệu chính
1. **Một structural break đã xảy ra ở scale k:** close (không phải wick) vượt một swing đối diện cùng cấp → có BOS/MSS.
2. **Origin của leg phá xác định được:** cực trị của nhịp hồi trước break — đó là *protected swing*, điểm invalidation.
3. **Termination đã đóng:** sau cực trị mới, giá hồi tối thiểu θ·ATR (HEURISTIC, mặc định θ = 2) → range chuyển FORMING → ACTIVE. Trước đó không đo location.
4. **Mỗi anchor có `known_at`:** thời điểm sớm nhất mà vai trò của nó biết được không cần dữ liệu tương lai.
5. **Giá đang ở bên trong range** và range chưa bị thay bởi event mới (EXTENDED / REVERSED / INVALIDATED).
6. **Scale khớp với quyết định:** D1 range cho context, H1 range cho setup, M5 chỉ cho execution.

### Ma trận nhận diện

| Thành phần | Bullish leg DR | Bearish leg DR | Cảnh báo / chọn sai |
|---|---|---|---|
| **Origin (protected)** | Swing low nơi leg phá swing high xuất phát | Swing high nơi leg phá swing low xuất phát | Chọn đáy/đỉnh "sâu nhất trên màn hình" thay vì origin của leg phá gần nhất (CX-04) |
| **Termination** | Cực trị cao nhất sau break, đã đóng bằng nhịp hồi ≥ θ·ATR | Cực trị thấp nhất sau break, đã đóng | Dùng termination chưa đóng → p ≈ 1 bị đọc thành "discount" (CX-03) |
| **Tạo bởi** | Break bằng close + (lý tưởng) displacement | Như bên trái | Wick-break, nến tin, micro swing |
| **Sweep tại origin** | Bằng chứng hỗ trợ (EC-11), không bắt buộc | Như bên trái | Coi "chưa sweep" là range không hợp lệ — sai về định nghĩa |
| **Location hiện tại** | Discount = nửa phía origin | Premium = nửa phía origin | Đo trên range FORMING hoặc range sai scale |
| **Internal liquidity** | Bullish FVG/OB ở discount còn unmitigated | Bearish FVG/OB ở premium | POI nằm giữa "đất trống" xa mọi PD array |
| **Liveness** | Origin chưa bị close xuyên, chưa có MSS ngược cùng scale | Như bên trái | Giữ range sau khi đã REVERSED |

### Điều kiện bắt buộc
- [ ] Ghi được **origin, termination, scale (θ\*), known_at, state** của range — với giá cụ thể.
- [ ] Origin có **structural consequence**: từ nó giá đã phá một swing đối diện cùng cấp bằng close.
- [ ] Range ở state **ACTIVE**.
- [ ] Range thuộc **scale khớp** narrative/quyết định đang xét.
- [ ] Đã đánh dấu EQ và biết giá ở nửa nào; đã xác định external liquidity hai phía và DOL ứng viên.

### Điều kiện tăng xác suất
*Tất cả là [HYPOTHESIS] — chưa điều kiện nào được validate trên dữ liệu (§20.1). Dùng như filter có ghi journal, không như edge.*
- [ ] Leg phá có **displacement** rõ (D-score cao; HYP-DR-006).
- [ ] Origin đã **sweep liquidity** phía sau khi hình thành (HYP-DR-007).
- [ ] **Nested-consistent:** location của child và parent cùng phía (HYP-DR-004 — proxy v0.2 *không* ủng hộ; §19.3).
- [ ] **LRI cao:** các candidate range hợp lệ đồng thuận về location (HYP-DR-011).
- [ ] POI ở discount nằm tại một PD array cụ thể, không ở giữa range rộng (W3 — [[#16.2. Nhóm B — Kích thước range, regime và lịch|§16.2]]).

### Điều kiện làm setup yếu đi
- Anchor là news spike, data artifact, hoặc chỉ là micro swing chọn vì gần giá.
- Range FORMING, CONSOLIDATING, hoặc đã stale (tuổi lớn, không tương tác).
- **Origin vừa bị sweep** mà chưa có trigger theo hướng leg (base-rate thấp — §5.4).
- Range quá hẹp so với stop, hoặc quá rộng so với ADR (location thô).
- Child location mâu thuẫn parent location và DOL gần (CX-12).
- Cấu trúc HTF đang chuyển trạng thái (location blackout).

### 3.1. Market Structure Foundation

Không thể chọn anchor đúng nếu chưa định nghĩa swing và structure chính xác. Section này đặt nền móng.

#### 3.1.1 Ba cách định nghĩa swing — và cái giá của mỗi cách

**(a) Fractal / Pivot n-bar.** Bar j là swing high nếu `High[j] > High[j±k]` với mọi k = 1..n.

- Ưu: đơn giản, khách quan.
- Nhược: **confirmation lag = n bar** — swing high tại bar j chỉ được biết tại close của bar j+n. Không phân biệt scale: một fractal nhỏ và một fractal lớn được coi như nhau.
- **[MATHEMATICAL — đã mô phỏng]** Trong random walk Gaussian, xác suất một bar là fractal high với n bar mỗi bên = (C(2n,n)/4ⁿ)². Với n = 2 (5-bar fractal): 0.1406 → **~35 swing highs trên 250 bar**. Với n = 3: ~24. Với n = 5: ~15. Mô phỏng 2 triệu bước khớp lý thuyết đến chữ số thứ tư. **Hàm ý:** một năm D1 của một chuỗi *hoàn toàn ngẫu nhiên* đã có hàng chục swing highs và lows. Bạn không bao giờ thiếu swing — bạn chỉ thiếu *tiêu chí*.

**(b) ZigZag / Directional Change (DC) với threshold θ.** Một swing high được xác nhận khi giá giảm ít nhất θ từ cực trị gần nhất (θ đo bằng % hoặc bội số ATR). Glattfelder, Dupuis & Olsen (2011) dùng cách "cắt" chuỗi giá theo directional-change events với nhiều threshold khác nhau để nghiên cứu cấu trúc đa scale của FX.

- Ưu: **scale-selective** — θ lớn chỉ giữ swing lớn. Đây là cách tự nhiên nhất để định nghĩa hierarchy.
- Nhược: lag thay đổi (phải đợi giá hồi θ); nhạy với θ.
- **[MATHEMATICAL — đã mô phỏng]** Glattfelder et al. báo cáo trong dữ liệu FX, overshoot trung bình sau một directional change xấp xỉ bằng chính θ. Mô phỏng random walk trong nghiên cứu này cho overshoot trung bình ≈ 1.04θ — tức **random walk cũng tạo ra "scaling law" này**. Bài học: nhiều "pattern" trong giá có một giải thích null (ngẫu nhiên) cần loại trừ trước khi kết luận về cấu trúc.

**(c) Structure-based swing.** Swing low = lowest low giữa hai lần break of structure liên tiếp trong cùng hướng. Đây là cách gần với cách trader ICT "đọc" chart nhất.

- Ưu: gắn trực tiếp với structural consequence.
- Nhược: phụ thuộc định nghĩa "break"; có thể đệ quy (cần swing để định nghĩa break, cần break để định nghĩa swing) — giải quyết bằng cách dùng (a) hoặc (b) làm tầng phát hiện, (c) làm tầng phân loại.

**Khuyến nghị cho framework:** tầng phát hiện = (b) ZigZag/DC theo ATR; tầng phân loại = (c) structural consequence; (a) dùng làm baseline.

#### 3.1.2 HH / HL / LH / LL — phải so cùng cấp

- **HH (Higher High):** swing high cao hơn swing high *trước đó cùng cấp*.
- **HL (Higher Low):** swing low cao hơn swing low trước đó cùng cấp.
- **LH, LL:** đối xứng.

**Lỗi category:** so một micro high trên M5 với một major high trên D1 rồi gọi là "LH". Structure chỉ có nghĩa khi so **cùng scale**. Một chuỗi HH–HL trên H1 có thể hoàn toàn nằm bên trong một LH–LL trên D1.

#### 3.1.3 Break: wick hay close?

Phải chọn trước và giữ cố định:

| Rule | Định nghĩa | Hệ quả |
|---|---|---|
| Wick break | High vượt level | Nhiều false break; nhầm sweep thành break |
| Close break | Close vượt level | Chuẩn phổ biến; vẫn bị ảnh hưởng bởi 1 close yếu |
| Close + displacement | Close vượt level bằng một candle có body/ATR ≥ X | Ít tín hiệu, chất lượng cao hơn (giả thuyết) |
| Close + acceptance | k close liên tiếp vượt level hoặc retest giữ | Chậm, ít false break |

[BACKTEST REQUIRED] — mỗi rule là một biến thể cần test riêng; đừng trộn rule giữa các lần phân tích.

#### 3.1.4 BOS vs MSS

- **BOS (Break of Structure):** phá swing theo **hướng của structure hiện tại** (bullish: phá swing high trước đó) → continuation.
- **MSS (Market Structure Shift):** phá **swing đang bảo vệ structure hiện tại** theo hướng ngược lại (bullish structure: phá protected low) → dấu hiệu chuyển trạng thái. Trong cách dùng ICT, MSS có ý nghĩa khi đi kèm displacement và thường sau một liquidity event.
- **Phân biệt then chốt:** "phá một swing low" ≠ MSS. Phá một *internal* low trong bullish structure chỉ là một internal event. MSS thật sự là phá swing low **có cấp độ tương đương với structure đang xét** — cụ thể là protected low.

#### 3.1.5 Protected swing và Target swing

**[ICT FRAMEWORK / SMC community]** Cộng đồng SMC dùng cặp khái niệm *strong/weak high/low*:

- **Protected (strong) low** trong bullish structure: swing low mà từ đó giá đã phá swing high trước → nó là origin của leg tạo BOS. Nếu bị phá (với acceptance), câu chuyện bullish ở scale đó chết.
- **Weak high:** swing high gần nhất chưa bị phá, là mục tiêu tiềm năng (external liquidity).

**Đây chính là cặp anchor tự nhiên của Leg DR:** protected low = anchor dưới (origin), high hiện tại/weak high = anchor trên (termination).

#### 3.1.6 Nguyên lý nền tảng

> **Structure được định nghĩa bởi các sự kiện break, không phải bởi hình dạng swing.** Một swing chỉ trở nên có ý nghĩa cấu trúc khi một sự kiện break xảy ra *liên quan đến nó* — hoặc từ nó (origin của BOS), hoặc qua nó (bị phá), hoặc gần nó (bị sweep).

Hệ quả: ý nghĩa của swing **luôn được xác nhận muộn**. Một swing low mới hình thành chỉ là *candidate*; nó trở thành *protected* tại thời điểm giá từ nó phá swing high trước đó. Thời điểm đó chính là `known_at` của vai trò protected.

#### 3.1.7 Internal vs External structure

- **External structure (ở scale k):** các swing là boundary của range đang hoạt động ở scale k.
- **Internal structure:** các swing nằm *bên trong* range đó.

Đây là khái niệm **quan hệ**. Cùng một swing high có thể là external đối với H1 leg range và là internal đối với D1 container range.

### 3.2. Swing Classification

#### 3.2.1 Hierarchy 5 cấp — phiên bản vận hành

Đây là **research framework**, không phải luật ICT. Các threshold là HEURISTIC, đo bằng bội số ATR(14) của chính timeframe đang xét.

| Level | Tên | Tiêu chí vận hành (đề xuất) | Vai trò điển hình | Liquidity |
|---|---|---|---|---|
| L1 | Micro swing | Fractal n ≤ 2, không tồn tại ở ZigZag θ₁ ≈ 1×ATR | Noise, trigger M5 | Rất nhỏ, thường bị lấy trong vài bar |
| L2 | Internal swing | Tồn tại ở θ₁ nhưng không ở θ₂ ≈ 2×ATR; nằm trong DR đang hoạt động | Nhịp hồi nội bộ, internal BOS | Internal liquidity |
| L3 | Intermediate structural | Tồn tại ở θ₂; là origin của ít nhất một BOS cùng cấp | Tạo setup, H1 structure | Pool trung bình |
| L4 | External / DR swing | Là boundary của DR đang hoạt động ở TF (protected hoặc termination) | Anchor | External liquidity của range |
| L5 | Major HTF swing | Là L4 trên TF cha (D1/W1) hoặc tồn tại ở θ₃ ≈ 4–5×ATR | Anchor HTF, DOL lớn | HTF external liquidity |

#### 3.2.2 Phê phán hierarchy 5 cấp

Hierarchy này **hữu ích nhưng lẫn lộn hai trục**:

- **L1, L2, L3, L5** mô tả **scale** — kích thước/độ bền của swing.
- **L4** mô tả **role** — swing đang *đóng vai* boundary của một range.

Một swing L3 có thể đồng thời là L4 (nếu nó đang là protected low của H1 leg). Một swing L5 có thể không phải L4 của range đang dùng. Trộn hai trục dẫn tới câu hỏi vô nghĩa kiểu "swing này là L3 hay L4?".

#### 3.2.3 Đề xuất cải tiến: phân loại hai trục

**Trục 1 — Scale (liên tục): persistence θ\***

> θ\*(swing) = threshold ZigZag lớn nhất (tính theo ATR của TF) mà swing đó vẫn còn là turning point.

Ý tưởng giống "persistence" trong topological data analysis: swing lớn sống sót khi ta "làm mờ" chart bằng threshold lớn dần; swing nhỏ biến mất sớm. θ\* là **một con số liên tục, khách quan**. Các "level" chỉ là cách chia bin θ\* (ví dụ θ\*<1 ATR = micro; 1–2 = internal; 2–4 = intermediate; >4 = major). sơ đồ v01-05 minh họa.

**Trục 2 — Role (rời rạc, thay đổi theo thời gian):**

| Role | Định nghĩa |
|---|---|
| CANDIDATE | Swing đã xác nhận (qua lag) nhưng chưa có hệ quả |
| PROTECTED | Origin của BOS gần nhất ở scale của nó, chưa bị phá |
| TARGET / WEAK | Extreme chưa bị phá đối diện protected; external liquidity tiềm năng |
| INTERNAL | Nằm trong DR đang dùng, không phải boundary |
| SWEPT | Đã bị vượt bởi wick/close nhưng không có acceptance |
| SPENT / BROKEN | Đã bị phá có acceptance; liquidity đã dùng; chỉ còn là reference (old high/low) |

![[Dealing-Range-v01-04-Hai-Truc-Swing.svg|760]]
*Sơ đồ: phân loại swing hai trục — θ* (scale) × role(t), với các swing ví dụ ở 3.2.5.*

**Trục 3 (tùy chọn) — Consequence record:** danh sách sự kiện gắn với swing (BOS originated, sweep performed, displacement launched, FVG created).

Như vậy mỗi swing có dạng: `swing = {price, time, known_at, θ*, role(t), consequences[]}`.

#### 3.2.4 Promotion và demotion

- **Promotion:** một swing L2 có thể được "thăng cấp" khi từ nó giá tạo ra một BOS lớn hơn dự kiến (θ\* được tính lại khi có thêm dữ liệu — lưu ý: θ\* của một swing *có thể tăng* theo thời gian vì giá đi xa hơn khỏi nó). Hệ quả: **θ\* cũng có known_at** — giá trị θ\* tại thời điểm t chỉ dùng dữ liệu đến t.
- **Demotion:** swing bị phá có acceptance → role chuyển sang SPENT. Swing bị sweep → SWEPT (liquidity đã bị lấy, vai trò anchor có thể vẫn giữ tùy rule).

#### 3.2.5 Ví dụ phân loại

```text
Uptrend H1, ATR(14) = 20 pips

Swing   Price    θ*(ATR)   Consequence                         Role (hiện tại)
A (L)   1.0800   ≥5        Origin của MSS bullish trên H1       PROTECTED (H1 trend scale)
B (H)   1.0880   2.0       Bị phá bởi leg C→D                   SPENT
C (L)   1.0840   2.0       Origin của BOS phá B                 (vai trò protected đã chuyển sang E)
D (H)   1.0920   2.25      Bị phá bởi leg E→F                   SPENT
E (L)   1.0875   2.25      Origin của BOS phá D                 PROTECTED (H1 leg scale)
x (L)   1.0902   0.4       Không                                INTERNAL (micro)
F (H)   1.0960   ≥1.8*     Chưa có                              TARGET (termination)

θ* ở đây xấp xỉ bằng min(biên độ leg đi vào swing, biên độ leg rời khỏi swing) / ATR.
* θ*(F) chưa hoàn tất vì giá chưa đi xa khỏi F — giá trị sẽ tăng nếu giá tiếp tục giảm.
Ở θ = 3×ATR, ZigZag bỏ qua B, C, D, E và chỉ còn A → F: "trend range" A–F xuất hiện
một cách khách quan ở scale lớn hơn.
```

Swing x (1.0902) trông như một HL rõ ràng trên M5 nhưng θ\* = 0.4 ATR của H1 → nó là micro swing đối với H1 và **không** được dùng làm anchor của H1 DR.

### 3.3. How to Select Meaningful Swings

#### 3.3.1 Câu hỏi trước câu hỏi: "significance" dự báo điều gì?

Đây là điểm mà hầu hết framework bỏ qua. "Swing quan trọng" là một khái niệm **không có nghĩa** cho đến khi ta chỉ ra nó quan trọng *đối với cái gì*. Ba lựa chọn target, mỗi cái cho ra một định nghĩa khác:

| Target (biến phụ thuộc) | Câu hỏi | Ví dụ đo lường |
|---|---|---|
| **Protection** | Swing có giữ được (không bị phá) trong k bar tới không? | P(not violated within k bars) |
| **Reaction** | Khi giá quay lại test, có phản ứng không? | P(reversal ≥ x·ATR within m bars \| touch) |
| **Anchor utility** | Dùng swing làm anchor DR có cải thiện expectancy của hệ thống không? | ΔE[R] giữa hai cách chọn anchor |

Một swing có thể rất tốt về *protection* (xa giá, khó bị chạm) nhưng vô dụng về *reaction*. Khi bạn xây scoring model, phải chọn target trước, nếu không bạn sẽ tối ưu hóa một thứ không xác định — và rất dễ overfit.

#### 3.3.2 Sáu thành phần — biến đo lường cụ thể

**S — Structural Significance**

| Biến | Định nghĩa | Loại |
|---|---|---|
| `bos_origin` | Từ swing này, giá đã phá swing đối diện cùng scale chưa? | Binary |
| `mss_origin` | BOS đó có phải là MSS (phá protected swing của structure ngược lại)? | Binary |
| `n_bos_from` | Số BOS liên tiếp phát sinh từ leg bắt đầu tại swing | Integer |
| `is_protected` | Hiện đang là protected swing ở scale k? | Binary (theo t) |
| `broke_level` | Level (θ\*) của swing bị phá bởi leg từ swing này | Continuous |

**L — Liquidity Significance**

| Biến | Định nghĩa |
|---|---|
| `sweep_prior` | Swing này có vượt qua một swing cùng phía trước đó rồi đảo chiều không (tức nó *là* một sweep)? |
| `sweep_depth_atr` | Khoảng vượt qua swing trước / ATR |
| `swept_level` | θ\* của swing bị sweep |
| `eq_cluster` | Số swing cùng phía trong phạm vi ε·ATR (equal highs/lows) |
| `untested_bars` | Số bar kể từ khi hình thành mà chưa bị chạm lại |
| `htf_visibility` | Swing có trùng với PDH/PDL, PWH/PWL, số tròn? |

**D — Displacement Significance**

| Biến | Định nghĩa |
|---|---|
| `max_body_atr` | Max(body/ATR) của các candle trong k bar đầu tiên rời khỏi swing |
| `leg_speed` | Biên độ leg / (số bar × ATR) |
| `fvg_count`, `fvg_size_atr` | Số lượng và kích thước FVG được tạo trong leg |
| `close_strength` | Vị trí close trong range của candle displacement |

**R — Reaction Significance**

| Biến | Định nghĩa |
|---|---|
| `reaction_amp_atr` | Biên độ leg phản ứng từ swing / ATR |
| `reaction_bars` | Số bar để đạt biên độ đó (tốc độ) |
| `follow_through` | Leg phản ứng có tạo BOS không? |

**T — Timeframe Significance**

| Biến | Định nghĩa |
|---|---|
| `theta_star` | Persistence (mục 3.2.3) |
| `parent_pivot` | Swing có là pivot trên timeframe cha không? |
| `lifetime_bars` | Tuổi đời swing (bar) tính đến t |

**P — Persistence**

| Biến | Định nghĩa |
|---|---|
| `alive` | Chưa bị phá có acceptance |
| `n_tests_held` | Số lần bị test mà giữ được |
| `age_vs_scale` | Tuổi / thời gian điển hình của leg ở scale này |

#### 3.3.3 Bốn scoring model đề xuất — tất cả là [HYPOTHESIS]

**M1 — Additive weighted score**

$$\text{Score} = w_S z_S + w_L z_L + w_D z_D + w_R z_R + w_T z_T + w_P z_P$$

với z là feature đã chuẩn hóa (z-score hoặc percentile rank).

- Ưu: linh hoạt.
- Nhược: **trọng số tùy tiện**; các thành phần tương quan mạnh (D và R thường đi cùng nhau; T và R cũng vậy vì swing lớn thì reaction lớn) → double-counting. Nhiều tham số → rủi ro overfit cao nhất.

**M2 — Gated / lexicographic (khuyến nghị bắt đầu)**

```text
GATE 1 (bắt buộc):  bos_origin == TRUE  (swing có structural consequence)
GATE 2 (bắt buộc):  alive == TRUE
GATE 3 (scale):     theta_star >= theta_min(TF)
RANK:               theta_star  → tie-break: sweep_prior → max_body_atr
```

- Ưu: ít tham số, dễ giải thích, bám sát logic cấu trúc, khó overfit.
- Nhược: bỏ qua sắc thái; ranh giới cứng.

**M3 — Persistence-only (baseline đơn giản nhất)**

`Score = theta_star`. Một tham số duy nhất. **Mọi model phức tạp hơn phải đánh bại M3 out-of-sample** mới đáng giữ.

**M4 — Learned model (logistic regression / gradient boosting)**

Target: một trong ba target ở 9.1. Features: toàn bộ biến ở 9.2.

- Nguy cơ: **target leakage** (ví dụ `reaction_amp_atr` được tính bằng dữ liệu sau thời điểm quyết định), overfitting, khó giải thích. Chỉ dùng với walk-forward nghiêm ngặt và feature có known_at rõ ràng.

#### 3.3.4 Cái bẫy của R (Reaction Significance)

Reaction là thành phần **nguy hiểm nhất** về hindsight: reaction của một swing chỉ được biết sau khi reaction xảy ra. Nếu bạn dùng "swing này có reaction mạnh" để chọn nó làm anchor, bạn phải chắc rằng reaction đó **đã hoàn tất trước thời điểm quyết định**. Trong nhiều trường hợp — đặc biệt với termination anchor (swing high hiện tại) — reaction đang diễn ra, và giá trị của R đang thay đổi. Quy tắc: **R chỉ được dùng cho anchor đã "đóng" (confirmed + reaction measured up to t)**.

#### 3.3.5 Kết luận của section

Swing có ý nghĩa, trong framework này, là swing **(1) sống sót ở scale đủ lớn (θ\*), (2) có hệ quả cấu trúc (origin của BOS/MSS hoặc là một sweep có consequence), (3) vẫn còn sống, (4) có vai trò trong range đang dùng**. Mọi thành phần khác (displacement, reaction, liquidity cluster) là **supporting evidence** để xếp hạng, không phải điều kiện cần — cho đến khi backtest chứng minh ngược lại.

### 3.4. Anchor Selection

#### 3.4.1 Đánh giá phê phán flow trong brief

Flow được đề xuất:

```text
Market Context → Identify Major Structure → Identify External Swings → Classify Swing Significance
→ Identify Structural Leg → Determine Origin → Determine Termination → Validate → Construct → Validate Range
```

**Điểm đúng:** top-down; tách origin và termination; có bước validate.

**Vấn đề 1 — Vòng tròn:** "Identify External Swings" đứng *trước* "Classify Swing Significance". Nhưng "external" chỉ có nghĩa *so với một range* — mà range chưa được xây. Và "major structure" cũng cần swing đã được phân loại. Flow ngầm giả định ta đã biết range để xác định swing, rồi dùng swing để xác định range.

**Vấn đề 2 — Thiếu bước "purpose/scale":** flow không hỏi *range này dùng để làm gì* (context hay setup) và *ở scale nào*. Không có câu trả lời, "major" là mơ hồ.

**Vấn đề 3 — Thiếu known_at:** không bước nào kiểm tra rằng anchor được xác định bằng thông tin có sẵn tại thời điểm quyết định.

**Vấn đề 4 — Chỉ một range:** flow cho ra một range. Thực tế cần *một tập candidate* và một bước chọn có kiểm tra robustness.

#### 3.4.2 Flow cải tiến (v0.1)

```text
0. PURPOSE & SCALE
   - Range dùng cho: CONTEXT (D1) | SETUP (H1)
   - Chọn theta_min theo TF (HEURISTIC: D1 ≈ 2×ATR_D1, H1 ≈ 2×ATR_H1)

1. DETECT SWINGS (range-independent)
   - ZigZag/DC theo ATR; ghi price, time, known_at

2. MEASURE SCALE
   - Tính theta*(t) cho mỗi swing (chỉ dữ liệu đến t)

3. DERIVE STRUCTURAL STATE ở scale đã chọn
   - Chuỗi BOS/MSS; xác định direction hiện tại (BULL/BEAR/UNDEFINED)

4. FIND LAST VALID STRUCTURAL BREAK ở scale đó
   - Break theo rule đã cố định (close / close+displacement)

5. ANCHORS (Leg DR)
   - Origin  = extreme của leg tạo ra break đó (bull: lowest low trước break) → PROTECTED
   - Termination = extreme đạt được sau break đến t (bull: highest high) → TARGET
   - Termination chỉ "đóng" khi giá hồi ≥ theta_min từ nó

6. ALTERNATIVE CANDIDATES
   - Container DR: swing high/low chưa bị phá gần nhất có theta* ≥ theta_min bao quanh giá
   - Lookback DR: HH/LL 20/40/60 bar
   - Leg DR ở scale lớn hơn một bậc

7. VALIDATE
   - W/ATR trong dải hợp lý; origin có consequence; state không INVALIDATED

8. LOCATION ROBUSTNESS
   - Tính p trên mọi candidate hợp lệ; LRI = tỷ lệ đồng thuận nhãn premium/discount

9. SELECT + RECORD
   - Primary range theo rule hierarchy (mục 4.2); lưu known_at, candidate set, LRI
```

#### 3.4.3 Trả lời trực tiếp: "Swing Low nào và Swing High nào?"

**Trong bối cảnh bullish, ở scale k:**

- **Swing Low anchor = lowest low của leg đã tạo ra BOS hợp lệ gần nhất ở scale k.** Swing low này đồng thời là (a) origin của leg, (b) protected low, (c) điểm invalidation của câu chuyện bullish ở scale k. Ba vai trò trùng nhau không phải ngẫu nhiên — đó là lý do nó là anchor "đúng": nó là mức giá mà nếu bị phá, *ý nghĩa* của range biến mất.
- **Swing High anchor = highest high đạt được sau BOS đó cho đến t.** Nó là termination (động — sẽ di chuyển nếu giá tiếp tục tăng) và là external liquidity phía trên (weak high).

**Trong bối cảnh bearish:** đối xứng — High anchor = highest high của leg tạo ra bearish BOS gần nhất (protected high); Low anchor = lowest low sau BOS.

**Trong consolidation (direction = UNDEFINED):** không có Leg DR hợp lệ. Dùng Container DR: swing high và swing low chưa bị phá gần nhất ở scale k, cả hai đều là external liquidity. Không có "protected" anchor → không có location-for-continuation; chỉ có location-for-mean-reversion (một hypothesis khác hẳn).

#### 3.4.4 Wick hay Body?

| Anchor | Lý do ủng hộ | Lý do phản đối |
|---|---|---|
| **Wick (extreme)** | Là giá thực sự đã giao dịch; nơi stops bị kích hoạt; nhất quán với định nghĩa liquidity | Nhạy với spike, spread widening, bad tick |
| **Body (open/close)** | Ổn định hơn; phản ánh "acceptance" | Không phải nơi liquidity nằm; mâu thuẫn với khái niệm sweep |

Mặc định trong framework: **wick** (nhất quán với ICT và với khái niệm liquidity). [BACKTEST REQUIRED] So sánh hai biến thể; nếu kết quả rất nhạy với lựa chọn này, đó là dấu hiệu phương pháp không robust.

#### 3.4.5 Thời điểm "range có thể dùng được"

Một Leg DR chỉ **usable** khi:

1. Origin đã được xác nhận là protected (BOS đã xảy ra) — `known_at_origin = thời điểm BOS`.
2. Termination đã "đóng" — giá đã hồi ≥ θ_min từ extreme — `known_at_term = thời điểm hồi đủ θ`.

Trước (2), range ở trạng thái **FORMING**: termination còn đang chạy, EQ còn đang di chuyển lên theo giá. Mọi phép đo "premium/discount" trong trạng thái FORMING là **không ổn định** — và trên thực tế, khi giá đang tạo high mới, nó luôn ở gần 100% (premium tối đa) của range đang hình thành. Đây là lý do mô hình "đợi retracement vào discount" tự nhiên đòi hỏi termination phải đóng trước.

#### 3.4.6 Minh họa: cùng một leg, hai giao thức anchor

![[Dealing-Range-EdgeB-DualAnchorOTE.svg|1516]]
*Sơ đồ (minh họa): cùng một leg NQ H1 — anchor wick-high 20,412 vs body-high 20,381 cho hai vùng OTE lệch nhau ~53 điểm ở mức 62%.*

Cả hai anchor đều hợp lệ; không cái nào "sai". Hệ quả đúng không phải "chọn cái đẹp hơn" mà là: **cố định một giao thức anchor trước**, ghi nó vào playbook, và để backtest so sánh hai giao thức như hai arm. Nếu kết quả nhạy mạnh với lựa chọn này, edge (nếu có) không robust (CX-06). Case lưu trữ tương ứng: [[#Case 5 (Minh họa — giao thức anchor wick vs body) — NQ, phiên NY AM|Case 5]].

### 3.5. Constructing the Dealing Range

#### 3.5.1 Ba thuật toán cho ba họ range

**(1) Leg DR (impulse range)**

```text
input: swings ở scale k (đã có known_at), break_rule
state = direction hiện tại ở scale k
if state == BULL:
    brk  = BOS bullish gần nhất (phá swing high cấp k)
    L*   = min(Low) từ swing low cấp k cuối cùng trước brk  → origin/protected
    H*   = max(High) từ brk đến t                          → termination
    status = FORMING nếu chưa có hồi ≥ theta_min từ H*, ngược lại ACTIVE
if state == BEAR: đối xứng
if state == UNDEFINED: không có Leg DR
```

**(2) Container DR (external range)**

```text
H* = swing high cấp ≥ k gần nhất, còn sống (chưa bị phá có acceptance), nằm trên giá
L* = swing low  cấp ≥ k gần nhất, còn sống, nằm dưới giá
direction = NEUTRAL (container không tự mang hướng)
```

**(3) Lookback DR (IPDA-style)**

```text
H* = max(High[t-N .. t-1]), L* = min(Low[t-N .. t-1]),  N ∈ {20, 40, 60} trên D1
Hoàn toàn khách quan, không cần swing detection → baseline lý tưởng.
```

Lưu ý: ở (3) cửa sổ dùng `t-1` để tránh bar hiện tại tự định nghĩa boundary của chính nó.

#### 3.5.2 Dealing Range in an Uptrend — phân tích A–F

Chuỗi giả định (D1, đơn vị điểm; ATR_D1 = 2.5; θ_min = 2×ATR = 5 điểm):

![[Dealing-Range-v01-06-Uptrend-A-F.svg|760]]
*Sơ đồ: sáu candidate range trong uptrend A–F; chỉ leg DR E–F và trend DR A–F đang có thẩm quyền.*

Mỗi high cao hơn high trước (HH), mỗi low cao hơn low trước (HL). Các nhịp hồi: B→C = 5 (2.0 ATR), D→E = 6 (2.4 ATR) — cả hai đạt θ_min.

**Sáu candidate range và trạng thái của chúng tại thời điểm t (sau khi F đã được xác nhận và giá hồi về 116):**

| Range | Anchors | Trạng thái tại t | Vì sao |
|---|---|---|---|
| A–B | 100 → 110 | **Historical (COMPLETED/EXTENDED)** | B đã bị phá bởi leg C→D; A–B không còn là range đang chi phối. B = "old high", nay nằm *dưới* protected low E |
| C–D | 105 → 118 | **Historical** | D đã bị phá bởi leg E→F. D = 118 nay là "old high" nằm *bên trong* E–F, tại p = 0.46 — gần EQ của E–F |
| E–F | 112 → 125 | **ACTIVE — Leg DR ở scale k** | E là origin của BOS phá D (protected low); F là termination đã đóng |
| A–D | 100 → 118 | **Obsolete container** | Là container trước khi F phá D; nay top đã bị vượt |
| C–F | 105 → 125 | **Fallback leg DR** | Chỉ trở thành leg DR chính nếu E *không* đạt θ_min (nhịp D→E quá nông ở scale k) |
| A–F | 100 → 125 | **ACTIVE — Trend DR (scale k+1)** | Ở θ = 3×ATR, ZigZag chỉ còn A → F; A là origin của toàn bộ trend |

**Range nào meaningful?** Câu trả lời không phải "một range", mà là **một cặp có phân cấp**:

- **E–F**: leg DR — trả lời "pullback hiện tại sâu đến đâu so với impulse gần nhất?"
- **A–F**: trend DR — trả lời "toàn bộ xu hướng đã kéo dài bao xa; giá đang cao hay thấp so với nó?"
- A–B, C–D, A–D là **historical** — chúng không cung cấp tọa độ nữa, nhưng các mức của chúng (B = 110, D = 118) trở thành **reference levels** (old highs) bên trong range đang hoạt động.

**Location tại các mức giá khác nhau:**

| Giá | p(E–F) | p(C–F) | p(A–F) | Đồng thuận? | Diễn giải |
|---|---|---|---|---|---|
| 120 | 0.62 (P) | 0.75 (P) | 0.80 (P) | Có — premium | Không phải location mua trong bất kỳ frame nào |
| 116 | 0.31 (D, OTE) | 0.55 (P) | 0.64 (P) | **Không** | Discount của leg, premium của trend: "counter-location" |
| 114 | 0.15 (D) | 0.45 (D) | 0.56 (P) | **Một phần** | Sâu trong leg; gần EQ của trend |
| 112.3 | 0.02 | 0.37 | 0.49 | Có — discount/EQ | Ngay trên protected low E — R:R tốt nhất *và* gần invalidation nhất |

**Phân tích sâu của hàng 116:** trong trend mạnh, retracement thường *không* đủ sâu để vào discount của trend range. Nếu quy tắc của bạn yêu cầu "discount trên mọi frame", bạn sẽ **loại bỏ có hệ thống những trend mạnh nhất** (retracement nông) — một dạng selection bias. Nếu quy tắc chỉ yêu cầu "discount của leg", bạn chấp nhận mua ở premium của trend. Không lựa chọn nào đúng a priori:

> **[HYPOTHESIS] HYP-DR-004:** Long entries ở discount của leg DR nhưng premium của parent DR có expectancy thấp hơn long entries ở discount của cả hai. **[BACKTEST REQUIRED]** — và lưu ý: nếu đúng, tần suất setup cũng giảm; phải so expectancy *theo thời gian* (R/tháng), không chỉ R/trade.

**Tiến hóa theo thời gian (quan trọng cho no-hindsight):**

```text
t1: B hình thành, giá đang tăng           → Leg A–B: FORMING (p luôn ≈ 1)
t2: giá hồi ≥ θ từ B                       → A–B: ACTIVE, B đóng
t3: C hình thành, chưa biết là HL          → C: CANDIDATE
t4: giá phá B                              → C: PROTECTED; Leg C–(new high): FORMING; A–B: EXTENDED
t5: D đóng (giá hồi ≥ θ)                   → C–D: ACTIVE
t6: E hình thành                           → E: CANDIDATE
t7: giá phá D                              → E: PROTECTED; C–D: EXTENDED; Leg E–(new high): FORMING
t8: F đóng                                 → E–F: ACTIVE
```

Chú ý t3 → t4: **giữa t3 và t4, E–F chưa tồn tại và C chỉ là candidate**. Ai đó nhìn chart sau t8 sẽ "thấy" C là một HL hiển nhiên — nhưng tại t3, C có thể trở thành đáy của một đợt giảm sâu hơn. Đây là hindsight bias cơ bản nhất trong DR.

#### 3.5.3 Dealing Range in a Downtrend — phân tích đối xứng

![[Dealing-Range-v01-07-Downtrend-A-F.svg|1516]]
*Sơ đồ: downtrend A–F — giá 184 nằm trong bearish OTE của E–F nhưng là discount của C–F và A–F.*

| Range | Anchors | Trạng thái | EQ |
|---|---|---|---|
| A–B | 200 → 190 | Historical | 195 |
| C–D | 195 → 182 | Historical (D bị phá bởi E→F) | 188.5 |
| E–F | 188 → 175 | **ACTIVE — Leg DR** (E = protected high) | 181.5 |
| C–F | 195 → 175 | Fallback | 185 |
| A–F | 200 → 175 | **ACTIVE — Trend DR** | 187.5 |

- **Premium của E–F:** 181.5–188. **Bearish OTE** (retracement 62–79% của leg giảm): p = 0.62–0.79 → 183.1–185.3.
- Tại giá 184: p(E–F) = 0.69 (premium, trong OTE), p(C–F) = 0.45 (discount), p(A–F) = 0.36 (discount). Xung đột đối xứng với trường hợp uptrend.
- **External liquidity:** BSL phía trên E (188) — là protected high, *và* là nơi stops của short sellers vào từ E–F có thể nằm. SSL phía dưới F (175) — DOL tiềm năng của continuation.
- **DOL:** nếu D1 bearish, DOL hợp lý là SSL dưới F hoặc swing low HTF xa hơn. Nếu giá phá E với acceptance → MSS bullish ở scale k → E–F INVALIDATED.

**Bất đối xứng thực tế (không phải ICT):** [MARKET MECHANICS — stylized fact] Trên equity indices, volatility có xu hướng tăng khi giá giảm (leverage effect / volatility feedback, được ghi nhận từ Black 1976, Christie 1982). Hệ quả: downtrend leg thường nhanh hơn, ATR giãn ra, và cùng một threshold θ tính bằng ATR cố định có thể cho số swing khác nhau giữa hai chiều. **Không được giả định rằng một rule set đối xứng sẽ hành xử đối xứng.** [BACKTEST REQUIRED] — tách kết quả theo chiều long/short.

### 3.6. External vs Internal Dealing Range

#### 3.6.1 Định nghĩa

- **External DR (ở scale k):** range có boundaries là các swing *external* ở scale k — tức là Container DR, hoặc Leg DR có anchors cấp ≥ k. Boundaries của nó là **external range liquidity**.
- **Internal DR:** một sub-range nằm *bên trong* external DR, được tạo bởi internal swings (thường là leg của nhịp hồi hoặc một mini-impulse bên trong).
- **HTF range:** external DR trên D1 hoặc W1 (đối với framework của bạn: D1 là HTF).
- **Noise range:** range mà anchors không đạt θ_min, không có structural consequence, hoặc có W nhỏ hơn stop distance của trade dự kiến.

#### 3.6.2 Quan hệ quan trọng

> **Boundaries của internal DR chính là internal liquidity của external DR.**

Ví dụ: trong D1 bullish leg 100 → 125, một H1 pullback tạo range nội bộ 121 → 116. High 121 và low 116 là *internal* đối với D1 range. Khi giá phá 116 trên H1, đó là một **internal event** đối với D1 — nó không thay đổi D1 structure (protected low vẫn là 112).

#### 3.6.3 Tiêu chí phân biệt noise range — "decision-horizon consistency"

Một range là **noise đối với một quyết định** nếu tuổi thọ kỳ vọng hoặc kích thước của nó nhỏ hơn horizon của quyết định:

```text
Điều kiện 1 (size):     W_range  ≥  c1 × stop_distance     (HEURISTIC: c1 ≈ 3)
Điều kiện 2 (target):   W_range  ≥  c2 × distance_to_target? — không bắt buộc, xem mục 14.6
Điều kiện 3 (lifetime): expected_lifetime(range) ≥ expected_holding_time(trade)
```

Trực giác: nếu stop của bạn lớn hơn một phần ba range, thì stop nằm *ngoài* ý nghĩa của range — "discount" hay "premium" của range đó không còn nói gì về rủi ro của bạn. Và nếu range thường bị thay thế trong 3 bar còn trade của bạn cần 30 bar, tọa độ sẽ thay đổi trước khi trade kết thúc.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Sáu câu bắt buộc trước khi đo premium/discount
> 1. **Range nào, họ nào, scale nào?** (leg / container / lookback; θ\* của anchors)
> 2. **Origin / termination / known_at / state** của range đó là gì?
> 3. **External liquidity nào còn mở** ở hai phía, cái nào là DOL ứng viên và vì sao?
> 4. **Giá ở đâu** trong range (p), và các candidate range khác nói gì (LRI)?
> 5. **Parent nói gì?** Child đang nested-consistent hay conflicting (R1–R7)?
> 6. **Điều gì sẽ làm range này hết hiệu lực** — viết mức giá và event trước khi vào lệnh.

![[Dealing-Range-v01-15-Gate-System.svg|1516]]
*Sơ đồ: hệ thống gate D1 → H1 → M5 và phân vai location / evidence / trigger.*

### D1 / H4 — Range gốc & Narrative

**Nhiệm vụ:**

1. Major structural swings (θ\* ≥ θ_min(D1)), với role và known_at.
2. External liquidity: swing highs/lows D1 còn sống; PDH/PDL; PWH/PWL.
3. Primary DR: D1 leg DR (nếu có direction) + D1 container / IPDA 20 (liquidity map).
4. Premium / discount / EQ của primary DR; LRI trên các candidate D1.
5. DOL candidates D1, xếp hạng theo mục 14.6.2.
6. HTF POI ở location phù hợp.

**D1 GATE — chỉ chuyển xuống H1 khi:**

| Điều kiện | Kiểm tra khách quan (v0.1) |
|---|---|
| D1 structure đủ xác định | Direction ∈ {BULL, BEAR} ở scale D1; protected anchor còn sống |
| DR đủ xác định | Leg DR ở state ACTIVE (không FORMING, không CONSOLIDATING) |
| DOL đủ xác định | Có ít nhất một DOL meaningful theo hướng direction, M trong dải hợp lý |
| Liquidity chính được xác định | dist_ext_up, dist_ext_dn đã tính |
| Location hiểu được | LRI ≥ ngưỡng (ví dụ ≥ 0.67) hoặc conflict được ghi nhận |

**Kết quả gate có ba trạng thái:** `PASS` / `AMBIGUOUS` / `FAIL`. Khi AMBIGUOUS: không giả vờ bias đã rõ. Các lựa chọn hợp lệ: (i) đứng ngoài, (ii) chỉ log setup cho research, (iii) chỉ xét setup tại D1 extremes (gần protected anchor hoặc boundary) với kích thước giảm — và phân tích riêng nhóm này.

```text
Mẫu ghi nhanh — D1 context (v0.2)
D1 leg DR: origin [giá] (known_at [ngày]) → termination [giá]   | state: ACTIVE
Scale: θ* origin = [x] ATR | family: LEG | direction: BULL
Container / IPDA20: [low] → [high]  (liquidity map)
EQ: [giá] | p hiện tại: [0.xx] | LRI (các candidate): [x/y cùng phía]
External liquidity: BSL [giá, loại: PDH/EQH/swing] · SSL [giá]
DOL ứng viên: [giá] — lý do: [timeframe, chưa bị lấy, path]
Invalidation: close D1 dưới origin [giá] HOẶC MSS ngược cùng scale tại [giá]
D1 GATE: PASS / AMBIGUOUS / FAIL — lý do: [...]
```

### H1 / M15 — Range con & POI

**Nhiệm vụ:**

1. Intermediate structure H1 (θ\* ≥ θ_min(H1)).
2. Internal liquidity của D1 range (chính là H1 swings).
3. H1 leg DR — thường là range của nhịp hồi hoặc sub-impulse bên trong D1 leg.
4. H1 POI trong location phù hợp của **cả** H1 DR và D1 context.
5. Liquidity engineering: equal highs/lows H1, inducement trước POI.
6. Quan hệ với D1 range: nested-consistent hay nested-conflicting?

**H1 refines D1 khi:** H1 DR nằm trong D1 DR và thu hẹp vùng location (ví dụ D1 discount 112–118.5 → H1 discount 113.5–116). **H1 KHÔNG được override D1 khi:** H1 MSS phá một swing có θ\* < θ_min(D1) — đó là internal event của D1 (R7). Một H1 bearish MSS bên trong D1 bullish discount thường chính là *nhịp hồi đang diễn ra*, không phải đảo chiều D1.

**H1 GATE — chỉ chuyển xuống M5 khi:**

- H1 structure xác định; H1 DR ACTIVE.
- POI xác định, nằm ở location phù hợp của H1 DR **và** không vi phạm R3 (parent constraint).
- Liquidity context xác định (có liquidity nào bị lấy/sắp bị lấy quanh POI).
- Setup location aligned với D1 context — không phải counter-HTF trừ khi đang test model countertrend một cách có chủ đích.

**Ghi chú liên quan journal của bạn:** lỗi counter-HTF entry thiếu H1 structural validation mà bạn đã phân tích trước đây chính là trường hợp vượt qua H1 GATE mà không kiểm tra điều kiện cuối. Biến H1 GATE thành checklist bắt buộc trong journal (field `h1_gate = PASS/FAIL` trước mỗi entry) là một cách đo trực tiếp lỗi này theo thời gian.

### M5 / M1 — Confirmation & Entry

M5 **dùng range như context/location, không dùng range như trigger.** Pipeline:

```text
D1 Range (location + direction)
   → H1 Range (setup location)
      → H1 POI (evidence)
         → M5: giá vào POI
            → M5 liquidity sweep (nếu model yêu cầu)
               → M5 MSS (phá M5 swing bảo vệ nhịp hồi)
                  → Displacement
                     → FVG
                        → Entry | Stop (M5 structure, trong khuôn khổ H1 protected) | Target (DOL)
```

**M5 GATE — entry chỉ khi:**

- Giá đã chạm POI H1 hợp lệ.
- Liquidity event xảy ra (nếu required).
- MSS xảy ra (nếu required) — phá swing M5 có ý nghĩa đối với nhịp hồi H1, không phải micro swing ngẫu nhiên.
- Displacement xảy ra (nếu required).
- Execution condition thỏa (FVG hình thành, giá retrace vào FVG theo rule).

**Một điểm hình học quan trọng:** khi stop là M5 structure (nhỏ) còn target là D1/H1 DOL (xa), vị trí trong DR ảnh hưởng *reward distance*, không ảnh hưởng *risk distance*. Điều đó nghĩa là location ở discount sâu hơn → R-multiple tiềm năng lớn hơn — nhưng martingale null vẫn áp dụng: không có bracket nào tạo edge nếu không có non-random behavior. M5 trigger phải *đóng góp thông tin* (tăng q so với p-baseline của bracket), không chỉ "làm đẹp" R:R.

```text
DR nói:       "Nếu bạn định mua, ở đây rẻ hơn so với leg đang chi phối."
DR KHÔNG nói: "Mua ở đây."
```

> [!warning] Range M5 không định nghĩa premium/discount của bias
> Range nhỏ trên M5 chỉ dùng cho execution. Bias và DOL được đo trên range của scale quyết định. Đừng kết luận "giá đang discount" bằng range M5 trong khi trên D1 giá đang premium — trên dữ liệu v0.2, location của *child* cũng không cho thông tin thêm khi điều kiện hóa theo parent (§4.1).

### 4.1. Multiple / Nested / Overlapping Ranges

#### 4.1.0 Ma trận alignment hai tầng (bản dùng nhanh) và dữ liệu thật

| Vị trí trong parent (D1) | Vị trí trong child (H1) | Cách đọc truyền thống | Bằng chứng v0.2 |
|---|---|---|---|
| Discount | Discount | "Cộng hưởng Long" | Proxy nested-consistent: P/W −0.018 [−0.094, +0.059], n = 304 |
| Discount | Premium | Chờ child retrace về discount (vẫn trong discount parent) | — |
| Premium | Discount | Bẫy phổ biến: "discount" child nhưng đang mua ở premium parent | Proxy nested-conflicting: −0.037 [−0.100, +0.031], n = 462 |
| Premium | Premium | "Cộng hưởng Short" (với bearish) | — |

Ghi đủ để không cherry-pick: nhóm entry ở nửa origin của child khi **parent ngược chiều child** cho P/W +0.049 [+0.007, +0.092] (n = 1,361; null −0.016) — *ngược* với kỳ vọng truyền thống. Đây là 1 trong ~16 phép thử của phân tích nested, nên mức "có ý nghĩa" này nhiều khả năng là ngẫu nhiên; nó không được nâng thành rule.

Quy tắc vận hành giữ nguyên ở mức **kỷ luật**: *parent quyết định hướng được phép, child quyết định thời điểm và giá entry; child không phủ quyết parent — xung đột thì giảm size hoặc đứng ngoài*. Nhưng ở mức **bằng chứng**, quy tắc này chưa được dữ liệu ủng hộ: nhóm "cộng hưởng" không tốt hơn nhóm "xung đột" một cách phân biệt được (HYP-DR-004 → REQUIRES MORE DATA, §20.1). Proxy dùng parent = leg DR θ = 6·ATR, child = θ = 2·ATR trên cùng chuỗi — chưa phải D1/H1 thật.

![[Dealing-Range-v02-Real-05-EURUSD-H1-Nested-Parent-Child.png|1516]]
*Hình (dữ liệu thật, EURUSD H1 21/04 → 04/05/2017): parent leg DR θ = 6 (khung tím) bắt đầu bằng gap mở cửa tuần 23/04/2017 (sau vòng 1 bầu cử Tổng thống Pháp); bốn child θ = 2 bên trong — hai cùng chiều, hai ngược chiều. Nửa discount của parent không bao giờ được revisit: ai chờ "discount của parent" đã đứng ngoài toàn bộ leg.*

Ba bài học từ chart thật này:
1. **Child ngược chiều parent ≠ parent đảo chiều.** Hai child bearish ở đây là pullback leg của parent; chúng không phá protected low của parent (R7).
2. **Parent bắt đầu bằng gap** → origin của parent là mức giá *trước gap*; nửa dưới của parent là vùng giá "chưa từng giao dịch" sau gap. Đây là edge case EC9 (opening gap) trong thực tế ([[#16.6. Nhóm F — Vòng đời, cập nhật và invalidation|§16.6]]).
3. **"Chờ discount" có chi phí cơ hội** — trend mạnh có thể không bao giờ về nửa origin của parent (EC5).

#### 4.1.1 Cấu trúc lồng nhau

```text
HTF Range (D1 container / IPDA 60)
└── Intermediate Range (D1 leg)
    └── Internal Range (H1 leg)
        └── Micro Range (M5 — chỉ dùng cho execution, không cho location)
```

#### 4.1.2 Năm loại quan hệ giữa parent và child

| Quan hệ | Mô tả | Diễn giải | Hành động |
|---|---|---|---|
| **Nested-consistent** | Child nằm trong parent; child discount ⊂ parent discount | Location đồng thuận | Location mạnh nhất (hypothesis) |
| **Nested-conflicting** | Child nằm trong parent; child discount nằm ở parent premium | Counter-location | Yêu cầu thêm evidence hoặc giảm kỳ vọng |
| **Overlapping-extension** | Child vượt boundary của parent theo hướng của parent (có acceptance) | Parent EXTENDED | Cập nhật parent |
| **Overlapping-violation** | Child vượt boundary của parent ngược hướng (protected anchor) | Parent có thể INVALIDATED | Kiểm tra invalidation rule |
| **Disjoint** | Child hoàn toàn nằm ngoài parent | Parent COMPLETED hoặc obsolete | Xây parent mới |

#### 4.1.3 Khi các range cho premium/discount khác nhau — range nào ưu tiên?

Không trả lời bằng trực giác. Mỗi range trả lời một câu hỏi khác, nên "ưu tiên" phụ thuộc vào *câu hỏi đang hỏi*:

| Câu hỏi | Range có thẩm quyền |
|---|---|
| Direction nào được phép? | Range cao nhất có protected anchor còn sống và structure rõ |
| Có đủ "room" đến DOL không? | Range chứa DOL (thường là parent) |
| Entry có ở location tốt không? | Range thấp nhất còn scale-matched với trade (thường là setup range H1) |
| Stop đặt ở đâu? | Structure của execution TF (M5), trong khuôn khổ protected anchor của setup range |

Các quy tắc hierarchy cụ thể ở mục 4.2.

![[Dealing-Range-v01-09-Nested-Relations.svg|1516]]
*Sơ đồ: năm quan hệ parent–child; quan hệ quyết định hành động.*

### 4.2. Range Hierarchy

![[Dealing-Range-v01-10-Hierarchy-Rules.svg|1516]]
*Sơ đồ: range hierarchy T0–T4 và bảy quy tắc ưu tiên R1–R7.*

#### 4.2.1 Các quy tắc ưu tiên (v0.1 — tất cả là [HYPOTHESIS] về thiết kế)

- **R1 — Direction từ trên xuống:** direction được quyết định bởi range cấp cao nhất có protected anchor còn sống và structure không mơ hồ. Trong framework của bạn: D1.
- **R2 — Location từ range scale-matched:** location của entry được đo trên range thấp nhất còn thỏa decision-horizon consistency (mục 3.6.3). Thường là H1 leg DR.
- **R3 — Parent constraint:** location của child chỉ hợp lệ nếu (a) child nằm ở vùng parent đồng thuận với direction, **hoặc** (b) DOL của parent nằm đủ xa phía trước để trade có room. Nếu cả hai đều không → skip.
- **R4 — Conflict labeling:** mọi xung đột location giữa các cấp phải được ghi nhận (`location_conflict = TRUE`) trong journal/backtest để phân tích riêng — không được âm thầm bỏ qua.
- **R5 — Recency trong cùng cấp:** giữa các range cùng scale, dùng range ACTIVE gần nhất (không phải range có vẻ "đẹp" nhất).
- **R6 — Parent invalidation lan xuống:** khi protected anchor của parent bị phá có acceptance, mọi child range mất directional support; phải tái suy luận từ trên xuống.
- **R7 — Child không override parent direction:** một MSS trên H1 chỉ thay đổi D1 direction nếu swing bị phá **có cấp độ D1** (ví dụ θ\* ≥ θ_min(D1)). Ý nghĩa thuộc về swing bị phá, không thuộc về chart mà bạn nhìn thấy sự kiện.

#### 4.2.2 Bảng tầng

| Tier | Range                  | Vai trò trong D1→H1→M5 | Được phép quyết định                     |
| ---- | ---------------------- | ---------------------- | ---------------------------------------- |
| T0   | W1 / IPDA 60           | Bối cảnh xa            | Room lớn, DOL HTF                        |
| T1   | D1 container / IPDA 20 | Liquidity map D1       | DOL candidates                           |
| T2   | D1 leg DR              | Daily bias location    | Direction + location D1                  |
| T3   | H1 leg DR              | Setup location         | Location của POI                         |
| T4   | M5 structure           | Execution              | Trigger, stop, không quyết định location |

#### 4.2.3 Một khuyết điểm cần thừa nhận

Hierarchy này giả định rằng các tầng *lồng nhau gọn gàng*. Thực tế: H1 leg có thể bắt đầu từ trước D1 BOS, hoặc kéo dài qua boundary D1. Khi cấu trúc không lồng nhau sạch sẽ, R1–R7 vẫn cho ra quyết định, nhưng quyết định đó nên được đánh dấu `nesting_clean = FALSE` và phân tích riêng. [BACKTEST REQUIRED] — có thể các setup "nesting sạch" có expectancy khác biệt đáng kể.

### 4.3. Bài toán quá nhiều swing

#### 4.3.1 Quy mô của vấn đề

[MATHEMATICAL — đã mô phỏng] Một random walk thuần túy, trên 250 bar, tạo ra trung bình:

| Định nghĩa swing | Swing highs / 250 bar | Swing lows / 250 bar |
|---|---|---|
| Fractal 5-bar (n=2) | ~35 | ~35 |
| Fractal 7-bar (n=3) | ~24 | ~24 |
| Fractal 11-bar (n=5) | ~15 | ~15 |

Nếu mọi swing đều có thể làm anchor, số cặp anchor khả dĩ trong một năm D1 là hàng trăm. Với hàng trăm range khả dĩ, **bất kỳ kết quả nào cũng có thể được "giải thích" bằng một range nào đó** — "giá phản ứng tại discount của range X", "giá phá range Y vì đó chỉ là internal range". Một framework có thể giải thích mọi kết quả là framework **không thể falsify** — và không có giá trị dự báo.

#### 4.3.2 Funnel lọc swing

![[Dealing-Range-v01-16-Swing-Funnel.svg|1516]]
*Sơ đồ: funnel lọc swing — detection → scale → consequence → alive → relevant.*

Số lượng chính xác ở mỗi tầng là **đại lượng cần đo** trên dữ liệu của bạn — đừng dùng con số của ai khác. Đo nó chính là một bước research hữu ích: nếu sau funnel vẫn còn quá nhiều swing, tham số quá lỏng; nếu còn 0, quá chặt.

![[Dealing-Range-v01-05-Scale-Space.svg|1516]]
*Sơ đồ: swing hierarchy như scale-space — tăng θ, swing nhỏ biến mất; leg cuối chưa xác nhận.*

Điểm đáng chú ý trong panel dưới cùng (θ = 8×ATR): toàn bộ đợt tăng từ bar ~46 đến bar 400 là **một leg chưa được xác nhận**. Ở scale lớn, tại thời điểm cuối chart, điều duy nhất ta biết chắc là range đang FORMING — đỉnh của nó chưa tồn tại. Đây là confirmation lag ở dạng trực quan nhất: scale càng lớn, bạn càng biết muộn.

#### 4.3.3 Hierarchy Micro → Internal → Intermediate → Structural → External → HTF có đủ không?

**Không hoàn toàn**, vì ba lý do:

1. **Trộn scale và role** (mục 3.2.2): "Structural" và "External" là vai trò, "Micro" và "HTF" là kích thước.
2. **Rời rạc hóa một đại lượng liên tục:** ranh giới giữa "internal" và "intermediate" là tùy ý; swing nằm gần ranh giới sẽ nhảy qua lại giữa các level khi tham số thay đổi nhỏ → kết quả không ổn định.
3. **Không có yếu tố thời gian:** một swing thay đổi role theo thời gian (candidate → protected → spent). Hierarchy tĩnh không nắm được điều đó.

**Cải tiến:** `swing = (θ*, role(t), consequences, known_at)` — xem mục 3.2.3. Level chỉ là *view* của θ\* để con người dễ đọc.

#### 4.3.4 Điều kiện để framework có thể falsify

Anchor selection phải là một **hàm xác định**:

$$A: \text{OHLC}_{\le t} \times \Theta \rightarrow (L^*, H^*, \text{state})$$

với Θ là bộ tham số **viết ra trước khi nhìn dữ liệu test**. Hai người khác nhau chạy A trên cùng dữ liệu phải ra cùng một range. Nếu không thể làm được điều này, phần đó của framework vẫn còn là discretionary — và phải được đánh dấu như vậy trong journal.

### 4.4. Bài toán quá nhiều range và LRI

#### 4.4.0 Dữ liệu thật: cùng một bar, bốn câu trả lời

![[Dealing-Range-v02-Real-04-EURUSD-H1-Four-Definitions-Same-Bar.png|1516]]
*Hình (dữ liệu thật, EURUSD H1, bar 24/05/2017 18:00): leg DR θ = 1.5 nói "bearish, giá ở premium — vùng bán"; θ = 2 nói "bearish, giá sát term — đừng bán đuổi"; θ = 3 nói "bullish, giá ở discount — vùng mua"; IPDA-20 nói "premium". Mỗi panel chỉ dùng dữ liệu ≤ T.*

**[EMPIRICAL v0.2]** Đo trên toàn universe (§19.3): trong các bar mà cả bốn định nghĩa (leg θ = 1.5 / 2 / 3, IPDA-20) cùng có range active, **cả bốn chỉ đồng thuận về phía premium/discount ở 54% (cổ phiếu D1), 56% (EURUSD H1), 70% (FX D1 close-only)** — và random walk cho gần đúng các con số đó (57% / 56% / 69%). Chênh lệch trung bình của p giữa θ = 1.5 và θ = 3 là 0.21–0.30 bề rộng range.

Hệ quả:
- **LRI thấp không phải dấu hiệu "thị trường khó đọc hôm nay"** — nó là thuộc tính hình học thường trực của việc có nhiều định nghĩa range hợp lệ. Gần một nửa thời gian, câu "giá đang ở discount" phụ thuộc vào lựa chọn định nghĩa nhiều hơn vào giá.
- Vì vậy LRI là **bộ lọc loại trừ** hợp lý (chỉ xét setup khi các candidate đồng thuận), nhưng việc LRI cao có *tăng* expectancy hay không vẫn là HYP-DR-011 (UNTESTED).

#### 4.4.1 Valid vs Relevant vs Tradeable

| Cấp | Định nghĩa | Ví dụ không đạt |
|---|---|---|
| **Valid** | Anchors thỏa định nghĩa; state ≠ INVALIDATED; W/ATR trong dải | Range có origin chưa có consequence |
| **Relevant** | Valid + scale-matched với quyết định + nhất quán với parent context + giá đang tương tác với nó | Range D1 hợp lệ nhưng giá đã ở cách xa 3×W |
| **Tradeable** | Relevant + location robust (LRI cao) + đủ room đến DOL + có POI + trigger khả thi + chi phí chấp nhận được | Range relevant nhưng DOL chỉ cách 0.8R |

> Một range có thể **valid nhưng không relevant**; **relevant nhưng không tradeable**. Phần lớn thời gian, không có range nào tradeable — và đó là thông tin đúng.

#### 4.4.2 Range Selection Framework

**Bước 1 — Sinh tập candidate** (cố định danh sách):

```text
C1: Leg DR ở scale k (setup)          C4: Container DR ở scale k
C2: Leg DR ở scale k+1 (trend)        C5: IPDA 20 (D1)
C3: Leg DR fallback (bỏ qua 1 HL)     C6: IPDA 40/60 (D1, context xa)
```

**Bước 2 — Lọc valid:** loại candidate INVALIDATED, FORMING (với mục đích location), W/ATR ngoài dải.

**Bước 3 — Chấm điểm relevance** (biến, không phải trọng số cố định):

| Biến | Đo |
|---|---|
| Timeframe / scale | θ\* của anchors |
| Structural significance | origin có BOS/MSS; MSS > BOS |
| Liquidity significance | anchor từng sweep liquidity; boundary có cluster |
| Displacement | D-score của leg |
| Reaction | reaction đã hoàn tất tại anchor (chỉ anchor đã đóng) |
| DOL fit | M = distance_to_DOL / W trong dải |
| Freshness | số bar kể từ known_at; số lần range bị chạm |
| Regime fit | trend-regime → leg DR; range-regime → container |
| Size | W / stop_distance ≥ c1 |
| Persistence | range đã tồn tại bao lâu mà không đổi state |

**Bước 4 — Chọn primary theo hierarchy** (mục 4.2): direction từ range cao nhất còn protected; location từ range scale-matched thấp nhất.

**Bước 5 — Location Robustness Index:**

$$LRI = \frac{\left|\sum_i w_i \cdot \ell_i\right|}{\sum_i w_i}, \qquad \ell_i = \begin{cases}+1 & p_i < 0.5 \\ -1 & p_i > 0.5\end{cases}$$

trên các candidate valid & relevant (w_i có thể bằng nhau ở v0.1). LRI = 1: mọi frame đồng thuận; LRI ≈ 0: chia đôi.

![[Dealing-Range-v01-17-Valid-Relevant-Tradeable-LRI.svg|1516]]
*Sơ đồ: valid → relevant → tradeable, và LRI trên hai case minh họa.*

**Bước 6 — Output bắt buộc:**

```text
primary_range, parent_range, candidate_set, LRI, location_conflict, nesting_clean, known_at
```

Nếu LRI thấp hoặc không có candidate relevant → `LOCATION = AMBIGUOUS`. **Không ép ra một câu trả lời.**

#### 4.4.3 Vì sao không chọn "range đẹp nhất"

"Đẹp" thường đồng nghĩa với "khớp với kết quả tôi đã thấy". Chọn range theo thẩm mỹ là con đường ngắn nhất đến hindsight bias. Quy tắc: nếu bạn không thể viết ra *vì sao* một range được chọn bằng các biến ở trên, bạn chưa chọn — bạn đang kể chuyện.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Dealing Range được xem là hợp lệ khi
- [ ] Origin có structural consequence ở scale k (từ nó giá đã close vượt một swing đối diện cùng cấp).
- [ ] Termination đã đóng: nhịp hồi từ cực trị ≥ θ·ATR(term) (HEURISTIC θ = 2) → state **ACTIVE**.
- [ ] Thời điểm phân tích ≥ `known_at` của cả hai anchor.
- [ ] Origin chưa bị **close** xuyên (wick xuyên = SWEPT, vẫn hợp lệ) và chưa có MSS ngược chiều cùng scale.
- [ ] Range thuộc đúng scale của quyết định; parent chưa bị invalidate (R6).
- [ ] Giá chưa đi quá xa termination (|p − 1| < x·W) và range chưa stale (HEURISTIC).

### Dealing Range bị vô hiệu (cần vẽ lại) khi
- [ ] **MSS ngược chiều cùng scale** (close vượt swing đối diện gần nhất cùng cấp) → REVERSED. Trên dữ liệu v0.2 đây là cách thất bại *phổ biến nhất* — xem [[#5.2. State machine|§5.2]].
- [ ] **Close xuyên origin + acceptance** (k close bên ngoài, không reclaim) → INVALIDATED.
- [ ] **BOS cùng chiều** (close vượt termination từ một nhịp hồi đạt θ) → range cũ EXTENDED/COMPLETED, range mới thay thế. Đây là *completion*, không phải thất bại.
- [ ] Trend chuyển sang consolidation (Scenario G) → leg DR = CONSOLIDATING, dùng container DR.
- [ ] Parent đổi trạng thái (Scenario I) → mọi child bị đánh giá lại từ trên xuống.
- [ ] Context / temporal invalidation: regime shock, range quá cũ không tương tác (CX-23, CX-24).
- [ ] Range chọn sai từ đầu theo quy tắc đã viết (không phải "sai" vì kết quả thua).

> [!important] Hai điều KHÔNG phải invalidation
> 1. **Wick xuyên boundary rồi close quay lại** = SWEPT (sweep), không phải invalidation — nhưng ở phía origin, đây là sự kiện **hạ base-rate** continuation (§5.4).
> 2. **Giá chạm/vượt termination (DOL ở boundary)** = completion — range đã làm đúng điều nó dự đoán.

### 5.1. Range Invalidation — bốn sự kiện hay bị gộp

#### 5.1.1 Phân biệt bốn sự kiện hay bị gộp chung

| Sự kiện | Định nghĩa | Range còn dùng được? |
|---|---|---|
| **Extension** | Giá vượt termination theo hướng của range, có acceptance | Có — range cập nhật (Scenario A/C) |
| **Completion** | Giá chạm/lấy DOL tại hoặc ngoài termination | Range đã hoàn thành nhiệm vụ; cần frame mới cho pha tiếp theo |
| **Sweep (violation không acceptance)** | Wick/close ngắn vượt boundary rồi quay lại | Có — state SWEPT; liquidity đã tiêu thụ |
| **Invalidation** | Protected anchor bị phá có acceptance | Không — directional interpretation chết |

**Lỗi phổ biến:** coi completion là invalidation ("giá đã phá range high, range invalid"). Trong bullish DR, phá range high là **điều range dự đoán** — nó là thành công, không phải thất bại.

![[Dealing-Range-v01-11-Four-Outcomes.svg|1516]]
*Sơ đồ: bốn kết cục của một bullish DR — chỉ phá protected low có acceptance mới là invalidation.*

#### 5.1.2 Năm loại invalidation

**(1) Structural invalidation** — protected anchor bị phá có acceptance.
Candidate objective definition (các tầng — HEURISTIC):

```text
SOFT:    Low < L*  (wick)                                   → SWEPT_L, không invalid
MEDIUM:  Close < L*                                         → PENDING_INVALIDATION
HARD:    Close < L*  AND  (body/ATR ≥ d  OR  k closes < L*)
         AND  không reclaim (close > L*) trong m bar         → INVALIDATED
```

**(2) Liquidity invalidation** — liquidity mà range được kỳ vọng hướng tới đã biến mất *không theo cách range dự đoán*. Ví dụ: equal highs (DOL) bị một spike tin tức lấy mất trong 1 phút rồi giá sập về giữa range. Range không invalid về cấu trúc, nhưng giá trị dự báo của nó (đường đến DOL) đã bị tiêu thụ.

**(3) Price invalidation** — giá đi quá xa một boundary: |P − boundary| > x·W (ví dụ x = 0.5). Khi giá đã đi thêm nửa range bên ngoài, tọa độ p (ví dụ p = −0.5) không còn ý nghĩa hữu ích; cần frame mới.

**(4) Temporal invalidation** — range quá cũ so với scale của nó: tuổi > T_max(TF) hoặc không có tương tác trong N bar. (IPDA 60-day lookback có thể xem là một định nghĩa "tuổi tối đa" tự nhiên cho D1.) HEURISTIC.

**(5) Context invalidation** — HTF đổi structure (R6); regime volatility đổi đột ngột (ATR hiện tại / ATR lúc hình thành range > r); sự kiện vĩ mô lớn khiến anchors cũ không còn phản ánh định giá hiện tại.

#### 5.1.3 Trả lời các câu hỏi trong brief

| Câu hỏi | Lập trường v0.1 | Lý do | Test |
|---|---|---|---|
| Có cần close outside range? | Có — close là điều kiện tối thiểu cho mọi thứ vượt "SOFT" | Wick-only có tỷ lệ false break cao; random walk tạo ra sweep ~43% số lần | So sánh wick vs close vs close+k |
| Wick outside có invalid không? | Không | Wick = sweep; liquidity lấy nhưng không acceptance | Tỷ lệ tiếp diễn sau wick vs sau close |
| Một lần sweep có invalid không? | Không; nhưng hai sweep ngược chiều liên tiếp (cả L\* và H\*) → CONSOLIDATING | Sweep hai phía gợi ý balance | Tần suất và hậu quả của "double sweep" |
| Có cần displacement outside range? | Không bắt buộc cho invalidation, nhưng là **bằng chứng tăng cường** | Displacement giảm xác suất reclaim (hypothesis) | P(reclaim \| close + displacement) vs P(reclaim \| close) |
| Có cần structural break? | Với protected anchor, **phá nó chính là structural break** | Protected anchor được định nghĩa là điểm invalidation | — |
| Có cần acceptance? | Có cho HARD | Acceptance phân biệt "đã chấp nhận giá mới" với "thử rồi bị từ chối" | Tối ưu k, m trên in-sample, kiểm tra plateau |
| Có cần reclaim? | Reclaim trong m bar → **hủy** invalidation, chuyển thành SWEPT (failed breakdown) | Failed breakdown là một sự kiện liquidity, không phải structure change | P(reversal \| reclaim) — đây chính là hypothesis "Turtle Soup"/sweep reversal |

#### 5.1.4 Định nghĩa "acceptance" có thể đo lường

Candidate definitions (chọn một, cố định, test):

1. **k-close acceptance:** k close liên tiếp bên ngoài boundary (k ∈ {1, 2, 3}).
2. **Time-at-price acceptance:** ≥ f% số bar trong cửa sổ m có close bên ngoài.
3. **Flip acceptance:** giá quay lại test boundary từ phía bên kia và bị từ chối (boundary cũ đổi vai trò).
4. **Displacement acceptance:** close bên ngoài bằng candle body/ATR ≥ d và để lại FVG bên ngoài boundary.

### 5.2. State machine

![[Dealing-Range-v01-12-State-Machine.svg|1516]]
*Sơ đồ: state machine v0.1 và đối chiếu với quy ước của note 57.*

#### 5.2.1 Đối chiếu với trạng thái của note 57

| Note 12 (state machine) | Note 57 | Ghi chú |
|---|---|---|
| FORMING | SUSPENDED (chưa đủ dữ liệu để phán) | Không đo location |
| ACTIVE | VALID | — |
| SWEPT_H / SWEPT_L | VALID (row 1 của bảng §14 note 57) | Wick xuyên, close trong range |
| Wick giãn biên → dời anchor lên wick | REFINED | Quy ước mặc định của vault (Scenario E, §5.3) |
| EXTENDED / COMPLETED | REPLACED | Range mới thay thế sau BOS cùng chiều |
| REVERSED / INVALIDATED | INVALIDATED | Note 12 tách REVERSED (MSS ngược) khỏi INVALIDATED (close xuyên origin) để đo được |
| CONSOLIDATING | — | Chuyển sang container DR |

#### 5.2.2 Dữ liệu thật: range thường "chết" như thế nào?

**[EMPIRICAL v0.2]** Theo dõi vòng đời của mọi leg DR θ = 2 (đã ACTIVE, đã kết thúc) trên universe §19.3:

| Nhóm | n DR | EXTENDED | REVERSED | INVALIDATED | Null EXTENDED |
|---|---:|---:|---:|---:|---:|
| Cổ phiếu D1 (OHLC) | 665 | 0.544 [0.507, 0.583] | 0.445 | 0.011 | 0.487 |
| EURUSD H1 (OHLC) | 183 | 0.530 [0.459, 0.601] | 0.464 | 0.005 | 0.482 |
| FX D1 (close-only) | 2,408 | 0.491 [0.471, 0.511] | 0.509 | 0.000 | 0.498 |

Ba điều rút ra:
1. **INVALIDATED gần như không xảy ra như một sự kiện riêng.** Vì origin thường chính là swing được xác nhận cuối cùng ở phía đó, close xuyên origin *đồng thời* là MSS ngược chiều → được ghi là REVERSED. Khoảng **một nửa** số REVERSED xảy ra khi origin vẫn còn nguyên (close phá một swing nội bộ nằm *trên* origin — như Real 2 ở §6). Thực hành: **mức invalidation vận hành là swing được xác nhận gần nhất cùng scale**, origin chỉ là backstop.
2. **Tỷ lệ leg tiếp diễn ≈ một đồng xu**, kể cả trên dữ liệu thật. Cổ phiếu D1 cao hơn null (0.544 vs 0.487, CI không chứa null) — dấu vết drift/momentum của chuỗi cổ phiếu giai đoạn 1995–2014, không phải của vị trí. FX D1 và EURUSD H1 không khác null có ý nghĩa. → HYP-DR-015.
3. **Đời sống trung vị** của một leg DR từ ACTIVE đến khi kết thúc: 11 bar (cổ phiếu D1), 12 bar (EURUSD H1), 8 bar (FX D1) — null 9 / 10 / 7. Một leg DR ở scale θ = 2 là khung tọa độ *ngắn hạn*; dùng nó cho mục tiêu xa hơn vài chục bar là dùng sai scale.

### 5.3. Range Updating

Mỗi scenario dưới đây giả định **bullish Leg DR ở scale k** (L\* = protected low, H\* = termination high), trừ khi ghi khác. Bốn hành động: **KEEP / REFINE / CREATE NEW / INVALIDATE**.

#### Scenario A — Giá tạo HH mới

- **Nếu HH xảy ra trong cùng impulse (chưa có pullback đạt θ):** → **REFINE** (EXTEND): H\* dời lên, L\* giữ nguyên, range quay lại FORMING cho đến khi high mới đóng. *Why:* chưa có leg mới; chỉ là leg cũ kéo dài.
- **Nếu HH được tạo bởi leg xuất phát từ một HL đạt θ:** → **CREATE NEW** leg DR (HL mới → HH mới); range cũ trở thành historical, HL mới trở thành protected. *Why:* protected low đã "dịch lên" — mức invalidation của câu chuyện bullish đã thay đổi.
- **Nếu HH chỉ là micro (không đạt θ so với swing trước ở scale k):** → **KEEP**. *Why:* không phải sự kiện ở scale k.

#### Scenario B — Giá tạo HL mới

→ **KEEP** + đánh dấu HL là CANDIDATE. *Why:* HL chỉ trở thành protected khi giá từ nó phá H\*. Cập nhật L\* tại thời điểm HL hình thành là hindsight nếu sau đó giá phá HL — bạn sẽ vẽ lại range sau khi thấy kết quả.

#### Scenario C — Giá phá external high trước đó (close + acceptance)

→ **CREATE NEW** (range cũ EXTENDED/COMPLETED). *Why:* đây là BOS ở scale k. Origin của leg vừa phá = protected low mới. Old high (H\* cũ) chuyển thành reference level bên trong range mới (có thể trở thành support/breaker area — [ICT FRAMEWORK] "old high" trong PD array matrix).

#### Scenario D — Giá phá internal high

→ **KEEP** external DR; **REFINE** internal/setup DR. *Why:* internal break không thay đổi structure ở scale k. Nhưng nếu đây là phá internal high *trong một nhịp hồi* của bullish DR (tức internal structure chuyển từ bearish sang bullish), đó có thể là dấu hiệu nhịp hồi kết thúc — thông tin cho H1 setup, không cho D1 range.

#### Scenario E — Giá sweep high rồi close quay lại bên trong

→ **KEEP** structural DR, **state = SWEPT_H**, cập nhật liquidity map: BSL phía trên H\* đã bị tiêu thụ. *Why:* không có acceptance → không phải BOS. Nhưng liquidity phía trên đã được lấy; nếu H\* là DOL, DOL đã được **completed** (một phần hoặc toàn bộ).

**Câu hỏi khó:** có dời H\* lên đỉnh wick của sweep không?

| Lựa chọn | Hệ quả |
|---|---|
| Dời H\* lên wick | EQ tăng; nhất quán với "extreme thực tế"; phù hợp nếu sau đó hình thành bearish leg (wick = origin của leg giảm mới) |
| Giữ H\* cũ | Range structural ổn định; wick được ghi nhận như một event, không như anchor |

> [!important] Quy ước — không âm thầm thay rule đã có trong vault
> **OLD RULE (vault, note 57 — REFINED):** wick giãn biên → dời anchor lên wick, đo lại levels, KHÔNG đổi phân tích. v0.1 **giữ nguyên** quy ước này làm mặc định.
> **ALTERNATIVE (đề xuất ban đầu của v0.1):** giữ H\* structural cũ, chỉ gắn cờ SWEPT_H; dùng wick làm origin nếu một bearish leg DR mới hình thành từ đó.
> **REASON:** tách "extreme giá" khỏi "anchor cấu trúc" giúp EQ ổn định hơn (liên quan W4 — EQ trôi qua đêm).
> **EXPECTED EFFECT:** ít re-measure hơn; nhưng có thể lệch khỏi mức mà người khác dùng.
> **BACKTEST REQUIRED?** Có — chạy hai quy ước như hai arm; nếu kết quả nhạy mạnh với lựa chọn này, edge (nếu có) không robust.

#### Scenario F — Displacement ngược chiều range

- **Displacement giảm từ premium, dừng trong discount, không phá L\*:** → **KEEP**, gắn cờ `adverse_displacement = TRUE`. *Why:* retracement sâu vẫn hợp lệ, nhưng chất lượng câu chuyện bullish giảm — bearish displacement là bằng chứng một phía bán đã áp đảo tạm thời.
- **Displacement phá L\* có close:** → **INVALIDATE** (xem mục 5.1), chuẩn bị bearish leg DR mới với origin = H\* (hoặc đỉnh gần nhất trước displacement).

#### Scenario G — Trend chuyển sang consolidation

Dấu hiệu (có thể formalize): n lần liên tiếp không phá được H\* hoặc L\*; biên độ swing nội bộ co lại (θ\* của swing mới giảm); các swing high/low mới gần bằng nhau.

→ **CREATE NEW** Container DR (swing high/low chưa bị phá của vùng consolidation), đặt state leg DR = CONSOLIDATING. *Why:* Leg DR giả định có một impulse đang chi phối; trong consolidation, không có. Premium/discount trong container mang ý nghĩa *mean-reversion* ("mua đáy hộp, bán đỉnh hộp") — một hypothesis **khác hẳn** continuation. Không được dùng thống kê của hypothesis này cho hypothesis kia.

#### Scenario H — Consolidation chuyển sang expansion

→ **CREATE NEW** Leg DR: origin = extreme đối diện của container (hoặc swing low cuối cùng bên trong container trước breakout), termination = high của expansion. Container cũ trở thành reference (boundary cũ = old high/low, "origin zone"). *Why:* breakout có displacement + acceptance là BOS ở scale của container.

#### Scenario I — HTF structure thay đổi

→ **INVALIDATE** mọi child range theo R6; tái suy luận từ D1 xuống. *Why:* direction của child được "vay" từ parent. Khi parent mất direction, child range có thể vẫn *valid* về hình học nhưng không còn *relevant* cho quyết định.

#### Tóm tắt Scenario

| Scenario | Sự kiện | Hành động | Lý do cốt lõi |
|---|---|---|---|
| A | HH mới | Extend / New / Keep | Tùy HH có từ HL đạt θ không |
| B | HL mới | Keep (candidate) | HL chưa có consequence |
| C | Phá external high | New | BOS ở scale k |
| D | Phá internal high | Keep ext., refine int. | Không phải sự kiện scale k |
| E | Sweep high | Keep + REFINED levels, SWEPT_H | Không acceptance; liquidity đã lấy |
| F | Displacement ngược | Keep + flag / Invalidate | Tùy có phá protected không |
| G | Trend → range | New container | Không còn impulse chi phối |
| H | Range → expansion | New leg | BOS ở scale container |
| I | HTF đổi | Invalidate children | Direction vay từ parent |

### 5.4. Sweep vs phá range thật & re-mapping

#### 5.4.1 Phân xử bằng rule viết trước

| Quan sát | State | Hành động | Ghi chú bằng chứng |
|---|---|---|---|
| Wick qua termination, close quay lại trong range | SWEPT_H (bullish DR) | KEEP; quy ước vault: REFINED — dời anchor lên wick, đo lại levels | DOL ở phía đó coi như đã *completed* một phần |
| Wick qua **origin**, close quay lại trong range | SWEPT_L (bullish DR) | KEEP anchor cấu trúc; **hạ confidence**; chỉ trade theo leg khi có trigger LTF | Base-rate continuation sau sweep thấp (§5.4.3) |
| Một close bên ngoài, chưa đủ k close | PENDING | Không hành động dựa trên range cho tới khi state rõ (EC-16) | k là HEURISTIC; HYP-DR-012 |
| k close bên ngoài phía termination, pullback không reclaim | EXTENDED / COMPLETED | CREATE NEW: origin mới = cực trị nhịp hồi trước break | Completion, không phải thất bại |
| Close phá swing đối diện gần nhất cùng scale (có thể trên origin) | REVERSED | Range hết hiệu lực; chờ range ngược chiều ACTIVE (location blackout) | Cách thất bại phổ biến nhất (§5.2.2) |
| Close xuyên origin + acceptance mà chưa có MSS trước | INVALIDATED | Như trên | Hiếm (~1%) |

#### 5.4.2 Re-mapping sau displacement — bốn nguyên tắc

Chi tiết đầy đủ: [[37-Re-mapping-Dealing-Range-sau-Displacement]].

1. **Range mới lấy gốc từ origin của displacement leg** (cực trị nhịp hồi trước break) → cực trị mới. Không giữ đầu range cũ đã bị phá làm biên.
2. **Chờ leg đóng mới đo:** đo khi displacement còn chạy = đo trên range FORMING (p ≈ 1).
3. **Sweep ≠ re-map:** wick qua boundary rồi close lại trong range không tạo range mới; chỉ **acceptance** (close + giữ ngoài) mới buộc re-map. *(Xem thay đổi rule ở §5.4.3 về phần "đáng tin hơn".)*
4. **Cascade re-map:** khi range của scale cao re-map, mọi range con bên trong được đánh giá lại theo bản đồ mới (Scenario I, R6).

#### 5.4.3 Dữ liệu thật: hai kết cục sau sweep origin

![[Dealing-Range-v02-Real-03-EURUSD-H1-Sweep-Two-Outcomes.png|1516]]
*Hình (dữ liệu thật, EURUSD H1): cùng một sự kiện — wick xuyên protected origin, close quay lại trong range. Panel A (08/2017): leg tiếp tục, EXTENDED sau ~4 ngày. Panel B (05/2017): REVERSED ngay bar kế tiếp. Tại thời điểm sweep hai trường hợp không phân biệt được bằng hình dạng.*

**[EMPIRICAL v0.2]** P(EXTENDED) của leg DR θ = 2, theo việc origin có bị sweep trong đời DR hay không:

| Nhóm | Có sweep origin | Không sweep | Null — có sweep | Null — không sweep |
|---|---:|---:|---:|---:|
| Cổ phiếu D1 | 0.277 [0.181, 0.373] (n = 83) | 0.582 [0.543, 0.622] | 0.183 | 0.533 |
| EURUSD H1 | 0.241 [0.103, 0.414] (n = 29) | 0.584 [0.506, 0.662] | 0.171 | 0.525 |

Đọc đúng:
- So với leg **không** bị sweep, leg bị sweep origin **ít** tiếp diễn hơn rõ rệt (≈ 0.25 vs ≈ 0.58). Trên random walk cũng vậy (0.17–0.18 vs 0.53) — phần lớn hiệu ứng là **hình học**: sweep origin nghĩa là giá đã retrace sâu tới tận protected level.
- So với null **cùng điều kiện sweep**, dữ liệu thật cao hơn ~0.06–0.09. Có thể có một chút thông tin, nhưng CI chồng nhau một phần và n nhỏ → HYP-DR-014.
- Tỷ lệ DR có sweep origin ở dữ liệu thật (12.5% cổ phiếu, 15.8% EURUSD H1) ≈ null (13.0% / 12.0%): **tần suất "sweep" không vượt ngẫu nhiên**.

> [!important] Thay đổi rule — không âm thầm sửa
> **OLD RULE (A3.3 / W2 bản cũ, và note 57 §14 row 1):** "Wick qua external rồi đóng lại trong range không tạo range mới — range cũ còn nguyên, **thậm chí đáng tin hơn / mạnh hơn về phía đối diện** vì một đầu vừa được 'sạc' liquidity."
> **NEW RULE (v0.2):** Sweep ≠ re-map **vẫn giữ** (state = SWEPT, anchor cấu trúc không đổi). Nhưng sweep **protected origin** của leg DR **không** làm range "đáng tin hơn": nó là sự kiện **hạ base-rate continuation**. Chỉ coi sweep là tín hiệu theo hướng leg khi có trigger LTF (MSS + displacement theo hướng leg) — và trigger đó chính là thứ phải được test (HYP-DR-014). W2 (ngày Seek & Destroy quét *cả hai* đầu của *container* range) là trường hợp khác, giữ ở dạng [HYPOTHESIS], chưa test.
> **REASON:** nghiên cứu vòng đời §5.2.2 / §19.3: P(EXT | sweep origin) ≈ 0.24–0.28 so với ≈ 0.58 khi không sweep.
> **EXPECTED EFFECT:** ít lệnh "bắt sweep" theo leg không có trigger; giảm size khi đang ở state SWEPT_L.
> **BACKTEST REQUIRED?** Có — HYP-DR-014 trên instrument mục tiêu với trigger LTF cụ thể. Note 57 §14 row 1 nên được đánh dấu tương ứng (chưa sửa trong v0.2 của note 12).

### 5.5. Hindsight Bias

#### 5.5.1 Vì sao DR đặc biệt dễ bị hindsight

Một Dealing Range nhìn *cực kỳ rõ* sau khi thị trường chạy xong, vì khi đó: swing tương lai đã tồn tại; significance đã được "chứng minh" bởi hậu quả; termination đã đóng; DOL đã được lấy (hoặc không); liquidity đã bị sweep (hoặc không). Tại thời điểm real-time, **không cái nào trong số đó đã biết**.

#### 5.5.2 Năm cơ chế look-ahead cụ thể trong DR

| # | Cơ chế | Ví dụ | Cách chặn |
|---|---|---|---|
| 1 | **Pivot confirmation lag** | Fractal low tại bar 100 (n=2) chỉ biết tại close bar 102 | Dùng known_at = j + n |
| 2 | **Significance lag** | Low tại bar 100 chỉ thành protected khi BOS tại bar 110 | Role(t) chỉ đổi tại thời điểm event |
| 3 | **Termination lag** | High tại bar 120 chỉ "đóng" khi giá hồi θ tại bar 127 | State FORMING đến bar 127 |
| 4 | **Selection among candidates** | Chọn range nào "hoạt động" sau khi xem kết quả | Selection rule cố định; lưu toàn bộ candidate set |
| 5 | **Repainting tools** | Nhiều ZigZag indicator vẽ lại leg cuối khi có dữ liệu mới | Chỉ dùng swing đã xác nhận; kiểm tra indicator có repaint không |

**Ví dụ timeline hoàn chỉnh (D1):**

![[Dealing-Range-v01-08-Known-At-Timeline.svg|1516]]
*Sơ đồ: known_at — low bar 100 thành CANDIDATE ở bar 102, PROTECTED ở bar 110; range chỉ ACTIVE từ bar 127.*

⇒ Mọi quyết định dựa trên "discount của range 1.0800–1.0960" chỉ hợp lệ từ bar 127. Một backtest dùng range này tại bar 121–126 là look-ahead.

#### 5.5.3 Ex-post range vs Real-time range

- **Ex-post range:** được xác định sau khi biết kết quả. Hợp lệ **chỉ** như *biến phụ thuộc* (label) trong research — ví dụ để hỏi "những range nào hóa ra quan trọng có đặc điểm gì tại thời điểm hình thành?".
- **Real-time range:** được xác định bằng A(OHLC ≤ t). Là loại *duy nhất* được phép làm *biến độc lập* (feature) trong backtest hoặc làm cơ sở cho quyết định.

Trộn hai loại — dùng ex-post range như feature — là lỗi phổ biến nhất trong backtest ICT thủ công.

#### 5.5.4 Protocol chống hindsight cho case study thủ công

1. **Che phần bên phải chart** (replay mode) trước khi phân tích.
2. Tại mỗi bar quyết định, **ghi lại** (timestamp): candidate set, primary range, LRI, D1/H1 gate state, POI dự kiến.
3. Chỉ sau đó mới tua tới — và **không sửa** bản ghi cũ; chỉ thêm bản ghi mới.
4. Cấu trúc T0 → T5 (mục 17.1) cho mỗi case.
5. Mỗi tháng, đo **tỷ lệ "redraw"**: số lần bạn muốn sửa range sau khi thấy kết quả. Đây là metric trực tiếp của hindsight bias cá nhân.

#### 5.5.5 Dữ liệu cần lưu để backtest không có look-ahead

```text
swings:   id, tf, type, price, bar_time, known_at, theta_star_at(t), role_history[(t, role)]
events:   id, tf, type (BOS/MSS/SWEEP/ACCEPT/RECLAIM), level_swing_id, bar_time, known_at
ranges:   id, tf, family, L*, H*, origin_side, known_at, state_history[(t, state)]
decisions:t, candidate_set, primary_range_id, p, LRI, gates, poi_id, action
```

Mọi phép join trong backtest đều phải có điều kiện `known_at ≤ t_decision`.

---

## 6. Ví dụ chart

> [!info] Ví dụ trong v0.2 là dữ liệu thật, dựng bằng thuật toán
> Mọi chart ở mục này (và Real 3–5 ở §4, §5) dựng từ OHLC thật EURUSD H1 (04/2017 → 02/2018) bằng đúng quy tắc của §19.3: swing = Directional Change θ = 2·ATR14; leg DR = origin của BOS (close vượt swing đã xác nhận) → termination; ACTIVE khi nhịp hồi ≥ 2·ATR. Không có bước nào chọn tay. Vùng mờ trên chart = dữ liệu *sau* thời điểm quyết định T2 — tại T2 bạn không thấy nó. Giờ trên trục là giờ theo dữ liệu. Các case *giả định* có cấu trúc T0–T5 ở [[#17.1. Case Studies|§17.1]].

### Ví dụ đúng — Bullish leg DR, retrace vào OTE, EXTENDED (Real 1)

![[Dealing-Range-v02-Real-01-EURUSD-H1-Leg-DR-OTE-Extended.png|1516]]
*Hình (dữ liệu thật): EURUSD H1 31/05 → 02/06/2017. Origin 1.11700 → termination 1.12566 (W ≈ 6.0 ATR). Chấm tím = thời điểm swing được xác nhận (known_at).*

**Tái dựng ex-ante (chỉ dùng thông tin có tại từng thời điểm):**
- **T0 (31/05 07:00):** swing high 1.11970 đã được xác nhận — đây là swing sẽ bị phá. Chưa có range.
- **T1 (31/05 10:00):** close vượt 1.11970 → **BOS**. Origin = đáy nhịp hồi trước break: 1.11700. Range ở state **FORMING** — termination còn chạy, p ≈ 1, *không đo location*.
- **T2 (01/06 06:00):** từ đỉnh 1.12566 giá hồi ≥ 2·ATR → termination đóng, range **ACTIVE**. EQ = 1.12133, OTE (p 0.21–0.38) = 1.11882–1.12029. Đây là thời điểm đầu tiên được phép nói "discount".
- **T3 (01/06 12:00):** đáy sâu nhất của nhịp hồi 1.12023 — p ≈ 0.37, chạm mép trên của OTE.
- **T4 (02/06 12:00):** close vượt swing high nội bộ → **EXTENDED** (BOS cùng chiều; range cũ hoàn thành vai trò).

**Vì sao đây là ví dụ "đúng" về *quy trình*:** anchor có hệ quả cấu trúc (origin của BOS), range chỉ được dùng sau khi ACTIVE, location đo trên đúng leg đang chi phối, invalidation viết được trước (close dưới 1.11700 hoặc MSS ngược cùng scale).

**Vì sao nó *không* phải bằng chứng:** đây là 1 trong 183 leg DR của chuỗi EURUSD H1 này; tỷ lệ EXTENDED toàn mẫu là 0.53, và trên random walk cùng độ biến động, P(EXTENDED | nhịp hồi sâu nhất nằm trong OTE) ≈ 0.50 (§5.2.2, §19.3). "Hình đẹp" không phân biệt được với may mắn.

### Ví dụ sai / dễ nhầm — Cùng quy trình, cùng vị trí OTE, kết cục ngược lại (Real 2)

![[Dealing-Range-v02-Real-02-EURUSD-H1-OTE-Then-Reversed.png|1516]]
*Hình (dữ liệu thật): EURUSD H1 24/04 → 27/04/2017. Origin 1.08209 → termination 1.09508 (W ≈ 9.7 ATR). Nhịp hồi chạm p ≈ 0.27 (giữa OTE) rồi REVERSED.*

**Tái dựng ex-ante:** BOS lúc 25/04 14:00 (close vượt 1.09063); range ACTIVE lúc 26/04 06:00; nhịp hồi xuống 1.08558 lúc 26/04 15:00 — p ≈ 0.27, *đẹp hơn* Real 1 theo mọi tiêu chí OTE. Ngày 27/04 13:00, close 1.08622 phá swing low nội bộ → **REVERSED**, trong khi origin 1.08209 **chưa hề bị chạm**.

**Bài học:**
1. **Vị trí trong range không phân biệt được Real 1 với Real 2 tại thời điểm quyết định.** Nếu có thứ phân biệt được, nó phải là thông tin *khác* location: direction của parent, trigger LTF, DOL — và chính những thứ đó mới là thứ cần test.
2. **Thất bại hiện ra dưới dạng MSS ngược chiều trên origin**, không phải "phá origin". Stop đặt "dưới origin cho chắc" chịu rủi ro lớn hơn cần thiết khi câu chuyện đã chết ở swing nội bộ (§5.2.2).
3. Lỗi kinh điển "chọn range quá nhỏ → tưởng discount nhưng thực ra premium" có phiên bản dữ liệu thật ở [[#4.4. Bài toán quá nhiều range và LRI|§4.4]] (Real 4): tại cùng một bar, bốn định nghĩa range hợp lệ cho bốn câu trả lời.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[27-Premium-Discount]] · [[26-OTE-Optimal-Trade-Entry|Optimal Trade Entry]] · [[10-Consequent-Encroachment-Mean-Threshold|Consequent Encroachment]]
- [[19-Liquidity]] · [[19-Liquidity#7. Buy-Side Liquidity (BSL)|Buy-side Liquidity]] · [[19-Liquidity#8. Sell-Side Liquidity (SSL)|Sell-side Liquidity]] · [[20-Liquidity-Sweep|Liquidity Sweep]] · [[16-Internal-External-Range-Liquidity-IRL-ERL|IRL ↔ ERL]]
- [[05-BOS-Break-of-Structure|Break of Structure]] · [[21-Market-Structure-Shift|Market Structure Shift]] · [[50-Displacement-In-Depth|Displacement]]
- [[13-FVG-Fair-Value-Gap|Fair Value Gap]] · [[25-OB-Order-Block|Order Block]] · [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest|OB selection hierarchy]]
- [[59-Daily-Bias]] · [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence|DOL SOP]] · [[01 - ICT 2022 Model|ICT 2022 Model]]

### 7.1. Sequence mẫu (v0.2)

Mỗi bước có **vai trò** riêng — location (DR), evidence (PD array), trigger (LTF), direction (HTF). Không bước nào thay được bước khác.

```text
LONG theo bullish leg DR
D1 GATE: direction BULL, protected low còn sống, DOL phía trên xác định       [direction]
→ H1 leg DR ở state ACTIVE; ghi origin / termination / known_at / LRI          [frame]
→ Giá vào nửa origin (discount) của H1 DR, không vi phạm parent (R3)          [location filter]
→ POI: bullish FVG / OB tại discount, còn unmitigated                          [evidence]
→ M5: sweep liquidity nội bộ (nếu model yêu cầu) → MSS → displacement → FVG  [trigger]
→ Entry tại FVG M5 | Stop: dưới swing M5 bảo vệ (trong khuôn khổ H1 protected)
→ Target: IRL đối diện trước → ERL / DOL sau
→ Ghi journal: range_state, p_entry, LRI, nesting_relation, h1_gate, sweep_origin_flag
→ Hết hiệu lực khi: MSS ngược cùng scale H1 (thường xảy ra TRƯỚC khi chạm origin)
```

```text
SHORT theo bearish leg DR — đối xứng
D1 GATE: direction BEAR → H1 bearish leg DR ACTIVE → giá vào nửa origin (premium)
→ bearish FVG / OB tại premium → M5 sweep BSL nội bộ → MSS → displacement → FVG
→ Entry | Stop trên swing M5 bảo vệ | Target: IRL đối diện → SSL / DOL
→ Hết hiệu lực khi: MSS tăng cùng scale H1
```

> [!note] Điều thay đổi so với sequence cũ
> 1. **"Đáy range đã sweep SSL" không còn là điều kiện bắt buộc** — đó là supporting evidence (HYP-DR-007). Điều kiện bắt buộc là *structural consequence* và state ACTIVE.
> 2. **Sweep protected origin trong lúc chờ entry là cờ cảnh báo**, không phải "tín hiệu đẹp hơn" — cần trigger theo hướng leg (§5.4.3).
> 3. Location chỉ là **filter**: trên dữ liệu v0.2, vào lệnh "ở discount" mà không có thông tin hướng/trigger cho P/W ≈ 0 ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]]). Mọi giá trị của sequence này (nếu có) đến từ direction và trigger — đó là những gì cần backtest.

### 7.2. Displacement / FVG / OB / POI Relationship

#### 7.2.1 Displacement và range

- **Tạo range:** displacement là cơ chế tạo ra leg; leg tạo ra termination; BOS do displacement tạo ra biến swing low xuất phát thành protected. Không có displacement → leg chậm, nhiều overlap → origin thường mơ hồ.
- **Xác nhận significance:** swing khởi động displacement có điểm D cao (mục 3.3.2). [HYPOTHESIS] swing như vậy "bền" hơn (xác suất bị phá thấp hơn trong k bar) — HYP-DR-006.
- **Invalidate range:** displacement ngược chiều xuyên protected anchor là dạng invalidation mạnh nhất (mục 5.1).
- **Origin nên ở đâu?** Anchor là **extreme giá** (wick low) của swing, không phải candle trước displacement (Order Block). OB là một **POI nằm gần origin** — thường ở deep discount của leg DR. Trộn hai khái niệm dẫn tới vẽ range lệch (dùng open của OB làm anchor thay vì low).

#### 7.2.2 DR + FVG

FVG trong displacement leg là IRL bên trong leg DR mới. Vị trí p của FVG xác định nó là "discount FVG" hay "premium FVG". Trong ICT 2022 Model: FVG tạo bởi displacement sau MSS, nằm ở discount (bullish) của leg vừa tạo — là execution PD array. [ICT FRAMEWORK]

#### 7.2.3 DR + OB

OB gần origin → p nhỏ (deep discount, gần protected low). R:R đến termination cao, nhưng stop gần vùng SSL (mục 14.6.4). DR giúp xếp hạng các OB: OB ở discount của *cả* leg DR và parent DR xếp trên OB chỉ ở discount của leg DR (hypothesis HYP-DR-004 dạng POI).

#### 7.2.4 DR có xác định POI không?

**Không.** POI (FVG, OB, Breaker, …) là đặc điểm của price action *tồn tại độc lập* với range. DR là **bộ lọc và bộ xếp hạng** POI theo location. Bảng phân vai:

| Thành phần | Trả lời | Công cụ | Timeframe chính |
|---|---|---|---|
| **Location** | *Ở đâu* hành động là hợp lý về giá? | Dealing Range, P/D, OTE | D1, H1 |
| **Evidence** | *Có gì* ở đó ủng hộ hành động? | PD arrays (FVG, OB, Breaker…), liquidity đã lấy | H1 |
| **Trigger** | *Khi nào* hành động? | Sweep → MSS → displacement → FVG | M5 |

Một trade cần cả ba. DR chỉ cung cấp phần đầu.

### 7.3. Decision tree

![[Dealing-Range-v01-19-Decision-Tree.svg|1516]]
*Sơ đồ: decision tree từ D1 structure đến D1 GATE; mỗi nhánh NO là một kết luận hợp lệ.*

**Phê phán từng bước (những chỗ còn yếu):**

| Bước | Điểm yếu | Mức độ | Hướng cải thiện |
|---|---|---|---|
| [1] | Direction D1 có thể UNDEFINED lâu; quy tắc chuyển trạng thái phụ thuộc break rule | Cao | Test nhiều break rule; đo thời gian UNDEFINED |
| [3] | θ\* phụ thuộc lưới threshold | Trung bình | Kiểm tra độ nhạy lưới |
| [5] | Termination "đóng" cần θ → lag lớn trong leg nhanh | Trung bình | Chấp nhận lag; đó là cái giá của no-hindsight |
| [9] | DOL selection vẫn còn nhiều discretion | **Cao** | Cần research riêng (05_DOL) |
| [10] | LRI threshold tùy ý; weights bằng nhau | Trung bình | Test LRI như một feature liên tục |
| [11] | "Mâu thuẫn mạnh" chưa định nghĩa | Trung bình | Dùng p_parent làm biến liên tục |
| [12] | Relevance có nhiều tham số (c1, M_max, x) | Trung bình | Ablation |
| [15] | Dễ bị lạm dụng để "vẽ lại" | **Cao** | Log mọi thay đổi + lý do bằng event id |

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Range đúng là điều kiện tiên quyết cho *kỷ luật vị trí*; nó không phải lý do vào lệnh. Mỗi dòng dưới đây ứng với một gate — fail một gate bắt buộc = không có lệnh.

### A. Context — D1 GATE (xác định range & hướng)
- [ ] Direction D1 xác định (BULL/BEAR) với protected anchor còn sống — **ghi giá**.
- [ ] D1 leg DR ở state ACTIVE: origin / termination / known_at / θ\* đã ghi.
- [ ] External liquidity hai phía đã đánh dấu; DOL ứng viên có lý do (timeframe, chưa bị lấy, path).
- [ ] LRI trên các candidate D1 đã tính; nếu thấp → ghi `location_conflict = TRUE` và áp dụng nhánh AMBIGUOUS.
- [ ] Không có cảnh báo dữ liệu: anchor không phải news spike / data artifact; feed đúng (futures gốc cho index).
- [ ] D1 GATE = PASS (AMBIGUOUS → chỉ log research hoặc size giảm theo playbook).

### B. Setup — H1 GATE
- [ ] H1 leg DR ACTIVE, nested trong D1 (consistent hay conflicting — đã ghi `nesting_relation`).
- [ ] POI nằm ở nửa origin của H1 DR **và** không vi phạm parent constraint (R3).
- [ ] Không có cờ SWEPT_L chưa xử lý (origin H1 vừa bị sweep mà chưa có trigger theo hướng leg).
- [ ] Range đủ rộng: W_H1 ≥ c1 × stop dự kiến (HEURISTIC c1 = 2); M_ratio đến DOL hợp lý.
- [ ] H1 GATE = PASS.

### C. Execution — M5 GATE
- [ ] Giá đã chạm POI H1 hợp lệ.
- [ ] Liquidity event (nếu model yêu cầu) → MSS phá swing M5 có ý nghĩa với nhịp hồi H1 → displacement → FVG.
- [ ] Stop theo cấu trúc M5, nằm trong khuôn khổ protected H1; R tới DOL ≥ kế hoạch.
- [ ] Không có tin cấp cao trong cửa sổ ±10 phút (Case 2).
- [ ] Invalidation viết ra **trước** khi vào lệnh: mức giá + event (MSS ngược cùng scale H1).

### D. Quy tắc "không có lệnh"
- [ ] Không ghi được origin / termination / state → không trade.
- [ ] Range FORMING, CONSOLIDATING hoặc đang location blackout → không trade location model.
- [ ] Giá quanh EQ (dải 40–60% — HEURISTIC) → không mở lệnh mới, trừ playbook continuation có trigger riêng.
- [ ] Premium/discount đo trên range sai scale → dừng, vẽ lại theo rule trước khi xét lệnh.

### Best practices (đã hiệu chỉnh theo v0.2)

> [!success] Best practices
> 1. **Vẽ range trước POI — nhưng vẽ structure trước range.** Swings → θ\* → anchors → DR → POI. Đảo thứ tự là lập luận vòng tròn.
> 2. **Mỗi range phải trả lời "origin nào, known_at khi nào, state gì?"** — không trả lời được = range chọn theo cảm tính. ("Hai đầu đã lấy liquidity nào?" là câu hỏi phụ, không phải tiêu chí định nghĩa.)
> 3. **Quadrant / OTE là cách mô tả vị trí, không phải thang conviction.** Dữ liệu v0.2 không cho thấy bin sâu hơn có P/W cao hơn ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]]).
> 4. **Ghi hai tầng vị trí vào journal** (`p_htf`, `p_ltf`, `nesting_relation`) — để chính dữ liệu của bạn trả lời HYP-DR-004, không phải niềm tin.
> 5. **Phân xử sweep vs acceptance bằng rule viết trước**, và coi sweep protected origin là cờ cảnh báo (§5.4).
> 6. **Quanh EQ = không làm gì** (HEURISTIC, giữ vì giảm chop, không vì có bằng chứng EQ là level đặc biệt).
> 7. **Khi hết external liquidity phía trước, dùng SD projection** ([[#14.9. Range projection — Standard Deviation|§14.9]]) — target phải là một mức đo được.
> 8. **Audit range cuối phiên:** state nào đổi, event id nào xảy ra; ghi vào daily note để sáng hôm sau không phân tích lại từ đầu — và đo lại levels mỗi sáng (W4).

---

## 9. Lỗi thường gặp

![[Dealing-Range-Sec-09-Loi-Thuong-Gap.svg|1516]]
*Sơ đồ: các lỗi phổ biến khi chọn Dealing Range — range quá nhỏ, sai timeframe, không vẽ lại, và cách sửa.*

Bảng gộp lỗi thực hành (bản concept cũ) và failure modes (v0.1) — mỗi lỗi chỉ xuất hiện một lần.

| # | Lỗi | Dấu hiệu | Vì sao sai | Cách sửa |
|---|---|---|---|---|
| 1 | **Chọn swing bằng hindsight** | Swing "hiển nhiên" chỉ sau khi thấy kết quả | Dùng thông tin chưa tồn tại tại thời điểm quyết định | `known_at` cho mọi anchor; blind protocol (§5.5) |
| 2 | **Đổi anchor sau khi biết outcome** | "Lệnh thua vì vẽ sai range" | Biến mọi thua lỗ thành lỗi vẽ → không bao giờ học được | Rule freeze + log mọi thay đổi có event id |
| 3 | **Chọn range để hợp bias** | Range luôn ủng hộ hướng đã muốn | Confirmation bias; fractal luôn có một range ủng hộ bất kỳ hướng nào | Candidate set cố định; LRI (§4.4) |
| 4 | **Range quá nhỏ** | Hai swing nhỏ gần giá | Stop lớn hơn range → location vô nghĩa; dễ "discount" giả | W ≥ c1 × stop; leo lên parent |
| 5 | **Range quá rộng** | EQ cách xa vùng giá hoạt động | Location thô; "discount" vẫn cách đáy rất xa (W3) | Child range; quadrant + PD array cụ thể |
| 6 | **Range quá cũ / stale** | Range đã hết vai trò vẫn dùng vì quen | Tọa độ không phản ánh định giá hiện tại | Temporal/context invalidation (CX-24) |
| 7 | **Đo trên sai scale** | Range M5 để kết luận bias D1 | Vị trí mâu thuẫn HTF; ý nghĩa thuộc swing bị phá | Bias trên range của scale quyết định; R7 |
| 8 | **Đo trên range FORMING** | "Discount" khi termination chưa đóng | p ≈ 1 thực tế; hindsight biến premium thành discount (CX-03) | Chỉ đo khi ACTIVE |
| 9 | **Không vẽ lại sau event** | Vẫn dùng range sau BOS cùng chiều / MSS ngược | Range "chết" cho DOL và location sai | Cập nhật theo Scenario A–I (§5.3) |
| 10 | **Liên tục vẽ lại range** | Mỗi wick một range mới | Tọa độ không ổn định, không đo được | Update chỉ theo event; sweep ≠ re-map |
| 11 | **Coi sweep origin là xác nhận** | "Vừa quét SSL dưới origin → long mạnh" | Base-rate continuation sau sweep ~0.25 trên dữ liệu v0.2 | Cần trigger LTF theo hướng leg (HYP-DR-014) |
| 12 | **Lẫn internal với external** | Coi FVG bên trong là target chính | Internal/external là quan hệ với một range cụ thể | Gắn nhãn sau khi dựng range |
| 13 | **Coi mọi swing như nhau** | Mọi đỉnh/đáy đều là "liquidity" | Random walk tạo ~35 fractal high / 250 bar | θ\* + consequence filter (§3.2–3.3) |
| 14 | **P/D = vùng đảo chiều tự động** | "Discount nên sẽ lên" | Martingale null: E[R] = 0 ở mọi vị trí | Location chỉ là filter; direction phải đến từ chỗ khác |
| 15 | **EQ = support/resistance ma thuật** | Đặt lệnh chờ đúng 50% | EQ là trung điểm hình học | Test EQ vs mức ngẫu nhiên (HYP-DR-005) |
| 16 | **Mua/bán quanh EQ** | Vào lệnh giữa range | R:R ≈ 1:1 tới boundary, dễ chop | Dải 40–60% = chờ (HEURISTIC) |
| 17 | **Bỏ qua HTF** | M5/H1 noise override D1 | Child không phủ quyết parent | R1, R7; D1 GATE |
| 18 | **Bỏ qua liquidity quanh stop** | Stop nằm ngay trong pool SSL hiển nhiên | Stop dễ bị sweep | Buffer; hoặc chờ sweep + trigger |
| 19 | **Bỏ qua DOL / room** | Location đẹp nhưng DOL quá gần | Không đủ R | M_ratio; min R đến DOL |
| 20 | **Đo OTE trên range sai** | Fib 62–79% trên range không hợp lệ | OTE chỉ là tọa độ của range đã chọn | OTE chỉ tính trên leg DR ACTIVE |
| 21 | **Nhầm mô tả với dự báo** | "Framework giải thích được mọi chart" | Mô tả tốt ≠ edge | Baseline + null so sánh (§19) |
| 22 | **Overfit anchor selection / candle-count tùy tiện** | Tối ưu θ, k, m trên cùng dữ liệu; "3 nến ngoài = invalid" | Garden of forking paths | Walk-forward, OOS, plateau; dán nhãn HEURISTIC |
| 23 | **Đo bằng MEHR trên dữ liệu rời rạc mà không có null** | "Discount có excess hit rate +8%" | Gradient MEHR có cả trên random walk (§19.3) | Dùng P/W hoặc MEHR − MEHR_null cùng cách theo dõi |

---

## 10. Câu hỏi tự kiểm tra

**Trước mỗi phiên:**
- Range tôi đang dùng thuộc họ nào (leg / container / lookback), scale nào, origin – termination – known_at – state là gì?
- Origin có structural consequence không — từ nó giá đã close vượt swing đối diện cùng cấp chưa?
- Giá đang ở premium / discount / EQ **của range nào** — và các candidate khác nói gì (LRI)?
- External liquidity nào còn mở? DOL ứng viên nào, vì sao phía đó chứ không phải phía kia?
- Range này hết hiệu lực ở mức giá nào, bằng event nào? (Viết ra.)
- Parent nói gì — tôi có đang mua discount của child trong premium của parent (CX-12)?
- Range đang FORMING hay ACTIVE? Nếu FORMING, tại sao tôi lại đang đo location?

**Sau mỗi lệnh / mỗi review:**
- Tôi có đổi anchor sau khi thấy giá đi không? Nếu có — đó là hindsight, ghi lại như một lỗi.
- Nếu lệnh thua, tôi có tiêu chí invalidation viết trước, hay đang đổ cho "thiếu confluence" theo cách không kiểm chứng được?
- Lệnh này vào lúc origin vừa bị sweep không? Có trigger theo hướng leg không?
- EQ hiện tại đã bị test bao nhiêu lần — tôi có đang tin vào một mức đã "mòn"?
- Range có rộng/hẹp bất thường so với ADR trong tuần có lịch đặc biệt không?
- Kết quả của lệnh này có khác gì một lệnh cùng bracket trên random walk không — và tôi biết điều đó bằng cách nào?

**Ba câu hỏi chẩn đoán (từ v0.1):**

1. Giá đang ở p = 0.30 của H1 leg DR và p = 0.72 của D1 leg DR, D1 BULL, DOL D1 cách giá 0.4×W_D1. Theo R1–R7, setup long có được phép không, và biến nào bạn phải ghi vào journal?
2. Một hệ thống có win rate 45% với target 1R. MEHR của nó là bao nhiêu, và nó tốt hơn hay tệ hơn ngẫu nhiên?
3. Tại sao một range ở state FORMING luôn cho p gần 1 — và điều đó nói gì về các "discount entry" mà bạn thấy trên chart đã chạy xong?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Dealing Range là gì (một câu, phiên bản cấu trúc)?
**Đáp:** Hệ tọa độ neo vào hai swing đối nghịch có quan hệ cấu trúc — origin (protected, điểm invalidation) và termination của leg vừa tạo BOS/MSS — dùng để đo vị trí giá (p), phân vùng liquidity internal/external và định nghĩa invalidation.

### Q2
**Hỏi:** Dealing Range dùng để làm gì — và *không* dùng để làm gì?
**Đáp:** Dùng để: đo location (premium/discount/EQ/OTE), chia IRL/ERL, khung cho DOL, đặt invalidation. Không dùng để: quyết định hướng ("discount nên sẽ lên") hay làm trigger vào lệnh.

### Q3
**Hỏi:** Internal vs external — thuộc tính hay quan hệ?
**Đáp:** Quan hệ. Một swing chỉ internal/external *so với một range cụ thể*. Còn micro → HTF là trục scale — độc lập với trục role.

### Q4
**Hỏi:** Chọn anchor theo tiêu chí gì?
**Đáp:** Structural consequence: origin = cực trị nhịp hồi trước khi giá close vượt swing đối diện cùng cấp; termination = cực trị của leg đó sau khi đóng bằng nhịp hồi ≥ θ·ATR. Mỗi anchor có `known_at`. Sweep liquidity tại origin là bằng chứng phụ, không phải điều kiện.

### Q5
**Hỏi:** Khi nào phải vẽ lại range?
**Đáp:** Theo event: BOS cùng chiều (EXTENDED — completion), MSS ngược chiều cùng scale (REVERSED), close xuyên origin + acceptance (INVALIDATED), chuyển consolidation, parent đổi trạng thái. Wick xuyên rồi close lại = SWEPT, không vẽ lại.

### Q6
**Hỏi:** Vì sao chọn sai range nguy hiểm — và vì sao chọn đúng range vẫn chưa đủ?
**Đáp:** Sai range → mọi tọa độ sai (mua premium tưởng discount). Nhưng đúng range không tạo edge: dưới martingale E[R] = 0 ở mọi vị trí; edge phải đến từ direction/trigger độc lập.

### Q7
**Hỏi:** Quan hệ giữa Dealing Range và Daily Bias?
**Đáp:** DR cung cấp location và protected anchor; bias là directional hypothesis kết hợp structure + DOL + location. Directional bias ≠ DOL ≠ setup ≠ entry direction — bốn thứ liên quan nhưng khác nhau.

### Q8
**Hỏi:** Martingale null nói gì về "mua discount"?
**Đáp:** Với stop ở L\*, target ở H\*, entry ở p: dưới martingale P(thắng) = p, R:R = (1 − p)/p ⇒ E[R] = 0 tại mọi p. Discount cho R:R cao hơn nhưng xác suất thắng thấp hơn đúng bằng tỷ lệ bù trừ. Location chỉ *khuếch đại* drift có sẵn.

### Q9
**Hỏi:** Vì sao không được đo edge vị trí bằng MEHR thô trên dữ liệu thực?
**Đáp:** Vì theo dõi rời rạc (bar, gap, close-only) làm hit-rate lệch khỏi p theo vị trí — gradient "discount tốt hơn" xuất hiện cả trên random walk. Phải dùng P/W (lãi lỗ thực hiện) hoặc trừ MEHR của null cùng cách theo dõi.

### Q10
**Hỏi:** Origin của bullish leg DR vừa bị wick xuyên rồi close lại trong range. Đọc thế nào?
**Đáp:** State = SWEPT_L, range chưa invalid. Nhưng đây là cờ cảnh báo: trên dữ liệu v0.2, P(EXTENDED | sweep origin) ≈ 0.24–0.28 so với ≈ 0.58 khi không sweep. Chỉ theo hướng leg nếu có trigger LTF (MSS + displacement theo hướng leg).

### Q11
**Hỏi:** LRI là gì và vì sao LRI thấp là "bình thường"?
**Đáp:** Location Robustness Index — tỷ lệ candidate range hợp lệ đồng thuận về phía premium/discount. Trên dữ liệu thật, bốn định nghĩa chỉ đồng thuận ở 54–70% số bar — bằng random walk. Bất đồng là thuộc tính hình học của định nghĩa, không phải tín hiệu thị trường.

### Q12
**Hỏi:** Một leg DR thường "chết" theo cách nào?
**Đáp:** Gần như luôn bằng MSS ngược chiều cùng scale (REVERSED) — khoảng một nửa trong số đó khi origin còn nguyên. Close xuyên origin mà chưa có MSS trước (INVALIDATED thuần) chỉ ~1%. Mức invalidation vận hành = swing được xác nhận gần nhất cùng scale.

---

## 12. Lesson Learned

### Bài học chính
- Dealing Range là **khung tham chiếu**, không phải tín hiệu vào lệnh; nhưng không có khung đúng thì mọi tín hiệu khác bị đo sai.
- Premium/discount và OTE là **tọa độ** — chọn sai range là sai từ gốc. Nhưng chọn đúng range **không** tạo edge: trên dữ liệu v0.2, vị trí trong leg DR cho P/W ≈ 0, và anchor cấu trúc không tốt hơn IPDA-20 hay anchor ngẫu nhiên một cách nhất quán.
- Anchor quan trọng vì **hệ quả**, không vì hình dạng; mọi anchor có `known_at`; range FORMING không có location.
- Range có **vòng đời**: sweep ≠ invalidation, completion ≠ invalidation; và range thường chết bằng MSS ngược chiều *trên* origin.
- **Sweep protected origin là cờ cảnh báo**, không phải phần thưởng — cần trigger theo hướng leg.
- Gần một nửa thời gian, "giá đang ở discount" phụ thuộc vào định nghĩa range nhiều hơn vào giá (LRI). "Không biết" là câu trả lời hợp lệ.
- Thước đo phải được kiểm tra trước khi tin kết quả: MEHR thô trên dữ liệu rời rạc tạo ra "edge" giả theo vị trí.

### Quy tắc cá nhân rút ra
- [ ] Tôi không đo premium/discount trước khi ghi origin / termination / known_at / state của range.
- [ ] Tôi không Long ở nửa termination / Short ở nửa origin của range đang chi phối; quanh EQ thì chờ.
- [ ] Tôi không coi location là lý do vào lệnh; mỗi lệnh phải ghi rõ nguồn direction và trigger.
- [ ] Khi origin vừa bị sweep, tôi giảm size hoặc chờ trigger LTF theo hướng leg; tôi không gọi đó là "setup đẹp hơn".
- [ ] Tôi đặt invalidation ở MSS ngược cùng scale (swing xác nhận gần nhất), không chỉ ở origin.
- [ ] Tôi không dùng range M5 để kết luận bias HTF.
- [ ] Tôi không đổi anchor sau khi thấy giá — mọi thay đổi có event id.

### Câu nhắc nhở khi trade
> **"Range sai thì discount cũng là premium. Range đúng thì discount vẫn chỉ là tọa độ — edge phải đến từ hướng và trigger."**

### 12.4. Mô hình tư duy cuối cùng

#### 12.4.1 Mô hình trong một hình

```text
                   ┌─────────────────────────────────────────────┐
                   │  DIRECTION (nguồn edge — nếu có)             │
                   │  D1 structure, protected anchor, DOL         │
                   └───────────────────────┬─────────────────────┘
                                           │ drift có điều kiện?
                                           ▼
 SWINGS ─► θ*, role(t) ─► ANCHORS ─► DEALING RANGE (frame, state) ─► LOCATION p
   (known_at)                          │                               │
                                       │                               ▼
                               LIQUIDITY MAP                    AMPLIFIER: R-geometry
                               (internal / external)           (vô dụng nếu không có drift)
                                       │                               │
                                       └──────────► EVIDENCE (PD arrays tại location)
                                                              │
                                                              ▼
                                                     TRIGGER (M5) ─► TRADE
```

#### 12.4.2 Mười hai nguyên tắc

1. **DR là thước, không phải lực.** Nó đo; nó không đẩy.
2. **Anchor quan trọng vì hệ quả, không vì hình dạng.** Origin = protected = invalidation.
3. **Mọi anchor có known_at.** Không có known_at, không có backtest.
4. **Ba họ range, ba câu hỏi.** Leg (pullback sâu đến đâu), Container (liquidity hai phía), Lookback (baseline khách quan).
5. **Internal/external là quan hệ; micro/HTF là kích thước.** Đừng trộn.
6. **Premium/discount không có nghĩa nếu không có range và direction.**
7. **Location khuếch đại; direction tạo ra.** Dưới martingale, không vị trí nào có edge.
8. **Sweep ≠ invalidation; completion ≠ invalidation.** Dùng state machine.
9. **Ý nghĩa thuộc về swing bị phá, không thuộc về chart bạn đang nhìn.** H1 không override D1 trừ khi phá swing cấp D1.
10. **Tính location trên mọi candidate hợp lệ.** LRI thấp = không biết — và "không biết" là câu trả lời hợp lệ.
11. **Cập nhật range theo event, không theo cảm giác.** Mọi thay đổi có event id.
12. **Cấu trúc tồn tại cả trong ngẫu nhiên.** Chứng minh vượt baseline trước khi tin.

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt ba họ range, internal/external là quan hệ, DR là tọa độ không phải lực? |
| Nhận diện trên chart |  | Chọn origin theo structural consequence, ghi known_at, chỉ đo khi ACTIVE? |
| Biết khi nào bỏ qua |  | Nhận ra FORMING / LRI thấp / sweep origin chưa có trigger / sai scale? |
| Kết hợp với context HTF |  | Ghi nesting_relation; áp dụng R1–R7; không để child phủ quyết parent? |
| Áp dụng vào trade thực tế |  | Mỗi lệnh có nguồn direction + trigger tách khỏi location? Invalidation viết trước? |
| Review sau trade |  | Ghi range_state, p_entry, LRI, sweep_origin_flag; so với null/baseline? |
| Hiểu bằng chứng |  | Giải thích được martingale null, artifact MEHR, kết quả §19.3 cho người khác? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập tối thiểu 30 setup có tag `[[Dealing Range]]` với đủ field journal ở §18.4.
- [ ] Tách thống kê theo `range_state_at_entry`, `nesting_relation`, `sweep_origin_flag`, LRI bin.
- [ ] So sánh R thực tế của nhóm "discount" với nhóm cùng bracket nhưng vị trí ngẫu nhiên (baseline cá nhân).
- [ ] Chạy lại nghiên cứu §19.3 trên NQ / XAUUSD / EURUSD intraday có phí — chỉ cập nhật rule khi đủ mẫu.

---

## 14. Cơ chế thị trường & các lăng kính diễn giải

Mục này trả lời câu hỏi *"vì sao Dealing Range có vẻ hoạt động?"* ở ba tầng: điều quan sát được (OHLC), cơ chế thị trường có bằng chứng, và diễn giải ICT. Nguyên tắc diễn đạt: mỗi sự kiện tách thành OBSERVABLE / ICT READING / MECHANISM / UNKNOWN ([[#14.1. Market Mechanics vs ICT Interpretation|§14.1]]).

### 14.1. Market Mechanics vs ICT Interpretation

#### 14.1.1 Bảng phân tách claim

| Claim | Loại | Có thể quan sát từ OHLC? | Ghi chú |
|---|---|---|---|
| Giá tạo ra một swing high | [MARKET MECHANICS] quan sát | Có | Fact |
| Swing high đó là "buy-side liquidity" | [ICT FRAMEWORK] | Không | Giả định có buy stops phía trên |
| Lệnh chờ tập trung quanh mức giá "hiển nhiên" | [MARKET MECHANICS] có bằng chứng | Không (cần order data) | Osler (2003): trên thị trường FX, stop-loss và take-profit order tập trung mạnh tại số tròn, với pattern khác nhau giữa hai loại — giải thích vì sao trend hay đảo chiều tại S/R và tăng tốc khi S/R bị phá |
| Stop-loss orders có thể tạo price cascade | [MARKET MECHANICS] có bằng chứng | Gián tiếp (tốc độ/extension sau break) | Osler (2005), NY Fed Staff Report 150 |
| Lệnh tập trung đặc biệt phía trên *swing high* (không phải số tròn) | [INTERPRETATION] | Không | Hợp lý (breakout traders, stop của short) nhưng bằng chứng trực tiếp yếu hơn so với số tròn |
| "Smart Money tạo ra range để engineer liquidity" | Speculative narrative | Không | Không thể suy ra ý định từ giá |
| Giá sẽ quay về EQ | [HYPOTHESIS] | Kiểm chứng được | Cần so với martingale baseline |
| Giá di chuyển IRL → ERL → IRL | [ICT FRAMEWORK] → [HYPOTHESIS] | Kiểm chứng được nếu formalize | Luôn đúng *một cách hời hợt* vì giá phải đi qua bên trong range để đến boundary |
| Discount tạo bullish reversal | [HYPOTHESIS] | Kiểm chứng được | Dưới martingale: không |

#### 14.1.2 "Liquidity" — hai nghĩa khác nhau

- **Nghĩa microstructure:** khả năng giao dịch một khối lượng lớn với price impact thấp — gồm tightness (spread), depth (khối lượng ở mỗi mức), resiliency (tốc độ phục hồi). (Kyle, 1985.)
- **Nghĩa ICT:** các lệnh chờ (chủ yếu stop orders) nằm tại những mức giá có thể đoán được, sẽ biến thành market orders khi bị chạm.

Hai nghĩa có liên hệ: một participant muốn **mua khối lượng lớn** cần **người bán**. Sell-stop orders dưới một swing low, khi bị kích hoạt, trở thành market sell orders — tức là nguồn cung mà người mua lớn có thể khớp vào. **[MARKET MECHANICS]** Logic "cần counterparty" là đúng. **[INTERPRETATION]** Việc *một ai đó cố ý* đẩy giá xuống dưới low để lấy nguồn cung đó là một diễn giải — không thể quan sát trên chart. Một giải thích thay thế hoàn toàn khả dĩ: giá rơi xuống dưới low vì dòng bán tự nhiên, kích hoạt stop, cascade dừng lại khi hết stop, và người mua *sẵn có* (limit orders, value buyers) hấp thụ — không cần ai "săn".

#### 14.1.3 Giới hạn quan sát theo loại thị trường

- **FX spot:** thị trường OTC phi tập trung, không có consolidated order book công khai. Volume trên chart retail thường là tick volume của một nhà cung cấp.
- **Futures (NQ, ES, …):** có displayed order book (limit orders) — nhưng stop orders thường **không hiển thị** trong displayed book. Vì vậy ngay cả với dữ liệu tốt nhất, "stop liquidity" vẫn là suy luận.
- **Kết luận thực hành:** trong framework này, "liquidity tại boundary" luôn là một **latent variable** (biến ẩn). Ta chỉ quan sát được *hệ quả* khi giá chạm mức đó: tăng tốc (gợi ý stop cascade), từ chối (gợi ý absorption), hoặc không có gì đặc biệt (gợi ý không có tập trung lệnh đáng kể).

#### 14.1.4 Nguyên tắc diễn đạt trong note này

Mỗi khi mô tả một sự kiện, tôi sẽ tách ba lớp:

```text
OBSERVABLE:     Giá vượt swing low 1.0812 xuống 1.0798 rồi đóng cửa 1.0825.
ICT READING:    Sell-side liquidity dưới 1.0812 đã bị sweep.
MECHANISM:      Có thể đã có sell stops dưới 1.0812; nếu có, chúng đã được khớp.
UNKNOWN:        Có bao nhiêu stops, ai là người mua đối ứng, có chủ đích hay không.
```

### 14.2. Ba cơ chế thường được đưa ra để giải thích Dealing Range — và mức bằng chứng của từng cái

*(Gộp "W0 — tầng WHY nền tảng" và "14.1 — cơ chế orderflow" của bản cũ; mỗi cơ chế được gắn nhãn thay vì callout sửa sai.)*

**Cơ chế 1 — Range là bản đồ phân bố lệnh chờ.**
- *Lập luận:* hai đầu range là nơi tập trung stop (stop của vị thế ngược chiều + lệnh breakout); bên trong là các vùng giao dịch một chiều chưa "hoàn tất" (FVG/OB). Người cần khớp khối lượng lớn cần đối tác → giá bị hút về nơi có lệnh chờ dày. Xem [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]].
- *Phần có cơ sở* **[MARKET MECHANICS]:** logic "cần counterparty" đúng; stop orders có thể tạo price cascade (Osler 2005); lệnh tập trung mạnh ở số tròn trong FX (Osler 2003).
- *Phần là diễn giải* **[INTERPRETATION]:** lệnh tập trung đặc biệt *ngay trên swing high / dưới swing low* (thay vì số tròn) — hợp lý nhưng bằng chứng trực tiếp yếu hơn. Stop orders thường **không hiển thị** trong displayed order book của futures và FX spot không có order book hợp nhất → "thấy cụm stop trên DOM" là không chính xác; cụm stop là suy luận.
- *Null phải loại trước:* random walk cũng tạo swing, range và "sweep"; trên dữ liệu v0.2, tần suất sweep origin ở dữ liệu thật ≈ null (§5.4.3).

**Cơ chế 2 — EQ là "value", premium/discount là lợi thế đàm phán (Auction Market Theory).**
- *Lập luận:* hai đầu range là hai mức thị trường đã thử và từ chối; trung điểm là "giá công bằng tạm thời" — trên đó người bán có lợi thế vị trí, dưới đó người mua có lợi thế.
- *Phần có cơ sở* **[MARKET MECHANICS]:** balance/imbalance và "excess" ở rìa là khung lý thuyết đấu giá có thật (Steidlmayer; Dalton) — giải thích *vì sao boundary có thể quan trọng*.
- *Phần không khớp:* value area trong AMT được xác định bằng **phân phối volume/TPO** (POC), không phải trung điểm hình học của hai swing. EQ hình học chỉ trùng value khi phân phối đối xứng. Gọi EQ là "value area" là một phép xấp xỉ, không phải đồng nhất ([[#14.8. Alternative Interpretations|§14.8]]).
- *Kiểm chứng:* HYP-DR-005 (reaction tại EQ vs mức ngẫu nhiên) — UNTESTED. Câu hỏi nghiên cứu: EQ vs POC, mức nào có reaction nhiều hơn?

**Cơ chế 3 — Chu kỳ cân tồn kho (inventory) của dealer / thuật toán.**
- *Lập luận:* khớp khối lớn tại external (nơi đủ thanh khoản) để lại tồn kho lệch; giá được đưa về internal (FVG) để cân tồn kho, rồi mới bắt đầu chu kỳ mới — "nhịp thở" ERL ↔ IRL.
- *Mức bằng chứng:* **[INTERPRETATION] / speculative narrative.** Inventory models trong microstructure là có thật, nhưng việc suy ra chu kỳ tồn kho của *ai đó cụ thể* từ OHLC là không quan sát được. Dạng có thể test là HYP-DR-008 (IRL→ERL vượt martingale) — UNTESTED.
- *Claim đã rút lại:* "VWAP trong phần lớn phiên hội tụ quanh 45–55% dealing range trong ngày" (bản cũ) không có nguồn hay dataset → **[HYPOTHESIS] — BACKTEST REQUIRED**, không dùng làm lập luận.

> [!quote] Kết luận của mục 14.2
> Cả ba cơ chế đều *có thể* đúng một phần, và cả ba đều tạo ra cùng một dự báo kiểm chứng được: **hành vi tại boundary/EQ/FVG phải khác random walk cùng độ biến động**. Trên dữ liệu v0.2, hành vi *theo vị trí trong leg DR* không khác null một cách robust — nghĩa là, nếu các cơ chế này tồn tại, hiệu ứng của chúng không lộ ra qua location đơn thuần mà (nếu có) phải qua điều kiện khác: direction, trigger, loại boundary (số tròn, PDH/PDL), volume.

### 14.3. Equilibrium

#### 14.3.1 Ý nghĩa toán học

[MATHEMATICAL] EQ = (H\* + L\*)/2 — điểm duy nhất cách đều hai boundary. Nếu một lệnh nhắm vào boundary đối diện với stop ở boundary gần, tại EQ R:R = 1:1.

#### 14.3.2 Độ nhạy với anchor — EQ là một đại lượng *phái sinh*

$$\Delta EQ = \frac{\Delta H^* + \Delta L^*}{2}, \qquad \frac{\partial p}{\partial L^*} = -\frac{H^* - P}{W^2}, \qquad \frac{\partial p}{\partial H^*} = -\frac{P - L^*}{W^2}$$

Ví dụ: H\* = 110, L\* = 100, P = 104 → p = 0.40 (discount). Nếu anchor dưới được chọn là swing low trước đó, L\* = 96 → p = 8/14 = 0.57 (premium). **Dời một anchor 4 điểm (40% range) làm nhãn location đảo dấu.** sơ đồ v01-03 minh họa cùng một mức giá được gán ba nhãn khác nhau bởi ba cách chọn anchor hợp lệ.

![[Dealing-Range-v01-03-Anchor-Sensitivity.svg|1516]]
*Sơ đồ: cùng một mức giá 116, ba anchor hợp lệ, ba nhãn location.*

Hệ quả phương pháp luận: **mọi claim về EQ thực chất là claim về anchor selection.** Nếu anchor nhiễu, EQ nhiễu; nếu EQ "hoạt động" chỉ với một cách chọn anchor cụ thể được chọn sau khi xem dữ liệu, đó là overfitting.

#### 14.3.3 Wick vs body

Trên D1 index, wick của một swing có thể dài 0.5–1.5 ATR. Chênh lệch EQ giữa anchor wick và anchor body có thể là 0.25–0.75 ATR — đủ để một FVG nằm "ở discount" theo cách này và "ở premium" theo cách kia. Đây là lý do cần kiểm tra Location Robustness (mục 4.4).

#### 14.3.4 Diễn giải ICT

[ICT FRAMEWORK] EQ là đường chia premium/discount; cùng ý tưởng với CE (Consequent Encroachment — 50% của một PD array như FVG). ICT dùng EQ như một mức tham chiếu "giá hợp lý" của range: bullish setup nên được tìm dưới EQ.

#### 14.3.5 Diễn giải cơ chế và tâm lý

- **[INTERPRETATION] — Reflexivity:** 50% retracement là heuristic cực kỳ phổ biến (Dow Theory mô tả secondary reactions thường hồi 1/3 đến 2/3 primary move; Fibonacci 50% có mặt trên mọi nền tảng). Nếu đủ nhiều người đặt limit orders quanh đó, có thể xuất hiện phản ứng tập thể. Nhưng: (a) mỗi người dùng anchor khác nhau nên "50%" của họ khác nhau → lệnh bị phân tán; (b) chưa có bằng chứng tôi có thể trích dẫn cho thấy phản ứng tại 50% của swing range vượt random baseline.
- **[MARKET MECHANICS] — Auction:** trong một balance area, giá dao động quanh vùng giao dịch nhiều nhất (value / POC trong Market Profile), không nhất thiết là midpoint hình học. Nếu phân phối thời gian-tại-giá lệch, "fair value" của auction lệch khỏi EQ hình học. Đây là một lý do để nghi ngờ tính đặc biệt của 50%.

#### 14.3.6 50% có tùy tiện không?

Có — theo nghĩa bất kỳ tỷ lệ nào (0.382, 0.5, 0.618, OTE 0.62–0.79) cũng có thể được dùng. 50% là lựa chọn *đối xứng tự nhiên*, không phải lựa chọn *được chứng minh*. Test: so sánh reaction frequency tại 0.382, 0.5, 0.618, 0.705 và **tại các mức ngẫu nhiên** trong khoảng [0.2, 0.8].

#### 14.3.7 Martingale null cho EQ — "EQ được chạm nhiều vì nó nằm ở giữa"

[MATHEMATICAL] Dưới martingale, xuất phát từ p > 0.5, xác suất chạm EQ trước khi chạm H\* là:

$$P(\text{touch EQ trước } H^*) = \frac{1 - p}{1 - 0.5} = 2(1-p)$$

Từ p = 0.6: 80%. Từ p = 0.8: 40%. **Giá quay về EQ thường xuyên chỉ đơn giản vì EQ ở gần.** Bất kỳ claim "EQ là magnet" nào cũng phải vượt baseline này.

#### 14.3.8 Kết quả mô phỏng: premium/discount dưới martingale và dưới drift

Thiết lập: range [0, 1], random walk Gaussian với 40 bước độ lệch chuẩn để đi hết một range; lệnh Buy tại p, stop tại 0, target tại 1; 20,000–40,000 path mỗi ô.

**Không drift (martingale):**

| p (entry) | R:R | q = P(target trước stop) | E[R] |
|---|---|---|---|
| 0.10 | 9.00 | 0.108 | ≈ 0 (+0.08)* |
| 0.25 | 3.00 | 0.253 | ≈ 0 (+0.01) |
| 0.40 | 1.50 | 0.409 | ≈ 0 (+0.02) |
| 0.50 | 1.00 | 0.497 | ≈ 0 (−0.01) |
| 0.60 | 0.67 | 0.596 | ≈ 0 (−0.01) |
| 0.75 | 0.33 | 0.746 | ≈ 0 (−0.01) |
| 0.90 | 0.11 | 0.894 | ≈ 0 (−0.01) |

\* Sai lệch nhỏ ở p = 0.10 là artifact của bước rời rạc (overshoot qua barrier), khớp với ước lượng lý thuyết q ≈ 0.111; nó không phải edge.

**Có drift dương nhỏ (0.01 σ mỗi bước):**

| p | q | q − p (excess) | E[R] = (q − p)/p |
|---|---|---|---|
| 0.10 | 0.156 | +0.056 | +0.56 (≈ +0.45 sau khi trừ artifact) |
| 0.25 | 0.338 | +0.088 | +0.35 |
| 0.50 | 0.600 | +0.100 | +0.20 |
| 0.75 | 0.815 | +0.065 | +0.09 |
| 0.90 | 0.927 | +0.027 | +0.03 |

(Với drift 0.005 σ/bước: E[R] lần lượt ≈ +0.32, +0.18, +0.09, +0.04, +0.01 — cùng pattern, một nửa độ lớn.)

![[Dealing-Range-v01-13-Martingale-Null.svg|1516]]
*Sơ đồ: martingale null — không drift thì P(thắng) ≈ p và E[R] ≈ 0 ở mọi vị trí; có drift thì discount khuếch đại edge theo R.*

*Sơ đồ v01-13 dùng một lần chạy độc lập (seed khác, lưới p mịn hơn); các giá trị lệch với bảng trên trong phạm vi sai số mô phỏng.*

#### 14.3.9 Đọc kết quả — ba bài học

1. **Không drift ⇒ không edge ở bất kỳ vị trí nào.** Công thức E[R] = (q − p)/p cho thấy expectancy chỉ đến từ *excess probability* q − p. Kết quả này tổng quát cho mọi bracket stop/target (optional stopping theorem), không chỉ stop tại range low.
2. **Có drift ⇒ excess probability lớn nhất quanh giữa range, nhưng expectancy tính theo R lớn nhất ở discount sâu** — vì cùng một excess được chia cho một rủi ro nhỏ hơn. Đây là cơ chế toán học đằng sau "buy discount in bullish context": **location khuếch đại directional edge**.
3. **Ba cái giá phải trả của discount sâu** (mô phỏng không tính): (a) chi phí cố định theo giá (spread/slippage) chiếm tỷ trọng lớn hơn khi rủi ro theo giá nhỏ; (b) tần suất giảm vì giá ít khi hồi sâu; (c) **selection effect** — việc giá hồi sâu có thể chính là thông tin cho thấy drift yếu hơn (bối cảnh đã đổi), nên q thực tế tại discount sâu có thể thấp hơn mô hình drift cố định. (c) là [HYPOTHESIS] quan trọng nhất cần test.

#### 14.3.10 Kết luận về EQ

EQ có **giá trị mô tả cao** (chuẩn hóa location, R:R geometry) và **giá trị dự báo chưa được chứng minh**. Mọi giá trị dự báo mà EQ có là *hàm của chất lượng anchor* và *sự tồn tại của drift có điều kiện*.

### 14.4. Premium / Discount

#### 14.4.1 Định nghĩa

- [MATHEMATICAL] Premium: p > 0.5. Discount: p < 0.5. Có thể chia mịn hơn: deep discount (p < 0.25), OTE bullish (0.21 ≤ p ≤ 0.38), shallow discount (0.38 < p < 0.5).
- [ICT FRAMEWORK] Trong bối cảnh bullish, tìm bullish PD arrays ở discount; bearish ngược lại. OTE (62–79% retracement) là tập con của discount trong leg bullish.

#### 14.4.2 Ý nghĩa cấu trúc

Discount của một bullish leg DR là vùng giá *thấp hơn trung bình* của impulse vừa xảy ra. Nếu impulse phản ánh một dòng tiền có hướng thật (drift), thì mua ở discount là mua *rẻ hơn mức trung bình mà dòng tiền đó đã chấp nhận*. Đây là diễn giải hợp lý duy nhất — và nó **phụ thuộc hoàn toàn** vào giả định dòng tiền đó còn tiếp tục.

#### 14.4.3 Tính tương đối — bốn hệ quả

1. Premium/discount **không có ý nghĩa nếu không có range được chỉ định**.
2. Premium/discount **không có ý nghĩa nếu không có direction**: discount trong bearish DR là nơi *chốt lời short*, không phải nơi mua.
3. Premium/discount **có thể xung đột giữa các cấp** (mục 3.5.2 — hàng 116).
4. Premium/discount **thay đổi khi range cập nhật** — một vị thế mở ở discount có thể "trở thành" premium sau khi range extend, dù giá không đổi.

#### 14.4.4 Quan hệ với Directional Bias, DOL, POI

```text
Directional Bias  → cho biết nên đọc discount là "mua" hay "chốt lời"
DOL               → cho biết có đủ room từ location hiện tại đến mục tiêu không
POI               → cho biết tại location đó có "evidence" (PD array) để hành động không
Premium/Discount  → chỉ cho biết vị trí
```

#### 14.4.5 Edge cases

| Case | Hiện tượng | Diễn giải | Hàm ý |
|---|---|---|---|
| **Bullish POI ở premium** | Bullish FVG/OB nằm trên EQ | Trong trend mạnh, retracement nông; POI ở premium của leg DR có thể vẫn là discount của H1 sub-leg | Chỉ hợp lệ nếu có frame khác xác nhận discount *và* DOL còn xa; ghi `location_conflict` |
| **Bearish POI ở discount** | Bearish OB dưới EQ | Có thể là continuation short sau khi bullish DR bị invalidate (bearish DR mới chưa hình thành) | Kiểm tra: range nào đang có thẩm quyền? |
| **Giá ở premium kéo dài** | Uptrend mạnh | [MATHEMATICAL] Trong uptrend, vị trí của giá trong rolling lookback range *theo định nghĩa* thường cao — "ở premium lâu" là chữ ký của trend, không phải bất thường | Đừng dùng "đã ở premium quá lâu" làm lý do short |
| **Giá ở discount kéo dài** | Downtrend / distribution | Tương tự | Tương tự |
| **Trend tiếp diễn không về EQ** | Retracement < 50% | Quy tắc "chỉ mua dưới EQ" bỏ lỡ các leg này | **Selection bias:** loại bỏ có hệ thống các trend mạnh nhất; test expectancy theo tháng, không chỉ theo trade |

#### 14.4.6 Tại sao "Buy discount / Sell premium" không phải luật

- Dưới martingale nó cho E = 0 (mục 14.3.8).
- Nó là **điều kiện cần hợp lý** trong một hệ thống có directional edge, **không phải điều kiện đủ**.
- Nó có thể *giảm* expectancy theo thời gian nếu nó loại bỏ nhiều setup continuation tốt hơn số setup xấu nó loại bỏ.

> **[HYPOTHESIS] HYP-DR-002:** Trong các D1 context bullish được xác định ex-ante, entries ở discount của H1 leg DR có excess hit probability (q − p) lớn hơn entries ở premium, sau khi kiểm soát khoảng cách đến DOL. **[BACKTEST REQUIRED]**

#### 14.4.7 Quadrant (0–25–50–75–100%) — mô tả tinh hơn, không phải thang conviction

![[Dealing-Range-Advanced-Quadrants.svg|1516]]
*Sơ đồ: chia range thành bốn quadrant — deep premium, premium nông, discount nông, deep discount.*

| Quadrant (bullish leg) | Cách đọc truyền thống [ICT FRAMEWORK] | Điều dữ liệu v0.2 nói [EMPIRICAL v0.2] |
|---|---|---|
| **75–100%** (deep premium) | Bearish PD array mạnh nhất; cấm Long mới | Entry theo leg ở bin u 0.75–1: P/W −0.007 [−0.029, +0.015] (θ = 2) |
| **50–75%** (premium nông) | Short cần confluence mạnh | P/W ≈ 0.000 [−0.025, +0.023] |
| **25–50%** (discount nông) | Long cần confluence mạnh | P/W +0.013 [−0.017, +0.045] |
| **0–25%** (deep discount; OTE rơi vào đây) | Bullish PD array mạnh nhất; vùng Long tối ưu | P/W +0.014 [−0.021, +0.048] |

*(u = khoảng cách từ origin chia W, nên với bullish leg, u = p. Arm A, toàn universe, entry = open sau lần close đầu tiên vào bin, stop = origin, target = termination; định nghĩa đầy đủ ở §19.3.)*

Hai ứng dụng của quadrant vẫn có giá trị **mô tả**, nhưng được viết lại cho đúng mức bằng chứng:
- **Chọn POI khi có nhiều ứng viên:** ưu tiên POI ở quadrant sâu là một quy ước *R:R* (stop gần origin, target xa) — hợp lý về hình học, nhưng dưới martingale R:R tốt hơn bị bù bởi xác suất thấp hơn. Quy ước này chỉ có lợi nếu có directional edge (§14.3).
- **"Retrace càng nông, trend càng khỏe":** đúng là trên dữ liệu thật (cổ phiếu D1), leg chỉ retrace nông có P(EXTENDED) cao hơn nhiều (~0.75 khi không vào discount vs ~0.45 khi có) — **nhưng random walk cho đúng gradient đó** (0.72 vs 0.41), và độ sâu retrace chỉ biết *ex-post* khi leg kết thúc. Đây là hình học của bracket, không phải dấu hiệu "sponsorship" đọc được ex-ante ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]], Kết quả 3).

**Hành vi quanh EQ:** rule thực dụng "close qua EQ và giữ được phía đó = nửa range nào đang kiểm soát" là một **mô tả** của trạng thái hiện tại, không phải dự báo; consolidation kéo dài quanh EQ được xử lý như Scenario G (chuyển sang container DR).

### 14.5. Liquidity Relationship

#### 14.5.1 Bốn khái niệm phải tách riêng

| Khái niệm | Bản chất | Quan sát được? | Ví dụ |
|---|---|---|---|
| **Range boundary** | Anchor hình học của frame | Có | H\* = 125 |
| **Liquidity pool** | Tập hợp lệnh chờ (giả định) quanh một mức | Không (latent) | Buy stops trên 125 |
| **Structural swing** | Swing có consequence cấu trúc | Có (qua định nghĩa) | F là termination của leg E–F |
| **DOL** | Dự báo về mục tiêu tiếp theo của giá | Không — là forecast | "Giá sẽ lấy BSL trên 125" |

Một mức giá có thể đồng thời là cả bốn — nhưng đó là **bốn claim khác nhau**, mỗi claim cần bằng chứng riêng. Nói "range high là DOL" là gộp ba bước suy luận thành một.

#### 14.5.2 Range boundary có tự động là liquidity không?

**Không.** Boundary là một điểm được *chọn*. Liquidity là một *giả thuyết về lệnh chờ*. Độ hợp lý của giả thuyết tăng theo:

1. **Obviousness:** swing hiển thị trên HTF, trùng PDH/PDL/PWH/PWL, số tròn (có bằng chứng Osler 2003 cho FX), equal highs/lows.
2. **Tuổi và trạng thái chưa bị chạm:** càng lâu chưa bị chạm, càng nhiều vị thế có thể đã đặt stop phía sau (hypothesis).
3. **Số lần test:** equal highs nhiều lần → nhiều người nhìn thấy cùng mức (hypothesis).
4. **Hành vi của participants:** breakout traders đặt buy-stop trên high; short sellers đặt stop-loss trên high. Hai nhóm này tạo ra buy orders *cùng một phía* — logic cơ chế hợp lý.

#### 14.5.3 Dấu hiệu quan sát được *sau* khi chạm boundary

Vì liquidity là latent, ta chỉ có thể suy luận ngược từ hành vi:

| Hành vi sau khi vượt boundary | Gợi ý | Mức tin cậy |
|---|---|---|
| Tăng tốc mạnh, range candle giãn | Stop cascade (Osler 2005) hoặc breakout flow | Trung bình |
| Vượt ngắn rồi đảo chiều nhanh | Lệnh đối ứng hấp thụ (absorption) / hết stops | Thấp–trung bình |
| Không có gì đặc biệt | Không có tập trung lệnh đáng kể, hoặc mức không quan trọng | — |

**Cảnh báo:** random walk cũng tạo ra cả ba hành vi. Mô phỏng: ~43% lần đầu vượt một fractal high đã xác nhận có close quay lại dưới mức đó. Muốn nói một "sweep" có ý nghĩa, phải so với baseline này (mục 19.2).

#### 14.5.4 Internal vs External Range Liquidity

![[Dealing-Range-v01-14-Four-Concepts.svg|1516]]
*Sơ đồ: boundary, liquidity pool, structural swing và DOL là bốn claim khác nhau; FVG là inefficiency, không phải liquidity theo nghĩa microstructure.*

**Phê phán thuật ngữ:** ICT gọi FVG là "internal range liquidity". Theo nghĩa microstructure, FVG **không phải** liquidity — nó là vùng giá mà giao dịch diễn ra *một chiều và nhanh* (ít thời gian tại giá, ít giao dịch hai chiều). Gọi nó là "liquidity" trộn hai ý: (a) nơi có lệnh chờ, (b) nơi giá "chưa được giao dịch đủ" (inefficiency). Giữ hai ý này tách biệt giúp tránh suy luận vòng tròn kiểu "giá quay lại FVG vì FVG là liquidity, và FVG là liquidity vì giá quay lại đó".

**[ICT FRAMEWORK → HYPOTHESIS] IRL ↔ ERL:** "Giá di chuyển từ IRL đến ERL và ngược lại." Dạng yếu của claim này **luôn đúng một cách tầm thường**: giá muốn đến boundary thì phải đi qua bên trong range. Dạng mạnh có thể test: *sau khi ERL bị lấy, xác suất giá quay lại chạm FVG gần nhất bên trong range trước khi đi thêm x·ATR ra ngoài là > baseline martingale*. HYP-DR-008.

#### 14.5.5 Biến liquidity có thể đo

- `dist_ext_up_atr`, `dist_ext_dn_atr`: khoảng cách đến swing chưa bị phá cấp ≥ k gần nhất phía trên / dưới.
- `liq_density_up(band)`: số swing highs còn sống trong dải [P, P + band·ATR].
- `eq_cluster_up`: số swing highs trong phạm vi ε·ATR của nhau (equal highs).
- `htf_confluence`: boundary có trùng PDH/PWH/số tròn không.

#### 14.5.6 Chu kỳ ERL ↔ IRL — "nhịp thở" của thị trường

**[ICT FRAMEWORK]** Luồng internal/external được mô tả như một chu kỳ (chi tiết: [[16-Internal-External-Range-Liquidity-IRL-ERL]]):

```text
Pha 1: Giá lấy ERL (quét range high/low)
Pha 2: Đảo, quay vào tìm IRL (FVG/OB đối diện bên trong range)
Pha 3: Rebalance xong IRL → expansion tới ERL đối diện
→ lặp lại trên range mới
```

Câu hỏi trước phiên tương ứng: *"giá đang ở pha nào của chu kỳ?"* — vừa quét ERL và reject → kỳ vọng về IRL (reversal); vừa rebalance IRL → kỳ vọng tới ERL (continuation); lơ lửng giữa hai pha → không có vị trí.

**Đánh giá:** dạng yếu của chu kỳ này **luôn đúng một cách tầm thường** — muốn tới boundary thì giá phải đi qua bên trong range, và FVG nằm bên trong range. Dạng mạnh, có thể sai, là: *sau khi ERL bị lấy, xác suất chạm FVG nội bộ gần nhất trước khi đi thêm x·ATR ra ngoài lớn hơn baseline martingale* (HYP-DR-008, UNTESTED). Liên quan: dữ liệu v0.2 cho thấy sau sweep origin, leg *ít* tiếp diễn hơn — tức "sweep ERL rồi đảo" là kịch bản phổ biến hơn "sweep rồi chạy tiếp" — nhưng phần lớn chênh lệch này cũng có trên random walk (§5.4.3).

### 14.6. Draw on Liquidity Relationship

#### 14.6.1 Định vị DOL so với DR

| Vị trí DOL | Ví dụ | Hàm ý |
|---|---|---|
| **Bên trong range** | FVG chưa lấp ở discount; EQ | DOL "ngắn hạn" trong một retracement; thường là internal |
| **Tại boundary** | H\* của leg DR (BSL) | DOL tự nhiên của continuation; range "hoàn thành" khi chạm |
| **Ngoài range** | Old D1 high phía trên H\* | Range là location frame, DOL là destination xa hơn |
| **Vượt nhiều lớp external liquidity** | W1 high phía trên cả D1 highs | Cần hierarchy DOL; các pool trung gian là "trạm" |

#### 14.6.2 Nearest vs meaningful

DOL gần nhất thường là internal hoặc micro liquidity — nó sẽ bị lấy "trên đường đi" dù hướng chính là gì. DOL *meaningful* được chọn theo:

1. **Scale:** θ\* của swing mục tiêu ≥ scale của range đang dùng.
2. **HTF alignment:** nằm theo hướng của D1 direction.
3. **Còn sống:** chưa bị lấy.
4. **Path of least resistance:** giữa giá và mục tiêu không có opposing structure lớn hơn (ví dụ một bearish D1 FVG lớn chắn đường).

#### 14.6.3 Khi DOL nằm ngoài DR — giữ hay định nghĩa lại range?

**Giữ range làm location frame.** DR và DOL trả lời hai câu hỏi khác nhau; DOL nằm ngoài range là *bình thường* (thực ra, với continuation, DOL *phải* ở ngoài hoặc tại termination).

**Chỉ định nghĩa lại (leo lên parent) khi range không scale-matched với mục tiêu:**

$$M = \frac{\text{distance to DOL}}{W}$$

- M ≈ 0–1.5: range phù hợp làm location frame cho mục tiêu này.
- M ≫ 1 (ví dụ > 3): range quá nhỏ so với hành trình; location "discount" của nó gần như không ảnh hưởng R:R đến DOL; dùng parent range. **HEURISTIC** — [BACKTEST REQUIRED] tìm dải M mà location còn mang thông tin.

#### 14.6.4 Opposing liquidity — rủi ro "lấy phía sau trước"

Khi DOL ở trên (BSL) nhưng có SSL rõ ràng ngay dưới protected low, tồn tại kịch bản giá lấy SSL trước (sweep L\*) rồi mới đi lên. Đây chính là vùng giao giữa **sweep** và **invalidation** (mục 5.1): nếu stop của bạn nằm ngay dưới L\*, nó nằm *trong* pool SSL. Hàm ý thực hành:

- Hoặc đặt stop dưới L\* với buffer đủ lớn để sống sót qua sweep (R nhỏ lại tương đối, R:R giảm).
- Hoặc chờ sweep L\* + reclaim + LTF MSS mới entry (đây thực chất là cấu trúc của ICT 2022 Model).

#### 14.6.5 DOL và Daily Bias — bốn thứ khác nhau

```text
Directional Bias  : giả thuyết về hướng chi phối (ví dụ D1 bullish)
DOL               : mục tiêu liquidity cụ thể (ví dụ BSL trên 125)
Trade Setup       : cấu hình điều kiện tại POI (H1)
Entry Direction   : hướng lệnh thực tế (có thể ngược bias trong model countertrend)
```

### 14.7. Market Structure Relationship

#### 14.7.1 Hai chiều nhân quả

- **Structure → Range:** anchors của DR được *suy ra* từ structure (protected low = origin của BOS).
- **Range → Structure interpretation:** sau khi có DR, ta *gán nhãn* internal/external cho swing, và đánh giá một break là "internal event" hay "structure change".

#### 14.7.2 Nguy cơ vòng tròn và cách phá

Nếu bạn dùng DR để quyết định swing nào là external, rồi dùng swing external để vẽ DR, bạn có thể biện minh cho *bất kỳ* range nào. Cách phá vòng tròn: **pipeline có thứ tự cố định**

```text
Stage 1: swing detection   (không phụ thuộc range)
Stage 2: scale θ*          (không phụ thuộc range)
Stage 3: break events      (phụ thuộc swing + scale, không phụ thuộc range)
Stage 4: DR construction   (phụ thuộc 1–3)
Stage 5: labels internal/external, P/D (phụ thuộc 4)
```

Không stage nào được dùng output của stage sau.

#### 14.7.3 Khi nào một HH/HL đủ quan trọng để redefine DR?

> **Một HH redefines DR ở scale k khi và chỉ khi: nó là break (theo rule đã chọn, có acceptance) của một swing high có θ\* ≥ θ_min(k), được tạo bởi một leg xuất phát từ một swing low có θ\* ≥ θ_min(k).**

Mọi HH khác là internal refinement. Bốn lý do phổ biến khiến một HH/HL **không** redefine range:

1. **Scale mismatch:** HH trên M5 bên trong D1 leg.
2. **Không có pullback đạt θ:** HL quá nông → không có origin mới → chỉ là extension.
3. **Không có acceptance:** HH là sweep, không phải break.
4. **Nằm trong parent consolidation:** HH ở scale k nhưng internal đối với parent container → thay đổi setup range, không thay đổi context range.

### 14.8. Alternative Interpretations

Cùng một cấu trúc quan sát được — **giá quét dưới swing low của range, close quay lại bên trong, tạo displacement tăng phá swing high nội bộ, rồi chạy đến range high** — dưới bảy lăng kính:

| Lăng kính | Diễn giải | Khái niệm tương ứng | Điều nó bổ sung / thách thức |
|---|---|---|---|
| **ICT** | SSL dưới range low bị sweep; MSS + displacement xác nhận; DOL là BSL trên range high | Sweep, MSS, DOL, IRL→ERL | Narrative có mục đích (liquidity được "nhắm") |
| **Classical price action** | False breakdown của support; bull trap ngược (bear trap); range trading | Support/resistance, failed break | Không cần giả định ý định; cùng hành vi, ít giả định hơn |
| **Dow Theory / swing structure** | Secondary reaction kết thúc; primary trend tiếp diễn; HL giữ | Primary/secondary trend, 1/3–2/3 retracement | Heuristic retracement có từ đầu thế kỷ 20 — "EQ" không phải phát minh mới |
| **Wyckoff** | *Spring* trong trading range (phá đáy giả rồi quay lại), sau đó sign of strength | Trading range, spring, upthrust, SOS | Nhấn mạnh volume và "effort vs result" — thông tin mà OHLC-only ICT thường bỏ qua |
| **Auction Market Theory** | Failed auction ở rìa balance: thị trường thử giá thấp hơn, không tìm được giao dịch tiếp nối (excess), quay lại value; imbalance lên phía trên | Balance/imbalance, value area, excess, poor low | Boundary quan trọng vì là nơi auction bị từ chối; EQ hình học ≠ value (POC) |
| **Microstructure / order flow** | Sell stops dưới low được kích hoạt → market sells; lệnh mua (limit) hấp thụ; khi hết stops, áp lực bán cạn; aggressive buyers đẩy giá | Stop cascade (Osler 2005), absorption, depth | Có thể quan sát một phần bằng volume/footprint trên futures; không cần "ai đó săn stops" |
| **Quantitative / statistical** | Một first-passage event trong một chuỗi có thể có hoặc không có drift; "sweep" xảy ra ~43% số lần ở lần vượt đầu tiên kể cả trong random walk | Martingale, optional stopping, momentum/mean-reversion regimes | Câu hỏi duy nhất quan trọng: tần suất của chuỗi này *có vượt baseline không* |

#### 14.8.1 Một kết nối thú vị: IPDA 20-day range và Donchian channel

IPDA 20-day lookback chính là **Donchian channel 20 ngày** — công cụ trend-following cổ điển (hệ thống Turtle nổi tiếng dùng breakout 20 và 55 ngày). Cùng một mức 20-day high:

- Với trend follower: là **điểm vào lệnh breakout** (buy-stop đặt trên 20-day high).
- Với ICT: là **buy-side liquidity**.

[INTERPRETATION] Hai cách nhìn này *nhất quán cơ học*: nếu có một lượng đáng kể trend follower đặt buy-stop trên 20-day high, thì theo đúng định nghĩa, ở đó có buy-side liquidity. ICT và trend-following nhìn cùng một vật thể từ hai phía của giao dịch. Điều này cũng gợi ý một test: **hành vi sau khi phá 20-day high là continuation (trend-following thắng) hay reversal (sweep thắng)?** — và câu trả lời có thể phụ thuộc regime. [BACKTEST REQUIRED]

#### 14.8.2 Bài học của section

Một hành vi giá quan sát được có thể được mô tả nhất quán bởi nhiều mô hình với mức giả định khác nhau. **ICT narrative có nhiều giả định nhất** (ý định của participant). Theo nguyên tắc parsimony, khi hai mô hình giải thích cùng dữ liệu, mô hình ít giả định hơn nên được ưu tiên *cho đến khi* mô hình nhiều giả định hơn tạo ra một dự báo khác biệt, kiểm chứng được. Giá trị thực sự của ICT (nếu có) nằm ở chỗ nó tạo ra *quy tắc hành động cụ thể* — và quy tắc thì test được.

#### 14.8.3 Dealing Range so với Value Area, Trading Range và footprint

| Khung | Khái niệm tương đương | Trùng ở đâu | Khác ở đâu |
|---|---|---|---|
| **Auction Market Theory** | Value Area, POC | EQ ≈ trung tâm vùng giá được chấp nhận; boundary ≈ rìa balance | AMT dùng phân phối volume/TPO thật; ICT dùng trung điểm hình học — đơn giản hơn nhưng thô hơn |
| **Wyckoff** | Trading Range; Spring / UTAD | "Giá bị giam trong biên trước markup/markdown"; test ở hai đầu | Wyckoff đọc **volume** qua từng test (effort vs result); ICT OHLC-only bỏ qua thông tin này |
| **Order flow / footprint** | Volume cluster, absorption | Cụm stop/absorption ở hai đầu | Footprint cho bằng chứng trực tiếp (hợp đồng khớp); ICT suy luận gián tiếp từ hình dạng nến |

**Kết luận đối chiếu:** Dealing Range là phiên bản đơn giản hóa, vẽ được bằng mắt, của Value Area (AMT) và Trading Range (Wyckoff) — đánh đổi độ chính xác (không dùng volume) lấy tốc độ và tính phổ quát. Với index futures có volume thật, câu hỏi nghiên cứu đáng làm là liệu volume/delta có giúp phân biệt sweep với break tốt hơn OHLC hay không (§20.2).

### 14.9. Range projection — Standard Deviation

**[ICT FRAMEWORK]** Khi external bị phá thật (acceptance) và giá expansion, range cũ còn một công dụng: **làm thước đo projection**. Dùng chiều cao range (hoặc manipulation leg) chiếu các mức −1, −2, −2.5, −4 SD theo hướng expansion để ước lượng terminus của leg mới (xem [[31-Standard-Deviation]] và [[08-Central-Bank-Dealers-Range]] cho phiên bản CBDR). Ứng dụng chính: khi giá vào "vùng trống" không còn external liquidity rõ phía trước, SD projection + HTF FVG là cách đặt target *đo được* thay vì "gồng tới số tròn".

**Mức bằng chứng:** [HYPOTHESIS]. Projection theo bội số của range là một quy ước đo; việc các mức SD có reaction nhiều hơn mức ngẫu nhiên cùng khoảng cách chưa được test trong vault. Test tối thiểu: tần suất đảo chiều (k·ATR) tại các mức SD so với các mức ngẫu nhiên trong cùng dải khoảng cách. **[BACKTEST REQUIRED]**

---

## 15. Phản biện & giới hạn (Critique)

### 15.1. Phản biện từ góc nhìn khoa học/quant — viết thẳng

1. **Tính chủ quan khi vẽ range là vấn đề gốc rễ, không phải chi tiết vặt.** Mục 16 (nhóm A) mổ xẻ anchor ambiguity, nhưng cần nói thẳng ở đây: hai trader nhìn cùng một chart, một người coi swing X "đủ ý nghĩa", người kia coi swing Y mới đúng — không có trọng tài khách quan nào phân xử ngay tại thời điểm ra quyết định. Đây không phải nhiễu nhỏ; nó thay đổi hoàn toàn kết luận Premium/Discount, tức đổi cả hướng lệnh.
2. **Hindsight bias & confirmation bias.** Sau khi trade xong, trader dễ nhớ những lần range "đúng như sách" và quên các lần range bị chọn sai rồi âm thầm "vẽ lại cho khớp" với những gì đã xảy ra. Không ai backtest bằng cách đóng băng quyết định vẽ range TẠI THỜI ĐIỂM chưa biết tương lai — hầu hết review đều đã biết giá đi đâu.
3. **Không có backtest công khai đạt chuẩn thống kê.** Không tồn tại nghiên cứu độc lập, có peer review hoặc ít nhất minh bạch dữ liệu, chứng minh "trade theo Dealing Range đúng" có edge dương có ý nghĩa thống kê (p-value, sample size đủ lớn, out-of-sample test) so với ngẫu nhiên. Toàn bộ "bằng chứng" hiện có là ảnh chụp màn hình chọn lọc từ cộng đồng ICT.
4. **Unfalsifiable — concept nào fail thì đổ cho "chưa đủ confluence".** Khi Long ở discount thua, câu trả lời phổ biến là "range chọn chưa đúng" hoặc "thiếu HTF POI xác nhận" — tức luôn có lối thoát để không bao giờ thừa nhận framework sai. Một lý thuyết mà mọi thất bại đều được giải thích bằng cách thêm điều kiện MỚI (chứ không phải bác bỏ điều kiện cũ) đang vi phạm tiêu chuẩn falsifiability cơ bản của Popper.
5. **Nguy cơ overfitting khi thêm filter.** Quadrant (§14.4.7), nested range alignment (§4.1), FVG age decay... mỗi lớp filter mới đều "nghe hợp lý" nhưng cộng dồn lại tạo ra một hệ thống có quá nhiều bậc tự do — dễ tìm ra combo filter khớp hoàn hảo với dữ liệu lịch sử (curve-fitting) nhưng không generalize ra tương lai.
6. **Backtest độc lập cho kết quả trái chiều.** Trong cộng đồng quant retail, các thử nghiệm tự phát về "mua discount bán premium" trên dữ liệu FX/futures cho kết quả không nhất quán: một số cho thấy edge nhẹ trong range environment, một số khác cho thấy không khác biệt so với random entry sau khi trừ phí giao dịch và slippage. *(Nhận định này không kèm nguồn cụ thể — chưa kiểm chứng, không dùng làm bằng chứng theo chiều nào. Bằng chứng duy nhất có nguồn trong vault là nghiên cứu exploratory §19.3.)*
7. **Giải thích thay thế đơn giản hơn.** Hiện tượng "giá đảo tại đỉnh/đáy trước đó" có thể giải thích hoàn toàn bằng **mean reversion** (giá dao động quanh trung bình sau khi lệch quá xa) và **volatility clustering** (biến động lớn thường theo sau bởi biến động lớn, tạo cảm giác "swing có ý nghĩa" chỉ vì đó là điểm biến động cực trị gần nhất) — hai hiện tượng thống kê đã biết rõ và không cần khái niệm "liquidity pool" hay "smart money" để giải thích.

### 15.2. Phản biện của phản biện — phần nào đúng, phần nào trả lời được

- **Chấp nhận hoàn toàn:** điểm 1 (tính chủ quan) và điểm 3 (thiếu backtest công khai chuẩn) là đúng và không thể chối cãi. Đây là giới hạn thật của toàn bộ trường phái ICT, không riêng Dealing Range.
- **Có thể trả lời một phần — quy tắc hóa để backtest được:** anchor ambiguity có thể giảm (không loại bỏ hết) bằng cách **định nghĩa cứng** "swing có ý nghĩa" = swing tạo bởi displacement đạt ngưỡng ATR cụ thể (ví dụ ≥ 1.5× ATR(14) của nến tạo swing) VÀ đã có ít nhất một wick chạm/xuyên qua một old high/low trước đó. Định nghĩa cứng này có thể code hóa và backtest — note này đã làm một phiên bản (Directional Change θ·ATR + close-break) ở §19.3.
- **Có thể trả lời — đây là framework đọc chart, không phải signal máy móc.** Dealing Range không tự xưng là một hệ thống giao dịch độc lập có thể chạy tự động không cần phán đoán — nó là một lăng kính để tổ chức thông tin trên chart (đâu là biên, đâu là trung tâm). So sánh công bằng hơn không phải "Dealing Range vs random entry" mà là "trader có framework tổ chức thông tin vs trader nhìn chart không có cấu trúc gì" — và ở phép so sánh này, có framework (bất kỳ framework hợp lý nào, không riêng ICT) thường giúp giảm nhiễu quyết định.
- **Không trả lời được bằng R:R — location không tự tạo expectancy.** Lập luận cũ "chỉ vào lệnh ở vùng R:R tốt hơn tự nó cải thiện kỳ vọng, độc lập với việc concept có đúng về dự đoán hay không" **sai về mặt toán học**: dưới martingale, với stop ở L\* và target ở H\*, xác suất thắng đúng bằng p ⇒ E[R] = (q − p)/p = 0 tại mọi vị trí (optional stopping; mô phỏng §14.3.8). R:R tốt hơn bị bù trừ chính xác bởi xác suất thắng thấp hơn. Location chỉ **khuếch đại** một directional edge đã có. Trên dữ liệu thật v0.2, P/W theo vị trí ≈ 0 (§19.3). Giá trị thật của location là **kỷ luật**: tránh mua đuổi, đặt stop có cơ sở, giảm số lệnh xấu — không phải tạo kỳ vọng dương.
- **Không thể trả lời — vẫn phải thừa nhận:** unfalsifiability (điểm 4) là vấn đề thật, chỉ giảm được bằng kỷ luật cá nhân (định nghĩa trước invalidation cụ thể, ghi journal khách quan) chứ không giải quyết được ở tầng lý thuyết. Overfitting (điểm 5) cũng chỉ giảm bằng cách giới hạn số lượng filter dùng cùng lúc, không loại bỏ được hoàn toàn.

### 15.3. Giới hạn cứng phải chấp nhận

1. **Không có định nghĩa toán học duy nhất cho "swing có ý nghĩa"** — mọi ngưỡng (ATR, số lần chạm, độ lớn displacement) đều là lựa chọn chủ quan của người dùng, dù đã quy tắc hóa.
2. **Range luôn có thể vẽ lại sau khi biết kết quả** — điều này khiến việc tự đánh giá "tôi vẽ đúng" cực kỳ dễ bị thiên lệch nếu không ghi chú TRƯỚC khi biết giá đi đâu.
3. **Không tồn tại bằng chứng ngoài cộng đồng ICT (academic, quant fund công khai) xác nhận edge thống kê có ý nghĩa** của việc trade theo Premium/Discount trên Dealing Range.
4. **Hiệu quả phụ thuộc nặng vào thanh khoản thị trường** — trên tài sản mỏng thanh khoản hoặc giờ giao dịch mỏng, khái niệm này kém tin cậy hơn nhiều so với FX majors giờ cao điểm.
5. **Không dự đoán được các cú sốc ngoại sinh** (tin tức, quyết định chính sách, thanh lý đòn bẩy) — Dealing Range chỉ mô tả cấu trúc lệnh tồn tại TRƯỚC cú sốc, không có khả năng dự báo bản thân cú sốc.
6. **Tính fractal (nested range) làm framework luôn có thể tìm được MỘT range nào đó ủng hộ bất kỳ hướng nào** — nếu không kỷ luật chọn đúng tầng trước khi vào lệnh, framework tự nó cung cấp lý do biện minh cho mọi quyết định.

> [!quote] Kết luận trung thực
> Dealing Range đáng dùng như một **công cụ tổ chức thông tin và kỷ luật vị trí entry**, không phải như một tín hiệu dự đoán giá. Nghiên cứu exploratory v0.2 trên dữ liệu thật (§19.3) không tìm thấy edge vị trí robust — điều này *khớp* với kết luận này chứ không mâu thuẫn với nó. Nó giúp tránh mua đỉnh/bán đáy một cách có hệ thống và ép trader phải trả lời rõ ràng "range nào, vì sao" trước khi vào lệnh — giá trị này là thật và không cần backtest để nhìn thấy trong hành vi quản trị vốn. Nhưng đừng tự huyễn hoặc rằng công thức "50% chia range" tự nó là một edge dự đoán được kiểm chứng khoa học; nó hoạt động tốt nhất khi kết hợp với size hợp lý, invalidation rõ ràng viết TRƯỚC khi vào lệnh, và một journal đủ lớn để tự kiểm tra thay vì tin vào trực giác "cảm thấy đúng".

### 15.4. What We Actually Know vs What We Assume

#### 15.4.1 Bảng claim

| Claim | Evidence Type | Confidence | Backtest Required? |
|---|---|---|---|
| Dealing Range được xác định bởi hai structural anchors | ICT framework (định nghĩa) | Cao *về việc đây là định nghĩa ICT*; thấp về việc có một cách chọn anchor chuẩn | Không (là định nghĩa) — nhưng *quy tắc chọn* thì có |
| 50% là equilibrium | Mathematical | Cao (định nghĩa hình học) | Không cho định nghĩa; **Có** cho mọi claim hành vi tại 50% |
| Premium/discount là tương đối | Mathematical | Cao | Không |
| Dưới martingale, location không tạo expectancy | Mathematical (optional stopping) + mô phỏng | Cao | Không |
| Discount tạo bullish reversals | Hypothesis | Thấp — proxy v0.2: P/W theo vị trí ≈ 0; nghiêng dương yếu ở θ nhỏ, không robust (§19.3) | **Có** |
| Location khuếch đại directional edge (nếu có drift) | Mathematical *có điều kiện* + mô phỏng | Cao về cơ chế; chưa biết drift có tồn tại có điều kiện hay không | **Có** (drift) |
| Range boundaries đại diện cho liquidity | Interpretation | Trung bình–thấp; bằng chứng mạnh nhất (Osler) là về số tròn trong FX, không phải swing | **Có** |
| Stop orders có thể tạo price cascade | Market mechanics (Osler 2005) | Trung bình–cao (FX) | Không cho cơ chế; Có cho khả năng khai thác |
| Order clustering tại số tròn trong FX | Market mechanics (Osler 2003) | Cao cho dữ liệu nghiên cứu | Không cho fact; Có cho áp dụng hiện tại |
| Giá luân phiên IRL ↔ ERL | ICT framework → Hypothesis | Thấp (dạng mạnh chưa test) | **Có** |
| Một số phương pháp chọn swing cải thiện expectancy | Hypothesis | Thấp — proxy v0.2: structural ≈ IPDA-20 ≈ anchor ngẫu nhiên | **Có** |
| Swing có displacement từ origin bền hơn | Hypothesis | Chưa biết | **Có** |
| Random walk tạo nhiều swing và "sweep" | Mathematical + mô phỏng | Cao — v0.2: tần suất sweep origin ở dữ liệu thật ≈ null | Không |
| MEHR thô là thước đo không thiên lệch của thông tin vị trí | Mathematical + [EMPIRICAL v0.2] | **Sai** khi có overshoot (gap, close-only, slippage): q − u = δ(1 − 2u)/(W + 2δ) | Không — dùng P/W |
| Sweep protected origin xác nhận continuation | [EMPIRICAL v0.2] | Thấp — P(EXTENDED) sau sweep 0.24–0.28 vs 0.58 khi không sweep | **Có** (với trigger: HYP-DR-014) |
| Range thường thất bại bằng MSS ngược chiều trước khi phá origin | [EMPIRICAL v0.2] + định nghĩa | Trung bình — ~50% REVERSED khi origin còn nguyên; INVALIDATED thuần ~1% | Không cho mô tả |
| Nhiều định nghĩa range thường đồng thuận về location | [EMPIRICAL v0.2] | **Sai** — chỉ 54–70% số bar, bằng null | Không |
| Intent của "Smart Money" có thể suy ra từ chart | Speculative narrative | Rất thấp | Không thể test bằng OHLC |

#### 15.4.2 Assumption audit — kiểm tra các giả định trong chính research brief

**Assumption 1:** "Dealing Range selection là trước hết một vấn đề về market structure và swing classification."
- *Problem:* đúng nhưng chưa đủ — nó còn là vấn đề về **mục đích** (range trả lời câu hỏi gì) và **scale matching** với horizon của trade.
- *Alternative:* DR selection = f(structure, purpose, scale, time).
- *Implication:* cùng một chart có thể có hai range "đúng" cho hai câu hỏi khác nhau; không nên tìm "range duy nhất".
- *Test:* so sánh arm A (leg) vs B (container) theo regime.

**Assumption 2:** Hierarchy 5 cấp Micro → HTF là trục phân loại phù hợp.
- *Problem:* trộn scale với role; rời rạc hóa đại lượng liên tục (mục 3.2.2).
- *Alternative:* hai trục (θ\*, role(t)).
- *Implication:* bớt tranh cãi "swing này level mấy"; thêm khả năng đo lường.
- *Test:* so sánh độ ổn định phân loại (bao nhiêu swing đổi level khi tham số đổi ±10%).

**Assumption 3:** "H1 range refines D1 range" — ngầm giả định các range lồng nhau gọn.
- *Problem:* thực tế thường chồng lấn/xung đột.
- *Alternative:* ghi nhận `nesting_relation` như một biến.
- *Implication:* có thể nhóm "nesting sạch" mới là nơi có edge — hoặc không.
- *Test:* HYP-DR-004.

**Assumption 4:** Premium/discount là một thành phần có predictive value cần được "tìm ra".
- *Problem:* dưới martingale nó không thể có; câu hỏi đúng là về *drift có điều kiện*.
- *Alternative:* location = amplifier, direction = source.
- *Implication:* đầu tư research vào *direction* (Daily Bias, DOL) có thể quan trọng hơn tinh chỉnh location.
- *Test:* so sánh arm F (no location filter) với arm A — nếu gần bằng nhau, location không phải nơi edge nằm.

**Assumption 5:** Mục tiêu cuối "biến DR từ discretionary thành structural framework có thể lượng hóa" là khả thi hoàn toàn.
- *Problem:* phần lớn *có thể* formalize (swing, break, state, location); phần DOL selection và "relevance" vẫn còn discretion đáng kể.
- *Alternative:* chấp nhận một framework **hybrid**: phần formalize được chạy bằng rule; phần còn discretionary được ghi lại dưới dạng lựa chọn có timestamp để đo sau.
- *Implication:* journal cần field cho mỗi lựa chọn discretionary.
- *Test:* đo inter-rater reliability — cùng chart, hai lần phân tích cách nhau 2 tuần (hoặc hai người), mức độ trùng khớp của range được chọn.

**Assumption 6 (ngầm):** Chart ICT chuẩn (OHLC, không volume) đủ thông tin để phân biệt sweep và break.
- *Problem:* OHLC chỉ cho hệ quả; cơ chế (stop cascade vs absorption) cần volume/order flow.
- *Alternative:* trên futures, bổ sung volume/delta như biến phụ.
- *Implication:* có thể có giới hạn trên về độ chính xác của mọi rule chỉ dùng OHLC.
- *Test:* so sánh rule OHLC-only vs rule có thêm volume trên NQ/ES.

---

## 16. Edge Cases & Counterexamples — catalog đã gộp

Bản cũ có bốn danh sách chồng nhau: **EC1–EC9** (edge cases thực chiến), **W1–W5** (war stories), **EC-01…EC-24** (edge cases v0.1) và **CX-01…CX-25** (counterexamples v0.1). v0.2 xếp chúng vào sáu nhóm theo *cơ chế gây lỗi*; các mục trùng nhau được gộp thành một entry (ID cũ giữ nguyên để link từ journal/note khác không mất nghĩa).

| Nhóm | Câu hỏi của nhóm | Entry (ID gốc) | Đã gộp |
|---|---|---|---|
| **A** | Anchor có đáng tin không? | A-1 (EC1+CX-04+CX-07+CX-08), W1/EC6, A-3 (EC7+EC-10+CX-01), CX-25, W4 | EC1↔CX-04/07/08; EC6↔W1; EC7↔EC-10↔CX-01 |
| **B** | Kích thước & regime có làm tọa độ vô nghĩa? | EC-01, W3/EC-02, EC8, EC-03, EC-23, EC-24, CX-05 | W3↔EC-02 |
| **C** | Nhiều range hợp lệ cùng lúc? | EC2/EC-06, EC-07, W5, CX-02, CX-09, CX-10, CX-11, CX-12, CX-14, CX-15 | EC2↔EC-06 |
| **D** | EQ & location có đổi nghĩa? | EC3, EC5/EC-22, EC-19, CX-13 | EC5↔EC-22 |
| **E** | Liquidity & sweep đọc thế nào? | EC-04, EC-05, EC-11, EC-12, EC-13, W2, EC-15 | — |
| **F** | Vòng đời: khi nào cập nhật, khi nào bỏ? | EC-09, EC-14, EC-16, EC-17, F-5 (EC-18+CX-24), EC-20, EC-21, EC4, CX-16…CX-23, EC9 | EC-18↔CX-24 |

Định dạng mỗi entry giữ nguyên dạng gốc (EC/W: tình huống → vì sao → nhận diện → xử lý; EC-xx: Class → Interpretation → Structure → Trading → Invalidation → Backtest; CX: ví dụ + *Why*). Các entry gộp được viết lại.

### 16.1. Nhóm A — Anchor, dữ liệu và feed

#### A-1. Anchor ambiguity — "swing nào?" (gộp EC1, CX-04, CX-07, CX-08)

**Tình huống (EC1):** trên XAUUSD H4, trader A chọn cặp swing gần giá nhất (đỉnh nhỏ mới, chưa lấy liquidity nào); trader B chọn cặp swing D1 xa hơn. Tại cùng một giá, A thấy "discount 30%", B thấy "premium 55%".

**Bốn nguồn gốc của ambiguity — mỗi nguồn có một lời giải khác nhau:**

| Nguồn | Ví dụ | Lời giải |
|---|---|---|
| **Chọn theo thị giác thay vì hệ quả** (CX-04) | Đáy sâu nhất màn hình (A) hút mắt, nhưng leg phá swing high gần nhất xuất phát từ một HL muộn hơn (E) → giá 116 là premium theo A–F, discount theo E–F | Origin = cực trị nhịp hồi *trước break gần nhất* — "lớn nhất" ≠ "có hệ quả gần nhất" |
| **Swing ngay tại ngưỡng** (CX-07) | Nhịp hồi 1.95 ATR (không đạt θ = 2) ở phiên bản A, 2.05 ATR ở phiên bản B → hai leg DR khác nhau | Gắn `near_threshold = TRUE` khi \|θ\* − θ_min\| < 0.2; xem LRI |
| **Rule break khác nhau** (CX-08) | Wick-break làm BOS sớm 3 bar → origin khác close-break | Cố định close-break (quy ước vault); wick chỉ là sweep |
| **Wick vs body** (CX-06) | EQ lệch 0.3–0.7 ATR | Cố định một giao thức ([[#3.4. Anchor Selection\|§3.4.6]]) |

**Cách xử lý chung:** sinh **candidate set cố định** theo rule, tính location trên mọi candidate (LRI) **trước** khi thấy phản ứng giá. "Chờ giá tự xác nhận rồi mới tin số liệu" (lời khuyên cũ) dễ biến thành chọn range theo kết quả. Dữ liệu thật: bốn định nghĩa hợp lệ chỉ đồng thuận ở 54–70% số bar ([[#4.4. Bài toán quá nhiều range và LRI|§4.4]]).

#### W1. Cùng một ngày, hai bản đồ — range trên Futures khác range trên CFD

![[Dealing-Range-War-Feed-Divergence.svg|1516]]
*Sơ đồ: NQ futures (ETH) có đỉnh overnight mà CFD không hiển thị đủ; hai đầu range lệch → EQ lệch → premium/discount lệch theo.*

**Hiện tượng:** bạn vẽ range trên chart CFD NAS100, đo discount, chờ giá về OTE — giá đảo sớm hơn vùng của bạn vài chục điểm, đúng tại mức mà *trên chart futures* là 62% retracement. Hoặc equal highs "đẹp" trên CFD không tồn tại trên futures (và không bao giờ bị quét).

**WHY — vì sao hai feed khác nhau và vì sao futures thắng:** dealing range hoạt động vì nó vẽ bản đồ *lệnh thật*. Lệnh thật của chỉ số nằm ở **CME (futures NQ)** — đó là nơi các desk lớn đặt stop, nơi thuật toán tham chiếu. CFD là giá tổng hợp broker tạo ra từ futures cộng spread markup, và nhiều broker cắt bớt giờ giao dịch → **đỉnh/đáy overnight (nơi một đầu range thật hình thành) có thể không tồn tại trên chart CFD**. Khi hai đầu range sai thì mọi số phái sinh (EQ, OTE, quadrant) sai theo — đây chính là "chọn sai range" ở mục 9, nhưng dưới dạng không thể phát hiện nếu chỉ nhìn một chart.

**Rule đo được:**
- Bản đồ (range, pool, EQ) vẽ trên **futures**; thực thi ở đâu cũng được nhưng level lấy từ bản đồ gốc.
- Backtest và live cùng một feed — nếu không, thống kê `location_in_range` vô nghĩa.
- Với FX: dùng feed có khối lượng lớn/chuẩn interbank làm tham chiếu, chấp nhận sai số vài pip giữa broker và ghi rõ điều đó vào buffer của stop.

*Gộp EC6 (cùng chủ đề):* với index CFD (NAS100/US30/SPX500), luôn kiểm tra chéo hợp đồng futures (NQ/YM/ES) quanh giờ overnight/Á trước khi kết luận một swing "không đáng kể"; vẽ range trên futures gốc, thực thi ở đâu cũng được.

#### A-3. Anchor hình thành trong tin tức (gộp EC7, EC-10, CX-01)

**Tình huống:** một nến M5 phá mạnh qua đỉnh cũ đúng lúc NFP — thân dài, giống displacement chuẩn (EC7); hoặc swing low là wick 90 pip trong bar NFP (CX-01).

**Vì sao nguy hiểm:** wick/thân trong 1–2 phút tin phản ánh thanh khoản mỏng tạm thời, spread giãn và slippage, không phải auction rejection bình thường. θ\* của anchor lớn một cách giả tạo; EQ bị kéo lệch (ví dụ CX-01: ~45 pip, khiến một FVG "discount" theo wick thực ra là premium theo body).

**Nhận diện sớm:** swing hình thành trong cửa sổ ±5 phút quanh tin cấp cao → hạ một bậc tin cậy mặc định, gắn cờ `news_anchor`.

**Xử lý:** dùng anchor theo body cho bar tin, hoặc chờ 30–60 phút cho cấu trúc sau tin hình thành rồi dựng range chính; swing trong nến tin chỉ dùng tạm. **Backtest (EC-10):** so sánh kết quả có/không loại anchor tin tức.

#### CX-25 — Anchor là artifact dữ liệu.

Bad tick, hoặc **continuous futures contract được back-adjust**: khi dữ liệu futures được nối bằng back-adjustment, giá lịch sử bị dịch — anchor trên chuỗi adjusted khác với giá thực đã giao dịch. Với phân tích liquidity quanh số tròn hoặc mức giá tuyệt đối, phải dùng giá *unadjusted* của contract đang giao dịch tại thời điểm đó. *Why abandon:* range dựa trên giá chưa từng tồn tại không thể đại diện cho lệnh chờ thật.

#### W4. EQ "trôi" qua đêm — sáng ra mọi level lệch vài điểm mà không ai báo

**Hiện tượng:** tối hôm trước bạn đo EQ = 20,302 và đặt alert/limit quanh OTE. Trong đêm, giá nhúng nhẹ làm range low thấp hơn 18 điểm — về cấu trúc range **không đổi** (vẫn swing đó, chỉ wick sâu hơn), nhưng **mọi mức % đã trôi**: EQ mới 20,293, OTE dịch theo. Limit của bạn giờ nằm lệch ngoài vùng thật — giá chạm vùng thật, đảo, và bạn đứng ngoài nhìn (hoặc tệ hơn: limit khớp ở mức đã thành premium nông).

**WHY — vì sao vài điểm lại quan trọng ở đây:** bản thân EQ là *vùng*, không phải mức (§14.2 cơ chế 2) — nhưng **OTE và quadrant biên là nơi các cụm lệnh limit của cả đám đông ICT trader đặt gần nhau**. Thuật toán khớp quanh các cụm đó với độ chính xác cao (đó chính là lý do "quét đúng mép" tồn tại). Sai số 15–20 điểm đủ để bạn rơi từ "trong cụm" ra "ngoài cụm". Level tĩnh trong một thị trường chạy 24h là một giả định sai âm thầm.

**Rule đo được:**
- **Đo lại toàn bộ range levels mỗi sáng** như một bước cứng trong pre-market routine (không kế thừa số của hôm qua) — cùng nguyên tắc với câu hỏi mở phiên bên [[59-Daily-Bias]].
- Dùng anchored fib trên chart (neo vào swing, tự cập nhật khi wick giãn) thay vì kẻ tay mức giá tĩnh.
- Alert đặt ở *vùng* (dải giá quanh OTE) chứ không ở một tick.

### 16.2. Nhóm B — Kích thước range, regime và lịch

#### EC-01 — Range cực hẹp (W < ~1.5×ATR của TF)

- *Class:* noise hoặc compression.
- *Interp:* balance ở scale nhỏ hơn TF, hoặc anchors bị phân loại sai scale.
- *Structure:* một bar đơn lẻ có thể quét toàn bộ range → p không ổn định.
- *Trading:* không dùng cho location; leo lên parent. Có thể xem như tín hiệu compression.
- *Invalidation:* vô nghĩa — mọi close đều có thể "phá" range.
- *Backtest:* lọc W/ATR ≥ w_min; test riêng xem range hẹp có đi trước expansion không (volatility clustering là stylized fact đã biết — cần baseline).

#### W3. Range quá rộng — khi "discount" vẫn còn cách đáy 300 điểm

**Hiện tượng:** D1 range của NQ sau một tuần biến động rộng 800 điểm. Giá "vào discount" (dưới 50%) — nhưng dưới đó vẫn còn 300 điểm không gian. Long "vì đang discount" rồi chịu 3 lần stop trước khi giá tìm được đáy thật ở deep discount.

**WHY — vì sao % không phải là khoảng cách:** premium/discount là **xác suất có điều kiện, không phải mức giá**. "Ở discount" chỉ nói rằng bên mua có lợi thế vị trí *tương đối*; nó không nói lệnh mua thật nằm ở đâu. Lệnh thật (theo §14.2 cơ chế 1) nằm tại các PD array cụ thể — FVG, OB — và trong range rộng, các array đó phân bố thưa. Khoảng giữa hai array là "đất trống": không có lệnh chờ nào ở đó, nên không có lý do nào để giá dừng ở đó. Range càng rộng, sai số của phép đo % càng lớn so với sai số của một array cụ thể.

**Rule đo được:**
- Range rộng bất thường (so với ADR trung bình 20 ngày, ví dụ > 1.5×): **cấm trade theo nửa range** — chỉ trade theo quadrant + array cụ thể (deep discount + FVG/OB, không phải "dưới 50%").
- Kết hợp ma trận §4.1: vị trí phải cộng hưởng ở cả hai tầng (D1 discount **và** H1 discount) và entry phải nằm *tại một array*, không nằm giữa đất trống.
- Journal: `range_width_vs_adr` — biến này giải thích một phần lớn các lệnh "đúng vùng, sai 100 điểm".

*Gộp EC-02 (range cực rộng, W > ~8–10×ATR D1):* class = HTF container, có thể trải qua nhiều regime; EQ nằm xa vùng giá hoạt động; P/D thô — một pullback 3 ATR có thể không đổi nhãn. Chỉ dùng làm context; location lấy từ child range; thường bị temporal invalidation trước structural. Backtest: chia bin W/ATR, kiểm tra location còn mang thông tin ở bin nào.

#### EC8. Range bị "nén" bất thường trước kỳ nghỉ lễ/tuần đáo hạn hợp đồng — kích thước tuyệt đối đánh lừa quadrant

**Tình huống:** tuần lễ Tạ ơn (Mỹ) hoặc tuần đáo hạn hợp đồng quý trên ES/NQ, range D1 co lại chỉ bằng 40% ADR bình thường do thanh khoản mỏng và nhiều tổ chức đứng ngoài. Quadrant vẫn tính ra "deep discount/deep premium" như bình thường nhưng con số đó gần như vô nghĩa.

**Vì sao bẫy được cả trader có kinh nghiệm:** công thức Fibonacci/quadrant vẫn chạy ra số đẹp bất kể range có ý nghĩa cấu trúc hay không — phần mềm/chart không tự cảnh báo "range này quá hẹp so với bình thường".

**Cách nhận diện sớm:** luôn so sánh độ rộng range hiện tại với ADR(20) trước khi tin vào quadrant; nếu range < 0.5× ADR trong tuần có yếu tố lịch/đáo hạn đặc biệt, hạ độ tin cậy.

**Cách xử lý:** trong các tuần thanh khoản mỏng theo lịch (lễ Mỹ/Anh, đáo hạn hợp đồng, giữa kỳ nghỉ Giáng sinh-Tết Dương), chuyển hẳn sang range của khung cao hơn (tuần trước đó) làm tham chiếu chính, chỉ dùng range trong tuần mỏng cho execution vi mô.

#### EC-03 — Range không có displacement rõ

- *Class:* leg "grind", nhiều overlap.
- *Interp:* có thể là trend do hấp thụ dần, hoặc chỉ là corrective leg của scale lớn hơn.
- *Structure:* origin có D-score thấp; BOS có thể biên (close vừa đủ vượt).
- *Trading:* độ tin cậy thấp hơn; cân nhắc container thay vì leg DR.
- *Invalidation:* hypothesis: dễ bị phá hơn.
- *Backtest:* chia theo D-score của leg; HYP-DR-006.

#### EC-23 — Range expansion (volatility regime tăng)

- *Class:* ATR giãn.
- *Interp:* regime mới.
- *Structure:* nếu θ\* đo bằng ATR *hiện tại*, swing cũ bị "hạ cấp" giả tạo; nếu đo bằng ATR *lúc hình thành*, scale ổn định.
- *Trading:* khuyến nghị: θ\* dùng ATR tại known_at của swing.
- *Invalidation:* context invalidation nếu ATR_now / ATR_formation > r.
- *Backtest:* so sánh hai cách chuẩn hóa.

#### EC-24 — Range compression

- *Class:* swing liên tiếp nhỏ dần (tam giác, wedge).
- *Interp:* balance thu hẹp; liquidity tích tụ hai phía.
- *Structure:* container co lại; θ\* của swing mới giảm dần.
- *Trading:* location ít giá trị; boundaries là DOL hai phía; chờ expansion.
- *Invalidation:* breakout có acceptance.
- *Backtest:* hướng breakout có dự báo được bởi D1 direction không? (HYP-DR-010)

#### CX-05 — Cấu trúc "sạch" trong thị trường không hiệu quả.

Random walk tạo ra chuỗi HH–HL trông hoàn hảo khá thường xuyên. Một range dựng trên chuỗi đó "đúng quy tắc" nhưng không có dòng tiền có hướng phía sau. *Why misleading:* sự hiện diện của cấu trúc không chứng minh drift. Kiểm tra: efficiency ratio thấp + displacement yếu → nghi ngờ.

### 16.3. Nhóm C — Nhiều range hợp lệ cùng lúc

#### EC2. Range lồng nhau đa khung cho Premium/Discount mâu thuẫn — không phải lúc nào cũng "chọn sai"

**Tình huống:** D1 range cho giá đang discount 25%; H1 range con (mới hình thành trong 2 ngày gần nhất) cho cùng mức giá đó đang premium 60%. Cả hai range đều vẽ đúng kỹ thuật (có displacement, có liquidity ở hai đầu).

**Vì sao bẫy được cả trader có kinh nghiệm:** phản xạ tự nhiên là nghĩ "một trong hai range chắc vẽ sai" và cố tìm lỗi — nhưng thực ra đây là hệ quả TỰ NHIÊN của cấu trúc fractal (§4.1), không phải lỗi. Trader mất thời gian "sửa" một range vốn dĩ không sai, hoặc tệ hơn, chọn tin range nào ủng hộ thiên kiến sẵn có của mình.

**Cách nhận diện sớm:** khi thấy hai tầng range mâu thuẫn, đừng tìm "range nào sai" — thay vào đó hỏi "tầng nào GOVERNS quyết định gì" theo đúng quy tắc §4.1.

**Cách xử lý:** HTF quyết định hướng được phép; LTF chỉ tinh chỉnh thời điểm/giá entry. Khi mâu thuẫn, chờ LTF tự đồng thuận với HTF (retrace hoặc MSS riêng) thay vì trade ngay theo LTF.

*Gộp EC-06 (range nằm trong range khác):* child là một pha của parent; boundaries của child là internal liquidity của parent; child bị phá **không** invalidate parent trừ khi phá cả protected của parent. Biến backtest: `nesting_relation` (§4.1). Dữ liệu v0.2: nested-consistent không tốt hơn nested-conflicting một cách phân biệt được.

#### EC-07 — Range chồng lấn một phần

- *Class:* overlapping, `nesting_clean = FALSE`.
- *Interp:* hai scale không đồng bộ (H1 leg bắt đầu trước D1 BOS).
- *Structure:* không có quan hệ parent-child sạch.
- *Trading:* giảm confidence; ghi nhận.
- *Invalidation:* đánh giá riêng từng range.
- *Backtest:* phân tích riêng nhóm này.

#### W5. Ba tầng range đều "hợp lệ" — và sự tê liệt của người phân tích giỏi

**Hiện tượng:** sau nhiều ngày consolidation, chart có 3 range lồng nhau đều đúng sách: range tuần (external chưa lấy hai đầu), range 3 ngày, range trong ngày. Ba bản đồ cho ba kết luận premium/discount khác nhau. Người mới chọn bừa; người giỏi… phân tích cả buổi rồi không trade được — cả hai đều thua theo cách của mình.

**WHY — vì sao nhiều range hợp lệ cùng lúc là một *thông điệp*, không phải một bài toán:** theo §14.2 cơ chế 3, giá di chuyển khi có tồn kho cần cân và pool rõ để nhắm tới. Ba tầng range mơ hồ chồng nhau nghĩa là **không có delivery nào đang dang dở** — thuật toán không nợ ai điều gì ở cả ba tầng. Đó chính là trạng thái "chưa chọn phía" quanh EQ (§14.4.7) phóng to lên nhiều tầng. Thị trường đang *tích luỹ thanh khoản hai phía để chuẩn bị cho expansion* — và expansion đó sẽ chỉ bắt đầu bằng một cú quét external của tầng LỚN nhất.
**Câu trả lời đúng không phải "chọn range nào" mà là "chưa có gì để trade cho tới khi tầng lớn nhất bị quét."**

**Rule đo được:**
- Khi ≥2 tầng range cho kết luận mâu thuẫn và không tầng nào có draw rõ vượt trội → ghi **No Trade / chờ sweep external của tầng cao nhất** vào pre-market note. Đây là một kết luận, không phải sự bất lực.
- Sau cú sweep external tầng cao nhất: các tầng dưới thường tự sắp hàng lại trong 1–2 phiên — lúc đó ma trận §4.1 mới dùng được.
- Journal: `nested_range_conflict` (true/false) — thống kê các lệnh vào trong trạng thái conflict; win rate của nhóm này thường là con số thuyết phục mình đứng ngoài tốt hơn mọi lời khuyên.

> [!success] Tổng kết mục War Stories
> Tầng WHY chung: dealing range hoạt động vì nó vẽ đúng **bản đồ lệnh** (§14.2 cơ chế 1), đúng **phiên đấu giá** (§14.2 cơ chế 2), đúng **chu kỳ cân tồn kho** (§14.2 cơ chế 3). Nó phản bội khi bản đồ vẽ trên feed sai (W1), khi đọc nhầm "sạc lại" thành "chết" (W2), khi nhầm % với vị trí lệnh thật (W3), khi level tĩnh trong thị trường động (W4), và khi ép mình trade lúc thuật toán không nợ ai điều gì (W5). Journal fields: `range_context`, `range_width_vs_adr`, `nested_range_conflict`.

#### CX-02 — D1 range hiển nhiên nằm trong W1 bearish leg.

D1 có chuỗi HH–HL sạch, nhưng toàn bộ nằm trong một nhịp hồi của W1 downtrend, dưới W1 protected high. *Why misleading:* "discount" của D1 là một vị trí bên trong *premium retracement* của W1 — bạn đang mua trong vùng mà scale lớn hơn coi là nơi bán. Hiển nhiên ở một scale, sai ở scale trên.

#### CX-09 — Leg DR vs container DR ở đầu trend.

Sau MSS bullish, leg DR = sweep low → high mới. Nhưng một swing high cũ (của downtrend trước) còn sống phía trên → container DR = sweep low → old high. Giá tại một mức có thể là premium của leg và discount của container. *Why:* hai họ range trả lời hai câu hỏi khác nhau (mục 1.2, kết luận 3).

#### CX-10 — IPDA 20 vs 40 vs 60.

Trong một uptrend dài có một nhịp hồi mới: cửa sổ 20 ngày chứa nhịp hồi → giá ở discount; cửa sổ 60 ngày chứa cả trend → giá ở premium. *Why:* lookback dài hơn "nhìn thấy" nhiều giá thấp hơn. Không có cửa sổ "đúng" — chỉ có cửa sổ khớp với horizon.

#### CX-11 — Leg discount / trend premium

(giá 116 trong ví dụ A–F). Mua ở "discount" của E–F là mua ở premium 0.64 của A–F. Nhãn nào đúng phụ thuộc câu hỏi.

#### CX-12 — H1 discount trong D1 premium.

Sau một run mạnh, giá ở p_D1 = 0.85. Một H1 bullish setup "ở discount H1" vẫn là mua gần đỉnh D1 leg; room đến DOL có thể < 1R. *Why:* child location không bù được parent location khi DOL gần.

#### CX-14 — Discount trong bearish DR.

Giá ở p = 0.2 của bearish leg DR. "Discount" ở đây là nơi *chốt lời short*, không phải nơi mua. *Why:* P/D không mang direction; direction phải đến từ nơi khác.

#### CX-15 — Consolidation: container discount = leg premium

(Case C, giá 2,320). Hai nhãn ngược nhau đều "đúng" theo frame của chúng. *Why:* regime quyết định frame nào có thẩm quyền.

### 16.4. Nhóm D — Equilibrium và location đổi nghĩa

#### EC3. Equilibrium bị test nhiều lần mất ý nghĩa — EQ không phải mức cố định miễn nhiễm

**Tình huống:** giá dao động quanh EQ của một range trong 4-5 phiên liên tiếp, chạm đi chạm lại vùng 48-52% mà không breakout dứt khoát về phía nào. Đến lần chạm thứ 5-6, trader vẫn coi đây là "vùng ra quyết định" quan trọng và cố đoán hướng breakout.

**Vì sao bẫy được cả trader có kinh nghiệm:** EQ có sức nặng lý thuyết (value area, xem mục 14) nhưng sức nặng đó **suy giảm dần theo số lần test** giống hệt cơ chế IRL age decay ([[16-Internal-External-Range-Liquidity-IRL-ERL]] Case Study 1) — thị trường "quen" với mức đó và ngày càng ít nhà giao dịch coi đó là điểm quyết định thật sự, khiến phản ứng tại EQ ngày càng yếu và nhiễu hơn.

**Cách nhận diện sớm:** đếm số lần giá chạm dải 45-55% của range trong N phiên gần nhất; từ lần chạm thứ 4 trở đi, hạ kỳ vọng phản ứng mạnh tại EQ.

**Cách xử lý:** sau nhiều lần test EQ không dứt khoát, ưu tiên chờ breakout có acceptance rõ + displacement thay vì tiếp tục coi mọi lần chạm EQ là tín hiệu. Nếu phải trade, chuyển kỳ vọng sang "range đang chuẩn bị mở rộng" (giống mục W5) thay vì "EQ sẽ đảo chiều".

![[Dealing-Range-EdgeB-EQDecayTouches.svg|1516]]
*Sơ đồ: giả thuyết EQ decay — phản ứng giảm dần theo số lần chạm.*

> [!warning] Lưu ý — số liệu trong sơ đồ trên chưa được kiểm chứng
> Các con số trong sơ đồ (N=140 range, win rate 61% → 19%) **không có dataset backtest tương ứng trong vault** — coi là minh họa của một giả thuyết, không phải kết quả. Baseline bắt buộc khi test: dưới martingale, xuất phát từ p > 0.5, xác suất chạm EQ trước H\* là 2(1 − p) — EQ được chạm nhiều chỉ vì nó ở gần (14.3.7). **[BACKTEST REQUIRED]**

#### EC5. Trend mạnh không bao giờ về discount — chờ mãi một mức không tồn tại

**Tình huống:** NQ trong một xu hướng tăng liên tục 3 tuần, mỗi lần retrace chỉ về khoảng 35-40% của leg vừa tạo (discount nông) rồi tiếp tục tăng. Trader đặt limit chờ giá về dưới 20% (deep discount) theo đúng sách vở quadrant — lệnh không bao giờ khớp trong suốt cả xu hướng.

**Vì sao bẫy được cả trader có kinh nghiệm:** quadrant theory (§14.4.7) dạy "deep discount là vùng conviction cao nhất", điều này đúng trong **range environment** nhưng không đúng trong **trending regime** — nơi range liên tục "trượt" theo hướng trend và deep discount của range cũ đã bị bỏ lại phía sau vĩnh viễn.

**Cách nhận diện sớm:** kiểm tra cấu trúc swing gần nhất — nếu là chuỗi higher-high/higher-low (hoặc lower-high/lower-low) liên tục không có swing ngược đáng kể, đó là trending regime; đừng áp dụng kỳ vọng deep-discount của range regime.

**Cách xử lý:** trong trending regime, đo Premium/Discount trên **range của leg đang sống** (nhịp gần nhất), chấp nhận entry ở discount nông kèm xác nhận continuation (MSS/displacement) thay vì chờ một mức deep discount có thể không bao giờ tới.

*Gộp EC-22 (trend continuation — chuỗi leg DR):* protected low dịch lên theo từng BOS; parent trend DR giãn liên tục nên P/D của parent ngày càng premium → xung đột leg-discount / parent-premium ngày càng phổ biến ở cuối trend. Invalidation theo protected low hiện hành. Backtest: HYP-DR-004 theo "tuổi" trend (leg thứ mấy).

#### EC-19 — External high mới, low cũ còn nguyên

- *Class:* extension không có HL đạt θ.
- *Interp:* impulse kéo dài.
- *Structure:* W tăng, EQ tăng một nửa phần extension; một mức từng là "discount nông" trở thành "discount sâu".
- *Trading:* cập nhật tọa độ POI; nhớ rằng R:R đến termination thay đổi.
- *Invalidation:* protected low không đổi.
- *Backtest:* đảm bảo tọa độ dùng tại thời điểm entry là tọa độ *tại thời điểm đó*, không phải sau extension.

#### CX-13 — Range cập nhật đổi nhãn vùng giá.

Sau new HL + BOS, protected low dịch lên. Vùng từng là "discount sâu" của range cũ giờ nằm *dưới* protected low mới → p < 0 — không còn là discount mà là **vùng invalidation** của range mới. *Why:* tọa độ phụ thuộc thời điểm; một POI "đẹp" hôm qua có thể đã mất location hôm nay.

### 16.5. Nhóm E — Liquidity và sweep

#### EC-04 — Range với nhiều equal highs ở đỉnh

- *Class:* liquidity cluster phía trên (ICT: relative equal highs).
- *Interp:* mức "hiển nhiên" → nhiều stops có thể nằm trên.
- *Structure:* boundary trên là một *vùng*; H\* = max của cluster.
- *Trading:* ứng viên DOL mạnh; không kỳ vọng nó "giữ" làm resistance; không đặt stop short ngay trên cluster.
- *Invalidation:* bị lấy = completion của DOL đó, không phải invalidation của bullish DR.
- *Backtest:* P(cluster bị lấy trong N bar) so với swing đơn lẻ *cùng khoảng cách* (kiểm soát distance là bắt buộc).

#### EC-05 — Range với nhiều equal lows ở đáy

- *Class:* SSL cluster ngay dưới protected low.
- *Interp:* stops của long nằm trong pool dễ đoán.
- *Structure:* protected anchor có "liquidity chưa bị lấy" phía sau → rủi ro sweep cao.
- *Trading:* đặt stop ngoài cluster với buffer, hoặc chờ sweep + reclaim.
- *Invalidation:* sweep ≠ invalidation; cần acceptance rule.
- *Backtest:* so sánh tỷ lệ bị stop giữa "origin có cluster chưa lấy" vs "origin đã lấy liquidity" (HYP-DR-007).

#### EC-11 — Range sau liquidity sweep

- *Class:* origin là sweep extreme (ICT 2022: sweep → MSS → leg mới).
- *Interp:* origin đã "tiêu thụ" liquidity phía sau nó.
- *Structure:* L-score cao; nhiều practitioner coi là origin mạnh nhất.
- *Trading:* ứng viên primary leg DR.
- *Invalidation:* phá sweep extreme có acceptance → setup thất bại rõ ràng.
- *Backtest:* HYP-DR-007 — origin-after-sweep có tỷ lệ bị phá thấp hơn origin thường?

#### EC-12 — Range trước liquidity sweep

- *Class:* origin với liquidity chưa lấy ngay phía sau.
- *Interp:* "unswept origin".
- *Structure:* protected anchor có rủi ro bị sweep.
- *Trading:* buffer stop hoặc chờ.
- *Invalidation:* sweep → SWEPT_L, *không* invalid.
- *Backtest:* đối xứng với EC-11.

> [!note] Dữ liệu v0.2 cho EC-11 / EC-12
> Hai entry trên nói về origin *hình thành* bởi sweep (EC-11) hoặc còn liquidity phía sau (EC-12) — HYP-DR-007, chưa test. Sự kiện khác — origin *bị sweep trong đời DR* — đã đo: P(EXTENDED) giảm từ ~0.58 xuống ~0.24–0.28 (§5.4.3). Đừng trộn hai câu hỏi.

#### EC-13 — Failed breakout (bị từ chối ngay)

- *Class:* SWEPT_H (không đạt acceptance).
- *Interp:* liquidity trên H\* bị lấy, lệnh đối ứng hấp thụ.
- *Structure:* range giữ nguyên; DOL phía trên đã completed.
- *Trading:* hypothesis reversal về phía đối diện (Turtle Soup / sweep reversal) — cần LTF MSS.
- *Invalidation:* nếu giá quay lại vượt H\* có acceptance → extension.
- *Backtest:* P(chạm L\* hoặc EQ trước H\* + x) sau failed breakout vs martingale baseline từ cùng p.

#### W2. Seek & Destroy — ngày quét cả hai đầu: range không chết, nó được "sạc lại"

![[Dealing-Range-War-Seek-Destroy-Recharge.svg|1516]]
*Sơ đồ: wick qua BSL, wick qua SSL, đóng ngày giữa range — cả hai external vừa được nạp thanh khoản mới; re-map lúc này là lỗi.*

**Hiện tượng:** ngày S&D quét cả hai external rồi đóng giữa range. Phản xạ sai phổ biến: "cả hai đầu đã bị lấy → range chết → vẽ range mới nhỏ hơn bên trong". Range mới nhỏ hơn đó cho premium/discount nhiễu và hôm sau bị nghiền.

**WHY — vì sao range sau S&D lại *mạnh hơn*:** quay về cơ chế nền §14.2 cơ chế 1 — stop là hàng tiêu hao, nhưng **cú quét cũng là máy sản xuất stop mới**. Wick qua BSL kích hoạt buy stops cũ *và* kéo một lớp breakout trader mới vào Long (stop của họ giờ nằm dưới); wick qua SSL làm điều đối xứng. Đóng ngày giữa range nghĩa là thuật toán đã **kiểm tra cả hai phía và từ chối cả hai** — đó là bằng chứng đắt giá nhất có thể có rằng biên range đúng. Về mặt đấu giá (§14.2 cơ chế 2): hai mức từ chối vừa được *tái xác nhận*, nên EQ cũ càng đáng tin. Re-map chỉ được phép khi có **acceptance** (đóng thân + giữ ngoài) — wick hai phía là điều ngược lại của acceptance.

**Rule đo được:**
- Sau ngày S&D: **giữ nguyên range + EQ**, nâng độ tin của hai external thêm một bậc.
- Sweep *lần hai* cùng một đầu trong những ngày kế = tier thấp hơn lần đầu (pool đã mỏng đi) — điều chỉnh kỳ vọng reversal tương ứng.
- Break thật qua external sau ngày S&D thường cần catalyst (tin lớn, mở tuần) — không có catalyst mà "phá" thì nghi ngờ gấp đôi.
- Journal: `range_context` (fresh / one_side_swept / both_swept_SD).

> [!warning] W2 sau v0.2
> W2 nói về **container range** bị quét **cả hai đầu** trong một ngày (Seek & Destroy) — khác với sweep protected origin của leg DR. Phần "range sau S&D *mạnh hơn*" là [HYPOTHESIS] chưa test; phần tương tự cho leg DR đã được thay bằng rule mới ở §5.4.3 (sweep origin hạ base-rate continuation).

#### EC-15 — Wick ra ngoài range

- *Class:* SOFT violation.
- *Interp:* sweep.
- *Structure:* không đổi.
- *Trading:* liquidity map cập nhật.
- *Invalidation:* không.
- *Backtest:* baseline: random walk tạo ~43% "sweep" ở lần vượt đầu tiên.

### 16.6. Nhóm F — Vòng đời, cập nhật và invalidation

#### EC-09 — Range trong expansion

- *Class:* FORMING.
- *Interp:* termination đang chạy.
- *Structure:* p ≈ 1 liên tục; EQ di chuyển theo giá.
- *Trading:* không ra quyết định location; nếu trade, dùng model continuation khác, không phải location model.
- *Invalidation:* chưa áp dụng.
- *Backtest:* loại bỏ mọi entry dựa trên location khi state = FORMING (nếu không sẽ có look-ahead: bạn đang dùng một range chưa tồn tại).

#### EC-14 — Breakout được chấp nhận rồi bị reclaim (acceptance failure)

- *Class:* trường hợp khó nhất: rule acceptance đã thỏa, state đã đổi, rồi giá quay lại.
- *Interp:* acceptance giả; rule quá lỏng hoặc regime đổi.
- *Structure:* **không được âm thầm "hoàn tác" state** — phải ghi event `reclaim_after_acceptance` và tạo range mới theo rule.
- *Trading:* đây là nơi nhiều trader "vẽ lại" range để hợp với kết quả.
- *Invalidation:* theo rule, không theo cảm giác.
- *Backtest:* đo tần suất acceptance failure theo k; nếu cao, k quá nhỏ.

#### EC-16 — Close ra ngoài range (một lần)

- *Class:* MEDIUM → PENDING.
- *Interp:* có thể là break hoặc failed break.
- *Structure:* chờ acceptance.
- *Trading:* không hành động dựa trên range cho đến khi state rõ.
- *Invalidation:* phụ thuộc k, m.
- *Backtest:* P(acceptance | 1 close) — để chọn k có cơ sở.

#### EC-17 — Nhiều close ra ngoài range

- *Class:* HARD.
- *Interp:* phía protected → invalidation; phía termination → extension.
- *Structure:* state đổi.
- *Trading:* xây range mới.
- *Invalidation:* đã xảy ra.
- *Backtest:* không có gì đặc biệt — ngoài việc kiểm tra hậu quả so với EC-16.

#### F-5. Range trở nên obsolete / temporal invalidation (gộp EC-18, CX-24)

- *Class:* price invalidation (giá đã rời xa, |p| rất lớn — ví dụ p = 2.0, CX-22) hoặc temporal invalidation (range quá cũ).
- *Ví dụ (CX-24):* range 90 phiên tuổi, không có tương tác 40 phiên, đã có cấu trúc mới cùng scale. Giữ nó là thiên kiến "tôi đã vẽ nó nên nó quan trọng".
- *Trading:* thay bằng range mới hoặc parent; ngưỡng x·W hoặc T_max là HEURISTIC.
- *Dữ liệu v0.2:* đời sống trung vị của leg DR θ = 2 từ ACTIVE tới khi kết thúc chỉ 8–12 bar (§5.2.2) — "range cũ" đến nhanh hơn trực giác.
- *Backtest:* giá trị location theo tuổi range (freshness).

#### EC-20 — External low mới, high cũ còn nguyên

- *Class:* trong bullish DR = phá protected low → MSS (nếu acceptance).
- *Interp:* bullish câu chuyện ở scale k chết.
- *Structure:* container mới = high cũ → low mới; bearish leg DR có origin là swing high (cấp k) nơi leg phá xuất phát — có thể là một LH thấp hơn H\*.
- *Trading:* chuyển sang bearish context ở scale k, kiểm tra parent.
- *Invalidation:* bullish DR INVALIDATED.
- *Backtest:* đo tần suất "MSS thật" vs "MSS rồi reclaim".

#### EC-21 — Trend reversal

- *Class:* range transition.
- *Interp:* ví dụ: sweep H\* → MSS xuống → bearish leg mới với origin = sweep high.
- *Structure:* range mới chỉ usable khi termination của leg giảm đóng (lag).
- *Trading:* khoảng trống giữa invalidation cũ và range mới ACTIVE là thời gian *không có location frame* ở scale k.
- *Invalidation:* sweep high bị phá có acceptance → reversal thất bại.
- *Backtest:* đo "location blackout" — thời gian không có range ACTIVE.

#### EC4. IRL-ERL flip khi range mở rộng — external cũ trở thành internal mới

**Tình huống:** một swing high từng là external liquidity (BSL) của range D1 bị phá bằng acceptance thật (đóng thân nến ngoài range, giữ được). Trader vẫn tiếp tục coi mức đó là "target BSL" cho lệnh cũ, không nhận ra vai trò của nó đã đổi thành internal liquidity/hỗ trợ cho range mới.

**Vì sao bẫy được cả trader có kinh nghiệm:** vai trò external/internal của một mức giá không cố định — nó phụ thuộc vào **range nào đang hoạt động tại thời điểm đó** (đúng nguyên tắc phân dạng đã nêu ở [[16-Internal-External-Range-Liquidity-IRL-ERL]] mục Nâng cao "Fractal nesting"). Trader quen nhìn một mức giá theo vai trò cũ dễ bỏ lỡ khoảnh khắc nó đổi vai trò.

**Cách nhận diện sớm:** mỗi khi có acceptance (không phải wick) qua một đầu range, ngay lập tức tự hỏi "mức vừa bị phá giờ đóng vai trò gì trong range MỚI?" — nó gần như luôn chuyển từ external sang internal của bản đồ mới.

**Cách xử lý:** re-map ngay theo quy trình §5.4.2; đừng giữ target cũ dựa trên vai trò external đã hết hiệu lực. Cú retrace về mức đó sau breakout là cơ hội continuation, không phải reversal.

#### CX-16 — Old high trở thành reference trong range mới.

D (118) của range C–D, sau khi bị phá, nằm tại p = 0.46 của E–F — gần EQ. Nếu giá hồi về đó, "old high" + "EQ" trùng nhau. *Why useful:* level cũ vẫn là nơi giao dịch đã diễn ra; chỉ vai trò đổi (spent → reference).

#### CX-17 — Parent trend range giữ thẩm quyền cho target lớn.

Sau năm leg DR mới, A–F vẫn trả lời "trend đã đi bao xa" và vẫn chứa protected low của trend. *Why useful:* R1 — direction đến từ range cao nhất còn protected.

#### CX-18 — Sau failed breakout, range cũ được khôi phục.

Trader "thay" range bằng range mới ngay khi giá close vượt boundary lần đầu; khi reclaim xảy ra, frame cũ mới là frame đúng. *Why useful:* đây là lý do cần PENDING state thay vì đổi range ngay.

#### CX-19 — Container cũ làm "origin zone" sau expansion.

Top của container cũ (2,392 trong Case C) trở thành mức retest. *Why useful:* acceptance/flip được đánh giá *so với boundary cũ*.

#### CX-20 — IPDA 60 làm liquidity map HTF.

Leg DR D1 thay đổi liên tục, nhưng 60-day high/low giữ nguyên hàng tuần, cung cấp external liquidity ổn định. *Why useful:* không phải range nào cũng phải là location frame; một số chỉ là liquidity map.

#### CX-21 — HARD invalidation.

Protected anchor bị phá bằng displacement, k close bên ngoài, không reclaim. Tiếp tục dùng range này là "cầu nguyện", không phải phân tích.

#### CX-22 — Price invalidation.

Giá đã đi xa termination 1×W; p = 2.0. Tọa độ không còn phân biệt gì. Cần frame mới.

#### CX-23 — Context invalidation do regime shock.

Một quyết định ngân hàng trung ương làm ATR tăng gấp đôi. Anchors hình thành trong regime cũ phản ánh mức định giá cũ; θ\* chuẩn hóa theo ATR cũ.

#### EC9. Range mở màn bằng Opening Gap — không có leg thật để đo

![[Dealing-Range-EdgeB-OpeningGapRange.svg|1516]]
*Sơ đồ (minh họa): NQ futures — Sunday open nhảy gap ~140 điểm (Fri close 20,340 → Sun open 20,480), chưa có displacement nào tạo swing mới.*

**Tình huống:** đầu tuần, giá mở cửa cách xa close thứ Sáu. Trader vẽ range mới từ mép gap như thể đó là một leg.

**Vì sao bẫy được cả trader có kinh nghiệm:** gap là bước nhảy của giá khi thị trường đóng, **không phải một leg có giao dịch** — không có swing nào được tạo bởi displacement thật bên trong khoảng trống đó, nên không có anchor có structural consequence.

**Cách xử lý:** giữ range D1/W1 trước gap làm khung tạm thời cho tới khi phiên Á/London đầu tuần tạo swing đầu tiên bằng displacement thật. Phương án thay thế (sơ đồ nêu): dùng hai mép gap (Fri close – Sun open) như một range tạm thời kiểu CBDR — **[HYPOTHESIS]**.

**Liên hệ:** range tạm thời này ở state FORMING — không đo location trên nó (3.4.5, 5.5).

*Dữ liệu thật cho EC9:* parent leg DR ở Real 5 ([[#4.1. Multiple / Nested / Overlapping Ranges|§4.1]]) bắt đầu bằng gap mở cửa 23/04/2017; nửa discount của parent (vùng giá trước gap) không bao giờ được revisit trong suốt đời DR.

---

## 17. Case Studies

Ba loại case trong note, đọc với ba mức tin cậy khác nhau:

| Loại | Ở đâu | Tính chất | Dùng để |
|---|---|---|---|
| **Dữ liệu thật, dựng bằng thuật toán** | Real 1–2 (§6), Real 3 (§5.4), Real 4 (§4.4), Real 5 (§4.1) | OHLC thật, không chọn tay, có ex-ante/ex-post | Thấy quy tắc chạy trên dữ liệu thật — *minh họa*, không phải thống kê |
| **Case giả định có cấu trúc T0–T5** | §17.1 (A–E) | Số liệu hypothetical, tái dựng không hindsight | Luyện quy trình ra quyết định từng bước |
| **Case lưu trữ (narrative)** | §17.2 (Case 0–6) | Chi tiết như giao dịch thật nhưng **không có log tương ứng** trong `04 - Backtesting/` hay `05 - Live Trading Journal/` | Bài học định tính về lịch tin, options expiry, funding, giao thức anchor |

Thống kê thật nằm ở [[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3]] — không case nào ở mục này được dùng làm bằng chứng cho edge.

### 17.1. Case Studies

> **Tất cả case study dưới đây dùng số liệu giả định (hypothetical)** được thiết kế để minh họa quy trình. Chúng không phải dữ liệu lịch sử và kết cục (T5) được chọn để minh họa — không phải bằng chứng. Mỗi case được viết theo nguyên tắc **no-hindsight**: tại mỗi mốc T, chỉ dùng thông tin đã có.

#### Case Study A — Uptrend (hypothetical EURUSD)

![[Dealing-Range-v01-20-Case-A-Uptrend.svg|1516]]
*Sơ đồ: Case A (hypothetical) — D1 OTE → H1 sweep + MSS → M5 entry; T0–T4 chỉ dùng thông tin đã có.*

**Context (D1).** Direction BULL ở scale D1 (θ_min = 2×ATR_D1; ATR_D1 ≈ 70 pips). Leg gần nhất: swing low 1.0750 — chính nó là một sweep của swing low trước đó 1.0762 (origin_swept_liq = TRUE) — tạo displacement và close phá swing high 1.0905 (BOS). Termination: 1.0980, đã đóng (giá hồi 1.0980 → 1.0840 = 2.0 ATR).

**Swings & classification (D1).**

| Swing | Giá | θ\* | Role tại T0 |
|---|---|---|---|
| Prior low | 1.0762 | 2.6 | SWEPT (bởi 1.0750) |
| Origin | 1.0750 | ≥3 | PROTECTED |
| Broken high | 1.0905 | 2.2 | SPENT → reference (old high) |
| Termination | 1.0980 | ≥2 | TARGET |
| Old D1 high | 1.1040 | 4.5 | ALIVE — external, ngoài range |

**Dealing Range (D1 leg):** 1.0750 → 1.0980, W = 230 pips (3.3 ATR), EQ = 1.0865, OTE (p 0.21–0.38) = 1.0798–1.0837.

**Liquidity.** SSL: dưới 1.0750 (protected low — rủi ro sweep). BSL: trên 1.0980 và trên 1.1040 (HTF, θ\* lớn). Old high 1.0905 nằm tại p = 0.67 — trong premium.

**DOL.** Primary: BSL trên 1.0980 (termination). Extended: 1.1040. M_ratio (từ giá ≈ 1.0830): (1.0980 − 1.0830)/0.0230 = 0.65 → scale-matched.

**Location robustness.** Candidates: D1 leg (p = 0.35, D); IPDA-40 container giả định 1.0690–1.1040 (p = 0.40, D); IPDA-20 ≈ D1 leg (D). LRI = 1.0. **D1 GATE = PASS.**

**H1 refinement.**

```text
T0 (D1 close): D1 range ACTIVE; giá 1.0860 (p = 0.48, gần EQ). Chưa ở OTE → chưa tìm setup.
T1: H1 tiếp tục giảm, internal structure H1 bearish (LH 1.0858 là swing bảo vệ nhịp hồi).
    H1 equal lows 1.0820 / 1.0822 hình thành → SSL H1 (internal liquidity của D1 range).
    Thông tin chưa có: đáy nhịp hồi ở đâu.
T2: Giá quét xuống 1.0808 (dưới equal lows, trong D1 OTE, trên D1 protected 1.0750).
    Tại T2 ta CHƯA biết 1.0808 là đáy. Chỉ biết: SSL H1 đã bị lấy.
T3: H1 displacement tăng, close phá 1.0858 → H1 MSS bullish (phá swing bảo vệ nhịp hồi).
    1.0808 trở thành PROTECTED ở scale H1 (known_at = T3).
    H1 leg DR: 1.0808 → high hiện tại (FORMING).
T4: Giá tạo high 1.0872 rồi hồi ≥ θ_min(H1) → H1 leg DR ACTIVE: 1.0808–1.0872, EQ 1.0840.
    Bullish FVG H1: 1.0826–1.0834 → p_H1 = 0.28–0.41, p_D1 = 0.33–0.37 (trong D1 OTE).
    Nested-consistent. H1 GATE = PASS.
```

**M5 execution.** Giá quay về FVG H1 trong London session. M5: sweep một M5 swing low 1.0823, M5 MSS phá M5 LH, displacement, M5 FVG. Entry 1.0831, stop 1.0819 (dưới M5 swing low, *trong* H1 protected 1.0808) = 12 pips. Target 1: 1.0872 (H1 termination, 3.4R); Target 2: 1.0980 (D1 BSL, 12.4R).

**p_bracket (martingale) cho Target 2:** 12 / (12 + 149) = 0.075. Nghĩa là: để setup này "tốt hơn ngẫu nhiên", tỷ lệ đạt Target 2 trước stop phải **vượt 7.5%** một cách có hệ thống qua nhiều mẫu.

**T5 (outcome giả định).** Giá đạt 1.0980 sau 4 phiên → D1 range COMPLETED (DOL đạt). Frame mới cho pha tiếp theo cần được dựng; 1.1040 trở thành DOL kế tiếp *nếu* một leg DR mới hình thành.

**Bài học:** location (D1 OTE + H1 discount) chỉ xác định *nơi tìm*; entry chỉ xảy ra sau chuỗi H1 MSS → M5 trigger. Nếu T3 không xảy ra (không có H1 MSS), không có setup — dù giá đã ở "discount đẹp".

#### Case Study B — Downtrend (hypothetical NQ)

![[Dealing-Range-v01-21-Case-B-Downtrend.svg|1516]]
*Sơ đồ: Case B (hypothetical) — bearish OTE; old low 17,980 (spent) chặn đường đến DOL.*

**Context (D1).** BEAR ở scale D1 (ATR_D1 ≈ 280 điểm). Protected high 18,400 (origin của leg phá swing low 17,980 — MSS bearish trước đó). Termination 17,650, đã đóng. W = 750 (2.7 ATR), EQ = 18,025, bearish OTE (p 0.62–0.79) = 18,115–18,242.

**Liquidity.** BSL trên 18,400 (protected high). SSL: dưới 17,650; equal lows D1 17,420/17,435 (cluster, θ\* lớn) — DOL mở rộng. Old low 17,980 (spent) nằm tại p = 0.44.

**DOL.** Primary: SSL dưới 17,650; extended: 17,420 cluster. M_ratio từ 18,150 ≈ 0.67.

**LRI.** D1 leg: p(18,150) = 0.67 (P); IPDA-20 giả định 17,650–18,560: p = 0.55 (P); container ≈ D1 leg (P). LRI = 1.0. **D1 GATE = PASS.**

```text
T0: Giá hồi lên 18,050 (p = 0.53). Chưa ở OTE.
T1: H1 bullish internal structure; H1 equal highs 18,188 / 18,190 → BSL H1.
T2: Giá quét 18,215 (trong OTE D1, dưới protected 18,400). Chưa biết đây là đỉnh.
T3: H1 displacement giảm, close phá H1 HL 18,090 → H1 MSS bearish. 18,215 = PROTECTED (H1).
T4: Low 18,040 đóng → H1 leg DR 18,215–18,040 ACTIVE; EQ 18,127.5; premium > 18,127.5.
    Bearish FVG H1 18,140–18,165 → p_H1 = 0.57–0.71; p_D1 = 0.65–0.68. Nested-consistent.
M5 (NY AM): sweep M5 high, M5 MSS xuống, displacement, M5 FVG.
    Entry 18,150; stop 18,182 (32 điểm); Target 1: 18,040 (3.4R); Target 2: 17,650 (15.6R).
T5 (giả định): giá đạt 18,040 nhưng không đạt 17,650 trong 3 phiên; bật lên từ 17,980 (old low).
```

**Bài học riêng của case B:**

1. **Old low 17,980 (spent) trở thành reference** — nó chặn đường đến DOL. mục 14.6.2: "path of least resistance" phải xét cả các level spent nằm giữa giá và DOL.
2. **Bất đối xứng volatility** (mục 3.5.3): trong index, leg giảm nhanh; θ tính theo ATR giãn → stop M5 cần buffer tương ứng.
3. **Tin tức NY AM** (10:00 ET data): nếu M5 trigger rơi vào bar tin, anchor M5 có thể là spike (EC-10).

#### Case Study C — Consolidation (hypothetical XAUUSD)

![[Dealing-Range-v01-22-Case-C-Consolidation.svg|1516]]
*Sơ đồ: Case C (hypothetical) — leg DR vs container DR, double sweep, LRI 0.33.*

**Context.** Sau expansion tăng 2,180 → 2,390 (D1 leg DR, protected 2,180), giá đi ngang 25 phiên trong 2,300–2,390. Wick 2,392 (vượt đỉnh 2 USD, close lại bên trong) và wick 2,297 (dưới đáy 3 USD, close lại) — **cả hai phía đều bị sweep**. θ\* của swing mới giảm dần (3.1 → 2.2 → 1.4 ATR).

**Hai frame xung đột tại giá 2,320:**

| Frame | Anchors | p(2,320) | Nhãn |
|---|---|---|---|
| D1 leg DR | 2,180 → 2,390 | 0.67 | Premium |
| Container DR | 2,297 → 2,392 | 0.24 | Discount |
| IPDA-20 | ≈ container | 0.24 | Discount |

LRI (trọng số bằng nhau) = |−1 + 1 + 1| / 3 = 0.33 → **AMBIGUOUS**.

**Vì sao range selection khó hơn trong consolidation:**

1. **Leg DR mất thẩm quyền:** leg 2,180 → 2,390 không còn "chi phối" — 25 phiên không có impulse mới. Nhưng protected low 2,180 vẫn còn sống → leg DR vẫn *valid*, chỉ không *relevant* cho location.
2. **Container có boundaries đã bị sweep:** mỗi phía đã bị lấy liquidity một lần. Boundary "thật" là wick hay đỉnh/đáy trước wick? (mục 5.3, Scenario E.)
3. **Ý nghĩa P/D đổi bản chất:** trong container, "discount" gợi ý mean-reversion (mua đáy hộp) — hypothesis khác với continuation. Thống kê của continuation không áp dụng.
4. **Swing compression** (EC-24): swing nhỏ dần → H1 ranges bên trong gần như noise so với D1.

```text
T0: Phiên thứ 10 của consolidation. State leg DR = ACTIVE nhưng 2 lần thất bại phá 2,390.
T1: Sweep 2,392 + close lại → SWEPT_H. Chưa đủ để gọi consolidation (1 phía).
T2: Sweep 2,297 + close lại → SWEPT_L (container). Double sweep → state CONSOLIDATING.
    D1 GATE (continuation) = AMBIGUOUS. Quyết định v0.1: không trade continuation; log.
T3: Swing co dần; equal-ish highs 2,385/2,388 hình thành → BSL tích tụ.
T4: Close 2,401 bằng displacement (body 1.4 ATR) + close tiếp theo 2,408 → acceptance (k=2).
    Scenario H: leg DR mới. Origin = swing low cuối cùng trong container trước breakout (2,331).
    Container 2,297–2,392 → reference zone.
T5 (giả định): giá hồi về 2,395 (top container cũ, flip) rồi tiếp tục → acceptance xác nhận.
    (Kịch bản thay thế: giá quay lại dưới 2,392 → acceptance failure, EC-14.)
```

**Bài học:** trong consolidation, câu trả lời đúng thường là **"không có location edge cho continuation"**. Framework phải có khả năng nói "không biết".

#### Case Study D — Trend Reversal (hypothetical GBPUSD)

![[Dealing-Range-v01-23-Case-D-Reversal.svg|1516]]
*Sơ đồ: Case D (hypothetical) — sweep → MSS → location blackout giữa T3 và T4.*

**Context.** Trend DR (scale lớn, ~W1): 1.2600 → 1.2900. Leg DR (scale D1): 1.2740 → 1.2900 (1.2740 là HL đạt θ_min(D1), origin của BOS phá 1.2850).

```text
T0: Giá tại 1.2880; hai DR ACTIVE. DOL: BSL trên 1.2900 (termination của cả hai).
T1: Giá quét lên 1.2935 rồi close 1.2885 → SWEPT_H (cả hai range) và DOL COMPLETED.
    Thông tin: BSL đã lấy. Chưa có gì về hướng tiếp theo.
T2: Displacement giảm phá internal low 1.2820 (internal event đối với leg DR) — cờ
    adverse_displacement. Leg DR vẫn ACTIVE.
T3: Hai close dưới 1.2740 (protected của leg DR), body close thứ hai 1.3 ATR, không reclaim
    trong 3 phiên → leg DR INVALIDATED → MSS bearish ở scale D1.
    Trend DR (protected 1.2600) VẪN ACTIVE → xung đột scale: D1 BEAR, W1 BULL.
    Bearish leg DR mới: origin = 1.2935 (sweep high), termination đang chạy → FORMING.
    ⇒ "Location blackout": không có frame ACTIVE ở scale D1 cho đến khi termination đóng.
T4: Low 1.2700 đóng (giá hồi ≥ θ) → bearish leg DR 1.2935–1.2700 ACTIVE; EQ 1.2817.
    DOL bearish: SSL dưới 1.2600 — chính là protected low của trend DR (parent).
T5 (giả định): giá hồi lên 1.2840 (p = 0.60, premium), H1 MSS xuống, tiếp tục đến 1.2610.
```

**Bài học:**

1. **Reversal có độ trễ cấu trúc không thể tránh:** giữa T3 (invalidation) và T4 (range mới ACTIVE) không có location frame. Trader cảm thấy "rõ ràng là giảm" ở T3 thường entry trong blackout — tức entry không có location.
2. **DOL của reversal là protected anchor của parent** — một pattern đáng test: HYP-DR-009 "sau MSS ở scale k ngược với scale k+1, xác suất đạt protected anchor của k+1 trước khi scale k reclaim".
3. **Sweep (T1) + adverse displacement (T2) là cảnh báo sớm, không phải invalidation.** Đánh đồng chúng dẫn tới đảo chiều quá sớm.

#### Case Study E — False Breakout / Sweep vs Invalidation (hypothetical EURUSD H1)

![[Dealing-Range-v01-24-Case-E-Sweep-vs-Invalidation.svg|1516]]
*Sơ đồ: Case E (hypothetical) — cùng một cú phá H1 low: SWEPT_L vs INVALIDATED.*

**Context.** D1 leg DR ACTIVE 1.0750–1.0980 (BULL). H1 bullish leg DR 1.0840 → 1.0905 (protected H1 low 1.0840). Rule: HARD invalidation = 2 close dưới L\* hoặc 1 close dưới với body ≥ 1.2 ATR_H1, và không reclaim trong 3 bar.

**Nhánh E1 — Sweep:**

```text
T0: Giá hồi về 1.0850 (p_H1 = 0.15).
T1: Bar H1 close 1.0836 (dưới 1.0840, body 0.6 ATR) → MEDIUM → PENDING.
T2: Bar tiếp theo close 1.0852 (reclaim trong 1 bar) → PENDING hủy → SWEPT_L.
    SSL dưới 1.0840 đã lấy; range H1 giữ nguyên; D1 không bị ảnh hưởng.
T3: M5 MSS tăng từ 1.0831 (low của sweep) → setup (M5 GATE kiểm tra).
```

**Nhánh E2 — Invalidation:**

```text
T1': Bar H1 close 1.0832 (body 1.4 ATR) → đạt điều kiện strong close → PENDING.
T2': Bar tiếp theo close 1.0826; T3': 1.0829; T4': 1.0821 → không reclaim trong 3 bar
     → H1 leg DR INVALIDATED.
     D1 leg DR vẫn ACTIVE (1.0840 là internal đối với D1; D1 protected = 1.0750).
     Diễn giải: nhịp hồi D1 sâu hơn dự kiến — không phải D1 reversal.
     Hành động: chờ H1 structure mới (H1 bullish MSS mới) trong D1 discount sâu hơn.
```

**Bài học:** cùng một sự kiện bề mặt ("giá phá H1 low") dẫn đến hai trạng thái khác nhau, và **cả hai đều không invalidate D1**. Phân biệt sweep/invalidation *phải được quyết định bằng rule đã viết trước*; nếu không, trader sẽ gọi nó là "sweep" khi trade thắng và "invalidation" khi trade thua.

### 17.2. Case lưu trữ (narrative)

> [!warning] Đọc đúng tính chất của các case dưới đây
> Kiểm tra ngày 2026-10-06: không tìm thấy log giao dịch tương ứng với Case 0–4 trong `04 - Backtesting/` hay `05 - Live Trading Journal/` (các con số chỉ xuất hiện trong note concept). Vì vậy chúng được xếp là **case minh họa dạng narrative** — giá trị nằm ở *bài học định tính* (lịch tin, options expiry, funding, nested conflict), không ở các con số R. Case 5–6 là tái dựng minh họa theo chú thích trong sơ đồ. Nếu một case là giao dịch thật của bạn, thêm link tới trade log để nâng nó thành bằng chứng có nguồn.

#### Case 0 (Bổ sung — Setup đẹp nhưng THUA vì xung đột nested range) — XAUUSD, thứ Năm, Long D1 discount nhưng Weekly đang Premium

![[Dealing-Range-Case-Study.svg|1516]]
*Entry ở discount 30% của range D1 nhưng cùng mức giá đó lại nằm sát Premium của range Weekly — xung đột nested range giữa hai tầng khung thời gian, minh họa cho EC2 ở mục 16.*

**Bối cảnh HTF:** XAUUSD. Weekly range: low 2,338 → high 2,412, Weekly EQ = 2,375 — giá đang giao dịch quanh 2,391, tức khoảng 50-55% Weekly range (sát Premium tuần). D1 range (hiệu lực riêng trong tuần): low 2,388 → high 2,406, D1 EQ = 2,397.

**Setup:** giá tại 2,391 rơi vào 30% của range D1 (discount), trùng một D1 bullish FVG — trông như một entry chuẩn theo checklist D1 đơn thuần. Vấn đề chỉ lộ ra khi đối chiếu ma trận nested range ở §4.1: cùng một giá đang ở discount D1 NHƯNG sát premium Weekly — hai tầng đang đưa ra kết luận trái ngược nhau.

**Diễn biến & execution:** Entry Long 2,391 (giữa D1 FVG), Stop kỹ thuật 2,378 (dưới FVG, buffer theo ATR D1). Kế hoạch R:R 1:3 hướng tới Weekly EQ 2,375→2,406. Thực tế: giá không phản ứng tại D1 FVG như kỳ vọng — áp lực bán từ Weekly premium thắng thế, giá xuyên thẳng qua D1 FVG và tiếp tục giảm về hướng Weekly EQ, quét Stop tại 2,378.

**Kết quả bằng số:** Risk 13 USD/oz (2,391→2,378) = 1,300 USD/lot chuẩn (100oz). **Kết quả: -1.3R.** R:R 1:3 dự kiến không bao giờ có cơ hội chạy vì hướng lệnh sai từ gốc.

**Bài học chỉ rút ra được nhờ case này:** khi hai tầng range (D1 và Weekly) mâu thuẫn về kết luận premium/discount, KHÔNG trade theo tầng nhỏ hơn một mình — tầng lớn hơn (Weekly) thường thắng thế về áp lực cung-cầu thực tế. Nếu kiểm tra Weekly range TRƯỚC khi vào lệnh (bước Context ở mục 4), setup này lẽ ra đã bị loại ngay từ đầu thay vì chờ đến khi Stop bị quét.

#### Case 1 (Thắng đúng sách) — EURUSD, thứ Ba, Long từ Discount D1 đồng thuận H1

**Bối cảnh HTF:** EURUSD, D1 Bullish bias sau khi giá quét SSL tại 1.0745 (đáy 3 tuần) và reclaim mạnh bằng displacement, để lại D1 bullish FVG tại 1.0762–1.0778. D1 dealing range: low 1.0745 → high 1.0834 (đỉnh cũ đã có BSL còn mở). Draw on liquidity chính: BSL D1 tại 1.0834.

**Setup:** Equilibrium D1 = 1.0790. Giá retrace về 1.0768 (khoảng 26% range D1, deep discount), trùng khít D1 FVG. Trên H1, range con trong 2 ngày gần nhất cũng cho vị trí discount (38% range H1) — cộng hưởng 2 tầng theo ma trận §4.1.

**Diễn biến & execution:** 08:12 giờ Frankfurt, giá vào vùng FVG D1, quét thêm một SSL nội bộ H1 tại 1.0761 (equal lows 2 lần chạm), reclaim ngay trong nến H1 tiếp theo. 08:47, M5 tạo bullish MSS (phá đỉnh M5 gần nhất tại 1.0770) kèm displacement để lại M5 FVG 1.0771–1.0776. Entry Long 1.0774 (giữa FVG M5), stop 1.0757 (dưới SSL vừa quét, buffer 4 pip = 1.0753 thực tế). Target 1: internal H1 OB đối diện tại 1.0806 (partial 50%). Target 2: external BSL D1 tại 1.0834.

**Kết quả bằng số:** Stop distance 21 pip. TP1 chạm lúc 14:20 cùng ngày (+32 pip, chốt 50% = +1.5R trên phần đó). TP2 chạm 10:05 sáng hôm sau (+60 pip trên phần còn lại). R-multiple tổng hợp: **+2.6R** trên toàn lệnh.

**Bài học chỉ rút ra được nhờ case này:** cộng hưởng 2 tầng (D1 discount + H1 discount) không chỉ là lý thuyết suông — trong case này nó trùng với cả một equal-low H1 (pool dày hơn single low), tạo ra 3 lớp confluence cộng dồn (range D1 + range H1 + độ dày liquidity pool) mà nếu chỉ nhìn D1 đơn thuần sẽ không phân biệt được với các setup discount D1 khác yếu hơn.

#### Case 2 (Setup đẹp như sách nhưng THUA — giá trị nhất) — NQ, thứ Năm, CPI 08:30 EST

**Bối cảnh HTF:** NQ, D1 Bullish bias, giá quanh 18,920. Dealing range D1: low 18,610 (đã quét SSL tuần trước, reclaim mạnh) → high 19,180 (BSL còn mở, đỉnh lịch sử gần nhất). EQ D1 = 18,895.

**Setup:** Trước CPI, giá đã retrace xuống 18,780 (khoảng 40% range D1 — discount nông), chạm một D1 bullish FVG 18,760–18,795. Toàn bộ checklist mục 8 đều xanh: swing có displacement, đã lấy liquidity 2 đầu, đúng timeframe, có internal POI ở discount, external BSL còn mở phía trên.

**Diễn biến & execution:** 08:30:00 EST, CPI công bố cao hơn dự báo (3.4% so với kỳ vọng 3.1%). 08:30:04, NQ lao dốc bằng một nến M1 thân dài từ 18,780 xuống 18,590 — **xuyên thẳng qua đáy dealing range D1 (18,610) và giữ acceptance ngoài** (đóng nến M1 tại 18,595, không reclaim). Trader đã đặt limit Long tại 18,775 (giữa FVG) bị khớp lúc 08:30:02 ngay trước cú lao dốc, cách đáy cũ chỉ 165 điểm — không kịp phản ứng vì tốc độ di chuyển dưới 5 giây. Stop kỹ thuật đặt tại 18,745 (dưới FVG, buffer 15 điểm) bị quét lúc 08:30:05, cách xa mức lý tưởng do trượt giá (slippage) trong nến tin — khớp thực tế tại 18,720.

**Kết quả bằng số:** Rủi ro dự kiến 30 điểm (18,775 → 18,745) = 600 USD/lot theo kế hoạch. Rủi ro thực tế do slippage: 55 điểm (18,775 → 18,720) = **1,100 USD/lot, tương đương -1.8R so với kế hoạch ban đầu** (dùng R = 30 điểm làm chuẩn).

**Bài học chỉ rút ra được nhờ case này:** setup đúng 100% theo checklist tĩnh (mục 8) vẫn thua vì checklist không có điều kiện nào về **lịch tin tức**. Đây chính là edge case EC7 ở mục 16 áp dụng ngược — nến tin không chỉ tạo swing giả, nó còn có thể **phá hủy một range đang hợp lệ trong tích tắc**, biến discount D1 "đúng sách" thành cái bẫy vì displacement tin tức không tôn trọng cấu trúc cũ. Quy tắc rút ra: không giữ limit order đang chờ khớp trong cửa sổ ±10 phút quanh CPI/NFP/FOMC cấp cao, bất kể setup nhìn "đẹp" tới đâu.

#### Case 3 (Đứng ngoài đúng — skip nhờ nhận ra red flag) — GBPUSD, thứ Tư, tuần đáo hạn quyền chọn FX cuối tháng

**Bối cảnh HTF:** GBPUSD, D1 Neutral-to-Bullish, giá quanh 1.2680. Dealing range D1 hiển thị: low 1.2605 → high 1.2755. Nhìn thoáng qua, giá ở 1.2680 tương đương 40% range — discount nông, "đủ điều kiện" tìm Long theo checklist cơ bản.

**Setup ban đầu (trước khi soát red flag):** một H1 bullish FVG tại 1.2670–1.2685 trùng đúng vùng giá hiện tại, trông như một entry hợp lý cho Long.

**Red flag phát hiện trước khi vào lệnh:** kiểm tra lịch kinh tế, phát hiện đây là ngày cuối tháng trùng kỳ đáo hạn quyền chọn FX lớn (options expiry) — thanh khoản buổi chiều London thường bị bóp méo bởi các dealer hedging quanh các mức "pin" tròn số (1.2700, 1.2650). Kiểm tra thêm cấu trúc: dealing range D1 rộng tới 150 pip trong khi ADR(20) của GBPUSD giai đoạn đó là khoảng 95 pip — tức range NÀY thực chất RỘNG hơn bình thường (khác EC8, nhưng cùng gốc "kiểm tra ADR trước khi tin số liệu"), gợi ý các swing 2 đầu hình thành từ các cú biến động bất thường trước đó, không phải nhịp bình thường của cặp tiền.

**Quyết định:** đứng ngoài, không vào Long dù checklist cơ bản "xanh". Log lại lý do: "range rộng bất thường + ngày options expiry = nhiễu cao, entry tại discount nông không đủ biên an toàn."

**Kết quả (theo dõi không giao dịch):** giá dao động giằng co quanh 1.2670–1.2705 suốt buổi chiều London-NY, quét cả FVG đã định vào lệnh lẫn phá nhẹ lên 1.2705 rồi đóng cửa ngày gần như đi ngang tại 1.2688. Nếu vào lệnh với stop kỹ thuật thông thường (dưới FVG khoảng 12 pip), khả năng cao đã bị quét bởi các đợt giằng co trước khi có bất kỳ đợt di chuyển thật nào — biên độ chop trong phiên vượt quá khoảng cách stop dự kiến ít nhất 2 lần.

**Bài học chỉ rút ra được nhờ case này:** checklist tĩnh không bắt được rủi ro theo lịch (options expiry, rollover). Kỹ năng thực chiến ở đây không phải là đọc range đúng hay sai — range vẽ đúng kỹ thuật — mà là biết **khi nào một range đúng kỹ thuật vẫn không đáng giao dịch** vì bối cảnh thanh khoản đặc biệt của ngày hôm đó.

#### Case 4 (Tài sản khác — Crypto) — BTCUSD, Chủ Nhật, funding time 16:00 UTC

**Bối cảnh HTF:** BTCUSD trên Binance USDT-M futures, D1 range: low 60,150 → high 63,800 (hình thành từ 4 ngày giao dịch trước, đã quét SSL và BSL rõ theo cả 2 đầu). EQ D1 = 61,975. Giá tại thời điểm phân tích: 61,200 (khoảng 32% range — discount).

**Setup:** một bullish 4H FVG tại 60,900–61,150 nằm gọn trong vùng deep discount. Bias Bullish do BTC vừa giữ vững trên vùng hỗ trợ tuần trước.

**Diễn biến & execution:** 15:52 UTC (8 phút trước funding 16:00), giá bắt đầu nhúng nhanh vào vùng FVG, chạm 60,920. Đây là hành vi điển hình "funding rate hunt" — các vị thế short đòn bẩy cao trên thị trường perpetual thường bị đẩy về phía thanh lý ngay trước mốc funding để dealer thu lợi từ chênh lệch funding rate, tạo ra các wick giả không phản ánh cấu trúc cung-cầu giao ngay thật. 16:01 UTC, ngay sau funding, giá bật lại rất nhanh lên 61,450 chỉ trong 6 phút — nến 4H đóng cửa với wick dài dưới, thân nhỏ, đúng dấu hiệu "sweep rồi reject" (không phải breakout thật). MSS bullish xác nhận trên M15 lúc 16:14 UTC. Entry Long 61,320 (retest vùng FVG sau reclaim), stop 60,850 (dưới wick funding, buffer khoảng 70 USD tương ứng biến động bình thường của BTC ở khung này). Target: internal OB đối diện tại 62,600 (partial), external BSL D1 tại 63,800 (full).

**Kết quả bằng số:** Stop distance 470 USD (~0.77% giá trị BTC tại entry). TP1 chạm sau 14 giờ (+1,280 USD, chốt 50% = ~1.36R phần đó). TP2 chạm sau 2 ngày (+2,480 USD trên phần còn lại). R-multiple tổng hợp: **+2.9R**.

**Bài học chỉ rút ra được nhờ case này:** trên crypto, các wick xuyên sâu vào IRL/vùng discount quanh giờ funding (00:00, 08:00, 16:00 UTC) cần được đọc khác với wick thường — nó thường là hệ quả cơ chế funding/thanh lý đòn bẩy hơn là phản ứng cung-cầu giao ngay thật, nhưng điều đó KHÔNG có nghĩa là bỏ qua nó: FVG vẫn được "sạc" thanh khoản thật tại đó, chỉ cần chờ xác nhận reclaim + MSS trước khi tin đây là điểm entry hợp lệ thay vì vào ngay lúc wick đang diễn ra.

#### Case 5 (Minh họa — giao thức anchor wick vs body) — NQ, phiên NY AM

![[Dealing-Range-CaseStudy-B1-NQ-Anchor-Skip.svg|1516]]
*Tái dựng minh họa (theo chú thích trong sơ đồ) — không phải giao dịch thật.*

**Bối cảnh:** swing low 20,180; wick-high (Anchor A, sweep) 20,412; body-high (Anchor B, displacement close) 20,381. OTE theo Anchor A: 20,308–20,253; theo Anchor B: 20,255–20,197 — chênh ~53 điểm ở mức 62%.

**Diễn biến (theo sơ đồ):** giá hồi thấp nhất 20,296 rồi chạy thẳng lên 20,470 — limit theo Anchor B (20,255) không bao giờ khớp.

**Bài học:** một case không nói giao thức nào tốt hơn — ở case khác, anchor wick sẽ là bên bị "phantom wick" đánh lừa. Bài học đúng là **chọn TRƯỚC một giao thức anchor và giữ nó**, rồi để backtest so sánh hai giao thức (3.4.4, CX-06). Đổi anchor sau khi thấy giá là hindsight.

#### Case 6 (Minh họa — thắng nhờ re-anchor sau acceptance) — EURUSD, London → NY

![[Dealing-Range-CaseStudy-B2-EURUSD-Reanchor-Win.svg|1516]]
*Tái dựng minh họa (theo chú thích trong sơ đồ) — không phải giao dịch thật.*

**Bối cảnh:** range cũ (Asia) 1.0810–1.0850. Nến H1 **đóng và giữ bên ngoài** range = acceptance, không phải sweep.

**Re-map:** range mới từ origin của displacement 1.0838 → extreme 1.0912, EQ mới 1.0875. Discount POI: bullish FVG 1.0845–1.0851. Entry 1.0848, SL 1.0828 (20 pip), TP 1.0908 (BSL của range mới) → **+3.0R**.

**Bài học:** nếu giữ range Asia cũ, cùng mức giá đó đã là "premium" → bỏ lỡ hoặc short nhầm hướng. Điểm mấu chốt không phải OTE đẹp mà là **phân xử acceptance vs sweep bằng rule viết trước** — đây chính là Scenario C / EXTENDED trong 5.3–5.1.

---

## 18. Khung định lượng & thuật toán

Mục này gom mọi thứ cần để **code hóa** Dealing Range: biến số (18.1), cách biến khái niệm chủ quan thành đại lượng đo được (18.2), pseudocode (18.3) và trường journal (18.4). Phiên bản Python tối giản của chính các quy tắc này đã được chạy trong nghiên cứu §19.3 (Directional Change swings, leg DR lifecycle, first-passage outcome).

### 18.1. Quantitative Framework

#### 18.1.1 Swing variables

| Biến | Công thức / định nghĩa | known_at |
|---|---|---|
| `amp_in_atr` | \|price − giá của swing đối diện trước\| / ATR_formation | Khi swing xác nhận |
| `amp_out_atr` | Biên độ leg rời swing (đến t) / ATR_formation | Cập nhật theo t |
| `duration_bars` | Số bar của leg vào / leg ra | Theo t |
| `retr_ratio` | Biên độ leg ra / biên độ leg vào (với HL: độ sâu hồi so với impulse trước) | Khi leg đóng |
| `theta_star` | Threshold DC lớn nhất mà swing còn là pivot (mục 3.2.3) | Theo t |
| `disp_max_body_atr` | max(body/ATR) trong k bar đầu leg ra | Sau k bar |
| `fvg_count_out`, `fvg_atr_out` | FVG tạo trong leg ra | Theo t |
| `bos_origin` | Leg ra đã phá swing đối diện cùng cấp? | Tại BOS |
| `break_magnitude_atr` | (close phá − level) / ATR | Tại BOS |
| `sweep_depth_atr` | Khoảng vượt swing trước cùng phía / ATR (nếu swing là sweep) | Khi swing xác nhận |

#### 18.1.2 Range variables

| Biến | Công thức |
|---|---|
| `W` | H\* − L\* |
| `W_atr` | W / ATR tại known_at của range |
| `range_duration` | t_termination − t_origin (bar) |
| `leg_slope` | W / (range_duration × ATR) — tốc độ chuẩn hóa của leg |
| `leg_efficiency` | W / Σ\|ΔClose\| trong leg (efficiency ratio; 1 = đi thẳng) |
| `n_internal_swings` | Số swing θ\* ≥ θ₁ bên trong range |
| `n_internal_bos` | Số internal BOS trong leg |
| `realized_vol_in_range` | Độ lệch chuẩn log-return trong range |
| `boundary_tests_up/dn` | Số lần giá chạm trong ε·ATR của H\*/L\* mà không vượt |
| `violations_up/dn` | Số lần vượt (wick) không acceptance |
| `age_bars` | t − known_at |

#### 18.1.3 Location variables

| Biến | Công thức |
|---|---|
| `p` | (P − L\*) / W |
| `dist_eq_W` | (P − EQ) / W = p − 0.5 |
| `dist_eq_atr` | (P − EQ) / ATR |
| `dist_to_H_atr`, `dist_to_L_atr` | Khoảng cách đến boundary / ATR |
| `in_ote` | 0.21 ≤ p ≤ 0.38 (bull) / 0.62 ≤ p ≤ 0.79 (bear) |
| `p_parent` | p trên parent range |
| `LRI` | mục 4.4.2 |

#### 18.1.4 Liquidity variables

| Biến | Công thức |
|---|---|
| `dist_ext_up_atr` | Khoảng cách đến swing high còn sống cấp ≥ k gần nhất phía trên |
| `dist_ext_dn_atr` | Tương tự phía dưới |
| `liq_density_up(b)` | Số swing highs còn sống trong [P, P + b·ATR] |
| `eq_cluster_top` | Số swing highs trong ε·ATR quanh H\* |
| `origin_swept_liq` | Origin là sweep của swing trước? (binary) |
| `unswept_liq_below_origin` | Có swing low còn sống trong b·ATR dưới L\*? |
| `htf_confluence_top` | H\* trùng PDH/PWH/số tròn trong ε |

#### 18.1.5 DOL variables

| Biến | Công thức |
|---|---|
| `dol_dist_atr` | Khoảng cách đến DOL được chọn / ATR |
| `dol_dir` | +1 / −1 |
| `dol_loc` | INSIDE / BOUNDARY / OUTSIDE |
| `M_ratio` | dol_dist / W |
| `opp_liq_dist_atr` | Khoảng cách đến liquidity đối diện (phía sau stop) |
| `dol_scale` | θ\* của swing mục tiêu |

#### 18.1.6 Outcome variables

| Biến | Định nghĩa |
|---|---|
| `y_hit` | 1 nếu target trước stop (first passage) |
| `R` | R-multiple thực hiện (sau chi phí) |
| `MFE_R`, `MAE_R` | Max favorable / adverse excursion tính theo R |
| `t_target`, `t_stop` | Số bar đến target / stop |
| `p_bracket` | r / (r + g), với r = risk, g = reward (xác suất thắng dưới martingale) |
| **`MEHR`** | **y_hit − p_bracket** (Martingale Excess Hit Rate) |

**MEHR là biến outcome trung tâm được đề xuất.** [MATHEMATICAL] Với bất kỳ bracket nào, dưới martingale E[MEHR] = 0, và

$$E[R] = \left(\bar{y}_{hit} - p_{bracket}\right) \cdot \frac{r + g}{r}$$

Tức là expectancy chính là MEHR được scale bởi hình học bracket. MEHR cho phép so sánh các setup có R:R khác nhau trên cùng một thang: *setup này có làm tốt hơn ngẫu nhiên không, sau khi đã tính đến hình học của nó?* Một hệ thống "win rate 60%" với target 0.5R có MEHR = 0.60 − 0.667 = **−0.067** — tệ hơn ngẫu nhiên. Một hệ thống "win rate 30%" với target 3R có MEHR = 0.30 − 0.25 = **+0.05** — tốt hơn ngẫu nhiên.

![[Dealing-Range-v01-18-MEHR.svg|1516]]
*Sơ đồ: MEHR — so win rate với martingale của chính bracket đó.*

#### 18.1.7 Range Quality Framework — descriptive vs predictive

**Descriptive feature:** mô tả range (W, duration, số swing). Luôn tính được, luôn "có nghĩa".
**Predictive feature:** một feature mà khi điều kiện hóa trên nó, phân phối outcome *thay đổi* so với baseline.

| Feature | Hypothesis hướng tác động (chưa kiểm chứng) | Cách test predictive value |
|---|---|---|
| `W_atr` | Range quá nhỏ/quá lớn → location ít thông tin | MEHR theo bin W_atr; kiểm tra quan hệ hình chữ U ngược |
| `range_duration` | ? (không có kỳ vọng mạnh) | MEHR theo bin |
| `n_internal_swings` | Leg ít swing nội bộ (sạch) → origin mạnh hơn | P(origin bị phá trong k bar) theo bin |
| `n_internal_bos` | ? | Như trên |
| `disp_max_body_atr` (từ origin) | Cao → origin bền hơn | HYP-DR-006 |
| `origin_swept_liq` | TRUE → origin bền hơn | HYP-DR-007 |
| `unswept_liq_below_origin` | TRUE → rủi ro sweep stop cao hơn | Tỷ lệ bị stop rồi giá đi đúng hướng |
| `dol_dist_atr`, `M_ratio` | M quá lớn → location vô nghĩa | MEHR theo M |
| `realized_vol regime` | Regime cao → threshold cần giãn | Tách regime |
| `violations_dn` | Nhiều lần sweep L\* → protected yếu | P(invalid) theo số violations |
| `boundary_tests_up` | Nhiều test H\* → BSL tích tụ → DOL mạnh | P(H\* bị lấy trong N bar) |
| `mitigations` (POI trong range) | Nhiều lần chạm → POI yếu dần | Reaction rate theo lần chạm |
| `age_bars` (recency) | Range cũ → ít thông tin | MEHR theo tuổi |

**Phương pháp test predictive value của một feature:**

1. Chia bin (quintile) feature, tính MEHR trung bình và CI mỗi bin.
2. Kiểm tra **monotonicity** hoặc hình dạng đã dự đoán trước (không "tìm hình dạng" sau khi xem).
3. **Permutation test:** xáo trộn feature giữa các sample (giữ outcome), tính lại độ chênh; p-value = tỷ lệ hoán vị cho chênh ≥ quan sát.
4. **Out-of-sample:** hình dạng phải lặp lại trên giai đoạn/instrument khác.
5. Điều chỉnh multiple testing khi test nhiều feature (mục 19.2).

> [!warning] MEHR sau v0.2
> MEHR (định nghĩa ở 18.1.6) đúng trong thế giới theo dõi liên tục, fill tại mức. Khi lệnh thoát *vượt* mức (gap, close-only, slippage), MEHR có gradient theo vị trí ngay cả trên random walk: q − u = δ(1 − 2u)/(W + 2δ). Từ v0.2: dùng **P/W hoặc R thực hiện** làm thước đo chính; nếu dùng MEHR thì luôn báo cáo MEHR − MEHR_null với null chạy cùng cách theo dõi ([[#19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)|§19.3.3]]).

### 18.2. Objective vs Subjective Variables

#### 18.2.1 Phân loại tổng quát

| Loại | Định nghĩa | Ví dụ trong DR |
|---|---|---|
| **Objective** | Xác định hoàn toàn bằng thuật toán, không tham số tùy ý | p, W, EQ, IPDA 20-day high/low, fractal pivot |
| **Semi-objective** | Xác định bằng thuật toán + threshold phải chọn | θ\*, "displacement" (body/ATR ≥ d), acceptance (k closes) |
| **Subjective** | Phụ thuộc diễn giải | "range có ý nghĩa", "liquidity lớn", "DOL rõ ràng" |

Mục tiêu của research: **đẩy mọi thứ từ subjective → semi-objective**, và giữ số threshold ở mức tối thiểu.

#### 18.2.2 Formalize tám khái niệm then chốt

**(1) Important swing**
- *Discretionary:* "Swing rõ ràng, quan trọng."
- *Problem:* không tái lập được; hindsight.
- *Candidate objective:* θ\* ≥ θ_min(TF) AND bos_origin = TRUE AND alive = TRUE.
- *Advantages:* 1 threshold, 2 binary; tái lập.
- *Limitations:* bỏ qua swing quan trọng vì lý do khác (ví dụ HTF level); θ_min tùy ý.
- *Backtest:* so sánh tỷ lệ swing bị phá trong k bar giữa nhóm "important" vs "không" ở cùng khoảng cách tới giá.

**(2) Meaningful range**
- *Discretionary:* "Range mà thị trường đang tôn trọng."
- *Problem:* "tôn trọng" được xác định sau khi thấy phản ứng.
- *Candidate objective:* Leg DR có origin là important swing, termination đã đóng, W_atr ∈ [w_min, w_max], state ∈ {ACTIVE, SWEPT}.
- *Advantages:* định nghĩa trước kết quả.
- *Limitations:* consolidation không có meaningful leg DR theo định nghĩa này (cần container).
- *Backtest:* MEHR của entries dùng meaningful range vs naive range.

**(3) External structure**
- *Discretionary:* "Các đỉnh/đáy lớn."
- *Problem:* nhầm scale với role.
- *Candidate objective:* các swing đang là boundary (L\*, H\*) của range đang dùng + swing còn sống có θ\* ≥ θ\*(anchors) bên ngoài range.
- *Advantages:* quan hệ rõ ràng với range.
- *Limitations:* phụ thuộc range selection.
- *Backtest:* không test trực tiếp — là định nghĩa phục vụ các test khác.

**(4) Strong displacement**
- *Discretionary:* "Nến mạnh, nhanh."
- *Problem:* "mạnh" tương đối với volatility.
- *Candidate objective:* ≥ 1 candle có body/ATR(14) ≥ d (HEURISTIC d ≈ 1.2–1.5) và close trong 25% cực của range candle, **hoặc** tổng body 3 candle liên tiếp cùng chiều ≥ d₃·ATR; tạo ít nhất 1 FVG.
- *Advantages:* chuẩn hóa theo volatility.
- *Limitations:* bỏ qua displacement dạng nhiều nến vừa; nhạy với d.
- *Backtest:* sweep d trên lưới, tìm **plateau** (vùng ổn định), không tìm đỉnh.

**(5) Major liquidity**
- *Discretionary:* "Liquidity lớn, hiển nhiên."
- *Problem:* latent, không quan sát.
- *Candidate objective:* swing còn sống có θ\* ≥ θ_min(parent TF), HOẶC equal-high cluster ≥ 2 trong ε·ATR, HOẶC trùng PDH/PWH/số tròn.
- *Advantages:* proxy tái lập được.
- *Limitations:* là proxy — không đo lệnh thật.
- *Backtest:* P(bị lấy trong N bar) và hành vi sau khi lấy (tăng tốc/đảo chiều) vs swing "thường" cùng khoảng cách.

**(6) Relevant range**
- *Discretionary:* "Range đang quan trọng lúc này."
- *Problem:* tùy tiện.
- *Candidate objective:* valid AND W ≥ c1·stop AND M_ratio ∈ [0, M_max] AND giá trong [L\* − x·W, H\* + x·W] AND nhất quán parent (R3).
- *Advantages:* gắn với quyết định cụ thể.
- *Limitations:* nhiều tham số (c1, M_max, x).
- *Backtest:* kiểm tra từng điều kiện có cải thiện MEHR không (ablation study).

**(7) Fresh range**
- *Discretionary:* "Range mới, chưa bị dùng."
- *Problem:* "dùng" chưa định nghĩa.
- *Candidate objective:* age_bars ≤ T_fresh AND số lần giá vào discount (bull) ≤ 1 kể từ known_at.
- *Advantages:* đơn giản.
- *Limitations:* T_fresh tùy ý.
- *Backtest:* MEHR theo lần chạm thứ 1, 2, 3 vào discount.

**(8) Range invalidation**
- *Discretionary:* "Range đã bị phá."
- *Problem:* nhầm sweep, completion, invalidation.
- *Candidate objective:* HARD rule (mục 5.1.2) với k, m, d cố định; completion và sweep được tách riêng.
- *Advantages:* state machine tái lập.
- *Limitations:* acceptance failure (EC-14) vẫn xảy ra.
- *Backtest:* tần suất acceptance failure; hậu quả của mỗi loại event.

### 18.3. Pseudocode (implementable)

```python
# ---------- 1. Swing detection: Directional Change theo ATR, có known_at ----------
def detect_dc_swings(bars, atr, theta):
    """Trả về swings với known_at = bar mà reversal đạt theta*ATR (không repaint)."""
    swings = []
    mode, ext_px, ext_i = +1, bars[0].high, 0          # +1: đang tìm high
    for i, b in enumerate(bars):
        th = theta * atr[ext_i]                         # ATR tại lúc hình thành extreme
        if mode == +1:
            if b.high > ext_px: ext_px, ext_i = b.high, i
            elif ext_px - b.low >= th:
                swings.append(Swing('H', ext_px, ext_i, known_at=i, theta=theta))
                mode, ext_px, ext_i = -1, b.low, i
        else:
            if b.low < ext_px: ext_px, ext_i = b.low, i
            elif b.high - ext_px >= th:
                swings.append(Swing('L', ext_px, ext_i, known_at=i, theta=theta))
                mode, ext_px, ext_i = +1, b.high, i
    return swings

# ---------- 2. Persistence theta* ----------
THETA_GRID = [0.5, 1, 1.5, 2, 3, 4, 6]                  # HEURISTIC, đơn vị ATR
def theta_star_at(swing_bar, side, swings_by_theta, t):
    best = 0
    for th in THETA_GRID:
        if any(s.bar == swing_bar and s.side == side and s.known_at <= t
               for s in swings_by_theta[th]):
            best = th
    return best

# ---------- 3. Structure state ở scale k (close-break rule) ----------
def structure_events(bars, swings_k):
    events, last_H, last_L, direction = [], None, None, 'UNDEFINED'
    for i, b in enumerate(bars):
        for s in [s for s in swings_k if s.known_at == i]:
            if s.side == 'H': last_H = s
            else:             last_L = s
        if last_H and b.close > last_H.price and not last_H.broken:
            last_H.broken = True
            kind = 'BOS' if direction == 'BULL' else 'MSS'
            origin = lowest_swing_low_between(swings_k, last_H.bar, i)   # origin của leg phá
            events.append(Event(kind, 'BULL', i, broken=last_H, origin=origin))
            direction = 'BULL'
        if last_L and b.close < last_L.price and not last_L.broken:
            last_L.broken = True
            kind = 'BOS' if direction == 'BEAR' else 'MSS'
            origin = highest_swing_high_between(swings_k, last_L.bar, i)
            events.append(Event(kind, 'BEAR', i, broken=last_L, origin=origin))
            direction = 'BEAR'
    return events

# ---------- 4. Leg DR tại thời điểm t ----------
def leg_dr_at(t, bars, events, theta_min, atr):
    ev = last_event_before(events, t)
    if ev is None: return None
    if ev.dir == 'BULL':
        L = ev.origin.price
        H_i = argmax(bars[j].high for j in range(ev.bar, t + 1))
        H = bars[H_i].high
        closed = (H - min(bars[j].low for j in range(H_i, t + 1))) >= theta_min * atr[H_i]
        return DR('LEG', 'BULL', L, H, origin='L',
                  state='ACTIVE' if closed else 'FORMING', known_at=t if closed else None)
    # BEAR: đối xứng

# ---------- 5. Cập nhật state (rút gọn) ----------
def update_state(dr, bar, k=2, m=3, d=1.2, atr=None):
    if dr.dir == 'BULL':
        if bar.low < dr.L and bar.close >= dr.L:
            dr.flag('SWEPT_L')
        if bar.close < dr.L:
            dr.closes_below += 1
            strong = (bar.open - bar.close) / atr >= d
            if dr.closes_below >= k or strong:
                dr.pending_invalid_since = dr.pending_invalid_since or bar.i
        if dr.pending_invalid_since and bar.close > dr.L and bar.i - dr.pending_invalid_since <= m:
            dr.pending_invalid_since = None; dr.flag('RECLAIM')       # failed breakdown
        if dr.pending_invalid_since and bar.i - dr.pending_invalid_since > m:
            dr.state = 'INVALIDATED'
        if bar.high > dr.H and bar.close <= dr.H:
            dr.flag('SWEPT_H')
        if bar.close > dr.H:
            dr.state = 'EXTENDED'                                   # → dựng leg mới theo rule
        if dr.dol and bar.high >= dr.dol.price:
            dr.state = 'COMPLETED'

# ---------- 6. Location Robustness Index ----------
def lri(price, candidates, weights=None):
    valid = [c for c in candidates if c.state in ('ACTIVE', 'SWEPT_L', 'SWEPT_H')]
    if not valid: return None
    w = weights or [1] * len(valid)
    lab = [(+1 if (price - c.L) / (c.H - c.L) < 0.5 else -1) for c in valid]
    return abs(sum(wi * li for wi, li in zip(w, lab))) / sum(w)

# ---------- 7. D1 gate ----------
def d1_gate(ctx):
    if ctx.direction == 'UNDEFINED': return 'FAIL'
    if ctx.primary is None or ctx.primary.state == 'FORMING': return 'FAIL'
    if ctx.dol is None or not (0 < ctx.M_ratio <= ctx.M_max): return 'AMBIGUOUS'
    if ctx.lri is None or ctx.lri < ctx.lri_min: return 'AMBIGUOUS'
    return 'PASS'
```

**Lưu ý triển khai:** (1) `atr` phải là ATR tính đến bar trước đó (không bao gồm bar hiện tại nếu quyết định tại open); (2) mọi hàm nhận `t` và chỉ đọc `bars[:t+1]`; (3) chạy unit test "no-lookahead": chạy hàm tại t với dữ liệu cắt ở t và với dữ liệu đầy đủ — output phải giống hệt nhau.

### 18.4. Trường journal đề xuất (gộp từ War Stories, Best Practices và v0.1)

*Chưa thêm vào template journal — đây là danh sách đề xuất. Mỗi trường gắn với một hypothesis để dữ liệu cá nhân có thể trả lời nó.*

| Trường | Giá trị | Phục vụ câu hỏi |
|---|---|---|
| `range_family` | LEG / CONTAINER / LOOKBACK | Họ range nào đang dùng (§1.2) |
| `range_state_at_entry` | ACTIVE / SWEPT_L / SWEPT_H / PENDING … | Có vào lệnh trên range FORMING/SWEPT không (§5.2) |
| `p_entry`, `p_htf`, `p_ltf` | 0–1 | Location hai tầng (§4.1) |
| `nesting_relation` | consistent / conflicting / overlap / disjoint | HYP-DR-004 |
| `LRI` / `location_conflict` | 0–1 / TRUE-FALSE | HYP-DR-011 |
| `sweep_origin_flag` | TRUE nếu origin bị wick xuyên trước entry | HYP-DR-014 (§5.4.3) |
| `h1_gate`, `d1_gate` | PASS / AMBIGUOUS / FAIL | Lỗi counter-HTF thiếu validation (§4) |
| `range_context` | fresh / one_side_swept / both_swept_SD | W2 |
| `range_width_vs_adr` | W / ADR(20) | W3, EC8 |
| `news_anchor` | TRUE / FALSE | A-3 (§16.1) |
| `near_threshold` | TRUE nếu \|θ\* − θ_min\| < 0.2 | A-1 (§16.1) |
| `invalidation_level`, `invalidation_event` | giá + event (MSS cùng scale / close xuyên origin) | Viết trước khi vào lệnh (§5) |
| `p_bracket`, `R_realized` | — | R thực hiện so với 0 và baseline ngẫu nhiên cùng bracket (§19.3) |

> [!tip] Đo chính mình bằng baseline — đúng cách
> Ghi `R_realized` cho mọi lệnh đã vào theo rule (kể cả lệnh thoát sớm). Sau ≥ 30 lệnh, so **R trung bình** với 0 và với một baseline cùng bracket đặt ở vị trí ngẫu nhiên — chia theo `range_state_at_entry`, `nesting_relation`, `sweep_origin_flag`. **Không** so win rate thô với `p_bracket`: theo dõi rời rạc (gap, nến lớn, slippage) làm win rate lệch khỏi p_bracket theo vị trí ngay cả khi không có edge — chính artifact MEHR ở §19.3.

---

## 19. Backtest & bằng chứng thực nghiệm

### 19.1. Backtesting Methodology

![[Dealing-Range-v01-25-Backtest-Design.svg|1516]]
*Sơ đồ: thiết kế backtest — location study, system study, 8 treatment arms, walk-forward + holdout.*

#### 19.1.1 Câu hỏi nghiên cứu

> **Does Dealing Range selection improve trading expectancy?**

Tách thành hai câu hỏi có thể trả lời riêng:

- **Q1 (Location information):** Location trong một DR được chọn theo cấu trúc có mang thông tin về first-passage outcome vượt baseline không? → *Location Study*.
- **Q2 (System value):** Trong full D1→H1→M5 model, phương pháp chọn DR có làm thay đổi expectancy không, khi mọi thứ khác giữ nguyên? → *System Study* với các treatment arm.

#### 19.1.2 Level 1 — Location Study (không có ICT trigger)

**Mục tiêu:** đo thuần túy giá trị thông tin của location, không bị trộn với chất lượng trigger.

```text
Sự kiện:   mỗi lần giá (close H1) vào một vùng location (bin p) của DR ACTIVE
Bracket:   stop = L* − buffer; target = H* (bullish DR)   [và đối xứng cho bearish]
Outcome:   y_hit (first passage), MEHR = y_hit − p_bracket
Phân tầng: context (D1 direction), p-bin, DR family, W_atr bin, M_ratio bin
Chống phụ thuộc: một sự kiện / DR / bin (lần chạm đầu tiên) để giảm autocorrelation
```

Nếu MEHR ≈ 0 ở mọi bin với structural DR, thì location không mang thông tin — và mọi giá trị trong System Study phải đến từ trigger.

#### 19.1.3 Level 2 — System Study (treatment arms)

Giữ nguyên D1 direction rule, H1 POI rule, M5 trigger, stop, target, session. **Chỉ thay đổi cách chọn DR:**

| Arm | Cách chọn DR | Vai trò |
|---|---|---|
| **A** | Structural Leg DR (mục 3.4.2) | Treatment chính |
| **B** | Container DR | Treatment thay thế |
| **C** | IPDA 20-day (D1) | Baseline khách quan (ICT-native) |
| **D** | Naive fractal: swing high/low 5-bar gần nhất | Baseline ngây thơ |
| **E** | Random anchors: chọn ngẫu nhiên từ candidate set hợp lệ | Placebo — kiểm soát "bất kỳ range nào cũng được" |
| **F** | Không có location filter | Baseline "trigger-only" |
| **G** | ATR-based pseudo range: P ± k·ATR | Baseline không cấu trúc |
| **H** | Previous day high/low (PDH/PDL) | Baseline đơn giản |

**Kết luận chỉ hợp lệ nếu A (hoặc B) vượt C, D, E, F out-of-sample** — đặc biệt phải vượt **E**: nếu anchor ngẫu nhiên từ candidate set cho kết quả tương đương, thì "cấu trúc" không đóng góp gì ngoài việc lọc bớt trade.

#### 19.1.4 Dataset

| Thành phần | Đặc tả đề xuất |
|---|---|
| **Instrument** | Tối thiểu 4–6 instrument khác đặc tính: EURUSD, GBPUSD, XAUUSD, NQ, ES (+ một instrument "khó" như USDJPY) |
| **Timeframe** | D1 (context), H1 (setup), M5 (execution); tick hoặc M1 để giải quyết thứ tự stop/target trong bar |
| **Period** | ≥ 8–10 năm nếu có thể. **Lý do:** D1 leg DR thay đổi chậm — mỗi instrument chỉ có vài chục D1 leg DR/năm; số lượng *DR độc lập* mới là sample size thật, không phải số bar |
| **Session** | Định nghĩa theo giờ New York (xử lý DST); ghi session cho mỗi trade (Asia/London/NY) |
| **Regime** | Gắn nhãn ex-ante: volatility regime (ATR percentile), trend/range (efficiency ratio), trước/sau các thay đổi chính sách lớn |
| **Data hygiene** | Futures: dùng giá unadjusted của contract đang giao dịch cho anchor & level; xử lý rollover; loại bad ticks |

#### 19.1.5 Định nghĩa trước khi xem outcome (pre-registration)

Viết ra và lưu (có timestamp) **trước khi chạy**:

1. Swing definition (DC θ-grid, ATR length, wick anchor).
2. θ_min cho D1, H1.
3. Break rule (close; close + displacement d).
4. Acceptance rule (k, m, d).
5. DR family và selection hierarchy.
6. Entry location rule (ví dụ: p ≤ 0.5 H1 và p_D1 ≤ 0.5 hoặc chỉ H1).
7. Stop rule, target rule, session rule.
8. Chi phí giả định.
9. **Danh sách hypothesis sẽ test và metric chính của mỗi cái.**
10. In-sample / out-of-sample split.

#### 19.1.6 Entry, Stop, Target — biến thể

| Loại | Biến thể (mỗi biến thể = một config; không trộn) |
|---|---|
| **Entry location** | Boundary (gần L\*); EQ; discount bất kỳ; OTE; POI trong discount; POI + LTF confirmation |
| **Stop** | Dưới L\* + buffer; dưới M5 swing (trong khuôn khổ L\*); ATR-based |
| **Target** | Fixed R (2R, 3R); H\* (opposing boundary); DOL (theo rule chọn DOL); structural (next swing cấp k) |

#### 19.1.7 Chi phí và thực thi

- **Spread:** dùng spread lịch sử theo giờ nếu có; nếu không, spread bảo thủ theo session (giãn rộng quanh rollover và tin tức).
- **Slippage:** stop orders chịu slippage — mô hình tối thiểu: slippage = f × spread, lớn hơn trong bar tin tức.
- **Intrabar ambiguity:** nếu stop và target cùng nằm trong một bar và không có dữ liệu thấp hơn, **giả định stop trước** (bảo thủ).
- **Commission:** theo cấu trúc thực tế của broker/prop firm bạn định dùng.
- **Quan trọng cho location sâu:** với entry sâu trong discount, risk theo giá nhỏ → chi phí chiếm tỷ trọng lớn trong R. Phải báo cáo expectancy **sau chi phí**.

#### 19.1.8 Metrics

**Chính:** MEHR (và CI), expectancy E[R] sau chi phí (và CI), R/tháng.
**Phụ:** win rate, average R, median R, profit factor, max drawdown (theo R), MAE/MFE phân phối, streak distribution, setup frequency, time in trade, time-to-target.
**Chẩn đoán:** tỷ lệ acceptance failure, tỷ lệ "location blackout", phân phối LRI, tỷ lệ trade trong mỗi nesting relation.

#### 19.1.9 Sample size — con số thực tế

**Để phát hiện chênh lệch win-rate:**

- So với một baseline cố định (one-sample), p₀ = 0.35 vs p₁ = 0.40, α = 0.05 hai phía, power 80%: **n ≈ 725 trades**.
- So sánh hai arm (two-sample) cùng chênh lệch: **n ≈ 1,470 trades mỗi arm**.

**Để chứng minh expectancy > 0:** với trade có kết quả −1R hoặc +2R, win rate 40% → E = +0.2R, SD ≈ 1.47R.

- n = 100: SE = 0.147R → 95% CI ≈ [−0.09, +0.49] — **không phân biệt được với 0**.
- Cần n ≈ 420 để có power 80% phát hiện E = 0.2R > 0.

**Hàm ý:** một backtest thủ công 50–100 trade **không thể** xác nhận hay bác bỏ một edge cỡ 0.2R. Nó chỉ có thể phát hiện lỗi thô và tạo hypothesis. Đây không phải lý do để không backtest thủ công — mà là lý do để *không kết luận* từ nó, và để hướng tới backtest có hệ thống (lập trình) cho các phần đã formalize được.

#### 19.1.10 Robustness tests

1. **Parameter plateau:** kết quả phải ổn định trên một vùng tham số lân cận (θ_min ± 20%, k ∈ {1,2,3}), không chỉ tại một điểm.
2. **Cross-instrument:** cùng rule, instrument khác.
3. **Cross-period:** chia theo năm; kết quả không được đến từ 1–2 năm.
4. **Long vs short tách riêng** (bất đối xứng volatility).
5. **Session tách riêng.**
6. **Cost stress:** nhân chi phí ×1.5, ×2.
7. **Ablation:** bỏ từng điều kiện (LRI, parent constraint, M_ratio) — điều kiện nào thực sự đóng góp?
8. **Synthetic null:** chạy nguyên hệ thống trên dữ liệu tổng hợp (mục 19.2.4).

### 19.2. Statistical Validation

#### 19.2.1 Các bias và biểu hiện cụ thể trong DR research

| Bias | Biểu hiện trong DR | Kiểm soát |
|---|---|---|
| **Look-ahead** | Dùng range FORMING; dùng pivot trước khi xác nhận; ATR bao gồm bar hiện tại | known_at; unit test no-lookahead |
| **Hindsight** | Chọn anchor "hiển nhiên" sau khi thấy chart | Replay/blind protocol; rule cố định |
| **Selection** | Chỉ backtest các giai đoạn "trend đẹp"; chỉ chọn setup "rõ ràng" | Chạy trên toàn bộ dữ liệu; mọi sự kiện thỏa rule |
| **Survivorship** | Chỉ test instrument đang phổ biến/đang tồn tại; bỏ các giai đoạn thị trường "xấu" | Chọn instrument trước; bao gồm mọi giai đoạn |
| **Overfitting** | Tối ưu θ, k, m, d, LRI threshold trên cùng dữ liệu đánh giá | Walk-forward; OOS chưa từng chạm |
| **Multiple testing** | Test hàng trăm config, báo cáo config tốt nhất | Correction; deflation (36.3) |
| **Data snooping** | Dữ liệu OOS đã được "nhìn" gián tiếp qua các vòng research trước | Holdout khóa; dùng một lần |
| **Regime dependence** | Edge chỉ tồn tại trong một regime volatility | Phân tầng regime ex-ante |

#### 19.2.2 Tại sao ICT concepts đặc biệt dễ overfit

1. **Nhiều bậc tự do ẩn:** mỗi khái niệm (swing, break, sweep, displacement, FVG, OB, DR, DOL) có nhiều cách định nghĩa hợp lý; chuỗi 8 khái niệm × 3 định nghĩa mỗi khái niệm = 3⁸ ≈ 6,500 biến thể mô hình.
2. **Thuật ngữ hấp thụ mọi kết cục:** giá phá low rồi tăng → "sweep"; giá phá low rồi giảm → "MSS". Khi mọi kết cục đều có tên, framework có thể giải thích mọi thứ — tức không dự báo được gì.
3. **Discretion = multiple testing ngầm:** ngay cả khi bạn chỉ "chạy một backtest", mỗi lựa chọn discretionary trong quá trình (swing nào, range nào, POI nào) là một phép chọn giữa nhiều khả năng — Gelman & Loken gọi hiện tượng này là *"garden of forking paths"*.
4. **Học liệu đến từ ví dụ đã chọn lọc:** ví dụ minh họa trong giáo trình được chọn vì chúng hoạt động — survivorship ở cấp giáo dục.

#### 19.2.3 Bùng nổ tổ hợp — ví dụ trong brief

```text
5 loại swing × 5 loại range × 4 entry location × 3 stop rule × 5 target rule = 1,500 config
```

Dưới null (không config nào có edge), với α = 0.05 và các test độc lập, kỳ vọng **~75 config "có ý nghĩa thống kê" chỉ do ngẫu nhiên**. Xác suất có ít nhất một config "có ý nghĩa" ≈ 1. Các config tương quan với nhau nên số test hiệu dụng nhỏ hơn 1,500 — nhưng vẫn đủ lớn để "config tốt nhất" gần như chắc chắn trông ấn tượng.

**Công cụ kiểm soát:**

| Công cụ | Dùng khi | Ghi chú |
|---|---|---|
| Holm–Bonferroni | Ít hypothesis, cần kiểm soát FWER | Bảo thủ |
| Benjamini–Hochberg | Nhiều hypothesis, chấp nhận kiểm soát FDR | Phù hợp giai đoạn khám phá |
| White's Reality Check (White, 2000) | So sánh nhiều chiến lược với benchmark | Bootstrap, có tính tương quan |
| Hansen SPA (Hansen, 2005) | Như trên, ít nhạy với chiến lược kém | Cải tiến của Reality Check |
| Deflated Sharpe Ratio (Bailey & López de Prado, 2014) | Điều chỉnh Sharpe cho số lần thử | Cần ghi lại *số config đã thử* |
| PBO / CSCV (Bailey, Borwein, López de Prado & Zhu) | Ước lượng xác suất backtest overfit | Chia tổ hợp in/out-sample |
| Ngưỡng t cao hơn (Harvey, Liu & Zhu, 2016) | Nghiên cứu nhiều factor | Họ đề xuất t > ~3 cho factor mới |

**Quy tắc thực hành quan trọng nhất:** *ghi lại mọi config đã thử*, kể cả config thất bại. Không có con số này, không thể deflate kết quả.

#### 19.2.4 Synthetic null tests

Chạy toàn bộ pipeline (swing → DR → setup → trigger → outcome) trên:

1. **Random walk Gaussian** với volatility khớp dữ liệu thật → mọi "edge" ở đây là artifact của pipeline hoặc chi phí.
2. **Block bootstrap** của returns thật (giữ volatility clustering, phá cấu trúc thứ tự dài hạn).
3. **Phase-randomized / shuffled** series (tùy mục đích).

Nếu hệ thống cho MEHR > 0 trên (1), có lỗi look-ahead hoặc lỗi mô phỏng thực thi. Nếu cho kết quả tương đương giữa dữ liệu thật và (2), cấu trúc "structure" mà bạn nghĩ đang khai thác không đóng góp.

#### 19.2.5 Khoảng tin cậy và phân phối

- Bootstrap CI cho expectancy (resample theo *DR* hoặc theo *tuần*, không theo trade, để tôn trọng phụ thuộc).
- Báo cáo median R cùng mean R — phân phối R lệch phải mạnh (vài trade lớn chi phối mean).
- Streak distribution: so với phân phối streak kỳ vọng từ win rate đo được (một hệ thống win 35% có chuỗi thua 10+ không hiếm) — quan trọng cho quy tắc drawdown của prop firm.

#### 19.2.6 Walk-forward

```text
[ IS 1 ][ OOS 1 ]
        [ IS 2 ][ OOS 2 ]
                [ IS 3 ][ OOS 3 ]
                                  [ HOLDOUT khóa — dùng đúng một lần ]
```

Tham số chỉ được chọn trên IS; OOS chỉ để đo. Holdout cuối cùng chỉ chạy một lần khi research đã "đóng băng" (v1.0).

### 19.3. Nghiên cứu thực nghiệm v0.2 (2026-10-06)

> [!abstract] Tóm tắt — đọc trước khi đọc số
> **Câu hỏi:** trên dữ liệu OHLC thật, vào lệnh theo hướng leg ở các vị trí khác nhau của leg DR có cho kết quả khác random walk cùng độ biến động không? Anchor cấu trúc có tốt hơn IPDA-20 hay anchor ngẫu nhiên không? Range "chết" như thế nào?
> **Trả lời ngắn (exploratory):** không thấy edge vị trí robust; anchor cấu trúc không tốt hơn baseline một cách nhất quán; gradient "discount tốt hơn" khi đo bằng MEHR là artifact đo lường; sweep origin hạ base-rate continuation; INVALIDATED thuần hiếm — range chết bằng MSS ngược chiều.
> **Không phải:** test pre-registered của HYP-DR-001 (không lọc D1 direction, không trigger LTF, không phí, dữ liệu không phải instrument mục tiêu NQ/XAUUSD intraday). Kết quả *thu hẹp* không gian giả thuyết; chúng không bác bỏ ICT 2022 Model — model đó có direction filter và trigger mà nghiên cứu này cố ý bỏ ra để cô lập *location*.

#### 19.3.1 Dữ liệu

| Nhóm | Instrument | TF | Giai đoạn | Bar | Theo dõi giá | DR ACTIVE (θ = 2) | Sự kiện entry (θ = 2) |
|---|---|---|---|---:|---|---:|---:|
| Cổ phiếu | ORCL, YHOO, NVDA, GOOG | D1 | 1995–2014 (GOOG 2004–2013) | 15,909 | OHLC, giá điều chỉnh theo Adj Close | 667 | 1,613 |
| FX intraday | EURUSD | H1 | 04/2017 → 02/2018 | 5,000 | OHLC | 183 | 416 |
| FX daily | EUR, GBP, JPY, CHF, AUD, CAD vs USD | D1 | 01/1999 → 09/2026 | 6 × 6,955 | **Close-only** (H/L dựng từ close liền kề) | 2,412 | 5,416 |

*Nguồn: các file CSV công khai trên GitHub (dữ liệu mẫu giáo dục); provenance chưa đối chiếu với nhà cung cấp gốc — coi là Tier 4 về độ tin cậy dữ liệu. Không có NQ / ES / XAUUSD intraday.*

#### 19.3.2 Quy tắc

*Minh bạch về thứ tự: quy tắc swing / DR / sự kiện / arm / null được cố định trước khi chạy θ = 2. Thước đo P/W và null close-only được bổ sung **sau** khi thấy MEHR của null có gradient (Kết quả 1); θ = 1.5 và 3 chạy sau như kiểm tra robustness. Không tham số nào được tinh chỉnh theo kết quả.*

```text
ATR        : Wilder ATR(14)
Swing      : Directional Change θ·ATR (θ ∈ {1.5, 2, 3}); swing có known_at = bar xác nhận (xem note 54)
BOS        : close vượt swing đã xác nhận gần nhất chưa bị phá (cùng phía)
Leg DR     : origin = cực trị nhịp hồi giữa swing bị phá và bar break; termination = cực trị sau break
ACTIVE     : khi giá hồi từ termination ≥ θ·ATR(term)   (trước đó: FORMING, không tạo sự kiện)
Hết hạn    : close xuyên origin (INVALIDATED) hoặc BOS mới (EXTENDED nếu cùng chiều / REVERSED nếu ngược)
Sự kiện    : lần close ĐẦU TIÊN rơi vào mỗi bin u ∈ [0,.25), [.25,.5), [.5,.75), [.75,1) của mỗi DR ACTIVE
             u = khoảng cách từ origin / W   (bullish: u = p; bearish: u = 1 − p)
Entry      : open của bar kế tiếp, luôn theo hướng leg
Outcome    : first passage — OHLC: chạm mức trong bar fill tại mức, gap fill tại open, cùng bar chạm cả hai → tính stop
             close-only: thoát ở close đầu tiên vượt mức (có overshoot)
Đo lường   : y = 1 nếu target trước stop;  MEHR = y − u_entry;  P/W = lãi lỗ thực hiện / bề rộng bracket
Không phí  : không spread, không commission, không slippage ngoài gap/overshoot tự nhiên
```

**Bốn arm (cùng sự kiện, cùng hướng, khác bracket):**

| Arm | Bracket | Câu hỏi nó trả lời |
|---|---|---|
| **A — Structural** | stop = origin, target = termination của leg DR | Vị trí trong leg DR cấu trúc có thông tin không? |
| **C — IPDA-20** | stop/target = low/high 20 bar trước (Donchian 20) | Range khách quan có tốt bằng không? |
| **E — Ngẫu nhiên** | một swing low ngẫu nhiên dưới giá + một swing high ngẫu nhiên trên giá (trong 20 swing đã xác nhận gần nhất mỗi phía) | Cấu trúc có hơn "bất kỳ range hợp lệ nào"? |
| **M — Mid bracket** | bracket đối xứng bề rộng W, entry ở giữa (u = 0.5) | Có drift theo hướng leg không, độc lập với vị trí? |

**Null:** với mỗi chuỗi, 5 bản random walk cùng số bar và cùng độ lệch chuẩn log-return (OHLC dựng từ 24 bước/bar, không drift; FX close-only có null close-only tương ứng) — chạy **đúng** cùng code. **Khoảng tin cậy:** 95% cluster bootstrap theo DR (các sự kiện trong một DR không độc lập). **Nested:** parent = leg DR θ×3 trên cùng chuỗi.

*(Thiết kế tổng quát: sơ đồ backtest ở §19.1 — v0.2 hiện thực hóa Level 1 / Location Study với arm A, C, E, M.)*

#### 19.3.3 Kết quả 1 — MEHR theo vị trí là artifact của overshoot

![[Dealing-Range-v02-26-Result-MEHR-Artifact.svg|1516]]
*Sơ đồ: MEHR (trái) và P/W (phải) theo bin u, arm A, θ = 2, toàn universe; ● thật, ◇ null.*

MEHR giảm đều từ +0.084 (bin sâu nhất) xuống −0.058 (sát termination) — đúng hình dạng "discount tốt hơn premium". Nhưng **null cho gần như cùng con số** (+0.074 → −0.056). Tách theo nhóm cho thấy nguồn gốc: ở dữ liệu OHLC (cổ phiếu, EURUSD H1) MEHR ≈ P/W; gradient đến gần như hoàn toàn từ **FX close-only** (73% số sự kiện), nơi lệnh chỉ thoát được ở close — tức thoát *vượt quá* mức stop/target (overshoot).

**[MATHEMATICAL] Vì sao overshoot tạo gradient.** Dưới martingale, optional stopping vẫn đúng cho *giá thoát thực tế*: nếu thoát ở L − δ_L hoặc H + δ_H thì

$$q = P(\text{target trước}) = \frac{uW + \delta_L}{W + \delta_L + \delta_H} \quad\Rightarrow\quad q - u = \frac{\delta_L - u(\delta_L + \delta_H)}{W + \delta_L + \delta_H}$$

Với δ_L = δ_H = δ: q − u = δ(1 − 2u)/(W + 2δ) — **dương ở nửa origin, âm ở nửa termination, tuyến tính theo u**, đúng như dữ liệu, *không cần bất kỳ edge nào*. P/W tính bằng giá thoát thực tế nên vẫn ≈ 0. Hệ quả thực hành: trên chart thật, gap cuối tuần, nến tin và slippage ở stop đóng vai trò δ — tỷ lệ thắng của entry sâu *trông* cao hơn kỳ vọng, nhưng phần thua lớn hơn 1R bù lại.

> [!important] Thay đổi phương pháp — không âm thầm sửa
> **OLD RULE (v0.1, §18.1 và §19.4):** đo thông tin vị trí bằng MEHR = y_hit − r/(r+g); HYP-DR-001 viết theo MEHR > 0.
> **NEW RULE (v0.2):** thước đo chính là **P/W hoặc R thực hiện** (lãi lỗ theo giá thoát thực tế). MEHR chỉ được dùng khi so với **MEHR của null chạy cùng cách theo dõi** (cùng TF, cùng quy tắc fill), dưới dạng MEHR − MEHR_null.
> **REASON:** gradient MEHR theo vị trí xuất hiện y hệt trên random walk khi có overshoot (Kết quả 1).
> **EXPECTED EFFECT:** loại một nguồn "edge giả" lớn nhất của các nghiên cứu location; mọi kết quả cũ dựa trên win rate vs p_bracket phải đọc lại.
> **BACKTEST REQUIRED?** Không cho bản thân thay đổi (là hệ quả toán học + đã quan sát); có cho mọi hypothesis dùng thước đo mới.

#### 19.3.4 Kết quả 2 — P/W theo vị trí × định nghĩa range × θ

![[Dealing-Range-v02-27-Result-Robustness-Grid.svg|1516]]
*Sơ đồ: P/W theo bin u cho arm A / C / E ở θ = 1.5, 2, 3 (36 ô); ô viền cam = CI không chứa 0.*

- **Arm A (structural):** mọi bin có CI chứa 0 ở cả ba θ. Có một độ nghiêng nhỏ, không có ý nghĩa, về phía dương ở hai bin nửa origin khi θ = 1.5 và 2 (+0.013 đến +0.027 W).
- **Arm C (IPDA-20) và E (ngẫu nhiên):** ≈ 0; 2/36 ô "có ý nghĩa" (C θ=3 bin 0.75–1 âm; E θ=3 bin 0.5–0.75 dương) — mức kỳ vọng do ngẫu nhiên là ~1.8 ô, và hai ô này không lặp lại ở θ khác.
- **Arm M (drift theo hướng leg):** +0.006 [−0.014, +0.026] (θ = 2); riêng cổ phiếu +0.023 [−0.011, +0.058] — dấu vết drift dương của cổ phiếu giai đoạn này, không phải của vị trí.

![[Dealing-Range-v02-30-Result-Discount-vs-Premium.svg|1516]]
*Sơ đồ: chênh lệch P/W giữa nửa origin và nửa termination, theo arm × θ.*

**Discount − premium (P/W, đơn vị W):** structural θ = 1.5: **+0.024 [+0.001, +0.044]**; θ = 2: +0.017 [−0.005, +0.039]; θ = 3: −0.004 [−0.031, +0.022]. IPDA-20 và ngẫu nhiên ≈ 0 ở mọi θ. Quy đổi thô cho entry ở nửa origin (u trung bình ≈ 0.30): **≈ +0.04R đến +0.08R mỗi lệnh trước phí** ở θ = 1.5–2. Đọc đúng: một tín hiệu yếu, chỉ ở scale nhỏ, biến mất ở θ = 3, nằm trong vùng mà chi phí giao dịch intraday có thể xóa hết → **HYP-DR-002: WEAK EVIDENCE**; HYP-DR-003: REQUIRES MORE DATA.

#### 19.3.5 Kết quả 3 — Vòng đời leg DR và độ sâu retrace

![[Dealing-Range-v02-28-Result-Lifecycle-Depth.svg|1516]]
*Sơ đồ: P(EXTENDED | độ sâu retrace lớn nhất) — thật vs null; dưới: phân phối độ sâu.*

- Phân phối độ sâu retrace ở dữ liệu thật **gần như trùng** null: ~70% leg DR (cổ phiếu, EURUSD H1) và ~66% (FX close-only) từng vào nửa origin; null 75% / 75% / 65%.
- P(EXTENDED) tăng mạnh khi retrace nông — ở **cả** dữ liệu thật và null → hình học của bracket, và độ sâu chỉ biết *ex-post*.
- Cổ phiếu D1 có P(EXTENDED) cao hơn null ở hầu hết các bin (tổng 0.544 vs 0.487) — đồng nhất với drift/momentum của nhóm này (Arm M), không đồng nhất với một "vùng" đặc biệt.
- Chi tiết kết cục (EXTENDED / REVERSED / INVALIDATED) và đời sống trung vị: [[#5.2. State machine|§5.2.2]].

#### 19.3.6 Kết quả 4 — Sweep origin và mức đồng thuận giữa các định nghĩa

![[Dealing-Range-v02-29-Result-Sweep-LRI.svg|1516]]
*Sơ đồ: trái — P(EXTENDED) theo điều kiện (sweep / không sweep / từng vào discount / chỉ ở premium); phải — % bar mà bốn định nghĩa range đồng thuận.*

- **Sweep protected origin:** P(EXTENDED) 0.28 (cổ phiếu) / 0.24 (EURUSD H1) so với 0.58 khi không sweep; null 0.18 / 0.17. Chi tiết và rule mới: [[#5.4. Sweep vs phá range thật & re-mapping|§5.4.3]].
- **LRI:** bốn định nghĩa chỉ đồng thuận ở 54% / 56% / 70% số bar (cổ phiếu / EURUSD H1 / FX D1) — null 57% / 56% / 69%. Chi tiết: [[#4.4. Bài toán quá nhiều range và LRI|§4.4]].
- **Nested:** nested-consistent −0.018 [−0.094, +0.059] (n = 304), nested-conflicting −0.037 [−0.100, +0.031] (n = 462): không phân biệt được (§4.1).

#### 19.3.7 Giới hạn — vì sao đây chỉ là exploratory

1. **Không phải instrument mục tiêu.** Không có NQ/ES/XAUUSD; EURUSD H1 chỉ ~10 tháng (n nhỏ: 183 DR); FX D1 là close-only.
2. **Không có direction filter và trigger.** Cố ý — để cô lập location. ICT 2022 Model đầy đủ (D1 gate + sweep + MSS + displacement + FVG) chưa được test.
3. **Không phí giao dịch.** Mọi con số P/W là trước chi phí; với H1/M5 FX, spread + commission có thể ≈ 0.05–0.1R mỗi lệnh tùy stop (ước lượng, chưa đo).
4. **Một định nghĩa swing (DC θ·ATR) và một rule break (close).** Wick-break và body-anchor chưa chạy; trong thiết kế §19.1 mới hiện thực arm A, C, E (+ M) — container (B), fractal (D), trigger-only (F), ATR pseudo-range (G), PDH/PDL (H) chưa chạy.
5. **Null đơn giản.** Random walk Gaussian, không volatility clustering, không drift; null cho cổ phiếu không có gap. Một null tốt hơn (block bootstrap của chính chuỗi) có thể thay đổi một số so sánh — đặc biệt Kết quả 3 cho cổ phiếu.
6. **Sự kiện trong cùng DR phụ thuộc nhau** (đã xử lý bằng cluster bootstrap); các DR liên tiếp cũng có thể phụ thuộc (chưa xử lý).
7. **Nhiều phép thử.** ~36 ô robustness + 9 ô discount−premium + ~16 phép thử nested; không hiệu chỉnh multiple testing — vì vậy mọi ô "có ý nghĩa" đơn lẻ được đọc là ngẫu nhiên cho đến khi lặp lại out-of-sample.
8. **Provenance dữ liệu chưa xác minh** (CSV công khai).

#### 19.3.8 Framework thay đổi gì sau nghiên cứu này

| Claim / rule | Trước v0.2 | Sau v0.2 |
|---|---|---|
| Location (discount) tự nó có thông tin | [HYPOTHESIS] chưa test | Proxy: P/W ≈ 0; nghiêng dương yếu ở scale nhỏ — WEAK EVIDENCE |
| Anchor cấu trúc tốt hơn baseline | [HYPOTHESIS] | Không nhất quán so với IPDA-20 / ngẫu nhiên — REQUIRES MORE DATA |
| Thước đo MEHR | Thước đo chính | Chỉ dùng khi trừ null cùng cách theo dõi; thước đo chính = P/W / R |
| Sweep ≠ re-map | Rule | Giữ |
| Sweep làm range "mạnh hơn" | Rule (A3.3, W2, note 57 §14 row 1) | Thay bằng: sweep origin hạ base-rate continuation; cần trigger (§5.4.3) |
| Mức invalidation | Origin | Vận hành: MSS ngược cùng scale; origin là backstop (§5.2.2) |
| LRI thấp là bất thường | Ngầm định | LRI thấp là trạng thái thường trực (~30–46% số bar) |
| "Retrace nông = trend khỏe" | Đọc như tín hiệu | Hình học + ex-post; không dùng làm tín hiệu ex-ante |

#### 19.3.9 Tái lập

Code Python (pandas/numpy) của nghiên cứu được lưu trong vault tại `Claude outputs/dealing-range-v02-study/` — gồm `drstudy.py` (ATR, DC swings, first passage, arms A/C/E/M, null), `lifecycle.py` (vòng đời DR), `run_study.py` (universe + null + bootstrap), `lc_study.py`, `lri_study.py` và script vẽ hình. Chạy lại cho instrument khác: thay hàm load dữ liệu, giữ nguyên mọi tham số đã cố định ở §19.3.2; nếu đổi tham số, ghi version mới của rule.

### 19.4. Falsification

#### 19.4.1 Phê phán hypothesis mẫu trong brief

> "Price reacting from discount of a correctly selected bullish dealing range produces positive expectancy."

| Cụm từ | Vấn đề | Sửa |
|---|---|---|
| "correctly selected" | Nếu "đúng" = "cái đã hoạt động", hypothesis không thể sai | Thay bằng thuật toán A(·) cụ thể, viết trước |
| "reacting from" | Điều kiện hóa trên phản ứng = điều kiện hóa trên outcome (look-ahead) | Thay bằng sự kiện ex-ante: "khi H1 close vào discount" hoặc "khi M5 trigger X xảy ra" |
| "discount" | Discount của range nào, scale nào? | Chỉ định: H1 leg DR, và/hoặc D1 leg DR |
| "positive expectancy" | So với cái gì? Sau chi phí? | "MEHR > 0 và E[R] sau chi phí > 0, và > arm E (random anchors)" |

#### 19.4.2 HYP-DR-001 — phiên bản falsifiable

> **HYP-DR-001:** Trong các giai đoạn D1 direction = BULL (xác định bởi rule R-D1 v0.1 tại close D1 trước đó), các sự kiện "H1 close lần đầu vào p ≤ 0.5 của H1 leg DR ACTIVE (rule A v0.1)" có MEHR > 0 với bracket (stop = L\*_H1 − 0.1·ATR_H1, target = H\*_H1), sau chi phí, trên dữ liệu out-of-sample; và MEHR(arm A) − MEHR(arm E: random anchors) > 0.

- **H₀ (martingale / no information):** E[MEHR] = 0.
- **H₀' (anchor không đóng góp):** E[MEHR_A] = E[MEHR_E].
- **H₁:** E[MEHR_A] > 0 và E[MEHR_A] > E[MEHR_E].
- **Outcome đo:** y_hit (first passage) trên từng sự kiện; MEHR trung bình với bootstrap CI theo DR.
- **Sample size:** mục tiêu ≥ 700 sự kiện OOS (mục 19.1.9) — nếu không đạt, status = REQUIRES MORE DATA, không phải SUPPORTED.
- **Baseline:** arm C (IPDA 20), D (fractal), E (random), F (no filter).
- **Failure criteria (viết trước):**
  - CI 95% của MEHR_A chứa 0 trên OOS → **REJECTED** (ở độ phân giải của dữ liệu).
  - MEHR_A > 0 nhưng không vượt MEHR_E → **REJECTED** cho claim "structural selection đóng góp"; location có thể có giá trị nhưng không nhờ cấu trúc.
  - Kết quả chỉ đạt ở một instrument hoặc một giai đoạn → **WEAK EVIDENCE**.
  - Kết quả biến mất khi θ_min ± 20% → **WEAK EVIDENCE** (không robust).

#### 19.4.3 Falsification cho các thành phần khác

| Thành phần | Điều gì sẽ bác bỏ nó |
|---|---|
| Swing significance scoring | Swing điểm cao bị phá trong k bar với tần suất ≈ swing điểm thấp, khi kiểm soát khoảng cách đến giá |
| EQ có ý nghĩa đặc biệt | Reaction frequency tại 0.5 ≈ tại mức ngẫu nhiên trong [0.2, 0.8] |
| IRL → ERL (dạng mạnh) | P(chạm FVG nội bộ gần nhất trước khi đi thêm x·ATR) ≈ martingale baseline |
| Sweep có ý nghĩa | P(reversal \| sweep theo định nghĩa) ≈ P(reversal) trên random walk cùng volatility |
| Parent constraint (R3) | Ablation: bỏ R3 không làm giảm MEHR |
| LRI | MEHR không tăng theo LRI |

#### 19.4.4 HYP-DR-001 sau v0.2 — phiên bản viết lại thước đo

Giữ nguyên toàn bộ thiết kế ở 19.4.2, chỉ đổi thước đo theo rule mới (§19.3.3):

> **HYP-DR-001 (v0.2):** Trong các giai đoạn D1 direction = BULL (rule R-D1 v0.1, xác định tại close D1 trước đó), các sự kiện "H1 close lần đầu vào p ≤ 0.5 của H1 leg DR ACTIVE" có **R thực hiện trung bình > 0 sau chi phí** với bracket (stop = L\*_H1 − 0.1·ATR_H1, target = H\*_H1) trên dữ liệu out-of-sample; **và** R(arm A) − R(arm E) > 0; **và** R(arm A) − R(null cùng cách theo dõi) > 0.

- **Kết quả proxy v0.2 (không D1 filter, không phí, không phải instrument mục tiêu):** P/W nửa origin của arm A = +0.013 (θ = 2) / +0.023 (θ = 1.5), CI của từng bin đều chứa 0; A − E ≈ +0.02 (CI của từng arm chồng nhau; hiệu số chưa được kiểm định riêng). → **REQUIRES MORE DATA**, không phải REJECTED — vì chưa phải test đã pre-register.
- **Test tiếp theo cần có:** dữ liệu intraday NQ/XAUUSD/EURUSD ≥ 2 năm; D1 direction filter đúng rule; chi phí thực tế; ≥ 700 sự kiện OOS; cùng null.

---

## 20. Hypothesis register & câu hỏi nghiên cứu

### 20.1. Hypothesis register (cập nhật v0.2)

![[Dealing-Range-v02-31-Hypothesis-Status.svg|1516]]
*Sơ đồ: trạng thái 15 hypothesis sau nghiên cứu v0.2 — không hypothesis nào đạt SUPPORTED.*

| ID | Hypothesis | Biến chính | Status | Bằng chứng / ghi chú v0.2 |
|---|---|---|---|---|
| HYP-DR-001 | Nửa origin của H1 leg DR trong D1 BULL có R thực hiện > 0 sau phí và > anchor ngẫu nhiên | R / P/W, arm A vs E | **REQUIRES MORE DATA** | Proxy (không D1 filter, không phí): P/W ≈ 0, structural ≈ random (§19.4.4) |
| HYP-DR-002 | Discount > premium (P/W), kiểm soát khoảng cách DOL | bin u | **WEAK EVIDENCE** | θ = 1.5: +0.024 W [+0.001, +0.044]; θ = 2: +0.017 (ns); θ = 3: −0.004 → không robust; chưa kiểm soát DOL |
| HYP-DR-003 | Structural anchor vượt IPDA-20, fractal, random, ATR, PDH/PDL | arm A–H | **REQUIRES MORE DATA** | A vs C vs E: không khác biệt nhất quán qua 3 θ; B, D, F, G, H chưa chạy |
| HYP-DR-004 | Nested-consistent > nested-conflicting | nesting_relation | **REQUIRES MORE DATA** | Proxy θ 2/6: −0.018 vs −0.037 W, CI chồng nhau (§4.1) |
| HYP-DR-005 | Reaction tại EQ > mức ngẫu nhiên [0.2, 0.8] | reaction rate | UNTESTED | — |
| HYP-DR-006 | Origin có displacement cao ít bị phá hơn trong k bar | D-score | UNTESTED | — |
| HYP-DR-007 | Origin *hình thành* bởi sweep bền hơn origin còn liquidity phía sau | origin_swept_liq | UNTESTED | Khác HYP-DR-014 |
| HYP-DR-008 | IRL→ERL dạng mạnh vượt martingale | P(touch FVG first) | UNTESTED | — |
| HYP-DR-009 | Sau MSS scale k ngược k+1, giá đạt protected của k+1 > baseline | first passage | UNTESTED | — |
| HYP-DR-010 | Hướng breakout khỏi compression theo D1 direction (vượt drift baseline) | breakout dir | UNTESTED | — |
| HYP-DR-011 | Expectancy tăng theo LRI | LRI bins | UNTESTED | Đã đo phân phối: đồng thuận 54–70% số bar = null (§4.4) |
| HYP-DR-012 | Có plateau của k (acceptance) | k, failure rate | UNTESTED | — |
| HYP-DR-013 | Thông tin location giảm khi M_ratio tăng | M bins | UNTESTED | — |
| **HYP-DR-014** *(mới)* | Sau sweep protected origin, **có** trigger LTF theo hướng leg (MSS + displacement) thì P(EXTENDED) và R vượt base-rate sau sweep và vượt null | sweep_origin_flag × trigger | UNTESTED | Base-rate sau sweep: 0.24–0.28 (null 0.17–0.18) — §5.4.3 |
| **HYP-DR-015** *(mới)* | Leg DR trên cổ phiếu D1 tiếp diễn nhiều hơn random walk, và phần chênh khai thác được sau phí | P(EXTENDED), R continuation | **WEAK EVIDENCE** (phần thống kê) / UNTESTED (khai thác) | 0.544 [0.507, 0.583] vs null 0.487; trùng với drift arm M — có thể chỉ là drift của mẫu |

**Phát hiện phương pháp (không phải hypothesis):** M-01 — MEHR thô có gradient theo vị trí khi có overshoot, kể cả trên random walk (§19.3.3). M-02 — Bốn định nghĩa range hợp lệ bất đồng về phía premium/discount ở 30–46% số bar, bằng null (§4.4). M-03 — Leg DR θ = 2 kết thúc bằng MSS ngược chiều chứ hầu như không bằng close xuyên origin thuần (§5.2.2).

### 20.2. Câu hỏi nghiên cứu mở

**Cập nhật v0.2:** câu 2 và 3 dưới đây đã có câu trả lời *proxy* (không robust / không khác biệt) — chuyển sang dạng test đầy đủ trên instrument mục tiêu. Câu 14 (scale tự nhiên θ): trên θ ∈ {1.5, 2, 3}, kết quả **phẳng** quanh 0, với nghiêng dương yếu ở θ nhỏ. Ba câu hỏi mới được đặt lên đầu:

- **N1 (ưu tiên cao nhất):** Chạy lại §19.3 trên NQ / XAUUSD / EURUSD M5–H1 ≥ 2 năm, có chi phí — kết quả có giữ nguyên "location ≈ 0" không?
- **N2:** HYP-DR-014 — trigger LTF sau sweep origin có tách được 0.25 base-rate thành hai nhóm khác nhau rõ rệt không?
- **N3:** Thêm D1 direction filter (Level 2 của §19.1): khi có direction, location có *khuếch đại* được gì không (đúng như lý thuyết amplifier)? Nếu direction không có edge, location không thể có.

**Ưu tiên cao (ảnh hưởng trực tiếp đến framework D1→H1→M5):**

1. Trên các instrument bạn định trade, D1 leg DR thay đổi bao nhiêu lần mỗi năm với θ_min = 2 ATR? (Xác định sample size thực tế có thể đạt.)
2. Location Study (mục 19.1.2): MEHR theo p-bin có khác 0 không, trên H1 leg DR trong D1 BULL/BEAR?
3. Arm A vs arm E (random anchors): cấu trúc có đóng góp vượt "bất kỳ range hợp lệ nào"?
4. Tỷ lệ "redraw" cá nhân trong case study thủ công (mục 5.5.4) là bao nhiêu? (Đo hindsight của chính bạn.)
5. Inter-rater reliability: cùng một chart, hai lần phân tích cách nhau 2 tuần, range trùng khớp bao nhiêu phần trăm?

**Ưu tiên trung bình:**

6. θ\* có dự báo protection (P(not violated in k bars)) tốt hơn fractal n không?
7. Wick vs body anchor — kết quả có nhạy không?
8. Acceptance rule k nào tạo plateau?
9. Xung đột leg/parent (HYP-DR-004) phổ biến đến mức nào trong trend mạnh, và nó ảnh hưởng R/tháng thế nào?
10. Location blackout sau MSS kéo dài bao lâu trung bình? Bao nhiêu trade thua của bạn rơi vào blackout?

**Ưu tiên thấp / khám phá:**

11. IPDA-20 breakout: continuation hay reversal theo regime? (Trend-following vs ICT trên cùng một level.)
12. Volume/delta trên NQ có cải thiện phân biệt sweep vs break không?
13. EQ vs POC (Market Profile) — mức nào có reaction nhiều hơn?
14. Có tồn tại một "scale tự nhiên" (θ_min) mà tại đó MEHR cực đại và ổn định, hay kết quả phẳng theo θ?
15. Kết quả có ổn định trước/sau các regime vĩ mô lớn không?

### 20.3. Vị trí trong vault

| Nội dung | Nơi đặt / liên kết |
|---|---|
| Lớp khái niệm (định nghĩa → mức độ thành thạo) | §1–13 của note này |
| Cơ chế, phản biện, catalog edge case, case studies | §14–17 của note này |
| Định lượng, backtest, thực nghiệm v0.2, register | §18–20 của note này |
| Code nghiên cứu v0.2 | `Claude outputs/dealing-range-v02-study/` |
| Swing detection (Directional Change, θ\*) | [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] |
| Swing density & DOL precedence | [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] |
| Bản nghiên cứu DR trước (VALID / REFINED / SUSPENDED / REPLACED) | [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] |
| Re-mapping sau displacement | [[37-Re-mapping-Dealing-Range-sau-Displacement]] |
| State machine D1–H1–M5 của model | [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] |
| IRL ↔ ERL, Premium/Discount, OTE, Daily Bias | [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[27-Premium-Discount]] · [[26-OTE-Optimal-Trade-Entry]] · [[59-Daily-Bias]] |
| Backtest theo 19.1 | `04 - Backtesting/` (bắt đầu từ `Backtest templete.md`) |
| Journal fields đề xuất (chưa thêm vào template) | xem bảng đầy đủ ở §18.4 |

**Versioning:** các rule cấu trúc là **v0.1**; thay đổi của v0.2 ghi ở §20.4. Khi thay đổi, ghi: OLD RULE → NEW RULE → REASON → EXPECTED EFFECT → BACKTEST REQUIRED?

### 20.4. Changelog v0.1 → v0.2

| Thay đổi | Chi tiết |
|---|---|
| **Gộp cấu trúc** | Phần concept cũ (§1–17) + Structural Framework v0.1 (§18.0–18.40) → một note 20 mục theo thứ tự template ICT Concept (§1–13) + mục chuyên sâu (§14–20). Mỗi chủ đề có một nơi trình bày đầy đủ. |
| **Ánh xạ số mục cũ → mới** | 18.2→1.3 · 18.3→1.4 · 18.4→1.1 · 18.5→2.1 · 18.6→14.1 · 18.7–18.12→3.1–3.6 · 18.13–18.14→4.1–4.2 · 18.15→5.3 · 18.16→5.1–5.2 · 18.17–18.21→14.3–14.7 · 18.22→7.2 · 18.23→§4 (D1/H1/M5) · 18.24–18.25→4.3–4.4 · 18.26 + 18.33 + EC1–9 + W1–5→§16 · 18.27 + §9 cũ→§9 · 18.28→5.5 · 18.29–18.30→18.1–18.2 · 18.31→7.3 + 18.3 · 18.32→17.1 · 18.34→14.8 · 18.35–18.37→19.1, 19.2, 19.4 · 18.38→15.4 · 18.39→12.4 + §2 · 18.40→20 |
| **Callout "Cập nhật v0.1"** | Viết lại thành nội dung chính tại chỗ (định nghĩa §1, liquidity §2.2, W0 + 14.1 cũ → §14.2, critique §15, EQ decay §16.4). |
| **Gỡ trùng lặp** | A1 quadrant → §14.4.7; A2 nested → §4.1.0; A3 re-mapping → §5.4.2; A5 ERL↔IRL → §14.5.6; §14.2 cũ (AMT/Wyckoff/footprint) → §14.8.3; 18.1 executive summary → callout đầu note; 18.39.3 → §2. |
| **Bỏ khỏi note (file vẫn còn trong attachments)** | Dealing-Range-Sec-01…05.svg, Deep-Mechanism.svg, Edge-Cases.svg, Example-Correct.png, Example-Wrong.png — nội dung đã được thay bằng sơ đồ v01 và chart dữ liệu thật. |
| **Mới** | §19.3 nghiên cứu thực nghiệm; 5 chart dữ liệu thật (Real 1–5); 6 sơ đồ (v02-00, 26–31); §5.2.1–5.2.2; §5.4; §16 catalog gộp; §18.4 journal fields; HYP-DR-014, 015; M-01…M-03. |
| **Rule đổi (OLD/NEW ghi tại chỗ)** | (1) Sweep origin: không còn "range mạnh hơn" (§5.4.3). (2) Thước đo: MEHR → P/W / R, MEHR chỉ dùng khi trừ null (§19.3.3). |
| **Sửa link** | Link alias không resolve (`[[Break of Structure]]`, `[[Displacement]]`, `[[Fair Value Gap]]`, `[[Order Block]]`, `[[Optimal Trade Entry]]`) → link tới file thật với alias hiển thị. |
| **Không đổi** | Frontmatter keys; quy ước REFINED của note 57 cho wick ở termination (Scenario E); D1/H1/M5 gates; R1–R7; mọi threshold vẫn là HEURISTIC. |

### 20.5. Phụ lục — Quality control (20 câu của brief v0.1)

| # | Câu hỏi | Trả lời | Mục |
|---|---|---|---|
| 1 | Giải thích cho beginner? | Có — Level 1, ẩn dụ cây thước, ví dụ số | 1.3, 1.4, 1.1.1 |
| 2 | Expert depth? | Có — martingale null, θ\*, state machine, MEHR | 3.2, 5.1, 14.3, 18.1 |
| 3 | Market structure trước range selection? | Có | 3.1 → 3.4 |
| 4 | "Swing nào thực sự quan trọng"? | Có — consequence + θ\* + role + known_at | 3.2, 3.3, 4.3 |
| 5 | "Quá nhiều DR"? | Có — valid/relevant/tradeable, LRI | 4.4 |
| 6 | Nested/overlapping? | Có — 5 loại quan hệ | 4.1, 4.2 |
| 7 | Range updating? | Có — Scenario A–I | 5.3 |
| 8 | Range invalidation? | Có — 5 loại + acceptance + state machine | 5.1 |
| 9 | P/D vs predictive edge? | Có — martingale null, amplifier | 14.3, 14.4 |
| 10 | Boundary vs liquidity? | Có — 4 khái niệm tách riêng | 14.5 |
| 11 | DOL vs boundary? | Có | 14.5.1, 14.6 |
| 12 | Kiểm soát hindsight? | Có — 5 cơ chế, known_at, blind protocol | 5.5 |
| 13 | Counterexamples? | Có — 25 | 16 |
| 14 | Subjective → measurable? | Có — 8 khái niệm | 18.1, 18.2 |
| 15 | Backtest methodology? | Có — Location Study + System Study, 8 arms | 19.1 |
| 16 | Multiple testing / overfitting? | Có — 1,500 config, corrections | 19.2 |
| 17 | ICT vs market mechanics? | Có — nhãn xuyên suốt | 14.1, 14.5, 14.8 |
| 18 | Hypotheses cần validation? | Có — 13 HYP-DR | 20.1 |
| 19 | Decision framework → systematic rules? | Có — decision tree + pseudocode | 7.3 |
| 20 | Khi nào KHÔNG dùng DR? | Có | 2 (Khi nào nên bỏ qua?) |

---

## Tài liệu tham khảo

**Academic / institutional (Tier 1–2):**

- Osler, C. L. (2003). *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.* Journal of Finance, 58(5). — NY Fed Staff Report 125: https://www.newyorkfed.org/research/staff_reports/sr125.html
- Osler, C. L. (2005). *Stop-Loss Orders and Price Cascades in Currency Markets.* Journal of International Money and Finance. — NY Fed Staff Report 150: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.pdf
- Glattfelder, J. B., Dupuis, A., & Olsen, R. B. (2011). *Patterns in high-frequency FX data: discovery of 12 empirical scaling laws.* Quantitative Finance. — arXiv: https://arxiv.org/abs/0809.1040
- Kyle, A. S. (1985). *Continuous Auctions and Insider Trading.* Econometrica.
- White, H. (2000). *A Reality Check for Data Snooping.* Econometrica.
- Hansen, P. R. (2005). *A Test for Superior Predictive Ability.* Journal of Business & Economic Statistics.
- Bailey, D. H., & López de Prado, M. (2014). *The Deflated Sharpe Ratio.* Journal of Portfolio Management.
- Bailey, D. H., Borwein, J., López de Prado, M., & Zhu, Q. J. *The Probability of Backtest Overfitting.* Journal of Computational Finance.
- Harvey, C. R., Liu, Y., & Zhu, H. (2016). *…and the Cross-Section of Expected Returns.* Review of Financial Studies.
- Gelman, A., & Loken, E. (2014). *The Statistical Crisis in Science* ("garden of forking paths"). American Scientist.
- Black, F. (1976); Christie, A. (1982) — leverage effect / asymmetric volatility.

**Practitioner frameworks (Tier 3):** Dow Theory (secondary reactions 1/3–2/3); Wyckoff method (trading range, spring, upthrust); Auction Market Theory / Market Profile (Steidlmayer; Dalton, *Mind Over Markets*); Donchian channel / Turtle breakout system.

**ICT community documentation (Tier 3–4 — dùng cho định nghĩa, không phải bằng chứng):**

- LuxAlgo Library — Internal vs External Range Liquidity: https://www.luxalgo.com/library/concept/internal-vs-external-range-liquidity/
- LuxAlgo Library — IPDA & Price Delivery Theory: https://www.luxalgo.com/library/concept/ipda-and-price-delivery-theory/
- TradingView — ICT IPDA Look Back (toodegrees): https://www.tradingview.com/script/rTJEJb5v-ICT-IPDA-Look-Back/

**Mô phỏng trong note này:** random walk Gaussian (numpy, seed cố định): fractal pivot frequency (2 triệu bước), first-passage theo vị trí trong range (20,000–40,000 path/ô), DC overshoot, tần suất "sweep" trên OHLC tổng hợp (60,000 bar × 50 tick). Đây là kết quả mô phỏng của *mô hình null*, không phải dữ liệu thị trường.

**Dữ liệu cho nghiên cứu v0.2 (§19.3):** chuỗi giá D1 ORCL, YHOO, NVDA (Adj Close), GOOG; EURUSD H1 (04/2017–02/2018, 5,000 bar); tỷ giá ngày của 6 đồng tiền so với USD (1999–2026, close-only) — tất cả từ file CSV công khai trên GitHub, dùng cho mục đích giáo dục; provenance chưa đối chiếu với nhà cung cấp gốc. Sự kiện bối cảnh của Real 5: vòng 1 bầu cử Tổng thống Pháp ngày 23/04/2017 (gap mở cửa EURUSD tuần sau đó).

**Liên quan trong vault:** [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] (Directional Change, θ\*) · [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]].
