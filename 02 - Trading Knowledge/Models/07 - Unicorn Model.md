---
type: ict-concept
concept: Unicorn Model
aliases:
  - Unicorn Model
  - ICT Unicorn
  - Breaker + FVG Overlap
  - Unicorn Setup
tags:
  - trading/ict/model
  - trading/study
  - "#unicorn"
  - "#breaker"
  - "#fvg"
status: developing
category: Entry Model
last_reviewed: 2026-07-05
created: 2026-07-04
updated: 2026-07-05
---

# 07 - Unicorn Model

> [!info] Link
> [ICT Unicorn Model — Breaker Block & FVG Overlap Setup + Free PDF](https://innercircletrader.net/tutorials/ict-unicorn-model/)

> [!summary] Tóm tắt 1 câu
> **Unicorn Model là điểm vào xác suất cao xuất hiện khi một [[04 - Breaker Block|Breaker Block]] và một [[13 - FVG  - Fair Value Gap|Fair Value Gap]] CHỒNG LẤN trên cùng một vùng giá — vùng giao nhau đó ("unicorn") mang áp lực kép: vừa phải lấp imbalance (FVG), vừa là hỗ trợ/kháng cự cấu trúc (Breaker), nên mạnh hơn hẳn FVG đơn hay Breaker đơn.**

> [!important] Nguyên tắc cốt lõi
> **Không có chồng lấn = không có Unicorn.** Breaker và FVG phải *thực sự* chia sẻ cùng dải giá. Khi FVG nằm TRỌN bên trong Breaker, vùng mạnh "gấp đôi". Và **không bao giờ vào lệnh ngay tại khoảnh khắc MSS** — phải chờ giá HỒI về vùng unicorn (lý tưởng là 50% CE của FVG bên trong Breaker).

> [!tip] Bản đồ đọc note này
> Mục 1–3 = *WHAT* (định nghĩa, cấu phần). Mục 4–7 = *HOW* (hình thành, kịch bản, vào lệnh). Mục 2 & 10–11 = *WHY & nâng cao* (cơ chế, fractal, confluence). Mục 13–19 = *thực chiến & prop-firm* (best practices, journal, mastery). Nếu bạn mới học, đọc 1→7 trước; nếu đã trade, nhảy tới 8–13.

---

## 1. Định nghĩa

![[Unicorn-Advanced-Anatomy.svg|697]]

**Khái niệm:** Unicorn = sự **chồng lấn giá** giữa Breaker Block và FVG do cùng một cú displacement tạo ra. Vùng giao nhau là điểm vào. Nó hoạt động vì khi giá quay lại đây, nó chịu **hai lực đồng thời**:
- **Lấp imbalance** — FVG là vùng mất cân bằng, thuật toán có xu hướng rebalance nó (xem [[41 - Change in State of Delivery]]).
- **Hỗ trợ/kháng cự cấu trúc** — Breaker (một [[25 - OB - Order Block|Order Block]] đã "thất bại" và đảo vai) là mức mà tổ chức đã để lại lệnh.

**Nó trả lời câu hỏi nào trên chart?**
- Trong nhiều FVG/Breaker rải rác, đâu là **POI có xác suất phản ứng cao nhất**?
- Điểm vào nào có **hai lớp lý do** thay vì một?
- Vùng nào đáng đặt **limit** với stop chặt và RR lớn?

**Vì sao tên là "Unicorn"?** Vì đây là setup *hiếm và đẹp*: không phải cú hồi nào cũng tạo được overlap thật giữa Breaker và FVG. Chính sự hiếm này là lý do bạn nên **kiên nhẫn chờ**, thay vì ép mọi FVG thành unicorn.

### Unicorn KHÔNG phải là gì
- Không phải một FVG đơn lẻ, cũng không phải một Breaker đơn lẻ — bắt buộc **chồng lấn**.
- Không phải tín hiệu vào ngay khi MSS xảy ra — phải **retrace**.
- Không phải cái cớ để bỏ qua bias HTF — vẫn cần narrative + premium/discount đúng.
- Không phải "chén thánh": overlap chỉ *nâng xác suất*, không *đảm bảo* thắng. Vẫn cần quản trị rủi ro ≤0.5%/lệnh ([[43 - Position Sizing]]).

---

## 2. Vì sao Unicorn hoạt động — cơ chế hai lực

![[Unicorn-WhyItWorks.svg|697]]

> [!important] Hiểu WHY trước khi hỏi WHAT
> Trader mới học "Breaker + FVG chồng nhau thì vào" như một công thức, nhưng không hiểu *vì sao* overlap lại mạnh — nên họ không phân biệt được overlap "thật đáng tin" với overlap "tình cờ". Hai lực dưới đây là nền tảng.

**Lực 1 — Áp lực rebalance imbalance (từ FVG).** Một [[13 - FVG  - Fair Value Gap|Fair Value Gap]] là dấu vết của một cú giao dịch **một chiều quá nhanh** (displacement): thị trường đã "bỏ qua" một dải giá mà không giao dịch cân bằng hai chiều ở đó. Cơ chế phân phối giá (delivery algorithm) của ICT có xu hướng quay lại "trả lại giá trị" cho vùng bị bỏ qua này — nên FVG hoạt động như một **nam châm** kéo giá hồi về. Đây là lý do ta canh giá *quay lại* FVG, không đuổi theo cú đẩy.

**Lực 2 — Dấu chân tổ chức (từ Breaker).** Một [[04 - Breaker Block|Breaker Block]] là một Order Block đã **thất bại và đảo vai**: vùng mà một nhóm lệnh tổ chức từng được đặt, sau đó bị "bẫy" khi cấu trúc đảo chiều. Khi giá quay lại vùng này, các bên liên quan có động cơ **phòng thủ mức** (bảo vệ vị thế, thêm lệnh). Nên Breaker hoạt động như một **bức tường** hỗ trợ/kháng cự cấu trúc.

**Vì sao giao của hai lực mạnh hơn tổng của từng lực:** khi FVG *nằm trong* Breaker, giá quay về vùng đó gặp **cả nam châm rebalance lẫn tường cấu trúc cùng một điểm**. Nếu bias đúng, xác suất phản ứng không chỉ cộng tuyến tính mà *cộng dồn* — đây là lý do Unicorn cho phép **stop chặt hơn** (giá "không nên" xuyên qua nếu setup đúng) và do đó **RR lớn hơn**.

> [!warning] Hệ quả quan trọng
> Nếu overlap chỉ là *ngẫu nhiên* (Breaker và FVG do hai cú displacement khác nhau, không cùng narrative) thì "hai lực" đó không thực sự cùng câu chuyện — độ tin cậy giảm mạnh. **Overlap chất lượng nhất khi cả Breaker lẫn FVG được tạo bởi CÙNG một cú displacement/MSS.**

Liên hệ sâu: [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] giải thích vì sao đám đông đặt lệnh sai chỗ (tạo thanh khoản để thuật toán "ăn"), còn Unicorn là nơi bạn đứng *cùng phía* với dấu chân tổ chức thay vì phía đám đông.

---

## 3. Cấu phần bắt buộc

**Breaker Block** (xem [[04 - Breaker Block]]): là **Order Block thất bại**. Bullish breaker = những nến giảm cuối cùng trước cú đẩy lên đã (a) quét một đáy (SSL) rồi (b) displacement lên phá swing high. Bearish breaker là ảnh gương: nến tăng cuối trước cú đẩy xuống sau khi quét đỉnh (BSL).

**Fair Value Gap** (xem [[13 - FVG  - Fair Value Gap]]): khe mất cân bằng để lại bởi chính cú displacement tạo MSS. Bullish = **BISI** (buyside imbalance sellside inefficiency); bearish = **SIBI**.

**Chồng lấn (overlap):** hai vùng trên phải cắt nhau về giá.

| Mức chồng lấn | Mô tả | Đánh giá |
|---|---|---|
| FVG nằm **trọn** trong Breaker | Toàn bộ dải FVG lọt trong dải Breaker | **Chất lượng cao nhất (A+)** |
| Chồng lấn **một phần** | Hai dải cắt nhau nhưng không bao trùm | Dùng được (A/B); vào tại phần giao |
| **Tiếp giáp** (chạm mép) | Chỉ chạm biên, không thực sự cắt | Yếu — hạ cấp hoặc bỏ |
| **Tách rời** | Breaker trên, FVG dưới (hoặc ngược) | **KHÔNG phải Unicorn** — bỏ |

> [!tip] Quy tắc "đo trước, tin sau"
> Luôn **đo bằng công cụ** phần giao nhau về giá. Cảm giác "chúng gần nhau" không đủ — nếu không cắt nhau thì đây chỉ là FVG đơn / Breaker đơn.

---

## 4. Chuỗi hình thành

![[Unicorn-Advanced-Formation-Sequence.svg|697]]

1. **Bias + Premium/Discount** — HTF bias rõ ([[27 - Premium Discount]], [[12 - Daily Bias]]).
2. **Quét thanh khoản** — [[20 - Liquidity Sweep|sweep]] một đỉnh/đáy (inducement/stop hunt — xem [[15 - Inducement]]).
3. **Displacement + [[21 - Market Structure Shift|MSS]]** — cú đẩy mạnh phá cấu trúc, để lại **FVG** và hình thành **Breaker**.
4. **Chồng lấn** — FVG rơi vào trong Breaker = **vùng Unicorn**.
5. **Retrace entry** — chờ giá hồi về vùng, KHÔNG vào lúc MSS.

> [!note] Vì sao thứ tự này bắt buộc
> Bỏ bước 2 (sweep) = bạn có thể đang vào một MSS "giả" không có nhiên liệu thanh khoản đứng sau. Bỏ bước 3 (displacement thật) = Breaker/FVG hình thành yếu, dễ bị xuyên. Bỏ bước 5 (retrace) = bạn chase và đặt stop xa, phá vỡ ưu thế RR của model.

---

## 5. Bullish vs Bearish

![[Unicorn-Advanced-Bullish-vs-Bearish.svg|697]]

**Bullish Unicorn:** giá quét **SSL (đáy)** → displacement lên phá swing high → bullish breaker + BISI/FVG chồng lấn → mua khi hồi về vùng. Target hướng lên [[16 - Internal & External Range Liquidity (IRL & ERL)|BSL/ERL]].

**Bearish Unicorn:** giá quét **BSL (đỉnh)** → displacement xuống phá swing low → bearish breaker + SIBI/FVG chồng lấn → bán khi hồi về vùng. Target hướng xuống SSL/ERL.

---

## 6. Hai bối cảnh: Reversal vs Continuation

![[Unicorn-Advanced-Reversal-vs-Continuation.svg|697]]

**Reversal Unicorn:** sau khi quét một đỉnh/đáy **lớn** (major high/low), kỳ vọng đảo chiều — rủi ro cao hơn, cần bias HTF ủng hộ mạnh và tốt nhất có [[42 - SMT Divergence]] xác nhận.

**Continuation Unicorn:** sau pullback/inducement **thuận** xu hướng đang chạy — xác suất cao hơn, ưu tiên. Đây là dạng nên tập trung khi mới học vì nó đi *cùng* dòng chảy HTF.

> [!tip] Ưu tiên khi phân vân
> Nếu không chắc đang ở reversal hay continuation, **mặc định coi là continuation** và chỉ trade khi thuận [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|DOL]] HTF. Reversal chỉ nên đánh khi bias HTF *đã* nghiêng về đảo chiều từ trước, không phải "hy vọng đảo".

---

## 7. Vào lệnh, Stop & Target

![[Unicorn-Advanced-Entry-CE.svg|697]]

- **Entry:** đặt **limit** tại vùng chồng lấn, lý tưởng là **50% CE** ([[10 - Consequent Encroachment (Mean Threshold)]]) của FVG nằm trong Breaker.
- **Stop:** vượt qua **wick của cú sweep** / cạnh xa của Breaker — không phải con số cố định.
- **Target:** [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL trước, ERL sau]]. Dời stop về BE sau khi chạm T1. RR thường lớn nhờ stop chặt.
- **Timing:** ưu tiên vùng hình thành trong [[18 - Kill Zones|killzone]] / [[40 - Macro Times|macro]].

![[Unicorn-Stop-Logic.svg|697]]

> [!example] Mẫu ghi nhanh — Unicorn (Bullish)
> ```text
> Bias (HTF): Bullish | DOL: BSL @ [level]
> Location: Discount
> (1) Sweep SSL @ [level] (wick)
> (2) Displacement lên + MSS phá [swing high] → BISI/FVG + bullish breaker
> (3) Overlap: FVG [low]-[high] nằm trong Breaker [low]-[high]
> (4) Entry: limit @ 50% CE = [mid] | Stop: dưới wick sweep @ [level]
> (5) T1 = IRL [..] (dời BE) → T2 = ERL [..]
> Killzone/Macro: [..] | SMT: [có/không]
> Invalid: đóng nến qua cạnh xa Breaker
> ```

> [!warning] Ba lỗi quản trị lệnh phổ biến
> 1. **Stop tại MSS pivot** (quá chặt) → bị wick quét vô lý. Đặt ngoài **toàn bộ** wick sweep.
> 2. **Không dời BE sau T1** → biến lệnh thắng thành hòa/thua.
> 3. **Chốt hết tại T1** → bỏ lỡ phần lớn move; nên chốt bậc thang IRL → ERL.

---

## 8. Xếp hạng chất lượng setup (Grading)

![[Unicorn-Grading-Matrix.svg|697]]

Không phải unicorn nào cũng ngang nhau. Chấm điểm **khách quan** trước khi bấm lệnh giúp bạn *size theo chất lượng* thay vì theo cảm xúc.

| Hạng | Điều kiện | Hành động |
|---|---|---|
| **A+** | FVG nằm trọn trong Breaker + đúng P/D + displacement sạch (có CISD) + trong killzone/macro + có SMT + thuận DOL (≥5/6) | Full size (≤0.5%) |
| **A** | Overlap rõ + đúng bias/P/D + displacement ổn, thiếu 1–2 confluence phụ (3–4/6) | Size chuẩn |
| **B** | Overlap nhỏ/mỏng, displacement trung bình, hoặc ngoài killzone (2/6) | Half-size hoặc bỏ |
| **Bỏ qua** | Không overlap thật / ngược bias / không sweep trước / chỉ vào được bằng chase | Không trade |

> [!tip]
> Ghi **grade** vào frontmatter mỗi trade (mục 17). Sau 20–30 lệnh, so win-rate theo grade — nếu B thua đều đặn, đó là bằng chứng khách quan để **bỏ hẳn B**.

---

## 9. Unicorn theo từng thị trường

![[Unicorn-CrossMarket.svg|697]]

Cùng cấu trúc overlap, nhưng độ sạch của displacement và độ dài wick khác nhau giữa các thị trường bạn đang trade.

| Đặc tính | NQ1 / NDX (NAS100) | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Độ sắc của overlap | Sắc nét trên 1m/5m | Thường mỏng hơn (range hẹp) | Rộng, wick dài |
| Displacement | Dứt khoát, đặc biệt quanh 09:30 mở NYSE | Rõ quanh London/NY open | Rất mạnh quanh tin (CPI/NFP/FOMC) |
| Rủi ro đặc thù | Nhiều FVG nhỏ chồng → dễ chọn nhầm overlap | Spread có thể "nuốt" overlap nhỏ | Wick dài dễ quét stop dù hướng đúng |
| Điều chỉnh thực dụng | Ưu tiên FVG **first & clean** ngay sau MSS | Tính spread vào CE; đòi overlap đủ rộng | Nới stop ngoài wick sweep; **giảm size** |
| Killzone hiệu quả nhất | NY AM, 09:50 macro | London Open, NY AM | London, NY AM, quanh giờ tin |

> [!tip]
> Quy tắc gọn: **NQ → chọn overlap "sạch đầu tiên"; FX → đòi overlap đủ rộng so với spread; Gold → nới stop & giảm size vì wick.**

---

## 10. Biến thể nâng cao — Unicorn lồng trong PD array HTF (Nested / Fractal)

![[Unicorn-Nested-Fractal.svg|697]]

> [!important] Đây là nơi Unicorn chuyển từ "setup LTF ngẫu nhiên" sang "vũ khí có bối cảnh"
> Một Unicorn LTF (5m/1m) **mạnh nhất khi nó hình thành BÊN TRONG một POI HTF cùng hướng** — ví dụ bullish unicorn 5m xuất hiện đúng lúc giá hồi về một bullish Order Block/discount POI trên H1/H4. Khi đó bạn có xác suất của cả hai khung: HTF cho *nơi*, LTF cho *thời điểm & entry chính xác*.

**Quy trình top-down (xem [[32 - Top-down Analysis (Multiple Timeframes)]]):**
1. **H4/H1:** xác định bias, DOL, và POI HTF (OB/FVG/breaker) mà giá đang hướng về.
2. Chờ giá **hồi về POI HTF** đó (vùng discount cho long / premium cho short).
3. **Zoom xuống 5m/1m** ngay tại POI HTF, tìm chuỗi sweep → displacement/MSS → Unicorn.
4. Entry LTF tại 50% CE của unicorn; **target = ERL của khung HTF** (không chỉ IRL nhỏ).

**Vì sao lồng khung tăng chất lượng:** POI HTF cho bạn lý do "giá nên phản ứng ở đây"; unicorn LTF cho bạn entry stop-chặt để khai thác phản ứng đó với RR lớn. Đây cũng là cách [[07 - Unicorn Model|Unicorn]] gắn vào các model khung lớn hơn — mỗi LRB của [[04 - Market Maker Buy Model – MMBM|MMBM]] hoặc mỗi retest của [[08 - 08 30 AM NY Model]] thường *chính là* một unicorn LTF.

> [!warning] Bẫy fractal
> Đừng đánh unicorn LTF **ngược** với POI HTF. Một bearish unicorn 1m xuất hiện giữa lúc giá đang hồi về một *bullish* POI H4 thường chỉ là nhiễu — bạn đang đứng ngược dòng lớn hơn.

---

## 11. Xếp chồng confluence (Confluence Stack)

Unicorn là *lõi cấu trúc*; các lớp dưới đây là *chất xúc tác* nâng grade:

- **Premium/Discount đúng** ([[27 - Premium Discount]]): bullish unicorn nên nằm ở discount của dealing range; bearish ở premium. Unicorn ở "sai nửa" range là cảnh báo.
- **SMT Divergence** ([[42 - SMT Divergence]]): NQ vs ES, EU vs GU phân kỳ tại điểm sweep = xác nhận mạnh cho reversal unicorn.
- **Killzone / Macro** ([[18 - Kill Zones]], [[40 - Macro Times]]): unicorn hình thành trong 09:50–10:10 (NQ) hoặc macro forex đáng tin hơn hẳn ngoài giờ.
- **CISD / Displacement chất lượng** ([[41 - Change in State of Delivery]]): nến displacement thân lớn, ít chồng lấn → FVG/Breaker "sạch".
- **OTE overlap** ([[26 - OTE - Optimal Trade Entry]]): nếu 50% CE của unicorn trùng vùng OTE 62–79% của nhịp đẩy → confluence điểm vào.
- **NWOG/NDOG lân cận** ([[24 - New Week Opening Gap]], [[23 - New Day Opening Gap]]): unicorn gần các gap mở cửa thường được "tôn trọng" hơn.

> [!note] Nguyên tắc confluence
> Confluence để **nâng grade và size**, không để "biện minh" cho một setup không có overlap thật. Không bao giờ đánh đổi: "không overlap nhưng có SMT nên vẫn vào" → đó không còn là Unicorn.

---

## 12. Ví dụ chart

### Ví dụ đúng
![[Unicorn-Example-Correct.svg|697]]

**Mô tả:** FVG nằm trọn trong Breaker, thuận HTF bias, hình thành trong killzone, có SMT divergence xác nhận; limit tại 50% CE.

**Vì sao tốt:** overlap thật + displacement sạch + đúng bias + đúng thời gian + entry retrace (không đuổi).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lệnh thật: đánh dấu (1) mức thanh khoản bị quét, (2) nến displacement/MSS, (3) Breaker (tô cam) và FVG (tô xanh) và phần chồng lấn (tím), (4) điểm limit 50% CE, (5) T1/T2. Ghi giờ ET + grade A+/A/B.*

### Ví dụ sai / dễ nhầm
![[Unicorn-Example-Wrong.svg|697]]

**Mô tả lỗi:** Breaker ở trên, FVG ở dưới, **tách rời** → không có vùng chồng lấn → **không phải Unicorn**. Hoặc vào ngay lúc MSS không chờ hồi, hoặc trade ngược bias.

**Bài học:** luôn **đo** phần chồng lấn; nếu không cắt nhau thì đây chỉ là FVG đơn / Breaker đơn, không phải setup unicorn.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lần bạn (hoặc người khác) gọi nhầm là unicorn: đánh dấu vì sao overlap không tồn tại, hoặc vì sao entry là chase. Đây là tư liệu quý cho review.*

---

## 13. Thực hành tốt nhất (Best Practices)

> [!summary]
> Đây là các thói quen ở mức chuyên nghiệp / chuẩn prop-firm — thứ phân biệt trader đọc đúng unicorn một cách nhất quán với trader chỉ thấy "hai hộp gần nhau là vào". Mục tiêu: không gọi nhầm overlap, không chase, không ngược HTF, và bảo toàn vốn qua vòng đánh giá prop-firm.

> [!tip] Quy tắc Unicorn (5 điều cốt lõi)
> 1. **Đo overlap thật** — nếu Breaker và FVG không cắt nhau về giá, bỏ qua.
> 2. **Yêu cầu displacement chất lượng** — nến đẩy mạnh, ít chồng lấn; nến yếu → hạ cấp setup.
> 3. **Thuận HTF bias + DOL** — unicorn ngược dòng tuần là bẫy.
> 4. **Ưu tiên timing** — killzone/macro (đặc biệt 09:50→10:10 NQ, macro forex).
> 5. **Đặt limit, không chase** — vào tại 50% CE; nếu giá không hồi về, bỏ lệnh.

### Quy trình pre-session (15–30 phút trước killzone)
1. **H4/H1:** xác định bias + DOL + đánh dấu các POI HTF (nơi unicorn LTF *có thể* hình thành).
2. Đánh dấu các pool thanh khoản (SSL/BSL) mà giá có thể quét trước khi tạo displacement.
3. Xác định trước **premium/discount** của dealing range hiện tại.
4. Viết sẵn kịch bản: "*Nếu* giá sweep [level] rồi displacement, tôi tìm unicorn ở [POI], entry ~[CE dự kiến], stop [..], target [..]."
5. Đặt sẵn ngưỡng **no-trade**: ngoài killzone / không có overlap / ngược bias → không đánh.

### Kỷ luật `missing_step` — biến review thành nghi thức tuần
- Với mỗi lệnh Unicorn thua/BE, bắt buộc điền `missing_step` (mục 17): `overlap` (không có overlap thật), `retrace` (chase, vào lúc MSS), `bias` (ngược HTF), `displacement` (đẩy yếu), `stop` (đặt sai stop), `timing` (ngoài killzone).
- Cuối tuần ([[07 - Reviews]]): thống kê tần suất. Giá trị nào chiếm >40% lệnh thua = **ưu tiên sửa số 1** tuần sau, gắn `[[Mistake - ...]]` tương ứng.

### Kỳ vọng thực tế về tần suất
- Unicorn A+ **không xuất hiện mỗi ngày**. Trên NQ, một tuần có thể chỉ 2–5 setup A/A+ đáng đánh. Phần lớn thời gian không có overlap thật — nhiệm vụ lúc đó là *chờ và đánh dấu*, không ép setup.
- "Trông giống unicorn" ≠ "là unicorn". Chỉ tính là một setup khi đã **đo được overlap** + đủ chuỗi hình thành (mục 4).

### Scale size chỉ sau khi có dữ liệu
- Không tăng size vì vài lệnh thắng liên tiếp "cảm thấy đúng". Chuẩn tối thiểu: **≥30 mẫu backtest** unicorn (tag đầy đủ frontmatter) qua [[04 - Backtesting|_Backtest Dashboard]], rồi forward-test 15–20 lệnh trước khi về mức chuẩn ≤0.5%/lệnh.

### Amateur vs Professional

| Khía cạnh | Amateur | Professional (chuẩn prop-firm) |
|---|---|---|
| Nhìn thấy Breaker & FVG gần nhau | Vào ngay, gọi là "unicorn" | Đo overlap; không cắt nhau → bỏ |
| Sau MSS | Market order đuổi giá | Đặt limit tại 50% CE, chờ hồi |
| Bias HTF | Bỏ qua, chỉ nhìn LTF | Chỉ đánh thuận DOL H4/H1 |
| Chọn size | Cảm xúc / "chắc kèo" | Theo grade A+/A/B đã chấm |
| Không có setup | Ép một cái để "có việc làm" | Chấp nhận ngày không trade |
| Sau lệnh thua | Trade gỡ ngay | Ghi `missing_step`, chờ setup thật |
| Tăng size | Sau vài lệnh thắng | Sau ≥30 mẫu backtest xác nhận |

- Kết hợp với các model khung ngày: [[08 - 08 30 AM NY Model]] và [[08 - 7 AM Liquidity Hunt + IFVG Entry]] thường tạo unicorn tại PD array sau MSS — khi PD array của chúng *chính là* Breaker+FVG chồng lấn thì đó là biến thể A+.

> [!tip]
> Nếu tóm Best Practices thành một câu: **"Đo overlap, chờ hồi, thuận HTF — chỉ đánh khi cả cấu trúc lẫn bối cảnh đồng ý, không phải khi hai cái hộp trông gần nhau."**

---

## 14. Checklist trước khi vào lệnh

- [ ] HTF bias rõ ràng, đúng hướng (thuận DOL)
- [ ] Giá ở Premium/Discount phù hợp
- [ ] Đã có sweep thanh khoản trước displacement
- [ ] Displacement tạo **MSS** rõ + FVG sạch (lý tưởng có CISD)
- [ ] Breaker hình thành và **chồng lấn** với FVG (đo được)
- [ ] Đã chấm **grade** (A+/A/B) theo ma trận mục 8
- [ ] Đặt limit tại **50% CE** của FVG trong Breaker
- [ ] Stop vượt wick sweep / cạnh xa Breaker
- [ ] T1 = IRL, T2 = ERL; RR đạt kế hoạch
- [ ] (Ưu tiên) trong killzone/macro + có SMT + trong POI HTF (nested)
- [ ] Không vào lúc MSS, không chase, không ngược bias

---

## 15. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Gọi nhầm FVG/Breaker đơn là unicorn | Không có phần chồng lấn | Mất "lực kép", xác suất chỉ như POI đơn | Đo overlap; bắt buộc cắt nhau về giá |
| Vào lúc MSS | Market order ngay nến displacement | Stop xa, phá vỡ ưu thế RR | Chờ hồi về 50% CE, đặt limit |
| Ngược bias | Setup đẹp nhưng ngược dòng tuần | Đứng ngược DOL HTF | Ưu tiên HTF narrative + DOL |
| Displacement yếu | Nến chồng lấn, không dứt khoát | Breaker/FVG "mỏng", dễ bị xuyên | Chỉ nhận displacement mạnh, có FVG rõ |
| Stop quá chặt/quá xa | Đặt tại MSS hoặc quá rộng | Bị quét vô lý / RR kém | Stop vượt wick sweep / cạnh xa Breaker |
| Bỏ qua bối cảnh HTF | Chỉ nhìn LTF | Unicorn LTF ngược POI HTF = nhiễu | Kiểm tra nested (mục 10) trước khi vào |
| Ép setup ngày không có | "Cố tìm" unicorn mỗi ngày | Đánh cả B/rác → cháy dần | Chấp nhận ngày no-trade |

---

## 16. Câu hỏi tự kiểm & Flashcards

### Câu hỏi tự kiểm nhanh
- Overlap có **thật** không (đo được), hay chỉ "gần nhau"?
- Đã có sweep + displacement + MSS trước khi overlap hình thành chưa?
- Tôi đang thuận hay ngược DOL HTF?
- Setup này grade mấy? Size tương ứng?
- Nó có nằm trong một POI HTF cùng hướng không (nested)?
- Nếu không trade, lý do "No Trade" là gì?

### Flashcards

**Q1 — Unicorn được tạo bởi sự kết hợp của gì?**
Breaker Block **chồng lấn** với FVG (do cùng cú displacement) → vùng unicorn có lực kép: rebalance imbalance + hỗ trợ/kháng cự cấu trúc.

**Q2 — Vào lệnh ở đâu và khi nào?**
Limit tại **50% CE** của FVG bên trong Breaker, trên **nhịp hồi** sau MSS — không vào lúc MSS.

**Q3 — Điều gì làm setup unicorn INVALID?**
Breaker và FVG không chồng lấn; hoặc giá đóng nến hẳn qua cạnh xa của Breaker mà không phản ứng.

**Q4 — Vì sao overlap mạnh hơn POI đơn?**
Vì giá gặp *hai lực độc lập cùng một điểm*: nam châm rebalance (FVG) + tường cấu trúc (Breaker). Xác suất phản ứng cộng dồn → cho phép stop chặt, RR lớn.

**Q5 — Unicorn "A+" cần gì?**
FVG nằm trọn trong Breaker + đúng P/D + displacement sạch + trong killzone/macro + có SMT + thuận DOL (≥5/6), lý tưởng nằm trong POI HTF (nested).

**Q6 — Điều chỉnh gì khi đánh XAUUSD?**
Nới stop ngoài wick sweep (wick dài quanh tin) và **giảm size** — overlap rộng nhưng dễ bị xuyên rồi hồi.

---

## 17. Liên kết với Trade Journal

### Lệnh áp dụng đúng model này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault dùng path riêng, thay `FROM ""` bằng `FROM "05 - Live Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: Unicorn # Unicorn | ICT-2022 | MMBM | MMSM | 0830-NY | 0700-IFVG
bias: bullish # bullish | bearish
context: continuation # continuation | reversal
overlap: full # full | partial | none
grade: A+ # A+ | A | B
entry_ce: true # vào tại 50% CE
nested_htf_poi: true # unicorn nằm trong POI HTF cùng hướng
smt: true
killzone: NY-AM
rr_planned: 4.0
missing_step: none # none | overlap | retrace | bias | displacement | stop | timing
```

> [!tip]
> Với lệnh thua, ghi `missing_step` để biết hay sai ở đâu — phổ biến nhất là `overlap` (không có overlap thật) hoặc `retrace` (chase, vào lúc MSS).

---

## 18. Lesson Learned

### Bài học chính
- Unicorn = **overlap thật** giữa Breaker và FVG do cùng displacement → lực kép.
- Chỉ vào tại **50% CE trên nhịp hồi**, không chase; stop ngoài wick sweep / cạnh xa Breaker.
- **Thuận HTF bias + DOL**; unicorn ngược dòng là bẫy.
- Mạnh nhất khi **nested trong POI HTF** cùng hướng + có confluence (SMT/killzone/CISD).
- Chấm **grade** và size theo grade; chấp nhận ngày không có setup.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn **đo** overlap trước khi gọi là unicorn.
- [ ] Tôi đặt limit tại 50% CE, không vào lúc MSS.
- [ ] Tôi chỉ đánh thuận DOL HTF, ưu tiên nested trong POI HTF.
- [ ] Tôi chấm grade và size theo grade, không theo cảm xúc.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc khi trade
> **"Không đo được overlap thì không phải unicorn. Chờ hồi, thuận HTF, đặt limit — không đuổi."**

---

## 19. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu cơ chế hai lực (WHY) | | Giải thích được vì sao overlap mạnh? |
| Đo & nhận diện overlap thật | | Phân biệt overlap thật vs tách rời? |
| Chờ retrace, đặt limit đúng | | Không chase lúc MSS? |
| Chấm grade + size theo grade | | Có kỷ luật A+/A/B? |
| Kết hợp bối cảnh HTF (nested) | | Kiểm tra POI HTF trước khi vào? |
| Áp dụng vào trade thực tế | | Entry thật ở 50% CE sau MSS? |
| Review sau trade | | Có gắn `missing_step` + review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập ≥20–30 setup tag `[[Unicorn Model]]`.
- [ ] Review theo `missing_step`: hay sai ở `overlap`, `retrace`, hay `bias`.
- [ ] Thống kê win-rate theo `grade`, `context` (reversal/continuation), và `nested_htf_poi`.
- [ ] Cập nhật rule khi đủ mẫu; nâng `confidence` trong frontmatter khi đạt mastery.
