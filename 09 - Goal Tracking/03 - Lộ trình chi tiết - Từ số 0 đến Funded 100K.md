---
type: roadmap
dashboard: Roadmap-Detail
created: 2026-07-18
updated: 2026-07-18
tags:
  - roadmap
  - ict
  - prop-firm
---

# 🧭 Lộ trình chi tiết: Từ số 0 (ICT) → Funded FTMO/The5ers 10K → Scale 100K

> [!summary] Cách dùng note này
> Đây là bản **phóng to** của [[01 - Roadmap]]: toàn bộ con đường từ người chưa biết gì về ICT tới trader funded 100K, chia thành **8 giai đoạn** với điều kiện gate cứng giữa các giai đoạn. Mỗi giai đoạn có: mục tiêu, nội dung chi tiết, bài tập, và **tiêu chí thoát (exit criteria)** — chưa đạt tiêu chí thì chưa sang giai đoạn sau, bất kể cảm giác "mình sẵn sàng rồi".
>
> Nguyên tắc xuyên suốt: **process over outcome** — một giai đoạn được tính là xong dựa trên *bằng chứng trong vault* (số note, số mẫu, mistake rate), không dựa trên cảm nhận.

## 📍 Vị trí hiện tại của mình (cập nhật 2026-07-18)

> [!info] Đang đứng ở đâu trên bản đồ
> Mình **không** bắt đầu từ số 0. Trạng thái thực tế trong vault:
>
> | Hạng mục | Bằng chứng trong vault | Trạng thái |
> |---|---|---|
> | Giai đoạn 0 — Nền tảng thị trường | Đã trade demo từ 03/2026 | ✅ Xong |
> | Giai đoạn 1 — ICT Core Concepts | 52 concept notes trong `02 - Trading Knowledge/Concepts` | ✅ Phần lớn xong — cần ôn sâu (spaced review) thay vì học mới |
> | Giai đoạn 2 — Model hoá (2022 Model) | Model notes có; **playbook A+ thành văn CHƯA có** | 🟡 Đang dở — đây là nút thắt #1 |
> | Giai đoạn 3 — Backtest 200 mẫu | **22/200** backtest notes trong `04 - Backtesting` | 🟡 Đang chạy (11%) |
> | Giai đoạn 4 — Demo forward test | 29 demo trades (16 Win / 12 Loss / 1 BE-Loss?) từ 03–06/2026; **0 lệnh trong ~30 ngày gần đây** | 🟡 Tạm dừng — rủi ro lớn nhất hiện tại |
> | Giai đoạn 5 — Challenge rehearsal 10K | Lot size note + Excel calculator đã có; demo-đúng-luật chưa chạy | 🔴 Chưa bắt đầu |
> | Giai đoạn 6 — Thi & Funded 10K | Chưa mua gói | 🔴 Chưa bắt đầu |
> | Giai đoạn 7 — Scale 100K | Gate 0/5 — xem [[Pass FTMO & The5ers 100K package]] | 🔴 Khoá |
>
> **Kết luận thẳng:** việc cần làm không phải học thêm concept mới, mà là (1) viết playbook A+ thành văn, (2) giữ nhịp backtest đều, (3) nối lại forward test demo. Ba việc này quyết định có kịp mốc readiness 2027-01-07 hay không.

## 🗺️ Bản đồ 8 giai đoạn

| # | Giai đoạn | Dành cho ai bắt đầu từ 0 | Kỳ hạn chuẩn | Với mình (thực tế) |
|---|---|---|---|---|
| 0 | Nền tảng thị trường | 4–6 tuần | Tháng 1 | ✅ Xong |
| 1 | ICT Core Concepts | 12–16 tuần | Tháng 2–5 | ✅ Ôn lại theo chu kỳ |
| 2 | Model hoá — ICT 2022 Model + Playbook | 4–8 tuần | Tháng 5–6 | 🟡 **07–08/2026** |
| 3 | Backtest 200 mẫu | 16–24 tuần | Tháng 6–11 | 🟡 **07–12/2026** (song song GĐ2) |
| 4 | Demo forward test có kỷ luật | 12+ tuần | Tháng 9–12 | 🟡 **08–12/2026** (song song GĐ3) |
| 5 | Challenge rehearsal (demo đúng luật quỹ) | 2–4 tuần | Tháng 12–13 | 🔴 **12/2026–01/2027** |
| 6 | Thi FTMO 10K & The5ers 10K (song song) | 2–4 tháng | Tháng 13–17 | 🔴 **Q1–Q2/2027** |
| 7 | Funded 10K → payout → Gate → 100K | 9–15 tháng | Tháng 17–30 | 🔴 **2027 H2 – 2028 H1** |

---

## Giai đoạn 0 — Nền tảng thị trường (từ số 0) · 4–6 tuần

> [!info] Với mình: ✅ đã xong. Giữ lại làm tài liệu tham chiếu chuẩn (và để dạy lại người khác — dạy lại là cách kiểm tra hiểu sâu tốt nhất).

**Mục tiêu:** Đọc được chart trần (không indicator) và nói được thị trường đang làm gì, trước khi đụng tới bất kỳ khái niệm ICT nào.

### Nội dung
1. **Cấu trúc nến & chart:** đọc nến OHLC, wick vs body, khung thời gian và tính phân dạng (fractal) — cùng một cấu trúc lặp lại trên M1 tới Monthly.
2. **Swing structure thuần:** swing high/low, higher high/higher low, downtrend/uptrend/range — đánh dấu bằng tay 20 chart/tuần.
3. **Phiên giao dịch & giờ:** Asia – London – New York theo giờ Việt Nam (UTC+7), đặc tính từng phiên (Asia tích luỹ, London tạo high/low của ngày, NY tiếp diễn/đảo chiều). Đây là nền cho Kill Zones sau này.
4. **Sản phẩm giao dịch:** tick size, point value, spread, đòn bẩy của NAS100/NQ1, EURUSD, GBPUSD, XAUUSD; cách tính lot size theo $ risk.
5. **Công cụ:** TradingView (replay mode — sống còn cho backtest sau này), lịch tin (ForexFactory), Obsidian vault này.

### Tiêu chí thoát
- Đánh dấu đúng swing structure trên 20 chart liên tiếp không cần trợ giúp.
- Tính lot size cho risk $50 với SL bất kỳ trên cả 4 symbol trong <2 phút.
- Nói được giờ mở/đóng London & NY theo giờ VN cả mùa đông lẫn mùa hè (DST).

---

## Giai đoạn 1 — ICT Core Concepts · 12–16 tuần (từ số 0)

> [!info] Với mình: ✅ 52 concept notes đã có. Việc còn lại là **spaced review** — mỗi tuần chọn 2 concept `status: developing` trong vault, review lại bằng 5 ví dụ chart mới, nâng lên `tested`. Không học rộng thêm.

**Mục tiêu:** Hiểu *cơ chế* (tại sao thị trường phải làm vậy theo logic dòng tiền tổ chức), không phải thuộc lòng định nghĩa. Mỗi concept học theo chu trình: **định nghĩa → cơ chế → 10 ví dụ chart tự tìm → 5 counter-example (khi nào nó fail) → concept note trong vault**.

### Khối 1 — Liquidity là trung tâm (tuần 1–3)
Đây là khối quan trọng nhất toàn bộ ICT. Học sai khối này thì mọi thứ sau đều lung lay.

1. **Liquidity & vai trò của nó:** tại sao smart money cần vùng thanh khoản để khớp lệnh lớn; equal highs/lows = engineered liquidity.
2. **BSL / SSL (Buyside & Sellside Liquidity):** nơi cụm stop nằm; thị trường di chuyển *từ pool thanh khoản này tới pool kia*.
3. **Liquidity sweep / stop hunt / turtle soup:** phân biệt sweep (quét rồi đảo) với break (phá rồi đi tiếp) — nhìn displacement và close.
4. **Draw on Liquidity (DOL):** câu hỏi bắt buộc trước mọi phân tích: *"giá đang bị hút về pool nào?"* — liên hệ trực tiếp tới cụm lỗi tháng 7 của mình ([[13 - Mistake - Trading Into Unswept Liquidity]], [[02 - Mistake - Enter before liquidity sweep]]).

### Khối 2 — Cấu trúc & dịch chuyển (tuần 4–6)
5. **Market Structure Shift (MSS) & Break of Structure (BOS):** MSS = gãy cấu trúc *ngược xu hướng sau khi sweep* (tín hiệu đảo chiều), BOS = gãy *thuận xu hướng* (tiếp diễn). Nhầm hai cái này = nhầm cả model.
6. **Displacement:** nến thân lớn, một chiều, tạo imbalance — bằng chứng tổ chức tham gia. Không displacement = MSS yếu = bỏ.
7. **CHoCH vs MSS:** ranh giới thuật ngữ giữa các trường phái SMC; trong vault này thống nhất dùng MSS.

### Khối 3 — PD Arrays (tuần 7–10)
8. **Dealing Range:** từ swing sau sweep → chia Premium/Discount qua Equilibrium (50%); chỉ mua ở discount, bán ở premium.
9. **Fair Value Gap (FVG) & Consequent Encroachment (CE):** imbalance 3 nến; CE = 50% của gap; điều kiện FVG "valid" (sinh ra từ displacement, chưa bị lấp).
10. **Order Block (OB):** nến ngược chiều cuối trước displacement; mean threshold; refine OB bằng FVG bên trong.
11. **Breaker Block, Mitigation Block, Rejection Block:** các biến thể khi OB fail hoặc bị quét.
12. **OTE (Optimal Trade Entry):** vùng fib 62–79% của chân displacement.

### Khối 4 — Thời gian & Model tư duy (tuần 11–14)
13. **Kill Zones:** London KZ (~13:00–16:00 VN mùa hè), NY AM KZ (~19:30–22:00 VN mùa hè) — thời gian là bộ lọc, không phải trang trí.
14. **Power of Three (AMD):** Accumulation – Manipulation – Distribution trong ngày/tuần; open–sweep–reverse.
15. **IPDA & HTF bias:** daily bias từ chart D1/H4 (PD array HTF nào chưa được respect, DOL tuần nằm đâu).
16. **SMT Divergence:** phân kỳ giữa cặp tương quan (NQ vs ES, EU vs GU) xác nhận sweep thật.

### Tiêu chí thoát (từ số 0)
- ≥40 concept notes với ví dụ chart tự tìm (không copy từ video).
- Bài kiểm tra mù: cho 10 chart lạ, đánh dấu đúng ≥8/10 các yếu tố: DOL, sweep, MSS, FVG valid, premium/discount.
- Giải thích được bằng lời "tại sao giá phải quét equal lows trước khi lên" cho một người không trade hiểu được.

### Với mình — kế hoạch ôn (07–12/2026)
- Mỗi Chủ nhật: chọn 2 concept `confidence ≤ 3` trong Dataview, review bằng 5 chart mới từ chính backtest tuần đó, cập nhật `last_reviewed`.
- Ưu tiên ôn theo cụm lỗi thực tế: **Draw on Liquidity, liquidity sweep, MSS in POI** (map thẳng vào các mistake trong `06 - Mistake Database`: [[02 - Mistake - Enter before liquidity sweep]], [[03 - Mistake - Entry When MSS not in POI Zone]], [[13 - Mistake - Trading Into Unswept Liquidity]]).

---

## Giai đoạn 2 — Model hoá: ICT 2022 Model → Playbook A+ · 🟡 NÚT THẮT HIỆN TẠI

> [!warning] Với mình: đây là việc số 1 của tháng 07–08/2026. Backtest 22 mẫu đã chạy nhưng **chưa có playbook thành văn** — tức là đang backtest một model tồn tại trong đầu, không phải trên giấy. Rủi ro: mỗi lần "thấy setup" là một phiên bản hơi khác nhau → mẫu không đồng nhất → 200 backtest xong vẫn không kết luận được gì. Viết playbook TRƯỚC, backtest THEO playbook.

**Mục tiêu:** Biến ICT 2022 Model từ "narrative hiểu trong đầu" thành **checklist nhị phân** — mọi điều kiện trả lời được CÓ/KHÔNG trước khi vào lệnh, không có chỗ cho "nhìn cũng được".

### Chuỗi logic chuẩn của 2022 Model (khung xương playbook)
1. **HTF bias (D1/H4):** xu hướng + DOL của ngày/tuần nằm đâu? Bias phải chọn TRƯỚC phiên, ghi vào note, không đổi giữa phiên.
2. **Thời gian:** chỉ trong Kill Zone đã chọn (London / NY AM). Ngoài KZ = không có setup, kể cả "đẹp".
3. **Liquidity sweep (M15/M5):** giá quét BSL/SSL rõ ràng (old high/low, equal highs/lows, Asia high/low). *Chưa sweep = chưa có gì để chờ* — đây chính là cụm lỗi 04/07 của mình.
4. **MSS + displacement (M5/M1):** gãy cấu trúc ngược chiều sweep, bằng nến displacement, **và MSS phải xảy ra từ trong/tại POI HTF** ([[03 - Mistake - Entry When MSS not in POI Zone]]).
5. **Entry PD array:** FVG sinh ra từ chân displacement (ưu tiên) hoặc OB refine; entry tại CE hoặc mép gap.
6. **Stop:** ngoài swing tạo sweep (không phải sát mép FVG cho "đẹp R").
7. **Target:** pool thanh khoản đối diện (DOL) — không phải con số R tròn tuỳ hứng. R:R tối thiểu theo playbook (ví dụ ≥2R) mới được vào.
8. **Risk:** ≤0,5%/lệnh, tối đa 2–3 lệnh/ngày.

### Việc cụ thể (2–4 tuần)
- [ ] Viết `03 - Playbooks/3.2 - Setups/2022 Model A+ Setup.md`: mỗi bước trên thành mục CÓ/KHÔNG + ảnh ví dụ chuẩn từ backtest thật + ảnh counter-example (trông giống nhưng thiếu 1 điều kiện).
- [ ] Định nghĩa **A+ vs B setup**: A+ = đủ 8/8 điều kiện; B = thiếu 1 điều kiện phụ → chỉ được backtest, không được trade demo/live.
- [ ] Checklist trước lệnh in ra được (pre-trade checklist) đồng bộ với `3.1 - Checklists`.
- [ ] Quy tắc quản trị lệnh: khi nào BE, khi nào partial, khi nào để nguyên — viết một lần, không quyết định trong lúc lệnh chạy.

### Tiêu chí thoát
- Playbook mà một trader ICT khác đọc xong có thể chấm 10 setup của mình đúng/sai **y hệt mình chấm** (kiểm tra tính khách quan).
- 10 backtest gần nhất đều được chấm A+/B/invalid theo checklist, không có "ngoại lệ".

---

## Giai đoạn 3 — Backtest 200 mẫu · 🟡 22/200 · mục tiêu xong 12/2026

**Mục tiêu:** Một bộ dữ liệu đủ lớn để trả lời bằng SỐ, không bằng niềm tin: *2022 Model trong tay MÌNH, trên symbol MÌNH trade, có expectancy dương không, và dương ở điều kiện nào?*

### Phương pháp (chống hindsight bias — không thoả hiệp)
1. **Replay mode bắt buộc:** TradingView bar replay, tua từng nến. Không bao giờ chấm setup trên chart đã hiện kết quả.
2. **Quy tắc "trigger trước, kết quả sau":** ghi entry/SL/TP vào note **trước khi** tua tiếp. Setup chỉ được tính nếu mọi điều kiện checklist đã CÓ tại thời điểm entry.
3. **Ghi cả setup thua và setup invalid:** mẫu chỉ gồm lệnh thắng đẹp = curve-fitting. Tỷ lệ invalid cũng là dữ liệu (cho biết tần suất setup thật).
4. **Frontmatter đầy đủ** theo schema backtest trong [[CLAUDE]] (`liquidity_swept`, `displacement`, `mss`, `fvg_valid`, `grade`, `followed_plan`…) — dashboard chỉ aggregate được khi field nhất quán.

### Nhịp & phân bổ
- **Nhịp chuẩn:** 5 backtest/tuần (mỗi ngày làm việc 1 phiên replay ~45 phút). 22 → 200 cần ~36 tuần; muốn xong 12/2026 cần **~8/tuần** → dồn thứ 7/CN mỗi ngày 2–3 mẫu.
- **Phân tầng mẫu:** tối thiểu 50 mẫu/symbol chính (NAS100, EURUSD), phủ cả London và NY, phủ cả năm 2024–2026 (nhiều chế độ thị trường khác nhau).
- **Checkpoint phân tích:** tại mốc **50 / 100 / 200 mẫu**, tính: win rate, average R, expectancy = (WR × AvgWin) − (LR × AvgLoss), max losing streak, phân rã theo session/symbol/grade. Ghi vào [[Build a statistically validated backtest sample]].

### Tiêu chí thoát (gate sang giai đoạn 5)
- ≥200 mẫu backtest đúng phương pháp, frontmatter sạch.
- Expectancy **dương và ổn định** ở cả 2 nửa mẫu (chia đôi theo thời gian — nửa sau không tệ hơn hẳn nửa trước).
- Biết rõ **max losing streak** trong mẫu (con số này quyết định risk 0,5% có sống nổi qua drawdown không: 10 lệnh thua liên tiếp @0,5% = −5%, vẫn còn cách Max Loss 5%).
- Nếu expectancy âm hoặc mong manh → **quay lại Giai đoạn 2 tinh chỉnh playbook**, không cố đi tiếp. Dữ liệu là trọng tài, không phải ICT.

---

## Giai đoạn 4 — Demo forward test có kỷ luật · 🟡 nối lại từ 08/2026

> [!warning] Với mình: 29 lệnh demo (16W/12L/1?) là khởi đầu tốt, nhưng chuỗi **~30 ngày không có lệnh live-demo nào** là rủi ro thật sự — backtest kiểm tra MODEL, forward test kiểm tra NGƯỜI. Không có nhịp forward test thì ngày thi challenge sẽ là lần đầu tiên chịu áp lực thời gian thực sau nhiều tháng.

**Mục tiêu:** Chứng minh mình thực thi được playbook trong thời gian thực — chờ được setup, bỏ được setup xấu, chấp nhận thua đúng luật.

### Cấu trúc
1. **Tài khoản demo 10K$** (đúng size sẽ thi), risk cố định 0,5%/lệnh.
2. **Chỉ trade Kill Zone đã chọn** — với lịch làm việc Amaris, thực tế nhất là **NY AM KZ (~19:30–22:00 giờ VN)**; London chỉ khi có thể ngồi chart trọn phiên.
3. **Mỗi lệnh một note** theo [[Trade template]], link mistake nếu có; **ngày không có setup cũng ghi** ("no-trade day" đúng playbook là một ngày THẮNG về quy trình).
4. **Mục tiêu mẫu:** ≥60 lệnh forward test trước khi rehearsal (hiện có 29 → cần ~31 lệnh nữa; với 2–5 setup A+/tuần thì cần ~3–4 tháng, khớp mốc 12/2026).

### Chỉ số theo dõi hàng tuần (ghi vào [[02 - Skill Metrics]] & weekly review)
- % lệnh followed_plan (mục tiêu >90%)
- Mistake rate = số mistake link / số lệnh (mục tiêu giảm dần, đặc biệt cụm [[02 - Mistake - Enter before liquidity sweep]])
- Expectancy forward vs expectancy backtest (lệch quá xa = đang trade khác playbook)

### Tiêu chí thoát
- ≥60 lệnh forward, followed_plan >90% trong 8 tuần cuối.
- Mistake rate 8 tuần cuối giảm ≥50% so với 8 tuần đầu.
- Expectancy forward cùng dấu và cùng bậc với backtest.
- Journaling streak: không lỗ hổng ghi chép >2 ngày trong 8 tuần.

---

## Giai đoạn 5 — Challenge rehearsal: demo đúng luật quỹ · 12/2026–01/2027

**Mục tiêu:** Diễn tập nguyên trạng kỳ thi trước khi trả tiền thật. Đây là mốc **readiness 2027-01-07**.

### Rehearsal FTMO (2 tuần)
- Demo 10K, luật thật: target +10%, Max Daily Loss 5% (mốc tĩnh balance đầu ngày), Max Loss 10%, ≥4 ngày giao dịch.
- Kỷ luật tự đặt CHẶT HƠN luật: dừng ngày ở −3%; 2–3 lệnh/ngày; alert equity tại 9.700$ (−3%) và 9.500$ (−5%).
- Pass rehearsal = đạt +10% không phá luật, không giới hạn thời gian nhưng ghi lại mất bao nhiêu ngày giao dịch (số này = kỳ vọng thực cho kỳ thi thật).

### Rehearsal The5ers (2 tuần)
- Khác biệt phải "diễn tập vào tay": daily drawdown neo **closing equity/balance hôm trước** → cuối mỗi ngày ghi lại mốc đóng cửa = trần lỗ ngày mai; và cần **3 ngày có lãi** → tập thói quen khoá lợi nhuận để đóng ngày xanh ≥0,5% (+50$).
- Mô phỏng trên giấy 3 kịch bản prior-close drawdown (ngày xanh → đệm tăng; ngày đỏ → đệm co; ngày flat) trước khi bắt đầu.

### Tiêu chí thoát (= tiêu chí MUA GÓI — thay cho "I feel ready")
- [ ] Backtest ≥200 mẫu, expectancy dương ổn định (Giai đoạn 3 ✓)
- [ ] ≥60 lệnh forward, followed_plan >90%, mistake rate giảm (Giai đoạn 4 ✓)
- [ ] Pass cả 2 rehearsal không vi phạm luật nào
- [ ] Bảng lot size + Excel calculator cập nhật ([[Lot size 10K]] ✓ đã có)
- [ ] Kế hoạch thi viết sẵn từng kịch bản (xem Giai đoạn 6)

---

## Giai đoạn 6 — Thi FTMO 10K & The5ers 10K (SONG SONG, không tuần tự) · Q1–Q2/2027

> [!tip] Chi tiết bổ sung cho lộ trình 10K — kế hoạch thi từng ngày
> Hai quỹ là **hai bài toán khác nhau**, thi song song nhưng KHÔNG áp luật quỹ này sang quỹ kia. Kế hoạch hành động từng bước của mỗi quỹ nằm trong goal note riêng: [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]]. Dưới đây là lớp chiến thuật bổ sung.

### Toán của kỳ thi (đọc mỗi sáng trước phiên)
- Risk 0,5%/lệnh, playbook R:R ≥2 → mỗi lệnh thắng ≈ +1% trở lên. Target Phase 1 +10% ≈ **7–12 lệnh thắng ròng** → với 2–4 setup A+/tuần, kỳ vọng thực tế **4–8 tuần/phase**. Ai quảng cáo pass trong 3 ngày là đang chơi trò khác (và thường cháy).
- Đệm thua: @0,5%, cần **6 lệnh thua liên tiếp** mới chạm mốc tự đặt −3% ngày; cần 20 lệnh thua ròng mới chạm Max Loss. Max losing streak trong backtest cho biết xác suất kịch bản này.
- **Không có áp lực thời gian ở cả hai quỹ** (unlimited) → kẻ thù duy nhất là tự ép nhịp.

### Kịch bản viết sẵn (quyết định TRƯỚC, không quyết trong phiên)
| Tình huống | Hành động đã cam kết |
|---|---|
| Ngày −3% (tự đặt) | Đóng platform ngay, ghi journal, quay lại ngày mai. Không "gỡ một lệnh cuối". |
| 3 ngày thua liên tiếp | Nghỉ 1 ngày, review 3 lệnh với checklist — lỗi thực thi hay variance? Variance thì tiếp tục y nguyên; lỗi thì sửa một thứ duy nhất. |
| Đạt +8%/10% Phase 1 | Giảm risk còn 0,25%/lệnh — bảo vệ tiến độ, không nước rút. |
| Đạt target nhưng chưa đủ ngày (FTMO 4 ngày giao dịch / The5ers 3 ngày lãi) | Trade size tối thiểu đúng playbook cho đủ điều kiện ngày, không risk thêm ý nghĩa. |
| Tin đỏ (CPI/FOMC/NFP) trong KZ | Không lệnh mới 30' trước–sau tin. Lệnh đang chạy: về BE nếu ≥+1R, hoặc đóng. |
| The5ers: ngày đang xanh +0,4–0,5% cuối phiên | Khoá lợi nhuận đóng "ngày có lãi" ≥+50$ — điều kiện ngày quý hơn vài chục $ để chạy thêm. |
| Cảm giác "phải vào kẻo lỡ" | Đó là [[04 - Mistake - FOMO Entry]] — đứng dậy 5 phút. Setup A+ tuần nào cũng có. |

### Khác biệt then chốt FTMO vs The5ers (dán cạnh màn hình)
| | FTMO 2-Step 10K | The5ers High Stakes 10K |
|---|---|---|
| Daily loss | 5% mốc **tĩnh** balance đầu ngày (00:00 CEST) | 5% từ **closing equity/balance hôm trước** (00:00 server) |
| Max loss | 10% tĩnh (floor 9.000$) | 10% tĩnh từ balance ban đầu |
| Điều kiện ngày | ≥4 **ngày giao dịch**/phase | ≥3 **ngày có lãi** (≥0,5%) |
| Hết hạn | Không giới hạn | Không giao dịch 30 ngày liên tiếp = hết hạn |
| Hàm ý chiến thuật | Lỗ hôm qua không co trần hôm nay | Ngày xanh nâng đệm — lợi nhuận giữ được làm mốc drawdown dịch lên theo |

---

## Giai đoạn 7 — Funded 10K → Payout → Gate → 100K · 2027 H2–2028 H1

**Mục tiêu:** Pass challenge chưa phải đích — **sống sót sau khi funded** mới là kỹ năng tạo thu nhập. Sau đó scale 100K theo gate cứng.

1. **3 tháng đầu funded:** giữ nguyên risk 0,5%, mục tiêu duy nhất là payout đầu tiên + không vi phạm. Lưu ý luật MỚI xuất hiện khi funded (FTMO Standard: hạn chế trade tin & giữ lệnh qua tuần — cân nhắc account type Swing).
2. **Payout kỷ luật:** rút đều theo chu kỳ, không "gộp cho to". Payout = dữ liệu chứng minh hệ thống ra tiền thật.
3. **Gate 100K (5 điều kiện):** định nghĩa đầy đủ trong [[Pass FTMO & The5ers 100K package]] — funded cả 2 quỹ 10K, ≥2 payout, 3 tháng lãi liên tiếp, mistake rate thấp ổn định, phí trả bằng lợi nhuận.
4. **Thi 100K:** cùng % rules, khác con số tuyệt đối (risk 0,5% = 500$/lệnh, daily buffer tự đặt −3% = 3.000$). Nếu con số tuyệt đối gây run tay → thêm 1 quý ở 10K. Kỹ thuật không đổi; đây là kỳ thi tâm lý.

---

## 🚦 Bảng gate tổng (in ra / pin lên Dashboard)

| Gate | Từ → Sang | Điều kiện đo được | Trạng thái |
|---|---|---|---|
| G1 | Concepts → Model hoá | ≥40 concept notes + blind test 8/10 | ✅ |
| G2 | Model hoá → Backtest chuẩn | Playbook A+ thành văn, chấm khách quan được | 🔴 **việc số 1 hiện tại** |
| G3 | Backtest → Rehearsal | 200 mẫu, expectancy dương ổn định 2 nửa mẫu | 🟡 22/200 |
| G4 | Forward test đạt chuẩn | ≥60 lệnh, followed_plan >90%, mistake rate ↓50% | 🟡 29/60, đang đứt nhịp |
| G5 | Rehearsal → Mua gói 10K | Pass 2 rehearsal 2 tuần không phá luật | 🔴 |
| G6 | Funded 10K → Mua gói 100K | 5 điều kiện gate trong [[Pass FTMO & The5ers 100K package]] | 🔴 0/5 |

> [!quote] Nguyên tắc cuối
> Lộ trình này dài hơn quảng cáo của mọi "funded trader guru" — vì nó được thiết kế để pass **một lần và giữ được tài khoản**, không phải pass nhanh rồi cháy. Mỗi gate bị bỏ qua là một khoản phí challenge bị đốt trong tương lai. Thời gian biểu có thể xê dịch; thứ tự gate thì không.

## Liên kết
- Lộ trình tổng: [[01 - Roadmap]] · Dashboard: [[00 - Goal Dashboard]] · Chỉ số: [[02 - Skill Metrics]]
- Goals: [[Pass FTMO first package challenge (10K$)]] · [[Pass The5er first package challenge (10k$)]] · [[Pass FTMO & The5ers 100K package]] · [[Build a statistically validated backtest sample]] · [[Master the ICT 2022 Model]] · [[Cut my top 3 repeated mistakes]] · [[Hold daily journaling and process discipline]]
- Nguồn luật quỹ (kiểm tra lại trước khi mua): [FTMO Trading Objectives](https://ftmo.com/en/trading-objectives/) · [The5ers High Stakes rules](https://help.the5ers.com/what-are-the-general-rules-for-the-high-stakes-program/)
