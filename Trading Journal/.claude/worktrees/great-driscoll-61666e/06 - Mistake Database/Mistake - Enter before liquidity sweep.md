---
type: mistake
category: execution
severity: high
related_model: ICT 2022
frequency: 4
status: active
---

# Mistake - Enter before liquidity sweep

## Mô tả lỗi

- Tôi vào lệnh khi thấy giá chạm OB/FVG và xuất hiện tín hiệu rejection
- Đuổi theo giá do sợ bỏ lỡ lệnh
- Vào lệnh khi giá chưa quét thanh khoản rõ ràng

## Biểu hiện

- Thấy giá phản ứng là vào sớm
- Chưa có displacement thật sự
- FVG quá nhỏ hoặc không clean
- Entry nằm ngay trong vùng nhiễu

## Tại sao lỗi này nguy hiểm?

- Dễ bị giá quét SL trước khi đi đúng hướng
- Không có confirmation từ smart money
- RR nhìn đẹp nhưng xác suất thấp

## Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-17 EURUSD Long]]
- 

## Rule phòng tránh

- Không vào lệnh nếu chưa có sweep liquidity + displacement.
- Nếu chỉ có phản ứng tại OB nhưng chưa có MSS/shift, chỉ quan sát.
- Entry phải nằm sau confirmation, không phải dự đoán phản ứng.