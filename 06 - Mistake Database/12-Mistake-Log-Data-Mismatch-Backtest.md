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
updated: 2026-08-02
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

2. **Vi phạm trực tiếp nguyên tắc "statistically valid backtest"** — mục tiêu của giai đoạn backtesting hiện tại là tích lũy một sample đủ lớn và **đáng tin** của ICT 2022 Model để nó có thể là căn cứ cho readiness gate (trước khi mua challenge FTMO/The5ers). Một sample chứa dữ liệu tự mâu thuẫn không đơn thuần là "1 mẫu bị nhiễu" — nó làm giảm độ tin cậy của toàn bộ kết luận rút ra từ dashboard, vì không ai (kể cả chính ) biết chính xác bao nhiêu note khác trong sample cũng có lỗi tương tự nhưng chưa bị phát hiện.

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
> Note này chưa được sửa — theo house rule "không tự ý sửa dữ liệu trade/backtest", cần xác nhận lại với  giá trị nào đúng (entry/SL/TP thật, và năm giao dịch thật là 2016) trước khi cập nhật file.

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

- **`backtest_date`** — ngày  *thực hiện* việc backtest (ví dụ hôm nay, 2026).
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
- [ ] Nếu phát hiện mismatch ở note cũ — đã dừng lại để xác nhận giá trị đúng với  trước khi sửa, thay vì tự ý ghi đè?

---

## 8. Ví dụ đã xảy ra

- [[04 - Backtesting/2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short|02 - Win - EURUSD - 2026-11-30 - Short]] — mismatch năm (`trade_date: 2016-11-30` vs filename `2026-11-30`, và năm 2016/2026 lẫn lộn trong narrative) + mismatch giá TP (frontmatter `1.05882` vs bảng Summary `1.05886`). **Chưa được sửa** — cần  xác nhận giá trị đúng trước khi cập nhật.

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

> Một backtest sai vì đọc sai chart vẫn là dữ liệu thật, chỉ là bài học đắt. Một backtest đúng chart nhưng log sai dữ liệu không phải là dữ liệu — nó là tiếng ồn mặc áo thống kê, và tiếng ồn đó sẽ len vào chính con số quyết định liệu  đã sẵn sàng mua challenge hay chưa.

---

## 11. Phân tích chuyên sâu (Deep-Dive)

![[LogMismatch-DeepDive-RootCause.svg|760]]
*Sơ đồ: Chuỗi 5 Whys từ lỗi gõ nhầm tới nguyên nhân gốc thiếu cơ chế cách ly, và pipeline GIGO minh họa vì sao dữ liệu bẩn phá hủy toàn bộ hàm tổng hợp.*

### 11.1. Chuỗi 5 Whys — từ "gõ nhầm một con số" tới nguyên nhân gốc

| Bậc | Câu hỏi | Câu trả lời |
|---|---|---|
| Bề mặt | Vì sao note có mismatch? | Vì frontmatter, bảng Summary và narrative được điền ở các thời điểm khác nhau, không đối chiếu lại. |
| Why 1 | Vì sao không đối chiếu lại? | Vì không có bước "audit tự nhất quán" nào trong quy trình đóng note — template chỉ nhắc điền, không nhắc kiểm tra khớp. |
| Why 2 | Vì sao template không có bước audit? | Vì template được thiết kế để tối ưu tốc độ ghi lúc mới học ICT 2022 Model — trọng tâm khi đó là ghi được logic setup, chưa phải tính toàn vẹn dữ liệu. |
| Why 3 | Vì sao trọng tâm ban đầu là logic setup, không phải data integrity? | Vì sample còn nhỏ (n thấp), rủi ro thống kê của một note lỗi có vẻ không đáng kể — "chỉ 1 note, không sao". |
| Why 4 | Vì sao "chỉ 1 note không sao" là một giả định sai? | Vì Dataview dashboard cộng gộp **mọi note** không phân biệt sạch/bẩn — một note bẩn không bị cách ly, nó pha trộn vào toàn bộ average R và win rate ngay khi được lưu. |
| **Gốc** | **Nguyên nhân gốc** | **Không có cơ chế cách ly (quarantine) giữa "note đã ghi" và "note đã được xác minh tự nhất quán" — toàn bộ sample được đối xử như đã sạch ngay khi file tồn tại.** |

### 11.2. GIGO (Garbage In, Garbage Out) áp dụng vào backtest dashboard

Nguyên lý GIGO trong khoa học dữ liệu nói: chất lượng đầu ra của bất kỳ hệ thống tính toán nào **không thể vượt quá** chất lượng đầu vào — dù công thức tính (ở đây là expectancy, win rate, average R) có đúng tuyệt đối. Áp vào bối cảnh vault:

- **Input:** các trường `entry_price`, `stop_loss`, `take_profit`, `r_multiple`, `trade_date` trong frontmatter của từng note.
- **Transform:** Dataview query cộng gộp, tính trung bình, tính tỷ lệ thắng.
- **Output:** các số hiển thị trên `_Backtest Dashboard` — con số dùng để quyết định readiness gate mua challenge.

Vấn đề: Dataview **không có bước validate** giữa Input và Transform. Nó tin tưởng tuyệt đối frontmatter là sự thật. Nếu 1 trong 50 note có `r_multiple` sai do gõ nhầm, output (average R tổng) bị lệch — và vì không có log lỗi, không ai biết *mức độ* lệch cho tới khi audit tay từng note, việc gần như không ai thực sự làm định kỳ.

Điều này khác biệt về bản chất so với lỗi phân tích/thực thi (các mistake khác trong database): lỗi phân tích làm **1 lệnh sai**, nhưng GIGO ở đây làm **toàn bộ hàm tổng hợp sai** — mức độ lan tỏa lỗi rộng hơn nhiều so với quy mô của chính lỗi gốc.

### 11.3. Bốn nguồn lỗi kỹ thuật cụ thể trong backtest — ngoài phạm vi mismatch nội bộ note

Mục 1 của note gốc đã liệt kê 4 dạng mismatch **nội bộ** (frontmatter/filename/summary/narrative). Nhưng có một tầng lỗi khác, **trước** cả bước ghi log, nằm ở chính quá trình lấy dữ liệu để backtest — các nguồn lỗi này không tạo ra mismatch nội bộ (mọi trường vẫn khớp nhau) nhưng vẫn làm dữ liệu sai lệch với thực tế thị trường:

| Nguồn lỗi | Cơ chế | Hệ quả lên R-multiple |
|---|---|---|
| **Look-ahead trong bar replay** | Công cụ replay hiển thị nến chưa đóng hoàn chỉnh, hoặc cho phép cuộn xem trước dữ liệu tương lai một cách vô thức trước khi "quyết định" entry | Entry trigger được đánh giá với thông tin không có sẵn tại thời điểm thật — inflate winrate một cách hệ thống |
| **Spread không được tính** | Giá entry lấy theo giá mid-market của nến lịch sử, không cộng/trừ spread thực tế của broker | R-multiple ghi cao hơn thực tế; SL/TP hit giả (chưa thực sự bị chạm theo giá bid/ask thật) |
| **Giá làm tròn không nhất quán** | Một số nguồn dữ liệu lịch sử làm tròn tới 4 số lẻ, nguồn khác tới 5 số lẻ — copy qua lại giữa nguồn tạo lệch nhỏ tại entry/SL/TP | Risk/reward tính lại từ giá đã làm tròn sẽ không khớp với `r_planned` ghi từ nguồn gốc, tạo ra false-positive mismatch hoặc che giấu mismatch thật |
| **Timezone không thống nhất** | Nguồn dữ liệu lịch sử ghi giờ theo broker time hoặc UTC, quy đổi tay sang UTC+7 không nhất quán giữa các dòng trong cùng note | Kill Zone bị gán sai (một lệnh thực chất ngoài London/NY KZ bị ghi nhận nhầm là trong KZ) — làm sai luôn cả điều kiện lọc setup, không chỉ sai R |

Bốn nguồn lỗi này **không xuất hiện dưới dạng mismatch rõ ràng** (vì tất cả các trường trong note vẫn có thể khớp nhau hoàn hảo) — đây là dạng nguy hiểm hơn mismatch nội bộ, vì checklist đối chiếu 4 nguồn (mục 5.1 note gốc) **không phát hiện được** loại lỗi này. Cần một lớp kiểm tra khác: đối chiếu note với nguồn dữ liệu gốc (chart thật, lịch sử giá thật), không chỉ đối chiếu note với chính nó.

### 11.4. Vì sao dữ liệu bẩn phá hủy Evidence Tier System của Doctrine v2

Doctrine v2 (Deep Audit 15 Case Studies) xây dựng toàn bộ khung suy luận trên **Evidence Tier System** — phân loại mọi kết luận theo mức độ chứng cứ (Tier 0: giả thuyết/suy luận logic chưa kiểm định; Tier 1: quan sát từ 1 mẫu thật; Tier 2+: nhiều mẫu, có thể tổng quát hoá). Toàn bộ hệ thống Tier này có một giả định tiên quyết không được nói ra: **mỗi mẫu đưa vào Tier phải là mẫu sạch**.

Log Data Mismatch phá vỡ giả định đó ở gốc:

- Một "Tier 1" (n=1, quan sát thật) dựa trên note bị mismatch **không phải Tier 1 thật** — nó là Tier 1 giả, vì "quan sát thật" đó có thể chưa từng xảy ra đúng như được ghi.
- Khi nhiều note bẩn được cộng vào để tạo "Tier 2" (n≥5), số lượng mẫu tăng lên **không** làm tăng độ tin cậy — nó chỉ làm tăng ảo giác về độ tin cậy (nhiều mẫu bẩn cộng lại không tạo ra ít mẫu bẩn hơn).
- Hậu quả nghiêm trọng nhất: một rule được "thăng cấp" từ Tier 0 lên Tier 1/Tier 2 dựa trên dữ liệu bẩn sẽ được ghi vào Doctrine như một nguyên tắc đáng tin — và từ đó lan tỏa vào mọi quyết định tương lai dựa trên Doctrine đó, xa hơn rất nhiều so với phạm vi của note gốc bị lỗi.

Nói cách khác: Evidence Tier System giả định trục "số lượng mẫu" là trục duy nhất cần tăng dần. Log Data Mismatch cho thấy còn một trục thứ hai bị bỏ sót — **độ sạch của mẫu** — và một hệ thống chỉ tăng Tier theo số lượng mà không kiểm tra độ sạch có thể tự tin sai ở quy mô lớn hơn một mẫu lỗi đơn lẻ.

### 11.5. Ma trận tương tác với các mistake khác

| Mistake liên quan | Cơ chế tương tác với Log Data Mismatch |
|---|---|
| [[05 - Mistake - Not enough RR]] | R-multiple bị log sai (do mismatch) có thể *che giấu* một lệnh thực chất có RR thấp — dashboard sẽ không bao giờ gắn cờ "RR thấp" nếu con số R đã bị ghi sai thành cao hơn thực tế. |
| [[09 - Mistake - Wrong daily bias]] | `bias_correct` ghi không nhất quán với lesson learned (dạng mismatch thứ 5, chưa liệt kê ở mục 1) khiến không thể biết tỷ lệ đọc bias đúng thực tế là bao nhiêu — làm hỏng luôn cả số liệu để cải thiện mistake #9. |
| 08 — Weak Displacement | Nếu ví dụ minh họa cho "displacement mạnh" trong log bị lấy từ note có mismatch ngày/giá, ranh giới "mạnh vs yếu" được huấn luyện trên dữ liệu không xác thực. |
| 10 — FVG Not Valid | Bảng thống kê điều kiện hợp lệ FVG (nếu được xây từ log) sẽ kế thừa toàn bộ lỗi GIGO nếu log nguồn có mismatch — hai mistake này cộng hưởng theo chiều "lỗi log làm hỏng lỗi phân tích". |

---

## 12. Debate — Tranh biện hai chiều

![[LogMismatch-Debate-Map.svg|760]]
*Sơ đồ: Bản đồ tranh biện Log tối giản vs Log đầy đủ bắt buộc, cùng phán quyết có điều kiện và trường bất khả xâm phạm.*

**Chủ đề tranh biện:** *"Log tối giản để duy trì thói quen ghi chép" (chỉ ghi vài trường cốt lõi, nhanh, dễ duy trì) **vs** "Log đầy đủ bắt buộc mọi trường" (chấp nhận chậm hơn, để đảm bảo tính toàn vẹn dữ liệu).*

### Phe Ủng hộ Log tối giản

1. **Ma sát thấp → duy trì được thói quen dài hạn.** Một quy trình log mất 10 phút/lệnh dễ bị bỏ sau vài tuần vì mệt; log 2 phút với vài trường cốt lõi (entry, SL, TP, kết quả) có tỷ lệ duy trì cao hơn hẳn theo kinh nghiệm hình thành habit nói chung.
2. **Log nào cũng tốt hơn không log.** Một trader log tối giản đều đặn 100 lệnh còn hữu ích hơn một trader log đầy đủ nhưng bỏ giữa đường sau 15 lệnh vì quá tải.
3. **Nhiều trường không dùng tới = lãng phí thời gian.** Nếu 80% các trường mở rộng (timezone gốc, nguồn dữ liệu, version công cụ replay...) chưa từng được dùng để ra quyết định, chi phí ghi chúng không tương xứng với giá trị.
4. **Rủi ro mismatch tăng theo số trường phải điền.** Nghịch lý: log "đầy đủ" hơn có nhiều trường hơn để đối chiếu, tức nhiều điểm hơn có thể sai — tăng field không tự động tăng chất lượng nếu kỷ luật điền không đổi.

### Phe Ủng hộ Log đầy đủ bắt buộc

1. **Chính mistake #12 này chứng minh log tối giản không đủ.** Ví dụ thật trong mục 4 xảy ra dù note đã có đủ frontmatter theo template hiện tại — vấn đề không phải thiếu trường mà là thiếu **đối chiếu**; nhưng nếu log tối giản hơn nữa (bỏ hẳn bảng Summary hoặc narrative), khả năng phát hiện mismatch còn giảm mạnh hơn vì không còn gì để đối chiếu.
2. **12 trường bắt buộc không phải gánh nặng nếu tự động hoá đối chiếu.** Chi phí duy trì log đầy đủ có thể giảm bằng công thức Dataview tự tính R từ entry/SL/TP thay vì gõ tay — vấn đề nằm ở thiết kế quy trình, không phải ở số lượng trường tự nó.
3. **Chi phí sửa 1 note bẩn về sau lớn hơn chi phí ghi thêm field lúc đầu.** Một lệnh bị phát hiện mismatch sau 3 tháng buộc phải quay lại chart cũ để xác minh — tốn thời gian hơn nhiều so với việc ghi đủ và đúng ngay từ đầu.
4. **Sample dùng để mở readiness gate cần độ tin cậy cao hơn log cá nhân thông thường.** Đây không phải journal thông thường để tự phản tư — nó là **bằng chứng để ra quyết định tài chính lớn** (mua challenge FTMO/The5ers); ngưỡng chất lượng dữ liệu cần cao hơn "chỉ để duy trì thói quen".

### Phản biện chéo (2 vòng)

**Vòng 1:**
- *Phản đối → Ủng hộ tối giản:* "Nếu log tối giản làm mất khả năng audit, tại sao không đo thực tế tỷ lệ duy trì log giữa hai nhóm field-count khác nhau trước khi kết luận?" → *Ủng hộ tối giản phản hồi:* "Đúng, chưa có số liệu — nhưng nguyên lý giảm ma sát tăng compliance đã được quan sát rộng trong các hệ thống habit-formation khác, không phải giả định vô căn cứ."
- *Ủng hộ tối giản → Phản đối:* "Log đầy đủ 12 trường có phải chính nó tạo áp lực khiến trader điền qua loa (giá trị mặc định, không dẫn chứng) thay vì điền đúng ít trường?" → *Phản đối phản hồi:* "Rủi ro đó là thật (xem mục Audit — red flag '6/6 ghi mặc định' áp dụng tương tự) nhưng là vấn đề của **thiết kế UI/quy trình ghi**, không phải lý do để giảm số trường cần có."

**Vòng 2:**
- *Phản đối → Ủng hộ tối giản:* "Log tối giản có tính đến field `trade_date` là trường bắt buộc tối thiểu để tránh lỗi nhầm năm (mục 5.3 note gốc) không? Nếu phải giữ field đó, log 'tối giản' vẫn cần ít nhất 8-10 trường — gần bằng log đầy đủ." → *Ủng hộ tối giản thừa nhận một phần:* "Đúng, một số trường (ngày, entry/SL/TP, kết quả) là bất khả xâm phạm dù tối giản tới đâu — tranh luận thực ra là về các trường **mở rộng** (context narrative chi tiết, ghi chú tâm lý...), không phải toàn bộ 12 trường."

### Phán quyết

Tranh biện thu hẹp lại còn một câu hỏi cụ thể hơn ban đầu: không phải "tối giản hay đầy đủ" mà là **"đâu là bộ trường lõi bất khả xâm phạm, và đâu là trường mở rộng có thể linh hoạt"**. Cả hai phe đồng thuận rằng: ngày-tháng-năm, entry/SL/TP, và kết quả là bất khả xâm phạm (không phe nào phản đối). Tranh cãi còn lại là về context narrative chi tiết và các trường phân tích mở rộng — **chưa có dữ liệu (Tier 0)** để xác định ngưỡng tối ưu giữa compliance rate và data completeness. Đề xuất Tier 1: đo thử tỷ lệ hoàn thành log trong 4 tuần với template rút gọn (8 trường lõi) so với template hiện tại (12+ trường) trước khi quyết định.

---

## 13. Devil's Advocate — Phản biện gay gắt

**Luận điểm bị tấn công:** *"Checklist đối chiếu 4 nguồn dữ liệu + audit định kỳ sẽ giải quyết được vấn đề Log Data Mismatch."*

1. **Checklist đối chiếu vẫn dựa vào chính người đã tạo ra lỗi để tự kiểm tra lỗi của mình.** Nếu một người vô thức gõ nhầm năm 2026 thành 2016 vì thói quen, cùng một người đọc lại note vẫn có thể vô thức "thấy đúng" vì não đã quen với lỗi đó — self-review có giới hạn tâm lý học đã biết (confirmation bias khi tự đọc lại sản phẩm của chính mình).

2. **"Đối chiếu 4 nguồn" giả định 4 nguồn độc lập — nhưng thực ra cả 4 đều bắt nguồn từ 1 người, 1 lần nhớ lại.** Nếu trí nhớ về giao dịch đã sai ngay từ đầu (ví dụ nhớ nhầm TP), cả filename, frontmatter, bảng Summary, và narrative có thể **đồng thời sai theo cùng một cách** — khớp nhau hoàn hảo nhưng vẫn sai so với thực tế thị trường. Checklist mục 7 note gốc không phát hiện được trường hợp "sai nhất quán" này, chỉ phát hiện "sai không nhất quán".

3. **Audit ngẫu nhiên 1-2 note/tuần (mục 6 Best Practices) có xác suất phát hiện rất thấp nếu tỷ lệ lỗi thực tế nhỏ.** Nếu tỷ lệ mismatch thực tế trong toàn sample là 5-10% (chưa biết, chưa đo), audit 1-2 note/tuần trên một sample hàng chục note sẽ mất nhiều tháng để có cơ hội hợp lý bắt được đa số lỗi — trong lúc đó dashboard vẫn tiếp tục cộng gộp dữ liệu bẩn vào các quyết định gần hạn (readiness gate).

4. **Chưa có ai đo tỷ lệ mismatch thực tế trong toàn bộ sample hiện có.** Ví dụ mục 4 là **1 trường hợp được phát hiện tình cờ** trong lúc soạn chính note mistake này — không phải kết quả của một cuộc audit có hệ thống. Không có cơ sở để tin rằng đây là trường hợp duy nhất; con số thật có thể cao hơn nhiều, hoặc thấp hơn — hiện tại là ẩn số hoàn toàn.

5. **House rule "không tự sửa dữ liệu, phải xác nhận trước" tạo ra một hàng đợi sửa lỗi không có deadline.** Ví dụ mục 4 note gốc ghi rõ "chưa được sửa" — không có cơ chế nào đảm bảo note này (và các note tương tự tương lai) sẽ thực sự được xác nhận và sửa trong một khung thời gian xác định, thay vì nằm mãi trong dashboard như một điểm dữ liệu bẩn vô thời hạn.

6. **Mục 5.4 note gốc nói lỗi này "không để lại dấu vết trên P&L" — nhưng điều đó cũng có nghĩa không có động lực tự nhiên nào để ưu tiên sửa nó so với các mistake khác có dấu hiệu rõ ràng hơn (thua lỗ ngay).** Trên thực tế, ưu tiên hoá đang cạnh tranh với các mistake "đau" hơn — rủi ro là Log Data Mismatch luôn bị đẩy xuống cuối danh sách ưu tiên dù tác động của nó (làm hỏng toàn bộ dashboard) có thể nghiêm trọng hơn về mặt hệ thống.

### Bảng tổng hợp: đòn công kích nào đã được xử lý, đòn nào còn treo

| # | Đòn công kích | Đã xử lý trong note gốc? | Ghi chú |
|---|---|---|---|
| 1 | Self-review có giới hạn tâm lý học | Chưa | Cần cơ chế review chéo (người khác đọc lại), note gốc chỉ có self-checklist |
| 2 | Sai nhất quán ở cả 4 nguồn cùng lúc | Chưa | Checklist mục 7 chỉ bắt lỗi *không* nhất quán, không bắt lỗi *nhất quán nhưng sai* |
| 3 | Xác suất phát hiện thấp của audit ngẫu nhiên | Chưa | Chưa có ước tính tỷ lệ mismatch thực tế để tính cỡ mẫu audit cần thiết |
| 4 | Chưa đo tỷ lệ mismatch toàn sample | Chưa | Backlog ưu tiên cao — cần audit toàn bộ 1 lần để có baseline |
| 5 | Hàng đợi sửa lỗi không deadline | Một phần | House rule có nêu nhưng không gắn deadline/SLA |
| 6 | Thiếu động lực ưu tiên vì không đau ngay | Chưa | Cần gắn severity rõ ràng hơn "high" hiện tại vào quy trình review hàng tuần |

---

## 14. Audit — Khung kiểm toán độc lập

![[LogMismatch-Audit-Framework.svg|760]]
*Sơ đồ: Pipeline kiểm toán 4 bước, bộ red flag tự lừa/gian lận, meta-audit chính note này, và nhịp audit đề xuất.*

> [!danger] Vì sao mục Audit đặc biệt quan trọng ở chính mistake này
> Đây **là** mistake về audit trail — một khung audit lỏng cho chính note "Log Data Mismatch" sẽ tự mâu thuẫn với nội dung nó đang cảnh báo. Mục này áp dụng chuẩn nghiêm ngặt hơn các mistake khác.

### 14.1. Trường log bắt buộc để có thể audit được chính lỗi mismatch

| # | Trường | Mục đích |
|---|---|---|
| 1 | `mismatch_detected` (Yes/No) | Đánh dấu note đã được audit và có hay không phát hiện mismatch |
| 2 | `mismatch_type` (a/b/c/d theo phân loại mục 1, hoặc "sai nhất quán" theo mục 13.2) | Phân loại để thống kê dạng lỗi phổ biến nhất |
| 3 | `mismatch_fields` (danh sách trường bị ảnh hưởng) | Xác định phạm vi ảnh hưởng cụ thể |
| 4 | `audit_date` | Ngày thực hiện audit — để tính độ trễ giữa `trade_date`/`backtest_date` và ngày phát hiện lỗi |
| 5 | `audit_method` (self-review / peer-review / cross-check với chart gốc) | Ghi rõ phương pháp, vì self-review có giới hạn đã nêu ở mục 13.1 |
| 6 | `resolution_status` (unresolved / confirmed-correct-value / corrected) | Theo dõi tiến độ xử lý, tránh hàng đợi vô thời hạn (mục 13.5) |
| 7 | `resolution_deadline` | Gắn deadline cụ thể — giải quyết đòn công kích mục 13.5 |
| 8 | `r_multiple_recalculated` | Giá trị R tính lại từ entry/SL/TP đã log, để so sánh với `r_multiple` gốc |
| 9 | `r_multiple_delta` | Chênh lệch giữa `r_multiple` gốc và giá trị tính lại — dùng để ưu tiên note nào cần sửa gấp |
| 10 | `data_source` | Nguồn dữ liệu gốc (tên platform/broker) — phục vụ audit nguồn lỗi kỹ thuật (mục 11.3) |
| 11 | `timezone_used` | Timezone đã dùng khi ghi log — phục vụ audit lỗi timezone (mục 11.3) |
| 12 | `included_in_dashboard_sample` (Yes/No) | Đánh dấu note có đang được tính vào sample thống kê hay đã bị cách ly (quarantine) |

### 14.2. Bộ câu hỏi PASS/FAIL

1. Filename và `trade_date` khớp tuyệt đối về năm-tháng-ngày? PASS/FAIL
2. Frontmatter và bảng Backtest Summary khớp 100% ở entry/SL/TP? PASS/FAIL
3. `r_multiple` khớp với giá trị tính lại từ entry/SL/TP (sai số 0)? PASS/FAIL
4. Mọi mốc thời gian trong narrative dùng nhất quán một năm? PASS/FAIL
5. `bias_correct` nhất quán với nội dung lesson learned? PASS/FAIL
6. `data_source` và `timezone_used` được ghi rõ (không để trống)? PASS/FAIL
7. Không có dấu hiệu look-ahead trong mô tả entry trigger (mục 11.3)? PASS/FAIL
8. Nếu note có mismatch đã phát hiện trước đó — có `resolution_status` và `resolution_deadline` được ghi? PASS/FAIL
9. Phương pháp audit (`audit_method`) có phải cross-check với chart gốc, không chỉ self-review? PASS/FAIL
10. Timestamp chỉnh sửa gần nhất có SAU `audit_date`, không SAU `timestamp_exit` một cách đáng ngờ (dấu hiệu sửa hồi tố)? PASS/FAIL
11. Note có đang bị đánh dấu `included_in_dashboard_sample: No` nếu chưa xử lý xong mismatch (không lẫn vào thống kê)? PASS/FAIL
12. Đã đối chiếu ít nhất 1 lần với nguồn dữ liệu gốc (không chỉ đối chiếu nội bộ giữa 4 nơi trong note)? PASS/FAIL

### 14.3. Rubric chấm điểm

| Hạng | Số câu PASS | Ý nghĩa | Hành động |
|---|---|---|---|
| A | 11-12 | Note sạch, đáng tin để dùng trong sample | Giữ trong dashboard, không cần hành động |
| B | 8-10 | Có vài lỗ hổng nhỏ, chưa nguy hiểm | Sửa lỗ hổng trong tuần, giữ tạm trong sample có ghi chú |
| C | 5-7 | Nghi ngờ đáng kể về tính toàn vẹn | Cách ly khỏi sample (`included_in_dashboard_sample: No`) cho tới khi audit lại |
| F | 0-4 | Không đáng tin — như ví dụ mục 4 note gốc | Cách ly ngay, đặt `resolution_deadline` cụ thể, ưu tiên xử lý trong tuần |

### 14.4. Red Flags — dấu hiệu tự lừa/gian lận phổ biến khi tự audit

- **Sửa `r_multiple` sau khi biết kết quả cuối để khớp với `result: Win/Loss`** — timestamp sửa sau timestamp đóng lệnh là bằng chứng hồi tố hoá, tương tự red flag đã nêu ở audit của mistake #10.
- **Đánh `mismatch_detected: No` mà không thực sự đối chiếu 4 nguồn** — dấu hiệu: `audit_date` trống hoặc trùng đúng ngày tạo note (không có khoảng cách thời gian để thực sự rà lại).
- **`resolution_status: confirmed-correct-value` nhưng không có ghi chú nào giải thích *vì sao* giá trị đó được xác nhận đúng** — thiếu dẫn chứng, giống red flag "6/6 ghi mặc định" ở mistake #10.
- **Toàn bộ sample có `mismatch_detected: No`** — về mặt thống kê rất khó xảy ra nếu sample đủ lớn (n≥20) và audit đủ nghiêm ngặt; tỷ lệ 0% mismatch trên toàn sample là dấu hiệu đáng ngờ hơn là dấu hiệu tốt.

### 14.5. Meta-audit chính note "Log Data Mismatch" này

- Ví dụ thật duy nhất (mục 4, mục 8 note gốc) là **1 trường hợp** — Tier 1, chưa đủ để khẳng định tỷ lệ phổ biến của lỗi này trong toàn vault (Doctrine v2 Rule 1: dùng ngôn ngữ "giả thuyết" cho tới khi có ≥5 mẫu).
- Note gốc chưa có bước "audit toàn bộ sample 1 lần để tạo baseline tỷ lệ mismatch" — đây nên là backlog ưu tiên cao nhất rút ra từ chính phần Audit này.
- Checklist mục 7 note gốc (đối chiếu nội bộ 4 nguồn) **không đủ** để bắt lỗi "sai nhất quán ở cả 4 nguồn" (đòn công kích 13.2) — cần bổ sung bước đối chiếu với nguồn ngoài (chart gốc/lịch sử giá).

### 14.6. Nhịp audit đề xuất

- **Ngay khi đóng note:** tự chạy checklist mục 7 note gốc (đối chiếu nội bộ 4 nguồn) — bắt buộc, không tùy chọn.
- **Cuối mỗi tuần:** chấm rubric 14.3 cho toàn bộ note mới trong tuần.
- **Cuối mỗi tháng:** audit toàn diện (bao gồm cross-check với chart gốc, không chỉ self-review nội bộ) cho 5-10 note chọn ngẫu nhiên từ toàn bộ sample — không chỉ note mới.
- **Một lần duy nhất (ưu tiên cao, nên làm sớm):** audit toàn bộ sample hiện có để lập baseline tỷ lệ mismatch thực tế — số liệu này là điều kiện tiên quyết để đánh giá đúng mức độ nghiêm trọng của backlog này.

---

## 15. Case Studies (kịch bản minh họa)

![[LogMismatch-CaseStudies-Panel.svg|760]]
*Sơ đồ: So sánh Case A (thật) với Case B/C (minh họa) — loại mismatch, hậu quả, rubric và bài học chính.*

> [!info] Ghi chú quan trọng
> Case A dưới đây dựa trên ví dụ **thật** đã có trong note gốc (mục 4, mục 8). Case B và Case C là **kịch bản minh họa** được dựng để làm rõ nguyên lý — KHÔNG phải log giao dịch thật, không đại diện cho một lệnh cụ thể nào đã xảy ra.

### Case A — Thật: mismatch năm + giá TP (EURUSD, đã có trong note gốc)

**Nguồn:** `04 - Backtesting/2026-07-15/02 - Win - EURUSD - 2026-11-30 - Short.md` (mục 4, mục 8 note gốc)

- Filename: `2026-11-30`. Frontmatter `trade_date: 2016-11-30`. Chênh 10 năm.
- Bảng Summary TP `1.05886` vs frontmatter TP `1.05882` — lệch 4 điểm giá.
- Narrative lẫn cả hai năm 2016/2026 cho cùng một chuỗi sự kiện liên tục.
- Kết quả ghi nhận: `result: Win`, R = 2.09, grade C+ — **một lệnh "thắng đẹp" nhưng dữ liệu không đáng tin.**

**Bài học:** kết quả tốt (Win, R cao) không tự động đảm bảo dữ liệu sạch — đây chính xác là loại lỗi "không để lại dấu vết trên P&L" nêu ở mục 11.4/5.4 note gốc. Note này hiện `resolution_status: unresolved` theo house rule, minh chứng sống cho đòn công kích 13.5 (hàng đợi không deadline).

### Case B — Minh họa: log tối giản làm mất khả năng phát hiện lỗi timezone

**Bối cảnh giả định:** Một trader áp dụng "log tối giản" (chỉ ghi entry, SL, TP, kết quả — theo đề xuất Phe Ủng hộ tối giản mục 12) cho một backtest GBPJPY dữ liệu 2015, không ghi `data_source` hay `timezone_used`.

- 6 tháng sau, khi audit toàn diện (mục 14.6), phát hiện nghi ngờ: entry trigger được ghi là "trong London KZ" nhưng không thể xác minh lại vì không biết dữ liệu gốc lấy theo giờ nào.
- Vì thiếu `timezone_used`, không thể phân biệt được đây là lỗi timezone thật (mục 11.3) hay ghi đúng — note rơi vào trạng thái "không thể audit", tệ hơn cả "audit ra lỗi", vì không có cách nào giải quyết dứt điểm.
- Rubric 14.3: note này chấm **F** — không phải vì chắc chắn sai, mà vì **không thể xác minh**, một dạng thất bại kiểm toán riêng biệt so với "chắc chắn có mismatch".

**Bài học:** minh họa trực tiếp cho luận điểm Phe Log đầy đủ trong Debate mục 12 — thiếu trường mở rộng (`data_source`, `timezone_used`) không gây mismatch rõ ràng ngay lúc ghi, nhưng phá hủy khả năng audit về sau, đúng lúc cần audit nhất.

### Case C — Minh họa (gray-zone): kết luận rule sai sinh ra từ một log bẩn

**Bối cảnh giả định:** Trong 15 backtest note về setup "FVG sau sweep", 1 note (giống dạng Case A) có `r_multiple` ghi tay cao hơn giá trị tính lại từ entry/SL/TP thật khoảng +1.2R do lỗi log. 14 note còn lại sạch, average R thật là +0.42R.

- Vì note bẩn đó nằm trong sample, average R hiển thị trên dashboard là +0.53R — có vẻ không khác biệt lớn, dễ bị coi là "sai số chấp nhận được".
- Dựa trên average R +0.53R (đã bị lệch), một kết luận được rút ra và ghi vào rule cá nhân: "Setup FVG sau sweep có expectancy đủ tốt để tăng size lên 1.5x mức chuẩn."
- Thực tế nếu loại note bẩn: average R thật +0.42R — có thể **không** đủ ngưỡng để biện minh cho việc tăng size, tùy vào ngưỡng quyết định đã đặt ra trước đó.
- **Đây là gray-zone kiểm toán:** không có bước nào trong quy trình hiện tại (checklist mục 7, Best Practices mục 6 note gốc) buộc phải loại trừ hoặc gắn cờ note khả nghi *trước khi* nó được dùng để rút ra kết luận thay đổi hành vi giao dịch (tăng size). Ranh giới "sai số chấp nhận được" so với "sai số làm sai lệch quyết định" chưa được định nghĩa bằng số cụ thể nào.

**Bài học:** minh họa trực tiếp cho mục 11.4 (Log Data Mismatch phá hủy Evidence Tier System) — một rule được "thăng cấp" dựa trên sample có lẫn dữ liệu bẩn có thể dẫn tới quyết định thực (tăng size, tăng rủi ro thật) mà không ai biết gốc rễ vấn đề là 1 note bẩn trong 15 note.

### Bảng so sánh 3 case

| Tiêu chí | Case A (Thật) | Case B (Minh họa) | Case C (Minh họa, gray-zone) |
|---|---|---|---|
| Loại mismatch | Năm + giá TP (dạng a, b) | Không thể xác minh (thiếu trường mở rộng) | Sai nhất quán, R ghi cao hơn thật (dạng d) |
| Phát hiện được bằng checklist mục 7? | Có, đã phát hiện | Không (checklist không yêu cầu timezone) | Không trực tiếp (cần audit toàn sample) |
| Hậu quả | 1 note treo `unresolved` | Note không thể audit dứt điểm | Rule sai lan vào quyết định size thật |
| Rubric 14.3 | F | F (không thể xác minh) | C (nghi ngờ, cần cách ly để kiểm tra) |
| Bài học chính | Kết quả tốt ≠ dữ liệu sạch | Thiếu field mở rộng phá khả năng audit | Dữ liệu bẩn lan vào cả quyết định hành vi |

---

## 16. Liên kết

**Mistakes liên quan:** [[05 - Mistake - Not enough RR]] · [[09 - Mistake - Wrong daily bias]]

**Dashboard:** [[04 - Backtesting/_Backtest Dashboard|_Backtest Dashboard]] · [[01 - Dashboard/02 - Mistake Frequency Dashboard|Mistake Frequency Dashboard]]

**Template:** [[08 - Templates/Backtest templete|Backtest templete]]
