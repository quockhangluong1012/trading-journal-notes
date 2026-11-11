---
type: mistake
category: management
severity: high
related_model: ICT 2022
frequency: 1
status: active
tags:
  - trading/ict/mistake
  - trading/review
  - trading/risk
created: 2026-10-13
updated: 2026-10-13
---

# Mistake - No Trade Management (lệnh có lời ≥ 2R quay về thua −1R)

> [!summary] Tóm tắt 1 câu
> Vào lệnh mà **không viết trước luật quản lý** (chốt ở đâu, khi nào dời SL, khi nào đóng theo thời gian, làm gì khi vắng mặt) — để rồi một lệnh đã đi được ≥ 2R quay ngược về chạm SL, biến một quyết định *có thể có lãi* thành −1R chỉ vì không ai (hoặc không luật nào) đứng ra đóng lệnh.

> [!danger] Nguyên tắc cốt lõi
> **Target là một lệnh, không phải một hy vọng.** Mỗi lệnh phải có, *trước khi bấm*: (1) TP đặt sẵn tại một mức thanh khoản thật, (2) luật quản lý đã chọn (`none_full_T1` hoặc `partial50_1R_BE` hoặc spec khác — viết ra), (3) giờ đóng lệnh bắt buộc, (4) quy tắc khi vắng mặt. Thiếu một trong bốn → lệnh phụ thuộc vào may rủi, không phụ thuộc vào quy trình.

---

## 1. Mô tả lỗi

Đây là lỗi ở **khâu sau entry** — tách biệt với chất lượng setup. Một setup tốt có thể thua vì lỗi này; một setup xấu có thể được "cứu" một phần nhờ quản lý tốt. Chính vì tách biệt, nó phải được log riêng, nếu không bạn sẽ đổ lỗi nhầm cho setup (hoặc ngược lại).

Các biến thể:

| Biến thể | Mô tả | Dấu hiệu trong log |
|---|---|---|
| **A — Không có kế hoạch thoát** | Chỉ có SL và một TP "ước lượng" (fib, số R đẹp), không có chốt một phần, không dời SL, không time-stop | `management:` trống; MFE ≥ 2R nhưng kết quả ≤ 0 |
| **B — Giữ lệnh khi vắng mặt** | Đi ngủ / rời máy khi lệnh còn rủi ro mở, SL chưa ở BE, TP đặt ở mức khó tới | Thời điểm chạm SL nằm ngoài giờ trực; ghi chú "đã đi ngủ" |
| **C — Giữ lệnh qua giờ chết** | Lệnh vào trong NY AM nhưng giữ qua NY lunch (11:30–13:00 NY, theo [[18-Kill-Zones]]) và phiên chiều, khi luận điểm AM đã hết thời gian | MFE đạt quanh cuối AM / đầu lunch, sau đó đảo |
| **D — TP không phải thanh khoản** | TP đặt theo fib/R mục tiêu, nằm sau (hoặc bên trong) một PD array đối nghịch → giá không bao giờ tới, lệnh không bao giờ được đóng có lãi | TP nằm trong FVG đối nghịch / sau PDH-PDL vừa bị phá — xem thêm [[05-Mistake-Not-enough-RR]] |

> [!note] Phân biệt với các mistake khác
> - [[05-Mistake-Not-enough-RR]] — lỗi **trước** entry: RR thật (đo tới thanh khoản không bị chặn) quá thấp. Biến thể D ở đây là *hậu quả quản lý* của cùng gốc: TP sai chỗ nên không bao giờ khớp.
> - [[01-Mistake-Emotional-revenge-trade]] / [[04-Mistake-FOMO-Entry]] — lỗi tâm lý khi vào. Note này là lỗi **thiết kế** sau khi vào: không có luật để thực thi.

---

## 2. Biểu hiện & Dấu hiệu nhận biết

| Câu hỏi tự kiểm tra (trước khi bấm) | Dấu hiệu lỗi | Dấu hiệu an toàn |
|---|---|---|
| TP đang nhắm pool thanh khoản nào? | "Fib 0.705", "3R cho đẹp" | Tên một mức cụ thể: ITH H1, PDH, đỉnh nến gốc nhịp, mép FVG đối nghịch |
| Giữa entry và TP có PD array đối nghịch nào? | Không kiểm tra | Liệt kê thang vật cản + R tới từng mức |
| Luật quản lý của lệnh này là gì? | "Để xem" | `none_full_T1` / `partial50_1R_BE` / spec khác — viết trước |
| Lệnh phải đóng lúc mấy giờ nếu chưa chạm TP/SL? | Không có | Ví dụ: 12:00 NY (23:00 VN khi EDT) |
| Tôi có ở trước màn hình tới giờ đó không? | Không chắc / sẽ đi ngủ | Có — hoặc lệnh đã có TP đặt sẵn và SL ≥ BE |
| Nếu lệnh đạt +2R rồi quay lại, tôi chấp nhận về −1R không? | Chưa nghĩ tới | Đã quyết định trước bằng luật |

---

## 3. Cơ chế — vì sao lỗi này đắt

1. **MFE là thông tin, không phải lợi nhuận.** Một lệnh đi được +2.5R rồi chạm SL cho thấy *hướng ngắn hạn* đúng một phần, nhưng kết quả ghi sổ chỉ có −1R. Không có luật quản lý = tự tay vứt đi toàn bộ phần thông tin đó.
2. **Lệnh ngược dòng chảy H1 có "tuổi thọ" ngắn.** `[INTERPRETATION]` Một nhịp hồi ngược order flow nội ngày thường chỉ đi tới EQ / vật cản đầu tiên của nhịp impulse rồi bị bán/mua lại. TP xa hơn mức đó cần một luận điểm khác (H1 MSS), không chỉ cần thời gian.
3. **Thời gian trong ngày.** `[ICT FRAMEWORK]` NY lunch (11:30–13:00 NY) là vùng chết — chuyển động AM hay dừng hoặc đảo. Một lệnh AM chưa tới TP khi vào lunch là lệnh mà luận điểm đã hết hạn.
4. **Vắng mặt biến quyết định thành xổ số.** Khi không có người và không có luật, kết quả chỉ còn phụ thuộc đường đi ngẫu nhiên của giá sau đó.
5. **Bẫy BE sớm (mặt ngược).** Dời BE quá sớm trên NDX cũng tốn: giá hay test lại vùng entry trước khi đi. Vì vậy "có quản lý" không có nghĩa là "dời BE càng sớm càng tốt" — phải chọn spec và **đo** bằng dữ liệu (xem §7).

---

## 4. Case thật

### Case 1 — [[Loss - 01 - Trade 2026-10-12 NDX Long]]

| Thông số | Giá trị |
|---|---|
| Entry / SL / TP | 30,664 / 30,627.9 / 30,796.3 (R = 36.1 điểm, planned RR 3.66) |
| MAE | 30,631 → −0.91R (SL còn cách 3.1 điểm) |
| MFE | 30,753 → **+2.47R** (~12:00 NY, đúng đầu NY lunch) |
| Kết quả | SL chạm ~14:45 NY (01:45 VN) → **−1R** · trả lại **3.47R** |
| Biến thể | A + B + C + D cùng lúc |
| Vật cản đầu tiên (biết trước lúc vào) | FVG giảm M15 30,706.5–30,722 → chỉ 1.18R |
| TP | Nằm **trong** FVG giảm 30,780–30,813 (do displacement mở cửa NY tạo ra) và trên PDL 30,763 đã bị phá |

Mô phỏng các luật quản lý *nếu đã viết trước* — **một đường giá duy nhất, có hindsight, chỉ để minh họa, không dùng để chọn luật**:

| Luật (giả định viết trước) | Kết quả |
|---|---|
| Như đã làm (không quản lý) | −1.00R |
| [[ICT 2022 Entry Checklist]]: 1R → chốt 50% + dời BE | +0.50R (phần còn lại bị quét BE ~11:15–11:30 NY) |
| Thoát hết tại mép FVG đối nghịch 30,705 | +1.14R |
| Thoát hết trước đỉnh nến gốc nhịp 10:00 (30,745) | +2.24R |
| Time-stop 12:00 NY (≈30,731) | +1.86R |
| 50% tại 30,705 + 50% tại 30,745, không BE | +1.69R |

---

## 5. Cách sửa (đưa vào Playbook)

1. **Rule MG-01 — TP là lệnh đặt sẵn.** Mỗi lệnh có TP order tại một mức thanh khoản có tên (không phải fib/R). TP đặt **trước** PD array đối nghịch đầu tiên, chốt sớm vài điểm (HEURISTIC: ~10–15% R hoặc 2 × spread).
2. **Rule MG-02 — Chọn một spec quản lý cho cả version.** `none_full_T1` (đo baseline) hoặc `partial50_1R_BE` (checklist hiện tại). Ghi vào frontmatter `management:`. Không đổi giữa chừng.
3. **Rule MG-03 — Time-stop.** Lệnh NY AM chưa tới TP/SL lúc **12:00 NY** → đóng (23:00 VN khi Mỹ dùng EDT; 00:00 VN khi Mỹ dùng EST từ 1/11).
4. **Rule MG-04 — Không để rủi ro mở khi vắng mặt.** Trước khi rời máy: hoặc đóng lệnh, hoặc SL ≥ BE và có spec runner viết sẵn.
5. **Rule MG-05 — Phân loại lệnh trước khi chọn TP.** Thuận dòng chảy H1 → T1 = ITH H1 đầu tiên, runner tới DOL. Ngược dòng chảy H1 → T1 = vật cản đầu tiên / EQ nhịp impulse, không runner.

---

## 6. Checklist (thêm vào [[ICT 2022 Entry Checklist]] mục quản lý)

- [ ] TP là một mức thanh khoản có tên, nằm trước PD array đối nghịch đầu tiên
- [ ] Đã liệt kê thang vật cản và R tới vật cản đầu tiên
- [ ] `management:` đã chọn và ghi vào note trước khi bấm
- [ ] Time-stop đã đặt (giờ NY)
- [ ] Tôi có mặt tới time-stop — hoặc lệnh tự quản lý được (TP đặt sẵn, SL ≥ BE)

---

## 7. Kiểm định (chống curve-fitting)

> [!warning] n = 1
> Một lệnh đủ để **ghi nhận lỗi quy trình** (không có luật quản lý là lỗi, bất kể kết quả). Nó **không** đủ để chọn luật quản lý nào tốt nhất — bảng §4 là hindsight trên một đường giá.

Field cần log cho **mọi** lệnh (thắng, thua, BE):

| Field | Ý nghĩa |
|---|---|
| `mfe_r` | Lãi tạm thời lớn nhất (theo R) |
| `mae_r` | Lỗ tạm thời lớn nhất (theo R) |
| `time_of_mfe` | Giờ NY đạt MFE |
| `management` | Spec quản lý đã dùng |
| `r_if_no_management` | Kết quả nếu giữ tới TP/SL |
| `first_obstacle_r` | R tới PD array đối nghịch đầu tiên tại lúc vào |

Sau 30–50 lệnh: so sánh `partial50_1R_BE` vs `none_full_T1` vs time-stop 12:00 NY (HYP-18, HYP-26 trong [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] / note Deep Research v0.2). Tín hiệu cần theo dõi: tỷ lệ lệnh có `mfe_r ≥ 2` nhưng `r_multiple ≤ 0` — nếu > 10–15% số lệnh, lỗi này đang là nguồn rò rỉ expectancy lớn.

---

## 8. Liên kết

- Mistakes: [[05-Mistake-Not-enough-RR]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[07-Mistake-Risk-more-than-0.5-total-account]]
- Concepts: [[18-Kill-Zones]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[13-FVG-Fair-Value-Gap]]
- Model: [[01 - ICT 2022 Model]] · [[13 - Intraday Profiles]]
- Playbook: [[ICT 2022 Entry Checklist]] · [[Daily Risk & Circuit Breaker Checklist]]
- Case: [[Loss - 01 - Trade 2026-10-12 NDX Long]]
