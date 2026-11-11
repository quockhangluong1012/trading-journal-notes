---
type: mistake
category: execution
severity: high
related_model: ICT 2022
frequency: 4
status: active
---

# Mistake - Emotional revenge trade

## Mô tả lỗi

Tôi vào lệnh khi thấy giá chạm OB/FVG nhưng chưa có sweep liquidity rõ ràng.

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

- [[Trade 2026-06-18 - XAUUSD Long Loss]]
- [[Trade 2026-06-15 - EURUSD Short Loss]]

## Rule phòng tránh

- Không vào lệnh nếu chưa có sweep liquidity + displacement.
- Nếu chỉ có phản ứng tại OB nhưng chưa có MSS/shift, chỉ quan sát.
- Entry phải nằm sau confirmation, không phải dự đoán phản ứng.