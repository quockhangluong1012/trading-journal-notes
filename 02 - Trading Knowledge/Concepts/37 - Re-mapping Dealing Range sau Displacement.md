---
type: ict-concept
concept: Re-mapping Dealing Range sau Displacement
aliases:
  - Re-mapping Dealing Range
  - Re-draw Dealing Range
  - Cập nhật Dealing Range sau displacement
  - Range Shift
tags:
  - trading/ict/concept
  - trading/study
  - "#DealingRange"
  - "#Displacement"
status: developing
category: Market Structure
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
last_reviewed: 2026-07-01
created: 2026-07-01
updated: 2026-07-01
common_mistakes:
  - "[[Mistake - Không re-map range sau displacement]]"
  - "[[Mistake - Wrong Dealing Range]]"
  - "[[Mistake - Thoát lệnh sớm]]"
---

# Re-mapping Dealing Range sau Displacement

> [!summary] Tóm tắt 1 câu
> **Sau mỗi nhịp displacement lấy external liquidity của range cũ, range cũ đã "chết" — mình phải VẼ LẠI dealing range trên swing mới (đáy mới → đỉnh mới) để đo lại premium/discount, phân loại lại internal/external liquidity và tìm POI tiếp theo; POI mới gần như luôn là FVG/OB do chính nhịp displacement để lại.**

> [!important] Nguyên tắc cốt lõi
> **POI không biến mất — nó đổi dạng.** Khi OB cũ đã mitigate và bạn "không thấy POI nào để theo dõi", nguyên nhân thường không phải hết cơ hội, mà là bạn vẫn đang nhìn vào **range cũ**. Displacement vừa rồi đã tạo ra một range mới và để lại PD array mới (FVG/OB) bên trong nó. Nhiệm vụ của bạn là re-map, không phải chờ đợi.

---

## 1. Định nghĩa

**Khái niệm:**  
Re-mapping Dealing Range là hành động **vẽ lại khung dealing range** sau khi một nhịp **displacement** (giãn nở mạnh, có động lượng, thường tạo FVG) đã **lấy external liquidity** ở một đầu range cũ hoặc tạo một swing point mới có ý nghĩa. Range cũ — vốn dùng để đo premium/discount và phân loại liquidity — không còn phản ánh cấu trúc hiện tại, nên mọi phép đo dựa trên nó trở nên sai. Re-mapping nghĩa là: xác định lại **swing high mới** và **swing low mới**, đo lại **equilibrium (50%)**, phân loại lại **internal vs external liquidity**, và từ đó **định vị POI tiếp theo**.

Đây là một **quy trình bảo trì range**, không phải một entry model. Nó là bước "cập nhật bản đồ" sau khi thị trường đã đi một quãng đường mới. Xem nền tảng ở [[12 - Dealing Range]].

**Mục đích trong ICT:**  
- **Giữ premium/discount luôn đúng thời sự:** sau displacement, giá có thể đã chuyển từ discount của range cũ sang một range hoàn toàn mới; nếu không re-map, bạn sẽ Long ở "discount" tưởng tượng trong khi thực chất đang ở premium của range mới.
- **Tái phân loại liquidity:** đỉnh vừa bị quét trở thành liquidity đã tiêu thụ; đáy mới / đỉnh mới trở thành external mới; các FVG/OB trong nhịp đẩy trở thành internal liquidity mới. Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]].
- **Tìm POI kế tiếp:** nhịp displacement tự sinh ra PD array (FVG, OB, breaker). POI tiếp theo là cái nằm trong **discount/equilibrium của range mới** và còn unmitigated.
- **Cập nhật draw on liquidity:** external nào vừa bị lấy, external nào còn mở → hướng hút tiếp theo của giá.

**Vì sao khái niệm này quan trọng:**  
Vì thị trường vận động theo chu kỳ **expansion → retracement → expansion**. Mỗi expansion (displacement) reset lại bối cảnh. Trader hay bị "kẹt" ở range cũ: họ chờ giá quay lại một OB đã mitigate, hoặc kết luận "hết setup", trong khi range mới đã hình thành ngay trước mắt với POI mới rõ ràng. Đây chính xác là tình huống "OB H1 đã mitigate, không thấy POI nào tiếp theo" — vấn đề nằm ở việc chưa re-map, chứ không phải hết cơ hội.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Range cũ còn hiệu lực không, hay displacement vừa rồi đã làm nó "chết"?
- Sau nhịp đẩy này, đâu là **swing high/low mới** tạo thành range hiện tại?
- Giá đang ở premium hay discount của **range MỚI** (không phải range cũ)?
- POI tiếp theo nằm ở đâu — FVG/OB nào trong nhịp displacement còn unmitigated?
- External liquidity nào vừa bị lấy, cái nào còn mở làm draw on liquidity?

### Re-mapping không phải là gì
- Không phải vẽ lại range mỗi khi giá nhích một chút; chỉ re-map khi có **displacement lấy external** hoặc tạo swing point có ý nghĩa.
- Không phải lý do để "dời cọc" cho khớp lệnh đang thua; re-map là đọc cấu trúc khách quan, không phải hợp lý hóa.
- Không phải chỉ đổi con số Fibonacci; nó bao gồm tái phân loại liquidity và xác định POI mới.
- Không phải tín hiệu vào lệnh; sau khi re-map xong, entry vẫn cần sweep + MSS + displacement trên LTF.

---

## 2. Bối cảnh sử dụng

### Ba tình huống kích hoạt re-mapping

| Tình huống kích hoạt | Chuyện gì vừa xảy ra | Hành động re-map |
|---|---|---|
| **External của range cũ bị lấy** | Displacement đóng thân qua đỉnh/đáy range cũ và giữ acceptance | Range cũ chết; vẽ range mới lấy đỉnh/đáy vừa tạo |
| **Swing point mới có ý nghĩa hình thành** | Sau sweep + MSS + displacement, giá tạo đáy/đỉnh mới rõ ràng | Dùng đáy/đỉnh mới làm một đầu range mới |
| **Đã "ăn" xong một nhịp, cần tìm nhịp kế** | Bạn vừa đóng lệnh tại internal liquidity (như quét đỉnh cũ) | Re-map trên swing (đáy entry → đỉnh vừa quét) để tìm POI retrace tiếp |

> [!tip]
> Tình huống thứ ba chính là **case của bạn**: bạn Long từ discount, thoát ở 1.6R khi giá quét đỉnh cũ (một internal/minor BSL). Nhịp đi lên đó là một **displacement leg mới**. Re-map ngay trên swing "đáy bạn entry → đỉnh vừa quét" thì POI tiếp theo (FVG/OB của chính nhịp này) hiện ra lập tức.

### Khi nào khái niệm này có giá trị cao?
- [ ] Vừa có một nhịp **displacement rõ ràng** (nến thân dài, momentum, để lại FVG).
- [ ] Displacement đó **lấy external liquidity** (quét đỉnh/đáy cũ) hoặc tạo **swing point mới**.
- [ ] Bạn vừa đóng một lệnh và đang tìm cơ hội tiếp theo cùng hướng bias.
- [ ] Daily Bias / HTF narrative vẫn còn hiệu lực (draw on liquidity chính chưa hoàn tất).
- [ ] Có FVG/OB do nhịp displacement để lại, còn unmitigated, nằm ở discount/premium của range mới.

### Khi nào nên bỏ qua?
- [ ] Nhịp giá vừa rồi chỉ là **wiggle / micro move**, không phải displacement thật → chưa cần vẽ lại.
- [ ] External chính của HTF range đã bị lấy và **draw on liquidity đã hoàn tất** → không re-map để cố tìm entry cùng hướng, mà cân nhắc đảo bias.
- [ ] Giá đang ở **equilibrium của range mới** → có range mới nhưng không có location tốt, vẫn phải chờ.
- [ ] Re-map ra range nhưng **không có internal POI hợp lệ** → không có gì để theo dõi thật, đứng ngoài.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Một nhịp displacement mới:** chuỗi nến giãn nở cùng hướng, momentum rõ, thường để lại một hoặc nhiều FVG chưa được lấp.
2. **External cũ bị chạm/lấy:** displacement quét qua đỉnh (BSL) hoặc đáy (SSL) của range trước đó.
3. **Swing point mới:** một đỉnh mới (nếu đẩy lên) hoặc đáy mới (nếu đẩy xuống) đủ rõ để làm đầu range.
4. **PD array mới bên trong nhịp đẩy:** FVG, OB, hoặc breaker do displacement tạo ra → ứng viên POI.
5. **Range cũ hết vai trò:** premium/discount đo trên range cũ mâu thuẫn với hành vi giá hiện tại.

### Quy trình re-map 5 bước (làm theo thứ tự)

```text
1. XÁC NHẬN displacement thật (không phải wiggle) và nó đã lấy external nào.
2. VẼ range mới: chọn swing low mới và swing high mới có ý nghĩa làm hai đầu.
3. ĐO equilibrium (50%) của range mới → giá đang premium hay discount?
4. PHÂN LOẠI lại liquidity: external mới (hai đầu) + internal mới (FVG/OB trong nhịp đẩy).
5. CHỌN POI tiếp theo: internal PD array còn unmitigated ở đúng nửa range cho hướng bias.
```

### Điều kiện bắt buộc (để một lần re-map là hợp lệ)
- [ ] Có displacement thật, xác nhận bằng momentum + FVG (không phải nến do dự).
- [ ] Xác định rõ **hai đầu range mới** và ghi giá cụ thể của từng đầu.
- [ ] Đo và đánh dấu **equilibrium (50%)** của range mới.
- [ ] Xác định **external nào vừa bị lấy** và **external nào còn mở** (draw on liquidity).
- [ ] Liệt kê **internal POI** (FVG/OB) hợp lệ trong range mới.

### Điều kiện tăng xác suất (POI mới đáng theo dõi)
- [ ] POI mới trùng với **discount/equilibrium của range mới** cho lệnh Long (hoặc premium cho Short).
- [ ] POI mới **cộng hưởng** với một PD array HTF (ví dụ FVG H1 nằm trong discount của range D1).
- [ ] External phía draw on liquidity **vẫn còn mở** (còn room để giá chạy tới target).
- [ ] Nhịp displacement đủ mạnh để tạo FVG "sạch" (ít bị lấp một phần).
- [ ] Range mới nằm cùng hướng với [[12 - Daily Bias]].

### Điều kiện làm setup yếu đi
- Displacement yếu / mập mờ → range mới không đáng tin.
- Draw on liquidity chính đã hoàn tất → tìm entry cùng hướng là bơi ngược narrative.
- FVG/OB của nhịp đẩy đã bị lấp gần hết → POI cạn.
- Range mới quá nhỏ, không đủ room tới external → R:R kém.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] 4 câu hỏi bắt buộc sau mỗi nhịp displacement
> 1. **Displacement vừa rồi có lấy external của range cũ / tạo swing mới không?** (nếu có → range cũ chết)
> 2. **Hai đầu của range MỚI là đâu, equilibrium ở giá nào?**
> 3. **Giá đang premium hay discount của range MỚI?**
> 4. **POI tiếp theo (FVG/OB nào của nhịp đẩy) còn unmitigated và ở đúng nửa range?**

### D1 / H4 — Bias & Narrative có còn hiệu lực?
- **Kiểm tra draw on liquidity HTF:** external chính (ví dụ đường xanh trên = BSL lớn) đã bị lấy chưa? Chưa → bias giữ nguyên, có lý do tìm entry cùng hướng sau khi re-map. Rồi → cân nhắc đảo bias thay vì re-map để cố Long tiếp.
- **Range gốc HTF:** re-map ở LTF không được mâu thuẫn với range D1. Range mới của H1 lý tưởng nằm gọn trong discount (cho Long) của range D1.

### H1 / M15 — Vẽ lại range con & xác định POI mới
- **Vẽ range H1 mới:** đáy mới (đáy bạn vừa entry / đáy displacement) → đỉnh mới (đỉnh vừa bị quét). Đây là "swing mới" thay cho range đã dùng OB cũ.
- **POI mới = internal của range H1 mới:** thường là **FVG H1** do nhịp displacement đi lên để lại. Chọn cái gần discount/equilibrium nhất và còn unmitigated.
- **POI dự phòng:** breaker block (nếu có minor high bị phá trong nhịp đẩy) hoặc mitigation block; OB cũ đã mitigate xếp ưu tiên thấp nhất.
- **External mới của range con:** đỉnh vừa quét là BSL nội bộ đã tiêu thụ; external còn mở là mục tiêu tiếp (đỉnh cao hơn / HTF BSL).

### M5 / M1 — Chờ giá về POI mới rồi mới tìm entry
- **Không đuổi giá ở premium** của range mới. Chờ retrace về POI H1 đã đánh dấu.
- **Khi giá chạm POI:** xuống M5 chờ đúng chuỗi ICT 2022 — sweep liquidity nội bộ → **MSS + displacement + FVG M5** → entry tại 50% FVG M5 (giống hệt lệnh trước của bạn). Xem [[21 - Market Structure Shift]].
- **Quản lý lệnh lần này:** target external còn mở; **scale-out tại internal liquidity, giữ runner** — sửa lỗi thoát toàn bộ ở 1.6R.

> [!warning]
> Range M5 cục bộ chỉ dùng cho execution. Việc "giá đang discount" để quyết định Long/Short phải đo trên **range H1/D1 đã re-map**, không phải range M5.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Re-map được xem là hợp lệ khi
- [ ] Có displacement thật đã lấy external cũ hoặc tạo swing mới có ý nghĩa.
- [ ] Hai đầu range mới rõ ràng, tạo bởi displacement/BOS, ghi được giá.
- [ ] Equilibrium mới được đo và giá có location rõ (premium hoặc discount).
- [ ] Có internal POI hợp lệ, còn unmitigated, đúng nửa range cho hướng bias.
- [ ] Range mới không mâu thuẫn với HTF range/bias.

### KHÔNG re-map (hoặc re-map là sai) khi
- [ ] Nhịp giá chỉ là retracement/wiggle, chưa phải displacement → range cũ vẫn sống.
- [ ] Bạn vẽ lại range chỉ để "cứu" một lệnh đang thua (bias confirmation).
- [ ] External chính HTF đã bị lấy, draw hoàn tất → nên đảo bias, không re-map cùng hướng.
- [ ] Sau re-map giá ở equilibrium hoặc không có POI → có range nhưng không có lệnh.

### Phân biệt "displacement tạo range mới" vs "chỉ là pullback trong range cũ"

| Quan sát | Cách đọc hợp lý |
|---|---|
| Nến thân dài, momentum, để lại FVG, đóng qua external cũ và giữ acceptance | **Displacement thật** → range cũ chết, re-map |
| Giá nhích lên nhưng thân nến nhỏ, nhiều wick, không lấy external, không FVG | **Chỉ pullback** → giữ range cũ, chưa re-map |
| Giá wick qua external rồi đóng ngược lại vào range + displacement ngược | **Sweep external** (turtle soup) → có thể đảo; re-map theo hướng đảo nếu MSS xác nhận |
| Giá lấy external một đầu rồi tạo BOS cùng hướng, swing mới rõ | **Range dịch chuyển** → re-map, hai đầu mới, đo lại premium/discount |

---

## 6. Ví dụ chart

### Ví dụ đúng — Re-map sau khi Long chạm internal liquidity, tìm được FVG H1 làm POI tiếp
![[paste-image-here.png]]

**Mô tả:**  
Range cũ: đáy đã sweep SSL → OB H1 ở discount. Trader Long tại FVG M5 trong OB đó, giá displacement đi lên và **quét một đỉnh cũ (internal BSL)** — trader thoát 1.6R. Thay vì kết luận "hết POI vì OB đã mitigate", trader **re-map**: vẽ range mới từ **đáy vừa entry → đỉnh vừa quét**, đo equilibrium. Nhịp đẩy lên để lại một **FVG H1** nằm ở discount của range mới, còn unmitigated. Đó là POI tiếp theo. Trader chờ giá retrace về FVG H1, xuống M5 chờ MSS + displacement + FVG M5, vào Long tiếp, target là external BSL còn mở (đỉnh cao hơn / đường xanh trên).

**Vì sao đây là ví dụ tốt:**
- OB cũ mitigate không có nghĩa hết cơ hội — nhịp displacement tự tạo POI mới (FVG H1).
- Premium/discount được đo lại trên **range mới**, nên location vẫn đúng để Long tiếp.
- Draw on liquidity (external BSL) vẫn còn mở → có lý do và có room cho lệnh tiếp theo.
- Luồng internal → external được nối tiếp mạch lạc thay vì "chờ trong vô định".

### Ví dụ sai / dễ nhầm — không re-map, cố chờ OB cũ hoặc Long ở premium range mới
![[paste-image-here.png]]

**Mô tả lỗi:**  
Sau khi thoát lệnh, trader vẫn dán mắt vào OB H1 cũ (đã mitigate) và chờ giá quay lại đó — nhưng giá không về, trader bỏ lỡ nhịp tiếp theo. Hoặc tệ hơn: trader thấy giá đang đi lên, nhảy vào Long ngay mà không re-map, hóa ra giá đang ở **premium của range mới**, sát BSL sắp bị quét → giá đảo, lệnh thua.

**Bài học:**
- **POI đổi dạng sau displacement** — đừng chờ POI cũ đã tiêu thụ.
- Trước khi vào lệnh tiếp, **luôn re-map và đo lại premium/discount trên range mới**; đừng Long ở premium vì tưởng còn ở discount range cũ.
- Đây là mặt còn lại của [[12 - Dealing Range]]: chọn/giữ sai range → mua premium tưởng discount.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[12 - Dealing Range]]
- [[27 - Premium Discount]]
- [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[13 - FVG  - Fair Value Gap]]
- [[25 - OB - Order Block]]
- [[04 - BB - Breaker Block]]
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[26 - OTE - Optimal Trade Entry]]
- [[12 - Daily Bias]]
- [[32 - Top-down Analysis (Multiple Timeframes)]]
- [[35 - Aggressive Displacement Entry]]

### Sequence mẫu — Re-map để tìm nhịp Long thứ hai
```text
Đã Long nhịp 1 từ discount range cũ → giá displacement lên, quét internal BSL (đỉnh cũ) → thoát/scale-out
→ RE-MAP: vẽ range mới [đáy entry → đỉnh vừa quét], đo equilibrium
→ Phân loại lại: external cũ (SSL đáy) đã tiêu thụ; internal MỚI = FVG/OB của nhịp đẩy
→ Chọn POI: FVG H1 trong discount range mới, còn unmitigated
→ Chờ giá retrace về POI (không đuổi ở premium)
→ M5: sweep nội bộ → MSS + Displacement + FVG M5 → entry 50% FVG
→ Stop dưới POI/swing low; Target: external BSL còn mở
→ Scale-out ở internal, giữ runner tới external (sửa lỗi thoát non 1.6R)
→ Re-map lại khi external tiếp theo bị lấy
```

> [!note]
> Re-mapping là cách biến một lệnh đơn lẻ thành **chuỗi lệnh cùng một narrative**: mỗi displacement lấy một tầng liquidity, để lại một POI mới cho nhịp sau, cho tới khi draw on liquidity HTF hoàn tất. Đây là tư duy "trading the delivery" thay vì "một lệnh rồi hết".

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Re-map cho bạn range và POI mới — nhưng có range chưa phải có lệnh. Vẫn cần location đúng + POI hợp lệ + xác nhận LTF.

### A. Trigger & Context
- [ ] Nhịp vừa rồi là **displacement thật** (momentum + FVG), không phải wiggle.
- [ ] Nó đã **lấy external cũ / tạo swing mới** → range cũ hết hiệu lực.
- [ ] HTF bias & draw on liquidity chính **vẫn còn hiệu lực** (external chính chưa bị lấy).

### B. Re-map (vẽ lại khung)
- [ ] Đã vẽ **range mới**, ghi giá hai đầu.
- [ ] Đã đo **equilibrium (50%)**; biết giá đang premium hay discount range mới.
- [ ] Đã phân loại **external mới** (đầu nào còn mở = draw) và **internal mới** (FVG/OB).
- [ ] Đã chọn **POI tiếp theo** ở đúng nửa range, còn unmitigated.

### C. Execution (khi giá về POI)
- [ ] Giá đã retrace về POI (không đuổi ở premium/equilibrium).
- [ ] Có sweep + MSS + displacement + FVG trên M5 trong POI.
- [ ] Entry có stop logic (dưới POI/swing).
- [ ] Target là external còn mở; có kế hoạch **scale-out + giữ runner**.
- [ ] R:R đạt kế hoạch; range mới đủ room tới external.

### D. Quy tắc "không có lệnh"
- [ ] Chỉ là pullback, chưa displacement → không re-map, không lệnh.
- [ ] Draw HTF đã hoàn tất → không cố Long cùng hướng; xét đảo bias.
- [ ] Sau re-map giá ở equilibrium / không có POI → chờ.
- [ ] Đang muốn re-map để hợp lý hóa một lệnh thua → dừng, đây là bias.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Không re-map sau displacement | "OB đã mitigate, hết POI để theo dõi" | Vẽ range mới trên swing mới; POI = FVG/OB của nhịp đẩy |
| Chờ POI đã tiêu thụ | Ngồi đợi giá quay lại OB cũ đã mitigate | POI đổi dạng; chuyển sang internal PD array mới |
| Long ở premium range mới | Nhảy vào theo momentum, không đo lại location | Re-map + đo equilibrium trước; chỉ Long ở discount |
| Re-map để cứu lệnh thua | Vẽ lại range cho khớp lệnh đang lỗ | Re-map là đọc cấu trúc khách quan, không phải hợp lý hóa |
| Re-map khi mới chỉ pullback | Vẽ range mới sau một nhịp hồi nhỏ | Chỉ re-map khi có displacement thật (momentum + FVG) |
| Bỏ qua draw HTF đã xong | Cố tìm Long tiếp sau khi BSL lớn đã bị lấy | Kiểm tra external HTF; nếu draw xong → xét đảo bias |
| Thoát non không giữ runner | Đóng toàn bộ ở internal liquidity (như 1.6R) | Scale-out ở internal, giữ runner tới external mới |

---

## 10. Câu hỏi tự kiểm tra

- Nhịp vừa rồi là displacement thật hay chỉ pullback?
- Displacement đó đã lấy external nào, tạo swing mới ở đâu?
- Hai đầu range MỚI là gì, equilibrium ở giá nào?
- Giá đang premium hay discount của range mới?
- POI tiếp theo là FVG/OB nào của nhịp đẩy, còn unmitigated không?
- External nào vừa tiêu thụ, external nào còn mở làm draw?
- Draw on liquidity HTF còn hiệu lực không, hay tôi nên đảo bias?
- Tôi đang re-map để đọc thị trường, hay để cứu một lệnh thua?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Re-mapping Dealing Range là gì?  
**Đáp:** Vẽ lại khung dealing range sau khi displacement lấy external cũ / tạo swing mới, để đo lại premium/discount, phân loại lại internal-external liquidity và tìm POI tiếp theo. Là quy trình bảo trì range, không phải entry model.

### Q2
**Hỏi:** Khi nào phải re-map?  
**Đáp:** Khi có displacement thật (momentum + FVG) đã lấy external của range cũ hoặc tạo một swing point mới có ý nghĩa; hoặc khi vừa đóng một nhịp và cần tìm nhịp kế cùng hướng bias.

### Q3
**Hỏi:** "OB đã mitigate, không còn POI" — sai ở đâu?  
**Đáp:** POI không biến mất mà đổi dạng. Nhịp displacement để lại FVG/OB mới. Vẫn đang nhìn range cũ nên không thấy; re-map thì POI mới (FVG H1 trong discount range mới) hiện ra.

### Q4
**Hỏi:** Điều kiện quan trọng nhất để re-map hợp lệ?  
**Đáp:** Phải có displacement THẬT (không phải pullback/wiggle) và nó đã lấy external / tạo swing mới; đồng thời HTF bias & draw còn hiệu lực.

### Q5
**Hỏi:** Sau re-map, POI tiếp theo thường là gì?  
**Đáp:** FVG (hoặc OB/breaker) do nhịp displacement tạo ra, nằm ở discount/equilibrium của range mới và còn unmitigated.

### Q6
**Hỏi:** Khi nào KHÔNG nên re-map để tìm lệnh cùng hướng?  
**Đáp:** Khi external chính của HTF đã bị lấy và draw on liquidity đã hoàn tất — lúc đó nên xét đảo bias, không cố Long/Short cùng hướng cũ.

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
TABLE date, symbol, position, pnl, r_multiple, mistakes
FROM ""
WHERE contains(string(mistakes), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault dùng path riêng cho trades, thay `FROM ""` bằng `FROM "05 - Live Trading Journal/Trades"`.

---

## 13. Lesson Learned

### Bài học chính
- **POI không biến mất, nó đổi dạng.** OB mitigate ≠ hết cơ hội; displacement tạo POI mới.
- Sau mỗi displacement, range cũ **chết** — premium/discount phải đo lại trên range mới trước khi nghĩ tới entry.
- Re-mapping biến một lệnh đơn lẻ thành **chuỗi lệnh cùng narrative** cho tới khi draw HTF hoàn tất.
- Re-map là đọc cấu trúc **khách quan**, tuyệt đối không dùng để hợp lý hóa một lệnh đang thua.
- Kết hợp re-map với **scale-out + runner**: mỗi tầng liquidity là một chốt một phần, không thoát toàn bộ ở internal.

### Quy tắc cá nhân rút ra
- [ ] Mỗi khi đóng một nhịp, tôi re-map range mới trước khi kết luận "hết POI".
- [ ] Tôi chỉ re-map khi có displacement thật, không re-map sau pullback.
- [ ] Tôi luôn đo lại equilibrium range mới trước khi vào lệnh tiếp — không Long ở premium.
- [ ] Nếu draw HTF đã hoàn tất, tôi xét đảo bias thay vì cố tìm lệnh cùng hướng.

### Câu nhắc nhở khi trade
> **"OB cũ mitigate rồi thì vẽ lại range — POI không mất, nó chỉ chuyển sang cái FVG mà cú displacement vừa để lại."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt re-map với chọn range ban đầu không? |
| Nhận diện trên chart |  | Có phân biệt displacement thật vs pullback để quyết định re-map không? |
| Biết khi nào bỏ qua |  | Có nhận ra khi draw HTF đã xong nên đảo bias thay vì re-map không? |
| Kết hợp với context HTF |  | Range mới có nằm trong discount/premium của HTF range không? |
| Áp dụng vào trade thực tế |  | Có tìm được POI tiếp theo và giữ runner tới external không? |

**Kế hoạch review tiếp theo:**  
- [ ] Đối chiếu lại lệnh EURUSD/NAS100 gần nhất: sau khi thoát 1.6R, POI tiếp theo (FVG H1) nằm ở đâu?
- [ ] Backtest 20–30 setup có nhịp displacement lấy internal liquidity → thống kê xác suất nhịp tiếp theo tới external.
- [ ] So sánh R trung bình khi thoát toàn bộ ở internal vs scale-out + runner tới external.

---

## Appendix — Re-map Quick Reference Card

> [!abstract] Copy vào Daily Note sau mỗi displacement
> **Date / Market:**  
> **Displacement thật? (momentum + FVG):** Yes / No  
> **External vừa bị lấy:** BSL @ ___ / SSL @ ___  
> **Range MỚI — đáy:** ___  **đỉnh:** ___  
> **Equilibrium (50%):** ___  
> **Location hiện tại:** Premium / Discount / Equilibrium  
> **External còn mở (draw):** BSL above ___ / SSL below ___  
> **POI tiếp theo (internal):** FVG/OB @ ___ (nửa nào?) — unmitigated?  
> **HTF bias còn hiệu lực?:** Yes / No (nếu No → xét đảo)  
> **Hướng ưu tiên:** Long ở discount / Short ở premium / chờ  
> **Kế hoạch quản lý:** scale-out @ internal ___ / runner → external ___  
> **No-trade:** chỉ pullback / equilibrium / không có POI / draw đã hoàn tất
