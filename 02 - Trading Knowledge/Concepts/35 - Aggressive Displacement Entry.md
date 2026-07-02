---
type: ict-concept
concept: Aggressive Displacement Entry
aliases:
  - Aggressive Displacement
  - Shallow Retrace Entry
  - Entry Refinement on Strong Displacement
tags:
  - trading/ict/concept
  - trading/study
  - "#AggressiveDisplacement"
status: developing
category: Entry Model
timeframes:
  - M5
  - M1
models:
  - "[[Trading Journal/02 - Trading Knowledge/Models/ICT 2022 Model|ICT 2022]]"
markets:
  - NDX
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 4
confidence: 2
last_reviewed: 2026-06-29
created: 2026-06-29
updated: 2026-06-29
related_concepts:
  - "[[13 - FVG  - Fair Value Gap]]"
  - "[[10 - Consequent Encroachment (Mean Threshold)]]"
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[17 - Inverse Fair Value Gap - iFVG]]"
  - "[[26 - OTE - Optimal Trade Entry]]"
  - "[[32 - Top-down Analysis (Multiple Timeframes)]]"
prerequisites:
  - "[[21 - Market Structure Shift]]"
  - "[[20 - Liquidity Sweep]]"
  - "[[13 - FVG  - Fair Value Gap]]"
common_mistakes: []
---

# Aggressive Displacement Entry

> [!summary] Tóm tắt 1 câu
> Khi giá quét liquidity → tạo MSS → **displacement rất mạnh**, giá thường KHÔNG retrace sâu về FVG đầu tiên/to nhất; entry thật nằm **cao hơn và phải refine ở khung nhỏ hơn (CE, M1 FVG/OB)** — displacement càng mạnh thì retrace càng nông.

> [!important] Nguyên tắc cốt lõi
> Displacement mạnh = institutional sponsorship lớn = smart money KHÔNG cho giá rẻ lại. Đây là **efficient delivery**, không phải lỗi của mình. Phản xạ chờ fill sâu vào FVG thấp/to là lý do bỏ lỡ lệnh. Vùng entry hợp lý nằm cao hơn mình nghĩ: **CE của FVG**, hoặc một **FVG/OB nhỏ hơn ở M1** trong leg retrace nông.

---

## 1. Định nghĩa

**Khái niệm:**
Aggressive Displacement Entry là cách tìm điểm vào lệnh khi sau chuỗi **liquidity sweep → MSS → displacement**, cú đẩy giá có lực bất thường (body lớn liên tiếp, ít/không có pullback) và giá **chỉ retrace rất nông** rồi tiếp tục đi về phía draw on liquidity — thay vì quay lại lấp đầy FVG đầu tiên mà trader đánh dấu.

**Mục đích trong ICT:**
- Giải quyết tình huống "FVG không được chạm" — một trong những lý do bỏ lỡ lệnh phổ biến nhất sau khi đọc đúng narrative.
- Chuyển từ tư duy "chờ fill sâu" sang tư duy "**refine entry ở khung nhỏ hơn + dùng CE**".
- Giữ kỷ luật R:R: entry nông hợp lý vẫn tốt hơn chase ở giá xấu.

**Vì sao khái niệm này quan trọng:**
Đọc đúng bias, đúng sweep, đúng MSS — nhưng vẫn lỗ cơ hội vì đặt limit ở FVG quá thấp. Bản thân việc giá không retrace sâu là **một tín hiệu** (move hiệu quả, có sponsorship), không phải tín hiệu nên bỏ. Hiểu điều này giúp định vị entry đúng nơi smart money thực sự cho phép vào.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Vì sao FVG mình đánh dấu không được giá quay về?
- Trong move mạnh, vùng retrace tối đa thực tế là tới đâu?
- Nên hạ khung nào để tìm entry refine?
- Nếu đã lỡ lệnh thì chờ cấu trúc tiếp theo ở đâu, thay vì đuổi giá?

### Aggressive Displacement Entry không phải là gì
- Không phải lý do để **chase** entry market ngay tại đỉnh leg.
- Không phải phủ định FVG — mà là chọn **FVG/PD array đúng vị trí** (cao hơn, nhỏ hơn).
- Không phải bỏ stop logic — stop vẫn dưới swing/điểm sweep gần nhất.
- Không phải mọi displacement đều "aggressive" — chỉ áp dụng khi lực đẩy thật sự mạnh và retrace nông.

---

## 2. Bối cảnh sử dụng

### Khi nào khái niệm này có giá trị cao?
- [ ] Đã có **SSL/BSL sweep + MSS** đúng sequence, cùng Daily Bias.
- [ ] Displacement leg gồm nhiều nến body lớn liên tiếp, **ít pullback nội bộ**.
- [ ] Giá retrace **rất nông** (không chạm FVG to/thấp nhất) rồi tiếp tục đi tiếp.
- [ ] Vẫn còn draw on liquidity rõ ràng phía trước → còn room cho R:R.
- [ ] Đang trong kill zone / cửa sổ có edge.

### Khi nào nên bỏ qua?
- [ ] Displacement yếu / nến chồng lấp nhiều → đây là move bình thường, cứ chờ FVG fill như thường.
- [ ] Giá đã chạy gần hết tới target, room còn lại quá ít.
- [ ] Không xác định được FVG/OB nào ở M1 để refine → entry trở thành đoán.
- [ ] Sweep/MSS chưa rõ ràng — đừng dùng concept này để hợp lý hóa việc chase.

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Displacement mạnh bất thường:** chuỗi body lớn, momentum dốc, gap/imbalance liên tiếp.
2. **Retrace nông:** pullback không chạm FVG đầu tiên (thường là FVG to/thấp nhất), thường dừng ở mép trên hoặc CE của một FVG cao hơn.
3. **Tiếp tục mở rộng:** sau retrace nông, giá đi tiếp về phía draw on liquidity, để lại FVG mới ở khung nhỏ.

### Điều kiện bắt buộc
- [ ] Có sweep + MSS hợp lệ trước displacement (xem [[21 - Market Structure Shift]], [[20 - Liquidity Sweep]]).
- [ ] Displacement có chất lượng "aggressive" (body close mạnh, urgency, ít hồi).
- [ ] Xác định được một PD array hợp lệ ở vị trí retrace nông (CE của FVG M5, hoặc FVG/OB M1).

### Điều kiện tăng xác suất
- [ ] M1 cho thấy một micro sweep + micro MSS ngay tại vùng retrace nông (cùng câu chuyện, phóng to).
- [ ] Vùng entry trùng với **CE (50%)** của FVG M5 — xem [[10 - Consequent Encroachment (Mean Threshold)]].
- [ ] Còn external liquidity rõ ràng phía trước cho R:R tốt.

### Điều kiện làm setup yếu đi
- Displacement thực ra yếu (nến nhỏ, chồng lấp) → không phải tình huống aggressive.
- Không có FVG/OB nào ở M1 để bấu víu → entry thiếu logic.
- Giá đã đi quá xa, retrace nông vẫn cho R:R kém.

---

## 4. Quy trình phân tích đa khung thời gian

> [!example] Quy trình refine khi displacement quá mạnh
> 1. **Move này có thực sự aggressive không?** (body lớn liên tiếp, retrace nông)
> 2. **CE của FVG M5 ở đâu?** — đặt đó làm vùng entry kỳ vọng thay vì đáy FVG.
> 3. **Hạ M1 tại leg retrace** — có FVG/OB nhỏ hơn nằm cao hơn không?
> 4. **Còn room tới draw on liquidity không?** Nếu không → bỏ.

### D1 / H4 — Bias & Narrative
- Xác nhận Daily Bias và draw on liquidity (move mạnh thường đang chạy về một external pool HTF).
- Move aggressive thường đồng pha với HTF bias — đó là lý do nó mạnh.

### H1 / M15 — POI & Context
- Đánh dấu FVG/OB M5 sinh ra từ displacement leg.
- Tính sẵn **CE (mức 50%)** của FVG đó — đây là vùng retrace tối đa kỳ vọng trong move mạnh.

### M5 / M1 — Confirmation & Entry
- **Hạ M1** ngay tại leg retrace nông: tìm FVG hoặc Order Block nhỏ hơn, nằm **cao hơn** so với FVG M5 to.
- Lý tưởng: M1 tạo một micro sweep + micro MSS tại vùng đó → xác nhận entry.
- Đặt limit tại **CE của FVG M5** hoặc tại M1 FVG/OB; stop dưới swing/điểm sweep gần nhất.
- Nếu giá không chạm CE → move quá mạnh, **không đuổi**, chờ leg tiếp theo.

```text
Mẫu ghi nhanh — Aggressive Displacement (Long)
Bias: Bullish | Draw on liquidity: BSL [level]
Sweep SSL [đáy] → MSS phá lower-high → displacement mạnh
FVG M5 (to/thấp): [zone]  → CE (50%): [level]  ← vùng entry kỳ vọng
Retrace nông dừng tại: [level] (chưa chạm đáy FVG M5)
M1 refine: FVG/OB tại [zone cao hơn] + micro MSS xác nhận
Entry: CE FVG M5 / M1 FVG  | Stop: dưới swing gần nhất | Target: BSL [level]
No-trade: displacement yếu / hết room / không có M1 PD array
```

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Entry được xem là hợp lệ khi
- [ ] Có sweep + MSS + displacement aggressive đúng sequence.
- [ ] Entry đặt tại **CE FVG M5** hoặc **M1 FVG/OB** nằm trong leg retrace nông.
- [ ] Có stop logic (dưới swing/điểm sweep) và còn room tới target.

### Setup bị vô hiệu khi
- [ ] Giá đóng acceptance ngược lại qua MSS level → failed shift, không phải retrace.
- [ ] Displacement hóa ra yếu / giá lấp đầy ngược trở lại sâu hơn cả FVG M5.
- [ ] Không có PD array M1 nào để vào → đứng ngoài thay vì đoán.

---

## 6. Ví dụ chart

### Ví dụ đúng — SSL sweep → MSS → displacement mạnh, retrace nông
![[paste-image-here.png]]

**Mô tả:**
Giá quét SSL (đáy, blue line), tạo MSS phá lower-high bằng displacement rất mạnh. FVG M5 to/thấp được đánh dấu nhưng giá **không quay về** — chỉ retrace nông tới CE của một FVG cao hơn rồi tiếp tục mở rộng lên. Entry hợp lý là CE FVG M5 / M1 FVG, không phải đáy FVG to.

**Vì sao đây là ví dụ tốt:**
- Move hiệu quả có sponsorship → retrace nông là điều dự kiến được.
- Entry refine ở M1/CE cho stop chặt và R:R tốt hơn chờ fill sâu.
- Không chase tại đỉnh leg.

### Ví dụ sai / dễ nhầm — chờ fill sâu vào FVG to nhất
![[paste-image-here.png]]

**Mô tả lỗi:**
Đặt limit ở đáy FVG to/thấp nhất ngay sau MSS. Giá chỉ retrace nông rồi đi tiếp → limit không bao giờ được khớp → bỏ lỡ một move đúng narrative. Sau đó FOMO chase ở giá xấu.

**Bài học:**
- FVG to/thấp = entry "an toàn" về cảm giác nhưng thường không được chạm trong move mạnh.
- Displacement càng mạnh → entry càng phải cao hơn và refine khung nhỏ hơn.

---

## 7. Entry model liên quan

Khái niệm này thường kết hợp với:
- [[20 - Liquidity Sweep]]
- [[21 - Market Structure Shift]]
- [[13 - FVG  - Fair Value Gap]]
- [[10 - Consequent Encroachment (Mean Threshold)]]
- [[17 - Inverse Fair Value Gap - iFVG]]
- [[25 - OB - Order Block]]
- [[26 - OTE - Optimal Trade Entry]]

### Sequence mẫu
```text
HTF Bias → Sweep (SSL/BSL) → MSS → Displacement MẠNH
→ Retrace NÔNG (không chạm FVG to)
→ Refine: CE của FVG M5  HOẶC  hạ M1 tìm FVG/OB + micro MSS
→ Entry tại CE / M1 PD array → Stop dưới swing → Target: draw on liquidity
→ Nếu không chạm CE: KHÔNG đuổi, chờ leg tiếp theo
```

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy displacement mạnh
> Aggressive Displacement Entry chỉ hợp lệ trong đúng context sweep + MSS + còn room. Đừng dùng nó để biện minh cho việc chase.

- [ ] Daily Bias rõ ràng, displacement cùng hướng bias.
- [ ] Đã có sweep + MSS hợp lệ trước displacement.
- [ ] Displacement thật sự aggressive (body lớn liên tiếp, retrace nông).
- [ ] Đã tính CE của FVG M5 và đặt đó làm vùng entry kỳ vọng.
- [ ] Đã hạ M1 tìm FVG/OB refine; lý tưởng có micro MSS xác nhận.
- [ ] Entry có stop logic; còn liquidity target rõ ràng cho R:R đủ.
- [ ] Nếu giá không chạm CE → chấp nhận bỏ lệnh, không FOMO.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Chờ fill sâu vào FVG to/thấp | Limit ở đáy FVG không bao giờ khớp | Dùng CE (50%) làm vùng entry, hoặc M1 FVG cao hơn |
| Đánh dấu sai FVG | Chọn FVG to/thấp thay vì FVG ngay tại nến MSS | Ưu tiên FVG hình thành ngay tại displacement/MSS candle |
| Chase sau khi lỡ | FOMO vào market ở đỉnh leg | Không đuổi; chờ leg tiếp theo (sweep nội bộ + FVG M1 mới) |
| Không hạ khung | Chỉ nhìn M5 cho một move quá mạnh | Drop M1 để phóng to leg retrace, tìm entry refine |
| Bỏ qua failed shift | Coi mọi pullback là retrace để mua | Acceptance ngược MSS level = invalidation, không vào |

---

## 10. Câu hỏi tự kiểm tra

- Move này thật sự aggressive (body lớn, retrace nông) hay chỉ là displacement bình thường?
- CE của FVG M5 nằm ở đâu, và giá có khả năng chạm tới đó không?
- Trên M1, có FVG/OB nào nằm cao hơn để refine entry không?
- Còn đủ room tới draw on liquidity để R:R đạt kế hoạch không?
- Nếu giá không chạm CE, tôi có kỷ luật đứng ngoài thay vì chase không?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Vì sao trong displacement mạnh, FVG to/thấp thường không được giá quay về?
**Đáp:** Vì có institutional sponsorship lớn — smart money không cho giá rẻ lại (efficient delivery). Retrace nông là tín hiệu của move mạnh, không phải lỗi.

### Q2
**Hỏi:** Entry refine nên tìm ở đâu khi retrace quá nông?
**Đáp:** Tại CE (50%) của FVG M5, hoặc hạ M1 tìm FVG/OB nhỏ hơn nằm cao hơn, lý tưởng có micro sweep + micro MSS xác nhận.

### Q3
**Hỏi:** Lỗi phổ biến nhất với tình huống này là gì?
**Đáp:** Đặt limit ở đáy FVG to/thấp → không được chạm → bỏ lỡ → FOMO chase ở giá xấu.

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
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

---

## 13. Lesson Learned

### Bài học chính
- Displacement càng mạnh → retrace càng nông → entry càng phải **cao hơn và refine ở khung nhỏ hơn**.
- FVG to/thấp = entry "an toàn" nhưng thường không được chạm.
- Thà entry nông tại CE + xác nhận M1 còn hơn chờ fill sâu không bao giờ tới.

### Quy tắc cá nhân rút ra
- [ ] Tôi tính CE của FVG M5 trước, dùng nó làm vùng entry kỳ vọng thay vì đáy FVG.
- [ ] Khi move quá mạnh, tôi hạ M1 tìm FVG/OB refine, không bám FVG M5 to.
- [ ] Nếu giá không chạm vùng entry hợp lý, tôi đứng ngoài, không chase.

### Câu nhắc nhở khi trade
> **"Displacement mạnh không cho giá rẻ. Entry nằm cao hơn mình nghĩ — refine, đừng chờ fill sâu, đừng chase."**

---

## 14. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Phân biệt được move aggressive vs displacement thường? |
| Nhận diện trên chart |  | Có nhận ra retrace nông sớm và tính CE không? |
| Biết khi nào bỏ qua |  | Có đứng ngoài khi hết room / không có M1 PD array không? |
| Kết hợp với context HTF |  | Move có luôn đồng pha draw on liquidity HTF không? |
| Áp dụng vào trade thực tế |  | Entry thực sự ở CE/M1, không chase đỉnh leg? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập các setup displacement mạnh, gắn tag `[[Aggressive Displacement Entry]]`.
- [ ] So sánh win rate giữa entry "CE/M1 refine" vs "chờ fill FVG to".
- [ ] Thống kê tỉ lệ FVG to/thấp được chạm trong các move mạnh để định lượng rule.
