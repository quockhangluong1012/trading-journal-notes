---
type: ict-concept
concept: OB Mitigation Depth
aliases:
  - Mitigation Depth
  - Shallow vs CE vs Full Mitigation
  - Độ sâu retracement vào Order Block
tags:
  - trading/ict/concept
  - trading/study
  - "#OrderBlock"
  - "#CE"
status: developing
category: PD Array
timeframes:
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
importance: 4
last_reviewed: 2026-07-19
created: 2026-07-19
updated: 2026-07-19
common_mistakes:
  - "[[Mistake - Trade Every Order Block]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
---

# OB Mitigation Depth — Vì sao Shallow, CE, hay Full khác nhau

> [!summary] Tóm tắt 1 câu
> **Độ sâu mà giá retrace vào một Order Block trước khi đảo chiều — chỉ chạm nông (giữa CE và cạnh trên), đúng CE (50%), hay xuyên gần hết tới cạnh dưới — không phải ngẫu nhiên: nó do vị trí nested FVG/OB con, vị trí liquidity pool (SSL/BSL) quanh OB, và vị trí OB trong Premium/Discount của dealing range lớn hơn quyết định.**

> [!important] Nguyên tắc cốt lõi
> **CE (Consequent Encroachment) là kỳ vọng xác suất trung bình, không phải luật vật lý.** Đọc đúng 3 lớp context — nested structure phía trên, liquidity phía dưới, vị trí trong Premium/Discount — mới biết nên kỳ vọng shallow, CE, hay full mitigation cho từng OB cụ thể. Ghi chú này là phần **bổ sung nguyên nhân (causal layer)** cho bảng kịch bản A–E đã có ở [[25 - OB - Order Block]] §7.2 — không lặp lại, mà trả lời câu hỏi "tại sao lại rơi vào kịch bản đó".

---

## 1. Định nghĩa

**Khái niệm:**
OB Mitigation Depth là mức độ sâu mà giá đi vào bên trong một Order Block (tính từ cạnh proximal/gần giá hiện tại tới cạnh distal/xa, tức đáy râu với Bullish OB hoặc đỉnh râu với Bearish OB) trước khi xuất hiện phản ứng đảo chiều đủ mạnh để tiếp tục narrative ban đầu. Phổ độ sâu chia làm 3 vùng tham chiếu:

1. **Shallow** — chỉ chạm vùng giữa CE và cạnh proximal (chưa lấp nửa OB).
2. **CE (50%)** — chạm đúng Mean Threshold, phản ứng "chuẩn" theo lý thuyết.
3. **Full** — đi sâu gần hết hoặc chạm tới cạnh distal (đáy râu), thậm chí wick chọc nhẹ qua mà thân vẫn đóng trong OB.

**Mục đích trong ICT:**
- Giúp trader không áp CE như một luật cứng ("chờ đúng 50% mới vào"), mà đọc được **vì sao** một OB cụ thể có khả năng chỉ cho shallow tap hay đòi hỏi full mitigation.
- Là cơ sở để đặt kỳ vọng entry linh hoạt: aggressive tại nested FVG khi có dấu hiệu shallow, hay kiên nhẫn chờ full mitigation kèm LTF confirmation khi bối cảnh đòi hỏi discount sâu.
- Giúp đặt stop-loss đúng chỗ — tránh bị quét non vì đặt stop sát CE trong khi thực ra cần dự phòng cho một cú full mitigation quét SSL trước.

**Vì sao khái niệm này quan trọng:**
Đây chính là lỗ hổng phổ biến nhất khi trader mới áp dụng CE: xem CE như điểm entry duy nhất hợp lệ, dẫn đến hai loại lỗi đối lập — **bỏ lỡ trade** (giá chỉ shallow tap rồi chạy, không bao giờ về tới CE) hoặc **bị stop non** (đặt stop quá sát CE trong khi giá cần full mitigation quét thanh khoản trước khi đảo chiều thật). Hiểu đúng 3 nguyên nhân gốc giúp phân biệt hai tình huống này trước khi vào lệnh, không phải sau khi đã thua.

**Nó giúp trả lời câu hỏi nào trên chart?**
- OB này có nested FVG/OB con phía trên CE không? Nếu có, giá có thể chỉ cần shallow tap.
- Có liquidity pool (SSL/BSL, equal highs/lows) nằm ngay sát cạnh distal của OB không? Nếu có, khả năng cao giá sẽ đi tới đó trước khi đảo chiều thật.
- OB này nằm ở đâu trong Premium/Discount của dealing range lớn hơn — gần equilibrium hay đã sâu trong discount/OTE?
- Đây là OB tại origin của leg hay OB hình thành giữa leg (mid-leg)?

### OB Mitigation Depth không phải là gì
- Không phải một quy luật cố định kiểu "OB luôn về tới CE" hay "luôn cần full mitigation" — cả hai đều sai nếu áp dụng máy móc.
- Không thay thế cho việc đọc [[25 - OB - Order Block]] §7.2 (bảng kịch bản A–E: touch&go / CE / distal / close-through / breaker) — ghi chú này chỉ trả lời phần "tại sao", còn bảng đó mô tả "hành vi giá trông như thế nào".
- Không phải lý do để bỏ LTF confirmation — dù dự đoán đúng độ sâu, vẫn cần MSS/displacement LTF trước khi entry.

---

## 2. Bối cảnh sử dụng

### Khi nào khái niệm này có giá trị cao?
- [ ] Đang phân vân nên đặt entry limit tại mép OB, tại CE, hay chờ sâu hơn.
- [ ] Có nested FVG hoặc OB con nằm giữa CE và cạnh proximal của OB lớn.
- [ ] Có equal highs/lows hoặc old high/low nằm sát cạnh distal của OB (nguy cơ full mitigation để quét).
- [ ] Đang đánh giá một OB nằm gần equilibrium của dealing range lớn hơn (chưa rõ có "đủ rẻ" chưa).
- [ ] Đang review một trade bị stop non hoặc bị lỡ tàu để tìm nguyên nhân gốc.

### Khi nào nên bỏ qua?
- [ ] OB không có displacement/BOS rõ ràng — lúc này vấn đề là OB có hợp lệ hay không, chưa tới bước hỏi "sâu bao nhiêu".
- [ ] Không xác định được dealing range lớn hơn hoặc liquidity xung quanh — thiếu dữ liệu để áp dụng 3 nguyên nhân gốc.
- [ ] Đang ở giữa range, không rõ Premium/Discount.

---

## 3. Ba nguyên nhân gốc quyết định độ sâu

![[OBMitigationDepth-Advanced-CausalDrivers.svg|720]]

*Hình: Ba nguyên nhân gốc khiến cùng một Bullish OB có thể chỉ cho shallow tap, dừng đúng CE, hay đòi hỏi full mitigation.*

### 3.1. Nested FVG/OB con phía trên CE → kéo giá chỉ tới shallow

Khi displacement tạo ra OB đồng thời để lại nhiều lớp imbalance chồng nhau (một FVG lớn bao ngoài, và bên trong nó có thể có một FVG/OB con nhỏ hơn hình thành từ chính nhịp điều chỉnh dẫn tới displacement), thị trường thường "trả nợ" thanh khoản ở tầng nông nhất trước. Nested FVG/OB con nằm giữa CE và cạnh proximal đóng vai trò như một điểm hấp thụ sớm — giá không cần đi xa hơn vì đã có đủ order được kích hoạt ở đó.

**Cách nhận diện:** xuống M15/M5 ngay sau khi OB hình thành, tìm FVG hoặc OB nhỏ nằm trong khoảng 50–100% (từ CE tới cạnh proximal) của OB lớn. Nếu có, đây là **refined entry** — ưu tiên xem đây là điểm entry chính thay vì chờ CE của OB lớn.

### 3.2. Liquidity pool (SSL/BSL) sát cạnh distal → kéo giá tới full mitigation

Nếu ngay dưới cạnh distal của một Bullish OB (hoặc ngay trên cạnh distal của Bearish OB) có một pool thanh khoản rõ ràng — equal lows, old low, hay đáy của một cú swing gần đó — nhiều khả năng giá sẽ đi xuyên qua CE, tới sát hoặc xuyên nhẹ cạnh distal để quét pool đó trước khi đảo chiều thật. Đây là cơ chế tạo ra **kịch bản C (lấp gần biên distal)** trong bảng §7.2 của [[25 - OB - Order Block]] — nguyên nhân gốc chính là liquidity chưa bị lấy, không phải OB "yếu".

**Hệ quả thực chiến quan trọng nhất:** nếu nhận diện được pool này trước, **không đặt stop ngay sát CE**. Hai lựa chọn hợp lý: (a) chờ pool bị quét xong rồi mới tìm LTF MSS để entry muộn hơn nhưng an toàn hơn, hoặc (b) nếu vẫn muốn entry sớm tại CE, đặt stop đủ xa để dự phòng cho cú quét đó (qua điểm sweep, không phải qua CE vài điểm).

### 3.3. Vị trí OB trong Premium/Discount của dealing range lớn hơn

![[OBMitigationDepth-Advanced-PDContext.svg|720]]

*Hình: OB càng gần Equilibrium của dealing range lớn hơn càng cần discount sâu hơn (full mitigation); OB càng nằm sâu trong Discount/OTE (62–79%) thì shallow tap đã đủ "rẻ" để buyer HTF nhập cuộc.*

Đây là nguyên nhân mang tính "vĩ mô" nhất trong ba yếu tố. Cùng một OB M15 có thể cho phản ứng hoàn toàn khác nhau tùy vào việc nó đang nằm ở đâu trong dealing range H4/H1:

- **OB nằm gần equilibrium (45–55%)** của dealing range lớn hơn: về bản chất giá "chưa đủ rẻ" để buyer HTF thấy hấp dẫn. Thường cần đi sâu hơn — full mitigation, đôi khi phải chờ giá lùi tiếp vào vùng OTE (62–79% retracement) mới có phản ứng đáng tin.
- **OB nằm sâu trong Discount hoặc trùng vùng OTE**: giá vốn đã "rẻ" theo góc nhìn HTF. Shallow tap thường đã đủ vì không cần thêm discount — đây cũng là lý do vì sao nhiều setup 2022 Model tốt nhất chỉ cho một cú test nông rồi bốc thẳng, khiến người máy móc chờ CE bị lỡ tàu.

Xem thêm cách xác định range và vùng này tại [[27 - Premium Discount]] và [[26 - OTE - Optimal Trade Entry]].

### 3.4. Hai yếu tố phụ trợ (đã có trong OB note, nhắc lại ngắn gọn để đủ khung nhân quả)

- **Origin OB vs mid-leg OB** ([[25 - OB - Order Block]] §7.4): OB hình thành tại chính điểm xuất phát của leg (nơi có sweep) là "true origin" — thường chỉ cần shallow/CE đã đủ vì đây là nơi order institutional dày đặc nhất. OB hình thành giữa một leg đang chạy chỉ là trạm dừng tạm — dễ bị xuyên sâu hơn (tới full) khi leg đã đi xa và cần rebalance nhiều hơn.
- **Chất lượng displacement:** displacement càng dứt khoát (nến thân lớn, ít wick đối nghịch, phá cấu trúc rõ) thì xác suất shallow/CE càng cao — vì thị trường "trả giá đủ" ngay từ đầu. Displacement yếu, nhiều nến giằng co mới phá được cấu trúc, thường đòi hỏi discount sâu hơn khi retrace.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Xác định dealing range & vị trí OB trong đó
- Dealing range lớn hơn đang là gì? Equilibrium ở đâu?
- OB đang quan sát rơi vào % nào của range (gần equilibrium hay sâu discount/OTE)?
- Liquidity target (draw on liquidity) phía trên là gì và cách OB bao xa?

### H1 / M15 — Quét liquidity quanh OB
- Có equal highs/lows hoặc old high/low nào sát cạnh distal của OB không?
- OB này là origin của leg hay mid-leg?
- Displacement tạo OB có dứt khoát không (thân lớn, ít wick ngược)?

### M15 / M5 — Tìm nested structure phía trên CE
- Có FVG/OB con nào nằm giữa CE và cạnh proximal không?
- Nếu có, đây có thể là điểm entry refined thay vì chờ CE của OB lớn.

### M5 / M1 — Xác nhận & entry theo đúng kỳ vọng độ sâu
- Nếu dự đoán shallow: chờ MSS con ngay tại nested FVG/OB con.
- Nếu dự đoán CE/full: chờ giá tới đúng vùng, sau đó chờ MSS LTF trước khi entry — không entry limit mù tại CE.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Dự đoán "shallow" được xem là hợp lý khi
- [ ] Có nested FVG/OB con rõ ràng giữa CE và cạnh proximal.
- [ ] OB nằm sâu trong Discount/OTE của dealing range lớn hơn.
- [ ] Displacement tạo OB rất dứt khoát, liquidity target phía trên gần và rõ.

### Dự đoán "full mitigation" được xem là hợp lý khi
- [ ] Có equal highs/lows hoặc pool thanh khoản rõ ràng sát cạnh distal OB.
- [ ] OB nằm gần equilibrium, chưa đủ "rẻ" theo HTF.
- [ ] OB hình thành giữa leg (không phải origin) sau một chuỗi di chuyển đã dài.

### Dự đoán bị vô hiệu khi
- [ ] Giá đóng nến **thân** xuyên qua cạnh distal và giữ acceptance ngoài đó — đây không còn là "full mitigation", mà là **invalidation** (kịch bản D trong [[25 - OB - Order Block]] §7.2). Toàn bộ phân tích độ sâu trong ghi chú này chỉ áp dụng khi OB còn sống.
- [ ] Giá lình xình quá lâu bên trong OB (quá N nến LTF) mà không phản ứng — dấu hiệu order đang bị hấp thụ dần, xác suất chuyển thành Breaker tăng.

---

## 6. Ví dụ chart

### Ví dụ đúng
![[OBMitigationDepth-Example-Correct.svg|720]]

**Mô tả:** Bullish OB NQ1 giả định 21,000–21,040 (CE = 21,020), có nested FVG 21,025–21,035 phía trên và SSL pool (equal lows) tại 20,995 phía dưới. Giá quét SSL 20,995 trước, tạo displacement lên, retrace về đúng nested FVG (~21,030) và phản ứng — trader vào lệnh tại đó với xác nhận M1 MSS, stop đặt dưới 21,000 (qua toàn bộ OB, không sát CE).

**Vì sao đây là ví dụ tốt:**
- Đọc đủ cả ba lớp trước khi chọn mốc: liquidity dưới OB, nested structure trên CE, và không cần chờ máy móc tại CE.
- Stop đặt theo logic cấu trúc (qua điểm sweep), không phải theo khoảng cách tùy tiện từ entry.
- Entry sớm hơn (tại nested FVG) nhưng vẫn có xác nhận LTF, không phải đoán mù.

### Ví dụ sai / dễ nhầm
![[OBMitigationDepth-Example-Wrong.svg|720]]

**Mô tả lỗi:** Cùng OB 21,000–21,040, nhưng trader đặt limit order cứng tại CE 21,020 với stop rất chặt tại 21,015 — không kiểm tra SSL pool tại 20,995. Giá chạm CE, quét trader bằng stop tại 21,015, sau đó tiếp tục xuống quét đúng SSL 20,995 như dự đoán ban đầu của OB, rồi mới đảo chiều thật và chạy — nhưng trader đã bị out từ trước.

**Bài học:**
- CE là mốc tinh chỉnh xác suất cao, không phải điểm entry được đảm bảo có phản ứng ngay lần chạm đầu.
- Luôn quét equal-lows/SSL dưới OB trước khi đặt stop; nếu có, chuẩn bị cho khả năng full mitigation.
- Đây là lỗi gốc rễ giống [[Mistake - Entry Before Liquidity Sweep]] nhưng ở chiều ngược: vào đúng hướng, đúng POI, nhưng sai vì bỏ qua lớp liquidity chưa được quét.

---

## 7. Checklist trước khi áp dụng vào trade

> [!warning] Không dùng CE như một cái nút bấm entry tự động
> CE chỉ có ý nghĩa khi đã trả lời được: OB có nested structure phía trên không? Có liquidity phía dưới không? OB đang ở đâu trong Premium/Discount? Thiếu cả ba câu hỏi này, entry tại CE cũng chỉ là đoán mò với vỏ bọc "kỹ thuật".

- [ ] Xác định dealing range lớn hơn và vị trí % của OB trong đó.
- [ ] Quét equal highs/lows quanh cạnh distal của OB.
- [ ] Xuống LTF tìm nested FVG/OB con giữa CE và cạnh proximal.
- [ ] Xác định OB là origin của leg hay mid-leg.
- [ ] Đặt kỳ vọng độ sâu (shallow / CE / full) TRƯỚC khi giá chạm OB, không suy diễn ngược sau khi đã thấy kết quả.
- [ ] Stop đặt theo logic cấu trúc (qua sweep point hoặc qua cạnh distal), không phải theo khoảng cách cố định từ CE.
- [ ] Có LTF MSS/displacement xác nhận tại đúng mốc đã dự đoán trước khi entry.

---

## 8. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Áp CE như luật cứng | Luôn đặt limit đúng 50% bất kể context | Kiểm tra 3 nguyên nhân gốc trước khi chọn mốc entry |
| Bỏ lỡ shallow tap | Chờ CE trong khi có nested FVG rõ ràng phía trên | Ưu tiên nested FVG/OB con làm điểm entry refined |
| Stop quá chặt sát CE | Đặt stop 5–10 điểm dưới CE mà không xét SSL bên dưới | Quét liquidity quanh OB trước; đặt stop qua điểm sweep |
| Không phân biệt full mitigation với invalidation | Hoảng khi giá xuyên gần đáy OB, thoát lệnh sớm | Chỉ coi là invalid khi có nến đóng THÂN + acceptance ngoài OB |
| Bỏ qua vị trí Premium/Discount của range lớn hơn | Chỉ nhìn OB đơn lẻ, không xét range H4/H1 | Luôn xác định % vị trí OB trong dealing range trước |

---

## 9. Câu hỏi tự kiểm tra

- Mình có thể giải thích 3 nguyên nhân gốc quyết định độ sâu mitigation trong 30 giây không?
- Với một OB cụ thể, mình đã kiểm tra đủ: nested structure phía trên, liquidity phía dưới, và vị trí Premium/Discount chưa?
- Điều gì phân biệt "full mitigation hợp lệ" với "invalidation"?
- Trong journal của mình, có trade nào bị stop non vì đặt stop sát CE mà không xét SSL bên dưới không?
- Có trade nào mình bỏ lỡ vì chờ CE trong khi giá chỉ shallow tap rồi chạy không?

---

## 10. Flashcards / Active Recall

### Q1
**Hỏi:** Ba nguyên nhân gốc nào quyết định giá sẽ shallow tap, chạm CE, hay full mitigation vào một OB?
**Đáp:** (1) Có nested FVG/OB con phía trên CE hay không, (2) có liquidity pool (SSL/BSL) sát cạnh distal hay không, (3) vị trí OB trong Premium/Discount của dealing range lớn hơn.

### Q2
**Hỏi:** Vì sao đặt stop sát CE có thể nguy hiểm?
**Đáp:** Nếu có liquidity pool (equal lows/highs) nằm sát cạnh distal của OB, giá thường cần quét pool đó trước khi đảo chiều thật — full mitigation. Stop sát CE dễ bị quét non trước khi giá đảo chiều đúng như dự đoán.

### Q3
**Hỏi:** Full mitigation khác invalidation ở điểm nào?
**Đáp:** Full mitigation là giá đi sâu (tới sát hoặc xuyên nhẹ cạnh distal bằng wick) nhưng thân nến vẫn đóng trong hoặc tại cạnh OB — OB còn sống. Invalidation là nến đóng THÂN xuyên qua cạnh distal và giữ acceptance ngoài đó — OB đã chết.

---

## 11. Lesson Learned

### Bài học chính
- CE là mốc tinh chỉnh xác suất cao trung bình, không phải điểm entry được đảm bảo — luôn đọc context trước khi áp dụng.
- Nested FVG/OB con phía trên CE và liquidity pool phía dưới cạnh distal là hai "tín hiệu sớm" quan trọng nhất để dự đoán độ sâu.
- Vị trí OB trong Premium/Discount của dealing range lớn hơn ảnh hưởng tới việc giá có cần discount sâu hơn hay không.

### Quy tắc cá nhân rút ra
- [ ] Luôn quét equal-highs/lows quanh OB trước khi đặt stop.
- [ ] Luôn xuống LTF tìm nested FVG/OB con trước khi quyết định chờ CE hay vào sớm.
- [ ] Log field `ob_mitigation_depth` (shallow / CE / full) cho mọi trade dùng model 2022 để lượng hóa tỷ lệ qua backtest, thay vì tin theo lý thuyết suông.

### Câu nhắc nhở khi trade
> CE cho biết nên tinh chỉnh entry ở đâu — không cho biết giá có dừng ở đó hay không. Luôn hỏi: có gì phía trên hút giá sớm, có gì phía dưới kéo giá xa hơn?

---

## Liên kết liên quan
- [[25 - OB - Order Block]] — khái niệm gốc, bảng kịch bản A–E (touch&go/CE/distal/close-through/breaker)
- [[10 - Consequent Encroachment (Mean Threshold)]] — định nghĩa và cơ chế CE
- [[13 - FVG  - Fair Value Gap]] — nested FVG và imbalance
- [[27 - Premium Discount]] — vị trí trong dealing range
- [[26 - OTE - Optimal Trade Entry]] — vùng 62–79% retracement
- [[16 - Internal & External Range Liquidity (IRL & ERL)]] — liquidity pool quanh OB
- [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] — lý do giá cần quét thanh khoản trước khi đảo chiều
