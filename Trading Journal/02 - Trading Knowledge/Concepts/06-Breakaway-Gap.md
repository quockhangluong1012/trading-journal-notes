---
type: ict-concept
concept: Breakaway Gap
aliases:
  - Breakaway Gap
  - BAG
  - Gap phá vỡ
  - Breakaway Gap (TA cổ điển)
tags:
  - trading/ict/concept
  - trading/study
  - trading/deep-dive
  - "#BreakawayGap"
status: developing
category: Market Structure
timeframes:
  - D1
  - H4
  - H1
  - M5
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 3
confidence:
version: v2
last_reviewed: 2026-11-10
created: 2026-06-26
updated: 2026-11-10
prerequisites:
  - "[[13-FVG-Fair-Value-Gap]]"
  - "[[50-Displacement-In-Depth]]"
  - "[[05-BOS-Break-of-Structure]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[19-Liquidity]]"
  - "[[12-Dealing-Range]]"
  - "[[23-New-Day-Opening-Gap]]"
  - "[[24-New-Week-Opening-Gap]]"
common_mistakes:
  - "[[04-Mistake-FOMO-Entry]]"
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[08-Mistake-Weak-Displacement]]"
  - "[[10-Mistake-FVG-Not-Valid]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
---

# Breakaway Gap (BAG) — Deep Dive · v2

> [!summary] Tóm tắt 1 câu
> **Breakaway Gap là một khoảng trống giá (hai cây nến liền nhau không chạm vào nhau) xuất hiện đúng lúc giá RỜI KHỎI một vùng đi ngang hoặc một mức mà nhiều người đã nhìn thấy. Bản thân khoảng trống chỉ là dấu vết; cái tên "breakaway" chỉ đúng khi các nến SAU đó cho thấy giá được chấp nhận ở vùng mới. Nó là thông tin BỐI CẢNH, không phải tín hiệu vào lệnh.**

> [!important] Năm nguyên tắc cốt lõi của bản v2
> 1. **Breakaway Gap là khái niệm của Technical Analysis cổ điển, không phải của ICT.** Bốn loại gap (common, breakaway, runaway, exhaustion) được đặt tên theo VỊ TRÍ của gap trong cấu trúc giá. Trong cộng đồng ICT, cùng cái tên này thường được dùng cho một thứ khác (một FVG không bị quay lại) — phải ghi rõ đang dùng nghĩa nào (§5.3).
> 2. **Gap là một sự kiện hình học; breakaway là một sự kiện cấu trúc; xu hướng là một sự kiện theo thời gian.** Ba thứ này cần ba lượng thông tin khác nhau và không suy ra nhau (§13).
> 3. **Không ai biết chắc một gap là breakaway tại lúc nó xuất hiện.** Lúc đó nó chỉ là "ứng viên". Bulkowski viết thẳng: khi bạn nhận diện chắc chắn được loại gap thì nhịp giá đã đi gần hết (§19).
> 4. **Lấp gap không có nghĩa là breakout thất bại.** Đường quyết định là biên của vùng cũ và nơi giá ĐÓNG CỬA, không phải mép gap (§12).
> 5. **Trong các thị trường bạn đang giao dịch (NQ1, EURUSD, GBPUSD, XAUUSD), gap thật trên D1 hiếm**, vì các thị trường này giao dịch gần như liên tục. Đừng ép mọi cú phá range thành "breakaway gap" (§16).

> [!abstract] Cách đọc note này — các nhãn dùng xuyên suốt
> | Nhãn | Nghĩa |
> |---|---|
> | **[QUAN SÁT]** | Thấy trực tiếp trên chart. Ai nhìn cũng thấy giống nhau. |
> | **[MARKET MECHANICS]** | Giải thích bằng cách lệnh được khớp, sổ lệnh, phiên giao dịch, đấu giá. Đây là sự thật về cách thị trường vận hành. |
> | **[TECHNICAL ANALYSIS]** | Cách TA cổ điển đặt tên và phân loại (Edwards & Magee, Bulkowski, StockCharts). |
> | **[ICT FRAMEWORK]** | Cách ICT / cộng đồng ICT dùng và diễn giải. |
> | **[INTERPRETATION]** | Hợp lý, nhưng KHÔNG thể xác nhận chỉ bằng chart OHLC. |
> | **[UNCONFIRMED CLAIM]** | Câu nói phổ biến nhưng không có đủ cơ sở. |
>
> Mỗi khái niệm khó đi theo đúng sáu bước: **Ví dụ đời thường → Điều gì xảy ra trên thị trường → Vì sao → Giải thích chuyên môn → Ý nghĩa thực tế → Giới hạn.**
> Mọi hình `BAG-v2-*` là **sơ đồ dựng (synthetic)**: giá trong hình là ví dụ để hiểu, không phải dữ liệu thật. Note này **hạn chế số học**: chỉ dùng so sánh giá đơn giản (cao hơn / thấp hơn), không công thức, không thống kê.

### Bản đồ đọc nhanh

| Bạn muốn biết | Đọc |
|---|---|
| Gap là gì, vì sao giá "nhảy" được | §2, §3, §4 |
| Breakaway Gap là gì, vì sao có | §5, §6, §7, §8 |
| Nhận diện và phân loại | §9, §10, §11 |
| Lấp gap, cấu trúc, thanh khoản, ICT | §12, §13, §14, §15 |
| Khác nhau giữa các thị trường | §16 |
| Thất bại, hiểu lầm, hindsight | §17, §18, §19 |
| Dùng thực tế trong D1 → H1 → M5 | §20, §21 |
| Ví dụ, lỗi, điều ta thật sự biết | §22, §23, §24, §25 |

---

## 1. Executive Summary

**Gap là gì (một câu):** hai cây nến liền nhau mà phần giá của chúng không chạm vào nhau — giữa chúng có một khoảng giá mà, trên chart đó, không có giao dịch nào được vẽ ra.

**Vì sao gap tồn tại:** giá chỉ xuất hiện ở những nơi có người mua và người bán khớp lệnh với nhau. Khi thị trường đóng cửa (qua đêm, cuối tuần) hoặc khi các mức giá ở giữa không có ai đặt lệnh, giá tiếp theo có thể xuất hiện ở xa giá cũ. **[MARKET MECHANICS]**

**Breakaway Gap là gì:** một gap xuất hiện đúng lúc giá rời khỏi một vùng đi ngang (range, vùng tích lũy) hoặc vượt qua một mức hỗ trợ/kháng cự mà nhiều người đã thấy. **[TECHNICAL ANALYSIS]**

**Điều làm nó khác các gap khác:** không phải kích thước, không phải màu nến, mà là **vị trí** (rời khỏi một cấu trúc) và **hành vi sau đó** (giá có được chấp nhận ở vùng mới không). Common gap nằm trong range; runaway gap nằm giữa một nhịp đang chạy; exhaustion gap nằm cuối một nhịp dài. Lúc mới xuất hiện, cả bốn có thể trông giống hệt nhau.

**Điều ta biết chắc:**
- Gap là chuyện bình thường của cách thị trường vận hành (phiên giao dịch, đấu giá mở cửa, sổ lệnh mỏng). **[MARKET MECHANICS]**
- TA cổ điển phân loại gap theo vị trí trong cấu trúc. **[TECHNICAL ANALYSIS]**
- Các nguồn TA (StockCharts, Bulkowski) đều nói breakaway gap thường KHÔNG bị lấp nhanh, khác với common gap và exhaustion gap. Đây là quan sát có điều kiện (chủ yếu trên cổ phiếu), không phải luật.

**Điều ta không biết chắc:**
- Ai đã tạo ra gap và vì sao. Chart không cho thấy danh tính hay ý định. **[INTERPRETATION]**
- Gap này có mở ra một xu hướng không — chỉ biết dần theo thời gian.

**Cách dùng đúng:** Breakaway Gap trả lời câu hỏi **"thị trường đang ở đâu so với vùng cũ?"** (bối cảnh D1). Nó **không** trả lời câu hỏi **"vào lệnh ở đâu?"** — câu đó thuộc về H1 → M5 (sweep → MSS → displacement → FVG).

---

## 2. Explain Like I'm 5 — Mental Model của Gap

### 2.1 Câu chuyện sạp cam

![[BAG-v2-01-ELI5-Cho-Cam.svg|960]]
*Hình BAG-v2-01 — Chiều hôm qua cam bán giá 10. Đêm qua có tin bão. Sáng nay không ai chịu bán ở 11, món đầu tiên bán ở 12. Giá 11 bị "bỏ qua".*

Hãy tưởng tượng một cái chợ nhỏ.

- **Chiều hôm qua:** sạp có rất nhiều cam. Ai muốn mua thì mua ở giá 10. Cả buổi chiều giá chỉ nhích quanh 10. Chợ đóng cửa, giá cuối cùng là 10.
- **Đêm qua:** chợ đóng, không ai mua bán được. Nhưng trên tivi có tin: bão làm hỏng mùa cam, cam sẽ ít đi. Mọi người **đổi ý** trong lúc ngủ. Người bán nghĩ: "cam sắp hiếm, mình không bán rẻ nữa". Người mua nghĩ: "phải mua sớm kẻo hết".
- **Sáng nay:** chợ mở. Không người bán nào chịu bán ở 11. Người bán rẻ nhất cũng đòi 12. Người mua đang vội nên chấp nhận 12. **Món cam đầu tiên được bán ở 12.**

Giữa 10 và 12 có số 11. Nhưng **không ai mua bán ở giá 11** trong khoảng thời gian giữa hai phiên chợ. Nếu bạn vẽ giá lên một cái thước, sẽ có một **khoảng trống** từ 10 đến 12. Đó là **gap**.

> [!tip] Ba điều đứa trẻ 5 tuổi cần nhớ
> 1. **Giá không phải là một con số tự bay.** Giá là con số mà một người mua và một người bán cùng đồng ý.
> 2. **Khi không có ai đồng ý ở một mức, mức đó không có giá.** Nó không bị "nhảy qua" bằng phép thuật — chỉ là không ai giao dịch ở đó.
> 3. **Gap thường xuất hiện khi mọi người đổi ý trong lúc không được mua bán** (chợ đóng cửa), hoặc **khi ở các mức giữa không có ai đứng bán** (§2.2).

### 2.2 Đi cầu thang hay nhảy cóc?

![[BAG-v2-02-Cau-Thang-va-Nhay-Coc.svg|960]]
*Hình BAG-v2-02 — Mỗi bậc là một mức giá, mỗi người đứng trên bậc là một người đang chờ bán. Bậc trống thì không có giao dịch ở đó.*

Gap còn có thể xảy ra **ngay trong lúc chợ đang mở**.

Tưởng tượng một cầu thang. Mỗi bậc là một mức giá: 101, 102, 103… Trên mỗi bậc có vài người đứng chờ bán cam ở đúng giá đó.

- Một người mua đến. Người đó mua của người đứng ở **bậc thấp nhất còn người**. Mua hết người ở bậc 101 thì lên bậc 102, rồi 103… Giá đi lên **từng bậc một**.
- Nhưng nếu **bậc 103 và 104 không có ai đứng**, người mua sau khi mua hết bậc 102 sẽ phải lên thẳng bậc 105 — nơi có người tiếp theo. Giá đi từ 102 lên 105. **103 và 104 không có giao dịch.**

Không có ai "cố ý" làm giá nhảy. Chỉ là các bậc ở giữa đang trống.

### 2.3 Vì sao sự thay đổi này đôi khi là chuyện lớn?

Quay lại sạp cam. Có hai khả năng sau buổi sáng:

- **Khả năng 1:** cả ngày, người ta tiếp tục mua ở 12, 13, 14. Không ai quay lại bán ở 10 nữa. → Cái chợ đã **đổi "giá bình thường"** từ khoảng 10 sang khoảng 12–14. Đây là một sự thay đổi lớn.
- **Khả năng 2:** đến trưa, người ta nghe tin bão đi hướng khác. Người bán lại chịu bán rẻ, giá quay về 10. → Buổi sáng chỉ là một **phản ứng tạm thời**.

Lúc 7 giờ sáng, khi món cam đầu tiên được bán ở 12, **không ai biết** ngày hôm đó sẽ là khả năng 1 hay khả năng 2. Đây chính là bài học quan trọng nhất của toàn bộ note:

> [!warning] Bài học cốt lõi
> **Gap cho bạn biết giá đã nhảy. Gap KHÔNG cho bạn biết giá sẽ ở lại.** Cái tên "Breakaway" chỉ được dùng khi giá chứng minh nó ở lại vùng mới (khả năng 1).

> [!note] Giới hạn của ví dụ
> Chợ cam đơn giản hơn thị trường thật nhiều. Thị trường thật có rất nhiều người, có lệnh chờ sẵn, có máy tính đặt lệnh, có nhiều sàn khác nhau. Nhưng nguyên lý "giá chỉ có ở nơi có người mua và người bán khớp nhau" là đúng ở mọi nơi.

---

## 3. What Is a Gap? — Gap là gì?

### 3.1 Ví dụ thị trường đơn giản (Level 2)

![[BAG-v2-03-Gap-Tren-Chart-Nen.svg|960]]
*Hình BAG-v2-03 — Cùng một cặp nến ngày, hai cách đo gap cho hai kết quả khác nhau.*

Dùng con số minh họa:

```text
PHIÊN TRƯỚC (hôm qua)               PHIÊN SAU (hôm nay)

                                    112  ← cao nhất hôm nay
                                    110  ← MỞ CỬA hôm nay
                                    108  ← thấp nhất hôm nay
                 ┐
                 │  khoảng 105 → 108: KHÔNG có giao dịch trong cả hai phiên
                 ┘
105  ← cao nhất hôm qua
104  ← ĐÓNG CỬA hôm qua
100  ← thấp nhất hôm qua
```

Trả lời từng câu:

| Câu hỏi | Trả lời |
|---|---|
| Giá đóng cửa phiên trước ở đâu? | 104 |
| Giá mở cửa phiên sau ở đâu? | 110 |
| Khoảng nào không có giao dịch trong cả hai phiên? | Từ 105 (cao nhất hôm qua) đến 108 (thấp nhất hôm nay) |
| Gap hình thành như thế nào? | Hôm nay giá bắt đầu ở 110 và cả ngày không xuống dưới 108. Hôm qua cả ngày không lên quá 105. Hai phiên không có phần giá chung. |
| Điều gì có thể khiến giá mở cao hơn đỉnh hôm qua? | Thông tin mới hoặc kỳ vọng mới trong lúc không có giao dịch liên tục, khiến người bán đòi giá cao hơn và người mua chấp nhận (§4, §6). |
| Vì sao đây có thể là dấu hiệu thị trường thay đổi? | Vì cả một phiên, không ai giao dịch ở giá cũ nữa. Nhưng "có thể" là chữ quan trọng: một phiên chưa đủ để kết luận (§19). |

### 3.2 Hai cách đo gap — và vì sao phải nói rõ

**[TECHNICAL ANALYSIS]** Có hai cách đo phổ biến:

| Cách đo | So sánh | Ví dụ trên | Ai dùng |
|---|---|---|---|
| **Full gap (High ↔ Low)** | Cao nhất nến trước với thấp nhất nến sau | 105 → 108 | TA cổ điển. Bulkowski định nghĩa gap tăng là khi "thấp nhất hôm nay cao hơn cao nhất hôm qua". |
| **Opening gap (Close → Open)** | Đóng cửa nến trước với mở cửa nến sau | 104 → 110 | Dùng cho gap mở phiên. ICT dùng kiểu này cho [[23-New-Day-Opening-Gap]] và [[24-New-Week-Opening-Gap]]. |

Hai cách đo **không cho cùng một kết quả**. Nếu hôm nay mở ở 110 nhưng trong ngày rơi xuống 104, thì:

- opening gap vẫn có (104 → 110),
- nhưng full gap **không còn** — trong ngày, giá đã đi lại toàn bộ khoảng đó. Trên chart D1 sẽ không còn khoảng trống nào.

> [!important] Quy tắc ghi chép
> Mỗi khi ghi "gap" trong journal, ghi luôn: **(1) đo kiểu nào, (2) trên khung nào, (3) chart của phiên nào / nguồn dữ liệu nào.** Thiếu một trong ba, hai người nhìn cùng một chart có thể nói về hai thứ khác nhau.

### 3.3 Gap có nghĩa là "không ai giao dịch ở đó" không?

![[BAG-v2-06-Gap-Phu-Thuoc-Cach-Ve-Chart.svg|960]]
*Hình BAG-v2-06 — Cùng một diễn biến, ba cách vẽ chart. Gap chỉ hiện rõ ở cách thứ nhất.*

**Không hoàn toàn.** Gap trên chart có nghĩa là **trên chart đó, trong các phiên được vẽ, không có giao dịch nào ở vùng giá đó.** Nó không chứng minh rằng ở mọi nơi, mọi lúc, không ai giao dịch ở đó.

**[MARKET MECHANICS]** Ba ví dụ:

1. **Cổ phiếu Mỹ có giờ giao dịch mở rộng** (trước giờ mở cửa và sau giờ đóng cửa). Chart chỉ vẽ giờ chính thức có thể hiện gap; nhưng trong giờ mở rộng, cổ phiếu có thể đã giao dịch ở chính các mức đó. SEC cảnh báo giá trong giờ mở rộng có thể không phản ánh giá giờ chính thức vì ít người tham gia, spread rộng hơn, và các hệ thống giao dịch giờ mở rộng không nối với nhau.
2. **Futures chỉ số (NQ, ES) giao dịch gần như cả ngày đêm.** Cùng một sự kiện làm cổ phiếu gap qua đêm có thể chỉ là một cây nến mạnh liên tục trên chart futures.
3. **Forex là thị trường phi tập trung.** Mỗi broker có nguồn giá riêng. Một "gap" trên chart broker này có thể không có trên chart broker khác (§16).

> [!note] Câu ngắn để nhớ
> **Gap là đặc điểm của CHART + PHIÊN + NGUỒN DỮ LIỆU.** Trước khi phân tích gap, hãy hỏi: "chart này vẽ phiên nào, từ nguồn nào?"

### 3.4 Gap có luôn xuất hiện giữa hai phiên không?

Không. Có hai loại theo thời điểm:

| Loại | Xảy ra khi nào | Nguyên nhân cơ học |
|---|---|---|
| **Opening gap** | Giữa giá đóng cửa và giá mở cửa của hai phiên (qua đêm, cuối tuần, sau giờ nghỉ) | Không có khớp lệnh liên tục trong lúc đóng cửa; thông tin và lệnh tích tụ lại |
| **Intraday discontinuity** (bước nhảy trong phiên) | Giữa hai nến liền nhau trong cùng phiên | Các mức giá ở giữa không có lệnh chờ (tin nóng, thanh khoản mỏng, ai đó rút lệnh) |

Trên khung nhỏ (M1, M5), một bước nhảy trong phiên có thể hiện ra như một gap giữa hai nến. Trên khung lớn, cùng bước nhảy đó nằm gọn trong một nến dài, không thấy gap nữa.

### 3.5 Thị trường tập trung và phi tập trung

| | Thị trường tập trung (sàn: cổ phiếu, futures) | Thị trường phi tập trung (OTC: Forex giao ngay) |
|---|---|---|
| Có một sổ lệnh chung? | Có, mỗi sàn có sổ lệnh và giá chính thức | Không. BIS mô tả FX giao ngay giao dịch "over the counter", qua dealer, "decentralised and fragmented" |
| Giá mở cửa | Do sàn xác định (ví dụ phiên đấu giá mở cửa) | Không có "giá mở cửa chính thức" duy nhất; mỗi nguồn có giá riêng |
| Gap trên chart | Rõ ràng, giống nhau trên mọi chart lấy dữ liệu từ sàn đó | Phụ thuộc broker / nhà cung cấp dữ liệu |
| Hệ quả | Gap là một sự kiện có thể kiểm tra | Gap phải được kiểm tra trên nhiều nguồn trước khi tin |

### 3.6 Bản đồ họ "gap" — đừng gọi mọi khoảng trống bằng cùng một tên

![[BAG-v2-07-Ban-Do-Ho-Gap.svg|960]]
*Hình BAG-v2-07 — Ba câu hỏi khác nhau: gap xảy ra KHI NÀO, gap nằm Ở ĐÂU trong cấu trúc, và đó có thật sự là gap không.*

| Thuật ngữ | Định nghĩa ngắn | Thuộc về |
|---|---|---|
| **Price gap** | Hai nến liền nhau không có phần giá chung | Hình học chart |
| **Opening gap** | Khoảng giữa giá đóng cửa phiên trước và giá mở cửa phiên sau | Thời điểm (phiên) |
| **Common gap** (area gap) | Gap nằm trong vùng đi ngang; thường lấp nhanh; ít ý nghĩa cấu trúc | TA cổ điển — vị trí |
| **Breakaway gap** | Gap xuất hiện khi giá rời một vùng tích lũy / cấu trúc | TA cổ điển — vị trí |
| **Runaway gap** (measuring / continuation) | Gap giữa một nhịp đang chạy mạnh | TA cổ điển — vị trí |
| **Exhaustion gap** | Gap gần cuối một nhịp dài; thường lấp nhanh rồi giá đứng lại/đảo chiều | TA cổ điển — vị trí |
| **Island reversal** | Một MÔ HÌNH: gap đi, đi ngang, rồi gap ngược lại, để lại một "hòn đảo" giá | TA cổ điển — mô hình |
| **Imbalance** | Cách DIỄN GIẢI một vùng giá đi nhanh một chiều. Không phải phép đo | Diễn giải |
| **ICT Fair Value Gap** | Mẫu 3 nến: vùng giá mà chỉ nến giữa đi qua | ICT — hình học 3 nến |

Hai trục "thời điểm" và "vị trí" là độc lập: một opening gap có thể là common hoặc breakaway; một breakaway có thể là opening gap hoặc bước nhảy trong phiên.

### 3.7 Breakaway Gap có giống FVG không?

**Không.** Đây là nhầm lẫn phổ biến nhất trong cộng đồng ICT. Chi tiết ở §15.2; tóm tắt:

| Khía cạnh | Breakaway Gap (TA cổ điển) | ICT Fair Value Gap |
|---|---|---|
| **Cách hình thành** | Hai nến liền nhau không chạm nhau | Ba nến: râu nến 1 và râu nến 3 không chạm nhau |
| **Cấu trúc giá** | Có khoảng giá KHÔNG có giao dịch trên chart | Khoảng giá CÓ giao dịch, nhưng chỉ nến giữa đi qua |
| **Điều kiện nhận diện** | Phải có vùng/cấu trúc bị rời bỏ | Không cần bối cảnh; FVG có thể ở bất cứ đâu |
| **Ý nghĩa** | Thị trường có thể đã đổi vùng giá | Giá đã đi qua đoạn này rất nhanh, một chiều |
| **Timeframe thường gặp** | D1 (cổ phiếu, futures qua phiên) | Mọi khung, kể cả M1–M5 |
| **Cách dùng** | Đọc bối cảnh | Tham chiếu vị trí cho entry |

Một chuỗi giá có thể có cả hai, chỉ có một, hoặc không có cái nào.

---

## 4. How Does a Gap Form? — Gap hình thành như thế nào?

Phần này giải thích Level 3 (thuật ngữ chuyên môn). Mỗi thuật ngữ được giải thích bằng lời trước.

### 4.1 Bảng thuật ngữ — giải thích bằng lời thường

| Thuật ngữ | Nghĩa bằng lời thường |
|---|---|
| **Bid** | Giá cao nhất mà ai đó đang **chờ mua** ngay lúc này |
| **Ask** (offer) | Giá thấp nhất mà ai đó đang **chờ bán** ngay lúc này |
| **Spread** | Khoảng cách giữa bid và ask |
| **Limit order** (lệnh giới hạn) | "Tôi chỉ mua ở giá X hoặc rẻ hơn" / "Tôi chỉ bán ở giá X hoặc đắt hơn". Lệnh này **nằm chờ** trong sổ lệnh |
| **Market order** (lệnh thị trường) | "Mua/bán ngay, giá nào cũng được". Lệnh này **ăn** các lệnh đang chờ |
| **Order book** (sổ lệnh) | Danh sách tất cả lệnh giới hạn đang chờ, xếp theo giá |
| **Order matching** (khớp lệnh) | Việc sàn ghép một lệnh mua với một lệnh bán ở cùng một giá |
| **Liquidity** (thanh khoản) | Có bao nhiêu lệnh đang chờ quanh giá hiện tại. Nhiều lệnh chờ = mua bán lớn mà giá ít thay đổi |
| **Price discovery** (tìm giá) | Quá trình thị trường thử các mức giá cho đến khi tìm được nơi có đủ người mua và người bán |
| **Volatility** (biến động) | Giá thay đổi nhiều hay ít trong một khoảng thời gian |
| **Opening price** | Giá giao dịch đầu tiên (hoặc giá đấu giá mở cửa) của phiên |
| **Previous close** | Giá đóng cửa của phiên trước |
| **Price discontinuity** | Hai mức giá liền kề trên chart không nối với nhau |
| **Market structure** | Cách các đỉnh, đáy, vùng đi ngang sắp xếp với nhau |
| **Breakout** | Giá đi ra ngoài một vùng hoặc một mức đã được nhiều người nhìn thấy |

### 4.2 Cơ chế 1 — Sổ lệnh có "bậc trống" (intraday discontinuity)

![[BAG-v2-04-So-Lenh-va-Khoang-Nhay.svg|960]]
*Hình BAG-v2-04 — Một lệnh mua thị trường ăn hết lệnh chờ ở 101, 102, rồi phải lên 105 vì 103–104 không có ai chờ bán.*

**Ví dụ đời thường:** cầu thang có bậc trống (§2.2).

**Điều gì xảy ra trên thị trường [MARKET MECHANICS]:**
1. Trong sổ lệnh, người bán chờ ở 101 (5 đơn vị), 102 (3 đơn vị), 105 (2 đơn vị), 106 (8 đơn vị). Ở 103 và 104 không có ai.
2. Một lệnh **mua thị trường** 10 đơn vị đến.
3. Sàn khớp: 5 đơn vị ở 101, 3 đơn vị ở 102. Còn thiếu 2. Mức tiếp theo có người bán là 105 → khớp 2 đơn vị ở 105.
4. Băng giao dịch in ra: 101, 102, 105. Trên chart: một bước nhảy từ 102 lên 105.

**Vì sao các bậc ở giữa trống?** Chart không trả lời được. Một số khả năng **[INTERPRETATION]**: người bán vừa rút lệnh vì sợ tin sắp ra; người tạo lập thị trường nới rộng giá chào khi không chắc chắn; đơn giản là chưa ai kịp đặt lệnh.

**Ý nghĩa thực tế:** bước nhảy trong phiên nói rằng **thanh khoản quanh giá lúc đó mỏng**. Nó không tự nói rằng có một sự thay đổi lâu dài.

**Giới hạn:** trên chart nến, bạn không thấy sổ lệnh. Bạn chỉ thấy hệ quả (bước nhảy), không thấy nguyên nhân.

### 4.3 Cơ chế 2 — Phiên đấu giá mở cửa (opening gap)

![[BAG-v2-05-Dau-Gia-Mo-Cua.svg|960]]
*Hình BAG-v2-05 — Lệnh dồn lại qua đêm được khớp MỘT lần ở MỘT giá lúc mở cửa.*

**Ví dụ đời thường:** sạp cam mở cửa buổi sáng (§2.1).

**Điều gì xảy ra trên thị trường [MARKET MECHANICS]:** Ở nhiều sàn cổ phiếu, lệnh gửi trước giờ mở cửa không được khớp ngay. Chúng được gom lại và khớp một lần trong **phiên đấu giá mở cửa**. Ví dụ Nasdaq Opening Cross: tài liệu của Nasdaq ghi rằng giá được chọn theo thứ tự ưu tiên — (1) khớp được nhiều cổ phiếu nhất, (2) phần lệnh không khớp được ít nhất, (3) gần giá giữa bid–ask nhất. Trước giờ mở cửa, Nasdaq công bố thông tin về phần lệnh mua/bán đang chênh (Net Order Imbalance Indicator).

**Vì sao giá mở cửa có thể xa giá đóng cửa:** không có quy tắc nào buộc giá mở cửa phải gần giá đóng cửa hôm qua. Giá mở cửa là nơi lệnh mua và lệnh bán **lúc đó** gặp nhau. Nếu qua đêm có tin làm nhiều người muốn mua ở giá cao và ít người chịu bán rẻ, điểm gặp nhau sẽ cao hơn nhiều.

**Giải thích chuyên môn:** trong lúc không có khớp lệnh liên tục, thông tin mới vẫn đến. Khi mở cửa, toàn bộ thông tin đó được phản ánh vào giá trong **một lần** — thay vì từng bước nhỏ như trong phiên. Đó là **price discovery dồn lại**.

**Ý nghĩa thực tế:** opening gap là kết quả **bình thường** của việc thị trường có giờ nghỉ. Bản thân nó chưa nói gì về "breakaway" hay xu hướng.

**Giới hạn:** futures và Forex không có phiên đấu giá mở cửa giống cổ phiếu (futures có các giai đoạn pre-open riêng theo quy định từng sàn — kiểm tra tài liệu của sàn). Đừng mang nguyên cơ chế cổ phiếu sang thị trường khác.

### 4.4 Năm nguồn gốc của gap — đừng gộp chung

| Nguồn gốc | Ví dụ | Gap này nói gì |
|---|---|---|
| **Tin tức / sự kiện bất ngờ** | Báo cáo lợi nhuận, quyết định lãi suất, tin địa chính trị | Thông tin mới được phản ánh nhanh |
| **Thay đổi kỳ vọng** | Dữ liệu kinh tế khác dự đoán, thay đổi trong định giá chung | Thị trường đánh giá lại "giá hợp lý" |
| **Thiếu thanh khoản ở các mức giữa** | Giờ thanh khoản mỏng, ngày lễ, sát giờ tin | Ít lệnh chờ, giá dễ nhảy |
| **Mở cửa sau giờ nghỉ** | Qua đêm, cuối tuần, giờ nghỉ hằng ngày của futures | Lệnh và thông tin tích tụ trong lúc nghỉ |
| **Do dữ liệu / cách vẽ chart** | Đổi hợp đồng futures, giờ đóng nến khác nhau, thiếu giờ mở rộng | Không phải sự kiện giá |

> [!warning] Đừng mặc định
> Không phải mọi breakaway gap đều có cùng một nguyên nhân. Một gap do tin bất ngờ và một gap do giờ thanh khoản mỏng có thể trông giống hệt nhau trên chart, nhưng nói lên những điều rất khác.

---

## 5. What Is a Breakaway Gap? — Breakaway Gap là gì?

### 5.1 Sáu bước để hiểu

**① Ví dụ đời thường — "Đi chơi" hay "Chuyển nhà"?**
Một gia đình sống trong một căn nhà rất lâu (đó là **vùng đi ngang** — range). Một sáng, cả nhà lên xe chạy một mạch sang đầu kia thành phố, không ghé con đường nào ở giữa (đó là **gap**). Họ đã **chuyển nhà** chưa? Chưa biết. Nếu tối đó họ quay về nhà cũ, đó chỉ là **một chuyến đi chơi**. Nếu họ ở lại, mở đồ đạc, sống ở nhà mới nhiều ngày — đó mới là **chuyển nhà**. Breakaway Gap là trường hợp "chuyển nhà": giá rời căn nhà cũ bằng một cú nhảy, rồi ở lại nhà mới.

**② Điều gì xảy ra trên thị trường [QUAN SÁT]:** giá đã đi ngang trong một vùng có biên rõ ràng. Rồi một nến mới xuất hiện **hoàn toàn bên ngoài** vùng đó, không chạm vào nến trước. Sau đó giá tiếp tục giao dịch ở phía bên ngoài.

**③ Vì sao [INTERPRETATION]:** trong lúc giá đi ngang, người mua và người bán tạm đồng ý rằng "giá hợp lý" nằm trong vùng đó. Gap nói rằng ở thời điểm mới, **không còn đủ người sẵn sàng giao dịch ở giá cũ** — có thể vì thông tin mới, vì kỳ vọng thay đổi, hoặc vì lệnh chờ ở biên đã bị dùng hết. Chart không cho biết lý do nào đúng.

**④ Giải thích chuyên môn [TECHNICAL ANALYSIS]:** StockCharts định nghĩa breakaway gap xảy ra "khi giá đang thoát khỏi một vùng giao dịch hoặc vùng tắc nghẽn" (*trading range or congestion area*). Bulkowski mô tả breakaway gap "bắt đầu một xu hướng mới" và "thường xảy ra khi rời một vùng tích lũy". Dòng phân loại bốn loại gap này đến từ TA cổ điển (truyền thống Edwards & Magee), có trước ICT hàng chục năm.

**⑤ Ý nghĩa thực tế:** nếu giá ở lại vùng mới, **khung tham chiếu của bạn đổi**: range cũ không còn là "nhà" của giá; biên cũ có thể trở thành nơi giá được thử lại; mục tiêu thanh khoản (DOL) có thể đổi.

**⑥ Giới hạn:** tên gọi chỉ chắc chắn khi nhìn lại. Lúc gap xuất hiện, bạn chỉ có một **ứng viên**. Bulkowski viết thẳng: dùng gap làm thứ để giao dịch thì "khi bạn nhận diện đúng được chúng, nhịp giá đã gần kết thúc" (§19).

### 5.2 Định nghĩa dùng trong vault này

> [!info] Định nghĩa làm việc (research framework của note — dựa trên định nghĩa TA cổ điển)
> **Breakaway Gap** = một **price gap** (đo và ghi rõ cách đo) thỏa cả ba điều kiện:
> 1. **Trước gap** có một vùng đi ngang / mẫu hình / mức hỗ trợ–kháng cự **xác định được trước khi gap xảy ra**;
> 2. Gap **đưa giá ra ngoài biên** của vùng đó, theo hướng của gap;
> 3. Sau gap, giá **được chấp nhận** ở phía bên ngoài (đóng cửa và tiếp tục giao dịch ngoài biên, không lấy lại vùng cũ) — điều kiện này chỉ biết được **theo thời gian**.
>
> Thỏa (1) và (2) nhưng chưa biết (3) → gọi là **Ứng viên Breakaway Gap**.
> Thỏa (1) và (2) nhưng thất bại ở (3) → gọi là **breakout thất bại có gap**, không gọi là breakaway.

Vì sao định nghĩa có ba điều kiện thay vì một? Vì nếu chỉ dùng điều kiện "có gap rời range", mọi gap rời range sẽ được gọi là breakaway — kể cả những gap bị lấp ngay ngày hôm sau và giá quay về range. Khi đó cái tên không còn mang thông tin gì.

### 5.3 Một cái tên, hai nghĩa — TA cổ điển và cộng đồng ICT

![[BAG-v2-25-Hai-Nghia-Cua-Ten-Goi.svg|960]]
*Hình BAG-v2-25 — Cùng chữ "Breakaway Gap" nhưng hai cộng đồng dùng cho hai thứ khác nhau.*

| | Nghĩa 1 — TA cổ điển | Nghĩa 2 — cách dùng phổ biến trong cộng đồng ICT/SMC |
|---|---|---|
| **Là gì** | Khoảng trống giá THẬT giữa hai nến khi giá rời một vùng tích lũy | Một FVG nằm trong cú displacement mà giá **không quay lại** ("unmitigated") |
| **Nguồn** | StockCharts, Bulkowski, truyền thống Edwards & Magee | Các trang cộng đồng: innercircletrader.net, FluxCharts, các diễn đàn |
| **Cần gap thật?** | Có | Không — chỉ cần FVG |
| **Biết lúc nào** | Hình học: ngay lập tức. Tên gọi: theo thời gian | Chỉ biết "không bị quay lại" SAU KHI giá đã đi xa |
| **Đi kèm** | Thường nói về volume, follow-through | Thường mô tả một "cơ chế giữ giá" phía dưới (breaker, iFVG, BPR) |

**[ICT FRAMEWORK]** Trong lần nghiên cứu này, **không tìm được định nghĩa nguyên văn của ICT (Michael J. Huddleston) cho "breakaway gap"**. Đã kiểm tra transcript máy của các tập 2, 3, 5, 6, 7, 14, 21 trong ICT 2022 Mentorship — không thấy chữ "breakaway". (Giới hạn: transcript tự động và chỉ đọc đầy đủ một phần — không tìm thấy KHÔNG chứng minh ICT chưa từng dùng.) Các trang cộng đồng dùng nghĩa 2 cũng **không dẫn nguồn ICT cụ thể**, và **mâu thuẫn nhau** về cách dùng: một trang khuyên chờ giá test "cơ chế giữ giá" rồi vào lệnh; trang khác nói breakaway gap "khó giữ vai trò vùng vào lệnh về sau".

> [!important] Quy tắc của vault
> Trong note này và trong journal, **"Breakaway Gap" = Nghĩa 1 (TA cổ điển)**. Khi muốn nói về "FVG trong displacement không bị quay lại", hãy viết đúng như vậy hoặc dùng [[13-FVG-Fair-Value-Gap]]. Đừng để một cái tên mang hai nghĩa trong cùng một bảng dữ liệu.

### 5.4 Breakout và gap là hai thứ khác nhau

![[BAG-v2-09-Ba-Kieu-Roi-Range.svg|960]]
*Hình BAG-v2-09 — Breakout không gap, breakout bằng gap, và gap nằm trong range. Chỉ ô giữa là ứng viên breakaway.*

| Trường hợp | Có gap? | Có rời range? | Gọi là |
|---|---|---|---|
| Nến lớn liên tục đi qua biên | Không | Có | Breakout (có thể có displacement, FVG) |
| Nến mới nhảy ra ngoài biên | Có | Có | **Ứng viên Breakaway Gap** |
| Gap nhỏ giữa một range rộng | Có | Không | Common gap |

---

## 6. Why Does Breakaway Gap Exist? — Vì sao Breakaway Gap xuất hiện và vì sao nó quan trọng?

### 6.1 Vì sao thường xuất hiện khi giá thoát khỏi vùng đi ngang?

**Ví dụ đời thường:** một cái đập giữ nước. Nước dâng dần sau đập (vùng đi ngang). Khi đập vỡ, nước không chảy từng giọt — nó tràn ra một lúc.

**Điều gì xảy ra [INTERPRETATION]:** trong một vùng đi ngang dài, nhiều người đặt lệnh **dựa vào chính các biên** của vùng:
- người bán khống ở biên trên đặt dừng lỗ ngay trên biên,
- người chờ breakout đặt lệnh mua chờ ngay trên biên,
- người giao dịch trong range bán ở biên trên.

Những lệnh này **tập trung quanh biên**. Khi có thông tin mới làm người bán ở biên rút đi (hoặc khi giá mở cửa thẳng ra ngoài biên), các lệnh mua chờ và dừng lỗ trở thành lệnh mua thị trường cùng một lúc. Lực đó có thể đẩy giá đi xa nhanh.

**Giới hạn:** đây là cách giải thích hợp lý dựa trên cách lệnh dừng lỗ vận hành **[MARKET MECHANICS]**, nhưng **chart không cho thấy** bao nhiêu lệnh như vậy thực sự tồn tại.

### 6.2 Vì sao gap có thể thể hiện sự thay đổi điều kiện thị trường?

Một vùng đi ngang là nơi giá được giao dịch qua lại **hai chiều** — người mua và người bán đều tìm thấy nhau ở nhiều mức. Một gap ra ngoài vùng có nghĩa là, **ở thời điểm đó**, không ai giao dịch ở các mức giữa. Nếu sau đó giá **tiếp tục được giao dịch hai chiều ở vùng mới**, ta có thể nói thị trường đã "chấp nhận" (accept) vùng giá mới. Đó là sự thay đổi điều kiện.

**Price acceptance** (chấp nhận giá) — giải thích cho trẻ 5 tuổi: nếu sạp cam bán ở 12 cả ngày, cả tuần, và người mua vẫn mua — thì 12 đã thành "giá bình thường mới". Nếu chỉ bán được vài quả ở 12 rồi phải hạ về 10 — thì 12 bị "từ chối" (rejected).

### 6.3 Vì sao đôi khi nó đánh dấu sự bắt đầu của một nhịp có hướng?

**[TECHNICAL ANALYSIS]** Đây là lý do cái tên tồn tại: những gap rời vùng tích lũy mà sau đó giá đi tiếp xa được gọi là breakaway. **Lưu ý vòng lặp logic:** ta gọi nó là breakaway *vì* sau đó có nhịp đi tiếp. Nên câu "breakaway gap đánh dấu sự bắt đầu của xu hướng" một phần đúng **theo định nghĩa**, không phải một phát hiện.

**[INTERPRETATION]** Lý do hợp lý vì sao một số gap dẫn đến xu hướng: thông tin gây ra gap có tác động dài (ví dụ thay đổi lớn trong triển vọng một công ty); người tham gia cần nhiều ngày để điều chỉnh vị thế; người lỡ tàu tiếp tục mua ở các mức cao hơn.

### 6.4 Breakaway Gap có thay đổi cách nhìn về hỗ trợ / kháng cự không?

Có thể. Biên trên của vùng cũ (kháng cự trước đó) thường được theo dõi như một nơi giá có thể dừng lại nếu quay xuống. StockCharts viết: điểm breakout "trở thành hỗ trợ mới" nếu là breakout đi lên. Bulkowski thì thận trọng hơn: gap là những nơi hỗ trợ/kháng cự **yếu**.

**Giới hạn:** "biên cũ thành hỗ trợ" là **giả thuyết có thể kiểm tra**, không phải quy luật. Nó có thể giữ, có thể không (§12).

### 6.5 Gap khi breakout ≠ gap dẫn đến breakout cấu trúc có ý nghĩa

| | Gap xuất hiện khi breakout | Gap dẫn đến structural breakout có ý nghĩa |
|---|---|---|
| Biết khi nào | Ngay khi nến mở | Sau nhiều nến |
| Cần gì | Một biên và một gap | Gap + đóng cửa ngoài biên + được chấp nhận ở vùng mới |
| Có thể thất bại? | Rất thường | Vẫn có thể, nhưng ít thông tin mâu thuẫn hơn |
| Tên gọi đúng | Ứng viên | Breakaway Gap (theo tiêu chí đã ghi trước) |

---

## 7. Core Market Mechanics — Cơ chế thị trường ở mức nâng cao

Phần này là Level 4. Mục tiêu: thay những câu nói mơ hồ bằng cơ chế cụ thể, và đánh dấu rõ chỗ nào là quan sát, chỗ nào là diễn giải.

### 7.1 Dịch những câu nói mơ hồ thành cơ chế

| Câu nói phổ biến | Nghĩa cụ thể (cơ chế) | Chart cho thấy được gì? |
|---|---|---|
| "Buyers overwhelmed sellers" (người mua áp đảo người bán) | Trong một khoảng thời gian, lượng **lệnh mua thị trường** lớn hơn lượng **lệnh bán chờ** ở các mức gần giá, nên giá phải đi lên các mức có người bán | Chỉ thấy giá đi lên. Không thấy lượng lệnh |
| "Strong buying pressure" (áp lực mua mạnh) | Lệnh mua chủ động đến liên tục và nhiều hơn khả năng đáp ứng của lệnh bán chờ | Nến tăng thân dài, ít râu trên; không thấy lệnh |
| "Imbalance in the market" (mất cân bằng) | Ở một mức giá cụ thể, phía muốn mua nhiều hơn phía muốn bán (hoặc ngược lại), nên mức đó không giữ được | Không đo được từ OHLC. Chỉ suy ra |
| "Institutional participation" (tổ chức tham gia) | Có những người đặt lệnh khối lượng lớn | Không thấy danh tính trên chart. Volume (nếu có) chỉ cho thấy khối lượng, không cho thấy ai |
| "Smart Money aggressively repriced the market" | Giá được giao dịch ở mức mới rất nhanh | Chỉ thấy tốc độ. "Smart Money" và "cố ý" là diễn giải không kiểm chứng được |

> [!warning] Quy tắc của note
> Không dùng "Smart Money" làm lời giải thích mặc định. Câu "tổ chức đã tạo ra gap này" **không thể** được xác nhận từ chart OHLC. **[UNCONFIRMED CLAIM]**

### 7.2 Market repricing — Thị trường định giá lại

**Ví dụ đời thường:** cửa hàng đổi bảng giá vào buổi sáng sau khi nhập hàng đắt hơn.

**[MARKET MECHANICS]** "Định giá lại" nghĩa là: giá mà người mua và người bán sẵn sàng khớp đã đổi. Khi đổi nhanh và trong lúc không có giao dịch liên tục, chart vẽ ra một gap. Khi đổi từ từ trong phiên, chart vẽ ra một chuỗi nến.

### 7.3 Order book dynamics — Sổ lệnh thay đổi thế nào quanh sự kiện

**[MARKET MECHANICS]** Người đặt lệnh chờ (lệnh giới hạn) chấp nhận rủi ro: nếu thông tin mới đến, lệnh của họ có thể bị khớp ở giá "sai". Vì vậy **trước và trong lúc có tin lớn**, nhiều người rút lệnh chờ hoặc đặt xa hơn. Sổ lệnh trở nên **mỏng**. Trong sổ lệnh mỏng, cùng một lượng lệnh thị trường làm giá đi xa hơn — và dễ tạo bước nhảy.

**[INTERPRETATION]** Đây là lý do gap hay xuất hiện quanh giờ tin và giờ mở phiên. Nhưng với một gap cụ thể, chart không cho biết sổ lệnh lúc đó dày hay mỏng.

### 7.4 Liquidity availability — Thanh khoản có sẵn ở đâu

**Ví dụ đời thường:** một cái chợ đông người bán cam (dễ mua nhiều mà giá không đổi) và một cái chợ chỉ có một người bán (mua nhiều là giá tăng ngay).

**[MARKET MECHANICS]** Thanh khoản không đều theo thời gian: đông vào giờ chính, thưa vào giờ lẻ, ngày lễ, cuối tuần. Gap trong giờ thanh khoản thưa **ít nói lên** về sự đồng thuận của thị trường hơn gap trong giờ đông người, vì có thể chỉ cần ít lệnh để tạo ra nó.

### 7.5 Aggressive vs passive — Lệnh chủ động và lệnh bị động

| | Lệnh chủ động (aggressive) | Lệnh bị động (passive) |
|---|---|---|
| Loại lệnh | Lệnh thị trường, hoặc lệnh giới hạn đặt xuyên qua giá đối diện | Lệnh giới hạn nằm chờ |
| Vai trò | **Lấy** thanh khoản, làm giá di chuyển | **Cung cấp** thanh khoản, làm giá đứng lại |
| Trong gap tăng | Người mua chủ động tìm người bán ở mức cao hơn | Người bán chờ ở mức cao hơn là "bậc thang" tiếp theo |

**Giới hạn:** chart nến không tách được lệnh chủ động/bị động. Cần dữ liệu khớp lệnh chi tiết (footprint, time & sales) — và kể cả vậy, ý định vẫn là diễn giải.

### 7.6 Auction dynamics — Đấu giá: thử, chấp nhận, từ chối

**[INTERPRETATION — khung Auction Market Theory]** Có thể nhìn thị trường như một cuộc đấu giá liên tục: giá đi lên để "tìm" người bán, đi xuống để "tìm" người mua. Khi giá đến một vùng mới:
- nếu giao dịch hai chiều tiếp diễn ở đó → **chấp nhận** (acceptance);
- nếu giá nhanh chóng bị đẩy về → **từ chối** (rejection).

Breakaway Gap thành công tương ứng với "chấp nhận ở vùng mới". Gap bị lấp và giá quay về range tương ứng với "từ chối". Đây là một **khung nhìn**, không phải một phép đo.

### 7.7 Participation và positioning — Ai đang đứng ở đâu khi gap xảy ra

**[INTERPRETATION]** Khi giá rời range bằng gap tăng, có thể có các nhóm sau (chart không cho biết tỷ lệ):

| Nhóm | Họ đang ở đâu | Phản ứng có thể có |
|---|---|---|
| Người bán khống ở biên trên | Đang lỗ | Mua để thoát (thêm lực mua) — hoặc giữ và chờ giá quay lại |
| Người mua trong range | Đang lời | Một phần chốt lời (thêm lực bán) |
| Người chờ breakout | Lệnh chờ đã khớp ở giá mở | Giữ, hoặc thoát nếu giá quay vào range |
| Người lỡ tàu | Chưa có vị thế | Chờ giá quay lại gần biên để mua (có thể tạo hỗ trợ) |
| Người phòng hộ (ví dụ bên bán quyền chọn) | Tùy vị thế | Có thể phải mua/bán theo hướng giá. **Không kiểm chứng được từ chart** |

Bài học: cùng một gap, các nhóm phản ứng theo nhiều hướng. **Kết quả sau gap phụ thuộc vào nhóm nào chiếm ưu thế — và điều đó chỉ thấy được qua hành vi giá SAU gap.**

---

## 8. Breakaway Gap Formation — Hình thành từng bước

![[BAG-v2-08-Bon-Giai-Doan-Hinh-Thanh.svg|960]]
*Hình BAG-v2-08 — Bốn giai đoạn. Giai đoạn 2 là phần chart không cho thấy. Giai đoạn 3 mới là "ứng viên". Giai đoạn 4 mới là bằng chứng.*

```text
GIAI ĐOẠN 1 — ĐI NGANG
   biên trên ──────────────────────────
               ║  ║   ║  ║   ║
                ║   ║   ║  ║
   biên dưới ──────────────────────────

GIAI ĐOẠN 2 — ĐIỀU KIỆN THAY ĐỔI  (tin / kỳ vọng / giờ nghỉ / lệnh chờ bị rút)
   → chart KHÔNG cho thấy gì ở giai đoạn này

GIAI ĐOẠN 3 — GIÁ ĐƯỢC ĐỊNH LẠI
                                        ║   ← nến đầu tiên nằm ngoài biên
                                        ║
                              ↑ GAP  (trên chart: không có giao dịch)
   biên trên ──────────────────────────
               ║  ║   ║  ║   ║

GIAI ĐOẠN 4 — ĐƯỢC CHẤP NHẬN (hay KHÔNG?)
                                        ║ ║  ║ ║   ← giá có tiếp tục giao dịch ở vùng mới?
                                        ║   ║
                              ↑ GAP
   biên trên ──────────────────────────
```

### Giai đoạn 1 — Đi ngang trong vùng

| Câu hỏi | Trả lời |
|---|---|
| Điều gì đang xảy ra? | Giá đi qua lại giữa hai biên. Mỗi lần chạm biên trên thì đi xuống, chạm biên dưới thì đi lên. |
| Vì sao? | Người mua và người bán tạm đồng ý về một khoảng "giá hợp lý". **[INTERPRETATION]** |
| Người tham gia phản ứng với gì? | Với chính hai biên: bán ở trên, mua ở dưới, đặt dừng lỗ ngoài biên. |
| Vai trò của thanh khoản | Lệnh chờ tập trung quanh biên (lệnh giới hạn bên trong, lệnh dừng lỗ bên ngoài). **[MARKET MECHANICS + INTERPRETATION]** |
| Vai trò của khớp lệnh | Khớp liên tục hai chiều ở nhiều mức trong vùng. |
| Quan sát được | Các đỉnh/đáy gần nhau; nhiều lần chạm cùng một vùng. **[QUAN SÁT]** |
| Chỉ là diễn giải | "Có người đang gom hàng / phân phối" — không thấy được trên chart. |

### Giai đoạn 2 — Điều kiện thay đổi

| Câu hỏi | Trả lời |
|---|---|
| Điều gì đang xảy ra? | Một điều gì đó làm thay đổi cái giá mà mọi người sẵn sàng giao dịch. |
| Vì sao? | Tin tức, dữ liệu kinh tế, kết quả kinh doanh, thay đổi kỳ vọng, hoặc đơn giản là thị trường đang đóng cửa trong lúc thông tin đến. |
| Người tham gia phản ứng với gì? | Với thông tin mới — và với phản ứng dự đoán của người khác. |
| Vai trò của thanh khoản | Người đặt lệnh chờ có thể rút lệnh vì không chắc chắn → sổ lệnh mỏng đi. **[MARKET MECHANICS]** |
| Vai trò của khớp lệnh | Nếu thị trường đóng cửa: không có khớp lệnh — lệnh tích tụ chờ phiên sau. |
| Quan sát được | **Thường không có gì trên chart.** Đây là phần vô hình. |
| Chỉ là diễn giải | Mọi câu chuyện về "vì sao" ở giai đoạn này. |

### Giai đoạn 3 — Giá được định lại (gap xuất hiện)

| Câu hỏi | Trả lời |
|---|---|
| Điều gì đang xảy ra? | Giao dịch đầu tiên (hoặc giá đấu giá mở cửa) xảy ra ở ngoài biên, không chạm vào nến trước. |
| Vì sao? | Tại giá cũ, lệnh mua nhiều hơn lệnh bán rất nhiều (gap tăng), nên điểm khớp phải ở mức cao hơn, nơi có đủ người bán. |
| Người tham gia phản ứng với gì? | Lệnh dừng lỗ của người bán khống và lệnh chờ breakout bị kích hoạt — nhưng khớp ở giá có sẵn (giá gap), không phải ở biên. |
| Vai trò của thanh khoản | Thanh khoản bị "dùng" ở vùng mới, không phải ở biên cũ. |
| Vai trò của khớp lệnh | Đấu giá mở cửa (cổ phiếu) hoặc lệnh thị trường ăn lệnh chờ ở các mức xa (thị trường liên tục). |
| Quan sát được | Một khoảng trống giữa hai nến; vị trí của nó so với biên. **[QUAN SÁT]** |
| Chỉ là diễn giải | "Breakout thật", "xu hướng mới bắt đầu" — CHƯA biết. |

### Giai đoạn 4 — Được chấp nhận ở vùng mới (hoặc không)

| Câu hỏi | Trả lời |
|---|---|
| Điều gì đang xảy ra? | Giá tiếp tục giao dịch ngoài biên, có thể đi tiếp, có thể quay lại thử gap. |
| Vì sao? | Ở vùng mới, vẫn có người mua sẵn sàng (giá giữ), hoặc không (giá quay về). |
| Người tham gia phản ứng với gì? | Với việc giá có giữ được không. Người lỡ tàu mua khi giá quay xuống; người mua sớm chốt lời. |
| Vai trò của thanh khoản | Giao dịch hai chiều xuất hiện ở vùng mới = "chấp nhận". |
| Vai trò của khớp lệnh | Khớp liên tục bình thường. |
| Quan sát được | Đóng cửa ở đâu, có follow-through không, có quay về range không. **[QUAN SÁT]** |
| Chỉ là diễn giải | "Breakaway đã xác nhận" là một **kết luận theo tiêu chí bạn đặt ra trước** — không phải sự thật tuyệt đối. |

---

## 9. Breakaway Gap Identification — Khung nhận diện

### 9.1 Bốn khối A → B → C → D

![[BAG-v2-13-Khung-Nhan-Dien-ABCD.svg|960]]
*Hình BAG-v2-13 — A và B biết ngay; C cần vài nến; D cần nhiều nến. Không nhảy từ B sang kết luận.*

#### A. Cấu trúc trước gap — biết TRƯỚC khi gap xảy ra

| Câu hỏi | Vì sao quan trọng |
|---|---|
| Giá đang đi ngang hay đang trend? | Breakaway cần một vùng để "rời bỏ". Gap giữa một nhịp đang chạy là ứng viên runaway hoặc exhaustion, không phải breakaway. |
| Có range / biên rõ không? | Không có biên rõ → không có gì để "phá". Biên phải đủ rõ để nhiều người cùng thấy. |
| Có hỗ trợ / kháng cự quan trọng không? | Gap qua một mức quan trọng có nhiều thông tin hơn gap qua một mức không ai để ý. |
| Có co hẹp (compression) trước đó không? | Biên độ co hẹp trước breakout là đặc điểm thường được nhắc trong TA — nhưng **tùy chọn**, không bắt buộc. |
| Biên được test nhiều lần chưa? | Nhiều lần test = nhiều người cùng nhìn thấy biên = nhiều lệnh tập trung quanh đó **[INTERPRETATION]**. |

#### B. Bản thân cái gap — biết ngay khi xuất hiện

| Câu hỏi | Vì sao quan trọng |
|---|---|
| Đo theo kiểu nào? | Full gap và opening gap cho kết quả khác nhau (§3.2). |
| Gap nằm ở đâu: trong hay ngoài biên? | Trong biên → common gap. Ngoài biên → ứng viên. |
| Có vượt qua swing high/low quan trọng không? | Vượt swing nội bộ ≠ vượt biên ngoài (§13.2). |
| Đủ rõ không? | Gap rất nhỏ trên chart có spread rộng có thể chỉ là nhiễu dữ liệu. |
| Có cần xuất hiện lúc mở phiên không? | **Không bắt buộc.** Opening gap là dạng phổ biến nhất ở cổ phiếu, nhưng bước nhảy trong phiên cũng có thể rời range. |
| Chart này có đúng phiên / nguồn không? | Gap có thể do cách vẽ (§16.6). |

#### C. Có phá cấu trúc thật không? — biết sau 1 đến vài nến

| Câu hỏi | Vì sao quan trọng |
|---|---|
| Giá ĐÓNG CỬA ngoài biên chưa? | Râu nến ra ngoài rồi đóng cửa trong range là một thông tin rất khác. |
| Có displacement không? | Nến mạnh, thân dài, đóng cửa gần đỉnh (gap tăng) cho thấy giá không bị từ chối ngay trong nến đó. Xem [[50-Displacement-In-Depth]]. |
| Có follow-through không? | Các nến tiếp theo đi tiếp theo hướng gap. |
| Giá có quay lại range không? | Quay lại và ở lại trong range → dấu hiệu thất bại. |

#### D. Hành vi sau gap — biết sau nhiều nến

| Kết quả | Thông tin |
|---|---|
| Tiếp tục mở rộng (expansion) | Ủng hộ breakaway |
| Quay lại test gap rồi giữ | Ủng hộ breakaway; vùng gap / biên cũ có phản ứng |
| Lấp một phần | Trung tính |
| Lấp hết nhưng giữ biên range | Trung tính → hơi ủng hộ (§12.4) |
| Lấy lại range (reclaim), đóng cửa và ở lại trong range | Breakout thất bại |
| Tạo vùng đi ngang mới ở vùng giá mới | Có thể là "chấp nhận" — vùng mới trở thành range mới |
| Đảo chiều mạnh | Thất bại; nếu đến cuối một nhịp dài, sau này có thể được gọi là exhaustion |

### 9.2 Bắt buộc, hỗ trợ, tùy chọn, gây nhầm

![[BAG-v2-14-Bat-Buoc-Ho-Tro-Tuy-Chon-Gay-Nham.svg|960]]
*Hình BAG-v2-14 — Chỉ cột 1 là định nghĩa. Các cột còn lại là bằng chứng hoặc nhiễu.*

| Nhóm | Đặc điểm | Ghi chú |
|---|---|---|
| **Bắt buộc** (theo định nghĩa) | Có price gap thật theo cách đo đã ghi; có vùng/cấu trúc xác định trước gap; gap đưa giá ra ngoài biên | Thiếu một trong ba → không phải breakaway |
| **Bằng chứng hỗ trợ** | Đóng cửa ngoài biên; follow-through; không quay lại range; volume tăng (ở thị trường có volume tập trung); bối cảnh khung lớn không chống lại | StockCharts: volume "nên" tăng rõ; và tốt hơn nếu volume tăng **sau** gap |
| **Tùy chọn** | Biên test nhiều lần; co hẹp trước đó; xảy ra lúc mở phiên; có tin giải thích được | Có thì thêm thông tin, không có vẫn có thể là breakaway |
| **Gây nhầm** | Gap rất to; một nến rất dài; gap chỉ có trên một feed; gap trong vài phút đầu sau tin lớn; gọi tên sau khi thấy cả nhịp | Trông "mạnh" nhưng không chứng minh gì |

> [!warning] Đừng biến đặc điểm thường gặp thành điều kiện bắt buộc
> "Volume cao" thường đi kèm breakaway gap trong các ví dụ cổ phiếu, nhưng (1) Forex giao ngay không có volume tập trung, (2) volume của broker chỉ là số tick. Biến volume thành điều kiện bắt buộc sẽ làm khái niệm không dùng được ở Forex.

---

## 10. Bullish vs Bearish Breakaway Gap — và các bối cảnh

### 10.1 Bullish Breakaway Gap

![[BAG-v2-11-Giai-Phau-Bullish.svg|960]]
*Hình BAG-v2-11 — Vùng cũ, biên bị rời bỏ, mép xa, mép gần, và hành vi sau gap.*

| Thành phần | Mô tả |
|---|---|
| **Điều kiện trước** | Một vùng đi ngang / kháng cự rõ, xác định được trước gap |
| **Cách gap xuất hiện** | Nến mới có giá thấp nhất cao hơn giá cao nhất của nến trước, và nằm trên biên trên |
| **Cấu trúc bị phá** | Biên trên của range (và mọi đỉnh nằm trong range) |
| **Mép xa** (far edge) | High của nến cuối trước gap. Giá quay về tới đây = lấp hết |
| **Mép gần** (near edge) | Low của nến đầu tiên sau gap. Giá quay xuống qua đây = bắt đầu lấp |
| **Ý nghĩa bullish** | Nếu giá được chấp nhận ở trên: range cũ thành vùng giá "phía dưới"; thanh khoản phía trên trở thành mục tiêu tiềm năng |
| **Tình huống thất bại** | Giá đóng cửa lại dưới biên trên và ở lại trong range; gap đến cuối một nhịp tăng dài rồi giá đảo chiều; gap trong giờ thanh khoản mỏng bị lấp khi thanh khoản trở lại |

### 10.2 Bearish Breakaway Gap

![[BAG-v2-12-Giai-Phau-Bearish.svg|960]]
*Hình BAG-v2-12 — Phiên bản đảo chiều: mọi nguyên tắc giống hệt, chỉ đảo hướng.*

Mọi thứ đảo ngược: nến mới có giá cao nhất **thấp hơn** giá thấp nhất của nến trước, nằm **dưới** biên dưới. Mép xa = low nến cuối trước gap; mép gần = high nến đầu sau gap. Thất bại khi giá đóng cửa lại **trên** biên dưới và ở lại trong range.

**Một khác biệt thực tế [INTERPRETATION]:** ở nhiều thị trường, các cú giảm thường nhanh hơn các cú tăng (người ta bán vội khi sợ). Gap giảm có thể đi kèm biến động lớn hơn và hồi lại mạnh hơn. Đây là quan sát phổ biến, cần kiểm tra trên thị trường của bạn.

### 10.3 Ba bối cảnh thường gặp

![[BAG-v2-15-Ba-Boi-Canh-Breakaway.svg|960]]
*Hình BAG-v2-15 — Rời vùng tích lũy, vượt kháng cự lớn, và gap trong quá trình đảo chiều.*

| Bối cảnh | Mô tả | Có phải breakaway "chuẩn"? |
|---|---|---|
| **Rời vùng tích lũy** | Hộp đi ngang rõ, gap ra ngoài | Dạng sách giáo khoa |
| **Vượt hỗ trợ / kháng cự lớn** | Một mức được test nhiều lần trong một xu hướng, gap vượt qua | Có, nếu mức đó đóng vai trò biên của một vùng giao dịch |
| **Trong quá trình đảo chiều** | Sau một xu hướng giảm, giá tạo đáy rồi gap tăng vượt đỉnh thấp dần gần nhất | **Phụ thuộc.** Nếu có vùng tạo đáy đi ngang để rời khỏi → hợp lý gọi là breakaway. Nếu không có vùng, đó là "gap trong đảo chiều" — cần tên riêng và kiểm chứng riêng; có thể là một phần của island reversal |

> [!note] Ghi rõ đây là khung nghiên cứu
> Ba bối cảnh trên là cách phân nhóm của note này để học, **không phải** một phân loại chính thức trong tài liệu TA. TA cổ điển chỉ chính thức phân loại theo vị trí: common, breakaway, runaway, exhaustion (và mô hình island reversal).

---

## 11. Breakaway Gap vs Other Gap Types — So sánh với các loại gap khác

### 11.1 Ví dụ đơn giản trước: một chuyến tàu

- **Common gap** — tàu đang đứng trong ga, lắc nhẹ một cái. Vẫn trong ga.
- **Breakaway gap** — tàu **rời ga**. Bắt đầu chuyến đi.
- **Runaway gap** — tàu đang chạy giữa đường, **tăng tốc** thêm một đoạn.
- **Exhaustion gap** — tàu **lao vào ga cuối**, rất nhanh, rồi phanh gấp và dừng (hoặc lùi lại).

Lúc bạn chỉ thấy một cú giật mạnh của toa tàu, bạn không biết đó là rời ga, tăng tốc, hay lao vào ga cuối. Bạn cần biết **tàu đã ở đâu trước đó** và **sau đó tàu làm gì**.

### 11.2 Vị trí trên một nhịp giá

![[BAG-v2-10-Vi-Tri-Cac-Loai-Gap.svg|960]]
*Hình BAG-v2-10 — Bốn loại gap cổ điển trên cùng một chuỗi. Tên gọi chỉ rõ khi nhìn lại toàn bộ.*

### 11.3 Bảng so sánh chuyên môn

| Đặc điểm | Common Gap | Breakaway Gap | Runaway Gap | Exhaustion Gap |
|---|---|---|---|---|
| **Vị trí điển hình** | Trong vùng đi ngang | Ngay khi rời vùng đi ngang / mức quan trọng | Giữa một nhịp đang chạy | Gần cuối một nhịp dài |
| **Điều kiện thị trường** | Không có hướng rõ | Chuyển từ đi ngang sang có hướng | Đang có hướng mạnh | Nhịp đã đi xa, thường rất nhanh ở đoạn cuối |
| **Ý nghĩa cấu trúc** | Gần như không có | Rời khỏi một cấu trúc | Tiếp diễn cấu trúc hiện có | Có thể là đoạn cuối của cấu trúc hiện có |
| **Quan hệ với xu hướng** | Không | Có thể là điểm bắt đầu | Ở giữa | Có thể là điểm kết thúc |
| **Hành vi điển hình** (theo nguồn TA) | Lấp nhanh, không tạo đỉnh/đáy mới | Không lấp nhanh; giá đi tiếp | Giá tạo đỉnh/đáy mới mà không lấp | Lấp nhanh rồi đi ngang hoặc đảo chiều |
| **Lấp gap** (theo Bulkowski, cổ phiếu, thị trường tăng) | Thường lấp trong vài ngày | Hiếm khi lấp trong tuần đầu; lấp thì thường sau nhiều tháng | Lấp chậm hơn common, nhanh hơn breakaway | Thường lấp trong khoảng một tuần |
| **Hàm ý tiềm năng** | Ít thông tin | Bối cảnh mới có thể đã hình thành | Nhịp còn đang chạy | Cảnh báo nhịp có thể sắp dừng |

### 11.4 Những câu hỏi then chốt

**Vì sao Breakaway khác Common?** Vì vị trí: common nằm **trong** vùng, breakaway đưa giá **ra khỏi** vùng. Common gap không thay đổi khung tham chiếu; breakaway có thể thay đổi.

**Vì sao Breakaway khác Runaway?** Vì thứ đứng trước gap: breakaway đến sau một vùng đi ngang; runaway đến khi giá **đã đang chạy**, không có vùng tích lũy ngay trước đó.

**Vì sao không thể phân loại chỉ bằng kích thước?** Vì kích thước phụ thuộc vào thị trường, khung thời gian, mức biến động lúc đó, và cách đo. Một gap "to" trong giờ thanh khoản mỏng có thể ít ý nghĩa hơn một gap "nhỏ" rời một vùng tích lũy rõ ràng. Không nguồn TA nào định nghĩa loại gap bằng kích thước.

**Vì sao Exhaustion có thể trông giống Breakaway lúc đầu?** Cả hai đều là một gap mạnh theo hướng nhịp. Bulkowski đưa ra một ví dụ mơ hồ đúng như vậy: một gap "có thể là exhaustion gap vì giá ngừng tăng; tuy nhiên gap hình thành khi giá rời một vùng tích lũy". Điểm khác duy nhất có thể biết **trước**: exhaustion đến **sau một nhịp đã chạy dài**, không đến ngay sau một vùng đi ngang.

**Phân biệt bằng chuỗi giá sau gap như thế nào?**

| Sau gap | Ủng hộ |
|---|---|
| Đi tiếp, gap không bị lấp, giá giữ ngoài vùng | Breakaway (nếu trước đó có vùng) / Runaway (nếu trước đó đang chạy) |
| Lấp nhanh, giá đứng lại hoặc đảo chiều | Exhaustion (nếu trước đó nhịp đã dài) / Breakout thất bại (nếu trước đó là range) |
| Lấp nhanh, giá ở lại trong vùng | Common gap |

### 11.5 Không phân loại được ngay — và điều đó bình thường

![[BAG-v2-16-Mot-Gap-Ba-Tuong-Lai.svg|960]]
*Hình BAG-v2-16 — Phần bên trái giống hệt nhau. Ba tương lai khác nhau. Tại T0, cả ba đều có thể.*

> [!important]
> **Tại thời điểm gap xuất hiện, không thể phân loại chắc chắn.** Câu trả lời đúng ở T0 là "ứng viên", hoặc "chưa rõ". Đây không phải điểm yếu của người phân tích — đây là bản chất của khái niệm.

---

## 12. Gap Filling — Vì sao giá quay lại lấp gap?

### 12.1 Sáu bước để hiểu "lấp gap"

**① Ví dụ đời thường:** gia đình đã chuyển sang nhà mới (§5.1). Một hôm họ quay về nhà cũ lấy đồ. **Quay về lấy đồ không có nghĩa là chuyển về ở lại.** Chỉ khi họ dọn đồ về nhà cũ và sống ở đó nhiều ngày mới là "chuyển về".

**② Điều gì xảy ra trên thị trường [QUAN SÁT]:** sau gap, giá quay ngược lại và giao dịch ở vùng giá mà trước đó không có giao dịch.

**③ Vì sao [INTERPRETATION]:** ở các mức thấp hơn (với gap tăng) có người bán chủ động và thiếu người mua mới (§12.3).

**④ Giải thích chuyên môn [TECHNICAL ANALYSIS]:** StockCharts định nghĩa gap "được lấp" khi giá quay lại ít nhất tới mức của ngày cuối cùng trước gap. Bulkowski: lấp gap là khi giá đi vào "che phủ khoảng trống".

**⑤ Ý nghĩa thực tế:** lấp gap là một **sự kiện hình học**. Ý nghĩa của nó phụ thuộc vào việc giá làm gì **sau khi** lấp — đặc biệt là đóng cửa ở đâu so với biên range cũ.

**⑥ Giới hạn:** "gap nào cũng sẽ được lấp" là **[UNCONFIRMED CLAIM]**. StockCharts viết: câu "mọi gap rồi sẽ được lấp" có thể không đúng, "đặc biệt với breakaway gap và runaway gap", và cảnh báo rằng chờ breakaway gap lấp có thể "tàn phá danh mục". Nghiên cứu của Plastun và cộng sự (2020) trên chỉ số chứng khoán Mỹ giai đoạn 1928–2018 kết luận kết quả của họ "trái với huyền thoại rằng gap có xu hướng được lấp".

### 12.2 Bốn kiểu quay lại

![[BAG-v2-17-Bon-Kieu-Quay-Lai-Gap.svg|960]]
*Hình BAG-v2-17 — Mỗi kiểu nói lên một điều và KHÔNG nói lên một điều khác.*

| Kiểu | Định nghĩa | Nói lên | KHÔNG nói lên |
|---|---|---|---|
| **Partial fill** (lấp một phần) | Giá đi vào trong gap nhưng không tới mép xa | Ở vùng đó có người bán đủ để kéo giá vào | Gap "mạnh" hay "yếu" |
| **Full fill** (lấp hết) | Giá chạm hoặc vượt qua mép xa | Khoảng trống không còn | Breakout thất bại |
| **Gap rejection** (bị từ chối) | Giá vào vùng gap rồi bật mạnh theo hướng cũ | Ở vùng đó có người mua phản ứng | Lần sau cũng sẽ bật |
| **Gap acceptance** (được chấp nhận) | Giá giao dịch và **đóng cửa** trong gap hoặc phía bên kia, và ở lại | Thị trường chấp nhận giao dịch lại ở vùng cũ | — đây là bằng chứng gần nhất với "thất bại", nhưng vẫn cần biên range xác nhận |

> [!important] "Lấp" phải được định nghĩa trước
> Lấp bằng **râu nến** hay bằng **giá đóng cửa**? Trên **khung nào**? Tới **mép xa** hay tới **biên range**? Ghi định nghĩa ra trước khi xem chart. Nếu không, bạn sẽ chọn định nghĩa nào hợp với kết quả bạn muốn.

### 12.3 Vì sao giá quay lại?

![[BAG-v2-18-Vi-Sao-Gia-Quay-Lai-Gap.svg|960]]
*Hình BAG-v2-18 — Không có "lực hút" bí ẩn. Giá chỉ quay lại khi ở dưới có người bán chủ động và thiếu người mua mới.*

**[MARKET MECHANICS]** Để giá đi xuống lại vùng gap, phải có giao dịch ở đó — tức là có người bán chấp nhận bán ở giá thấp hơn, và người mua ở giá cao hơn đã không còn đủ. Bốn lý do thường được đưa ra (đều là **[INTERPRETATION]**):

1. **Người mua sớm chốt lời** — người mua trong range đang lời, một phần bán ra.
2. **Lực mua "một lần" đã dùng hết** — lệnh dồn qua đêm và lệnh dừng lỗ của người bán khống chỉ khớp một lần lúc mở cửa. Sau đó, người mua mới ở giá cao có thể không còn nhiều.
3. **Thông tin được đánh giá lại** — sau phản ứng đầu tiên, nhiều người đọc lại tin và thấy giá đi quá đà.
4. **Lệnh chờ ở vùng giá cũ** — người lỡ tàu đặt lệnh mua chờ quanh biên cũ. Khi giá xuống, đó là nơi CÓ người mua — giá có thể dừng lại ở đó.

Lý do số 4 cũng là cách giải thích vì sao **lấp một phần** hay xảy ra: giá xuống tới nơi có lệnh mua chờ thì dừng, chưa cần tới mép xa.

### 12.4 Lấp gap ≠ breakout thất bại

![[BAG-v2-19-Lap-Gap-Khong-Phai-That-Bai.svg|960]]
*Hình BAG-v2-19 — Hai kịch bản đều lấp hết gap. Chỉ một là thất bại. Đường quyết định là biên range, không phải mép gap.*

| | Lấp gap | Breakout thất bại |
|---|---|---|
| Định nghĩa | Giá quay về tới mép xa của gap | Giá đóng cửa trở lại trong range và ở lại đó (theo tiêu chí bạn ghi trước) |
| Đường tham chiếu | Mép xa của gap | **Biên của range cũ** |
| Có thể xảy ra mà không có cái kia? | Có: lấp gap nhưng giữ trên biên | Có, nhưng hiếm: nếu mép xa của gap nằm trên biên range, giá phải lấp gap trước rồi mới vào được range |

**Có trường hợp lấp gap mà xu hướng vẫn tiếp tục không?** Có — rất thường. Xem §22.3 (năm ví dụ).

**Có trường hợp gap KHÔNG bị lấp mà giá vẫn đảo chiều không?** Có. Hai ví dụ:
- **Island reversal [TECHNICAL ANALYSIS]:** giá gap tăng, đi ngang vài phiên, rồi **gap giảm** xuống dưới. Cú gap giảm nhảy qua chính vùng gap cũ — vùng đó vẫn chưa có giao dịch, nhưng xu hướng đã đảo.
- **Đảo chiều trên khung nhỏ trước khi về tới gap:** giá tạo đỉnh, các khung nhỏ chuyển sang giảm, nhưng gap D1 nằm quá xa bên dưới. Nhịp tăng đã kết thúc dù gap chưa được chạm.

### 12.5 Gap fill không phải là tín hiệu độc lập

"Giá đã lấp gap → mua" hay "giá chưa lấp gap → sẽ quay lại lấp → bán" đều là **cách dùng gap như một tín hiệu đơn lẻ**. Không có cơ sở cho cả hai. Lấp gap chỉ cho bạn biết **giá đang ở đâu so với một vùng tham chiếu**. Quyết định giao dịch vẫn phải đi qua bối cảnh D1, setup H1, và xác nhận M5 (§21).

---

## 13. Breakaway Gap + Market Structure

### 13.1 Câu hỏi trung tâm: gap có "mạnh hơn" một breakout bình thường không?

**Câu trả lời ngắn: nó là một LOẠI bằng chứng khác, không tự động mạnh hơn.**

- **Điều gap cho thêm:** trên chart đó, giá đã đổi vùng **mà không giao dịch ở giữa**. Đó là dấu hiệu của một lần định giá lại nhanh **[MARKET MECHANICS]**. Bulkowski ghi nhận trong dữ liệu cổ phiếu của ông rằng các mẫu hình có gap ngay ngày breakout thường cho kết quả tốt hơn — một quan sát **có điều kiện** (cổ phiếu, cách đo của ông), không phải luật chung.
- **Điều gap lấy đi:** giá chưa từng giao dịch ở các mức giữa. Không có "thử" biên, không có giao dịch hai chiều ở đó. Một số người cho rằng vì thế vùng gap là nơi hỗ trợ yếu — Bulkowski gọi gap là nơi hỗ trợ/kháng cự **yếu**.
- **Kết luận:** một gap rời range là một bằng chứng **về tốc độ** định giá lại. Nó **không** thay thế bằng chứng về **sự chấp nhận** (follow-through, đóng cửa ngoài biên, không reclaim).

### 13.2 Ba cấp: khoảng trống → phá cấu trúc → mở rộng có hướng

![[BAG-v2-20-Ba-Cap-Bang-Chung.svg|960]]
*Hình BAG-v2-20 — Mỗi cấp cần thêm thông tin. Cấp dưới không suy ra cấp trên.*

| Cấp | Tên | Biết khi nào | Ví dụ không đạt cấp tiếp theo |
|---|---|---|---|
| 1 | **Price discontinuity** | Ngay khi nến mở | Gap nằm trong range (common gap) |
| 2 | **Structural break** | Khi nến đóng cửa ngoài một biên có ý nghĩa | Đóng cửa ngoài biên nhưng sau đó đi ngang sát gap rồi quay về |
| 3 | **Confirmed directional expansion** | Sau nhiều nến | — |

> [!warning] Đừng đồng nhất ba thứ này
> "Có gap" ≠ "đã phá cấu trúc" ≠ "xu hướng mới đã bắt đầu". Mỗi bước cần thêm nến và thêm bằng chứng.

### 13.3 Gap vượt cấu trúc nội bộ hay cấu trúc ngoài?

![[BAG-v2-21-Internal-vs-External.svg|960]]
*Hình BAG-v2-21 — Gap vượt đỉnh nội bộ (vẫn trong range lớn) khác hẳn gap vượt biên ngoài.*

| Trường hợp | Ý nghĩa |
|---|---|
| **Gap vượt swing nội bộ** (internal structure) | Thông tin hạn chế. Giá vẫn ở trong khung giao dịch lớn hơn; biên ngoài còn nguyên phía trên. Dễ là gap trong range. |
| **Gap vượt biên ngoài** (external range high/low) | Giá rời toàn bộ khung giao dịch cũ. Đây là bối cảnh của breakaway theo định nghĩa cổ điển. |
| **Gap phá range high** | Bullish breakaway candidate. Đường cần theo dõi: range high. |
| **Gap phá range low** | Bearish breakaway candidate. Đường cần theo dõi: range low. |

Xem [[16-Internal-External-Range-Liquidity-IRL-ERL]] và [[12-Dealing-Range]] để xác định biên nào là "ngoài".

### 13.4 Quan hệ với BOS, MSS / CHoCH

| Tình huống | Có thể gọi là | Ghi chú |
|---|---|---|
| Xu hướng tăng → đi ngang → gap tăng rời range | Breakaway gap + **BOS** tiếp diễn | Xem [[05-BOS-Break-of-Structure]] |
| Xu hướng giảm → vùng tạo đáy → gap tăng vượt đỉnh thấp dần gần nhất | Gap + **MSS / CHoCH** tiềm năng | Xem [[21-Market-Structure-Shift]], [[09-Change-of-Character]]. Vẫn cần follow-through |
| Gap vượt một đỉnh nhỏ trong range | Không phải BOS của khung lớn | Có thể là BOS của khung nhỏ |

Gap **không** tự động là BOS hay MSS. BOS/MSS được định nghĩa bằng việc **đóng cửa** vượt một swing có ý nghĩa; gap chỉ là cách giá đi qua swing đó.

### 13.5 Khi cấu trúc chưa rõ, và khi không có follow-through

- **Gap khi cấu trúc chưa rõ:** không có vùng/biên xác định trước → không có gì để "breakaway". Gọi nó là "gap" và ghi lại vị trí. Đừng đặt tên sau khi biết kết quả.
- **Gap không có follow-through:** giá giữ ngoài biên nhưng đi ngang sát gap. Chưa thất bại, chưa xác nhận. Trạng thái đúng là "đang chờ thông tin". Nếu giá tạo một vùng đi ngang mới ở đó, vùng mới đó có thể trở thành range mới — breakaway tiếp theo (nếu có) sẽ là rời khỏi vùng mới này.

---

## 14. Breakaway Gap + Liquidity

### 14.1 Gap hình thành khi giá vượt qua vùng thanh khoản như thế nào?

![[BAG-v2-22-Gap-va-Thanh-Khoan.svg|960]]
*Hình BAG-v2-22 — Lệnh chờ trên đỉnh bằng nhau bị kích hoạt khi giá mở cửa vượt qua — và khớp ở giá mở, không phải ở mức kích hoạt.*

**Ví dụ đời thường:** nhiều người hẹn nhau "khi giá cam lên tới 11 thì tôi mua". Sáng nay giá mở thẳng ở 12. Tất cả những lời hẹn đó được thực hiện ở 12 — không ai mua được ở 11.

**[MARKET MECHANICS]** Phía trên các đỉnh bằng nhau (equal highs) hoặc một swing high rõ, thường có:
- lệnh dừng lỗ của người bán khống (khi kích hoạt → thành lệnh **mua** thị trường),
- lệnh mua chờ breakout (buy stop).

ICT gọi vùng này là **buy-side liquidity (BSL)**; phía dưới đáy là **sell-side liquidity (SSL)**. Xem [[19-Liquidity]].

Khi giá **mở cửa vượt qua** mức đó bằng gap, các lệnh dừng (stop) bị kích hoạt nhưng **khớp ở giá có sẵn lúc đó** — quanh giá mở cửa hoặc tệ hơn. Đó là **trượt giá** (slippage). Lực mua từ các lệnh này góp vào cú đẩy lúc mở cửa — và là lực **"một lần"**: sau khi chúng khớp, không còn ai phải mua vì cùng lý do đó **[INTERPRETATION]**.

### 14.2 Những câu hỏi về liquidity

| Câu hỏi | Trả lời |
|---|---|
| Mọi breakaway gap có liên quan đến liquidity sweep không? | **Không.** "Sweep" nghĩa là giá vượt qua một đỉnh/đáy rồi **quay ngược lại**. Breakaway nghĩa là giá vượt qua rồi **ở lại**. Một gap vượt đỉnh rồi bị đảo ngược là kịch bản sweep/thất bại, không phải breakaway. Xem [[20-Liquidity-Sweep]]. |
| Có phải luôn có thanh khoản ở hai phía của gap? | Không nhất thiết. Sau gap tăng, phía trên có thể có các đỉnh cũ của khung lớn (BSL); phía dưới có biên range và các lệnh dừng của người vừa mua. Nhưng "có" hay "không" phải được xác định bằng các swing cụ thể, không mặc định. |
| Gap có tạo ra liquidity void không? | Gap là trường hợp cực đoan của "vùng không có giao dịch trên chart". Trong vault, [[21-Liquidity-Void]] thường chỉ một đoạn giá **dài, nhiều nến**, đi một chiều. Một gap có thể **nằm trong** một liquidity void lớn hơn (ví dụ gap mở cửa rồi tiếp tục chạy mạnh nhiều nến). |
| Gap có thể phá một vùng thanh khoản quan trọng không? | Có — như ví dụ BSL ở trên. Nhưng "thanh khoản đã bị lấy" chỉ có nghĩa là **giá đã giao dịch qua mức đó**. Chart không cho biết bao nhiêu lệnh thật sự có ở đó. |
| Gap có thể đơn giản là thị trường chuyển sang vùng giá mới? | Có — và đây là cách mô tả trung lập nhất. Không cần câu chuyện "săn thanh khoản" để giải thích một gap. |

### 14.3 Năm khái niệm không được dùng thay cho nhau

![[BAG-v2-23-Nam-Khai-Niem-De-Lan.svg|960]]
*Hình BAG-v2-23 — Gap, Liquidity Void, FVG, Liquidity Sweep, Displacement: năm câu hỏi khác nhau.*

| Khái niệm | Câu hỏi nó trả lời | Đo bằng | Có thể có mà không có gap? |
|---|---|---|---|
| **Gap** | Hai nến liền kề có phần giá chung không? | High/low (hoặc close/open) | — |
| **Liquidity Void** | Có đoạn giá dài nào đi qua rất nhanh, một chiều? | Độ dài đoạn ít giao dịch hai chiều | Có |
| **FVG** | Có vùng nào chỉ nến giữa của 3 nến đi qua? | High nến 1 ↔ low nến 3 | Có |
| **Liquidity Sweep** | Giá có vượt một đỉnh/đáy rõ rồi quay ngược không? | Vượt mức + quay lại | Có |
| **Displacement** | Chuyển động có nhanh, dứt khoát so với bình thường không? | Thân nến, đóng cửa, so với biên độ thường | Có |

---

## 15. Breakaway Gap + ICT Concepts

> [!note] Nguyên tắc
> Breakaway Gap là khái niệm TA cổ điển. Phần này hỏi: nó **liên quan** thế nào với các khái niệm ICT. Không phải mọi breakaway gap đều phải gắn với một khái niệm ICT. Nếu không có quan hệ trực tiếp, note sẽ nói rõ.

### 15.1 Displacement

![[BAG-v2-26-Gap-Displacement-OB.svg|960]]
*Hình BAG-v2-26 — Displacement không cần gap; gap không chứng minh displacement; gap không định nghĩa Order Block.*

| Câu hỏi | Trả lời |
|---|---|
| Breakaway gap có luôn đi kèm displacement không? | **Không bắt buộc.** Gap có thể xuất hiện rồi các nến sau nhỏ và đuối. Nhưng một breakaway gap được **xác nhận** thường có các nến sau đi tiếp mạnh — tức là có displacement **sau** gap. |
| Displacement có thể xuất hiện mà không có gap không? | **Có, rất thường** — nhất là ở thị trường giao dịch liên tục (FX, futures trong phiên). Nến thân dài nối tiếp nhau, đi qua mọi mức. |
| Khác nhau ở đâu? | Gap là **hình học giữa hai nến**. Displacement là **tính chất của chuyển động** (tốc độ, thân nến, đóng cửa). Xem [[50-Displacement-In-Depth]]. |

### 15.2 Fair Value Gap

![[BAG-v2-24-Breakaway-Gap-vs-FVG.svg|960]]
*Hình BAG-v2-24 — Gap thật không có FVG, FVG không có gap thật, và cả hai cùng lúc.*

**Ví dụ đời thường:** gap giống như **hai bậc thang không có bậc ở giữa** — không ai đứng ở đó. FVG giống như **một đoạn cầu thang mà chỉ có một người chạy vụt qua**, không ai đi lên đi xuống thêm lần nào. Đoạn cầu thang FVG có người đi qua (có giao dịch), chỉ là đi qua rất nhanh và một chiều.

| Câu hỏi | Trả lời |
|---|---|
| Breakaway gap có thể chứa FVG không? | Có. Nếu gap đi kèm nến mạnh, mẫu 3 nến quanh gap thường tạo FVG, và **vùng gap nằm bên trong FVG**. |
| FVG có thể xuất hiện sau breakaway gap không? | Có — trong các nến follow-through. Trên khung nhỏ, các FVG đó là nơi ICT tìm entry tiếp diễn. |
| Có thể cùng xuất hiện trong một chuỗi giá không? | Có (hình 24, ô 3). |
| Cơ chế và ý nghĩa khác nhau thế nào? | Gap: không có giao dịch trên chart trong khoảng đó (thường do phiên/đấu giá/sổ lệnh trống). FVG: có giao dịch, nhưng chỉ một chiều trong một nến. Gap nói về **cách giá đổi vùng**; FVG được ICT dùng như **tham chiếu vị trí**. |

### 15.3 Order Block

| Câu hỏi | Trả lời |
|---|---|
| Breakaway gap có thể xuất hiện sau khi giá rời OB không? | Có. Một cú rời OB nhanh có thể đi kèm gap (đặc biệt nếu đi qua giờ mở phiên). |
| Gap có giúp đánh giá sức mạnh của move rời OB? | Gap **mô tả tốc độ**. Nó là một chi tiết, không phải thước đo chất lượng OB. |
| Có nên dùng gap để xác định OB không? | **Không.** OB được định nghĩa bằng cấu trúc + displacement + bối cảnh. Xem [[25-OB-Order-Block]]. |

### 15.4 Breaker Block / Mitigation Block

**[ICT FRAMEWORK]** Breaker và mitigation block là các vùng cấu trúc cũ mà giá đã phá qua. Một breakaway gap có thể **chính là cách** giá phá qua một vùng như vậy (ví dụ gap tăng qua một OB giảm cũ, biến nó thành breaker tiềm năng). Trong cách dùng của cộng đồng ICT (§5.3), breaker/iFVG/BPR được mô tả là "cơ chế giữ giá" bên dưới một FVG không bị quay lại.

**Giới hạn:** quan hệ này là **cách diễn giải**. Không có nguồn ICT gốc nào trong lần nghiên cứu này định nghĩa breakaway gap qua breaker. Xem [[04-Breaker-Block]], [[22-Mitigation-Block]], [[17-Inverse-Fair-Value-Gap-iFVG]], [[03-Balanced-Price-Range]].

### 15.5 Imbalance

| | Imbalance trong đấu giá / sổ lệnh | "Imbalance" trong ICT |
|---|---|---|
| Nghĩa | Ở một mức giá cụ thể, lượng lệnh mua khác lượng lệnh bán (ví dụ NOII của Nasdaq trước giờ mở cửa) | Tên gọi cho vùng giá đi nhanh một chiều (thường là FVG / BISI / SIBI) |
| Đo được không? | Có, nếu có dữ liệu sổ lệnh / đấu giá | Đo hình học trên nến; còn "mất cân bằng" là diễn giải |
| Quan hệ với gap | Gap mở cửa có thể là kết quả của imbalance trong đấu giá | Gap thường được gọi là imbalance — nhưng đó là **cách gọi**, không phải phép đo lệnh |

**Gap có đồng nghĩa với imbalance không?** Không. "Mọi gap là imbalance" là **[UNCONFIRMED CLAIM]** (§18). Một gap do giờ nghỉ của sàn, do đổi hợp đồng futures, hay do giờ đóng nến khác nhau không nói gì về sự mất cân bằng giữa người mua và người bán. Xem [[29-Sell-side-Imbalance-Buy-side-Inefficiency]].

---

## 16. Breakaway Gap Across Different Markets

### 16.1 Giờ giao dịch quyết định gap xuất hiện ở đâu

![[BAG-v2-27-Gio-Giao-Dich-va-Noi-Gap-Xuat-Hien.svg|960]]
*Hình BAG-v2-27 — Sơ đồ một tuần (giản lược). Khoảng trắng = không có khớp lệnh liên tục → nơi gap có thể hình thành. Giờ cụ thể phải kiểm tra theo lịch chính thức của sàn/broker.*

| Thị trường | Cấu trúc | Gap thật xuất hiện khi nào | Ghi chú cho Breakaway Gap |
|---|---|---|---|
| **Cổ phiếu** | Sàn tập trung; giờ chính thức + giờ mở rộng; đấu giá mở cửa | Mỗi sáng (qua đêm), sau cuối tuần, sau tin ngoài giờ | Nơi khái niệm ra đời. Gap D1 thường xuyên. Phải chú ý giờ mở rộng |
| **Futures** (chỉ số, hàng hóa) | Sàn tập trung; giao dịch gần như liên tục, có giờ nghỉ hằng ngày và cuối tuần (CME ghi rõ giờ có thể thay đổi) | Sau giờ nghỉ hằng ngày (thường nhỏ), sau cuối tuần, khi đổi hợp đồng (trên chart nối liên tục) | Gap D1 ít hơn cổ phiếu nhiều. ICT dùng chính các gap này cho NDOG/NWOG |
| **Chỉ số tiền mặt** (cash index) | Tính từ giá cổ phiếu thành phần, chỉ trong giờ cổ phiếu | Mỗi sáng | Gap trên cash index có thể không có trên futures cùng chỉ số |
| **Forex giao ngay** | OTC phi tập trung, gần như 24/5, không có sổ lệnh chung | Chủ yếu cuối tuần; khi có cú sốc; quanh giờ rollover (spread giãn) | Gap thật hiếm; "breakaway" thường là phá range liên tục |
| **Hàng hóa CFD** (ví dụ XAUUSD) | Theo nguồn của broker, thường bám futures/thị trường OTC | Cuối tuần, giờ nghỉ hằng ngày của broker | Kiểm tra feed |
| **Crypto spot** | Nhiều sàn, giao dịch 24/7 | Gần như không có trên chart spot | Futures crypto của CME có giờ nghỉ → có "CME gap" trên chart futures |

### 16.2 Vì sao cổ phiếu hay có gap qua đêm?

Vì sàn đóng cửa mỗi đêm (giờ mở rộng có thanh khoản thấp), và tin của doanh nghiệp thường được công bố ngoài giờ chính thức — SEC ghi rõ điều này trong bản tin về giao dịch ngoài giờ. Sáng hôm sau, đấu giá mở cửa phản ánh toàn bộ thông tin trong một lần (§4.3).

### 16.3 Vì sao futures có session gap?

Futures chỉ số và hàng hóa trên CME Globex giao dịch gần như liên tục nhưng có **giờ nghỉ hằng ngày** và **nghỉ cuối tuần**. Mỗi lần mở lại, giá có thể khác giá trước khi nghỉ → gap. Gap hằng ngày thường nhỏ vì giờ nghỉ ngắn; gap cuối tuần có thể lớn. Xem [[23-New-Day-Opening-Gap]], [[24-New-Week-Opening-Gap]].

### 16.4 Forex — đừng dùng logic cổ phiếu

![[BAG-v2-28-Forex-Gap-Thuc-Te.svg|960]]
*Hình BAG-v2-28 — Weekend gap, phá range không gap, và "gap" do spread giãn: ba thứ khác nhau.*

**[MARKET MECHANICS]** BIS mô tả thị trường FX giao ngay giao dịch "over the counter", qua dealer — "phi tập trung và phân mảnh", khác với cổ phiếu và futures giao dịch trên sàn tập trung. Hệ quả:

| Hiện tượng trên chart FX | Bản chất | Có phải Breakaway Gap? |
|---|---|---|
| **Weekend gap** | Giá mở cửa đầu tuần khác giá cuối tuần trước | Chỉ khi nó rời một vùng có ý nghĩa VÀ được chấp nhận. Thường bị lấp sớm; nhiều khi chỉ là gap mở tuần |
| **"Session gap"** | Phiên Á / London / New York là **khung giờ**, không phải thời gian đóng cửa → **không có gap giữa các phiên** theo nghĩa cổ phiếu | Không |
| **Bước nhảy trong phiên** (tin lớn) | Nhà cung cấp thanh khoản rút giá chào → bước nhảy | Hiếm khi là breakaway; thường là phản ứng tin |
| **ICT FVG** | Mẫu 3 nến, có giao dịch | Không phải gap thật |
| **Displacement phá range** | Nến mạnh nối liền | Hành vi giống breakaway, nhưng **không có gap**. Gọi đúng tên: "breakout có displacement" |
| **"Gap" do spread lúc rollover** | Chart broker thường vẽ theo bid; spread giãn tạo râu/nhảy giả | Không — là hiện tượng dữ liệu |

> [!warning] Giới hạn khi dùng Breakaway Gap trên Forex
> 1. Gap thật hiếm → khái niệm cổ điển ít áp dụng trực tiếp.
> 2. Không có volume tập trung → không dùng được tiêu chí volume của TA cổ phiếu.
> 3. Mỗi broker một nguồn giá → gap phải được kiểm tra trên nhiều nguồn.
> 4. Thứ bạn thấy thường xuyên trên EURUSD/GBPUSD là **phá range bằng displacement**. Đó là một hiện tượng có giá trị riêng — nhưng hãy gọi đúng tên, đừng gọi là breakaway gap.

### 16.5 Thị trường của bạn: NQ1, EURUSD, GBPUSD, XAUUSD

| Thị trường | Gap thật trên D1 | Thứ thay thế thường gặp | Gợi ý |
|---|---|---|---|
| **NQ1** (futures) | Chủ yếu sau cuối tuần và sau giờ nghỉ hằng ngày; ít và thường nhỏ | Gap trên chart **cash index** (NDX) hoặc cổ phiếu/ETF liên quan vào giờ mở cửa New York | Nếu nghiên cứu breakaway gap "chuẩn" của chỉ số, hãy xem cả chart cash index, nhưng ghi rõ nguồn |
| **EURUSD, GBPUSD** | Hiếm, chủ yếu cuối tuần | Phá range bằng displacement + FVG | Đừng ép thành breakaway gap |
| **XAUUSD** (CFD) | Cuối tuần, giờ nghỉ của broker | Phá range bằng displacement | Kiểm tra feed của broker |

### 16.6 Data feed và cách vẽ chart có thể tạo hoặc xóa gap

![[BAG-v2-29-Gio-Dong-Nen-Tao-Hoac-Xoa-Gap.svg|960]]
*Hình BAG-v2-29 — Cùng dữ liệu theo giờ. Cắt nến ngày ở giờ nghỉ → có gap trên D1. Cắt ở giờ khác → bước nhảy nằm trong một nến, gap biến mất.*

Những thứ có thể tạo **gap giả** hoặc **gap không tương đương** giữa các nền tảng:

1. **Giờ đóng nến D1 khác nhau** (giờ máy chủ broker, giờ sàn, UTC).
2. **Chart futures nối liên tục** khi đổi hợp đồng (rollover) — giá hợp đồng mới khác hợp đồng cũ.
3. **Có/không có giờ mở rộng** trên chart cổ phiếu.
4. **Nguồn giá FX khác nhau** giữa các broker.
5. **Dữ liệu thiếu** (mất kết nối, ngày lễ).

> [!important] Quy tắc kiểm tra
> Trước khi ghi một breakaway gap vào journal: mở thêm **ít nhất một nguồn dữ liệu khác** (ví dụ chart futures và chart CFD của cùng thị trường). Nếu gap chỉ có trên một nguồn → ghi là "gap của dữ liệu", không phân tích tiếp.

---

## 17. Breakaway Gap Failure — Khi Breakaway Gap thất bại

### 17.1 Mười tình huống thất bại

![[BAG-v2-30-That-Bai-1-5.svg|960]]
*Hình BAG-v2-30 — Tình huống 1–5. Vùng xám = range cũ, đường đứt = biên trên, ô vàng = gap.*

![[BAG-v2-31-That-Bai-6-10.svg|960]]
*Hình BAG-v2-31 — Tình huống 6–10. Ô 10 là thất bại của người đọc chart, không phải của giá.*

Mỗi tình huống: **Chuyện gì xảy ra → Vì sao (diễn giải) → Quan sát được gì → Hàm ý cấu trúc → Điều nó KHÔNG chứng minh.**

| # | Chuyện gì xảy ra | Vì sao có thể xảy ra **[INTERPRETATION]** | Quan sát được **[QUAN SÁT]** | Hàm ý cấu trúc | KHÔNG chứng minh |
|---|---|---|---|---|---|
| 1 | Gap xuất hiện nhưng bị lấp hết rất nhanh | Lực mua lúc mở cửa là lực "một lần"; không có người mua mới ở giá cao | Giá quay về mép xa trong vài nến | Chưa có sự chấp nhận ở vùng mới | Rằng có ai đó "bẫy" người mua |
| 2 | Gap vượt kháng cự nhưng giá đóng cửa lại dưới kháng cự | Người bán ở kháng cự cũ quay lại; người mua breakout thoát lệnh | Đóng cửa trong range, ở lại đó | **Breakout thất bại** theo tiêu chí thông thường | Rằng range sẽ giữ mãi |
| 3 | Gap vượt hỗ trợ (gap giảm) nhưng giá lấy lại hỗ trợ | Ngược lại của #2 | Đóng cửa lại trên biên dưới | Breakout giảm thất bại | Rằng xu hướng tăng đã bắt đầu |
| 4 | Gap không có follow-through | Không có thêm thông tin / người tham gia mới | Giá đi ngang sát gap | Trạng thái "chưa biết" | Thất bại (chưa) — cũng không chứng minh thành công |
| 5 | Gap rời range nhỏ, nằm trong một range LỚN hơn | Biên của range lớn có người bán riêng | Giá dừng ở đỉnh range lớn | Breakaway của khung nhỏ, không phải của khung lớn | Rằng gap vô nghĩa — nó vẫn có ý nghĩa trong khung nhỏ |
| 6 | Gap ngay trước một đảo chiều | Đến cuối một nhịp dài; người mua cuối cùng vào lệnh | Gap → một vài nến cao hơn → đảo chiều mạnh | Sau này có thể được gọi là exhaustion | Rằng bạn "đáng lẽ phải biết" lúc đó |
| 7 | Gap do tin rồi giá đảo chiều | Thông tin được đánh giá lại sau phản ứng đầu tiên | Gap lớn quanh giờ tin → lấp và đi ngược | Phản ứng tin, không phải chuyển vùng giá | Rằng tin đó "không quan trọng" |
| 8 | Gap chỉ phá cấu trúc nội bộ | Biên ngoài còn phía trên | Giá dừng dưới biên ngoài, quay lại | Chưa rời khung giao dịch lớn | Rằng sẽ không phá biên ngoài sau này |
| 9 | Gap phá cấu trúc nhưng không mở rộng | Có chấp nhận một phần, không có lực đi tiếp | Đóng cửa ngoài biên, rồi đi ngang | Có thể đang hình thành range mới ở vùng mới | Thất bại hay thành công |
| 10 | Gap trong điều kiện thanh khoản thấp (giờ lẻ, ngày lễ) | Ít lệnh tạo ra gap; khi thanh khoản trở lại, giá điều chỉnh | Gap → lấp khi phiên chính mở | Gap ít đại diện cho sự đồng thuận | Rằng mọi gap giờ lẻ đều vô nghĩa |

### 17.2 Khi nào một Breakaway Gap không còn được xem là breakout có ý nghĩa?

Theo tiêu chí của note (bạn có thể chỉnh, nhưng phải ghi trước khi nhìn chart):

> [!danger] Tiêu chí vô hiệu (research framework)
> Ứng viên breakaway bị coi là **breakout thất bại** khi **giá đóng cửa trở lại bên trong range cũ trên khung đang xét, và nến tiếp theo không lấy lại được biên**. Râu nến xuyên vào range không đủ; lấp gap không đủ.

### 17.3 Failed breakout ≠ gap fill thông thường

| | Gap fill thông thường | Failed breakout |
|---|---|---|
| Đường tham chiếu | Mép xa của gap | Biên range |
| Bằng chứng | Giá chạm mép xa | Giá **đóng cửa và ở lại** trong range |
| Ý nghĩa | Giá thử lại vùng đã bỏ qua | Thị trường không chấp nhận giá ở vùng mới |
| Hành động hợp lý | Theo dõi phản ứng; không tự động đảo kế hoạch | Kế hoạch dựa trên breakaway bị vô hiệu |

> [!warning] Đừng "đổi tên" để biện hộ
> Khi một ứng viên breakaway thất bại, cám dỗ lớn nhất là nói "à, hóa ra đó là exhaustion gap". Đó là đổi tên sau khi biết kết quả. Hãy ghi đúng: **"ứng viên breakaway — thất bại"**. Chỉ dùng tên exhaustion nếu TRƯỚC gap bạn đã ghi rằng nhịp đã chạy dài.

---

## 18. Common Misconceptions — Những hiểu lầm phổ biến

Mỗi hiểu lầm: **Câu nói → Vì sao người ta tin → Thực sự quan sát được gì → Diễn giải đúng → Hệ quả thực hành.**

| # | Câu nói | Vì sao người ta tin | Quan sát được | Diễn giải đúng | Hệ quả thực hành |
|---|---|---|---|---|---|
| 1 | **"Mọi gap là imbalance"** | Cộng đồng ICT gọi vùng giá đi nhanh là imbalance; gap trông giống "chỗ trống" | Hai nến không có phần giá chung | Gap có thể do giờ nghỉ, đổi hợp đồng, giờ đóng nến. "Imbalance" là diễn giải, không phải phép đo | Kiểm tra nguồn gốc gap (§4.4) trước khi gọi tên |
| 2 | **"Mọi gap rồi sẽ được lấp"** | Nhiều gap (common, exhaustion) lấp thật; người ta nhớ những lần đó | Một số gap lấp nhanh, một số không lấp trong rất lâu | StockCharts và Bulkowski đều nói breakaway/runaway gap thường không lấp nhanh; Plastun và cộng sự (2020) bác bỏ "huyền thoại" này trên chỉ số Mỹ | Không giao dịch ngược breakaway chỉ để "chờ lấp" |
| 3 | **"Breakaway Gap luôn mở ra xu hướng mới"** | Định nghĩa vòng tròn: ta gọi là breakaway *vì* nó mở ra xu hướng | Nhiều ứng viên thất bại | Chỉ những gap đã được xác nhận mới gọi là breakaway; ứng viên có thể thất bại | Luôn có tiêu chí vô hiệu |
| 4 | **"Gap càng to, breakout càng mạnh"** | Gap to trông ấn tượng | Kích thước gap | Kích thước phụ thuộc thị trường, giờ, thanh khoản. Gap to trong giờ mỏng có thể ít nghĩa hơn gap nhỏ rời range rõ | Không dùng kích thước làm tiêu chí phân loại |
| 5 | **"Mọi gap vượt kháng cự là breakaway"** | Bỏ qua bối cảnh | Gap trên một mức | Cần vùng tích lũy trước đó + sự chấp nhận sau đó. Gap qua kháng cự sau một nhịp dài có thể là exhaustion | Kiểm tra khối A (§9.1) |
| 6 | **"Lấp gap = breakout thất bại"** | Nhầm mép gap với biên range | Giá chạm mép xa | Thất bại là khi đóng cửa và ở lại trong range (§12.4) | Đặt đường vô hiệu ở biên range, không ở mép gap |
| 7 | **"Gap không lấp = tổ chức đang mua mạnh"** | Câu chuyện "Smart Money" dễ nghe | Giá không quay lại vùng gap | Có thể do nhiều lý do: xu hướng chung, thiếu người bán, tin tiếp theo. Danh tính người mua không thấy được | Không dùng câu chuyện này làm lý do vào lệnh |
| 8 | **"Mọi Breakaway Gap do Smart Money tạo ra"** | ICT narrative | Một gap | Gap có thể do đấu giá mở cửa, giờ nghỉ, sổ lệnh mỏng. Không xác định được người tạo từ OHLC **[UNCONFIRMED CLAIM]** | Mô tả bằng cơ chế, không bằng nhân vật |
| 9 | **"Breakaway Gap và FVG là một"** | Cộng đồng ICT dùng tên "breakaway gap" cho FVG không bị quay lại | Hai mẫu hình khác nhau (2 nến vs 3 nến) | Hai khái niệm, hai cơ chế, hai cách dùng (§3.7, §15.2) | Ghi rõ nghĩa đang dùng |
| 10 | **"Breakaway Gap luôn cần volume cao"** | Sách TA cổ phiếu nhấn mạnh volume | Volume (nếu có) | StockCharts nói volume "nên" tăng — là bằng chứng hỗ trợ, không phải định nghĩa. FX không có volume tập trung | Volume = bằng chứng hỗ trợ, không bắt buộc |
| 11 | **"Breakaway Gap chỉ xảy ra lúc mở phiên"** | Ví dụ sách giáo khoa toàn là gap D1 cổ phiếu | Opening gap là dạng thường gặp nhất | Bước nhảy trong phiên cũng có thể rời range (§3.4) | Không giới hạn tìm kiếm ở giờ mở phiên — nhưng ghi rõ loại |

---

## 19. Real-Time Identification vs Hindsight

### 19.1 Được phép gọi tên gì, vào lúc nào?

![[BAG-v2-32-Real-Time-vs-Hindsight.svg|960]]
*Hình BAG-v2-32 — Bốn thời điểm. Cột phải là tên được phép dùng nếu không dùng nến tương lai.*

| Thời điểm | Trạng thái | Biết được | Chưa biết | Tên được phép |
|---|---|---|---|---|
| **T0** — nến gap vừa mở | **Initial gap observation** | Gap ở đâu; so với biên range; giờ nào; có tin không | Nến sẽ đóng cửa ở đâu | "Gap" |
| **T1** — nến gap đóng cửa ngoài biên | **Preliminary breakaway candidate** | Đã rời range khi đóng cửa | Giá có được chấp nhận ở vùng mới không | "Ứng viên Breakaway" |
| **T2** — follow-through / giữ khi test | **Post-gap confirmation** | Giá đi tiếp và giữ ngoài range theo tiêu chí đã ghi | Nhịp sẽ đi bao xa | "Breakaway Gap (xác nhận theo tiêu chí X)" |
| **T2'** — đóng cửa lại trong range | **Failed breakout** | Thị trường không chấp nhận giá mới | — | "Breakout thất bại có gap" |

### 19.2 Vì sao hindsight nguy hiểm đặc biệt với khái niệm này

Bulkowski viết về việc dùng gap để giao dịch: **"khi bạn nhận diện đúng được chúng, nhịp giá đã gần kết thúc."** Lý do: ba trong bốn loại gap được định nghĩa bằng **vị trí trong một nhịp** — và vị trí trong nhịp (đầu, giữa, cuối) chỉ biết được khi nhịp đã xong.

**Ví dụ của sự tự lừa mình:**
- Bạn nhìn lại chart, thấy một gap ở đầu một xu hướng tăng dài → "đây là breakaway gap đẹp".
- Bạn **không thấy** mười gap khác rời range rồi thất bại, vì bạn không tìm chúng — chúng không "đẹp".
- Kết luận "breakaway gap rất đáng tin" được rút ra từ mẫu đã bị lọc theo kết quả.

### 19.3 Cách tránh hindsight bias

1. **Ghi khối A (bối cảnh) TRƯỚC khi nhìn nến gap** — biên range ở đâu, xu hướng trước đó dài bao nhiêu.
2. **Ghi tiêu chí xác nhận và tiêu chí vô hiệu TRƯỚC khi nhìn tiếp** — ví dụ "xác nhận = hai nến đóng cửa ngoài biên và không đóng cửa lại trong range; vô hiệu = đóng cửa trong range".
3. **Khi xem lại chart lịch sử, dùng bar replay** — che phần bên phải của chart, mở từng nến.
4. **Ghi lại MỌI ứng viên**, không chỉ những cái thành công.
5. **Ghi thời điểm của mỗi tên gọi** — "nến số mấy thì gọi là gì".

> [!important] Câu hỏi kiểm tra
> "Nếu tôi chỉ được xem đến nến này, tôi có gọi nó là breakaway không?" Nếu câu trả lời là "không, nhưng giờ nhìn lại thì rõ" — đó là hindsight.

---

## 20. Practical Chart Reading Framework — Quy trình đọc chart

### 20.1 Đánh giá quy trình 6 bước ban đầu

Quy trình 6 bước trong yêu cầu nghiên cứu (bối cảnh → gap → phá cấu trúc → hành vi sau gap → phân loại → ý nghĩa) là đúng thứ tự thời gian. Ba điểm cần bổ sung:

| Điểm yếu | Vì sao là vấn đề | Bổ sung |
|---|---|---|
| Thiếu bước kiểm tra dữ liệu | Gap có thể do giờ đóng nến, rollover, feed (§16.6). Phân tích một gap giả là lãng phí và gây sai | **Bước 0** |
| Bước 5 có thể bị dùng hindsight | "Phân loại" sau khi đã thấy cả nhịp | Bắt buộc ghi **thời điểm** của mỗi phân loại; cho phép "chưa rõ" |
| Bước 6 dừng ở "có setup không" | Breakaway gap là bối cảnh; nếu không nối sang mô hình entry riêng, dễ biến gap thành tín hiệu | **Bước 7**: chuyển sang quy trình H1 → M5 |

### 20.2 Quy trình 8 bước (0 → 7)

![[BAG-v2-33-Quy-Trinh-Doc-Chart.svg|960]]
*Hình BAG-v2-33 — Mỗi bước có lối thoát "DỪNG". Phần lớn gap dừng ở bước 0–3, và đó là kết quả bình thường.*

**Bước 0 — Kiểm tra dữ liệu**
- Chart vẽ phiên nào? Có giờ mở rộng không? Futures nối liên tục hay hợp đồng cụ thể?
- Giờ đóng nến D1 là giờ nào?
- Gap có trên nguồn dữ liệu thứ hai không? → Không có → **DỪNG** ("gap của dữ liệu").

**Bước 1 — Bối cảnh trước gap** (ghi ra trước khi xem tiếp)
- Trend hay range? Biên nào rõ? Biên ngoài ở đâu? Có hỗ trợ/kháng cự lớn?
- Nhịp trước đó đã chạy bao xa? (để tách breakaway khỏi exhaustion)
- Không có cấu trúc rõ → chỉ gọi là "gap", **DỪNG** phân loại breakaway.

**Bước 2 — Mô tả gap**
- Hướng; vị trí so với biên; cách đo; phiên/giờ; có tin không.
- Gap nằm trong range → common gap, **DỪNG**.

**Bước 3 — Có phá cấu trúc không?**
- Biên nội bộ hay biên ngoài? Nến gap đóng cửa ở đâu?
- Không đóng cửa ngoài biên ngoài → **DỪNG** (hoặc chỉ ghi là breakout của khung nhỏ).

**Bước 4 — Hành vi sau gap**
- Follow-through? Test? Lấp một phần / hết? Lấy lại range?
- Lấy lại range theo tiêu chí vô hiệu → **breakout thất bại**.

**Bước 5 — Phân loại có ghi thời điểm**
- Ứng viên / xác nhận / thất bại / runaway / exhaustion / **chưa rõ**. Ghi "tại nến số mấy".

**Bước 6 — Ý nghĩa thực tế**
- Range cũ còn là "nhà" của giá không? Cấu trúc đã đổi chưa? Có bối cảnh hướng mới không?
- Gap / biên cũ là tham chiếu gì (vùng có thể được test, không phải lệnh chờ tự động)?
- Không có bối cảnh mới → không có lý do giao dịch theo gap.

**Bước 7 — Chuyển sang mô hình entry**
- Breakaway Gap chỉ là **bối cảnh**. Entry đi theo quy trình H1 → M5 riêng (§21).
- Không có trigger M5 → **không có lệnh**.

### 20.3 Khi nào KHÔNG nên dùng Breakaway Gap làm bối cảnh

- Gap chỉ có trên một nguồn dữ liệu.
- Không có vùng / biên xác định trước gap.
- Gap nằm trong range, hoặc chỉ vượt cấu trúc nội bộ.
- Gap đến sau một nhịp đã chạy rất dài (nguy cơ exhaustion — bạn không phân biệt được ở T0).
- Gap trong giờ thanh khoản rất mỏng (ngày lễ, giờ lẻ) và chưa có phiên chính xác nhận.
- Gap trong vài phút quanh một tin lớn, khi giá còn đang dao động mạnh hai chiều.
- Thị trường giao dịch liên tục (FX, crypto spot) mà bạn đang gọi một cú phá range liên tục là "gap".
- Bạn đang gọi tên sau khi đã thấy cả nhịp.

---

## 21. D1 → H1 → M5 Application

![[BAG-v2-34-D1-H1-M5.svg|960]]
*Hình BAG-v2-34 — Gap D1 là bối cảnh; H1 là setup; FVG M5 là tham chiếu entry. Sơ đồ dựng.*

> [!important] Phân vai rõ ràng
> **Breakaway Gap = bối cảnh cấu trúc (D1).** **FVG = tham chiếu vị trí cho entry (M5).** Breakaway Gap **không phải** điều kiện bắt buộc của [[01 - ICT 2022 Model]]. Phần lớn ngày giao dịch sẽ không có breakaway gap nào trên D1 — và mô hình vẫn hoạt động bình thường.

### 21.1 D1 — CONTEXT

| Câu hỏi | Cách trả lời |
|---|---|
| Gap có thể thay đổi Daily Context không? | Có thể — nếu gap rời biên **ngoài** của dealing range D1 và được chấp nhận. Khi đó range cũ không còn là khung tham chiếu; dealing range cần được vẽ lại. Xem [[12-Dealing-Range]], [[37-Re-mapping-Dealing-Range-sau-Displacement]]. |
| Gap phá major swing có ý nghĩa gì? | Là một ứng viên thay đổi cấu trúc HTF. Ý nghĩa thật chỉ có khi giá đóng cửa và ở lại ngoài swing đó. |
| Gap có thể cho thấy thay đổi cấu trúc HTF? | Có thể, nếu đi kèm BOS/MSS trên D1 theo định nghĩa đóng cửa. Gap tự nó không phải BOS/MSS. |
| Daily Bias sau gap | Là **giả thuyết có hướng** dựa trên vị trí so với range cũ, DOL mới, premium/discount — không phải lệnh. Xem [[59-Daily-Bias]]. |

**Lưu ý cho NQ1:** vì futures giao dịch gần như liên tục, breakaway gap D1 thật trên NQ1 hiếm. Một cú rời range D1 bằng nến mạnh liên tục là **displacement phá range** — có thể đóng vai trò bối cảnh tương tự, nhưng hãy ghi đúng tên.

### 21.2 H1 — SETUP

| Câu hỏi | Cách trả lời |
|---|---|
| H1 gap có giúp xác định structural breakout không? | H1 gap thường là bước nhảy trong phiên hoặc gap giờ nghỉ. Nó có thể là một phần của displacement H1 — nhưng câu hỏi "breakout có ý nghĩa không" vẫn trả lời bằng đóng cửa và follow-through. |
| Gap xuất hiện trong H1 POI có ý nghĩa gì? | Giá rời POI nhanh. Đây là chi tiết về **tốc độ phản ứng**, không phải xác nhận độc lập. |
| Gap có phải dấu hiệu của displacement không? | Có thể đi kèm, nhưng không bắt buộc và không đủ (§15.1). |
| Vai trò thực tế | Khi giá quay về vùng gap D1 / biên range cũ, H1 cho thấy **setup có đang hình thành không**: có SSL nội bộ bị quét không, có cấu trúc giảm nhỏ để phá không. |

### 21.3 M5 — EXECUTION

| Câu hỏi | Cách trả lời |
|---|---|
| M5 gap có thể dùng để xác nhận displacement không? | Gap M5 trong phiên thường chỉ là bước nhảy do thanh khoản mỏng. Displacement M5 được đánh giá bằng thân nến, đóng cửa, và việc phá swing — không cần gap. |
| M5 gap có thể xuất hiện sau sweep và MSS không? | Có thể, đặc biệt quanh giờ tin. Nhưng chuỗi execution là: **sweep → MSS → displacement → FVG → entry**. Gap không thay thế bước nào. |
| Gap là confirmation hay entry trigger? | **Không phải cả hai.** Ở M5, tham chiếu entry là FVG trong displacement (theo [[01 - ICT 2022 Model]]). Gap M5, nếu có, chỉ là một chi tiết mô tả. |

### 21.4 Một luồng ví dụ (sơ đồ dựng, không phải dữ liệu thật)

```text
D1  (CONTEXT)
    Range nhiều ngày ── biên trên rõ
    Gap tăng rời biên trên, nến đóng cửa ngoài biên         → ỨNG VIÊN breakaway
    Hai ngày tiếp theo đóng cửa ngoài range                  → bối cảnh: range cũ ở "phía dưới"
    DOL: BSL của đỉnh cũ khung lớn phía trên                 → bias: GIẢ THUYẾT tăng

H1  (SETUP)
    Giá hồi về vùng gap D1 / biên trên range cũ
    Quét một đáy nhỏ nội bộ (SSL nội bộ)                     → setup ĐANG hình thành

M5  (EXECUTION)
    Sweep đáy M5 → MSS (đóng cửa vượt đỉnh nhỏ) → displacement → FVG
    Entry: tại FVG M5     SL: dưới đáy sweep     Target: liquidity theo DOL
    Không có chuỗi này → KHÔNG có lệnh, dù gap D1 'đẹp'

Vô hiệu bối cảnh D1: giá đóng cửa D1 trở lại trong range cũ.
```

### 21.5 Điều không được làm

- Không vào lệnh **chỉ vì** giá chạm vùng gap D1.
- Không dùng gap D1 làm lý do bỏ qua bước xác nhận M5.
- Không phân tích M5 tách rời D1/H1.
- Không đặt lệnh chờ ở mép gap "vì gap sẽ được lấp" hoặc "vì gap sẽ giữ".

---

## 22. Case Studies and Counterexamples

> [!note] Về dữ liệu
> Tất cả case dưới đây là **chuỗi giá dựng (synthetic)** để học cơ chế. Không case nào là dữ liệu lịch sử thật; không gán tên mã hay ngày cụ thể. Mỗi nến được mô tả theo dạng **[thấp – cao, mở → đóng]**.

### Case A — Bullish Breakaway Gap hợp lệ

```text
Ngày 1–8 : đi ngang 100–104 (đỉnh 104 chạm 3 lần)
Ngày 9   : [102.6 – 104.0, 103.1 → 103.8]   ← sát biên trên
Ngày 10  : [106.4 – 108.1, 107.0 → 107.8]   ← GAP: thấp nhất 106.4 > cao nhất 104.0
Ngày 11  : [107.3 – 109.4, 107.8 → 109.1]   ← đi tiếp
Ngày 12  : [108.7 – 110.6, 109.1 → 110.3]
Ngày 13  : [106.0 – 109.6, 109.2 → 106.9]   ← quay vào gap (lấp một phần), không chạm 104
Ngày 14+ : đi lên tiếp, không đóng cửa dưới 104
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh trước | Range rõ, biên trên test nhiều lần |
| 2 | Hình thành gap | Opening gap tăng, full gap 104.0 → 106.4 |
| 3 | Bối cảnh cấu trúc | Gap rời biên ngoài của range |
| 4 | Hành vi quan sát được | Đóng cửa ngoài biên; follow-through hai ngày; lấp một phần ngày 13 |
| 5 | Diễn giải TA | Breakaway Gap (xác nhận theo tiêu chí: đóng cửa ngoài biên + không reclaim) |
| 6 | Diễn giải ICT | Range cũ thành vùng phía dưới; vùng gap/biên cũ có thể là POI khi giá hồi; DOL dời lên trên |
| 7 | Hành vi sau đó | Lấp một phần rồi đi tiếp |
| 8 | Bài học | Lấp một phần là bình thường; đường quyết định là 104 |
| 9 | Không kết luận được | Ai đã mua; nhịp sẽ đi bao xa; lần test sau có giữ không |

### Case B — Bearish Breakaway Gap hợp lệ

```text
Ngày 1–8 : đi ngang 96–100 (đáy 96 chạm nhiều lần)
Ngày 9   : [96.0 – 97.4, 96.9 → 96.2]
Ngày 10  : [91.9 – 93.6, 93.0 → 92.2]   ← GAP giảm: cao nhất 93.6 < thấp nhất 96.0
Ngày 11  : [90.6 – 92.7, 92.2 → 90.9]
Ngày 12  : [90.2 – 94.0, 90.8 → 93.1]   ← hồi vào gap, không đóng cửa trên 96
Ngày 13+ : giảm tiếp
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh trước | Range rõ, biên dưới test nhiều lần |
| 2 | Hình thành gap | Gap giảm, full gap 93.6 → 96.0 |
| 3 | Bối cảnh cấu trúc | Rời biên dưới |
| 4 | Quan sát | Đóng cửa ngoài biên; follow-through; hồi vào gap không lấy lại range |
| 5 | Diễn giải TA | Bearish Breakaway Gap |
| 6 | Diễn giải ICT | Range cũ thành vùng phía trên (premium so với vùng mới); DOL dời xuống |
| 7 | Sau đó | Giảm tiếp |
| 8 | Bài học | Đối xứng với Case A; đường quyết định là 96 |
| 9 | Không kết luận được | Nguyên nhân; độ dài nhịp |

### Case C — Gap trông như breakaway nhưng không phải

```text
Ngày 1–6 : tăng đều từ 100 lên 105.6 (không có vùng đi ngang)
Ngày 7   : [106.6 – 108.8, 107.0 → 108.5]   ← GAP tăng mạnh
Ngày 8   : [105.4 – 108.7, 108.5 → 105.6]   ← lấp gap ngay
Ngày 9   : [103.6 – 105.8, 105.6 → 103.9]
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh trước | Đang chạy, KHÔNG có range ngay trước gap |
| 2 | Gap | Gap tăng lớn |
| 3 | Cấu trúc | Không có biên nào bị "rời bỏ" |
| 4 | Quan sát | Lấp ngay ngày hôm sau, giá đảo chiều |
| 5 | TA | Thiếu điều kiện bắt buộc số 1 → không phải breakaway. Vị trí gợi ý exhaustion (theo nhìn lại) |
| 6 | ICT | Có thể đọc là đi vào BSL rồi đảo — diễn giải sau sự kiện |
| 7 | Sau đó | Giảm |
| 8 | Bài học | Khối A (bối cảnh) loại trường hợp này TRƯỚC khi gap xảy ra |
| 9 | Không kết luận được | Rằng mọi gap sau nhịp dài đều là exhaustion |

### Case D — Breakaway Gap bị lấp (nhưng không thất bại)

```text
Ngày 1–8 : range 100–104;  Ngày 9: [102.9 – 105.0, 103.1 → 104.7] (đóng cửa nhẹ trên biên)
Ngày 10  : [106.8 – 108.6, 107.4 → 108.3]   ← GAP 105.0 → 106.8
Ngày 11  : [107.9 – 109.4, 108.3 → 109.0]
Ngày 12  : [106.4 – 109.2, 109.0 → 106.7]
Ngày 13  : [104.6 – 107.0, 106.7 → 105.2]   ← LẤP HẾT gap (chạm 105.0, xuống 104.6)
Ngày 14  : [104.3 – 106.6, 105.2 → 106.3]   ← râu vào range, đóng cửa trên 104
Ngày 15+ : đi lên
```

| # | Mục | Nội dung |
|---|---|---|
| 1–3 | Bối cảnh | Như Case A |
| 4 | Quan sát | Gap bị lấp hết ngày 13; râu vào range ngày 14 nhưng đóng cửa trên biên |
| 5 | TA | Gap filled, breakaway vẫn chưa bị phủ nhận theo tiêu chí đóng cửa |
| 6 | ICT | Biên range cũ hoạt động như vùng phản ứng; có thể có sweep SSL ngắn dưới biên |
| 7 | Sau đó | Đi lên |
| 8 | Bài học | **Lấp gap ≠ thất bại** (§12.4) |
| 9 | Không kết luận được | Rằng biên cũ "luôn" giữ |

### Case E — Breakaway Gap với follow-through mạnh

```text
Range 100–104 → Ngày 10: GAP lên [106.4 – 108.1]
Ngày 11–16: mỗi ngày tạo đỉnh mới, không ngày nào xuống dưới 106.4
```

| # | Mục | Nội dung |
|---|---|---|
| 1–3 | Bối cảnh | Như Case A |
| 4 | Quan sát | Không có lần test nào; giá chạy liên tục |
| 5 | TA | Breakaway; các gap tiếp theo (nếu có) giữa nhịp sẽ là ứng viên runaway |
| 6 | ICT | Trên khung nhỏ có thể có nhiều FVG tiếp diễn |
| 7 | Sau đó | Nhịp kéo dài |
| 8 | Bài học | Người "chờ lấp gap mới mua" đứng ngoài cả nhịp — chờ lấp không phải chiến lược |
| 9 | Không kết luận được | Rằng nhịp sau cũng sẽ như vậy |

### Case F — Gap trong vùng đi ngang (common gap)

```text
Range rộng 100–110, ở giữa range:
Ngày 5: [105.6 – 107.4, 106.9 → 105.9]
Ngày 6: [103.2 – 104.9, 104.6 → 103.6]   ← GAP giảm nhỏ 104.9 → 105.6, vẫn trong range
Ngày 8: [103.9 – 106.2, 104.1 → 105.9]   ← lấp lại
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh | Range rộng |
| 2 | Gap | Gap nhỏ |
| 3 | Cấu trúc | Không phá biên nào |
| 4 | Quan sát | Lấp sau hai nến |
| 5 | TA | Common gap |
| 6 | ICT | Không có ý nghĩa cấu trúc riêng |
| 7 | Sau đó | Tiếp tục trong range |
| 8 | Bài học | Vị trí quyết định tên, không phải hình dạng |
| 9 | Không kết luận được | Rằng range sẽ không bị phá sau này |

### Case G — Gap trong quá trình đảo chiều

```text
Ngày 1–5 : giảm, đỉnh thấp dần (110.6 → 108.8 → 107.6 → 104.8)
Ngày 6–9 : đi ngang tạo đáy 100–104
Ngày 10  : [106.4 – 108.4, 107.0 → 108.1]   ← GAP tăng vượt đỉnh thấp dần gần nhất (104.8)
Ngày 11+ : đi lên, tạo đỉnh cao hơn
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh | Xu hướng giảm → vùng tạo đáy ngắn |
| 2 | Gap | Gap tăng |
| 3 | Cấu trúc | Vượt đỉnh thấp dần gần nhất → ứng viên đổi cấu trúc |
| 4 | Quan sát | Follow-through, đỉnh cao hơn |
| 5 | TA | Có vùng đáy để rời → hợp lý gọi là breakaway khỏi vùng đáy. Nếu không có vùng đáy, đó chỉ là gap trong đảo chiều |
| 6 | ICT | Có thể là MSS/CHoCH trên D1 ([[21-Market-Structure-Shift]]) |
| 7 | Sau đó | Đảo chiều thành tăng |
| 8 | Bài học | Câu hỏi "có vùng để rời không" quyết định tên |
| 9 | Không kết luận được | Rằng đáy đã chắc chắn |

### Case H — Forex

```text
EURUSD (minh họa), H4:
Thứ Năm–Thứ Sáu: đi ngang hẹp
Chủ nhật mở cửa: GAP tăng nhỏ trên biên trên (weekend gap)
Thứ Hai phiên Á: giá trôi xuống, lấp gap
Thứ Hai phiên London: phá biên trên bằng ba nến H4 mạnh LIÊN TỤC (không gap) → đi tiếp
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh | Range hẹp cuối tuần |
| 2 | Gap | Weekend gap — gap thật duy nhất trong tuần |
| 3 | Cấu trúc | Gap vượt biên nhưng bị lấp ngay |
| 4 | Quan sát | Lấp trong phiên Á thanh khoản mỏng; breakout thật đến sau, không có gap |
| 5 | TA | Weekend gap: không phải breakaway. Breakout London: breakout có displacement, KHÔNG có gap |
| 6 | ICT | Weekend gap ↔ NWOG ([[24-New-Week-Opening-Gap]]); breakout London để lại FVG |
| 7 | Sau đó | Đi tiếp theo breakout London |
| 8 | Bài học | Trên FX, "breakaway" thực tế thường là phá range liên tục. Đừng gọi weekend gap là breakaway chỉ vì nó vượt biên |
| 9 | Không kết luận được | Rằng weekend gap "dự báo" hướng tuần |

### Case I — Futures / Cổ phiếu

```text
Cổ phiếu X (minh họa), D1:
Ba tuần đi ngang 50–54
Kết quả kinh doanh công bố SAU giờ đóng cửa
Sáng hôm sau: đấu giá mở cửa ở 58 → GAP 54 → 57.5 (low của ngày)
Volume ngày gap cao hơn rõ; hai ngày sau giá đóng cửa trên 57

Futures chỉ số cùng thời điểm: chart gần 24 giờ cho thấy một nến mạnh lúc tin ra
ngoài giờ cổ phiếu — KHÔNG có gap trên D1 của futures.
```

| # | Mục | Nội dung |
|---|---|---|
| 1 | Bối cảnh | Range ba tuần |
| 2 | Gap | Opening gap sau tin ngoài giờ; giá mở do đấu giá mở cửa |
| 3 | Cấu trúc | Rời biên ngoài |
| 4 | Quan sát | Gap, volume tăng, follow-through |
| 5 | TA | Breakaway Gap "sách giáo khoa" |
| 6 | ICT | Không cần khái niệm ICT để giải thích. Nếu áp vào, range cũ thành vùng phía dưới |
| 7 | Sau đó | Phụ thuộc vào việc giá giữ trên 54 |
| 8 | Bài học | Cùng một sự kiện: gap trên cổ phiếu, không gap trên futures 24 giờ. Gap là đặc điểm của chart + phiên |
| 9 | Không kết luận được | Rằng kết quả kinh doanh tốt "chắc chắn" giữ được giá |

### 22.1 Năm trường hợp dễ bị phân loại nhầm

![[BAG-v2-35-Nam-Case-Phan-Loai-Nham.svg|960]]
*Hình BAG-v2-35 — Năm lỗi phân loại thường gặp.*

| # | Trường hợp | Nhầm thành | Thật ra là | Cách tránh |
|---|---|---|---|---|
| 1 | Weekend gap FX vượt biên | Breakaway | Gap mở tuần, thường bị lấp sớm | Bước 0 + chờ phiên chính |
| 2 | Gap rời range nhỏ nằm trong range lớn | Breakaway khung lớn | Breakaway khung nhỏ | Xác định biên ngoài trước (§13.3) |
| 3 | Gap mạnh sau một nhịp dài, không có range trước | Breakaway | Ứng viên exhaustion / runaway | Khối A: có vùng để rời không? |
| 4 | Gap do đổi hợp đồng / giờ đóng nến | Breakaway | Gap của dữ liệu | Kiểm tra nguồn thứ hai |
| 5 | Breakaway thật bị lấp một phần | "Exhaustion vì bị lấp" | Breakaway vẫn còn hiệu lực | Đường quyết định là biên range |

### 22.2 Năm trường hợp gap không tạo ra breakout thành công

```text
1. Lấp ngay           : gap → 2 nến đỏ → đóng cửa trong range
2. Reclaim kháng cự   : gap → 1 nến tăng → nến giảm dài đóng cửa dưới biên → ở lại trong range
3. Kẹt dưới range lớn : gap → chạm đỉnh range lớn → đi ngang → quay về
4. Tin rồi đảo chiều  : gap lớn giờ tin → nến đảo chiều cùng ngày → lấp và đi ngược
5. Thanh khoản mỏng   : gap ngày lễ → phiên chính mở → lấp và trở lại range
```

Chi tiết từng trường hợp ở §17.1 (tình huống 1, 2, 5, 7, 10).

### 22.3 Năm trường hợp lấp gap nhưng KHÔNG đảo chiều

![[BAG-v2-36-Nam-Case-Lap-Gap-Khong-Dao-Chieu.svg|960]]
*Hình BAG-v2-36 — Điểm chung: giá không đóng cửa và ở lại trong range cũ.*

| # | Trường hợp | Vì sao không phải đảo chiều |
|---|---|---|
| 1 | Lấp một phần rồi đi tiếp | Chưa tới mép xa, càng chưa tới biên |
| 2 | Lấp hết, giữ trên biên range | Đóng cửa trên biên; range chưa được lấy lại |
| 3 | Lấp hết, râu thủng biên rồi đóng cửa lại phía trên | Râu ≠ đóng cửa; thường được ICT đọc là quét SSL dưới biên |
| 4 | Lấp sau rất lâu, sau khi đã có nhịp tăng | Lấp là một pullback sâu trong xu hướng, không phải phủ nhận breakout |
| 5 | Lấp trên khung nhỏ, khung lớn vẫn còn | Râu nến D1 chạm vùng; cấu trúc D1 không đổi |

---

## 23. Common Trading Mistakes

| # | Lỗi | Vì sao xảy ra | Vì sao sai | Cách tốt hơn |
|---|---|---|---|---|
| 1 | **Vào lệnh ngay khi thấy gap** | Sợ lỡ cơ hội ([[04-Mistake-FOMO-Entry]]) | Lúc đó chỉ biết T0; giá mở thường có biến động và spread lớn nhất | Gap là bối cảnh; chờ quy trình H1 → M5 |
| 2 | **Cho rằng mọi gap sẽ đi tiếp cùng hướng** | Nhớ các ví dụ thành công | Nhiều ứng viên thất bại; common và exhaustion gap thường lấp | Phân loại theo khối A–D; có tiêu chí vô hiệu |
| 3 | **Coi mọi gap là FVG** | Lẫn tên gọi | Hai cấu trúc khác nhau (§15.2) | Gọi đúng tên; FVG cho entry, gap cho bối cảnh |
| 4 | **Cho rằng mọi gap phải được lấp** | "Huyền thoại gap" | Bị nguồn TA và nghiên cứu bác bỏ cho breakaway/runaway | Không fade breakaway chỉ để chờ lấp |
| 5 | **Nhầm lấp gap với breakout thất bại** | Nhìn mép gap thay vì biên range | Lấp ≠ reclaim (§12.4) | Đường vô hiệu = biên range + đóng cửa |
| 6 | **Bỏ qua cấu trúc khung lớn** | Chỉ nhìn khung đang trade | Gap có thể rời range nhỏ trong range lớn ([[09-Mistake-Wrong-daily-bias]]) | Xác định biên ngoài D1 trước |
| 7 | **Bỏ qua phiên giao dịch** | Không biết chart vẽ phiên nào | Gap giờ nghỉ/giờ lẻ ít đại diện | Bước 0; ghi phiên/giờ của gap |
| 8 | **Bỏ qua tin tức** | Không xem lịch kinh tế | Gap do tin thường biến động hai chiều mạnh | Ghi tin; chờ giá ổn định sau tin |
| 9 | **Dùng logic gap cổ phiếu cho Forex** | Sách TA chủ yếu viết cho cổ phiếu | FX không có đấu giá mở cửa, không có volume tập trung, giao dịch liên tục | §16.4: gọi đúng tên phá range liên tục |
| 10 | **Gọi tên breakaway sau khi thấy cả nhịp** | Nhìn lại chart lịch sử | Hindsight bias; mẫu bị lọc theo kết quả | Bar replay; ghi tên kèm thời điểm (§19.3) |
| 11 | **Vào lệnh không có xác nhận thực thi riêng** | Tin rằng gap "đủ mạnh" | Bối cảnh ≠ trigger ([[06-Mistake-Not-Have-Market-Structure-Shift]]) | Sweep → MSS → displacement → FVG trên M5 |
| 12 | **Coi kích thước gap là thước đo duy nhất** | Gap to trông ấn tượng | Kích thước phụ thuộc thị trường, giờ, thanh khoản | Đánh giá vị trí + chấp nhận, không đánh giá độ lớn |

---

## 24. What We Actually Know — Điều ta thật sự biết

![[BAG-v2-37-Dieu-Ta-That-Su-Biet.svg|960]]
*Hình BAG-v2-37 — Sáu bậc độ chắc chắn. Đừng để nhận định bậc dưới mượn độ tin cậy của bậc trên.*

| Nhận định | Loại bằng chứng | Độ tin cậy | Giới hạn |
|---|---|---|---|
| Giá chỉ khớp ở nơi có lệnh đối ứng; mức không có lệnh chờ thì không có giao dịch | Market Mechanics | **Cao** | Không cho biết vì sao các mức đó trống |
| Gap mở cửa là kết quả bình thường của việc không có khớp lệnh liên tục | Market Mechanics (tài liệu Nasdaq, SEC) | **Cao** | Cơ chế mở cửa khác nhau giữa các sàn/thị trường |
| Hành vi gap phụ thuộc vào cấu trúc thị trường và phiên giao dịch | Market Mechanics | **Cao** | Mức độ phụ thuộc phải kiểm tra trên từng thị trường |
| Breakaway Gap gắn với việc giá rời một vùng tích lũy / cấu trúc | Technical Analysis (định nghĩa) | **Cao — về định nghĩa** | Là định nghĩa, không phải phát hiện về dự báo |
| Breakaway gap ít khi bị lấp nhanh so với common/exhaustion gap | Technical Analysis (quan sát của Bulkowski, StockCharts) | **Trung bình** | Chủ yếu dữ liệu cổ phiếu, thị trường tăng; phụ thuộc cách phân loại (vốn có yếu tố nhìn lại) |
| Breakaway Gap có thể cho thấy price discovery đã chuyển sang vùng mới | Market Mechanics + Interpretation | **Trung bình** | Chỉ khi được chấp nhận theo thời gian; tại T0 chưa biết |
| Vùng gap / biên cũ trở thành hỗ trợ/kháng cự | Interpretation | **Thấp–Trung bình** | Bulkowski gọi đó là hỗ trợ/kháng cự **yếu**; cần kiểm tra |
| Cộng đồng ICT dùng "breakaway gap" cho FVG không bị quay lại | ICT community usage | **Trung bình — về việc nó được dùng như vậy** | Chưa tìm được định nghĩa nguyên văn của ICT; các nguồn mâu thuẫn |
| Mọi Breakaway Gap mở ra xu hướng mới | Unconfirmed Claim | **Thấp** | Vòng tròn định nghĩa; nhiều ứng viên thất bại |
| Mọi gap phải được lấp | Unconfirmed Claim | **Thấp** | Bị nguồn TA và nghiên cứu học thuật bác bỏ cho breakaway/runaway |
| Breakaway Gap và FVG là một | Conceptual Claim | **Sai về định nghĩa** | Hai cấu trúc khác nhau |
| Gap do "Smart Money" tạo ra | Unconfirmed Claim | **Không kiểm chứng được từ OHLC** | Chart không cho thấy danh tính hay ý định |
| Kết quả nghiên cứu học thuật về gap là giống nhau giữa các thị trường | — | **Không** | Caporale & Plastun (2017): hành vi sau gap phần lớn phù hợp thị trường hiệu quả, ngoại trừ FX; Plastun và cộng sự (2020): trên chỉ số Mỹ, giá có xu hướng đi theo hướng gap trong ngày gap. Kết quả khác nhau theo thị trường và giai đoạn |

---

## 25. Final Mental Model

![[BAG-v2-38-Mental-Model-Cuoi.svg|960]]
*Hình BAG-v2-38 — Năm câu để mang theo.*

> [!summary] Năm câu
> 1. **Gap là dấu vết.** Giá xuất hiện ở mức mới mà không đi qua các mức giữa — vì không có giao dịch liên tục hoặc không có lệnh chờ ở giữa.
> 2. **Breakaway là VỊ TRÍ.** Gap đưa giá ra khỏi một vùng mà mọi người đã thấy. Không có vùng → không có breakaway.
> 3. **Tên gọi đến SAU.** Lúc gap xuất hiện chỉ là ứng viên. Giữ / lấp / quay về range mới cho phép gọi tên.
> 4. **Lấp gap ≠ thất bại.** Đường quyết định là biên range và nơi giá đóng cửa.
> 5. **Bối cảnh, không phải cò súng.** Breakaway Gap trả lời "thị trường đang ở đâu". Câu hỏi "vào lệnh ở đâu" thuộc về H1 → M5.

```text
           ┌────────────────────────── THẤY GAP ──────────────────────────┐
           │                                                               │
   Dữ liệu thật? ──không──► gap của dữ liệu (dừng)                         │
           │ có                                                            │
   Có vùng/biên trước gap? ──không──► chỉ là "gap" (ghi lại, dừng)         │
           │ có                                                            │
   Gap ra NGOÀI biên ngoài? ──không──► common gap / breakout khung nhỏ     │
           │ có                                                            │
   ỨNG VIÊN BREAKAWAY  ── chờ ──►  đóng cửa + ở lại trong range? ──có──► breakout thất bại
           │ không
   follow-through / giữ khi test  ──►  BREAKAWAY GAP (theo tiêu chí đã ghi)
           │
   = BỐI CẢNH D1  ──►  setup H1  ──►  trigger M5 (sweep → MSS → displacement → FVG)  ──► mới có lệnh
```

---

## 26. Further Research Questions

1. Trên **NQ1 futures**, nếu định nghĩa "gap D1" theo session CME, có bao nhiêu ứng viên breakaway trong một năm? So với **cash index NDX** thì khác ra sao? (Câu hỏi đếm, không phải thống kê dự báo.)
2. Trên **EURUSD**, "phá range bằng displacement liên tục" có thể được định nghĩa chặt chẽ như thế nào để không lẫn với breakaway gap?
3. Nên dùng tiêu chí vô hiệu nào — **một** nến đóng cửa trong range, hay **hai**? Mỗi lựa chọn đổi số lượng "thất bại" thế nào trong journal của bạn?
4. Khi ứng viên breakaway D1 xuất hiện, các setup ICT 2022 trên H1/M5 **cùng hướng** có khác gì (về tần suất, về chất lượng ghi nhận) so với những ngày không có?
5. Vùng gap / biên cũ có thật sự là nơi giá phản ứng thường xuyên hơn các mức ngẫu nhiên khác không? (Cần nhóm so sánh — BACKTEST REQUIRED.)
6. Gap quanh tin lớn có hành vi khác gap không có tin không? Ghi trường `news_event` để so sánh.
7. Nghĩa ICT của "breakaway gap" (FVG không bị quay lại) có thể được định nghĩa **ex-ante** (không cần biết tương lai) không? Nếu không, nó có dùng được cho giao dịch không?
8. Trên XAUUSD, các nguồn dữ liệu broker khác nhau cho ra bao nhiêu gap D1 không trùng nhau?
9. Có nên thêm trạng thái "range mới đang hình thành" sau ứng viên breakaway không có follow-through?
10. ICT có từng định nghĩa "breakaway gap" trong một video gốc không? Cần tìm nguồn nguyên văn trước khi dùng nghĩa 2 trong hệ thống.

---

## Flashcards / Active Recall

**Q1.** Gap là gì, giải thích cho trẻ 5 tuổi?
**A.** Giá chỉ có ở nơi người mua và người bán đồng ý. Khi chợ đóng cửa hoặc không ai đứng bán ở các mức giữa, giá tiếp theo có thể xuất hiện ở xa giá cũ — khoảng ở giữa là gap.

**Q2.** Hai cách đo gap và vì sao phải ghi rõ?
**A.** Full gap (high ↔ low) và opening gap (close → open). Chúng cho kết quả khác nhau; opening gap có thể còn khi full gap đã biến mất trong ngày.

**Q3.** Ba điều kiện của Breakaway Gap trong vault?
**A.** (1) Có vùng/cấu trúc xác định trước gap; (2) gap đưa giá ra ngoài biên; (3) giá được chấp nhận ở bên ngoài (biết theo thời gian). Thiếu (3) → ứng viên.

**Q4.** Breakaway Gap khác FVG ở đâu?
**A.** Gap: 2 nến không có phần giá chung, cần bối cảnh rời vùng, dùng cho bối cảnh. FVG: 3 nến, vùng chỉ nến giữa đi qua (có giao dịch), không cần bối cảnh, dùng làm tham chiếu entry.

**Q5.** "Breakaway Gap" trong cộng đồng ICT thường có nghĩa gì? Vault dùng nghĩa nào?
**A.** FVG trong displacement không bị quay lại. Vault dùng nghĩa TA cổ điển; chưa tìm được định nghĩa nguyên văn của ICT.

**Q6.** Lấp gap có phải breakout thất bại không?
**A.** Không. Thất bại là khi giá đóng cửa và ở lại trong range cũ. Đường quyết định là biên range.

**Q7.** Vì sao không phân loại gap được ngay tại T0?
**A.** Vì loại gap được định nghĩa bằng vị trí trong nhịp và hành vi sau đó — cả hai chỉ biết theo thời gian.

**Q8.** Vì sao Breakaway Gap thật hiếm trên EURUSD?
**A.** FX giao ngay là OTC, giao dịch gần như liên tục 24/5; gap thật chủ yếu ở cuối tuần. "Breakaway" trên FX thường là phá range liên tục bằng displacement.

**Q9.** Gap có phải imbalance không?
**A.** Không nhất thiết. Gap có thể do giờ nghỉ, đổi hợp đồng, giờ đóng nến. "Imbalance" là diễn giải.

**Q10.** Breakaway Gap đứng ở đâu trong D1 → H1 → M5?
**A.** D1 — bối cảnh. Không phải điều kiện bắt buộc của ICT 2022. Entry vẫn cần sweep → MSS → displacement → FVG trên M5.

---

## Lesson Learned

### Bài học chính
- Gap là **dấu vết**, không phải **tín hiệu**.
- "Breakaway" là một **vị trí** cộng với một **kết quả theo thời gian**.
- Ghi bối cảnh và tiêu chí **trước**, gọi tên **sau**, kèm thời điểm.
- Đường vô hiệu là **biên range + giá đóng cửa**, không phải mép gap.
- Trên thị trường giao dịch liên tục, gọi đúng tên: "phá range bằng displacement", không phải "breakaway gap".

### Quy tắc cá nhân
- [ ] Tôi kiểm tra gap trên nguồn dữ liệu thứ hai trước khi phân tích.
- [ ] Tôi ghi biên range và độ dài nhịp trước đó TRƯỚC khi xem nến gap.
- [ ] Tôi chỉ dùng "Breakaway Gap" theo nghĩa TA cổ điển.
- [ ] Tôi không vào lệnh chỉ vì gap; mọi lệnh đi qua H1 → M5.
- [ ] Tôi không đổi tên một ứng viên thất bại thành "exhaustion" sau khi biết kết quả.

### Câu nhắc nhở
> **"Gap cho biết giá đã nhảy. Chỉ thời gian cho biết giá có ở lại."**

---

## Tự kiểm tra chất lượng note (Research QC)

| # | Câu hỏi QC | Trả lời ở |
|---|---|---|
| 1 | Giải thích Gap từ con số 0? | §2, §3 |
| 2 | Người mới hình dung được gap hình thành? | §2.1–2.2, Hình 01–03 |
| 3 | Vì sao giá nhảy qua một vùng giá? | §2.2, §4.2, §4.3, Hình 04–05 |
| 4 | Cơ chế order matching và liquidity? | §4.1–4.3, §7.3–7.5 |
| 5 | Breakaway Gap là gì, chính xác? | §5.1–5.2 |
| 6 | Vì sao nó xuất hiện? | §6, §7, §8 |
| 7 | Phân biệt với các loại gap khác? | §3.6, §11 |
| 8 | Phân biệt Gap với FVG? | §3.7, §15.2, Hình 24–25 |
| 9 | Gap filling? | §12 |
| 10 | Quan hệ với Market Structure? | §13 |
| 11 | Liquidity và Displacement? | §14, §15.1 |
| 12 | Tách Market Mechanics và ICT Interpretation? | Nhãn xuyên suốt, §5.3, §7.1, §15, §24 |
| 13 | Các trường hợp thất bại? | §17, §22.2 |
| 14 | Nhận diện real-time? | §19, §20 |
| 15 | Kiểm soát hindsight bias? | §19.2–19.3, §17.3 |
| 16 | Counterexamples? | §22 (Case C, D, F, H), §22.1–22.3 |
| 17 | Ứng dụng D1 → H1 → M5? | §21 |
| 18 | Khi nào KHÔNG xem gap là Breakaway Gap? | §9.2, §16.4, §20.3 |

---

## Liên kết

**Nền tảng:** [[13-FVG-Fair-Value-Gap]] · [[50-Displacement-In-Depth]] · [[21-Liquidity-Void]] · [[29-Sell-side-Imbalance-Buy-side-Inefficiency]] · [[36-Forex-CFD-Basics-Pip-Lot-Spread-Swap-Leverage-Margin]]
**Gap thật trong ICT:** [[23-New-Day-Opening-Gap]] · [[24-New-Week-Opening-Gap]]
**Cấu trúc:** [[05-BOS-Break-of-Structure]] · [[21-Market-Structure-Shift]] · [[09-Change-of-Character]] · [[12-Dealing-Range]] · [[37-Re-mapping-Dealing-Range-sau-Displacement]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]]
**Thanh khoản:** [[19-Liquidity]] · [[20-Liquidity-Sweep]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]
**Họ PD array:** [[25-OB-Order-Block]] · [[04-Breaker-Block]] · [[22-Mitigation-Block]] · [[17-Inverse-Fair-Value-Gap-iFVG]] · [[03-Balanced-Price-Range]]
**Bối cảnh & thực thi:** [[59-Daily-Bias]] · [[27-Premium-Discount]] · [[32-Top-down-Analysis-Multiple-Timeframes]] · [[18-Kill-Zones]] · [[01 - ICT 2022 Model]] · [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] · [[12 - Consolidation Trading Strategy]]
**Khung giải thích:** [[60-IPDA-Tai-sao-gia-di-chuyen-Tu-Price-Discovery-den-Price-Delivery]]

---

## Nguồn tham khảo

> [!note] Về nguồn
> Định nghĩa và phân loại gap dựa trên TA cổ điển (Tier 3). Cơ chế mở cửa và giao dịch ngoài giờ dựa trên tài liệu của sàn và cơ quan quản lý (Tier 1). Cấu trúc thị trường FX dựa trên BIS (Tier 1–2). Nghiên cứu học thuật (Tier 2) được dùng để cho thấy kết quả **khác nhau theo thị trường**, không để đưa ra con số. Nguồn cộng đồng ICT (Tier 4, có quảng cáo khóa học) chỉ dùng để mô tả **cách tên gọi được dùng**, không làm bằng chứng. **Không tìm được trích dẫn nguyên văn của ICT về "breakaway gap"**; mọi câu về ICT trong note được dán nhãn diễn giải.

**Technical Analysis**
- Bulkowski, T. N. — *Bulkowski on Price Gaps*, ThePatternSite. Định nghĩa gap (low hôm nay > high hôm qua), bốn loại gap, quan sát rằng breakaway gap hiếm khi lấp trong tuần đầu, gap là hỗ trợ/kháng cự yếu, và câu "khi bạn nhận diện đúng được chúng, nhịp giá đã gần kết thúc". https://www.thepatternsite.com/gaps.html
- StockCharts ChartSchool — *Gaps and Gap Analysis*. Định nghĩa breakaway gap (thoát khỏi trading range/congestion area), volume nên tăng (tốt hơn nếu tăng sau gap), cảnh báo câu "mọi gap rồi sẽ được lấp" không đúng với breakaway/runaway gap. https://chartschool.stockcharts.com/table-of-contents/chart-analysis/gaps-and-gap-analysis
- Edwards, R. D. & Magee, J. — *Technical Analysis of Stock Trends* (1948, nhiều lần tái bản). Truyền thống phân loại gap cổ điển. *Không đọc trực tiếp trong lần nghiên cứu này; dẫn như nguồn gốc của dòng phân loại.*

**Market mechanics (sàn và cơ quan quản lý)**
- Nasdaq — *Opening and Closing Cross FAQ*. Thứ tự ưu tiên chọn giá mở cửa; Net Order Imbalance Indicator. https://www.nasdaqtrader.com/content/productsservices/trading/crosses/openclose_faqs.pdf
- U.S. SEC / Investor.gov — *Investor Bulletin: After-Hours Trading* (2022). Rủi ro giao dịch ngoài giờ: ít thanh khoản, spread rộng, giá có thể không phản ánh giờ chính thức, tin công bố ngoài giờ. https://www.investor.gov/additional-resources/news-alerts/alerts-bulletins/investor-bulletin-after-hours-trading
- CME Group — *Holiday and Trading Hours* (giờ giao dịch có thể thay đổi; kiểm tra theo từng sản phẩm). https://www.cmegroup.com/trading-hours.html
- BIS Quarterly Review (12/2025) — *The FX trade execution landscape through the prism of the 2025 BIS Triennial Survey*. FX giao ngay giao dịch OTC qua dealer, "phi tập trung và phân mảnh". https://www.bis.org/publ/qtrpdf/r_qt2512v.htm

**Nghiên cứu học thuật**
- Caporale, G. M. & Plastun, A. (2017). *Price gaps: Another market anomaly?* Investment Analysts Journal, 46(4), 279–293. Dữ liệu cổ phiếu, FX, hàng hóa 2000–2015: hành vi sau gap phần lớn phù hợp thị trường hiệu quả, ngoại trừ FX. https://bura.brunel.ac.uk/handle/2438/14372
- Plastun, A., Sibande, X., Gupta, R. & Wohar, M. E. (2020). *Price gap anomaly in the US stock market: The whole story.* North American Journal of Economics and Finance, 52, 101177. Chỉ số Mỹ 1928–2018: giá có xu hướng đi theo hướng gap trong ngày gap, hiệu ứng tạm thời, kết quả trái với "huyền thoại gap luôn được lấp". https://repository.up.ac.za/items/ea0f239b-b602-4665-b070-b8cb5648552c/full

**Cách dùng trong cộng đồng ICT/SMC (Tier 4 — chỉ để đối chiếu cách dùng tên)**
- innercircletrader.net — *ICT Breakaway Gap* (định nghĩa là FVG không bị mitigate kèm "holding mechanism"; không dẫn nguồn ICT; có quảng cáo khóa học). https://innercircletrader.net/tutorials/ict-breakaway-gap/
- FluxCharts — *Breakaway Gap explained* (định nghĩa là FVG giá không quay lại; thừa nhận "dễ nhận ra khi nhìn lại"). https://www.fluxcharts.com/articles/Trading-Concepts/Price-Action/breakaway-gap
- Kiểm tra transcript máy của ICT 2022 Mentorship (tập 2, 3, 5, 6, 7, 14, 21) trên sozai.app: không thấy chữ "breakaway" (chỉ đọc đầy đủ một phần; không chứng minh ICT chưa từng dùng).

**Bản cũ:** bản v1 của note này được sao lưu tại `Claude outputs/backups/06-Breakaway-Gap.2026-11-10.md.bak`. Các hình `BreakawayGap-*.svg` của bản v1 vẫn còn trong thư mục `attachments` nhưng không còn được note này dùng.
