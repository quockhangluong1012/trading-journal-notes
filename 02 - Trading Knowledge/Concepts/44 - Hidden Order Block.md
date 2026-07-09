---
type: ict-concept
concept: Hidden Order Block
aliases:
  - Hidden Order Block
  - Hidden OB
  - Secret PD Array
tags:
  - trading/ict/concept
  - trading/study
  - "#pd-array"
  - "#entry-model"
status: seed
category: PD Array
last_reviewed: 2026-07-09
created: 2026-07-09
updated: 2026-07-09
---

# Hidden Order Block

> [!summary] Tóm tắt 1 câu
> **Hidden Order Block là một Order Block KHÔNG hiện trên HTF vì nó bị chôn bên trong vùng WICK CHỒNG nhau của hai nến cùng màu liên tiếp — zoom xuống LTF vào vùng overlap đó là một OB sạch đang chờ, "hidden in plain sight".**

> [!important] Nguyên tắc cốt lõi
> Trên HTF, một cụm lệnh tổ chức (institutional order) có thể được giao (deliver) ngay bên trong khoảng wick chồng của hai nến cùng màu, nhưng **thân nến HTF che mất** vùng đó nên đa số retail không nhìn thấy Order Block. Khi zoom xuống LTF (M5/M15) bên trong khoảng overlap, cấu trúc OB cổ điển (nến ngược hướng cuối cùng trước displacement) lộ ra rõ ràng. Hidden OB vì thế là một **PD array "bí mật"**: cùng bản chất order flow với OB thường, chỉ khác cách nó ẩn mình trên khung lớn. **Bản thân Hidden OB là vùng chờ, không phải trigger** — entry vẫn cần retrace về vùng + CISD/MSS trên LTF + đúng bias/PD.

---

## 1. Định nghĩa

**Khái niệm:**
**Hidden Order Block** là Order Block sinh ra trong **vùng chồng lấn (overlap) của wick** giữa **hai nến CÙNG MÀU liên tiếp** trên HTF. Vì hai nến cùng màu, mắt thường chỉ thấy "hai nến đi cùng hướng" chứ không thấy có OB nào; nhưng dòng lệnh thật đã để lại một Order Block bên trong khoảng wick chồng đó. **Range của Hidden OB** trải từ **cực trị wick này sang cực trị wick kia**: với bullish, từ **low wick của nến thứ 2** lên **high wick của nến thứ 1**; với bearish thì ngược lại (high wick nến 2 → low wick nến 1).

![[HiddenOB-Advanced-Anatomy.svg|697]]

*Trên HTF chỉ thấy 2 nến xanh với wick chồng nhau — không thấy OB. Zoom LTF vào đúng vùng overlap, một Order Block sạch (nến giảm cuối trước displacement tăng) hiện ra. Proximal = mép gần giá (điểm vào), distal = mép xa (stop).*

**Nó giúp trả lời câu hỏi nào trên chart?**
- Vùng "trống" mà giá vừa rời đi nhưng **không để lại OB rõ trên HTF** — liệu có POI ẩn nào ở đó không?
- Vì sao giá cứ **phản ứng mạnh** tại một khoảng mà HTF nhìn như không có gì đặc biệt?
- Tôi có thể tìm một **entry chính xác, stop nhỏ** ngay bên trong một vùng mà đám đông HTF bỏ qua không?

### Hidden OB KHÔNG phải là gì
- **Không phải** Order Block thường ([[25 - OB - Order Block]]): OB thường là **một nến ngược hướng đơn lẻ nhìn thấy được** trên chart; Hidden OB là **hai nến cùng màu** với OB thật giấu trong vùng wick chồng, chỉ hiện trên LTF.
- **Không phải** [[22 - Mitigation Block]]: Mitigation Block là OB được giá quay lại "giảm nhẹ" (mitigate) phần lệnh chưa lấp — khác về vòng đời và vai trò, không phải về cách ẩn trong wick.
- **Không phải** [[04 - Breaker Block]]: Breaker là OB **thất bại rồi đảo cực** sau sweep + MSS; Hidden OB không cần fail/flip, nó chỉ là OB bị che.
- **Không phải** Suspension Block: đó là một PD array riêng biệt; đừng gộp chung.
- **Không phải** trigger vào lệnh: nó là **vùng POI** để chờ giá về, sau đó mới tìm CISD/MSS trên LTF.

---

## 2. Cơ chế sâu — vì sao Hidden OB hoạt động

Đây là phần "why" mà đa số bỏ qua khi chỉ học "vẽ box giữa hai wick". Hiểu cơ chế mới phân biệt được Hidden OB thật với hai nến cùng màu ngẫu nhiên.

**(a) Lệnh tổ chức nằm trong overlap mà thân nến HTF che đi.** Theo mô hình ICT, giá được market maker giao quanh các vùng có lệnh chưa được lấp. Khi engine gom/đẩy hàng trong một cụm giá hẹp rồi tiếp tục đi, trên HTF nó chỉ in ra **hai nến cùng màu** — thân nến lớn nuốt trọn cấu trúc bên trong. Nhưng ở tầng LTF, đúng khoảng wick chồng đó chứa một **nến ngược hướng cuối cùng trước displacement** (định nghĩa kinh điển của OB). Cụm lệnh institutional được đặt ngay tại đó; giá quay lại để **lấp phần lệnh còn dư** rồi đi tiếp.

**(b) Vì sao retail miss.** Retail nhìn HTF thấy "hai nến xanh đi lên" → kết luận vùng đó không có gì để giao dịch, hoặc chỉ vẽ OB tại nến giảm rõ ràng gần nhất (thường xa hơn, tệ hơn về R). Họ **không zoom vào wick chồng**. Chính vì đám đông bỏ qua, vùng này còn **nguyên lệnh chưa lấp** → phản ứng sạch khi giá về, ít bị "nhiễu" bởi stop cluster của retail.

**(c) Vì sao nó cho entry đẹp hơn.** Vì OB thật nằm sâu trong overlap, **proximal của Hidden OB thường gần hơn** so với OB HTF "hiển nhiên", cho phép stop nhỏ (đặt sau distal/wick) và R:R lớn hơn với cùng một target. Đây là edge về giá vào, không chỉ về hướng.

> [!info] Hidden OB so với OB thường — cùng gốc, khác độ "ẩn"
> Cả hai đều là Order Block (nến/cụm ngược hướng cuối trước displacement). Khác biệt **duy nhất về bản chất** là: OB thường hiện thành một nến nhìn thấy trên khung bạn đang xem; Hidden OB bị **hai nến cùng màu che** nên chỉ hiện khi bạn hạ khung. Nói cách khác, Hidden OB **luôn là chuyện đa khung**: nó "ẩn" trên khung này và "hiện" trên khung dưới. Nếu bạn hạ khung mà không thấy OB sạch trong vùng overlap → không phải Hidden OB, chỉ là hai nến trùng màu.

---

## 3. Bối cảnh sử dụng

### Khi nào có giá trị cao?
- [ ] Xuất hiện trên **HTF bias rõ** (D1/H4 swing, hoặc H1 intraday) và **thuận [[12 - Daily Bias]]**
- [ ] Nằm đúng **vùng Premium/Discount** ([[27 - Premium Discount]]): bullish ở discount, bearish ở premium
- [ ] Zoom LTF vào overlap **thật sự thấy một OB sạch** (có nến ngược hướng + displacement rời đi)
- [ ] Đi kèm **liquidity sweep** ngay trước đó ([[20 - Liquidity Sweep]]) — sweep dọn entry sớm, Hidden OB giao fill
- [ ] Có **FVG / breaker / liquidity void** ([[13 - FVG  - Fair Value Gap]], [[21 - Liquidity Void]]) xếp chồng trong cùng vùng
- [ ] Giá **quay lại tap vùng** rồi cho **CISD/MSS** trên LTF ([[41 - Change in State of Delivery]], [[21 - Market Structure Shift]])

### Khi nào nên bỏ qua?
- [ ] Hai nến **khác màu**, hoặc wick **không thật sự chồng** (có khoảng hở)
- [ ] Vùng nằm **giữa range**, không gắn với pool thanh khoản nào
- [ ] **Ngược HTF bias** hoặc sai vùng PD (bullish Hidden OB ở premium)
- [ ] Zoom LTF **không thấy OB sạch** — chỉ là hai nến trùng màu ngẫu nhiên
- [ ] Phiên **thanh khoản mỏng** (giờ nghỉ trưa Asia) — dễ tạo cấu trúc giả
- [ ] Chưa có **trigger** (CISD/MSS) mà đã muốn vào "đón đầu"

---

## 4. Bullish vs Bearish Hidden OB

![[HiddenOB-Advanced-BullBear.svg|697]]

**Bullish Hidden OB (2 nến XANH):** nến 1 có **upper wick** đáng kể, nến 2 có **lower wick chồng xuống** phủ lên thân/wick nến 1. Range box = **low wick nến 2 → high wick nến 1**. Đặt trong **discount** → tín hiệu **long** mạnh. Zoom LTF vào overlap sẽ thấy OB tăng (nến giảm cuối trước displacement lên).

**Bearish Hidden OB (2 nến ĐỎ):** gương phản chiếu — nến 1 có **lower wick** dài, nến 2 có **upper wick chồng lên**. Range box = **high wick nến 2 → low wick nến 1**. Đặt trong **premium** → tín hiệu **short** mạnh.

> [!tip] Mẹo đọc nhanh
> Đừng học thuộc "nến nào wick nào" một cách máy móc. Nhớ nguyên tắc gốc: **box của Hidden OB luôn ôm trọn khoảng WICK CHỒNG** — tức từ cực trị wick xa nhất phía trên đến cực trị wick xa nhất phía dưới của hai nến. Chiều (long/short) do **bias + vị trí PD** quyết định, không do màu nến quyết định một mình.

---

## 5. Cách nhận diện (3 bước)

![[HiddenOB-Advanced-Identification.svg|697]]

1. **Tìm hai nến CÙNG MÀU liên tiếp** trên khung bias. Hai nến xanh (cho bullish) hoặc hai nến đỏ (cho bearish) đứng cạnh nhau. Khác màu → dừng lại, không phải Hidden OB.
2. **Xác nhận WICK CHỒNG nhau.** Lower wick của nến 2 phải phủ lên thân/wick của nến 1 (bullish); nếu có khoảng hở giữa hai wick thì **loại**. Vùng chồng chính là "hộp chứa" OB ẩn.
3. **Vẽ BOX từ wick extreme này sang wick extreme kia.** Bullish: low wick nến 2 → high wick nến 1. Đây là vùng Hidden OB. Sau đó **zoom LTF** vào box để xác nhận có OB sạch, và chờ giá retrace về.

> [!info] Bước ẩn thứ 4 — luôn kiểm chứng trên LTF
> Ba bước trên chỉ **khoanh vùng nghi ngờ** trên HTF. Bước quyết định là hạ khung: nếu trong box thật sự có một OB (nến ngược hướng cuối + displacement rời đi để lại FVG), Hidden OB được xác nhận. Nếu không → bỏ. Đây là điểm khác biệt lớn nhất với việc "vẽ box đại giữa hai nến".

---

## 6. Proximal / Distal & Premium–Discount

![[HiddenOB-Advanced-ProximalDistal.svg|697]]

Coi Hidden OB như một **PD array** với hai biên:

- **Proximal line** = mép **gần giá hiện tại** → đây là nơi **canh vào lệnh** (entry). Với bullish Hidden OB (giá đến từ trên xuống), proximal là mép **trên** của box.
- **Distal line** = mép **xa giá** → đây là nơi đặt **stop** (ra ngoài distal). Với bullish, distal là mép **dưới** (low wick nến 2).

Lọc theo vùng **Premium/Discount** của dealing range ([[27 - Premium Discount]]):
- **Bullish Hidden OB ở DISCOUNT** (dưới equilibrium) = long xác suất cao, target về **ERL high**.
- **Bearish Hidden OB ở PREMIUM** (trên equilibrium) = short xác suất cao, target về **ERL low**.
- Hidden OB **ngược vùng PD** (bullish ở premium) là **cờ đỏ** — bỏ hoặc hạ hạng.

> [!tip] Vào tại proximal, không đợi distal
> Nhiều trader tham lam chờ giá chạm distal để "vào giá đẹp hơn" rồi bị bỏ lại khi giá bật từ proximal. Kỷ luật: **vào quanh proximal (hoặc Mean Threshold/50% của box)** khi có trigger LTF, stop ngoài distal. Giá thường không cần chạm hết box mới đi.

---

## 7. Hidden OB đa khung (MTF)

![[HiddenOB-Advanced-MTF.svg|697]]

Hidden OB về bản chất là câu chuyện **top-down** ([[32 - Top-down Analysis (Multiple Timeframes)]]):

1. **HTF (H4/H1) — chọn bias & mark vùng.** Xác định [[12 - Daily Bias]], tìm Hidden OB trên khung bias, vẽ box. Hidden OB càng lớn (khung càng cao) → **move mục tiêu càng lớn**.
2. **Chờ retrace — không đuổi.** Để giá chạy khỏi vùng rồi quay lại **tap** box. Đây là kỷ luật quan trọng nhất: Hidden OB là vùng chờ, không phải tín hiệu vào tức thì.
3. **LTF (M5/M15) — timing entry.** Khi giá vào box, hạ khung tìm **CISD hoặc MSS** cùng hướng bias. Vào tại **close của nến CISD/MSS** hoặc retest sạch của nó (thường có FVG đi kèm).

Nguyên tắc "khung trên quyết định vùng & hướng, khung dưới quyết định giờ vào" — đừng để một cấu trúc LTF kéo bạn vào lệnh khi giá còn chưa tap Hidden OB HTF.

---

## 8. Confluence với Liquidity Sweep

![[HiddenOB-Advanced-SweepConfluence.svg|697]]

Đây là **setup xác suất cao nhất** của Hidden OB: ghép với một **liquidity sweep** ngay trước điểm vào.

- **① Sweep** SSL dưới một swing low (bullish) → dọn sạch stop của long non và kích hoạt lệnh sell breakout. Đây là **lý do** đảo chiều.
- **② Hidden OB** nằm ngay trên vùng bị sweep = **vùng fill**: nơi giá quay lại để lấp lệnh institutional.
- **③ LTF CISD/MSS** bên trong Hidden OB = **trigger** cấu trúc.
- **④ Long entry**, stop dưới wick sweep (distal), target **BSL / opposing PD array**.

Chuỗi này mạnh vì nó gộp ba tầng độc lập: sweep (thanh khoản), Hidden OB (POI), CISD (cấu trúc). Càng nhiều confluence xếp trong cùng vùng — FVG, breaker, liquidity void — xác suất càng tăng.

> [!info] Vì sao "sweep rồi Hidden OB" ăn tiền
> Sweep lấy đi thanh khoản làm "nhiên liệu" cho chân ngược lại và **loại bớt trader vào sớm** (họ bị stop). Ngay sau đó Hidden OB giao phần fill mà đám đông không thấy, còn CISD cho bạn thời điểm vào có xác nhận. Bạn vào **sau** khi bẫy đã sập, không phải trước.

---

## 9. Quy trình vào lệnh

**Bước 1 — Xác định HTF bias & vùng PD.** Chốt [[12 - Daily Bias]] trên D1/H4 (hoặc H1 intraday). Xác định dealing range và equilibrium để biết premium/discount ([[27 - Premium Discount]]).

**Bước 2 — Quét tìm Hidden OB trên khung bias.** Áp 3 bước nhận diện (mục 5): hai nến cùng màu → wick chồng → vẽ box. Ưu tiên vùng gắn với một **pool thanh khoản** hoặc ngay sau một **sweep**.

**Bước 3 — Xác nhận trên LTF.** Zoom vào box; chỉ giữ lại nếu thấy **OB sạch** (nến ngược hướng cuối + displacement để lại FVG). Không thấy → loại.

**Bước 4 — Chờ giá retrace về vùng (KHÔNG đuổi).** Đánh dấu proximal/distal. Kiên nhẫn đợi giá tap box; nếu giá bỏ đi luôn thì không có lệnh — chấp nhận.

**Bước 5 — Trigger + Entry.** Khi giá vào box, tìm **CISD hoặc MSS** cùng hướng trên M5/M15. Vào tại **close của nến CISD/MSS** hoặc **retest sạch** (thường tại FVG / proximal / Mean Threshold của box).

**Bước 6 — Stop & Target.** Stop **dưới swing low của CISD/MSS** (longs) / **trên swing high** (shorts), hoặc rộng hơn **ra ngoài distal** nếu cần thở. Target: **opposing PD array** kế tiếp / **liquidity pool** / bám thang [[16 - Internal & External Range Liquidity (IRL & ERL)]] (T1 = IRL, T2 = ERL / draw on liquidity), nhắm tối thiểu **~1:3**.

---

## 10. Ví dụ chart

### Ví dụ đúng

![[HiddenOB-Example-Correct.svg|697]]

*Trong discount, giá quét SSL rồi reject (①). Bên trong Hidden OB (2 nến xanh, wick chồng) xuất hiện LTF CISD (②). Long entry tại proximal (③), stop dưới wick sweep, target ERL/BSL ~1:3.*

**Vì sao đây là ví dụ tốt:**
- Hidden OB nằm ở **discount**, thuận **HTF bias long**.
- Có **liquidity sweep** ngay trước → dọn entry sớm, tạo lý do đảo chiều.
- Có đủ chuỗi: **sweep (lý do) + Hidden OB (POI) + CISD (trigger) + FVG (entry)**.
- Vào tại **proximal**, stop rõ ràng sau wick sweep/distal → R:R lành mạnh (T1 = IRL, T2 = ERL).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp chart của bạn: đánh dấu (1) hai nến cùng màu có wick chồng trên HTF, (2) box Hidden OB (wick→wick), (3) OB sạch khi zoom LTF, (4) sweep + CISD/MSS, (5) entry/stop/target và vùng PD. Thay `paste-image-here.png` bằng tên file theo quy ước SYMBOL-YYYYMMDD-TF-N.png.*

### Ví dụ sai / dễ nhầm

![[HiddenOB-Example-Wrong.svg|697]]

*Ba lỗi kinh điển: (trái) hai nến xanh nhưng wick KHÔNG chồng — có khoảng hở → không đủ điều kiện; (giữa) bullish Hidden OB nhưng nằm ở PREMIUM và ngược bias giảm → long ngược dòng; (phải) Hidden OB treo giữa range, không gắn pool thanh khoản nào → thiếu lý do.*

**Bài học:**
- **Wick phải thật sự chồng** — không có overlap thì không có Hidden OB, chỉ là hai nến trùng màu.
- Hidden OB phải **thuận bias và đúng vùng PD**; ngược dòng thì bỏ hoặc hạ hạng nặng.
- Vùng phải **gắn với thanh khoản** (tốt nhất là sau sweep); giữa range không có draw thì không giao dịch.
- Luôn **kiểm chứng LTF**: không thấy OB sạch trong box → không phải Hidden OB.

---

## 11. Thực hành tốt nhất (Best Practices)

> [!tip] 7 quy tắc Hidden OB
> 1. **Hai nến cùng màu + wick CHỒNG** — thiếu overlap là loại ngay.
> 2. **Luôn kiểm chứng LTF** — box HTF chỉ hợp lệ khi zoom vào thấy OB sạch.
> 3. **Thuận bias & đúng PD** — bullish ở discount, bearish ở premium; ngược thì bỏ.
> 4. **Chờ retrace, không đuổi** — Hidden OB là vùng chờ, không phải trigger tức thì.
> 5. **Cần trigger cấu trúc** — vào bằng CISD/MSS trên LTF, không "đón đầu".
> 6. **Ưu tiên confluence** — sweep, FVG, breaker, liquidity void xếp trong cùng vùng.
> 7. **Bỏ phiên thanh khoản mỏng** — tránh giờ nghỉ trưa Asia, cấu trúc dễ giả.

- Vào quanh **proximal / Mean Threshold** của box, đừng tham chờ distal.
- Stop sau **swing của CISD/MSS** hoặc ngoài **distal**; target bám thang [[16 - Internal & External Range Liquidity (IRL & ERL)]] (T1 = IRL, T2 = ERL), nhắm ~1:3.
- HTF Hidden OB **càng lớn → move càng lớn**: dùng khung bias để chọn vùng "đáng đi".
- Ghi nhật ký có kỷ luật: gắn nhãn mỗi lệnh **có/không Hidden OB xác nhận** và **có/không sweep đi kèm** để đo edge tách nhóm.

> [!warning] Bối cảnh prop-firm (FTMO & The5ers)
> Hai bộ luật KHÁC NHAU, đừng bao giờ trộn lẫn. **FTMO 10K** đo daily loss theo **balance khởi đầu CỐ ĐỊNH** (mốc reset mỗi ngày theo balance đầu ngày/đầu challenge tuỳ biến thể) và yêu cầu **số ngày giao dịch tối thiểu** — bạn phải giữ mức thua trong ngày dưới ngưỡng tính trên con số cố định đó. **The5ers 10K** tham chiếu **equity ĐÓNG CỬA của ngày HÔM TRƯỚC** cho ngưỡng rủi ro và đòi hỏi **một số ngày có lãi tối thiểu** (mỗi ngày lãi ~0.5%+ mới được tính). Hidden OB không thay đổi các luật này — nó chỉ **nâng xác suất mỗi lệnh và cho stop nhỏ hơn**, giúp bạn ít vi phạm daily loss hơn. Nhấn mạnh **process > outcome**, rủi ro **≤0.5%/lệnh**. Khang đang ở **giai đoạn foundation/backtesting (chưa live)** — hãy **backtest win-rate của riêng Hidden OB** (và tách nhóm "có sweep A+") cho đến khi expectancy ổn định TRƯỚC khi tin dùng nó vào challenge.

---

## 12. Checklist trước khi dùng

> [!warning] Hidden OB không phải nút "mua/bán"
> Nó chỉ là vùng POI ẩn. Entry vẫn cần retrace + CISD/MSS + đúng bias/PD.

- [ ] Hai nến **cùng màu** liên tiếp trên khung bias
- [ ] Wick hai nến **thật sự chồng** (không có khoảng hở)
- [ ] Đã **vẽ box** wick→wick đúng chiều
- [ ] **Zoom LTF** thấy OB sạch (nến ngược hướng + displacement + FVG)
- [ ] **Thuận HTF bias** và đúng vùng **Premium/Discount**
- [ ] Có **pool thanh khoản** / **sweep** đi kèm (ưu tiên)
- [ ] Giá đã **retrace về tap** vùng (không đuổi)
- [ ] Có **CISD/MSS** trên LTF làm trigger
- [ ] Xác định rõ **proximal (entry)** và **distal (stop)**
- [ ] Target bám **IRL → ERL**, R:R ≥ ~1:3
- [ ] Không vào trong **phiên thanh khoản mỏng**
- [ ] Rủi ro **≤0.5%** cho lệnh này

---

## 13. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Wick không chồng | Hai nến cùng màu nhưng có khoảng hở giữa wick | Chỉ tính Hidden OB khi wick thật sự overlap |
| Không kiểm chứng LTF | Vẽ box HTF rồi giao dịch luôn | Luôn zoom LTF xác nhận có OB sạch trong box |
| Nhầm với OB thường | Gọi mọi nến ngược hướng là "hidden" | Hidden OB = OB bị 2 nến cùng màu che, chỉ hiện LTF |
| Ngược bias / sai PD | Bullish Hidden OB ở premium, HTF giảm | Lọc theo bias + Premium/Discount trước khi tin |
| Đuổi giá | Vào ngay khi vừa vẽ box, chưa retrace | Chờ giá tap vùng rồi mới tìm trigger |
| Thiếu trigger | Vào "đón đầu" không CISD/MSS | Chỉ vào khi có CISD/MSS trên LTF |
| Giữa range, không sweep | Hidden OB xa mọi pool thanh khoản | Chỉ dùng vùng gắn liquidity / sau sweep |
| Vào tại distal | Chờ giá chạm mép xa mới vào, bị bỏ lại | Vào quanh proximal / Mean Threshold |
| Phiên mỏng | Đọc Hidden OB giờ nghỉ trưa Asia | Bỏ qua phiên thanh khoản thấp |

---

## 14. Câu hỏi tự kiểm tra

- Tôi giải thích được Hidden OB trong 30 giây và phân biệt với OB thường, Mitigation, Breaker không?
- Vì sao Hidden OB "ẩn" trên HTF nhưng "hiện" trên LTF — cơ chế order flow là gì?
- Range box của bullish Hidden OB tính từ đâu đến đâu? Còn bearish?
- Ba bước nhận diện là gì, và "bước ẩn thứ 4" quan trọng thế nào?
- Proximal dùng để làm gì, distal dùng để làm gì?
- Vì sao "sweep rồi Hidden OB" là setup xác suất cao nhất?
- Hidden OB là bias, POI, trigger hay entry? Tôi dùng nó ở bước nào?
- Trong journal của tôi, nhóm lệnh "có Hidden OB + sweep" có expectancy khác nhóm còn lại ra sao?

---

## 15. Flashcards / Active Recall

### Q1
**Hỏi:** Hidden OB là gì trong 1 câu?
**Đáp:** Một Order Block bị che trên HTF vì nằm trong vùng wick chồng của hai nến cùng màu; zoom LTF vào overlap thì OB sạch hiện ra.

### Q2
**Hỏi:** Range box của bullish Hidden OB tính thế nào?
**Đáp:** Từ **low wick của nến thứ 2** lên **high wick của nến thứ 1** (bearish thì ngược: high wick nến 2 → low wick nến 1).

### Q3
**Hỏi:** Ba bước nhận diện Hidden OB?
**Đáp:** (1) Hai nến cùng màu liên tiếp; (2) xác nhận wick chồng nhau; (3) vẽ box wick→wick. Bước ẩn thứ 4: zoom LTF kiểm chứng có OB sạch.

### Q4
**Hỏi:** Hidden OB khác OB thường ở điểm bản chất nào?
**Đáp:** Cùng là Order Block, nhưng OB thường hiện thành một nến thấy được; Hidden OB bị hai nến cùng màu che nên chỉ hiện khi hạ khung — nó luôn là chuyện đa khung.

### Q5
**Hỏi:** Proximal và distal dùng làm gì?
**Đáp:** Proximal (mép gần giá) = điểm vào; distal (mép xa) = nơi đặt stop bên ngoài.

### Q6
**Hỏi:** Vì sao ghép Hidden OB với liquidity sweep lại mạnh?
**Đáp:** Sweep dọn entry sớm + tạo lý do đảo chiều; Hidden OB là vùng fill; CISD/MSS trên LTF là trigger. Bạn vào sau khi bẫy đã sập.

### Q7
**Hỏi:** Hidden OB nên nằm ở vùng PD nào?
**Đáp:** Bullish ở discount, bearish ở premium. Ngược vùng PD là cờ đỏ.

### Q8
**Hỏi:** Hidden OB là trigger hay vùng chờ?
**Đáp:** Là **vùng POI (chờ)**. Phải để giá retrace về rồi mới tìm CISD/MSS trên LTF làm trigger — không vào đón đầu.

---

## 16. Lesson Learned

**Bài học chính:** Hidden OB không phải "mẹo vẽ box" — nó là một Order Block thật, chỉ ẩn trên khung lớn. Giá trị nằm ở kỷ luật đa khung: khoanh vùng HTF, kiểm chứng LTF, chờ retrace, vào bằng trigger.

**Quy tắc cá nhân rút ra:**
- Không có wick chồng → không vẽ. Không có OB sạch trên LTF → không giao dịch.
- Chỉ giao dịch Hidden OB **thuận bias, đúng PD, sau sweep**; ba điều kiện đủ trước khi tính entry.
- Vào tại proximal + CISD, stop ngoài distal, target IRL→ERL, ≤0.5% rủi ro.
- Backtest trước khi tin: đo win-rate/expectancy của Hidden OB tách theo "có/không sweep".

> [!quote] Câu nhắc nhở
> "Order Block tốt nhất là cái đám đông không thấy — nhưng chỉ khi tôi kiểm chứng được nó trên khung dưới. Ẩn với họ, rõ với tôi."

---

> [!cite] Nguồn
> [ICT Hidden Order Block: Spot the Secret PD Array (Step-by-Step)](https://innercircletrader.net/tutorials/what-is-ict-hidden-order-block/)
