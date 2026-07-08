---
type: mistake
category: psychology
severity: high
related_model: ICT 2022
frequency: 5
status: active
tags:
  - trading/ict/mistake
  - trading/review
  - trading/psychology
created: 2026-07-08
updated: 2026-07-08
---

# Mistake - FOMO Entry

> [!summary] Tóm tắt 1 câu
> Vào lệnh vì **sợ bỏ lỡ** một con sóng đang chạy — đuổi theo giá đã di chuyển xa khỏi POI, thường ở đúng vùng Premium (với lệnh mua) hoặc Discount (với lệnh bán) — thay vì chờ giá chiết khấu về một điểm vào có cơ sở cấu trúc và RR hợp lý.

> [!danger] Nguyên tắc cốt lõi
> **Bỏ lỡ một lệnh không tốn tiền; đuổi theo một lệnh thì có.** Nếu quyết định vào lệnh được kích hoạt bởi cảm giác "nó chạy mất rồi" chứ không phải bởi một checklist đã hoàn tất (POI + sweep + MSS trong đúng phía Premium/Discount), thì đó không phải là một entry — đó là một phản ứng cảm xúc đang đội lốt phân tích.

---

## 1. Mô tả lỗi

FOMO Entry (Fear Of Missing Out) là lỗi **tâm lý-thực thi**: trader nhìn thấy một con sóng displacement đang chạy mạnh và nhảy vào giữa/cuối con sóng đó, không phải vì có tín hiệu hợp lệ mà vì sợ "con tàu rời ga mà mình chưa lên". Đây là một trong những lỗi phá tài khoản âm thầm nhất vì nó *cảm giác* như đang chủ động, quyết đoán, "bắt được nhịp" — trong khi thực chất là đang mua đúng nơi đắt nhất và bán đúng nơi rẻ nhất.

Khác với [[02 - Mistake - Enter before liquidity sweep]] (vào sớm, trước khi thanh khoản bị quét) — FOMO thường là vào **muộn**: sweep đã xảy ra, displacement đã đi phần lớn quãng đường, draw on liquidity gần cạn, và bạn nhảy vào đúng lúc con sóng sắp hết nhiên liệu. Cả hai lỗi đều là entry sai thời điểm, nhưng FOMO nằm ở đầu bên kia của trục thời gian.

Các biểu hiện điển hình:

- Tôi thấy một nến xanh/đỏ lớn và vào lệnh ngay trên nến đó vì "momentum đang mạnh".
- Tôi đã bỏ lỡ entry "đẹp" trước đó, nên vào một entry tệ hơn để "cho bằng được".
- Tôi vào lệnh mà không thể chỉ ra POI phía trước — giá đang ở "vùng trống", không có mốc nào để neo target hay SL.
- Tôi tự nới rộng SL để "theo kịp" giá, phá vỡ luôn quy tắc rủi ro (xem [[07 - Mistake - Risk more than 0.5% total account]]).

![[FOMO-Sec-01-MoTa.svg|760]]
*Sơ đồ: entry FOMO mua tại đỉnh Premium sau khi sóng đã kéo dài — đúng nơi lẽ ra phải chờ pullback về Discount POI.*

---

## 2. Biểu hiện & Dấu hiệu nhận biết

FOMO có hai lớp dấu hiệu song song: **tâm lý** (trong đầu) và **kỹ thuật** (trên chart). Nhận diện được cả hai giúp bắt lỗi *trước* khi tay chạm chuột.

| Dấu hiệu | Loại | Mức cảnh báo |
|---|---|---|
| "Nó chạy mất rồi, phải vào ngay!" | Tâm lý | Đỏ |
| Tim đập nhanh / tay run khi bấm lệnh | Tâm lý | Đỏ |
| Bỏ qua checklist vì "không kịp" | Tâm lý | Đỏ |
| Vừa đóng một lệnh, ngay lập tức muốn "vào lại" | Tâm lý | Amber |
| Giá đã đi 3-5 nến displacement liên tiếp | Kỹ thuật | Amber |
| Entry rơi vào Premium (mua) / Discount (bán) | Kỹ thuật | Đỏ |
| Không có POI nào phía trước entry | Kỹ thuật | Đỏ |
| Vào ngay sau một cú news spike | Kỹ thuật | Đỏ |
| SL buộc phải nới rất rộng để "theo" giá | Kỹ thuật | Đỏ |

Checklist nhận diện nhanh (nếu ≥1 dòng "đúng" → dừng lại):

- [ ] Tôi có đang vào lệnh vì sợ bỏ lỡ, thay vì vì checklist đã hoàn tất không?
- [ ] Entry này có nằm ở phía Premium/Discount SAI so với hướng lệnh không?
- [ ] Tôi có thể chỉ ra POI cụ thể mà giá đang phản ứng, hay giá đang ở "vùng trống"?
- [ ] Nếu bỏ lỡ lệnh này, liệu có còn setup khác trong ngày/tuần không? (Câu trả lời luôn là "có".)

![[FOMO-Sec-02-BieuHien.svg|760]]
*Sơ đồ: bảng đối chiếu tell tâm lý (trái) và tell kỹ thuật (phải) — chỉ cần 1 tell đỏ mỗi bên là đủ để đánh dấu "no-trade".*

---

## 3. Cơ chế & Vì sao nguy hiểm

FOMO nguy hiểm vì nó khai thác trực tiếp cơ chế thưởng-phạt của não bộ: nỗi đau khi thấy người khác (hoặc chính mình) kiếm được tiền mà mình đứng ngoài, mạnh hơn cả nỗi sợ thua lỗ. Chính vì thế nó vượt qua được lý trí ngay cả với trader có kiến thức tốt.

Về mặt cấu trúc thị trường, entry FOMO gần như luôn xảy ra ở giai đoạn muộn nhất của một con sóng — nơi có ba vấn đề chồng lên nhau:

1. **Sai vị trí (Premium/Discount).** Một con sóng tăng đã chạy xa nghĩa là giá đang ở Premium. Mua ở Premium là mua đắt — đi ngược nguyên tắc [[27 - Premium Discount]]. Bạn đang mua nơi smart money muốn bán.
2. **Sai thời điểm (draw on liquidity đã cạn).** Nếu con sóng đã quét xong pool thanh khoản mục tiêu (BSL/ERL), thì "nhiên liệu" kéo giá đi tiếp đã hết. Không còn draw on liquidity rõ ràng phía trước nghĩa là không có lý do thuật toán nào để giá tiếp tục. Xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]].
3. **Sai SL (buộc phải rộng).** Vì vào giữa/cuối sóng, không có mốc cấu trúc gần để đặt SL, bạn buộc phải nới SL rộng để tránh nhiễu — làm RR sụp đổ và thường kéo theo vi phạm quy tắc rủi ro.

**Bạn trở thành thanh khoản thoát hàng (exit liquidity).** Đây là điểm cốt lõi: lệnh mua FOMO của đám đông ở đỉnh chính là đối ứng mà smart money cần để chốt lời khối lượng lớn của họ. Bạn không giao dịch *cùng* SM — bạn đang *cung cấp* cho họ chính xác lượng lệnh mua họ cần để bán ra. Xem [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]].

![[FOMO-Sec-03-CoChe.svg|760]]
*Sơ đồ: sóng tăng hoàn tất mục tiêu BSL → SM phân phối → lệnh mua FOMO đổ vào làm đối ứng → đảo chiều, entry FOMO sai cả vị trí, thời điểm lẫn SL.*

**Đối với tài khoản prop firm (FTMO / The5ers):** FOMO là một trong những cơ chế phổ biến nhất dẫn tới breach. Nó thường đi kèm ba lỗi khác cùng lúc — SL rộng (vi phạm risk cap), overtrading (vào nhiều lệnh đuổi trong một phiên), và revenge trading (FOMO sau khi bỏ lỡ → thua → càng FOMO). Một chuỗi 2-3 entry FOMO liên tiếp với SL rộng đủ để chạm daily loss limit của gói 10K.

---

## 4. Ví dụ minh họa

### ✅ Đúng — bỏ lỡ sóng đầu, chờ pullback về POI

Giá tạo một con sóng tăng mạnh (sóng 1). Tôi *bỏ lỡ* nó vì chưa có setup — và điều đó hoàn toàn ổn. Thay vì đuổi theo, tôi chờ giá pullback về vùng Discount, nơi có một FVG/OB hợp lệ (POI). Tại POI đó xuất hiện một MSS trên khung nhỏ (LTF) xác nhận phe mua quay lại. Tôi vào lệnh tại POI, SL đặt chặt dưới POI/điểm sweep, target là BSL phía trên.

![[FOMO-Example-Correct.svg|760]]
*Sơ đồ: bỏ lỡ sóng 1 → chờ pullback về Discount FVG/OB → MSS LTF xác nhận → entry tại POI, SL chặt, target BSL.*

**Vì sao đúng:** Entry là kết quả của một quy trình, không phải của cảm xúc. Vào tại Discount nghĩa là mua rẻ (đúng phía Premium/Discount), có POI để neo SL chặt (RR cao), và có draw on liquidity thật (BSL) phía trước làm mục tiêu. Bỏ lỡ sóng đầu không phải là mất mát — nó là cái giá bình thường để chờ một entry có xác suất cao.

### ❌ Sai — đuổi nến xanh lớn tại đỉnh

Giá đã đi 5-6 nến tăng liên tiếp. Tôi thấy một nến xanh thân lớn và nghĩ "momentum quá mạnh, phải vào" — nhảy vào mua ngay trên nến đó, ở đúng vùng Premium, không có POI phía trước, SL đặt rộng dưới đáy vài nến. Ngay nến thứ hai sau entry, giá đảo chiều và quét SL trước khi thực sự giảm sâu.

![[FOMO-Example-Wrong.svg|760]]
*Sơ đồ: đuổi nến xanh lớn nhất tại đỉnh Premium → đảo chiều tức thì → SL rộng bị quét ở nến thứ hai.*

**Bài học:** Nến displacement lớn nhất thường là nến *cuối* của một con sóng — nơi lực mua cạn kiệt và SM hoàn tất phân phối. Momentum không phải tín hiệu vào lệnh; nó thường là tín hiệu con sóng *sắp kết thúc*. Đây chính là [[Loss - 01 - Trade 2026-06-20 NAS100 Long]] (xem mục 8).

---

## 5. Kiến thức nâng cao (Advanced)

![[FOMO-Advanced-Reflexivity.svg|760]]
*Sơ đồ: vòng lặp reflexivity (displacement → đám đông thấy "rõ ràng phải mua" → SM phân phối → đảo chiều) và bản đồ Premium/Discount cho thấy sức hấp dẫn FOMO tỷ lệ nghịch với edge thực tế.*

### 5.1. Liquidity Reflexivity — FOMO được thiết kế, không ngẫu nhiên

FOMO không phải là điểm yếu ngẫu nhiên của riêng bạn; nó là một cơ chế *có thể dự đoán và khai thác được* của thị trường. Nguyên lý [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]: khi một chuyển động giá càng trở nên "hiển nhiên" với số đông (displacement mạnh + tin tức + mọi người trên mạng xã hội đều nói cùng một hướng), thì càng nhiều lệnh muộn của đám đông tích tụ về phía đó — và đó chính là pool thanh khoản mà smart money cần để đảo chiều. Quy tắc thực hành: **mức độ "hiển nhiên phải vào" tỷ lệ thuận với mức độ gần đỉnh/đáy.** Khi bạn cảm thấy chắc chắn nhất, hãy nghi ngờ nhất.

### 5.2. FOMO vs continuation entry hợp lệ — ranh giới

Không phải mọi entry vào một con sóng đang chạy đều là FOMO. Có tồn tại **continuation entry hợp lệ**: vào một FVG/OB continuation trong cùng một leg sau khi MSS gốc đã rõ ràng. Ranh giới phân biệt:

- **Continuation hợp lệ:** giá pullback về một POI *chưa được mitigate* trong leg, bạn vào *tại* POI đó (mua ở phần chiết khấu của pullback), có MSS/cấu trúc rõ ràng đứng sau, và vẫn còn draw on liquidity phía trước.
- **FOMO:** bạn vào *giữa khoảng trống* giữa các POI (không tại POI nào), đuổi theo nến đang chạy, không có điểm chiết khấu, và thường draw on liquidity đã bị quét.

Bài kiểm tra một câu: *"Tôi đang vào TẠI một POI, hay đang vào GIỮA hai POI?"* Nếu là "giữa", gần như chắc chắn là FOMO.

### 5.3. News-driven FOMO và Judas swing

Các cú spike do tin tức (NFP, CPI, FOMC) là bẫy FOMO cổ điển. Displacement do tin thường tạo cảm giác "cơ hội ngàn năm có một", nhưng phần lớn các cú spike đầu tiên sau tin là **Judas swing** — cú đẩy sai hướng để quét thanh khoản trước khi đảo chiều theo bias thật. Vào FOMO ngay trên cú spike tin tức = vào đúng đỉnh Judas. Nguyên tắc: sau tin, *chờ* cấu trúc lắng lại và một MSS hợp lệ trong [[18 - Kill Zones]] rồi mới hành động; không giao dịch trên nến tin đầu tiên.

### 5.4. OTE — công cụ chống FOMO bằng cấu trúc

[[26 - OTE - Optimal Trade Entry]] (vùng retracement 62%-79% của một leg impulse) là liều thuốc giải kỹ thuật cho FOMO: nó buộc bạn chỉ vào lệnh khi giá đã *hồi về* một vùng chiết khấu định lượng được, thay vì đuổi theo phần impulse. Nếu bạn thấy mình muốn vào ở phần 0%-38% của một leg (tức phần đã chạy), đó là tín hiệu FOMO; OTE nhắc bạn chờ về 62%-79%.

### 5.5. Cơ chế thần kinh & cửa sổ 90 giây

FOMO là một đợt kích hoạt cảm xúc (amygdala) áp đảo vỏ não trước trán (lý trí). Về mặt sinh lý, đỉnh của một đợt bốc cảm xúc thường kéo dài khoảng **60-90 giây** rồi bắt đầu hạ. Đây là cơ sở cho một guardrail cực kỳ hiệu quả: khi cảm thấy FOMO, *bắt buộc* đặt tay rời chuột và đợi 90 giây trước khi được phép bấm lệnh. Trong phần lớn trường hợp, "cơ hội" đó hoặc đã biến mất (chứng minh nó không phải setup thật), hoặc giá đã pullback về một điểm vào hợp lý hơn (biến FOMO thành entry có cấu trúc).

### 5.6. FOMO của việc "bỏ lỡ" vs FOMO của việc "gỡ" — phân biệt với revenge

FOMO thuần túy (sợ bỏ lỡ lợi nhuận) và revenge trading (muốn gỡ lại lệnh vừa thua) là hai trạng thái khác nhau nhưng thường trộn vào nhau và cộng hưởng: bỏ lỡ → tự trách → thấy sóng khác → FOMO để "bù"; hoặc thua → cay cú → FOMO vào lệnh kế tiếp để gỡ. Khi hai lỗi này xuất hiện cùng lúc, mức độ nguy hiểm nhân lên. Xem [[01 - Mistake - Emotional revenge trade]] để nhận diện nhánh revenge.

---

## 6. Best Practices

> [!success] Best Practices
> 1. Áp dụng quy tắc "cửa sổ 90 giây": khi cảm thấy FOMO, rời tay khỏi chuột, đợi tối thiểu 90 giây trước khi được phép hành động.
> 2. Trước mỗi entry, tự hỏi: "Tôi đang vào TẠI một POI, hay GIỮA hai POI?" — nếu "giữa", không vào.
> 3. Chỉ mua ở Discount, chỉ bán ở Premium; từ chối mọi entry mua ở Premium bất kể momentum trông mạnh đến đâu.
> 4. Luôn xác định draw on liquidity (POI mục tiêu) trước khi vào — nếu không chỉ ra được mục tiêu phía trước, không có lệnh.
> 5. Không giao dịch trên nến tin đầu tiên; chờ cấu trúc lắng và MSS hợp lệ trong kill zone.
> 6. Dùng OTE (62%-79% retracement) như bộ lọc cứng: chỉ vào khi giá đã hồi về vùng chiết khấu, không đuổi phần impulse.
> 7. Ghi lại mọi lần "suýt FOMO" (kể cả khi không vào) vào journal — biến sự kiềm chế thành dữ liệu để củng cố phản xạ.
> 8. Nhắc bản thân câu thần chú: "Luôn còn sóng sau." Thị trường tạo cơ hội mới mỗi phiên; bỏ lỡ một lệnh không bao giờ là thảm họa.

---

## 7. Rule phòng tránh & Checklist

- [ ] Không vào lệnh nếu quyết định được kích hoạt bởi cảm giác "sợ bỏ lỡ" thay vì checklist hoàn tất.
- [ ] Không mua ở Premium / không bán ở Discount, bất kể momentum.
- [ ] Xác định được POI cụ thể mà giá đang phản ứng — không vào ở "vùng trống" giữa các POI.
- [ ] Chỉ ra được draw on liquidity (mục tiêu) phía trước trước khi vào.
- [ ] Áp dụng cửa sổ chờ 90 giây khi phát hiện tín hiệu FOMO.
- [ ] Không giao dịch trên nến tin đầu tiên (news spike); chờ MSS trong kill zone.
- [ ] SL phải neo vào một mốc cấu trúc gần (POI/sweep) — nếu buộc phải nới rộng để "theo giá", đó là FOMO, bỏ qua.
- [ ] Kiểm tra chéo với trạng thái revenge (mục 5.6) — nếu vừa thua/vừa bỏ lỡ, tăng cảnh giác gấp đôi.

---

## 8. Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-20 NAS100 Long]]
-

> [!info] Định dạng liên kết trade
> Khi thêm ví dụ thật, dùng đúng định dạng filename của vault: `[[Result - NN - Trade YYYY-MM-DD SYMBOL Position]]` (Result = Win/Loss/BE).

---

## 9. Flashcards / Active Recall

**Q1:** FOMO Entry khác gì với lỗi "vào trước khi sweep" về mặt thời điểm?
**A1:** "Vào trước sweep" là vào *sớm* (thanh khoản chưa bị quét); FOMO là vào *muộn* (sweep đã xong, displacement đã đi phần lớn đường, draw on liquidity gần cạn). Cả hai đều sai thời điểm nhưng ở hai đầu đối nghịch của trục thời gian.

**Q2:** Vì sao entry FOMO thường "sai cả ba"?
**A2:** Sai vị trí (vào ở Premium khi mua / Discount khi bán = mua đắt bán rẻ), sai thời điểm (draw on liquidity đã cạn, hết nhiên liệu), và sai SL (không có mốc cấu trúc gần nên buộc nới rộng, phá RR và risk cap).

**Q3:** "Người FOMO là exit liquidity" nghĩa là gì?
**A3:** Lệnh mua muộn của đám đông ở đỉnh chính là đối ứng mà smart money cần để chốt lời khối lượng lớn. Bạn không giao dịch cùng SM — bạn cung cấp cho họ chính lượng lệnh họ cần để phân phối.

**Q4:** Bài kiểm tra một câu để phân biệt FOMO với continuation entry hợp lệ là gì?
**A4:** "Tôi đang vào TẠI một POI hay GIỮA hai POI?" Vào tại một POI chưa mitigate trong pullback là continuation hợp lệ; vào giữa khoảng trống giữa các POI, đuổi theo nến đang chạy, là FOMO.

**Q5:** Vì sao "cửa sổ 90 giây" hiệu quả?
**A5:** Đỉnh của một đợt bốc cảm xúc thường kéo dài 60-90 giây rồi hạ. Chờ 90 giây cho phép vỏ não trước trán (lý trí) giành lại quyền kiểm soát; thường "cơ hội" hoặc biến mất (chứng minh không phải setup thật) hoặc giá đã hồi về điểm vào hợp lý hơn.

**Q6:** Vì sao OTE là công cụ chống FOMO?
**A6:** OTE (62%-79% retracement) buộc bạn chỉ vào khi giá đã *hồi về* vùng chiết khấu định lượng được, thay vì đuổi theo phần impulse (0%-38%). Muốn vào ở phần đã chạy chính là tín hiệu FOMO.

---

## 10. Lesson Learned

Cốt lõi của FOMO là một sự nhầm lẫn về khan hiếm: não bộ coi cơ hội giao dịch như tài nguyên hữu hạn sắp cạn, trong khi thực tế thị trường tạo ra cơ hội mới mỗi phiên, mỗi ngày, mỗi tuần. Sự khan hiếm thật sự không nằm ở cơ hội — nó nằm ở **vốn** và ở **kỷ luật**. Mỗi lần đuổi theo một con sóng là một lần đánh đổi hai tài nguyên khan hiếm thật (tiền + sự tự chủ) để lấy một tài nguyên dồi dào giả (một cơ hội trong vô số cơ hội).

Đối với hành trình prop firm, sửa FOMO không chỉ cải thiện một chỉ số — nó gỡ bỏ đồng thời ba cơ chế breach phổ biến nhất (SL rộng, overtrading, revenge). Một trader kiểm soát được FOMO gần như tự động thỏa mãn các yêu cầu về consistency và drawdown mà FTMO/The5ers đặt ra.

Quy tắc cá nhân:
- [ ] Không bao giờ vào lệnh khi cảm giác "sợ bỏ lỡ" là lý do chính; chờ 90 giây.
- [ ] Chỉ vào TẠI một POI ở đúng phía Premium/Discount, không vào giữa khoảng trống.
- [ ] Luôn xác định draw on liquidity phía trước trước khi bấm lệnh.

> Bỏ lỡ một con sóng là chuyện bình thường của nghề; đuổi theo nó mới là tai nạn. Thị trường không bao giờ hết sóng — chỉ có tài khoản là có thể hết tiền.

---

## 11. Liên kết

**Concepts:** [[27 - Premium Discount]] · [[26 - OTE - Optimal Trade Entry]] · [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] · [[15 - Inducement]] · [[18 - Kill Zones]] · [[19 - Liquidity]]

**Mistakes liên quan:** [[02 - Mistake - Enter before liquidity sweep]] · [[01 - Mistake - Emotional revenge trade]] · [[06 - Mistake - Not Have Market Structure Shift]] · [[07 - Mistake - Risk more than 0.5% total account]]
