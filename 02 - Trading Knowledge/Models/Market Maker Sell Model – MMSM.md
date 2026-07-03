---
type: ict-concept
concept: Market Maker Sell Model – MMSM
aliases:
  - Market Maker Sell Model
  - MMSM
  - Market Maker Sell Model MMSM
  - MM Sell Model
tags:
  - trading/ict/concept
  - trading/study
  - "#MMSM"
  - "#MMXM"
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
  - MMXM
  - ICT 2022
  - AMD
  - OTE
markets:
  - NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-07-03
created: 2026-06-24
updated: 2026-07-03
related_concepts:
  - "[[02 - AMD]]"
  - "[[12 - Daily Bias]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[Order Block]]"
  - "[[27 - Premium Discount]]"
  - "[[15 - Inducement]]"
  - "[[33 - Turtle Soup]]"
  - "[[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]]"
  - "[[16 - Internal & External Range Liquidity (IRL & ERL)]]"
prerequisites:
  - "[[02 - AMD]]"
  - "[[19 - Liquidity]]"
  - "[[21 - Market Structure Shift]]"
common_mistakes:
  - "[[Mistake - Skip Liquidity Sweep]]"
  - "[[Mistake - Chase Displacement]]"
  - "[[Mistake - Trade Against Bias]]"
---

# Market Maker Sell Model – MMSM

> [!info] Refer Link
> [ICT Market Maker Sell Model (MMSM) — Step-by-Step Guide + PDF](https://innercircletrader.net/tutorials/ict-market-maker-sell-model/)

> [!summary] Tóm tắt 1 câu
> **MMSM là kịch bản đảo chiều GIẢM hoàn chỉnh của market maker: giá bị đẩy lên (buy program) để quét buy-side liquidity và xây "smart money high", rồi đảo chiều thành sell program đẩy giá xuống về sell-side liquidity — mình chỉ tham gia ở phía BÁN sau khi đỉnh đã được lập.**

> [!important] Nguyên tắc cốt lõi
> **MMSM có 2 nửa đối xứng quanh một SMART MONEY HIGH: (A) Buy Program kết thúc bằng cú sweep BSL tạo đỉnh → (B) Sell Program đẩy giá xuống qua các đợt re-distribution. Bạn KHÔNG mua ở nửa A; bạn chỉ BÁN ở nửa B sau khi có MSS giảm xác nhận đỉnh.**
> Đây là "bản đồ kịch bản một chiều sell" — không phải tín hiệu. Vào sai nửa (long trong buy program kéo dài) là cách thua điển hình. MMSM là ảnh phản chiếu của [[Market Maker Buy Model – MMBM]].

---

## 1. Định nghĩa

![[MMSM-ProgramCycle-FlowDiagram.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ dạng đường zig-zag mô tả một chu kỳ giá hoàn chỉnh theo chiều ngang: bắt đầu bằng một hộp "Original Consolidation" phía dưới bên trái, sau đó một chuỗi các đoạn tăng bậc thang đi lên (mỗi bậc gắn nhãn nhỏ "LRB"), tô màu xanh nhạt cho toàn bộ vùng này và ghi chú "Buy Program — Nửa A". Đỉnh của chuỗi bậc thang là một điểm sweep rõ ràng xuyên qua một đường ngang đánh dấu "BSL", có một vòng tròn nhấn mạnh ghi chữ "Smart Money High" ngay tại điểm đó. Từ điểm đó, vẽ mũi tên gãy xuống phá qua một đường ngang mảnh ghi "MSS giảm", sau đó là chuỗi các đoạn giảm bậc thang đi xuống (mỗi bậc gắn nhãn nhỏ "LRS"), tô màu đỏ nhạt cho vùng này và ghi chú "Sell Program — Nửa B", kết thúc ở một đường ngang phía dưới ghi "SSL / Original Consolidation (Target)". Đây là sơ đồ khái niệm minh họa cấu trúc mô hình, không phải chart giá thật.

**Khái niệm:**
Market Maker Sell Model (MMSM) là **mô hình hành vi giá** mô tả cách market maker tạo ra một đợt giảm giá lớn. ICT chia chu kỳ thành **Buy Program** (đẩy giá lên để gom thanh khoản phía trên) và **Sell Program** (đẩy giá xuống để phân phối về thanh khoản phía dưới). MMSM nhìn từ góc độ: "đỉnh đã hình thành xong, giờ là chu kỳ bán". Nó thuộc họ **MMXM**, là cặp đối xứng với [[Market Maker Buy Model – MMBM]].

**Cấu trúc 2 nửa quanh Smart Money High:**
1. **Original Consolidation:** vùng tích lũy ban đầu phía dưới, nơi market maker bắt đầu chương trình mua.
2. **Buy Program (nửa A):** chuỗi đợt tăng (mỗi đợt có một Low Risk Buy — LRB), giá đi lên bậc thang, quét dần các pool BSL.
3. **Smart Money High (SMH):** cú **sweep buy-side liquidity** cuối cùng tạo đỉnh thật — tâm điểm của mô hình.
4. **Sell Program (nửa B):** sau MSS giảm, giá đảo chiều xuống theo các đợt **re-distribution** (mỗi đợt có một Low Risk Sell — LRS tại FVG/OB).
5. **Target:** sell-side liquidity phía dưới (đáy cũ, equal lows, original consolidation).

**Bản chất:** market maker cần thanh khoản đối ứng để vào vị thế bán lớn. Họ tạo hưng phấn mua (buy program) để trader mua đuổi/đặt stop trên đỉnh → khi đủ thanh khoản, họ phân phối và đảo chiều, đẩy giá về sell-side liquidity để chốt lời. Trader ICT chỉ "đu" theo nửa sell.

**Mục đích trong ICT:**
- Cho một **khung kịch bản đảo chiều giảm** rõ ràng từ đáy narrative đến đỉnh rồi xuống lại.
- Giúp trader **không mua đỉnh**: nhận ra buy program sắp kết thúc để chuyển sang tư duy bán.
- Định nghĩa các điểm **LRS** (low risk sell) lặp lại trong sell program.

**Vì sao khái niệm này quan trọng:**
Nhiều trader thua vì **long đúng vào lúc buy program kết thúc** (mua đỉnh). MMSM dạy cách đọc khi nào "phe mua hết nhiên liệu" để lật sang bán, biến điểm thua tiềm năng thành điểm vào lệnh xác suất cao.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Buy program đã quét xong BSL và lập Smart Money High chưa?
- Đã có MSS giảm xác nhận chuyển sang Sell Program chưa?
- Đang ở đợt re-distribution thứ mấy, LRS tiếp theo ở FVG/OB nào?
- Sell-side liquidity target ở đâu, còn bao nhiêu room?

### MMSM không phải là gì
- Không phải tín hiệu bán bất cứ khi nào thấy giá tăng.
- Không phải lý do để "bắt đỉnh" trước khi có sweep BSL + MSS giảm.
- Không phải mô hình một timeframe — nó là narrative HTF→LTF.
- Không phải đối nghịch với trend: nó mô tả chính cách trend giảm được tạo ra.
- Không đảm bảo thắng; vẫn cần premium/discount + risk management.

### Vì sao mô hình này hoạt động — thanh khoản, Inducement & tính fractal của MMXM

> [!important] Đây là phần lý thuyết nền — hiểu WHY trước khi hỏi WHAT
> Trader mới thường học "sweep rồi MSS thì bán" như một công thức máy móc, nhưng buy program của MMSM hiếm khi chỉ có MỘT cú sweep sạch. Nó thường là một chuỗi các cú tăng, trong đó phần lớn là **bẫy (inducement)** chứ không phải đỉnh thật. Không hiểu cơ chế này, trader dễ bán nhầm vào một trong các bẫy đó rồi bị quét thêm một bậc nữa.

**Vì sao market maker cần cả một "chương trình" mua, không chỉ một cú quét:**
- Để đảo chiều một xu hướng tăng lớn thành giảm, các tổ chức lớn cần **khớp một khối lượng bán khổng lồ** mà không đẩy giá trượt quá xa. Điều đó đòi hỏi một lượng đối ứng mua tương xứng — và nguồn đối ứng lớn nhất trên thị trường luôn là **cụm lệnh dừng lỗ (stop-loss) của các vị thế Short đang mắc kẹt** nằm ngay trên các đỉnh cũ.
- Một cú sweep duy nhất hiếm khi đủ thanh khoản cho một cú đảo chiều lớn (HTF). Vì vậy giá thường phải "đi thu gom" qua **nhiều bậc thang tăng liên tiếp** (mỗi bậc là một LRB), mỗi bậc quét một cụm stop nhỏ hơn, trước khi tới cụm lớn nhất (nơi hình thành Smart Money High thật).

**Inducement — bẫy được thiết kế TRƯỚC Smart Money High thật:**
- ICT gọi các đỉnh trung gian trong buy program (không phải đỉnh cuối) là **[[15 - Inducement]]**: những đỉnh "đẹp", dễ nhìn thấy, khiến trader retail đặt lệnh bán sớm hoặc đặt stop ngay trên đó — chính những lệnh này lại trở thành thanh khoản để market maker tiếp tục đẩy giá lên bậc kế tiếp.
- Phân biệt Inducement với Smart Money High thật: sau khi quét Inducement, giá có thể tụt xuống nhưng **không đủ mạnh để tạo MSS giảm thật** (không phá được swing low có ý nghĩa, không có displacement + FVG rõ) — đây chỉ là một nhịp điều chỉnh kỹ thuật rồi tiếp tục tăng. Smart Money High thật là điểm sweep DUY NHẤT sau đó có MSS giảm + displacement hợp lệ.
- Đây cũng chính là ý tưởng đứng sau [[33 - Turtle Soup]]: một cú phá đỉnh giả (false break) rồi đảo chiều — về bản chất Turtle Soup mô tả đúng hành vi tại từng Inducement bên trong buy program, chỉ khác là ICT 2022 Model/Turtle Soup thường zoom vào một cú sweep đơn lẻ LTF, còn MMSM zoom ra để thấy toàn bộ chuỗi.

**Tính fractal của MMXM — MMSM có thể chỉ là một mảnh của mô hình lớn hơn:**
- Xem [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]]: cùng logic đó áp dụng cho đỉnh (Short Term High/Intermediate Term High/Long Term High). Mỗi cú sweep trong buy program tương ứng một đỉnh ngắn hạn; khi một đỉnh ngắn hạn bị phá bằng MSS giảm mạnh, nó có thể trở thành đỉnh trung hạn; và nếu tiếp tục giữ vững qua nhiều nhịp hồi lớn hơn, nó có thể được nhìn nhận là đỉnh dài hạn. Smart Money High của một MMSM trên H1 thường chỉ là một đỉnh ngắn/trung hạn — nó có thể chỉ là **một LRS bên trong một MMSM lớn hơn trên D1**, hoặc tệ hơn, chỉ là **một nhịp hồi bên trong nửa A của một MMBM D1** vẫn đang chạy.
- Hệ quả thực dụng: trước khi tin một Smart Money High H1/M15 là "đỉnh thật để bán mạnh tay", luôn phải hỏi: *"Đỉnh này đang đóng vai trò gì trên D1/H4 — nó là Smart Money High của một MMSM D1, hay chỉ là một nhịp hồi kỹ thuật (Inducement) bên trong một buy program D1 vẫn chưa kết thúc?"*

**Áp dụng thực dụng của lý thuyết này:**
- Trước phiên, đánh dấu SẴN tất cả các pool BSL "đẹp" (equal highs, đỉnh phiên trước) — đây thường chính là các Inducement mà đám đông sẽ bán sớm.
- Đừng bán ngay tại cú sweep đầu tiên bạn thấy trong ngày; hỏi xem đã có bao nhiêu bậc LRB trước đó, và liệu HTF (D1/H4) đã ở gần một pool BSL lớn, "đáng" để market maker dừng chương trình mua hay chưa.
- Chấp nhận rằng một số lệnh thua sẽ đến từ việc bán đúng Inducement — đây là chi phí hợp lý của việc học đọc chuỗi; điều quan trọng là luôn đặt stop hợp lý và không tăng size chỉ vì "tin chắc đỉnh đã tới".

---

## 2. Bối cảnh sử dụng

### Hai nửa & khái niệm tương ứng

| Giai đoạn | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| Đáy | Original Consolidation | [[19 - Liquidity]], [[12 - Dealing Range]] | SSL phía dưới ở đâu (target cuối)? |
| Nửa A | Buy Program (các LRB) | [[Order Block]], [[Fair Value Gap]], [[15 - Inducement]] | Giá đang tăng bậc thang quét BSL nào? Đây là Inducement hay SMH thật? |
| Đỉnh | Smart Money High | [[20 - Liquidity Sweep]], [[07 - Buy-side Liquidity]] | BSL cuối đã bị quét + reject chưa? |
| Chuyển pha | MSS giảm | [[21 - Market Structure Shift]], [[Displacement]] | Đã phá swing low gần nhất chưa? |
| Nửa B | Sell Program (các LRS) | [[Fair Value Gap]], [[Order Block]], [[Optimal Trade Entry]] | LRS tiếp theo ở FVG/OB nào? |
| Target | Sell-side liquidity | [[30 - Sell-side Liquidity]], [[16 - Internal & External Range Liquidity (IRL & ERL)]] | SSL/đáy cũ nào là target? Internal hay external? |

### Biến thể thường gặp
- **+ AMD:** buy program ~ pha manipulation/accumulation lên; SMH ~ distribution; sell program ~ markdown ([[02 - AMD]]).
- **+ ICT 2022 Model:** mỗi LRS là một chuỗi ICT 2022 thu nhỏ (sweep nhỏ → MSS → FVG → entry) ([[ICT 2022 Model]]).
- **+ OTE:** LRS tinh chỉnh bằng vùng OTE 62–79% của nhịp đẩy xuống ([[Optimal Trade Entry]]).
- **+ Silver Bullet / Kill Zones:** SMH hoặc các LRS thường rơi vào London/NY KZ ([[18 - Kill Zones]]).

> [!tip]
> Cách nhớ nhanh MMSM: **"Mua lên lấy đỉnh → Lập Smart Money High → Bán xuống từng bậc về đáy."** Bạn chỉ tham gia khi đã thấy đỉnh được lập (sweep BSL + MSS giảm), rồi bán các LRS.

### Khi nào mô hình này có giá trị cao?
- [ ] HTF bias đang chuyển sang Bearish / giá ở premium cao của dealing range lớn.
- [ ] Buy program đã quét một pool BSL lớn (equal highs, đỉnh cũ HTF).
- [ ] Có MSS giảm rõ ràng + displacement để lại FVG.
- [ ] Sell-side liquidity phía dưới rõ (target có room).
- [ ] Trong [[18 - Kill Zones]] (London/NY).

### Khi nào nên bỏ qua?
- [ ] Buy program còn đang chạy mạnh, chưa quét BSL chính → đừng bắt đỉnh.
- [ ] Chưa có MSS giảm (chỉ thấy tăng chậm lại).
- [ ] Giá ở discount HTF (đã xuống thấp) → room bán hẹp.
- [ ] Không xác định được sell-side target rõ ràng.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Original consolidation phía dưới** + SSL đánh dấu (target cuối của sell program).
2. **Buy program bậc thang:** chuỗi nhịp tăng, mỗi nhịp có OB/FVG mua (LRB), giá lên cao dần.
3. **Smart Money High:** cú sweep BSL cuối (thường là equal highs / đỉnh HTF) rồi reject mạnh.
4. **MSS giảm + displacement:** phá swing low gần nhất, để lại bearish FVG.
5. **Re-distribution:** các đợt pullback nhỏ về FVG/OB (LRS) trong khi giá tụt xuống.

### Ma trận nhận diện MMSM

| Giai đoạn | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Original Consolidation | Vùng đi ngang + SSL phía dưới | Không có target dưới → room kém |
| Buy Program | Tăng bậc thang, OB/FVG mua | Tăng dựng đứng không nghỉ → khó định LRS |
| Smart Money High | Sweep BSL + reject | Không sweep → đỉnh chưa chắc |
| MSS giảm | Phá swing low + FVG bearish | Chưa MSS → vẫn là buy program |
| Re-distribution | Pullback về FVG/OB rồi giảm tiếp | FVG bị lấp hẳn → chờ POI mới |

### Điều kiện bắt buộc
- [ ] Xác định được original consolidation + SSL target.
- [ ] Buy program đã quét BSL chính (Smart Money High).
- [ ] Có MSS giảm + displacement để lại FVG.
- [ ] Xác định LRS (FVG/OB) để vào.
- [ ] Sell-side liquidity target rõ.

### Điều kiện tăng xác suất
- [ ] SMH trùng HTF premium + HTF POI (OB/FVG D1/H4).
- [ ] MSS xảy ra trong kill zone.
- [ ] LRS trùng OTE 62–79% + FVG.
- [ ] Sell-side target có nhiều room (R:R cao).

### Điều kiện làm setup yếu đi
- Sweep BSL mờ, reject yếu (đỉnh chưa chắc).
- MSS chỉ là cú giảm nhẹ, không displacement.
- Quá nhiều FVG chồng chéo, LRS mơ hồ.
- Giá đã xuống gần SSL (room còn ít).

### Smart Money High thật vs. Inducement (sweep giả) — khung đánh giá khách quan hóa

![[MMSM-SmartMoneyHigh-RealVsFake-Comparison.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Chart minh họa 2 cột cạnh nhau. Bên trái "Smart Money High hợp lệ": giá xuyên lên trên một đường BSL cũ với bấc trên dài, sau đó 1–2 nến đóng cửa trở lại DƯỚI đường BSL đó (reject rõ), tiếp theo là một nhịp giảm phá hẳn qua swing low gần nhất kèm nến thân lớn để lại FVG — ghi chú "Reject nhanh + MSS thật". Bên phải "Inducement / sweep giả": giá cũng xuyên lên trên một đỉnh cũ, tụt xuống nhẹ vài nến nhưng KHÔNG phá qua swing low gần nhất (chỉ là pullback nông), rồi tiếp tục tăng cao hơn lên một đỉnh mới cao hơn — ghi chú "Tụt yếu, không MSS, buy program tiếp diễn". Đây là chart minh họa khái niệm, không phải dữ liệu giao dịch thật.

> [!important] Đây là bước dễ nhầm nhất trong toàn bộ mô hình
> Phần lớn lệnh thua theo MMSM đến từ việc **bán nhầm một Inducement** rồi tưởng đó là Smart Money High. Bốn tiêu chí dưới đây giúp khách quan hóa việc phân biệt, thay vì chỉ dựa vào cảm giác "giá tăng nhiều rồi, chắc sắp quay đầu".

**Tiêu chí 1 — Tốc độ và độ dứt khoát của reject:**
- SMH hợp lệ: giá đóng cửa trở lại DƯỚI mức BSL vừa quét trong vòng **1–2 nến** sau sweep (reject nhanh, dứt khoát).
- Inducement: giá tiếp tục đóng cửa TRÊN mức vừa quét trong nhiều nến liên tiếp (reject chậm hoặc không có) — đây là dấu hiệu buy program còn "nhiên liệu".

**Tiêu chí 2 — Chất lượng MSS ngay sau sweep:**
- SMH hợp lệ: nhịp tụt xuống sau sweep phải **phá qua một swing low có ý nghĩa gần nhất** (không phải chỉ là đáy của một cây nến đơn lẻ) kèm displacement + FVG rõ.
- Inducement: nhịp tụt xuống chỉ là pullback nông, không phá được swing low nào đáng kể, rồi giá tiếp tục tăng — đây thực chất là một LRB mới đang hình thành, không phải điểm đảo chiều.

**Tiêu chí 3 — "Độ sạch" và tuổi đời của pool bị quét:**
- SMH hợp lệ thường quét một pool BSL **rõ ràng, "nghỉ" lâu** (equal highs nhiều lần chạm, đỉnh HTF cũ D1/H4) — pool càng lớn, càng nhiều thanh khoản đối ứng, càng "đáng" để market maker dừng buy program tại đó.
- Inducement thường là một đỉnh nhỏ, mới hình thành gần đây (chỉ vài nến), ít lệnh dừng thật sự tích lũy — quét xong vẫn chưa đủ "nhiên liệu" để đảo chiều lớn.

**Tiêu chí 4 — Vị trí trong bối cảnh HTF (nested MMXM):**
- SMH hợp lệ nên trùng hoặc gần vùng premium cao của dealing range HTF (D1/H4), lý tưởng trùng một HTF POI (OB/FVG cũ).
- Nếu sweep chỉ xảy ra ở giữa dealing range HTF (chưa vào premium cao), khả năng cao đây vẫn là một LRB nội bộ, chưa phải Smart Money High thật của toàn bộ MMSM.

**Bảng quyết định nhanh:**

| Tiêu chí | Smart Money High hợp lệ | Inducement (bỏ qua) |
|---|---|---|
| Tốc độ reject | 1–2 nến, dứt khoát | Chậm hoặc không có |
| MSS sau sweep | Phá swing low rõ + FVG | Pullback nông, không phá |
| Độ sạch của pool | Equal highs / đỉnh HTF "nghỉ" lâu | Đỉnh nhỏ, mới hình thành |
| Vị trí HTF | Premium cao + HTF POI | Giữa dealing range |
| Hành động tiếp theo | Bán LRS đầu tiên | Coi là một LRB, chờ tiếp |

> [!tip]
> Nếu một cú sweep chỉ đạt 1–2/4 tiêu chí, đừng loại bỏ hoàn toàn — hạ cấp thành "có thể là LRB", đánh dấu lại và tiếp tục chờ. Chỉ khi đạt ≥3/4 tiêu chí mới nên coi đó là Smart Money High và bắt đầu tìm LRS để bán.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng MMSM
> 1. **Buy program đã quét BSL chính và lập Smart Money High chưa?**
> 2. **Đã có MSS giảm + displacement để lại FVG chưa?**
> 3. **LRS (FVG/OB) tiếp theo ở đâu, đúng premium không?**
> 4. **Sell-side target ở đâu, R:R bao nhiêu, có trong kill zone không?**

### D1 / H4 — Bias & Narrative
- **Bias:** đang chuyển/đang là Bearish (xem [[12 - Daily Bias]]).
- **Original consolidation & SSL:** vùng đáy và pool sell-side là target cuối.
- **Premium:** xác nhận giá đang ở nửa trên dealing range (vùng bán).

### H1 / M15 — POI & Context
- **BSL pool sẽ bị sweep:** đánh dấu equal highs / đỉnh cũ.
- **Chờ sweep + reject:** xác nhận Smart Money High.
- **MSS giảm + FVG:** ghi range FVG + CE, ví dụ `H1 bearish FVG 18120–18150, CE 18135`.

### M5 / M1 — Confirmation & Entry
- **LRS:** mỗi pullback về FVG/OB là một low risk sell; có thể chờ M5 MSS xác nhận.
- **Entry:** tại FVG (quanh CE) / OTE của nhịp đẩy xuống.
- **Stop:** trên điểm sweep / trên đầu kia FVG.
- **Target:** internal liquidity trước, sau đó SSL của original consolidation.

```text
Mẫu ghi nhanh — MMSM (Sell)
Bias (HTF): Bearish | Original consolidation SSL @ [level]
Location: Premium
(1) Buy program: quét BSL @ [level] → Smart Money High + reject
(2) MSS giảm phá [swing low] → bearish FVG
(3) LRS#1 FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop trên SMH / trên FVG
(5) Target: internal [..] → SSL [..] (original consolidation)
Kill zone: London / NY AM
Invalid: đóng nến trên Smart Money High
```

> [!warning]
> **Đừng long trong buy program nếu mục tiêu là MMSM.** Buy program là để TẠO đỉnh, không phải để bạn mua. Khi đã xác định kịch bản MMSM, nhiệm vụ duy nhất là chờ Smart Money High + MSS giảm rồi BÁN các LRS. Mua đỉnh = đi ngược chính kịch bản mình đang đọc.

### Mô hình biểu hiện khác nhau ra sao trên từng thị trường đang trade

![[MMSM-CrossMarket-Behavior-Comparison.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Bảng/sơ đồ 3 cột so sánh side-by-side một chu kỳ MMSM điển hình của NQ1/NDX, EURUSD/GBPUSD, và XAUUSD trong cùng khung thời gian intraday. Cột NQ1 vẽ một buy program ngắn, dốc, chỉ 2–3 bậc LRB trong vài giờ trước khi có Smart Money High. Cột FX vẽ một buy program trải dài nhiều phiên/nhiều ngày với các bậc LRB thoai thoải hơn. Cột XAUUSD vẽ một buy program bị "cắt ngang" đột ngột bởi một nến giật mạnh quanh giờ tin tức tạo Smart Money High ngay lập tức thay vì tăng bậc thang từ từ. Đây là sơ đồ minh họa hành vi thị trường mang tính khái niệm, không phải chart giá thật.

Cùng một kịch bản 2 nửa, nhưng **độ dài buy program, số bậc LRB, và cách Smart Money High hình thành** khác nhau đáng kể giữa các thị trường đang trade.

| Đặc tính | NQ1 / NDX (NAS100) | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Độ dài buy program điển hình | Ngắn, thường hoàn tất trong 1 phiên (vài giờ) | Dài hơn, có thể trải qua 1–3 ngày | Thất thường; có thể rất ngắn nếu có tin |
| Số bậc LRB trước SMH thật | Thường 2–4 bậc rõ ràng | Thường 1–2 bậc, thoai thoải | Có thể chỉ 1 bậc "gãy" đột ngột |
| Độ tin cậy của equal highs làm BSL | Cao, hình thành rõ trong phiên | Rất cao nhờ thanh khoản sâu | Trung bình, dễ bị "xuyên qua" do biến động |
| Rủi ro Inducement | Cao do nhiều bậc nhỏ liên tiếp, dễ nhầm | Trung bình, các bậc rõ ràng hơn | Cao quanh giờ tin — sweep + MSS có thể dồn vào vài phút |
| Kill zone hiệu quả nhất | NY AM, London Open | London Open, NY AM (giờ handoff) | London Open, NY AM, quanh giờ tin CPI/NFP/FOMC |
| Điều chỉnh thực dụng | Cần kiên nhẫn đếm đủ bậc LRB trước khi tin SMH; size nhỏ vì biến động nhanh | Có thể cần theo dõi qua nhiều phiên trước khi SMH hoàn tất; không sốt ruột | Ưu tiên chờ MSS + FVG rõ ràng ngay cả khi sweep diễn ra rất nhanh; nới stop vì wick dài |

> [!tip]
> Quy tắc thực dụng: **NQ1 → đếm đủ bậc LRB trước khi tin đỉnh; FX → kiên nhẫn theo dõi qua nhiều phiên; XAUUSD → SMH có thể tới rất nhanh quanh tin, nhưng vẫn phải chờ MSS + FVG mới vào, không bán ngay tại wick.**

### Biến thể nâng cao — MMSM lồng trong MMXM lớn hơn (Nested MMXM)

![[MMSM-Nested-MMXM-Diagram.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ 2 tầng lồng nhau kiểu "hộp trong hộp". Tầng ngoài cùng vẽ một chu kỳ MMBM D1 hoàn chỉnh và lớn (một buy program lớn kéo dài, đáy Smart Money Low ở đầu, xu hướng tăng chủ đạo). Bên trong pha "Buy Program" của MMBM D1 đó — tức là nhịp tăng chính — vẽ một chu kỳ MMSM H1 hoàn chỉnh và nhỏ hơn (một nhịp điều chỉnh giảm tạm thời có đủ sweep + MSS + LRS riêng của nó), ghi chú rõ "MMSM H1 chỉ là một LRB/nhịp điều chỉnh bên trong MMBM D1 lớn hơn — KHÔNG phải đảo chiều thật". Dùng màu khác nhau cho mỗi tầng. Đây là sơ đồ khái niệm minh họa tính fractal của họ MMXM, không phải chart giá thật.

> [!important] Đây là bẫy nâng cao nhất khi trade MMSM — nhầm điều chỉnh kỹ thuật với đảo chiều thật
> Vì MMXM có tính fractal (mỗi chu kỳ lớn chứa nhiều chu kỳ nhỏ hơn bên trong nó — xem thêm [[ICT 2022 Model]] phần Nested AMD), một MMSM hoàn chỉnh và "sạch" trên H1 hoàn toàn có thể chỉ là **một nhịp điều chỉnh bên trong nửa Buy Program của một MMBM D1 lớn hơn** vẫn đang chạy. Nếu bán theo MMSM H1 mà không kiểm tra ngữ cảnh D1, bạn đang bán ngược một trend tăng lớn hơn nhiều.

- **Cách kiểm tra:** trước khi tin một MMSM H1/M15 là đảo chiều thật, luôn xác định D1/H4 đang ở pha nào — nếu D1 đang trong một MMBM chưa hoàn tất (chưa có Smart Money Low + MSS tăng D1), thì MMSM H1 chỉ nên được coi là cơ hội **bán ngắn hạn để mua lại** (counter-trend scalp), không phải để giữ dài theo hướng sell program.
- **SMH kép/ba (compound Smart Money High):** đôi khi buy program không kết thúc bằng một sweep duy nhất mà bằng 2–3 lần quét gần bằng nhau (giống mô hình đỉnh đôi/đỉnh ba). Đây vẫn là MMSM hợp lệ — chỉ cần kiên nhẫn chờ MSS + displacement xác nhận sau lần quét CUỐI CÙNG, không phải lần đầu tiên trông giống đỉnh đôi.
- **Ứng dụng thực dụng:** khi phân tích đa khung thời gian (mục 4 phía trên), luôn xác định trước "MMSM này đang nằm ở tầng nào" — nếu chỉ là tầng trong (nested) của một MMBM lớn hơn, hạ kỳ vọng về R:R và độ dài của sell program, ưu tiên chốt lời sớm hơn thay vì giữ đến tận SSL của original consolidation lớn.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Buy program đã quét BSL chính → Smart Money High + reject.
- [ ] Có MSS giảm + displacement để lại bearish FVG.
- [ ] Entry tại LRS (retrace về FVG/OB), ở premium.
- [ ] Stop trên Smart Money High / trên FVG.
- [ ] Sell-side target rõ; R:R đạt kế hoạch.
- [ ] (Lý tưởng) trong kill zone + confluence OB/OTE.

### Setup bị vô hiệu khi
- [ ] Chưa có sweep BSL + MSS giảm (vẫn là buy program).
- [ ] Giá **đóng nến trên Smart Money High** → đỉnh bị phá, kịch bản hỏng.
- [ ] LRS FVG bị lấp hẳn mà giá không phản ứng.
- [ ] Entry ở discount / chase nhịp đẩy xuống.

### Mức độ "đủ kịch bản"

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Có SMH + MSS giảm + LRS sạch | **A+ sell** | Thực thi LRS theo plan |
| Có SMH nhưng chưa MSS giảm | **Chờ xác nhận** | Đừng bắt đỉnh non |
| MSS giảm nhưng chưa sweep BSL chính | **Nghi ngờ** | Có thể là pullback trong buy program (Inducement) |
| Đủ kịch bản nhưng đã gần SSL | **Hạ cấp** | Room ít, giảm size hoặc bỏ |
| Đủ kịch bản trên LTF nhưng D1/H4 vẫn trong MMBM chưa xong | **Hạ cấp (nested)** | Chỉ scalp ngắn, không giữ dài |

> [!note]
> MMSM mạnh nhất khi bạn vào ở **LRS đầu tiên** ngay sau MSS giảm tại Smart Money High — đó là điểm có R:R tốt nhất. Các LRS sau vẫn dùng được nhưng room giảm dần khi tiến về SSL.

---

## 6. Ví dụ chart

### Ví dụ đúng — Buy program → Smart Money High → MSS giảm → bán LRS về SSL
![[MMSM-Example-Correct-SweepMSSSellLRS.svg]]

**Mô tả:**
HTF bias chuyển Bearish, giá ở premium. **(1)** Buy program đẩy giá lên bậc thang, quét một pool **BSL (equal highs)** tạo **Smart Money High** rồi reject. **(2)** Một **MSS giảm + displacement** phá swing low gần nhất, để lại bearish FVG. **(3)** Giá pullback về FVG (LRS#1) → **entry**, stop trên SMH. **(4)** Sell program đẩy giá xuống về **SSL** của original consolidation.

**Vì sao đây là ví dụ tốt:**
- Đỉnh được xác nhận bằng **sweep BSL + reject** trước khi bán.
- Entry ở **LRS (retrace)**, đúng premium, không chase.
- Stop logic trên Smart Money High; target là sell-side liquidity rõ.

### Ví dụ sai / dễ nhầm — Bắt đỉnh giữa buy program, chưa có MSS giảm (bán nhầm Inducement)
![[MMSM-Example-Wrong-PrematureSellNoSMH.svg]]

**Mô tả lỗi:**
Trader thấy giá tăng "đã cao" nên **bán bắt đỉnh** giữa buy program, chưa hề có sweep BSL chính và chưa có MSS giảm — thực chất đó chỉ là một **Inducement**. Buy program tiếp tục một bậc nữa, quét luôn stop trên điểm bán. Đỉnh thật (Smart Money High) hình thành cao hơn.

**Bài học:**
- Không bắt đỉnh khi buy program chưa kết thúc (chưa sweep BSL + MSS giảm).
- "Tăng cao" không phải tín hiệu bán; **sweep + reject + MSS** mới là tín hiệu.
- Luôn chờ LRS sau khi đỉnh đã xác nhận, và luôn kiểm tra khung đánh giá ở mục 3 trước khi tin một đỉnh là Smart Money High.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[02 - AMD]]
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[07 - Buy-side Liquidity]]
- [[30 - Sell-side Liquidity]]
- [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[Displacement]]
- [[Fair Value Gap]]
- [[Order Block]]
- [[Optimal Trade Entry]]
- [[27 - Premium Discount]]
- [[18 - Kill Zones]]
- [[15 - Inducement]]
- [[33 - Turtle Soup]]
- [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]]
- [[ICT 2022 Model]]
- [[Market Maker Buy Model – MMBM]]

### Sequence mẫu — MMSM (đầy đủ)
```text
(1) Original consolidation + SSL target (đáy)
(2) Buy Program: các LRB đẩy giá lên bậc thang (một số là Inducement)
(3) Sweep BSL chính (+ reject nhanh) = Smart Money High
(4) MSS giảm + displacement → bearish FVG
(5) Sell Program: các LRS (retrace về FVG/OB, lý tưởng OTE)
(6) Entry tại LRS; Stop trên Smart Money High
(7) Target: Internal liquidity → SSL (original consolidation)
(+ Kill zone London/NY, + đồng hướng AMD, + kiểm tra không nested trong MMBM D1)
```

> [!note]
> MMSM và [[Market Maker Buy Model – MMBM]] là cặp đối xứng. Học một cái là hiểu cái kia (lật ngược). Chúng cùng thuộc họ MMXM và là "khung kịch bản" để gắn các chuỗi [[ICT 2022 Model]] nhỏ vào từng LRS/LRB.

---

## Best Practices

> [!summary]
> Đây là các thói quen ở mức chuyên nghiệp / chuẩn prop-firm — thứ phân biệt trader đọc đúng kịch bản MMSM một cách nhất quán với trader chỉ biết lý thuyết nhưng bán bừa mỗi khi thấy giá tăng nhiều. Mục tiêu cuối: không bán nhầm Inducement, không bán ngược một MMBM lớn hơn, và bảo toàn vốn qua vòng đánh giá prop-firm.

### Quy trình pre-session — map cả hai kịch bản (MMSM & MMBM) trước khi chọn phe

- Không bao giờ vào phiên với suy nghĩ "hôm nay chắc chắn là MMSM". Luôn map **cả hai kịch bản** trước, vì thị trường sẽ tự quyết định nó đang chạy chương trình nào.
- Trình tự pre-session đề xuất (15–30 phút trước London Open hoặc NY AM):
  1. Xem D1/H4: xác định bias hiện tại và xem D1 có đang ở giữa một MMBM chưa hoàn tất không (kiểm tra nested — mục 4).
  2. Đánh dấu tất cả pool BSL "đẹp" — đây là những ứng viên Inducement nhiều khả năng bị quét trước khi tới Smart Money High thật.
  3. Đánh dấu tất cả pool SSL phía dưới làm target cuối cho kịch bản MMSM.
  4. Viết sẵn cả kịch bản MMSM (nếu SMH hình thành) lẫn kịch bản "buy program vẫn tiếp diễn" (nếu SMH thất bại) vào Quick Reference Card.
  5. Xác định trước ngưỡng vô hiệu hóa: nếu giá đóng nến trên một mức cụ thể, kịch bản MMSM bị loại hoàn toàn cho phiên đó.
- Lợi ích: khi sweep xảy ra, bạn chỉ cần đối chiếu với kịch bản đã viết sẵn (đây có phải Inducement hay SMH thật theo 4 tiêu chí ở mục 3?) thay vì phân tích trong áp lực thời gian thực.

### Kỷ luật `missing_step` cho MMSM — biến review thành nghi thức hằng tuần

- Với mỗi lệnh MMSM thua/BE, bắt buộc điền `missing_step` (xem mục 13) — không để trống.
- Cuối mỗi tuần (xem [[07 - Reviews]]), thống kê tần suất từng giá trị: `smh` (chưa có Smart Money High thật, bán nhầm Inducement), `mss` (chưa có MSS giảm), `lrs` (vào sai vị trí LRS/chase), `target` (target sai/room hết), `nested` (bán ngược một MMBM lớn hơn).
- Nếu một giá trị chiếm >40% lệnh thua trong tuần, đó là **ưu tiên sửa số 1** của tuần kế tiếp — ghi vào Weekly Review và gắn `[[Mistake - ...]]` tương ứng.
- Sau 4–6 tuần, tần suất lỗi `smh` (bán nhầm Inducement) và `nested` (bán ngược HTF) nên giảm dần rõ rệt — đây là bằng chứng khách quan cho việc đọc chuỗi đang tiến bộ.

### Kỳ vọng thực tế: một MMSM hoàn chỉnh xảy ra bao lâu một lần

- MMSM là một **kịch bản HTF/hoàn chỉnh**, không phải một setup xuất hiện liên tục như ICT 2022 Model đơn lẻ. Kỳ vọng thực dụng theo thị trường:
  - NQ1/NDX: có thể thấy 1 chu kỳ MMSM/MMBM rõ ràng mỗi 1–3 ngày trên khung H1/H4; các LRS bên trong sell program thì thường xuyên hơn.
  - EURUSD/GBPUSD: một chu kỳ MMSM đầy đủ trên D1/H4 thường mất **vài ngày đến một tuần** để hoàn tất cả hai nửa.
  - XAUUSD: thất thường, phụ thuộc lịch tin — có thể một chu kỳ hoàn chỉnh chỉ diễn ra trong một phiên tin lớn.
- **Đừng ép một MMSM xuất hiện mỗi ngày.** Phần lớn thời gian, thị trường chỉ đang ở giữa buy program (chưa tới SMH) — nhiệm vụ lúc đó là quan sát và đánh dấu pool, không phải cố tìm lý do để bán.
- Quy tắc thực dụng: chỉ tính là "đã có một setup MMSM" khi đủ cả 4 câu hỏi ở đầu mục 4 — không tính các lần chỉ "trông giống" đỉnh.

### Scale confidence & size chỉ sau khi backtest đủ mẫu

- Không tăng size chỉ vì vài lần bán LRS liên tiếp thắng "cảm thấy đúng công thức". MMSM có nhiều biến thể (single SMH, compound SMH, nested trong MMBM lớn hơn) — mỗi biến thể cần được backtest riêng.
- Chuẩn tối thiểu trước khi tăng size: **≥ 30–50 mẫu backtest** cho MMSM (tag đầy đủ frontmatter `model: MMSM`, `smart_money_high`, `mss_down`, `missing_step`...) tổng hợp qua [[04 - Backtesting/_Backtest Dashboard]].
- Quy trình scale đề xuất: backtest đủ mẫu → forward test size tối thiểu 15–20 lệnh → chỉ khi cả hai giai đoạn khớp kỳ vọng mới tăng về mức chuẩn ≤0.5%/lệnh.

### Amateur habits vs. Professional habits khi trade MMSM

| Khía cạnh | Amateur (nghiệp dư) | Professional (chuyên nghiệp / chuẩn prop-firm) |
|---|---|---|
| Nhìn thấy giá tăng cao | Bán ngay vì "chắc sắp đảo chiều" | Kiểm tra đủ 4 tiêu chí ở mục 3 trước khi tin đó là SMH |
| Sau khi bán, giá tụt yếu | Giữ lệnh, hy vọng | Coi đó là dấu hiệu Inducement, cắt lỗ theo kế hoạch |
| Bối cảnh D1/H4 | Không kiểm tra, chỉ nhìn H1 | Luôn xác nhận không đang bán ngược một MMBM D1 (nested check) |
| Entry | Bán ngay tại điểm sweep | Chờ LRS — retrace về FVG/OB sau MSS |
| Số MMSM tìm mỗi ngày | Cố tìm 1 cái mỗi ngày, ép setup | Chấp nhận có ngày/tuần không có MMSM nào đủ chuẩn |
| Sau lệnh thua vì Inducement | Trade gỡ ngay tại bậc LRB tiếp theo | Dừng, ghi `missing_step: smh`, chờ SMH thật |
| Tăng size | Tăng ngay sau vài lệnh LRS thắng | Chỉ tăng sau ≥30–50 mẫu backtest xác nhận |

> [!tip]
> Nếu phải tóm gọn Best Practices thành một câu: **"Đếm đủ bậc, kiểm tra bối cảnh lớn hơn, chỉ bán khi Inducement đã bị loại trừ — không phải khi giá 'trông đã tăng đủ nhiều'."**

---

## 9. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì giá "đã tăng cao"
> Phải đủ kịch bản: Sweep BSL (Smart Money High) → MSS giảm → LRS. Một nhịp tăng chậm lại KHÔNG phải là MMSM.

### A. Context (HTF)
- [ ] Bias đang Bearish / chuyển Bearish.
- [ ] Original consolidation + SSL target đã xác định.
- [ ] Giá ở premium của dealing range.
- [ ] BSL pool (đỉnh/equal highs) đã đánh dấu.
- [ ] Đã kiểm tra D1/H4 không đang ở giữa một MMBM chưa hoàn tất (nested check).

### B. Execution (LTF)
- [ ] Buy program đã quét BSL chính → Smart Money High + reject.
- [ ] Đã đối chiếu SMH với 4 tiêu chí ở mục 3 (không phải Inducement).
- [ ] Có MSS giảm + displacement để lại FVG.
- [ ] LRS (FVG/OB) sạch, xác định CE; lý tưởng trùng OTE.
- [ ] Entry ở retrace về LRS, không chase.
- [ ] Stop trên Smart Money High / trên FVG.
- [ ] Sell-side target rõ; R:R đạt; trong kill zone.

### C. Quy tắc "không có lệnh"
- [ ] Chưa sweep BSL + MSS giảm → không bán.
- [ ] Đang long giữa buy program với ý định "đu MMSM" → mâu thuẫn, không trade.
- [ ] Giá ở discount / sát SSL (room ít) → cân nhắc bỏ.
- [ ] Chỉ vào được bằng chase → không trade.
- [ ] D1/H4 vẫn đang trong một MMBM chưa hoàn tất → chỉ scalp nhỏ hoặc bỏ qua.

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bắt đỉnh non | Bán khi buy program còn chạy | Chưa có Smart Money High | Chờ sweep BSL + MSS giảm |
| Bán nhầm Inducement | Bán ngay tại đỉnh trung gian đầu tiên | Tụt yếu, không MSS, giá tăng tiếp | Đối chiếu 4 tiêu chí SMH thật ở mục 3 |
| Long đỉnh | Mua đúng lúc buy program kết thúc | Đi ngược chính kịch bản MMSM | Nhận diện SMH để lật sang bán |
| Bỏ qua MSS giảm | Bán chỉ vì "tăng đã nhiều" | Đỉnh chưa xác nhận | Yêu cầu MSS + displacement |
| Chase sell program | Bán đuổi nhịp giảm | Bỏ bước LRS, R:R xấu | Chờ pullback về FVG/OB |
| Bán ở discount | Vào khi giá đã gần SSL | Room ít, R:R kém | Chỉ bán ở premium, LRS sớm |
| Bỏ qua nested MMBM | Bán theo MMSM H1 khi D1 vẫn tăng mạnh | Bán ngược trend lớn hơn | Kiểm tra D1/H4 trước khi tin SMH |
| Stop tùy tiện | Không đặt trên SMH | Bị quét vô lý | Stop trên Smart Money High |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = sell-side liquidity |

---

## 11. Câu hỏi tự kiểm tra

- Mình có phân biệt được buy program (nửa A) và sell program (nửa B) không?
- Smart Money High đã hình thành chưa (sweep BSL + reject), hay đây chỉ là một Inducement?
- Đã có MSS giảm + displacement để lại FVG chưa?
- LRS tiếp theo ở FVG/OB nào, đúng premium không?
- D1/H4 có đang ở giữa một MMBM lớn hơn chưa hoàn tất không (nested check)?
- Sell-side target ở đâu, R:R bao nhiêu?
- Mình đang định bán (đúng kịch bản) hay đang lỡ long đỉnh?
- Nếu không trade, lý do "No Trade" rơi vào giai đoạn nào?

---

## 12. Flashcards / Active Recall

### Q1
**Hỏi:** MMSM gồm mấy nửa và tâm điểm là gì?
**Đáp:** Hai nửa — Buy Program (tạo đỉnh) và Sell Program (đẩy xuống) — đối xứng quanh một **Smart Money High** (sweep BSL + reject).

### Q2
**Hỏi:** Trong MMSM mình được phép trade phía nào?
**Đáp:** Chỉ phía BÁN (Sell Program), sau khi Smart Money High đã xác nhận bằng sweep BSL + MSS giảm. Không mua trong buy program nếu đang đọc MMSM.

### Q3
**Hỏi:** LRS (Low Risk Sell) là gì?
**Đáp:** Điểm bán rủi ro thấp tại FVG/OB (lý tưởng trùng OTE) trong mỗi đợt re-distribution của sell program; mỗi LRS ~ một chuỗi ICT 2022 thu nhỏ.

### Q4
**Hỏi:** Điều gì làm kịch bản MMSM bị vô hiệu?
**Đáp:** Khi giá đóng nến **trên Smart Money High** (đỉnh bị phá), hoặc khi chưa hề có sweep BSL + MSS giảm.

### Q5
**Hỏi:** Vì sao bắt đỉnh giữa buy program là sai?
**Đáp:** Buy program tồn tại để quét nốt BSL và tạo đỉnh thật; bán trước khi nó kết thúc thường bị quét stop ở bậc tăng tiếp theo — đó là bán nhầm Inducement.

### Q6
**Hỏi:** Inducement khác Smart Money High thật ở điểm nào?
**Đáp:** Sau khi bị quét, Inducement chỉ tụt yếu, không phá được swing low (không MSS thật) rồi giá tiếp tục tăng; Smart Money High có reject nhanh + MSS giảm + displacement rõ ngay sau đó.

### Q7
**Hỏi:** Vì sao phải kiểm tra D1/H4 trước khi tin một MMSM H1?
**Đáp:** Vì MMXM có tính fractal — một MMSM H1 "sạch" có thể chỉ là một nhịp điều chỉnh (nested) bên trong buy program của một MMBM D1 lớn hơn vẫn chưa hoàn tất; bán theo nó là bán ngược trend HTF thật.

---

## 13. Liên kết với Trade Journal

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
> Nếu vault có folder riêng như `Trades`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: MMSM # MMBM | MMSM | ICT-2022 | OSOK | Venom
bias: bearish
program: sell # sell | buy
smart_money_high: true # đã có SMH chưa
mss_down: true # MSS giảm xác nhận
lrs_entry: true # vào tại LRS (FVG/OB)
entry_location: Premium
target: SSL
nested_htf_conflict: false # có đang bán ngược MMBM D1 lớn hơn không
rr_planned: 4.0
missing_step: none # none | smh | mss | lrs | target | nested
```

> [!tip]
> Với các lệnh thua theo MMSM, ghi `missing_step` để biết mình hay vào sai ở đâu — phổ biến nhất là vào khi **chưa có SMH** (bán nhầm Inducement) hoặc **chase sell program** (bỏ LRS).

---

## 14. Lesson Learned

### Bài học chính
- MMSM là **kịch bản đảo chiều giảm**: mua lên lấy đỉnh → lập Smart Money High → bán xuống về SSL.
- Chỉ tham gia **phía bán**, sau khi đỉnh đã xác nhận (sweep BSL + MSS giảm, không phải Inducement).
- Vào tại **LRS (retrace về FVG/OB)**, không chase sell program.
- Stop **trên Smart Money High**; target là sell-side liquidity.
- Luôn kiểm tra tính **fractal/nested** với D1/H4 trước khi tin một SMH LTF là đảo chiều thật.
- Mạnh nhất ở **LRS đầu tiên** sau MSS, trong kill zone, có confluence OB/OTE.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ bán sau khi thấy Smart Money High + MSS giảm, đã đối chiếu với 4 tiêu chí phân biệt Inducement.
- [ ] Tôi không long đỉnh khi đang đọc kịch bản MMSM.
- [ ] Tôi vào ở LRS, không đuổi nhịp giảm.
- [ ] Tôi đặt stop trên Smart Money High.
- [ ] Tôi kiểm tra D1/H4 trước khi tin một MMSM LTF là đảo chiều thật.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc nhở khi trade
> **"Đợi đỉnh được lập, rồi bán từng bậc. Không bắt đỉnh, không mua đỉnh, và luôn kiểm tra bức tranh lớn hơn."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt buy/sell program và SMH? |
| Nhận diện trên chart |  | Xác định đúng Smart Money High theo thời gian thực, phân biệt được Inducement? |
| Biết khi nào bỏ qua |  | Dám không bắt đỉnh khi chưa có SMH? |
| Kết hợp với context HTF |  | Ghép bias + premium + SSL target + kill zone + nested check? |
| Áp dụng vào trade thực tế |  | Entry có thật sự ở LRS sau MSS không? |
| Review sau trade |  | Có gắn `missing_step` và review bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup tag `[[Market Maker Sell Model – MMSM]]`.
- [ ] Review theo `missing_step`: hay sai ở SMH, Inducement, hay LRS.
- [ ] Thống kê win rate theo `program`, `entry_location`, và `nested_htf_conflict`.
- [ ] Cập nhật rule khi đủ mẫu.

---

## Appendix — MMSM Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Bias:** Bearish / chuyển Bearish
> **Original consolidation SSL (target):** @ ____
> **Location:** Premium?
> **D1/H4 nested check:** đang ở giữa MMBM lớn hơn? Yes/No
> **(1) Buy program — BSL quét:** @ ____ → Smart Money High? Yes/No (reject nhanh?)
> **(2) MSS giảm + displacement:** phá ____ → FVG? Yes/No
> **(3) LRS (FVG/OB):** [low]–[high], CE ____ ; OTE? ____
> **(4) Entry:** ____ ; Stop (trên SMH): ____
> **(5) Target:** internal ____ → SSL ____
> **Đủ kịch bản (SMH+MSS+LRS, không phải Inducement)?** Yes / No — thiếu: ____
> **Kill zone:** London / NY AM / NY PM
> **R:R dự kiến:**
> **No-trade condition:**
