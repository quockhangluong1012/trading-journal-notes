---
type: dashboard
scope: toan-vault-22-lenh
created: 2026-08-03
sources:
  - "[[../../analysis_summaries/aggregate_stats.md]]"
tags: [dashboard, backtest, statistics, ict2022]
---

# Dashboard & Statistics — Toàn bộ 22 lệnh backtest ICT 2022

> [!info] Nguồn số liệu
> Toàn bộ bảng và số dưới đây lấy nguyên văn từ `analysis_summaries/aggregate_stats.md` (tính từ frontmatter của 22 note) và đối chiếu chéo với `batchA.md` → `batchE.md`. Không suy diễn thêm số nào ngoài các file đó. Đây là dashboard **tổng hợp cấp vault**, không thay thế `_Backtest Dashboard`/`_POI Analytics Dashboard` nếu các file đó tồn tại — kiểm tra không thấy tồn tại trong vault tại thời điểm viết (2026-08-03), nên không có xung đột append-only.

## 1. Bảng đầy đủ 22 lệnh

| # | File | Symbol | Pos | Result | POI | Entry | Confl | R | Grade | 1st error | Session |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [[2026-07-01/01 - Win - EURUSD - 2010-10-19 - Long]] | EURUSD | Long | Win | OB | None | None | 1.53 | A | None | London |
| 2 | [[2026-07-06/01 - Win - EURUSD - 2005-04-12 - Short]] | EURUSD | Short | Win | OB | None | None | 2.1 | A | None | New York |
| 3 | [[2026-07-06/02 - Win - EURUSD - 2005-04-13 - Short]] | EURUSD | Short | Win | OB | None | None | 2.78 | A | None | New York |
| 4 | [[2026-07-07/02 - Win - EURUSD - 2005-04-24 - Long]] | EURUSD | Long | Win | Unicorn Model | None | None | 2.23 | A | None | New York |
| 5 | [[2026-07-07/02 - Win - EURUSD - 2005-04-27 - Long]] | EURUSD | Long | Win | IFVG | None | None | 2.48 | A | None | London |
| 6 | [[2026-07-08/01 - Loss- EURUSD - 2005-05-02 - Long]] | EURUSD | Long | Loss | Order Block | Edge | 0 | -1 | D | displacement | London |
| 7 | [[2026-07-09/01 - Win - EURUSD - 2005-05-11- Short]] | EURUSD | Short | Win | FVG | CE | 0 | 2.85 | A | none | New York AM |
| 8 | [[2026-07-10/01 - Win - EURUSD - 2021-05-03- Short]] | EURUSD | Short | Win | Unicorn | CE | 1 | 3.075 | A | none | New York AM |
| 9 | [[2026-07-10/02 - Loss- EURUSD - 2021-05-07- Short]] | EURUSD | Short | Loss | Order Block | CE | 0 | -1 | C | draw | Asia |
| 10 | [[2026-07-10/03 - Win - EURUSD - 2021-07-22- Long]] | EURUSD | Long | Win | FVG | CE | 0 | 2.86 | B | none | New York AM |
| 11 | [[2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]] | EURUSD | Long | Win | FVG | Edge | 1 | 3.18 | A | entry | None |
| 12 | [[2026-07-12/01 - Win - GBPUSD- 2024-12-04- Long]] | GBPUSD | Long | Win | Order Block | Edge | 2 | 3.4 | B | entry | None |
| 13 | [[2026-07-13/01 - Win - NAS100 - 2026-04-02- Long]] | NAS100 | Long | Win | FVG | CE | 1 | 2.89 | A | none | New York AM |
| 14 | [[2026-07-14/01 - Win - XAUUSD- 2014-05-12- Short]] | XAUUSD | Short | Win | FVG | CE | 2 | 2.9 | A- | none | New York AM |
| 15 | [[2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short]] | XAUUSD | Short | Loss | Rejection Block | CE | 2 | -1 | B- | poi | London |
| 16 | [[2026-07-14/03 - Win - XAUUSD- 2014-05-14 - Short]] | XAUUSD | Short | Win | FVG | CE | 2 | 2.97 | A | none | New York |
| 17 | [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short]] | XAUUSD | Short | Loss | Breaker Block | CE | 3 | -1 | C+ | poi | London |
| 18 | [[2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short]] | EURUSD | Short | Win | FVG | CE | 2 | 2.09 | C+ | none | London |
| 19 | [[2026-07-16/01 - Win - EURUSD - 2016-06-12 - Short]] | EURUSD | Short | Win | Order Block | CE | 2 | 2.49 | B+ | none | London |
| 20 | [[2026-07-16/02 - Win - GBPUSD - 2014-06-25 - Long]] | GBPUSD | Long | Win | Order Block | CE | 1 | None | B+ | none | London Open KZ |
| 21 | [[2026-07-17/01 - Win - GBPUSD - 2014-06-25 - Long]] | GBPUSD | Long | Win | FVG | CE | 3 | 2.33 | B | 6 | New York (sau NY Open KZ) |
| 22 | [[2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] | GBPUSD | Long | Loss | FVG | CE | 1 | -1 | C | sweep | New York AM |

> [!warning] Lưu ý hàng #20 và #21
> Hai note trùng tên hiển thị "GBPUSD - 2014-06-25 - Long" nhưng theo `batchE.md`, hàng #21 (`2026-07-17/01`) có `trade_date` thật ghi trong frontmatter là **2014-07-14**, không phải 2014-06-25 như tên file. Đây là **hai lệnh khác nhau** bị trùng tên file do lỗi đặt tên chưa sửa — không phải cùng một lệnh backtest hai lần. Bảng trên giữ nguyên tên file gốc (append-only, không đổi tên file), chỉ cảnh báo tại đây.

## 2. Key numbers (nguyên văn từ aggregate_stats.md, đã verify lại bằng Python)

- **22 lệnh: 17 Win / 5 Loss = WR 77.3%** — verify: 17/22 = 77.27% ✅. *(Diễn giải bên dưới: con số này [UNSUPPORTED] ở cấp toàn sample — xem [[01 - Cross-Setup Devils Advocate (BACKTEST mode)]]).*
- **Tổng R = +37.16R trên 21 lệnh có số** — verify bằng Python: tổng 21 giá trị R = **37.155**, làm tròn khớp +37.16R ✅ (lệnh #20 không có `r_multiple` nên loại khỏi tổng, đúng như note gốc).
- **avg +1.77R/lệnh** — verify: 37.155/21 = 1.7693 ✅.
- **avg win +2.63R** — verify: tổng 16 lệnh Win có số / 16 = 2.6347 ✅ (16, không phải 17, vì lệnh #20 thiếu R).
- **loss luôn -1R** — verify: cả 5 Loss đều ghi đúng -1 ✅ (kỷ luật cắt lỗ đồng nhất, không có lệnh nào gồng lỗ).
- **Symbol**: EURUSD 11W/2L, GBPUSD 3W/1L, XAUUSD 2W/2L, NAS100 1W/0L — verify đếm tay khớp bảng mục 1 ✅.
- **POI paradox**: FVG 8W/1L, OB 6W/2L, nhưng POI hạng cao Breaker 0W/1L, Rejection Block 0W/1L, Unicorn 2W/0L → thang POI rank **chưa được data ủng hộ**.
- **Confluence score KHÔNG tách được Win/Loss**: Loss xuất hiện ở mọi mức 0, 1, 2, 3; Loss có confluence cao nhất (3) chính là XAUUSD 19/5 (Breaker Block, [[2026-07-15/01 - Loss - XAUUSD - 2014-05-19 - Short]]).
- **Entry**: CE 10W/4L, Edge 2W/1L → 2 lệnh Edge-entry Win ([[2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]], [[2026-07-12/01 - Win - GBPUSD- 2024-12-04- Long]]) là "thắng dù sai" (`first_error_step: entry`).
- **first_error 5 lệnh Loss**: displacement (05-02), draw (2021-05-07), poi (XAU 14/5), poi (XAU 19/5), sweep (GBP 17/7) — 5 nhãn bề mặt khác nhau, nhưng [[2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] mục 9.3 đã gộp cả 4 lệnh gần nhất (không tính 05-02) thành họ "Unswept Liquidity Path".
- **Session**: London 7, NY AM 6, NY 4, Asia 1 (lệnh Asia = Loss duy nhất tại Asia, [[2026-07-10/02 - Loss- EURUSD - 2021-05-07- Short]]).
- **5 note đầu (07-01 → 07-07) thiếu field mới** (`entry_type`, `confluence_score`, `first_error_step`) → schema drift giữa đầu và cuối sample.

## 3. Diễn giải: cái gì data ủng hộ, cái gì chưa

### 3.1. Được data ủng hộ (ở mức "quan sát nhất quán trong mẫu này", KHÔNG phải "đã kiểm định thống kê")

- **Kỷ luật cắt lỗ**: cả 5/5 Loss đều đúng -1R, không có lệnh nào gồng/dời SL. Đây là quan sát trực tiếp từ số ghi, không cần suy luận thêm.
- **CE-entry chiếm đa số outcome tốt về mặt tần suất** (10W/4L trong số các lệnh có ghi `entry_type`), nhưng xem mục 3.2 — không nên đọc thành "CE tốt hơn Edge" vì n Edge quá nhỏ (3 lệnh).
- **FVG là POI xuất hiện nhiều nhất và có tỷ lệ Win cao nhất về số tuyệt đối** (8W/1L) — nhất quán với việc FVG là khái niệm đơn giản nhất, ít bước xác nhận nhất nên ít chỗ để log sai (xem thêm [[../Case Studies/CS-03 - Nghich ly POI rank|CS-03]]).

### 3.2. CHƯA được data ủng hộ (n quá nhỏ hoặc thiếu nhóm đối chứng)

- **WR 77.3%** — [UNSUPPORTED] ở cấp toàn sample nếu không chứng minh được provenance: không có ghi chép nào trong vault về các setup **đạt tiêu chí nhưng không được backtest / bị bỏ qua**. Nếu 22 lệnh này được chọn (có ý thức hoặc vô thức) vì chúng có sẵn ảnh chụp màn hình đẹp, hoặc vì trader nhớ rõ các lệnh thắng hơn lệnh thua, WR không đại diện cho hiệu suất hệ thống. Chi tiết đầy đủ ở [[01 - Cross-Setup Devils Advocate (BACKTEST mode)]] mục Cross-setup.
- **POI rank cao (Breaker, Rejection Block) có vẻ thua nhiều hơn** — n=1 mỗi loại, không đủ để kết luận nhân quả "khái niệm cao cấp kém tin cậy hơn". `batchD.md` chỉ ra khả năng thay thế: cả hai lệnh Loss này đều **thiếu chuỗi sự kiện bắt buộc theo canon** khi gán nhãn (RB cần OB-thất-bại-trước; Breaker cần đủ 3 mắt xích) — tức có thể là lỗi *quy trình nhận diện nhãn*, không phải bản chất khái niệm kém hơn. Xem [[../Case Studies/CS-03 - Nghich ly POI rank|CS-03]].
- **Edge-entry "thắng dù sai" (n=2)** — không đủ để kết luận Edge-entry là một edge riêng biệt; cả hai note tự đề xuất Grade tối đa = B cho tới khi có ≥20 mẫu Edge-entry. Xem [[../Case Studies/CS-02 - Edge entry vs CE entry|CS-02]].
- **Confluence score không tách Win/Loss** — với n=22 và chỉ 5 Loss trải đều trên 4 mức điểm (0-3), không đủ mẫu để nói "confluence score vô dụng"; nhưng cũng không có bằng chứng ngược lại rằng nó có giá trị dự báo — đúng nghĩa "không kết luận được theo cả hai chiều" với mẫu này.
- **Session**: NY AM/London chiếm đa số Win chỉ vì đây là session được backtest nhiều nhất (13/22 lệnh), không phải bằng chứng bản thân các session này có edge cao hơn Asia (n=1, không so sánh được).

## 4. Schema drift giữa note đầu và note cuối vault

| Đặc điểm | Note đầu (07-01 → 07-07, 5 note) | Note cuối (07-14 → 07-17) |
|---|---|---|
| Field `entry_type` | Không có (`None`) | Có, ghi rõ CE/Edge/Between |
| Field `confluence_score` | Không có (`None`) | Có, thang 0-8 |
| Field `first_error_step` | Không có (`None`) | Có, tên bước cụ thể |
| POI type ghi trong frontmatter | Tên tự do (`Unicorn Model`, `IFVG`) | Controlled vocabulary hơn nhưng vẫn có ngoại lệ (BPR phải "ép" về `FVG`, xem [[2026-07-14/03 - Win - XAUUSD- 2014-05-14 - Short]]) |
| MSS/displacement | Mô tả bằng lời, không kèm giá đóng nến cụ thể (theo `batchA.md`, cả 5/5 note đầu) | Có số cụ thể hơn (fvg_high/low, ce_price), dù vẫn còn note thiếu (`2026-07-11`, BPR bounds bị lỗi đánh máy) |
| Template | Template cũ (theo ghi chú chuyển đổi trong `2026-07-14/01`, `2026-07-14/02`, `2026-07-14/03`) | Backtest template - POI & Step Decision (mới) |

**Hệ quả thống kê trực tiếp**: mọi con số tổng hợp theo `entry_type`/`confluence_score`/`first_error_step` ở mục 2 chỉ tính được trên **17 lệnh** (07-08 trở về sau), không phải 22 — 5 note đầu không có dữ liệu để đưa vào các phép đếm này. Đây không phải lỗi tính toán của `aggregate_stats.md` (file đó đã ghi `None` đúng chỗ, không suy diễn) mà là giới hạn cấu trúc của dữ liệu nguồn.

## 5. Danh sách lỗi arithmetic đã phát hiện (theo file)

| # | File | Lỗi | Nguồn phát hiện |
|---|---|---|---|
| 1 | [[2026-07-01/01 - Win - EURUSD - 2010-10-19 - Long]] | Dealing Range H1 ghi "High 1.14594, Low 1.38319" — High < Low, bất khả thi vật lý | `batchA.md` mục 1 |
| 2 | [[2026-07-07/02 - Win - EURUSD - 2005-04-24 - Long]] | Unicorn overlap ghi 1.29433–1.29498, tính lại bằng max(low)-min(high) từ breaker (1.29357–1.29480) ∩ FVG (1.29426–1.29595) = 1.29426–1.29480 — cạnh trên lệch 1.8 pip ra ngoài vùng giao thực | `batchA.md` mục 4 |
| 3 | [[2026-07-06/02 - Win - EURUSD - 2005-04-13 - Short]] | CE FVG H1 tính lại = 1.29532, không đối chiếu được trực tiếp trong note (minor) | `batchA.md` mục 3 |
| 4 | [[2026-07-08/01 - Loss- EURUSD - 2005-05-02 - Long]] | RR ghi 2.76 vs tính lại 2.692 | `batchB.md` mục 1 |
| 5 | [[2026-07-09/01 - Win - EURUSD - 2005-05-11- Short]] | CE tính lại 1.28886 lệch 14.8 pip so với `ce_price` ghi (1.29034) | `batchB.md` mục 2 |
| 6 | [[2026-07-10/01 - Win - EURUSD - 2021-05-03- Short]] | `r_multiple` ghi 3.075 vs RR tính trực tiếp entry/SL/TP = 2.123 — chênh ~1R, nghi là số blended qua partial nhưng không minh bạch TP1/%KL | `batchB.md` mục 3 |
| 7 | [[2026-07-10/02 - Loss- EURUSD - 2021-05-07- Short]] | RR tính lại 3.365 khớp gần đúng với 3.39 ghi trong note (chênh không đáng kể, gần PASS) | `batchB.md` mục 4 |
| 8 | [[2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short]] | `r_planned: 2.09` trong frontmatter không khớp RR tính lại từ entry/SL/TP (≈2.34–2.36 tùy TP nào trong 2 giá trị mâu thuẫn đã biết) — note gốc đã tự bắt 2 mâu thuẫn khác (CE/Edge, TP 1.05882/1.05886) nhưng bỏ sót lỗi này | `batchD.md` Note 5 |
| 9 | [[2026-07-16/02 - Win - GBPUSD - 2014-06-25 - Long]] | `r_planned: 2.47` không khớp khi tính lại từ entry/SL/TP1 = 2.373 (lệch ~0.1R/4%); nguyên nhân gốc: SL 1.6938 được back-calculate NGƯỢC từ RR mục tiêu 2.47 — vòng lặp tự tham chiếu | `batchE.md` mục 2 |
| 10 | [[2026-07-17/01 - Win - GBPUSD - 2014-06-25 - Long]] | Note tự phát hiện và sửa lỗi 6 pip trong CE/EQ mà bản gốc ghi tay bỏ lỡ (self-correction, không phải lỗi còn tồn) | `batchE.md` mục 3 |
| 11 | [[2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] | CE FVG H1 = 1.70988 (đúng công thức) nhưng note ghi CE 1.70990 — lệch ~0.2 pip (minor, đã ghi trong note gốc mục 0) | Note gốc, mục 0 "Kiểm tra lại các con số" |
| 12 | [[2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]] | Bounds BPR bị lỗi đánh máy trong note gốc ("1.34237 - 1.34-96") khiến không tính được CE thật — không phải lỗi arithmetic có thể verify, mà là dữ liệu nguồn không đọc được | `batchC.md` mục 1 |

**Tổng kết mục 5**: 12 điểm bất thường số học được ghi nhận qua 5 batch, trải trên 10/22 note (một số note có nhiều hơn 1 điểm). Không có điểm nào bị xác nhận là gian lận có chủ đích — toàn bộ đọc như lỗi ghi chép tay (typo, làm tròn, hoặc số blended qua partial TP không minh bạch nguồn).

## Liên kết

- [[01 - Cross-Setup Devils Advocate (BACKTEST mode)]]
- [[02 - Master Lesson Learned]]
- [[../Case Studies/CS-01 - Ho loi Trading Into Unswept Liquidity|CS-01]] · [[../Case Studies/CS-02 - Edge entry vs CE entry|CS-02]] · [[../Case Studies/CS-03 - Nghich ly POI rank|CS-03]] · [[../Case Studies/CS-04 - MSS som va sweep 2 chuan|CS-04]] · [[../Case Studies/CS-05 - Outcome bias va hindsight|CS-05]]
- Nguồn: `analysis_summaries/aggregate_stats.md`, `analysis_summaries/batchA.md` → `batchE.md`
