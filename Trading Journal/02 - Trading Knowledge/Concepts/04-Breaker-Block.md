---
type: ict-concept
concept: Breaker Block
aliases:
  - BB
  - Breaker Block
  - Breaker
  - Bullish Breaker
  - Bearish Breaker
  - Failed Order Block
tags:
  - trading/ict/concept
  - trading/study
  - trading/deep-dive
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
  - "[[07 - Unicorn Model|Unicorn]]"
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence:
version: v3
last_reviewed: 2026-11-10
created: 2026-06-22
updated: 2026-11-10
prerequisites:
  - "[[25-OB-Order-Block]]"
  - "[[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[05-BOS-Break-of-Structure]]"
  - "[[50-Displacement-In-Depth]]"
  - "[[19-Liquidity]]"
  - "[[20-Liquidity-Sweep]]"
  - "[[12-Dealing-Range]]"
common_mistakes:
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[08-Mistake-Weak-Displacement]]"
  - "[[09-Mistake-Wrong-daily-bias]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
  - "[[12-Mistake-Log-Data-Mismatch-Backtest]]"
---

# Breaker Block (BB) — Deep Dive · v3

> [!summary] Tóm tắt 1 câu
> **Breaker Block là cái tên ICT đặt cho một cây nến nằm ở “đỉnh giữa” (hoặc “đáy giữa”), SAU KHI hai việc đã xảy ra đúng thứ tự: giá vượt qua cực trị cũ ở phía bên kia, rồi quay lại phá luôn cái swing chứa cây nến đó. Từ lúc ấy, vùng từng CHẶN giá được theo dõi như vùng có thể ĐỠ giá (và ngược lại). Nó là một cái nhãn dán lên lịch sử giá, kèm một kỳ vọng về tương lai — không phải tín hiệu vào lệnh.**

> [!important] Năm nguyên tắc cốt lõi của bản v3
> 1. **Breaker là một CHUỖI, không phải một hình chữ nhật.** Ba mắt xích, đúng thứ tự: có một cây nến tại đỉnh/đáy giữa → cực trị cũ bị vi phạm → swing giữa bị phá. Thiếu một mắt xích thì gọi bằng tên khác.
> 2. **“Failed Order Block” là cái tên RỘNG, “Breaker” là cái tên HẸP.** Mọi Breaker đều là một OB đã thất bại; không phải OB thất bại nào cũng là Breaker (§10).
> 3. **Việc cực trị cũ bị vi phạm nằm TRONG lời định nghĩa của ICT. Displacement và FVG thì không.** Đừng biến thứ hay đi cùng thành thứ bắt buộc (§15).
> 4. **Bốn mốc phải tách rời:** hình thành (ứng viên) → xác nhận → retest → vào lệnh. Mỗi mốc cho phép một việc khác nhau (§18).
> 5. **Breaker là VỊ TRÍ, không phải BẰNG CHỨNG.** Lợi thế giao dịch của nó là **[BACKTEST REQUIRED]** — phải đếm trên dữ liệu của chính bạn, kể cả mẫu thủng và mẫu không bao giờ được chạm lại.

> [!abstract] Cách đọc note này — 6 nhãn dùng xuyên suốt
> | Nhãn trong note | Tương ứng protocol | Nghĩa |
> |---|---|---|
> | **[QUAN SÁT]** | Observable fact | Thấy trực tiếp trên nến (OHLC). Ai nhìn cũng thấy giống nhau |
> | **[ICT]** | ICT framework | Cách ICT đặt tên và dùng hiện tượng đó. Đúng về *tên gọi*, không nói gì về *hiệu quả* |
> | **[CƠ CHẾ]** | Market mechanics | Giải thích bằng cách lệnh được đặt và khớp; có nghiên cứu độc lập ủng hộ |
> | **[DIỄN GIẢI]** | Interpretation | Hợp lý, nhưng không thể xác nhận chỉ từ chart nến |
> | **[GIẢ THUYẾT]** | Hypothesis | Có thể kiểm chứng, nhưng chưa được kiểm chứng |
> | **[BACKTEST REQUIRED]** | Backtest required | Chưa được phép coi là lợi thế giao dịch |
>
> Mỗi khái niệm khó đi theo 5 tầng: **(1) Trực giác đời thường → (2) Chuỗi giá đơn giản → (3) Thuật ngữ ICT chính xác → (4) Cơ chế thị trường → (5) Ý nghĩa nâng cao.**
> Mọi hình `BB-v3-*` là **sơ đồ dựng (synthetic)**: nến trong hình là ví dụ, không phải dữ liệu thị trường. Note này **không dùng công thức, không dùng thống kê**; chỗ nào cần so sánh thì chỉ so “cao hơn / thấp hơn / trong / ngoài”.
> Trong hình: **vùng cam** = OB gốc · **vùng xanh dương** = Breaker · **đường tím** = cực trị cũ (nơi có liquidity) · **đường xám** = swing giữa.

![[BB-v3-03-Sau-Loai-Cau-Noi.svg|960]]
*Hình 03 — Cùng một Breaker, sáu loại câu nói. Lỗi phổ biến nhất khi học ICT là đọc một câu DIỄN GIẢI như thể nó là QUAN SÁT.*

### Bản đồ trả lời: WHAT → WHY → HOW → WHEN → WHEN NOT

| Câu hỏi | Trả lời ở đâu |
|---|---|
| **WHAT** — Breaker là gì? | §2, §3, §5 |
| **WHY** — vì sao nó hình thành, vì sao vùng đổi vai? | §6, §7, §11, §12 |
| **HOW** — nhận ra thế nào, vẽ ở đâu? | §5.5, §8, §9, §25 |
| **Khác gì** Failed OB, Mitigation Block, S/R, Supply/Demand? | §10, §13 |
| **Quan hệ** với liquidity, MSS/BOS, displacement, FVG, premium/discount? | §14 → §17 |
| **WHEN** — khi nào có ý nghĩa trong ICT 2022 Model? | §20, §22 |
| **WHEN NOT** — khi nào bỏ qua? | §19, §20.3, §21, §26.8 |
| **Không dùng hindsight** thì làm sao? | §18, §24 |
| **Ta thật sự biết gì?** | §27, §28 |

> [!info] v2 → v3: thay đổi gì (OLD → NEW → REASON → cần backtest?)
> | OLD (v2, 2026-10-17) | NEW (v3) | Lý do | Backtest? |
> |---|---|---|---|
> | 71 mục kỹ thuật, nhiều mã định nghĩa và công thức | 30 phần theo protocol mới, giải thích “trẻ 5 tuổi hiểu được” trước rồi mới tới thuật ngữ | Yêu cầu của protocol: hiểu cơ chế trước, hạn chế số học | — |
> | Định nghĩa ICT lấy qua nguồn thứ cấp | Đối chiếu **phụ đề tự động của chính bài giảng ICT “Core Content – Month 04 – Breaker Block”**[^ict-bb] | Ưu tiên nguồn gốc. Lưu ý: vẫn là phụ đề tự động, chưa nghe đối chiếu âm thanh | — |
> | “ICT coi Breaker mạnh hơn Mitigation Block” | Hạ xuống **[GIẢ THUYẾT] của cộng đồng** | Không tìm thấy câu so sánh này trong bài giảng Breaker đã đối chiếu | Có |
> | “Breaker = Order Block thất bại” (nêu như lời ICT) | Ghi rõ: bài giảng Breaker của ICT **không dùng chữ “order block”**; “failed OB” là cách gọi tắt của cộng đồng — đúng về vị trí cây nến, nhưng rộng hơn định nghĩa (§5.4, §10) | Tránh gán cho ICT điều ông không nói | — |
> | “Thân nến đóng qua swing” (nêu như định nghĩa) | Ghi rõ là **quy ước làm việc của note**. ICT nói “violated / break through”, không nói thân hay râu | Phân biệt lời ICT với quy tắc do mình thêm | Có (so râu vs thân) |
> | Mô phỏng random walk, registers DEF/RULE/HYP, thiết kế backtest 17 yếu tố, journal extension | **Đưa ra khỏi thân note** — vẫn còn nguyên trong bản backup v2. Bản v3 chỉ giữ một câu kết luận của mô phỏng (§12.4) và danh sách câu hỏi backtest đơn giản (§27) | Protocol mới: không thống kê, không mô hình phức tạp | — |
> | 32 hình `BB-Deep-*`, `BB-Sim-*` | 58 hình mới `BB-v3-01…58`. Hình cũ vẫn nằm trong `attachments`, không còn được nhúng | Hình mới vẽ theo kiểu “từng khung hình”, có bản bullish và bearish đối xứng | — |
> | Quy ước nến: **nến tăng ở đỉnh giữa** (VAR-A) cho Bullish Breaker | **Giữ nguyên** — nay có căn cứ từ bài giảng gốc | — | — |
>
> Bản v2 đầy đủ: `Claude outputs/backups/04-Breaker-Block.2026-11-10.md.bak`.

---

## 1. Executive Summary

- **Breaker là gì.** [ICT] Bullish Breaker là cây nến tăng (up-close) nằm ở swing high gần nhất, có trước khi một đáy cũ bị vi phạm; khi giá sau đó phá lên trên swing high ấy rồi quay lại, ICT coi đó là một setup mua đáng cân nhắc. Bearish Breaker là ảnh gương: nến giảm ở swing low gần nhất, có trước khi một đỉnh cũ bị vi phạm[^ict-bb] (Hình 11, 12).
- **Nói kiểu trẻ con.** Quả bóng nảy lên đụng trần, rơi thủng sàn xuống hầm, rồi bật lên đục thủng luôn cái trần ấy. Tấm trần cũ giờ nằm dưới chân bóng: nó thành sàn. Sàn này có thể đỡ bóng, cũng có thể thủng tiếp (Hình 01).
- **Vì sao nó hình thành.** [QUAN SÁT] Vì giá đã đi một vòng: bị chặn ở một chỗ → đi xa về phía ngược lại, xa tới mức vượt cả cực trị cũ → rồi quay lại vượt qua đúng cái chỗ từng chặn nó. Cái chỗ ấy vừa chứng kiến một phe thắng lớn rồi thua ngay tại sân nhà (Hình 15, 17).
- **Điều gì thật sự thay đổi.** [QUAN SÁT] Cấu trúc của khung đó: cái đỉnh sinh ra đáy thấp hơn (đỉnh được bảo vệ của nhịp giảm) đã bị vượt. Chuỗi “đỉnh thấp hơn, đáy thấp hơn” không còn. Đây là một Market Structure Shift trên khung ấy (§6).
- **Vì sao vùng có thể đổi vai.** [DIỄN GIẢI] Ba nhóm người có thể cùng muốn mua khi giá quay về: người bán bị kẹt muốn thoát gần hoà vốn, người lỡ cú phá, người mua từ đáy muốn mua thêm. [CƠ CHẾ] Lệnh dừng lỗ quanh mức dễ thấy làm cú phá đi nhanh. Không điều nào nhìn thấy được trên chart nến (§11, §12).
- **Failed OB ≠ Breaker.** Một OB bị nến đóng xuyên qua có bốn khả năng tên gọi: Breaker, Mitigation Block, OB vô hiệu không tên, hoặc chưa thất bại (chỉ râu xuyên). Điểm tách Breaker với Mitigation Block: cực trị cũ có bị vi phạm hay không (Hình 24, 28).
- **Thứ không nằm trong định nghĩa.** Displacement, FVG, mức 50% của vùng, nơi đặt stop, điều kiện vô hiệu, yêu cầu khung lớn: bài giảng Breaker của ICT không nêu. Chúng là phần cộng đồng và phần khung làm việc của bạn thêm vào (Hình 33, 57).
- **Dùng thế nào trong D1 → H1 → M5.** D1 cho hướng và vùng chờ. H1 tìm Breaker *bên trong* vùng D1 và *cùng hướng* D1. M5 chỉ tìm bằng chứng tại Breaker H1: sweep → MSS → displacement → FVG → entry. Không có chuỗi M5 thì không có lệnh (Hình 43, 44).
- **Khi nào bỏ qua.** Breaker ngược khung lớn; swing bị phá chỉ là gợn nhỏ; nằm giữa vùng đi ngang; đã bị chạm nhiều lần; mục tiêu đã đạt trước khi giá quay lại; không còn chỗ chạy so với mức dừng (§20, §21).
- **Giới hạn lớn nhất.** Hindsight. Breaker luôn trông rõ nhất khi nhìn lại những lần nó đã chạy. Tại thời điểm thật, bạn chỉ biết bốn ô đầu của sơ đồ; hai ô cuối là dấu hỏi (Hình 48, 58).

---

## 2. Breaker Block — Explain Like I’m Five

### 2.1 Câu chuyện: ngôi nhà ba tầng và quả bóng

Có một ngôi nhà ba tầng: **hầm**, **tầng 1**, **tầng 2**. Trong nhà có một quả bóng nảy. Quả bóng là **giá**. Càng lên cao là càng “đắt”.

1. Bóng đang ở tầng 1, nảy lên và **đụng trần**. Cộp! Nó không qua được, rơi xuống. Cái trần là chỗ bóng bị chặn.
2. Bóng rơi mạnh tới mức **thủng cả sàn**, lọt xuống hầm. Ai đứng xem cũng nghĩ: “bóng này sẽ còn rơi nữa”.
3. Nhưng bóng bật ngược lên rất mạnh, bay qua tầng 1 và **đục thủng luôn cái trần** đã từng chặn nó. Giờ bóng ở tầng 2.
4. Bóng lại rơi xuống. Lần này, tấm trần cũ nằm **dưới chân** bóng. Nhìn từ tầng 2, nó không còn là trần nữa — nó là **sàn**. Bóng có thể nảy lên trên tấm sàn ấy… hoặc lọt qua cái lỗ thủng. Không ai biết trước.

Tấm ván ở bước 4 — cái trần đã bị đục thủng, nay đóng vai sàn — chính là **Breaker**.

![[BB-v3-01-ELI5-Ngoi-Nha-Ba-Tang.svg|960]]
*Hình 01 — Bốn khung hình của câu chuyện. Tấm ván không đổi chỗ; chỉ có quả bóng đổi phía, nên vai của tấm ván đổi theo.*

### 2.2 Ghép câu chuyện với chart

![[BB-v3-02-Cau-Chuyen-Tren-Chart.svg|960]]
*Hình 02 — Câu chuyện ngôi nhà vẽ bằng nến, đánh số theo đúng thứ tự thời gian.*

| Trong câu chuyện | Trên chart | Tên ICT |
|---|---|---|
| Sàn cũ | Một cái đáy đã có từ trước | Old low (đáy cũ) — bên dưới có sell-side liquidity |
| Cái trần | Nến tăng cuối cùng ở đỉnh, ngay trước khi giá rơi | Up-close candle ở swing high = bearish Order Block |
| Bóng thủng sàn | Giá đi xuống dưới đáy cũ | Old low “violated”, run on stops |
| Bóng xuyên trần | Giá quay lên, nến đóng cửa trên đỉnh | Swing high bị phá = Market Structure Shift |
| Trần thành sàn | Vùng nến ở đỉnh được đổi tên | **Bullish Breaker Block** |
| Bóng rơi lại tấm sàn | Giá hồi về vùng đó | Retest |

Bearish Breaker là câu chuyện lộn ngược: bóng đụng **sàn**, nảy lên thủng **trần cũ**, rồi rơi xuống đục thủng luôn cái sàn; tấm sàn cũ giờ nằm **trên đầu** bóng và đóng vai trần.

### 2.3 Năm câu hỏi của một đứa trẻ

**“Một vùng giá thất bại nghĩa là gì?”**
Cái trần có một việc: không cho bóng lên. Khi bóng đã đứng ở tầng trên, cái trần đã không làm được việc của nó. Thế là “thất bại”. Trên chart: vùng có việc là chặn giá; giá đã đóng cửa ở phía bên kia và ở lại đó.

**“Thế nào là phá vỡ?”**
Có ba mức, đừng lẫn (Hình 16):
- *Đụng trần rồi rơi xuống* — chỉ là chạm.
- *Thò đầu qua lỗ rồi tụt xuống* — chỉ là cái râu nến.
- *Đứng hẳn lên tầng trên* — cây nến **đóng cửa** phía bên kia. Chỉ mức này mới là phá.

**“Tại sao vai trò của vùng lại đổi?”**
Tấm ván không đổi. **Chỗ đứng của quả bóng đổi.** Cùng một tấm ván: đứng dưới nhìn lên là trần, đứng trên nhìn xuống là sàn. Trên chart cũng vậy: cùng một dải giá, khi giá ở dưới thì nó nằm trên đường đi lên (có thể chặn); khi giá ở trên thì nó nằm trên đường đi xuống (có thể đỡ).

**“Tại sao bóng quay lại chỗ cũ?”**
Bóng nảy lên rồi rơi xuống là chuyện bình thường. Nhưng **không ai hứa** nó rơi đúng vào tấm ván. Có lần nó nảy đi luôn, không về nữa.

**“Tại sao tấm ván cũ có thể làm bóng nảy lên?”**
Chỗ này phải kể một chuyện khác, vì thứ đỡ giá không phải gỗ mà là **con người**:

> Bạn Tí bán gói kẹo với giá 5 đồng. Ngay sau đó giá kẹo vọt lên 8. Tí tiếc lắm: “biết thế mình không bán”. Mấy hôm sau giá kẹo tụt về lại 5. Tí vội mua lại: “coi như mình chưa bán”. Bạn Tèo — người hôm trước đứng xem giá vọt mà không kịp mua — cũng tranh thủ mua ở 5. Hai bạn cùng mua một lúc, nên giá kẹo khó tụt xuống dưới 5.

Tí là **người bán bị kẹt**. Tèo là **người lỡ chuyến**. Nếu ở mức giá cũ có nhiều Tí và nhiều Tèo, mức đó có thể đỡ giá. Nhưng nếu Tí đã mua lại từ lúc giá ở 6 vì sợ quá, còn Tèo thì hết tiền — sẽ không có ai đỡ cả.

### 2.4 Giới hạn của câu chuyện (rất quan trọng)

Câu chuyện giúp nhớ **hình dạng** và **thứ tự**. Nó **sai** nếu hiểu theo nghĩa đen ở bốn chỗ:

1. **Không có tấm ván nào cả.** Thứ chặn hay đỡ giá là lệnh mua bán của con người. Lệnh có thể đã bị rút, đã khớp hết, hoặc chưa từng tồn tại.
2. **Bóng không có trí nhớ.** Không có lực vật lý nào bắt giá phải nảy ở mức cũ. Nếu giá nảy, lý do nằm ở người (§11) — và ta không nhìn thấy họ.
3. **Chuyện Tí và Tèo là [DIỄN GIẢI].** Hợp lý, có cơ sở hành vi, nhưng chart nến không cho biết có bao nhiêu Tí, bao nhiêu Tèo.
4. **“Thủng” trong truyện là một khoảnh khắc; trên chart là một quy ước.** Bạn phải tự quy định: râu qua có tính không, hay phải đợi nến đóng cửa (§5.5).

---

## 3. Mental Model of Breaker Block

![[BB-v3-04-Mental-Model-Ba-Mat-Xich.svg|960]]
*Hình 04 — Ba ô viền đậm là định nghĩa. Hai ô viền đứt là thứ ta theo dõi, không được giả định.*

Giữ trong đầu **một câu** và **ba câu hỏi**:

> **Một câu:** *Breaker là chỗ mà một phe vừa thắng lớn rồi thua ngay tại sân nhà.*

- “Thắng lớn” = từ chỗ đó giá đã đi xa tới mức vượt qua cực trị cũ (mắt xích 2).
- “Thua tại sân nhà” = giá quay lại và vượt qua chính chỗ đó (mắt xích 3).
- “Chỗ đó” = cây nến ngược màu cuối cùng tại swing giữa (mắt xích 1).

**Ba câu hỏi kiểm tra, theo đúng thứ tự:**

| # | Câu hỏi | Nếu “không” thì gọi là gì |
|---|---|---|
| 1 | Có cây nến ngược màu tại đỉnh giữa / đáy giữa không? | Không có vùng nào để gọi tên |
| 2 | Cực trị cũ ở phía bên kia đã bị vi phạm chưa? | Nếu swing giữa vẫn bị phá: **Mitigation Block** |
| 3 | Swing giữa đã bị phá (nến đóng cửa qua) chưa? | OB gốc vẫn đang giữ vai cũ; mới là **ứng viên** |

Ba câu “có” → vùng được gọi là Breaker. Đến đây **mới xong phần tên gọi**. Hai câu hỏi tiếp theo thuộc về tương lai: *giá có quay lại không?* và *nếu quay lại, vùng giữ hay thủng?* Không câu nào trong ba câu đầu trả lời hộ hai câu này.

**Vì sao mô hình ba mắt xích tốt hơn câu “Breaker là OB thất bại”:**
- Nó cho biết **khi nào** được gọi tên (ngay khi mắt xích 3 hoàn tất, không sớm hơn).
- Nó cho biết **gọi là gì khi thiếu** một mắt xích, thay vì gom tất cả vào chữ “Breaker”.
- Nó tách **lịch sử** (ba mắt xích, kiểm tra được) khỏi **kỳ vọng** (retest và phản ứng).

---

## 4. Conceptual Foundation — Order Block / Market Structure / Liquidity

Chỉ nhắc những gì cần để hiểu Breaker. Bản đầy đủ nằm ở các note riêng (liên kết cuối mỗi mục).

### 4.1 Cây nến và swing

![[BB-v3-05-Nen-Va-Swing.svg|960]]
*Hình 05 — Hai viên gạch đầu tiên: nến tăng/nến giảm, và swing high/swing low.*

- **Tầng 1.** Một cây nến là một “ngày làm việc” của giá: sáng mở cửa ở đâu, chiều đóng cửa ở đâu, trong ngày lên cao nhất và xuống thấp nhất tới đâu.
- **Tầng 2.** Đóng cửa cao hơn mở cửa → nến tăng (xanh). Đóng cửa thấp hơn mở cửa → nến giảm (đỏ). Phần giá đã tới nhưng không ở lại là **râu**.
- **Tầng 3.** ICT gọi nến tăng là *up-close candle*, nến giảm là *down-close candle*. Một **swing high** là cây nến có đỉnh cao hơn đỉnh của nến bên trái và bên phải; **swing low** thì ngược lại.
- **Tầng 4.** [QUAN SÁT] Swing chỉ được biết **sau khi** nến bên phải đóng cửa. Mọi thứ xây trên swing đều chậm ít nhất một nến.
- **Tầng 5.** Trong Breaker có ba swing: **cực trị cũ** (đáy cũ / đỉnh cũ), **swing giữa** (đỉnh giữa / đáy giữa — nơi có cây nến Breaker), và **cực trị mới** (đáy thấp hơn / đỉnh cao hơn). Toàn bộ định nghĩa là thứ tự ba swing này bị vượt qua.

### 4.2 Market Structure: HH, HL, LH, LL, BOS, MSS

![[BB-v3-06-Cau-Truc-BOS-MSS.svg|960]]
*Hình 06 — Bậc thang đi lên, và hai kiểu “phá”: phá theo hướng đang đi (BOS) và phá ngược hướng đang đi (MSS).*

- **Tầng 1.** Giá đi như leo cầu thang. Leo lên: mỗi bậc cao hơn bậc trước. Đi xuống: mỗi bậc thấp hơn bậc trước.
- **Tầng 2.** Xu hướng tăng = đỉnh sau cao hơn đỉnh trước (**HH**, higher high) và đáy sau cao hơn đáy trước (**HL**, higher low). Xu hướng giảm = đỉnh sau thấp hơn (**LH**, lower high) và đáy sau thấp hơn (**LL**, lower low).
- **Tầng 3.** [ICT] **BOS** (Break of Structure) = giá vượt một swing **theo hướng đang đi** — cấu trúc được “gia hạn”. **MSS** (Market Structure Shift) = giá vượt một swing **ngược hướng đang đi** — chuỗi bậc thang bị gãy. Chi tiết: [[05-BOS-Break-of-Structure]], [[21-Market-Structure-Shift]].
- **Tầng 4.** [QUAN SÁT] “Vượt” có hai mức: râu vượt, hoặc thân nến đóng cửa vượt. Trong vault, MSS đòi thân nến đóng cửa và thường kèm displacement.
- **Tầng 5 — vai trong Breaker.**

| Thành phần | Vai trong một Bullish Breaker |
|---|---|
| Swing low có trước | Là **đáy cũ**. Việc nó bị vi phạm là mắt xích 2 |
| Swing high kế tiếp | Là **đỉnh giữa**. Cây nến tăng tại đây là Breaker tương lai |
| LL (đáy thấp hơn) | Bằng chứng đáy cũ đã bị vi phạm. Lúc này cấu trúc đọc là *giảm* |
| LH / đỉnh được bảo vệ | Đỉnh giữa chính là cái đỉnh đã sinh ra LL. Chừng nào nó còn nguyên, chuyện giảm còn nguyên |
| MSS | Nến đóng cửa trên đỉnh giữa. Đây là mắt xích 3 |
| BOS | Cú phá *kế tiếp* theo hướng mới (vượt đỉnh cao hơn nữa). Không cần cho định nghĩa |

### 4.3 Order Block

![[BB-v3-07-Order-Block-La-Gi.svg|960]]
*Hình 07 — Bullish OB và Bearish OB là ảnh gương của nhau.*

- **Tầng 1.** Order Block là “chỗ lấy đà”: cây nến cuối cùng đi ngược hướng, ngay trước khi giá chạy mạnh.
- **Tầng 2.** **Bullish OB:** giá đang giảm → một nến giảm cuối cùng → rồi giá tăng vọt. Nến giảm cuối cùng ấy là bullish OB; khi giá quay về, vùng này có thể **đỡ**. **Bearish OB:** nến tăng cuối cùng trước khi giá rơi mạnh; khi giá quay về, vùng này có thể **chặn**.
- **Tầng 3.** [ICT] OB được coi là dấu vết của việc gom/xả lệnh lớn trước một cú displacement. Tên gọi gắn với **displacement**: không có cú chạy mạnh rời khỏi cây nến thì không có lý do gọi nó là OB.
- **Tầng 4.** [QUAN SÁT] Sau cây nến đó giá chạy nhanh. [DIỄN GIẢI] Có lệnh lớn nằm ở đó. Chart nến không phân biệt được “lệnh lớn của tổ chức” với “nhiều lệnh nhỏ cùng lúc” hay “một mẩu tin”.
- **Tầng 5.** Trả lời nhanh các câu hỏi của protocol:

| Câu hỏi | Trả lời |
|---|---|
| OB có phải chỉ là một cây nến? | Thường là một; nếu có vài nến cùng màu liền nhau thì có thể lấy cả chuỗi. Ghi rõ đã chọn cách nào |
| Mọi nến trước một displacement đều là OB? | Không. Phải là nến *ngược màu cuối cùng*, và việc nó có “đáng quan tâm” hay không còn tuỳ vị trí, cấu trúc, liquidity (xem [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]]) |
| Vì sao vùng được xem là có ý nghĩa? | [ICT] vì là nơi lệnh lớn được đặt. [QUAN SÁT] vì đó là nơi cuối cùng giá “đứng lại” trước khi chạy |
| OB nào có thể thành Breaker? | Chỉ OB nằm **ngay tại swing giữa**: bearish OB tại đỉnh giữa (→ Bullish Breaker), bullish OB tại đáy giữa (→ Bearish Breaker) |

**Một OB có thể thất bại vì sao?** [QUAN SÁT] Vì khi giá quay lại, lượng mua chủ động lớn hơn lượng bán đang chờ ở vùng đó (với bearish OB), nên giá đi xuyên qua. *Tại sao* lượng mua lớn hơn thì chart không nói: có thể người bán cũ đã chốt lời hết, có thể có tin, có thể lệnh dừng lỗ bị kích hoạt hàng loạt, có thể khung lớn đang đi hướng ngược lại. Tất cả đều là [DIỄN GIẢI].

![[BB-v3-08-OB-Ba-Ket-Cuc.svg|960]]
*Hình 08 — Ba kết cục khi giá quay lại một bearish OB. Chỉ C là “thất bại” — và C vẫn chưa đủ để gọi là Breaker.*

### 4.4 Liquidity

![[BB-v3-09-Liquidity-Nam-O-Dau.svg|960]]
*Hình 09 — Túi lệnh chờ nằm sau các đỉnh và đáy dễ thấy.*

- **Tầng 1.** Liquidity là “túi lệnh đang chờ”. Người ta hay để lệnh chờ ở những chỗ ai cũng nhìn thấy: ngay trên một cái đỉnh, ngay dưới một cái đáy.
- **Tầng 2.** Trên đỉnh cũ: lệnh dừng lỗ của người đang bán + lệnh mua đuổi của người chờ breakout → **buy-side liquidity (BSL)**. Dưới đáy cũ: lệnh dừng lỗ của người đang mua + lệnh bán đuổi → **sell-side liquidity (SSL)**. Hai đỉnh bằng nhau (**equal highs, EQH**) hay hai đáy bằng nhau (**equal lows, EQL**) là chỗ túi lệnh dày hơn vì mức đó càng dễ thấy.
- **Tầng 3.** [ICT] **Liquidity sweep** = giá vượt qua mức đó rồi quay lại ngay (thường chỉ bằng râu). **Liquidity run** = giá vượt qua và đi tiếp. ICT còn gọi cú vượt đáy cũ rồi đảo chiều là “turtle soup” (xem [[33-Turtle-Soup]]).
- **Tầng 4.** [CƠ CHẾ] Lệnh dừng khi bị chạm sẽ thành lệnh thị trường, nên giá hay bị đẩy thêm một đoạn qua mức đó. Có nghiên cứu độc lập về hiện tượng này quanh các mức tròn trên FX[^osler]. [QUAN SÁT] Chart nến không cho thấy các lệnh; ta chỉ suy ra chúng từ việc mức đó dễ thấy.
- **Tầng 5 — vai trong Breaker.** Một Bullish Breaker chứa **hai** sự kiện liquidity: (a) túi sell-side dưới đáy cũ bị lấy — đây là mắt xích 2; (b) túi buy-side trên đỉnh giữa bị lấy đúng lúc đỉnh giữa bị phá — đây là mắt xích 3. Chi tiết ở §14.

![[BB-v3-10-Sweep-vs-Structural-Break.svg|960]]
*Hình 10 — Cùng là “vượt qua một mức”: sweep là thò chân qua vạch rồi rút về; structural break là bước hẳn sang bên kia.*

> [!warning] Hai sự kiện hay bị nhầm
> **Liquidity sweep ≠ structural break.** Sweep nói về *lệnh chờ đã bị lấy*; cấu trúc chưa đổi. Structural break nói về *giá đã đóng cửa và ở lại bên kia*; cấu trúc đã đổi. Trong một Bullish Breaker, đáy cũ thường bị **sweep hoặc run**, còn đỉnh giữa phải bị **break**. Liên kết: [[19-Liquidity]], [[20-Liquidity-Sweep]].

---

## 5. Precise Definition of Breaker Block

### 5.1 Tầng 1 — Cho người mới

Breaker là **một cái trần đã bị đục thủng, nay nằm dưới chân bạn** (hoặc một cái sàn đã bị đục thủng, nay nằm trên đầu bạn). Nó từng chặn giá. Giá đã vượt qua nó. Bây giờ người ta để mắt xem nó có đỡ giá không.

### 5.2 Tầng 2 — Trình tự giá

```text
BULLISH BREAKER                          BEARISH BREAKER
(thấp – cao – THẤP HƠN – phá đỉnh)       (cao – thấp – CAO HƠN – phá đáy)

            ④ đóng cửa trên đỉnh giữa              ③ đỉnh mới (cao hơn đỉnh cũ)
           /                                      /\
  ② ĐỈNH GIỮA ──[nến tăng]── ⑤ retest     ① đỉnh cũ  \
     /\            /    \    /               /\       \
    /  \          /      \__/               /  \       \       __ ⑤ retest
   /    \        /                         /    \       \     /  \
 ① đáy cũ \     /                                ② ĐÁY GIỮA ──[nến giảm]──
           \   /                                          \
            \_/                                            ④ đóng cửa dưới đáy giữa
          ③ đáy mới (thấp hơn đáy cũ)
```

Đọc bằng lời (Bullish): có một **đáy cũ** → giá hồi lên tạo **đỉnh giữa** → giá rơi xuống **dưới đáy cũ**, tạo đáy mới → giá quay lên và **đóng cửa trên đỉnh giữa** → vùng nến tăng tại đỉnh giữa được gọi là Bullish Breaker → giá có thể hồi về vùng đó.

![[BB-v3-11-Bullish-Breaker-Giai-Phau.svg|960]]
*Hình 11 — Giải phẫu Bullish Breaker. ①–④ là định nghĩa, ⑤ là cái tên, ⑥ là điều có thể xảy ra.*

![[BB-v3-12-Bearish-Breaker-Giai-Phau.svg|960]]
*Hình 12 — Giải phẫu Bearish Breaker. Ảnh gương hoàn toàn của Hình 11.*

### 5.3 Tầng 3 — Định nghĩa theo ICT

**[ICT]** Trong bài giảng *Core Content – Month 04 – ICT Breaker Block*[^ict-bb], ICT mô tả:

- **Bullish Breaker:** một “bullish range or up close candle” nằm ở swing high gần nhất, có trước khi một đáy cũ bị “violated”. Những người đã bán ở vùng đáy đó, khi thấy swing high bị vượt, sẽ tìm cách “mitigate the loss”. Khi giá quay về swing high ấy, đó là setup mua đáng cân nhắc. Ông nói phải chờ giá “break through” swing high để xác nhận rằng đã có một cú “run on stops”.
- **Bearish Breaker:** một “bearish range or down close candle” nằm ở swing low gần nhất, có trước khi một đỉnh cũ bị “violated”. Khi giá phá xuống dưới swing low và quay lại, đó là setup bán đáng cân nhắc.
- Ông lấy **cả khoảng nến** (“the entire range”) trong ví dụ thực tế, và chọn cây nến tăng **cao nhất** trước khi giá rơi.
- Ông phê bình việc chỉ kẻ một đường ngang hỗ trợ/kháng cự mà không có “storyline” giải thích vì sao giá làm vậy.

> [!note] Bài giảng đó KHÔNG nói gì (theo phụ đề đã đối chiếu)
> Không dùng các chữ **“order block”**, **“failed order block”**, **“displacement”**, **“fair value gap”**. Không nói nến phải **đóng cửa** qua swing hay chỉ cần râu. Không nói vào ở **50%** vùng. Không nói **đặt stop ở đâu**, **khi nào Breaker thất bại**, hay phải **thuận khung lớn**. Không so sánh Breaker “mạnh hơn” Mitigation Block hay Order Block. Ông có dùng “market structure shift” và “market structure break” để tả cú phá, và nhắc “turtle soup” cho cú vượt đáy cũ.
>
> **Hệ quả:** mọi thứ trong danh sách trên, nếu bạn gặp ở nơi khác, là phần **cộng đồng hoặc chính bạn thêm vào** — có thể hữu ích, nhưng không phải định nghĩa. Giới hạn của nguồn: đây là phụ đề tự động và bản tóm tắt, chưa nghe đối chiếu âm thanh; các bài giảng khác của ICT có thể nói thêm.

### 5.4 Tầng 4 — Ý nghĩa cấu trúc

Cây nến tại đỉnh giữa không phải cây nến bất kỳ. Nó nằm ở **gốc của nhịp giảm đã tạo ra đáy thấp hơn**. Theo cách đọc cấu trúc, đỉnh giữa là *đỉnh được bảo vệ* của nhịp giảm đó. Khi giá đóng cửa trên nó:

- [QUAN SÁT] Chuỗi “đỉnh thấp hơn, đáy thấp hơn” trên khung này đã gãy.
- [QUAN SÁT] Cái đáy mới, vừa nãy còn là bằng chứng phe bán thắng, nay được đọc lại là một cú đi quá đà rồi đảo ngược.
- [ICT] Vùng nến tại đỉnh giữa được theo dõi với vai ngược lại.

“Breaker = Order Block thất bại” đúng ở chỗ: nến tăng cuối cùng tại đỉnh giữa *chính là* thứ mà định nghĩa OB gọi là bearish OB. Nhưng nó **thiếu** ở chỗ: nó không nhắc gì tới việc cực trị cũ phải bị vi phạm trước, cũng không nhắc OB phải nằm tại swing (§10).

### 5.5 Quy ước làm việc của note này (BB-DEF v3)

Ba chỗ ICT để ngỏ, note phải tự chọn và **ghi tên lựa chọn**:

| Chỗ để ngỏ | Lựa chọn của note | Vì sao | Biến thể cần ghi nếu dùng |
|---|---|---|---|
| **Nến nào?** | Nến tăng cuối cùng tại đỉnh giữa (Bullish); nến giảm cuối cùng tại đáy giữa (Bearish). Nếu có vài nến cùng màu liền nhau: ghi rõ lấy nến cuối hay cả chuỗi | Khớp lời ICT; đúng nghĩa “OB đã thất bại” | Cách B: các nến của nhịp rơi (Hình 13) |
| **Biên vùng?** | Cả râu (từ low tới high của cây nến) | ICT nói dùng “the entire range” | Chỉ thân nến |
| **Thế nào là “phá”?** | **Thân nến đóng cửa** qua swing giữa. Râu vượt qua = chưa tính | Tránh nhầm một cú quét với một cú phá (Hình 10) | Cho phép râu |

![[BB-v3-13-Nen-Nao-La-Breaker.svg|960]]
*Hình 13 — Ba cách đánh dấu đang lưu hành. A khớp bài giảng ICT. B là biến thể của một số thư viện/blog[^lux-bb][^mql5]. C là gọi sai tên: đó là Order Block của nhịp tăng mới.*

![[BB-v3-14-Bien-Vung-Mep-Gan-Mep-Xa.svg|960]]
*Hình 14 — Cả râu hay chỉ thân; và vì sao mép gần / mép xa đổi chỗ khi vùng đổi vai.*

> [!warning] Mâu thuẫn định nghĩa còn mở trong vault
> [[07 - Unicorn Model]] và [[22-Mitigation-Block]] hiện đặt vùng ở **đáy mới** (cách C của Hình 13), khác với quy ước của note này. Đây là khác biệt thật về vị trí vào lệnh và mức dừng. Note này không sửa hai note kia; khi log lệnh, ghi rõ bạn đã dùng cách đánh dấu nào.

### 5.6 Năm khái niệm không được dùng thay nhau

| Khái niệm | Là gì | Cần cây nến cụ thể? | Cần cực trị cũ bị vi phạm? | Vai khi giá quay lại |
|---|---|---|---|---|
| **Order Block** | Nến ngược màu cuối cùng trước một cú chạy mạnh | Có | Không | Vai **gốc** (bullish OB đỡ, bearish OB chặn) |
| **Failed Order Block** | *Bất kỳ* OB nào đã bị nến đóng xuyên qua | Có | Không | Không xác định — tuỳ nhánh (§10) |
| **Breaker Block** | OB tại swing giữa, sau khi cực trị cũ bị vi phạm và swing giữa bị phá | Có | **Có** | Vai **ngược** |
| **Support / Resistance** | Một mức ngang giá đã phản ứng nhiều lần | Không | Không | Giữ vai; nếu bị phá thì “đổi vai” theo TA cổ điển |
| **Supply / Demand zone** | Vùng nền (vài nến nhỏ) trước một cú chạy mạnh | Không (là một cụm) | Không | Vai gốc; một số trường phái cho đổi vai khi bị phá |

### 5.7 Câu hỏi trung tâm: mọi Failed Order Block có phải là Breaker không?

**Không.** Breaker cần thêm hai điều mà một OB thất bại nói chung không có: (1) OB phải nằm **tại swing giữa**, và (2) **cực trị cũ phải đã bị vi phạm** trước khi swing giữa bị phá. Phân nhánh đầy đủ ở §10.

---

## 6. Why Does a Breaker Block Form?

Câu “vì Order Block thất bại” không giải thích gì — nó chỉ đổi chữ. Có ba lớp trả lời, từ chắc tới ít chắc.

### 6.1 Lớp 1 — [QUAN SÁT] Vì giá đã đi một vòng

Một Breaker tồn tại khi và chỉ khi giá đã làm đủ ba việc: bị chặn ở một chỗ, đi xa về phía ngược lại tới mức vượt cực trị cũ, rồi quay lại vượt đúng chỗ đã chặn nó. Breaker không “gây ra” điều gì; nó là **dấu vết** của một cú đảo chiều hai nhịp. Giống vết chân trên cát: nó cho biết có người vừa quay đầu ở đây, không cho biết người đó sẽ đi đâu tiếp.

### 6.2 Lớp 2 — [QUAN SÁT + ICT] Vì cấu trúc của khung đó đổi

![[BB-v3-17-Cau-Truc-Truoc-Va-Sau.svg|960]]
*Hình 17 — Cùng những đỉnh và đáy ấy; ý nghĩa đổi hẳn sau một cây nến đóng cửa.*

Trước cú phá, đỉnh giữa là thứ “giữ” câu chuyện giảm. Sau cú phá, câu chuyện giảm trên khung đó không còn chỗ dựa. Vì cây nến Breaker nằm ngay tại đỉnh giữa, **OB thất bại và cấu trúc đổi là một sự kiện**, không phải hai. Đây là lý do Breaker khác một OB bị thủng ở chỗ khác: nó bị thủng đúng tại điểm mà cấu trúc xoay quanh.

### 6.3 Lớp 3 — [DIỄN GIẢI] Vì những người có mặt ở đó

Ai đó đã bán ở đỉnh giữa. Ai đó đã bán đuổi khi đáy cũ thủng. Khi giá vọt lên trên đỉnh giữa, cả hai nhóm đều lỗ. ICT kể rằng họ sẽ tìm cách giảm lỗ khi giá quay về. Câu chuyện này hợp lý, nhưng chart nến không cho biết các nhóm đó có thật không và còn ở đó không (§11).

### 6.4 “Thất bại” nghĩa là gì, chính xác

![[BB-v3-16-Failure-Co-Bon-Muc.svg|960]]
*Hình 16 — Bốn mức khi giá quay lại một bearish OB ở đỉnh giữa. Chỉ mức D là thất bại.*

| Mức | Nến làm gì | Cấu trúc | Gọi là |
|---|---|---|---|
| A | Chui vào vùng rồi quay đầu, lập đáy thấp hơn nữa | Xu hướng giảm tiếp diễn | OB **giữ** |
| B | Râu vượt đỉnh giữa, thân đóng lại bên dưới | Chưa đổi | Cú quét; OB **chưa thất bại** |
| C | Thân đóng bên trong vùng, dưới đỉnh giữa | Chưa đổi | **Đang bị thử** |
| D | Thân đóng trên đỉnh giữa | **Đổi** (MSS) | OB **thất bại** |

Vậy *failure* gồm đúng hai thành phần nhìn thấy được: **(i)** thân nến đóng cửa ở phía bên kia swing giữa, và **(ii)** giá ở lại phía đó (không bị kéo ngược về ngay). Mọi mô tả khác (“phe bán kiệt sức”, “Smart Money đổi hướng”) là diễn giải về *nguyên nhân* của hai thành phần này.

### 6.5 Vì sao bearish OB thành Bullish Breaker — và ngược lại

**Bearish OB → Bullish Breaker.** Bearish OB là chỗ mà, theo ICT, có lệnh bán. Từ đó giá đã rơi và lập đáy thấp hơn: bên bán đã “đúng”. Khi giá quay lên và đóng cửa trên đỉnh giữa, ba điều đổi cùng lúc: (1) cấu trúc — từ “đỉnh thấp hơn, đáy thấp hơn” sang một cú MSS tăng; (2) vị trí — giá giờ ở **trên** vùng nên vùng nằm trên đường đi xuống; (3) [DIỄN GIẢI] vị thế — những người bán ở vùng đó giờ đang lỗ, và cách thoát lỗ của họ là **mua**. Một vùng từng tập trung lệnh bán nay có thể tập trung lệnh mua.

**Bullish OB → Bearish Breaker.** Ảnh gương: bullish OB tại đáy giữa từng đỡ giá, đẩy giá lên vượt đỉnh cũ. Khi giá quay xuống và đóng cửa dưới đáy giữa: cấu trúc gãy theo hướng giảm; giá ở **dưới** vùng; [DIỄN GIẢI] những người mua ở vùng đó đang lỗ, và cách thoát lỗ của họ là **bán**.

Điểm chung: **vùng không đổi; phía mà giá đứng và phía mà người kẹt muốn thoát thì đổi.**

---

## 7. Core Formation Mechanism

![[BB-v3-15-Tam-Buoc-Hinh-Thanh.svg|960]]
*Hình 15 — Tám khung hình. Mỗi khung chỉ vẽ những nến đã đóng cửa tại thời điểm đó.*

Protocol nêu 8 bước. Note giữ 8 bước nhưng **chèn rõ** một việc mà chuỗi của protocol không gọi tên: việc cực trị cũ bị vi phạm (nằm trong bước 2 dưới đây). Ví dụ là Bullish; Bearish đảo ngược mọi chữ lên/xuống.

**Bước 1 — Order Block gốc hình thành**
- *Giá làm gì:* tăng tới đỉnh giữa rồi quay xuống. Nến tăng cuối cùng tại đỉnh là bearish OB.
- *Cấu trúc:* có một đáy cũ và một đỉnh giữa. Chưa có gì đặc biệt.
- *Liquidity:* dưới đáy cũ có túi sell-side; trên đỉnh giữa bắt đầu có túi buy-side (stop của người vừa bán).
- *Vì sao quan trọng:* đây là thứ sau này mang tên Breaker. Phải ghi lại **lúc này**, không phải lúc đã biết kết quả.
- *Điều xác nhận bước kế:* giá rời vùng đi xuống.
- *Nếu không xảy ra:* không có OB tại swing → không có gì để thành Breaker.

**Bước 2 — Giá rời vùng và vi phạm cực trị cũ**
- *Giá làm gì:* rơi từ đỉnh giữa xuống dưới đáy cũ, tạo đáy mới.
- *Cấu trúc:* đáy thấp hơn. Trên khung này, đọc là giảm. OB trông như đã thắng.
- *Liquidity:* túi sell-side dưới đáy cũ bị lấy. ICT gọi là run on stops.
- *Vì sao quan trọng:* đây là mắt xích tách Breaker khỏi Mitigation Block.
- *Điều xác nhận bước kế:* giá ngừng rơi và bật lên.
- *Nếu không xảy ra:* (giá dừng trên đáy cũ) → nếu sau đó đỉnh giữa vẫn bị phá, vùng là Mitigation Block.

**Bước 3 — Giá quay lại vùng Order Block**
- *Giá làm gì:* bật lên, chui vào vùng OB.
- *Cấu trúc:* chưa đổi. Đây có thể chỉ là một nhịp hồi trong xu hướng giảm.
- *Liquidity:* giá tiến gần túi buy-side trên đỉnh giữa.
- *Vì sao quan trọng:* đây là lúc OB được thử thách. Hai tương lai còn mở ngang nhau (Hình 32).
- *Điều xác nhận bước kế:* nến đóng cửa ở đâu so với đỉnh giữa.
- *Nếu không xảy ra:* (giá không quay lại) → không có gì để thất bại; xu hướng giảm tiếp diễn.

**Bước 4 — Order Block không giữ được; cấu trúc bị phá**
- *Giá làm gì:* một thân nến đóng cửa trên đỉnh giữa.
- *Cấu trúc:* MSS tăng trên khung này.
- *Liquidity:* túi buy-side trên đỉnh giữa bị lấy; lệnh dừng thành lệnh mua, có thể đẩy giá thêm.
- *Vì sao quan trọng:* mắt xích 3. Đây là khoảnh khắc Breaker **ra đời về mặt định nghĩa**.
- *Điều xác nhận bước kế:* giá ở lại phía trên, không bị kéo về ngay.
- *Nếu không xảy ra:* (giá bị đẩy ra, hoặc chỉ râu vượt) → OB giữ; không có Breaker (Hình 16 A, B).

**Bước 5 — Giá đi tiếp theo hướng mới**
- *Giá làm gì:* tiếp tục tăng, rời xa vùng.
- *Cấu trúc:* nếu vượt thêm một đỉnh nữa thì có BOS tăng.
- *Liquidity:* giá hướng tới các túi buy-side cao hơn.
- *Vì sao quan trọng:* cho biết cú phá dứt khoát hay lê lết (Hình 34). Không phải điều kiện định nghĩa.
- *Điều xác nhận bước kế:* —
- *Nếu không xảy ra:* (giá quay lại ngay bên dưới đỉnh giữa) → Breaker yếu; có thể chỉ là một cú quét phía trên.

**Bước 6 — Vùng cũ được xác định là Breaker**
- *Giá làm gì:* không gì mới. Đây là việc của **bạn**: kiểm tra đủ ba mắt xích, khoá biên vùng.
- *Vì sao quan trọng:* tách “thấy cú phá” khỏi “gọi tên vùng”. Vùng khoá rồi thì không dời.
- *Nếu bỏ qua:* bạn sẽ vẽ vùng sau khi thấy giá bật — tức là hindsight.

**Bước 7 — Giá quay lại vùng Breaker**
- *Giá làm gì:* hồi về, chạm vùng từ phía trên.
- *Cấu trúc:* một nhịp hồi trong nhịp tăng mới.
- *Liquidity:* nhịp hồi có thể tạo các đáy nhỏ ngay trên/trong vùng — nơi có túi lệnh mới.
- *Vì sao quan trọng:* chỉ khi có bước này mới có chuyện để bàn về lệnh.
- *Nếu không xảy ra:* Breaker hết hạn. Không đuổi theo giá.

**Bước 8 — Giá có thể phản ứng**
- *Giá làm gì:* bật lên (giữ), đóng cửa xuyên qua (thủng), hoặc lình xình (chưa rõ).
- *Vì sao quan trọng:* đây là thứ duy nhất trong cả chuỗi mà bạn **chưa biết** khi lập kế hoạch.
- *Điều xác nhận:* bằng chứng trên khung nhỏ (§22).
- *Nếu thủng:* Breaker thất bại — ghi lại như mọi mẫu khác.

> [!tip] Điều chuỗi 8 bước dạy
> Bước 1–4 là **lịch sử**: đã xảy ra, kiểm tra được, không tranh cãi. Bước 5–6 là **việc của bạn**. Bước 7–8 là **tương lai**. Người giao dịch giỏi không phải người đoán đúng bước 8, mà là người không lẫn bước 6 với bước 8.

---

## 8. Bullish Breaker Block

### 8.1 Trình tự hình thành

Sơ đồ của protocol (Previous High → giá giảm → Bearish OB → phá cấu trúc lên → displacement → quay lại → Bullish Breaker → giá tăng) đúng về hướng nhưng **thiếu và thừa** so với lời ICT:

- **Thiếu:** bước “đáy cũ bị vi phạm”. Theo ICT đây là một phần của định nghĩa.
- **Thừa (nếu coi là bắt buộc):** “displacement”. ICT chỉ tả cú phá là mạnh; không đặt nó thành điều kiện.

Trình tự đã chỉnh:

```text
   Đáy cũ (swing low có trước)
        ↓
   Giá hồi lên → ĐỈNH GIỮA; nến tăng cuối cùng tại đây = bearish OB
        ↓
   Giá rơi xuống DƯỚI đáy cũ → đáy mới            ← mắt xích 2 (theo ICT)
        ↓
   Giá quay lên, thân nến đóng cửa TRÊN đỉnh giữa ← mắt xích 3 (MSS)
        ↓
   Vùng nến tăng ở đỉnh giữa = BULLISH BREAKER
        ↓
   (có thể) giá hồi về vùng → (có thể) bật lên
```

### 8.2 Mười hai câu hỏi chi tiết

| Câu hỏi | Trả lời | Nhãn |
|---|---|---|
| Bắt nguồn từ loại OB nào? | **Bearish OB** — nến tăng cuối cùng tại đỉnh giữa | [ICT] về vị trí nến; chữ “OB” là của cộng đồng |
| OB cũ thất bại thế nào? | Giá quay lại và thân nến đóng cửa trên đỉnh giữa (mức D, Hình 16) | [QUAN SÁT] |
| Cấu trúc nào cần bị phá? | **Đỉnh giữa** — swing high chứa cây nến đó | [ICT] |
| Có cần sweep sell-side không? | Cần **đáy cũ bị vi phạm**. Không cần cú vi phạm đó “đẹp” hay lấy một túi lớn | [ICT] cho việc vi phạm; chất lượng là bộ lọc của bạn |
| Có cần MSS hoặc BOS không? | Cú phá đỉnh giữa *chính là* một MSS trên khung đó. Không cần thêm BOS | [ICT] |
| Có cần displacement không? | Không nằm trong định nghĩa. Là bằng chứng chất lượng | [GIẢ THUYẾT] rằng có thì tốt hơn |
| Có cần FVG không? | Không | Không có trong bài giảng Breaker |
| Khi nào xác nhận được? | Khi nến phá đỉnh giữa **đóng cửa** | Quy ước của note |
| Chờ nến đóng hay râu là đủ? | ICT không nói rõ. Note chọn **chờ đóng cửa** để không nhầm với cú quét | Quy ước của note |
| Vùng là nến nào? | Nến tăng cuối cùng tại đỉnh giữa, cả râu | [ICT] |
| Khi giá quay lại, điều gì khiến vùng đáng chú ý? | Nó là chỗ cấu trúc vừa đổi; có thể có người kẹt muốn thoát, người lỡ muốn vào | [DIỄN GIẢI] |
| Khi nào vùng hết hợp lệ? | Thân nến đóng dưới **mép xa** (mép dưới) và giá ở lại đó; hoặc vùng hết hạn (§18) | Quy ước của note — ICT không nêu |

### 8.3 Ba ví dụ chuỗi giá

**Ví dụ 1 — Sách giáo khoa.**

![[BB-v3-18-Bullish-Vi-Du-1-Textbook.svg|960]]
*Hình 18 — Đủ ba mắt xích, có retest, retest giữ. Số dưới chart là thứ tự nến.*

**Ví dụ 2 — Trông giống hệt nhưng thiếu một mắt xích.**

![[BB-v3-19-Bullish-Vi-Du-2-Thieu-Dieu-Kien.svg|960]]
*Hình 19 — Đáy cũ không bị vi phạm. Theo ICT đây là Mitigation Block.*

Bài học: hành vi giá sau đó có thể giống hệt. Lý do vẫn phải gọi đúng tên: (a) mức “sai” của ý tưởng nằm ở chỗ khác; (b) nếu trộn hai loại vào một rổ, bạn không bao giờ biết việc “cực trị cũ bị vi phạm” có tạo khác biệt hay không.

**Ví dụ 3 — Đúng định nghĩa và thất bại.**

![[BB-v3-20-Bullish-Vi-Du-3-That-Bai.svg|960]]
*Hình 20 — Mười bảy nến đầu giống Ví dụ 1. Khi giá quay lại, vùng không đỡ được.*

Bài học: định nghĩa đúng không hứa kết quả. Ai “mua vì giá chạm Breaker” ở nến 21 đã vào lệnh mà không có bằng chứng nào ngoài cái tên.

---

## 9. Bearish Breaker Block

### 9.1 Trình tự hình thành

Sơ đồ của protocol (Previous Low → giá tăng → Bullish OB → phá cấu trúc xuống → displacement → quay lại → Bearish Breaker → giá giảm) cần cùng hai chỉnh sửa như §8.1:

```text
   Đỉnh cũ (swing high có trước)
        ↓
   Giá hồi xuống → ĐÁY GIỮA; nến giảm cuối cùng tại đây = bullish OB
        ↓
   Giá tăng lên TRÊN đỉnh cũ → đỉnh mới            ← mắt xích 2
        ↓
   Giá quay xuống, thân nến đóng cửa DƯỚI đáy giữa ← mắt xích 3 (MSS)
        ↓
   Vùng nến giảm ở đáy giữa = BEARISH BREAKER
        ↓
   (có thể) giá hồi lên vùng → (có thể) rơi tiếp
```

### 9.2 Các câu hỏi chi tiết

| Câu hỏi | Trả lời | Nhãn |
|---|---|---|
| Bắt nguồn từ loại OB nào? | **Bullish OB** — nến giảm cuối cùng tại đáy giữa | [ICT] về vị trí nến |
| OB cũ thất bại thế nào? | Giá quay lại và thân nến đóng cửa dưới đáy giữa | [QUAN SÁT] |
| Cấu trúc nào cần bị phá? | **Đáy giữa** — swing low chứa cây nến đó | [ICT] |
| Có cần sweep buy-side không? | Cần **đỉnh cũ bị vi phạm** | [ICT] |
| Có cần MSS hoặc BOS không? | Cú phá đáy giữa là một MSS giảm trên khung đó | [ICT] |
| Displacement? FVG? | Không nằm trong định nghĩa | — |
| Khi nào xác nhận? | Khi nến phá đáy giữa đóng cửa | Quy ước của note |
| Vùng nào được đánh dấu? | Nến giảm cuối cùng tại đáy giữa, cả râu | [ICT] |
| Vì sao giá có thể rơi khi retest? | Vùng nằm trên đường giá đi lên; có thể có người mua bị kẹt muốn bán để thoát, người lỡ cú rơi muốn bán | [DIỄN GIẢI] |
| Khi nào hết hợp lệ? | Thân nến đóng trên **mép xa** (mép trên) và giá ở lại đó; hoặc hết hạn | Quy ước của note |

ICT thêm một câu về hướng Bearish: sau khi đáy bị phá, mọi nhịp hồi về sau được nhìn như cơ hội bán mới[^ict-bb]. Đây là một cách đọc **bối cảnh**, không phải lời hứa rằng nhịp hồi nào cũng bán được.

### 9.3 Ba ví dụ chuỗi giá

**Ví dụ 1 — Sách giáo khoa.**

![[BB-v3-21-Bearish-Vi-Du-1-Textbook.svg|960]]
*Hình 21 — Ảnh gương của Hình 18.*

**Ví dụ 2 — Râu đâm qua đáy giữa nhưng thân không đóng qua.** Ở đây thiếu mắt xích 3 (khác với Ví dụ 2 phía Bullish, nơi thiếu mắt xích 2).

![[BB-v3-22-Bearish-Vi-Du-2-Thieu-Dieu-Kien.svg|960]]
*Hình 22 — Bullish OB tại đáy giữa vẫn sống. Vẽ Bearish Breaker ở đây là vẽ sớm.*

**Ví dụ 3 — Đúng định nghĩa và thất bại.**

![[BB-v3-23-Bearish-Vi-Du-3-That-Bai.svg|960]]
*Hình 23 — Giá hồi lên, đóng cửa trên mép xa của vùng.*

> [!note] Đối xứng trong định nghĩa, không chắc đối xứng ngoài thị trường
> Trên giấy, Bullish và Bearish Breaker là ảnh gương. Ngoài thị trường, tốc độ giảm và tốc độ tăng của một sản phẩm có thể khác nhau (đặc biệt với chỉ số chứng khoán). Vì vậy khi ghi nhật ký, **tách hai chiều** thay vì gộp chung.

---

## 10. Failed Order Block vs Breaker Block

![[BB-v3-24-Failed-OB-Bon-Nhanh.svg|960]]
*Hình 24 — Một bearish OB bị giá đi vào: bốn nhánh, bốn cái tên.*

### 10.1 Bảy câu hỏi của protocol

1. **OB bị xuyên thủng có tự động thành Breaker không?** Không. Cần OB nằm tại swing giữa và cực trị cũ đã bị vi phạm.
2. **Phá vùng OB có đủ không?** Không. Thứ phải bị phá là **swing chứa OB**. Nếu OB nằm tại đỉnh giữa thì hai việc trùng nhau; nếu OB nằm giữa một nhịp thì phá OB không phá swing nào cả (nhánh 3 của Hình 24, Case C ở §26).
3. **Có cần phá một structural swing không?** Có — đó là mắt xích 3. [ICT]
4. **Có cần displacement xác nhận không?** Không theo định nghĩa. Là bằng chứng chất lượng. [GIẢ THUYẾT]
5. **Có cần một lần retest không?** Không. Retest là điều kiện để *giao dịch*, không phải để *được gọi là Breaker*. Một Breaker không bao giờ được chạm lại vẫn là Breaker.
6. **Breaker hình thành lúc phá hay chỉ xác nhận sau một sự kiện tiếp theo?** Theo lời ICT, phải chờ giá phá qua swing để xác nhận. Trong note: Breaker **có tên** từ lúc nến phá swing giữa đóng cửa. Không cần chờ thêm sự kiện nào.
7. **Có OB thất bại mà không bao giờ thành Breaker không?** Có, rất nhiều: OB giữa nhịp bị thủng; OB tại swing bị thủng nhưng cực trị cũ chưa bị vi phạm (thành Mitigation Block).

### 10.2 Bảng so sánh

| Yếu tố | Failed OB (nghĩa rộng) | Breaker — theo lời ICT | Điều kiện note thêm vào |
|---|---|---|---|
| OB gốc tồn tại | Có | Có — nến up/down-close tại swing gần nhất | Ghi lại lúc swing vừa hình thành |
| OB gốc thất bại | Có (đó là định nghĩa) | Có — swing chứa nó bị phá | “Thất bại” = thân nến đóng qua |
| OB nằm tại swing | Không bắt buộc | **Bắt buộc** | — |
| Cực trị cũ bị vi phạm trước | Không bắt buộc | **Bắt buộc** (“prior to an old low/high being violated”) | Ghi thêm đó là túi liquidity nào |
| Structural break | Không bắt buộc | **Bắt buộc** (“break through that swing”) | Bằng thân nến |
| Displacement | Không | Không nêu thành điều kiện | Ghi như một đặc điểm chất lượng |
| Role reversal | Không chắc | Có — giá quay lại là setup theo hướng mới | — |
| Retest | Không | Không bắt buộc để có tên; cần để có setup | Cần cho lệnh |
| Phân loại ICT | Không có tên riêng | Breaker Block | — |

> [!important] Một câu để nhớ
> **Failed OB trả lời “vùng này còn làm vai cũ không?”. Breaker trả lời thêm “và nó đã thua theo đúng trình tự nào?”.** Chỉ câu trả lời thứ hai mới cho bạn một cái tên, một hướng, và một mức để biết mình sai.

---

## 11. Why Does the Role Reverse?

Câu hỏi: vì sao một vùng từng đỡ lại có thể chặn, và một vùng từng chặn lại có thể đỡ? Năm góc nhìn, xếp từ chắc tới ít chắc.

### 11.1 Góc ICT

**[ICT]** Câu chuyện của ICT cho Bullish Breaker: giá chạy xuống dưới đáy cũ, kích hoạt lệnh dừng bán và kéo thêm người bán đuổi. Sau đó giá đảo chiều, vượt đỉnh giữa. Những người đã bán nay lỗ và sẽ tìm cách “mitigate the loss” khi giá quay về; còn phía đã mua ở đáy sẽ mua thêm. Vì vậy khi giá hồi về đỉnh giữa, ông coi đó là chỗ mua[^ict-bb].

Đây là một **câu chuyện về vị thế**, được kể từ hình dạng của chart. Nó không phải là quan sát. ICT cũng nhấn mạnh phải có “storyline” — tức ông coi câu chuyện là một phần của phương pháp, không phải thứ suy ra được từ nến.

### 11.2 Góc cấu trúc

**[QUAN SÁT]** Trước cú phá, vùng nằm ở *gốc của nhịp giảm* — nơi phe bán mạnh nhất. Sau cú phá, vùng nằm ở *gốc của bằng chứng rằng phe bán đã thua*. Cùng một dải giá, nhưng thứ nó “đại diện” trong câu chuyện cấu trúc đã lật.

Cẩn thận: đây là cách **đọc**, chưa phải lý do khiến giá phải làm gì. Cấu trúc đổi là điều chắc chắn; việc cấu trúc mới sẽ tiếp diễn là kỳ vọng.

### 11.3 Góc khớp lệnh

Trước hết, ba loại lệnh nói kiểu trẻ con:

| Loại lệnh | Nói kiểu trẻ con | Tác động lên giá |
|---|---|---|
| **Limit** (lệnh chờ giá tốt) | “Con chỉ mua kẹo nếu giá xuống còn 5 đồng.” | **Hãm** giá: đứng chờ sẵn, ai muốn bán thì bán cho con |
| **Stop** (lệnh chờ giá xấu) | “Nếu giá lên tới 9 đồng thì mua ngay giúp con, kẻo lên nữa.” | **Đẩy** giá: khi bị chạm, biến thành mua ngay |
| **Market** (lệnh mua/bán ngay) | “Con mua ngay bây giờ, giá nào cũng được.” | **Đẩy** giá: ăn hết lệnh chờ ở mức gần nhất rồi tới mức kế |

Stop-loss là một lệnh stop dùng để thoát lệnh đang lỗ. Người đang **bán** thoát lỗ bằng cách **mua**; người đang **mua** thoát lỗ bằng cách **bán**. Đây là chìa khoá của cả §11.

![[BB-v3-26-Luc-Pha-Va-Luc-Quay-Lai.svg|960]]
*Hình 26 — Hai khoảnh khắc, hai cơ chế khác nhau.*

- **Lúc phá** — [CƠ CHẾ] Trên đỉnh giữa có lệnh dừng mua (stop-loss của người bán, lệnh breakout). Khi giá chạm, chúng thành lệnh mua ngay; lượng mua dồn dập ăn hết lệnh bán chờ ở các mức gần → giá nhảy. Đây là hiện tượng đã được nghiên cứu cho các mức tròn trên FX[^osler]; chưa có nghiên cứu tương tự cho Order Block hay Breaker.
- **Lúc quay lại** — [DIỄN GIẢI] Thứ có thể đỡ giá là lệnh **limit mua** đặt quanh vùng, và những người đang muốn mua để thoát vị thế bán. Thứ này không đẩy giá lên; nó **hãm** đà rơi. Nếu lượng bán tới lớn hơn, vùng thủng.

Chart nến không cho thấy bất kỳ lệnh nào trong số này. Không được nói “tại Breaker có lệnh mua của tổ chức”.

### 11.4 Góc vị thế của trader

![[BB-v3-25-Ai-Dang-Dung-O-Dau.svg|960]]
*Hình 25 — Năm nhóm có thể có mặt quanh một Bullish Breaker ngay sau cú phá.*

| Tình huống của protocol | Trong một Bullish Breaker | Trong một Bearish Breaker |
|---|---|---|
| Người bị kẹt khi luận điểm thất bại | Người **bán** ở đỉnh giữa và người bán đuổi dưới đáy cũ | Người **mua** ở đáy giữa và người mua đuổi trên đỉnh cũ |
| Phe có thể kiểm soát sau cú phá | Phe mua | Phe bán |
| Người tham gia theo hướng mới | Người lỡ cú phá, chờ mua khi giá hồi | Người lỡ cú rơi, chờ bán khi giá hồi |
| Người giữ vị thế cũ phải thoát | Người bán: thoát bằng cách **mua** | Người mua: thoát bằng cách **bán** |

Cả bốn dòng là **[GIẢ THUYẾT] về cơ chế**. Chúng có nền tảng hành vi: con người có xu hướng giữ lệnh lỗ và thoát khi giá về gần hoà vốn (disposition effect[^shef]). Nhưng trên FX giao ngay không có sổ lệnh chung để đo.

Có một điểm tự mâu thuẫn mà các bài dạy Breaker hay bỏ qua: **cùng một cú phá vừa tạo ra người bị kẹt, vừa giải thoát họ.** Người bán nào đặt stop ngay trên đỉnh giữa đã bị thoát lệnh lúc phá — họ không còn ở đó để “mua lại ở hoà vốn” nữa. Chỉ những người bán *không* đặt stop gần mới còn kẹt. Ta không biết tỷ lệ giữa hai nhóm.

### 11.5 Vì sao retest quan trọng — và vì sao nó không luôn xảy ra

![[BB-v3-27-Retest-Ba-Ket-Cuc.svg|960]]
*Hình 27 — Ba kết cục sau khi Breaker được gọi tên. Cả ba phải được ghi.*

| Câu hỏi | Quan sát được | Giải thích hợp lý | Cách ICT diễn giải | Giả định chưa kiểm chứng |
|---|---|---|---|---|
| Vì sao giá quay lại? | Sau một nhịp đi nhanh, giá thường hồi một phần | Người mua sớm chốt lời; lệnh chờ ở xa mỏng dần | Giá quay về để “mitigate” / lấy thêm lệnh | Rằng giá *phải* quay về đúng vùng này |
| Vì sao có thể phản ứng? | Đôi khi nến chạm vùng rồi đóng cửa quay ra | Lệnh limit và người thoát lệnh tụ quanh mức dễ thấy | Người kẹt giảm lỗ, phe thắng thêm lệnh | Rằng các lệnh đó hiện đang có mặt |
| Vì sao không luôn phản ứng? | Đôi khi nến đóng xuyên qua | Người kẹt đã thoát; lượng bán tới lớn hơn; khung lớn đi hướng ngược | “Không có institutional sponsorship” | Rằng ta biết trước được trường hợp nào |

Retest quan trọng vì đó là **lần duy nhất** câu chuyện ở §11.1–11.4 được thử nghiệm. Trước retest, mọi thứ chỉ là kể chuyện.

---

## 12. Breaker Block and Market Mechanics

Mục này trả lời: trong các lời giải thích về Breaker, cái nào có bằng chứng ngoài ICT?

### 12.1 Thứ có bằng chứng độc lập (nhưng không nói về Breaker)

- **Lệnh dừng tụ quanh mức dễ thấy và gây chuyển động tiếp diễn khi bị chạm.** Nghiên cứu lệnh FX của Osler[^osler] cho thấy: lệnh chốt lời tụ *tại* các mức tròn (làm giá hay đảo chiều ở đó); lệnh dừng lỗ tụ *ngay bên kia* các mức tròn (làm giá đi tiếp nhanh khi mức bị vượt). → Ủng hộ phần “lúc phá” của Hình 26. Nghiên cứu nói về mức tròn, **không** về OB hay Breaker.
- **Mức hỗ trợ/kháng cự phản ánh nơi lệnh chờ tụ lại.** Kavajecz & Odders-White[^kav] cho thấy các mức S/R kỹ thuật trùng với chỗ lệnh limit dày trong sổ lệnh. → Ủng hộ ý “mức dễ thấy thì có lệnh”.
- **Mức S/R làm giá đảo chiều nhiều hơn ngẫu nhiên, và mức đã bật nhiều lần thì dễ bật lần nữa.** Kết quả của Chung & Bellotti[^chung] trên dữ liệu trong ngày. → Chú ý: điều này **ngược** với niềm tin phổ biến trong cộng đồng ICT rằng “lần chạm đầu là tốt nhất, càng chạm càng yếu”. Hai điều không thể cùng đúng một cách tổng quát → [BACKTEST REQUIRED].
- **Người ta giữ lệnh lỗ quá lâu và hay thoát quanh hoà vốn.** Đây là disposition effect của Shefrin & Statman[^shef]. → Ủng hộ khả năng tồn tại “người bán bị kẹt”.

### 12.2 Thứ chỉ là diễn giải

- Rằng một nhóm cụ thể (“Smart Money”, tổ chức) **cố ý** tạo ra cú quét đáy cũ để gom lệnh.
- Rằng **trong vùng Breaker đang có** lệnh tổ chức chờ sẵn.
- Rằng cú phá “chứng tỏ” ai đó đã đổi hướng.

Không điều nào suy ra được từ nến. Không dùng câu kiểu *“Smart Money đã thiết kế chính xác Breaker này”*.

### 12.3 Thứ quan sát được

Chỉ có vậy: giá đã vượt cực trị cũ; nến đã đóng cửa qua swing giữa; giá có/không quay lại; nến đóng cửa trong hay ngoài vùng.

### 12.4 Lời giải thích “không có cơ chế nào cả”

Phải luôn giữ một khả năng trên bàn: **vùng Breaker được chạm lại và “bật” chỉ vì hình học**. Vùng nằm ngay sát giá sau cú phá nên dễ bị chạm lại; và mỗi lần chạm thì giá hoặc đi lên hoặc đi xuống. Bản v2 của note đã thử định nghĩa Breaker trên một chuỗi giá *ngẫu nhiên hoàn toàn* (không có ai đặt lệnh): định nghĩa vẫn tìm ra rất nhiều “Breaker”, phần lớn được chạm lại nhanh, và chúng “giữ” khoảng một nửa số lần — ngang với một vùng ngẫu nhiên cùng kích thước (chi tiết trong bản backup v2).

Ý nghĩa: **thấy Breaker, thấy giá quay lại, thấy giá bật — tự chúng không chứng minh gì.** Thứ phải chứng minh là: trên dữ liệu thật, Breaker (có bộ lọc của bạn) giữ giá *tốt hơn* một vùng bất kỳ ở cùng vị trí. Đó là việc của §27.

---

## 13. Breaker Block vs Related Concepts

### 13.1 Breaker Block vs Order Block

| Khía cạnh | Order Block | Breaker Block |
|---|---|---|
| Hình thành | Nến ngược màu cuối cùng trước một cú chạy mạnh | Chính cây nến đó, *nếu* nằm tại swing giữa, *sau khi* cực trị cũ bị vi phạm và swing giữa bị phá |
| Bối cảnh cấu trúc | Thường ở gốc một nhịp theo xu hướng | Ở điểm cấu trúc vừa gãy |
| Vai | Vai gốc: bullish OB đỡ, bearish OB chặn | Vai ngược: bearish OB cũ đỡ, bullish OB cũ chặn |
| Thất bại | Thân nến đóng qua mép xa | Thân nến đóng qua mép xa (mép xa nay ở phía ngược lại — Hình 14) |
| Retest | Lần quay lại đầu tiên là lúc OB được thử | Lần quay lại đầu tiên *sau khi đổi tên* là lúc Breaker được thử |
| Cách dùng | Tìm chỗ vào **thuận** nhịp đã tạo ra OB | Tìm chỗ vào **thuận** nhịp đã phá OB |

Trong cùng một cú đảo chiều thường có **cả hai**: Breaker (ở đỉnh giữa, nông) và Order Block mới (ở đáy mới, sâu) — xem Hình 36.

### 13.2 Breaker Block vs Mitigation Block

![[BB-v3-28-Breaker-vs-Mitigation-Block.svg|960]]
*Hình 28 — Khác nhau ở đúng một chỗ: đáy cũ có bị vi phạm không.*

- **Khác ở trình tự:** Breaker = thấp – cao – **thấp hơn** – phá đỉnh. Mitigation Block = thấp – cao – **cao hơn** (failure swing) – phá đỉnh.
- **Khác ở điều kiện cấu trúc:** với Breaker, ngay trước cú phá, cấu trúc đang đọc là *giảm* (vừa có đáy thấp hơn) — cú phá là một cú lật ngược. Với Mitigation Block, cấu trúc chưa từng có đáy thấp hơn — cú phá là sự tiếp diễn sau một nhịp hồi không tới đích.
- **Vì sao hay nhầm:** vùng được đánh dấu giống nhau (nến tại swing giữa), cú phá giống nhau, retest giống nhau. Chỉ khác ở một cái đáy nằm phía bên trái chart.
- **Khi nào là Breaker thay vì Mitigation:** khi cực trị cũ đã bị vượt — dù chỉ bằng râu. Tóm tắt của một thư viện thuật ngữ: có sweep thì là breaker, hụt thì là mitigation block[^lux-mb].
- **Trường hợp mơ hồ:** đáy mới chỉ thấp hơn đáy cũ một chút xíu (Case D, §26). Ghi “mơ hồ” thay vì ép.

Về câu “Breaker mạnh hơn Mitigation Block”: phổ biến trong cộng đồng, **không tìm thấy** trong bài giảng Breaker đã đối chiếu; bài giảng Mitigation Block chỉ tiếp cận được qua bản tóm tắt[^ict-mb]. Coi là [GIẢ THUYẾT].

### 13.3 Breaker Block vs Rejection Block

| Khía cạnh | Rejection Block | Breaker Block |
|---|---|---|
| Định nghĩa | Phần **râu** của một đỉnh/đáy: từ thân nến cao nhất (thấp nhất) tới đầu râu | Cả cây nến ngược màu tại swing giữa |
| Hình thành | Ngay khi swing có râu dài hình thành | Sau một trình tự ba mắt xích |
| Hành vi giá | Giá quay lại *chạm vào vùng râu* rồi đảo chiều | Giá quay lại vùng *sau khi đã vượt qua nó* |
| Ý nghĩa cấu trúc | Swing chưa bị phá; vùng giữ **vai gốc** | Swing đã bị phá; vùng **đổi vai** |
| Phân biệt thực hành | Nằm *ở cực trị* | Nằm *ở swing giữa*, phía sau lưng giá |

Chi tiết: [[28-Rejection-Block]]. Lần nghiên cứu này chưa đối chiếu bài giảng gốc của ICT cho Rejection Block; mô tả theo cách dùng phổ biến.

### 13.4 Breaker Block vs Reclaimed Order Block

[ICT — theo cách dùng phổ biến, chưa đối chiếu bài giảng gốc] **Reclaimed OB** là một OB cũ đã từng bị giá đi xuyên qua, nay giá quay trở lại phía ban đầu và vùng ấy **làm lại vai gốc**. Ví dụ: một bullish OB bị thủng trong nhịp giảm; sau khi giá đảo chiều và vượt lên trên nó, vùng đó lại được dùng làm hỗ trợ.

Khác biệt cốt lõi: **Reclaimed OB lấy lại vai cũ; Breaker đổi sang vai mới.** Trong cùng một cú đảo chiều, hai vùng thường nằm sát nhau (bullish OB cũ ngay dưới đỉnh giữa), nên hay bị gọi lẫn. Phân biệt bằng cây nến: Reclaimed OB (phía mua) là một nến **giảm**; Bullish Breaker là một nến **tăng**.

![[BB-v3-29-Ho-Hang-Block.svg|960]]
*Hình 29 — Năm cái tên trong họ “block”, ví dụ phía mua.*

### 13.5 Breaker Block vs Support / Resistance

“Hỗ trợ bị phá thành kháng cự” là ý tưởng có từ rất lâu trước ICT. Breaker là một **trường hợp hẹp** của ý tưởng đó, thêm ba ràng buộc: phải là một cây nến cụ thể tại swing; phải có cực trị cũ bị vi phạm trước; phải có câu chuyện về người bị kẹt.

Vì sao không phải mọi hỗ trợ bị phá đều là Breaker:
- Một mức ngang được chạm nhiều lần rồi bị phá **không có** cây nến tại swing giữa và **không có** cực trị cũ bị vi phạm.
- Một hỗ trợ bị phá trong xu hướng giảm đang tiếp diễn giống trình tự của **Mitigation Block** hơn.
- Ngược lại, một Breaker có thể *đồng thời* là mức S/R cổ điển. Khi đó **đừng đếm hai lần**: cùng một mức giá vì cùng một lý do là một bằng chứng.

### 13.6 Breaker Block vs Supply / Demand

Trường phái Supply/Demand đánh dấu **vùng nền** (vài nến nhỏ đi ngang) trước một cú chạy mạnh, với lý lẽ “còn lệnh chưa khớp ở đó”. Khi vùng bị phá, một số tác giả cho nó đổi vai (“flip zone”).

| | Supply/Demand | Breaker (ICT) |
|---|---|---|
| Đơn vị | Một cụm nến nền | Một cây nến (hoặc chuỗi cùng màu) |
| Yêu cầu trình tự swing | Không | Có |
| Yêu cầu cực trị cũ bị vi phạm | Không | Có |
| Câu chuyện | Lệnh chưa khớp còn sót | Người bị bẫy ở cả hai phía |

![[BB-v3-30-Breaker-vs-SR-vs-Supply-Demand.svg|960]]
*Hình 30 — Ba ý tưởng cùng nói “thứ từng chặn giờ có thể đỡ”. Breaker là phiên bản hẹp nhất.*

Hẹp hơn không tự động là tốt hơn. Ràng buộc thêm chỉ có giá trị nếu nó thật sự tách được vùng giữ khỏi vùng thủng → [BACKTEST REQUIRED].

---

## 14. Breaker Block + Liquidity

![[BB-v3-31-Hai-Su-Kien-Liquidity.svg|960]]
*Hình 31 — Hai sự kiện liquidity trong một Bullish Breaker.*

### 14.1 Sáu câu hỏi của protocol

**1. Liquidity sweep có bắt buộc trước Breaker không?**
Phải tách hai ý. *Cực trị cũ bị vi phạm* — **có**, theo lời ICT đó là một phần của định nghĩa. *Một cú sweep “đẹp”* (râu dài, lấy một túi lớn, bật lại ngay) — **không**. Cú vi phạm có thể là một nhịp rơi chậm, đóng cửa hẳn dưới đáy cũ nhiều nến liền (một liquidity run), rồi mới đảo chiều.

> [!warning] Chỗ note này không đồng ý với giả định của protocol
> Protocol viết “không mặc định mọi Breaker đều cần liquidity sweep”. Điều đó đúng nếu “sweep” nghĩa là *một cú quét chất lượng cao*. Nhưng nếu hiểu là “không cần cực trị cũ bị vi phạm” thì **trái với lời ICT**: thiếu việc đó, ICT gọi vùng là Mitigation Block. Cách nói chính xác: **vi phạm là điều kiện định nghĩa; chất lượng của cú vi phạm là bộ lọc.** Cộng đồng có một cách dùng lỏng hơn (mọi OB bị phá đều là Breaker)[^lux-bb]; nếu bạn dùng cách đó, hãy ghi rõ để không trộn dữ liệu.

**2. Breaker có nhất thiết xuất hiện sau một liquidity raid không?**
Theo định nghĩa chặt: có một cú vượt cực trị cũ. Cú vượt đó có “raid” được nhiều lệnh hay không thì không ai nhìn thấy.

**3. Liquidity sweep và structural break khác nhau thế nào?**
Sweep: vượt mức rồi quay lại; cấu trúc chưa đổi. Structural break: đóng cửa bên kia và ở lại; cấu trúc đổi (Hình 10). Trong Breaker: cực trị cũ bị *sweep hoặc run*; swing giữa bị *break*.

**4. Liquidity event có vai trò gì trong việc xác nhận Breaker?**
Nó là mắt xích 2 — điều kiện cần. Nó **không** xác nhận gì một mình: phải chờ mắt xích 3.

**5. Có thể có Breaker không có sweep rõ ràng không?**
Có: khi cực trị cũ chỉ là một gợn nhỏ, hoặc chỉ bị vượt một chút (Case D). Đúng chữ, yếu nghĩa. Ghi lại như một điểm yếu, hoặc ghi “mơ hồ (Breaker hoặc Mitigation)”.

**6. Mọi liquidity sweep đều tạo ra Breaker?**
Không.

![[BB-v3-32-Sau-Sweep-Ba-Tuong-Lai.svg|960]]
*Hình 32 — Ba tương lai sau khi đáy cũ thủng. Mười hai nến đầu giống hệt nhau.*

### 14.2 Các loại liquidity và Breaker

| Khái niệm | Quan hệ với Breaker |
|---|---|
| **Sell-side liquidity** (dưới đáy) | Bị lấy ở mắt xích 2 của **Bullish** Breaker. Về sau là thứ nằm dưới mức “ý tưởng sai” |
| **Buy-side liquidity** (trên đỉnh) | Bị lấy ở mắt xích 2 của **Bearish** Breaker. Với Bullish Breaker: là **mục tiêu** phía trên |
| **Equal highs / equal lows** | Nếu cực trị cũ là EQL/EQH thì túi bị lấy dày hơn → câu chuyện rõ hơn [GIẢ THUYẾT]. Nếu EQL nằm *ngay dưới* một Bullish Breaker: giá có thể lao qua vùng để lấy chúng trước |
| **Liquidity run** | Cú vi phạm cực trị cũ kéo dài nhiều nến. Vẫn tính là mắt xích 2 |
| **External liquidity** (đỉnh/đáy của cả dealing range) | Breaker mà mắt xích 2 lấy external liquidity là Breaker của một cú đảo chiều lớn hơn |
| **Internal liquidity** (đỉnh/đáy bên trong range) | Breaker mà mắt xích 2 chỉ lấy internal liquidity thường chỉ là một nhịp điều chỉnh trong range |
| **Inducement** | Các đỉnh/đáy nhỏ hình thành *trong nhịp hồi về Breaker*. Giá có thể lấy chúng — kể cả đâm sâu vào vùng — trước khi phản ứng. Đây là lý do “chạm vùng” chưa phải tín hiệu. Xem [[15-Inducement]] |

Liên kết: [[16-Internal-External-Range-Liquidity-IRL-ERL]].

> [!important] Liquidity Sweep ≠ Breaker Block Formation
> Sweep là **một** sự kiện (mắt xích 2). Breaker là **ba** sự kiện đúng thứ tự. “Giá vừa quét đáy” chỉ mở ra *khả năng* có Breaker; nó không phải Breaker, càng không phải tín hiệu mua.

---

## 15. Breaker Block + MSS / BOS / Displacement

![[BB-v3-33-Formation-Chat-Luong-Entry.svg|960]]
*Hình 33 — Ba ngăn kéo: điều kiện hình thành · bằng chứng chất lượng · tín hiệu vào lệnh.*

### 15.1 Market Structure Shift

- **MSS có cần thiết không?** Có — nhưng không phải như một điều kiện *thêm*. Cú phá swing giữa **chính là** MSS trên khung của Breaker. ICT dùng đúng chữ “market structure shift” khi tả cú phá này.
- **MSS xảy ra trước hay sau khi OB thất bại?** Cùng lúc. Vì OB nằm tại swing giữa, thân nến đóng qua swing giữa vừa làm OB thất bại vừa tạo MSS. (Ngoại lệ nhỏ: nếu râu của swing cao hơn cây nến OB, có thể có một nến đóng cửa *trên thân OB nhưng dưới đỉnh giữa* — lúc đó OB đang bị thử, MSS chưa có; Hình 16 C.)
- **MSS nào có ý nghĩa?** MSS phá **swing chứa cây nến Breaker**. Một MSS phá một gợn nhỏ nào đó bên dưới không tính.
- **Internal MSS có đủ không?** Đủ để *gọi tên* một Breaker trên khung đó. Chưa đủ để coi nó *quan trọng*: Breaker phá một gợn nội bộ trong một nhịp giảm lớn là chuyện khác hẳn Breaker phá đỉnh được bảo vệ của cả cấu trúc (§20, câu 2).
- **Swing nào cần bị phá?** Swing giữa: swing high gần nhất có trước khi đáy cũ bị vi phạm (Bullish); swing low gần nhất có trước khi đỉnh cũ bị vi phạm (Bearish).

### 15.2 BOS

- **BOS và MSS khác nhau thế nào ở đây?** Cùng một cú phá có thể mang hai tên tuỳ bạn so với xu hướng nào. So với nhịp vừa tạo cực trị mới → nó ngược hướng → **MSS**. Nếu khung lớn vốn đang tăng và cả trình tự chỉ là một nhịp hồi quét đáy → trên khung lớn, cú phá là sự **tiếp diễn**; cú vượt đỉnh lớn kế tiếp mới là BOS.
- **Mọi BOS đều xác nhận Breaker?** Không. Một BOS trong xu hướng đang chạy, không có cực trị cũ bị vi phạm phía ngược lại, ứng với trình tự của Mitigation Block.

### 15.3 Displacement

![[BB-v3-34-Pha-Manh-vs-Pha-Yeu.svg|960]]
*Hình 34 — Cùng “đóng nến trên đỉnh giữa”, hai cú phá rất khác nhau.*

- **Vai trò:** mô tả *cách* swing giữa bị phá — nhanh, thân dài, ít do dự. Trẻ con: xô cửa xông vào, khác với rón rén lách qua khe.
- **Xác nhận điều gì?** [QUAN SÁT] Rằng trong quãng đó lượng mua chủ động áp đảo lượng bán chờ. [DIỄN GIẢI] Rằng có “người lớn” tham gia.
- **Có Breaker không có displacement rõ không?** Có (Hình 34 phải). Đủ định nghĩa; note xếp là “chất lượng thấp?” — có dấu hỏi vì đây là [GIẢ THUYẾT].
- **Displacement có cần tạo FVG không?** Không bắt buộc. Displacement mạnh *thường* để lại FVG, nên hai thứ hay đi cùng; nhưng có cú phá mạnh bằng nhiều nến chồng nhau, không để lại khoảng trống nào.

Chi tiết: [[50-Displacement-In-Depth]].

### 15.4 FVG

- **Có phải điều kiện bắt buộc?** Không. Bài giảng Breaker của ICT không nhắc tới.
- **FVG nằm trong hoặc gần Breaker có ý nghĩa gì?** Nó cho biết nhịp phá có displacement. Nếu chồng lên Breaker, cộng đồng gọi là “Unicorn” (§16).
- **Vai khác nhau thế nào?** Breaker là một cây nến **cũ** (có trước cú phá), nói về *chỗ cấu trúc đổi*. FVG là dấu vết **của chính cú phá**, nói về *tốc độ*. Một cái là địa điểm, một cái là dấu chân.

### 15.5 Tóm tắt: hình thành · bằng chứng · tín hiệu vào lệnh

| Yếu tố | Điều kiện hình thành | Bằng chứng chất lượng | Tín hiệu vào lệnh |
|---|---|---|---|
| Nến tại swing giữa | ✓ | | |
| Cực trị cũ bị vi phạm | ✓ | (túi lớn hay nhỏ) | |
| Swing giữa bị phá = MSS khung Breaker | ✓ | (bằng thân nến) | |
| Displacement ở cú phá | | ✓ | |
| FVG ở cú phá | | ✓ | |
| BOS kế tiếp theo hướng mới | | ✓ | |
| Giá quay lại vùng | | | điều kiện cần |
| Sweep + MSS + displacement + FVG **trên khung nhỏ** | | | ✓ |

---

## 16. Breaker Block + FVG / Other PD Arrays

### 16.1 Breaker + FVG

![[BB-v3-35-Breaker-va-FVG-Unicorn.svg|960]]
*Hình 35 — FVG chồng lên Breaker (“Unicorn”) và FVG nằm riêng.*

- **Vai:** Breaker = chỗ cấu trúc đổi. FVG = khoảng trống của nhịp phá.
- **Vùng này có xác nhận vùng kia không?** FVG xác nhận rằng cú phá có displacement. Nó **không** phải bằng chứng độc lập rằng Breaker sẽ giữ: cả hai sinh ra từ cùng một nhịp.
- **Có thể chồng lên nhau?** Có — khi cây nến phá đi xuyên qua vùng Breaker bằng một thân dài. Phần chung là vùng “Unicorn” ([[07 - Unicorn Model]]). Một thư viện thuật ngữ nói gọn: nếu không chồng nhau, bạn có hai ý tưởng riêng[^lux-uni].
- **Nếu hai vùng cho tín hiệu khác nhau?** Ví dụ Breaker thủng nhưng FVG bên dưới giữ: ý tưởng tăng chưa sai, vùng Breaker thì sai. Ghi riêng từng vùng.
- **Ưu tiên vùng nào?** Không có câu trả lời chung. Vùng nông cho vào sớm, mức dừng xa; vùng sâu cho mức dừng gần, hay lỡ lệnh.
- **Confluence hay requirement?** Confluence.

### 16.2 Các tổ hợp khác

![[BB-v3-36-Breaker-Giua-Cac-PD-Array.svg|960]]
*Hình 36 — Một nhịp tăng, bốn vùng xếp từ nông tới sâu.*

| Tổ hợp | Hai vùng có vai gì | Chồng được không | Khi “nói” khác nhau | Requirement hay confluence |
|---|---|---|---|---|
| **Breaker + Order Block** | Breaker ở đỉnh giữa (nông); OB mới ở cực trị mới (sâu) | Hiếm, chỉ khi nhịp rất ngắn | Breaker thủng, OB giữ → vùng sai, ý tưởng còn | Confluence. Là hai mức sâu của cùng một nhịp |
| **Breaker + Mitigation Block** | Không thể là cùng một swing (hoặc cái này hoặc cái kia). Có thể lồng khác khung: Breaker H1 nằm trong Mitigation Block H4 | Khác khung thì được | Khung lớn quyết định hướng | Confluence đa khung |
| **Breaker + Rejection Block** | Rejection Block là râu của cực trị mới — sâu nhất | Không | Giá xuống tới Rejection Block nghĩa là Breaker đã thủng từ lâu | Confluence |
| **Breaker + BPR** | BPR là phần chồng của hai FVG ngược chiều, sinh ra khi nhịp rơi và nhịp phá đều đi nhanh qua cùng một dải | Có, khi cả nhịp rơi lẫn nhịp phá đều có FVG quanh vùng | Như với FVG | Confluence. Xem [[03-Balanced-Price-Range]] |
| **Breaker + Liquidity pool** | Túi lệnh **phía trước** (trên, với Bullish) là mục tiêu. Túi lệnh **ngay sau lưng** vùng (EQL sát dưới) là mối nguy | — | Có EQL sát dưới Breaker: giá có thể đi qua vùng để lấy chúng | Bối cảnh, không phải requirement |

> [!warning] Nhiều vùng chồng nhau ≠ xác suất cao hơn
> Breaker, FVG, Order Block, Rejection Block của **cùng một nhịp** là bốn cách mô tả một sự kiện. Chúng không phải bốn phiếu bầu độc lập. Bằng chứng độc lập thật sự đến từ nguồn khác: hướng khung lớn, vị trí trong dealing range, phiên giao dịch, và thứ khung nhỏ cho thấy lúc retest. “Càng nhiều PD array càng tốt” là [GIẢ THUYẾT] → [BACKTEST REQUIRED].

---

## 17. Breaker Block + Premium / Discount / Dealing Range

> **Breaker là một khái niệm về cấu trúc và hành vi giá. Premium/Discount chỉ cho biết VỊ TRÍ.**

![[BB-v3-37-Breaker-Premium-Discount.svg|960]]
*Hình 37 — Breaker ở nửa trên hay nửa dưới tuỳ bạn đo bằng khoảng giá nào.*

**Nền tối thiểu.** Dealing range là khoảng giữa một đáy và một đỉnh quan trọng. Nửa trên là **premium** (đắt), nửa dưới là **discount** (rẻ), giữa là **equilibrium**. Chi tiết: [[12-Dealing-Range]], [[27-Premium-Discount]].

### 17.1 Sáu vị trí

| Vị trí của Breaker | Đọc thế nào |
|---|---|
| **Bullish Breaker trong discount** (của range lớn) | Vị trí thuận: mua ở nửa rẻ, còn nhiều chỗ chạy lên |
| **Bullish Breaker trong premium** | Vẫn là Breaker. Nhưng mua ở nửa đắt: chỗ chạy còn ít, mức dừng tương đối xa |
| **Tại equilibrium** | Trung tính. Giá hay lình xình quanh giữa range → dễ gặp tình huống “đóng cửa trong vùng, chưa rõ” |
| **Ở ranh giới dealing range** | Thường là Breaker của một cú đảo chiều: mắt xích 2 đã lấy external liquidity. Câu chuyện rõ nhất — cũng là nơi dễ nhầm với một cú phá thật ra ngoài range |
| **Trong internal range** | Mắt xích 2 chỉ lấy internal liquidity. Breaker “nội bộ”, hay là một nhịp điều chỉnh |
| **Gắn với external range** | Breaker hình thành sau khi đỉnh/đáy của cả range bị lấy. Quan trọng hơn về cấu trúc |

### 17.2 Năm câu hỏi của protocol

1. **Dealing range có xác định Breaker không?** Không. Breaker được xác định bằng ba swing cục bộ. Dealing range chỉ cho biết ba swing ấy nằm ở đâu trong bức tranh lớn.
2. **Breaker có tồn tại độc lập với dealing range không?** Về định nghĩa: có. Về giá trị sử dụng: gần như không — một Breaker không biết mình ở đâu trong range thì không biết còn bao nhiêu chỗ chạy.
3. **Premium/Discount có giúp đánh giá vị trí không?** Có, và đó là việc duy nhất nó làm ở đây.
4. **Bullish Breaker trong premium có bị loại không?** Không bị loại khỏi định nghĩa. Bị **hạ ưu tiên** vì khoảng chạy còn lại. Và phải hỏi: premium của range *nào*? (Hình 37 C: premium của nhịp H1 có thể là discount của range D1.)
5. **Bearish Breaker trong discount có bị loại không?** Tương tự: không loại, hạ ưu tiên.

“Mua ở discount, bán ở premium” là một gợi ý về vị trí, **không phải luật**. Trong một xu hướng mạnh, giá có thể không bao giờ hồi về discount; đòi discount tuyệt đối là tự loại mình khỏi cả xu hướng.

**Một hệ quả hình học đáng nhớ:** Bullish Breaker luôn nằm tại đỉnh giữa — tức là ở *phần trên* của nhịp rơi vừa qua. Nó nằm ở premium hay discount của nhịp **tăng mới** tuỳ vào việc cú phá đi được bao xa (Hình 37 A và B). Cú phá càng xa, Breaker càng nằm sâu trong discount của nhịp mới.

---

## 18. Breaker Block Lifecycle

![[BB-v3-38-Vong-Doi-Breaker.svg|960]]
*Hình 38 — Năm trạng thái, ba lối ra giữa đường, ba kết cục.*

### 18.1 Sáu câu hỏi về vòng đời

| Câu hỏi | Trả lời |
|---|---|
| Khi nào vùng mới chỉ là **candidate**? | Từ lúc cực trị cũ bị vi phạm cho tới trước khi có thân nến đóng qua swing giữa. Rất nhiều ứng viên không bao giờ được xác nhận |
| Khi nào là **confirmed** Breaker? | Từ lúc nến phá swing giữa **đóng cửa**. Lúc này khoá biên vùng |
| Khi nào vùng trở nên **relevant**? | Khi (a) nó thuận bối cảnh khung lớn, (b) giá đang quay về gần nó, và (c) mục tiêu phía trước còn nguyên |
| Khi nào vùng trở nên **stale** (cũ)? | Giá đã đi quá xa và lâu; hoặc vùng đã bị chạm vài lần; hoặc mục tiêu mà nó phục vụ đã đạt; hoặc một cấu trúc ngược đã hình thành phía trên trước khi giá quay lại |
| Khi nào vùng bị **invalidated**? | Thân nến đóng qua **mép xa** và giá ở lại bên kia (không bị kéo về trong vài nến sau). Một cái râu qua mép xa là cú quét, chưa phải vô hiệu |
| Khi nào **không nên dùng tiếp**? | Khi vô hiệu, khi cũ, hoặc khi bối cảnh khung lớn đã đổi hướng |

Quy ước “đóng cửa và ở lại” là quy tắc làm việc của bạn (đã dùng nhất quán trong vault), không phải lời ICT.

### 18.2 Bốn sự kiện tách biệt

![[BB-v3-39-Bon-Su-Kien-Tach-Biet.svg|960]]
*Hình 39 — Hình thành ≠ xác nhận ≠ retest ≠ vào lệnh.*

| Sự kiện | Trên chart | Việc được làm | Việc CHƯA được làm |
|---|---|---|---|
| **1 · Formation** (ứng viên) | Cực trị cũ vừa bị vi phạm | Ghi chú; đánh dấu mức swing giữa cần bị phá | Vẽ vùng Breaker; lên kế hoạch lệnh |
| **2 · Confirmation** | Thân nến đóng qua swing giữa | Vẽ vùng, khoá biên; ghi mục tiêu và điều kiện hết hạn; đặt cảnh báo | Vào lệnh |
| **3 · Retest** | Giá chạm vùng | Xuống khung nhỏ quan sát | Vào lệnh chỉ vì chạm |
| **4 · Trade entry** | Khung nhỏ cho chuỗi tín hiệu | Vào lệnh theo kế hoạch | — |

Giữa các mốc có thể **không có gì xảy ra**: ứng viên không được xác nhận; Breaker không được retest; retest không cho tín hiệu. Cả ba đều bình thường và đều phải được ghi.

---

## 19. Valid vs Invalid Breaker

Bốn nhãn dùng trong mục này: **Hợp lệ** (đủ ba mắt xích, chưa bị vô hiệu) · **Tiềm năng** (ứng viên; hoặc đang bị thử) · **Thất bại** (đã hợp lệ rồi bị đóng nến qua mép xa) · **Không phải Breaker** (thiếu mắt xích).

![[BB-v3-40-Muoi-Hai-Tinh-Huong.svg|960]]
*Hình 40 — Mười hai tình huống, ví dụ phía mua.*

| # | Chuỗi giá | Điều kiện cấu trúc | Phân loại | Nghĩa là gì | Điều gì làm nó vô hiệu / đổi nhãn |
|---|---|---|---|---|---|
| 1 | OB bị nến đóng xuyên, nhưng swing gốc của nhịp còn nguyên | Không có MSS | **Không phải Breaker** (OB vô hiệu) | Vùng mất vai cũ, không có vai mới | Nếu về sau swing gốc bị phá *và* cực trị cũ đã bị vi phạm → xét lại từ đầu |
| 2 | OB tại swing giữa bị đóng xuyên; cực trị cũ đã bị vi phạm trước đó | MSS trên khung đó | **Hợp lệ** (đã xác nhận) | Vùng được theo dõi với vai ngược | Thân nến đóng qua mép xa và ở lại |
| 3 | Như #2 nhưng cú phá chậm, nến nhỏ chồng nhau | MSS có, không displacement | **Hợp lệ** — chất lượng thấp? [GIẢ THUYẾT] | Đủ tên, thiếu sức | Giá quay lại dưới swing giữa và ở lại |
| 4 | Như #2, phá mạnh, giá đi thẳng không quay lại | MSS + displacement | **Hợp lệ → Hết hạn** | Không có cơ hội vào; không phải lỗi | Hết hạn khi mục tiêu đạt |
| 5 | Giá quay lại và đi xuyên thẳng qua vùng | Cấu trúc mới bị thách thức | **Thất bại** | Vai mới không giữ | — (đã vô hiệu) |
| 6 | Chỉ râu nến chạm vào vùng rồi giá đi tiếp | Cấu trúc mới giữ | **Hợp lệ** — retest nông | Có thể đã lỡ lệnh; không sao | Lần sau thân nến đóng qua mép xa |
| 7 | Nến đóng cửa **bên trong** vùng | Chưa rõ | **Tiềm năng** — đang bị thử | Không kết luận được. Chờ nến sau | Đóng qua mép xa → thất bại; đóng trở ra phía gần → còn hợp lệ |
| 8 | Nến đóng cửa **xuyên qua** mép xa | Cấu trúc mới có thể đã gãy | **Thất bại** (nếu giá ở lại) | Bỏ vùng | Nếu ngay nến sau giá bị kéo về trong vùng: đó là cú quét — xét lại theo quy ước “ở lại” |
| 9 | Vùng được chạm nhiều lần, lần nào cũng giữ | Đi ngang trên vùng | **Hợp lệ** — đang cũ dần? [GIẢ THUYẾT] | Hai niềm tin trái ngược (§12.1). Chưa biết bên nào đúng với dữ liệu của bạn | Thân nến đóng qua mép xa |
| 10 | Trước khi quay về vùng, giá đã tạo một MSS **ngược** ở phía trên | Cấu trúc đã đổi lần nữa | **Cần đánh giá lại** | Giá đang về vùng trong một nhịp giảm mới, không phải một nhịp hồi | Coi như bối cảnh đã đổi: hạ ưu tiên hoặc bỏ |
| 11 | Retest, bật yếu một hai nến, rồi đóng xuyên | MSS khung nhỏ không xuất hiện | **Thất bại** | “Phản ứng” không đồng nghĩa “giữ” | — |
| 12 | Trình tự xảy ra bên trong một vùng đi ngang | Không có xu hướng; swing đều là gợn nhỏ | **Hợp lệ theo chữ → bỏ qua** | Nhiễu | Chỉ xét lại khi giá rời vùng đi ngang |

**Khi dữ kiện chưa đủ, không kết luận.** Ba trường hợp nên ghi “CHƯA RÕ” thay vì ép nhãn: (a) cực trị cũ chỉ bị vượt một chút xíu; (b) không xác định được nến nào là nến ngược màu cuối cùng tại swing (nhiều nến nhỏ lẫn lộn); (c) nến phá đóng cửa gần như đúng tại mức swing.

---

## 20. Breaker Block Selection

Một chart luôn đầy vùng đã thất bại. Không dùng thang điểm. Dùng năm câu hỏi theo thứ tự.

![[BB-v3-41-Khung-Chon-Breaker.svg|960]]
*Hình 41 — Năm câu hỏi. Trả lời “không” ở đâu thì dừng hoặc hạ ưu tiên ở đó.*

### 20.1 Vì sao là năm câu này

| Câu hỏi | Gộp các yếu tố nào của protocol | Vì sao đứng ở vị trí này |
|---|---|---|
| 1. Cùng hướng khung lớn? | HTF structure, quan hệ với DOL | Sai ở đây thì mọi thứ phía sau vô nghĩa |
| 2. Swing bị phá có quan trọng? | Structural swing, timeframe | Quyết định Breaker “thuộc cấp nào” |
| 3. Trước cú phá có lấy túi liquidity đáng kể? | Liquidity context, chất lượng OB gốc | Phân biệt cú đảo chiều có câu chuyện với một gợn sóng |
| 4. Cú phá có dứt khoát? | Displacement, FVG | Chất lượng của chính sự kiện tạo ra Breaker |
| 5. Còn mới, còn chỗ chạy? | Freshness, số lần retest, vị trí trong dealing range | Kiểm tra cuối: có đáng đặt cảnh báo không |

### 20.2 Sáu câu hỏi của protocol

1. **Breaker nào đáng ưu tiên?** Cái qua được cả năm câu. Nếu phải chọn giữa hai cái: ưu tiên cái thuận khung lớn hơn; rồi tới cái phá swing quan trọng hơn.
2. **Có nên ưu tiên Breaker gần external liquidity không?** Tách hai nghĩa. Breaker mà *mắt xích 2 đã lấy* external liquidity: có, câu chuyện rõ hơn [GIẢ THUYẾT]. Breaker có external liquidity *chưa bị lấy nằm ngay sau lưng* (ví dụ đáy lớn ngay dưới một Bullish Breaker): thận trọng — giá có thể đi qua vùng để lấy nó.
3. **Breaker H1 có quan trọng hơn Breaker M5 không?** Về cấu trúc: có — nó phá một swing lớn hơn và cần nhiều lệnh hơn để bị thủng. Nhưng “quan trọng hơn” không có nghĩa “dễ giao dịch hơn”: vùng H1 rộng, mức dừng xa. Trong khung làm việc này hai thứ có vai khác nhau: H1 = vị trí, M5 = thời điểm.
4. **Khi nhiều Breaker cùng tồn tại?** (a) Bỏ hết cái ngược khung lớn. (b) Trong số còn lại, lấy cái của khung **setup** (H1). (c) Nếu vẫn còn hai cái H1 cùng hướng: cái gần giá là nơi sẽ được thử trước; cái xa hơn là phương án dự phòng. Lưu ý từ một mẫu thật trong vault: vùng nông có thể chỉ là liquidity để giá đi tới vùng sâu (§26.9).
5. **Breaker hợp lệ có nhất thiết tradeable?** Không. Hợp lệ là chuyện tên gọi. Tradeable cần thêm: bối cảnh, retest, tín hiệu khung nhỏ, và khoảng chạy đủ lớn so với mức dừng.
6. **Khi nào bỏ qua?** Xem §20.3.

### 20.3 Danh sách bỏ qua

- Ngược bias D1 mà không có playbook riêng cho việc đó.
- Swing bị phá là gợn nhỏ bên trong một nhịp lớn ngược hướng.
- Nằm giữa vùng đi ngang (Case F).
- Đã bị chạm nhiều lần, hoặc đã bị thân nến đóng xuyên.
- Mục tiêu (DOL) đã đạt trước khi giá quay về.
- Trước khi quay về, giá đã tạo MSS ngược ở phía trên (tình huống 10).
- Khoảng từ vùng tới mục tiêu quá ngắn so với khoảng từ vùng tới mức dừng.
- Giá quay về vào lúc có tin lớn hoặc ngoài khung giờ bạn giao dịch ([[18-Kill-Zones]]).
- Bạn không chỉ ra được cây nến nào là nến gốc — tức vùng được vẽ “theo cảm giác”.

Toàn bộ khung chọn này là **[GIẢ THUYẾT]**: hợp lý, nhất quán với ICT 2022 Model, nhưng chưa được kiểm chứng trên dữ liệu của bạn.

---

## 21. Breaker in Different Market Conditions

![[BB-v3-42-Sau-Boi-Canh-Thi-Truong.svg|960]]
*Hình 42 — Cùng một hình Breaker, sáu bối cảnh.*

| Bối cảnh | Chuỗi giá | Cấu trúc | Phân loại | Kỳ vọng theo ICT | Cách đọc khác | Điều kiện thất bại |
|---|---|---|---|---|---|---|
| **A · Xu hướng tăng** | Nhịp hồi quét một đáy cao hơn, rồi phá đỉnh giữa | Khung lớn: HH/HL. Khung nhỏ: MSS tăng | Bullish Breaker **thuận** xu hướng | Giá hồi về vùng rồi đi tiếp lên đỉnh mới | Chỉ là “mua khi điều chỉnh” thông thường; Breaker không thêm gì ngoài một mức cụ thể | Giá đóng cửa dưới đáy vừa quét → nhịp hồi đã thành đảo chiều |
| **B · Xu hướng giảm** | Nhịp hồi quét một đỉnh thấp hơn, rồi phá đáy giữa | Khung lớn: LH/LL | Bearish Breaker **thuận** xu hướng | Giá hồi lên vùng rồi rơi tiếp | Như trên, ảnh gương | Giá đóng cửa trên đỉnh vừa quét |
| **C · Đi ngang** | Đỉnh/đáy nhỏ bị quét và phá qua lại | Không có xu hướng | Nhiều “Breaker” theo chữ | (ICT thường khuyên tránh vùng đi ngang) | Đây chỉ là dao động quanh một mức giá cân bằng | Gần như lần nào cũng thủng sau vài nến |
| **D · Đảo chiều xu hướng** | Cuối xu hướng giảm: đáy cuối bị quét, đỉnh thấp hơn gần nhất bị phá | MSS **ngược** xu hướng cũ | Bullish Breaker đầu tiên của xu hướng mới — *nếu* đúng là xu hướng mới | Điểm vào sớm nhất của xu hướng mới | Có thể chỉ là một nhịp hồi sâu trong xu hướng giảm | Giá lập đáy thấp hơn đáy vừa quét |
| **E · Sau một cú phá giả** | Giá vượt đỉnh vùng rồi rơi lại, phá đáy giữa | Cú vượt đỉnh hoá ra là sweep | **Bearish** Breaker | Phá giả phía trên = mắt xích 2 của Breaker phía dưới | TA cổ điển gọi là “bull trap” | Giá quay lên đóng cửa trên đỉnh vừa quét → cú phá hoá ra là thật |
| **F · Chỉ có sweep** | Đáy cũ bị quét, giá bật lên nhưng không vượt đỉnh giữa | Chưa có MSS | **Không có Breaker** | — | Một cú quét trong xu hướng giảm đang tiếp diễn | — |

**Phản ví dụ chống nhận diện máy móc:**
- Một **false breakout** tự nó không phải Breaker. Nó chỉ là mắt xích 2. Phải chờ mắt xích 3 ở phía ngược lại (E).
- Một **liquidity sweep** tự nó không phải Breaker (F).
- Trong xu hướng mạnh, mỗi nhịp hồi nông tạo ra trình tự của **Mitigation Block** (không quét đáy cao hơn), không phải Breaker. Gọi tất cả là Breaker sẽ làm hỏng thống kê của bạn.
- Ở D, tại thời điểm thật **không thể biết** đó là đảo chiều hay nhịp hồi sâu. Thứ duy nhất giúp là khung lớn hơn nữa.

---

## 22. D1 → H1 → M5 Application

**D1 = BỐI CẢNH · H1 = SETUP · M5 = THỰC THI.** Liên kết: [[01 - ICT 2022 Model]], [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]], [[32-Top-down-Analysis-Multiple-Timeframes]].

![[BB-v3-43-D1-H1-M5-Long-Nhau.svg|960]]
*Hình 43 — Ba khung, ba câu hỏi. Mỗi khung là một lần phóng to vào khung trước.*

### 22.1 Bảy câu hỏi cốt lõi

**1. Breaker trên D1 có vai gì?** Là một **vùng bối cảnh** (HTF POI): chỗ đáng chờ giá quay về, nếu nó thuận với bias và DOL. Nó quá rộng để vào lệnh trực tiếp. Nó trả lời “chờ ở đâu”, không trả lời “vào lúc nào”.

**2. Breaker H1 refine bối cảnh D1 thế nào?** Khi giá đã vào vùng D1 (một OB, FVG hay Breaker D1), H1 cho biết *bên trong vùng đó* cấu trúc có đổi theo hướng D1 không. Một Bullish Breaker H1 hình thành trong vùng mua D1 nghĩa là: giá đã quét một đáy H1 và đã phá một đỉnh H1 — bằng chứng đầu tiên rằng vùng D1 đang được tôn trọng.

**3. Khi nào Breaker H1 được dùng làm setup POI?** Khi đủ ba điều: (a) cùng hướng bias D1; (b) nằm trong hoặc ngay cạnh vùng D1 đang chờ; (c) phía trước còn mục tiêu (DOL) chưa bị lấy.

**4. Khi nào Breaker M5 có nghĩa?** Chỉ khi nó xuất hiện **tại** POI H1 và **cùng hướng** D1/H1. Khi đó nó là một trong các dạng tín hiệu thực thi (bên cạnh FVG M5). Một Breaker M5 giữa hư không chỉ là một gợn.

**5. Breaker M5 có thể chống lại bối cảnh D1 không?** Nó *sẽ* xuất hiện ngược D1 rất thường xuyên — mỗi nhịp hồi của D1 đều chứa vài cái. Trong khung này, **không giao dịch chúng**. M5 không có quyền tạo bối cảnh.

**6. Khi Breaker D1 và H1 chỉ hai hướng khác nhau?**

![[BB-v3-46-Xung-Dot-D1-H1.svg|960]]
*Hình 46 — D1 đang hướng lên trong cả hai hình.*

Khung lớn quyết định hướng. Bearish Breaker H1 giữa xu hướng tăng D1 thường chỉ là *cách nhịp hồi của D1 diễn ra*. Không bán theo nó. Nó có ích theo cách khác: khi Bearish Breaker H1 đó bị giá đóng cửa xuyên lên, đó là dấu hiệu nhịp hồi đã xong. Nếu mâu thuẫn kéo dài (H1 liên tục tạo cấu trúc giảm sâu vào vùng D1), câu hỏi đúng không phải “theo ai” mà là “bias D1 của mình còn đúng không?” — xem [[59-Daily-Bias]].

**7. Có nên dùng Breaker như tín hiệu vào lệnh độc lập?** Không. Breaker = vị trí. Lệnh cần thêm bối cảnh (phía trên) và bằng chứng (phía dưới).

### 22.2 Ví dụ hoàn chỉnh theo ICT 2022 Model

![[BB-v3-44-ICT-2022-Vi-Du-Day-Du.svg|960]]
*Hình 44 — Một ví dụ mua trên M5 tại Breaker H1. Khung ví dụ, không phải trình tự bắt buộc.*

| Bước | Câu hỏi của protocol | Trả lời |
|---|---|---|
| D1 hướng và vùng chờ | Vì sao D1 phải phân tích trước? | Vì D1 cho biết giá *đang đi đâu* (DOL) và *đang ở đâu* (premium/discount). Không có hai thứ đó, một Breaker H1 chỉ là một hình vẽ không có hướng |
| H1 cấu trúc → Breaker H1 | Vì sao Breaker H1 cần bối cảnh cấu trúc? | Vì cùng một hình Breaker có sáu ý nghĩa khác nhau (§21). Chỉ bối cảnh mới nói đó là A (thuận) hay C (nhiễu) |
| Giá tới Breaker H1 | Vì sao không vào chỉ vì giá chạm? | Vì chạm chỉ là “đến nơi”. Tại lúc chạm, hai kết cục *giữ* và *thủng* còn mở (Hình 27). Giá còn có thể đâm sâu để lấy các đáy nhỏ (inducement) |
| M5 sweep → M5 MSS | MSS xác nhận điều gì? | Rằng trên khung nhỏ, phe mua vừa thắng một trận *tại đúng vùng này*. Đây là bằng chứng đầu tiên, không phải bảo đảm |
| Displacement | Displacement xác nhận điều gì? | Rằng cú thắng đó dứt khoát. MSS không có displacement là lỗi đã có tên trong vault: [[08-Mistake-Weak-Displacement]] |
| FVG | FVG đóng vai gì? | Cho một chỗ **cụ thể** để vào lệnh khi giá hồi, thay vì mua đuổi |
| Stop loss | Dựa trên điều kiện vô hiệu nào? | Xem §22.3 |
| Target | Xác định bằng liquidity thế nào? | Mục tiêu gần: đỉnh M5/H1 gần nhất chưa bị lấy. Mục tiêu xa: DOL của D1. Nếu khoảng tới mục tiêu gần đã không đủ so với mức dừng → bỏ lệnh ([[05-Mistake-Not-enough-RR]]) |

> **Breaker Block = Potential POI / Location.** Nó **không** phải Automatic Entry Signal.

Chuỗi trên là khung của ICT 2022 Model áp lên một Breaker. Không phải setup nào cũng có đủ mọi bước theo đúng thứ tự (ví dụ M5 có thể không quét thêm đáy nào trước khi MSS). Thứ không được thiếu trong khung của bạn: **bối cảnh D1 + vị trí H1 + một bằng chứng cấu trúc trên M5**.

### 22.3 Mức dừng lỗ: ba mức “sai” khác nhau

![[BB-v3-45-Ba-Muc-Sai.svg|960]]
*Hình 45 — Setup sai, vùng sai, ý tưởng sai.*

| Mức | Nằm ở đâu (lệnh mua) | Câu hỏi nó trả lời | Đánh đổi |
|---|---|---|---|
| **Setup sai** | Dưới đáy M5 vừa bị quét | “Chuỗi vào lệnh của tôi còn đúng không?” | Gần → mất ít khi sai; dễ bị một cú quét nữa lấy mất |
| **Vùng sai** | Dưới mép xa của Breaker H1 | “Breaker này còn giữ không?” | Vừa phải |
| **Ý tưởng sai** | Dưới đáy mới (đáy quét của H1) | “Câu chuyện đảo chiều còn đúng không?” | Xa → khó bị quét; mất nhiều khi sai, và khoảng chạy tương đối nhỏ lại |

ICT không nêu nơi đặt stop trong bài giảng Breaker. Chọn mức nào là quyết định của bạn, phải có **trước** khi vào lệnh, và khối lượng phải được tính sao cho rủi ro không vượt quy tắc ≤ 0,5% mỗi lệnh.

---

## 23. Common Mistakes

![[BB-v3-47-Sau-Loi-Nhin-Thay-Duoc.svg|960]]
*Hình 47 — Sáu lỗi nhìn thấy được ngay trên chart.*

| # | Lỗi | Vì sao xảy ra | Vì sao sai | Cách nghĩ đúng | Cách phòng |
|---|---|---|---|---|---|
| 1 | Gọi mọi Failed OB là Breaker | Câu định nghĩa một dòng “Breaker = OB thất bại” | Bỏ qua vị trí tại swing và việc cực trị cũ bị vi phạm | Failed OB rộng, Breaker hẹp (§10) | Hỏi đủ ba câu của §3 trước khi gọi tên |
| 2 | Gọi mọi hỗ trợ bị phá là **Bearish** Breaker | Lẫn với “hỗ trợ thành kháng cự” | Thiếu cây nến tại swing, thiếu đỉnh cũ bị vi phạm | Đó là S/R đổi vai, một ý tưởng rộng hơn (§13.5) | Chỉ ra được cây nến gốc và cực trị cũ thì mới gọi |
| 3 | Gọi mọi kháng cự bị phá là **Bullish** Breaker | Như trên | Như trên | Như trên | Như trên |
| 4 | Không xác định structural break | Nhìn vùng trước, nhìn cấu trúc sau | Không có cú phá swing giữa thì OB vẫn sống | Mắt xích 3 là thứ tạo ra cái tên | Kẻ mức swing giữa trước; chờ nến đóng cửa qua |
| 5 | Nhầm liquidity sweep với structural break | Cả hai đều “vượt qua một mức” | Sweep không đổi cấu trúc | Râu qua rồi về = sweep; đóng cửa và ở lại = break | Quy tắc “thân nến đóng cửa” |
| 6 | Nhầm BOS với MSS | Hai tên cho cùng động tác “phá” | Dẫn tới đọc sai hướng bối cảnh | Hỏi: cú phá này thuận hay ngược nhịp trước nó? | Ghi rõ đang so với xu hướng của khung nào |
| 7 | Xác định Breaker bằng hindsight | Lật chart cũ, mọi thứ đã xong | Chọn lọc những lần đã chạy | Tại mỗi nến, hỏi “lúc đó mình biết gì?” | Dùng chế độ replay; ghi giờ vẽ vùng |
| 8 | Chọn sai cây nến | Nhiều nguồn dạy khác nhau | Đổi vị trí vào và mức dừng | Một quy ước, ghi tên (§5.5) | Ghi `cách A` hay `cách B` trong nhật ký |
| 9 | Vẽ vùng quá rộng | Sợ lỡ; “lấy cả cụm cho chắc” | Vùng rộng thì gần như lúc nào cũng “được chạm” — vô nghĩa | Một cây nến, hoặc chuỗi cùng màu liền nhau | Nếu vùng rộng hơn hẳn các nến xung quanh → xem lại |
| 10 | Vẽ vùng quá hẹp | Muốn mức dừng thật gần | Giá phản ứng ngay ngoài vùng → “lỡ” hoặc bị quét | Lấy cả râu theo lời ICT, trừ khi có lý do ghi rõ | Không thu hẹp vùng sau khi đã khoá |
| 11 | Coi râu và thân như nhau không có lý do | Không nghĩ tới | Hai cách cho hai vùng khác nhau | Chọn một, ghi lại, giữ nguyên trong cả bộ mẫu | Một dòng trong template: `biên = cả râu / chỉ thân` |
| 12 | Vào lệnh ngay khi giá chạm | Nóng vội; nhầm vị trí với tín hiệu | Lúc chạm, *giữ* và *thủng* còn mở ngang nhau | Chạm = đến nơi | Bắt buộc có MSS khung nhỏ trước khi vào ([[06-Mistake-Not-Have-Market-Structure-Shift]]) |
| 13 | Bỏ qua bối cảnh khung lớn | Chỉ mở một khung | Breaker ngược khung lớn thường là nhịp hồi | D1 trước, H1 sau, M5 cuối | Không mở M5 trước khi viết xong bias D1 ([[09-Mistake-Wrong-daily-bias]]) |
| 14 | Không quan tâm DOL | Chỉ nhìn điểm vào | Không biết đi đâu thì không biết còn chỗ chạy không | Mục tiêu có trước, điểm vào có sau | Ghi DOL trước khi đặt cảnh báo ([[13-Mistake-Trading-Into-Unswept-Liquidity]]) |
| 15 | Coi FVG là điều kiện bắt buộc | Hay thấy chúng đi cùng nhau | ICT không nêu; loại bỏ oan nhiều mẫu | FVG là bằng chứng chất lượng | Ghi “có/không FVG” thành một cột, không thành bộ lọc cứng |
| 16 | Cố tìm Breaker trong mọi chart | Có búa thì thấy đâu cũng là đinh | Trong vùng đi ngang, định nghĩa cho ra toàn nhiễu | Phần lớn thời gian không có Breaker đáng chờ | Cho phép mình ghi “hôm nay không có” |
| 17 | Dời vùng sau khi biết kết quả | Muốn hình “khớp” | Phá hỏng mọi dữ liệu về sau | Vùng khoá lúc xác nhận | Chụp ảnh chart lúc vẽ vùng |
| 18 | Coi một lần phản ứng là bằng chứng về lợi thế | Một mẫu đẹp gây ấn tượng mạnh | Một mẫu không nói gì; vùng ngẫu nhiên cũng “bật” nhiều lần (§12.4) | Lợi thế chỉ thấy được qua nhiều mẫu, gồm cả mẫu hỏng | Ghi cả ba kết cục cho mọi Breaker đã xác nhận |

---

## 24. Hindsight Bias

![[BB-v3-48-Hindsight-vs-Real-Time.svg|960]]
*Hình 48 — Cùng một chart: nhìn lại và nhìn tới.*

- **Ex-post Breaker:** vùng được gọi tên sau khi đã thấy toàn bộ chuỗi giá, kể cả retest và phản ứng. Lúc nào cũng “đẹp”.
- **Real-time Breaker:** vùng được gọi tên chỉ bằng những nến *đã đóng cửa* tại thời điểm đó. Luôn kèm hai dấu hỏi.

Tại thời điểm thật, đây là những thứ **có thể chưa xảy ra**: OB chưa thất bại; swing giữa chưa bị phá; chưa có displacement; Breaker chưa được xác nhận; chưa có retest. Vẽ vùng Breaker khi một trong các thứ này còn thiếu là vẽ bằng trí tưởng tượng.

![[BB-v3-49-Dong-Thoi-Gian-T1-T9.svg|960]]
*Hình 49 — Dòng thời gian T1 → T9 trên chart và trong bảng.*

| Mốc | Trader biết gì | Chưa thể biết gì | Xác nhận Breaker được chưa? | Được vẽ vùng Breaker? | Được vào lệnh? |
|---|---|---|---|---|---|
| **T1** OB gốc tồn tại | Có một nến ngược màu tại một swing vừa hình thành | Swing này có thành “swing giữa” không | Chưa | Chưa (chỉ đánh dấu như một OB) | Không |
| **T2** Giá tiến về OB | Cực trị cũ đã bị vi phạm; giá đang quay lại | OB sẽ giữ hay thủng | Chưa — mới là ứng viên | Chưa | Không |
| **T3** OB bị thử | Nến đóng cửa trong vùng | Nến sau đóng ở đâu | Chưa | Chưa | Không |
| **T4** Cấu trúc bị phá | Thân nến đóng qua swing giữa | Giá có ở lại bên kia không | Đang xảy ra | Chuẩn bị | Không |
| **T5** Displacement | Cú phá mạnh hay yếu | Giá có quay lại không | — | — | Không (không mua đuổi) |
| **T6** Đánh giá ứng viên | Đủ/thiếu mắt xích nào | — | Đang kiểm tra | — | Không |
| **T7** Gọi tên Breaker | Vùng, biên, mức sai, mục tiêu | Có retest không; giữ hay thủng | **Rồi** | **Được — và khoá lại** | Không |
| **T8** Retest | Giá đã chạm vùng | Giữ hay thủng | Rồi | Đã vẽ | Chưa — xuống khung nhỏ |
| **T9** Xác nhận vào lệnh | Khung nhỏ cho (hoặc không cho) chuỗi tín hiệu | Kết quả lệnh | Rồi | Đã vẽ | **Được, nếu có tín hiệu** |

Ba thói quen chống hindsight:
1. **Che nửa phải chart.** Tại nến đang xét, tự hỏi hai câu riêng: “đã gọi tên được chưa?” và “đã vào lệnh được chưa?”.
2. **Ghi giờ.** Mỗi vùng trong nhật ký có giờ vẽ. Vùng không có giờ vẽ là vùng vẽ sau.
3. **Đếm cả mẫu hỏng.** Mỗi Breaker đã xác nhận phải kết thúc bằng một trong ba nhãn: giữ, thủng, hết hạn.

---

## 25. Practical Identification Framework

![[BB-v3-50-Decision-Tree-Nhan-Dien.svg|960]]
*Hình 50 — Cây quyết định sáu câu hỏi.*

### 25.1 Đánh giá phê phán flow của protocol

| Bước trong flow của protocol | Có phải điều kiện theo ICT? | Nhận xét |
|---|---|---|
| Identify Original Order Block | Một phần | ICT nói “up/down-close candle tại swing gần nhất”, không nói “order block”. Thêm: nến phải **tại swing** |
| Did Price Fail the Original OB? | Có (gián tiếp) | Tương đương “swing chứa nến bị phá”. **Thiếu một bước trước nó: cực trị cũ đã bị vi phạm chưa?** Đây là chỗ flow của protocol hở nhất |
| Did Relevant Market Structure Break? | Có | Với OB tại swing, bước này và bước trên là một |
| Is There Evidence of Directional Displacement? | **Không** | Bằng chứng chất lượng. Nếu để thành cổng bắt buộc, bạn sẽ không bao giờ biết displacement có giúp gì |
| Does the Sequence Qualify…? | — | Bước tổng hợp; đúng chỗ |
| Identify the Breaker Zone | Có | Thêm: khoá biên ngay lúc này |
| Check HTF Context | **Không** | Bộ lọc của bạn. Rất nên có, nhưng là của khung ICT 2022, không phải của định nghĩa Breaker |
| Check Liquidity and DOL | **Không** | Như trên |
| Wait for Price to Return | Không (với tên gọi) | Cần cho giao dịch |
| Observe Reaction / Confirmation | Không | Thuộc về vào lệnh |
| Evaluate Entry Conditions | Không | Thuộc về vào lệnh |
| Maintain / Invalidate / Abandon | Không nêu | Quy ước của note (§18) |

Flow đã sửa nằm ở Hình 50: chèn câu hỏi về cực trị cũ; chuyển displacement từ cổng bắt buộc thành ghi chú chất lượng; tách rõ ba khối **định nghĩa → lọc → thực thi**.

### 25.2 Checklist nhận diện ngắn

**A · Formation — có đủ nguyên liệu chưa?**
- [ ] Chỉ ra được **cực trị cũ** (đáy cũ / đỉnh cũ).
- [ ] Chỉ ra được **swing giữa** và **cây nến ngược màu cuối cùng** tại đó.
- [ ] Cực trị cũ **đã bị vi phạm** sau khi swing giữa hình thành.

**B · Validation — đã thành Breaker chưa?**
- [ ] Một **thân nến đã đóng cửa** qua swing giữa.
- [ ] Đã vẽ vùng (cả râu) và **khoá**; đã ghi giờ.
- [ ] Đã ghi: cú phá dứt khoát hay lê lết; có/không FVG; cực trị cũ là túi lớn hay gợn nhỏ.

**C · Relevance — có đáng chờ không?**
- [ ] Cùng hướng bias D1; biết DOL ở đâu.
- [ ] Swing bị phá là swing quan trọng của khung đó.
- [ ] Vùng chưa bị chạm; mục tiêu chưa đạt; còn đủ chỗ chạy.

**D · Entry — có lệnh không?**
- [ ] Giá **đã quay lại** vùng.
- [ ] Khung nhỏ cho bằng chứng cấu trúc (MSS có displacement) tại vùng.
- [ ] Có chỗ vào cụ thể (FVG khung nhỏ), mức dừng theo một trong ba mức “sai”, mục tiêu là liquidity.
- [ ] Rủi ro ≤ 0,5%.

Bản một trang dùng hằng ngày ở §30.

---

## 26. Case Studies and Counterexamples

Sáu case **dựng** (giá giả định) để tập đọc trình tự, cộng hai mẫu **thật** đã có trong vault (§26.9). Mỗi case đi qua đúng 11 mục của protocol.

### 26.1 Case A — Bullish Breaker sách giáo khoa

![[BB-v3-51-Case-A-Textbook-Bullish.svg|960]]
*Hình 51 — Case A.*

1. **Cấu trúc ban đầu:** D1 hướng lên; H1 đang hồi xuống về nửa dưới của khoảng giá lớn.
2. **OB gốc:** nến tăng cuối cùng tại đỉnh giữa H1 (bearish OB). Đánh dấu ngay khi swing hình thành.
3. **Chuỗi giá:** đáy phiên trước → đỉnh giữa → rơi qua đáy phiên trước → bật lên → đóng cửa trên đỉnh giữa → hồi về → bật lên.
4. **Liquidity:** túi sell-side dưới đáy phiên trước bị lấy — một túi dễ thấy.
5. **Structural break:** thân nến đóng cửa trên đỉnh giữa (MSS tăng H1).
6. **Displacement:** có — vài nến tăng thân dài liên tiếp.
7. **Nhận diện Breaker:** đủ ba mắt xích ngay khi nến phá đóng cửa. Vùng = cả cây nến tăng tại đỉnh giữa.
8. **Retest:** râu chạm sâu vào vùng, nến đóng cửa trong vùng, không đóng dưới mép xa.
9. **Xét vào lệnh:** chỉ sau khi M5 cho MSS tăng có displacement tại vùng; vào ở FVG M5.
10. **Vô hiệu:** setup — dưới đáy M5 vừa quét; vùng — đóng cửa dưới mép xa; ý tưởng — dưới đáy mới H1.
11. **Kết luận được gì:** đây là hình dạng của trình tự khi mọi thứ cùng chiều. Nó **không** cho biết trình tự này chạy đúng bao nhiêu lần.

### 26.2 Case B — Bearish Breaker sách giáo khoa

![[BB-v3-52-Case-B-Textbook-Bearish.svg|960]]
*Hình 52 — Case B. Ảnh gương của Case A.*

1. **Cấu trúc ban đầu:** D1 hướng xuống; H1 đang hồi lên về nửa trên của khoảng giá lớn.
2. **OB gốc:** nến giảm cuối cùng tại đáy giữa H1 (bullish OB).
3. **Chuỗi giá:** đỉnh phiên trước → đáy giữa → tăng vượt đỉnh phiên trước → rơi → đóng cửa dưới đáy giữa → hồi lên → rơi tiếp.
4. **Liquidity:** túi buy-side trên đỉnh phiên trước bị lấy.
5. **Structural break:** thân nến đóng cửa dưới đáy giữa (MSS giảm H1).
6. **Displacement:** có.
7. **Nhận diện Breaker:** ngay khi nến phá đóng cửa. Vùng = cả cây nến giảm tại đáy giữa.
8. **Retest:** râu chạm vùng, đóng cửa trong vùng, không đóng trên mép xa.
9. **Xét vào lệnh:** M5 cho MSS giảm có displacement; vào ở FVG M5.
10. **Vô hiệu:** setup — trên đỉnh M5 vừa quét; vùng — đóng cửa trên mép xa; ý tưởng — trên đỉnh mới H1.
11. **Kết luận được gì:** định nghĩa đối xứng. Thị trường thì chưa chắc — ghi riêng hai chiều.

### 26.3 Case C — Failed OB nhưng không phải Breaker

![[BB-v3-53-Case-C-Failed-OB-Khong-Phai-Breaker.svg|960]]
*Hình 53 — Case C.*

```text
  đỉnh gốc ──────────────────────────────────  (CHƯA bị phá)
     \
      \   [nến tăng nhỏ = bearish OB giữa nhịp]
       \  /\                         /\  ← đóng cửa trên OB
        \/  \                       /  \
             \                     /    \→ quay xuống qua vùng
              \                   /
               \_________________/
                       đáy
```

1. **Cấu trúc ban đầu:** một nhịp giảm rõ, bắt đầu từ “đỉnh gốc”.
2. **OB gốc:** một nến tăng nhỏ **giữa** nhịp giảm — không nằm tại đỉnh của nhịp.
3. **Chuỗi giá:** giảm → nến tăng nhỏ → giảm tiếp tới đáy → hồi lên → đóng cửa trên OB → quay xuống.
4. **Liquidity:** không có cực trị cũ nào ở phía dưới bị vi phạm theo nghĩa của Breaker.
5. **Structural break:** **không có**. Đỉnh gốc còn nguyên; chuỗi đỉnh thấp hơn chưa gãy.
6. **Displacement:** nhịp hồi lên khá mạnh — và vẫn không đổi được kết luận.
7. **Nhận diện Breaker:** không. Thiếu “OB tại swing” và thiếu “swing bị phá”.
8. **Retest:** giá quay xuống qua vùng OB cũ như không có gì ở đó.
9. **Xét vào lệnh:** không có cơ sở mua tại vùng này.
10. **Vô hiệu:** không áp dụng — vùng chưa từng là Breaker.
11. **Kết luận được gì:** OB này vô hiệu. Hết. “Kháng cự bị phá thì thành hỗ trợ” không tự động đúng.

### 26.4 Case D — Breaker không có cú quét rõ ràng

![[BB-v3-54-Case-D-Khong-Co-Sweep-Ro-Rang.svg|960]]
*Hình 54 — Case D.*

1. **Cấu trúc ban đầu:** giá đi ngang hẹp rồi nhích lên.
2. **OB gốc:** nến tăng cuối cùng tại đỉnh giữa.
3. **Chuỗi giá:** một đáy nhỏ → đỉnh giữa → rơi về, thò xuống dưới đáy nhỏ ấy một chút → bật lên → đóng cửa trên đỉnh giữa.
4. **Liquidity:** “đáy cũ” chỉ là một gợn; khoảng vượt rất ngắn. Trên dữ liệu của sàn khác có thể không thấy cú vượt.
5. **Structural break:** rõ ràng.
6. **Displacement:** có.
7. **Nhận diện Breaker:** *theo chữ* — có (old low violated). *Theo cách đọc chặt* — mơ hồ giữa Breaker và Mitigation Block.
8. **Retest:** có, giữ.
9. **Xét vào lệnh:** như thường, nếu bối cảnh ủng hộ. Phân loại mơ hồ không cấm giao dịch; nó chỉ đổi mức “ý tưởng sai”.
10. **Vô hiệu:** vì hai cách phân loại cho hai mức “ý tưởng sai” gần như trùng nhau ở đây, dùng mức thấp hơn.
11. **Kết luận được gì:** định nghĩa của ICT không nói phải vi phạm bao nhiêu. Điều kiện **cần** để hợp lệ là có vi phạm; điều kiện để **đáng chờ** là cú vi phạm lấy một túi liquidity có ý nghĩa. Ghi “mơ hồ” + lý do; đừng ép về phía mình thích.

### 26.5 Case E — Breaker thất bại

![[BB-v3-55-Case-E-Breaker-That-Bai.svg|960]]
*Hình 55 — Case E.*

1. **Cấu trúc ban đầu:** D1 hướng **xuống**; nhịp tăng H1 là một nhịp hồi vào nửa trên của khoảng giá lớn.
2. **OB gốc:** nến tăng cuối cùng tại đỉnh giữa H1.
3. **Chuỗi giá:** đủ ba mắt xích → giá đi lên thêm một chút → hồi về vùng → bật một nến → đóng cửa xuyên qua.
4. **Liquidity:** đáy cũ H1 đã bị lấy. Nhưng phía trên, gần ngay đó, là vùng bán của D1.
5. **Structural break:** có, trên H1.
6. **Displacement:** có ở cú phá; **không có** ở cú bật lúc retest.
7. **Nhận diện Breaker:** hợp lệ.
8. **Retest:** nến đóng cửa trong vùng; một nến tăng nhỏ không tạo đỉnh mới; rồi nến đóng cửa dưới mép xa.
9. **Xét vào lệnh:** theo khung của note thì **không có lệnh**: ngược bias D1 (dừng ở câu 4 của cây quyết định) và M5 không cho MSS có displacement.
10. **Vô hiệu:** nến đóng cửa dưới mép xa và giá ở lại.
11. **Kết luận được gì:** vùng đúng tên, sai bối cảnh. Một mẫu không chứng minh quy tắc nào; nó gợi ra một câu hỏi đáng đếm (§27, câu 5).

### 26.6 Case F — Breaker trong vùng đi ngang

![[BB-v3-56-Case-F-Breaker-Trong-Consolidation.svg|960]]
*Hình 56 — Case F.*

1. **Cấu trúc ban đầu:** giá dao động giữa hai mép; không có chuỗi đỉnh/đáy cao hơn hay thấp hơn.
2. **OB gốc:** rất nhiều — mỗi gợn có một nến ngược màu.
3. **Chuỗi giá:** đỉnh nhỏ bị quét → đáy nhỏ bị phá → đáy nhỏ bị quét → đỉnh nhỏ bị phá → lặp lại.
4. **Liquidity:** toàn túi nhỏ bên trong vùng. Túi lớn nằm ngoài hai mép.
5. **Structural break:** có, nhưng chỉ là phá các gợn nội bộ.
6. **Displacement:** thỉnh thoảng — và bị đảo ngược ngay.
7. **Nhận diện Breaker:** theo chữ thì ra ba bốn cái. Theo §20: dừng ngay ở câu 2 (swing không quan trọng).
8. **Retest:** có, và phần lớn bị xuyên sau vài nến.
9. **Xét vào lệnh:** không.
10. **Vô hiệu:** liên tục.
11. **Kết luận được gì:** một định nghĩa có thể “đúng” mà vô dụng. Việc nên làm là chờ giá lấy liquidity ở một mép và rời vùng; lúc đó mới tìm Breaker.

### 26.7 Năm trường hợp dễ nhầm là Breaker

1. **Hỗ trợ/kháng cự ngang bị phá rồi retest** — không có cây nến tại swing, không có cực trị cũ bị vi phạm (§13.5).
2. **Mitigation Block** — giống hệt, chỉ khác cực trị cũ còn nguyên (Hình 19, 28).
3. **Order Block của nhịp mới** (nến giảm tại đáy mới) bị gọi là Bullish Breaker (Hình 13 C).
4. **OB giữa nhịp bị thủng** (Case C).
5. **Râu vượt swing giữa** được coi như cú phá (Hình 22).

### 26.8 Năm trường hợp Breaker hợp lệ nhưng không nên giao dịch

1. Ngược bias D1 (Case E, Hình 46 B).
2. Trong vùng đi ngang (Case F).
3. Mục tiêu đã đạt trước khi giá quay lại; hoặc khoảng chạy quá ngắn so với mức dừng.
4. Giá đã tạo MSS ngược trước khi về vùng (tình huống 10, §19).
5. Có túi liquidity lớn chưa bị lấy nằm **ngay sau lưng** vùng — giá có lý do để đi qua.

### 26.9 Năm kiểu Breaker thất bại — và hai mẫu thật trong vault

Năm kiểu:
1. **Xuyên thẳng:** giá về vùng và đóng cửa qua mép xa ngay (Hình 20).
2. **Bật yếu rồi thủng:** một hai nến phản ứng, không có MSS khung nhỏ, rồi thủng (Case E).
3. **Mòn dần:** giữ vài lần, mỗi lần bật thấp hơn, rồi thủng (tình huống 9).
4. **Bị bỏ qua vì vùng sâu hơn:** giá đi qua Breaker để tới FVG/OB bên dưới rồi mới bật — Breaker sai, ý tưởng đúng (Hình 36).
5. **Thất bại do gán nhãn:** vùng chưa bao giờ là Breaker (thiếu mắt xích), nên “thất bại” của nó không nói gì về Breaker.

**Hai mẫu thật (n = 2 — không đủ để kết luận gì về lợi thế):**

> [!example] Mẫu thắng — [[01 - Win - EURUSD - 2021-05-03- Short|EURUSD 03/05/2021 Short]]
> Bullish OB cuối tháng 4 → nhịp tăng tạo đỉnh range → các nến displacement đóng xuyên OB và quét old lows → Breaker chồng FVG (vùng Unicorn, ở premium) → giá hồi lên, một nến đóng **ngoài** cạnh trên vùng Unicorn rồi bị từ chối ngay → M5 cho FVG → vào lệnh. Đọc theo ba mắt xích: mắt xích 1 và 3 rõ. **Mắt xích 2 (đỉnh cũ bị vi phạm trước cú phá) chưa xác minh được từ ghi chép** → hiện xếp “Breaker theo nghĩa rộng; cần mở lại chart H1 để biết là Breaker chặt hay Mitigation Block”. Hành vi lúc retest khớp quy ước “đóng qua rồi bị kéo về ngay = chưa vô hiệu”.

> [!failure] Mẫu thua — [[01 - Loss - XAUUSD - 2014-05-19 - Short|XAUUSD 19/05/2014 Short]]
> Một “Bearish Breaker” H1 được chọn theo vị trí Fib thay cho OB sâu hơn; giá quét qua cạnh trên vùng (dính stop), lên tới OB sâu hơn rồi mới rơi đúng hướng. [[CS-03 - Nghich ly POI rank]] đã chỉ ra vùng này **không nêu được cây nến gốc** → theo §3 đây là kiểu thất bại số 5 (lỗi gán nhãn), đồng thời minh hoạ kiểu số 4 (vùng nông là liquidity cho vùng sâu).

---

## 27. Backtestable Observations

Không cần mô hình. Chỉ cần ghi đều tay, cho **mọi** Breaker đã xác nhận, không chọn lọc.

### 27.1 Ba loại thông tin

| Loại | Gồm | Ghi thế nào |
|---|---|---|
| **Quan sát trực tiếp** | Vị trí cây nến gốc · swing giữa bị phá (nến nào, giờ nào) · cực trị cũ bị vi phạm (có/không) · có FVG trong nhịp phá (có/không) · biên vùng · có retest (có/không) · nến retest đóng trong hay ngoài · vô hiệu (có/không) | Có/không, hoặc một mức giá. Hai người ghi phải ra cùng kết quả |
| **Bán khách quan** | Swing bị phá có “quan trọng” không · displacement “mạnh” không · túi liquidity “đáng kể” không · OB gốc “đẹp” không | Ghi kèm **quy tắc bạn dùng** (ví dụ “mạnh = ba nến cùng màu liền nhau, thân dài hơn hẳn các nến trước”). Quy tắc viết ra trước khi xem kết quả |
| **Chủ quan / diễn giải** | Ý định của Smart Money · vị thế của tổ chức · vì sao ai đó vào lệnh · vùng có “chứa lệnh tổ chức” không | **Không ghi như dữ liệu.** Không kiểm chứng được bằng chart |

### 27.2 Bảy câu hỏi backtest đơn giản

| # | Câu hỏi | Cách đếm | Nhãn |
|---|---|---|---|
| 1 | Breaker có được retest không? | Trong mọi Breaker đã xác nhận: bao nhiêu cái được chạm lại, bao nhiêu cái hết hạn | Quan sát |
| 2 | Giá phản ứng thế nào khi retest? | Chia ba nhóm: giữ / thủng / chưa rõ (theo quy ước đóng cửa và ở lại) | Quan sát |
| 3 | Sau retest giá có tạo displacement theo hướng kỳ vọng không? | Có/không, trên khung nhỏ đã định trước | Bán khách quan |
| 4 | Giá có phá vùng Breaker không? | Số mẫu thân nến đóng qua mép xa | Quan sát |
| 5 | Thuận xu hướng, ngược xu hướng và đi ngang có khác nhau không? | Tách ba rổ theo bối cảnh khung lớn; so số mẫu giữ / thủng của từng rổ | [GIẢ THUYẾT] [BACKTEST REQUIRED] |
| 6 | Breaker khung lớn và khung nhỏ có khác nhau không? | Tách rổ theo khung của Breaker | [GIẢ THUYẾT] [BACKTEST REQUIRED] |
| 7 | Có túi liquidity lớn, hoặc có displacement, thì có tốt hơn không? | Tách rổ có/không; so sánh | [GIẢ THUYẾT] [BACKTEST REQUIRED] |

Thêm ba câu hỏi đến từ chính nghiên cứu này:

| # | Câu hỏi | Vì sao đáng hỏi |
|---|---|---|
| 8 | Breaker (cực trị cũ bị vi phạm) có khác Mitigation Block (không bị vi phạm) không? | Đây là thứ duy nhất tách hai cái tên. Nếu không khác, sự phân biệt chỉ có giá trị từ vựng |
| 9 | Lần chạm đầu có tốt hơn các lần sau không? | Niềm tin của cộng đồng ICT và một nghiên cứu về S/R nói ngược nhau (§12.1) |
| 10 | Breaker có giữ tốt hơn **một vùng cùng kích thước đặt ở chỗ khác** không? | Câu hỏi nền tảng. Không trả lời được câu này thì mọi câu khác vô nghĩa (§12.4) |

Bốn nguyên tắc để dữ liệu dùng được: **(1)** ghi cả mẫu hỏng và mẫu hết hạn; **(2)** quy tắc viết trước, không sửa sau khi thấy kết quả; **(3)** không trộn hai cách đánh dấu nến; **(4)** tách Bullish và Bearish. Template: [[Backtest templete]]; lỗi liên quan: [[12-Mistake-Log-Data-Mismatch-Backtest]].

---

## 28. What We Actually Know vs What We Assume

![[BB-v3-57-Biet-vs-Gia-Dinh.svg|960]]
*Hình 57 — Bốn tầng bằng chứng.*

| Claim | Phân loại | Ta thật sự biết gì |
|---|---|---|
| Breaker bắt nguồn từ một OB thất bại | **[ICT] — đúng một phần** | ICT định nghĩa bằng “nến up/down-close tại swing gần nhất”, không dùng chữ order block trong bài giảng Breaker. Cây nến đó trùng với thứ định nghĩa OB gọi là OB, nên cách nói tắt đúng về vị trí — nhưng bỏ sót hai điều kiện |
| Structural break liên quan tới Breaker | **[ICT] — đúng** | Phải chờ giá “break through” swing giữa. ICT gọi đó là market structure shift/break |
| Mọi Failed OB là Breaker | **Sai** | Thiếu “tại swing” và “cực trị cũ bị vi phạm” thì không phải (§10) |
| Mọi Breaker cần liquidity sweep | **Đúng theo định nghĩa chặt, với một lưu ý** | Cần cực trị cũ bị *vi phạm*. Không cần cú vi phạm là một sweep “đẹp”. Cách dùng lỏng của cộng đồng bỏ luôn điều kiện này |
| Mọi Breaker cần displacement | **Không có trong định nghĩa** | ICT chỉ tả cú phá là mạnh. Cộng đồng biến thành điều kiện. Có giúp hay không: [BACKTEST REQUIRED] |
| Mọi Breaker phải chứa FVG | **Sai** | Bài giảng Breaker không nhắc FVG. Breaker + FVG là một tổ hợp (Unicorn), không phải định nghĩa |
| Breaker có thể đóng vai POI ngược chiều | **[ICT]** | Đó chính là cách ICT dùng nó: “setup worth considering” khi giá quay lại |
| Breaker luôn tạo phản ứng | **Giả định vô căn cứ** | Ba kết cục giữ / thủng / không quay lại đều xảy ra |
| Breaker có lợi thế giao dịch | **[BACKTEST REQUIRED]** | Không nguồn nào đã đối chiếu đưa ra số liệu kiểm chứng. Mô phỏng ở bản v2 cho thấy vùng ngẫu nhiên cũng “giữ” khoảng một nửa số lần. Vault hiện có hai mẫu |
| Breaker mạnh hơn Mitigation Block | **[GIẢ THUYẾT] của cộng đồng** | Không tìm thấy trong bài giảng Breaker đã đối chiếu |
| Vào lệnh ở 50% vùng Breaker | **Cộng đồng thêm vào** | Không có trong bài giảng Breaker |
| Người bán bị kẹt mua lại ở hoà vốn nên vùng đỡ giá | **[DIỄN GIẢI]** | Có nền hành vi; không đo được trên chart nến |
| Smart Money cố ý tạo ra Breaker | **Không kiểm chứng được** | Không thể suy ra danh tính hay ý định từ OHLC |

**Chỗ các nguồn không thống nhất (trình bày, không gộp):**
- *Nến nào:* bài giảng ICT, và một số trader theo sát ICT[^dang][^tt] → nến up-close tại swing high cho Bullish. Một thư viện thuật ngữ và một blog[^lux-bb][^mql5] → nến giảm của nhịp rơi.
- *Có cần sweep không:* định nghĩa chặt cần; cách dùng lỏng không cần[^lux-bb].
- *Thân hay râu:* cả hai đều lưu hành; ICT nói “entire range” trong ví dụ.
- *Xác nhận bằng gì:* ICT nói “break through”; cộng đồng thêm displacement, thêm “lần retest đầu tiên”.

---

## 29. Final Mental Model

### 29.1 Mười câu trả lời bằng ngôn ngữ đơn giản nhất

1. **Breaker thật sự là gì?** Một cái trần đã bị đục thủng, nay nằm dưới chân giá (hoặc một cái sàn đã bị đục thủng, nay nằm trên đầu giá).
2. **Nó bắt đầu từ đâu?** Từ một cây nến ngược màu ở đỉnh giữa hoặc đáy giữa — chỗ giá từng bị chặn lại.
3. **Điều gì khiến Order Block gốc thất bại?** Giá quay lại và một cây nến đóng cửa ở phía bên kia. Vì sao phe giữ vùng thua thì chart không nói.
4. **Điều gì khiến nó thành Breaker?** Hai việc xảy ra theo thứ tự: trước tiên giá đi quá cực trị cũ ở phía bên kia; sau đó giá quay lại phá cái swing chứa cây nến ấy.
5. **Tại sao vùng đổi vai?** Vùng không đổi. Giá đổi phía. Và những người bị kẹt ở đó muốn thoát theo hướng ngược lại.
6. **Tại sao giá quay lại?** Vì sau một nhịp đi nhanh giá hay hồi. Nhưng không ai hứa nó hồi về đúng chỗ đó.
7. **Tại sao giá có thể phản ứng?** Vì ở mức dễ thấy có thể có người muốn thoát lệnh và người muốn vào lệnh. “Có thể” — không nhìn thấy được.
8. **Điều gì xác nhận Breaker?** Cây nến đóng cửa qua swing giữa, sau khi cực trị cũ đã bị vi phạm. Không cần gì thêm.
9. **Điều gì làm Breaker thất bại?** Một cây nến đóng cửa qua mép xa của vùng và giá ở lại bên đó.
10. **Khi nào dùng trong ICT 2022 Model?** Khi Breaker H1 nằm trong vùng D1 đang chờ, cùng hướng D1, còn mục tiêu phía trước — và chỉ vào lệnh khi M5 cho bằng chứng tại vùng.

### 29.2 Một sơ đồ duy nhất

![[BB-v3-58-Final-Mental-Model.svg|960]]
*Hình 58 — ORIGINAL ORDER BLOCK → FAILURE → STRUCTURAL CHANGE → BREAKER FORMATION → RETEST → POSSIBLE REACTION.*

**Ý nghĩa của từng mũi tên:**

| Mũi tên | Nghĩa | Loại |
|---|---|---|
| **Original OB → Failure** | Giá đã đi xa (vượt cực trị cũ), rồi quay lại; một thân nến đóng cửa xuyên qua vùng | Đã xảy ra — nhìn thấy được |
| **Failure → Structural change** | Vì OB nằm ngay tại swing giữa, thủng OB cũng là thủng swing. Hai việc là một | Đã xảy ra — nhìn thấy được |
| **Structural change → Breaker formation** | Một hành động *đặt tên*: vùng cũ, vai mới. Khoá biên vùng | Việc của bạn |
| **Breaker formation → Retest** | Giá hồi về vùng. **Có thể không bao giờ xảy ra** | Tương lai |
| **Retest → Possible reaction** | Vùng giữ, thủng, hoặc chưa rõ. Chỉ bằng chứng khung nhỏ mới biến “có thể” thành một lệnh | Tương lai |

Ba mũi tên đầu là **lịch sử**. Hai mũi tên cuối là **giả thuyết**. Toàn bộ kỷ luật khi dùng Breaker nằm ở việc không lẫn hai nhóm này.

---

## 30. Daily Trading Checklist

> [!todo] Checklist Breaker — dùng mỗi phiên
> **TRƯỚC PHIÊN (D1 → H1)**
> - [ ] Đã viết bias D1 và DOL. Biết giá đang ở premium hay discount của khoảng giá lớn.
> - [ ] Đã đánh dấu vùng D1 đang chờ.
> - [ ] Trên H1: có Breaker nào **đã xác nhận**, **cùng hướng D1**, **trong hoặc sát vùng D1** không? Nếu không → hôm nay không có setup Breaker. Ghi “không có” và dừng.
>
> **VỚI MỖI BREAKER H1 ĐANG THEO DÕI**
> - [ ] Chỉ ra được ba thứ: cực trị cũ · swing giữa · cây nến gốc.
> - [ ] Cực trị cũ đã bị vi phạm **trước** cú phá. (Nếu không: ghi là Mitigation Block.)
> - [ ] Có **thân nến đóng cửa** qua swing giữa. (Nếu chỉ râu: chưa phải.)
> - [ ] Vùng đã khoá (cả râu), có giờ vẽ. Không dời.
> - [ ] Đã ghi ba đặc điểm: cú phá dứt khoát / lê lết · có / không FVG · túi liquidity lớn / nhỏ.
> - [ ] Vùng chưa bị chạm; mục tiêu chưa đạt; còn chỗ chạy.
> - [ ] Đã đặt cảnh báo ở mép gần.
>
> **KHI GIÁ TỚI VÙNG (M5)**
> - [ ] Đang trong khung giờ giao dịch của mình; không sát tin lớn.
> - [ ] Chờ. Chạm vùng **chưa** phải tín hiệu.
> - [ ] M5 cho MSS **có displacement** theo hướng Breaker, tại vùng.
> - [ ] Có FVG M5 để vào khi giá hồi. Không mua/bán đuổi.
> - [ ] Mức dừng đã chọn theo một trong ba mức “sai” (setup / vùng / ý tưởng) — chọn **trước** khi vào.
> - [ ] Mục tiêu là một túi liquidity cụ thể; khoảng tới mục tiêu đủ lớn so với mức dừng.
> - [ ] Rủi ro ≤ 0,5% tài khoản.
>
> **KHÔNG CÓ LỆNH NẾU**
> - [ ] Breaker ngược bias D1 · nằm giữa vùng đi ngang · đã bị đóng nến xuyên · M5 không cho MSS · mình đang muốn “gỡ”.
>
> **SAU PHIÊN**
> - [ ] Mỗi Breaker đã xác nhận nhận một nhãn: **giữ / thủng / chưa rõ / hết hạn** — kể cả khi không vào lệnh.
> - [ ] Chụp chart lúc vẽ vùng và lúc kết thúc.

---

## Flashcards / Active Recall

**Q1.** Ba mắt xích của một Bullish Breaker, đúng thứ tự?
**A.** Nến tăng cuối cùng tại đỉnh giữa → đáy cũ bị vi phạm → thân nến đóng cửa trên đỉnh giữa.

**Q2.** Thiếu mắt xích 2 nhưng có mắt xích 3 thì gọi là gì?
**A.** Mitigation Block.

**Q3.** Vì sao “Breaker = OB thất bại” chưa đủ?
**A.** Vì nó bỏ sót hai điều kiện: OB phải nằm tại swing giữa, và cực trị cũ phải bị vi phạm trước.

**Q4.** Bài giảng Breaker của ICT có đòi displacement và FVG không?
**A.** Không. Đó là phần cộng đồng thêm vào; trong note chúng là bằng chứng chất lượng.

**Q5.** Bullish Breaker là nến màu gì, nằm ở đâu?
**A.** Nến **tăng**, tại **đỉnh giữa**. (Nến giảm tại đáy mới là Order Block của nhịp tăng mới.)

**Q6.** Sau khi thành Bullish Breaker, mép nào là mép xa?
**A.** Mép **dưới**. Thân nến đóng dưới đó và ở lại = Breaker thất bại.

**Q7.** Bốn sự kiện phải tách rời?
**A.** Hình thành (ứng viên) → xác nhận → retest → vào lệnh.

**Q8.** Giá chạm Breaker — đã vào lệnh được chưa?
**A.** Chưa. Chạm là “đến nơi”. Cần MSS có displacement trên khung nhỏ tại vùng.

**Q9.** Một Breaker không bao giờ được retest thì ghi thế nào?
**A.** Hết hạn. Vẫn tính vào mẫu.

**Q10.** Breaker M5 ngược bias D1?
**A.** Không giao dịch. M5 không có quyền tạo bối cảnh.

**Q11.** Trong một Bullish Breaker có mấy sự kiện liquidity?
**A.** Hai: sell-side dưới đáy cũ (mắt xích 2) và buy-side trên đỉnh giữa (mắt xích 3).

**Q12.** Điều gì trong câu chuyện “người bán bị kẹt” là quan sát được?
**A.** Không gì cả. Đó là diễn giải hợp lý; chart nến không cho thấy vị thế.

---

## Lesson Learned

### Bài học chính
- Breaker là **dấu vết của một cú đảo chiều hai nhịp**, không phải một lực hút. Nó cho biết điều gì đã xảy ra; không hứa điều gì sẽ xảy ra.
- Thứ làm Breaker khác một vùng bị phá bất kỳ là **trình tự** (cực trị cũ trước, swing giữa sau) và **vị trí** (tại swing). Bỏ một trong hai là đang nói về thứ khác.
- Phần lớn những gì được dạy là “quy tắc Breaker” (displacement, FVG, 50%, stop) không nằm trong bài giảng gốc. Chúng có thể hữu ích — với điều kiện mình biết đó là quy tắc **của mình**.

### Quy tắc cá nhân rút ra
- Không vẽ vùng Breaker trước khi có thân nến đóng qua swing giữa.
- Không vào lệnh vì giá chạm vùng.
- Mỗi Breaker đã xác nhận phải có một nhãn kết cục, kể cả khi không giao dịch.
- Khi phân loại mơ hồ, ghi “mơ hồ”.

### Câu nhắc khi trade
> *“Ba mắt xích là lịch sử. Retest và phản ứng là dấu hỏi. Mình giao dịch bằng chứng, không giao dịch cái tên.”*

---

## Tự kiểm tra chất lượng note (QC theo protocol)

| # | Câu hỏi QC | Đạt? | Ở đâu |
|---|---|---|---|
| 1 | Giải thích Breaker cho người chưa biết ICT? | ✓ | §2, §4 |
| 2 | Giải thích WHY chứ không chỉ WHAT? | ✓ | §6, §11, §12 |
| 3 | Giải thích rõ Original Order Block? | ✓ | §4.3, §7 bước 1 |
| 4 | Giải thích chính xác Failure? | ✓ | §6.4, Hình 16 |
| 5 | Giải thích structural break? | ✓ | §4.2, §6.2, §15.1 |
| 6 | Phân biệt Failed OB với Breaker? | ✓ | §5.7, §10, Hình 24 |
| 7 | Giải thích vì sao vùng đổi vai? | ✓ | §6.5, §11 |
| 8 | Phân biệt Bullish và Bearish Breaker? | ✓ | §8, §9 |
| 9 | Quan hệ với Liquidity? | ✓ | §4.4, §14 |
| 10 | Phân biệt MSS, BOS, Displacement? | ✓ | §15 |
| 11 | Vai trò của FVG? | ✓ | §15.4, §16.1 |
| 12 | Phân biệt Formation, Confirmation, Retest, Entry? | ✓ | §18.2, Hình 39 |
| 13 | Có counterexamples? | ✓ | §8.3, §9.3, §21, §26 |
| 14 | Giải thích Breaker thất bại? | ✓ | §19, §26.5, §26.9 |
| 15 | Kiểm soát hindsight? | ✓ | §24 |
| 16 | Phân biệt diễn giải ICT với quan sát? | ✓ | Nhãn xuyên suốt; §5.3, §28 |
| 17 | Áp dụng D1 → H1 → M5? | ✓ | §22 |
| 18 | Có checklist nhận diện thực hành? | ✓ | §25.2, §30 |
| 19 | Tránh khẳng định cơ chế không quan sát được? | ✓ | §11, §12.2 |
| 20 | Chỉ ra điều cần backtest? | ✓ | §27, §28 |

**Giới hạn còn lại của lần nghiên cứu này:** (a) lời ICT được đối chiếu qua phụ đề tự động và bản tóm tắt, chưa nghe âm thanh gốc — nên kiểm tra lại màu nến ở hai đoạn định nghĩa trước khi coi là chắc chắn; (b) bài giảng Mitigation Block chỉ tiếp cận được qua bản tóm tắt; (c) Rejection Block và Reclaimed OB mô tả theo cách dùng phổ biến; (d) chưa đối chiếu các bài giảng ICT khác (kể cả 2022 Mentorship) xem ông có bổ sung điều kiện cho Breaker không.

---

## Liên kết

**Nền tảng:** [[25-OB-Order-Block]] · [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]] · [[51-OB-Mitigation-Depth-Vi-sao-Shallow-CE-hay-Full-khac-nhau]] · [[01-Advance-Market-Structure-Short-Term-Low-Intermediate-Term-Low-Long-Term-Low]]
**Họ block:** [[22-Mitigation-Block]] · [[28-Rejection-Block]] · [[44-Hidden-Order-Block]] · [[17-Inverse-Fair-Value-Gap-iFVG]] · [[03-Balanced-Price-Range]] · [[13-FVG-Fair-Value-Gap]]
**Cấu trúc:** [[21-Market-Structure-Shift]] · [[05-BOS-Break-of-Structure]] · [[09-Change-of-Character]] · [[50-Displacement-In-Depth]] · [[41-Change-in-State-of-Delivery]]
**Liquidity & vị trí:** [[19-Liquidity]] · [[20-Liquidity-Sweep]] · [[33-Turtle-Soup]] · [[15-Inducement]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[12-Dealing-Range]] · [[27-Premium-Discount]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]]
**Mô hình & thực thi:** [[01 - ICT 2022 Model]] · [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] · [[07 - Unicorn Model]] · [[59-Daily-Bias]] · [[32-Top-down-Analysis-Multiple-Timeframes]] · [[18-Kill-Zones]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]]

---

## Nguồn tham khảo

> [!note] Về nguồn
> **Nguồn gần gốc nhất** đã dùng là phụ đề tự động của chính bài giảng ICT về Breaker[^ict-bb]. Phụ đề tự động có lỗi nhận dạng; các cụm trong ngoặc kép ở note là những cụm ngắn lặp lại nhiều lần trong phụ đề. Các nguồn cộng đồng dùng để **đối chiếu cách định nghĩa**, không dùng làm bằng chứng về hiệu quả. **Không nguồn nào đưa ra thống kê có kiểm chứng về Breaker.**

**ICT (nguồn gốc, tiếp cận gián tiếp)**
[^ict-bb]: Michael J. Huddleston (ICT) — *ICT Mentorship Core Content – Month 04 – ICT Breaker Block*. Video: https://www.youtube.com/watch?v=UrS-mtGHtAA. Đối chiếu qua phụ đề tự động tại https://opentools.ai/youtube-summary/ict-mentorship-core-content-month-04-ict-breaker-block và bản tóm tắt tại https://videohighlight.com/v/UrS-mtGHtAA. Truy cập 2026-11-10.
[^ict-mb]: Michael J. Huddleston (ICT) — *ICT Mentorship Core Content – Month 04 – Mitigation Blocks*. Chỉ tiếp cận được qua bản tóm tắt tự động (không phải lời nguyên văn): https://videohighlight.com/v/FOUzW0QmsfI. Truy cập 2026-11-10.

**Cộng đồng ICT (đối chiếu định nghĩa)**
[^dang]: Dangstrat — thread *Breaker Blocks & How to Use Them* (2023): nến up-close tại swing high cho Bullish Breaker; cần raid + MSS. https://en.rattibha.com/thread/1647911678397366272
[^tt]: TTrades — *Breaker Blocks Simplified* (qua bản tóm tắt tự động): chuỗi low – high – lower low – higher high; breaker là chuỗi nến up-close; Unicorn = breaker + FVG. https://videohighlight.com/v/75S4vwD4P1U
[^lux-bb]: LuxAlgo Library — *Breaker Block*: định nghĩa chặt cần liquidity run, cách dùng lỏng coi mọi OB bị phá là breaker; đánh dấu nến của nhịp thất bại; “marking conventions vary”. https://www.luxalgo.com/library/concept/breaker-block/
[^lux-mb]: LuxAlgo Library — *Mitigation Block*: có sweep là breaker, failure swing là mitigation block; câu chuyện người bị kẹt là “plausible story”, không phải quan sát. https://www.luxalgo.com/library/concept/mitigation-block/
[^lux-uni]: LuxAlgo Library — *Unicorn*: breaker chồng FVG; nếu không chồng thì là hai ý tưởng riêng. https://www.luxalgo.com/library/concept/unicorn/
[^mql5]: MQL5 blog — *Breaker Blocks: Why Most ICT Traders Draw Them Wrong* (2026): ba điều kiện sweep + displacement + retest đầu; dùng nến giảm; tác giả bán công cụ. https://www.mql5.com/en/blogs/post/773691

**Nghiên cứu ngoài ICT (cơ chế thị trường)**
[^osler]: Osler, C. L. (2003). *Currency Orders and Exchange-Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis*. Journal of Finance 58(5). Bản staff report: https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf
[^kav]: Kavajecz, K. A., & Odders-White, E. R. (2004). *Technical Analysis and Liquidity Provision*. Review of Financial Studies 17(4).
[^chung]: Chung, K., & Bellotti, A. (2021). *Evidence and Behaviour of Support and Resistance Levels in Financial Time Series*. arXiv:2101.07410. https://arxiv.org/abs/2101.07410
[^shef]: Shefrin, H., & Statman, M. (1985). *The Disposition to Sell Winners Too Early and Ride Losers Too Long*. Journal of Finance 40(3).

**Nội bộ vault**
- Bản v2 (71 mục, registers, mô phỏng null, thiết kế backtest): `Claude outputs/backups/04-Breaker-Block.2026-11-10.md.bak`
- Mẫu backtest: [[01 - Win - EURUSD - 2021-05-03- Short]] · [[01 - Loss - XAUUSD - 2014-05-19 - Short]] · [[CS-03 - Nghich ly POI rank]]

---

## Changelog

### v3 — 2026-11-10
- **Viết lại toàn bộ** theo *ICT Deep Research Protocol — Breaker Block* (30 phần): giải thích kiểu trẻ 5 tuổi trước, thuật ngữ sau; năm tầng cho mỗi khái niệm; không công thức, không thống kê.
- **Nguồn:** đối chiếu phụ đề tự động của bài giảng ICT Month 04 — Breaker Block. Hệ quả: (a) xác nhận quy ước “nến tăng tại đỉnh giữa” và “cả râu”; (b) xác nhận việc cực trị cũ bị vi phạm nằm trong định nghĩa; (c) ghi rõ displacement, FVG, 50%, stop, điều kiện vô hiệu **không** có trong bài giảng; (d) hạ “Breaker mạnh hơn Mitigation Block” xuống giả thuyết.
- **Khung mới:** ba mắt xích + hai theo dõi (§3); bốn nhánh của Failed OB (§10); ba ngăn hình thành / chất lượng / vào lệnh (§15); bốn sự kiện tách biệt (§18); năm câu hỏi chọn Breaker (§20); ba mức “sai” (§22.3); dòng thời gian T1–T9 (§24).
- **Hình:** 58 sơ đồ mới `BB-v3-01…58`. Hình `BB-Deep-*`, `BB-Sim-*` của v2 vẫn trong `attachments`, không nhúng.
- **Đưa ra khỏi thân note** (còn trong backup v2): registers DEF-BB / RULE-BB / HYP-BB, journal extension, thiết kế backtest 17 yếu tố, chi tiết mô phỏng null.
- **Frontmatter:** thêm `version: v3`, tag `trading/deep-dive`; thêm prerequisite [[05-BOS-Break-of-Structure]], [[19-Liquidity]]; thêm mistake [[09-Mistake-Wrong-daily-bias]]. `status` giữ `developing`.
- **Mã sinh hình:** `Claude outputs/BB-v3-figures/` (Python; sửa và chạy lại để cập nhật hình).
- **Backup v2:** `Claude outputs/backups/04-Breaker-Block.2026-11-10.md.bak`.

### v2 — 2026-10-17
Viết lại theo protocol 18 phần / 71 mục: BB-DEF v0.1, vòng đời 10 trạng thái, registers, mô phỏng null, 32 hình `BB-Deep` / `BB-Sim`. Sửa quy ước nến sang “nến tăng tại đỉnh giữa”.

### v1 — 2026-06-22 → 2026-07-28
Bản gốc: định nghĩa, nhận diện, MTF, ví dụ chart, checklist, edge cases, case studies.
