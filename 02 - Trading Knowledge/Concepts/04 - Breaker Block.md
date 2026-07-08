---
type: ict-concept
concept: Breaker Block
aliases:
  - BB
  - Breaker Block
  - Breaker
  - Bullish Breaker
  - Bearish Breaker
tags:
  - trading/ict/concept
  - trading/study
  - "#BreakerBlock"
status: developing
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
importance: 5
last_reviewed: 2026-07-08
created: 2026-06-22
updated: 2026-07-08
common_mistakes:
  - "[[Mistake - Confuse OB with Breaker Block]]"
  - "[[Mistake - Breaker Without Sweep]]"
  - "[[Mistake - Breaker Without MSS]]"
---

# Breaker Block (BB)

> [!summary] Tóm tắt 1 câu
> **Breaker Block là một Order Block ĐÃ THẤT BẠI: khi giá quét liquidity rồi displacement phá cấu trúc ngược lại, vùng OB cũ đảo cực và trở thành hỗ trợ/kháng cự cho hướng mới — là POI để vào lệnh theo hướng đảo chiều.**

> [!important] Nguyên tắc cốt lõi
> **Một vùng chỉ là Breaker khi có đủ chuỗi: liquidity sweep → displacement phá cấu trúc (MSS) → vùng OB cũ bị "phá vai trò" rồi retest. Thiếu sweep hoặc thiếu MSS thì đó chỉ là một OB/level thường, không phải breaker.**
> Breaker = OB fail + flip polarity. Không phải "cứ thấy giá break một level rồi retest là breaker".

---

## 1. Định nghĩa

**Khái niệm:**
Breaker Block là vùng giá hình thành từ một **Order Block thất bại**. Trong cấu trúc tạo swing, có một OB (vùng nến trước một nhịp đẩy). Khi thị trường **quét liquidity** ở phía OB đó rồi **displacement phá cấu trúc theo hướng ngược lại** (MSS), OB cũ mất vai trò ban đầu và **đảo cực (flip polarity)**: vùng từng là kháng cự trở thành hỗ trợ, hoặc ngược lại. Khi giá quay lại **retest** vùng này, nó trở thành POI để vào theo hướng mới.

**Cấu trúc Bullish Breaker (để Long):**
1. Giá tạo một đáy (Low1) rồi rally lên một đỉnh (High1) — trong đoạn tạo đỉnh có cụm **nến giảm** (đây sẽ là vùng breaker).
2. Giá quay xuống và **quét xuống dưới Low1** (sweep SSL — lấy sell-side liquidity, tạo Low2 < Low1).
3. Một **displacement tăng** đẩy giá lên **phá High1** (MSS bullish).
4. Cụm nến giảm gần High1 (OB cũ thất bại) đảo cực thành **bullish breaker** — là hỗ trợ.
5. Giá retrace về vùng breaker → **Long**; stop dưới vùng / dưới Low2; target BSL phía trên.

**Cấu trúc Bearish Breaker (để Short):** đối xứng — giá tạo High1 → rally tạo... thực chất: tạo một đỉnh, pullback, rồi quét **trên một đỉnh cũ** (sweep BSL), sau đó **displacement giảm phá đáy** (MSS bearish); cụm **nến tăng** gần đáy cũ đảo cực thành **bearish breaker** (kháng cự) → Short khi retest.

![[Breaker-Advanced-Anatomy.svg|697]]

*Giải phẫu một Bullish Breaker theo đúng thứ tự: OB cũ (cụm nến giảm) → sweep SSL dưới Low1 → displacement phá High1 = MSS + FVG → OB đảo cực thành hỗ trợ → retest = entry → target BSL. Bearish breaker là hình ảnh phản chiếu ở hộp amber phía dưới.*

**Phân biệt cốt lõi — Breaker vs Order Block vs Mitigation Block:**
- **Order Block (OB):** vùng nến cuối cùng TRƯỚC displacement tạo move; entry theo hướng move ban đầu (chưa fail).
- **Breaker Block:** OB ĐÃ fail; giá đã quét liquidity + phá cấu trúc ngược; vùng đảo cực; entry theo hướng MỚI.
- **Mitigation Block:** tương tự breaker về vị trí nhưng không nhất thiết có sweep liquidity rõ ràng — là vùng giá quay lại "giải tỏa" lệnh kẹt; ICT đôi khi dùng gần nghĩa, nhưng breaker nhấn mạnh **có sweep + MSS**.

**Mục đích trong ICT:**
- Là **POI đảo chiều chất lượng cao**: kết hợp sẵn sweep + MSS trong cấu trúc.
- Cho **entry sau khi xu hướng đã đổi**, R:R tốt vì stop logic nằm ngoài điểm sweep.
- Là bằng chứng **thị trường đã chuyển delivery**: OB cũ fail nghĩa là phe cũ đã mất kiểm soát.

**Vì sao khái niệm này quan trọng:**
Breaker giúp bạn vào lệnh **đảo chiều** với cấu trúc rõ ràng thay vì đoán đỉnh/đáy. Nhưng nó bị nhầm nhiều nhất với OB thường: trader thấy giá break một level rồi retest và gọi là "breaker" mà không kiểm tra có sweep + MSS hay không — dẫn tới vào lệnh ngược xu hướng vẫn còn nguyên.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Một OB vừa fail có tạo thành breaker không (có sweep + MSS chưa)?
- Vùng đảo cực (breaker) nằm ở đâu để retest và vào lệnh?
- Đây là breaker thật hay chỉ là OB/level thường bị xuyên qua?
- Stop logic (ngoài điểm sweep) và target liquidity ở đâu?

### Breaker Block không phải là gì
- Không phải mọi OB bị xuyên qua — phải có sweep liquidity + MSS rõ.
- Không phải "break level rồi retest" đơn thuần (đó có thể chỉ là S/R thường).
- Không phải tín hiệu độc lập — vẫn cần đúng bias + premium/discount + (lý tưởng) confluence FVG.
- Không giống Inversion FVG (IFVG) về cấu trúc, dù cùng ý tưởng "đảo cực" — breaker dựa trên OB, IFVG dựa trên FVG.
- Không phải OB thường: OB = theo hướng move gốc; breaker = theo hướng ĐẢO.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái của Breaker

| Loại | Cấu trúc | Vai trò thực chiến |
|---|---|---|
| **Bullish Breaker** | Sweep SSL (Low2<Low1) → displacement phá High1 (MSS bullish) → cụm nến giảm gần đỉnh đảo cực | Hỗ trợ → tìm **Long** khi retest |
| **Bearish Breaker** | Sweep BSL (High2>High1) → displacement phá Low1 (MSS bearish) → cụm nến tăng gần đáy đảo cực | Kháng cự → tìm **Short** khi retest |
| **Breaker + FVG** | Breaker trùng/đi kèm FVG của nhịp displacement | Confluence mạnh, entry refined |
| **HTF Breaker** | Breaker hình thành trên D1/H4 | POI đảo chiều lớn, độ tin cậy cao |

> [!tip]
> Breaker mạnh nhất khi vùng đảo cực **trùng một FVG** của chính nhịp displacement đã phá cấu trúc. Lúc đó bạn có breaker + FVG + (đã có sweep + MSS) trong cùng một vùng — confluence rất cao.

### Breaker trong "họ Order Block" — 4 vùng dễ nhầm

Breaker chỉ là một thành viên trong nhóm các vùng có "gốc gác order block/imbalance". Trước khi gán nhãn một vùng, hãy trả lời ba câu chốt: **(a) có SWEEP không? (b) swing bị PHÁ hay còn GIỮ? (c) nguồn gốc là OB hay FVG?**

![[Breaker-Advanced-Block-Family.svg|697]]

*So sánh nhanh: [[25 - OB - Order Block|Order Block]] (chưa fail, vào theo hướng gốc) vs Breaker (OB fail + có sweep + đảo cực) vs [[22 - Mitigation Block|Mitigation Block]] (OB fail nhưng KHÔNG sweep, swing giữ) vs [[17 - Inverse Fair Value Gap - iFVG|IFVG]] (nguồn từ FVG, fail bằng close). Breaker là vùng DUY NHẤT bắt buộc có cả sweep lẫn MSS.*

### Khi nào khái niệm này có giá trị cao?
- [ ] Có đủ chuỗi: **sweep liquidity → displacement phá cấu trúc (MSS)** rõ ràng.
- [ ] Breaker đồng hướng **Daily Bias** sau khi cấu trúc đã đổi.
- [ ] Vùng breaker nằm đúng **discount** (bullish breaker) / **premium** (bearish breaker).
- [ ] Breaker trùng/đi kèm **FVG** của nhịp displacement.
- [ ] Có target liquidity rõ ở phía hướng mới.

### Khi nào nên bỏ qua?
- [ ] Không có sweep liquidity trước khi "phá" → chỉ là OB/level thường.
- [ ] Không có MSS rõ — chỉ là một cú xuyên qua level.
- [ ] Breaker ngược bias mà cấu trúc HTF chưa thực sự đổi.
- [ ] Vùng breaker ở sai premium/discount cho hướng vào.
- [ ] Giá đã chạy xa khỏi breaker — retest thành chase.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **OB ban đầu:** xác định cụm nến OB (gần High1 cho bullish breaker / gần Low1 cho bearish breaker).
2. **Sweep liquidity:** giá quét qua đáy/đỉnh thanh khoản ở phía OB (SSL cho bullish, BSL cho bearish).
3. **Displacement + MSS:** một nhịp mạnh phá cấu trúc theo hướng NGƯỢC với OB ban đầu.
4. **Đảo cực:** OB cũ thất bại, vùng của nó đổi vai trò support↔resistance.
5. **Retest:** giá quay lại test vùng breaker → điểm vào lệnh.

### Ma trận nhận diện Breaker

| Thành phần | Bullish Breaker (→ Long) | Bearish Breaker (→ Short) | Cảnh báo / không phải breaker |
|---|---|---|---|
| **Liquidity sweep** | Quét SSL (Low2 < Low1) | Quét BSL (High2 > High1) | Không có sweep |
| **Displacement/MSS** | Đẩy lên phá High1 (MSS bullish) | Đẩy xuống phá Low1 (MSS bearish) | Chỉ xuyên qua level, không MSS |
| **Vùng đảo cực** | Cụm nến giảm gần High1 → hỗ trợ | Cụm nến tăng gần Low1 → kháng cự | OB chưa fail / level thường |
| **Location** | Discount của dealing range | Premium của dealing range | Sai phía |
| **Bias** | Đồng hướng bias bullish mới | Đồng hướng bias bearish mới | Ngược bias chưa đổi |

### Điều kiện bắt buộc
- [ ] Xác định OB ban đầu và liquidity mà nó liên quan.
- [ ] Có sweep liquidity rõ ràng trước khi đảo chiều.
- [ ] Có displacement + MSS phá cấu trúc theo hướng mới.
- [ ] Xác định vùng đảo cực (breaker) và mức invalidation.

### Điều kiện tăng xác suất
- [ ] Breaker trùng FVG của nhịp displacement.
- [ ] Breaker đúng premium/discount cho hướng vào.
- [ ] Đồng hướng Daily Bias sau khi cấu trúc đã đổi.
- [ ] HTF breaker (D1/H4) làm khung lớn, LTF refine entry.
- [ ] Có target liquidity rõ; R:R đạt kế hoạch.

### Điều kiện làm setup yếu đi
- Sweep mờ nhạt / không rõ pool nào bị quét.
- MSS yếu (chỉ phá một chút, không displacement).
- Breaker đã bị test nhiều lần, ăn mòn.
- Vùng breaker quá rộng, không xác định được entry/stop rõ.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Breaker
> 1. **OB nào đã fail, và đã có sweep liquidity trước khi nó fail chưa?**
> 2. **Đã có displacement + MSS phá cấu trúc theo hướng mới chưa?**
> 3. **Vùng breaker có đúng premium/discount + đồng hướng bias mới không?**
> 4. **Stop (ngoài điểm sweep) và target liquidity ở đâu, R:R bao nhiêu?**

![[Breaker-Advanced-Sequence-Chain.svg|697]]

*Breaker là POI xuất hiện ở bước ⑤ — SAU khi sweep (③) và MSS (④) đã xảy ra, TRƯỚC retest và entry. Bỏ qua sweep hoặc MSS thì vùng đó không phải breaker.*

### D1 / H4 — Bias & Narrative
- **Bias hiện tại / đang đổi:** breaker thường xuất hiện tại điểm cấu trúc HTF chuyển hướng (xem [[12 - Daily Bias]]).
- **Liquidity HTF:** pool nào vừa bị quét để tạo breaker; pool nào là target.
- **Vị trí premium/discount:** bullish breaker cần ở discount; bearish breaker cần ở premium.

### H1 / M15 — POI & Context
- **Xác định breaker cụ thể:** ghi vùng breaker H1/M15, ví dụ `bullish breaker 1.0840–1.0855 sau sweep SSL 1.0810 + MSS phá 1.0850`.
- **Confluence:** breaker có trùng FVG của nhịp displacement không?
- **Trạng thái:** vùng breaker còn unmitigated chưa, đã bị retest mấy lần?

### M5 / M1 — Confirmation & Entry
- **Retest + LTF confirm:** chờ giá retrace về vùng breaker; M5/M1 cho phản ứng (reject) hoặc MSS nhỏ.
- **Entry:** tại mép/Mean Threshold của breaker, hoặc tại FVG trùng vùng.
- **Stop loss logic:** ngoài vùng breaker / ngoài điểm sweep (Low2 cho bullish, High2 cho bearish).
- **Target:** liquidity phía hướng mới (BSL cho bullish breaker, SSL cho bearish breaker).

```text
Mẫu ghi nhanh — Bullish Breaker (Long)
HTF Bias: Bullish (vừa đổi) | Location: Discount
OB cũ (fail): cụm nến giảm gần High1 [range]
Sweep: SSL Low2 < Low1 tại [level]
MSS: displacement phá High1 tại [level]
Breaker zone: [low]–[high]; confluence FVG? Yes/No
Entry: retest vùng breaker + M5 confirm
Stop: dưới Low2 / dưới breaker
Target: BSL [level]
Invalid: đóng nến lại dưới breaker + dưới MSS
```

```text
Mẫu ghi nhanh — Bearish Breaker (Short)
HTF Bias: Bearish (vừa đổi) | Location: Premium
OB cũ (fail): cụm nến tăng gần Low1 [range]
Sweep: BSL High2 > High1 tại [level]
MSS: displacement phá Low1 tại [level]
Breaker zone: [low]–[high]; confluence FVG? Yes/No
Entry: retest vùng breaker + M5 confirm
Stop: trên High2 / trên breaker
Target: SSL [level]
Invalid: đóng nến lại trên breaker + trên MSS
```

> [!warning]
> **Breaker không phải lý do để bắt đỉnh/đáy sớm.** Nó chỉ hợp lệ SAU khi sweep + MSS đã xảy ra. Vào "breaker" khi cấu trúc chưa thực sự đổi là vào ngược xu hướng còn nguyên.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Có sweep liquidity rõ trước khi OB fail.
- [ ] Có displacement + MSS phá cấu trúc theo hướng mới.
- [ ] Vùng breaker đúng premium/discount + đồng hướng bias mới.
- [ ] (Lý tưởng) breaker trùng FVG của nhịp displacement.
- [ ] Giá retest vùng breaker và respect (reject) + LTF confirm.
- [ ] Stop ngoài điểm sweep; target liquidity rõ; R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Không có sweep liquidity / không có MSS → không phải breaker.
- [ ] Giá **đóng nến xuyên qua** vùng breaker và đi tiếp (breaker fail).
- [ ] Breaker ngược bias mà cấu trúc HTF chưa đổi.
- [ ] Vùng breaker ở sai premium/discount cho hướng vào.
- [ ] Giá đã chạy quá xa, retest thành chase.

### OB thường vs Breaker vs Breaker fail

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| OB chưa bị phá, entry theo hướng move gốc | **Order Block** | Dùng OB bình thường |
| OB fail sau sweep + MSS, retest đảo cực, reject | **Breaker hợp lệ** | Entry theo hướng mới |
| "Breaker" không có sweep/MSS, giá xuyên qua | **Không phải breaker** | Bỏ; đó là level thường |
| Breaker hợp lệ nhưng giá đóng nến xuyên qua khi retest | **Breaker fail** | Hủy lệnh; cảnh giác tiếp diễn hướng cũ |

> [!note]
> Breaker và **[[25 - OB - Order Block|Order Block]]** là hai mặt của một cấu trúc: cùng một vùng nến, nhưng OB dùng khi vùng còn "giữ" theo hướng gốc, còn breaker dùng khi vùng đã fail và đảo cực. Hỏi đúng một câu: **"Vùng này đã quét liquidity và phá cấu trúc NGƯỢC lại chưa?"** — nếu rồi, đó là breaker.

![[Breaker-Advanced-Failed-Breaker.svg|697]]

*Ranh giới cứng giữa "giữ lệnh" và "hủy lệnh" là **acceptance**: một wick chọc vào breaker vẫn là "chờ" (bên trái, respect/reject); một nến ĐÓNG xuyên qua vùng + một nến sau GIỮ bên kia và xuyên lại MSS level = failed breaker (bên phải), thoát ngay và cảnh giác tiếp diễn hướng cũ.*

### Nâng cao — Breaker + FVG confluence và cách refine entry bằng CE/OTE

Một breaker "trần" (chỉ có vùng đảo cực) thường quá rộng để đặt stop chặt. Chất lượng entry tăng vọt khi bạn **xếp lớp breaker với FVG của chính nhịp displacement** rồi refine bằng CE (Consequent Encroachment) hoặc OTE.

- **Vì sao FVG của nhịp MSS là confluence "cùng nguồn":** nhịp displacement phá High1/Low1 (bước tạo MSS) gần như luôn để lại một [[Fair Value Gap]]. FVG này và vùng breaker sinh ra từ **cùng một sự kiện đảo delivery**, nên khi chúng chồng lên nhau, bạn có hai bằng chứng độc lập cùng chỉ về một vùng giá. Đây là trạng thái "Breaker + FVG" ở bảng phân loại mục 2.
- **Refine bằng CE (điểm 50% của FVG/breaker):** thay vì vào ở mép xa của breaker (giá tốt nhưng dễ bị xuyên) hay mép gần (an toàn nhưng R:R kém), đặt limit tại **Mean Threshold / CE** — trung điểm của vùng chồng lấn breaker∩FVG. Đây là điểm cân bằng giữa fill-rate và stop-distance.
- **Kết hợp [[26 - OTE - Optimal Trade Entry|OTE]]:** vẽ Fibonacci trên nhịp displacement (từ swept low/high tới đỉnh/đáy displacement). Nếu vùng breaker∩FVG rơi vào cụm OTE 62–79%, đó là "triple confluence" (breaker + FVG + OTE) — ưu tiên cao nhất, size chuẩn.
- **Thứ tự ưu tiên khi nhiều vùng:** breaker∩FVG∩OTE > breaker∩FVG > breaker∩OTE > breaker trần. Ghi lại tag `breaker_fvg_confluence` và `entry_refine` (CE/OTE/mép) vào journal để về sau đo R trung bình theo từng loại.

> [!tip]
> Nếu breaker và FVG **không** chồng nhau, hãy coi chúng là hai POI riêng biệt theo thứ tự giá sẽ chạm: thường FVG (gần đỉnh/đáy displacement) được test trước, breaker (sâu hơn về discount/premium) test sau. Đừng gộp làm một vùng "to" — điều đó chỉ làm stop rộng ra vô ích.

### Nâng cao — Phân tầng chất lượng breaker theo loại liquidity pool bị sweep và vị trí HTF

Không phải breaker nào cũng đáng tin ngang nhau. Vì breaker **bắt buộc có một sweep**, chất lượng của nó phụ thuộc trực tiếp vào **loại pool bị quét** ở bước tạo breaker và **vị trí HTF** của vùng đảo cực.

| Tier | Pool bị sweep để tạo breaker | Vị trí HTF của vùng breaker | Vì sao chất lượng cao / thấp |
|---|---|---|---|
| **A — cao nhất** | Equal highs/lows, PDH/PDL, PWH/PWL, session high/low | Đúng discount (bull) / premium (bear) + trùng HTF POI | Sweep external liquidity giải phóng nhiều "nhiên liệu"; breaker nằm đúng phía dealing range → đảo chiều bền, target rộng |
| **B — tốt** | Swing high/low đơn, rõ ràng, **unmitigated** | Discount/premium hợp lệ nhưng không trùng HTF POI lớn | Cấu trúc sạch nhưng thiếu "cộng hưởng" HTF; vẫn tradeable với size chuẩn |
| **C — trung bình** | Swing đã bị test 1 lần | Gần equilibrium (chưa hẳn premium/discount) | Pool đã mỏng bớt; breaker dễ chỉ đủ sức cho một internal leg, giảm size |
| **D — thấp / bỏ** | Micro swing, hoặc pool đã bị quét nhiều lần | Sai phía (bull breaker ở premium) | "Nhiên liệu" gần cạn + location xấu → phần lớn là failed breaker, đừng trade |

- **Nguyên tắc nhân chất lượng:** một breaker Tier A trong kill zone ([[18 - Kill Zones]]) đồng hướng [[12 - Daily Bias]] là setup A+; cùng cấu trúc đó nhưng sweep một micro swing giữa range thì tụt thẳng xuống Tier D dù "trông giống breaker".
- **HTF breaker làm khung, LTF refine:** một breaker trên D1/H4 (sweep PDL/PWL) tạo POI đảo chiều lớn; bạn xuống M15/M5 tìm một breaker/MSS nhỏ **bên trong** vùng HTF đó để refine entry — HTF cho location + độ tin, LTF cho entry + stop chặt.
- **Ghi vào journal:** tag `breaker_swept_pool_tier` (A/B/C/D) và `breaker_htf_location` (POI-aligned / range). Sau 20–30 mẫu, so R trung bình giữa Tier A và Tier C — gần như chắc chắn bạn sẽ thấy chênh lệch đủ lớn để bỏ hẳn Tier C–D.

### Nâng cao — Đọc một Failed Breaker như tín hiệu tiếp diễn

Một breaker thất bại không chỉ là "setup hỏng" — nó là **bằng chứng phe cũ vẫn kiểm soát**, và thường mở ra một cơ hội theo hướng ngược lại (tiếp diễn hướng gốc).

1. **Định nghĩa fail bằng acceptance, không bằng cảm giác:** breaker chỉ được coi là fail khi có **một nến đóng thân xuyên qua vùng breaker + một nến sau giữ bên kia và xuyên lại MSS level** (xem diagram trên). Một wick chọc qua rồi đóng lại bên trong vùng vẫn là respect — đừng thoát non.
2. **Failed breaker = MSS bị phủ nhận:** khi giá đóng xuyên lại MSS level, cú "đảo chiều" ban đầu bị vô hiệu. Điều này nói: sweep + MSS trước đó chỉ là một cú **liquidity grab tạm thời**, và delivery gốc chưa hề đổi. Đây là lúc chuyển tư duy từ "tìm entry đảo chiều" sang "canh tiếp diễn hướng cũ".
3. **Setup tiếp diễn sau failed breaker:** vùng breaker đã fail thường **đảo vai trò lần nữa** — trở lại thành rào cản theo hướng cũ (một bullish breaker fail → vùng đó thành kháng cự cho hướng giảm tiếp diễn). Kết hợp với FVG của nhịp phá xuống, bạn có POI để vào theo hướng gốc, thường về đúng pool liquidity mà "MSS giả" vừa tạo ra ở phía đối diện.
4. **Thông tin cho bias:** nhiều failed breaker liên tiếp ngược [[12 - Daily Bias|Daily Bias]] là dấu hiệu HTF delivery còn rất mạnh theo hướng bias — đáng ghi vào Daily Note như một xác nhận, không phải một thất bại đơn lẻ.

> [!warning]
> Đừng "trả thù" một failed breaker bằng cách đảo lệnh ngay tại cây nến phá. Chờ giá **retest vùng breaker đã fail** (giờ là rào cản hướng cũ) hoặc FVG của nhịp phá, rồi mới vào theo hướng tiếp diễn — vẫn phải đúng sequence, chỉ là hướng đã đổi.

---

## 6. Ví dụ chart

### Ví dụ đúng — Bullish Breaker: sweep SSL + MSS, retest về vùng đảo cực, Long
![[Breaker-Block-Example-Correct.png]]

**Mô tả:**
Giá tạo Low1 rồi rally lên High1 (đoạn tạo đỉnh có cụm nến giảm = OB cũ). Sau đó giá quay xuống **quét SSL dưới Low1** (Low2 < Low1). Một **displacement tăng** đẩy giá lên **phá High1** (MSS bullish), khiến cụm nến giảm gần High1 đảo cực thành **bullish breaker** (hỗ trợ). Giá retrace về vùng breaker, reject; Long tại đó; stop dưới Low2 / dưới vùng; target BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- Có đủ chuỗi **sweep SSL → displacement → MSS** trước khi gọi là breaker.
- Vùng breaker ở **discount**, đồng hướng bias bullish mới.
- Entry tại retest vùng đảo cực, stop logic ngoài điểm sweep.
- Target là liquidity rõ ràng (BSL).

### Ví dụ sai / dễ nhầm — Gọi OB thường là "breaker", không sweep + không MSS
![[Breaker-Block-Example-Wrong.png]]

**Mô tả lỗi:**
Trong một nhịp tăng, trader thấy một cụm nến giảm, rồi giá phá nhẹ qua một đỉnh và đánh dấu cụm nến đó là "bullish breaker", Long khi retest. Nhưng **không có sweep liquidity** trước đó và **không có MSS thật** (chỉ là một cú phá yếu). Vùng "breaker" tự gán không có cơ sở; giá xuyên thẳng qua và tiếp tục giảm, stop bị quét.

**Bài học:**
- Breaker **bắt buộc** có sweep liquidity + displacement/MSS; thiếu là không phải breaker.
- Không gọi mọi cụm nến trước một cú break là "breaker".
- Hỏi: "Đã quét pool liquidity nào? Đã phá cấu trúc ngược lại chưa?" — nếu chưa, bỏ qua.

---
### Sequence mẫu — Long từ Bullish Breaker
```text
HTF Bias chuyển Bullish
→ Low1 → rally High1 (cụm nến giảm = OB cũ)
→ Sweep SSL (Low2 < Low1)
→ Displacement tăng phá High1 (MSS bullish) → tạo FVG
→ OB cũ đảo cực thành Bullish Breaker (hỗ trợ)
→ Giá retrace về breaker (lý tưởng trùng FVG, ở discount)
→ M5/M1 confirm → Entry
→ Stop dưới Low2 / dưới breaker
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short từ Bearish Breaker
```text
HTF Bias chuyển Bearish
→ High1 → pullback Low1 (cụm nến tăng = OB cũ)
→ Sweep BSL (High2 > High1)
→ Displacement giảm phá Low1 (MSS bearish) → tạo FVG
→ OB cũ đảo cực thành Bearish Breaker (kháng cự)
→ Giá retrace về breaker (lý tưởng trùng FVG, ở premium)
→ M5/M1 confirm → Entry
→ Stop trên High2 / trên breaker
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> Breaker là "phiên bản đảo cực" của [[25 - OB - Order Block|Order Block]]: cùng nguyên liệu (cụm nến + displacement), nhưng đi kèm bắt buộc một [[20 - Liquidity Sweep]] và một [[21 - Market Structure Shift]] để xác nhận hướng đã đổi. Nếu vùng đó còn trùng một [[Fair Value Gap]] thì confluence càng mạnh.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Breaker chỉ là POI sau khi cấu trúc đã đổi. Chỉ vào khi có sweep + MSS + đúng context.

### A. Context (HTF)
- [ ] Daily Bias đã rõ / vừa chuyển hướng: `Bullish / Bearish`.
- [ ] Đã có sweep liquidity tạo nền cho breaker.
- [ ] Đã có displacement + MSS phá cấu trúc theo hướng mới.
- [ ] Vùng breaker đúng discount (bullish) / premium (bearish).
- [ ] Có draw on liquidity rõ làm target.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá retest vùng breaker và respect (reject).
- [ ] (Lý tưởng) breaker trùng FVG của nhịp displacement.
- [ ] LTF có phản ứng/MSS nhỏ xác nhận.
- [ ] Entry tại mép/Mean Threshold breaker hoặc FVG trùng vùng.
- [ ] Stop ngoài điểm sweep (Low2/High2) / ngoài breaker.
- [ ] Target liquidity rõ; R:R tối thiểu đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Không có sweep liquidity → không phải breaker → không trade.
- [ ] Không có MSS rõ → không trade.
- [ ] Breaker ngược bias chưa đổi → không trade.
- [ ] Sai premium/discount → không trade.
- [ ] Giá đã đóng nến xuyên qua breaker (fail) → không trade.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Nhầm OB với breaker | Gọi mọi cụm nến trước cú break là breaker | Vào ngược xu hướng còn nguyên | Yêu cầu sweep + MSS mới gọi breaker |
| Breaker không có sweep | "Phá level rồi retest" mà không quét liquidity | Thiếu cơ sở đảo chiều | Chỉ tính breaker khi có sweep rõ |
| Breaker không có MSS | Cú xuyên yếu, không displacement | Cấu trúc chưa đổi | Yêu cầu displacement + MSS |
| Vào ngược bias chưa đổi | Bắt đỉnh/đáy khi HTF chưa chuyển | Xác suất thấp | Chỉ vào khi cấu trúc đã đổi + đúng bias |
| Bỏ qua premium/discount | Bullish breaker ở premium | R:R xấu, entry chase | Bullish breaker ở discount, bearish ở premium |
| Stop quá sát | Stop trong vùng breaker | Bị quét dễ dàng | Stop ngoài điểm sweep / ngoài breaker |
| Giữ lệnh khi breaker fail | Giá đóng nến xuyên qua mà vẫn ôm | Tiếp diễn hướng cũ | Cắt khi đóng nến xuyên breaker + MSS |
| Vùng breaker quá rộng | Không xác định entry/stop rõ | Quản trị rủi ro mơ hồ | Refine bằng FVG / Mean Threshold |

---

## 10. Câu hỏi tự kiểm tra

- Mình có phân biệt được Breaker và Order Block thường trong 30 giây không?
- Vùng này đã quét liquidity nào và phá cấu trúc gì để trở thành breaker?
- Đây là bullish hay bearish breaker, và nó ở premium hay discount?
- Breaker có trùng FVG của nhịp displacement không?
- Stop (ngoài điểm sweep) và target (liquidity) ở đâu, R:R bao nhiêu?
- Điều gì làm breaker này fail?
- Breaker này có đồng hướng bias đã đổi không?
- Nếu không trade breaker này, lý do "No Trade" là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Breaker Block là gì?
**Đáp:** Là một Order Block đã thất bại: sau khi giá quét liquidity rồi displacement phá cấu trúc ngược lại (MSS), vùng OB cũ đảo cực và trở thành hỗ trợ/kháng cự cho hướng mới.

### Q2
**Hỏi:** Cấu trúc một Bullish Breaker gồm những bước nào?
**Đáp:** Low1 → rally High1 (OB cũ) → sweep SSL (Low2<Low1) → displacement tăng phá High1 (MSS) → cụm nến giảm gần High1 đảo cực thành hỗ trợ → retest = Long.

### Q3
**Hỏi:** Hai điều kiện bắt buộc để một vùng là breaker (không phải OB thường)?
**Đáp:** (1) Có liquidity sweep; (2) Có displacement + MSS phá cấu trúc theo hướng ngược với OB ban đầu.

### Q4
**Hỏi:** Khác biệt giữa Order Block và Breaker Block về hướng vào lệnh?
**Đáp:** OB → entry theo hướng move gốc (chưa fail). Breaker → entry theo hướng MỚI (OB đã fail và đảo cực).

### Q5
**Hỏi:** Đặt stop cho một Bullish Breaker ở đâu?
**Đáp:** Ngoài điểm sweep (dưới Low2) hoặc dưới vùng breaker.

### Q6
**Hỏi:** Confluence nào làm breaker mạnh hơn?
**Đáp:** Khi vùng breaker trùng một FVG của chính nhịp displacement đã phá cấu trúc, đúng premium/discount, và đồng hướng bias mới.

### Q7
**Hỏi:** Khi nào một breaker bị vô hiệu?
**Đáp:** Khi không thực sự có sweep/MSS (không phải breaker), hoặc khi giá đóng nến xuyên qua vùng breaker và tiếp tục theo hướng cũ.

---

## 12. Lesson Learned

### Bài học chính
- Breaker = **OB fail + đảo cực**, không phải "break level rồi retest".
- Bắt buộc có **sweep liquidity + displacement/MSS** mới gọi là breaker.
- Breaker cho entry theo **hướng MỚI** (ngược hướng OB gốc), sau khi cấu trúc đã đổi.
- Mạnh nhất khi trùng **FVG** + đúng **premium/discount** + đồng hướng bias mới.
- Stop nằm ngoài **điểm sweep**; target là liquidity phía hướng mới.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ gọi một vùng là "breaker" khi có sweep liquidity + MSS rõ.
- [ ] Tôi không nhầm breaker với OB thường; tôi xác định hướng vào theo hướng MỚI.
- [ ] Tôi chỉ vào breaker đồng hướng bias đã đổi và đúng premium/discount.
- [ ] Tôi ưu tiên breaker trùng FVG để có confluence.
- [ ] Tôi đặt stop ngoài điểm sweep và cắt khi giá đóng nến xuyên breaker.

### Câu nhắc nhở khi trade
> **"Breaker là một OB đã chết và sống lại theo hướng ngược — chỉ tin nó khi đã thấy sweep + MSS."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt breaker vs OB vs mitigation block không? |
| Nhận diện trên chart |  | Có xác định đúng chuỗi sweep → MSS → đảo cực không? |
| Biết khi nào bỏ qua |  | Có dám bỏ "breaker" thiếu sweep/MSS không? |
| Kết hợp với context HTF |  | Breaker có đặt trong bias đã đổi + premium/discount không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự tại retest vùng đảo cực không? |
| Review sau trade |  | Có kiểm tra bằng dữ liệu journal thay vì cảm tính không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[Breaker Block]]`.
- [ ] Review riêng: breaker có sweep+MSS rõ vs mờ; có/không FVG confluence.
- [ ] Thống kê win rate, average R theo `mss_confirmed` và `breaker_fvg_confluence`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## 14. Best Practices

> [!success] Nguyên tắc vàng
> **"Breaker là một OB đã chết và sống lại theo hướng ngược."** Trước khi gọi bất kỳ vùng nào là breaker, bắt buộc thấy đủ chuỗi: **sweep liquidity → displacement + MSS → đảo cực**. Thiếu sweep hoặc thiếu MSS thì đó chỉ là một level/OB thường bị xuyên qua — và trade nó là vào ngược một xu hướng còn nguyên.

1. **Kiểm tra ba cổng theo đúng thứ tự: Có sweep? Có MSS/displacement? Vùng đã đảo cực chưa?** Thiếu một cổng = không phải breaker, không trade. Phần lớn lệnh thua gắn tag breaker trong journal sẽ rơi vào nhóm "không có sweep thật" hoặc "MSS yếu, chỉ là wick". Viết ba câu hỏi này cạnh màn hình cho tới khi thành phản xạ.

2. **Phân biệt breaker với [[22 - Mitigation Block]] bằng phép thử sweep.** Cả hai đều là OB đảo hướng, nhưng breaker BẮT BUỘC có sweep (đáy/đỉnh cũ bị phá), còn mitigation block hình thành khi swing cũ GIỮ VỮNG (không sweep). Tên gọi quyết định vị trí stop: breaker → stop ngoài điểm sweep (Low2/High2); mitigation → stop ngoài extreme failure swing. Đặt sai tên = đặt sai stop.

3. **Ưu tiên breaker trùng FVG của chính nhịp displacement.** Confluence mạnh nhất là khi vùng đảo cực chồng lên FVG do nhịp MSS để lại — lúc đó bạn có sweep + MSS + breaker + FVG trong một vùng. Refine entry quanh CE ([[10 - Consequent Encroachment (Mean Threshold)|Mean Threshold]]) hoặc [[26 - OTE - Optimal Trade Entry|OTE]] của vùng để có stop ngắn hơn và R:R tốt hơn nhiều so với vào cả breaker rộng.

4. **Chấm chất lượng pool bị sweep trước khi tin breaker.** Một breaker sinh sau khi quét equal highs/lows hay PDH/PDL (external liquidity nhiều "nhiên liệu") đáng tin hơn hẳn một breaker sau khi quét một swing vụn vặt. Ghi trường `breaker_swept_pool_tier` vào journal để sau này lọc — nhiều trader phát hiện chỉ breaker từ pool Tier 1–2 mới có edge ổn định.

5. **Đặt stop ngoài ĐIỂM SWEEP, không sát mép breaker.** Vì breaker luôn đi kèm một sweep, điểm swept (Low2 cho bullish, High2 cho bearish) là mốc invalidation tự nhiên — nếu giá quay lại phá nó thì narrative đảo chiều đã sai. Stop sát mép breaker là lỗi kinh điển khiến lệnh bị quét bởi nhiễu quanh vùng trước khi đi đúng hướng.

6. **Đọc một Failed Breaker như tín hiệu tiếp diễn, không cố "gồng".** Ranh giới cứng là acceptance: một nến đóng ngược xuyên qua vùng breaker + một nến giữ bên kia = breaker fail → thoát, và cảnh giác thị trường muốn tiếp diễn hướng cũ. Trước ranh giới đó, retrace sâu vào vùng là bình thường; sau ranh giới đó, đừng giữ vì hy vọng.

7. **Backtest breaker theo tổ hợp điều kiện, không theo tổng thể.** Đừng hỏi "breaker win rate bao nhiêu?" — hỏi "breaker + sweep Tier 1 + trùng FVG + đúng premium/discount có win rate bao nhiêu so với breaker thiếu từng điều kiện?". 20–30 mẫu mỗi nhóm đủ thấy chênh lệch ([[04 - Backtesting]]), và đó là cách biến niềm tin thành quy tắc có số liệu.
