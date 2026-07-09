---
type: ict-concept
concept: ICT Reversal Patterns
aliases:
  - ICT Reversal Patterns
  - IFVG BPR CISD MSS Sequence
  - Three-Stage Reversal
tags:
  - trading/ict/concept
  - trading/study
  - "#reversal"
  - "#entry-model"
status: seed
category: Reversal
last_reviewed: 2026-07-09
created: 2026-07-09
updated: 2026-07-09
---

# ICT Reversal Patterns

> [!summary] Tóm tắt 1 câu
> **ICT Reversal Patterns là chuỗi BA xác nhận đảo chiều nối tiếp nhau — Stage 1 IFVG/BPR (dấu hiệu yếu đầu tiên) → Stage 2 CISD (xác nhận cấp nến) → Stage 3 MSS (phá cấu trúc) — dùng để bắt điểm đảo chiều SỚM, trước khi retail nhận ra, đặc biệt khi cả chuỗi diễn ra tại một HTF PD array.**

> [!important] Nguyên tắc cốt lõi
> Một cực trị đảo chiều hiếm khi "báo" bằng một tín hiệu duy nhất — nó **rò rỉ dần** qua nhiều tầng bằng chứng. Trong xu hướng khỏe, giá **tôn trọng** FVG và bật ra khỏi chúng; khi giá bắt đầu **phá** FVG (Stage 1), rồi **đổi state of delivery** ở cấp nến (Stage 2 CISD), rồi **phá cấu trúc** swing gần nhất (Stage 3 MSS), mỗi tầng thêm vào một lớp xác nhận và **conviction tăng dần**. Chuỗi này **là entry model có điều kiện**, không phải tín hiệu đơn: Stage 1 chỉ để *quan sát*, Stage 2 cho phép vào *aggressive*, Stage 3 + **retest** là điểm vào *conviction cao nhất*. Hai trên ba tầng thường đã đủ; đủ cả ba theo thứ tự tại một HTF PD array = cú đảo chiều mạnh nhất.

---

## 1. Định nghĩa

**Khái niệm:**
**ICT Reversal Patterns** (còn gọi *Three-Stage Reversal* / chuỗi IFVG-BPR → CISD → MSS) là một **quy trình đọc đảo chiều theo tầng**. Thay vì đợi một tín hiệu "hoàn hảo", ta xếp chồng ba xác nhận độc lập nhưng liên tục: (1) **IFVG/BPR** — dấu hiệu đầu tiên rằng xu hướng đang yếu vì giá bắt đầu phá FVG; (2) **CISD (Change in State of Delivery)** — xác nhận ở cấp nến khi giá phá body của cây đối chiều cuối cùng; (3) **MSS (Market Structure Shift)** — phá swing point đối-xu-hướng gần nhất, tuyên bố cấu trúc đã đổi. Làm chủ ba tầng theo đúng thứ tự cho phép vào lệnh **sớm và có kiểm soát rủi ro**, thay vì đuổi theo sau khi đảo chiều đã lộ rõ.

![[Reversal-Advanced-Sequence.svg|697]]

*Chuỗi ba tầng đọc từ trái sang phải: Stage 1 IFVG/BPR (giá bắt đầu phá FVG = xu hướng yếu) → Stage 2 CISD (phá body cây đối chiều cuối = đổi state) → Stage 3 MSS (phá lower swing high gần nhất). Thanh conviction ở dưới cho thấy độ tin cậy tăng dần: Stage 1 chỉ watch, Stage 2 vào aggressive, Stage 3 + retest = conviction cao nhất.*

**Nó giúp trả lời câu hỏi nào trên chart?**
- Xu hướng hiện tại đã **thật sự yếu** chưa, hay pullback này chỉ là nhịp nghỉ để tiếp diễn?
- Cực trị vừa hình thành có phải là **điểm đảo chiều** đáng để đặt lệnh ngược xu hướng không?
- Tôi nên vào ở **tầng nào** — chờ thêm xác nhận (an toàn hơn) hay vào sớm (R lớn hơn nhưng rủi ro cao hơn)?
- Cú phá cấu trúc vừa rồi là **MSS thật** (đảo chiều) hay chỉ là [[05 - BOS - Break of Structure]] nội bộ theo xu hướng cũ?

### Ba pattern này KHÔNG phải là gì

- **Không phải** ba tín hiệu rời rạc để chọn một — chúng là **một chuỗi có thứ tự**. Giá trị nằm ở việc chúng chồng lên nhau đúng trình tự.
- **Không phải** lý do để vào lệnh chỉ với Stage 1. IFVG đơn lẻ là dấu hiệu **yếu nhất**; trade nó một mình là lỗi phổ biến nhất.
- **Không phải** setup dùng được ở bất kỳ đâu trên chart. Đảo chiều chỉ đáng tin khi diễn ra tại một **HTF PD array** (xem [[27 - Premium Discount]]) — không phải giữa range.
- **Không** thay thế được bước **retest**. MSS xác nhận cấu trúc, nhưng entry vẫn cần chờ giá retrace về POI post-MSS; vào ngay cây MSS thường bị quét stop.
- **Không** đảm bảo đảo chiều — nó chỉ nâng xác suất. Vẫn cần quản trị rủi ro ≤0.5% cho mỗi lệnh.

---

## 2. Cơ chế sâu — vì sao chuỗi 3 tầng hoạt động

Đây là phần "why" quyết định việc bạn dùng chuỗi này như một edge hay chỉ vẽ mũi tên sau sự việc. Hiểu cơ chế mới biết **khi nào tin và khi nào bỏ**.

**(a) Đảo chiều là một QUÁ TRÌNH, không phải một điểm.** Smart money không thể đảo toàn bộ order flow trong một cây nến. Trước tiên họ ngừng đẩy giá theo xu hướng cũ (giá không còn tôn trọng FVG → **Stage 1**), rồi bắt đầu giao hàng theo chiều mới ở cấp nến (**CISD**), rồi mới đủ lực phá cấu trúc để lộ ý đồ (**MSS**). Ba tầng chính là **ba dấu chân theo thời gian** của cùng một quá trình phân phối. Đọc chúng theo thứ tự = đọc đúng tốc độ mà quá trình thật sự diễn ra.

**(b) Xếp chồng xác nhận độc lập làm giảm mạnh tín hiệu giả.** Mỗi tầng đơn lẻ đều có tỉ lệ "false positive" cao: một FVG bị phá có thể chỉ là nhiễu; một CISD có thể bị phủ nhận ngay; một cú phá swing có thể là sweep. Nhưng xác suất **cả ba cùng sai theo đúng thứ tự** thấp hơn nhiều. Đây là logic confluence: mỗi lớp không cộng mà **nhân** độ tin cậy, vì chúng đo những khía cạnh khác nhau của cùng hiện tượng (gap delivery → candle delivery → structure).

**(c) Thứ tự mang thông tin.** IFVG/BPR **trước** CISD **trước** MSS là trình tự tự nhiên của một đảo chiều thật. Nếu bạn thấy "MSS" mà trước đó **không** có dấu hiệu yếu (Stage 1) và **không** có CISD, rất có thể đó là [[05 - BOS - Break of Structure]] theo xu hướng cũ hoặc một cú sweep — không phải đảo chiều. Thứ tự sai = cảnh báo đọc nhầm.

**(d) Bắt SỚM nhưng không bắt DAO RƠI.** Cái hay của chuỗi là nó cho phép vào **trước** khi đảo chiều rõ ràng với đám đông, nhưng vẫn có **cấu trúc rủi ro xác định** (stop ngoài cực trị MSS). Bạn không đoán đáy/đỉnh mù quáng — bạn chờ bằng chứng tích lũy đủ rồi mới hành động, và mỗi tầng cho bạn một điểm vào với R:R khác nhau.

> [!info] Vì sao chồng xác nhận thắng một tín hiệu đơn
> Một tín hiệu đơn (chỉ IFVG, chỉ MSS) ép bạn chọn giữa *vào sớm nhưng nhiều nhiễu* hoặc *vào trễ nhưng chắc*. Chuỗi 3 tầng giải quyết mâu thuẫn đó: nó **phân tầng rủi ro** — bạn tự chọn điểm trên đường cong tin cậy tùy khẩu vị và bối cảnh. Với người ở giai đoạn foundation, mặc định nên đứng ở tầng 2–3 (sau CISD, lý tưởng sau MSS + retest) để ưu tiên tính nhất quán hơn là bắt sát đáy.

---

## 3. Bối cảnh sử dụng

### Khi nào chuỗi có giá trị cao?
- [ ] Giá đang phản ứng tại một **HTF PD array** rõ ràng (Daily/4h FVG, OB, premium/discount — xem [[27 - Premium Discount]])
- [ ] Đảo chiều **tại discount** (cho bullish) hoặc **tại premium** (cho bearish)
- [ ] Có **draw on liquidity** hợp lý ở phía đối diện để làm target (equal highs/lows, ERL — xem [[16 - Internal & External Range Liquidity (IRL & ERL)]])
- [ ] Trong **killzone** hoặc **macro window** (đặc biệt 09:50 NY-AM — xem [[40 - Macro Times]])
- [ ] Chuỗi diễn ra **theo đúng thứ tự** IFVG/BPR → CISD → MSS
- [ ] Có thêm confluence: [[42 - SMT Divergence]] tại cực trị, sweep thanh khoản trước Stage 1

### Khi nào nên bỏ qua?
- [ ] Không có **HTF PD array** — chỉ là đảo chiều giữa range
- [ ] Mới chỉ có **Stage 1 (IFVG đơn lẻ)**, chưa có CISD/MSS
- [ ] "MSS" xuất hiện mà **không** có dấu hiệu yếu và CISD trước đó (nghi ngờ là BOS/sweep)
- [ ] Đảo chiều **ngược HTF bias mạnh** mà không có narrative HTF hỗ trợ
- [ ] Vùng giá **không có target** (không có liquidity đối diện để giá "draw" tới)
- [ ] Ngoài killzone, thanh khoản mỏng, spread rộng (tin đỏ)

---

## 4. Stage 1 — IFVG / BPR

Trong một xu hướng khỏe, giá **tôn trọng** các FVG: chạm vào là bật ra tiếp tục xu hướng. Dấu hiệu YẾU đầu tiên xuất hiện khi giá **bắt đầu phá** FVG — đóng cửa (close) vượt qua nó theo chiều ngược lại. Khi đó FVG cũ trở thành **IFVG (Inversion FVG)** và đảo vai trò support ↔ resistance (xem [[17 - Inverse Fair Value Gap - iFVG]]). Nếu **trong lúc phá**, giá tạo thêm **một FVG ngược chiều** đè lên FVG cũ, phần chồng nhau là **BPR (Balanced Price Range)** — tín hiệu mạnh hơn (xem [[03 - Balanced Price Range]], [[13 - FVG  - Fair Value Gap]]).

![[Reversal-Advanced-IFVG-BPR.svg|697]]

*Trái: IFVG = MỘT FVG bị close phá ngược, đảo vai support↔resistance — xác nhận YẾU. Phải: BPR = HAI FVG ngược chiều chồng nhau, phần overlap (tím) là vùng vào lệnh quanh CE — xác nhận MẠNH hơn. Cả hai vẫn thuộc Stage 1: dấu hiệu yếu đầu tiên, chưa phải trigger.*

**Phân biệt then chốt (đây là lỗi hay gặp):**

- **IFVG = một FVG duy nhất** bị close phá ngược. Chỉ một gap, một lần đảo vai. Tín hiệu yếu, dễ bị phủ nhận.
- **BPR = hai FVG ngược chiều overlap**. Ví dụ bullish BPR: leg giảm để lại một bearish FVG (SIBI), rồi giá đảo và leg tăng để lại một bullish FVG (BISI) đè lên. **Chỉ phần giao nhau** là BPR, không phải toàn bộ hai FVG.
- **BPR mạnh hơn IFVG** vì nó thể hiện lực hai chiều cân bằng rồi nghiêng về chiều mới — bằng chứng đảo chiều dày hơn.

**Cách dùng Stage 1:** Sau khi BPR/IFVG hình thành, **chờ giá retrace về vùng đó** rồi vào **theo chiều BPR/IFVG**. Nhưng ở giai đoạn foundation, coi Stage 1 là **đèn vàng — chuẩn bị, chưa bấm cò**. Đừng trade IFVG đơn lẻ giữa range.

> [!warning] Cạm bẫy Stage 1
> Đa số lệnh thua "đảo chiều" đến từ việc **trade IFVG một mình** khi thấy giá phá một FVG bất kỳ. Một FVG bị phá giữa range chẳng nói lên điều gì. IFVG chỉ có nghĩa khi (a) đang ở HTF PD array và (b) sẽ được CISD + MSS xác nhận tiếp.

---

## 5. Stage 2 — CISD

**CISD (Change in State of Delivery)** là xác nhận cấp nến rằng "chế độ giao hàng" của giá đã đổi chiều. Bullish delivery = chuỗi nến bullish liên tiếp; khi giá **phá xuống dưới ĐIỂM BẮT ĐẦU** của chuỗi bullish đó → CISD sang phía bán. Điểm bắt đầu của bullish delivery = **body low (giá close) của cây bearish CUỐI CÙNG** ngay trước chuỗi nến bullish (xem [[41 - Change in State of Delivery]]).

![[Reversal-Advanced-CISD.svg|697]]

*CISD level được đánh tại BODY LOW (giá đóng cửa) của cây bearish cuối trước chuỗi bullish liên tiếp — KHÔNG phải wick low, KHÔNG phải open của cây bullish đầu tiên. Khi giá đóng cửa phá xuống mức đó = bearish CISD. Đối xứng cho bullish CISD: phá LÊN body high của cây bullish cuối.*

**Quy tắc đánh dấu CISD level (nhấn mạnh — BODY không WICK):**

1. Xác định **chuỗi nến cùng chiều liên tiếp** (bullish delivery cho reversal giảm; bearish delivery cho reversal tăng).
2. Tìm **cây đối chiều CUỐI CÙNG** ngay trước chuỗi đó.
3. CISD level = **giá close** của cây đó = **body low** (với cây bearish) hoặc **body high** (với cây bullish). **Đây là giá đóng cửa, không phải đuôi nến.**
4. Khi giá **đóng cửa** vượt qua mức này theo chiều ngược = CISD được kích hoạt.

> [!warning] CISD là BODY, không phải WICK
> Ba lỗi giết chết CISD: (1) dùng **wick** (đuôi nến) thay vì body — mức sẽ quá xa, dễ bị quét; (2) dùng **open của cây directional đầu tiên** thay vì close của cây đối chiều cuối; (3) đánh CISD giữa range không context. Sai mức = CISD giả, bị sweep rồi stop-out.

**Cách dùng Stage 2:** Sau khi CISD kích hoạt, **chờ giá retrace về Breaker/BPR/FVG/IFVG** hình thành *trong lúc* CISD (xem [[04 - Breaker Block]]), rồi vào **theo chiều CISD**. Đây là điểm vào **aggressive** — sớm hơn MSS, R lớn hơn, nhưng chưa có xác nhận cấu trúc nên rủi ro cao hơn tầng 3.

---

## 6. Stage 3 — MSS

**MSS (Market Structure Shift)** là xác nhận thứ ba / gần cuối: giá **phá swing point đối-xu-hướng GẦN NHẤT**, tuyên bố phe cũ đã mất kiểm soát. Bullish MSS = phá **lower swing high gần nhất** (phe bán hết lực); bearish MSS = phá **higher swing low gần nhất** (phe mua hết lực). Xem [[21 - Market Structure Shift]].

![[Reversal-Advanced-MSS.svg|697]]

*Xu hướng giảm tạo các lower swing high/low. MSS thật = phá đúng lower swing high ĐỐI-XU-HƯỚNG GẦN NHẤT (vòng tròn xanh) bằng một cây displacement đóng cửa trên mức đó — KHÔNG phải phá một pullback nhỏ bất kỳ (đó chỉ là BOS nội bộ), cũng KHÔNG phải một swing high ở xa phía trên.*

**Điểm phân biệt then chốt — "swing gần nhất", không phải swing bất kỳ:**

- MSS thật phải phá **swing point đối-xu-hướng gần nhất** — tức pullback cuối cùng ngược xu hướng ngay trước cực trị.
- Phá một **pullback nhỏ nội bộ** không đủ tư cách MSS; đó là dao động thường hoặc [[05 - BOS - Break of Structure]] tiếp diễn.
- Phá một swing high ở **xa phía trên** (không phải cái gần nhất) = đọc sai — bạn đang đợi quá nhiều và có thể đã bỏ lỡ, hoặc gán nhãn nhầm.
- **MSS ≠ BOS:** BOS phá cấu trúc **theo** xu hướng (tiếp diễn); MSS phá cấu trúc **ngược** xu hướng (đảo chiều). Cùng một cú phá, ý nghĩa ngược nhau tùy nó phá swing nào.

**Cách dùng Stage 3:** Sau MSS, **chờ giá retrace về Breaker/IFVG/BPR/FVG** hình thành trong lúc phá cấu trúc, rồi vào theo hướng mới. Đây là điểm vào **conviction cao nhất** — có đủ ba tầng và một điểm vào với stop rõ ràng (ngoài cực trị MSS).

---

## 7. Bullish vs Bearish

Chuỗi đảo chiều đối xứng hoàn toàn giữa hai chiều, nhưng **bối cảnh Premium/Discount** là bộ lọc bắt buộc: đảo tăng chỉ đáng tin ở **discount**, đảo giảm ở **premium**.

![[Reversal-Advanced-BullBear.svg|697]]

*Trái — Bullish reversal: giá giảm vào DISCOUNT của HTF PD array, tạo đáy chuỗi, rồi IFVG/BPR → CISD → MSS đẩy lên. Phải — Bearish reversal: giá tăng vào PREMIUM, tạo đỉnh chuỗi, rồi chuỗi ba tầng đẩy xuống. Đảo chiều mà KHÔNG đứng ở discount/premium của HTF thường là bẫy.*

**Bullish reversal (bắt ĐÁY):**
- Bối cảnh: giá ở **discount** của HTF PD array; lý tưởng vừa quét sell-side liquidity.
- Chuỗi: bearish FVG bị phá lên (IFVG/BPR) → phá body high cây bullish... *(đối chiều: phá lên body của cây bearish cuối)* → CISD tăng → MSS phá lower swing high gần nhất.
- Entry **long**, stop dưới đáy MSS, TP về ERL/BSL phía trên.

**Bearish reversal (bắt ĐỈNH):**
- Bối cảnh: giá ở **premium**; lý tưởng vừa quét buy-side liquidity.
- Chuỗi: bullish FVG bị phá xuống (IFVG/BPR) → CISD giảm (phá body low cây bullish cuối) → MSS phá higher swing low gần nhất.
- Entry **short**, stop trên đỉnh MSS, TP về ERL/SSL phía dưới.

> [!tip] Lọc theo Premium/Discount trước khi tin chuỗi
> Trước khi đọc IFVG/CISD/MSS, hỏi: *giá đang ở premium hay discount của range HTF?* Bullish reversal ở **premium** hoặc bearish reversal ở **discount** là cờ đỏ — thường là bẫy ngược. Đây là cách nhanh nhất loại 1 lượng lớn setup rác.

---

## 8. Thứ tự & mức độ tin cậy của chuỗi

Ba tầng không ngang nhau — mỗi tầng là một **điểm trên đường cong tin cậy**, và bạn chọn vào ở tầng nào tùy khẩu vị rủi ro và chất lượng bối cảnh.

- **Stage 1 — IFVG/BPR = WATCH (quan sát).** Dấu hiệu yếu nhất. Ở foundation: **không** trade một mình. Chỉ dùng để bật cảnh báo "có thể sắp đảo — chuẩn bị".
- **Stage 2 — CISD = AGGRESSIVE ENTRY.** Đã có xác nhận cấp nến. Vào tại Breaker/POI post-CISD. R lớn (vào sớm) nhưng chưa có xác nhận cấu trúc → size thận trọng.
- **Stage 3 — MSS = HIGHEST CONVICTION.** Cấu trúc đã đổi. Vào trên **retest** post-MSS PD array. Đây là điểm vào chuẩn mực nhất, stop rõ ràng ngoài cực trị MSS.

**Quy tắc "hai trên ba":**
- **Hai trong ba tầng** (thường CISD + MSS, hoặc BPR + CISD) đã **đủ** để giao dịch có edge, đặc biệt khi ở HTF PD array.
- **Đủ cả ba theo thứ tự** = tín hiệu **mạnh nhất**, cho phép size ở mức đầy đủ (vẫn ≤0.5%).
- Thiếu thứ tự (MSS trước, không có Stage 1/2) → nghi ngờ, thường không phải đảo chiều thật.

> [!info] Chọn tầng vào theo giai đoạn phát triển
> Trader càng non kinh nghiệm càng nên đứng ở **tầng cao** (chờ MSS + retest): ít lệnh hơn, chắc hơn, dễ backtest và đo lường. Khi đã có dữ liệu chứng minh mắt đọc IFVG/CISD chuẩn, mới hạ dần xuống tầng 2 để bắt R lớn hơn. Đừng vào Stage 1 chỉ vì sốt ruột.

---

## 9. Quy trình vào lệnh

![[Reversal-Advanced-TradeFlow.svg|697]]

*HTF PD array → giá chạm → Stage 1 IFVG/BPR → Stage 2 CISD → Stage 3 MSS → CHỜ retest post-MSS PD array → entry → stop ngoài cực trị MSS → TP về cực đối diện. Bước retest (⑥) là bắt buộc — bỏ nó (vào ngay cây MSS) là lỗi phổ biến nhất.*

**Bước 1 — Xác định HTF PD array.** Trên Daily/4h: tìm FVG, OB, hoặc vùng premium/discount có ý nghĩa. Đây là "địa điểm" duy nhất đáng đọc đảo chiều.

**Bước 2 — Chờ giá tiếp cận array.** Không đuổi giá. Để giá tới vùng đã đánh dấu; lý tưởng đi kèm một cú sweep thanh khoản ngay trước khi phản ứng.

**Bước 3 — Stage 1: IFVG/BPR ngược xu hướng.** Quan sát giá bắt đầu phá FVG của xu hướng cũ. Ghi nhận IFVG (yếu) hay BPR (mạnh). Chưa vào.

**Bước 4 — Stage 2: CISD.** Chờ giá phá **body** cây đối chiều cuối. Đánh CISD level chuẩn (body, không wick). Có thể vào aggressive tại POI post-CISD nếu bối cảnh A+.

**Bước 5 — Stage 3: MSS.** Chờ giá phá **swing point đối-xu-hướng gần nhất** bằng displacement. Xác nhận đây là MSS (đảo) chứ không phải BOS (tiếp diễn).

**Bước 6 — CHỜ retest post-MSS PD array.** Sau MSS, để giá retrace về Breaker/BPR/IFVG/FVG hình thành khi phá cấu trúc. **Đây là bước không được bỏ.**

**Bước 7 — Entry theo hướng mới.** Vào tại POI retest (Breaker/FVG/CE của BPR). Vào lệnh khi có phản ứng rõ (reject) tại vùng đó.

**Bước 8 — Stop.** Đặt **ngoài cực trị của MSS** (dưới đáy MSS cho long, trên đỉnh MSS cho short) + một buffer nhỏ cho spread/nhiễu.

**Bước 9 — Take Profit.** TP về **cực đối diện của leg trước** đó, cộng thêm relative equal highs/lows và HTF FVG. Đây chính là **draw on liquidity** — nhắm ERL đối diện; quản trị partial tại IRL trung gian (xem [[16 - Internal & External Range Liquidity (IRL & ERL)]]).

---

## 10. Ví dụ chart

### Ví dụ đúng

![[Reversal-Example-Correct.svg|697]]

**Mô tả:** Giá giảm vào **discount HTF PD array**. Stage 1: một FVG của xu hướng giảm bị phá lên (IFVG/BPR ①). Stage 2: giá phá body → **CISD** level ②. Stage 3: giá phá **lower swing high gần nhất** = **MSS** ③. Giá retrace về breaker/FVG post-MSS → **entry long** ④, stop dưới đáy MSS, TP về ERL đối diện phía trên.

**Vì sao đây là ví dụ tốt:**
- Đứng tại **HTF PD array** (discount) — có "địa điểm" hợp lệ, không phải giữa range.
- Đủ **ba tầng theo đúng thứ tự** ①→②→③ — confirmation chồng confirmation.
- CISD đánh đúng **body**, không wick; MSS là **swing đối-xu-hướng gần nhất**, không phải pullback bất kỳ.
- **CHỜ retest** post-MSS mới vào (④) — không đuổi cây phá.
- Stop **ngoài đáy MSS**, TP về **ERL đối diện** → R:R lành mạnh, rủi ro định nghĩa rõ.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một cú đảo chiều thật trên chart của bạn (NQ/EURUSD/XAUUSD): đánh dấu (1) HTF PD array, (2) Stage 1 IFVG/BPR, (3) CISD level (body!), (4) MSS = swing gần nhất, (5) điểm retest + entry, (6) stop ngoài MSS, (7) TP tại ERL đối diện.*

### Ví dụ sai / dễ nhầm

![[Reversal-Example-Wrong.svg|697]]

**Mô tả lỗi:** (A) Trade **IFVG đơn lẻ giữa range**, không có HTF PD array — vào long chỉ vì một FVG bị phá; giá chop và dính stop. (B) Vào **ngay cây MSS** (đuổi) mà không chờ retest — giá retrace sâu về POI, quét stop entry, rồi mới đi thật (sau khi mình đã bị đá ra).

**Bài học:**
- Đảo chiều cần **HTF PD array + chuỗi xác nhận**, không trade Stage 1 một mình.
- **Luôn chờ retest** post-MSS; cây MSS gần như luôn retrace về POI trước khi đi tiếp — vào đuổi là tự dâng stop.
- Không nhầm **IFVG (một FVG)** với **BPR (hai FVG overlap)**; không nhầm **MSS (swing ngược gần nhất)** với phá pullback bất kỳ.

---

## 11. Thực hành tốt nhất (Best Practices)

> [!tip] 8 quy tắc dùng ICT Reversal Patterns
> 1. **Luôn bắt đầu từ HTF PD array** — không có array = không đọc đảo chiều. Đây là bộ lọc số một.
> 2. **Lọc theo Premium/Discount** — bullish reversal ở discount, bearish ở premium. Ngược vùng = bỏ.
> 3. **Đọc theo đúng thứ tự** IFVG/BPR → CISD → MSS. Thứ tự sai = nghi ngờ đọc nhầm (có thể là BOS/sweep).
> 4. **Stage 1 chỉ để watch** — đừng trade IFVG đơn lẻ. Vào từ tầng 2 trở lên.
> 5. **CISD là BODY, không WICK** — đánh mức tại giá close của cây đối chiều cuối.
> 6. **MSS = swing đối-xu-hướng GẦN NHẤT** — không phải pullback nhỏ, không phải swing xa.
> 7. **Luôn chờ RETEST post-MSS** — không đuổi cây phá. Đây là kỷ luật cứu tài khoản.
> 8. **Stop ngoài cực trị MSS; TP về ERL đối diện** — rủi ro và target đều định nghĩa trước khi vào.

- Ghép chuỗi với **[[42 - SMT Divergence]]** tại cực trị: nếu tài sản tương quan cũng lệch pha đúng lúc chuỗi hình thành → confluence hạng nhất.
- Ưu tiên chuỗi diễn ra trong **macro window 09:50 NY-AM** ([[40 - Macro Times]]) — displacement sạch, MSS đáng tin hơn.
- **Cặp/thị trường tốt:** GBPUSD, EURUSD, USDCAD, XAUUSD, XAGUSD, NQ, ES. Context HTF trên Daily/4h; entry trên 5m/15m/1m.
- Mở sẵn **HTF + LTF cạnh nhau**: HTF cho array + bias, LTF cho chuỗi 3 tầng + timing entry.
- **Đánh dấu trước** các HTF PD array và draw-on-liquidity đầu phiên, để khi giá tới chỉ việc theo dõi chuỗi hình thành.
- **Ghi nhật ký theo tầng:** với mỗi lệnh, ghi bạn vào ở tầng nào (2 hay 3), có đủ mấy tầng, có ở HTF PD array không — để về sau đo edge tách theo tầng.

> [!warning] Bối cảnh prop-firm (FTMO & The5ers)
> Chuỗi 3 tầng đặc biệt hợp với prop-firm vì nó **giảm số lệnh bốc đồng** và ép bạn chờ xác nhận — đúng loại kỷ luật bảo vệ daily loss limit. Nhưng phải nhớ luật đo drawdown **khác nhau** và không được nhầm:
> - **FTMO (10K):** daily loss đo theo **balance khởi đầu ngày CỐ ĐỊNH** + có yêu cầu **số ngày giao dịch tối thiểu**. Đừng tính daily loss theo equity trồi sụt trong ngày kiểu The5ers.
> - **The5ers (10K):** tham chiếu **equity đóng cửa NGÀY HÔM TRƯỚC** để tính giới hạn ngày, và có yêu cầu **số ngày có lãi tối thiểu** (mỗi ngày đạt ~0.5% lợi nhuận). Mục tiêu là chuỗi ngày xanh nhỏ đều, không phải một lệnh lớn.
> - **Không bao giờ trộn lẫn hai bộ luật này** — biết chính xác challenge nào bạn đang trade.
> - **Process > outcome; ≤0.5% rủi ro/lệnh.** Một "good loss" (đúng chuỗi, đúng retest, thua vì thị trường) tốt hơn một "bad win" (đuổi cây MSS, thắng nhờ may).
> - **Khang đang ở giai đoạn foundation/backtesting:** hãy **backtest chuỗi này** và đếm cụ thể — *2-of-3 thắng bao nhiêu % so với 3-of-3?* Từ đó quyết định mặc định vào ở tầng nào trước khi bỏ tiền mua challenge.

---

## 12. Checklist trước khi dùng

> [!warning] Chuỗi không phải nút "mua/bán"
> Nó xác nhận đảo chiều đáng tin. Entry vẫn cần HTF PD array + đủ tầng + retest. Thiếu một mắt xích thì đứng ngoài.

- [ ] Có **HTF PD array** rõ ràng (Daily/4h FVG/OB/premium-discount)
- [ ] Giá ở đúng vùng: **discount** cho bullish, **premium** cho bearish
- [ ] Có **draw on liquidity** đối diện làm target (ERL, equal highs/lows)
- [ ] **Stage 1** IFVG/BPR đã hình thành (phân biệt đúng IFVG vs BPR)
- [ ] **Stage 2** CISD kích hoạt, đánh level đúng **body** (không wick)
- [ ] **Stage 3** MSS phá đúng **swing đối-xu-hướng gần nhất** (không nhầm BOS)
- [ ] Chuỗi diễn ra **theo đúng thứ tự**
- [ ] Đã **chờ retest** post-MSS PD array — không đuổi cây phá
- [ ] **Stop** đặt ngoài cực trị MSS + buffer
- [ ] **TP** về ERL đối diện; có kế hoạch partial tại IRL
- [ ] Trong **killzone/macro**; không vào quanh tin đỏ
- [ ] Rủi ro lệnh **≤0.5%**; biết rõ luật prop-firm đang áp dụng

---

## 13. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Trade IFVG đơn lẻ | Vào ngay khi một FVG bị phá, không context | Chỉ dùng Stage 1 để watch; vào từ tầng 2 tại HTF PD array |
| Nhầm IFVG với BPR | Gọi mọi FVG bị phá là "BPR" | IFVG = 1 FVG; BPR = 2 FVG ngược chiều overlap |
| Đánh sai CISD level | Dùng wick, hoặc open cây directional đầu | CISD = giá CLOSE (body) của cây đối chiều cuối |
| Coi mọi swing break là MSS | Phá pullback nhỏ bất kỳ rồi gọi MSS | Phải là swing đối-xu-hướng GẦN NHẤT |
| Nhầm MSS với BOS | Phá cấu trúc theo xu hướng rồi tưởng đảo | MSS = phá ngược xu hướng; BOS = phá theo xu hướng |
| Bỏ qua retest | Vào ngay cây MSS, bị quét stop | Luôn chờ retrace về POI post-MSS mới vào |
| Đảo chiều không có HTF PD array | Trade đảo giữa range | Chỉ đọc đảo chiều tại HTF FVG/OB/premium-discount |
| Sai vùng PD | Bullish reversal ở premium (ngược lại) | Lọc premium/discount trước khi tin chuỗi |
| Thứ tự sai | "MSS" nhưng không có Stage 1/2 trước | Yêu cầu đúng trình tự; thiếu = nghi sweep/BOS |

---

## 14. Câu hỏi tự kiểm tra

- Tôi kể được ba tầng theo đúng thứ tự và giải thích vì sao thứ tự quan trọng không?
- Khác biệt chính xác giữa **IFVG** (một FVG) và **BPR** (hai FVG overlap) là gì?
- CISD level đánh ở đâu — body hay wick? Của cây nào?
- "Swing đối-xu-hướng gần nhất" nghĩa là gì, và vì sao không phải mọi cú phá swing đều là MSS?
- MSS khác BOS ở điểm nào?
- Vì sao bước **retest** post-MSS lại bắt buộc? Điều gì xảy ra nếu tôi vào ngay cây MSS?
- Tôi nên vào ở tầng nào tùy bối cảnh, và vì sao 2-of-3 thường đã đủ?
- Stop và TP của một lệnh đảo chiều được đặt ở đâu và dựa trên logic gì?

---

## 15. Flashcards / Active Recall

### Q1
**Hỏi:** ICT Reversal Patterns gồm ba tầng nào, theo thứ tự?
**Đáp:** Stage 1 **IFVG/BPR** (dấu hiệu yếu) → Stage 2 **CISD** (xác nhận cấp nến) → Stage 3 **MSS** (phá cấu trúc). Conviction tăng dần qua từng tầng.

### Q2
**Hỏi:** Phân biệt IFVG và BPR?
**Đáp:** IFVG = **một** FVG bị close phá ngược (đảo vai support↔resistance). BPR = **hai** FVG ngược chiều **overlap**; phần giao nhau là BPR. BPR mạnh hơn.

### Q3
**Hỏi:** CISD level được đánh chính xác ở đâu?
**Đáp:** Tại **body** (giá close) của cây đối chiều **cuối cùng** trước chuỗi delivery — body low với cây bearish, body high với cây bullish. **Không** phải wick, **không** phải open của cây directional đầu tiên.

### Q4
**Hỏi:** MSS thật khác gì với phá swing thường / BOS?
**Đáp:** MSS = phá **swing đối-xu-hướng GẦN NHẤT** (đảo chiều). Phá pullback nhỏ bất kỳ = dao động thường. Phá cấu trúc **theo** xu hướng = BOS (tiếp diễn), không phải MSS.

### Q5
**Hỏi:** Vì sao chồng ba xác nhận thắng một tín hiệu đơn?
**Đáp:** Mỗi tầng đo một khía cạnh khác nhau (gap → candle → structure) và có tỉ lệ false positive riêng. Xác suất cả ba cùng sai theo đúng thứ tự rất thấp → confluence nhân độ tin cậy, đồng thời phân tầng rủi ro cho entry.

### Q6
**Hỏi:** Sau MSS phải làm gì trước khi vào lệnh?
**Đáp:** **Chờ retest** giá retrace về Breaker/BPR/IFVG/FVG post-MSS, rồi mới vào theo hướng mới. Vào ngay cây MSS thường bị quét stop.

### Q7
**Hỏi:** Quy tắc "hai trên ba" nghĩa là gì?
**Đáp:** Hai trong ba tầng (thường CISD + MSS) đã đủ edge để giao dịch, nhất là tại HTF PD array. Đủ cả ba theo thứ tự = tín hiệu mạnh nhất.

### Q8
**Hỏi:** Stop và TP của lệnh đảo chiều đặt ở đâu?
**Đáp:** Stop **ngoài cực trị MSS** + buffer. TP về **cực đối diện của leg trước** + relative equal highs/lows + HTF FVG = draw on liquidity (ERL đối diện; partial tại IRL).

---

## 16. Lesson Learned

> [!summary] Ghi lại khi backtest / trade thật
> - Điền sau khi có dữ liệu thực: tỉ lệ thắng **2-of-3 vs 3-of-3** của riêng mình.
> - Tầng nào mình đọc chuẩn nhất, tầng nào hay sai (đặc biệt CISD body/wick và MSS swing gần nhất)?
> - Bao nhiêu lệnh thua đến từ việc **bỏ retest** hoặc **thiếu HTF PD array**?
> - Kết luận: mặc định nên vào ở tầng nào trong giai đoạn foundation?

---

> [!cite] Nguồn
> [Powerful ICT Reversal Patterns — IFVG/BPR + CISD + MSS](https://innercircletrader.net/tutorials/powerful-ict-reversal-patterns/)
