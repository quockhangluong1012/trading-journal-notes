---
title: "Tổng hợp phiên debate — US Tech 100 Daily Bias"
date: 2026-08-03
instrument: US Tech 100 (NDX CFD, Spreadex feed, TradingView)
timeframes: D1 (turn 1, turn 5) + H1, W1 (turn 3)
mode: LIVE (hard right edge — outcome chưa biết với cả hai bên)
skills: extract-screenshot-data (ICT-VISION) · ict-devils-advocate · ict-doctrine
files:
  - daily-bias/extraction_ustech100_d1_2026-08-03.json
  - daily-bias/devils-advocate-ustech100-2026-08-03.md
  - daily-bias/trading-rules.md
  - daily-bias/assets/*.svg
---

# Tổng hợp phiên debate — US Tech 100 Daily Bias (2026-08-03)

> Tài liệu này tổng hợp 5 turn debate giữa trader và devil's advocate, soi lại bằng lăng kính
> ict-doctrine, kèm 4 sơ đồ minh họa và 3 case study rút từ chính phiên này.
>
> **Lưu ý phương pháp:** file `references/doctrine.md` của skill ict-doctrine không có trong bundle
> phiên này, nên mọi doctrine anchor dưới đây trích từ **bảng định nghĩa nhanh trong SKILL.md** của
> ict-doctrine — đủ cho evidence bar từng term, nhưng không thay được anchor chi tiết per-term.

---

## 1. TL;DR — thesis đã đi từ đâu đến đâu

| | Turn 1 (thesis gốc) | Turn 5 (trạng thái cuối) |
|---|---|---|
| **Bias** | Bullish, "giá đã reclaim vào lại range" | Bullish **có điều kiện** — chờ D1 close acceptance bên trong range |
| **Sweep claim** | "Đây là 1 Liquidity Sweep" (khẳng định) | AMBIGUOUS — fork O1′, chờ phân xử bằng backtest T3 |
| **Reclaim** | Khẳng định đã xảy ra | Chưa chứng minh — **zero** close hoàn chỉnh D1/W1 trên 28,187 (O2) |
| **Invalidation** | Không có | 28,187 + acceptance bên dưới (commit turn 3) |
| **Target** | Không nêu | EQH 30,660.9 · DR high 30,728.3 (pool có tên) |
| **Kiến trúc quyết định** | Không có | **D1-gate** (Rule R1, commit turn 5) — thiếu duy nhất tham số "acceptance" (O8) |
| **Verdict** | BROKEN | UNPROVEN — falsifiable & coherent, evidence pending |

Thesis không "thắng" cũng không "thua" sau 5 turn — nó **tiến hóa từ một khẳng định không falsifiable
thành một framework có invalidation, target, kiến trúc quyết định và test tiền đăng ký**. Đó là kết quả
thật của debate, không phải verdict một chiều.

![Price map D1](assets/price-map.svg)

---

## 2. Diễn biến 5 turn

| Turn | Input | Sự kiện chính |
|---|---|---|
| 1 | Chart D1 + thesis "sweep EQL 28,197, đã reclaim, bias Bullish" | Extraction JSON; 6 objection (O1 fatal — mô tả nến sai; O2 — reclaim chưa có close chứng minh). Verdict: BROKEN |
| 2 | Rebuttal W1: "nến thân rất dài đã đóng lại trong range" | O1 → NARROWED O1′ (concede hình sweep W1: thân 8%, râu dưới 75%; giữ: nến thân dài là tuần 20–24/7 đóng 28,135 DƯỚI range). O7 issued: tự mâu thuẫn "đã đóng trong range" vs "khó nói giá quay lại range" |
| 3 | Chart H1 + W1, commit invalidation 28,187 + target 30,660.9/30,728.3 | Số platform-exact: W1 close 28,160.6 (dưới biên 26.4 pts) → O7 CLOSED (claim bị falsify); O4, O5 WITHDRAWN (arithmetic discount đúng, framework đã falsifiable); O6 CLOSED; O2 sharpened thành load-bearing |
| 4 | "Tổng hợp đúng/sai + có phải chờ D1, no-trade hôm nay?" | Scoreboard; O8 (acceptance chưa có số), O9 (vai trò H1/kiến trúc chưa chọn), O10 (H1 positional, gap-borne) |
| 5 | Commit kiến trúc D1-gate, rule cố định từ hôm nay | O9 WITHDRAWN (điều kiện retraction thỏa); Rule R1 ghi vào `trading-rules.md`; O8 thành gate-blocker duy nhất |

---

## 3. Doctrine check — soi lại các label bằng ict-doctrine

Trạng thái theo taxonomy chuẩn (PASS / FAIL / UNSUPPORTED / HINDSIGHT / AMBIGUOUS):

| Term / claim | Status | Căn cứ (anchor: bảng định nghĩa nhanh, ict-doctrine SKILL.md) |
|---|---|---|
| **Liquidity pool** — EQL 28,192–28,237 là pool có tên | **PASS** | "Sweep = quét liquidity tại level *có tên*" — level được nêu đích danh, khớp đo đạc twin lows tháng 6 trong ±5 pts |
| **Sweep** — label cho đợt 24–29/7 | **AMBIGUOUS** (fork O1′) | Evidence bar của sweep: level có tên ✓ + *được dùng/reject* — nhưng đợt này có break + 3 close D1 rõ dưới pool, sâu −4.06%, kéo 4–5 phiên. Canon **không fix** độ sâu/số phiên tối đa → doctrine gap, không được tự chế chuẩn để FAIL hay tự nới chuẩn để PASS. Phân xử: backtest T3 |
| **Premium/Discount** — "giá đang discount" | **PASS** | "Theo midpoint của dealing range chọn đúng" — DR commit 28,187–30,728.3, EQ 29,457.7, giá 28,486.6 → depth 9.3%; robust khi thay low 27,052 (37.3%). Arithmetic kiểm bằng Python, không lệch |
| **DOL / Target** — EQH 30,660.9 + DR high | **PASS** | "Mô tả draw on liquidity (pool đối diện), không phải khuyến nghị trade" — pool có tên, khớp June highs đo được |
| **Reclaim / "giá đã vào lại range"** | **UNSUPPORTED → FAIL fact tại W1** | Turn 1–2 claim reclaim khi zero close hoàn chỉnh trên 28,187; riêng "W1 đã đóng trong range" bị số platform-exact bác (28,160.6 < 28,187) — sai fact, không phải sai định nghĩa |
| **"Acceptance"** (term trung tâm của rule R1) | **UNDEFINED** | Không nằm trong bảng canon — đây là term *vận hành* do trader tự đưa vào. Không có định nghĩa ex-ante thì mọi phán quyết sweep-vs-acceptance là post hoc (O1′, O8) |
| **MSS D1** | *không được claim* | Đúng kỷ luật: chưa có body close phá LH 29,163 thì chưa được gọi MSS — trader không overcall term này ở bất kỳ turn nào |
| **NWOG 286.9 pts** | **PASS** (fact) | Đo platform-exact: prior W1 close 28,160.6 → open 28,447.5; chưa fill 236.9 pts. Chính trader là người chỉ ra hệ quả: vị trí "trên range" hiện tại là gap-borne |
| **Hindsight** | không phạm | Mode LIVE — rủi ro chính không phải hindsight mà là *unfalsifiability*, và nó đã được xử bằng commit invalidation + target ở turn 3 |

**Điểm doctrine đáng giá nhất của phiên:** ranh giới sweep ↔ acceptance là **doctrine gap thật** — canon
định nghĩa sweep bằng "quét + được dùng (reject)" nhưng không định lượng bao sâu, bao lâu thì một
excursion hết được gọi là sweep. Cả hai phía đều không được phép phán bừa chỗ này; lối ra duy nhất
sạch là tiêu chí ex-ante + backtest (T3).

---

## 4. Objection ledger — toàn bộ vòng đời O1–O10

![Ledger lifecycle](assets/ledger-lifecycle.svg)

| # | Tier | Severity | Attacks | Nội dung | Trạng thái cuối | Điều kiện rút |
|---|---|---|---|---|---|---|
| O1′ | [CHART]→[METHOD] | fatal→material | C1 | Mô tả nến phá sai (body-dominant, không phải "râu dài thân nhỏ"); sau narrow: thiếu tiêu chí ex-ante sweep-vs-acceptance | **OPEN** — fork trung tâm | Tiêu chí ex-ante + kết quả T3 |
| O2 | [CHART] | material, **load-bearing** | C3 | Reclaim chưa chứng minh: zero close hoàn chỉnh D1/W1 trên 28,187 kể từ low 27,052; vị trí hiện tại 100% gap-borne | **OPEN** | D1 close > 28,237 (28,272 an toàn tolerance) |
| O3 | [CHART] | material | C2 | HH/HL không còn là cấu trúc operative (chuỗi LH 30,596→…→29,163) | **OPEN ↓** | Body close D1 > 29,163 |
| O4 | [ARITHMETIC] | material | C4 | Nghi vấn arithmetic discount | **WITHDRAWN** (turn 3) — số của trader đúng | — |
| O5 | [METHOD] | material | C5 | Thesis không falsifiable (không invalidation/target) | **WITHDRAWN** (turn 3) — đã commit cả hai | residual → thành O8 |
| O6 | [CHART] | minor | C1 | 28,197 vs mức đo 28,187/28,192 | **CLOSED** (turn 3) | — |
| O7 | [SELF-CONTRADICTION] | material | C6 | "W1 đã đóng trong range" vs chính trader nói gap làm giá bật — số platform-exact phán: đóng DƯỚI | **CLOSED** (turn 3) — claim bị falsify, trader bỏ claim | — |
| O8 | [METHOD] | material, **gate-blocker** | C8+C10 | "Acceptance" chưa có số → rule R1 chưa vận hành được | **OPEN** | N, X, body/wick, limbo — điền trước D1 close đầu tiên |
| O9 | [METHOD] | material | C9+C10 | Kiến trúc chưa chọn (D1-gate vs H1-confirm-trong-bias) + rule viết giữa phiên | **WITHDRAWN** (turn 5) — kiến trúc D1-gate được commit, ghi file auditable | residual: tái sinh thành [SELF-CONTRADICTION] nếu vi phạm |
| O10 | [CHART] | material→minor-in-consequence | C9 | "H1 bias bullish" là positional read: failure swing thứ Sáu (28,59→27,96) + ~10 nến post-gap, chưa có MSS/displacement H1 | **OPEN ↓** (decoration dưới D1-gate) | H1 higher-low sau gap-fill, hoặc H1 body close > 28,59 |

**Kỷ luật ledger đã giữ được:** số objection ổn định qua 5 turn, không renumber; concede bằng số
(O4, O5, O9 withdrawn khi evidence/commitment tới); không manufacture objection mới khi một objection
được trả lời (turn 5: zero objection mới).

---

## 5. Scoreboard — trader đúng ở đâu, sai ở đâu

**ĐÚNG (evidence chống lưng):**
- Vùng EQL có thật; 28,197/28,187 khớp đo đạc trong ±5 pts
- Break 24/7 đúng ngày
- Nến W1 tuần qua đúng *hình* sweep (thân 8% range, râu dưới 75%)
- Phát hiện weekly opening gap — đúng và exact (286.9 pts), tự chỉ ra hệ quả bất lợi cho thesis của mình
- Arithmetic discount 9.3% đúng theo DR đã commit; robust khi đổi biên
- Target là pool có tên, khớp June highs
- Commit invalidation trước outcome; không overcall MSS

**SAI (bị chứng cứ bác):**
- "Nến phá có râu dài, thân không quá lớn" — các nến phá D1 đều body-dominant
- "Giá đã reclaim vào lại range" (turn 1) — chưa từng có close hoàn chỉnh trên 28,187
- "Nến W1 thân rất dài đã đóng lại trong range" (turn 2) — close 28,160.6 dưới biên; và nến thân dài (tuần 20–24/7, đóng 28,135 dưới range) với nến đóng-gần-biên là **hai nến khác nhau**

**CHƯA CHỨNG MINH (mở):**
- Reclaim/acceptance vào lại range (O2 — load-bearing)
- Đợt 24–29/7 là sweep hay failed acceptance (O1′ — fork trung tâm)
- HH/HL còn là cấu trúc operative (O3 — giảm trọng lượng)

---

## 6. Case studies

### CS1 — Sweep vs Acceptance: cùng "quét", khác bậc chứng cứ

![Sweep vs Acceptance](assets/sweep-vs-acceptance.svg)

Textbook sweep (panel A) đạt evidence bar dễ dàng: wick xuyên pool có tên, body close ngay lại bên
trên, không có close nào dưới. Case thật của phiên này (panel B) khác hẳn về *bậc chứng cứ*: break
24/7 + 3 close D1 rõ dưới pool (28,045 / 27,800 / 27,097), sâu −4.06%, kéo 4–5 phiên — rồi mới quay
về nhờ một nến +1,130 pts và một gap 286.9 pts.

**Bài học:** gọi panel B là "sweep" *chỉ vì giá đã quay lại* là định nghĩa bằng outcome — post hoc.
Dưới cùng logic đó, nếu giá không quay lại thì cùng một cụm nến sẽ được gọi là "acceptance". Một label
mà outcome quyết định thay cho tiêu chí thì không dùng được tại hard right edge. Doctrine không fix
lằn ranh này (gap thật) → lối ra là tiêu chí ex-ante, kiểm bằng T3.

### CS2 — Vị trí gap-borne ≠ reclaim organic

Thứ Sáu 31/7, lần test organic cuối cùng của mức 28,187 trên H1 **thất bại**: giá lên 28,59, gãy
ngược về 27,96, đóng tuần 28,160.6 — dưới biên. Sáng thứ Hai giá đứng 28,486.6, "bên trên range" —
nhưng 100% quãng vượt biên đó là weekly opening gap, không có nến nào *giao dịch* xuyên qua mức.

**Bài học:** "giá đang trên X" là hai claim khác nhau tùy con đường: vị trí (positional) và cấu trúc
(structural). Thị trường chưa hề *đấu giá* qua 28,187 — nó nhảy qua. Chính trader là người phát hiện
điều này ở turn 2, và đó là lý do O2 vẫn mở dù giá "đã ở trên": nếu gap fill mà mức không giữ được,
toàn bộ position case sụp mà không có tầng structural nào đỡ. Test phân xử: gap-fill matrix (T2′).

### CS3 — Rule viết giữa phiên: free parameter kể cả khi conservative

Turn 4, trader đề xuất "bias có điều kiện ⇒ chờ D1 ⇒ no-trade" — nghe rất kỷ luật. Nhưng rule này
(a) chưa từng được viết trước đó, (b) dùng term "acceptance" chưa có số, (c) mâu thuẫn tiềm tàng với
cascade D1→H1→M5 đang dùng ở các case khác. Một rule sinh ra giữa phiên theo hướng *thận trọng* vẫn
là free parameter: lần sau, dưới áp lực ngược chiều, nó sẽ bị nới theo hướng ngược lại — cũng giữa phiên.

**Bài học:** giá trị của rule không nằm ở nội dung mà ở **thời điểm và nơi nó được viết**. Giải pháp
của phiên: chọn kiến trúc công khai (D1-gate), ghi vào file auditable (`trading-rules.md`), đánh dấu
tham số còn thiếu — và chấp nhận rằng O9 sẽ tái sinh thành [SELF-CONTRADICTION] nếu rule bị vi phạm
ngay lần thử đầu tiên.

---

## 7. Rule R1 và tham số còn thiếu

![D1-gate flow](assets/d1-gate-flow.svg)

Rule R1 (commit 2026-08-03, 15:41 +07): **kiến trúc D1-gate** — no-trade đến khi D1 có close
acceptance bên trong range; trước đó mọi read H1/M5 không mang trọng lượng quyết định. Invalidation
giữ nguyên rule turn 3: close < 28,187 + acceptance bên dưới → bias invalid.

Gate chưa vận hành được vì 4 ô trống (O8): **N** close, mức **X** (28,187 hay 28,237), body/wick,
và cách xử lý limbo 28,187–28,237. Deadline tự nhiên: D1 close đầu tiên sau commit (~05:17 +07 ngày 4/8).

---

## 8. Pre-registered tests

| Test | Thiết kế | Ngưỡng cam kết trước | Quyết định |
|---|---|---|---|
| **T2′ — gap-fill matrix** (≤3 phiên) | (a) fill NWOG về 28,16–28,20 rồi D1 close ≥ 28,237 → reclaim organic; (b) fill + close < 28,187 + acceptance → invalidated theo rule của chính trader; (c) không fill, body close > 29,163 → bias confirmed structurally | như 3 nhánh | (a) rút O2 · (b) sập bias · (c) O2 moot + đóng O3 |
| **T3 — backtest EQL sweep** | 30 case NDX lịch sử: EQL bị phá, ≥3 close dưới, excursion >3%, quay lại ≤3 phiên | ≥18/30 tiếp tục lên → rút hệ quả O1′; ≤12/30 → tiêu chí sweep cần filter độ sâu/số phiên | Phân xử fork O1′ |
| **T4 — chi phí của D1-gate** | Cùng 30 case: đo % quãng đường từ đáy sweep đến target đã đi xong tại thời điểm close D1 acceptance đầu tiên | median ≤25% → gate rẻ; ≥50% → gate đắt đo được | Định giá rule R1, đóng phần chi phí của O9 |

---

## 9. Bài học meta của phiên

1. **Hình vẽ là claim, không phải evidence.** Box "EQL" trên chart là trader *khẳng định* có pool; pool được xác lập bởi nến, không bởi box. Suốt phiên, mọi phán quyết đều tách price action / UI nền tảng / hình vẽ.
2. **Số platform-exact đảo phán quyết.** O7 chỉ đóng được khi có số thật: 28,160.6 vs 28,187 — chênh 26.4 pts, mắt thường trên chart W1 không phân giải nổi. "Ngay sát biên" và "trong biên" là hai thế giới.
3. **Outcome không phải evidence cho label.** "Giá quay lại rồi nên đó là sweep" và "giá chạy đúng nên phân tích đúng" cùng một lỗi — tại hard right edge, chỉ tiêu chí ex-ante đếm được.
4. **Concede bằng số là sức mạnh của cả hai phía.** Trader concede "chưa reclaim D1"; devil's advocate withdraw O4/O5/O9 khi evidence tới. Ledger ổn định số là thứ khiến 5 turn không quay vòng.
5. **Một thesis tốt lên không phải nhờ thắng cãi, mà nhờ trở nên falsifiable hơn.** Từ "đã reclaim, bias Bullish" (không kiểm được) đến "Bullish nếu acceptance > X, invalid nếu acceptance < 28,187, target pool có tên, gate D1, 3 test tiền đăng ký" — cùng một bias, khác hẳn phẩm chất.
6. **Doctrine gap phải được gọi tên, không được phán bừa.** Sweep-vs-acceptance là chỗ canon im lặng; tự chế chuẩn để FAIL người khác cũng là doctrine drift như tự nới chuẩn để cứu claim của mình.

---

## 10. Files của phiên

| File | Nội dung |
|---|---|
| `daily-bias/extraction_ustech100_d1_2026-08-03.json` | Extraction ICT-VISION (D1+H1+W1, confidence 0.75, M5 absent) |
| `daily-bias/devils-advocate-ustech100-2026-08-03.md` | Report debate đầy đủ 5 turn, ledger nguyên văn |
| `daily-bias/trading-rules.md` | Rule R1 (D1-gate) + 4 tham số còn thiếu |
| `daily-bias/assets/price-map.svg` | Sơ đồ giá D1 với toàn bộ mức đã đo |
| `daily-bias/assets/ledger-lifecycle.svg` | Vòng đời O1–O10 qua 5 turn |
| `daily-bias/assets/sweep-vs-acceptance.svg` | Case study CS1 |
| `daily-bias/assets/d1-gate-flow.svg` | Flow kiến trúc D1-gate + checklist O8 |
