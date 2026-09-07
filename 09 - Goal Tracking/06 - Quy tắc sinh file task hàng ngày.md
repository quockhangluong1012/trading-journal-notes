---
type: spec
dashboard: Automation
created: 2026-09-07
updated: 2026-09-07
tags:
  - spec
  - automation
  - routine
---

# 🤖 Quy tắc sinh file task hàng ngày

> [!info] File này là hợp đồng giữa vault và routine "daily tasks"
> Routine chạy **04:00 giờ VN mỗi ngày** (cloud agent, quản lý ở `claude.ai/code/routines`), clone repo, đọc file này, rồi sinh `00 - Inbox/01 - Daily Tasks/YYYY-MM-DD tasks.md` và commit vào `master`.
>
> **Muốn đổi cách sinh task thì sửa FILE NÀY, không sửa prompt của routine.** Prompt cố tình để ngắn và chỉ trỏ về đây.

## 0. Đầu ra & giới hạn cứng

| Hạng mục | Luật |
|---|---|
| Đường dẫn | `00 - Inbox/01 - Daily Tasks/<ngày Asia/Bangkok> tasks.md` |
| Khuôn | `08 - Templates/Daily_Tasks_Template.md` |
| Ngày | **Ngày hiện tại theo Asia/Bangkok (UTC+7)** — `TZ=Asia/Bangkok date +%F`, không dùng ngày UTC |
| File đã tồn tại | **Không ghi đè.** Dừng và báo trong kết quả run |
| Trần độ dài | **120 dòng** |
| Ngôn ngữ | Tiếng Việt |
| Số liệu | **Đếm trực tiếp từ repo.** Không có dữ liệu → ghi "chưa có dữ liệu" |
| Checkbox | **Để trống hết.** Routine không bao giờ tick thay người dùng |

> [!danger] Vì sao có trần 120 dòng
> File task 07/2026 dài 200–300 dòng, mỗi ngày lặp lại toàn bộ lịch sử cảnh báo. Hệ thống sụp sau 18 ngày. **File task phải đọc xong trong 60 giây** — nếu không, nó trở thành việc thứ tư phải làm trong ngày. Chi tiết dài nằm ở [[05 - Nhịp ngày & tuần - Vận hành lộ trình]], không nằm trong file task.

## 1. Bước 1 — đọc trạng thái thật (đếm, không đoán)

Đọc trước 3 file định hướng: [[CLAUDE]] (quy ước vault) · [[01 - Roadmap]] (giai đoạn đang mở + gate) · [[05 - Nhịp ngày & tuần - Vận hành lộ trình]] (§4 menu việc theo giai đoạn, §7 bảng bằng chứng).

Rồi đếm:

| Cần biết | Cách đếm |
|---|---|
| Backtest tổng | Số file có `type: backtest` trong `04 - Backtesting` |
| Mẫu **trong phạm vi** | Trong số đó, `symbol` là NAS100 hoặc EURUSD |
| Mẫu **đếm vào 200** | Trong số trong-phạm-vi, có `r_net` đo thật (mẫu thiếu `r_net` = 0 điểm) |
| Concept | Đếm theo `status`; liệt kê `importance: 5` còn `seed`; tìm `last_reviewed` cũ nhất |
| Goal đang mở | `09 - Goal Tracking/Goals/**` — số cột mốc `[x]`/tổng, ngày dòng "Nhật ký tiến độ" gần nhất |
| Chuỗi | Ngày có file trong `00 - Inbox/02 - Daily Summary`: số ngày log trong 7 ngày qua, số tuần liên tiếp ≥5 ngày |
| Mốc gần nhất | Ngày backtest gần nhất · daily summary gần nhất · lệnh live gần nhất |
| 3 file task gần nhất | Để biết concept nào vừa được lên lịch (dùng cho luật loại trừ ở §2) |

## 2. Bước 2 — chọn nội dung từng khối (theo luật, không tuỳ hứng)

### 🟢 Ngày tối thiểu
Copy nguyên văn 3 mục ở §3 của [[05 - Nhịp ngày & tuần - Vận hành lộ trình]]. Luôn có, mọi ngày.

### 🧠 Retrieval — 1 concept/ngày
Thứ tự ưu tiên: (1) `importance: 5` đang `seed` → (2) `last_reviewed` cũ nhất trong `developing`.
**Loại trừ:** mọi concept xuất hiện ở mục Retrieval của **3 file task gần nhất**, và mọi concept có `last_reviewed` trong **3 ngày** qua.
Kèm **1 câu lý do chọn**, nối vào bước cụ thể của [[2022 Model A+ Setup]] hoặc một lỗi trong `06 - Mistake Database`. Không viết đoạn dài.

### 📊 Sản xuất — đúng 1 việc
Lấy từ **menu §4 của note 05** theo giai đoạn đang mở. Với GĐ0: một cột mốc chưa tick trong [[Sua he do - du lieu dang tin truoc khi dat gate]]. **Không thêm việc ngoài menu** — muốn thêm thì sửa note 05 trước.

### 📊 Replay
1 mẫu (2 nếu `day_type: deep`), chọn symbol đang lệch ít mẫu hơn giữa NAS100/EURUSD. Nhắc đủ: 7 bước · GATE 7 bước của playbook · dòng survivorship.

### 🌙 Đóng vòng
Daily Summary · đẩy số vào goal **chỉ khi số đổi thật** · tự chấm 1–5 · kiểm tra tick trung thực.

### Thêm theo thứ trong tuần
- **Thứ Hai:** khối "Mở tuần" 10' — chọn 3 concept của tuần, symbol focus, `day_type` dự kiến 7 ngày.
- **Chủ Nhật:** khối "Đóng tuần" 45' — weekly review + dán 1 dòng vào [[02 - Skill Metrics]].

## 3. Bước 3 — phần "nói thật": đúng MỘT callout, tối đa 5 gạch đầu dòng

Chỉ nêu điểm rò rỉ **có bằng chứng file**, mỗi mục 1–2 dòng, kèm **số ngày treo**:

- Hôm qua có file task nhưng không có Daily Summary → chuỗi đứt, gọi tên.
- **Overtick:** có `[x]` trong file task hôm qua mà file liên quan không đổi trong ngày đó.
- Goal có cột mốc / dòng log đứng yên **>7 ngày**.
- Dòng [[02 - Skill Metrics]] của tuần trước chưa dán (kiểm từ thứ Hai).
- `r_net` còn trống ở mẫu của tuần này.

> [!warning] Ba điều cấm trong callout này
> 1. **Không viết lại toàn bộ lịch sử** — 07/2026 mỗi ngày kể lại mọi cảnh báo cũ, làm file phình và người đọc chai sạn.
> 2. **Không lặp lại một cảnh báo nhiều ngày liền** nếu không có dữ liệu mới — nêu một lần, kèm số ngày treo.
> 3. **Không suy diễn động cơ** ("lười", "mất động lực"). Chỉ ghi sự kiện + số ngày.

## 4. Bước 4 — commit

- `git add` **đúng file task vừa tạo** → commit message `Add daily tasks for YYYY-MM-DD` → push `master`.
- **Không sửa file nào khác**, trừ khi spec này nói rõ.

## 5. Điều routine KHÔNG được làm

- ❌ Tick checkbox thay người dùng (bằng chứng phải do người tạo ra).
- ❌ Sinh task **live-trade** trước GĐ3 — buổi tối GĐ0–GĐ2 là khối đóng vòng, không phải khối chart.
- ❌ Đề xuất symbol ngoài **NAS100 / EURUSD**.
- ❌ Viết dòng "Nhật ký tiến độ" rỗng vào goal note.
- ❌ Tạo hộ Daily Summary / Weekly review — đó là việc của người, routine chỉ sinh **task**.
- ❌ Sửa `last_reviewed` / `confidence` của concept — đó là bằng chứng học, không phải dữ liệu quản trị.
- ❌ Bịa P&L, R, giá, hay số mẫu. Thiếu thì ghi thiếu.

## Liên kết
- Quy trình ngày/tuần: [[05 - Nhịp ngày & tuần - Vận hành lộ trình]] · Khuôn file: [[Daily_Tasks_Template]]
- Lộ trình: [[01 - Roadmap]] · [[03 - Lộ trình chi tiết - Từ số 0 đến Funded 100K]] · Phương pháp: [[04 - Phương pháp luyện tập, vòng lặp AI & giữ động lực]]
- Playbook chấm setup: [[2022 Model A+ Setup]] · Chỉ số: [[02 - Skill Metrics]]
