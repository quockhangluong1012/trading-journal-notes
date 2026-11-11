---
type: mistake
category: execution
severity: high
related_model: "[[03 - Playbooks/3.2 - Setups/ICT 2022 Model|ICT 2022 Model]]"
frequency: 1
status: active
tags:
  - trading/ict/mistake
  - trading/review
created: 2026-06-18
updated: 2026-07-08
---

# Mistake - Entry When MSS not in POI Zone

> [!summary] Tóm tắt 1 câu
> Vào lệnh khi mô hình entry ICT 2022 (sweep + displacement + MSS + FVG) trông "đúng bài" về mặt kỹ thuật, nhưng MSS lại xảy ra ở giữa dealing range — không nằm trong vùng POI HTF/H1 hợp lệ — nghĩa là có confirmation mà không có địa chỉ (location) để confirmation đó có ý nghĩa.

> [!danger] Nguyên tắc cốt lõi
> **POI là địa chỉ, MSS là xác nhận.** Một xác nhận (MSS) không có địa chỉ (POI hợp lệ) là một xác nhận vô chủ — nó không cho biết ai đang bảo vệ mức giá đó, và vì vậy không có gì đảm bảo "sự đảo chiều" sẽ được duy trì.

## 1. Mô tả lỗi

Đây là lỗi tinh vi nhất trong nhóm execution, vì bề ngoài trade vẫn "đủ điều kiện" theo checklist ICT 2022: có liquidity sweep, có displacement, có MSS, có FVG để entry. Vấn đề không nằm ở việc **thiếu** một thành phần nào của mô hình — vấn đề nằm ở **vị trí** nơi mô hình đó xảy ra.

- Giá quét một pool thanh khoản nhỏ (local high/low, đôi khi chỉ là equal highs/lows nội bộ), tạo displacement, tạo MSS, tạo FVG — toàn bộ chuỗi sự kiện nhìn giống hệt một entry chuẩn.
- Nhưng chuỗi sự kiện này diễn ra ở **giữa dealing range**, quanh vùng equilibrium (50%), **không phải** tại một OB/FVG HTF (H4/H1) đã được xác định trước là POI hợp lệ.
- Nói cách khác: tôi có **entry model** (cách vào lệnh) nhưng không có **location context** (vào lệnh ở đâu thì có ý nghĩa). Một mô hình entry tách rời khỏi POI chỉ là một tín hiệu kỹ thuật trống rỗng.
- Đây là lỗi khác — và nguy hiểm hơn — so với việc hoàn toàn không có MSS. Ở đây MSS có thật, chỉ là nó xác nhận nhầm chỗ.

![[MSSPOI-Sec-01-MoTa.svg|760]]
*Sơ đồ: cùng một chuỗi sweep → displacement → MSS → FVG, nhưng bên trái xảy ra tại POI H1 hợp lệ trong discount, bên phải xảy ra ở vùng EQ giữa range — không có POI nào phía sau để "bảo chứng" cho MSS.*

## 2. Biểu hiện & Dấu hiệu nhận biết

Bảng tự kiểm tra nhanh — nếu không trả lời được cột "Có" cho câu hỏi đầu tiên, dừng lại trước khi phân tích tiếp:

| Câu hỏi | Dấu hiệu lỗi (Không/Không rõ) | Dấu hiệu an toàn (Có) |
|---|---|---|
| Có thể nêu tên chính xác POI (HTF/H1 OB hay FVG cụ thể, mốc giá cụ thể) mà MSS này đang phản ứng không? | Không nêu được, chỉ nói "giá đảo chiều" | Nêu được: "Bullish OB H1 tại vùng X, được tạo bởi displacement ngày Y" |
| Entry nằm ở đâu trong dealing range (theo % Premium/Discount)? | Quanh 45–55%, sát đường EQ | Discount sâu (long) hoặc Premium sâu (short), thường 62–79% hoặc hơn |
| Swing bị quét để tạo MSS là gì? | Micro-swing ngẫu nhiên trong nội bộ phiên, không liên quan draw on liquidity | Swing gắn với một liquidity pool đã xác định trước (equal highs/lows, sweep của session trước) |
| POI có unmitigated (chưa từng bị test lại) không? | Không kiểm tra, hoặc POI đã bị mitigate trước đó | Còn nguyên, lần đầu giá quay lại |
| Timeframe tạo ra POI có đủ "trọng lượng" so với timeframe entry không? | Dùng M5 làm cả POI lẫn entry | POI đến từ H4/H1, entry refine xuống M5/M1 |
| MSS này có nằm cùng hướng với draw on liquidity của HTF không? | Ngược hoặc không rõ | Cùng hướng, dẫn tới BSL/SSL hoặc PD array kế tiếp hợp lý |

Checklist nhanh trước khi bấm entry:
- [ ] Tôi đã đánh dấu POI HTF/H1 **trước khi** thấy MSS xảy ra (không phải vẽ ngược lại sau khi đã thấy giá đảo chiều)
- [ ] MSS xảy ra **bên trong hoặc ngay sau khi chạm** vùng POI đó, không phải ở khoảng trống giữa range
- [ ] Tôi có thể chỉ ra entry đang ở phần Premium hay Discount nào của dealing range hiện tại

![[MSSPOI-Sec-02-BieuHien.svg|760]]
*Sơ đồ: checklist trực quan — vị trí MSS trong range quyết định đây có phải setup hợp lệ hay chỉ là nhiễu giữa EQ.*

## 3. Cơ chế & Vì sao nguy hiểm

Về bản chất thị trường, một MSS chỉ có ý nghĩa khi nó xảy ra tại nơi có **smart money footprint** — tức là tại một OB/FVG nơi displacement gốc cho thấy có lệnh tổ chức lớn được đặt. Khi MSS xảy ra giữa range, không tại vị trí đó, nó thường chỉ là:

1. **Internal repricing / pullback bình thường** — giá đang điều chỉnh trong nội bộ một leg lớn hơn, không phải đảo chiều thật. Xác suất tiếp diễn theo hướng cũ vẫn cao hơn xác suất đảo chiều.
2. **Induced mini-MSS** — thuật toán tạo ra một cú shift nhỏ ở giữa range (thường bằng cách quét một vài equal highs/lows nội bộ) để dụ các trader theo mô hình ICT 2022 vào lệnh sớm. Sau khi các lệnh chờ (SL của nhóm này) đã nằm sẵn ở đúng chỗ, giá tiếp tục di chuyển về **POI thật** — nơi có draw on liquidity thực sự — và quét sạch các SL vừa được đặt trên đường đi.
3. **Không có ai bảo vệ mức giá** — vì không có OB/FVG HTF nào tại đó, không có lý do cấu trúc để tổ chức bảo vệ vùng giá này. MSS xảy ra do dòng lệnh ngắn hạn (thường là retail hoặc thanh khoản mỏng), dễ bị áp đảo ngược lại chỉ bằng một đợt lệnh nhỏ tiếp theo.

Hệ quả: **RR nhìn đẹp trên biểu đồ nhưng expectancy thực tế âm hoặc rất thấp**, vì:
- Entry ở giữa range thường có SL đặt ngay dưới/trên một swing yếu → dễ bị quét bởi noise bình thường.
- Take profit hướng tới cùng draw on liquidity với "POI thật", nghĩa là chính lệnh của tôi là thanh khoản mà giá cần quét trước khi đi đúng hướng phân tích ban đầu — tôi đang bị stop-out ngay trước khi đúng hướng.
- Vì pattern "nhìn đủ điều kiện", trader vẫn vào full size như một setup A+ — đây là **rò rỉ expectancy âm thầm**, không bị phát hiện nếu không tách riêng biến "MSS có nằm trong POI hay không" khi review.

![[MSSPOI-Sec-03-CoChe.svg|760]]
*Sơ đồ: đường đi thật của giá — mini-MSS giữa range dụ entry, quét SL, rồi mới tới POI thật và đảo chiều đúng nghĩa.*

## 4. Ví dụ minh họa

### ✅ Đúng — MSS xác nhận tại POI hợp lệ trong Discount

Chuỗi sự kiện: giá được deliver xuống một **bullish OB/FVG H1** nằm sâu trong vùng **Discount** của dealing range (dưới 50% EQ, lý tưởng quanh OTE 62–79%). Tại đây, giá quét một **SSL** cục bộ (equal lows hoặc old low), sau đó displacement mạnh lên kèm MSS phá vỡ swing high gần nhất **ngay bên trong/ngay sau khi rời POI**, tạo FVG mới trên M5/M1 để entry. Stop loss đặt dưới POI/điểm sweep, target hướng tới BSL — draw on liquidity phía trên.

![[MSSPOI-Example-Correct.svg|760]]
*Sơ đồ: POI H1 trong Discount → sweep SSL → displacement + MSS ngay tại POI → FVG entry → target BSL.*

**Vì sao đúng:**
- POI được xác định **trước** khi có phản ứng, dựa trên cấu trúc H1 chứ không phải vẽ hồi tố.
- MSS xảy ra đúng tại vị trí có origin displacement rõ ràng (OB/FVG chưa bị mitigate).
- Vị trí trong range là Discount sâu — phù hợp với bias long, không phải mua đuổi ở EQ.
- Draw on liquidity phía trên (BSL) hợp lý với hướng entry — có "lý do" cho giá tiếp tục.

### ❌ Sai — MSS giữa range, không có POI phía sau

Chuỗi sự kiện: giá dao động quanh vùng EQ (45–55%) của dealing range trong phiên, tạo một swing nhỏ, quét vài tick qua equal lows nội bộ (không liên quan gì đến pool thanh khoản lớn), bật lên tạo MSS M5 và FVG. Trader vào long ngay tại FVG này vì "đủ điều kiện mô hình". Thực tế đây chỉ là pullback nội bộ của một leg giảm lớn hơn — giá tiếp tục đi xuống, quét đúng SL vừa đặt, rồi mới thật sự đảo chiều tại **POI H1 thật** nằm sâu hơn.

![[MSSPOI-Example-Wrong.svg|760]]
*Sơ đồ: mini-MSS tại EQ dụ entry long, SL bị quét, giá tiếp tục xuống đúng POI H1 thật mới đảo chiều.*

**Bài học:**
- "Pattern đẹp" không thay thế được câu hỏi vị trí — luôn hỏi "MSS này đang phản ứng với POI cụ thể nào?" trước khi hỏi "mô hình entry đã đủ chưa?".
- Nếu không nêu tên được POI HTF/H1 cụ thể, mặc định coi MSS đó là nhiễu nội bộ (internal), không phải tín hiệu đảo chiều.
- Trade này chính là [[Loss - 01 - Trade 2026-06-18 NDX Short]] — được ghi lại chi tiết ở mục 8.

## 5. Kiến thức nâng cao (Advanced)

![[MSSPOI-Advanced-POIValidity.svg|760]]
*Sơ đồ: 5 tiêu chí xác định một POI hợp lệ trước khi tin vào MSS xảy ra tại đó.*

### 5.1. Tiêu chí POI hợp lệ (POI Validity Criteria)

Một vùng chỉ được coi là POI đủ điều kiện làm địa chỉ cho MSS khi thỏa đồng thời:

1. **Có origin displacement** — vùng đó được tạo ra bởi một cú di chuyển giá mạnh, dứt khoát (không phải nến doji lình xình).
2. **Unmitigated** — chưa từng bị giá quay lại lấp đầy/test kể từ khi hình thành; POI đã bị chạm và mitigate một lần có xác suất phản ứng thấp hơn nhiều ở lần thứ hai.
3. **Đúng vị trí Premium/Discount** — POI cho long phải nằm trong Discount của dealing range hiện hành, POI cho short phải nằm trong Premium; một OB "đẹp" nhưng nằm sai phía EQ không đủ điều kiện.
4. **Aligned với draw on liquidity** — phía sau POI phải có một đích thanh khoản hợp lý (BSL/SSL, PDH/PDL) để giải thích "tại sao giá cần đi tới đó".
5. **Timeframe đủ trọng lượng** — với entry M5/M1, POI nên đến từ H4/H1 trở lên; một "OB" tự vẽ trên M5 không đủ trọng lượng để làm địa chỉ cho một MSS quan trọng.

### 5.2. "MSS bên trong một POI" vs "MSS tạo ra POI mới"

Cần phân biệt hai vai trò khác nhau của MSS:

- **MSS bên trong POI đã biết**: POI H1 được đánh dấu từ trước; giá đến, MSS xảy ra ngay tại/ngay sau vùng đó → đây là **confirmation của POI đã có**, an toàn để entry.
- **MSS tạo ra POI mới**: MSS là chính hành động phá vỡ cấu trúc, và OB/FVG được tạo ra bởi cú displacement của MSS đó lại trở thành POI cho lần retest tiếp theo (ví dụ dùng làm continuation entry). Đây là dùng MSS để **định nghĩa** một POI mới, không phải xác nhận một POI cũ.

Lỗi trong note này xảy ra khi trader nhầm lẫn hai vai trò: coi một MSS giữa range (không liên quan tới POI nào cả) như thể nó đang "xác nhận" một điều gì đó, trong khi thực chất nó không thuộc cả hai nhóm trên — nó không xác nhận POI cũ (vì không có POI ở đó) và cũng không đủ ý nghĩa để tạo POI mới (vì không nằm ở vị trí premium/discount hợp lý, không gắn với liquidity đáng kể).

### 5.3. MTF POI refinement / Nested POI

Quy trình chuẩn: xác định POI trên HTF (H4/H1) trước → khi giá đến vùng đó, hạ xuống LTF (M5/M1) để tìm FVG/OB **nested** — tức là POI nhỏ hơn nằm bên trong vùng POI lớn — và MSS trên LTF phải xảy ra bên trong ranh giới của POI lớn đó. MSS xảy ra ngay trước khi giá chạm đủ sâu vào vùng H1 (còn cách xa CE của POI lớn) vẫn nên được xem là sớm/chưa đáng tin, vì "địa chỉ" chưa thực sự được viếng thăm.

### 5.4. Bẫy Equilibrium (Equilibrium Trap)

Vùng quanh 50% EQ của dealing range là nơi có xác suất đảo chiều gần như ngẫu nhiên (~50/50) vì đây là điểm cân bằng giữa buyer và seller, không nghiêng về phía nào. Bất kỳ MSS nào xảy ra sát EQ mà không có POI hỗ trợ đều mang expectancy gần bằng 0 hoặc âm sau khi trừ chi phí (spread, slippage, SL bị quét). Dùng đường 50% như một **bộ lọc**: nếu entry nằm trong dải 45–55% của range và không có POI HTF trùng khớp, mặc định bỏ qua bất kể mô hình nến/FVG trông đẹp thế nào.

### 5.5. Vai trò của Consequent Encroachment (CE)

CE (50% của FVG/OB tạo nên POI) giúp tinh chỉnh hai việc cùng lúc:
- **Điểm entry**: entry tại CE của POI thường cho RR tốt hơn là entry ngay mép ngoài.
- **Đánh giá "MSS có tôn trọng POI hay không"**: nếu giá chỉ chạm mép ngoài POI, chưa từng tiến đến gần CE, mà đã có MSS bật ngược — đây là phản ứng yếu, khả năng cao là liquidity grab tạm thời chứ không phải POI đã thực sự được "kích hoạt". MSS đáng tin hơn nếu giá đã test tới gần hoặc qua CE trước khi shift.

### 5.6. Phân biệt CHoCH thật tại POI vs cú gom thanh khoản nội bộ (internal liquidity grab)

Một CHoCH/MSS thật tại POI thường đi kèm: displacement mạnh hơn hẳn các nến trước đó, volume/momentum tăng rõ rệt, và phá vỡ một swing có ý nghĩa cấu trúc (không phải swing vừa mới hình thành 2-3 nến trước). Ngược lại, một cú gom thanh khoản nội bộ (chỉ để dụ entry) thường có: displacement yếu hơn, phá vỡ một swing "non" mới tạo trong phiên, và không xảy ra tại vùng có origin OB/FVG rõ ràng. Khi nghi ngờ, chờ thêm một nến xác nhận thay vì vào ngay tại nến phá vỡ đầu tiên.

## 6. Best Practices

> [!success] Best Practices
> 1. Luôn xác định và đánh dấu POI HTF/H1 **trước khi** tìm kiếm MSS — không phân tích ngược từ MSS để "tìm ra" POI biện minh.
> 2. Trước mỗi entry, tự hỏi và trả lời được: "MSS này đang phản ứng với POI cụ thể nào, ở mức giá nào?"
> 3. Dùng đường EQ (50%) như bộ lọc cứng: MSS trong dải 45–55% range mà không trùng POI HTF → bỏ qua.
> 4. Kiểm tra POI có unmitigated không trước khi tin vào phản ứng tại đó.
> 5. Refine POI theo MTF: HTF xác định vùng, LTF xác định FVG/OB nested và MSS chính xác bên trong vùng đó.
> 6. Ưu tiên MSS xảy ra sau khi giá đã tiến gần/qua CE của POI hơn là MSS bật ngay tại mép ngoài.
> 7. Ghi chú trong journal biến `MSS_in_POI: yes/no` cho mọi lệnh để lộ diện tỷ lệ thắng thực sự của từng nhóm.
> 8. Nếu không chỉ tên được POI, mặc định coi đó là internal repricing — chỉ quan sát, không giao dịch.

## 7. Rule phòng tránh & Checklist

- [ ] Xác định POI HTF/H1 hợp lệ (unmitigated, đúng phía Premium/Discount, có draw on liquidity phía sau) **trước** khi chờ phản ứng
- [ ] Không coi bất kỳ MSS nào là tín hiệu entry nếu không nêu được tên/mức giá POI mà nó đang xác nhận
- [ ] Không entry nếu vị trí giá đang ở dải 45–55% của dealing range (vùng EQ) trừ khi trùng khớp với một POI HTF đã xác định
- [ ] Refine xuống LTF chỉ sau khi giá đã chạm vùng POI HTF, tìm FVG/OB nested để entry chính xác
- [ ] Kiểm tra swing bị quét để tạo MSS có gắn với một liquidity pool thật (equal highs/lows đã biết, PDH/PDL) hay chỉ là micro-swing ngẫu nhiên
- [ ] Ghi lại trong trade log trường `MSS_in_POI: yes/no` để review định kỳ tỷ lệ thắng theo nhóm
- [ ] Nếu đã vào lệnh và nhận ra sau đó MSS không nằm trong POI — coi đây là vi phạm quy trình dù thắng hay thua, không rationalize kết quả tốt

## 8. Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-18 NDX Short]]
- 

## 9. Flashcards / Active Recall

**Q1:** POI và MSS khác nhau vai trò như thế nào trong mô hình ICT 2022?
**A1:** POI là địa chỉ (nơi có smart money footprint, do displacement gốc tạo ra); MSS là xác nhận (dấu hiệu giá đã phản ứng tại địa chỉ đó). Cần cả hai — thiếu POI, MSS trở thành xác nhận vô chủ.

**Q2:** Vì sao một MSS giữa range (quanh EQ) lại nguy hiểm dù mô hình kỹ thuật vẫn "đủ điều kiện"?
**A2:** Vì tại đó không có ai bảo vệ mức giá (không có OB/FVG HTF), nên MSS thường chỉ là pullback nội bộ hoặc bẫy do thuật toán tạo ra để dụ entry trước khi giá tiếp tục về POI thật, quét SL trên đường đi.

**Q3:** Kể ra 5 tiêu chí để một vùng được coi là POI hợp lệ.
**A3:** (1) Có origin displacement, (2) unmitigated, (3) đúng phía Premium/Discount so với bias, (4) aligned với draw on liquidity, (5) đến từ timeframe đủ trọng lượng (H4/H1 cho entry M5).

**Q4:** Phân biệt "MSS bên trong POI đã biết" và "MSS tạo ra POI mới" như thế nào?
**A4:** MSS bên trong POI đã biết là xác nhận cho một vùng đã đánh dấu từ trước (an toàn để entry ngay). MSS tạo ra POI mới nghĩa là chính cú shift đó tạo ra OB/FVG sẽ dùng làm địa chỉ cho lần retest sau, chứ không phải tín hiệu entry ngay lập tức.

**Q5:** CE (Consequent Encroachment) hỗ trợ đánh giá gì trong bối cảnh lỗi này?
**A5:** CE giúp tinh chỉnh entry (vào tại 50% của POI thay vì mép ngoài) và giúp đánh giá độ tin cậy của MSS — nếu giá chưa từng tiến gần CE mà đã bật ngược, phản ứng đó yếu, nhiều khả năng chỉ là liquidity grab tạm thời.

**Q6:** Cách đơn giản nhất để lộ diện lỗi này khi review journal là gì?
**A6:** Thêm trường `MSS_in_POI: yes/no` vào mỗi trade log và so sánh win rate giữa hai nhóm — nhóm "no" thường có expectancy âm dù pattern nhìn đẹp như nhau.

## 10. Lesson Learned

Mô hình ICT 2022 không phải là một danh sách check-box độc lập — sweep, displacement, MSS, FVG chỉ có ý nghĩa khi được neo vào một POI hợp lệ. Sự cám dỗ lớn nhất của lỗi này là nó **trông giống hệt** một setup A+, khiến trader tự tin vào full size mà không nhận ra mình đang thiếu câu hỏi quan trọng nhất: "giá đang phản ứng với ai?". Kỷ luật thật sự không nằm ở việc nhận diện mô hình entry nhanh, mà ở việc luôn hỏi vị trí (location) trước khi hỏi xác nhận (confirmation). Một "good loss" vì bỏ qua setup không có POI luôn tốt hơn một "bad win" ăn may từ mini-MSS giữa range.

## 11. Liên kết

**Concepts:** [[21 - Market Structure Shift]] · [[25 - OB - Order Block]] · [[13 - FVG  - Fair Value Gap]] · [[27 - Premium Discount]] · [[10 - Consequent Encroachment (Mean Threshold)]] · [[12 - Dealing Range]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]]

**Mistakes liên quan:** [[06 - Mistake - Not Have Market Structure Shift]] · [[02 - Mistake - Enter before liquidity sweep]] · [[09 - Mistake - Wrong daily bias]]

**Model:** [[03 - Playbooks/3.2 - Setups/ICT 2022 Model|ICT 2022 Model]]

---
