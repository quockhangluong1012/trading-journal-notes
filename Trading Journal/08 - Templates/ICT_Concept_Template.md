---
type: ict-concept
concept: "{{title}}"
aliases: []
tags:
  - trading/ict/concept
  - trading/study
status: seed # seed | developing | tested | mastered
category: "" # Liquidity | Market Structure | PD Array | Entry Model | 
last_reviewed: 
created: {{date}}
updated: {{date}}
---

# {{title}}

> [!summary] Tóm tắt 1 câu
> Viết lại khái niệm này bằng **ngôn ngữ của mình** trong 1 câu ngắn gọn.

---

## 1. Định nghĩa

**Khái niệm:**  

**Mục đích trong ICT:**  

**Vì sao khái niệm này quan trọng:**  

**Nó giúp trả lời câu hỏi nào trên chart?**
- Giá đang ở đâu trong narrative?
- Giá vừa lấy thanh khoản hay chưa?
- Giá có đang phản ứng ở POI hợp lệ không?
- Có đủ điều kiện để xuống LTF tìm entry không?

---

## 2. Bối cảnh sử dụng

### Khi nào khái niệm này có giá trị cao?
- [ ] Có Daily Bias rõ ràng
- [ ] Giá đang ở Premium/Discount phù hợp
- [ ] Giá nằm trong hoặc phản ứng tại POI HTF
- [ ] Có liquidity pool rõ ràng
- [ ] Có thời điểm giao dịch phù hợp: London / New York Kill Zone
- [ ] Có displacement / MSS / FVG xác nhận trên LTF

### Khi nào nên bỏ qua?
- [ ] Giá đang ở giữa range, không rõ Premium/Discount
- [ ] Không có liquidity target rõ ràng
- [ ] Không có HTF narrative
- [ ] Tín hiệu xuất hiện ngoài kill zone
- [ ] Chỉ thấy mô hình nhỏ lẻ nhưng không nằm trong POI

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. 
2. 
3. 

### Điều kiện bắt buộc
- [ ] 
- [ ] 
- [ ] 

### Điều kiện tăng xác suất
- [ ] Có liquidity sweep trước đó
- [ ] Có displacement mạnh
- [ ] Có FVG/Imbalance rõ ràng
- [ ] Có MSS/BOS đúng ngữ cảnh
- [ ] Entry nằm trong vùng Premium/Discount hợp lý
- [ ] Target là external/internal liquidity rõ ràng

### Điều kiện làm setup yếu đi
- 
- 
- 

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Bias & Narrative
- Bias hiện tại: 
- Giá đang trong dealing range nào? 
- Giá đang ở Premium hay Discount? 
- Liquidity target gần nhất: 
- POI HTF quan trọng: 

### H1 / M15 — POI & Context
- POI đang quan sát: 
- Lý do POI hợp lệ: 
- Giá đã sweep liquidity chưa? 
- Giá có phản ứng rõ không? 

### M5 / M1 — Confirmation & Entry
- Có MSS không? 
- MSS có nằm trong POI không? 
- Có displacement không? 
- Có FVG/OB entry model không? 
- Entry có hợp lệ theo checklist không? 

---

## 5. Quy tắc xác nhận / vô hiệu hóa

### Setup được xem là hợp lệ khi
- [ ] 
- [ ] 
- [ ] 

### Setup bị vô hiệu khi
- [ ] Giá phá hẳn POI mà không phản ứng
- [ ] MSS xảy ra nhưng không nằm trong POI
- [ ] Không có displacement rõ ràng
- [ ] Liquidity sweep chưa xảy ra nhưng đã cố vào lệnh
- [ ] Entry ngược Daily Bias mà không có lý do mạnh

---

## 6. Ví dụ chart

### Ví dụ đúng
![[paste-image-here.png]]

**Mô tả:**  

**Vì sao đây là ví dụ tốt:**
- 
- 
- 

### Ví dụ sai / dễ nhầm
![[paste-image-here.png]]

**Mô tả lỗi:**  

**Bài học:**
- 
- 
- 
---

## 7. Checklist trước khi áp dụng vào trade

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Khái niệm ICT chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**.

- [ ] Daily Bias rõ ràng
- [ ] Xác định đúng dealing range
- [ ] Giá ở Premium/Discount phù hợp với hướng trade
- [ ] Có HTF POI rõ ràng
- [ ] Giá đã sweep liquidity trước khi đảo chiều
- [ ] Có MSS trên LTF
- [ ] MSS xảy ra trong POI, không phải giữa range
- [ ] Có displacement tạo FVG/Imbalance
- [ ] Entry có stop loss logic
- [ ] Target là liquidity rõ ràng
- [ ] Risk/reward tối thiểu đạt kế hoạch
- [ ] Không trade vì revenge / FOMO / muốn gỡ lệnh thua

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Vào lệnh trước liquidity sweep | Giá chưa lấy đỉnh/đáy rõ ràng đã vào | Chờ sweep + đóng nến quay lại range |
| MSS không nằm trong POI | Thấy displacement ở giữa range | Chỉ xét MSS khi giá đã chạm HTF POI |
| Xác định sai dealing range | Chọn swing quá nhỏ hoặc quá cũ | Ưu tiên swing tạo displacement/BOS rõ |
| Nhầm pullback với đảo chiều | Giá chỉ hồi nhẹ rồi tiếp tục trend | Cần sweep + MSS + displacement |
| Trade ngược bias | LTF đẹp nhưng HTF không ủng hộ | Ưu tiên HTF narrative trước |

---

## 10. Câu hỏi tự kiểm tra

- Mình có thể giải thích khái niệm này trong 30 giây không?
- Khái niệm này dùng để xác định **bias**, **POI**, **entry**, hay **target**?
- Nó cần xuất hiện ở khung thời gian nào để có giá trị?
- Điều gì làm tín hiệu này bị invalid?
- Setup nào trong trade journal của mình đã áp dụng đúng/sai khái niệm này?

---

## 11. Flashcards / Active Recall

### Q1
**Hỏi:** Khái niệm này dùng để làm gì?  
**Đáp:** 

### Q2
**Hỏi:** Điều kiện hợp lệ quan trọng nhất là gì?  
**Đáp:** 

### Q3
**Hỏi:** Lỗi phổ biến nhất khi dùng khái niệm này là gì?  
**Đáp:** 

---

## 12. Lesson Learned

### Bài học chính
- 
- 
- 

### Quy tắc cá nhân rút ra
- [ ] 
- [ ] 
- [ ] 

### Câu nhắc nhở khi trade
> 

---
