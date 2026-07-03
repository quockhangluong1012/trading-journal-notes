---
type: ict-concept
concept: Market Maker Buy Model – MMBM
aliases:
  - Market Maker Buy Model
  - MMBM
  - Market Maker Buy Model MMBM
  - MM Buy Model
tags:
  - trading/ict/concept
  - trading/study
  - "#MMBM"
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

# Market Maker Buy Model – MMBM

> [!info] Refer Link
> [ICT Market Maker Buy Model (MMBM): How to Spot & Trade It](https://innercircletrader.net/tutorials/ict-market-maker-buy-model/)

> [!summary] Tóm tắt 1 câu
> **MMBM là kịch bản đảo chiều TĂNG hoàn chỉnh của market maker: giá bị bán xuống (sell program) để quét sell-side liquidity và xây "smart money low", rồi đảo chiều thành buy program đẩy giá lên về buy-side liquidity — mình chỉ tham gia ở phía MUA sau khi đáy đã được lập.**

> [!important] Nguyên tắc cốt lõi
> **MMBM có 2 nửa đối xứng quanh một SMART MONEY LOW: (A) Sell Program kết thúc bằng cú sweep SSL tạo đáy → (B) Buy Program đẩy giá lên qua các đợt re-accumulation. Bạn KHÔNG bán ở nửa A; bạn chỉ MUA ở nửa B sau khi có MSS tăng xác nhận đáy.**
> Đây là "bản đồ kịch bản một chiều buy" — không phải tín hiệu. Vào sai nửa (short trong sell program kéo dài) là cách thua điển hình.

---

## 1. Định nghĩa

![[MMBM-ProgramCycle-FlowDiagram.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ dạng đường zig-zag mô tả một chu kỳ giá hoàn chỉnh theo chiều ngang: bắt đầu bằng một hộp "Original Consolidation" phía trên bên trái, sau đó một chuỗi các đoạn giảm bậc thang đi xuống (mỗi bậc gắn nhãn nhỏ "LRS"), tô màu đỏ nhạt cho toàn bộ vùng này và ghi chú "Sell Program — Nửa A". Đáy của chuỗi bậc thang là một điểm sweep rõ ràng xuyên qua một đường ngang đánh dấu "SSL", có một vòng tròn nhấn mạnh ghi chữ "Smart Money Low" ngay tại điểm đó. Từ điểm đó, vẽ mũi tên bật lên phá qua một đường ngang mảnh ghi "MSS tăng", sau đó là chuỗi các đoạn tăng bậc thang đi lên (mỗi bậc gắn nhãn nhỏ "LRB"), tô màu xanh nhạt cho vùng này và ghi chú "Buy Program — Nửa B", kết thúc ở một đường ngang phía trên ghi "BSL / Original Consolidation (Target)". Đây là sơ đồ khái niệm minh họa cấu trúc mô hình, không phải chart giá thật.

**Khái niệm:**
Market Maker Buy Model (MMBM) là **mô hình hành vi giá** mô tả cách market maker tạo ra một đợt tăng giá lớn. ICT chia một chu kỳ giá thành hai chương trình (program): **Sell Program** (đẩy giá xuống để gom thanh khoản phía dưới) và **Buy Program** (đẩy giá lên để phân phối về thanh khoản phía trên). MMBM là toàn bộ kịch bản nhìn từ góc độ: "đáy đã hình thành xong, giờ là chu kỳ mua". Nó là một biến thể trong họ **MMXM** (Market Maker Models), cặp đôi với [[Market Maker Sell Model – MMSM]].

**Cấu trúc 2 nửa quanh Smart Money Low:**
1. **Original Consolidation:** vùng tích lũy ban đầu phía trên, nơi market maker bắt đầu chương trình bán.
2. **Sell Program (nửa A):** một chuỗi các đợt giảm (mỗi đợt thường có một Low Risk Sell — LRS), giá đi xuống theo bậc thang, quét dần các pool SSL.
3. **Smart Money Low (SML):** cú **sweep sell-side liquidity** cuối cùng tạo đáy thật — đây là tâm điểm của mô hình.
4. **Buy Program (nửa B):** sau MSS tăng, giá đảo chiều lên theo các đợt **re-accumulation** (mỗi đợt có một Low Risk Buy — LRB tại FVG/OB).
5. **Target:** buy-side liquidity phía trên (đỉnh cũ, equal highs, original consolidation).

**Bản chất:** market maker cần thanh khoản đối ứng để vào vị thế mua lớn. Họ tạo ra hoảng loạn bán (sell program) để các trader bán ra/đặt stop dưới đáy → khi đủ thanh khoản, họ hấp thụ và đảo chiều, đẩy giá về phía buy-side liquidity để chốt lời. Trader ICT chỉ "đu" theo nửa buy.

**Mục đích trong ICT:**
- Cho một **khung kịch bản đảo chiều tăng** rõ ràng từ đỉnh narrative đến đáy rồi lên lại.
- Giúp trader **không bán đáy**: nhận ra sell program sắp kết thúc để chuyển sang tư duy mua.
- Định nghĩa các điểm **LRB** (low risk buy) lặp lại trong buy program.

**Vì sao khái niệm này quan trọng:**
Nhiều trader thua vì **short đúng vào lúc sell program kết thúc** (bán đáy). MMBM dạy cách đọc khi nào "phe bán hết nhiên liệu" để lật sang mua, biến điểm thua tiềm năng thành điểm vào lệnh xác suất cao.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Sell program đã quét xong SSL và lập Smart Money Low chưa?
- Đã có MSS tăng xác nhận chuyển sang Buy Program chưa?
- Đang ở đợt re-accumulation thứ mấy, LRB tiếp theo ở FVG/OB nào?
- Buy-side liquidity target ở đâu, còn bao nhiêu room?

### MMBM không phải là gì
- Không phải tín hiệu mua bất cứ khi nào thấy giá giảm.
- Không phải lý do để "bắt đáy" trước khi có sweep SSL + MSS tăng.
- Không phải mô hình một timeframe — nó là narrative HTF→LTF.
- Không phải đối nghịch hoàn toàn với trend: nó mô tả chính cách trend tăng được tạo ra.
- Không đảm bảo thắng; vẫn cần premium/discount + risk management.

### Vì sao mô hình này hoạt động — thanh khoản, Inducement & tính fractal của MMXM

> [!important] Đây là phần lý thuyết nền — hiểu WHY trước khi hỏi WHAT
> Trader mới thường học "sweep rồi MSS thì mua" như một công thức máy móc, nhưng sell program của MMBM hiếm khi chỉ có MỘT cú sweep sạch. Nó thường là một chuỗi các cú giảm, trong đó phần lớn là **bẫy (inducement)** chứ không phải đáy thật. Không hiểu cơ chế này, trader dễ mua nhầm vào một trong các bẫy đó rồi bị quét thêm một bậc nữa.

**Vì sao market maker cần cả một "chương trình" bán, không chỉ một cú quét:**
- Để đảo chiều một xu hướng giảm lớn thành tăng, các tổ chức lớn cần **khớp một khối lượng mua khổng lồ** mà không đẩy giá trượt quá xa. Điều đó đòi hỏi một lượng đối ứng bán tương xứng — và nguồn đối ứng lớn nhất trên thị trường luôn là **cụm lệnh dừng lỗ (stop-loss) của các vị thế Long đang mắc kẹt** nằm ngay dưới các đáy cũ.
- Một cú sweep duy nhất hiếm khi đủ thanh khoản cho một cú đảo chiều lớn (HTF). Vì vậy giá thường phải "đi thu gom" qua **nhiều bậc thang giảm liên tiếp** (mỗi bậc là một LRS), mỗi bậc quét một cụm stop nhỏ hơn, trước khi tới cụm lớn nhất (nơi hình thành Smart Money Low thật).

**Inducement — bẫy được thiết kế TRƯỚC Smart Money Low thật:**
- ICT gọi các đáy trung gian trong sell program (không phải đáy cuối) là **[[15 - Inducement]]**: những đáy "đẹp", dễ nhìn thấy, khiến trader retail đặt lệnh mua sớm hoặc đặt stop ngay dưới đó — chính những lệnh này lại trở thành thanh khoản để market maker tiếp tục đẩy giá xuống bậc kế tiếp.
- Phân biệt Inducement với Smart Money Low thật: sau khi quét Inducement, giá có thể nảy lên nhưng **không đủ mạnh để tạo MSS tăng thật** (không phá được swing high có ý nghĩa, không có displacement + FVG rõ) — đây chỉ là một nhịp hồi kỹ thuật rồi tiếp tục giảm. Smart Money Low thật là điểm sweep DUY NHẤT sau đó có MSS tăng + displacement hợp lệ.
- Đây cũng chính là ý tưởng đứng sau [[33 - Turtle Soup]]: một cú phá đáy giả (false break) rồi đảo chiều — về bản chất Turtle Soup mô tả đúng hành vi tại từng Inducement bên trong sell program, chỉ khác là ICT 2022 Model/Turtle Soup thường zoom vào một cú sweep đơn lẻ LTF, còn MMBM zoom ra để thấy toàn bộ chuỗi.

**Tính fractal của MMXM — MMBM có thể chỉ là một mảnh của mô hình lớn hơn:**
- Xem [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )]]: mỗi cú sweep trong sell program tương ứng một **Short Term Low (STL)**; khi một STL bị phá bằng MSS mạnh, nó có thể trở thành **Intermediate Term Low (ITL)**; và nếu ITL đó tiếp tục giữ vững qua nhiều nhịp hồi lớn hơn, nó có thể được nhìn nhận là **Long Term Low (LTL)**. Smart Money Low của một MMBM trên H1 thường chỉ là một STL/ITL — nó có thể chỉ là **một LRB bên trong một MMBM lớn hơn trên D1**, hoặc tệ hơn, chỉ là **một nhịp hồi bên trong nửa A của một MMSM D1** vẫn đang chạy.
- Hệ quả thực dụng: trước khi tin một Smart Money Low H1/M15 là "đáy thật để mua mạnh tay", luôn phải hỏi: *"Đáy này đang đóng vai trò gì trên D1/H4 — nó là Smart Money Low của một MMBM D1, hay chỉ là một nhịp hồi kỹ thuật (Inducement) bên trong một sell program D1 vẫn chưa kết thúc?"*

**Áp dụng thực dụng của lý thuyết này:**
- Trước phiên, đánh dấu SẴN tất cả các pool SSL "đẹp" (equal lows, đáy phiên trước) — đây thường chính là các Inducement mà đám đông sẽ mua sớm.
- Đừng mua ngay tại cú sweep đầu tiên bạn thấy trong ngày; hỏi xem đã có bao nhiêu bậc LRS trước đó, và liệu HTF (D1/H4) đã ở gần một pool SSL lớn, "đáng" để market maker dừng chương trình bán hay chưa.
- Chấp nhận rằng một số lệnh thua sẽ đến từ việc mua đúng Inducement — đây là chi phí hợp lý của việc học đọc chuỗi; điều quan trọng là luôn đặt stop hợp lý và không tăng size chỉ vì "tin chắc đáy đã tới".

---

## 2. Bối cảnh sử dụng

### Hai nửa & khái niệm tương ứng

| Giai đoạn | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| Đỉnh | Original Consolidation | [[19 - Liquidity]], [[12 - Dealing Range]] | BSL phía trên ở đâu (target cuối)? |
| Nửa A | Sell Program (các LRS) | [[Order Block]], [[Fair Value Gap]], [[15 - Inducement]] | Giá đang giảm bậc thang quét SSL nào? Đây là Inducement hay SML thật? |
| Đáy | Smart Money Low | [[20 - Liquidity Sweep]], [[30 - Sell-side Liquidity]] | SSL cuối đã bị quét + reclaim chưa? |
| Chuyển pha | MSS tăng | [[21 - Market Structure Shift]], [[Displacement]] | Đã phá swing high gần nhất chưa? |
| Nửa B | Buy Program (các LRB) | [[Fair Value Gap]], [[Order Block]], [[Optimal Trade Entry]] | LRB tiếp theo ở FVG/OB nào? |
| Target | Buy-side liquidity | [[07 - Buy-side Liquidity]], [[16 - Internal & External Range Liquidity (IRL & ERL)]] | BSL/đỉnh cũ nào là target? Internal hay external? |

### Biến thể thường gặp
- **+ AMD:** sell program ~ pha manipulation/distribution xuống; SML ~ accumulation; buy program ~ distribution lên ([[02 - AMD]]).
- **+ ICT 2022 Model:** mỗi LRB chính là một chuỗi ICT 2022 thu nhỏ (sweep nhỏ → MSS → FVG → entry) ([[ICT 2022 Model]]).
- **+ OTE:** LRB tinh chỉnh bằng vùng OTE 62–79% của nhịp đẩy lên ([[Optimal Trade Entry]]).
- **+ Silver Bullet / Kill Zones:** SML hoặc các LRB thường rơi vào London/NY KZ ([[18 - Kill Zones]]).

> [!tip]
> Cách nhớ nhanh MMBM: **"Bán xuống lấy đáy → Lập Smart Money Low → Mua lên từng bậc về đỉnh."** Bạn chỉ tham gia khi đã thấy đáy được lập (sweep SSL + MSS tăng), rồi mua các LRB.

### Khi nào mô hình này có giá trị cao?
- [ ] HTF bias đang chuyển sang Bullish / giá ở discount sâu của dealing range lớn.
- [ ] Sell program đã quét một pool SSL lớn (equal lows, đáy cũ HTF).
- [ ] Có MSS tăng rõ ràng + displacement để lại FVG.
- [ ] Buy-side liquidity phía trên rõ (target có room).
- [ ] Trong [[18 - Kill Zones]] (London/NY).

### Khi nào nên bỏ qua?
- [ ] Sell program còn đang chạy mạnh, chưa quét SSL chính → đừng bắt đáy.
- [ ] Chưa có MSS tăng (chỉ thấy giảm chậm lại).
- [ ] Giá ở premium HTF (đã lên cao) → room mua hẹp.
- [ ] Không xác định được buy-side target rõ ràng.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Original consolidation phía trên** + BSL đánh dấu (target cuối của buy program).
2. **Sell program bậc thang:** chuỗi nhịp giảm, mỗi nhịp có OB/FVG bán (LRS), giá hạ thấp dần.
3. **Smart Money Low:** cú sweep SSL cuối (thường là equal lows / đáy HTF) rồi reclaim mạnh.
4. **MSS tăng + displacement:** phá swing high gần nhất, để lại bullish FVG.
5. **Re-accumulation:** các đợt pullback nhỏ về FVG/OB (LRB) trong khi giá leo lên.

### Ma trận nhận diện MMBM

| Giai đoạn | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Original Consolidation | Vùng đi ngang + BSL phía trên | Không có target trên → room kém |
| Sell Program | Giảm bậc thang, OB/FVG bán | Giảm dựng đứng không nghỉ → khó định LRB |
| Smart Money Low | Sweep SSL + reclaim | Không sweep → đáy chưa chắc |
| MSS tăng | Phá swing high + FVG bullish | Chưa MSS → vẫn là sell program |
| Re-accumulation | Pullback về FVG/OB rồi tăng tiếp | FVG bị lấp hẳn → chờ POI mới |

### Điều kiện bắt buộc
- [ ] Xác định được original consolidation + BSL target.
- [ ] Sell program đã quét SSL chính (Smart Money Low).
- [ ] Có MSS tăng + displacement để lại FVG.
- [ ] Xác định LRB (FVG/OB) để vào.
- [ ] Buy-side liquidity target rõ.

### Điều kiện tăng xác suất
- [ ] SML trùng HTF discount + HTF POI (OB/FVG D1/H4).
- [ ] MSS xảy ra trong kill zone.
- [ ] LRB trùng OTE 62–79% + FVG.
- [ ] Buy-side target có nhiều room (R:R cao).

### Điều kiện làm setup yếu đi
- Sweep SSL mờ, reclaim yếu (đáy chưa chắc).
- MSS chỉ là cú nảy nhẹ, không displacement.
- Quá nhiều FVG chồng chéo, LRB mơ hồ.
- Giá đã lên gần BSL (room còn ít).

### Smart Money Low thật vs. Inducement (sweep giả) — khung đánh giá khách quan hóa

![[MMBM-SmartMoneyLow-RealVsFake-Comparison.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Chart minh họa 2 cột cạnh nhau. Bên trái "Smart Money Low hợp lệ": giá xuyên xuống dưới một đường SSL cũ với bấc dưới dài, sau đó 1–2 nến đóng cửa trở lại TRÊN đường SSL đó (reclaim rõ), tiếp theo là một nhịp tăng phá hẳn qua swing high gần nhất kèm nến thân lớn để lại FVG — ghi chú "Reclaim nhanh + MSS thật". Bên phải "Inducement / sweep giả": giá cũng xuyên xuống dưới một đáy cũ, nảy lên nhẹ vài nến nhưng KHÔNG phá qua swing high gần nhất (chỉ là pullback nông), rồi tiếp tục giảm sâu hơn xuống một đáy mới thấp hơn — ghi chú "Nảy yếu, không MSS, sell program tiếp diễn". Đây là chart minh họa khái niệm, không phải dữ liệu giao dịch thật.

> [!important] Đây là bước dễ nhầm nhất trong toàn bộ mô hình
> Phần lớn lệnh thua theo MMBM đến từ việc **mua nhầm một Inducement** rồi tưởng đó là Smart Money Low. Bốn tiêu chí dưới đây giúp khách quan hóa việc phân biệt, thay vì chỉ dựa vào cảm giác "giá giảm nhiều rồi, chắc sắp quay đầu".

**Tiêu chí 1 — Tốc độ và độ dứt khoát của reclaim:**
- SML hợp lệ: giá đóng cửa trở lại TRÊN mức SSL vừa quét trong vòng **1–2 nến** sau sweep (reclaim nhanh, dứt khoát).
- Inducement: giá tiếp tục đóng cửa DƯỚI mức vừa quét trong nhiều nến liên tiếp (reclaim chậm hoặc không có) — đây là dấu hiệu sell program còn "nhiên liệu".

**Tiêu chí 2 — Chất lượng MSS ngay sau sweep:**
- SML hợp lệ: nhịp bật lên sau sweep phải **phá qua một swing high có ý nghĩa gần nhất** (không phải chỉ là đỉnh của một cây nến đơn lẻ) kèm displacement + FVG rõ.
- Inducement: nhịp bật lên chỉ là pullback nông, không phá được swing high nào đáng kể, rồi giá tiếp tục giảm — đây thực chất là một LRS mới đang hình thành, không phải điểm đảo chiều.

**Tiêu chí 3 — "Độ sạch" và tuổi đời của pool bị quét:**
- SML hợp lệ thường quét một pool SSL **rõ ràng, "nghỉ" lâu** (equal lows nhiều lần chạm, đáy HTF cũ D1/H4) — pool càng lớn, càng nhiều thanh khoản đối ứng, càng "đáng" để market maker dừng sell program tại đó.
- Inducement thường là một đáy nhỏ, mới hình thành gần đây (chỉ vài nến), ít lệnh dừng thật sự tích lũy — quét xong vẫn chưa đủ "nhiên liệu" để đảo chiều lớn.

**Tiêu chí 4 — Vị trí trong bối cảnh HTF (nested MMXM):**
- SML hợp lệ nên trùng hoặc gần vùng discount sâu của dealing range HTF (D1/H4), lý tưởng trùng một HTF POI (OB/FVG cũ).
- Nếu sweep chỉ xảy ra ở giữa dealing range HTF (chưa vào discount sâu), khả năng cao đây vẫn là một LRS nội bộ, chưa phải Smart Money Low thật của toàn bộ MMBM.

**Bảng quyết định nhanh:**

| Tiêu chí | Smart Money Low hợp lệ | Inducement (bỏ qua) |
|---|---|---|
| Tốc độ reclaim | 1–2 nến, dứt khoát | Chậm hoặc không có |
| MSS sau sweep | Phá swing high rõ + FVG | Pullback nông, không phá |
| Độ sạch của pool | Equal lows / đáy HTF "nghỉ" lâu | Đáy nhỏ, mới hình thành |
| Vị trí HTF | Discount sâu + HTF POI | Giữa dealing range |
| Hành động tiếp theo | Mua LRB đầu tiên | Coi là một LRS, chờ tiếp |

> [!tip]
> Nếu một cú sweep chỉ đạt 1–2/4 tiêu chí, đừng loại bỏ hoàn toàn — hạ cấp thành "có thể là LRS", đánh dấu lại và tiếp tục chờ. Chỉ khi đạt ≥3/4 tiêu chí mới nên coi đó là Smart Money Low và bắt đầu tìm LRB để mua.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng MMBM
> 1. **Sell program đã quét SSL chính và lập Smart Money Low chưa?**
> 2. **Đã có MSS tăng + displacement để lại FVG chưa?**
> 3. **LRB (FVG/OB) tiếp theo ở đâu, đúng discount không?**
> 4. **Buy-side target ở đâu, R:R bao nhiêu, có trong kill zone không?**

### D1 / H4 — Bias & Narrative
- **Bias:** đang chuyển/đang là Bullish (xem [[12 - Daily Bias]]).
- **Original consolidation & BSL:** vùng đỉnh và pool buy-side là target cuối.
- **Discount:** xác nhận giá đang ở nửa dưới dealing range (vùng mua).

### H1 / M15 — POI & Context
- **SSL pool sẽ bị sweep:** đánh dấu equal lows / đáy cũ.
- **Chờ sweep + reclaim:** xác nhận Smart Money Low.
- **MSS tăng + FVG:** ghi range FVG + CE, ví dụ `H1 bullish FVG 17850–17880, CE 17865`.

### M5 / M1 — Confirmation & Entry
- **LRB:** mỗi pullback về FVG/OB là một low risk buy; có thể chờ M5 MSS xác nhận.
- **Entry:** tại FVG (quanh CE) / OTE của nhịp đẩy.
- **Stop:** dưới điểm sweep / dưới đầu kia FVG.
- **Target:** internal liquidity trước, sau đó BSL của original consolidation.

```text
Mẫu ghi nhanh — MMBM (Buy)
Bias (HTF): Bullish | Original consolidation BSL @ [level]
Location: Discount
(1) Sell program: quét SSL @ [level] → Smart Money Low + reclaim
(2) MSS tăng phá [swing high] → bullish FVG
(3) LRB#1 FVG: [low]–[high], CE [mid]
(4) Entry: quanh CE / OTE; Stop dưới SML / dưới FVG
(5) Target: internal [..] → BSL [..] (original consolidation)
Kill zone: London / NY AM
Invalid: đóng nến dưới Smart Money Low
```

> [!warning]
> **Đừng short trong sell program nếu mục tiêu là MMBM.** Sell program là để TẠO đáy, không phải để bạn bán. Khi đã xác định kịch bản MMBM, nhiệm vụ duy nhất là chờ Smart Money Low + MSS tăng rồi MUA các LRB. Bán đáy = đi ngược chính kịch bản mình đang đọc.

### Mô hình biểu hiện khác nhau ra sao trên từng thị trường đang trade

![[MMBM-CrossMarket-Behavior-Comparison.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Bảng/sơ đồ 3 cột so sánh side-by-side một chu kỳ MMBM điển hình của NQ1/NDX, EURUSD/GBPUSD, và XAUUSD trong cùng khung thời gian intraday. Cột NQ1 vẽ một sell program ngắn, dốc, chỉ 2–3 bậc LRS trong vài giờ trước khi có Smart Money Low. Cột FX vẽ một sell program trải dài nhiều phiên/nhiều ngày với các bậc LRS thoai thoải hơn. Cột XAUUSD vẽ một sell program bị "cắt ngang" đột ngột bởi một nến giật mạnh quanh giờ tin tức tạo Smart Money Low ngay lập tức thay vì giảm bậc thang từ từ. Đây là sơ đồ minh họa hành vi thị trường mang tính khái niệm, không phải chart giá thật.

Cùng một kịch bản 2 nửa, nhưng **độ dài sell program, số bậc LRS, và cách Smart Money Low hình thành** khác nhau đáng kể giữa các thị trường đang trade.

| Đặc tính | NQ1 / NDX (NAS100) | EURUSD / GBPUSD | XAUUSD |
|---|---|---|---|
| Độ dài sell program điển hình | Ngắn, thường hoàn tất trong 1 phiên (vài giờ) | Dài hơn, có thể trải qua 1–3 ngày | Thất thường; có thể rất ngắn nếu có tin |
| Số bậc LRS trước SML thật | Thường 2–4 bậc rõ ràng | Thường 1–2 bậc, thoai thoải | Có thể chỉ 1 bậc "gãy" đột ngột |
| Độ tin cậy của equal lows làm SSL | Cao, hình thành rõ trong phiên | Rất cao nhờ thanh khoản sâu | Trung bình, dễ bị "xuyên qua" do biến động |
| Rủi ro Inducement | Cao do nhiều bậc nhỏ liên tiếp, dễ nhầm | Trung bình, các bậc rõ ràng hơn | Cao quanh giờ tin — sweep + MSS có thể dồn vào vài phút |
| Kill zone hiệu quả nhất | NY AM, London Open | London Open, NY AM (giờ handoff) | London Open, NY AM, quanh giờ tin CPI/NFP/FOMC |
| Điều chỉnh thực dụng | Cần kiên nhẫn đếm đủ bậc LRS trước khi tin SML; size nhỏ vì biến động nhanh | Có thể cần theo dõi qua nhiều phiên trước khi SML hoàn tất; không sốt ruột | Ưu tiên chờ MSS + FVG rõ ràng ngay cả khi sweep diễn ra rất nhanh; nới stop vì wick dài |

> [!tip]
> Quy tắc thực dụng: **NQ1 → đếm đủ bậc LRS trước khi tin đáy; FX → kiên nhẫn theo dõi qua nhiều phiên; XAUUSD → SML có thể tới rất nhanh quanh tin, nhưng vẫn phải chờ MSS + FVG mới vào, không mua ngay tại wick.**

### Biến thể nâng cao — MMBM lồng trong MMXM lớn hơn (Nested MMXM)

![[MMBM-Nested-MMXM-Diagram.svg]]
> [!info] Ảnh minh họa cần vẽ/dán tại đây
> Sơ đồ 2 tầng lồng nhau kiểu "hộp trong hộp". Tầng ngoài cùng vẽ một chu kỳ MMSM D1 hoàn chỉnh và lớn (một sell program lớn kéo dài, đỉnh Smart Money High ở đầu, xu hướng giảm chủ đạo). Bên trong pha "Sell Program" của MMSM D1 đó — tức là nhịp giảm chính — vẽ một chu kỳ MMBM H1 hoàn chỉnh và nhỏ hơn (một nhịp hồi tăng tạm thời có đủ sweep + MSS + LRB riêng của nó), ghi chú rõ "MMBM H1 chỉ là một LRS/nhịp hồi bên trong MMSM D1 lớn hơn — KHÔNG phải đảo chiều thật". Dùng màu khác nhau cho mỗi tầng. Đây là sơ đồ khái niệm minh họa tính fractal của họ MMXM, không phải chart giá thật.

> [!important] Đây là bẫy nâng cao nhất khi trade MMBM — nhầm hồi kỹ thuật với đảo chiều thật
> Vì MMXM có tính fractal (mỗi chu kỳ lớn chứa nhiều chu kỳ nhỏ hơn bên trong nó — xem thêm [[ICT 2022 Model]] phần Nested AMD), một MMBM hoàn chỉnh và "sạch" trên H1 hoàn toàn có thể chỉ là **một nhịp hồi kỹ thuật bên trong nửa Sell Program của một MMSM D1 lớn hơn** vẫn đang chạy. Nếu mua theo MMBM H1 mà không kiểm tra ngữ cảnh D1, bạn đang mua ngược một trend giảm lớn hơn nhiều.

- **Cách kiểm tra:** trước khi tin một MMBM H1/M15 là đảo chiều thật, luôn xác định D1/H4 đang ở pha nào — nếu D1 đang trong một MMSM chưa hoàn tất (chưa có Smart Money High + MSS giảm D1), thì MMBM H1 chỉ nên được coi là cơ hội **mua ngắn hạn để bán lại** (counter-trend scalp), không phải để giữ dài theo hướng buy program.
- **SML kép/ba (compound Smart Money Low):** đôi khi sell program không kết thúc bằng một sweep duy nhất mà bằng 2–3 lần quét gần bằng nhau (giống mô hình đáy đôi/đáy ba). Đây vẫn là MMBM hợp lệ — chỉ cần kiên nhẫn chờ MSS + displacement xác nhận sau lần quét CUỐI CÙNG, không phải lần đầu tiên trông giống đáy đôi.
- **Ứng dụng thực dụng:** khi phân tích đa khung thời gian (mục 4 phía trên), luôn xác định trước "MMBM này đang nằm ở tầng nào" — nếu chỉ là tầng trong (nested) của một MMSM lớn hơn, hạ kỳ vọng về R:R và độ dài của buy program, ưu tiên chốt lời sớm hơn thay vì giữ đến tận BSL của original consolidation lớn.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Sell program đã quét SSL chính → Smart Money Low + reclaim.
- [ ] Có MSS tăng + displacement để lại bullish FVG.
- [ ] Entry tại LRB (retrace về FVG/OB), ở discount.
- [ ] Stop dưới Smart Money Low / dưới FVG.
- [ ] Buy-side target rõ; R:R đạt kế hoạch.
- [ ] (Lý tưởng) trong kill zone + confluence OB/OTE.

### Setup bị vô hiệu khi
- [ ] Chưa có sweep SSL + MSS tăng (vẫn là sell program).
- [ ] Giá **đóng nến dưới Smart Money Low** → đáy bị phá, kịch bản hỏng.
- [ ] LRB FVG bị lấp hẳn mà giá không phản ứng.
- [ ] Entry ở premium / chase nhịp đẩy.

### Mức độ "đủ kịch bản"

| Quan sát | Trạng thái | Cách đọc hợp lý |
|---|---|---|
| Có SML + MSS tăng + LRB sạch | **A+ buy** | Thực thi LRB theo plan |
| Có SML nhưng chưa MSS tăng | **Chờ xác nhận** | Đừng bắt đáy non |
| MSS tăng nhưng chưa sweep SSL chính | **Nghi ngờ** | Có thể là bounce trong sell program (Inducement) |
| Đủ kịch bản nhưng đã gần BSL | **Hạ cấp** | Room ít, giảm size hoặc bỏ |
| Đủ kịch bản trên LTF nhưng D1/H4 vẫn trong MMSM chưa xong | **Hạ cấp (nested)** | Chỉ scalp ngắn, không giữ dài |

> [!note]
> MMBM mạnh nhất khi bạn vào ở **LRB đầu tiên** ngay sau MSS tăng tại Smart Money Low — đó là điểm có R:R tốt nhất. Các LRB sau vẫn dùng được nhưng room giảm dần khi tiến về BSL.

---

## 6. Ví dụ chart

### Ví dụ đúng — Sell program → Smart Money Low → MSS tăng → mua LRB về BSL
![[MMBM-Example-Correct-SweepMSSBuyLRB.svg]]

**Mô tả:**
HTF bias chuyển Bullish, giá ở discount. **(1)** Sell program đẩy giá xuống bậc thang, quét một pool **SSL (equal lows)** tạo **Smart Money Low** rồi reclaim. **(2)** Một **MSS tăng + displacement** phá swing high gần nhất, để lại bullish FVG. **(3)** Giá pullback về FVG (LRB#1) → **entry**, stop dưới SML. **(4)** Buy program đẩy giá lên về **BSL** của original consolidation.

**Vì sao đây là ví dụ tốt:**
- Đáy được xác nhận bằng **sweep SSL + reclaim** trước khi mua.
- Entry ở **LRB (retrace)**, đúng discount, không chase.
- Stop logic dưới Smart Money Low; target là buy-side liquidity rõ.

### Ví dụ sai / dễ nhầm — Bắt đáy giữa sell program, chưa có MSS tăng (mua nhầm Inducement)
![[MMBM-Example-Wrong-PrematureBuyNoSML.svg]]

**Mô tả lỗi:**
Trader thấy giá giảm "đã sâu" nên **mua bắt đáy** giữa sell program, chưa hề có sweep SSL chính và chưa có MSS tăng — thực chất đó chỉ là một **Inducement**. Sell program tiếp tục một bậc nữa, quét luôn stop dưới điểm mua. Đáy thật (Smart Money Low) hình thành thấp hơn.

**Bài học:**
- Không bắt đáy khi sell program chưa kết thúc (chưa sweep SSL + MSS tăng).
- "Giảm sâu" không phải tín hiệu mua; **sweep + reclaim + MSS** mới là tín hiệu.
- Luôn chờ LRB sau khi đáy đã xác nhận, và luôn kiểm tra khung đánh giá ở mục 3 trước khi tin một đáy là Smart Money Low.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[02 - AMD]]
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[30 - Sell-side Liquidity]]
- [[07 - Buy-side Liquidity]]
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
- [[Market Maker Sell Model – MMSM]]

### Sequence mẫu — MMBM (đầy đủ)
```text
(1) Original consolidation + BSL target (đỉnh)
(2) Sell Program: các LRS đẩy giá xuống bậc thang (một số là Inducement)
(3) Sweep SSL chính (+ reclaim nhanh) = Smart Money Low
(4) MSS tăng + displacement → bullish FVG
(5) Buy Program: các LRB (retrace về FVG/OB, lý tưởng OTE)
(6) Entry tại LRB; Stop dưới Smart Money Low
(7) Target: Internal liquidity → BSL (original consolidation)
(+ Kill zone London/NY, + đồng hướng AMD, + kiểm tra không nested trong MMSM D1)
```

> [!note]
> MMBM và [[Market Maker Sell Model – MMSM]] là cặp đối xứng. Học một cái là hiểu cái kia (lật ngược). Chúng cùng thuộc họ MMXM và là "khung kịch bản" để gắn các chuỗi [[ICT 2022 Model]] nhỏ vào từng LRB/LRS.

---

## Best Practices

> [!summary]
> Đây là các thói quen ở mức chuyên nghiệp / chuẩn prop-firm — thứ phân biệt trader đọc đúng kịch bản MMBM một cách nhất quán với trader chỉ biết lý thuyết nhưng mua bừa mỗi khi thấy giá giảm nhiều. Mục tiêu cuối: không mua nhầm Inducement, không mua ngược một MMSM lớn hơn, và bảo toàn vốn qua vòng đánh giá prop-firm.

### Quy trình pre-session — map cả hai kịch bản (MMBM & MMSM) trước khi chọn phe

- Không bao giờ vào phiên với suy nghĩ "hôm nay chắc chắn là MMBM". Luôn map **cả hai kịch bản** trước, vì thị trường sẽ tự quyết định nó đang chạy chương trình nào.
- Trình tự pre-session đề xuất (15–30 phút trước London Open hoặc NY AM):
  1. Xem D1/H4: xác định bias hiện tại và xem D1 có đang ở giữa một MMSM chưa hoàn tất không (kiểm tra nested — mục 4).
  2. Đánh dấu tất cả pool SSL "đẹp" — đây là những ứng viên Inducement nhiều khả năng bị quét trước khi tới Smart Money Low thật.
  3. Đánh dấu tất cả pool BSL phía trên làm target cuối cho kịch bản MMBM.
  4. Viết sẵn cả kịch bản MMBM (nếu SML hình thành) lẫn kịch bản "sell program vẫn tiếp diễn" (nếu SML thất bại) vào Quick Reference Card.
  5. Xác định trước ngưỡng vô hiệu hóa: nếu giá đóng nến dưới một mức cụ thể, kịch bản MMBM bị loại hoàn toàn cho phiên đó.
- Lợi ích: khi sweep xảy ra, bạn chỉ cần đối chiếu với kịch bản đã viết sẵn (đây có phải Inducement hay SML thật theo 4 tiêu chí ở mục 3?) thay vì phân tích trong áp lực thời gian thực.

### Kỷ luật `missing_step` cho MMBM — biến review thành nghi thức hằng tuần

- Với mỗi lệnh MMBM thua/BE, bắt buộc điền `missing_step` (xem mục 13) — không để trống.
- Cuối mỗi tuần (xem [[07 - Reviews]]), thống kê tần suất từng giá trị: `sml` (chưa có Smart Money Low thật, mua nhầm Inducement), `mss` (chưa có MSS tăng), `lrb` (vào sai vị trí LRB/chase), `target` (target sai/room hết), `nested` (mua ngược một MMSM lớn hơn).
- Nếu một giá trị chiếm >40% lệnh thua trong tuần, đó là **ưu tiên sửa số 1** của tuần kế tiếp — ghi vào Weekly Review và gắn `[[Mistake - ...]]` tương ứng.
- Sau 4–6 tuần, tần suất lỗi `sml` (mua nhầm Inducement) và `nested` (mua ngược HTF) nên giảm dần rõ rệt — đây là bằng chứng khách quan cho việc đọc chuỗi đang tiến bộ.

### Kỳ vọng thực tế: một MMBM hoàn chỉnh xảy ra bao lâu một lần

- MMBM là một **kịch bản HTF/hoàn chỉnh**, không phải một setup xuất hiện liên tục như ICT 2022 Model đơn lẻ. Kỳ vọng thực dụng theo thị trường:
  - NQ1/NDX: có thể thấy 1 chu kỳ MMBM/MMSM rõ ràng mỗi 1–3 ngày trên khung H1/H4; các LRB bên trong buy program thì thường xuyên hơn.
  - EURUSD/GBPUSD: một chu kỳ MMBM đầy đủ trên D1/H4 thường mất **vài ngày đến một tuần** để hoàn tất cả hai nửa.
  - XAUUSD: thất thường, phụ thuộc lịch tin — có thể một chu kỳ hoàn chỉnh chỉ diễn ra trong một phiên tin lớn.
- **Đừng ép một MMBM xuất hiện mỗi ngày.** Phần lớn thời gian, thị trường chỉ đang ở giữa sell program (chưa tới SML) — nhiệm vụ lúc đó là quan sát và đánh dấu pool, không phải cố tìm lý do để mua.
- Quy tắc thực dụng: chỉ tính là "đã có một setup MMBM" khi đủ cả 4 câu hỏi ở đầu mục 4 — không tính các lần chỉ "trông giống" đáy.

### Scale confidence & size chỉ sau khi backtest đủ mẫu

- Không tăng size chỉ vì vài lần mua LRB liên tiếp thắng "cảm thấy đúng công thức". MMBM có nhiều biến thể (single SML, compound SML, nested trong MMSM lớn hơn) — mỗi biến thể cần được backtest riêng.
- Chuẩn tối thiểu trước khi tăng size: **≥ 30–50 mẫu backtest** cho MMBM (tag đầy đủ frontmatter `model: MMBM`, `smart_money_low`, `mss_up`, `missing_step`...) tổng hợp qua [[04 - Backtesting/_Backtest Dashboard]].
- Quy trình scale đề xuất: backtest đủ mẫu → forward test size tối thiểu 15–20 lệnh → chỉ khi cả hai giai đoạn khớp kỳ vọng mới tăng về mức chuẩn ≤0.5%/lệnh.

### Amateur habits vs. Professional habits khi trade MMBM

| Khía cạnh | Amateur (nghiệp dư) | Professional (chuyên nghiệp / chuẩn prop-firm) |
|---|---|---|
| Nhìn thấy giá giảm sâu | Mua ngay vì "chắc sắp đảo chiều" | Kiểm tra đủ 4 tiêu chí ở mục 3 trước khi tin đó là SML |
| Sau khi mua, giá nảy yếu | Giữ lệnh, hy vọng | Coi đó là dấu hiệu Inducement, cắt lỗ theo kế hoạch |
| Bối cảnh D1/H4 | Không kiểm tra, chỉ nhìn H1 | Luôn xác nhận không đang mua ngược một MMSM D1 (nested check) |
| Entry | Mua ngay tại điểm sweep | Chờ LRB — retrace về FVG/OB sau MSS |
| Số MMBM tìm mỗi ngày | Cố tìm 1 cái mỗi ngày, ép setup | Chấp nhận có ngày/tuần không có MMBM nào đủ chuẩn |
| Sau lệnh thua vì Inducement | Trade gỡ ngay tại bậc LRS tiếp theo | Dừng, ghi `missing_step: sml`, chờ SML thật |
| Tăng size | Tăng ngay sau vài lệnh LRB thắng | Chỉ tăng sau ≥30–50 mẫu backtest xác nhận |

> [!tip]
> Nếu phải tóm gọn Best Practices thành một câu: **"Đếm đủ bậc, kiểm tra bối cảnh lớn hơn, chỉ mua khi Inducement đã bị loại trừ — không phải khi giá 'trông đã giảm đủ nhiều'."**

---

## 9. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì giá "đã giảm sâu"
> Phải đủ kịch bản: Sweep SSL (Smart Money Low) → MSS tăng → LRB. Một nhịp giảm chậm lại KHÔNG phải là MMBM.

### A. Context (HTF)
- [ ] Bias đang Bullish / chuyển Bullish.
- [ ] Original consolidation + BSL target đã xác định.
- [ ] Giá ở discount của dealing range.
- [ ] SSL pool (đáy/equal lows) đã đánh dấu.
- [ ] Đã kiểm tra D1/H4 không đang ở giữa một MMSM chưa hoàn tất (nested check).

### B. Execution (LTF)
- [ ] Sell program đã quét SSL chính → Smart Money Low + reclaim.
- [ ] Đã đối chiếu SML với 4 tiêu chí ở mục 3 (không phải Inducement).
- [ ] Có MSS tăng + displacement để lại FVG.
- [ ] LRB (FVG/OB) sạch, xác định CE; lý tưởng trùng OTE.
- [ ] Entry ở retrace về LRB, không chase.
- [ ] Stop dưới Smart Money Low / dưới FVG.
- [ ] Buy-side target rõ; R:R đạt; trong kill zone.

### C. Quy tắc "không có lệnh"
- [ ] Chưa sweep SSL + MSS tăng → không mua.
- [ ] Đang short giữa sell program với ý định "đu MMBM" → mâu thuẫn, không trade.
- [ ] Giá ở premium / sát BSL (room ít) → cân nhắc bỏ.
- [ ] Chỉ vào được bằng chase → không trade.
- [ ] D1/H4 vẫn đang trong một MMSM chưa hoàn tất → chỉ scalp nhỏ hoặc bỏ qua.

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bắt đáy non | Mua khi sell program còn chạy | Chưa có Smart Money Low | Chờ sweep SSL + MSS tăng |
| Mua nhầm Inducement | Mua ngay tại đáy trung gian đầu tiên | Nảy yếu, không MSS, giá giảm tiếp | Đối chiếu 4 tiêu chí SML thật ở mục 3 |
| Short đáy | Bán đúng lúc sell program kết thúc | Đi ngược chính kịch bản MMBM | Nhận diện SML để lật sang mua |
| Bỏ qua MSS tăng | Mua chỉ vì "giảm đã nhiều" | Đáy chưa xác nhận | Yêu cầu MSS + displacement |
| Chase buy program | Mua đuổi nhịp đẩy | Bỏ bước LRB, R:R xấu | Chờ pullback về FVG/OB |
| Mua ở premium | Vào khi giá đã gần BSL | Room ít, R:R kém | Chỉ mua ở discount, LRB sớm |
| Bỏ qua nested MMSM | Mua theo MMBM H1 khi D1 vẫn giảm mạnh | Mua ngược trend lớn hơn | Kiểm tra D1/H4 trước khi tin SML |
| Stop tùy tiện | Không đặt dưới SML | Bị quét vô lý | Stop dưới Smart Money Low |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = buy-side liquidity |

---

## 11. Câu hỏi tự kiểm tra

- Mình có phân biệt được sell program (nửa A) và buy program (nửa B) không?
- Smart Money Low đã hình thành chưa (sweep SSL + reclaim), hay đây chỉ là một Inducement?
- Đã có MSS tăng + displacement để lại FVG chưa?
- LRB tiếp theo ở FVG/OB nào, đúng discount không?
- D1/H4 có đang ở giữa một MMSM lớn hơn chưa hoàn tất không (nested check)?
- Buy-side target ở đâu, R:R bao nhiêu?
- Mình đang định mua (đúng kịch bản) hay đang lỡ short đáy?
- Nếu không trade, lý do "No Trade" rơi vào giai đoạn nào?

---

## 12. Flashcards / Active Recall

### Q1
**Hỏi:** MMBM gồm mấy nửa và tâm điểm là gì?
**Đáp:** Hai nửa — Sell Program (tạo đáy) và Buy Program (đẩy lên) — đối xứng quanh một **Smart Money Low** (sweep SSL + reclaim).

### Q2
**Hỏi:** Trong MMBM mình được phép trade phía nào?
**Đáp:** Chỉ phía MUA (Buy Program), sau khi Smart Money Low đã xác nhận bằng sweep SSL + MSS tăng. Không bán trong sell program nếu đang đọc MMBM.

### Q3
**Hỏi:** LRB (Low Risk Buy) là gì?
**Đáp:** Điểm mua rủi ro thấp tại FVG/OB (lý tưởng trùng OTE) trong mỗi đợt re-accumulation của buy program; mỗi LRB ~ một chuỗi ICT 2022 thu nhỏ.

### Q4
**Hỏi:** Điều gì làm kịch bản MMBM bị vô hiệu?
**Đáp:** Khi giá đóng nến **dưới Smart Money Low** (đáy bị phá), hoặc khi chưa hề có sweep SSL + MSS tăng.

### Q5
**Hỏi:** Vì sao bắt đáy giữa sell program là sai?
**Đáp:** Sell program tồn tại để quét nốt SSL và tạo đáy thật; mua trước khi nó kết thúc thường bị quét stop ở bậc giảm tiếp theo — đó là mua nhầm Inducement.

### Q6
**Hỏi:** Inducement khác Smart Money Low thật ở điểm nào?
**Đáp:** Sau khi bị quét, Inducement chỉ nảy yếu, không phá được swing high (không MSS thật) rồi giá tiếp tục giảm; Smart Money Low có reclaim nhanh + MSS tăng + displacement rõ ngay sau đó.

### Q7
**Hỏi:** Vì sao phải kiểm tra D1/H4 trước khi tin một MMBM H1?
**Đáp:** Vì MMXM có tính fractal — một MMBM H1 "sạch" có thể chỉ là một nhịp hồi (nested) bên trong sell program của một MMSM D1 lớn hơn vẫn chưa hoàn tất; mua theo nó là mua ngược trend HTF thật.

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
model: MMBM # MMBM | MMSM | ICT-2022 | OSOK | Venom
bias: bullish
program: buy # sell | buy
smart_money_low: true # đã có SML chưa
mss_up: true # MSS tăng xác nhận
lrb_entry: true # vào tại LRB (FVG/OB)
entry_location: Discount
target: BSL
nested_htf_conflict: false # có đang mua ngược MMSM D1 lớn hơn không
rr_planned: 4.0
missing_step: none # none | sml | mss | lrb | target | nested
```

> [!tip]
> Với các lệnh thua theo MMBM, ghi `missing_step` để biết mình hay vào sai ở đâu — phổ biến nhất là vào khi **chưa có SML** (mua nhầm Inducement) hoặc **chase buy program** (bỏ LRB).

---

## 14. Lesson Learned

### Bài học chính
- MMBM là **kịch bản đảo chiều tăng**: bán xuống lấy đáy → lập Smart Money Low → mua lên về BSL.
- Chỉ tham gia **phía mua**, sau khi đáy đã xác nhận (sweep SSL + MSS tăng, không phải Inducement).
- Vào tại **LRB (retrace về FVG/OB)**, không chase buy program.
- Stop **dưới Smart Money Low**; target là buy-side liquidity.
- Luôn kiểm tra tính **fractal/nested** với D1/H4 trước khi tin một SML LTF là đảo chiều thật.
- Mạnh nhất ở **LRB đầu tiên** sau MSS, trong kill zone, có confluence OB/OTE.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ mua sau khi thấy Smart Money Low + MSS tăng, đã đối chiếu với 4 tiêu chí phân biệt Inducement.
- [ ] Tôi không short đáy khi đang đọc kịch bản MMBM.
- [ ] Tôi vào ở LRB, không đuổi nhịp đẩy.
- [ ] Tôi đặt stop dưới Smart Money Low.
- [ ] Tôi kiểm tra D1/H4 trước khi tin một MMBM LTF là đảo chiều thật.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc nhở khi trade
> **"Đợi đáy được lập, rồi mua từng bậc. Không bắt đáy, không bán đáy, và luôn kiểm tra bức tranh lớn hơn."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt sell/buy program và SML? |
| Nhận diện trên chart |  | Xác định đúng Smart Money Low theo thời gian thực, phân biệt được Inducement? |
| Biết khi nào bỏ qua |  | Dám không bắt đáy khi chưa có SML? |
| Kết hợp với context HTF |  | Ghép bias + discount + BSL target + kill zone + nested check? |
| Áp dụng vào trade thực tế |  | Entry có thật sự ở LRB sau MSS không? |
| Review sau trade |  | Có gắn `missing_step` và review bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup tag `[[Market Maker Buy Model – MMBM]]`.
- [ ] Review theo `missing_step`: hay sai ở SML, Inducement, hay LRB.
- [ ] Thống kê win rate theo `program`, `entry_location`, và `nested_htf_conflict`.
- [ ] Cập nhật rule khi đủ mẫu.

---

## Appendix — MMBM Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Bias:** Bullish / chuyển Bullish
> **Original consolidation BSL (target):** @ ____
> **Location:** Discount?
> **D1/H4 nested check:** đang ở giữa MMSM lớn hơn? Yes/No
> **(1) Sell program — SSL quét:** @ ____ → Smart Money Low? Yes/No (reclaim nhanh?)
> **(2) MSS tăng + displacement:** phá ____ → FVG? Yes/No
> **(3) LRB (FVG/OB):** [low]–[high], CE ____ ; OTE? ____
> **(4) Entry:** ____ ; Stop (dưới SML): ____
> **(5) Target:** internal ____ → BSL ____
> **Đủ kịch bản (SML+MSS+LRB, không phải Inducement)?** Yes / No — thiếu: ____
> **Kill zone:** London / NY AM / NY PM
> **R:R dự kiến:**
> **No-trade condition:**
