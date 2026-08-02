---
type: ict-concept
concept: "Bread and Butter Buy-Setup"
aliases:
  - Bread and Butter Buy-Setup
  - B&B Buy
  - Bread and Butter Buy
tags:
  - trading/ict/model
  - trading/study
  - "#bread-and-butter"
  - "#intraday-scalp"
status: developing
category: "Entry Model"
last_reviewed: 2026-07-28
created: 2026-07-28
updated: 2026-07-28
---

# 11 - Bread and Butter Buy-Setup

> [!info] Link
> [ICT Bread and Butter Buy-Setup](https://innercircletrader.net/tutorials/ict-bread-and-butter-buy-setup/)

> [!summary] Tóm tắt 1 câu
> **Bread and Butter Buy-Setup là mô hình SCALP intraday BULLISH chạy trên 4 session (London Open, NY Open, London Close, Asia Open — giờ New York): khi HTF (D1/H4/H1) institutional order flow đang bullish, IPDA dùng một trong hai engine (offset-accumulation hoặc re-accumulation) để đẩy giá xuống một discount PD array gom sell-side liquidity, ta chờ 5m MSS xác nhận rồi vào LONG tại retest, chốt scalp 15–30 pips (tối đa 50).**

> [!important] Nguyên tắc cốt lõi
> **Hai điều kiện KHÔNG được thiếu: (1) HTF bullish bias phải được xác nhận TRƯỚC (D1 + H4 + HTF PD array); (2) phải chờ 5m MSS tại discount rồi mới vào — chạm discount KHÔNG phải là entry.** Đây là một SCALP 15–30 pips trong 1–2 giờ, RR ~1:1, KHÔNG phải swing. Giữ target scalp là một phần của mô hình; giữ đòi 100 pips là phá mô hình. Luôn dùng **giờ New York** để đọc session — sai timezone là hỏng toàn bộ. Đây là **ảnh gương (mirror)** của [[10 - Bread and Butter Sell Setup]] — cùng khung tư duy, đảo ngược hướng.

> [!tip] Bản đồ đọc note này
> Mục 1–3 = *định nghĩa + 2 engine + 4 session + cấu trúc nhận diện*. Mục 4–5 = *quy trình 10 bước + xác nhận/vô hiệu*. Mục 6 = *ví dụ đúng/sai*. Ba mục **Chuyên sâu A/B/C** = *edge cases, kinh nghiệm live, case studies*. Mục 8–15 = *best practices, checklist, lỗi, flashcards, journal, mastery*. Mới học: 1→6; đã trade: nhảy Chuyên sâu A→C rồi 10.

---

## 1. Định nghĩa

![[BBBuy-Mechanism.svg|697]]

**Bread and Butter Buy-Setup** là bộ khung scalp mua trong ngày của ICT — đối xứng gương với [[10 - Bread and Butter Sell Setup|Bread and Butter Sell]]. "Bread and butter" vẫn giữ nguyên nghĩa *cơm áo gạo tiền*: một setup lặp lại đủ đều để tạo dòng lợi nhuận nhỏ nhưng ổn định, KHÔNG phải cú swing lớn. Bản chất là một chuỗi **fade các cú đẩy giả xuống discount** trong bối cảnh HTF đang bullish.

Toàn bộ mô hình xoay quanh việc IPDA (Interbank Price Delivery Algorithm) đưa giá xuống một vùng discount để **gom sell-side liquidity** rồi đảo chiều tăng. Có **hai engine** để hiểu vì sao giá lại bị đẩy xuống trước khi tăng — mirror trực tiếp của offset-distribution/re-distribution bên bán:

- **Offset-Accumulation** — IPDA reprice giá **xuống dưới một old low** (một pool SSL/sell stops đã biết) để kích sell stops của những người đang long + dụ breakout sellers vào ở **discount**. Sau khi thanh khoản bán đã bị hút đủ, thuật toán đảo chiều tăng mạnh, cung cấp giá tốt cho long entry. Đây là kiểu "quét đáy rồi bật".
- **Re-Accumulation** — IPDA reprice giá xuống tới một **fair-value discount PD array** (FVG/OB/breaker dưới open). Cú hồi này gây **áp lực cover** cho long hiện hữu + **induce selling** từ đám đông tưởng giá sẽ đi tiếp xuống. Nó tạo ra chính sell-side liquidity mà tổ chức cần để vào long ở discount. Đây là kiểu "hồi xuống fair value rồi tích lũy tiếp".

Điểm chung của cả hai — và đây chính là chỗ đối xứng với bên Sell: **giá xuống discount không phải để đi tiếp xuống, mà để tạo nhiên liệu cho một cú mua.** Nhiệm vụ của trader là nhận ra bối cảnh (HTF bullish + đang ở discount) và chờ trigger 5m MSS, y hệt logic bên Sell nhưng lật ngược hướng và lật ngược vùng giá (premium ↔ discount).

**Thông số cốt lõi của mô hình:**

| Thuộc tính | Giá trị |
|---|---|
| Hướng | BULLISH (scalp mua) |
| Số session/ngày | 4 session, mỗi phiên 1 setup → tổng 2–3 setup/ngày, tới 15+/tuần |
| HTF bias | D1/H4/H1 institutional order flow phải BULLISH |
| Execution chart | 5-minute (5m) |
| HTF PD array | từ H1/H4/D1 |
| Mục tiêu | 15–30 pips/lệnh, tối đa 50 pips (nguồn gốc mô tả "30–50 pips/phiên" như biên trên) |
| Thời lượng | 1–2 giờ/lệnh |
| RR | ~1:1 (có thể hơn) |
| Risk | 0.5–1%/lệnh |

> [!note] Vì sao gọi là "bread and butter"
> Giống hệt lý do bên Sell: mô hình không cố bắt cú lớn. Edge đến từ **tần suất + kỷ luật**: nhiều setup nhỏ, mỗi cái RR khiêm tốn nhưng xác suất cao khi bias đúng. Chính vì nhiều lệnh/ngày nên **risk phải chặt** (0.5–1%) — nếu không drawdown cộng dồn rất nhanh, y hệt rủi ro đã nêu ở [[10 - Bread and Butter Sell Setup]].

---

## 2. Bối cảnh sử dụng

Mô hình chạy trên **4 session cố định theo giờ New York** — cùng khung giờ với bên Sell, nhưng ba phiên đầu giờ là LONG (fade Judas xuống); London Close là ngoại lệ (setup NGƯỢC = SELL, khó nhất — đối xứng chính xác với London Close BUY bên mô hình Sell).

| Session | Giờ (NY) | Hành vi kỳ vọng | Entry |
|---|---|---|---|
| **London Open** | 00:00 NY | London tạo **LOW of day** bằng một classic London Judas swing xuống; nhịp hồi 05:00–07:00 NY vào một discount PD array | LONG scalp tại discount sau hồi |
| **NY Open** | 08:20 NY (CME open, nguồn gốc ghi 07:00 NY cho mốc mở cửa rộng nhưng killzone thực thi vẫn canh 08:20 NY) | Đón **NY Judas swing** xuống rồi fade | LONG; target = HTF premium array kế (H1/H4/D1) |
| **London Close** | 10:30–13:00 NY | Setup **NGƯỢC (SELL)** — hồi của đỉnh ngày; chỉ khi London + NY đã **cùng tăng** AND đã chạm HTF premium array | SELL: 5m failure swing ở đỉnh + bearish OB; stop 10 pips trên đỉnh ngày; target 20–30% daily range |
| **Asia Open** | 19:00 NY (0 GMT) | LONG tại/ngay dưới open, kỳ vọng 15–20 pips khi Asian range hình thành | LONG; chậm, cần kiên nhẫn |

**Khi nào mô hình giá trị cao:**
- HTF bullish order flow **rõ ràng** (D1 + H4 đồng thuận, đã có HTF PD array discount để react).
- Đang ở đúng cửa sổ session (giờ NY) và có một cú Judas swing xuống discount sạch.
- Thị trường sạch theo session: FX (GBPUSD, EURUSD, USDCAD, USDJPY), metals; map sạch sang NQ/ES futures — đúng như danh sách cặp mà bên Sell dùng.

**Khi nào nên bỏ qua:**
- Chưa xác nhận HTF bullish bias → mọi discount đều "trông giống" setup nhưng không có edge.
- Ngoài cửa sổ session, hoặc đã trễ session (vào "London" lúc 06:00 NY là trễ).
- London Close mà London + NY **chưa** cùng tăng hoặc chưa chạm HTF premium → không có bối cảnh cho SELL.
- Quanh tin lớn 08:30 NY trên NQ/XAU khi chưa muốn chịu whipsaw quét stop.

---

## 3. Cấu trúc nhận diện

![[BBBuy-Sessions.svg|697]]

**Dấu hiệu chính (LONG):** một **Judas swing xuống vào discount** (offset: quét dưới old low; hoặc re-accumulation: hồi xuống fair-value discount PD array) → theo sau là **MSS 5m lên** (đóng trên một swing high nội phiên + displacement) → **retest** vào post-MSS PD array (FVG/OB/breaker) là điểm vào LONG.

**Điều kiện bắt buộc:**
- HTF (D1/H4/H1) order flow **bullish** đã xác nhận trước.
- Đang trong đúng session theo **giờ NY**.
- Có một **discount PD array** rõ ràng để giá react (FVG/OB/breaker dưới open).
- Có **5m MSS** lên sau khi giá chạm discount — đây là trigger thật.

**Điều kiện tăng xác suất:**
- Judas swing quét sạch một pool SSL/relative equal lows cụ thể trước khi đảo.
- Displacement sau MSS mạnh, dứt khoát (nến thân lớn, đóng cửa quyết đoán).
- HTF premium array kế còn đủ xa để scalp có "room" 15–30 pips.
- Macro window (09:50 NY-AM) hỗ trợ cho NY setup — cùng khung giờ mạnh như bên Sell.

**Điều kiện làm yếu:**
- Không có discount sạch, giá chỉ đi ngang choppy.
- Chạm discount nhưng **không có MSS** (chỉ là pullback nông rồi đi tiếp xuống).
- Session sai / trễ session.
- Tin lớn sắp ra hoặc vừa ra → whipsaw.

> [!warning] Chạm discount KHÔNG phải entry
> Sai lầm phổ biến nhất là long ngay khi giá "chạm" discount — mirror chính xác của lỗi "chạm premium ≠ entry" bên Sell. Discount chỉ là **zone quan tâm**. Trigger thật là **5m MSS** — chỉ khi cấu trúc 5m gãy lên (đóng trên swing high + displacement) thì mới có xác nhận rằng IPDA đã chuyển sang tích lũy.

---

## 4. Quy trình phân tích đa khung + trình tự 10 bước

Đọc từ HTF xuống LTF: **D1/H4 (bias) → H1 (PD array + session context) → 5m (trigger + entry)**.

1. **Xác nhận HTF bullish order flow** — D1 + H4 + HTF PD array (discount để react). Không bullish → không có setup.
2. **Đặt chart về giờ New York.** Đây là bước hay bị bỏ qua nhất và cũng nguy hiểm nhất.
3. **Xác định phiên đang active** — London Open / NY Open / London Close / Asia Open.
4. **Mark discount PD array của phiên** — FVG/OB/breaker dưới open (từ H1/H4/D1 map xuống).
5. **Chờ engine IPDA** — offset-accumulation (quét dưới old low) hoặc re-accumulation (hồi xuống fair-value discount).
6. **Xuống 5m tìm trigger** — chờ **MSS tại discount** (đóng trên swing high + displacement).
7. **Vào ở retest post-MSS PD array** hướng mua (FVG/OB/breaker vừa hình thành).
8. **Stop ngoài đáy discount bị quét + buffer nhỏ.**
9. **Chốt 15–30 pips (max 50)**; trail runner **chỉ khi** HTF premium còn xa.
10. **Risk 0.5–1%/lệnh** — vì 2–3 lệnh/ngày dễ cộng dồn drawdown.

> [!example] Mẫu ghi nhanh — một phiên B&B Buy (LONG)
> ```text
> HTF bias: D1 = bullish, H4 = bullish, HTF PD array discount = [level]
> Timezone: chart đã về giờ NY ✔
> Session: [London Open / NY Open / London Close / Asia Open] @ [giờ NY]
> Discount PD array (dưới open): [type FVG/OB/breaker], zone [low]-[high]
> Engine: [offset-accumulation: quét old low @ level] / [re-accumulation: hồi xuống fair value]
> 5m trigger: MSS đóng trên [swing high] + displacement ✔
> Entry LONG: retest post-MSS PD array @ [price]
> Stop: ngoài đáy discount bị quét @ [price] + buffer
> Target: 15–30 pips → HTF premium array kế @ [level] (max 50)
> Risk: 0.5–1% | RR ~1:1
> ```

---

## 5. Quy tắc xác nhận / vô hiệu hóa

| Trạng thái | Điều kiện | Hành động |
|---|---|---|
| **Xác nhận LONG** | HTF bullish + đúng session (giờ NY) + discount PD array + **5m MSS lên** | Vào LONG tại retest post-MSS PD array |
| **Xác nhận SELL (London Close)** | London + NY đã cùng tăng + đã chạm HTF premium + 5m failure swing đỉnh + bearish OB | SELL, stop 10 pips trên đỉnh ngày, target 20–30% daily range |
| **Chưa đủ (chờ)** | Chạm discount nhưng CHƯA có 5m MSS | Đứng ngoài, chờ MSS — không long sớm |
| **Vô hiệu (skip)** | HTF không bullish / sai session / sai timezone / không có discount sạch | Không trade phiên đó |
| **Vô hiệu sau entry** | Giá đóng lại dưới đáy discount bị quét (stop) hoặc phá cấu trúc MSS ngược | Cắt lệnh, không dời stop chạy theo |
| **Tránh (điều kiện xấu)** | Tin lớn 08:30 NY trên NQ/XAU, thanh khoản mỏng, whipsaw | Đứng ngoài hoặc giảm size mạnh |

---

## 6. Ví dụ chart

### Ví dụ ĐÚNG — NY session Judas fade (LONG)

![[BBBuy-Example-Correct.svg|697]]

HTF bullish đã xác nhận. Vào phiên NY (08:20 NY), giá tạo một Judas swing xuống quét đáy discount (một FVG dưới open) — re-accumulation gom sell-side liquidity. Trên 5m, giá đóng trên swing high nội phiên + displacement = **MSS lên**. Ta chờ **retest** vào post-MSS PD array và vào **LONG**, đặt stop ngoài đáy discount bị quét. Giá tăng về HTF premium array, chốt **+24 pips**. `missing_step: none`.

### Ví dụ SAI — long không bias / bỏ 5m MSS / target tham

![[BBBuy-Example-Wrong.svg|697]]

Trader thấy giá chạm discount liền **long ngay** mà (a) chưa xác nhận HTF bullish bias và (b) chưa có 5m MSS. Vì bối cảnh không phải bullish và không có xác nhận cấu trúc, giá tiếp tục giảm, quét stop dưới discount. Đây là lỗi "chạm discount ≠ entry" cộng với "trade khi chưa có bias" — mirror chính xác lỗi tương ứng ở [[10 - Bread and Butter Sell Setup]]. `missing_step: bias + mss`.

---

## Chuyên sâu A — Edge cases & Failure modes (thực chiến Bread and Butter Buy)

![[BBBuy-EdgeCase-Matrix.svg|720]]

Sáu tình huống đầu tiên dưới đây là bản mirror trực tiếp của Chuyên sâu A bên [[10 - Bread and Butter Sell Setup]] — cùng cơ chế gãy, đảo ngược hướng và đảo ngược vùng giá (discount thay premium). Mỗi ca đọc theo mạch **dấu hiệu → cơ chế → cách xử lý**.

**① Sai timezone (dùng giờ broker thay vì giờ NY).**
*Dấu hiệu:* chart đang hiển thị giờ server/broker chứ không phải giờ New York, các mốc session lệch. *Cơ chế:* toàn bộ mô hình định nghĩa 4 session theo giờ NY; nếu lệch, ta sẽ đón "London Judas" hoặc "NY Judas" vào sai cửa sổ, react với một pool thanh khoản không phải pool mà thuật toán đang nhắm. *Cách xử lý:* ép chart về giờ New York NGAY từ bước 2 của quy trình; ghi rõ "timezone: NY ✔" trong mẫu ghi nhanh trước khi làm bất cứ gì khác.

**② Trade khi HTF bias không bullish.**
*Dấu hiệu:* D1/H4 đang bearish hoặc đi ngang không rõ, nhưng trader vẫn long vì "giá đang ở discount". *Cơ chế:* khi order flow HTF không bullish, một cú đẩy xuống discount thường là move thật (continuation xuống) chứ không phải Judas để tích lũy — mọi discount trông như setup nhưng không có edge. *Cách xử lý:* xác nhận HTF bullish TRƯỚC (bước 1), coi bias là bộ lọc bật/tắt; không bullish thì bỏ toàn bộ các setup long của ngày.

**③ Chạm discount nhưng bỏ 5m MSS → vào sớm.**
*Dấu hiệu:* giá vừa chạm vùng discount, trader long ngay mà không chờ cấu trúc 5m gãy lên. *Cơ chế:* discount chỉ là một zone quan tâm; nếu IPDA chưa chuyển sang tích lũy thì cú chạm chỉ là pullback nông và giá đẩy tiếp xuống — trader bị đẩy ra ở đáy. *Cách xử lý:* bắt buộc chờ 5m MSS (đóng trên swing high + displacement) làm trigger; "chạm discount ≠ entry" phải thành phản xạ.

**④ Target tham biến scalp thành swing.**
*Dấu hiệu:* lệnh đã đạt 15–30 pips nhưng trader giữ đòi 80–100 pips vì "trend còn chạy". *Cơ chế:* mô hình là scalp với RR ~1:1; khi HTF premium array kế còn xa, giá thường phản ứng ngược (quét về âm) trước khi đi tiếp — giữ quá lâu là đứng sai chế độ, y hệt lỗi tương ứng bên Sell. *Cách xử lý:* chốt theo target scalp đã định (15–30, max 50); chỉ trail runner khi HTF premium còn XA và đã chốt phần chính.

**⑤ Ép trade London Close mỗi ngày.**
*Dấu hiệu:* trader cố tìm một setup London Close SELL mỗi phiên. *Cơ chế:* London Close là setup NGƯỢC và khó nhất — nó chỉ hợp lệ khi London + NY đã **cùng tăng** AND giá đã **chạm HTF premium array**; thiếu một trong hai thì không có bối cảnh cho cú hồi đỉnh. *Cách xử lý:* coi London Close là cơ hội có điều kiện, không phải lịch cố định; thiếu điều kiện thì bỏ, để dành cho ba phiên long dễ hơn.

**⑥ NQ/XAU quanh 08:30 news → whipsaw quét stop discount.**
*Dấu hiệu:* trade NQ hoặc XAU ngay quanh tin 08:30 NY, giá giật hai chiều mạnh. *Cơ chế:* phản ứng tin tạo whipsaw quét cả hai đầu — stop đặt ngoài đáy discount dễ bị càn trước khi hướng thật xuất hiện. *Cách xử lý:* tránh vào lệnh mới ngay quanh 08:30 trên NQ/XAU; nếu buộc phải trade thì nới stop hợp lý + giảm size, hoặc chờ 15–30 phút sau tin.

> [!note] Nguyên tắc chung khi nghi ngờ
> Khi bất kỳ ô nào ở trên xuất hiện, **hạ kỳ vọng và ưu tiên giữ tiền**. Trước mỗi lệnh, xác nhận lại đúng ba thứ theo thứ tự: **timezone NY → HTF bullish bias → 5m MSS tại discount**. Thiếu một trong ba là đủ để bỏ phiên đó.

### Sáu edge case bổ sung — độc lập với bên Sell, đặc thù của Buy-Setup

![[BBBuy-EdgeCase-Matrix2.svg]]
> [!info] Mô tả hình
> Ma trận 6 ô (2 hàng x 3 cột): double-dip (2 mũi tên quét xuống), London-low-không-rõ (đáy phẳng khó xác định), Asia-range-nuốt-setup-buy, gap-mở-cửa-cuối-tuần, funding-rate-crypto-tương-quan, NY-Judas-quá-nông.

**⑦ Double dip — giá quét discount hai lần trước khi MSS thật xuất hiện.**
*Dấu hiệu:* giá chạm/xuyên nhẹ qua đáy discount lần 1, bật nhẹ lên nhưng KHÔNG có 5m MSS, sau đó lại rơi quét thêm một pool thấp hơn (lần 2) rồi mới thật sự MSS lên. *Cơ chế:* một pool SSL đơn lẻ đôi khi không đủ thanh khoản đối ứng cho lệnh tổ chức; IPDA có thể cần gom thêm ở một mức thấp hơn trước khi displacement thật xảy ra — hiện tượng bình thường của offset-accumulation trên thanh khoản mỏng, đối xứng chính xác với "double purge" bên Sell (Chuyên sâu A⑦ của [[10 - Bread and Butter Sell Setup]]). *Hành động đúng:* không vào LONG ở lần chạm đầu chỉ vì "nhìn giống Judas"; chờ MSS thật sự xảy ra dù nó đến sau lần quét thứ hai, dời điểm tham chiếu "đáy discount bị quét" sang đáy của lần quét sau cùng. *Bài học:* discount đầu tiên bị quét không tự động là discount sẽ đảo chiều.

**⑧ Đáy London không rõ ràng — hình thành dạng "double bottom phẳng" thay vì một Judas swing sắc nét.**
*Dấu hiệu:* thay vì một cú quét sắc rồi bật (Judas swing cổ điển), giá dao động đi ngang tạo 2-3 đáy gần bằng nhau trong khung 00:00–05:00 NY, không có wick quét rõ ràng để xác định "đáy ngày" duy nhất. *Cơ chế:* khi thanh khoản London mỏng bất thường (lễ EU, đầu tuần sau nghỉ dài), IPDA đôi khi tích lũy qua một range hẹp nhiều giờ thay vì một cú quét dứt khoát — vẫn là accumulation nhưng không có "một cây nến Judas" rõ để bám. Nếu ép tìm một wick sắc như minh họa lý thuyết, trader dễ bỏ lỡ toàn bộ setup vì cứ chờ "cú quét đẹp" không tới. *Hành động đúng:* khi thấy range tích lũy phẳng kéo dài, coi toàn bộ vùng đáy (không phải một điểm) là discount PD array tiềm năng, và chờ MSS 5m phá lên trên biên trên của range đó thay vì chờ một wick quét sắc nét dưới một mức cụ thể. *Bài học:* Judas swing sắc nét là kịch bản phổ biến nhất, không phải kịch bản duy nhất — range tích lũy phẳng vẫn có thể sinh ra MSS hợp lệ.

**⑨ Asia range quá rộng nuốt trọn cả setup Asia Open (mirror của edge case ⑨ bên Sell).**
*Dấu hiệu:* ngay sau 19:00 NY, giá dao động biên độ lớn bất thường khiến target 15–20 pips bị stop trước khi đạt, hoặc entry bị quét ngược trước khi đảo đúng hướng. *Cơ chế:* Asia Open dựa trên giả định range hình thành hẹp và có trật tự; khi có tin tức khu vực Á (BOJ, PBOC, dữ liệu Úc/NZ), biên độ Asia có thể giãn gấp 2–3 lần bình thường. *Hành động đúng:* trước phiên Asia, kiểm tra lịch tin khu vực Á-Thái Bình Dương và ATR Asia gần đây; nếu đang giãn rộng bất thường, giảm size hoặc bỏ hẳn setup Asia hôm đó. *Bài học:* "Asia range hẹp" là một giả định về regime, áp dụng y hệt cho cả buy và sell setup của Asia Open.

**⑩ Gap mở cửa Chủ Nhật/thứ Hai làm sai lệch "old low" tham chiếu.**
*Dấu hiệu:* giá mở cửa tuần mới với một gap đáng kể so với giá đóng cửa thứ Sáu, khiến "old low" mà trader định dùng làm điểm tham chiếu cho offset-accumulation nằm ở phía bên kia của gap — không còn là một pool thanh khoản thực tế trong phiên hiện tại. *Cơ chế:* gap cuối tuần trên FX (đặc biệt các cặp có exposure với tin cuối tuần hoặc thị trường crypto/dầu ảnh hưởng phái sinh) tạo ra một "khoảng trống" giá mà tại đó không có lệnh chờ (resting orders) thực sự — quét qua gap này không mang ý nghĩa thanh khoản như quét một old low được hình thành trong phiên liên tục. *Hành động đúng:* vào đầu tuần (đặc biệt thứ Hai), ưu tiên xác định old low/old high **mới** hình thành sau gap, không dùng mù quáng mức trước gap của tuần trước làm điểm tham chiếu offset-accumulation. *Bài học:* thanh khoản đặt trước gap không "tồn tại" theo cùng cách với thanh khoản hình thành liên tục — gap làm gián đoạn giả định nền tảng của offset-accumulation.

**⑪ Setup Buy trên chỉ số liên quan tài sản có funding/rollover đặc thù (ví dụ NQ quanh phiên đáo hạn hợp đồng).**
*Dấu hiệu:* setup Buy trông đủ điều kiện trên NQ/ES nhưng rơi đúng vào ngày/tuần đáo hạn hợp đồng tương lai (quarterly rollover) — giá có thể biến động bất thường không phản ánh order flow thật của phiên. *Cơ chế:* quanh ngày đáo hạn, thanh khoản dịch chuyển giữa hợp đồng cũ và mới, tạo ra các biến động giá không đến từ cùng động lực IPDA thông thường — dễ nhầm một cú dịch chuyển kỹ thuật (technical roll) với một Judas swing thật. *Hành động đúng:* kiểm tra lịch đáo hạn hợp đồng futures trước khi trade NQ/ES vào cuối mỗi quý; giảm size hoặc chuyển sang cặp FX thuần trong tuần đáo hạn nếu không chắc phân biệt được. *Bài học:* không phải mọi thị trường "map sạch" từ FX sang đều giữ nguyên đặc tính quanh các sự kiện kỹ thuật riêng của thị trường đó.

**⑫ NY Judas quá nông — không đủ để coi là "swing" thật, dẫn đến MSS giả liên tiếp.**
*Dấu hiệu:* tại phiên NY Open, giá chỉ giảm nhẹ vài pip dưới discount rồi bật lên ngay, biên độ Judas nông hơn nhiều so với trung bình lịch sử của cặp đó, khiến MSS 5m theo sau cũng yếu và dễ bị vô hiệu hóa lại gần như ngay lập tức. *Cơ chế:* Judas swing cần đủ biên độ để thật sự "kích" một lượng thanh khoản đáng kể; một cú nhúng nông có thể chỉ là nhiễu 5m bình thường chứ không phải cơ chế gom thanh khoản intent thật — MSS hình thành sau đó cũng dễ là MSS giả (xem tương tự case "double purge/dip"). *Hành động đúng:* so sánh biên độ Judas hiện tại với ATR(5) của các phiên NY gần nhất; nếu biên độ Judas nhỏ hơn đáng kể so với trung bình, hạ mức tin cậy của setup và đòi hỏi displacement sau MSS phải mạnh hơn bình thường để bù lại. *Bài học:* không phải mọi cú nhúng dưới discount đều là Judas swing đúng nghĩa — biên độ tương đối so với lịch sử gần đây là một bộ lọc hữu ích.

---

## Chuyên sâu B — Kinh nghiệm live/backtest thực chiến

![[BBBuy-Advanced-Experience.svg|720]]

Đây là những bài học "trả giá bằng lệnh thật" khi trade Bread and Butter Buy — phần lớn đối xứng với kinh nghiệm bên Sell, nhưng có vài điểm khác biệt đặc thù do bất đối xứng tự nhiên giữa hành vi mua và bán trên thị trường.

1. **Giờ New York là bắt buộc, không thương lượng.** Mọi định nghĩa session của mô hình neo vào giờ NY — giống hệt yêu cầu bên Sell. Ép chart về giờ NY trước khi làm bất cứ gì.

2. **HTF bias TRƯỚC, session sau.** Xác nhận D1/H4 bullish rồi mới chọn session để "săn" discount. Đảo thứ tự là cách tự lừa mình vào các lệnh ngược order flow.

3. **5m MSS là trigger thật; discount chỉ là zone.** Rất nhiều lệnh thua đến từ việc long lúc "chạm discount". Không có MSS 5m thì không có entry.

4. **Giữ target scalp kỷ luật — và tính NET sau spread/commission.** Giống hệt cảnh báo bên Sell: 15–30 pips nghe nhỏ nhưng spread có thể ăn một phần đáng kể, đặc biệt các lệnh 15 pips.

5. **Risk 0.5–1% vì 2–3 lệnh/ngày dễ cộng dồn drawdown.** Nhiều lệnh/ngày nghĩa là một chuỗi thua ngắn có thể xóa nhiều ngày lãi nếu size lớn.

6. **Hành vi khác nhau rõ theo market.** FX sạch theo session; NQ/ES nhạy với macro 09:50 NY-AM; XAU quanh tin thì whipsaw — nới stop, giảm size.

7. **Kỷ luật `missing_step` thống kê theo session/engine.** Ghi `session`, `engine` (offset/reaccumulation) và `missing_step` mỗi lệnh để biết bạn hay hỏng ở phiên nào.

8. **Cần ≥30 mẫu backtest, tách theo session & engine, trước khi tin edge.** Đừng gộp chung tất cả rồi kết luận.

9. **Bất đối xứng quan trọng: Judas swing giảm (Buy-Setup) thường nhanh và sắc hơn Judas swing tăng (Sell-Setup) trên FX.** Nhiều trader kỳ cựu ghi nhận thị trường thường "rơi nhanh hơn khi tăng chậm" — hàm ý các cú quét xuống discount ở phiên London/NY có xu hướng diễn ra trong ít nến hơn (2–3 nến 5m) so với các cú quét lên premium tương ứng bên Sell (có thể kéo 3–5 nến). Hệ quả thực hành: khi trade Buy-Setup, chuẩn bị vào lệnh nhanh hơn sau khi MSS xuất hiện — cửa sổ retest có thể ngắn hơn.

10. **Discount PD array dễ bị "quét sâu qua" hơn premium trong các phiên có tin xấu bất ngờ.** Tin tiêu cực bất ngờ (rủi ro địa chính trị, dữ liệu kinh tế yếu) có xu hướng tạo phản ứng bán tháo mạnh hơn phản ứng mua tương ứng khi có tin tốt — nghĩa là stop dưới discount bị quét sâu ("stop hunt" quá mức dự kiến) xảy ra thường xuyên hơn một chút so với việc premium bị quét sâu bên Sell. Cân nhắc buffer stop rộng hơn một chút (thêm 20–30% so với buffer chuẩn) cho Buy-Setup trong các giai đoạn thị trường lo ngại rủi ro (risk-off).

11. **Demo vs live vs funded account không giống nhau ở khâu execution.** Trên demo, fill thường đúng giá; trên live retail, spread + slippage ăn vào đúng lúc entry; trên funded còn thêm daily loss limit làm biến dạng hành vi.

12. **Kỳ vọng thực tế về tần suất setup A+.** Lý thuyết nói 2–3 setup/ngày, nhưng setup A+ thật sự hiếm hơn nhiều. Backtest thực tế thường cho thấy chỉ khoảng 40–60% số phiên có setup đủ điều kiện — đừng ép đủ số lượng.

13. **Chuỗi thua liên tiếp là toán học, không phải điềm xấu.** Với winrate giả định ~50–55% và tần suất 2–3 lệnh/ngày, chuỗi 4–5 lệnh thua liên tiếp trong một tháng không hề nhỏ — không tự "sửa" quy trình khi không hỏng.

14. **Khi nào được phép tăng size.** Chỉ tăng size sau ≥30 mẫu backtest tách theo session/engine, kết quả live khớp kỳ vọng backtest trong ≥20 lệnh thật, và đã trải qua ít nhất một chuỗi thua mà không phá kỷ luật risk.

> [!tip]
> Một câu gói lại: **timezone NY → HTF bullish bias → discount → 5m MSS → retest long → chốt 15–30 pips; risk chặt vì nhiều lệnh/ngày, và nhớ Judas xuống thường nhanh hơn Judas lên — vào tay nhanh hơn khi MSS đã xác nhận.**

---

## Chuyên sâu C — Case studies mổ xẻ chuyên sâu (kịch bản minh họa)

> [!info] Đọc đúng tinh thần các ca dưới đây
> Tất cả các ca đều là **kịch bản minh họa có nhãn (hypothetical)**, KHÔNG phải lệnh thật và không dùng số liệu giá thật. Mục đích là luyện phản xạ đọc bối cảnh: **chấm điểm bằng process (đúng quy trình hay không), không bằng P&L** của từng ca.

### Case 1 — NY Session WIN (đúng chuẩn)

![[BBBuy-Advanced-CaseStudy-Win.svg|720]]

**Chuỗi:** HTF bullish đã xác nhận (D1 + H4). Chart để giờ NY. Vào phiên NY, tại **08:20 NY** giá tạo một Judas swing xuống vào một **discount FVG** dưới open — re-accumulation gom sell-side liquidity. Trên 5m, giá đóng trên swing high nội phiên + displacement = **MSS lên**. Trader chờ **retest** vào post-MSS PD array và vào **LONG**, stop ngoài đáy discount bị quét. Giá tăng về **HTF premium array** kế, chốt **+24 pips**.

**Chẩn đoán:** Đủ cả ba điều kiện lõi — timezone NY, HTF bullish, 5m MSS tại discount. `session: NY`, `engine: reaccumulation`, `mss_5m: true`, `missing_step: none`.

**Bài học:** Khi bias + session + MSS đồng thuận, đây là một scalp "cơm áo" điển hình — mirror trực tiếp của Case 1 bên [[10 - Bread and Butter Sell Setup]].

### Case 2 — LOSS (không bias / bỏ 5m MSS)

![[BBBuy-Advanced-CaseStudy-Loss.svg|720]]

**Chuỗi (gãy):** Trader thấy giá chạm một vùng discount đẹp trong phiên NY và **long ngay**, nhưng (a) chưa xác nhận HTF bullish — D1/H4 thực ra đang đi ngang, và (b) chưa có 5m MSS. Giá chỉ pullback nông rồi tiếp tục giảm, quét stop dưới discount.

**Chẩn đoán:** Vi phạm hai điều kiện lõi cùng lúc. `missing_step: bias + mss`.

**Bài học:** Discount chỉ là zone. Nếu không có HTF bullish và không có 5m MSS thì đó không phải setup, chỉ là một cú long cảm tính.

### Case 3 — No-Trade đúng (không có Judas/discount sạch, hoặc London Close không đồng tăng)

![[BBBuy-Advanced-CaseStudy-NoTrade.svg|720]]

**Chuỗi:** Vào phiên, giá đi ngang choppy — **không có cú Judas swing xuống discount sạch**, không có discount rõ để react, và không xuất hiện 5m MSS. Ở kịch bản London Close, London + NY **chưa cùng tăng** và giá **chưa chạm HTF premium** → không có bối cảnh cho cú SELL hồi đỉnh. Trader đứng ngoài, chỉ đánh dấu các pool BSL/SSL để chờ.

**Chẩn đoán:** Thiếu điều kiện bắt buộc. `missing_step: none` (đây là skip đúng, không phải lỗi).

**Bài học:** Không có setup thì đứng ngoài chính là quyết định thắng — mirror trực tiếp của nguyên tắc "good skip" bên Sell.

### Case 4 — WIN: Double dip trước MSS thật (London Open, không hoảng khi bị quét lần đầu)

> [!info] Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa

![[BBBuy-Advanced-CaseStudy-DoubleDip-Win.svg|720]]

**Chuỗi:** HTF bullish đã xác nhận (D1 + H4). Đầu phiên London (00:00 NY), giá quét nhẹ một đáy discount cũ nhưng KHÔNG có 5m MSS theo sau — chỉ bật nhẹ. Trader **không long** (đúng theo Chuyên sâu A⑦). 35 phút sau, giá rơi xuống quét thêm một pool SSL thấp hơn (lần quét thứ hai), rồi mới đóng trên swing high nội phiên + displacement = **MSS lên thật**. Trader vào LONG tại retest post-MSS, stop ngoài đáy của **lần quét thứ hai**. Giá tăng về HTF premium, chốt **+21 pips**.

**Chẩn đoán:** `session: London`, `engine: offset`, `mss_5m: true`, `missing_step: none`. Ví dụ trực tiếp của Chuyên sâu A⑦.

**Bài học:** Một lần chạm discount không phải sàn của Judas swing — kiên nhẫn chờ MSS thật quan trọng hơn việc đoán đúng đáy nào là đáy cuối cùng.

### Case 5 — LOSS: Gap cuối tuần làm sai lệch old low tham chiếu (London Open thứ Hai)

> [!info] Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa

![[BBBuy-Advanced-CaseStudy-WeekendGap-Loss.svg|720]]

**Chuỗi:** HTF bullish, thứ Hai đầu tuần. Giá mở cửa gap xuống đáng kể so với đóng cửa thứ Sáu. Trader vẫn dùng old low của thứ Sáu (bên kia gap) làm mức tham chiếu cho offset-accumulation, chờ giá quét xuống đúng mức đó. Giá không bao giờ quay lại chạm mức cũ đó (vì gap đã "nhảy qua" vùng thanh khoản đó) — thay vào đó hình thành một low mới ngay sau gap mà trader bỏ lỡ vì đang chờ sai mức, sau đó đuổi theo long muộn ở một mức tệ hơn và bị stop khi giá hồi nhẹ.

**Chẩn đoán:** `session: London`, `engine: offset`, `mss_5m: true (nhưng muộn, tại mức đuổi theo)`, `missing_step: none về quy trình MSS, nhưng vi phạm Chuyên sâu A⑩` (dùng old low sai tham chiếu qua gap).

**Bài học:** Thanh khoản đặt trước một gap cuối tuần không "còn nguyên" theo cách tính toán thông thường; đầu mỗi tuần cần vẽ lại old low/old high dựa trên hành động giá **sau gap**, không dùng máy móc mức của tuần trước.

### Case 6 — No-Trade đúng: NY Judas quá nông, MSS liên tục bị vô hiệu

> [!info] Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa

![[BBBuy-Advanced-CaseStudy-ShallowJudas-NoTrade.svg|720]]

**Chuỗi:** HTF bullish đúng, phiên NY Open (08:20 NY) có vẻ đang hình thành setup LONG. Nhưng Judas swing xuống chỉ nông bằng khoảng 30% ATR(5) trung bình của phiên NY gần đây. Một MSS 5m hình thành nhưng displacement rất yếu; giá phá lên rồi ngay lập tức bị phá ngược lại (MSS giả). Trader áp dụng Chuyên sâu A⑫: nhận ra Judas quá nông so với lịch sử, hạ mức tin cậy, không vào lệnh dù về lý thuyết "đủ" các bước cấu trúc.

**Chẩn đoán:** `session: NY`, `missing_step: none` (skip đúng do chất lượng Judas kém, không phải bỏ lỡ setup thật). Minh họa trực tiếp cho phản biện "không phải mọi cú nhúng đều là Judas thật".

**Bài học:** Biên độ tương đối của Judas swing so với ATR gần đây là một bộ lọc chất lượng quan trọng — cấu trúc "đủ điều kiện trên giấy" không thay thế được việc đánh giá độ tin cậy của chính cú quét đó.

> [!summary] Sáu ca — một thông điệp
> Trước mỗi lệnh, xác nhận theo đúng thứ tự **timezone NY → HTF bullish bias → discount → 5m MSS**, rồi **chốt theo target scalp**. Kết quả từng lệnh (win/loss) là **nhiễu**; sự nhất quán của process mới là **tín hiệu**. Case 4–6 cho thấy có những lệnh "thua" vì lỗi tham chiếu cụ thể (gap cuối tuần) khác với các lỗi phổ biến bên Sell, và một số tình huống đòi hỏi đánh giá chất lượng Judas thay vì chỉ đếm đủ bước. Ghi `session`, `engine` và `missing_step` mỗi lệnh ([[07 - Reviews]]) để biến các kịch bản này thành phản xạ. Xem thêm setup ngược [[10 - Bread and Butter Sell Setup]], [[18 - Kill Zones]].

---

## Phản biện & Giới hạn của mô hình

> [!warning] Đọc trước khi tin tuyệt đối vào Bread and Butter Buy
> Phần này không phủ nhận giá trị của mô hình — nó tồn tại để bạn dùng Bread and Butter Buy như một **công cụ xác suất tần suất cao có giới hạn biết trước**, không phải một cỗ máy in tiền chắc chắn. Vì mô hình giao dịch nhiều lần/ngày, sai lệch nhỏ trong giả định sẽ bị nhân lên nhanh — đúng như đã cảnh báo ở bản mirror [[10 - Bread and Butter Sell Setup]].

### 1. "IPDA tích lũy giá liên ngân hàng" là narrative không thể kiểm chứng — vẫn có cách đọc khác cho cùng hiện tượng giá

Toàn bộ câu chuyện "IPDA cố tình đẩy giá xuống discount để gom sell-side liquidity rồi mới tích lũy" là một **narrative**, không phải một cơ chế đã được bất kỳ ngân hàng/tổ chức nào xác nhận công khai — hoàn toàn đối xứng với phản biện đã nêu ở [[10 - Bread and Butter Sell Setup]]. Các cách giải thích thay thế hợp lý cho cùng hiện tượng "xuống rồi lên" quanh phiên mở cửa:
- **Auction market theory:** phiên mở cửa thường test lại vùng giá cực biên của phiên trước để tìm "value" — hành vi price discovery bình thường, không cần giả định ý đồ.
- **Mean-reversion quanh tin/thanh khoản thấp:** nhiều phiên mở cửa có đặc tính spike rồi hồi về do thanh khoản mỏng đầu phiên.
- **Volatility clustering:** giờ mở phiên là thời điểm volatility tập trung theo thống kê — hiện tượng đã biết trong tài chính định lượng.
- **Self-fulfilling prophecy:** khi đủ nhiều trader retail cùng chờ long tại cùng một loại discount PD array, chính hành vi tập thể đó có thể tạo ra một phần hiệu ứng quan sát được.

**Hệ quả thực hành:** bạn không cần tin "IPDA có thật" để trade mô hình này có hiệu quả — chỉ cần các điều kiện quan sát được (discount sweep, MSS, session timing) lặp lại đủ thường xuyên để có edge thống kê.

### 2. Rủi ro thống kê khi backtest Bread and Butter Buy

- **Hindsight bias:** nhìn lại chart đã đóng, gần như mọi cú giảm xuống rồi tăng đều "trông giống" một Judas swing vào discount — mắt bạn tự động bỏ qua các lần giá giảm xuống rồi **không** đảo chiều. Chỉ backtest bar-by-bar mới cho số liệu đáng tin.
- **Degrees of freedom quá nhiều:** chọn "swing high nào" cho MSS, "FVG nào" là discount PD array hợp lệ, "pool nào" là old low đáng quét — càng nhiều bậc tự do càng dễ overfit bằng cách chọn đúng swing/FVG "khớp đẹp" sau khi đã biết kết quả.
- **Cỡ mẫu:** với tần suất 2–3 setup/ngày, một tháng backtest cho ≈ 40–60 mẫu — nhưng tách theo 4 session × 2 engine × nhiều thị trường, mỗi ô con thực ra chỉ có vài mẫu, không đủ để kết luận edge riêng.
- **Survivorship của case được chia sẻ:** các ví dụ "Bread and Butter Buy thành công" lưu hành công khai gần như luôn là ca thắng đẹp — không ai chia sẻ những lần "giống setup" nhưng thất bại, làm người mới ảo tưởng winrate cao hơn thực tế.

### 3. Điều kiện thị trường làm mô hình gãy — cụ thể cho Bread and Butter Buy

- **Ngày trending giảm mạnh một chiều:** không có retracement đủ sâu để tạo discount sạch cho cả 4 session — đặc biệt phá vỡ giả định London Close SELL.
- **Thanh khoản bất thường theo phiên** (lễ US/EU, giữa tháng 12): sweep trông giống Judas nhưng thực ra chỉ là nhiễu giá do thiếu người tham gia.
- **Tần suất giao dịch cao làm chi phí ăn sâu vào edge — điểm đặc thù quan trọng nhất, giống hệt bên Sell:** với 2–3 lệnh/ngày × 15+ lệnh/tuần, spread trung bình 1–2 pip trên target 15 pips tương đương **6–13% RR bị ăn ngay từ entry**. Nếu commission ECN cộng thêm, tổng chi phí trên 15+ lệnh/tuần có thể xóa sạch một phần đáng kể edge lý thuyết.
- **Mục tiêu pip cố định (15–30, max 50) không thích ứng với thay đổi volatility regime theo thời gian:** con số này dựa trên ATR trung bình lịch sử; khi ATR nền thay đổi qua các năm, giữ nguyên con số tuyệt đối là áp dụng máy móc một chuẩn đã lỗi thời. **Cách tự kiểm chứng:** tính lại target scalp như % của ATR(14) H1 hiện tại, review mỗi quý.
- **London Close (SELL) nổi tiếng khó — đối xứng chính xác với London Close (BUY) khó bên mô hình Sell:** vì nó là setup ngược và cần đồng thời hai điều kiện hiếm (London+NY đồng tăng VÀ đã chạm premium), tỷ lệ ngày đủ điều kiện thấp hơn nhiều so với 3 phiên long.
- **Bất đối xứng thị trường thật (điểm khác biệt với Sell, không chỉ là mirror lý thuyết):** dữ liệu thị trường tài chính nói chung cho thấy các đợt giảm giá thường nhanh và mạnh hơn các đợt tăng giá tương ứng (volatility skew) — điều này có nghĩa Judas swing xuống discount trong Buy-Setup có thể "quá tay" và đâm sâu hơn dự kiến thường xuyên hơn so với Judas swing lên premium trong Sell-Setup, làm tăng khả năng stop bị quét dù bias vẫn đúng hướng dài hạn. Đây không phải giả định lý thuyết đối xứng thuần túy mà là một khác biệt thực nghiệm cần tính đến khi đặt buffer stop.

### 4. Con số "15–30 pips, RR ~1:1" lấy từ đâu — và "30–50 pips/phiên" trong nguồn gốc nghĩa là gì?

Nguồn gốc bài viết mô tả mục tiêu ở hai chỗ hơi khác nhau: phần giới thiệu nói "capture at least 30 to 50 pips per session", trong khi phần "Realistic Objectives" chi tiết lại ghi "15 to 30 pips, or maximum 50 pips" mỗi lệnh ([nguồn ICT Bread and Butter Buy-Setup](https://innercircletrader.net/tutorials/ict-bread-and-butter-buy-setup/)). Đây là một điểm không hoàn toàn nhất quán trong tài liệu gốc — con số "30-50/phiên" nhiều khả năng là mô tả marketing ở mức tổng quát, còn "15-30, max 50" mỗi lệnh mới là con số chi tiết dùng để trade. Tài liệu này ưu tiên dùng **15–30 pips/lệnh, tối đa 50** làm chuẩn thực hành, nhất quán với cách file 10 xử lý con số tương đương bên Sell — và khuyến nghị người đọc tự đối chiếu với ATR H1 hiện tại của từng cặp trước khi tin nguyên con số gốc.

### 5. Cách tự kiểm định khách quan

1. **Pre-registration:** viết ra trước quy tắc chính xác cho "Judas swing sạch", "MSS hợp lệ", "discount PD array" trước khi backtest.
2. **Forward test song song backtest:** chạy forward test trên tài khoản demo/nhỏ song song với backtest lịch sử — chênh lệch lớn là dấu hiệu định nghĩa chưa đủ khách quan.
3. **Đếm cả setup bỏ lỡ:** ghi log mọi lần giá đủ điều kiện nhưng bạn không vào — nếu chúng thắng nhiều hơn lệnh thật đã vào, vấn đề nằm ở tâm lý thực thi.
4. **Walk-forward theo quý:** chia dữ liệu thành các quý liên tiếp, tối ưu trên quý trước rồi test mù trên quý sau.
5. **Tối thiểu 100+ mẫu/nhóm regime** trước khi tin một con số winrate/edge riêng cho một session×engine×market cụ thể.

> [!tip] Một câu gói lại phần này
> Bread and Butter Buy là một **khung xác suất tần suất cao**, không phải một quy luật vật lý — và vì volatility skew tự nhiên khiến các cú giảm thường nhanh hơn các cú tăng, mô hình Buy có thể cần buffer stop nới hơn một chút so với bản mirror Sell của nó, dù cấu trúc logic hai bên gần như giống hệt nhau.

---

## Best Practices

> [!summary]
> Đây là các thói quen ở mức chuyên nghiệp / chuẩn prop-firm cho Bread and Butter Buy — phần lớn giống hệt chuẩn mực bên [[10 - Bread and Butter Sell Setup]], chỉ đảo hướng. Vì đây là mô hình nhiều lệnh/ngày, **kỷ luật quy trình và risk chặt** quan trọng hơn bất kỳ một lệnh đơn lẻ nào.

### Quy trình pre-session — cố định bốn thứ trước khi phiên mở

- Trước mỗi phiên (giờ NY), dành 5–10 phút:
  1. Xác nhận **HTF bullish bias** (D1 + H4 + HTF PD array discount) — bộ lọc bật/tắt cho các setup long.
  2. Ép chart về **giờ New York** và ghi lại mốc session đang tới.
  3. Mark sẵn **discount PD array** dưới open (FVG/OB/breaker) và **HTF premium array** kế làm target.
  4. Định trước **risk 0.5–1%** và target scalp 15–30 pips (max 50); ghi daily loss limit.
- Lợi ích: khi phiên mở, bạn chỉ còn một việc — chờ 5m MSS, không phải phân tích lại từ đầu trong lúc giá chạy.

### Kỷ luật giữ target scalp — chống lại chính mình

- Đặt target scalp NGAY khi vào lệnh; không dời target theo cảm xúc giữa lệnh.
- Chỉ trail runner khi **HTF premium còn xa** VÀ đã chốt phần chính — mặc định là chốt trọn ở target.
- Nếu thấy mình liên tục "giữ thêm", ghi lại thành `missing_step: target` và review riêng nhóm này.

### Risk management cho mô hình nhiều lệnh/ngày

- 0.5–1%/lệnh; đặt **daily loss limit** (ví dụ −2R hoặc −1.5%) và dừng ngày khi chạm.
- Không tăng size để "gỡ" sau một chuỗi thua ngắn.
- Tính NET sau spread/commission; bỏ phiên khi spread rộng bào hết RR.
- Cân nhắc buffer stop nới hơn một chút so với bên Sell, do volatility skew khiến các cú quét xuống discount có xu hướng đâm sâu hơn dự kiến (xem Phản biện mục 3).

### Amateur habits vs. Professional habits với Bread and Butter Buy

| Khía cạnh | Amateur (nghiệp dư) | Professional (chuẩn prop-firm) |
|---|---|---|
| Timezone | Dùng giờ broker, không để ý | Luôn ép chart về giờ New York trước |
| Thứ tự phân tích | Thấy discount đẹp rồi long | Xác nhận HTF bullish bias TRƯỚC, session sau |
| Trigger vào lệnh | Long ngay khi chạm discount | Chờ 5m MSS xác nhận rồi mới vào retest |
| Target | Giữ đòi 100 pips "cho bõ" | Chốt 15–30 pips (max 50) theo kỷ luật scalp |
| London Close | Ép tìm SELL mỗi ngày | Chỉ đánh khi London+NY đồng tăng & chạm premium |
| Risk | Size lớn vì "nhiều setup" | 0.5–1%/lệnh + daily loss limit |
| Buffer stop | Dùng chung một buffer cho cả Buy/Sell | Nới buffer Buy hơn do volatility skew xuống nhanh hơn |
| Đánh giá edge | Cảm giác "mô hình này ăn" | ≥30 mẫu backtest tách theo session & engine |

> [!tip]
> Nếu phải tóm gọn Best Practices thành một câu: **"Giờ NY, bias trước, chờ MSS, chốt scalp, risk chặt — và nhớ Judas xuống thường nhanh hơn Judas lên, nên đừng chậm tay khi MSS đã lên."**

---

## 9. Checklist trước khi giao dịch

> [!warning] Chạm discount KHÔNG phải entry
> Không có 5m MSS thì không có lệnh, dù giá đang ở đúng vùng discount đẹp.

- [ ] HTF bullish bias đã xác nhận (D1 + H4 + HTF PD array)?
- [ ] Chart đã về **giờ New York**?
- [ ] Đang trong đúng cửa sổ session (không trễ)?
- [ ] Đã mark discount PD array dưới open (FVG/OB/breaker)?
- [ ] Có engine IPDA rõ (offset quét old low / re-accumulation hồi fair value)?
- [ ] Đã xuất hiện **5m MSS** tại discount (đóng trên swing high + displacement)?
- [ ] Entry ở retest post-MSS PD array?
- [ ] Stop ngoài đáy discount bị quét + buffer (nới hơn nếu đang risk-off)?
- [ ] HTF premium array kế còn đủ xa cho 15–30 pips?
- [ ] Risk 0.5–1% và chưa chạm daily loss limit?
- [ ] (London Close) London + NY đã cùng tăng & chạm HTF premium chưa?
- [ ] Nếu đầu tuần: đã vẽ lại old low/old high SAU gap cuối tuần, không dùng mức cũ trước gap?

---

## 10. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Sai timezone | Chart dùng giờ broker | Đón Judas sai cửa sổ session, react sai pool | Ép chart về giờ New York trước khi làm gì |
| Trade khi chưa bullish bias | Long vì "giá ở discount" | Mọi discount trông như setup, không có edge | Xác nhận HTF bullish TRƯỚC (bộ lọc bật/tắt) |
| Bỏ 5m MSS (vào sớm) | Long ngay khi chạm discount | Bị đẩy tiếp xuống, stop-out ở đáy | Chờ 5m MSS; "chạm discount ≠ entry" |
| Phá session boundary | Trade "London" lúc 06:00 NY | Đã trễ session, bối cảnh khác | Tôn trọng cửa sổ giờ NY của từng phiên |
| Target tham | Giữ 100 pips, biến scalp thành swing | Giá quay lại quét khi premium còn xa | Chốt 15–30 (max 50); trail chỉ khi premium xa |
| Ép London Close mỗi ngày | Cố tìm SELL hằng phiên | Setup khó nhất, thiếu điều kiện | Chỉ đánh khi London+NY đồng tăng & chạm premium |
| Dùng old low trước gap cuối tuần | Chờ giá về mức thứ Sáu sau gap thứ Hai | Mức tham chiếu không còn ý nghĩa thanh khoản | Vẽ lại old low/high sau gap, không dùng mức cũ |

---

## 11. Câu hỏi tự kiểm tra

- HTF bias có thật sự bullish không (D1 + H4 + HTF PD array)?
- Chart của tôi đang ở giờ nào — đã về giờ New York chưa?
- Tôi đang ở phiên nào và có còn trong cửa sổ session không?
- Discount PD array nằm ở đâu, engine là offset hay re-accumulation?
- Đã có 5m MSS chưa, hay tôi mới chỉ thấy giá "chạm" discount?
- Entry của tôi ở retest post-MSS PD array, stop ngoài đáy bị quét chưa?
- HTF premium kế còn xa không — target scalp 15–30 pips có "room" không?
- Tôi đang giữ target scalp hay đang tham đòi 100 pips?
- (London Close) London + NY đã cùng tăng & chạm HTF premium chưa?
- Nếu đầu tuần: tôi có đang dùng nhầm old low trước gap cuối tuần không?

---

## 12. Flashcards / Active Recall

> [!question] Bread and Butter Buy là loại mô hình gì, RR và target bao nhiêu?
> Mô hình **scalp intraday bullish** chạy trên 4 session (giờ NY); target **15–30 pips (max 50)**, thời lượng 1–2h, **RR ~1:1**, risk 0.5–1%/lệnh.

> [!question] Hai engine IPDA của mô hình là gì?
> **Offset-Accumulation** (quét xuống dưới old low → kích sell stops → đảo tăng) và **Re-Accumulation** (hồi xuống fair-value discount PD array → induce selling → tích lũy mua). Cả hai đều gom sell-side liquidity ở discount trước khi tăng.

> [!question] Trigger thật để vào lệnh là gì — có phải "chạm discount" không?
> KHÔNG. Chạm discount chỉ là zone. Trigger thật là **5m MSS** (đóng trên swing high + displacement); entry là ở **retest post-MSS PD array**.

> [!question] Bốn session (giờ NY) và hướng của chúng?
> **London Open (00:00)** LONG · **NY Open (08:20)** LONG · **London Close (10:30–13:00)** SELL (ngược, khó nhất) · **Asia Open (19:00)** LONG.

> [!question] Vì sao London Close là setup khó nhất?
> Vì nó là setup NGƯỢC (SELL) và chỉ hợp lệ khi **London + NY đã cùng tăng** AND giá **đã chạm HTF premium array**; thiếu điều kiện thì không được ép.

> [!question] Bread and Butter Buy khác gì so với bản mirror Sell của nó ngoài hướng giao dịch?
> Về logic thì gần như giống hệt (đảo premium↔discount, offset-distribution↔offset-accumulation). Khác biệt thực nghiệm quan trọng: volatility skew khiến Judas swing xuống (Buy) có xu hướng nhanh/sâu hơn Judas swing lên (Sell) — nên buffer stop và tốc độ vào lệnh cần điều chỉnh tương ứng.

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
> Nếu vault có folder riêng như `Trades`, hãy thay `FROM ""` bằng path tương ứng, ví dụ: `FROM "05 - Live Trading Journal/Trades"`.

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: BnB-Buy
session: NY # London | NY | LondonClose | Asia
engine: offset # offset | reaccumulation
htf_bias: bullish
mss_5m: true # đã có 5m MSS tại discount chưa
pips_target: 25 # target scalp (15-30, max 50)
missing_step: none # none | bias | mss | session | target | timezone
```

> [!tip]
> Theo dõi PnL tách riêng theo `session` và `engine` — nếu một phiên/engine âm dài hạn trên một market, dữ liệu đang nói bạn nên bỏ nhóm đó. Thống kê `missing_step` để biết bạn hay hỏng ở khâu nào nhất.

---

## 14. Lesson Learned

### Bài học chính
- Bread and Butter Buy là **scalp tần suất**, không phải swing — edge đến từ lặp lại kỷ luật + risk chặt, không từ một cú lớn.
- **Timezone NY → HTF bullish bias → 5m MSS** là ba điều kiện lõi; thiếu một là bỏ phiên.
- Chạm discount **không phải** entry; 5m MSS mới là trigger.
- Target scalp là một phần của mô hình — giữ tham biến scalp thành swing là cách phá edge nhanh nhất.
- London Close (SELL) là phiên khó nhất, chỉ đánh khi London+NY đồng tăng & đã chạm HTF premium.
- Nhiều lệnh/ngày → risk 0.5–1% + daily loss limit là bắt buộc.
- Đây là mirror của [[10 - Bread and Butter Sell Setup]] nhưng không đối xứng tuyệt đối về hành vi giá — volatility skew là khác biệt thực nghiệm cần nhớ.

### Quy tắc cá nhân rút ra
- [ ] Tôi luôn ép chart về giờ New York trước khi đọc session.
- [ ] Tôi xác nhận HTF bullish bias TRƯỚC, chọn session sau.
- [ ] Tôi chỉ vào lệnh sau khi có 5m MSS tại discount, tại retest post-MSS.
- [ ] Tôi chốt theo target scalp 15–30 pips (max 50), không đòi 100.
- [ ] Tôi không ép London Close khi thiếu điều kiện đồng tăng/premium.
- [ ] Tôi giữ risk 0.5–1% và dừng khi chạm daily loss limit.
- [ ] Tôi ghi `session`, `engine`, `missing_step` mỗi lệnh để review theo nhóm.
- [ ] Tôi vẽ lại old low/high sau gap cuối tuần thay vì dùng mù quáng mức cũ.

### Câu nhắc nhở khi trade
> **"Giờ NY, bias trước, chờ MSS, chốt scalp. Chạm discount chưa phải là lệnh — 5m MSS mới là."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Nắm 2 engine (offset-accumulation/re-accumulation) và bản chất scalp chưa? |
| Nhận diện trên chart |  | Thấy Judas ↓ vào discount + 5m MSS đúng session (giờ NY)? |
| Biết khi nào bỏ qua |  | Nhận ra thiếu bias / sai timezone / thiếu MSS / London Close thiếu điều kiện? |
| Kết hợp với context HTF |  | Ghép HTF bullish bias + discount/premium + session? |
| Áp dụng vào trade thực tế |  | Giữ được target scalp và risk chặt không? |
| Hiểu khác biệt với bản mirror Sell |  | Biết vì sao buffer stop Buy cần nới hơn (volatility skew)? |
| Review sau trade |  | Có ghi `session`, `engine`, `missing_step` và review theo nhóm không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập **≥30 mẫu backtest**, tách riêng theo **session** (London/NY/LondonClose/Asia) & **engine** (offset/reaccumulation).
- [ ] Thống kê winrate + kỳ vọng NET (sau spread/commission) cho từng nhóm session/engine trên từng market (FX vs NQ/ES vs XAU).
- [ ] Đếm tần suất từng giá trị `missing_step` (bias/mss/session/target/timezone) để tìm khâu hỏng nhiều nhất.
- [ ] So sánh trực tiếp thống kê Buy-Setup với Sell-Setup ([[10 - Bread and Butter Sell Setup]]) trên cùng market để kiểm chứng thực nghiệm giả thuyết volatility skew.
- [ ] Cập nhật rule riêng (ví dụ bỏ Asia trên XAU, hoặc chỉ đánh NY re-accumulation) khi đủ mẫu.
