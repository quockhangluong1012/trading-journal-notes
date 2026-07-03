---
type: ict-concept
concept: Mitigation Block
aliases:
  - Mitigation Block
  - MB
  - Bullish Mitigation Block
  - Bearish Mitigation Block
tags:
  - trading/ict/concept
  - trading/study
  - "#MitigationBlock"
status: seed
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[ICT 2022 Model]]"
importance: 5
confidence: 2
last_reviewed: 2026-07-02
created: 2026-06-26
updated: 2026-07-02
related_concepts:
  - "[[25 - OB - Order Block]]"
  - "[[04 - BB - Breaker Block]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[27 - Premium Discount]]"
  - "[[12 - Daily Bias]]"
prerequisites:
  - "[[25 - OB - Order Block]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Break of Structure]]"
  - "[[19 - Liquidity]]"
common_mistakes: []
---

# Mitigation Block (MB)

> [!summary] Tóm tắt 1 câu
> **Mitigation Block là một order block hình thành từ một FAILURE SWING — giá KHÔNG quét được đỉnh/đáy cũ (swing point giữ vững, không có sweep), sau đó displacement + MSS xác nhận hướng mới; cụm nến ngược chiều cuối cùng trước nhịp đẩy trở thành POI để giá quay lại "giải tỏa" (mitigate) các lệnh kẹt từ nhịp thất bại trước.**

> [!important] Nguyên tắc cốt lõi
> **Điều phân biệt Mitigation Block với [[04 - BB - Breaker Block]] là PHÉP THỬ SWEEP: Breaker BẮT BUỘC quét liquidity (phá đáy/đỉnh cũ) trước khi đảo chiều; Mitigation Block hình thành KHI KHÔNG có sweep — đỉnh/đáy cũ GIỮ VỮNG (higher low / lower high), giá không tạo được đáy/đỉnh mới, rồi MSS xác nhận hướng mới.**
> Hỏi một câu để tách hai khái niệm: **"Swing point cũ đã bị PHÁ (sweep) hay vẫn GIỮ?"** — Bị phá → Breaker. Vẫn giữ → Mitigation Block.

---

## 1. Định nghĩa

**Khái niệm:**
Mitigation Block là một vùng order block sinh ra trong **bối cảnh failure swing** (nhịp swing thất bại). Sau một nhịp di chuyển bị thất bại, giá quay lại vùng order block để **mitigate** (giải tỏa / bù trừ) các vị thế đã kẹt từ nhịp đó. Điểm cốt lõi: trong cấu trúc tạo Mitigation Block, giá **KHÔNG quét** được đỉnh/đáy swing trước — swing point cũ **giữ vững** (failure to make a new low/high), sau đó một **displacement** + **Market Structure Shift (MSS)** xác nhận hướng mới. Cụm nến ngược chiều cuối cùng trước nhịp đẩy trở thành Mitigation Block — là POI để vào lệnh theo hướng mới khi giá retest.

![[Mitigation-Advanced-Anatomy.svg|697]]
*Giải phẫu bullish Mitigation Block: đáy cũ (STL) GIỮ VỮNG tạo higher low — không có sweep SSL — rồi displacement phá STH (MSS) khiến cụm nến giảm cuối cùng trở thành MB. Retest MB = Long, stop dưới higher low, target BSL. Hộp dưới là cấu trúc bearish MB đối xứng.*

**Cấu trúc Bullish Mitigation Block (để Long):**
1. Trong bối cảnh đang chuyển bullish, giá tạo một **đáy ngắn hạn (STL — Short-Term Low)** rồi rally lên một **đỉnh ngắn hạn (STH — Short-Term High)**.
2. Giá pullback xuống nhưng **THẤT BẠI không phá xuống dưới STL cũ** (tạo higher low — **KHÔNG có sweep** SSL; đáy cũ giữ vững).
3. Một **displacement tăng** đẩy giá lên **phá STH** → **MSS bullish** xác nhận.
4. Cụm **nến giảm (down-close)** cuối cùng trước nhịp đẩy lên trở thành **bullish mitigation block** — đóng vai trò hỗ trợ.
5. Giá retrace về vùng MB → **Long**; stop dưới vùng MB / dưới điểm thấp nhất của failure swing; target buyside liquidity phía trên.

**Cấu trúc Bearish Mitigation Block (để Short):** đối xứng — giá tạo **STH**, dip xuống **STL**, rồi rally lên nhưng **THẤT BẠI không phá lên trên STH cũ** (tạo lower high — **KHÔNG có sweep** BSL; đỉnh cũ giữ vững). Sau đó **displacement giảm** phá xuống dưới STL → **MSS bearish**. Cụm **nến tăng (up-close)** cuối cùng trước nhịp đẩy xuống trở thành **bearish mitigation block** (kháng cự) → **Short** khi retest; stop trên vùng MB / trên điểm cao nhất của failure swing; target sellside liquidity phía dưới.

**Phân biệt cốt lõi — Mitigation Block vs Order Block vs Breaker Block:**
- **[[25 - OB - Order Block|Order Block]]:** cụm nến ngược chiều cuối cùng TRƯỚC displacement trong một nhịp mới (chưa fail); entry theo hướng move ban đầu.
- **[[04 - BB - Breaker Block|Breaker Block]]:** OB ĐÃ fail; giá **đã quét liquidity** (phá đáy/đỉnh cũ) + displacement phá cấu trúc ngược; vùng đảo cực; entry theo hướng MỚI.
- **Mitigation Block:** cùng vị trí ý tưởng với breaker (vùng đảo chiều), nhưng **KHÔNG có sweep** — đỉnh/đáy cũ GIỮ VỮNG (failure swing), rồi MSS xác nhận. Giá quay lại "giải tỏa" lệnh kẹt từ nhịp thất bại.

![[Mitigation-Advanced-vs-Breaker.svg|697]]
*Phép thử sweep là dao mổ tách hai khái niệm: cùng một cấu trúc đảo chiều bullish, panel trái đáy cũ GIỮ (higher low, không sweep → Mitigation, stop dưới higher low) vs panel phải đáy cũ BỊ PHÁ (sweep SSL, Low2 < Low1 → Breaker, stop dưới điểm sweep). Chỉ khác "swing cũ bị phá hay giữ" nhưng quyết định toàn bộ SL logic.*

**Mục đích trong ICT:**
- Là **POI đảo chiều / tiếp diễn chất lượng cao** trong bối cảnh failure swing, khi thị trường KHÔNG cần quét liquidity vẫn đổi hướng.
- Cho **entry sớm hơn breaker** trong một số ngữ cảnh (vì không phải chờ sweep), nhưng đòi hỏi MSS xác nhận chắc.
- Là bằng chứng **phe cũ đã yếu**: giá không đủ lực tạo đáy/đỉnh mới (failure swing) trước khi đảo hướng.

**Vì sao khái niệm này quan trọng:**
Mitigation Block giúp đọc các điểm đảo chiều **không kèm sweep** mà nhiều trader bỏ lỡ vì cứ chờ "phải quét đáy/đỉnh". Nhưng nó cũng bị nhầm nhiều nhất với breaker: trader thấy đảo chiều rồi retest và gọi đại là "breaker/mitigation" mà không kiểm tra phép thử sweep, hoặc gọi mọi OB là mitigation block. Hiểu đúng giúp bạn chọn đúng SL logic và đúng narrative.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Đảo chiều này có sweep không? Nếu KHÔNG có sweep mà swing cũ giữ vững → đây là Mitigation Block, không phải Breaker.
- Vùng nến ngược chiều cuối cùng (MB) nằm ở đâu để retest và vào lệnh?
- Đây là failure swing thật (higher low / lower high) hay chỉ là pullback thường?
- Stop logic (ngoài extreme của failure swing) và target liquidity ở đâu?

### Mitigation Block không phải là gì
- **Không phải** Breaker — breaker có sweep, MB thì swing cũ giữ vững (không sweep). Phép thử sweep tách hai cái.
- **Không phải** mọi Order Block — MB sinh từ ngữ cảnh failure swing + đảo hướng, không phải OB của một nhịp tiếp diễn thường.
- **Không phải** tín hiệu độc lập — vẫn cần đúng [[12 - Daily Bias]] + [[27 - Premium Discount]] + MSS xác nhận + (lý tưởng) confluence FVG.
- **Không phải** lý do để bắt đỉnh/đáy khi chưa có MSS — failure swing chưa được MSS xác nhận thì chưa phải MB hợp lệ.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái của Mitigation Block

| Loại | Cấu trúc | Vai trò thực chiến |
|---|---|---|
| **Bullish Mitigation Block** | Higher low (KHÔNG sweep SSL) → displacement phá STH (MSS bullish) → cụm nến giảm cuối cùng | Hỗ trợ → tìm **Long** khi retest |
| **Bearish Mitigation Block** | Lower high (KHÔNG sweep BSL) → displacement phá STL (MSS bearish) → cụm nến tăng cuối cùng | Kháng cự → tìm **Short** khi retest |
| **MB + FVG** | MB trùng/đi kèm FVG của nhịp displacement | Confluence mạnh, entry refined |
| **HTF Mitigation Block** | MB hình thành trên D1/H4 | POI đảo chiều lớn, độ tin cậy cao |

> [!tip]
> Mitigation Block mạnh nhất khi vùng MB **trùng một [[Fair Value Gap]]** của chính nhịp displacement đã tạo MSS. Lúc đó bạn có MB + FVG + (failure swing + MSS) trong cùng một vùng — confluence rất cao, dù không có sweep.

![[Mitigation-Advanced-Block-Family.svg|697]]
*Họ Block dùng chung "nguyên liệu" (cụm nến ngược chiều + displacement) nhưng khác bối cảnh: [[25 - OB - Order Block|Order Block]] = nhịp tiếp diễn chưa fail; Mitigation Block = failure swing nhưng KHÔNG sweep; [[04 - BB - Breaker Block|Breaker Block]] = failure swing CÓ sweep. Bảng dưới tóm tắt failure swing / sweep / hướng entry / SL logic của cả ba.*

### Khi nào khái niệm này có giá trị cao?
- [ ] Có **failure swing** rõ: higher low (bullish) / lower high (bearish) — swing cũ KHÔNG bị phá.
- [ ] Có **displacement + MSS** xác nhận hướng mới rõ ràng.
- [ ] MB đồng hướng [[12 - Daily Bias]] sau khi cấu trúc đã đổi/tiếp diễn.
- [ ] Vùng MB nằm đúng **discount** (bullish MB) / **premium** (bearish MB) — xem [[27 - Premium Discount]].
- [ ] MB trùng/đi kèm **FVG** của nhịp displacement.
- [ ] Có target liquidity rõ ở phía hướng mới.

### Khi nào nên bỏ qua?
- [ ] Thực ra có **sweep** đáy/đỉnh cũ → đó là [[04 - BB - Breaker Block|Breaker]], dùng logic breaker, không phải MB.
- [ ] Không có **MSS** rõ — chỉ là pullback thường, chưa xác nhận hướng.
- [ ] MB ngược bias mà cấu trúc HTF chưa thực sự đổi.
- [ ] Vùng MB ở sai premium/discount cho hướng vào.
- [ ] Giá đã chạy xa khỏi MB — retest thành chase.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Failure swing:** giá tạo higher low (bullish) / lower high (bearish) — swing point cũ **giữ vững**, KHÔNG có sweep.
2. **OB ngược chiều:** cụm nến giảm (bullish MB) / nến tăng (bearish MB) cuối cùng trước nhịp đẩy.
3. **Displacement + MSS:** một nhịp mạnh phá STH (bullish) / STL (bearish) xác nhận hướng mới.
4. **Mitigation zone:** vùng nến ngược chiều cuối cùng = MB, là nơi giá quay lại "giải tỏa" lệnh kẹt.
5. **Retest:** giá quay lại test vùng MB → điểm vào lệnh.

### Ma trận nhận diện Mitigation Block

| Thành phần | Bullish MB (→ Long) | Bearish MB (→ Short) | Cảnh báo / không phải MB |
|---|---|---|---|
| **Phép thử sweep** | KHÔNG sweep SSL; higher low (đáy cũ giữ) | KHÔNG sweep BSL; lower high (đỉnh cũ giữ) | Có sweep → đó là Breaker |
| **Displacement/MSS** | Đẩy lên phá STH (MSS bullish) | Đẩy xuống phá STL (MSS bearish) | Chỉ pullback, không MSS |
| **Vùng OB** | Cụm nến giảm cuối cùng → hỗ trợ | Cụm nến tăng cuối cùng → kháng cự | OB của nhịp tiếp diễn thường |
| **Location** | Discount của dealing range | Premium của dealing range | Sai phía |
| **Bias** | Đồng hướng bias bullish | Đồng hướng bias bearish | Ngược bias chưa đổi |

### Điều kiện bắt buộc (must-have)
- [ ] Xác định **failure swing** (higher low / lower high) — xác nhận swing cũ KHÔNG bị quét.
- [ ] Có **displacement + MSS** phá cấu trúc theo hướng mới.
- [ ] Xác định **cụm nến ngược chiều cuối cùng** (vùng MB) và mức invalidation.
- [ ] Đặt trong bối cảnh [[12 - Daily Bias]] / [[27 - Premium Discount]].

### Điều kiện tăng xác suất (nice-to-have)
- [ ] MB trùng **FVG** của nhịp displacement.
- [ ] MB đúng premium/discount cho hướng vào.
- [ ] Đồng hướng [[12 - Daily Bias]] sau khi cấu trúc đã đổi.
- [ ] HTF MB (D1/H4) làm khung lớn, LTF refine entry.
- [ ] Có target liquidity rõ; R:R đạt kế hoạch.

### Điều kiện làm setup yếu đi (warning)
- Failure swing mờ nhạt (không rõ là higher low / lower high hay là sweep).
- MSS yếu (chỉ phá một chút, không displacement).
- MB đã bị test nhiều lần, ăn mòn.
- Vùng MB quá rộng, không xác định được entry/stop rõ.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Mitigation Block
> 1. **Đáy/đỉnh swing cũ đã bị PHÁ (sweep) hay vẫn GIỮ?** Nếu giữ (higher low / lower high) → đang xét MB, không phải breaker.
> 2. **Đã có displacement + MSS xác nhận hướng mới chưa?**
> 3. **Vùng MB có đúng premium/discount + đồng hướng bias không?**
> 4. **Stop (ngoài extreme của failure swing) và target liquidity ở đâu, R:R bao nhiêu?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại / đang đổi:** MB thường xuất hiện tại điểm cấu trúc HTF chuyển hướng hoặc tiếp diễn sau failure swing (xem [[12 - Daily Bias]]).
- **Liquidity HTF:** pool nào CHƯA bị quét (vì MB không có sweep); pool nào là target hướng mới.
- **Vị trí premium/discount:** bullish MB cần ở discount; bearish MB cần ở premium.

### H1 / M15 — POI & Context
- **Xác định MB cụ thể:** ghi vùng MB H1/M15, ví dụ `bullish MB 1.0840–1.0855 sau higher low (không sweep) + MSS phá STH 1.0890`.
- **Confluence:** MB có trùng FVG của nhịp displacement không?
- **Trạng thái:** vùng MB còn unmitigated chưa, đã bị retest mấy lần?

### M5 / M1 — Confirmation & Entry
- **Retest + LTF confirm:** chờ giá retrace về vùng MB; M5/M1 cho phản ứng (reject) hoặc MSS nhỏ.
- **Entry:** tại mép / Mean Threshold của MB, hoặc tại FVG trùng vùng. Lý tưởng entry ở discount (bullish) / premium (bearish) — kết hợp [[Optimal Trade Entry]].
- **Stop loss logic:** ngoài vùng MB / ngoài extreme của failure swing (dưới higher low cho bullish, trên lower high cho bearish).
- **Target:** liquidity phía hướng mới (BSL cho bullish MB, SSL cho bearish MB).

```text
[LONG SETUP — Bullish Mitigation Block]
- HTF Bias: Bullish | Location: Discount
- Failure swing: higher low (KHÔNG sweep SSL) — đáy cũ giữ vững [level]
- OB cũ (cụm nến giảm cuối cùng): [range]
- MSS: displacement tăng phá STH tại [level]
- MB zone: [low]–[high]; confluence FVG? Yes/No
- Entry: retest vùng MB + M5 confirm   SL: dưới higher low / dưới MB [level]
- TP1: internal liquidity [level]   TP2: BSL phía trên [level]
- RR dự kiến: ____
- Invalid: đóng nến lại dưới MB + dưới higher low
```

```text
[SHORT SETUP — Bearish Mitigation Block]
- HTF Bias: Bearish | Location: Premium
- Failure swing: lower high (KHÔNG sweep BSL) — đỉnh cũ giữ vững [level]
- OB cũ (cụm nến tăng cuối cùng): [range]
- MSS: displacement giảm phá STL tại [level]
- MB zone: [low]–[high]; confluence FVG? Yes/No
- Entry: retest vùng MB + M5 confirm   SL: trên lower high / trên MB [level]
- TP1: internal liquidity [level]   TP2: SSL phía dưới [level]
- RR dự kiến: ____
- Invalid: đóng nến lại trên MB + trên lower high
```

> [!warning]
> **Mitigation Block không phải lý do để bắt đỉnh/đáy sớm.** Nó chỉ hợp lệ SAU khi failure swing + MSS đã xảy ra. Nếu thực ra có sweep, đừng gọi MB — đó là [[04 - BB - Breaker Block|Breaker]], và SL logic khác (ngoài điểm sweep).

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi (✓)
- [ ] Có **failure swing** rõ: higher low (bullish) / lower high (bearish) — swing cũ KHÔNG bị sweep.
- [ ] Có **displacement + MSS** phá cấu trúc theo hướng mới.
- [ ] Vùng MB đúng premium/discount + đồng hướng bias.
- [ ] (Lý tưởng) MB trùng FVG của nhịp displacement.
- [ ] Giá retest vùng MB và respect (reject) + LTF confirm.
- [ ] Stop ngoài extreme failure swing; target liquidity rõ; R:R đạt kế hoạch.

### Setup bị vô hiệu khi (✗)
- [ ] Hóa ra có **sweep** đáy/đỉnh cũ → không phải MB (đó là breaker; xét lại logic).
- [ ] Không có **MSS** → chỉ là pullback, chưa xác nhận hướng.
- [ ] Giá **đóng nến xuyên qua** vùng MB và đi tiếp (MB fail).
- [ ] MB ngược bias mà cấu trúc HTF chưa đổi.
- [ ] Vùng MB ở sai premium/discount cho hướng vào.
- [ ] Giá đã chạy quá xa, retest thành chase.

### Mitigation Block vs Breaker vs OB thường

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Swing cũ GIỮ (higher low/lower high), không sweep, MSS xác nhận | **Mitigation Block** | Entry theo hướng mới, SL ngoài extreme failure swing |
| Swing cũ BỊ PHÁ (sweep liquidity), MSS đảo cực | **Breaker Block** | Entry theo hướng mới, SL ngoài điểm sweep |
| Cụm nến trước displacement của nhịp tiếp diễn (chưa fail) | **Order Block** | Dùng OB bình thường theo hướng move gốc |
| "MB/Breaker" không có MSS, giá xuyên qua | **Không phải POI** | Bỏ; đó là pullback / level thường |

> [!note]
> Mitigation Block và **[[04 - BB - Breaker Block|Breaker Block]]** rất giống nhau về vị trí và vai trò — khác biệt nằm ở **một phép thử duy nhất: có sweep hay không**. Breaker = swing cũ bị phá (sweep) rồi đảo cực. MB = swing cũ giữ vững (failure to make new low/high) rồi MSS. Đừng dùng chung; SL logic khác nhau.

### Nâng cao — Phép thử sweep chi tiết: khi nào một "higher low" thực ra là một sweep vi mô

Phép thử sweep nghe đơn giản ("đáy cũ giữ hay bị phá?") nhưng trên chart LTF nó thường mờ. Vấn đề nằm ở **cơ sở đo**: một higher low thật được đo bằng **body/close**, còn một sweep vi mô chỉ là **wick** thò xuống dưới đáy cũ vài tick rồi kéo lại. Nhầm hai cái này khiến bạn gọi sai POI và đặt sai stop.

Ba câu hỏi để tách "higher low thật" khỏi "sweep trá hình":

1. **Wick hay body xuyên đáy cũ?** Nếu chỉ có wick xuyên nhẹ rồi đóng nến TRÊN đáy cũ → đó vẫn là *raid/sweep* (đã lấy thanh khoản dưới đáy) → hành xử như [[04 - BB - Breaker Block|Breaker]], stop dưới đáy wick, không phải MB. Nếu cả nến (kể cả wick) **không chạm** đáy cũ và tạo đáy cao hơn hẳn → higher low thật → MB hợp lệ.
2. **Có cụm stop rõ dưới đáy cũ không?** Nếu đáy cũ là equal lows / một đáy được nhiều người theo dõi, khả năng cao thị trường sẽ raid nó — một "higher low" ngay sát trên đó thường chỉ là bẫy trước khi sweep thật. Đợi thêm.
3. **Khoảng cách higher low tới đáy cũ có "đủ sạch" không?** Higher low cách đáy cũ một biên độ rõ (không dính sát vài tick) là dấu hiệu failure swing thật; higher low dính sát mép đáy cũ dễ bị nhịp sau quét nốt.

| Quan sát tại đáy | Phân loại | POI / SL logic |
|---|---|---|
| Body + wick đều KHÔNG chạm đáy cũ, đáy cao hơn rõ | **Higher low thật → Mitigation** | MB; stop dưới higher low |
| Wick thò dưới đáy cũ, body đóng TRÊN đáy cũ | **Sweep vi mô → Breaker** | Breaker; stop dưới đáy wick (điểm sweep) |
| Body đóng DƯỚI đáy cũ rồi mới đảo | **Sweep rõ → Breaker** | Breaker; stop dưới điểm sweep |
| Đáy cũ là equal lows, "higher low" dính sát | **Nghi ngờ bẫy** | Đợi — có thể raid nốt trước khi đảo thật |

> [!tip]
> Ghi lại `sweep_test` cho từng lệnh trong journal: `held` (higher low/lower high thật → MB) hay `swept` (wick/body xuyên → Breaker). Sau 20–30 mẫu bạn sẽ thấy mình nhầm về hướng nào nhiều hơn và win-rate của mỗi nhãn khác nhau ra sao.

### Nâng cao — MB vs Breaker: chọn cái nào, và SL logic ảnh hưởng R:R ra sao

Vì MB và Breaker chỉ khác nhau ở phép thử sweep, **bạn không "chọn" — chart chọn hộ**. Đáy/đỉnh cũ giữ → MB; bị phá → Breaker. Nhưng hệ quả thực chiến thì rất khác, đặc biệt ở **SL logic** và do đó **R:R**:

- **MB cho stop gần hơn.** Stop nằm dưới higher low (bullish) / trên lower high (bearish) — mà higher low nằm *cao hơn* đáy cũ. Vì swing không bị quét, khoảng cách entry→stop ngắn hơn → **R:R lớn hơn** với cùng target.
- **Breaker cho stop xa hơn nhưng an toàn hơn trước raid.** Stop dưới điểm sweep — thanh khoản dưới đó đã bị lấy, nên xác suất bị quét lần nữa thấp hơn. Đổi lại R:R nhỏ hơn.
- **Hệ quả tâm lý:** MB dễ cám dỗ đặt stop quá sát (vì trông "gần"); nếu thực ra đó là sweep vi mô, stop sát bị quét ngay. Đây chính là lỗi ở "Ví dụ sai" mục 6.

| Tiêu chí | Mitigation Block | Breaker Block |
|---|---|---|
| Điều kiện kích hoạt | Đáy/đỉnh cũ GIỮ (higher low / lower high) | Đáy/đỉnh cũ BỊ PHÁ (sweep) |
| Vị trí SL | Dưới higher low / trên lower high | Dưới điểm sweep (Low2) / trên điểm sweep (High2) |
| Khoảng cách entry→SL | Ngắn hơn | Dài hơn |
| R:R (cùng target) | Cao hơn | Thấp hơn |
| Rủi ro bị quét lại | Cao hơn (thanh khoản dưới chưa bị lấy) | Thấp hơn (đã sweep) |
| Khi nào ưu tiên đi hẳn | Failure swing sạch + FVG confluence | Sau raid rõ vào pool có ý nghĩa (PDL/equal lows) |

> [!warning]
> Đừng "ép" một Breaker thành MB để có R:R đẹp hơn. Nếu đáy cũ đã bị sweep, thanh khoản dưới higher-low-giả vẫn còn nguyên và dễ bị quét — R:R đẹp trên giấy nhưng win-rate thấp. Log cả hai nhãn riêng và so win-rate × R trung bình trước khi kết luận cái nào hợp phong cách bạn.

### Nâng cao — Mitigation trong tiếp diễn trend (không chỉ đảo chiều)

MB thường được dạy như một POI **đảo chiều**, nhưng trong một trend đang chạy, cùng cấu trúc failure swing xuất hiện ở quy mô nhỏ hơn để cho **entry tiếp diễn** (continuation). Trong một uptrend HTF: giá pullback tạo một failure swing nhỏ (higher low, không sweep các đáy nội bộ), rồi displacement + MSS nội bộ đẩy tiếp lên — cụm nến giảm cuối cùng của pullback đó là một **bullish MB tiếp diễn**, đồng hướng trend lớn.

Điểm khác biệt và lưu ý:

- **Bias là bạn, không phải kẻ thù.** MB tiếp diễn đồng hướng HTF bias → xác suất cao hơn MB đảo chiều (vốn cắt ngang delivery HTF). Ưu tiên loại này khi mới học MB.
- **"MSS" ở đây là internal shift của leg pullback**, không phải MSS đảo cả HTF. Đừng dùng nó để tuyên bố trend đã đổi.
- **Vị trí vẫn quan trọng:** MB tiếp diễn bullish vẫn nên nằm ở discount của *dealing range nội bộ* (pullback), không phải mua đuổi ở đỉnh.
- **Đừng nhầm với đảo chiều:** nếu failure swing xuất hiện tại một HTF premium (cho uptrend) kèm sweep BSL, đó có thể là tín hiệu đảo chiều/breaker, không phải MB tiếp diễn.

| Ngữ cảnh | MB đảo chiều | MB tiếp diễn |
|---|---|---|
| Quan hệ với HTF bias | Cắt ngang / chuyển hướng | Đồng hướng |
| "MSS" đo trên | Cấu trúc đảo hướng chính | Internal shift của leg pullback |
| Vị trí lý tưởng | Cuối một leg đối nghịch, tại HTF POI | Discount/premium của range pullback nội bộ |
| Xác suất tương đối | Thấp hơn (counter-delivery) | Cao hơn (theo delivery) |
| Rủi ro nhầm lẫn | Bị coi là tiếp diễn khi trend chưa đổi | Bị coi là đảo chiều → đặt target ngược trend |

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish Mitigation Block: higher low (không sweep) + MSS, retest, Long
![[MitigationBlock-Example-Correct.svg|697]]

**Mô tả:**
Giá tạo STL rồi rally lên STH (đoạn tạo đỉnh có cụm nến giảm = OB cũ). Sau đó giá pullback nhưng **THẤT BẠI không phá xuống dưới STL** (tạo higher low — **KHÔNG có sweep SSL**, đáy cũ giữ vững). Một **displacement tăng** đẩy giá lên **phá STH** (MSS bullish), khiến cụm nến giảm cuối cùng trở thành **bullish mitigation block** (hỗ trợ). Giá retrace về vùng MB, reject; Long tại đó; stop dưới higher low / dưới vùng MB; target BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- Có đủ chuỗi **failure swing (higher low, không sweep) → displacement → MSS** trước khi gọi là MB.
- Vùng MB ở **discount**, đồng hướng bias bullish.
- Entry tại retest, stop logic ngoài extreme của failure swing.
- Target là liquidity rõ ràng (BSL).

### Ví dụ sai / dễ nhầm — Gọi một breaker (có sweep) là "mitigation block"
![[MitigationBlock-Example-Wrong.svg|697]]

**Mô tả lỗi:**
Trader thấy giá đảo chiều và retest, gắn nhãn "mitigation block" rồi đặt stop sát mép vùng. Nhưng thực ra trước đó giá **đã quét xuống dưới đáy cũ** (sweep SSL) — đây là một **Breaker**, không phải MB. Vì gọi sai, trader đặt stop quá sát (theo logic MB) thay vì dưới điểm sweep, nên bị quét stop dù hướng đúng.

**Bài học:**
- Luôn chạy **phép thử sweep** trước: đáy/đỉnh cũ bị phá hay giữ vững?
- Nếu có sweep → là Breaker → stop dưới điểm sweep, không phải dưới mép MB.
- Đừng gắn nhãn POI tùy tiện; tên gọi quyết định SL logic.

### Giải phẫu Mitigation Block
![[MitigationBlock-Anatomy.svg|697]]

**Mô tả:** Sơ đồ chú thích STL/STH, failure swing (higher low / lower high, không sweep), cụm nến ngược chiều cuối cùng (vùng MB), điểm MSS, và vùng retest để vào lệnh.

---

![[Mitigation-Advanced-Sequence-Chain.svg|697]]
*MB không đứng một mình — nó là một mắt xích trong chuỗi ICT: HTF Bias/Discount → failure swing (higher low, KHÔNG sweep) → displacement + MSS → cụm nến ngược = MB → retest (lý tưởng trùng FVG) → entry → target BSL. So với chuỗi Breaker, khác biệt duy nhất nằm ở bước ② (đáy cũ giữ thay vì bị sweep).*

### Sequence mẫu — Long từ Bullish Mitigation Block
```text
HTF Bias Bullish + Location Discount
→ STL → rally STH (cụm nến giảm = OB cũ)
→ Pullback FAILS không phá STL (higher low, KHÔNG sweep)
→ Displacement tăng phá STH (MSS bullish) → tạo FVG
→ Cụm nến giảm cuối cùng = Bullish Mitigation Block (hỗ trợ)
→ Giá retrace về MB (lý tưởng trùng FVG, ở discount)
→ M5/M1 confirm → Entry
→ Stop dưới higher low / dưới MB
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short từ Bearish Mitigation Block
```text
HTF Bias Bearish + Location Premium
→ STH → dip STL (cụm nến tăng = OB cũ)
→ Rally FAILS không phá STH (lower high, KHÔNG sweep)
→ Displacement giảm phá STL (MSS bearish) → tạo FVG
→ Cụm nến tăng cuối cùng = Bearish Mitigation Block (kháng cự)
→ Giá retrace về MB (lý tưởng trùng FVG, ở premium)
→ M5/M1 confirm → Entry
→ Stop trên lower high / trên MB
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> Mitigation Block hoạt động mạnh nhất khi đóng vai trò **POI trong khung của [[ICT 2022 Model]]** — nhưng với một khác biệt then chốt so với breaker: thay vì chờ sweep, ta xác nhận bằng **failure swing + MSS**. Nếu vùng đó trùng một [[Fair Value Gap]] thì confluence càng mạnh.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Mitigation Block chỉ là POI sau khi failure swing + MSS đã rõ. Không đủ mục A + B → **không có lệnh**.

### A. Context (HTF)
- [ ] [[12 - Daily Bias]] đã rõ / vừa chuyển hướng: `Bullish / Bearish`.
- [ ] Đã có **failure swing**: higher low (bullish) / lower high (bearish) — xác nhận swing cũ KHÔNG bị sweep.
- [ ] Đã có **displacement + MSS** phá cấu trúc theo hướng mới.
- [ ] Vùng MB đúng discount (bullish) / premium (bearish).
- [ ] Có draw on liquidity rõ làm target.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá retest vùng MB và respect (reject).
- [ ] (Lý tưởng) MB trùng FVG của nhịp displacement.
- [ ] LTF có phản ứng / MSS nhỏ xác nhận.
- [ ] Entry tại mép / Mean Threshold MB hoặc FVG trùng vùng.
- [ ] Stop ngoài extreme failure swing (dưới higher low / trên lower high) / ngoài MB.
- [ ] Target liquidity rõ; R:R tối thiểu đạt kế hoạch.
- [ ] Risk ≤ 0.5% theo khung rủi ro.

### C. Quy tắc "không có lệnh"
- [ ] Hóa ra có sweep đáy/đỉnh cũ → không phải MB (xét lại như breaker).
- [ ] Không có MSS rõ → không trade.
- [ ] MB ngược bias chưa đổi → không trade.
- [ ] Sai premium/discount → không trade.
- [ ] Giá đã đóng nến xuyên qua MB (fail) → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Nhầm MB với Breaker | Gọi mọi đảo chiều + retest là "mitigation/breaker" | Sai SL logic (stop quá sát) → bị quét | Chạy phép thử sweep: swing cũ phá hay giữ? |
| Gọi mọi OB là MB | Gắn nhãn "mitigation" cho OB của nhịp tiếp diễn thường | Vào sai ngữ cảnh, không có failure swing | Chỉ gọi MB khi có failure swing + đảo hướng |
| Vào khi chưa có MSS | Thấy higher low/lower high là vào ngay | Pullback chưa xác nhận, dễ tiếp diễn hướng cũ | Bắt buộc displacement + MSS mới gọi MB |
| Trade ngược bias chưa đổi | Bắt đỉnh/đáy khi HTF chưa chuyển | Xác suất thấp | Chỉ vào khi đồng hướng bias + cấu trúc đã đổi |
| Bỏ qua premium/discount | Bullish MB ở premium / bearish MB ở discount | R:R xấu, entry chase | Bullish MB ở discount, bearish ở premium |
| Stop quá sát | Stop trong vùng MB | Bị quét dễ dàng | Stop ngoài extreme failure swing / ngoài MB |
| Giữ lệnh khi MB fail | Giá đóng nến xuyên qua mà vẫn ôm | Tiếp diễn hướng cũ | Cắt khi đóng nến xuyên MB + xuyên failure swing |
| Thiếu LTF confirm | Vào "mù" tại mép MB không chờ phản ứng | Dễ bắt dao rơi | Chờ reject / MSS nhỏ trên M5/M1 |

---

## 10. Câu hỏi tự kiểm tra
- Mình có phân biệt được Mitigation Block và Breaker Block trong 30 giây bằng phép thử sweep không?
- Đáy/đỉnh swing cũ ở đây đã bị PHÁ hay vẫn GIỮ?
- Đây là bullish hay bearish MB, và nó ở premium hay discount?
- Failure swing này (higher low / lower high) đã được MSS xác nhận chưa?
- MB có trùng FVG của nhịp displacement không?
- Stop (ngoài extreme failure swing) và target (liquidity) ở đâu, R:R bao nhiêu?
- Điều gì làm MB này fail?
- Nếu không trade MB này, lý do "No Trade" là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Mitigation Block là gì?
**Đáp:** Là order block hình thành từ một failure swing — giá KHÔNG quét được đỉnh/đáy cũ (swing giữ vững, không sweep), sau đó displacement + MSS xác nhận hướng mới; cụm nến ngược chiều cuối cùng trở thành POI để giá quay lại giải tỏa (mitigate) lệnh kẹt.

### Q2
**Hỏi:** Điều DUY NHẤT phân biệt Mitigation Block với Breaker Block là gì?
**Đáp:** Phép thử sweep. Breaker = swing cũ BỊ PHÁ (có sweep liquidity) rồi đảo cực. MB = swing cũ GIỮ VỮNG (higher low / lower high, KHÔNG sweep) rồi MSS xác nhận.

### Q3
**Hỏi:** Cấu trúc một Bullish Mitigation Block gồm những bước nào?
**Đáp:** STL → rally STH (OB cũ) → pullback FAILS không phá STL (higher low, không sweep) → displacement tăng phá STH (MSS) → cụm nến giảm cuối cùng = bullish MB → retest = Long.

### Q4
**Hỏi:** Khác biệt giữa Order Block và Mitigation Block?
**Đáp:** OB = cụm nến trước displacement của một nhịp tiếp diễn (chưa fail), entry theo hướng gốc. MB = sinh từ ngữ cảnh failure swing + đảo hướng (không sweep), entry theo hướng mới.

### Q5
**Hỏi:** Đặt stop cho một Bullish Mitigation Block ở đâu?
**Đáp:** Ngoài extreme của failure swing — dưới higher low — hoặc dưới vùng MB.

### Q6
**Hỏi:** Confluence nào làm MB mạnh hơn?
**Đáp:** Khi vùng MB trùng một FVG của chính nhịp displacement đã tạo MSS, đúng premium/discount, và đồng hướng bias.

### Q7
**Hỏi:** Khi nào một Mitigation Block bị vô hiệu?
**Đáp:** Khi hóa ra có sweep (không phải MB, là breaker), khi không có MSS, hoặc khi giá đóng nến xuyên qua vùng MB và tiếp tục theo hướng cũ.

---

## 12. Lesson Learned

### Bài học chính
- MB = order block sinh từ **failure swing** (swing cũ giữ vững, KHÔNG sweep) + MSS xác nhận.
- **Phép thử sweep** là dao mổ tách MB khỏi [[04 - BB - Breaker Block|Breaker]]: phá = breaker, giữ = MB.
- MB cho entry theo **hướng mới**, mạnh nhất khi trùng **FVG** + đúng **premium/discount** + đồng hướng bias.
- Stop nằm ngoài **extreme của failure swing**; target là liquidity phía hướng mới.
- Đừng gọi mọi OB là "mitigation block".

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn chạy phép thử sweep trước khi gắn nhãn MB hay breaker.
- [ ] Tôi chỉ gọi MB khi có failure swing (higher low / lower high) + MSS rõ.
- [ ] Tôi chỉ vào MB đồng hướng bias và đúng premium/discount.
- [ ] Tôi ưu tiên MB trùng FVG để có confluence.
- [ ] Tôi đặt stop ngoài extreme failure swing và cắt khi giá đóng nến xuyên MB.

### Câu nhắc nhở khi trade
> **"Breaker quét rồi đảo; Mitigation giữ rồi đảo. Hỏi một câu — đáy/đỉnh cũ bị phá hay vẫn giữ? — trước khi đặt tên và đặt stop."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt MB vs Breaker vs OB bằng phép thử sweep không? |
| Nhận diện trên chart |  | Có xác định đúng failure swing (không sweep) → MSS không? |
| Biết khi nào bỏ qua |  | Có dám bỏ "MB" thiếu MSS / thực ra có sweep không? |
| Kết hợp với context HTF |  | MB có đặt trong bias + premium/discount không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự tại retest vùng MB, SL ngoài failure swing không? |
| Review sau trade |  | Có kiểm tra bằng dữ liệu journal thay vì cảm tính không? |

**Kế hoạch review tiếp theo:**
- [ ] Backtest 20–30 setup có tag `[[Mitigation Block]]` trên NQ1/NAS100 & EURUSD.
- [ ] Review riêng: MB có failure swing rõ vs mờ; có/không FVG confluence.
- [ ] So sánh win rate MB vs Breaker để hiểu khi nào dùng cái nào.
- [ ] Đối chiếu với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]].
- [ ] Review lại note này sau 2 tuần, cập nhật `confidence` & `last_reviewed`.

---

## 14. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
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
> Nếu vault của bạn có folder riêng như `Trades`, `Journal`, hoặc `Trading Journal`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

---

## 15. Best Practices

> [!success] Nguyên tắc vàng
> **"Breaker quét rồi đảo; Mitigation giữ rồi đảo."** Trước khi đặt tên cho một vùng đảo chiều, chạy đúng MỘT phép thử: đáy/đỉnh swing cũ đã bị PHÁ (sweep) hay vẫn GIỮ (higher low / lower high)? Câu trả lời quyết định cả tên gọi lẫn vị trí stop — và đó là nơi phần lớn lệnh thua "đúng hướng nhưng sai stop" được sinh ra.

1. **Luôn chạy phép thử sweep TRƯỚC khi gắn nhãn.** Đừng gọi một vùng là "mitigation" chỉ vì thấy đảo chiều + retest. Kéo mức đáy/đỉnh swing cũ ra và hỏi: giá có đóng/wick xuyên qua nó không? Nếu có sweep → đây là [[04 - BB - Breaker Block|Breaker]] (stop dưới điểm sweep); nếu swing giữ vững → mới là MB (stop dưới higher low / trên lower high). Ghi trường `sweep_test: held|swept` vào journal cho mỗi lệnh để sau này lọc thống kê.

2. **Chỉ tin MB sau khi displacement + MSS xác nhận, không phải khi vừa thấy failure swing.** Một higher low đơn thuần chỉ là pullback; nó chỉ trở thành nền của MB khi có một nhịp displacement phá STH/STL kèm MSS. Vào lệnh tại failure swing khi chưa có MSS là bắt dao rơi — phần lớn các lệnh MB thua trong journal sẽ rơi vào nhóm "chưa có MSS".

3. **Phân biệt failure swing thật với sweep vi mô (micro-sweep).** Một "higher low" trên khung lớn đôi khi thực chất đã quét một micro liquidity pool trên khung nhỏ hơn. Soi M1/M5 để xác nhận đáy cũ thực sự GIỮ chứ không bị wick lấy thanh khoản. Nếu có micro-sweep, hãy đọc setup theo logic breaker và dời stop ra ngoài điểm micro-sweep để tránh bị quét.

4. **Ưu tiên MB trùng FVG của chính nhịp displacement.** Confluence mạnh nhất là khi vùng MB (cụm nến ngược chiều cuối) chồng lên FVG do nhịp phá cấu trúc để lại. Lúc đó bạn có failure swing + MSS + FVG trong một vùng — entry refine quanh CE/[[26 - OTE - Optimal Trade Entry|OTE]] cho R:R tốt hơn nhiều so với vào cả vùng MB rộng.

5. **Đặt stop theo extreme của failure swing, không theo mép MB.** Đây là khác biệt SL cốt lõi so với breaker. Với bullish MB, stop nằm dưới higher low (extreme của failure swing), không phải sát mép dưới vùng MB. Stop sát mép MB là lỗi kinh điển khiến lệnh bị quét bởi nhiễu trước khi giá đi đúng hướng.

6. **Chờ LTF confirmation tại retest — đừng vào "mù" tại mép.** Khi giá quay lại vùng MB, chờ một phản ứng M5/M1 (reject rõ hoặc một MSS nhỏ) rồi mới vào. Điều này lọc bỏ các lần giá xuyên thẳng qua MB (MB fail) và giữ bạn đứng ngoài khi vùng đã mất hiệu lực (giá đóng nến xuyên MB + xuyên extreme failure swing).

7. **Backtest MB và Breaker song song để biết khi nào dùng cái nào.** Đừng gộp chung "vùng đảo chiều". Gắn tag phân biệt và so sánh win rate / average R của MB (no-sweep) vs Breaker (sweep) trên NQ1/NAS100 và EURUSD qua 20–30 mẫu mỗi loại ([[04 - Backtesting]]). Nhiều trader phát hiện breaker (có sweep + MSS) ổn định hơn MB trong một số sản phẩm/phiên — chỉ dữ liệu của chính bạn mới trả lời được, và nó biến "cảm giác" thành quy tắc.

---

## Appendix — Mitigation Block Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish
> **Loại MB:** Bullish / Bearish
> **Phép thử sweep:** Swing cũ GIỮ (higher low / lower high) — KHÔNG sweep ✓ (nếu có sweep → là Breaker, dừng lại)
> **Failure swing tại:** [level]
> **OB cũ (cụm nến ngược chiều) range:** [range]
> **MSS phá cấu trúc tại:** [level]
> **MB zone:** [low]–[high]
> **Confluence FVG?** Yes / No
> **Location:** Premium / Discount
> **Entry plan (retest):** ____
> **Stop (ngoài extreme failure swing):** [level]
> **Target (liquidity hướng mới):** [level]
> **R:R dự kiến:** ____
> **Kill zone permitted:** London / NY AM / NY PM
> **Invalidation (đóng nến xuyên MB tại):** [level]
> **No-trade condition:** có sweep → breaker / không MSS / sai premium-discount
> **Liên quan:** [[25 - OB - Order Block]] · [[04 - BB - Breaker Block]] · [[Fair Value Gap]] · [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[27 - Premium Discount]] · [[12 - Daily Bias]] · [[ICT 2022 Model]]
