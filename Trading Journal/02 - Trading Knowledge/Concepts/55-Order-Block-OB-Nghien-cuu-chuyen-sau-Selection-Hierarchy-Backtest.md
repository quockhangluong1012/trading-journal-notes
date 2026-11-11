---
type: ict-concept
concept: "Order Block (OB) — Deep Research"
aliases:
  - OB Deep Research
  - Order Block Selection
  - OB Quality Framework
  - Too Many Order Blocks
  - OB Hierarchy
tags:
  - trading/ict/concept
  - trading/study
  - trading/deep-dive
  - "#OrderBlock"
  - pd-array
  - d1-h1-m5
  - 2022-model
  - backtesting
status: developing
category: PD Array
timeframes: [D1, H1, M5]
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets: [NQ1, EURUSD, GBPUSD, XAUUSD]
importance: 5
confidence: 3
last_reviewed: 2026-09-27
created: 2026-09-27
updated: 2026-09-27
prerequisites:
  - "[[25-OB-Order-Block]]"
  - "[[50-Displacement-In-Depth]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[13-FVG-Fair-Value-Gap]]"
  - "[[12-Dealing-Range]]"
  - "[[19-Liquidity]]"
  - "[[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]"
common_mistakes:
  - "[[08-Mistake-Weak-Displacement]]"
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]"
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
rule_versions:
  - OB-DEF v0.1
  - OB-HIER v0.1
  - OB-INVAL v0.1
  - OBQS v0.1
---

# Order Block (OB) — Nghiên cứu chuyên sâu: Cơ chế, Phân cấp, Chọn lọc & Backtest

> [!abstract] Cách đọc note này
> - Note này **không thay thế** [[25-OB-Order-Block]] (note nền tảng) và [[51-OB-Mitigation-Depth-Vi-sao-Shallow-CE-hay-Full-khac-nhau]] (độ sâu mitigation). Đây là **lớp nghiên cứu**: định nghĩa tối thiểu có thể backtest, cơ chế thị trường, phân cấp OB, giải bài toán "quá nhiều OB", kịch bản A–F, 24 edge cases, lượng hóa và thiết kế backtest.
> - Mọi mệnh đề quan trọng được gắn nhãn (bảng dưới). **Mọi ngưỡng số trong note là HEURISTIC** — điểm khởi đầu để backtest, không phải luật ICT.
> - Ví dụ ở §15–§17 là **ví dụ dựng (synthetic)**: giá minh họa để luyện tư duy, **không phải dữ liệu lịch sử**, không phải kết quả backtest.
> - Cuối note có **Phụ lục A — Audit note 25**: những mệnh đề trong note cũ nên hạ cấp từ "fact" xuống "hypothesis".

| Nhãn | Nghĩa | Ví dụ |
|---|---|---|
| **[MARKET MECHANICS]** | Giải thích được bằng cơ chế khớp lệnh, thanh khoản, đấu giá, hoặc có bằng chứng thực nghiệm độc lập | Lệnh market tiêu thụ lệnh limit → giá dịch chuyển |
| **[ICT FRAMEWORK]** | Cách ICT định nghĩa/diễn giải | "Smart money mitigate vị thế lỗ khi giá quay về OB" |
| **[INTERPRETATION]** | Diễn giải hợp lý nhưng không chứng minh được chỉ từ chart | "Người mua lớn còn metaorder chưa khớp xong" |
| **[HYPOTHESIS]** | Giả thuyết kiểm chứng được bằng dữ liệu | "OB có sweep trước đó cho expectancy cao hơn" |
| **[BACKTEST REQUIRED]** | Không được coi là edge cho đến khi có dữ liệu | "Rule 3 nến để invalidate OB" |
| **HEURISTIC** | Ngưỡng số đặt tạm để có thể đo, chưa tối ưu, chưa kiểm chứng | "displacement ≥ 1.5× ATR" |

---

## 1. Executive Summary

![[OB-DeepResearch-Anatomy.svg|760]]
*Hình 1 — Giải phẫu một Bullish OB: phần quan sát được (nến, sweep, displacement, FVG, swing bị phá, các mức giá) tách khỏi phần diễn giải (ai đặt lệnh, lệnh còn hay hết).*

**Mental model quan trọng nhất, trong 8 mệnh đề:**

1. **OB là một giả thuyết về VỊ TRÍ, không phải tín hiệu.** Điều duy nhất chart cho bạn biết chắc là: *tại vùng giá này, một cú mất cân bằng đo được (displacement) đã bắt đầu*. Mọi câu chuyện "lệnh tổ chức còn nằm chờ ở đó" là suy diễn. [MARKET MECHANICS cho phần quan sát; INTERPRETATION cho phần "lệnh còn chờ"]

2. **Ba lớp phải tách rời:** **OB = location** (nơi đáng để nghe) → **MSS/displacement khi giá quay lại = evidence** (bằng chứng phản ứng đang xảy ra) → **entry rule = execution** (quy tắc bóp cò). Gộp ba lớp thành một ("chạm OB là mua") là nguồn gốc của phần lớn lệnh thua kiểu OB. Mỗi lớp có thể backtest riêng.

3. **OB thừa hưởng ý nghĩa từ swing mà nó sinh ra.** Một OB quan trọng không phải vì hình dạng cây nến, mà vì cú displacement bắt đầu từ nó đã *làm gì*: lấy thanh khoản nào, phá cấu trúc cấp nào, tạo ra dealing range nào. Vì vậy **bài toán "quá nhiều OB" được giải bằng cách xếp hạng swing trước, rồi mới xét OB** — không phải so sánh các cây nến với nhau.

4. **Phần lớn OB là sản phẩm phụ tất yếu của mọi xu hướng.** Mỗi lần một trend nghỉ rồi đi tiếp, nó để lại một "nến ngược hướng cuối cùng". Trend càng dài, số OB càng nhiều, và đa số là OB internal sẽ bị xuyên qua. Điều đó là **bình thường về mặt thống kê**, không phải bằng chứng "thị trường tạo OB giả để bẫy trader ICT".

5. **Giá trị ít tranh cãi nhất của một structural OB là hình học rủi ro, không phải dự đoán.** Structural OB nằm tại swing được bảo vệ (protected low/high) — nơi mà nếu bị phá thì *chính luận điểm cấu trúc* sai. Nó đặt **điểm vào** và **điểm luận điểm sai** gần nhau → stop có logic, R:R bất đối xứng. Giá trị này tồn tại *ngay cả khi* OB không có sức mạnh dự đoán đặc biệt nào. [INTERPRETATION có cơ sở hình học; expectancy vẫn BACKTEST REQUIRED]

6. **Trạng thái bằng chứng (trung thực):** chưa có nghiên cứu peer-reviewed nào kiểm định *ICT Order Block* một cách trực tiếp. Bằng chứng lân cận có tồn tại: vùng support/resistance trùng với các đỉnh độ sâu sổ lệnh [^S3]; giá "bật" ở các mức S/R được phát hiện thường xuyên hơn là xuyên qua, và mức có nhiều lần bật trước đó có xác suất bật cao hơn [^S4][^S5]; stop-loss tụ ngay sau các mức giá hiển nhiên và khi bị kích hoạt tạo ra các cú tăng tốc (price cascade) [^S1][^S2]. Những bằng chứng này nói rằng **"các mức giá được nhiều người để ý có ảnh hưởng"** — chúng **không** chứng minh OB đặc biệt hơn các mức giá khác.

7. **Trong framework D1 → H1 → M5 của bạn:** D1 OB = vùng **context**; H1 OB = **POI** để chọn nơi chờ setup; M5 = nơi tìm **bằng chứng** (sweep → MSS → displacement) và **thực thi** (FVG là PD array entry chính của 2022 Model, M5 OB là phương án thay thế). Không bao giờ giao dịch "cú chạm OB" đơn thuần.

8. **Chương trình nghiên cứu:** *định nghĩa tối thiểu, đặc trưng phong phú*. Định nghĩa OB càng ít điều kiện càng tốt, rồi đo từng đặc trưng (sweep, FVG, cấp swing, premium/discount, HTF alignment, freshness) như **biến giải thích**. Nếu nhồi mọi confluence vào định nghĩa, bạn sẽ không bao giờ biết confluence nào thật sự tạo edge. Thứ tự kiểm định: (a) OB có phản ứng nhiều hơn vùng đối chứng không? → (b) đặc trưng nào làm tăng expectancy? → (c) entry/stop/invalidation nào tối ưu? → (d) có sống sót out-of-sample và sau chi phí không?

> [!important] Mental model một câu
> **OB là "địa chỉ gốc" của một cú mất cân bằng đo được. Nó chỉ đáng xem xét khi swing nó sinh ra có ý nghĩa cấu trúc, nằm đúng phía narrative D1, chưa bị tiêu thụ, và còn đường tới DOL. Khi giá tới OB, đó không phải lý do vào lệnh — đó là lúc bắt đầu *nghe*. Vào lệnh là do M5 cho bằng chứng; stop đặt nơi câu chuyện sai.**

---

## 2. Conceptual Foundation — từ zero đến advanced

### 2.1 Level 0 — Trực giác bằng một phiên đấu giá

Hãy tưởng tượng một phiên đấu giá tranh. Giá đang giằng co quanh 100 triệu, người bán đang nhỉnh hơn — vài lượt trả giá cuối còn thấp hơn một chút (đó là "cây nến giảm cuối cùng"). Đột nhiên một người mua xuất hiện và trả giá dồn dập: 105, 110, 118, 120 — nhanh đến mức gần như không có ai kịp trả giá xen giữa (đó là **displacement**, và "khoảng trống" giữa các lượt trả giá là **FVG**). Mức cao cũ 112 mà trước đó không ai vượt qua được giờ bị bỏ lại phía sau (đó là **phá cấu trúc**).

Một lúc sau, giá trôi ngược về 102–104. Câu hỏi của trader OB là: *người mua mạnh kia có trả giá lại ở vùng 100–103 không?*

- **Có thể có** — nếu anh ta vẫn muốn mua thêm mà lúc nãy chưa mua đủ vì giá chạy quá nhanh.
- **Có thể không** — nếu anh ta đã mua xong, hoặc cú tăng giá chỉ là do nhiều người bán hoảng loạn rút lui cùng lúc chứ không phải do một người mua lớn.
- **Có thể có người khác** — những ai lỡ chuyến lần trước, hoặc những ai nhìn thấy cú bật và nghĩ "vùng 100 là vùng rẻ".

**Chart chỉ cho bạn thấy cú nhảy giá. Nó không cho bạn thấy lượng cầu còn lại của người mua.** Toàn bộ nghệ thuật (và giới hạn) của OB nằm trong câu này.

> [!warning] Giới hạn của phép so sánh
> Thị trường thật có hàng nghìn người tham gia ẩn danh, lệnh được chia nhỏ, và phần lớn thanh khoản không hiển thị. Không có "một người mua" để theo dõi. Phép so sánh đúng ở cấu trúc logic (quan sát được cú nhảy, không quan sát được ý định), nhưng sai nếu bạn hiểu theo nghĩa đen là có một nhân vật cụ thể sẽ quay lại.

### 2.2 Level 1 — Những viên gạch cần có trước khi nói về OB

Các thuật ngữ dưới đây được dùng như tiền đề trong toàn bộ note:

| Thuật ngữ | Giải thích đơn giản | Ghi chú kỹ thuật |
|---|---|---|
| **Nến (OHLC)** | Tóm tắt giá trong một khoảng thời gian: Open, High, Low, Close | Ranh giới nến là **lát cắt thời gian tùy ý** — đổi giờ mở nến (broker, múi giờ) là đổi hình dạng nến |
| **Down-close / Up-close** | Nến đóng dưới giá mở / trên giá mở | Với nến giảm, **Open là đỉnh thân**; với nến tăng, Open là đáy thân |
| **Body / Wick** | Thân (Open↔Close) / râu (phần vượt ra ngoài thân) | Râu = giá đã *đi tới* nhưng *không được chấp nhận* khi nến đóng |
| **Lệnh limit** | Lệnh chờ ở một mức giá — *cung cấp* thanh khoản (passive) | Nằm trong sổ lệnh, chờ bị khớp |
| **Lệnh market** | Lệnh khớp ngay — *tiêu thụ* thanh khoản (aggressive) | Giá chỉ dịch chuyển khi lệnh market ăn hết lệnh limit ở mức giá tốt nhất |
| **Stop order** | Lệnh "ngủ", biến thành lệnh market khi giá chạm mức kích hoạt | Stop của người long nằm *dưới* đáy → khi kích hoạt thành lệnh **bán** |
| **Liquidity (ICT)** | Nơi có nhiều lệnh chờ tập trung — đặc biệt là stop trên đỉnh (BSL) và dưới đáy (SSL) | Xem [[19-Liquidity]], [[19-Liquidity#7. Buy-Side Liquidity (BSL)\|Buy-side Liquidity]], [[19-Liquidity#8. Sell-Side Liquidity (SSL)\|Sell-side Liquidity]] |
| **Swing high / low** | Đỉnh/đáy cục bộ mà giá quay đầu | Cấp độ (significance) của swing khác nhau — xem [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]], [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] |
| **BOS / MSS** | Phá swing theo hướng trend / phá swing ngược trend làm đổi narrative | [[05-BOS-Break-of-Structure]], [[21-Market-Structure-Shift]] |
| **Displacement** | Cú dịch chuyển nhanh, một chiều, thân lớn, ít chồng lấp | [[50-Displacement-In-Depth]] |
| **FVG** | Vùng giữa râu nến 1 và râu nến 3 không chồng lấp nhau | Ở khung đó, giá đi qua vùng này rất nhanh, gần như một chiều — **không** có nghĩa là "không có giao dịch nào" ở tick level |
| **ATR** | Biên độ trung bình của nến | Dùng để **chuẩn hóa** mọi khoảng cách: "0.5 ATR" có nghĩa như nhau trên EURUSD và NQ |

### 2.3 Level 2 — OB nằm ở đâu trong chuỗi sự kiện ICT

Chuỗi sự kiện "sách giáo khoa" của một Bullish OB, theo thứ tự thời gian:

```
(1) Giá giảm vào một vùng có thanh khoản bên dưới (equal lows, PDL, Asian low…)
(2) Giá quét qua đáy đó → sell stop bị kích hoạt           ← LIQUIDITY SWEEP
(3) Nến giảm cuối cùng hình thành tại/ngay sau đáy        ← ỨNG VIÊN OB
(4) Chuỗi nến tăng mạnh, thân lớn, ít chồng lấp           ← DISPLACEMENT
(5) Displacement đóng cửa vượt qua một swing high         ← BOS / MSS
(6) Displacement để lại khoảng trống 3 nến                ← FVG
(7) Giá chạy tới một mức, rồi hồi về                      ← RETRACEMENT
(8) Giá chạm (hoặc gần chạm) FVG/OB                       ← RETEST
(9) Phản ứng: MSS nhỏ trên LTF, displacement mới           ← EVIDENCE
(10) Entry theo rule → stop → target DOL                  ← EXECUTION
```

Điểm mấu chốt: **OB (bước 3) chỉ được "xác nhận" sau bước 4–5**. Tại thời điểm cây nến giảm đóng cửa, không ai biết nó là OB. Nó trở thành OB *hồi tố* khi displacement xảy ra. Đây là lý do mọi backtest OB phải ghi **thời điểm OB trở nên khả dụng** (`t_avail` = thời điểm nến xác nhận BOS/MSS đóng cửa), không phải thời điểm cây nến OB hình thành — nếu không sẽ dính **look-ahead bias** (xem §20).

### 2.4 Level 3 — OB như một đối tượng có điều kiện (advanced)

Câu hỏi nghiệp dư: *"Giá có phản ứng ở OB không?"* — Câu trả lời luôn là "có, đôi khi", vì giá phản ứng ở **mọi nơi** đôi khi. Một chuỗi giá bất kỳ đều có hàng trăm điểm quay đầu mỗi ngày trên M5.

Câu hỏi nghiên cứu đúng:

$$P(\text{phản ứng} \mid \text{OB}, \text{context}) \;\; \text{so với} \;\; P(\text{phản ứng} \mid \text{vùng đối chứng cùng độ rộng, cùng khoảng cách}, \text{context})$$

và quan trọng hơn:

$$E[R \mid \text{rule giao dịch OB}] - \text{chi phí} > 0 \;\; \text{một cách ổn định, out-of-sample?}$$

Ba hệ quả nâng cao từ cách nhìn này:

1. **OB là một vùng mờ (fuzzy region), không phải đường kẻ chính xác.** Vì ranh giới nến là lát cắt thời gian tùy ý, cùng một cú mất cân bằng sẽ tạo ra OB hơi khác nhau trên feed broker khác, múi giờ nến khác, timeframe khác. Kỳ vọng độ chính xác đến từng pip là ảo tưởng — đây là lý do kịch bản "near miss" (§12, Scenario A) là hiện tượng bình thường.
2. **OB là một nút trong hệ phân cấp.** Mỗi OB thuộc về một swing ở một cấp. OB M5 nằm trong OB H1 nằm trong OB D1. Câu hỏi "OB này có giá trị không" vô nghĩa nếu không nói *ở cấp nào, trong context nào*.
3. **Phản ứng không phải biến nhị phân.** "Bật" hay "không bật" là cách đo thô. Phản ứng nên đo bằng biến liên tục: độ xuyên (penetration %), MFE/MAE theo ATR, tốc độ, thời gian tới mục tiêu. Nhị phân hóa quá sớm làm mất thông tin và dễ bị "chọn ngưỡng cho đẹp".

---

## 3. Precise Definition of Order Block

### 3.1 Có nhiều định nghĩa OB không? — Có, và chúng mâu thuẫn nhau

Đây là sự thật đầu tiên cần chấp nhận: **"Order Block" không có một định nghĩa chuẩn duy nhất**, kể cả trong cộng đồng ICT. Các định nghĩa phổ biến:

| Mã | Định nghĩa | Nguồn gốc | Vấn đề chính |
|---|---|---|---|
| **D0 — Naive** | Nến ngược hướng cuối cùng trước một cú di chuyển | Cách hiểu đại trà | Quá rộng: mọi pullback đều sinh OB → vô dụng về mặt thống kê |
| **D1 — ICT cổ điển** | Bullish OB: "nến down-close **thấp nhất**, có **range open→close lớn nhất**, nằm **gần support**" (bearish đối xứng) [^S12] | Thường được trích dẫn từ tài liệu mentorship thời kỳ 2016–2017 (bản trích lại ở nguồn thứ cấp; note này **chưa đối chiếu được video gốc**) | Chứa các từ mơ hồ: "gần support", "range lớn nhất" so với cái gì |
| **D1b — ICT "state of delivery"** | OB = điểm chuyển từ "sell program" sang "buy program" | Cách diễn đạt ICT về sau, gắn với [[41-Change-in-State-of-Delivery]] | Mô tả chức năng, không phải thuật toán nhận diện |
| **D2 — Series OB** | Khi có chuỗi nhiều nến down-close liên tiếp, OB là **cả chuỗi** | ICT refinement | Biên OB phụ thuộc cách gom chuỗi |
| **D3 — Displacement-validated (SMC mainstream)** | Nến ngược hướng cuối cùng trước displacement **gây BOS/MSS** và thường **để lại FVG** | Phổ biến nhất hiện nay, cũng là cách [[25-OB-Order-Block]] dùng | Nếu gộp FVG + sweep vào định nghĩa thì không đo được đóng góp riêng của chúng |
| **D4 — Engulf/grab variant** | Nến impulse phải "grab" low của nến OB và **nhấn chìm thân-thân, râu-râu**, kèm FVG + MSS LTF [^S12] | Một số trang giáo dục ICT thứ cấp | Rất chặt, số mẫu ít; tiêu chí "grab" là của một biến thể, không phổ quát |
| **D5 — Orderflow (ngoài ICT)** | Vùng có absorption/delta rõ trên footprint | Orderflow trading | Cần dữ liệu volume/tick thật — không khả thi trên FX spot |

Ngoài khác biệt về *nến nào là OB*, còn khác biệt về *đo vùng thế nào*:

- **Body hay full range (có râu)?**
- **Mean Threshold (MT) hay Consequent Encroachment (CE)?** Trong nhiều nguồn ICT thứ cấp, **MT của OB được đo trên thân nến** (50% Open↔Close), còn **CE là thuật ngữ cho điểm giữa FVG/râu**. Note [[25-OB-Order-Block]] §7.1 lại định nghĩa "CE/Mean Threshold = 50% của cả cây nến (tính râu)". Hai định nghĩa này **cho ra hai mức giá khác nhau** — nếu không khai báo, backtest của bạn sẽ trộn hai biến khác nhau. (Xem Phụ lục A.)
- **Opening price:** với bullish OB (nến giảm), Open chính là **đỉnh thân** — tức "mép proximal của thân". Khi ICT nói "giá hay quay về đúng open của OB", đó là một mệnh đề về *mép thân*, không phải một mức bí ẩn thứ tư. [ICT FRAMEWORK; tính đặc biệt của mức này: HYPOTHESIS]

> [!important] Hệ quả phương pháp luận
> Vì định nghĩa không thống nhất, câu hỏi "OB có hoạt động không?" **không có nghĩa** cho đến khi bạn nói rõ: *OB theo định nghĩa nào, đo bằng body hay range, trên timeframe nào, feed nào*. Mọi thảo luận "OB win rate" trên mạng mà không khai báo các thứ này đều không so sánh được với nhau.

### 3.2 Necessary conditions vs Confluence — ba tầng

Thay vì một danh sách lẫn lộn, tách thành ba tầng. Mỗi tầng trả lời một câu hỏi khác nhau:

| Tầng | Câu hỏi | Điều kiện | Loại điều kiện |
|---|---|---|---|
| **Tầng 1 — Candidate OB** | "Đây có phải *gốc* của một cú mất cân bằng không?" | (a) Nến/chuỗi nến có close ngược hướng; (b) **ngay sau đó** là displacement đo được | **Necessary** — thiếu (b) thì chỉ là một cây nến |
| **Tầng 2 — Valid OB** | "Cú mất cân bằng đó có *hệ quả cấu trúc* không?" | (c) Displacement giao dịch vượt qua **high** của nến OB (bullish) — tiêu chí "validation" thường gán cho ICT; (d) displacement **đóng cửa** vượt một swing đã xác nhận (BOS/MSS) | **Necessary** cho khái niệm OB theo nghĩa ICT |
| **Tầng 3 — Qualified OB** | "OB này có *đáng giao dịch* trong context hiện tại không?" | Sweep trước đó, FVG, cấp swing bị phá, vị trí premium/discount, HTF alignment, freshness, khoảng cách tới DOL, phiên, tin tức… | **Confluence / quality features** — mỗi cái là một **biến cần kiểm định**, không phải điều kiện định nghĩa |

Lập luận vì sao **sweep và FVG không nằm trong định nghĩa** (dù chúng rất quan trọng trong ICT):

1. **Có OB hợp lệ không có sweep** (ví dụ OB continuation giữa trend, hoặc OB hình thành *trước* khi liquidity bị quét — edge case 21). Nếu bắt buộc sweep, bạn loại bỏ cả một lớp hiện tượng mà không kiểm tra.
2. **Có displacement không để lại FVG** vì râu chồng lấp (xem [[50-Displacement-In-Depth]] CS "không tạo FVG"). Nếu bắt buộc FVG, định nghĩa phụ thuộc vào chi tiết râu nến — một yếu tố rất nhạy với feed.
3. **Nếu nhồi mọi confluence vào định nghĩa, bạn sẽ không đo được đóng góp biên của từng confluence.** Câu hỏi "sweep có làm tăng expectancy không?" chỉ trả lời được khi dữ liệu có cả OB-có-sweep và OB-không-sweep.

> [!tip] Nguyên tắc: *Definition minimal, features rich*
> Định nghĩa càng ít điều kiện càng tốt (Tầng 1 + 2). Mọi thứ khác ghi lại như **cột dữ liệu**. Sau 200–400 mẫu, dữ liệu sẽ cho bạn biết cột nào đáng giữ — thay vì niềm tin.

### 3.3 OB-DEF v0.1 — Định nghĩa tối thiểu có thể backtest

Định nghĩa dưới đây đủ cụ thể để hai người (hoặc một đoạn code) áp dụng cho ra kết quả gần giống nhau. Mọi tham số là **HEURISTIC v0.1**, cần được khóa trước khi xem kết quả và chỉ thay đổi theo quy trình versioning (§20).

**Input:** chuỗi OHLC trên timeframe TF; `ATR_base` = ATR(14) tại nến **ngay trước** khi displacement bắt đầu (baseline trước expansion, đúng tinh thần [[50-Displacement-In-Depth]] CS5 — tránh ATR bị "phồng" bởi chính cú displacement); một swing detector có độ trễ xác nhận rõ ràng (fractal n nến hai bên, hoặc Directional Change θ — xem [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]).

**Bước 1 — Displacement leg `L` (bullish; bearish đối xứng):** một chuỗi từ 1 đến 5 nến liên tiếp (HEURISTIC) với:
- `Net_L = (Close_cuối − Open_đầu) / ATR_base ≥ 1.5` (HEURISTIC; nên chuyển sang **percentile** theo instrument × phiên — xem §19),
- trung bình `|body| / range` của các nến trong L ≥ 0.6 (HEURISTIC),
- không có nến nào trong L đóng cửa dưới Open của nến đầu tiên của L.

**Bước 2 — Hệ quả cấu trúc:** trong L (hoặc tối đa m = 3 nến sau L, HEURISTIC), có ít nhất một nến **đóng cửa** trên swing high gần nhất **đã được xác nhận trước khi L bắt đầu**. Ghi lại: swing nào, cấp nào (L1–L5, §8), là internal hay external, BOS hay MSS.

**Bước 3 — Nến OB:** nến down-close (Close < Open) gần nhất **trước** nến đầu của L, tìm lùi tối đa s = 3 nến (HEURISTIC). Nếu có nhiều nến down-close liên tiếp → ghi cả chuỗi (cờ `ob_series = true`). Nếu không tìm thấy nến down-close nào trong s nến → ghi nhận "displacement không có OB" (vẫn lưu lại — đây là edge case "FVG không có OB rõ ràng").

**Bước 4 — Đo vùng (ghi TẤT CẢ, không chọn một):**
- `ob_full = [min(Low), max(High)]` của nến/chuỗi OB,
- `ob_body = [min(Close), max(Open)]`,
- `ob_open` = Open của nến OB cuối cùng (với bullish OB = đỉnh thân),
- `mt_body` = điểm giữa `ob_body`; `ce_range` = điểm giữa `ob_full`,
- `proximal` = mép gần giá hiện tại (bullish: đỉnh), `distal` = mép xa (bullish: đáy) — ghi cho cả body và full.

**Bước 5 — Thời điểm khả dụng:** `t_avail` = thời điểm đóng cửa của nến xác nhận Bước 2. **Mọi tín hiệu dùng OB này trước `t_avail` là look-ahead.**

**Bước 6 — Validation:** kiểm tra displacement đã giao dịch vượt High của nến OB (với bullish). Gần như luôn thỏa nếu Bước 1–2 thỏa, nhưng kiểm tra tường minh để loại lỗi dữ liệu.

**Output:** một bản ghi OB với các cột ở §19. Sweep, FVG, premium/discount, HTF alignment, freshness… **đều là cột**, không phải điều kiện.

### 3.4 Những lựa chọn đo lường bắt buộc phải khai báo

| Lựa chọn | Phương án | Khuyến nghị v0.1 | Lý do |
|---|---|---|---|
| Zone | body / full | Ghi cả hai, phân tích cả hai | Chưa có bằng chứng cái nào tốt hơn — đây là câu hỏi thực nghiệm |
| Mốc giữa | `mt_body` / `ce_range` | Ghi cả hai | Tránh trộn hai định nghĩa (Phụ lục A) |
| Chuỗi nến | nến cuối / cả chuỗi | Ghi cả hai | Biên OB khác nhau đáng kể khi chuỗi dài |
| Timeframe | TF phát hiện | D1, H1, M5 riêng biệt | Mỗi TF là một quần thể khác nhau |
| Feed | broker CFD / futures | Một feed cố định cho toàn bộ nghiên cứu | Nến khác nhau giữa feed → OB khác nhau |
| ATR baseline | tại thời điểm trước L | ATR(14) pre-expansion | Nhất quán với note 50 |
| Swing detector | fractal n / DC θ | Chọn một, khóa tham số | Độ trễ xác nhận quyết định `t_avail` |

---

## 4. Market Mechanism — cơ chế thị trường đằng sau hành vi quan sát được

### 4.1 Trước displacement: điều gì thực sự quan sát được?

**Quan sát được (observable):**
- Giá đang giảm hoặc đi ngang, thường tiến vào một vùng có mức giá "hiển nhiên" bên dưới (đáy cũ, equal lows, PDL, Asian low).
- Nhiều trường hợp giá xuyên qua mức đó một đoạn ngắn (sweep), rồi nến giảm cuối cùng đóng cửa.
- Nến giảm cuối cùng là **nến cuối cùng mà phe bán "thắng" trong khoảng thời gian của nến đó** (Close < Open). Không hơn, không kém.

**Cơ chế đã được ghi nhận:**
- **Stop-loss tụ lại ngay phía sau các mức giá hiển nhiên.** Dữ liệu lệnh thật của một ngân hàng FX cho thấy take-profit tụ mạnh *tại* số tròn còn stop-loss tụ mạnh *ngay phía sau* số tròn [^S1]. Khi giá chạm vùng stop, các lệnh này biến thành lệnh market cùng chiều, tạo **phản hồi dương** (positive feedback) — giá chạy nhanh bất thường, và phản ứng này lớn hơn, kéo dài hơn phản ứng tại vùng take-profit [^S2]. [MARKET MECHANICS]
- Hệ quả logic: khi giá quét qua một đáy hiển nhiên, **một lượng lệnh bán bị ép xuất hiện** (sell stops kích hoạt). Với bất kỳ ai muốn **mua khối lượng lớn**, đây là thời điểm có sẵn đối ứng. [MARKET MECHANICS cho phần "có đối ứng"; INTERPRETATION cho phần "có người cố ý chờ để mua"]

> [!note] Lưu ý phạm vi bằng chứng
> Nghiên cứu của Osler dùng lệnh thật từ một ngân hàng và tập trung vào **số tròn**, không phải swing high/low. Việc mở rộng sang swing points là suy luận hợp lý (cả hai đều là "mức hiển nhiên") nhưng **không phải điều đã được chứng minh trong nghiên cứu đó**. Osler cũng lưu ý hiệu ứng có ý nghĩa thống kê trong **hàng giờ, không phải hàng ngày** [^S2].

### 4.2 Trong displacement: một hình dạng nến, nhiều nguyên nhân khả dĩ

**Cơ chế khớp lệnh:** giá tăng nhanh khi lượng mua chủ động (market buy) vượt quá tốc độ bổ sung lệnh bán limit. Giá "leo" qua các tầng của sổ lệnh; mỗi mức giá chỉ có ít giao dịch hai chiều → thân nến dài, râu ngắn, các nến ít chồng lấp nhau → FVG xuất hiện ở khung thời gian quan sát. [MARKET MECHANICS]

Nhưng **cùng một hình dạng displacement** có thể sinh ra từ các nguyên nhân rất khác nhau, và mỗi nguyên nhân có hàm ý khác nhau cho OB phía sau:

| Nguyên nhân | Mô tả | Hàm ý cho OB khi giá quay lại |
|---|---|---|
| **(a) Sponsored buying** | Một/một nhóm người mua lớn chủ động mua (thông tin, tái cân bằng danh mục, hedging) | Có thể còn nhu cầu mua chưa khớp → OB *có cơ sở* để giữ [INTERPRETATION] |
| **(b) Stop cascade** | Buy-stop của phe short bị kích hoạt dây chuyền khi giá vượt các đỉnh hiển nhiên [^S2] | Không ai "muốn" mua ở gốc — họ bị *ép* mua. Khi cascade cạn, giá có thể hồi sâu → OB yếu hơn [HYPOTHESIS] |
| **(c) News repricing** | Tin tức làm thay đổi "giá hợp lý"; market maker rút báo giá, giá nhảy tới mặt bằng mới | Gốc displacement thuộc về *chế độ giá cũ*; OB tiền-tin có thể không còn ý nghĩa [HYPOTHESIS] |
| **(d) Hỗn hợp** | Phổ biến nhất: sponsored flow kích hoạt stop, stop kích hoạt thêm momentum traders | Không tách được chỉ bằng nến |

> [!warning] Giới hạn cốt lõi
> Trên FX spot (OTC, phi tập trung) **không có sổ lệnh hợp nhất và không có volume tập trung** để phân biệt (a), (b), (c). Trên NQ futures có volume và sổ lệnh CME, nhưng vẫn **ẩn danh**. Nghĩa là: trên chart nến, **bạn không thể biết displacement là "tổ chức mua" hay "phe short bị ép"**. Mọi câu "đây là dấu chân smart money" đều vượt quá dữ liệu.

Một số biến quan sát được *có thể* giúp phân biệt một phần (đều là [HYPOTHESIS]): displacement bắt đầu **trước** hay **sau** khi vượt một vùng stop hiển nhiên; có timestamp tin tức trong ±5 phút không; volume (với futures) tăng đột biến ở nến đầu hay dồn về cuối chuỗi.

### 4.3 Vì sao vùng gốc displacement *có thể* trở thành POI? — Sáu cơ chế cạnh tranh

Đây là phần quan trọng nhất của note về mặt tư duy. Có ít nhất sáu cơ chế có thể giải thích vì sao giá hay phản ứng gần OB. Điểm mấu chốt: **mỗi cơ chế dự đoán một dấu vết thống kê khác nhau** — nên backtest được thiết kế tốt có thể phân biệt chúng.

**M1 — Metaorder chưa khớp xong.** [INTERPRETATION]
Người giao dịch lớn hiếm khi đặt một lệnh khổng lồ; họ chia lệnh mẹ (metaorder) thành nhiều lệnh con thực hiện trong nhiều giờ/ngày — đây là thực tế đã được ghi nhận trong nghiên cứu cấu trúc thị trường [^S11]. Nếu giá chạy đi quá nhanh khi lệnh mẹ chưa khớp xong, phần còn lại có thể được đặt lại ở vùng giá tốt hơn — tức gần gốc displacement.
*Dự đoán:* phản ứng mạnh hơn khi OB **còn mới**; **suy giảm theo thời gian** (lệnh mẹ rồi cũng xong); mạnh hơn khi displacement xảy ra trong phiên thanh khoản cao.

**M2 — Impact reversion (hồi quy tác động giá).** [MARKET MECHANICS cho cổ phiếu; mở rộng sang FX/NQ intraday là INTERPRETATION]
Trên dữ liệu ~8 triệu metaorder cổ phiếu Mỹ, khi metaorder kết thúc, tác động giá bắt đầu hồi lại: đến cuối ngày còn khoảng **2/3 tác động đỉnh**, và tiếp tục suy giảm trong các ngày sau [^S6]. Nghĩa là **một phần của cú đẩy giá tự nhiên hồi lại** sau khi dòng lệnh chủ động dừng.
*Dự đoán:* việc giá **hồi về phía gốc** là tính chất chung của mọi cú đẩy, *không riêng gì OB*. Phân bố độ sâu hồi là **rộng và trơn**, không tập trung đặc biệt ở mép OB. → Đây là lý do "giá đã quay về OB" **không phải bằng chứng** OB có sức hút.

**M3 — Trapped traders và thoát lệnh hòa vốn.** [INTERPRETATION — hành vi]
Những người bán trong nến OB, hoặc short theo cú phá đáy (sweep), đang lỗ khi displacement xảy ra. Khi giá quay về điểm vào của họ, một phần sẽ thoát ở hòa vốn → lệnh mua đóng short tập trung quanh thân nến OB/vùng sweep.
*Dự đoán:* phản ứng tập trung quanh **thân nến OB và vùng sweep**; mạnh hơn khi cú sweep thu hút nhiều lệnh breakout (ví dụ quét equal lows rất rõ ràng).

**M4 — Sự chú ý tự hiện thực hóa và lệnh limit tụ lại.** [MARKET MECHANICS cho S/R nói chung; HYPOTHESIS cho OB]
Kavajecz & Odders-White cho thấy các mức support/resistance **trùng với các đỉnh độ sâu trên sổ lệnh limit** — và quan hệ này đến từ việc các quy tắc kỹ thuật *định vị* được độ sâu đã có sẵn [^S3]. Garzarelli và cộng sự phát hiện giá cổ phiếu LSE (dữ liệu 2002, thang thời gian 45–180 giây) **bật lại nhiều hơn là xuyên qua** các mức S/R được phát hiện, và xác suất bật **tăng theo số lần bật trước đó**, trong khi chuỗi giá xáo trộn ngẫu nhiên cho xác suất ~0.5 không đổi [^S4]. Chung & Bellotti (preprint) cũng ghi nhận mức S/R có nhiều lần bật trước đó dễ bật lại hơn, và xác suất bật **giảm dần theo thời gian** [^S5].
*Dự đoán:* OB càng "hiển nhiên" (HTF, sạch, được nhiều người vẽ) càng dễ có phản ứng — nhưng đồng thời **stop cũng tụ ngay sau distal** (cơ chế M5).

**M5 — Cụm stop phía sau distal.** [MARKET MECHANICS (cơ chế stop cascade) + INTERPRETATION (áp dụng cho OB)]
Người long tại OB đặt stop dưới distal → một pool sell-stop hình thành ngay dưới OB. Pool này vừa là **đối ứng cho người mua lớn** (quét rồi đảo), vừa là **nhiên liệu cho cú phá** (cascade) [^S1][^S2].
*Dự đoán:* hành vi tại distal có tính **lưỡng cực (bimodal)** — hoặc quét nhanh rồi lấy lại (Scenario D), hoặc phá mạnh và chấp nhận giá bên ngoài (Scenario F). Ít khi "lình xình vừa phải".

**M6 — Giả thuyết không (null): ngẫu nhiên + chọn lọc.** [HYPOTHESIS H0]
Trong một chuỗi giá nhiễu có xu hướng, các nhịp hồi phải kết thúc *ở đâu đó*. Khi dưới giá có nhiều vùng OB ứng viên, xác suất một điểm quay đầu ngẫu nhiên rơi "trúng hoặc gần" một OB là cao (tính minh họa ở §14.3).
*Dự đoán:* tỷ lệ phản ứng tại OB ≈ tỷ lệ phản ứng tại **vùng đối chứng** cùng độ rộng, cùng khoảng cách.

**Bảng so sánh dấu vết thống kê mà mỗi cơ chế dự đoán:**

| Dấu vết | M1 Metaorder | M2 Reversion | M3 Trapped | M4 Attention | M5 Stop cluster | M6 Null |
|---|---|---|---|---|---|---|
| OB mới vs cũ | Mới mạnh hơn rõ | Không khác | Mới mạnh hơn | Có thể **cũ mạnh hơn** nếu đã được "xác nhận" | — | Không khác |
| Suy giảm theo thời gian | Có | Có (theo thời gian từ cú đẩy) | Có | Có (theo [^S5]) | — | Không |
| Số lần chạm trước | Mỗi lần chạm làm cạn | — | Mỗi lần chạm làm cạn | **Nhiều lần bật → bật dễ hơn** [^S4][^S5] | Stop dày thêm sau mỗi lần giữ | Không khác |
| Vị trí phản ứng trong zone | Quanh gốc | Phân bố rộng | Quanh thân/vùng sweep | Quanh mép hiển nhiên (proximal) | Sau distal | Đều |
| Hành vi tại distal | — | — | — | — | **Lưỡng cực** | Không đặc biệt |
| OB vs vùng đối chứng | OB > đối chứng | OB ≈ đối chứng | OB > đối chứng | OB > đối chứng nếu OB "phổ biến" | — | **OB ≈ đối chứng** |

> [!important] Một mâu thuẫn quan trọng cần kiểm chứng
> ICT (và note 25) nói **"first touch mạnh hơn second touch; mỗi lần mitigate OB yếu đi"**. Bằng chứng S/R lân cận [^S4][^S5] lại cho thấy **mức có nhiều lần bật trước đó dễ bật hơn**. Hai mệnh đề này dự đoán ngược nhau. Có thể cả hai đều đúng ở những điều kiện khác nhau (ví dụ: "chạm" nông khác "mitigate" sâu; S/R trên cổ phiếu 45 giây khác OB H1 trên FX). **Đây chính xác là loại câu hỏi mà backtest của bạn nên trả lời** — xem HYP-OB-006.

### 4.4 Điều chúng ta KHÔNG thể biết từ chart

1. **Danh tính và ý định** của người tạo displacement.
2. **Lượng lệnh còn lại** (nếu có) tại vùng OB. Lệnh limit có thể bị hủy bất cứ lúc nào; lệnh chờ không phải cam kết.
3. Displacement là **sponsored hay cascade hay tin tức** (trên FX spot không có volume tập trung).
4. Phản ứng khi retest là do **"lệnh OB cũ"** hay do **người tham gia mới** (M4) hay chỉ là **nhịp hồi ngẫu nhiên kết thúc** (M6).
5. Liệu cùng một vùng có "tồn tại" trên feed/timeframe khác hay không — OB là sản phẩm của cách lấy mẫu dữ liệu.

**Điều chart CÓ cho biết:** vị trí gốc của cú mất cân bằng; cấp độ cấu trúc mà nó phá; thanh khoản nào đã bị lấy; và **nơi mà luận điểm cấu trúc sai** nếu bị phá. Chỉ riêng những điều này đã đủ để xây một hệ thống có kỷ luật — miễn là không đòi hỏi chart nói nhiều hơn những gì nó có.

---

## 5. ICT Interpretation — ICT giải thích hiện tượng này thế nào

### 5.1 Narrative gốc [ICT FRAMEWORK]

Trong ICT, giá được "giao" (delivered) bởi một cơ chế thuật toán (IPDA) đi lại giữa các vùng thanh khoản và các vùng mất hiệu quả (inefficiency). Order Block được giải thích như sau:

1. **Smart money cần thanh khoản để khớp lệnh lớn.** Để mua lượng lớn, họ cần người bán → giá được đẩy xuống quét sell-side liquidity (stop dưới đáy).
2. **Nến down-close cuối cùng** chứa hoạt động của smart money: họ bán (hoặc để giá giảm) nhằm kích hoạt stop, đồng thời tích lũy vị thế mua.
3. **Displacement** là lúc chương trình mua chạy thật sự — "change in the state of delivery from a sell program to a buy program".
4. **Mitigation:** khi giá quay lại OB, smart money **"mitigate"** — đóng các vị thế bán đang lỗ từ lúc tạo OB ở mức hòa vốn và/hoặc bổ sung vị thế mua. Đây là nghĩa gốc của từ "mitigation" trong ICT (giảm thiểu lỗ), khác với nghĩa phổ thông "giá chạm vùng".
5. **Validation & Mean Threshold (theo cách thường được trích dẫn):** OB được xác nhận khi giá giao dịch vượt High của nến down-close; khi giá quay lại, việc **thân nến đóng cửa vượt quá Mean Threshold (50% thân)** là dấu hiệu sớm OB đang yếu/không còn hiệu lực [^S12].
6. **PD array trong premium/discount:** chỉ dùng bullish OB ở discount, bearish OB ở premium của dealing range liên quan.
7. **Trong 2022 Mentorship Model**, PD array thực thi tiêu chuẩn sau MSS là **FVG**; OB đóng vai trò POI khung lớn hoặc phương án entry thay thế. → Trong framework D1 → H1 → M5 của bạn, OB chủ yếu là **công cụ định vị**, không phải trigger.

### 5.2 Đặt ICT narrative cạnh giải thích cấu trúc thị trường

| Thành phần | ICT nói | Cấu trúc thị trường nói | Khác biệt cốt lõi |
|---|---|---|---|
| Sweep trước OB | Smart money "đi săn" stop để lấy thanh khoản | Stop tụ sau mức hiển nhiên; khi kích hoạt tạo lệnh market cùng chiều [^S1][^S2]. Bất kỳ ai cần khối lượng đều hưởng lợi | ICT gán **ý định**; cơ chế chỉ cần **cấu trúc lệnh** |
| Nến OB | Nơi smart money tích lũy | Nến cuối cùng mà phe bán thắng trong khung thời gian đó | ICT gán **danh tính**; chart chỉ cho **kết quả ròng** |
| Displacement | Chương trình mua của tổ chức | Mua chủ động > bổ sung lệnh bán; có thể là sponsored, cascade hoặc tin tức | Không phân biệt được trên nến |
| Giá quay lại | Thuật toán quay về để mitigate | Impact reversion [^S6] + nhịp hồi thông thường + người tham gia mới | ICT: có "lý do" quay lại; cơ chế: hồi là **mặc định thống kê** |
| Phản ứng tại OB | Lệnh tổ chức còn ở đó | Có thể: metaorder dở dang, thoát hòa vốn, lệnh limit tụ do chú ý chung [^S3] | ICT: một nguyên nhân; thực tế: nhiều nguyên nhân chồng lấp |
| OB fail | "Không phải OB thật" / "đã thành breaker" | Cụm stop sau distal bị kích hoạt; hoặc chẳng có lệnh nào ở đó cả | ICT narrative có thể **giải thích mọi kết quả** → nguy cơ không thể bác bỏ |

> [!quote] Đánh giá trung thực
> Narrative ICT là **một mô hình làm việc hữu ích** để tổ chức quan sát (sweep → displacement → origin → return). Vấn đề chỉ xuất hiện khi narrative được dùng như **bằng chứng**: "giá phản ứng ở OB vì smart money ở đó" là một câu không thể kiểm chứng bằng chart. Câu kiểm chứng được là: "OB thỏa điều kiện X có tỷ lệ phản ứng/expectancy cao hơn vùng đối chứng trong dữ liệu Y".

---

## 6. Fact vs Interpretation — bảng phân loại mệnh đề

| # | Mệnh đề | Nhãn | Ghi chú |
|---|---|---|---|
| 1 | Giá chỉ dịch chuyển khi lệnh chủ động tiêu thụ lệnh limit | [MARKET MECHANICS] | Cơ chế khớp lệnh cơ bản |
| 2 | Stop-loss tụ ngay sau các mức giá hiển nhiên; khi kích hoạt, giá tăng tốc | [MARKET MECHANICS] | Có bằng chứng FX với số tròn [^S1][^S2]; mở rộng sang swing = INTERPRETATION |
| 3 | Mức S/R trùng với các đỉnh độ sâu sổ lệnh | [MARKET MECHANICS] | Bằng chứng trên sổ lệnh cổ phiếu [^S3] |
| 4 | Sau khi dòng lệnh lớn dừng, một phần tác động giá hồi lại | [MARKET MECHANICS] | Bằng chứng trên metaorder cổ phiếu [^S6] |
| 5 | OB là nến ngược hướng cuối cùng trước displacement phá cấu trúc | [ICT FRAMEWORK] | Một trong nhiều định nghĩa (§3.1) |
| 6 | Smart money đặt lệnh ở OB và quay lại mitigate | [ICT FRAMEWORK] → không kiểm chứng được | Danh tính/ý định không quan sát được |
| 7 | Có thể còn nhu cầu mua chưa khớp ở gốc displacement | [INTERPRETATION] | Hợp lý vì metaorder được chia nhỏ [^S11], nhưng không quan sát được |
| 8 | Giá phản ứng tại OB nhiều hơn vùng đối chứng | [HYPOTHESIS] [BACKTEST REQUIRED] | Câu hỏi nền tảng nhất — HYP-OB-001 |
| 9 | OB có sweep trước đó tốt hơn OB không sweep | [HYPOTHESIS] [BACKTEST REQUIRED] | HYP-OB-003 |
| 10 | OB tạo FVG tốt hơn OB không tạo FVG | [HYPOTHESIS] [BACKTEST REQUIRED] | HYP-OB-004 |
| 11 | OB chưa bị chạm (fresh) mạnh hơn OB đã chạm | [HYPOTHESIS] — **có bằng chứng lân cận ngược chiều** | [^S4][^S5]; HYP-OB-006 |
| 12 | CE/MT 50% là mức phản ứng đáng tin nhất | [HYPOTHESIS] | Chưa có cơ chế nào dự đoán riêng mức 50% — HYP-OB-007 |
| 13 | Râu xuyên distal chưa phải invalidation, thân đóng qua mới là | [ICT FRAMEWORK] → rule cần test | Hợp lý theo M5, nhưng ngưỡng cụ thể là HEURISTIC |
| 14 | "3 nến đóng ngoài OB = OB chết" | HEURISTIC [BACKTEST REQUIRED] | §12 Scenario F |
| 15 | Structural OB đặt điểm vào gần điểm luận điểm sai → R:R bất đối xứng | [INTERPRETATION] có cơ sở hình học | Là thuộc tính hình học; expectancy vẫn cần test |
| 16 | Thị trường tạo OB giả để bẫy trader ICT | [INTERPRETATION] không kiểm chứng được | Có giải thích đơn giản hơn (§14) |
| 17 | D1 alignment cải thiện kết quả của setup M5 | [HYPOTHESIS] [BACKTEST REQUIRED] | Tiền đề của chính framework — HYP-OB-010 |

---

## 7. Anatomy of a High-Quality OB — phân tích từng thành phần

Với mỗi thành phần, trả lời bốn câu: **Nó là gì? Vì sao có thể quan trọng (cơ chế nào ở §4.3)? Đo thế nào? Nó là đặc trưng *mô tả* hay đã được chứng minh là *dự đoán*?**

### 7.0 Phân biệt descriptive feature và predictive feature

- **Descriptive feature** mô tả *quá khứ* của OB: "OB này sinh ra một cú displacement 3 ATR", "OB này quét equal lows". Đo được, khách quan — nhưng **chưa nói gì về tương lai**.
- **Predictive feature** là đặc trưng đã được chứng minh (trên dữ liệu, out-of-sample) là làm thay đổi xác suất/expectancy của phản ứng khi retest.
- **Hầu hết "tiêu chí OB chất lượng" trong cộng đồng ICT là descriptive** được *giả định* là predictive. Việc biến chúng thành predictive là công việc của backtest, không phải của lời giảng.
- **Bẫy "đặc trưng nhiễm kết quả" (outcome-contaminated):** bất kỳ đặc trưng nào chỉ biết được *sau* khi retest diễn ra (ví dụ "OB đã giữ được giá", "leg đi được bao xa tính đến đỉnh cuối cùng") **không được dùng làm biến dự đoán**. "Khoảng cách giá đã đi" phải đo **tới thời điểm retest**, không phải tới đỉnh của cả leg.

### 7.1 Liquidity event tại/trước OB

- **Là gì:** giá quét qua một mức thanh khoản hiển nhiên ngay trước hoặc chính trong nến OB. Trường hợp mạnh nhất về mặt narrative: **râu của chính nến OB là cú quét** ("self-sweep").
- **Vì sao có thể quan trọng:** cung cấp đối ứng cho người mua lớn (M1), tạo nhóm trader bị kẹt (M3), đánh dấu một cú mở rộng thất bại.
- **Đo:** `sweep_prior` (có/không), `swept_level_class` (L1–L5 của mức bị quét: equal lows H1? PDL? Asian low?), `sweep_depth_atr`, `bars_sweep_to_disp`.
- **Trạng thái:** descriptive. Predictive = **HYP-OB-003**. Lưu ý: cấp của mức bị quét quan trọng hơn chuyện "có quét hay không" — quét một micro low M5 gần như luôn xảy ra.

### 7.2 Displacement

- **Là gì:** chuỗi nến một chiều, thân lớn, ít chồng lấp, bắt đầu ngay sau OB.
- **Vì sao có thể quan trọng:** là bằng chứng một bên đã áp đảo; càng mạnh càng khó giải thích bằng nhiễu.
- **Đo:** `disp_net_atr`, `disp_body_ratio_mean`, `disp_overlap`, `disp_bars`, `disp_speed` (ATR mỗi nến), percentile của `disp_net_atr` theo instrument × phiên.
- **Trạng thái:** descriptive; predictive = **HYP-OB-002**.
- **Bẫy chọn mẫu khi retest (quan trọng):** displacement càng mạnh, giá càng đi xa, **càng ít khả năng quay lại OB trong khung thời gian hợp lý**. Các OB *được retest* có thể thiên về những OB có động lượng yếu dần. Vì vậy phải phân tích tách biệt: `P(retest | OB)` và `P(phản ứng | retest)`. Nếu chỉ nhìn các OB đã được retest, bạn đang nhìn một mẫu đã bị chọn lọc.

### 7.3 Hệ quả cấu trúc

- **Là gì:** displacement phá swing nào — cấp nào, internal hay external, BOS hay MSS.
- **Vì sao quan trọng:** đây là thứ **nâng cấp** swing gốc thành swing được bảo vệ (protected). Một đáy dẫn tới việc phá đỉnh external trở thành "đáy phải giữ" của cấu trúc tăng — OB tại đó thừa hưởng vai trò này (§8).
- **Đo:** `broken_swing_level` (L1–L5), `break_type` (BOS/MSS), `break_internal_external`, `break_margin_atr` (khoảng cách close vượt swing, theo ATR).
- **Trạng thái:** đây là **biến phân cấp chính** của note này. Predictive = **HYP-OB-005**.

### 7.4 FVG để lại

- **Là gì:** khoảng trống 3 nến trong displacement.
- **Vì sao có thể quan trọng:** bằng chứng tốc độ/một chiều; đồng thời là **POI nông hơn** nằm phía trên OB (bullish).
- **Đo:** `fvg_present`, `fvg_size_atr`, `fvg_filled_before_ob_touch` (FVG bị lấp hoàn toàn trước khi giá chạm OB?).
- **Tương tác quan trọng:** nếu giá phản ứng ngay tại FVG, **OB không bao giờ được test** — đây không phải "OB fail" mà là "OB không được hỏi đến". Nếu giá lấp trọn FVG mà không phản ứng, OB phía dưới trở thành "phòng tuyến tiếp theo".
- **Trạng thái:** predictive = **HYP-OB-004**.

### 7.5 Origin of leg vs mid-leg

- **Là gì:** OB nằm ngay tại cực trị swing (điểm xuất phát của cả leg) hay nằm giữa một leg đang chạy.
- **Vì sao có thể quan trọng:** OB tại origin trùng với swing được bảo vệ; OB mid-leg chỉ là một trạm nghỉ.
- **Đo:** `ob_at_swing_extreme` = |distal − swing extreme| ≤ 0.1 ATR (HEURISTIC).

### 7.6 Vị trí trong dealing range

- **Là gì:** OB nằm ở premium hay discount — **của range nào** (D1? H1?) và **tại thời điểm nào** (lúc hình thành hay lúc retest — range có thể đã re-map, xem [[37-Re-mapping-Dealing-Range-sau-Displacement]]).
- **Đo:** `pd_pos_h1 = (ob_mid − range_low) / (range_high − range_low)` tại thời điểm retest; tương tự `pd_pos_d1`.
- **Trạng thái:** ICT coi là gần như bắt buộc; predictive = **HYP-OB-008**.

### 7.7 HTF alignment

- **Đo:** `d1_bias` (dấu), `ob_inside_htf_poi` (có nằm trong D1/H4 PD array cùng hướng?), `h1_structure_dir`.
- **Trạng thái:** tiền đề của chính framework — **HYP-OB-010**. Nếu dữ liệu cho thấy D1 alignment không cải thiện kết quả M5, cả kiến trúc D1 → H1 → M5 cần xem lại.

### 7.8 Freshness và lịch sử mitigation

- **Đo:** `touch_count` (số lần giá vào trong ε của proximal), `penetration_max_pct` các lần trước, `body_close_beyond_mt_count`.
- **Trạng thái:** ICT: fresh > mitigated; bằng chứng S/R lân cận gợi ý chiều ngược lại [^S4][^S5]. **HYP-OB-006** — một trong những câu hỏi đáng trả lời nhất.

### 7.9 Khoảng cách tới DOL và thanh khoản đối diện

- **Đo:** `dist_to_dol_R` (khoảng cách tới DOL tính bằng R nếu stop ở distal), `opposing_pd_array_between` (có PD array HTF ngược hướng chắn đường không?), `dist_to_opposing_liq_atr`.
- **Vì sao quan trọng:** một OB đẹp mà không có "đường chạy" tới DOL thì R:R bị giới hạn ngay từ đầu.

### 7.10 Hành vi sau khi hình thành

- **Đo (tới thời điểm retest):** `travel_before_retest_atr`, `bars_to_retest`, `new_bos_since_formation` (đã có BOS mới chưa → OB có bị "supersede" không).

### 7.11 Thời gian kể từ khi hình thành

- **Đo:** `age_bars`, `age_sessions`. Dự đoán của M1/M3/M4 đều nói có suy giảm theo thời gian — nhưng tốc độ khác nhau. **HYP-OB-009**.

### 7.12 Độ rộng so với ATR

- **Đo:** `ob_width_atr` (full và body).
- **Vì sao quan trọng:** quá hẹp (< ~0.1 ATR hoặc < ~3 lần spread, HEURISTIC) → vùng nằm trong nhiễu spread; quá rộng (> ~1.5 ATR, HEURISTIC) → stop theo distal không quản trị được, phải refine xuống LTF.

### 7.13 Phiên và tin tức

- **Đo:** `session_formation`, `session_retest`, `news_within_30m` (khi hình thành và khi retest).
- **Vì sao:** cùng một hình dạng nến trong phiên Á mỏng và trong NY AM có ý nghĩa thanh khoản khác nhau ([[50-Displacement-In-Depth]] CS3; [[18-Kill-Zones]]).

### 7.14 Độ rõ ràng của invalidation

- **Đo:** `invalidation_coincides_structure` = distal (hoặc sweep low) có trùng/sát với swing được bảo vệ không.
- **Vì sao:** đây là nguồn của "hình học rủi ro" ở §1 mệnh đề 5. OB mà distal không trùng với bất kỳ điểm cấu trúc nào → stop là một con số tùy ý.

**Bảng tổng hợp:**

| Thành phần | Biến đo | Khách quan? | Rủi ro look-ahead | Trạng thái predictive |
|---|---|---|---|---|
| Sweep | `sweep_prior`, `swept_level_class`, `sweep_depth_atr` | Cao (nếu level class có quy tắc) | Thấp | HYP-OB-003 |
| Displacement | `disp_net_atr`, `disp_body_ratio_mean`, `disp_overlap` | Cao | Trung bình (ATR baseline) | HYP-OB-002 |
| Cấu trúc | `broken_swing_level`, `break_type`, `break_margin_atr` | Trung bình (phụ thuộc swing detector) | **Cao** (độ trễ xác nhận swing) | HYP-OB-005 |
| FVG | `fvg_present`, `fvg_size_atr` | Cao | Thấp | HYP-OB-004 |
| Origin | `ob_at_swing_extreme` | Cao | Trung bình | HYP-OB-005 |
| Premium/Discount | `pd_pos_h1`, `pd_pos_d1` | Trung bình (chọn range) | **Cao** (range re-map) | HYP-OB-008 |
| HTF alignment | `d1_bias`, `ob_inside_htf_poi` | Thấp–trung bình (bias là phán đoán) | Cao | HYP-OB-010 |
| Freshness | `touch_count`, `penetration_max_pct` | Cao | Thấp | HYP-OB-006 |
| DOL room | `dist_to_dol_R`, `opposing_pd_array_between` | Trung bình | Trung bình | HYP-OB-011 |
| Tuổi | `age_bars` | Cao | Thấp | HYP-OB-009 |
| Độ rộng | `ob_width_atr` | Cao | Thấp | Biến kiểm soát |
| Phiên/tin | `session_*`, `news_within_30m` | Cao | Thấp | HYP-OB-012 |

---

## 8. OB Classification & Hierarchy — Micro → Internal → Structural → HTF

![[OB-DeepResearch-Hierarchy.svg|760]]
*Hình 2 — Một uptrend H1 với năm OB. Chỉ OB-B là structural: nó là gốc của leg đã phá external high, nên đáy của nó là protected low của dealing range hiện tại. OB-A là gốc của cả move nhưng leg từ nó không phá gì → chỉ là reference sâu trong zone HTF. OB-C/D là internal, OB-E là micro. Sau BOS mới, dealing range re-map và vai trò structural chuyển sang OB mới.*

### 8.1 Nguyên lý nền: cấp của OB = cấp của cấu trúc mà displacement của nó phá

Đây là mệnh đề trung tâm để giải bài toán phân cấp:

> [!important] Nguyên lý thừa kế
> **Một đáy trở thành "protected low" vì cú đi lên từ nó đã phá một đỉnh có ý nghĩa.** Vì vậy cấp của một bullish OB được quyết định bởi **cấp của swing high mà displacement từ OB đó phá vỡ** — không phải bởi kích thước cây nến OB. OB chỉ là dấu vết giá tại gốc của swing; ý nghĩa nằm ở swing.

Hệ quả: để phân cấp OB, trước hết phải có **hệ phân cấp swing** (L1 micro → L5 major HTF) — chính là khung Swing Classification trong framework của bạn và [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]] (STL/ITL/LTL), [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]], [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]. Một cách lượng hóa: dùng Directional Change với nhiều ngưỡng θ (ví dụ θ = 0.5, 1, 2, 4 × ATR_D1 — HEURISTIC); cấp của một swing = ngưỡng θ lớn nhất mà điểm đó vẫn là turning point.

### 8.2 Bốn cấp OB

| Cấp | Định nghĩa vận hành | Vai trò hợp lý | Giá trị độc lập |
|---|---|---|---|
| **Level 1 — Micro OB** | Gốc của displacement chỉ phá micro swing (fractal 1–2 nến) hoặc không phá gì; thường trên M5/M1 | **Chỉ** dùng để refine entry/stop *sau khi* đã có bằng chứng ở cấp cao hơn | Gần như nhiễu nếu đứng một mình |
| **Level 2 — Internal OB** | Gốc của một leg phá **internal structure** bên trong dealing range hiện tại, nhưng không phá cực trị của range | POI continuation trong trend mạnh; mục tiêu hồi (IRL); **ứng viên inducement** | Có điều kiện (xem 8.4) |
| **Level 3 — Structural OB** | Gốc của leg phá **external structure** của TF (cực trị dealing range) → nằm tại **protected swing**; nếu bị phá (acceptance) thì cấu trúc TF đổi | POI chính trên TF đó; invalidation trùng với invalidation cấu trúc | Cao nhất trên TF đó (về mặt logic) |
| **Level 4 — HTF OB** | Structural OB của D1/H4/W1; chứa nhiều cấu trúc LTF bên trong | **Context/zone** để xuống LTF tìm setup; không giao dịch trực tiếp vì quá rộng | Là bộ lọc, không phải trigger |

### 8.3 Các quy tắc phân cấp — OB-HIER v0.1

**R-H1 — Override (HTF lấn át LTF).** Bên trong một zone Level 4 bullish còn hiệu lực, một bearish OB M5/H1 được đọc là **đặc điểm internal ngược context** (thường là nơi tích tụ thanh khoản/inducement), không phải tín hiệu short — **trừ khi** zone HTF đã bị invalidate (acceptance bên ngoài distal, §12F). [INTERPRETATION; lợi ích của rule: HYP-OB-010]

**R-H2 — Nested OB có ý nghĩa khi nó là "tiếng nói LTF của phản ứng HTF".** Một OB LTF bên trong OB HTF chỉ có giá trị refinement nếu nó **hình thành sau khi giá đã vào zone HTF** và là **gốc của một MSS LTF theo hướng HTF**. OB LTF đã tồn tại từ trước khi giá vào zone chỉ là một OB cũ nằm chồng lên — không mang thông tin về phản ứng hiện tại.

**R-H3 — Supersession (thay thế sau BOS).** Khi có BOS mới trên TF: re-map dealing range; swing low tạo ra BOS trở thành protected low mới; OB tại đó trở thành **structural OB đang hoạt động**. Structural OB cũ bị **hạ xuống "reference sâu"** — chỉ có liên quan trở lại nếu protected low mới bị phá. Đây là cách xử lý chuỗi OB₁ → OB₅ trong một trend.

**R-H4 — Khi nào internal OB vẫn có giá trị.** Internal OB đáng xem xét khi đồng thời: (a) trend đang ở pha **expansion** với các nhịp hồi nông (displacement gần nhất mạnh, percentile cao); (b) cùng hướng HTF và DOL chưa bị chạm; (c) có FVG nằm trong/sát OB; (d) retest xảy ra trong kill zone. Ngoài các điều kiện đó, coi internal OB là **mục tiêu hồi / inducement**, không phải POI để mua.

**R-H5 — Khi nào OB chỉ là noise.** Một trong các điều kiện: không có hệ quả cấu trúc; hình thành bên trong consolidation với các nến chồng lấp dày; `ob_width_atr` < 0.1 hoặc độ rộng < 3 lần spread (HEURISTIC); hình thành trong giờ thanh khoản mỏng mà không được phiên sau xác nhận; hình thành bởi một nến tin (spike). Ghi nhận vào dữ liệu với cờ `noise_flag`, không xóa — để kiểm tra xem "noise" có thật sự kém hơn không.

**R-H6 — Gộp nhiều OB thành một zone.** Gộp khi: (a) cùng một swing gốc (chuỗi nến down-close liên tiếp, hoặc cách nhau ≤ 2 nến mà không có BOS xen giữa); hoặc (b) khoảng trống giữa hai zone < 0.25 × ATR của TF (HEURISTIC) và không có BOS xen giữa. Zone gộp = hợp của hai zone; giữ các mức con (proximal của từng OB) làm mức tham chiếu nội bộ.

**R-H7 — Khi nào OB mất tư cách.** (a) Invalidation theo giá (§12F); (b) **hết vai trò**: leg sinh ra từ OB đã chạm DOL HTF và cấu trúc HTF đã đảo → OB không còn vai trò continuation (vẫn có thể là mức tham chiếu lịch sử); (c) bị supersede và giá đã rời xa > N × ATR_D1 (HEURISTIC).

### 8.4 Khi nào OB nhỏ bị OB lớn "override", và khi nào không

- **Bị override:** khi OB nhỏ nằm **ngược hướng** với zone lớn đang hoạt động, hoặc nằm **phía trên** zone lớn (bullish) ở vùng premium của range lớn — giá có xu hướng đi xuyên qua để tới zone lớn (OB nhỏ đóng vai trò inducement). [HYPOTHESIS — HYP-OB-005]
- **Không bị override:** khi OB nhỏ nằm **bên trong** zone lớn và hình thành như phản ứng hiện tại (R-H2) → nó là *bộ phận* của zone lớn, không phải đối thủ.
- **Trường hợp khó:** OB nhỏ nằm ngay **dưới** zone lớn (bullish), tức là giá đã xuyên qua distal của zone lớn. Đây là tín hiệu zone lớn có thể đang thất bại — xem Scenario D/E/F.

> [!warning] Bẫy "lớn hơn là tốt hơn"
> OB HTF có vẻ "giữ giá tốt hơn" một phần chỉ vì **chúng rộng hơn** (bao phủ nhiều giá hơn → dễ "trúng") và stop xa hơn (khó bị quét hơn). Khi so sánh các cấp, phải **chuẩn hóa theo độ rộng và theo R**. Tỷ lệ "giữ giá" không chuẩn hóa là thước đo sai.

---

## 9. Selecting OB When There Are Many — giải bài toán "quá nhiều OB"

### 9.1 Vì sao "quá nhiều OB" là tất yếu

Trong một uptrend H1 có 5 nhịp hồi, bạn sẽ có ít nhất 5 bullish OB trên H1 và có thể 15–25 OB trên M5 (con số minh họa). Đó không phải lỗi của thị trường — đó là **hệ quả tổ hợp của định nghĩa**: mỗi lần chuỗi giá nghỉ rồi đi tiếp, định nghĩa D0/D3 sinh ra một OB. Vì vậy câu hỏi "OB nào là thật?" là câu hỏi sai. Câu hỏi đúng:

> **"Với context hiện tại, những OB nào *đủ tư cách được xem xét*, OB nào tôi *kỳ vọng bị xuyên qua*, và tôi sẽ làm gì *trong từng trường hợp*?"**

### 9.2 Ba nguyên tắc chọn lọc

1. **Xếp hạng swing trước, OB sau** (nguyên lý thừa kế §8.1).
2. **Chọn lọc là lọc + lập kế hoạch có điều kiện**, không phải dự đoán. Khi còn 2 ứng viên, bạn không chọn một — bạn viết kế hoạch cho cả hai.
3. **Mỗi OB bị loại phải có lý do ghi được.** Nếu bạn không nói được vì sao loại OB₂, nhiều khả năng bạn đang chọn theo cảm giác (và sẽ chọn lại theo hindsight).

### 9.3 Decision Hierarchy — tám cổng lọc

```
TẤT CẢ OB ỨNG VIÊN (theo OB-DEF v0.1)
│
├─ G0 CONTEXT: D1 bias + hướng DOL cho phép phía nào?
│     └─ Chỉ giữ OB cùng phía. OB ngược phía → chỉ xét nếu có playbook countertrend riêng.
│
├─ G1 RANGE: dealing range H1 HIỆN TẠI (sau re-map gần nhất) là gì?
│     └─ Bullish: giữ OB nằm ở discount (pd_pos_h1 < 0.5). OB ở premium → danh sách "inducement/IRL".
│
├─ G2 STRUCTURE: OB thuộc cấp nào (L1–L4)?
│     └─ Giữ L3 (structural) + L2 (internal, nếu thỏa R-H4). L1 chỉ dùng refine ở M5.
│
├─ G3 CONSUMPTION: OB đã bị tiêu thụ chưa?
│     └─ Loại nếu đã có thân nến đóng qua distal trước đó. Gắn cờ nếu đã bị chạm (không loại — đây là biến cần test).
│
├─ G4 LIQUIDITY MAP: thanh khoản nằm ở đâu so với OB?
│     ├─ SSL chưa quét nằm GIỮA giá hiện tại và OB → giá nhiều khả năng lấy nó trước; OB phía trên SSL đó = inducement.
│     ├─ SSL chưa quét nằm NGAY DƯỚI distal (≤ 0.5 ATR_H1) → kỳ vọng sweep xuyên distal (Scenario D): KHÔNG đặt limit ở proximal.
│     └─ OB hình thành bởi một cú sweep có cấp ≥ L3 → cộng điểm chất lượng.
│
├─ G5 DOL PATH: phản ứng từ OB có đường tới DOL không?
│     └─ Loại nếu dist_to_dol_R < R tối thiểu của plan, hoặc có PD array HTF ngược hướng chắn giữa.
│
├─ G6 RANK: chấm OBQS v0.1 (§9.5) — chỉ để sắp thứ tự chú ý, KHÔNG để chọn.
│
└─ G7 CONDITIONAL PLAN: còn ≥ 2 ứng viên?
      ├─ Plan A (ứng viên nông hơn): chỉ vào khi có M5 sweep → MSS → displacement; target gần hơn; size theo grade.
      └─ Plan B (giá xuyên qua A): A chuyển thành inducement; chờ tại B với cùng quy trình M5.
```

### 9.4 Nghịch lý "OB gần nhất" và "OB sâu nhất"

- **OB gần nhất** nằm trên đường đi của giá nên **bị chạm nhiều nhất** → nhiều cơ hội nhất, nhưng cũng nhiều lần bị xuyên nhất. Nếu bạn chỉ đếm "số lần OB có phản ứng", OB gần nhất trông như tốt nhất — vì nó được hỏi nhiều nhất.
- **OB sâu nhất (structural)** hiếm khi được chạm → ít lệnh, vị trí tốt, invalidation rõ.
- **Đánh đổi tần suất ↔ chất lượng phải được đo**, không phải tranh luận. Chỉ số cần: `setups_per_week`, `E[R]`, và **E[R] × tần suất** (tổng R kỳ vọng mỗi tuần) — chỉ số cuối cùng quan trọng với mục tiêu prop firm vì thời gian có hạn.

### 9.5 OBQS v0.1 — Order Block Quality Score (giả thuyết nghiên cứu)

> [!warning] OBQS là giả thuyết, không phải edge
> Trọng số bằng nhau là lựa chọn **có chủ ý** để tránh overfitting khi chưa có dữ liệu. Chỉ sau khi có đủ mẫu (xem §20) mới kiểm tra: điểm càng cao thì kết quả có **tăng đơn điệu** không? Nếu không đơn điệu, OBQS vô dụng dù trông hợp lý đến đâu.

**Cổng cứng (fail = loại, không chấm điểm):** G0 context sai phía (khi không có playbook countertrend) · OB đã bị invalidate · `dist_to_dol_R` < R tối thiểu.

| Yếu tố | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|
| **Cấp cấu trúc** (`broken_swing_level`) | L1 | L2 (internal) | L3+ (external/protected) |
| **Displacement** (percentile `disp_net_atr`) | < P50 | P50–P80 | > P80 |
| **Liquidity** (`swept_level_class`) | Không sweep / sweep micro | Sweep L2 | Sweep ≥ L3 hoặc self-sweep mức L3 |
| **FVG** | Không có | Có, `fvg_size_atr` < 0.3 | Có, ≥ 0.3 (HEURISTIC) |
| **Vị trí** (`pd_pos_h1` với bullish) | ≥ 0.5 | 0.3–0.5 | < 0.3 |
| **HTF** | Không nằm trong HTF POI | Cùng hướng D1 bias | Cùng hướng + nằm trong D1/H4 PD array |
| **Freshness** | Đã bị xuyên > MT | Đã bị chạm nông | Chưa chạm |
| **Thanh khoản dưới distal** | SSL chưa quét sát distal (không có plan D) | — | Không có SSL chưa quét sát distal, **hoặc** có plan D rõ ràng |

Tổng 0–16. Phân nhóm để kiểm định: **A (≥ 12), B (8–11), C (< 8)**. Mục tiêu nghiên cứu không phải "chỉ trade A", mà là **xác minh A > B > C về E[R]** trên dữ liệu out-of-sample.

---

## 10. Relationship With Other ICT Concepts

### 10.1 Đồ thị nhân quả: OB đứng ở đâu?

Trước khi đi vào từng khái niệm, cần đặt OB đúng vị trí trong chuỗi nhân quả:

```
CONTEXT (bộ lọc, có trước)          SỰ KIỆN                    DẤU VẾT (hệ quả)
─────────────────────────           ─────────────               ──────────────────
Daily Bias ─┐                                                 ┌─► OB   (dấu vết tại GỐC)
DOL ────────┤                                                 ├─► FVG  (dấu vết trên ĐƯỜNG ĐI)
Dealing Range┼──► Liquidity bị lấy ──► DISPLACEMENT ──────────┼─► BOS/MSS (hệ quả CẤU TRÚC)
Premium/Disc┘      (sweep)                                    └─► Range mới được định nghĩa

KHI GIÁ QUAY LẠI:  OB/FVG (location) ──► LTF sweep + MSS + displacement (evidence) ──► Entry (trigger)
KHI OB THẤT BẠI:   acceptance xuyên distal ──► Breaker (vai trò đảo ngược)
```

> [!important] Hệ quả quan trọng nhất
> **OB là hệ quả, không phải nguyên nhân.** OB không "làm" giá đi lên; displacement mới là sự kiện, OB chỉ là dấu vết giá tại gốc của nó. Mọi lập luận kiểu "giá tăng vì có OB bên dưới" là đảo ngược nhân quả. Lập luận đúng: "giá đã tăng mạnh từ vùng này; nếu giá quay lại, đây là nơi đáng quan sát xem bên mua có xuất hiện lại không".

### 10.2 Bảng tổng hợp quan hệ

| Khái niệm | Quan hệ với OB | Vai trò | Tồn tại độc lập? | Kết hợp có cải thiện expectancy? |
|---|---|---|---|---|
| **Liquidity** (chung) | Cú lấy thanh khoản thường mở màn displacement sinh ra OB; thanh khoản quanh OB quyết định hành vi khi retest | Cause (lúc hình thành) + context (lúc retest) | Có | [BACKTEST REQUIRED] — HYP-OB-003 |
| **BSL** | Với bullish OB: BSL phía trên là target/DOL; với bearish OB: BSL bị quét tạo ra OB | Target / cause | Có | Target theo BSL vs fixed R: cần test |
| **SSL** | Với bullish OB: SSL bị quét trước OB (tốt); SSL **chưa quét dưới distal** (rủi ro) | Cause / rủi ro | Có | HYP-OB-011 (SSL dưới distal làm giảm E[R] của entry proximal) |
| **Internal liquidity** | Internal OB là một dạng IRL; stop của người mua internal OB = SSL nội bộ | OB là **một phần** của IRL | Có | — |
| **External liquidity** | Structural OB nằm tại cực trị range (ERL); sau khi ERL phía đối diện bị lấy, OB/FVG là draw hồi (IRL) | Context chu kỳ ERL → IRL → ERL | Có | HYP-OB-011 |
| **Market Structure** | Cấp của OB = cấp cấu trúc mà displacement phá (§8.1) | Định nghĩa **cấp** | Cấu trúc có trước OB | HYP-OB-005 |
| **Dealing Range** | OB structural là một đầu mút của range; vị trí OB trong range quyết định P/D | Context | Có | HYP-OB-008 |
| **Premium/Discount** | Bullish OB ở discount, bearish OB ở premium — **của range nào** phải khai báo | Filter | Có | HYP-OB-008 |
| **DOL** | OB = điểm xuất phát; DOL = điểm đến; OB chỉ có nghĩa nếu nằm trên đường tới DOL | Context/target | Có | HYP-OB-011 |
| **Daily Bias** | Bias chọn phía OB được phép; OB **không tạo** bias một mình | Filter | Có | HYP-OB-010 |
| **Displacement** | Điều kiện cần để một nến trở thành OB | **Định nghĩa** | Displacement tồn tại không cần OB (edge case 2); OB không tồn tại không cần displacement | HYP-OB-002 (độ mạnh có dự đoán không) |
| **MSS** | Structural OB (đảo chiều) là gốc của leg MSS; trong 2022 Model, gốc leg MSS M5 là vùng entry | Consequence (lúc hình thành) / evidence (lúc retest, ở LTF) | Có | HYP-OB-013 (entry OB vs FVG sau MSS) |
| **BOS** | OB continuation là gốc của leg BOS | Consequence | Có | HYP-OB-005 |
| **FVG** | OB = gốc; FVG = đường đi; FVG thường là POI nông hơn | Đồng hệ quả của displacement | Có, cả hai chiều | HYP-OB-004, HYP-OB-013 |
| **POI** | OB là **một loại** POI (cùng FVG, breaker, OTE…) | Tập con | POI không cần OB | — |
| **Inducement** | Internal OB nông có thể **là** inducement: lệnh mua + stop của người mua tại đó thành thanh khoản cho cú xuống sâu hơn | OB có thể đóng vai inducement | Có | HYP-OB-014 (OB nông nhất bị xuyên thường xuyên hơn OB structural) |
| **Liquidity Sweep** | (a) Sweep trước khi hình thành OB; (b) sweep distal của OB khi retest (Scenario D) | Cause / event khi retest | Có | HYP-OB-003, HYP-OB-015 |
| **Mitigation** | ICT: giá quay lại OB để smart money "mitigate" vị thế; phổ thông: "giá đã chạm OB". Mitigation Block = biến thể từ failure swing | Sự kiện retest / biến thể block | — | HYP-OB-006 |
| **Breaker** | OB bị phá có acceptance → đảo vai trò → Breaker | Consequence của **thất bại** | Breaker cần một OB đã fail | Xem [[04-Breaker-Block]] |

### 10.3 Những quan hệ cần phân tích sâu hơn

**Liquidity × OB — "thanh khoản bảo vệ OB" và "thanh khoản nằm dưới OB".**
Hai cấu hình có vẻ giống nhau nhưng hàm ý ngược nhau:
- *OB được sinh ra bởi sweep* (SSL đã bị lấy tại gốc): thanh khoản bên dưới đã được "dọn". Khi giá retest, **không còn nam châm hiển nhiên ngay dưới distal** → OB có cơ hội giữ tốt hơn. [INTERPRETATION]
- *OB nằm ngay trên SSL chưa bị lấy* (ví dụ equal lows H1 cách distal 0.3 ATR): SSL đó là một nam châm. Theo logic DOL của chính ICT ([[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]), giá có xu hướng đi lấy thanh khoản đó — nghĩa là **xuyên qua OB**. Đây là cấu hình sinh ra Scenario D. Rule thực hành: **không đặt limit ở proximal của OB có SSL chưa quét ngay dưới distal**; chờ sweep + reclaim. [INTERPRETATION → HYP-OB-011]

**Market Structure / BOS / MSS × OB.**
- OB continuation (gốc leg BOS) và OB reversal (gốc leg MSS) có cơ chế khác nhau: OB continuation được "chống lưng" bởi trend đang có; OB reversal là nơi trend **mới** bắt đầu — vì vậy rủi ro "MSS giả" cao hơn.
- MSS trên LTF khi retest OB HTF **không phải cùng loại sự kiện** với MSS tạo ra OB. Cái trước là *evidence* của phản ứng; cái sau là *consequence* đã tạo ra OB.

**Dealing Range / Premium-Discount × OB — vấn đề "range nào?".**
Một bullish OB H1 có thể nằm ở discount của range H1 nhưng ở premium của range D1. Quy tắc giải quyết (đề xuất): **range dùng để đánh giá P/D là range của timeframe mà DOL/target được lấy ra**. Nếu target là BSL D1 → dùng range D1 làm context, range H1 làm setup. OB ở discount H1 nhưng premium D1 được xếp hạng thấp hơn OB ở discount của cả hai. [INTERPRETATION → HYP-OB-008]

**DOL × OB.**
OB và DOL là cặp "điểm xuất phát — điểm đến". Một OB đẹp không có ý nghĩa nếu:
- DOL đã bị chạm (leg đã hoàn thành nhiệm vụ);
- giữa OB và DOL có một PD array HTF ngược hướng (lực cản);
- khoảng cách OB → DOL < R tối thiểu khi stop ở distal.
Ngược lại, **OB ngược hướng DOL** là OB countertrend: có thể phản ứng (vì các cơ chế M2–M4 không quan tâm DOL), nhưng phản ứng thường chỉ là nhịp hồi — target phải ngắn. [HYPOTHESIS]

**Displacement / FVG × OB — hai dấu vết của cùng một sự kiện.**
OB và FVG cùng là dấu vết của một displacement. Lựa chọn entry giữa chúng là **đánh đổi**:

| | Entry tại FVG | Entry tại OB |
|---|---|---|
| Vị trí | Nông hơn (gần giá hơn) | Sâu hơn |
| Xác suất được khớp | Cao hơn | Thấp hơn (nhiều lệnh bỏ lỡ khi giá bật từ FVG) |
| R:R nếu stop ở cùng điểm | Thấp hơn | Cao hơn |
| Rủi ro | Giá lấp trọn FVG và đi tiếp xuống OB → stop nếu stop sát FVG | Bỏ lỡ lệnh (opportunity cost) |

Đánh đổi này không có đáp án lý thuyết — nó là câu hỏi thực nghiệm (**HYP-OB-013**), và vault đã có sẵn cột `entry_type` (CE/Edge) và `rr_if_ce` trong template backtest để bắt đầu đo.

**Inducement × OB.**
Inducement (xem [[15-Inducement]]) là thanh khoản "mồi" nằm trước POI thật. Internal OB nông là ứng viên inducement tự nhiên: nhiều người đặt lệnh mua ở đó, stop của họ nằm ngay dưới → tạo SSL nội bộ. Khi giá đi xuống lấy SSL này, nó cung cấp đối ứng cho cú đi xuống POI sâu hơn, hoặc cho chính phản ứng tại structural OB. Đây là cơ chế đứng sau quan sát "OB nông nhất thường là inducement" ở [[25-OB-Order-Block]] §14.1 — nhưng quan sát đó vẫn là **[HYPOTHESIS]** (HYP-OB-014) cho đến khi được đo.

**Mitigation × Breaker × Reclaim — ba kết cục khác nhau của một OB bị "chạm sâu".**

| Kết cục | Điều quan sát được | Diễn giải | Hành động |
|---|---|---|---|
| **Mitigation giữ** | Giá vào OB, không có thân đóng ngoài distal, phản ứng theo hướng OB | OB giữ vai trò | Theo plan OB (cần M5 evidence) |
| **Reclaim (deviation)** | Giá đóng ngoài distal ngắn hạn (1–2 nến TF OB), rồi displacement lấy lại vào trong/trên OB | Cú xuyên là sweep; OB vẫn (hoặc càng) có hiệu lực | Chờ MSS LTF theo hướng OB sau reclaim |
| **Breaker** | Giá đóng ngoài distal, **tạo cấu trúc ngoài** (ví dụ lower high LTF dưới distal), rồi retest OB từ phía ngược và bị từ chối | OB đã fail; vai trò đảo ngược | Xử lý như [[04-Breaker-Block]] — hướng ngược |

---

## 11. D1 → H1 → M5 Framework

![[OB-DeepResearch-D1H1M5.svg|760]]
*Hình 3 — OB ở mỗi timeframe trả lời một câu hỏi khác nhau. D1 OB: "vùng nào đáng chờ?" (location/context). H1 OB: "POI cụ thể nào?" (setup). M5: "phản ứng có đang xảy ra không, vào ở đâu, sai ở đâu?" (evidence + trigger).*

### 11.1 D1 — Context

**D1 OB dùng để làm gì?** Để trả lời "nếu giá hồi, vùng nào là nơi *hợp lý* để D1 narrative tiếp tục?" Nó thu hẹp không gian tìm kiếm của H1/M5 từ "bất cứ đâu" xuống "một vài vùng".

**Có nên dùng D1 OB làm directional bias không?** **Không trực tiếp.** Lý do:
- "Giá đang ở bullish OB nên bias bullish" là lập luận **vòng tròn nửa vời**: giá *đến được* OB chính là nhờ một cú giảm, và phía trên thường cũng có bearish PD array. OB chỉ cho biết *nơi* bias có thể được thể hiện, không cho biết bias.
- Bias đến từ: cấu trúc D1 (protected low còn nguyên?), DOL (thanh khoản D1 nào là đích?), vị trí trong range D1, và hành vi của nến D1 gần đây ([[59-Daily-Bias]]).
- D1 OB **đóng góp vào** bias khi đồng thời: cấu trúc D1 bullish còn nguyên + giá ở discount D1 + D1 OB được chạm và nến D1 đóng cửa từ chối (không đóng dưới distal) + DOL phía trên rõ ràng. Khi đó bias là một **giả thuyết có invalidation**: nến D1 đóng dưới distal/protected low.

**D1 OB và Dealing Range.** Structural D1 OB nằm tại đáy của range D1 (bullish) → ở discount sâu. D1 OB nằm ở premium của range D1 là internal D1 OB → ưu tiên thấp cho long.

**D1 OB và External Liquidity.** Câu hỏi then chốt ở D1: **"OB này được thanh khoản bảo vệ, hay có thanh khoản nằm dưới nó?"** Nếu một SSL D1 hiển nhiên (đáy tuần/tháng trước) nằm ngay dưới D1 OB, kịch bản có xác suất đáng kể là giá xuyên qua OB lấy ERL đó rồi mới phản ứng (Scenario D ở cấp D1) — và một lệnh M5 đặt ở proximal D1 OB sẽ bị cuốn đi.

**D1 OB và DOL.** Cặp (D1 OB, D1 DOL) định nghĩa "hành lang giao dịch D1": OB là nơi nhịp hồi có thể kết thúc, DOL là nơi leg tiếp theo đi tới. Khoảng cách giữa hai điểm (theo ATR D1) là tiềm năng R của cả narrative.

**Khi nào D1 OB là context, khi nào KHÔNG được dùng để trigger entry?** Luôn là context; **không bao giờ** là trigger:
- Độ rộng D1 OB thường tương đương một phần lớn ATR D1 → stop theo distal D1 quá xa so với cách vào lệnh M5.
- Nến D1 chỉ "xác nhận" khi đóng cửa → dùng hành vi D1 trong ngày để vào lệnh là dùng thông tin chưa hoàn tất.
- D1 OB là vùng thời gian nhiều ngày; phản ứng có thể bắt đầu ở bất kỳ phiên nào.

### 11.2 H1 — Setup

**H1 OB xác định POI như thế nào?** Bên trong zone D1, áp dụng tám cổng §9.3 cho các H1 OB. Kết quả thường là 1–2 H1 POI.

**Hai kiểu setup H1 hợp lệ:**
1. **Kiểu "HTF POI → H1 MSS → H1 OB mới":** giá vào zone D1 → H1 sweep một mức thanh khoản H1 → H1 MSS theo hướng D1 → **OB mới tại gốc leg MSS H1** trở thành POI để retest. Đây là cách áp dụng R-H2 ở cấp H1: OB H1 mang thông tin vì nó *sinh ra từ phản ứng* tại zone D1.
2. **Kiểu "H1 OB có sẵn trong zone D1":** một H1 structural OB đã tồn tại bên trong zone D1 và giá đang tiến về đó. Kiểu này cần M5 evidence chặt hơn, vì OB được hình thành *trước* khi có phản ứng hiện tại.

**H1 structure ảnh hưởng đến lựa chọn OB ra sao?** Khi D1 bullish nhưng H1 đang giảm (đang hồi), các bullish OB H1 cũ nằm **ngược cấu trúc H1** — chúng là nơi H1 *có thể* đảo chiều, không phải nơi H1 *đã* đảo chiều. Điều bạn chờ là H1 MSS bullish bên trong zone D1. Trước MSS đó, mọi bullish H1 OB chỉ là ứng viên.

**Kết hợp H1 OB với liquidity engineering.** Cấu hình lý tưởng (ICT framework): phía trên H1 OB có equal lows hoặc trendline liquidity dẫn giá xuống → giá quét chúng trong lúc tiến vào OB → thanh khoản được lấy **ngay tại/trên** OB, không phải dưới distal. Cấu hình xấu: equal lows nằm **dưới** distal H1 OB (xem 10.3).

**Có nhiều H1 OB thì chọn cái nào?** Không chọn bằng mắt: G0–G7. Nếu còn hai → Plan A/B.

### 11.3 M5 — Execution

**M5 OB có phải entry signal không?** **Không.** M5 OB là vùng tinh chỉnh bên trong một H1 POI *sau khi* có bằng chứng. Một M5 OB đứng một mình (không trong H1 POI, không sau MSS) là micro OB — nhiễu.

**Trình tự thực thi trong 2022 Model (bullish):**

| Bước | Câu hỏi | Vai trò |
|---|---|---|
| 1 | Giá đã vào H1 POI (OB/FVG) trong zone D1 chưa? | **Location** — điều kiện tiên quyết |
| 2 | Có M5 sweep một mức thanh khoản cục bộ (low phiên, equal lows M5) bên trong/sát POI không? | Manipulation — tăng chất lượng (HYP-OB-003 ở cấp M5) |
| 3 | Có M5 MSS theo hướng bullish, đóng cửa vượt swing high M5 có ý nghĩa không? | **Evidence** — bắt buộc |
| 4 | MSS có displacement không (đo theo [[50-Displacement-In-Depth]])? | **Evidence** — chất lượng |
| 5 | Leg MSS để lại FVG và/hoặc M5 OB ở gốc? | Tạo **vùng entry** |
| 6 | Entry: limit tại FVG (mặc định 2022 Model) hoặc tại M5 OB/MT (phương án sâu hơn) | **Trigger/execution rule** |
| 7 | Stop: dưới sweep low M5 (hoặc dưới distal M5 OB); stop dự phòng = distal H1 OB | **Invalidation** |
| 8 | Target: IRL gần (chốt một phần) → DOL H1/D1 | **Target** |

**Có nên chờ liquidity sweep?** Trong framework của bạn: ưu tiên **có** (đây là thành phần manipulation). Nhưng đừng biến nó thành điều kiện định nghĩa — ghi `ltf_sweep` như biến để đo xem setup không có sweep có thật sự kém hơn không.

**MSS? Displacement? FVG?** MSS = bắt buộc (không có MSS thì chưa có bằng chứng phản ứng). Displacement = bắt buộc về chất lượng (MSS yếu là lỗi đã ghi nhận của bạn, xem [[08-Mistake-Weak-Displacement]]). FVG = vùng entry mặc định; nếu không có FVG, M5 OB là phương án thay thế (xem ví dụ S3 ở §16).

**OB retest vs FVG retest?** Xem bảng đánh đổi ở 10.3. Quyết định nên dựa trên dữ liệu `entry_type` của chính bạn.

### 11.4 Phân biệt ba khái niệm — bảng chốt

| Khái niệm | Trả lời câu hỏi | Ví dụ | Sai lầm nếu gộp |
|---|---|---|---|
| **OB = location** | "Nên quan sát ở đâu?" | H1 structural OB trong discount D1 | "Chạm OB là mua" — vào lệnh không có bằng chứng |
| **MSS/displacement = evidence** | "Phản ứng có đang thật sự xảy ra không?" | M5 MSS với displacement ≥ P80 bên trong H1 OB | "Thấy MSS là vào" — MSS ở giữa range, không trong POI ([[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]) |
| **Entry trigger = execution rule** | "Bóp cò chính xác ở đâu, khi nào, stop ở đâu?" | Limit tại M5 FVG, stop dưới sweep low, target PDH | "Có setup là được" — không định nghĩa entry/stop trước nên không backtest được |

---

## 12. Price Returning to OB — phân tích Scenarios A–F

![[OB-DeepResearch-Scenarios-AF.svg|760]]
*Hình 4 — Sáu kịch bản giá quay về một Bullish OB. A: near miss; B: chạm proximal; C: tới MT/CE; D: râu quét distal, đóng lại bên trong; E: đóng ngoài 1–3 nến rồi quay lại; F: đóng và duy trì bên ngoài.*

> [!note] Hai nguyên tắc trước khi đi vào từng kịch bản
> 1. **OB invalidation ≠ trade invalidation.** Một lệnh có thể bị stop trong khi OB vẫn còn hiệu lực (Scenario D với stop quá sát); một OB có thể bị invalidate khi bạn không có lệnh nào. Hai quy tắc này phải được viết riêng.
> 2. **Đếm nến phải theo timeframe của OB.** "1–3 nến" đóng ngoài một H1 OB là 1–3 giờ; 1–3 nến M5 đóng ngoài một H1 OB chỉ là 5–15 phút nhiễu. Mọi rule đếm nến phải ghi rõ TF, hoặc tốt hơn: quy đổi sang **thời gian** và **khoảng cách ATR**.

Quy ước tọa độ trong zone (dùng cho cả phần định lượng): **0 = proximal, 1 = distal, >1 = bên ngoài distal**. `penetration = (proximal − giá thấp nhất khi retest) / (proximal − distal)` với bullish OB.

### Scenario A — Giá tiến gần OB nhưng chưa chạm, rồi đảo chiều (near miss)

**OB có thực sự cần được chạm không?** Không. Có bốn giải thích cạnh tranh:
1. **Front-running:** khi nhiều người cùng biết một vùng, người sốt ruột đặt lệnh mua *phía trên* vùng để được khớp trước. Nếu đủ nhiều người làm vậy, phản ứng dịch lên trên OB. Đây là hệ quả logic của việc một mức giá trở thành "điểm hội tụ chú ý" (M4). [INTERPRETATION]
2. **Một POI nông hơn làm nhiệm vụ:** FVG phía trên OB (xem 7.4) — phản ứng tại FVG không phải "near miss của OB", mà là "OB không được hỏi đến".
3. **Artifact dữ liệu:** trên feed khác, TF khác, OB có thể đã được chạm.
4. **Không liên quan tới OB (M6):** nhịp hồi kết thúc ở một mức ngẫu nhiên gần OB.

**Nói gì về độ chính xác của zone?** Biên OB có độ chính xác cỡ *spread + một phần nhỏ ATR*, không phải từng pip. Đòi hỏi chính xác hơn mức đó là overprecision.

**Hàm ý thực thi:** limit order tại proximal sẽ **bỏ lỡ** các near miss — đây là chi phí thật (opportunity cost) phải được đo. Nếu phản ứng từ vùng "gần OB" có M5 evidence đầy đủ (sweep → MSS → displacement), setup vẫn có thể được vào qua FVG của cú phản ứng — điều kiện location là "nằm trong **vùng ảnh hưởng** của POI" = từ proximal + 0.25 × ATR_H1 trở xuống (HEURISTIC).

**Backtest near miss:**
- Định nghĩa "approach event": giá tiến vào trong k × ATR_TF của proximal (k ∈ {0.1, 0.25, 0.5}) sau khi đã cách ≥ 1 ATR.
- So sánh phân bố phản ứng (MFE theo ATR trong N nến) giữa: chạm thật / near miss / vùng đối chứng cùng khoảng cách.
- Đo `missed_trade_rate` = tỷ lệ setup đạt chuẩn mà limit ở proximal không khớp, và R bị bỏ lỡ.

### Scenario B — Giá chạm một cạnh OB và phản ứng

**Proximal edge:** chạm mép gần nhất rồi bật = penetration ≈ 0. Đây là kịch bản "OB mạnh" trong narrative — nhưng về mặt quan sát, nó không phân biệt được với "phản ứng tại FVG/level sát trên OB".

**Distal edge:** đi tới gần mép xa (penetration ≈ 0.9–1.0) rồi mới bật. Theo [[51-OB-Mitigation-Depth-Vi-sao-Shallow-CE-hay-Full-khac-nhau]], độ sâu chịu ảnh hưởng của: nested FVG/OB phía trên CE (kéo nông), SSL sát distal (kéo sâu), vị trí P/D, khoảng cách tới draw. Đây là các biến đo được, không phải "độ mạnh của OB".

**Zone penetration** là biến liên tục — ghi lại, đừng nhị phân hóa thành "chạm/không chạm".

**Reaction strength** — đo bằng:
- `mfe_atr_N` = MFE theo ATR trong N nến TF sau điểm thấp nhất (N = 12, HEURISTIC),
- `bars_to_1atr` = số nến để giá đi được +1 ATR từ điểm thấp nhất,
- `mfe_mae_ratio` trong N nến.

**Rule ứng viên:** entry proximal = entry *aggressive* — chỉ khi OBQS cao **và** không có SSL chưa quét dưới distal (G4). [HYPOTHESIS — HYP-OB-007 so sánh các mức entry]

### Scenario C — Giá đi tới CE/MT 50% rồi phản ứng

**Vì sao 50% được dùng?**
1. **Thỏa hiệp khớp lệnh ↔ R:R:** nông hơn distal (dễ khớp hơn), sâu hơn proximal (R:R tốt hơn).
2. **Lý do thống kê thuần túy:** nếu bạn tin mức phản ứng "thật" nằm đâu đó trong zone với độ bất định đều, **điểm giữa là điểm tối thiểu hóa sai số tuyệt đối kỳ vọng**. Đây là lý do của *người đo*, không phải cơ chế của *thị trường*.
3. **ICT teaching:** MT là "vạch ranh giới" — thân nến đóng qua MT là dấu hiệu sớm OB yếu.
4. **Một giả thuyết cơ chế thú vị (M3):** nếu phản ứng đến từ trader bị kẹt thoát hòa vốn, mức phản ứng nên nằm quanh **giá vào trung bình** của họ — xấp xỉ **VWAP của nến OB**, thường gần giữa thân. Nghĩa là MT *có thể* là một proxy thô của VWAP nến OB. Kiểm chứng được trên NQ futures (có volume): so sánh điểm quay đầu khi retest với MT và với VWAP nến OB. [HYPOTHESIS]

**CE có cơ sở predictive không?** Hiện **không có bằng chứng** nào cho thấy mức 50% có tính chất đặc biệt so với 40% hay 60%. Không cơ chế nào trong M1–M6 dự đoán *riêng* mức 50% (trừ giả thuyết VWAP ở trên, vốn dự đoán một mức *thay đổi theo từng nến*, không cố định 50%).

**Rule hay heuristic?** **Heuristic.** Dùng MT/CE làm mức entry mặc định là chấp nhận được vì lý do (1) và (2), miễn là bạn không tin rằng nó "đặc biệt".

**Kiểm chứng:**
- Vẽ phân bố điểm quay đầu khi retest theo tọa độ zone (0 → 1). Nếu 50% đặc biệt, phải thấy **mật độ tập trung quanh 0.5** vượt mức kỳ vọng từ một phân bố trơn — và vượt so với vùng đối chứng.
- So sánh E[R] của các entry {proximal, 0.25, MT, CE, open, distal+buffer} với **cùng quy tắc stop và target** (entry khác nhau thay đổi cả win rate lẫn R — chỉ E[R] và tổng R mới so sánh công bằng).
- Kiểm tra rule ICT: `P(OB giữ | thân đóng qua MT)` vs `P(OB giữ | không đóng qua MT)`.

### Scenario D — Giá quét qua distal bằng râu nhưng đóng nến trở lại bên trong OB

**Ba diễn giải cạnh tranh:**
1. **Sweep & absorb:** stop dưới distal bị kích hoạt (M5), lượng bán ép này bị hấp thụ bởi người mua → reclaim. Narrative ICT: OB "tự bảo vệ" bằng cách lấy thanh khoản bên dưới — thường được coi là phản ứng mạnh.
2. **OB là inducement cho chính cú sweep của nó:** lệnh mua tại OB + stop dưới distal tạo ra pool; cú quét là sự kiện chính, OB chỉ là mồi.
3. **Dấu hiệu thất bại sớm:** nến tiếp theo tiếp tục xuống và đóng ngoài (chuyển sang E/F).

**Invalidation hay vẫn valid?** Rule v0.1: **trên TF của OB, râu xuyên distal nhưng thân đóng lại trong zone → OB vẫn valid**, gắn cờ `distal_swept = true`. Wick penetration **không phải** invalidation tự động.

**Nghịch lý đặt stop:** nếu stop đặt ngay dưới distal, bạn bị stop bởi *chính sự kiện* mà sau đó được coi là xác nhận. Ba cách xử lý:
- **Entry xác nhận:** chờ reclaim (đóng lại trong zone) + M5 MSS, stop dưới sweep low → khớp muộn hơn nhưng stop "đúng chỗ".
- **Stop có đệm:** distal − k × ATR_TF, k ∈ {0.1, 0.25, 0.5} (HEURISTIC, cần test) → stop xa hơn, size nhỏ hơn.
- **Plan D có chủ đích:** khi G4 phát hiện SSL chưa quét ngay dưới distal → không đặt limit proximal; chỉ đợi kịch bản D.

**Backtest:** biến `sweep_depth_atr`, `reclaim_bars`, vị trí close của nến quét trong zone; **HYP-OB-015**: "sweep nông (≤ 0.5 ATR) + reclaim trong 1 nến TF OB cho E[R] cao hơn retest không sweep".

### Scenario E — Giá đóng dưới OB 1–3 nến rồi quay trở lại OB

**Ba khả năng — cần phân biệt, không đoán:**

| Khả năng | Dấu hiệu khi giá quay lại | Hành động |
|---|---|---|
| **Failed breakdown → Reclaim** | Displacement đưa giá đóng trở lại **trên MT/proximal**; LTF MSS bullish | OB (reclaimed) còn hiệu lực — chờ M5 evidence rồi mới vào |
| **Breaker đang hình thành** | Giá quay lên chạm distal/phần dưới OB **từ bên dưới** và bị từ chối; LTF lower high dưới distal | OB đã fail → xem [[04-Breaker-Block]] (hướng ngược) |
| **Không quyết định** | Lình xình quanh distal, nến chồng lấp | Không giao dịch |

**Kiểm tra cấu trúc bắt buộc:** cú đóng dưới distal có **phá protected swing** không? Nếu OB là L3 và thân nến đã đóng dưới protected low → cấu trúc TF đã đổi. Khi đó "quay lại OB" không đủ; cần **MSS bullish mới** để khôi phục narrative bullish.

**Vì sao thời gian ở ngoài quan trọng:** càng ở ngoài lâu, càng nhiều người tham gia thích nghi (đặt stop mới, vào lệnh theo hướng phá) → acceptance hình thành. Đó là trực giác đằng sau "đếm nến" — nhưng trực giác này cần được lượng hóa, không phải cố định.

**Rule ứng viên (OB-INVAL v0.1, trạng thái trung gian):** sau thân đóng đầu tiên ngoài distal, OB chuyển sang **"suspended"**. Được **khôi phục** nếu trong M nến TF OB (M = 3, HEURISTIC) có thân đóng trở lại trên MT kèm displacement. Nếu không → **invalid** và chuyển sang theo dõi breaker.

### Scenario F — Giá đóng và duy trì bên ngoài OB > 3 nến, không reclaim

**Khi nào OB nên được coi là invalid?** Khi giá **chấp nhận** (accept) vùng giá bên ngoài. "Acceptance" cần định nghĩa bằng sự kiện đo được, không phải cảm giác.

**"3 nến" có phải rule hợp lệ?** Nó là một **ngưỡng tùy ý** — có thể tốt, có thể tệ, và gần như chắc chắn không cùng giá trị tối ưu cho D1, H1, M5, cho EURUSD và NQ. Nó chỉ trở thành rule khi được chọn bằng dữ liệu.

**Cách xây dựng invalidation khách quan — OB-INVAL v0.1 (đề xuất):** OB invalid khi **bất kỳ** điều kiện nào xảy ra:
1. **Structural:** OB là L3 và thân nến TF đóng qua protected swing gắn với nó → invalid ngay.
2. **Time-in-acceptance:** N thân nến TF liên tiếp đóng ngoài distal mà không reclaim (N = 2, HEURISTIC; test N ∈ {1, 2, 3, 5}).
3. **Distance:** một thân nến đóng ngoài distal ≥ 0.5 × ATR_TF (HEURISTIC).
4. **Structure-outside:** giá tạo cấu trúc bên ngoài — ví dụ một lower high LTF hình thành dưới distal rồi bị phá xuống.
5. **Breaker confirmation:** giá quay lại distal từ phía ngoài và bị từ chối.

**Chọn N bằng dữ liệu — phân tích hazard:**
- Với mọi lần thân nến đầu tiên đóng ngoài distal, tính `P(reclaim trong M nến | đã có n nến liên tiếp đóng ngoài)` với n = 1…6.
- Vẽ đường cong: xác suất reclaim giảm dần theo n. Chọn n tại điểm xác suất reclaim rơi dưới ngưỡng p* — p* được chọn theo **chi phí** của hai loại sai: invalidate nhầm (bỏ lỡ reclaim) vs giữ một OB đã chết (vào lệnh vào vùng không còn giá trị).
- Chọn trên in-sample → kiểm tra trên out-of-sample → kiểm tra độ ổn định giữa instrument/TF. Nếu n tối ưu nhảy lung tung giữa các tập dữ liệu, rule đếm nến **không có cấu trúc thật** — dùng điều kiện structural/distance thay thế.

**Bảng tổng kết A–F:**

| Kịch bản | Tọa độ zone | OB status | Hàm ý thực thi | Nhãn |
|---|---|---|---|---|
| A — Near miss | < 0 | Valid | Limit proximal bỏ lỡ; có thể vào qua FVG phản ứng nếu có M5 evidence | [INTERPRETATION] + đo `missed_trade_rate` |
| B — Chạm proximal | ≈ 0 | Valid | Entry aggressive chỉ khi OBQS cao, không có SSL dưới distal | HYP-OB-007 |
| C — Tới MT/CE | ≈ 0.5 | Valid (ICT: cảnh báo nếu thân đóng qua MT) | Mức entry mặc định vì lý do thỏa hiệp, không vì "đặc biệt" | HEURISTIC; HYP-OB-007 |
| D — Râu quét distal, đóng trong | > 1 (râu), ≤ 1 (thân) | Valid, cờ `distal_swept` | Entry xác nhận sau reclaim; stop dưới sweep low | HYP-OB-015 |
| E — Đóng ngoài 1–3 nến rồi quay lại | > 1 tạm thời | Suspended → reclaim hoặc invalid | Phân biệt reclaim vs breaker bằng hành vi khi quay lại | OB-INVAL v0.1 |
| F — Duy trì ngoài | > 1 kéo dài | Invalid | Chuyển sang theo dõi breaker; xóa khỏi POI list | OB-INVAL v0.1 [BACKTEST REQUIRED] |

---

## 13. Edge Cases — phân tích từng trường hợp

Mỗi edge case theo cấu trúc: **Classification → Interpretation → Trading implication → Invalidation → Backtest implication**.

**EC-01 — OB không tạo FVG**
- *Classification:* Valid OB (Tầng 2) nếu có displacement + BOS; thiếu một đặc trưng chất lượng.
- *Interpretation:* displacement có râu chồng lấp — đủ mạnh để phá cấu trúc nhưng không đủ nhanh ở TF này; có thể FVG tồn tại ở LTF.
- *Trading implication:* không có POI nông phía trên → OB là vùng entry chính; kiểm tra FVG ở LTF; hạ grade.
- *Invalidation:* như OB thường.
- *Backtest:* `fvg_present = false` vs `true` (HYP-OB-004); thêm cột `fvg_present_ltf`.

**EC-02 — FVG không có OB rõ ràng**
- *Classification:* "Displacement origin không có OB" — displacement bắt đầu từ doji/inside bar, hoặc từ một gap.
- *Interpretation:* gốc mất cân bằng vẫn tồn tại, chỉ là không có nến ngược hướng để gán nhãn — minh chứng rằng **OB là nhãn của hình dạng nến, còn sự kiện thật là displacement**.
- *Trading implication:* dùng FVG làm POI; mức gốc = swing low.
- *Invalidation:* swing low gốc bị phá có acceptance.
- *Backtest:* rất có giá trị: so sánh "gốc có OB" vs "gốc không có OB" với displacement tương đương → trả lời trực tiếp **OB có thêm thông tin gì ngoài displacement + FVG không**.

**EC-03 — OB tạo displacement nhưng không phá structure**
- *Classification:* Candidate (Tầng 1), **không** phải Valid OB.
- *Interpretation:* cú đẩy mạnh bên trong range; có thể chỉ là chạy tới biên range mà không phá.
- *Trading implication:* không phải POI tự thân.
- *Invalidation:* không áp dụng.
- *Backtest:* **giữ lại làm nhóm đối chứng tự nhiên** — so sánh với OB có BOS để kiểm tra điều kiện BOS có tạo giá trị không.

**EC-04 — OB phá structure nhưng displacement yếu**
- *Classification:* Valid về cấu trúc, chất lượng thấp.
- *Interpretation:* cú phá kiểu "trôi" — có thể là liquidity run (quét stop trên đỉnh) hơn là mất cân bằng thật; nguy cơ MSS giả.
- *Trading implication:* không dùng làm POI đảo chiều; nếu dùng cho continuation cần HTF alignment rất rõ.
- *Invalidation:* như OB thường; thêm cảnh báo nếu giá quay lại dưới swing vừa phá (reclaim ngược).
- *Backtest:* nhóm `disp_percentile < P50` — kiểm tra HYP-OB-002.

**EC-05 — Nhiều OB liên tiếp trong một leg**
- *Classification:* chuỗi OB; một structural, còn lại internal/micro.
- *Interpretation:* sản phẩm tổ hợp của trend (§9.1).
- *Trading implication:* R-H3 (supersession) + R-H6 (gộp) + G0–G7.
- *Invalidation:* mỗi OB riêng; khi OB structural fail thì toàn bộ chuỗi phía trên mất context.
- *Backtest:* cột `ob_order_in_leg` (1 = gần giá nhất) → kiểm tra HYP-OB-014 ("OB nông nhất bị xuyên thường xuyên hơn").

**EC-06 — Nested OB**
- *Classification:* OB LTF bên trong OB HTF.
- *Interpretation:* có ý nghĩa nếu hình thành *sau* khi giá vào zone HTF và là gốc MSS LTF (R-H2).
- *Trading implication:* dùng OB LTF để refine entry và stop.
- *Invalidation:* OB LTF invalid → chưa chắc OB HTF invalid; OB HTF invalid → OB LTF mất context.
- *Backtest:* cột `nested_formed_after_htf_entry` → so sánh nested "phản ứng" vs nested "có sẵn".

**EC-07 — OB overlap**
- *Classification:* (a) cùng hướng chồng nhau → gộp (R-H6); (b) **ngược hướng chồng nhau** (bullish OB nằm trong bearish OB) → "contested zone".
- *Interpretation:* vùng giá mà cả hai phía từng thắng — thông tin mâu thuẫn.
- *Trading implication:* HTF quyết định (R-H1); yêu cầu M5 evidence chặt hơn; giảm size.
- *Invalidation:* theo OB cùng hướng HTF.
- *Backtest:* cờ `opposite_overlap`.

**EC-08 — OB bị partial mitigation**
- *Classification:* vẫn valid (trừ khi thân đóng qua MT theo rule ICT).
- *Interpretation:* theo M1/M3: một phần nhu cầu đã được tiêu thụ; theo M4: vùng đã được "xác nhận" bởi thị trường.
- *Trading implication:* một số trader thu hẹp zone về phần chưa bị mitigate — đây là một biến thể cần test, không phải quy tắc.
- *Invalidation:* như thường.
- *Backtest:* `prior_penetration_max_pct` làm biến giải thích cho lần retest sau.

**EC-09 — OB bị mitigated nhiều lần (bị xuyên sâu nhiều lần)**
- *Classification:* "worn OB".
- *Interpretation:* ICT: yếu dần. Bằng chứng S/R lân cận [^S4][^S5]: mức có nhiều lần bật có thể **mạnh hơn**. Thêm M5: mỗi lần giữ, stop lại dồn thêm dưới distal → khi vỡ thì vỡ mạnh.
- *Trading implication:* không giả định chiều nào; size nhỏ; chuẩn bị cho kịch bản phá mạnh.
- *Invalidation:* như thường; nhưng cú phá sau nhiều lần giữ thường là cascade → không "bắt dao" ở dưới.
- *Backtest:* HYP-OB-006 với `mitigation_count` (xuyên qua MT) tách khỏi `touch_count` (EC-19).

**EC-10 — OB bị sweep rồi reclaim**
- *Classification:* Reclaimed OB (Scenario D/E).
- *Interpretation:* cú xuyên là sweep; thanh khoản dưới OB đã được lấy.
- *Trading implication:* ứng viên mạnh **nếu** reclaim có displacement; entry sau reclaim + MSS M5.
- *Invalidation:* thân nến đóng dưới sweep low.
- *Backtest:* HYP-OB-015.

**EC-11 — OB nằm ngay giữa dealing range (quanh EQ)**
- *Classification:* vị trí mơ hồ (`pd_pos` ≈ 0.45–0.55).
- *Interpretation:* premium/discount là biến liên tục; ngưỡng 0.5 là quy ước.
- *Trading implication:* bỏ qua, trừ khi nằm trong HTF POI hoặc là structural OB của một range nhỏ hơn đúng hướng.
- *Invalidation:* như thường.
- *Backtest:* dùng `pd_pos` liên tục, kiểm tra quan hệ đơn điệu với kết quả (HYP-OB-008) thay vì chỉ so "trên/dưới 0.5".

**EC-12 — Bullish OB nằm ở premium**
- *Classification:* thường là internal/continuation OB.
- *Interpretation:* trong trend mạnh, OB continuation *luôn* nằm ở premium của range **cũ** — vì range chưa được re-map.
- *Trading implication:* re-map range sau BOS ([[37-Re-mapping-Dealing-Range-sau-Displacement]]); OB có thể là discount của range **mới**. Nếu vẫn ở premium sau re-map → ưu tiên thấp.
- *Invalidation:* như thường.
- *Backtest:* ghi `pd_pos` theo cả range cũ và range re-map → kiểm tra range nào dự đoán tốt hơn.

**EC-13 — Bearish OB nằm ở discount**
- *Classification:* đối xứng EC-12, hoặc short continuation trong downtrend.
- *Interpretation:* nếu nằm sát SSL lớn → short vào ngay trên đích thanh khoản → room nhỏ.
- *Trading implication:* chỉ xét khi DOL là một SSL external xa hơn và room ≥ R tối thiểu.
- *Invalidation:* như thường.
- *Backtest:* `dist_to_dol_R` là biến then chốt.

**EC-14 — OB cùng hướng DOL**
- *Classification:* trường hợp cơ sở của framework.
- *Interpretation:* phản ứng (nếu có) có "đường chạy".
- *Trading implication:* vẫn phải qua G4/G5 (thanh khoản quanh OB, PD array chắn đường).
- *Invalidation:* như thường; thêm: DOL bị chạm trước khi retest → OB mất vai trò continuation.
- *Backtest:* nhóm tham chiếu cho EC-15.

**EC-15 — OB ngược hướng DOL**
- *Classification:* countertrend OB.
- *Interpretation:* M2–M4 không quan tâm DOL → phản ứng vẫn có thể xảy ra, nhưng thường là nhịp hồi.
- *Trading implication:* ngoài framework chính; nếu có playbook countertrend: target IRL gần, size giảm.
- *Invalidation:* chặt hơn (một thân đóng ngoài distal).
- *Backtest:* so E[R] OB cùng hướng vs ngược hướng DOL — đây là một phép thử trực tiếp giá trị của DOL.

**EC-16 — OB chống lại HTF trend**
- *Classification:* countertrend so với D1 — lưu ý: **HTF trend và DOL có thể khác nhau** (D1 bullish nhưng DOL hôm nay là SSL — nhịp hồi).
- *Interpretation:* bearish OB intraday cùng hướng DOL ngày nhưng ngược trend D1.
- *Trading implication:* phải khai báo cái nào thống trị trong framework. Đây cũng là điểm yếu đã ghi nhận của bạn (counter-HTF entries thiếu H1 confirmation) → bắt buộc có H1 MSS trước khi xét.
- *Invalidation:* như thường.
- *Backtest:* tách 4 nhóm theo (cùng/ngược trend D1) × (cùng/ngược DOL).

**EC-17 — OB xuất hiện ngay trước high-impact news**
- *Classification:* (a) OB tiền-tin; (b) OB do chính nến tin tạo ra (nguyên nhân (c) ở §4.2).
- *Interpretation:* tin tức có thể thay đổi mặt bằng giá → OB tiền-tin thuộc "chế độ giá cũ"; nến tin có spread giãn, râu bất thường.
- *Trading implication:* không để lệnh limit tại OB qua tin; không coi nến tin là displacement "sạch" ([[25-OB-Order-Block]] §14.2, §14.6).
- *Invalidation:* đánh giá lại toàn bộ sau tin.
- *Backtest:* cờ `news_within_30m`; phân tích riêng hoặc loại khỏi mẫu chính (khai báo trước).

**EC-18 — OB quá cũ**
- *Classification:* phụ thuộc vào việc nó **còn là structural OB của một range đang hoạt động** hay không.
- *Interpretation:* một D1 OB 3 tháng tuổi vẫn là protected low của range D1 → còn liên quan; một internal H1 OB 2 tuần tuổi đã bị supersede → cũ.
- *Trading implication:* tuổi không tự nó loại OB; trạng thái cấu trúc mới loại.
- *Invalidation:* R-H7.
- *Backtest:* `age_bars` + `still_structural` — tách hiệu ứng tuổi khỏi hiệu ứng supersession (HYP-OB-009).

**EC-19 — OB đã được test nhiều lần (chạm nông nhiều lần)**
- *Classification:* "tested OB" — khác EC-09: chạm/gần chạm, không xuyên sâu.
- *Interpretation:* điểm then chốt — **các lần chạm lặp lại tạo ra những đáy gần bằng nhau ngay tại proximal = equal lows = SSL**. Theo chính logic ICT, SSL này trở thành một **draw**. Nghĩa là OB càng được test nhiều, chính nó càng biến thành mục tiêu thanh khoản. Mâu thuẫn với bằng chứng S/R [^S4] (nhiều lần bật → bật dễ hơn).
- *Trading implication:* coi là vùng hai mặt: có thể giữ, nhưng nếu vỡ thì vỡ mạnh.
- *Invalidation:* như thường.
- *Backtest:* HYP-OB-006 với `touch_count`; thêm `equal_lows_formed_at_proximal`.

**EC-20 — OB hình thành sau liquidity sweep**
- *Classification:* "sweep-origin OB" — cấu hình chuẩn.
- *Interpretation:* thanh khoản dưới OB đã được dọn.
- *Trading implication:* cộng điểm — **nếu** mức bị quét có cấp ≥ L2 (quét micro low thì gần như luôn có).
- *Invalidation:* như thường.
- *Backtest:* HYP-OB-003 với `swept_level_class`.

**EC-21 — OB hình thành trước liquidity sweep (thanh khoản còn nằm ngoài distal)**
- *Classification:* "unprotected OB".
- *Interpretation:* nam châm SSL nằm dưới OB.
- *Trading implication:* **Plan D** — không limit proximal; chờ sweep + reclaim.
- *Invalidation:* sau sweep, nếu không reclaim → invalid.
- *Backtest:* HYP-OB-011 — so E[R] của entry proximal giữa OB protected vs unprotected.

**EC-22 — OB hình thành trong consolidation**
- *Classification:* thường là micro/internal; nhiều ứng viên chồng lấp.
- *Interpretation:* ATR bị nén → displacement "trông" lớn so với ATR baseline (bẫy đo lường, [[50-Displacement-In-Depth]]).
- *Trading implication:* ưu tiên biên range; OB trong consolidation chỉ có ý nghĩa khi là **gốc của leg phá range** (khi đó cấp của nó = cấp của cú phá).
- *Invalidation:* như thường.
- *Backtest:* cờ regime (ví dụ efficiency ratio thấp hoặc `range_width_atr` trong N nến nhỏ).

**EC-23 — OB hình thành trong expansion**
- *Classification:* continuation OB giữa expansion.
- *Interpretation:* nhịp hồi nông; giá thường không quay về tới OB.
- *Trading implication:* FVG thường là POI thực tế hơn OB; internal OB theo R-H4.
- *Invalidation:* như thường.
- *Backtest:* `P(retest)` sẽ thấp — phân tích riêng `P(retest)` và `P(phản ứng | retest)` (7.2).

**EC-24 — OB tồn tại trên một timeframe nhưng không rõ trên timeframe khác**
- *Classification:* OB phụ thuộc TF.
- *Interpretation:* ranh giới nến là lát cắt thời gian tùy ý; H4 có thể gộp nhiều nến H1 thành một nến tăng, "xóa" OB H1; feed broker khác giờ server tạo nến D1 khác (ví dụ nến Chủ nhật).
- *Trading implication:* khai báo TF phát hiện; không "đi tìm" TF có OB đẹp nhất (đó là multiple testing).
- *Invalidation:* theo TF đã khai báo.
- *Backtest:* phát hiện trên nhiều TF và đo độ trùng; "multi-TF confirmed OB" là một feature cần test, không phải điều kiện.

---

## 14. Failure Modes & Common Mistakes

### 14.1 Bốn loại OB cần phân biệt

| Loại | Định nghĩa | Nhận biết | Hậu quả nếu nhầm |
|---|---|---|---|
| **A. Genuine structural OB** | Thỏa OB-DEF v0.1 + cấp L3/L4 + context đúng (G0–G5) | Có thể chỉ ra swing được bảo vệ, thanh khoản đã lấy, DOL | **Vẫn có thể thua** — "genuine" không có nghĩa "chắc thắng". Một lệnh thua ở OB loại A theo đúng plan là *good loss* |
| **B. Technically valid, low-quality** | Thỏa định nghĩa nhưng đặc trưng yếu: L1–L2, displacement < P50, sai vị trí, không có room | OBQS thấp; trượt ở một hoặc nhiều cổng | Trade quá nhiều, win rate thấp, "OB không hoạt động" — thực ra là không lọc |
| **C. Misidentified OB** | **Không** thỏa định nghĩa: không displacement, không BOS, chọn sai nến, lấy OB từ TF khác mà không khai báo | Không trả lời được "displacement nào? phá swing nào?" | Toàn bộ phân tích xây trên một vật thể không tồn tại |
| **D. Retrospectively valid, no predictive value** | Được định nghĩa bằng thông tin **không có** tại thời điểm quyết định | Dùng swing chưa xác nhận; chọn zone *vì* giá đã phản ứng ở đó; biết OB nào trong nhiều OB đã giữ | Backtest đẹp, live thua — dạng nguy hiểm nhất vì *trông* như bằng chứng |

### 14.2 "Thị trường có tạo OB giả để bẫy ICT traders không?"

Câu hỏi này thường được trả lời bằng narrative "Smart Money cố tình tạo OB giả". Narrative đó **không thể kiểm chứng** từ chart (không quan sát được ý định). Quan trọng hơn: **nó không cần thiết**, vì có một loạt giải thích đơn giản hơn, mỗi cái đủ để sinh ra hiện tượng "OB đẹp mà fail":

1. **Tính phổ biến của OB (ambiguous/permissive definitions):** định nghĩa lỏng sinh ra hàng chục OB mỗi tuần. Với số lượng đó, phần lớn *phải* fail — không cần ai "tạo" chúng.
2. **Liquidity events không cần ý định:** stop của người mua OB tụ dưới distal. Bất kỳ người bán lớn nào cũng hưởng lợi khi giá đi xuyên qua (thêm thanh khoản), và bất kỳ người mua lớn nào cũng hưởng lợi khi mua được từ các stop đó (sweep rồi đảo). Cả hai kết cục đều sinh ra từ **cấu trúc lệnh**, không từ âm mưu. Đây chính là cơ chế được bàn ở [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]].
3. **Failed breakouts là thường xuyên:** các cú phá cấu trúc thất bại là hiện tượng phổ biến ở mọi thị trường; mỗi lần như vậy, "OB" tại gốc cú phá bị vô hiệu.
4. **Regime change:** một OB hình thành trong regime trending sẽ hành xử khác khi thị trường chuyển sang ranging hoặc volatility thay đổi.
5. **News-driven movement:** tin tức định giá lại tài sản; OB tiền-tin mất ý nghĩa (EC-17).
6. **Random price structure (M6):** chuỗi giá có xu hướng + nhiễu tự nhiên sinh ra các hình dạng "OB" ngẫu nhiên.
7. **Survivorship bias:** chart mẫu, bài giảng, screenshot trên mạng là những OB đã thành công. Hàng nghìn OB fail không ai chụp lại.
8. **Hindsight bias:** sau khi biết kết quả, nhận ra OB "đúng" là dễ (14.3).
9. **Selection bias:** trader nhớ và log những OB mình chú ý; OB bị bỏ qua (vì "không đủ đẹp") không vào dữ liệu — và tiêu chí "đủ đẹp" thường bị điều chỉnh theo kết quả.
10. **Multiple-testing problem:** mỗi trader thử nhiều TF, nhiều cách vẽ (body/wick, single/series), nhiều entry (proximal/MT/open). Với đủ nhiều phép thử, luôn có một tổ hợp "khớp" với quá khứ.

> [!important] Kết luận
> "OB giả" là một nhãn *hậu nghiệm* cho những OB đã thất bại. Câu hỏi hữu ích không phải "ai tạo OB giả?" mà là **"những đặc trưng quan sát được *trước* nào phân biệt OB giữ với OB fail — và sự phân biệt đó có ổn định ngoài mẫu không?"** Nếu không có đặc trưng nào như vậy, thì "OB giả" chỉ là tên gọi khác của "phương sai".

### 14.3 Vì sao "perfect OB" sau sự kiện không thể xác định trước — một phép tính minh họa

![[OB-DeepResearch-Hindsight-Coverage.svg|760]]
*Hình 5 — Trước quyết định (trái): năm vùng OB ứng viên dưới giá. Sau sự kiện (phải): nhịp hồi kết thúc ở một mức, và luôn có một OB "hoàn hảo" ở gần đó — kể cả khi điểm quay đầu là ngẫu nhiên.*

Phép tính minh họa (không phải dữ liệu, chỉ là số học):
- Không gian hồi giá khả dĩ dưới giá hiện tại: khoảng **6 ATR**.
- Trong đó có **5 OB ứng viên** (internal + structural + HTF), mỗi OB rộng **0.4 ATR**.
- Độ phủ của các zone: 5 × 0.4 / 6 ≈ **33%**. Nghĩa là một điểm quay đầu **hoàn toàn ngẫu nhiên** có khoảng 1/3 cơ hội rơi *trong* một OB.
- Nếu chấp nhận "near miss" ±0.2 ATR (như Scenario A), mỗi zone hiệu dụng rộng 0.8 ATR → độ phủ ≈ 4 / 6 ≈ **67%**.
- Thêm tự do chọn TF (M15/H1/H4), body hay wick, single hay series → độ phủ hiệu dụng còn cao hơn.

**Hệ quả:** tìm thấy "một OB nơi giá đã quay đầu" sau sự kiện là điều **được kỳ vọng ngay cả khi OB không có giá trị gì**. Điều này **không chứng minh OB vô dụng** — nó chứng minh rằng **ví dụ hậu nghiệm không phải là bằng chứng**. Bằng chứng duy nhất là một kế hoạch được cam kết *trước* (OB nào, hành động gì) được đánh giá trên nhiều mẫu, so với đối chứng.

### 14.4 Mười bảy lỗi phổ biến

| # | Lỗi | Vì sao gây hại | Cách sửa (rule) |
|---|---|---|---|
| 1 | Mark mọi last down candle là bullish OB | Định nghĩa D0 → hàng chục OB → không lọc được | Bắt buộc Tầng 1 + 2 (displacement + BOS) |
| 2 | Mark mọi last up candle là bearish OB | Như trên | Như trên |
| 3 | Không yêu cầu displacement | Nến không phải là gốc của mất cân bằng nào | Đo `disp_net_atr`, percentile ([[08-Mistake-Weak-Displacement]]) |
| 4 | Không xét structure | Không biết OB cấp nào, không có invalidation logic | Ghi `broken_swing_level`; phân cấp L1–L4 |
| 5 | Không xét liquidity | Bỏ qua SSL dưới distal → bị cuốn trong Scenario D | Cổng G4; [[13-Mistake-Trading-Into-Unswept-Liquidity]] |
| 6 | Chọn OB chỉ vì giá từng phản ứng ở đó | Đó là S/R, không phải OB; và là chọn theo kết quả | OB được định nghĩa bởi displacement, không bởi phản ứng |
| 7 | Chọn OB sau khi biết outcome | Loại D — backtest vô giá trị | Log OB tại `t_avail`, trước retest; chụp màn hình có timestamp |
| 8 | Overfitting | Thêm filter cho đến khi quá khứ "hoàn hảo" | Khóa rule v0.x trước; out-of-sample; đếm số phép thử |
| 9 | Chọn timeframe tùy ý | Multiple testing ngầm | Khai báo TF phát hiện theo framework (D1/H1/M5) |
| 10 | Dùng OB như standalone signal | Gộp location với trigger | Tách location / evidence / trigger (§11.4) |
| 11 | Ignore HTF context | OB đúng hình, sai narrative ([[09-Mistake-Wrong-daily-bias]]) | Cổng G0; R-H1 |
| 12 | Ignore DOL | Không có đường chạy; R:R bị chặn | Cổng G5; `dist_to_dol_R` |
| 13 | Treat CE như magic level | Kỳ vọng sai, đặt stop sai | CE là heuristic thỏa hiệp (Scenario C) |
| 14 | Treat wick penetration như automatic invalidation | Bị stop bởi chính cú sweep xác nhận | Scenario D; invalidation theo thân đóng + OB-INVAL v0.1 |
| 15 | Treat candle count như universal law | "3 nến" không có cơ sở phổ quát | Hazard analysis (Scenario F); quy đổi theo TF |
| 16 | Confuse reaction với prediction | "Giá đã bật ở OB" ≠ "OB dự đoán được cú bật" | So với vùng đối chứng (HYP-OB-001) |
| 17 | Confuse explanation với evidence | Narrative giải thích được mọi kết quả → không bác bỏ được | Chỉ chấp nhận mệnh đề có thể sai; ghi hypothesis + điều kiện bác bỏ |

---

## 15. Bullish Examples (ví dụ dựng — synthetic)

> [!warning] Đọc trước
> Các ví dụ dưới đây là **dựng** để luyện chuỗi suy luận. Giá là minh họa, không phải dữ liệu lịch sử của ngày cụ thể nào. **Kết quả (thắng/thua) cố ý không được nêu** — vì bài học nằm ở việc mọi quyết định chỉ dùng thông tin có sẵn tại thời điểm đó, không nằm ở kết cục của một mẫu đơn lẻ.

### B1 — EURUSD: Structural H1 OB sau sweep, lồng trong D1 OB (reversal ở discount D1)

**Context (D1):** cấu trúc D1 bullish — protected low 1.0700 còn nguyên, BOS gần nhất vượt 1.0950. Dealing range D1: 1.0700–1.1000, EQ 1.0850. Giá hồi về 1.0800 → `pd_pos_d1` ≈ 0.33 (discount). D1 bullish OB (L4): 1.0760–1.0810, là gốc leg đã phá 1.0950. DOL D1: equal highs 1.1000 (BSL).

**Liquidity:** H1 equal lows 1.0788 và PDL 1.0785 — SSL chưa quét, nằm **bên trong** D1 OB (không phải dưới distal D1 OB).

**Structure (H1):** H1 đang giảm (nhịp hồi của D1), lower high gần nhất 1.0842 — đây là đỉnh external của range hồi H1.

**Displacement:** London mở cửa, giá quét xuống 1.0779 (qua equal lows/PDL ~0.5 ATR_H1, với ATR_H1 ≈ 18 pip). Nến H1 down-close cuối: O 1.0796 / H 1.0801 / L 1.0779 / C 1.0782. Hai nến H1 tiếp theo tăng mạnh, nến thứ hai đóng 1.0847 > 1.0842 → **H1 MSS bullish**. `disp_net_atr` ≈ (1.0847 − 1.0782)/0.0018 ≈ 3.6. FVG H1: 1.0801–1.0812.

**OB:** H1 bullish OB — full 1.0779–1.0801, body 1.0782–1.0796, `mt_body` 1.0789, `ce_range` 1.0790. Cấp **L3** (displacement phá đỉnh external của range H1). Self-sweep (râu của chính nến OB quét SSL). Nested trong D1 OB và **hình thành sau khi giá vào zone D1** → thỏa R-H2. `t_avail` = đóng cửa nến H1 phá 1.0842.

**Retracement:** phiên NY, giá hồi từ 1.0860 về, lấp FVG, chạm 1.0795 → penetration = (1.0801 − 1.0795)/(1.0801 − 1.0779) ≈ 27%.

**Reaction (M5 evidence):** M5 quét low cục bộ 1.0798 xuống 1.0795 → M5 MSS vượt 1.0812 với displacement → M5 FVG 1.0803–1.0808.

**Entry:** limit tại CE của M5 FVG ≈ 1.0805. **Invalidation:** stop dưới M5 sweep low 1.0795 − 2 pip = 1.0793 (rủi ro 12 pip). Stop dự phòng (nếu dùng stop cấu trúc H1): dưới distal H1 OB 1.0777. **OB invalidation:** thân H1 đóng dưới 1.0779.

**Target:** T1 = đỉnh H1 1.0860 (≈ +4.6R với stop 12 pip) — chốt một phần; T2 = D1 DOL 1.1000 cho runner theo plan swing.

**Vì sao là ví dụ tốt:** qua đủ G0–G7; OB cấp L3 với invalidation trùng cấu trúc; thanh khoản đã bị lấy tại gốc; có DOL rõ; M5 cho evidence đúng thứ tự.

**Dòng thời gian thông tin (chống hindsight):**
- **T0 (trước London):** biết context D1, D1 OB, H1 equal lows, LH 1.0842. *Chưa biết* có sweep hay không → chưa có H1 OB nào để giao dịch.
- **T1:** sweep xảy ra — vẫn chưa có OB (chỉ là một nến giảm).
- **T2:** nến phá 1.0842 đóng cửa → OB **trở nên khả dụng**. Mọi phân tích dùng OB này trước T2 là look-ahead.
- **T3:** retracement vào FVG/OB — chưa phải tín hiệu.
- **T4:** M5 sweep → MSS → displacement → entry theo rule.
- **T5:** kết quả — *không liên quan tới việc đánh giá chất lượng quyết định*.

### B2 — NQ1: Continuation OB sau re-map dealing range (supersession)

**Context (D1):** D1 bullish expansion; DOL D1 = BSL 21,900 (synthetic). Giá đang ở nửa trên range D1 — tức "premium D1". Đây là điểm cần phản biện: trong pha expansion, logic ERL → IRL → ERL cho phép mua ở IRL dù đang ở premium của range D1 **cũ**, miễn là DOL D1 ở phía trên và không có bearish PD array D1 chắn đường. Việc này mâu thuẫn một phần với rule "chỉ mua ở discount" → ghi nhận như biến cần test (HYP-OB-008).

**Structure (H1):** H1 vừa BOS vượt 21,600 bằng displacement xuất phát từ H1 low 21,420. **Re-map:** range H1 mới = 21,420 → 21,690 (đỉnh mới), EQ 21,555. Swing 21,420 trở thành protected low mới; structural OB cũ ở 21,250 bị **supersede** (R-H3) — chỉ còn là reference sâu.

**OB:** nến H1 down-close tại đáy 21,420: full 21,420–21,455. Cấp L3 của range H1 mới. FVG H1 trên leg: 21,470–21,500.

**Liquidity:** pre-market low 21,448 (SSL nội bộ) nằm ngay trên proximal OB.

**Retracement:** ngày hôm sau, giá hồi về 21,470 lúc gần NY open → `pd_pos_h1` = (21,470 − 21,420)/270 ≈ 0.19 (discount sâu của range mới). Giá lấp FVG, xuống 21,441 — quét pre-market low, chạm proximal OB 21,455 và xuyên nhẹ (penetration ≈ 40%).

**Reaction (M5):** M5 MSS vượt 21,488 với displacement; M5 FVG 21,462–21,474.

**Entry:** 21,468. **Invalidation:** stop 21,436 (dưới sweep low 21,441 − 5 điểm) → rủi ro 32 điểm. OB invalidation: thân H1 đóng dưới 21,420 (protected low).

**Target:** T1 = đỉnh range H1 21,690 (ERL); T2 = D1 DOL 21,900.

**Vì sao là ví dụ tốt:** minh họa supersession và re-map: `pd_pos` được tính trên range **mới**, không phải range cũ (nếu tính trên range cũ, OB này nằm ở premium và bị loại nhầm — EC-12). Thanh khoản (pre-market low) bị lấy **ngay trên/tại** OB, không phải dưới distal.

### B3 — XAUUSD: Unprotected OB → Plan D (chờ sweep thanh khoản dưới distal)

**Context (D1):** D1 bullish; range D1 3,200–3,420; giá 3,285 → `pd_pos_d1` ≈ 0.39. DOL: equal highs D1 3,420.

**OB:** H1 structural bullish OB 3,272–3,280 (gốc leg MSS hai ngày trước). Cấp L3.

**Liquidity — điểm mấu chốt:** H1 equal lows 3,268.5/3,268.8 nằm **dưới distal** khoảng 3.5 điểm ≈ 0.3 ATR_H1 (ATR_H1 ≈ 12). Cổng G4 gắn cờ **"unprotected OB → Plan D"**: không đặt limit ở proximal.

**Retracement & reaction:** NY AM, giá vào OB tại 3,279, không phản ứng, xuyên distal xuống 3,264.9 (quét equal lows ≈ 0.3 ATR), nhưng nến H1 **đóng lại** 3,274.2 bên trong OB → Scenario D. M5: MSS vượt 3,281 với displacement; M5 FVG 3,276–3,279.

**Entry:** 3,277.5. **Invalidation:** stop dưới sweep low 3,264.9 − 1.5 = 3,263.4 (rủi ro 14.1 điểm). OB invalidation: thân H1 đóng dưới 3,264.9.

**Target:** T1 = swing high H1 3,318; T2 = D1 DOL 3,420.

**Vì sao là ví dụ tốt:** một limit ở proximal 3,280 với stop 3,270 sẽ bị stop bởi chính cú sweep. Rule Plan D được viết **trước**. Chi phí của rule: nếu giá bật từ OB mà không sweep, bạn bỏ lỡ lệnh — chi phí này được chấp nhận và **đo** qua `missed_trade_rate`. Đừng đánh giá Plan D chỉ bằng những lần nó "cứu" bạn (đó là selection bias).

---

## 16. Bearish Examples (ví dụ dựng — synthetic)

### S1 — GBPUSD: D1 bearish OB (L4) + H1 structural OB sau BSL sweep

**Context (D1):** D1 bearish — protected high 1.3000; range D1 1.2600–1.3000, EQ 1.2800. Giá hồi lên 1.2880 → `pd_pos_d1` ≈ 0.70 (premium). D1 bearish OB (L4): 1.2870–1.2920. DOL: PDL 1.2790 (IRL) → equal lows D1 1.2600 (ERL).

**Liquidity:** PDH 1.2893 (BSL) nằm trong D1 OB.

**Structure (H1):** H1 đang tăng (nhịp hồi), higher low gần nhất 1.2835.

**Displacement:** London, giá quét PDH lên 1.2901. Nến H1 up-close cuối: O 1.2881 / H 1.2901 / L 1.2878 / C 1.2897. Hai nến H1 giảm mạnh, đóng 1.2826 < 1.2835 → **H1 MSS bearish**. FVG H1: 1.2862–1.2878.

**OB:** H1 bearish OB — full 1.2878–1.2901, body 1.2881–1.2897, `mt_body` 1.2889. Cấp L3; self-sweep BSL; nested trong D1 OB, hình thành sau khi giá vào zone D1.

**Retracement:** NY, giá hồi lên lấp FVG, chạm 1.2880 (penetration ≈ 9%).

**Reaction (M5):** M5 quét high cục bộ 1.2877 lên 1.2881 → MSS xuống dưới 1.2858 với displacement → M5 FVG 1.2866–1.2871.

**Entry:** 1.2868. **Invalidation:** stop 1.2884 (trên sweep high + 3 pip) → 16 pip. OB invalidation: thân H1 đóng trên 1.2901.

**Target:** T1 = PDL 1.2790 (≈ +4.9R); T2 = D1 SSL 1.2600.

**Vì sao là ví dụ tốt:** D1 OB rộng 50 pip — không thể dùng làm stop; nó chỉ khoanh vùng. Toàn bộ quản trị rủi ro đến từ cấu trúc H1/M5 bên trong. Đây là minh họa đúng của "D1 = context, H1 = setup, M5 = execution".

### S2 — NQ1: Bearish continuation — FVG trước, OB là Plan B

**Context (D1):** D1 bearish sau MSS D1; DOL D1 = SSL 20,800.

**Structure (H1):** H1 BOS xuống dưới 21,150 (đáy external của range H1) bằng displacement từ swing high 21,340 (protected high). Re-map range H1: 21,020 (đáy mới) → 21,340; EQ 21,180.

**OB & FVG:** H1 bearish OB tại gốc: 21,305–21,340 (L3). FVG H1 trên leg: 21,230–21,265.

**Plan viết trước:**
- **Plan A (FVG, nông hơn):** nếu giá hồi vào FVG 21,230–21,265 (premium của range mới, `pd_pos` ≈ 0.7–0.8) và có M5 sweep → MSS → displacement → vào.
- **Plan B (OB, sâu hơn):** nếu giá xuyên qua FVG không phản ứng và đi vào OB 21,305–21,340 → chờ cùng quy trình M5 bên trong OB; stop trên 21,345.

**Diễn biến:** giá hồi lên 21,262 (trong FVG), M5 quét high 21,255 lên 21,262, M5 MSS xuống dưới 21,228 với displacement → **Plan A kích hoạt**. Entry 21,240; stop 21,272 (32 điểm); T1 = 21,020 (ERL H1).

**Vì sao là ví dụ tốt:** OB **không được test** — và đó **không phải** "OB fail". Plan có điều kiện xử lý cả hai nhánh mà không cần dự đoán giá sẽ dừng ở FVG hay OB. Nếu log backtest, ghi `ob_tested = false`, `entry_array = FVG`.

### S3 — EURUSD: Nested OB không có FVG (EC-01) — entry bằng M5 OB

**Context (D1):** D1 bearish; D1 bearish OB (L4) 1.0980–1.1030; giá hồi vào zone.

**Liquidity & Displacement (H1):** giá quét H1 equal highs 1.1002 lên 1.1008; H1 MSS xuống với displacement đủ mạnh (`disp_net_atr` > P80) nhưng các nến **chồng lấp râu** → **không có FVG H1** (EC-01).

**OB:** H1 bearish OB 1.0996–1.1008 (body 1.0998–1.1005). Nested trong D1 OB, hình thành sau khi giá vào zone.

**Reaction (M5):** giá hồi vào H1 OB tại 1.0999 → M5 MSS xuống dưới 1.0990 với displacement. M5 FVG chỉ rộng 0.6 pip (< 3 lần spread → nhiễu theo R-H5). Dùng **M5 OB tại gốc leg MSS**: 1.0995–1.0999.

**Entry:** 1.0997 (MT của M5 OB). **Invalidation:** stop 1.1010 (trên sweep high H1 1.1008 + 2 pip) → 13 pip. **Target:** T1 = đáy H1 1.0950 (≈ +3.6R); T2 = SSL D1.

**Vì sao là ví dụ tốt:** thiếu một đặc trưng (FVG) không làm setup vô hiệu — nó hạ OBQS (Grade B) và theo plan thì giảm size. Minh họa cách xử lý edge case bằng rule đã viết sẵn thay vì ứng biến.

---

## 17. Counterexamples — trông như OB hợp lệ nhưng không phải tradeable edge

### CX1 — OB "sách giáo khoa" ở EQ, ngược D1 DOL

**Cấu trúc nhìn thấy:** D1 bearish, DOL = SSL D1 phía dưới. Trên H1, trong một leg giảm, giá quét Asian low, tạo nến down-close, rồi displacement mạnh (> P80) để lại FVG và **phá một đỉnh internal** (L2). Hình dạng: hoàn hảo — sweep, OB, displacement, FVG, BOS.

**Vì sao không phải edge:**
- **G0 thất bại:** bullish OB ngược D1 bias và ngược DOL.
- **Cấp L2:** chỉ phá cấu trúc internal trong một leg giảm → chức năng kỳ vọng là **gốc của nhịp hồi / inducement**, không phải gốc của trend mới.
- **Vị trí:** `pd_pos_d1` ≈ 0.52 — ngay EQ.
- Các đặc trưng "đẹp" (sweep, FVG, displacement) là **descriptive** cho một cú bật cục bộ; chúng không nói gì về việc retest sẽ ra sao trong context bearish.

**Bẫy hindsight:** nếu retest bật được 40 pip trước khi giá tiếp tục giảm, người xem lại sẽ nói "OB đã hoạt động". Nhưng một lệnh long với target ở DOL phía trên là **ngược hướng draw** — và mẫu này, nếu tính đúng theo rule, là một lệnh không được phép vào.

**Bài học:** *độ hoàn chỉnh của pattern ≠ tính hợp lệ của context.*

### CX2 — OB trong consolidation phiên Á: ảo giác ATR

**Cấu trúc nhìn thấy:** EURUSD phiên Á, range 12 pip. ATR M5 lúc 03:00 chỉ ≈ 1.8 pip. Một cú đẩy 5 pip = **2.8 × ATR** — "displacement" theo ngưỡng ATR thô. Nó phá micro high của Asian range (L1) và để lại FVG 0.4 pip.

**Vì sao không phải edge:**
- **ATR baseline bị nén** — 2.8 ATR phiên Á có thể chỉ tương đương 0.5 ATR phiên London. Nếu dùng percentile theo phiên, cú đẩy này nằm dưới P50.
- **Cấp L1**, FVG **nhỏ hơn spread** phiên Á (R-H5 → noise).
- Retest thường xảy ra lúc London mở cửa — thời điểm có các sự kiện thanh khoản lớn hơn nhiều, "không quan tâm" tới một micro OB phiên Á.

**Bài học:** *ngưỡng chuẩn hóa sai sẽ biến nhiễu thành tín hiệu.* Đây là lý do §19 đề xuất percentile theo instrument × phiên thay cho bội số ATR cố định.

### CX3 — "Perfect OB" do chọn sau sự kiện

**Cấu trúc nhìn thấy (sau sự kiện):** trong một nhịp hồi H1, giá quay đầu đúng ở 1.0831 — "trúng" OB-b (1.0826–1.0834), phản ứng mạnh. Screenshot trông như bằng chứng hoàn hảo.

**Thông tin tại thời điểm quyết định (trước sự kiện):** dưới giá có **bốn** OB ứng viên:
- OB-a 1.0848–1.0853 (internal, L2),
- OB-b 1.0826–1.0834 (internal, L2),
- OB-c 1.0801–1.0809 (structural, L3, tại protected low),
- OB-d 1.0762–1.0778 (HTF, L4).

Trader theo G0–G7 (với R-H4 không thỏa cho internal OB lúc đó) sẽ có **Plan A tại OB-c**, và OB-a/OB-b được gắn nhãn "internal/inducement". Giá quay đầu ở OB-b → **không có lệnh** (hoặc lệnh bị bỏ lỡ).

**Vì sao không phải edge:** "OB-b hoàn hảo" chỉ hiện ra **sau** khi biết giá quay đầu ở đâu. Với bốn zone, mỗi zone ≈ 0.4 ATR_H1, trong không gian hồi ≈ 5 ATR, độ phủ ≈ 32% (≈ 64% nếu tính near miss) — một điểm quay đầu ngẫu nhiên cũng dễ "trúng" một OB.

**Điều CX3 KHÔNG nói:** nó không nói internal OB vô dụng. Nó nói rằng nếu bạn muốn giao dịch internal OB, **rule phải cho phép điều đó trước** (R-H4), và bạn phải chấp nhận giao dịch *tất cả* internal OB thỏa rule — kể cả OB-a (có thể fail). Chỉ khi đó mới đo được internal OB có edge hay không.

---

## 18. Decision Framework — cây quyết định từ Context đến Target

![[OB-DeepResearch-Decision-Tree.svg|760]]
*Hình 6 — Cây quyết định rút gọn. Mỗi ô thoi là một câu hỏi có đáp án đo được; mỗi nhánh "KHÔNG" kết thúc bằng một hành động rõ ràng (NO TRADE / WAIT / loại OB) thay vì "cân nhắc thêm".*

Cây dưới đây được viết để sau này có thể chuyển thẳng thành quy tắc định lượng: mỗi câu hỏi tương ứng một hoặc vài biến ở §19.

```
[1] MARKET CONTEXT — D1
 ├─ Q1.1 Protected swing D1 còn nguyên? ──────────── KHÔNG → bias neutral → NO TRADE (chờ D1 MSS)
 ├─ Q1.2 DOL D1 xác định được (pool cụ thể, chưa quét)? ─ KHÔNG → NO TRADE
 ├─ Q1.3 Giá ở phía đúng của range D1?
 │        ├─ Có (discount cho long) → tiếp
 │        └─ Không → chỉ xét continuation nếu có logic ERL→IRL→ERL rõ + không có PD array D1 ngược chặn; nếu không → WAIT
 └─ OUTPUT: giả thuyết bias + điều kiện vô hiệu D1

[2] LIQUIDITY MAP
 ├─ Q2.1 Pool nào vừa bị lấy (ERL/IRL)?  → xác định pha: expansion / retracement
 ├─ Q2.2 Pool chưa quét nào nằm GIỮA giá và POI? → POI phía trên pool đó = inducement
 └─ Q2.3 Pool chưa quét nào nằm DƯỚI distal POI (≤ 0.5 ATR_H1)? → cờ UNPROTECTED → Plan D

[3] STRUCTURE — H1
 ├─ Q3.1 H1 cùng hướng D1 hay đang hồi?
 └─ Q3.2 Range H1 hiện tại (sau re-map gần nhất)? EQ ở đâu?

[4] DISPLACEMENT → CANDIDATE OB
 ├─ Q4.1 Có displacement đạt OB-DEF v0.1 (Tầng 1)? ─── KHÔNG → không có OB
 ├─ Q4.2 Displacement đóng cửa qua swing đã xác nhận (Tầng 2)? ─ KHÔNG → chỉ là candidate (log làm đối chứng)
 └─ Q4.3 Đã qua t_avail? ────────────────────────────── KHÔNG → chưa được dùng

[5] OB QUALITY & HIERARCHY
 ├─ Q5.1 Cấp? L1 → chỉ refine M5 │ L2 → thỏa R-H4? │ L3/L4 → tiếp
 ├─ Q5.2 Đã bị invalidate/tiêu thụ? ───────────────── CÓ → loại
 └─ Q5.3 OBQS v0.1 → Grade A / B / C (chỉ để xếp thứ tự và sizing theo plan)

[6] HTF ALIGNMENT → POI
 ├─ Q6.1 Cùng hướng D1 bias? ───────────────────────── KHÔNG → loại (trừ playbook countertrend)
 ├─ Q6.2 pd_pos_h1 phù hợp (discount cho long)? ────── KHÔNG → danh sách inducement/IRL
 ├─ Q6.3 Room tới DOL ≥ R_min, không PD array ngược chặn? ─ KHÔNG → loại
 └─ Q6.4 Còn ≥ 2 POI? → viết Plan A / Plan B  │  Cờ UNPROTECTED? → viết Plan D
      OUTPUT: POI list + kế hoạch có điều kiện, viết TRƯỚC khi giá tới

[7] PRICE RETURN
 ├─ Q7.1 Giá vào vùng ảnh hưởng POI (≤ proximal + 0.25 ATR_H1) trong kill zone? ─ KHÔNG → WAIT
 ├─ Q7.2 Tin high-impact trong ±30 phút? ──────────── CÓ → STAND ASIDE
 └─ Q7.3 Kịch bản:
       A/B/C → sang [8]
       D (râu quét distal, đóng trong) → chờ reclaim + [8]
       E (đóng ngoài 1–3 nến TF OB) → SUSPENDED → reclaim? sang [8] : INVALID
       F (acceptance ngoài) → INVALID → theo dõi Breaker (hướng ngược)

[8] REACTION EVIDENCE — M5
 ├─ Q8.1 M5 sweep cục bộ trong/sát POI? → cộng chất lượng (không bắt buộc, nhưng log)
 ├─ Q8.2 M5 MSS đóng cửa qua swing M5 có ý nghĩa? ──── KHÔNG → NO ENTRY
 ├─ Q8.3 Displacement đạt chuẩn (percentile ≥ ngưỡng plan)? ─ KHÔNG → NO ENTRY
 └─ Q8.4 MSS xảy ra BÊN TRONG vùng ảnh hưởng POI? ─── KHÔNG → NO ENTRY

[9] ENTRY
 ├─ Mặc định: limit tại M5 FVG (CE hoặc edge — theo plan đã khai báo)
 ├─ Không có FVG hợp lệ: M5 OB tại gốc leg MSS (MT)
 └─ Plan D: vào sau reclaim + MSS (limit tại FVG của leg reclaim)

[10] INVALIDATION (ba lớp, viết riêng)
 ├─ Trade stop: dưới sweep low M5 / distal M5 OB (+ buffer đã khai báo)
 ├─ Setup invalidation: H1 OB theo OB-INVAL v0.1
 └─ Bias invalidation: protected swing D1

[11] TARGET / DOL
 ├─ T1: IRL / swing H1 gần nhất (chốt một phần theo plan)
 ├─ T2: DOL H1 → D1
 └─ R tới T1 < R_min? → BỎ LỆNH (dù mọi thứ khác đẹp)
```

---

## 19. Quantitative Framework — biến OB thành biến số đo được

### 19.1 Từ điển biến

Chia theo **thời điểm biết được** — đây là cách đơn giản nhất để chống look-ahead: biến ở nhóm sau không bao giờ được dùng để dự đoán nhóm trước.

**(a) Biến định nghĩa — biết tại `t_avail`**

| Biến | Công thức / định nghĩa | Khách quan? |
|---|---|---|
| `ob_full_hi`, `ob_full_lo` | max High, min Low của nến/chuỗi OB | Có |
| `ob_body_hi`, `ob_body_lo` | max(Open, Close), min(Open, Close) của chuỗi | Có |
| `ob_open` | Open của nến OB cuối | Có |
| `mt_body`, `ce_range` | Điểm giữa body / full | Có |
| `ob_width_atr` | (hi − lo) / ATR_base — cho cả full và body | Có |
| `ob_series_len` | Số nến down-close liên tiếp | Có |
| `t_form`, `t_avail` | Thời điểm nến OB đóng / nến xác nhận BOS đóng | Có |

**(b) Đặc trưng hình thành — biết tại `t_avail`**

| Biến | Công thức | Khách quan? |
|---|---|---|
| `disp_net_atr` | (Close_cuối_L − Open_đầu_L) / ATR_base | Có |
| `disp_pctile` | Percentile của `disp_net_atr` trong phân bố 250 ngày **quá khứ** cùng instrument × phiên | Có |
| `disp_body_ratio_mean` | Trung bình \|C−O\| / (H−L) trong L | Có |
| `disp_overlap` | Tổng phần chồng lấp giữa các nến liên tiếp / tổng range | Có |
| `fvg_present`, `fvg_size_atr` | FVG 3 nến trong L; độ rộng / ATR_base | Có |
| `broken_swing_level` | Cấp (L1–L5) của swing bị phá, theo swing detector đã khóa | Có (khi detector cố định) |
| `break_margin_atr` | (Close phá − mức swing) / ATR_base | Có |
| `sweep_prior`, `swept_level_class`, `sweep_depth_atr` | Có quét mức nào trong k nến trước L; cấp của mức; độ sâu | Có (khi quy tắc phân loại mức cố định) |
| `ob_at_swing_extreme` | \|distal − cực trị swing\| ≤ 0.1 ATR | Có |
| `session_formation`, `news_formation` | Phiên; có tin trong ±30′ | Có |

**(c) Đặc trưng context — đo tại thời điểm retest (nhưng chỉ dùng dữ liệu tới thời điểm đó)**

| Biến | Công thức | Khách quan? |
|---|---|---|
| `d1_bias` | +1/−1/0 theo quy tắc: hướng BOS D1 gần nhất và protected swing còn nguyên | Trung bình (phụ thuộc quy tắc) |
| `pd_pos_h1`, `pd_pos_d1` | (ob_mid − range_lo)/(range_hi − range_lo), range theo quy tắc re-map | Trung bình |
| `ob_inside_htf_poi` | OB nằm trong PD array D1/H4 cùng hướng | Trung bình |
| `dist_to_dol_R` | (DOL − entry)/(entry − stop) với DOL = pool chưa quét gần nhất theo hướng bias | Trung bình |
| `unprotected` | Có pool chưa quét trong 0.5 ATR_H1 dưới distal | Có |
| `touch_count`, `mitigation_count` | Số lần vào trong ε của proximal / số lần thân đóng qua MT, trước retest này | Có |
| `age_bars`, `still_structural` | Tuổi; còn là OB structural của range đang hoạt động? | Có |
| `ob_order_in_leg` | Thứ tự OB trong chuỗi (1 = gần giá nhất) | Có |
| `session_retest`, `news_retest` | Phiên; tin ±30′ | Có |

**(d) Biến retest — đo trong lúc retest**

| Biến | Công thức |
|---|---|
| `approach_min_dist_atr` | Khoảng cách gần nhất tới proximal (âm nếu xuyên) |
| `penetration` | (proximal − extreme retest) / (proximal − distal) |
| `distal_swept`, `sweep_depth_beyond_distal_atr` | Râu xuyên distal; độ sâu |
| `closes_outside_n` | Số thân nến TF OB liên tiếp đóng ngoài distal |
| `time_in_zone_bars` | Số nến ở trong zone trước khi rời |
| `ltf_mss`, `ltf_disp_pctile`, `ltf_fvg_size_atr` | Bằng chứng M5 |

**(e) Biến kết quả — KHÔNG BAO GIỜ dùng làm biến dự đoán**

| Biến | Công thức |
|---|---|
| `mfe_atr_N`, `mae_atr_N` | MFE/MAE theo ATR trong N nến sau extreme retest |
| `bars_to_1atr` | Tốc độ phản ứng |
| `r_multiple` | Kết quả lệnh theo R |
| `mfe_R`, `mae_R` | MFE/MAE theo R của lệnh |
| `time_to_target`, `time_in_trade` | |
| `hit_T1`, `hit_T2`, `stopped` | |

### 19.2 Chuyển khái niệm chủ quan thành định nghĩa đo được (v0.1)

| Khái niệm chủ quan | Định nghĩa đo được v0.1 | Lý do chọn | Phương án thay thế cần test |
|---|---|---|---|
| **"Strong displacement"** | `disp_pctile` ≥ P80 **và** `disp_body_ratio_mean` ≥ 0.6 **và** (`fvg_present` **hoặc** `disp_overlap` ≤ 0.2) | Percentile tự thích nghi với instrument và phiên (tránh CX2); body ratio loại nến râu dài; FVG/overlap đo tính một chiều | Bội số ATR cố định (1.5×); ngưỡng P70/P90 |
| **"Important swing"** | Swing có cấp ≥ L3 theo DC đa ngưỡng: cấp = θ lớn nhất mà điểm vẫn là turning point; hoặc swing là cực trị của dealing range TF | Cấp swing là biến liên tục theo θ → phân tầng không cần phán đoán | Fractal n = 2/3/5; "swing đã tạo BOS" |
| **"Clean OB"** | `ob_width_atr` trong [0.1, 1.5] **và** không có OB ngược hướng chồng lấp (`opposite_overlap` = false) **và** số nến đã giao dịch xuyên qua zone trong 20 nến trước khi hình thành ≤ 3 | "Sạch" = zone chưa từng là vùng giằng co; độ rộng quản trị được | Chỉ dùng `ob_width_atr` |
| **"Strong reaction"** | `mfe_atr_N` ≥ 1.5 (N = 12 nến TF) **trước khi** giá đóng ngoài distal; hoặc `bars_to_1atr` ≤ 4 | Đo cả độ lớn và tốc độ, có điều kiện không bị invalidate trước | MFE ≥ 2R; tỷ lệ MFE/MAE |
| **"Fresh OB"** | `touch_count` = 0 kể từ `t_avail` (chạm = extreme giá vào trong 0.05 ATR của proximal) | Định nghĩa nhị phân rõ; tách khỏi `mitigation_count` | Fresh = `mitigation_count` = 0 (cho phép chạm nông) |
| **"HTF aligned"** | `d1_bias` cùng dấu hướng OB **và** `dist_to_dol_R` ≥ R_min | Bias theo quy tắc cấu trúc; DOL theo quy tắc pool gần nhất | Thêm `ob_inside_htf_poi` = true |
| **"Acceptance ngoài OB"** | OB-INVAL v0.1 (§12F) | Sự kiện đo được thay cho cảm giác | N chọn bằng hazard analysis |

### 19.3 Vì sao percentile tốt hơn bội số ATR cố định

- ATR chuẩn hóa theo *biến động gần đây*, nhưng không chuẩn hóa theo **phân bố hình dạng** của displacement ở từng instrument/phiên. 1.5 × ATR trên XAUUSD phiên NY và trên EURUSD phiên Á không cùng "độ hiếm".
- Percentile trả lời trực tiếp câu hỏi có ý nghĩa: **"cú đẩy này hiếm đến mức nào so với các cú đẩy bình thường của chính thị trường này, trong chính phiên này?"**
- **Chống look-ahead:** phân bố percentile chỉ được xây từ dữ liệu **trước** thời điểm đánh giá (rolling window), không dùng toàn bộ tập dữ liệu.

### 19.4 Bộ rule v0.1 — tổng hợp và kiểm soát phiên bản

| Rule | Nội dung tóm tắt | Phiên bản | Trạng thái |
|---|---|---|---|
| **OB-DEF** | Tầng 1 + Tầng 2 (§3.3); đo body + full; `t_avail` | v0.1 | Hypothesis — khóa trước backtest |
| **OB-HIER** | Nguyên lý thừa kế; L1–L4; R-H1…R-H7 (§8.3) | v0.1 | Hypothesis |
| **OB-INVAL** | Structural / N nến / distance / structure-outside / breaker (§12F) | v0.1 | Hypothesis — N chọn bằng hazard analysis |
| **OBQS** | 8 yếu tố × 0–2 điểm, trọng số bằng nhau, cổng cứng (§9.5) | v0.1 | Hypothesis — cần kiểm tra tính đơn điệu |
| **ENTRY-OB** | FVG M5 mặc định; M5 OB khi không có FVG; Plan D | v0.1 | Hypothesis |

> [!note] Quy trình thay đổi rule (theo framework của bạn)
> Mọi thay đổi ghi theo mẫu: **OLD RULE → NEW RULE → REASON FOR CHANGE → EXPECTED EFFECT → BACKTEST REQUIRED?** Không thay đổi rule giữa chừng một đợt backtest. Không thay đổi rule vì một lệnh thua.

---

## 20. Backtesting Methodology — kiểm chứng một cách statistically sound

### 20.1 Vì sao bias đặc biệt nguy hiểm khi backtest khái niệm ICT

1. **Định nghĩa co giãn:** body hay wick, một nến hay chuỗi, MT hay CE, TF nào — mỗi lựa chọn là một "bậc tự do". Người nghiên cứu có thể (vô thức) chọn lại các lựa chọn này *sau khi thấy chart*. Hiện tượng này được gọi là "garden of forking paths" — nhiều nhánh phân tích khả dĩ khiến kết quả "có ý nghĩa" xuất hiện dù không có hiệu ứng thật [^S10].
2. **Narrative giải thích được mọi kết quả:** OB giữ → "OB mạnh"; OB fail → "đó là inducement / breaker / thiếu confluence". Khi mọi kết quả đều có nhãn, không kết quả nào bác bỏ được lý thuyết.
3. **Gán nhãn lại sau sự kiện:** một vùng được gọi là "OB" trước khi giá tới, nhưng được gọi lại là "breaker" sau khi nó fail — nếu log lúc sau, dữ liệu OB chỉ còn những lần thành công.
4. **Tài liệu học được chọn lọc:** chart mẫu là những ví dụ thành công (survivorship) → trader hình thành kỳ vọng win rate quá cao.
5. **Mẫu nhỏ:** backtest thủ công 30–50 lệnh là phổ biến — quá nhỏ để phân biệt edge với may rủi (20.8).
6. **Nhiều tham số, ít dữ liệu:** 8 yếu tố OBQS × nhiều ngưỡng × nhiều entry → rất dễ tìm ra một tổ hợp "hoàn hảo" trong quá khứ. Lịch sử nghiên cứu phân tích kỹ thuật cho thấy những quy tắc tốt nhất trong mẫu thường không giữ được hiệu quả ở giai đoạn ngoài mẫu sau khi điều chỉnh cho data snooping [^S8][^S9].

### 20.2 Câu hỏi nghiên cứu — theo giai đoạn

| Giai đoạn | Câu hỏi | Hypothesis | Nếu thất bại thì sao? |
|---|---|---|---|
| **Q1 — OB effect** | OB (OB-DEF v0.1) có phản ứng mạnh hơn/nhiều hơn vùng đối chứng không? | HYP-OB-001 | Nếu OB ≈ đối chứng: OB không mang thông tin riêng → dùng OB chỉ như công cụ hình học (stop/location), không kỳ vọng "sức hút" |
| **Q2 — Features** | Đặc trưng nào (sweep, FVG, cấp, P/D, HTF, freshness…) làm tăng E[R]? | HYP-OB-002…012 | Bỏ các confluence không có đóng góp → hệ thống đơn giản hơn, nhiều mẫu hơn |
| **Q3 — Execution** | Entry/stop/invalidation nào tối ưu (sau chi phí)? | HYP-OB-007, 013, 015, 016 | Chọn phương án đơn giản nhất không kém hơn có ý nghĩa |
| **Q4 — Robustness** | Kết quả có giữ ngoài mẫu, qua instrument, qua regime không? | Tất cả | Kết quả chỉ tồn tại in-sample = overfitting |
| **Q5 — Forward** | Demo/forward test có khớp với backtest không? | Tất cả | Chênh lệch lớn = lỗi thực thi hoặc bias trong backtest |

### 20.3 Dataset

| Thành phần | Thiết kế |
|---|---|
| **Instrument** | NQ1 (hoặc NAS100 CFD — chọn **một** nguồn và giữ nguyên), EURUSD, GBPUSD, XAUUSD — khớp với danh mục trong vault |
| **Timeframe** | D1 (context), H1 (OB phát hiện + setup), M5 (execution) — mỗi TF là một quần thể riêng |
| **Giai đoạn** | Tối thiểu 2–3 năm, phủ nhiều regime (trending mạnh, sideway, biến động cao/thấp). Chia theo **thời gian**: ~60% in-sample, ~20% validation, ~20% out-of-sample **không được nhìn** cho đến bước cuối |
| **Session** | Gắn nhãn Asia / London / NY AM / NY PM theo giờ New York (có xử lý DST); vault dùng UTC+7 — quy đổi nhất quán |
| **Regime** | Gắn nhãn bằng biến đo được (ví dụ ATR D1 percentile, efficiency ratio) — không gắn nhãn bằng mắt |
| **Tin tức** | Lịch tin high-impact có timestamp; khai báo trước: loại bỏ hay phân tích riêng |
| **Feed** | Một feed cố định; ghi lại giờ server/nến D1 (vấn đề nến Chủ nhật) |

### 20.4 Hai track song song

**Track 1 — Mechanical (code trên OHLC):** trả lời Q1, Q2 và phần lớn Q3. Ưu điểm: hàng nghìn sự kiện, không có discretion, không có hindsight. Nhược điểm: bias D1 và DOL phải được quy tắc hóa (thô hơn phán đoán thật). Đây là track **duy nhất** đủ mẫu để trả lời các câu hỏi về features (xem 20.8).

**Track 2 — Discretionary replay (2022 Model đầy đủ):** trả lời "khi tôi áp dụng toàn bộ quy trình, kết quả ra sao?" Bắt buộc:
- **Pre-registration:** khóa OB-DEF, entry, stop, target, invalidation **trước**.
- **Blind replay:** dùng bar replay, không nhìn phía phải; chọn ngày ngẫu nhiên (không chọn ngày "nhớ là đẹp").
- **Log mọi ứng viên**, kể cả setup bị bỏ qua, kèm lý do bỏ qua — tại thời điểm quyết định, không phải sau.
- **Screenshot có timestamp** tại `t_avail` và tại quyết định entry.

### 20.5 Thiết kế đối chứng (control) — phần hay bị bỏ qua nhất

Không có đối chứng, "OB phản ứng 60% số lần" **không có nghĩa gì** — vì một mức giá bất kỳ cũng có một tỷ lệ "phản ứng" nào đó (trong nghiên cứu của Garzarelli và cộng sự, chuỗi xáo trộn cho xác suất bật ≈ 0.5 theo định nghĩa của họ [^S4]). Bốn loại đối chứng:

| Đối chứng | Cách tạo | Trả lời câu hỏi |
|---|---|---|
| **C1 — Vùng ngẫu nhiên khớp điều kiện** | Với mỗi OB retest, tạo vùng cùng độ rộng, cùng khoảng cách tới giá tại thời điểm retest, ở vị trí ngẫu nhiên | OB có hơn một vùng bất kỳ ở cùng khoảng cách không? |
| **C2 — Displacement không BOS** | Candidate Tầng 1 không đạt Tầng 2 (EC-03) | Điều kiện BOS có tạo giá trị không? |
| **C3 — Vùng giữa leg** | Vùng ở điểm giữa leg displacement, cùng độ rộng OB | "Gốc" có đặc biệt hơn "đường đi" không? |
| **C4 — OB dịch chuyển** | Dịch zone OB lên/xuống ±0.5 ATR | Vị trí chính xác của OB có quan trọng không, hay chỉ "vùng lân cận"? |

### 20.6 Định nghĩa sự kiện

- **Formation event:** OB thỏa OB-DEF v0.1, ghi tại `t_avail`.
- **Retest event:** lần đầu tiên sau `t_avail` giá vào vùng ảnh hưởng (proximal + 0.25 ATR_TF), **sau khi đã đi xa ≥ 1 ATR_TF** khỏi proximal (để không đếm dao động sát ngay sau hình thành).
- **Một OB → một first-retest event** cho phân tích chính. Các retest sau phân tích riêng (HYP-OB-006) — không trộn, vì các retest của cùng một OB không độc lập với nhau.
- **Cửa sổ phản ứng:** N nến TF (N = 12, HEURISTIC; kiểm tra độ nhạy với N = 6, 24).
- **Không có retest trong M nến (ví dụ 200 nến H1):** ghi `retested = false` — cần cho phân tích `P(retest)`.

### 20.7 Entry / Stop / Target — biến thể khai báo trước

| Thành phần | Biến thể | Ghi chú |
|---|---|---|
| **Entry** | proximal limit · MT limit · CE limit · open limit · M5 FVG sau MSS (confirmation) · market sau reclaim (Plan D) | Limit chỉ tính khớp khi giá **giao dịch xuyên qua** ít nhất 1 tick (với FX, chart là giá bid → lệnh buy limit cần cộng spread) |
| **Stop** | distal − k × ATR_TF (k = 0.1 / 0.25 / 0.5) · dưới sweep low · dưới swing M5 | Stop qua vùng cascade có thể **trượt giá** [^S2] — mô hình hóa slippage lớn hơn cho stop |
| **Target** | 2R · 3R · IRL gần nhất · DOL · partial (T1 IRL + runner DOL) | Target theo thanh khoản phải được xác định **tại thời điểm entry** |
| **Quản trị** | BE sau T1? Có/không — khai báo trước | Dời stop là biến số, không phải cảm hứng |

> [!warning] Lưới biến thể = multiple testing
> 6 entry × 3 stop × 5 target = **90 biến thể**. Nếu chọn biến thể tốt nhất in-sample rồi báo cáo kết quả đó, bạn gần như chắc chắn đang báo cáo may rủi. Đếm số biến thể đã thử, ghi lại tất cả, và đánh giá biến thể được chọn **trên out-of-sample**. Có thể ước lượng xác suất backtest bị overfit bằng phương pháp CSCV/PBO [^S7].

### 20.8 Metrics và cỡ mẫu — những con số khiến 30 mẫu trở nên vô nghĩa

**Metrics tối thiểu:** win rate · expectancy E[R] · average R · median R · profit factor · MAE/MFE (theo R và ATR) · max drawdown (theo R) · phân bố chuỗi thua · time in trade · setup frequency (lệnh/tuần) · fill rate & `missed_trade_rate` · **tổng R kỳ vọng mỗi tuần = E[R] × tần suất**.

**Khoảng tin cậy 95% (Wilson) của win rate khi win rate quan sát = 50%:**

| n | Khoảng tin cậy |
|---|---|
| 20 | 30% – 70% |
| 30 | 33% – 67% |
| 50 | 37% – 63% |
| 100 | 40% – 60% |
| 200 | 43% – 57% |
| 400 | 45% – 55% |

**Expectancy:** giả sử một chiến lược thắng 40% với target 2R, thua −1R → E[R] = +0.2R, độ lệch chuẩn ≈ 1.47R. Khoảng tin cậy 95% của E[R]:

| n | Khoảng tin cậy E[R] | Diễn giải |
|---|---|---|
| 30 | −0.33R … +0.73R | Không phân biệt được với chiến lược lỗ |
| 50 | −0.21R … +0.61R | Vẫn không |
| 100 | −0.09R … +0.49R | Vẫn chứa 0 |
| 200 | ≈ 0.00R … +0.40R | Chạm ngưỡng |
| 400 | +0.06R … +0.34R | Bắt đầu tin được là dương |

Để có 80% power phát hiện E[R] = +0.2R (hai phía, α = 5%) cần khoảng **420 lệnh**. Để phát hiện chênh lệch win rate 50% vs 40% giữa hai nhóm (ví dụ OB có sweep vs không sweep) cần khoảng **390 mẫu mỗi nhóm**. (Các con số tính theo công thức chuẩn; giả định trên là minh họa, không phải kết quả của bạn.)

> [!important] Hệ quả thực tế cho lộ trình của bạn
> Với backtest thủ công (Track 2), bạn thực tế chỉ trả lời được **2–3 câu hỏi lớn** (ví dụ "toàn bộ quy trình 2022 Model của tôi có E[R] dương không?"). Các câu hỏi về từng feature (sweep, FVG, freshness…) **cần Track 1**. Đừng kết luận "OB có FVG tốt hơn" từ 40 lệnh.

**Chuỗi thua — liên quan trực tiếp tới prop firm:** với win rate 40%, trong 100 lệnh, xác suất gặp ít nhất một chuỗi **≥ 6 lệnh thua liên tiếp** ≈ **87%**; chuỗi **≥ 8** ≈ **49%** (mô phỏng Monte Carlo, giả định các lệnh độc lập). Với risk 0.5%/lệnh, chuỗi 8 lệnh thua = −4% — phải nằm trong giới hạn drawdown của FTMO và The5ers với biên an toàn. Đây là lý do phân bố chuỗi thua quan trọng không kém win rate.

### 20.9 Kiểm soát bias — bảng tổng hợp

| Bias | Cách nó lẻn vào backtest OB | Biện pháp kiểm soát |
|---|---|---|
| **Look-ahead** | Dùng swing chưa được xác nhận (fractal cần n nến bên phải); dùng OB trước `t_avail`; dùng nến D1 chưa đóng; dùng range re-map bằng đỉnh chưa hình thành; percentile tính trên toàn bộ dữ liệu | Mọi biến gắn timestamp; chỉ dùng dữ liệu ≤ thời điểm quyết định; swing detector có độ trễ tường minh; rolling percentile |
| **Hindsight** | Chọn OB sau khi thấy giá phản ứng; gán nhãn lại (OB → breaker/inducement) sau sự kiện | Phân loại OB (cấp, Plan A/B/D) **cam kết tại `t_avail`**; screenshot timestamp |
| **Survivorship** | Chỉ log setup nhớ được / đẹp; chỉ chọn giai đoạn thị trường trending; bỏ ngày dữ liệu lỗi có lợi | Chọn ngày ngẫu nhiên; log toàn bộ ứng viên; ghi rõ dữ liệu bị loại và lý do |
| **Selection** | Discretion bỏ qua setup "trông xấu" — và tiêu chí "xấu" trôi theo kết quả gần đây | Ghi lý do bỏ qua tại thời điểm quyết định; sau này so kết quả giả định của các setup bị bỏ qua với setup được vào |
| **Discretionary selection** | Người backtest biết (hoặc lờ mờ nhớ) ngày đó giá đi đâu | Blind replay; ngày ngẫu nhiên; ẩn ngày tháng nếu có thể |
| **Overfitting** | Tinh chỉnh ngưỡng (ATR, percentile, N nến) cho tới khi đẹp | Khóa rule trước; chia IS/validation/OOS theo thời gian; walk-forward; PBO [^S7] |
| **Multiple testing** | Thử 20 feature ở mức ý nghĩa 5% → xác suất có ít nhất một "phát hiện giả" ≈ **64%** (40 feature: ≈ 87%) | Đếm số phép thử; hiệu chỉnh (Holm, Benjamini–Hochberg); kiểm định kiểu Reality Check [^S9]; ưu tiên ít giả thuyết, định trước |

### 20.10 Độ tin cậy giữa người đánh dấu (inter-rater reliability)

Trước khi hỏi "OB có hoạt động không", hãy hỏi "**OB có được nhận diện nhất quán không**":
- Lấy 50 chart ngẫu nhiên. Bạn đánh dấu OB theo OB-DEF v0.1 hai lần, cách nhau ≥ 1 tuần, không xem lại lần đầu (hoặc nhờ một người khác đánh dấu độc lập).
- Đo mức độ đồng thuận (ví dụ Cohen's kappa cho "có/không phải OB", và độ lệch biên theo ATR).
- Nếu đồng thuận thấp → **định nghĩa chưa đủ khách quan**; sửa định nghĩa trước khi đo kết quả. Không có bước này, backtest discretionary đo "tâm trạng của người vẽ" chứ không đo OB.

### 20.11 Kế hoạch phân tích (định trước)

1. **Mô tả:** số OB theo TF/instrument/phiên; `P(retest)`; phân bố `penetration`.
2. **Q1:** so sánh `mfe_atr_N` và tỷ lệ "strong reaction" giữa OB và C1–C4 (khoảng tin cậy bootstrap).
3. **Q2:** phân tích đơn biến từng feature (có khoảng tin cậy) → chỉ những feature có hiệu ứng rõ mới đưa vào mô hình đa biến nhỏ. Quy tắc kinh nghiệm (HEURISTIC): khoảng ≥ 10 sự kiện kết quả cho mỗi biến trong mô hình hồi quy logistic.
4. **Kiểm tra OBQS:** E[R] theo nhóm A/B/C — có đơn điệu không?
5. **Q3:** so sánh biến thể entry/stop/target — báo cáo **tất cả**, chọn trên validation, xác nhận trên OOS.
6. **Q4:** OOS + từng instrument + từng regime. Kết quả chỉ tồn tại ở một instrument/regime → ghi rõ phạm vi.
7. **Q5:** forward test demo với đúng rule đã chốt.

---

## 21. What We Actually Know vs What We Assume

### 21.1 Thang bằng chứng

| Mức | Mệnh đề | Cơ sở |
|---|---|---|
| **Biết chắc (cơ chế)** | Giá dịch chuyển khi lệnh chủ động tiêu thụ lệnh limit; stop order biến thành lệnh market khi kích hoạt; FX spot là OTC, không có sổ lệnh hợp nhất | Cơ chế thị trường |
| **Có bằng chứng lân cận** | Stop tụ sau mức hiển nhiên, take-profit tụ tại mức đó; stop kích hoạt gây tăng tốc kéo dài hàng giờ [^S1][^S2] | FX, số tròn, dữ liệu lệnh một ngân hàng |
| | Mức S/R trùng với đỉnh độ sâu sổ lệnh [^S3] | Cổ phiếu |
| | Giá bật nhiều hơn xuyên tại mức S/R được phát hiện; nhiều lần bật trước → bật dễ hơn [^S4]; xác suất bật giảm theo thời gian [^S5] | Cổ phiếu, thang giây–phút; [^S5] là preprint |
| | Tác động giá hồi lại một phần sau khi metaorder kết thúc [^S6] | Cổ phiếu Mỹ, dữ liệu tổ chức |
| | Hiệu quả quy tắc kỹ thuật bị thổi phồng bởi data snooping; overfitting backtest đo được [^S7][^S8][^S9] | Tài chính định lượng |
| **Hợp lý nhưng không quan sát được** | Metaorder dở dang ở OB; trader bị kẹt thoát hòa vốn; displacement là sponsored hay cascade | Suy luận từ cơ chế |
| **Chưa biết (riêng cho OB)** | OB có hơn vùng đối chứng không; feature nào có giá trị; CE có đặc biệt không; freshness theo chiều nào; N nến invalidation | **Chưa có nghiên cứu công khai đạt chuẩn — cần dữ liệu của chính bạn** |
| **Narrative không bác bỏ được (ở dạng hiện tại)** | "Smart money đặt lệnh ở OB", "thuật toán quay lại để mitigate", "thị trường tạo OB giả để bẫy trader ICT" | Ý định không quan sát được |

### 21.2 Phản biện các giả định — Assumption → Problem → Alternative → Implication → How to test

**CT-1 — "Trong nhiều OB, có một OB 'đúng' có thể xác định trước."**
- *Problem:* giả định sự bất định có thể loại bỏ bằng phân tích. Thực tế, với nhiều ứng viên, sự mơ hồ trước sự kiện có thể là **không thể giảm** — và sau sự kiện luôn có một OB "đúng" (§14.3).
- *Alternative:* chọn lọc = lọc + kế hoạch có điều kiện; "OB đúng" được **tiết lộ** bởi bằng chứng M5, không được **dự đoán** bởi phân tích.
- *Implication:* đánh giá chất lượng *kế hoạch*, không đánh giá độ chính xác *dự đoán*.
- *Test:* so sánh E[R] và tần suất của (a) chiến lược chọn trước một OB duy nhất vs (b) Plan A/B có điều kiện + M5 confirmation.

**CT-2 — "Sweep + OB + displacement + FVG + MSS = 5 confluence."**
- *Problem:* FVG, MSS và độ mạnh displacement đều là **hệ quả của cùng một sự kiện** (displacement). Chúng tương quan chặt với nhau. Đếm chúng như 5 bằng chứng độc lập là **"lạm phát confluence"** — cảm giác chắc chắn tăng nhanh hơn lượng thông tin thật.
- *Alternative:* về thông tin, có thể chỉ có 2–3 mảnh độc lập: (1) cú mất cân bằng mạnh đến đâu, (2) thanh khoản nào đã bị lấy, (3) context HTF.
- *Implication:* OBQS v0.1 có thể đang tính trùng. Một setup "5/5 confluence" có thể không tốt hơn setup "3/5" nếu 2 cái thiếu là hệ quả của cái đã có.
- *Test:* ma trận tương quan giữa các feature; kiểm tra **giá trị gia tăng có điều kiện** — FVG có thêm thông tin khi đã biết `disp_pctile` không?

**CT-3 — "Giá phản ứng tại OB chứng tỏ OB có giá trị."**
- *Problem:* phản ứng ≠ dự đoán. Giá phản ứng ở mọi nơi đôi khi; impact reversion (M2) khiến việc giá quay về gần gốc là mặc định.
- *Alternative:* M2 + M6.
- *Implication:* ví dụ OB phản ứng đẹp không phải bằng chứng.
- *Test:* HYP-OB-001 với đối chứng C1–C4.

**CT-4 — "OB khung lớn quan trọng hơn OB khung nhỏ."**
- *Problem:* nhiễu bởi độ rộng (zone rộng dễ "trúng") và stop rộng (khó bị quét).
- *Alternative:* sau khi chuẩn hóa theo độ rộng và R, khác biệt có thể nhỏ hơn nhiều.
- *Implication:* đừng so "tỷ lệ giữ giá" giữa các cấp mà không chuẩn hóa.
- *Test:* so E[R] (theo R) và phản ứng theo ATR giữa các cấp, kiểm soát `ob_width_atr`.

**CT-5 — "OB fresh mạnh hơn OB đã chạm."**
- *Problem:* có bằng chứng S/R lân cận theo chiều ngược lại [^S4][^S5]; và nhiều lần chạm tạo equal lows = thanh khoản (EC-19).
- *Alternative:* quan hệ có thể phi tuyến: chạm nông lần 2 tốt, lần 4+ xấu (thanh khoản tích tụ).
- *Implication:* không loại OB đã chạm chỉ vì "không còn fresh" cho đến khi có dữ liệu.
- *Test:* HYP-OB-006, phân tích theo `touch_count` và `mitigation_count` riêng.

**CT-6 — "D1 context cải thiện kết quả của execution M5."**
- *Problem:* đây là **tiền đề của chính framework** nhưng chưa được bạn kiểm chứng. Thêm vào đó, nếu D1 bias được xác định bằng phán đoán, có rủi ro vòng tròn: bias được "đọc" sau khi đã thấy ngày đó giá đi đâu.
- *Alternative:* D1 alignment có thể cải thiện win rate nhưng giảm tần suất đến mức tổng R/tuần không đổi.
- *Implication:* nếu không được kiểm chứng, kiến trúc D1 → H1 → M5 là một niềm tin, không phải edge.
- *Test:* HYP-OB-010 với D1 bias **theo quy tắc** (hướng BOS D1 gần nhất + protected swing), so sánh setup M5 cùng hướng vs ngược hướng.

### 21.3 Hypothesis Register — OB

| ID | Hypothesis | Biến chính | Test / Điều kiện bác bỏ | Status |
|---|---|---|---|---|
| **HYP-OB-001** | OB (OB-DEF v0.1) có phản ứng mạnh hơn vùng đối chứng cùng độ rộng, cùng khoảng cách | `mfe_atr_N`, nhóm OB vs C1–C4 | Bác bỏ nếu khoảng tin cậy chênh lệch chứa 0 trên OOS | UNTESTED |
| **HYP-OB-002** | Độ mạnh displacement (percentile) có quan hệ đơn điệu với E[R] khi retest | `disp_pctile` | Bác bỏ nếu không đơn điệu qua các nhóm percentile | UNTESTED |
| **HYP-OB-003** | OB có sweep mức ≥ L2 trước khi hình thành cho E[R] cao hơn OB không sweep | `sweep_prior`, `swept_level_class` | Bác bỏ nếu chênh lệch không có ý nghĩa với cỡ mẫu đủ power | UNTESTED |
| **HYP-OB-004** | OB có FVG cho E[R] cao hơn OB không FVG, **kể cả khi kiểm soát `disp_pctile`** | `fvg_present`, `fvg_size_atr` | Bác bỏ nếu hiệu ứng biến mất khi kiểm soát displacement | UNTESTED |
| **HYP-OB-005** | OB cấp L3+ > L2 > L1 về E[R] (theo R, kiểm soát độ rộng) | `broken_swing_level` | Bác bỏ nếu thứ tự không giữ sau chuẩn hóa | UNTESTED |
| **HYP-OB-006** | Số lần chạm/mitigation trước ảnh hưởng tới phản ứng — **chiều chưa biết** (ICT: giảm; S/R: tăng) | `touch_count`, `mitigation_count` | Kiểm định hai phía; báo cáo chiều và hình dạng | UNTESTED |
| **HYP-OB-007** | Các mức entry (proximal/MT/CE/open) cho E[R] khác nhau; mức 50% **không** có mật độ quay đầu vượt trội | `penetration`, `entry_level` | Bác bỏ "CE không đặc biệt" nếu có đỉnh mật độ ở 0.5 vượt đối chứng | UNTESTED |
| **HYP-OB-008** | `pd_pos` có quan hệ đơn điệu với E[R]; range re-map dự đoán tốt hơn range cũ | `pd_pos_h1`, `pd_pos_d1` (cũ và mới) | Bác bỏ nếu không đơn điệu / range cũ tốt hơn | UNTESTED |
| **HYP-OB-009** | Phản ứng suy giảm theo tuổi OB, sau khi kiểm soát supersession | `age_bars`, `still_structural` | Bác bỏ nếu không có xu hướng khi `still_structural` = true | UNTESTED |
| **HYP-OB-010** | Setup M5 cùng hướng D1 bias (theo quy tắc) có E[R] và tổng R/tuần cao hơn ngược hướng | `d1_bias` | Bác bỏ nếu không khác biệt → xem lại kiến trúc framework | UNTESTED |
| **HYP-OB-011** | OB "unprotected" (pool chưa quét ≤ 0.5 ATR dưới distal): entry proximal có E[R] thấp hơn; Plan D cải thiện E[R] | `unprotected`, `entry_level`, `plan` | Bác bỏ nếu không khác biệt | UNTESTED |
| **HYP-OB-012** | Retest trong kill zone cho E[R] cao hơn ngoài kill zone | `session_retest` | Bác bỏ nếu không khác biệt | UNTESTED |
| **HYP-OB-013** | Sau M5 MSS: entry FVG vs entry OB — so **tổng R** (E[R] × fill rate) | `entry_array`, `missed_trade_rate` | Báo cáo cả hai; chọn đơn giản hơn nếu tương đương | UNTESTED |
| **HYP-OB-014** | OB nông nhất trong chuỗi bị xuyên thường xuyên hơn structural OB (inducement) | `ob_order_in_leg`, `broken_swing_level` | Bác bỏ nếu tỷ lệ xuyên không khác biệt | UNTESTED |
| **HYP-OB-015** | Sweep distal nông (≤ 0.5 ATR) + reclaim trong 1 nến TF OB cho E[R] cao hơn retest không sweep | `distal_swept`, `sweep_depth_beyond_distal_atr`, `reclaim_bars` | Bác bỏ nếu không khác biệt | UNTESTED |
| **HYP-OB-016** | Đường cong hazard reclaim theo số nến đóng ngoài có "khuỷu" ổn định qua instrument/TF | `closes_outside_n` | Bác bỏ nếu N tối ưu không ổn định → dùng invalidation structural/distance | UNTESTED |

---

## 22. Final Mental Model

> [!summary] OB trong 7 dòng
> 1. **OB = địa chỉ gốc của một cú mất cân bằng đo được.** Không phải kho lệnh, không phải tín hiệu.
> 2. **Ý nghĩa của OB = ý nghĩa của swing nó sinh ra.** Xếp hạng swing trước, OB sau.
> 3. **Nhiều OB là bình thường.** Lọc bằng context → range → cấp → tiêu thụ → thanh khoản → DOL; còn nhiều hơn một thì lập kế hoạch có điều kiện, không đoán.
> 4. **OB là location. MSS/displacement là evidence. Entry là rule.** Ba thứ, ba câu hỏi, ba lần kiểm chứng.
> 5. **Giá trị chắc chắn nhất của structural OB là hình học rủi ro:** điểm vào gần điểm luận điểm sai.
> 6. **Râu không giết OB; acceptance mới giết.** Acceptance phải được định nghĩa bằng sự kiện đo được, không bằng "3 nến" cảm tính.
> 7. **Mọi "OB loại X tốt hơn" là giả thuyết** cho đến khi dữ liệu của chính bạn — có đối chứng, đủ mẫu, ngoài mẫu — nói khác.

**Công thức ra quyết định (nhân, không cộng):**

$$\text{Trade} = \text{Location}_{OB} \times \text{Context}_{D1/H1} \times \text{Evidence}_{M5} \times \text{Invalidation}_{structure} \times \text{Room}_{DOL}$$

Bất kỳ thừa số nào bằng 0 → **không có lệnh**, bất kể các thừa số khác đẹp đến đâu. Confluence không bù trừ cho nhau.

---

## Câu hỏi tự kiểm tra

1. Nếu chỉ được giữ hai điều kiện trong định nghĩa OB, bạn giữ gì và vì sao sweep/FVG không nằm trong đó?
2. Vì sao "giá đã quay về OB" không phải bằng chứng OB có sức hút? (Gợi ý: M2.)
3. Trong một uptrend với OB₁…OB₅, OB nào là structural và điều gì xảy ra với nó sau BOS mới?
4. Phân biệt Scenario D và Scenario E bằng dữ liệu nào?
5. Vì sao "3 nến" không phải rule, và bạn sẽ chọn N bằng cách nào?
6. Vì sao cần vùng đối chứng khi backtest OB?
7. Với win rate 50% sau 30 lệnh, khoảng tin cậy 95% là bao nhiêu? Bạn kết luận được gì?
8. "5 confluence" có thể chỉ là mấy mảnh thông tin độc lập? Vì sao?

## Flashcards

**Q1:** OB được "xác nhận" tại thời điểm nào, và vì sao điều đó quan trọng cho backtest?
**A1:** Tại `t_avail` — khi nến xác nhận BOS/MSS đóng cửa. Dùng OB trước thời điểm đó là look-ahead.

**Q2:** Cấp của một bullish OB được quyết định bởi gì?
**A2:** Bởi cấp của swing high mà displacement từ OB phá vỡ (nguyên lý thừa kế) — không phải kích thước nến.

**Q3:** OB "unprotected" là gì và xử lý thế nào?
**A3:** OB có pool thanh khoản chưa quét ngay dưới distal. Không đặt limit proximal; dùng Plan D (chờ sweep + reclaim + M5 MSS).

**Q4:** Mâu thuẫn chính giữa ICT và bằng chứng S/R về freshness?
**A4:** ICT: mỗi lần chạm làm OB yếu đi. Nghiên cứu S/R: mức có nhiều lần bật trước đó dễ bật hơn. → HYP-OB-006, kiểm định hai phía.

**Q5:** Ba lớp invalidation cần viết riêng là gì?
**A5:** Trade stop (M5), setup invalidation (H1 OB theo OB-INVAL), bias invalidation (protected swing D1).

**Q6:** Vì sao percentile tốt hơn bội số ATR cố định để đo displacement?
**A6:** Percentile đo "độ hiếm" so với chính instrument × phiên, tránh ảo giác ATR bị nén (CX2); phải tính rolling để không look-ahead.

---

## Final Quality Test (tự kiểm tra theo yêu cầu nghiên cứu)

| # | Câu hỏi | Trả lời | Ở đâu |
|---|---|---|---|
| 1 | Đã giải thích OB cho beginner chưa? | Có — phép so sánh đấu giá, bảng thuật ngữ nền | §2.1–2.2 |
| 2 | Có đạt expert depth? | Cơ chế M1–M6 với dấu vết thống kê phân biệt; phân cấp; lượng hóa; thiết kế backtest có đối chứng và power | §4.3, §8, §19, §20 |
| 3 | Phân biệt ICT narrative với market mechanics? | Có — nhãn xuyên suốt; bảng đối chiếu | §5.2, §6, §21.1 |
| 4 | Giải quyết "quá nhiều OB"? | Nguyên lý thừa kế + 8 cổng + kế hoạch có điều kiện + OBQS | §8.1, §9 |
| 5 | Khi nào KHÔNG dùng OB? | Cổng G0–G5, R-H5 (noise), EC-11/15/17/22, CX1–CX3 | §9.3, §8.3, §13, §17 |
| 6 | Edge cases? | 24 trường hợp theo 5 bước | §13 |
| 7 | Counterexamples? | 3 counterexamples + phép tính độ phủ | §14.3, §17 |
| 8 | Tránh hindsight? | Dòng thời gian T0–T5; `t_avail`; kết quả ví dụ cố ý bỏ trống | §2.3, §15 B1, §20.9 |
| 9 | Chuyển subjective → measurable? | Bảng 7 khái niệm | §19.2 |
| 10 | Framework backtest được? | Q1–Q5, đối chứng C1–C4, sự kiện, metrics, cỡ mẫu | §20 |
| 11 | Chỉ ra assumptions cần validation? | 16 hypotheses + 6 phản biện | §21.2–21.3 |
| 12 | Tránh trình bày hypothesis như fact? | Mọi ngưỡng HEURISTIC; audit note cũ | Toàn bài, Phụ lục A |

---

## Phụ lục A — Audit [[25-OB-Order-Block]]: những mệnh đề nên hạ cấp

Note 25 là nền tảng tốt, nhưng một số mệnh đề đang được trình bày như fact trong khi chỉ là heuristic/hypothesis, và có vài điểm không nhất quán. **Note này không sửa note 25** — danh sách dưới đây là đề xuất để bạn quyết định.

| # | Vị trí trong note 25 | Mệnh đề | Vấn đề | Đề xuất |
|---|---|---|---|---|
| 1 | §7.1 | "CE / Mean Threshold = mốc 50% của CẢ cây nến (tính râu)" | Nhiều nguồn ICT thứ cấp đo MT trên **thân**; CE thường là thuật ngữ cho FVG/râu. Hai mức khác nhau | Định nghĩa riêng `mt_body` và `ce_range`; ghi rõ dùng cái nào |
| 2 | §7.1, §7.2 | "Phản ứng mạnh và đáng tin nhất thường xảy ra quanh mốc 50%"; kịch bản B "xác suất cao" | Chưa có bằng chứng | Gắn [HYPOTHESIS] → HYP-OB-007 |
| 3 | §7.2 | "First touch mạnh hơn second touch… vì thanh khoản dần cạn" | Bằng chứng S/R lân cận theo chiều ngược lại | [HYPOTHESIS] hai phía → HYP-OB-006 |
| 4 | §7.4 | "Thuật toán thường trả giá về đúng open đó" | Narrative; với nến giảm, open = đỉnh thân (mép proximal body) | [ICT FRAMEWORK]; đo như một mức entry trong HYP-OB-007 |
| 5 | §7.4 | "Thời gian giá ở trong OB tỉ lệ nghịch với chất lượng phản ứng" | Hợp lý nhưng chưa đo | [HYPOTHESIS]; biến `time_in_zone_bars` |
| 6 | §7.5 (5) | "N nến (vd 3 nến M5) bên trong OB" | HEURISTIC; lệch TF nếu OB là H1 | Quy đổi theo TF OB; chọn N bằng dữ liệu |
| 7 | §16.2 | "38–79% theo Fibonacci, hoặc 1 × ATR" | Con số không có nguồn | Bỏ hoặc gắn nguồn; ý "mean reversion" giữ lại, dẫn [^S6] |
| 8 | §16.5 | Bảng stop-distance điển hình; "BTC ở vùng 60–70k" | Minh họa, dễ lỗi thời | Thay bằng thống kê từ log của chính bạn |
| 9 | §17.2 | "Hai người áp dụng… gần giống nhau trên 80–90% trường hợp" | Con số không có nguồn | Đo bằng inter-rater test (§20.10) |
| 10 | §14–§15 | Các kết quả cụ thể (ví dụ "+4.1R", "R:R 18.8") | Không xác minh được từ note | Nếu là trade/backtest thật → link note gốc; nếu dựng → gắn nhãn "synthetic" |
| 11 | Frontmatter | `common_mistakes` trỏ tới `[[Mistake - Trade Every Order Block]]`… | Các note này không tồn tại trong `06 - Mistake Database/` | Relink tới note hiện có (ví dụ [[08-Mistake-Weak-Displacement]]) hoặc tạo note mới |
| 12 | Frontmatter | `status: tested` | Chưa có tiêu chí "tested" | Định nghĩa: ví dụ ≥ N backtest đã log theo OB-DEF đã khóa |
| 13 | §1 vs §3 | §1: OB "bắt buộc có narrative: liquidity bị quét → …"; §3: sweep nằm ở "điều kiện tăng xác suất" | Không nhất quán về việc sweep có bắt buộc không | Thống nhất theo Tầng 1/2/3 (§3.2 note này) |

## Phụ lục B — Trường dữ liệu đề xuất cho backtest (bổ sung, không thay template)

Template backtest hiện có các trường liên quan: `poi_type`, `liquidity_swept`, `displacement`, `mss`, `fvg_valid`, `entry_type`, `rr_if_ce`. Để trả lời các HYP-OB, đề xuất **thêm** (không đổi tên trường cũ để không làm hỏng dashboard):

```yaml
ob_def_version: "OB-DEF v0.1"
ob_tf: H1                 # TF phát hiện OB
ob_level: L3              # L1 | L2 | L3 | L4
ob_zone_basis: full       # full | body
ob_width_atr:
disp_pctile:
fvg_present:
sweep_prior:
swept_level_class:        # L1..L5
pd_pos_h1:
pd_pos_d1:
unprotected:              # true nếu có pool chưa quét ≤ 0.5 ATR dưới distal
touch_count:
penetration:              # 0 = proximal, 1 = distal
scenario:                 # A | B | C | D | E | F
plan:                     # A | B | D
entry_array:              # FVG | OB | reclaim
entry_level:              # proximal | MT | CE | open | FVG-CE | FVG-edge
obqs:
obqs_grade:               # A | B | C
t_avail:
dist_to_dol_R:
missed:                   # true nếu setup đạt chuẩn nhưng lệnh không khớp
mfe_R:
mae_R:
```

> [!tip] Bước tiếp theo đề xuất
> (1) Khóa OB-DEF v0.1 và chạy inter-rater test trên 50 chart. (2) Bắt đầu Track 1 (code) cho HYP-OB-001 — câu hỏi nền tảng. (3) Song song, tiếp tục Track 2 với các trường Phụ lục B để tích lũy mẫu cho HYP-OB-010/011/013.

---

## Liên kết liên quan

- Nền tảng: [[25-OB-Order-Block]] · [[51-OB-Mitigation-Depth-Vi-sao-Shallow-CE-hay-Full-khac-nhau]] · [[44-Hidden-Order-Block]]
- Họ block: [[04-Breaker-Block]] · [[22-Mitigation-Block]] · [[28-Rejection-Block]] · [[34-Vacuum-Block]]
- Displacement & cấu trúc: [[50-Displacement-In-Depth]] · [[35-Aggressive-Displacement-Entry]] · [[21-Market-Structure-Shift]] · [[05-BOS-Break-of-Structure]] · [[41-Change-in-State-of-Delivery]] · [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]
- Swing & định lượng: [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] · [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]
- Range & vị trí: [[12-Dealing-Range]] · [[37-Re-mapping-Dealing-Range-sau-Displacement]] · [[27-Premium-Discount]] · [[10-Consequent-Encroachment-Mean-Threshold]]
- Thanh khoản & bias: [[19-Liquidity]] · [[19-Liquidity#7. Buy-Side Liquidity (BSL)|Buy-side Liquidity]] · [[19-Liquidity#8. Sell-Side Liquidity (SSL)|Sell-side Liquidity]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[20-Liquidity-Sweep]] · [[15-Inducement]] · [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] · [[59-Daily-Bias]] · [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]
- FVG & thời gian: [[13-FVG-Fair-Value-Gap]] · [[18-Kill-Zones]] · [[32-Top-down-Analysis-Multiple-Timeframes]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]]
- Model: [[01 - ICT 2022 Model]]
- Mistakes: [[08-Mistake-Weak-Displacement]] · [[02-Mistake-Enter-before-liquidity-sweep]] · [[03-Mistake-Entry-When-MSS-not-in-POI-Zone]] · [[09-Mistake-Wrong-daily-bias]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[12-Mistake-Log-Data-Mismatch-Backtest]]

---

## Nguồn

> Ghi chú về nguồn: Tier 1–2 (học thuật) được dùng cho **cơ chế thị trường lân cận**; không nguồn học thuật nào kiểm định trực tiếp ICT Order Block. Định nghĩa ICT được lấy từ nguồn thứ cấp (Tier 3–4) vì note này chưa đối chiếu được video mentorship gốc — coi là "cách thường được trích dẫn", không phải trích nguyên văn đã xác minh.

[^S1]: Osler, C. L. (2003). *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.* Journal of Finance, 58(5), 1791–1819. https://doi.org/10.1111/1540-6261.00588 — take-profit tụ tại số tròn; stop-loss tụ ngay sau số tròn; giải thích dự đoán "đảo chiều tại S/R" và "tăng tốc sau khi xuyên".

[^S2]: Osler, C. L. (2005). *Stop-loss orders and price cascades in currency markets.* Journal of International Money and Finance, 24(2), 219–241. Bản staff report: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.pdf — stop-loss gây price cascade; phản ứng với stop lớn hơn và kéo dài hơn phản ứng với take-profit; có ý nghĩa trong hàng giờ, không phải hàng ngày.

[^S3]: Kavajecz, K. A., & Odders-White, E. R. (2004). *Technical Analysis and Liquidity Provision.* Review of Financial Studies, 17(4), 1043–1071. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=315660 — mức S/R trùng với đỉnh độ sâu sổ lệnh limit; quy tắc kỹ thuật định vị độ sâu đã có sẵn.

[^S4]: Garzarelli, F., Cristelli, M., et al. (2014). *Memory effects in stock price dynamics: evidences of technical trading.* Scientific Reports, 4, 4487. https://www.nature.com/articles/srep04487 (preprint: arXiv:1110.5197) — 9 cổ phiếu LSE năm 2002, thang 45–180 giây; giá bật nhiều hơn xuyên tại S/R; xác suất bật tăng theo số lần bật trước; chuỗi xáo trộn ≈ 0.5.

[^S5]: Chung, K., & Bellotti, A. (2021). *Evidence and Behaviour of Support and Resistance Levels in Financial Time Series.* arXiv:2101.07410 (preprint, chưa peer-review). https://arxiv.org/abs/2101.07410 — mức S/R có nhiều lần bật trước dễ bật hơn; xác suất bật giảm theo thời gian.

[^S6]: Bucci, F., Benzaquen, M., Lillo, F., & Bouchaud, J.-P. (2019). *Slow decay of impact in equity markets: insights from the ANcerno database.* Market Microstructure and Liquidity. arXiv:1901.05332 — ~8 triệu metaorder; cuối ngày tác động còn ≈ 2/3 đỉnh, tiếp tục suy giảm các ngày sau.

[^S7]: Bailey, D. H., Borwein, J., López de Prado, M., & Zhu, Q. J. (2017). *The Probability of Backtest Overfitting.* Journal of Computational Finance. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253 — khung CSCV/PBO để ước lượng xác suất backtest bị overfit.

[^S8]: Sullivan, R., Timmermann, A., & White, H. (1999). *Data-Snooping, Technical Trading Rule Performance, and the Bootstrap.* Journal of Finance, 54(5), 1647–1691.

[^S9]: White, H. (2000). *A Reality Check for Data Snooping.* Econometrica, 68(5), 1097–1126.

[^S10]: Gelman, A., & Loken, E. (2014). *The Statistical Crisis in Science.* American Scientist, 102(6), 460–465 — "garden of forking paths".

[^S11]: Lillo, F., Mike, S., & Farmer, J. D. (2005). *Theory for long memory in supply and demand.* Physical Review E, 71, 066122 — lệnh lớn được chia nhỏ thành nhiều lệnh con (metaorder splitting).

[^S12]: Định nghĩa ICT qua nguồn thứ cấp (Tier 3–4): bản trích lại định nghĩa "lowest candle with a down close that has the most range between open to close… near support" và quy tắc Mean Threshold theo thân nến — https://en.rattibha.com/thread/1758939804388012497 ; biến thể "grab + engulf" — https://innercircletrader.net/tutorials/ict-order-block/ . Chưa đối chiếu với video mentorship gốc.
