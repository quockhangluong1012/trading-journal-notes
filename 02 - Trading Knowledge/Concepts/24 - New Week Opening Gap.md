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
updated: 2026-06-24
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
![[NWOG-Example-Correct.png]]

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
![[NWOG-Example-Wrong.png]]

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
![[NWOG-Anatomy.png]]

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
