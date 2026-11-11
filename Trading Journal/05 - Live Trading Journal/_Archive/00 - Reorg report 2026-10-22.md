---
type: reorg-report
date: 2026-10-22
tags: [vault-maintenance]
---
# Tổ chức lại Live Trading Journal — 2026-10-22

> [!info] Cấu trúc mới
> - `Trades/` — **phẳng**, 27 note lệnh (nguồn chuẩn duy nhất, dashboard đọc từ đây)
> - `attachments/` — **phẳng**, 120 hình (trước nằm ở `Screenschots/YYYY/MM/(DD)`). Không có tên trùng nên mọi `![[...]]` vẫn hoạt động.
> - `_Archive/Date-folder versions/` — 30 note từ các folder `yyyy-mm-dd` cũ, đổi đuôi `(archive yyyy-mm-dd)` để không trùng tên với note trong Trades
> - `_Archive/Duplicate Imports/` — 3 bản import trùng cũ, đuôi `(archive dup import)`
> Không file nào bị xoá — chỉ di chuyển; chỉ xoá các folder rỗng.

## Kết quả kiểm tra trùng lặp (Trades ↔ folder yyyy-mm-dd)

Ghép theo dữ liệu thật (date, entry, PnL, source_id), không chỉ theo tên file. **27 lệnh thật**; folder ngày chứa 31 note cho 26 lệnh; Trades chứa 26 note (thiếu 06-02).

| Lệnh | Bản chuẩn trong `Trades/` | Bản trùng (đã archive) | Ghi chú |
|---|---|---|---|
| 2026-03-25 XAUUSD Long — Loss 01 | Loss - 01 - Trade 2026-03-25 XAUUSD Long | 2026-03-25 (giống hệt) |  |
| 2026-03-30 NQ1 Short — Loss 01 | Loss - 01 - Trade 2026-03-30 NQ1 Short | 2026-03-30 (có DA audit) |  |
| 2026-03-31 NQ1 Long — Win 01 | Win - 01 - Trade 2026-03-31 NQ1 Long | 2026-03-31 (giống hệt) |  |
| 2026-04-01 NQ1 Long — Win 01 | Win - 01 - Trade 2026-04-01 NQ1 Long | 2026-04-01 (có DA audit) |  |
| 2026-04-02 NQ1 Long — Win 01 | Win - 01 - Trade 2026-04-02 NQ1 Long | 2026-04-02 (có DA audit) + 2026-05-02 (bản cũ, nằm SAI folder) | Lệnh 04-02 bị copy nhầm vào folder 2026-05-02 |
| 2026-04-20 NQ1 Long — Win 01 | Win - 01 - Trade 2026-04-20 NQ1 Long | 2026-04-20 (có DA audit) |  |
| 2026-04-23 NDX Long — Win 01 | Win - 01 - Trade 2026-04-23 NDX Long | 2026-04-23 (có DA audit) |  |
| 2026-04-27 NDX Long — Loss 01 | Loss - 01 - Trade 2026-04-27 NDX Long | 2026-04-27 (có DA audit) |  |
| 2026-04-28 NDX Long — Win 01 | Win - 01 - Trade 2026-04-28 NDX Long | 2026-04-28 (có DA audit) |  |
| 2026-04-28 NDX Long — Loss 02 | Loss - 02 - Trade 2026-04-28 NDX Long | 2026-04-28 (có DA audit) |  |
| 2026-04-29 NDX Long — Loss 01 | Loss - 01 - Trade 2026-04-29 NDX Long | 2026-04-29 (có DA audit) |  |
| 2026-05-01 NDX Long — Win 01 | Win - 01 - Trade 2026-05-01 NDX Long | 2026-05-01 (có DA audit) |  |
| 2026-05-04 NDX — Win 01 | Win - 01 - Trade 2026-05-04 NDX | 2026-05-04 (có DA audit, 6 hình vs 5) |  |
| 2026-05-08 EURUSD Short — Win 01 | Win - 01 - Trade 2026-05-08 EURUSD Short | 2026-05-08 (có DA audit) |  |
| 2026-05-13 NDX Long — Loss (entry 29,150) | Loss - 01 - Trade 2026-05-13 NDX Long (bản merged) | Loss-01 + Loss-02 trong 2026-05-13 + 1 bản Duplicate Import | ⚠️ CÙNG 1 lệnh nhưng folder ngày đặt 2 tên Loss-01/Loss-02 → nhìn như 2 lệnh |
| 2026-05-13 NDX Long — Win (entry 29,127.5) | Win - 01 - Trade 2026-05-13 NDX Long (bản merged) | Win-01 + Win-02 trong 2026-05-13 + 1 bản Duplicate Import | ⚠️ CÙNG 1 lệnh, bị nhân đôi tương tự |
| 2026-05-15 NDX Long — Win 01 | Win - 01 - Trade 2026-05-15 NDX Long (bản merged) | 2 bản trong 2026-05-15 (…NDX-Long và …NDX) + 1 bản Duplicate Import | ⚠️ 3 bản thừa cho 1 lệnh |
| 2026-05-21 NDX — Win 01 | Win - 01 - Trade 2026-05-21 NDX | 2026-05-21 (có DA audit) |  |
| 2026-06-02 NDX — Win 01 | Win - 01 - Trade 2026-06-02 NDX ✅ MỚI ĐƯA VÀO | — | ⚠️ Trước đây CHỈ có trong folder ngày → dashboard thiếu lệnh +265 này |
| 2026-06-05 NDX — Loss 01 | Loss - 01 - Trade 2026-06-05 NDX | 2026-06-05 (có DA audit) |  |
| 2026-06-12 NDX Long — Win 01 | Win - 01 - Trade 2026-06-17 NDX Long | 2026-06-12 (giống hệt) + 2026-06-17/Win-01 (có DA audit) | ⚠️ Tên file ghi 06-17 nhưng frontmatter date = 2026-06-12 |
| 2026-06-17 EURUSD Long — Loss 01 | Loss - 01 - Trade 2026-06-17 EURUSD Long | 2026-06-17 (có DA audit) | ⚠️ frontmatter date = 2026-06-18 |
| 2026-06-17 GBPUSD Long — Loss 02 | Loss - 02 - Trade 2026-06-17 GBPUSD Long | 2026-06-17 (có DA audit) | ⚠️ frontmatter date = 2026-06-18 |
| 2026-06-17 EURUSD Long — Loss 03 | Loss - 03 - Trade 2026-06-17 EURUSD Long | 2026-06-17 (có DA audit) | ⚠️ frontmatter date = 2026-06-18 |
| 2026-06-17 NDX Long — Loss 04 | Loss - 04 - Trade 2026-06-17 NDX Long | 2026-06-17 (có DA audit) |  |
| 2026-06-18 NDX Short — Loss 01 | Loss - 01 - Trade 2026-06-18 NDX Short | 2026-06-18 (có DA audit) |  |
| 2026-10-12 NDX Long — Loss 01 | Loss - 01 - Trade 2026-10-12 NDX Long | — | Chỉ có trong Trades |

> [!warning] Khác biệt nội dung cần biết
> - ~24 bản trong folder ngày là bản **đã thêm phần Devil's Advocate audit** (frontmatter `da_verdict`, `da_objections`…) và có chú thích chèn vào mục 4–5 do bạn viết. Nội dung audit này giờ chỉ còn trong `_Archive/Date-folder versions/` — nếu muốn, có thể gộp phần `## Devil's Advocate` vào note chuẩn sau.
> - Một số note chuẩn trong Trades lại có phần mà bản folder ngày KHÔNG có (bảng chấm điểm, Action Items): 05-04, 05-13, 05-15, 06-05, 06-17 Loss 04. Vì vậy giữ Trades làm bản chuẩn.
> - Bản 06-02 được đưa vào Trades chính là bản có DA audit (bản duy nhất tồn tại).

## Việc còn tồn (chưa tự sửa)

- [ ] Đổi tên `Win - 01 - Trade 2026-06-17 NDX Long` → `… 2026-06-12 …` (frontmatter date là 06-12). Đổi bằng Obsidian để link tự cập nhật.
- [ ] Kiểm tra frontmatter `date` của 3 lệnh Loss 01–03 ngày 06-17 (đang ghi 2026-06-18 → PnL Calendar hiển thị ở ngày 18).
- [ ] Hình mồ côi (không note nào nhúng): `EURUSD-20210208-2021-4`, `EURUSD-20220429-2024-1..4`, `EURUSD-20230503-2025-1..5` (có vẻ là ảnh backtest để nhầm vào live → cân nhắc chuyển sang `04 - Backtesting/Screenshots`), `NDX-20260605-M5`, `NDX-20261021-D1-context`, `NDX-20261021-M1-postmortem` (có ảnh ngày 10-21 nhưng chưa có note lệnh).
- [ ] Note 05-21 nhúng placeholder `![[SYMBOL-YYYYMMDD-M1.png]]` chưa thay bằng hình thật.
- [ ] Obsidian → Settings → Files & links → *Default location for new attachments* = `05 - Live Trading Journal/attachments` (hoặc theo ý bạn), và thêm `05 - Live Trading Journal/_Archive` vào *Excluded files* để bản archive không lẫn vào search/graph.
- [ ] Scheduled task **Daily Summary** (đang tắt) còn đọc `Trades/{YYYY}/{MM}/{DD}/` — cần sửa nếu bật lại.

## Đã cập nhật quy ước
- `CLAUDE.md`, `README.md`: Trades phẳng, hình vào `attachments/`
- 6 dashboard: dòng mô tả ví dụ đường dẫn (không đụng vào code dataviewjs — vẫn đọc `FROM "05 - Live Trading Journal/Trades"` nên chạy bình thường)
- `19-Liquidity`: dòng hướng dẫn lưu ảnh
