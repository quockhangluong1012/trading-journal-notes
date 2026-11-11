# CHoCH v2 figures — mã sinh hình

Mã Python sinh 54 hình `CHoCH-v2-*.svg` của note `09-Change-of-Character` (v2, 2026-11-10).

- `bbdraw.py` — thư viện vẽ gốc (copy từ `BB-v3-figures`, không sửa).
- `chdraw.py` — phần mở rộng: tiền tố tên hình, zigzag, bộ sinh chuỗi nến `gen()`, `fvgs()`, chuỗi dựng `bull_seq()` / `bear_seq()`.
- `figs1.py` … `figs4.py` — hình 01–13, 14–26, 27–40, 41–54. Chạy một hình: `python3 figs2.py 19`.
- `qa.js` — kiểm tra tràn chữ / chồng chữ bằng Playwright và xuất PNG (`svg/` → `png/`).
- `sheet.py` — ghép nhiều PNG thành một trang xem nhanh.

Chạy: `python3 figs1.py && python3 figs2.py && python3 figs3.py && python3 figs4.py` (cần Pillow và font Inter; sửa `FR`, `FB` trong `bbdraw.py` nếu font nằm chỗ khác). Hình ra thư mục `svg/` cạnh mã. Mọi mức giá là số minh họa.
