---
type: market-analysis
status: watchlist
date: 2026-07-19
symbol: EURUSD
timeframe: "Top-down D1 → H1 → M5, chart FXReplay. D1 hiển thị giai đoạn khoảng Jun/2013 – Sep/2014; H1/M5 zoom chi tiết quanh 04–06/06/2014"
session: replay
htf_bias: "Bullish trên D1 — giá ở Deep Discount của dealing range 1.34811–1.39918, đã sweep một SSL nội bộ (1.35033/~1.3520) rất sát external thật (1.34811, chưa bị chạm) + displacement tăng xác nhận. NHƯNG sau khi re-map range con H1/M5 theo đúng swing của chính displacement này, giá hiện đang ở Deep Premium của range MỚI (~92%) → xung đột nested range D1 (Discount) vs H1 (Premium), chưa đủ điều kiện Tier A"
setup: "Áp dụng đồng thời Daily Bias (tier, PO3/macro time) và Dealing Range (quadrant, nested alignment, re-map sau displacement, chu kỳ ERL↔IRL) vào một ví dụ top-down D1→H1→M5 cụ thể để luyện quy trình phân tích 3 tầng"
in_trade: false
draw_on_liquidity: "D1 (range gốc): BSL xa tại 1.39918; 1.37233 (~EQ D1) là target gần/internal. H1-M5 (range re-map): BSL mới tại đỉnh vừa quét ~1.3670; SSL sâu hơn (chưa bị lấy) vẫn là 1.34811"
key_poi: "FVG/OB vùng 1.36000–1.36316 — trùng ranh giới Deep Discount/Discount-nông của D1 range GỐC, đồng thời là internal liquidity (IRL) của range H1/M5 MỚI sau re-map. Đây là POI cần chờ giá retrace về, không phải giá hiện tại (~1.36582, đang ở đỉnh range mới)"
invalidation: "(1) D1 đóng thân dưới 1.34811 (external SSL thật của range gốc) mà không reclaim → toàn bộ giả thuyết bullish HTF sụp đổ. (2) Giá xuyên thẳng và đóng thân dưới vùng 1.36000–1.3635 (POI/IRL của range mới) mà không phản ứng → range vừa re-map cũng hỏng, cần tìm đáy sâu hơn"
topic: "Quadrant theory (0-25-50-75-100%) áp vào Dealing Range D1; kiểm tra Partially vs Fully Consumed cho cú sweep 1.35033 so với external thật 1.34811; bắt buộc Re-map Dealing Range con H1/M5 sau displacement theo đúng 5 bước; ma trận Nested Range Alignment (location_htf vs location_ltf) phát hiện xung đột Discount D1/Premium H1; chu kỳ ERL↔IRL xác định giá đang ở pha nào; Daily Bias đầy đủ theo mẫu + chấm Bias Tier A/B/C; giả thuyết Delayed Judas (giờ sweep ~08:00 NY, ngoài London KZ) cần verify"
tags:
  - analysis
  - watchlist
  - EURUSD
  - daily-bias
  - dealing-range
  - remap
  - nested-range
  - quadrant-theory
  - erl-irl
  - premium-discount
  - liquidity-sweep
  - market-structure-shift
  - macro-times
  - ict-2022
---

# EURUSD D1→H1→M5 — Daily Bias & Dealing Range: Nested Alignment, Re-map, Quadrant — 2026-07-19

> [!info] Trạng thái
> **WATCHLIST — không vào lệnh.** Đây là note tổng hợp 3 lượt trao đổi trong cùng một phiên: (1) đọc top-down D1→H1→M5 theo [[01 - ICT 2022 Model|2022 Model]] cơ bản, (2) đào sâu Daily Bias + Dealing Range bằng chính framework nâng cao đã có sẵn trong vault ([[12 - Daily Bias]], [[12 - Dealing Range]], [[37 - Re-mapping Dealing Range sau Displacement]]). Note này **không lặp lại** lý thuyết ba bài đó — nó **áp dụng trực tiếp** vào ví dụ cụ thể, đồng thời phơi bày một xung đột quan trọng mà lượt đọc đầu tiên đã bỏ sót.

> [!warning] Ảnh gốc & độ chính xác của số liệu
> Toàn bộ phân tích dựa trên 3 ảnh chụp màn hình FXReplay (D1, H1, M5) Khang gửi trong chat — **chưa được lưu vào vault**. Nếu muốn tham chiếu lại chính xác, lưu 3 ảnh vào `10 - Market Analysis/Attachments/` với tên gợi ý `EURUSD-20260719-D1-1.png`, `EURUSD-20260719-H1-1.png`, `EURUSD-20260719-M5-1.png`, rồi thêm dòng `![[...]]` tương ứng vào mục 1–3 bên dưới. Mọi mức giá trong note này là **ước lượng đọc từ pixel ảnh** (D1 high 1.39918, low D1 range 1.34811, sweep ~1.35033/1.3520, đỉnh rally ~1.3670, giá hiện tại 1.36582 — mức này là số duy nhất đọc được rõ ràng từ nhãn giá trên ảnh) — không phải giá trích xuất chính xác từ nền tảng. Trước khi dùng case này cho một backtest thật, verify lại toàn bộ số trên chart gốc.

---

## 0. Bối cảnh & câu hỏi gốc

Khang gửi 3 ảnh (D1/H1/M5) của EURUSD trên FXReplay, giai đoạn lịch sử khoảng Jun/2013–Jun/2014, và hỏi cách phân tích top-down theo [[01 - ICT 2022 Model|2022 Model]]: mỗi khung cần xác định gì, phân tích gì, chờ gì. Lượt đọc đầu tiên dựng một câu chuyện khá "sách giáo khoa": D1 có draw on liquidity xuống SSL 1.35033/1.34811, giá sweep xong displacement tăng mạnh, H1/M5 test lại vùng OB 1.36000–1.36316 để tìm Long.

Ở lượt thứ hai, khi đào sâu bằng đúng framework Daily Bias/Dealing Range nâng cao đã có trong vault, phát hiện ra một lớp quan trọng bị bỏ sót ở lượt đầu: **range H1 cũ đã "chết" sau displacement và bắt buộc phải re-map** — và khi re-map đúng, giá hiện tại (1.36582) hóa ra đang ở **Deep Premium của range mới**, không phải discount như cảm giác ban đầu ("đang test lại OB từ trên xuống, có vẻ để Long tiếp"). Đây chính là bài học lõi của note này.

---

## 1. D1 — Dealing Range gốc & Quadrant

![[EURUSD-20260719-D1-1.png]]

**Hai đầu range (theo [[12 - Dealing Range]]):**

| Đầu range | Giá | Vai trò |
|---|---|---|
| Swing low | **1.34811** | External SSL thật — **chưa từng bị chạm** trong toàn bộ chuỗi sự kiện quan sát được |
| Swing high | **1.39918** | External BSL — còn mở, là draw on liquidity xa |

**Equilibrium** = (1.34811 + 1.39918) / 2 ≈ **1.37365** — đáng chú ý: mức kháng cự 1.37233 mà Khang tự kẻ trên chart nằm gần như đúng tại EQ này. Vùng consolidation nhiều tháng quanh 1.36–1.37 chính là thị trường "từ chối quyết định" quanh trung tâm giá trị của range (auction theory, mục A1 của [[12 - Dealing Range]]), không phải trùng hợp ngẫu nhiên.

**Chia quadrant (biên độ 0.05107):**

| Quadrant | Vùng giá | Ý nghĩa |
|---|---|---|
| 75–100% (Deep Premium) | 1.38641 – 1.39918 | Vùng Short tối ưu, cấm Long mới |
| 50–75% (Premium nông) | 1.37365 – 1.38641 | Short cần confluence mạnh |
| 25–50% (Discount nông) | 1.36088 – 1.37365 | Long cần confluence mạnh |
| **0–25% (Deep Discount)** | **1.34811 – 1.36088** | **Vùng Long tối ưu — OTE thường rơi vào đây** |

Vùng OB Khang tự khoanh tay (1.36000–1.36316) nằm **gần như đúng tại ranh giới Deep Discount / Discount nông** — phần lớn box nằm trong Deep Discount. Đây là một xác nhận đẹp: OB vẽ bằng mắt trùng khớp với vùng có xác suất phản ứng cao nhất theo đúng lý thuyết quadrant.

**Kết luận tầng D1: vị trí = Deep Discount → điều kiện tiên quyết cho bias Bullish đã thỏa.**

---

## 2. Cú sweep 1.35033 — Partially hay Fully Consumed?

Đây là lớp bị bỏ qua ở lượt đọc đầu tiên. Áp bảng 3 tiêu chí của [[37 - Re-mapping Dealing Range sau Displacement]] (mục "Consumed hoàn toàn hay một phần"):

| Tiêu chí | Đọc cho case này |
|---|---|
| Khoảng cách internal vừa lấy (1.35033/~1.3520) → external HTF thật (1.34811) | ~20 pip ≈ **4% biên độ range** — rất gần external, dưới xa ngưỡng 15–20% |
| Cấu trúc H4/D1 có break không? | Không — wick dài rồi đảo chiều ngay (turtle soup), D1 không đóng thân dưới 1.34811 |
| FVG/external HTF phía sau còn nguyên không? | 1.34811 **vẫn chưa bị chạm** — vẫn còn nguyên |
| Phản ứng giá | Wick dài + đảo chiều tức thì = dấu hiệu sweep, không phải acceptance |

→ **Partially consumed**, nhưng ở mức rất sát ranh giới. 1.35033 chỉ là một **internal liquidity pool** (minor SSL) nằm ngay phía trên external thật. Hệ quả quan trọng cho invalidation: nếu displacement hiện tại thất bại, còn nguyên khả năng giá quay lại "ăn nốt" 1.34811 trước khi thật sự đảo chiều — đây phải được ghi vào điều kiện invalidation, không được bỏ qua.

---

## 3. H1/M5 — Re-map bắt buộc sau displacement

Trên H1, range consolidation cũ (~1.36000–1.37233, kéo dài 22/5–05/6) đã bị **displacement phá thủng đầu dưới** (giá xuyên xuống ~1.3520). Theo nguyên tắc lõi của [[37 - Re-mapping Dealing Range sau Displacement]] — *"Sau mỗi nhịp displacement lấy external liquidity của range cũ, range cũ đã chết — phải vẽ lại"* — range H1 cũ **không còn dùng được** để đo premium/discount nữa.

**Range H1/M5 mới (5 bước re-map):**

| Bước | Kết quả |
|---|---|
| 1. Xác nhận displacement thật | ✅ chuỗi nến tăng gần dựng đứng, để lại FVG, phá qua toàn bộ consolidation cũ |
| 2. Vẽ range mới | Đáy mới ≈ **1.3520** (đáy sweep) → Đỉnh mới ≈ **1.3670** (đỉnh rally) |
| 3. Đo equilibrium mới | (1.3520+1.3670)/2 = **1.3595** |
| 4. Phân loại lại liquidity | External mới: BSL ~1.3670 (còn mở), SSL ~1.3520 (vừa tiêu thụ, internal so với external D1 thật 1.34811) |
| 5. Chọn POI tiếp theo | FVG/OB của chính nhịp displacement, ước lượng trùng vùng 1.360–1.3635 |

**Giá hiện tại (1.36582) nằm ở đâu trong range MỚI?**

(1.36582 − 1.3520) / (1.3670 − 1.3520) = 0.01382 / 0.0150 ≈ **92%** → **Deep Premium của chính range vừa re-map.**

Đây là phát hiện quan trọng nhất của cả buổi: nhìn thoáng qua, cảm giác là "giá đang test lại OB từ trên xuống để Long tiếp" — nhưng sau khi re-map đúng quy trình, giá thực ra đang ở **đỉnh của range mới**, không phải đáy.

---

## 4. Nested Range Alignment — xung đột kinh điển

Áp đúng ma trận trong [[12 - Dealing Range]] (mục A2):

| Vị trí D1 (range gốc) | Vị trí H1 (re-mapped) | Kết luận |
|---|---|---|
| **Discount** (deep) | **Premium** (deep, ~92%) | *"Xung đột: chờ H1 retrace về discount H1 (vẫn trong discount D1) rồi mới tìm Long"* |

Hành động đúng, theo đúng chữ trong note gốc của Khang: **không đuổi mua tại 1.36582.** Chờ giá thoái lui về discount/EQ của range mới (~1.3520–1.3595), đúng khu vực hai hình chữ nhật xám Khang đã khoanh trên M5 (~1.360–1.3635) — đó chính là **internal liquidity (IRL) của range mới**, không phải đích đến.

---

## 5. Đọc theo chu kỳ ERL ↔ IRL

Áp khung "nhịp thở" của [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL & ERL]] (mục A5, note Dealing Range):

```
Pha 1: Giá lấy ERL — sweep internal SSL ~1.3520 (sát external D1 thật 1.34811)   → ĐÃ XONG
Pha 2: Đảo, quay vào tìm IRL — rally lên 1.3670 rồi ĐANG thoái lui về vùng
       OB/FVG 1.360–1.3635                                                      → ĐANG DIỄN RA
Pha 3: Rebalance xong IRL → expansion tới ERL đối diện (1.37233 rồi 1.39918)     → CHƯA XẢY RA
```

Việc giá đang ở "premium của range mới" không mâu thuẫn với việc nó retrace vào IRL — đó chính là Pha 2. Việc cần làm không phải hoảng vì "premium xấu", mà **chờ Pha 2 hoàn tất**: giá chạm và phản ứng tại vùng OB/FVG 1.360–1.3635 với sweep nội bộ + MSS + displacement trên M1/M5, trước khi tin vào Pha 3.

---

## 6. Daily Bias đầy đủ theo mẫu + chấm Tier

Áp mẫu "Bullish Bias" của [[12 - Daily Bias]]:

```text
HTF dealing range: 1.34811 → 1.39918
Location: Deep Discount (giá vừa sweep tại ~0-4% range, dưới cả mốc 25%)
Draw on liquidity: BSL tại 1.39918 (xa); 1.37233 (~EQ, target gần/internal)
Expected path: sweep SSL nội bộ ~1.3520 (sát external 1.34811 chưa bị chạm)
  → bullish displacement → HIỆN ĐANG re-map + rebalance IRL (Pha 2 ERL/IRL)
  → chờ retest vùng 1.360–1.3635 → nếu giữ, expansion tới 1.37233 rồi 1.39918
Invalidation: D1 đóng thân chấp nhận dưới 1.34811 (SSL thật bị lấy + không reclaim),
  HOẶC giá xuyên thẳng vùng OB 1.360–1.3635 và đóng thân giữ dưới đó mà không phản ứng
```

**Chấm Tier (bảng 7.5 của [[12 - Daily Bias]]):**

| Điều kiện Tier A | Trạng thái |
|---|---|
| HTF array rõ hai đầu | ✅ Có |
| Đúng vị trí quadrant D1 | ✅ Deep Discount |
| Weekly profile thuận | ❓ Không xác định được từ ảnh — cần biết đây là thứ mấy trong tuần |
| Không có tin lớn chắn đường | ❓ Chưa xác minh — xem mục 7 |
| Nested range alignment D1/H1 cùng phía | ❌ **Xung đột** (Discount D1 / Premium H1) |

→ **Tier B (Partial)** với dữ liệu hiện có, không phải Tier A. Theo đúng quy tắc tự đặt ra: risk 1/2, hoặc chờ yếu tố còn thiếu (H1 retrace về discount của range mới) được giải quyết rồi mới nâng lên full risk.

---

## 7. Giả thuyết cần verify: Delayed Judas (W1)?

Trục thời gian M5 hiển thị UTC+0. Cú sweep xảy ra quanh mốc **~12:00 UTC ≈ 08:00 NY** (EDT, tháng 6) — **không** rơi vào London Kill Zone cổ điển (~06:00–09:00 UTC = 02:00–05:00 NY), mà rơi sát cửa sổ **8:30 NY** ([[40 - Macro Times]]). Đây khớp với pattern **W1 – Delayed Judas** trong [[12 - Daily Bias]]: London không tạo displacement giữ hướng, manipulation thật chạy muộn hơn, gần giờ tin/giờ mở NY.

> [!question] Cần Khang tự xác minh
> Giờ chính xác của cây nến sweep trên chart gốc, và (nếu muốn dùng case này cho backtest thật) tra lịch tin ngày 05/06/2014 cho EURUSD. Đây là giả thuyết dựa trên đọc trục thời gian từ ảnh, không phải xác nhận chắc chắn.

Nếu đúng là Delayed Judas ngoài London KZ chuẩn, đây là lý do bổ sung để **hạ thêm một bậc tin cậy**, cần xác nhận LTF chắc chắn hơn trước khi entry.

---

## 8. Checklist tổng hợp áp cho case này

| Hạng mục | Trạng thái |
|---|---|
| HTF dealing range xác định đúng (2 đầu có liquidity) | ✅ 1.34811 / 1.39918 |
| Vị trí Premium/Discount đúng range D1 | ✅ Deep Discount |
| Liquidity sweep trước reversal | ✅ (internal, sát external — mục 2) |
| MSS + displacement xác nhận | ✅ rally ~1.3520→1.3670 |
| Re-map range con sau displacement | ✅ thực hiện ở mục 3 — bước không được bỏ qua |
| Nested alignment D1 vs H1 cùng phía | ❌ Xung đột — lý do CHƯA vào lệnh |
| Giá đang ở POI (IRL) của range mới | ⏳ Đang tiến vào, chưa xác nhận phản ứng M1/M5 |
| Weekly profile / lịch tin đã kiểm tra | ❓ Cần Khang tự tra thêm |
| Kill Zone / Macro Time của cú sweep | ❓ Nghi vấn Delayed Judas — cần verify (mục 7) |

---

## 9. Concept đã áp dụng

- [[12 - Dealing Range]] · [[37 - Re-mapping Dealing Range sau Displacement]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]] · [[27 - Premium Discount]]
- [[12 - Daily Bias]] · [[40 - Macro Times]] · [[18 - Kill Zones]]
- [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]]
- [[01 - ICT 2022 Model]]

---

## 10. Bài học rút ra

1. **Re-map không phải bước tùy chọn.** Ngay khi một displacement phá external của range con, phải vẽ lại range đó trước khi kết luận premium/discount — lượt đọc đầu tiên của buổi này bỏ qua bước này và suýt kết luận sai rằng giá "đang ở discount, chuẩn bị Long".
2. **Quadrant chính xác hơn nhị phân 50/50.** OB khoanh tay của Khang trùng khớp gần như chính xác với ranh giới Deep Discount của D1 range — một xác nhận rằng trực giác đọc chart của Khang đang đi đúng hướng với lý thuyết.
3. **Nested range conflict là tín hiệu chờ, không phải tín hiệu hủy.** Discount D1 + Premium H1(mới) không có nghĩa là bias sai — nó có nghĩa là **chưa đúng lúc**; đúng theo chu kỳ ERL↔IRL, đây là Pha 2 (đang rebalance), cần kiên nhẫn chờ Pha 2 hoàn tất.
4. **Internal pool rất sát external thật (partially consumed ở ranh giới) vẫn để lại rủi ro treo lơ lửng** — 1.34811 chưa bị chạm nghĩa là kịch bản "quay lại ăn nốt SSL sâu hơn" vẫn hợp lệ và cần có trong invalidation.
5. **Giờ sweep lệch khỏi London KZ chuẩn đáng để nghi vấn Delayed Judas** — một lớp xác nhận bổ sung (hoặc cảnh báo hạ tier) mà nhiều trader bỏ qua vì chỉ nhìn hướng, không nhìn giờ.

---

## 11. Câu hỏi cần chốt (chưa xác nhận)

- Giá đóng thân chính xác của cây nến sweep trên D1 — có thực sự không đóng dưới 1.34811 hay chỉ wick (cần xem chart gốc, không phải ảnh chụp)?
- Giờ chính xác (UTC) của cây nến displacement chính trên M5, để xác nhận/loại bỏ giả thuyết Delayed Judas ở mục 7.
- Weekly profile: ngày 05–06/06/2014 là thứ mấy trong tuần, và weekly draw đã hit chưa (theo [[12 - Daily Bias]] mục W2)?
- Biên chính xác của FVG/OB trong vùng 1.360–1.3635 (fvg_high/fvg_low) để tính entry_precision và fill_depth_pct nếu sau này dùng case cho backtest thật.
- Phản ứng thực tế của giá tại vùng POI 1.360–1.3635 sau thời điểm ảnh chụp (đã sweep nội bộ + MSS + displacement M5 chưa, hay đã xuyên thủng và invalid)?

## 12. Next steps

- Nếu Khang tiếp tục replay và giá thực sự phản ứng đúng tại vùng 1.360–1.3635 (sweep + MSS + displacement M1/M5), tạo một file backtest riêng theo [[Backtest template - POI & Step Decision (ICT 2022)]] trong `04 - Backtesting/`, cross-link ngược về note này.
- Nếu tình huống "nested range conflict" (Discount HTF / Premium LTF re-map) lặp lại nhiều lần trong quá trình backtest, đây là ứng viên tốt để thêm một case cụ thể vào [[12 - Dealing Range]] mục A2 (hiện bài đó có ma trận lý thuyết nhưng chưa có ví dụ số liệu đầy đủ).
- Lưu 3 ảnh gốc vào `10 - Market Analysis/Attachments/` (tên gợi ý ở đầu note) để lần sau đối chiếu chính xác thay vì đọc lại ước lượng.
- Nếu muốn luyện phản xạ, có thể quiz nhanh về quadrant/nested range/re-map để kiểm tra mức độ nắm vững trước khi áp dụng lên chart sống.

---
*Ghi chú: `date` = ngày thực hiện phân tích (VN, UTC+7), không phải ngày trên chart (chart là dữ liệu lịch sử FXReplay ~2013-2014). Không log backtest vì không vào lệnh — đây là note phân tích/watchlist + luyện tập framework. Mọi mức giá là ước lượng đọc từ ảnh chụp màn hình, không phải giá trích xuất chính xác từ nền tảng — verify lại trên chart gốc trước khi dùng cho quyết định giao dịch thật.*
