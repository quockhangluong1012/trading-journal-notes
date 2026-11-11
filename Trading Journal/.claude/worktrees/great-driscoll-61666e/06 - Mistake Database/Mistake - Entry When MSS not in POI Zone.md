---
type: mistake
category: execution
severity: high
related_model: "[[03 - Playbooks/3.2 - Setups/ICT 2022 Model|ICT 2022 Model]]"
frequency: 1
status: active
---

# Mistake - Entry When MSS not in POI Zone

## Mô tả lỗi

- Tôi vào lệnh khi thấy giá đã quét thanh khoản + displacement (giá di chuyển mạnh ngược chiều) + kèm tạo ra FVG
- Tuy nhiên điều quan trọng là gái phản ứng ( Sweep + MSS) không trong vùng POI hợp lệ

## Biểu hiện

- Thấy giá phản ứng là vào sớm (điều kiện entry của mô hình ICT 2022)
- Giá không nằm trong vùng POI hợp lệ

## Tại sao lỗi này nguy hiểm?
- Giá tạo ra mô hình entry để dẫn dụ trader vào lệnh sớm sau đó quét stop loss
- Không có POI hợp lệ (Quét giữa khoảng không)
- RR nhìn đẹp nhưng xác suất thấp

## Ví dụ đã xảy ra

- [[Loss - 01 - Trade 2026-06-18 NDX Short]]

## Rule phòng tránh
- Xác định các vùng POI quan trọng trước khi tìm điểm vào lệnh
- Không vào lệnh nếu chưa có sweep liquidity + displacement.
- Khi giá tới vùng POI nếu không có MSS, không trade
- Entry phải nằm sau confirmation, không phải dự đoán phản ứng.