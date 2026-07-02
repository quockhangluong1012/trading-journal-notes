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
last_reviewed: 2026-06-24
created: 2026-06-24
updated: 2026-06-24
related_concepts:
  - "[[02 - AMD]]"
  - "[[12 - Daily Bias]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[Order Block]]"
  - "[[27 - Premium Discount]]"
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

---

## 2. Bối cảnh sử dụng

### Hai nửa & khái niệm tương ứng

| Giai đoạn | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| Đỉnh | Original Consolidation | [[19 - Liquidity]], [[12 - Dealing Range]] | BSL phía trên ở đâu (target cuối)? |
| Nửa A | Sell Program (các LRS) | [[Order Block]], [[Fair Value Gap]] | Giá đang giảm bậc thang quét SSL nào? |
| Đáy | Smart Money Low | [[20 - Liquidity Sweep]], [[30 - Sell-side Liquidity]] | SSL cuối đã bị quét + reclaim chưa? |
| Chuyển pha | MSS tăng | [[21 - Market Structure Shift]], [[Displacement]] | Đã phá swing high gần nhất chưa? |
| Nửa B | Buy Program (các LRB) | [[Fair Value Gap]], [[Order Block]], [[Optimal Trade Entry]] | LRB tiếp theo ở FVG/OB nào? |
| Target | Buy-side liquidity | [[07 - Buy-side Liquidity]] | BSL/đỉnh cũ nào là target? |

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
| MSS tăng nhưng chưa sweep SSL chính | **Nghi ngờ** | Có thể là bounce trong sell program |
| Đủ kịch bản nhưng đã gần BSL | **Hạ cấp** | Room ít, giảm size hoặc bỏ |

> [!note]
> MMBM mạnh nhất khi bạn vào ở **LRB đầu tiên** ngay sau MSS tăng tại Smart Money Low — đó là điểm có R:R tốt nhất. Các LRB sau vẫn dùng được nhưng room giảm dần khi tiến về BSL.

---

## 6. Ví dụ chart

### Ví dụ đúng — Sell program → Smart Money Low → MSS tăng → mua LRB về BSL
![[paste-image-here.png]]

**Mô tả:**
HTF bias chuyển Bullish, giá ở discount. **(1)** Sell program đẩy giá xuống bậc thang, quét một pool **SSL (equal lows)** tạo **Smart Money Low** rồi reclaim. **(2)** Một **MSS tăng + displacement** phá swing high gần nhất, để lại bullish FVG. **(3)** Giá pullback về FVG (LRB#1) → **entry**, stop dưới SML. **(4)** Buy program đẩy giá lên về **BSL** của original consolidation.

**Vì sao đây là ví dụ tốt:**
- Đáy được xác nhận bằng **sweep SSL + reclaim** trước khi mua.
- Entry ở **LRB (retrace)**, đúng discount, không chase.
- Stop logic dưới Smart Money Low; target là buy-side liquidity rõ.

### Ví dụ sai / dễ nhầm — Bắt đáy giữa sell program, chưa có MSS tăng
![[paste-image-here.png]]

**Mô tả lỗi:**
Trader thấy giá giảm "đã sâu" nên **mua bắt đáy** giữa sell program, chưa hề có sweep SSL chính và chưa có MSS tăng. Sell program tiếp tục một bậc nữa, quét luôn stop dưới điểm mua. Đáy thật (Smart Money Low) hình thành thấp hơn.

**Bài học:**
- Không bắt đáy khi sell program chưa kết thúc (chưa sweep SSL + MSS tăng).
- "Giảm sâu" không phải tín hiệu mua; **sweep + reclaim + MSS** mới là tín hiệu.
- Luôn chờ LRB sau khi đáy đã xác nhận.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[02 - AMD]]
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[30 - Sell-side Liquidity]]
- [[07 - Buy-side Liquidity]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[Displacement]]
- [[Fair Value Gap]]
- [[Order Block]]
- [[Optimal Trade Entry]]
- [[27 - Premium Discount]]
- [[18 - Kill Zones]]
- [[ICT 2022 Model]]
- [[Market Maker Sell Model – MMSM]]

### Sequence mẫu — MMBM (đầy đủ)
```text
(1) Original consolidation + BSL target (đỉnh)
(2) Sell Program: các LRS đẩy giá xuống bậc thang
(3) Sweep SSL chính (+ reclaim) = Smart Money Low
(4) MSS tăng + displacement → bullish FVG
(5) Buy Program: các LRB (retrace về FVG/OB, lý tưởng OTE)
(6) Entry tại LRB; Stop dưới Smart Money Low
(7) Target: Internal liquidity → BSL (original consolidation)
(+ Kill zone London/NY, + đồng hướng AMD)
```

> [!note]
> MMBM và [[Market Maker Sell Model – MMSM]] là cặp đối xứng. Học một cái là hiểu cái kia (lật ngược). Chúng cùng thuộc họ MMXM và là "khung kịch bản" để gắn các chuỗi [[ICT 2022 Model]] nhỏ vào từng LRB/LRS.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì giá "đã giảm sâu"
> Phải đủ kịch bản: Sweep SSL (Smart Money Low) → MSS tăng → LRB. Một nhịp giảm chậm lại KHÔNG phải là MMBM.

### A. Context (HTF)
- [ ] Bias đang Bullish / chuyển Bullish.
- [ ] Original consolidation + BSL target đã xác định.
- [ ] Giá ở discount của dealing range.
- [ ] SSL pool (đáy/equal lows) đã đánh dấu.

### B. Execution (LTF)
- [ ] Sell program đã quét SSL chính → Smart Money Low + reclaim.
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

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bắt đáy non | Mua khi sell program còn chạy | Chưa có Smart Money Low | Chờ sweep SSL + MSS tăng |
| Short đáy | Bán đúng lúc sell program kết thúc | Đi ngược chính kịch bản MMBM | Nhận diện SML để lật sang mua |
| Bỏ qua MSS tăng | Mua chỉ vì "giảm đã nhiều" | Đáy chưa xác nhận | Yêu cầu MSS + displacement |
| Chase buy program | Mua đuổi nhịp đẩy | Bỏ bước LRB, R:R xấu | Chờ pullback về FVG/OB |
| Mua ở premium | Vào khi giá đã gần BSL | Room ít, R:R kém | Chỉ mua ở discount, LRB sớm |
| Stop tùy tiện | Không đặt dưới SML | Bị quét vô lý | Stop dưới Smart Money Low |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = buy-side liquidity |

---

## 10. Câu hỏi tự kiểm tra

- Mình có phân biệt được sell program (nửa A) và buy program (nửa B) không?
- Smart Money Low đã hình thành chưa (sweep SSL + reclaim)?
- Đã có MSS tăng + displacement để lại FVG chưa?
- LRB tiếp theo ở FVG/OB nào, đúng discount không?
- Buy-side target ở đâu, R:R bao nhiêu?
- Mình đang định mua (đúng kịch bản) hay đang lỡ short đáy?
- Nếu không trade, lý do "No Trade" rơi vào giai đoạn nào?

---

## 11. Flashcards / Active Recall

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
**Đáp:** Sell program tồn tại để quét nốt SSL và tạo đáy thật; mua trước khi nó kết thúc thường bị quét stop ở bậc giảm tiếp theo.

### Q6
**Hỏi:** MMBM liên hệ với AMD ra sao?
**Đáp:** Sell program ~ manipulation/distribution xuống; Smart Money Low ~ accumulation; Buy program ~ distribution lên.

---

## 12. Liên kết với Trade Journal

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
rr_planned: 4.0
missing_step: none # none | sml | mss | lrb | target
```

> [!tip]
> Với các lệnh thua theo MMBM, ghi `missing_step` để biết mình hay vào sai ở đâu — phổ biến nhất là vào khi **chưa có SML** (bắt đáy) hoặc **chase buy program** (bỏ LRB).

---

## 13. Lesson Learned

### Bài học chính
- MMBM là **kịch bản đảo chiều tăng**: bán xuống lấy đáy → lập Smart Money Low → mua lên về BSL.
- Chỉ tham gia **phía mua**, sau khi đáy đã xác nhận (sweep SSL + MSS tăng).
- Vào tại **LRB (retrace về FVG/OB)**, không chase buy program.
- Stop **dưới Smart Money Low**; target là buy-side liquidity.
- Mạnh nhất ở **LRB đầu tiên** sau MSS, trong kill zone, có confluence OB/OTE.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ mua sau khi thấy Smart Money Low + MSS tăng.
- [ ] Tôi không short đáy khi đang đọc kịch bản MMBM.
- [ ] Tôi vào ở LRB, không đuổi nhịp đẩy.
- [ ] Tôi đặt stop dưới Smart Money Low.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc nhở khi trade
> **"Đợi đáy được lập, rồi mua từng bậc. Không bắt đáy, không bán đáy."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt sell/buy program và SML? |
| Nhận diện trên chart |  | Xác định đúng Smart Money Low theo thời gian thực? |
| Biết khi nào bỏ qua |  | Dám không bắt đáy khi chưa có SML? |
| Kết hợp với context HTF |  | Ghép bias + discount + BSL target + kill zone? |
| Áp dụng vào trade thực tế |  | Entry có thật sự ở LRB sau MSS không? |
| Review sau trade |  | Có gắn `missing_step` và review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup tag `[[Market Maker Buy Model – MMBM]]`.
- [ ] Review theo `missing_step`: hay sai ở SML hay LRB.
- [ ] Thống kê win rate theo `program` và `entry_location`.
- [ ] Cập nhật rule khi đủ mẫu.

---

## Appendix — MMBM Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Bias:** Bullish / chuyển Bullish
> **Original consolidation BSL (target):** @ ____
> **Location:** Discount?
> **(1) Sell program — SSL quét:** @ ____ → Smart Money Low? Yes/No (reclaim?)
> **(2) MSS tăng + displacement:** phá ____ → FVG? Yes/No
> **(3) LRB (FVG/OB):** [low]–[high], CE ____ ; OTE? ____
> **(4) Entry:** ____ ; Stop (dưới SML): ____
> **(5) Target:** internal ____ → BSL ____
> **Đủ kịch bản (SML+MSS+LRB)?** Yes / No — thiếu: ____
> **Kill zone:** London / NY AM / NY PM
> **R:R dự kiến:**
> **No-trade condition:**
