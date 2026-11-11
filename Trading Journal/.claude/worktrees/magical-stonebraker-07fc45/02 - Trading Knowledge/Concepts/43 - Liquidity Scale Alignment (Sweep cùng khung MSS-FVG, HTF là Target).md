---
type: ict-concept
concept: Liquidity Scale Alignment
aliases:
  - Liquidity Scale Alignment
  - Sweep cùng khung
  - Timeframe-matched Sweep
  - Target vs Trigger
  - Scale Mismatch
tags:
  - trading/ict/concept
  - trading/study
  - "#LiquidityScaleAlignment"
status: developing
category: Liquidity
timeframes:
  - D1
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NAS100
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 3
last_reviewed: 2026-07-12
created: 2026-07-12
updated: 2026-07-12
prerequisites:
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]"
  - "[[16 - Internal & External Range Liquidity (IRL & ERL)]]"
  - "[[32 - Top-down Analysis (Multiple Timeframes)]]"
common_mistakes:
  - "[[02 - Mistake - Enter before liquidity sweep]]"
  - "[[03 - Mistake - Entry When MSS not in POI Zone]]"
  - "[[06 - Mistake - Not Have Market Structure Shift]]"
---

# Liquidity Scale Alignment (Sweep cùng khung với MSS & FVG)

> [!summary] Tóm tắt 1 câu
> **Cú [[20 - Liquidity Sweep|liquidity sweep]] mà mô hình [[01 - ICT 2022 Model|2022]] yêu cầu phải xảy ra CÙNG KHUNG (cùng scale) với [[21 - Market Structure Shift|MSS]] và [[13 - FVG  - Fair Value Gap|FVG]] tạo entry — thường là một short-term high/low cấp LTF ngay tại POI; còn các bể thanh khoản lớn của HTF (EQH/EQL) là [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|TARGET / draw]], KHÔNG phải điều kiện kích hoạt (TRIGGER) để vào lệnh.**

> [!important] Nguyên tắc cốt lõi
> **Trigger và Target phải khác scale và khác vai trò.**
> - **Trigger** (cho phép bấm lệnh) = sweep + MSS + FVG, tất cả **cùng khung entry** (M5/M1).
> - **Target** (nơi giá hướng tới) = bể liquidity đối ứng của **HTF** (EQH/EQL, old high/low).
>
> Đòi bể HTF phải bị quét thì mới vào = **ép một điều kiện cấp HTF làm trigger cho một tín hiệu cấp LTF** → *lệch khung (timeframe/scale mismatch)* → bỏ lỡ những cú đảo chiều xuất phát ngay từ POI.

---

## 1. Định nghĩa

**Khái niệm:** "Scale alignment" là nguyên tắc khớp **cấp độ (khung thời gian) của cú liquidity sweep** với cấp độ của MSS và FVG trong cùng một entry. Trong chuỗi kinh điển của mô hình 2022 — **Sweep → MSS → FVG → Entry** — cả ba mắt xích diễn ra trên **cùng khung entry**. Nếu bạn vào lệnh trên M5, thì "sweep" cần thiết là một cú quét cấp M5 (một short-term high/low, một cụm equal highs/lows nhỏ *ngay tại POI*), không phải cú quét bể EQH/EQL đồ sộ của H1/H4.

**Mục đích trong ICT:** Phân tách rạch ròi hai vai trò của thanh khoản để không nhầm lẫn:
- **Draw / Target:** lý do giá *di chuyển* và nơi giá *muốn tới* — thuộc về narrative HTF ([[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]]).
- **Trigger:** bằng chứng khách quan rằng order flow *đã đảo tại POI ngay bây giờ* — thuộc về xác nhận LTF.

**Vì sao khái niệm này quan trọng:** Đây là lằn ranh giữa "chờ đúng kỷ luật" và "chờ nhầm điều kiện rồi đứng nhìn lệnh trôi". Rất nhiều setup A+ đảo chiều **từ trong POI** mà **không** chạy lên quét bể HTF gần nhất; nếu lấy cú quét HTF làm điều kiện bắt buộc, bạn sẽ có một bộ lọc *quá chặt* loại bỏ chính những cú thắng sạch nhất.

**Nó giúp trả lời câu hỏi nào trên chart?**
- "Cú sweep cần cho entry này là sweep ở khung nào?"
- "Bể thanh khoản mình đang nhìn là *lý do vào lệnh* hay *nơi để chốt lời*?"
- "Giá đã cho tôi trigger hợp lệ chưa, hay tôi đang chờ một điều kiện không thuộc về entry model này?"

---

## 2. Bối cảnh sử dụng

### Khi nào khái niệm này có giá trị cao?
- [ ] Đang chạy top-down [[32 - Top-down Analysis (Multiple Timeframes)|D1 → H1 → M5]]: HTF cho bias + POI, LTF cho entry.
- [ ] Có một bể EQH/EQL lớn của HTF nằm **phía trên/dưới POI** khiến bạn phân vân "có cần quét nó trước không".
- [ ] POI (OB/FVG) nằm **thấp/cao hơn** bể HTF đó — tức là chờ quét bể HTF sẽ mâu thuẫn với việc vào lệnh từ POI.
- [ ] Giá vừa phản ứng tại POI bằng một cú quét nhỏ + [[21 - Market Structure Shift|MSS]] trên LTF.

### Khi nào nên bỏ qua / cẩn trọng?
- [ ] POI **chính là** bể thanh khoản (khi đó sweep tại POI và sweep bể trùng nhau — xem mục 6, ca Turtle Soup).
- [ ] Chưa có LTF confirmation nào cả (không có sweep + MSS ở bất kỳ khung nào) → chưa có trigger, đứng ngoài.
- [ ] Bể HTF nằm **rất sát** POI (chênh vài pip) → thực tế cùng scale, đừng bắt bẻ.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. Có **hai lớp liquidity khác scale**: một bể lớn cấp HTF (EQH/EQL, old high/low) và một short-term high/low nhỏ cấp LTF ngay tại POI.
2. Giá **phản ứng và đảo chiều từ POI** (tap + reject) mà chưa chạm bể HTF.
3. Cú sweep cấp LTF (wick qua STH/STL tại POI rồi đóng lại) đi kèm **displacement** tạo MSS + FVG — trigger đã đủ.

### Điều kiện bắt buộc (để coi là trigger hợp lệ)
- [ ] Sweep, MSS và FVG **cùng một khung entry**.
- [ ] Sweep là **body-context** hợp lệ: wick lấy thanh khoản rồi **đóng cửa quay lại** (không phải phá hẳn).
- [ ] MSS có **displacement** để lại [[13 - FVG  - Fair Value Gap|FVG]] ([[35 - Aggressive Displacement Entry|displacement]]).
- [ ] POI có lý do đảo chiều ([[27 - Premium Discount|premium/discount]] hợp bias, [[10 - Consequent Encroachment (Mean Threshold)|CE]] đã chạm).

### Điều kiện làm setup yếu đi
- Bể HTF quá gần và quá "béo" ngay trên POI → xác suất giá bị hút lên quét nó trước cao hơn (rủi ro cho lệnh vào sớm — cân nhắc scale-in / chờ thêm).
- LTF sweep quá nông, MSS không có displacement → dễ là noise, không phải trigger thật.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Bias & Narrative
- Xác định bias và **draw on liquidity** (bể HTF là *target*): EQL/SSL dưới (bias giảm) hoặc EQH/BSL trên (bias tăng).
- Ghi rõ: bể HTF này là **nơi giá hướng tới**, không phải điều kiện vào lệnh.

### H1 / M15 — POI & Context
- Khoanh POI ([[25 - OB - Order Block|OB]]/FVG) trong [[27 - Premium Discount|premium/discount]] đúng bias.
- Nhận diện short-term high/low **ngay cạnh POI** — đây mới là bể mà cú entry cần quét.
- Câu hỏi kiểm tra: "POI của mình có phải chính là bể HTF không? Nếu KHÔNG → tuyệt đối không lấy cú quét bể HTF làm trigger."

### M5 / M1 — Confirmation & Entry
- Chờ giá vào POI → soi LTF: **sweep STH/STL tại POI → MSS (displacement) → FVG**.
- **M5 MSS chính là trọng tài**: nó xuất hiện ở đâu thì cú đảo chiều bắt đầu ở đó — bất kể bể HTF đã bị quét hay chưa.
- Entry vào FVG / LTF OB do cây displacement để lại, kèm [[26 - OTE - Optimal Trade Entry|OTE]] nếu có. Target = bể HTF (draw).

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] Sweep + MSS + FVG cùng khung entry, tại POI.
- [ ] POI có confluence ([[27 - Premium Discount|PD]] + [[10 - Consequent Encroachment (Mean Threshold)|CE]] + lý do liquidity cục bộ).
- [ ] Có target HTF rõ ràng để lệnh có nơi đi tới (RR đạt kế hoạch).

### Setup bị vô hiệu / phải đứng ngoài khi
- [ ] Không có cú sweep + MSS ở **bất kỳ** khung nào (chưa có trigger thật).
- [ ] MSS nằm giữa range, không ở POI ([[21 - Market Structure Shift|internal repricing]], không phải đảo chiều).
- [ ] Giá phá hẳn POI mà không phản ứng.
- [ ] Bạn đang **chờ bể HTF bị quét** trong khi entry model của bạn không yêu cầu điều đó → đây là lỗi scale mismatch, không phải kỷ luật.

---

## 6. Ví dụ chart

### Ví dụ đúng (case tham chiếu)
![[EQH-target-vs-trigger-20260712.svg]]

**Mô tả:** Bias D1 giảm. POI = [[25 - OB - Order Block|OB]] H1 premium (1.75360–1.74360). Phía trên OB có một vùng **EQH (4 đỉnh ngang)** — bể BSL lớn cấp H1. Giá retrace lên, **wick qua mép trên OB (quét BSL cục bộ cấp LTF) rồi đóng lại vào OB**, sau đó displacement giảm + M5 MSS. Giá **không** chạm EQH.

**Vì sao đây là ví dụ tốt:**
- Cú sweep cục bộ trên OB + M5 MSS = **trigger đầy đủ, cùng scale** → được phép vào.
- EQH ở trên là **target/draw**, để dành cho tương lai (unfinished business), không phải điều kiện vào.
- Xem chi tiết ca này ở [[2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)]].

### Ví dụ sai / dễ nhầm
**Mô tả lỗi:** Thấy EQH "béo" ở trên OB → tự nhủ "phải quét EQH rồi mới short" → khi giá đảo ngay từ OB mà chưa quét EQH, kết luận "chưa có liquidity sweep" và **không vào**, dù M5 đã cho MSS.

**Bài học:**
- "Chưa có liquidity sweep" là **sai về sự kiện**: cú quét đã xảy ra ở cấp LTF (wick trên OB), chỉ là không ở bể HTF.
- Đòi quét EQH để short *từ dưới* EQH thường **tự mâu thuẫn**: nếu giá thật sự lên quét EQH, OB có thể đã hỏng.
- Đây thuần là lỗi **scale mismatch** → xem [[02 - Mistake - Enter before liquidity sweep]].

---

## 7. Checklist trước khi áp dụng vào trade

> [!warning] Hỏi trước khi chờ một cú sweep
> **"Bể thanh khoản mình đang chờ có CÙNG khung với entry của mình không?"** Nếu không → nó là target, không phải trigger.

- [ ] Xác định entry TF (M5/M1) và giữ nguyên yêu cầu sweep ở đúng khung đó.
- [ ] POI có phải chính là bể liquidity không? (Nếu có → ca Turtle Soup, cần wick qua bể; nếu không → không đòi quét bể HTF.)
- [ ] Đã có sweep cục bộ + MSS + FVG tại POI trên khung entry chưa?
- [ ] Bể HTF được ghi rõ là **TARGET**, đã tính RR tới đó.
- [ ] Không hoãn lệnh chỉ vì một bể HTF chưa bị chạm.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Ép sweep HTF làm trigger | Chờ quét EQH/EQL lớn mới vào, dù POI thấp/cao hơn bể | Chỉ đòi sweep **cùng khung entry** tại POI; bể HTF = target |
| "Chưa có sweep" (sai sự kiện) | Bỏ qua wick quét STH/STL cục bộ ngay tại POI | Coi wick-qua-rồi-đóng-lại tại POI là sweep hợp lệ |
| Short ngay dưới bể BSL | Vào lệnh khi còn draw mạnh phía trên | Nếu bể HTF quá sát/béo → chờ thêm hoặc để giá quét bể trước |
| MSS giữa range | Displacement không ở POI | Chỉ tính MSS khi giá đã ở HTF POI |
| Nhầm target với trigger | Dùng old high/low để "xin phép vào" | Old high/low là nơi chốt lời, không phải điều kiện vào |

---

## 10. Câu hỏi tự kiểm tra

- Cú sweep cần cho entry này ở khung nào? Nó có cùng khung với MSS/FVG không?
- Bể thanh khoản mình đang nhìn là *trigger* hay *target*?
- Nếu bể HTF chưa bị quét nhưng LTF đã MSS tại POI — mình có được vào không? (Có, nếu confluence đủ.)
- Việc mình "chờ" là kỷ luật đúng, hay là đang chờ nhầm một điều kiện không thuộc entry model?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Trong chuỗi Sweep → MSS → FVG của mô hình 2022, cú sweep phải ở khung nào?
**Đáp:** Cùng khung entry với MSS và FVG (thường M5/M1), là một STH/STL cấp LTF tại POI — không phải bể EQH/EQL cấp HTF.

### Q2
**Hỏi:** EQH/EQL lớn của HTF đóng vai trò gì?
**Đáp:** TARGET / draw on liquidity (nơi giá hướng tới, nơi chốt lời), KHÔNG phải trigger để vào lệnh.

### Q3
**Hỏi:** Lỗi phổ biến nhất của khái niệm này là gì?
**Đáp:** Ép điều kiện quét bể HTF làm trigger cho entry LTF → lệch khung → bỏ lỡ cú đảo chiều xuất phát ngay từ POI.

---

## 12. Lesson Learned

### Bài học chính
- Trigger và Target khác scale, khác vai trò — đừng trộn.
- Trọng tài quyết định vào lệnh là **LTF MSS tại POI**, không phải việc bể HTF đã vỡ hay chưa.
- "Chờ" chỉ là kỷ luật khi mình chờ đúng điều kiện của entry model; chờ nhầm điều kiện là một dạng lỗi.

### Quy tắc cá nhân rút ra
- [ ] Trước mỗi setup, ghi rõ đâu là TRIGGER (LTF) và đâu là TARGET (HTF).
- [ ] Không hoãn entry chỉ vì một bể HTF chưa bị chạm.
- [ ] Nếu bể HTF quá sát/béo trên POI → hạ size hoặc scale-in, đừng biến nó thành lý do bỏ lệnh.

### Câu nhắc nhở khi trade
> Sweep cho entry phải **cùng khung** với MSS/FVG. EQH/EQL là nơi mình **đi tới**, không phải nơi xin phép **đi vào**.

---

## Liên kết
- Model: [[01 - ICT 2022 Model]]
- Nền tảng: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]] · [[32 - Top-down Analysis (Multiple Timeframes)]]
- Case liên quan: [[2026-07-12 M15 - Xác định MSS khi retrace OB H1 (nến xanh liên tiếp)]] · [[2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)]]
