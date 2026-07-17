---
type: mistake
category: process
severity: high
related_model: ICT 2022
frequency: 1
status: active
tags:
  - trading/ict/mistake
  - trading/review
  - trading/backtest
created: 2026-07-17
updated: 2026-07-17
---

# Mistake - Log Data Mismatch - Backtest

> [!summary] Tóm tắt 1 câu
> Dữ liệu ghi trong một backtest note bị lệch nhau giữa các nguồn — frontmatter, bảng Backtest Summary, phần phân tích chi tiết, và filename — khiến chính bản thân sample đó không còn đáng tin cậy để tính expectancy, dù setup/entry logic có thể hoàn toàn đúng.

> [!danger] Nguyên tắc cốt lõi
> Một backtest chỉ có giá trị thống kê nếu **dữ liệu của nó tự nhất quán (internally consistent)**. Nếu frontmatter nói một giá, bảng summary nói giá khác, và phần narrative nói năm khác — thì con số `r_multiple` mà Dataview dashboard đang cộng vào expectancy tổng không phản ánh bất kỳ giao dịch thật nào đã xảy ra. Đây là lỗi **trước cả** câu hỏi "setup có đúng không" — nó là lỗi ở tầng ghi nhận sự thật.

---

## 1. Mô tả lỗi

Log Data Mismatch là việc một backtest note (hoặc trade note) chứa các giá trị **mâu thuẫn nhau giữa nhiều nơi trong cùng một file**, hoặc giữa file và tên file của chính nó. Đây không phải lỗi phân tích (đọc sai chart) hay lỗi thực thi (vào lệnh sai) — nó là lỗi **ghi nhận dữ liệu (data entry)**, xảy ra *sau khi* trade/backtest đã hoàn tất, trong lúc điền lại vào template.

Bốn dạng mismatch phổ biến nhất quan sát được trong vault này:

| # | Dạng mismatch | Ví dụ cụ thể |
|---|---|---|
| a | **Frontmatter vs Filename** | Filename ghi `2026-11-30`, nhưng `trade_date` trong frontmatter ghi `2016-11-30` |
| b | **Frontmatter vs bảng Backtest Summary (thân note)** | Frontmatter `take_profit: 1.05882`, nhưng bảng Summary trong thân note ghi `Take Profit \| 1.05886` |
| c | **Narrative vs chính nó (nội bộ thân note)** | Cùng một note, phần bias/context ghi `9/11/2016`, `24/7/2026`, `28/11/2016`, rồi entry sequence lại ghi `30/11/2026`, `12:15 30/11/2026` — năm 2016 và 2026 bị dùng lẫn lộn cho cùng một chuỗi sự kiện |
| d | **R-multiple không khớp với Entry/SL/TP đã log** | `r_planned`/`r_multiple` ghi sẵn một con số, nhưng tự tính lại từ `entry_price`, `stop_loss`, `take_profit` đã log ra risk/reward khác với con số đó |

Root causes phổ biến:

- Copy note cũ làm template cho note mới rồi quên sửa hết các trường ngày/giá (đặc biệt là năm — thói quen gõ năm hiện tại `2026` xen lẫn năm dữ liệu lịch sử `2016`/`2014` khi backtest dùng dữ liệu quá khứ).
- Điền frontmatter trước, viết narrative sau (hoặc ngược lại) ở hai thời điểm khác nhau, không đối chiếu lại.
- Tính R bằng nhẩm/ước lượng lúc mới chốt lệnh, sau đó sửa entry/SL/TP cho "chính xác hơn" nhưng không tính lại R.
- Dữ liệu backtest lấy từ nền tảng có timezone khác (ví dụ broker time hoặc UTC) rồi quy đổi tay sang UTC+7 không nhất quán giữa các dòng.

---

## 2. Biểu hiện & Dấu hiệu nhận biết

| Dấu hiệu | Mức độ cảnh báo |
|---|---|
| Năm trong `trade_date` (frontmatter) khác năm trong tên file | Đỏ |
| Giá trị entry/SL/TP trong bảng Summary khác với frontmatter (dù chỉ lệch vài pip) | Đỏ |
| Tự tính lại risk = \|entry − SL\|, reward = \|entry − TP\| ra R khác với `r_planned`/`r_multiple` đã log | Đỏ |
| Trong cùng một đoạn narrative, các mốc thời gian nhảy giữa hai năm khác nhau cho cùng một chuỗi sự kiện liên tục | Đỏ |
| `bias_correct` ghi Yes nhưng phần lesson learned lại mô tả bias sai (hoặc ngược lại) | Amber |
| Không nhớ được lý do vì sao một con số cụ thể được ghi, khi được hỏi lại | Amber |

Checklist nhận diện nhanh trước khi coi một backtest note là "hoàn tất":

- [ ] Năm trong filename, `trade_date`, và mọi mốc thời gian trong narrative có khớp nhau tuyệt đối không?
- [ ] `entry_price`, `stop_loss`, `take_profit` trong frontmatter có khớp 100% với bảng Backtest Summary trong thân note không?
- [ ] Tự tính lại risk/reward từ entry/SL/TP đã log — kết quả có khớp `r_planned`/`r_multiple` đã ghi không?
- [ ] `bias_correct` có nhất quán với nội dung phần lesson learned/phân tích không?

---

## 3. Cơ chế & Vì sao nguy hiểm

Khác với các mistake khác trong database này (đều là lỗi *tại thời điểm ra quyết định* trên chart), Log Data Mismatch là lỗi *hậu kỳ* — nó không làm hỏng một lệnh, nó **làm hỏng dữ liệu về lệnh đó**. Điều này nguy hiểm theo một cách âm thầm hơn nhiều:

1. **Dataview dashboard không biết dữ liệu sai** — `_Backtest Dashboard` và các dashboard khác trong `01 - Dashboard/` đọc thẳng frontmatter để tính win rate, average R, expectancy. Một `r_multiple` bị log sai (dù chỉ do gõ nhầm) sẽ **cộng thẳng vào** các con số tổng hợp mà không có cơ chế nào tự phát hiện — vì Dataview không biết "sự thật" của giao dịch, nó chỉ biết những gì được gõ vào.

2. **Vi phạm trực tiếp nguyên tắc "statistically valid backtest"** — mục tiêu của giai đoạn backtesting hiện tại là tích lũy một sample đủ lớn và **đáng tin** của ICT 2022 Model để nó có thể là căn cứ cho readiness gate (trước khi mua challenge FTMO/The5ers). Một sample chứa dữ liệu tự mâu thuẫn không đơn thuần là "1 mẫu bị nhiễu" — nó làm giảm độ tin cậy của toàn bộ kết luận rút ra từ dashboard, vì không ai (kể cả chính Khang) biết chính xác bao nhiêu note khác trong sample cũng có lỗi tương tự nhưng chưa bị phát hiện.

3. **Tạo điều kiện cho hindsight bias/curve-fitting mà không ai nhận ra** — nếu ngày tháng trong narrative bị lẫn lộn (ví dụ dùng nhầm năm hiện tại `2026` cho một chuỗi phân tích lẽ ra thuộc năm dữ liệu `2016`), rất khó xác minh sau này liệu entry trigger có thực sự "objectively identifiable trước khi biết kết quả" hay narrative đã bị viết lại một cách vô thức để khớp với kết quả đã biết. Đây chính là rủi ro curve-fitting/hindsight bias mà quy trình backtesting cần tránh — và data mismatch làm cho việc audit lại điều này gần như bất khả thi.

4. **Xói mòn lòng tin vào chính hệ thống journaling** — một khi phát hiện 1 file có mismatch, câu hỏi tự nhiên tiếp theo là "còn bao nhiêu file khác bị vậy mà mình chưa để ý?" — điều này làm giảm giá trị của toàn bộ vault như một nguồn sự thật (source of truth), đúng lúc nó cần đóng vai trò đó nhất (trước khi ra quyết định mua challenge).

---

## 4. Ví dụ minh họa

### ❌ Sai — ví dụ có thật trong vault

File: `04 - Backtesting/2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short.md`

Đây là ví dụ **thật, đã tồn tại trong vault**, không phải dựng lại — được phát hiện khi soạn note này:

- **Filename** ghi ngày `2026-11-30`.
- **Frontmatter** `trade_date: 2016-11-30` — khác năm với filename.
- **Bảng Backtest Summary** trong thân note ghi `Take Profit | 1.05886`, trong khi **frontmatter** `take_profit: 1.05882` — lệch 4 điểm giá ở vị trí cuối.
- **Phần narrative** (HTF Context, Entry Sequence) dùng lẫn lộn cả hai năm cho cùng một chuỗi sự kiện liên tục: "24/7/2026", "9/11/2026", "28/11/2016", "30/11/2026", "12:15 30/11/2026" — không thể xác định chắc chắn năm nào là đúng chỉ bằng cách đọc lại note.
- Risk/reward tự tính lại từ entry/SL/TP đã log (entry 1.06434, SL 1.06668, TP 1.05882/1.05886) cũng không khớp gọn với "Risk (points)" và "Reward (points)" đã ghi sẵn trong bảng Summary.

**Vì sao đây là ví dụ chuẩn của lỗi này:** setup logic được mô tả (Sweep → Displacement → MSS → FVG → entry) hoàn toàn có thể đúng — vấn đề không nằm ở đọc chart. Vấn đề là **không thể xác nhận chắc chắn giao dịch này thực sự xảy ra khi nào**, và con số TP dùng để tính R trong dashboard là con số nào trong hai con số đã log. File này cần được đối chiếu lại với dữ liệu gốc (chart/lịch sử giá) và sửa cho nhất quán trước khi được tính là một mẫu hợp lệ trong sample thống kê.

> [!warning] Chưa chỉnh sửa
> Note này chưa được sửa — theo house rule "không tự ý sửa dữ liệu trade/backtest", cần xác nhận lại với Khang giá trị nào đúng (entry/SL/TP thật, và năm giao dịch thật là 2016) trước khi cập nhật file.

### ✅ Đúng — quy trình chuẩn

Sau khi hoàn tất một backtest, trước khi đóng file:

1. Điền frontmatter trước, dựa trực tiếp trên chart/lịch sử giá — không gõ lại từ trí nhớ.
2. Copy nguyên giá trị (không gõ lại tay lần hai) từ frontmatter sang bảng Backtest Summary trong thân note.
3. Tự tính risk = |entry − SL|, reward = |entry − TP|, R = reward / risk → so với `r_planned` đã log. Nếu lệch, sửa lại cho khớp — không giữ cả hai con số khác nhau.
4. Đọc lại toàn bộ narrative một lượt chỉ để kiểm tra **ngày tháng** — đặc biệt khi backtest dùng dữ liệu lịch sử (năm dữ liệu ≠ năm hiện tại), đây là nơi dễ gõ nhầm nhất.

---

## 5. Kiến thức nâng cao (Advanced)

### 5.1. Bốn nguồn sự thật trong một backtest note — và vì sao chúng phải khớp tuyệt đối

Một backtest note trong vault này có **bốn nơi** có thể chứa cùng một thông tin: filename, frontmatter (Dataview đọc ở đây), bảng Backtest Summary (mục 0, con người đọc ở đây), và narrative chi tiết (mục 1-4). Thiết kế template vốn dĩ **trùng lặp có chủ đích** để dễ đọc — nhưng trùng lặp có chủ đích chỉ an toàn nếu có kỷ luật đồng bộ. Nếu không, trùng lặp trở thành bốn cơ hội để dữ liệu rẽ nhánh thành bốn phiên bản khác nhau của "sự thật".

### 5.2. R-multiple là con số dẫn xuất, không phải con số tự do

`r_multiple` và `r_planned` không nên được gõ như một con số độc lập — chúng là **hàm số** của `entry_price`, `stop_loss`, `take_profit`:

```
risk   = |entry_price − stop_loss|
reward = |entry_price − take_profit|
R      = reward / risk
```

Nếu ba giá trị gốc (entry/SL/TP) đã được log, R không cần "nhớ lại" hay "ước lượng" — nó cần được **tính ra**. Bất kỳ lúc nào R được gõ tay mà không tính lại từ ba giá trị gốc, đó là một điểm rủi ro mismatch tiềm ẩn. Xem thêm [[05 - Mistake - Not enough RR]] về cách đo RR đúng chuẩn tới draw on liquidity — nguyên tắc "RR phải là con số đo được, không phải con số tự chọn" áp dụng ở cả hai lỗi, nhưng ở đây vấn đề là RR *bị log sai* chứ không phải RR *bị chọn thấp*.

### 5.3. Lỗi năm khi backtest dữ liệu lịch sử — pattern rất riêng của backtesting

Trade log thật (05 - Live Trading Journal) không có rủi ro này vì luôn là ngày hiện tại. Nhưng **backtest** (04 - Backtesting) luôn có hai "năm" khác nhau tồn tại song song trong cùng một note:

- **`backtest_date`** — ngày Khang *thực hiện* việc backtest (ví dụ hôm nay, 2026).
- **`trade_date`** — ngày dữ liệu giá *thuộc về* (ví dụ 2014, 2016 — dữ liệu lịch sử dùng để replay).

Vì `backtest_date` luôn mang năm hiện tại (2026) và tay đã quen gõ năm đó, rất dễ vô thức "kéo" năm 2026 vào phần narrative lẽ ra phải thuộc `trade_date` (2016) — chính xác là lỗi đã xảy ra ở ví dụ mục 4. Quy tắc phòng tránh: **luôn viết narrative bằng ngày-tháng-không-năm trước** (ví dụ "30/11"), rồi mới thêm năm của `trade_date` vào một lần duy nhất, thay vì gõ năm lặp lại ở từng dòng.

### 5.4. Vì sao lỗi này khó tự phát hiện hơn các mistake khác

Tất cả các mistake khác trong database (bias sai, RR thấp, entry sớm...) đều để lại **dấu vết trên P&L** — thua lỗ là tín hiệu cảnh báo tự nhiên khiến trader quay lại xem xét. Log Data Mismatch **không** để lại dấu vết như vậy: một lệnh có thể thắng (`result: Win`), grade cao, và vẫn chứa dữ liệu sai hoàn toàn — như chính ví dụ mục 4 (`result: Win`, R = 2.09, grade C+). Đây là lý do lỗi này cần một cơ chế phát hiện **chủ động** (checklist đối chiếu, không phải "chờ thấy dấu hiệu"), khác với các mistake khác vốn có thể nhận biết qua biểu hiện hành vi khi giao dịch.

### 5.5. Ngưỡng chấp nhận một backtest vào sample thống kê

Trước khi một backtest note được tính là 1 mẫu hợp lệ trong sample dùng để đánh giá readiness (theo mục 6 "Readiness gate" của quy tắc dự án), nó nên vượt qua một bộ lọc tối thiểu:

- [ ] Không có mismatch giữa filename/frontmatter/bảng Summary/narrative (mục 1-2).
- [ ] R-multiple khớp với công thức tính từ entry/SL/TP đã log (mục 5.2).
- [ ] Entry trigger được mô tả theo trình tự thời gian nhất quán, có thể audit lại được (mục 5.4 + nguyên tắc chống hindsight bias).

Một mẫu không qua được bộ lọc này nên được đánh dấu tạm hoãn (không xoá) cho đến khi được đối chiếu và sửa, thay vì để nguyên trong dashboard như một mẫu "sạch".

---

## 6. Best Practices

> [!success] Thực hành cụ thể
> 1. Điền frontmatter trước tiên, trực tiếp từ chart — không gõ lại từ trí nhớ sau khi đã viết narrative.
> 2. Copy giá trị từ frontmatter sang bảng Backtest Summary, không gõ tay lần hai.
> 3. Sau khi log xong entry/SL/TP, luôn tự tính lại R = reward/risk và so với `r_planned`/`r_multiple` — sửa nếu lệch, không giữ song song hai con số.
> 4. Với backtest dữ liệu lịch sử: viết narrative bằng ngày-tháng trước, thêm năm của `trade_date` sau, một lần duy nhất; tránh gõ năm lặp lại thủ công ở từng dòng.
> 5. Đọc lại toàn bộ note một lượt riêng chỉ để rà ngày-tháng và số liệu — tách biệt với lượt đọc để rà logic setup.
> 6. Định kỳ (cuối mỗi tuần review) chọn ngẫu nhiên 1-2 backtest note cũ để đối chiếu lại 4 nguồn dữ liệu — audit ngẫu nhiên, không chỉ audit note mới.
> 7. Không tự ý sửa số liệu của người khác/note cũ mà không xác nhận lại giá trị đúng — theo house rule vault, chỉ đề xuất sửa và xin xác nhận.

---

## 7. Rule phòng tránh & Checklist

Checklist bắt buộc trước khi coi một backtest/trade note là "hoàn tất" và tính vào sample:

- [ ] Năm trong filename khớp tuyệt đối với `trade_date` trong frontmatter?
- [ ] `entry_price`, `stop_loss`, `take_profit` trong frontmatter khớp 100% với bảng Backtest Summary?
- [ ] Tự tính risk = |entry − SL|, reward = |entry − TP|, R = reward/risk — có khớp `r_planned`/`r_multiple` đã log không?
- [ ] Toàn bộ mốc thời gian trong narrative dùng nhất quán một năm (năm của `trade_date`, không lẫn năm của `backtest_date`)?
- [ ] `bias_correct` có nhất quán với nội dung lesson learned không?
- [ ] Nếu phát hiện mismatch ở note cũ — đã dừng lại để xác nhận giá trị đúng với Khang trước khi sửa, thay vì tự ý ghi đè?

---

## 8. Ví dụ đã xảy ra

- [[04 - Backtesting/2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short|02 - Win - EURUSD - 2026-11-30 - Short]] — mismatch năm (`trade_date: 2016-11-30` vs filename `2026-11-30`, và năm 2016/2026 lẫn lộn trong narrative) + mismatch giá TP (frontmatter `1.05882` vs bảng Summary `1.05886`). **Chưa được sửa** — cần Khang xác nhận giá trị đúng trước khi cập nhật.

*(Thêm các mismatch khác phát hiện được vào danh sách này theo định dạng `[[đường dẫn note|tên hiển thị]] — mô tả ngắn loại mismatch`.)*

---

## 9. Flashcards / Active Recall

**Q1:** Log Data Mismatch khác với các mistake khác trong database (bias sai, RR thấp, entry sớm...) ở điểm cốt lõi nào?
**A1:** Các mistake khác là lỗi *tại thời điểm ra quyết định* trên chart và thường để lại dấu vết qua P&L thua lỗ. Log Data Mismatch là lỗi *hậu kỳ*, xảy ra khi ghi lại dữ liệu, và có thể tồn tại ngay cả trên một lệnh thắng — không có dấu hiệu tự nhiên nào cảnh báo.

**Q2:** Bốn nơi trong một backtest note có thể chứa cùng một dữ liệu, và vì sao chúng phải khớp nhau?
**A2:** Filename, frontmatter, bảng Backtest Summary, và narrative chi tiết. Chúng phải khớp vì frontmatter là nơi Dataview đọc để tính thống kê, còn ba nơi còn lại là nơi con người đọc để hiểu bối cảnh — nếu lệch nhau, không rõ phiên bản nào là "sự thật".

**Q3:** R-multiple nên được xử lý như một con số tự do hay một con số dẫn xuất? Vì sao?
**A3:** Là con số dẫn xuất — R = |entry−TP| / |entry−SL|. Nếu entry/SL/TP đã được log, R cần được tính ra, không nên gõ tay/ước lượng, vì gõ tay là điểm rủi ro mismatch.

**Q4:** Vì sao backtest dữ liệu lịch sử dễ bị lỗi nhầm năm hơn trade log thật?
**A4:** Vì mỗi backtest note có hai năm song song: `backtest_date` (năm hiện tại, năm thực hiện việc backtest) và `trade_date` (năm dữ liệu lịch sử). Tay quen gõ năm hiện tại nên dễ vô thức lẫn vào phần narrative lẽ ra thuộc năm dữ liệu.

**Q5:** Vì sao một sample backtest chứa dữ liệu mismatch lại nguy hiểm hơn "chỉ 1 mẫu bị nhiễu"?
**A5:** Vì nó làm giảm độ tin cậy của toàn bộ kết luận rút ra từ dashboard (win rate, expectancy dùng cho readiness gate), và làm cho việc audit lại tính hindsight-bias-free của mọi mẫu khác trở nên khó khăn hơn — không biết còn bao nhiêu mismatch chưa bị phát hiện.

---

## 10. Lesson Learned

**Bài học chính:**
- Một backtest/trade note có bốn nơi có thể chứa cùng dữ liệu (filename, frontmatter, bảng Summary, narrative) — trùng lặp này chỉ an toàn nếu có kỷ luật đồng bộ, nếu không nó là bốn cơ hội để dữ liệu rẽ nhánh.
- R-multiple là con số dẫn xuất từ entry/SL/TP, không phải con số tự do — luôn tính lại, không gõ tay.
- Backtest dữ liệu lịch sử có rủi ro nhầm năm riêng biệt (năm backtest vs năm dữ liệu) mà trade log thật không có.
- Lỗi này không để lại dấu vết qua P&L — cần checklist chủ động, không thể chờ "cảm thấy có gì sai".

**Quy tắc cá nhân:**
- [ ] Luôn tự tính lại R từ entry/SL/TP đã log, không giữ song song hai con số khác nhau.
- [ ] Rà lại ngày-tháng-năm trong narrative như một bước riêng, tách biệt với rà logic setup.
- [ ] Không tự sửa dữ liệu note cũ khi phát hiện mismatch — xác nhận giá trị đúng trước.
- [ ] Định kỳ audit ngẫu nhiên các note cũ, không chỉ note mới nhất.

> Một backtest sai vì đọc sai chart vẫn là dữ liệu thật, chỉ là bài học đắt. Một backtest đúng chart nhưng log sai dữ liệu không phải là dữ liệu — nó là tiếng ồn mặc áo thống kê, và tiếng ồn đó sẽ len vào chính con số quyết định liệu Khang đã sẵn sàng mua challenge hay chưa.

---

## 11. Liên kết

**Mistakes liên quan:** [[05 - Mistake - Not enough RR]] · [[09 - Mistake - Wrong daily bias]]

**Dashboard:** [[04 - Backtesting/_Backtest Dashboard|_Backtest Dashboard]] · [[01 - Dashboard/02 - Mistake Frequency Dashboard|Mistake Frequency Dashboard]]

**Template:** [[08 - Templates/Backtest templete|Backtest templete]]
