---
type: ict-concept
concept: ICT 2022 Model
aliases:
  - ICT 2022 Model
  - ICT 2022
  - 2022 Model
  - ICT Model 2022
  - ICT 2022 Entry Model
tags:
  - trading/ict/concept
  - trading/study
  - trading/deep-dive
  - "#ICT2022"
  - d1-h1-m5
status: developing
category: Entry Model
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - ICT 2022
  - Silver Bullet
  - OTE
  - AMD
  - Unicorn
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 2
last_reviewed: 2026-10-11
created: 2026-06-22
updated: 2026-10-11
prerequisites:
  - "[[59-Daily-Bias]]"
  - "[[12-Dealing-Range]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[20-Liquidity-Sweep]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[50-Displacement-In-Depth]]"
  - "[[13-FVG-Fair-Value-Gap]]"
  - "[[18-Kill-Zones]]"
common_mistakes:
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]"
  - "[[04-Mistake-FOMO-Entry]]"
  - "[[05-Mistake-Not-enough-RR]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[08-Mistake-Weak-Displacement]]"
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
rule_version: ICT2022-Core (D1-H1-M5) v0.2
---

# ICT 2022 Model — Từ bối cảnh D1 đến thực thi M5

> [!summary] Tóm tắt 1 câu
> **ICT 2022 Model là một quy trình lọc tuần tự: D1 cho biết hướng nào được phép xét và giá đang bị hút về đâu → H1 cho biết cơ hội có đang hình thành tại vùng đáng quan tâm không → M5 chỉ trả lời một câu hỏi: tại đúng vùng đó, đúng giờ đó, giá đã để lại đủ bằng chứng (sweep → MSS có displacement → FVG) để đặt một lệnh có entry, stop và target xác định trước hay chưa.**

> [!important] Ba nguyên tắc không được vi phạm
> 1. **Đi từ trên xuống, không đi ngược.** D1 xác định bối cảnh → H1 xác định cơ hội → M5 xác định điều kiện thực thi. Không bao giờ thấy M5 "đẹp" rồi quay lên D1 tìm lý do hợp lý hóa.
> 2. **Mỗi bước chưa đủ điều kiện thì phải nói rõ đang chờ điều gì** — không tự động chuyển sang bước tiếp theo. *Mở M5 để quan sát* khác *được phép vào lệnh*.
> 3. **No Trade là một kết quả hợp lệ — và là kết quả thường gặp nhất.** Một setup "trông đẹp" nhưng thiếu bằng chứng là một setup không tồn tại.

> [!info] Phiên bản mô hình đang nghiên cứu trong note này
> **ICT2022-Core (D1-H1-M5) v0.2** — bốn lớp thành phần (core · bộ lọc của phiên bản · confluence · biến thể) ở [[#3. Toàn cảnh mô hình từ đầu đến cuối|§3]]; định nghĩa đo được ở [[#49. Định nghĩa khách quan (đo được)|§49]]; danh sách quy tắc có version ở [[#62. Danh sách quy tắc đã định nghĩa (rule register)|§62]].

> [!info] Note này đứng ở đâu trong vault — để không lặp thông tin
> | Note | Vai trò | Quan hệ với note này |
> |---|---|---|
> | **Note này** | Tài liệu học & nghiên cứu chính: cơ chế, quy trình D1→H1→M5, ví dụ, failure modes, case study backtest, khung kiểm chứng | Nguồn gốc của thang POI rank, displacement score, confluence score mà template đang dùng |
> | [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] | Đặc tả hình thức: state S0–S13, gate G1/G2 đầy đủ, TTL, reset router, null model, audit 22 lệnh | Note này **tóm tắt và dẫn link**, không chép lại spec |
> | [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]] | Biến thể hạ khung H1→M5→M1 | Cùng logic, đổi tham số khung |
> | [[ICT 2022 Entry Checklist]] · [[ICT 2022 State Machine Gate Checklist]] · [[2022 Model A+ Setup]] | Thẻ thao tác trong phiên | Checklist ở Part VI là bản gốc lý giải; thẻ playbook là bản bấm nhanh |
> | [[Backtest template - POI & Step Decision (ICT 2022)]] | Schema log | Part VII chỉ giải thích *vì sao* có các trường, không chép lại schema |

> [!note] Hệ nhãn bằng chứng dùng trong toàn bộ note
> | Nhãn | Nghĩa | Ví dụ |
> |---|---|---|
> | `[OBSERVABLE]` | Quan sát trực tiếp được từ OHLC/thời gian | "Giá giao dịch dưới đáy cũ rồi đóng nến trở lại bên trên" |
> | `[MARKET MECHANICS]` | Cơ chế khớp lệnh/đấu giá có nền tảng nghiên cứu | "Stop-loss khi bị kích hoạt trở thành lệnh market" |
> | `[ICT FRAMEWORK]` | Cách ICT đặt tên và diễn giải | "Sell-side liquidity bị raid trước khi giá tìm tới buy-side" |
> | `[INTERPRETATION]` | Hợp lý nhưng không chứng minh được từ chart | "Reclaim nhanh cho thấy phía bán đã cạn" |
> | `[HYPOTHESIS]` | Mệnh đề kiểm định được (có mã HYP-xx) | "Setup có sweep có expectancy cao hơn setup không sweep" |
> | `[BACKTEST REQUIRED]` | Không được coi là lợi thế khi chưa có dữ liệu | Mọi nhận định về hiệu quả |
> | `HEURISTIC` | Con số khởi điểm để test, không phải sự thật | "Reclaim trong ≤ 3 nến", "TTL 12 nến" |

> [!info]- Danh mục hình (31 hình mới + 8 hình cũ tái sử dụng)
> | # | Hình | Mục |
> |---|---|---|
> | 1 | Kiến trúc D1 → H1 → M5 | §3 |
> | 2 | Bản đồ thành phố (ELI5) | §4 |
> | 3 | D1 structure & cấp swing STH/ITH/LTH | §6–7 |
> | 4 | Dealing range, EQ, Premium/Discount | §8–9 |
> | 5 | Internal vs External liquidity | §10 |
> | 6 | Xếp hạng DOL | §11 |
> | 7 | Daily Bias 4 trạng thái | §12 |
> | 8 | H1 setup development | §18 |
> | 9 | D1 bullish – H1 bearish correction | §16 |
> | 10 | Ba trạng thái chuyển H1 → M5 | §23 |
> | 11 | Ba tình huống tại thanh khoản | §25 |
> | 12 | Sweep không MSS | §25 |
> | 13 | MSS không sweep | §26 |
> | 14–15 | Chuỗi bullish / bearish đầy đủ | §26, §36–37 |
> | 16 | FVG 3 nến bullish/bearish | §28 |
> | 17 | Displacement 4 tiêu chí | §27 |
> | 18 | Entry E1/E2/E3 | §29 |
> | 19 | Entry hợp lệ nhưng chạm SL | §32, §60 |
> | 20 | Setup vô hiệu trước entry | §29, §60 |
> | 21 | No Trade: M5 đẹp, H1 sai chỗ | §38, §61 |
> | 22 | Giá chạy thẳng không entry | §29, §38 |
> | 23 | Toàn bộ quy trình D1 → H1 → M5 | §35 |
> | 24 | Decision tree | §42 |
> | 25 | Timeline real-time B1–B8 | §50 |
> | 26 | Look-ahead bias | §51 |
> | 27 | Phân tầng invalidation | §32 |
> | 28 | Core vs bộ lọc vs biến thể | §3, §39 |
> | 29 | Xác suất chuỗi thua | §53 |
> | 30 | Tóm tắt 1 trang | §61.1 |
> | 31 | Killzone NY → giờ VN | §39 |

---

## PART I — NỀN TẢNG

### 1. ICT 2022 Entry Model là gì?

**Nguồn gốc** `[ICT FRAMEWORK]`. "ICT 2022 Model" là tên cộng đồng đặt cho mô hình vào lệnh mà Michael J. Huddleston (Inner Circle Trader) trình bày trong loạt **2022 Mentorship** phát miễn phí trên YouTube. Không có một văn bản đặc tả chính thức; mọi "định nghĩa" đều là tóm tắt thứ cấp. Các bản tóm tắt phổ biến mô tả chung một chuỗi ba nhịp **raid → shift → entry**:

1. Giá **quét một pool thanh khoản** dễ thấy (đáy cũ khi tìm long, đỉnh cũ khi tìm short), lý tưởng là đi vào một mục tiêu khung cao.
2. Giá **đổi chiều bằng displacement** — một nhịp mạnh đóng cửa vượt qua swing đối diện gần nhất (**MSS**).
3. Vào lệnh khi giá **hồi về FVG** do nhịp displacement để lại; **stop ngoài cực trị của cú quét**; **target là thanh khoản phía đối diện**.

Theo các bản tóm tắt này, bias và pool thanh khoản được đọc trên khung khoảng 15 phút–1 giờ, còn sweep/shift/retrace được thực thi trên khung 1–5 phút; mô hình thường chạy trong killzone London hoặc New York buổi sáng (bản tóm tắt AI của bài giảng Charter ghi: FX ≈ 07:00–10:00 NY, index ≈ 08:30–11:00 NY — *cần đối chiếu video gốc*), và lệnh limit được đặt **tại mép FVG để chắc chắn được khớp**. Các nguồn tóm tắt cũng tự nhận rằng *cách hiểu "smart money" là diễn giải, và chưa có hồ sơ hiệu quả được kiểm chứng độc lập*.

> [!warning] Hai điều cần thẳng thắn ngay từ đầu
> - **D1 → H1 → M5 là cách BẠN phân rã mô hình**, không phải cấu hình ICT dạy nguyên bản. Bản gốc chủ yếu là một mô hình intraday (bối cảnh ~15m–1h, thực thi 1–5m). Phân rã D1/H1/M5 hợp lý vì mỗi bước của chuỗi giải quyết một loại bất định khác nhau (xem §2), nhưng nó là *thiết kế của người nghiên cứu* — hiệu quả của nó phải được đo riêng.
> - **Chuỗi sweep → MSS → FVG xuất hiện cả trên dữ liệu ngẫu nhiên.** Mô phỏng 100.000 phiên random walk trong [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] (§4.6) cho thấy chuỗi đầy đủ chiều long xuất hiện ở khoảng 1.4% phiên, với kỳ vọng ≈ 0R. Pattern *tồn tại* không chứng minh pattern *có lợi thế*. Thứ bạn phải chứng minh là: **bối cảnh D1/H1 làm lệch phân phối kết quả của chuỗi đó so với null.**

**Định nghĩa dùng trong note này (định nghĩa vận hành):**

> **ICT2022-Core (D1-H1-M5)** = một quy trình ba tầng, trong đó D1 phát hành một *giả thuyết bối cảnh có phạm vi* (hướng được phép, vùng được phép, mục tiêu, mức sai); H1 biến giả thuyết đó thành *một vùng có điều kiện* và quyết định khi nào được quan sát M5; M5 chỉ phát hành lệnh khi *sweep một pool đã đánh dấu trước → MSS phá một swing đã đánh dấu trước bằng thân nến có displacement → FVG* xảy ra theo đúng thứ tự, trong killzone, với R tới target đầu tiên ≥ 2. Mọi bước được đánh giá trên **nến đã đóng** và có **điều kiện vô hiệu** viết ra từ trước.

### 2. Mô hình cố gắng giải quyết vấn đề gì?

| Vấn đề của người học ICT | Mô hình giải quyết bằng cách | Nếu thiếu bước này |
|---|---|---|
| Biết từng khái niệm (FVG, OB, MSS…) nhưng **không biết ghép theo thứ tự nào** | Đặt các khái niệm vào một chuỗi có thứ tự cố định | Thấy FVG là vào; thấy MSS là vào |
| **Entry không có bối cảnh** — mọi chuyển động M5 đều "có thể là setup" | D1 và H1 lọc hướng và vùng trước khi nhìn M5 | Hàng chục "tín hiệu" mỗi ngày, phần lớn là nhiễu |
| **Không biết khi nào mình sai** | Mỗi tầng có invalidation riêng (structure, POI, sweep extreme) | Dời stop, gồng lệnh, đổi lý do giữa chừng |
| **Không kiểm chứng được** | Mỗi bước là một câu hỏi CÓ/KHÔNG trên dữ liệu có timestamp | Backtest đo "người chọn lệnh", không đo mô hình |

**Vì sao thứ tự là D1 → H1 → M5 mà không phải ngược lại.** Mỗi tầng trả lời một loại bất định có *tốc độ thay đổi* và *chi phí khi sai* khác nhau: hướng (chậm, sai thì cả ngày sai phía) → vùng (vừa, sai thì R:R xấu) → thời điểm (nhanh, sai thì một lệnh thua). Cái sai đắt nhất phải được kiểm tra trước, bằng dữ liệu chậm và ít nhiễu nhất. Đảo thứ tự — chọn giả thuyết bằng M5 rồi dùng D1 hợp lý hóa — là lỗi logic, không chỉ là lỗi kỷ luật. (Bảng đầy đủ: [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §2.4.)

`[INTERPRETATION — giả định có drift]` Có một lập luận định lượng cho việc lấy hướng từ khung cao: *nếu* giá có một xu hướng (drift) cường độ μ, phần tín hiệu tăng tuyến tính theo thời gian (μt) còn nhiễu tăng theo căn bậc hai (σ√t), nên trên một horizon dài hơn tỷ lệ tín hiệu/nhiễu cao hơn. D1 nhìn horizon nhiều ngày; một nhịp M5 chỉ là vài chục phút. Lập luận này phụ thuộc vào giả định có drift — chính điều backtest phải kiểm. Hệ quả kiểm định được `[HYPOTHESIS]`: giá trị chính của M5 nằm ở **hình học rủi ro** (stop sát hơn → R lớn hơn), không nhất thiết ở win rate.

### 3. Toàn cảnh mô hình từ đầu đến cuối

![[ICT2022-v2-01-Kien-truc-tong-quan.svg]]

| Bước | Khung | Câu hỏi | Loại bằng chứng | Output |
|---|---|---|---|---|
| Structure, range, liquidity, DOL, bias | D1 | Hướng nào được phép? Giá bị hút về đâu? | **Context** | D1 Context Note |
| HTF POI | D1 | Vùng nào đáng chờ? | **Location** (vĩ mô) | Vùng được phép + mức sai |
| Intermediate structure, H1 liquidity, POI refine | H1 | Cơ hội có đang hình thành? Khi nào được nhìn M5? | **Location** (thực thi) + **timing gate** | H1 Handoff (state) |
| Liquidity sweep | M5 | Nhiên liệu ngược đã bị tiêu thụ chưa? | **Event** | Cực trị sweep (neo SL) |
| MSS + displacement | M5 | Mất cân bằng đã lật chưa? | **Structural + delivery evidence** | Xác nhận |
| FVG + entry rule | M5 | Đặt lệnh ở đâu? | **Execution location** | Execution Plan |
| SL / Target | M5 (target từ H1/D1) | Sai ở đâu? Đúng tới đâu? | **Risk geometry** | R, size |

> [!important] Gọi tất cả là "confirmation" là cách nhanh nhất để không biết mình sai ở đâu
> Bias là *context*, POI là *location*, sweep là *event*, MSS là *structural evidence*, displacement là *delivery evidence*, FVG là *execution location*, entry là *execution rule*. Khi lệnh thua, bạn cần biết **mắt xích nào** hỏng — đó là lý do log có `first_error_step`.

**Bốn lớp thành phần — đừng âm thầm biến bộ lọc thành "luật ICT":**

![[ICT2022-v2-28-Core-vs-Filter-vs-Variant.svg]]

| Lớp | Thành phần | Ai quyết định | Hệ quả khi thiếu |
|---|---|---|---|
| **1. Core** | Bối cảnh + DOL, vùng quan tâm, sweep, displacement + MSS, FVG, entry retrace, SL cực trị sweep, target thanh khoản | Mô tả phổ biến của mô hình | Không phải ICT 2022 Model (Core) |
| **2. Bộ lọc của phiên bản** | Killzone · P/D đồng pha D1↔H1 · R(T1) ≥ 2 · risk ≤ 0.5% · không tin đỏ ±15' | **Bạn** (quy tắc vận hành) | Không trade *trong phiên bản này* |
| **3. Confluence chấm điểm** | POI rank, CE∩OTE, SMT, CISD, macro, NWOG/NDOG, SD, IDM | Bạn (thang 0–8) | Quyết định hạng & size; **tổng 0–1 = No Trade** (giữ theo [[ICT 2022 Entry Checklist]]) — tức lớp này là một cổng mềm, không hoàn toàn tùy chọn |
| **4. Biến thể cộng đồng** | Silver Bullet, Unicorn, entry aggressive, MSS-only, LTF 1m, multi-leg, countertrend | Mỗi biến thể là một spec | Thống kê riêng, không trộn |

### 4. Giải thích cho người mới — năm tầng

#### Level 1 — Cho trẻ 5 tuổi

![[ICT2022-v2-02-Ban-do-thanh-pho-ELI5.svg]]

Hãy tưởng tượng bạn muốn đi tới một cửa hàng trong thành phố.

- **D1 là bản đồ cả thành phố.** Nó cho biết bạn đang đứng ở đâu (giá đang ở phần "rẻ" hay "đắt" của khu vực), và điểm đến lớn là ở đâu (nơi có nhiều lệnh chờ — DOL).
- **H1 là bản đồ một khu phố.** Bạn không đi lang thang khắp thành phố; bạn khoanh đúng khu có cửa hàng muốn vào (POI). Khi chưa tới khu đó, bạn không cần nhìn biển số từng căn nhà.
- **M5 là con đường nhỏ trước cửa hàng.** Ở đây bạn chờ những dấu hiệu cụ thể: xe đi vòng qua bãi xe đông người (quét thanh khoản), rồi rẽ mạnh bỏ hẳn hướng cũ (MSS + displacement), để lại một "ổ gà" (FVG). Bạn chỉ lên xe khi xe quay lại đúng ổ gà đó (entry). Nếu xe lùi qua cả bãi xe — bạn đã đi sai đường (stop loss).

**Giới hạn của phép so sánh:** bản đồ thành phố *không biết trước tương lai* — "điểm đến" chỉ là giả thuyết; con đường nhỏ *không quyết định* hướng của cả thành phố — một khúc rẽ trên M5 không đổi bias D1; và trên chart không có "người lái xe" để đọc ý định — chart chỉ cho thấy giá *đã* đi đâu, không cho thấy *ai* đi và *vì sao*.

#### Level 2 — Chuỗi giá minh họa

```text
D1: cấu trúc tăng, giá đã hồi về nửa dưới (discount) của range, đỉnh range còn nguyên (DOL)
        │   → "chỉ xét LONG, quanh vùng D1 FVG 104–112, sai nếu D1 đóng dưới 92"
        ▼
H1: giá giảm thành LH–LL (nhịp hồi) đi VÀO D1 FVG; đáy H1 106.7 tạo pool SSL
        │   → trạng thái MONITORING: mở M5, đánh dấu trước pool 106.7 và swing high 113.0
        ▼
M5 (killzone NY AM):
   1. giá đâm xuống 105.6 (dưới 106.7) rồi đóng lại trên 106.7   → SWEEP (event)
   2. hai nến tăng thân lớn, đóng sát đỉnh, để lại khoảng trống  → DISPLACEMENT
   3. thân nến đóng 113.4 > 113.0                                → MSS (confirmation)
   4. khoảng trống 111.2–113.1 (CE 112.15)                       → FVG
   5. giá hồi về 112.15 → limit khớp; SL 105.3; T1 126.0 (R≈2)   → ENTRY / RISK
```

Điều thực sự xảy ra ở từng bước: (1) một mức giá dễ thấy bị giao dịch xuyên qua — các lệnh stop/breakout tại đó được khớp; (2) ngay sau đó dòng lệnh một chiều mạnh tới mức có những vùng giá chỉ được giao dịch một lần; (3) điểm khởi đầu của nhịp giảm trước đó bị vượt bằng thân nến — nhịp giảm vừa rồi bị "hoàn trả" toàn bộ; (4) vùng giao dịch một chiều trở thành địa chỉ đặt lệnh; (5) lệnh có mức sai rõ ràng (dưới cực trị cú quét) và mục tiêu rõ ràng (thanh khoản H1 phía trên).

#### Level 3 — Ngôn ngữ ICT

Daily Bias bullish với **draw on liquidity** là buy-side liquidity (BSL) ngoài range D1 → giá ở **discount** và trong **HTF PD array** (D1 FVG) → trên H1, **sell-side liquidity** nội bộ được tạo ra (liquidity engineering) → trong **killzone**, giá **raid SSL**, **displacement** lên phá **market structure** ngắn hạn (MSS) để lại **FVG/BISI** → entry khi **retrace** vào FVG (thường quanh **CE**), stop dưới **swing low vừa quét**, target **internal range liquidity** của range D1 (cũng chính là **external liquidity của range H1**) rồi **external range liquidity** của D1.

#### Level 4 — Trên chart, bạn làm gì

| Thời điểm | Đánh dấu gì | Chờ gì | Quyết định |
|---|---|---|---|
| Trước phiên | D1: ITH/LTH, range + EQ, pool hai phía, DOL, POI, mức sai → viết Context Note | — | Bias / Neutral; được mở H1 hay không |
| Giá hồi về D1 POI | H1: POI refine, SSL/BSL H1, T1 = H1 ERL | Giá vào POI + killzone | NOT READY / MONITORING |
| Vào killzone, giá ở POI | M5: pool sẽ bị quét + swing (ITH) sẽ bị phá — **trước** sự kiện | Sweep → MSS → displacement → FVG | EXECUTION ELIGIBLE → phát hành lệnh hoặc không |
| Sau MSS | FVG, entry theo rule, SL, T1, R, TTL | Giá hồi về mức entry | Khớp / hủy (TTL, +1R, invalid) |

#### Level 5 — Giới hạn

Quan sát trực tiếp được chỉ là: giá xuyên mức rồi quay lại, thân nến đóng vượt swing, khoảng giá chỉ giao dịch một lần, thời điểm trong ngày. Mọi thứ khác — "thanh khoản bị nhắm tới", "bối cảnh làm tăng xác suất", mọi ngưỡng số — là diễn giải hoặc giả thuyết. Bảng phân loại đầy đủ ở §5.

### 5. Những gì mô hình có thể và không thể khẳng định

| Hiện tượng | `[OBSERVABLE]` | `[ICT FRAMEWORK]` | `[INTERPRETATION]` hợp lý | `[HYPOTHESIS]` cần dữ liệu |
|---|---|---|---|---|
| Sweep | Giá giao dịch xuyên một mức cũ rồi đóng lại bên trong | Liquidity raid / stop hunt | Lệnh stop tại mức dễ thấy được khớp, tạo thanh khoản đối ứng | Sau sweep, xác suất đảo chiều cao hơn base rate |
| MSS | Thân nến đóng vượt một swing | Market structure shift | Nhịp ngược chiều trước đó đã bị hoàn trả | MSS sau sweep tốt hơn MSS không sweep (HYP-03) |
| Displacement | Nến thân lớn, ít râu, liên tiếp | Thể hiện "intent" | Dòng lệnh một chiều mạnh hơn bình thường | Displacement mạnh → kết quả tốt hơn (HYP-04) |
| FVG | Khoảng giá chỉ một nến giao dịch | Imbalance, giá "nợ" một lần cân bằng | Thanh khoản mỏng ở vùng đó | Giá hồi về và phản ứng tại FVG nhiều hơn ngẫu nhiên |
| DOL | Các mức đỉnh/đáy cũ, EQH/EQL | Giá bị "hút" về thanh khoản | Mức dễ thấy có thể tập trung lệnh chờ | Primary DOL bị chạm trước mức sai nhiều hơn null |

**Cơ chế thị trường có bằng chứng** `[MARKET MECHANICS]`. Không có nghiên cứu bình duyệt nào kiểm định trực tiếp ICT 2022 Model. Thứ có bằng chứng là các mảnh cơ học bên dưới:
- Trên thị trường FX, lệnh stop-loss và take-profit **co cụm quanh các mức số tròn** và hành xử ngược nhau: stop-loss khi bị kích hoạt trở thành lệnh market *cùng chiều* phá vỡ, nên có thể **khuếch đại** chuyển động (price cascade); take-profit có xu hướng **hãm** chuyển động (Osler 2003, 2005). Việc co cụm quanh *đỉnh/đáy cũ* (thay vì số tròn) là suy rộng hợp lý nhưng không phải điều các nghiên cứu này đo trực tiếp.
- Trên cổ phiếu NYSE, các mức hỗ trợ/kháng cự kỹ thuật **trùng với nơi sổ lệnh giới hạn dày** (Kavajecz & Odders-White 2004) — chưa chắc chuyển nguyên vẹn sang FX/futures.

**Hệ quả quan trọng nhất** `[INTERPRETATION dựa trên cơ chế trên]`: *sweep* và *breakout (run)* là **cùng một sự kiện ban đầu với hai kết cục**. Khi giá chạm cụm stop, các stop được khớp thành lệnh market đẩy giá xuyên mức. Nếu sau khi cụm stop bị tiêu thụ **không có dòng lệnh mới cùng chiều**, mất cân bằng lật lại → giá reclaim (sweep). Nếu cú phá đến từ **thông tin mới**, cascade trở thành nhiên liệu → giá chạy tiếp (run). Chart chỉ phân biệt được hai kết cục **sau vài nến** — bằng reclaim hay acceptance. Đây là lý do mô hình đòi MSS + displacement sau sweep, thay vì vào lệnh ngay tại sweep.

**Narrative ICT và giải thích thay thế** — cùng một chart có thể khớp với nhiều câu chuyện:

![[ICT2022-Advanced-Epistemic-TwoNarratives.svg]]

| Câu chuyện | Nội dung | Có thể phân biệt bằng chart? |
|---|---|---|
| ICT / IPDA | Một "thuật toán giao giá liên ngân hàng" đưa giá từ pool thanh khoản này sang pool khác; smart money quét stop để lấy đối ứng ([[60-IPDA-Tai-sao-gia-di-chuyen-Tu-Price-Discovery-den-Price-Delivery]]) | Không — tác nhân và ý định không quan sát được |
| Auction market theory | Thị trường thử các vùng giá để tìm nơi có đối ứng hai chiều; vùng mỏng bị xuyên rồi bật lại | Không |
| Microstructure (stop cascade) | Cụm stop hữu hạn bị tiêu thụ; nếu không có dòng lệnh mới, giá quay lại | Một phần — qua tốc độ reclaim/acceptance |
| Self-fulfilling / phản thân | Đủ nhiều người vẽ cùng FVG/EQH thì hành vi tập thể tạo phản ứng tại đó ([[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]]) | Không |

> [!warning] Dùng IPDA như mô hình tư duy, không như lời giải thích khi review lệnh thua
> "Vì IPDA cần thêm thanh khoản" giải thích được *mọi* kết quả — nên nó không giải thích gì cả. Câu trả lời trung thực hơn khi review: *"mẫu này đã/không lặp lại trong dữ liệu của tôi; tôi không chứng minh được cơ chế nền."*

### 5.1 Từ điển nhanh — định nghĩa bằng lời đơn giản

Định nghĩa đo được (có ngưỡng) nằm ở [[#49. Định nghĩa khách quan (đo được)]]. Ở đây chỉ là nghĩa — để đọc phần sau không bị vấp.

| Thuật ngữ | Nghĩa đơn giản |
|---|---|
| **Swing high / low** | Đỉnh/đáy nhỏ mà hai bên đều thấp/cao hơn nó |
| **STH / ITH / LTH** | Đỉnh/đáy ngắn hạn (3 nến) · trung hạn (STH có STH thấp hơn hai bên) · dài hạn (ITH có ITH thấp hơn hai bên) — [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]] |
| **HH / HL / LH / LL** | Đỉnh cao hơn / đáy cao hơn / đỉnh thấp hơn / đáy thấp hơn so với swing cùng cấp trước đó |
| **Internal / external structure** | Swing bên trong một nhịp lớn / swing tạo biên của nhịp lớn |
| **BOS** | Phá swing theo **cùng** hướng xu hướng đang có (tiếp diễn) |
| **MSS** | Phá swing **ngược** hướng nhịp vừa rồi, bằng thân nến, có displacement — dấu hiệu nhịp đó bị phủ định |
| **CHoCH** | Thuật ngữ SMC gần nghĩa MSS; nhiều nguồn dùng cho lần phá đầu tiên ngược xu hướng, không đòi displacement |
| **Liquidity** | Nơi có thể có nhiều lệnh chờ (stop, breakout, take-profit) — thường quanh đỉnh/đáy dễ thấy |
| **BSL / SSL** | Thanh khoản phía trên đỉnh (buy stops) / phía dưới đáy (sell stops) |
| **Internal / external liquidity (IRL/ERL)** | Thanh khoản bên trong range (FVG, swing nội bộ) / ở biên hoặc ngoài range |
| **Sweep (raid)** | Giá xuyên một pool rồi **đóng lại** bên trong trong vài nến |
| **Run / breakout** | Giá xuyên pool và **được chấp nhận** bên ngoài (acceptance) |
| **Acceptance** | Thân nến đóng ngoài một mức và **giữ** ở đó (≥ 2 nến, HEURISTIC) — dùng để vô hiệu |
| **Displacement** | Nhịp giá mạnh, quyết đoán, thân nến lớn, để lại FVG |
| **FVG** | Khoảng giá chỉ một nến giao dịch (mô hình 3 nến) |
| **CE** | Điểm 50% của FVG (hoặc của một vùng) |
| **Dealing range** | Khoảng giá giữa hai swing được chọn làm khung tham chiếu |
| **EQ / Premium / Discount** | Điểm 50% của range / nửa trên ("đắt") / nửa dưới ("rẻ") |
| **DOL** | Pool thanh khoản mà giả thuyết cho rằng giá đang bị hút về |
| **POI / PD array** | Vùng giá đáng quan sát (FVG, OB, breaker…) — chỗ chờ, không phải tín hiệu |
| **Inducement** | Pool nhỏ nằm trước POI, dễ bị quét trước khi giá tới POI |
| **Killzone** | Cửa sổ thời gian ưu tiên (London, NY AM) định nghĩa theo giờ New York |
| **Daily Bias** | Hướng được phép xét trong ngày — một giả thuyết có điều kiện, không phải dự báo |

---

## PART II — D1: BỐI CẢNH

> [!important] Nhiệm vụ thật sự của D1
> D1 **không** tìm điểm entry. D1 trả lời bốn câu hỏi và viết câu trả lời ra *trước* khi mở khung thấp:
> 1. **Tôi đang ở đâu?** (cấu trúc, range, vị trí trong range)
> 2. **Hướng nào đáng được ưu tiên xét?** (bias — hoặc không có)
> 3. **Giá có thể đang bị hút về đâu, và điều gì cản đường?** (DOL, pool đối diện)
> 4. **Điều gì chứng minh tôi sai?** (invalidation)
>
> Output của D1 là một **Context Note** (mẫu ở §14). Không có Context Note viết ra được → không có lý do mở H1.

### 6. Major Market Structure

**Hiểu nhanh.** Cấu trúc là "câu chuyện" của các đỉnh và đáy quan trọng: chúng đang leo lên, đi xuống, hay đi ngang? Câu chuyện chỉ được kể bằng các đỉnh/đáy *có ý nghĩa*, không phải mọi răng cưa nhỏ.

![[ICT2022-v2-03-D1-Cau-truc-va-cap-swing.svg]]

**Quy trình đọc (làm đúng thứ tự):**
1. **Phóng ra đủ xa** (thường 3–6 tháng D1) để thấy ít nhất 2–3 swing cấp lớn.
2. **Đánh dấu swing theo cấp:** STH (3 nến) → ITH → LTH (định nghĩa ở §7). Chỉ ITH/LTH được dùng để kết luận cấu trúc D1.
3. **Tách external khỏi internal:** external = các swing tạo biên nhịp lớn; internal = dao động bên trong nhịp đó.
4. **Đọc chuỗi HH/HL hay LH/LL** trên swing cùng cấp — không so một STH với một ITH.
5. **Tìm swing đã tạo ra chuyển động đáng kể hoặc đổi cấu trúc** — swing khởi phát displacement, swing đã lấy thanh khoản lớn. Đây là ứng viên neo range (§8) và "protected swing".
6. **Kết luận trạng thái:** Bullish · Bearish · Range · Transition/Không rõ.

**Bốn trạng thái cấu trúc và ý nghĩa thực hành:**

| Trạng thái | Dấu hiệu `[OBSERVABLE]` | Hệ quả |
|---|---|---|
| **Bullish** | ITH/LTH tạo HH–HL; ITH low gần nhất (protected low) còn nguyên | Long được *xem xét*; chưa có nghĩa "phải mua" |
| **Bearish** | LH–LL; protected high còn nguyên | Short được xem xét |
| **Range** | Đỉnh/đáy ITH quanh hai biên, không phá có acceptance | Chỉ trade nếu có spec riêng cho range; mặc định Neutral |
| **Transition** | Vừa có MSS cấp ITH ngược cấu trúc cũ, chưa có leg mới xác nhận | Neutral cho tới khi leg mới hình thành |

**Một cấu trúc bullish vẫn chứa nhịp hồi bearish** — đây không phải mâu thuẫn mà là hình học bình thường. Giá đi lên bằng các leg: tăng (impulse) → hồi (pullback) → tăng. Trong lúc hồi, STH (thậm chí ITH nội bộ) bị phá xuống. Chỉ khi **protected low** (ITH/LTH đã khởi phát leg tăng gần nhất) bị **thân nến D1 đóng xuyên qua**, câu chuyện D1 mới đổi.

**Khi nào KHÔNG được dùng một swing nhỏ để kết luận bias:** khi swing đó là STH; khi nó nằm giữa range; khi nó bị phá bằng râu (wick) chứ không bằng thân; khi cú phá đến từ một nến tin tức đơn lẻ rồi bị lấy lại ngay.

**Khi nào nên giữ Neutral:** không xác định được ≥ 2 ITH cùng chiều; vừa có MSS cấp ITH ngược chiều (transition); giá đi ngang quanh EQ của range nhiều tuần; hai khung W1 và D1 chống nhau tại một vùng phản ứng lớn.

> [!warning] Không mặc định "HH/HL là mua, LH/LL là bán"
> Cấu trúc chỉ trả lời "câu chuyện đang là gì". Quyết định có xét long hay không còn phụ thuộc **vị trí** (§9) và **DOL** (§11). Một cấu trúc bullish với giá đang ở sát đỉnh range, DOL đã bị lấy, là bối cảnh *tồi* để tìm long.

### 7. Swing Significance — phân cấp ý nghĩa của swing

**Vì sao cần phân cấp.** Trên D1 lúc nào cũng có rất nhiều đỉnh/đáy. Nếu mọi swing đều "quan trọng", bạn sẽ luôn tìm được một swing vừa bị phá để biện minh cho bất kỳ hướng nào. Phân cấp biến "swing nào quan trọng" thành một quy tắc trước-sự-kiện.

| Cấp nghiên cứu | Tương ứng ICT | Định nghĩa vận hành | Dùng để |
|---|---|---|---|
| L1 — Micro | — | Fractal 1 nến hai bên | Không dùng trên D1 |
| L2 — Internal | **STH** | Fractal 3 nến (nến giữa cao/thấp hơn hai bên, tính râu) | Nhiễu nội bộ; target nhỏ |
| L3 — Intermediate | **ITH / ITL** | STH có STH thấp hơn (cao hơn) ở **cả hai bên** | MSS hợp lệ; protected swing của leg |
| L4 — External / dealing range | ITH/LTH tạo biên range | Swing neo range: lấy thanh khoản + khởi phát displacement | Neo range, ERL, DOL |
| L5 — HTF major | **LTH / LTL**, W1/MN swing | ITH có ITH thấp hơn hai bên, thường tại HTF PD array | Đổi bias dài hạn; final DOL |

**Năm câu hỏi chấm ý nghĩa (S · L · D · R · T):**
- **S — Structural:** phá nó có làm đổi câu chuyện không? (phá protected low = có; phá STH giữa leg = không)
- **L — Liquidity:** nó đã lấy thanh khoản đáng kể chưa, hoặc phía sau nó còn thanh khoản đáng kể không?
- **D — Displacement:** nó có khởi phát một nhịp mạnh không?
- **R — Reaction:** phản ứng sau nó lớn cỡ nào so với ATR?
- **T — Timeframe:** nó hiện rõ ở khung nào? (thấy được trên W1 > chỉ thấy trên D1)

Một swing có S, L, D cao là ứng viên neo range và protected swing. Một swing chỉ có T thấp và R nhỏ là STH — dùng làm target nhỏ, không dùng để đổi bias.

> [!info] Swing có độ trễ xác nhận — chi tiết ở §51
> Một STH chỉ "tồn tại" sau khi nến bên phải đóng; một ITH chỉ tồn tại khi STH bên phải đã hình thành. Trong thời gian thực, swing gần nhất luôn là **ứng viên**. Backtest gắn nhãn swing trước thời điểm xác nhận là **look-ahead bias**. Phân cấp đầy đủ và thuật toán phát hiện swing: [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]], [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]].

### 8. Dealing Range

**Hiểu nhanh.** Dealing range là "cái thước" bạn chọn để đo giá đang rẻ hay đắt. Thước nào thì kết quả đo theo thước đó — nên phải chọn thước có lý do, và chọn *trước* khi nhìn khung thấp.

![[ICT2022-v2-04-Dealing-Range-Premium-Discount.svg]]

**Quy trình xác định:**
1. **Chọn neo dưới và neo trên** — hai swing cấp L4/L5 (ITH/LTH) gần nhất bao quanh giá hiện tại.
2. **Kiểm tra lý do chọn neo** (4 câu hỏi): swing có lấy thanh khoản rõ? có khởi phát displacement? đã có cấu trúc mới làm range cũ hết hiệu lực chưa? range có chứa giá hiện tại và DOL không?
3. **Phân biệt range operative với range con:** range D1 là thước cho bias; range nhỏ bên trong (internal) chỉ dùng cho H1/M5.
4. **Kẻ EQ 50%** và hai nửa Premium/Discount.
5. **Ghi neo ra Context Note** (giá + ngày của hai neo). Đổi neo sau khi thấy giá đi = hindsight.

```text
Dealing Range High  ─────────────  (neo trên: swing đã lấy BSL)
        │  PREMIUM   — giá "đắt" so với thước này
        │
        ├──── EQUILIBRIUM 50% ────
        │
        │  DISCOUNT  — giá "rẻ" so với thước này
Dealing Range Low   ─────────────  (neo dưới: swing đã lấy SSL + khởi phát displacement)
```

**Khi có nhiều range hợp lệ** (rất thường gặp): ghi **cả hai**. Ví dụ, range nhịp tăng gần nhất (leg range) và range tổng của 3 tháng. Quy tắc chọn mặc định của phiên bản này: *range nhỏ nhất vẫn chứa cả giá hiện tại lẫn primary DOL, với hai neo cấp ≥ L4.* Nếu hai range cho kết luận P/D ngược nhau → hạ confidence hoặc Neutral, không chọn cái "thuận" với ý muốn.

**Khi nào phải re-map:** khi một neo bị phá bằng acceptance; khi có displacement mới tạo swing cấp L4 bên ngoài range cũ ([[37-Re-mapping-Dealing-Range-sau-Displacement]]). Re-map là một **sự kiện ghi log**, không phải điều chỉnh âm thầm.

### 9. Premium, Discount và Equilibrium

**Ý nghĩa đúng:** P/D là cách đo **vị trí tương đối** của giá trong thước đã chọn. Logic ICT: mua ở phần "rẻ" của một nhịp tăng cho hình học rủi ro tốt hơn (stop gần neo dưới, target xa ở neo trên).

**Giới hạn — vì sao 50% không phải phép màu:**
- EQ là quy ước hình học, không phải mức giá "thị trường biết". Đổi neo 1% → EQ dịch theo.
- Discount **không** = vùng mua. Nó = vùng *được phép xem xét* long. Giá có thể ở discount và tiếp tục giảm xuyên qua neo dưới.
- Quanh EQ (± ~5% bề rộng range, HEURISTIC) vị trí mơ hồ → hạ confidence.
- OTE 62–79% là một **phép đo vị trí khác** (thường đo trên một leg), là bộ lọc tùy chọn — xem §39.

`[HYPOTHESIS]` HYP-01: setup long có z = (giá − low)/(high − low) ≤ 0.5 trên range D1 có expectancy cao hơn setup long ở z > 0.5. `[BACKTEST REQUIRED]` — đo bằng cách log z cho *mọi* setup, kể cả setup ở premium bị chặn.

### 10. Internal và External Liquidity

![[ICT2022-v2-05-Internal-External-Liquidity.svg]]

**Hiểu nhanh.** "Thanh khoản" trong ICT là nơi *có thể* có nhiều lệnh chờ: ngay trên các đỉnh dễ thấy (stop của người bán, lệnh mua breakout) và ngay dưới các đáy dễ thấy.

| Khái niệm | Định nghĩa | Ví dụ trên D1 |
|---|---|---|
| **BSL** | Thanh khoản phía trên đỉnh | PDH, PWH, đỉnh range, EQH |
| **SSL** | Thanh khoản phía dưới đáy | PDL, PWL, đáy range, EQL |
| **ERL** (external) | Thanh khoản ở biên/ngoài dealing range | Đỉnh/đáy range, swing L4/L5 |
| **IRL** (internal) | Thanh khoản bên trong range | FVG chưa lấp, swing nội bộ, EQH/EQL giữa range |

**Phân biệt ba thứ dễ trộn lẫn:**
1. **Liquidity có thể nhận diện trên chart** `[OBSERVABLE — gián tiếp]`: một mức đỉnh/đáy dễ thấy. Chart OHLC *không* cho thấy sổ lệnh — ta chỉ suy luận rằng lệnh *có thể* co cụm ở đó (có bằng chứng thống kê cho FX, xem §5).
2. **Mục tiêu mà ICT diễn giải là giá hướng tới** `[ICT FRAMEWORK]`: "price seeks liquidity".
3. **Một dự báo đã được chứng minh** `[BACKTEST REQUIRED]`: "primary DOL bị chạm trước invalidation với tần suất cao hơn null". Chưa có trong dữ liệu của bạn.

Chu kỳ ICT hay mô tả — ERL bị lấy → giá về IRL (entry) → giá hướng ERL đối diện ([[16-Internal-External-Range-Liquidity-IRL-ERL]]) — là **mô tả**, không phải luật. Không phải EQH nào cũng là mục tiêu chắc chắn.

### 11. Draw on Liquidity (DOL)

**Hiểu nhanh.** DOL là câu trả lời có điều kiện cho câu "nếu giả thuyết của tôi đúng, giá sẽ đi lấy thanh khoản ở đâu trước?". Nó là một **mệnh đề**, không phải một vật thể: *pool X, trong khoảng thời gian Y, trước khi chạm mức sai Z*.

![[ICT2022-v2-06-DOL-Xep-hang-pool.svg]]

**Quy trình:**
1. **Liệt kê mọi pool hai phía** còn nguyên (chưa bị lấy) trong phạm vi hợp lý (≈ 1–3 ADR và các mức W1).
2. **Phân loại** mỗi pool: cấp khung, external/internal, còn nguyên hay đã bị wick, khoảng cách (theo ATR D1).
3. **Đánh giá đường đi:** giữa giá hiện tại và pool có vật cản nào (FVG ngược chiều, pool nhỏ hơn) không?
4. **Đánh giá pool đối diện:** pool phía ngược bias gần đến đâu, đã bị lấy chưa? Pool đối diện gần và còn nguyên là **điểm yếu số một** của luận điểm (giá có thể lấy nó trước).
5. **Ghi ba thứ riêng biệt:** **primary DOL** (pool cấp ≥ L4 theo hướng bias), **secondary DOL** (mục tiêu kế tiếp *cùng hướng*, thường là pool cấp cao hơn phía sau primary), và **pool đối diện / điểm yếu** (pool gần nhất ở phía ngược bias còn nguyên). Kèm horizon + mức vô hiệu. Nếu không pool nào nổi trội → "DOL chưa đủ cơ sở".

*Lưu ý cấp:* DOL chỉ chọn từ pool cấp ≥ L4 (biên range, swing W1). Pool nhỏ hơn (PDH/PDL nội bộ, swing H1) là **IRL / Target 1**, không phải DOL.

**Khi nào DOL kém thuyết phục:**
- Pool đã bị wick một hoặc nhiều lần (thanh khoản có thể đã được khớp một phần).
- Pool quá gần (< ~1 ATR D1): luận điểm gần hoàn tất, R cho lệnh mới thấp.
- Có pool đối diện gần hơn, còn nguyên, cùng hướng với nhịp ngắn hạn đang chạy.
- DOL chỉ có "lý do" là gần nhất.

**Bốn cách một DOL "hết dùng được"** (mỗi cách một hành động khác nhau — chi tiết [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]], [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]):

| Trạng thái | Nghĩa | Hành động |
|---|---|---|
| **Fulfilled** | Giá đã chạm DOL | Luận điểm hoàn tất → viết lại Context Note |
| **Superseded** | Pool đối diện bị lấy *với displacement + acceptance* | Đánh giá lại bias |
| **Expired** | Hết horizon mà chưa tới | Hạ confidence, re-derive |
| **Invalidated** | Mức sai (protected swing) bị đóng xuyên | Reset về S0 |

`[HYPOTHESIS]` HYP-02: primary DOL được chọn ex-ante bị chạm trước mức vô hiệu với tần suất cao hơn xác suất null tính bằng khoảng cách (random walk). `[BACKTEST REQUIRED]`

### 12. Daily Bias

**Hiểu nhanh.** Bias không phải "hôm nay giá sẽ tăng". Bias là **chính sách cấp phép**: "hôm nay tôi chỉ xét setup long" (hoặc short, hoặc không xét gì).

![[ICT2022-v2-07-Daily-Bias-4-trang-thai.svg]]

```text
Major Structure  +  Dealing Range  +  Liquidity  +  Location  +  HTF POI
                                  │
                                  ▼
            Directional Assessment (ủng hộ vs mâu thuẫn, thiếu gì, sai ở đâu)
                                  │
         ┌──────────────┬─────────┴─────────┬────────────────┐
      BULLISH        BEARISH            NEUTRAL         CONFLICTING
```

| Trạng thái | Bằng chứng ủng hộ | Bằng chứng mâu thuẫn hay gặp | Làm yếu đi khi | Vô hiệu khi | Thông tin thường thiếu |
|---|---|---|---|---|---|
| **Bullish** | ITH/LTH tạo HH–HL; giá ở discount hoặc tại HTF POI bullish; SSL gần vừa bị lấy rồi reclaim; BSL ERL còn nguyên | SSL D1 gần chưa bị lấy (pool đối diện); W1 ở premium hoặc W1 POI bearish | Giá về EQ không phản ứng; SSL gần bị lấy *với displacement* | Thân D1 đóng dưới protected low | Range nào là operative; DOL có bị wick trước đó không |
| **Bearish** | ITH/LTH tạo LH–LL; giá ở premium hoặc tại HTF POI bearish; BSL gần vừa bị lấy rồi reclaim; SSL ERL còn nguyên | BSL D1 gần chưa bị lấy; W1 ở discount hoặc W1 POI bullish | Giá về EQ không phản ứng; BSL gần bị lấy *với displacement* | Thân D1 đóng trên protected high | Như trên |
| **Neutral** | Không có ≥ 2 ITH cùng chiều; giá quanh EQ (± ~5%); hai DOL ngang nhau; vừa có MSS cấp ITH ngược cấu trúc cũ (transition) | — (chính sự thiếu bằng chứng là kết luận) | — | Chuyển sang Bull/Bear khi leg mới hình thành hoặc một pool bị lấy có reclaim rõ | Một leg mới, một DOL nổi trội |
| **Conflicting** | Cấu trúc ủng hộ một hướng | Vị trí hoặc DOL ủng hộ hướng kia (vd bullish nhưng ở premium sát DOL; W1 chống D1 tại W1 POI) | Mâu thuẫn kéo dài nhiều phiên → coi như Neutral | Được giải quyết khi giá về vị trí phù hợp (→ Bull/Bear) hoặc cấu trúc đổi | Thời gian — thường chỉ cần chờ |

**Không ép phải chọn mỗi ngày.** Một hệ thống không bao giờ trả lời "Neutral" là một hệ thống ép dữ liệu. Theo bản tóm tắt thứ cấp Ep.19 của 2022 Mentorship (trích trong [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]]), chính ICT nói có những lúc ông không có bias và chờ displacement tạo ra một range dùng được.

**Bias ≠ DOL ≠ Setup ≠ Entry direction:**
- **Bias** (D1): hướng được phép.
- **DOL** (D1): mục tiêu giả thuyết.
- **Setup** (H1): cơ hội cụ thể tại một vùng.
- **Entry direction** (M5): hướng lệnh. Thường trùng bias; một lệnh ngược bias là **mô hình countertrend** — cần spec riêng, không phải "linh hoạt".

> [!warning] Chấm bias đúng cách
> Chấm `bias_correct` bằng "nến D1 đóng đúng hướng không" là outcome bias. Cách đúng: chấm **ex-ante** theo Context Note (bias có tuân thủ quy trình không), và đánh giá *giá trị* của bias bằng câu hỏi: **setup được bias cho phép có expectancy tốt hơn setup bị chặn không?** — đòi hỏi log cả setup bị chặn. Chi tiết: [[59-Daily-Bias]].

### 13. Higher-Timeframe POI

POI D1 là vùng mà nếu giá tới, bạn có lý do quan sát kỹ hơn. Không cần nghiên cứu lại từng khái niệm — chỉ cần biết vì sao một vùng đáng theo dõi *trong bối cảnh này*:

| Loại POI | Vì sao có thể đáng theo dõi `[ICT FRAMEWORK]` | Chi tiết |
|---|---|---|
| **D1 FVG** | Vùng giao dịch một chiều do displacement để lại | [[13-FVG-Fair-Value-Gap]] |
| **D1 Order Block** | Nến ngược chiều cuối cùng trước displacement phá cấu trúc | [[25-OB-Order-Block]], [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]] |
| **Breaker / Rejection block** | OB thất bại đổi cực / vùng râu từ chối | [[04-Breaker-Block]], [[28-Rejection-Block]] |
| **Mức thanh khoản cũ** | PDL/PWL, đáy range — nơi sweep có thể xảy ra | [[19-Liquidity]] |

**Sáu câu hỏi cho mỗi POI:**
1. POI nằm ở đâu (giá, ngày tạo)?
2. Có phù hợp cấu trúc không? (POI bullish nằm ở discount của range operative)
3. Có liên quan range/DOL không? (nằm giữa giá và pool đối diện = vùng hồi hợp lý)
4. Giá đã tiếp cận chưa, còn bao xa (theo ATR)?
5. Điều gì làm POI mất giá trị? (acceptance xuyên distal — ≥ 2 thân D1, HEURISTIC; bị mitigate sâu nhiều lần)
6. Vì sao nó **chỉ là vùng quan tâm**? — vì chạm POI là *arrival*, một sự kiện có base rate cao; nó không chứa thông tin về việc mất cân bằng đã lật hay chưa.

### 14. D1 checklist và mẫu Context Note

**Checklist D1 — phân biệt cốt lõi và bổ trợ:**

| Mục | Cốt lõi / Bổ trợ | Đủ khi |
|---|---|---|
| Structure state bằng ITH/LTH | **Cốt lõi** | Gọi được Bullish/Bearish/Range/Transition kèm swing cụ thể |
| Dealing range operative + EQ | **Cốt lõi** | Hai neo có giá + ngày; z của giá hiện tại |
| Pool hai phía + primary/secondary DOL | **Cốt lõi** | Có tên, có giá, có horizon |
| Bias | **Cốt lõi** | Một trong 4 trạng thái + lý do |
| Invalidation | **Cốt lõi** | Một mức giá + điều kiện (D1 close) |
| HTF POI | **Cốt lõi** (cho phiên bản này) | Ít nhất 1 vùng được phép, hoặc ghi rõ "dùng z < 0.5 làm vùng" |
| W1 context, SMT, displacement D1 gần nhất | Bổ trợ | Tăng/giảm confidence |

```text
D1 CONTEXT NOTE — [SYMBOL] — [ngày] — viết lúc [giờ VN] (TRƯỚC khi mở H1)
D1 STRUCTURE:       [Bullish/Bearish/Range/Transition] | protected swing: [giá, ngày] | swing đối diện: [giá]
DAILY BIAS:         [Bullish/Bearish/Neutral/Conflicting] — confidence [Low/Medium/High] ([n]/6 supporting: liệt kê)
DEALING RANGE:      [neo dưới: giá, ngày, lý do] → [neo trên: giá, ngày, lý do] | EQ [giá]
CURRENT LOCATION:   [giá] → z = [..] ([discount/premium/gần EQ])
RELEVANT LIQUIDITY: BSL: [các pool, cấp, đã/chưa chạm] · SSL: [các pool, cấp, đã/chưa chạm]
POTENTIAL DOL:      Primary [pool ≥ L4, horizon] · Secondary [mục tiêu kế tiếp cùng hướng] · Pool đối diện/điểm yếu [pool]
HTF POI:            [loại, giá, ngày tạo, đã mitigate chưa]
KEY INVALIDATION:   [D1 close vượt mức nào → reset] · [acceptance qua distal POI → POI fail]
WHAT I WANT ON H1:  [một câu: nhịp nào, đi vào đâu, tạo pool gì; điều KHÔNG làm]
```

Ví dụ điền đầy đủ: §58 (B1).

**Giải thích từng trường bằng lời đơn giản:**
- **D1 STRUCTURE** — câu chuyện lớn đang là gì, và *đáy nào nếu thủng thì câu chuyện đổi*.
- **DAILY BIAS** — hôm nay được xét hướng nào; confidence giúp chia size, không giúp phá luật.
- **DEALING RANGE** — cái thước, kèm lý do chọn hai đầu thước.
- **CURRENT LOCATION** — giá đang ở phần rẻ hay đắt của thước (z).
- **RELEVANT LIQUIDITY** — mọi pool đáng kể ở cả hai phía, không chỉ phía mình thích.
- **POTENTIAL DOL** — mục tiêu chính, mục tiêu phụ, và *điểm yếu của luận điểm*.
- **HTF POI** — vùng được phép tìm setup.
- **KEY INVALIDATION** — viết ra để khỏi phải quyết định trong lúc cảm xúc.
- **WHAT I WANT ON H1** — hướng dẫn cho chính mình ở bước sau; giúp không "quên" bối cảnh khi zoom vào.

### 15. Điều kiện chuyển xuống H1 (Gate G1)

**Quy tắc:** chỉ mở H1 khi Context Note đủ rõ để định hướng việc quan sát H1 — tức là H1 biết mình **đang tìm cái gì, ở đâu, theo hướng nào, và sai khi nào**.

| Loại | Điều kiện | Ghi chú |
|---|---|---|
| **Required** (thiếu một = không mở H1) | R1 structure ∈ {Bullish, Bearish} · R2 range operative có 2 neo cấp ≥ L4 · R3 pool hai phía + primary/secondary DOL · R4 bias ∈ {Bullish, Bearish} (Neutral và Conflicting đều không qua) · R5 vị trí tương thích (z ≤ 0.5 cho long, hoặc đang ở/tiến về HTF POI) · R6 có invalidation viết ra | Spec đầy đủ: [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)\|01c]] §8.2 |
| **Supporting** (chỉ tăng confidence, không mở gate) | W1 cùng hướng · displacement D1 gần nhất cùng hướng · pool đối diện vừa bị lấy và reclaim · primary DOL chưa từng bị chạm · khoảng cách tới DOL ≥ 2 ATR D1 · SMT không phân kỳ ngược | 0–2 Low · 3–4 Medium · 5–6 High → size 0.25% / 0.4% / 0.5% (HEURISTIC, trần 0.5%) |
| **Disqualifying** (có một = không mở H1) | Khoảng cách tới DOL < 1 ATR D1 · ngày có tin cấp cao mà không chạy event-mode · W1 ngược hướng *và* giá ở W1 POI ngược hướng · circuit breaker đang khóa · Context Note viết sau khi đã nhìn H1/M5 | |

> [!important] Quy tắc này thay quy tắc "2-of-3" của v0.1
> "2-of-3" là phép đếm cộng — nó cho phép thiếu chính điều kiện quan trọng nhất (vd thiếu DOL hoặc thiếu invalidation) nếu hai điều kiện kia thỏa. Đề xuất đã nêu ở [[59-Daily-Bias]] §4.7; note này dùng làm mặc định nghiên cứu. OLD / NEW / REASON / EXPECTED EFFECT / BACKTEST ở changelog §62 (D-03).

**Nếu Gate G1 fail — ở lại D1 làm gì:**

| Fail vì | Việc làm được |
|---|---|
| Structure Transition/Range | Theo dõi xem leg mới hình thành chưa; không tìm setup |
| DOL chưa đủ cơ sở | Viết 2 kịch bản có điều kiện: "nếu giá lấy X rồi reclaim → bullish; nếu accept dưới Y → bearish" |
| Neutral | Ghi lý do; ghi trigger nào sẽ biến Neutral thành Bull/Bear |
| Vị trí sai (bullish nhưng ở premium) | **Chờ giá về discount/POI** — trạng thái chờ hay gặp nhất, cũng là nơi FOMO sinh ra ([[04-Mistake-FOMO-Entry]]) |
| DOL quá gần | Chờ fulfilled rồi viết lại Context Note |

---

## PART III — H1: SETUP

> [!important] Nhiệm vụ thật sự của H1
> H1 **không** lặp lại D1 ở mức phóng to, và **không** quyết định lại hướng. H1 kế thừa hướng, vùng và mức sai từ Context Note, rồi trả lời:
> - Giá đang làm gì *bên trong* bối cảnh đó — hồi về vùng quan tâm, hay đang phá vùng đó?
> - Vùng nào trong vùng D1 là nơi cụ thể đáng chờ (POI refine)?
> - Thanh khoản nào đang được tạo ra gần vùng đó (pool sẽ bị quét)?
> - **Khi nào** được mở M5, và mở để *quan sát* hay để *thực thi*?

**Vì sao không nhảy thẳng D1 → M5.** Khoảng cách thông tin giữa D1 và M5 quá lớn: một ngày D1 chứa 288 nến M5. Không có tầng trung gian, M5 sẽ cho bạn rất nhiều MSS mỗi ngày, và bạn sẽ tự thuyết phục rằng cái nào cũng "thuận D1". H1 là bộ lọc vị trí và thời điểm: nó quyết định M5 được hỏi **một câu**, **ở một chỗ**, **trong một khung giờ**.

### 16. Intermediate Market Structure

**Quy trình:**
1. Xác định swing H1 có ý nghĩa **trong bối cảnh D1** — thường là các ITH/ITL H1 của nhịp đang hồi về POI D1.
2. Phân biệt internal (răng cưa trong nhịp hồi) và external (đỉnh/đáy tạo biên nhịp hồi).
3. Đánh dấu các lần phá swing; phân loại bằng định nghĩa ở §26 (BOS / MSS / structural break yếu).
4. Kết luận H1 đang: **tiếp diễn theo D1** · **hồi ngược D1** · **có dấu hiệu chuyển trạng thái** tại/sau POI.

![[ICT2022-v2-09-D1-Bull-H1-Bear-Correction.svg]]

**H1 bearish có phủ định D1 bullish không?** Không tự động. Ý nghĩa của H1 chỉ đọc được khi đặt cạnh **vị trí**:

| H1 đang… | So với D1 POI | Đọc là | Hành động |
|---|---|---|---|
| Bearish (LH–LL) | **Chưa tới** POI | Nhịp hồi đang diễn ra — hình học bình thường | NOT READY; không short theo H1 |
| Bearish, giá **trong** POI | Trong POI, chưa acceptance | Có thể sắp có alignment | MONITORING |
| MSS bullish | **Tại/sau** POI | Alignment H1 với D1 | Xét EXECUTION ELIGIBLE |
| Thân H1 đóng **xuyên** POI, giữ ≥ 2 nến | Acceptance dưới distal | POI thất bại | Hủy setup tại POI; REASSESS D1 |
| Bearish **xuyên** protected low D1 trong phiên | Dưới mức sai D1 (chưa D1 close) | Cảnh báo cấp cao | SUSPEND (ngừng tìm entry mới), chờ D1 close |

**Một H1 bearish MSS không làm D1 bearish.** Tầng dưới có quyền *tạm dừng* (suspend) tầng trên, không có quyền *vô hiệu hóa* nó. Chỉ D1 close xuyên protected swing mới đổi cấu trúc D1.

### 17. H1 Liquidity và Price Path

**Cần đánh dấu:**
- **Internal liquidity H1:** đáy/đỉnh STH trong nhịp hồi, EQL/EQH nội bộ.
- **External liquidity H1:** đỉnh/đáy tạo biên nhịp hồi; đây thường là **Target 1** (ITH/ITL H1 đầu tiên theo hướng lệnh còn chưa bị lấy).
- **Inducement:** pool nhỏ *nằm trước* POI — dễ bị quét trước khi giá chạm POI ([[15-Inducement]]).
- **Pool gần POI:** đáy H1 nằm trong/ngay dưới POI — ứng viên số một cho cú sweep M5.

**Phân biệt điều đáng chú ý và nhiễu:** một mức đáng chú ý khi (a) nó là ITL/ITH H1 hoặc EQL/EQH rõ, (b) nó nằm trong hoặc sát POI, (c) việc nó bị lấy sẽ thay đổi cách đọc (vd lấy inducement = "dọn đường" tới POI). Một STH giữa nhịp hồi, xa POI, là nhiễu.

**Năm câu hỏi phải trả lời được:**
1. Giá đang ở đâu so với DOL của D1? (còn chỗ đi bao nhiêu ATR?)
2. H1 có tạo một liquidity objective mới không? (vd một SSL nội bộ ngay trong POI)
3. Liquidity nào **có ý nghĩa cho setup này**? (pool sẽ bị quét + target 1)
4. Sweep đã **xảy ra** hay mình mới đang **dự đoán**? — đánh dấu pool *trước* là dự đoán có kiểm soát; gắn nhãn "sweep" sau khi thấy giá quay đầu là hindsight.
5. Sau liquidity event, bằng chứng tiếp theo cần là gì? — MSS + displacement trên M5, theo định nghĩa §26–27.

### 18. POI Refinement — thu hẹp vùng từ D1 xuống H1

![[ICT2022-v2-08-H1-Setup-Development.svg]]

**Khi nào giữ nguyên POI D1, khi nào thu hẹp:**

| Tình huống | Quyết định | Lý do |
|---|---|---|
| Bên trong POI D1 có một H1 FVG/OB hình thành từ displacement H1 | Thu hẹp về H1 POI | Có một vùng cụ thể hơn, có nguồn gốc cấu trúc |
| POI D1 hẹp (< ~0.5 ATR D1) | Giữ nguyên | Thu hẹp thêm chỉ tăng xác suất bị "xuyên" |
| Có nhiều H1 POI trong POI D1 | Xếp hạng (bên dưới), giữ tối đa 2, theo thứ tự | Không chọn cái gần nhất theo phản xạ |
| H1 POI nằm **ngoài** POI D1 | Không dùng cho Core | Vị trí D1 là điều kiện của phiên bản |

**Không thu hẹp quá mức:** POI càng hẹp, càng hay bị xuyên bởi chính cú sweep — và cú sweep lại là điều mô hình *cần*. Vùng hợp lý phải chứa được cả cú sweep lẫn phản ứng.

**Funnel lọc khi có nhiều ứng viên POI:**

```text
Ứng viên POI → cùng hướng D1? → nằm trong POI D1 / đúng P/D? → nguồn gốc displacement (có phá cấu trúc)?
     → còn "fresh" (chưa bị mitigate sâu)? → liên quan pool (có SSL ngay dưới để sweep)?
     → đủ chỗ tới T1 (R ≥ 2 dự kiến)? → còn > 1 ứng viên → xếp hạng; nếu vẫn ngang nhau → giữ cả hai, ghi rõ vì sao mơ hồ
```

**Thang POI Rank 1–5** (template gọi là *"thang 8.1"*; giữ nguyên để dữ liệu cũ còn so sánh được):

| Rank | Loại POI | Vì sao xếp cao hơn `[INTERPRETATION]` | Note |
|---|---|---|---|
| 1 | **FVG đơn** | Chỉ là vùng giao dịch một chiều | [[13-FVG-Fair-Value-Gap]] |
| 2 | **FVG + Order Block** | FVG chồng lên nến gốc của displacement | [[25-OB-Order-Block]] |
| 3 | **Breaker Block** | OB thất bại và đổi cực — thêm bằng chứng "đổi trạng thái" | [[04-Breaker-Block]] |
| 4 | **iFVG** | FVG bị close xuyên và đảo cực | [[17-Inverse-Fair-Value-Gap-iFVG]] |
| 5 | **Unicorn (Breaker ∩ FVG)** | Hai loại POI từ cùng displacement trùng một dải giá | [[07 - Unicorn Model]] |

> [!warning] Ranking này là HEURISTIC nghiên cứu `[BACKTEST REQUIRED]`
> Chưa có dữ liệu cho thấy rank cao cho expectancy cao hơn. Lưu ý thêm: FVG M5 nằm trong FVG H1 nằm trong FVG D1 là **cùng một đoạn giá được đo ở ba khung**, không phải ba bằng chứng độc lập — không cộng điểm ba lần. Và `[INTERPRETATION]` POI "đẹp quá" có thể chính là nơi đám đông ICT cũng đặt lệnh và đặt stop ([[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]]): ưu tiên POI có một inducement đã bị quét trước nó, và đặt stop ngoài vùng stop "hiển nhiên".

**Chọn POI theo dữ liệu của bạn:** template đã có `poi_type`, `poi_rank`, `fill_depth_pct`; sau 30–50 mẫu, [[_POI Analytics Dashboard]] trả lời "POI nào tôi thực thi tốt nhất" — câu trả lời đó thay thế thang trên, không phải ngược lại.

### 19. Setup Direction — quy trình ra quyết định

1. **Daily Bias đang ưu tiên hướng nào?** — đọc từ Context Note, không đọc lại từ chart.
2. **H1 có ở vị trí phù hợp để nghiên cứu hướng đó không?** — giá đang hồi về / đang ở POI D1, đúng P/D.
3. **Có liquidity event hoặc diễn biến cấu trúc đáng chú ý không?** — inducement đã bị lấy? SSL H1 đã hình thành trong POI?
4. **Setup đã đủ điều kiện chưa?** — đối chiếu §21.
5. **Nếu chưa, chính xác đang chờ điều gì?** — ghi một câu: "chờ giá vào 104–112 trong killzone NY AM".
6. **Nếu H1 đang đi ngược D1:** điều chỉnh bình thường (chưa tới POI) · xung đột (xuyên POI có acceptance) · cần đánh giá lại (xuyên protected swing trong phiên) — bảng §16.
7. **Nếu H1 không phù hợp kế hoạch:** bỏ qua setup. Không có setup hôm nay cũng là một quyết định đúng.

> [!warning] Hai điều không được làm ở bước này
> - Ép H1 phải xác nhận bias D1 *ngay* — H1 hồi ngược là bình thường cho tới khi giá tới POI.
> - Coi một cú quét liquidity H1 hoặc một MSS H1 đơn lẻ là đủ để vào lệnh — đó mới là *arrival* và *event*, chưa có M5 confirmation.

### 20. Điều kiện chờ

| Đang thiếu | Chờ điều gì cụ thể | Trạng thái |
|---|---|---|
| Giá còn xa POI D1 | Giá đi vào POI (đặt alert tại proximal) | NOT READY |
| Giá ở POI nhưng killzone chưa mở | Killzone mở | MONITORING nếu KZ mở trong ≤ 30 phút (HEURISTIC); xa hơn → NOT READY |
| Chưa có pool rõ để sweep | Một SSL/BSL H1–M5 hình thành trong POI | MONITORING |
| Pool đã có, chưa sweep | Sweep pool đã đánh dấu | EXECUTION ELIGIBLE (chờ trigger) |
| Sweep rồi, chưa MSS | MSS trong ≤ 12 nến M5 tính từ nến trigger sweep (HEURISTIC) | ELIGIBLE (trigger search) |
| MSS rồi, chưa retrace | Giá về mức entry trong TTL | Lệnh chờ |

### 21. Điều kiện setup hợp lệ

**Ba khái niệm không được dùng thay nhau:**

| Khái niệm | Câu hỏi | Ví dụ | Sai lầm khi trộn |
|---|---|---|---|
| **POI** | Ở đâu cần *quan sát*? | H1 FVG 105.5–110 trong D1 FVG | Vào lệnh khi giá chạm POI |
| **Setup qualification** | Có được phép *tiếp tục tìm* cơ hội không? | Bối cảnh còn hiệu lực + giá ở POI + đúng giờ + đủ chỗ đi | Tìm trigger M5 khi bối cảnh đã chết |
| **Entry trigger** | Có được phép *đặt lệnh* không? | Sweep → MSS → displacement → FVG trên M5 | Đặt lệnh khi chưa có MSS |

**Setup H1 hợp lệ khi** (đây là điều kiện để được vào trạng thái MONITORING ở §23; ELIGIBLE cần thêm Gate G2):
- **Required:** Context Note còn hiệu lực · có H1 POI trong vùng D1, đúng P/D, chưa bị acceptance · có pool cụ thể để sweep · xác định được **T1 = đỉnh/đáy cấp ≥ L3 (ITH/ITL H1) đầu tiên theo hướng lệnh còn chưa bị lấy** (một mức như vậy nằm giữa entry và mục tiêu xa hơn thì *chính nó* là T1, không được bỏ qua) · **R_proxy ≥ 1.5** (định nghĩa ở §23).
- **Supporting:** inducement đã bị quét · H1 nén (compression) khi vào POI · SMT thuận hướng tại POI · arrival trùng macro time.
- **Disqualifying:** arrival bằng một nến H1 đi xuyên qua toàn bộ POI · pool dự kiến sweep nằm dưới protected low D1 · **pool đối diện quan trọng hơn** (cấp ≥ L3, phía stop loss) còn nguyên và nằm ngoài vùng sweep dự kiến — giá có thể đi lấy nó trước ([[13-Mistake-Trading-Into-Unswept-Liquidity]], Case 4) · đã có **2 lần thất bại** trong cùng zone hôm nay (chuỗi M5 fail hoặc lệnh thua).

### 22. Điều kiện invalidation ở H1

| Kiểu | Trigger quan sát được | Hành động |
|---|---|---|
| POI acceptance | ≥ 2 thân H1 liên tiếp đóng ngoài **distal của H1 POI** → setup fail; ngoài **distal của D1 POI** → D1 POI fail | Hủy setup tại POI → POI kế tiếp (nếu còn trong D1 POI) hoặc REASSESS D1 |
| Target hoàn tất trước | T1 bị chạm trước khi giá về POI | Setup hết ý nghĩa (không còn chỗ đi) |
| Opposing pool mới | Một pool ngược chiều mới hình thành giữa POI và T1 | Tính lại T1/R; nếu R < 2 → bỏ |
| Context đổi | D1 SUSPEND / invalidated | Dừng mọi tìm kiếm |
| Hết thời gian | Hết killzone / D1 close mà chưa arrival | Setup hết hạn → viết lại cho phiên sau |
| Lặp thất bại | 2 lần thất bại trong cùng zone (chuỗi M5 fail hoặc lệnh thua) | Zone đã "trả lời" → ngừng |

Bốn hành động sau invalidation H1 (KEEP · WAIT · REASSESS · ABANDON) và cơ chế reset về "tầng sâu nhất còn hợp lệ": [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §10.

### 23. Khi nào chuyển xuống M5? — Gate G2

![[ICT2022-v2-10-Trang-thai-chuyen-khung-H1-M5.svg]]

| Trạng thái | Định nghĩa | Được làm | Không được làm |
|---|---|---|---|
| **A — NOT READY** | Giá còn xa POI, hoặc context chưa armed, hoặc killzone còn > 30 phút mới mở | Cập nhật bản đồ H1, đặt alert | Mở M5 tìm MSS |
| **B — MONITORING** | Setup H1 hợp lệ (§21) + giá đang tiến vào/vừa chạm POI + killzone đang mở hoặc mở trong ≤ 30 phút | **Mở M5 để chuẩn bị:** đánh dấu pool sẽ bị quét, đánh dấu ITH (mss_reference), tính R_proxy | Đặt lệnh |
| **C — EXECUTION ELIGIBLE** | **Gate G2 pass** = 3 điều kiện lõi + 4 kiểm tra vận hành (bên dưới) | Chờ trigger M5 theo rule; phát hành Execution Plan khi đủ | Vào khi trigger thiếu; nới điều kiện vì "sắp hết giờ" |

**Ba điều kiện lõi (giữ nguyên quy tắc "H1 → M5 cần đủ 3/3" của bạn):**
1. **Neo HTF:** bias + DOL còn hiệu lực (không SUSPEND, không invalidated).
2. **Đúng vị trí:** giá đã thực sự vào H1 POI, đúng phía P/D, **D1 và H1 đồng pha**, POI chưa bị acceptance.
3. **Đúng thời gian:** đang trong killzone đã khai báo.

**Bốn kiểm tra vận hành (dựa trên gate G2 của 01c):** pool và mss_reference đã được đánh dấu *trước* sweep · **R_proxy ≥ 1.5** · không tin đỏ ±15 phút · risk overlay chưa khóa.

> [!info] R_proxy — vì sao cần, và vì sao ngưỡng thấp hơn 2
> Trước trigger, entry và SL thật chưa tồn tại (SL phụ thuộc cực trị sweep, entry phụ thuộc FVG sau MSS). Dùng chúng để tính R "dự kiến" là dùng thông tin tương lai. v0.2 định nghĩa một proxy chỉ bằng dữ liệu đã có:
> `R_proxy = (T1 − mss_reference) / (mss_reference − (pool − buffer))` (long; short đối xứng)
> — entry xấp xỉ bằng mss_reference, SL xấp xỉ ngay dưới pool sẽ bị quét (cú quét thật thường sâu hơn → R thật có thể thấp hơn proxy). Ngưỡng sàng lọc **1.5** (HEURISTIC; 01c G2.R6 dùng 2 với proxy không định nghĩa). **R ≥ 2 vẫn bắt buộc tại Execution Plan** với entry/SL thật.

**Đồng pha Premium/Discount D1 ↔ H1** — điều kiện vị trí hay bị bỏ qua nhất:

![[ICT2022-Advanced-D1H1-PD-Alignment.svg|720]]

| Vị trí D1 | Vị trí H1 | Trạng thái | Hành động (kịch bản long; short đối xứng) |
|---|---|---|---|
| Discount | Discount | **Đồng pha** | Đạt điều kiện vị trí |
| Discount | Premium | **Lệch pha** | Chờ: draw ngắn hạn H1 hướng xuống trước; đợi H1 sweep rồi về discount H1 |
| Premium | Discount | Xung đột cấp cao | Thường là pullback ngược trend lớn → bỏ |
| EQ / Neutral | — | Không rõ | Đứng ngoài |

*Liên hệ dữ liệu của bạn:* lệnh thắng EURUSD 2013-11-21 có ghi chú "chờ H1 quay về Discount trước khi tìm entry" (đồng pha, Case 1). Lệnh thua EURUSD 2021-05-07 (Case 4) chủ yếu là lỗi **draw ngắn hạn / BSL chưa bị lấy** — liên quan nhưng không đồng nhất với lệch pha P/D.

**Ba cái bẫy khi xuống M5:**
1. **Xuống quá sớm** — khi giá còn xa POI. Bạn sẽ thấy rất nhiều "M5 MSS" và tự thuyết phục mình. Mở M5 ở trạng thái NOT READY là nguồn gốc số một của chase/FOMO.
2. **Nhảy cóc khung** — bias D1, entry M1: noise M1 nuốt tín hiệu, spread ăn R. Biến thể hạ khung có spec riêng: [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]].
3. **Overtrade** — khung thấp cho nhiều "cơ hội" hơn → giữ giới hạn cứng số lệnh/ngày kể cả khi đã ở trạng thái ELIGIBLE.

### 24. H1 handoff checklist — kèm hai ví dụ

```text
H1 HANDOFF
HTF CONTEXT:               (copy từ Context Note: bias, DOL, mức sai)
H1 STRUCTURE:              hồi ngược D1 / alignment / xuyên POI?
SETUP DIRECTION:           LONG only / SHORT only
RELEVANT LIQUIDITY:        pool sẽ bị sweep · inducement · T1 (H1 ERL)
POI:                       H1 POI (giá, nguồn gốc, rank)
CURRENT PRICE LOCATION:    cách POI bao nhiêu ATR(H1); z trên range H1
EXPECTED PRICE BEHAVIOR:   giá vào POI → quét [pool] → MSS phá [ITH] trên M5
WHAT MUST HAPPEN ON M5:    sweep [pool] + reclaim ≤3 nến → close > [ITH] ≤12 nến + displacement ≥3/4 → FVG
WHAT INVALIDATES:          acceptance < [distal POI] · D1 SUSPEND · hết killzone · 2 lần fail
STATUS:                    NOT READY / MONITORING / EXECUTION ELIGIBLE
```

**Cách điền:** mỗi trường phải là một *giá* hoặc một *điều kiện kiểm tra được*, không phải tính từ ("POI đẹp", "có vẻ yếu"). Nếu không điền được một trường bằng giá/điều kiện, trạng thái tối đa là MONITORING.

**Ví dụ 1 — EXECUTION ELIGIBLE (long, dựng; FX, cùng số liệu §58):**
```text
HTF CONTEXT:             Bullish · DOL 140.0 · sai nếu D1 close < 92.0
H1 STRUCTURE:            Một leg giảm từ ITH H1 126.0 vào D1 FVG 104–112; các đỉnh bên trong leg chỉ là STH (L2); chưa acceptance
SETUP DIRECTION:         LONG only
RELEVANT LIQUIDITY:      SSL H1 106.7 (đáy trong POI) · inducement EQL 120 (đã quét trên đường xuống) · T1 = ITH H1 126.0 (ITH đầu tiên phía trên)
POI:                     H1 FVG 105.5–110.0 (rank 1), nằm trong D1 FVG
CURRENT PRICE LOCATION:  107.6 — đã ở trong H1 POI
EXPECTED PRICE BEHAVIOR: quét 106.7 → MSS phá ITH M5 113.0
WHAT MUST HAPPEN ON M5:  sweep 106.7 + reclaim ≤3 nến → close > 113.0 trong ≤12 nến tính từ nến trigger + displacement ≥3/4 → FVG
WHAT INVALIDATES:        2 thân H1 < 105.5 (H1 POI fail) · 2 thân H1 < 104.0 (D1 POI fail → REASSESS) · hết NY AM KZ 10:00 NY · 2 lần thất bại
STATUS:                  EXECUTION ELIGIBLE (07:30 NY; KZ FX đã mở từ 07:00; R_proxy = (126 − 113) / (113 − 106.4) = 1.97 ≥ 1.5)
```

**Ví dụ 2 — NOT READY (short, dựng; cùng bối cảnh §59):**
```text
HTF CONTEXT:             Bearish · DOL 92.0 (range low) · sai nếu D1 close > 138.0
H1 STRUCTURE:            HH–HL hồi lên, giá 112.0; D1 FVG bearish 118–125 còn cách ~1.5 ATR(H1)
SETUP DIRECTION:         SHORT only
RELEVANT LIQUIDITY:      BSL H1 trong POI chưa hình thành rõ · T1 chưa xác định
POI:                     D1 FVG 118–125 — chưa có H1 POI refine
CURRENT PRICE LOCATION:  dưới POI; z(D1, range 92–138) = 0.43 → đang ở DISCOUNT — sai phía cho short
EXPECTED PRICE BEHAVIOR: hồi tiếp vào 118–125 (premium), tạo BSL nội bộ
WHAT MUST HAPPEN ON M5:  (chưa áp dụng)
WHAT INVALIDATES:        acceptance > 125 · D1 close > 138
STATUS:                  NOT READY — đặt alert 118.0; KHÔNG mở M5; KHÔNG long theo nhịp hồi H1
```

---

## PART IV — M5: THỰC THI

> [!important] Nhiệm vụ thật sự của M5
> M5 là khung tìm **điều kiện thực thi**, không phải nơi tự viết câu chuyện giao dịch. M5 chỉ được hỏi khi H1 đã ở trạng thái EXECUTION ELIGIBLE, và chỉ hỏi một câu: *"Tại vùng này, trong giờ này, giá đã để lại đủ bằng chứng đo được chưa?"*
>
> | M5 có thể cho biết | M5 KHÔNG thể tự xác nhận |
> |---|---|
> | Pool đã đánh dấu có bị quét và reclaim không | Hướng của ngày (bias) |
> | Nhịp giảm vào sweep có bị phủ định bằng thân nến không (MSS) | Vùng nào đáng giao dịch (POI) |
> | Chuyển động có "mạnh bất thường" không (displacement) | Target cuối (DOL) |
> | Đặt lệnh ở đâu, sai ở đâu (FVG, cực trị sweep) | Rằng giá *sẽ* đi tới target |
>
> **Vì sao một MSS M5 không đổi Daily Bias:** nó phá một swing có phạm vi vài chục phút; bias D1 dựa trên swing có phạm vi nhiều ngày. **Vì sao không phải MSS nào cũng là cơ hội:** trên M5 lúc nào cũng có một swing vừa bị phá — MSS chỉ mang thông tin khi swing đó được chọn *trước* và nằm ở *đúng chỗ*. **Vì sao entry đẹp vẫn có thể thuộc setup kém:** `[HYPOTHESIS]` HYP-12 — chất lượng của lệnh chủ yếu được quyết định ở D1/H1 (bối cảnh, vị trí, chỗ đi), còn M5 chủ yếu quyết định hình học rủi ro.

### 25. Liquidity Sweep

**Hiểu nhanh.** Giá đi quá một mức ai cũng thấy (đáy cũ), "chạm" vào các lệnh đang chờ ở đó, rồi quay lại ngay. Điều quan trọng không phải là giá *đi quá*, mà là giá *quay lại và không ở lại bên ngoài*.

**Định nghĩa vận hành (bullish; bearish đối xứng)** — dùng nhất quán trong toàn bộ note:
1. **Pool P được đánh dấu trước** (từ H1 handoff): ITL H1, EQL, PDL, session low, đáy STH rõ trong POI.
2. **Trigger:** có nến M5 với low < P.
3. **Reclaim:** trong ≤ 3 nến (HEURISTIC) có một thân nến đóng **trên** P.
4. **Không phải run:** trước reclaim, không có **acceptance** dưới P (2 thân nến liên tiếp đóng dưới P — cùng định nghĩa acceptance dùng ở mọi nơi trong note).
5. **Cực trị sweep** = low thấp nhất từ trigger tới reclaim — chỉ dùng dữ liệu tới nến reclaim. Đây là neo của stop loss.
6. **Sweep thất bại sau reclaim:** nếu trước khi có MSS, một thân nến đóng dưới cực trị sweep → chuỗi chết (cú quét đã thành run).

**Sweep khác gì breakout/run và "liquidity run":**

| | Sweep (raid) | Run / breakout | Liquidity run (ICT) |
|---|---|---|---|
| Quan sát được | Xuyên rồi đóng lại bên trong | Xuyên và được chấp nhận bên ngoài | Giá đi một mạch lấy nhiều pool liên tiếp |
| Ý nghĩa cho mô hình | **Event** cần thiết của Core | Không có setup; nếu là pool bảo vệ → báo H1 | Thường là *nhịp tới DOL*, không phải điểm vào |

**Một râu nến xuyên mức có đủ để gọi là sweep không?** Râu xuyên rồi thân đóng lại bên trong ngay trong nến đó **là** sweep theo định nghĩa trên (reclaim trong cùng nến). Nhưng sweep chỉ là **event** — nó chưa nói gì về việc phe bán đã cạn. Râu xuyên một mức *không được đánh dấu trước* thì không tính (đó là hindsight).

**Khi sweep vừa xảy ra, bạn biết gì và chưa biết gì:**
- **Đã biết** `[OBSERVABLE]`: pool đã bị giao dịch xuyên; cực trị sweep (nếu reclaim đã có); tốc độ reclaim.
- **Chưa biết**: đây là sweep hay sẽ thành run; phe bán đã cạn chưa; giá có tạo MSS không. → **Vào lệnh ngay tại sweep là vào trước khi có câu trả lời.**

![[ICT2022-v2-11-Ba-tinh-huong-tai-thanh-khoan.svg]]

| Case | Diễn biến | Phù hợp phiên bản Core? | Quyết định |
|---|---|---|---|
| **A** | Sweep → phản ứng theo hướng dự kiến | Có (mới là event) | Chờ MSS + displacement + FVG |
| **B** | Sweep → giá tiếp tục breakout (acceptance dưới P trước reclaim, hoặc thân nến đóng dưới cực trị sweep sau reclaim) | Không — sweep đã thành run | Hủy chuỗi; nếu pool là bảo vệ của POI → báo H1 REASSESS |
| **C** | Không sweep nhưng có structural break (MSS) | **Không** — thiếu event | Không vào; log `missing_step: sweep`; muốn trade → biến thể riêng (HYP-03) |

> [!info] Không khẳng định "sweep luôn phải xảy ra trước mọi MSS"
> Trên thị trường, MSS không có sweep vẫn xảy ra (tần suất trên dữ liệu của bạn: chưa đo). Phiên bản Core **chọn** đòi sweep vì giả thuyết rằng "nhiên liệu ngược đã bị tiêu thụ" làm tăng chất lượng setup — đây là **định nghĩa của phiên bản**, không phải sự thật về thị trường, và phải được kiểm định bằng so sánh A/B (HYP-03).

**Sweep không có MSS — vì sao sweep không phải tín hiệu vào lệnh:**

![[ICT2022-v2-12-Sweep-khong-MSS.svg]]

**Double / triple sweep.** Giá quét pool thứ nhất, reclaim, rồi quét tiếp một pool sâu hơn *trước khi* có MSS. Cách xử lý đúng là quy tắc chung: **sweep không bao giờ là trigger**, nên cú sweep đầu không làm bạn vào lệnh; **mss_reference cố định tại thời điểm pre-mark** (không dời xuống đỉnh thấp hơn hình thành giữa hai cú quét); cực trị sweep cập nhật theo cú sâu nhất *cho tới khi MSS xảy ra*; cửa sổ 12 nến tính lại từ nến trigger của cú quét sâu. Nếu cú sweep sâu xuyên distal POI H1 có acceptance → đó không còn là sweep mà là POI fail. (Case 7 ở §54 minh họa lệnh thắng nhờ không vào ở sweep đầu.)

### 26. Market Structure Shift (MSS)

**Hiểu nhanh.** Giá vừa đi xuống (vào cú sweep). MSS xảy ra khi giá đi lên và **đóng cửa vượt qua điểm mà nhịp giảm đó bắt đầu** — tức là toàn bộ nhịp giảm vừa rồi bị "trả lại". Phá một đỉnh nhỏ bất kỳ bên trong nhịp giảm thì chưa phải.

**Các thuật ngữ dễ trộn — và cách note này dùng chúng:**

| Thuật ngữ | Note này dùng nghĩa | Khác MSS ở đâu |
|---|---|---|
| **Structural break** | Bất kỳ lần giá vượt một swing (râu hoặc thân) | Không phân biệt cấp swing, không đòi displacement |
| **BOS** | Phá swing **theo** hướng xu hướng đang có — tiếp diễn ([[05-BOS-Break-of-Structure]]) | MSS là phá **ngược** nhịp vừa rồi |
| **MSS** | Thân nến đóng vượt **mss_reference** (ITH đánh dấu trước, gốc của leg vào sweep), **sau** reclaim, trong ≤ 12 nến M5 tính từ nến trigger sweep (nến trigger = 1), kèm displacement | — |
| **CHoCH** | Thuật ngữ SMC: lần phá đầu tiên ngược cấu trúc; nhiều nguồn không đòi displacement hay sweep ([[09-Change-of-Character]]) | Lỏng hơn MSS của note này |
| **Liquidity sweep** | Event tại pool (xem §25) | Sweep xảy ra *ở phía đối diện* của MSS |
| **Displacement** | Đặc điểm của chuyển động (§27) | Displacement có thể có mà không phá cấu trúc; MSS là sự kiện cấu trúc |

> [!note] Thuật ngữ trong cộng đồng ICT không thống nhất
> "MSS" và "CHoCH" được dùng lẫn lộn; có người đòi close, có người chấp nhận râu; có người đòi phá "swing có ý nghĩa", có người phá swing gần nhất. Note này **chọn một định nghĩa vận hành và giữ nhất quán** (ở trên). Đổi định nghĩa = tạo version mới (§62), không đổi âm thầm.

**Trả lời 9 câu hỏi để nhận diện MSS trong thời gian thực:**
1. **Cấu trúc trước MSS là gì?** — một leg giảm (trên M5) đi vào H1 POI và quét pool.
2. **Swing nào cần phá?** — **gốc của leg đi vào sweep**: ITH M5 cao nhất của leg đó, đánh dấu khi leg hình thành, *trước* sweep, và **cố định** từ đó. Nếu leg chưa có ITH M5 nào được xác nhận → mss_reference không xác định → không có setup.
3. **Vì sao swing đó quan trọng hơn swing nhỏ khác?** — vì phá nó là phủ định toàn bộ leg giảm; phá một STH bên trong leg chỉ nói leg đang hồi.
4. **Phá bằng râu có đủ không?** — Không. Râu vượt mà thân đóng dưới = structural break yếu (có thể chính là một sweep của chu kỳ khác).
5. **Khi nào cần close?** — Luôn luôn trong phiên bản này: **thân nến M5 đóng trên mss_reference**.
6. **Displacement có vai trò gì?** — phân biệt MSS có lực với "slow grind": cùng phá swing nhưng bằng chuỗi nến nhỏ chồng chéo → không có mất cân bằng ([[08-Mistake-Weak-Displacement]]).
7. **Khi nào structural break chỉ là break nhỏ?** — khi swing bị phá là STH; khi phá bằng râu; khi không có displacement; khi nó xảy ra *trước* sweep.
8. **Khi nào MSS phù hợp setup?** — xảy ra sau sweep của pool đã đánh dấu, trong H1 POI, trong killzone, cùng hướng bias.
9. **Điều gì làm MSS không còn phù hợp giả thuyết?** — thân nến đóng trở lại dưới mss_reference *trước khi* lệnh khớp (MSS failure — chỉ xảy ra được khi entry nằm dưới mss_reference, tức E2/E3); cực trị sweep bị phá.

**MSS ≠ reversal.** MSS M5 cho biết *nhịp M5 vừa rồi bị phủ định*. Nó không nói gì về việc xu hướng D1 đổi, và không đảm bảo giá đi tiếp. Nó là một mắt xích bằng chứng, không phải dự báo.

**Minh họa bullish MSS (ASCII):**
```text
            mss_reference (ITH 113.0, đánh dấu trước)
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┬ ─ ─ ─ ─
        ╲                                   │ ← thân nến đóng 113.4 (MSS)
         ╲      ╱╲                         ╱
          ╲    ╱  ╲                       ╱  ← displacement: 2 nến thân lớn
           ╲  ╱    ╲        ╱╲           ╱
            ╲╱      ╲      ╱  ╲         ╱
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─╲─ ─ ╱─ ─ ╲─ ─ ─ ╱─ ─ ─ ─  pool SSL 106.7 (đánh dấu trước)
                       ╲╱       ╲   ╱
                                 │ ← râu quét 105.6, thân đóng lại trên 106.7 (sweep)
```
- **Swing đang xét:** 113.0 — gốc leg giảm, cấp ITH M5.
- **Thuộc cấu trúc nào:** cấu trúc *nội bộ* của nhịp hồi H1; không phải cấu trúc D1.
- **Vì sao break có ý nghĩa:** nó xảy ra *sau* sweep pool đã đánh dấu, *trong* POI, bằng thân nến có displacement.
- **Điều còn chưa xác nhận:** giá có hồi về FVG không; giá có đi tới T1 không; nhịp tăng có phải chỉ là hồi kỹ thuật không.
- **Vì sao không được suy ra giá chắc chắn tăng tiếp:** MSS chỉ là một bằng chứng trong chuỗi; trên dữ liệu ngẫu nhiên chuỗi này vẫn xuất hiện (§1). Xác suất có điều kiện của "tăng tiếp" là thứ backtest phải đo.

![[ICT2022-v2-14-Sequence-Bullish-day-du.svg]]

**Bearish MSS** — đối xứng: leg tăng đi vào H1 POI premium, quét BSL đã đánh dấu (123.3 → 124.4, thân đóng lại dưới 123.3), rồi thân nến đóng **dưới** ITL đã đánh dấu (117.0) với displacement giảm, để lại bearish FVG 116.9–118.8.

![[ICT2022-v2-15-Sequence-Bearish-day-du.svg]]

**MSS không có sweep — ngoài phiên bản Core:**

![[ICT2022-v2-13-MSS-khong-Sweep.svg]]

> [!warning] Căng thẳng giữa "chờ xác nhận" và "thời gian thực"
> Playbook [[2022 Model A+ Setup]] yêu cầu MSS "giữ 3–5 nến không bị reclaim". Trong thời gian thực, chờ 3–5 nến M5 sau MSS thường **trùng đúng lúc giá hồi về FVG** — điều kiện xác nhận có thể khiến bạn bỏ lỡ phần lớn entry, hoặc tệ hơn, khiến bạn đổi entry thành market order. Đề xuất v0.2 (M-04, §62):
> - **MSS xác nhận tại close của nến MSS.**
> - **Execution Plan phát hành tại close của nến kế tiếp** — lúc đó tiêu chí ③ của displacement và FVG (nến thứ 3) đã xác nhận.
> - "Giữ không bị reclaim" chuyển thành **điều kiện hủy lệnh chờ**: thân nến đóng lại dưới mss_reference trước khi khớp → hủy.
>
> Cả hai cách đều hợp lệ như *spec*; điều không hợp lệ là chọn cách nào tùy lệnh. `[BACKTEST REQUIRED]` — so sánh hai spec trên cùng dữ liệu (HYP-16).

### 27. Displacement

**Hiểu nhanh.** Displacement là khi giá di chuyển *mạnh và dứt khoát* tới mức bỏ lại khoảng trống phía sau. Không phải nến to nào cũng là displacement — một nến to với râu dài hai đầu là giằng co dữ dội, không phải một bên áp đảo.

![[ICT2022-v2-17-Displacement-4-tieu-chi.svg]]

**Bốn tiêu chí quan sát được** (mỗi tiêu chí 1 điểm → `displacement_score` 0–4 trong template). Tiêu chí ① ② chấm trên **nến có thân lớn nhất trong leg** từ cực trị sweep tới nến MSS; ③ cần nến kế tiếp sau MSS; ④ chấm trên cả leg.

| # | Tiêu chí | Câu hỏi bằng lời | Đo (nến tăng) | Ngưỡng gợi ý (HEURISTIC) |
|---|---|---|---|---|
| ① | **Close location (CLV)** | Nến đóng gần đỉnh của nó không? | (Close − Low) / (High − Low) | ≥ 0.7 |
| ② | **Thân / range** | Thân chiếm phần lớn cây nến không? | \|Close − Open\| / (High − Low) | ≥ 65% |
| ③ | **Phá + không bị lấp ngược** | Có vượt swing đã đánh dấu và nến *kế tiếp* không đóng lại dưới mức vừa phá? | close > mss_reference; close(nến kế) > mss_reference | có |
| ④ | **FVG** | Leg có để lại khoảng trống 3 nến không? | Low(nến 3) > High(nến 1) trong leg | có |

**Hợp lệ khi ≥ 3/4** (HEURISTIC), chấm xong tại close nến kế tiếp sau MSS — cùng lúc phát hành Execution Plan (§26). Ví dụ trong hình: nến hợp lệ có CLV ≈ 0.94, thân ≈ 90%, phá và không bị lấp ngược, có FVG → 4/4. Nến "to nhưng yếu" có CLV ≈ 0.47, thân ≈ 33%, phá rồi bị đóng ngược vào trong, không FVG → 0/4.

**Biến thể định lượng — một spec thay thế, không cộng dồn với bốn tiêu chí trên** (từ [[50-Displacement-In-Depth]] và [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §12.3): đo cả leg từ cực trị sweep tới nến MSS — `leg_range / ATR(M5,20) ≥ 2.0` · `max_body_ratio ≥ 0.6` · `efficiency ≥ 0.5` · có FVG ≥ 0.2 × ATR · leg ≤ 8 nến (nếu dùng biến thể này, cửa sổ MSS thực tế là 8 nến thay vì 12). Chuẩn hóa theo ATR loại bỏ ảo giác do zoom chart và do biến động chung cao (một nến "khủng" lúc 08:30 NY có thể chỉ là 1.2 ATR khi ATR đang cao vì tin).

**Năm câu hỏi thường gặp:**
- *Displacement có cần phá cấu trúc không?* — Định nghĩa displacement (đặc điểm chuyển động) thì không; nhưng **trong Core**, displacement phải là nhịp chứa nến MSS. Displacement không phá gì chỉ là một nến mạnh.
- *MSS có thể có mà không có displacement mạnh không?* — Có (slow grind break). Theo phiên bản này: **không phát hành lệnh**.
- *Khi nào nến lớn chỉ phản ánh volatility?* — quanh tin (±5 phút tin cấp cao), rollover, mở phiên với spread giãn; râu dài hai đầu; ATR đang cao bất thường. Gắn cờ `news_displacement` và thống kê riêng.
- *Displacement có bảo đảm continuation không?* — Không. Nó là bằng chứng mất cân bằng *đã xảy ra*, không phải cam kết nó tiếp diễn.
- *Vì sao displacement quan trọng trong ICT?* `[ICT FRAMEWORK]` — được diễn giải là dấu hiệu của dòng lệnh tổ chức; `[INTERPRETATION]` hợp lý hơn: dòng lệnh một chiều mạnh hơn mức bình thường, đủ để tạo vùng chỉ giao dịch một lần.

### 28. Fair Value Gap (FVG)

![[ICT2022-v2-16-FVG-Bullish-Bearish-3-nen.svg]]

**Định nghĩa:** trong 3 nến liên tiếp, **bullish FVG** khi Low(nến 3) > High(nến 1) — vùng [High₁, Low₃]; **bearish FVG** khi High(nến 3) < Low(nến 1) — vùng [High₃, Low₁]. **CE** = trung điểm ([[10-Consequent-Encroachment-Mean-Threshold]]). Mép gần giá hiện tại là **proximal**, mép xa là **distal**.

**Ba khái niệm khác nhau — không gộp:**
- **MSS** = sự kiện cấu trúc (một swing bị phủ định).
- **Displacement** = đặc điểm của chuyển động (mạnh, dứt khoát).
- **FVG** = một cấu trúc giá cụ thể (khoảng giá một nến giao dịch).

Chúng *thường* đi cùng nhau trong setup tốt, nhưng mỗi cái có thể xuất hiện mà không có cái kia.

**Câu hỏi thực hành:**
- *FVG có bắt buộc xuất hiện sau MSS không?* — Trong Core: có — không có FVG từ leg displacement thì không có địa chỉ entry → không phát hành lệnh.
- *FVG có thể xuất hiện mà không có MSS không?* — Có, rất thường (FVG trong nhịp hồi, FVG ngược hướng). Những FVG đó không phải entry của mô hình.
- *FVG nào được dùng khi leg có nhiều FVG?* — chọn **một quy tắc cố định** cho mỗi version:

| Quy tắc | Mô tả | Ưu | Nhược |
|---|---|---|---|
| **F1 — FVG chứa/sát mss_reference** (mặc định v0.2) | Retrace về đúng chỗ cấu trúc bị phá | Có ý nghĩa cấu trúc | Có thể xa cực trị sweep → stop rộng |
| F2 — FVG đầu tiên sau sweep | FVG thấp nhất trong leg | Stop gần | Hay bị xuyên |
| F3 — FVG lớn nhất | Theo kích thước | Dễ khớp | Chọn theo kích thước là tùy tiện |

- *Vì sao không phải FVG nào cũng đáng giao dịch?* — FVG ngoài POI, FVG trong grind chậm, FVG quanh tin, FVG đã bị lấp đều không mang "dấu vết" của setup.
- *Giá có bắt buộc quay lại FVG không?* — **Không.** `[HYPOTHESIS]` HYP-13: những lần giá không quay lại có thể là những nhịp mạnh nhất — nếu đúng, lệnh limit chịu *adverse selection* (§29).
- *FVG lồng nhau (M5 trong H1 trong D1)* — xem cảnh báo ở §18: không cộng điểm ba lần.

### 29. Entry — các biến thể và các tình huống "nếu…"

Trình tự ra quyết định đầy đủ: §36 (bullish), §37 (bearish), §42 (decision tree). Ở đây chỉ bàn **kiểu entry** và **các tình huống "nếu…"**.

![[ICT2022-v2-18-Entry-FVG-E1-E2-E3.svg]]

| Entry type | Mức | Trong ví dụ | Đặc tính thống kê cần biết |
|---|---|---|---|
| **E1 — Edge** (proximal) | Mép gần của FVG | 113.10 → R ≈ 1.65 | Khớp nhiều nhất, R nhỏ nhất. Bản tóm tắt bài giảng của ICT mô tả đặt limit ở mép FVG "để chắc khớp" |
| **E2 — CE** (mặc định v0.2) | 50% FVG | 112.15 → R ≈ 2.02 | Cân bằng; bỏ lỡ nhiều hơn E1 |
| **E3 — OTE** | 62–79% (sweet spot 70.5%) của leg từ cực trị sweep tới đỉnh displacement | Leg 105.6 → 114.8 ⇒ OTE 107.53–109.10, 70.5% = 108.31 → R ≈ 5.9 nhưng **không khớp** (đáy hồi 110.9) | R lớn nhất, khớp ít nhất |
| E4 — Aggressive (market tại MSS close) | — | *ngoài Core* | Không bỏ lỡ; stop xa nhất; spec riêng ([[35-Aggressive-Displacement-Entry]]) |

> [!warning] Adverse selection — bẫy thống kê lớn nhất của entry bằng limit
> `[HYPOTHESIS]` HYP-13: lệnh limit sâu khớp *nhiều hơn* ở những setup mà giá hồi sâu — và hồi sâu có thể tương quan với luận điểm yếu; những setup giá không quay lại (có thể là mạnh nhất) thì không khớp. Hệ quả: tập lệnh *đã khớp* bị lệch về phía xấu so với tập *setup*. **Chỉ log lệnh đã khớp = đo sai.** Log cả `limit_filled: No`, `missed_by`, `would_have_result`. Đừng trộn nhiều kiểu entry trong một thống kê; đổi kiểu entry = đổi version.

**Các tình huống "nếu…":**

| Nếu… | Quyết định | Log |
|---|---|---|
| **Giá không hồi về FVG** và đi tới +1R phía target trước khi khớp | Hủy lệnh. **Không đuổi bằng market** | `limit_filled: No`, `missed_by`, `would_have_result` (dùng để tính expectancy/ngày, HYP-09) |
| Giá hồi về FVG nhưng **không phản ứng**, tiếp tục xuyên | Lệnh đã khớp → để SL làm việc (không can thiệp v0.2) | Ghi `failed_after_entry` nếu MSS fail sau khớp |
| **Setup vô hiệu trước entry**: TTL hết · hết killzone · tin đỏ sắp ra · H1 POI accept · MSS failure (thân nến đóng lại dưới mss_reference — chỉ có thể xảy ra với E2/E3). *Lưu ý:* "close dưới cực trị sweep" hay "FVG bị close xuyên" không thể xảy ra trước khi E1/E2 khớp (giá phải chạm limit trước) — chỉ áp dụng cho E3 hoặc khi có gap | Hủy lệnh chờ | `expired` / `invalidated` |
| **Entry hợp lệ nhưng không tới target** (quay đầu giữa đường) | Theo luật quản lý đã định (§31); không "cứu" lệnh bằng cách dời SL | `r_multiple` thật, MFE/MAE |

**Giá chạy thẳng không entry — bỏ lỡ không có nghĩa phải đuổi:**

![[ICT2022-v2-22-Gia-chay-thang-khong-entry.svg]]

**Setup bị vô hiệu trước entry — hủy đúng lúc:**

![[ICT2022-v2-20-Setup-vo-hieu-truoc-entry.svg]]

### 30. Stop Loss

**Quy tắc v0.2:** `SL = cực trị sweep − max(2 × spread, 0.1 × ATR(M5))` (long; short đối xứng).

**Vì sao ở đó:** nếu giá giao dịch dưới cực trị sweep, cú sweep đã trở thành run — phe bán chưa cạn — luận điểm "mất cân bằng đã lật" sai. Đây là stop **cấu trúc**, đặt ở nơi luận điểm sai, không phải nơi "an toàn".

| Biến thể | Vị trí | Khi nào xét |
|---|---|---|
| **S1 — dưới cực trị sweep** (mặc định) | Như trên | Luôn |
| S2 — dưới nến 1 của FVG | Chặt hơn | Chỉ như một biến thể có spec riêng; đổi win rate lấy R |
| S3 — dưới distal H1 POI | Rộng | Không dùng cho entry M5 (sai tầng) |

**Stop quá gần** khi: nằm *trong* H1 POI (execution POI) hoặc trong vùng retrace bình thường của OTE; chỉ cách entry vài lần spread; được chọn để R:R đẹp (Case 3 ở §54). **SL nằm trong H1 POI (execution POI) → chặn trần grade ở B.**

**Stop quá xa** khi: R(T1) < 2 — khi đó **bỏ lệnh**, không siết stop để "làm đẹp" R. R là hệ quả của SL đúng chỗ, không phải ngược lại.

**Buffer phải phản ánh chi phí thật:** spread giãn quanh rollover 17:00 NY và mở phiên London/NY, và quanh tin (Case 6 ở §54).

**Không bao giờ dời stop ra xa vì không muốn nhận lỗ.** Luật quản lý (dời BE, chốt một phần) phải được viết trước và áp như nhau cho mọi lệnh.

### 31. Target

**Quy tắc v0.2:**
1. **T1 (bắt buộc)** = đỉnh/đáy cấp ≥ L3 (ITH/ITL H1) **đầu tiên** theo hướng lệnh còn chưa bị lấy — đây là external liquidity của range H1 (đồng thời thường là internal liquidity của range D1). Không được "nhảy qua" một mức như vậy để nhắm mục tiêu xa hơn. Nếu R(T1) < 2 → không phát hành lệnh ([[05-Mistake-Not-enough-RR]]).
2. **Final target** = primary DOL của D1 (runner, nếu spec có quản lý nhiều phần).
3. **Phía ngược lại** — pool đối diện chưa bị lấy nằm ngay sau vùng SL là rủi ro "trading into unswept liquidity" ([[13-Mistake-Trading-Into-Unswept-Liquidity]], Case 4): giá có thể đi lấy nó trước. Yêu cầu sweep của Core xử lý phần lớn tình huống này; nếu sau sweep vẫn còn một pool đối diện cấp cao hơn sát SL → No Trade (§33).
4. **Target thay thế** khi DOL ban đầu không còn hợp lý (DOL bị supersede, xuất hiện pool mới chen giữa): dùng mức IRL/ITH gần nhất làm T1, tính lại R — nếu < 2 thì không vào.

**Quản lý lệnh — một xung đột cần BẠN chọn:**

> [!question] Hai spec khác nhau đang cùng tồn tại trong vault
> - [[ICT 2022 Entry Checklist]] mục D: *"1R → chốt 50% + dời SL về BE"*.
> - [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §12.7 đề xuất **không quản lý** trong giai đoạn đo baseline (full exit tại T1 hoặc SL), để tách *edge của entry* khỏi *edge của quản lý*.
>
> Note này không chọn thay bạn. Dù giữ quy tắc nào, hãy ghi `management:` vào spec và log thêm `r_if_no_management` (kết quả giả định nếu giữ tới T1/SL) — để sau 30–50 lệnh so sánh được hai cách.

**Không giả định giá chắc chắn tới target chỉ vì đã có MSS.** Target là nơi luận điểm *đúng* nếu nó đúng — không phải lời hứa.

### 32. Invalidation — sáu khái niệm không đồng nghĩa

![[ICT2022-v2-27-Phan-tang-Invalidation.svg]]

| Khái niệm | Trigger | Phạm vi |
|---|---|---|
| **Invalidation của Daily Bias** | Thân nến D1 đóng xuyên protected swing | Mọi setup cùng hướng trong ngày |
| **Invalidation của H1 setup** | Acceptance xuyên distal POI; T1 chạm trước arrival; pool ngược chiều mới chen giữa | Setup tại POI đó |
| **Invalidation của M5 entry** | Trước reclaim/MSS: close dưới cực trị sweep. Sau khi đặt lệnh: MSS fail (E2/E3) · TTL hết · hết killzone · tin đỏ (FVG close-through chỉ áp dụng cho E3/gap) | Lệnh chờ đó |
| **Stop Loss bị chạm** | Giá chạm SL sau khi đã có vị thế | Lệnh đó |
| **Giả thuyết giao dịch không còn hợp lệ** | Bất kỳ tầng trên invalid, hoặc DOL fulfilled/superseded | Mọi lệnh *mới* theo giả thuyết đó |
| **Lệnh thua nhưng tuân thủ quy trình** | Mọi bước đúng spec, SL chạm | Không gì cả — không có hành vi cần sửa |

![[ICT2022-v2-19-Entry-hop-le-cham-SL.svg]]

**Một giao dịch thua có thể vẫn là một giao dịch tuân thủ mô hình** — và trong một hệ thống có win rate < 100%, phần lớn lệnh thua *nên* là loại này. Chấm lệnh bằng `first_error_step` / `missing_step` / `followed_plan`, không bằng P&L từng lệnh.

**Wick không bao giờ invalidate; acceptance mới invalidate.** Râu xuyên một mức là dữ liệu (có thể là sweep); ≥ 2 thân nến đóng và giữ ngoài mức (HEURISTIC N = 2; quy tắc cá nhân của bạn ghi 2–3 nến) mới là vô hiệu.

### 33. Khi nào KHÔNG được vào lệnh (danh sách duy nhất)

> [!danger] NO TRADE nếu bất kỳ điều nào dưới đây đúng
> **Bối cảnh (Gate G1)**
> - D1 Neutral / Conflicting / thiếu DOL / thiếu invalidation viết ra.
> - Context Note được viết *sau* khi đã nhìn H1/M5.
> - DOL còn < 1 ATR D1 (luận điểm gần hoàn tất).
> - W1 ngược hướng *và* giá đang ở W1 POI ngược hướng.
> - Ngày có tin cấp cao (FOMC/CPI/NFP) mà không chạy spec event-mode.
>
> **Vị trí & thời gian (Gate G2)**
> - Giá chưa ở H1 POI, hoặc POI đã bị acceptance xuyên qua; arrival bằng một nến H1 đi xuyên cả POI.
> - D1 và H1 lệch pha Premium/Discount.
> - Ngoài killzone đã khai báo; tin đỏ trong ±15 phút; tuần lễ thanh khoản mỏng (nghỉ lễ Mỹ) nếu spec loại trừ.
> - R_proxy < 1.5; pool dự kiến sweep nằm dưới protected low D1 (long) / trên protected high (short).
>
> **Trigger M5**
> - Không có sweep của pool đã đánh dấu (Core) — hoặc sweep thành run.
> - Pool/mss_reference được đánh dấu *sau* khi sweep xảy ra; leg vào sweep không có ITH M5 xác nhận (mss_reference không xác định).
> - MSS phá STH thay vì ITH; phá bằng râu; ngoài cửa sổ 12 nến; displacement < 3/4; không có FVG từ leg đó.
>
> **Thực thi & rủi ro**
> - Chỉ vào được bằng cách đuổi giá (không có retrace về mức entry theo rule).
> - R(T1) < 2 khi SL đặt đúng chỗ (T1 = ITH H1 đầu tiên, không nhảy qua).
> - Pool đối diện cấp cao hơn còn nguyên sát vùng SL.
> - Confluence score 0–1 (hạng C, theo checklist hiện có).
> - Đã chạm daily loss limit / số lệnh tối đa / 2 lần thất bại trong cùng zone; đang muốn "gỡ" lệnh trước.

### 34. M5 checklist

- [ ] Trạng thái H1 = EXECUTION ELIGIBLE (không phải MONITORING).
- [ ] Pool và ITH (mss_reference) đã đánh dấu **trước** sweep — có ảnh chụp/ghi chú kèm giờ.
- [ ] Sweep: low < pool, thân đóng lại trên pool trong ≤ 3 nến, không acceptance; ghi cực trị sweep.
- [ ] MSS: thân nến đóng trên mss_reference, sau reclaim, trong ≤ 12 nến tính từ nến trigger sweep.
- [ ] Displacement ≥ 3/4 tiêu chí (chấm xong ở close nến kế tiếp sau MSS); ghi `displacement_score`; không phải nến tin.
- [ ] FVG theo quy tắc F1; ghi FVG high/low/CE.
- [ ] Entry theo `entry_type` đã chọn trước; SL = cực trị sweep − buffer; T1 = ITH H1 đầu tiên chưa bị lấy; R ≥ 2; confluence ≥ 2.
- [ ] Risk ≤ 0.5%, chưa chạm giới hạn ngày; đặt limit + TTL (12 nến / hết killzone / +1R).

---

## PART V — TÍCH HỢP

### 35. D1 → H1 → M5 trên một hình

![[ICT2022-v2-23-Quy-trinh-D1-H1-M5.svg]]

Thông tin chỉ chảy theo hai chiều có kiểm soát: **từ trên xuống** dưới dạng *tham số* (hướng, vùng, mục tiêu, mức sai), và **từ dưới lên** dưới dạng *veto* (tạm dừng, yêu cầu đánh giá lại). Không tầng nào được tự tạo lại bối cảnh của tầng trên.

### 36. Bullish setup — trình tự ra quyết định

Bảng dưới là **tiêu chí**; ví dụ đi đủ các bước với số liệu cụ thể nằm ở §58.

| # | Câu hỏi | Tiêu chí v0.2 | Nếu KHÔNG |
|---|---|---|---|
| 1 | Bối cảnh D1 cần có? | Gate G1 pass với bias Bullish: structure ITH tăng, z ≤ 0.5 hoặc tại HTF POI bullish, primary DOL phía trên, invalidation viết ra | Neutral / No Trade |
| 2 | H1 cần cho thấy gì? | Nhịp hồi đi vào D1 POI; H1 POI refine; SSL H1 trong/sát POI; T1 = ITH H1 đầu tiên phía trên | NOT READY |
| 3 | Giá cần đến vùng nào? | Arrival vào H1 POI (không xuyên cả POI bằng một nến H1) trong killzone | Chờ |
| 4 | Liquidity event nào? | Sweep pool SSL đã đánh dấu trước, reclaim ≤ 3 nến, không acceptance | Không event → không setup |
| 5 | MSS xác định thế nào? | Thân nến đóng trên ITH M5 đã đánh dấu, sau reclaim, ≤ 12 nến từ nến trigger | Hủy chuỗi |
| 6 | Displacement đóng vai trò gì? | ≥ 3/4 tiêu chí — phân biệt MSS có lực với slow grind | Không phát hành lệnh |
| 7 | FVG nào? | F1 — FVG chứa/sát mss_reference, ≥ 0.2 × ATR(M5) | Không có địa chỉ entry |
| 8 | Khi nào entry được phép? | Execution Plan tại close nến sau MSS; entry theo entry_type; R(T1) ≥ 2; confluence ≥ 2; risk ok | — |
| 9 | Khi nào tiếp tục chờ? | Trong TTL, giá chưa về mức entry | — |
| 10 | Khi nào loại bỏ? | TTL hết · hết KZ · +1R chưa khớp · MSS failure (E2/E3) · tin đỏ · H1 POI accept | Log expired / missed / invalidated |

### 37. Bearish setup — trình tự ra quyết định

Cùng 10 câu hỏi, đảo chiều. Ví dụ số liệu: §59.

| # | Tiêu chí v0.2 (short) | Điểm khác cần chú ý |
|---|---|---|
| 1 | Gate G1 pass với bias **Bearish**: LH–LL cấp ITH, z ≥ 0.5 hoặc tại HTF POI bearish, primary DOL phía dưới | Một bearish MSS M5 trong ngày D1 bullish **không** phải setup này (countertrend) |
| 2 | Nhịp hồi lên vào D1 POI bearish; H1 POI refine; BSL H1 trong/sát POI; T1 = ITL H1 đầu tiên phía dưới | H1 HH–HL trước POI là bình thường |
| 3 | Arrival vào H1 POI trong killzone | — |
| 4 | Sweep BSL đã đánh dấu: high > pool, thân đóng lại **dưới** pool ≤ 3 nến | — |
| 5 | Thân nến đóng **dưới** ITL M5 đã đánh dấu, ≤ 12 nến từ nến trigger | — |
| 6 | Displacement giảm ≥ 3/4 (CLV đo bằng (High − Close)/(High − Low)) | Nến giảm do tin thường râu dài hai đầu |
| 7 | Bearish FVG F1: High(3) < Low(1), chứa/sát mss_reference | — |
| 8 | Sell limit theo entry_type; SL = cực trị sweep **+** buffer; R(T1) ≥ 2 | Spread được tính ở phía ask khi mua đóng lệnh |
| 9–10 | Như bullish, đối xứng (MSS failure = thân nến đóng lại **trên** mss_reference) | — |

> [!tip] Điểm hay sai riêng của setup bearish
> Nhiều người "thấy" bearish MSS ở mọi nhịp hồi M5 trong ngày D1 bullish và gọi đó là "short theo M5". Đó là **countertrend** — không thuộc Core. Bearish setup Core chỉ tồn tại khi **D1 bias = Bearish**.

### 38. Các tình huống tích hợp (Scenario A–F)

#### Scenario A — HTF bullish, setup bullish
```text
D1: bullish, discount, DOL phía trên  →  H1: hồi vào POI, SSL nội bộ  →  M5: sweep → MSS → FVG  →  chờ entry theo rule
```
| | |
|---|---|
| **Bối cảnh ban đầu** | Context Note Bullish, POI D1 xác định, killzone mở trong ≤ 30 phút |
| **Đã quan sát** | Giá vào POI; H1 đã quét inducement; pool M5 rõ |
| **Chưa biết** | Sweep có thành run không; có MSS không; giá có hồi về FVG không |
| **Quyết định đúng** | MONITORING → pre-mark → ELIGIBLE → chờ trigger |
| **Điều kiện cần chờ** | Sweep + reclaim; MSS ≤ 12 nến; displacement ≥ 3/4 |
| **Vô hiệu** | Acceptance dưới distal POI; D1 SUSPEND; hết KZ |
| **Sai lầm phổ biến** | Vào ngay tại sweep; dùng MSS phá STH |
| **Bài học** | Bối cảnh tốt chỉ cho phép *tìm*; bằng chứng M5 mới cho phép *vào* |

**Vì sao kế hoạch vẫn có thể thất bại:** pool đối diện (SSL D1) chưa bị lấy và giá đi lấy nó trước; tin vĩ mô đổi regime; sweep thực chất là run do thông tin mới; DOL đã bị nhiều người nhìn thấy (reflexivity).

#### Scenario B — HTF bullish, H1 bearish correction
| | |
|---|---|
| **Bối cảnh ban đầu** | D1 Bullish; H1 đang LH–LL |
| **Đã quan sát** | H1 bearish, giá còn cách POI D1 ~1 ATR(H1) |
| **Chưa biết** | Giá có tới POI không; tới thì có phản ứng không |
| **Quyết định đúng** | NOT READY. Không short theo H1, không long sớm |
| **Điều kiện cần chờ** | Giá vào POI trong killzone |
| **Vô hiệu / đánh giá lại** | H1 đóng xuyên POI có acceptance → POI fail; xuyên protected low D1 trong phiên → SUSPEND |
| **Sai lầm phổ biến** | Coi H1 bearish là "bias đã đổi"; hoặc long ngay khi thấy một nến xanh H1 giữa đường |
| **Bài học** | H1 ngược D1 trước POI là hình học bình thường của nhịp hồi (hình 9) |

#### Scenario C — D1 bullish nhưng M5 bearish MSS
| | |
|---|---|
| **Bối cảnh ban đầu** | D1 Bullish; giá đang hồi về D1 POI; H1 LH–LL |
| **Đã quan sát** | Trên M5, một nhịp tăng nhỏ bị phá xuống bằng thân nến có displacement (bearish MSS) |
| **Chưa biết** | MSS này chỉ đổi cấu trúc nội bộ M5 (phạm vi vài chục phút) hay báo hiệu D1 đổi? — chart M5 không trả lời được |
| **Quyết định đúng** | **Không bán.** Nếu giá chưa tới POI: NOT READY. Đây gần như chắc chắn là một phần nhịp hồi đưa giá về POI |
| **Điều kiện cần chờ** | Giá tới D1/H1 POI, rồi chuỗi **bullish** theo §36 |
| **Điều kiện vô hiệu (của bias)** | Chỉ khi D1 close dưới protected low; xuyên trong phiên → SUSPEND |
| **Sai lầm phổ biến** | "Scalp ngược chiều cho vui" làm bẩn thống kê Core; đổi bias vì một MSS M5 |
| **Bài học** | M5 không có quyền đảo bias D1. Muốn trade countertrend → viết một spec riêng (vd: chỉ tại HTF POI ngược hướng, có sweep BSL cấp H1, target giới hạn ở IRL) và thống kê riêng |

#### Scenario D — D1/H1 rõ ràng nhưng không có M5 entry
| | |
|---|---|
| **Bối cảnh ban đầu** | Context hoàn hảo; giá ở H1 POI trong killzone; trạng thái EXECUTION ELIGIBLE |
| **Đã quan sát** | Không có sweep pool đã đánh dấu; hoặc có MSS nhưng displacement 2/4; hoặc không hình thành FVG |
| **Chưa biết** | Giá có tạo chuỗi hợp lệ muộn hơn trong killzone không |
| **Quyết định đúng** | **No Trade** ở thời điểm này; tiếp tục chờ trong killzone nếu zone còn armed |
| **Điều kiện cần chờ** | Một chuỗi mới: pool mới + mss_reference mới được đánh dấu trước |
| **Điều kiện vô hiệu** | Hết killzone; POI acceptance; 2 lần thất bại trong zone |
| **Sai lầm phổ biến** | "Bối cảnh đẹp thế này chắc chắn sẽ lên" → vào không trigger; hạ chuẩn displacement "cho đủ" |
| **Bài học** | Bối cảnh tốt ≠ có lệnh. Những ngày như vậy là dữ liệu quý: cho biết bối cảnh tốt dẫn tới trigger bao nhiêu % thời gian |

#### Scenario E — M5 có MSS đẹp nhưng H1 chưa ở vùng quan tâm

![[ICT2022-v2-21-No-Trade-M5-dep-H1-sai-cho.svg]]

| | |
|---|---|
| **Bối cảnh ban đầu** | D1 Bullish; H1 POI nằm thấp hơn giá hiện tại đáng kể |
| **Đã quan sát** | M5: sweep → MSS → displacement → FVG rất "sách giáo khoa" — nhưng giá ở giữa range H1, ngoài killzone |
| **Chưa biết** | Giá sẽ tăng tiếp hay hồi sâu về POI trước |
| **Quyết định đúng** | No Trade (G2 vị trí + thời gian fail) |
| **Điều kiện cần chờ** | Giá về H1 POI trong killzone |
| **Điều kiện vô hiệu** | Context D1 đổi; POI bị acceptance |
| **Sai lầm phổ biến** | "Setup đẹp thế này không vào thì phí" — chính là đảo ngược thứ tự D1 → M5 ([[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]) |
| **Bài học** | Tín hiệu M5 đẹp về hình thái không thay thế điều kiện vị trí và thời gian |

#### Scenario F — Giá đi thẳng đến target mà không tạo entry
| | |
|---|---|
| **Bối cảnh ban đầu** | Setup đủ điều kiện; Execution Plan E2 đã phát hành |
| **Đã quan sát** | Sweep → MSS → FVG; limit tại CE; giá không hồi, chạy thẳng (hình 22) |
| **Chưa biết** | Giá có quay lại CE sau đó không — thường là không trước khi tới T1 |
| **Quyết định đúng** | Hủy khi chạm +1R mà chưa khớp; log `missed` + `would_have_result` |
| **Điều kiện cần chờ** | Không có — chuỗi này đã kết thúc; chỉ một chuỗi *mới* (pool mới, mss_reference mới) mới được xét |
| **Điều kiện vô hiệu** | +1R chạm trước khớp; TTL; hết killzone |
| **Sai lầm phổ biến** | Đuổi bằng market order — đổi sang entry E4 chưa backtest, SL xa hơn, R thấp hơn |
| **Bài học** | Một lệnh missed không làm giảm expectancy *mỗi lệnh* của tập lệnh theo rule; nó làm giảm số lệnh (ảnh hưởng expectancy *mỗi ngày* — HYP-09). Entry ngoài rule thì làm bẩn dữ liệu. Đo tỷ lệ missed, đừng tiếc nó |

### 39. OTE, Killzone và các bộ lọc bổ sung

Mỗi yếu tố được trả lời bằng 7 câu hỏi: (1) core hay bộ lọc trong phiên bản này? (2) giải quyết vấn đề gì? (3) thông tin mới hay diễn đạt lại? (4) khi nào hữu ích? (5) khi nào không cần? (6) bỏ đi mô hình còn chạy không? (7) có bằng chứng thực nghiệm chưa?

| Yếu tố | (1) Vai trò v0.2 | (2) Giải quyết | (3) Mới hay lặp? | (4) Hữu ích khi | (5) Không cần khi | (6) Bỏ đi? | (7) Bằng chứng |
|---|---|---|---|---|---|---|---|
| **Killzone** ([[18-Kill-Zones]]) | **Bộ lọc bắt buộc** (quy tắc của bạn) | Chọn giờ thanh khoản cao; giảm nhiễu giờ chết | Mới — trục thời gian độc lập với giá | Phân biệt sweep "có người tham gia" với nhiễu giờ Á | Không bao giờ trong v0.2; một biến thể "mọi giờ" có thể bỏ (nguồn tóm tắt nói mô hình có thể hình thành bất cứ giờ nào) | Còn chạy theo định nghĩa Core, nhưng là phiên bản khác | Chưa — HYP-07 |
| **Premium/Discount** ([[27-Premium-Discount]]) | **Bộ lọc bắt buộc** (D1 + đồng pha H1) | Hình học rủi ro; tránh mua đắt | Một phần lặp với POI (POI tốt thường đã ở discount) | Khi range operative rõ | Khi POI đã nằm chắc ở nửa đúng của range (thông tin trùng) | Còn chạy | Chưa — HYP-01, HYP-06 |
| **OTE 62–79%** ([[26-OTE-Optimal-Trade-Entry]]) | Confluence (+1 khi CE ∩ OTE) / entry type E3 | Đo độ sâu retrace trên leg | Phần lớn **lặp** với P/D trên leg | Khi FVG nằm trong dải — hai lý do trùng một mức | Khi đã chọn E1/E2 và FVG nằm ngoài dải | Còn chạy | Chưa tìm thấy nguồn công bố kiểm định ngưỡng 62/70.5/79 |
| **FVG** | **Core** (địa chỉ entry) | Mức đặt lệnh cụ thể | — | Luôn | — | Không — mất địa chỉ entry | Chưa — HYP-08, HYP-15 |
| **Order Block** | Loại POI (H1/D1); không phải entry M5 trong v0.2 | Vùng nguồn gốc displacement | Thường trùng FVG | Khi FVG + OB (rank 2) | Khi FVG đã đủ làm POI | Còn chạy | Xem [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]] |
| **Session high/low** | Ứng viên pool để sweep | Cung cấp pool rõ trong phiên | Mới | Asian range trước London; London range trước NY | Khi đã có pool H1 rõ hơn trong POI | Còn chạy | Chưa |
| **Macro time** ([[40-Macro-Times]]) | Confluence | Siết thời gian xuống cửa sổ ~20 phút | Lặp một phần với killzone | NQ quanh 09:50–10:10 NY | FX khi killzone đã đủ lọc | Còn chạy | Chưa |
| **SMT** ([[42-SMT-Divergence]]) | Confluence | Xác nhận chéo sweep bằng tài sản tương quan | Mới (dữ liệu ngoài chart chính) | Tại điểm sweep, cặp tương quan chặt, không tin riêng | Khi một cặp có tin riêng; tương quan đứt gãy | Còn chạy | Chưa |

> [!warning] Không được khẳng định "entry chỉ hợp lệ khi OTE + FVG + Killzone + P/D cùng xuất hiện"
> Đó là *định nghĩa của một biến thể*, không phải ICT 2022 Model nói chung. Mỗi yếu tố thêm vào là một bậc tự do mới → tăng nguy cơ overfit và giảm cỡ mẫu. Thêm yếu tố bằng **ablation test** (bỏ từng yếu tố, đo thay đổi expectancy), không bằng cảm giác.

#### 39.1 Killzone theo giờ New York và giờ Việt Nam

![[ICT2022-v2-31-Killzone-NY-sang-gio-VN.svg]]

| Cửa sổ (định nghĩa theo NY) | Khi Mỹ dùng EDT (≈ 8/3 → 1/11/2026) | Khi Mỹ dùng EST (≈ 1/11/2026 → 14/3/2027) |
|---|---|---|
| London KZ 02:00–05:00 NY | 13:00–16:00 VN | 14:00–17:00 VN |
| NY AM KZ 07:00–10:00 NY (FX) | 18:00–21:00 VN | 19:00–22:00 VN |
| Index 08:30–11:00 NY | 19:30–22:00 VN | 20:30–23:00 VN |
| Ranh giới ngày 17:00 NY | 04:00 VN | 05:00 VN |

*Lưu ý:* checklist hiện có ghi "killzone 20:30–23:00 VN" — khớp cửa sổ index khi Mỹ dùng **EST**, nhưng lệch 1 giờ (thành 09:30–12:00 NY) khi Mỹ dùng **EDT**. Năm 2026 Anh lùi giờ ngày 25/10 còn Mỹ lùi giờ ngày 1/11 — tuần 25/10–1/11 London mở cửa lúc 04:00 NY thay vì 03:00 NY. Định nghĩa killzone bằng giờ NY trên chart; giờ VN chỉ để nhắc lịch. Ngày cần kiểm tra: **Mỹ** — CN thứ hai tháng 3 và CN đầu tháng 11; **Anh** — CN cuối tháng 3 và CN cuối tháng 10.

#### 39.2 Confluence scoring — GATE trước, SCORE sau

**GATE** (pass/fail, không tính điểm) = toàn bộ điều kiện Core + bộ lọc của phiên bản (§33). **SCORE** chỉ chấm sau khi GATE pass:

| # | Confluence (+1 mỗi mục) | Nguồn |
|---|---|---|
| 1 | POI rank ≥ 3 (Breaker / iFVG / Unicorn) | §18 |
| 2 | CE của FVG nằm trong dải OTE 62–79% | §39 |
| 3 | SMT divergence tại điểm sweep | [[42-SMT-Divergence]] |
| 4 | CISD xác nhận đổi trạng thái delivery trên LTF | [[41-Change-in-State-of-Delivery]] |
| 5 | Entry rơi trong macro time (không chỉ killzone) | [[40-Macro-Times]] |
| 6 | Trùng NWOG/NDOG hoặc HTF PD array | [[23-New-Day-Opening-Gap]], [[24-New-Week-Opening-Gap]] |
| 7 | Mức −2 SD projection của leg manipulation trùng T1 | [[31-Standard-Deviation]] |
| 8 | Có inducement bị quét trước POI | [[15-Inducement]] |

Khi cả *confidence* từ Gate G1 (§15) và *hạng* từ SCORE cùng đưa ra mức risk, **dùng mức thấp hơn**.

| Tổng | Hạng | Size (trần 0.5%, theo [[43-Position-Sizing]]) |
|---|---|---|
| ≥ 5 | A+ | ≤ 0.5% |
| 3–4 | A | 0.3–0.5% |
| 2 | B | ≤ 0.25% (hoặc bỏ nếu ngoài macro) |
| 0–1 | C | No Trade |

> [!warning] Ba luật chống lạm dụng điểm số
> 1. Chỉ tick confluence có mặt **tại thời điểm quyết định**, không tick sau khi giá đã chạy.
> 2. **GATE luôn thắng SCORE** — 8/8 điểm nhưng thiếu sweep vẫn là No Trade.
> 3. Điểm cao không phá luật rủi ro. (Hạng D/F trong template dùng để chấm *quy trình* sau lệnh, không phải hạng confluence.) Các trọng số +1 bằng nhau là giả định đơn giản hóa `[BACKTEST REQUIRED]`: sau 30–50 lệnh, thống kê win rate và average R **theo từng confluence** để biết cái nào thực sự có thông tin trên dữ liệu của bạn.

#### 39.3 Khác biệt theo thị trường `[INTERPRETATION — chưa đo trên dữ liệu của bạn]`

| | NQ1 / NAS100 | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Đặc tính chung | Biến động nhanh, nhiều nhịp intraday | Mượt hơn, xoay quanh handoff London → NY | Giật mạnh quanh tin vĩ mô, FVG rộng |
| Killzone thường dùng | NY AM (index 08:30–11:00 NY) | London, NY AM | London, NY AM; tránh sát tin |
| Rủi ro thực thi | Râu dài → cần buffer SL | Spread thấp trừ lúc tin/rollover | Spread & slippage cao quanh NFP/CPI/FOMC |
| Điều chỉnh thực dụng | Giới hạn số lệnh/ngày chặt; bỏ setup B ngoài macro | Kiên nhẫn chờ đúng phiên; tránh giờ Á | Ưu tiên chất lượng displacement; tính spread vào R |
| Cặp SMT | ES | GBPUSD ↔ EURUSD (thuận), DXY (nghịch) | DXY (lỏng) |

Các nhận định về "số sweep mỗi ngày" hay "số setup A+ mỗi tuần" **không được đưa vào note** vì chưa có số liệu — hãy để Daily State Log của bạn trả lời (§52).

### 40. Failure modes — vì sao mô hình thất bại

| # | Lỗi | Vì sao xuất hiện | Dấu hiệu nhận biết | Cách sửa → quy tắc ngăn lặp |
|---|---|---|---|---|
| 1 | Daily Bias tùy tiện | Muốn có bias mỗi ngày | Bias đổi theo nến D1 gần nhất | Required G1; Neutral hợp lệ (R1) |
| 2 | Chọn range vì nó làm phân tích "đẹp" | Chọn neo sau khi thấy giá | Neo đổi giữa các phiên không có sự kiện re-map | Ghi neo + lý do vào Context Note trước phiên |
| 3 | Nhầm internal với external liquidity | Không phân cấp swing | Target là EQL giữa range | Bảng §10; DOL chỉ chọn từ pool cấp ≥ L4 |
| 4 | Gán DOL chắc chắn khi có nhiều mục tiêu mâu thuẫn | Thiên lệch xác nhận | Không ghi secondary DOL | Luôn ghi primary + secondary + điểm yếu (§11) |
| 5 | Dùng mọi swing nhỏ để kết luận structure | Không phân cấp | Gọi "MSS D1" khi phá STH | STH/ITH/LTH (§7) |
| 6 | Xuống M5 quá sớm | Sốt ruột | Mở M5 khi giá còn xa POI | 3 trạng thái (§23) |
| 7 | Tìm tín hiệu M5 khi giá chưa tới POI | Đảo thứ tự phân tích | MSS "đẹp" ngoài POI | G2 vị trí (Scenario E) |
| 8 | Nhầm sweep với MSS | Coi event là confirmation | Vào ngay tại râu quét | Sweep ≠ trigger (§25) |
| 9 | Nhầm displacement với MSS | Coi nến to là đổi cấu trúc | Vào khi chưa close qua ITH | §26–27 tách hai khái niệm |
| 10 | Cho rằng FVG nào cũng phải được lấp | Hiểu sai "imbalance" | Đuổi lệnh vì "chắc chắn sẽ về" | Giá không bắt buộc quay lại (§28) |
| 11 | Đánh đồng MSS với đảo chiều | Ngôn ngữ ICT | Đổi bias sau MSS M5 | MSS ≠ reversal (§26) |
| 12 | Vào lệnh khi setup chưa hoàn chỉnh | FOMO | `missing_step` ≠ none ở lệnh đã vào | Checklist §34 + log setup bị loại |
| 13 | Bỏ qua invalidation | Không viết trước | Gồng lệnh "chờ quay lại" | Invalidation trong Context Note & Execution Plan |
| 14 | Di chuyển stop loss tùy ý | Sợ lỗ | SL lệnh thua khác SL kế hoạch | SL cấu trúc, không dời ra xa (§30) |
| 15 | Đổi Daily Bias vì một tín hiệu M5 | Tầng dưới "đảo" tầng trên | Bias đổi trong phiên | Chỉ D1 close đổi cấu trúc; M5 chỉ SUSPEND |
| 16 | Nhìn chart sau khi giá chạy rồi chọn swing để giải thích | Hindsight | Pool/ITH không có timestamp | Pre-mark có ảnh chụp kèm giờ (§50) |
| 17 | Chỉ lưu giao dịch đẹp | Survivorship | Log ít ngày hơn số ngày giao dịch | Log mọi ngày (Daily State Log) |
| 18 | Đổi definition sau mỗi lệnh thua | Muốn "sửa" mô hình | Nhiều luật mới không có version | Version control §62; đổi = version mới |
| 19 | Thêm quá nhiều bộ lọc | Mỗi lệnh thua sinh một bộ lọc | Mẫu teo lại, edge "đẹp" trên in-sample | Ablation + out-of-sample (§52) |
| 20 | Nhầm một lệnh thắng với bằng chứng có edge | Outcome bias | "Lần này đúng" làm tăng size | ≥ 30–50 mẫu/biến thể, Wilson CI (§53) |

**Edge case vận hành bổ sung** (gộp từ bản cũ — chỉ giữ những ca không trùng 20 lỗi trên):

| Edge case | Cơ chế | Xử lý |
|---|---|---|
| Displacement lấp FVG ngay | Nến kế tiếp lấp gần hết khoảng trống | FVG đã tiêu; không đuổi; chờ chuỗi mới nếu zone còn |
| Gap cuối tuần / tin nhảy qua POI | NWOG/NDOG hoặc cú nhảy tin làm limit không khớp hoặc khớp xấu | Tính lại R sau gap; không giữ limit/SL cũ |
| Tin ra giữa lúc chờ retrace | Volatility phá cấu trúc vừa dựng | Hủy limit trước tin đỏ; chờ chuỗi mới sau tin |
| Spread giãn tại mở phiên / rollover 17:00 NY | SL tính theo mid, khớp theo bid/ask | Buffer SL lớn hơn quanh mốc; hoặc tránh entry ±5 phút quanh mốc (Case 6) |
| DST lệch giờ | Mỹ và Anh đổi giờ khác tuần | Giờ NY trên chart; kiểm các ngày đổi giờ ở §39.1 (Case 5) |
| Tuần nghỉ lễ Mỹ | Thanh khoản mỏng, "sweep/displacement" giả | Hạ size hoặc đứng ngoài; tách khỏi mẫu backtest chính |
| SMT giả do tin riêng một cặp | Phân kỳ do tin đơn lẻ | Loại SMT nếu một cặp có tin riêng trong 30–60 phút |
| Limit CE không khớp vì giá chỉ chạm mép | Không phải FVG nào cũng hồi tới CE | Không phải lỗi — log `missed` |
| CE vs full-fill khác theo regime | Trend mạnh: hồi nông; range: hồi sâu | Đây là lý do phải chọn một entry_type và đo theo regime, không đổi tùy ý |
| Backtest vs live lệch nhau | Spread cố định trong backtest vs spread thật + slippage | Backtest với chi phí xấu hơn thực tế; chênh lệch expectancy là bình thường |

### 41. Những hiểu lầm phổ biến

| Hiểu lầm | Thực tế |
|---|---|
| "ICT 2022 Model = sweep + MSS + FVG trên M5" | Đó là phần *trigger*. Mô hình bắt đầu từ bối cảnh; trigger không bối cảnh xuất hiện cả trên dữ liệu ngẫu nhiên |
| "Có đủ 7 bước là thắng" | Đủ chuỗi chỉ cho phép đặt lệnh có R xác định; kết quả từng lệnh vẫn là xác suất |
| "Bias là dự báo hướng ngày" | Bias là chính sách cấp phép; đánh giá bằng expectancy có điều kiện |
| "Discount là vùng mua" | Discount là vị trí *được phép xét* mua |
| "Smart money săn stop của retail" | Chart không cho thấy tác nhân hay ý định; chỉ cho thấy giá xuyên mức rồi quay lại |
| "Thêm confluence = tăng xác suất" | Mỗi confluence là một bậc tự do; chỉ có giá trị nếu dữ liệu nói vậy |
| "Killzone/OTE là bắt buộc trong mọi ICT 2022 Model" | Chúng là bộ lọc của *phiên bản* bạn chọn |

(Các hiểu lầm "giá luôn quay lại FVG", "thua vài lệnh = mô hình hỏng", "lệnh thắng là lệnh đúng" đã nằm trong failure modes #10 và #20.)

---

## PART VI — QUY TẮC VẬN HÀNH

### 42. Decision tree hoàn chỉnh

![[ICT2022-v2-24-Decision-Tree.svg]]

**Giải thích từng nhánh:**

| Câu | Thuộc | Vì sao câu này đứng ở đây | Nhánh KHÔNG nghĩa là |
|---|---|---|---|
| 1. Cấu trúc đọc được bằng ITH/LTH? | Gate G1 — Core | Không đọc được câu chuyện thì không có gì để kế thừa | Neutral; viết kịch bản "nếu…thì…" |
| 2. Range + pool + DOL + invalidation đã ghi? | Gate G1 — Core | H1 cần tham số cụ thể, không cần cảm giác | Tiếp tục ở D1 |
| 3. Bias ∈ {Bullish, Bearish} và vị trí phù hợp? | Gate G1 — Core + bộ lọc P/D | Bias ở sai vị trí là bias chưa dùng được | Conflicting → chờ vị trí |
| 4. Có H1 POI hợp lệ trong vùng D1? | Gate G2 — Core | Location thực thi | Chờ / POI kế / REASSESS |
| 5. Giá đang vào POI + killzone mở (hoặc mở trong ≤ 30')? | Gate G2 — Core + bộ lọc thời gian | Arrival + đồng hồ | NOT READY |
| 6. Pre-mark xong, R_proxy ≥ 1.5, không tin đỏ? | Gate G2 — vận hành | Chống hindsight; sàng lọc chỗ đi bằng dữ liệu đã có | Ở MONITORING |
| 7. Sweep pool đã đánh dấu? | Trigger — Core | Event | Hủy chuỗi |
| 8. MSS close vượt ITH ≤ 12 nến (từ nến trigger)? | Trigger — Core | Structural evidence | Hủy chuỗi |
| 9. Displacement ≥ 3/4 + FVG? | Trigger — Core | Delivery evidence + địa chỉ | Không phát hành lệnh |
| 10. Entry/SL/T1 theo entry_type, R ≥ 2? | Execution — bộ lọc R | R là hệ quả của SL đúng chỗ | No Trade |
| 11. Risk check? | Lớp rủi ro (ưu tiên trên phân tích) | Bảo vệ tài khoản | No Trade |
| 12. Khớp trước TTL / +1R / invalid? | Execution | Luận điểm có tính thời gian | Hủy, log |

Decision tree này là **quy trình của phiên bản Core v0.2**, không phải chuỗi sự kiện bắt buộc của mọi biến thể ICT. Một biến thể khác (vd MSS-only) sẽ bỏ câu 7 — và phải được thống kê riêng.

### 43. Pre-trade checklist (trước phiên)

Làm 15–30 phút trước killzone; hoàn tất *trước* khi nhìn H1/M5 của ngày.

- [ ] Kiểm tra lịch tin (tin đỏ, giờ) và DST tuần này.
- [ ] Kiểm tra lớp rủi ro: daily/weekly limit, số lệnh còn lại, trạng thái circuit breaker ([[Daily Risk & Circuit Breaker Checklist]]).
- [ ] D1: structure (ITH/LTH), range operative + EQ + z, pool hai phía, primary/secondary DOL, bias, HTF POI, invalidation → **viết Context Note** (§14).
- [ ] Gate G1: Required đủ? Disqualifying không? Confidence → size tối đa.
- [ ] Viết **cả kịch bản ngược** ("nếu SSL D1 bị lấy rồi acceptance thì…") — để không bị bất ngờ.
- [ ] Ghi killzone sẽ theo dõi và **giờ dừng tìm setup mới**.

### 44. Setup monitoring checklist (trong phiên, trước trigger)

- [ ] Context Note còn hiệu lực? (không có hard event, không SUSPEND)
- [ ] H1: giá đang hồi về POI hay đang phá POI? Inducement đã bị lấy?
- [ ] H1 POI refine + rank; pool sẽ bị sweep; T1 = ITH H1 đầu tiên chưa bị lấy; R_proxy.
- [ ] Trạng thái: NOT READY / MONITORING / EXECUTION ELIGIBLE — ghi kèm giờ.
- [ ] Khi MONITORING: đánh dấu pool + ITH trên M5 **trước sweep**, chụp ảnh có timestamp.
- [ ] Không "nhảy qua" một ITH H1 nào khi chọn T1; không có pool đối diện cấp cao hơn còn nguyên sát vùng SL dự kiến.

### 45. Entry checklist — thẻ Execution Plan (điền khi §34 đã pass)

§34 là danh sách CÓ/KHÔNG; thẻ dưới đây là bản ghi các giá trị — để lệnh có thể audit lại được.

```text
EXECUTION PLAN — [SYMBOL] — [ngày] — phát hành lúc [giờ NY] (close nến sau MSS)
Pool / pre-mark lúc:   [giá] / [giờ]        mss_reference / pre-mark lúc: [giá] / [giờ]
Sweep:                 trigger [giờ] · reclaim [giờ] · cực trị [giá]
MSS:                   nến [giờ], close [giá]        Displacement: [_/4]
FVG (F1):              [low]–[high], CE [giá]
Entry type / giá:      [E1/E2/E3] @ [giá]
SL:                    [cực trị] − max(2×spread [..], 0.1×ATR(M5) [..]) = [giá]
T1 / R:                [giá] (ITH H1 đầu tiên) · R = [..] (≥ 2)
Confluence / hạng:     [_/8] → [A+/A/B]      Risk: [..]% (= min(confidence G1, hạng))
Order TTL:             hủy nếu: 12 nến sau MSS ([giờ]) · hết KZ ([giờ]) · chạm +1R [giá] chưa khớp · MSS failure
```

Thẻ bấm nhanh trong phiên: [[ICT 2022 Entry Checklist]]; gate theo state machine: [[ICT 2022 State Machine Gate Checklist]].

### 46. Trade management checklist

- [ ] Luật quản lý của spec đang chạy: `management: none_full_T1` hoặc `partial50_1R_BE` — **viết trước, không đổi trong lệnh**.
- [ ] Không dời SL ra xa. Không thêm vị thế để "trung bình giá".
- [ ] Nếu Context Note bị invalidated trong khi đang có lệnh: theo v0.2, để SL làm việc và ghi nhận (không thoát cảm tính); nếu muốn có luật thoát sớm → tạo spec riêng và test.
- [ ] Ghi `exit_price` đo thật, `spread_cost`, `r_net` — không copy từ TP kế hoạch.
- [ ] Ghi MFE/MAE (dùng để đánh giá vị trí SL và T1 sau này).

### 47. Post-trade review — và nghi thức hằng tuần

**Sau mỗi phiên (kể cả không có lệnh):**
- [ ] Log ngày vào Daily State Log: dừng ở trạng thái nào (S0 / G1 fail / NOT READY / MONITORING / trigger fail / lệnh).
- [ ] Mỗi lệnh: `step1…step7_ok`, `first_error_step`, `missing_step`, `chained_fully`, `followed_plan`.
- [ ] Mỗi setup bị loại: bước dừng, lý do.
- [ ] Mỗi lệnh không khớp: `limit_filled: No`, `missed_by`, `would_have_result`.

**Bảy bước của log (`step1_ok` … `step7_ok` trong template) ↔ quy trình v0.2:**

| Trường | Bước | Đúng khi |
|---|---|---|
| `step1_bias_ok` | Bias | Gate G1 pass, bias chấm ex-ante theo Context Note |
| `step2_draw_ok` | Draw (DOL) | Primary DOL hợp lệ (≥ L4), không có pool đối diện quan trọng bị bỏ qua |
| `step3_sweep_ok` | Sweep | Pool đánh dấu trước, sweep theo §25 |
| `step4_displacement_ok` | MSS + displacement | MSS theo §26, displacement ≥ 3/4 |
| `step5_poi_ok` | POI / FVG | Arrival đúng H1 POI; FVG theo F1 |
| `step6_entry_ok` | Entry | Đúng entry_type, không chase, SL đúng chỗ |
| `step7_target_ok` | Target | T1 = ITH H1 đầu tiên; quản lý theo spec |

**Phân biệt hai trường chẩn đoán:**
- **`missing_step`** — mắt xích **vắng mặt hoàn toàn** khi bạn vẫn vào lệnh (vd không có sweep). Đo: "loại setup thiếu nào tôi hay vào?"
- **`first_error_step`** — mắt xích **đầu tiên bị làm sai** (kể cả khi chuỗi đủ). Đo: "lỗi thực thi sớm nhất của tôi nằm ở đâu?" Một lệnh có thể `chained_fully: Yes` mà `first_error_step: entry` (Case 1).

**Nghi thức Weekly Review** (trong [[Weekly_Trading_Review_ICT_Obsidian]] / Weekly Summary):
1. Lọc lệnh Loss/BE trong tuần; đếm tần suất mỗi giá trị `first_error_step` và `missing_step`.
2. Giá trị nào chiếm > 40% lệnh thua → **ưu tiên sửa số 1** của tuần sau, gắn `[[NN-Mistake-…]]` tương ứng.
3. Đếm số ngày dừng ở từng trạng thái → biết "phễu" của bạn (bao nhiêu ngày có bối cảnh, bao nhiêu tới trigger, bao nhiêu tới lệnh).
4. Sau 4–6 tuần, tần suất một `first_error_step` cụ thể phải giảm — đó là bằng chứng kỷ luật đang cải thiện, không phải cảm giác.

### 48. Quy tắc rút gọn — mỗi quy tắc có lý do, ví dụ, ngoại lệ và cách kiểm tra

> [!note] Đây là quy tắc vận hành do người nghiên cứu chọn cho phiên bản v0.2, không phải quy luật thị trường. Mỗi quy tắc có thể bị bác bỏ bởi dữ liệu.

**R1 — Nếu D1 chưa có bối cảnh đủ rõ, không ép Daily Bias.**
- *Vì sao:* bias ép buộc biến nhiễu thành "hướng", làm mọi tầng dưới sai theo.
- *Đúng:* giá ở EQ, hai DOL ngang nhau → ghi Neutral, viết kịch bản. *Sai:* "hôm qua nến xanh nên hôm nay bullish".
- *Ngoại lệ:* không có — Neutral luôn hợp lệ.
- *Kiểm tra:* so expectancy của setup trong ngày "bias tier cao" vs "bias tier thấp"; nếu không khác → tiêu chí bias không có thông tin.

**R2 — Viết Context Note trước khi mở H1/M5.**
- *Vì sao:* chống đảo thứ tự và hindsight. *Đúng:* note có giờ viết trước killzone. *Sai:* sửa note sau khi thấy M5.
- *Ngoại lệ:* re-map sau sự kiện cấu trúc — ghi thành phiên bản note mới, có giờ.
- *Kiểm tra:* tỷ lệ note có timestamp trước phiên (mục tiêu 100%).

**R3 — Nếu giá chưa đến vùng quan tâm, tiếp tục chờ.**
- *Vì sao:* vị trí quyết định hình học rủi ro. *Đúng:* đặt alert, đóng M5. *Sai:* "giá chắc chắn tới POI, vào sớm cho chắc".
- *Ngoại lệ:* không có trong Core.
- *Kiểm tra:* so kết quả giả định của setup ngoài POI (log ở trạng thái bị loại) với setup trong POI.

**R4 — Mở M5 để quan sát ≠ được vào lệnh.**
- *Vì sao:* tách chuẩn bị khỏi thực thi. *Đúng:* MONITORING → pre-mark. *Sai:* thấy MSS trong lúc MONITORING là vào.
- *Ngoại lệ:* không có.
- *Kiểm tra:* tỷ lệ lệnh có `status` ELIGIBLE tại thời điểm vào (mục tiêu 100%).

**R5 — Nếu H1 chưa tạo cơ hội phù hợp, không tìm entry chỉ vì M5 có MSS.**
- *Vì sao:* M5 không có quyền tự tạo vị trí; MSS ở sai chỗ mang thông tin rất ít.
- *Đúng:* Scenario E → No Trade. *Sai:* "MSS đẹp quá".
- *Ngoại lệ:* không có trong Core.
- *Kiểm tra:* expectancy giả định của "MSS ngoài POI" (log) vs "MSS trong POI".

**R6 — Sweep là event, không phải trigger.**
- *Vì sao:* tại sweep, chưa biết sweep hay run (§5). *Đúng:* chờ MSS. *Sai:* vào tại râu quét (Case 2).
- *Ngoại lệ:* biến thể "sweep entry" có spec riêng — không trộn.
- *Kiểm tra:* HYP-05: entry tại sweep vs entry sau MSS — expectancy và MAE.

**R7 — MSS chỉ tính khi thân nến vượt ITH đã đánh dấu trước sweep.**
- *Vì sao:* biến MSS từ "nhãn tìm sau" thành "dự báo có thể sai". *Đúng:* ITH 113.0 đánh dấu lúc 07:25 NY, sweep 07:45. *Sai:* chọn swing sau khi thấy giá đi lên.
- *Ngoại lệ:* không có; nếu leg chưa có ITH xác nhận thì không có setup.
- *Kiểm tra:* audit timestamp pre-mark trên mọi lệnh.

**R8 — Nếu M5 chưa đáp ứng điều kiện xác nhận đã chọn, không vào lệnh.**
- *Vì sao:* "gần đủ" là cách ngưỡng bị hạ dần mà không ai ghi lại.
- *Đúng:* displacement 2/4 → không phát hành lệnh. *Sai:* "gần đủ rồi".
- *Ngoại lệ:* không có — muốn ngưỡng khác thì tạo version mới.
- *Kiểm tra:* phân bố `displacement_score` của lệnh đã vào (không được có giá trị < 3).

**R9 — Entry theo một entry_type chọn trước; giá không về thì bỏ lỡ, không đuổi.**
- *Vì sao:* đổi kiểu entry giữa chừng = chạy nhiều hệ thống trong một thống kê. *Đúng:* Scenario F. *Sai:* market order sau khi giá "bỏ chạy".
- *Ngoại lệ:* biến thể E4 (aggressive) có spec và thống kê riêng.
- *Kiểm tra:* tỷ lệ missed theo entry_type; so `would_have_result` với lệnh thật.

**R10 — SL ở nơi luận điểm sai; nếu R < 2 thì bỏ lệnh, không siết SL.**
- *Vì sao:* R là hệ quả của SL đúng chỗ; siết SL làm R đẹp trên giấy nhưng biến nhịp hồi bình thường thành lệnh thua.
- *Đúng:* SL dưới cực trị sweep. *Sai:* SL ở mép POI để R:R 3 (Case 3).
- *Ngoại lệ:* biến thể S2 có spec riêng.
- *Kiểm tra:* MAE của lệnh thắng: nếu nhiều lệnh thắng có MAE vượt mức SL "chặt" → SL chặt sẽ biến chúng thành lệnh thua.

**R11 — Nếu setup bị invalidated trước entry, hủy setup.**
- *Vì sao:* luận điểm "mất cân bằng vừa lật" có tính thời gian; lệnh khớp muộn là giả thuyết khác.
- *Đúng:* TTL hết → hủy (hình 20). *Sai:* để lệnh treo qua phiên.
- *Ngoại lệ:* không có.
- *Kiểm tra:* kết quả giả định của lệnh "lẽ ra đã hủy" (log `expired` kèm `would_have_result`).

**R12 — Mỗi lệnh được chấm theo quy trình, không theo kết quả.**
- *Vì sao:* kết quả từng lệnh là nhiễu. *Đúng:* lệnh thua tuân thủ = `first_error_step: none`. *Sai:* "thắng nên đúng".
- *Ngoại lệ:* không có.
- *Kiểm tra:* tương quan giữa `followed_plan` và r_multiple sau ≥ 50 lệnh — nếu tuân thủ không tốt hơn, chính quy trình cần xem lại.

---

## PART VII — KIỂM CHỨNG

### 49. Định nghĩa khách quan (đo được)

Mục tiêu: **hai người độc lập chạy trên cùng dữ liệu phải ra cùng một danh sách setup.** Mọi ngưỡng dưới đây là `HEURISTIC` v0.2 — chọn trước, test sau, đổi thì tăng version.

| Đối tượng | Định nghĩa vận hành v0.2 | Thời điểm được dùng (confirmed_at) |
|---|---|---|
| **STH** | Nến có high > high hai nến kề (low < low hai nến kề) | Khi nến bên phải đóng |
| **ITH / ITL** | STH có STH thấp hơn ở cả hai bên (ITL đối xứng) | Khi STH bên phải đã xác nhận |
| **LTH / LTL** | ITH có ITH thấp hơn hai bên | Khi ITH bên phải đã xác nhận |
| **Dealing range D1** | Range nhỏ nhất có 2 neo cấp ≥ L4 chứa cả giá hiện tại và primary DOL | Tại cutoff trước phiên |
| **z (vị trí)** | (giá − range low) / (range high − range low) | Tại cutoff |
| **Pool** | ITL/ITH H1, EQL/EQH (hai đỉnh/đáy cách nhau ≤ 0.1 × ATR(H1)), PDL/PDH, session high/low | Khi được đánh dấu (ghi giờ) |
| **Sweep** | low < P; thân đóng > P trong ≤ 3 nến M5; trước reclaim không có acceptance dưới P | Tại nến reclaim |
| **Cực trị sweep** | min(low) từ nến trigger tới nến reclaim | Tại nến reclaim |
| **MSS** | Thân nến M5 đóng > mss_reference (ITH gốc của leg vào sweep, đánh dấu trước sweep, cố định); sau reclaim; ≤ 12 nến tính từ nến trigger sweep (nến trigger = 1) | Tại close nến MSS |
| **Displacement** | ≥ 3/4: ① CLV ≥ 0.7 và ② thân ≥ 65% range (chấm trên nến thân lớn nhất của leg) · ③ phá mss_reference và nến kế tiếp không đóng lại dưới · ④ có FVG. *Spec thay thế (không cộng dồn):* leg ≥ 2 × ATR(M5,20), max body ≥ 0.6, efficiency ≥ 0.5, FVG ≥ 0.2 × ATR, ≤ 8 nến | Tại close nến kế tiếp sau MSS |
| **FVG** | Bull: Low₃ > High₁, kích thước ≥ 0.2 × ATR(M5); chọn theo F1 | Tại close nến 3 |
| **Entry** | E1 proximal / E2 CE / E3 OTE 70.5% — chọn một cho cả version | Tại phát hành lệnh |
| **SL** | Cực trị sweep − max(2 × spread, 0.1 × ATR(M5)) | Tại phát hành lệnh |
| **T1** | H1 ERL đầu tiên theo hướng lệnh; yêu cầu R ≥ 2 | Tại phát hành lệnh |
| **Order TTL** | Hủy nếu: 12 nến M5 sau MSS · hết killzone · giá chạm +1R chưa khớp · thân nến đóng lại **dưới** (long) / **trên** (short) mss_reference trước khi khớp (chỉ xảy ra được với E2/E3) | Liên tục |
| **Acceptance (vô hiệu một mức/vùng)** | ≥ 2 thân nến liên tiếp đóng ngoài mức, không reclaim | Tại close nến thứ 2 |
| **Killzone** | London 02:00–05:00 NY; NY AM 07:00–10:00 NY (FX) / 08:30–11:00 NY (index) | Đồng hồ NY |
| **R_proxy** (sàng lọc trước trigger) | (T1 − mss_reference) / (mss_reference − (pool − buffer)) ≥ 1.5 (long; short đối xứng) | Tại pre-mark |
| **Quy ước giờ** | Giờ của nến = giờ **mở** nến (như TradingView); nến M5 "08:00" đóng lúc 08:05 | — |

> [!info] Mọi ngưỡng thời gian tròn (3 nến, 12 nến) phải được kiểm bằng *hazard analysis*
> Vẽ tỷ lệ "setup còn thành công" theo số nến chờ. Đường cong rơi rõ sau k nến → k là TTL tự nhiên; phẳng → TTL không quan trọng; tăng → bạn đang cắt bỏ những setup tốt nhất.

### 50. Nhận diện trong thời gian thực

![[ICT2022-v2-25-Timeline-Real-time-B1-B8.svg]]

*(Protocol gọi các mốc này là T1–T8; note đổi thành **B1–B8** — "bước" — để không trùng với T1 = Target 1.)*

```text
B1: D1 context identified           → Context Note (giờ viết)
B2: H1 setup becomes relevant       → H1 Handoff, status NOT READY → MONITORING
B3: Price reaches monitored area    → arrival; pre-mark pool + ITH (ảnh chụp có giờ)
B4: Liquidity event occurs, if any  → sweep + reclaim (hoặc run / không có)
B5: MSS candidate appears           → close vượt ITH? displacement score?
B6: Entry conditions satisfied?     → Execution Plan (entry, SL, T1, R, TTL) hoặc không
B7: Entered / rejected / skipped    → khớp · hủy (expired/invalidated) · missed
B8: Outcome recorded                → R thật, MFE/MAE, first_error_step, missing_step
```

**Swing candidate vs swing confirmed.** Tại hard right edge, swing gần nhất luôn là *ứng viên*. Một STH chỉ được xác nhận khi nến bên phải đóng; ITH khi STH bên phải đã xác nhận. Quy tắc: **một đối tượng chỉ được dùng từ thời điểm `confirmed_at` của nó.**

**Ghi nhận setup không hoàn thành:** mỗi setup dừng ở T2–T6 vẫn là một dòng log với `stopped_at` và lý do. Không có những dòng này, bạn không đo được phễu và không tính được selection bias.

### 51. Look-ahead bias

![[ICT2022-v2-26-Look-ahead-Swing-xac-nhan.svg]]

**Bốn nguồn phổ biến nhất trong backtest ICT thủ công** và cách chặn:

| Nguồn | Ví dụ | Chặn bằng |
|---|---|---|
| Swing được "thấy" trước khi xác nhận | Gắn nhãn ITH tại chính nến đỉnh | `confirmed_at`; replay từng nến |
| Chọn range/DOL sau khi thấy giá đi | Range được chọn sao cho giá "vừa đúng discount" | Context Note có giờ, trước phiên |
| Cực trị/mức tính bằng dữ liệu sau entry | Sweep extreme = đáy thấp nhất cả đoạn, kể cả nến sau entry | Định nghĩa "chỉ dùng dữ liệu tới nến k" |
| Chấm `bias_correct` sau khi biết kết quả | 21/22 lệnh "bias đúng" trong audit 01c | Chấm ex-ante theo Context Note |

[[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §4.6 ghi nhận một lỗi look-ahead tinh vi trong chính detector của nó đã tạo ra "edge" +0.10R với sai số chuẩn 0.016 — tức "có ý nghĩa thống kê" — **trên dữ liệu hoàn toàn ngẫu nhiên**. Cách nhanh nhất để "tìm thấy" lợi thế là ghi sổ sai.

### 52. Thiết kế backtest

#### 52.1 Xác định phiên bản mô hình trước khi chạy

| Hạng mục | Giá trị v0.2 |
|---|---|
| Thị trường | EURUSD, GBPUSD, XAUUSD, NQ1 — **thống kê riêng từng thị trường** |
| Timeframe | D1 (context) · H1 (setup) · M5 (execution) |
| Daily Bias | Gate G1 v0.2 (§15) |
| Dealing range | §49 |
| Liquidity / DOL | Pool cấp ≥ L4 cho DOL; primary + secondary + horizon |
| H1 setup | §21; trạng thái theo §23 |
| Sweep / MSS / Displacement / FVG | §49 |
| Entry | E2 CE (mặc định) — chạy E1, E3 như biến thể riêng |
| SL / Target | S1 / T1 (R ≥ 2) |
| Quản lý | Chọn một: `none_full_T1` hoặc `partial50_1R_BE` |
| Bộ lọc thời gian/bối cảnh | Killzone; tin đỏ ±15'; loại trừ tuần nghỉ lễ Mỹ (ghi rõ) |
| Chi phí | Spread + slippage **xấu hơn** thực tế (vd spread × 1.5 quanh mốc phiên) |

**Không đổi bất kỳ định nghĩa nào giữa chừng.** Muốn đổi → dừng, tăng version, chạy lại từ đầu trên dữ liệu đó (hoặc chỉ chạy tiếp trên dữ liệu mới).

#### 52.2 Dữ liệu cần thu thập

Schema đầy đủ đã có trong [[Backtest template - POI & Step Decision (ICT 2022)]] — note này không chép lại. Ánh xạ giữa các trường protocol yêu cầu và trường template:

| Trường protocol | Trường template | Bắt buộc cho câu hỏi nào |
|---|---|---|
| Date, Instrument, Session | `trade_date`, `symbol`, `session` | Mọi câu hỏi |
| D1 Structure, Daily Bias | `htf_bias`, `bias_correct` (chấm ex-ante) | HYP-01, giá trị của bias |
| Dealing Range, Location | `poi_location` (+ đề xuất thêm `z_d1`) | HYP-01 |
| Relevant Liquidity, DOL | `step2_draw_ok` (+ đề xuất `primary_dol`, `dol_hit_before_inv`) | HYP-02 |
| HTF POI, H1 setup | `poi_type`, `poi_rank`, `poi_timeframe` | POI analytics |
| M5 Liquidity Event | `liquidity_swept`, `sweep_type`, `step3_sweep_ok` | HYP-03, HYP-05 |
| MSS, Displacement, FVG | `mss`, `displacement`, `displacement_score`, `fvg_valid`, `fvg_high/low`, `ce_price` | HYP-04, HYP-08 |
| Entry, SL, Target, R | `entry_type`, `entry_price`, `stop_loss`, `take_profit`, `r_planned`, `r_multiple`, `r_net` | Expectancy |
| Fill | `limit_filled`, `fill_depth_pct`, `missed_by` | Adverse selection |
| MFE / MAE | (đề xuất thêm `mfe_r`, `mae_r`) | Vị trí SL/T1 |
| Invalidation, Rule violations | `first_error_step`, `missing_step`, `followed_plan` | Chẩn đoán |

**Trường đề xuất bổ sung** (không có trong template hiện tại; thêm khi bạn sẵn sàng đổi template): `pd_aligned_d1_h1`, `fvg_rule`, `would_have_result`, `stopped_at`, `stopped_by_spread_widening`, `r_proxy`, `z_d1`, `primary_dol`, `dol_hit_before_inv`, `state_reached` (S-state cao nhất trong ngày), `premark_time`, `sweep_time`, `mss_time`, `mfe_r`, `mae_r`, `management`, `r_if_no_management`, `news_displacement`.

**Đơn vị dữ liệu quan trọng nhất không phải "lệnh" mà là "ngày"** — Daily State Log ghi mọi ngày, kể cả ngày dừng ở D1 ([[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §22.3). Chỉ log ngày có lệnh = không đo được bối cảnh có giá trị hay không.

#### 52.3 Giả thuyết cần kiểm chứng

Danh sách đầy đủ có trạng thái: [[#63. Danh sách giả thuyết chưa kiểm chứng (hypothesis register)]]. Các so sánh cốt lõi:
- MSS cùng hướng HTF vs MSS ngược HTF.
- MSS sau sweep vs MSS không sweep.
- MSS có displacement ≥ 3/4 vs structural break yếu.
- Setup tại POI vs setup giữa range.
- Entry FVG (E2) vs entry khác (E1, E3, E4).
- Kết quả theo session, theo thị trường, theo regime biến động.

**Thiết kế để kết luận được:** chạy **Baseline** (chỉ trigger M5, không bối cảnh) → **Model A** (+ D1) → **Model B** (+ H1) → **Model C** (đầy đủ). Nếu bối cảnh có giá trị, expectancy phải tăng từ Baseline → C *trên dữ liệu ngoài mẫu*. Kiến trúc chi tiết: [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §22.2.

### 53. Đánh giá kết quả

**Các chỉ số — giải thích bằng ví dụ đơn giản.** Giả sử 40 lệnh: 16 thắng trung bình +2.1R, 24 thua trung bình −1.0R.

| Chỉ số | Cách tính | Ví dụ | Ý nghĩa |
|---|---|---|---|
| **Win rate** | thắng / tổng | 16/40 = 40% | Một mình nó vô nghĩa |
| **Average win / loss** | | +2.1R / −1.0R | Kết hợp với win rate |
| **Expectancy** | WR × avg win − (1 − WR) × avg loss | 0.4 × 2.1 − 0.6 × 1.0 = **+0.24R/lệnh** | Lợi nhuận kỳ vọng mỗi lệnh |
| **Break-even win rate** | 1 / (1 + R) | R = 2 → cần > 33.3% | Win rate tối thiểu để không lỗ |
| **Profit factor** | tổng lãi / tổng lỗ | 33.6 / 24 = 1.4 | > 1 là có lãi |
| **Max drawdown** | sụt giảm lớn nhất từ đỉnh vốn | Chuỗi 6 lệnh thua liền ở risk 0.5% ≈ −3% tài khoản | Quyết định có sống sót qua giới hạn prop firm không |
| **MFE / MAE** | lãi/lỗ tạm thời lớn nhất trong lệnh (theo R) | Nhiều lệnh thắng có MAE ≈ −0.9R → SL đang sát giới hạn; nhiều lệnh thua có MFE ≥ +1.5R → T1 có thể quá xa hoặc thiếu luật quản lý | SL có quá chặt? T1 có quá gần/xa? |
| **Số lượng setup** | mẫu | 40 | Quá nhỏ để kết luận chắc |
| **Out-of-sample** | kết quả trên dữ liệu không dùng để xây luật | Xây luật trên 2015–2019, kiểm trên 2020–2023 | Chống overfit |

**Khoảng tin cậy cho expectancy — vì sao 40 lệnh chưa nói được gì:** với ví dụ trên, độ lệch chuẩn của R ≈ 1.54 → sai số chuẩn ≈ 1.54/√40 ≈ 0.24 → khoảng tin cậy 95% ≈ +0.24 ± 0.48 = **[−0.24R, +0.72R]**. Khoảng này chứa 0: chưa thể kết luận có edge. Muốn khoảng hẹp bằng một nửa cần gấp 4 lần số lệnh.

**Bao nhiêu mẫu là đủ?** Khoảng tin cậy Wilson 95% cho win rate quan sát được:

| Mẫu | Win rate quan sát | Khoảng tin cậy 95% |
|---|---|---|
| 7/10 | 70% | 40% – 89% |
| 15/30 | 50% | 33% – 67% |
| 25/50 | 50% | 37% – 63% |
| 50/100 | 50% | 40% – 60% |
| 100/200 | 50% | 43% – 57% |

Với 30 lệnh, win rate thật có thể là 33% hoặc 67% — đủ khác nhau để đổi hoàn toàn kết luận. Ngưỡng "≥ 30–50 mẫu/biến thể" là **mức tối thiểu để bắt đầu đọc**, không phải để kết luận; so sánh giữa các nhánh (vd NY AM vs London) cần cỡ mẫu ba chữ số mỗi nhánh.

**Audit hiện trạng** (từ [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] §25): 22 lệnh backtest trong vault cho win rate 77% (Wilson 95%: 57–90%) và +1.77R/lệnh — nhiều khả năng phản ánh **quy trình chọn mẫu** hơn là edge: mẫu chọn thủ công theo ngày, chỉ log ngày có lệnh, `bias_correct` chấm sau khi biết kết quả (21/22 = Yes), có lỗi dữ liệu ([[12-Mistake-Log-Data-Mismatch-Backtest]]). Đây là trạng thái mặc định của mọi backtest thủ công chưa có protocol, không phải lỗi cá nhân — và là lý do Part VII tồn tại.

**Chuỗi thua là bình thường về thống kê:**

![[ICT2022-v2-29-Xac-suat-chuoi-thua.svg]]

| Win rate | P(≥ 3 thua liên tiếp trong 20 lệnh) | P(≥ 5 thua liên tiếp trong 50 lệnh) | P(≥ 5 trong 100 lệnh) | Chuỗi thua dài nhất trong 100 lệnh (trung vị · 10% số lần ≥) |
|---|---|---|---|---|
| 55% | 68% | 39% | 65% | 5 · 7 |
| 45% | 87% | 71% | 92% | 6 · 10 |
| 35% | 96% | 92% | 99.5% | 9 · 13 |

*(Tính chính xác bằng quy hoạch động với giả định lệnh độc lập, win rate cố định; cột cuối mô phỏng 20.000 lần.)*

**Đọc đúng:** 3–4 lệnh thua liên tiếp không phải bằng chứng mô hình hỏng. Tín hiệu thật là **các lệnh thua có cùng `first_error_step` lặp lại**. Đặt circuit breaker theo các con số này, không theo cảm xúc. Thực tế các lệnh không độc lập (cùng regime) → chuỗi thua có thể còn dài hơn mô phỏng.

> [!important] Hai kết luận hoàn toàn khác nhau
> **"Setup hợp lý về mặt ICT"** (đủ chuỗi, đúng bối cảnh) và **"setup đã chứng minh được lợi thế thống kê"** (expectancy dương có ý nghĩa, ngoài mẫu, sau chi phí). Note này giúp bạn đạt điều thứ nhất một cách nhất quán; chỉ dữ liệu của bạn mới cho điều thứ hai.

### 54. Case studies

> [!info] Hai nhóm khác nhau về bản chất
> **54.1 — Case 1–4:** backtest tháng 7/2026 (dữ liệu thật, file gốc dẫn link). **54.2 — Case 5–7:** ca tái dựng minh họa, *không phải dữ liệu* — chỉ dùng để minh họa cơ chế. Đánh số giữ nguyên vì [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]] tham chiếu Case 3, 6, 7.

#### 54.1 Từ backtest của bạn (Case 1–4)

##### Case 1 — EURUSD 2013-11-21 Long: Win +3.18R nhưng sai quy trình

![[ICT2022-Advanced-CaseStudy-Win-A.svg|720]]

- **Chuỗi:** Bias D1 Bullish (BOS + CISD trên pullback) → giá ở discount D1 → sweep inducement + vào OB H1 (1.34083–1.33909) → displacement tăng + MSS để lại BPR (FVG bull chồng FVG bear) → entry → chạm TP +3.18R. `chained_fully: Yes`, grade A.
- **Vấn đề:** `first_error_step: entry`. (1) Vào tại **cạnh trên BPR** thay vì CE, quyết định tại chỗ vì sợ lỡ — không theo rule A/B định trước. (2) Theo spec cũ (chưa có quy tắc T1), TP đặt ở một mức internal liquidity tùy chọn, không nhất quán với DOL đã tự ghi (**FVG D1 1.35938–1.36970**) và không có kế hoạch runner. Theo v0.2: T1 = ITH H1 đầu tiên (bắt buộc), DOL là final target *nếu* spec có quản lý nhiều phần — đó là lựa chọn ở §31.
- **Bài học — outcome bias:** lệnh thắng vẫn có thể sai quy trình, và nguy hiểm vì **thắng củng cố một hành vi chưa được backtest** (bắt cạnh vì FOMO). Sửa: chọn `entry_type` trước (§29), target theo §31.
- → File gốc: [[04 - Backtesting/2026-07-11/01 - Win - EURUSD - 2013-11-21- Long]] · Lỗi: [[04-Mistake-FOMO-Entry]]

##### Case 2 — EURUSD 2005-05-02 Long: Loss −1R (vào tại sweep, thiếu displacement)

![[ICT2022-Advanced-CaseStudy-Loss-Chase.svg|720]]

- **Chuỗi gãy:** Bias D1 Bullish đúng, giá về OB H1 (1.28503–1.28249) đúng discount, có sweep — **nhưng** tại thời điểm entry chỉ có một nhịp reject nhỏ (doji), **không displacement, không MSS**. `missing_step: displacement`, grade D, `followed_plan: No`.
- **Bằng chứng định lượng của FOMO:** entry 1.28639 nằm **cao hơn cả đỉnh OB** (1.28503). GATE fail ở 3 mục. Giá quét sâu hơn, dính stop; displacement thật chỉ xảy ra *sau đó*.
- **Bài học:** sweep là event, không phải trigger (R6). Diễn biến sau đó là một **double sweep** (§25): vào ở cú quét đầu, bị cú quét sâu hơn lấy stop, rồi displacement thật mới xảy ra.
- → File gốc: [[04 - Backtesting/2026-07-08/01 - Loss- EURUSD - 2005-05-02 - Long]] · Lỗi: [[02-Mistake-Enter-before-liquidity-sweep]], [[08-Mistake-Weak-Displacement]]

##### Case 3 — XAUUSD 2014-05-14 Short: −1R, quy trình tốt nhưng SL sai chỗ

![[ICT2022-Advanced-CaseStudy-GoodLoss-SL.svg|720]]

- **Chuỗi:** Bias Bearish đúng, top-down tốt, POI Rejection Block H1 đúng premium, entry rất đẹp tại CE/OTE 0.618 (1301.482). Log gốc: `followed_plan: Yes`, grade B− (theo thang cũ), kết quả −1R.
- **Nguyên nhân duy nhất — SL logic:** SL 1302.715 = mép RB (một swing nhỏ M1), không phải invalidation thật của RB (đóng trên 1304.109). Một nhịp hồi bình thường quét stop trước khi luận điểm kịp chạy. R:R 3.22 "đẹp" chỉ là sản phẩm phụ của SL chật.
- **Bài học:** R là hệ quả của SL đúng chỗ (R10). Chấm lại theo spec v0.2: SL nằm trong H1 POI là **vi phạm R10** → đây *không* còn là "good loss"; `first_error_step` gần nhất trong từ vựng template là `entry` (đề xuất thêm giá trị `stop`). Grade trần B.
- → File gốc: [[04 - Backtesting/2026-07-14/02 - Loss- XAUUSD- 2014-05-14- Short]]

##### Case 4 — EURUSD 2021-05-07 Short: đáng ra No Trade (sai bối cảnh)

![[ICT2022-Advanced-CaseStudy-NoTrade-Context.svg|720]]

- **Chuỗi:** POI là OB đúng premium — *không sai loại*. Nhưng `first_error_step: draw`, `missing_step: sweep`, grade C.
- **Lỗi 1 — draw:** draw ngắn hạn đang hướng **lên** (BSL phía trên chưa bị lấy) → giá lên lấy BSL trước, quét stop. Đây là lệch pha P/D và "unswept liquidity" ([[13-Mistake-Trading-Into-Unswept-Liquidity]]).
- **Lỗi 2 — session:** entry 10:05 giờ VN (phiên Á), ngoài killzone.
- **Bài học:** pattern "đủ điều kiện bề mặt" trong sai bối cảnh không phải setup. Hai cổng (đồng pha draw ngắn hạn + killzone) phải được kiểm *trước* khi nhìn M5.
- → File gốc: [[04 - Backtesting/2026-07-10/02 - Loss- EURUSD - 2021-05-07- Short]]

#### 54.2 Ca minh họa — không phải dữ liệu (Case 5–7)

##### Case 5 — GBPUSD: bỏ lỡ setup vì lệch giờ DST (minh họa)

![[ICT2022-Advanced-CaseStudy-DST-Miss.svg|720]]

Trader dùng bảng quy đổi NY → VN cố định từ đầu năm; tuần đầu tháng 11 Mỹ vừa lùi giờ, NY AM killzone thật dời muộn 1 giờ theo giờ VN. Trader ngừng canh đúng lúc chuỗi sweep → MSS → FVG hình thành. **Lỗi vận hành thuần túy**, không phải lỗi phân tích. **Rule:** định nghĩa killzone bằng giờ NY trên chart; kiểm các ngày đổi giờ của Mỹ và Anh liệt kê ở §39.1.

##### Case 6 — USDJPY Short: thua do spread giãn tại rollover 17:00 NY (minh họa)

![[ICT2022-Advanced-Spread-Widening-SessionOpen.svg|720]]

Chuỗi và SL đều đúng quy tắc; giá hồi về CE đúng lúc rollover, spread giãn trong vài giây, giá bid/ask chạm SL dù giá mid không tới; 15 phút sau giá đi đúng hướng. **"Good process, bad luck do cấu trúc thị trường"** — chi phí vận hành khu trú vào khung giờ có thể phòng tránh. **Rule:** entry dự kiến trong ±5 phút quanh rollover/mở phiên → nới buffer (vd +30–50%) hoặc trì hoãn; log `stopped_by_spread_widening` để tách khỏi "lỗi phân tích".

##### Case 7 — XAUUSD Long: double sweep — kỷ luật không vào ở cú quét đầu (minh họa)

Giá quét SSL nông rồi reclaim — trông như sweep hợp lệ. Trader **không vào** (R6), chờ MSS. Giá quét tiếp một SSL sâu hơn rồi mới displacement + MSS trên **M5** → FVG → entry tại CE, SL dưới cú quét sâu → chạm target (kết quả mang tính minh họa). **Đối lập trực tiếp với Case 2:** cùng tình huống "có sweep", kỷ luật chờ xác nhận quyết định giữa bị nhồi vào pool trung gian và bắt đúng pool cuối.

> [!summary] Bốn ca dữ liệu — một thông điệp
> **Kết quả từng lệnh là nhiễu; quy trình (chuỗi + vị trí + SL logic + bối cảnh) là tín hiệu.** Case 1 thắng mà vẫn phải sửa; Case 2 vào trước xác nhận; Case 3 đọc đúng nhưng SL sai chỗ; Case 4 lẽ ra không tồn tại. Ba ca minh họa (5–7) chỉ bổ sung cơ chế vận hành (DST, spread, double sweep), không phải bằng chứng.

### 55. Giới hạn của nghiên cứu

**Giới hạn nhận thức:**
- Không có dữ liệu order flow công khai xác nhận một "thuật toán" vận hành theo logic ICT. IPDA, smart money là **mô hình tư duy**, không phải cơ chế đã chứng minh (§5).
- Bằng chứng học thuật chỉ chạm tới các mảnh cơ học (stop clustering, S/R trùng độ sâu sổ lệnh) — chưa có kiểm định trực tiếp mô hình (§5).

**Rủi ro thống kê khi backtest:**
- **Hindsight bias** — trên bất kỳ đoạn chart lịch sử nào cũng "tìm ra" được một câu chuyện ICT khớp kết quả.
- **Quá nhiều bậc tự do** — chọn swing nào, FVG nào, sweep nào, cộng thêm killzone/macro/SMT/CISD… → số tổ hợp "vừa khớp" gần như vô hạn = cơ chế của overfitting.
- **Mẫu nhỏ** — chuỗi 5–10 lệnh thắng của một biến thể hoàn toàn có thể là may rủi (§53).
- **Survivorship của case được chia sẻ** — cộng đồng đăng case đẹp, không đăng 50 lần "trông giống nhưng gãy".
- **Adverse selection của limit order** (§29) và **chi phí thực** (spread, slippage) làm kết quả live thấp hơn backtest.

**Điều kiện thị trường làm mô hình yếu đi** `[INTERPRETATION]`:

| Regime | Vì sao yếu đi | Dấu hiệu |
|---|---|---|
| Thanh khoản cực mỏng (nghỉ lễ Mỹ, cuối tháng 12) | Sweep/displacement không phản ánh dòng lệnh thật | Range ngày hẹp bất thường |
| Sự kiện vĩ mô đổi regime | Tương quan (SMT) đứt gãy; DOL cũ mất nghĩa | Phân kỳ kéo dài giữa cặp vốn tương quan chặt |
| Trend một chiều do tin | Không có retrace về FVG | Nhiều giờ không hồi tới CE |
| Range siết kéo dài | Quét hai phía liên tục không displacement | ATR co lại rõ |
| Spread rộng bất thường | FVG LTF bị spread nuốt, R ròng âm | Spread gấp 2–3 lần thường lệ |

**Ngưỡng "chuẩn" không phải hằng số:** OTE 62–79%, CLV ≥ 0.7, "40 pip CBDR" và các ngưỡng tương tự đến từ quan sát định tính trên một giai đoạn biến động cụ thể; chưa tìm thấy nguồn công bố kèm kiểm định ngoài mẫu. Biến động trung bình thay đổi theo thời gian — chuẩn hóa theo ATR của chính dữ liệu gần đây (rolling 20–60 ngày) tốt hơn dùng con số cố định.

**Cách tự kiểm định khách quan:** pre-registration (viết ngưỡng trước khi nhìn dữ liệu) · walk-forward (tối ưu trên đoạn đầu, kiểm trên đoạn sau) · forward test size nhỏ trước khi scale · đếm cả setup bị bỏ lỡ · so sánh "đủ chuỗi" vs "thiếu đúng một bước" trên cùng dữ liệu để đo giá trị của từng mắt xích.

### 56. Câu hỏi nghiên cứu còn mở

1. Bối cảnh D1 có thực sự làm lệch phân phối kết quả của chuỗi M5 so với Baseline không — và lệch ở win rate hay ở R?
2. Sweep trước MSS có giá trị thông tin không, hay chỉ là một bộ lọc làm giảm số mẫu?
3. Quy tắc "giữ 3–5 nến" của MSS cải thiện hay làm xấu kết quả so với "xác nhận tại close + hủy khi đóng ngược"?
4. TTL tự nhiên của một setup M5 là bao nhiêu nến (hazard analysis)?
5. Entry E1 / E2 / E3: biến thể nào có expectancy **mỗi ngày** cao nhất sau khi tính lệnh missed?
6. POI rank có tương quan với kết quả không, hay chỉ là thứ tự thẩm mỹ?
7. Đồng pha P/D D1↔H1 có thông tin độc lập với vị trí D1 không?
8. Killzone có cải thiện expectancy hay chỉ giảm số lệnh?
9. Kết quả có ổn định qua thị trường (FX vs index vs vàng) và qua regime biến động không?
10. Quản lý `partial50_1R_BE` vs `none_full_T1`: cái nào tốt hơn sau chi phí, và tốt hơn vì entry hay vì quản lý?

---

## PART VIII — TỔNG HỢP

### 57. Toàn bộ mô hình — giải thích cho trẻ 5 tuổi

Có một cái hồ cá lớn (D1). Bạn nhìn cả hồ trước và tự hỏi: *cá đang bơi về phía nào, và chỗ nào trong hồ cá hay tụ lại?* Nếu không biết, bạn không câu — về nhà cũng được.

Nếu biết, bạn chọn **một góc hồ** để ngồi (H1) — góc mà cá thường đi qua khi bơi về chỗ tụ. Bạn không thả câu khi cá còn ở tít đầu kia hồ; bạn chờ cá tới gần góc của mình, và chỉ câu vào **giờ cá ăn** (killzone).

Khi cá tới gần, bạn nhìn thật kỹ mặt nước ngay trước phao (M5). Bạn chờ ba dấu hiệu theo đúng thứ tự: cá **đớp thử** một miếng mồi nhỏ ở chỗ đông cá (sweep), rồi **quay đầu bơi mạnh** về phía bạn đoán (MSS + displacement), để lại một **vệt sóng** (FVG). Bạn chỉ giật cần khi cá quay lại đúng vệt sóng đó (entry).

Trước khi câu, bạn đã quyết định: nếu dây chùng quá mức này thì thả cá, không cố kéo (stop loss); và bạn biết mình muốn kéo cá về tới bờ nào (target). Có hôm ngồi cả buổi không giật cần lần nào — **đó vẫn là một buổi câu đúng cách.**

*Giới hạn của phép so sánh:* cá thật có ý định; giá không có "ý định" mà ta đọc được. "Chỗ cá tụ" chỉ là nơi ta *đoán* có nhiều lệnh chờ — chưa chắc đúng.

### 58. Ví dụ bullish từ D1 đến M5 (dựng, FX, cùng số liệu hình 14 và 23)

Quy ước: giờ của nến = giờ mở nến (nến M5 "08:00" đóng lúc 08:05). ATR(M5) = 3.0; spread = 0.1. B1–B8 là các bước thời gian (§50).

```text
B1 (05:30 VN, trước phiên) — D1 Context Note
  Structure: Bullish; protected low (ITH) 92.0; HH 140.0.
  Range 92.0 → 140.0, EQ 116.0; giá 114.5 → z = 0.47 (discount, sát EQ).
  Pool: BSL 140.0 (range high, chưa chạm) · PWH 146 · SSL 101.5 (PDL) · SSL 92.
  DOL: primary 140.0 (L4, horizon 1–5 phiên) · secondary 146 (PWH) · pool đối diện/điểm yếu: 101.5.
  HTF POI: D1 FVG 104.0–112.0. Invalidation: D1 close < 92.0.
  Gate G1: Required đủ; Supporting 3/6 (W1 cùng hướng · displacement D1 gần nhất cùng hướng ·
           primary DOL chưa từng bị chạm) → Medium → risk tối đa 0.4%.
  WHAT I WANT ON H1: nhịp hồi đi vào 104–112, tạo SSL nội bộ; không tìm short.

B2 (phiên London) — H1 (xem H1 Handoff, §24 Ví dụ 1)
  Một leg giảm từ ITH H1 126.0 vào D1 FVG; các đỉnh trong leg chỉ là STH; inducement EQL 120 bị quét trên đường xuống.
  H1 POI refine: H1 FVG 105.5–110.0. SSL H1 106.7 (trong POI). T1 = ITH H1 126.0.
  Status: MONITORING (KZ NY AM FX mở lúc 07:00 NY, còn < 30 phút).

B3 (07:25 NY) — chuẩn bị M5
  Pre-mark: pool 106.7 · mss_reference = ITH M5 113.0 (gốc leg giảm). Ảnh chụp lưu giờ.
  R_proxy = (126.0 − 113.0) / (113.0 − 106.4) = 1.97 ≥ 1.5 · không tin đỏ · KZ đã mở → EXECUTION ELIGIBLE.

B4 (nến 07:45) — Sweep
  Low 105.6 < 106.7; thân đóng 107.1 > 106.7 cùng nến → sweep. Cực trị 105.6.

B5 (nến 07:55–08:00) — MSS
  Hai nến thân ~90%, CLV > 0.9; nến 08:00 đóng 113.4 > 113.0 → MSS (nến thứ 4 tính từ nến trigger).
  Đỉnh leg displacement 114.8 (nến 08:05).

B6 (08:10, close nến 08:05) — Execution Plan
  Displacement 4/4 (③ xác nhận ở nến 08:05). FVG F1 = 111.2–113.1 (chứa 113.0), CE 112.15 — xác nhận ở nến 08:05.
  E2 limit 112.15 · SL 105.6 − max(0.2, 0.3) = 105.3 · T1 126.0 → R = 13.85 / 6.85 = 2.02 ≥ 2.
  Confluence: inducement đã quét (+1) · SMT — cặp tương quan không tạo đáy mới tại cú quét (+1) → 2/8 → hạng B.
  Risk = min(0.4% theo confidence, 0.25% theo hạng B) = 0.25%.
  TTL: 12 nến sau nến MSS (hết nến 09:00) / hết KZ 10:00 / giá chạm 119.0 (+1R) chưa khớp / MSS failure.

B7 (nến 08:20) — giá hồi đáy 110.9 → limit 112.15 khớp.
B8 — giá đi lên chạm 126.0 → +2.02R (trước chi phí). Log: chained_fully Yes, first_error_step none.
```

*Ghi chú:* M5 FVG nằm hơi trên H1 POI (105.5–110.0) — hợp lệ, vì điều kiện vị trí là *arrival và sweep xảy ra trong POI*; FVG là nơi displacement để lại, thường nằm phía trên vùng sweep. Nếu kết quả là −1R thay vì +2R, lệnh vẫn được chấm y hệt về quy trình.

### 59. Ví dụ bearish từ D1 đến M5 (dựng, FX, cùng số liệu hình 15)

```text
B1 (trước phiên) — D1 Context Note
  Structure: Bearish; protected high (ITH) 138.0. Range 138.0 → 92.0, EQ 115.0; giá 121.0 → z = 0.63 (premium).
  Pool: SSL 104.0 (ITL H1 — IRL của range D1) · SSL 92.0 (range low) · SSL 88 (PWL) · BSL 126.0 (chưa chạm).
  DOL: primary 92.0 (L4) · secondary 88 (PWL) · pool đối diện/điểm yếu: BSL 126.0.
  HTF POI: D1 FVG bearish 118.0–125.0. Invalidation: D1 close > 138.0.
  Gate G1: Required đủ; Supporting 4/6 → Medium → risk tối đa 0.4%.

B2 (London) — H1
  Nhịp hồi HH–HL vào D1 FVG; H1 POI refine: H1 FVG 120.0–124.5; BSL H1 123.3 trong POI.
  T1 = ITL H1 đầu tiên phía dưới = 104.0 (các đáy giữa chỉ là STH). Status: MONITORING.

B3 (07:25 NY) — Pre-mark: pool 123.3 · mss_reference = ITL M5 117.0 (gốc leg tăng).
  R_proxy = (117.0 − 104.0) / ((123.3 + 0.3) − 117.0) = 1.97 ≥ 1.5 · KZ đã mở → EXECUTION ELIGIBLE.
B4 (nến 07:45) — Sweep: high 124.4 > 123.3; thân đóng 122.9 < 123.3 → sweep; cực trị 124.4.
B5 (nến 08:00) — MSS: displacement giảm, thân đóng 116.6 < 117.0.
B6 (08:10) — Displacement 4/4; FVG F1 116.9–118.8, CE 117.85.
  E2 sell limit 117.85 · SL 124.4 + 0.3 = 124.7 · T1 104.0 → R = 13.85 / 6.85 = 2.02.
  Confluence: BSL nội bộ (inducement) bị quét trước POI (+1) · SMT (+1) → 2/8 → B → risk 0.25%.
  TTL: hết nến 09:00 / hết KZ / chạm 111.0 (+1R) chưa khớp / thân nến đóng lại trên 117.0 trước khớp.
B7 (nến 08:20) — giá hồi chạm 117.85 → khớp.  B8 — giá giảm tới 104.0 → +2.02R.
```

### 60. Ví dụ setup bị invalidated (dựng, số liệu hình 20) — và một lệnh thua hợp lệ (hình 19)

**Invalidated trước entry:** bối cảnh và trigger như §58 tới B6 (MSS nến 08:00, FVG 111.2–113.1, limit 112.15). Sau MSS, giá **đi ngang trên FVG**, đáy thấp nhất 113.2 — không chạm CE 112.15. Khi nến 09:00 đóng (12 nến sau nến MSS) TTL hết → **hủy lệnh, log `expired`**. Một giờ sau giá sập xuyên FVG và xuống dưới cực trị sweep 105.6 — nếu lệnh còn treo, nó đã khớp muộn rồi dính SL. Hủy setup không phải thua lệnh: không mất tiền, không phải lỗi; là quy trình hoạt động đúng.

**Lệnh thua tuân thủ:** cùng bối cảnh, lệnh khớp tại 112.15, sau đó giá không đi tiếp mà giảm dần và chạm SL 105.3 → −1R. Mọi `step_ok = Yes`, `first_error_step: none`, `followed_plan: Yes`. Việc cần làm: ghi đúng, không dời SL, không đổi định nghĩa, không revenge trade.

### 61. Ví dụ No Trade (dựng, số liệu hình 21 — một ví dụ độc lập với §58)

D1 bullish; H1 POI 110–115 (nằm trong D1 POI của ví dụ này); giá H1 đang ở 128, gần EQ của range H1, cách POI xa. Lúc 12:40 NY (ngoài killzone) M5 xuất hiện một chuỗi sweep → MSS → displacement → FVG "sách giáo khoa". **Quyết định: No Trade** — G2 vị trí fail (không ở POI) và G2 thời gian fail (ngoài KZ). M5 không có quyền tự tạo setup. Log: `stopped_at: G2`, `reason: location+time`. Nếu giá tăng sau đó, đó là kết quả ngoài mô hình — không phải cơ hội bị bỏ lỡ của mô hình.

### 61.1 Toàn bộ quy trình trên một trang

![[ICT2022-v2-30-Tom-tat-1-trang.svg]]

1. **Trước phiên — D1:** structure (ITH/LTH) → range + EQ + z → pool hai phía → primary/secondary DOL + pool đối diện → bias (4 trạng thái) → HTF POI → invalidation. Viết Context Note. **Gate G1:** tất cả Required, không Disqualifying; không qua → Neutral / chờ / No Trade.
2. **Trong ngày — H1:** H1 đang hồi về D1 POI hay phá nó? → H1 POI refine → pool sẽ bị quét → T1 = ITH/ITL H1 đầu tiên → setup hợp lệ (§21) → **NOT READY → MONITORING** (pre-mark pool + mss_reference trên M5) → **Gate G2** (neo HTF + vị trí đồng pha + killzone + pre-mark + R_proxy ≥ 1.5 + không tin + risk mở) → **EXECUTION ELIGIBLE**.
3. **Killzone — M5:** sweep pool đã đánh dấu (reclaim ≤ 3 nến) → MSS: thân nến vượt mss_reference (≤ 12 nến từ trigger) → displacement ≥ 3/4 → FVG F1 → Execution Plan tại close nến sau MSS: entry theo entry_type, SL = cực trị sweep ± buffer, R(T1) ≥ 2, confluence ≥ 2, risk = min(confidence, hạng) ≤ 0.5%.
4. **Lệnh chờ:** hủy nếu TTL 12 nến / hết killzone / +1R chưa khớp / MSS failure. Không đuổi.
5. **Sau phiên:** log mọi ngày (kể cả dừng ở D1), setup bị loại, missed/expired; chấm lệnh bằng step1–7, first_error_step, missing_step. Đổi định nghĩa = version mới.

### 62. Danh sách quy tắc đã định nghĩa (rule register)

**Phiên bản: ICT2022-Core (D1-H1-M5) v0.2 — 2026-10-11.** Mọi quy tắc là quy tắc vận hành do người nghiên cứu chọn; trạng thái kiểm chứng ghi ở cột cuối.

| ID | Quy tắc | Mục | Trạng thái |
|---|---|---|---|
| D-01 | Structure D1 kết luận bằng ITH/LTH; STH không đổi bias | §6–7 | Định nghĩa |
| D-02 | Context Note viết trước khi mở H1/M5, có giờ | §14, R2 | Định nghĩa |
| D-03 | Gate G1: tất cả Required, không Disqualifying (thay "2-of-3") | §15 | **Đổi từ v0.1** — BACKTEST REQUIRED |
| D-04 | Neutral/Conflicting là output hợp lệ → không trade | §12, R1 | Định nghĩa |
| D-05 | DOL = primary + secondary + horizon + điểm yếu | §11 | Định nghĩa |
| H-01 | H1 kế thừa hướng; H1 ngược D1 trước POI = bình thường | §16 | Định nghĩa |
| H-02 | Ba trạng thái NOT READY / MONITORING / EXECUTION ELIGIBLE | §23 | Định nghĩa |
| H-03 | Gate G2 / ELIGIBLE = 3 điều kiện lõi (neo HTF, vị trí + đồng pha P/D, killzone) + 4 kiểm tra vận hành (pre-mark, R_proxy ≥ 1.5, không tin, risk mở) | §23 | Giữ quy tắc 3/3 của v0.1 + bổ sung; ngưỡng R_proxy là HEURISTIC |
| H-05 | MONITORING khi killzone đang mở hoặc mở trong ≤ 30 phút | §20, §23 | HEURISTIC |
| H-04 | Acceptance = ≥ 2 thân nến liên tiếp đóng ngoài mức (dùng chung cho sweep, POI, structure); H1 POI distal → setup fail, D1 POI distal → REASSESS | §22, §49 | HEURISTIC |
| M-01 | Sweep: pool đánh dấu trước; reclaim ≤ 3 nến | §25 | HEURISTIC |
| M-02 | Sweep là event, không phải trigger | §25, R6 | Định nghĩa |
| M-03 | MSS: thân nến vượt ITH đánh dấu trước (cố định), ≤ 12 nến tính từ nến trigger sweep | §26 | HEURISTIC |
| M-04 | MSS xác nhận tại close; đóng ngược trước khớp → hủy (thay "giữ 3–5 nến") | §26 | **Đề xuất đổi** — BACKTEST REQUIRED |
| M-05 | Displacement ≥ 3/4 tiêu chí | §27 | HEURISTIC |
| M-06 | FVG chọn theo F1 | §28 | HEURISTIC (HYP-08) |
| M-07 | Entry type chọn một cho cả version (mặc định E2 CE) | §29, R9 | **Đổi từ v0.1** — BACKTEST REQUIRED (HYP-09) |
| M-08 | Không đuổi; +1R chưa khớp → hủy | §29 | Định nghĩa |
| M-09 | SL = cực trị sweep − max(2 × spread, 0.1 × ATR) | §30 | HEURISTIC |
| M-10 | T1 = ITH/ITL H1 đầu tiên theo hướng lệnh chưa bị lấy; R ≥ 2 | §31 | Định nghĩa |
| M-11 | Order TTL: 12 nến / hết KZ / +1R | §29, §49 | HEURISTIC |
| R-01 | Risk ≤ 0.5%/lệnh; size theo confidence/hạng trong trần | §15, §39.2 | Luật cứng vault |
| R-02 | GATE thắng SCORE; confluence 0–1 = No Trade (theo checklist hiện có) | §39.2 | Định nghĩa (trọng số +1 bằng nhau: BACKTEST REQUIRED) |
| L-01 | Log mọi ngày; log setup bị loại, missed, expired | §47, §52 | Định nghĩa |
| L-02 | Đổi định nghĩa = version mới | §26, §52 | Định nghĩa |

**Changelog quy tắc (chuẩn OLD / NEW / REASON):**

| | D-03 (step-down D1 → H1) | M-04 (xác nhận MSS) | M-07 (entry) |
|---|---|---|---|
| **OLD** | 2 trong 3 điều kiện | MSS phá ITH + giữ 3–5 nến | "Quanh CE" hoặc "Edge" tùy lệnh |
| **NEW** | Tất cả Required + không Disqualifying | Xác nhận tại close; đóng ngược trước khớp → hủy | Một `entry_type` cho cả version |
| **REASON** | "2-of-3" cho phép thiếu điều kiện quan trọng nhất | Chờ 3–5 nến trùng thời điểm retrace → bỏ lỡ hoặc đuổi | Trộn kiểu entry làm thống kê vô nghĩa (Case 1) |
| **EXPECTED EFFECT** | Ít ngày PASS hơn, chất lượng cao hơn (nếu điều kiện có thông tin) | Ít missed hơn; một số MSS fail sẽ được hủy thay vì vào | Thống kê so sánh được |
| **BACKTEST?** | Có — A/B trên cùng dữ liệu | Có — A/B | Có — E1 vs E2 vs E3 |

### 63. Danh sách giả thuyết chưa kiểm chứng (hypothesis register)

| ID | Giả thuyết | Biến cần log | Dự đoán | Có thể bị bác bỏ khi | Trạng thái |
|---|---|---|---|---|---|
| HYP-01 | Long ở z ≤ 0.5 (D1) có expectancy cao hơn long ở z > 0.5 | `z_d1`, r_multiple | Cao hơn | Không khác biệt với ≥ 100 mẫu/nhánh | UNTESTED |
| HYP-02 | Primary DOL ex-ante bị chạm trước invalidation nhiều hơn null theo khoảng cách | `primary_dol`, `dol_hit_before_inv` | > null | ≈ null | UNTESTED |
| HYP-03 | MSS sau sweep có expectancy cao hơn MSS không sweep | `liquidity_swept`, r | Cao hơn | Không khác hoặc thấp hơn | UNTESTED |
| HYP-04 | Displacement 4/4 cho kết quả tốt hơn 3/4 | `displacement_score` | Tốt hơn | Không khác | UNTESTED |
| HYP-05 | Entry sau MSS có expectancy cao hơn entry ngay tại sweep | entry timing, MAE | Cao hơn, MAE thấp hơn | Ngược lại | UNTESTED |
| HYP-06 | Đồng pha P/D D1↔H1 cải thiện expectancy độc lập với vị trí D1 | `pd_aligned_d1_h1` | Cải thiện | Không cải thiện khi kiểm soát z_d1 | UNTESTED |
| HYP-07 | Killzone cải thiện expectancy, không chỉ giảm số lệnh | session, r | Cải thiện | Expectancy ngoài KZ ≈ trong KZ | UNTESTED |
| HYP-08 | FVG F1 có expectancy/ngày cao hơn F2 | `fvg_rule` | Cao hơn | Ngược lại | UNTESTED |
| HYP-09 | E2 CE có expectancy/ngày cao hơn E1 sau khi tính missed | `entry_type`, `limit_filled`, `would_have_result` | Cao hơn | Ngược lại | UNTESTED |
| HYP-10 | POI rank ≥ 3 cho kết quả tốt hơn rank 1–2 | `poi_rank` | Tốt hơn | Không tương quan | UNTESTED |
| HYP-11 | Bối cảnh D1 + H1 làm lệch phân phối kết quả của trigger M5 so với Baseline | Model Baseline/A/B/C | C > Baseline ngoài mẫu | C ≈ Baseline | UNTESTED |
| HYP-12 | Giá trị của M5 nằm ở R (stop sát) hơn là ở win rate | avg R, stop distance, WR (B vs C) | R tăng, WR có thể giảm | Không tăng R | UNTESTED |
| HYP-13 | Adverse selection: trong cùng tập setup, lệnh limit đã khớp có expectancy thấp hơn tập không khớp (theo `would_have_result`) | `limit_filled`, `would_have_result` | Thấp hơn | Không khác | UNTESTED |
| HYP-14 | Sau sweep (theo §25), xác suất giá đi ngược hướng sweep ≥ 1 ATR trước khi đi tiếp cao hơn base rate random walk | sweep events, kết quả 1 ATR | > base rate | ≈ base rate | UNTESTED |
| HYP-15 | Giá phản ứng tại FVG (hồi về rồi đi tiếp ≥ 1R) nhiều hơn tại một vùng ngẫu nhiên cùng kích thước | FVG vs vùng đối chứng | Nhiều hơn | Không khác | UNTESTED |
| HYP-16 | MSS "xác nhận tại close + hủy khi đóng ngược" (M-04 mới) cho expectancy/ngày cao hơn "giữ 3–5 nến" | spec A/B | Cao hơn | Ngược lại | UNTESTED |
| HYP-17 | Gate G1 "tất cả Required" (D-03 mới) cho expectancy trên ngày PASS cao hơn "2-of-3" | spec A/B, số ngày PASS | Cao hơn, ít ngày hơn | Không khác | UNTESTED |
| HYP-18 | Quản lý `partial50_1R_BE` vs `none_full_T1`: khác biệt expectancy sau chi phí | `management`, `r_if_no_management` | Chưa có dự đoán | — | UNTESTED |
| HYP-19 | Setup được bias cho phép có expectancy cao hơn setup cùng loại bị bias chặn | log setup bị chặn | Cao hơn | Không khác | UNTESTED |
| HYP-20 | Tồn tại TTL tự nhiên (hazard giảm rõ sau k nến) cho lệnh chờ FVG | thời gian tới khớp, kết quả | Có điểm gãy | Đường hazard phẳng | UNTESTED |
| HYP-21 | SL S1 (dưới cực trị sweep) cho expectancy cao hơn S2 (dưới nến 1 FVG) | `stop_variant`, MAE | Cao hơn | Ngược lại | UNTESTED |
| HYP-22 | MSS cùng hướng HTF có expectancy cao hơn MSS ngược hướng HTF | hướng MSS vs bias | Cao hơn | Không khác | UNTESTED |

Trạng thái hợp lệ: UNTESTED · TESTING · SUPPORTED · WEAK EVIDENCE · REJECTED · REQUIRES MORE DATA. "Được ủng hộ bởi vài ví dụ" **không phải** SUPPORTED.

---

## Active recall

> [!question]- Q1. Ba tầng D1 / H1 / M5 mỗi tầng trả lời câu hỏi gì?
> D1: hướng nào được phép, giá bị hút về đâu, sai ở đâu (context). H1: cơ hội có hình thành tại vùng quan tâm không, khi nào được nhìn M5 (location + timing gate). M5: tại vùng đó, giờ đó, đã đủ bằng chứng đo được để đặt lệnh chưa (execution).

> [!question]- Q2. Vì sao sweep không phải tín hiệu vào lệnh?
> Tại thời điểm sweep, chưa phân biệt được sweep với run (cùng một sự kiện ban đầu, hai kết cục). Chỉ MSS có displacement sau đó mới cho bằng chứng mất cân bằng đã lật. Vào tại sweep = Case 2.

> [!question]- Q3. MSS trong note này được định nghĩa thế nào? Vì sao phải đánh dấu swing trước?
> Thân nến M5 đóng vượt mss_reference (ITH gốc của leg đi vào sweep), sau reclaim, ≤ 12 nến. Đánh dấu trước biến MSS từ một nhãn luôn tìm được (vì lúc nào cũng có swing vừa bị phá) thành một dự báo có thể sai.

> [!question]- Q4. "Mở M5" khác "được vào lệnh" thế nào?
> MONITORING: mở M5 để đánh dấu pool, ITH, tính R — chưa được đặt lệnh. EXECUTION ELIGIBLE: đủ 3 điều kiện lõi + 4 kiểm tra vận hành — được chờ trigger theo rule.

> [!question]- Q5. D1 bullish, H1 đang LH–LL, giá chưa tới POI. Làm gì?
> NOT READY. Không short theo H1 (countertrend, ngoài spec), không long sớm. Đặt alert ở POI.

> [!question]- Q6. Sáu khái niệm invalidation khác nhau là gì?
> Invalidation bias D1 · invalidation H1 setup · invalidation M5 entry · SL bị chạm · giả thuyết không còn hợp lệ · lệnh thua tuân thủ quy trình (không có gì để sửa).

> [!question]- Q7. Vì sao không đuổi giá khi limit không khớp?
> Đuổi = đổi sang entry model khác chưa backtest, SL xa hơn, R thấp hơn. Lệnh missed không làm giảm expectancy *mỗi lệnh* của tập theo rule (chỉ giảm số lệnh/ngày); entry ngoài rule làm bẩn dữ liệu. Log missed + would_have_result.

> [!question]- Q8. Với win rate 45%, xác suất gặp ít nhất một chuỗi 3 lệnh thua liên tiếp trong 20 lệnh là bao nhiêu? Ý nghĩa?
> ≈ 87%. Chuỗi thua ngắn là bình thường; tín hiệu thật là các lệnh thua có cùng first_error_step lặp lại.

> [!question]- Q9. Killzone, OTE, P/D là core hay bộ lọc?
> Trong v0.2: killzone và P/D là bộ lọc bắt buộc *do bạn chọn*; OTE là confluence/entry type. Không phải điều kiện của mọi ICT 2022 Model.

> [!question]- Q10. Case 1 thắng +3.18R. Vì sao vẫn phải sửa?
> first_error_step: entry — vào ở cạnh BPR vì FOMO thay vì rule định trước, và TP ở internal liquidity thay vì DOL đã ghi. Thắng củng cố một hành vi chưa được kiểm chứng.

> [!quote] Câu nhắc khi mở chart
> **"Bối cảnh trước — vị trí sau — bằng chứng cuối cùng. Thiếu một tầng, tôi không có lệnh. Có lệnh hay không, tôi ghi lại."**

---

## Phụ lục A — Những gì đã thay đổi trong bản rework (2026-10-11)

> [!info]- Bản đồ khử trùng lặp (bản cũ 1234 dòng → cấu trúc Part I–VIII)
> | Nội dung bản cũ | Xuất hiện ở | Xử lý |
> |---|---|---|
> | Chuỗi 7 bước | §1, §2 (bảng), §3, §5, §6 sequences, §11, Flashcards, Lesson Learned | Gộp thành §3 (bảng kiến trúc) + §36–37; các nơi khác dẫn link |
> | Checklist "điều kiện bắt buộc / hợp lệ / không trade" | §2, §3, §5, §8.4 GATE, §9, §10 | Gộp thành **một** danh sách No Trade (§33) + checklist Part VI |
> | "Đừng chase displacement" | ≥ 6 chỗ | Một quy tắc R9 + Scenario F |
> | IPDA "vì sao hoạt động" và "Phản biện epistemic" | §1 và mục Phản biện | Gộp vào §5 (có/không thể khẳng định) + §55 |
> | Thang POI rank | §8.1 và Chuyên sâu 4 #4 | Một bảng §18 (giữ nhãn "thang 8.1" cho template) |
> | Khung displacement 4 tiêu chí | §3 và edge case ④ | Một bảng §27 |
> | Sample size ≥ 30–50, tăng size, tần suất setup | Chuyên sâu 4 #7, #12, #13 và Best Practices | Gộp vào §53 + R12; bỏ các con số tần suất chưa đo |
> | Nghi thức `missing_step` hằng tuần | Best Practices và §13.3 | Một chỗ: §47 |
> | Schema YAML đầy đủ (§13.1) | Trùng 1:1 với template | Thay bằng bảng ánh xạ §52.2 + link template |
> | Edge cases ①–⑭ | Chuyên sâu 3 | Gộp với 20 failure modes (§40); giữ ca vận hành riêng |
> | Case 1–7 | Chuyên sâu 5 | Giữ nguyên số liệu & đánh số (01c tham chiếu); tách Case 5–7 thành "ca minh họa — không phải dữ liệu", bỏ kết quả R bịa của Case 7; chấm lại Case 3 theo R10 |
>
> **Sửa lỗi:** bảng xác suất chuỗi thua (giá trị minh họa sai → tính chính xác); wikilink hỏng tới concept (`[[Fair Value Gap]]`, `[[Order Block]]`, `[[Optimal Trade Entry]]`, `[[Displacement]]` → tên file hyphen thật); `common_mistakes` trỏ tới file mistake thật.
>
> **Bỏ có chủ đích:** các con số "1–3 setup A+/ngày NQ", "3–6 setup/tuần FX", "3–6+ sweep/ngày" — không có nguồn đo; để Daily State Log trả lời.
>
> **Thêm mới:** kiến trúc 3 tầng có output, Gate G1 v0.2, Gate G2 + R_proxy, ba trạng thái H1 → M5, định nghĩa vận hành thống nhất (§49), 6 khái niệm invalidation, Scenario A–F, hypothesis register, rule register có version, 31 hình SVG mới.

## Phụ lục B — Nguồn tham khảo

**Nguồn về mô hình (thứ cấp — không có đặc tả chính thức từ ICT):**
- LuxAlgo Library — *Model 2022* (tóm tắt chuỗi raid → shift → entry, khung thời gian, killzone như bộ lọc, ghi chú rằng narrative smart money là diễn giải và chưa có track record kiểm chứng độc lập): https://www.luxalgo.com/library/concept/model-2022/
- VideoHighlight — tóm tắt AI của *ICT Charter Price Action Model 13 — Charter Lecture On 2022 YouTube Model* (khung 5m → 1m, cửa sổ FX 07:00–10:00 / index 08:30–11:00 NY, limit tại mép FVG): https://videohighlight.com/v/kNlySn81dmo — *trang tự cảnh báo có thể không chính xác; cần đối chiếu video gốc.*

**Nguồn cơ chế thị trường (bình duyệt, được trích qua [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)|01c]]):**
- Osler, C. L. (2003). *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.* Journal of Finance.
- Osler, C. L. (2005). *Stop-loss orders and price cascades in currency markets.* Journal of International Money and Finance.
- Kavajecz, K. A. & Odders-White, E. R. (2004). *Technical Analysis and Liquidity Provision.* Review of Financial Studies.

**Nghiên cứu nội bộ vault:** [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] (null model, gate, audit) · [[59-Daily-Bias]] · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]] · [[50-Displacement-In-Depth]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]] · [[32-Top-down-Analysis-Multiple-Timeframes]]
