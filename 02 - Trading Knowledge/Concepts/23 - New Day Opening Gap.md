---
type: ict-concept
concept: New Day Opening Gap
aliases:
  - New Day Opening Gap
  - NDOG
  - Daily Opening Gap
tags:
  - trading/ict/concept
  - trading/study
  - "#NDOG"
status: seed
category: Time & Price
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
models:
  - "[[ICT 2022 Model]]"
importance: 4
confidence: 1
created: 2026-06-26
updated: 2026-07-03
related_concepts:
  - "[[24 - New Week Opening Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
  - "[[27 - Premium Discount]]"
  - "[[18 - Kill Zones]]"
prerequisites:
  - "[[Fair Value Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[24 - New Week Opening Gap]]"
common_mistakes: []
---

# New Day Opening Gap

> [!summary] Tóm tắt 1 câu
> **New Day Opening Gap (NDOG) là khoảng gap giá giữa giá đóng cửa phiên regular của NGÀY hôm trước (~16:00–16:15 ET) và giá mở cửa khi futures reopen vào ~18:00 ET (sau khi nghỉ bảo trì 17:00–18:00 ET); đây là phiên bản THEO NGÀY của [[24 - New Week Opening Gap]] — một mốc tham chiếu fair value và draw on liquidity cho ngày mới, với đường giữa (Consequent Encroachment / CE 50%) là nam châm và support/resistance.**

> [!important] Nguyên tắc cốt lõi
> - **CE (50% của NDOG) là mốc quan trọng nhất**, không phải các cạnh gap. Giá bị hút về CE rồi phản ứng tại đó. (Xem [[10 - Consequent Encroachment (Mean Threshold)]].)
> - **Giữ 1–3 NDOG gần nhất trên chart** như đường tham chiếu cố định. Đừng xóa khi gap đã "fill" — gap đã fill vẫn là support/resistance.
> - NDOG là một **vùng fair value** sinh ra từ ngắt quãng thời gian (giờ nghỉ bảo trì hằng ngày), không phải FVG/imbalance nội phiên.
> - **NDOG nhỏ hơn và ít sức nặng hơn [[24 - New Week Opening Gap]]** — khi NDOG trùng NWOG thì confluence càng mạnh, ưu tiên mốc tuần.
> - Dùng NDOG để trả lời: **giá đang ở premium hay discount của ngày?** và **đâu là draw on liquidity tự nhiên trong ngày?**

---

## 1. Định nghĩa

### Khái niệm
**New Day Opening Gap (NDOG)** là khoảng cách giá giữa:
- **Cạnh 1 = Prior Day Close (Regular Session Close)**: giá đóng cửa phiên regular của ngày hôm trước trên index/CME futures, lấy quanh **16:00 ET** (cash close), thường được dẫn là **~16:15 ET** với regular session close của index futures.
- **Cạnh còn lại = Reopen**: giá mở cửa khi thị trường futures mở lại vào **~18:00 ET**, sau khi nghỉ giờ bảo trì/halt hằng ngày **17:00–18:00 ET**.

Vì thị trường **không giao dịch qua khoảng nghỉ ~1¾ giờ** đó, vùng giữa hai mức giá là một **inefficiency / fair value reference** mặc định cho ngày mới — chính là **bản sao theo ngày** của weekend gap [[24 - New Week Opening Gap]].

### Bản chất
- NDOG không sinh ra từ một cú displacement trong phiên như FVG, mà sinh ra từ **sự ngắt quãng thời gian** (giờ nghỉ bảo trì hằng ngày). Đây là một dạng **fair value gap theo thời gian**, không phải theo cấu trúc nến.
- Vì giá "nhảy" từ Prior Close sang Reopen mà không qua giao dịch, vùng ở giữa giống một **liquidity void / vùng fair value chưa được kiểm định** — thị trường có xu hướng quay lại "balance" lại vùng này.
- ICT lập luận rằng các **Interbank / market maker** dùng các mốc này như mốc tham chiếu giá hợp lý, nên giá thường gravitate (bị hút) về NDOG, đặc biệt là về CE.

### Cách vẽ gap + CE 50%
1. Xác định **Prior Day Close** (~16:00–16:15 ET): vẽ một đường ngang tại mức giá đóng cửa regular của ngày hôm trước.
2. Xác định **Reopen** (~18:00 ET): vẽ một đường ngang tại mức giá mở cửa đầu tiên sau giờ nghỉ bảo trì.
3. Vùng giữa hai đường = **NDOG range** (tô màu / box).
4. Tính **CE = (Prior Close + Reopen) / 2** → vẽ đường giữa. **Đây là mức quan trọng nhất.** (Xem [[10 - Consequent Encroachment (Mean Threshold)]].)
5. Đặt tên & màu cố định, **giữ lại 1–3 NDOG gần nhất** trên chart như mốc tham chiếu (ít hơn NWOG vì sức nặng nhỏ hơn).

```text
Prior Day Close (~16:00–16:15 ET) ── cạnh trên ──┐
                                                 │  NDOG range
              CE (50%) ───────●──────────────────│  ← mức nam châm / SR chính
                                                 │
Reopen (~18:00 ET) ───────────── cạnh dưới ──────┘
```

### So sánh với NWOG (New Week Opening Gap)
- **NWOG = New Week Opening Gap**: gap cuối tuần giữa Friday Close (~16:59–17:00 ET settlement) và Sunday Open (~17:00–18:00 ET). Là mốc tham chiếu cho **cả tuần** — sức nặng lớn, giữ 3–5 cái.
- **NDOG là phiên bản NGÀY** của NWOG: mốc tham chiếu intraday/daily, sức nặng nhỏ hơn, giữ ít hơn (1–3 cái).
- Khi **NDOG và NWOG trùng/chồng nhau** → vùng đó càng có sức nặng tham chiếu; ưu tiên NWOG (mốc tuần) khi xung đột.

| Thuộc tính | NDOG | NWOG |
|---|---|---|
| Khoảng thời gian | Trong ngày (prev close → reopen) | Cuối tuần (Fri → Sun) |
| Mốc đóng cửa | Prior day ~16:00–16:15 ET | Friday ~16:59–17:00 ET |
| Mốc mở cửa | Reopen ~18:00 ET | Sunday ~17:00–18:00 ET |
| Sức nặng | Trung bình (tham chiếu ngày) | Cao (tham chiếu cả tuần) |
| Số lượng giữ trên chart | 1–3 cái gần nhất | 3–5 cái gần nhất |
| Khi trùng nhau | Confluence mạnh hơn | Ưu tiên hơn NDOG |

### Mục đích trong ICT
- Cung cấp **mốc tham chiếu fair value** cho ngày giao dịch.
- Là một **draw on liquidity** tự nhiên trong ngày: giá thường hướng về NDOG/CE chưa được fill.
- Làm **support/resistance** và xác định bias premium/discount của ngày (xem [[27 - Premium Discount]], [[12 - Daily Bias]]).

### Vì sao quan trọng
- Giờ nghỉ bảo trì hằng ngày khiến thị trường **không giao dịch** trong ~1¾ giờ → tạo inefficiency không thể fill trong khoảng thời gian đó → "nợ kỹ thuật" mà thị trường thường quay lại trả trong phiên kế tiếp.
- Là mốc **khách quan, không vẽ tay mơ hồ** — chỉ cần Prior Close và Reopen, ai vẽ cũng giống nhau → giảm chủ quan.

### Nó giúp trả lời câu hỏi nào trên chart?
- Giá hôm nay đang ở **premium hay discount** so với CE của NDOG?
- **Draw on liquidity** tự nhiên của ngày nằm ở đâu (NDOG nào chưa fill)?
- Đâu là **support/resistance** đáng tin để chờ phản ứng vào kill zone?
- Khi giá tiếp cận NDOG/CE, nên **kỳ vọng phản ứng** (đảo chiều/chậm lại) thay vì đu theo đà.

### NDOG không phải là gì
- **Không phải** là tín hiệu entry trực tiếp — nó là **mốc tham chiếu/draw**, cần xác nhận tại đó.
- **Không phải** FVG nội phiên — nó sinh từ ngắt quãng thời gian, không từ displacement.
- **Không phải** thứ chắc chắn "fill ngay trong ngày" — có thể mất nhiều ngày mới quay lại; gap đã fill vẫn là SR.
- **Không phải** thứ để xóa khi đã được chạm — giữ lại làm mốc lịch sử.
- **Không phải** thay thế cho [[24 - New Week Opening Gap]] — NDOG có sức nặng nhỏ hơn, là bổ trợ cho mốc tuần.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái

| Trạng thái | Mô tả | Hàm ý giao dịch |
|---|---|---|
| **Gap up** | Reopen > Prior Close | Ngày mở trong premium so với prior close; CE phía dưới có thể là draw |
| **Gap down** | Reopen < Prior Close | Ngày mở trong discount so với prior close; CE phía trên có thể là draw |
| **Inside / no gap** | Reopen ≈ Prior Close (gap rất nhỏ) | NDOG mỏng, ít sức nặng; ưu tiên NDOG cũ / NWOG hơn |
| **Filled NDOG** | Giá đã trade lại qua toàn bộ range gap | Gap đã "trả nợ"; vẫn là SR, CE vẫn phản ứng |
| **Unfilled NDOG** | Giá chưa quay lại chạm/lấp gap | Là **draw on liquidity** trong ngày — mục tiêu tiềm năng |

### Khi nào giá trị cao? (checklist)
- [ ] Giá đang gần hoặc đang hướng về một **NDOG chưa fill** (unfilled).
- [ ] CE của NDOG trùng với một PD-array khác ([[Order Block]], [[Fair Value Gap]], [[08 - Central Bank Dealers Range]]).
- [ ] NDOG **trùng/chồng với một NWOG** → confluence mạnh.
- [ ] NDOG nằm tại biên premium/discount của dealing range trong ngày.
- [ ] Có **confluence** với [[19 - Liquidity]] (buyside/sellside) ngay cạnh NDOG.
- [ ] Phản ứng được kỳ vọng trong [[18 - Kill Zones]] (London/NY).

### Khi nào bỏ qua? (checklist)
- [ ] Gap quá nhỏ/inside (gần như không có gap) → ít ý nghĩa.
- [ ] Giá đang ở rất xa NDOG và không có draw rõ ràng về nó.
- [ ] Tin tức lớn (high-impact news) đang làm giá chạy mạnh, bỏ qua mọi mốc fair value.
- [ ] NDOG bị "che" bởi một mức HTF mạnh hơn ([[24 - New Week Opening Gap]], weekly OB) — ưu tiên mức mạnh hơn.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Hai mốc giá rõ ràng**: Prior Day Close (~16:00–16:15 ET) và Reopen (~18:00 ET).
2. **Khoảng trống thời gian** giữa hai mốc (giờ nghỉ bảo trì, không có nến 17:00–18:00 ET).
3. **Đường CE 50%** nằm chính giữa range.
4. Giá lịch sử cho thấy **phản ứng tại CE / các cạnh** (đảo chiều, từ chối, chậm lại).
5. NDOG chưa fill tạo thành **mục tiêu hút giá** (draw on liquidity) trong ngày.

### Ma trận nhận diện

| Yếu tố | NDOG hợp lệ & đáng tin | NDOG yếu / bỏ qua |
|---|---|---|
| Độ rộng gap | Đủ rộng, dễ thấy | Quá mỏng / inside |
| Vị trí trong dealing range | Tại biên premium/discount | Giữa range, mờ nhạt |
| Confluence PD-array | Trùng OB/FVG/CBDR/NWOG | Đứng một mình |
| Trạng thái | Unfilled (draw) hoặc CE chưa test | Đã fill nhiều lần, không phản ứng |
| Phản ứng lịch sử | Có rejection rõ tại CE/cạnh | Giá xuyên qua không phản ứng |
| Kill zone | Tiếp cận trong London/NY KZ | Tiếp cận lúc thanh khoản thấp |

### Điều kiện bắt buộc (must-have)
- [ ] Xác định đúng **Prior Day Close (~16:00–16:15 ET)** và **Reopen (~18:00 ET)** theo đúng múi giờ ET.
- [ ] Vẽ đúng **CE = 50%** của range.
- [ ] Đặt trong bối cảnh [[12 - Daily Bias]] / [[27 - Premium Discount]] của ngày.

### Tăng xác suất (nice-to-have)
- [ ] Confluence với PD-array khác (OB, FVG, CBDR — xem [[08 - Central Bank Dealers Range]]).
- [ ] NDOG trùng/chồng [[24 - New Week Opening Gap]].
- [ ] Trùng với [[19 - Liquidity]] pool gần đó.
- [ ] Tiếp cận trong [[18 - Kill Zones]].
- [ ] NDOG còn **unfilled** (draw mạnh hơn).

### Làm yếu đi (warning)
- [ ] Gap quá mỏng / inside.
- [ ] News lớn đang chi phối.
- [ ] Giá đã xuyên CE nhiều lần không phản ứng.
- [ ] Mức HTF mạnh hơn (NWOG, weekly level) nằm ngay sát.

### Nâng cao — NY Midnight Open Price Theory và mối liên hệ với NDOG

ICT dùng một mốc riêng gọi là **Midnight Open (MO)** — giá mở cửa tại đúng **00:00 ET** — như đường tham chiếu bias cho toàn bộ phần còn lại của ngày: **giá đang giao dịch TRÊN Midnight Open thì thiên hướng của ngày là bullish; giá đang giao dịch DƯỚI Midnight Open thì thiên hướng là bearish.** Đây không phải là NDOG, nhưng hai mốc này gắn rất chặt với nhau về mặt thời gian và giá trị: NDOG là khoảng gap giữa Prior Day Close (~16:00–16:15 ET) và Reopen (~18:00 ET), còn Midnight Open nằm ngay bên trong (hoặc rất sát) hành trình giá diễn ra sau đó — nói cách khác, **NDOG straddle (bao trùm/nằm sát) quanh đúng mốc Midnight Open** vì cả hai đều hình thành trong cùng một cửa sổ "đầu ngày mới" theo giờ ET.

![[NDOG-Advanced-MidnightOpenTheory.svg]]
*Giá trên đường Midnight Open (00:00 ET) mang thiên hướng bullish trong ngày; giá dưới mang thiên hướng bearish. NDOG luôn straddle sát mốc này vì cả hai đều hình thành quanh cùng một khung giờ đầu ngày.*

Cách một trader dùng cặp mốc này làm bộ lọc hướng trong ngày:
1. **Xác định vị trí giá so với CE của NDOG** (premium hay discount — xem [[27 - Premium Discount]]) và **vị trí giá so với Midnight Open** (trên hay dưới) gần như cùng lúc.
2. **Khi hai tín hiệu đồng thuận** (vd: giá vừa ở discount của NDOG vừa đang trên Midnight Open sau khi retest) → độ tin cậy của [[12 - Daily Bias]] hướng bullish tăng lên, vì hai mốc độc lập cùng chỉ một hướng.
3. **Khi hai tín hiệu mâu thuẫn** (vd: giá ở discount của NDOG nhưng vẫn nằm dưới Midnight Open) → nên coi bias là chưa rõ ràng, cần thêm [[21 - Market Structure Shift]] LTF xác nhận trước khi vào lệnh, thay vì ép theo một mốc duy nhất.
4. Midnight Open cũng hoạt động như một **mốc support/resistance intraday riêng** — giá có xu hướng retrace về đây trong phiên NY trước khi tiếp tục — tương tự cách CE của NDOG hút giá về, nhưng đây là hai mốc tách biệt, không nên gộp làm một.

> [!info] Phân biệt rõ hai mốc
> **NDOG** = khoảng gap giữa hai mức giá (Prior Close ↔ Reopen), có **độ rộng** và một **CE ở giữa**. **Midnight Open** = một **đường giá đơn** tại đúng 00:00 ET, không có độ rộng. Chúng gần nhau về thời gian và thường được dùng cùng lúc, nhưng là hai công cụ khác nhau — NDOG cho vùng/target, Midnight Open cho bộ lọc hướng nhanh. Số liệu thắng/thua khi kết hợp cả hai **cần backtest xác nhận** trên từng thị trường (NQ1/NDX khác EURUSD/GBPUSD/XAUUSD).

### Nâng cao — Consequent Encroachment (50%) của NDOG như một mốc mean-threshold/target

CE (50% của NDOG) không chỉ là "đường ở giữa cho đẹp" — nó hoạt động như một **nam châm giá (mean-threshold)** đúng theo logic ICT vẫn dùng cho [[10 - Consequent Encroachment (Mean Threshold)]] khi áp cho FVG: thị trường có xu hướng quay lại lấp một nửa vùng inefficiency trước khi quyết định tiếp diễn hay đảo chiều thật sự. Với NDOG, CE là nơi giá "cân bằng lại" giữa Prior Day Close và Reopen sau khi gap hình thành qua giờ nghỉ bảo trì.

![[NDOG-Advanced-ConsequentEncroachment.svg]]
*CE (50% của NDOG) hoạt động như nam châm hút giá từ cả premium lẫn discount của ngày; giá trên CE = premium (ưu tiên Short theo bias bearish), giá dưới CE = discount (ưu tiên Long theo bias bullish).*

Cách CE của NDOG tương tác với khung Premium/Discount trong ngày:
- **Giá trên CE = premium của ngày** — vùng ưu tiên tìm Short nếu [[12 - Daily Bias]] là bearish; giá dưới CE = **discount của ngày** — vùng ưu tiên tìm Long nếu bias bullish. Đây là cách dùng CE của NDOG y hệt cách dùng CE của một FVG lớn để định vị premium/discount cục bộ, chỉ khác quy mô thời gian (cả ngày thay vì một cú swing).
- **CE là TARGET/mốc chờ phản ứng, không phải trigger entry.** Giá đạt CE chỉ xác nhận "đã về tới vùng cân bằng" — vẫn cần [[20 - Liquidity Sweep]] + [[21 - Market Structure Shift]] LTF trước khi coi đó là một setup hợp lệ, giống hệt nguyên tắc đã nêu ở mục 3 và mục 5 của note này.
- Khi **CE của NDOG trùng với CE của một [[24 - New Week Opening Gap]]** đang mở, đây là một dạng confluence mean-threshold hai tầng (ngày + tuần) — độ tin cậy của target cao hơn, nhưng theo nguyên tắc đã nêu ở phần so sánh NDOG/NWOG, vẫn ưu tiên NWOG khi hai mốc mâu thuẫn về hướng.

> [!tip] Fractal với NWOG
> Về bản chất, **một tuần giao dịch chứa nhiều NDOG lồng bên trong nó** — mỗi NDOG là một "phiên bản thu nhỏ theo ngày" của cùng cơ chế gap-qua-thời-gian tạo ra [[24 - New Week Opening Gap]] ở quy mô tuần. CE của từng NDOG trong tuần có thể được nhìn như các mốc mean-threshold nhỏ nằm bên trong mốc mean-threshold lớn hơn là CE của NWOG — một quan hệ fractal giữa hai khung thời gian, không phải hai công cụ độc lập.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Bối cảnh & bias
1. Vẽ **1–3 NDOG gần nhất** với CE của từng cái; vẽ thêm [[24 - New Week Opening Gap]] để so chiếu.
2. Xác định giá đang ở **premium hay discount** so với CE của NDOG hiện hành (xem [[27 - Premium Discount]]).
3. Tìm **NDOG chưa fill** gần nhất → đây là **draw on liquidity** tiềm năng trong ngày.
4. Ghép với [[12 - Daily Bias]]: bias hướng về NDOG nào? Có trùng draw của NWOG không?

### H1 / M15 — Lập kế hoạch & vùng chờ
1. Khoanh vùng NDOG/CE mà giá có khả năng tiếp cận.
2. Tìm confluence: [[Order Block]], [[Fair Value Gap]], [[20 - Liquidity Sweep]] gần NDOG.
3. Chờ giá tiếp cận vùng trong [[18 - Kill Zones]].

### M5 / M1 — Xác nhận & entry
1. Quan sát phản ứng tại NDOG/CE: rejection, [[20 - Liquidity Sweep]] quét cạnh gap.
2. Chờ [[21 - Market Structure Shift]] (MSS) xác nhận đảo chiều / tiếp diễn.
3. Tinh chỉnh entry vào FVG/OB hình thành sau MSS, SL ngoài cạnh NDOG hoặc swing gần.

```text
[LONG SETUP — phản ứng tại NDOG discount]
- HTF: giá ở discount, dưới CE của NDOG; bias bullish, draw lên NDOG phía trên (unfilled)
- Vùng: giá quét sellside / chạm cạnh dưới NDOG hoặc CE
- LTF: M5 MSS lên + FVG bullish hình thành
- Entry: ____   SL: dưới cạnh dưới NDOG / swing low [level]
- TP1: CE NDOG [level]   TP2: cạnh trên / NDOG unfilled phía trên [level]
- RR dự kiến: ____
```

```text
[SHORT SETUP — phản ứng tại NDOG premium]
- HTF: giá ở premium, trên CE của NDOG; bias bearish, draw xuống NDOG phía dưới (unfilled)
- Vùng: giá quét buyside / chạm cạnh trên NDOG hoặc CE
- LTF: M5 MSS xuống + FVG bearish hình thành
- Entry: ____   SL: trên cạnh trên NDOG / swing high [level]
- TP1: CE NDOG [level]   TP2: cạnh dưới / NDOG unfilled phía dưới [level]
- RR dự kiến: ____
```

> [!warning]
> NDOG là **mốc tham chiếu**, không phải tín hiệu entry. Tuyệt đối **không vào lệnh chỉ vì giá chạm CE/cạnh gap** — phải có xác nhận LTF (MSS + FVG/OB) trong kill zone. Chạm mức mà không xác nhận = chưa có lệnh.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup hợp lệ (✓)
- [ ] Giá tiếp cận NDOG/CE đúng phía bias (discount → long, premium → short).
- [ ] Có [[20 - Liquidity Sweep]] hoặc rejection rõ tại cạnh/CE.
- [ ] [[21 - Market Structure Shift]] LTF xác nhận.
- [ ] Có entry array (FVG/OB) để vào, SL rõ ràng ngoài cạnh NDOG.
- [ ] Tiếp cận trong [[18 - Kill Zones]].

### Setup bị vô hiệu (✗)
- [ ] Giá đóng nến **xuyên thẳng qua CE và cạnh đối diện** không phản ứng → mốc bị vô hiệu cho hướng đó.
- [ ] Không có MSS xác nhận sau khi chạm vùng.
- [ ] Tiếp cận lúc thanh khoản thấp / ngoài kill zone.
- [ ] News lớn override toàn bộ.

| Tiêu chí | Giữ kế hoạch (hợp lệ) | Hủy kế hoạch (vô hiệu) |
|---|---|---|
| Phản ứng tại CE | Rejection / sweep rõ | Đóng nến xuyên qua, không phản ứng |
| MSS LTF | Có MSS đúng hướng | Không có MSS |
| Vị trí premium/discount | Đúng phía bias | Sai phía / mâu thuẫn bias |
| Thời điểm | Trong kill zone | Ngoài kill zone / news |

> [!note]
> Một NDOG "bị xuyên qua không phản ứng" **không bị xóa khỏi chart** — nó vẫn là SR lịch sử và có thể phản ứng ở lần test sau. "Vô hiệu" ở đây nghĩa là **vô hiệu cho kế hoạch trade hiện tại**, không phải xóa mốc.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[NDOG-Example-Correct.svg]]

**Mô tả:**
- Ngày mở **gap down** (Reopen < Prior Close); giá đầu phiên nằm ở discount dưới CE.
- Bias bullish HTF, draw on liquidity là NDOG **unfilled** phía trên.
- Trong NY KZ, giá quét sellside và phản ứng tại cạnh dưới NDOG, M5 cho MSS lên + FVG bullish.

**Vì sao đây là ví dụ tốt:**
- Mốc NDOG được vẽ đúng từ Prior Close (~16:15 ET) → Reopen (~18:00 ET), có CE 50%.
- Entry chỉ thực hiện **sau xác nhận** (sweep + MSS + FVG), không phải chỉ vì chạm CE.
- Mục tiêu hợp lý: CE rồi tới NDOG unfilled phía trên (draw on liquidity).
- Tiếp cận trong kill zone, đúng phía premium/discount.

### Ví dụ sai
![[NDOG-Example-Wrong.svg]]

**Mô tả:**
- Trader vào long ngay khi giá **vừa chạm CE** mà không chờ phản ứng/MSS.
- Giá đóng nến xuyên thẳng qua CE và cạnh đối diện của NDOG.
- Lệnh dính SL khi mốc bị "xuyên qua không phản ứng".

**Bài học:**
- NDOG/CE là **mốc chờ**, không phải lệnh tự động — luôn cần xác nhận LTF.
- Vào lệnh ngoài kill zone / lúc news làm tăng rủi ro mốc bị bỏ qua.
- Đặt SL ngoài cạnh NDOG, không quá sát CE.
- Phải xác định trước hướng bias (premium/discount); vào ngược bias là sai.

### Giải phẫu NDOG
![[NDOG-Anatomy.svg]]

**Mô tả:** Sơ đồ chú thích Prior Day Close, giờ nghỉ bảo trì 17:00–18:00 ET, Reopen, NDOG range, CE 50%, và cách giữ 1–3 NDOG gần nhất làm mốc tham chiếu (so với 3–5 NWOG của tuần).

---

## 7. Entry model liên quan

- [[ICT 2022 Model]] — sweep → MSS → FVG entry, với NDOG/CE làm vùng POI/draw.
- [[20 - Liquidity Sweep]] — quét cạnh NDOG trước khi đảo chiều.
- [[21 - Market Structure Shift]] — xác nhận đảo chiều LTF tại NDOG.
- [[Fair Value Gap]] — entry array sau MSS.
- [[Order Block]] — confluence tại cạnh/CE NDOG.
- [[10 - Consequent Encroachment (Mean Threshold)]] — CE là mức phản ứng chính.
- [[24 - New Week Opening Gap]] — mốc tuần; confluence khi trùng NDOG.
- [[27 - Premium Discount]] / [[12 - Daily Bias]] — xác định hướng vào lệnh.

```text
[Chuỗi triển khai chuẩn quanh NDOG]
1. HTF: vẽ 1–3 NDOG + CE (và NWOG) → xác định draw (NDOG unfilled) & premium/discount
2. Chờ giá tiếp cận NDOG/CE đúng phía bias, trong kill zone
3. LTF: Liquidity Sweep tại cạnh/CE → Market Structure Shift đúng hướng
4. Entry vào FVG/OB hình thành sau MSS; SL ngoài cạnh NDOG
5. TP1 = CE; TP2 = cạnh đối diện / NDOG unfilled kế tiếp (hoặc NWOG nếu trùng)
```

> [!note]
> NDOG hoạt động mạnh nhất khi **đóng vai trò draw/POI trong khung của [[ICT 2022 Model]]**, không dùng riêng lẻ. CE là điểm phản ứng then chốt. Khi NDOG trùng [[24 - New Week Opening Gap]], ưu tiên xem đó là vùng confluence sức nặng cao.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning]
> Không có đủ mục A + B → **không có lệnh**. NDOG là mốc chờ, kiên nhẫn là kỷ luật.

### A. Context
- [ ] Đã vẽ 1–3 NDOG gần nhất + CE từng cái (và đối chiếu NWOG).
- [ ] Xác định giá đang premium hay discount so với CE.
- [ ] Tìm được NDOG unfilled = draw on liquidity của ngày.
- [ ] Bias HTF ([[12 - Daily Bias]]) rõ ràng và NHẤT QUÁN với hướng định trade.

### B. Execution
- [ ] Giá tiếp cận NDOG/CE trong [[18 - Kill Zones]].
- [ ] Có [[20 - Liquidity Sweep]] / rejection tại vùng.
- [ ] Có [[21 - Market Structure Shift]] LTF xác nhận.
- [ ] Có entry array (FVG/OB), SL ngoài cạnh NDOG, RR ≥ ngưỡng tối thiểu.
- [ ] Risk ≤ 0.5% theo khung rủi ro.

### C. "Không có lệnh" khi
- [ ] Giá xuyên CE/cạnh không phản ứng.
- [ ] Không có MSS xác nhận.
- [ ] Ngoài kill zone / đang có news lớn.
- [ ] Vào ngược bias / gap quá mỏng.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Vào lệnh chỉ vì chạm CE | Entry ngay khi giá touch CE, không xác nhận | NDOG là mốc chờ, không phải tín hiệu; dễ bị xuyên qua | Luôn chờ sweep + MSS + FVG trước khi vào |
| Vẽ sai mốc thời gian | Dùng giờ địa phương thay vì ET; lấy nhầm close/open | Sai cả range & CE → mọi phân tích lệch | Cố định múi giờ ET: prior close ~16:00–16:15, reopen ~18:00 |
| Xóa NDOG đã fill | Chỉ giữ gap chưa fill | Gap đã fill vẫn là SR | Giữ 1–3 NDOG gần nhất bất kể đã fill |
| Bỏ qua premium/discount | Long ở premium / short ở discount | Vào ngược fair value, xác suất thấp | Luôn chiếu vị trí giá so với CE trước khi quyết định hướng |
| Quá nhiều NDOG trên chart | Vẽ chồng chục gap ngày, rối mắt | Mất trọng tâm, nhiễu | Giữ tối đa 1–3 cái gần nhất + NWOG |
| Coi NDOG luôn fill ngay trong ngày | Ép giá phải quay về gap cùng ngày | Có thể mất nhiều ngày; ép lệnh sai timing | Dùng NDOG làm draw, không cưỡng ép timing |
| Bỏ qua confluence với NWOG | Trade NDOG mà không nhìn mốc tuần | NWOG sức nặng lớn hơn, dễ ngược mốc mạnh | Đối chiếu NWOG; ưu tiên vùng trùng nhau |

---

## 10. Câu hỏi tự kiểm tra
- Prior Day Close và Reopen lấy vào những mốc giờ ET nào? Giờ nghỉ bảo trì là khi nào?
- CE của NDOG tính thế nào và vì sao nó quan trọng hơn các cạnh?
- NDOG khác [[24 - New Week Opening Gap]] ở điểm nào? Khi nào hai cái này chồng nhau?
- Vì sao gap đã fill vẫn nên giữ trên chart?
- Làm sao dùng NDOG để xác định premium/discount của ngày?
- "NDOG unfilled = draw on liquidity" nghĩa là gì trong thực chiến?
- Điều kiện tối thiểu để biến NDOG từ mốc tham chiếu thành setup hợp lệ?

---

## 11. Flashcards / Active Recall
- **Q1:** NDOG được tạo bởi hai mức giá nào, vào giờ ET nào?
  → A1: Prior Day Close (regular session close ~16:00–16:15 ET) và Reopen (~18:00 ET, sau giờ nghỉ bảo trì 17:00–18:00 ET).
- **Q2:** Mức quan trọng nhất bên trong NDOG là gì?
  → A2: CE (Consequent Encroachment) = 50% của range; là nam châm và SR chính.
- **Q3:** Nên giữ bao nhiêu NDOG trên chart và có xóa khi đã fill không?
  → A3: Giữ 1–3 cái gần nhất; không xóa khi đã fill (vẫn là SR).
- **Q4:** NDOG khác NWOG thế nào?
  → A4: NDOG là phiên bản theo NGÀY (prior close → reopen, sức nặng nhỏ, giữ 1–3); NWOG là phiên bản theo TUẦN (Fri → Sun, sức nặng lớn, giữ 3–5). Khi trùng nhau → confluence mạnh, ưu tiên NWOG.
- **Q5:** Vì sao daily opening gap lại có ý nghĩa với ICT?
  → A5: Giờ nghỉ bảo trì hằng ngày khiến thị trường không giao dịch ~1¾ giờ → inefficiency không thể fill → thị trường thường quay lại balance; là fair value & draw on liquidity.
- **Q6:** Điều kiện để vào lệnh tại NDOG là gì?
  → A6: Đúng phía premium/discount + tiếp cận trong kill zone + sweep/rejection + MSS LTF + entry array (FVG/OB) với SL ngoài cạnh NDOG.

---

## 12. Lesson Learned
> [!example] Ghi nhận khi áp dụng thực tế
> - Bối cảnh: ____
> - NDOG dùng (Prior Close / Reopen / CE): [level] / [level] / [level]
> - Có trùng NWOG không: ____
> - Phản ứng quan sát được: ____
> - Kết quả (R-multiple): ____
> - Điều làm đúng: ____
> - Điều cần sửa: ____
> - Liên kết tới [[Mistake - ...]] nếu có: ____

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm (1–5) | Ghi chú |
|---|---|---|
| Hiểu định nghĩa & cách vẽ | ____ | |
| Phân biệt NDOG vs NWOG | ____ | |
| Dùng CE làm SR/bias | ____ | |
| Nhận diện draw (unfilled) | ____ | |
| Tích hợp vào ICT 2022 Model | ____ | |
| Kỷ luật chờ xác nhận | ____ | |

**Kế hoạch ôn tập:**
- [ ] Backtest 10–20 lần giá tiếp cận NDOG/CE trên NQ1/NAS100 & EURUSD.
- [ ] Mỗi ngày: vẽ NDOG mới lúc reopen, ghi lại phản ứng tới CE trong phiên.
- [ ] So sánh win rate khi NDOG trùng NWOG vs đứng riêng.
- [ ] Đối chiếu với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]].
- [ ] Review lại note này sau 2 tuần, cập nhật `confidence` & `last_reviewed`.

---

## Best Practices

> [!success] Nguyên tắc vàng
> **NDOG có sức nặng thật nhất trên futures/index (NQ1, NAS100) — nơi giờ nghỉ bảo trì tạo ra một inefficiency có thật; trên forex 24 giờ (EURUSD, GBPUSD, XAUUSD), "NDOG" chỉ là một xấp xỉ quanh Midnight Open, không phải một gap đúng nghĩa.** Nhầm lẫn hai trường hợp này là nguồn sai lầm phổ biến nhất khi áp dụng NDOG trên danh mục thị trường hỗn hợp mà bạn đang trade.

1. **Phân biệt rõ NDOG futures thật với NDOG-xấp-xỉ trên forex.** Trên NQ1/NAS100 (CME futures), giờ nghỉ bảo trì ~17:00–18:00 ET tạo một khoảng thị trường **thực sự không giao dịch**, nên NDOG là một inefficiency có thật với sức nặng đáng tin. Trên EURUSD/GBPUSD/XAUUSD (giao dịch gần như 24 giờ), không có halt thật — chênh lệch giá quanh nửa đêm chỉ là một **xấp xỉ** dựa trên chênh lệch giá quanh Midnight Open, thường rất mỏng và kém tin cậy hơn nhiều. Ghi trường `ndog_instrument_type: futures / forex-approx` cho mỗi lần dùng NDOG trong journal để tách riêng thống kê hai nhóm — đừng gộp chung win-rate của NQ1 và EURUSD dưới cùng một nhãn "NDOG".

2. **Trên forex, ưu tiên Midnight Open + Daily Bias hơn là cố vẽ một NDOG "cho có".** Nếu chênh lệch giá quanh 00:00 ET trên EURUSD/GBPUSD/XAUUSD quá mỏng để tạo thành một vùng có ý nghĩa, đừng ép vẽ NDOG — thay vào đó dùng trực tiếp vị trí giá so với đường Midnight Open làm bộ lọc hướng (xem mục Nâng cao ở trên). Ghi `midnight_open_side: above/below` mỗi ngày cho các cặp forex, thay vì cố gắn `ndog_range` cho một gap gần như không tồn tại.

3. **Dùng CE của NDOG làm target/mốc chờ phản ứng, không bao giờ làm trigger entry độc lập.** Giá chạm CE chỉ xác nhận "đã về vùng cân bằng" — luôn cần [[20 - Liquidity Sweep]] + [[21 - Market Structure Shift]] LTF trong [[18 - Kill Zones]] trước khi coi đó là setup hợp lệ. Ghi `ce_reaction: yes/no` cho từng lần giá tiếp cận CE để đo tỉ lệ phản ứng thật so với xuyên qua không phản ứng.

4. **Luôn ghép NDOG với [[12 - Daily Bias]] trước khi diễn giải hướng.** Một NDOG đứng một mình không nói lên gì về hướng đi — nó chỉ là một vùng tham chiếu. Phải trả lời trước: bias HTF của ngày là gì, giá đang premium hay discount theo [[27 - Premium Discount]], rồi mới dùng NDOG/CE để tìm điểm vào lệnh đúng phía. Vào lệnh tại CE mà ngược bias là lỗi kinh điển (xem mục 9 và ví dụ sai ở mục 6).

5. **Giữ khung fractal rõ ràng giữa NDOG và [[24 - New Week Opening Gap]].** NDOG là bản sao theo-ngày của NWOG; nhiều NDOG trong một tuần lồng bên trong khung của NWOG tuần đó. Khi NDOG và NWOG trùng/chồng nhau, đó là confluence hai tầng thời gian — ưu tiên NWOG khi hai mốc mâu thuẫn về hướng, nhưng ghi nhận confluence này làm tăng độ tin cậy khi chúng đồng thuận.

6. **Không xóa NDOG đã fill, và không ép giá phải "trả nợ" gap trong cùng ngày.** Gap đã fill vẫn là support/resistance lịch sử; NDOG unfilled là draw on liquidity nhưng có thể mất nhiều phiên mới được lấp. Giữ 1–3 NDOG gần nhất trên chart bất kể trạng thái fill.

7. **Trên các phiên thiếu thanh khoản hoặc có news lớn, hạ trọng số cho mọi mốc NDOG/Midnight Open.** Cả hai công cụ đều dựa trên hành vi "giá quay lại cân bằng" trong điều kiện thị trường bình thường; một cú news mạnh có thể xóa sạch logic đó trong vài phút. Kiểm tra lịch kinh tế trước khi đặt kỳ vọng vào phản ứng tại CE.

8. **Backtest riêng NQ1/NDX và riêng từng cặp forex trước khi tin vào con số cụ thể nào.** Vì sức nặng của NDOG khác nhau rõ rệt giữa futures và forex, mọi phát biểu kiểu "NDOG fill trong X% thời gian" hay "CE phản ứng Y% số lần" **cần backtest xác nhận** theo từng nhóm thị trường riêng biệt — không dùng chung một con số cho cả bốn thị trường bạn đang trade (NQ1/NDX, EURUSD, GBPUSD, XAUUSD). Đối chiếu kết quả với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]] sau mỗi đợt review.
