---
type: ict-concept
concept: Liquidity
aliases:
  - ICT Liquidity
  - Liquidity Pools
  - Buy-side Liquidity
  - Buyside Liquidity
  - BSL
  - Buy Stops
  - Sell-side Liquidity
  - Sellside Liquidity
  - SSL
  - Sell Stops
  - Equal Highs
  - Equal Lows
  - EQH
  - EQL
tags:
  - trading/ict/concept
  - trading/study
  - "#Liquidity"
  - "#BSL"
  - "#SSL"
status: developing
category: Liquidity
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NQ1/NAS100
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-10-15
created: 2026-06-22
updated: 2026-10-15
version: "v2.0 — hợp nhất 19-Liquidity + 07-Buy-side-Liquidity + 30-Sell-side-Liquidity"
prerequisites:
  - "[[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]"
  - "[[12-Dealing-Range]]"
  - "[[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]"
common_mistakes:
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[09-Mistake-Wrong-daily-bias]]"
---
#Liquidity #BuySideLiquidity #SellSideLiquidity
# Liquidity — từ First Principles đến quy tắc kiểm chứng được (BSL · SSL · DOL · D1 → H1 → M5)

> [!summary] Tóm tắt 1 câu
> **Trên chart, "liquidity" là một MỨC GIÁ THAM CHIẾU được xác định trước (đỉnh/đáy cũ, EQH/EQL, PDH/PDL, PWH/PWL, high/low phiên) mà nhiều người cùng nhìn thấy, nên lệnh có điều kiện (stop, breakout) CÓ THỂ dồn ở phía bên kia nó — BSL ở trên, SSL ở dưới; đó là giả thuyết về NƠI cần quan sát, không phải lời tiên tri về NƠI giá sẽ đi.**

> [!important] Nguyên tắc cốt lõi của note này
> **Xác định mức TRƯỚC → giải thích VÌ SAO nó đáng chú ý → đặt nó vào CẤU TRÚC → lập KỊCH BẢN → quan sát giá LÀM GÌ → PHÂN XỬ theo định nghĩa → CẬP NHẬT → KIỂM CHỨNG bằng dữ liệu.**
> Không bao giờ: nhìn giá quét một mức rồi mới quay lại gọi đó là "liquidity cần được lấy".

> [!info] Note này là bản hợp nhất (v2.0, 2026-10-15)
> Gộp và viết lại ba note: `19-Liquidity`, `07-Buy-side-Liquidity`, `30-Sell-side-Liquidity`. Bản gốc được lưu nguyên vẹn trong `02 - Trading Knowledge/_Archive/` (đuôi `.md.bak`, không bị Dataview/graph đọc). Những gì được giữ, sửa và bỏ — cùng lý do — nằm ở [[#Phụ lục C — Nhật ký hợp nhất OLD → NEW]].
> Note này là **note gốc (hub)** cho Liquidity. Chi tiết sâu của từng nhánh vẫn ở note riêng: sweep/run → [[20-Liquidity-Sweep]] · DOL → [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]] · IRL/ERL → [[16-Internal-External-Range-Liquidity-IRL-ERL]] · Dealing Range → [[12-Dealing-Range]] · thuật toán swing → [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]. Các định nghĩa ở đây **dùng lại** định nghĩa của những note đó (DEF-LS-04, DEF-LS-05, DEF-LS-06, bộ quy tắc DOL v0.2) chứ không đặt định nghĩa mới cạnh tranh.

---

## Cách đọc note này

### Hệ thống nhãn bằng chứng (dùng xuyên suốt)

| Nhãn | Nghĩa | Ví dụ |
|---|---|---|
| **[OBSERVABLE]** | Đọc trực tiếp từ OHLC + thời gian | "Low nến 08:35 xuyên dưới PDL 3 pip, close nến đó trên PDL" |
| **[MARKET MECHANICS]** | Cơ chế khớp lệnh / thanh khoản có cơ sở lý thuyết hoặc thực nghiệm đã công bố | "Stop-loss khi kích hoạt trở thành lệnh market" |
| **[MATHEMATICAL]** | Đúng theo toán học (với giả định nêu rõ) | "Random walk không drift: P(chạm mức gần trước) = d_xa/(d_gần + d_xa)" |
| **[ICT FRAMEWORK]** | Cách ICT / cộng đồng ICT gọi tên và diễn giải | "Mức trên đỉnh cũ gọi là Buy-Side Liquidity" |
| **[INTERPRETATION]** | Diễn giải hợp lý, không chứng minh được từ chart | "Có stop của người short dồn trên đỉnh này" |
| **[HYPOTHESIS]** | Mệnh đề kiểm chứng được, chưa kiểm chứng | "Rejection tại HTF POI đảo chiều nhiều hơn rejection giữa range" |
| **[BACKTEST REQUIRED]** | Không được dùng như edge cho tới khi test đúng phương pháp | mọi câu có chữ "xác suất cao hơn", "hiệu quả hơn" |
| **[HEURISTIC]** | Ngưỡng số chọn để có quy tắc nhất quán — không phải hằng số của thị trường | "Dung sai EQH = 0.10 × ATR(14)" |
| **[SIMULATION]** | Kết quả mô phỏng (random walk / toy model) với giả định nêu rõ — không phải dữ liệu thị trường | "LS-Sim-07: EQH tự xuất hiện trên random walk" |
| **[CONSISTENCY]** | Quy tắc vận hành để phân tích nhất quán, kiểm chứng được; đúng theo mục đích, không cần backtest | "Nhãn ERL/IRL luôn kèm tên range" |

**Về nguồn ICT.** Giáo trình gốc của ICT (Michael J. Huddleston) chủ yếu ở dạng video, không có văn bản định nghĩa chính thức. "[ICT FRAMEWORK]" trong note = cách hiểu phổ biến trong tài liệu cộng đồng, **không phải trích dẫn nguyên văn**. Note không gán cho ICT những câu chưa kiểm chứng.

**Về "Smart Money".** Trong note, "Smart Money" là **một nhân vật trong câu chuyện của mô hình ICT**, không phải một nhóm người quan sát được trên chart. Khi cần nói về người tham gia thị trường, note dùng từ vựng định nghĩa được: *người cung cấp thanh khoản (maker)*, *người tiêu thụ thanh khoản (taker)*, *lệnh có điều kiện (stop)*, *lệnh lớn chia nhỏ (metaorder)*.

### Năm tầng giải thích cho mỗi khái niệm

| Tầng | Tên | Mục tiêu |
|---|---|---|
| **T1** | Đời thường | Hiểu ý chính không cần thuật ngữ |
| **T2** | Diễn biến giá | Một chuỗi giá đơn giản, biết gì ở từng thời điểm |
| **T3** | ICT | Gọi đúng tên theo ICT, sau khi đã hiểu hiện tượng |
| **T4** | Thực hành | Đánh dấu gì, ghi gì, quyết định gì tiếp theo |
| **T5** | Giới hạn | Khi nào khái niệm vô dụng, dễ nhầm, hoặc chưa đủ cơ sở kết luận |

### Bản đồ note

| Part | Nội dung | Mục |
|---|---|---|
| **I — Foundation** | Liquidity là gì, hai nghĩa, vì sao quan trọng, chart cho biết gì, không phải lời tiên tri | 1–6 |
| **II — Classification** | BSL, SSL, swing, EQH/EQL, internal/external, mức theo thời gian, mức độ quan trọng | 7–14 |
| **III — Structural Context** | Market structure, dealing range, premium/discount, BOS/MSS, displacement, POI | 15–21 |
| **IV — Liquidity Events** | Sweep, run, breakout, phản ứng sau khi vượt, trường hợp chưa phân loại, cập nhật | 22–27 |
| **V — Draw on Liquidity** | DOL là gì, xác định, xếp hạng, kịch bản thay thế, cập nhật, lỗi | 28–33 |
| **VI — Multi-Timeframe** | D1 → H1 → M5, checklist, điều kiện chuyển khung, xung đột, 7 tình huống | 34–43 |
| **VII — Operational** | SOP mở chart, đánh dấu, ghi sự kiện, quan sát vs diễn giải, decision tree, quy tắc nếu–thì, 22 lỗi | 44–50A |
| **VIII — Validation** | Định nghĩa vận hành, ghi real-time, journal, chống hindsight, backtest, đánh giá, giả thuyết | 51–58 |
| **IX — Final Synthesis** | ELI5, ví dụ bullish/bearish, run, DOL bị cập nhật, không đủ bằng chứng, một trang, checklist, registers | 59–68 |
| **Phụ lục** | Checklist trade, flashcards, lesson learned, nhật ký hợp nhất OLD → NEW, nguồn, liên kết | A–E |

![[Liquidity-v2-01-Ban-Do-Tong-Quan.svg|900]]

> [!example]- Hình 01 — đọc thế nào
> - **Đang diễn ra gì:** không có giá — đây là bản đồ tư duy của toàn note, 8 bước theo thứ tự phân tích.
> - **Mức nào được đánh dấu:** không áp dụng; bước 2 là nơi các mức được tạo ra.
> - **Timeframe:** áp dụng cho mọi khung; bước 2–5 làm trên D1/H1, bước 6 trên M5.
> - **Vì sao đáng chú ý:** bước 8 (kiểm chứng) quay về bước 2–3 — định nghĩa được sửa bằng dữ liệu, không bằng cảm giác.
> - **Đã xác nhận:** không có gì về giá; chỉ là thứ tự công việc.
> - **Chưa biết:** mọi thứ về giá.
> - **Trader làm gì tiếp:** không nhảy cóc. Thiếu đầu ra của một bước = chưa được sang bước sau.

---
## PART I — FOUNDATION

### 1. Liquidity là gì?

**T1 — Đời thường.** Hãy tưởng tượng một cái chợ. Ở sạp đông người bán và đông người mua, bạn mua một ký cam rất dễ: hỏi là có, giá gần như không đổi. Ở một sạp vắng, bạn muốn mua mười ký thì người bán phải lục kho, nâng giá, hoặc bạn phải chờ. *Liquidity (thanh khoản) là mức độ "dễ" của việc mua bán: mua bán được nhiều, nhanh, mà giá không bị xô lệch nhiều.*

> [!warning] Giới hạn của ví dụ
> Chợ có người thật đứng đó, nhìn thấy được. Thị trường tài chính thì phần lớn ý định mua bán **không nhìn thấy**: lệnh chờ có thể bị hủy trong một phần nghìn giây, lệnh có điều kiện (stop) nằm ẩn trên máy chủ của broker, và trên FX spot không có một "cái chợ" duy nhất — mỗi nơi khớp lệnh có sổ lệnh riêng.

**T2 — Diễn biến giá.** Giả sử ở giá 1.0850 có 50 lot đang chờ bán, 1.0851 có 3 lot, 1.0852 có 40 lot. Một người cần mua ngay 60 lot sẽ ăn hết 50 lot ở 1.0850, 3 lot ở 1.0851 và 7 lot ở 1.0852 — giá giao dịch cuối cùng nhảy từ 1.0850 lên 1.0852. Nơi "mỏng" (1.0851) bị xuyên qua rất nhanh; nơi "dày" làm giá chậm lại. **[MARKET MECHANICS]** (số lượng là giả định).

**T3 — Theo ICT.** ICT dùng chữ "liquidity" theo một nghĩa hẹp và thực dụng hơn: **những mức giá trên chart mà phía bên kia của chúng được giả định là có nhiều lệnh chờ** — chủ yếu là lệnh có điều kiện (stop-loss, lệnh breakout). Mức phía trên đỉnh cũ gọi là **Buy-Side Liquidity (BSL)**, mức phía dưới đáy cũ gọi là **Sell-Side Liquidity (SSL)**. ICT mô tả giá như "tìm tới", "lấy", "quét" các mức đó. **[ICT FRAMEWORK]**

**T4 — Thực hành.** Bạn sẽ không bao giờ "nhìn thấy liquidity". Bạn nhìn thấy **mức giá** (một đỉnh, một đáy, PDH…) và **thời điểm mức đó trở nên được biết**. Toàn bộ công việc của note này là: chọn mức nào đưa vào danh sách theo dõi, vì sao, và giá làm gì khi tới đó.

**T5 — Giới hạn.** Một đường ngang trên chart **không đo** được có bao nhiêu lệnh ở đó, ai đặt, còn hay đã hủy. Nó là một **giả thuyết về nơi lệnh có thể dồn lại** — được xây trên một lập luận hợp lý (nhiều người nhìn cùng một mức), không phải trên dữ liệu sổ lệnh.

> [!example] DEF-LQ-01 — Market liquidity (nghĩa thị trường)
> Khả năng giao dịch một khối lượng mong muốn **nhanh**, với **chi phí thấp**, mà **ít làm giá dịch chuyển**. Ba chiều kinh điển (Kyle 1985): **tightness** (spread hẹp), **depth** (khối lượng sẵn sàng tại mỗi mức giá), **resiliency** (độ sâu bị ăn mất được bù lại nhanh). Harris (2003) bổ sung **immediacy** (giao dịch được ngay). **[MARKET MECHANICS]**

> [!example] DEF-LQ-02 — Liquidity reference level (nghĩa ICT, định nghĩa làm việc của vault)
> Một mức giá **L** được xác định **trước** sự kiện (có `known_at`), nổi bật với nhiều người tham gia (swing đã xác nhận, EQH/EQL, PDH/PDL, PWH/PWL, high/low phiên, số tròn), sao cho phía bên kia L **có thể** tập trung lệnh có điều kiện. Đồng nghĩa với DEF-LS-01 trong [[20-Liquidity-Sweep]]. **[ICT FRAMEWORK]** cho tên gọi; **[INTERPRETATION]** cho phần "có lệnh".

---

### 2. Liquidity trong market microstructure và trong ICT khác nhau như thế nào?

![[Liquidity-v2-02-Hai-Nghia-Cua-Liquidity.svg|900]]

> [!example]- Hình 02 — đọc thế nào
> - **Đang diễn ra gì:** trái là sổ lệnh tại một thời điểm (ask = lệnh bán chờ, bid = lệnh mua chờ); phải là chart nến với một đỉnh cũ được kẻ ngang.
> - **Mức được đánh dấu:** đỉnh cũ L (bên phải), dán nhãn "BSL?" — có dấu hỏi.
> - **Timeframe:** không quan trọng cho ý tưởng; sổ lệnh là ảnh chụp tức thời.
> - **Vì sao đáng chú ý:** hai thứ cùng tên "liquidity" nhưng một thứ **đo được** (nếu có dữ liệu), thứ kia **suy luận**.
> - **Đã xác nhận:** chart chỉ cho biết mức L và giá đã/chưa đi qua L.
> - **Chưa biết:** khối lượng lệnh sau L, ai đặt, còn hay hủy.
> - **Làm gì tiếp:** mỗi khi viết "BSL ở đây", tự đọc thầm câu đầy đủ ở bảng bên dưới.

| Khía cạnh | Market microstructure | ICT (trên chart OHLC) |
|---|---|---|
| Đối tượng | Sổ lệnh: spread, độ sâu, khả năng hồi phục | Mức giá tham chiếu (đỉnh/đáy cũ, PDH/PDL…) |
| Quan sát được? | Có, nếu có dữ liệu Level 2 / DOM / dữ liệu khớp lệnh | Chỉ thấy **mức** và **giá đi qua mức hay chưa** |
| "Liquidity cao" nghĩa là | Mua bán nhiều mà giá ít xô lệch | Phía sau mức "có thể" có nhiều stop |
| Ai tạo ra | Maker đặt limit (cung cấp), taker đặt market (tiêu thụ) | Được giải thích qua hành vi đặt stop/breakout của đám đông |
| Hệ quả khi giá chạm | Độ sâu bị ăn; giá dịch chuyển nếu dòng lệnh vượt độ sâu | "Liquidity bị lấy", "sweep", "run" |
| Nguy cơ nhầm | Coi volume là liquidity | Coi đường kẻ là phép đo |

**Câu nói đầy đủ và trung thực** khi bạn viết "có BSL trên đỉnh X" (theo [[20-Liquidity-Sweep]] §1.8):

> *"Mức X nổi bật với nhiều người (đỉnh cũ, số tròn, PDH, EQH…). Do đó **có thể** có mật độ cao hơn bình thường của (a) lệnh MUA có điều kiện ngay sau X — stop-loss của người đang short, buy-stop vào breakout — và (b) lệnh BÁN chờ ngay tại/trước X — chốt lời, người bán ở đỉnh. Nếu giá giao dịch qua X, (a) biến thành lệnh market; điều này có thể khuếch đại chuyển động hoặc cung cấp đối ứng cho người cần bán khối lượng lớn. Ta không quan sát được khối lượng, vị trí chính xác, hay ai sẽ dùng chúng."*

**Tách ẩn dụ khỏi sự thật:**

| Cách nói (ẩn dụ ICT) | Nghĩa đen có thể bảo vệ | Không được ngầm định |
|---|---|---|
| "Liquidity nằm trên đỉnh" | Có thể có mật độ lệnh có điều kiện cao quanh mức nổi bật | Lệnh *chắc chắn* ở đó; số lượng; ai đặt |
| "Giá đi lấy liquidity" | Giá đã giao dịch qua mức | Giá "muốn", "cần", "được điều khiển" để làm vậy |
| "Pool đã bị lấy" | Giá đã đi qua mức; lệnh gần mức (nếu có) đã bị kích hoạt | Toàn bộ lệnh đã khớp; không còn lệnh sâu hơn |
| "Smart money hunted stops" | Có một đợt giao dịch làm giá vượt mức rồi giá quay lại | Ý định, danh tính, sự phối hợp |

**Bốn từ, bốn đối tượng** (định nghĩa làm việc v0.1 — kế thừa [[20-Liquidity-Sweep]] §3.1):

| Thuật ngữ | Định nghĩa | Quan sát được? |
|---|---|---|
| **Level** (mức) | Một giá cụ thể L, xác định ex-ante | Có |
| **Zone** (vùng) | Dải [L, L + w] phía bên kia mức, w tính theo ATR | Biên do mình chọn |
| **Pool** (bể lệnh) | Tập hợp lệnh *được giả định* nằm trong zone | **Không** |
| **Cluster** (cụm) | Nhiều level sát nhau (≤ 0.10·ATR — `cluster_merge_atr`), ví dụ PDH + Asia high + số tròn | Có (các mức) |

> [!tip] Hệ quả quan trọng nhất của mục này
> Khi bạn viết "giá lấy pool", thứ bạn **thực sự quan sát** là "giá giao dịch qua level/zone". Pool là phần **suy luận**. Viết journal bằng ngôn ngữ quan sát trước, diễn giải sau.

---

### 3. Tại sao Liquidity quan trọng?

#### 3.1 Ba loại lệnh — từ số 0

| Loại lệnh | Làm gì | Vai trò với liquidity | Hiển thị? |
|---|---|---|---|
| **Market order** | Mua/bán ngay ở giá tốt nhất đang có | **Tiêu thụ** liquidity (ăn vào sổ lệnh) | Không chờ — khớp ngay |
| **Limit order** | Chờ mua ở giá ≤ X / bán ở giá ≥ X | **Cung cấp** liquidity (nằm trên sổ, chờ người khác ăn) | Có (trên sổ lệnh), nhưng có thể bị hủy bất cứ lúc nào |
| **Stop order** | Khi giá chạm X → gửi lệnh market | Lệnh **tiêu thụ có điều kiện**: ngủ yên rồi thành market | Thường **không** hiển thị trên sổ lệnh công khai |

**[MARKET MECHANICS]** Bốn hệ quả trực tiếp:

1. **Market order cần đối tác.** Một lệnh mua market chỉ khớp được nếu có người bán (thường là limit sell đang chờ). Nếu phía bán mỏng, lệnh mua phải đi lên nhiều mức giá mới khớp đủ → giá dịch chuyển.
2. **Limit order cung cấp thanh khoản nhưng có thể biến mất.** Độ sâu bạn thấy trên DOM không cam kết gì; nó có thể rút khi giá tới gần.
3. **Stop order khuếch đại.** Khi giá chạm mức có nhiều stop mua, các stop thành lệnh mua market — cùng chiều với chuyển động vừa xảy ra — có thể đẩy giá đi xa hơn và kích hoạt stop kế tiếp (cascade).
4. **Khi nhiều lệnh được kích hoạt hoặc khớp trong một vùng giá hẹp, hành vi giá thay đổi:** tăng tốc (nếu phía đối diện mỏng) hoặc khựng lại / quay đầu (nếu có người đứng sẵn phía đối diện hấp thụ).

#### 3.2 Vì sao một số mức giá "đáng chú ý" hơn mức khác?

**Cơ chế gốc: điểm hội tụ (focal point / salience).** Khi nhiều người cùng nhìn một chart và cùng học một kiểu đặt stop ("stop trên đỉnh gần nhất"), các quyết định của họ **dồn về cùng vài mức giá**. Không cần ai phối hợp — chỉ cần cùng một tham chiếu. **[INTERPRETATION]** có cơ sở thực nghiệm:

- **Osler (2003, *Journal of Finance*)** — dữ liệu lệnh có điều kiện của một ngân hàng FX: lệnh **take-profit dồn tại số tròn**, lệnh **stop-loss dồn ngay sau số tròn** (stop mua ngay trên, stop bán ngay dưới). Điều này phù hợp với hai hiện tượng kỹ thuật lâu đời: xu hướng hay **chững/đảo tại số tròn** và hay **tăng tốc sau khi vượt** chúng. **[MARKET MECHANICS]**
- **Osler (2005, *Journal of International Money and Finance*)** — giá FX có xu hướng chuyển động nhanh hơn sau khi đi vào vùng tập trung stop-loss ("price cascades"), và hiệu ứng kéo dài hơn so với vùng tập trung take-profit. Tác giả không chứng minh được quan hệ **nhân quả** từ dữ liệu đó. **[MARKET MECHANICS]**, mức độ: tương quan.
- **Garzarelli và cộng sự (2014, *Scientific Reports*)** — trên dữ liệu cổ phiếu, giá có xu hướng **bật lại** tại các mức support/resistance được định nghĩa khách quan nhiều hơn một quá trình không nhớ; tác giả diễn giải là dấu hiệu của **niềm tin tự củng cố** (self-fulfilling) của người giao dịch kỹ thuật. **[MARKET MECHANICS]** (thực nghiệm) + **[INTERPRETATION]** (cơ chế).

> [!note] Đọc các bằng chứng này cho đúng
> Chúng nói về **số tròn** và **S/R được định nghĩa khách quan** — không phải về "BSL/SSL của ICT" như một mô hình giao dịch. Chúng cho thấy *cơ chế nền* (lệnh dồn quanh mức nổi bật; giá phản ứng khác thường ở đó) là có thật. Chúng **không** cho thấy mỗi đỉnh bạn kẻ đều có stop, hay rằng giá "phải" tới đó.

#### 3.3 Tại sao giá di chuyển đến một mức liquidity?

Có ít nhất bảy cơ chế không cần giả định một "Smart Money" toàn năng (chi tiết: [[20-Liquidity-Sweep]] §4.1). Bảng dưới là bản tóm tắt dùng cho note gốc:

| # | Cơ chế | Dấu vết trên chart | Nhãn | Giới hạn |
|---|---|---|---|---|
| A | **Kích hoạt stop** — stop thành market, dây chuyền | Tăng tốc ngay sau mức, nến dài | [MARKET MECHANICS] | Giải thích vì sao giá **đi qua** nhanh, không giải thích vì sao giá **tới** |
| B | **Nhu cầu khớp lệnh lớn** — người cần khớp nhiều tìm nơi có đối ứng | Có thể là hấp thụ (giá đứng yên dù giao dịch nhiều) | [INTERPRETATION] | Không thấy ý định; không có bằng chứng công khai là lệnh lớn *thường* tìm tới cụm stop |
| C | **Price discovery** — giá "thử" mức mới: có người giao dịch thì ở lại, không thì quay về | Acceptance hoặc rejection | [MARKET MECHANICS] | Mô tả được kết quả, khó dự báo trước nhánh nào |
| D | **Người giao dịch breakout** vào lệnh tại mức nổi bật | Dòng lệnh cùng chiều tại mức | [MARKET MECHANICS] | Hiệu quả của breakout là chuyện khác |
| E | **Thuật toán thực thi & market making** né vùng mỏng, rút quote trước mức nhạy cảm | Chỉ thấy bằng dữ liệu sổ lệnh chi tiết | [INTERPRETATION] | Không áp dụng được cho một sự kiện cụ thể từ OHLC |
| F | **Kích hoạt có chủ đích** (predatory — Brunnermeier & Pedersen 2005) | **Không phân biệt được** với A trên OHLC | [INTERPRETATION] | Có thể xảy ra; **không** phải lời giải thích mặc định |
| G | **Động lực đấu giá (AMT)** — giá quảng bá ra xa tìm đối ứng, gặp "excess" thì quay về | Đuôi dài + quay về vùng giá trị | [INTERPRETATION] (khung AMT) | Ít bằng chứng thống kê công khai |
| **H** | **Baseline hình học** — mức gần hơn bị chạm trước với xác suất cao hơn, chỉ vì nó gần | Không có dấu vết riêng — đó chính là vấn đề | [MATHEMATICAL] | **Bắt buộc kiểm trước mọi cơ chế khác** |

![[Liquidity-v2-03-Order-Book-Va-Stop.svg|900]]

> [!example]- Hình 03 — đọc thế nào
> - **Đang diễn ra gì:** ba ảnh chụp sổ lệnh quanh mức L khi giá đi từ dưới lên: trước khi chạm, lúc chạm (stop thành market, ăn hết ask), và hai nhánh có thể sau đó.
> - **Mức được đánh dấu:** L — một đỉnh cũ.
> - **Timeframe:** cơ chế xảy ra ở cấp tick/giây; trên M5 bạn chỉ thấy một cây nến có wick.
> - **Vì sao đáng chú ý:** cùng một cú "giá vọt qua L" có thể kết thúc bằng **hấp thụ** (nhánh A → ứng viên sweep) hoặc **chấp nhận** (nhánh B → breakout).
> - **Đã xác nhận:** chỉ khi xem giá làm gì sau đó (close ở đâu, trong bao nhiêu nến).
> - **Chưa biết:** tại thời điểm ② không ai biết nhánh nào; khối lượng trên hình là giả định.
> - **Làm gì tiếp:** đừng phân loại tại wick; chờ cửa sổ phân xử (mục 22).

#### 3.4 Câu hỏi quan trọng nhất: ta quan sát giá đi tới liquidity, hay ta chọn mức liquidity sau khi giá đã tới đó?

Trên một chart bất kỳ có hàng chục đỉnh/đáy. Sau khi giá chạy, **luôn luôn** có một đỉnh/đáy nào đó nằm gần điểm giá quay đầu. Nếu bạn chọn mức **sau** khi thấy giá quay đầu, câu "giá đã đi lấy liquidity" sẽ đúng 100% — và không chứa thông tin gì.

**Cách tránh lựa chọn hậu nghiệm (bắt buộc):**

1. **Danh sách mức chốt trước** khi giá tiếp cận (trước phiên), có giờ ghi (RULE-LQ-003).
2. **Thuật toán chọn mức được khai báo** (N-bar pivot, dung sai EQH, khung giờ phiên) — không "nhìn bằng mắt".
3. **Mức không có trong danh sách mà bị xuyên** → ghi "unlisted breach", **không** gọi là sweep (RULE-LS-001).
4. **Ghi cả những mức không bao giờ bị chạm** — đó là mẫu số của mọi tỷ lệ.
5. **So với baseline hình học** (mục 5) trước khi kết luận "giá có xu hướng tới liquidity".

---

### 4. Những gì biểu đồ có thể và không thể cho biết

| Chart OHLC **cho biết** [OBSERVABLE] | Chart OHLC **không cho biết** |
|---|---|
| Mức giá của đỉnh/đáy, PDH/PDL, high/low phiên | Có bao nhiêu lệnh chờ sau mức đó |
| Thời điểm một swing được xác nhận (theo thuật toán bạn chọn) | Ai đặt lệnh, vì sao, còn hay đã hủy |
| Giá có giao dịch qua mức hay không, sâu bao nhiêu (theo ATR) | Lệnh nào đã khớp khi giá xuyên mức |
| Close nằm ở đâu so với mức, sau bao nhiêu nến | Ai là người "hấp thụ" khi giá quay lại |
| Tốc độ (range nến, số nến), FVG để lại | Ý định, sự phối hợp, "thuật toán trung tâm" |
| Cấu trúc swing nào bị phá | Mức nào **sẽ** bị chạm tiếp theo |

**Ba giới hạn dữ liệu cụ thể của trader retail:**

- **FX spot phi tập trung.** Không có một sổ lệnh chung; "volume" trên MT4/MT5/TradingView FX thường là **tick volume** (số lần giá thay đổi), không phải khối lượng giao dịch. Futures (NQ trên CME) có khối lượng thật, nhưng DOM cũng chỉ hiện lệnh limit, không hiện stop.
- **Feed khác nhau cho high/low khác nhau.** CFD broker và sàn gốc có thể lệch vài tick đúng ở đỉnh/đáy — đủ để một feed "đã xuyên", feed kia "chưa chạm". Chốt một feed chuẩn cho toàn bộ backtest và ghi `feed_source`.
- **Mốc thời gian.** PDH/PDL phụ thuộc giờ đóng ngày (17:00 New York cho FX; phiên CME cho NQ) và cài đặt múi giờ của chart. Vault quy ước chart theo **giờ New York**.

**Ex-ante vs ex-post.** Mọi câu trong journal phải gắn được vào một thời điểm: *"tại 19:40 VN, tôi biết X, chưa biết Y"*. Một nhãn (ví dụ "sweep") có `known_at` = **close của nến phân xử**, không phải lúc wick chạm.

---

### 5. Vì sao Liquidity không phải là lời tiên tri

| Mệnh đề hay gặp | Trạng thái đúng |
|---|---|
| "Có liquidity thì giá sẽ tới đó" | **Sai về dạng mệnh đề.** Mức có thể không bao giờ bị chạm trong horizon của bạn |
| "Giá tới liquidity thì sẽ đảo chiều" | **Sai.** Giá có thể xuyên qua và được chấp nhận (breakout / run) |
| "Giá xuyên qua mức = sweep đã hoàn tất" | **Sai.** Sweep là kết quả **phân xử** sau cửa sổ k nến (mục 22) |
| "Vượt qua rồi tiếp tục là sweep thất bại" | **Không chính xác.** Đó là sự kiện khác (acceptance / run); ghi đúng tên |
| "Mức được chọn làm mục tiêu thì sẽ hoạt động" | **[HYPOTHESIS]** — DOL có thể sai; tỷ lệ đúng phải đo |
| "Lúc nào cũng phải xác định được một DOL" | **Sai.** "Chưa có DOL rõ" là kết luận hợp lệ (mục 28–29, RULE-LQ-007) |

**Baseline hình học — phép thử bắt buộc.** Với random walk không drift bắt đầu giữa hai mức, xác suất chạm mức gần trước là **d_xa / (d_gần + d_xa)** **[MATHEMATICAL]** (gambler's ruin). Nghĩa là: nếu mức gần cách 1 ATR và mức xa cách 3 ATR, **75%** số lần mức gần bị chạm trước — **không cần bất kỳ "liquidity" nào**.

![[Liquidity-v2-28-Baseline-Hinh-Hoc.svg|900]]

> [!example]- Hình 28 — đọc thế nào
> - **Đang diễn ra gì:** đường cong P(mức gần bị chạm trước) theo tỷ lệ khoảng cách d_xa/d_gần, cho random walk không drift.
> - **Mức được đánh dấu:** bốn điểm 1×, 2×, 3×, 4× → 50%, 67%, 75%, 80%.
> - **Timeframe:** độc lập khung thời gian (chỉ phụ thuộc khoảng cách tính theo cùng một thước đo biến động).
> - **Vì sao đáng chú ý:** phần lớn câu "giá luôn lấy liquidity gần trước" có thể chỉ là hình học.
> - **Đã xác nhận:** công thức đúng về toán với giả định nêu.
> - **Chưa biết:** thị trường thật có drift, biến động đổi theo phiên, cửa sổ thời gian hữu hạn — baseline nâng cao cần mô phỏng trên dữ liệu của chính bạn.
> - **Làm gì tiếp:** mọi tỷ lệ trong journal phải được trừ baseline trước khi gọi là "edge".

> [!important] Mô hình tư duy chốt Part I
> **Liquidity là một công cụ để XÂY và KIỂM TRA giả thuyết về hành vi giá — không phải công cụ biết trước giá sẽ đi đâu.**
> Nó trả lời tốt câu hỏi *"nên nhìn vào đâu và hỏi gì?"*; nó trả lời kém câu hỏi *"giá sẽ làm gì?"*.

---

### 6. Bản đồ tổng quan về Liquidity

Hình 01 (đầu note) là bản đồ **quy trình**. Bảng dưới là bản đồ **đối tượng** — mọi thứ note này đặt tên, thuộc loại nào, và được định nghĩa ở đâu.

| Nhóm | Đối tượng | Loại | Định nghĩa | Mục |
|---|---|---|---|---|
| Nền tảng | Market liquidity | Khái niệm thị trường | DEF-LQ-01 | 1 |
| Nền tảng | Liquidity reference level | **Mức** | DEF-LQ-02 | 1, 14 |
| Phía | BSL / SSL | **Mức** (phân theo phía) | DEF-LQ-03/04 | 7, 8 |
| Nguồn mức | Swing high/low | **Mức** (từ thuật toán) | DEF-LQ-05 | 9 |
| Nguồn mức | EQH / EQL | **Mức** (hai swing gần bằng nhau) | DEF-LQ-06 | 10 |
| Vai trò | Internal / External | **Quan hệ** mức – range | DEF-LQ-07 | 11, 12 |
| Nguồn mức | PDH/PDL, PWH/PWL, Asia/London H-L | **Mức** (theo thời gian) | DEF-LQ-08 | 13 |
| Tầm quan trọng | Significant liquidity | **Thuộc tính** của mức | DEF-LQ-09 | 14 |
| Sự kiện | Liquidity event (E0–E9) | **Sự kiện** | DEF-LQ-10 | 22–26 |
| Sự kiện | Sweep / Run / Breakout | **Sự kiện** (đã phân xử) | DEF-LS-04 / DEF-LS-05 / E4 | 22–24 |
| Mục tiêu | DOL | **Giả thuyết** có trạng thái | DEF-LQ-14 | 28–33 |
| Kết quả | Post-liquidity reaction | **Biến đo** | DEF-LQ-15 | 25, 55 |
| Vận hành | Trạng thái theo dõi | **Trạng thái** | DEF-LQ-16 | 39, 43 |

**Chuỗi suy luận đúng thứ tự** — mỗi mũi tên là một bước có thể sai, phải ghi riêng:

```text
MỨC (ex-ante)  →  SỰ KIỆN đã xảy ra  →  PHÂN LOẠI (E-code)  →  Ý NGHĨA với cấu trúc  →  GIẢ THUYẾT tiếp theo  →  KẾT QUẢ (chỉ biết sau)
[OBSERVABLE]       [OBSERVABLE]          [định nghĩa]           [INTERPRETATION]          [HYPOTHESIS]               [OBSERVABLE, ex-post]
```

---
## PART II — LIQUIDITY CLASSIFICATION

![[Liquidity-v2-04-BSL-SSL.svg|900]]

> [!example]- Hình 04 — đọc thế nào
> - **Đang diễn ra gì:** một range với hai đỉnh gần bằng nhau (EQH) phía trên và hai đáy gần bằng nhau (EQL) phía dưới; giá hiện tại ở giữa.
> - **Mức được đánh dấu:** L của EQH (BSL) và L của EQL (SSL), cùng vùng [L, L + w] / [L − w, L] phía bên kia.
> - **Timeframe:** minh họa — có thể là H1.
> - **Vì sao đáng chú ý:** tên gọi theo **phía của lệnh có điều kiện** sẽ bị kích hoạt; mỗi vùng còn chứa lệnh chờ ngược chiều (chốt lời, người bán đỉnh / bắt đáy).
> - **Đã xác nhận:** chỉ có vị trí hai mức.
> - **Chưa biết:** có bao nhiêu lệnh ở mỗi vùng; giá sẽ chạm phía nào trước (xem baseline mục 5).
> - **Làm gì tiếp:** đưa hai mức vào danh sách nếu qua cổng G1–G5 (mục 14); ghi phía nào là ERL/IRL của range đã khai báo.

### 7. Buy-Side Liquidity (BSL)

**T1 — Đời thường.** Một cái trần nhà mà ai cũng thấy. Người cược "trần sẽ giữ" dặn môi giới: *"nếu giá vượt trần thì cắt lỗ cho tôi"* (tức là **mua lại**). Người cược "trần sẽ vỡ" dặn: *"nếu giá vượt trần thì mua cho tôi"*. Hai nhóm ngược quan điểm nhưng **đặt lệnh mua ở cùng một chỗ** — ngay trên trần.

**T2 — Diễn biến giá.** Giá tạo đỉnh 1.0920 rồi giảm về 1.0880. Người short ở 1.0915 đặt stop 1.0925. Người chờ breakout đặt buy-stop 1.0923. Khi giá quay lên: buy-stop 1.0923 kích hoạt trước, stop 1.0925 ngay sau — lần lượt, gần như cùng lúc nếu giá nhảy. Nếu phía bán ở 1.0925–1.0930 mỏng, giá nhảy nhanh; nếu có người bán lớn đứng chờ, giá có thể khựng và quay xuống. *(Số liệu giả định.)*

**T3 — ICT.** **Buy-Side Liquidity** là liquidity nằm **phía trên** các đỉnh tham chiếu: swing high, **Equal Highs (EQH)**, **PDH**, **PWH**, high phiên Asia/London, số tròn phía trên. Gọi là "buy-side" vì lệnh có điều kiện ở đó, khi kích hoạt, là **lệnh MUA**. **[ICT FRAMEWORK]**

> [!example] DEF-LQ-03 — Buy-Side Liquidity (v0.1)
> Một liquidity reference level **L nằm trên giá hiện tại**, cùng vùng [L, L + w] phía trên nó, nơi **giả định** có: (a) lệnh MUA có điều kiện — stop-loss của người đang short, buy-stop vào breakout, thanh lý vị thế short có đòn bẩy; và (b) lệnh BÁN chờ tại/trước L — chốt lời của người long, người bán ở đỉnh. Mặc định w = 0.25 × ATR(14) của khung xác nhận L **[HEURISTIC]**.

**Thành phần của BSL — và ai được lợi khi nó bị kích hoạt:**

| Thành phần | Lệnh gì | Khi kích hoạt làm gì | Nhãn |
|---|---|---|---|
| Stop-loss của người short | BUY stop | Mua market → đẩy giá lên | [INTERPRETATION] (vị trí), [MARKET MECHANICS] (hành vi) |
| Buy-stop vào breakout | BUY stop | Mua market | như trên |
| Thanh lý short có đòn bẩy | Mua cưỡng bức | Mua market | như trên |
| Chốt lời của người long / người bán đỉnh | SELL limit | Đứng chờ, **hấp thụ** lệnh mua | [INTERPRETATION] |

Người **cần BÁN** khối lượng lớn được lợi khi BSL bị kích hoạt: có một dòng lệnh mua đột ngột để khớp mà không phải tự đẩy giá xuống. Đây là logic cơ học đằng sau câu chuyện ICT *"lấy BSL rồi giảm"*. Logic khớp lệnh là **[MARKET MECHANICS]**; việc *ai* đã thực sự bán là **[INTERPRETATION]** không xác minh được.

**BSL khác "kháng cự" như thế nào?**

| | Kháng cự (phân tích kỹ thuật cổ điển) | BSL (ICT) |
|---|---|---|
| Câu hỏi | Giá có **dừng / đảo** ở đây không? | **Lệnh** có thể nằm ở đâu? |
| Hàm ý khi giá chạm | Kỳ vọng bán, giá quay đầu | Không hàm ý hướng; giá có thể xuyên qua (kích hoạt stop) |
| Khi giá xuyên qua | "Kháng cự bị phá" → thường kỳ vọng tăng | Có thể là sweep (rồi quay lại) **hoặc** acceptance — phải phân xử |
| Lỗi thường gặp | Bán mù tại kháng cự | Bán ngay khi giá vừa chạm BSL, trước khi có bất kỳ phân xử nào |

**BSL có hai vai trò — cả hai đều là giả thuyết:**

1. **Mục tiêu (DOL):** khi bối cảnh D1 tăng, BSL phía trên là ứng viên mục tiêu (mục 28–33).
2. **Nơi quan sát phản ứng:** khi bối cảnh D1 giảm và giá ở premium, BSL phía trên là nơi có thể xảy ra sweep trước khi giảm tiếp — **chỉ là ứng viên**; phải có rejection + xác nhận (mục 22, 25).

**Khi giá vượt BSL, khi nào có xu hướng tiếp tục, khi nào có xu hướng quay lại?** Đây là câu hỏi dự báo — note **không** trả lời bằng khẳng định, chỉ liệt kê các biến cần đo **[HYPOTHESIS] [BACKTEST REQUIRED]**:

| Biến | Nghiêng về acceptance / tiếp tục (giả thuyết) | Nghiêng về rejection / quay lại (giả thuyết) |
|---|---|---|
| Bối cảnh D1/H1 | BSL cùng hướng cấu trúc HTF; đang có RUN cùng phía | BSL ngược cấu trúc HTF, ở premium của range D1 |
| Vai trò trong range | BSL là IRL trên đường tới ERL lớn hơn (waypoint) | BSL là ERL của range D1 / nằm trong HTF POI |
| Close sau khi xuyên | ≥ 2 close liên tiếp trên L, retest giữ được | Close quay lại dưới L − δ trong k nến |
| Displacement | Theo hướng xuyên | Ngược hướng xuyên, phá swing có ý nghĩa |
| Thời điểm | Tin tier-1 / mở phiên với dòng lệnh một chiều | Killzone sau khi mức đã được "chốt" từ trước |

**Làm sao phân biệt BSL tiềm năng với một đường kẻ tùy tiện?** Một mức chỉ được gọi là BSL trong journal khi qua **5 cổng** (mục 14): G1 có `known_at` trước quyết định · G2 là swing đã xác nhận theo thuật toán khai báo (hoặc nhãn thời gian/EQH theo định nghĩa) · G3 chưa bị giao dịch qua · G4 đúng phía (trên giá) · G5 không phải dữ liệu bẩn (gap rollover, spike lỗi feed).

> [!warning] Buy-Side Liquidity KHÔNG phải là
> - Không phải kháng cự để bán mù khi giá chạm.
> - Không phải tín hiệu Short độc lập — cần phân xử (rejection) + xác nhận (MSS + displacement) + bối cảnh.
> - Không phải lúc nào cũng là điểm đảo — trong bối cảnh tăng, BSL có thể chỉ là trạm trung chuyển (waypoint) [HYPOTHESIS — HYP-LQ-011].
> - Không nằm dưới giá (đó là SSL).
> - Không phải mọi đỉnh đều "nặng" như nhau — xem cấp độ ở mục 14.

---

### 8. Sell-Side Liquidity (SSL)

**T1 — Đời thường.** Cái sàn nhà ai cũng thấy. Người cược "sàn sẽ giữ" dặn *"nếu thủng sàn thì cắt lỗ cho tôi"* (tức là **bán ra**). Người cược "sàn sẽ vỡ" dặn *"nếu thủng sàn thì bán cho tôi"*. Lại hai quan điểm ngược nhau, **cùng đặt lệnh bán ngay dưới sàn**.

**T2 — Diễn biến giá.** Đáy 1.0840; người long đặt stop 1.0835; người chờ breakdown đặt sell-stop 1.0837. Giá giảm qua 1.0837 rồi 1.0835 → hai lệnh lần lượt thành lệnh bán market (gần như cùng lúc nếu giá nhảy). Có người mua lớn đứng chờ → giá có thể bật lên; không có → giá trượt tiếp. *(Số liệu giả định.)*

**T3 — ICT.** **Sell-Side Liquidity** nằm **phía dưới** đáy tham chiếu: swing low, **Equal Lows (EQL)**, **PDL**, **PWL**, low phiên Asia/London, số tròn phía dưới. Lệnh có điều kiện ở đó là **lệnh BÁN**. **[ICT FRAMEWORK]**

> [!example] DEF-LQ-04 — Sell-Side Liquidity (v0.1)
> Một liquidity reference level **L nằm dưới giá hiện tại**, cùng vùng [L − w, L], nơi **giả định** có: (a) lệnh BÁN có điều kiện — stop-loss của người long, sell-stop vào breakdown, thanh lý long có đòn bẩy; (b) lệnh MUA chờ tại/trước L — chốt lời của người short, người bắt đáy. w mặc định = 0.25 × ATR(14) của khung xác nhận **[HEURISTIC]**.

**SSL khác "hỗ trợ":** hỗ trợ là dự đoán giá **dừng** ở đó; SSL là giả thuyết về **lệnh bán** nằm ngay dưới đó — giá có thể thủng qua chính vì những lệnh đó được kích hoạt. Người **cần MUA** khối lượng lớn có đối ứng khi SSL bị kích hoạt — logic đằng sau câu ICT *"lấy SSL rồi tăng"* (thường gắn với **Judas swing** trong mô hình AMD — [[02-AMD]]). **[ICT FRAMEWORK]** cho câu chuyện; **[INTERPRETATION]** cho ai đã mua.

**Điều gì có thể xảy ra khi giá chạm hoặc vượt SSL** — năm nhánh quan sát được (mã E ở mục 22–26):

| Quan sát [OBSERVABLE] | Mã | Tên gọi | Có được gọi là sweep? |
|---|---|---|---|
| Giá tới gần nhưng low > L + ε | E0 | Near-miss | Không |
| Low trong ±ε quanh L, close trên L | E1 | Chạm | Không |
| Low < L − ε, close nến đó > L + δ | E2 | Rejection ngay nến xuyên | **Có** (sweep) |
| Close nến xuyên ≤ L + δ (chưa phân xử), rồi trong k nến close > L + δ | E3 | Failed breakdown | **Có** (sweep) |
| ≥ 2 close liên tiếp dưới L, hoặc 1 close cách L > 0.5·ATR | E4 | Acceptance / breakdown | Không — là phá vỡ |

> [!warning] Sell-Side Liquidity KHÔNG phải là
> - Không phải hỗ trợ để mua mù khi giá chạm.
> - Không phải tín hiệu Long độc lập.
> - Không phải lúc nào cũng là điểm đảo — trong bối cảnh giảm, SSL có thể chỉ là trạm trung chuyển (waypoint) [HYPOTHESIS — HYP-LQ-011].
> - Không nằm trên giá (đó là BSL).
> - Không phải mọi đáy đều quan trọng như nhau.

> [!tip] Mẹo nhớ tên gọi
> **Tên = phía của lệnh có điều kiện sẽ bị kích hoạt.** BSL → kích hoạt lệnh MUA → nằm TRÊN. SSL → kích hoạt lệnh BÁN → nằm DƯỚI. Tên **không** nói giá sẽ đi lên hay xuống.

---

### 9. Swing Highs và Swing Lows

**T1.** Một swing high là "một cái đỉnh mà hai bên đều thấp hơn". Vấn đề: chart nào cũng có hàng trăm cái như vậy. Nếu cái nào cũng là liquidity thì câu "giá đi lấy liquidity" mô tả **mọi** chuyển động — tức là không mô tả gì.

**T3 — ICT.** Swing là **nguồn tham chiếu** để đặt BSL/SSL. ICT phân biệt short-term / intermediate-term / long-term high-low ([[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]). **[ICT FRAMEWORK]**

> [!example] DEF-LQ-05 — Swing high/low dùng cho liquidity (v0.1)
> - **D1 và H1:** N-bar pivot với **N = 3** — high của nến t lớn hơn high của 3 nến trước và 3 nến sau (low đối xứng). **known_at = close của nến thứ 3 sau pivot.** Trước thời điểm đó, swing **chưa tồn tại** với bạn.
> - **M5:** Directional Change với ngưỡng **θ = 0.4 × ATR(14, M5)** — swing high được xác nhận khi giá giảm từ đỉnh gần nhất ≥ θ. known_at = nến xác nhận.
> - Lý do và đánh đổi nhạy ↔ trễ: [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]. **[HEURISTIC]** — giữ cố định trong một đợt backtest.

**Vì sao không phải mọi swing quan trọng như nhau?** Năm câu hỏi (biến S, L, D, R, T — dùng lại framework swing của project):

| Biến | Câu hỏi | Vì sao làm swing "nổi tiếng" hơn (lập luận cơ chế) |
|---|---|---|
| **S** — cấu trúc | Swing có bảo vệ cấu trúc (protected high/low) hoặc là biên dealing range không? | Người theo cấu trúc đặt stop "đúng sách" ở đó |
| **L** — liquidity | Swing hình thành bằng một cú xuyên mức trước đó? Nó có tạo ra pool mới không? | Cực trị của một cú quét thường là wick rõ — dễ thấy |
| **D** — displacement | Leg rời khỏi swing có mạnh bất thường không? | Leg mạnh làm swing được nhiều người chú ý, để lại FVG |
| **R** — phản ứng | Biên độ phản ứng từ swing (theo ATR)? | Phản ứng lớn = nhiều người nhớ |
| **T** — khung | Swing xác nhận ở khung nào? | Swing D1 được nhiều người nhìn hơn swing M5 |

**Khi nào một swing trở nên quan trọng?** Khi **phá nó sẽ làm đổi cách đọc cấu trúc** — nó gây ra hoặc bảo vệ một thay đổi cấu trúc. Ví dụ: higher low tạo ra cú phá đỉnh gần nhất (protected low) quan trọng hơn mọi đáy nhỏ bên trong nhịp hồi.

**Khi swing đã bị vượt qua thì sao?** Cập nhật ngay:
- Bị xuyên + **rejection** → mức "đã bị kiểm tra"; cực trị của cú xuyên trở thành **mức mới** L' (mục 26, hình 36).
- Bị xuyên + **acceptance** → mức "spent" ở vai trò cũ; nếu là swing cấu trúc → cấu trúc đổi (BOS/MSS tùy định nghĩa).
- **Không xóa** dòng cũ trong journal — thêm dòng mới (append-only).

---

### 10. Equal Highs và Equal Lows

![[Liquidity-v2-05-EQH-EQL-Dung-Sai.svg|900]]

> [!example]- Hình 05 — đọc thế nào
> - **Đang diễn ra gì:** trái là một EQH hợp lệ trên H1; phải là ba trường hợp nhìn "giống EQH" nhưng không qua định nghĩa.
> - **Mức được đánh dấu:** L = max(H₁, H₂); dải màu là dung sai.
> - **Timeframe:** H1 (trường hợp c cố tình trộn H1 với M5 để minh họa lỗi).
> - **Vì sao đáng chú ý:** "gần bằng nhau" không có con số thì mỗi người một EQH khác nhau.
> - **Đã xác nhận:** chỉ hình học của hai đỉnh.
> - **Chưa biết:** EQH có thật sự chứa nhiều stop hơn đỉnh đơn không — đó là giả thuyết cần đo.
> - **Làm gì tiếp:** chốt dung sai, khoảng cách tối thiểu và nhịp hồi tối thiểu trước khi đánh dấu; không chỉnh theo chart.

**T1.** Hai lần giá đụng trần rồi rơi → ai cũng thấy "trần". Người cược trần giữ và người cược trần vỡ **cùng đặt lệnh ngay trên trần cao hơn trong hai lần đụng**. Đó là lý do EQH được coi là liquidity "rõ".

**T3 — ICT.** ICT gọi là **equal highs / equal lows** hoặc **relative equal highs/lows** ("smooth" highs/lows) — được xem là liquidity dễ thấy, thường được dùng làm mục tiêu hoặc được diễn giải là "mồi" (inducement). **[ICT FRAMEWORK]**

> [!example] DEF-LQ-06 — EQH / EQL (v0.1)
> Hai (hoặc nhiều) swing high **đã xác nhận trên cùng một khung T** (DEF-LQ-05) thỏa:
> 1. |H₁ − H₂| ≤ **0.10 × ATR(14, T)** tại thời điểm H₂ được xác nhận;
> 2. cách nhau ≥ **3 nến**;
> 3. giữa hai đỉnh giá **hồi ≥ 0.5 × ATR(14, T)** và **không có close nào > max(H₁, H₂)**.
> **L = max(H₁, H₂)** (EQL: L = min). **known_at = known_at của swing thứ hai.** Mọi ngưỡng là **[HEURISTIC]**.

**Hai mức có cần bằng nhau tuyệt đối không?** Không — nhưng phải có **dung sai khai báo trước**. Theo mô phỏng random walk trong [[20-Liquidity-Sweep]] (LS-Sim-07, **[SIMULATION]**): số EQH "tự nhiên xuất hiện" là khoảng 1.5 / 2.8 / 5.4 / 8.0 lần mỗi 1.000 nến M15 với dung sai 0.05 / 0.1 / 0.2 / 0.3 ATR. Hai điều suy ra:
- **EQH xuất hiện cả khi không có ai "engineer"** — sự tồn tại của EQH không phải bằng chứng thao túng.
- **Đổi dung sai làm số EQH đổi ~5 lần** — nới dung sai sau khi nhìn chart là cách nhanh nhất để tự lừa.

**Khi nào một cụm đỉnh/đáy thực sự đáng quan tâm?** (giả thuyết để test, không phải luật):
- EQH nằm ở **khung ≥ H1** và trùng vai trò cấu trúc (biên range, protected high/low) → đưa vào danh sách.
- EQH nằm **ngay trước một POI HTF** → ICT hay gọi là inducement; nếu muốn dùng nhãn này, phải gắn `engineered?: yes` **trước** khi biết kết quả, rồi đếm sau 30+ trường hợp.
- EQH chỉ là hai wick dính nhau, hoặc trộn khung → **không** tính.

**Đánh dấu bằng mắt vs quy tắc khách quan:**

| | Bằng mắt | Quy tắc DEF-LQ-06 |
|---|---|---|
| Tốc độ | Nhanh | Chậm hơn (phải đo ATR, đếm nến) |
| Tái lập được? | Không — hai người hai kết quả | Có |
| Backtest được? | Không | Có |
| Rủi ro | Chọn sau khi thấy giá chạy | Ngưỡng có thể chưa tối ưu — nhưng nhất quán |

> [!note] Dung sai theo pip/tick (bản cũ) → theo ATR (bản này)
> Note BSL cũ đề xuất "≤ 3 tick NQ, ≤ 2 pip FX". Bản này đổi sang **0.10 × ATR(14)** để cùng một quy tắc dùng được cho mọi sản phẩm và mọi chế độ biến động. Con số pip/tick cũ vẫn có thể dùng như phép kiểm tra nhanh (sanity check). Xem Phụ lục C.

---

### 11. Internal Liquidity

![[Liquidity-v2-07-Internal-External-Range.svg|900]]

> [!example]- Hình 07 — đọc thế nào
> - **Đang diễn ra gì:** một range D1 đã khai báo (biên trên = swing high lớn, biên dưới = swing low lớn); giá đang hồi lên bên trong range.
> - **Mức được đánh dấu:** ERL trên/dưới (ngoài hai biên) và ba IRL bên trong (swing high nội bộ, swing low nội bộ, FVG chưa lấp).
> - **Timeframe:** D1 (bên trái); bên phải minh họa cùng một mức X dưới hai range khác nhau.
> - **Vì sao đáng chú ý:** "internal/external" là **quan hệ** giữa mức và range, không phải thuộc tính cố định.
> - **Đã xác nhận:** vị trí các mức so với range đã chọn.
> - **Chưa biết:** giá sẽ tới IRL hay ERL trước; range có bị re-map sau displacement không.
> - **Làm gì tiếp:** mọi nhãn ERL/IRL trong journal kèm tên range, ví dụ `ERL(D1 range 2026-10-01→10-09)`.

> [!example] DEF-LQ-07 — Internal / External liquidity (v0.1)
> Cho một range tham chiếu **R** đã khai báo (hai biên, ngày khai báo, lý do chọn):
> - **External Range Liquidity — ERL(R):** BSL tại/trên biên trên của R và SSL tại/dưới biên dưới của R.
> - **Internal Range Liquidity — IRL(R):** các mức nằm **trong** R — swing nhỏ hơn, EQH/EQL bên trong, FVG chưa lấp (theo cách dùng ICT).
> - **Mặc định:** khi không ghi R, R = **range D1 context** chốt trước phiên (RULE-LS-009).

**T1.** Một căn phòng có tường (biên range). Đồ vật trong phòng là "internal"; thứ nằm ngoài tường là "external". Nhưng nếu bạn đổi sang xét **cả ngôi nhà**, bức tường phòng ngủ chỉ còn là một thứ bên trong nhà.

**Vì sao phải xác định range TRƯỚC khi phân loại?** Vì cùng một mức đổi vai khi đổi range (hình 07, bên phải). Nếu không khai báo range, bạn có thể gọi một cú quét bất kỳ là "external" — ngôn ngữ nghe có trọng lượng nhưng không có nội dung.

**[ICT FRAMEWORK]** ICT mô tả giá "dao động" giữa ERL và IRL: lấy ERL → hồi về IRL (thường là FVG) → từ IRL đi tới ERL kế tiếp ([[16-Internal-External-Range-Liquidity-IRL-ERL]]). Đây là **mô tả** một khuôn mẫu; tỷ lệ nó đúng là **[HYPOTHESIS]** (HYP-DOL trong [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]).

**Không mặc định mọi swing bên trong range là IRL có giá trị như nhau.** Một swing H1 cấu trúc bên trong range D1 (Level 3) khác hẳn một fractal M5 bên trong range D1 (Level 1). Dùng cấp độ ở mục 14.

**Lưu ý về FVG như IRL:** FVG **không** phải "cụm stop" — nó là vùng giá đi một chiều để lại khoảng trống ([[13-FVG-Fair-Value-Gap]]). ICT xếp nó vào IRL vì theo ICT giá hay quay lại vùng đó [ICT FRAMEWORK] — tần suất thực tế [BACKTEST REQUIRED]; cơ chế khác với stop cluster. Đừng trộn hai cơ chế khi giải thích một phản ứng.

---

### 12. External Liquidity

**ERL là gì:** liquidity ở/ngoài **hai biên** của range đã khai báo. Trong framework D1 → H1 → M5 của vault, ERL của **range D1 context** là ứng viên DOL ngày/tuần mặc định.

**Một mức có thể internal ở range này, external ở range khác — ví dụ cụ thể:** range H1 của phiên London là 1.0850–1.0890. High 1.0890 là **ERL(H1 London range)**. Nhưng range D1 context là 1.0780–1.0960 → 1.0890 là **IRL(D1 range)**. Một cú quét 1.0890 là "sweep external" với người nhìn H1 và "sweep internal" với người nhìn D1. Ý nghĩa của nó thuộc về swing bị lấy (khung xác nhận của 1.0890), không thuộc về chart bạn đang mở.

**Khi nào phân loại ERL/IRL hữu ích?**
- Khi chọn DOL: ERL của range D1 là ứng viên mục tiêu có thứ bậc cao hơn IRL.
- Khi đọc ý nghĩa một sự kiện: sweep ERL của range D1 có tỷ lệ rejection khác sweep IRL hay không là giả thuyết **HYP-LQ-001**; hàm ý cấu trúc của nó (range có đổi không) thì rõ hơn vì ERL là biên range.
- Khi quản lý lệnh: IRL thường là mục tiêu từng phần (T1), ERL là mục tiêu cuối (T2) — **quy ước quản lý**, không phải bằng chứng.

**Khi nào nó gây nhầm lẫn?**
- Khi range được chọn **sau** khi giá chạy.
- Khi range nhỏ (M5/M15) được dùng để gọi "external" cho một sự kiện mà ở khung context chỉ là internal (lỗi CX6 trong [[20-Liquidity-Sweep]]).
- Khi range bị **re-map** sau displacement ([[37-Re-mapping-Dealing-Range-sau-Displacement]]) mà nhãn cũ bị sửa thay vì thêm nhãn mới.

---

### 13. Session Highs/Lows và các mức theo thời gian

![[Liquidity-v2-08-Session-Va-Muc-Thoi-Gian.svg|900]]

> [!example]- Hình 08 — đọc thế nào
> - **Đang diễn ra gì:** một ngày giao dịch trước (D-1) và các phiên Asia, London, NY AM của ngày hiện tại; một đường giá minh họa.
> - **Mức được đánh dấu:** PDH/PDL (biết lúc 17:00 NY), Asia H/L (biết lúc 00:00 NY), London H (biết lúc 05:00 NY), PWH (biết từ đóng cửa thứ Sáu).
> - **Timeframe:** trục thời gian theo giờ New York, kèm giờ Việt Nam (mùa hè Mỹ: VN = NY + 11h).
> - **Vì sao đáng chú ý:** mức theo thời gian chỉ **tồn tại** sau khi cửa sổ thời gian của nó đóng.
> - **Đã xác nhận:** trong kịch bản này Asia L bị xuyên trong London — đó là một sự kiện, phải phân loại bằng E-code.
> - **Chưa biết:** sự kiện đó có ý nghĩa gì cho DOL ngày.
> - **Làm gì tiếp:** cố định múi giờ, mốc đóng ngày, khung giờ phiên trong file cấu hình backtest.

**DEF-LQ-08 — Mức theo thời gian (quy ước vault, giờ New York)**

| Mức | Khoảng thời gian xác định | known_at | Khi nào có ý nghĩa | Khi nào kém phù hợp |
|---|---|---|---|---|
| **PDH / PDL** | Ngày giao dịch trước: FX 17:00→17:00 NY; NQ: phiên CME 18:00→17:00 ET | Đóng ngày (17:00) | Mốc chung trên mọi nền tảng; DOL trong ngày [ICT FRAMEWORK] | Ngày trước là ngày lễ/nửa phiên; feed CFD dùng giờ server khác |
| **PWH / PWL** | Tuần trước: mở cửa Chủ nhật → đóng cửa thứ Sáu | Đóng cửa thứ Sáu | DOL tuần; ERL cấp cao | Tuần có lễ lớn; tuần roll hợp đồng NQ |
| **Asia H / L** | **20:00–00:00 NY** (theo [[18-Kill-Zones]]) | 00:00 NY | Mốc của London/NY; hay gắn với Judas swing [ICT FRAMEWORK] | Asia range quá rộng (> 0.5·ATR(D1) — `asia_range_max_atr_d1`) hoặc có tin lớn trong phiên Á |
| **London H / L** | London KZ **02:00–05:00 NY** | 05:00 NY | Mốc cho NY AM | Khi London không có chuyển động (range quá hẹp) |
| **NY AM H / L** | 07:00–10:00 NY | 10:00 NY | Mốc cho phiên chiều / ngày sau | Ngày có tin 14:00 (FOMC) |

**Số tròn** (bội số 50/100 pip FX, 100/250 điểm NQ) **không** phải mức theo thời gian; nó có bằng chứng clustering riêng (Osler 2003). Nếu dùng: bật `round_numbers` trong file tham số (mục 51) trước khi backtest, mặc định Level 3, và cẩn thận đếm trùng khi nó trùng mức khác.

**Giờ Việt Nam:** Asia range 07:00–11:00 VN (mùa hè Mỹ) / 08:00–12:00 VN (mùa đông Mỹ); London KZ 13:00–16:00 / 14:00–17:00; NY AM 18:00–21:00 / 19:00–22:00. Năm 2026 Mỹ đổi về giờ mùa đông ngày Chủ nhật 01/11 — kiểm lại mỗi năm.

**Tránh chọn mức sau khi biết kết quả:**
1. Khung giờ phiên ghi trong file cấu hình, **không** đổi giữa chừng.
2. Không "dời" Asia range thêm một giờ vì "hôm nay London mở sớm".
3. Nếu một phiên có tin tier-1, đánh dấu cờ `news_in_window: true` thay vì loại bỏ phiên đó khỏi mẫu.

**Không mặc định mọi session high/low quan trọng như nhau.** Asia H/L là Level 3 theo mặc định; PDH/PDL Level 4; PWH/PWL Level 5. Thứ tự tầng pool trong ngày *"Asia H/L → London H/L → PDH/PDL → PWH/PWL"* là cách lập bản đồ, **không** phải trình tự giá bắt buộc phải đi.

---

### 14. Phân loại mức độ quan trọng của liquidity

**Bước 1 — Cổng bắt buộc (thiếu một = không vào danh sách)** — kế thừa [[20-Liquidity-Sweep]] §9.3:

| Cổng | Điều kiện | Lý do |
|---|---|---|
| **G1 Ex-ante** | Mức có known_at trước thời điểm quyết định | Không có G1 → hindsight |
| **G2 Xác nhận** | Swing theo DEF-LQ-05, EQH theo DEF-LQ-06, nhãn thời gian theo DEF-LQ-08, hoặc số tròn **nếu loại mức này đã được khai báo trước** (RULE-LQ-001; mặc định Level 3) | Mức "nhìn bằng mắt" không tái lập được |
| **G3 Chưa bị lấy** | Chưa có giao dịch vượt mức kể từ known_at | Mức đã bị lấy là chuyện khác |
| **G4 Đúng phía** | BSL trên giá hiện tại, SSL dưới | — |
| **G5 Không phải artifact** | Không phải gap rollover/DST, spike lỗi feed | Mức giả |

**Bước 2 — Cấp độ (Level 1–5)** — framework nghiên cứu của vault, không phải phân cấp chính thức của ICT:

| Level | Tên | Ví dụ điển hình | Vai trò thường gặp | Vào danh sách? |
|---|---|---|---|---|
| 5 | Major HTF | Swing D1/W1 lớn, PWH/PWL | DOL tuần/tháng | Có |
| 4 | External / dealing range | Biên range D1 context, PDH/PDL | DOL ngày; sweep "có nghĩa" | Có |
| 3 | Intermediate structural | Swing H1 cấu trúc; Asia/London H-L; EQH/EQL H1 | Mục tiêu trong ngày; nơi quan sát | Có |
| 2 | Internal | Swing H1 nhỏ bên trong range | Trung gian / inducement? | Chỉ khi gần mức cấp cao hoặc có vai trò cấu trúc |
| 1 | Micro | Fractal M1/M5 | Nhiễu | **Không** |

> [!example] DEF-LQ-09 — Significant liquidity (v0.1)
> Một mức là **significant** cho framework D1 → H1 → M5 khi: qua đủ **G1–G5** **và** đạt **Level ≥ 3**. Mức Level 2 chỉ được thêm khi nó trùng (≤ 0.10·ATR H1) với một mức Level ≥ 3 hoặc là protected high/low của cấu trúc H1. Mức M5 **không bao giờ** tự là significant.

**Bước 3 — Xếp hạng bằng lời (khi nhiều mức cùng phía):** khung cao hơn · là ERL của range D1 · trùng nhiều nhãn (PDH + EQH H1 = một cụm dày, **đếm là một**, không phải hai) · chưa bị test · cùng hướng cấu trúc HTF (nếu xét làm DOL). Phiên bản định lượng (LSS — Liquidity Significance Score, trọng số bằng nhau làm baseline, ước lượng ngoài mẫu) ở [[20-Liquidity-Sweep]] §9.3. **Không chọn trọng số bằng mắt.**

**Bước 4 — Giới hạn kích thước danh sách:** tối đa **3–4 mức mỗi phía** (6–8 tổng). Quá số đó → bỏ mức cấp thấp nhất. **[HEURISTIC]** (RULE-LQ-009) — mục đích là giữ chart đọc được (hình 33).

**Ba bước lọc khi cấu trúc dày đỉnh/đáy** (giữ từ note BSL cũ, chi tiết ở [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]]):
1. **Lọc hiệu lực** — "Nếu mức này bị phá (acceptance), cấu trúc có đổi không?" Không → chỉ là mức tồn kho, không đủ tư cách làm DOL.
2. **Gộp cụm** — các mức trong 0.10·ATR của nhau là **một** mức (một pool dày), không phải nhiều ứng viên.
3. **Xếp theo khung** — monthly > weekly > daily > London/NY session > Asia.

#### 14.1 Bảng so sánh các loại liquidity (yêu cầu §4.2 của protocol)

| Loại | Định nghĩa ngắn | Vị trí | Cách nhận diện | Bối cảnh khiến nó đáng chú ý | Quan hệ với structure | Vai trò | Làm giảm mức quan tâm | Hiểu lầm phổ biến |
|---|---|---|---|---|---|---|---|---|
| **BSL** | Lệnh mua có điều kiện trên đỉnh | Trên giá | Từ swing/EQH/nhãn thời gian | Đỉnh cấu trúc, ERL D1, PDH/PWH | Đỉnh bảo vệ cấu trúc giảm | DOL khi HTF tăng; nơi quan sát khi HTF giảm | Đã bị acceptance; Level ≤ 2 | "BSL = kháng cự", "chạm là bán" |
| **SSL** | Lệnh bán có điều kiện dưới đáy | Dưới giá | như trên | Đáy cấu trúc, ERL D1, PDL/PWL | Đáy bảo vệ cấu trúc tăng | Đối xứng BSL | như trên | "SSL = hỗ trợ", "chạm là mua" |
| **Swing H/L** | Đỉnh/đáy theo thuật toán | Bất kỳ | N-bar / DC θ | S, L, D, R, T cao | Là chính cấu trúc | Nguồn của BSL/SSL | Micro (Level 1) | "Mọi swing là liquidity" |
| **EQH/EQL** | Hai swing cùng khung gần bằng nhau | Bất kỳ | DEF-LQ-06 | Khung ≥ H1, có vai trò cấu trúc | Hay nằm ở biên range | Mục tiêu / inducement? | Dung sai nới; trộn khung | "EQH chắc chắn bị lấy", "EQH = engineered" |
| **Internal (IRL)** | Mức trong range R | Trong R | Theo R đã khai báo | Là swing cấp 3 / FVG lớn | Nhịp hồi trong cấu trúc | Mục tiêu trung gian | R chọn sau | "Internal không quan trọng" |
| **External (ERL)** | Mức ở/ngoài biên R | Biên R | Theo R | R là range D1 context | Phá = range mới | DOL mặc định | R quá nhỏ | Gọi "external" theo range M5 |
| **PDH/PDL, PWH/PWL** | Cực trị ngày/tuần trước | Bất kỳ | Theo giờ khai báo | Mốc chung mọi nền tảng | Có thể trùng swing | DOL ngày/tuần | Ngày lễ; feed lệch | "PDH luôn bị lấy trong ngày" |
| **Session H/L** | Cực trị phiên | Bất kỳ | Theo khung giờ | Range phiên sạch | Thường Level 3 | Mốc trong ngày | Phiên có tin; range rộng | "London luôn quét Asia" |

**Phân loại theo bản chất khái niệm:**
- **Khái niệm cơ bản** (định nghĩa được bằng hình học + thời gian): swing high/low, PDH/PDL, PWH/PWL, session H/L.
- **Phân loại theo bối cảnh** (cần một tham chiếu khác): BSL/SSL (cần giá hiện tại), internal/external (cần range), significant (cần cấp độ).
- **Cần quy tắc bổ sung để backtest được:** EQH/EQL (dung sai), "engineered", inducement, terminus/waypoint, DOL.

---
## PART III — STRUCTURAL CONTEXT

### 15. Liquidity và Market Structure

**Vì sao không thể nghiên cứu liquidity như những đường ngang rời rạc?** Vì giá trị phân tích của một mức đến từ **vai trò của swing tạo ra nó**:
- Swing high là điểm tham chiếu cho BSL; swing low cho SSL — nhưng một đáy nhỏ trong nhịp hồi và một protected low có cùng hình dạng, khác hẳn ý nghĩa.
- Một mức quan trọng ở H1 có thể chỉ là nhiễu ở D1, và một mức D1 có thể không "thấy" được trên M5 (nó nằm ngoài khung hình).

![[Liquidity-v2-06-Swing-5-Cap.svg|900]]

> [!example]- Hình 06 — đọc thế nào
> - **Đang diễn ra gì:** một đường giá chứa swing ở 5 cấp; vùng tô nhạt là range hiện tại (từ swing high L5 xuống swing low L4).
> - **Mức được đánh dấu:** L5 (major HTF), L4 (biên range), L3 (cấu trúc trung gian), L2 (nội bộ), L1 (micro).
> - **Timeframe:** minh họa đa khung trên một đường.
> - **Vì sao đáng chú ý:** cấp của swing quyết định nó có vào danh sách mức hay không.
> - **Đã xác nhận:** vị trí swing (sau khi xác nhận theo thuật toán).
> - **Chưa biết:** swing nào sẽ bị lấy trước.
> - **Làm gì tiếp:** với mỗi swing định đưa vào danh sách, trả lời 7 câu hỏi bên dưới bằng lời.

**Bảy câu hỏi đánh giá một swing (bằng lời, không cần điểm số):**

1. Nó thuộc **timeframe** nào (khung xác nhận)?
2. Nó có ý nghĩa gì với **cấu trúc** — bảo vệ xu hướng, làm biên range, hay chỉ là nhịp nhỏ?
3. Nó có đại diện cho một **vùng liquidity dễ nhận biết** không (EQH/EQL, trùng PDH, số tròn)?
4. Giá đã **phản ứng** quanh nó như thế nào (biên độ theo ATR, số lần test)?
5. Nó có liên quan đến một **chuyển động mạnh** hoặc một **structural break** không?
6. Nếu mức này **bị vượt qua với acceptance**, điều gì thay đổi trong cách đọc?
7. Nó còn **phù hợp với bối cảnh hiện tại** không (còn trong range context, chưa quá cũ, chưa bị re-map)?

![[Liquidity-v2-09-Liquidity-Va-Structure.svg|900]]

> [!example]- Hình 09 — đọc thế nào
> - **Đang diễn ra gì:** cấu trúc tăng trên H1 (H → HL → HH(BOS) → HL protected → HH range high), sau đó một nhịp hồi có swing nội bộ ih/il.
> - **Mức được đánh dấu:** BSL ngoài range high (L4), BSL trên ih (L2), SSL dưới il (L2), SSL dưới protected low (L3–4), SSL dưới range low (L4–5).
> - **Timeframe:** H1.
> - **Vì sao đáng chú ý:** năm đường ngang trông giống nhau; bị phá thì hậu quả rất khác nhau.
> - **Đã xác nhận:** cấu trúc tăng tới thời điểm hiện tại.
> - **Chưa biết:** nhịp hồi có dừng ở il/protected low hay không.
> - **Làm gì tiếp:** với mỗi mức, viết trước "nếu bị phá + acceptance thì câu chuyện đổi thế nào" (bảng bên phải hình).

> [!tip] Câu hỏi gốc của mục này
> **"Phá mức này có ĐỔI cách đọc không?"** — nếu không, mức đó không đủ tư cách làm DOL và không nên là nơi bạn tìm reversal.

---

### 16. Liquidity và Dealing Range

**Vì sao phải xác định range trước khi đánh giá internal/external?** Vì không có range thì không có "bên trong" hay "bên ngoài" (mục 11–12). Phương pháp chọn range — swing significance, thuật toán chọn, re-map — đã có trong [[12-Dealing-Range]] và [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]]; ở đây chỉ nhắc phần liên quan tới liquidity.

**Range được chọn dựa trên những swing nào?** Mặc định: cặp swing D1 (N = 3) gần nhất **bao quanh giá hiện tại**, mỗi swing có phản ứng ≥ **1.0 × ATR(14, D1)** **[HEURISTIC]**, trong đó **một đầu là điểm khởi phát của displacement gần nhất**. Sau khi chọn, hai biên được **gán Level 4** (Level 5 nếu đồng thời là swing W1). Ghi lý do chọn bằng một câu.

**Khi nào range lớn phù hợp hơn range nhỏ?**

| Mục đích | Range phù hợp | Lý do |
|---|---|---|
| Chọn DOL ngày / tuần | Range D1 context | DOL cần thứ bậc cao và tầm với ≤ 1–1.5 ATR D1 cho horizon 1–2 ngày |
| Theo dõi phản ứng trong phiên | Range H1 của nhịp hiện tại | Đủ chi tiết, vẫn có ý nghĩa cấu trúc |
| Ghi sự kiện M5 | Không dùng range M5 để gọi "external" | Tránh lỗi CX6 (internal bị nhầm là external) |

**Khi nào range cần được cập nhật?** Khi có **close + acceptance ngoài một biên** ở khung của range (D1 cho range D1) — range cũ thành lịch sử, range mới được khai báo **với ngày khai báo mới**. Không "kéo" biên cũ cho vừa giá.

**Sơ đồ — vị trí tương đối của các mức (ASCII):**

```text
        ── BSL ngoài range (ERL trên)  ─────────────────  ↑ external
   ════ Dealing Range High ════════════════════════════
        · · BSL nội bộ (IRL, swing H1)
                   PREMIUM
   ---- EQ 50% ----------------------------------------
                   DISCOUNT          ● giá hiện tại
        · · SSL nội bộ (IRL)   ▒▒ FVG chưa lấp (IRL) ▒▒
   ════ Dealing Range Low ═════════════════════════════
        ── SSL ngoài range (ERL dưới)  ─────────────────  ↓ external
```

> [!warning] Không chọn range vì nó làm câu chuyện hợp lý sau khi giá đã chạy
> Dấu hiệu bạn đang làm vậy: range được vẽ **sau** sự kiện; hai biên trùng "vừa khít" với điểm quay đầu; ngày khai báo range trống. Cách chặn: range ghi trong thẻ D1 trước phiên, có ngày.

---

### 17. Liquidity và Premium/Discount

![[Liquidity-v2-10-Premium-Discount.svg|900]]

> [!example]- Hình 10 — đọc thế nào
> - **Đang diễn ra gì:** trái là một dealing range chia Premium (trên EQ) và Discount (dưới EQ); phải là ba phản ví dụ.
> - **Mức được đánh dấu:** Range High/Low (ERL), EQ 50%.
> - **Timeframe:** range theo khung đã khai báo (thường D1).
> - **Vì sao đáng chú ý:** "ở Premium" không có nghĩa "sẽ giảm".
> - **Đã xác nhận:** vị trí tương đối của giá trong range đã chọn.
> - **Chưa biết:** giá có tôn trọng vị trí đó hay không.
> - **Làm gì tiếp:** dùng Premium/Discount để **tổ chức** việc theo dõi (BSL nào đáng theo dõi khi ở Premium), không dùng làm tín hiệu.

**[ICT FRAMEWORK]** Premium = nửa trên range (vùng "đắt" để mua, ưu tiên tìm bán theo ICT); Discount = nửa dưới. **[MATHEMATICAL]** Đó chỉ là vị trí tương đối: (giá − range low) / (range high − range low). Chọn range khác → vị trí khác.

**Vì sao vị trí không tự chứng minh đảo chiều:**
- **Ở Premium nhưng vẫn tăng:** giá chạy tiếp lấy BSL ngoài range và được chấp nhận → range mới; vị trí "đắt" trở thành Discount của range mới.
- **Ở Discount nhưng vẫn giảm:** "rẻ" không ngăn "rẻ hơn" — SSL ngoài range bị phá kèm acceptance.
- **Vị trí "đẹp" nhưng không phản ứng:** mức nằm đúng chỗ kỳ vọng nhưng giá lình xình rồi đi xuyên.

> [!important] Đừng đếm hai lần
> "Giá ở Premium" và "giá gần BSL range high" thường mô tả **cùng một thông tin** (giá ở gần biên trên). Trong checklist confluence, đó là **một** điểm, không phải hai. Tương tự: "SSL ở Discount" + "gần range low".

---

### 18. Liquidity và BOS/MSS

**Năm khái niệm, năm loại đối tượng — liên quan nhưng không đồng nhất:**

| Khái niệm | Loại đối tượng | Định nghĩa làm việc |
|---|---|---|
| **Liquidity (BSL/SSL)** | Mức (giả thuyết về vị trí lệnh) | DEF-LQ-02/03/04 |
| **BOS** | Sự kiện cấu trúc — phá swing theo hướng xu hướng | [[05-BOS-Break-of-Structure]] |
| **MSS** | Sự kiện cấu trúc — phá swing có ý nghĩa **ngược** hướng trước đó, thường kèm displacement | [[21-Market-Structure-Shift]] |
| **Displacement** | Tính chất của chuyển động | [[50-Displacement-In-Depth]] |
| **Liquidity sweep** | Sự kiện — xuyên mức đã liệt kê rồi bị phân xử là rejection | DEF-LS-04 |

**Năm tình huống bắt buộc** (mỗi tình huống: đã biết / chưa biết / quyết định tiếp):

| # | Tình huống | Đã biết | Chưa biết | Quyết định phân tích tiếp |
|---|---|---|---|---|
| 1 | **Sweep rồi MSS** (hình 15) | Mức đã liệt kê bị xuyên và rejection; swing có ý nghĩa ngược chiều bị phá | Giá có tới mục tiêu đối diện không | Ghi REVERSAL CONF.; mục tiêu là giả thuyết; vô hiệu khi close qua cực trị sweep |
| 2 | **Sweep nhưng không MSS** | Rejection đã xảy ra | Có dòng lệnh mới ngược chiều không | Trạng thái STALE sau m nến; không coi là reversal |
| 3 | **MSS mà không có sweep rõ** (hình 18) | Cấu trúc đổi | Mức đối diện còn nguyên có bị lấy không | Ghi `sweep_before_mss = false`; nhóm đối chứng — không ép thành sweep |
| 4 | **Phá swing nhỏ, cấu trúc lớn không đổi** | Swing Level 1–2 bị phá | Có lan lên khung cao không | Ghi sự kiện ở khung của swing; không đổi bối cảnh D1 (RULE-LQ-006) |
| 5 | **Vượt mức rồi đi tiếp cùng hướng** (hình 13; hình 16 nếu có sweep trước) | Acceptance | Đây là run hay chỉ một breakout | Kiểm tra mức kế cùng phía; trong RUN ACTIVE không tìm reversal |

> [!warning] Sweep → MSS không phải chuỗi bắt buộc
> Có ba nhóm quan sát được: **sweep + MSS**, **sweep không MSS**, **MSS không sweep**. Chỉ ghi nhóm đầu thì không đo được sweep đóng góp gì (ablation). Câu cũ *"reversal có chất lượng gần như luôn có sweep trước"* được hạ xuống thành **[HYPOTHESIS]** (Phụ lục C).

---

### 19. Liquidity và Displacement

**[ICT FRAMEWORK]** Displacement = chuyển động mạnh, một chiều, thường để lại FVG, được ICT diễn giải là dấu hiệu "tổ chức tham gia". **[OBSERVABLE]** phần đo được: thân nến lớn so với ATR, nhiều nến liên tiếp cùng chiều, phá swing, để lại khoảng trống giá.

**Displacement cung cấp thông tin gì sau một liquidity event?** Nó phân biệt hai trường hợp mà rejection đơn thuần không phân biệt được: (a) giá quay lại vì **không còn ai mua đuổi** (rejection thụ động) và (b) giá quay lại vì **có dòng lệnh mới ngược chiều** (rejection có lực). Đó là lý do DEF-LS-06 yêu cầu displacement + MSS làm lớp xác nhận. **[INTERPRETATION]**

**Khi nào "nến lớn" chỉ phản ánh volatility?** Khi cả thị trường đang giãn biên độ (tin tức, mở phiên): một nến 1.5·ATR trong 5 phút sau CPI không nói gì về "tổ chức" — nó nói biến động đã đổi thang. Định lượng: so với ATR **của cùng giờ trong các ngày trước**, không chỉ ATR(14) liên tục **[HEURISTIC]**.

**Displacement có bắt buộc sau mọi sweep không?** Không. Sweep là sự kiện; displacement là một tính chất có thể có hoặc không. Tách hai lớp để đo giá trị riêng.

**Displacement cũng có thể theo hướng xuyên:** một nến mạnh xuyên qua BSL rồi tiếp tục — đó là displacement **ủng hộ acceptance**, không phải reversal. Hỏi: displacement theo hướng nào so với mức?

---

### 20. Liquidity và POI

**Bốn thứ khác nhau, hay bị gộp:**

| | Là gì | Ví dụ |
|---|---|---|
| **Mức liquidity** | Một giá L phía bên kia có thể có lệnh có điều kiện | SSL dưới PDL |
| **POI (Point of Interest)** | Một **vùng** giá được kỳ vọng có phản ứng: OB, FVG, breaker… | Bullish FVG H1 ngay trên PDL |
| **Phản ứng giá** | Điều đã xảy ra tại vùng/mức | Wick dưới PDL, close lại trên |
| **Tín hiệu cấu trúc** | Sự kiện xác nhận thay đổi | MSS M5 sau phản ứng |

**[ICT FRAMEWORK]** Mô hình 2022 ghép chúng: giá tới **HTF POI** → **lấy liquidity** gần đó → **MSS + displacement** trên LTF → entry tại FVG. Việc mức liquidity nằm gần một OB/FVG **không đảm bảo** phản ứng; nó chỉ làm vùng đó đáng quan sát hơn **[HYPOTHESIS: HYP-LQ-004]**.

**Inducement trước POI** (giữ từ note 19 cũ, hạ nhãn): ICT mô tả một swing nhỏ ngay trước POI thật đóng vai "mồi" — giá quét nó, người vào sớm bị dừng lỗ, rồi giá đi sâu hơn vào POI rồi mới đảo ([[15-Inducement]]). Cách dùng an toàn:
1. Gắn nhãn `inducement?` cho swing đó **trước** khi giá tới.
2. Ghi khoảng cách từ swing đó tới mép POI (theo ATR).
3. Sau 30+ trường hợp, đếm xem tỷ lệ "quét inducement → đi tiếp vào POI" có khác "quét inducement → đảo luôn" không.
Không làm 3 bước này thì "inducement" là nhãn hậu kiểm cho mọi lần bạn bị dừng lỗ.

---

### 21. Phân biệt các khái niệm liên quan

![[Liquidity-v2-37-Lien-He-Khai-Niem.svg|900]]

> [!example]- Hình 37 — đọc thế nào
> - **Đang diễn ra gì:** một chuỗi giá đảo chiều tăng được dán 7 nhãn: mức liquidity, POI, sweep, displacement, FVG, MSS, DOL.
> - **Mức được đánh dấu:** SSL (1), vùng POI (2), DOL phía trên (7).
> - **Timeframe:** minh họa (có thể là M15).
> - **Vì sao đáng chú ý:** bảy nhãn thuộc năm loại đối tượng (mức / vùng / sự kiện / tính chất / mục tiêu).
> - **Đã xác nhận:** các sự kiện 3, 4, 5, 6 đã xảy ra trong hình.
> - **Chưa biết:** 7 (DOL) chỉ là giả thuyết.
> - **Làm gì tiếp:** khi chấm confluence, gom các nhãn cùng nguồn thông tin thành một biến.

**Mỗi khái niệm liên quan bổ sung gì cho liquidity?** (yêu cầu §10 của protocol)

| Khái niệm | Bổ sung thông tin gì | Trùng lặp với | Hữu ích khi | Không cần khi | Cần backtest gì nếu dùng làm bộ lọc |
|---|---|---|---|---|---|
| **POI** (OB/FVG) | Nơi phản ứng có thể mạnh hơn | Vị trí premium/discount | Chọn mức nào để theo dõi sát | Mức đã là ERL D1 rõ | Tỷ lệ rejection tại mức trong POI vs ngoài POI (HYP-LQ-004) |
| **Displacement** | Có dòng lệnh mới ngược chiều? | MSS, FVG (cùng một nến) | Phân biệt rejection có lực / thụ động | Đã yêu cầu MSS có thân lớn | Ablation: sweep+MSS có/không displacement |
| **FVG** | Dấu vết của displacement; vùng entry | Displacement | Chọn vùng vào lệnh | Chỉ phân loại sự kiện | Tỷ lệ fill, MFE sau fill |
| **MSS** | Cấu trúc LTF đã đổi | Displacement | Xác nhận sau rejection | Khi đang RUN ACTIVE ngược hướng H1 | Nhóm sweep+MSS vs MSS không sweep |
| **Premium/Discount** | Vị trí tương đối | Gần ERL | Lọc phía nào đáng theo dõi | Range chưa khai báo | Rejection rate theo vị trí trong range |
| **Kill Zone / phiên** | Khi nào dòng lệnh đủ dày | — | Lọc thời điểm quan sát | Sự kiện D1 | Kết quả theo phiên (HYP-LQ-006) |
| **SMT** | Phân kỳ giữa tài sản tương quan | — | Phá thế hòa giữa hai kịch bản | Mặc định | Likelihood ratio (HYP-LS-014) |

**Liquidity và thời gian giao dịch (§10.6 của protocol).** Session H/L là **mức**; kill zone là **cửa sổ thời gian** quan sát. Không mặc định một kill zone là điều kiện bắt buộc của mọi liquidity event — sự kiện D1 không quan tâm kill zone. Kill zone được dùng như **bộ lọc vận hành** cho M5 (khi nào mở M5) và như **biến** trong backtest. Bằng chứng gián tiếp hợp lý: phiên có thanh khoản dày → giá ít "nhảy" qua mức do lệnh lẻ. **[INTERPRETATION]**

**Ba khung lý thuyết khác mô tả cùng lớp hiện tượng** (giữ từ note 07/30 cũ):

| Khung | Khái niệm tương đương | Giống ICT ở đâu | Khác ICT ở đâu |
|---|---|---|---|
| **Wyckoff** | Spring (thủng hỗ trợ rồi hồi) ≈ sweep SSL; Upthrust/UTAD ≈ sweep BSL | Cùng hành vi "thử biên rồi bị từ chối" | Nhấn mạnh giai đoạn tích lũy/phân phối và volume |
| **Auction Market Theory** | Excess / failed auction ngoài value area | Giá thăm dò ra ngoài, thiếu chấp nhận thì quay về | Đo bằng volume profile/TPO; không cần giả định ý định |
| **Order flow / footprint** | Absorption, delta divergence tại mức | Lệnh lớn hấp thụ dòng lệnh đối diện | Đo trực tiếp bằng dữ liệu khớp lệnh; ICT suy luận gián tiếp |

> [!note] Hệ quả
> Ba bộ từ vựng, một lớp hiện tượng. Chọn bộ từ vựng không đổi hành vi giá — nhưng đổi **cách kiểm chứng**. AMT và footprint ít bị phê phán falsifiability hơn vì không cần giả định ý định của người tham gia.

---
## PART IV — LIQUIDITY EVENTS

> [!important] Ba thuật ngữ không được dùng thay nhau
> **Sweep** = một mức bị xuyên rồi **quay lại** (rejection). **Run** = nhiều mức cùng phía bị xuyên và **được chấp nhận**. **Breakout** = một mức bị xuyên và **được chấp nhận** (acceptance). Khác nhau ở **cách phân xử** và **số mức**, không ở cảm giác "mạnh/yếu".

### 22. Liquidity Sweep

**T1.** Bạn thò tay qua hàng rào nhà hàng xóm để nhặt quả bóng, rồi rút tay về. Tay đã **qua** hàng rào — nhưng bạn **không ở lại** bên đó.

**T2 — Chuỗi giá, biết gì ở từng thời điểm:**

| Thời điểm | Diễn biến [OBSERVABLE] | Biết | Chưa biết |
|---|---|---|---|
| t₀ | Đỉnh 1.0920 (H1) được xác nhận, vào danh sách | Mức L = 1.0920 | Giá có tới không |
| t₁ | Giá tới 1.0915 | Giá đang tiến tới L | Có xuyên không |
| t₂ (đang chạy) | High nến M5 = 1.0927 | L đã bị xuyên (PENETRATED) | Close ở đâu |
| t₃ (close nến) | Close 1.0911 (< L − δ) | **Rejection** → nhãn SWEEP | Có MSS không; có đảo chiều không |
| t₄ | Close dưới swing low M5 cấp 2 | Xác nhận lớp 2 (MSS) | Mục tiêu đối diện có bị chạm không |

**T3 — ICT.** ICT dùng *sweep*, *raid*, *stop run*, *stop hunt*, *liquidity grab* gần như thay nhau cho hiện tượng "giá lấy liquidity phía trên đỉnh/dưới đáy rồi quay lại". Hình mẫu gốc là **Turtle Soup** — chiến lược "đánh ngược cú phá đỉnh/đáy 20 ngày thất bại" của Linda Raschke & Larry Connors trong *Street Smarts* (1995) — ICT dùng lại tên này ([[33-Turtle-Soup]]). **[ICT FRAMEWORK]**

**Các cách định nghĩa phổ biến — và cái note này chọn:**

| Phiên bản | Điều kiện | Ưu | Nhược |
|---|---|---|---|
| A. Chỉ cần wick | High > L, close < L (cùng nến) | Đơn giản, biết sớm | Bỏ sót trường hợp close vượt rồi quay lại nến sau; nhạy nhiễu |
| B. Close quay lại trong k nến (**DEF-LS-04**) | High > L + ε; trong k nến có close < L − δ, trước khi có acceptance | Bao cả E2 và E3; có thời điểm biết rõ; tách khỏi xác nhận | Có tham số (ε, δ, k) |
| C. Close quay lại + displacement | B + nến quay lại có thân lớn | Gần với cách ICT "cảm" | Trộn sự kiện với xác nhận → không đo được giá trị riêng của displacement |

**Chọn B** cho bản nghiên cứu đầu tiên. Quy ước của bạn trong memory (*"wick qua mức là sweep hợp lệ, không phải invalidation; invalidation = close bên kia và giữ 2–3 nến"*) **tương thích** với B: wick + close lại = E2; close bên kia nhưng không đủ acceptance rồi quay lại = E3; giữ 2 close = acceptance (E4).

> [!example] DEF-LQ-11 = DEF-LS-04 — Liquidity Sweep (v0.1, HEURISTIC)
> Cho mức **L** trong danh sách (known_at < t₀), BSL (SSL đối xứng). Gọi **j** là nến đầu tiên có `high_j > L + ε`.
> - **SWEEP** nếu ∃ t ∈ [j, j + k]: `close_t < L − δ`, **và** trước t **không có acceptance** (không có 2 close liên tiếp > L, không có close > L + 0.5·ATR).
> - **known_at của nhãn** = close nến t. **Cực trị sweep** = max(high) từ j tới t. **Độ sâu** = (cực trị − L)/ATR. **Thời gian bên kia** = t − j.
> - Cửa sổ phân xử = **nến j và k nến sau đó** (j … j + k; với k = 3 là tối đa 4 close). Hết j + k chưa phân xử → **EXPIRED** (không phải sweep).
> - Mặc định M5–M15: **ε = 0.02·ATR** (hoặc 1 tick), **δ = 0.25·ATR**, **k = 3**. Khai báo trước khi backtest.

![[Liquidity-v2-12-Giai-Phau-Sweep.svg|900]]

> [!example]- Hình 12 — đọc thế nào
> - **Đang diễn ra gì:** giá M15 tiến lên BSL L; nến j xuyên L+ε bằng wick và close dưới L−δ ngay trong nến đó (E2); hai nến sau phá swing low nội bộ, để lại FVG.
> - **Mức được đánh dấu:** L (swing H1 đã có trong danh sách trước phiên), L+ε, L−δ, swing low nội bộ.
> - **Timeframe:** M15 quan sát một mức H1.
> - **Vì sao đáng chú ý:** cho thấy nhãn SWEEP có thời điểm biết chính xác (close nến j) và tách khỏi lớp xác nhận (MSS + displacement).
> - **Đã xác nhận:** sự kiện SWEEP (E2); sau đó là MSS (nếu swing low nội bộ là Level ≥ 2).
> - **Chưa biết:** kết quả — giá có tới mục tiêu đối diện không.
> - **Làm gì tiếp:** ghi E-code, known_at, độ sâu, thời gian bên kia; chờ m nến cho xác nhận; nếu không → STALE.

**Tại sao phải biết mức TRƯỚC khi giá chạm?** Vì nếu chọn mức sau, mọi cú quay đầu đều "là sweep của một cái gì đó" (mục 3.4). Mức ngoài danh sách bị xuyên → **unlisted breach**.

**Tại thời điểm giá vừa vượt mức, những gì CHƯA thể kết luận:**
- Đây là sweep hay breakout (hình 14 — hai kịch bản giống hệt nhau tại close nến j).
- Có ai "hấp thụ" không, ai.
- Giá có đảo chiều không.
- Mức đã "hết liquidity" chưa (lệnh sâu hơn có thể vẫn còn).

![[Liquidity-v2-14-Sweep-vs-Breakout-Cung-Diem-Dau.svg|900]]

> [!example]- Hình 14 — đọc thế nào
> - **Đang diễn ra gì:** hai kịch bản dùng chung 9 nến đầu; nến j high vượt L, close trên L (chưa đủ acceptance → PENDING). Kịch bản 1 quay lại dưới L−δ (E3); kịch bản 2 có close thứ hai trên L (E4).
> - **Mức được đánh dấu:** L.
> - **Timeframe:** bất kỳ (minh họa).
> - **Vì sao đáng chú ý:** không có quy tắc **một nến** nào phân biệt sweep với breakout.
> - **Đã xác nhận:** tại close nến j — chỉ là "đã xuyên".
> - **Chưa biết:** mọi thứ còn lại, cho tới hết cửa sổ k.
> - **Làm gì tiếp:** không hành động trên nhãn chưa có; đợi phân xử (RULE-LS-002).

---

### 23. Liquidity Run

**[ICT FRAMEWORK]** Trong cách dùng của ICT, *liquidity run* chỉ việc giá **đi qua lần lượt nhiều mức liquidity cùng phía** — lấy mức này, hồi nông, lấy mức kế — thường trong một xu hướng hoặc một đợt expansion. ICT còn phân biệt **Low-Resistance Liquidity Run (LRLR)** — đường đi có chuỗi mức cùng chiều và không có PD array ngược chiều chặn — và **High-Resistance (HRLR)** — đường đi bị chặn bởi FVG/OB ngược chiều chưa xử lý. **[ICT FRAMEWORK]**; "LRLR chạy nhanh hơn, ít pullback sâu hơn" là **[HYPOTHESIS]** (đo: thời gian và độ sâu pullback giữa các mức).

> [!example] DEF-LQ-12 = DEF-LS-05 — Liquidity Run (v0.1, HEURISTIC)
> Run lên (run xuống đối xứng): chuỗi mức ex-ante L₁ < L₂ < … < Lₙ (n ≥ 2, cùng phía BSL) sao cho
> 1. mỗi Lᵢ bị xuyên theo thứ tự và được phân xử bằng **acceptance** trước khi Lᵢ₊₁ bị xuyên;
> 2. nhịp hồi giữa hai lần lấy < **50%** leg trước đó;
> 3. không có sự kiện cấu trúc ngược chiều ở khung của run;
> 4. **known_at của nhãn "run"** = close nến xác nhận acceptance tại **L₂** — run không tồn tại khi mới có một mức.
> **Run kết thúc** (DEF-LS-07): rejection ở mức kế tiếp (một sweep), MSS ngược ở khung run, hoặc hết cửa sổ khai báo.

![[Liquidity-v2-13-Liquidity-Run.svg|900]]

> [!example]- Hình 13 — đọc thế nào
> - **Đang diễn ra gì:** giá lấy L₁, L₂, L₃ lần lượt với 2 close phía trên mỗi mức và nhịp hồi nông; tại L₄ giá xuyên rồi close lại dưới.
> - **Mức được đánh dấu:** L₁…L₄ — các swing high cũ đã có trong danh sách.
> - **Timeframe:** minh họa (thường H1 cho run, M5–M15 để thấy chi tiết).
> - **Vì sao đáng chú ý:** nhãn RUN chỉ có từ L₂; RUN kết thúc bằng một sweep tại mức cuối.
> - **Đã xác nhận:** E4 tại L₁, L₂, L₃; rejection tại L₄.
> - **Chưa biết:** rejection tại L₄ có dẫn tới đảo chiều không — vẫn cần lớp xác nhận.
> - **Làm gì tiếp:** trong RUN ACTIVE không tìm reversal ở từng mức nhỏ (RULE-LS-005); sau RUN ENDED mới xét kịch bản đảo chiều.

**Trường hợp giá vượt một vùng liquidity rồi tiếp tục cùng hướng** không phải "sweep thất bại" theo nghĩa chung chung — nó là **acceptance**, và nếu mức kế tiếp cũng được chấp nhận, là **run**. Nếu trước đó đã có nhãn sweep (rejection) rồi giá quay lại xuyên với acceptance, đó là **chuyển trạng thái S1** (sweep → run, nếu mức kế cũng được chấp nhận): thêm dòng "rejection failed", không xóa nhãn cũ.

---

### 24. Breakout

**Theo phân tích kỹ thuật thông thường:** breakout = giá vượt một mức hỗ trợ/kháng cự và được kỳ vọng tiếp tục theo hướng phá.

**Một sự kiện, hai cách mô tả:** giá vượt một swing high với acceptance có thể **đồng thời** được gọi là *structural breakout / BOS* (nếu swing đó là cấu trúc) và *"BSL đã bị lấy"* (ngôn ngữ ICT). Không mâu thuẫn — hai nhãn trả lời hai câu hỏi khác nhau (cấu trúc đổi chưa? / mức đã bị giao dịch qua chưa?).

> [!example] DEF-LQ-13 — Breakout / Acceptance (= mã E4)
> Sau khi xuyên L: **≥ 2 close liên tiếp** bên kia L, **hoặc** 1 close cách L > 0.5·ATR, trước khi có rejection. known_at = close nến thỏa điều kiện.

**Chỉ thấy giá vượt mức là chưa đủ.** Cần quan sát thêm để phân biệt các kịch bản:
- **Close** ở đâu và **bao nhiêu nến** liên tiếp (định nghĩa E3 vs E4);
- **Retest** từ phía bên kia có giữ được không;
- **Displacement theo hướng nào**;
- Bối cảnh **HTF** (đang RUN cùng phía? mức là waypoint hay ERL?).

> [!warning] Không ép một lần vượt mức vào một nhãn duy nhất
> Nếu định nghĩa đang dùng không cho phép phân biệt (ví dụ hết k nến mà chưa có close nào thỏa), nhãn đúng là **EXPIRED/UNDETERMINED** — không phải "chắc là sweep" hay "chắc là breakout".

---

### 25. Phản ứng sau khi vượt liquidity — bốn tình huống bắt buộc

> [!example] DEF-LQ-15 — Post-liquidity reaction (các biến đo, v0.1)
> Tính trong cửa sổ **W nến** sau known_at của nhãn (W khai báo trước, ví dụ W = 48 nến M5 = 4 giờ):
> - **MFE / MAE** (theo ATR) tính từ close nến phân xử;
> - **Thời gian quay lại L** (nếu có); **thời gian tới mức đối diện**;
> - **Mức nào bị chạm trước**: mục tiêu đối diện hay cực trị sweep (+ buffer);
> - **Có MSS (Level ≥ 2) + displacement trong m nến** không (DEF-LS-06);
> - Mọi biến so với **baseline** cùng khoảng cách.

#### Case A — Sweep rồi đảo chiều

![[Liquidity-v2-15-Case-A-Sweep-Roi-Dao-Chieu.svg|900]]

> [!example]- Hình 15 — đọc thế nào
> - **Đang diễn ra gì:** giá tiến lên PDH; T2 nến close trên PDH (PENDING); T3 close lại dưới PDH−δ (SWEEP, E3); T4 phá swing low nội bộ với thân lớn (REVERSAL CONF.); T5 (ex-post) giá giảm tiếp.
> - **Mức được đánh dấu:** PDH (BSL, có trong danh sách trước phiên); swing low nội bộ M5; SSL đối diện.
> - **Timeframe:** M5 quan sát mức D1.
> - **Vì sao đáng chú ý:** đây là diễn biến "đẹp" nhất — và vì đẹp nên dễ được nhớ quá mức.
> - **Đã xác nhận:** SWEEP tại T3; xác nhận tại T4.
> - **Chưa biết:** tại T2–T4: giá có tới SSL đối diện không, có quay lại lấy cực trị sweep không.
> - **Làm gì tiếp:** ghi cả những lần T3 xảy ra mà T5 thất bại — chúng là mẫu số.

```text
Thứ tự sự kiện (BSL):  T0 mức trong danh sách → T1 giá tiến tới → T2 xuyên, close trên L (PENDING)
→ T3 close < L − δ trong k nến (SWEEP, E3) → T4 MSS + displacement (REVERSAL CONF.) → T5 kết quả (ex-post)
```

| | Nội dung |
|---|---|
| **Nhận định ban đầu (T0–T1)** | PDH là ứng viên BSL; bối cảnh D1 giảm/giá ở premium → PDH là nơi đáng quan sát |
| **Đã xác nhận** | T3: SWEEP. T4: MSS M5 Level 2 + displacement |
| **Chưa xác nhận** | Đảo chiều có tiếp diễn tới mục tiêu không |
| **Điều kiện tiếp tục theo dõi** | Giá ở dưới cực trị sweep; không có 2 close trên PDH |
| **Điều kiện hủy giả thuyết giảm** | Close vượt cực trị sweep, hoặc 2 close liên tiếp trên PDH (acceptance) |

#### Case B — Sweep (rejection) nhưng giá tiếp tục tăng

![[Liquidity-v2-16-Case-B-Sweep-Roi-Tiep-Dien.svg|900]]

> [!example]- Hình 16 — đọc thế nào
> - **Đang diễn ra gì:** T3 có rejection đúng định nghĩa (SWEEP, E3); T4 giá quay lại đóng trên L hai lần (acceptance) và đi tiếp tới BSL kế.
> - **Mức được đánh dấu:** L₁ (swing H1 cũ), L₂ (BSL kế tiếp).
> - **Timeframe:** M5 hoặc M15.
> - **Vì sao đáng chú ý:** một sweep theo định nghĩa không hứa hẹn đảo chiều.
> - **Đã xác nhận:** SWEEP tại T3 (đúng tại thời điểm đó); acceptance tại T4.
> - **Chưa biết:** L₂ có được chấp nhận không (để thành RUN).
> - **Làm gì tiếp:** thêm dòng "rejection failed" — **không** sửa nhãn T3.

| | Nội dung |
|---|---|
| **Nhận định ban đầu** | L₁ là BSL; quan sát phản ứng |
| **Đã xác nhận** | T3 SWEEP; T4 acceptance → ghi "rejection failed"; nếu L₂ cũng được chấp nhận → **S1** (sweep → run) |
| **Chưa xác nhận** | Run có tiếp diễn qua L₂ không |
| **Theo dõi tiếp** | Phản ứng tại L₂; trạng thái cấu trúc H1 |
| **Hủy giả thuyết tăng tiếp** | Rejection tại L₂ + MSS ngược ở khung run |

**Vì sao không gọi Case B là "tín hiệu đảo chiều thất bại" chung chung?** Vì "tín hiệu đảo chiều" chưa bao giờ được định nghĩa ở đây — sweep là **sự kiện**, đảo chiều là **giả thuyết** cần lớp xác nhận. Gọi đúng: "sweep tại T3, acceptance tại T4". Case B là dữ liệu quan trọng nhất để đo xem bộ lọc (MSS + displacement + bối cảnh HTF) có giá trị không.

#### Case C — Giá chạm liquidity nhưng không xuyên qua

![[Liquidity-v2-17-Case-C-Cham-Khong-Xuyen.svg|900]]

> [!example]- Hình 17 — đọc thế nào
> - **Đang diễn ra gì:** giá tiến lên EQH H1, high thiếu vài tick so với L+ε, rồi giảm.
> - **Mức được đánh dấu:** L (EQH H1) và dải ε.
> - **Timeframe:** M15.
> - **Vì sao đáng chú ý:** nhiều người gọi đây là "sweep yếu" khi giá sau đó giảm — đó là đổi định nghĩa theo kết quả.
> - **Đã xác nhận:** E1 (chạm trong ε) hoặc E0 (near-miss); mức chưa bị giao dịch qua.
> - **Chưa biết:** mức có giữ được lần sau không; "front-run" chỉ là diễn giải.
> - **Làm gì tiếp:** giữ mức trong danh sách (G3 vẫn đúng), tăng biến N (số lần test).

| | Nội dung |
|---|---|
| **Biết** | Lần này mức chưa bị giao dịch qua |
| **Không được kết luận** | "Liquidity đã bị lấy" (sai định nghĩa); "mức sẽ giữ" (chưa có cơ sở); "ai đó front-run" (diễn giải) |
| **Theo dõi tiếp** | Mức vẫn active; ghi N |
| **Cập nhật khi** | Giá quay lại xuyên L → phân xử mới; hoặc cấu trúc đổi làm mức mất vai trò |

#### Case D — Giá phá cấu trúc nhưng không có sweep rõ ràng

![[Liquidity-v2-18-Case-D-MSS-Khong-Sweep.svg|900]]

> [!example]- Hình 18 — đọc thế nào
> - **Đang diễn ra gì:** giá tạo lower high dưới PDH (không chạm), rồi close dưới swing low H1 với thân lớn (MSS giảm).
> - **Mức được đánh dấu:** PDH (chưa bị chạm), swing low H1.
> - **Timeframe:** H1/M15.
> - **Vì sao đáng chú ý:** sự kiện này **không** khớp mô hình "sweep → MSS" — và không cần khớp.
> - **Đã xác nhận:** MSS (theo định nghĩa MSS của vault); `sweep_before_mss = false`.
> - **Chưa biết:** BSL phía trên còn nguyên có bị quay lại lấy không (rủi ro cho kịch bản giảm).
> - **Làm gì tiếp:** ghi vào nhóm "MSS không sweep" để so sánh với nhóm "sweep + MSS".

| | Nội dung |
|---|---|
| **Biết** | Cấu trúc H1 đổi; mức liệt kê phía trên chưa bị chạm |
| **Không được làm** | Tìm một wick M1 bất kỳ rồi gọi là "sweep" để hợp thức hóa |
| **Theo dõi tiếp** | Khoảng cách tới BSL còn nguyên (đối thủ gần?) |
| **Biến cần ghi** | `sweep_before_mss`, khoảng cách tới mức chưa quét gần nhất phía sau stop (điều kiện loại trừ DOL-D1 của bộ quy tắc DOL v0.2 — không phải khung D1 / [[13-Mistake-Trading-Into-Unswept-Liquidity]]) |

---

### 26. Những trường hợp không đủ điều kiện phân loại

> [!example] DEF-LQ-10 — Liquidity event (v0.1)
> Một tương tác giữa giá và một mức **L có trong danh sách** (qua G1), được gán **đúng một** mã E0–E9 / PND / EXP theo bảng dưới; known_at = thời điểm biết sớm nhất của mã đó. Tương tác với mức **ngoài** danh sách = *unlisted breach* (ghi lại, không phân loại như liquidity event).

**Bảng mã sự kiện đầy đủ** (taxonomy E0–E9 của [[20-Liquidity-Sweep]] §7.2, viết cho BSL; SSL đối xứng):

| Mã | Tên | Điều kiện quan sát | Thời điểm biết sớm nhất | Gọi là |
|---|---|---|---|---|
| **E0** | Near-miss | max(high) < L − ε, rồi giá rời đi ≥ 0.5·ATR (`near_miss_exit_atr`) | Khi giá rời đủ xa | "chưa lấy" |
| **E1** | Chạm | \|high − L\| ≤ ε, close < L | Close nến chạm | test |
| **E2** | Xuyên bằng wick → rejection | high > L + ε, close nến đó < L − δ | Close nến xuyên | **sweep** |
| **E3** | Close chưa phân xử → quay lại | close nến xuyên ≥ L − δ (chưa rejection, chưa acceptance — gồm cả close > L), rồi close < L − δ trong k nến | Close nến quay lại | **sweep** (failed breakout) |
| **E4** | Acceptance | ≥ 2 close liên tiếp > L, hoặc 1 close > L + 0.5·ATR | Close nến thỏa | breakout / BOS |
| **E5** | Nhảy gap qua mức | Open phiên mới đã ở bên kia L | Open phiên | "lấy mức không có giao dịch tại L" |
| **E6** | Thọc nhiều lần | ≥ 2 lần high > L, mỗi lần close < L, trong một cửa sổ | Close lần thứ hai | multi-poke |
| **E7** | Run | DEF-LS-05 | Acceptance tại L₂ | liquidity run |
| **E8** | Hai phía | Cả mức trên và mức dưới bị xuyên trong cùng phiên | Khi phía thứ hai bị xuyên | expansion, "quét hai đầu" |
| **E9** | Run thất bại | Run rồi rejection ở Lₙ₊₁ và close lại dưới Lₙ | Close dưới Lₙ | run gãy |
| **PND / EXP** | Chưa phân xử / hết hạn | Sau xuyên chưa thỏa E2/E3/E4 trong k nến | Close nến j + k | — |

**Các trường hợp phải giữ "chưa xác định":**

| Trường hợp | Vì sao không phân loại được | Ghi thế nào |
|---|---|---|
| Hết k nến, giá lình xình quanh L | Không thỏa rejection lẫn acceptance | `EXPIRED` + mô tả |
| Gap qua mức (cuối tuần, mở phiên) | Không có giao dịch hai chiều tại L | `E5`, tách khỏi nhóm sweep |
| Spike tin tier-1 xuyên nhiều mức trong một nến | Thang biến động đổi; spread giãn | `news_spike`, vẽ lại danh sách sau tin |
| Feed broker và sàn gốc lệch ở đúng mức | Một feed xuyên, một feed chưa | Ghi theo feed chuẩn; cờ `feed_conflict` |
| Mức không có trong danh sách | Không qua G1 | `unlisted breach` |
| Quét cả hai đầu không MSS | Không có thông tin hướng | `E8`, DOL "chưa rõ" |

![[Liquidity-v2-36-Vong-Doi-Muc-Liquidity.svg|900]]

> [!example]- Hình 36 — đọc thế nào
> - **Đang diễn ra gì:** vòng đời một mức L: hình thành → xác nhận → vào danh sách → được test (2 lần) → bị xuyên rồi close lại dưới L − δ ngay trong nến đó (E2) → cực trị của cú xuyên thành mức mới L', về sau L' cũng bị lấy.
> - **Mức được đánh dấu:** L và L'.
> - **Timeframe:** minh họa.
> - **Vì sao đáng chú ý:** mức giá và lệnh là hai thứ khác nhau — mức còn trên chart khi lệnh đã khớp/hủy; cực trị cú quét có thể là nơi lệnh mới dồn lại.
> - **Đã xác nhận:** chuỗi sự kiện trên hình.
> - **Chưa biết:** số lần test làm mức mạnh lên hay yếu đi (dấu của biến N) — cần đo.
> - **Làm gì tiếp:** sau sweep, thêm L' vào danh sách với known_at = close nến phân xử; stop đặt sát L' cần buffer.

---

### 27. Cách cập nhật nhận định theo diễn biến thực tế

**Năm quy tắc cập nhật:**

1. **Append-only.** Thông tin mới = dòng mới. Không sửa nhãn cũ, không xóa dự đoán sai (RULE-LQ-010).
2. **Cập nhật theo sự kiện, không theo cảm giác.** Chỉ đổi nhận định khi có một **sự kiện đã phân loại** (E-code) hoặc một **sự kiện cấu trúc** ở khung có thẩm quyền.
3. **Khung nào đổi khung đó.** Sự kiện M5 đổi trạng thái M5; sự kiện H1 đổi trạng thái H1; chỉ sự kiện D1 (close D1 + acceptance qua mức trong "điều kiện đánh giá lại") mới đổi bản đồ D1 (RULE-LQ-006).
4. **Gạch mức đã tiêu, thêm mức mới.** Sau E4: mức cũ "spent". Sau E2/E3: thêm cực trị sweep L'. Sau run: mức cuối bị rejection là ứng viên quan sát.
5. **DOL đổi trạng thái có lý do và giờ** (mục 32): projected → active → delivered → spent, hoặc invalidated → flip.

**Ba chuyển trạng thái giữa sweep và run** ([[20-Liquidity-Sweep]] §6.5):

| Mã | Chuyển | Khi nào | Hệ quả |
|---|---|---|---|
| **S1** | Sweep → Run | Rejection rồi giá quay lại xuyên với acceptance và lấy tiếp mức kế | Nhãn sweep giữ nguyên; thêm "rejection failed"; bối cảnh = run |
| **S2** | Sweep phía này → Run phía kia | Sweep BSL, sau đó chuỗi acceptance qua các SSL | Đảo chiều thành công theo nghĩa cấu trúc |
| **S3** | Run → Sweep | Run kết thúc bằng rejection ở mức kế | Mức đó thành ứng viên quan sát đảo chiều — cần xác nhận |

---
## PART V — DRAW ON LIQUIDITY (DOL)

> [!info] Phạm vi của Part V
> Đây là phần DOL **cần cho note gốc Liquidity**. Bộ quy tắc DOL v0.2 đầy đủ (R1–R5, S1–S5, D1–D6, tier A/B/C, quản lý lệnh), cơ chế, 6 ví dụ, 8 bẫy và thiết kế backtest DOL nằm ở [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]. Ontology và failure model: [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]]. SOP đầu ngày: [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]. Part V **không** đặt quy tắc DOL mới mâu thuẫn với v0.2.

### 28. DOL là gì?

**T1.** Trên bản đồ có nhiều thành phố (các mức liquidity). DOL là **thành phố bạn đoán chiếc xe đang hướng tới** — kèm theo thành phố thay thế, thời hạn, và dấu hiệu cho thấy bạn đoán sai.

**T3 — ICT.** *Draw on Liquidity* là mức liquidity mà giá được mô tả là "bị hút" về — mục tiêu của price delivery trong một horizon. **[ICT FRAMEWORK]** Trong ngôn ngữ của vault, "hút" được dịch thành **xác suất được chạm trước đối thủ trong horizon** — một mệnh đề đo được.

**DOL khác BSL/SSL thế nào?**

| | BSL / SSL | DOL |
|---|---|---|
| Loại đối tượng | Mức tồn tại trên chart (có thể có nhiều) | **Một giả thuyết** chọn ra từ các mức đó |
| Số lượng | Nhiều mỗi phía | Một DOL chính + một thay thế + một đối thủ |
| Có thời hạn? | Không (đến khi bị lấy/hết vai trò) | **Có** — horizon |
| Có điều kiện sai? | Không | **Có** — invalidation |
| Có trạng thái? | listed / tested / spent | projected / active / delivered / spent / invalidated / flip |

**Một mức liquidity có phải lúc nào cũng là DOL hiện tại?** Không. Phần lớn mức trong danh sách **không** phải DOL — chúng là đối thủ, trạm trung chuyển (waypoint), hoặc nơi quan sát phản ứng.

> [!example] DEF-LQ-14 — DOL (v0.1, tương thích bộ quy tắc DOL v0.2)
> Một **thẻ DOL** hợp lệ phải có, **khóa trước giờ quyết định**:
> 1. **Range D1 đã chốt** (R1);
> 2. **Mức DOL**: một mức (hoặc cụm) **chưa tiêu**, Level ≥ 4, ở khung ≥ khung xác định bias (R2);
> 3. **Đối thủ** (mức phía đối diện mà nếu bị **chạm trước** thì thẻ DOL được chấm **SAI** theo metric first-touch), **horizon**, **invalidation** (R3);
>    - **Đối thủ ≠ mức quan sát.** Một mức gần ở phía đối diện mà bạn **kỳ vọng có thể bị quét** trước khi giá đi về DOL (ví dụ SSL dưới HL D1 trong bối cảnh tăng) phải được ghi là **mức quan sát** (`terminus?`), **không** phải đối thủ. Sweep (E2/E3) tại mức quan sát không làm thẻ sai; **acceptance (E4)** tại đó thường chính là điều kiện vô hiệu.
> 4. **Trong tầm với**: ≤ 1.0–1.5 ATR(14, D1) cho horizon 1–2 ngày **[HEURISTIC]** (R4);
> 5. **Trạng thái con lắc ERL/IRL** — phía nào vừa bị lấy — hoặc ghi "chưa có hướng" (R5).
> Được phép kết luận: **"Chưa có DOL rõ."**

**Vì sao DOL phải đặt trong bối cảnh?** Vì cùng một PDH có thể là DOL (bối cảnh D1 tăng, giá ở discount, đường đi không bị chặn), là đối thủ (bối cảnh D1 giảm), hoặc chỉ là waypoint (đang có run lên tới PWH).

> [!warning] DOL không phải là mức chắc chắn được chạm
> Nó là giả thuyết có tỷ lệ đúng **phải đo**. Một DOL sai không làm quy trình sai — miễn là invalidation đã viết trước và được tôn trọng (hình 25).

---

### 29. Xác định các DOL tiềm năng — quy trình 6 bước

**Bước 1 — Cấu trúc lớn.** Thị trường đang trong xu hướng, trong range, hay chưa rõ? Swing nào đang chi phối cách đọc (Level 4–5)? Nếu chưa rõ → ghi "chưa rõ" và đi tiếp với độ tin cậy thấp.

**Bước 2 — Đánh dấu mức đáng chú ý** (đã qua G1–G5, Level ≥ 3): BSL, SSL, EQH/EQL, PDH/PDL, PWH/PWL, high/low phiên liên quan.

**Bước 3 — Đặt các mức vào bối cảnh:** giá hiện tại ở đâu (premium/discount của range D1)? Mức nào gần? Mức nào là ERL/IRL của range D1? Khoảng cách mỗi mức tính theo ATR(D1)?

**Bước 4 — Xây kịch bản:**
- Nếu giá **tiếp tục** theo hướng hiện tại → mức nào có thể bị tiếp cận trước?
- Nếu giá **đảo chiều** → mức nào thành mục tiêu thay thế?
- Bằng chứng ủng hộ / chống đối mỗi kịch bản là gì (viết ra, không chấm điểm vội)?

**Bước 5 — Xếp hạng bằng lời** (mục 30).

**Bước 6 — Viết điều kiện cập nhật:** mức nào bị lấy thì DOL đổi? Sự kiện cấu trúc nào ở khung nào làm DOL mất hiệu lực? Tin gì sắp ra?

**Nếu chưa đủ bằng chứng để ưu tiên một DOL** → ghi **kịch bản C: chưa có DOL rõ**. Đây là đầu ra hợp lệ của quy trình (RULE-LQ-007).

---

### 30. So sánh và xếp hạng các mục tiêu

![[Liquidity-v2-11-DOL-Kich-Ban.svg|900]]

> [!example]- Hình 11 — đọc thế nào
> - **Đang diễn ra gì:** giá ở giữa sáu mức: PWH, PDH, Asia H phía trên; Asia L, PDL, PWL phía dưới, với khoảng cách theo ATR D1.
> - **Mức được đánh dấu:** sáu mức. Theo DEF-LQ-14 chỉ **PDH/PDL** qua R2 (Level ≥ 4) + R4 (tầm với ≤ 1.5 ATR D1) để làm DOL/đối thủ; Asia H/L (Level 3) là mốc quan sát trong ngày; PWH/PWL nằm ngoài tầm với cho horizon 1–2 ngày.
> - **Timeframe:** khoảng cách theo ATR(14) D1; nến là phiên hiện tại.
> - **Vì sao đáng chú ý:** có ba kịch bản hợp lý; mỗi kịch bản có ủng hộ, chống đối, vô hiệu.
> - **Đã xác nhận:** vị trí và khoảng cách các mức.
> - **Chưa biết:** mức nào bị chạm trước.
> - **Làm gì tiếp:** tính baseline hình học cho cặp DOL–đối thủ trước khi "đọc ICT"; lý lẽ ICT chỉ có giá trị nếu làm tốt hơn con số này.

**Tiêu chí xếp hạng bằng lời** (không cần công thức):

| Tiêu chí | Câu hỏi | Ưu tiên khi |
|---|---|---|
| Khung thời gian | Mức thuộc khung nào? | Khung cao hơn |
| Vai trò range | Là ERL của range D1? | Có |
| Hướng cấu trúc HTF | Cùng hướng cấu trúc D1? | Có |
| Tầm với | Trong ≤ 1–1.5 ATR D1 (horizon 1–2 ngày)? | Có |
| Đường đi | Có POI ngược chiều chưa xử lý chặn đường (HRLR)? | Không bị chặn (LRLR) |
| Đối thủ | Đối thủ gần hay xa? | Không xếp hạng — ghi d_đối thủ/d_DOL và baseline; đó là mốc mà lý lẽ cấu trúc phải vượt qua |
| Đã bị test? | Mức nguyên vẹn hay đã bị chạm? | Nguyên vẹn (giả thuyết — biến N chưa biết dấu) |

**Baseline cho cặp DOL – đối thủ [MATHEMATICAL]:** P(DOL chạm trước đối thủ | random walk) = d_đối thủ / (d_DOL + d_đối thủ). Trong hình 11: PDH (+1.2 ATR) trước PDL (−1.0 ATR) ≈ **45%** — tức là chọn PDH làm DOL đang cược **ngược** hình học; lý lẽ cấu trúc phải đủ mạnh để bù. Asia H (+0.4) trước Asia L (−0.7) ≈ **64%** (chỉ minh họa hình học — không phải cặp DOL hợp lệ vì Asia H/L là Level 3) chỉ do khoảng cách.

**Tier theo DOL v0.2:** A = R1–R5 + S1 + (S2 hoặc S3), không dính loại trừ · B = R1–R5 + một trong S1/S2/S3 · C = còn lại → chỉ quan sát.

---

### 31. Các kịch bản thay thế

**Mẫu thẻ kịch bản** (dán vào daily note):

```text
DOL CARD — [ngày] — khóa lúc [giờ VN]
Range D1: [low] → [high] (khai báo [ngày]; lý do: ...)
Vị trí giá: [premium/discount, % trong range]
Kịch bản A (chính): DOL = [mức], đối thủ = [mức], horizon = [..], baseline = [..%]
   Ủng hộ: ...    Chống: ...    Vô hiệu: [sự kiện, khung]
Kịch bản B (thay thế): DOL = [mức], đối thủ = [mức]
   Ủng hộ: ...    Chống: ...    Vô hiệu: ...
Kịch bản C: chưa có DOL rõ — điều kiện: [vd: hai phía cân bằng, tin tier-1 lúc ...]
Mức trên đường đi (waypoint): [...]
Tier (DOL v0.2): A / B / C     Loại trừ (DOL-D1…DOL-D6): ...
```

**Terminus vs waypoint** (giữ từ note 19 cũ — đã chuyển thành nhãn ex-ante): với mỗi mức trên đường tới DOL, gắn trước nhãn `terminus?` (nơi có thể đảo) hoặc `waypoint?` (nơi có thể bị đi xuyên). Mức cùng phía với DOL, nằm giữa giá và DOL → mặc định `waypoint`. Mức đối diện DOL, tại HTF POI → ứng viên `terminus`. **Nhãn phải có trước khi giá tới**; sau 30+ trường hợp, đo tỷ lệ nhãn đúng. Nhầm waypoint thành terminus là một nguyên nhân hay được nêu của việc Short vào giữa một nhịp tăng [INTERPRETATION].

---

### 32. Điều kiện cập nhật hoặc loại bỏ DOL

**Vòng đời DOL** (DOL v0.2 §2.6): `projected → active → delivered → spent`, hoặc `projected/active → invalidated → flip`.

| Chuyển | Điều kiện (ví dụ v0.1) | Ghi gì |
|---|---|---|
| projected → **active** | Có displacement ở khung setup (H1) hướng về DOL | Giờ, nến |
| active → **delivered** | Giá giao dịch qua mức DOL (≥ ε) | Giờ; MFE trước đó |
| delivered → **spent** | Sau khi chạm, mức hết vai trò mục tiêu | Mức mới cho DOL kế tiếp |
| → **invalidated** | Close + acceptance ở khung của DOL qua mức vô hiệu; MSS ≥ H1 ngược hướng; tin làm đổi bối cảnh | Sự kiện + giờ + khung |
| invalidated → **flip** | Đối thủ (đã ghi sẵn) trở thành DOL mới | Lý do; **không** xóa dòng cũ |

![[Liquidity-v2-25-DOL-Duoc-Cap-Nhat.svg|900]]

> [!example]- Hình 25 — đọc thế nào
> - **Đang diễn ra gì:** lúc 06:00 DOL dự kiến = PDH, đối thủ = PDL, vô hiệu = H1 acceptance dưới protected low. T1 có displacement về PDH (active); T2 hai close H1 dưới protected low (invalidated); T3 DOL đổi sang PDL (flip).
> - **Mức được đánh dấu:** PDH, PDL, protected low H1.
> - **Timeframe:** H1.
> - **Vì sao đáng chú ý:** dự đoán ban đầu SAI, nhưng quy trình ĐÚNG vì điều kiện vô hiệu đã viết trước và được tôn trọng.
> - **Đã xác nhận:** sự kiện vô hiệu tại T2.
> - **Chưa biết:** PDL có được delivered không.
> - **Làm gì tiếp:** chấm điểm riêng hai thứ: độ chính xác DOL (thống kê) và kỷ luật cập nhật (quy trình).

---

### 33. Những lỗi phổ biến khi xác định DOL

| Lỗi | Vì sao xảy ra | Dấu hiệu | Cách sửa | Quy tắc chặn |
|---|---|---|---|---|
| Chọn DOL **sau khi giá đã chạy** | Muốn câu chuyện khớp | Thẻ DOL trống giờ khóa | Khóa thẻ trước phiên | RULE-LQ-003 |
| "Giá luôn đi từ liquidity này sang liquidity khác" | Ẩn dụ bị hiểu thành luật | Mọi chuyển động đều được giải thích | Thay bằng xác suất chạm trước đối thủ + baseline | Mục 5 |
| Chọn **mọi mức** làm mục tiêu cùng lúc | Ngại sai | Thẻ có 4 DOL | Một chính + một thay thế + một đối thủ | DEF-LQ-14 |
| Bỏ qua cấu trúc lớn | Nhìn M5 trước | DOL là mức M5 | DOL phải Level ≥ 4, khung ≥ khung bias | DEF-LQ-14 (R2) |
| Coi mục tiêu **gần** là chắc chắn | Hình học bị nhầm thành "draw" | Tỷ lệ "đúng" ≈ baseline | Trừ baseline | HYP-LQ-005 |
| Không cập nhật khi giá đổi | Neo vào dự đoán | Giữ DOL thứ Hai tới thứ Tư dù đã delivered/invalidated | Trạng thái DOL + giờ | Mục 32 |
| Nhầm "câu chuyện hợp lý" với khả năng dự báo | Lời giải thích nghe hay | Không có số đo | Đo tỷ lệ đúng ngoài mẫu | Part VIII |

---
## PART VI — MULTI-TIMEFRAME ANALYSIS: D1 → H1 → M5

> [!important] Ba khung, ba câu hỏi, không phải ba chart độc lập
> - **D1 = Context:** *"Tôi đang ở đâu, mức lớn nào thật sự quan trọng, DOL có thể là gì, điều gì buộc tôi đánh giá lại?"*
> - **H1 = Setup:** *"Trong bối cảnh đó, giá đang tiến tới / phản ứng / đi xuyên mức nào, cấu trúc trung gian ủng hộ hay mâu thuẫn, khi nào cần nhìn gần?"*
> - **M5 = Quan sát chi tiết (execution timeframe):** *"Chuyện gì đang xảy ra quanh mức đã chọn — theo đúng trình tự — và nó được phân loại là gì?"*
> Không bắt đầu bằng M5 rồi chọn D1/H1 để hợp thức hóa một nhận định đã có.

![[Liquidity-v2-22-Quy-Trinh-D1-H1-M5.svg|900]]

> [!example]- Hình 22 — đọc thế nào
> - **Đang diễn ra gì:** ba cột D1/H1/M5 — câu hỏi, cái cần xác định, cái bỏ qua, cổng chuyển, đầu ra.
> - **Mức được đánh dấu:** không áp dụng (sơ đồ quy trình).
> - **Timeframe:** cả ba.
> - **Vì sao đáng chú ý:** mỗi mũi tên là một **điều kiện**, không phải thói quen.
> - **Đã xác nhận:** —
> - **Chưa biết:** —
> - **Làm gì tiếp:** in cột "Bỏ qua" ra — đó là phần giúp chart sạch.

### 34. D1 — Higher-Timeframe Liquidity Context

![[Liquidity-v2-19-D1-Ban-Do-Liquidity.svg|900]]

> [!example]- Hình 19 — đọc thế nào
> - **Đang diễn ra gì:** D1 giảm từ range high (swing L5) xuống vùng EQL D1 (range low); có lower high (IRL) và một FVG D1 giảm ở premium.
> - **Mức được đánh dấu:** BSL ngoài range high; EQL D1 = range low (SSL ngoài range); lower high; PWH/PWL; EQ; FVG D1.
> - **Timeframe:** D1.
> - **Vì sao đáng chú ý:** bản tóm tắt D1 bên phải là **đầu ra bắt buộc** trước khi mở H1.
> - **Đã xác nhận:** cấu trúc giảm tới hiện tại; vị trí giá ở discount gần range low.
> - **Chưa biết:** DOL A (SSL dưới EQL D1) có được chạm trước khi lower high (Level 3 — mức **vô hiệu**, không đủ chuẩn DOL) bị lấy kèm acceptance hay không.
> - **Làm gì tiếp:** ghi điều kiện đánh giá lại; sang H1 để xem cách giá tiến tới EQL D1.

**Nhiệm vụ của D1:** trả lời — cấu trúc lớn thế nào; swing nào thật sự quan trọng; BSL/SSL lớn ở đâu; internal/external theo range nào; có DOL đủ cơ sở không; giá đang ở đâu so với các mức; POI/cấu trúc nào ảnh hưởng cách đọc liquidity; điều gì buộc đánh giá lại.

**Quy trình D1 bắt buộc:**

| Bước | Việc | Cách làm (v0.1) | Đầu ra |
|---|---|---|---|
| 1 | **Đọc cấu trúc lớn** | N-bar pivot N = 3 trên D1; giữ swing Level 4–5; bỏ dao động nhỏ | Xu hướng / range / chưa rõ |
| 2 | **Chọn dealing range** | Cặp swing D1 gần nhất bao quanh giá, phản ứng ≥ 1.0·ATR(D1), một đầu là gốc của displacement gần nhất → gán Level 4; ghi lý do | Range D1 + ngày khai báo |
| 3 | **Đánh dấu BSL/SSL** | Chỉ mức qua G1–G5, Level ≥ 3; EQH/EQL D1 theo DEF-LQ-06; PWH/PWL, PDH/PDL | 3–4 mức mỗi phía |
| 4 | **Phân loại ERL/IRL** | Theo range ở bước 2 | Nhãn ERL/IRL có tên range |
| 5 | **Đánh giá DOL tiềm năng** | Mục 29–30; một hoặc nhiều kịch bản | Thẻ DOL (có thể "chưa rõ") |
| 6 | **Vị trí giá** | % trong range; khoảng cách tới từng mức theo ATR D1 | Premium/discount + khoảng cách |
| 7 | **Điều kiện cập nhật** | Sự kiện D1 nào làm cấu trúc / phân loại / DOL phải xem lại | 1–3 điều kiện cụ thể |

> [!warning] Những điều KHÔNG làm trên D1
> - Không đánh dấu mọi swing thành liquidity quan trọng.
> - Không khẳng định DOL chắc chắn bị chạm.
> - Không suy ra số lượng stop từ OHLC.
> - Không đổi cách chọn swing để giải thích diễn biến đã xảy ra.
> - Không ép bullish/bearish khi bằng chứng mâu thuẫn — "chưa rõ" là đầu ra hợp lệ.

---

### 35. D1 checklist

| Trường | Bắt buộc? | Ý nghĩa / cách điền |
|---|---|---|
| **D1 structure** | ✅ | Tăng / giảm / range / chưa rõ + swing chi phối (giá, ngày) |
| **Dealing range** | ✅ | Low → High, ngày khai báo, lý do một câu |
| **Major BSL** | ✅ | 1–3 mức Level ≥ 4 phía trên (giá, loại, khung) |
| **Major SSL** | ✅ | 1–3 mức Level ≥ 4 phía dưới |
| **Internal liquidity** | ✅ | IRL đáng kể trong range (swing L3, FVG D1) |
| **External liquidity** | ✅ | ERL trên / dưới của range |
| **Potential DOL** | ✅ | Kịch bản A/B/C (có thể "chưa rõ") |
| **Current price location** | ✅ | % trong range; premium/discount; khoảng cách tới DOL và đối thủ theo ATR |
| **Important POI** | ⭕ bổ trợ | OB/FVG D1 có thể ảnh hưởng phản ứng |
| **Alternative scenario** | ✅ | Ít nhất một |
| **What would invalidate / weaken** | ✅ | Sự kiện D1 cụ thể (close + acceptance qua mức nào) |
| **What I need to observe on H1** | ✅ | Mức nào, hành vi gì |

---

### 36. Điều kiện chuyển từ D1 xuống H1

**Chuyển khi:** tóm tắt D1 đã có đủ các trường ✅ — kể cả khi một số trường ghi "chưa rõ". Mục đích của D1 là **định hướng việc quan sát**, không phải "có bias".

**Nếu D1 chưa rõ:** vẫn được xem H1 để **thu thập thông tin** (ví dụ: giá đang tạo cấu trúc gì quanh biên range), nhưng:
- ghi rõ `d1_status: unclear` trong thẻ;
- **không** được giả vờ có bias; mọi sự kiện M5 sau đó chỉ được ghi nhận, không được dùng làm cơ sở trade theo framework D1 → H1 → M5;
- đặt câu hỏi D1 cụ thể mà H1 có thể giúp trả lời (ví dụ "giá có chấp nhận dưới EQL D1 không?").

---

### 37. H1 — Intermediate Liquidity Analysis

![[Liquidity-v2-20-H1-Trong-Boi-Canh-D1.svg|900]]

> [!example]- Hình 20 — đọc thế nào
> - **Đang diễn ra gì:** H1 giảm liên tục (lower highs) tiến tới SSL D1 (EQL = range low từ bản đồ D1); dải dưới chart cho thấy trạng thái theo dõi chuyển NOT READY → MONITORING → EVENT.
> - **Mức được đánh dấu:** SSL D1 (mức đến từ D1), EQH H1 phía trên (đối thủ gần).
> - **Timeframe:** H1.
> - **Vì sao đáng chú ý:** H1 không tạo bias mới — nó trả lời "khi nào cần nhìn gần".
> - **Đã xác nhận:** H1 đồng thuận với D1 (cùng giảm); mức D1 đang bị xuyên.
> - **Chưa biết:** sự kiện tại mức D1 sẽ là rejection hay acceptance.
> - **Làm gì tiếp:** mở M5, phân xử theo DEF-LS-04; điền H1 handoff checklist.

**Nhiệm vụ của H1:** giá đang tiến tới mức D1 nào; cấu trúc trung gian ủng hộ hay mâu thuẫn D1; có mức liquidity mới bên trong range không; mức H1 nào đủ quan trọng để đổi cách theo dõi; giá đang tiếp cận / phản ứng / đi xuyên; có lý do quan sát M5 chưa.

**Quy trình H1 bắt buộc:**

| Bước | Việc | Chi tiết |
|---|---|---|
| 1 | **Cấu trúc H1 trong bối cảnh D1** | N-bar N = 3; phân biệt internal/external structure H1; không coi mọi swing H1 như nhau |
| 2 | **Đánh dấu liquidity H1** | Swing H1 Level ≥ 3, EQH/EQL H1, high/low phiên; mức H1 **liên quan** mức D1 |
| 3 | **Quan hệ H1 ↔ D1** | Mức H1 nào nằm gần mục tiêu D1? Mức nào chỉ là nội bộ? Có xung đột? Một mức H1 đã bị lấy có đổi mục tiêu D1 không (thường **không** — trừ khi là sự kiện ở khung D1) |
| 4 | **Theo dõi diễn biến thực tế** | Phân loại trạng thái (bảng dưới) |
| 5 | **Đánh giá thông tin mới** | Cái gì đổi nhận định (sự kiện đã phân loại, sự kiện cấu trúc H1) vs cái gì chỉ là dao động |
| 6 | **Điều kiện tiếp theo** | Cần theo dõi gì tiếp trên H1 hoặc M5 |

**Phân loại trạng thái quan hệ giá – mức (không gọi tất cả là sweep):**

| Trạng thái | Quan sát | Gọi là sweep? |
|---|---|---|
| Còn xa vùng quan tâm | \|giá − L\| > 1.5·ATR(14, H1) (DEF-LQ-16) | Không |
| Đang tiến tới | Trong phạm vi, chưa chạm | Không |
| Đã chạm | E1 | Không |
| Đã vượt qua (đang chạy) | PENETRATED / PENDING | **Chưa** |
| Vượt qua và quay lại | E2/E3 | **Có** |
| Vượt qua và tiếp tục | E4 (có thể E7) | Không |
| Chưa đủ thông tin | EXPIRED / không rõ | Không |

---

### 38. H1 checklist (handoff)

| Trường | Ý nghĩa |
|---|---|
| **D1 context** | Một dòng tóm tắt từ thẻ D1 (cấu trúc, DOL A/B/C) |
| **H1 structure** | Xu hướng H1, swing H1 cấu trúc gần nhất (protected high/low) |
| **Relevant BSL** | Mức phía trên liên quan (từ D1 hoặc H1 Level ≥ 3) |
| **Relevant SSL** | Mức phía dưới liên quan |
| **Internal/external classification** | Theo range D1 (mặc định) |
| **Current price location** | Khoảng cách tới mức theo ATR(H1) |
| **Liquidity event status** | Một trong 7 trạng thái ở mục 37 |
| **Potential next price paths** | (a)… (b)… — tối đa 2–3 nhánh |
| **What I need to observe on M5** | Close ở đâu so với L; MSS? displacement? |
| **What would weaken the current interpretation** | Sự kiện H1 cụ thể |
| **Status** | NOT READY / MONITORING / EVENT UNDER EVALUATION |

**Ví dụ 1 — D1 và H1 đồng thuận** (hình 20): D1 giảm, DOL A = SSL D1. H1 giảm với lower highs liên tục tới mức D1. *Status: EVENT UNDER EVALUATION* khi mức bị xuyên. Cần xem trên M5: close có quay lại trên L + δ không; có MSS tăng không. Nếu có → đó là **phản ứng đảo chiều ngay tại mức DOL A** (DOL đã delivered) → DOL chuyển `delivered`; câu hỏi mới: có kịch bản đảo chiều (B) không.

**Ví dụ 2 — H1 đi ngược D1:** D1 tăng (DOL = BSL range high), giá đang ở discount. H1 lại đang giảm với lower highs, tiến tới SSL dưới HL D1. Cách xử lý:
- Giữ D1 làm bối cảnh; gọi nhịp H1 là **pullback có điều kiện** — không phải bias mới.
- Mức cần theo dõi là **mức D1** (HL D1), không phải đáy H1 bất kỳ.
- Status MONITORING khi giá vào phạm vi mức D1 trong killzone.
- Nếu H1 tạo **acceptance** dưới HL D1 (2 close H1 liên tiếp) → đó mới là sự kiện có thể đổi D1 (cần close D1 để xác nhận ở khung D1).
- Nếu rejection + MSS tăng trên M5 → ghi nhận; kịch bản D1 tăng **tiếp tục là giả thuyết**, chưa được chứng minh. (Ví dụ đầy đủ: hình 31.)

---

### 39. Điều kiện chuyển từ H1 xuống M5

> [!example] DEF-LQ-16 — Trạng thái theo dõi (v0.1, HEURISTIC)
> - **STATE A — NOT READY:** \|giá − L\| > **1.5 × ATR(14, H1)** với mọi mức L trong danh sách, **hoặc** ngoài killzone đã khai báo, **hoặc** trong cửa sổ tin tier-1 (−10 phút → +15 phút).
> - **STATE B — MONITORING:** \|giá − L\| ≤ 1.5 × ATR(14, H1) với ít nhất một mức L, **và** trong killzone, **và** không trong cửa sổ tin.
> - **ARMED** là trạng thái của **MỨC** (có trong danh sách, chưa bị xuyên); NOT READY / MONITORING / EVENT là trạng thái của **việc theo dõi**.
> - **STATE C — EVENT UNDER EVALUATION:** một mức L trong danh sách vừa bị xuyên (high > L + ε hoặc low < L − ε) — trạng thái PENDING trong k nến M5.

| Trạng thái | Ý nghĩa | Hành động | Không được làm |
|---|---|---|---|
| **A — NOT READY** | Giá chưa tới vùng quan tâm hoặc H1 chưa cho lý do rõ | Tiếp tục theo dõi H1; đặt cảnh báo giá | Tìm tín hiệu M5 chỉ vì có dao động nhỏ |
| **B — MONITORING** | Giá ở gần / trong vùng quan tâm | Mở M5 để **ghi nhận phản ứng** | Kết luận sweep / reversal / entry |
| **C — EVENT UNDER EVALUATION** | Sự kiện quanh mức đang/vừa xảy ra | Theo dõi trình tự, phân xử theo định nghĩa | Phân loại tại wick; hành động trước khi có nhãn |

![[Liquidity-v2-23-May-Trang-Thai-Chuyen-Khung.svg|900]]

> [!example]- Hình 23 — đọc thế nào
> - **Đang diễn ra gì:** máy trạng thái NOT READY ⇄ MONITORING → EVENT → CLASSIFIED → UPDATE MAP → (REASSESS D1 nếu có sự kiện D1); nhánh UNDETERMINED khi hết k nến.
> - **Mức được đánh dấu:** không áp dụng.
> - **Timeframe:** H1 điều khiển NOT READY/MONITORING; M5 điều khiển EVENT/CLASSIFIED; D1 điều khiển REASSESS.
> - **Vì sao đáng chú ý:** trạng thái mặc định là **chờ**; không trạng thái nào đồng nghĩa "vào lệnh".
> - **Đã xác nhận:** —
> - **Chưa biết:** —
> - **Làm gì tiếp:** ghi trạng thái vào log mỗi lần chuyển, kèm giờ.

> [!warning] Chuyển xuống M5 ≠ đã có setup
> Mở M5 ở STATE B chỉ để **quan sát**. Setup giao dịch (nếu có) thuộc về model ([[01 - ICT 2022 Model]]) và bộ quy tắc DOL v0.2 — không thuộc note Liquidity.

---

### 40. M5 — Detailed Liquidity Observation

![[Liquidity-v2-21-M5-Quan-Sat-Phan-Ung.svg|900]]

> [!example]- Hình 21 — đọc thế nào
> - **Đang diễn ra gì:** M5 quanh SSL D1: 08:20 tiếp cận; nến 08:35 (đóng 08:40) xuyên L và close > L + δ ngay trong nến đó (SWEEP, E2); 09:05 close trên swing high M5 Level 2 với thân lớn, để lại FVG (REVERSAL CONF.).
> - **Mức được đánh dấu:** L (từ D1), L + δ, swing high M5 Level 2 (bỏ qua micro swing 08:30).
> - **Timeframe:** M5, giờ New York.
> - **Vì sao đáng chú ý:** known_at của nhãn là **08:40** (close nến phân xử), không phải 08:35.
> - **Đã xác nhận:** SWEEP + MSS M5.
> - **Chưa biết:** giá có hồi tới EQH H1 không; D1 có đổi hướng không.
> - **Làm gì tiếp:** kết thúc phân tích M5 khi sự kiện đã được phân loại; quay về H1.

**M5 cung cấp gì:** trình tự chính xác (tiếp cận → xuyên → close ở đâu → phản ứng), thời điểm biết của nhãn, độ sâu xuyên, swing nào bị phá.

**M5 KHÔNG tự xác nhận được:** bias D1; DOL; ý nghĩa cấu trúc lớn; "ai" đã giao dịch.

**Vì sao một mức M5 kém quan trọng hơn mức D1?** Ít người nhìn (T thấp), bị tạo ra liên tục (Level 1), và trên random walk xuất hiện dày đặc — "lấy liquidity M5" mô tả gần như mọi nhịp dao động.

**Khi nào swing M5 chỉ là dao động nhỏ?** Khi nó không qua DC θ = 0.4·ATR(M5) hoặc nằm bên trong nhịp giữa hai swing Level 2 liền kề. **Khi nào phản ứng M5 đủ quan trọng để cập nhật H1?** Khi nó xảy ra **tại một mức H1/D1 trong danh sách** và tạo ra sự kiện cấu trúc ở **swing Level ≥ 2** — và kể cả khi đó, nó cập nhật **trạng thái** H1, không đổi bối cảnh D1.

**Vì sao không đánh dấu mọi wick M5 thành liquidity event?** Vì một wick xuyên một mức không có trong danh sách là "unlisted breach" — ghi lại thì được, gọi là liquidity event thì không (G1).

**Quy trình M5 (7 bước):**

| Bước | Việc |
|---|---|
| 1 | **Xác nhận lại mức:** mức đến từ D1, H1, hay mới hình thành trên M5? (Mức mới M5 → không phải mức theo dõi chính.) |
| 2 | **Xác định chính xác điều gì đang xảy ra:** tiến tới / chạm / xuyên / close bên kia / quay lại? |
| 3 | **Ghi nhận phản ứng:** tốc độ (range nến / ATR M5), close ở đâu, swing nào bị phá. Không dùng một cây nến lớn đơn lẻ làm bằng chứng đầy đủ |
| 4 | **Kiểm tra cấu trúc liên quan:** nếu dùng MSS/BOS — swing nào bị phá, thuộc cấp nào (Level ≥ 2 mới tính) |
| 5 | **Phân biệt kịch bản:** sweep + phản ứng quay lại · vượt rồi tiếp tục · chạm chưa phản ứng rõ · phá cấu trúc không sweep · không đủ bằng chứng |
| 6 | **Cập nhật nhận định:** cái gì đã xác nhận, cái gì vẫn là giả thuyết, bước quan sát tiếp theo |
| 7 | **Không ép kết luận:** không thỏa định nghĩa → "chưa xác định" / "không phù hợp giả thuyết đang kiểm tra" |

**Điều kiện kết thúc phân tích M5:** sự kiện được **phân loại xong** (E-code + có/không xác nhận trong m nến), **hoặc** hết killzone, **hoặc** giá rời phạm vi (> 1.5·ATR H1), **hoặc** tin tier-1. Kết thúc **không** có nghĩa giá sẽ đảo chiều hay tiếp tục.

**Năm lớp phải tách riêng khi ghi M5:**
1. **Sự kiện đã xảy ra** [OBSERVABLE];
2. **Cách phân loại** (E-code) [định nghĩa];
3. **Ý nghĩa với cấu trúc** [INTERPRETATION];
4. **Giả thuyết về diễn biến tiếp theo** [HYPOTHESIS];
5. **Kết quả thực tế** — chỉ biết sau [OBSERVABLE, ex-post].

---

### 41. M5 checklist

- [ ] Mức đang theo dõi có trong danh sách trước phiên (ghi nguồn: D1/H1) — **bắt buộc**
- [ ] Giờ tiếp cận; trạng thái MONITORING bắt đầu lúc …
- [ ] Nến xuyên đầu tiên (j): giờ, high/low, close
- [ ] Phân xử trong nến j + k = 3 nến sau: REJECTED / ACCEPTED / EXPIRED — **known_at = …**
- [ ] Độ sâu xuyên (ATR M5), thời gian bên kia (số nến)
- [ ] Trong m nến: MSS (swing Level ≥ 2 nào?) + displacement (thân / ATR) → REV. CONF. / STALE
- [ ] Cực trị sweep L' thêm vào danh sách (nếu E2/E3)
- [ ] Ghi rõ: đã xác nhận / còn là giả thuyết / chưa biết
- [ ] Điều kiện làm yếu nhận định (ví dụ close qua cực trị sweep)
- [ ] Trạng thái DOL sau sự kiện (không đổi / delivered / invalidated)

---

### 42. Các trường hợp D1 / H1 / M5 mâu thuẫn

**Nguyên tắc:** mỗi khung mô tả **cấu trúc của chính nó**. Mâu thuẫn thường là hai khung mô tả hai thứ khác nhau, không phải một khung "sai".

| Xung đột | Cách đọc | Hành động |
|---|---|---|
| D1 tăng, H1 giảm | H1 là pullback trong bối cảnh D1 (cho tới khi có sự kiện D1) | Theo dõi mức D1 mà pullback tiến tới; không đổi D1 vì H1 |
| D1 tăng, H1 tăng, M5 giảm mạnh | M5 là dao động trong nhịp H1 | Chỉ quan tâm nếu nó xảy ra tại mức trong danh sách |
| D1 range (chưa rõ), H1 xu hướng | Bối cảnh lớn chưa cho hướng | `d1_status: unclear`; ghi sự kiện, không trade theo framework |
| H1 có RUN ACTIVE ngược hướng với kịch bản M5 | Rejection M5 trong run H1 có thể chỉ là nhịp hồi [HYPOTHESIS — RULE-LQ-011] | Không tìm reversal tới khi RUN ENDED (RULE-LS-005) |
| M5 MSS tăng tại mức D1, nhưng H1 vẫn lower high | Chỉ mới đổi ở M5 | Ghi REV. CONF. (M5); H1 vẫn giảm cho tới sự kiện H1 |
| Ba khung đều mâu thuẫn và không có mức nào gần | Không đủ thông tin | **UNDETERMINED** — đứng ngoài là kết luận hợp lệ |

**Khi nào giữ trạng thái chưa rõ:** khi không xác định được khung nào đang mô tả cấu trúc liên quan tới mức đang theo dõi, hoặc khi hai kịch bản có bằng chứng tương đương (hình 24).

---

### 43. Quy trình tích hợp ba timeframe — bảy tình huống chuyển khung

#### Tình huống 1 — D1 có các mức liquidity rõ nhưng giá còn ở xa

| | |
|---|---|
| **Đã biết** | Bản đồ D1; khoảng cách tới mức gần nhất > 1.5·ATR(H1) |
| **Chưa biết** | Giá sẽ tới mức nào trước, khi nào |
| **Quan sát tiếp** | H1 (1–2 lần mỗi phiên); cảnh báo giá tại biên phạm vi |
| **Điều kiện chuyển bước** | Giá vào phạm vi một mức + killzone → MONITORING |
| **Cập nhật khi** | Có sự kiện D1, hoặc xuất hiện mức H1 Level ≥ 3 mới gần mức D1 |
| **Không được kết luận** | "Hôm nay giá sẽ tới mức X" |

```text
D1:  ── PDH ──────────────────  (xa)
                 ● giá  (cách > 1.5 ATR H1 mọi mức)
     ── PDL ──────────────────  (xa)
→ STATE A. Không mở M5.
```

#### Tình huống 2 — Giá đang tiến tới một mức D1

| | |
|---|---|
| **Đã biết** | Hướng tiếp cận, tốc độ (số nến H1, có displacement không) |
| **Chưa biết** | Giá có xuyên không, phản ứng thế nào |
| **Quan sát tiếp** | H1 — cấu trúc của nhịp tiếp cận (đồng thuận hay ngược D1?) |
| **Điều kiện chuyển bước** | ≤ 1.5·ATR(H1) + killzone → mở M5 (MONITORING) |
| **Cập nhật khi** | Nhịp tiếp cận tạo mức H1 mới (EQL H1 ngay trước mức D1 → gắn `inducement?`) |
| **Không được kết luận** | "Giá đang bị hút tới" (đó là ẩn dụ); "sẽ đảo tại mức" |

```text
H1:  ╲  ╱╲
      ╲╱  ╲  ╱╲
           ╲╱  ╲      ← lower highs (đồng thuận D1 giảm?)
   ────────────── L (mức D1)   ← cách 1.2 ATR H1 → MONITORING nếu trong killzone
```

#### Tình huống 3 — Giá đã chạm vùng liquidity trên H1

| | |
|---|---|
| **Đã biết** | E1 trên H1 (chạm trong ε) — chưa xuyên |
| **Chưa biết** | Lần tới có xuyên không |
| **Quan sát tiếp** | M5 nếu đang trong killzone (để thấy chi tiết lần chạm kế); nếu ngoài killzone → chờ H1 |
| **Điều kiện chuyển bước** | Xuyên → EVENT |
| **Cập nhật khi** | Giá rời ≥ 0.5·ATR(H1) → E0/E1 đóng hồ sơ; tăng N |
| **Không được kết luận** | "Mức đã bị lấy", "mức giữ được" |

#### Tình huống 4 — M5 tạo EQH/EQL nhưng H1 chưa có vùng quan tâm rõ

| | |
|---|---|
| **Đã biết** | Một cặp đỉnh/đáy M5 gần bằng nhau |
| **Chưa biết** | Nó có ý nghĩa gì với cấu trúc H1/D1 |
| **Quan sát tiếp** | Không đổi gì; tiếp tục theo dõi H1 |
| **Điều kiện chuyển bước** | Không có |
| **Cập nhật khi** | EQH M5 trùng (≤ 0.10·ATR H1) với một mức H1/D1 trong danh sách → coi như **mức H1** |
| **Không được kết luận** | Nâng EQL M5 thành "mục tiêu lớn"; gọi cú quét nó là "sweep external" |

```text
M5:  ‾‾╲╱‾‾╲╱‾‾    ← EQH M5 (Level 1–2)
H1:  (không có mức nào gần) → bỏ qua, ghi chú tùy chọn
```

#### Tình huống 5 — M5 tạo MSS nhưng không liên quan đến mức đang theo dõi

| | |
|---|---|
| **Đã biết** | Cấu trúc M5 đổi ở xa mọi mức trong danh sách |
| **Chưa biết** | Có lan lên H1 không |
| **Quan sát tiếp** | H1 |
| **Điều kiện chuyển bước** | Không có (vẫn STATE A/B) |
| **Cập nhật khi** | Nó tạo ra swing H1 cấu trúc mới |
| **Không được kết luận** | "Đảo chiều bắt đầu"; "có sweep ở đâu đó" |

#### Tình huống 6 — Giá xuyên mức liquidity và tiếp tục chạy

| | |
|---|---|
| **Đã biết** | E4 (acceptance); có thể là run nếu mức kế cũng được chấp nhận |
| **Chưa biết** | Run sẽ kết thúc ở đâu |
| **Quan sát tiếp** | H1 — trạng thái run; mức kế tiếp cùng phía |
| **Điều kiện chuyển bước** | Mức kế vào phạm vi → MONITORING cho mức đó |
| **Cập nhật khi** | Mức cũ "spent"; nếu là mức vô hiệu của DOL → DOL invalidated |
| **Không được kết luận** | "Sweep thất bại nên sắp đảo"; "đây chỉ là cú quét sâu" |

```text
   ─ L2 ─────────────   ← mức kế (MONITORING tiếp theo)
      ▮▮ ▮               ← 2 close trên L1 = E4
   ─ L1 ─▮───────────   ← L1 spent
   ▮▮▮
```

#### Tình huống 7 — D1, H1, M5 đưa ra tín hiệu mâu thuẫn

| | |
|---|---|
| **Đã biết** | Mỗi khung có cấu trúc riêng |
| **Chưa biết** | Khung nào "thắng" — câu hỏi này thường sai dạng |
| **Quan sát tiếp** | Xác định khung nào mô tả cấu trúc **của mức đang theo dõi** (ý nghĩa thuộc về swing — R7 của Dealing Range) |
| **Điều kiện chuyển bước** | Chỉ khi một khung có sự kiện đã phân loại tại mức trong danh sách |
| **Cập nhật khi** | Sự kiện ở khung có thẩm quyền (D1 cho bối cảnh, H1 cho setup) |
| **Không được kết luận** | Lấy khung nào thuận câu chuyện nhất |

**Quy trình tích hợp (tóm tắt):** D1 vẽ bản đồ + DOL (trước phiên) → H1 xác định trạng thái A/B/C (trong phiên, mỗi giờ hoặc khi có cảnh báo) → M5 ghi sự kiện tại mức (chỉ ở B/C) → sự kiện đã phân loại quay về H1 cập nhật trạng thái → chỉ sự kiện D1 mới về D1.

---
## PART VII — OPERATIONAL FRAMEWORK

### 44. Quy trình mở chart từ đầu (SOP)

> [!abstract] SOP-LQ v0.1 — mở một chart chưa phân tích
> **Bước 1 — D1 (trước phiên, ~15 phút).** Xác định swing lớn (N = 3) → chọn range có lý do → đánh dấu BSL/SSL qua G1–G5 (Level ≥ 3) → gắn ERL/IRL theo range → thẻ DOL (A/B/C) → vị trí giá → điều kiện đánh giá lại.
> **Đầu ra:** *bản đồ liquidity D1 có cấu trúc và lý do* (mục 35).
>
> **Bước 2 — H1 (đầu phiên + mỗi giờ).** Cấu trúc trung gian → liên kết mức H1 với D1 → giá đang tiến tới / đã vượt mức nào → thông tin còn thiếu → STATE A/B/C.
> **Đầu ra:** *danh sách mức H1 có ý nghĩa + trạng thái theo dõi* (mục 38).
>
> **Bước 3 — M5 (chỉ khi STATE B/C).** Xác nhận mức cần theo dõi → ghi sự kiện đúng thứ tự → tiếp cận / xuyên / quay lại / tiếp tục → phân loại theo DEF-LS-04 → theo dõi cấu trúc nếu liên quan → cập nhật hoặc bác bỏ giả thuyết.
> **Đầu ra:** *bản ghi sự kiện không dựa vào hindsight* (mục 41).
>
> **Bước 4 — Tổng hợp (cuối phiên).** Trả lời 6 câu: mức nào đã xác định trước? · mức nào thực sự bị tiếp cận/vượt? · điều gì xảy ra sau sự kiện? · diễn giải ban đầu có được hỗ trợ không? · còn gì chưa biết? · cần theo dõi gì tiếp?
> **Đầu ra:** *một đoạn tổng hợp + cập nhật bản đồ cho ngày mai.*
>
> **Không bắt buộc** phải có dự báo hay giao dịch ở cuối mỗi lần phân tích.

---

### 45. Cách đánh dấu mức liquidity

![[Liquidity-v2-33-Danh-Dau-Qua-Nhieu.svg|900]]

> [!example]- Hình 33 — đọc thế nào
> - **Đang diễn ra gì:** cùng một chart H1; trái kẻ mọi swing (fractal 3 nến), phải chỉ giữ 4 mức có lý do.
> - **Mức được đánh dấu:** phải: range high/low (ERL), swing H1 cấu trúc, higher low bảo vệ.
> - **Timeframe:** H1.
> - **Vì sao đáng chú ý:** đánh dấu mọi swing làm "giá lấy liquidity" mô tả mọi chuyển động.
> - **Đã xác nhận:** vị trí các mức.
> - **Chưa biết:** —
> - **Làm gì tiếp:** giới hạn 3–4 mức mỗi phía; mỗi mức có nhãn đầy đủ.

**Quy ước trên TradingView (đề xuất):**

| Thành phần | Quy ước |
|---|---|
| Màu | BSL cam/đỏ đậm · SSL xanh dương · DOL tím · range xám đậm · EQ xám nét đứt |
| Nét | Level 4–5 nét liền dày · Level 3 nét đứt · Level 2 (nếu giữ) chấm |
| Nhãn | `BSL · PDH · L4 · IRL(D1 10/01–10/09) · known 10-14 17:00 NY` |
| Điểm bắt đầu | Kẻ từ **nến tạo mức**, không kẻ từ mép trái chart |
| Mức đã tiêu | Không xóa — đổi sang xám nhạt + ghi `spent 10-15 19:40 VN (E4)` hoặc `swept 19:40 VN (E2)` |
| Mức mới sau sweep | L' tại cực trị sweep, nhãn `L' · from E2 · known 19:40 VN` |
| Ảnh chụp | Chụp danh sách mức trước phiên, lưu vào `05 - Live Trading Journal/attachments/` theo quy ước tên của vault |

**Danh sách mức trong daily note** (copy được vào backtest):

```text
LEVELS — EURUSD — 2026-10-15 — khóa 06:30 VN — feed: [tên feed]
side | price   | type   | TF | level | role(D1 range) | known_at (NY)     | notes
BSL  | 1.0960  | swing  | D1 | L5    | ERL            | 2026-10-08 17:00  | range high
BSL  | 1.0912  | PDH    | D1 | L4    | IRL            | 2026-10-14 17:00  |
BSL  | 1.0889  | EQH    | H1 | L3    | IRL            | 2026-10-14 05:00  | Δ=0.06 ATR(H1); engineered? no
SSL  | 1.0842  | PDL    | D1 | L4    | IRL            | 2026-10-14 17:00  |
SSL  | 1.0780  | EQL    | D1 | L4    | ERL            | 2026-10-09 17:00  | range low
```
*(Giá trong bảng là giả định để minh họa định dạng.)*

---

### 46. Cách ghi nhận một liquidity event

![[Liquidity-v2-29-Nhat-Ky-Append-Only.svg|900]]

> [!example]- Hình 29 — đọc thế nào
> - **Đang diễn ra gì:** một nhật ký append-only: mức được liệt kê, DOL dự kiến, sự kiện xuyên, phân xử, xác nhận, thất bại sau đó, và một mức không bao giờ bị chạm.
> - **Mức được đánh dấu:** PDL, EQH H1.
> - **Timeframe:** nhiều khung; cột known_at ghi giờ.
> - **Vì sao đáng chú ý:** dòng 21:50 "REV. FAILED" là dòng **mới**, không sửa dòng 20:05; dòng cuối "NOT TOUCHED" vẫn được ghi — đó là mẫu số.
> - **Đã xác nhận:** định dạng ghi.
> - **Chưa biết:** —
> - **Làm gì tiếp:** dùng đúng các cột này cho mọi sự kiện, kể cả sự kiện mơ hồ.

**Một sự kiện = một dòng tối thiểu:** `ghi lúc` · `known_at` · `mức (giá, loại, TF, level, ERL/IRL)` · `E-code` · `độ sâu / thời gian bên kia` · `xác nhận (MSS/disp, m)` · `trạng thái DOL sau sự kiện` · `ghi chú quan sát` · `ghi chú diễn giải (tách riêng)`. Mẫu đầy đủ ở mục 53.

---

### 47. Cách phân biệt quan sát với diễn giải

| Câu viết kiểu "kể chuyện" | Viết lại: quan sát | Viết lại: diễn giải (gắn nhãn) |
|---|---|---|
| "Smart money hunt stop trên PDH rồi xả" | "High M5 08:35 vượt PDH 4 pip; close 08:40 dưới PDH − δ (E2)" | "[INTERPRETATION] Có thể có stop mua trên PDH bị kích hoạt; ai bán thì không biết" |
| "Giá bị hút về SSL" | "Giá giảm 1.1 ATR H1 trong 3 giờ, tới cách SSL 0.2 ATR" | "[ICT FRAMEWORK] SSL là DOL A; [MATHEMATICAL] baseline = d_đối thủ / (d_SSL + d_đối thủ), lấy từ thẻ DOL" |
| "Engineered liquidity" | "Hai đỉnh H1 lệch 0.05 ATR, cách 7 nến, hồi 0.8 ATR giữa" | "[HYPOTHESIS] có thể là inducement — đã gắn nhãn trước" |
| "Sweep xong rồi, vào thôi" | "Rejection E2 lúc 19:40 VN; chưa có MSS" | "Chưa có REVERSAL CONF.; STALE nếu hết m nến" |
| "Thị trường muốn lên PWH" | "Cấu trúc D1 tăng; PWH cách 1.4 ATR D1" | "[HYPOTHESIS] DOL A = PWH, horizon 2 ngày" |

**Quy tắc viết journal:** câu quan sát trước, nhãn diễn giải sau, **trên hai dòng khác nhau**. Nếu một câu không thể viết lại thành quan sát → nó là diễn giải, phải có nhãn.

---

### 48. Decision tree

![[Liquidity-v2-26-Decision-Tree.svg|900]]

> [!example]- Hình 26 — đọc thế nào
> - **Đang diễn ra gì:** chín câu hỏi theo thứ tự; mỗi nhánh "KHÔNG" là một kết quả hợp lệ (chờ, ghi "chưa rõ", unlisted breach, EXPIRED…).
> - **Mức được đánh dấu:** không áp dụng.
> - **Timeframe:** câu 1–4 trên D1/H1 trước phiên; 5–8 trên H1/M5 trong phiên; 9 sau sự kiện.
> - **Vì sao đáng chú ý:** cây mô tả **thứ tự câu hỏi**, không hứa giá sẽ đi theo trình tự nào.
> - **Đã xác nhận:** —
> - **Chưa biết:** —
> - **Làm gì tiếp:** dùng cây này như checklist khi review một sự kiện đã ghi.

```text
1. Đã xác định bối cảnh cấu trúc (D1)?
   ├─ CHƯA → tiếp tục phân tích, hoặc ghi "chưa rõ" (không giả vờ có bias)
   └─ RỒI ↓
2. Đã khai báo range / phạm vi để phân loại liquidity?
   ├─ CHƯA → làm rõ range, hoặc ghi giới hạn "ERL/IRL chưa xác định"
   └─ RỒI ↓
3. Mức có trong danh sách TRƯỚC khi giá tiếp cận?
   ├─ CHƯA → không tạo mức vì giá vừa chạm → "unlisted breach"
   └─ CÓ ↓
4. Mức có ý nghĩa gì trong cấu trúc hiện tại (Level, ERL/IRL, vai trò)?
   ├─ CHƯA RÕ → theo dõi với độ tin cậy thấp; không dùng làm DOL
   └─ CÓ LÝ DO ↓
5. Giá đã tiếp cận (≤ 1.5·ATR H1, trong killzone)?
   ├─ CHƯA → chờ (NOT READY)
   └─ RỒI → MONITORING, ghi giờ ↓
6. Giá đã xuyên mức (quá L ± ε)?
   ├─ CHƯA → E0/E1 — KHÔNG gọi là sweep
   └─ RỒI → PENDING ↓
7. Trong k nến, hành vi sau khi xuyên?
   ├─ close quay lại qua L ∓ δ trước acceptance  → REJECTED (E2/E3)
   ├─ 2 close liên tiếp bên kia / 1 close cách L > 0.5·ATR → ACCEPTED (E4)
   └─ chưa thỏa gì hết k nến                       → EXPIRED
8. Đủ điều kiện definition để gắn E-code?
   ├─ CHƯA → giữ trạng thái chưa xác định
   └─ CÓ → ghi E-code + known_at ↓
9. Sự kiện có làm đổi cách đọc cấu trúc hoặc DOL?
   ├─ KHÔNG → giữ nhận định cũ (vẫn ghi sự kiện)
   └─ CÓ → cập nhật: gạch mức, DOL state, thêm L', ghi lý do; sự kiện D1 → vẽ lại D1
```

**Ngoại lệ và chú thích cho từng nhánh:**
- **Nhánh 3:** gap qua mức (E5) cũng đi qua bước 3, nhưng ở bước 7 được ghi riêng — không có giao dịch tại L nên không phân xử như wick.
- **Nhánh 5:** tin tier-1 trong cửa sổ → buộc NOT READY dù giá ở gần (điều kiện loại trừ DOL-D2 của DOL v0.2).
- **Nhánh 7:** E6 (thọc nhiều lần) — mỗi lần thọc là một PENDING mới; ghi tất cả, phân loại theo lần cuối trong cửa sổ.
- **Sau nhánh 7 — REJECTED:** lớp xác nhận DEF-LS-06 (MSS Level ≥ 2 + displacement trong m nến) → REVERSAL CONF. hoặc STALE. **Không** phải mọi REJECTED đều cần xác nhận nếu mục đích chỉ là mô tả.
- **Sau nhánh 7 — ACCEPTED:** kiểm tra mức kế cùng phía → có thể RUN (DEF-LS-05).

---

### 49. Các quy tắc nếu–thì (Objective Rules)

> [!info] Hai loại quy tắc
> **[CONSISTENCY]** = quy tắc để phân tích **nhất quán và kiểm chứng được** — không cần backtest để biết nó đúng; nó đúng theo mục đích. **[HYPOTHESIS → BACKTEST REQUIRED]** = quy tắc giao dịch/lọc mà giá trị phải được đo.

**RULE-LQ-001 — Chỉ đánh dấu mức khi có lý do xác định được** [CONSISTENCY]
- *Một câu:* Mỗi mức phải đến từ thuật toán swing (DEF-LQ-05), định nghĩa EQH (DEF-LQ-06) hoặc nhãn thời gian (DEF-LQ-08).
- *Vì sao:* Mức "nhìn bằng mắt" không tái lập được.
- *Đúng:* "BSL 1.0912 = PDH, known 17:00 NY." *Sai:* "Có vẻ có liquidity quanh 1.0915."
- *Ngoại lệ:* Số tròn — được phép nếu khai báo trước rằng số tròn là một loại mức.
- *Ghi trên chart:* nhãn đầy đủ (mục 45). *Kiểm tra:* hai người dùng SOP độc lập trên cùng chart → tỷ lệ trùng danh sách (HYP-LQ-009).

**RULE-LQ-002 — Khai báo timeframe và range trước khi đánh giá mức độ quan trọng** [CONSISTENCY]
- *Vì sao:* Level và ERL/IRL là quan hệ; thiếu tham chiếu thì nhãn rỗng.
- *Đúng:* "ERL(D1 range 10/01–10/09)". *Sai:* "external liquidity" không kèm range.
- *Ngoại lệ:* Không có. *Kiểm tra:* tỷ lệ nhãn ERL/IRL có tên range trong journal = 100%.

**RULE-LQ-003 — Mức phải được xác định trước khi giá tiếp cận nếu muốn kiểm tra khả năng dự báo** [CONSISTENCY]
- *Vì sao:* Chặn lựa chọn hậu nghiệm (mục 3.4).
- *Đúng:* danh sách khóa 06:30 VN, có ảnh chụp. *Sai:* thêm mức lúc 19:36 sau khi giá vừa xuyên.
- *Ngoại lệ:* L' (cực trị sweep) được thêm **sau** sự kiện, với known_at = close nến phân xử — hợp lệ cho các sự kiện **sau** thời điểm đó.
- *Kiểm tra:* mọi sự kiện trong backtest có `level_known_at < event_time`.

**RULE-LQ-004 — Không gọi một sự kiện là sweep khi DEF-LS-04 chưa được đáp ứng** [CONSISTENCY]
- *Đúng:* "PENDING" lúc wick đang chạy; "E3" sau close quay lại. *Sai:* "sweep!" lúc nến chưa đóng.
- *Ngoại lệ:* Không. *Kiểm tra:* không có nhãn sweep nào có known_at = thời điểm wick.

**RULE-LQ-005 — Không kết luận reversal chỉ vì giá vượt mức rồi quay lại trong thời gian ngắn** [HYPOTHESIS → BACKTEST REQUIRED]
- *Một câu:* Rejection chỉ là sự kiện; muốn coi là ứng viên reversal cần DEF-LS-06 (MSS Level ≥ 2 + displacement trong m nến) **và** không có RUN ACTIVE ngược hướng ở H1.
- *Vì sao:* Case B (mục 25) là phổ biến; rejection đơn thuần có thể chỉ là nhịp hồi.
- *Đúng:* "E2 lúc 19:40 VN, chờ MSS tới 20:10 VN." *Sai:* vào lệnh ngay sau close quay lại.
- *Kiểm tra:* so P(mục tiêu đối diện trước cực trị sweep) − p_null giữa nhóm có/không xác nhận (HYP-LS-001/003).

**RULE-LQ-006 — Swing M5 không tự động thay đổi bối cảnh D1** [CONSISTENCY] (giá trị thực hành: [HYPOTHESIS])
- *Vì sao:* Ý nghĩa thuộc về swing bị phá; D1 chỉ đổi khi có sự kiện ở khung D1.
- *Đúng:* "MSS M5 tăng tại SSL D1 — D1 vẫn giảm cho tới close D1." *Sai:* "M5 đảo rồi, bias hôm nay là tăng."
- *Ngoại lệ:* Chuỗi sự kiện M5 tạo ra swing H1 cấu trúc → cập nhật H1 (không phải D1).
- *Kiểm tra:* số lần đổi bias D1 trong tuần; so kết quả khi tuân thủ / không tuân thủ.

**RULE-LQ-007 — Nhiều DOL tiềm năng → ghi các phương án, không chọn một mục tiêu "chắc chắn"** [CONSISTENCY]
- *Đúng:* thẻ A/B/C có đối thủ, horizon, vô hiệu. *Sai:* "target hôm nay là PWH."
- *Kiểm tra:* 100% thẻ DOL có đối thủ + vô hiệu.

**RULE-LQ-008 — Không đủ thông tin → ghi UNDETERMINED** [CONSISTENCY]
- *Đúng:* "E8 hai phía, không MSS, CPI 08:30 → UNDETERMINED." *Sai:* chọn đại một phía.
- *Kiểm tra:* tỷ lệ UNDETERMINED không bằng 0 (nếu bằng 0 sau 50 phiên, bạn đang ép câu chuyện).

**RULE-LQ-009 — Danh sách tối đa 3–4 mức mỗi phía** [HEURISTIC]
- *Vì sao:* chart đọc được; buộc phải xếp hạng.
- *Ngoại lệ:* Cụm mức sát nhau (≤ 0.10·ATR) đếm là một.
- *Kiểm tra:* so tỷ lệ "sự kiện tại mức không có trong danh sách" khi giới hạn 3 vs 5 mức.

**RULE-LQ-010 — Append-only, mỗi nhãn có known_at** [CONSISTENCY]
- *Đúng:* dòng mới "rejection failed 21:50". *Sai:* sửa dòng 19:40 thành "breakout".
- *Kiểm tra:* lịch sử phiên bản file (Obsidian File Recovery / git) không có sửa dòng cũ.

**RULE-LQ-011 — Trong RUN ACTIVE ngược hướng ở H1, không tìm reversal ở từng mức nhỏ** (= RULE-LS-005) [HYPOTHESIS → BACKTEST REQUIRED]
- *Kiểm tra:* tỷ lệ REV. CONF. thành công trong vs ngoài RUN ACTIVE H1.

**RULE-LQ-012 — Không đặt stop sát cực trị sweep; dùng buffer** (= RULE-LS-004) [HYPOTHESIS → BACKTEST REQUIRED]
- *Vì sao:* cực trị sweep có thể là nơi lệnh mới dồn lại (L', hình 36).
- *Kiểm tra:* phân phối MAE sau entry so với cực trị sweep; tỷ lệ bị quét "vài tick".

**RULE-LQ-013 — Cửa sổ tin tier-1 (−10 → +15 phút): không phân loại, không mở MONITORING mới** [HEURISTIC]
- *Ghi:* `news_spike`; vẽ lại danh sách sau tin.
- *Kiểm tra:* tách nhóm sự kiện trong/ngoài cửa sổ tin.

**Bảng nếu–thì rút gọn:**

| NẾU | THÌ |
|---|---|
| Mức không có trong danh sách bị xuyên | Ghi "unlisted breach"; không gọi sweep |
| Wick xuyên, nến chưa đóng | PENDING; không hành động |
| Close quay lại qua L ∓ δ trong k nến, chưa acceptance | E2/E3 = SWEEP; chờ xác nhận m nến |
| 2 close liên tiếp bên kia, hoặc 1 close cách L > 0.5·ATR | E4 = acceptance; mức cũ spent; kiểm tra mức kế |
| Hết k nến chưa phân xử | EXPIRED |
| Rejection + MSS Level ≥ 2 + displacement trong m nến | REVERSAL CONF. (ứng viên, chưa phải kết quả) |
| Rejection, không xác nhận trong m nến | STALE |
| Close qua cực trị sweep sau REV. CONF. | Thêm dòng "REV. FAILED" |
| Sự kiện D1 qua mức vô hiệu | DOL invalidated → flip (đối thủ đã ghi) |
| Hai phía bị xuyên, không MSS, tin sắp ra | UNDETERMINED; DOL kịch bản C |

---

### 50. Các trường hợp phải giữ trạng thái chưa rõ

![[Liquidity-v2-24-Khong-Du-Bang-Chung.svg|900]]

> [!example]- Hình 24 — đọc thế nào
> - **Đang diễn ra gì:** range M15 hẹp trước CPI; Asia H và Asia L đều bị xuyên rồi close quay lại; không có MSS ở khung có ý nghĩa.
> - **Mức được đánh dấu:** Asia H (BSL), Asia L (SSL), PDH/PDL ở xa.
> - **Timeframe:** M15.
> - **Vì sao đáng chú ý:** cố ép câu chuyện "London quét Asia L nên hôm nay tăng" ở đây là nguồn thua lỗ âm thầm.
> - **Đã xác nhận:** E8 (hai phía).
> - **Chưa biết:** hướng sau tin; DOL nào được chạm trước.
> - **Làm gì tiếp:** ghi UNDETERMINED; vẽ lại danh sách mức ≥ 15 phút sau tin.

**Danh sách trường hợp bắt buộc ghi "chưa rõ":**
1. D1 không có cấu trúc rõ (range chồng chéo, swing Level 4 mâu thuẫn).
2. Range không khai báo được (giá vừa phá biên, chưa có range mới).
3. Hai DOL có bằng chứng tương đương và baseline gần 50%.
4. Sự kiện hết k nến chưa phân xử (EXPIRED).
5. Quét hai phía (E8) không có xác nhận.
6. Cửa sổ tin tier-1, ngày lễ, nửa phiên.
7. Feed chuẩn và feed phụ mâu thuẫn ngay tại mức.
8. Ba khung mâu thuẫn và không có mức nào trong phạm vi.

---

### 50A. Hai mươi hai lỗi phổ biến khi nghiên cứu Liquidity

| # | Lỗi | Vì sao xuất hiện | Dấu hiệu nhận biết | Ví dụ | Cách sửa | Quy tắc chặn | Kiểm tra cách sửa có hiệu quả |
|---|---|---|---|---|---|---|---|
| 1 | Đánh dấu mọi swing thành liquidity quan trọng | Sợ bỏ sót | > 8 đường trên chart | 14 đường H1 (hình 33) | Level ≥ 3 + G1–G5 | RULE-LQ-009 | Tỷ lệ sự kiện tại mức trong danh sách / tổng sự kiện |
| 2 | Nhầm liquidity thị trường với đường kẻ | Cùng một từ | Viết "có nhiều liquidity ở đây" | "Pool dày ở EQH" | Dùng câu đầy đủ mục 2 | Mục 2 | Journal không còn câu "pool dày" không nhãn |
| 3 | Cho rằng mọi EQH/EQL có lượng lệnh lớn | Bài giảng nhấn mạnh EQH | Gọi EQH là "nam châm" | "EQH sẽ bị lấy hôm nay" | EQH là mức Level theo khung; giả thuyết HYP-LQ-002 | DEF-LQ-06 | So tốc độ sau xuyên EQH vs đỉnh đơn |
| 4 | Nhầm BSL/SSL với kháng cự/hỗ trợ | Nền tảng PTKT cổ điển | Bán khi chạm BSL | Short tại PDH khi vừa chạm | Phân xử trước, xác nhận sau | RULE-LQ-004/005 | Tỷ lệ lệnh vào trước nhãn |
| 5 | Phân loại internal/external không xác định range | Thói quen gọi tên | "external" không kèm range | Sweep high M15 gọi là external | Ghi tên range | RULE-LQ-002 | 100% nhãn có range |
| 6 | Chọn DOL sau khi giá đã chạy | Muốn câu chuyện khớp | Thẻ DOL không có giờ khóa | DOL viết lúc 21:00 | Khóa thẻ trước phiên | RULE-LQ-003 | Thẻ có timestamp < giờ phiên |
| 7 | Coi DOL là mục tiêu chắc chắn | Ngôn ngữ "draw" | Không có đối thủ/vô hiệu | "Target PWH" | Thẻ A/B/C | RULE-LQ-007 | Tỷ lệ thẻ đủ trường |
| 8 | Nhầm sweep với breakout | Phân loại tại wick | Nhãn có known_at = giờ wick | "Sweep!" lúc 08:35 | Cửa sổ k nến | RULE-LQ-004 | Không còn nhãn tại wick |
| 9 | Nhầm sweep với run | Không đếm số mức | Gọi một mức là "run" | "Run lấy PDH" | Run cần ≥ 2 mức acceptance | DEF-LS-05 | Nhãn run có L₂ |
| 10 | Cho rằng mọi sweep dẫn đến reversal | Ghi nhớ chọn lọc | Không có Case B trong journal | Chỉ lưu sweep thắng | Ghi mọi sweep; đo tỷ lệ | RULE-LQ-010 | Tỷ lệ Case B > 0 |
| 11 | Coi mọi wick vượt mức có ý nghĩa như nhau | Không đo độ sâu | Không có cột độ sâu | Wick 1 tick = wick 0.8 ATR | Ghi độ sâu/ATR | DEF-LS-04 | Phân tích theo nhóm độ sâu |
| 12 | Không tách sự kiện vừa xảy ra với giả thuyết tiếp theo | Kể chuyện liền mạch | Một câu chứa cả quan sát và dự đoán | "Sweep nên sẽ giảm" | Hai dòng riêng | Mục 47 | Mỗi dòng log có nhãn |
| 13 | Dùng swing M5 đổi cấu trúc D1 | M5 nhìn lâu nhất | Bias đổi nhiều lần/ngày | "M5 MSS → bias tăng" | Sự kiện D1 mới đổi D1 | RULE-LQ-006 | Số lần đổi bias/tuần |
| 14 | Xuống M5 quá sớm | Sốt ruột | M5 mở cả phiên | Theo dõi M5 khi giá cách 3 ATR H1 | STATE A/B/C | DEF-LQ-16 | Thời gian ở M5 / phiên |
| 15 | Đánh dấu quá nhiều mức | Như lỗi 1 | Chart rối | — | Gộp cụm, giới hạn | RULE-LQ-009 | — |
| 16 | Đổi definition giữa các ví dụ | Không có file định nghĩa | ε/δ/k khác nhau mỗi lần | k = 3 hôm nay, 5 hôm sau | Một file tham số v0.1 | Mục 51 | Tham số trong log khớp file |
| 17 | Chỉ lưu những lần giá phản ứng đúng kỳ vọng | Thiên kiến xác nhận | Journal toàn thắng | — | Log mọi mức, mọi sự kiện | RULE-LQ-010 | Tỷ lệ NOT TOUCHED, STALE > 0 |
| 18 | Bỏ qua các lần giá xuyên qua liquidity | Không "đẹp" | Không có E4 trong log | — | Ghi E4/E7 | Mục 26 | Phân bố E-code |
| 19 | Nhìn chart sau khi giá chạy mới quyết định mức nào quan trọng | Review bằng hindsight | Level gán sau | — | Level gán trong danh sách trước phiên | RULE-LQ-003 | Level có known_at |
| 20 | Dùng vài ví dụ đẹp kết luận có lợi thế | Bằng chứng giai thoại | n < 30 | "5/6 lần đúng" | Wilson CI; n ≥ 300 cho chênh 8 điểm % | Mục 55.3 | Báo cáo kèm CI |
| 21 | Cho rằng ICT giải thích được danh tính/ý định | Ngôn ngữ "smart money" | Câu có chủ ngữ "họ" | "Họ quét stop của tôi" | Từ vựng vi cấu trúc | Cách đọc note | Câu có chủ ngữ ẩn danh → nhãn INTERPRETATION |
| 22 | Coi diễn giải hợp lý là bằng chứng thực nghiệm | Câu chuyện mạch lạc | Không có số đo | "Rõ ràng là inducement" | Gắn nhãn + test | Part VIII | Mỗi claim có HYP-id |

---
## PART VIII — VALIDATION

> [!warning] Không kết luận "liquidity có khả năng dự báo" vì nhiều chart quá khứ trông phù hợp
> Chart quá khứ luôn "phù hợp" khi bạn chọn mức sau khi biết kết quả. Part VIII thiết kế cách kiểm chứng **đơn giản, rõ ràng và làm được** với dữ liệu của một trader retail.

### 51. Xây dựng definition vận hành

**Bộ tham số v0.1** — chép nguyên khối này vào đầu mọi file backtest liquidity; **không** đổi giữa chừng. Đổi = version mới + changelog.

```yaml
liquidity_params_version: v0.1   # 2026-10-15
chart_timezone: America/New_York
bar_timestamp: open                # nến "08:35" (M5) mở 08:35, đóng 08:40 — known_at dùng giờ ĐÓNG
day_boundary_fx: "17:00"          # NY
day_boundary_nq: "CME session 18:00-17:00 ET"
feed_reference: "<tên feed chuẩn>"
swing_d1_h1: { method: n_bar_pivot, N: 3 }        # known_at = close nến thứ N sau pivot
swing_m5: { method: directional_change, theta_atr: 0.4, atr_len: 14 }
eqh_eql: { tol_atr: 0.10, min_bars_apart: 3, min_retrace_atr: 0.5, same_tf: true }
zone_width_atr: 0.25              # w của vùng BSL/SSL
significance: { gates: [G1, G2, G3, G4, G5], min_level: 3, max_levels_per_side: 4, cluster_merge_atr: 0.10 }
range_anchor_min_reaction_atr_d1: 1.0   # swing làm biên range D1 phải có phản ứng ≥ 1.0 ATR(D1)
near_miss_exit_atr: 0.5            # E0/E1 đóng hồ sơ khi giá rời mức ≥ 0.5 ATR
asia_range_max_atr_d1: 0.5         # Asia range rộng hơn → hạ độ tin cậy của Asia H/L
round_numbers: { enabled: false, default_level: 3 }   # bật = khai báo trước (RULE-LQ-001)
sessions_ny: { asia: "20:00-00:00", london_kz: "02:00-05:00", ny_am_kz: "07:00-10:00" }
sweep_def_ls_04: { eps_atr: 0.02, delta_atr: 0.25, k_bars: 3, acceptance: "2 consecutive closes beyond L, or 1 close > 0.5 ATR beyond L" }
confirmation_def_ls_06: { mss_min_level: 2, m_bars: 6, displacement_body_atr: 1.0 }   # HEURISTIC
run_def_ls_05: { min_levels: 2, max_retrace_pct: 50 }
monitoring: { range_atr_h1: 1.5, killzone_required: true, news_window_min: [-10, 15] }
reaction_window_W: { m5: 48, m15: 16, h1: 8 }
dol: { reach_atr_d1: 1.5, horizon_days: [1, 2], require_opponent: true, require_invalidation: true }
```

**Khi một khái niệm có nhiều cách định nghĩa hợp lý** (ví dụ sweep: chỉ wick / close trong k / close + displacement — mục 22), quy tắc là: **chọn một cho v0.1, ghi lý do, và giữ các phương án kia làm biến thể cho kiểm định độ nhạy** (robustness). Không lặng lẽ biến định nghĩa do mình chọn thành "luật của ICT".

**Phép thử độ rõ của định nghĩa — inter-rater (HYP-LQ-009):** hai người (hoặc bạn ở hai thời điểm cách nhau ≥ 2 tuần, không xem lại kết quả cũ) dùng SOP này độc lập trên **cùng 30 chart**. Đo:
- tỷ lệ trùng **danh sách mức** (Jaccard ≥ 0.7 là mục tiêu);
- **Cohen's κ** cho E-code của cùng sự kiện (κ ≥ 0.7 là mục tiêu).
Nếu không đạt → định nghĩa chưa đủ rõ để backtest; sửa định nghĩa trước khi đo bất kỳ "edge" nào.

---

### 52. Ghi nhận sự kiện theo thời gian thực

![[Liquidity-v2-27-Vi-Du-Real-Time.svg|900]]

> [!example]- Hình 27 — đọc thế nào
> - **Đang diễn ra gì:** sáu cột T0 → T5: chốt danh sách, giá tới gần, xuyên mức, phân xử, xác nhận, review hôm sau — mỗi cột có "đã biết / chưa biết / hành động".
> - **Mức được đánh dấu:** PDL (ví dụ SSL).
> - **Timeframe:** giờ Việt Nam, mùa hè Mỹ.
> - **Vì sao đáng chú ý:** thông tin của cột sau không được chảy ngược vào cột trước.
> - **Đã xác nhận:** chuỗi trạng thái ARMED → MONITORING → PENDING → REJECTED → REV. CONF. → CLOSED.
> - **Chưa biết:** ở mỗi cột, ghi rõ trong ô "chưa biết".
> - **Làm gì tiếp:** nếu review khiến bạn muốn đổi T0, đổi cho **lần sau** (v0.2) — không sửa hồ sơ lần này.

**Quy trình ghi real-time (forward test):**
1. **T0 (trước phiên):** danh sách mức + thẻ DOL + ảnh chụp có giờ → lưu vào daily note.
2. **Mỗi chuyển trạng thái** (A→B, B→C, C→phân loại): một dòng log có giờ.
3. **Không chỉnh sửa** dòng đã ghi; sai thì thêm dòng "correction: …" có giờ.
4. **Cuối phiên:** đóng mọi sự kiện mở (EXPIRED nếu chưa phân xử); ghi mức không bị chạm.
5. **Review** ở file riêng hoặc mục riêng, sau khi cửa sổ W đã đóng.

---

### 53. Thiết kế journal

**Mẫu một sự kiện liquidity** (giải thích từng trường; chỉ giữ trường cần cho câu hỏi đang kiểm tra):

| Trường | Ý nghĩa / cách điền | Bắt buộc cho |
|---|---|---|
| `date` | Ngày (NY) | mọi câu hỏi |
| `instrument` | EURUSD, NQ1… | mọi |
| `session_tz` | Phiên + múi giờ (ví dụ "NY AM, America/New_York") | mọi |
| `htf_context` | Cấu trúc D1 (một dòng) | dự báo |
| `dealing_range` | Low → High + ngày khai báo | ERL/IRL |
| `liquidity_type` | swing / EQH / EQL / PDH / PDL / PWH / PWL / asia / london / round | mọi |
| `liquidity_tf` | Khung xác nhận mức | mọi |
| `level_price` | Giá L | mọi |
| `level_known_at` | Thời điểm mức được biết | **mọi** (chống hindsight) |
| `reason_selected` | Vì sao vào danh sách (một câu) | mọi |
| `level` | 1–5 | xếp hạng |
| `irl_erl` | IRL / ERL + tên range | ERL/IRL |
| `potential_dol` | Thẻ DOL lúc đó (A/B/C) | DOL |
| `price_location_before` | % trong range; khoảng cách/ATR | dự báo, baseline |
| `first_approach_time` | Giờ vào phạm vi | thời gian |
| `reached` | Có chạm (E1+) không | mô tả |
| `crossed` | Có xuyên (> L ± ε) không | mô tả |
| `returned_across` | Có close quay lại qua L ∓ δ trong k nến | sweep |
| `continued_breakout` | Có acceptance (E4) không | breakout |
| `event_code` | E0–E9 / PND / EXP | mọi |
| `event_known_at` | Close nến phân xử | mọi |
| `depth_atr`, `bars_beyond` | Độ sâu, thời gian bên kia | phân nhóm |
| `related_structural_event` | MSS/BOS (swing nào, Level) + displacement | xác nhận |
| `post_event_behavior` | MFE/MAE (ATR), mức nào chạm trước, trong W nến | kết quả |
| `original_hypothesis` | Giả thuyết trước sự kiện | đánh giá |
| `evidence_for` / `evidence_against` | Ghi cả hai | đánh giá |
| `final_classification` | E-code + CONF/STALE/FAILED | mọi |
| `setup_status` | Không setup / setup theo model X / bỏ qua vì … | ứng dụng |
| `notes_uncertainty` | Những gì chưa biết, cờ (news, feed_conflict, holiday) | mọi |

**Đề xuất trường bổ sung cho frontmatter trade/backtest** (thay bộ trường cũ của note 19; **chưa sửa template** — đề xuất để bạn duyệt):

```yaml
dol_card: "A: SSL EQL D1 1.0780 | opp: BSL PDH 1.0912 | watch: EQH H1 1.0889 | horizon 1d | inval: D1 close + acceptance > 1.0912"
liquidity_level_entry_side: "SSL · PDL · D1 · L4 · IRL(D1 10/01-10/09)"   # mức phía sau stop / nơi xảy ra sự kiện
liquidity_event_code: E2          # E0..E9 | PND | EXP
liquidity_event_known_at: "2026-10-15 08:40 NY"
sweep_confirmation: REV_CONF      # REV_CONF | STALE | NONE
sweep_before_mss: true            # nhóm so sánh ablation
unswept_level_behind_sl_atr_h1: 0.8   # khoảng cách tới mức chưa quét gần nhất phía sau SL (điều kiện loại trừ DOL-D1)
dol_state_at_entry: active        # projected | active | delivered | spent | invalidated | flip
```

> [!note] Mapping với bộ trường cũ (note 19 cũ §12)
> `draw_on_liquidity` → `dol_card` · `liquidity_side`/`liquidity_type`/`liquidity_range` → gộp vào `liquidity_level_entry_side` · `swept_before_entry` → `liquidity_event_code` + `sweep_before_mss` · `sweep_confirmed` → `sweep_confirmation` · `liquidity_target_hit` → tính từ `post_event_behavior`, không ghi tay.

---

### 54. Tránh hindsight bias và look-ahead bias

**Danh sách kiểm tra (bắt buộc cho mọi backtest liquidity):**

1. **Đánh dấu mức trước khi giá tiếp cận** — `level_known_at < event_time` cho 100% sự kiện.
2. **Ghi timestamp** cho danh sách mức và mọi nhãn.
3. **Chỉ dùng thông tin có tại thời điểm đánh giá:**
   - Swing N-bar chỉ tồn tại **sau** N nến (pivot N = 3 trên D1 = trễ 3 ngày). Trong backtest, swing chưa xác nhận **không** được dùng làm mức.
   - **Nến khung cao chưa đóng** không được dùng: lúc 10:30 NY, nến H1 10:00 chưa đóng → không dùng close của nó.
   - **ATR đóng băng** tại nến trước sự kiện.
   - Mức theo thời gian chỉ tồn tại sau khi cửa sổ của nó đóng (Asia H/L sau 00:00 NY).
4. **Không đổi mức đã đánh dấu sau khi biết kết quả** mà không ghi lại thay đổi.
5. **Ghi cả các mức không bị chạm** (mẫu số).
6. **Ghi các sự kiện không phản ứng như kỳ vọng** (Case B, STALE, REV. FAILED).
7. **Không bỏ các trường hợp khó phân loại** — EXPIRED/UNDETERMINED là một nhóm.
8. **Phân biệt "sự kiện không xảy ra" với "xảy ra nhưng không phản ứng"** — E0/E1 khác E2 + STALE.
9. **Range và DOL** được chốt trước phiên; re-map range ghi như sự kiện mới.
10. **Survivorship:** nếu backtest nhiều sản phẩm, giữ cả sản phẩm "không đẹp"; không chọn giai đoạn vì nó cho kết quả tốt.

---

### 55. Thiết kế backtest

#### 55.1 Câu hỏi nghiên cứu (giả thuyết, không phải kết luận)

| # | Câu hỏi | Loại kết luận |
|---|---|---|
| Q1 | Những loại mức (swing / EQH / PDH / Asia…) nào thường được tiếp cận / xuyên trong horizon H — **so với baseline** cùng khoảng cách? | Dự báo |
| Q2 | EQH/EQL có hành vi khác swing đơn (tốc độ sau xuyên, tỷ lệ rejection)? | Mô tả → dự báo |
| Q3 | Mức D1 có hành vi khác mức M5? | Mô tả |
| Q4 | Sweep theo DEF-LS-04 có thường được theo sau bởi chuyển động quay vào range? Bao nhiêu so với baseline? | Dự báo |
| Q5 | Sau khi vượt mức, điều kiện nào gắn với tiếp tục vs quay lại? | Dự báo |
| Q6 | Sự kiện tại HTF POI khác sự kiện giữa range? | Dự báo |
| Q7 | Mức gần ERL khác mức IRL? | Dự báo |
| Q8 | Kết quả có đổi theo phiên, sản phẩm, chế độ biến động? | Độ bền |
| Q9 | Lớp xác nhận (MSS + displacement) có thêm giá trị so với rejection đơn thuần? | Ablation |

#### 55.2 Thiết kế mẫu (ví dụ cho Q4 — hướng dẫn làm được bằng tay hoặc code)

| Mục | Thiết lập v0.1 |
|---|---|
| **Giả thuyết** | HYP-LS-001/003: sau SWEEP (E2/E3) tại mức Level ≥ 3, P(chạm mức đối diện trước cực trị sweep + buffer) > p_null |
| **Quần thể** | Mọi sự kiện xuyên mức trong danh sách (không chọn) |
| **Sản phẩm / thời kỳ** | EURUSD, GBPUSD, XAUUSD, NQ1 · 2023-01 → 2025-12 (in-sample) · 2026 (out-of-sample, **không xem** cho tới khi khóa quy tắc) |
| **Khung** | Danh sách D1/H1; sự kiện M5 |
| **Bao gồm** | Mức qua G1–G5, Level ≥ 3; sự kiện trong killzone |
| **Loại trừ (ghi lại, không xóa)** | Cửa sổ tin tier-1; ngày lễ; tuần roll NQ; feed conflict |
| **"Entry" mô phỏng** | Close nến phân xử (hoặc close nến xác nhận nếu test DEF-LS-06) |
| **"Stop" mô phỏng** | Cực trị sweep + buffer 0.1·ATR(M5) |
| **"Target" mô phỏng** | Mức đối diện gần nhất trong danh sách |
| **Spread/slippage** | Spread thực tế theo phiên của feed + 1 tick slippage cho stop |
| **Biến kết quả** | Chạm target trước stop (0/1); MFE, MAE (ATR); thời gian; R sau phí |
| **Baseline** | p_null = d_stop / (d_stop + d_target) cho từng sự kiện; trung bình trên mẫu |
| **Thống kê** | Tỷ lệ quan sát − p_null trung bình, Wilson CI 95%; bootstrap theo ngày |
| **Độ bền** | Đổi k ∈ {2,3,5}, δ ∈ {0.15,0.25,0.4}·ATR; theo phiên; theo sản phẩm; theo năm |

#### 55.3 Cỡ mẫu

Để phân biệt tỷ lệ 58% với 50% (α = 0.05 hai phía, power 80%) cần khoảng **300 sự kiện** **[MATHEMATICAL]**. Với **30 sự kiện**, một tỷ lệ quan sát 60% có khoảng tin cậy Wilson 95% ≈ **42%–75%** — gần như không nói được gì. Với 100 sự kiện: ≈ 50%–69%. Với 300: ≈ 54%–65%.

#### 55.4 Pseudocode trích xuất sự kiện (implementable)

```python
# Inputs: bars_by_tf (OHLC, NY time), params (mục 51), levels_list builder
for day in trading_days:
    levels = build_levels(day, bars_by_tf, params)          # chỉ dùng dữ liệu có trước day_start
    log_levels(levels, locked_at=day_start)                  # G1..G5, Level, ERL/IRL, known_at
    for bar in m5_bars(day):
        atr = atr_m5.frozen_at(bar.prev)
        for L in levels.active(side=both):
            if L.state == "ARMED" and gapped_beyond(bar.open, L):      # mở phiên đã ở bên kia L
                log_event(L, code="E5", known_at=bar.open_time); L.state = "CLASSIFIED"; continue
            if L.state == "ARMED" and touched_within_eps(bar, L, params.eps * atr):
                L.touches += 1; log_event(L, code="E1", known_at=bar.close_time)   # chạm, không xuyên
            if L.state == "ARMED" and penetrated(bar, L, params.eps * atr):
                L.state, L.j = "PENDING", bar.idx
            if L.state == "PENDING":                                 # phân xử cả chính nến j
                verdict = adjudicate(L, bars_since(L.j), atr, params)   # REJECTED / ACCEPTED / None
                if verdict:
                    log_event(L, code=e_code(verdict, L), known_at=bar.close_time,
                              depth=(L.extreme - L.price) / atr, bars_beyond=bar.idx - L.j)
                    if verdict == "REJECTED":
                        levels.add(new_level(L.extreme, known_at=bar.close_time))   # L'
                    L.state = "CLASSIFIED"
                elif bar.idx - L.j >= params.k:
                    log_event(L, code="EXP", known_at=bar.close_time); L.state = "CLASSIFIED"
    for L in levels.never_touched(): log_event(L, code="NOT_TOUCHED")
# Outcome pass (riêng biệt, sau khi trích xuất xong): MFE/MAE/first-touch trong W nến; p_null cho từng sự kiện
```

**Lỗi thường gặp khi code:** dùng high/low của nến H1 đang chạy; tính ATR có cả nến sự kiện; xác nhận pivot không trễ N nến; lấy PDH theo giờ server broker.

---

### 56. Đánh giá kết quả

**Các tỷ lệ — giải thích bằng lời:**

| Thước đo | Nghĩa đơn giản | Luôn so với |
|---|---|---|
| Tỷ lệ mức được **tiếp cận** | Bao nhiêu % mức trong danh sách được giá tới gần trong horizon | Baseline theo khoảng cách |
| Tỷ lệ mức bị **xuyên** | Bao nhiêu % bị giao dịch qua | như trên |
| Tỷ lệ **quay lại** sau xuyên (E2/E3) | Bao nhiêu % lần xuyên kết thúc bằng rejection | Mô phỏng random walk cùng tham số ε/δ/k |
| Tỷ lệ **tiếp tục** (E4) | Bao nhiêu % thành acceptance | như trên |
| **Thời gian** từ khi xác định tới khi tiếp cận | Mức "chờ" bao lâu | Theo khoảng cách/ATR |
| Khác biệt theo **loại mức / khung / phiên / chế độ biến động** | Có nhóm nào khác hẳn không | Chênh lệch có nằm ngoài CI không |
| **Ổn định ngoài mẫu** | Kết quả in-sample có lặp lại ở dữ liệu chưa dùng không | — |

> [!warning] Tỷ lệ quay lại sau sweep ≠ chiến lược có lợi nhuận
> Một tỷ lệ "70% sweep quay về range" có thể đi kèm R:R xấu, chi phí cao, và stop bị quét trước khi tới target. Kết luận giao dịch cần định nghĩa sự kiện, cửa sổ quan sát, chi phí và tiêu chí kết quả — xem 56.1 bên dưới.

#### 56.1 Ba loại kết luận — không tương đương

![[Liquidity-v2-34-Ba-Loai-Ket-Luan.svg|900]]

> [!example]- Hình 34 — đọc thế nào
> - **Đang diễn ra gì:** ba tầng kết luận: mô tả → dự báo → ứng dụng giao dịch; mỗi tầng cần bằng chứng mạnh hơn.
> - **Mức được đánh dấu:** không áp dụng.
> - **Timeframe:** —
> - **Vì sao đáng chú ý:** không suy ra tầng trên từ tầng dưới.
> - **Đã xác nhận:** —
> - **Chưa biết:** các con số trong ví dụ là **giả định** — chưa có dữ liệu nào trong vault hỗ trợ chúng.
> - **Làm gì tiếp:** mỗi kết luận trong review phải ghi rõ nó thuộc tầng nào.

1. **Mô tả:** giá đã làm gì quanh một mức liquidity?
2. **Dự báo:** một đặc điểm có giúp đoán hành vi tiếp theo **tốt hơn baseline** không?
3. **Ứng dụng giao dịch:** thông tin đó có dùng được trong một hệ thống **có lời sau chi phí** không?

---

### 57. Các giả thuyết cần kiểm chứng (Hypothesis Register)

| ID | Giả thuyết | Biến | Điều kiện test | Kết quả kỳ vọng nếu đúng | Bác bỏ khi | Liên quan | Trạng thái |
|---|---|---|---|---|---|---|---|
| **HYP-LQ-001** | Mức Level ≥ 4 (ERL D1, PDH/PDL) khi bị xuyên có tỷ lệ rejection khác mức Level 2 ở cùng khoảng cách | E-code, Level, d/ATR | Q3/Q7, mọi sự kiện | Chênh lệch ngoài CI | CI chồng nhau ở OOS | HYP-LS-007, HYP-LS-011 | UNTESTED |
| **HYP-LQ-002** | Sau khi xuyên EQH/EQL, giá tăng tốc mạnh hơn sau khi xuyên đỉnh đơn cùng khoảng cách (dấu vết cụm stop) | range nến xuyên/ATR, thời gian tới +0.5 ATR | Q2 | Tốc độ EQH > đơn | Không khác | HYP-LS-006/007 | UNTESTED |
| **HYP-LQ-003** | Tỷ lệ mức được chạm trong horizon H vượt baseline hình học, khác nhau theo loại mức (thời gian vs swing) | touched, d/ATR, loại | Q1 | Tỷ lệ − baseline > 0 cho ít nhất một loại | ≈ 0 mọi loại | HYP-DOL | UNTESTED |
| **HYP-LQ-004** | Rejection tại mức nằm trong HTF POI có P(đối diện trước stop) − p_null lớn hơn rejection giữa range | in_poi, outcome, p_null | Q6 | Chênh lệch dương ngoài CI | Không khác | HYP-LS-004 | UNTESTED |
| **HYP-LQ-005** | DOL chọn theo quy trình (ERL D1, cùng cấu trúc, ≤ 1.5 ATR) được chạm trước đối thủ nhiều hơn baseline | dol_hit_first, p_null | DOL card log | > baseline | ≈ baseline | HYP-DOL-001.. | UNTESTED |
| **HYP-LQ-006** | Kết quả sau sweep khác nhau theo phiên (killzone vs ngoài) | session | Q8 | Khác biệt ổn định qua các năm | Không ổn định | HYP-LS-005 | UNTESTED |
| **HYP-LQ-007** | Số lần test N làm thay đổi xác suất xuyên/acceptance (dấu chưa biết) | N | Q1/Q5 | Có quan hệ đơn điệu | Không quan hệ | LSS biến N | UNTESTED |
| **HYP-LQ-008** | Tuổi mức A ảnh hưởng hành vi (dấu chưa biết) | A (số nến) | Q1 | Có quan hệ | Không | LSS biến A | UNTESTED |
| **HYP-LQ-009** | SOP v0.1 cho danh sách mức tái lập được giữa hai lần đánh dấu độc lập (Jaccard ≥ 0.7, κ ≥ 0.7) | Jaccard, κ | 30 chart | Đạt ngưỡng | Không đạt → sửa định nghĩa | — | UNTESTED |
| **HYP-LQ-010** | Sau sweep, cực trị sweep L' bị xuyên lại trong cùng phiên nhiều hơn baseline (replenishment) | L' touched | Q5 | > baseline | ≈ baseline | HYP-LS-015 | UNTESTED |
| **HYP-LQ-011** | Nhãn ex-ante `waypoint`/`terminus` đúng nhiều hơn ngẫu nhiên | nhãn, outcome | Forward test | Accuracy > tỷ lệ cơ sở | ≈ tỷ lệ cơ sở | note 19 cũ §7.2 | UNTESTED |
| **HYP-LQ-012** | LRLR (không POI ngược chiều chặn) có pullback nông hơn và tới mục tiêu nhanh hơn HRLR | path_resistance, thời gian, độ sâu hồi | DOL log | Khác biệt có ý nghĩa | Không | note 19 cũ §7.3 | UNTESTED |

**Trạng thái có thể:** UNTESTED · TESTING · SUPPORTED · WEAK EVIDENCE · REJECTED · REQUIRES MORE DATA. *"Được ủng hộ bởi vài ví dụ" ≠ SUPPORTED.*

---

### 58. Những giới hạn và câu hỏi nghiên cứu còn mở

**Giới hạn cứng (không backtest nào khắc phục hoàn toàn):**
1. **Không quan sát được lệnh** — mọi câu về pool là suy luận từ OHLC.
2. **Không đọc được ý định** — cùng một wick có thể là kích hoạt stop, dealer hedging, lệnh VWAP khớp nốt, thanh lý đòn bẩy, hay lệnh lớn của một nhà giao dịch đơn lẻ.
3. **Sweep vs breakout chỉ phân biệt được sau cửa sổ k** — luôn trễ.
4. **Thuật toán swing có đánh đổi nhạy ↔ trễ** — không có N/θ "đúng".
5. **Hiệu quả phụ thuộc chế độ thị trường** (biến động, tin, phiên) — kết quả có thể không ổn định qua năm.
6. **Rủi ro không bác bỏ được (unfalsifiable):** nếu mọi kết cục đều được giải thích bằng một khái niệm ICT khác ("pool khác mạnh hơn", "chưa đủ HTF"), khung không còn dự báo gì. Cách chống duy nhất: tiêu chí viết **trước**, kết quả ghi **sau**, đếm **tất cả**.

**Phản biện đáng chấp nhận — và câu trả lời có thể:**

| Phản biện | Đánh giá |
|---|---|
| "Clustering là thói quen con người, không phải ý định tổ chức" | **Chấp nhận.** Không phá hiện tượng (lệnh dồn quanh mức nổi bật), chỉ phá câu chuyện ý định |
| "Niềm tin tự củng cố là đủ giải thích" | **Đúng một phần** — và vẫn giao dịch được: hàm ý mức phổ biến nhất có phản ứng mạnh nhất (kiểm chứng được) |
| "Không chứng minh được nhân quả" | **Đúng.** Giao dịch chỉ cần tương quan ổn định ngoài mẫu — đánh giá liquidity ở chuẩn đó |
| "Thêm bộ lọc nào cũng khớp quá khứ hơn" | **Đúng** — giới hạn số biến, test ngoài mẫu, ablation |

**Câu hỏi nghiên cứu mở:**
- Biến nào trong LSS ([[20-Liquidity-Sweep]] §9.3: T khung, V nhãn phiên/ngày, Q đối xứng, N số lần test, A tuổi…) thực sự mang thông tin? [HYPOTHESIS] có thể chỉ T, V và khoảng cách.
- Tỷ lệ waypoint/terminus đúng của chính bạn là bao nhiêu?
- Sweep có thêm giá trị gì so với MSS đơn thuần (ablation ba nhóm)?
- Hành vi tại mức thay đổi thế nào giữa EURUSD (phi tập trung) và NQ (sàn tập trung)?
- Ngưỡng k, δ tối ưu có ổn định qua năm không, hay chỉ là nhiễu?

---
## PART IX — FINAL SYNTHESIS

### 59. Giải thích toàn bộ Liquidity cho trẻ 5 tuổi

![[Liquidity-v2-35-ELI5-Vach-Ai-Cung-Thay.svg|900]]

> [!example]- Hình 35 — đọc thế nào
> - **Đang diễn ra gì:** một vạch ai cũng thấy (đỉnh cũ); phía sau vạch có nhiều bạn đứng chờ "nếu bóng vượt vạch thì tớ chạy theo"; ở ngay vạch có vài bạn "ai muốn mua thì tớ bán cho"; quả bóng (giá) lăn tới gần.
> - **Mức được đánh dấu:** vạch (L).
> - **Timeframe:** —
> - **Vì sao đáng chú ý:** giải thích vì sao vượt vạch có thể làm bóng bay xa hơn **hoặc** bị đẩy ngược lại.
> - **Đã xác nhận:** ta thấy vạch.
> - **Chưa biết:** có bao nhiêu bạn đứng chờ, họ có bỏ đi không, bóng sẽ làm gì.
> - **Làm gì tiếp:** đọc khung đỏ "chỗ ví dụ không còn đúng" trước khi dùng ví dụ này để giải thích cho người khác.

> *"Trên sân có một cái vạch mà ai cũng nhìn thấy. Nhiều bạn hẹn nhau: 'Nếu bóng lăn qua vạch, tớ sẽ chạy theo.' Vài bạn khác đứng ngay ở vạch, sẵn sàng đá bóng ngược lại. Khi bóng tới vạch, có hai chuyện có thể xảy ra: nhiều bạn cùng chạy và bóng bay xa hơn, hoặc các bạn đứng ở vạch đá bóng quay lại. Mình không đếm được có bao nhiêu bạn đang chờ, nên mình không biết trước chuyện nào sẽ xảy ra — mình chỉ biết **nhìn vào cái vạch**, và **xem bóng làm gì** khi tới đó."*

**Một câu cho người lớn:** *Liquidity là nơi có thể có nhiều người cùng chờ hành động vì họ nhìn cùng một mức giá — nó giúp ta biết NHÌN vào đâu và HỎI gì, không cho ta biết trước giá sẽ đi đâu.*

---

### 60. Một ví dụ bullish từ D1 đến M5

![[Liquidity-v2-31-Vi-Du-Bullish-D1-H1-M5.svg|900]]

> [!example]- Hình 31 — đọc thế nào
> - **Đang diễn ra gì:** D1 tăng (HH/HL), giá hồi về discount gần HL D1; H1 hồi giảm vào mức đó; M5 ghi nhận sweep SSL dưới HL D1 rồi MSS tăng.
> - **Mức được đánh dấu:** BSL range high (DOL), SSL dưới HL D1 (protected low, L4), EQ.
> - **Timeframe:** D1 → H1 → M5 (tỷ lệ giữa các panel không theo thang thật).
> - **Vì sao đáng chú ý:** cùng một mức (HL D1) được theo dõi xuyên suốt ba khung — M5 không tạo mức mới.
> - **Đã xác nhận:** sweep (E2) + MSS M5 + displacement.
> - **Chưa biết:** DOL D1 (range high) có bị chạm không.
> - **Làm gì tiếp:** cập nhật trạng thái; giữ điều kiện vô hiệu D1 (close + acceptance dưới HL D1).

**Diễn biến theo thông tin có được** (ví dụ giả định, không phải giao dịch thật):

| Thời điểm | Khung | Biết gì | Chưa biết gì | Trạng thái |
|---|---|---|---|---|
| T0 06:30 VN | D1 | Cấu trúc tăng; range từ đáy cũ tới range high; giá ở discount; DOL A = BSL range high (+1.3 ATR D1); **đối thủ** = SSL range low (−1.5 ATR D1) → baseline A ≈ 54%; **mức quan sát** (`terminus?`) = SSL dưới HL D1 (−0.4 ATR D1) | Giá tới đâu trước | Thẻ DOL khóa; vô hiệu = D1 close + acceptance dưới HL D1 |
| T1 | H1 | H1 giảm (pullback) vào mức D1; không có mức H1 nào cấp ≥ 3 giữa giá và mức D1 | Phản ứng tại mức | NOT READY → MONITORING khi vào phạm vi trong NY AM |
| T2 | M5 | Nến xuyên SSL; close quay lại trên L + δ | Có xác nhận không | PENDING → REJECTED (E2) |
| T3 | M5 | Close trên swing high M5 Level 2, thân lớn, FVG | Mục tiêu có tới không | REVERSAL CONF. |
| T4 | H1 | — | — | Chờ sự kiện H1 (higher low H1?) để cập nhật setup |

**Bài học của ví dụ:** nếu tại T0 bạn ghi SSL dưới HL D1 (−0.4 ATR) làm **đối thủ**, baseline của DOL A chỉ còn ~24% và cú sweep ở T2 sẽ chấm thẻ **SAI** ngay lập tức — dù diễn biến đúng là kịch bản bạn đang chờ. Đó là lý do DEF-LQ-14 tách **đối thủ** (mức mà chạm trước = thẻ sai) khỏi **mức quan sát** (mức có thể bị quét trước khi đi về DOL). Sự kiện tại mức quan sát (sweep + MSS) là thông tin mới **làm đổi bài toán**: mức quan sát đã bị xuyên rồi rejection (E2), L' được thêm vào danh sách, DOL A vẫn `active` cho tới khi có vô hiệu. Không có gì trong hình chứng minh range high **sẽ** bị chạm.

---

### 61. Một ví dụ bearish từ D1 đến M5

![[Liquidity-v2-32-Vi-Du-Bearish-D1-H1-M5.svg|900]]

> [!example]- Hình 32 — đọc thế nào
> - **Đang diễn ra gì:** gương đối xứng của hình 31 — D1 giảm, giá hồi lên premium gần LH D1; H1 hồi tăng; M5 ghi nhận sweep BSL trên LH D1 rồi MSS giảm.
> - **Mức được đánh dấu:** SSL range low (DOL), BSL trên LH D1 (protected high, L4), EQ.
> - **Timeframe:** D1 → H1 → M5.
> - **Vì sao đáng chú ý:** cấu trúc phân tích giống hệt bullish — chỉ đổi phía.
> - **Đã xác nhận:** sweep (E2) + MSS M5.
> - **Chưa biết:** SSL range low có bị chạm không.
> - **Làm gì tiếp:** vô hiệu D1 = close + acceptance trên LH D1.

**Điểm khác cần lưu ý khi đối xứng hóa:** thị trường không hoàn toàn đối xứng. (1) Với chỉ số cổ phiếu (NQ), các nhịp giảm thường đi kèm biến động tăng mạnh hơn nhịp tăng — hiện tượng bất đối xứng biến động (volatility asymmetry / leverage effect) được ghi nhận rộng rãi trong tài chính thực nghiệm **[MARKET MECHANICS]**; nghĩa là cùng một tham số ATR có thể đo hai phía khác nhau. (2) Sự tập trung lệnh (clustering) **có thể** bất đối xứng theo phía và theo hướng giá — note 30 cũ có trích một bài SSRN về chủ đề này nhưng toàn văn chưa được đối chiếu **[HYPOTHESIS]**. Khi backtest, **tách kết quả theo phía** (BSL vs SSL) trước khi gộp.

---

### 62. Một ví dụ giá vượt liquidity rồi tiếp tục

Dùng hình 16 (Case B) và hình 13 (Run). Kịch bản giả định trên EURUSD H1–M15:

1. **T0:** danh sách có BSL L₁ = swing H1 cũ (Level 3) và L₂ = PDH (Level 4). D1 tăng; DOL A = PDH.
2. **T1 (London):** giá xuyên L₁, close M15 trên L₁, rồi nến sau close lại dưới L₁ − δ → **SWEEP (E3)**. Một trader đọc "lấy BSL rồi giảm" sẽ tìm Short.
3. **T2:** không có MSS M15 Level ≥ 2 trong m nến → **STALE** — rejection không được xác nhận.
4. **T3 (NY AM):** giá quay lên, 2 close trên L₁ → **acceptance (E4)**; ghi thêm "rejection failed" (không sửa dòng T1). Đây mới là breakout; chuyển trạng thái **S1** (sweep → run) chỉ được xác nhận ở T4 khi PDH cũng được chấp nhận.
5. **T4:** giá tới PDH, 2 close trên PDH → E4 tại L₂ → nhãn **RUN** (known_at = close thứ hai trên PDH; giả định nhịp hồi giữa L₁ và PDH < 50% leg trước — nếu không, chỉ ghi E4 tại PDH, không gắn RUN). DOL A delivered.
6. **Bài học:** (a) rejection ≠ reversal; (b) thiếu xác nhận là thông tin; (c) bối cảnh D1 tăng + DOL A phía trên đã cho thấy L₁ có thể là **waypoint** — nếu nhãn `waypoint?` được gắn từ T0, quyết định ở T1 đã rõ hơn.

---

### 63. Một ví dụ DOL bị cập nhật

Hình 25 (mục 32). Tóm tắt các bước bắt buộc khi DOL đổi:
1. Sự kiện vô hiệu xảy ra **ở đúng khung** đã ghi trong thẻ (H1 close + acceptance dưới protected low).
2. Ghi dòng `INVALIDATED` + giờ + sự kiện.
3. Flip sang **đối thủ đã ghi sẵn** — không phát minh mục tiêu mới lúc giữa phiên trừ khi có lý do và ghi rõ.
4. Mọi giao dịch/ý định theo DOL cũ được đánh giá lại theo quy tắc của model (không thuộc note này).
5. Review cuối ngày: dự đoán DOL **sai**, kỷ luật cập nhật **đúng** — hai điểm số riêng.

---

### 64. Một ví dụ không đủ bằng chứng để kết luận

Hình 24 (mục 50). Kết luận đúng: **UNDETERMINED** — E8 (hai phía bị xuyên), không MSS ở khung setup, tin tier-1 sắp ra trong 30 phút tới. Hành động: không trade; ghi đủ sự kiện; vẽ lại danh sách ≥ 15 phút sau tin. Giá trị dài hạn: sau 50 ngày như vậy, bạn sẽ biết những ngày "chưa rõ" thực sự diễn biến ra sao — đó là dữ liệu mà người luôn ép câu chuyện không bao giờ có.

---

### 65. Toàn bộ quy trình trên một trang

![[Liquidity-v2-30-Quy-Trinh-Mot-Trang.svg|900]]

> [!example]- Hình 30 — đọc thế nào
> - **Đang diễn ra gì:** mười bước từ bản đồ D1 tới review, mỗi bước có đầu ra.
> - **Mức được đánh dấu:** —
> - **Timeframe:** bước 1–3 D1; 4–5 H1; 6–7 M5; 8–10 sau sự kiện/cuối phiên.
> - **Vì sao đáng chú ý:** thiếu đầu ra của một bước = chưa được sang bước sau.
> - **Đã xác nhận:** —
> - **Chưa biết:** —
> - **Làm gì tiếp:** in ra, dán cạnh màn hình; ba câu nhắc ở cuối hình là phần quan trọng nhất.

---

### 66. Checklist thực hành

**Trước phiên (D1/H1):**
- [ ] Swing D1 (N = 3) Level 4–5 đã xác định
- [ ] Range D1 khai báo (hai biên, ngày, lý do)
- [ ] Danh sách mức: G1–G5, Level ≥ 3, ≤ 4 mỗi phía, cụm đã gộp, có known_at
- [ ] ERL/IRL có tên range
- [ ] Thẻ DOL: A/B/C, đối thủ, horizon, vô hiệu, baseline
- [ ] Mức trên đường đi gắn nhãn `waypoint?` / `terminus?` / `inducement?`
- [ ] Lịch tin tier-1 + cửa sổ cấm
- [ ] Ảnh chụp danh sách + giờ khóa

**Trong phiên (H1 → M5):**
- [ ] Trạng thái A/B/C ghi mỗi lần chuyển
- [ ] Chỉ mở M5 ở B/C
- [ ] Không phân loại tại wick (PENDING)
- [ ] Phân xử trong k nến → E-code + known_at
- [ ] Xác nhận trong m nến → REV. CONF. / STALE
- [ ] Thêm L' sau sweep
- [ ] Ghi tách quan sát / diễn giải

**Sau phiên:**
- [ ] Đóng mọi sự kiện mở (EXPIRED)
- [ ] Ghi mức không bị chạm
- [ ] Cập nhật DOL state
- [ ] Trả lời 6 câu tổng hợp (mục 44, bước 4)
- [ ] Không sửa log; mọi điều chỉnh định nghĩa → ghi cho version sau

---

### 67. Danh sách definition đã được xác định

| ID | Tên | Nội dung tóm tắt | Mục |
|---|---|---|---|
| DEF-LQ-01 | Market liquidity | Giao dịch nhanh, rẻ, ít tác động giá; tightness/depth/resiliency/immediacy | 1 |
| DEF-LQ-02 | Liquidity reference level | Mức ex-ante nổi bật, phía bên kia có thể có lệnh có điều kiện (= DEF-LS-01) | 1 |
| DEF-LQ-03 | Buy-Side Liquidity | Mức trên giá + vùng [L, L + 0.25·ATR] | 7 |
| DEF-LQ-04 | Sell-Side Liquidity | Mức dưới giá + vùng [L − 0.25·ATR, L] | 8 |
| DEF-LQ-05 | Swing high/low | N-bar N = 3 (D1, H1); DC θ = 0.4·ATR (M5); known_at sau xác nhận | 9 |
| DEF-LQ-06 | EQH/EQL | Cùng khung; Δ ≤ 0.10·ATR; ≥ 3 nến; hồi ≥ 0.5·ATR | 10 |
| DEF-LQ-07 | Internal/External | Quan hệ mức – range đã khai báo; mặc định range D1 | 11 |
| DEF-LQ-08 | Mức theo thời gian | PDH/PDL, PWH/PWL, Asia 20–00, London 02–05, NY AM 07–10 (NY) | 13 |
| DEF-LQ-09 | Significant liquidity | G1–G5 + Level ≥ 3 | 14 |
| DEF-LQ-10 | Liquidity event | Tương tác giá – mức trong danh sách, phân loại E0–E9/PND/EXP | 26 |
| DEF-LQ-11 | Liquidity sweep | = DEF-LS-04 (ε 0.02, δ 0.25, k 3) | 22 |
| DEF-LQ-12 | Liquidity run | = DEF-LS-05 (≥ 2 mức acceptance, hồi < 50%) | 23 |
| DEF-LQ-13 | Breakout / acceptance | E4: 2 close liên tiếp bên kia, hoặc 1 close cách L > 0.5·ATR | 24 |
| DEF-LQ-14 | DOL | Thẻ có range, mức chưa tiêu Level ≥ 4, đối thủ, horizon, vô hiệu, tầm với, trạng thái con lắc | 28 |
| DEF-LQ-15 | Post-liquidity reaction | MFE/MAE, thời gian, first-touch, xác nhận trong W nến, so baseline | 25 |
| DEF-LQ-16 | Trạng thái theo dõi | NOT READY / MONITORING (≤ 1.5·ATR H1 + killzone) / EVENT | 39 |
| *(dùng lại)* DEF-LS-06 | Reversal confirmation | REJECTED + MSS Level ≥ 2 + displacement trong m nến | 22, 48 |
| *(dùng lại)* DEF-LS-07 | Run end | Rejection ở mức kế / MSS ngược / hết cửa sổ | 23 |

---

### 68. Danh sách giả thuyết chưa được kiểm chứng

Toàn bộ ở **Hypothesis Register (mục 57)**: HYP-LQ-001 → HYP-LQ-012, tất cả **UNTESTED**. Thêm vào đó, các mệnh đề **từ các note cũ** được hạ xuống thành giả thuyết (không xóa — chờ dữ liệu):

| Mệnh đề cũ | Trạng thái mới |
|---|---|
| "Reversal có chất lượng gần như luôn có sweep trước" | [HYPOTHESIS] — đo bằng ba nhóm (HYP-LS-010) |
| "Equal highs/lows hiếm khi xuất hiện tình cờ — chúng được engineer" | [INTERPRETATION]; EQH xuất hiện trên random walk (LS-Sim-07). Muốn dùng → gắn nhãn ex-ante |
| "Asia tạo, London quét, NY giao" | [ICT FRAMEWORK] khuôn mẫu; tần suất theo phiên → HYP-LQ-006 |
| "Thời gian giá ở lại vùng pool tỷ lệ nghịch với xác suất reversal" | [HYPOTHESIS] — đo bằng tham số m và trạng thái STALE |
| "Pool khung cao luôn thắng pool khung thấp (seniority)" | [HYPOTHESIS] — HYP-LQ-001/005 |
| "LRLR chạy nhanh, HRLR giật cục" | [HYPOTHESIS] — HYP-LQ-012 |
| "Stop ngay ngoài đáy sweep là an toàn nhất" | Ngược lại có thể đúng (L' — replenishment) → RULE-LQ-012, HYP-LQ-010 |

---

## Phụ lục A — Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Liquidity là **khung quan sát**. Quyết định giao dịch thuộc về model đã kiểm chứng ([[01 - ICT 2022 Model]]) và bộ quy tắc rủi ro của vault (≤ 0.5% mỗi lệnh).

**A. Context (HTF)**
- [ ] Bản đồ D1 + thẻ DOL khóa trước phiên (có đối thủ, horizon, vô hiệu)
- [ ] Mức liên quan tới setup có trong danh sách (G1–G5, Level ≥ 3)
- [ ] Biết mức đó là ERL hay IRL của range D1, và là waypoint hay terminus (nhãn ex-ante)
- [ ] Không có RUN ACTIVE ngược hướng ở H1

**B. Sự kiện (LTF)**
- [ ] Sự kiện đã được **phân xử** (E-code + known_at) — không hành động tại wick
- [ ] Nếu là rejection: có xác nhận DEF-LS-06 trong m nến
- [ ] Không trong cửa sổ tin tier-1
- [ ] Không có mức chưa quét trong 0.5·ATR(H1) phía sau stop (điều kiện loại trừ DOL-D1 — [[13-Mistake-Trading-Into-Unswept-Liquidity]])
- [ ] Stop có buffer so với cực trị sweep (RULE-LQ-012)

**C. Quy tắc "không có lệnh"**
- [ ] DOL "chưa rõ" → không trade theo framework
- [ ] Sự kiện EXPIRED / UNDETERMINED → không trade
- [ ] Acceptance (E4) qua mức vô hiệu → không tìm reversal tại đó

---

## Phụ lục B — Tự kiểm tra, flashcards, bài học

### B.1 Câu hỏi tự kiểm tra

- Tôi có giải thích được hai nghĩa của "liquidity" trong 30 giây không?
- Vì sao BSL nằm trên và gồm lệnh mua — và vì sao điều đó **không** nói giá sẽ đi lên?
- Mức này có trong danh sách **trước** khi giá tới không? known_at là gì?
- Mức này ERL hay IRL — của range nào?
- Sự kiện này là E mấy? known_at của nhãn là lúc nào?
- Tôi đang **mô tả**, **dự báo**, hay **ứng dụng**?
- Baseline hình học cho cặp DOL – đối thủ hôm nay là bao nhiêu?
- Khung nào có thẩm quyền đổi bối cảnh đang dùng?

### B.2 Flashcards / Active Recall

**Q1.** Liquidity trên chart ICT "thực sự" là gì?
**A1.** Một mức tham chiếu ex-ante mà phía bên kia **có thể** có lệnh có điều kiện; pool là suy luận, không đo được từ OHLC.

**Q2.** BSL nằm ở đâu, gồm lệnh gì, và ai được lợi khi nó bị kích hoạt?
**A2.** Trên đỉnh tham chiếu; lệnh MUA có điều kiện (stop của short, buy-stop breakout, thanh lý short) + lệnh bán chờ; người cần BÁN lượng lớn có đối ứng.

**Q3.** SSL khác "hỗ trợ" ở điểm nào?
**A3.** Hỗ trợ dự đoán giá dừng; SSL là giả thuyết về lệnh bán nằm ngay dưới — giá có thể thủng qua chính vì các lệnh đó.

**Q4.** Điều kiện EQH v0.1?
**A4.** Hai swing cùng khung đã xác nhận; Δ ≤ 0.10·ATR(14); cách ≥ 3 nến; hồi ≥ 0.5·ATR, không close vượt; L = max; known_at = swing thứ hai.

**Q5.** Vì sao "internal/external" không có nghĩa nếu không ghi range?
**A5.** Vì đó là quan hệ mức – range; đổi range thì đổi vai.

**Q6.** Sweep theo DEF-LS-04 cần gì? known_at là lúc nào?
**A6.** Xuyên L + ε, rồi trong k nến có close quay lại qua L − δ trước acceptance; known_at = close nến phân xử.

**Q7.** Sweep, run, breakout khác nhau ở đâu?
**A7.** Cách phân xử (rejection vs acceptance) và số mức (một vs ≥ 2).

**Q8.** Bốn tình huống bắt buộc của Part IV?
**A8.** A sweep → đảo; B sweep → tiếp tục; C chạm không xuyên; D MSS không sweep.

**Q9.** Một thẻ DOL hợp lệ có những gì?
**A9.** Range D1, mức chưa tiêu Level ≥ 4, đối thủ, horizon, vô hiệu, tầm với ≤ 1–1.5 ATR D1, trạng thái con lắc; được phép "chưa rõ".

**Q10.** Khi nào chuyển H1 → M5?
**A10.** MONITORING: giá trong 1.5·ATR(H1) của mức + killzone + ngoài cửa sổ tin; hoặc EVENT: mức đang bị xuyên.

**Q11.** Vì sao 78% "giá lấy liquidity gần trước" có thể không chứng minh gì?
**A11.** Vì baseline hình học (gambler's ruin) với tỷ lệ khoảng cách 1:3 đã là 75%.

**Q12.** Cần khoảng bao nhiêu sự kiện để phân biệt 58% với 50%?
**A12.** Khoảng 300 (α 0.05, power 80%); 30 sự kiện cho CI ~42%–75% quanh 60%.

### B.3 Lesson Learned

**Bài học chính**
- Liquidity trả lời "nhìn vào đâu và hỏi gì", không trả lời "giá sẽ đi đâu".
- Mức phải có **trước**; nhãn sự kiện có **known_at**; nhật ký **append-only**.
- Sweep là **sự kiện đã phân xử**; reversal là **giả thuyết cần xác nhận**; kết quả là **dữ liệu ex-post**.
- "Chưa rõ" là kết luận hợp lệ và là dữ liệu.
- Mọi tỷ lệ phải trừ baseline trước khi gọi là edge.

**Quy tắc cá nhân rút ra**
- [ ] Tôi không vẽ thêm mức trong phiên (ngoại trừ L' sau sweep, có known_at).
- [ ] Tôi không gọi "sweep" trước khi nến phân xử đóng.
- [ ] Tôi không đổi bias D1 vì M5.
- [ ] Tôi ghi cả mức không bị chạm và sweep không đảo chiều.
- [ ] Tôi viết câu quan sát trước, câu diễn giải sau.

**Câu nhắc nhở khi trade**
> **"Mức có từ TRƯỚC không? Sự kiện đã PHÂN XỬ chưa? Tôi đang MÔ TẢ hay DỰ BÁO?"**

### B.4 Mức độ thành thạo

| Tiêu chí | Điểm 1–5 | Ghi chú |
|---|---:|---|
| Phân biệt hai nghĩa của liquidity |  | Có viết journal bằng ngôn ngữ quan sát không? |
| Lập danh sách mức theo G1–G5 + Level |  | Inter-rater với chính mình sau 2 tuần? |
| Phân loại sự kiện bằng E-code đúng thời điểm |  | Có nhãn nào known_at = giờ wick không? |
| Đặt mức vào cấu trúc / range / premium-discount |  | Có đếm trùng thông tin không? |
| Thẻ DOL + cập nhật trạng thái |  | Tỷ lệ thẻ đủ trường; kỷ luật flip |
| D1 → H1 → M5 đúng cổng |  | Thời gian ở M5 khi STATE A? |
| Backtest có baseline + CI |  | n, Wilson CI, OOS |

**Kế hoạch review tiếp theo:**
- [ ] Inter-rater test HYP-LQ-009 trên 30 chart (trước mọi backtest khác).
- [ ] Event study Q4 (sweep → quay lại) với baseline p_null, 2 sản phẩm.
- [ ] Ablation ba nhóm (sweep + MSS / sweep only / MSS only) — HYP-LS-010.
- [ ] Forward test 20 phiên với thẻ DOL khóa trước phiên.

---

## Phụ lục C — Nhật ký hợp nhất OLD → NEW

> [!info] Quy ước versioning
> Theo nguyên tắc của project: không đổi quy tắc một cách lặng lẽ. Mỗi thay đổi ghi **OLD → NEW → LÝ DO → TÁC ĐỘNG KỲ VỌNG → CẦN BACKTEST?**. Bản gốc ba note nằm trong `02 - Trading Knowledge/_Archive/` (đuôi `.md.bak`).

### C.1 Đã giữ và tích hợp

| Từ note | Nội dung giữ lại | Ở đâu trong note này |
|---|---|---|
| 19 | Bản đồ liquidity trước phiên; câu hỏi "ai kẹt ở đây, stop của họ ở đâu" | Mục 44, 45 |
| 19 | Terminus vs waypoint | Mục 31 (thành nhãn ex-ante) + HYP-LQ-011 |
| 19 | LRLR / HRLR | Mục 23 + HYP-LQ-012 |
| 19 | Inducement trước POI, "liquidity ladder" | Mục 20 (thành quy trình 3 bước) |
| 19 | Đọc phản ứng sau khi pool bị lấy (sponsorship) | DEF-LS-06 / STALE (mục 22, 48) |
| 19 | Bản đồ phiên Asia/London/NY | Mục 13 (giờ theo [[18-Kill-Zones]]) |
| 07 | Hai nguồn buy-stop; "BSL không phải là gì"; bảng trọng lượng | Mục 7, 14 |
| 07 | Ba bước lọc khi dày đỉnh (hiệu lực, gộp cụm, xếp khung) | Mục 14 |
| 07 / 30 | Đối chiếu Wyckoff / AMT / footprint | Mục 21 |
| 30 | Nguồn học thuật về clustering, price cascade, self-fulfilling S/R | Mục 3.2, Phụ lục D |
| 30 | Phản biện falsifiability và bảng "phản biện của phản biện" | Mục 58 |
| 30 | Edge cases EC1–EC12 (mở rộng thành EC1–EC14) | Phụ lục C.3 |

### C.2 Đã sửa (OLD → NEW)

| # | OLD | NEW | Lý do | Tác động kỳ vọng | Backtest? |
|---|---|---|---|---|---|
| 1 | "Liquidity là cụm lệnh chờ mà thị trường — vận hành như thuật toán — bị hút tới để fill khối lượng của smart money" | Liquidity reference level (DEF-LQ-02); pool là suy luận; "thuật toán / smart money" là câu chuyện [ICT FRAMEWORK] | Ý định và khối lượng không quan sát được từ chart | Bớt đọc chart theo câu chuyện | Không |
| 2 | "Sweep gần như luôn xảy ra trước một reversal có chất lượng" | [HYPOTHESIS]; ba nhóm sweep+MSS / sweep / MSS | Case D tồn tại; chưa có số đo | Không bỏ qua MSS không sweep | **Có** (HYP-LS-010) |
| 3 | "Không bao giờ vào lệnh khi liquidity đối diện entry chưa được lấy" | Giữ như **cổng rủi ro** (DOL v0.2 — điều kiện loại trừ DOL-D1: không có mức chưa quét trong 0.5·ATR H1 sau SL), không phải "luật thị trường" | Đây là quy tắc quản trị rủi ro, giá trị phải đo | Giữ kỷ luật Mistake 13 | **Có** |
| 4 | "EQH/EQL hiếm khi tình cờ — engineered" | EQH xuất hiện cả trên random walk; "engineered" là nhãn ex-ante cần đếm | Mô phỏng LS-Sim-07 | Bớt tự tin giả | **Có** |
| 5 | Dung sai EQH theo pip/tick | 0.10 × ATR(14) cùng khung | Một quy tắc cho mọi sản phẩm/chế độ biến động | Tái lập được | Độ nhạy tol |
| 6 | "Sweep = wick qua mức + reclaim + displacement" (gộp) | Sweep = DEF-LS-04 (không gồm displacement); xác nhận = DEF-LS-06 | Tách sự kiện khỏi xác nhận để đo từng lớp | Ablation được | **Có** |
| 7 | "Asia tạo, London quét, NY giao" như trình tự | Khuôn mẫu [ICT FRAMEWORK]; tần suất là HYP-LQ-006 | Không có số đo | Không ép câu chuyện theo giờ | **Có** |
| 8 | Frontmatter `swept_before_entry`, `liquidity_range`… | `dol_card`, `liquidity_event_code`, `sweep_before_mss`… (mục 53) | Ghi theo sự kiện đã phân loại | Dữ liệu dùng được cho ablation | — |
| 9 | Ví dụ chart PNG cũ (Liquidity-Example-*, Sell-side Liquidity-Example-*, Buy-side-Liquidity-Example-*) | Thay bằng 37 hình `Liquidity-v2-*` | Ảnh cũ là minh họa tổng hợp (không phải chart thật), có chỗ khó đọc (ví dụ vị trí nhãn SL trong ảnh SSL-Wrong) | — | — |

### C.3 Edge cases thực chiến (gộp từ note 19/07/30 — mô tả cơ chế, không phải dữ liệu giao dịch của bạn)

| # | Edge case | Vì sao bẫy | Cách xử lý (v0.1) |
|---|---|---|---|
| EC1 | **Feed lệch** — CFD vs sàn gốc khác vài tick ở đỉnh/đáy | Một feed "đã sweep", feed kia "chưa chạm" | Một feed chuẩn; ghi `feed_source`; cờ `feed_conflict` |
| EC2 | **Gap mở phiên/tuần qua mức** | Trông như sweep trên D1 | E5 riêng; chờ cấu trúc nội phiên |
| EC3 | **Sweep nhiều tầng** (mức nông rồi mức sâu cùng phía) | Vào ở tầng một bị dừng | Hỏi "còn mức sâu hơn cùng phía chưa bị lấy?" — HYP-LS-015 |
| EC4 | **MSS giả trong chính cú sweep** (LTF) | Wick tạo swing mới | MSS phải có close + thân + swing Level ≥ 2 |
| EC5 | **Phiên mỏng** (lễ, NY lunch, cuối năm) | Thiếu dòng lệnh đối ứng | Giảm/bỏ; không nới ngưỡng |
| EC6 | **Tin tier-1 xuyên nhiều mức** | Thang biến động đổi | Không phân loại trong cửa sổ; vẽ lại sau tin |
| EC7 | **Thanh lý dây chuyền (crypto/đòn bẩy cao)** | Xuyên xa mọi mức lý thuyết | Không dùng buffer kiểu FX; chờ biến động co lại |
| EC8 | **Mức bị test 3+ lần** | Lệnh ở mức có thể đã bị tiêu | Ghi N; HYP-LQ-007 |
| EC9 | **Stop sát cực trị sweep** | L' là nơi lệnh mới dồn | Buffer; bỏ lệnh nếu R:R không đạt (RULE-LQ-012) |
| EC10 | **Tương quan chồng rủi ro** (EURUSD + GBPUSD cùng phía) | Hai lệnh = một rủi ro USD | Tính rủi ro gộp |
| EC11 | **Rollover / DST** làm PDH/PDL "nhảy" | Mức giả | Quy ước mốc ngày cố định; G5 |
| EC12 | **Sweep "đúng" nhưng không có entry** (giá đi thẳng) | Cảm giác "bỏ lỡ" | Kết quả bình thường; ghi tần suất bỏ lỡ |
| EC13 | **Inducement nhiều tầng trước POI HTF** | MSS nhỏ sau tầng một trông như xác nhận | Đo khoảng cách còn lại tới mép POI; nhãn ex-ante |
| EC14 | **Fractal conflict** — D1 đúng, LTF sweep liên tiếp không MSS | Thử lại mỗi lần sweep nhỏ | Hai lần STALE liên tiếp → về H1 |

### C.4 Đã bỏ (không mang sang)

| Nội dung | Lý do bỏ |
|---|---|
| Các "Case Studies" có giá, ngày, R cụ thể trong note 19 (NQ 22/05, EURUSD 09/09, XAUUSD 03/10, BTCUSD 18/06) và note 07 (GBPUSD, XAUUSD, EURUSD, BTCUSD) | Không truy được về file trade/backtest nào trong vault; theo CLAUDE.md *"Don't fabricate trade data"*. Note 30 cũ cũng đã ghi rõ phần này "không thể viết thay bạn". **Nếu đó là giao dịch thật của bạn**, bản gốc vẫn trong `_Archive` — hãy chuyển chúng thành note trade/backtest có ảnh chụp, rồi liên kết lại vào đây |
| "War Stories" kể ở ngôi thứ nhất trong note 19/07 | Cùng lý do |
| Câu "cộng đồng quant độc lập khi mã hóa sweep thường cho kết quả cận biên hoặc âm" | Không có nguồn; thay bằng kết quả mô phỏng có ghi nhãn [SIMULATION] của [[20-Liquidity-Sweep]] |
| Bảng con số Osler "~5 lần/ngày vs ~1 cascade/tuần" (note 30) | Chính note 30 ghi chưa đối chiếu toàn văn; chỉ giữ phát hiện định tính |
| Khẳng định về dealer gamma hedging như cơ chế mặc định | Giữ ở mức [INTERPRETATION]; không phải cơ chế mặc định (chưa có hàng riêng trong bảng mục 3.3 — gần nhất là cơ chế E/F) |

---

## Phụ lục D — Nguồn tham khảo

**Market microstructure (Tier 1–2):**
- Kyle, A. S. (1985). *Continuous Auctions and Insider Trading.* Econometrica, 53(6), 1315–1335. — ba chiều của liquidity (tightness, depth, resiliency).
- Harris, L. (2003). *Trading and Exchanges: Market Microstructure for Practitioners.* Oxford University Press. — loại lệnh, cung cấp/tiêu thụ thanh khoản, immediacy.
- Bouchaud, J.-P., Bonart, J., Donier, J., Gould, M. (2018). *Trades, Quotes and Prices: Financial Markets Under the Microscope.* Cambridge University Press. — impact, metaorder.
- Osler, C. L. (2003). *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.* Journal of Finance, 58(5). (Bản working paper: [NY Fed Staff Report 125](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.html)).
- Osler, C. L. (2005). *Stop-Loss Orders and Price Cascades in Currency Markets.* Journal of International Money and Finance, 24(2). DOI `10.1016/j.jimonfin.2004.12.002`. (Bản working paper: [NY Fed Staff Report 150](https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr150.html)).
- Garzarelli, F., Cristelli, M., Pompa, G., Zaccaria, A., Pietronero, L. (2014). *Memory effects in stock price dynamics: evidences of technical trading.* Scientific Reports, 4, 4487. DOI `10.1038/srep04487` ([arXiv 1110.5197](https://www.arxiv.org/abs/1110.5197)).
- Kavajecz, K. A., Odders-White, E. R. (2004). *Technical Analysis and Liquidity Provision.* Review of Financial Studies, 17(4).
- Brunnermeier, M. K., Pedersen, L. H. (2005). *Predatory Trading.* Journal of Finance, 60(4).
- King, M. R., Osler, C. L., Rime, D. (2012). *Foreign Exchange Market Structure, Players, and Evolution.* (Handbook of Exchange Rates / working paper).
- *Limit Order Clustering and Price Barriers on Financial Markets: Evidence from Euronext.* SSRN, DOI `10.2139/ssrn.966454` (trích qua note 30 cũ).
- *Price Clustering Asymmetries in Limit Order Flows.* SSRN, DOI `10.2139/ssrn.2613532` (trích qua note 30 cũ).
- *Tick size reduction and price clustering in a FX order book* ([arXiv 1307.5440](https://ar5iv.arxiv.org/html/1307.5440)).

**Lịch sử / thực hành (Tier 3):**
- Connors, L. A., Raschke, L. B. (1995). *Street Smarts: High Probability Short-Term Trading Strategies.* — chiến lược "Turtle Soup" mà ICT dùng lại tên.
- ICT (Michael J. Huddleston) — mentorship video; không trích nguyên văn. Cách hiểu cộng đồng: Tier 3–4.

**Trong vault (định nghĩa dùng lại):** [[20-Liquidity-Sweep]] (DEF-LS-01…08, RULE-LS-001…010, HYP-LS-001…018, mô phỏng LS-Sim-01…07) · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]] (bộ quy tắc DOL v0.2) · [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] (N-bar, DC θ) · [[12-Dealing-Range]] · [[18-Kill-Zones]].

---

## Phụ lục E — Liên kết

**Note liên quan trực tiếp:** [[20-Liquidity-Sweep]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[15-Inducement]] · [[21-Liquidity-Void]] · [[33-Turtle-Soup]] · [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] · [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]] · [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] · [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] · [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]

**Cấu trúc & bối cảnh:** [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]] · [[05-BOS-Break-of-Structure]] · [[21-Market-Structure-Shift]] · [[12-Dealing-Range]] · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] · [[37-Re-mapping-Dealing-Range-sau-Displacement]] · [[27-Premium-Discount]] · [[59-Daily-Bias]] · [[60-IPDA-Tai-sao-gia-di-chuyen-Tu-Price-Discovery-den-Price-Delivery]] · [[32-Top-down-Analysis-Multiple-Timeframes]]

**PD arrays & xác nhận:** [[13-FVG-Fair-Value-Gap]] · [[25-OB-Order-Block]] · [[50-Displacement-In-Depth]] · [[02-AMD]] · [[18-Kill-Zones]] · [[42-SMT-Divergence]]

**Model:** [[01 - ICT 2022 Model]] · [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]]

**Mistake liên quan:** [[02-Mistake-Enter-before-liquidity-sweep]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[06-Mistake-Not-Have-Market-Structure-Shift]] · [[09-Mistake-Wrong-daily-bias]]
