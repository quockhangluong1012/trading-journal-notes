---
type: goal
horizon: Short
category: Process
status: In Progress
priority: High
progress: 0
metric: Số khuyết tật đo lường còn tồn tại (dashboard sai path, R bịa, lệnh trùng, link hỏng, goal sai phase)
baseline: "6 khuyết tật: 6 dashboard sai path · 4 dashboard bịa ±1R · 3 cặp lệnh trùng · 3437 link hỏng · 2 goal sai phase · CLAUDE.md sai vị trí Reviews"
target: 0 khuyết tật — mọi số trên dashboard là phép đo, không phải suy đoán
phase: Phase 0 - Data Integrity
start_date: 2026-09-07
due_date: 2026-10-22
tags:
  - goal
  - data-integrity
---

# Sửa hệ đo — dữ liệu đáng tin trước khi đặt gate

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Process / Data integrity
> - **Vì sao quan trọng:** Mọi gate của GĐ1–GĐ6 đều đọc số từ dashboard và frontmatter. Nếu số sai thì gate vô nghĩa — tệ hơn là gate sai sẽ cho phép chuyển giai đoạn khi chưa đủ điều kiện, hoặc chặn khi đã đủ.
> - **Điều kiện thành công:** Mọi con số hiển thị đều truy được về một phép đo thật.

> [!warning] Vì sao đây là Giai đoạn 0 chứ không phải việc phụ
> Weekly review W27 và W28 đã nêu đúng các lỗi này. W29 nêu lại **nguyên văn**. Không lỗi nào được sửa. Pattern "chẩn đoán xuất sắc, khắc phục gần bằng không" chính là thứ giai đoạn này tồn tại để phá.

## Định nghĩa hoàn thành
- [ ] Không dashboard nào render rỗng
- [ ] Không con số R nào được bịa ra
- [ ] Không lệnh nào bị đếm hai lần
- [ ] Không link hỏng tới concept/mistake note
- [ ] Mọi goal khớp phase trong [[01 - Roadmap]]

## Cách đo lường
- **Chỉ số:** Số khuyết tật còn lại
- **Hiện tại:** xem Cột mốc bên dưới
- **Mục tiêu:** 0
- **Tần suất review:** Hàng tuần cho tới khi xong

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [x] Sửa đường dẫn dataview ở 6 dashboard (bỏ tiền tố `Trading Journal/`)
- [x] Bỏ bịa ±1R — `rValue()` trả `null`, thêm ô đếm "lệnh thiếu R"
- [x] Gỡ 3 cặp lệnh live trùng (28 → 25 lệnh), giữ lại cả dữ liệu đo lẫn narrative
- [x] Đưa file audit NQ1 bị xếp nhầm ra khỏi `04 - Backtesting` (đếm backtest = 22)
- [x] Sửa 3.087 wikilink hỏng trên toàn vault
- [x] Khôi phục 8 file bị xoá nhầm (3 debate + 5 BO-SUNG)
- [x] Sửa `phase:`/`horizon:`/`progress:` cho 8 goal note
- [x] Sửa CLAUDE.md (vị trí Reviews + quy ước đặt tên đã đổi)
- [ ] Chốt một bản live journal duy nhất (còn 2 bản song song đã trôi lệch)
- [ ] Tạo `30-Sell-side-Liquidity` (đếm lại 2026-09-07: **138 wikilink trong 22 file** trỏ tới `[[30 - Sell-side Liquidity]]` + 3 link `[[Sell-side Liquidity]]`, note đích không tồn tại — con số 38 ghi ban đầu là thiếu). Gồm 2 phần: tạo note + đổi link sang basename gạch nối theo quy ước [[CLAUDE]].
- [ ] Điền `r_multiple` cho 10 lệnh live còn thiếu, hoặc đánh dấu là không đo được

## Nhật ký tiến độ
| Ngày | Tiến độ % | Ghi chú |
|---|---:|---|
| 2026-09-07 | 73 | 8/11 cột mốc xong trong một phiên. Còn: chốt bản live journal, tạo note slot 30, xử lý 10 lệnh thiếu R. |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Phương pháp: [[04 - Phương pháp luyện tập, vòng lặp AI & giữ động lực]]
