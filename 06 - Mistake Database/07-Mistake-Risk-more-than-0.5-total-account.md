---
type: mistake
category: risk
severity: critical
related_model: ICT 2022
frequency: 2
status: active
tags:
  - trading/ict/mistake
  - trading/review
  - trading/risk
created: 2026-06-19
updated: 2026-08-02
---

# Mistake - Risk more than 0.5% total account

> [!summary] Tóm tắt 1 câu
> Risk vượt quá 0.5% equity trên một lệnh — dù bằng lot quá khổ, SL bị nới rộng mà không giảm size, gồng thêm vào lệnh đang thua, hay stack các vị thế tương quan cao cùng lúc — là con đường nhanh nhất để một chuỗi thua hoàn toàn bình thường (thống kê) biến thành một lần bị loại khỏi challenge FTMO/The5ers.

> [!danger] Nguyên tắc cốt lõi
> 0.5% không phải là con số "an toàn cho có" — nó là tham số được tính toán để một chuỗi 8-10 lệnh thua liên tiếp (điều **sẽ** xảy ra với bất kỳ edge nào, kể cả edge dương) vẫn nằm trong daily loss limit, và một chuỗi ~20 lệnh thua vẫn nằm trong max loss limit. Vượt 0.5% không làm bạn "kiếm nhanh hơn" — nó chỉ rút ngắn khoảng cách từ một ngày xấu bình thường đến việc mất tài khoản.

---

## 1. Mô tả lỗi

Đây là lỗi risk quản lý nghiêm trọng nhất trong toàn bộ vault, vì nó không cần sai về phân tích (bias, entry, cấu trúc) vẫn có thể phá hủy tài khoản chỉ bằng cách vi phạm một con số duy nhất: **$ risk trên mỗi lệnh vượt quá 0.5% equity**. Lỗi này có 4 hình thái, thường xuất hiện độc lập nhưng cũng hay cộng dồn với nhau:

1. **Lot quá khổ (oversized lot):** vào size lớn hơn công thức cho phép vì "cảm thấy chắc ăn" (high conviction), bỏ qua việc tính toán từ khoảng cách SL.
2. **SL rộng hơn nhưng giữ nguyên lot:** kế hoạch ban đầu là SL 20 điểm với lot X, nhưng khi giá không cho phép đặt SL sát như vậy, trader dời SL ra 35-40 điểm mà **không** tính lại lot — $ risk tăng tỷ lệ thuận với SL mới.
3. **Gồng lệnh thua (adding to losers):** thêm vị thế cùng hướng vào một lệnh đang âm để "trung bình giá", với hy vọng giá quay đầu — biến một lệnh 0.5% ban đầu thành 1%, 1.5% hoặc hơn trên cùng một hướng sai.
4. **Stack correlated exposure:** mở nhiều lệnh "0.5% mỗi lệnh" trên các instrument tương quan cao cùng lúc (NAS100 + US30, EURUSD + GBPUSD) — trên giấy tờ mỗi lệnh đúng luật, nhưng rủi ro tổng hợp gần như một lệnh 1% duy nhất vì chúng di chuyển cùng chiều.

Điểm chung của cả 4 hình thái: trader luôn có thể tự biện minh rằng "về mặt kỹ thuật tôi vẫn tuân thủ 0.5%" trong khi $ risk thực tế đã vượt xa mức đó.

![[OverRisk-Sec-01-MoTa.svg|760]]
*Sơ đồ: 4 con đường phá vỡ trần 0.5%/lệnh và cách chúng cộng dồn thành rủi ro tổng vượt cap.*

---

## 2. Biểu hiện & Dấu hiệu nhận biết

| Dấu hiệu | Mức độ cảnh báo |
|---|---|
| "Setup này chắc ăn quá, size gấp đôi thôi" | Đỏ |
| Dời SL rộng hơn kế hoạch nhưng không bấm lại lot size | Đỏ |
| Vào thêm lệnh để "trung bình giá" khi đang âm | Đỏ |
| Mở cùng lúc NAS100 + US30, hoặc EURUSD + GBPUSD cùng hướng | Amber |
| "Risk creep" sau vài lệnh thắng liên tiếp — cảm giác "chơi bằng tiền của thị trường" | Amber |
| Revenge sizing — tăng size để "gỡ lại" lệnh vừa thua | Đỏ |
| Không biết chính xác $ risk trước khi bấm lệnh (chỉ biết "khoảng khoảng") | Đỏ |

Checklist nhận diện nhanh trước khi bấm lệnh:

- [ ] Tôi đã tính $ risk chính xác từ StopDistance và xác định lot size tương ứng chưa, hay đang áng chừng?
- [ ] Nếu SL phải rộng hơn dự kiến, tôi đã **giảm lot** để giữ nguyên $ risk chưa?
- [ ] Tôi có đang mở cùng lúc một lệnh tương quan cao (NAS100/US30, EURUSD/GBPUSD, XAUUSD/DXY) không?
- [ ] Đây có phải là revenge sizing hay "chơi bằng tiền của thị trường" sau chuỗi thắng không?
- [ ] Tôi có đang thêm size vào một lệnh đang âm để trung bình giá không?

![[OverRisk-Sec-02-BieuHien.svg|760]]
*Sơ đồ: các tell cảnh báo khi risk thực tế (từng lệnh hoặc cộng dồn) vượt 0.5%.*

---

## 3. Cơ chế & Vì sao nguy hiểm

### Position sizing — công thức bắt buộc phải thuộc lòng

```
PositionSize = (AccountEquity × RiskPercent) / (StopDistance × ValuePerPoint hoặc ValuePerPip)
```

**Ví dụ 1 — NAS100:** Equity $10,000, risk 0.5% = $50. SL kế hoạch 25 điểm. Value/điểm ≈ $10 cho mỗi 1.0 lot (tức $1/điểm cho mỗi 0.1 lot).

```
Size = $50 / (25 điểm × $10/điểm) = $50 / $250 = 0.2 lot
```

Nếu cấu trúc thị trường buộc SL phải rộng ra 40 điểm để hợp lệ (dưới swing low thật, không phải SL "đoán"), size **phải giảm**:

```
Size mới = $50 / (40 × $10) = 0.125 lot (làm tròn xuống theo bước lot broker cho phép)
```

Đây chính là điểm phân biệt trader kỷ luật và trader phá vỡ 0.5%: **không bao giờ giữ nguyên lot khi SL nới rộng — luôn tính lại size để $ risk cố định.**

**Ví dụ 2 — EURUSD:** Equity $10,000, risk 0.5% = $50. SL kế hoạch 15 pips. Giả sử (dùng số tròn để minh họa, số thực tế phụ thuộc broker/account currency): $1/pip cho mỗi micro lot (0.01 lot) trên tài khoản của bạn.

```
Size = $50 / (15 pip × $1/pip) = 3.33 → làm tròn XUỐNG 3 micro lot (0.03 lot)
```

*Ghi chú kỹ thuật:* theo chuẩn thị trường phổ biến, 1 lot chuẩn EURUSD ≈ $10/pip, 1 mini lot (0.1) ≈ $1/pip, 1 micro lot (0.01) ≈ $0.1/pip — hãy luôn kiểm tra contract specification thật của broker trước khi tính, nguyên tắc công thức không đổi dù $/pip khác nhau. **Luôn làm tròn xuống**, không bao giờ làm tròn lên để "cho đẹp số lot".

### Drawdown & risk-of-ruin — vì sao 0.5% không phải là sự thận trọng thái quá

Một chuỗi thua liên tiếp là **hiện tượng thống kê bình thường**, kể cả với một edge dương rõ ràng. Với win rate 45-50% (khá thực tế cho một discretionary edge như ICT 2022), xác suất gặp một chuỗi 6-10 lệnh thua liên tiếp trong vài trăm lệnh là rất cao — đây không phải dấu hiệu edge bị hỏng, mà là variance tự nhiên. Vấn đề là: **prop firm không quan tâm bạn có edge dương về lâu dài hay không — họ chỉ nhìn drawdown tức thời.**

Bảng dưới đây tính equity còn lại sau N lệnh thua liên tiếp, với size được tính lại theo equity hiện tại sau mỗi lệnh (equity-based sizing, đúng chuẩn compounding):

| N lệnh thua | Equity @ 0.5%/lệnh | Equity @ 1%/lệnh | Equity @ 2%/lệnh |
|---|---|---|---|
| 1 | $9,950 | $9,900 | $9,800 |
| 3 | $9,850.75 | $9,702.99 | $9,411.92 ⚠️ **breach daily** |
| 5 | $9,752.49 | $9,509.90 | $9,039.21 |
| 6 | $9,703.73 | $9,414.80 ⚠️ **breach daily** | $8,858.43 🔴 **breach max** |
| 10 | $9,511.11 | $9,043.82 | $8,170.73 (giả định nếu bị ép tiếp tục) |
| 11 | $9,463.55 ⚠️ **breach daily** | $8,953.38 🔴 **breach max** | $7,847.17 |
| 15 | $9,275.69 | $8,600.59 | $7,385.70 |
| 20 | $9,046.09 | $8,179.07 | $6,676.09 |
| 21 | $9,000.86 🔴 **≈ breach max** | — | — |

*Ngưỡng FTMO 10K: daily loss 5% = $500 (so với balance đầu ngày, reset mỗi ngày); overall max loss 10% = $1,000 (tính xuyên suốt, không reset).*

Đọc bảng này theo đúng ngữ cảnh: **daily loss limit** chỉ bị vi phạm nếu chuỗi thua xảy ra **trong cùng một ngày giao dịch** (vì nó so với balance đầu ngày và reset hàng ngày); **max loss limit** thì cộng dồn xuyên suốt toàn bộ challenge, không quan tâm chuỗi thua trải dài bao nhiêu ngày. Với logic đó:

- **Ở 2% risk:** chỉ cần một ngày xấu với 3 lệnh thua liên tiếp là đã phá vỡ daily limit; 6 lệnh thua (có thể chỉ trong 1-2 ngày) là phá vỡ luôn max loss — challenge kết thúc.
- **Ở 1% risk:** cần một ngày cực xấu với 6 lệnh thua để chạm daily limit; nhưng chỉ cần tổng cộng 11 lệnh thua (có thể trải qua vài ngày) để phá vỡ max loss — biên độ an toàn vẫn mỏng.
- **Ở 0.5% risk:** cần tới ~10-11 lệnh thua **trong cùng một ngày** mới chạm daily limit (kịch bản gần như không xảy ra với kỷ luật entry hợp lý), và cần ~20-21 lệnh thua cộng dồn mới chạm max loss — đủ biên độ để một chuỗi thua thống kê bình thường không đồng nghĩa với việc bị loại.

![[OverRisk-Sec-03-CoChe.svg|760]]
*Sơ đồ: equity curve so sánh 0.5% / 1% / 2% qua một chuỗi thua liên tiếp — 2% phá vỡ daily limit trong ~3 lệnh và max loss trong ~6 lệnh, trong khi 0.5% vẫn an toàn xuyên suốt.*

### Correlation — hai lệnh 0.5% có thể là một lệnh 1%

Rủi ro không chỉ đến từ một lệnh đơn lẻ mà từ **rủi ro tổng hợp** khi các vị thế di chuyển cùng chiều:

- **NAS100 & US30:** cả hai đều là chỉ số Mỹ, correlation thường ở mức 0.85-0.95. Long cả hai cùng lúc gần như là nhân đôi cùng một cược.
- **EURUSD & GBPUSD:** cùng chung "chân" USD, correlation thường 0.7-0.9. Một tin tức USD mạnh làm cả hai cặp di chuyển cùng hướng ngược lại vị thế của bạn cùng lúc.
- **XAUUSD & DXY:** quan hệ nghịch biến rõ rệt — long XAUUSD về bản chất là một cược ngược chiều với USD, tương tự như short một rổ USD. Nếu đồng thời short USD-pair khác, bạn đang cộng dồn cùng một luận điểm vĩ mô hai lần.

**Quy tắc cap:** khi mở từ 2 vị thế trở lên trên các instrument có correlation > 0.7, coi tổng rủi ro của nhóm đó bị giới hạn ở 0.5% aggregate — ví dụ chia đều 0.25%/lệnh, hoặc tốt hơn là chỉ chọn lệnh có conviction cao nhất trong nhóm và bỏ qua các lệnh còn lại.

---

## 4. Ví dụ minh họa

### ✅ Đúng

NAS100 Long, equity $10,000, risk cố định 0.5% = $50. Size được tính từ SL thật (dưới swing low hợp lệ), không phải từ "cảm giác". Khi SL buộc phải rộng ra giữa chừng phân tích, size được tính lại ngay để giữ nguyên $50. Muốn thêm US30 Long cùng hướng — tổng rủi ro nhóm correlated bị cap ở 0.5%, không phải 0.5% × 2. Circuit breaker (dừng sau 2 lệnh thua liên tiếp hoặc -1% ngày) đã được viết ra từ trước.

![[OverRisk-Example-Correct.svg|760]]
*Sơ đồ: risk 0.5% cố định, size tính từ SL, correlated exposure bị cap, circuit breaker đặt sẵn.*

**Vì sao đúng:** $ risk luôn cố định ở 0.5% bất kể lot size, SL rộng/hẹp, hay số lượng lệnh đang mở — công thức luôn được áp dụng, không có ngoại lệ cho "conviction cao". Correlated exposure được cap chủ động thay vì cộng dồn vô tình. Circuit breaker được quyết định trước khi cảm xúc có cơ hội chi phối, nên một chuỗi thua bình thường (thống kê) — như bảng ở mục 3 cho thấy — không biến thành một lần bị loại khỏi challenge.

### ❌ Sai

Cùng setup NAS100 Long nhưng "cảm thấy chắc ăn quá" nên risk 2% = $200 thay vì $50. Giữa chừng, giá chạy qua SL dự kiến, trader dời SL rộng ra nhưng **giữ nguyên lot** — $ risk thực tế còn cao hơn $200. Đồng thời mở thêm US30 Long "vì cùng xu hướng" — correlation ~0.9 khiến rủi ro tổng hợp gần gấp đôi một vị thế 2% đơn lẻ. Không có circuit breaker nào được đặt trước.

![[OverRisk-Example-Wrong.svg|760]]
*Sơ đồ: risk 2% "chắc ăn", SL bị nới rộng mà không giảm size, double-up correlated không kiểm soát.*

**Bài học:** Bias đúng và setup "đẹp" không bao giờ là lý do hợp lệ để tăng risk — chúng không làm giảm variance hay xác suất một chuỗi thua bình thường xảy ra. Chỉ cần 3 lệnh thua liên tiếp ở 2% là đã đủ phá vỡ daily loss limit của FTMO; cộng thêm SL bị nới rộng không tính lại và correlated exposure không kiểm soát, con số thiệt hại thực tế thường tệ hơn nhiều so với "$200 trên giấy".

---

## 5. Kiến thức nâng cao (Advanced)

![[OverRisk-Advanced-RiskOfRuin.svg|760]]
*Sơ đồ: % drawdown sau N lệnh thua liên tiếp ở 0.5% / 1% / 2% — 2% chạm cả daily lẫn max limit trong vài lệnh đầu tiên.*

### 5.1. Risk of ruin & vì sao 0.5% cố tình sub-Kelly

Công thức Kelly criterion cho cỡ cược tối ưu để tối đa hóa tăng trưởng kép dài hạn: `f* = (b×p − q) / b`, với `b` = tỷ lệ RR trung bình, `p` = win rate, `q = 1 − p`. Ví dụ với một backtest cho thấy win rate 45%, RR trung bình 2.5: `f* = (2.5×0.45 − 0.55) / 2.5 = 0.575/2.5 ≈ 23%`. Ngay cả **quarter-Kelly** (25% của Kelly đầy đủ) cũng đã là ~5.75% — cao hơn 0.5% tới hơn 11 lần.

Vì sao vẫn chọn 0.5% thay vì một con số gần Kelly hơn?

1. **Kelly giả định edge đã biết chính xác và ổn định.** Một discretionary edge (đọc cấu trúc, POI, bias bằng mắt) luôn có sai số ước lượng lớn — win rate và RR thực tế trên forward test gần như luôn khác backtest.
2. **Kelly chấp nhận drawdown ngắn hạn lớn để đổi lấy tăng trưởng dài hạn tối ưu** — điều này hợp lý khi "ruin" là vô hạn (bạn có thể chờ hồi phục). Nhưng prop firm tạo ra một **rào cản ruin nhân tạo và tức thời**: chạm 10% là bị loại ngay lập tức, không quan tâm edge của bạn có thể phục hồi trong 500 lệnh tiếp theo hay không.
3. Vì rào cản này cứng và gần (chỉ vài chục lệnh trong evaluation), bài toán tối ưu không còn là "tối đa hóa tăng trưởng kép dài hạn" mà là "tối thiểu hóa xác suất chạm rào cản trong N lệnh của kỳ đánh giá" — bài toán này đòi hỏi risk **thấp hơn Kelly rất nhiều**, không phải gần Kelly.

0.5% vì vậy không phải là "thận trọng cho có" — nó là lựa chọn có tính toán để edge chưa được xác nhận chắc chắn vẫn sống sót qua sai số ước lượng và variance tự nhiên trong giới hạn cứng của prop firm.

### 5.2. Correlation-adjusted risk & exposure cap

Rủi ro cộng dồn cần được nhìn theo **nhóm tương quan**, không theo từng lệnh riêng lẻ. Quy tắc thực dụng: liệt kê các nhóm correlated chính bạn hay giao dịch (Indices: NAS100/US30/SP500; USD-pairs: EURUSD/GBPUSD/AUDUSD; Metals vs DXY: XAUUSD/XAGUSD nghịch biến với USD) và áp dụng cap: **tổng risk mở đồng thời trong một nhóm correlation > 0.7 không vượt quá 0.5% aggregate**, không phải 0.5% nhân với số lệnh. Nếu hệ thống giao dịch của bạn thực sự cần vào nhiều lệnh trong cùng nhóm, hãy coi chúng như MỘT vị thế duy nhất khi tính size.

### 5.3. Daily & weekly loss limits, circuit breakers

Risk per trade đúng chuẩn (0.5%) là điều kiện cần nhưng chưa đủ — cần thêm các circuit breaker cấp cao hơn:

- **Circuit breaker ngày:** dừng giao dịch ngay khi (a) thua 2 lệnh liên tiếp trong ngày, hoặc (b) equity ngày giảm -1%. Đây là "phanh khẩn cấp" trước khi tilt khiến bạn phá vỡ chính rule 0.5%.
- **Circuit breaker tuần:** nếu tuần đang -2% equity, giảm risk per trade xuống 0.25% cho phần còn lại của tuần hoặc tạm dừng, thay vì cố "gỡ" bằng cách tăng risk.
- Các rule này **phải được viết ra và cam kết trước** khi vào lệnh đầu tiên trong ngày/tuần — quyết định giữa lúc đang thua luôn bị cảm xúc chi phối.

### 5.4. Sizing off backtest — dùng chuỗi thua & drawdown lịch sử của chính bạn

0.5% là điểm khởi đầu hợp lý, nhưng nên được hiệu chỉnh dựa trên dữ liệu backtest thực tế của chính hệ thống (xem `04 - Backtesting`). Nếu backtest cho thấy chuỗi thua dài nhất từng ghi nhận là 8 lệnh liên tiếp, và bạn muốn chuỗi đó (nếu lặp lại) chỉ tiêu tốn tối đa 60% daily loss budget ($500 × 0.6 = $300) làm biên an toàn:

```
risk_max ≈ SafeBudget / LongestLosingStreak = $300 / 8 ≈ $37.5/lệnh ≈ 0.375% equity
```

Con số này **thấp hơn cả 0.5%** — cho thấy 0.5% không phải là mức trần tuyệt đối miễn nhiễm với mọi kịch bản; nếu chuỗi thua thật của hệ thống dài hơn giả định, cần hạ risk thấp hơn nữa hoặc siết chặt circuit breaker thay vì tin tưởng mù quáng vào "0.5% là đủ an toàn".

### 5.5. Mô hình "one good trade" — giảm áp lực tâm lý phải tăng size

Thay vì nghĩ "lệnh này phải thắng để bù cho những lệnh trước", hãy coi **mỗi lệnh là một sự kiện độc lập**, đóng góp một phần nhỏ ($50 ở ví dụ NAS100) vào kỳ vọng dài hạn của toàn bộ hệ thống. Khi tư duy chuyển từ "lệnh này quan trọng" sang "đây chỉ là một trong hàng trăm lệnh good trade tôi sẽ thực hiện", áp lực phải tăng size để "làm cho nó đáng giá" biến mất — đây là cơ chế tâm lý trực tiếp chống lại risk creep và revenge sizing.

### 5.6. Equity-based vs balance-based sizing — vì sao khác biệt với The5ers

- **FTMO 10K:** daily loss limit so với **balance cố định tại đầu ngày** (giờ reset theo server time), không di chuyển trong ngày dù equity thả nổi tăng/giảm. Overall max loss 10% tính trên balance ban đầu của toàn challenge. FTMO còn yêu cầu số ngày giao dịch tối thiểu (minimum trading days) — vi phạm risk không chỉ đe dọa giới hạn loss mà còn có thể khiến bạn "cháy" trước khi đủ điều kiện pass.
- **The5ers 10K:** logic loss limit tham chiếu theo **equity đóng cửa của ngày TRƯỚC** (prior-day closing equity), bao gồm cả floating P/L của các vị thế còn mở khi ngày đóng cửa. Điều này có nghĩa là nếu bạn sizing theo "balance" (chỉ tính P/L đã đóng) thay vì equity thực (bao gồm floating), bạn có thể đang risk nhiều hơn 0.5% thực tế mà không biết — đặc biệt khi giữ lệnh qua đêm. The5ers cũng yêu cầu một số ngày có lãi (mỗi ngày ≥ khoảng 0.5%+), nên risk quá tay một ngày không chỉ đe dọa giới hạn loss mà còn phá hỏng luôn điều kiện "ngày lãi" đó.
- **Bài học chung:** luôn sizing off equity hiện tại (không phải balance cũ hoặc con số "tưởng tượng"), và với The5ers, kiểm tra lại equity thực tế mỗi khi có lệnh giữ qua đêm trước khi tính risk cho ngày mới.

---

## 6. Best Practices

> [!success] Best Practices
> 1. Luôn tính size bằng công thức `PositionSize = (Equity × Risk%) / (StopDistance × ValuePerPoint/Pip)` — không bao giờ áng chừng lot bằng cảm giác.
> 2. Khi SL buộc phải nới rộng, **giảm lot ngay lập tức** để giữ nguyên $ risk — không bao giờ giữ nguyên lot và chấp nhận risk cao hơn.
> 3. Coi các instrument correlation > 0.7 (NAS100/US30, EURUSD/GBPUSD, XAUUSD/DXY) như một nhóm — cap tổng risk nhóm ở 0.5% aggregate, không cộng dồn 0.5% mỗi lệnh.
> 4. Đặt circuit breaker ngày (dừng sau 2 lệnh thua liên tiếp hoặc -1% ngày) và tuần (-2% ngày giảm risk hoặc dừng) **trước** khi vào lệnh đầu tiên.
> 5. Hiệu chỉnh risk dựa trên chuỗi thua dài nhất và max drawdown thực tế từ backtest của chính hệ thống, không chỉ dựa vào con số 0.5% mặc định.
> 6. Sizing luôn theo equity hiện tại (bao gồm floating P/L nếu giữ lệnh qua đêm), đặc biệt quan trọng với The5ers vì loss limit tham chiếu prior-day closing equity.
> 7. Dùng mô hình "one good trade" — mỗi lệnh là một sự kiện độc lập, không phải cơ hội để "gỡ" hay "làm cho đáng giá".
> 8. Không bao giờ tăng size để bù lỗ (revenge sizing) hoặc vì vừa thắng vài lệnh liên tiếp (risk creep) — $ risk luôn cố định theo % equity, bất kể tâm trạng.

---

## 7. Rule phòng tránh & Checklist

- [ ] Tính $ risk và lot size bằng công thức trước khi vào lệnh, không áng chừng.
- [ ] Nếu SL nới rộng hơn kế hoạch, tính lại lot ngay để giữ nguyên $ risk cố định.
- [ ] Kiểm tra correlation trước khi mở lệnh thứ 2 trở lên — nếu > 0.7 với vị thế đang mở, cap tổng risk nhóm ở 0.5%.
- [ ] Không thêm size vào một lệnh đang âm (không trung bình giá).
- [ ] Circuit breaker ngày: dừng sau 2 lệnh thua liên tiếp hoặc equity ngày -1%.
- [ ] Circuit breaker tuần: nếu tuần -2%, hạ risk per trade xuống 0.25% hoặc dừng hẳn.
- [ ] Sizing off equity hiện tại (không phải balance cũ) — đặc biệt kiểm tra lại nếu có lệnh giữ qua đêm (The5ers).
- [ ] Tự hỏi trước khi bấm lệnh: "Đây có phải revenge sizing hay risk creep sau chuỗi thắng không?"

---

## 8. Ví dụ đã xảy ra

- 

*Định dạng liên kết khi có trade thực tế: `[[Loss - NN - Trade YYYY-MM-DD SYMBOL Position]]`*

---

## 9. Flashcards / Active Recall

**Q1:** Viết công thức tính position size và áp dụng cho NAS100 với equity $10,000, risk 0.5%, SL 25 điểm, value/điểm $10 mỗi 1.0 lot.
**A1:** `PositionSize = (Equity × Risk%) / (StopDistance × ValuePerPoint)` = ($10,000 × 0.5%) / (25 × $10) = $50 / $250 = 0.2 lot.

**Q2:** Khi SL phải nới rộng hơn kế hoạch giữa chừng, bạn nên làm gì với lot size?
**A2:** Giảm lot ngay để giữ nguyên $ risk cố định — không bao giờ giữ nguyên lot và chấp nhận $ risk cao hơn.

**Q3:** Vì sao hai lệnh "0.5% mỗi lệnh" trên NAS100 và US30 mở cùng lúc có thể tương đương một lệnh 1%?
**A3:** Vì NAS100 và US30 có correlation cao (0.85-0.95, cùng là chỉ số Mỹ) — khi chúng di chuyển cùng chiều, rủi ro tổng hợp thực tế gần bằng tổng risk của cả hai, không phải hai rủi ro độc lập.

**Q4:** Vì sao 0.5% được coi là cố tình sub-Kelly thay vì gần với Kelly criterion?
**A4:** Vì Kelly giả định edge đã biết chính xác và chấp nhận drawdown ngắn hạn lớn để tối ưu tăng trưởng dài hạn — hợp lý khi ruin không có giới hạn thời gian. Nhưng prop firm tạo rào cản ruin nhân tạo và tức thời (10% = loại ngay), nên bài toán thực tế là tối thiểu hóa xác suất chạm rào cản trong một số lệnh giới hạn của kỳ đánh giá, đòi hỏi risk thấp hơn Kelly rất nhiều.

**Q5:** Khác biệt cốt lõi giữa cách FTMO và The5ers tính loss limit là gì, và nó ảnh hưởng thế nào tới cách bạn sizing?
**A5:** FTMO so daily loss với balance cố định đầu ngày (không đổi trong ngày); The5ers so với equity đóng cửa ngày trước đó (bao gồm floating P/L). Vì vậy với The5ers, phải luôn sizing theo equity thực tế (kể cả floating), đặc biệt khi giữ lệnh qua đêm — sizing theo "balance" cũ có thể khiến bạn risk nhiều hơn 0.5% thực tế mà không biết.

**Q6:** Ở risk 2%/lệnh, cần bao nhiêu lệnh thua liên tiếp để phá vỡ daily loss limit và overall max loss limit của FTMO 10K?
**A6:** Khoảng 3 lệnh thua liên tiếp để phá vỡ daily limit (5% = $500), và khoảng 6 lệnh để phá vỡ overall max loss (10% = $1,000) — so với 0.5% cần tới ~10-11 lệnh (daily) và ~20-21 lệnh (max).

---

## 10. Lesson Learned

Bài học chính: **risk per trade là tham số duy nhất quyết định bạn có còn "trong cuộc chơi" để chờ edge của mình phát huy hay không.** Một chuỗi thua 6-10 lệnh liên tiếp không phải bằng chứng edge sai — đó là variance bình thường mà bất kỳ hệ thống có xác suất nào cũng sẽ gặp. Ở 0.5%, chuỗi đó chỉ là một tuần khó chịu. Ở 2%, chuỗi đó là dấu chấm hết cho challenge, bất kể edge của bạn có tốt đến đâu về lâu dài.

Đối với FTMO và The5ers, 0.5% không phải là sự thận trọng cho có — nó là **tham số để pass challenge**, được tính toán dựa trên chính các giới hạn cứng (daily loss, max loss) mà prop firm áp đặt. Một "lệnh thua tốt" ở 0.5% (đúng kế hoạch, đúng size, đúng correlation cap) luôn tốt hơn một "lệnh thắng may mắn" ở 2% — vì lệnh thắng may mắn ở 2% củng cố sai thói quen sẽ giết tài khoản ở lần thua tiếp theo.

Quy tắc cá nhân:
- [ ] Không bao giờ risk vượt 0.5% equity trên một lệnh, dù conviction cao đến đâu.
- [ ] Luôn tính lại lot khi SL thay đổi — $ risk cố định, lot là biến số phụ thuộc.
- [ ] Cap tổng risk ở 0.5% cho mọi nhóm correlated đang mở đồng thời.

> Một chuỗi thua bình thường chỉ nguy hiểm khi bạn tự biến nó thành bất thường bằng cách tăng risk giữa chừng.

---

## 11. Phân tích chuyên sâu (Deep-Dive)

![[OverRisk-DeepDive-RootCause.svg|760]]
*Sơ đồ: chuỗi 5 Whys từ "risk vượt 0.5%" xuống nguyên nhân gốc, kèm nhánh cơ chế AMD giải thích ai đang thu hoạch thanh khoản của ai.*

### 11.1. Root cause — 5 Whys

| Tầng | Câu hỏi | Câu trả lời |
|---|---|---|
| Bề mặt | Vì sao lệnh này risk 2% thay vì 0.5%? | "Setup chắc ăn quá, tôi tăng size" |
| Why 1 | Vì sao "chắc ăn" lại dẫn tới tăng size? | Vì tôi tin conviction chủ quan có thể thay thế cho công thức position sizing khách quan |
| Why 2 | Vì sao tôi tin conviction thay được công thức? | Vì tôi chưa có dữ liệu backtest cho thấy conviction cao của chính tôi tương quan với win rate cao hơn — tôi đang hành động như thể tương quan đó = 1, trong khi chưa đo bao giờ |
| Why 3 | Vì sao chưa đo mà vẫn tin? | Vì hệ thống chưa bắt buộc ghi log `conviction_score` song song với `outcome` — không có cơ chế phản hồi (feedback loop) để tự sửa niềm tin sai |
| Why 4 | Vì sao chưa có cơ chế ghi log đó? | Vì trọng tâm hiện tại đang dồn vào học framework phân tích (bias, POI, MSS) nhanh hơn tốc độ tích lũy Tier 1 — đúng mô tả tổng quát ở Doctrine v2 §3.1: lý thuyết hoá nhanh hơn tốc độ có dữ liệu |
| **Gốc rễ** | — | **Thiếu một bộ lọc bắt buộc giữa "cảm giác conviction" và "hành động thay đổi risk" — hệ thống hiện tại cho phép cảm xúc bỏ qua công thức mà không có phanh nào ở giữa.** |

Nguyên nhân gốc không phải "tham lam" (đó là nhãn đạo đức, không giúp sửa gì) — nguyên nhân gốc là **thiết kế quy trình thiếu circuit breaker tại đúng điểm quyết định** (giữa lúc nhìn thấy setup và lúc bấm lệnh). Đây là lỗi hệ thống, có thể sửa bằng cách thêm một bước bắt buộc (khai báo lot bằng công thức, dán màn hình, hoặc dùng calculator tự động khoá size tối đa), không chỉ bằng "cố gắng kỷ luật hơn".

### 11.2. Cơ chế vi cấu trúc thị trường (first principles)

Prop firm (FTMO, The5ers) không kiếm tiền chủ yếu từ phí challenge nếu tỷ lệ pass thấp là điều họ mong đợi về mặt mô hình kinh doanh — cấu trúc daily loss/max loss không phải để "bảo vệ trader", nó là **risk management của chính prop firm khi họ đứng ở vị thế cấp vốn cho một dòng lệnh chưa được kiểm chứng**. Về bản chất, khi bạn risk 2%/lệnh, bạn không chỉ đang cược tiền của mình — bạn đang khiến biến động P&L của bạn tiến gần hơn tới ngưỡng mà prop firm coi là "quá rủi ro để tiếp tục cấp vốn", bất kể edge của bạn dương hay âm về dài hạn.

Xét theo khung AMD (Accumulation – Manipulation – Distribution) áp dụng ở cấp độ hành vi trader thay vì hành vi giá: giai đoạn "accumulation" là lúc trader tích luỹ niềm tin sai ("mình đang kiểm soát được risk") qua vài lệnh thắng liên tiếp ở size lớn hơn kế hoạch — không bị phạt ngay vì variance ngắn hạn thuận lợi. Giai đoạn "manipulation" là chuỗi thắng đó tự nó thao túng tâm lý trader tin rằng size lớn hơn là "bình thường mới" (risk creep, xem mục 2). Giai đoạn "distribution" là khi một chuỗi thua thống kê bình thường ập đến đúng lúc size đã bị neo (anchor) ở mức cao — toàn bộ equity tích luỹ được từ giai đoạn accumulation bị phân phối ngược lại cho thị trường (hoặc cụ thể hơn: cho counterparty đã bán thanh khoản đối ứng ở đúng điểm SL bị quét) chỉ trong vài lệnh.

**Ai là counterparty và tiền của ai đang bị thu hoạch?** Không cần đến một "kẻ thao túng" cụ thể — counterparty đơn giản là thanh khoản đối ứng tại điểm SL: khi risk 2% khiến SL của bạn nằm ở một mức giá đủ "hợp lý" về mặt kỹ thuật để nhiều trader retail khác cũng đặt SL gần đó, cụm SL này trở thành một pool thanh khoản bị quét bởi displacement thật đi ngược hướng — tiền bị thu hoạch chính là excess risk bạn tự thêm vào, không phải "thị trường ghét bạn". **Thời điểm trong chu kỳ:** rủi ro cao nhất luôn nằm ở đoạn chuyển giao từ accumulation (chuỗi thắng ru ngủ) sang distribution (chuỗi thua thống kê bình thường ập tới) — đúng lúc size đã bị neo cao nhất.

### 11.3. Phân tích định lượng

> [!warning] Số liệu minh họa
> Toàn bộ số liệu dưới đây là **mô phỏng minh họa** với giả định winrate/RR hợp lý cho một discretionary edge ICT 2022 chưa kiểm chứng — cần thay bằng số backtest thật (Tier 1, n≥20) của chính trader trước khi dùng để ra quyết định risk thật.

**Expectancy trước/sau khi mắc lỗi** (giả định winrate 45%, RR trung bình 2.2, equity $10,000):

| Kịch bản | Risk/lệnh | $ risk | Expectancy/lệnh ($) | Expectancy/lệnh (theo % equity) |
|---|---|---|---|---|
| Tuân thủ đúng | 0.5% | $50 | (0.45×2.2×50) − (0.55×50) = 49.5 − 27.5 = **+$22** | +0.22% |
| Lỗi nhẹ (risk creep) | 1% | $100 | (0.45×2.2×100) − (0.55×100) = 99 − 55 = **+$44** | +0.44% |
| Lỗi nặng (oversized) | 2% | $200 | (0.45×2.2×200) − (0.55×200) = 198 − 110 = **+$88** | +0.44% |

Điểm mấu chốt: **expectancy theo % equity không đổi khi tăng risk tuyến tính** (giả định winrate/RR không đổi) — vấn đề không nằm ở kỳ vọng trung bình, mà ở **phương sai (variance) và xác suất chạm rào cản cứng** (xem bảng equity-curve ở mục 3), thứ mà công thức expectancy đơn thuần không thể hiện. Đây là lý do một trader mới thường lý luận sai: "risk cao hơn thì kiếm nhiều hơn, toán học ủng hộ tôi" — đúng về kỳ vọng điểm, sai về xác suất sống sót qua rào cản.

**Độ nhạy — lỗi xuất hiện 10%/25%/50% số lệnh:** giả định 100 lệnh trong một kỳ, mỗi lệnh vi phạm risk trung bình gấp 3 lần kế hoạch (0.5% → 1.5%) khi xảy ra:

| Tần suất lỗi | Số lệnh vi phạm /100 | Risk trung bình toàn kỳ | Xác suất ước tính chạm max loss 10% trong kỳ (minh họa, mô phỏng Monte Carlo giản lược) |
|---|---|---|---|
| 10% số lệnh | 10 lệnh | ~0.6% | ~8-12% |
| 25% số lệnh | 25 lệnh | ~0.75% | ~20-28% |
| 50% số lệnh | 50 lệnh | ~1.0% | ~40-55% |

*Ghi chú: cột xác suất là ước tính định hướng dựa trên logic random-walk drawdown, KHÔNG phải kết quả mô phỏng chạy thật — cần chạy Monte Carlo thật với đúng phân phối RR/winrate của trader để có con số chính xác.* Xu hướng quan trọng hơn con số tuyệt đối: xác suất chạm rào cản **tăng nhanh hơn tuyến tính** khi tần suất vi phạm tăng, vì các lệnh risk cao có xác suất rơi vào đúng chuỗi thua ngẫu nhiên không hề giảm đi.

**Chi phí kép khi risk-vượt đi cùng mistake khác:** nếu lỗi này xảy ra đồng thời với [[01-Mistake-Emotional-revenge-trade]] (revenge sizing sau thua) — hai lỗi không cộng dồn tuyến tính mà **nhân với nhau**: revenge trade thường đi kèm entry vội (bỏ qua checklist sweep/MSS/FVG) nên winrate của riêng nhóm lệnh này thấp hơn baseline (giả định 30% thay vì 45%) VÀ risk cao hơn (2% thay vì 0.5%) cùng lúc — expectancy của tổ hợp này thường **âm rõ rệt**, không chỉ "kém hơn một chút":

```
Expectancy_tổ_hợp = (0.30 × 2.2 × 200) − (0.70 × 200) = 132 − 140 = −$8/lệnh (âm)
```

### 11.4. Taxonomy các biến thể con

1. **"Conviction override"** — mô tả: tăng size vì cảm giác chủ quan setup đẹp bất thường. Dấu hiệu phân biệt: không có log `conviction_score` định lượng trước khi vào lệnh, chỉ có mô tả cảm tính sau khi vào. Mức nguy hiểm: **Cao** — dễ tái diễn vì được củng cố bởi các lần thắng ngẫu nhiên.
2. **"Stealth SL creep"** — mô tả: SL bị nới rộng dần qua nhiều lần chỉnh sửa nhỏ (5 điểm, rồi thêm 5 điểm nữa) mà không tính lại lot ở mỗi lần chỉnh — mỗi lần chỉnh riêng lẻ "trông không đáng kể" nhưng cộng dồn vượt xa 0.5% ban đầu. Dấu hiệu: nhiều lần sửa SL trong lịch sử lệnh (broker log) mà không có log lot tương ứng. Mức nguy hiểm: **Cao** — đây là biến thể "ngụy trang" khó nhận ra nhất vì mỗi bước đơn lẻ có vẻ vô hại.
3. **"Correlation blindness"** — mô tả: mở nhiều lệnh đúng 0.5%/lệnh về mặt kỹ thuật nhưng không kiểm tra correlation, tự tin rằng "tôi tuân thủ rule". Dấu hiệu: nhiều lệnh mở đồng thời trên các symbol có hệ số tương quan > 0.7 chưa từng được tính gộp. Mức nguy hiểm: **Trung bình-cao** — dễ bị bỏ qua vì mỗi lệnh riêng lẻ "đúng luật".
4. **"Time-diluted revenge"** — mô tả: không tăng size ngay sau lệnh thua (để tránh bị tự nhận ra là revenge trade), nhưng tăng size dần qua vài lệnh tiếp theo trong cùng ngày với lý do "gỡ lại từ từ". Dấu hiệu: risk trung bình trong ngày tăng dần sau một lệnh thua đầu ngày dù không có lệnh nào đơn lẻ vượt 1%. Mức nguy hiểm: **Trung bình** — khó phát hiện vì phân tán qua nhiều lệnh, chỉ lộ ra khi tổng hợp theo ngày.
5. **"Backtest-confidence transfer"** — mô tả: dùng kết quả backtest tốt (n nhỏ, Tier 0/1 sơ khai) để biện minh cho risk cao hơn trên tài khoản live/challenge, trong khi backtest chưa đạt Tier 1 thật (n≥20, đã tính spread/slippage/tâm lý thật). Dấu hiệu: risk % tăng đột ngột ngay sau một giai đoạn backtest có kết quả đẹp. Mức nguy hiểm: **Cao** — đây là biến thể tinh vi nhất vì được ngụy trang bằng vẻ ngoài "có dữ liệu ủng hộ".

### 11.5. Ma trận tương tác với mistake khác

| Mistake liên quan | Cơ chế khuếch đại lẫn nhau | Mức nguy hiểm tổ hợp |
|---|---|---|
| [[01-Mistake-Emotional-revenge-trade]] | Revenge sizing (tăng risk) + entry vội bỏ qua checklist → winrate giảm VÀ risk tăng cùng lúc, expectancy có thể âm hẳn (xem 11.3) | **Rất cao — tổ hợp nguy hiểm nhất** |
| [[05-Mistake-Not-enough-RR]] | RR thấp làm expectancy vốn đã mỏng ở 0.5%; nếu risk vượt lên 1-2% với RR thấp, một chuỗi thua ngắn cũng đủ chạm daily loss vì mỗi lệnh thua "ăn" nhiều hơn mà mỗi lệnh thắng bù lại ít hơn | Cao |
| [[09-Mistake-Wrong-daily-bias]] | Bias sai tạo cụm lệnh thua tương quan trong cùng phiên (theo mô tả ở chính note 09, mục 3) — nếu risk mỗi lệnh trong cụm đó đã vượt 0.5%, chuỗi 2-3 lệnh thua cùng gốc bias sai có thể chạm daily loss limit chỉ trong một buổi sáng | **Rất cao** |
| [[02-Mistake-Enter-before-liquidity-sweep]] | Entry sớm (trước sweep) thường có SL đặt sai vị trí cấu trúc (quá gần hoặc quá xa) — trader dễ "bù" bằng cách không tính lại size đúng cách khi SL thực tế khác kế hoạch | Trung bình-cao |

> [!question] Tổ hợp nguy hiểm nhất
> **Wrong daily bias + Risk vượt 0.5%** là tổ hợp có khả năng phá tài khoản nhanh nhất trong một buổi sáng duy nhất: bias sai tạo ra 2-3 tín hiệu entry "sách vở" liên tiếp cùng hướng sai (không phải lỗi ngẫu nhiên độc lập — cùng một nguyên nhân gốc), và nếu mỗi lệnh trong chuỗi đó đã risk 1-2% thay vì 0.5%, daily loss limit có thể bị chạm chỉ với 2-3 lệnh trong một phiên London/NY duy nhất.

---

## 12. Debate — Tranh biện hai chiều

![[OverRisk-Debate-Map.svg|760]]
*Sơ đồ: bản đồ tranh biện "0.5%/lệnh" — luận điểm ủng hộ vs phản đối, phản hồi chéo, và phán quyết có điều kiện gắn với Evidence Tier hiện tại.*

**Kiến nghị (Motion):** *"Mọi lệnh vượt quá 0.5% risk/equity, không có ngoại lệ nào (kể cả conviction cao, kể cả backtest đẹp), đều phải bị cấm tuyệt đối trong suốt giai đoạn challenge và ít nhất 6 tháng đầu trading live."*

### Phe Ủng hộ (giữ rule cứng)

1. **Toán học rào cản cứng của prop firm không khoan nhượng.** Như bảng ở mục 3 cho thấy, ở 2% risk chỉ cần 3 lệnh thua liên tiếp để chạm daily loss và 6 lệnh để chạm max loss — đây là xác suất thống kê bình thường (không phải kịch bản hiếm), nên "ngoại lệ cho conviction cao" thực chất là đặt cược vào việc lệnh đó không rơi vào 45-55% xác suất thua, một cược không có cơ sở edge nào hỗ trợ.
2. **Discretionary edge chưa kiểm chứng (Tier 0) không đủ cơ sở để tự tin chọn "lệnh nào đáng risk cao hơn".** Nếu trader thực sự có khả năng phân biệt lệnh conviction cao có winrate cao hơn, khả năng đó bản thân nó phải được đo bằng dữ liệu (ví dụ tương quan `conviction_score` với `outcome` trên ≥20 mẫu) trước khi được tin — chưa có dữ liệu này trong toàn bộ hệ thống hiện tại.
3. **Chi phí của việc phá rule một lần luôn không đối xứng với lợi ích.** Một lần risk 2% thắng chỉ mang lại thêm 1.5% equity so với 0.5%; một lần risk 2% thua trong đúng lúc gặp chuỗi thua có thể chấm dứt toàn bộ challenge (chi phí = 100% phí challenge + toàn bộ thời gian đã đầu tư) — bất đối xứng risk/reward rất rõ ràng nghiêng về phía giữ rule cứng.
4. **Rule cứng loại bỏ hoàn toàn một bậc quyết định dễ bị cảm xúc thao túng.** Nếu "conviction cao" được phép là lý do hợp lệ để tăng risk, mọi lệnh thua sau đó đều có thể được biện minh ngược "lúc đó tôi tin nó cao" — rule không có ngoại lệ giúp loại bỏ hoàn toàn kẽ hở biện minh này.

### Phe Phản đối (rule nên mềm/có ngoại lệ)

1. **Chi phí cơ hội thật và có thể đo được.** Nếu một trader thực sự có khả năng phân biệt setup A+ (đầy đủ mọi điều kiện: bias Tier A, sweep sạch, displacement mạnh, MSS + FVG hợp lưu) với setup B trung bình, risk cố định 0.5% cho cả hai đồng nghĩa với việc "lãng phí" edge thật ở đúng những lệnh có xác suất thắng cao nhất — một số trường phái risk management chuyên nghiệp (ví dụ mô hình "confidence-weighted sizing" trong một số quỹ prop) thực sự scale size theo độ tin cậy setup, không cố định tuyệt đối.
2. **Overfit trên sample nhỏ theo đúng chiều ngược lại.** Chính con số "0.5%" trong note này cũng chưa từng được kiểm định trên dữ liệu thật của trader (đúng tinh thần Doctrine v2 §3.1: mọi rule hiện tại là Tier 0/1 sơ khai) — nếu 0.5% chính nó là một con số tùy ý (xem Devil's Advocate mục 13), thì việc áp đặt nó "tuyệt đối, không ngoại lệ" là đang cứng nhắc hoá một giả thuyết chưa kiểm chứng, mâu thuẫn ngay trong logic của chính lập luận ủng hộ #2.
3. **Các trader/trường phái nổi tiếng dùng position sizing biến thiên thành công.** Turtle Traders (Richard Dennis/William Eckhardt) dùng công thức N (ATR-based) với risk % biến thiên theo volatility và tín hiệu; nhiều CTA (Commodity Trading Advisor) chuyên nghiệp dùng volatility-scaled sizing thay vì % cố định tuyệt đối — cho thấy "0.5% cố định cho mọi lệnh" không phải chuẩn mực duy nhất của risk management chuyên nghiệp, dù các hệ thống đó thường có backtest quy mô lớn hơn hẳn (n hàng nghìn) hỗ trợ.
4. **Điều kiện thị trường nơi rule phản tác dụng: giai đoạn cần xây confidence/kỹ năng đọc bối cảnh.** Rule cứng "không bao giờ vượt 0.5%" có thể khiến trader không bao giờ trải nghiệm cảm giác thực của một lệnh size lớn hơn trong môi trường kiểm soát (ví dụ demo/backtest), làm chậm quá trình học cách quản lý tâm lý ở size cao hơn — kỹ năng này vẫn cần được rèn luyện ở đâu đó trước khi lên tài khoản live thật với size lớn.

### Vòng phản hồi chéo

**Vòng 1:**
- *Ủng hộ đáp Phản đối #1 (confidence-weighted sizing):* Ngay cả các quỹ dùng confidence-weighted sizing đều xây trên hàng trăm/nghìn mẫu dữ liệu đã đo lường được tương quan conviction–outcome thật; áp dụng ý tưởng này khi n=0 mẫu đã đo là copy hình thức mà không có nội dung thống kê đứng sau — đây chính là cơ sở của [[EURUSD H1→M15]] case ở Doctrine v2 §5.1 về gate cứng vs mềm: một điều kiện chỉ nên "mềm hoá" khi có dữ liệu chứng minh việc mềm hoá đó không làm tăng rủi ro ruin.
- *Phản đối đáp Ủng hộ #2 (Tier 0 chưa đủ cơ sở):* Đúng là chưa có dữ liệu, nhưng điều đó cũng áp dụng ngược lại cho chính con số "0.5%" — nếu tiêu chuẩn là "không hành động khi chưa có Tier 1", thì cả hai phía (risk cố định 0.5% VÀ risk biến thiên theo conviction) đều đang hành động trên giả thuyết, chỉ khác nhau ở việc một bên thận trọng hơn về mặt hậu quả xấu nhất (downside), không phải về mặt bằng chứng.

**Vòng 2:**
- *Ủng hộ đáp lại:* Chấp nhận cả hai đều là giả thuyết Tier 0, nhưng bài toán không đối xứng — sai lầm loại 1 (risk quá thấp) chỉ có chi phí cơ hội (tăng trưởng chậm hơn), có thể sửa sau khi có Tier 1; sai lầm loại 2 (risk quá cao) có chi phí không thể đảo ngược (mất challenge, phải mua lại). Khi không chắc chắn, nguyên tắc quản trị rủi ro chuẩn là chọn nhánh có sai lầm ít tốn kém hơn để sửa — đây chính là lý do chọn 0.5% dù chưa tối ưu.
- *Phản đối đáp lại:* Đồng ý về tính bất đối xứng của hậu quả, nhưng điều đó chỉ ủng hộ "risk thấp trong giai đoạn challenge/early live" — nó không chứng minh được "0.5% mãi mãi, kể cả sau khi đã có Tier 1 xác nhận edge thật và equity đã lớn hơn nhiều so với ngưỡng ruin ban đầu". Rule "tuyệt đối, không bao giờ" đi xa hơn mức bằng chứng bất đối xứng có thể biện minh.

### Phán quyết & tổng hợp

Ở **Evidence Tier hiện tại (Tier 0 — giả thuyết, dựa trên lý thuyết Kelly/risk-of-ruin, chưa có backtest thật của chính trader)**, phe Ủng hộ đúng cho giai đoạn challenge và ít nhất giai đoạn đầu live: bất đối xứng hậu quả (mất challenge không đảo ngược được vs tăng trưởng chậm có thể bù sau) đủ mạnh để biện minh một rule gần-cứng trong giai đoạn này — ngôn ngữ đúng phải là "giả thuyết đang được áp dụng như chính sách phòng ngừa thận trọng", **chưa được phép nói "đây là doctrine đã kiểm chứng"**.

Phe Phản đối đúng về mặt dài hạn có điều kiện: MỘT KHI trader đã tích lũy Tier 1 thật (n≥20 lệnh log đầy đủ, đo được tương quan giữa `conviction_score` và `outcome`) VÀ đã vượt qua challenge (không còn rào cản ruin nhân tạo tức thời), việc xem xét scale size nhẹ theo tier bias/setup quality (xem [[09-Mistake-Wrong-daily-bias]] mục 5.1 — Bias Tier A/B/C đã có sẵn cơ chế này) là hợp lý và không mâu thuẫn với tinh thần risk management, miễn là vẫn có trần tuyệt đối (ví dụ không bao giờ vượt 1% dù tier cao nhất).

**Dữ liệu nào sẽ giải quyết được cuộc tranh biện:** (1) chạy ≥30 lệnh với `conviction_score` (thang 1-5) ghi TRƯỚC entry và đối chiếu với `outcome`/R-multiple thật — nếu tương quan Spearman > 0.3 và có ý nghĩa thống kê, ủng hộ việc cân nhắc scale nhẹ theo conviction đã đo được (không phải cảm tính); (2) tính maximum drawdown thật từ ≥30 lệnh ở 0.5% cố định — nếu drawdown thật thấp hơn nhiều so với ngưỡng breach, có dư địa để xem xét nới nhẹ; nếu bằng hoặc gần ngưỡng, giữ nguyên hoặc hạ thấp hơn 0.5% (đúng logic mục 5.4 của note gốc).

---

## 13. Devil's Advocate — Phản biện gay gắt

1. **Đòn tấn công:** "0.5% là một con số tùy ý, chưa từng được tối ưu hoá cho chính hệ thống của bạn — nó có thể quá thấp HOẶC quá cao tùy vào edge thật, và bạn không biết cái nào vì chưa đo."
   **Cơ sở của đòn tấn công:** Toàn bộ lập luận trong note (Kelly, risk-of-ruin, bảng equity curve) dùng winrate/RR **giả định** (45%, RR 2.2-2.5), không phải số thật của trader. Nếu winrate thật của hệ thống là 60% với RR 1.5 thay vì 45%/2.2, cả bài toán Kelly lẫn bảng drawdown đều cho ra kết luận khác — có thể 0.5% quá thận trọng so với edge thật, làm chậm tăng trưởng không cần thiết.
   **Phản bác trung thực:** Đúng — đây là điểm yếu thật. Note không có cách nào biết winrate/RR thật nếu chưa backtest. Phần **KHÔNG đáp được**: không có lý do logic nào để tin 0.5% (thay vì 0.3% hay 0.8%) là con số tối ưu cho MỌI hệ thống ICT 2022 — nó là điểm khởi đầu an toàn theo tiêu chuẩn ngành, không phải kết quả tối ưu hoá.
   **Falsification test:** Chạy backtest Tier 1 (n≥30) đo winrate thật + RR trung bình thật → tính Kelly criterion thật → so sánh quarter-Kelly với 0.5%. Nếu quarter-Kelly thật < 0.5%, 0.5% đang quá cao (rủi ro hơn tưởng); nếu quarter-Kelly thật > 1%, có cơ sở cân nhắc nới risk (dù vẫn cần cân nhắc rào cản ruin nhân tạo của prop firm, mục 11.2 5.1).

2. **Đòn tấn công:** "Bảng equity-curve ở mục 3 là một phép tính xác định (deterministic) giả định chuỗi thua LIÊN TỤC — nhưng thực tế không ai gặp đúng kịch bản 'thua N lệnh liên tiếp không xen kẽ thắng nào'; bảng này thổi phồng rủi ro thật để biện minh cho rule."
   **Cơ sở của đòn tấn công:** Đúng về mặt kỹ thuật — bảng equity curve trong note tính theo kịch bản "N lệnh thua liên tiếp không gián đoạn", đây là kịch bản xấu nhất (worst-case), không phải kịch bản kỳ vọng (expected case) khi có winrate 45-50%.
   **Phản bác trung thực:** Đây chính là **mục đích của bảng** — nó không cố mô tả kịch bản trung bình, mà cố trả lời câu hỏi "nếu kịch bản xấu (nhưng hoàn toàn có xác suất xảy ra thật, không phải giả tưởng) ập tới, tôi còn sống không". Risk management chuẩn luôn stress-test bằng worst-case hợp lý, không phải expected-case — đây không phải điểm yếu, đó là đúng phương pháp luận risk. Tuy nhiên phần **thừa nhận:** note chưa tính xác suất THẬT của việc gặp đúng chuỗi N-thua-liên-tiếp đó trong một kỳ challenge cụ thể (ví dụ 30 ngày giao dịch) — chỉ có bảng hệ quả NẾU nó xảy ra, thiếu bảng xác suất NÓ SẼ xảy ra.
   **Falsification test:** Chạy mô phỏng Monte Carlo với winrate/RR thật, N lệnh/ngày thật, số ngày challenge thật → đo phân phối xác suất drawdown tối đa trong kỳ. Nếu xác suất chạm max loss ở 0.5% dưới 5%, rule 0.5% có cơ sở thống kê vững; nếu vẫn trên 15-20% dù ở 0.5%, vấn đề không nằm ở risk % mà nằm ở edge (winrate/RR) chưa đủ tốt — hạ risk thêm nữa không giải quyết được gốc rễ.

3. **Đòn tấn công:** "Ví dụ 'Đúng/Sai' ở mục 4 bị hindsight bias — viết SAU khi biết kết quả, nên câu chuyện tự động khớp với bài học muốn dạy; không có ví dụ nào cho thấy trường hợp tuân thủ 0.5% vẫn thua đau."
   **Cơ sở của đòn tấn công:** Đúng — ví dụ "❌ Sai" mô tả một chuỗi sự kiện (SL nới rộng + correlated exposure + risk 2%) mà MỌI yếu tố đều xấu cùng lúc, một kịch bản "quá hoàn hảo" để minh họa bài học, giống mô tả về war stories illustrative ở Doctrine v2 §3.4 — nguy cơ note tạo cảm giác "tôi đã học bài học này từ kinh nghiệm" trong khi đây thuần là kịch bản dựng sẵn.
   **Phản bác trung thực:** Ghi nhận đúng — mục 4 của note gốc không gắn nhãn rõ ràng "đây là composite/illustrative, không phải log thật" theo đúng chuẩn Doctrine v2 §3.4. Đây là khoảng trống có thật, cần bổ sung (xem Case Studies mục 15 bên dưới đã tuân thủ ghi chú này).
   **Falsification test:** Không phải một test số liệu — mà là một audit định dạng: rà soát toàn bộ ví dụ minh họa trong note gốc (mục 4), nếu không có nhãn `illustrative` tường minh, coi như CHƯA đạt chuẩn Doctrine v2 và cần bổ sung callout xác nhận.

4. **Đòn tấn công:** "Rule cứng 0.5% là cách né tránh việc học kỹ năng đánh giá conviction thật — thay vì học cách phân biệt setup tốt/xấu bằng dữ liệu, trader chỉ đơn giản trốn vào một con số cố định."
   **Cơ sở của đòn tấn công:** Có phần đúng về mặt tâm lý học kỹ năng: nếu không bao giờ thử nghiệm scale size theo conviction (ngay cả trong môi trường kiểm soát như backtest/demo), trader không bao giờ xây dựng được calibration — khả năng tự đánh giá đúng mức độ tin cậy của chính mình, một kỹ năng meta-cognitive quan trọng trong trading chuyên nghiệp.
   **Phản bác trung thực:** Phản bác được một phần: rule 0.5% chỉ áp dụng cho **risk thật trên tài khoản live/challenge** — không có gì ngăn cản trader luyện tập calibration trên backtest/demo (ghi `conviction_score` dự đoán TRƯỚC, so với outcome sau, không risk tiền thật). Phần **không đáp được:** đúng là nếu trader chỉ tuân thủ 0.5% một cách máy móc mà không song song xây dựng và đo lường khả năng calibration ở nơi an toàn, kỹ năng đó thực sự không phát triển — rule cứng không tự động dạy kỹ năng, nó chỉ ngăn thiệt hại trong lúc chưa có kỹ năng.
   **Falsification test:** Theo dõi `conviction_score` (ghi trước) vs `outcome` (biết sau) trên backtest/demo qua ≥30 mẫu. Nếu correlation gần 0 → trader chưa có calibration thật, rule cứng 0.5% là bảo vệ cần thiết. Nếu correlation rõ ràng dương và ổn định qua ≥2 giai đoạn thị trường khác nhau → có cơ sở Tier 2 để cân nhắc nới rule.

5. **Đòn tấn công:** "Định nghĩa 'correlation > 0.7' để cap risk nhóm là mơ hồ đến mức không falsifiable trong thực chiến — trader không có công cụ tính correlation real-time giữa NAS100/US30 tại đúng thời điểm vào lệnh, nên rule này chỉ tồn tại trên giấy."
   **Cơ sở của đòn tấn công:** Đúng về mặt thực dụng — correlation là một con số thống kê tính trên cửa sổ thời gian (rolling window) nào đó (30 ngày? 90 ngày? intraday?) mà note không chỉ rõ, và hầu hết trader retail không có bảng correlation matrix cập nhật real-time trong lúc ra quyết định trong vài giây.
   **Phản bác trung thực:** Một phần đáp được: với các cặp "hiển nhiên" (NAS100/US30 cùng là chỉ số Mỹ, EURUSD/GBPUSD cùng chân USD), không cần tính số chính xác — kiến thức nền (domain knowledge) đã đủ để biết chúng tương quan cao mà không cần công cụ. Phần **không đáp được:** với các cặp ít hiển nhiên hơn (ví dụ XAUUSD và một chỉ số châu Á), rule "> 0.7" hoàn toàn không thực thi được nếu không có công cụ đo, và note không cung cấp danh sách đầy đủ các cặp cần cap, chỉ có 3 ví dụ mẫu.
   **Falsification test:** Xây một bảng correlation tĩnh (cập nhật hàng tháng, không cần real-time) cho các cặp instrument trader thực sự giao dịch — nếu bảng này không tồn tại trong vòng 1 tháng tới sau khi đọc note, rule "cap correlation" là rule chỉ tồn tại trên giấy, cần hạ xuống thành "quy tắc mềm: tự nhận biết trực giác các cặp hiển nhiên" thay vì con số "> 0.7" giả vờ chính xác.

**Bảng tổng hợp — đòn nào note hiện tại CHƯA đỡ được:**

| # | Đòn tấn công | Đỡ được? | Việc cần làm |
|---|---|---|---|
| 1 | 0.5% là số tùy ý, chưa tối ưu cho edge thật | Không đỡ được hoàn toàn | Chạy Tier 1 backtest để tính Kelly thật, so sánh với 0.5% |
| 2 | Bảng equity-curve là worst-case, chưa có bảng xác suất thật | Đỡ được một phần | Chạy Monte Carlo với thông số thật thay vì chỉ bảng hệ quả xác định |
| 3 | Ví dụ minh họa có hindsight bias, chưa gắn nhãn illustrative | Không đỡ được | Gắn nhãn "kịch bản minh họa" rõ ràng cho mọi ví dụ trong mục 4 (đã bổ sung ở mục 15 dưới đây) |
| 4 | Rule cứng né tránh học kỹ năng calibration | Đỡ được một phần | Thêm bài tập calibration trên backtest/demo song song với rule cứng trên live |
| 5 | "Correlation > 0.7" không falsifiable trong thực chiến | Không đỡ được | Xây bảng correlation tĩnh cụ thể cho danh mục instrument hay giao dịch |

---

## 14. Audit — Khung kiểm toán độc lập

![[OverRisk-Audit-Framework.svg|760]]
*Sơ đồ: pipeline audit risk-per-trade — log đủ field → bộ câu hỏi PASS/FAIL → rubric A/B/C/F → hành động, kèm khối red flags.*

### 14.1. Mục tiêu & phạm vi audit

Audit hành vi **sizing quyết định tại thời điểm vào lệnh** (không audit chất lượng phân tích bias/POI — đó thuộc phạm vi các note khác), trên dữ liệu: trade log broker (entry/SL/lot thật) đối chiếu với kế hoạch đã ghi trước (nếu có) và frontmatter trade note trong vault.

### 14.2. Trường dữ liệu bắt buộc trong log

- `planned_risk_pct` — % risk đã tính trước khi vào lệnh (theo công thức)
- `actual_risk_pct` — % risk thực tế đã chấp nhận (tính lại từ SL thật × lot thật ÷ equity)
- `sl_distance_planned` / `sl_distance_actual` — khoảng cách SL kế hoạch vs thực tế
- `lot_recalculated_after_sl_change` — có/không, đã tính lại lot khi SL đổi chưa
- `concurrent_positions_correlation_group` — nhãn nhóm correlation nếu có ≥2 lệnh mở đồng thời
- `conviction_score` (1-5) — ghi TRƯỚC khi vào lệnh, không được điền hồi tố sau khi biết kết quả
- `circuit_breaker_active` — có/không, ngày/tuần đó circuit breaker có đang kích hoạt không
- `screenshot_pre_entry` — ảnh chụp màn hình tính toán lot TRƯỚC khi bấm lệnh
- Không log đủ các field trên = **không audit được = tự động FAIL**, bất kể kết quả lệnh thắng hay thua.

### 14.3. Bộ câu hỏi audit

| # | Câu hỏi | Tiêu chí PASS |
|---|---|---|
| 1 | `actual_risk_pct` có ≤ 0.5% không? | PASS nếu ≤0.5%, đo trực tiếp từ log |
| 2 | `planned_risk_pct` và `actual_risk_pct` có khớp nhau (chênh ≤0.05%) không? | PASS nếu khớp, cho thấy không có "trôi" risk giữa kế hoạch và thực thi |
| 3 | Nếu SL thực tế khác kế hoạch, `lot_recalculated_after_sl_change` = có? | PASS nếu có, hoặc SL không đổi |
| 4 | Nếu có ≥2 lệnh đồng thời cùng nhóm correlation, tổng risk nhóm ≤0.5%? | PASS nếu tổng ≤0.5% hoặc không có nhóm correlated mở đồng thời |
| 5 | `conviction_score` được ghi TRƯỚC entry (có timestamp/screenshot xác nhận)? | PASS nếu có bằng chứng ghi trước, FAIL nếu chỉ có ghi chú mơ hồ sau |
| 6 | Lệnh có phải revenge sizing (risk tăng ngay sau lệnh thua liền trước, không có lý do cấu trúc mới) không? | PASS nếu không phải, FAIL nếu risk tăng bất thường sau thua |
| 7 | Circuit breaker ngày (2 lệnh thua liên tiếp / -1% ngày) có được tuân thủ nếu đã kích hoạt? | PASS nếu tuân thủ dừng, FAIL nếu vẫn vào thêm lệnh |
| 8 | Circuit breaker tuần (-2% → hạ risk 0.25%) có được áp dụng đúng tuần đó? | PASS nếu đúng, FAIL nếu bỏ qua |
| 9 | Sizing có dùng equity hiện tại (không phải balance cũ), đặc biệt với lệnh giữ qua đêm (The5ers)? | PASS nếu đúng equity thời điểm tính |
| 10 | Có `screenshot_pre_entry` xác nhận phép tính lot trước khi bấm lệnh không? | PASS nếu có ảnh/log rõ ràng |
| 11 | Nếu risk vượt 0.5% xảy ra, có được ghi nhận NGAY trong log (không chờ bị phát hiện khi audit) không? | PASS nếu tự ghi nhận minh bạch, FAIL nếu chỉ lộ ra khi đối chiếu broker log |
| 12 | Tần suất vi phạm risk trong 20 lệnh gần nhất có dưới 10% không? | PASS nếu <10% (2/20), cảnh báo nếu 10-25%, FAIL nếu >25% |

### 14.4. Rubric chấm điểm

| Hạng | Số câu PASS /12 | Ý nghĩa | Ngưỡng hành động |
|---|---|---|---|
| **A** | 11-12 | Kỷ luật risk vững, hệ thống hoá tốt | Tiếp tục, có thể cân nhắc thu thập dữ liệu Tier 1 để xem xét tối ưu (không nới risk ngay) |
| **B** | 8-10 | Có vi phạm nhưng không hệ thống | Xác định câu FAIL cụ thể, thêm 1 circuit breaker bổ sung tại đúng điểm yếu |
| **C** | 5-7 | Vi phạm mang tính lặp lại, có mẫu hình | Tạm dừng size lớn hơn 0.3%, quay lại backtest/demo để rèn calibration trước khi live tiếp |
| **F** | 0-4 | Hệ thống risk gần như không tồn tại trên thực tế | **Cấm trade live ngay lập tức**, quay lại backtest, không được mở lại tài khoản live/challenge cho tới khi đạt tối thiểu hạng B trên ≥20 lệnh demo liên tiếp |

### 14.5. Red flags khi audit

- **Sửa log sau khi biết kết quả:** `conviction_score` hoặc ghi chú "tôi cảm thấy chắc" chỉ xuất hiện SAU khi lệnh đã thắng — không có timestamp/screenshot trước entry để xác minh.
- **Chỉ log lệnh đẹp:** trade log có khoảng trống bất thường quanh các lệnh thua lớn hoặc vi phạm risk — dấu hiệu chọn lọc (selective logging).
- **Định nghĩa xê dịch theo kết quả:** gọi một lệnh là "conviction cao nên risk 1%" khi thắng, nhưng gọi lệnh risk 1% khác là "một lần lỡ tay" khi thua — cùng hành vi, hai cách gọi tên khác nhau tùy kết quả.
- **"Quên" tính correlation** đúng vào những ngày có ≥2 lệnh cùng thắng lớn — correlation chỉ được nhắc tới khi nó gây thua, không khi nó gây thắng kép.
- **Circuit breaker bị "diễn giải lại"** giữa lúc đang thua ("chỉ 1.8% chưa tới -2% nên chưa cần dừng" trong khi số liệu thật là -2.1%).

### 14.6. Meta-audit chính note này

Tự kiểm toán note gốc theo chuẩn Doctrine v2: **Evidence Tier hiện tại của note = Tier 0** cho hầu hết các con số cụ thể (winrate 45-50%, RR 2.2-2.5, Kelly 23%) — đây là giả định hợp lý dựa trên benchmark ngành, KHÔNG phải số đo từ chính trader. **Sample size:** 0 lệnh thật được dẫn chứng trong note gốc cho riêng chủ đề risk-per-trade (mục 8 "Ví dụ đã xảy ra" đang để trống). **Điểm đang khẳng định vượt quá bằng chứng:** câu "0.5% ... là tham số được tính toán" (callout đầu note) dùng giọng điệu chắc chắn (`[!danger]`) cho một con số thực chất là benchmark ngành áp dụng chung, chưa được tối ưu riêng cho hệ thống của trader — nên hạ giọng thành "0.5% là điểm khởi đầu thận trọng dựa trên tính toán rào cản prop firm, cần hiệu chỉnh khi có Tier 1". **Cần dữ liệu gì để nâng tier:** ≥20 lệnh backtest log đầy đủ (winrate, RR, MAE thật) để thay các con số giả định bằng số thật, và ≥20 lệnh forward test/demo để xác nhận drawdown thật khớp với dự đoán mô hình.

### 14.7. Nhịp audit

- **Hàng ngày:** tự chấm nhanh 3 câu hỏi cốt lõi (risk thực ≤0.5%? SL đổi có tính lại lot? circuit breaker ngày có bị kích hoạt?) ngay sau phiên.
- **Hàng tuần:** chạy đủ bộ 12 câu hỏi trên toàn bộ lệnh trong tuần, tính rubric A/B/C/F, đối chiếu `conviction_score` vs `outcome`.
- **Hàng tháng:** tổng hợp tần suất vi phạm, cập nhật bảng correlation instrument (mục 13, đòn #5), xem xét có đủ dữ liệu để chạy Kelly criterion thật chưa.
- **Ai/cái gì là "auditor":** bản thân trader (self-audit hàng ngày, dễ bị thiên vị — cần trung thực triệt để) + rule cứng đã viết ra trước (circuit breaker, checklist) đóng vai trò "auditor tự động" không cảm xúc + review định kỳ hàng tuần/tháng đóng vai trò auditor có khoảng cách thời gian để nhìn khách quan hơn.

---

## 15. Case Studies (kịch bản minh họa)

> [!quote] Ghi chú bắt buộc
> Các case dưới đây là **kịch bản minh họa được xây dựng chi tiết** để huấn luyện nhận diện — KHÔNG phải log giao dịch thật (tuân thủ mục 3.4 Doctrine v2). Số liệu giá mang tính đại diện.

![[OverRisk-CaseStudies-Panel.svg|760]]
*Sơ đồ: 3 case minh họa trên tài khoản 100k FTMO — Case A (risk vượt + correlated blow-up), Case B (tuân thủ 0.5%, bỏ lỡ upside), Case C (gray-zone SL creep hợp lý hoá).*

### Case A — Thất bại điển hình (tài khoản FTMO 100K)

**Bối cảnh:** Tài khoản FTMO Challenge 100K (daily loss 5% = $5,000 tính trên balance đầu ngày; max loss 10% = $10,000). Symbol NAS100 và US30, phiên New York, không có tin lớn trong ngày. Balance đầu ngày: $102,400 (đã lãi nhẹ từ tuần trước).

**Timeline diễn biến (giờ VN, UTC+7 — NY mở cửa 20:30 giờ VN mùa hè):**

- **20:35 (VN) / 09:35 NY:** Setup NAS100 Long xuất hiện — sweep SSL nội bộ, MSS M5, FVG hình thành. Kế hoạch ban đầu: risk 0.5% = $512, SL 25 điểm dưới swing low, entry ở FVG.
- **20:41 (VN):** Giá pullback sâu hơn dự kiến, không chạm FVG mà xuyên luôn xuống dưới, kích hoạt suy nghĩ "chờ thêm chút nữa chắc quay lại, setup này mạnh". Trader dời điểm chờ entry xuống thấp hơn — SL kế hoạch giờ phải rộng ra 42 điểm để vẫn hợp lệ dưới swing low mới. **Lot KHÔNG được tính lại** — vẫn giữ lot tương ứng $512/25 điểm, khiến $ risk thực tế tăng lên ≈$860 (~0.84% equity).
- **20:52 (VN):** Entry khớp. Đồng thời, thấy US30 cũng đang setup tương tự (correlation ước tính ~0.9 với NAS100 trong phiên này) — trader mở thêm US30 Long risk 0.5% kế hoạch ($512) mà không cộng dồn vào nhóm correlation đã mở. Tổng risk danh nghĩa "trên giấy" = 1%, nhưng vì correlation cao, risk hiệu dụng gần một vị thế ~1.6-1.7% duy nhất (0.84% + 0.5% × hệ số tương quan cao).
- **21:15 (VN):** Cả hai lệnh cùng bị một cú đảo chiều mạnh quét qua — vì cùng hướng, cùng correlation, chúng phản ứng gần như đồng thời. NAS100 chạm SL: −$860. US30 chạm SL: −$512. Tổng thiệt hại: **−$1,372, tương đương 1.34% equity trong một buổi sáng — đã tiêu tốn hơn 1/4 daily loss budget ($5,000 → còn $3,628) chỉ từ MỘT ý tưởng bias duy nhất bị nhân đôi qua correlation.**
- **21:20 (VN):** Cảm giác "phải gỡ lại" xuất hiện — trader vào thêm 1 lệnh XAUUSD Short (không liên quan trực tiếp bias buổi sáng) với risk $700 (~0.68%) để "cân bằng lại cảm xúc". Lệnh này cũng thua: −$700.
- **Kết quả cuối ngày:** Tổng thiệt hại **−$2,072 (~2.02% equity)**, tương đương hơn 40% daily loss budget trong một buổi sáng, xuất phát từ 1 lần không tính lại lot khi SL nới rộng + 1 lần bỏ qua correlation cap + 1 lần revenge sizing tiếp nối.

**Post-mortem (đối chiếu checklist audit mục 14.3):**
- FAIL câu 3 (lot không được tính lại khi SL nới rộng — đây là lỗi kích hoạt đầu tiên).
- FAIL câu 4 (tổng risk nhóm correlation NAS100/US30 vượt xa 0.5% aggregate).
- FAIL câu 6 (lệnh XAUUSD sau đó là revenge sizing rõ ràng — risk tăng ngay sau chuỗi thua không có lý do cấu trúc mới).
- FAIL câu 7 (không có circuit breaker ngày nào được kích hoạt dù đã thua 3 lệnh liên tiếp cùng buổi sáng).
- **Thiệt hại thực:** $1,372 (hai lệnh đầu) + **thiệt hại kép:** $700 (lệnh revenge) = tổng $2,072, so với kế hoạch ban đầu nếu tuân thủ đúng 0.5% + cap correlation chỉ là khoảng $512 (một lệnh duy nhất trong nhóm, các lệnh còn lại bị cap hoặc bỏ qua) — **chênh lệch 4 lần** giữa kỷ luật và không kỷ luật trên cùng một buổi sáng.

### Case B — Xử lý đúng (cùng bối cảnh, trader tuân thủ process)

**Bối cảnh:** Cùng tài khoản FTMO 100K, cùng ngày, cùng setup NAS100 Long ban đầu.

**Diễn biến:** Khi giá pullback sâu hơn dự kiến (20:41 VN), trader **tính lại lot ngay lập tức** theo SL mới 42 điểm: lot mới cho $512/42 điểm ≈ giảm khoảng 40% so với lot ban đầu. Khi thấy US30 setup tương tự, trader nhận diện đúng nhóm correlation NAS100/US30 đã mở — theo quy tắc cap, **chỉ chọn lệnh có conviction cao hơn (NAS100, vì FVG rõ hơn) và bỏ qua US30 hoàn toàn**, giữ tổng risk nhóm ở đúng 0.5%.

Kết quả: lệnh NAS100 vẫn bị quét SL đúng như kịch bản A (cùng một cú đảo chiều mạnh) — thiệt hại đúng $512 (0.5% chẵn). Vì không mở US30, trader **bỏ lỡ** khả năng — trên thực tế trong kịch bản này US30 cũng thua giống NAS100 nên bỏ qua nó là đúng, nhưng giả sử một biến thể khác: nếu US30 sau đó đã bật tăng mạnh và thắng, trader tuân thủ process vẫn "mất" một cơ hội thắng $600-800 tiềm năng đó — **đây chính là "trả giá" của kỷ luật correlation cap: đôi khi bạn bỏ lỡ một lệnh thắng vì đã coi nhóm correlation là một vị thế duy nhất.**

**Vì sao vẫn đúng về mặt kỳ vọng dài hạn:** nếu tính trên 100 buổi sáng tương tự, việc luôn cap correlation ở 0.5% aggregate (thay vì để mỗi lệnh 0.5% độc lập) làm giảm **phương sai** của kết quả hàng ngày rất nhiều mà không giảm expectancy trung bình bao nhiêu (vì hai lệnh correlated cao gần như luôn cùng thắng hoặc cùng thua) — cái giá phải trả (bỏ lỡ một vài lần "thắng kép may mắn") nhỏ hơn nhiều so với lợi ích (tránh các lần "thua kép" như Case A). Quy tắc đúng không phải lúc nào cũng cho kết quả đẹp ở từng lệnh — nó tối ưu cho toàn bộ phân phối kết quả.

### Case C — Vùng xám (gray zone)

**Tình huống mơ hồ:** SL kế hoạch ban đầu là 20 điểm cho NAS100. Ngay trước khi entry, giá có một wick nhỏ vượt qua mức SL dự kiến 3 điểm rồi quay lại — cấu trúc thật (swing low hợp lệ theo đúng quy tắc [[06-Mistake-Not-Have-Market-Structure-Shift]]) giờ nằm ở 23 điểm thay vì 20. Chênh lệch chỉ 3 điểm (15% so với kế hoạch) — không lớn như case A (42 vs 25 điểm), nhưng đủ nhỏ để tạo cám dỗ "chắc không đáng phải tính lại lot, chênh có 3 điểm thôi, làm tròn cho tiện".

**Phân tích cả hai cách xử lý:**
- **Xử lý A — giữ nguyên lot (không tính lại):** $ risk tăng từ $512 lên khoảng $588 (~0.575% thay vì 0.5%) — vi phạm kỹ thuật rule nhưng ở mức độ rất nhỏ, khó coi là "risk creep nghiêm trọng" như Case A.
- **Xử lý B — tính lại lot đúng 23 điểm:** giữ đúng $512, nhưng lot mới có thể rơi vào giữa hai bước lot broker cho phép (ví dụ 0.19 lot làm tròn xuống 0.18 lot) — khiến $ risk thực tế còn THẤP hơn 0.5% một chút (~$490), tức là "quá thận trọng" theo nghĩa hẹp.

**Tiêu chí tie-break:** Theo đúng quy tắc mục 7 của note gốc ("không bao giờ giữ nguyên lot khi SL nới rộng — luôn tính lại size"), Xử lý B là đúng theo chữ của rule, kể cả khi chênh lệch nhỏ. Lý do: **rule không có ngưỡng miễn trừ theo phần trăm chênh lệch** — nếu cho phép "chênh nhỏ thì bỏ qua", ranh giới "nhỏ" sẽ dần bị nới ra theo thời gian (đúng cơ chế "Stealth SL creep" ở mục 11.4 biến thể #2) cho tới khi các lần "nhỏ" cộng dồn thành vi phạm lớn không được nhận ra.

**Bài học về giới hạn của rule:** Rule cứng "luôn tính lại lot" xử lý tốt các trường hợp rõ ràng (chênh lệch lớn như Case A) nhưng tạo ra chi phí giao dịch nhỏ (thời gian, làm tròn lot bất tiện) ở các trường hợp biên rất nhỏ như Case C — đây chính là loại tình huống mà phe Phản đối ở mục 12 nêu ra (chi phí tuân thủ cứng nhắc). Giải pháp thực dụng không phải bỏ rule, mà **tự động hoá phép tính** (dùng position size calculator có sẵn, không tính tay) để chi phí tuân thủ ở các trường hợp biên nhỏ tiến gần về 0 — biến câu hỏi "có đáng tính lại không" (dễ bị cảm tính bỏ qua) thành một phép tính tự động không tốn công cân nhắc.

### Bảng so sánh 3 case

| Case | Trigger | Quyết định | Kết quả | Bài học 1 dòng |
|---|---|---|---|---|
| A — Thất bại | SL nới rộng 25→42 điểm + correlation NAS100/US30 | Giữ nguyên lot, mở cả 2 lệnh, sau đó revenge XAUUSD | −$2,072 (~2.02% equity), 40% daily budget | Một lần không tính lại lot + bỏ qua correlation có thể nhân bốn lần thiệt hại so với tuân thủ |
| B — Đúng | SL nới rộng 25→42 điểm + correlation NAS100/US30 | Tính lại lot, chỉ giữ 1 lệnh trong nhóm correlation | −$512 (đúng 0.5%), bỏ lỡ khả năng thắng kép từ US30 | Tuân thủ đúng đôi khi "mất" một cơ hội thắng — đó là cái giá bình thường của kỷ luật, không phải bằng chứng rule sai |
| C — Gray zone | SL lệch nhẹ 20→23 điểm (chênh nhỏ) | Tính lại lot dù chênh nhỏ, chấp nhận lot bị làm tròn lệch nhẹ | ~$490-512 tùy làm tròn, chênh lệch không đáng kể | Rule không có ngưỡng miễn trừ theo % — chênh nhỏ vẫn phải tính lại, nên tự động hoá phép tính để giảm chi phí tuân thủ |

---


## 16. Liên kết

**Concepts:** [[36-Forex-CFD-Basics-Pip-Lot-Spread-Swap-Leverage-Margin]]

**Mistakes liên quan:** [[05-Mistake-Not-enough-RR]] · [[01-Mistake-Emotional-revenge-trade]] · [[09-Mistake-Wrong-daily-bias]] · [[02-Mistake-Enter-before-liquidity-sweep]]
