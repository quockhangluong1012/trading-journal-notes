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

---

## 2. Bối cảnh sử dụng

### Hai nửa & khái niệm tương ứng

| Giai đoạn | Tên | Khái niệm liên kết | Câu hỏi kiểm tra |
|---|---|---|---|
| Đáy | Original Consolidation | [[19 - Liquidity]], [[12 - Dealing Range]] | SSL phía dưới ở đâu (target cuối)? |
| Nửa A | Buy Program (các LRB) | [[Order Block]], [[Fair Value Gap]] | Giá đang tăng bậc thang quét BSL nào? |
| Đỉnh | Smart Money High | [[20 - Liquidity Sweep]], [[07 - Buy-side Liquidity]] | BSL cuối đã bị quét + reject chưa? |
| Chuyển pha | MSS giảm | [[21 - Market Structure Shift]], [[Displacement]] | Đã phá swing low gần nhất chưa? |
| Nửa B | Sell Program (các LRS) | [[Fair Value Gap]], [[Order Block]], [[Optimal Trade Entry]] | LRS tiếp theo ở FVG/OB nào? |
| Target | Sell-side liquidity | [[30 - Sell-side Liquidity]] | SSL/đáy cũ nào là target? |

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
| MSS giảm nhưng chưa sweep BSL chính | **Nghi ngờ** | Có thể là pullback trong buy program |
| Đủ kịch bản nhưng đã gần SSL | **Hạ cấp** | Room ít, giảm size hoặc bỏ |

> [!note]
> MMSM mạnh nhất khi bạn vào ở **LRS đầu tiên** ngay sau MSS giảm tại Smart Money High — đó là điểm có R:R tốt nhất. Các LRS sau vẫn dùng được nhưng room giảm dần khi tiến về SSL.

---

## 6. Ví dụ chart

### Ví dụ đúng — Buy program → Smart Money High → MSS giảm → bán LRS về SSL
![[paste-image-here.png]]

**Mô tả:**
HTF bias chuyển Bearish, giá ở premium. **(1)** Buy program đẩy giá lên bậc thang, quét một pool **BSL (equal highs)** tạo **Smart Money High** rồi reject. **(2)** Một **MSS giảm + displacement** phá swing low gần nhất, để lại bearish FVG. **(3)** Giá pullback về FVG (LRS#1) → **entry**, stop trên SMH. **(4)** Sell program đẩy giá xuống về **SSL** của original consolidation.

**Vì sao đây là ví dụ tốt:**
- Đỉnh được xác nhận bằng **sweep BSL + reject** trước khi bán.
- Entry ở **LRS (retrace)**, đúng premium, không chase.
- Stop logic trên Smart Money High; target là sell-side liquidity rõ.

### Ví dụ sai / dễ nhầm — Bắt đỉnh giữa buy program, chưa có MSS giảm
![[paste-image-here.png]]

**Mô tả lỗi:**
Trader thấy giá tăng "đã cao" nên **bán bắt đỉnh** giữa buy program, chưa hề có sweep BSL chính và chưa có MSS giảm. Buy program tiếp tục một bậc nữa, quét luôn stop trên điểm bán. Đỉnh thật (Smart Money High) hình thành cao hơn.

**Bài học:**
- Không bắt đỉnh khi buy program chưa kết thúc (chưa sweep BSL + MSS giảm).
- "Tăng cao" không phải tín hiệu bán; **sweep + reject + MSS** mới là tín hiệu.
- Luôn chờ LRS sau khi đỉnh đã xác nhận.

---

## 7. Entry model liên quan

Khái niệm này tổng hợp:
- [[02 - AMD]]
- [[12 - Daily Bias]]
- [[19 - Liquidity]]
- [[07 - Buy-side Liquidity]]
- [[30 - Sell-side Liquidity]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[Displacement]]
- [[Fair Value Gap]]
- [[Order Block]]
- [[Optimal Trade Entry]]
- [[27 - Premium Discount]]
- [[18 - Kill Zones]]
- [[ICT 2022 Model]]
- [[Market Maker Buy Model – MMBM]]

### Sequence mẫu — MMSM (đầy đủ)
```text
(1) Original consolidation + SSL target (đáy)
(2) Buy Program: các LRB đẩy giá lên bậc thang
(3) Sweep BSL chính (+ reject) = Smart Money High
(4) MSS giảm + displacement → bearish FVG
(5) Sell Program: các LRS (retrace về FVG/OB, lý tưởng OTE)
(6) Entry tại LRS; Stop trên Smart Money High
(7) Target: Internal liquidity → SSL (original consolidation)
(+ Kill zone London/NY, + đồng hướng AMD)
```

> [!note]
> MMSM và [[Market Maker Buy Model – MMBM]] là cặp đối xứng. Học một cái là hiểu cái kia (lật ngược). Chúng cùng thuộc họ MMXM và là "khung kịch bản" để gắn các chuỗi [[ICT 2022 Model]] nhỏ vào từng LRS/LRB.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì giá "đã tăng cao"
> Phải đủ kịch bản: Sweep BSL (Smart Money High) → MSS giảm → LRS. Một nhịp tăng chậm lại KHÔNG phải là MMSM.

### A. Context (HTF)
- [ ] Bias đang Bearish / chuyển Bearish.
- [ ] Original consolidation + SSL target đã xác định.
- [ ] Giá ở premium của dealing range.
- [ ] BSL pool (đỉnh/equal highs) đã đánh dấu.

### B. Execution (LTF)
- [ ] Buy program đã quét BSL chính → Smart Money High + reject.
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

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Bắt đỉnh non | Bán khi buy program còn chạy | Chưa có Smart Money High | Chờ sweep BSL + MSS giảm |
| Long đỉnh | Mua đúng lúc buy program kết thúc | Đi ngược chính kịch bản MMSM | Nhận diện SMH để lật sang bán |
| Bỏ qua MSS giảm | Bán chỉ vì "tăng đã nhiều" | Đỉnh chưa xác nhận | Yêu cầu MSS + displacement |
| Chase sell program | Bán đuổi nhịp giảm | Bỏ bước LRS, R:R xấu | Chờ pullback về FVG/OB |
| Bán ở discount | Vào khi giá đã gần SSL | Room ít, R:R kém | Chỉ bán ở premium, LRS sớm |
| Stop tùy tiện | Không đặt trên SMH | Bị quét vô lý | Stop trên Smart Money High |
| Không có target rõ | TP cảm tính | R:R không kế hoạch | Target = sell-side liquidity |

---

## 10. Câu hỏi tự kiểm tra

- Mình có phân biệt được buy program (nửa A) và sell program (nửa B) không?
- Smart Money High đã hình thành chưa (sweep BSL + reject)?
- Đã có MSS giảm + displacement để lại FVG chưa?
- LRS tiếp theo ở FVG/OB nào, đúng premium không?
- Sell-side target ở đâu, R:R bao nhiêu?
- Mình đang định bán (đúng kịch bản) hay đang lỡ long đỉnh?
- Nếu không trade, lý do "No Trade" rơi vào giai đoạn nào?

---

## 11. Flashcards / Active Recall

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
**Đáp:** Buy program tồn tại để quét nốt BSL và tạo đỉnh thật; bán trước khi nó kết thúc thường bị quét stop ở bậc tăng tiếp theo.

### Q6
**Hỏi:** MMSM liên hệ với AMD ra sao?
**Đáp:** Buy program ~ manipulation/accumulation lên; Smart Money High ~ distribution; Sell program ~ markdown.

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
model: MMSM # MMBM | MMSM | ICT-2022 | OSOK | Venom
bias: bearish
program: sell # sell | buy
smart_money_high: true # đã có SMH chưa
mss_down: true # MSS giảm xác nhận
lrs_entry: true # vào tại LRS (FVG/OB)
entry_location: Premium
target: SSL
rr_planned: 4.0
missing_step: none # none | smh | mss | lrs | target
```

> [!tip]
> Với các lệnh thua theo MMSM, ghi `missing_step` để biết mình hay vào sai ở đâu — phổ biến nhất là vào khi **chưa có SMH** (bắt đỉnh) hoặc **chase sell program** (bỏ LRS).

---

## 13. Lesson Learned

### Bài học chính
- MMSM là **kịch bản đảo chiều giảm**: mua lên lấy đỉnh → lập Smart Money High → bán xuống về SSL.
- Chỉ tham gia **phía bán**, sau khi đỉnh đã xác nhận (sweep BSL + MSS giảm).
- Vào tại **LRS (retrace về FVG/OB)**, không chase sell program.
- Stop **trên Smart Money High**; target là sell-side liquidity.
- Mạnh nhất ở **LRS đầu tiên** sau MSS, trong kill zone, có confluence OB/OTE.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ bán sau khi thấy Smart Money High + MSS giảm.
- [ ] Tôi không long đỉnh khi đang đọc kịch bản MMSM.
- [ ] Tôi vào ở LRS, không đuổi nhịp giảm.
- [ ] Tôi đặt stop trên Smart Money High.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc nhở khi trade
> **"Đợi đỉnh được lập, rồi bán từng bậc. Không bắt đỉnh, không mua đỉnh."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt buy/sell program và SMH? |
| Nhận diện trên chart |  | Xác định đúng Smart Money High theo thời gian thực? |
| Biết khi nào bỏ qua |  | Dám không bắt đỉnh khi chưa có SMH? |
| Kết hợp với context HTF |  | Ghép bias + premium + SSL target + kill zone? |
| Áp dụng vào trade thực tế |  | Entry có thật sự ở LRS sau MSS không? |
| Review sau trade |  | Có gắn `missing_step` và review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup tag `[[Market Maker Sell Model – MMSM]]`.
- [ ] Review theo `missing_step`: hay sai ở SMH hay LRS.
- [ ] Thống kê win rate theo `program` và `entry_location`.
- [ ] Cập nhật rule khi đủ mẫu.

---

## Appendix — MMSM Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Bias:** Bearish / chuyển Bearish
> **Original consolidation SSL (target):** @ ____
> **Location:** Premium?
> **(1) Buy program — BSL quét:** @ ____ → Smart Money High? Yes/No (reject?)
> **(2) MSS giảm + displacement:** phá ____ → FVG? Yes/No
> **(3) LRS (FVG/OB):** [low]–[high], CE ____ ; OTE? ____
> **(4) Entry:** ____ ; Stop (trên SMH): ____
> **(5) Target:** internal ____ → SSL ____
> **Đủ kịch bản (SMH+MSS+LRS)?** Yes / No — thiếu: ____
> **Kill zone:** London / NY AM / NY PM
> **R:R dự kiến:**
> **No-trade condition:**
