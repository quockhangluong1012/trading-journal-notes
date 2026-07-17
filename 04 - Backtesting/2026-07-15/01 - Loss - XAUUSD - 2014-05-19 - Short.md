---
type: backtest
backtest_date: 2026-07-15
trade_date: 2014-05-19
symbol: XAUUSD
position: Short
result: Loss
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[04 - Breaker Block|Breaker Block]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1301.167
stop_loss: 1301.789
take_profit: 1298.732
r_planned: 3.9
r_multiple: -1
grade: C+
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2014-05-19 — XAUUSD Short

> [!info] Mục đích backtest
> Thử nghiệm dùng **Bearish Breaker Block** làm POI trong chuỗi ICT 2022 Model (thay cho OB/FVG hay dùng). Cấu trúc: HTF Breaker POI → LTF (M1/M5) Sweep + Displacement + FVG → entry retrace FVG. Đây là lệnh **thua**, và là một trong những mẫu backtest giá trị nhất tới giờ: **đúng hướng, đúng vùng chung, nhưng chọn SAI PD Array** — dữ liệu phản chứng trực tiếp cho việc chọn Breaker (0.618) thay vì Order Block (0.786) khi hai POI xếp chồng trong Premium.

> [!important] Kết quả tóm gọn
> Giá quét qua cạnh trên BB bằng **Bullish Displacement** → dính SL. **Sau đó** giá mới retrace lên **OB phía trên (0.786)**, quét OB rồi đảo chiều giảm đúng hướng và chạm TP. → **BB không phải POI terminal; OB mới là.** SL của tôi nằm ngay trên đường thanh khoản mà giá cần lấy để với tới OB.

---

## 0. Backtest Summary

| Field                | Value                                        |
| -------------------- | -------------------------------------------- |
| Symbol               | XAUUSD                                       |
| Trade Date (dữ liệu) | 2014-05-19 17:55 (UTC+7)                     |
| Position             | Short                                        |
| Result               | Loss (Hit Stop Loss)                         |
| Session              | London                                       |
| Setup                | ICT 2022 Model                               |
| Entry Model          | HTF Breaker POI + LTF Sweep/Displacement/FVG |
| Entry Timeframe      | M1 (refine trong M1 FVG)                     |
| HTF Bias             | Bearish                                      |
| Bias Correct?        | Yes (giá cuối cùng chạm TP)                  |
| POI dùng             | Bearish Breaker Block (0.618)                |
| Entry                | 1301.167 (≈ CE của M1 FVG)                   |
| Stop Loss            | 1301.789 (cạnh trên BB + buffer)             |
| Take Profit          | 1298.732 (internal SSL)                      |
| Risk (points)        | 0.622                                        |
| Reward (points)      | 2.435                                        |
| R Planned            | 3.9                                          |
| R Multiple (kết quả) | -1                                           |
| Grade                | C+                                           |
| Followed Plan?       | Yes                                          |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.
> ⚠️ **Cần xác nhận**: `take_profit = 1298.732` được đọc từ order line màu xanh trên chart H1/D1. Nếu TP thực khác, sửa lại `take_profit` + `r_planned`.

---

## 1. HTF Context & Bias

### D1 — Daily Bias & Context

- **Bias**: Bearish (nghiêng giảm trong nhịp retrace / range lớn)
- **Market Condition**: Corrective / Range sau đỉnh
- **Lý do xác định bias (PD array, draw on liquidity)**:
	- Sau nhịp tăng dài kết thúc bằng **Long Term High tại 1392.098**, giá bị bán mạnh xuống vùng ~1280 → đã có **Bearish MSS + Displacement trên khung lớn**.
	- Nhịp hồi lên ~1330 tạo **lower high**, sau đó tiếp tục bị đẩy xuống → order flow D1 vẫn nghiêng giảm.
	- Hiện tại giá dao động trong nửa dưới của range hậu-đỉnh (~1280–1330), sát vùng 1287–1309.
	- Bên dưới còn một **D1 demand/OB (~1200–1215)** nhưng ở rất xa, không phải target của lệnh intraday này.
- **Draw on Liquidity**:
	- Buy-side (BSL): D1 range high 1392.098; các internal high của range.
	- Sell-side (SSL): các đáy range ~1287.66 và 1280; đây là draw dài hạn phía dưới → **thuận hướng Short intraday**.
![[Pasted image 20260715100017.png]]
### H1 — Cấu trúc & POI

- **Cấu trúc H1**:
	- Xác định dealing range cho setup bằng fib: **Low (0) = 1287.711 → High (1) = 1309.013**.
	- Giá rally lên 1309.013 (lấy BSL / tạo swing high), sau đó **Bearish Displacement + MSS** đẩy xuống → xác nhận bias giảm.
	- Sau MSS, giá xả xuống vùng Discount (~1290/1287), quét SSL, rồi **retrace ngược lên vùng Premium** để tìm short → đúng kịch bản ICT 2022 (short từ Premium sau khi Discount bị quét).
- **Hai PD Array (POI) trong Premium — điểm mấu chốt của bài học**:
	- **Order Block (OB)**: ~**1304.5 – 1306** (quanh/ trên mức **0.786 = 1304.454**). *POI sâu hơn, nằm cao hơn trong Premium.*
	- **Bearish Breaker Block (BB)**: **1300.545 – 1301.645** (quanh **0.618 = 1300.87 → 0.705 = 1302.729**). *POI nông hơn, nằm thấp hơn.* → **Đây là POI tôi chọn để short.**
- **Fib OTE levels**: 0.618 = 1300.87 · 0.705 = 1302.729 · 0.786 = 1304.454.
- **Order plan (đọc trên chart)**: Entry 1301.167 (gray) · SL 1301.789 (red, trên BB) · TP 1298.732 (green, internal SSL dưới đáy M1 ~1299.3).
- **Liquidity cần chờ sweep**: internal BSL của consolidation quanh BB; sau sweep → draw về SSL phía dưới (1299.3 → 1298.7 → xa hơn 1287.66).

![[Pasted image 20260715095910.png]]

### Phân tích context → lệnh

- Bias Bearish (D1 + H1 đồng thuận), giá đã quét SSL vùng Discount và đang retrace lên Premium → **khung cảnh cho một lệnh Short là hợp lệ**.
- Trong Premium có **2 POI xếp chồng**: OB (0.786) ở trên, BB (0.618) ở dưới. Tôi quyết định **thử BB** làm POI (thay vì OB/FVG như thường lệ).
- Kế hoạch: chờ giá về BB (tốt hơn thì tới CE của BB ~1301.095) → xuống M1/M5 tìm Sweep + Displacement + FVG → entry retrace FVG → SL trên cạnh BB + buffer → TP về internal SSL.

---

## M5 / M1 — Xác nhận & điểm vào lệnh

### Phân tích:

- **M5**: giá tiến vào vùng BB/OB, có phản ứng bán nhưng **chất lượng displacement không sạch** — các nến giằng co, bóng nến overlap, không tạo được một FVG M5 rõ ràng và dứt khoát (tương tự cảnh báo ở [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]]). Đây đáng lẽ đã là một tín hiệu *đứng ngoài chờ thêm*.
- **M1**: xuống M1 tìm trigger tinh hơn:
	- **Sweep**: ~16:50 giá đẩy lên **quét minor high 1301.647** (internal BSL) — đánh dấu "sweep" trên chart.
	- **Displacement + FVG**: sau sweep, một nhịp giảm để lại **M1 FVG: 1301.239 – 1301.098** (CE ≈ 1301.169).
	- **Entry**: đặt limit trong FVG, khớp tại **1301.167** (≈ đúng **CE của M1 FVG**) lúc **17:55**.
	- **SL**: **1301.789** = cạnh trên BB (1301.645) + buffer (~0.14).
	- **TP**: **1298.732** (internal SSL, dưới đáy M1 gần nhất ~1299.3).
- **Entry trigger**:
	- Liquidity Sweep: quét minor high 1301.647 trên M1.
	- MSS: M1 phá swing low của nhịp sweep.
	- Displacement → tạo M1 FVG 1301.239–1301.098.
	- Retrace về CE FVG → khớp lệnh.
- **Invalidation (theo kế hoạch)**: giá đóng nến trên cạnh trên BB.
- **Tôi có chờ đủ điều kiện không?** Có (theo đúng plan đã định) — nhưng plan chọn sai POI (xem Replay).

M5:
![[Pasted image 20260715100315.png]]
M1:
![[Pasted image 20260715100207.png]]

Result:
![[Pasted image 20260715095941.png]]
---

## 2. ICT 2022 Model — Entry Sequence

- [x] **1. Liquidity Sweep** — M1 quét minor high 1301.647 (internal BSL)
- [x] **2. Displacement** — nến M1 giảm sau sweep, tạo FVG
- [x] **3. Market Structure Shift (MSS)** — M1 phá swing low ngược hướng sweep
- [x] **4. FVG hợp lệ** — M1 FVG 1301.239 – 1301.098
- [x] **5. Entry** — limit tại CE M1 FVG (1301.167), trong Kill Zone London
- [x] **6. Stop Loss** — trên cạnh trên BB + buffer (1301.789)
- [x] **7. Take Profit** — internal SSL 1298.732

> [!warning] Chuỗi "đủ bước" nhưng vẫn thua
> Đủ 7 bước KHÔNG bảo chứng thắng nếu **bước 0 (chọn POI) sai**. Ở đây bước 1–5 diễn ra ở một POI **không phải terminal** → toàn bộ trigger LTF chỉ là nhiễu trên đường giá đi lấy POI thật (OB).

---

## 3. Setup Quality Checklist

- [x] Bias D1 rõ ràng, không mâu thuẫn H1
- [ ] **POI selection tối ưu** — ❌ chọn BB (nông) trong khi OB (sâu, 0.786) mới là terminal POI
- [~] Giá nằm trong Kill Zone — **cần xác minh** (17:55 UTC+7 có thể đã trôi khỏi London KZ chính; xem Lesson)
- [x] Có Liquidity Sweep trước entry (M1)
- [ ] **Displacement rõ ràng** — ⚠️ M5 không tạo FVG sạch (displacement yếu)
- [x] Có MSS hợp lệ (M1)
- [x] POI nằm trong Premium (đúng phía cho Short)
- [ ] **Entry trong POI hợp lệ, không đua giá** — ⚠️ short khi Bullish Displacement còn đang đẩy mạnh vào vùng
- [ ] **SL ở vùng invalidation hợp lý** — ❌ SL trên BB nhưng **dưới OB** → nằm ngay trong đường thanh khoản mà giá cần lấy
- [x] RR ≥ 1:2 (R planned 3.9 — nhưng xem cảnh báo grade)

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: **Hit Stop Loss** (−1R). Sau khi dính SL, giá **tiếp tục lên OB (0.786), quét OB, rồi mới đảo chiều giảm và chạm TP 1298.732**.

### Tại sao lệnh thua? (root cause thật)

**Root cause đơn nhất: SAI POI SELECTION — chọn Bearish Breaker Block (0.618) làm POI trong khi Order Block (0.786) phía trên mới là POI terminal, khiến SL bị đặt ngay trong đường thanh khoản mà giá phải lấy để với tới OB.**

Kiểm chứng bằng cấu trúc và số học:

- Trong Premium của range 1287.711 → 1309.013 có **2 PD Array xếp chồng**:
	- OB: ~1304.5–1306 (≥ 0.786 = 1304.454) — **sâu hơn**
	- BB: 1300.545–1301.645 (0.618–0.705) — **nông hơn** ← tôi chọn cái này
- Khi hai POI xếp chồng cùng phía, **thanh khoản có xu hướng bị kéo tới POI SÂU hơn trước khi đảo chiều**. BB nông nằm *trên đường đi* tới OB.
- SL của tôi = 1301.789, chỉ nhỉnh trên cạnh BB (1301.645). Nhưng **buy-side liquidity nằm rải rác từ trên BB lên tới OB (1301.6 → 1306)**. Để giá với được OB, nó **bắt buộc phải đi xuyên qua 1301.789** → SL của tôi bị "ăn" như một phần của nhịp gom thanh khoản, **không phải** vì luận điểm Short bị phủ định.
- Bằng chứng phủ định trực tiếp: sau khi quét SL, giá **không** tiếp tục tăng vô định — nó lên đúng OB (0.786), quét, rồi **đảo chiều xuống chạm TP 1298.732**. → **Hướng của tôi ĐÚNG. Chỉ có POI (và do đó SL) là sai.**

### Thị trường có cho tín hiệu cảnh báo trước không? Có — ít nhất 3 cái:

1. **Còn một POI cao hơn chưa được test (OB @ 0.786)**. Khi shorting BB, giá vẫn còn "lý do" để đi lên chạm OB. Short POI nông khi POI sâu chưa được chạm = short quá sớm.
2. **M5 không tạo FVG sạch** — phản ứng bán ở vùng yếu/giằng co. Đáng lẽ là tín hiệu no-trade, không phải tín hiệu tụt xuống M1 để "moi" setup. Liên kết [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]].
3. **Bullish Displacement mạnh đẩy vào vùng** ngay trước/tại entry (chính điều đã lưu ý khi phân tích live: M1 đang bị bid lên mạnh). Order flow ngắn hạn phía mua vẫn khỏe → bán ngược vào nó ở POI nông = rủi ro cao bị quét.

### Setup khớp bao nhiêu % với mô hình chuẩn? ~**70%**

- Khớp tốt (context & sequence): bias Bearish đúng; SSL Discount đã bị quét; retrace về Premium; chuỗi Sweep → MSS + Displacement + FVG có tồn tại trên M1; TP về internal SSL hợp lý; entry đúng CE của FVG (kỷ luật tốt).
- Lệch chuẩn (decision & execution): (a) **chọn POI nông (BB) thay vì POI terminal (OB)** — sai nặng nhất; (b) **SL nằm dưới OB, trong đường thanh khoản** → bị quét bởi chính nhịp đi lấy OB; (c) vào khi Bullish Displacement đối nghịch còn mạnh; (d) M5 displacement yếu (không FVG) mà vẫn vào.

### Nếu được vào lại, tôi sẽ làm gì khác?

1. **Ưu tiên POI SÂU hơn khi có POI xếp chồng**: chờ giá lên **OB (0.786)** rồi tìm phản ứng + LTF trigger tại đó. OB là nơi giá thực sự đảo chiều — đúng như POI tôi *vẫn hay dùng*.
2. **Nếu vẫn muốn short từ BB**, thì SL **bắt buộc phải đặt trên OB + buffer (~1306.x)**, không phải trên BB. Khi đó: reward 2.435 / risk ~5.0 = **~0.5R** → RR quá tệ → **tín hiệu rõ ràng rằng entry BB là sai chỗ, nên BỎ lệnh**. (Bài học lặp lại từ [[04 - Breaker Block]] & note 2014-05-14: *SL đúng invalidation quyết định có vào hay không — không siết SL cho đẹp RR*.)
3. **Coi "M5 không FVG" = no-trade.** Không tụt M1 để tìm tín hiệu khi khung xác nhận trung gian bẩn.
4. **Không short khi Bullish Displacement vào vùng chưa bị hấp thụ** — chờ nến Bearish displacement sạch phá cấu trúc tại/ dưới POI rồi mới tìm entry retrace.
5. **Xác minh Kill Zone**: entry 17:55 UTC+7 — kiểm tra lại có nằm trong London KZ chuẩn không; nếu ngoài KZ thì thêm một điểm trừ timing.

---

## 5. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Bias và phân tích top-down **đúng** (giá chạm TP sau đó), nhưng thua vì **chọn Breaker (0.618) làm POI thay vì Order Block (0.786)** — SL nằm ngay trong đường thanh khoản dẫn tới OB, nên giá quét stop trên đường đi lấy POI thật rồi mới đảo chiều đúng hướng.

> [!warning] Ghi chú của mentor
> Đây là một **"loss đúng hướng"** — loại thua nguy hiểm nhất về mặt tâm lý, vì rất dễ tự nhủ "tôi phân tích đúng mà" và **giữ nguyên lỗi**. Không. Đúng hướng nhưng sai POI + sai SL vẫn là −1R thật. Đừng để R:R 3.9 đánh lừa: nó là *sản phẩm phụ* của một SL đặt ở POI nông, không phải bằng chứng chất lượng. Grade **C+**: bias đúng và execution kỷ luật (vào đúng CE, followed plan) kéo điểm lên, nhưng lỗi POI selection + SL trong vùng sweep chặn trần grade. Một lệnh "đúng hướng nhưng SL bị quét vì chọn POI nông" **không** phải setup có edge — nó là setup cần sửa ở tầng ra quyết định.

### 5.1. Bài học kỹ thuật

**Root cause (chỉ MỘT):**
Khi hai PD Array xếp chồng trong cùng vùng Premium (BB @ 0.618 và OB @ 0.786), tôi chọn **POI nông (BB)**. Thanh khoản bị kéo tới **POI sâu (OB)** trước khi đảo chiều, và SL đặt trên BB (dưới OB) rơi vào đúng đường gom thanh khoản đó → bị quét bởi nhịp *đi lấy POI*, không phải bởi tín hiệu phủ định luận điểm.

**Cơ chế thị trường đã diễn ra (để lặp lại được):**
Giá vào BB, cho một phản ứng LTF nhỏ (đủ để tạo M1 sweep/FVG dụ tôi vào). Nhưng **BB chưa hoàn tất "nhiệm vụ" của cấu trúc** — buy-side liquidity phía trên (gồm SL của tôi) và OB @ 0.786 vẫn chưa bị chạm. Một cây **Bullish Displacement** đẩy giá xuyên BB, quét SL, chạy lên **quét OB**, rồi mới **đảo chiều giảm** về TP. Đây là kịch bản kinh điển: **"stopped out trên đường giá đi lấy POI sâu hơn"** (raid-then-reverse tại POI terminal).

**Triệu chứng dễ nhầm là "đúng" (phải cảnh giác):**
- **Entry đẹp đúng CE của M1 FVG (1301.167)** — kỷ luật entry tốt, nhưng entry chuẩn tại POI *sai chỗ* vẫn thua.
- **R:R 3.9 hấp dẫn** — do SL nông tạo ra; chính SL nông giết lệnh.
- **Chuỗi ICT 2022 đủ 7 bước trên M1** — nhưng chuỗi đúng ở POI sai = trap.
- **"Tôi phân tích đúng hướng"** — đúng, nhưng đó không cứu được −1R; nó chỉ xác nhận lỗi nằm ở POI/SL chứ không phải bias.

**Insight quan trọng nhất từ thí nghiệm này:**
Tôi *vẫn hay dùng OB/FVG* làm POI — và lần này **OB chính là nơi giá đảo chiều thật**. Thí nghiệm "dùng BB" cho một **kết quả phản chứng sạch**: với cấu trúc BB-nông + OB-sâu xếp chồng, **OB là POI terminal, BB chỉ là inducement/nơi bị quét**. BB không vô dụng, nhưng **BB không nên được ưu tiên hơn một OB sâu hơn nằm cùng phía chưa được test**. Đây là 1 mẫu — cần thêm mẫu để kết luận, nhưng nó cảnh báo mạnh về thứ tự ưu tiên POI.

**Cần xác minh thêm (đừng vội chốt):**
- Đo lại **mép chính xác của OB** (1304.5–1306?) và xác nhận nó ôm đúng vùng giá đảo chiều.
- Xác nhận **TP thực = 1298.732** (đọc từ order line).
- **Kill Zone**: 17:55 UTC+7 có trong London KZ chuẩn không?
- BB có được vẽ đúng chuẩn breaker (thân nến của OB tăng thất bại) không, hay chỉ là một vùng giá tùy chọn?

### 5.2. Pattern lặp lại (để ý lần sau)

- **Short POI nông khi còn POI sâu hơn chưa test** → giá dễ chạy tới POI sâu, quét mình trên đường đi. Liên kết [[03 - Mistake - Entry When MSS not in POI Zone]].
- **Siết SL cho đẹp R:R** → đặt SL ở mép POI nông thay vì trên invalidation terminal (trên OB). Pattern nguy hiểm nhất.
- **Tụt khung "moi" setup** khi M5 báo phản ứng yếu/không FVG. Liên kết [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]].
- **Bán ngược Bullish Displacement đang đẩy vào vùng** chưa bị hấp thụ.

### 5.3. Rule cần thêm/cập nhật vào Playbook

1. **Rule POI Priority (mới):** Khi ≥2 PD Array xếp chồng cùng phía trong Premium/Discount, **ưu tiên POI SÂU hơn** (gần external liquidity/OTE 0.79 hơn) làm POI terminal. Chỉ short/long POI nông nếu POI sâu **đã bị test và từ chối trước đó**.
2. **Rule SL theo POI terminal:** SL luôn neo trên/dưới **invalidation của POI SÂU nhất còn hiệu lực + buffer**, không neo vào mép POI nông. Nếu SL đúng làm RR < RR floor → **BỎ lệnh**, không siết SL.
3. **Rule confirmation:** M5 không tạo displacement/FVG sạch → **no-trade**, không tụt M1 tìm tín hiệu.
4. **Rule momentum đối nghịch:** Không vào ngược một Displacement đang đẩy mạnh vào POI chưa bị hấp thụ.
5. **Rule grading:** Lệnh "đúng hướng nhưng SL bị quét do chọn POI nông" chặn trần grade ở **C+/B−**, bất kể R:R lý thuyết.

---

## 6. Final Grade

| Tiêu chí                       | Điểm  |
| ------------------------------ | ----- |
| HTF Bias (D1 + H1)             | 9/10  |
| POI Selection                  | 3/10  |
| Liquidity Sweep (M1)           | 7/10  |
| Displacement/MSS quality (M5/M1) | 4/10  |
| Entry refine (CE M1 FVG)       | 8/10  |
| Risk / SL placement            | 2/10  |
| Followed Plan / Discipline     | 8/10  |

**Overall Grade**: **C+** (đúng hướng + kỷ luật execution, nhưng POI selection & SL placement là lỗi cấu trúc chặn trần grade)

> [!tip] Chống curve-fitting
> Trigger (M1 sweep + displacement + FVG trong killzone) có nhận diện được **trước** outcome không? → Có. Nhưng bài học không nằm ở trigger mà ở **POI selection** — thứ cũng phải được quyết định *trước*. Câu hỏi kiểm tra: *trước khi vào, tôi đã hỏi "còn POI nào sâu hơn chưa được test phía trên không?" chưa?* Nếu chưa → đó chính là lỗ hổng quy trình cần đóng.

---

### Liên kết

- Concept POI: [[04 - Breaker Block]] · [[25 - OB - Order Block]] · [[27 - Premium Discount]] · [[26 - OTE - Optimal Trade Entry]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- Bước mô hình: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- Model: [[01 - ICT 2022 Model]]
- Timing: [[18 - Kill Zones]] · [[40 - Macro Times]]
- Mistake liên quan: [[03 - Mistake - Entry When MSS not in POI Zone]] · [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]] · [[05 - Mistake - Not enough RR]]
- Dashboard: [[_Backtest Dashboard]]
