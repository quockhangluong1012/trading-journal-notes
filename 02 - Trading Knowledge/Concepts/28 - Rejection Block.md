---
type: ict-concept
concept: Rejection Block
aliases:
  - Rejection Block
  - RB
tags:
  - trading/ict/concept
  - trading/study
  - "#RejectionBlock"
status: seed
category: PD Array
last_reviewed:
created: 2026-06-24
updated: 2026-07-03
---

# Rejection Block

> [!summary] Tóm tắt 1 câu
> **Rejection Block (RB)** là một PD-array được xác định bởi **cụm wick/tail dài** tại một swing high hoặc swing low — vùng "đuôi nến bị từ chối" nơi giá bị đẩy ngược mạnh — và được dùng làm support/resistance, làm POI để vào lệnh khi giá retest về.

> [!important] Nguyên tắc cốt lõi
> - RB **lấy phần wick** của nến, **không lấy body** như [[Order Block]]. Đây là điểm phân biệt quan trọng nhất.
> - Vùng RB = khoảng từ **open/close (mép body)** đến **đỉnh/đáy của wick (extreme)** tại điểm đảo chiều.
> - **Bullish RB** hình thành ở **đáy** một down-move (wick dưới dài); **Bearish RB** hình thành ở **đỉnh** một up-move (wick trên dài).
> - Wick dài thường là dấu vết của một **[[20 - Liquidity Sweep]]** (quét stop) → RB thường trùng với vùng giá vừa "ăn" thanh khoản rồi quay đầu.
> - RB là PD-array **xác suất phụ** (importance 3): chỉ giá trị khi sự từ chối thể hiện qua wick chứ không qua một body/displacement sạch.

---

## 1. Định nghĩa

### Khái niệm
**Rejection Block** là một vùng giá (PD-array) được vẽ từ **phần thân–đuôi nến (body-to-wick region)** tại một điểm đảo chiều quan trọng, nơi thị trường để lại **một hoặc nhiều wick dài** thể hiện sự từ chối mạnh của một mức giá. Khác với [[Order Block]] — vốn dùng **body của nến** cuối cùng trước displacement — RB tập trung vào **đuôi nến (wick/tail)**: chính phần giá mà thị trường "thử rồi loại bỏ".

Khi giá vươn tới một vùng, in ra một wick dài rồi đóng cửa quay lại, phần wick đó cho thấy lực bán/mua đã từ chối mức đó. Cụm wick này trở thành **bộ nhớ** của thị trường: lần sau giá retest về, vùng wick có khả năng phản ứng lại lần nữa.

### Cách vẽ Rejection Block
- **Bearish RB (ở swing high):** vẽ vùng từ **mép trên của body (open/close cao hơn)** lên tới **high của wick** (extreme phía trên). Đây là "vùng wick trên" tại đỉnh.
- **Bullish RB (ở swing low):** vẽ vùng từ **mép dưới của body (open/close thấp hơn)** xuống tới **low của wick** (extreme phía dưới). Đây là "vùng wick dưới" tại đáy.
- Nếu có một **cụm nhiều wick** cùng từ chối một mức, lấy vùng bao trùm các wick đó (từ mép body chung tới wick extreme xa nhất).
- Mức tham chiếu để vào lệnh thường là **mép body** (open/close), với **wick extreme** là điểm stop / invalidation.

> [!tip] Mẹo vẽ
> Body cho bạn **vùng vào lệnh (entry zone)**; wick extreme cho bạn **điểm vô hiệu hóa (invalidation)**. Đừng đảo ngược hai vai trò này.

### Bullish RB vs Bearish RB (định hướng)
- **Bullish Rejection Block** → tại **đáy** của một down-move, các nến để lại **wick dưới dài** (giá bị đẩy lên trở lại). Đóng vai trò **support / discount POI** cho lệnh **Long**.
- **Bearish Rejection Block** → tại **đỉnh** của một up-move, các nến để lại **wick trên dài** (giá bị đẩy xuống trở lại). Đóng vai trò **resistance / premium POI** cho lệnh **Short**.

### Rejection Block vs Order Block vs Breaker Block
| Tiêu chí            | **Rejection Block**                  | **[[Order Block]]**                      | **[[Breaker Block]]**               |
| ------------------- | ------------------------------------ | ---------------------------------------- | ----------------------------------- |
| Phần nến định nghĩa | **Wick / tail** (đuôi nến)           | **Body** của nến cuối trước displacement | **Body** của OB thất bại (bị phá)   |
| Vị trí hình thành   | Swing high/low có wick dài           | Nến nghịch hướng cuối trước cú đẩy       | OB cũ bị phá rồi giá quay lại       |
| Tín hiệu đi kèm     | Long wick = từ chối / sweep          | Displacement + FVG ra khỏi OB            | MSS/BOS phá qua OB, đảo vai trò     |
| Vai trò             | S/R, POI re-entry                    | POI gốc, gốc của lệnh institutional      | POI sau đảo chiều cấu trúc          |
| Khi nào ưu tiên     | Từ chối qua wick, không có body sạch | Có body + displacement rõ                | Cấu trúc đã đảo, OB cũ flip vai trò |
| Bullish ở đâu       | Đáy down-move, wick dưới dài         | Nến đỏ cuối trước cú tăng                | OB bán cũ bị phá lên → support      |
| Bearish ở đâu       | Đỉnh up-move, wick trên dài          | Nến xanh cuối trước cú giảm              | OB mua cũ bị phá xuống → resistance |

### Quan hệ với [[20 - Liquidity Sweep]]
Wick dài ≈ **dấu vết của một cú quét thanh khoản**. Khi giá đâm qua một swing để lấy [[07 - Buy-side Liquidity]] / [[30 - Sell-side Liquidity]] rồi nhanh chóng đóng cửa quay lại, phần đâm ra đó chính là wick tạo nên RB. Vì vậy RB chất lượng cao thường nằm **ngay sau một sweep** — đây cũng là logic của [[33 - Turtle Soup]]. Hãy luôn hỏi: *"Wick này đã quét thanh khoản gì?"*

### Mục đích trong ICT
- Cung cấp một **POI thay thế cho OB** khi sự từ chối thể hiện qua đuôi nến chứ không qua body/displacement.
- Đánh dấu **vùng S/R có dấu vết thanh khoản** để canh re-entry theo [[27 - Premium Discount]].
- Bổ trợ confluence cho các entry model như [[ICT 2022 Model]], [[Optimal Trade Entry]].

### Vì sao quan trọng
Nhiều điểm đảo chiều thật **không** để lại một OB body đẹp — chúng đảo bằng một loạt wick (spike + reject). Nếu chỉ biết OB, ta bỏ lỡ các vùng này. RB lấp khoảng trống đó: nó đọc **nơi giá đã bị từ chối**, không chỉ nơi giá đã giao dịch khối lượng body.

### Nó giúp trả lời câu hỏi gì?
- "Vùng đỉnh/đáy này bị từ chối ở đâu, và mức nào đáng để canh retest?"
- "Khi không có OB body sạch, đâu là POI hợp lý cho re-entry?"
- "Wick dài vừa rồi có để lại một vùng kháng cự/hỗ trợ dùng được không?"

### Rejection Block không phải là gì
- **Không** phải mọi wick dài đều là RB — phải nằm tại **swing high/low có ý nghĩa cấu trúc**.
- **Không** phải [[Order Block]] (RB dùng wick, OB dùng body).
- **Không** phải tín hiệu vào lệnh độc lập — cần confirmation (sweep + phản ứng + cấu trúc).
- **Không** thay thế [[12 - Daily Bias]]; RB chỉ là POI, hướng do bias quyết định.

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái
| Loại | Vị trí | Wick định hướng | Vai trò | Thiên hướng lệnh | Đi kèm |
|---|---|---|---|---|---|
| **Bullish RB** | Đáy của down-move (swing low) | Wick **dưới** dài | Support / discount POI | **Long** | Sweep [[30 - Sell-side Liquidity]] |
| **Bearish RB** | Đỉnh của up-move (swing high) | Wick **trên** dài | Resistance / premium POI | **Short** | Sweep [[07 - Buy-side Liquidity]] |

### Khi nào RB có giá trị cao?
- [ ] Wick **quét thanh khoản** rõ ràng (swing cũ, equal highs/lows, [[19 - Liquidity]] pool) rồi đóng quay lại.
- [ ] RB nằm đúng phía [[27 - Premium Discount]] (Bullish RB ở discount, Bearish RB ở premium).
- [ ] RB trùng với một POI HTF (OB/FVG/RB khung lớn) → confluence.
- [ ] Sau RB có **[[21 - Market Structure Shift]] / [[Break of Structure]]** xác nhận đảo chiều.
- [ ] RB hình thành trong [[18 - Kill Zones]] (London/NY).
- [ ] Wick dài bất thường so với các nến lân cận (lực từ chối thật).

### Khi nào nên bỏ qua RB?
- [ ] Wick ngắn, không có sự từ chối đáng kể — chỉ là noise.
- [ ] Nằm ngược phía bias HTF và ngược [[27 - Premium Discount]] (vd Long ở premium).
- [ ] Giá đã **đóng cửa vượt khỏi wick extreme** → RB đã bị vô hiệu.
- [ ] Không quét thanh khoản nào → thiếu logic "stop run".
- [ ] Có một [[Order Block]] body sạch tốt hơn ở cùng vùng → ưu tiên OB.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Swing high/low rõ ràng** có một hoặc nhiều nến để lại wick dài.
2. **Wick dài** vượt khỏi một mức thanh khoản (sweep) rồi bị **đẩy ngược**, body đóng cửa lùi lại.
3. **Body co lại** ở phía đối diện wick (nến reject thường là pin/spike, body nhỏ so với wick).
4. Sau cú từ chối, giá **di chuyển khỏi vùng** theo hướng từ chối (thường kèm displacement).
5. Khi retest, giá phản ứng tại **vùng body→wick** (đặc biệt quanh mép body / open-close).

### Ma trận nhận diện
| Yếu tố | Bullish RB | Bearish RB | Ý nghĩa |
|---|---|---|---|
| Vị trí | Swing low | Swing high | Điểm đảo chiều cấu trúc |
| Wick | Dưới, dài | Trên, dài | Hướng bị từ chối |
| Body | Nằm trên wick | Nằm dưới wick | Phe thắng thế đóng cửa |
| Sweep | Quét sell-side | Quét buy-side | Stop run trước đảo |
| Phản ứng sau | Đẩy lên | Đẩy xuống | Xác nhận hướng RB |
| Vùng entry | Mép body trên→low wick | Mép body dưới→high wick | Khu re-entry |
| Invalidation | Đóng dưới low wick | Đóng trên high wick | RB chết |

### Điều kiện
- **Bắt buộc:** có swing high/low; có wick dài thể hiện từ chối; có phản ứng đảo chiều sau đó.
- **Tăng xác suất:** wick quét thanh khoản; đúng phía premium/discount; có MSS/displacement sau; confluence với POI HTF; trong kill zone.
- **Làm yếu đi:** wick nhỏ/noise; ngược bias; không sweep; giá đã đóng vượt wick extreme; vùng đã được retest nhiều lần (mitigated).

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Rejection Block
> 1. **Wick này có thực sự quét một mức thanh khoản có ý nghĩa không?**
> 2. **Tỉ lệ wick/body có đủ lớn để tính là từ chối thật không?**
> 3. **RB có đúng phía premium/discount theo bias không?**
> 4. **Có MSS/BOS xác nhận sau đó chưa, và invalidation (đóng cửa vượt wick extreme) nằm ở đâu?**

### D1 / H4 — Bối cảnh & bias
- Xác định [[12 - Daily Bias]] và vị trí giá trong [[12 - Dealing Range]] ([[27 - Premium Discount]]).
- Khoanh các swing high/low HTF có **wick dài** + mức [[19 - Liquidity]] quanh đó.
- Đánh dấu RB HTF làm vùng "đại bản doanh" cho POI.

### H1 / M15 — Định khung POI
- Trong vùng RB HTF (hoặc gần mức thanh khoản), chờ giá tiếp cận.
- Xác nhận **sweep** một mức thanh khoản M15/H1, quan sát wick reject.
- Vẽ RB M15/H1 và canh [[21 - Market Structure Shift]] để xác nhận đảo chiều.

### M5 / M1 — Entry tinh chỉnh
- Sau MSS, chờ giá pullback về **mép body của RB** (hoặc FVG/OTE trùng RB).
- Vào lệnh tại RB, stop sau **wick extreme**, target về thanh khoản đối diện.

```text
[QUICK NOTE — BULLISH RB LONG]
HTF bias: bullish | Giá ở: discount
Swing low quét: [sell-side liquidity] @ [level]
Wick dưới dài + reject lên: có
RB zone (body→low wick): [range] – [range]
MSS xác nhận (M5/M15): có @ [level]
Entry (mép body RB): [____]   SL (dưới low wick): [____]
TP1 / TP2 (buy-side): [____] / [____]
R dự kiến: [____]  | Kill zone: [____]
```

```text
[QUICK NOTE — BEARISH RB SHORT]
HTF bias: bearish | Giá ở: premium
Swing high quét: [buy-side liquidity] @ [level]
Wick trên dài + reject xuống: có
RB zone (body→high wick): [range] – [range]
MSS xác nhận (M5/M15): có @ [level]
Entry (mép body RB): [____]   SL (trên high wick): [____]
TP1 / TP2 (sell-side): [____] / [____]
R dự kiến: [____]  | Kill zone: [____]
```

> [!warning] Cảnh báo đa khung
> RB **không trùng** giữa các khung là chuyện bình thường: wick HTF có thể là cả một cấu trúc trên LTF. Luôn dùng RB HTF làm **vùng**, và để LTF cho **timing/confirmation**. Đừng vào lệnh chỉ vì có wick dài trên M1 mà không có bối cảnh HTF.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Xác nhận (confirmation) — cần đủ confluence
- [ ] Wick đã **quét một mức thanh khoản** thực sự (không phải swing vô nghĩa).
- [ ] Có **phản ứng đảo chiều** (đóng cửa quay lại / displacement) sau wick.
- [ ] **[[21 - Market Structure Shift]] / [[Break of Structure]]** trên LTF ủng hộ hướng RB.
- [ ] RB đúng phía [[27 - Premium Discount]] theo bias.
- [ ] (Bonus) Trùng POI HTF, trong [[18 - Kill Zones]].

### Vô hiệu hóa (invalidation)
- [ ] **Giá đóng cửa vượt khỏi wick extreme** (đóng dưới low wick với Bullish RB / đóng trên high wick với Bearish RB) → **RB chết, hủy ý tưởng**.
- [ ] MSS đảo lại ngược hướng RB sau khi đã hình thành.
- [ ] Giá đi xuyên qua không phản ứng (no reaction) → vùng đã bị tiêu hóa.

### So sánh xác nhận theo loại
| Tình huống | Bullish RB | Bearish RB |
|---|---|---|
| Sweep cần thấy | Sell-side bị quét | Buy-side bị quét |
| Đóng cửa hợp lệ | Trên low wick | Dưới high wick |
| Đóng cửa = invalid | Dưới low wick | Trên high wick |
| MSS xác nhận | Phá swing high LTF | Phá swing low LTF |

> [!note] Lưu ý quan trọng
> Phân biệt **wick xuyên** và **body đóng vượt**. Giá có thể đâm qua wick extreme bằng một wick mới (vẫn ổn nếu đóng lại trong vùng), nhưng một **body đóng cửa vượt extreme** là tín hiệu vô hiệu hóa dứt khoát. Luôn chờ đóng nến để phán xét.

### Nâng cao — Định lượng tỉ lệ Wick/Body: khi nào một cái đuôi nến đủ dài để tính là Rejection Block

"Wick dài" là một phán đoán trực quan dễ bị bóp méo bởi khung thời gian, biến động thị trường và cả zoom level của chart. Để RB có tính lặp lại (repeatable) thay vì phụ thuộc cảm giác, cần một phép đo cụ thể thay vì eyeball.

![[RejectionBlock-Advanced-WickBody-Ratio.svg]]
*Ba nến cùng vị trí swing nhưng tỉ lệ wick/body khác nhau: yếu (wick <1x body, dưới 40% tổng range), vừa (wick 1.5-2x body, 50-65% tổng range) và mạnh (wick >2.5x body, wick chiếm ≥70% tổng range của nến). Tier càng cao, RB càng đáng tin làm POI chính.*

Ba tiêu chí định lượng nên dùng song song, không riêng lẻ:
1. **Tỉ lệ wick/body tuyệt đối.** Đo chiều dài wick (từ mép body tới extreme) chia cho chiều dài body (open→close). Wick ≥ 2x body là ngưỡng tối thiểu đáng cân nhắc; dưới đó thường chỉ là biến động bình thường của nến, không phải một cú từ chối rõ rệt.
2. **Tỉ lệ wick / tổng range (high-low) của nến.** Wick chiếm ≥ 60-70% tổng biên độ nến cho thấy phần lớn "hành trình" của nến bị từ chối và đẩy ngược — đây là dấu hiệu áp lực đảo chiều mạnh hơn so với chỉ nhìn tỉ lệ với body.
3. **So sánh tương đối với range trung bình 10-20 nến gần nhất (kiểu ATR).** Một wick dài 15 pip có thể là cực đoan trên một phiên Á yên tĩnh (M1) nhưng lại tầm thường trên một cây nến tin tức mạnh. Luôn hỏi: *"Wick này có dài bất thường so với biên độ trung bình gần đây không, hay chỉ đang theo kịp biến động chung của thị trường lúc này?"*

Bảng quyết định nhanh để gắn tier ngay trên chart:

| Tỉ lệ wick/body | % wick / total range | Tier | Hành động |
|---|---|---|---|
| < 1x body | < 40% | **Yếu (weak)** | Không tính là RB đáng tin; bỏ qua hoặc chỉ theo dõi |
| 1.5x – 2x body | 50% – 65% | **Vừa (moderate)** | Chỉ trade khi có thêm sweep + MSS xác nhận |
| > 2.5x body | ≥ 70% | **Mạnh (strong)** | Ưu tiên làm POI chính, đặc biệt nếu trùng HTF POI |

> [!tip]
> Ghi lại `wick_body_ratio` cho mỗi RB vào journal (ước lượng bằng mắt hoặc đo pixel/pip). Sau 20-30 mẫu trên NQ1/EURUSD/XAUUSD, bạn sẽ có ngưỡng riêng phù hợp với phong cách và khung thời gian mình hay trade, thay vì dùng một con số chung chung cho mọi thị trường.

### Nâng cao — Cụm Rejection Block (stacked/layered wicks): khi nhiều cây nến liên tiếp cùng từ chối một vùng

Không phải lúc nào sự từ chối cũng đến từ một wick spike đơn lẻ và kịch tính. Nhiều khi thị trường từ chối một vùng bằng một **cụm 2-4 nến liên tiếp**, mỗi nến để lại một wick nhỏ hơn nhưng gần như cùng một mức — tạo thành một "kệ từ chối" (rejection shelf) rộng hơn là một điểm sắc nét.

![[RejectionBlock-Advanced-Stacked-Cluster.svg]]
*Bốn nến liên tiếp cùng để lại wick tại gần một mức thanh khoản, thay vì một wick spike đơn lẻ. Envelope RB được vẽ bao trùm toàn bộ cụm — từ wick extreme thấp nhất (hoặc cao nhất, với bearish) trong cụm tới mép body gần nhất — trước khi displacement rời khỏi vùng.*

Cách vẽ RB trong trường hợp cụm:
- **Envelope = từ wick extreme xa nhất trong cụm tới mép body gần nhất.** Không vẽ riêng từng nến; gộp toàn bộ cụm thành một vùng RB duy nhất, giống cách bạn gộp một chuỗi order block liền kề.
- **Invalidation vẫn là wick extreme xa nhất của cả cụm** (đáy thấp nhất với bullish, đỉnh cao nhất với bearish) — không phải extreme của riêng nến cuối.
- **Entry ưu tiên gần mép body của nến cuối cùng trong cụm** (nến gần nhất với nhịp displacement), vì đó là nơi giá "rời đi" thật sự.

Vì sao một cụm RB, dù trông "lộn xộn" hơn, lại có thể **đáng tin hơn** một wick spike đơn lẻ:
- **Nhiều lần thử = nhiều thanh khoản bị hấp thụ.** Mỗi wick trong cụm là một lần thị trường thử đẩy giá qua mức đó và bị từ chối lại — tổng khối lượng lệnh chống lại mức đó lớn hơn nhiều so với một lần thử duy nhất.
- **Dấu chân institutional rõ hơn.** Việc giá quay lại thử cùng một vùng nhiều lần liên tiếp mà không phá được thường phản ánh một lệnh lớn đang được nạp dần (accumulation/distribution theo từng phần), khó thấy trên một cây nến đơn.
- **Ít nhạy với nhiễu của một cây nến bất thường.** Một wick spike đơn có thể là do thanh khoản mỏng tức thời (spike giả); một cụm nhiều nến đồng thuận về cùng một mức khó bị coi là ngẫu nhiên hơn.

> [!warning]
> Đừng nhầm một cụm RB với một vùng đang bị "ăn mòn" (mitigated nhiều lần). Nếu các nến trong cụm xảy ra rải rác qua nhiều phiên với các nhịp đảo ngược ở giữa, đó có thể là một vùng equal highs/lows bị test nhiều lần chứ không phải một cụm từ chối liên tục thật. Cụm RB hợp lệ nên hình thành trong một khoảng thời gian ngắn, liên tục, ngay trước nhịp displacement rời đi.

### Nâng cao — Rejection Block vs Turtle Soup: cùng logic sweep-and-reverse nhưng khác vai trò

[[33 - Turtle Soup]] và Rejection Block thường bị dùng lẫn lộn vì cả hai đều xoay quanh logic "quét thanh khoản rồi đảo chiều" (sweep-and-reverse). Nhưng chúng thuộc hai phạm trù khác nhau:

- **Turtle Soup là một ENTRY MODEL / PATTERN** — một cấu trúc setup cụ thể: giá phá giả (false breakout) qua một swing point đã định nghĩa trước, rồi đảo chiều trở lại trong khung cấu trúc đó. Nó có điều kiện vào lệnh, stop, target theo một kịch bản pattern rõ ràng.
- **Rejection Block là một PD-ARRAY / ZONE** — một vùng giá được đánh dấu bởi wick còn sót lại từ một cú từ chối, dùng làm POI để retest bất cứ khi nào giá quay lại, không gắn với một pattern entry cụ thể nào.

Trong nhiều trường hợp, **cây nến đảo chiều của một setup Turtle Soup chính là thứ tạo ra một Rejection Block** — hai khái niệm chồng lấp và củng cố lẫn nhau: Turtle Soup cho bạn *bối cảnh pattern* (đã phá giả swing nào, trong cấu trúc nào), còn RB cho bạn *vùng giá cụ thể* để canh re-entry nếu bỏ lỡ entry ban đầu hoặc muốn thêm vị thế khi giá retest.

Nhưng chúng **không phải là từ đồng nghĩa**:
- Bạn có thể có một **RB không đi kèm Turtle Soup** chính thức — ví dụ một wick từ chối xuất hiện giữa một nhịp tiếp diễn trend (continuation), không phải một cú phá giả swing point theo đúng kịch bản Turtle Soup.
- Bạn cũng có thể có một **setup Turtle Soup không để lại RB textbook** — false breakout xảy ra nhưng nến đảo chiều lại có body lớn, wick ngắn (không đủ tỉ lệ wick/body để gọi là RB rõ ràng), dù pattern Turtle Soup vẫn hợp lệ về mặt cấu trúc.

| Tiêu chí | **Turtle Soup** | **Rejection Block** |
|---|---|---|
| Bản chất | Entry model / pattern (false breakout + reversal) | PD-array / zone (vùng wick từ chối) |
| Điều kiện | Phá giả một swing point cụ thể trong cấu trúc | Có wick dài tại swing high/low, không bắt buộc phá giả một swing đã định nghĩa |
| Dùng để | Kích hoạt entry theo kịch bản pattern | Đánh dấu vùng POI để retest, dùng lại nhiều lần |
| Khi nào chồng lấp | Nến đảo chiều của Turtle Soup tạo ra RB | RB xuất hiện đúng tại điểm phá giả của Turtle Soup |
| Khi nào tách biệt | Reversal candle body lớn, không để lại wick rõ | RB trong nhịp continuation, không phải phá giả swing |

> [!note]
> Câu hỏi thực chiến: khi thấy một wick dài tại swing high/low, hỏi thêm *"Đây có phải một cú phá giả (false breakout) đúng kịch bản Turtle Soup không, hay chỉ là một cú từ chối bình thường giữa xu hướng?"* Câu trả lời không đổi vùng RB bạn vẽ, nhưng đổi cách bạn đặt kỳ vọng và quản trị lệnh — Turtle Soup cho một kịch bản entry đầy đủ, còn RB đơn thuần chỉ cho một vùng giá để phản ứng.

![[RejectionBlock-Advanced-vs-TurtleSoup.svg]]
*Hai vòng tròn chồng lấp: Turtle Soup (entry model dựa trên false breakout + reversal trong cấu trúc cụ thể) và Rejection Block (PD-array đánh dấu vùng wick từ chối). Vùng giao nhau là nơi nến đảo chiều của một Turtle Soup chính là một Rejection Block — nhưng mỗi khái niệm vẫn có phần riêng không phụ thuộc khái niệm kia.*

---

## 6. Ví dụ chart

### Ví dụ đúng
![[RejectionBlock-Example-Correct.svg]]

**Mô tả:** Bullish RB tại đáy một down-move, sau khi giá quét sell-side rồi reject lên.
- Giá đâm xuống quét [sell-side liquidity] tại [level], in **wick dưới dài**.
- Nến đóng cửa quay lại → để lại RB zone (mép body → low wick) ở [range] – [range].
- Sau đó có MSS lên tại [level] xác nhận đảo chiều.
- Giá pullback về **mép body RB**, vào Long, SL dưới low wick [____], TP về buy-side [____].
- R đạt được: [____].

### Ví dụ sai
![[RejectionBlock-Example-Wrong.svg]]

**Mô tả:** Vào lệnh tại "wick dài" nhưng thiếu bối cảnh — RB giả.
- Wick xuất hiện **không quét thanh khoản** nào (chỉ là noise giữa range).
- Vào ngược [[27 - Premium Discount]] (Long ở premium) và ngược bias HTF.
- Không có MSS xác nhận; ngay sau đó giá **đóng cửa vượt wick extreme** → RB bị vô hiệu.
- Kết quả: stop tại [____], lệnh thua vì confluence rỗng.

### Giải phẫu (tùy chọn)
![[RejectionBlock-Anatomy.svg]]

**Mô tả:** Cấu trúc một Bearish RB.
- Phần **wick trên** = vùng từ chối / sweep buy-side.
- Phần **body** = entry zone (mép open/close).
- **High của wick** = invalidation (đóng trên = chết).

---

## 7. Entry model liên quan

- [[ICT 2022 Model]] — RB là một dạng POI thay thế OB trong chuỗi sweep → MSS → re-entry.
- [[Order Block]] — POI "anh em"; chọn RB khi từ chối qua wick, OB khi qua body.
- [[Optimal Trade Entry]] — tinh chỉnh entry trong vùng RB bằng vùng OTE.
- [[Fair Value Gap]] — FVG trùng RB tạo confluence entry mạnh.
- [[33 - Turtle Soup]] — logic sweep-and-reverse rất hợp với RB sau sweep.
- [[Breaker Block]] — nếu RB/OB cũ bị phá rồi flip, chuyển sang đọc breaker.

```text
[SEQUENCE — RB RE-ENTRY]
1. Bias (D1/H4) + xác định premium/discount
2. Giá tới vùng thanh khoản → SWEEP (wick dài)
3. Reject + MSS (LTF) xác nhận đảo chiều
4. Pullback về MÉP BODY của RB (± FVG/OTE)
5. Entry → SL sau WICK EXTREME → TP thanh khoản đối diện
6. Quản trị: dời SL, partial tại TP1
```

> [!note] Ghi nhớ
> RB hiếm khi đứng một mình. Sức mạnh thật đến khi **RB + sweep + MSS + đúng premium/discount** xếp chồng. Một mình "wick dài" không phải là edge.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không vào lệnh nếu chưa qua đủ checklist
> Mỗi mục bỏ qua là một lần hạ xác suất. RB thiếu confluence = RB giả.

**A. Bối cảnh (HTF)**
- [ ] [[12 - Daily Bias]] rõ ràng, RB cùng hướng bias.
- [ ] Giá đúng phía [[27 - Premium Discount]] (Bullish RB ở discount / Bearish RB ở premium).
- [ ] RB có confluence với POI HTF (OB/FVG/RB khung lớn).

**B. Cấu trúc & tín hiệu (LTF)**
- [ ] Wick đã **quét thanh khoản** thực sự.
- [ ] Có phản ứng đảo chiều + [[21 - Market Structure Shift]] xác nhận.
- [ ] Vùng RB chưa bị đóng cửa vượt wick extreme.
- [ ] Đang trong [[18 - Kill Zones]] (ưu tiên).

**C. Quản trị & kỷ luật**
- [ ] Entry, SL (sau wick extreme), TP đã xác định trước.
- [ ] Risk ≤ 0.5% / trade; R dự kiến hợp lý (≥ [____]R).
- [ ] Không vi phạm daily/weekly loss limit; tâm lý ổn định.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Nhầm RB với [[Order Block]] | Vẽ vào body thay vì wick | Sai vùng entry & invalidation | RB = wick; OB = body. Kiểm lại phần nến dùng |
| Coi mọi wick dài là RB | Vào lệnh ở wick giữa range | Không có logic sweep → noise | Chỉ RB tại swing có quét thanh khoản |
| Bỏ qua premium/discount | Long ở premium / Short ở discount | Vào ngược dòng tiền | Luôn lọc theo [[27 - Premium Discount]] + bias |
| Không chờ MSS | Vào ngay khi thấy wick | Bắt dao rơi, không xác nhận đảo | Chờ [[21 - Market Structure Shift]] LTF |
| Đặt SL sai chỗ | SL ở mép body, không phải wick | Dễ bị quét bởi wick mới | SL **sau** wick extreme |
| Phớt lờ invalidation | Giữ lệnh sau khi đóng vượt extreme | RB đã chết, lỗ lan rộng | Đóng nến vượt extreme = thoát ngay |
| Dùng RB thay vì OB tốt hơn | Bỏ OB body sạch để chọn wick | Mất POI chất lượng cao hơn | Có OB + displacement rõ → ưu tiên OB |
| RB đã mitigated | Vùng đã retest nhiều lần | Lực còn lại rất yếu | Ưu tiên RB còn "tươi" (fresh) |

---

## 10. Câu hỏi tự kiểm tra
1. RB lấy phần nào của nến, và khác [[Order Block]] ở chỗ nào?
2. Bullish RB hình thành ở đâu và wick hướng nào? Còn Bearish RB?
3. Cách vẽ vùng RB (mốc nào là entry, mốc nào là invalidation)?
4. Vì sao wick dài thường liên quan đến [[20 - Liquidity Sweep]]?
5. Điều gì làm một RB **vô hiệu hóa** dứt khoát?
6. Khi nào nên chọn RB thay vì OB, và ngược lại?
7. RB khác [[Breaker Block]] thế nào về cấu trúc và bối cảnh?
8. Những confluence nào nâng RB từ "noise" thành "edge"?

---

## 11. Flashcards / Active Recall
> **Q1.** Rejection Block được định nghĩa bởi phần nào của nến?
> **A1.** Phần **wick/tail** (đuôi nến) tại swing high/low — không phải body như OB.

> **Q2.** Vẽ vùng Bullish RB từ đâu tới đâu?
> **A2.** Từ **mép body dưới (open/close thấp)** xuống **low của wick** tại đáy down-move.

> **Q3.** Bearish RB hình thành ở đâu?
> **A3.** Ở **đỉnh** một up-move, với **wick trên dài** (giá bị từ chối xuống). POI cho Short.

> **Q4.** Wick dài của RB thường là dấu vết của điều gì?
> **A4.** Một **[[20 - Liquidity Sweep]]** (stop run) — giá đâm lấy thanh khoản rồi quay lại.

> **Q5.** Điều kiện vô hiệu hóa RB là gì?
> **A5.** **Body đóng cửa vượt khỏi wick extreme** (dưới low wick / trên high wick).

> **Q6.** Đặt SL ở đâu khi giao dịch RB?
> **A6.** **Sau wick extreme** (không phải mép body), để tránh bị quét bởi wick mới.

---

## 12. Lesson Learned
> [!example] Ghi chú khi áp dụng thực chiến
> - Trade tham chiếu: [[ ]]
> - RB loại: [bullish/bearish] tại [level]
> - Sweep gì: [____] | MSS xác nhận: [____]
> - Kết quả & R: [____]
> - Điều rút ra: ____
> - Cần cải thiện: ____

---

## 13. Mức độ thành thạo

| Cấp độ | Mô tả | Đạt? |
|---|---|---|
| Seed | Hiểu định nghĩa RB & khác biệt với OB | [ ] |
| Developing | Vẽ đúng RB, lọc theo premium/discount + sweep | [ ] |
| Tested | Đã backtest ≥ [N] mẫu, có thống kê win-rate | [ ] |
| Mastered | Vào lệnh RB nhất quán theo [[ICT 2022 Model]], tự sửa lỗi | [ ] |

**Review plan**
- [ ] Backtest ≥ [N] mẫu RB (cả bullish & bearish) trên NQ1/EURUSD/XAUUSD.
- [ ] Lập bảng so sánh RB vs OB tại cùng điểm đảo (cái nào holds tốt hơn).
- [ ] Cập nhật `confidence` và `last_reviewed` sau mỗi đợt ôn.
- [ ] Đánh dấu 3 ví dụ chart (đúng/sai/anatomy) thật từ journal.

---

## Best Practices

> [!success] Nguyên tắc vàng
> **RB là wick, không phải body — và một wick chỉ đáng tin khi nó vừa quét thanh khoản có ý nghĩa, vừa đủ lớn theo tỉ lệ định lượng, vừa được MSS xác nhận.** Thiếu bất kỳ điều nào trong ba điều đó, "RB" chỉ là một cái tên gắn cho noise; đủ cả ba, RB trở thành một trong những POI có edge thật trong bộ công cụ ICT.

1. **Luôn xác nhận wick đã quét một mức thanh khoản có ý nghĩa trước khi gọi nó là RB.** Một wick dài giữa range, không chạm equal highs/lows, không chạm swing cũ nào, chỉ là biến động ngẫu nhiên. Hỏi rõ: *"Wick này vừa lấy [[19 - Liquidity]] gì — buy-side hay sell-side, ở mức nào?"* Nếu không trả lời được, đừng vẽ RB. Ghi trường `liquidity_swept` (loại + mức) vào journal cho mỗi RB đã trade để sau này lọc ra nhóm "RB không sweep" và so win-rate.

2. **Định lượng tỉ lệ wick/body thay vì eyeball "wick dài".** Dùng ngưỡng cụ thể: wick ≥ 2x body, wick ≥ 60-70% tổng range, hoặc dài bất thường so với range trung bình 10-20 nến gần nhất. Một wick "dài" trên M1 giữa phiên Á yên tĩnh có thể chỉ tương đương noise bình thường trên một nến tin tức H1. Ghi `wick_body_ratio` cho từng lệnh và xây ngưỡng riêng theo khung thời gian/thị trường bạn hay trade.

3. **Ưu tiên cụm RB (rejection shelf) hơn một wick spike đơn lẻ khi cả hai đều có mặt.** Một cụm 2-4 nến cùng từ chối gần một mức phản ánh nhiều lần thử và hấp thụ thanh khoản hơn — dấu chân institutional rõ hơn một cú spike đơn. Khi phải chọn POI giữa một RB đơn và một RB cụm ở cùng khu vực, nghiêng về phía cụm, miễn là cụm hình thành liên tục trong thời gian ngắn chứ không rải rác qua nhiều phiên.

4. **Không tin một RB cho tới khi có [[21 - Market Structure Shift]] / Break of Structure xác nhận.** Wick dài chỉ là bằng chứng của sự từ chối tại một thời điểm; nó không tự động nói lên cấu trúc đã đảo. Vào lệnh ngay khi thấy wick mà chưa có MSS là bắt dao rơi. Ghi `mss_confirmed: yes/no` cho mỗi lệnh RB và so sánh nhóm có MSS với nhóm không — gần như chắc chắn nhóm không MSS sẽ kéo win-rate xuống.

5. **Đặt stop nghiêm ngặt sau wick extreme, không phải mép body.** Đây là lỗi kinh điển nhất khi giao dịch RB: đặt SL sát mép body cho "gọn" khiến lệnh dễ bị quét bởi một wick mới còn nằm trong logic của cùng RB. SL luôn nằm ngoài điểm xa nhất của wick (hoặc ngoài envelope nếu là cụm RB) — đó là ranh giới invalidation thật, không phải điểm entry.

6. **Coi Rejection Block và [[Order Block]] là hai POI anh em, không ép RB vào mọi chỗ.** Khi cùng một điểm đảo chiều vừa có một OB body sạch với displacement rõ, vừa có một wick dài, ưu tiên OB — nó thường cho vùng entry gọn hơn và ít bị "nhiễu wick mới" chi phối invalidation. Chỉ dùng RB làm POI chính khi sự từ chối thực sự thể hiện qua wick chứ không qua body sạch.

7. **Nhận diện đúng mối quan hệ RB với [[33 - Turtle Soup]] mà không đánh đồng hai khái niệm.** Turtle Soup là entry model (false breakout + reversal theo kịch bản cấu trúc); RB là PD-array (vùng wick để retest). Chúng chồng lấp khi nến đảo chiều của một Turtle Soup chính là RB, nhưng bạn có thể gặp RB không kèm Turtle Soup (trong continuation) và Turtle Soup không để lại RB textbook. Đừng gọi mọi RB là "Turtle Soup" hay ngược lại — mỗi cái có logic quản trị lệnh riêng.

8. **Log `wick_body_ratio`, loại cụm-hay-đơn, và kết quả từng lệnh RB, rồi review sau 20-30 mẫu trên NQ1/EURUSD/XAUUSD.** Chỉ dữ liệu thực chiến mới trả lời được các câu hỏi: ngưỡng wick/body nào cho win-rate tốt nhất trên từng thị trường? RB cụm có thực sự outperform RB đơn không? RB có kém tin cậy hơn OB tại cùng điểm đảo hay không? Đối chiếu kết quả với [[01 - Roadmap]] và cập nhật [[02 - Skill Metrics]] sau mỗi đợt review, đồng thời nâng `confidence` của note này khi đã có đủ bằng chứng thay vì để mãi ở mức seed.
