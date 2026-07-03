---
type: ict-concept
concept: New Week Opening Gap
aliases:
  - New Week Opening Gap
  - NWOG
  - Weekend Gap
tags:
  - trading/ict/concept
  - trading/study
  - "#NWOG"
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
last_reviewed:
created: 2026-06-24
updated: 2026-07-03
related_concepts:
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[Fair Value Gap]]"
  - "[[12 - Daily Bias]]"
  - "[[27 - Premium Discount]]"
  - "[[18 - Kill Zones]]"
prerequisites:
  - "[[Fair Value Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
common_mistakes: []
---

# New Week Opening Gap

> [!summary] Tóm tắt 1 câu
> **New Week Opening Gap (NWOG) là khoảng gap giá giữa giá đóng cửa Thứ Sáu (settlement, 16:59–17:00 ET) và giá mở cửa Chủ Nhật (Sunday open / futures reopen 17:00–18:00 ET); ICT coi nó là một mốc tham chiếu fair value và draw on liquidity quan trọng nhất cho cả tuần, với đường giữa (Consequent Encroachment / CE 50%) đóng vai trò nam châm và support/resistance.**

> [!important] Nguyên tắc cốt lõi
> - **CE (50% của NWOG) là mốc quan trọng nhất**, không phải các cạnh gap. Giá liên tục bị hút về CE rồi phản ứng tại đó.
> - **Giữ 3–5 NWOG gần nhất trên chart** như các đường tham chiếu cố định. Đừng xóa khi gap đã được "fill" — gap đã fill vẫn là support/resistance.
> - NWOG là một **vùng fair value** (không phải FVG/imbalance kiểu thông thường) — nó tồn tại vì cuối tuần thị trường đóng cửa, tạo ra inefficiency không thể giao dịch.
> - Dùng NWOG để trả lời: **giá đang ở premium hay discount của tuần?** và **đâu là draw on liquidity tự nhiên?**

---

## 1. Định nghĩa

### Khái niệm
**New Week Opening Gap (NWOG)** là khoảng cách giá giữa:
- **Cạnh trên/dưới 1 = Friday Close (Settlement)**: giá đóng cửa phiên Thứ Sáu, lấy quanh **16:59–17:00 ET** (giờ settlement của futures CME).
- **Cạnh còn lại = Sunday Open (Reopen)**: giá mở cửa khi thị trường futures mở lại vào **Chủ Nhật ~17:00–18:00 ET** (NY index futures thường reopen 18:00 ET).

Khoảng giữa hai mức giá này là **gap cuối tuần** — vùng giá mà thị trường không hề giao dịch qua (no trading over the weekend), do đó là một **inefficiency / fair value reference** mặc định cho tuần mới.

### Bản chất
- NWOG không sinh ra từ một cú displacement trong phiên như FVG, mà sinh ra từ **sự ngắt quãng thời gian** (thị trường đóng cửa cuối tuần). Đây là một dạng **fair value gap theo thời gian**, không phải theo cấu trúc nến.
- Vì giá "nhảy" từ Friday Close sang Sunday Open mà không qua giao dịch, vùng ở giữa giống như một **liquidity void / vùng fair value chưa được kiểm định** — thị trường có xu hướng quay lại để "balance" lại vùng này.
- ICT lập luận rằng các **Interbank / market maker** dùng các mốc này như mốc tham chiếu giá hợp lý, nên giá thường gravitate (bị hút) về NWOG, đặc biệt là về CE.

### Cách vẽ gap + CE 50%
1. Xác định **Friday Close** (16:59–17:00 ET): vẽ một đường ngang tại mức giá đóng cửa cuối cùng của Thứ Sáu.
2. Xác định **Sunday Open** (17:00–18:00 ET): vẽ một đường ngang tại mức giá mở cửa đầu tiên của Chủ Nhật.
3. Vùng giữa hai đường = **NWOG range** (tô màu / box).
4. Tính **CE = (Friday Close + Sunday Open) / 2** → vẽ đường giữa. **Đây là mức quan trọng nhất.** (Xem [[10 - Consequent Encroachment (Mean Threshold)]].)
5. Đặt tên & màu cố định, **giữ lại 3–5 NWOG gần nhất** trên chart như mốc tham chiếu.

```text
Friday Close (17:00 ET) ── cạnh trên ──┐
                                       │  NWOG range
            CE (50%) ───────●──────────│  ← mức nam châm / SR chính
                                       │
Sunday Open (18:00 ET) ── cạnh dưới ───┘
```

### So sánh với NDOG (New Day Opening Gap)
- **NDOG = New Day Opening Gap**: gap giữa giá đóng phiên ngày hôm trước (~**16:15 ET**, regular session close của index futures) và giá mở cửa phiên reopen (~**18:00 ET**) trong **các ngày trong tuần**.
- NDOG là phiên bản **ngày** của NWOG (intraday/daily reference), NWOG là phiên bản **tuần** (lớn hơn, mạnh hơn, ưu tiên cao hơn).
- Khi NWOG và NDOG trùng/chồng nhau → vùng đó càng có sức nặng tham chiếu.

| Thuộc tính | NWOG | NDOG |
|---|---|---|
| Khoảng thời gian | Cuối tuần (Fri → Sun) | Trong ngày (prev close → reopen) |
| Mốc đóng cửa | Friday ~16:59–17:00 ET | ~16:15 ET ngày trước |
| Mốc mở cửa | Sunday ~17:00–18:00 ET | ~18:00 ET |
| Sức nặng | Cao (tham chiếu cả tuần) | Trung bình (tham chiếu ngày) |
| Số lượng giữ trên chart | 3–5 cái gần nhất | 1–3 cái gần nhất |

### Mục đích trong ICT
- Cung cấp **mốc tham chiếu fair value cố định** cho cả tuần.
- Là một **draw on liquidity** tự nhiên: giá thường hướng về NWOG/CE chưa được fill.
- Làm **support/resistance** và xác định bias premium/discount của tuần (xem [[27 - Premium Discount]], [[12 - Daily Bias]]).

### Vì sao quan trọng
- Cuối tuần thị trường **không giao dịch** → inefficiency tồn tại mà không thể bị fill trong khoảng thời gian đó → tạo ra "nợ kỹ thuật" mà thị trường thường quay lại trả.
- Là mốc **khách quan, không vẽ tay mơ hồ** — chỉ cần Friday Close và Sunday Open, ai vẽ cũng giống nhau → giảm chủ quan.

### Nó giúp trả lời câu hỏi nào trên chart?
- Giá tuần này đang ở **premium hay discount** so với CE của NWOG?
- **Draw on liquidity** tự nhiên của tuần nằm ở đâu (NWOG nào chưa fill)?
- Đâu là **support/resistance** đáng tin để chờ phản ứng vào kill zone?
- Khi giá tiếp cận NWOG/CE, nên **kỳ vọng phản ứng** (đảo chiều/chậm lại) thay vì đu theo đà.

### NWOG không phải là gì
- **Không phải** là tín hiệu entry trực tiếp — nó là **mốc tham chiếu/draw**, cần xác nhận tại đó.
- **Không phải** FVG nội phiên — nó sinh từ ngắt quãng thời gian, không từ displacement.
- **Không phải** mục tiêu "chắc chắn fill ngay tuần này" — có thể mất nhiều tuần mới quay lại; gap đã fill vẫn là SR.
- **Không phải** thứ để xóa khi đã được chạm — giữ lại làm mốc lịch sử.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái

| Trạng thái | Mô tả | Hàm ý giao dịch |
|---|---|---|
| **Gap up** | Sunday Open > Friday Close | Tuần mở trong premium so với Fri; CE phía dưới có thể là draw |
| **Gap down** | Sunday Open < Friday Close | Tuần mở trong discount so với Fri; CE phía trên có thể là draw |
| **Inside / no gap** | Sunday Open ≈ Friday Close (gap rất nhỏ) | NWOG mỏng, ít sức nặng; ưu tiên NWOG cũ hơn |
| **Filled NWOG** | Giá đã trade lại qua toàn bộ range gap | Gap đã "trả nợ"; vẫn là SR, CE vẫn phản ứng |
| **Unfilled NWOG** | Giá chưa quay lại chạm/lấp gap | Là **draw on liquidity** mạnh — mục tiêu tiềm năng |

### Khi nào giá trị cao? (checklist)
- [ ] Giá đang gần hoặc đang hướng về một **NWOG chưa fill** (unfilled).
- [ ] CE của NWOG trùng với một PD-array khác ([[Order Block]], [[Fair Value Gap]], [[03 - Balanced Price Range]]).
- [ ] NWOG nằm tại biên premium/discount của [[12 - Dealing Range]] tuần.
- [ ] Có **confluence** với [[19 - Liquidity]] (buyside/sellside) ngay cạnh NWOG.
- [ ] Phản ứng được kỳ vọng trong [[18 - Kill Zones]] (London/NY).

### Khi nào bỏ qua? (checklist)
- [ ] Gap quá nhỏ/inside (gần như không có gap) → ít ý nghĩa.
- [ ] Giá đang ở rất xa NWOG và không có draw rõ ràng về nó.
- [ ] Tin tức lớn (high-impact news) đang làm giá chạy mạnh, bỏ qua mọi mốc fair value.
- [ ] NWOG bị "che" bởi một mức HTF mạnh hơn (weekly OB, monthly level) — ưu tiên mức mạnh hơn.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Hai mốc giá rõ ràng**: Friday Close (17:00 ET) và Sunday Open (18:00 ET).
2. **Khoảng trống thời gian** giữa hai mốc (không có nến cuối tuần).
3. **Đường CE 50%** nằm chính giữa range.
4. Giá lịch sử cho thấy **phản ứng tại CE / các cạnh** (đảo chiều, từ chối, chậm lại).
5. NWOG chưa fill tạo thành **mục tiêu hút giá** (draw on liquidity).

### Ma trận nhận diện

| Yếu tố | NWOG hợp lệ & đáng tin | NWOG yếu / bỏ qua |
|---|---|---|
| Độ rộng gap | Đủ rộng, dễ thấy | Quá mỏng / inside |
| Vị trí trong dealing range | Tại biên premium/discount | Giữa range, mờ nhạt |
| Confluence PD-array | Trùng OB/FVG/CBDR | Đứng một mình |
| Trạng thái | Unfilled (draw mạnh) hoặc CE chưa test | Đã fill nhiều lần, không phản ứng |
| Phản ứng lịch sử | Có rejection rõ tại CE/cạnh | Giá xuyên qua không phản ứng |
| Kill zone | Tiếp cận trong London/NY KZ | Tiếp cận lúc thanh khoản thấp |

### Điều kiện bắt buộc (must-have)
- [ ] Xác định đúng **Friday Close (16:59–17:00 ET)** và **Sunday Open (17:00–18:00 ET)** theo đúng múi giờ ET.
- [ ] Vẽ đúng **CE = 50%** của range.
- [ ] Đặt trong bối cảnh [[12 - Daily Bias]] / [[27 - Premium Discount]] của tuần.

### Tăng xác suất (nice-to-have)
- [ ] Confluence với PD-array khác (OB, FVG, CBDR — xem [[08 - Central Bank Dealers Range]]).
- [ ] Trùng với [[19 - Liquidity]] pool gần đó.
- [ ] Tiếp cận trong [[18 - Kill Zones]].
- [ ] NWOG còn **unfilled** (draw mạnh hơn).

### Làm yếu đi (warning)
- [ ] Gap quá mỏng / inside.
- [ ] News lớn đang chi phối.
- [ ] Giá đã xuyên CE nhiều lần không phản ứng.
- [ ] Mức HTF mạnh hơn nằm ngay sát.

### Nâng cao — True Week Open và vai trò của nến Chủ Nhật (Sunday candle)

Một điểm gây nhầm lẫn thường gặp: **"Sunday Open" dùng để vẽ cạnh NWOG không phải lúc nào cũng trùng với cái mà một số tài liệu ICT gọi là "True Week Open"**. Cạnh NWOG luôn là **giá mở cửa thực tế khi futures reopen** (~17:00–18:00 ET Chủ Nhật) — đây là mốc khách quan, ai cũng vẽ giống nhau vì nó là điểm dữ liệu có thật đầu tiên của tuần. Trong khi đó, một số cách dạy ICT dùng thêm khái niệm **"true day open"/"true week open"** neo vào **00:00 (nửa đêm) giờ New York của Thứ 2** như một mốc tham chiếu bias bổ sung cho cấu trúc ngày/tuần "thật" theo múi giờ NY, tách biệt với giờ mở cửa sàn theo truyền thống.

![[NWOG-Advanced-TrueWeekOpen.svg]]
*So sánh giá mở cửa Chủ Nhật (literal reopen, dùng để vẽ cạnh NWOG) với mốc "true week open" ở một số cách dạy ICT (00:00 NY Thứ 2) — cùng với đặc điểm nến Chủ Nhật thường mỏng, nhiễu, spread rộng.*

Ba điều cần tách bạch khi làm việc với dữ liệu đầu tuần:
1. **Cạnh NWOG = Sunday Reopen literal.** Đây là mức giá đầu tiên khi thị trường giao dịch trở lại — dùng mức này để vẽ gap và tính CE, **không** thay bằng "true week open" nếu không chắc hai nguồn dữ liệu định nghĩa giống nhau.
2. **"True week open" là một tham chiếu bias bổ sung, không phải cạnh gap.** Nếu dùng khái niệm này, hãy rõ ràng nó phục vụ mục đích khác (đọc cấu trúc ngày/tuần theo giờ NY chuẩn), không lẫn vào công thức tính NWOG.
3. **Nến Chủ Nhật đầu tiên thường thanh khoản mỏng và dễ nhiễu** — spread rộng hơn bình thường, dễ có wick giả do thanh khoản thấp lúc vừa mở lại. Tránh vội kết luận cấu trúc (MSS, swing quan trọng) chỉ dựa vào 1–2 nến Chủ Nhật đầu tiên; nên chờ đến khi phiên Á/London Thứ 2 vào để dữ liệu đáng tin hơn.

> [!warning] So sánh & edge case
> Nếu broker/data feed của bạn hiển thị giờ mở cửa Chủ Nhật khác với "true week open" mà bạn quen dùng, **đừng trộn hai mốc**: giữ nguyên NWOG = Friday Close vs Sunday Reopen literal cho mọi tính toán CE/premium-discount, và chỉ dùng "true week open" như một ghi chú bias phụ nếu bạn có lý do cụ thể để tin tưởng cách định nghĩa đó. Sự nhất quán về mốc thời gian quan trọng hơn việc chọn "đúng" trường phái nào — cần backtest xác nhận trường phái nào phù hợp hơn với phong cách của bạn.

### Nâng cao — NWOG lồng NDOG: cấu trúc fractal đa khung theo tuần

NWOG và [[23 - New Day Opening Gap]] không phải hai công cụ tách biệt — chúng là **cùng một cơ chế (gap do ngắt quãng thời gian) lặp lại ở hai khung khác nhau**, theo đúng tinh thần fractal của ICT: mỗi tuần có **một NWOG** (Friday Close → Sunday Open) đóng vai trò khung lớn, và **bên trong tuần đó có 4–5 NDOG hằng ngày** (mỗi ngày một gap prior-close → reopen) nằm lồng bên trong phạm vi thời gian của NWOG đó.

![[NWOG-Advanced-NestedWithNDOG.svg]]
*Một tuần giao dịch với NWOG khung lớn bao trùm toàn bộ tuần, trong khi mỗi ngày (Thứ 2 đến Thứ 6) có một NDOG riêng nằm lồng bên trong — bias tuần đến từ NWOG, phản ứng trong ngày đến từ NDOG.*

Cách phối hợp hai khung này trong phân tích thực chiến:
- **NWOG (D1/H4) trả lời câu hỏi bias**: giá tuần này đang premium hay discount so với CE của NWOG? Draw on liquidity của cả tuần nằm ở NWOG nào (unfilled)?
- **NDOG (H1/M15) trả lời câu hỏi timing trong ngày**: hôm nay giá có khả năng phản ứng ở đâu, dựa trên gap ngày hôm nay?
- **Chỉ ưu tiên NDOG cùng hướng với bias NWOG.** Nếu NWOG cho bias bullish (giá ở discount tuần) nhưng một NDOG cụ thể lại gợi ý short ngắn hạn ngược hướng, NWOG (khung lớn hơn) có trọng số cao hơn — dùng NDOG đó thận trọng hơn hoặc chỉ như phản ứng ngắn hạn trong xu hướng lớn.
- **Khi một NDOG trong tuần trùng vị trí với CE hoặc cạnh của NWOG** → đây là điểm confluence đa khung mạnh nhất trong tuần: cùng lúc vừa là mốc tham chiếu ngày, vừa là mốc tham chiếu tuần.

> [!note] So sánh nhanh
> Tư duy giống hệt cách NWOG khác NDOG về sức nặng (xem bảng so sánh ở mục 1): NWOG là **khung tham chiếu cho toàn bộ tuần**, NDOG là **khung tham chiếu cho một ngày cụ thể bên trong tuần đó**. Luôn đọc NDOG trong bối cảnh của NWOG hiện hành, không đọc NDOG một mình như thể nó là mốc cao nhất.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Bối cảnh & bias
1. Vẽ **3–5 NWOG gần nhất** với CE của từng cái.
2. Xác định giá đang ở **premium hay discount** so với CE của NWOG hiện hành (xem [[27 - Premium Discount]]).
3. Tìm **NWOG chưa fill** gần nhất → đây là **draw on liquidity** tiềm năng cho tuần.
4. Ghép với [[12 - Daily Bias]]: bias hướng về NWOG nào?

### H1 / M15 — Lập kế hoạch & vùng chờ
1. Khoanh vùng NWOG/CE mà giá có khả năng tiếp cận.
2. Tìm confluence: [[Order Block]], [[Fair Value Gap]], [[20 - Liquidity Sweep]] gần NWOG.
3. Chờ giá tiếp cận vùng trong [[18 - Kill Zones]].

### M5 / M1 — Xác nhận & entry
1. Quan sát phản ứng tại NWOG/CE: rejection, [[20 - Liquidity Sweep]] quét cạnh gap.
2. Chờ [[21 - Market Structure Shift]] (MSS) xác nhận đảo chiều / tiếp diễn.
3. Tinh chỉnh entry vào FVG/OB hình thành sau MSS, SL ngoài cạnh NWOG hoặc swing gần.

```text
[LONG SETUP — phản ứng tại NWOG discount]
- HTF: giá ở discount, dưới CE của NWOG; bias bullish, draw lên NWOG phía trên (unfilled)
- Vùng: giá quét sellside / chạm cạnh dưới NWOG hoặc CE
- LTF: M5 MSS lên + FVG bullish hình thành
- Entry: ____   SL: dưới cạnh dưới NWOG / swing low [level]
- TP1: CE NWOG [level]   TP2: cạnh trên / NWOG unfilled phía trên [level]
- RR dự kiến: ____
```

```text
[SHORT SETUP — phản ứng tại NWOG premium]
- HTF: giá ở premium, trên CE của NWOG; bias bearish, draw xuống NWOG phía dưới (unfilled)
- Vùng: giá quét buyside / chạm cạnh trên NWOG hoặc CE
- LTF: M5 MSS xuống + FVG bearish hình thành
- Entry: ____   SL: trên cạnh trên NWOG / swing high [level]
- TP1: CE NWOG [level]   TP2: cạnh dưới / NWOG unfilled phía dưới [level]
- RR dự kiến: ____
```

> [!warning]
> NWOG là **mốc tham chiếu**, không phải tín hiệu entry. Tuyệt đối **không vào lệnh chỉ vì giá chạm CE/cạnh gap** — phải có xác nhận LTF (MSS + FVG/OB) trong kill zone. Chạm mức mà không xác nhận = chưa có lệnh.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup hợp lệ (✓)
- [ ] Giá tiếp cận NWOG/CE đúng phía bias (discount → long, premium → short).
- [ ] Có [[20 - Liquidity Sweep]] hoặc rejection rõ tại cạnh/CE.
- [ ] [[21 - Market Structure Shift]] LTF xác nhận.
- [ ] Có entry array (FVG/OB) để vào, SL rõ ràng ngoài cạnh NWOG.
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
> Một NWOG "bị xuyên qua không phản ứng" **không bị xóa khỏi chart** — nó vẫn là SR lịch sử và có thể phản ứng ở lần test sau. "Vô hiệu" ở đây nghĩa là **vô hiệu cho kế hoạch trade hiện tại**, không phải xóa mốc.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[NWOG-Example-Correct.svg]]

**Mô tả:**
- Tuần mở **gap down** (Sunday Open < Friday Close); giá đầu tuần nằm ở discount dưới CE.
- Bias bullish HTF, draw on liquidity là NWOG **unfilled** phía trên.
- Trong London KZ, giá quét sellside và phản ứng tại cạnh dưới NWOG, M5 cho MSS lên + FVG bullish.

**Vì sao đây là ví dụ tốt:**
- Mốc NWOG được vẽ đúng từ Friday Close (17:00 ET) → Sunday Open (18:00 ET), có CE 50%.
- Entry chỉ thực hiện **sau xác nhận** (sweep + MSS + FVG), không phải chỉ vì chạm CE.
- Mục tiêu hợp lý: CE rồi tới NWOG unfilled phía trên (draw on liquidity).
- Tiếp cận trong kill zone, đúng phía premium/discount.

### Ví dụ sai
![[NWOG-Example-Wrong.svg]]

**Mô tả:**
- Trader vào long ngay khi giá **vừa chạm CE** mà không chờ phản ứng/MSS.
- Giá đóng nến xuyên thẳng qua CE và cạnh đối diện của NWOG.
- Lệnh dính SL khi mốc bị "xuyên qua không phản ứng".

**Bài học:**
- NWOG/CE là **mốc chờ**, không phải lệnh tự động — luôn cần xác nhận LTF.
- Vào lệnh ngoài kill zone / lúc news làm tăng rủi ro mốc bị bỏ qua.
- Đặt SL ngoài cạnh NWOG, không quá sát CE.
- Phải xác định trước hướng bias (premium/discount); vào ngược bias là sai.

### Giải phẫu NWOG
![[NWOG-Anatomy.svg]]

**Mô tả:** Sơ đồ chú thích Friday Close, Sunday Open, NWOG range, CE 50%, và cách giữ 3–5 NWOG gần nhất làm mốc tham chiếu.

---

## 7. Entry model liên quan

- [[ICT 2022 Model]] — sweep → MSS → FVG entry, với NWOG/CE làm vùng POI/draw.
- [[20 - Liquidity Sweep]] — quét cạnh NWOG trước khi đảo chiều.
- [[21 - Market Structure Shift]] — xác nhận đảo chiều LTF tại NWOG.
- [[Fair Value Gap]] — entry array sau MSS.
- [[Order Block]] — confluence tại cạnh/CE NWOG.
- [[10 - Consequent Encroachment (Mean Threshold)]] — CE là mức phản ứng chính.
- [[27 - Premium Discount]] / [[12 - Daily Bias]] — xác định hướng vào lệnh.

```text
[Chuỗi triển khai chuẩn quanh NWOG]
1. HTF: vẽ 3–5 NWOG + CE → xác định draw (NWOG unfilled) & premium/discount
2. Chờ giá tiếp cận NWOG/CE đúng phía bias, trong kill zone
3. LTF: Liquidity Sweep tại cạnh/CE → Market Structure Shift đúng hướng
4. Entry vào FVG/OB hình thành sau MSS; SL ngoài cạnh NWOG
5. TP1 = CE; TP2 = cạnh đối diện / NWOG unfilled kế tiếp
```

> [!note]
> NWOG hoạt động mạnh nhất khi **đóng vai trò draw/POI trong khung của [[ICT 2022 Model]]**, không phải dùng riêng lẻ. CE là điểm phản ứng then chốt.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning]
> Không có đủ mục A + B → **không có lệnh**. NWOG là mốc chờ, kiên nhẫn là kỷ luật.

### A. Context
- [ ] Đã vẽ 3–5 NWOG gần nhất + CE từng cái.
- [ ] Xác định giá đang premium hay discount so với CE.
- [ ] Tìm được NWOG unfilled = draw on liquidity của tuần.
- [ ] Bias HTF ([[12 - Daily Bias]]) rõ ràng và NHẤT QUÁN với hướng định trade.

### B. Execution
- [ ] Giá tiếp cận NWOG/CE trong [[18 - Kill Zones]].
- [ ] Có [[20 - Liquidity Sweep]] / rejection tại vùng.
- [ ] Có [[21 - Market Structure Shift]] LTF xác nhận.
- [ ] Có entry array (FVG/OB), SL ngoài cạnh NWOG, RR ≥ ngưỡng tối thiểu.
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
| Vào lệnh chỉ vì chạm CE | Entry ngay khi giá touch CE, không xác nhận | NWOG là mốc chờ, không phải tín hiệu; dễ bị xuyên qua | Luôn chờ sweep + MSS + FVG trước khi vào |
| Vẽ sai mốc thời gian | Dùng giờ địa phương thay vì ET; lấy nhầm close/open | Sai cả range & CE → mọi phân tích lệch | Cố định múi giờ ET: Fri 16:59–17:00, Sun 17:00–18:00 |
| Xóa NWOG đã fill | Chỉ giữ gap chưa fill | Gap đã fill vẫn là SR mạnh | Giữ 3–5 NWOG gần nhất bất kể đã fill |
| Bỏ qua premium/discount | Long ở premium / short ở discount | Vào ngược fair value, xác suất thấp | Luôn chiếu vị trí giá so với CE trước khi quyết định hướng |
| Quá nhiều NWOG trên chart | Vẽ 10+ gap, rối mắt | Mất trọng tâm, nhiễu | Giữ tối đa 3–5 cái gần nhất |
| Coi NWOG luôn fill ngay tuần này | Ép giá phải quay về gap tuần này | Có thể mất nhiều tuần; ép lệnh sai timing | Dùng NWOG làm draw dài hạn, không cưỡng ép timing |
| Bỏ qua confluence | Trade NWOG đứng một mình | Thiếu xác suất | Ưu tiên NWOG trùng OB/FVG/liquidity |

---

## 10. Câu hỏi tự kiểm tra
- Friday Close và Sunday Open lấy vào những mốc giờ ET nào?
- CE của NWOG tính thế nào và vì sao nó quan trọng hơn các cạnh?
- NWOG khác NDOG ở điểm nào? Khi nào hai cái này chồng nhau?
- Vì sao gap đã fill vẫn nên giữ trên chart?
- Làm sao dùng NWOG để xác định premium/discount của tuần?
- "NWOG unfilled = draw on liquidity" nghĩa là gì trong thực chiến?
- Điều kiện tối thiểu để biến NWOG từ mốc tham chiếu thành setup hợp lệ?

---

## 11. Flashcards / Active Recall
- **Q1:** NWOG được tạo bởi hai mức giá nào, vào giờ ET nào?
  → A1: Friday Close (settlement ~16:59–17:00 ET) và Sunday Open (reopen ~17:00–18:00 ET).
- **Q2:** Mức quan trọng nhất bên trong NWOG là gì?
  → A2: CE (Consequent Encroachment) = 50% của range; là nam châm và SR chính.
- **Q3:** Nên giữ bao nhiêu NWOG trên chart và có xóa khi đã fill không?
  → A3: Giữ 3–5 cái gần nhất; không xóa khi đã fill (vẫn là SR).
- **Q4:** NDOG là gì và khác NWOG thế nào?
  → A4: New Day Opening Gap — gap giữa close ngày trước (~16:15 ET) và reopen (~18:00 ET); phiên bản ngày, sức nặng nhỏ hơn NWOG (tuần).
- **Q5:** Vì sao weekend gap lại có ý nghĩa với ICT?
  → A5: Cuối tuần thị trường không giao dịch → inefficiency không thể fill → thị trường thường quay lại balance; là fair value & draw on liquidity.
- **Q6:** Điều kiện để vào lệnh tại NWOG là gì?
  → A6: Đúng phía premium/discount + tiếp cận trong kill zone + sweep/rejection + MSS LTF + entry array (FVG/OB) với SL ngoài cạnh NWOG.

---

## 12. Lesson Learned
> [!example] Ghi nhận khi áp dụng thực tế
> - Bối cảnh: ____
> - NWOG dùng (Fri Close / Sun Open / CE): [level] / [level] / [level]
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
| Phân biệt NWOG vs NDOG | ____ | |
| Dùng CE làm SR/bias | ____ | |
| Nhận diện draw (unfilled) | ____ | |
| Tích hợp vào ICT 2022 Model | ____ | |
| Kỷ luật chờ xác nhận | ____ | |

**Kế hoạch ôn tập:**
- [ ] Backtest 10–20 lần giá tiếp cận NWOG/CE trên NQ1/NAS100 & EURUSD.
- [ ] Mỗi tuần: vẽ NWOG mới Chủ Nhật, ghi lại phản ứng tới CE trong tuần.
- [ ] Đối chiếu với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]].
- [ ] Review lại note này sau 2 tuần, cập nhật `confidence` & `last_reviewed`.

---

## Best Practices

> [!success] Nguyên tắc vàng
> **NWOG mạnh nhất và "sạch" nhất khi có một khoảng đóng cửa thị trường thật sự (index/futures); trên forex nó chỉ là một xấp xỉ mềm hơn nhiều. Dùng NWOG làm mốc bias/draw ở khung tuần — không bao giờ làm tín hiệu entry độc lập — và luôn đối chiếu với [[12 - Daily Bias]] trước khi diễn giải hướng.**

1. **Trên index/futures (NQ1/NDX, NAS100) NWOG là "sạch" nhất — nên coi đây là ứng dụng chuẩn.** CME futures thực sự đóng cửa cuối tuần và có giờ reopen cố định (~17:00–18:00 ET Chủ Nhật), tạo ra một khoảng gap giá thật, khách quan, không ai tranh cãi được. Đây là nơi lý thuyết NWOG được ICT xây dựng gốc và có độ tin cậy cao nhất trong bốn thị trường bạn theo dõi. Ghi `nwog_instrument_type: futures` khi log các setup trên NQ1/NAS100.

2. **Trên forex (EURUSD, GBPUSD, XAUUSD) NWOG chỉ là một xấp xỉ mềm — hạ trọng số tương ứng.** Thị trường forex giao dịch gần như liên tục qua nhiều trung tâm tài chính; phiên Chủ Nhật tối mở lại với thanh khoản rất mỏng nhưng **không có một "market close" chính thức** như futures. Gap quan sát được thường nhỏ hơn, đôi khi gần như "inside" (xem ví dụ sai ở mục 6). Không đối xử với NWOG forex y hệt NWOG futures — coi nó như một tín hiệu bổ trợ yếu hơn, cần nhiều confluence hơn để tin tưởng. Ghi `nwog_instrument_type: forex-approx` để sau này so sánh win-rate giữa hai nhóm.

3. **Luôn dùng NWOG như một mốc bias/target ở khung TUẦN, không phải một tín hiệu entry.** NWOG trả lời câu hỏi "giá đang premium hay discount so với tuần, và draw on liquidity của tuần nằm ở đâu" — nó không tự nó nói "vào lệnh ngay". Mọi entry thực tế vẫn cần chuỗi sweep → MSS → FVG/OB trên LTF như mô tả ở mục 4–5. Ghi `weekly_bias_aligned: yes/no` cho mỗi lệnh: lệnh có đi đúng hướng bias mà NWOG/CE gợi ý không?

4. **Kết hợp NWOG với [[12 - Daily Bias]] ở cấp độ tuần trước khi hạ xuống ngày.** Trước khi dùng Daily Bias để định hướng cho một ngày cụ thể, hãy hỏi: vị trí giá so với CE của NWOG hiện hành có đồng thuận với bias ngày không? Nếu Daily Bias ngược với vị trí premium/discount của NWOG tuần, đó là tín hiệu cần thận trọng hơn (bias ngày có thể chỉ là một nhịp điều chỉnh trong bias tuần lớn hơn) chứ không phải lý do bỏ qua một trong hai.

5. **Giữ 3–5 NWOG gần nhất trên mọi chart, không chỉ chart đang trade.** Vì NWOG là mốc lịch sử (gap đã fill vẫn là SR), việc xóa sớm khiến bạn mất khả năng nhận diện confluence khi giá quay lại một mức cũ nhiều tuần sau. Việc này tốn ít công nhưng thường bị bỏ qua khi chart bị "dọn dẹp" quá tay.

6. **Không ép giá phải fill NWOG trong tuần hiện tại.** NWOG unfilled là draw on liquidity dài hạn — nó có thể mất vài tuần mới được test lại. Ép lệnh vì "tuần này giá phải về gap" là sai logic; hãy để price action (sweep + MSS đúng phía) xác nhận thời điểm, không phải lịch tuần.

7. **Phân biệt rõ vai trò của Sunday candle khi phân tích cấu trúc đầu tuần.** Như đã nêu ở mục 3 (Nâng cao — True Week Open), dữ liệu Chủ Nhật đầu tiên thường mỏng và nhiễu. Đừng dùng riêng 1–2 nến đó để kết luận MSS hay xác nhận hướng; chờ phiên Á/London Thứ 2 vào để có dữ liệu đáng tin hơn trước khi hành động theo NWOG.

8. **Log đầy đủ và review theo thị trường riêng biệt.** Ghi `nwog_instrument_type`, `weekly_bias_aligned`, trạng thái filled/unfilled, và kết quả R-multiple cho mỗi lần dùng NWOG trong kế hoạch trade. Sau 15–20 mẫu mỗi nhóm (futures vs forex), so sánh win-rate và mức độ "sạch" của phản ứng tại CE — **cần backtest xác nhận** liệu NWOG forex có đáng để giữ trong bộ checklist hay chỉ nên dùng làm ghi chú tham khảo phụ. Đối chiếu kết quả với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]], nâng `confidence` của note này khi có đủ bằng chứng thay vì để mãi ở mức seed.

---

## Appendix — New Week Opening Gap Quick Reference Card

> [!abstract] Thẻ tra nhanh NWOG
> - **Định nghĩa:** Gap giữa Friday Close (~17:00 ET) và Sunday Open (~18:00 ET).
> - **Mốc đóng cửa (Fri):** ____ ET → giá: [level]
> - **Mốc mở cửa (Sun):** ____ ET → giá: [level]
> - **NWOG range:** [range]
> - **CE (50%):** [level]  ← mức phản ứng chính
> - **Trạng thái:** gap up / gap down / inside / filled / unfilled = ____
> - **Vị trí giá hiện tại:** premium / discount so với CE = ____
> - **Draw on liquidity (NWOG unfilled gần nhất):** [level]
> - **Confluence:** OB / FVG / liquidity / CBDR = ____
> - **Kill zone tiếp cận:** London / NY = ____
> - **Điều kiện entry:** sweep + MSS + FVG, SL ngoài cạnh NWOG
> - **TP1:** CE [level]   **TP2:** cạnh đối diện / NWOG unfilled [level]
> - **Giữ trên chart:** 3–5 NWOG gần nhất (kể cả đã fill)
> - **Liên quan:** [[10 - Consequent Encroachment (Mean Threshold)]] · [[Fair Value Gap]] · [[27 - Premium Discount]] · [[12 - Daily Bias]] · [[18 - Kill Zones]] · [[ICT 2022 Model]]
