---
type: ict-concept
concept: IPDA — Interbank Price Delivery Algorithm
aliases:
  - IPDA
  - Interbank Price Delivery Algorithm
  - Institutional Price Delivery Algorithm
  - Price Delivery
  - Tại sao giá di chuyển
tags:
  - trading/ict/concept
  - trading/study
  - "#IPDA"
status: developing
category: Market Model
timeframes:
  - MN
  - W1
  - D1
  - H1
  - M5
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - EURUSD
  - GBPUSD
  - XAUUSD
  - NQ1
importance: 5
confidence: 2
last_reviewed: 2026-10-07
created: 2026-10-07
updated: 2026-10-07
prerequisites:
  - "[[36-Forex-CFD-Basics-Pip-Lot-Spread-Swap-Leverage-Margin]]"
  - "[[19-Liquidity]]"
  - "[[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]"
  - "[[12-Dealing-Range]]"
common_mistakes:
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
---

# IPDA — Tại sao giá di chuyển? Từ Price Discovery đến Price Delivery

> [!summary] Tóm tắt 1 câu
> **Giá thay đổi vì giao dịch tiếp theo xảy ra ở một mức giá khác; price discovery là quá trình thị trường liên tục đi tìm mức giá mà tại đó người mua và người bán còn chịu giao dịch; liquidity (lượng lệnh chờ sẵn sàng làm đối ứng) quyết định một dòng lệnh đẩy giá đi xa hay gần; ICT dùng từ "price delivery" để mô tả đường đi của giá từ vùng này sang vùng khác, và IPDA là *mô hình khái niệm* của ICT để tổ chức cách đọc đường đi đó theo giá, thời gian và liquidity — không phải một cỗ máy bí mật mà ta nhìn thấy được hay chứng minh được là đang điều khiển giá.**

> [!important] Nguyên tắc cốt lõi
> **Không bao giờ nói "giá di chuyển vì IPDA".** Luôn nói theo thứ tự: *ai gửi lệnh gì → lệnh khớp ở đâu → vì sao giao dịch tiếp theo phải xảy ra ở mức giá mới → ICT gọi chuỗi đó là gì*.
> IPDA là **lớp tư duy**, không phải entry model. Nó giúp đặt câu hỏi "giá đang được đưa *từ đâu tới đâu*, trong *khung thời gian nào*?". Nó không bao giờ tự nói "mua ở đây".
> Mọi "đích đến" (DOL) là **giả thuyết có điều kiện**, phải có invalidation và phải thắng một baseline hình học (random walk cũng "đi tới liquidity" rất thường xuyên — mục 24, 31).

> [!info] Đọc trước khi dùng
> - **Tên gọi.** Tài liệu ICT gốc (và các note cũ trong vault như [[41-Change-in-State-of-Delivery]], [[40-Macro-Times]]) dùng **Interbank** Price Delivery Algorithm. "**Institutional** Price Delivery Algorithm" là cách gọi phổ biến khác trong cộng đồng. Note này giải thích cả hai từ, vì mỗi từ hứa hẹn một điều khác nhau (mục 14, 17).
> - **Nguồn ICT.** ICT (Michael J. Huddleston) dạy chủ yếu qua video/mentorship, không có văn bản định nghĩa chính thức. Các bài liên quan trực tiếp nhất là *ICT Mentorship Core Content (2016–17) — Month 05: Quarterly Shifts & IPDA Data Ranges* và *Month 07: Short Term Trading — Blending IPDA Data Ranges & PD Arrays*. Nội dung chi tiết trong note được lấy từ **tóm tắt của cộng đồng** (Tier 3–4), **không** phải trích nguyên văn. Hãy đối chiếu video gốc trước khi trích dẫn.
> - **Mô phỏng.** Hình `IPDA-Sim-*` là **mô phỏng mô hình null / toy model** — baseline mà mọi claim phải vượt, **không phải dữ liệu thị trường**. Hình `IPDA-Deep-*` là sơ đồ khái niệm.
> - **Không có gì trong note này là edge đã kiểm chứng.** Mọi RULE-IPDA là v0.1 — BACKTEST REQUIRED.
> - Note này cố ý đi **chậm**: 11 mục đầu không cần biết ICT. Nếu bạn đã chắc phần cơ bản, vẫn nên đọc mục 6, 8, 11 — đó là chỗ hầu hết giải thích ICT bị "nhảy cóc".

> [!abstract]- Mục lục (bấm để mở)
> - **Cách đọc note** — nhãn, ba tầng giải thích, thẻ 10 câu hỏi
> - **0. Executive Summary** — 16 kết luận
> - **PHẦN A — QUÊN ICT TRƯỚC:** 1. Market · 2. Buyer & Seller · 3. Orders · 4. Bid/Ask · 5. Price discovery · 6. Vì sao giá tăng · 7. Vì sao giá giảm · 8. Vì sao giá chạy rất nhanh · 9. Vì sao giá gần như đứng yên · 10. Vì sao giá đổi hướng và tạo high/low rõ ràng · 11. Liquidity · *Kiểm tra giữa chặng*
> - **PHẦN B — PRICE DELIVERY & IPDA:** 12. Price delivery · 13. Vì sao ICT cần khái niệm này · 14. IPDA là gì · 15. IPDA có tồn tại không · 16. IPDA có "điều khiển thị trường" không · 17. "Institutional/Interbank" · 18. "Algorithm" · 19. IPDA có "đẩy giá" không · 20. Vì sao ICT nói về liquidity · 21. DOL · 22. Vì sao giá không luôn tới DOL
> - **PHẦN C — THỜI GIAN, RANGE, CẤU TRÚC:** 23. IPDA & thời gian · 24. IPDA Data Ranges 20/40/60 · 25. IPDA & Dealing Range · 26. IPDA & Market Structure · 27. IPDA & FVG/Displacement · 28. IPDA trong toàn bộ framework D1→H1→M5
> - **PHẦN D — PHẢN BIỆN & KIỂM CHỨNG:** 29. Fact vs Interpretation · 30. Chart cho biết gì / không cho biết gì · 31. IPDA có kiểm chứng được không · 32. Hypothesis register · 33. IPDA & randomness · 34. Mười hiểu lầm phải sửa
> - **PHẦN E — TỔNG HỢP & ÁP DỤNG:** 35. Câu chuyện khu chợ lớn · 36. Mô hình tư duy cuối cùng · 37. Bài kiểm tra "5 tuổi" · 38. Trả lời 27 câu hỏi cuối · 39. Áp dụng vào workflow · 40. Checklist · 41. Lỗi thường gặp · 42. Câu hỏi tự kiểm tra · 43. Flashcards · 44. Lesson learned · 45. Registers · Tài liệu tham khảo · Phụ lục · Changelog

---

## Cách đọc note này

### Hệ thống nhãn

| Nhãn | Ý nghĩa | Mức tin cậy mặc định |
|---|---|---|
| **[MARKET MECHANICS]** | Có cơ sở từ cơ chế khớp lệnh, cấu trúc thị trường hoặc nghiên cứu thực nghiệm đã công bố | Cao → trung bình tùy bằng chứng |
| **[OBSERVABLE]** | Nhìn thấy trực tiếp trên dữ liệu (giá, thời gian, high/low) | Cao — nhưng chỉ *mô tả*, không *giải thích* |
| **[MATHEMATICAL]** | Đúng theo định nghĩa hoặc chứng minh toán học | Cao về logic, không nói gì về hành vi thật |
| **[SIMULATION]** | Kết quả mô phỏng trên mô hình null / toy model | Cao *về mô hình*; không phải dữ liệu thị trường |
| **[ICT FRAMEWORK]** | Cách ICT / cộng đồng ICT định nghĩa, gọi tên, mô hình hóa | Cao về *định nghĩa*; không nói gì về *hiệu quả* |
| **[INTERPRETATION]** | Cách diễn giải hợp lý nhưng chưa chắc đúng, không chứng minh được từ OHLC | Trung bình → thấp |
| **[HYPOTHESIS]** | Claim có thể kiểm chứng bằng dữ liệu | Chưa biết |
| **[UNKNOWN]** | Không thể biết trực tiếp từ chart | — |
| **[UNSUPPORTED CLAIM]** | Claim không có bằng chứng công khai và/hoặc không thể bị chứng minh sai | Không dùng làm nền cho quyết định |
| **[BACKTEST REQUIRED]** | Không được coi là edge cho đến khi test đúng phương pháp | — |

### Ba tầng giải thích

Mỗi khái niệm quan trọng được giải thích theo ba tầng, **luôn theo thứ tự này**:

| Tầng | Người đọc | Công cụ | Mục tiêu |
|---|---|---|---|
| **TẦNG 1** | Trẻ 5 tuổi | cửa hàng, quả táo, đấu giá, con đường, chiếc xe | Hình dung được chuyện gì đang xảy ra — **không jargon** |
| **TẦNG 2** | Người mới trading | buyer, seller, order, bid, ask, liquidity, price | Biết ẩn dụ tương ứng với cái gì trên chart |
| **TẦNG 3** | Technical | microstructure, order matching, price impact, auction, volatility — rồi mới tới ICT, price delivery, IPDA, DOL | Hiểu cơ chế và giới hạn |

### Thẻ 10 câu hỏi

Các khái niệm cốt lõi có một **thẻ 10 câu** (theo yêu cầu của brief): *1. Nó là gì? · 2. Hãy tưởng tượng thế nào? · 3. Điều gì thực sự xảy ra? · 4. Tại sao nó xảy ra? · 5. Trên chart ta thấy gì? · 6. ICT gọi nó là gì? · 7. Ta không biết gì? · 8. Đâu là fact? · 9. Đâu là interpretation? · 10. Đâu là hypothesis?* Thẻ được viết dạng bảng để tra nhanh khi ôn.

### Chuỗi nhân quả của toàn bộ note

![[IPDA-Deep-00-Chuoi-Nhan-Qua.svg|760]]

> [!tip] Quy tắc viết cho chính mình
> Nếu một câu giải thích có chứa "IPDA muốn…", "thuật toán cần…", "smart money định…" mà **không** chỉ ra được *ai gửi loại lệnh gì và lệnh đó khớp ở đâu*, thì câu đó là **narrative**, không phải **explanation**. Viết lại.

---

## 0. Executive Summary

Mười sáu kết luận. Mỗi kết luận được phát triển ở các mục sau.

**1. Giá không có chân.** **[MARKET MECHANICS]** "Giá" trên chart là mức của giao dịch gần nhất (hoặc báo giá bid/ask gần nhất, tùy feed). Giá "tăng" nghĩa là *giao dịch tiếp theo* xảy ra ở mức cao hơn — vì các lệnh bán rẻ hơn đã được khớp hết, đã bị rút, hoặc người mua chấp nhận trả cao hơn. Không có lực vô hình nào "đẩy" giá (mục 1, 6).

**2. "Nhiều người mua hơn người bán" là cách giải thích sai.** **[MATHEMATICAL]** Trong mọi giao dịch, khối lượng mua *bằng đúng* khối lượng bán. Cái khác nhau là **phía nào chủ động** (chấp nhận giá của phía kia bằng lệnh market) và **phía nào rút/đặt lệnh chờ** (mục 2).

**3. Có ba loại lệnh, và chúng làm ba việc khác nhau với liquidity.** Market order *tiêu thụ* thanh khoản; limit order *cung cấp* thanh khoản; stop order *ẩn* cho tới khi chạm mức rồi biến thành lệnh market — tức *tiêu thụ* thanh khoản đúng lúc giá vừa vượt qua một mức rõ ràng (mục 3).

**4. Price discovery là một vòng lặp không dừng**, không phải một sự kiện: thông tin/nhu cầu → lệnh → khớp → mọi người thấy giá mới → điều chỉnh lệnh → … (mục 5).

**5. Tốc độ của giá phụ thuộc vào tỉ số "dòng lệnh chủ động / độ sâu sổ lệnh".** **[MARKET MECHANICS]** Cont, Kukanov & Stoikov (2014) cho thấy trong khoảng thời gian ngắn, thay đổi giá gần như tuyến tính theo *order flow imbalance* với độ dốc tỉ lệ nghịch với độ sâu. Cùng một lực mua, sổ mỏng làm giá đi xa hơn nhiều (mục 8; **[SIMULATION]** IPDA-Sim-01: độ lệch chuẩn Δgiá/bước 0.20 tick ở sổ dày so với 3.92 tick ở sổ mỏng, *cùng* chuỗi lệnh).

**6. Stop gom lại phía trên đỉnh / dưới đáy rõ ràng có thể tạo dây chuyền tăng tốc.** **[MARKET MECHANICS]** Osler (NY Fed, 2001; 2002) dùng dữ liệu lệnh thật của một ngân hàng FX: stop-loss mua tập trung ngay *trên* số tròn, stop-loss bán ngay *dưới*; khi tỷ giá chạm các vùng này, xu hướng nhanh bất thường ("price cascades"). Đây là nền tảng cơ chế tốt nhất cho ý tưởng "buy-side / sell-side liquidity" của ICT (mục 8, 11, 20).

**7. "Liquidity" có ít nhất ba nghĩa** — thanh khoản (kinh tế học: giao dịch lớn, nhanh, rẻ mà giá không chạy), liquidity pool (ICT: vùng *nghi là* có nhiều lệnh chờ), và "lấy liquidity" (sự kiện: giá giao dịch xuyên qua vùng đó). Trộn nghĩa 2 với nghĩa 1 là lỗi phổ biến nhất (mục 11).

**8. Price delivery là từ vựng mô tả đường đi**, không phải vật thể. "Giá được delivery từ A tới B" chỉ mô tả *đường đi đã xảy ra*; nó không chứng minh có "người giao hàng" (mục 12–13).

**9. IPDA là một mô hình khái niệm của ICT** gồm ba trục — **giá, thời gian, liquidity** — và một số công cụ (data ranges 20/40/60, quarterly shifts, PD arrays, DOL). Có ba cách hiểu: (A) robot trung tâm điều khiển giá — **[UNSUPPORTED CLAIM]**; (B) các quy luật nổi lên từ nhiều người tham gia và nhiều thuật toán thật — **[HYPOTHESIS]**, kiểm chứng được; (C) bộ từ vựng giúp trader tổ chức quan sát — **[INTERPRETATION]**, giá trị đo bằng kỷ luật và expectancy. Note này dùng (B) + (C) (mục 14–15).

**10. FX không có "ông vua".** **[MARKET MECHANICS]** Thị trường FX giao dịch ≈ **9.6 nghìn tỷ USD/ngày** (BIS, khảo sát tháng 4/2025), phi tập trung, gồm hàng nghìn dealer, ECN, quỹ, doanh nghiệp, ngân hàng trung ương với mục tiêu mâu thuẫn nhau. Các vụ thao túng *cục bộ, có thật, bị phạt* (ví dụ các vụ thông đồng ở benchmark fix bị phạt năm 2014–2015) chứng minh rằng thao túng *có thể* xảy ra ở quy mô nhỏ — **không** chứng minh có một thuật toán trung tâm (mục 16).

**11. "Algorithm" trong thị trường là có thật, nhưng là số nhiều.** Thuật toán thực thi (TWAP/VWAP/iceberg), thuật toán tạo lập thị trường, HFT, thuật toán quản trị stop… đều tồn tại. "Thị trường có tính thuật toán" là **[MARKET MECHANICS]**; "có MỘT thuật toán tên IPDA quyết định giá đi đâu" là **[UNSUPPORTED CLAIM]** (mục 18).

**12. "Price seeks liquidity" có một phiên bản cơ chế hợp lý:** người cần giao dịch khối lượng lớn cần đối ứng; vùng có nhiều lệnh chờ/stop là nơi đối ứng xuất hiện dồn dập; nên giao dịch lớn *có động cơ* được thực hiện ở đó. Nhưng ý định cụ thể của ai đó **không thể** suy ra từ chart → **[HYPOTHESIS / UNKNOWN]** (mục 20).

**13. DOL là giả thuyết, không phải lời tiên tri.** Từ cùng một điểm, giá có nhiều đường đi hợp lý. **[MATHEMATICAL]** Với random walk không drift, xác suất chạm mức trên trước mức dưới bằng đúng *vị trí tương đối* của giá giữa hai mức; **[SIMULATION]** IPDA-Sim-02C khớp gần như hoàn hảo. Nghĩa là "giá thường đi tới liquidity gần hơn trước" là **hình học**, chưa phải edge (mục 22).

**14. 20/40/60 ngày là một kênh Donchian — khách quan, nhưng chưa chắc đặc biệt.** **[SIMULATION]** Dưới random walk: xác suất chạm H20 *hoặc* L20 trong 20 ngày tới ≈ **90%** (trong 60 ngày ≈ **99%**); chạm riêng H20 trong 20 ngày ≈ **50%** — và **[MATHEMATICAL]** con số 50% này đúng *chính xác* cho mọi random walk đối xứng, do tính đối xứng thời gian. Xác suất thay đổi **trơn** theo độ dài cửa sổ; 20/40/60 không có "nút" nào dưới null. Muốn chứng minh 20/40/60 là đặc biệt, dữ liệu thật phải cho thấy một "nút" mà null không có (mục 24).

**15. Chart cho bạn phần nổi của tảng băng.** Giá, thời gian, OHLC, high/low, biến động, (volume nếu là futures). Chart **không** cho bạn: ai đặt lệnh, vì sao, lệnh chờ ở từng mức, lệnh bị hủy, ý định tổ chức, thuật toán nào đang chạy. Mọi câu "tổ chức đã…" là suy luận từ phần nổi về phần chìm (mục 30). Thêm một chi tiết thực dụng: chart MT4/MT5 mặc định vẽ theo **giá Bid**, nên một buy stop (khớp theo **Ask**) có thể bị kích hoạt dù chart *không* chạm mức đó.

**16. Câu hỏi đúng không phải "IPDA đúng hay sai?" mà là "nếu IPDA (theo nghĩa B) đúng thì dữ liệu phải cho thấy gì khác với đồng xu?"** — mức ICT được chạm nhiều hơn mức đối chứng cùng khoảng cách; 20/40/60 khác 17/35/71; phản ứng sau khi chạm lớn hơn baseline. Note đề xuất 8 giả thuyết HYP-IPDA-001…008 (mục 31–32). Đồng xu cũng vẽ ra "swing high", "sweep", "MSS", "FVG" (**[SIMULATION]** IPDA-Sim-03: 110 nến nhiễu thuần cho 12 "sweep", 8 "MSS", 20 "FVG").

---

# PHẦN A — HÃY QUÊN ICT TRƯỚC

> [!note] Luật của Phần A
> Trong mục 1–11, giả định **ICT không tồn tại**. Không dùng "smart money", "IPDA", "DOL", "manipulation". Mục tiêu: trả lời được *tại sao giá di chuyển* chỉ bằng con người, lệnh và giao dịch. Nếu không làm được điều này, mọi thuật ngữ ICT phía sau chỉ là nhãn dán lên một hộp đen.

---

## 1. Market là gì?

### 1.1 TẦNG 1 — Khu chợ táo

Có một khu chợ. Cô Lan bán táo giá $1.00. Chú Ba bán $1.05. Bà Tư bán $1.10. Mỗi người chỉ còn một quả.

Bé An chạy tới: "Cho con một quả, **ngay**!" Quầy rẻ nhất là cô Lan → An trả $1.00 → giao dịch xảy ra. Bảng giá của chợ ghi: **$1.00**.

Bé Bình tới: "Con cũng muốn một quả, ngay!" Nhưng cô Lan đã hết táo. Quầy rẻ nhất *còn lại* là chú Ba → Bình trả $1.05. Bảng giá ghi: **$1.05**.

Bé Chi tới, cũng muốn ngay. Lan và Ba đều hết. Chỉ còn bà Tư → $1.10. Bảng giá ghi: **$1.10**.

![[IPDA-Deep-01-Cho-Tao-Gia-La-Giao-Dich.svg|760]]

Hãy để ý ba điều:

1. **Không ai "đẩy" giá.** Không có ai ra lệnh "hôm nay táo phải lên $1.10".
2. **Giá thay đổi vì giao dịch tiếp theo buộc phải xảy ra ở quầy đắt hơn** — các quầy rẻ đã hết hàng.
3. **"Giá" chỉ là con số của giao dịch gần nhất.** Trước khi Chi mua, chẳng ai biết giá tiếp theo là bao nhiêu. Nếu ngay lúc đó cô Lan về với một rổ táo mới và rao $1.00, giao dịch tiếp theo có thể lại là $1.00.

> [!example] Biến thể để tự kiểm tra
> Giả sử sau giao dịch $1.10, không còn ai muốn mua ngay. Bà Tư sốt ruột muốn về sớm, rao: "Ai mua $1.02 không?" Bé Dũng đi ngang, mua. Bảng giá: **$1.02**. Giá "giảm" — dù không có ai "bán khống", không có "phe bán" nào thắng. Chỉ là giao dịch tiếp theo xảy ra ở mức thấp hơn vì người bán chịu nhượng bộ.

### 1.2 TẦNG 2 — Từ chợ táo sang thị trường tài chính

| Trong chợ | Trên thị trường |
|---|---|
| Quả táo | Một đơn vị tài sản (1 lot EURUSD, 1 hợp đồng NQ, 1 ounce vàng) |
| Người bán rao giá ở quầy | **Lệnh bán chờ** (sell limit) — tạo thành phía **ask/offer** |
| Người mua hỏi "ai bán dưới $1.00?" | **Lệnh mua chờ** (buy limit) — tạo thành phía **bid** |
| "Cho con một quả, ngay!" | **Lệnh market** — chấp nhận giá tốt nhất đang có |
| Bảng giá của chợ | **Giá trên chart** (giao dịch cuối, hoặc bid/ask, tùy feed) |
| Quầy hết hàng | Mức giá đó **không còn lệnh chờ** |

**Định nghĩa đơn giản:** *Market là nơi (hoặc mạng lưới) mà những người muốn mua gặp những người muốn bán, và giao dịch xảy ra ở những mức giá mà cả hai bên chấp nhận.*

### 1.3 TẦNG 3 — Technical

**[MARKET MECHANICS]** Có hai kiểu tổ chức thị trường chính, và trader ICT dùng cả hai:

| Đặc điểm | Sàn tập trung có sổ lệnh (ví dụ CME: NQ, ES, GC) | Thị trường phi tập trung OTC (FX spot: EURUSD, GBPUSD) |
|---|---|---|
| Nơi khớp lệnh | Một sổ lệnh trung tâm (central limit order book) | Nhiều nơi: sàn liên ngân hàng (EBS, LSEG Matching), các ECN, dealer báo giá trực tiếp, nội bộ ngân hàng |
| Quy tắc khớp | Ưu tiên giá, rồi thời gian (với nhiều sản phẩm) | Tùy nơi; dealer có thể từ chối trong cửa sổ "last look" |
| Có "một giá" duy nhất? | Có — giao dịch cuối trên sàn | **Không** — mỗi nơi có báo giá riêng, gần nhau nhờ arbitrage |
| Volume trên chart | Volume thật của sàn | Thường là **tick volume** (số lần báo giá thay đổi) của broker |
| Chart retail bạn thấy | Gần với sàn (qua data feed) | Luồng báo giá **của broker/nhà cung cấp** của bạn |

**[MARKET MECHANICS]** Quy mô FX: khảo sát ba năm một lần của BIS cho thấy giao dịch FX đạt **≈ 9.6 nghìn tỷ USD/ngày** vào tháng 4/2025 (tăng 28% so với 7.5 nghìn tỷ năm 2022); USD nằm ở một phía của 89% giao dịch.

> [!warning] Hệ quả thực dụng cho prop firm / CFD
> Khi bạn trade EURUSD trên FTMO/The5ers, "giá" trên chart là **báo giá của nhà cung cấp thanh khoản cho tài khoản đó**, không phải "giá liên ngân hàng". Hai broker có thể in ra high/low khác nhau vài pip. Một "sweep" trên broker A có thể không xảy ra trên broker B. Điều này quan trọng khi ta nói "giá đã lấy liquidity trên đỉnh" — đỉnh của *feed nào*?

### 1.4 Thẻ 10 câu — Market

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Nơi/mạng lưới người muốn mua gặp người muốn bán và giao dịch ở mức giá cả hai chấp nhận |
| 2 | Tưởng tượng thế nào? | Một khu chợ nhiều quầy, mỗi quầy rao một giá |
| 3 | Điều gì thực sự xảy ra? | Lệnh được gửi, khớp với lệnh đối diện, giao dịch được ghi lại |
| 4 | Tại sao? | Mỗi người có lý do riêng: cần đổi tiền, phòng hộ, đầu cơ, tái cân bằng, cắt lỗ |
| 5 | Trên chart thấy gì? | Chuỗi giá (giao dịch hoặc báo giá) theo thời gian, được gộp thành nến |
| 6 | ICT gọi là gì? | ICT nói về "the market", "price", "IPDA" — nhưng phần nền này là chung cho mọi trường phái |
| 7 | Ta không biết gì? | Ai đang giao dịch, vì sao, bao nhiêu lệnh đang chờ ở mỗi mức |
| 8 | Fact | Giá trên chart = kết quả của giao dịch/báo giá |
| 9 | Interpretation | "Thị trường đang muốn đi lên" — chỉ là cách nói |
| 10 | Hypothesis | (chưa có — phần này là định nghĩa) |

---

## 2. Buyer và Seller

### 2.1 TẦNG 1

```text
BUYER  — "Tôi muốn mua."
SELLER — "Tôi muốn bán."
```

Một người muốn mua mà không có ai bán → **không có giao dịch**. Một người muốn bán mà không có ai mua → **không có giao dịch**. Cần cả hai, **và** cần một mức giá mà cả hai cùng chấp nhận.

```text
Buyer
  ↕
Transaction   ← chỉ xảy ra khi có người chịu giao dịch ở MỘT mức giá
  ↕
Seller
```

### 2.2 TẦNG 2 — Ngộ nhận phải sửa ngay

> [!failure] "Giá tăng vì có nhiều người mua hơn người bán"
> **[MATHEMATICAL]** Trong một giao dịch, nếu ai đó mua 5 lot thì ai đó *bán đúng* 5 lot. Tổng khối lượng mua **luôn bằng** tổng khối lượng bán. Số *người* có thể khác (một quỹ mua 1.000 lot từ 200 người bán nhỏ), nhưng 1.000 = 1.000.
> Vì vậy "nhiều người mua hơn" không giải thích được gì về **cơ chế**.

![[IPDA-Deep-02-Moi-Giao-Dich-Hai-Phia.svg|760]]

**Vậy cái gì khác nhau?** Hai điều:

1. **Ai sốt ruột (chủ động)?** Người chấp nhận ngay giá mà phía kia đang rao → gọi là *aggressor*, dùng lệnh market. Người kiên nhẫn đặt sẵn giá và chờ → *passive*, dùng lệnh limit.
2. **Phía nào rút lui / nhượng bộ?** Người bán có thể rút lệnh hoặc nâng giá chào; người mua có thể rút lệnh hoặc nâng giá hỏi.

**Ví dụ số** (cùng 1.000 lot được giao dịch):

| | Kịch bản A — giá 100 → 103 | Kịch bản B — giá 100 → 97 |
|---|---|---|
| Ai chủ động? | Người mua dùng market, chấp nhận ask 101, 102, 103 | Người bán dùng market, chấp nhận bid 99, 98, 97 |
| Ai bị động? | Người bán chỉ đặt limit chờ | Người mua chỉ đặt limit chờ |
| Mua = Bán? | 1.000 = 1.000 ✓ | 1.000 = 1.000 ✓ |
| Kết quả | Giao dịch dịch lên | Giao dịch dịch xuống |

### 2.3 TẦNG 3

**[MARKET MECHANICS]** Trong microstructure, đại lượng có ý nghĩa là **order flow có dấu** (signed order flow): mỗi giao dịch được gán dấu + nếu bên khởi xướng là người mua (khớp ở ask), − nếu là người bán (khớp ở bid). Tổng có dấu trong một khoảng thời gian = *order flow imbalance* (theo nghĩa trade-based). Evans & Lyons (NBER 1999, xuất bản *Journal of Political Economy* 2002) cho thấy order flow liên ngân hàng giải thích **hơn 50%** biến động tỷ giá DM/$ theo ngày — trong khi các mô hình vĩ mô hiếm khi vượt 10%. Đây là bằng chứng mạnh rằng *dòng lệnh chủ động* là "nguyên nhân gần" (proximate cause) của biến động giá — dù nó chưa nói *vì sao* người ta gửi lệnh.

> [!quote] Câu cần nhớ
> **Volume không có phe.** Volume chỉ là số lot đã khớp. Hướng giá đến từ việc *phía nào vượt spread* và *phía nào rút/đặt lệnh chờ*.

---

## 3. Orders — lệnh

### 3.1 TẦNG 1

Một người nói: **"Tôi muốn mua táo ngay bây giờ."** → Họ sẽ mua ở quầy rẻ nhất *đang có*, dù giá bao nhiêu.

Một người khác nói: **"Tôi chỉ mua nếu giá xuống $1."** → Họ đứng chờ. Có thể chờ mãi.

Một người thứ ba dặn bạn: **"Nếu giá táo lên tới $1.20, hãy mua giúp tôi ngay, giá nào cũng được."** → Lời dặn này nằm im trong túi bạn cho tới khi giá chạm $1.20.

```text
MARKET ORDER — "Mua ngay!"
LIMIT ORDER  — "Tôi chỉ mua nếu giá tới X (hoặc tốt hơn)."
STOP ORDER   — "Nếu giá tới X, hãy kích hoạt lệnh (thành lệnh market)."
```

### 3.2 TẦNG 2 — Map sang trading

![[IPDA-Deep-03-Ba-Loai-Lenh.svg|760]]

| Loại | Khi nào khớp | Với liquidity | Bạn có nhìn thấy nó? | Rủi ro chính |
|---|---|---|---|---|
| **Market** | Ngay lập tức, ở giá tốt nhất đối diện | **Tiêu thụ** (taker) | Chỉ thấy *dấu vết* (giao dịch) | Trượt giá nếu sổ mỏng |
| **Limit** | Khi có người chấp nhận giá X | **Cung cấp** (maker) | Có — nếu sàn công bố độ sâu sổ lệnh | Không được khớp |
| **Stop** | Khi giá chạm X → thành market | Lúc chờ: **ẩn**; lúc kích hoạt: **tiêu thụ** | **Không** — cho tới khi kích hoạt | Trượt giá đúng lúc thị trường chạy nhanh |
| *Stop-limit* | Khi chạm X → thành limit ở Y | Lúc kích hoạt: cung cấp | Không | Có thể không khớp nếu giá nhảy qua Y |

**Stop order thường nằm ở đâu?** Đây là điểm nối quan trọng nhất với ICT về sau:

- **Buy stop** phía **trên** một đỉnh rõ ràng: stop-loss của người đang short (họ đặt stop "ngay trên đỉnh") + lệnh breakout của người muốn mua khi giá phá đỉnh.
- **Sell stop** phía **dưới** một đáy rõ ràng: stop-loss của người đang long + lệnh breakdown.

> [!warning] Chi tiết kỹ thuật dễ bị bỏ qua — bid chart và ask trigger
> **[MARKET MECHANICS]** Nền tảng MT4/MT5 mặc định vẽ chart theo **giá Bid**. Buy stop (và stop-loss của lệnh short) được kích hoạt theo **giá Ask**. Ask = Bid + spread. Nên khi spread giãn (mở phiên, tin tức, cuối ngày rollover), stop-loss của lệnh short có thể bị chạm **dù chart không hề in ra mức đó**. Trên chart bạn sẽ thấy "giá chưa chạm stop mà vẫn bị cắt" — không có gì bí ẩn, chỉ là spread.

### 3.3 TẦNG 3

**[MARKET MECHANICS]** Trên sàn có sổ lệnh như CME Globex, lệnh stop do sàn giữ và **không hiển thị** trong độ sâu sổ lệnh cho tới khi được kích hoạt. Trong FX OTC, stop của khách hàng nằm ở dealer/broker của họ (một dealer lớn có thể thấy tập trung stop của khách hàng *của mình* — đó chính là dữ liệu mà Osler đã nghiên cứu). Nghĩa là: **không có một nơi nào mà "toàn bộ stop của thị trường" hiện ra.** Mọi câu "có rất nhiều stop trên đỉnh này" là **suy luận** dựa trên hành vi điển hình — có cơ sở (mục 8.3), nhưng không phải quan sát.

### 3.4 Thẻ 10 câu — Orders

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Chỉ thị mua/bán kèm điều kiện về giá và thời điểm khớp |
| 2 | Tưởng tượng? | "Mua ngay" / "chỉ mua nếu rẻ" / "nếu giá tới X thì mua giúp tôi" |
| 3 | Thực sự xảy ra? | Market khớp ngay với lệnh chờ; limit nằm chờ; stop chờ điều kiện rồi thành market |
| 4 | Tại sao có nhiều loại? | Đánh đổi giữa *chắc chắn được khớp* (market) và *chắc chắn về giá* (limit); stop để tự động hóa cắt lỗ/breakout |
| 5 | Trên chart? | Chỉ thấy kết quả: giá in ra. Không thấy lệnh chờ, lệnh hủy, stop |
| 6 | ICT gọi? | "Buy stops / sell stops", "resting liquidity", "buy-side / sell-side liquidity" |
| 7 | Không biết gì? | Lượng stop/limit thực tế ở mỗi mức; ai đặt; bao nhiêu bị hủy trước khi chạm |
| 8 | Fact | Market tiêu thụ, limit cung cấp, stop kích hoạt thành market |
| 9 | Interpretation | "Trên đỉnh kia có nhiều stop" (dựa trên hành vi điển hình) |
| 10 | Hypothesis | "Khi giá vượt đỉnh rõ ràng, tốc độ di chuyển tăng hơn baseline" (test được — HYP-IPDA-005) |

---

## 4. Bid và Ask

### 4.1 TẦNG 1

```text
Người bán: "Tôi bán $101."
Người mua: "Tôi mua $100."
           ↓
Chưa có giao dịch ở $100/$101 — hai bên chưa đồng ý.
```

Nếu một người **chấp nhận mua ở $101**, giao dịch xảy ra ở **$101**. Nếu một người **chấp nhận bán ở $100**, giao dịch xảy ra ở **$100**. Khoảng giữa 100 và 101 là "vùng chưa ai đồng ý".

### 4.2 TẦNG 2

```text
ASK  101   ← giá thấp nhất mà một người bán ĐANG chịu bán
           ← spread = 1
BID  100   ← giá cao nhất mà một người mua ĐANG chịu mua
```

![[IPDA-Deep-04-So-Lenh-Bid-Ask-Spread.svg|760]]

**Câu then chốt của toàn bộ Phần A:** *Giá thay đổi vì giao dịch **có thể** xảy ra ở một mức giá mới.* Không phải vì giá "muốn" đi đâu.

### 4.3 TẦNG 3

**[MARKET MECHANICS]** Spread tồn tại vì người cung cấp thanh khoản (market maker, người đặt limit) chịu ba loại chi phí: (1) chi phí vận hành, (2) **rủi ro tồn kho** (inventory risk — họ phải giữ vị thế cho tới khi tìm được đối ứng ngược lại), (3) **rủi ro lựa chọn ngược** (adverse selection — có khả năng bên kia biết điều mình không biết). Khi rủi ro (2) và (3) tăng — trước tin tức, lúc thanh khoản mỏng — spread giãn ra và độ sâu co lại. Đây là lý do mở phiên và quanh tin tức là lúc giá dễ "nhảy".

| "Giá" trên chart nghĩa là gì? | Phổ biến ở |
|---|---|
| Giá giao dịch cuối (last) | Futures, cổ phiếu (sàn tập trung) |
| Giá Bid | MT4/MT5 FX & CFD (mặc định) |
| Giá Mid = (Bid + Ask)/2 | Một số nền tảng dữ liệu, nghiên cứu học thuật |

---

## 5. Price Discovery

### 5.1 TẦNG 1 — Hai người mặc cả

Hai người mặc cả một món đồ: "100 nghìn nhé?" — "Không, 130." — "110 thì sao?" — "120, không bớt nữa." — "Thôi được, 115?" — "OK, 115."

Không ai biết trước con số 115. Nó **được khám phá** qua quá trình hai bên thử và từ chối. Đó là trực giác của **price discovery**.

### 5.2 TẦNG 2

Trên thị trường, quá trình mặc cả này diễn ra giữa hàng nghìn người cùng lúc, bằng lệnh thay vì lời nói, và **không bao giờ dừng**:

![[IPDA-Deep-10-Price-Discovery-Vong-Lap.svg|760]]

1. **Thông tin & nhu cầu mới** xuất hiện: tin tức, dòng tiền thương mại, nhu cầu phòng hộ, một quỹ cần tái cân bằng, stop của ai đó bị chạm.
2. Người ta **gửi lệnh mới**: market, limit, hoặc **hủy** lệnh cũ.
3. Lệnh **khớp** ở một mức giá nào đó → giao dịch in ra.
4. **Mọi người thấy giá mới** → điều chỉnh: đặt lệnh mới, hủy lệnh, stop bị kích hoạt → quay lại bước 2.

### 5.3 TẦNG 3

**[MARKET MECHANICS]** *Price discovery là quá trình thị trường liên tục tìm kiếm mức giá mà tại đó người mua và người bán sẵn sàng giao dịch, bằng cách gộp thông tin phân tán (ở trong đầu hàng nghìn người) vào giá thông qua lệnh.* Các mô hình kinh điển (Kyle 1985; Glosten–Milgrom 1985) mô tả cách người có thông tin giao dịch, và cách người tạo lập thị trường cập nhật giá *từ chính dòng lệnh* họ nhìn thấy — dòng lệnh mua liên tục khiến họ suy ra "có thể có tin tốt" và nâng giá chào. Đó là lý do một chuỗi lệnh mua có thể làm giá tăng ngay cả khi người tạo lập *không biết* lý do đằng sau.

> [!note] Price discovery có hai "tốc độ"
> - **Nhanh:** vài mili-giây đến vài phút — thuật toán tạo lập cập nhật báo giá, stop bị chạm, tin tức ra.
> - **Chậm:** vài ngày đến vài tháng — thị trường tái định giá kỳ vọng lãi suất, tăng trưởng, rủi ro.
>
> Cả hai cùng tồn tại trên một chart. ICT dùng ngôn ngữ "delivery" cho cả hai thang — đây là một nguồn nhầm lẫn (mục 23).

### 5.4 Thẻ 10 câu — Price Discovery

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Quá trình liên tục tìm mức giá mà tại đó giao dịch còn xảy ra được |
| 2 | Tưởng tượng? | Hai người mặc cả cho tới khi gặp nhau ở 115 |
| 3 | Thực sự xảy ra? | Lệnh mới/hủy → khớp → giá mới → mọi người điều chỉnh → lặp |
| 4 | Tại sao? | Thông tin và nhu cầu liên tục thay đổi; không ai biết "giá đúng" từ trước |
| 5 | Trên chart? | Mỗi nến là bản tóm tắt (OHLC) của hàng nghìn vòng discovery |
| 6 | ICT gọi? | ICT dùng "price delivery" — nhấn mạnh *đường đi* hơn là *quá trình tìm giá* (mục 12) |
| 7 | Không biết gì? | Thông tin nào đang được "gộp" vào giá, ai mang thông tin đó |
| 8 | Fact | Giá là kết quả của giao dịch; giao dịch là kết quả của lệnh |
| 9 | Interpretation | "Thị trường đang định giá lại kỳ vọng X" |
| 10 | Hypothesis | "Dòng lệnh có dấu dự báo được biến động giá ngắn hạn" (đã có nhiều bằng chứng trong FX — Evans & Lyons) |

---

## 6. Vậy tại sao giá lại TĂNG?

> [!danger] Câu trả lời bị cấm
> "Vì buyers mạnh hơn." — "Vì có lực mua." — "Vì smart money mua." — "Vì IPDA muốn lên."
> Những câu này *gọi tên* hiện tượng, không *giải thích* cơ chế. Hãy hỏi tiếp: *lực mua nghĩa là gì? ai gửi lệnh gì? khớp ở đâu?*

### 6.1 TẦNG 1

Ba người bán đứng xếp hàng: A bán ở $100, B ở $101, C ở $102. Nếu người mua sốt ruột mua hết hàng của A, rồi của B, thì người mua tiếp theo chỉ còn C — giao dịch xảy ra ở $102.

```text
SELLER A → bán $100   (hết hàng)
SELLER B → bán $101   (hết hàng)
SELLER C → bán $102   ← giao dịch tiếp theo chỉ có thể ở đây
```

**Giá không có chân để chạy. Giá thay đổi vì *nơi* giao dịch tiếp theo xảy ra thay đổi.**

### 6.2 TẦNG 2 — Ví dụ số với sổ lệnh

![[IPDA-Deep-05-Gia-Tang-An-Qua-So-Lenh.svg|760]]

Sổ lệnh trước: ask 101 (200 lot), 102 (300), 103 (150), 104 (400); bid 100 (250), 99 (180). Một lệnh **market buy 600 lot** đến:

| Bước | Khớp | Còn thiếu | Giao dịch in ra |
|---|---|---|---|
| 1 | 200 @ 101 | 400 | 101 |
| 2 | 300 @ 102 | 100 | 102 |
| 3 | 100 @ 103 | 0 ✓ | 103 |

Sau lệnh: giao dịch cuối = **103**, best ask = 103 (còn 50), khoảng 101–102 phía bán **trống**. Trên chart M1 bạn chỉ thấy một nến xanh từ 100 lên 103 — không thấy đó là 1 lệnh 600 hay 60 lệnh 10, không thấy ai mua và vì sao.

### 6.3 TẦNG 3 — Hai cơ chế, không phải một

**[MARKET MECHANICS]** Giá có thể tăng theo **hai** đường, và cả hai thường xảy ra cùng lúc:

| Cơ chế | Điều gì xảy ra | Cần giao dịch lớn? | Ví dụ |
|---|---|---|---|
| **(a) Tiêu thụ thanh khoản** | Lệnh market mua "ăn" qua các tầng ask | Có | Ví dụ 6.2 |
| **(b) Điều chỉnh báo giá** | Người bán **hủy** ask hoặc nâng giá chào; người mua đặt bid **cao hơn** | **Không** — có thể gần như không có giao dịch | Market maker thấy dòng lệnh mua liên tục → tự nâng báo giá (Glosten–Milgrom); tin tốt ra → mọi người cùng dời báo giá lên |

Cont, Kukanov & Stoikov (2014, *Journal of Financial Econometrics*) đo trên dữ liệu NYSE: trong khoảng thời gian ngắn, thay đổi giá chủ yếu do **order flow imbalance** — tổng hợp của *cả* lệnh market, lệnh limit mới và lệnh hủy ở best bid/ask — với quan hệ gần tuyến tính, **độ dốc tỉ lệ nghịch với độ sâu**. Họ cũng chỉ ra quan hệ giữa giá và *volume giao dịch* thì nhiễu hơn nhiều. Bài học: **nhìn volume để đoán hướng là kém; nhìn sự mất cân bằng giữa hai phía của sổ lệnh tốt hơn** — và chart OHLC không cho bạn cái thứ hai.

**Công thức khái niệm** (không phải định luật):

```text
Δgiá (ngắn hạn)  ≈  λ × (dòng lệnh chủ động ròng + thay đổi lệnh chờ ròng)
λ  ~  1 / độ sâu thanh khoản gần giá
```

Kyle (1985) gọi λ là "độ nhạy giá với dòng lệnh" (*Kyle's lambda*). Với lệnh lớn được chia nhỏ (metaorder), tác động tăng theo **căn bậc hai** khối lượng chứ không tuyến tính — *square-root law* (Tóth et al. 2011) — vì thanh khoản gần giá hiện tại luôn "mỏng" một cách bất thường và được bổ sung dần khi giá đi.

### 6.4 Thẻ 10 câu — Vì sao giá tăng

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Giao dịch tiếp theo xảy ra ở mức cao hơn giao dịch trước |
| 2 | Tưởng tượng? | Quầy rẻ hết hàng, người mua tiếp theo phải tới quầy đắt hơn |
| 3 | Thực sự xảy ra? | (a) Lệnh market mua ăn hết các tầng ask; và/hoặc (b) ask bị rút / bid được nâng |
| 4 | Tại sao? | Ai đó cần mua *ngay* nhiều hơn lượng bán đang chờ ở giá hiện tại; hoặc người bán không còn chịu bán ở giá cũ |
| 5 | Trên chart? | Nến xanh, high mới; không thấy (a) hay (b) |
| 6 | ICT gọi? | "Price is being delivered higher", "bullish order flow", "displacement" (nếu nhanh) |
| 7 | Không biết gì? | Ai mua, vì sao, có phải một lệnh lớn hay nhiều lệnh nhỏ, có phải chỉ là rút ask |
| 8 | Fact | Giao dịch đã xảy ra ở mức cao hơn |
| 9 | Interpretation | "Có người mua lớn" (có thể chỉ là ask bị rút) |
| 10 | Hypothesis | "Order flow imbalance hôm nay dự báo hướng ngày mai" (thường yếu ở thang ngày — cần test) |

---

## 7. Vậy tại sao giá GIẢM?

Hoàn toàn đối xứng.

```text
BUYER A → mua $100   (đã được khớp hết)
BUYER B → mua $99    (đã được khớp hết)
BUYER C → mua $98    ← giao dịch tiếp theo chỉ có thể ở đây
```

![[IPDA-Deep-06-Gia-Giam-An-Qua-Bid.svg|760]]

Lệnh **market sell 500 lot** gặp bid 100 (150), 99 (250), 98 (300): khớp 150 @ 100, 250 @ 99, 100 @ 98 → giao dịch cuối **98**. Hoặc: người mua **rút** bid 100 và 99 (vì lo, vì thấy tin, vì thuật toán điều chỉnh) → best bid tự rơi xuống 98 mà gần như không có giao dịch.

> [!summary] Tổng hợp mục 6–7
> ```text
> PRICE MOVEMENT
>
> KHÔNG PHẢI:  "Giá tự chạy."
> MÀ LÀ:       "Giao dịch và price discovery đang xảy ra ở những mức giá khác nhau."
> ```
> Mức giao dịch tiếp theo phụ thuộc vào ba thứ: **(1)** phía nào đang chủ động vượt spread, **(2)** bao nhiêu lệnh chờ ở mỗi tầng, **(3)** lệnh chờ được thêm/rút nhanh thế nào. Không cần "ý chí" nào ở đây.

---

## 8. Tại sao giá đôi khi di chuyển RẤT NHANH?

Đây là cầu nối quan trọng nhất giữa microstructure và ICT, vì "displacement", "FVG", "liquidity run" đều là hình dạng của một lần giá đi nhanh.

### 8.1 TẦNG 1 — Đường trống

Một cửa hàng có hàng ở các mức $100, $101, $102, $103, $104 — mỗi mức chỉ một ít. Một đám đông ùa vào, ai cũng muốn mua **ngay**. Hàng ở mỗi mức hết trong chớp mắt:

```text
$100 → hết nhanh
$101 → hết nhanh
$102 → hết nhanh
$103 → hết nhanh
$104 → hết nhanh
```

Giá "chạy" từ 100 lên 104 trong vài giây. Một chiếc xe trên con đường **trống** có thể chạy rất nhanh.

### 8.2 TẦNG 2 — Sổ dày vs sổ mỏng

![[IPDA-Deep-07-So-Lenh-Day-vs-Mong.svg|760]]

Cùng một lệnh market buy 500 lot:

| | Sổ DÀY (1.000 lot/tầng) | Sổ MỎNG (100 lot/tầng) |
|---|---|---|
| Lệnh ăn được | Nửa tầng 101 | Sạch 5 tầng 101 → 105 |
| Giá đi | 100 → 101 (**+1**) | 100 → 105 (**+5**) |
| Trên chart | Nến nhỏ | Nến dài, có thể để lại khoảng trống |

**[SIMULATION]** IPDA-Sim-01 đưa **cùng một chuỗi** 400 lệnh market ngẫu nhiên vào hai sổ: độ lệch chuẩn của Δgiá mỗi bước là **0.20 tick** ở sổ dày so với **3.92 tick** ở sổ mỏng — gấp gần 20 lần, không cần thêm "ý định" nào. Panel C–D cho thấy khi độ sâu sụp 90% trong 12 bước *và* dòng lệnh trong lúc đó tình cờ một chiều, giá nhảy một đoạn dài; gộp thành nến thì thấy ngay **displacement + FVG**.

![[IPDA-Sim-01-Toy-Order-Book-Depth.png|900]]

### 8.3 TẦNG 3 — Năm nguồn tạo ra chuyển động nhanh

| # | Nguồn | Cơ chế | Bằng chứng / nhãn |
|---|---|---|---|
| 1 | **Sổ mỏng** | Ít lệnh chờ gần giá → mỗi lot chủ động dịch giá xa hơn | **[MARKET MECHANICS]** Kyle λ; Cont–Kukanov–Stoikov |
| 2 | **Rút thanh khoản trước sự kiện** | Market maker giảm báo giá trước tin (rủi ro lựa chọn ngược tăng) → sổ mỏng *đúng lúc* dòng lệnh mạnh | **[MARKET MECHANICS]** Biến động & spread quanh tin vĩ mô được ghi nhận rộng rãi (ví dụ Andersen & Bollerslev 1998 với DM/$) |
| 3 | **Dây chuyền stop (stop cascade)** | Giá chạm vùng stop → stop thành market → ăn ask → giá lên → chạm thêm stop → … | **[MARKET MECHANICS]** Osler 2002 (dữ liệu lệnh thật) |
| 4 | **Dòng lệnh một chiều** | Nhiều người cùng cần mua (tin, fix, tái cân bằng, margin call) → aggressor chỉ ở một phía | **[MARKET MECHANICS]** order flow (Evans & Lyons) |
| 5 | **Cú sốc thông tin** | Mọi người cùng dời báo giá → giá "nhảy" mà có khi rất ít giao dịch ở các mức giữa | **[MARKET MECHANICS]** cơ chế (b) mục 6.3 |

![[IPDA-Deep-08-Stop-Cascade.svg|760]]

**Về stop cascade** — vì đây là gốc của ý tưởng "buy-side liquidity": Osler (NY Fed Staff Report 125, 2001; Staff Report 150, 2002) phân tích lệnh take-profit và stop-loss thật tại một ngân hàng dealer FX lớn và thấy:

- Mức kích hoạt của các lệnh này **tập trung mạnh ở số tròn** (…00, …50).
- **Take-profit** tập trung *đúng tại* số tròn → có xu hướng **chặn/đảo** xu hướng (lệnh ngược chiều, "negative feedback").
- **Stop-loss mua** tập trung *ngay trên* số tròn, **stop-loss bán** *ngay dưới* → khi bị vượt, có xu hướng **đẩy nhanh** xu hướng ("positive feedback").
- Khi tỷ giá chạm các vùng stop đã được ghi nhận, xu hướng **nhanh bất thường** và hiệu ứng **kéo dài hàng giờ**; phản ứng với stop-loss mạnh và dài hơn phản ứng với take-profit.

> [!important] Ý nghĩa cho người học ICT
> Đây là phiên bản **có dữ liệu** của hai câu ICT: "giá chạy qua đỉnh để lấy buy stops" và "đỉnh/đáy rõ ràng là nơi liquidity nằm". Lưu ý phạm vi: Osler nghiên cứu **số tròn**, không phải swing high. Việc mở rộng sang "swing high rõ ràng" là **[INTERPRETATION]** hợp lý (trader cũng hay đặt stop ngay sau đỉnh/đáy) nhưng **chưa được kiểm chứng** trong nghiên cứu đó.

### 8.4 Giới hạn — OHLC che mất gần hết

> [!warning] Cảnh báo bắt buộc
> Chart OHLC không cho ta thấy bên trong order book. Một nến M5 dài 30 pip có thể là: một lệnh lớn; năm trăm lệnh nhỏ; một dây chuyền stop; market maker rút báo giá trước tin; hoặc kết hợp. **Năm cơ chế khác nhau cho cùng một hình dạng nến.** Vì vậy "displacement" là một *mô tả hình dạng*, không phải chẩn đoán nguyên nhân.

### 8.5 Thẻ 10 câu — Chuyển động nhanh

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Giá đi qua nhiều mức trong rất ít thời gian |
| 2 | Tưởng tượng? | Xe chạy trên đường trống; đám đông ùa vào cửa hàng ít hàng |
| 3 | Thực sự xảy ra? | Dòng lệnh chủ động lớn so với lượng lệnh chờ gần giá; có thể kèm stop bị kích hoạt dây chuyền |
| 4 | Tại sao? | Sổ mỏng, thanh khoản rút trước tin, stop cascade, dòng lệnh một chiều, sốc thông tin |
| 5 | Trên chart? | Nến dài, thân lớn, có thể để lại khoảng trống 3 nến |
| 6 | ICT gọi? | Displacement, "delivery mạnh", liquidity run, tạo FVG |
| 7 | Không biết gì? | Cơ chế nào trong năm cơ chế đã tạo ra nến đó; ai gửi lệnh |
| 8 | Fact | Giá đã đi xa trong thời gian ngắn; với futures có thể thấy volume tăng |
| 9 | Interpretation | "Có tổ chức tham gia mạnh" |
| 10 | Hypothesis | "Displacement sau sweep dự báo tiếp diễn tốt hơn displacement không sau sweep" (xem [[50-Displacement-In-Depth]]) |

---

## 9. Tại sao giá đôi khi gần như ĐỨNG YÊN?

### 9.1 TẦNG 1 — Đường đông người

Một chiếc xe đi trên con đường **đông người** khó chạy nhanh: mỗi mét đều phải lách qua ai đó. Nếu ở quanh mức giá hiện tại có rất nhiều người sẵn sàng mua *và* bán:

```text
$99  — rất nhiều người mua chờ
$100 — giá hiện tại
$101 — rất nhiều người bán chờ
```

thì mỗi lệnh mua đều bị người bán hấp thụ, mỗi lệnh bán đều bị người mua hấp thụ. Giá phải mất rất nhiều thời gian (và rất nhiều giao dịch) mới ra khỏi vùng đó.

### 9.2 TẦNG 2–3

```text
Nhiều thanh khoản sẵn có         Thanh khoản mỏng
        ↓                               ↓
Giao dịch dễ thực hiện          Price impact lớn hơn
        ↓                               ↓
Ít dịch chuyển giá / giao dịch  Có thể di chuyển nhanh hơn
```

Bốn lý do giá "đứng":

1. **Sổ dày** — nhiều lệnh limit hai phía (mục 8.2, sổ dày).
2. **Dòng lệnh hai chiều cân bằng** — mua chủ động và bán chủ động xen kẽ, triệt tiêu nhau.
3. **Hấp thụ (absorption)** — một người tham gia lớn liên tục bổ sung lệnh limit ở một mức (ví dụ một quỹ muốn bán dần) → mọi lệnh mua chủ động đều bị "nuốt", giá không qua được mức đó dù volume lớn.
4. **Tồn kho của market maker** — khi market maker đã mua quá nhiều, họ hạ báo giá để khuyến khích người khác mua lại từ họ → kéo giá về, tạo **mean reversion** ngắn hạn.

> [!warning] Không phải định luật
> "Nhiều thanh khoản → chậm, ít thanh khoản → nhanh" là **xu hướng**, không phải luật. Độ sâu thay đổi từng giây; người cung cấp thanh khoản có thể rút đi đúng lúc giá bắt đầu chạy (mục 8.3, nguồn 2). Một vùng "dày" có thể trở thành "mỏng" trong vài mili-giây.

---

## 10. Tại sao giá ĐỔI HƯỚNG — và vì sao chart có những high/low rõ ràng?

Brief yêu cầu trả lời câu này trước khi sang IPDA, vì toàn bộ "market structure" của ICT được xây trên swing high/low.

### 10.1 TẦNG 1

Bạn đi lên cầu thang tìm quầy táo. Lên tới tầng 5 thì gặp một quầy có **cả núi táo** rao $1.10, và người bán sẵn sàng bán cho bất kỳ ai. Không ai cần trả hơn $1.10 nữa. Những người mua sốt ruột đã mua xong. Giờ người bán lại phải hạ giá để tìm người mua mới. Tầng 5 trở thành **"đỉnh"**.

### 10.2 TẦNG 2–3 — Năm cơ chế đảo chiều

| # | Cơ chế | Mô tả | Nhãn |
|---|---|---|---|
| 1 | **Cạn người mua chủ động** | Những người cần mua *ngay* đã mua xong (stop đã kích hoạt hết, short đã cover xong) → không còn ai chấp nhận ask cao hơn | **[MARKET MECHANICS]** |
| 2 | **Gặp lệnh đối ứng lớn** | Take-profit tập trung (Osler), một người bán lớn đặt limit, hoặc người chờ "bán ở giá tốt" → hấp thụ dòng mua | **[MARKET MECHANICS]** |
| 3 | **Tồn kho dealer** | Market maker đã bán khống quá nhiều cho người mua → hạ báo giá / tìm người bán | **[MARKET MECHANICS]** |
| 4 | **Thông tin đổi** | Tin mới, dữ liệu vĩ mô, thay đổi kỳ vọng | **[MARKET MECHANICS]** |
| 5 | **Phản xạ sau dây chuyền** | Sau stop cascade, những ai mua do bị buộc (stop-loss của short) không phải người mua "tự nguyện" → khi chuỗi stop hết, dòng mua biến mất đột ngột | **[INTERPRETATION]** — cơ chế hợp lý, khớp với mô tả ICT về "sweep rồi đảo" |

**Vì sao high/low "rõ ràng"?** Một swing high là **điểm mà tại đó giao dịch tiếp theo ở mức cao hơn đã không xảy ra trong một khoảng thời gian** — vì một trong năm cơ chế trên. Sau khi hình thành, chính sự rõ ràng của nó khiến con người đặt lệnh quanh nó (stop ngay trên, limit sell gần nó, breakout buy stop trên nó) → nó trở thành nơi **lệnh tập trung** → lần sau giá quay lại, chuyện gì xảy ra ở đó phụ thuộc vào lượng lệnh nào lớn hơn. Đây là vòng phản hồi ở mục 26.

> [!caution] Hindsight
> Mọi swing high đều "rõ ràng" khi nhìn lại. Tại thời điểm nó đang hình thành, bạn không biết đó là đỉnh hay chỉ là một nhịp nghỉ. Đây là lý do mọi định nghĩa swing trong backtest phải có **độ trễ xác nhận** (xem [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]).

---

## 11. Liquidity là gì?

### 11.1 Đầu tiên: liquidity KHÔNG đơn giản có nghĩa là "stop loss"

Trong cộng đồng ICT, "liquidity" hay bị hiểu là "chỗ có stop loss". Đó chỉ là một phần nhỏ — và là phần *suy luận*.

### 11.2 TẦNG 1

Một chợ có **rất nhiều** người bán táo. Bạn muốn mua 100 quả: dễ, nhanh, giá gần như không đổi. Một chợ chỉ có hai người bán: mua 100 quả là bất khả — hoặc bạn phải trả giá rất cao. **Chợ thứ nhất "thanh khoản" hơn.**

### 11.3 TẦNG 2–3 — Ba nghĩa

![[IPDA-Deep-09-Ba-Nghia-Cua-Liquidity.svg|760]]

| | Nghĩa 1 — Thanh khoản (kinh tế học) | Nghĩa 2 — Liquidity pool (ICT) | Nghĩa 3 — "Lấy liquidity" (sự kiện ICT) |
|---|---|---|---|
| Định nghĩa | Khả năng giao dịch khối lượng lớn, nhanh, chi phí thấp mà giá không bị đẩy nhiều | Vùng giá nơi **nghi là** có nhiều lệnh chờ tập trung: trên swing high (BSL), dưới swing low (SSL), equal highs/lows | Giá giao dịch xuyên qua vùng đó (wick hoặc đóng nến) |
| Đo bằng | Spread, độ sâu sổ lệnh, price impact, thời gian hồi phục | **Không đo trực tiếp được** trên chart retail; suy từ hình học + hành vi điển hình | Quan sát được: high/low bị vượt |
| Nhãn | **[MARKET MECHANICS]** | **[ICT FRAMEWORK]** + **[INTERPRETATION]** (cơ sở một phần: Osler) | **[OBSERVABLE]** (sự kiện) + **[INTERPRETATION]** (ý nghĩa) |
| Ví dụ | EURUSD giờ London thanh khoản hơn 4h sáng thứ Hai | "Equal highs trên H1 = BSL" | "Giá đã sweep PDH" |

> [!important] Nghịch lý cần hiểu
> Vùng mà ICT gọi là "có nhiều liquidity" (nghĩa 2) thường là nơi giá chạy **nhanh** qua khi bị chạm — vì stop biến thành lệnh market *tiêu thụ* thanh khoản (nghĩa 1). Tức là "nhiều liquidity theo nghĩa ICT" có thể đi kèm "thanh khoản tạm thời mỏng theo nghĩa kinh tế học". Từ "liquidity" trong ICT gần nghĩa **"lệnh đối ứng tiềm năng"** hơn là "độ sâu thị trường".

**Câu chuyển tiếp sang ICT:** *Trong ICT, từ "liquidity" được dùng theo nghĩa rộng hơn để mô tả những vùng giá nơi có khả năng tập trung lệnh chờ — đặc biệt là stop — mà một người cần giao dịch khối lượng lớn có thể dùng làm đối ứng.* Mục 20 giải thích vì sao điều đó quan trọng.

### 11.4 Thẻ 10 câu — Liquidity

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | (1) khả năng giao dịch lớn mà ít ảnh hưởng giá; (2) ICT: vùng nghi có nhiều lệnh chờ |
| 2 | Tưởng tượng? | Chợ đông người bán / "chỗ hẹn" mà nhiều người đặt lệnh |
| 3 | Thực sự xảy ra? | Lệnh chờ (limit + stop chưa kích hoạt) nằm ở các mức giá; khi giá tới, chúng được khớp |
| 4 | Tại sao lệnh tập trung? | Con người dùng mốc giống nhau: số tròn, đỉnh/đáy rõ, high/low ngày/tuần trước |
| 5 | Trên chart? | Chỉ thấy *mốc* (đỉnh, đáy, số tròn) và *sự kiện* (bị vượt). Không thấy lượng lệnh |
| 6 | ICT gọi? | BSL, SSL, liquidity pool, resting liquidity, external/internal range liquidity |
| 7 | Không biết gì? | Lượng lệnh thật, bao nhiêu đã bị hủy trước, ai là đối ứng |
| 8 | Fact | Lệnh stop/TP tập trung quanh số tròn (Osler); stop kích hoạt thành market |
| 9 | Interpretation | "Đỉnh H1 này có nhiều buy stop" |
| 10 | Hypothesis | "Vượt swing high rõ → tốc độ tăng hơn baseline" (HYP-IPDA-005); "sau khi vượt, xác suất đảo cao hơn baseline" (HYP-IPDA-006) |

---

> [!check] Kiểm tra giữa chặng — giải thích không dùng một thuật ngữ ICT nào
> *"Giá EURUSD vừa tăng 30 pip trong 2 phút rồi quay đầu. Vì sao?"*
>
> **Trả lời mẫu:** Giá đang ở gần một mức mà nhiều người đã đặt lệnh "nếu giá vượt mức này thì mua" (người bán khống đặt cắt lỗ ở đó, người theo breakout đặt lệnh chờ ở đó). Khi những giao dịch đầu tiên in ra trên mức đó, các lệnh này tự động biến thành lệnh mua ngay. Phía bán lúc ấy không có nhiều lệnh chờ — có thể vì người bán đã rút bớt trước giờ ra tin — nên mỗi lệnh mua phải khớp ở mức cao hơn mức trước, và giá chạy rất nhanh. Khi các lệnh "buộc phải mua" đã chạy hết, không còn ai cần mua ngay; trong khi một số người đã đặt sẵn lệnh bán ở vùng cao đó (chốt lời, hoặc bán chờ giá tốt). Họ trở thành phía chủ động, và giao dịch bắt đầu xảy ra ở các mức thấp dần.
>
> Nếu bạn viết được đoạn như trên, bạn đã hiểu *tại sao giá di chuyển*. Phần B chỉ là đặt tên cho các bước của đoạn này — và hỏi xem cái tên đó thêm được gì.

---

# PHẦN B — PRICE DELIVERY VÀ IPDA

> [!note] Từ đây ICT được phép xuất hiện
> Nhưng luật vẫn giữ nguyên: mỗi thuật ngữ ICT phải **trỏ được về** một bước cơ chế ở Phần A. Thuật ngữ nào không trỏ được thì được dán nhãn **[INTERPRETATION]**, **[HYPOTHESIS]** hoặc **[UNSUPPORTED CLAIM]**.

---

## 12. Price Delivery là gì?

### 12.1 TẦNG 1 — Chiếc xe đi qua các trạm

Hãy tưởng tượng giá là một chiếc xe. Xe đang ở **A**. Sau đó nó đi qua **B** (trạm xăng), **C** (bến đông khách), rồi tới **D**. Quá trình chiếc xe đi từ A tới D — qua những trạm nào, theo thứ tự nào, nhanh hay chậm ở đoạn nào — là hình ảnh của **"price delivery"**.

![[IPDA-Deep-11-Price-Delivery-Chiec-Xe.svg|760]]

### 12.2 TẦNG 2 — Trên chart

```text
Giá hiện tại (A)
      ↓   giá quay lại giao dịch trong một FVG bên dưới  (B — internal liquidity)
      ↓   giá chạy lên vượt đỉnh cũ                       (C — external liquidity / BSL)
      ↓   giá đi tìm vùng tiếp theo                        (D)
```

ICT đọc chuỗi này là: *"giá được delivery từ A, rebalance FVG, lấy buy-side liquidity, rồi hướng tới vùng kế tiếp"*.

### 12.3 TẦNG 3 — Định nghĩa

**[ICT FRAMEWORK]** *Price delivery là cách ICT mô tả quá trình giá được đưa từ mức/vùng này sang mức/vùng khác theo thời gian, đọc qua các mốc liquidity (đỉnh, đáy) và các vùng giá mà giá đã đi qua quá nhanh (FVG, imbalance).*

Map về Phần A — *cái gì thực sự xảy ra* trong mỗi đoạn:

| ICT nói | Cơ chế ở Phần A |
|---|---|
| "Giá được delivery lên" | Giao dịch liên tiếp xảy ra ở mức cao hơn (mục 6) |
| "Giá rebalance FVG" | Giá quay lại giao dịch ở vùng mà trước đó nó đi qua rất nhanh, ít giao dịch (mục 27) |
| "Lấy BSL" | Giá giao dịch trên đỉnh cũ; stop/breakout order (nếu có) được kích hoạt (mục 8.3) |
| "Delivery nhanh / displacement" | Dòng lệnh chủ động lớn so với độ sâu (mục 8) |
| "Delivery chậm / consolidation" | Sổ dày, dòng lệnh hai chiều, hấp thụ (mục 9) |

> [!warning] Nhấn mạnh
> Price delivery là **thuật ngữ của framework**, không phải một vật thể vật lý trong thị trường. Không có "dòng delivery" nào chảy trong dây cáp của sàn. Có lệnh, có khớp lệnh, có giá in ra. "Delivery" là cái tên ta đặt cho **hình dạng của chuỗi giá in ra**.

### 12.4 Giới hạn của ẩn dụ chiếc xe

1. Xe có tài xế và điểm đến. **Giá không có tài xế nhìn thấy được.**
2. Bản đồ hành trình A→B→C được **vẽ sau** khi xe đã đi. Khi giá đang ở A, ta chỉ có một **danh sách** điểm đến có thể.
3. "Delivery" mô tả *đường đi đã xảy ra*; không chứng minh có *người giao hàng*.

### 12.5 Thẻ 10 câu — Price Delivery

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Từ vựng ICT mô tả đường đi của giá giữa các vùng theo thời gian |
| 2 | Tưởng tượng? | Chiếc xe đi qua các trạm A → B → C → D |
| 3 | Thực sự xảy ra? | Chuỗi giao dịch ở các mức khác nhau — nhanh ở chỗ sổ mỏng/stop, chậm ở chỗ sổ dày |
| 4 | Tại sao đường đi có hình dạng đó? | Phân bố lệnh chờ, dòng lệnh chủ động, tin tức, thời gian trong ngày |
| 5 | Trên chart? | Chuỗi nến đi từ vùng này sang vùng khác; các đỉnh/đáy bị vượt; các FVG được lấp |
| 6 | ICT gọi? | Price delivery, delivery leg, "delivering to", "seeking liquidity", "rebalancing" |
| 7 | Không biết gì? | Đích đến tiếp theo; có "ai" chủ đích đưa giá đi không |
| 8 | Fact | Giá đã đi từ A tới B qua những mức đó |
| 9 | Interpretation | "Giá đi lên *để* lấy BSL" (từ "để" là diễn giải mục đích) |
| 10 | Hypothesis | "Sau khi lấy external liquidity, giá có xác suất cao hơn baseline quay về internal (FVG)" (HYP-IPDA-007) |

---

## 13. Tại sao ICT dùng khái niệm "Price Delivery"?

### 13.1 Mục đích: đổi câu hỏi

Trader thông thường nhìn: *"Nến tăng hay giảm? Có mẫu hình nến gì?"*

ICT muốn trader hỏi: *"Giá đang được đưa **từ đâu → tới đâu**? Nó vừa rời vùng nào, đang đi qua vùng nào, vùng nào còn chưa được giao dịch lại, mốc liquidity nào còn nguyên?"*

```text
CURRENT PRICE
      ↓
Internal Liquidity (FVG, OB — vùng bên trong range)
      ↓
External Liquidity (đỉnh/đáy của range)
      ↓
Next Price Area
```

Đây là một đóng góp **có giá trị thật** của framework, bất kể IPDA có tồn tại theo nghĩa đen hay không: nó buộc trader **nhìn cấu trúc của đường đi** thay vì nhìn từng nến rời rạc, và buộc phải **gọi tên mục tiêu và vùng sai** trước khi vào lệnh.

### 13.2 Câu hỏi bắt buộc: giá có "biết" đích đến trước không?

> [!question] Price có thực sự "biết" destination trước không?
> **Không thể biết chắc từ chart.** Chart chỉ cho thấy đường đi *đã* xảy ra. Cùng một đường đi tương thích với ít nhất ba câu chuyện:
> 1. Có một (nhóm) người tham gia chủ đích đưa giá tới đó. **[UNKNOWN]**
> 2. Nhiều người độc lập, mỗi người có lý do riêng, tình cờ tạo ra đường đi đó; các mốc liquidity chỉ ảnh hưởng *tốc độ* tại chỗ (stop cascade). **[MARKET MECHANICS]** cho phần cơ chế.
> 3. Đường đi là ngẫu nhiên và các "trạm" được ta vẽ thêm sau. **[SIMULATION]** IPDA-Sim-03 cho thấy nhiễu thuần cũng sinh ra "trạm".
>
> **Do đó: price delivery target là một HYPOTHESIS, không phải lời tiên tri.**

---

## 14. IPDA là gì?

Giờ — và chỉ giờ — mới hỏi: **IPDA là gì?**

### 14.1 Giải phẫu cái tên

![[IPDA-Deep-12-Phan-Ra-Ten-IPDA.svg|760]]

| Chữ | Từ | Gợi ý điều gì | Ta quan sát được | Ta KHÔNG quan sát được | Nhãn |
|---|---|---|---|---|---|
| **I** | **Interbank** (ICT gốc) / *Institutional* (cách gọi khác) | Giá được hình thành trong mạng lưới ngân hàng–dealer–tổ chức | FX là OTC phi tập trung, ≈ 9.6 nghìn tỷ USD/ngày; có dealer, ECN, market maker, quỹ | Ai cụ thể đang giao dịch, ý định gì | **[MARKET MECHANICS]** + **[UNKNOWN]** |
| **P** | **Price** | Đối tượng của mô hình là giá | Giá, thời gian, OHLC từ feed bạn dùng | "Giá thật" duy nhất của FX (không tồn tại) | **[OBSERVABLE]** |
| **D** | **Delivery** | Giá được "giao" từ vùng này tới vùng khác — có chủ đích | Giá *đã* đi từ A tới B | "Chủ đích" | **[ICT FRAMEWORK]** + **[INTERPRETATION]** |
| **A** | **Algorithm** | Quá trình có quy tắc, có hệ thống, lặp lại | Có rất nhiều thuật toán thật trong thị trường | Một thuật toán *duy nhất* tên IPDA điều khiển giá | **[HYPOTHESIS]** (pattern) / **[UNSUPPORTED CLAIM]** (literal) |

> [!note] "Interbank" hay "Institutional" — khác nhau ở đâu?
> - **Interbank** chỉ một *nơi*: thị trường liên ngân hàng FX (dealer giao dịch với dealer). ICT phát triển ý tưởng này chủ yếu cho FX, rồi áp dụng sang futures chỉ số.
> - **Institutional** chỉ một *loại người tham gia*: tổ chức (ngân hàng, quỹ, công ty quản lý tài sản…). Từ này dễ gợi ý "các tổ chức hành động như một khối" — điều sai về thực tế (mục 17).
> - Với mục đích học: dùng tên **IPDA**, nhưng khi giải thích luôn nói rõ *bạn đang nói về cơ chế (dòng lệnh, stop, thanh khoản) hay về một chủ thể (ai đó)*.

### 14.2 ICT nói IPDA làm gì? (theo tóm tắt của cộng đồng)

**[ICT FRAMEWORK]** — các ý dưới đây là cách cộng đồng tóm tắt bài giảng ICT; **không** phải trích nguyên văn:

1. **Giá được "delivery" chứ không chỉ được "discover".** Mỗi chuyển động phục vụ một trong hai việc: **(I)** tìm tới **liquidity** (đỉnh/đáy nơi có stop), hoặc **(II)** **rebalance** một vùng mất cân bằng (FVG / imbalance / inefficiency).
2. **IPDA Data Ranges:** nhìn lại **20, 40, 60 ngày giao dịch** trên D1 để xác định các mức tham chiếu ngắn/trung/dài hạn; kèm ý tưởng **"look forward"** (chiếu các mức này về phía trước) và **"quarterly shift"** — thị trường thường đổi pha sau khoảng **3–4 tháng**.
3. **Thời gian quan trọng như giá:** killzones, macro times, các mốc mở cửa (midnight open, daily/weekly open) là nơi "thuật toán" được cho là hoạt động (xem [[18-Kill-Zones]], [[40-Macro-Times]]).
4. **PD Arrays** (FVG, OB, breaker, mitigation block…) là "điểm tham chiếu" mà giá được cho là tương tác khi được delivery giữa các vùng liquidity.

### 14.3 Định nghĩa làm việc (v0.1) cho note này

> [!abstract] IPDA — định nghĩa làm việc v0.1
> **IPDA là mô hình khái niệm của ICT dùng để mô tả và đặt giả thuyết về đường đi của giá (price delivery) theo ba trục — GIÁ, THỜI GIAN, LIQUIDITY — với giả định rằng đường đi đó có tính hệ thống: giá có xu hướng di chuyển giữa các vùng tập trung lệnh (external liquidity) và các vùng nó đã đi qua quá nhanh (internal / inefficiency), trong các khung thời gian lặp lại.**
>
> - *Phần mô tả* (đường đi giữa các vùng) → **[ICT FRAMEWORK]**, luôn áp dụng được.
> - *Phần "có tính hệ thống"* → **[HYPOTHESIS]**, phải kiểm chứng.
> - *Phần "do một thuật toán thực hiện"* → **không** nằm trong định nghĩa này. Xem mục 15.

### 14.4 Thẻ 10 câu — IPDA

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Mô hình khái niệm của ICT về đường đi của giá theo giá–thời gian–liquidity |
| 2 | Tưởng tượng? | Một tấm bản đồ ghi các "trạm" mà giá hay đi qua, và giờ nào giao thông đông |
| 3 | Thực sự xảy ra? | Lệnh → khớp → giá; stop gom quanh mốc rõ ràng; biến động tập trung theo phiên |
| 4 | Tại sao ICT cần nó? | Để biến chuỗi nến hỗn loạn thành một câu chuyện có điểm xuất phát, điểm đến và vùng sai |
| 5 | Trên chart? | Không có "IPDA" trên chart. Chỉ có giá, các mốc và đường đi |
| 6 | ICT gọi? | Interbank Price Delivery Algorithm |
| 7 | Không biết gì? | Có tồn tại một quy trình hệ thống như mô tả không; nếu có, ai/cái gì thực hiện |
| 8 | Fact | Giá đi giữa các vùng; stop tập trung quanh mốc; biến động theo phiên có thật |
| 9 | Interpretation | "Đường đi này do thuật toán tạo ra" |
| 10 | Hypothesis | Các mức IPDA được chạm/phản ứng nhiều hơn baseline (HYP-IPDA-001…008) |

---

## 15. IPDA có thực sự tồn tại không?

### 15.1 Tách cái nhìn thấy được khỏi cái không nhìn thấy

![[IPDA-Deep-13-Tang-Bang-Quan-Sat.svg|760]]

| OBSERVABLE — nhìn thấy được | NOT DIRECTLY OBSERVABLE — không nhìn thấy trực tiếp |
|---|---|
| Giá | "IPDA engine" |
| Thời gian | Ý định chính xác của tổ chức |
| High, low | Thuật toán chính xác của tổ chức |
| Biến động | Lệnh riêng của người tham gia |
| Volume (futures; FX chỉ có tick volume của broker) | Lý do chính xác vì sao giá di chuyển |
| Một số proxy của liquidity (số tròn, đỉnh/đáy rõ, độ sâu nếu sàn công bố) | Lượng stop thật ở mỗi mức |
| Cấu trúc swing | Lịch sử sổ lệnh đầy đủ (với trader retail) |

**Kết luận bắt buộc:** **Không được biến IPDA từ một mô hình khái niệm thành một vật thể vật lý.** Câu "IPDA đã làm X" phải luôn được đọc là "đường đi của giá *tương thích với* mô tả X của mô hình IPDA".

### 15.2 Ba cách hiểu — chọn cách nào?

![[IPDA-Deep-14-Ba-Cach-Hieu-IPDA.svg|760]]

| | A. Robot trung tâm | B. Quy luật nổi lên (emergent) | C. Ngôn ngữ mô tả |
|---|---|---|---|
| Claim | Một thuật toán duy nhất quyết định giá đi đâu | Nhiều người + nhiều thuật toán thật tạo ra mẫu hình lặp lại | IPDA là bộ từ vựng để tổ chức quan sát |
| Bằng chứng | Không có bằng chứng công khai | Một phần có (stop cascade, biến động theo phiên, order flow) | Không cần — nó là công cụ |
| Falsify được? | **Không** — mọi kết quả đều "giải thích" được sau khi xảy ra | **Có** — so với baseline | Không áp dụng; đánh giá bằng hữu ích |
| Nhãn | **[UNSUPPORTED CLAIM]** | **[HYPOTHESIS]** | **[INTERPRETATION]** |
| Dùng trong note? | ❌ | ✅ | ✅ |

> [!tip] Vì sao cách hiểu A nguy hiểm cho trader
> Nếu bạn tin có một robot biết trước đích đến, mọi lệnh thua sẽ được giải thích là "mình đọc sai IPDA" thay vì "đây là xác suất". Bạn sẽ liên tục tìm "cách đọc đúng hơn" — tức là overfit vào quá khứ. Cách hiểu B + C cho phép bạn thua mà không phải sửa framework mỗi lần.

---

## 16. IPDA có phải "ai điều khiển thị trường" không?

### 16.1 Trả lời trực tiếp

**Không nên hiểu như vậy.**

### 16.2 TẦNG 1

Không có một "ông vua" ngồi sau thị trường và nói: *"Hôm nay EURUSD phải đi tới 1.2500."* Thị trường giống một con phố lớn với hàng triệu người, mỗi người đi việc riêng: người đi làm, người đi chợ, người chạy bộ. Dòng người có những lúc đông ở ngã tư (giờ cao điểm), có những đoạn đường ai cũng tránh (công trình). Nhìn từ trên cao, dòng người có **hình dạng** — nhưng không có ai điều khiển từng bước chân.

### 16.3 TẦNG 2–3 — Thị trường có những ai, muốn gì?

| Người tham gia | Họ muốn gì | Hệ quả lên giá |
|---|---|---|
| Ngân hàng dealer / market maker | Kiếm spread, quản lý tồn kho, phục vụ khách hàng | Báo giá hai chiều; điều chỉnh báo giá theo dòng lệnh |
| Ngân hàng trung ương | Ổn định tiền tệ, đôi khi can thiệp | Hiếm, nhưng có thể rất lớn |
| Doanh nghiệp xuất nhập khẩu | Đổi tiền để thanh toán, phòng hộ | Dòng lệnh không nhạy giá |
| Công ty quản lý tài sản, quỹ hưu trí | Mua tài sản nước ngoài, tái cân bằng, phòng hộ tỷ giá | Dòng lệnh lớn, thường vào cuối tháng/quý, quanh fix |
| Quỹ đầu cơ, CTA | Lợi nhuận từ xu hướng, vĩ mô, chênh lệch | Có thể khuếch đại xu hướng |
| HFT / prop firm | Lợi nhuận rất ngắn hạn từ báo giá, độ trễ | Cung cấp và rút thanh khoản rất nhanh |
| Trader retail (qua broker) | Lợi nhuận đầu cơ | Thường được broker gộp, hedge, hoặc giữ nội bộ |

**[MARKET MECHANICS]** Những người này có **mục tiêu mâu thuẫn nhau**. Không có cơ chế nào khiến họ phối hợp như một khối. Ngay cả trong một ngân hàng, bàn tạo lập thị trường và bàn quản lý tài sản có thể đứng ở hai phía.

### 16.4 Thao túng có xảy ra không?

**[MARKET MECHANICS — lịch sử]** Có — **cục bộ, có thật, và bị phạt**. Trong hai năm 2014–2015, nhà chức trách Anh, Mỹ, Thụy Sĩ đã phạt nhiều ngân hàng lớn tổng cộng hàng tỷ USD vì trader của họ thông đồng qua các phòng chat để tác động tới benchmark tỷ giá (WM/Reuters fix) và lạm dụng thông tin lệnh của khách hàng.

Điều này cho ta biết hai thứ, và **không** cho ta biết thứ ba:

1. ✅ Hành vi lợi dụng lệnh khách hàng / tác động giá trong cửa sổ ngắn **là có thể** — đủ để ý tưởng "săn stop" không phải hoàn toàn hoang đường ở quy mô cục bộ.
2. ✅ Khi xảy ra, nó **bị phát hiện qua dữ liệu và chat log**, bị truy tố, bị phạt — tức là nó *không phải* trạng thái vận hành bình thường được hệ thống hóa.
3. ❌ Nó **không** chứng minh có một thuật toán trung tâm điều phối giá mỗi ngày.

```text
ICT MODEL (công cụ mô tả đường đi)
        vs
Literal Central Controller (một bộ não điều khiển)  ← KHÔNG có bằng chứng
```

---

## 17. "Institutional" (và "Interbank") trong IPDA

### 17.1 "Institutional" không đồng nghĩa với một tổ chức duy nhất

Không được nói: *"Institutional traders điều khiển giá."* Thay vào đó, hãy hỏi: **những loại tổ chức nào, và họ để lại dấu vết gì trên chart?**

| Loại | Dấu vết *có thể* thấy | Có chắc là họ? |
|---|---|---|
| Market maker điều chỉnh tồn kho | Mean reversion ngắn hạn, giá "nảy" quanh một mức | Không |
| Quỹ thực thi lệnh lớn bằng TWAP/VWAP | Xu hướng đều, ít pullback trong vài giờ | Không |
| Lệnh quanh fix (16:00 London) | Biến động tăng quanh 15:55–16:05 London | Biết là có dòng lệnh fix, không biết của ai |
| Stop cascade | Nến dài khi vượt mốc rõ ràng | Biết cơ chế, không biết của ai |
| Can thiệp ngân hàng trung ương | Cú nhảy rất lớn, thường được công bố sau | Đôi khi được xác nhận sau |

### 17.2 Câu hỏi then chốt

> [!question] Chart có cho chúng ta biết chính xác ai đang mua/bán không?
> **Không.** Trên chart retail, mọi giao dịch đều vô danh. Ngay cả với dữ liệu futures có volume, bạn chỉ biết *bao nhiêu* đã khớp và (với dữ liệu tick) *phía nào chủ động*, không biết *ai*.
>
> **Do đó: danh tính người tham gia không thể được suy ra chắc chắn chỉ từ price chart.** Câu "smart money đang tích lũy" phải được viết lại thành "giá đang đi ngang trong khi [quan sát cụ thể]; một cách diễn giải là có người tham gia lớn đang hấp thụ lệnh bán" — kèm nhãn **[INTERPRETATION]**.

---

## 18. "Algorithm" trong IPDA

### 18.1 TẦNG 1 — Robot làm bánh

Một robot làm bánh có quy tắc:

```text
Cho bột → Cho nước → Trộn → Nướng 20 phút → Bánh
```

Đó là một **algorithm**: một chuỗi bước rõ ràng, lần nào cũng làm giống nhau, ai đọc quy tắc cũng làm lại được.

### 18.2 Câu hỏi: IPDA có rulebook rõ ràng như vậy không?

Nếu IPDA là một algorithm theo nghĩa robot làm bánh, phải có một danh sách bước mà ai cũng làm lại được, cho ra cùng kết quả. Trong thực tế:

- ICT đưa ra **khái niệm và ví dụ**, không đưa ra quy tắc đủ để hai người độc lập luôn ra cùng một dự đoán.
- Cùng một chart, hai trader ICT có thể chọn hai DOL khác nhau, hai FVG khác nhau, hai "data range" khác nhau (cộng đồng ghi nhận ICT "linh hoạt" với cách tính data range).

→ Đó là đặc điểm của một **mô hình khái niệm** (conceptual model), không phải **thuật toán theo nghĩa đen** (literal algorithm).

### 18.3 TẦNG 3 — Thuật toán thật trong thị trường

**[MARKET MECHANICS]** Thị trường hiện đại **có** tính thuật toán rất cao — nhưng là **số nhiều**:

| Loại thuật toán | Làm gì | Ảnh hưởng tới giá |
|---|---|---|
| **Thực thi** (TWAP, VWAP, POV, iceberg) | Chia lệnh lớn thành nhiều lệnh nhỏ theo thời gian/khối lượng | Áp lực đều một chiều trong nhiều giờ |
| **Tạo lập thị trường** | Báo giá hai chiều, điều chỉnh theo tồn kho và dòng lệnh | Spread, độ sâu, mean reversion ngắn hạn |
| **HFT / arbitrage** | Đồng bộ giá giữa các nơi giao dịch, khai thác độ trễ | Giữ giá các venue gần nhau; rút thanh khoản khi biến động |
| **Quản trị rủi ro / stop** | Tự động cắt lỗ, margin call | Dây chuyền khi giá vượt mốc |
| **Fix / benchmark** | Thực thi lệnh tại giá fix | Biến động quanh giờ fix |

> [!important] Phân biệt bắt buộc
> | | Literal algorithm | Conceptual model |
> |---|---|---|
> | Định nghĩa | Một chương trình cụ thể, với quy tắc cụ thể, đang chạy ở đâu đó | Một cách mô tả có hệ thống về hành vi quan sát được |
> | "Thị trường có nhiều thuật toán" | ✅ đúng | — |
> | "Có MỘT thuật toán tên IPDA điều khiển giá" | ❌ không có bằng chứng | — |
> | "Đường đi của giá có thể được mô tả *như thể* có quy tắc" | — | ✅ đây là cách dùng hợp lý của IPDA |

---

## 19. IPDA có "đẩy giá" không?

Không dùng câu *"IPDA pushes price"*. Hãy hỏi: **cái gì thực sự xảy ra trên market?**

```text
Orders  →  Execution  →  Price Discovery  →  Price Movement     ← [MARKET MECHANICS]
```

ICT có thể mô hình hóa quá trình đó bằng:

```text
Price Delivery  →  Liquidity  →  DOL                               ← [ICT FRAMEWORK]
```

**Đây là framework để diễn giải price movement**, không phải nguyên nhân thứ hai đứng *song song* với lệnh và khớp lệnh.

### 19.1 Bảng dịch "ngôn ngữ ICT → ngôn ngữ cơ chế"

| Câu ICT thường gặp | Viết lại bằng cơ chế | Phần còn lại là gì? |
|---|---|---|
| "IPDA đẩy giá lên lấy BSL" | Lệnh mua chủ động + stop bị kích hoạt trên đỉnh làm giao dịch xảy ra ở mức cao hơn | "Đẩy *để* lấy" = diễn giải mục đích **[INTERPRETATION]** |
| "Thuật toán quay lại rebalance FVG" | Giá quay lại giao dịch trong vùng nó đã đi qua nhanh | "Để rebalance" = mục đích; xác suất quay lại cao hơn baseline? **[HYPOTHESIS]** |
| "Smart money đã tích lũy ở discount" | Giá đi ngang ở nửa dưới range trước khi tăng | Danh tính & ý định **[UNKNOWN]**; "tích lũy" = nhãn đặt sau khi giá tăng (rủi ro hindsight) |
| "IPDA đang chạy chương trình bán" | Một chuỗi nến giảm liên tiếp | "Chương trình" = **[UNSUPPORTED CLAIM]** nếu hiểu theo nghĩa đen |
| "Macro 9:50 là lúc thuật toán khai hỏa" | Biến động thường tăng quanh một số mốc giờ (mở cửa, tin) | Hiệu ứng theo giờ: một phần **[MARKET MECHANICS]**; "khai hỏa" **[INTERPRETATION]** |

---

## 20. Tại sao ICT nói về liquidity?

### 20.1 TẦNG 1

Bạn muốn **bán** 1.000 quả táo cùng lúc. Trong chợ bình thường, mỗi phút chỉ có vài người mua → bạn phải hạ giá rất nhiều mới bán hết. Nhưng nếu có một **lúc** mà hàng trăm người cùng ùa tới muốn mua ngay (ví dụ: vừa có thông báo "táo sắp khan hiếm") — đó là lúc **tốt nhất** để bạn bán 1.000 quả mà không phải hạ giá.

### 20.2 TẦNG 2–3 — Phiên bản cơ chế của "price seeks liquidity"

**[MARKET MECHANICS]** Người cần giao dịch khối lượng **lớn** gặp một vấn đề: lệnh của họ tự đẩy giá đi ngược lại họ (price impact, mục 6.3). Muốn bán nhiều mà giá không sụp, họ cần **nhiều người mua cùng lúc** làm đối ứng.

Ở đâu có nhiều người mua cùng lúc? **Ngay khi giá vượt một đỉnh rõ ràng**, nơi buy stop (cắt lỗ của short + breakout) bị kích hoạt và biến thành lệnh market mua (mục 8.3).

```text
Liquidity (nhiều lệnh đối ứng xuất hiện dồn dập)
     ↓
Cơ hội thực thi lệnh lớn với ít trượt giá
     ↓
Giao dịch lớn ngược chiều có ĐỘNG CƠ được thực hiện ở đó
     ↓
Sau khi stop chạy hết + người bán lớn đã bán xong → giá có thể đảo
```

Đây là **phiên bản hợp lý nhất** của câu "price seeks liquidity": không phải giá có ý chí, mà là **người cần đối ứng có động cơ giao dịch ở nơi đối ứng xuất hiện**. Nó cũng giải thích vì sao ICT coi "sweep rồi đảo chiều" là mẫu hình quan trọng.

> [!warning] Ranh giới của lập luận
> - Lập luận trên cho thấy hành vi đó **có động cơ** — không chứng minh nó **xảy ra thường xuyên**, cũng không chứng minh **mọi** sweep là do người bán lớn.
> - Ý định của một người tham gia cụ thể là **[UNKNOWN]** từ chart.
> - Nếu stop đã bị kích hoạt và có người lớn bán vào đó, *dữ liệu* sẽ cho thấy gì? → tốc độ tăng khi vượt đỉnh (cascade), rồi đảo chiều với xác suất cao hơn baseline. Điều này **test được** (HYP-IPDA-005, -006).
>
> **Kết luận:** "Price seeks liquidity" phải được coi là **framework/hypothesis**, không phải định luật vật lý.

---

## 21. DOL là gì?

### 21.1 TẦNG 1

Giá đang ở **A**. Phía trên có một vùng **B** mà nhiều người đã đặt lệnh chờ ở đó. Ta có thể nói: *B là một nơi giá có thể bị "hút" tới.*

```text
B   ← một vùng có nhiều lệnh chờ (potential draw)
│
A   ← giá hiện tại
```

### 21.2 TẦNG 2–3

**[ICT FRAMEWORK]** ICT gọi ý tưởng này là **Draw on Liquidity (DOL)**: vùng liquidity mà giá được cho là đang được "kéo" về phía nó. Note chuyên sâu: [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]], [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]], [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]], [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]].

```text
DOL  ≠  Guaranteed destination
DOL  =  một HYPOTHESIS về nơi giá có thể được kéo tới
        + điều kiện vô hiệu hóa
        + thời hạn
```

**Quan hệ với IPDA:** DOL là **câu trả lời tạm thời** cho câu hỏi mà IPDA đặt ra — "giá đang được delivery *tới đâu*?". IPDA là lớp câu hỏi; DOL là một câu trả lời cụ thể, có thể sai, tại một thời điểm.

### 21.3 Thẻ 10 câu — DOL

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | Vùng liquidity được giả thuyết là mục tiêu tiếp theo của giá |
| 2 | Tưởng tượng? | Thị trấn gần nhất trên bản đồ — có thể tới, chưa chắc tới |
| 3 | Thực sự xảy ra? | Nếu giá tới đó: lệnh chờ ở đó được khớp |
| 4 | Tại sao giá có thể tới đó? | Hình học (gần), stop cascade (tăng tốc khi tới gần), người cần đối ứng |
| 5 | Trên chart? | Một đỉnh/đáy/vùng chưa bị chạm |
| 6 | ICT gọi? | Draw on Liquidity |
| 7 | Không biết gì? | Giá có tới không, tới khi nào, tới trước hay sau khi lấy phía đối diện |
| 8 | Fact | Mức đó tồn tại và chưa bị vượt |
| 9 | Interpretation | "Giá đang được kéo về đó" |
| 10 | Hypothesis | "Phương pháp chọn DOL của tôi chạm trước mức đối diện nhiều hơn tỉ lệ khoảng cách" (HYP-IPDA-002) |

---

## 22. Tại sao price không phải lúc nào cũng đi tới DOL?

Đây là phần quan trọng nhất để tránh hiểu IPDA như một cỗ máy tất định.

![[IPDA-Deep-15-Nhieu-DOL-Nhieu-Duong.svg|760]]

```text
Current Price
      ├──── DOL A (gần)
      ├──── DOL B (xa hơn)
      └──── DOL C (phía đối diện)
```

Giá có thể đi: `A → B`, hoặc `A → C`, hoặc `A → B → C`, hoặc `A → thanh khoản đối diện → B`. **Tất cả đều "hợp lý" khi nhìn từ A**, và sau khi giá đi, *đường nào xảy ra* cũng sẽ có một câu chuyện ICT phù hợp.

### 22.1 Bảy lý do giá không tới DOL (hoặc tới sau khi đã lấy phía đối diện)

| # | Lý do | Cơ chế |
|---|---|---|
| 1 | **Có nhiều DOL cạnh tranh** | Ở mỗi thời điểm luôn có liquidity cả trên lẫn dưới |
| 2 | **Thông tin mới** | Tin vĩ mô đổi kỳ vọng → toàn bộ báo giá dời đi |
| 3 | **Hấp thụ** | Một người tham gia lớn đặt limit chặn đường (mục 9) |
| 4 | **Liquidity "thật" ở chỗ khác** | Mức ta chọn không thực sự có nhiều lệnh như ta nghĩ (vì ta không thấy được) |
| 5 | **Khung thời gian** | DOL của D1 có thể cần nhiều tuần; trong ngày giá đi ngược hoàn toàn hợp lý |
| 6 | **Nhiễu** | Một phần lớn chuyển động ngắn hạn không dự báo được |
| 7 | **DOL được chọn sai ngay từ đầu** | Chọn bằng hindsight hoặc theo mức gần nhất mà gọi là "phân tích" |

### 22.2 Baseline hình học — điều mà mọi phương pháp DOL phải vượt

**[MATHEMATICAL]** Với chuyển động Brown không drift, xác suất giá chạm mức trên **H** trước mức dưới **L**, khi đang ở **x**, là:

$$P(\text{chạm } H \text{ trước } L) = \frac{x - L}{H - L}$$

tức là **bằng đúng vị trí tương đối của giá trong range**. Giá ở 70% của range → 70% chạm đỉnh trước — **không cần thông tin gì**.

**[SIMULATION]** IPDA-Sim-02 panel C (20.000 đường random walk, range 20 ngày): giá ở vị trí 0.05 → 6% chạm H20 trước; 0.25 → 28.5%; 0.55 → 55.4%; 0.95 → 94%. Gần như trùng đường chéo.

> [!important] Hệ quả cho việc đánh giá DOL
> Nếu phương pháp chọn DOL của bạn hay chọn mức **gần hơn**, nó sẽ "đúng" thường xuyên chỉ vì hình học. "DOL được chạm 70% số ngày" vô nghĩa cho tới khi so với *xác suất chạm theo khoảng cách*. Đây chính là ý của project về `p_null` trong [[59-Daily-Bias]] và [[20-Liquidity-Sweep]].
>
> **Framework IPDA nên được hiểu như BẢN ĐỒ (các điểm đến có thể), không như GPS (một con đường biết trước).**

---

# PHẦN C — THỜI GIAN, RANGE VÀ CẤU TRÚC

## 23. IPDA và thời gian

### 23.1 Vì sao ICT nói về thời gian?

Thị trường không chỉ có **GIÁ**, mà còn có **THỜI GIAN**. Hai chuyển động cùng là `100 → 110`:

| | Trong 1 phút | Trong 3 ngày |
|---|---|---|
| Cơ chế khả dĩ | Tin tức, stop cascade, sổ mỏng, dòng lệnh dồn dập | Tái định giá dần, dòng tiền đều, thuật toán thực thi chia nhỏ |
| Trên chart | Một nến dài, có thể có FVG | Nhiều nến, pullback, cấu trúc HH–HL |
| Rủi ro cho trader | Trượt giá, stop bị nhảy qua | Đảo chiều giữa chừng, tốn thời gian |
| ICT đọc | Displacement, "delivery mạnh" | Trend có trật tự, "delivery có cấu trúc" |

→ Cùng biên độ, **hành vi hoàn toàn khác**. Nên một mô hình về price delivery buộc phải có trục thời gian.

### 23.2 Phần nào có cơ sở?

**[MARKET MECHANICS]** Biến động theo giờ trong ngày (intraday seasonality) là hiện tượng được ghi nhận rất rộng rãi: biến động FX tăng khi các trung tâm tài chính mở cửa, đặc biệt giai đoạn London–New York chồng nhau, và nhảy vọt quanh tin vĩ mô định kỳ (Andersen & Bollerslev 1997, 1998). Lý do cơ chế: nhiều người tham gia hoạt động cùng lúc, lệnh tồn đọng qua đêm được xử lý, tin tức được công bố vào giờ cố định, fix 16:00 London tập trung dòng lệnh.

**[ICT FRAMEWORK]** ICT xây trên hiện tượng này các công cụ thời gian: killzones ([[18-Kill-Zones]]), macro times ([[40-Macro-Times]]), midnight open / daily open, weekly profile, quarterly shifts.

**[INTERPRETATION / HYPOTHESIS]** Phần ICT thêm vào là: những khung giờ đó là lúc "thuật toán" *chủ động* thực hiện các bước delivery (sweep, displacement). Hiệu ứng theo giờ *tồn tại* không chứng minh *diễn giải* đó — nó được giải thích đủ bằng việc có nhiều người tham gia và nhiều tin tức ở những giờ đó.

### 23.3 Các thang thời gian

| Thang | Ví dụ công cụ ICT | Cơ sở |
|---|---|---|
| Phút | Macro times, M5 MSS | Tin tức, mở phiên — **[MARKET MECHANICS]** cho biến động; phần "macro" **[ICT FRAMEWORK]** |
| Phiên | Killzones, Asia range | Biến động theo phiên — **[MARKET MECHANICS]** |
| Ngày | Daily bias, PDH/PDL, midnight open | Cách định nghĩa "ngày" thay đổi kết quả (xem [[59-Daily-Bias]] §3.8.5) |
| Tuần | Weekly profile, NWOG | Lịch tin trong tuần |
| 20/40/60 ngày | IPDA Data Ranges | ≈ 1/2/3 tháng giao dịch — mục 24 |
| Quý | Quarterly shift | Kỳ báo cáo, chính sách tiền tệ, tái cân bằng quý — **[HYPOTHESIS]** về tính chu kỳ |

---

## 24. IPDA Data Ranges 20 / 40 / 60 ngày

### 24.1 TẦNG 1

Hãy tưởng tượng bạn nhìn lại những gì đã xảy ra trong **20 ngày**, **40 ngày**, **60 ngày** qua, và đánh dấu **chỗ cao nhất** và **chỗ thấp nhất** trong mỗi khoảng. Đó là ba cặp "mốc" để biết hôm nay giá đang ở gần đỉnh hay gần đáy của một tháng, hai tháng, ba tháng vừa qua.

### 24.2 TẦNG 2 — Trên chart

![[IPDA-Deep-16-IPDA-Data-Range-20-40-60.svg|760]]

```text
H20 / L20 = high cao nhất / low thấp nhất của 20 ngày giao dịch gần nhất
H40 / L40 = … 40 ngày
H60 / L60 = … 60 ngày
```

Vì một tháng có khoảng 20–22 ngày giao dịch, **20/40/60 ≈ 1/2/3 tháng ≈ một quý**. Đây có lẽ là logic tự nhiên nhất của các con số: chúng khớp với **lịch** (tháng, quý), vốn là đơn vị mà quỹ báo cáo, tái cân bằng, và ngân hàng trung ương họp.

### 24.3 TẦNG 3 — ICT nói gì, toán nói gì, cần test gì

**[ICT FRAMEWORK]** (theo tóm tắt cộng đồng về Mentorship 2016–17, Month 05 & 07):

- **Look back:** từ ngày hiện tại, nhìn lại 20/40/60 ngày giao dịch; high/low trong các cửa sổ này là **liquidity tham chiếu** mà giá được cho là sẽ tìm tới hoặc dùng làm mốc premium/discount.
- **Look forward:** chiếu các mức đó về phía trước như vùng mục tiêu cho 20/40/60 ngày tới.
- **Quarterly shift:** thị trường thường đổi pha sau khoảng 3–4 tháng; data ranges giúp nhận ra lúc chuyển pha.
- Cộng đồng ghi nhận ICT "linh hoạt" về cách tính (bắt đầu từ ngày đầu tháng, tính lại mỗi ngày, hoặc từ một ngày được chọn) → **cùng một tên, nhiều định nghĩa**.

**[MATHEMATICAL]** Về mặt tính toán, H20/L20 chính là **kênh Donchian 20 ngày** — một công cụ có từ giữa thế kỷ 20 (Richard Donchian), nổi tiếng với hệ thống Turtle (breakout 20/55 ngày). Nó **hoàn toàn khách quan**: với cùng feed dữ liệu và cùng giờ chốt ngày, ai tính cũng ra cùng con số. Đây là điểm mạnh lớn: IPDA data range là **baseline khách quan tốt nhất** trong số các công cụ range của ICT (xem [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]]).

> [!question] 20/40/60 có phải đồng hồ của một thuật toán không?
> Không có bằng chứng công khai rằng 20/40/60 là "đồng hồ" của một thuật toán nào. Cách đọc khiêm tốn hơn và đủ dùng: **20/40/60 là ba thang nhìn lại tiện dụng, khớp với lịch tháng/quý**, cho ra các mốc mà nhiều người cùng nhìn thấy. **[ICT FRAMEWORK / HYPOTHESIS]**

### 24.4 Baseline random walk — con số phải thắng

![[IPDA-Sim-02-Random-Walk-Baseline-20-40-60.png|900]]

**[SIMULATION]** 20.000 đường random walk Gaussian không drift (σ ngày = 1, 24 bước/ngày để có high/low trong ngày):

| Mức | P(chạm trong 20 ngày tới) | P(chạm trong 60 ngày tới) | P(chỉ chạm High trong 20 ngày) |
|---|---|---|---|
| H20 **hoặc** L20 | **≈ 90%** | **≈ 99%** | H20: **≈ 50%** |
| H40 hoặc L40 | ≈ 76% | ≈ 95% | H40: ≈ 40% |
| H60 hoặc L60 | ≈ 66% | ≈ 90% | H60: ≈ 34% |

**[MATHEMATICAL]** Con số **50%** cho "chạm H20 trong 20 ngày tới" không phải trùng hợp: với *mọi* random walk có bước tăng giảm đối xứng và độc lập, đường đi 20 ngày qua (đọc ngược thời gian) có cùng phân phối với đường đi 20 ngày tới. Nên xác suất "đỉnh của 20 ngày tới cao hơn đỉnh của 20 ngày qua" bằng xác suất ngược lại — **đúng 1/2**.

**Panel B:** xác suất chạm H_N trong 20 ngày giảm **trơn** theo N: N = 17 → 52.9%; 20 → 50.4%; 35 → 41.5%; 40 → 39.5%; 60 → 33.5%; 71 → 31.3%. Không có "nút" ở 20/40/60.

> [!important] Đọc kết quả này thế nào
> 1. "Giá thường chạm H20 hoặc L20 trong tháng tới" là **hình học**, không phải bằng chứng IPDA. Random walk làm điều đó 90% thời gian.
> 2. "Giá chạm H20 trong 20 ngày" cần được so với **50%**, không phải với 0%.
> 3. Để 20/40/60 được coi là **đặc biệt**, dữ liệu thật phải cho thấy một điều mà null không có — ví dụ phản ứng (đảo chiều/tăng tốc) tại H20 mạnh hơn tại H17 hoặc H25, sau khi đã chuẩn hóa theo khoảng cách và biến động. → HYP-IPDA-003.
> 4. Random walk thiếu những thứ thị trường thật có (đuôi dày, biến động thành cụm, xu hướng nhẹ). Những thứ này **có thể** làm số thật khác null — đó chính là lý do phải test, chứ không phải lý do để tin.

### 24.5 Cách dùng hợp lý trong workflow D1

- Dùng H20/L20 (và H40/L40, H60/L60) như **danh sách ứng viên external liquidity** trên D1 — vì chúng khách quan và ai cũng thấy.
- Dùng vị trí của giá trong range 20/40/60 như **một** thước đo premium/discount (so với dealing range cấu trúc — chúng có thể mâu thuẫn; xem LRI trong [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]]).
- **Không** dùng chúng như "đồng hồ" dự báo ngày đảo chiều.

### 24.6 Thẻ 10 câu — IPDA Data Ranges

| # | Câu hỏi | Trả lời |
|---|---|---|
| 1 | Nó là gì? | High/low của 20/40/60 ngày giao dịch gần nhất trên D1 |
| 2 | Tưởng tượng? | Ba thước đo: tháng qua, hai tháng qua, ba tháng qua — cao nhất/thấp nhất ở đâu |
| 3 | Thực sự xảy ra? | Một phép tính max/min trên cửa sổ trượt |
| 4 | Tại sao hữu ích? | Khách quan; khớp lịch tháng/quý; ai cũng thấy → có thể thu hút lệnh |
| 5 | Trên chart? | Sáu đường ngang (H/L × 3) dịch chuyển mỗi ngày |
| 6 | ICT gọi? | IPDA Data Ranges, look back / look forward, quarterly shift |
| 7 | Không biết gì? | Lượng lệnh thật ở các mức; có "chu kỳ" thật không |
| 8 | Fact | Các mức đó tồn tại và tính được chính xác |
| 9 | Interpretation | "Thuật toán dùng 20/40/60 ngày làm tham chiếu" |
| 10 | Hypothesis | 20/40/60 cho thông tin vượt cửa sổ tùy ý (HYP-IPDA-003) |

---

## 25. IPDA và Dealing Range

Chỉ nêu quan hệ cơ bản; chi tiết ở [[12-Dealing-Range]], [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]], [[27-Premium-Discount]], [[16-Internal-External-Range-Liquidity-IRL-ERL]].

```text
HIGH ─────────────  ← trên đó: buy-side liquidity (external)
│   Premium
├── Equilibrium (50%)
│   Discount
LOW  ─────────────  ← dưới đó: sell-side liquidity (external)
```

![[IPDA-Deep-17-Dealing-Range-va-Delivery.svg|760]]

**Câu hỏi:** *Nếu giá đang di chuyển trong một range, ta dùng range đó để hiểu price delivery như thế nào?*

```text
Price  →  Range  →  Liquidity  →  Potential Delivery
```

1. **Range cho VỊ TRÍ**, không cho hướng: giá ở premium hay discount của range *nào*.
2. **Range cho DANH SÁCH MỤC TIÊU**: external (ngoài biên) và internal (FVG/OB bên trong chưa được giao dịch lại).
3. **[ICT FRAMEWORK]** Nguyên lý luân phiên IRL ↔ ERL: lấy external → quay về internal; lấp internal → hướng ra external phía đối diện. **[HYPOTHESIS]** — HYP-IPDA-007.
4. **[MATHEMATICAL]** Premium/discount là **tương đối**: cùng một giá có thể là premium của range nhỏ và discount của range lớn. Equilibrium không có "lực hút" vật lý.

---

## 26. IPDA và Market Structure

### 26.1 Giá tạo ra cấu trúc

```text
Price Movement → Swing High / Low → Structure → New Liquidity
```

Mỗi lần giá di chuyển và đổi hướng (mục 10), nó để lại một swing high/low. Chuỗi swing tạo thành **cấu trúc** (HH–HL, LH–LL, BOS, MSS). Chính các swing rõ ràng lại là nơi con người đặt lệnh → **liquidity mới**.

### 26.2 Vòng phản hồi

![[IPDA-Deep-18-Vong-Lap-Structure-Liquidity.svg|760]]

```text
PRICE → STRUCTURE → LIQUIDITY → FUTURE PRICE CONTEXT → PRICE → …
```

**[MARKET MECHANICS]** Phần "lệnh gom quanh mốc rõ ràng" có cơ sở (Osler với số tròn). **[INTERPRETATION]** Phần mở rộng sang swing high/low là hợp lý nhưng cần test. Đây là một dạng **reflexivity** — thứ được mô tả kỹ ở [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]].

> [!warning] Structure không phải nguyên nhân duy nhất
> Vòng lặp trên không giải thích được: tin vĩ mô, thay đổi lãi suất, dòng tiền thương mại, phòng hộ của doanh nghiệp, tái cân bằng cuối tháng, can thiệp ngân hàng trung ương. Structure/liquidity là **một** lớp giải thích. Coi nó là lớp **duy nhất** là lỗi nhân quả.

---

## 27. IPDA và FVG / Displacement

```text
Rapid Price Movement  →  Displacement  →  Possible FVG
```

![[IPDA-Deep-19-Displacement-FVG.svg|760]]

**Giải thích theo thứ tự đúng:**

1. **[MARKET MECHANICS]** Giá đi rất nhanh qua một vùng khi dòng lệnh chủ động lớn so với độ sâu (mục 8).
2. **[MATHEMATICAL]** Khi nến 2 đi rất xa, high của nến 1 và low của nến 3 có thể **không chồng lên nhau** → khoảng trống **hình học** trên chart.
3. **[ICT FRAMEWORK]** ICT gọi khoảng trống đó là FVG / imbalance / inefficiency, và coi nó là một đặc điểm của price delivery.
4. **[HYPOTHESIS]** Giá quay lại vùng đó với xác suất cao hơn baseline cùng khoảng cách, và *phản ứng* ở đó.

> [!danger] Câu bị cấm
> ❌ "FVG tồn tại vì IPDA muốn tạo FVG." — ❌ "Thuật toán phải quay lại lấp inefficiency."
> Đây là giải thích bằng **mục đích** (teleology): không chỉ ra ai gửi lệnh gì, và không thể bị chứng minh sai. Random walk cũng tạo ~30 FVG/100 nến và cũng quay lại rất thường (xem FVG-Sim trong [[13-FVG-Fair-Value-Gap]]).

**FVG có thể được xem là một đặc điểm hình học của price delivery** — dấu vết của một đoạn đường mà giá đi qua nhanh, với ít giao dịch hai chiều. Liệu đoạn đường đó có "kéo" giá quay lại hay không là câu hỏi **thực nghiệm**.

---

## 28. IPDA và toàn bộ ICT Framework

### 28.1 IPDA là lớp tư duy bao trùm

```text
IPDA
 ├── Price            — giá ở đâu so với các mốc
 ├── Time             — khi nào, đã bao lâu, thang nào
 ├── Liquidity        — lệnh chờ (nghi là) ở đâu
 ├── DOL              — mục tiêu có thể
 ├── Dealing Range    — vị trí premium/discount
 ├── Market Structure — swing, BOS/MSS
 └── PD Arrays        — FVG, OB, breaker, …
```

![[IPDA-Deep-20-IPDA-Trong-He-Thong-ICT.svg|760]]

### 28.2 Map vào framework D1 → H1 → M5 của mình

| Tầng | Câu hỏi IPDA ở tầng này | Công cụ cụ thể | Output |
|---|---|---|---|
| **D1 = CONTEXT** | "Giá đang được delivery từ vùng nào của 1–3 tháng qua, tới vùng nào?" | IPDA 20/40/60, dealing range D1, PDH/PDL, external liquidity D1, HTF FVG | Danh sách DOL ứng viên + vị trí P/D + invalidation D1 |
| **H1 = SETUP** | "Trong bối cảnh đó, giá đang tiến vào POI nào, lấy liquidity nội bộ nào?" | Internal/external H1, POI H1, structure H1 | POI đang theo dõi + liquidity cần bị lấy trước |
| **M5 = EXECUTION** | "Có bằng chứng giao dịch đã đổi chiều tại POI không? Sai ở đâu?" | Sweep, MSS, displacement, FVG M5 | Entry, stop, target, invalidation |

> [!important] IPDA không phải entry strategy
> Không có tín hiệu "IPDA mua". IPDA cung cấp **câu hỏi** ở D1 và H1; quyết định vào lệnh vẫn đi qua các điều kiện M5 của [[01 - ICT 2022 Model|ICT 2022 Model]] với điều kiện và invalidation viết trước. Nếu bạn thấy mình nói "IPDA cho thấy mua ở đây", hãy dừng lại và viết ra *quan sát cụ thể* nào khiến bạn nói vậy.

---

# PHẦN D — PHẢN BIỆN VÀ KIỂM CHỨNG

## 29. Fact vs ICT Interpretation — phân loại từng claim

| # | Claim | Nhãn | Ghi chú |
|---|---|---|---|
| 1 | Giá thay đổi vì giao dịch xảy ra ở một mức giá khác | **[MARKET MECHANICS]** | Định nghĩa của "giá" |
| 2 | Khối lượng mua luôn bằng khối lượng bán | **[MATHEMATICAL]** | |
| 3 | Lệnh market tiêu thụ thanh khoản; limit cung cấp; stop kích hoạt thành market | **[MARKET MECHANICS]** | |
| 4 | Thay đổi giá ngắn hạn ≈ order flow imbalance / độ sâu | **[MARKET MECHANICS]** | Cont–Kukanov–Stoikov 2014 (cổ phiếu Mỹ) |
| 5 | Order flow giải thích một phần lớn biến động tỷ giá ngày | **[MARKET MECHANICS]** | Evans & Lyons 2002: R² > 50% với DM/$, ≈ 45% với ¥/$ |
| 6 | Stop-loss tập trung ngay sau số tròn và tạo price cascade | **[MARKET MECHANICS]** | Osler 2001, 2002 |
| 7 | Stop tập trung ngay sau **swing high/low rõ ràng** | **[INTERPRETATION]** | Mở rộng hợp lý từ (6), chưa kiểm chứng trực tiếp |
| 8 | Biến động tập trung theo phiên và quanh tin | **[MARKET MECHANICS]** | Andersen & Bollerslev |
| 9 | Price delivery: giá đi giữa các vùng liquidity | **[ICT FRAMEWORK]** | Mô tả; luôn "đúng" như một cách mô tả |
| 10 | Giá có xu hướng đi tới liquidity **nhiều hơn baseline** | **[HYPOTHESIS]** | HYP-IPDA-001 |
| 11 | Giá thường chạm H20 hoặc L20 trong tháng tới | **[SIMULATION]** → không phải bằng chứng | Random walk ≈ 90% |
| 12 | 20/40/60 đặc biệt hơn các cửa sổ khác | **[HYPOTHESIS]** | HYP-IPDA-003 |
| 13 | Quarterly shift 3–4 tháng | **[ICT FRAMEWORK / HYPOTHESIS]** | Cần định nghĩa "shift" khách quan rồi mới test được |
| 14 | Sau khi lấy external, giá quay về internal | **[ICT FRAMEWORK / HYPOTHESIS]** | HYP-IPDA-007 |
| 15 | FVG được tạo khi giá đi nhanh | **[MATHEMATICAL]** | Hình học của OHLC |
| 16 | FVG được lấp vì thuật toán cần rebalance | **[UNSUPPORTED CLAIM]** (dạng mục đích) | Dạng test được: "quay lại nhiều hơn baseline" |
| 17 | Tổ chức đã cố ý tạo liquidity đó | **[HYPOTHESIS / UNKNOWN]** | Không suy ra được ý định từ chart |
| 18 | Smart money kiểm soát thị trường | **[UNSUPPORTED CLAIM]** | Mâu thuẫn với cấu trúc FX phi tập trung |
| 19 | IPDA là một thuật toán máy tính có thật điều khiển giá | **[UNSUPPORTED CLAIM]** | Không có bằng chứng công khai |
| 20 | Thị trường có nhiều thuật toán thật (thực thi, tạo lập, HFT) | **[MARKET MECHANICS]** | |
| 21 | Thao túng cục bộ đã từng xảy ra và bị phạt | **[MARKET MECHANICS — lịch sử]** | Không suy ra được "thao túng hệ thống mỗi ngày" |
| 22 | Macro times là lúc thuật toán "khai hỏa" | **[ICT FRAMEWORK / INTERPRETATION]** | Hiệu ứng giờ có thật; diễn giải thì chưa |
| 23 | Price "biết" đích đến | **[UNSUPPORTED CLAIM]** | Đích đến chỉ biết sau khi tới |
| 24 | DOL là target chắc chắn | **Sai** | DOL là hypothesis |
| 25 | IPDA hữu ích như một cách đặt câu hỏi | **[INTERPRETATION]** | Đánh giá bằng kỷ luật/expectancy |

---

## 30. Những điều chart có thể và không thể cho ta biết

| CHART CÓ THỂ CHO BIẾT | CHART KHÔNG THỂ TRỰC TIẾP CHO BIẾT |
|---|---|
| Giá (của feed bạn dùng) | Ai đặt lệnh |
| Thời gian | Tại sao họ đặt lệnh |
| OHLC | Ý định của tổ chức |
| High, low | Lịch sử sổ lệnh đầy đủ |
| Biến động (range, ATR) | Lượng liquidity chính xác ở mỗi mức giá |
| Cấu trúc swing | Lệnh nào bị hủy trước khi khớp |
| Các mức giá lặp lại | Thuật toán chính xác nào đang chạy |
| Volume (futures) / tick volume (FX) | "Logic IPDA" chính xác |
| Thời điểm mốc bị vượt | Nến dài là do một lệnh lớn, nhiều lệnh nhỏ, stop cascade hay rút báo giá |

> [!warning] Ba cái bẫy riêng của trader FX/CFD
> 1. **Feed khác nhau** → high/low khác nhau → "sweep" có thể chỉ tồn tại trên broker của bạn.
> 2. **Bid chart** → stop của lệnh short (khớp theo Ask) có thể bị chạm dù chart không in ra mức đó.
> 3. **Tick volume** ≠ volume thật; nó đo số lần báo giá thay đổi, tương quan với hoạt động nhưng không đo được "ai mua bao nhiêu".

**Đây là một trong những kết luận quan trọng nhất của note:** mọi phân tích ICT là **suy luận từ phần nổi (giá, thời gian) về phần chìm (lệnh, ý định)**. Suy luận có thể đúng, nhưng phải được *gắn nhãn* là suy luận và phải *kiểm chứng được qua hệ quả*.

---

## 31. IPDA có thể được chứng minh không?

### 31.1 Đổi câu hỏi

Không hỏi: **"IPDA có đúng không?"** — câu này không trả lời được, vì IPDA theo nghĩa A không falsify được, theo nghĩa C không phải là claim.

Hỏi: **"Nếu IPDA (nghĩa B) đúng, chúng ta phải quan sát thấy điều gì *khác với đồng xu*?"**

### 31.2 Logic kiểm chứng

![[IPDA-Deep-22-Kiem-Dinh-Gia-Thuyet.svg|760]]

```text
Expected Liquidity Target (định nghĩa TRƯỚC, chỉ dùng dữ liệu ≤ T0)
        ↓
Matched control levels (cùng khoảng cách theo ATR, cùng phía, cùng thời điểm)
        ↓
Measure: P(chạm trong N ngày), chạm trước mức đối diện?, thời gian tới chạm, phản ứng sau chạm
        ↓
Compare: hiệu số ICT − đối chứng, khoảng tin cậy, nhiều thị trường × nhiều năm
        ↓
Verdict: SUPPORTED / WEAK EVIDENCE / REJECTED / REQUIRES MORE DATA
```

**Nếu không vượt baseline → hypothesis yếu đi.** Không phải "mình đọc IPDA sai" — mà là *mô tả đó không thêm thông tin so với hình học*.

### 31.3 Điều gì sẽ làm IPDA hypothesis sai?

1. Mức ICT (DOL, H20/L20, swing rõ) **không** được chạm nhiều hơn mức đối chứng cùng khoảng cách.
2. "Chạm đúng hướng DOL" **không** vượt xác suất theo khoảng cách (`p_null`).
3. Phản ứng sau khi chạm (đảo chiều hoặc tăng tốc) **không** khác mức đối chứng.
4. Kết quả chỉ có ở một thị trường hoặc một giai đoạn (overfit).
5. 20/40/60 **không** khác 17/35/71 hay 25/50/75.
6. Phải dùng thông tin tương lai (hindsight) mới chọn được mức "đúng".

> [!note] Một kết quả "SUPPORTED" chứng minh gì?
> Nó chứng minh **mẫu hình** có thật trong dữ liệu (nghĩa B). Nó **không** chứng minh có một thuật toán trung tâm (nghĩa A). Stop cascade, tồn kho dealer, dòng tiền theo lịch đều có thể tạo ra mẫu hình mà không cần ai điều phối.

---

## 32. Backtest chỉ ở mức hypothesis — Hypothesis Register

> [!caution] Không biến nghiên cứu này thành trading strategy
> Các mục dưới là **câu hỏi có thể test**, không phải quy tắc vào lệnh. Hypothesis ≠ fact. Trạng thái mặc định: **UNTESTED**.

| ID | Hypothesis | Biến đo | Baseline / đối chứng | Falsification | Status |
|---|---|---|---|---|---|
| **HYP-IPDA-001** | Giá chạm các mức liquidity theo định nghĩa ICT (swing high/low rõ, equal highs/lows) nhiều hơn các mức ngẫu nhiên cùng khoảng cách | P(chạm ≤ N bar), thời gian tới chạm | Mức ngẫu nhiên cùng khoảng cách ATR, cùng phía, cùng thời điểm | Hiệu số ≈ 0 với CI chứa 0 trên ≥ 3 thị trường | UNTESTED |
| **HYP-IPDA-002** | Phương pháp chọn DOL (của mình) cho biết phía nào bị chạm trước tốt hơn vị trí tương đối trong range | P(DOL trước mức đối diện) − (x−L)/(H−L) | Gambler's ruin (mục 22.2) | Excess ≤ 0 | UNTESTED |
| **HYP-IPDA-003** | Cửa sổ 20/40/60 ngày cho thông tin vượt các cửa sổ tùy ý | Phản ứng tại H_N/L_N (MFE ngược chiều sau chạm, tỉ lệ đảo) theo N = 10…80 | Đường cong trơn theo N (Sim-02B) | Không có "nút" ở 20/40/60 | UNTESTED |
| **HYP-IPDA-004** | Target dựa trên liquidity có hiệu quả khác nhau theo regime (trend vs range, vol cao vs thấp) | Tỉ lệ chạm target trước stop, expectancy | Cùng target, cùng regime, mức ngẫu nhiên | Không khác giữa regime | UNTESTED |
| **HYP-IPDA-005** | Khi giá vượt swing high/low rõ ràng, tốc độ di chuyển ngay sau đó cao hơn baseline (dấu vết stop cascade) | Range/ATR của k bar sau khi vượt | Vượt mức ngẫu nhiên cùng khoảng cách | Không cao hơn | UNTESTED |
| **HYP-IPDA-006** | Sau khi vượt swing rõ ràng và đóng nến quay lại, xác suất đảo chiều cao hơn baseline | P(đi ngược ≥ 1 ATR trước khi đi tiếp 1 ATR) | Cùng hình dạng tại mức ngẫu nhiên | ≈ 50% hoặc ≈ baseline | UNTESTED |
| **HYP-IPDA-007** | Sau khi lấy external liquidity, giá quay về internal (FVG gần nhất) với xác suất cao hơn baseline cùng khoảng cách | P(chạm FVG ≤ N bar) | `p_null` theo khoảng cách | Excess ≤ 0 | UNTESTED |
| **HYP-IPDA-008** | Một số mẫu price delivery (ví dụ: sweep → displacement → retrace FVG → tiếp diễn) lặp lại với tần suất cao hơn random walk cùng biến động | Tần suất mẫu / 1.000 bar | Random walk / GARCH cùng vol (Sim-03) | Tần suất ≈ null | UNTESTED |

**Thiết kế chung (áp dụng cho mọi HYP):**

- **Dữ liệu:** ≥ 3 thị trường (EURUSD, GBPUSD, XAUUSD, NQ), ≥ 5 năm, một feed cố định, ghi rõ giờ chốt ngày.
- **Không nhìn tương lai:** mọi mức chỉ dùng dữ liệu ≤ T0; swing chỉ được xác nhận sau độ trễ (known_at).
- **Đối chứng ghép cặp:** cùng khoảng cách theo ATR, cùng phía, cùng thời điểm.
- **Đa kiểm định:** nếu test nhiều biến thể (N, ngưỡng), điều chỉnh cho data snooping (White 2000; Hansen 2005) — đã có trong reference của DR-v0.1.
- **Out-of-sample:** chia theo thời gian; thông số khóa trước khi chạy giai đoạn test.
- **Báo cáo hiệu số + CI**, không chỉ "tỉ lệ thắng".

---

## 33. IPDA và randomness

### 33.1 TẦNG 1 — Đồng xu

Một đồng xu tung liên tục có thể ra: `N S N N S S S N …`. Nếu cộng +1 cho Ngửa, −1 cho Sấp, bạn được một đường đi lên xuống — trông rất giống một chart.

![[IPDA-Deep-23-Dong-Xu-va-Chart.svg|760]]

Chart thật cũng có những chuyển động không thể dự đoán hoàn hảo. Do đó:

- ✅ **Một framework không cần dự đoán mọi chuyển động để hữu ích.** Trading là xác suất.
- ⚠️ **Nhưng**: nếu IPDA claim một mẫu hình là có *hệ thống*, mẫu hình đó phải tạo ra **bằng chứng thống kê vượt baseline**.

### 33.2 TẦNG 3 — "Hãy tìm IPDA trong chart này"

![[IPDA-Sim-03-Tim-IPDA-Trong-Nhieu.png|900]]

**[SIMULATION]** 110 nến random walk Gaussian, mọi nhãn do thuật toán gán (không chọn lọc): **15 swing high, 16 swing low, 20 FVG ≥ 0.25 ATR, 12 "sweep", 8 "MSS" trong vòng 8 nến sau sweep, 2 cặp "equal highs"**. Không có tổ chức, thuật toán, hay liquidity nào trong dữ liệu này.

> [!important] Bài học
> Sự **xuất hiện** của sweep, MSS, FVG, "delivery tới DOL" trên chart thật **không phải bằng chứng** của IPDA. Chúng xuất hiện trong nhiễu thuần. Bằng chứng chỉ có thể là **tần suất hoặc hệ quả khác với nhiễu** — và điều đó chỉ thấy được qua đếm có hệ thống, không qua nhìn từng chart.

---

## 34. Mười hiểu lầm phải sửa

| # | ❌ Hiểu lầm | Vì sao sai hoặc quá đơn giản | ✅ Cách nói đúng hơn |
|---|---|---|---|
| 1 | "IPDA là robot điều khiển thị trường." | Không có bằng chứng; mâu thuẫn với cấu trúc FX phi tập trung; không falsify được | "IPDA là mô hình khái niệm để mô tả đường đi của giá" |
| 2 | "IPDA luôn biết price sẽ đi đâu." | Đích đến chỉ biết sau khi tới; nhiều DOL cạnh tranh | "Ở mỗi thời điểm có một danh sách đích đến có thể, kèm xác suất có điều kiện" |
| 3 | "Price luôn phải tìm liquidity." | Giá không có ý chí; có lúc giá đi xa khỏi mọi mốc rõ ràng (tin tức, tái định giá) | "Người cần đối ứng có động cơ giao dịch nơi đối ứng xuất hiện; khi giá chạm mốc có stop, tốc độ có thể tăng" |
| 4 | "Mọi liquidity đều sẽ bị lấy." | Đúng một cách tầm thường theo thời gian vô hạn (random walk cuối cùng chạm mọi mức); vô dụng cho trading có thời hạn | "Mức X có P(chạm trong N ngày) = p; so với baseline p₀" |
| 5 | "DOL là target chắc chắn." | Giá thường lấy phía đối diện trước hoặc không tới | "DOL là hypothesis có invalidation và thời hạn" |
| 6 | "Smart Money kiểm soát market." | Nhiều tổ chức mục tiêu mâu thuẫn; thao túng cục bộ thì bị phạt | "Có những người tham gia lớn; dấu vết của họ không phân biệt được chắc chắn trên chart" |
| 7 | "20/40/60 là luật vật lý." | Dưới random walk xác suất chạm thay đổi trơn theo N | "20/40/60 là ba thang nhìn lại khách quan khớp lịch tháng/quý" |
| 8 | "Nếu chart match ICT thì IPDA đã được chứng minh." | Nhiễu thuần cũng "match" (Sim-03); chọn lọc chart xác nhận | "Bằng chứng = tần suất/hệ quả khác baseline trên mẫu lớn" |
| 9 | "Price đi tới liquidity nên liquidity chắc chắn là nguyên nhân." | Tương quan ≠ nhân quả; hình học giải thích phần lớn (gambler's ruin) | "Cần tách: hình học, stop cascade, và phần còn lại (nếu có)" |
| 10 | "IPDA giải thích được mọi price movement." | Một lý thuyết giải thích *mọi thứ* sau khi xảy ra thì không dự báo được gì | "IPDA mô tả được nhiều đường đi; giá trị dự báo của nó phải được đo" |

---

# PHẦN E — TỔNG HỢP VÀ ÁP DỤNG

## 35. Giải thích IPDA bằng một câu chuyện

> [!example] Câu chuyện khu chợ lớn
> Hãy tưởng tượng một khu chợ rất lớn, mở cửa gần như cả ngày lẫn đêm.
>
> Trong chợ có người muốn mua và người muốn bán. Có những quầy đông khách và những góc vắng tanh. Có món đồ đang được rao ở nhiều mức giá khác nhau.
>
> **Giá của món đồ thay đổi mỗi khi người mua và người bán đồng ý giao dịch ở một mức mới.** Khi một nhóm người sốt ruột ùa vào mua và các quầy rẻ hết hàng, giao dịch tiếp theo phải xảy ra ở quầy đắt hơn — giá tăng. Khi người bán sốt ruột muốn về sớm và hạ giá, giao dịch tiếp theo xảy ra thấp hơn — giá giảm.
>
> Ở một số góc chợ, có rất nhiều người đứng chờ với những lời dặn kiểu "nếu giá lên tới mức này thì mua giúp tôi ngay". Khi giá chạm tới góc đó, tất cả lời dặn cùng lúc biến thành người mua thật — và giá chạy rất nhanh qua góc đó. Một người buôn lớn muốn bán thật nhiều hàng sẽ thích bán đúng lúc ấy, vì đó là lúc có nhiều người mua nhất.
>
> Có những giờ chợ đông (sáng sớm, giờ tan tầm) và những giờ chợ vắng. Giờ đông, giá thay đổi nhanh hơn.
>
> Nếu nhìn từ trên cao, đường đi của giá trông như đi từ góc này sang góc khác, ghé qua những chỗ trước đó nó đi quá vội, rồi chạy tới những góc có nhiều người chờ. **Theo cách nhìn của ICT, ta gọi đường đi đó là "price delivery", và IPDA là một tấm bản đồ khái niệm giúp ta suy nghĩ về việc giá được đưa giữa các vùng giá và các vùng liquidity theo thời gian.**
>
> **Nhưng điều này không có nghĩa là có một robot bí mật đang điều khiển toàn bộ khu chợ.** Tấm bản đồ chỉ tốt khi nó giúp ta đoán đúng *thường xuyên hơn đoán mò* — và điều đó phải được đếm, không phải cảm nhận.

---

## 36. Mô hình tư duy cuối cùng

```text
             MARKET
                │
                ↓
       BUYERS + SELLERS
                │
                ↓
             ORDERS
                │
                ↓
        ORDER MATCHING
                │
                ↓
         PRICE DISCOVERY
                │
                ↓
          PRICE MOVEMENT
                │
        ┌───────┴───────┐
        ↓               ↓
    STRUCTURE       LIQUIDITY
        │               │
        └───────┬───────┘
                ↓
          PRICE DELIVERY
                │
                ↓
        ICT INTERPRETATION
                │
                ↓
              IPDA
                │
        ┌───────┼───────┐
        ↓       ↓       ↓
      PRICE    TIME   LIQUIDITY
                │
                ↓
              DOL
```

![[IPDA-Deep-21-Mo-Hinh-Tu-Duy-Cuoi-Cung.svg|760]]

**Giải thích từng mũi tên bằng ngôn ngữ đơn giản:**

| Mũi tên | Nghĩa là | Nhãn |
|---|---|---|
| Market → Buyers + Sellers | Chợ là nơi người muốn mua gặp người muốn bán | **[MARKET MECHANICS]** |
| Buyers + Sellers → Orders | Họ nói ý muốn của mình bằng lệnh: mua ngay, chờ giá tốt, hoặc "nếu giá tới X thì…" | **[MARKET MECHANICS]** |
| Orders → Order matching | Lệnh gặp nhau; ai chấp nhận giá của người kia thì giao dịch xảy ra | **[MARKET MECHANICS]** |
| Order matching → Price discovery | Giao dịch tiếp theo xảy ra ở đâu, đó là "giá mới"; ai cũng thấy và điều chỉnh | **[MARKET MECHANICS]** |
| Price discovery → Price movement | Chuỗi giao dịch ở các mức khác nhau theo thời gian = giá di chuyển | **[MARKET MECHANICS]** |
| Price movement → Structure | Giá đổi hướng để lại đỉnh và đáy | **[OBSERVABLE]** |
| Price movement → Liquidity | Con người đặt lệnh quanh đỉnh/đáy/số tròn → lệnh gom lại ở đó | **[MARKET MECHANICS]** (số tròn) / **[INTERPRETATION]** (swing) |
| Structure ↔ Liquidity | Đỉnh/đáy rõ thu hút lệnh; lệnh ảnh hưởng chuyện xảy ra khi giá quay lại | **[INTERPRETATION]** |
| → Price delivery | ICT đặt tên cho đường đi giữa các vùng đó | **[ICT FRAMEWORK]** |
| → ICT interpretation | Đọc đường đi bằng liquidity, PD array, structure, time | **[ICT FRAMEWORK]** |
| → IPDA | Gom các cách đọc thành một mô hình có ba trục | **[ICT FRAMEWORK]** |
| IPDA → Price / Time / Liquidity | Ba trục để mô tả delivery | **[ICT FRAMEWORK]** |
| → DOL | Câu trả lời tạm thời cho "giá có thể bị kéo về đâu?" — có invalidation, phải vượt baseline | **[HYPOTHESIS]** |

> [!important] Chiều đọc
> **Đọc từ trên xuống = nhân quả** (có cơ sở). **Đọc từ dưới lên = suy luận** (từ chart đoán cơ chế). Khi phân tích chart thật, bạn luôn đi *ngược* chiều: thấy giá di chuyển → đoán liquidity → đoán delivery → đặt giả thuyết DOL. **Mỗi bước ngược đều mất thông tin.** Vì vậy mọi kết luận ở tầng cam/tím phải mang nhãn [INTERPRETATION] hoặc [HYPOTHESIS].

---

## 37. Bài kiểm tra "5 tuổi"

### Test 1 — Không dùng bất kỳ thuật ngữ ICT nào, tôi có giải thích được tại sao giá di chuyển không?

> Giá là con số của lần mua bán gần nhất. Giá lên khi người mua sốt ruột đã mua hết hàng ở giá rẻ, nên lần mua tiếp theo phải trả cao hơn — hoặc khi người bán không chịu bán rẻ nữa. Giá xuống thì ngược lại. Giá chạy nhanh khi có ít hàng đang chờ bán (hoặc chờ mua) ở gần giá hiện tại, hoặc khi nhiều lời dặn "nếu giá tới đây thì mua/bán ngay" cùng bị kích hoạt. Giá đứng yên khi hai bên đều có rất nhiều người chờ sẵn.

✅ Đạt.

### Test 2 — Tôi có giải thích được IPDA mà không dùng câu "IPDA làm cho giá…" không?

> IPDA là cách ICT đặt tên cho một tấm bản đồ: trên bản đồ có các vùng mà nhiều người chờ giao dịch (đỉnh, đáy cũ), các vùng giá đã đi qua quá vội (FVG), các mốc thời gian mà chợ đông (phiên, giờ tin), và các mốc 1–2–3 tháng qua (20/40/60 ngày). ICT dùng bản đồ này để đoán giá có thể đi đâu tiếp theo. Bản đồ này là một giả thuyết: nó hữu ích nếu những đoán đó đúng thường hơn đoán mò.

✅ Đạt — không có chủ thể "IPDA" làm hành động nào.

### Test 3 — Tôi có phân biệt được điều tôi nhìn thấy trên chart với điều tôi suy luận không?

| Tôi nhìn thấy | Tôi suy luận |
|---|---|
| Giá vượt đỉnh hôm qua 8 pip rồi đóng nến quay lại dưới đỉnh | Buy stop trên đỉnh đã bị kích hoạt |
| Nến M5 dài 25 pip, để lại khoảng trống 3 nến | Có dòng lệnh chủ động lớn so với độ sâu (hoặc rút báo giá, hoặc stop cascade) |
| Giá đi ngang 3 ngày ở nửa dưới range rồi tăng | "Có người tích lũy" (nhãn đặt *sau* khi thấy giá tăng) |
| Giá chạm H20 sau 12 ngày | "IPDA đã delivery tới H20" (random walk làm điều này ≈ 50% trong 20 ngày) |

✅ Đạt khi mỗi dòng "suy luận" trong journal của mình đều có nhãn.

---

## 38. Trả lời 27 câu hỏi cuối cùng

| # | Câu hỏi | Trả lời ngắn gọn nhưng chính xác |
|---|---|---|
| 1 | Market là gì? | Nơi/mạng lưới người muốn mua gặp người muốn bán, và giao dịch xảy ra ở mức giá cả hai chấp nhận. |
| 2 | Buyer và seller làm gì? | Gửi lệnh thể hiện họ muốn giao dịch bao nhiêu, ở giá nào, ngay hay chờ. Mỗi giao dịch cần cả hai; lượng mua luôn bằng lượng bán. |
| 3 | Order là gì? | Chỉ thị mua/bán kèm điều kiện: market (ngay, tiêu thụ thanh khoản), limit (chờ giá, cung cấp thanh khoản), stop (chờ chạm mức rồi thành market). |
| 4 | Liquidity là gì? | (1) Khả năng giao dịch lớn, nhanh, rẻ mà giá ít bị đẩy; (2) trong ICT: vùng giá *nghi là* có nhiều lệnh chờ (trên đỉnh, dưới đáy) — tức đối ứng tiềm năng. |
| 5 | Price discovery là gì? | Vòng lặp liên tục: thông tin/nhu cầu → lệnh → khớp ở mức mới → mọi người điều chỉnh → … để tìm mức giá mà giao dịch còn xảy ra. |
| 6 | Tại sao giá tăng? | Vì giao dịch tiếp theo xảy ra cao hơn: lệnh mua chủ động đã khớp hết các mức bán rẻ, và/hoặc người bán rút/nâng giá chào, người mua nâng giá hỏi. |
| 7 | Tại sao giá giảm? | Đối xứng: lệnh bán chủ động khớp hết các mức mua cao, và/hoặc người mua rút lệnh, người bán hạ giá chào. |
| 8 | Tại sao giá đôi khi chạy rất nhanh? | Dòng lệnh chủ động lớn so với độ sâu: sổ mỏng, thanh khoản rút trước tin, stop cascade, dòng lệnh một chiều, cú sốc thông tin. |
| 9 | Price delivery là gì? | Từ vựng ICT mô tả đường đi của giá giữa các vùng (liquidity, FVG) theo thời gian. Mô tả đường đi, không chứng minh có người "giao hàng". |
| 10 | Tại sao ICT dùng khái niệm price delivery? | Để chuyển từ đọc từng nến sang đọc đường đi "từ đâu tới đâu", buộc trader gọi tên mục tiêu và vùng sai trước khi vào lệnh. |
| 11 | IPDA là gì? | Mô hình khái niệm của ICT về đường đi của giá theo ba trục giá–thời gian–liquidity, giả định đường đi có tính hệ thống. |
| 12 | "Institutional" trong IPDA nghĩa là gì? | ICT gốc dùng "Interbank" (thị trường liên ngân hàng FX); "Institutional" chỉ loại người tham gia (ngân hàng, quỹ…). Không phải một tổ chức duy nhất; danh tính không suy ra được từ chart. |
| 13 | "Pricing" nghĩa là gì? | Liên quan tới giá — đối tượng mà mô hình mô tả (tên gốc là "Price"). |
| 14 | "Delivery" nghĩa là gì? | Quá trình giá được đưa từ vùng này sang vùng khác; hàm ý "có chủ đích" là phần diễn giải. |
| 15 | "Algorithm" nghĩa là gì? | Gợi ý quá trình có quy tắc, hệ thống. Thị trường có nhiều thuật toán thật (số nhiều); IPDA thì là mô hình khái niệm, không phải một chương trình cụ thể quan sát được. |
| 16 | IPDA có phải literal computer algorithm không? | Không có bằng chứng công khai. Nên dùng như conceptual model. |
| 17 | IPDA có thực sự điều khiển thị trường không? | Không nên hiểu như vậy. FX phi tập trung, nhiều người tham gia mục tiêu mâu thuẫn; thao túng cục bộ từng xảy ra và bị phạt, không chứng minh một bộ điều khiển trung tâm. |
| 18 | Tại sao ICT liên hệ IPDA với liquidity? | Vì người cần giao dịch lớn cần đối ứng, và đối ứng xuất hiện dồn dập ở nơi lệnh chờ/stop tập trung → đó là nơi giao dịch lớn *có động cơ* xảy ra và giá có thể tăng tốc. |
| 19 | DOL liên hệ với IPDA như thế nào? | IPDA đặt câu hỏi "giá đang được delivery tới đâu?"; DOL là một câu trả lời cụ thể, tạm thời, có invalidation. |
| 20 | 20/40/60-day concept thực sự có ý nghĩa gì? | Ba cửa sổ nhìn lại (≈ 1/2/3 tháng) cho high/low tham chiếu khách quan (kênh Donchian). Việc chúng "đặc biệt" là hypothesis; dưới random walk không có gì đặc biệt ở 20/40/60. |
| 21 | Chart cho chúng ta biết gì? | Giá (của feed bạn dùng), thời gian, OHLC, high/low, biến động, cấu trúc swing, volume (futures). |
| 22 | Chart không cho chúng ta biết gì? | Ai đặt lệnh, vì sao, lệnh chờ ở từng mức, lệnh hủy, ý định tổ chức, thuật toán đang chạy, "logic IPDA". |
| 23 | Điều gì là market mechanics? | Giá = giao dịch; lệnh market/limit/stop; price impact ~ dòng lệnh/độ sâu; order flow giải thích biến động; stop cluster & cascade ở số tròn; biến động theo phiên. |
| 24 | Điều gì là ICT interpretation? | Price delivery, DOL, PD arrays, IRL↔ERL, "smart money", "thuật toán khai hỏa", "rebalance". |
| 25 | Điều gì vẫn chỉ là hypothesis? | Giá đi tới liquidity nhiều hơn baseline; 20/40/60 đặc biệt; quarterly shift; quay về internal sau khi lấy external; sweep → đảo nhiều hơn baseline. |
| 26 | IPDA có thể được kiểm chứng bằng dữ liệu không? | Theo nghĩa B (mẫu hình có hệ thống): có — so mức ICT với mức đối chứng cùng khoảng cách. Theo nghĩa A (robot trung tâm): không falsify được. |
| 27 | Điều gì có thể làm IPDA hypothesis sai? | Mức ICT không được chạm/phản ứng nhiều hơn đối chứng; DOL không vượt xác suất theo khoảng cách; 20/40/60 không khác cửa sổ tùy ý; kết quả không bền qua thị trường/thời gian; cần hindsight mới chọn được mức "đúng". |

---

## 39. Áp dụng vào workflow của mình

### 39.1 "IPDA Card" — 5 phút trước phiên (D1 → H1)

```text
IPDA CARD — [SYMBOL] — [NGÀY]

1. VỊ TRÍ (Price)
   - Giá đang ở đâu trong range 20 / 40 / 60 ngày?   p20 = __  p40 = __  p60 = __
   - Giá ở premium/discount của dealing range D1 nào? (ghi rõ anchor)
   - Các frame có đồng thuận về vị trí không? (LRI cao/thấp)

2. LIQUIDITY
   - External phía trên gần nhất: ____ (loại: PDH / PWH / H20 / swing D1 / EQH)
   - External phía dưới gần nhất: ____
   - Phía nào đã bị lấy gần đây? ____
   - Internal chưa được giao dịch lại (FVG D1/H4): ____

3. THỜI GIAN (Time)
   - Hôm nay có tin lớn không? Giờ nào?
   - Killzone mình trade: ____  — giá đang ở đâu so với midnight/daily open?

4. GIẢ THUYẾT DELIVERY (Hypothesis)
   - DOL ứng viên chính: ____   vì: ____ (quan sát cụ thể, KHÔNG viết "IPDA muốn")
   - Baseline hình học: giá ở ___% khoảng cách giữa hai external → p_null ≈ ___
   - Lý do mình nghĩ có thông tin VƯỢT baseline: ____ (nếu không có → ghi "không có")
   - Invalidation: ____    Thời hạn: ____

5. HÀNH ĐỘNG
   - Được tìm setup hướng: LONG / SHORT / KHÔNG
   - POI H1 cần chờ: ____
```

### 39.2 Quy tắc v0.1 (BACKTEST REQUIRED)

> [!warning] Đây là quy tắc *quy trình* (process), không phải tín hiệu
> Chúng không thay đổi entry model hiện tại; chúng thay đổi cách viết phân tích để có thể kiểm chứng sau này.

| ID | Quy tắc v0.1 | Lý do | Hiệu ứng mong đợi | Backtest? |
|---|---|---|---|---|
| **RULE-IPDA-001** | Mọi DOL ghi trong journal phải kèm **baseline khoảng cách** (p_null ≈ vị trí tương đối giữa hai external) | Tách "đúng vì hình học" khỏi "đúng vì phân tích" | Sau 50+ ngày, đo được phương pháp DOL có excess hay không | Có — HYP-IPDA-002 |
| **RULE-IPDA-002** | Không viết câu có chủ thể "IPDA/thuật toán/smart money" trong phần lý do vào lệnh; viết quan sát cụ thể | Chống narrative, chống giải thích vòng tròn | Review lệnh thua dễ hơn | Không (quy trình) |
| **RULE-IPDA-003** | Ghi H20/L20, H40/L40, H60/L60 (cùng feed, cùng giờ chốt) trên D1 mỗi ngày như **ứng viên** external liquidity | Mốc khách quan, tái lập được; tạo dữ liệu cho HYP-IPDA-003 | Có dữ liệu để test 20/40/60 vs cửa sổ khác | Có |
| **RULE-IPDA-004** | Khi ghi "sweep", ghi thêm: feed nào, wick bao nhiêu pip, spread lúc đó | Sweep trên bid chart có thể là hiệu ứng spread/feed | Giảm sweep "ảo" | Có — kiểm tra chéo 2 feed |
| **RULE-IPDA-005** | Phân biệt trong journal: **[QS]** quan sát / **[DG]** diễn giải / **[GT]** giả thuyết | Theo nhãn của note này | Journal dùng được cho thống kê | Không (quy trình) |

### 39.3 Liên hệ với các rule hiện có

- Không mâu thuẫn với step-down D1 → H1 → M5 trong [[01 - ICT 2022 Model|ICT 2022 Model]] và [[59-Daily-Bias]]; IPDA Card là **đầu vào** cho Bias Card của Daily Bias v2.
- RULE-IPDA-001 là phiên bản áp dụng của khái niệm `p_null` đã có trong [[59-Daily-Bias]] (§8.2) và [[20-Liquidity-Sweep]].

---

## 40. Checklist trước khi dùng "IPDA" trong phân tích

> [!warning] Không trade chỉ vì "IPDA đang delivery"
> IPDA chỉ có giá trị khi nó đi kèm **quan sát cụ thể + baseline + invalidation**.

- [ ] Mình mô tả được đường đi gần nhất của giá bằng *lệnh và giao dịch* (không dùng thuật ngữ ICT)?
- [ ] DOL được chọn **trước** khi nhìn phiên hôm nay (không hindsight)?
- [ ] Đã ghi baseline khoảng cách cho DOL (RULE-IPDA-001)?
- [ ] Có ít nhất một lý do *vượt hình học* để chọn phía này? (nếu không, ghi rõ "không có")
- [ ] Đã ghi external liquidity cả hai phía, không chỉ phía mình muốn?
- [ ] Đã kiểm tra feed/spread khi đánh dấu sweep (RULE-IPDA-004)?
- [ ] Có tin lớn trong phiên? (thanh khoản có thể rút → chuyển động nhanh, không phải "thuật toán")
- [ ] Invalidation và thời hạn của giả thuyết delivery đã viết ra?
- [ ] Setup M5 vẫn đủ điều kiện ICT 2022 (sweep tại POI, MSS có displacement, FVG, stop logic, RR)?
- [ ] Mình *không* vào lệnh chỉ vì "giá sẽ phải tới DOL"?

---

## 41. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Giải thích vòng tròn | "Giá lên vì IPDA muốn lấy BSL" | Viết lại: ai gửi lệnh gì, khớp ở đâu, vì sao mức mới |
| Coi DOL là chắc chắn | Không có invalidation; giữ lệnh vì "giá phải tới" | DOL = hypothesis + invalidation + thời hạn |
| Đánh giá DOL không có baseline | "DOL đúng 70%!" | So với P(chạm theo khoảng cách) |
| Nhầm hai nghĩa của liquidity | "Đỉnh này nhiều liquidity nên giá sẽ chậm lại ở đó" | Phân biệt thanh khoản (độ sâu) với liquidity pool (lệnh chờ/stop) |
| Gán ý định | "Smart money đã tích lũy" | Ghi quan sát + nhãn [DG] |
| Tin 20/40/60 là đồng hồ | Chờ "đúng ngày 20" để đảo chiều | Dùng như mốc giá khách quan, không như lịch |
| Bỏ qua feed/spread | "Sweep" chỉ có trên broker mình | Kiểm chứng chéo; ghi spread |
| Chọn chart xác nhận | Chỉ lưu các ví dụ "IPDA đúng" | Lưu mọi ngày, kể cả ngày không khớp |
| Dùng IPDA làm tín hiệu vào lệnh | "IPDA cho thấy mua" | IPDA = câu hỏi D1/H1; entry vẫn theo M5 model |
| Giải thích mọi thứ sau khi xảy ra | Ngày nào cũng có câu chuyện IPDA khớp | Viết dự đoán trước; chấm điểm sau |

---

## 42. Câu hỏi tự kiểm tra

- Mình có thể giải thích "vì sao giá tăng 3 tick" chỉ bằng sổ lệnh trong 30 giây không?
- Vì sao "nhiều người mua hơn người bán" là cách nói sai?
- Hai cơ chế khiến giá tăng là gì? Cơ chế nào không cần giao dịch lớn?
- Vì sao vùng "nhiều liquidity" theo ICT lại thường là nơi giá chạy **nhanh** qua?
- Osler đã chứng minh điều gì, và điều gì bà **không** chứng minh?
- Ba cách hiểu IPDA là gì? Cách nào falsify được?
- Nếu giá ở 75% khoảng cách giữa L và H, xác suất chạm H trước là bao nhiêu dưới random walk? Vì sao điều này quan trọng cho DOL?
- Vì sao "giá chạm H20 trong 20 ngày" phải so với 50%?
- Một FVG xuất hiện có chứng minh "thuật toán" không? Vì sao?
- Điều gì sẽ làm mình tin IPDA (nghĩa B) *ít hơn*?

---

## 43. Flashcards / Active Recall

### Q1
**Hỏi:** Giá trên chart thực chất là gì?
**Đáp:** Mức của giao dịch (hoặc báo giá bid/ask) gần nhất trên feed mình dùng. Giá "di chuyển" = giao dịch tiếp theo xảy ra ở mức khác.

### Q2
**Hỏi:** Vì sao "nhiều buyer hơn seller" không giải thích được giá tăng?
**Đáp:** Lượng mua luôn bằng lượng bán trong mọi giao dịch. Cái khác là phía nào chủ động (vượt spread) và phía nào rút/đặt lệnh chờ.

### Q3
**Hỏi:** Market / limit / stop làm gì với thanh khoản?
**Đáp:** Market tiêu thụ; limit cung cấp; stop ẩn rồi khi kích hoạt thì tiêu thụ.

### Q4
**Hỏi:** Công thức khái niệm cho tốc độ của giá?
**Đáp:** Δgiá ≈ λ × dòng lệnh ròng, λ ~ 1/độ sâu. Sổ mỏng → cùng lực, giá đi xa hơn.

### Q5
**Hỏi:** Price cascade là gì và ai ghi nhận nó?
**Đáp:** Stop bị kích hoạt → thành lệnh market → đẩy giá chạm thêm stop → tự củng cố. Osler (NY Fed 2002) với dữ liệu lệnh FX thật; stop gom ngay sau số tròn.

### Q6
**Hỏi:** Ba nghĩa của "liquidity"?
**Đáp:** Thanh khoản (kinh tế học); liquidity pool (ICT: vùng nghi có lệnh chờ); "lấy liquidity" (sự kiện giá vượt vùng đó).

### Q7
**Hỏi:** Price delivery là gì — và không phải là gì?
**Đáp:** Từ vựng mô tả đường đi giữa các vùng. Không phải vật thể; không chứng minh có người "giao hàng".

### Q8
**Hỏi:** IPDA viết tắt của gì theo ICT gốc?
**Đáp:** Interbank Price Delivery Algorithm ("Institutional" là cách gọi khác của cộng đồng).

### Q9
**Hỏi:** Ba cách hiểu IPDA và cách nào dùng?
**Đáp:** A robot trung tâm (unsupported) · B quy luật nổi lên (hypothesis, test được) · C ngôn ngữ mô tả (công cụ). Dùng B + C.

### Q10
**Hỏi:** Phiên bản cơ chế của "price seeks liquidity"?
**Đáp:** Người cần giao dịch lớn cần đối ứng; đối ứng xuất hiện dồn dập khi stop tập trung bị kích hoạt → giao dịch lớn có động cơ xảy ra ở đó. Ý định cụ thể: unknown.

### Q11
**Hỏi:** Baseline hình học cho "chạm H trước L"?
**Đáp:** (x − L)/(H − L) — vị trí tương đối của giá. Mọi phương pháp DOL phải vượt con số này.

### Q12
**Hỏi:** Dưới random walk, P(chạm H20 hoặc L20 trong 20 ngày)? P(chạm riêng H20)?
**Đáp:** ≈ 90%; ≈ 50% (chính xác 1/2 do đối xứng thời gian).

### Q13
**Hỏi:** FVG có chứng minh IPDA không?
**Đáp:** Không. FVG là hình học của một lần giá đi nhanh; random walk cũng tạo ~30 FVG/100 nến. Chỉ "quay lại nhiều hơn baseline" mới là bằng chứng.

### Q14
**Hỏi:** IPDA có phải entry model không?
**Đáp:** Không. Nó là lớp câu hỏi ở D1/H1; entry vẫn theo M5 (sweep → MSS → displacement → FVG) với invalidation viết trước.

---

## 44. Lesson Learned

### Bài học chính
- Giá di chuyển vì **giao dịch tiếp theo xảy ra ở mức khác** — mọi lời giải thích khác phải quy về câu này.
- **Tốc độ** của giá là chuyện **dòng lệnh so với độ sâu**; displacement và FVG là *hình dạng* của chuyện đó, không phải *chữ ký* của một thuật toán.
- "Liquidity" của ICT có **một nền cơ chế thật** (stop cluster & cascade — Osler), nhưng phần mở rộng sang mọi swing là **diễn giải**, và phần "ai đó cố ý" là **không biết được**.
- IPDA tốt nhất khi được dùng như **bản đồ câu hỏi**, tệ nhất khi được dùng như **lời giải thích cho mọi thứ**.
- Random walk "đi tới liquidity" rất thường xuyên. **Một framework phải thắng đồng xu, không chỉ khớp với chart.**

### Quy tắc cá nhân rút ra
- [ ] Không viết "IPDA/thuật toán/smart money muốn…" trong lý do vào lệnh (RULE-IPDA-002).
- [ ] Mọi DOL có baseline khoảng cách + invalidation + thời hạn (RULE-IPDA-001).
- [ ] Ghi H/L 20/40/60 mỗi ngày, cùng feed, cùng giờ chốt (RULE-IPDA-003).
- [ ] Mọi sweep ghi feed + spread (RULE-IPDA-004).
- [ ] Journal tách [QS] / [DG] / [GT] (RULE-IPDA-005).

### Câu nhắc nhở khi trade
> *"Ai gửi lệnh gì, khớp ở đâu? — Còn lại chỉ là tên gọi."*

---

## 45. Registers

### 45.1 Definitions (v0.1)

| ID | Thuật ngữ | Định nghĩa làm việc |
|---|---|---|
| DEF-IPDA-01 | Price | Mức của giao dịch/báo giá gần nhất trên một feed xác định |
| DEF-IPDA-02 | Price discovery | Vòng lặp lệnh → khớp → điều chỉnh để tìm mức giá giao dịch được |
| DEF-IPDA-03 | Liquidity (thanh khoản) | Khả năng giao dịch khối lượng lớn, nhanh, chi phí thấp, ít price impact |
| DEF-IPDA-04 | Liquidity pool (ICT) | Vùng giá nghi có tập trung lệnh chờ/stop (trên swing high, dưới swing low, equal H/L, số tròn) |
| DEF-IPDA-05 | Price delivery | Đường đi của giá giữa các vùng theo thời gian (mô tả) |
| DEF-IPDA-06 | IPDA | Mô hình khái niệm của ICT về price delivery theo giá–thời gian–liquidity; giả định tính hệ thống là hypothesis |
| DEF-IPDA-07 | IPDA Data Range N | max(High), min(Low) của N ngày giao dịch gần nhất trên D1, feed và giờ chốt cố định |
| DEF-IPDA-08 | p_null (khoảng cách) | Xác suất chạm mức dưới random walk cùng biến động, trong cùng cửa sổ thời gian |

### 45.2 Hypotheses

HYP-IPDA-001 … 008 — xem mục 32. Tất cả: **UNTESTED**.

### 45.3 Rules

RULE-IPDA-001 … 005 (v0.1) — xem mục 39.2.

### 45.4 Câu hỏi nghiên cứu mở

1. Trên dữ liệu tick có dấu (futures NQ), tốc độ sau khi vượt swing high rõ ràng có lớn hơn sau khi vượt mức ngẫu nhiên cùng khoảng cách không? (HYP-IPDA-005)
2. Sweep trên bid chart MT5 có bao nhiêu phần trăm là "sweep do spread" (ask vượt, bid không)?
3. "Quarterly shift" có thể định nghĩa khách quan thế nào (đổi dấu của độ dốc 60 ngày? phá H60/L60?) để test được?
4. Phản ứng tại H20/L20 có khác giữa tháng có họp ngân hàng trung ương và tháng không có?
5. Trong ICT 2022 Model của mình, các setup có DOL "vượt baseline" (theo RULE-IPDA-001) có expectancy khác các setup DOL "chỉ là mức gần nhất" không?

### 45.5 Liên kết

- Nền tảng: [[36-Forex-CFD-Basics-Pip-Lot-Spread-Swap-Leverage-Margin]] · [[19-Liquidity]] · [[19-Liquidity#7. Buy-Side Liquidity (BSL)|Buy-side Liquidity]] · [[19-Liquidity#8. Sell-Side Liquidity (SSL)|Sell-side Liquidity]]
- Liquidity & DOL: [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[20-Liquidity-Sweep]] · [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]
- Range & vị trí: [[12-Dealing-Range]] · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] · [[27-Premium-Discount]]
- Delivery & displacement: [[13-FVG-Fair-Value-Gap]] · [[50-Displacement-In-Depth]] · [[41-Change-in-State-of-Delivery]] · [[21-Market-Structure-Shift]]
- Thời gian: [[18-Kill-Zones]] · [[40-Macro-Times]] · [[02-AMD]]
- Bias & framework: [[59-Daily-Bias]] · [[32-Top-down-Analysis-Multiple-Timeframes]] · [[01 - ICT 2022 Model|ICT 2022 Model]]
- Định lượng swing: [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]

---

## Tài liệu tham khảo

**Tier 1–2 — nghiên cứu, dữ liệu chính thức**

- Osler, C. L. (2001). *Currency Orders and Exchange-Rate Dynamics: Explaining the Success of Technical Analysis.* Federal Reserve Bank of New York Staff Report 125. (Bản công bố: *Journal of Finance*, 2003.) — https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.html
- Osler, C. L. (2002). *Stop-Loss Orders and Price Cascades in Currency Markets.* Federal Reserve Bank of New York Staff Report 150. (Bản công bố: *Journal of International Money and Finance*, 2005.) — https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.html
- Evans, M. D. D., & Lyons, R. K. (1999/2002). *Order Flow and Exchange Rate Dynamics.* NBER Working Paper 7317; *Journal of Political Economy* 110(1). — https://www.nber.org/papers/w7317
- Cont, R., Kukanov, A., & Stoikov, S. (2014). *The Price Impact of Order Book Events.* *Journal of Financial Econometrics* 12(1), 47–88. — https://arxiv.org/abs/1011.6402
- Tóth, B., Lempérière, Y., Deremble, C., de Lataillade, J., Kockelkoren, J., & Bouchaud, J.-P. (2011). *Anomalous Price Impact and the Critical Nature of Liquidity in Financial Markets.* *Physical Review X* 1, 021006. — https://arxiv.org/abs/1105.1694
- Kyle, A. S. (1985). *Continuous Auctions and Insider Trading.* *Econometrica* 53(6).
- Glosten, L. R., & Milgrom, P. R. (1985). *Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders.* *Journal of Financial Economics* 14(1).
- Andersen, T. G., & Bollerslev, T. (1997). *Intraday Periodicity and Volatility Persistence in Financial Markets.* *Journal of Empirical Finance* 4. · (1998). *Deutsche Mark–Dollar Volatility: Intraday Activity Patterns, Macroeconomic Announcements, and Longer Run Dependencies.* *Journal of Finance* 53(1).
- Bank for International Settlements (2025). *Triennial Central Bank Survey — OTC foreign exchange turnover in April 2025* (thông cáo 30/09/2025: 9.6 nghìn tỷ USD/ngày). — https://www.bis.org/press/p250930.htm
- White, H. (2000). *A Reality Check for Data Snooping.* *Econometrica.* · Hansen, P. R. (2005). *A Test for Superior Predictive Ability.* *JBES.*

**Sách nền tảng (Tier 2)**

- Harris, L. (2003). *Trading and Exchanges: Market Microstructure for Practitioners.* Oxford University Press — các loại lệnh, người tham gia, thanh khoản.
- Hasbrouck, J. (2007). *Empirical Market Microstructure.* Oxford University Press.
- Bouchaud, J.-P., Bonart, J., Donier, J., & Gould, M. (2018). *Trades, Quotes and Prices: Financial Markets Under the Microscope.* Cambridge University Press — price impact, square-root law.

**ICT — nguồn gốc khái niệm (video; nội dung trong note theo tóm tắt cộng đồng)**

- ICT (Michael J. Huddleston). *ICT Mentorship Core Content (2016–17) — Month 05: Quarterly Shifts & IPDA Data Ranges.*
- ICT. *ICT Mentorship Core Content — Month 07: Short Term Trading — Blending IPDA Data Ranges & PD Arrays.* (Ghi chú cộng đồng: https://forum.ictsharks.com/t/ict-mentorship-core-content-month-7-short-term-trading-blending-ipda-data-ranges-pd-arrays/96)

**Cộng đồng (Tier 3–4 — dùng cho định nghĩa, không phải bằng chứng)**

- LuxAlgo Library — *IPDA & Price Delivery Theory* (dùng tên "Interbank Price Delivery Algorithm"; ghi rõ sự tồn tại của IPDA *chưa được chứng minh*): https://www.luxalgo.com/library/concept/ipda-and-price-delivery-theory/
- innercircletrader.net — *ICT IPDA* (hai mục tiêu: rebalance imbalance / hunt liquidity; lookback 20/40/60; quarterly shift 3–4 tháng; không dẫn nguồn sơ cấp): https://innercircletrader.net/tutorials/ict-ipda/
- TradingView — *ICT IPDA Lookback / Cast-forward* (ghi nhận ICT "linh hoạt" về cách tính data range): https://www.tradingview.com/script/wVvKH6cA-ICT-IPDA-Lookback-Cast-forward/

**Tài liệu nội bộ**

- [[59-Daily-Bias]] (v2) — `p_null`, Bias Card, nhãn.
- [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] và Claude Project `ICT/03_Dealing_Range/` — IPDA lookback như baseline khách quan, LRI.
- [[13-FVG-Fair-Value-Gap]] (FVG-Sim) · [[20-Liquidity-Sweep]] (LS-Sim).

---

## Phụ lục A — Ghi chú mô phỏng

| Figure | Mô hình | Kích thước | Kết quả chính |
|---|---|---|---|
| **IPDA-Sim-01** | **TOY MODEL** sổ lệnh: mỗi tầng giá có N lot cố định, sổ được báo giá lại quanh giá mới sau mỗi bước; lệnh market có dấu ngẫu nhiên, kích thước \|t(3)\| × 260 + 40 lot; panel C: độ sâu 400 → 40 trong 12 bước, dòng lệnh trong cửa sổ đó là một chiều | 400 bước, seed 2026 | σ(Δgiá/bước): sổ 1.000 lot/tầng = 0.20 tick; sổ 100 lot/tầng = 3.92 tick; panel D: gộp 6 bước/nến xuất hiện displacement + FVG |
| **IPDA-Sim-02** | Random walk Gaussian, σ ngày = 1, 24 bước/ngày (để có high/low trong ngày), không drift | 20.000 đường × (130 ngày lịch sử + 60 ngày phía trước), seed 42 | P(chạm H_N hoặc L_N trong 20 / 60 ngày): N=20: 89.9% / 99.1%; N=40: 75.7% / 95.0%; N=60: 65.6% / 89.5%. P(chạm H_N trong 20 ngày): 17 → 52.9%; 20 → 50.4%; 35 → 41.5%; 40 → 39.5%; 60 → 33.5%; 71 → 31.3%. P(chạm H20 trước L20) theo vị trí (bin 0.1): 0.05→6.0%, 0.15→16.3%, 0.25→28.5%, 0.35→36.8%, 0.45→44.6%, 0.55→55.4%, 0.65→64.7%, 0.75→75.4%, 0.85→85.3%, 0.95→94.0% (cùng ngày chạm cả hai: chia 50/50) |
| **IPDA-Sim-03** | Random walk Gaussian bước nhỏ, 30 bước/nến; swing = fractal 2; FVG ≥ 0.25 ATR(14); sweep = wick qua swing đã xác nhận + đóng quay lại; MSS = đóng qua swing đối diện trong 8 nến sau sweep; EQH = hai swing high cách nhau 3–25 nến, chênh ≤ 0.1 ATR | 110 nến, seed 314 | 15 swing high, 16 swing low, 20 FVG, 12 sweep, 8 MSS, 2 EQH |

**Giới hạn:** Gaussian không có đuôi dày và biến động theo cụm; toy order book bỏ qua lệnh hủy, hàng đợi, tái bổ sung thanh khoản dần dần; bước rời rạc làm high/low trong ngày nhỏ hơn mô hình liên tục. Các kết quả mô tả **mô hình null / toy model**, không mô tả thị trường thật. Mục đích là xác định **baseline** mà các claim về IPDA phải vượt, không phải chứng minh ICT sai.

**Kết quả toán học dùng trong note:**
- Gambler's ruin (Brown không drift): P(chạm H trước L | x) = (x − L)/(H − L).
- Đối xứng thời gian: với bước độc lập, phân phối đối xứng, P(max 20 ngày tới > max 20 ngày qua, tính từ giá hiện tại) = 1/2.

---

## Phụ lục B — Danh sách hình

| File | Nội dung | Mục |
|---|---|---|
| `IPDA-Deep-00-Chuoi-Nhan-Qua.svg` | Chuỗi nhân quả của note; giải thích vòng tròn vs cơ chế | Cách đọc |
| `IPDA-Deep-01-Cho-Tao-Gia-La-Giao-Dich.svg` | Chợ táo: giá là giao dịch gần nhất | 1 |
| `IPDA-Deep-02-Moi-Giao-Dich-Hai-Phia.svg` | Mua = bán; ai chủ động | 2 |
| `IPDA-Deep-03-Ba-Loai-Lenh.svg` | Market / limit / stop và vị trí điển hình | 3 |
| `IPDA-Deep-04-So-Lenh-Bid-Ask-Spread.svg` | Sổ lệnh, spread, ba kịch bản | 4 |
| `IPDA-Deep-05-Gia-Tang-An-Qua-So-Lenh.svg` | Giá tăng: ăn qua ask + cơ chế điều chỉnh báo giá | 6 |
| `IPDA-Deep-06-Gia-Giam-An-Qua-Bid.svg` | Giá giảm: đối xứng | 7 |
| `IPDA-Deep-07-So-Lenh-Day-vs-Mong.svg` | Sổ dày vs mỏng; con đường; Kyle λ | 8 |
| `IPDA-Deep-08-Stop-Cascade.svg` | Dây chuyền stop (Osler) | 8 |
| `IPDA-Deep-09-Ba-Nghia-Cua-Liquidity.svg` | Ba nghĩa của liquidity | 11 |
| `IPDA-Deep-10-Price-Discovery-Vong-Lap.svg` | Vòng lặp price discovery | 5 |
| `IPDA-Deep-11-Price-Delivery-Chiec-Xe.svg` | Price delivery: chiếc xe và giới hạn | 12 |
| `IPDA-Deep-12-Phan-Ra-Ten-IPDA.svg` | Giải phẫu tên I-P-D-A | 14 |
| `IPDA-Deep-13-Tang-Bang-Quan-Sat.svg` | Observable vs unobservable | 15, 30 |
| `IPDA-Deep-14-Ba-Cach-Hieu-IPDA.svg` | Ba cách hiểu IPDA | 15 |
| `IPDA-Deep-15-Nhieu-DOL-Nhieu-Duong.svg` | Nhiều DOL, nhiều đường; bản đồ vs GPS | 22 |
| `IPDA-Deep-16-IPDA-Data-Range-20-40-60.svg` | 20/40/60 trên D1 giả lập | 24 |
| `IPDA-Deep-17-Dealing-Range-va-Delivery.svg` | Range, IRL/ERL | 25 |
| `IPDA-Deep-18-Vong-Lap-Structure-Liquidity.svg` | Vòng phản hồi structure–liquidity | 26 |
| `IPDA-Deep-19-Displacement-FVG.svg` | Displacement → FVG; cách nói đúng/sai | 27 |
| `IPDA-Deep-20-IPDA-Trong-He-Thong-ICT.svg` | IPDA trong D1→H1→M5 | 28 |
| `IPDA-Deep-21-Mo-Hinh-Tu-Duy-Cuoi-Cung.svg` | Mô hình tư duy cuối cùng | 36 |
| `IPDA-Deep-22-Kiem-Dinh-Gia-Thuyet.svg` | Thiết kế kiểm định | 31 |
| `IPDA-Deep-23-Dong-Xu-va-Chart.svg` | Đồng xu vẽ ra chart | 33 |
| `IPDA-Sim-01-Toy-Order-Book-Depth.png` | Toy order book: độ sâu và tốc độ | 8 |
| `IPDA-Sim-02-Random-Walk-Baseline-20-40-60.png` | Baseline 20/40/60, gambler's ruin | 22, 24 |
| `IPDA-Sim-03-Tim-IPDA-Trong-Nhieu.png` | Nhãn ICT trên nhiễu thuần | 33 |

---

## Changelog

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| v0.1 | 2026-10-07 | Tạo note theo *ICT Deep Research Protocol — IPDA: Why does price move?* (43 mục). 24 sơ đồ `IPDA-Deep-*`, 3 hình mô phỏng `IPDA-Sim-*`. Hypothesis HYP-IPDA-001…008 (UNTESTED); RULE-IPDA-001…005 (v0.1, quy trình). Tên gọi: dùng "Interbank" theo ICT gốc và các note cũ; giải thích thêm "Institutional". |
