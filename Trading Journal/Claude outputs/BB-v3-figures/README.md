# BB-v3 figures — mã sinh hình

Mã Python sinh 58 hình `BB-v3-*.svg` của note `04-Breaker-Block` (v3, 2026-11-10).

- `bbdraw.py` — thư viện vẽ (nến, vùng, nhãn) + các chuỗi nến dựng (`seq(kind)`).
- `figs1.py` … `figs4.py` — hình 01–14, 15–30, 31–46, 47–58.
- `qa.js` — kiểm tra tràn chữ / chồng chữ bằng Playwright và xuất PNG.

Chạy: `python3 figs1.py && python3 figs2.py && python3 figs3.py && python3 figs4.py` (cần Pillow và font Inter để đo độ rộng chữ; sửa `FR`, `FB` trong `bbdraw.py` nếu font nằm ở chỗ khác). Hình ra thư mục `svg/` cạnh mã.
