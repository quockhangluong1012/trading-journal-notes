# LỘ TRÌNH TOÀN DIỆN: TỪ SỐ 0 VỚI ICT → PASS FTMO 100K & THE5ERS 100K

> Phiên bản: 08/2026 · Định hướng: ICT 2022 Model · Thời lượng thực tế: **12–18 tháng** (có thể rút xuống 9–12 tháng nếu học toàn thời gian, hoặc kéo dài 24 tháng nếu vừa học vừa làm — cả hai đều bình thường).
>
> Nguyên tắc xuyên suốt: **Bạn không "thi pass quỹ". Bạn xây một hệ thống giao dịch có kỳ vọng dương + kỷ luật thi hành, rồi việc pass quỹ chỉ là hệ quả.** Tỷ lệ pass FTMO toàn thị trường chỉ khoảng 8–10% ([TradeNinety](https://tradeninety.com/blog/how-to-pass-ftmo-challenge-2026/)) — gần như toàn bộ người trượt là do vi phạm quản trị rủi ro, không phải do thiếu kiến thức.

---

## BẢN ĐỒ TỔNG QUAN 6 GIAI ĐOẠN

| Giai đoạn | Thời gian gợi ý | Mục tiêu cốt lõi | Điều kiện "tốt nghiệp" (Gate) |
|---|---|---|---|
| **GĐ1 — Nền tảng thị trường + ngôn ngữ ICT** | Tháng 1–3 | Hiểu và nhận diện đúng mọi khái niệm ICT trên chart nguội | Vượt bài kiểm tra nhận diện 50 chart, đúng ≥ 90% thuật ngữ |
| **GĐ2 — Master ICT 2022 Model + Backtest** | Tháng 3–7 | Thuộc thuật toán 2022 Model, backtest ≥ 200 setup có nhật ký | Backtest cho thấy expectancy dương ổn định trên ≥ 200 mẫu |
| **GĐ3 — Forward test Demo (giao dịch thật, tiền giả)** | Tháng 7–10 | Thi hành hệ thống trong điều kiện thời gian thực | 3 tháng demo liên tiếp có lãi, tuân thủ kế hoạch ≥ 95% |
| **GĐ4 — Mô phỏng Challenge + Tâm lý thi đấu** | Tháng 10–12 | Trade demo theo ĐÚNG luật FTMO/The5ers như thi thật | Pass ≥ 2 lần mô phỏng challenge liên tiếp trên demo |
| **GĐ5 — Thi thật: FTMO 100K & The5ers 100K** | Tháng 12–15 | Pass Phase 1 → Phase 2 → Funded ở cả hai quỹ | Nhận tài khoản funded |
| **GĐ6 — Funded: Sống sót, payout, scaling** | Tháng 15+ | Rút tiền đều đặn, scale vốn | Payout đầu tiên + không vi phạm luật trong 90 ngày |

**Quy tắc chuyển giai đoạn:** KHÔNG được nhảy cóc. Mỗi Gate là điều kiện cứng. Trượt Gate → ở lại giai đoạn đó thêm 4 tuần rồi kiểm tra lại. Tiền mua challenge chỉ được chi khi qua Gate 4.

---

# GIAI ĐOẠN 1 (Tháng 1–3): NỀN TẢNG THỊ TRƯỜNG + NGÔN NGỮ ICT

## 1.1. Tuần 1–2: Nền tảng thị trường thô (bắt buộc, đừng bỏ qua)

Trước khi học ICT, phải hiểu "sân chơi":

- **Cơ chế thị trường:** bid/ask, spread, lệnh market/limit/stop, khớp lệnh, slippage, swap, commission.
- **Các phiên giao dịch:** Asia (07:00–13:00 GMT+7), London (14:00–17:00), New York (19:30–23:00) — giờ Việt Nam. Đặc tính thanh khoản từng phiên.
- **Sản phẩm:** FX majors (EURUSD, GBPUSD), chỉ số (US30, NAS100), vàng (XAUUSD). *Khuyến nghị: chọn 1–2 cặp duy nhất cho toàn bộ lộ trình (ví dụ EURUSD + NAS100 hoặc chỉ XAUUSD) — đừng học dàn trải.*
- **Nến, khung thời gian, cách đọc chart TradingView, đo pips/points, tính khối lượng lot theo % rủi ro.**
- **Toán rủi ro cơ bản:** risk per trade, RR (risk:reward), win rate, expectancy = (WinRate × AvgWin) − (LossRate × AvgLoss). Học thuộc công thức này — nó là "hiến pháp" của toàn lộ trình.

**Bài tập tuần 1–2:** Tự tính bằng tay 20 ví dụ về khối lượng lot: "Tài khoản 100k, rủi ro 0.5%, stop loss 12 pips EURUSD → lot bao nhiêu?" Phải làm nhanh và đúng 100%.

## 1.2. Tuần 3–6: Khối khái niệm ICT lõi — học theo đúng thứ tự này

Nguồn học chuẩn: **ICT 2022 Mentorship (YouTube, miễn phí, ~41 video)** làm xương sống + Core Content tham chiếu khi cần đào sâu. Học theo cụm khái niệm, mỗi cụm 3–5 ngày, cuối mỗi cụm phải đánh dấu được khái niệm đó trên 20 chart lịch sử.

**Cụm A — Thanh khoản (Liquidity), nền tảng của mọi thứ:**
- Buyside Liquidity (BSL) / Sellside Liquidity (SSL): cụm stop nằm trên đỉnh cũ / dưới đáy cũ.
- Equal highs / Equal lows (EQH/EQL) — thanh khoản "được vẽ ra để bị lấy".
- Liquidity sweep / stop hunt / raid: giá quét qua đỉnh/đáy rồi đảo chiều — khác với break thật như thế nào.
- Khái niệm "Smart Money" săn thanh khoản: thị trường đi từ vùng thanh khoản này đến vùng thanh khoản khác.

**Cụm B — Cấu trúc thị trường (Market Structure):**
- Swing high/low đúng chuẩn ICT (3 nến).
- Break of Structure (BOS) — tiếp diễn xu hướng; Market Structure Shift (MSS) — tín hiệu đảo chiều **chỉ có giá trị khi đi kèm displacement**.
- CISD (Change In State of Delivery), sự khác nhau giữa MSS và CISD.
- Displacement: nến thân lớn, dứt khoát, để lại FVG — dấu hiệu của lệnh tổ chức.

**Cụm C — PD Arrays (mảng Premium/Discount):**
- **Fair Value Gap (FVG)**: định nghĩa 3 nến, cách giá "rebalance" về FVG; Inversion FVG.
- **Order Block (OB)**: nến ngược chiều cuối cùng trước displacement; điều kiện OB hợp lệ.
- Breaker Block, Mitigation Block, Rejection Block (mức độ ưu tiên thấp hơn — học sau).
- Thứ tự ưu tiên PD array trong 2022 Model: **FVG là công cụ vào lệnh chính**, OB là hỗ trợ.

**Cụm D — Dealing Range, Premium/Discount, OTE:**
- Dealing range: từ swing low đến swing high sau một cú sweep có displacement.
- Equilibrium (50%): trên = premium (vùng bán), dưới = discount (vùng mua). **Chỉ mua ở discount, chỉ bán ở premium** — vi phạm điều này là lỗi doctrine nặng nhất của người mới.
- OTE (Optimal Trade Entry): vùng fib 0.62–0.79 của chân displacement.

**Cụm E — Thời gian (Time) — ICT là "Time THEN Price":**
- Killzones: **London KZ 02:00–05:00 EST (14:00–17:00 VN), New York AM KZ 08:30–11:00 EST (20:30–23:00 VN)**, NY PM KZ. Người Việt đi làm ban ngày nên NY AM killzone (buổi tối VN) thường là lựa chọn thực tế nhất.
- Midnight open (00:00 EST), 08:30 open; True Day; Judas Swing (cú lừa đầu phiên).
- Power of Three (PO3 / AMD): Accumulation → Manipulation → Distribution trong ngày/tuần.
- Weekly profile cơ bản: thứ Ba/Tư thường tạo high/low tuần.

**Cụm F — Liên khung thời gian (Top-down):**
- HTF (D1/H4) cho bias và dealing range → H1/M15 cho cấu trúc và vùng POI → M5/M1 cho tín hiệu vào lệnh.
- Quy tắc "HTF là luật, LTF là cửa vào": không bao giờ trade ngược bias HTF trong giai đoạn học.

## 1.3. Tuần 7–12: Luyện nhận diện + kiểm định bằng công cụ trong Project này

Mỗi ngày 45–90 phút, mở chart lịch sử (chức năng Replay của TradingView):

1. Chọn ngẫu nhiên 1 ngày trong quá khứ, đánh dấu: dealing range HTF, premium/discount, BSL/SSL, sweep, displacement, MSS/CISD, FVG, OB, killzone.
2. **Chụp screenshot D1/H1/M5 và đưa vào phiên chat này** — tôi sẽ chạy trích xuất ICT-VISION (skill `extract-screenshot-data`) để đối chiếu JSON dữ kiện khách quan với những gì bạn tự đánh dấu.
3. Viết phân tích ngắn (5–10 câu) rồi yêu cầu tôi **kiểm định doctrine** (skill `ict-doctrine`) — bạn sẽ biết ngay mình gọi sai thuật ngữ nào, overcall chỗ nào.
4. Ghi lỗi vào "Sổ lỗi khái niệm". Lỗi nào lặp ≥ 3 lần → quay lại video gốc học lại cụm đó.

**GATE 1 — Điều kiện qua Giai đoạn 1:**
- [ ] Tự đánh dấu đúng ≥ 90% các thành phần trên 50 chart nguội (dùng vòng lặp kiểm định ở trên để chấm).
- [ ] Trả lời trôi chảy: "Khác nhau giữa BOS và MSS?", "Khi nào FVG hợp lệ?", "Tại sao chỉ mua ở discount?", "Sweep khác break thật ở điểm nào?"
- [ ] Thuộc lịch killzone theo giờ Việt Nam.

---

# GIAI ĐOẠN 2 (Tháng 3–7): MASTER ICT 2022 MODEL + BACKTEST CÓ HỆ THỐNG

## 2.1. Thuật toán 2022 Model — quy trình cứng từng bước

Đây là checklist thi hành, in ra dán trước màn hình:

**Bước 1 — HTF Bias (D1/H4, làm cuối tuần + cập nhật mỗi sáng):**
1. Xác định dealing range D1 hiện hành (swing low → swing high gần nhất có sweep + displacement).
2. Giá đang ở premium hay discount của range đó?
3. Draw on Liquidity (DOL): mục tiêu thanh khoản HTF kế tiếp là gì (old high/low, FVG D1 chưa lấp)?
4. Kết luận bias: **chỉ Long, chỉ Short, hoặc ĐỨNG NGOÀI** (bias không rõ = không trade, đây cũng là một vị thế).

**Bước 2 — Bối cảnh H1/M15:**
5. Trong killzone, chờ giá tiếp cận vùng thanh khoản ngược bias (ví dụ bias short → chờ giá quét BSL/old high M15).
6. Xác nhận sweep: giá đâm qua đỉnh/đáy thanh khoản rồi từ chối.

**Bước 3 — Tín hiệu M5/M1:**
7. Sau sweep, chờ **MSS/CISD kèm displacement** ngược hướng sweep (thân nến lớn, phá swing gần nhất, để lại FVG).
8. Vào lệnh tại **FVG của chân displacement** (hoặc OTE 0.62–0.79 nếu FVG quá nông).
9. Stop loss: trên/dưới đỉnh/đáy của cú sweep (thêm buffer spread).
10. Target: thanh khoản đối diện gần nhất (TP1) và DOL HTF (TP2). RR tối thiểu chấp nhận: **1:2**; dưới 1:2 → bỏ lệnh.

**Bước 4 — Quản lý lệnh:**
11. TP1 chốt 50% + dời SL về entry (breakeven) khi giá đi được 1R.
12. Không dời SL rộng ra, không trung bình giá, không "gồng" quá DOL.

## 2.2. Quy trình Backtest chuẩn (mục tiêu: ≥ 200 setup)

**Công cụ:** TradingView Replay (bản trả phí đáng tiền ở giai đoạn này) hoặc FX Replay/Fenix. Sổ nhật ký: Notion/Google Sheets.

**Cách chạy:**
- Mỗi phiên backtest = 1 ngày giao dịch lịch sử, chạy replay đúng trình tự thời gian (không tua biết trước).
- Chỉ backtest 1–2 cặp đã chọn, chỉ trong killzone đã chọn.
- Mỗi setup ghi đủ 15 trường: ngày, cặp, phiên/killzone, bias HTF (+lý do), thanh khoản bị quét, có displacement không, loại entry (FVG/OTE/OB), RR kế hoạch, kết quả (R), thời gian giữ lệnh, tuân thủ checklist (Y/N từng bước), lỗi nếu có, cảm xúc giả định, ảnh chart trước/sau, bài học 1 câu.
- **Chuẩn khối lượng: 10–15 setup/tuần × 16–20 tuần = 200–300 setup.** Đây là phần tốn công nhất toàn lộ trình và cũng là phần quyết định nhất.

**Phân tích số liệu mỗi 50 setup:**
- Win rate, average RR, expectancy (đơn vị R), max losing streak, phân bố lãi theo ngày trong tuần / theo killzone / theo loại setup.
- Cắt bỏ: loại setup/khung giờ có expectancy âm. Giữ lại: 1–2 "mẫu setup vàng" có thống kê tốt nhất → hệ thống của bạn hẹp lại và sắc hơn.

**Vòng lặp kiểm định trong Project (điểm khác biệt của bạn so với người tự học):**
1. Sau mỗi tuần backtest, chọn 3 setup tiêu biểu → chụp D1/H1/M5 → tôi trích xuất JSON dữ kiện (ICT-VISION).
2. Nộp phân tích của bạn + JSON → tôi chạy **audit** (skill `ict-audit`): tách rõ claim nào bị dữ liệu phủ nhận, claim nào không đủ bằng chứng, dữ kiện bất lợi nào bạn lờ đi.
3. Mỗi tháng 1 lần, đưa loạt backtest tốt nhất cho tôi **phản biện kiểu devil's advocate** (skill `ict-devils-advocate`) — xây case đối lập mạnh nhất từ chính chart của bạn. Sống sót qua phản biện = setup thật; không sống sót = hindsight bias.

**GATE 2 — Điều kiện qua Giai đoạn 2:**
- [ ] ≥ 200 setup backtest có nhật ký đầy đủ.
- [ ] Expectancy ≥ +0.3R/lệnh ổn định trên 100 setup gần nhất; win rate ≥ 40% với RR trung bình ≥ 1:2 (hoặc tương đương).
- [ ] Biết rõ max losing streak lịch sử của hệ thống (thường 5–8 lệnh) — con số này quyết định risk per trade ở giai đoạn thi.
- [ ] Có văn bản **Trading Plan v1** (xem mục 3.1).

---

# GIAI ĐOẠN 3 (Tháng 7–10): FORWARD TEST DEMO — GIAO DỊCH THỜI GIAN THỰC

## 3.1. Viết Trading Plan hoàn chỉnh (văn bản, có chữ ký của chính bạn)

Nội dung bắt buộc:
1. **Thị trường & khung giờ:** cặp nào, killzone nào, ngày nào trong tuần (khuyến nghị bỏ thứ Hai đầu phiên Á và thứ Sáu sau tin nếu thống kê backtest xấu).
2. **Định nghĩa setup hợp lệ:** checklist 2022 Model ở mục 2.1, kèm ảnh mẫu "setup vàng".
3. **Risk model:** rủi ro cố định mỗi lệnh (đề xuất **0.5% giai đoạn demo**, sẽ giảm còn 0.25–0.5% khi thi), tối đa **2 lệnh/ngày**, daily stop **−1%** (thua tới −1% trong ngày → tắt máy), weekly stop **−2.5%**.
4. **Quy tắc quản lý lệnh:** BE tại 1R, chốt 50% tại TP1, không gồng qua DOL.
5. **Quy tắc hành vi:** không trade ngoài killzone, không trade khi mất ngủ/say/giận, không xem chart sau khi đóng lệnh cuối ngày, nghỉ 1 ngày sau 3 lệnh thua liên tiếp.
6. **Nhật ký:** bắt buộc ghi trước-khi-vào-lệnh (lý do vào theo checklist), không được ghi hồi tố.

## 3.2. Thi hành 3 tháng demo

- Tài khoản demo **100.000 USD** (đúng kích thước sẽ thi), đòn bẩy 1:100, trên MT5 (The5ers dùng MT5 Hedge; FTMO có MT4/MT5/cTrader/DXtrade — chọn MT5 để dùng chung) ([The5ers](https://the5ers.com/high-stakes/), [TraderNotion](https://www.tradernotion.com/blog/how-to-pass-the-ftmo-challenge-rules-math-strategy-2026)).
- KPI theo dõi hằng tuần: expectancy, tuân thủ checklist (%), số lệnh ngoài kế hoạch (mục tiêu = 0), max DD.
- **Điểm tuân thủ quan trọng hơn lợi nhuận.** Tháng lãi 5% nhưng có 4 lệnh phá kế hoạch = tháng THẤT BẠI. Tháng lãi 1.5% với 100% tuân thủ = tháng thành công.
- Tiếp tục vòng lặp audit/phản biện hằng tuần với các skill trong Project như ở GĐ2, nhưng giờ áp lên lệnh forward thật.

## 3.3. Xây "hồ sơ tâm lý" của chính bạn

Ghi nhận qua nhật ký: bạn thuộc kiểu lỗi nào? (a) revenge trading sau thua, (b) fomo nhảy lệnh sớm trước displacement, (c) chốt non vì sợ, (d) gồng lỗ vì hy vọng. Mỗi kiểu có "phanh" riêng — ví dụ kiểu (a): quy tắc cứng "sau lệnh thua, đứng dậy 15 phút, không nhìn chart". Giai đoạn thi quỹ, kẻ giết bạn không phải thị trường mà là chính các pattern này.

**GATE 3 — Điều kiện qua Giai đoạn 3:**
- [ ] 3 tháng demo liên tiếp: mỗi tháng ≥ +1%, tổng ≥ +6%, max DD < 4%, không ngày nào chạm −2%.
- [ ] Tuân thủ kế hoạch ≥ 95% số lệnh (đếm bằng nhật ký).
- [ ] Max losing streak thực tế không vượt quá streak backtest + 2.

---

# GIAI ĐOẠN 4 (Tháng 10–12): MÔ PHỎNG CHALLENGE — TẬP THI TRƯỚC KHI THI

## 4.1. Tại sao cần giai đoạn này

Trade demo tự do và trade dưới luật drawdown của quỹ là hai môn thể thao khác nhau. Ở đây bạn tập chịu đúng các ràng buộc: **daily loss tính theo equity (lỗ nổi cũng tính)**, sàn drawdown tĩnh, và áp lực "tiền phí đã bỏ ra". FTMO tính daily loss theo equity gồm cả vị thế đang mở — bạn có thể vi phạm ngay cả khi chưa đóng lệnh ([TradeNinety](https://tradeninety.com/blog/how-to-pass-ftmo-challenge-2026/)).

## 4.2. Cách mô phỏng

- Dùng FTMO **Free Trial** (miễn phí, không giới hạn thời gian, tới 200k) để quen nền tảng và dashboard đo drawdown của chính FTMO ([FTMO](https://ftmo.com/en/how-it-works/)).
- Chạy 2 vòng mô phỏng, mỗi vòng theo đúng bộ luật ở Phần 5 dưới đây: vòng 1 theo luật FTMO 2-step, vòng 2 theo luật The5ers High Stakes (tự giám sát 3 ngày lời ≥ 0.5%).
- Risk per trade trong mô phỏng: **0.25–0.5%**, daily stop cá nhân **−1.5%** (tự đặt chặt hơn luật −5% của quỹ rất xa — không bao giờ để luật quỹ là phòng tuyến đầu tiên).

**GATE 4 — Điều kiện mua challenge thật:**
- [ ] Pass 2 vòng mô phỏng liên tiếp (đạt target, không chạm bất kỳ giới hạn nào, kể cả giới hạn cá nhân).
- [ ] Có sẵn quỹ dự phòng cho **tối thiểu 2–3 lần phí mỗi quỹ** (FTMO 100k: €540/lần; The5ers 100k High Stakes: ~$495–545/lần — kiểm tra giá tại thời điểm mua) ([TraderNotion](https://www.tradernotion.com/blog/ftmo-rule-changes-2026)). Tâm lý "chỉ đủ tiền thi 1 lần" là công thức thất bại.

---

# PHẦN 5: LUẬT CHI TIẾT HAI QUỸ (SỐ LIỆU CHO TÀI KHOẢN 100K)

> ⚠️ Luật prop firm thay đổi thường xuyên. Trước khi bấm mua, đọc lại trang Trading Objectives chính thức và FAQ của từng quỹ. Số liệu dưới đây cập nhật đến 08/2026.

## 5.1. FTMO 100K — 2-Step (khuyến nghị cho lần thi đầu)

| Hạng mục | Phase 1 (Challenge) | Phase 2 (Verification) | FTMO Account (funded) |
|---|---|---|---|
| Profit target | **10% = $10.000** | **5% = $5.000** | Không có target |
| Max Daily Loss | 5% = $5.000 | 5% = $5.000 | 5% |
| Max Loss (tổng) | 10% = $10.000, **tĩnh** (equity không bao giờ được chạm $90.000) | 10% | 10% |
| Số ngày giao dịch tối thiểu | 4 ngày | 4 ngày | — |
| Giới hạn thời gian | **Không giới hạn** | Không giới hạn | — |
| Profit split | — | — | **90/10**, hoàn 100% phí ở lần rút đầu |

([FTMO](https://ftmo.com/en/how-it-works/), [TraderNotion](https://www.tradernotion.com/blog/how-to-pass-the-ftmo-challenge-rules-math-strategy-2026))

**Chi tiết sống còn về cách tính:**
- **Daily loss tính theo EQUITY** (gồm lỗ nổi + phí + swap), mốc reset lúc **nửa đêm CET** dựa trên balance/equity thời điểm đó. Ví dụ: balance lúc nửa đêm $103.000 → sàn vi phạm hôm sau là $98.000 ([Tanto](https://tradetanto.com/learn/ftmo-rules-evaluation-process)).
- **Max loss là sàn tĩnh $90.000** tính từ balance ban đầu, không trail theo đỉnh — điểm dễ thở nhất của FTMO so với các quỹ trailing.
- News trading & giữ lệnh qua đêm/cuối tuần: **tự do trong 2 phase thi**; sang tài khoản funded loại Standard mới bị hạn chế (tin ±2 phút, không giữ qua cuối tuần) — muốn swing thì chọn **Swing account** ngay từ đầu ([FTMO](https://ftmo.com/en/how-it-works/)).
- EA/copy trade từ chính mình: được phép nếu không khai thác lỗi giá.
- Trượt Phase 1 nhưng không vi phạm max loss (hết kiên nhẫn, tự bỏ): có cơ chế **Retry miễn phí** trong một số điều kiện; luôn đọc điều khoản hiện hành.

**FTMO 1-Step (tuỳ chọn mới từ 02/2026, KHÔNG khuyến nghị cho lần đầu):** target 10% một phase duy nhất, nhưng daily loss chỉ **3%**, max loss 10% **trailing theo ngày** (tính trên balance đóng ngày cao nhất, cập nhật lúc 23:59:59 CET, chỉ đi lên), kèm **Best Day Rule 50%** (không ngày nào được chiếm quá 50% tổng lợi nhuận). Split 90% từ payout đầu ([Tanto](https://tradetanto.com/learn/ftmo-rules-evaluation-process), [TraderNotion](https://www.tradernotion.com/blog/ftmo-rule-changes-2026)). Chỉ cân nhắc khi bạn đã pass 2-step ít nhất một lần.

## 5.2. The5ers 100K — High Stakes (2-Step)

| Hạng mục | Step 1 | Step 2 | Funded |
|---|---|---|---|
| Profit target | **10% = $10.000**¹ | **5% = $5.000** | 10% mỗi nấc để scale |
| Max Daily Loss | 5% = $5.000 — **chạm là cháy tài khoản** | 5% | 5% |
| Max Loss (tổng) | 10% = $10.000 | 10% | 10% |
| Ngày tối thiểu | **3 ngày CÓ LỜI** (mỗi ngày lời ≥ 0.5% = $500 tính trên lệnh đã đóng) | 3 ngày có lời | 3 ngày có lời mỗi nấc scale |
| Thời gian | Không giới hạn (nhưng **30 ngày không giao dịch → tài khoản hết hạn**) | Không giới hạn | — |
| Profit split | — | — | **80% → 100%** theo nấc scaling tới $500K, kèm thưởng cố định $4.000–10.000 ở các nấc cao |

¹ Trang chính thức hiện niêm yết Step 1 = 10% (một số tài liệu cũ ghi 8% — luôn xác nhận trên dashboard lúc mua). ([The5ers](https://the5ers.com/high-stakes/))

**Chi tiết sống còn:**
- **"Ngày có lời"** = min(balance, equity) lúc nửa đêm − balance ngày trước ≥ +0.5% vốn gốc. Nghĩa là bạn KHÔNG thể pass bằng 1 cú ăn đậm duy nhất — phải dàn lợi nhuận ra ≥ 3 ngày, mỗi ngày ≥ $500.
- **Không được đặt/đóng lệnh trong khung ±2 phút quanh tin tác động mạnh** (được giữ lệnh xuyên tin). Đây là khác biệt lớn với FTMO phase thi — đặt lịch tin ForexFactory làm mặc định.
- Giữ lệnh qua đêm/cuối tuần: được phép (chỉ số qua cuối tuần chịu swap cao).
- Nền tảng: MT5 Hedge, đòn bẩy 1:100 ([The5ers](https://the5ers.com/high-stakes/)).

## 5.3. So sánh nhanh — điều chỉnh chiến thuật giữa hai quỹ

| Điểm khác | FTMO 2-Step | The5ers High Stakes | Hệ quả chiến thuật |
|---|---|---|---|
| Ngày tối thiểu | 4 ngày giao dịch (chỉ cần có lệnh) | 3 ngày **có lời ≥0.5%** | Với The5ers: kế hoạch phải nhắm "nhiều ngày lời vừa phải", không dồn 1 ngày |
| Tin tức khi thi | Tự do | Cấm khớp lệnh ±2 phút quanh tin đỏ | Với The5ers: không entry sát giờ tin |
| Split khởi điểm | 90% | 80% (lên dần 100%) | FTMO trả tốt hơn giai đoạn đầu |
| Hoàn phí | 100% ở payout đầu | Theo chính sách từng thời điểm | — |
| Drawdown | Tĩnh cả hai | Tĩnh theo niêm yết | Giống nhau: sàn $90.000 |

---

# GIAI ĐOẠN 5 (Tháng 12–15): THI THẬT — KẾ HOẠCH TÁC CHIẾN CỤ THỂ

## 5A. Trình tự khuyến nghị

1. **Thi FTMO 100K trước** (luật dễ thở hơn: không yêu cầu ngày-có-lời, news tự do khi thi).
2. Pass FTMO Phase 1 → trong lúc chờ/trade Phase 2, **mua The5ers 100K** và chạy song song (hai tài khoản cùng hệ thống, cùng lệnh — lưu ý The5ers cấm khớp lệnh quanh tin nên lệnh sát tin chỉ đánh bên FTMO).
3. Không bao giờ chạy quá 2 challenge cùng lúc trong lần đầu.

## 5B. Kế hoạch rủi ro cho từng phase (con số cụ thể, tài khoản $100.000)

**Cấu hình chuẩn: risk 0.5%/lệnh = $500; tối đa 2 lệnh/ngày; daily stop cá nhân −1% = −$1.000; sau 2 ngày thua liên tiếp → nghỉ 1 ngày.**

| | Target | Số R cần (RR 1:2, WR 45%) | Số lệnh dự kiến | Thời gian dự kiến |
|---|---|---|---|---|
| FTMO Phase 1 | +$10.000 = 20R (risk 0.5%) | ~20R lãi ròng | 45–70 lệnh | 6–12 tuần |
| FTMO Phase 2 | +$5.000 = 10R | ~10R | 25–40 lệnh | 3–6 tuần |
| The5ers Step 1 | +$10.000, dàn ≥3 ngày lời | ~20R | 45–70 lệnh | 6–12 tuần |
| The5ers Step 2 | +$5.000 | ~10R | 25–40 lệnh | 3–6 tuần |

Toán an toàn: risk 0.5% → cần **20 lệnh thua liên tiếp** mới chạm max loss 10%, và **10 lệnh thua trong 1 ngày** mới chạm daily 5% — trong khi daily stop cá nhân của bạn đã chặn ở 2 lệnh. Xác suất cháy vì thị trường gần bằng 0; chỉ có thể cháy vì phá kỷ luật ([TradeNinety](https://tradeninety.com/blog/how-to-pass-ftmo-challenge-2026/)).

**Biến thể tăng tốc (chỉ dùng nếu Gate 4 pass thuyết phục):** 0.75% cho 2 lệnh đầu ngày khi có setup A+ đúng killzone; quay về 0.5% ngay khi tài khoản +3%.

**Quy tắc "về đích an toàn":**
- Đạt +8%: giảm risk còn 0.25%/lệnh. Đạt +9.5%: chỉ trade setup A+ hoàn hảo. Đừng bao giờ tăng size để "kết thúc cho nhanh" — đây là nguyên nhân trượt phổ biến nhất ở 2% cuối.
- Với The5ers: theo dõi bộ đếm "ngày có lời"; nếu đã đủ target mà mới có 2 ngày lời ≥0.5%, kế hoạch ngày còn lại là 1 lệnh nhỏ risk 0.25% nhắm +0.5–0.7% rồi dừng.
- Với FTMO: đủ target + đủ 4 ngày giao dịch → **DỪNG HẲN**, chờ kết quả. Không trade "cho vui".

## 5C. Nhịp vận hành một ngày thi (mẫu, killzone NY AM — giờ VN)

- **19:00–20:15:** Cập nhật bias D1/H4, đánh dấu dealing range + DOL, check lịch tin đỏ (nếu thi The5ers: khoanh khung cấm ±2'), viết kịch bản "nếu–thì" cho 2 tình huống.
- **20:30–23:00 (NY AM killzone):** Chỉ chờ đúng kịch bản: sweep → MSS + displacement M5 → entry FVG/OTE. Tối đa 2 lệnh. Hết killzone = hết ngày, kể cả chưa có lệnh nào (ngày không lệnh là ngày TỐT nếu không có setup).
- **23:15:** Ghi nhật ký 10 phút, chụp chart, chấm điểm tuân thủ. Tuyệt đối không mở lại chart sau đó.
- **Cuối tuần:** Tổng kết số liệu tuần + gửi 2–3 setup cho vòng audit/phản biện trong Project này.

## 5D. Danh sách "tử huyệt" — nguyên nhân trượt thực tế và phanh cụ thể

| # | Tử huyệt | Phanh |
|---|---|---|
| 1 | Vi phạm daily loss vì **lỗ nổi** (equity) khi ôm nhiều lệnh | Không bao giờ để tổng risk đang mở > 1%; tính cả lệnh đang chạy |
| 2 | Revenge trading sau lệnh thua đầu ngày | Thua lệnh 1 → nghỉ 15 phút; thua lệnh 2 → hết ngày (daily stop) |
| 3 | Tăng size khi gần target hoặc khi "cảm thấy nóng máy" | Size cố định ghi trong plan; mọi thay đổi size phải chờ sang tuần mới |
| 4 | Trade ngoài killzone vì sốt ruột "chưa đủ ngày" | Ngày giao dịch tối thiểu rất dễ đạt (4 ngày/3 ngày) — không bao giờ là lý do ép lệnh |
| 5 | Ôm lệnh qua tin đỏ (The5ers: khớp lệnh quanh tin là vi phạm) | Lịch tin là bước 1 của mọi phiên; The5ers: không entry trong 30' trước tin |
| 6 | Gap cuối tuần đâm thủng sàn drawdown | Trong phase thi: hạn chế giữ qua cuối tuần trừ khi lệnh đã +1R và dời BE |
| 7 | Phase 2 chủ quan ("dễ mà") rồi trade ẩu | Phase 2 giữ NGUYÊN quy trình, thậm chí giảm risk còn 0.25–0.4% vì chỉ cần 5% |
| 8 | Thi lại ngay sau khi trượt, trong trạng thái cay cú | Trượt → bắt buộc 2 tuần quay lại demo + audit toàn bộ lệnh của lần thi trước khi mua lại |

## 5E. Nếu trượt (kịch bản phải có sẵn)

1. Xuất toàn bộ lịch sử lệnh, phân loại: thua-đúng-hệ-thống (bình thường, không sửa gì) vs thua-do-phá-luật (đây mới là lỗi).
2. Nếu >20% lệnh là phá luật → quay về GĐ4 tối thiểu 4 tuần. Nếu hệ thống được tuân thủ mà vẫn âm → mang dữ liệu vào Project này chạy audit + devil's advocate để tìm lỗi hệ thống (thường là bias HTF sai quy trình hoặc chọn killzone không hợp múi giờ sinh hoạt).
3. Ngân sách đã dự phòng 2–3 lần phí — trượt 1 lần nằm trong kế hoạch, không phải thảm họa.

---

# GIAI ĐOẠN 6 (Tháng 15+): SAU KHI FUNDED

- **Tháng đầu funded:** giảm risk còn 0.25%/lệnh. Mục tiêu duy nhất: sống sót 30 ngày đầu + payout đầu tiên (dù nhỏ) để hoàn phí FTMO và "khóa" trạng thái tâm lý.
- **FTMO Standard account:** nhớ luật mới xuất hiện ở giai đoạn funded — hạn chế trade quanh tin ±2 phút và giữ lệnh qua cuối tuần (Swing account thì không bị) ([FTMO](https://ftmo.com/en/how-it-works/)).
- **The5ers scaling:** mỗi +10% (kèm 3 ngày lời) → nâng vốn theo nấc $100K → $125K → … → $500K, split tăng từ 80% lên 100% + thưởng cố định ([The5ers](https://the5ers.com/high-stakes/)).
- Nhịp payout: rút đều theo chu kỳ ngắn nhất được phép, đừng "nuôi" lợi nhuận trong tài khoản quỹ — tiền chưa rút chưa phải của bạn.
- Khi đã ổn định 3 tháng: cân nhắc thêm tài khoản/quỹ thứ ba để phân tán rủi ro "quỹ sập" — không bao giờ để toàn bộ thu nhập phụ thuộc một prop firm.

---

# PHỤ LỤC

## A. Khung thời gian học mỗi tuần (người đi làm)

- T2–T6: 60–90 phút/tối (lý thuyết hoặc backtest; GĐ3+ là phiên trade NY AM 20:30–23:00 VN).
- T7: 3–4 giờ (backtest khối lượng lớn + tổng kết tuần).
- CN: 1–2 giờ (bias tuần mới + gửi setup vào vòng kiểm định của Project).
- Tổng ~10–13 giờ/tuần. Dưới 8 giờ/tuần → nhân đôi thời lượng lộ trình, đó là đánh đổi bình thường, đừng rút bớt Gate.

## B. Tài nguyên học ICT theo thứ tự

1. ICT 2022 Mentorship (YouTube playlist chính chủ Michael J. Huddleston) — xương sống của GĐ1–2.
2. ICT Core Content (Month 1–4: liquidity, structure, PD arrays; xem chọn lọc khi cần đào sâu).
3. Market Maker Series / lectures về Time & Price cho GĐ2+.
4. Công cụ: TradingView (Replay), ForexFactory (lịch tin), FTMO Free Trial, sổ Notion/Sheets.
5. Bộ skill trong chính Project này: `extract-screenshot-data` (trích dữ kiện chart), `ict-doctrine` (kiểm thuật ngữ/doctrine), `ict-audit` (đối chiếu phân tích với dữ kiện), `ict-devils-advocate` (phản biện đối kháng) — dùng như "huấn luyện viên kiểm định" hằng tuần trong suốt lộ trình.

## C. Checklist tổng (in ra, tick dần)

- [ ] Gate 1: nhận diện khái niệm ≥90%/50 chart
- [ ] Gate 2: ≥200 setup backtest, expectancy ≥ +0.3R
- [ ] Gate 3: 3 tháng demo lãi + tuân thủ ≥95%
- [ ] Gate 4: pass 2 vòng mô phỏng challenge + quỹ dự phòng 2–3 lần phí
- [ ] FTMO Phase 1 (+10%, ≥4 ngày, đáy $90k bất khả xâm phạm)
- [ ] FTMO Phase 2 (+5%)
- [ ] FTMO funded + payout đầu (hoàn phí, split 90%)
- [ ] The5ers Step 1 (+10%, ≥3 ngày lời ≥0.5%, né khớp lệnh quanh tin)
- [ ] The5ers Step 2 (+5%)
- [ ] The5ers funded + nấc scaling đầu tiên

## D. Nguồn tham chiếu luật (kiểm tra lại trước khi mua)

- FTMO — How it works / Trading Objectives: https://ftmo.com/en/how-it-works/
- FTMO rules tổng hợp 2026 (1-step & 2-step): https://tradetanto.com/learn/ftmo-rules-evaluation-process · https://www.tradernotion.com/blog/ftmo-rule-changes-2026
- Hướng dẫn pass FTMO + toán rủi ro: https://tradeninety.com/blog/how-to-pass-ftmo-challenge-2026/ · https://www.tradernotion.com/blog/how-to-pass-the-ftmo-challenge-rules-math-strategy-2026
- The5ers High Stakes (trang chính thức): https://the5ers.com/high-stakes/
- The5ers so sánh các chương trình: https://the5ers.com/challenge-programs-bootcamp-high-stakes-hyper-growth-explained/

---

*Tài liệu này là lộ trình huấn luyện, không phải khuyến nghị đầu tư. Giao dịch ký quỹ có rủi ro mất vốn; chỉ thi quỹ bằng tiền phí bạn sẵn sàng mất.*
