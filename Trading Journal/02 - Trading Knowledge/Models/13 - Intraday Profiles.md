---
type: ict-concept
concept: "ICT Intraday Profiles (Daily Profiles)"
aliases:
  - ICT Intraday Profiles
  - ICT Daily Profiles
  - London Protraction Model
  - CBDR Model
tags:
  - trading/ict/model
  - trading/study
  - "#intraday-profiles"
  - "#CBDR"
  - "#judas-swing"
status: developing
category: "Entry Model"
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - ICT Intraday Profiles
  - CBDR
  - Judas Swing
  - London Protraction
last_reviewed: 2026-07-28
created: 2026-07-28
updated: 2026-07-28
common_mistakes:
  - "[[Mistake - Skip CBDR Size Check]]"
  - "[[Mistake - Pre-position Before Judas Swing]]"
  - "[[Mistake - Confuse Normal With Delayed Protraction]]"
---

# 13 - Intraday Profiles

> [!info] Link
> [ICT Intraday Profiles (Daily Profiles) — London Protraction Model](https://innercircletrader.net/tutorials/ict-intraday-profiles/)

> [!summary] Tóm tắt 1 câu
> **Intraday Profiles là khung day-trading dựa trên chuỗi ba mốc giờ New York cố định — Central Bank Dealers Range (CBDR, 14h–20h) → Asian range (20h–0h) → Judas Swing (0h–2h) — để dự đoán một trong bốn kịch bản (London Normal/Delayed × Buy/Sell) cho phần còn lại của phiên London/NY-AM.**

> [!important] Nguyên tắc cốt lõi
> **Mô hình chỉ hợp lệ khi CBDR và Asian range đủ HẸP (nén) — đây là tiền đề bắt buộc, không phải chi tiết phụ.** CBDR/Asian range rộng nghĩa là thị trường đã "dùng" biến động của khung giờ đó, làm hỏng độ tin cậy của projection SD sau đó. Luôn dùng **giờ New York** để đọc mốc; và luôn chờ **MSS LTF** sau protraction — protraction một mình không phải entry.

> [!tip] Bản đồ đọc note này
> Mục 1–5 = *định nghĩa 3 mốc giờ + 4 profile + cấu trúc nhận diện + quy trình đa khung + xác nhận/vô hiệu*. Mục 6 = *ví dụ đúng/sai*. Mục 7 = *sequence mẫu theo giờ*. Các mục **Chuyên sâu** = *Phản biện, Edge cases, Case studies, Kinh nghiệm live/backtest*. Mục cuối = *best practices, checklist, lỗi thường gặp, flashcards, nguồn*.

---

## 1. Định nghĩa

![[IntradayProf-Definition-Timeline.svg]]
> [!info] Mô tả hình
> Timeline ngang theo giờ NY từ 14:00 tới 08:00 hôm sau, chia 3 khối màu: CBDR (14h–20h, khối xanh dương nhạt) → Asian range (20h–0h, khối tím nhạt) → Judas Swing window (0h–2h, khối cam nhạt) → London/NY-AM session (2h–8h, khối xám). Đường giá minh họa đi ngang trong CBDR+Asian, rồi có một nhịp đẩy (Judas) trước khi đảo chiều vào London.

**Khái niệm:** ICT Intraday Profiles (còn gọi Daily Profiles) là một mô hình day-trading hoàn chỉnh, xây trên 3 mốc thời gian cố định theo giờ New York:

| Mốc | Giờ NY | Vai trò |
|---|---|---|
| **CBDR** — Central Bank Dealers Range | 14:00–20:00 | Range tham chiếu để tính SD projection |
| **Asian range** | 20:00–00:00 | Xác nhận thêm mức độ nén của thanh khoản trước Judas |
| **Judas Swing window** | 00:00–02:00 | Cửa sổ giá tạo cú đẩy giả (rally nếu sell day, dip nếu buy day) |

**Ngưỡng gốc (theo bài viết ICT tổng hợp — xem Phản biện #1 về tính lỗi thời):**
- CBDR nên **< 40 pip**.
- Asian range nên **20–30 pip**.
- Protraction của Judas Swing không vượt quá **2–3 độ lệch chuẩn (SD)** của CBDR.

**SD projection:** từ CBDR, vẽ các đường chiếu 1, 2, 3 lần độ rộng CBDR lên trên và xuống dưới — đây là giới hạn kỳ vọng cho Judas Swing. ICT gọi đây là "standard deviation" nhưng đây là **thuật ngữ quy ước (misnomer)**, không phải độ lệch chuẩn thống kê thật (xem Phản biện #2).

**Bốn profile (2 hướng × 2 kiểu protraction):**

| Profile | Bias | Hành vi 0h–2h NY | Protraction |
|---|---|---|---|
| London Normal — Sell | Bearish | Rally lên trên CBDR đúng cửa sổ 0h–2h | Đúng giờ (Normal) |
| London Delayed — Sell | Bearish | KHÔNG rally đúng giờ; IPDA vào protraction sau 2h | Trễ (Delayed) |
| London Normal — Buy | Bullish | Dip xuống dưới CBDR đúng cửa sổ 0h–2h | Đúng giờ (Normal) |
| London Delayed — Buy | Bullish | KHÔNG dip đúng giờ; IPDA vào protraction sau 2h | Trễ (Delayed) |

**Judas Swing:** là cú đẩy giá (rally cho sell day, dip cho buy day) ra khỏi CBDR trong cửa sổ 0h–2h — đóng vai trò tương tự Judas Swing trong Silver Bullet/killzone models: một cú đẩy giả để gom thanh khoản retail trước khi đảo chiều đúng bias thật của ngày.

![[IntradayProf-4Profiles-Matrix.svg]]
> [!info] Mô tả hình
> Ma trận 2×2: cột "Normal" / "Delayed", hàng "Sell (bearish)" / "Buy (bullish)". Mỗi ô mini-chart nhỏ minh họa hành vi giá 0h–2h NY tương ứng (rally đúng giờ, rally trễ, dip đúng giờ, dip trễ). Góc dưới mỗi ô ghi rõ tên profile và mức tin cậy tương đối (Normal viền xanh đậm hơn Delayed).

---

## 2. Bối cảnh sử dụng

### Khi nào mô hình này có giá trị cao?
- [ ] Bias D1/H4 xác định trước (bullish/bearish), không neutral.
- [ ] CBDR < 40 pip (FX major) — hoặc ngưỡng tương đương đã chuẩn hóa theo ATR cho thị trường khác.
- [ ] Asian range 20–30 pip, xác nhận thêm mức nén.
- [ ] Judas Swing xảy ra trong 0h–2h NY (Normal) hoặc rõ ràng bị trễ tới sau 2h (Delayed) — không mơ hồ giữa hai loại.
- [ ] Protraction không vượt quá 2–3 SD của CBDR.

### Khi nào nên bỏ qua?
- [ ] CBDR hoặc Asian range quá rộng (thị trường đã "dùng" biến động sớm — projection SD mất ý nghĩa).
- [ ] Không có bias HTF rõ.
- [ ] Đã pre-position trước khi Judas Swing thật sự xảy ra.
- [ ] Tuần có FOMC/CPI/NFP làm nhiễu toàn bộ chuỗi CBDR–Asian–Judas.
- [ ] DST transition tuần vừa đổi giờ chưa kiểm tra lại múi giờ output data.

### Thị trường & timeframe phù hợp
- **Thiết kế gốc:** chỉ số NQ/E-mini (Michael Huddleston), sau mở rộng sang FX majors và kim loại (XAU/USD).
- **Timeframe:** D1 làm parent bias; M15/M5 để quan sát protraction; M5/M1 để bắt MSS trigger và fill.
- **Best profile:** London Normal Protraction (cả Buy và Sell) — tin cậy hơn Delayed vì Delayed dễ nhầm với ngày chạy một chiều không đảo (xem Phản biện #3).

> [!tip]
> Trader mới nên tập trung London Normal Protraction trong 30 ngày demo đầu trước khi thêm biến thể Delayed — đúng khuyến nghị gốc của tài liệu ICT.

---

## 3. Cấu trúc nhận diện trên chart

![[IntradayProf-CBDR-AsianRange.svg]]
> [!info] Mô tả hình
> Chart 2 tầng: tầng trên là CBDR (14h–20h NY) với range hẹp và 3 đường SD projection (1/2/3 SD) kẻ lên trên + xuống dưới bằng nét đứt vàng; tầng dưới là Asian range (20h–0h) nằm gọn trong CBDR. Nhãn ghi rõ độ rộng pip của mỗi range.

### Dấu hiệu chính
1. **CBDR hẹp** (14h–20h NY) — range compact, không có spike lớn do tin.
2. **Asian range hẹp**, nằm gần hoặc trong CBDR — xác nhận thêm mức nén.
3. **SD projection** vẽ từ CBDR: 1, 2, 3 SD trên và dưới.
4. **Judas Swing** trong 0h–2h: giá đẩy ra ngoài CBDR theo hướng NGƯỢC với bias (rally nếu sell day, dip nếu buy day).
5. **MSS LTF (M5/M1)** xác nhận đảo chiều đúng bias ngay sau protraction.
6. **Entry** tại retest premium PD array (sell) hoặc discount PD array (buy).

### Ma trận nhận diện — London Normal Sell Profile

| Bước | Phải thấy gì | Cảnh báo nếu thiếu |
|---|---|---|
| Bias | D1/H4 bearish | Không rõ → bỏ toàn bộ mô hình hôm đó |
| CBDR | < 40 pip, sạch (không tin lớn) | CBDR rộng → SD projection không đáng tin |
| Asian range | 20–30 pip | Quá rộng/quá hẹp bất thường → nghi ngờ regime khác |
| Judas Swing | Rally lên trên CBDR trong 0h–2h | Không rally đúng giờ → chuyển sang Delayed profile |
| Protraction | ≤2–3 SD của CBDR | Vượt hẳn 3 SD → nghi ngờ đây không còn là Judas Swing mà là breakout thật |
| MSS | M5/M1 xuống, có displacement | MSS yếu/không có → chưa xác nhận, không vào |
| Entry | SELL tại premium PD array sau MSS | Vào ngay tại đỉnh protraction (chase) → risk cao, chưa xác nhận |

### Điều kiện bắt buộc
- [ ] Bias HTF xác định trước.
- [ ] CBDR + Asian range đều đủ hẹp theo ngưỡng đã chuẩn hóa cho thị trường đang trade.
- [ ] Có protraction (rally/dip) trong hoặc sau cửa sổ 0h–2h, đúng hướng ngược bias.
- [ ] MSS LTF xác nhận đảo chiều sau protraction.

### Điều kiện tăng xác suất
- [ ] Protraction chạm đúng vùng 1–2 SD (không quá sát CBDR, không vượt 3 SD).
- [ ] MSS trùng với một premium/discount PD array HTF (confluence).
- [ ] Profile là Normal (đúng giờ 0h–2h), không phải Delayed.
- [ ] Không có tin lớn (NFP/CPI/FOMC) trong hoặc gần cửa sổ Judas Swing.

### Điều kiện làm setup yếu đi
- CBDR/Asian range rộng bất thường (regime volatility cao).
- Protraction vượt quá 3 SD mà không có MSS đảo chiều theo sau.
- Profile mơ hồ giữa Normal và Delayed (protraction bắt đầu lúc 1h55, kết thúc mờ nhạt).
- Tuần FOMC hoặc DST transition chưa hiệu chỉnh giờ.

![[IntradayProf-SDProjection.svg]]
> [!info] Mô tả hình
> CBDR vẽ giữa làm dải gốc; ba cặp đường nét đứt vàng song song chiếu lên/xuống ở khoảng cách 1×, 2×, 3× độ rộng CBDR, nhãn "1 SD", "2 SD", "3 SD". Chú thích nhỏ "Đây là quy ước chiếu tỷ lệ, KHÔNG phải độ lệch chuẩn thống kê tính từ phân phối xác suất". Một mũi tên cam minh họa Judas Swing chạm vùng 2 SD trước khi MSS đảo chiều.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] 4 câu hỏi bắt buộc trước khi trade Intraday Profile
> 1. **Bias D1/H4 là gì?**
> 2. **CBDR và Asian range có đủ hẹp theo ngưỡng đã chuẩn hóa không?**
> 3. **Judas Swing xảy ra đúng giờ (Normal) hay trễ (Delayed), protraction bao nhiêu SD?**
> 4. **MSS LTF đã xác nhận chưa, entry/stop/target ở đâu?**

### D1/H4 — Bias & bối cảnh
- Xác định bias ngày trước 14:00 NY (trước khi CBDR bắt đầu hình thành) để tránh nhìn ngược từ kết quả.
- Xác định draw on liquidity HTF — premium PD array (cho sell) hoặc discount PD array (cho buy) làm target sau MSS.

### 14h–0h NY — Đo CBDR & Asian range
- Đo độ rộng CBDR (14h–20h) khi phiên đóng lúc 20:00 NY.
- Vẽ SD projection 1/2/3 lần độ rộng CBDR.
- Đo Asian range (20h–0h) khi phiên đóng lúc 0:00 NY — xác nhận có đồng nhất với CBDR không (cả hai hẹp, hoặc một trong hai rộng bất thường).

### 0h–2h NY — Theo dõi Judas Swing
- Quan sát protraction đúng hướng ngược bias.
- Nếu protraction xảy ra trong khung này → **London Normal**.
- Nếu KHÔNG có protraction rõ trong khung này, chờ tiếp sau 2h → **London Delayed** (dùng dealing range gần nhất thay CBDR/Asian cho stop, xem mục 1 bảng 4 profile).

### M5/M1 — MSS trigger & entry
- Chờ MSS trên M5 (hoặc M1) ngay sau khi protraction đạt hoặc vượt vùng SD kỳ vọng.
- Entry tại retest premium PD array (sell) hoặc discount PD array (buy) hình thành từ MSS.
- Stop trên London-session high (sell) / dưới London-session low (buy) cho Normal; dùng dealing-range high/low cho Delayed.
- Target: draw-on-liquidity HTF, PD array đối diện, hoặc mặc định 50–70 pip.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

**Xác nhận hợp lệ:**
- [ ] Bias HTF rõ, CBDR + Asian range đều hẹp theo ngưỡng chuẩn hóa.
- [ ] Protraction đúng hướng ngược bias, trong phạm vi 2–3 SD.
- [ ] MSS LTF xác nhận đảo chiều đúng bias ngay sau protraction.
- [ ] R:R tới target HTF ≥1:1.5.

**Vô hiệu hóa:**
- CBDR hoặc Asian range vượt xa ngưỡng hẹp kỳ vọng (theo ATR hiện tại) → toàn bộ SD projection sau đó mất cơ sở, nên hạ cấp thành "chỉ scalp, không theo full model".
- Protraction vượt quá 3 SD mà KHÔNG có MSS đảo chiều theo sau trong vài nến → khả năng cao đây là breakout thật của ngày (one-way day), không phải Judas Swing (xem Edge case tương ứng).
- Tin lớn (NFP/CPI/FOMC châu Âu hoặc Mỹ) rơi vào giữa cửa sổ Judas Swing → protraction có thể do tin, không phải cấu trúc IPDA thông thường.

---

## 6. Ví dụ chart

![[IntradayProf-Example-Correct.svg]]
> [!info] Mô tả hình
> Timeline: CBDR 14h–20h hẹp (28 pip) với SD projection 1/2/3 vẽ trên/dưới. Asian range 20h–0h nằm trong CBDR (18 pip). 0h–2h: giá rally lên chạm vùng 2 SD (mũi tên cam, nhãn "Judas Swing — London Normal Sell"). M5 MSS xuống ngay sau đó (đường tím đứt), để lại FVG premium. Entry SELL tại FVG, target xuống HTF discount PD array.

### Ví dụ ĐÚNG — London Normal Sell Profile
Bias D1 bearish rõ. CBDR 28 pip (dưới 40), Asian range 18 pip (trong khoảng 20–30, hơi hẹp nhưng chấp nhận được). 0h05 NY, giá rally lên chạm đúng vùng 2 SD của CBDR — Judas Swing đúng giờ (Normal). M5 MSS xuống với displacement rõ ngay sau đó, để lại FVG premium sạch. Entry SELL tại retest FVG, stop trên London-session high, target = discount PD array H4. R:R 1:2.1. Đúng chuẩn toàn bộ chuỗi điều kiện.

### Ví dụ SAI — Vào lệnh khi CBDR đã rộng bất thường
Bias D1 bearish. CBDR đo được 55 pip (vượt xa ngưỡng 40) do có một spike tin nhẹ giữa phiên London Close/NY PM hôm trước. Trader vẫn vẽ SD projection từ CBDR 55 pip này và chờ Judas Swing như bình thường — giá rally lên đúng cửa sổ 0h–2h, có MSS M5 xuống, và trader vào SELL. Sai vì: CBDR đã vượt ngưỡng hẹp ngay từ đầu, khiến SD projection dựa trên một range đã "dùng phần lớn biến động ngày" — vùng 1–3 SD trở nên quá rộng để còn ý nghĩa như Judas Swing limit thật, dẫn tới target/stop bị đặt sai tỷ lệ so với biến động còn lại của ngày.

---

## 7. Sequence mẫu — trình tự thực thi

1. **Trước 14:00 NY:** xác định bias D1/H4. Neutral → bỏ mô hình này hôm nay.
2. **14:00–20:00 NY:** theo dõi & đo CBDR khi đóng. Kiểm tra CBDR có "sạch" (không tin lớn giữa phiên) và có hẹp theo ngưỡng chuẩn hóa cho thị trường đang trade.
3. **20:00 NY:** vẽ SD projection (1/2/3 SD) từ CBDR.
4. **20:00–00:00 NY:** theo dõi Asian range, đo khi đóng. Xác nhận đồng nhất mức nén với CBDR.
5. **00:00–02:00 NY:** quan sát Judas Swing — chờ giá đẩy ngược bias, ghi nhận có protraction trong khung này (Normal) hay không (chuyển Delayed).
6. **Xác định profile:** Normal (protraction 0h–2h) hoặc Delayed (protraction sau 2h) × Buy/Sell theo bias.
7. **Hạ khung M5/M1:** chờ MSS xác nhận đảo chiều đúng bias ngay sau protraction đạt vùng SD kỳ vọng.
8. **Entry:** tại retest PD array premium (sell)/discount (buy) do MSS để lại.
9. **Set stop:** trên/dưới London-session high/low (Normal) hoặc dealing-range high/low (Delayed).
10. **Set target:** draw-on-liquidity HTF, PD array đối diện, hoặc mặc định 50–70 pip nếu không có target rõ hơn.

---

## Phản biện & Giới hạn của mô hình

> [!warning] Đọc trước khi áp nguyên trạng các con số gốc
> Mô hình này có nhiều con số cụ thể (40 pip, 20–30 pip, 2–3 SD) khiến nó DỄ có cảm giác "khách quan, đo lường được" hơn các mô hình ICT khác — nhưng chính vì có số cụ thể, nó cũng dễ bị áp dụng sai khi các con số đó không còn phù hợp với điều kiện thị trường hiện tại.

### 1. Ngưỡng CBDR < 40 pip & Asian range 20–30 pip là số cũ, cần chuẩn hóa theo ATR

![[IntradayProf-ModelCritique-ATRNormalize.svg]]
> [!info] Mô tả hình
> Biểu đồ cột so sánh 2 giai đoạn: "Volatility FX thời điểm số liệu gốc phổ biến" (cột thấp) vs "Volatility FX hiện tại" (cột cao hơn) — mũi tên chỉ "Ngưỡng pip cố định (40/20-30) không co giãn theo cột bên phải" kèm công thức thay thế "Ngưỡng = k × ATR(H1, 6 giờ)".

Con số "CBDR < 40 pip, Asian range 20–30 pip" phổ biến trong tài liệu ICT được truyền miệng/viết lại qua nhiều năm, gắn với một giai đoạn volatility FX cụ thể trong quá khứ — **không có bằng chứng các ngưỡng này được cập nhật định kỳ theo biến động thị trường hiện tại**. Vấn đề thực dụng:
- Volatility trung bình của FX majors thay đổi theo chu kỳ kinh tế (lãi suất, chính sách tiền tệ, biến động vĩ mô) — một ngưỡng pip cố định có thể "quá chặt" trong giai đoạn volatility cao (loại bỏ hầu hết các ngày hợp lệ) hoặc "quá lỏng" trong giai đoạn volatility thấp (chấp nhận cả những ngày CBDR thực ra là rộng so với biến động chung).
- **Cách chuẩn hóa thực dụng hơn:** thay ngưỡng pip cố định bằng ngưỡng tương đối theo ATR — ví dụ CBDR hợp lệ khi độ rộng CBDR < k × ATR(H1) đo trong 6 giờ tương ứng khung CBDR, với k là hệ số tự calibrate trên dữ liệu gần đây (ví dụ 3 tháng gần nhất) của chính cặp tiền/thị trường đang trade, thay vì dùng "40" cố định cho mọi giai đoạn.
- Tương tự với Asian range: dùng % của ATR daily hoặc ATR của đúng phiên Á thay vì số pip tuyệt đối.

### 2. "Standard deviation" của CBDR là thuật ngữ misnomer — không phải SD thống kê thật

Điểm quan trọng cần hiểu rõ để không áp nhầm lý thuyết xác suất: "1/2/3 SD của CBDR" trong ICT **không phải độ lệch chuẩn (standard deviation) tính từ phân phối dữ liệu giá** như trong thống kê thông thường (không có việc tính variance của một tập mẫu quan sát). Nó đơn giản là **1, 2, 3 lần độ rộng của range CBDR**, chiếu lên trên và xuống dưới — một phép nhân hình học, không phải một đại lượng thống kê suy ra từ phân phối xác suất.
- Hệ quả: không thể áp các tính chất của phân phối chuẩn (ví dụ "68% dữ liệu nằm trong 1 SD") cho các vùng này — chúng chỉ là các mốc tỷ lệ quy ước, tương tự Fibonacci extension, không mang ý nghĩa xác suất thống kê nghiêm ngặt.
- Việc dùng từ "standard deviation" tạo cảm giác mô hình có nền tảng thống kê chặt hơn thực tế — cần hiểu đây là quy ước đặt tên, không phải phép tính SD thật, khi giải thích hoặc dạy lại mô hình này cho người khác.

### 3. Model gốc thiết kế cho FX majors — áp lên index/gold cần điều chỉnh gì

Model được test đầu tiên trên NQ/E-mini (theo tick/điểm chỉ số), sau đó lan sang FX (pip) và kim loại (đô/cent). Ba điều chỉnh cần làm khi áp dụng ngoài FX majors:
- **Đơn vị đo:** chuyển ngưỡng pip sang tick (futures) hoặc đô (gold) theo đúng tỷ lệ biến động trung bình của thị trường đó, không dùng nguyên số "40" hay "20–30".
- **Giờ giao dịch:** NQ/ES có giờ mở/đóng và thanh khoản theo phiên khác FX 24 giờ — CBDR 14h–20h NY có thể rơi vào giờ thanh khoản thấp hơn của futures (sau giờ đóng cash session), cần kiểm tra volume thực tế trong khung đó cho từng thị trường trước khi tin số liệu CBDR có ý nghĩa.
- **Gold đặc thù:** XAU/USD có biến động không đối xứng quanh tin tức Mỹ (NFP/CPI/FOMC) nhiều hơn FX majors — CBDR/Asian range trên gold cần biên độ ngưỡng rộng hơn tương ứng, và cửa sổ Judas Swing dễ bị nhiễu bởi tin châu Á/châu Âu hơn (gold nhạy với USD real yield, tin lãi suất toàn cầu).

### 4. Delayed Protraction dễ nhầm với ngày one-way — vấn đề nhận diện quan trọng nhất

London Delayed Protraction (khi Judas Swing không xảy ra trong 0h–2h mà lùi sang sau 2h) có một điểm yếu nhận diện nghiêm trọng: **không có cách phân biệt chắc chắn, theo thời gian thực, giữa "Delayed Protraction sẽ đảo chiều sau 2h" và "ngày chạy một chiều thật (one-way day) không có Judas Swing/không đảo chiều"** cho tới khi đã quá muộn. Cả hai trông giống nhau ở giai đoạn đầu: giá không rally/dip trong 0h–2h, tiếp tục drift nhẹ theo một hướng. Sự khác biệt chỉ lộ ra SAU khi:
- Delayed: giá protract sau 2h rồi có MSS đảo chiều đúng bias.
- One-way: giá tiếp tục drift/tăng tốc theo hướng ban đầu, không hề đảo — thực chất bias ngày đã đổi hoặc đây là ngày trend mạnh không có consolidation-then-reversal.

Không có bộ lọc khách quan công khai để phân biệt hai kịch bản này TRƯỚC khi MSS (hoặc sự thiếu vắng MSS) xuất hiện — đây là lý do tài liệu gốc khuyên tập trung Normal Protraction trước, vì Delayed vốn có tỷ lệ nhận diện sai cao hơn về bản chất cấu trúc.

### 5. Rủi ro thống kê khi backtest mô hình này

- **Hindsight bias:** với 4 profile khả dĩ (Normal/Delayed × Buy/Sell), gần như luôn có MỘT trong bốn khớp với bất kỳ ngày nào nhìn lại — dễ tạo cảm giác mô hình "luôn đúng" khi thực ra chỉ là chọn đúng nhãn sau khi biết kết quả.
- **Degrees of freedom:** chọn ngưỡng CBDR/Asian range bao nhiêu là "hẹp", chọn SD nào (1, 2 hay 3) là điểm vào hợp lệ, chọn thời điểm chính xác nào trong khung 0h–2h là "protraction bắt đầu" — mỗi lựa chọn đều co giãn được để khớp với kết quả mong muốn khi backtest hồi cứu.
- **Sample size:** một tuần chỉ có 5 ngày giao dịch; để có ≥30–50 mẫu MỖI loại trong 4 profile cần tối thiểu vài tháng dữ liệu sạch (loại các tuần FOMC/holiday) — ít trader thực sự tích lũy đủ mẫu trước khi tin vào một profile cụ thể.
- **Cách tự kiểm định khách quan hơn:** định nghĩa TRƯỚC ngưỡng CBDR/Asian range theo ATR (không phải pip cố định), ngưỡng SD entry cụ thể, và mốc giờ chính xác phân biệt Normal/Delayed; forward test tách riêng theo profile, đếm cả các ngày CBDR/Asian range không đạt ngưỡng (loại khỏi mẫu ngay từ đầu, không tính là "miss").

> [!important] Kết luận thực dụng
> Coi các con số gốc (40 pip, 20–30 pip, 2–3 SD) là **điểm khởi đầu tham khảo lịch sử**, không phải hằng số cố định. Tự calibrate lại theo ATR hiện tại của đúng thị trường đang trade, hiểu rõ "SD" ở đây là quy ước hình học chứ không phải thống kê thật, và ưu tiên Normal Protraction trước khi thử Delayed vì Delayed có vấn đề nhận diện cấu trúc khó giải quyết triệt để.

---

## Chuyên sâu A — Edge cases & Failure modes (thực chiến Intraday Profiles)

> [!warning] Đây là phần chỉ live/backtest nhiều mới thấy
> Mỗi edge case theo format: **hiện tượng → cách nhận diện sớm → hành động đúng → bài học**.

### 1. DST làm lệch cả CBDR lẫn killzone

![[IntradayProf-EdgeCase-DST.svg]]
> [!info] Mô tả hình
> Hai timeline xếp chồng: "Trước DST" với CBDR 14h–20h khớp đúng khối màu, "Sau DST (lệch 1 giờ)" với khối CBDR bị dịch lệch so với nhãn giờ trên biểu đồ nếu không cập nhật — mũi tên đỏ cảnh báo "Lệch 1 giờ nếu nguồn dữ liệu chưa đổi timezone".

**Hiện tượng:** Mỹ đổi DST (Chủ Nhật thứ 2 tháng 3 sang giờ hè, Chủ Nhật đầu tháng 11 về giờ chuẩn) không cùng ngày với châu Âu — trong 1–3 tuần mỗi năm, nếu nguồn dữ liệu/nền tảng chart chưa đồng bộ đúng timezone NY, mốc CBDR/Asian range/Judas Swing bị lệch 1 giờ so với giờ NY thật. **Cách nhận diện sớm:** kiểm tra chênh lệch UTC hiện tại giữa nền tảng trading và giờ NY chính thức mỗi lần Mỹ hoặc khu vực mình đang ở đổi DST; nếu thấy CBDR "đóng" không đúng cảm giác quen thuộc theo phiên (ví dụ NY-AM mở sớm/muộn hơn bình thường), nghi ngay vấn đề timezone. **Hành động đúng:** trong tuần chuyển DST (cả tháng 3 và tháng 11), chủ động verify lại mốc giờ NY thật trên ít nhất 2 nguồn độc lập trước khi tin bảng giờ quen dùng; tạm giảm size hoặc bỏ qua mô hình này nếu chưa chắc chắn múi giờ đã đúng. **Bài học:** không có cơ chế tự động cảnh báo — sai lệch DST thường chỉ phát hiện SAU khi đã đọc nhầm cửa sổ vài lần; đặt nhắc lịch thủ công cho 2 ngày đổi DST mỗi năm.


![[IntradayProf-EdgeCase-CBDR41pip.svg]]
> [!info] Mô tả hình
> Thước đo ngang chia vùng màu: 0–35 pip (xanh "tin cậy cao"), 35–40 pip (xanh nhạt), 40–45 pip (vàng "giảm tin cậy"), >45 pip (đỏ "bỏ qua"). Một điểm đánh dấu tại 41 pip nằm ngay trong vùng vàng, nhãn "41 pip — không phải nhị phân, chỉ giảm độ tin cậy".
### 2. CBDR 41 pip — sát ngưỡng, quyết định thế nào?

**Hiện tượng:** CBDR đo được 41 pip — vượt ngưỡng "< 40 pip" chỉ 1 pip. Áp dụng máy móc quy tắc cứng sẽ loại bỏ hoàn toàn ngày này, nhưng 41 pip về bản chất biến động không khác đáng kể so với 39 pip. **Cách nhận diện sớm:** đây không phải "edge case hiếm" — nó xảy ra thường xuyên vì bất kỳ ngưỡng cứng nào cũng tạo ra các trường hợp biên. **Hành động đúng:** không coi ngưỡng 40 pip là vạch phân định tuyệt đối nhị phân (hợp lệ/không hợp lệ); thay vào đó dùng nó như một **vùng tin cậy giảm dần** — CBDR 35–40 pip: tin cậy cao; 40–45 pip: tin cậy giảm, có thể trade với size nhỏ hơn hoặc đòi thêm xác nhận (MSS mạnh hơn, confluence PD array HTF); >45–50 pip: bỏ qua. **Bài học:** ngưỡng số trong ICT (ở đây và các mô hình khác) nên được đọc như một dải xác suất liên tục, không phải công tắc bật/tắt — sát ngưỡng không có nghĩa là "chắc chắn không hợp lệ", nhưng cũng không nên bị bỏ qua hoàn toàn việc giảm độ tin cậy.

### 3. Judas Swing vượt quá 3 SD rồi vẫn đảo chiều

**Hiện tượng:** protraction vượt xa vùng 3 SD kỳ vọng — theo quy tắc gốc, đây được coi là dấu hiệu "không còn là Judas Swing hợp lệ, có thể là breakout thật". Nhưng sau đó giá vẫn MSS đảo chiều đúng bias như một Judas Swing bình thường, chỉ là protraction sâu hơn dự kiến. **Cách nhận diện sớm:** không thể biết trước liệu vượt 3 SD sẽ dẫn tới đảo chiều muộn hay tiếp tục chạy một chiều — đây là điểm không chắc chắn cố hữu, không phải lỗi phân tích. **Hành động đúng:** khi protraction đã vượt 3 SD, hạ chuẩn xác nhận: đòi MSS RÕ RÀNG hơn (displacement mạnh, CLV cao) mới vào, thay vì vào ngay khi thấy dấu hiệu đảo nhẹ; đồng thời chấp nhận rằng target có thể cần thu hẹp lại (giá đã "dùng" nhiều biến động ngày hơn dự tính vào phase Judas Swing). **Bài học:** vùng 2–3 SD là ngưỡng thực dụng để đánh giá xác suất, không phải giới hạn cứng của thị trường — thị trường không "biết" về giới hạn 3 SD và có thể vượt qua nó bất kỳ lúc nào.

### 4. Ngày có tin lúc 2h sáng NY (tin châu Âu) làm nhiễu Judas Swing

![[IntradayProf-EdgeCase-EuroNews.svg]]
> [!info] Mô tả hình
> Timeline 0h–2h NY với một biểu tượng "tin châu Âu" (ví dụ CPI Đức/Eurozone PMI) đặt gần mốc 2h, giá biến động 2 chiều dữ dội đúng lúc đó; nhãn "Protraction do tin, không do cấu trúc CBDR/Asian".

**Hiện tượng:** 2h sáng NY tương ứng khoảng 7–8h sáng giờ London/châu Âu — đúng giờ nhiều số liệu kinh tế châu Âu (PMI, CPI sơ bộ, số liệu Đức/Eurozone) được công bố. Một protraction xảy ra ngay lúc này có thể là phản ứng tin tức thuần túy, không phải Judas Swing theo cấu trúc CBDR/Asian range. **Cách nhận diện sớm:** kiểm tra lịch tin châu Âu trước khi vào phiên — nếu có số liệu quan trọng rơi vào khung 1h45–2h15 NY, coi bất kỳ protraction quanh mốc đó là khả năng cao do tin. **Hành động đúng:** không trade MSS xảy ra trong 10–15 phút quanh giờ tin châu Âu dù hình dạng giống Judas Swing hợp lệ; chờ biến động ổn định, đánh giá lại cấu trúc từ dữ liệu sau tin. **Bài học:** cửa sổ 0h–2h NY không "sạch" như giả định ban đầu — nó trùng giờ mở cửa kinh tế châu Âu, nên luôn cần chéo kiểm lịch tin đa khu vực (Mỹ VÀ châu Âu), không chỉ tin Mỹ.

### 5. Tuần FOMC làm nhiễu toàn bộ chuỗi profile

**Hiện tượng:** trong tuần có FOMC (thường là thứ Tư), cả CBDR, Asian range và Judas Swing của ngày FOMC (và thường cả ngày trước/sau) đều bị nhiễu bởi tâm lý chờ đợi/phản ứng chính sách tiền tệ — range co hẹp bất thường trước tin (chờ đợi) hoặc giãn rộng bất thường sau tin (phản ứng). **Cách nhận diện sớm:** biết trước lịch FOMC (họp 8 lần/năm, thường công bố 14h NY) — nếu CBDR của ngày đang xét rơi đúng hoặc ngay sau khung giờ FOMC, coi số liệu CBDR ngày đó là không đáng tin cho mô hình. **Hành động đúng:** loại hẳn ngày FOMC (và thường cả ngày kế tiếp nếu biến động dư chấn còn lớn) ra khỏi mẫu backtest/live trading theo mô hình Intraday Profiles; không cố "áp" quy tắc CBDR/SD cho tuần này. **Bài học:** không phải mọi tuần đều có đủ điều kiện "bình thường" để mô hình hoạt động đúng thiết kế — biết loại trừ chủ động là một phần của kỹ năng, không phải là bỏ lỡ cơ hội.

### 6. CBDR/Asian range hẹp bất thường do holiday thanh khoản mỏng

**Hiện tượng:** vào các tuần lễ nghỉ (Giáng sinh, Năm mới, July 4th của Mỹ), CBDR và Asian range có thể hẹp hơn ngưỡng "chuẩn" rất nhiều — không phải vì nén thanh khoản kiểu IPDA, mà đơn giản vì thanh khoản tổng thể quá mỏng, không có đủ volume để tạo biến động dù nhỏ. **Cách nhận diện sớm:** kiểm tra lịch holiday thị trường chính (Mỹ, Anh, EU) trước khi tin một CBDR "đẹp, hẹp" là tín hiệu tốt. **Hành động đúng:** giảm size hoặc bỏ qua hoàn toàn các ngày trong tuần lễ holiday — CBDR hẹp do thanh khoản mỏng không mang cùng ý nghĩa với CBDR hẹp do nén thật trong điều kiện thanh khoản bình thường; protraction sau đó (nếu có) cũng dễ là spike bất thường vì thiếu đối ứng, không phải Judas Swing có cấu trúc. **Bài học:** "hẹp" không tự động đồng nghĩa "chất lượng" — cần phân biệt hẹp do nén thanh khoản bình thường với hẹp do vắng thanh khoản hoàn toàn.

### 7. Asian range lấn sang tối thứ Sáu/sáng thứ Hai (gap cuối tuần)

**Hiện tượng:** với các cặp FX, phiên giao dịch mở lại tối Chủ Nhật (giờ Á) sau khi đóng cuối tuần — Asian range của "ngày thứ Hai" có thể bắt đầu ngay sau một gap giá cuối tuần, khiến range này không phản ánh đúng hành vi nén thanh khoản thông thường mà phản ánh phần lớn là điều chỉnh gap. **Cách nhận diện sớm:** nếu giá mở phiên Á thứ Hai lệch đáng kể so với giá đóng phiên thứ Sáu, Asian range đo được trong vài giờ đầu chủ yếu là "điều chỉnh gap", không phải hành vi nén bình thường. **Hành động đúng:** với ngày thứ Hai có gap mở đáng kể, cân nhắc bỏ qua mô hình Intraday Profiles cho riêng ngày đó hoặc chỉ áp dụng sau khi gap đã được "hấp thụ" (giá ổn định lại, không còn drift một chiều do gap). **Bài học:** không phải mọi Asian range đều cùng một "chất" — Asian range ngay sau gap cuối tuần cần được đối xử khác Asian range giữa tuần bình thường.

### 8. Nhầm lẫn giữa Delayed Protraction thật và ngày range toàn bộ (không hề có protraction nào)

**Hiện tượng:** một số ngày, giá không hề protract ra khỏi CBDR/Asian range cả trước và sau 2h — toàn bộ phiên London/NY-AM chỉ đi ngang trong một range hẹp hơn hoặc tương đương CBDR. Đây KHÔNG phải Delayed Protraction (vì Delayed vẫn giả định SẼ có một protraction, chỉ là muộn hơn) — đây là ngày mô hình không áp dụng được. **Cách nhận diện sớm:** đặt một mốc giờ cắt hợp lý (ví dụ 6h–7h NY, khi London session đã diễn ra phần lớn) — nếu tới lúc đó vẫn chưa có protraction rõ ràng nào, khả năng cao đây là ngày range, không phải Delayed đang chờ. **Hành động đúng:** dừng tìm setup theo mô hình Intraday Profiles sau mốc giờ cắt nếu chưa thấy protraction nào; chuyển sang tư duy range-trading thông thường ([[12 - Consolidation Trading Strategy]]) nếu range đủ rõ để áp dụng khung đó. **Bài học:** "Delayed" không có nghĩa là "cứ chờ thêm mãi" — cần một giới hạn thời gian hợp lý để phân loại ngày này thành "không có profile" thay vì tiếp tục coi là Delayed vô thời hạn.

---

## Chuyên sâu B — Kinh nghiệm live/backtest thực chiến

### 1. Slippage/spread thực tế tại đúng thời điểm entry
Cửa sổ Judas Swing (0h–2h NY) trùng với thời điểm thanh khoản liên ngân hàng chuyển giao giữa phiên Á và London — nhiều broker retail có spread giãn rõ rệt trong giai đoạn này (đặc biệt 0h–1h NY), khiến limit order đặt sát đỉnh/đáy protraction dự kiến dễ không khớp đúng giá hoặc khớp với slippage 2–4 pip trên FX major. MSS trigger trên M5/M1 thường xảy ra sau giai đoạn spread giãn mạnh nhất (gần 1h–2h), nên độ trễ thực thi ít nghiêm trọng hơn so với chính lúc protraction đỉnh/đáy.

### 2. Khác biệt demo vs live vs funded account
- **Demo:** dễ có cảm giác mô hình "rất chuẩn" vì fill lý tưởng đúng SD projection.
- **Live cá nhân:** SD projection là mốc tham khảo, giá hiếm khi chạm ĐÚNG 2.000 SD — cần luyện quen với việc protraction dừng ở 1.7 SD hay 2.4 SD, không phải luôn đúng số tròn.
- **Funded account:** vì mô hình đòi qua nhiều giờ chờ đợi (14h hôm trước tới 2h–6h hôm sau), một số nền tảng funded giới hạn giờ trade hoặc có quy tắc daily loss reset theo giờ server khác giờ NY — cần verify quy tắc drawdown tính theo giờ nào trước khi áp mô hình xuyên đêm này.

### 3. Tâm lý sau 2–3 loss liên tiếp đúng model
Vì mô hình phụ thuộc nhiều yếu tố nối tiếp (CBDR hẹp → Asian range hẹp → Judas đúng giờ/SD → MSS đúng), một chuỗi loss có thể xuất phát từ các khâu khác nhau mỗi lần (không phải luôn cùng một lỗi) — dễ gây cảm giác "mô hình không nhất quán". Thực tế cần tách log theo TỪNG khâu (CBDR đạt chuẩn? Asian đạt chuẩn? Judas đúng giờ? SD trong ngưỡng? MSS rõ?) để biết loss đến từ khâu nào lặp lại nhất, thay vì gộp chung "mô hình sai".

### 4. Journaling missing_step
Các `missing_step` đặc thù cho mô hình này: `cbdr_too_wide` (CBDR vượt ngưỡng nhưng vẫn trade), `asian_range_mismatch` (Asian range không đồng nhất mức nén với CBDR), `wrong_profile_label` (gọi nhầm Normal thành Delayed hoặc ngược lại), `dst_timezone_error` (sai lệch giờ do DST chưa cập nhật), `news_contamination` (protraction trùng giờ tin Mỹ hoặc châu Âu). Review theo tháng để biết khâu nào gây lỗi thường xuyên nhất.

### 5. Kỳ vọng tần suất setup A+ thực tế
Vì cần CẢ 3 mốc (CBDR hẹp, Asian range hẹp, Judas đúng SD) cùng đạt chuẩn, tần suất một ngày đạt đủ điều kiện London Normal "sạch" thấp hơn nhiều mô hình chỉ đòi 1–2 điều kiện. Kỳ vọng thực dụng: **1–3 setup A+ mỗi tuần** trên một cặp FX major theo dõi thường xuyên, thấp hơn hẳn Consolidation Trading hay Bread and Butter. Điều này có nghĩa nếu theo dõi nhiều cặp/nhiều thị trường song song (FX + gold + index), tần suất tổng hợp có thể cao hơn đáng kể.

### 6. Khi nào được phép tăng size
Chỉ sau khi tách riêng kết quả theo TỪNG profile (Normal-Sell, Normal-Buy, Delayed-Sell, Delayed-Buy) với ≥30 mẫu mỗi loại, vì bốn profile có đặc tính rủi ro khác nhau rõ rệt (Normal tin cậy hơn Delayed theo cả lý thuyết và Edge case 8). Không nên gộp chung cả bốn để tính một winrate duy nhất rồi quyết định size — cách này che mất sự khác biệt thật giữa các profile.

---

## Chuyên sâu C — Case studies mổ xẻ chuyên sâu (kịch bản minh họa)

> [!warning] Ghi chú tính xác thực
> Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa — KHÔNG gắn với ngày giao dịch cụ thể có thể kiểm chứng sai. Nếu có nhắc sự kiện thật (FOMC/CPI/NFP generic), chỉ mô tả đặc điểm phổ biến đã biết, không phải số liệu của một lần công bố cụ thể.

### Case 1 — WIN: London Normal Buy Profile, đủ điều kiện, MSS sạch

![[IntradayProf-CaseStudy-Win.svg]]
> [!info] Mô tả hình
> Timeline NY: 14h–20h CBDR hẹp (24 pip) → 20h–0h Asian range hẹp (16 pip, nằm trong CBDR) → 0h20 giá dip xuống chạm vùng 2 SD dưới (mũi tên cam "Judas Swing — Buy") → M5 MSS lên ngay sau (đường tím đứt, để lại FVG discount) → entry BUY tại FVG 0h35 → target lên premium PD array H1, đóng lệnh +2.4R lúc 3h10.

**Bối cảnh HTF:** D1 bullish rõ, giá đang ở discount của dealing range tuần. **Diễn biến:** CBDR 14h–20h đo 24 pip (dưới 40, sạch, không tin lớn giữa phiên). Asian range 20h–0h đo 16 pip, nằm gọn trong CBDR — xác nhận mức nén tốt. 0h20 NY, giá dip xuống chạm đúng vùng 2 SD dưới CBDR — Judas Swing đúng giờ (Normal). M5 xuất hiện MSS lên với displacement rõ ràng (CLV cao), để lại FVG discount sạch. **Quyết định:** BUY tại retest FVG 0h35, stop dưới London-session low (buffer nhỏ), target = premium PD array H1 gần nhất. **Kết quả:** giá chạm target lúc 3h10, đóng lệnh +2.4R. **Mổ xẻ:** đúng toàn bộ chuỗi — CBDR hẹp, Asian range đồng nhất, Judas đúng giờ và đúng vùng SD (không quá sát, không vượt 3 SD), MSS có displacement rõ, entry không chase. **Bài học → rule:** khi cả 3 mốc (CBDR, Asian range, Judas SD) đều đạt chuẩn đồng thời, đây là setup ưu tiên full size theo risk chuẩn.

### Case 2 — LOSS: Nhầm Delayed Protraction với ngày one-way

![[IntradayProf-CaseStudy-Loss.svg]]
> [!info] Mô tả hình
> Timeline: CBDR + Asian range đạt chuẩn → 0h–2h không có protraction rõ → sau 2h giá bắt đầu trôi nhẹ lên (không phải rally mạnh) → trader vào SELL vì nghĩ là "Delayed Protraction" → giá tiếp tục tăng xuyên suốt sáng, không hề đảo, đường giá đi ngược, nhãn "-1.3R".

**Bối cảnh HTF:** D1 bearish nhẹ (không mạnh). **Diễn biến:** CBDR 30 pip, Asian range 22 pip — cả hai đạt chuẩn. 0h–2h không có protraction rõ ràng nào (giá đi ngang sát CBDR). Sau 2h, giá bắt đầu trôi lên nhẹ, chậm, không có đặc điểm "rally dứt khoát" của một Judas Swing thật — nhưng trader vẫn gọi đây là "London Delayed Sell Profile" vì "đã quá 2h rồi, chắc đang vào protraction". **Quyết định (sai):** SELL ngay khi giá vượt nhẹ qua CBDR sau 2h, không chờ MSS xác nhận rõ ràng, vì tin rằng "đây đúng là Delayed". **Kết quả:** giá tiếp tục trôi lên suốt cả sáng theo một xu hướng chậm nhưng bền, không hề có MSS đảo chiều — dừng lỗ ở -1.3R sau khi giá vượt xa mức stop trên dealing-range high. **Mổ xẻ:** lỗi cốt lõi là nhầm lẫn giữa "Delayed Protraction thật" (Edge case 8, phân biệt) và một ngày trôi một chiều chậm không có cấu trúc Judas Swing rõ — trader đã gán nhãn "Delayed" cho bất kỳ điều gì xảy ra sau 2h, thay vì đòi protraction phải có đặc điểm rõ ràng (đủ nhanh, đủ dứt khoát) TRƯỚC khi gọi tên profile. **Bài học → rule:** Delayed Protraction vẫn cần một cú đẩy có đặc điểm nhận diện được (không chỉ "trôi chậm sau 2h") VÀ đòi MSS xác nhận đầy đủ như Normal — không hạ chuẩn xác nhận chỉ vì đã "quá giờ chờ đợi".

### Case 3 — NO-TRADE đúng: CBDR quá rộng do dư chấn FOMC hôm trước

**Bối cảnh HTF:** D1 bullish, nhưng hôm trước là ngày FOMC. **Diễn biến:** CBDR (14h–20h NY) của ngày sau FOMC đo được 58 pip — vượt xa ngưỡng chuẩn hóa kỳ vọng cho cặp tiền này (thường quanh 25–35 pip theo ATR gần đây), do dư chấn biến động từ phản ứng chính sách tiền tệ hôm trước còn kéo dài sang phiên London Close/NY PM. **Quyết định:** không áp mô hình Intraday Profiles cho ngày này — CBDR không phản ánh mức nén thanh khoản bình thường mà phản ánh dư chấn tin tức, khiến SD projection từ đó không có cơ sở tin cậy. **Kết quả:** đứng ngoài; giá sau đó thực sự có một protraction lớn trong 0h–2h nhưng biên độ SD dựa trên CBDR méo khiến nếu có trade theo đúng công thức máy móc, target/stop sẽ bị đặt sai tỷ lệ hoàn toàn so với biến động còn lại của ngày. **Mổ xẻ:** đây là quyết định ĐÚNG — nhận diện đúng nguyên nhân CBDR rộng (dư chấn FOMC, không phải biến động tự nhiên) và từ chối áp mô hình dù bias HTF vẫn hợp lý. **Bài học → rule:** luôn kiểm tra lịch tin lớn của NGÀY TRƯỚC khi đo CBDR — dư chấn tin từ hôm trước có thể làm hỏng toàn bộ chuỗi số liệu của ngày đang xét, dù bản thân ngày đang xét không có tin gì.

---

### Case 4 — MISS: Gán nhầm Delayed thành Normal, bỏ lỡ MSS thật

![[IntradayProf-CaseStudy-Miss.svg]]
> [!info] Mô tả hình
> Timeline 0h–4h NY: không có protraction rõ trong 0h–2h (vùng xám nhạt “không có gì”), nhưng ngay sau 2h30 giá mới thực sự protract mạnh (mũi tên cam) và MSS đảo chiều đúng hướng ngay sau đó — nhãn “Đây là Delayed thật, không phải one-way” và dấu hỏi đỏ tại vùng entry bị bỏ lỡ.

**Bối cảnh HTF:** D1 bearish rõ. **Diễn biến:** CBDR + Asian range đều đủ hẹp, nhưng 0h–2h NY không có rally rõ ràng — trader kết luận vội vàng đây là “ngày không có Judas Swing, bỏ qua luôn” thay vì tiếp tục theo dõi khả năng Delayed Protraction sau 2h. **Quyết định (sai do dừng theo dõi sớm):** tắt chart, không đặt cảnh báo giá cho khung 2h–4h. **Kết quả:** lúc 2h35 NY, giá mới thực sự rally mạnh (Delayed Protraction) rồi MSS xuống đúng bias, chạy +2.8R mà không có lệnh nào được vào. **Mổ xẻ:** đây là lỗi quy trình — “không có protraction trong 0h–2h” không đồng nghĩa “không có Judas Swing hôm nay”, mà là điều kiện để chuyển sang theo dõi Delayed Protraction (xem mục 1, bảng 4 profile). **Bài học → rule:** không thấy protraction trong 0h–2h không phải tín hiệu để dừng theo dõi — đó là tín hiệu để chuyển chế độ quan sát sang Delayed, giữ cảnh báo giá tới hết phiên London thay vì tắt chart sớm.

---

## Best Practices

> [!summary] Tư duy cốt lõi
> Intraday Profiles thưởng cho việc **đo đạc kỷ luật từng mốc giờ TRƯỚC khi diễn giải**, và phạt nặng việc gán nhãn profile theo cảm tính hoặc theo mong muốn kết quả. Phần lớn edge nằm ở việc từ chối các ngày CBDR/Asian range không đạt chuẩn, không nằm ở việc cố "thấy" Judas Swing ở mọi ngày.

### 1. Quy trình đo đạc tuần tự — không bỏ bước
- [ ] Đo CBDR đúng lúc đóng 20:00 NY, ghi số liệu (không ước lượng bằng mắt).
- [ ] Vẽ SD projection ngay sau khi có số CBDR chính xác.
- [ ] Đo Asian range đúng lúc đóng 0:00 NY, so sánh với CBDR.
- [ ] Kiểm tra lịch tin Mỹ VÀ châu Âu cho cửa sổ 0h–2h trước khi diễn giải bất kỳ protraction nào.

### 2. Chuẩn hóa ngưỡng theo ATR trước khi bắt đầu chu kỳ đánh giá
- [ ] Tính ATR(H1) trung bình 20 ngày gần nhất cho thị trường đang trade.
- [ ] Đặt ngưỡng CBDR/Asian range theo tỷ lệ % của ATR đó, không dùng nguyên "40 pip"/"20–30 pip" nếu thị trường/giai đoạn hiện tại khác biệt rõ so với lúc số liệu gốc được đưa ra.
- [ ] Giữ ngưỡng cố định suốt một chu kỳ đánh giá (ví dụ 3 tháng) trước khi cân nhắc điều chỉnh lại.

### 3. Kỷ luật phân loại Normal vs Delayed
- [ ] Đặt mốc giờ cắt rõ ràng (ví dụ 6h NY) để chuyển từ "đang chờ Delayed" sang "không có profile hôm nay".
- [ ] Không gọi tên "Delayed" cho bất kỳ chuyển động nào sau 2h — đòi có đặc điểm protraction rõ ràng (đủ dứt khoát) trước khi gán nhãn.
- [ ] Ghi log riêng loại profile mỗi lệnh để review winrate tách biệt theo 4 nhóm.

### 4. Amateur habits vs Professional habits

| Tình huống | Thói quen nghiệp dư | Thói quen chuyên nghiệp |
|---|---|---|
| Đo CBDR | Ước lượng bằng mắt, không ghi số cụ thể | Đo chính xác lúc 20:00 NY, ghi log số liệu |
| CBDR hơi rộng (sát ngưỡng) | Bỏ qua ngưỡng, trade như bình thường | Coi là vùng tin cậy giảm, giảm size hoặc đòi thêm xác nhận |
| Không có protraction 0h–2h | Ngồi đợi mãi, gọi bất kỳ chuyển động nhỏ là "Delayed" | Đặt mốc giờ cắt, chỉ gọi Delayed khi có protraction rõ đặc điểm sau 2h |
| Ngày FOMC/tin lớn hôm trước | Vẫn áp máy móc công thức CBDR | Loại ngày đó khỏi mẫu, không tin số liệu CBDR bị dư chấn |
| DST vừa đổi | Dùng nguyên bảng giờ cũ | Verify lại giờ NY thật trên ≥2 nguồn trong tuần chuyển DST |
| Backtest 4 profile | Gộp chung tính 1 winrate | Tách riêng từng profile, so sánh độ tin cậy Normal vs Delayed |

---

## Chuyên sâu D — So sánh với Consolidation Trading (khi nào chọn cái nào)

> [!tip] Vì sao cần mục này
> CBDR + Asian range về hình thức cũng là một dạng "consolidation" — dễ nhầm với [[12 - Consolidation Trading Strategy]] nếu không phân biệt rõ.

| Tiêu chí | Intraday Profiles (file này) | Consolidation Trading |
|---|---|---|
| Định nghĩa range | Theo mốc GIỜ CỐ ĐỊNH (14h–20h, 20h–0h) | Theo CẤU TRÚC GIÁ (≥2 điểm chạm mỗi phía, bất kỳ giờ nào) |
| Ngưỡng hợp lệ | Số liệu cụ thể (pip/ATR) cho từng mốc giờ | Không có ngưỡng số cố định, chỉ cần range rõ |
| Sweep kỳ vọng | Judas Swing đúng hướng ngược bias trong 0h–2h (hoặc sau, nếu Delayed) | Sweep mép ngược bias, không ràng buộc giờ cụ thể |
| Điểm entry | Sau MSS, tại premium/discount PD array | Sau MSS, tại retest FVG/CE/mép range |
| Rủi ro đặc thù | DST, tin châu Âu 2h sáng, FOMC làm nhiễu cả chuỗi 3 mốc | Megaphone, range trong range, sweep trùng giờ tin |

**Nguyên tắc chọn nhanh:** nếu bạn đang theo dõi đúng 3 mốc giờ NY cố định (CBDR/Asian/Judas) → dùng file này. Nếu bạn tự vẽ một range bất kỳ trên chart không gắn với 3 mốc giờ đó → dùng [[12 - Consolidation Trading Strategy]].

---

## 9. Checklist trước khi giao dịch

### A. Đo đạc (CBDR + Asian range)
- [ ] CBDR đo đúng lúc 20:00 NY, ghi số liệu cụ thể.
- [ ] CBDR đạt ngưỡng hẹp đã chuẩn hóa theo ATR cho thị trường đang trade.
- [ ] Asian range đo đúng lúc 0:00 NY, đồng nhất mức nén với CBDR.
- [ ] Đã kiểm tra lịch tin Mỹ + châu Âu cho cửa sổ 0h–2h.
- [ ] Đã kiểm tra không phải tuần FOMC hoặc ngay sau FOMC.
- [ ] Đã verify timezone đúng nếu đang trong tuần chuyển DST.

### B. Judas Swing & phân loại profile
- [ ] Protraction đúng hướng ngược bias.
- [ ] Đã phân loại đúng Normal (0h–2h) hay Delayed (sau 2h, có đặc điểm protraction rõ).
- [ ] Protraction trong vùng 1–3 SD (nếu vượt 3 SD, đòi MSS mạnh hơn để xác nhận).

### C. Execution
- [ ] MSS M5/M1 xác nhận đảo chiều đúng bias.
- [ ] Entry tại retest premium/discount PD array, không chase đỉnh/đáy protraction.
- [ ] Stop trên/dưới London-session high/low (Normal) hoặc dealing-range high/low (Delayed).
- [ ] R:R ≥1:1.5 tới target HTF.

### D. Sau giao dịch (ghi log)
- [ ] Ghi lại độ rộng CBDR/Asian range thời điểm thật (không đo lại sau khi biết kết quả).
- [ ] Ghi lại profile_type đã gán trước entry, không sửa lại sau khi thấy kết quả.
- [ ] Ghi số SD thực tế giá đảo — dùng cho thống kê phân phối SD cá nhân theo thời gian.
- [ ] Đánh dấu riêng các ngày có tin (Judas window hoặc tuần FOMC) để loại khỏi thống kê winrate "chuẩn".

---

## 10. Lỗi thường gặp

1. **Bỏ qua kiểm tra độ rộng CBDR/Asian range.** Trade như bình thường dù CBDR vượt xa ngưỡng — làm hỏng cơ sở của toàn bộ SD projection sau đó.
2. **Pre-position trước khi Judas Swing xảy ra.** Vào lệnh sớm dựa trên dự đoán, bị mắc kẹt sai hướng khi protraction thật sự diễn ra.
3. **Nhầm Normal với Delayed.** Gọi tên sai loại profile khiến chọn sai mốc stop (London-session high/low vs dealing-range high/low).
4. **Không chờ MSS.** Vào ngay khi thấy protraction chạm vùng SD, chưa có xác nhận đảo chiều LTF.
5. **Stop quá sát.** Đặt đúng tại London-session high/low không buffer, dễ bị quét lại lần hai.
6. **Bỏ qua ảnh hưởng tin châu Âu.** Chỉ kiểm tra lịch tin Mỹ, quên rằng 0h–2h NY trùng giờ mở cửa châu Âu.
7. **Áp máy móc ngưỡng pip cố định mọi thị trường/giai đoạn.** Không chuẩn hóa lại theo ATR khi volatility đã thay đổi so với lúc số liệu gốc phổ biến.
8. **Gộp chung cả 4 profile khi tính winrate.** Che mất sự khác biệt tin cậy thật giữa Normal và Delayed.

---

## 11. Câu hỏi tự kiểm tra

1. Vì sao CBDR và Asian range đều phải hẹp — thiếu một trong hai thì hệ quả gì?
2. "Standard deviation" của CBDR khác gì với độ lệch chuẩn thống kê thật?
3. Phân biệt London Normal và London Delayed Protraction dựa trên tiêu chí nào?
4. Vì sao Delayed Protraction dễ bị nhầm với ngày one-way — cách giảm thiểu nhầm lẫn này là gì?
5. CBDR 41 pip nên được xử lý thế nào — loại bỏ hoàn toàn hay đánh giá theo thang độ tin cậy?
6. Vì sao cửa sổ 0h–2h NY cần kiểm tra CẢ lịch tin Mỹ và châu Âu?
7. Tuần FOMC ảnh hưởng thế nào tới toàn bộ chuỗi CBDR–Asian range–Judas Swing?
8. Vì sao ngưỡng pip cố định (40, 20–30) cần được chuẩn hóa lại theo ATR thay vì dùng nguyên trạng?
9. Khác biệt giữa Intraday Profiles (file này) và Consolidation Trading tổng quát ở điểm nào?
10. Vì sao ngày sau FOMC cần bị loại khỏi mẫu backtest, dù chính ngày đang xét không có tin gì?

---

## 12. Flashcards / Active Recall

> [!question]- Ba mốc giờ cốt lõi của Intraday Profiles là gì?
> CBDR (14h–20h NY), Asian range (20h–0h NY), Judas Swing window (0h–2h NY).

> [!question]- Ngưỡng gốc cho CBDR và Asian range là bao nhiêu?
> CBDR < 40 pip, Asian range 20–30 pip — nhưng đây là số cũ cần chuẩn hóa lại theo ATR hiện tại (xem Phản biện #1).

> [!question]- "SD" trong SD projection của CBDR có phải độ lệch chuẩn thống kê thật không?
> Không — đây là thuật ngữ quy ước (misnomer): chỉ là 1/2/3 lần độ rộng CBDR chiếu lên/xuống, không phải giá trị tính từ phân phối xác suất thống kê.

> [!question]- Khác biệt giữa London Normal và London Delayed Protraction?
> Normal: Judas Swing xảy ra đúng trong cửa sổ 0h–2h NY. Delayed: không có protraction rõ trong 0h–2h, IPDA vào protraction sau 2h — dùng dealing-range high/low thay London-session high/low cho stop.

> [!question]- Vì sao Delayed Protraction "khó hơn" Normal về mặt nhận diện?
> Vì Delayed dễ bị nhầm với một ngày chạy một chiều (one-way) không hề có Judas Swing/không đảo chiều — sự khác biệt chỉ lộ ra sau khi có hoặc không có MSS đảo chiều, không thể biết trước chắc chắn.

> [!question]- Intraday Profiles khác Consolidation Trading tổng quát ở điểm nào?
> Intraday Profiles định nghĩa range theo MỐC GIỜ CỐ ĐỊNH (CBDR 14h–20h, Asian 20h–0h) và có ngưỡng số cụ thể (pip/SD); Consolidation Trading định nghĩa range theo CẤU TRÚC GIÁ (≥ 2 điểm chạm mỗi phía) không ràng buộc giờ cố định.

> [!question]- Vì sao cần loại ngày sau FOMC khỏi mẫu backtest, dù chính ngày đó không có tin?
> Vì dư chấn biến động từ phản ứng chính sách tiền tệ hôm trước có thể kéo dài sang CBDR của ngày kế tiếp, làm CBDR không phản ánh mức nén thanh khoản bình thường.

> [!question]- Vì sao cửa sổ 0h–2h NY cần kiểm tra cả lịch tin châu Âu?
> Vì 0h–2h NY tương ứng khoảng 7h–8h sáng giờ London/châu Âu — đúng giờ nhiều số liệu kinh tế châu Âu công bố, có thể tạo protraction giả do tin, không do cấu trúc CBDR/Asian range.

> [!question]- CBDR 41 pip (sát ngưỡng 40) nên xử lý thế nào thay vì loại bỏ tuyệt đối?
> Không coi 40 là công tắc bật/tắt nhị phân — dùng như vùng tin cậy giảm dần: gần ngưỡng thì giảm size hoặc đòi thêm xác nhận MSS mạnh hơn, chỉ loại hẳn khi vượt xa ngưỡng — vì sai số đo đạc khiến ranh giới chính xác tuyệt đối là phi thực tế.

> [!question]- Judas Swing vượt quá 3 SD rồi vẫn đảo chiều đúng hướng — điều này nói lên gì về SD projection?
> Nói lên rằng SD projection chỉ là vùng xác suất tham khảo, không phải giới hạn cứng — giá vẫn có thể protract xa hơn dự kiến rồi mới đảo, đòi hỏi trader kiên nhẫn chờ MSS thật thay vì entry sớm chỉ vì đã "đủ SD".

---

## 13. Liên kết với Trade Journal

### Trường dữ liệu nên ghi cho mỗi lệnh Intraday Profile
- `bias_htf`: bullish / bearish / neutral.
- `cbdr_pips`: độ rộng CBDR đo được (số tuyệt đối).
- `cbdr_atr_ratio`: tỷ lệ CBDR/ATR(H1) — dùng để chuẩn hóa thay ngưỡng pip cố định.
- `asian_range_pips`: độ rộng Asian range.
- `profile_type`: normal-sell / delayed-sell / normal-buy / delayed-buy.
- `sd_reached`: số SD thực tế đã đạt được tại điểm protraction cực đại.
- `news_window`: có/không — cửa sổ Judas Swing có trùng tin Mỹ hoặc châu Âu không.
- `dst_week`: có/không — có rơi vào tuần chuyển DST không.
- `missing_step`: cbdr_too_wide / asian_range_mismatch / wrong_profile_label / dst_timezone_error / news_contamination / khong_co.
- `r_result`: kết quả R thực tế.

### Gợi ý review theo tháng
- [ ] Winrate tách riêng theo `profile_type` — Normal có thật sự đáng tin hơn Delayed không theo dữ liệu của chính mình?
- [ ] Phân phối `sd_reached` — phần lớn setup thắng dừng ở vùng SD nào?
- [ ] Tỷ lệ `missing_step = khong_co` trên tổng số ngày đủ điều kiện đo đạc.
- [ ] So sánh winrate ngày `dst_week = có` với ngày bình thường — nếu lệch đáng kể, xem lại quy trình verify timezone trước khi trade tuần chuyển DST.

---

## Nguồn

- [ICT Intraday Profiles (Daily Profiles) — London Protraction Model](https://innercircletrader.net/tutorials/ict-intraday-profiles/) — bài nguồn chính cho toàn bộ mục 1–7, common mistakes, FAQ.
- Xem thêm trong bộ: [[12 - Consolidation Trading Strategy]] (khung range tổng quát, so sánh chi tiết ở Chuyên sâu D), [[01 - ICT 2022 Model]] (chuỗi sweep→displacement→FVG dùng chung cho bước MSS/entry), [[05 - Friday Profit Taking]] (một dạng thiên hướng theo thời gian khác, liên hệ với vấn đề ngưỡng số cố định lỗi thời).
- Ghi chú phương pháp: các ngưỡng pip/SD trong bài được giữ nguyên từ nguồn gốc để tham chiếu lịch sử, nhưng khuyến nghị chuẩn hóa theo ATR hiện tại trước khi áp dụng live (xem Phản biện #1).

> [!tip] Nhắc lại nhanh: CBDR/Asian range là bước đo lường mở đầu, Judas Swing là bước xác nhận hướng — thiếu một trong hai, mô hình Intraday Profiles không còn đủ cơ sở để vào lệnh.
