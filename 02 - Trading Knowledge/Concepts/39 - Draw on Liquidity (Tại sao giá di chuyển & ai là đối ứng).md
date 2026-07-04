---
type: ict-concept
concept: Draw on Liquidity
aliases:
  - Draw on Liquidity
  - Order Matching
  - Bài toán đối ứng
  - Counterparty Problem
  - Tại sao giá di chuyển
  - Institutional Order Filling
tags:
  - trading/ict/concept
  - trading/study
  - "#draw-on-liquidity"
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
markets:
  - NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 2
last_reviewed: 2026-07-04
created: 2026-07-04
updated: 2026-07-04
related_concepts:
  - "[[19 - Liquidity]]"
  - "[[07 - Buy-side Liquidity]]"
  - "[[30 - Sell-side Liquidity]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[15 - Inducement]]"
  - "[[02 - AMD]]"
  - "[[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]"
  - "[[16 - Internal & External Range Liquidity (IRL & ERL)]]"
prerequisites:
  - "[[19 - Liquidity]]"
  - "[[07 - Buy-side Liquidity]]"
  - "[[30 - Sell-side Liquidity]]"
common_mistakes:
  - "[[Mistake - Enter before liquidity sweep]]"
---

# Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)

> [!summary] Tóm tắt 1 câu
> **Tổ chức lớn KHÔNG thể "đàm phán" để có được khối lượng khổng lồ họ cần — họ buộc phải ĐẨY GIÁ tới nơi tập trung dày đặc lệnh chờ (stop-loss, breakout, lệnh limit tổ chức) để tạo ra đủ đối ứng hấp thụ lệnh của mình; "ai mua giá cao / bán giá thấp" chính là những người bị stop-loss cưỡng bức, breakout đuổi theo, FOMO, và các bên giao dịch vì nghĩa vụ chứ không vì quan điểm giá.**

> [!important] Nguyên tắc cốt lõi
> Vấn đề số một của một lệnh lớn KHÔNG phải là "tìm giá tốt", mà là **"tìm đủ đối ứng (counterparty) để khớp mà không tự đẩy giá chống lại mình"**. Để MUA lớn cần một *biển người BÁN*; để BÁN lớn cần một *biển người MUA*. Giá di chuyển về vùng thanh khoản chính là cơ chế **tạo ra** biển đối ứng đó. Đây là lý do sâu xa của mọi khái niệm "draw on liquidity", "stop hunt", "sweep" trong ICT.

---

## 1. Định nghĩa

**Khái niệm:**
**Draw on Liquidity (DOL)** là vùng thanh khoản mà giá đang **bị hút về** như một "nam châm" — nơi tập trung mật độ lệnh chờ cao nhất. Câu hỏi nền tảng mà note này trả lời là: *tại sao giá lại di chuyển tới các mức cực trị (cao/thấp) thay vì các bên lớn ngồi lại đàm phán một mức giá, và ai là người đứng ở phía đối ứng tại các mức đó?*

**Bài toán gốc — Nghịch lý của lệnh lớn:**
Mỗi lệnh MUA chỉ khớp được khi có một lệnh BÁN đối ứng, và ngược lại. Một tổ chức muốn mua khối lượng khổng lồ (ví dụ tương đương hàng trăm triệu USD trên NDX) không thể quăng toàn bộ lệnh ra thị trường công khai — làm vậy sẽ "ăn" sạch mọi lệnh bán ở từng mức giá và **tự đẩy giá vọt lên chống lại chính mình** (trượt giá / slippage). Giống như cố mua sạch cà chua trong chợ: giá cà chua tăng vọt ngay khi bạn mua, và bạn mua những quả cuối với giá cắt cổ.

**Vì sao KHÔNG chỉ đàm phán trực tiếp (OTC/dark pool/interbank)?**
Các tổ chức *có* đàm phán trực tiếp qua block trade, dark pool, thị trường liên ngân hàng — nhưng điều đó không đủ, vì bốn lý do:
- **Vấn đề đối ứng đối xứng:** hiếm khi có sẵn một bên muốn giao dịch *đúng khối lượng, đúng thời điểm, đúng giá*. Nhu cầu hai bên gần như không bao giờ khớp hoàn hảo.
- **Rò rỉ thông tin (information leakage):** công khai ý định "tôi cần mua lớn" là tự để lộ bài, đối tác sẽ đòi giá bất lợi hơn. Nguyên tắc số một của giao dịch tổ chức là **giấu ý định và quy mô thật**.
- **Tham chiếu giá:** kể cả giao dịch OTC vẫn phải neo vào giá thị trường công khai — không thoát khỏi thị trường công khai được.
- **Đàm phán cho GIÁ tốt nhưng không cho THANH KHOẢN:** giao dịch 1-1 chỉ giải quyết được lệnh nhỏ, lẻ; nó không tạo ra khối lượng đối ứng khổng lồ mà một chương trình thực thi lớn cần.

**Mục đích trong ICT:**
- Giải thích **động cơ thật** đằng sau chuyển động giá: giá đi tìm nơi khớp được lệnh, không đi ngẫu nhiên.
- Xác định **draw on liquidity** — mục tiêu tiếp theo giá bị hút về (buy-side ở trên, sell-side ở dưới).
- Hiểu vì sao [[20 - Liquidity Sweep|sweep]] xảy ra trước khi giá đảo chiều thật: sweep chính là hành động **gom đối ứng**.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đang bị hút về vũng thanh khoản nào (buy-side hay sell-side)?
- Tại vùng cực trị đó, ai sẽ là đối ứng để lệnh tổ chức khớp?
- Cú di chuyển tới đỉnh/đáy là "đi thật" hay chỉ là hành động gom thanh khoản trước khi đảo?

### Draw on Liquidity KHÔNG phải là gì
- Không phải "một ông trùm săn stop-loss của cá nhân tôi" — quá nhỏ để họ quan tâm. Giá bị hút về nơi có **mật độ lệnh** cao nhất, đó là cơ chế cung–cầu của order flow, không phải thuyết âm mưu.
- Không phải "giá luôn quay lại quét mọi đỉnh/đáy" — chỉ những vùng thanh khoản *có ý nghĩa* mới là DOL.
- Không phải một entry model — đây là **narrative/bias** trả lời "giá đang đi đâu và vì sao", không phải "vào lệnh ở đâu".

---

## 2. Bối cảnh sử dụng

### AI đứng ở phía đối ứng? — 4 nhóm cung cấp thanh khoản

> [!info] Trả lời trực tiếp: "ai mua giá cao / bán giá thấp?"
> Những người ở phía bên kia **không tự nguyện chấp nhận giá xấu** — họ bị *cưỡng bức* hoặc bị *đánh lừa* để giao dịch, hoặc giao dịch vì *nghĩa vụ*.

| Nhóm đối ứng | Ở giá THẤP (SM mua) họ làm gì | Ở giá CAO (SM bán) họ làm gì | Vì sao họ ở đó |
|---|---|---|---|
| **Stop-loss nhỏ lẻ** | Stop của lệnh Long bị kích hoạt = lệnh BÁN cưỡng bức | Stop của lệnh Short bị kích hoạt = lệnh MUA cưỡng bức | Đặt stop ngay dưới đáy / trên đỉnh "hiển nhiên" |
| **Breakout traders** | Bán đuổi vì tưởng "phá đáy = trend giảm" | Mua đuổi vì tưởng "phá đỉnh = trend tăng" | Chiến lược đuổi theo momentum |
| **FOMO / tâm lý đám đông** | Bán tháo vì hoảng loạn khi thấy nến đỏ mạnh | Mua đuổi vì sợ bỏ lỡ khi thấy nến xanh mạnh | Cảm xúc, không phải lý trí |
| **Tổ chức có mandate khác** | Index fund/ETF bán khi có dòng rút; hedger đóng vị thế | Index fund mua theo tỷ trọng khi có dòng vào; nhà nhập khẩu mua ngoại tệ | Giao dịch vì **nghĩa vụ**, không vì quan điểm giá |

**Giải thích cặn kẽ nguồn quan trọng nhất — stop-loss:**
Một stop-loss của vị thế MUA, về bản chất kỹ thuật, **chính là một lệnh BÁN** (sell stop). Dưới một đáy cũ tập trung hàng nghìn stop như vậy, cộng thêm lệnh breakout bán mới. Khi SM đẩy giá xuống *dưới* đáy đó ([[30 - Sell-side Liquidity|sell-side raid]]), toàn bộ số lệnh này kích hoạt cùng lúc → tạo ra một **thác lệnh BÁN**. Đó chính là biển đối ứng để SM âm thầm MUA vào ở giá thấp mà không làm giá bật lên ngay. Ở đỉnh thì đối xứng hoàn toàn với [[07 - Buy-side Liquidity|buy-side liquidity]].

**Nhóm "mandate khác" — điểm tinh tế ít người nhắc:**
Không phải mọi tổ chức lớn giao dịch để kiếm lời từ hướng giá. Index fund **bắt buộc** mua theo tỷ trọng khi có dòng tiền mới, bất kể giá cao. Nhà nhập khẩu mua ngoại tệ dù tỷ giá bất lợi vì cần vận hành kinh doanh. Hãng hàng không mua hợp đồng dầu để *bảo hiểm* giá xăng, không phải đầu cơ. Đây là các **"natural counterparty"** — sẵn lòng đứng phía đối ứng ở mức giá mà nhà đầu cơ coi là "xấu".

### Khi nào khái niệm này có giá trị cao?
- [ ] Cần xác định mục tiêu tiếp theo của giá (DOL) để đặt target/bias.
- [ ] Giá đang tiến về một vùng equal highs/lows, đỉnh/đáy cũ rõ ràng.
- [ ] Đang phân vân một cú phá đỉnh/đáy là thật hay là sweep gom thanh khoản.
- [ ] Trước tin/mở phiên — thời điểm SM cần thanh khoản để thực thi lệnh lớn.

### Khi nào nên thận trọng?
- [ ] Dùng khái niệm này để "đoán" mọi đỉnh/đáy đều sẽ bị quét → dễ overtrade.
- [ ] Giữa range, không có vũng thanh khoản rõ ràng → DOL không xác định được.
- [ ] Biến nó thành lý do chống lại mọi breakout mà không có bằng chứng.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Vùng thanh khoản rõ ràng làm "nam châm":** equal highs/lows, đỉnh/đáy phiên trước (PDH/PDL), đỉnh/đáy tuần, old high/low. Đây là nơi cụm stop dày đặc → ứng viên DOL.
2. **Giá tiến có chủ đích về vùng đó** thay vì đi ngẫu nhiên — thường kèm nhịp inducement dụ lệnh trước.
3. **Sweep + phản ứng:** giá quét qua vùng thanh khoản rồi **đóng nến quay lại** (rejection) — dấu hiệu SM đã gom xong đối ứng và bắt đầu đi hướng thật.

### Điều kiện bắt buộc để coi là DOL hợp lệ
- [ ] Có mật độ lệnh chờ thực sự (đỉnh/đáy có ý nghĩa, không phải noise).
- [ ] Nằm đúng logic bias HTF (giá bị hút về đâu trong dealing range).
- [ ] Có [[16 - Internal & External Range Liquidity (IRL & ERL)|ERL/IRL]] rõ ràng để định vị.

### Điều kiện tăng xác suất
- [ ] Có [[15 - Inducement]] phía trước DOL (mồi để gom lệnh).
- [ ] Sweep đi kèm [[13 - FVG  - Fair Value Gap|FVG]]/displacement sau khi quét.
- [ ] DOL trùng một POI HTF (order block / FVG khung lớn).
- [ ] Xảy ra trong [[18 - Kill Zones|killzone]] chính.

### Điều kiện làm tín hiệu yếu đi
- Vùng thanh khoản quá nhỏ / không ai đặt lệnh ở đó.
- Đã bị quét nhiều lần trước đó (thanh khoản đã cạn).
- Giá phá thẳng qua mà không phản ứng → có thể là displacement thật, không phải sweep.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Câu hỏi "đối ứng" bắt buộc trước khi xác định DOL
> 1. **Nếu tôi là SM cần khớp một lệnh lớn, tôi cần MUA hay BÁN, và tôi cần biển đối ứng nào?**
> 2. **Cụm lệnh chờ dày nhất (stop + breakout) đang nằm ở đâu — trên hay dưới giá hiện tại?**
> 3. **Giá đang bị hút về buy-side (trên) hay sell-side (dưới)?**

### D1 / H4 — Bias & Narrative
- Bias hiện tại: Bullish / Bearish / Neutral ([[12 - Daily Bias]]).
- Dealing range hiện tại và vị trí giá (premium/discount — [[27 - Premium Discount]]).
- **DOL chính:** vũng thanh khoản HTF (ERL) mà giá đang bị hút về.

### H1 / M15 — POI & Context
- POI HTF nằm ở đâu so với DOL?
- Có inducement (thanh khoản nội vi) trước POI/DOL không?
- Giá đã sweep vùng thanh khoản có ý nghĩa chưa?

### M5 / M1 — Confirmation & Entry
- Sau khi giá chạm DOL và sweep → có phản ứng (rejection/[[21 - Market Structure Shift|MSS]]) không?
- MSS có nằm trong POI không, hay chỉ giữa range?
- Chờ xác nhận SM đã gom đối ứng xong (sweep + displacement) rồi mới tính entry.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Coi là DOL đã "hoàn thành nhiệm vụ" (giá sắp đi hướng thật) khi
- [ ] Giá đã quét vùng thanh khoản mục tiêu (lấy stop/đối ứng).
- [ ] Đóng nến từ chối rõ ràng (rejection) khỏi vùng đó.
- [ ] Có MSS + displacement đồng hướng bias HTF sau sweep.
- [ ] Còn một DOL đối diện phía trước làm target.

### Tín hiệu bị vô hiệu / cần xét lại khi
- [ ] Giá phá thẳng DOL, đóng nến vượt qua, không phản ứng → đó là displacement thật, đổi narrative.
- [ ] Không có cụm lệnh thực sự ở vùng ta tưởng là DOL.
- [ ] Vào lệnh *trước* khi sweep xảy ra ([[Mistake - Enter before liquidity sweep]]).

---

## 6. Ví dụ chart

### Ví dụ đúng
![[paste-image-here.png]]

**Mô tả:**
_(Dán screenshot: giá tiến về sell-side liquidity dưới một đáy cũ → quét stop → đóng nến quay lại range → displacement lên. SM đã dùng vùng đáy đó làm biển đối ứng để mua vào.)_

**Vì sao đây là ví dụ tốt:**
-
-
-

### Ví dụ sai / dễ nhầm
![[paste-image-here.png]]

**Mô tả lỗi:**
_(Dán screenshot: tưởng phá đáy là "trend giảm" nên bán đuổi — chính là đang cung cấp đối ứng cho SM mua; ngay sau đó giá đảo chiều lên.)_

**Bài học:**
-
-
-

---

## 7. Entry model liên quan

Khái niệm này là nền tảng **narrative/bias**, thường kết hợp với:
- [[19 - Liquidity]]
- [[07 - Buy-side Liquidity]]
- [[30 - Sell-side Liquidity]]
- [[20 - Liquidity Sweep]]
- [[15 - Inducement]]
- [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[02 - AMD]]
- [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]
- [[01 - ICT 2022 Model|ICT 2022 Model]]

### Sequence mẫu
```text
HTF Bias → Xác định DOL (buy-side / sell-side là target)
→ Giá tiến về DOL (thường qua Inducement)
→ Sweep DOL = SM gom đối ứng (stop + breakout + FOMO khớp lệnh)
→ Rejection + MSS + Displacement (đối ứng đã đủ)
→ Entry tại POI/FVG → Target: DOL đối diện
```

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Đừng nhầm "gom thanh khoản" với "đi hướng thật"
> Một cú phá đỉnh/đáy có thể chỉ là hành động gom đối ứng trước khi đảo. Luôn chờ xác nhận sweep + rejection trước khi kết luận hướng.

- [ ] Xác định rõ DOL chính (buy-side / sell-side) theo bias HTF.
- [ ] Trả lời được: nếu là SM, tôi cần biển đối ứng nào và nó ở đâu.
- [ ] Vùng DOL có mật độ lệnh thực sự (đỉnh/đáy có ý nghĩa).
- [ ] Đã có sweep + phản ứng trước khi vào (không vào trước sweep).
- [ ] Có DOL đối diện làm target, RR ≥ kế hoạch.
- [ ] Không đặt stop tại swing hiển nhiên nhất (nơi cụm stop bị nhắm).
- [ ] Không giao dịch chỉ vì "thấy phá đỉnh/đáy" mà không có narrative.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Bán đuổi khi phá đáy / mua đuổi khi phá đỉnh | Vào theo breakout tại DOL | Nhận ra đó có thể là điểm SM gom đối ứng; chờ rejection |
| Tưởng SM "đàm phán để có giá tốt" | Kỳ vọng giá đứng yên, không hiểu vì sao giá quét | Hiểu SM cần THANH KHOẢN, không chỉ GIÁ → phải đẩy giá tới DOL |
| Đặt stop ngay dưới đáy / trên đỉnh | SL tại nơi cụm stop dày | Lùi stop ra ngoài vùng thanh khoản logic |
| Vào lệnh trước sweep | Giá chưa lấy DOL đã vào | Chờ sweep + đóng nến quay lại |
| Coi mọi đỉnh/đáy đều là DOL | Overtrade, đoán bừa | Chỉ xét vùng thanh khoản có ý nghĩa + đúng bias HTF |

---

## 10. Câu hỏi tự kiểm tra

- Tôi giải thích được trong 30 giây "vì sao SM phải đẩy giá thay vì đàm phán" không?
- Ai là đối ứng ở giá cao? Ở giá thấp? (kể ít nhất 3 nhóm)
- DOL tiếp theo mà giá bị hút về đang ở đâu, và vì sao?
- Cú phá đỉnh/đáy trước mặt là sweep (gom đối ứng) hay displacement thật?
- Setup nào trong journal tôi đã bán/mua đuổi và trở thành đối ứng cho SM?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Vấn đề số một của một lệnh tổ chức lớn là gì?
**Đáp:** Không phải tìm giá tốt, mà tìm đủ **đối ứng (counterparty)** để khớp mà không tự đẩy giá chống lại mình.

### Q2
**Hỏi:** Vì sao đàm phán trực tiếp (OTC/dark pool) không giải quyết được?
**Đáp:** Hiếm có đối ứng đối xứng đúng khối lượng/thời điểm; công khai ý định gây rò rỉ thông tin; vẫn phải tham chiếu giá công khai; đàm phán cho GIÁ tốt nhưng không tạo ra THANH KHOẢN lớn.

### Q3
**Hỏi:** Để MUA một khối lượng khổng lồ, SM cần điều kiện gì và họ tạo ra nó thế nào?
**Đáp:** Cần một *biển người BÁN*; họ đẩy giá xuống dưới đáy cũ (sell-side raid) để kích hoạt stop-loss của phe Long (= lệnh bán) và breakout bán, tạo biển đối ứng để mua vào.

### Q4
**Hỏi:** "Ai mua ở giá cao?" — kể 3 nhóm.
**Đáp:** Stop-loss của phe Short bị kích hoạt (lệnh mua cưỡng bức), breakout mua đuổi, FOMO buyers, và index fund/hedger mua vì mandate.

### Q5
**Hỏi:** Vì sao "một ông trùm săn stop của cá nhân tôi" là cách hiểu sai?
**Đáp:** Cá nhân quá nhỏ; giá bị hút về nơi có **mật độ lệnh** cao nhất theo cơ chế order flow — nơi có nhiều lệnh nhất để khớp, không phải âm mưu nhắm vào một người.

---

## 12. Nền tảng lý thuyết

> [!note] Auction Theory & Market Microstructure
> Thị trường là một **cuộc đấu giá hai chiều liên tục (double auction)**. Để khớp một lệnh lớn, giá buộc phải di chuyển đến nơi có **mật độ lệnh chờ cao nhất** — nơi đủ đối ứng hấp thụ khối lượng. ICT gọi nơi đó là "liquidity"; bản chất vi mô là **mật độ lệnh chờ** (resting orders), gồm cụm stop retail, lệnh limit tổ chức, vùng quanh strike quyền chọn lớn, và vùng VWAP nơi thuật toán thực thi đang làm việc.

> [!note] Vai trò retail bị phóng đại — đọc kèm [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]
> Với NQ/NDX, phần lớn khối lượng đến từ tổ chức, options dealer hedging, arbitrageur, HFT — retail chiếm tỷ trọng nhỏ. "Săn stop retail" là **mô hình sư phạm** hữu ích để đọc chart, nhưng đừng hiểu theo nghĩa đen rằng thị trường tồn tại để lấy tiền cá nhân bạn. Cả hai cách diễn giải (ICT "stop hunt" và microstructure "mật độ lệnh") dẫn tới cùng một hành động giao dịch, nhưng hiểu cơ chế thật giúp bạn không giao dịch mê tín.

> [!tip] Bài học thực chiến cho Prop Firm (risk ≤ 0.5%/lệnh)
> Vì cụm stop tập trung ở nơi *hiển nhiên* (ngay dưới đáy gần nhất, ngay trên đỉnh gần nhất) và đó chính là DOL, **đừng đặt stop ở những nơi hiển nhiên đó**. Lùi stop ra ngoài vùng thanh khoản logic để tránh bị quét trước khi giá đi đúng hướng.

---

## 13. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault có folder riêng cho trades, thay `FROM ""` bằng path tương ứng, ví dụ `FROM "05 - Live Trading Journal/Trades"`.

---

## 14. Lesson Learned

### Bài học chính
- Lệnh lớn cần **đối ứng**, không chỉ cần giá tốt → giá phải đi tìm thanh khoản.
- "Ai mua cao / bán thấp": stop-loss cưỡng bức, breakout đuổi, FOMO, và tổ chức giao dịch vì mandate.
- Giá bị hút về nơi **mật độ lệnh** cao nhất (DOL) — cơ chế, không phải âm mưu.
- Phá đỉnh/đáy thường là **gom đối ứng** trước khi đảo, không phải tín hiệu đi thẳng.

### Quy tắc cá nhân rút ra
- [ ] Trước mỗi trade, tôi xác định DOL và tự hỏi "nếu là SM, tôi cần đối ứng ở đâu".
- [ ] Tôi không bán đuổi khi phá đáy / mua đuổi khi phá đỉnh mà chưa có rejection.
- [ ] Tôi không đặt stop tại swing hiển nhiên nhất.

### Câu nhắc nhở khi trade
> **"Giá không đi tìm giá tốt cho Smart Money — nó đi tìm ĐỐI ỨNG. Nơi có nhiều stop nhất là nơi giá muốn tới. Đừng đứng cùng phía với đám đông tại đỉnh/đáy hiển nhiên."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa | | Giải thích được bài toán đối ứng & vì sao không chỉ đàm phán? |
| Nhận diện trên chart | | Xác định đúng DOL (buy-side/sell-side) & sweep? |
| Biết khi nào bỏ qua | | Không coi mọi đỉnh/đáy đều là DOL? |
| Kết hợp với context HTF | | Dùng DOL để định bias/target chồng lên ICT 2022? |
| Áp dụng vào trade thực tế | | Có chờ sweep + rejection trước khi vào? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 ví dụ giá phản ứng tại DOL (buy-side & sell-side).
- [ ] Đối chiếu với [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] và [[02 - AMD]].
