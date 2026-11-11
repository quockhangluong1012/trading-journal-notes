---
type: mistake
category: risk
severity: high
related_model: ICT 2022
frequency: 3
status: active
tags:
  - trading/ict/mistake
  - trading/review
  - trading/risk
created: 2026-06-20
updated: 2026-07-08
---

# Mistake - Not enough RR

> [!summary] Tóm tắt 1 câu
> Vào lệnh với reward-to-risk thực tế (đo tới liquidity thật gần nhất, sau spread/slippage) quá thấp để hệ thống có thể sống sót — hoặc tệ hơn, "làm đẹp" con số bằng cách nới rộng SL hay kéo TP lại gần để RR trên giấy trông ổn trong khi RR thật thì không.

> [!danger] Nguyên tắc cốt lõi
> RR không phải là con số bạn gõ vào ô Take Profit — nó là khoảng cách thật từ SL structural tới **draw on liquidity** gần nhất mà không có pool đối ứng nào chặn giữa đường. Nếu không đo được khoảng cách đó bằng một mức liquidity cụ thể, bạn không có RR — bạn có một con số bịa ra để cảm thấy yên tâm.

---

## 1. Mô tả lỗi

Đây là lỗi về **chất lượng thiết lập**, không phải lỗi về hướng đi (bias). Trader xác định đúng hướng thị trường, đúng POI, thậm chí đúng cả sweep + MSS — nhưng khoảng cách reward thực tế từ entry tới nơi giá thật sự có khả năng đi tới lại quá nhỏ so với risk đã bỏ ra. Có hai biến thể của lỗi này:

1. **RR kế hoạch thấp ngay từ đầu** — TP được đặt theo một số pip "cảm thấy hợp lý" hoặc theo tỷ lệ RR tối thiểu formal (ví dụ 1:1) mà không kiểm tra xem tại đó có thật sự tồn tại một mức liquidity nào không.
2. **RR trên giấy bị "làm đẹp"** — SL bị nới rộng ra để tránh bị quét (làm risk lớn hơn giá trị thật của setup), hoặc TP bị kéo lại gần vì sợ giá quay đầu (chốt non), khiến RR thực hiện được thấp hơn nhiều so với RR đã lên kế hoạch.

Cả hai biến thể đều vi phạm nguyên tắc cốt lõi của ICT 2022 Model: entry chỉ có giá trị khi có một **draw on liquidity** rõ ràng, đủ xa, và không bị chặn để biện minh cho risk đã bỏ ra. Xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]].

- Tôi đặt TP theo một số pip cố định (ví dụ luôn luôn 20 pips) thay vì tại một mức liquidity cụ thể.
- Tôi không thể trả lời câu hỏi "TP này đang nhắm vào pool thanh khoản nào?".
- Tôi biết setup "đúng hướng" nên chấp nhận RR 1:1 hoặc thấp hơn vì nghĩ win rate sẽ bù lại.
- Tôi nới SL ra "cho an toàn" mà không tính lại xem RR còn hợp lý không.

![[LowRR-Sec-01-MoTa.svg|760]]
*Sơ đồ: risk đo tới SL structural, nhưng reward bị đo sai — tới một TP tùy ý thay vì tới liquidity thật, trong khi một pool đối ứng nằm giữa đường có thể đảo giá trước khi tới đích.*

---

## 2. Biểu hiện & Dấu hiệu nhận biết

| Dấu hiệu | Mức độ cảnh báo |
|---|---|
| TP đặt theo số pip cố định, không tại một mức liquidity cụ thể | Đỏ |
| Không thể gọi tên pool thanh khoản mà TP đang nhắm tới | Đỏ |
| RR kế hoạch < 1:2 tới liquidity thật gần nhất | Đỏ |
| Có pool đối ứng / FVG chưa lấp nằm giữa entry và TP | Đỏ |
| "Chắc sẽ chạm TP" — không đo khoảng cách thật bằng số | Amber |
| Dời TP lại gần hơn vì sợ giá quay đầu (chốt non) | Amber |
| SL đặt theo số tròn / thói quen, không theo cấu trúc (sweep/OB) | Amber |

Checklist nhận diện nhanh trước khi bấm lệnh:

- [ ] TP của tôi đang nằm tại một mức liquidity cụ thể nào — internal (EQH/EQL, FVG) hay external (old H/L, session H/L)?
- [ ] RR đo được từ SL structural tới mức đó có ≥1:2 không?
- [ ] Có pool thanh khoản đối ứng hoặc FVG chưa lấp nằm giữa entry và TP không (xem mục 5.2 Runway check)?
- [ ] Tôi có đang co TP lại gần vì sợ, hay vì có lý do cấu trúc thật?
- [ ] SL của tôi có đặt tại một điểm cấu trúc (sau sweep/OB/MSS) hay chỉ là "khoảng cách cảm thấy an toàn"?

![[LowRR-Sec-02-BieuHien.svg|760]]
*Sơ đồ: bảng tell — mỗi dấu Đỏ là lý do dừng lại và đo lại RR trước khi vào lệnh.*

---

## 3. Cơ chế & Vì sao nguy hiểm

Về bản chất đây là bài toán **kỳ vọng (expectancy)**, không phải bài toán "đúng hay sai hướng":

```
Expectancy (R) = (Win Rate × R trung bình thắng) − (Loss Rate × R trung bình thua)
```

Khi RR trung bình thắng thấp, win rate cần thiết để **hòa vốn (breakeven)** tăng rất nhanh — và với chi phí giao dịch thật (spread, slippage, đôi khi commission), ngưỡng hòa vốn thực tế còn cao hơn con số lý thuyết dưới đây:

| RR | Win rate hòa vốn (lý thuyết) |
|---|---|
| 1 : 1 | 50% |
| 1 : 1.5 | 40% |
| 1 : 2 | 33% |
| 1 : 3 | 25% |
| 1 : 4 | 20% |
| 1 : 5 | 17% |

Một trader ICT discretionary tốt, có kỷ luật, thường đạt win rate thực tế trong khoảng **40–55%** (không phải 70-80% như quảng cáo). Với vùng win rate đó:

- Ở RR 1:1, breakeven WR (50%) nằm sát mép trên của vùng win rate thật — biên an toàn gần như bằng 0, chỉ cần một chuỗi thua ngắn hoặc chi phí giao dịch cũng đủ đẩy hệ thống về âm.
- Ở RR ≥1:2, breakeven WR (≤33%) thấp hơn hẳn win rate thật — tạo ra **biên an toàn (margin)** đủ lớn để hệ thống chịu được variance, chuỗi thua, và chi phí giao dịch mà vẫn có kỳ vọng dương.

Đây là lý do vì sao RR thấp không chỉ "kém tối ưu" mà **nguy hiểm về mặt cấu trúc**: nó buộc bạn phải đạt một win rate cao hơn khả năng thực tế của một hệ thống discretionary để chỉ hòa vốn, chưa nói tới có lời.

Ngoài ra, với tài khoản prop firm (FTMO, The5ers...), RR thấp gây thêm hai vấn đề:

1. **Cần nhiều lệnh hơn để đạt target lợi nhuận** → nhiều lệnh hơn = nhiều cơ hội hơn để phạm lỗi khác (overtrading, revenge trade, risk quá mức) và variance tích lũy cao hơn.
2. **Xác suất breach daily/max drawdown tăng** vì mỗi chuỗi thua ngắn cần nhiều lệnh thắng RR thấp hơn để bù lại, kéo dài thời gian tài khoản "ở trong vùng rủi ro" của giới hạn drawdown.

![[LowRR-Sec-03-CoChe.svg|760]]
*Sơ đồ: win rate hòa vốn giảm mạnh khi RR tăng — ở RR≥1:2, biên an toàn so với win rate discretionary điển hình (40–55%) mới thật sự tồn tại.*

---

## 4. Ví dụ minh họa

### ✅ Đúng

Entry tại POI (FVG/OB) hình thành ngay sau sweep + displacement + MSS, SL đặt structural ngay sau điểm sweep. TP1 đặt tại internal liquidity (equal highs) ở khoảng 2R, TP2 (runner) đặt tại external liquidity thật (old high / BSL) ở khoảng 4R. Không có FVG hay pool đối ứng nào nằm giữa entry và cả hai target.

![[LowRR-Example-Correct.svg|760]]
*Sơ đồ: entry tại POI với SL structural chặt, TP1 internal liquidity ≥2R, TP2 external draw ≈4R, runway sạch suốt đường đi.*

**Vì sao đúng:** SL chặt vì đặt tại cấu trúc thật (ngay sau sweep), không phải vì "hy vọng giá không quay lại". Cả hai target đều là liquidity thật, có thể gọi tên cụ thể, và không có gì cản đường — nên RR đo được (≥1:2 tới TP1) là RR **khả dụng thật**, không phải RR lý thuyết trên giấy. Đây chính là kiểu setup mà kỷ luật chờ đợi (xem [[02 - Mistake - Enter before liquidity sweep]]) được đền đáp bằng một khoảng reward xứng đáng.

### ❌ Sai

Chase entry giữa sóng sau khi displacement đã chạy xong (không phải tại POI), buộc SL phải đặt xa theo kiểu volatility-based vì không còn cấu trúc gần để dựa vào. TP đặt vào đúng một resting pool nhỏ chỉ cách entry chưa tới 1.5R — giá chạm pool, đảo chiều ngay, quét luôn SL trước khi hồi lại đúng hướng bias ban đầu.

![[LowRR-Example-Wrong.svg|760]]
*Sơ đồ: chase entry giữa sóng, SL rộng vì không có cấu trúc gần, TP nén vào một resting pool <1.5R rồi giá đảo chiều.*

**Bài học:** Bias đúng và setup "trông ổn" không cứu được một RR tồi. Vào trễ (chase) tạo ra tác động kép tiêu cực: vừa làm SL phải xa hơn (vì không còn cấu trúc gần), vừa làm reward còn lại ngắn hơn (vì một phần con sóng đã "delivered" trước khi bạn vào). Đây chính là lý do RR thấp và entry trễ thường đi kèm nhau như nguyên nhân — hệ quả (xem mục 5.6).

---

## 5. Kiến thức nâng cao (Advanced)

![[LowRR-Advanced-Runway.svg|760]]
*Sơ đồ: hai kịch bản cùng bias, cùng RR "trên giấy" — khác nhau ở việc có pool đối ứng chặn đường (runway) hay không.*

### 5.1. Đo RR tới draw on liquidity thật, không phải tới pip tùy ý

RR chỉ có ý nghĩa khi mẫu số (risk) và tử số (reward) đều được neo vào cấu trúc thị trường thật. Risk neo vào SL structural (sau sweep/OB/MSS — xem mục 5.3). Reward phải neo vào một **draw on liquidity** cụ thể: internal range liquidity (EQH/EQL, FVG chưa lấp) hoặc external range liquidity (old H/L, session H/L, PDH/PDL). Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]] và [[19 - Liquidity]]. Nếu không thể chỉ ra chính xác pool nào đang được nhắm tới, con số RR trên màn hình chỉ là ảo giác của sự chuẩn bị — nó không phản ánh gì về khả năng giá thật sự di chuyển tới đó.

### 5.2. Runway check — có gì cản đường giữa entry và target?

Trước khi chốt một RR kế hoạch, luôn tự hỏi ba câu:

1. Có equal highs/lows (EQH/EQL) hoặc old high/low nào nằm giữa entry và target không?
2. Có FVG/OB đối ứng (chiều ngược bias) chưa được lấp nằm trên đường đi không?
3. Draw on liquidity hiện tại đã được "giao" (delivered) một phần chưa — còn đủ quãng đường để tới target không?

Nếu câu trả lời cho bất kỳ câu nào là "có", RR thật thấp hơn RR đo trên biểu đồ — vì giá có xu hướng phản ứng tại pool đối ứng đó (đảo chiều một phần hoặc hoàn toàn) trước khi tiếp tục hành trình tới target xa hơn. Trong trường hợp này, hoặc hạ target về ngay trước pool đối ứng để tính RR bảo thủ hơn, hoặc bỏ qua lệnh nếu RR mới không còn đạt ngưỡng tối thiểu.

### 5.3. Stop logic — structural vs volatility-based, và vai trò của CE/OTE

Có hai triết lý đặt SL:

- **Structural stop:** đặt ngay sau điểm cấu trúc quan trọng nhất (sau sweep, ngoài OB, ngoài điểm MSS) — khoảng cách do thị trường quyết định, không phải do trader "cảm thấy an toàn".
- **Volatility-based stop:** đặt theo một hệ số của ATR hoặc một khoảng cách cố định — thường xa hơn cần thiết vì không tận dụng được cấu trúc.

Structural stop luôn cho RR tốt hơn với cùng một target, vì risk (mẫu số) nhỏ hơn. Công cụ để tối ưu structural stop mà **không đánh đổi win rate**: dùng **CE (Consequent Encroachment)** — xem [[10 - Consequent Encroachment (Mean Threshold)]] — để refine entry vào đúng điểm giữa của OB/FVG thay vì mép ngoài, và dùng **OTE (Optimal Trade Entry)** — xem [[26 - OTE - Optimal Trade Entry]] — kết hợp với [[27 - Premium Discount]] để đảm bảo entry nằm sâu trong vùng discount/premium hợp lệ. Cả hai kỹ thuật này giúp SL chặt hơn mà không cần đợi thêm confirmation (tức không hy sinh xác suất vào lệnh) — đây là cách "tăng RR mà không giảm win rate" đúng nghĩa, khác với việc chỉ đơn giản nới TP xa hơn.

### 5.4. Fixed TP vs partials + runner — tác động tới expectancy và tính nhất quán prop firm

Chốt toàn bộ vị thế tại TP1 (internal liquidity, ~2R) đảm bảo RR thực hiện ổn định nhưng bỏ lỡ phần mở rộng (external draw). Chốt một phần tại TP1 và để runner chạy tới TP2 (external liquidity) cải thiện R trung bình thắng dài hạn, nhưng tăng phương sai của từng lệnh riêng lẻ. Sự lựa chọn này nên gắn với luật của prop firm cụ thể:

- **FTMO** (target lợi nhuận cố định, ví dụ 10% cho gói 10K, với giới hạn daily loss 5% và max loss 10%): một vài lệnh RR lớn (runner) giúp đạt target nhanh hơn, giảm số lệnh cần thiết — nhưng phải cân bằng với daily loss limit vì một lệnh runner thua hết cũng ăn vào giới hạn ngày.
- **The5ers** (thường thưởng cho **ngày giao dịch có lời đều đặn**, ví dụ ~0.5%+/ngày, thay vì một target tổng cố định): chốt một phần sớm tại TP1 giúp khóa lời ổn định mỗi ngày, phù hợp với tiêu chí "consistency" hơn là để toàn bộ vị thế chạy runner rồi có ngày âm ngày dương thất thường.

Chốt lời quá sớm ("chốt non" so với TP1 đã hoạch định) luôn làm giảm RR thực hiện so với kế hoạch — đây chính là biến thể thứ hai của lỗi này đã nêu ở mục 1.

### 5.5. Ngưỡng RR tối thiểu như bộ lọc chống overtrading và chống chase

Một quy tắc "không vào lệnh nếu RR đo được tới liquidity thật < 1:2" không chỉ là quy tắc quản trị rủi ro — nó tự động lọc bỏ phần lớn các lệnh chase và overtrade, vì:

- Entry trễ (chase) luôn làm SL xa hơn và reward còn lại ngắn hơn → tự động vi phạm ngưỡng RR tối thiểu → bị loại trước khi kịp vào lệnh.
- Một ngày không có setup nào đạt ngưỡng RR tối thiểu là tín hiệu để đứng ngoài, thay vì hạ tiêu chuẩn để "có lệnh cho có".

Nói cách khác, kỷ luật RR và kỷ luật entry timing củng cố lẫn nhau — vi phạm cái này gần như luôn kéo theo vi phạm cái kia.

### 5.6. Vì sao entry trễ là kẻ giết RR số một

Entry trễ (sau khi displacement đã chạy, "đuổi theo giá") tạo ra tác động kép luôn làm RR xấu đi: (1) SL phải xa hơn vì không còn cấu trúc gần (sweep/OB) để dựa vào, buộc dùng volatility-based stop; (2) reward còn lại ngắn hơn vì một phần con sóng đã "delivered" trước khi vào lệnh. Đây là lý do việc chờ entry đúng tại POI — thay vì đuổi theo phản ứng giá — không chỉ là vấn đề xác suất (win rate) như đã phân tích ở [[02 - Mistake - Enter before liquidity sweep]], mà còn trực tiếp quyết định RR có đạt ngưỡng tối thiểu hay không.

---

## 6. Best Practices

> [!success] Best Practices
> 1. Luôn xác định TP tại một mức liquidity cụ thể, có thể gọi tên — không bao giờ đặt theo số pip tùy ý.
> 2. Đo RR từ SL structural tới target thật; nếu không đạt ≥1:2, không vào lệnh.
> 3. Chạy runway check (mục 5.2) trước khi chốt RR kế hoạch — tìm pool đối ứng/FVG chưa lấp nằm giữa đường.
> 4. Ưu tiên structural stop (sau sweep/OB/MSS); dùng CE/OTE để tối ưu entry và làm SL chặt hơn thay vì kéo TP ra xa để "sửa" RR.
> 5. Xác định rõ TP1 (internal liquidity) và TP2 (external draw) trước khi vào lệnh; quyết định trước tỷ lệ chốt từng phần.
> 6. Khớp chiến lược chốt lời (fixed vs runner) với luật cụ thể của prop firm đang trade (FTMO target cố định vs The5ers consistency theo ngày).
> 7. Không dời TP lại gần vì sợ — chỉ điều chỉnh target khi có lý do cấu trúc thật (ví dụ phát hiện pool đối ứng mới).
> 8. Log lại RR kế hoạch và RR thực hiện của mọi lệnh để phát hiện thói quen "chốt non" hoặc "TP ảo tưởng" theo thời gian.

---

## 7. Rule phòng tránh & Checklist

- [ ] Không vào lệnh nếu RR đo được từ SL structural tới liquidity thật gần nhất < 1:2.
- [ ] TP phải neo vào một mức liquidity cụ thể (EQH/EQL, FVG, old H/L, session H/L) — không đặt theo pip tùy ý.
- [ ] Chạy runway check: xác nhận không có pool đối ứng/FVG chưa lấp nằm giữa entry và target đã chọn.
- [ ] SL đặt tại điểm cấu trúc (sau sweep/OB/MSS), dùng CE/OTE để tối ưu thay vì nới rộng SL cho "an toàn".
- [ ] Xác định trước TP1 (internal, ≥2R) và TP2 (external, 3–5R) và tỷ lệ chốt từng phần trước khi vào lệnh.
- [ ] Không dời TP lại gần sau khi vào lệnh trừ khi có lý do cấu trúc mới xuất hiện.
- [ ] Nếu không thể trả lời "TP này đang nhắm vào pool nào?" — không vào lệnh.
- [ ] Ghi lại RR kế hoạch vs RR thực hiện trong log để theo dõi độ lệch theo thời gian.

---

## 8. Ví dụ đã xảy ra

- *(chưa có — thêm liên kết theo định dạng bên dưới khi phát sinh lệnh thực tế liên quan tới lỗi này)*

Định dạng thêm liên kết: `[[Loss - NN - Trade YYYY-MM-DD SYMBOL Position]]`

---

## 9. Flashcards / Active Recall

**Q1:** Vì sao RR thấp lại nguy hiểm hơn nhiều so với việc chỉ "kém tối ưu"?
**A1:** Vì nó buộc win rate hòa vốn tăng rất nhanh (ví dụ 1:1 cần 50% chỉ để hòa vốn), trong khi win rate thực tế của một hệ thống discretionary ICT thường chỉ 40–55%. Ở RR thấp, biên an toàn gần như bằng 0 — một chuỗi thua ngắn hoặc chi phí giao dịch cũng đủ đẩy hệ thống về âm.

**Q2:** Hai biến thể của lỗi "Not enough RR" là gì?
**A2:** (1) RR kế hoạch thấp ngay từ đầu vì TP đặt theo pip tùy ý thay vì tại liquidity thật; (2) RR trên giấy bị "làm đẹp" — nới SL rộng ra hoặc kéo TP lại gần sau khi vào lệnh — khiến RR thực hiện thấp hơn RR kế hoạch.

**Q3:** "Runway check" là gì và tại sao nó quan trọng?
**A3:** Là việc kiểm tra xem có EQH/EQL, old H/L, hoặc FVG/OB đối ứng nào nằm giữa entry và target không. Nếu có, giá có xu hướng phản ứng (đảo một phần hoặc hoàn toàn) tại đó trước khi tới target xa hơn, khiến RR thật thấp hơn RR đo trên biểu đồ.

**Q4:** Vì sao entry trễ (chase) được gọi là "kẻ giết RR số một"?
**A4:** Vì nó tạo tác động kép: SL phải đặt xa hơn do không còn cấu trúc gần (buộc dùng volatility-based stop), đồng thời reward còn lại ngắn hơn vì một phần con sóng đã delivered trước khi vào lệnh.

**Q5:** Sự khác biệt trong chiến lược chốt lời giữa FTMO và The5ers ảnh hưởng thế nào tới quyết định RR/runner?
**A5:** FTMO có target lợi nhuận cố định nên một vài lệnh RR lớn (runner) giúp đạt target nhanh hơn, miễn cân bằng với daily loss limit. The5ers thưởng cho ngày lời đều đặn (~0.5%+/ngày) nên chốt một phần sớm tại TP1 phù hợp hơn để duy trì tính nhất quán.

**Q6:** Công cụ nào giúp tăng RR mà KHÔNG làm giảm win rate?
**A6:** CE (Consequent Encroachment) và OTE kết hợp Premium/Discount — dùng để refine entry vào đúng điểm giữa/tối ưu của OB/FVG, giúp SL chặt hơn (risk nhỏ hơn) mà không cần đợi thêm confirmation, khác với việc chỉ đơn giản kéo TP xa hơn để "sửa" RR.

---

## 10. Lesson Learned

Bài học chính: **RR không phải là con số tự chọn để cảm thấy yên tâm — nó là kết quả đo lường của một setup có cấu trúc thật.** Một lệnh "đúng hướng" với RR không đủ vẫn là một quyết định tồi về mặt kỳ vọng, vì nó âm thầm đòi hỏi một win rate mà một hệ thống discretionary không thể duy trì bền vững. Ngưỡng RR tối thiểu (≥1:2 tới liquidity thật) không phải là một con số cứng nhắc để làm khó bản thân — nó là ranh giới giữa một hệ thống có biên an toàn thống kê và một hệ thống sống nhờ may mắn ngắn hạn.

Quy tắc cá nhân:
- [ ] Không vào lệnh nếu RR đo được tới liquidity thật < 1:2.
- [ ] Luôn chạy runway check trước khi chốt target.
- [ ] Không dời TP lại gần vì sợ; không nới SL ra vì thiếu tự tin vào cấu trúc đã xác định.

> Risk là con số bạn kiểm soát bằng cấu trúc. Reward là con số thị trường quyết định bằng draw on liquidity. RR chỉ trung thực khi cả hai đều được đo bằng thước đo của thị trường, không phải bằng cảm giác của bạn.

---

## 11. Liên kết

**Concepts:** [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] · [[19 - Liquidity]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]] · [[26 - OTE - Optimal Trade Entry]] · [[27 - Premium Discount]] · [[10 - Consequent Encroachment (Mean Threshold)]]

**Mistakes liên quan:** [[07 - Mistake - Risk more than 0.5% total account]] · [[02 - Mistake - Enter before liquidity sweep]] · [[01 - Mistake - Emotional revenge trade]] · [[09 - Mistake - Wrong daily bias]]
