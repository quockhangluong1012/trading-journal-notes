---
date: 2026-06-18T21:31:00
symbol: NDX
position: Short
entry_price: 30,214.9
take_profit: 29,989.2
stop_loss: 30,323.0
kill_zone: New York
pnl: -32.43
r_multiple:
mistakes: "[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]"
tags:
  - DailyBias
  - KillZones
  - LiquiditySweep
  - OrderBlock
  - FVG
  - Premium
planned_rr: 2.09
result: Loss
session: New York
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 1, minor: 1}
da_opposite_case: "weaker but non-trivial"
---
# Trade 2026-06-17 - EURUSD Long Loss

## 1. Pre-market Bias
### D1  
- Bias:  Bearish
- Lý do:  giá đang trong nhịp Pullback và đang giao dịch bên trong thân nến ngày trước đó
![[NDX-20260618-D1.png]]
### H1  
- Giá tạo quét đỉnh ( Liquidity Sweep), asu đó giá quay ngược trở lại vào range

![[NDX-20260618-H1.png]]

### M5  
-  tôi đã mắc sai lầm khi chỉ chú ý giá quay ngược lại range + displacement + FVG
- Lỗi nghiêm trọng: giá quét thanh khoản tại 1 vùng không có bất kỳ POI nào ( OB, FVG, ..)
![[NDX-20260618-M5.png]]
## 2. Phân tích sau lệnh:
- **Result**: Hit ==stoploss==
- **Mistake**: [[06-Mistake-Not-Have-Market-Structure-Shift]]
- **Lý do**: Thấy giá quét thanh khoản khung H1 khi đó tôi đã xuống ngay khung thời gian nhỏ hơn để tìm điểm vào lệnh mà quên mất ngay vùng đó không có bất kỳ 1 POI nào -> Quá tập trung tìm MSS mà quên mất phải chờ giá retrace về vùng POI sau đó tìm xác nhận

## 4. Phân Tích Sau Lệnh (điền dựa trên dữ kiện có trong file)

File không có checklist/Execution Review — mục 2 gộp phân tích. Nguyên nhân tự nhận rất cụ thể và khác các file EURUSD/GBPUSD cùng cụm: không phải "thiếu MSS" đơn thuần mà là **entry tại vùng không có POI nào** (tự nhận: "giá quét thanh khoản tại 1 vùng không có bất kỳ POI nào (OB, FVG,..)") — khớp đúng với mistake tag frontmatter `[[03-Mistake-Entry-When-MSS-not-in-POI-Zone]]`, dù dòng "Mistake" trong body lại ghi tag khác (`[[06-Mistake-Not-Have-Market-Structure-Shift]]`) — hai tag khác nhau giữa frontmatter và body cho cùng một lệnh *(ghi nhận sự khác biệt, không suy diễn lý do)*. Bias D1 lần này là Bearish (đảo hướng so với Bullish sai của cả 3 lệnh Long ngày 17/06) — và Short đúng theo bias Bearish này, khác các lệnh Long ngày trước đều tự nhận sai bias.

## 5. Lesson Learned

Bài học gốc: quá tập trung tìm MSS mà quên chờ giá về đúng vùng POI trước.

### Bài học kỹ thuật
- Đây là lỗi khác về BẢN CHẤT so với 4 lệnh Long ngày 17/06: không phải "thiếu MSS trước khi entry đúng vùng" mà là "tìm MSS ở đúng vùng không có POI nào cả" — thứ tự quy trình bị đảo (tìm confirmation trước khi xác định đúng zone), không phải bỏ qua một bước (liên kết O1).
- Bias D1 lần này đúng hướng (Bearish, khớp Short) — khác hẳn 3/4 lệnh Long ngày trước tự nhận sai bias — nên lỗi ở đây không nằm ở tầng bias.

### Bài học tâm lý
- Đảo hướng từ Long (4 lệnh liên tiếp ngày 17/06, đều thua) sang Short ngay hôm sau (18/06) — không có gì trong file này tự nhận đây là phản ứng theo 4 losses hôm trước (khác Loss-03, Loss-04 cùng cụm tự gắn tag revenge rõ ràng) — đây là điểm cần nói rõ: không có bằng chứng trực tiếp cho revenge ở lệnh này, chỉ có suy luận gián tiếp từ trình tự thời gian (liên kết O2, và Bối cảnh cụm).
- Không tự nhận FOMO hay revenge trong mistake tag (chỉ có "Entry When MSS not in POI Zone") — khác biệt này tự nó là dữ kiện, không nên bị gộp chung với 4 lệnh trước như cùng một tâm lý.

### Bài học quy trình & risk
- Thứ tự quy trình đúng phải là: xác định POI hợp lệ trước → chờ giá vào đó → mới tìm MSS/confirmation bên trong; lệnh này làm ngược: thấy sweep → nhảy xuống M5 tìm MSS ngay → bỏ qua bước xác nhận đang ở đúng zone.
- Không có checklist trong file này để đối chiếu — giống 3/4 lệnh Long khác trong cụm (chỉ Loss-04 có checklist đầy đủ) — đây là pattern proportionality: lệnh thua "nặng" nhất về hệ quả tâm lý (đứng cuối chuỗi 5 lệnh) không phải là lệnh có journal chi tiết nhất.

### Rule cần thêm/cập nhật
- Rule kiểm tra được: "Khi thấy Liquidity Sweep ở H1, bước tiếp theo BẮT BUỘC là xác định vùng POI cụ thể (OB/FVG) tồn tại tại đúng vùng giá sau sweep — nếu không có POI nào, KHÔNG xuống M5/M1 tìm MSS, dừng lại." — đo bằng: ghi rõ tên/vị trí POI trước khi chuyển timeframe thấp hơn.
- Rule kiểm tra được: "Sau một chuỗi ≥3 lệnh thua liên tiếp cùng ngày hoặc ngày liền trước, bắt buộc ghi rõ trong mục Tâm lý liệu quyết định đảo hướng (Long→Short hoặc ngược lại) có bị ảnh hưởng bởi chuỗi thua đó hay không — không để trống mục này."

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only, không chart. Sufficiency: **thin** — narrative ngắn, không checklist, không Final Grade.

**Thesis & claims**:
- C1: Bias D1 Bearish, đúng hướng theo tự nhận (không bị phủ định trong file, khác 3 lệnh Long ngày trước).
- C2: H1 Liquidity Sweep tại đỉnh → giá quay lại range.
- C3: Entry Short tại M5 dựa trên "quay lại range + displacement + FVG" — **load-bearing claim**.
- C4 (tự nhận): vùng entry không có POI nào (OB/FVG) — trực tiếp phủ định C3 (vì C3 tuyên bố có FVG).
- C5: mistake tag frontmatter (`03 - MSS not in POI Zone`) khác mistake tag trong body (`06 - Not Have MSS`).

**Điều gì đứng vững**: Bias D1 Bearish là điều duy nhất trong toàn cụm 17-18/06 không bị chính user tự phủ định — không có gì trong file mâu thuẫn với việc bias này đúng hướng.

**Objections**:

**O1 · [SELF-CONTRADICTION] · fatal · attacks C3 (load-bearing)**
Claim: "giá quay ngược lại range + displacement + FVG" là cơ sở hợp lệ cho entry Short M5.
Fails: ngay câu tiếp theo trong cùng mục M5, chính user tự phủ định: "Lỗi nghiêm trọng: giá quét thanh khoản tại 1 vùng không có bất kỳ POI nào (OB, FVG, ..)" — nếu không có POI nào, không thể có FVG hợp lệ như câu trước đó tuyên bố. Đây là hai câu liên tiếp tự mâu thuẫn về cùng một sự kiện.
Evidence: đối chiếu trực tiếp 2 dòng trong mục "M5" của chính file.
Consequence: entry không có PD array thật đứng sau — displacement/FVG được "thấy" là nhận diện sai (confirmation bias tìm MSS ở nơi không có setup), không phải PD array hợp lệ bị bỏ qua điều kiện khác (khác các lệnh Long ngày trước — nơi FVG có vẻ tồn tại nhưng thiếu MSS).
Your best answer: "có FVG nhỏ hình thành ngay trong nhịp quay lại, không phải OB lớn khung H1." — Không cứu được: câu tự nhận dùng đúng cụm "không có bất kỳ POI nào" bao gồm cả FVG trong dấu ngoặc liệt kê, không chỉ loại trừ OB.
Retracted by: chart M5 xác nhận có FVG 3-nến hợp lệ tại đúng vùng entry — không có chart nên hiện tại không thể discharge.

**O2 · [METHOD] · material · attacks C4 (Bối cảnh cụm)**
Claim: đảo hướng Long→Short ngày 18/06 là một quyết định độc lập, không liên quan tới 4 losses Long ngày 17/06.
Fails: không có gì trong file này (mistake tag chỉ ghi "03 - MSS not in POI Zone", không có revenge tag) TRỰC TIẾP xác nhận hoặc phủ định điều này — đây là một khoảng trống evidence, không phải một fact đã biết theo chiều nào.
Consequence: nếu đảo hướng là phản ứng cảm xúc với 4 losses hôm trước (giống cách nhảy instrument ngày 17/06 mà không có thesis chung — xem Loss-01/02), thì lỗi "tìm MSS sai vùng" (O1) có thể là hệ quả của việc vào lệnh quá vội theo cùng động lực tâm lý, không phải lỗi kỹ thuật độc lập. Nếu đảo hướng là một quan sát kỹ thuật độc lập và hợp lý (bias Bearish đúng hướng), thì đây là lệnh có nền tảng bias tốt nhất trong cụm nhưng vẫn thua vì lỗi thực thi khác hẳn (POI sai vùng, không phải thiếu MSS).
Retracted by: ghi chú tâm lý (mục Tâm lý, hiện không tồn tại trong file này) xác nhận rõ theo chiều nào — hiện không có.

**O3 · [UNSUPPORTED] · minor** — mistake tag frontmatter ("03 - Entry When MSS not in POI Zone") khác mistake tag trong body ("06 - Not Have MSS") cho cùng một lệnh — không rõ tag nào đại diện đúng cho nguyên nhân chính. Retracted by: xác nhận tag nào được điền sau/là tag chính thức cuối cùng.

Drafted 4, cut 1 (draft [DOCTRINE] về định nghĩa Liquidity Sweep bị loại — user tự dùng đúng, có level cụ thể "đỉnh" được nêu tên, đạt evidence bar tối thiểu theo doctrine sweep, không phải overcall).

**Verdict**: **BROKEN** — load-bearing claim C3 (entry có FVG hợp lệ) tự sụp trong chính hai câu liên tiếp của file (O1, fatal), không cần chart hay suy luận thêm. Tôi tấn công tính nhất quán nội tại của narrative M5 và nguồn gốc tâm lý của quyết định đảo hướng — phá được O1 hoàn toàn, không phá được O2 theo bất kỳ chiều nào (đây là khoảng trống evidence thật, không phải một claim có thể bị bác). Critique này KHÔNG xác lập được: liệu đảo hướng Long→Short có động lực tâm lý từ chuỗi losses hôm trước hay không (O2 để mở), và liệu có FVG thật tồn tại trên chart hay không (cần chart).

**Bối cảnh cụm 17–18/06**: Đây là lệnh thứ 5 và duy nhất ngày 18/06 (theo tên file, dù `date` frontmatter một số lệnh 06-17 khác cũng ghi 06-18 — xem ghi chú date-mismatch ở các file EURUSD/GBPUSD), và duy nhất theo hướng Short sau 4 lệnh Long liên tiếp thua ngày 17/06. Đảo hướng ngay sau một chuỗi losses cùng hướng là dấu hiệu bề mặt phù hợp với overtrading/revenge pattern mà CS-O4 (`[METHOD] · material`) đã gọi tên cho cụm này, nhưng khác với Loss-03/Loss-04 (tự gắn tag revenge trade rõ ràng), file này KHÔNG có bằng chứng tự nhận tâm lý nào — mistake tag duy nhất là kỹ thuật ("MSS not in POI Zone"), không phải cảm xúc. Vì vậy: tự nó có nền tảng kỹ thuật (bias Bearish đúng hướng, sweep H1 có tên level) khác hẳn 4 lệnh Long trước, nhưng thất bại vì một lỗi thực thi cụ thể khác (POI sai vùng, O1) — không thể gộp chung "tất cả 5 lệnh là một chuỗi tâm lý đồng nhất" chỉ vì cùng cụm ngày, đúng như CS-O4 chỉ dùng 2/4 losses có tự-nhận revenge làm evidence, không phải cả 5.

## 9. Opposite Case (Counter-Argument)

Load-bearing claim của kèo ngược: đây KHÔNG phải một entry lỗi thực thi độc lập, mà là hệ quả trực tiếp của trạng thái tâm lý "cố gỡ" kéo dài từ 4 losses ngày trước — tốc độ chuyển từ nhận diện sweep H1 sang entry M5 ("Quá tập trung tìm MSS mà quên mất phải chờ giá retrace về vùng POI") là dấu hiệu hành vi vội vàng đặc trưng của overtrading, không phải lỗi phân tích đơn thuần.

**Tự đánh kèo ngược**: không có tag tâm lý (FOMO/revenge) nào được tự gắn trong file này, khác hẳn Loss-03/04 cùng cụm — nếu đây thực sự là hành vi overtrading do ảnh hưởng tâm lý từ hôm trước, user đã tự gắn tag đó ở 2/4 lệnh khác trong cùng cụm nhưng không gắn ở đây, dù đây là lệnh muộn nhất và có lý do nhiều nhất để bị ảnh hưởng tâm lý.
- Ngược lại, thesis gốc (lỗi thực thi kỹ thuật độc lập, quy trình bị đảo) khớp đúng 100% với mistake tag tự nhận, không cần suy diễn thêm gì.

**Strength label**: **weaker but non-trivial** — thesis gốc (lỗi quy trình kỹ thuật) được evidence trực tiếp ủng hộ mạnh hơn (mistake tag khớp đúng), nhưng kèo ngược (ảnh hưởng tâm lý từ chuỗi losses) vẫn "non-trivial" vì trình tự thời gian (ngay sau 4 losses) là một fact thật không thể loại trừ hoàn toàn chỉ vì thiếu tag tự nhận — thiếu tag không đồng nghĩa không có ảnh hưởng, chỉ đồng nghĩa không có bằng chứng trực tiếp.

**Observable phân biệt**: một ghi chú tâm lý (mục "Tâm lý khi vào lệnh", hiện không tồn tại trong file này, khác format có ở Loss-04) xác nhận rõ có/không bị ảnh hưởng bởi 4 losses hôm trước — hiện không có, nên không thể phân biệt hai reading từ dữ kiện đã cho.

## 10. Falsification Tests

1. Nếu tìm được ghi chú tâm lý (nhật ký khác, không trong 6 file này) xác nhận trạng thái cảm xúc trước entry lệnh này — đóng O2 và xác định lại strength label ở section 9 theo chiều tương ứng.
2. Nếu có chart M5 xác nhận có/không FVG 3-nến hợp lệ đúng tại vùng entry — đóng O1 dứt điểm theo chiều evidence (nếu có FVG thật, O1 narrow thành "FVG có tồn tại nhưng không đủ mạnh"; nếu không, O1 giữ nguyên fatal).
