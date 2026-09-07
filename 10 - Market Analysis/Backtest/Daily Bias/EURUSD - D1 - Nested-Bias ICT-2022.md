# Case Study — EUR/USD D1: Nested Dealing Range, Xung đột Bias & Chuyển giao Authority (ICT 2022 Model)

> **Nguồn:** phiên phân tích/backtest EUR/USD D1 (OANDA, FXReplay — dữ liệu replay 2016, giai đoạn Brexit). Toàn bộ mức giá đọc từ ảnh chụp màn hình, sai số tự khai **±5–10 pip**. Tài liệu này tổng hợp lại chuỗi phân tích → devil's advocate → doctrine check → audit → Q&A về cấu trúc lồng (nested structure) đã thực hiện trong phiên.
>
> **Nguyên tắc đọc tài liệu:** mọi hình vẽ tay trên chart (box, đường kẻ) là **claim của người phân tích**, không phải **evidence** — evidence chỉ là nến (OHLC) thật. Tài liệu giữ nguyên phân biệt này ở mọi bước.

---

## 1. Bối cảnh & Dữ liệu Chart

| Mục | Giá trị |
|---|---|
| Instrument | EUR/USD |
| Khung thời gian | D1 (chính), H1 (bổ sung) |
| Nguồn dữ liệu | OANDA via FXReplay (replay lịch sử 2016) |
| Giá tại điểm quyết định gốc | 1.11501 (nến D1: O 1.11156 / H 1.11562 / L 1.11128 / C 1.11501) |
| Giá tại các lần review sau | 1.12624 → 1.1262 (hiện tại, theo Q&A gần nhất) |
| Sai số đọc giá | ±5–10 pip (tự khai, do đọc pixel trên ảnh chụp) |
| Sự kiện neo cấu trúc lớn | Displacement giảm mạnh — Brexit, cuối tháng 6/2016 |

**Giới hạn công cụ trong phiên:** checkout của các skill `ict-doctrine`, `ict-audit`, `ict-devils-advocate` chỉ có `SKILL.md` — các file `doctrine.md`, `audit_rubric.md`, `check_facts.py`, `rebuttal_playbook.md` không có mặt. Mọi ruling doctrine trong tài liệu này neo vào bảng định nghĩa nhanh, không phải canon đầy đủ. Audit chạy ở chế độ **không có JSON extraction** — chỉ finding LOGIC/CONSISTENCY được ground đầy đủ; finding EVIDENCE là tạm định.

---

## 2. External Structure (Bậc lớn, D1)

**C1 — External dealing range:** anchor là nến displacement giảm cực mạnh (Brexit), tạo range hợp lệ:

- **Range High:** ~1.1426 (đỉnh trước displacement — BSL lớn, chưa bị quét)
- **Range Low:** ~1.0917 (đáy Brexit — SSL lớn, chưa bị quét lại)
- **Equilibrium (EQ):** (1.1426 + 1.0917) / 2 ≈ **1.1172**

**C2 — Vị trí giá tại điểm quyết định gốc (1.1150):** ngay dưới EQ → rìa trên vùng discount, gần trung tính về premium/discount trên range lớn.

**Bearish MSS bậc lớn:** cú displacement giảm Brexit tự nó là một bearish MSS hợp lệ trên cấu trúc lớn — phá body xuống dưới swing low của leg tăng trước đó. Theo doctrine, delivery bậc lớn là **bearish cho đến khi bị phủ nhận** (displacement + close D1 qua 1.1426).

<svg viewBox="0 0 960 580" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans, Helvetica, Arial, sans-serif">
<text x="480" y="28" font-size="15" fill="#111" text-anchor="middle" font-weight="bold">Sơ đồ 1 — External Dealing Range · Premium/Discount · Leg giá hiện tại</text>
<rect x="120" y="82.7" width="500" height="169.3" fill="#e0433d" fill-opacity="0.1"/>
<rect x="120" y="252.0" width="500" height="170.0" fill="#1f9d55" fill-opacity="0.1"/>
<rect x="120" y="82.7" width="500" height="339.3" fill="none" fill-opacity="1.0" stroke="#555" stroke-width="1.5"/>
<line x1="120" y1="252.0" x2="620" y2="252.0" stroke="#2563eb" stroke-width="1.6" stroke-dasharray="6,4"/>
<line x1="120" y1="82.7" x2="634" y2="82.7" stroke="#c0392b" stroke-width="1.2"/>
<line x1="634" y1="82.7" x2="646" y2="90" stroke="#bbb" stroke-width="1"/>
<text x="650" y="87" font-size="11.5" fill="#c0392b" text-anchor="start" font-weight="bold">1.1426 — BSL lớn / Old High</text>
<text x="650" y="101" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">external, chưa quét</text>
<line x1="120" y1="153.3" x2="634" y2="153.3" stroke="#e08e0b" stroke-width="1.2" stroke-dasharray="4,3"/>
<text x="650" y="147.3" font-size="11.5" fill="#e08e0b" text-anchor="start" font-weight="bold">1.1320 — wick reject (H1)</text>
<text x="650" y="161.3" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">[OPEN] chưa xác nhận</text>
<line x1="120" y1="192.0" x2="634" y2="192.0" stroke="#111" stroke-width="1.2" stroke-dasharray="4,3"/>
<text x="650" y="187.3" font-size="11.5" fill="#111" text-anchor="start" font-weight="bold">1.1262 — giá hiện tại</text>
<line x1="120" y1="209.3" x2="634" y2="209.3" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,3"/>
<line x1="634" y1="209.3" x2="646" y2="230.3" stroke="#bbb" stroke-width="1"/>
<text x="650" y="227.3" font-size="11.5" fill="#2563eb" text-anchor="start" font-weight="bold">1.1236 — BSL nội bộ</text>
<text x="650" y="241.3" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">đã quét (body close)</text>
<line x1="120" y1="252.0" x2="634" y2="252.0" stroke="#2563eb" stroke-width="1.2" stroke-dasharray="4,3"/>
<line x1="634" y1="252.0" x2="646" y2="270.3" stroke="#bbb" stroke-width="1"/>
<text x="650" y="267.3" font-size="11.5" fill="#2563eb" text-anchor="start" font-weight="bold">EQ 1.1172</text>
<text x="650" y="281.3" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">biên premium/discount</text>
<line x1="120" y1="266.7" x2="634" y2="266.7" stroke="#7a7a7a" stroke-width="1.2" stroke-dasharray="4,3"/>
<line x1="634" y1="266.7" x2="646" y2="310.3" stroke="#bbb" stroke-width="1"/>
<text x="650" y="307.3" font-size="11.5" fill="#7a7a7a" text-anchor="start" font-weight="bold">1.1150 — nến quyết định</text>
<text x="650" y="321.3" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">turn 1 (bias gốc)</text>
<line x1="120" y1="334.7" x2="634" y2="334.7" stroke="#c0392b" stroke-width="1.2" stroke-dasharray="4,3"/>
<line x1="634" y1="334.7" x2="646" y2="350.3" stroke="#bbb" stroke-width="1"/>
<text x="650" y="347.3" font-size="11.5" fill="#c0392b" text-anchor="start" font-weight="bold">1.1048 — invalidation nội bộ</text>
<text x="650" y="361.3" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">C7</text>
<line x1="120" y1="422.0" x2="634" y2="422.0" stroke="#c0392b" stroke-width="1.2"/>
<text x="650" y="416.0" font-size="11.5" fill="#c0392b" text-anchor="start" font-weight="bold">1.0917 — SSL lớn / Brexit Low</text>
<text x="650" y="430.0" font-size="9.5" fill="#777" text-anchor="start" font-weight="normal" font-style="italic">external, chưa quét</text>
<rect x="230" y="294.7" width="130" height="22.0" fill="#888888" fill-opacity="0.28" stroke="#555" stroke-width="1" stroke-dasharray="3,2"/>
<text x="295" y="301.7" font-size="9.3" fill="#333" text-anchor="middle" font-weight="normal">box 1.1075–1.1108</text>
<text x="295" y="314.7" font-size="8.6" fill="#8a4b00" text-anchor="middle" font-weight="bold" font-style="italic">[UNVERIFIED, user-drawn]</text>
<polyline points="150,422.0 250,400.0 350,209.3 430,336.7 490,266.7 560,153.3 600,192.0" fill="none" stroke="#1d4ed8" stroke-width="2.4"/>
<circle cx="150" cy="422.0" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="91.80000000000001" y="380.0" width="116.39999999999999" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<circle cx="250" cy="400.0" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="180.60000000000002" y="423.0" width="138.79999999999998" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<circle cx="350" cy="209.3" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="283.4" y="153.3" width="133.2" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<circle cx="430" cy="336.7" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="371.8" y="359.7" width="116.39999999999999" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<circle cx="490" cy="266.7" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="434.6" y="210.7" width="110.8" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<circle cx="560" cy="153.3" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="515.8" y="97.30000000000001" width="88.39999999999999" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<circle cx="600" cy="192.0" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="572.6" y="215.0" width="54.8" height="28.0" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<text x="150" y="404.0" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.0917</text>
<text x="150" y="391.0" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">Brexit low (anchor)</text>
<text x="250" y="434.0" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.0950</text>
<text x="250" y="447.0" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">sweep? [C3 UNSUPPORTED]</text>
<text x="350" y="177.3" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.1236</text>
<text x="350" y="164.3" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">displacement high (C4)</text>
<text x="430" y="370.7" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.1045</text>
<text x="430" y="383.7" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">pullback / OTE (C5)</text>
<text x="490" y="234.7" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.1150</text>
<text x="490" y="221.7" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">nến quyết định gốc</text>
<text x="560" y="121.30000000000001" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.1320</text>
<text x="560" y="108.30000000000001" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">wick, rejected</text>
<text x="600" y="226.0" font-size="10" fill="#1d4ed8" text-anchor="middle" font-weight="bold">1.1262</text>
<text x="600" y="239.0" font-size="8.6" fill="#444" text-anchor="middle" font-weight="normal">hiện tại</text>
<circle cx="150" cy="422.0" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<circle cx="250" cy="400.0" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<circle cx="350" cy="209.3" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<circle cx="430" cy="336.7" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<circle cx="490" cy="266.7" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<circle cx="560" cy="153.3" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<circle cx="600" cy="192.0" r="4.3" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="160" y="553" width="14" height="10" fill="#e0433d" fill-opacity="0.25"/>
<text x="180" y="562" font-size="10.5" fill="#333" text-anchor="start" font-weight="normal">Premium (external)</text>
<rect x="340" y="553" width="14" height="10" fill="#1f9d55" fill-opacity="0.25"/>
<text x="360" y="562" font-size="10.5" fill="#333" text-anchor="start" font-weight="normal">Discount (external)</text>
<line x1="520" y1="558" x2="542" y2="558" stroke="#1d4ed8" stroke-width="2.4"/>
<text x="548" y="562" font-size="10.5" fill="#333" text-anchor="start" font-weight="normal">Leg giá hiện tại (schematic)</text>
</svg>

---

## 3. Internal Leg — Bậc nhỏ (nội bộ dealing range hiện tại)

Chuỗi lập luận gốc theo trình tự 2022 Model trên D1:

1. **C3 — Sweep sellside:** đầu tháng 8, giá tạo đáy ~1.0950 quét nhẹ dưới các đáy tháng 7 (equal lows) — sellside bị lấy trước. **Trạng thái: UNSUPPORTED** — biên độ quét nhỏ hơn sai số pixel tự khai, chưa có OHLC readout xác nhận.
2. **C4 — Displacement + MSS nội bộ:** chuỗi nến xanh thân lớn đẩy thẳng từ ~1.0950 lên 1.1236, phá qua swing high nội bộ vùng 1.115–1.117. **Trạng thái: PASS — load-bearing.** Đây là claim duy nhất đứng vững trước mọi đòn tấn công trong toàn bộ phiên (xem §4).
3. **C5 — Retracement về OTE/FVG:** pullback về ~1.1045 (67% leg) rơi vào OTE (62–79%); ô xám 1.1075–1.1108 được gắn nhãn FVG/OB. **Trạng thái: UNSUPPORTED** — ô xám là hình vẽ tay (claim), gap phải được xác lập bằng 3 nến thật; khi tính lại, box nằm ở retrace 44.8–56.3%, **ngoài** OTE 62–79% — hai vùng không giao nhau như bản gốc trình bày.
4. **C6 — Kết luận bias:** "bias chính bullish trong range, khi 1.1048 còn giữ." Chỉ đứng được nhờ C4; hai chân phụ C3 và C5 không cứu được thứ hạng "chính" này.
5. **C7 — Invalidation:** D1 đóng dưới 1.1048 → đảo sang kịch bản giảm về 1.0950 → 1.0917. **Trạng thái: PASS** — đây là điểm mạnh nhất của bản phân tích gốc: falsifiable, tiền đăng ký trước khi biết kết quả.

<svg viewBox="0 0 960 540" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans, Helvetica, Arial, sans-serif">
<text x="480" y="28" font-size="15" fill="#111" text-anchor="middle" font-weight="bold">Sơ đồ 3 — Bản đồ thanh khoản (Liquidity Map)</text>
<rect x="120" y="68.0" width="500" height="384.0" fill="#fafafa" fill-opacity="1.0" stroke="#ddd" stroke-width="1"/>
<line x1="120" y1="82.7" x2="620" y2="82.7" stroke="#1d4ed8" stroke-width="1" stroke-dasharray="2,2"/>
<circle cx="136" cy="82.7" r="5" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<line x1="136" y1="82.7" x2="150" y2="95" stroke="#ccc" stroke-width="1"/>
<rect x="158" y="79" width="420" height="30" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<text x="160" y="91" font-size="11.5" fill="#111" text-anchor="start" font-weight="bold">1.1426 — BSL lớn — Old High trước Brexit</text>
<text x="160" y="106" font-size="9.8" fill="#666" text-anchor="start" font-weight="normal" font-style="italic">chưa quét</text>
<line x1="120" y1="209.3" x2="620" y2="209.3" stroke="#1d4ed8" stroke-width="1" stroke-dasharray="2,2"/>
<circle cx="136" cy="209.3" r="5" fill="#1d4ed8" stroke="#1a1a1a" stroke-width="1.5"/>
<line x1="136" y1="209.3" x2="150" y2="201.3" stroke="#ccc" stroke-width="1"/>
<rect x="158" y="185.3" width="420" height="30" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<text x="160" y="197.3" font-size="11.5" fill="#111" text-anchor="start" font-weight="bold">1.1236 — BSL nội bộ — đỉnh swing trước leg tăng</text>
<text x="160" y="212.3" font-size="9.8" fill="#666" text-anchor="start" font-weight="normal" font-style="italic">ĐÃ quét (body close xuyên)</text>
<line x1="120" y1="334.7" x2="620" y2="334.7" stroke="#c0392b" stroke-width="1" stroke-dasharray="2,2"/>
<circle cx="136" cy="334.7" r="5" fill="#c0392b" stroke="#1a1a1a" stroke-width="1.5"/>
<line x1="136" y1="334.7" x2="150" y2="326.7" stroke="#ccc" stroke-width="1"/>
<rect x="158" y="310.7" width="420" height="30" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<text x="160" y="322.7" font-size="11.5" fill="#111" text-anchor="start" font-weight="bold">1.1048 — SSL nội bộ — đáy pullback gần nhất</text>
<text x="160" y="337.7" font-size="9.8" fill="#666" text-anchor="start" font-weight="normal" font-style="italic">= mốc invalidation (C7)</text>
<line x1="120" y1="383.3" x2="620" y2="383.3" stroke="#c0392b" stroke-width="1" stroke-dasharray="2,2"/>
<circle cx="136" cy="383.3" r="5" fill="#c0392b" stroke="#1a1a1a" stroke-width="1.5"/>
<rect x="158" y="366.7" width="420" height="30" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<text x="160" y="378.7" font-size="11.5" fill="#111" text-anchor="start" font-weight="bold">1.0975 — cụm SSL — equal lows tháng 7</text>
<text x="160" y="393.7" font-size="9.8" fill="#666" text-anchor="start" font-weight="normal" font-style="italic">chưa xác nhận bị quét (O1 OPEN)</text>
<line x1="120" y1="422.0" x2="620" y2="422.0" stroke="#c0392b" stroke-width="1" stroke-dasharray="2,2"/>
<circle cx="136" cy="422.0" r="5" fill="#c0392b" stroke="#1a1a1a" stroke-width="1.5"/>
<line x1="136" y1="422.0" x2="150" y2="438.7" stroke="#ccc" stroke-width="1"/>
<rect x="158" y="422.7" width="420" height="30" fill="#ffffff" fill-opacity="0.88" rx="3"/>
<text x="160" y="434.7" font-size="11.5" fill="#111" text-anchor="start" font-weight="bold">1.0917 — SSL lớn — Brexit Low</text>
<text x="160" y="449.7" font-size="9.8" fill="#666" text-anchor="start" font-weight="normal" font-style="italic">chưa quét (untouched)</text>
<text x="480" y="524" font-size="10.5" fill="#555" text-anchor="middle" font-weight="normal">BSL = buyside liquidity (đỉnh)   ·   SSL = sellside liquidity (đáy)</text>
</svg>

---

## 4. Objection Ledger — Devil's Advocate & Audit

| # | Target | Loại | Mức độ | Nội dung | Trạng thái |
|---|---|---|---|---|---|
| O1 | C3 | UNSUPPORTED | material | Sweep ~1.0950 nằm trong sai số pixel ±5–10 pip; không ảnh nào phân giải được đáy Aug có thấp hơn đáy July | OPEN |
| O2 | C5 | METHOD | material | Ô xám là hình vẽ (claim) dùng làm bằng chứng cho chính nó; box thực tế nằm ngoài dải OTE khi tính lại | OPEN |
| O3 | C6 | METHOD | material | Tie-breaker chọn "bullish là bias chính" dựa trên C3 + C5 — cả hai đều lỗi | OPEN |
| O4 | C2 | ARITHMETIC | minor | Nhãn "discount" flip thành premium 54.3% nếu dùng range nội bộ 1.1048–1.1236 | OPEN |
| O5 | C7 | SELF-CONTRADICTION | minor | Invalidation 1.1048 nằm trên đáy tham chiếu tự đo 1.1045 (chênh 3 pip, không giải thích) | OPEN |
| O6 | C8* | SELF-CONTRADICTION | material | Quy trình "D1 chỉ cần dealing range + bias nội bộ" mâu thuẫn với chính phát biểu "ngoài range vẫn bearish" | OPEN |
| O7 | C10* | ARITHMETIC | material | "Ưu tiên long" phát biểu vô điều kiện tại 67.8% external / ~79% internal — premium-on-premium | OPEN |
| O8 | C10+C11* | METHOD | **fatal** | Stance "ưu tiên long cho tới khi quét BSL" không có điều kiện làm stance *sai* trước khi biết kết quả | OPEN |
| O9 | C11* | METHOD | material | Chuẩn kép: flip bull cần ít bằng chứng hơn flip bear | OPEN |
| O10 | quy trình | DOCTRINE | minor | "Sweep tạo thành MSS" — sai; đây là hai sự kiện tách biệt (sweep, rồi displacement+close mới là MSS) | OPEN |

*C8–C11: các claim phát sinh từ câu hỏi quy trình D1→H1→M5 của người dùng, đánh số tiếp theo C1–C7.

**Verdict Devil's Advocate (vòng 1 — thesis D1 gốc):** SURVIVES, WEAKENED — C4 (load-bearing) không bị phá; các chân phụ C3, C5 và thứ hạng "primary" của C6 thì không đứng được.

**Verdict Devil's Advocate (vòng 2 — quy trình D1→H1→M5 + stance hiện tại):** BROKEN — C8 sập bởi self-contradiction; C10 sập bởi arithmetic (premium-on-premium); C11 thiếu chuẩn đối xứng; O8 là objection fatal duy nhất trong toàn phiên.

**Verdict ICT Doctrine Check:** DOCTRINE ALIGNED — load-bearing C4 PASS, không claim nào FAIL/HINDSIGHT; UNSUPPORTED phụ nêu tên: C3, C5b. *(ALIGNED nghĩa là gọi tên đúng luật với evidence đã đưa — không phải "setup tốt", không xác nhận bias.)*

**Verdict ICT Audit:** THESIS UNPROVEN (vòng 1) → THESIS BROKEN (vòng 2, quy trình) — load-bearing đứng về logic nhưng chuỗi suy luận tới kết luận đứt ở các claim phụ chưa evidence-grade.

<svg viewBox="0 0 960 420" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans, Helvetica, Arial, sans-serif">
<text x="480" y="28" font-size="15" fill="#111" text-anchor="middle" font-weight="bold">Sơ đồ 4 — Chuỗi lập luận (C1 tới C7) và các objection tấn công</text>
<rect x="28.0" y="70" width="112" height="96" fill="#eaf7ee" fill-opacity="1.0" stroke="#1f9d55" stroke-width="1.8"/>
<text x="84.0" y="90" font-size="13" fill="#1f9d55" text-anchor="middle" font-weight="bold">C1</text>
<text x="84.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">External range</text>
<text x="84.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">+ EQ</text>
<text x="84.0" y="144" font-size="8.8" fill="#1f9d55" text-anchor="middle" font-weight="bold">PASS</text>
<rect x="160.0" y="70" width="112" height="96" fill="#eaf7ee" fill-opacity="1.0" stroke="#1f9d55" stroke-width="1.8"/>
<text x="216.0" y="90" font-size="13" fill="#1f9d55" text-anchor="middle" font-weight="bold">C2</text>
<text x="216.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">Premium/discount</text>
<text x="216.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">~ EQ</text>
<text x="216.0" y="144" font-size="8.8" fill="#1f9d55" text-anchor="middle" font-weight="bold">PASS</text>
<line x1="140.0" y1="118" x2="160.0" y2="118" stroke="#999" stroke-width="1.3"/>
<polygon points="153.0,113 153.0,123 160.0,118" fill="#999"/>
<rect x="292.0" y="70" width="112" height="96" fill="#fdecea" fill-opacity="1.0" stroke="#c0392b" stroke-width="1.8"/>
<text x="348.0" y="90" font-size="13" fill="#c0392b" text-anchor="middle" font-weight="bold">C3</text>
<text x="348.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">Sweep SSL</text>
<text x="348.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">~1.0950</text>
<text x="348.0" y="144" font-size="8.8" fill="#c0392b" text-anchor="middle" font-weight="bold">UNSUPPORTED</text>
<line x1="272.0" y1="118" x2="292.0" y2="118" stroke="#999" stroke-width="1.3"/>
<polygon points="285.0,113 285.0,123 292.0,118" fill="#999"/>
<rect x="424.0" y="70" width="112" height="96" fill="#eaf7ee" fill-opacity="1.0" stroke="#1f9d55" stroke-width="1.8"/>
<text x="480.0" y="90" font-size="13" fill="#1f9d55" text-anchor="middle" font-weight="bold">C4</text>
<text x="480.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">Displacement</text>
<text x="480.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">+ MSS nội bộ</text>
<text x="480.0" y="144" font-size="8.8" fill="#1f9d55" text-anchor="middle" font-weight="bold">PASS</text>
<text x="480.0" y="155" font-size="8.8" fill="#1f9d55" text-anchor="middle" font-weight="bold">(load-bearing)</text>
<line x1="404.0" y1="118" x2="424.0" y2="118" stroke="#999" stroke-width="1.3"/>
<polygon points="417.0,113 417.0,123 424.0,118" fill="#999"/>
<rect x="556.0" y="70" width="112" height="96" fill="#fdecea" fill-opacity="1.0" stroke="#c0392b" stroke-width="1.8"/>
<text x="612.0" y="90" font-size="13" fill="#c0392b" text-anchor="middle" font-weight="bold">C5</text>
<text x="612.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">OTE + FVG</text>
<text x="612.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">respected</text>
<text x="612.0" y="144" font-size="8.8" fill="#c0392b" text-anchor="middle" font-weight="bold">UNSUPPORTED</text>
<line x1="536.0" y1="118" x2="556.0" y2="118" stroke="#999" stroke-width="1.3"/>
<polygon points="549.0,113 549.0,123 556.0,118" fill="#999"/>
<rect x="688.0" y="70" width="112" height="96" fill="#fff7e6" fill-opacity="1.0" stroke="#e08e0b" stroke-width="1.8"/>
<text x="744.0" y="90" font-size="13" fill="#e08e0b" text-anchor="middle" font-weight="bold">C6</text>
<text x="744.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">Bias chính:</text>
<text x="744.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">bullish</text>
<text x="744.0" y="144" font-size="8.8" fill="#e08e0b" text-anchor="middle" font-weight="bold">Chỉ đứng</text>
<text x="744.0" y="155" font-size="8.8" fill="#e08e0b" text-anchor="middle" font-weight="bold">nhờ C4</text>
<line x1="668.0" y1="118" x2="688.0" y2="118" stroke="#999" stroke-width="1.3"/>
<polygon points="681.0,113 681.0,123 688.0,118" fill="#999"/>
<rect x="820.0" y="70" width="112" height="96" fill="#eaf7ee" fill-opacity="1.0" stroke="#1f9d55" stroke-width="1.8"/>
<text x="876.0" y="90" font-size="13" fill="#1f9d55" text-anchor="middle" font-weight="bold">C7</text>
<text x="876.0" y="108" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">Invalidation</text>
<text x="876.0" y="121" font-size="9.8" fill="#222" text-anchor="middle" font-weight="normal">1.1048</text>
<text x="876.0" y="144" font-size="8.8" fill="#1f9d55" text-anchor="middle" font-weight="bold">PASS</text>
<line x1="800.0" y1="118" x2="820.0" y2="118" stroke="#999" stroke-width="1.3"/>
<polygon points="813.0,113 813.0,123 820.0,118" fill="#999"/>
<line x1="348.0" y1="300" x2="348.0" y2="168" stroke="#8a4b00" stroke-width="1.5" stroke-dasharray="4,3"/>
<polygon points="343.0,175 353.0,175 348.0,168" fill="#8a4b00"/>
<rect x="273.0" y="302" width="150" height="56" fill="#fff" fill-opacity="1.0" stroke="#8a4b00" stroke-width="1"/>
<text x="348.0" y="320" font-size="11" fill="#8a4b00" text-anchor="middle" font-weight="bold">O1 · material</text>
<text x="348.0" y="337" font-size="9.3" fill="#555" text-anchor="middle" font-weight="normal">sweep &lt; sai số</text>
<text x="348.0" y="350" font-size="9.3" fill="#555" text-anchor="middle" font-weight="normal">pixel</text>
<line x1="612.0" y1="300" x2="612.0" y2="168" stroke="#8a4b00" stroke-width="1.5" stroke-dasharray="4,3"/>
<polygon points="607.0,175 617.0,175 612.0,168" fill="#8a4b00"/>
<rect x="537.0" y="302" width="150" height="56" fill="#fff" fill-opacity="1.0" stroke="#8a4b00" stroke-width="1"/>
<text x="612.0" y="320" font-size="11" fill="#8a4b00" text-anchor="middle" font-weight="bold">O2 · material</text>
<text x="612.0" y="337" font-size="9.3" fill="#555" text-anchor="middle" font-weight="normal">box = claim,</text>
<text x="612.0" y="350" font-size="9.3" fill="#555" text-anchor="middle" font-weight="normal">không phải evidence</text>
<line x1="744.0" y1="300" x2="744.0" y2="168" stroke="#8a4b00" stroke-width="1.5" stroke-dasharray="4,3"/>
<polygon points="739.0,175 749.0,175 744.0,168" fill="#8a4b00"/>
<rect x="669.0" y="302" width="150" height="56" fill="#fff" fill-opacity="1.0" stroke="#8a4b00" stroke-width="1"/>
<text x="744.0" y="320" font-size="11" fill="#8a4b00" text-anchor="middle" font-weight="bold">O3 · material</text>
<text x="744.0" y="337" font-size="9.3" fill="#555" text-anchor="middle" font-weight="normal">tie-breaker dựa</text>
<text x="744.0" y="350" font-size="9.3" fill="#555" text-anchor="middle" font-weight="normal">C3+C5 (đều lỗi)</text>
<text x="480" y="400" font-size="11.5" fill="#111" text-anchor="middle" font-weight="bold">C4 (load-bearing) không bị phá bởi objection nào -&gt; verdict: SURVIVES, WEAKENED</text>
</svg>

---

## 5. Nested Structure — Xung đột Bias giữa hai bậc

Câu hỏi cốt lõi của phiên: giá đã có bearish MSS trên cấu trúc D1 lớn (hậu-Brexit), nhưng trong range hiện tại lại có sweep SSL + displacement + MSS nội bộ → bias bullish. Hai bias này **không mâu thuẫn** vì chúng trả lời hai câu hỏi khác nhau:

- **Bậc lớn (external D1):** "giá đang được deliver đi đâu trong toàn bức tranh?" → bearish, hiệu lực tới khi bị phủ nhận tại 1.1426.
- **Bậc nhỏ (internal leg):** "giá đang làm gì trong range hiện tại?" → bullish, nhưng authority chỉ có giá trị **trong nội bộ range đó**.

Điểm mấu chốt bị bỏ sót trong phát biểu quy trình gốc của người dùng (C8, bị O6 bắt lỗi): leg bullish nội bộ **chính là công cụ phục vụ** kịch bản bearish lớn — sau một bearish MSS, thị trường cần một nhịp retracement lên premium để lấy giá bán tốt trước khi tiếp tục xuống. Internal bullish không "chống lại" external bearish, nó "chở hàng" cho external bearish.

<svg viewBox="0 0 960 380" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans, Helvetica, Arial, sans-serif">
<text x="480" y="28" font-size="15" fill="#111" text-anchor="middle" font-weight="bold">Sơ đồ 2 — Xung đột hai bậc cấu trúc (nested bias)</text>
<rect x="70" y="65" width="300" height="245" fill="#fdecea" fill-opacity="1.0" stroke="#c0392b" stroke-width="1.6"/>
<text x="220" y="92" font-size="13" fill="#c0392b" text-anchor="middle" font-weight="bold">BẬC LỚN (External, D1)</text>
<text x="220" y="116" font-size="11" fill="#333" text-anchor="middle" font-weight="normal">Bearish MSS sau displacement</text>
<text x="220" y="132" font-size="11" fill="#333" text-anchor="middle" font-weight="normal">Brexit — thân lớn, phá cấu trúc</text>
<text x="220" y="158" font-size="10.5" fill="#555" text-anchor="middle" font-weight="normal">Hiệu lực tới khi bị phủ nhận:</text>
<text x="220" y="174" font-size="10.5" fill="#555" text-anchor="middle" font-weight="normal">displacement + close D1 qua 1.1426</text>
<line x1="220" y1="192" x2="220" y2="240" stroke="#c0392b" stroke-width="3"/>
<polygon points="210,240 230,240 220,254" fill="#c0392b"/>
<text x="220" y="285" font-size="12" fill="#c0392b" text-anchor="middle" font-weight="bold">Delivery: XUỐNG</text>
<rect x="590" y="65" width="300" height="245" fill="#eaf7ee" fill-opacity="1.0" stroke="#1f9d55" stroke-width="1.6"/>
<text x="740" y="92" font-size="13" fill="#1f9d55" text-anchor="middle" font-weight="bold">BẬC NHỎ (Internal leg)</text>
<text x="740" y="116" font-size="11" fill="#333" text-anchor="middle" font-weight="normal">Bullish sau sweep SSL* +</text>
<text x="740" y="132" font-size="11" fill="#333" text-anchor="middle" font-weight="normal">displacement + MSS nội bộ</text>
<text x="740" y="158" font-size="10.5" fill="#555" text-anchor="middle" font-weight="normal">Chỉ có authority TRONG range</text>
<text x="740" y="174" font-size="10.5" fill="#555" text-anchor="middle" font-weight="normal">nội bộ (C4 = load-bearing)</text>
<line x1="740" y1="254" x2="740" y2="206" stroke="#1f9d55" stroke-width="3"/>
<polygon points="730,206 750,206 740,192" fill="#1f9d55"/>
<text x="740" y="270" font-size="12" fill="#1f9d55" text-anchor="middle" font-weight="bold">Delivery: LÊN</text>
<text x="740" y="286" font-size="10.3" fill="#1f9d55" text-anchor="middle" font-weight="normal">(retracement phục vụ</text>
<text x="740" y="300" font-size="10.3" fill="#1f9d55" text-anchor="middle" font-weight="normal">delivery bậc lớn)</text>
<rect x="400" y="140" width="160" height="115" fill="#fff7e6" fill-opacity="1.0" stroke="#e08e0b" stroke-width="1.6" stroke-dasharray="4,3"/>
<text x="480" y="168" font-size="12" fill="#8a4b00" text-anchor="middle" font-weight="bold">VÙNG VA CHẠM</text>
<text x="480" y="187" font-size="10.3" fill="#8a4b00" text-anchor="middle" font-weight="normal">Premium 1.1172–1.1426</text>
<text x="480" y="203" font-size="10.3" fill="#8a4b00" text-anchor="middle" font-weight="normal">giá hiện tại: 1.1262</text>
<text x="480" y="222" font-size="10.5" fill="#c0392b" text-anchor="middle" font-weight="bold">Handoff?</text>
<text x="480" y="237" font-size="10.5" fill="#c0392b" text-anchor="middle" font-weight="bold">[CHƯA XÁC NHẬN]</text>
<line x1="380" y1="195" x2="300" y2="175" stroke="#999" stroke-width="1.3" stroke-dasharray="3,2"/>
<line x1="560" y1="195" x2="640" y2="175" stroke="#999" stroke-width="1.3" stroke-dasharray="3,2"/>
<text x="480" y="350" font-size="10.5" fill="#8a4b00" text-anchor="middle" font-weight="normal" font-style="italic">* sweep SSL (C3) vẫn UNSUPPORTED — chưa có OHLC readout xác nhận</text>
</svg>

---

## 6. Ranh giới Chuyển giao Authority

Không có một mức giá "cứng" duy nhất — đây là một vùng có nhiều nấc tin cậy khác nhau:

| Nấc | Mức giá | Trạng thái | Ý nghĩa |
|---|---|---|---|
| Soft boundary | EQ 1.1172 | Đã xác lập (C1) | Bắt đầu premium — chưa phải handoff, chỉ là ranh giới định giá |
| Observation | 1.1236 | Taken (body close xuyên) | Internal BSL đã bị vượt — hết vai trò biên |
| Observation | 1.1320 | **OPEN** | Wick reject H1 — dữ kiện đầu tiên gợi ý phản ứng bậc lớn, nhưng thiếu sweep + CISD/MSS H1 xác nhận |
| Unresolved | Bearish FVG/OB (nến Brexit) | **Chưa xác định** | Đây lẽ ra là mức cụ thể nhất, nhưng vị trí chưa từng được xác lập — cần H1/M5 zoom đoạn hình thành cú giảm Brexit (chưa được cung cấp trong phiên) |
| Hard boundary | 1.1426 | Đã xác lập (C1) | External invalidation: displacement + D1 close qua đây → external structure flip |
| Internal invalidation | 1.1048 | Đã xác lập (C7) | Bias nội bộ (C6) chết nếu D1 đóng dưới đây |

<svg viewBox="0 0 960 620" xmlns="http://www.w3.org/2000/svg" font-family="Noto Sans, Helvetica, Arial, sans-serif">
<text x="480" y="28" font-size="15" fill="#111" text-anchor="middle" font-weight="bold">Sơ đồ 5 — Ranh giới chuyển giao Authority giữa hai bậc</text>
<rect x="120" y="60.0" width="500" height="22.700000000000003" fill="#fdecea" fill-opacity="0.7"/>
<rect x="120" y="82.7" width="500" height="70.60000000000001" fill="#fff3e0" fill-opacity="0.7"/>
<rect x="120" y="153.3" width="500" height="56.0" fill="#fef9e6" fill-opacity="0.7"/>
<rect x="120" y="209.3" width="500" height="42.69999999999999" fill="#eaf7ee" fill-opacity="0.7"/>
<rect x="120" y="252.0" width="500" height="82.69999999999999" fill="#e8f0fe" fill-opacity="0.7"/>
<rect x="120" y="334.7" width="500" height="87.30000000000001" fill="#eaf7ee" fill-opacity="0.7"/>
<rect x="120" y="60.0" width="500" height="393.3" fill="none" fill-opacity="1.0" stroke="#555" stroke-width="1.3"/>
<line x1="120" y1="82.7" x2="634" y2="82.7" stroke="#c0392b" stroke-width="1.6"/>
<line x1="634" y1="82.7" x2="648" y2="95" stroke="#ccc" stroke-width="1"/>
<text x="652" y="91" font-size="11.3" fill="#c0392b" text-anchor="start" font-weight="bold">HARD BOUNDARY — 1.1426</text>
<text x="652" y="106" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">External invalidation: displacement + D1 close</text>
<text x="652" y="118" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">qua đây</text>
<line x1="120" y1="153.3" x2="634" y2="153.3" stroke="#e08e0b" stroke-width="1.6" stroke-dasharray="5,4"/>
<line x1="634" y1="153.3" x2="648" y2="145.3" stroke="#ccc" stroke-width="1"/>
<text x="652" y="141.3" font-size="11.3" fill="#e08e0b" text-anchor="start" font-weight="bold">OBSERVATION — 1.1320</text>
<text x="652" y="156.3" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">Wick reject H1 [OPEN] — cần sweep + CISD/MSS</text>
<text x="652" y="168.3" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">để xác nhận</text>
<line x1="120" y1="209.3" x2="634" y2="209.3" stroke="#c9a227" stroke-width="1.6" stroke-dasharray="5,4"/>
<line x1="634" y1="209.3" x2="648" y2="203.3" stroke="#ccc" stroke-width="1"/>
<text x="652" y="199.3" font-size="11.3" fill="#c9a227" text-anchor="start" font-weight="bold">TAKEN — 1.1236</text>
<text x="652" y="214.3" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">BSL nội bộ đã bị xuyên qua, không còn là biên</text>
<line x1="120" y1="252.0" x2="634" y2="252.0" stroke="#2563eb" stroke-width="1.6" stroke-dasharray="5,4"/>
<line x1="634" y1="252.0" x2="648" y2="261.3" stroke="#ccc" stroke-width="1"/>
<text x="652" y="257.3" font-size="11.3" fill="#2563eb" text-anchor="start" font-weight="bold">SOFT BOUNDARY — EQ 1.1172</text>
<text x="652" y="272.3" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">Bắt đầu premium, chưa phải handoff</text>
<line x1="120" y1="334.7" x2="634" y2="334.7" stroke="#c0392b" stroke-width="1.6" stroke-dasharray="5,4"/>
<line x1="634" y1="334.7" x2="648" y2="326.7" stroke="#ccc" stroke-width="1"/>
<text x="652" y="322.7" font-size="11.3" fill="#c0392b" text-anchor="start" font-weight="bold">INTERNAL INVALIDATION — 1.1048</text>
<text x="652" y="337.7" font-size="9.4" fill="#666" text-anchor="start" font-weight="normal">Bias nội bộ (C6) chết nếu D1 đóng dưới đây</text>
<rect x="155" y="226.7" width="190" height="-73.39999999999998" fill="#888" fill-opacity="0.24" stroke="#555" stroke-width="1" stroke-dasharray="3,2"/>
<text x="250" y="184.0" font-size="10" fill="#333" text-anchor="middle" font-weight="bold">Bearish FVG/OB (Brexit)</text>
<text x="250" y="198.0" font-size="9.8" fill="#8a4b00" text-anchor="middle" font-weight="normal" font-style="italic">vị trí CHƯA XÁC ĐỊNH</text>
<text x="250" y="211.0" font-size="9.2" fill="#8a4b00" text-anchor="middle" font-weight="normal" font-style="italic">(cần H1 zoom nến Brexit)</text>
<text x="480" y="600" font-size="11.5" fill="#111" text-anchor="middle" font-weight="bold">Giá hiện tại 1.1262 -&gt; trong vùng OBSERVATION, chưa chạm HARD boundary</text>
</svg>

---

## 7. Quy trình chuẩn D1 → H1 → M5 (đã sửa sau audit)

Phát biểu gốc của người dùng ("D1: chỉ cần xác định dealing range rồi bias nội bộ, thế thôi") bị audit đánh **BROKEN** vì tự mâu thuẫn với chính nhận định trước đó rằng cấu trúc lớn vẫn có tiếng nói. Quy trình đã sửa:

1. **D1 — External trước:** xác định external dealing range + DOL bậc lớn + array nào đang chặn trên/dưới.
2. **D1 — Internal sau:** trong range đó, xác định dealing range của leg giá hiện tại + bias nội bộ qua sweep + displacement + MSS.
3. **Định vị leg nội bộ trong external range:** premium hay discount? Nếu premium sâu (như hiện tại, ~67.8% external / ~79% internal), bias nội bộ chỉ còn cho biết **hướng draw**, không còn cho biết **giá tốt để vào** — quyền ưu tiên đang gần chuyển giao lại cho bậc lớn.
4. **H1:** xác nhận CISD/MSS trong chính dealing range nội bộ.
5. **M5:** thực thi tại PD array lộ ra trên H1.

Nguyên tắc rút ra: **mỗi lần đọc bias của leg hiện tại phải kèm câu hỏi "leg này đang ở premium/discount của range nào lớn hơn nó, và range đó đang chỉ về HTF array nào" — bỏ câu hỏi đó là quay lại đúng lỗi self-contradiction đã bị audit bắt.**

---

## 8. Falsification Tests còn mở

| Test | Đóng objection | Điều kiện | Chưa thực hiện được vì |
|---|---|---|---|
| T1 | O1 | OHLC readout chính xác đáy tháng 7 vs đáy đầu tháng 8 trên FXReplay | Ảnh H1 gửi lại cùng độ zoom với ảnh gốc, không phân giải thêm được |
| T2 | O2 | H1/M15 cửa sổ Jul 25 → Aug 5 để kiểm imbalance 3 nến tại 1.1075–1.1108 | H1 đã gửi bắt đầu từ Aug 4 05:00 — đoạn hình thành box nằm ngoài mép trái cửa sổ |
| T3 | O3 | ≥20 case backtest "bias tại EQ ±5%, vẫn tuyên bố primary" — tỷ lệ chạm DOL trước invalidation | Cần dữ liệu journal dài hạn, ngoài phạm vi một phiên chart |
| — | Vị trí Bearish FVG/OB Brexit | H1/M5 zoom đoạn hình thành nến giảm Brexit cuối tháng 6/2016 | Chưa được cung cấp trong phiên — đây là mảnh còn thiếu quan trọng nhất cho §6 |

---

## 9. Action Items

- [ ] Đọc readout giá chính xác đáy tháng 7 vs đáy đầu tháng 8 trên FXReplay (đóng T1/O1)
- [ ] Trích xuất H1 cửa sổ Jul 25 – Aug 5 để kiểm imbalance 3 nến tại 1.1075–1.1108 (đóng T2/O2)
- [ ] Trích xuất H1/M5 zoom đoạn hình thành nến giảm Brexit để định vị bearish FVG/OB (đóng vùng "chưa xác định" ở §6)
- [ ] Viết lại quy trình D1 thành 3 bước đúng thứ tự: external structure + DOL → dealing range nội bộ + premium/discount → bias nội bộ (đã áp dụng ở §7)
- [ ] Định nghĩa bằng số invalidation cho stance "ưu tiên long" hiện tại (đóng O8 — objection fatal duy nhất của phiên)
- [ ] Cố định một evidence bar duy nhất cho flip bias, dùng chung cho cả hai chiều bull/bear (đóng O9)
- [ ] Tag các case "long tại premium-on-premium" và "bias unclear tại EQ" trong journal để chạy T3 dài hạn

---

## 10. Registry Claim đầy đủ (C1–C11)

| Claim | Nội dung | Trạng thái |
|---|---|---|
| C1 | External dealing range 1.1426–1.0917, EQ ≈ 1.1172 | PASS |
| C2 | Giá 1.1150 ≈ EQ → premium/discount trung tính | PASS (điều kiện: dùng external range) |
| C3 | Đáy ~1.0950 sweep các đáy tháng 7 | UNSUPPORTED |
| C4 | Leg 1.0950→1.1236 là displacement + MSS nội bộ | **PASS — load-bearing** |
| C5 | Pullback 1.1045 = OTE; box 1.1075–1.1108 = FVG/OB được tôn trọng | UNSUPPORTED |
| C6 | Bias chính bullish trong range, khi 1.1048 còn giữ | Chỉ đứng nhờ C4, không đứng độc lập |
| C7 | Invalidation: D1 đóng dưới 1.1048 | PASS |
| C8 | Quy trình D1: chỉ cần dealing range + bias nội bộ | BROKEN (self-contradiction, O6) |
| C9 | LTF (H1/M5) có bị chi phối bởi HTF (D1) không | Đúng — xác nhận nested hierarchy |
| C10 | Bias nội bộ bullish hiện tại → ưu tiên long | BROKEN nếu phát biểu vô điều kiện (O7); PASS nếu điều kiện hóa theo premium/discount |
| C11 | Bias nội bộ chỉ đổi bearish khi quét BSL tạo MSS | Thiếu chuẩn đối xứng với flip bull (O9); "sweep tạo thành MSS" sai thuật ngữ (O10) |

---

## Giới hạn của tài liệu này

- Toàn bộ đường kẻ, box do người dùng vẽ trên chart (BSL/SSL, FVG/OB, ba đường đỏ H1) là **claim**, không phải **evidence** — được giữ nguyên phân biệt này trong mọi sơ đồ minh họa (nhãn `[UNVERIFIED]`/`[OPEN]` ở Sơ đồ 1 và 5).
- Audit chạy không có JSON extraction từ `extract-screenshot-data` — finding LOGIC/CONSISTENCY được ground đầy đủ; finding EVIDENCE là tạm định.
- Doctrine ruling neo vào bảng định nghĩa nhanh (quick-table) vì `doctrine.md` đầy đủ không có trong checkout skill tại thời điểm phiên này.
- Tài liệu không đưa ra khuyến nghị giao dịch (long/short/entry/stop/target) — đây là bản tổng hợp phân tích cấu trúc và audit lập luận, không phải trade plan.
