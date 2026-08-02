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
last_reviewed:
created: 2026-06-24
updated: 2026-07-28
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

---

## 14. Phân tích chuyên sâu: cơ chế thị trường đằng sau NWOG

![[NWOG-Deep-Mechanism.svg|720]]
*Cơ chế thật của NWOG: CME đóng cửa hoàn toàn từ Friday settlement tới Sunday reopen — nhưng OTC FX, dealer đa quốc gia và tin tức cuối tuần (địa chính trị, central bank) vẫn "chạy ngầm", khiến Sunday Open phản ánh 48-60 giờ thông tin dồn nén, không phải một cú nhảy giá tình cờ.*

### Cơ chế orderflow/auction thực sự

- **CME futures đóng cửa thật từ ~17:00 ET Thứ Sáu đến ~18:00 ET Chủ Nhật** — đây là khoảng ngắt quãng dài nhất trong tuần giao dịch tiêu chuẩn (~49 giờ), dài hơn nhiều so với halt hằng ngày ~1¾ giờ của NDOG. Vì vậy lượng thông tin "dồn nén" chờ được định giá lại tại Sunday Open lớn hơn hẳn — đây là lý do cốt lõi khiến NWOG có sức nặng cao hơn NDOG, không phải vì ICT "quy định" thế.
- Trong khi CME đóng, **thị trường FX giao ngay (spot OTC) và một số venue phái sinh vẫn hoạt động rải rác** qua các trung tâm tài chính Trung Đông/châu Á mở cửa sớm Chủ Nhật tối (giờ địa phương) — nghĩa là "giá thế giới" của rủi ro thực ra không hoàn toàn đứng yên suốt cuối tuần, chỉ riêng CME index futures là đứng yên hoàn toàn.
- **Tin tức cuối tuần có trọng số bất đối xứng:** các sự kiện địa chính trị, phát biểu ngân hàng trung ương, tin bầu cử thường được cố ý công bố cuối tuần (khi thị trường thanh khoản thấp nhất) để giảm biến động tức thời — nhưng hệ quả là toàn bộ phản ứng dồn vào đúng cửa sổ Sunday Open, khiến NWOG cuối tuần có tin thường rộng bất thường so với NWOG "bình thường".
- **Dealer FX (interbank) phải neo giá quote Thứ Hai theo world events cuối tuần** — đây là cơ chế tương tự cách NDOG hình thành hằng ngày nhưng ở quy mô lớn hơn: giá Sunday Open là kết quả tổng hợp của mọi thông tin từ dealer desk toàn cầu, không phải giá do một sàn duy nhất quyết định.
- Về bản chất **thanh khoản Sunday Open cực mỏng** (nhiều bàn trading lớn chưa vào ca, thanh khoản chủ yếu đến từ Sydney/Tokyo mở cửa) — nến Chủ Nhật đầu tiên do đó dễ bị "outlier" bởi một vài lệnh lớn, tương tự vấn đề đã nêu ở mục 3 (Nâng cao — True Week Open) của note.

### Đối chiếu với các khung lý thuyết khác

| Khung lý thuyết | Điểm trùng với NWOG | Điểm khác biệt |
|---|---|---|
| **Auction Market Theory** | NWOG là "gap ngoài giờ giao dịch" kinh điển nhất trong Market Profile — lý thuyết dự đoán giá có xu hướng "auction" trở lại lấp gap khi thanh khoản đầy đủ quay lại (Thứ Hai/Thứ Ba). | Market Profile không phân biệt NWOG vs NDOG theo "sức nặng" cố định — chỉ dùng độ rộng gap tương đối so với average true range. |
| **Wyckoff (Composite Man)** | Cuối tuần được xem như giai đoạn Composite Man "chuẩn bị" — Sunday Open phản ánh vị thế tích lũy/phân phối đã thiết lập trước đó, giống ý tưởng NWOG là "điểm nối" giữa hai giai đoạn campaign. | Wyckoff không gán riêng ý nghĩa "gap thời gian cuối tuần" mà xem xét toàn bộ cấu trúc nhiều tuần bằng volume, không riêng biệt hai điểm giá. |
| **Orderflow/Footprint** | Volume tại nến Sunday đầu tiên thường cực thấp trên footprint — xác nhận trực quan giả thuyết "vùng chưa kiểm định" quanh CE của NWOG. | Cần dữ liệu tick thật để xác nhận, còn NWOG chỉ dựa vào hai điểm giá OHLC. |

### Điều kiện làm NWOG mạnh lên/yếu đi

- **Regime trending mạnh xuyên suốt nhiều tuần** (bull run chỉ số Mỹ 2023-2024): NWOG bị "nuốt" nhanh, CE hiếm khi giữ vai trò cản, giá chỉ gap tiếp theo hướng trend.
- **Regime ranging đa tuần**: đây là môi trường lý tưởng — CE của NWOG phản ứng rõ rệt nhiều lần liên tiếp vì giá dao động trong biên độ ổn định.
- **Volatility cao đầu tuần có sự kiện lớn** (FOMC thứ Tư, NFP thứ Sáu tuần trước): NWOG cuối tuần đó thường rộng hơn trung bình, nhưng độ tin cậy giảm vì gap phản ánh phần lớn là premium rủi ro sự kiện, không phải fair value thuần túy.
- **Volatility thấp mùa hè/kỳ nghỉ**: NWOG mỏng, CE gần như "inside", giá trị tham chiếu thấp.
- **Loại tài sản** là yếu tố quyết định lớn nhất (xem bảng dưới) — sự khác biệt giữa index futures và FX/crypto ở NWOG còn rõ hơn cả ở NDOG vì độ dài khoảng ngắt quãng lớn hơn nhiều.

### Bảng so sánh hành vi NWOG trên 3 loại thị trường

| Tiêu chí | FX majors (EURUSD, GBPUSD) | Index futures (NQ/ES, CME) | Crypto (BTC/ETH) |
|---|---|---|---|
| Có đóng cửa cuối tuần thật không | Gần như có — phần lớn broker/ECN dừng khớp lệnh từ ~17:00 ET Thứ Sáu đến ~17:00 ET Chủ Nhật, dù một số venue nhỏ vẫn có giá lác đác | **Có, rõ ràng nhất** — CME Globex đóng hẳn, giờ mở lại cố định | Không — giao dịch liên tục 24/7/365, không có khái niệm "cuối tuần" |
| NWOG có "thật" không | Có, và thường rõ hơn NDOG (vì khoảng nghỉ dài hơn nhiều so với halt ngày) | NWOG thật và mạnh nhất trong 3 nhóm | Không tồn tại — mọi "gap cuối tuần" tự vẽ trên BTC là ảo giác thống kê |
| Độ rộng gap điển hình | EURUSD: có thể 10-40 pip cuối tuần có tin; GBPUSD thường rộng hơn do thanh khoản mỏng hơn | NQ: 20-150+ điểm tùy tin cuối tuần | N/A |
| Nguồn gap | Chênh lệch giữa Friday spot close và Sunday Tokyo/Sydney open, phản ánh tin cuối tuần dồn nén qua dealer OTC | Đấu giá lại thật sau đóng cửa CME hoàn toàn | Không có — traders coi "candle W1 close/open" chỉ là quy ước mốc thời gian, không phải gap thật |
| Khuyến nghị | Dùng NWOG với độ tin cậy trung bình-cao, luôn kiểm tra lịch tin cuối tuần trước | Dùng NWOG chuẩn ICT — mốc tham chiếu tuần đáng tin nhất | Không dùng NWOG; dùng Weekly Open (giá tại 00:00 UTC Thứ Hai) làm bias filter riêng biệt |

> [!tip] Chốt cơ chế
> NWOG mạnh hơn NDOG không phải vì "ICT nói vậy" mà vì **khoảng ngắt quãng dài hơn gấp ~28 lần** (49 giờ vs 1¾ giờ) đồng nghĩa lượng thông tin dồn nén chờ định giá lại lớn hơn nhiều — đây là lý do cơ học, đo lường được, không phải một quy tắc tùy ý.

---

## 15. Phản biện & giới hạn (Critique)

### 1. Phản biện từ góc nhìn khoa học/quant

- **Tính chủ quan khi vẽ:** dù hai cạnh gap (Friday Close, Sunday Open) là khách quan về mặt dữ liệu, việc quyết định "gap này có ý nghĩa hay không" (đủ rộng, đủ rõ để trade) vẫn hoàn toàn chủ quan — không có ngưỡng độ rộng chuẩn hóa nào được công bố để phân biệt "NWOG đáng tin" với "NWOG inside không đáng kể".
- **Hindsight bias:** trader nhớ những tuần NWOG "kéo giá về CE đẹp như sách" nhưng quên các tuần giá gap liên tiếp theo cùng hướng 2-3 tuần liền mà không bao giờ quay lại CE của tuần đầu tiên — survivorship bias trong trí nhớ khiến concept trông hiệu quả hơn thực tế.
- **Không có backtest công khai đạt chuẩn thống kê:** tương tự NDOG, chưa có nghiên cứu định lượng độc lập nào với sample size đủ lớn và kiểm định ý nghĩa thống kê chứng minh CE của NWOG có tỷ lệ "phản ứng" cao hơn một đường 50% ngẫu nhiên bất kỳ trong cùng dealing range tuần.
- **Unfalsifiable khi fail:** khi giá xuyên CE tuần không phản ứng, lý giải thường là "trend quá mạnh nên bỏ qua NWOG" — một lý luận đúng bất kể kết quả ra sao, nên không kiểm chứng được.
- **Overfitting khi thêm filter:** thêm điều kiện "unfilled + đúng phía premium/discount + confluence OB/FVG + trong kill zone + không mâu thuẫn Daily Bias" khiến mẫu backtest co lại chỉ còn vài case mỗi quý — không đủ để rút ra kết luận tổng quát.
- **Backtest độc lập trái chiều:** nhiều thử nghiệm định lượng công khai về "weekend gap fill rate" trên các chỉ số Mỹ (S&P, Nasdaq) cho kết quả rất khác nhau tùy khung thời gian nghiên cứu và định nghĩa "fill" — không có con số đồng thuận.
- **Giải thích thay thế đơn giản hơn:** hiện tượng "giá quay về gần CE của NWOG" có thể chỉ phản ánh **tính chất mean-reverting ở khung thời gian ngắn cộng với thực tế đơn giản CE luôn nằm giữa hai giá tuần liên tiếp** (vốn không cách nhau quá xa trong phần lớn các tuần bình thường) — không cần viện đến "market maker để lại dấu vết".

### 2. Phản biện của phản biện

- **Phần phải chấp nhận hoàn toàn:** thiếu backtest công khai chuẩn hóa, thiếu ngưỡng khách quan để phân loại "gap đáng kể", và rủi ro overfitting khi cộng filter — đúng, không thể phủ nhận.
- **Phần có thể trả lời được:**
  - **Quy tắc hóa cứng để backtest được:** hoàn toàn có thể định nghĩa "gap đáng kể" = độ rộng NWOG ≥ X% của ATR(20) tuần, và "phản ứng" = giá chạm CE ±Y điểm rồi đóng N nến ngược hướng — một khi cố định, ai cũng backtest ra cùng kết quả, dù kết quả đó có ấn tượng hay không.
  - **NWOG là framework đọc chart, không phải máy dự đoán:** giá trị cốt lõi nằm ở việc cho một mốc **khách quan, không cần vẽ tay** để định vị premium/discount của cả tuần — điều mà các công cụ chủ quan khác (trendline, Fibonacci tự chọn điểm) không làm được.
  - **Edge đến từ risk management + location:** một trader chỉ vào lệnh tại NWOG khi có sweep + MSS xác nhận thực chất đang tận dụng NWOG như một bộ lọc vị trí (location filter) để tìm nơi đặt SL chặt và tham gia cùng hướng xác nhận cấu trúc — phần "dự đoán hướng" gần như không tồn tại độc lập.

### 3. Giới hạn cứng phải chấp nhận

1. Không có nghiên cứu định lượng độc lập, công khai, đạt chuẩn thống kê nào xác nhận CE của NWOG có tỷ lệ phản ứng vượt trội một đường 50% ngẫu nhiên trong cùng dealing range.
2. "Friday Close" và "Sunday Open" khác nhau đáng kể tùy nguồn dữ liệu (CME settlement chính thức vs giá hiển thị trên nền tảng retail vs giá dealer FX) — không có một con số "đúng tuyệt đối" duy nhất.
3. NWOG không tồn tại đúng bản chất trên crypto (giao dịch 24/7, không đóng cửa) — mọi vận dụng ở đó chỉ là quy ước thời gian tùy chọn.
4. Trên FX, "đóng cửa cuối tuần" không đồng nhất giữa các broker (một số vẫn báo giá lác đác thứ Bảy do thanh khoản dư từ phiên châu Á cuối), khiến việc xác định chính xác Friday Close với broker này có thể khác broker khác vài pip.
5. Không thể loại trừ khả năng phần lớn "phản ứng tại CE" chỉ là hiện tượng mean-reversion tự nhiên trong biến động ngắn hạn, không liên quan trực tiếp đến hành vi có chủ đích của market maker như narrative ICT mô tả.

> [!quote] Kết luận trung thực
> NWOG là công cụ khoanh vùng đáng tin nhất trong họ "opening gap" của ICT, đặc biệt trên index futures nơi việc đóng cửa cuối tuần là sự kiện khách quan, đo lường được. Nhưng nó vẫn là **một mốc tham chiếu, không phải một quy luật vật lý** — chỉ dùng khi có xác nhận LTF độc lập, luôn tự backtest với định nghĩa cứng riêng, và không bao giờ coi "NWOG unfilled" là lý do đủ để ép một lệnh phải thắng.

---

## 16. Edge Cases thực chiến (chỉ thấy khi live/backtest đủ nhiều)

### Edge Case 1 — DST Mỹ và DST châu Âu lệch nhau 2-3 tuần mỗi năm làm Sunday Open "trôi" giờ

**Tình huống:** Mỹ chuyển sang giờ mùa hè (EDT) vào Chủ Nhật thứ hai của tháng 3, nhưng Liên minh châu Âu/Anh chuyển giờ mùa hè muộn hơn — Chủ Nhật cuối tháng 3 (thường lệch 1-2 tuần). Ngược lại vào tháng 10-11, EU "fall back" vào Chủ Nhật cuối tháng 10, còn Mỹ chờ đến Chủ Nhật đầu tháng 11 (lệch khoảng 1 tuần). Trong các cửa sổ giao thời này, khoảng cách giờ giữa "giờ mở cửa London" và "giờ mở cửa NY futures" **không cố định như bình thường** — có những tuần bị lệch thêm/bớt 1 giờ so với quy đổi quen thuộc.

**Vì sao bẫy được cả trader có kinh nghiệm:** Một trader quen quy đổi "Sunday Open 18:00 ET = 23:00 giờ London" cả năm sẽ tính sai đúng trong 1-2 tuần giao thời mỗi năm (cuối tháng 3 và cuối tháng 10) — vì trong tuần đó, Mỹ đã đổi giờ nhưng Anh/EU chưa (hoặc ngược lại), khiến chênh lệch London-NY tạm thời là 4 giờ thay vì 5 giờ tiêu chuẩn (hoặc ngược lại).

**Cách nhận diện sớm:** Đánh dấu lịch riêng hai ngày DST: Mỹ (Chủ Nhật thứ 2 tháng 3 / Chủ Nhật đầu tháng 11) và EU (Chủ Nhật cuối tháng 3 / Chủ Nhật cuối tháng 10) — bất kỳ tuần nào nằm giữa hai mốc DST khác quốc gia này đều là "tuần rủi ro quy đổi".

**Cách xử lý:** Trong các tuần giao thời DST, tuyệt đối không tự cộng trừ giờ bằng trí nhớ — luôn kiểm tra trực tiếp đồng hồ NY time và London time hiển thị song song, và set toàn bộ chart theo giờ NY tuyệt đối thay vì giờ địa phương quy đổi tay.

![[NWOG-Edge-Cases.svg|720]]
*So sánh 3 chế độ giờ trong năm: bình thường NY-London lệch 5 giờ, nhưng trong ~3 tuần giao thời tháng 3 và ~1 tuần tháng 10-11, độ lệch tạm thời chỉ còn 4 giờ do Mỹ và EU đổi giờ DST không cùng ngày.*

### Edge Case 2 — Server broker GMT+2/+3 khiến Sunday Open trên chart lệch hẳn với Sunday Open thật của CME

**Tình huống:** Broker CFD phổ biến dùng giờ server GMT+2 (mùa đông)/GMT+3 (mùa hè). Candle Chủ Nhật đầu tiên trên MT4/MT5 thường mở lúc 00:00 giờ server — tức khoảng 21:00-22:00 ET Chủ Nhật (không phải 17:00-18:00 ET) tùy chế độ DST đang áp dụng ở cả hai phía.

**Vì sao bẫy được cả trader có kinh nghiệm:** Trader dùng nến D1/W1 trên chart broker để xác định "Sunday Open" sẽ vô tình lấy một mức giá đã trải qua 3-4 giờ giao dịch thực tế (kể từ 18:00 ET thật), không phải giá mở cửa nguyên bản — Sunday Open "giả" này thường đã dịch chuyển đáng kể so với tick đầu tiên thật trên CME, đặc biệt nếu có tin ngay đầu phiên Á.

**Cách nhận diện sớm:** So sánh giờ mở nến D1 trên chart broker với 18:00 ET quy đổi chuẩn — nếu không trùng khớp, chart bạn dùng không phản ánh đúng Sunday Open theo định nghĩa ICT gốc.

**Cách xử lý:** Luôn lấy Sunday Open từ chart futures CME thật (continuous contract) hoặc từ nguồn dữ liệu cho phép custom timezone chính xác 18:00 ET, không dựa vào nến D1/W1 mặc định của broker CFD.

### Edge Case 3 — Ngày lễ Mỹ rơi vào thứ Hai (Labor Day, MLK Day, Presidents' Day) làm tuần mới "mất" phiên London/NY đầu tuần

**Tình huống:** Khi thứ Hai là ngày lễ liên bang Mỹ (CME đóng cửa hoặc rút ngắn), NWOG hình thành từ Friday Close vẫn đúng như thường lệ, nhưng phiên NY đầu tuần để "test" hoặc "xác nhận" mốc CE bị trì hoãn tới tận thứ Ba — trong khi phiên London/Á thứ Hai vẫn hoạt động bình thường (không phải lễ ở châu Âu/châu Á).

**Vì sao bẫy được cả trader có kinh nghiệm:** Trader chờ đợi phản ứng "chuẩn" của NY tại CE ngay thứ Hai sẽ không thấy volume/displacement đúng như các tuần bình thường — dễ kết luận nhầm "CE không có ý nghĩa tuần này" trong khi thực chất chỉ là thiếu thanh khoản NY, không phải NWOG mất hiệu lực.

**Cách nhận diện sớm:** Luôn kiểm tra lịch nghỉ lễ liên bang Mỹ (New Year's Day, MLK Day tháng 1, Presidents' Day tháng 2, Memorial Day tháng 5, Juneteenth, July 4th, Labor Day tháng 9, Thanksgiving tháng 11, Christmas) trước khi lên kế hoạch tuần.

**Cách xử lý:** Vào tuần có lễ thứ Hai, hạ kỳ vọng phản ứng CE trong ngày lễ, dời trọng tâm quan sát sang thứ Ba (khi NY hoạt động đầy đủ trở lại) như "ngày mở tuần thực tế" về mặt thanh khoản.

### Edge Case 4 — NWOG trên crypto 24/7: không hề tồn tại nhưng traders vẫn cố "vẽ ra" bằng W1 candle

**Tình huống:** BTCUSD/ETHUSD giao dịch liên tục không nghỉ. Một số trader coi "giá đóng nến tuần UTC (thường Chủ Nhật 23:59 hoặc theo quy ước sàn)" và "giá mở nến tuần kế tiếp" là NWOG — nhưng như trên NDOG, hai giá trị này **luôn bằng nhau tuyệt đối** vì không có khoảng ngắt quãng thời gian nào.

**Vì sao bẫy được cả trader có kinh nghiệm:** Nhầm lẫn này phổ biến hơn cả nhầm lẫn tương tự với NDOG vì nhiều indicator/script cộng đồng (kể cả một số script Pine Script phổ biến trên TradingView) tự động "vẽ NWOG" cho mọi symbol kể cả BTCUSD bằng cách lấy chênh lệch giá giữa hai sàn tại thời điểm quy ước — tạo ảo giác có một "gap" trong khi đó chỉ là basis/spread liên sàn nhiễu.

**Cách nhận diện sớm:** Kiểm tra trực tiếp: nếu giá đóng nến W1 và giá mở nến W1 kế tiếp trên cùng một sàn duy nhất bằng nhau tuyệt đối (0.00 chênh lệch), NWOG không tồn tại cho symbol đó.

**Cách xử lý:** Trên crypto, dùng Weekly Open (giá đơn tại một mốc giờ quy ước, ví dụ 00:00 UTC Thứ Hai) làm bias filter kiểu Midnight Open — tuyệt đối không tìm hay báo cáo "NWOG" cho BTC/ETH trong journal.

### Edge Case 5 — Sunday candle thanh khoản mỏng tạo NWOG "giả" bị đảo ngược hoàn toàn trong 2-3 giờ đầu

**Tình huống:** Một số Chủ Nhật, tick đầu tiên khi CME reopen 18:00 ET bị một lệnh lớn bất thường đẩy giá chênh hẳn so với Friday Close (tạo NWOG trông "rất rộng"), nhưng trong 2-3 giờ tiếp theo (khi thanh khoản Sydney/Tokyo dần vào), giá quay ngược lại gần sát Friday Close — nghĩa là NWOG "thật" (dựa trên giá ổn định) hẹp hơn nhiều so với NWOG "biểu kiến" (dựa trên tick đầu tiên).

**Vì sao bẫy được cả trader có kinh nghiệm:** Nếu vẽ NWOG ngay khi vừa thấy tick đầu tiên và đặt lệnh dựa trên CE tính từ đó, trader sẽ giao dịch một mốc hoàn toàn sai chỉ vài giờ sau khi thanh khoản thật vào thị trường.

**Cách nhận diện sớm:** Không vội vẽ NWOG chính thức ngay khi vừa thấy giá tick đầu tiên — quan sát diễn biến giá trong 1-3 giờ đầu tiên của phiên Á Chủ Nhật để xác nhận Sunday Open có "giữ" hay bị đảo ngược mạnh.

**Cách xử lý:** Với các tuần nghi ngờ outlier, dùng giá ổn định sau 2-3 giờ (thay vì tick đầu tiên tuyệt đối) làm Sunday Open tham chiếu cho CE, ghi chú rõ trong journal đây là "NWOG điều chỉnh" khác với "NWOG tick đầu tiên".

### Edge Case 6 — Tuần đáo hạn quyền chọn hằng tháng/quý làm NWOG kém tin cậy do pinning effect

**Tình huống:** Vào tuần thứ Sáu đáo hạn quyền chọn tháng (monthly OPEX, thường thứ Sáu tuần thứ 3) hoặc đáo hạn quý (quarterly triple/quadruple witching tháng 3/6/9/12), giá chỉ số có xu hướng bị "ghim" (pinning) gần các strike có open interest lớn ngay trước khi đóng cửa thứ Sáu — khiến Friday Close không phản ánh fair value tự nhiên mà phản ánh áp lực dealer hedging gamma quanh strike đó.

**Vì sao bẫy được cả trader có kinh nghiệm:** NWOG được vẽ từ một Friday Close bị "ghim nhân tạo" sẽ cho một CE lệch khỏi xu hướng thật của thị trường — tuần kế tiếp giá thường "thoát pin" nhanh chóng ngay đầu tuần, khiến CE của NWOG hầu như không có ý nghĩa tham chiếu.

**Cách nhận diện sớm:** Kiểm tra lịch đáo hạn quyền chọn (OPEX calendar) — nếu Friday Close rơi đúng ngày OPEX lớn (đặc biệt quarterly witching), tăng cảnh giác với NWOG tuần đó.

**Cách xử lý:** Hạ trọng số tin cậy cho NWOG hình thành từ Friday OPEX; ưu tiên chờ xác nhận cấu trúc (MSS) rõ ràng vào thứ Ba-thứ Tư tuần mới (sau khi hiệu ứng pinning đã tan) trước khi tin vào CE.

### Edge Case 7 — Fractal conflict: NWOG tuần và NWOG tuần trước chồng lấp gây nhiễu loạn confluence giả

**Tình huống:** Trong giai đoạn ranging kéo dài nhiều tuần, NWOG của 2-3 tuần liên tiếp có thể nằm rất gần nhau về vùng giá (chênh nhau vài điểm NQ hoặc vài pip FX) — tạo cảm giác "vùng confluence rất mạnh" vì nhiều CE chồng lên nhau, nhưng thực chất đây chỉ là hệ quả tự nhiên của thị trường đi ngang, không phải một tín hiệu đặc biệt.

**Vì sao bẫy được cả trader có kinh nghiệm:** Trader dễ đánh giá quá cao độ tin cậy của một vùng giá chỉ vì "3 CE của 3 tuần gần nhau" trùng nhau — trong khi log dữ liệu khách quan cho thấy trong một thị trường ranging, HẦU HẾT các mốc tham chiếu (OB, FVG, NWOG, NDOG) đều có xu hướng tụ lại gần nhau đơn giản vì range giá tổng thể hẹp.

**Cách nhận diện sớm:** Trước khi kết luận "vùng confluence mạnh", kiểm tra xem liệu toàn bộ dealing range của giai đoạn đó có đang hẹp bất thường không — nếu có, hạ kỳ vọng về "sức mạnh đặc biệt" của vùng chồng lấp này.

**Cách xử lý:** Chỉ tính confluence NWOG đa tuần là có ý nghĩa khi kèm theo bối cảnh HTF rõ ràng (D1/W1 bias, liquidity pool lớn) — không dùng riêng số lượng CE chồng lấp làm tiêu chí duy nhất.

---

## 17. Case Studies chuyên sâu

![[NWOG-Case-Study.svg|720]]
*Case Study 1 minh họa: sweep đáy phiên Á → MSS → FVG → entry 1.0898 → TP1 CE 1.0907 → TP2 cạnh trên NWOG 1.0920, kết quả +1.83R.*

### Case Study 1 — EURUSD, thắng đúng sách: NWOG gap-down dẫn giá về CE trong London KZ Thứ Hai

**Bối cảnh HTF:** Tuần từ Thứ Hai 18/08. Friday Close (tuần trước) tại 1.0920; Sunday Open (18:00 ET, phiên Á/Sydney bắt đầu) tại 1.0894 → NWOG gap-down 1.0894–1.0920, CE = 1.0907. D1 bias bullish (giá vừa sweep sellside tuần trước đó và có MSS H4 tăng), nghĩa là giá mở tuần trong **discount** so với CE — đúng phía bias.

**Setup:** Thứ Hai, giá dao động hẹp quanh 1.0895-1.0905 trong suốt phiên Á (thanh khoản mỏng điển hình đầu tuần). Kỳ vọng: [[18 - Kill Zones|London Kill Zone]] Thứ Hai sẽ quét thanh khoản dưới đáy phiên Á rồi đẩy giá về CE và xa hơn.

**Diễn biến & execution:**
- 02:10 ET (London Open KZ): giá quét đáy phiên Á tại 1.0891 (sweep sellside, thấp hơn Sunday Open 3 pip), để lại wick dài trên M15.
- 02:25 ET: M15 in MSS tăng (phá đỉnh nhỏ 1.0902) + FVG bullish hình thành 1.0896–1.0900.
- Entry: 1.0898. SL: 1.0886 (dưới đáy sweep 5 pip).
- TP1 tại CE 1.0907 — chạm 03:40 ET.
- TP2 tại cạnh trên NWOG 1.0920 (Friday Close, draw on liquidity của tuần) — chạm 07:15 ET (đầu NY AM KZ).

**Kết quả bằng số:** Risk 12 pip (1.0898–1.0886). Reward tới TP2: 22 pip → R-multiple ≈ +1.83R. Với 1 lot chuẩn (10 USD/pip), lãi 220 USD trên rủi ro 120 USD.

**Bài học chỉ rút ra được nhờ case này:** NWOG hoạt động rõ nhất khi kết hợp với thực tế thanh khoản đầu tuần cực mỏng — cú sweep đáy phiên Á "dễ" xảy ra hơn bình thường chính vì thiếu thanh khoản, không phải vì thị trường "cố tình" nhắm vào NWOG. Đây là minh chứng cho luận điểm ở mục 15: edge thật đến từ việc nhận diện đúng bối cảnh thanh khoản mỏng đầu tuần, NWOG chỉ đóng vai trò khung tham chiếu.

### Case Study 2 — NQ, setup đẹp như sách nhưng THUA: NWOG bị "nuốt" bởi tin địa chính trị cuối tuần

**Bối cảnh HTF:** Tuần từ Thứ Hai đầu tháng 4. Friday Close 18,450; Sunday Open 18,405 (gap-down nhẹ, tin thường lệ) → NWOG 18,405–18,450, CE = 18,427.5. D1 bias bullish rõ ràng (chuỗi 3 tuần tăng liên tiếp trước đó).

**Setup:** Thứ Hai đầu phiên Á, giá test nhẹ CE từ dưới lên, tưởng chừng chuẩn bị bật lên tiếp tục xu hướng bullish theo đúng kịch bản NWOG discount → long.

**Diễn biến & execution:**
- 20:30 ET Chủ Nhật (giờ Sydney): tin căng thẳng địa chính trị bất ngờ leo thang (thông báo ngoài giờ hành chính, không nằm trong lịch kinh tế thường lệ) khiến risk-off toàn cầu.
- 21:00 ET: NQ bắt đầu bán tháo mạnh, xuyên thẳng qua CE 18,427.5 và toàn bộ NWOG, giảm xuống 18,340 chỉ trong 90 phút — không hề có bất kỳ phản ứng nào tại CE.
- Trader đã đặt sẵn lệnh chờ (limit order) long tại CE 18,427.5 từ tối Chủ Nhật, SL 18,405 (dưới cạnh dưới NWOG) — lệnh khớp lúc 20:52 ET, dính SL lúc 21:05 ET khi giá tiếp tục rơi.

**Kết quả bằng số:** Lỗ 22.5 điểm NQ = -1R theo kế hoạch ban đầu (risk 22.5 điểm).

**Bài học chỉ rút ra được nhờ case này:** Đặt lệnh chờ (limit order) sẵn tại CE của NWOG **qua đêm cuối tuần** là một trong những lỗi nguy hiểm nhất với concept này — vì đây chính là khung thời gian có xác suất cao nhất xảy ra tin bất ngờ ngoài lịch kinh tế thông thường (địa chính trị, thiên tai, tin doanh nghiệp cuối tuần). Nguyên tắc "News lớn override toàn bộ" trong note cần được diễn giải mở rộng: rủi ro tin cuối tuần **không thể phòng bằng lịch kinh tế** vì phần lớn không được lên lịch trước — do đó nguyên tắc an toàn hơn là không đặt lệnh chờ xuyên đêm Chủ Nhật tại NWOG, mà chờ xác nhận sống vào thứ Hai/thứ Ba.

### Case Study 3 — Đứng ngoài đúng: nhận ra NWOG hình thành từ Friday OPEX bị pinning, không tin CE

**Bối cảnh HTF:** Tuần có quarterly triple witching (thứ Sáu tuần thứ 3 tháng 6). Friday Close tại ES 5,480 — nhưng dữ liệu options cho thấy đây là vùng có open interest cực lớn tại strike 5,480 (gamma pinning rõ rệt suốt buổi chiều thứ Sáu, giá "dính" quanh mức này bất thường 90 phút cuối phiên). Sunday Open tại 5,462 → NWOG 5,462–5,480, CE = 5,471.

**Setup (cân nhắc nhưng bị loại bỏ):** Về lý thuyết, giá đang ở discount so với CE tuần mới, có thể tìm long tại CE nếu bias D1 bullish.

**Diễn biến & execution (quyết định không vào lệnh):**
- Trước khi lên kế hoạch tuần, kiểm tra lại hành vi giá chiều thứ Sáu: nhận thấy rõ dấu hiệu pinning quanh 5,480 (biên độ dao động cực hẹp, volume giảm dần cuối phiên dù đây là ngày OPEX thường có volume cao) — dấu hiệu Friday Close bị "ghim nhân tạo" bởi dealer gamma hedging, không phản ánh fair value tự nhiên.
- Theo edge case 6 đã ghi nhận, hạ mức tin cậy cho CE của NWOG tuần này; quyết định **không đặt lệnh dựa trên CE** cho đến khi có xác nhận cấu trúc từ thứ Ba trở đi.
- Kết quả thực tế: Thứ Hai, giá "thoát pin" nhanh, gap tiếp xuống 5,440 ngay đầu phiên Á rồi dao động hỗn loạn không theo logic CE thông thường trong 2 ngày đầu tuần trước khi ổn định lại.

**Kết quả bằng số:** 0R (không giao dịch) — tránh được một setup có khả năng dính SL cao nếu đã vào long tại CE theo kịch bản ban đầu.

**Bài học chỉ rút ra được nhờ case này:** Kỹ năng nhận diện "Friday Close bất thường" (do OPEX/pinning) **trước khi** nó trở thành cạnh của NWOG là một lớp lọc quan trọng mà phần lớn tài liệu ICT phổ thông không đề cập — đòi hỏi trader phải liên tục theo dõi lịch đáo hạn quyền chọn song song với việc vẽ NWOG, không chỉ nhìn thuần túy vào hai điểm giá.

### Case Study 4 — GBPUSD, minh họa NWOG "xấp xỉ mềm" trên FX bị vô hiệu bởi thanh khoản không đồng đều

**Bối cảnh HTF:** Tuần từ Thứ Hai giữa tháng 9. Do một số broker retail vẫn báo giá GBPUSD lác đác thứ Bảy (dư âm thanh khoản châu Á), "Friday Close" ghi nhận trên nền tảng của trader lúc 17:00 ET thứ Sáu là 1.2650, nhưng nến D1 hiển thị trên chart thực tế đóng muộn hơn tới 1.2647 (do vài giao dịch lẻ tẻ ngoài giờ chính thức). Sunday Open trên cùng nền tảng ghi nhận 1.2622.

**Setup:** Trader tính NWOG dựa trên 1.2647 (giá hiển thị D1 close) thay vì 1.2650 (giá 17:00 ET chuẩn) → NWOG 1.2622–1.2647, CE = 1.26345 — lệch khoảng 1.5 pip so với CE "chuẩn" (1.2650–1.2622, CE = 1.2636).

**Diễn biến & execution:**
- Thứ Hai, London KZ, giá tiếp cận vùng 1.2634-1.2636 — trong biên độ sai lệch giữa hai cách tính CE.
- Vì chênh lệch quá nhỏ (1.5 pip) so với spread trung bình GBPUSD giờ London (thường 1-2 pip) và độ nhiễu bình thường của thị trường, phản ứng giá tại vùng này không đủ rõ ràng để phân biệt được đâu là "phản ứng tại CE chuẩn" và đâu là nhiễu ngẫu nhiên — giá dao động qua lại vài pip rồi tiếp tục xu hướng giảm xuống 1.2590 mà không có MSS tăng rõ ràng nào.
- Trader chờ xác nhận MSS nhưng không có, quyết định không vào lệnh — tránh được việc "ép" một phản ứng không thật sự tồn tại.

**Kết quả bằng số:** 0R (không giao dịch, đúng theo checklist "không có MSS xác nhận").

**Bài học chỉ rút ra được nhờ case này:** Trên FX, sự khác biệt vài pip giữa các nguồn dữ liệu khi xác định Friday Close **có thể lớn hơn chính "sức nặng" biên của một NWOG mỏng** — đây là giới hạn thực tế của việc áp dụng NWOG (vốn được xây dựng gốc trên CME futures với settlement rõ ràng) sang FX, nơi khái niệm "đóng cửa" luôn có một vùng xám. Bài học: trên FX, luôn đòi hỏi MSS LTF rõ ràng làm điều kiện lọc bổ sung mạnh hơn, không tin tưởng CE tới từng pip lẻ.

---

## 18. Tình huống thực chiến (War Stories)

> [!example] War Story 1 — Đặt lệnh chờ NWOG xuyên đêm Chủ Nhật và trả giá
> Tôi từng có thói quen đặt sẵn limit order tại CE của NWOG ngay tối Chủ Nhật trước khi đi ngủ, nghĩ rằng "cứ để đó, sáng dậy xem kết quả". Một lần tin địa chính trị nổ ra lúc 3 giờ sáng giờ tôi (giữa đêm Chủ Nhật rạng Thứ Hai theo giờ Mỹ), lệnh khớp và dính SL trước khi tôi kịp tỉnh dậy kiểm tra tin tức. Từ đó tôi không bao giờ đặt lệnh chờ xuyên đêm cuối tuần tại bất kỳ mốc NWOG nào nữa — chỉ theo dõi sống và vào tay khi có xác nhận.

> [!example] War Story 2 — Nhầm giữa "gap tuần" và "gap do rollover hợp đồng"
> Có một tuần tôi thấy NQ "gap" rất lớn ngay đầu tuần và hào hứng nghĩ đây là NWOG hiếm có với sức nặng cực lớn — hóa ra đó là tuần chart continuous tự động chuyển hợp đồng (contract roll) trùng đúng thứ Sáu tuần đó, khiến "Friday Close" tôi nhìn thấy trên chart là giá của hợp đồng cũ, còn "Sunday Open" là giá hợp đồng mới, chênh lệch hoàn toàn do basis spread chứ không phải weekend gap thật. Từ đó tôi luôn kiểm tra lịch rollover CME trước khi tin vào bất kỳ NWOG "bất thường lớn" nào.

> [!example] War Story 3 — Coi thường tuần Thanksgiving rồi bất ngờ vì "NWOG không phản ứng gì cả"
> Tuần sau Lễ Tạ ơn, tôi vẽ NWOG như bình thường và chờ phản ứng tại CE suốt cả tuần — nhưng thanh khoản thấp bất thường (do thứ Năm nghỉ lễ và thứ Sáu chỉ nửa phiên) khiến giá chỉ đi ngang lình xình cả tuần, không hề có displacement rõ ràng nào tại CE. Tôi từng nghĩ "chắc NWOG thất bại", nhưng thực ra vấn đề là tôi đã bỏ qua yếu tố thanh khoản theo mùa — NWOG cần thanh khoản đầy đủ mới có ý nghĩa, tuần lễ Tạ ơn không phải môi trường phù hợp để tin vào bất kỳ mốc tham chiếu opening-gap nào.

---

## 19. Câu hỏi tự kiểm tra *(bổ sung)*
- Vì sao NWOG có sức nặng lớn hơn NDOG xét về mặt cơ chế thời gian, không chỉ vì "quy tắc ICT"?
- Kể ra ít nhất 2 tình huống DST (Mỹ vs EU) có thể khiến quy đổi giờ Sunday Open sai lệch tạm thời.
- Vì sao đặt lệnh chờ (limit order) xuyên đêm Chủ Nhật tại CE của NWOG là một rủi ro đặc thù của concept này?
- Pinning effect từ đáo hạn quyền chọn (OPEX) ảnh hưởng thế nào đến độ tin cậy của Friday Close?
- Trên crypto, vì sao không thể vẽ NWOG đúng nghĩa dù nhiều indicator cộng đồng vẫn "vẽ" được một đường gì đó?

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
