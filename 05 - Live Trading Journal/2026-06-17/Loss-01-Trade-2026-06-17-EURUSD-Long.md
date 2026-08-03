---
date: 2026-06-18T17:36:00
symbol: EURUSD
position: Long
entry_price: 1.15907
take_profit: 1.16082
stop_loss: 1.15975
kill_zone:
  - London
pnl: -32
r_multiple:
mistakes: "[[06 - Mistake - Not Have Market Structure Shift]]"
tags:
  - Discount
  - FVG
  - KillZones
  - OrderBlock
  - DealingRange
  - DailyBias
planned_rr:
result: Loss
session: London
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 1, minor: 1}
da_opposite_case: "not viable"
---
# Trade 2026-06-17 - EURUSD Long Loss

## 1. Pre-market Bias
### D1  
- Bias:  Bullish
- Lý do:  giá đang trong nhịp tăng
![[EURUSD-20260617-D1.png]]
### H1  
- Khung H1 giá đang tạo Higher high/ Higer low
- Giá tạo Order Block khung H1
- OB nằm trong vùng Discount khung H1
- Chờ giá retrace về và vào khung nhỏ hơn kiểm tra
![[EURUSD-20260617-H1.png]]
### M5  
- Giá xuất hiện phản ứng khi di chuyển tới OB
- Hình thành các cây nến có râu dài, nến đó bên ngoài hoặc cạnh OB và râu xuyên vào OB gần tới 50% OB
- Xuống khung nhỏ hơn quan sát
![[EURUSD-20260617-M5.png]]
### M1
- Giá phản ứng khi vào vùng OB
- Giá có cú displacement và hình thành FVG
- Vào lệnh khi giá quay về vùng FVG
  ![[EURUSD-20260617-M1.png]]
## 2. Phân tích sau lệnh:
- **Result**: Hit ==stoploss==
- **Mistake**: [[06 - Mistake - Not Have Market Structure Shift]]
- **Lý do**: Vào đuổi giá vì sợ lỡ mất nhịp giá. Khi dó giá chạm PD Array và xuất hiện displacement, tuy nhiên không có MSS. Tôi bỏ qua một điều kiện xác định quan trọng và vào lệnh Long trong khi các khung M15/M5 là nhịp giá giảm
- Không check các tin tức quan trọng của ngày

## 4. Phân Tích Sau Lệnh (điền dựa trên dữ kiện có trong file)

File gốc không có section 3 (Execution Review) hay checklist — chỉ có mục 2 ở trên. Dựa trên narrative đã có: bias D1 Bullish trong khi M15/M5 "là nhịp giá giảm" (tự nhận trong mục 2) là bias-structure mismatch tại thời điểm entry, không phải suy luận thêm. MSS bị bỏ qua là mistake duy nhất được gắn tag, khớp với narrative "không có MSS". *(Không có checklist pre-trade trong file này để đối chiếu tick — khác với Loss-04, không suy luận thêm phần này.)*

## 5. Lesson Learned

Bài học gốc của user (trong mục 2): "vào đuổi giá vì sợ lỡ mất nhịp", "bỏ qua MSS", "không check tin tức".

### Bài học kỹ thuật
- MSS là điều kiện bắt buộc trước entry, không phải displacement + FVG đơn thuần — displacement không nằm trong khung có MSS xác nhận không tạo mandate cho entry (liên kết O1, CS-O2).
- Bias D1 Bullish nhưng chính user tự ghi M15/M5 là "nhịp giá giảm" tại thời điểm vào lệnh — đây là counter-trend entry trên timeframe thực thi, không chỉ là thiếu MSS đơn lẻ.

### Bài học tâm lý
- FOMO ("đuổi giá vì sợ lỡ mất nhịp") là động cơ entry được tự nhận, không phải suy diễn — đây là root cause tâm lý, MSS chỉ là biểu hiện kỹ thuật của nó (liên kết O1).
- Đây là lệnh đầu tiên trong cụm ngày 17-18/06 theo trình tự trong ngày (cùng giờ với Loss-02) — xem Bối cảnh cụm bên dưới.

### Bài học quy trình & risk
- Không có checklist pre-trade nào trong file này để đối chiếu — không thể kiểm tra liệu FOMO entry có đi qua gate nào trước khi vào lệnh (liên kết CS-O2: rule không có cơ chế thực thi giữa lệnh và lệnh).
- Không check tin tức kinh tế trước killzone London — tự nhận, không có rule "check news" nào được xác nhận đã tồn tại trước lệnh này.

### Rule cần thêm/cập nhật
- Rule kiểm tra được: "Không entry nếu M15/M5 tại thời điểm quyết định đang di chuyển ngược hướng bias D1, bất kể displacement/FVG đã hình thành" — đo bằng: quan sát trực tiếp cấu trúc M15/M5 ngay trước entry, ghi Yes/No, chỉ entry khi No mâu thuẫn với bias.
- Rule kiểm tra được: "Check economic calendar trước mỗi killzone (London/NY), ghi vào journal tick Yes/No" — hiện tại mục này luôn bỏ trống trong toàn cụm 17-18/06.

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, không có screenshot chart (mọi `![[...]]` là link Obsidian không tồn tại). Sufficiency: **thin** — narrative rất ngắn (chỉ 2 mục, không checklist, không Execution Review, không Final Grade). Toàn bộ "OB", "FVG", "displacement", "MSS thiếu" là claim của user.

**Thesis & claims**:
- C1: Bias D1 = Bullish, dựa trên "giá đang trong nhịp tăng" (claim, không evidence).
- C2: OB H1 nằm trong Discount, giá retrace về OB rồi phản ứng ở M5/M1, hình thành FVG.
- C3: Entry Long tại FVG M1 — **load-bearing claim** (đây là hành động thực tế bị đánh giá).
- C4 (tự nhận): không có MSS xác nhận reversal, và M15/M5 đang là nhịp giảm tại thời điểm entry → C3 mâu thuẫn với chính C4.
- C5 (tự nhận): động cơ vào lệnh là FOMO ("đuổi giá vì sợ lỡ nhịp"), không phải theo checklist.

**Điều gì đứng vững**: Nhận diện thiếu MSS và gọi tên đúng root cause (FOMO) là tự-chẩn đoán chính xác theo đúng dữ kiện tự nêu — không có gì trong file mâu thuẫn với nhận định này của chính user.

**Objections**:

**O1 · [METHOD] · fatal · attacks C3 (load-bearing)**
Claim: "displacement + FVG hình thành tại M1 là đủ điều kiện entry."
Fails: chính user tự nhận C4 (không MSS, M15/M5 đang giảm) NGAY SAU KHI vào lệnh — nghĩa là điều kiện entry đã thiếu ngay tại thời điểm quyết định, không phải phát hiện muộn. Đây không phải lỗi chart mà là lỗi quy trình: FVG + displacement được dùng làm đủ điều kiện dù doctrine (theo chính checklist các file khác trong cụm) yêu cầu MSS trước.
Consequence: entry không có structural mandate — kết quả Loss không phải "xấu số" mà là hệ quả trực tiếp của thiếu điều kiện đã biết trước khi vào lệnh.
Your best answer: "displacement mạnh đủ để coi như tín hiệu reversal." — Không cứu được: chính user dùng đúng chữ "không có MSS" để tự chẩn đoán nguyên nhân thua, tức tại thời điểm ghi journal cũng không chấp nhận lý do này.
Retracted by: một MSS thực sự (break structure ngược hướng move giảm) được nêu tên tại thời điểm entry — hiện không có trong narrative.

**O2 · [UNSUPPORTED] · material · attacks C1**
Claim: Bias D1 Bullish "vì giá đang trong nhịp tăng."
Fails: không nêu dealing range, không nêu swing cụ thể nào xác lập "nhịp tăng" — đây là mô tả định hướng chung, không phải xác định bias theo cấu trúc (HH/HL) như doctrine yêu cầu.
Consequence: nếu D1 bias sai (giống Loss-02, Loss-03 cùng cụm đều tự nhận "Sai Bias"), toàn bộ OB Discount phía dưới cũng sai hướng tham chiếu.
Retracted by: nêu swing D1 cụ thể (higher high/higher low) xác lập bias.

**O3 · [DOCTRINE] · minor · attacks C2** — OB "nằm trong vùng Discount khung H1" nhưng không nêu dealing range (high/low) hay midpoint tính premium/discount — không đủ evidence để xác nhận phân loại Discount đúng. Retracted by: nêu high/low của dealing range dùng để tính.

Drafted 4, cut 1 (một draft [CHART] về "râu nến xuyên OB" bị loại vì không có chart để kiểm, không tier hợp lệ).

**Verdict**: **BROKEN** — load-bearing claim C3 (entry hợp lệ) sụp vì chính user tự xác nhận thiếu MSS ngay tại thời điểm entry (O1), không phải hindsight. Tôi đã tấn công quy trình entry (O1) và bias foundation (O2), không phá được vì cả hai đã được chính user tự nhận trong file — không có gì để "phá" thêm, chỉ còn xác nhận. Critique này KHÔNG xác lập được: (a) OB/FVG có thực sự tồn tại trên chart hay không (không có chart), (b) đây có phải lệnh đầu tiên trong cụm revenge hay không về mặt tâm lý (xem Bối cảnh cụm).

**Bối cảnh cụm 17–18/06**: Lệnh này và Loss-02 (GBPUSD) có cùng timestamp frontmatter 2026-06-18T17:36 — cùng session London, khả năng cao là hai lệnh gần như đồng thời hoặc entry rất gần nhau trên hai instrument khác nhau. Nếu Loss-01 xảy ra trước, đây là mắt xích đầu tiên trong chuỗi 4 losses cùng cụm được [cross_setup_findings.md](/home/user/workspace/analysis/cross_setup_findings.md) gọi là revenge/overtrading chain (CS-O4 · [METHOD] · material). Thiếu MSS lặp lại đúng pattern đã bị vi phạm ít nhất 4 lần trước đó theo timeline lesson (CS-O2 · [METHOD] · fatal — trích: "rule được ghi ra nhưng không có cơ chế thực thi nào giữa lệnh và lệnh").

## 9. Opposite Case (Counter-Argument)

Load-bearing claim của kèo ngược: displacement + FVG tại M1 sau khi giá phản ứng ở OB H1 Discount **là** một continuation setup hợp lệ trong nhịp tăng D1 — MSS không bắt buộc nếu OB H1 đã đủ làm PD array chính, vì bias D1 vẫn Bullish (chưa bị user tự phủ định trong file này, khác Loss-02/03 nơi user tự nhận "Sai Bias").

**Tự đánh kèo ngược**: cùng chính user tự ghi "M15/M5 là nhịp giá giảm" tại thời điểm entry — nếu M15/M5 đang giảm, đây không còn là continuation của nhịp tăng D1 mà là counter-trend trên TF thực thi, đúng như C4 đã nêu. Kèo ngược không giải thích được câu tự nhận này.

**Strength label**: **not viable** — không có fact nào trong file mà kèo ngược giải thích được tốt hơn thesis gốc; cả hai đọc đều dựa trên đúng một câu tự nhận "không MSS, M15/M5 giảm" và câu đó chỉ tương thích với thesis gốc (entry sai vì thiếu MSS), không tương thích với continuation-hợp-lệ.

**Observable phân biệt**: swing H1/M15 cụ thể xác nhận đây là continuation thực sự (HH mới sau OB) hay reversal-thất bại — hiện không có trong narrative để phân biệt.

## 10. Falsification Tests

1. Nếu tìm được swing D1 cụ thể (không chỉ mô tả "nhịp tăng") xác nhận HH/HL tại thời điểm 06-17/18 — O2 bị đóng (retracted). Ngược lại O2 giữ nguyên UNSUPPORTED.
2. Nếu có bằng chứng (timestamp chi tiết hơn) cho thấy Loss-01 xảy ra SAU Loss-02 (không phải cùng lúc/trước) — thứ tự trong "Bối cảnh cụm" cần điều chỉnh, nhưng verdict O1 không đổi.
