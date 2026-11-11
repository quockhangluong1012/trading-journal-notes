---
type: ict-concept
concept: Sell-side Liquidity
aliases:
  - SSL
  - Sell-side Liquidity
  - Sellside Liquidity
tags:
  - trading/ict/concept
  - trading/study
  - "#SSL"
status: developing
category: Liquidity
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-06-22
common_mistakes:
  - "[[Mistake - Long When SSL Only Tagged]]"
  - "[[Mistake - Entry Before Liquidity Sweep]]"
  - "[[Mistake - Buy Into Continuation Breakdown]]"
---

# Sell-side Liquidity

> [!summary] Tóm tắt 1 câu
> **Sell-side Liquidity (SSL) là cụm lệnh sell chờ nằm DƯỚI thị trường — chủ yếu là sell stop (stop loss của lệnh Long) và sell-stop của breakout trader — tích tụ dưới các đáy; nó vừa là DRAW (mục tiêu giá bị hút xuống) vừa là vùng để SWEEP trước khi đảo chiều Long.**

> [!important] Nguyên tắc cốt lõi
> **Chạm SSL không phải tín hiệu Long. Tín hiệu là SWEEP SSL → RECLAIM/displacement lên → LTF MSS tại POI.**  
> Giá đóng nến phá xuống dưới SSL và giữ giá (acceptance) là tiếp diễn giảm, KHÔNG phải lý do để bắt đáy.

---

## 1. Định nghĩa

**Khái niệm:**  
Sell-side Liquidity là tập hợp các **lệnh bán chờ (resting sell orders)** nằm phía dưới mức giá hiện tại. Phần lớn là **sell stop**: chính là stop loss của những người đang giữ lệnh Long (khi giá phá xuống, các stop này biến thành lệnh bán thị trường) cộng với **sell-stop entry** của breakout trader muốn bán khi giá phá đáy. Các lệnh này tập trung dày đặc ngay **dưới previous lows, equal lows / relative equal lows, swing lows, session lows (Asia low / London low), PDL (Previous Day Low), PWL (Previous Week Low)**. Khi nói "giá đang đi tìm SSL", ý là giá có xu hướng bị hút xuống nơi tập trung các lệnh bán đó.

**Mục đích trong ICT:**
- Xác định **draw on liquidity phía dưới**: đâu là đáy/level mà giá có xác suất bị kéo xuống để lấy.
- Cung cấp **target chốt lời** cho lệnh Short (giá phân phối xuống về SSL).
- Đánh dấu **vùng SWEEP** để chờ đảo chiều Long: smart money quét stop của phe Long để gom thanh khoản mua.
- Giải thích vì sao giá "phá đáy rồi quay đầu lên" — đó là stop hunt rồi reverse, không phải ngẫu nhiên.

**Vì sao khái niệm này quan trọng:**  
Thị trường không di chuyển ngẫu nhiên giữa các mức; nó di chuyển từ **liquidity pool này sang liquidity pool khác**. SSL là một nửa của bản đồ thanh khoản (nửa còn lại là [[07 - Buy-side Liquidity]]). Nếu không đọc được SSL nằm ở đâu, trader hay đặt stop loss đúng chỗ market muốn quét, hoặc bắt đáy quá sớm khi giá chỉ vừa chạm chứ chưa sweep + reclaim.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Phía dưới còn cụm thanh khoản nào chưa bị lấy, và nó nằm ở level nào?
- Giá đang bị hút xuống SSL hay đã quét xong rồi?
- Lệnh Short của tôi nên chốt lời tại SSL nào?
- Cú phá đáy vừa rồi là **sweep để reverse** hay **acceptance để tiếp diễn**?
- Đáy này có phải engineered liquidity (equal lows được "tạo" để dụ) không?

### Sell-side Liquidity không phải là gì
- Không phải "vùng hỗ trợ để mua". Đáy là nơi tập trung lệnh bán; chạm đáy là lúc nguy hiểm nhất, không phải an toàn nhất.
- Không phải tín hiệu Long khi giá chỉ **chạm** SSL. Cần sweep + reclaim + LTF MSS/displacement.
- Không phải mức giá cố định; SSL chỉ bị "lấy" khi giá quét xuống dưới nó, không phải khi giá đến gần.
- Không phải lý do bỏ qua HTF bias. SSL chỉ là điểm tựa cho narrative, không thay thế bias.
- Không phải "cứ phá đáy là sẽ hồi lên". Phá xuống và giữ giá là tiếp diễn giảm.

---

## 2. Bối cảnh sử dụng

### SSL đóng hai vai trò ngược nhau tùy bias

| Vai trò | Bối cảnh | Hành động ưu tiên |
|---|---|---|
| **DRAW / Target** | Bearish bias; giá đang phân phối xuống; SSL phía dưới còn mở | Dùng SSL làm **target chốt lời Short**; không bắt đáy giữa đường tới SSL |
| **SWEEP zone (reversal)** | Bullish bias; giá retrace về discount; SSL nằm ngay dưới một POI bullish | Chờ giá **quét SSL** → reclaim/displacement lên → tìm Long tại POI |
| **Neutral / chưa rõ** | Giá ở equilibrium; nhiều cụm SSL hai phía; chưa rõ pool nào ưu tiên | Không ép; đánh dấu các cụm SSL rồi chờ giá chọn hướng và sweep rõ |

> [!tip]
> **Cùng một SSL có thể là target rồi sau đó thành điểm reversal.** Khi giá Short về tới SSL và quét nó, đó vừa là lúc chốt lời Short vừa là lúc bắt đầu canh Long nếu xuất hiện reclaim + MSS lên. Vai trò phụ thuộc vào nơi giá đang ở trong narrative.

### Phân loại SSL theo nguồn gốc

| Loại SSL | Mô tả | Độ "hấp dẫn" với smart money |
|---|---|---|
| **Equal lows / relative equal lows** | Hai hoặc nhiều đáy gần bằng nhau → engineered liquidity, được "tạo" để dụ trader đặt stop/breakout bên dưới | Rất cao — đây là magnet rõ nhất |
| **PDL / PWL** | Đáy ngày/tuần trước; level được nhiều trader theo dõi | Cao |
| **Session lows (Asia low / London low)** | Đáy phiên; thường bị quét trong phiên sau | Cao trong intraday |
| **Swing low đơn lẻ** | Một đáy cấu trúc rõ; nơi đặt stop của Long | Trung bình–cao |
| **Old lows / long-term lows** | Đáy HTF lâu ngày; cụm thanh khoản lớn | Cao nhưng theo HTF timing |

> [!note]
> **Equal lows = engineered SSL.** Khi thấy hai đáy bằng nhau, hãy giả định thanh khoản đã được "kỹ nghệ hóa" để dụ. Giá thường sẽ quét xuống dưới các equal lows này trước khi đi hướng thật.

### Khi nào khái niệm này có giá trị cao?
- [ ] Có cụm SSL rõ ràng và chưa bị lấy: equal lows, PDL/PWL, session low, swing low đáng kể.
- [ ] HTF bias đã xác định, biết SSL đóng vai trò target (Bearish) hay sweep zone (Bullish).
- [ ] SSL nằm ngay dưới một POI bullish (FVG/OB discount) → tạo setup "sweep rồi Long" chất lượng.
- [ ] Giá đang ở discount của dealing range và đang trôi xuống về SSL trong kill zone.
- [ ] Có khoảng trống đủ rộng từ SSL tới target ngược chiều để R:R hợp lý.

### Khi nào nên bỏ qua?
- [ ] SSL đã bị quét xong và giá đã reprice mạnh đi xa.
- [ ] Giá đóng nến phá xuống dưới SSL và **giữ giá** (acceptance) → đây là tiếp diễn, không Long.
- [ ] Không rõ pool SSL nào ưu tiên; giá ở equilibrium, chop hai phía.
- [ ] Chỉ thấy giá chạm SSL nhưng chưa có reclaim/displacement; bắt đáy lúc này là đoán.
- [ ] SSL nằm ngược HTF bias mà không có POI và counter-trend playbook riêng.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Đáy được nhiều trader theo dõi:** equal lows, swing low rõ, PDL/PWL, session low — nơi stop loss của Long dồn lại.
2. **Cụm equal lows / relative equal lows:** dấu hiệu mạnh nhất của engineered SSL; hai/nhiều đáy nằm gần một đường ngang.
3. **Vị trí trong dealing range:** SSL ý nghĩa nhất khi nằm ở **discount** (cho kịch bản sweep-rồi-Long) hoặc là **external target** phía dưới (cho Short).
4. **Chưa bị lấy:** SSL còn mở (giá chưa quét xuống dưới) mới còn là draw.
5. **Phản ứng sau khi chạm:** sau khi giá quét xuống dưới SSL, có **reclaim nhanh + displacement lên** (reversal) hay **đóng nến giữ giá phía dưới** (acceptance/tiếp diễn)?

### Ma trận nhận diện SSL

| Thành phần | Tín hiệu Long (sweep rồi reverse) | Tín hiệu tiếp diễn giảm (acceptance) | Cảnh báo / chưa rõ |
|---|---|---|---|
| **Cách giá chạm SSL** | Wick xuyên nhanh dưới đáy rồi đóng lại trên (sweep) | Body nến đóng dưới SSL, không reclaim | Chỉ đến gần, chưa xuyên rõ |
| **Reclaim** | Giá nhanh chóng đóng trở lại trên SSL/range | Các pullback không reclaim được level | Reclaim yếu, do dự |
| **Displacement** | Có bullish displacement, để lại FVG lên | Không có; hoặc displacement xuống tiếp | Nến nhỏ, không urgency |
| **Vị trí** | SSL ở discount + dưới một bullish POI | SSL bị phá khi giá ở giữa range/đang trend xuống mạnh | Quanh equilibrium |
| **LTF MSS** | Bullish MSS hình thành ngay sau sweep, trong POI | Không có MSS lên; cấu trúc vẫn LL/LH | MSS ngoài POI / trước sweep |

### Điều kiện bắt buộc (để dùng SSL cho setup Long)
- [ ] Xác định được cụm SSL cụ thể và level của nó (ghi rõ: equal lows tại x.xxxx).
- [ ] SSL phù hợp với HTF bias (Bullish) và nằm ở discount.
- [ ] Có POI bullish hợp lệ (FVG/OB) tại hoặc ngay trên vùng SSL.
- [ ] Giá thực sự **quét xuống dưới SSL** (sweep), không chỉ chạm.
- [ ] Có **reclaim + displacement lên** sau sweep.

### Điều kiện tăng xác suất
- [ ] SSL là equal lows / relative equal lows (engineered → magnet mạnh).
- [ ] Sweep xảy ra trong London / New York Kill Zone.
- [ ] Bullish MSS + displacement để lại FVG ngay sau sweep, trong POI.
- [ ] Có external BSL phía trên còn mở làm target cho leg Long → R:R tốt.
- [ ] SSL trùng / gần một HTF discount PD Array (D1/H4 FVG, OB).

### Điều kiện làm setup yếu đi
- Giá đóng nến phá xuống dưới SSL và giữ giá → khả năng acceptance/tiếp diễn.
- SSL nằm giữa range, không có POI hỗ trợ; bắt đáy thành đoán.
- Sweep xảy ra nhưng không có displacement/MSS lên → chưa đủ bằng chứng reversal.
- SSL ngược HTF bias (Bearish) nhưng cố Long tại đó mà không có lý do mạnh.
- Đã có nhiều cú quét nhỏ liên tiếp dưới đáy mà không reverse → đáy đang bị "ăn mòn" theo hướng giảm.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng SSL
> 1. **Cụm SSL chính nằm ở đâu, và nó là target (Bearish) hay sweep zone (Bullish)?**  
> 2. **SSL này đã bị lấy chưa, hay còn mở để hút giá?**  
> 3. **Nếu giá quét SSL, tôi chờ reclaim + MSS lên tại POI nào để Long?**  
> 4. **Điều gì biến cú phá đáy này thành tiếp diễn (acceptance) thay vì reversal?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral.
- **Đánh dấu các cụm SSL HTF:** PWL, PDL, equal lows D1/H4, swing low quan trọng.
- **SSL đóng vai trò gì theo bias?**
  - Bullish → SSL phía dưới là nơi **chờ sweep để Long**.
  - Bearish → SSL phía dưới là **target chốt lời**.
- **Vị trí giá:** premium / discount / equilibrium so với dealing range.
- **Narrative:** giá có xu hướng bị hút xuống SSL tại ___ trước khi ___; invalid nếu ___.

```text
Mẫu ghi nhanh — Bullish Bias, dùng SSL làm sweep zone
HTF dealing range: [D1 low] → [D1 high]
Location: Discount / đang trôi xuống về SSL
SSL target để sweep: equal lows tại [level] (nằm dưới H1 bullish FVG)
Expected path: quét SSL → reclaim → bullish MSS trong POI → Long → target BSL trên
Invalidation: đóng nến H1/H4 dưới SSL và giữ giá (acceptance), không reclaim
```

```text
Mẫu ghi nhanh — Bearish Bias, dùng SSL làm target
HTF dealing range: [D1 low] → [D1 high]
Location: Premium / đang chạm bearish PD Array
SSL target chốt lời Short: PDL / equal lows tại [level]
Expected path: sweep BSL trên → bearish displacement → phân phối xuống → chốt tại SSL
Invalidation: sweep SSL xong xuất hiện reclaim + bullish MSS → ngừng kỳ vọng giảm
```

### H1 / M15 — POI & Context
- **POI bullish gần SSL:** ghi vùng cụ thể, ví dụ `H1 bullish FVG x.xxxx–x.xxxx`, nằm ngay trên cụm SSL.
- **SSL đã bị quét chưa?** xác định đáy bị lấy, độ sâu của wick, chất lượng reclaim.
- **Phản ứng sau sweep:** có displacement lên rõ không, hay giá chỉ đi ngang/giảm tiếp?
- **Phân biệt pullback vs reversal:** giá phá xuống dưới SSL khi đang Bullish có thể chỉ là **sweep để lấy thanh khoản** nếu reclaim ngay; đừng đổi bias chỉ vì một cú phá đáy.

### M5 / M1 — Confirmation & Entry
- **Có bullish MSS không?** MSS phải phá swing high nội bộ có ý nghĩa **sau khi** SSL bị sweep.
- **MSS có nằm trong POI không?** nếu ngoài POI hoặc giữa range → bỏ qua.
- **Có displacement lên không?** cần body đóng quyết đoán, để lại FVG.
- **Entry tại FVG/OB:** retrace vào imbalance hình thành từ displacement; stop nằm **dưới điểm sweep low** (dưới đáy vừa quét).
- **Target:** internal liquidity trước, external BSL chính sau.

> [!warning]
> **Chạm SSL ≠ tín hiệu Long.** SSL chỉ cho phép execution Long sau khi: sweep (quét xuống dưới) → reclaim → LTF MSS/displacement tại POI. Thiếu một bước là chưa có lệnh.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi (Long sau SSL sweep)
- [ ] SSL được xác định rõ và phù hợp HTF bias Bullish, nằm ở discount.
- [ ] Có POI bullish (FVG/OB) tại hoặc ngay trên SSL.
- [ ] Giá thực sự **quét xuống dưới SSL** (wick xuyên đáy).
- [ ] Giá **reclaim** trở lại trên SSL/range nhanh chóng.
- [ ] Có **bullish displacement** để lại FVG sau sweep.
- [ ] **Bullish MSS** hình thành trong / ngay sau POI.
- [ ] Target là BSL/liquidity còn mở phía trên, R:R đạt plan.

### Setup bị vô hiệu khi
- [ ] Giá đóng nến phá xuống dưới SSL và **giữ giá** (acceptance) → tiếp diễn giảm.
- [ ] Không có reclaim sau khi chạm/xuyên SSL.
- [ ] Không có displacement/MSS lên sau sweep.
- [ ] MSS xảy ra ngoài POI hoặc giữa range.
- [ ] Cố Long chỉ vì giá **chạm** SSL, chưa sweep + reclaim.
- [ ] Long ngược HTF bias (Bearish) mà không có counter-trend playbook.

### Phân biệt "Sweep SSL (reversal)" vs "Phá xuống tiếp diễn (acceptance)"

| Quan sát | Cách đọc hợp lý | Hành động |
|---|---|---|
| Wick nhanh xuyên dưới SSL rồi **đóng lại trên**, kèm bullish displacement | **Sweep → reversal**: stop hunt rồi gom thanh khoản mua | Chờ MSS lên tại POI → Long, stop dưới sweep low |
| Body nến **đóng dưới SSL**, các pullback không reclaim được level | **Acceptance → tiếp diễn giảm** | KHÔNG Long; nếu Bearish, đây là tiếp tục về SSL kế tiếp |
| Giá chỉ đến gần SSL, chưa xuyên rõ, đứng do dự | Chưa có sweep | Chờ; chưa đủ điều kiện |
| Quét SSL nhưng không displacement, đi ngang | Sweep yếu / chưa rõ | Không vội; cần displacement + MSS xác nhận |
| Nhiều cú quét nhỏ liên tiếp dưới đáy, mỗi lần phá sâu thêm | SSL đang bị "ăn mòn" theo hướng giảm | Thiên về tiếp diễn, không bắt đáy |

> [!important]
> Khác biệt sống còn: **sweep là wick xuyên rồi reclaim**; **acceptance là body đóng dưới và ở lại**. Quy tắc: không Long khi giá vẫn còn ở dưới SSL chưa reclaim.

---

## 6. Ví dụ chart

### Ví dụ đúng — Sweep SSL (equal lows) rồi Long theo Bullish Bias
![[Sell-side Liquidity-Example-Correct.png]]

**Mô tả:**  
D1/H4 Bullish, draw on liquidity chính là BSL phía trên. Giá retrace về discount, ngay dưới một H1 bullish FVG có cụm **equal lows** (engineered SSL). Trong New York Kill Zone, giá quét xuống dưới equal lows — trigger stop của các lệnh Long, tạo ra lượng lệnh bán làm thanh khoản. Giá lập tức **reclaim** trở lại, M5 tạo **bullish MSS + displacement** để lại FVG. Entry tại FVG retrace; stop dưới sweep low; TP hướng về BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- SSL là engineered liquidity (equal lows) → magnet mạnh, dễ bị quét.
- **Sweep xảy ra TRƯỚC reversal**, đúng thứ tự stop hunt → reverse.
- Sweep + reclaim + MSS + displacement nằm trong POI ở discount, thuận HTF bias.
- Stop loss đặt **dưới điểm sweep** — nơi market vừa quét xong, ít có lý do quay lại.

### Ví dụ sai / dễ nhầm — Long vì giá "chạm đáy" nhưng giá phá tiếp
![[Sell-side Liquidity-Example-Wrong.png]]

**Mô tả lỗi:**  
Giá giảm mạnh tới một swing low; trader cho rằng "đây là SSL, hỗ trợ, mua được". Nhưng HTF đang Bearish, target SSL thật nằm thấp hơn. Giá **đóng nến body dưới đáy** và giữ giá (acceptance) — đây là tiếp diễn giảm, không phải sweep. Không có reclaim, không có MSS lên. Lệnh Long bị quét stop khi giá tiếp tục phân phối xuống SSL kế tiếp.

**Bài học:**
- **Chạm SSL không phải tín hiệu Long.** Đáy là nơi tập trung lệnh bán, không phải vùng an toàn.
- Phải phân biệt **sweep (wick + reclaim)** với **acceptance (body đóng dưới, giữ giá)**.
- Khi HTF Bearish, SSL phía dưới là **target**, không phải vùng để bắt đáy ngược bias.
- Hỏi: "Giá đã reclaim chưa? Có MSS lên trong POI chưa?" Nếu chưa → không có lệnh.

---

### Sequence mẫu — Long sau khi sweep SSL (thuận Bullish bias)
```text
HTF Bullish Bias
→ HTF Dealing Range
→ Giá về Discount + Bullish PD Array
→ SSL (equal lows / swing low) nằm dưới POI
→ SWEEP SSL (quét stop của Long, gom thanh khoản mua)
→ RECLAIM trở lại trên SSL
→ Bullish MSS trong POI
→ Displacement tạo FVG/OB
→ Retrace vào FVG/OB (M5/M1)
→ Stop DƯỚI sweep low (dưới đáy vừa quét)
→ Target: Internal liquidity trước, External BSL chính sau
```

### Sequence mẫu — Short dùng SSL làm target (thuận Bearish bias)
```text
HTF Bearish Bias
→ HTF Dealing Range
→ Giá về Premium + Bearish PD Array
→ Sweep BSL phía trên
→ Bearish MSS trong POI
→ Displacement tạo FVG/OB
→ Retrace vào FVG/OB (M5/M1)
→ Stop sau swing high / sweep high logic
→ Target: SSL phía dưới (PDL / equal lows) → chốt lời tại đó
→ Lưu ý: tại SSL, canh khả năng reversal Long nếu xuất hiện sweep + reclaim + MSS lên
```

> [!note]
> SSL là **đối xứng** với [[07 - Buy-side Liquidity]] (BSL): BSL là cụm buy stop nằm TRÊN thị trường (dưới các đỉnh, equal highs, swing high, PDH/PWH), bị quét trước khi đảo chiều Short. SSL và BSL là cặp ảnh phản chiếu — quét BSL để Short, quét SSL để Long. Hiểu một bên là hiểu cả cặp; chỉ cần lật ngược logic premium↔discount, trên↔dưới, sell stop↔buy stop.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Chạm SSL không phải tín hiệu. Khái niệm ICT chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**.

### A. Context (HTF)
- [ ] Tôi xác định đúng cụm SSL chính và level cụ thể (equal lows / PDL / PWL / swing low).
- [ ] Tôi biết SSL này là **target** (Bearish) hay **sweep zone** (Bullish).
- [ ] HTF bias rõ ràng; SSL phù hợp với bias đó.
- [ ] Có POI bullish gần SSL nếu kế hoạch là Long sau sweep.
- [ ] SSL còn mở (chưa bị lấy), nằm ở discount cho kịch bản Long.
- [ ] Ghi điều kiện invalidation: đóng nến giữ giá dưới SSL = acceptance.

### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã **quét xuống dưới SSL** (sweep), không chỉ chạm.
- [ ] Có **reclaim** trở lại trên SSL/range.
- [ ] Có **bullish displacement** để lại FVG.
- [ ] **Bullish MSS** hình thành trong / ngay sau POI.
- [ ] Entry tại FVG/OB; stop **dưới sweep low**.
- [ ] Target là BSL/liquidity còn mở; đường tới target không bị cản bởi liquidity gần hơn.
- [ ] R:R tối thiểu đạt plan; không vượt risk limit.

### C. Quy tắc "không có lệnh"
- [ ] Giá chỉ **chạm** SSL, chưa sweep + reclaim → không Long.
- [ ] Giá đóng nến giữ giá dưới SSL (acceptance) → không bắt đáy.
- [ ] Không có MSS lên / displacement sau sweep → không trade.
- [ ] SSL ngược HTF bias không có counter-trend playbook → không trade.
- [ ] Bias Neutral / nhiều cụm SSL không rõ ưu tiên → đứng ngoài.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Coi SSL là "hỗ trợ để mua" | Long ngay khi giá chạm đáy/SSL | Đáy là nơi dồn lệnh bán; market thường quét sâu hơn | Chờ sweep + reclaim + MSS; không mua tại level chạm |
| Long khi chỉ **chạm** SSL | Vào lệnh trước khi giá xuyên đáy | Stop của bạn nằm đúng nơi market còn muốn quét | Chỉ Long sau khi SSL đã bị sweep và giá reclaim |
| Nhầm acceptance với sweep | Body đóng dưới SSL nhưng vẫn cố bắt đáy | Acceptance = tiếp diễn giảm, không reversal | Phân biệt: wick + reclaim (sweep) vs body đóng dưới + giữ giá (acceptance) |
| Bắt đáy ngược Bearish bias | HTF giảm nhưng Long vì "đã giảm nhiều rồi" | SSL phía dưới là target, giá còn phân phối tiếp | Khi Bearish, dùng SSL làm target chốt Short, không Long |
| Đặt stop ngay tại SSL | Stop loss đặt đúng dưới đáy chuẩn | Đó chính là nơi sell stops nằm; dễ bị quét | Đặt stop dưới điểm sweep, có buffer; tránh đặt tại cụm thanh khoản rõ |
| Bỏ qua equal lows | Không nhận ra engineered SSL | Equal lows là magnet mạnh, giá rất dễ quét xuống | Đánh dấu mọi equal lows / relative equal lows làm SSL ưu tiên |
| Long mà không có displacement | Thấy sweep rồi vào ngay, không chờ xác nhận | Sweep mà không displacement chưa đủ bằng chứng reversal | Bắt buộc có displacement + MSS lên sau sweep |
| Chốt Short quá sớm trước SSL | Đóng lệnh trước khi giá tới SSL target | Bỏ lỡ phần lớn leg phân phối tới thanh khoản | Giữ tới SSL hợp lý; chốt từng phần quanh internal trước, external SSL sau |
| Long giữa range | MSS lên ở giữa, không gần SSL/POI | Đó có thể là internal repricing, không phải reversal thật | Chỉ Long sau sweep SSL tại discount + POI |
| Đổi bias vì một cú phá đáy | Bullish nhưng hoảng khi giá xuyên SSL | Có thể chỉ là sweep để lấy thanh khoản rồi reverse | Chờ xem reclaim; chỉ đổi bias khi acceptance rõ |

---

## 10. Câu hỏi tự kiểm tra

- Tôi có thể giải thích SSL là gì (lệnh sell chờ dưới thị trường) trong 30 giây không?
- Cụm SSL chính hôm nay nằm ở level nào? Là equal lows, PDL/PWL hay swing low?
- SSL này là **target** (Bearish) hay **sweep zone** (Bullish) theo bias của tôi?
- SSL đã bị lấy chưa, hay còn mở để hút giá xuống?
- Cú phá đáy vừa rồi là **sweep** (wick + reclaim) hay **acceptance** (body đóng dưới, giữ giá)?
- Tôi có đang định Long chỉ vì giá **chạm** SSL không? (Nếu có → dừng lại.)
- Sau sweep, đã có reclaim + bullish MSS + displacement tại POI chưa?
- Stop của tôi có đang đặt đúng tại cụm SSL — nơi dễ bị quét — không?
- Equal lows trên chart đã được tôi đánh dấu là engineered SSL chưa?
- Nếu không Long, lý do "No Trade" của tôi tại SSL là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Sell-side Liquidity (SSL) là gì và nằm ở đâu so với giá?  
**Đáp:** Là cụm lệnh sell chờ (chủ yếu sell stop = stop loss của Long + sell-stop của breakout trader) nằm **dưới** thị trường, tập trung dưới previous lows, equal lows, swing lows, session lows, PDL/PWL.

### Q2
**Hỏi:** SSL đóng hai vai trò nào?  
**Đáp:** (1) **Draw/target** khi giá đang bị hút xuống (đặc biệt cho lệnh Short chốt lời); (2) **Vùng sweep** để quét trước khi đảo chiều Long.

### Q3
**Hỏi:** Vì sao quét SSL thường dẫn tới leg tăng?  
**Đáp:** Quét xuống dưới đáy → trigger stop loss của các lệnh Long → tạo ra lượng lệnh bán; smart money dùng đám lệnh bán đó làm thanh khoản để **mua**, rồi đẩy giá lên (stop hunt → reverse).

### Q4
**Hỏi:** Equal lows là loại SSL gì và vì sao quan trọng?  
**Đáp:** Là **engineered SSL** — thanh khoản được "tạo" để dụ trader đặt stop/breakout bên dưới; là magnet rất hấp dẫn nên giá thường quét xuống dưới chúng trước.

### Q5
**Hỏi:** Phân biệt "sweep SSL" và "phá xuống tiếp diễn"?  
**Đáp:** Sweep = wick xuyên dưới SSL rồi **reclaim** + displacement lên → tín hiệu reversal Long. Tiếp diễn = body nến **đóng dưới SSL và giữ giá** (acceptance) → tiếp tục giảm, KHÔNG phải tín hiệu Long.

### Q6
**Hỏi:** Có được Long ngay khi giá chạm SSL không?  
**Đáp:** Không. Cần đủ thứ tự: **sweep SSL → reclaim → LTF MSS/displacement tại POI**. Chỉ chạm SSL là chưa đủ và rất rủi ro.

### Q7
**Hỏi:** SSL liên hệ thế nào với BSL?  
**Đáp:** SSL và BSL là **cặp ảnh phản chiếu**. BSL là buy stop nằm TRÊN (dưới các đỉnh/equal highs), bị quét trước khi đảo Short; SSL nằm DƯỚI, bị quét trước khi đảo Long. Lật ngược logic trên↔dưới, premium↔discount.

### Q8
**Hỏi:** Nên đặt stop loss của lệnh Long (sau sweep SSL) ở đâu?  
**Đáp:** **Dưới điểm sweep low** (dưới đáy vừa quét), có buffer — không đặt ngay tại cụm SSL chuẩn vì đó là nơi thanh khoản dễ bị quét.

---
## 12. Lesson Learned

### Bài học chính
- SSL là **nam châm hút giá xuống**, không phải hỗ trợ. Giá đi tới SSL để **lấy** thanh khoản, không phải để dừng lại an toàn.
- Cùng một SSL vừa là **target chốt Short** vừa là **điểm canh Long** — tùy giá đang ở đâu trong narrative.
- Sự khác biệt sống còn là **sweep (wick + reclaim) vs acceptance (body đóng dưới, giữ giá)**: một bên là reversal, một bên là tiếp diễn.
- **Equal lows = engineered liquidity**; gần như luôn cần giả định giá sẽ quét chúng trước khi đi hướng thật.
- Stop loss không bao giờ nên nằm đúng tại cụm SSL chuẩn — đó là nơi market muốn quét.

### Quy tắc cá nhân rút ra
- [ ] Tôi không Long chỉ vì giá **chạm** SSL; cần sweep + reclaim + MSS/displacement tại POI.
- [ ] Tôi luôn phân biệt sweep và acceptance trước khi kết luận reversal.
- [ ] Khi Bearish, tôi dùng SSL làm **target**, không bắt đáy ngược bias.
- [ ] Tôi đặt stop **dưới sweep low**, không đặt ngay tại đáy/equal lows.
- [ ] Tôi đánh dấu mọi equal lows / PDL / PWL như SSL ưu tiên trong pre-market.

### Câu nhắc nhở khi trade
> **"Đáy không phải nơi để mua. Đáy là nơi thanh khoản nằm. Chỉ Long sau khi giá quét nó rồi reclaim — không trước."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có giải thích được SSL = sell stop dưới thị trường, hai vai trò draw/sweep không? |
| Nhận diện trên chart |  | Có đánh dấu đúng equal lows, PDL/PWL, swing low làm SSL không? |
| Biết khi nào bỏ qua |  | Có phân biệt được sweep vs acceptance, và không bắt đáy khi acceptance không? |
| Kết hợp với context HTF |  | SSL có được dùng đúng vai trò theo bias (target vs sweep zone) không? |
| Áp dụng vào trade thực tế |  | Long có thực sự xảy ra sau sweep + reclaim + MSS tại POI không? |
| Review sau trade |  | Có kiểm tra bằng journal liệu "sweep + reclaim" có edge hơn "chạm là mua" không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[Sell-side Liquidity]]`.
- [ ] Review riêng các lệnh Long sau **sweep** đúng quy trình vs các lần bắt đáy lúc **acceptance**.
- [ ] Thống kê win rate, average R theo `sweep_or_acceptance` và `reclaim_confirmed`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.