---
type: ict-concept
concept: AMD
aliases:
  - AMD
  - Accumulation Manipulation Distribution
  - Power of 3
  - PO3
  - Po3
tags:
  - trading/ict/concept
  - trading/study
  - "#AMD"
status: developing
category: Market Model
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
models:
  - "[[Trading Journal/02 - Trading Knowledge/Models/ICT 2022 Model|ICT 2022]]"
importance: 4
last_reviewed: 2026-06-22
created: 2026-06-22
updated: 2026-07-02
common_mistakes:
  - "[[Mistake - Trade The Manipulation Leg]]"
  - "[[Mistake - Breakout During Accumulation]]"
  - "[[Mistake - Ignore Daily Open]]"
---

# AMD — Accumulation, Manipulation, Distribution (Power of 3)

> [!summary] Tóm tắt 1 câu
> **AMD (Power of 3) là mô hình mô tả cách một cây nến HTF / một phiên được xây dựng qua 3 giai đoạn — Tích lũy (range), Thao túng (Judas swing quét liquidity sai hướng), và Phân phối (expansion theo hướng thật) — giúp xác định bẫy và điểm vào theo hướng phân phối.**

> [!important] Nguyên tắc cốt lõi
> **Move bạn nhìn thấy đầu tiên (manipulation/Judas) thường là move SAI; move thật (distribution) đi ngược lại nó. Đừng đuổi theo giai đoạn thao túng — chờ nó quét liquidity rồi vào theo hướng phân phối.**
> AMD đặt mọi thứ vào trật tự thời gian: tích lũy → bẫy → chạy thật. Daily Open là mốc tham chiếu trung tâm.

---

## 1. Định nghĩa

**Khái niệm:**
AMD (Accumulation – Manipulation – Distribution), còn gọi **Power of 3 (PO3)**, mô tả cấu trúc 3 pha mà một cây nến lớn (daily, weekly) hoặc một phiên giao dịch hình thành:

- **Accumulation (Tích lũy):** giá đi ngang trong một range hẹp quanh mức mở cửa (thường là phiên Á / đầu ngày). Smart money âm thầm gom vị thế; đám đông thấy "không có gì xảy ra".
- **Manipulation (Thao túng / Judas Swing):** một cú đẩy giả theo hướng NGƯỢC với ý định thật, để **quét liquidity** (stop) ở một phía của range và **bẫy** trader vào sai hướng. Đây là "Judas swing" — phản bội kỳ vọng đám đông.
- **Distribution (Phân phối):** move thật, expansion mạnh theo hướng đã định, chạy về pool liquidity mục tiêu. Đây là nơi smart money "phân phối" vị thế đã gom.

![[AMD-Advanced-PO3-Candle-Anatomy.svg|697]]

**Vai trò của Daily Open:** mức mở cửa ngày là mốc tham chiếu trung tâm. Trong một ngày bullish điển hình: giá tích lũy quanh open → thao túng XUỐNG dưới open (sweep SSL) → phân phối LÊN, đóng cửa gần đỉnh ngày. Ngày bearish thì đối xứng.

**Đọc ngược từ nến D1:** một nến daily bullish với **wick dưới dài** chính là "hóa thạch" của AMD — wick là dấu vết Judas, body là dấu vết phân phối. Kỹ năng nâng cao là nhìn nến D1/W1 *chưa đóng* và tự hỏi: "wick của nến này đã được in chưa?" Nếu bias bullish mà ngày chưa có nhịp xuống dưới open, xác suất cao move giảm buổi sáng chỉ đang "xây wick" — đó là nơi tìm Long, không phải lý do hoảng loạn.

**Vì sao thị trường PHẢI có manipulation (logic thanh khoản):** lệnh lớn của smart money cần counterparty. Muốn mua khối lượng lớn mà không đẩy giá chạy mất, họ cần một lượng lớn lệnh **bán** xuất hiện cùng lúc — thứ chỉ có được bằng cách đẩy giá xuống quét sell-stop (stop của phe mua + lệnh sell breakout). Judas swing không phải "âm mưu" thần bí; nó là **cơ chế bơm thanh khoản** để vị thế lớn được khớp. Hiểu điều này giúp bạn tin vào khung AMD một cách có cơ sở thay vì thuộc lòng.

**Liên hệ với chu kỳ thị trường:** AMD là phiên bản "vi mô intraday" của chu kỳ accumulation–distribution kinh điển. Nó ghép trực tiếp với [[18 - Kill Zones]] (thao túng thường xảy ra đầu London / NY, phân phối trong kill zone chính) và với [[20 - Liquidity Sweep]] (giai đoạn manipulation CHÍNH LÀ cú sweep).

**Mục đích trong ICT:**
- Cho **bản đồ thời gian trong ngày**: biết đang ở pha nào để không trade nhầm.
- Giải thích **vì sao breakout thường fail**: breakout xảy ra trong/ngay sau manipulation, bị bẫy.
- Định vị **điểm vào**: vào theo distribution, SAU khi manipulation đã quét liquidity.
- Kết nối **bias + kill zone + sweep** thành một câu chuyện mạch lạc trong ngày.

**Vì sao khái niệm này quan trọng:**
Phần lớn trader thua vì họ trade **giai đoạn thao túng** — họ thấy giá phá range và đuổi theo, đúng lúc đó là bẫy. AMD dạy bạn nhận ra "đây là Judas swing, không phải move thật", chờ nó hoàn tất, rồi vào theo phân phối. Đây là khung tổ chức toàn bộ ngày giao dịch.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Hiện tại đang ở pha nào: tích lũy, thao túng, hay phân phối?
- Cú phá range vừa rồi là move thật hay Judas swing (bẫy)?
- Manipulation đã quét pool liquidity nào, theo hướng nào?
- Phân phối sẽ chạy về pool liquidity nào (target)?
- Daily Open ở đâu, giá đang trên hay dưới nó?

### AMD không phải là gì
- Không phải chỉ báo định giờ chính xác — pha có thể dài/ngắn khác nhau, cần đọc price action.
- Không phải mọi ngày đều có AMD đẹp; ngày tin tức / range lớn có thể méo mó.
- Không phải lý do trade breakout của range tích lũy.
- Không phải tín hiệu entry độc lập — vẫn cần POI + sweep + LTF confirm.
- Không cố định một chiều; ngày bullish và bearish có AMD đối xứng.

---

## 2. Bối cảnh sử dụng

### Ba pha của AMD

| Pha | Đặc điểm | Hành động đúng |
|---|---|---|
| **Accumulation** | Range hẹp quanh Daily Open (thường phiên Á) | KHÔNG trade breakout; đánh dấu range high/low (liquidity) |
| **Manipulation (Judas)** | Cú phá giả quét liquidity 1 phía, thường đầu London/NY | KHÔNG đuổi theo; chờ sweep + reclaim |
| **Distribution** | Expansion mạnh theo hướng thật về pool target | Vào theo hướng phân phối sau sweep + MSS |

### AMD theo hướng ngày

| Ngày | Accumulation | Manipulation | Distribution |
|---|---|---|---|
| **Bullish day** | Range quanh open | Thao túng XUỐNG, sweep SSL dưới range/open | Phân phối LÊN, đóng gần đỉnh ngày |
| **Bearish day** | Range quanh open | Thao túng LÊN, sweep BSL trên range/open | Phân phối XUỐNG, đóng gần đáy ngày |

> [!tip]
> Ghép AMD với [[18 - Kill Zones]]: thường **Asia = accumulation**, **London open = manipulation (Judas)**, **London/NY = distribution**. NY cũng có thể có một Judas riêng đầu phiên trước khi phân phối tiếp.

![[AMD-Advanced-Session-Timeline.svg|697]]

### Nâng cao — PO3 là fractal: Weekly → Daily → Session

AMD không chỉ chạy ở khung ngày. Cùng logic A→M→D lặp lại ở **mọi cấp thời gian**, và các cấp lồng vào nhau:

- **Weekly PO3:** tuần bullish điển hình tích lũy Thứ 2, in **low của tuần vào Thứ 2–Thứ 3** (Judas tuần, thường quét dưới Weekly Open), phân phối Thứ 3–Thứ 5, đóng tuần gần đỉnh. Hệ quả: nếu bias tuần bullish mà Thứ 2 đang giảm — đó có thể là manipulation của *tuần*, không phải trend giảm mới.
- **Daily PO3:** khung "chuẩn" của note này — một nến D1 xây bằng 3 pha quanh midnight open.
- **Session PO3:** ngay trong một phiên NY AM cũng có accumulation nhỏ (trước 08:30), Judas đầu phiên (quét pool London để lại), rồi phân phối. Dùng cấp này cho timing M5/M1.

**Điểm mấu chốt:** xác suất cao nhất khi các cấp **đồng pha** — ví dụ Judas ngày (London sweep) xảy ra đúng lúc tuần cũng cần in low tuần: khi đó phân phối của ngày *chính là* một phần phân phối của tuần, move thường chạy xa và sạch. Ngược lại khi ngày và tuần lệch pha (ngày muốn lên nhưng tuần đang cần quét đỉnh), phân phối ngày dễ bị "cụt".

![[AMD-Advanced-Fractal-PO3.svg|697]]

### Khi nào khái niệm này có giá trị cao?
- [ ] Có range tích lũy rõ (phiên Á) với high/low xác định làm liquidity.
- [ ] Daily Bias rõ để biết hướng phân phối kỳ vọng.
- [ ] Manipulation quét đúng pool liquidity ngược hướng bias (Judas).
- [ ] Phân phối bắt đầu trong kill zone với displacement + MSS.
- [ ] Có pool liquidity HTF rõ làm target cho phân phối.

### Khi nào nên bỏ qua?
- [ ] Ngày tin tức lớn làm cấu trúc méo / range bất thường.
- [ ] Không xác định được range tích lũy / Judas (giá trend thẳng).
- [ ] Đã ở cuối pha phân phối, giá chạy xa — entry thành chase.
- [ ] Bias không rõ (neutral) → khó biết hướng phân phối.
- [ ] Ngoài kill zone / ngoài plan.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Range tích lũy:** vùng đi ngang quanh Daily Open; đánh dấu high/low của range.
2. **Judas swing:** cú phá range theo một hướng, có wick/sweep, KHÔNG được duy trì.
3. **Reclaim:** giá quay lại range / về phía Daily Open sau Judas.
4. **Displacement + MSS:** move phân phối phá cấu trúc theo hướng thật.
5. **Expansion về target:** giá chạy mạnh về pool liquidity HTF, ít retrace.

### Ma trận nhận diện AMD

| Thành phần | Bullish day | Bearish day | Cảnh báo |
|---|---|---|---|
| **Accumulation** | Range quanh open | Range quanh open | Không có range rõ |
| **Manipulation** | Judas XUỐNG, sweep SSL | Judas LÊN, sweep BSL | Phá range mà giữ luôn (có thể trend day) |
| **Reclaim** | Quay lại trên đáy range/open | Quay lại dưới đỉnh range/open | Không reclaim |
| **Distribution** | Expansion LÊN | Expansion XUỐNG | Đi ngang tiếp |
| **Target** | BSL phía trên | SSL phía dưới | Không có pool rõ |

### Điều kiện bắt buộc
- [ ] Xác định Daily Open và range tích lũy (high/low).
- [ ] Nhận ra Judas swing và pool liquidity nó quét.
- [ ] Có reclaim + displacement xác nhận phân phối.
- [ ] Xác định pool target của phân phối.

### Điều kiện tăng xác suất
- [ ] Judas đúng pool ngược hướng bias (sweep "đẹp").
- [ ] Phân phối có MSS + để lại FVG để refine entry.
- [ ] Diễn ra trong kill zone phù hợp.
- [ ] Có HTF draw on liquidity rõ làm target.

### Điều kiện làm setup yếu đi
- Range tích lũy mơ hồ / quá rộng.
- Judas không quét pool rõ ràng.
- Phân phối yếu, không displacement.
- Ngày có nhiều cú phá hai chiều (whipsaw) không theo cấu trúc.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình 4 câu bắt buộc trước khi dùng AMD
> 1. **Range tích lũy và Daily Open ở đâu?**
> 2. **Đã có Judas swing chưa, nó quét pool liquidity nào?**
> 3. **Phân phối đã bắt đầu chưa (reclaim + displacement + MSS)?**
> 4. **Phân phối chạy về pool target nào, và tôi đang ở pha nào?**

### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[12 - Daily Bias]]) → quyết định hướng phân phối kỳ vọng.
- **Daily Open & pool HTF:** đánh dấu open, PDH/PDL, range Á — đây là các mốc liquidity của AMD.
- **Draw on liquidity:** pool nào là target cuối của phân phối.

### H1 / M15 — POI & Context
- **Range tích lũy:** xác định high/low range Á; đánh dấu là liquidity hai phía.
- **Judas + POI:** Judas swing quét phía nào? POI (FVG/OB) nơi phân phối có thể bắt đầu.
- **Reclaim:** giá đã quay lại range / qua Daily Open chưa?

### M5 / M1 — Confirmation & Entry
- **Xác nhận phân phối:** sau Judas + sweep, chờ M5/M1 reclaim + MSS + displacement.
- **Entry:** tại FVG/OB của nhịp phân phối, hoặc retest mép range vừa reclaim.
- **Stop loss logic:** ngoài cực điểm của Judas swing (sweep low/high).
- **Target:** pool liquidity HTF của phân phối.

```text
Mẫu ghi nhanh — Bullish AMD (Long)
Daily Bias: Bullish
Accumulation: range Á [low]–[high], Daily Open [..]
Manipulation: Judas XUỐNG sweep SSL tại [level]
Reclaim: giá đóng lại trên đáy range/open
Distribution: displacement LÊN + MSS → FVG [range]
Entry: FVG/OB nhịp phân phối
Stop: dưới đáy Judas ([sweep low])
Target: BSL [level]
Pha hiện tại: Distribution (early)
```

```text
Mẫu ghi nhanh — Bearish AMD (Short)
Daily Bias: Bearish
Accumulation: range Á [low]–[high], Daily Open [..]
Manipulation: Judas LÊN sweep BSL tại [level]
Reclaim: giá đóng lại dưới đỉnh range/open
Distribution: displacement XUỐNG + MSS → FVG [range]
Entry: FVG/OB nhịp phân phối
Stop: trên đỉnh Judas ([sweep high])
Target: SSL [level]
Pha hiện tại: Distribution (early)
```

> [!warning]
> **Cú phá range ĐẦU TIÊN thường là Judas, không phải phân phối.** Nếu bạn vào ngay khi giá phá range tích lũy, khả năng cao bạn đang trade giai đoạn thao túng. Chờ sweep + reclaim + displacement.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Xác định rõ accumulation (range) + Daily Open.
- [ ] Judas swing đã quét pool liquidity đúng (ngược hướng bias).
- [ ] Có reclaim + displacement + MSS xác nhận phân phối.
- [ ] Entry tại POI nhịp phân phối, đồng hướng Daily Bias.
- [ ] Stop ngoài cực điểm Judas; target là pool liquidity HTF.
- [ ] Diễn ra trong kill zone phù hợp; R:R đạt kế hoạch.

### Setup bị vô hiệu khi
- [ ] Giá phá range và **giữ luôn** không reclaim → có thể là trend day / không theo AMD chuẩn.
- [ ] Không xác định được Judas / range → bỏ khung AMD cho ngày đó.
- [ ] Phân phối không có displacement/MSS → chưa xác nhận.
- [ ] Entry ngược Daily Bias.
- [ ] Đã ở cuối phân phối, giá chạy xa.

### Accumulation vs Manipulation vs Distribution (cách đọc)

| Quan sát | Pha | Cách đọc hợp lý |
|---|---|---|
| Range hẹp, đi ngang quanh open | **Accumulation** | Chờ; đánh dấu liquidity; KHÔNG trade breakout |
| Phá range 1 phía rồi quay lại | **Manipulation (Judas)** | Đây là sweep; chờ reclaim, chuẩn bị vào hướng ngược |
| Expansion mạnh, MSS, ít retrace | **Distribution** | Vào theo hướng này (sau sweep), giữ tới pool target |
| Phá range và giữ, trend thẳng | **Trend day / ngoài AMD** | Dùng model trend, không ép khung AMD |

![[AMD-Advanced-Trend-Day-Filter.svg]]

### Nâng cao — Nhận diện sớm Trend Day (khi AMD không áp dụng)

Trend day là "kẻ thù" lớn nhất của trader AMD: bạn chờ Judas quay đầu nhưng nó không bao giờ quay. Dấu hiệu cảnh báo sớm:

- Cú phá range Á có **đóng nến H1 bên ngoài range** và pullback sau đó **không về được Daily Open** (pullback nông, dạng bear/bull flag).
- Phá range **thuận hướng bias HTF** ngay từ đầu ngày — khi HTF đang cần chạy về một draw lớn, thị trường có thể bỏ qua nghi thức Judas.
- Ngày có **tin lớn** (CPI, FOMC, NFP): cấu trúc AMD thường bị nén trước tin và bùng nổ một chiều sau tin.
- Range Á **quá hẹp bất thường** so với ADR — năng lượng nén thường giải phóng thành trend một chiều.

Kỷ luật đi kèm: **quy tắc 2 lần thử** — nếu đã bị stop một lần vì "tưởng Judas" mà giá vẫn không reclaim, ngừng đánh ngược; hoặc đứng ngoài, hoặc chuyển sang trade *theo* hướng phá với pullback nông. Không có lần thứ ba.

> [!note]
> AMD không phải đồng hồ bấm giờ; nó là **trật tự logic**. Có ngày accumulation kéo dài, có ngày Judas rất nhanh. Đọc price action (sweep + reclaim + displacement) quan trọng hơn canh đúng phút.

---

## 6. Ví dụ chart

### Ví dụ đúng — Tích lũy → Thao túng (Judas) → Phân phối, Long
![[AMD-Example-Correct.png]]

**Mô tả:**
Daily Bias Bullish. Phiên Á **tích lũy** trong range hẹp quanh Daily Open. Đầu London, một **Judas swing xuống** quét SSL dưới đáy range (bẫy phe bán / quét stop phe mua). Giá nhanh chóng reclaim trên đáy range, rồi một **displacement tăng** phá cấu trúc (MSS bullish) mở ra giai đoạn **phân phối**. Entry tại FVG/OB của nhịp phân phối; stop dưới đáy Judas; target BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- Ba pha rõ ràng, đúng trật tự, đồng hướng bias bullish.
- Judas quét đúng SSL trước khi phân phối — không đuổi theo cú phá giả.
- Entry SAU sweep, trong giai đoạn phân phối, stop ngoài cực điểm Judas.
- Target là pool liquidity rõ (BSL).

### Ví dụ sai / dễ nhầm — Short theo Judas swing (nhầm thao túng là move thật)
![[AMD-Example-Wrong.png]]

**Mô tả lỗi:**
Trong một ngày bullish, giá tích lũy rồi đẩy XUỐNG (manipulation). Trader thấy "giá đang giảm mạnh, phá đáy range" và **Short ngay tại đáy Judas**, tưởng đó là move thật. Nhưng đó chính là giai đoạn **thao túng**: ngay sau khi quét SSL, giá đảo chiều phân phối LÊN, quét sạch stop của lệnh Short.

**Bài học:**
- Cú phá range đầu tiên thường là **Judas**, không phải distribution.
- Đừng trade giai đoạn thao túng; chờ sweep + reclaim + displacement rồi vào theo phân phối.
- Luôn hỏi: "Đây là move thật hay đang bị bẫy?" — đối chiếu với Daily Bias.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[18 - Kill Zones]] — KHI NÀO mỗi pha thường xảy ra
- [[20 - Liquidity Sweep]] — pha manipulation chính là cú sweep
- [[21 - Market Structure Shift]] — xác nhận chuyển từ manipulation sang distribution
- [[12 - Daily Bias]] — quyết định hướng phân phối kỳ vọng
- [[13 - FVG  - Fair Value Gap]] / [[25 - OB - Order Block]] / [[26 - OTE - Optimal Trade Entry]] — refine entry trong pha phân phối
- [[08 - Central Bank Dealers Range]] — range Á làm khung accumulation
- [[33 - Turtle Soup]] — mô hình trade trực tiếp cú Judas

### Sequence mẫu — Long với Bullish AMD
```text
Daily Bias: Bullish
→ Accumulation: range Á quanh Daily Open (đánh dấu SSL/BSL range)
→ Kill zone London: Manipulation (Judas XUỐNG) sweep SSL
→ Reclaim trên đáy range / Daily Open
→ Distribution: displacement LÊN phá cấu trúc (MSS) → FVG
→ Entry tại FVG/OB nhịp phân phối (lý tưởng OTE/discount)
→ Stop dưới đáy Judas
→ Target: Internal liquidity → External BSL
```

### Sequence mẫu — Short với Bearish AMD
```text
Daily Bias: Bearish
→ Accumulation: range Á quanh Daily Open
→ Kill zone London: Manipulation (Judas LÊN) sweep BSL
→ Reclaim dưới đỉnh range / Daily Open
→ Distribution: displacement XUỐNG phá cấu trúc (MSS) → FVG
→ Entry tại FVG/OB nhịp phân phối (lý tưởng OTE/premium)
→ Stop trên đỉnh Judas
→ Target: Internal liquidity → External SSL
```

> [!note]
> AMD là "khung kể chuyện" cho cả ngày; [[20 - Liquidity Sweep]] là pha manipulation, [[21 - Market Structure Shift]] xác nhận chuyển sang distribution, còn [[Fair Value Gap]]/[[Order Block]]/[[Optimal Trade Entry]] là cách refine entry trong pha phân phối. [[18 - Kill Zones]] cho biết KHI NÀO mỗi pha thường xảy ra.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Biết đang ở pha nào quan trọng hơn vào lệnh. Chỉ vào trong pha phân phối, sau sweep.

### A. Context (HTF)
- [ ] Daily Bias đã rõ → hướng phân phối kỳ vọng.
- [ ] Daily Open và range tích lũy đã xác định.
- [ ] Pool liquidity hai phía range đã đánh dấu.
- [ ] Có draw on liquidity HTF làm target.

### B. Execution (LTF / trong ngày)
- [ ] Đã nhận ra Judas swing và pool nó quét.
- [ ] Có reclaim + displacement + MSS xác nhận phân phối.
- [ ] Entry tại POI nhịp phân phối, đồng hướng bias.
- [ ] Diễn ra trong kill zone phù hợp.
- [ ] Stop ngoài cực điểm Judas; target pool HTF; R:R đạt kế hoạch.

### C. Quy tắc "không có lệnh"
- [ ] Đang ở pha accumulation → không trade breakout.
- [ ] Đang ở pha manipulation (chưa reclaim) → không đuổi theo.
- [ ] Không xác định được Judas/range → bỏ khung AMD.
- [ ] Entry ngược Daily Bias → không trade.
- [ ] Đã cuối phân phối, chạy xa → không chase.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade giai đoạn thao túng | Đuổi theo cú phá range đầu tiên | Đó là Judas/bẫy, sắp đảo | Chờ sweep + reclaim + displacement |
| Breakout của accumulation | Mua/bán khi giá vừa phá range Á | Range Á hay là vùng bẫy | Không trade breakout range tích lũy |
| Bỏ qua Daily Open | Không dùng open làm mốc | Mất tham chiếu pha & hướng | Luôn đánh dấu Daily Open |
| Nhầm Judas là distribution | Tưởng move giả là move thật | Vào sai hướng ngay trước đảo chiều | Đối chiếu Daily Bias + chờ reclaim |
| Vào quá muộn (cuối distribution) | Vào khi giá đã chạy về target | Hết dư địa, dễ retrace | Vào early distribution sau sweep |
| Ép AMD vào trend day | Cố tìm Judas khi giá trend thẳng | Cấu trúc không phải AMD | Nhận diện trend day, đổi model |
| Bỏ qua kill zone | Trade phân phối ngoài giờ chính | Thanh khoản kém, dễ nhiễu | Ưu tiên distribution trong kill zone |

---

## 10. Câu hỏi tự kiểm tra

- Mình có giải thích được 3 pha A-M-D trong 30 giây không?
- Daily Open và range tích lũy hôm nay ở đâu?
- Cú phá range vừa rồi là Judas (bẫy) hay distribution (thật)?
- Manipulation đã quét pool liquidity nào?
- Phân phối chạy về pool target nào?
- Mình đang ở pha nào của ngày, và pha đó cho phép trade không?
- Entry có đồng hướng Daily Bias và sau sweep không?
- Nếu không trade, lý do "No Trade" theo pha AMD là gì?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** AMD / Power of 3 gồm những pha nào?
**Đáp:** Accumulation (tích lũy/range) → Manipulation (thao túng/Judas swing quét liquidity sai hướng) → Distribution (phân phối/expansion theo hướng thật).

### Q2
**Hỏi:** Judas swing là gì?
**Đáp:** Là cú đẩy giả trong pha manipulation, đi NGƯỢC hướng thật để quét liquidity và bẫy đám đông vào sai hướng trước khi phân phối.

### Q3
**Hỏi:** Trong một ngày bullish, AMD diễn ra thế nào?
**Đáp:** Tích lũy quanh Daily Open → thao túng XUỐNG (sweep SSL) → phân phối LÊN, đóng cửa gần đỉnh ngày.

### Q4
**Hỏi:** Vì sao không nên trade cú phá range tích lũy đầu tiên?
**Đáp:** Vì cú phá đầu tiên thường là Judas swing (manipulation) — một cái bẫy quét liquidity, không phải move phân phối thật.

### Q5
**Hỏi:** Đặt stop cho entry phân phối (bullish) ở đâu?
**Đáp:** Ngoài cực điểm của Judas swing — dưới đáy của cú thao túng (sweep low).

### Q6
**Hỏi:** AMD ghép với Kill Zones như thế nào?
**Đáp:** Thường Asia = accumulation, London open = manipulation (Judas), London/NY = distribution; mỗi pha gắn với một khung giờ phiên.

### Q7
**Hỏi:** Mốc tham chiếu trung tâm của AMD trong ngày là gì?
**Đáp:** Daily Open — dùng để xác định giá đang ở phía nào và hướng phân phối kỳ vọng.

---

## 12. Lesson Learned

### Bài học chính
- AMD là **khung tổ chức cả ngày**: tích lũy → bẫy → chạy thật.
- Move đầu tiên (manipulation/Judas) thường **sai**; move thật (distribution) đi ngược lại.
- **Đừng trade giai đoạn thao túng**; chờ sweep + reclaim + displacement rồi vào theo phân phối.
- **Daily Open** là mốc tham chiếu trung tâm cho pha và hướng.
- AMD ghép chặt với [[18 - Kill Zones]] và [[20 - Liquidity Sweep]]: đúng giờ, đúng pool, đúng pha.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn xác định Daily Open + range tích lũy trước khi trade.
- [ ] Tôi không đuổi theo cú phá range đầu tiên (giả định là Judas).
- [ ] Tôi chỉ vào trong pha phân phối, sau khi manipulation đã quét liquidity.
- [ ] Tôi đặt stop ngoài cực điểm của Judas swing.
- [ ] Tôi ưu tiên vào early distribution trong kill zone, đồng hướng bias.

### Câu nhắc nhở khi trade
> **"Cú giật đầu tiên là cái bẫy. Tôi chờ Judas quét xong, rồi đi cùng phân phối — không bao giờ ngược lại."**

---

## 13. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có nắm 3 pha + Judas + vai trò Daily Open không? |
| Nhận diện trên chart |  | Có phân biệt manipulation vs distribution theo thời gian thực không? |
| Biết khi nào bỏ qua |  | Có dám bỏ breakout accumulation / không ép AMD vào trend day không? |
| Kết hợp với context HTF |  | AMD có ghép với bias + kill zone + liquidity không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự ở early distribution sau sweep không? |
| Review sau trade |  | Có gắn nhãn pha tại entry và review bằng dữ liệu không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[AMD]]`.
- [ ] Review riêng: entry theo pha (`phase_at_entry`); có Judas rõ vs không.
- [ ] Thống kê win rate, average R theo `phase_at_entry` và `entry_killzone`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.

---

## 14. Best Practices

> [!success] Nguyên tắc vàng
> **"Pha trước, lệnh sau."** Câu hỏi đầu tiên của mỗi phiên không phải "mua hay bán?" mà là "đang ở pha nào của PO3?". Mỗi pha chỉ có một việc đúng: Accumulation = chuẩn bị, Manipulation = quan sát, Distribution = thực thi.

![[AMD-Advanced-Phase-Decision.svg|697]]

1. **Đánh dấu 3 mốc trước khi London mở: Daily Open, Asia High, Asia Low.** Đây là bộ khung tối thiểu của AMD. Không có 3 mốc này trên chart thì mọi nhận định về pha đều là cảm giác. Ghi luôn vào Daily Note để có bằng chứng khi review.

2. **Viết kịch bản Judas HAI CHIỀU từ trước.** "Nếu bias bullish: chờ quét Asia Low/dưới open rồi tìm Long; nếu giá quét Asia High trước thì KHÔNG short đuổi mà chờ xem có phải trend day." Kịch bản viết sẵn giúp không phải "nghĩ" trong lúc giá chạy — lúc dễ bị bẫy nhất.

3. **Coi mọi cú phá range đầu tiên là Judas cho đến khi chứng minh ngược lại.** Gánh nặng chứng minh nằm ở phía breakout: nó phải đóng nến H1 ngoài range và pullback nông không reclaim thì mới được coi là move thật. Mặc định ngược lại sẽ khiến bạn mua đỉnh Judas như đám đông.

4. **Chỉ entry ở EARLY distribution.** Điểm vào hợp lệ là ngay sau reclaim + MSS + FVG đầu tiên của nhịp phân phối. Nếu đã lỡ, để nó đi — vào giữa/cuối distribution là đổi một setup xác suất cao lấy một cú chase R:R xấu. "Lỡ một move" không tốn tiền; chase mới tốn.

5. **Stop luôn nằm ngoài cực điểm Judas, không phải trong range.** Đáy/đỉnh Judas là điểm thị trường đã chứng minh có người mua/bán thật. Stop trong range Á là stop nằm giữa vùng nhiễu — bị quét bởi chính cấu trúc bạn đang trade.

6. **Đối chiếu pha với kill zone và với PO3 tuần.** Judas đúng giờ London/NY open + đồng pha với chiều tuần = setup hạng A. Judas lệch giờ hoặc ngược pha tuần = hạ size hoặc bỏ. Ghi `entry_killzone` và pha tuần vào journal để thống kê.

7. **Ngày không rõ pha = ngày không trade.** Khoảng 2–3 ngày mỗi tuần AMD in rất rõ; những ngày còn lại méo mó. Lợi thế của khung này đến từ việc **chỉ chơi những ngày sách giáo khoa** — đó cũng chính là kỷ luật mà Prop Firm exam đòi hỏi.

---

## Appendix — AMD Quick Reference Card

> [!abstract] Copy vào Daily Note / pre-market
> **Date / Market:**
> **Daily Bias:** Bullish / Bearish / Neutral
> **Daily Open:**
> **Accumulation range (Á):** [low]–[high]
> **Judas direction (manipulation):** Down / Up — sweep pool: SSL / BSL @ ____
> **Reclaim xác nhận?** Yes / No
> **Distribution (displacement + MSS)?** Yes / No — FVG: ____
> **Pha hiện tại:** Accumulation / Manipulation / Distribution-early / Distribution-late
> **Entry plan (theo distribution):**
> **Stop (ngoài cực điểm Judas):**
> **Target (pool HTF):**
> **Kill zone:** Asia / London / NY-AM / NY-PM
> **No-trade condition:**
