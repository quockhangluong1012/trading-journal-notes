---
type: case-study
instrument: EURUSD
timeframe: D1-W1
method: ICT 2022 Model — Daily Bias backtest, MSS vs BOS distinction, DOL vs Target, Devil's Advocate audit
source: TradingView / FXReplay (bar replay), giai đoạn lịch sử 05/09/2005 – 04/01/2006
period_covered: "05/09/2005 → 04/01/2006 (replay dừng đúng bar hiện tại, chưa play forward)"
status: "CLOSED — 5 objection (O1–O5), tất cả đã đóng hoặc thu hẹp về minor. Verdict: SURVIVES THIS ATTACK"
tags: [ict, smc, backtest, case-study, eurusd, d1-bias, w1-bias, devils-advocate, mss-vs-bos, dol-vs-target]
---

# Case Study: EURUSD D1 Backtest 2005–2006 — Daily Bias, MSS vs BOS, DOL vs Target

> Đọc nhanh: case này bắt đầu từ 1 case study D1 hoàn chỉnh (bias, dealing range, MSS, FVG, DOL) trên dữ liệu lịch sử EURUSD 2005–2006, được audit qua 3 vòng devil's-advocate với 5 objection (O1–O5). Kết thúc với: (1) nhãn Premium/Discount được sửa đúng theo convention, (2) MSS và BOS được tách bạch đúng thứ tự (12/12/2005 vs 03/01/2006), (3) phân biệt rõ **Target thực tế** (D1 Dealing Range High) và **DOL thật** (external liquidity chưa quét, cao hơn nhiều).

![[EURUSD-D1-2005-StructureMap-20260808.svg]]

---

## 1. Tổng quan tình huống

- **Công cụ:** TradingView, feed OANDA qua FXReplay (bar replay) — dữ liệu lịch sử thật, không phải live.
- **Chế độ:** xử lý như **LIVE** trong suốt audit — replay dừng đúng tại bar hiện tại, không dùng hiểu biết về việc giá đã đi đâu sau đó để chấm điểm phân tích (tránh hindsight bias).
- **Giá tại bar hiện tại:** 1.20752.
- **Khung thời gian case:** D1 05/09/2005–17/11/2005 tạo cấu trúc LL/LH lớn; W1 xác nhận cùng hướng Bearish từ đỉnh Mar'05.
- **Vai trò AI trong case này:** Devil's Advocate — 3 lượt tranh luận, 5 objection (O1–O5), chỉ nhượng bộ khi có bằng chứng hoặc lập luận mới thật sự đánh bại được objection.

---

## 2. Thesis ban đầu (bản viết đầu tiên của user)

- Cấu trúc D1 05/09–17/11/2005: LL/LH (Bearish tổng thể); W1 cũng được cho là Bearish (ban đầu chỉ khẳng định bằng lời, chưa kèm chart).
- D1 Dealing Range: High 1.25942 (05/09) – Low 1.16410 (17/11).
- Vùng thanh khoản cũ 1.18651 (06/07–19/10/2005) đã bị quét 04–15/11/2005; giá tạo relative equal lows mới để tích lũy thanh khoản.
- 03–04/01/2006: displacement bullish mạnh sau khi lấy sell-side liquidity, phá qua "Intermediate term high" (nến 14/12/2005, High 1.20615) → tạo Market Structure Shift.
- Displacement để lại Bullish FVG (1.20003–1.18672, CE 1.193375), trùng với 1 Bearish iFVG trước đó (1.19758–1.19141, CE 1.194495) → BPR.
- DOL ban đầu = D1 Dealing Range High (1.25942); các mức 1.21798 / 1.22735 / 1.23230–1.23794 / 1.24998–1.25429 là Internal Liquidity trên đường đi.
- **Kết luận ban đầu:** D1 Bias hiện tại là Bullish, đọc như 1 nhịp pullback bên trong cấu trúc Bearish lớn hơn (D1 tổng thể + W1). Giá đang ở Discount của D1 range.

---

## 3. Vòng 1 — 3 objection đầu tiên

| # | Tier | Severity | Nội dung | Kết quả |
|---|---|---|---|---|
| O1 | SELF-CONTRADICTION / METHOD | fatal | "W1 cũng đang Bearish" khẳng định bằng lời, không kèm chart W1 — đúng lỗi mà user từng tự sửa ở 1 case trước (phải có chart W1 thật, không suy diễn từ D1 lên) | **giữ mở**, chờ chart W1 |
| O2 | ARITHMETIC | material | (1.20752−1.16410)/(1.25942−1.16410) = 45.6% của D1 range → theo convention chuẩn (&lt;45% discount / &gt;55% premium) là **Equilibrium**, không phải Discount như bạn viết | **giữ mở**, chờ phản hồi |
| O3 | CHART | material | Cùng chart D1, phần đầu bên trái (~Jun 2005) có 1 đỉnh cao hơn 1.25942, chưa được đặt tên/vẽ — 1.25942 có thể chỉ là internal liquidity, không phải DOL thật | **giữ mở**, cần số chính xác |
| O4 | UNSUPPORTED / METHOD | material | Pool "sell-side liquidity" ngay trước displacement không có mức giá cụ thể; pool duy nhất có số (1.18651) đã bị quét 40+ ngày trước — quá xa để là nhiên liệu trực tiếp cho MSS | **giữ mở**, cần pool sát hơn |
| O5 | ARITHMETIC | minor | Nến "MSS 04/01/2006": Open 1.21520, High 1.21438 — High &lt; Open, bất khả thi cho bất kỳ nến nào | **giữ mở**, cần sửa dữ liệu |

Verify bằng `check_arithmetic.py`: CE của cả 2 FVG (1.193375 và 1.194495) khớp đúng midpoint — không có lỗi ở phần này.

---

## 4. Vòng 2 — User gửi thêm chart W1, tự sửa Premium/Discount

User cung cấp chart W1 thật cho thấy downtrend Jan/Mar 2005 → Nov 2005 rõ ràng, LH/LL nguyên vẹn, chưa bị phá tính tới bar hiện tại.

| # | Cập nhật | Kết quả |
|---|---|---|
| O1 | Chart W1 xác nhận Bearish structure còn nguyên → khung "D1 Bullish = pullback trong W1 Bearish" có nền tảng thật | **WITHDRAWN** |
| O2 | User chấp nhận: 45.6% là Equilibrium, không phải Discount | **CLOSED** |
| O3 | Chart W1 (đi xa hơn về Jan/Mar 2005) cho thấy 1 đỉnh còn cao hơn ước tính ban đầu — cần số chính xác | **giữ mở, nâng cấp bằng chứng** |
| O4 | User cho ngày chính xác hơn cho pool 1.18651 (05/07–29/10/2005) — nhưng vẫn là cùng pool cũ, không giải quyết vấn đề khoảng cách thời gian tới displacement | **HELD** |
| O5 | — | chưa phản hồi |

Script `check_arithmetic.py --sensitivity` với boundary thay thế (~1.348, ước lượng) cho kết quả: nếu dùng range 1.16410–1.348, giá ở 23.6% → Discount rõ hơn nhiều so với 45.6% khi dùng 1.25942 — xác nhận thêm nghi vấn ở O3.

---

## 5. Vòng 3 — User cho số chính xác, tự sửa nhãn MSS/BOS

User cung cấp: đỉnh tháng 3 chính xác = **1.34806 (11/03/2005)**; relabel MSS thực tế xảy ra **12/12/2005** (không phải 04/01/2006 như viết ban đầu), còn 03/01/2006 là 1 **BOS** xác nhận tiếp diễn; pool SSL chính xác = 2 relative equal lows (22/11: 1.16858, 28/11: 1.16812), quét 02/12/2005 (Low 1.16608); sửa lại candle O5 (Open 1.20178, High 1.21438 — hợp lệ).

| # | Tier cuối | Severity cuối | Kết quả | Ghi chú |
|---|---|---|---|---|
| **O1** | SELF-CONTRADICTION | fatal→— | **CLOSED** | Không cần hỏi thêm — chỉ ~4-5 nến W1 từ đáy Nov'05, không đủ để là 1 MSS độc lập ở degree Weekly; nhãn "MSS" trên chart W1 chỉ là drawing copy từ D1 |
| **O2** | ARITHMETIC | material | **CLOSED** | Đổi nhãn thành "Equilibrium, nghiêng nhẹ discount" |
| **O3** | CHART | material→minor | **NARROWED** | 1.34806 xác nhận là DOL thật, chưa bị quét. User đưa lập luận trade-management hợp lý (partial exit ở internal liquidity, phần còn lại ở gần dealing range) → không cần đổi kế hoạch, chỉ cần đổi câu chữ: **"Target = D1 DLR High (1.25942); DOL = các swing high phía trên"** — user đã tự sửa đúng câu này |
| **O4** | UNSUPPORTED | material | **WITHDRAWN** | Pool đúng (equal lows 22/11 + 28/11), sweep đúng (02/12, Low 1.16608, dưới cả 2 equal lows), khoảng cách tới MSS (12/12) chỉ 10 ngày liên tục, không có nhịp ngược chen giữa — đạt chuẩn Step 2 |
| **O5** | ARITHMETIC | minor | **WITHDRAWN** | Open sửa → 1.20178, High (1.21438) ≥ mọi giá trị khác — hợp lệ. Nến này được hiểu lại là nến BOS (03/01), không phải MSS (12/12) |

**Điểm cộng đáng ghi nhận:** tự phân biệt đúng MSS (khởi tạo shift) và BOS (xác nhận tiếp diễn) — đây là 1 trong những nhầm lẫn phổ biến nhất khi đọc cấu trúc ICT, và user tự bắt lỗi này ở chính phân tích của mình, không cần AI chỉ ra.

![[EURUSD-D1-2005-ObjectionLedger-20260808.svg]]

---

## 6. Verdict cuối cùng

**SURVIVES THIS ATTACK.**

- **Evidence sufficiency: FULL** — D1 và W1 đều có chart thật xác nhận; chuỗi sweep → MSS → BOS có đầy đủ giá + ngày; CE của 2 FVG đúng toán học.
- **Đã tấn công và không phá được:** hướng D1 Bias (Bullish, pullback trong Bearish lớn hơn), backdrop W1 Bearish, toàn bộ trình tự cấu trúc (sweep 02/12 → MSS 12/12 → BOS 03/01), vị trí FVG/iFVG BPR trong nửa Discount của range.
- **Opposite case strength: weaker but non-trivial** — case đối lập ("đây chỉ là 1 correction-degree bounce, chưa phải reversal thật") chỉ còn sống nếu swing bị phá bởi MSS 12/12/2005 hóa ra là 1 swing không đáng kể — giá trị chính xác của swing đó chưa được verify, nhưng bằng chứng xung quanh (pool thật, sweep thật, trình tự đúng) đã làm case đối lập yếu đi nhiều so với vòng 1.
- **Điều này không chứng minh:** H1/M5 sẽ xác nhận theo hướng nào (chưa xuống khung đó — đúng theo quy trình D1→H1→M5, không nhảy cóc), hay lệnh cụ thể sẽ thắng/thua — chỉ là quy trình đọc D1/W1 đã đứng vững qua đối kháng.

---

## 7. Framework/bài học rút ra (áp dụng cho case sau)

- **DOL ≠ Target thực tế.** D1 Dealing Range High/Low là biên hợp lệ để tính Premium/Discount cho leg hiện tại (theo chuẩn "leg-start" tự đặt ra), nhưng KHÔNG tự động là DOL nếu có external liquidity chưa quét nằm xa hơn. Ghi rõ 2 khái niệm riêng trong mọi case sau: *Target (dùng để lên kế hoạch chốt lời/phản ứng)* vs *DOL thật (draw dài hạn, có thể không bao giờ cần chạm tới nếu đã scale-out trước đó)*.
- **MSS vs BOS: MSS = khởi tạo shift (breaking swing đầu tiên sau sweep); BOS = xác nhận tiếp diễn (breaking swing cao hơn, hình thành SAU MSS).** Gán nhãn cho đúng thứ tự thời gian trước khi gọi tên — kiểm tra ngày của "swing bị phá" phải luôn SAU ngày hình thành của chính swing đó.
- **Premium/Discount: dùng đúng ngưỡng chuẩn &lt;45% / &gt;55%, giữa là Equilibrium** — không tự nới "trên 50% = discount".
- **Liquidity run (Step 2) cần đúng 2 điều: pool có tên + giá cụ thể, VÀ khoảng cách thời gian từ sweep tới displacement phải liên tục, không có nhịp ngược/pool khác chen giữa.** Pool cũ, xa (nhiều tuần) không tự động là "nhiên liệu" cho 1 MSS xảy ra sau đó.
- **Đo bằng crosshair, không đoán bằng mắt qua pixel** — trong case này, AI đoán sai 2 lần (1.275, rồi 1.348) trước khi user cho số thật (1.34806); số của user luôn đáng tin hơn ước lượng hình ảnh.

---

## 8. Action items

- [ ] Xuống H1 tại vùng hiện tại — chạy đúng checklist H1 Confirmation (đã xây ở case 07/08/2026: 5 điều kiện AND) trước khi coi bất kỳ phản ứng nào là xác nhận đảo chiều hay tiếp diễn.
- [ ] Verify giá trị chính xác của swing bị phá bởi MSS 12/12/2005 (đang là điểm duy nhất chưa closed 100%).
- [ ] Khi case study tiếp theo dùng nested D1/W1 bias, luôn đính kèm chart W1 thật ngay từ đầu — không suy diễn W1 từ D1.
- [ ] Cập nhật `status` trong frontmatter khi lệnh backtest này (nếu play forward tiếp) cho kết quả thật.
