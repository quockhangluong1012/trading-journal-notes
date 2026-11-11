---
type: ict-concept
concept: Fair Value Gap
aliases:
  - FVG
  - Fair Value Gap
  - Imbalance
  - BISI
  - SIBI
  - Buyside Imbalance Sellside Inefficiency
  - Sellside Imbalance Buyside Inefficiency
  - Price Imbalance
tags:
  - trading/ict/concept
  - trading/study
  - trading/deep-dive
  - "#FVG"
status: tested
category: PD Array
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence:
version: v2
last_reviewed: 2026-10-07
created: 2026-06-22
updated: 2026-10-07
prerequisites:
  - "[[50-Displacement-In-Depth]]"
  - "[[19-Liquidity]]"
  - "[[20-Liquidity-Sweep]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[12-Dealing-Range]]"
  - "[[10-Consequent-Encroachment-Mean-Threshold]]"
common_mistakes:
  - "[[10-Mistake-FVG-Not-Valid]]"
  - "[[08-Mistake-Weak-Displacement]]"
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[04-Mistake-FOMO-Entry]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
  - "[[12-Mistake-Log-Data-Mismatch-Backtest]]"
---

# Fair Value Gap (FVG)

> [!summary] Tóm tắt 1 câu (v2)
> **Fair Value Gap là đoạn giá mà trong ba nến liên tiếp chỉ có nến giữa đi qua — dấu vết hình học của một chuyển động nhanh, một chiều (thường là displacement), chỉ được biết khi nến 3 đóng cửa. FVG *mô tả* chắc chắn nơi giá đã đi qua với rất ít thời gian; còn việc giá quay lại, phản ứng hay xuyên thủng nó phụ thuộc vào hình học khoảng cách, chế độ trend và bản chất của dòng lệnh đã tạo ra nến giữa — những thứ chart nến không cho thấy trực tiếp.**

> [!important] Nguyên tắc cốt lõi (v2)
> **FVG là một LOCATION có định nghĩa chính xác, không phải một TÍN HIỆU.**
> 1. **Sự tồn tại của FVG gần như không mang thông tin.** Trên random walk thuần túy có ~31 FVG / 100 nến (≥ 0.5 ATR: ~12 / 100 nến) — FVG-Sim-01.
> 2. **Việc FVG "được lấp" không phải bằng chứng.** Random walk không drift lấp hết 71% FVG trong 20 nến và 97% trong 2000 nến — "gap nào cũng lấp" là tính chất hồi quy của chuyển động ngẫu nhiên (FVG-Sim-02).
> 3. **Mọi tuyên bố "FVG có edge" phải thắng một vùng đối chứng cùng hình học**, với thời điểm biết (known_at = close nến 3) đúng và khớp lệnh thực tế. Lỗi look-ahead phổ biến nhất biến win rate 32% thành 65% trên dữ liệu không có edge (FVG-Sim-05).
>
> *Nguyên tắc của v1 — "FVG chỉ là một điểm tham chiếu giá; nó KHÔNG phải tín hiệu trade. Chỉ FVG sinh ra từ displacement phá cấu trúc (BOS/MSS), nằm tại POI HTF, đúng premium/discount, đồng hướng Daily Bias và xuất hiện sau liquidity sweep mới đáng vào lệnh" — **vẫn giữ nguyên giá trị thực hành**. v2 bổ sung: (a) các bộ lọc đó là **giả thuyết về việc thay đổi tỷ lệ các loại displacement trong mẫu**, chưa phải edge đã kiểm chứng (§30); (b) lọc "displacement mạnh" có thể làm kết quả TỆ hơn nếu lệnh limit bị khớp chủ yếu ở loại displacement tạm thời — adverse selection (§30.4, FVG-Sim-04).*

> [!quote]- Tóm tắt và nguyên tắc của v1 (nguyên văn — giữ để đối chiếu)
> **Tóm tắt 1 câu (v1):**
> **Fair Value Gap (FVG) là vùng mất cân bằng (imbalance) tạo bởi 3 nến, nơi giá được giao dịch một chiều quá nhanh do displacement, để lại một khoảng giá chưa được cân bằng mà thị trường có xu hướng quay lại rebalance — vừa là POI để vào lệnh, vừa là draw để giá bị hút về.**
>
> **Nguyên tắc cốt lõi (v1):**
> **FVG chỉ là một điểm tham chiếu giá; nó KHÔNG phải tín hiệu trade. Chỉ FVG sinh ra từ displacement phá cấu trúc (BOS/MSS), nằm tại POI HTF, đúng premium/discount, đồng hướng Daily Bias và xuất hiện sau liquidity sweep mới đáng vào lệnh.**
> Một FVG nhỏ giữa range, không có displacement, không có context bias là nhiễu — đừng trade.

> [!info] Đây là bản v2 (2026-10-07) — đọc trước khi dùng
> - Note hợp nhất **note v1** (2026-06-22 → 2026-07-28) với nghiên cứu **Fair Value Gap — Deep Research v0.1** theo brief 54 mục (Part I–XI). Nội dung v1 được giữ **nguyên văn** ở chỗ phù hợp và đánh dấu *(v1)*; nơi v1 có claim cần sửa hoặc gắn nhãn, chú thích v2 đứng ngay cạnh, không xóa bản gốc. Bản đồ di chuyển nội dung ở [[#Changelog]]. Bản v1 nguyên vẹn được sao lưu tại `Claude outputs/backups/13-FVG-Fair-Value-Gap.2026-10-07.md.bak`.
> - Ba loạt hình: `FVG-Deep-01…23` = sơ đồ khái niệm mới (v2); `FVG-Sim-01…06` = **mô phỏng null model / toy model** — đường nền mà mọi claim phải vượt, **không phải dữ liệu thị trường**; `FVG-Sec-*`, `FVG-Advanced-*`, `FVG-War-*`, `FVG-EdgeB-*`… = hình của v1.
> - Mọi ngưỡng số là **HEURISTIC**; mọi `RULE-FVG` là **v0.1 — BACKTEST REQUIRED**; mọi `HYP-FVG` là **UNTESTED**. Không thành phần nào trong note là edge đã được kiểm chứng trên dữ liệu thật.
> - **Vì sao chỉ có mô phỏng, không có dữ liệu thật?** Phiên nghiên cứu này không truy cập được nguồn dữ liệu giá (Yahoo/Dukascopy/Binance/Stooq đều bị chặn từ cả hai máy). Thay vì bịa số, note dùng null model để trả lời câu hỏi "hiện tượng X xảy ra bao nhiêu khi KHÔNG có edge?" và đặc tả đầy đủ backtest để bạn chạy trên dữ liệu của mình (§41–43).
> - Note liên quan dùng làm nền, không lặp lại: [[50-Displacement-In-Depth]] · [[20-Liquidity-Sweep]] · [[10-Consequent-Encroachment-Mean-Threshold]] · [[17-Inverse-Fair-Value-Gap-iFVG]] · [[21-Liquidity-Void]] · [[03-Balanced-Price-Range]] · [[14-Implied-Fair-Value-Gap]] · [[48-1st-Presented-Fair-Value-Gap]] · [[12-Dealing-Range]] · [[59-Daily-Bias]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]].

> [!abstract]- Mục lục (bấm để mở)
> - **Cách đọc note** — hệ thống nhãn, thang giải thích 6 tầng, ký hiệu
> - **0. Executive Summary** — 22 kết luận
> - **PART I — Nền tảng:** 1. Lệnh, khớp lệnh, price discovery · 2. Gap là gì · 3. "Fair value" nghĩa là gì · 4. Inefficiency & imbalance
> - **PART II — Khái niệm cốt lõi:** 5. FVG chính xác là gì (6 tầng + định nghĩa vận hành) · 6. Vì sao 3 nến · 7. Bullish/Bearish từ số 0 · 8. FVG hình thành thế nào — và vì sao nó không phải "lỗ hổng"
> - **PART III — Vì sao FVG tồn tại:** 9. Câu hỏi trung tâm · 10. FVG vs Displacement
> - **PART IV — Thuật ngữ:** 11. Gia đình gap & thuật ngữ · 12. FVG vs Liquidity / OB / Liquidity Void / Gap
> - **PART V — Hành vi:** 13. Vì sao giá quay lại · 14. Fill & từ vựng · 15. FVG có luôn được lấp? · 16. Consequent Encroachment · 17. Mitigation · 18. FVG như S/R · 19. Invalidation · 20. Vòng đời & state machine · 21. Real-time vs ex-post
> - **PART VI — Bối cảnh:** 22. + MSS · 23. + Liquidity Sweep · 24. + POI · 25. + Dealing Range · 26. + DOL · 27. Đa khung D1 → H1 → M5 & nesting
> - **PART VII — Ứng dụng:** 28. Continuation vs Reversal · 29. Hierarchy & significance score · 30. Vì sao FVG này chạy, FVG kia fail · 31. Failure modes · 32. Khung quyết định · 33. Ví dụ, case studies, war stories, edge cases · 34. Checklist
> - **PART VIII — Phản biện:** 35. Misconceptions · 36. Hindsight, look-ahead, narrative · 37. Phản biện & giới hạn · 38. Lỗi thường gặp
> - **PART IX — Định lượng:** 39. Từ điển biến · 40. FVG có predictive value độc lập không?
> - **PART X — Backtest:** 41. Thiết kế · 42. Giả thuyết · 43. Cỡ mẫu, kiểm định, robustness
> - **PART XI — Mô hình tư duy:** 44. Giải thích cho trẻ 5 tuổi · 45. Tổng hợp 15 câu hỏi · 46. Mô hình tri thức cuối cùng · 47. Tự kiểm tra, flashcards, lesson learned, thành thạo · 48. Registers
> - Tài liệu tham khảo · Phụ lục A (mô phỏng) · Phụ lục B (pseudocode) · Changelog

---

## Cách đọc note này — hệ thống nhãn

| Nhãn | Ý nghĩa | Mức tin cậy mặc định |
|---|---|---|
| **[OBSERVABLE]** | Đọc trực tiếp được từ OHLC + thời gian ("Low nến 3 = 1.0779 > High nến 1 = 1.0761") | Cao — nhưng chỉ mô tả |
| **[MATHEMATICAL]** | Đúng theo định nghĩa hoặc chứng minh toán học (vd: nến 2 phải đi qua toàn bộ vùng FVG trong thị trường liên tục) | Cao — về logic, không về thị trường thật |
| **[SIMULATION]** | Kết quả mô phỏng null model (random walk, GARCH) với seed cố định | Cao về *mô hình null*; không phải dữ liệu thị trường |
| **[TOY MODEL]** | Mô hình cơ chế đơn giản hóa, tham số minh họa, không hiệu chỉnh | Chỉ minh họa *một* cơ chế có thể |
| **[MARKET MECHANICS]** | Giải thích bằng order matching, liquidity, impact, auction — hoặc có bằng chứng thực nghiệm đã công bố | Cao → trung bình tùy bằng chứng |
| **[ICT FRAMEWORK]** | Cách ICT / cộng đồng ICT định nghĩa hoặc dùng thuật ngữ | Cao về *định nghĩa*; không nói gì về *hiệu quả* |
| **[INTERPRETATION]** | Diễn giải hợp lý nhưng không chứng minh được từ OHLC | Trung bình → thấp |
| **[HYPOTHESIS]** | Claim kiểm chứng được | Chưa biết |
| **[BACKTEST REQUIRED]** | Không được coi là edge cho tới khi test đúng phương pháp | — |
| **[HEURISTIC]** | Ngưỡng số chọn để có quy tắc nhất quán, không phải hằng số của thị trường | — |

**Về nguồn ICT.** Giáo trình gốc của ICT (Michael J. Huddleston) chủ yếu ở dạng video/mentorship. Định nghĩa FVG được trích trong note lấy từ transcript bài *ICT Mentorship Core Content — Month 04 — Fair Value Gaps* (qua dịch vụ tóm tắt video — Tier 3/4, không phải văn bản gốc do ICT xuất bản). Phần còn lại của "[ICT FRAMEWORK]" = *cách hiểu phổ biến trong tài liệu cộng đồng*. Note không gán cho ICT những câu chưa kiểm chứng.

**Về "Smart Money".** Trong note, "Smart Money" luôn được hiểu là **một nhân vật trong câu chuyện của mô hình ICT**, không phải nhóm người tham gia quan sát được trên chart. Khi cần nói về người tham gia, note dùng thuật ngữ vi cấu trúc định nghĩa được: *maker* (cung cấp thanh khoản), *taker* (tiêu thụ thanh khoản), *metaorder* (lệnh lớn được chia nhỏ thực thi theo thời gian), *dòng lệnh ròng*, *liquidity provider*.

**Về mô phỏng.** Sáu hình `FVG-Sim-01 … 06` dùng random walk Gaussian (và biến thể Student-t, GARCH) không drift trừ khi ghi rõ, bước 1 phút hoặc 10 giây, tới 18 triệu bước mỗi lần chạy; FVG-Sim-03/04 dùng thêm một **toy model** ba loại displacement. Mục đích không phải chứng minh ICT sai — mà để biết *một hiện tượng xuất hiện thường xuyên tới mức nào khi không có bất kỳ "ý định" nào*. Chi tiết ở [[#Phụ lục A — Ghi chú mô phỏng]].

**Thang giải thích 6 tầng** (theo yêu cầu "giải thích cho đứa trẻ 5 tuổi" của brief):

| Tầng | Tên | Mục tiêu |
|---|---|---|
| L1 | Trực giác | Ngôn ngữ đời thường, không thuật ngữ |
| L2 | Ví dụ giá đơn giản | Một chuỗi OHLC / sơ đồ ASCII |
| L3 | Trading | Thuật ngữ trading phổ thông |
| L4 | Cơ chế thị trường | Order matching, market/limit/stop, bid/ask, impact, price discovery, auction |
| L5 | ICT | "ICT gọi hiện tượng này là…" — chỉ sau khi đã có L4 |
| L6 | Giới hạn | Chart **không thể** cho biết điều gì |

**Ký hiệu dùng xuyên suốt**

| Ký hiệu | Nghĩa |
|---|---|
| H₁, L₁, H₃, L₃ | High/Low của nến 1 và nến 3 (nến 2 là nến giữa) |
| Proximal | Mép FVG mà giá chạm TRƯỚC khi retrace (bullish: L₃; bearish: H₃) |
| Distal | Mép xa (bullish: H₁; bearish: L₁) |
| CE | Consequent Encroachment = (proximal + distal)/2 |
| size | \|proximal − distal\| — luôn chuẩn hóa: size/ATR |
| depth | Độ sâu fill = (proximal − cực trị retrace)/size; 0 = vừa chạm, 0.5 = CE, 1 = full fill |
| ATR | ATR(14) của khung đang xét, đóng băng tại nến biết FVG |
| known_at | Thời điểm (close nến) mà FVG/nhãn trở nên biết được. FVG: known_at = close nến 3 |
| p_null | Xác suất random walk không drift chạm target trước stop = (Entry − Stop)/(Target − Stop) (long) |
| excess | Win rate − p_null — thước đo "hơn hình học" |
| control zone | Vùng đối chứng: cùng hướng, cùng khoảng cách tới giá, cùng size (đơn vị ATR) nhưng KHÔNG phải FVG |

---

## 0. Executive Summary

Hai mươi hai kết luận. Mỗi kết luận được phát triển ở các mục sau.

**1. FVG là vùng giá chỉ MỘT cây nến đi qua — không phải vùng "không có giao dịch".** Trong thị trường giao dịch liên tục (open nến sau = close nến trước): Open₂ = Close₁ ≤ H₁ và Close₂ = Open₃ ≥ L₃ ⇒ **nến 2 đã đi qua toàn bộ vùng [H₁, L₃]** **[MATHEMATICAL]**. Ngoại lệ duy nhất là khi có session/opening gap giữa các nến. Câu "vùng giá chưa được giao dịch" (rất phổ biến, kể cả trong tài liệu công cụ chart) là sai về mặt cơ học (§2, §8; FVG-Deep-01).

**2. "Gap" trong FVG là thiếu hụt THỜI GIAN tại mức giá, không phải thiếu hụt giao dịch.** Cùng hiện tượng mà Market Profile gọi là *single prints*. Trên random walk, thời gian/đơn vị giá bên trong một H1 FVG có trung vị bằng **0.56 lần** phần còn lại của ba nến (FVG-Sim-06B) — và điều đó đúng *theo định nghĩa*, không phải bằng chứng của "imbalance tổ chức" **[SIMULATION]** (§2, §27).

**3. "Fair value" trong FVG không phải fair value của kinh tế học hay kế toán.** ICT định nghĩa FVG là *"a range in price delivery where one side of the market liquidity is offered"* (transcript, Tier 3–4). "Fair" ở đây là quy ước của ICT cho việc giá được chào hai chiều; FVG **không** tuyên bố giá trong vùng là "không công bằng" hay "định giá sai" (§3).

**4. Sự tồn tại của FVG gần như không mang thông tin.** Random walk Gaussian: **30.9 FVG / 100 nến** (≥ 0.25 ATR: 19.8; ≥ 0.5 ATR: 11.8); Student-t(3): 33.7; GARCH(1,1): 30.9. Kích thước trung vị ≈ 0.37 ATR (FVG-Sim-01) **[SIMULATION]**. Một bộ sưu tập "FVG đẹp" luôn tìm được, trên mọi chart.

**5. FVG gần như là hàm số của "nến giữa lớn" — nhưng hầu hết FVG không đến từ nến lớn.** P(FVG | nến 2 ≥ 2 ATR) ≈ **88%** trên random walk; nhưng **78%** FVG lại sinh từ nến 2 < 1.5 ATR (FVG-Sim-01B). Displacement và FVG liên quan chặt nhưng không đồng nhất: có displacement không FVG và FVG không displacement (§10, FVG-Deep-04).

**6. "Giá quay lại FVG" trước hết là hình học.** Random walk không drift, FVG ≥ 0.1 ATR (n = 51,902): **43%** bị chạm ngay nến kế tiếp, **83%** trong 20 nến, **92%** trong 100 nến; xác suất chạm trong 20 nến theo khoảng cách khớp công thức first-passage của chuyển động Brown — không cần bất kỳ "logic FVG" nào (FVG-Sim-02) **[SIMULATION + MATHEMATICAL]** (§13, §15).

**7. "Gap nào cũng lấp" đúng cả khi không có ai.** Random walk một chiều là *hồi quy* (Pólya): mọi mức giá hữu hạn đều được chạm lại với xác suất 1. Full fill: 71% trong 20 nến, 94% trong 500 nến, **97%** trong 2000 nến (FVG-Sim-02A). Câu "price always fills imbalance" vì thế không phân biệt được FVG với bất kỳ vùng nào khác **[MATHEMATICAL]** (§15).

**8. Gap không được lấp chủ yếu nói về TREND (drift), không về "ý định".** Thêm drift 0.2 ATR/nến: **39%** FVG cùng chiều trend không bao giờ bị chạm trong 500 nến; FVG ngược trend: **0%** (FVG-Sim-02C). Số lượng FVG theo hướng cũng tự lệch theo drift (45,327 cùng chiều vs 13,172 ngược chiều). Đây là giải thích đơn giản nhất cho "breakaway gap" (§15) **[SIMULATION]**.

**9. Có các cơ chế thị trường thật có thể làm FVG hành xử khác hình học — và chúng dự báo những điều KHÁC nhau.** (a) *Transient impact*: tác động giá của lệnh chủ động lớn hồi lại một phần sau khi dòng lệnh dừng; nghiên cứu metaorder cho thấy impact vĩnh viễn ≈ **0.5–0.7** lần đỉnh (Moro et al. 2009; Bershova & Rakhlin 2013), lý thuyết "fair pricing" dự đoán **≈ 2/3** (Farmer et al. 2013). (b) *Phần thưởng cho người cung cấp thanh khoản*: dòng lệnh không mang thông tin buộc giá nhượng bộ rồi hồi lại (Grossman & Miller 1988; Campbell, Grossman & Wang 1993; Nagel 2012). (c) *Dòng lệnh có trí nhớ dài*: metaorder chưa thực thi xong kéo giá tiếp tục cùng chiều (Lillo & Farmer 2004). (a)+(b) dự báo retrace sâu; (c) dự báo không retrace **[MARKET MECHANICS]** (§9, §13).

**10. Ba loại displacement để lại FVG giống nhau nhưng số phận trái ngược.** Toy model: FVG từ *liquidity shock* bị đóng cửa xuyên distal trong 16 nến ở **77%**; từ *information shock* **33%**; từ *metaorder* **13%** (và 51% không bao giờ bị chạm). Phân bố kích thước gần như chồng nhau (FVG-Sim-03) **[TOY MODEL]**. Chart nến không cho biết bạn đang nhìn loại nào.

**11. Adverse selection: lệnh limit tại CE được khớp nhiều nhất ở loại FVG tệ nhất.** Trong toy model, lúc hình thành ba loại chia ~31/35/33%; trong các lệnh CE *được khớp* tỷ lệ thành **49/36/16%**. Lọc "displacement mạnh" (nến 2 ≥ 2 ATR) tăng tỷ lệ FVG-có-sự-kiện từ 11% lên 69% nhưng excess win của FVG còn **−7.6%** so với **−1.4%** của vùng đối chứng (FVG-Sim-04) **[TOY MODEL]**. Đây là cảnh báo về cơ chế, không phải số đo thị trường thật — nhưng nó cho thấy tại sao bộ lọc "đẹp" có thể làm hại.

**12. Trên nhiễu, FVG không hơn vùng đối chứng cùng hình học.** Quy tắc khai báo trước (limit CE, stop distal + 0.1 ATR, target 2R): random walk — FVG excess +1.6% (SE 0.3%), đối chứng +1.9%; GARCH — +2.0% vs +2.2% (phần dương chung là sai số lấy mẫu của p_null, giống nhau cho cả hai). Đây là điều *phải* xảy ra trên dữ liệu không có edge — và chính là **baseline** mà dữ liệu thật phải vượt (FVG-Sim-04A) **[SIMULATION]**.

**13. CE không có địa vị đặc biệt trong hình học.** Sau khi chạm proximal, xác suất giá đi sâu hơn q·size trước khi bật ra 1·size đúng bằng **1/(1+q)**: "giữ được ở CE" xảy ra **31%** số lần chỉ do hình học, không có điểm gãy tại 0.5 (FVG-Sim-04B). Lý thuyết transient impact gợi ý mức hồi ≈ ⅓ cú đẩy — không liên quan tới trung điểm của gap. CE là **quy ước hữu ích để đặt lệnh**, giá trị dự báo là **[HYPOTHESIS]** (§16).

**14. Từ vựng quyết định con số.** Trên cùng một tập FVG random walk, trong 20 nến: touch **83%**, CE **77%**, full fill **71%**, đóng cửa xuyên distal **64%**. "FVG được tôn trọng X%" không có nghĩa nếu không nêu định nghĩa, khung thời gian và cửa sổ (§14, §19, FVG-Deep-07/09).

**15. FVG chỉ tồn tại khi nến 3 đóng cửa.** Tại close nến 2, "gap tạm thời" C₂ − H₁ chỉ sống sót qua nến 3 ở **48%** trường hợp trên random walk; gap tạm thời 0.15 ATR sống sót ~22%, 0.6 ATR ~65%, 1.1 ATR ~90% — khớp công thức Brown (FVG-Sim-05A). Vẽ FVG khi nến 3 chưa đóng là dùng thông tin chưa tồn tại (§21).

**16. Hai lỗi backtest có thể tự tạo ra "edge" lớn.** Cùng FVG, cùng quy tắc, trên random walk: đúng = win **31.6%**, E[R] **−0.05**; *coi low của nến 3 là lần chạm đầu* = win **65.3%**, E[R] **+0.96**; *kiểm tra stop/target bằng nến H1 và coi nến mơ hồ là thắng* = **50.2%**, E[R] **+0.51** (FVG-Sim-05B). Mọi kết quả FVG không nêu rõ cách xử lý known_at và độ phân giải khớp lệnh đều phải nghi ngờ (§21, §36).

**17. FVG là thuộc tính của khung thời gian bạn nhìn.** Trên random walk, **98%** H1 FVG chứa một M5 FVG cùng chiều trong nến 2 — nhưng **99.9%** nến H1 lớn KHÔNG tạo H1 FVG cũng chứa M5 FVG. "LTF liquidity void xác nhận HTF FVG" vì thế gần như tự động; chỉ **5.7%** M5 FVG nằm trong một H1 FVG chưa bị phá — nesting là bộ lọc *số lượng*, chưa phải bằng chứng (FVG-Sim-06) (§27). Mốc đóng nến của broker (GMT+2 vs GMT+3) cũng có thể tạo/xóa FVG H1 (v1 EdgeB).

**18. FVG không phải Liquidity, không phải Order Block, không phải POI, không phải tín hiệu vào lệnh, không phải confirmation.** Nó có thể *đóng vai* location bên trong một POI. Gộp FVG = POI = Entry chính là chiến lược "FVG alone" — trên nhiễu không hơn đối chứng (§12, §24, FVG-Deep-23).

**19. "Vì sao FVG này chạy, FVG kia fail?" tách thành bốn câu hỏi.** (a) Dòng lệnh nào đã tạo nến 2 (tạm thời / thông tin / metaorder) — không quan sát trực tiếp, chỉ có proxy; (b) chế độ drift; (c) lựa chọn định nghĩa (touch/CE/close, khung, cửa sổ); (d) khớp lệnh. "Confluence" chỉ có giá trị khi nó là proxy *đo được trước* cho (a) hoặc (b) (§30).

**20. Cỡ mẫu cần lớn hơn trực giác.** Phát hiện win rate hơn hình học +5 điểm % (baseline 1/3, α = 0.05, power 80%) cần ~**711** lệnh; +3 điểm cần ~**1,962**. So sánh FVG vs đối chứng chênh 5 điểm cần ~**1,444 mỗi nhóm**. Expectancy +0.2R với bracket 2R cần ~**424** lệnh. Một journal 30 lệnh có khoảng tin cậy win rate ±**17.5** điểm % **[MATHEMATICAL]** (§43).

**21. Một số claim của v1 phải sửa.** "Gap = quãng giá không ai kịp giao dịch, lệnh bị bỏ lại vẫn còn sống" (W0) sai như một cơ chế mặc định — lệnh limit nằm sẵn trong vùng đã bị nến 2 khớp; "CE là giá vốn trung bình của dealer/bên tạo gap" là **[INTERPRETATION]** không kiểm chứng được từ OHLC; số liệu case study v1 không có dữ liệu gốc. Mọi rule của v1 được giữ, gắn nhãn HEURISTIC, thay đổi trình bày dạng OLD/NEW (§48.2).

**22. Kết luận trung thực.** FVG là một **mô tả đáng tin cậy** và một **công cụ định vị có kỷ luật** (nơi chờ, nơi đặt stop, nơi bác bỏ ý tưởng). Nó **chưa được chứng minh là bộ dự báo**. Nếu có edge, edge đến từ (1) bộ lọc context đo được *trước* làm thay đổi tỷ lệ loại displacement, (2) cách vào lệnh tránh adverse selection, (3) quản trị rủi ro — và chỉ biết được khi thắng vùng đối chứng trên dữ liệu thật của chính bạn.

> [!tip] Câu trả lời ngắn cho câu hỏi trung tâm của brief — "Tại sao FVG tồn tại?"
> Vì trong một khoảng thời gian bằng một cây nến, **dòng lệnh chủ động một chiều đã tiêu thụ hết thanh khoản đang chờ nhanh hơn tốc độ thanh khoản mới được bổ sung**, khiến giá đi một mạch qua một đoạn rồi dừng ở mức mới; hai nến kề bên — đại diện cho giao dịch "bình thường" trước và sau — không chạm lại đoạn đó. Dòng lệnh ấy có thể là thông tin mới, một người cần thanh khoản gấp, một metaorder đang được thực thi, một chuỗi stop bị kích hoạt — hoặc đơn giản là nhiễu đủ lớn. FVG ghi lại **chuyện đã xảy ra** một cách chính xác. Nó không cho biết **ai** làm, **vì sao**, và **họ đã làm xong chưa** — mà chính ba điều đó quyết định giá có quay lại, phản ứng hay xuyên qua.

---

# PART I — NỀN TẢNG

> [!note] Vì sao bắt đầu từ lệnh và sổ lệnh?
> Brief yêu cầu: "Đừng dạy tôi cách nhận diện hình dạng FVG trước." Một FVG là *hậu quả* của cách giá được tạo ra. Nếu không hiểu giá được tạo ra thế nào, mọi câu "FVG là imbalance", "giá quay lại để rebalance" chỉ là những từ thay thế cho nhau. Part I dựng các viên gạch cần thiết; phần chi tiết về lệnh/stop/liquidity đã có ở [[20-Liquidity-Sweep]] §1 nên ở đây chỉ nhắc lại phần liên quan trực tiếp tới FVG.

## 1. Nền tảng thị trường: lệnh, khớp lệnh, price discovery

### 1.1 L1 — Trực giác trước khi có thuật ngữ

Hãy tưởng tượng một chợ đấu giá. Người bán treo bảng giá ("tôi bán 5 cái ở giá 100, 3 cái ở 100.5…"), người mua đến và mua ngay theo giá đang treo. Nếu bỗng nhiên có rất nhiều người mua cùng lúc, họ mua hết hàng ở 100, rồi hết ở 100.5, rồi 101… Giá "chạy" lên rất nhanh qua nhiều bảng giá. Khi đám đông đã mua xong, hoặc khi người bán mới mang hàng ra, giá dừng lại.

Bây giờ hãy chụp ảnh chợ mỗi 15 phút và chỉ ghi lại *giá cao nhất, thấp nhất, giá đầu và giá cuối* trong 15 phút đó. Đó chính là một cây nến. Nếu đợt mua dồn dập xảy ra trong một khung 15 phút, cây nến đó sẽ rất dài; khung trước nó và khung sau nó có thể không hề "chạm" tới đoạn giá ở giữa mà đợt mua đã chạy qua. **Đoạn giá ở giữa đó — có người mua bán, nhưng chỉ trong khoảnh khắc chạy qua — là thứ ICT gọi là Fair Value Gap.**

> [!warning] Giới hạn của ẩn dụ
> Trong chợ thật không có "một đám đông" duy nhất và không ai "quay lại" đoạn giá đó vì nhớ nó. Ẩn dụ chỉ giúp hình dung *vì sao* có đoạn giá ít thời gian; nó không chứng minh đoạn giá đó có ý nghĩa gì về sau.

### 1.2 L4 — Ba loại lệnh, sổ lệnh và cách giá dịch chuyển **[MARKET MECHANICS]**

| Loại lệnh | Vai trò | Có hiển thị trong sổ lệnh? | Liên quan FVG |
|---|---|---|---|
| **Limit** | Nằm chờ ở một mức giá → *cung cấp* thanh khoản (maker) | Có (trừ phần ẩn/iceberg) | Là "vật cản" mà nến 2 phải tiêu thụ để đi qua |
| **Market** | Khớp ngay với lệnh limit tốt nhất → *tiêu thụ* thanh khoản (taker) | Không (khớp tức thì) | Là "động cơ" của nến 2 |
| **Stop** | Trở thành lệnh market khi giá chạm mức kích hoạt | Thường không | Có thể khuếch đại nến 2 (stop cascade — Osler 2005) |

**Giá chỉ dịch chuyển khi lệnh chủ động tiêu thụ hết khối lượng ở mức giá tốt nhất.** Ví dụ sổ lệnh phía bán (ask) của một hợp đồng giả định:

```text
Mức giá   Khối lượng chờ bán (limit)
102.0     ████ 4
101.5     █ 1
101.0     ██ 2
100.5     ███ 3
100.0     █████ 5      ← best ask
-----------------------
 99.5     ████ 4       ← best bid
```

Một lệnh **market mua 15 lots** đến:
- khớp 5 lots ở 100.0 → hết mức 100.0
- khớp 3 lots ở 100.5 → hết
- khớp 2 lots ở 101.0 → hết
- khớp 1 lot ở 101.5 → hết
- khớp 4 lots ở 102.0 → best ask mới là mức kế tiếp phía trên

Giá giao dịch cuối cùng là 102.0. **Mọi mức có lệnh chờ đều có giao dịch xảy ra.** Mức không có lệnh chờ (nếu có) bị "nhảy qua" — đó là "gap" duy nhất theo nghĩa đen ở cấp vi cấu trúc, và nó thường chỉ rộng vài tick ở thị trường thanh khoản tốt.

Ba kết quả nghiên cứu nền tảng giúp hiểu nến 2 của FVG:

1. **Kyle (1985) — λ (lambda):** thay đổi giá tỷ lệ với dòng lệnh ròng; λ lớn khi thị trường "mỏng" (ít thanh khoản) hoặc khi người tạo thị trường lo ngại dòng lệnh mang thông tin.
2. **Cont, Kukanov & Stoikov (2014) — Order Flow Imbalance (OFI):** trên khoảng thời gian ngắn, thay đổi giá gần như **tuyến tính theo OFI** (chênh lệch giữa lệnh/hủy lệnh phía mua và phía bán ở mức tốt nhất), với độ dốc **tỷ lệ nghịch với độ sâu** sổ lệnh. Hệ quả cho FVG: *một nến 2 lớn = OFI lớn, HOẶC sổ mỏng, HOẶC cả hai.* OHLC không phân biệt được hai trường hợp.
3. **Easley, López de Prado & O'Hara (2012) — flow toxicity:** khi dòng lệnh bị nghi là mang thông tin ("toxic"), người cung cấp thanh khoản rút lệnh/giãn spread → sổ mỏng đi đúng lúc dòng lệnh mạnh → giá chạy xa hơn cho cùng một lượng lệnh. Đây là cơ chế hợp lý cho việc nến 2 "đi một mạch".

**Resiliency (khả năng phục hồi của sổ lệnh).** Sau khi một mức bị tiêu thụ, lệnh limit mới được đặt lại theo thời gian. Tốc độ "lấp lại" sổ lệnh và phần tác động giá *tạm thời* hồi lại (transient impact) là chủ đề §13 — đây là một trong những cơ chế thật nhất có thể đứng sau "giá quay lại FVG".

### 1.3 L4 — Price discovery và góc nhìn đấu giá (Auction Market Theory) **[MARKET MECHANICS + INTERPRETATION]**

Trong Auction Market Theory (Steidlmayer; Dalton, *Mind Over Markets*), thị trường luôn "quảng cáo giá" để tìm đối tác:

- **Balance (cân bằng):** người mua và người bán đều chấp nhận một vùng giá → giá quay đi quay lại, giao dịch nhiều thời gian ở đó → hình thành **value area** (vùng chứa phần lớn thời gian/khối lượng). Trên chart nến: các nến chồng lấp nhau.
- **Imbalance (mất cân bằng):** một phía áp đảo → giá di chuyển một chiều, ít thời gian ở mỗi mức, cho tới khi gặp phía đối diện "phản hồi" (responsive) → **one-timeframing**, **single prints** trên TPO profile. Trên chart nến: nến lớn, ít chồng lấp — đây là chỗ FVG xuất hiện.

Trong ngôn ngữ AMT, sau khi giá rời một vùng balance bằng một đợt imbalance, giá có thể (a) **chấp nhận** mức mới (xây value mới ở đó), hoặc (b) **từ chối** và quay về value cũ. Hai nhánh này tương ứng với "FVG giữ được" và "FVG bị lấp/xuyên". AMT *mô tả* hai nhánh rất tốt; nó **không** cho một quy tắc dự báo nhánh nào sẽ xảy ra chỉ từ hình dạng.

> [!info] Single print ↔ FVG
> Theo bài phân tích quan điểm của Dalton trên ATAS, single prints "cho thấy các mức giá tăng tốc" và "sức mạnh, sự quyết liệt của một phía", thường được dùng làm vùng hỗ trợ/kháng cự, và "người mua còn mạnh cho tới khi giá xóa single prints". Đây gần như là câu chuyện ICT kể về FVG — **đo bằng thời gian tại mức giá** thay vì bằng biên của 3 nến. Sự trùng hợp này là bằng chứng rằng hai cộng đồng mô tả cùng một hiện tượng; nó **không** phải bằng chứng rằng hiện tượng đó có giá trị dự báo.

### 1.4 L6 — Chart nến cho biết gì và không cho biết gì

![[FVG-Deep-05-Cung-OHLC-Khac-Ben-Trong.svg|720]]
*FVG-Deep-05: Hai đường đi bên trong nến 2 cho cùng OHLC và cùng FVG — một đường đi một mạch (imbalance theo nghĩa thông thường), một đường dừng lâu giữa vùng (có giao dịch hai chiều đáng kể). Chart nến không phân biệt được.*

| Chart nến CHO BIẾT **[OBSERVABLE]** | Chart nến KHÔNG cho biết |
|---|---|
| Biên của 3 nến; vùng [H₁, L₃]; size so với ATR | Khối lượng và thời gian ở từng mức bên trong nến 2 |
| Nến 2 đã đi qua toàn vùng trong một khung thời gian | Ai giao dịch; lệnh chủ động hay bị động; ý định |
| Thời điểm vùng được biết (close nến 3) | Còn lệnh chờ nào bên trong vùng hay không |
| Giá có quay lại chạm / lấp / đóng cửa xuyên qua hay không | Cú di chuyển là thông tin (giữ giá), thanh khoản (hồi lại) hay metaorder (tiếp tục) |
| Vị trí tương đối với range, swing, liquidity đã đánh dấu | Sổ lệnh có mỏng bất thường hay không |

**Quy tắc làm việc rút ra:** mọi câu trong journal về FVG nên viết được ở cột trái. Câu nào thuộc cột phải phải gắn nhãn **[INTERPRETATION]** hoặc **[HYPOTHESIS]**.

---

## 2. Gap là gì? — First principle

### 2.1 Gap truyền thống (price gap / opening gap)

```text
Phiên 1 đóng cửa:  Close = 100
Phiên 2 mở cửa:    Open  = 105

105 ─────  ← Open phiên 2
    │
    │  GAP: không có giao dịch nào trên sàn này giữa 100 và 105
    │      (thị trường đóng cửa — tin tức tích lũy — mở cửa ở mức mới)
100 ─────  ← Close phiên 1
```

Đây là **gap theo nghĩa đen**: trong khoảng thời gian thị trường đóng cửa, không có giao dịch nào ở các mức 100–105 trên venue đó. Gặp ở cổ phiếu (qua đêm), futures (giữa các phiên, cuối tuần), FX (cuối tuần), crypto (hiếm, vì 24/7 — nhưng có thể có giữa các sàn). ICT có hệ thuật ngữ riêng cho loại này: **NDOG / NWOG** ([[23-New-Day-Opening-Gap]], [[24-New-Week-Opening-Gap]]), opening gap, breakaway gap ([[06-Breakaway-Gap]]).

### 2.2 Vì sao FVG được gọi là "gap" dù thị trường giao dịch liên tục? **[MATHEMATICAL]**

![[FVG-Deep-01-Mot-Nen-Di-Qua.svg|720]]
*FVG-Deep-01: Vùng 100–102 không trống — nến 2 đã đi qua toàn bộ nó. "Gap" là: nến 1 và nến 3 không chạm vào vùng này, nên thời gian giá ở lại đây rất ngắn (panel phải — minh họa).*

**Chứng minh ngắn gọn** (bullish FVG, thị trường liên tục, open nến sau = close nến trước):

1. Open₂ = Close₁, và Close₁ ≤ High₁ (close luôn nằm trong range của nến) ⇒ **Open₂ ≤ H₁**.
2. Close₂ = Open₃, và Open₃ ≥ Low₃ ⇒ **Close₂ ≥ L₃**.
3. FVG nghĩa là H₁ < L₃. Nến 2 bắt đầu ở mức ≤ H₁ và kết thúc ở mức ≥ L₃ ⇒ **đường giá trong nến 2 đã đi qua mọi mức giữa H₁ và L₃** (giá đi qua các mức theo tick liên tiếp — có thể bỏ vài tick trống trong sổ lệnh, nhưng không bỏ cả một vùng).

∎ Vậy "gap" **không phải** khoảng trống giữa các giao dịch. Nó là **khoảng trống giữa phạm vi của nến 1 và phạm vi của nến 3** — hai nến kề bên đại diện cho giao dịch "trước" và "sau" cú đẩy. Vùng này chỉ được giao dịch:
- trong **một** khoảng thời gian (nến 2),
- theo **một** chiều (đi lên, với bullish),
- và (thường) **nhanh**.

**Ngoại lệ:** nếu giữa các nến có session gap (Open₂ ≠ Close₁ hoặc Open₃ ≠ Close₂ vì thị trường đóng cửa), một phần vùng có thể thật sự không có giao dịch — khi đó FVG trùng một phần với opening gap. Đây là lý do FVG quanh giờ mở phiên của futures/cổ phiếu, và FVG có nến chủ nhật của FX, cần gắn nhãn riêng (xem EC2 của v1 ở §33.6).

### 2.3 Ba loại "khoảng trống" khác nhau ở chỗ có giao dịch hay không

![[FVG-Deep-03-FVG-vs-Gap-vs-VI.svg|720]]
*FVG-Deep-03: Opening gap (không có giao dịch trong vùng) ≠ FVG (có, nhưng chỉ trong nến 2, một chiều) ≠ Volume imbalance (có — bóng nến chồng lấp, chỉ thân không chạm).*

| Câu hỏi | Opening / session gap | Fair Value Gap | Volume imbalance (ICT) |
|---|---|---|---|
| Số nến xác định | 2 | 3 | 2 |
| Điều kiện | Open₂ ≠ Close₁ do thị trường đóng | H₁ < L₃ (bull) | Thân 2 nến không chạm, bóng chạm |
| Có giao dịch trong vùng? | **Không** (trên venue đó) | **Có**, chỉ trong nến 2 | **Có**, bởi bóng nến |
| Phụ thuộc phiên? | Có | Không | Không (nhưng hay gặp quanh open) |
| Quan sát được từ OHLC? | Có | Có | Có |
| ICT gọi là | NDOG / NWOG / opening gap | FVG — BISI / SIBI | Volume imbalance |

### 2.4 Hệ quả của định nghĩa "chỉ một nến đi qua"

1. **FVG phụ thuộc khung thời gian.** Cùng một đường giá, gộp thành nến M5, M15 hay H1 cho các FVG khác nhau. Trên random walk: tần suất FVG giảm dần khi mỗi nến chứa nhiều bước hơn — **37.9** FVG/100 nến (nến 5 bước) → **30.9** (15) → **26.5** (60) → **24.7** (240) (FVG-Sim-01) **[SIMULATION]**.
2. **FVG phụ thuộc mốc đóng nến.** Dịch mốc đóng nến H1 một giờ (broker GMT+2 vs GMT+3) có thể làm xuất hiện hoặc biến mất một FVG từ cùng dữ liệu M1 (hình EdgeB của v1 ở §27.5).
3. **FVG là vùng ít thời gian tại mức giá — theo định nghĩa.** Trên random walk, thời gian/đơn vị giá bên trong H1 FVG trung vị **0.56×** phần còn lại của ba nến (IQR 0.37–0.83) (FVG-Sim-06B). Vì vậy "FVG có ít giao dịch" không cần giải thích bằng "tổ chức để lại" — nó là cách FVG được chọn ra.

---

## 3. "Fair value" nghĩa là gì?

Brief yêu cầu không mặc định *fair value = equilibrium*. Đây là năm nghĩa khác nhau của cùng một cụm từ.

### 3.1 Nghĩa thường ngày
"Giá hợp lý" — giá mà người mua và người bán đều thấy chấp nhận được. Mơ hồ, mang tính chủ quan.

### 3.2 Kinh tế học & tài chính: fundamental value và thị trường hiệu quả
Giá trị nội tại (intrinsic/fundamental value) = giá trị hiện tại của dòng tiền kỳ vọng, hoặc kỳ vọng của giá trị tài sản dựa trên mọi thông tin hiện có. Giả thuyết thị trường hiệu quả (Fama, 1970) nói rằng giá phản ánh thông tin sẵn có; dạng yếu: không thể dự báo lợi nhuận vượt trội từ lịch sử giá. **Theo nghĩa này, nếu FVG dự báo được giá sau chi phí giao dịch, đó chính là một "inefficiency" của thị trường** — trớ trêu thay, đó là điều ICT muốn khai thác, chứ không phải điều FVG mô tả.

### 3.3 Kế toán (IFRS 13 / ASC 820)
Fair value = giá sẽ nhận được khi bán một tài sản (hoặc trả để chuyển một nghĩa vụ) trong một giao dịch có trật tự giữa các bên tham gia thị trường tại ngày đo lường — một "exit price". Không liên quan tới FVG.

### 3.4 Auction Market Theory
"Value" = nơi thị trường dành nhiều thời gian/khối lượng nhất (value area ~70% hoạt động). Giá xa value nhanh và ngắn ngủi = "excess" hoặc "single prints". **Đây là nghĩa gần ICT nhất**: vùng FVG là vùng giá *không* được thị trường dành thời gian để "đồng ý" — nhưng AMT không gọi nó là "unfair".

### 3.5 Vi cấu trúc thị trường
Trong các mô hình Kyle (1985) / Glosten–Milgrom (1985), có một "efficient price" (kỳ vọng của giá trị tài sản theo thông tin công khai); giá giao dịch lệch khỏi nó do spread và tác động tạm thời của lệnh. Farmer, Gerig, Lillo & Waelbroeck (2013) đưa ra **"fair pricing condition"**: với một metaorder, *giá thực hiện trung bình bằng giá cuối cùng sau khi tác động tạm thời đã phai* — nghĩa là người tạo cú đẩy không lời không lỗ chỉ vì kích thước lệnh. Hệ quả của điều kiện này: giá sau khi metaorder kết thúc **hồi về khoảng 2/3 đỉnh tác động**. Đây là khái niệm "fair" có nội dung định lượng gần với câu chuyện "giá quay lại" nhất — nhưng nó nói về *mức hồi của cú đẩy*, không về *trung điểm của một gap 3 nến* (xem §16).

### 3.6 ICT
**[ICT FRAMEWORK]** Theo transcript bài Month 04 của ICT Mentorship Core Content:

> *"A fair value gap is a range in price delivery where one side of the market liquidity is offered. It is typically confirmed with a liquidity void on the lower time frame charts in the same range of price. Price can actually gap to create a literal vacuum of trading thus posting an actual price gap."*

Cùng nguồn, ICT mô tả vùng đó là *"an exposed area that only delivered on the downside"* và nói rằng *"a pocket of porous price action… will eventually want to trade back up into [the] little gapped area so we expect price to fill in that area."* (trích qua bản tóm tắt transcript — Tier 3/4).

Đọc kỹ, ICT dùng "fair" theo nghĩa: **giá "công bằng" là giá được chào cho cả hai phía (buyside và sellside)**; FVG là đoạn giá chỉ được chào một phía. Từ đó có cặp thuật ngữ **BISI** (Buyside Imbalance, Sellside Inefficiency — bullish FVG: phía mua áp đảo, phía bán "không được phục vụ hiệu quả") và **SIBI** (ngược lại).

### 3.7 Kết luận

| Nghĩa của "fair value" | Đo bằng gì | FVG có nói giá trong vùng là "unfair" theo nghĩa này? |
|---|---|---|
| Thường ngày | Cảm nhận | Không xác định |
| Kinh tế học / EMH | Kỳ vọng giá trị theo thông tin | **Không** — FVG không chứa thông tin về giá trị cơ bản |
| Kế toán | Exit price trong giao dịch có trật tự | Không liên quan |
| Auction Market Theory | Thời gian/khối lượng tại giá | Gần: vùng chưa được "chấp nhận" — nhưng không gọi là unfair |
| Vi cấu trúc (efficient price, fair pricing) | Giá sau khi tác động tạm thời phai | Gián tiếp: cú đẩy có thể chứa phần tạm thời — nhưng mức hồi không gắn với gap |
| ICT | Giá được chào hai phía hay một phía | **Có — theo định nghĩa riêng của ICT** |

> [!important] Kết luận §3
> "Fair Value Gap" là **thuật ngữ mô tả cách giá được giao (price delivery)**, không phải một tuyên bố định giá. Đừng để chữ "fair" khiến bạn nghĩ rằng giá "nợ" thị trường một lần quay lại. Câu hỏi đúng là thực nghiệm: *vùng một chiều này có hành xử khác vùng bình thường cùng khoảng cách không?*

---

## 4. "Inefficiency" và "imbalance" nghĩa chính xác là gì?

### 4.1 Inefficiency — hai nghĩa không được trộn

| | Inefficiency kiểu Fama (thông tin) | "Inefficiency" kiểu ICT (price delivery) |
|---|---|---|
| Nghĩa | Có thể dự báo lợi nhuận vượt trội từ thông tin sẵn có | Một đoạn giá chỉ được giao một chiều |
| Kiểm chứng | Thống kê lợi nhuận sau chi phí | Quan sát trực tiếp trên chart |
| Quan hệ với FVG | **Nếu** FVG có edge sau phí → đó là inefficiency kiểu Fama | FVG **là** inefficiency kiểu ICT theo định nghĩa |

Hệ quả logic: câu "giá quay lại để lấp inefficiency" dùng chữ inefficiency theo nghĩa ICT (mô tả) để ngầm tuyên bố một inefficiency theo nghĩa Fama (dự báo được). Hai thứ đó phải được kiểm chứng riêng.

### 4.2 Bảy "imbalance" khác nhau

| Thuật ngữ | Định nghĩa | Quan sát được từ | Ghi chú |
|---|---|---|---|
| **Order imbalance / OFI** | Chênh lệch dòng lệnh mua vs bán (chủ động, hoặc tại mức tốt nhất) | Dữ liệu trade/quote, tick | Cont et al. 2014: giải thích phần lớn thay đổi giá ngắn hạn **[MARKET MECHANICS]** |
| **Volume imbalance (footprint)** | Tại một mức giá, volume mua chủ động ≫ bán chủ động (vd tỷ lệ 3:1, "stacked imbalances") | Footprint / order flow | Công cụ gần nhất để *kiểm chứng* một FVG |
| **Volume imbalance (ICT)** | Hai nến liên tiếp: thân không chạm, bóng chạm | OHLC | Tên trùng nhưng là khái niệm khác hẳn dòng trên |
| **Price imbalance (ICT)** | Dùng gần như đồng nghĩa với FVG | OHLC | — |
| **Liquidity imbalance** | Độ sâu bid vs ask lệch nhau | Sổ lệnh L2 | Có giá trị dự báo rất ngắn hạn trong nghiên cứu vi cấu trúc |
| **Market imbalance (AMT)** | Một phía áp đảo → one-timeframing, giá rời value | TPO, volume profile | Gần với ý nghĩa "imbalance" mà ICT muốn nói |
| **Inventory imbalance** | Vị thế của market maker lệch | Không công khai | Dùng trong lập luận v1 §14.2 — **[INTERPRETATION]** |

### 4.3 FVG có phải imbalance không?

- **Theo nghĩa ICT:** có, theo định nghĩa (FVG ≡ price imbalance).
- **Theo nghĩa order flow:** *có thể*. Một nến 2 lớn **tương thích** với OFI lớn trong khung thời gian đó (Cont et al.), nhưng cũng tương thích với sổ mỏng + OFI vừa phải, hoặc với một chuỗi stop bị kích hoạt. OHLC không cho phép kết luận dòng lệnh đã mất cân bằng bao nhiêu.
- **Tránh định nghĩa vòng tròn:** "FVG là imbalance" + "imbalance là thứ tạo ra FVG" = không nói gì. Định nghĩa vận hành trong note này (DEF-FVG-01, §5.7) chỉ dùng OHLC; mọi liên hệ với order flow được gắn nhãn.

> [!tip] Cách kiểm chứng "imbalance" thật sự (nếu có dữ liệu)
> Với NQ/ES (dữ liệu CME), footprint chart hoặc dữ liệu tick cho phép đo: (1) volume trong vùng FVG / volume trung bình mỗi mức của ba nến; (2) tỷ lệ mua/bán chủ động trong nến 2; (3) thời gian giá ở trong vùng. Một FVG "thật" theo nghĩa order flow sẽ có (1) thấp, (2) lệch mạnh, (3) ngắn. v1 §14.3 đã gợi ý dùng footprint để lọc FVG "ảo ảnh gộp nến" — đó là một hướng **[HYPOTHESIS]** đáng test (HYP-FVG-012).

---

# PART II — KHÁI NIỆM CỐT LÕI

## 5. FVG chính xác là gì? — sáu tầng giải thích

### 5.1 L1 — Trực giác
Một chiếc xe đang chạy chậm trong phố (nhiều điểm dừng — giá đi qua lại), bỗng phóng rất nhanh qua một đoạn đường cao tốc (không dừng chỗ nào), rồi lại chạy chậm ở khu phố mới. Nếu bạn đánh dấu những chỗ xe *dừng lại*, đoạn cao tốc sẽ trống trơn. **FVG là đoạn "cao tốc" đó trên trục giá**: xe *có* đi qua, nhưng không dừng.

> Ẩn dụ không nói xe sẽ quay lại đoạn cao tốc. Xe quay lại hay không tùy vì sao nó phóng nhanh (đi cấp cứu, quên đồ, hay đã tới nơi) — §13, §30.

### 5.2 L2 — Chuỗi giá đơn giản

```text
           Nến 1          Nến 2              Nến 3
Open        99.0           99.6              103.0
High       100.0  ←H₁     103.4              104.2
Low         98.0           99.4              102.0  ←L₃
Close       99.6          103.0              103.8

Điều kiện bullish FVG:  L₃ = 102.0  >  H₁ = 100.0   ✓
Vùng FVG = [100.0, 102.0]   proximal = 102.0   distal = 100.0   CE = 101.0   size = 2.0
Biết được khi: nến 3 đóng cửa (không sớm hơn)
```

Đọc từng bước:
1. Nến 1 không bao giờ lên trên 100.0.
2. Nến 2 bắt đầu ở 99.6 (≤ 100), kết thúc ở 103.0 (≥ 102) → đi qua toàn bộ 100–102 **trong khung thời gian của chính nó**.
3. Nến 3 không bao giờ xuống dưới 102.0.
4. Vậy đoạn 100–102 chỉ có nến 2 đi qua. Đó là bullish FVG.

### 5.3 L3 — Thuật ngữ trading
- **Bullish FVG (BISI):** L₃ > H₁, vùng [H₁, L₃], nằm *dưới* giá sau khi hình thành → nếu giá retrace xuống, chạm proximal (L₃) trước.
- **Bearish FVG (SIBI):** H₃ < L₁, vùng [H₃, L₁], nằm *trên* giá → retrace lên chạm proximal (H₃) trước.
- **Displacement:** nến (hoặc chuỗi nến) lớn, nhanh, một chiều — thường là nến 2 (§10).
- **Retracement / touch / fill / CE / full fill / invalidation / IFVG:** §14, §19.
- **Mitigation:** trong ICT dùng lỏng — xem §17 để có định nghĩa tách bạch.

### 5.4 L4 — Cơ chế thị trường: nến 2 đã đòi hỏi điều gì?
Để giá đi từ ≤ H₁ tới ≥ L₃ trong một khung nến, **lượng lệnh chủ động một chiều trong khung đó phải lớn hơn lượng thanh khoản đối diện mà sổ lệnh có sẵn và kịp bổ sung trên quãng đường đó** (§1.2). Có ít nhất năm nguồn khả dĩ (không loại trừ nhau):

| Nguồn | Mô tả | Quan sát được từ OHLC? |
|---|---|---|
| Thông tin mới | Tin vĩ mô, dữ liệu, tin doanh nghiệp → nhiều người cùng cập nhật giá | Một phần (giờ tin) |
| Nhu cầu thanh khoản | Một bên buộc phải mua/bán gấp (thanh lý, hedge, rebalance) | Không |
| Metaorder | Lệnh lớn đang được chia nhỏ thực thi; một đoạn thực thi dồn dập | Không |
| Stop / liquidation cascade | Giá chạm cụm stop → lệnh market dây chuyền (Osler 2005) | Gián tiếp (vị trí so với mức nổi bật) |
| Sổ mỏng + nhiễu | Thanh khoản rút đi (giờ thấp điểm, trước tin) → lệnh vừa phải cũng đẩy xa | Gián tiếp (session) |

Và một nguồn "rẻ" nhất: **nhiễu đủ lớn** — random walk cũng tạo nến 2 lớn và FVG (FVG-Sim-01).

### 5.5 L5 — Cách ICT dùng FVG **[ICT FRAMEWORK]**
- Định nghĩa (transcript): *"a range in price delivery where one side of the market liquidity is offered… typically confirmed with a liquidity void on the lower time frame charts"*.
- Thuộc nhóm **PD Arrays** (Premium/Discount arrays) — các vùng giá tham chiếu cùng với Order Block, Breaker, Mitigation Block, Liquidity Void, BPR…
- Vai trò trong ICT 2022 Model: sau liquidity sweep + displacement + MSS, FVG của leg displacement là **vùng chờ retrace để vào lệnh**; HTF FVG còn mở được dùng như **draw/target**.
- Các mức trong FVG: proximal, **CE (consequent encroachment, 50%)**, distal; "quadrants" 25/50/75%.
- FVG thất bại (bị đóng cửa xuyên qua) → **Inversion FVG** ([[17-Inverse-Fair-Value-Gap-iFVG]]).

### 5.6 L6 — Giới hạn: chart không cho phép kết luận gì
- Không kết luận được **ai** tạo nến 2, hay "smart money" có tham gia không.
- Không kết luận được vùng "không có giao dịch" (§2.2 chứng minh điều ngược lại).
- Không kết luận được còn **lệnh chờ** trong vùng.
- Không kết luận được giá **sẽ** quay lại — chỉ có xác suất, và đường nền của xác suất đó là hình học (§13, §15).
- Không kết luận được FVG "mạnh" hay "yếu" theo nghĩa nhân quả — chỉ có các biến tương quan cần kiểm định (§30).

### 5.7 Định nghĩa vận hành v0.1 — DEF-FVG-01 (cho journal và code)

**[MATHEMATICAL]** Với chuỗi nến cùng khung, chỉ số i là nến 3:

```text
Bullish FVG tại i  ⇔  L[i] > H[i−2]          zone = [H[i−2], L[i]]   proximal = L[i]   distal = H[i−2]
Bearish FVG tại i  ⇔  H[i] < L[i−2]          zone = [H[i], L[i−2]]   proximal = H[i]   distal = L[i−2]
size = |proximal − distal|     size_atr = size / ATR14[i]     CE = (proximal + distal) / 2
known_at = close của nến i     id = (symbol, timeframe, i, direction)
```

Các lựa chọn thiết kế và lý do:

| Câu hỏi | Lựa chọn v0.1 | Phương án khác | Lý do / đánh đổi |
|---|---|---|---|
| Wick hay body? | **Wick** (High/Low) | Body (open/close) | Wick là định nghĩa ICT chuẩn; body-gap cho vùng rộng hơn, nhiều hơn và trùng với "volume imbalance" — trộn hai khái niệm |
| Bất đẳng thức chặt (>)? | **Có** (L₃ > H₁) | ≥ | Zero-size gap không có vùng để giao dịch; ≥ chỉ thêm nhiễu |
| Kích thước tối thiểu? | **size ≥ 0.25·ATR14** cho setup; ghi lại mọi FVG ≥ 1 tick cho thống kê | ATR %, số tick cố định, % giá | ATR chuẩn hóa giữa các thị trường/khung. 0.25 là **HEURISTIC**: trên random walk, ~20 FVG/100 nến vẫn vượt ngưỡng này (FVG-Sim-01) — ngưỡng KHÔNG lọc nhiễu, chỉ lọc vùng quá hẹp để đặt lệnh |
| Nến 2 bắt buộc displacement? | **Không** trong định nghĩa; **ghi lại** `c2_range_atr`, `c2_body_atr` như biến | Bắt buộc range ≥ k·ATR | Tách "FVG là gì" khỏi "FVG nào đáng dùng". Nếu gộp, không còn kiểm định được displacement có thêm thông tin không (HYP-FVG-001) |
| Nến 1 và nến 3 có điều kiện? | Không | Màu nến, body tối thiểu | Không có cơ sở; ghi lại làm biến nếu cần |
| Cùng khung? | **Bắt buộc** — 3 nến cùng timeframe | Trộn khung | Trộn khung = định nghĩa khác (nesting, §27) |
| Session gap giữa các nến? | **Gắn cờ** `session_gap = true` | Loại bỏ | FVG chứa opening gap có cơ chế khác (một phần là literal gap) |
| Tin tức? | **Gắn cờ** `news_window = true` (±5 phút quanh tin high-impact) | Loại bỏ | v1 W1/EC3: chất liệu khác; giữ để kiểm định riêng |
| Khi nào biết? | **Close nến 3** | Trong nến 3 | Mọi thứ sớm hơn là look-ahead (§21) |

> [!example] Ví dụ áp dụng DEF-FVG-01
> EURUSD M15, ATR14 = 0.00080. Nến 1 High = 1.08412; nến 3 Low = 1.08455 → bullish, size = 0.00043 = **0.54·ATR** ≥ 0.25 → đủ điều kiện setup. CE = 1.084335. known_at = close nến 3. Ghi: `c2_range_atr = 2.1`, `session = London`, `news_window = false`. **Chưa** nói gì về chất lượng — chỉ là một ứng viên.

### 5.8 Định nghĩa của v1 *(v1 §1, nguyên văn — có chú thích v2 bên dưới)*

![[FVG-Sec-01-Dinh-Nghia.svg|720]]
*Sơ đồ: Cấu trúc 3 nến của Bullish FVG (BISI) và Bearish FVG (SIBI); mức CE (50%) là tham chiếu quan trọng nhất.*

**Khái niệm:**  
Fair Value Gap là một vùng **imbalance** trên chart, hình thành khi giá di chuyển một chiều quá mạnh và quá nhanh (single-sided delivery / displacement), khiến một phần khoảng giá không được giao dịch đầy đủ ở cả hai phía. FVG được nhận diện qua **3 nến liên tiếp**:

- **Bullish FVG (BISI — Buyside Imbalance Sellside Inefficiency):** khoảng trống giữa **HIGH của nến 1** và **LOW của nến 3**, với **nến 2** là nến displacement tăng mạnh. Khoảng giữa hai mức này chưa được cân bằng bởi phía bán → giá có xu hướng quay lại lấp nó.
- **Bearish FVG (SIBI — Sellside Imbalance Buyside Inefficiency):** khoảng trống giữa **LOW của nến 1** và **HIGH của nến 3**, với **nến 2** là nến displacement giảm mạnh.

**Bản chất:** FVG là một dạng **price inefficiency**. Trong một thị trường "fair", giá nên giao dịch đủ ở cả hai phía. Khi displacement xảy ra, giá nhảy qua một vùng mà không có sự tham gia đầy đủ của bên đối diện → vùng đó "kém hiệu quả" (inefficient). Logic ICT là thị trường có xu hướng quay về **rebalance** vùng imbalance này trước khi tiếp tục delivery.

**CE (Consequent Encroachment):** là mức **50% của gap** — mức quan trọng nhất để xác nhận phản ứng. Giá thường tôn trọng CE: nếu chỉ retrace tới CE rồi reject, đó là dấu hiệu FVG đang được "respect". CE còn là điểm tham chiếu để chia một FVG lớn thành hai nửa premium/discount nội bộ.

**Mục đích trong ICT:**  
- Là **POI (Point of Interest)** để vào lệnh: chờ giá retrace về FVG rồi tìm entry.
- Là **DRAW on liquidity / draw on price**: giá bị hút về lấp FVG hoặc rebalance imbalance còn mở.
- Là bằng chứng của **intent**: một FVG sinh ra từ displacement phá cấu trúc cho thấy có "chủ đích" đẩy giá.
- Là vùng đặt **stop loss logic**: stop thường nằm ngoài đầu kia của FVG / đầu displacement.

**Vì sao khái niệm này quan trọng:**  
FVG là một trong những PD Array trung tâm của ICT 2022 model. Nhưng chính vì dễ thấy, nó là khái niệm bị **lạm dụng** nhiều nhất: trader vẽ FVG khắp nơi và trade mọi gap. FVG chỉ có edge khi đặt trong narrative HTF + liquidity + premium/discount đúng — giống hệt triết lý của [[59-Daily-Bias]].

**Nó giúp trả lời câu hỏi nào trên chart?**
- Sau displacement, giá có khả năng retrace về đâu để tìm entry?
- Imbalance nào còn mở mà giá có thể bị hút về (draw)?
- Mức 50% (CE) nào giá đang tôn trọng?
- FVG này có "chất lượng" không, hay chỉ là gap ngẫu nhiên giữa range?
- FVG đã bị xuyên thủng và đảo cực (IFVG) chưa?

> [!note] Chú thích v2 cho định nghĩa v1
> | Câu trong v1 | Nhãn v2 | Ghi chú |
> |---|---|---|
> | "một phần khoảng giá không được giao dịch đầy đủ ở cả hai phía" | **[ICT FRAMEWORK]** — hợp lý nếu hiểu là "ít giao dịch, một chiều" | KHÔNG có nghĩa là không có giao dịch (§2.2) |
> | "giá có xu hướng quay lại lấp nó" | **[MATHEMATICAL]** cho phần lớn; **[HYPOTHESIS]** cho phần vượt hình học | Random walk lấp 71% trong 20 nến (§15) |
> | "CE… mức quan trọng nhất… Giá thường tôn trọng CE" | **[HYPOTHESIS] — BACKTEST REQUIRED** | Hình học: CE "giữ" 31% số lần chạm (§16) |
> | "Là bằng chứng của intent" | **[INTERPRETATION]** | Nhiễu cũng tạo FVG; "intent" không quan sát được |
> | "Là DRAW… giá bị hút về" | **[HYPOTHESIS]** | "Hút" phải được đo so với vùng đối chứng cùng khoảng cách (HYP-FVG-010) |
> | "stop thường nằm ngoài đầu kia của FVG" | **[HEURISTIC]** hợp lý | Đây là quy tắc quản trị rủi ro, không phải claim về thị trường |
> | "FVG chỉ có edge khi đặt trong narrative HTF…" | **[HYPOTHESIS]** | Nhất quán với kết quả mô phỏng (FVG một mình không hơn đối chứng trên nhiễu) nhưng "có edge khi có context" chưa được chứng minh |

### 5.9 FVG không phải là gì

**v1 (nguyên văn):**

- Không phải "cứ thấy gap 3 nến là vào lệnh".
- Không phải tín hiệu độc lập — nó là điểm tham chiếu giá, cần context bias + liquidity.
- Không phải mọi FVG đều phải được lấp; chỉ imbalance phù hợp narrative mới là draw đáng tin.
- Không phải lý do bỏ qua premium/discount: Long ở FVG premium hay Short ở FVG discount thường là chase.
- Không phải bất biến — khi bị đóng nến xuyên qua, FVG có thể invalid hoặc đảo cực thành IFVG.
- Không thay thế cho liquidity sweep: FVG entry trước khi sweep thường bị quét stop.

**Bổ sung v2:**
- Không phải **vùng không có giao dịch** — nến 2 đã đi qua toàn bộ vùng (§2.2).
- Không phải **bằng chứng của tổ chức / smart money** — random walk tạo ~31 FVG/100 nến (§9).
- Không phải **liquidity** — liquidity là giả thuyết về nơi có lệnh; FVG là hình học của giá đã đi qua (§12).
- Không phải **Order Block** — OB là nơi cú đẩy bắt đầu; FVG là đoạn giữa cú đẩy (§12).
- Không phải **POI tự thân** — nó có thể là location *bên trong* một POI (§24).
- Không phải **một thực thể khách quan độc lập với khung thời gian và mốc đóng nến** (§2.4, §27).
- Không phải **một lời hứa** rằng giá sẽ quay lại — chỉ có xác suất, và đường nền của xác suất đó là khoảng cách (§13).

---

## 6. Vì sao cần đúng 3 nến?

### 6.1 Hình học của "trước — cú đẩy — sau"
Để nói "đoạn giá này chỉ được đi qua một lần, rất nhanh", ta cần:
- một **tham chiếu trước** cú đẩy (nến 1 — giá đã ở đâu),
- **chính cú đẩy** (nến 2),
- một **tham chiếu sau** cú đẩy (nến 3 — giá dừng lại ở đâu).

Vùng FVG là phần **không chồng lấp** giữa tham chiếu trước và tham chiếu sau. Ba nến là cửa sổ *nhỏ nhất* có cả "trước" lẫn "sau".

| Cửa sổ | Câu nó trả lời | Tên |
|---|---|---|
| Nến 1 → nến 2 | Nến 2 có mở cách nến 1 không? Thân có chạm không? | Opening gap / volume imbalance |
| Nến 2 → nến 3 | Nến 3 có quay lại vào nến 2 không? | Không có tên chuẩn — chỉ đo mức hồi |
| **Nến 1 → nến 3** (nến 2 ở giữa) | **Trước và sau cú đẩy có chạm nhau không?** | **FVG** |
| Nến j → nến k (k − j > 2) | Cả một leg có để lại đoạn không chồng lấp? | Liquidity void (nhiều FVG liên tiếp) |

### 6.2 Nến 2 có phải là FVG không?
**Không.** Nến 2 là *nến displacement* chứa FVG; FVG là một **khoảng con** của range nến 2 (§2.2). Hệ quả thực hành:
- Size FVG ≤ range nến 2 − (phần nến 1 đã đi trong range nến 2) − (phần nến 3 đã đi trong range nến 2).
- Cùng một nến 2 dài, FVG có thể rộng (nến 1 và nến 3 có bóng ngắn) hoặc không tồn tại (nến 3 hồi sâu) — FVG-Deep-04 panel "Displacement KHÔNG có FVG".

### 6.3 Vì sao không phải 2 nến, hay 4 nến?
- **Điều kiện hình học tương đương** (bullish): Close₂ − Open₂ > (H₁ − Close₁) + (Open₃ − L₃). Đọc thành lời: **thân nến 2 phải dài hơn tổng của bóng trên nến 1 (tính từ close) và bóng dưới nến 3 (tính từ open)**. Nói cách khác, FVG xảy ra khi cú đẩy của nến 2 *vượt* những dao động hai bên. Đây là lý do FVG nhạy với nến 1/nến 3 có bóng ngắn — không chỉ với nến 2 lớn.
- **3 nến là một lựa chọn độ phân giải**, không phải định luật. Dùng 4 nến (H₁ < L₄ với nến 2–3 là cú đẩy) cho ra các "gap hai nến đẩy" — tương đương FVG trên khung gấp đôi. Đây chính là vì sao FVG phụ thuộc khung thời gian.

---

## 7. Bullish FVG và Bearish FVG — từ số 0

![[FVG-Deep-02-Bullish-Bearish-OHLC.svg|720]]
*FVG-Deep-02: Bullish (BISI) và Bearish (SIBI) đọc bằng số OHLC. Proximal = mép giá chạm trước khi retrace; distal = mép xa.*

### 7.1 Bullish FVG (BISI)

```text
Candle 1                 Candle 2                    Candle 3
High = 100  ─┐           BIG BULLISH MOVE            Low = 102 ─┐
             │           99.6 ─────────▶ 103.0                  │
                                                                
102 ────────────────────────────── proximal (L₃)
      ▲
      │  bullish FVG [100, 102]   CE = 101
      ▼
100 ────────────────────────────── distal (H₁)
```

- **Vì sao "bullish"?** Vì cú đẩy tạo ra nó đi lên và vùng nằm *dưới* giá sau khi hình thành. Nếu giá quay xuống, đây là nơi ICT kỳ vọng phản ứng tăng (hỗ trợ) — **[ICT FRAMEWORK]**; kỳ vọng đó là **[HYPOTHESIS]**.
- **Hành vi giá tạo ra nó [OBSERVABLE]:** nến 2 đi lên một mạch qua 100–102; nến 3 giữ trên 102 suốt khung của nó. Phần sau ("nến 3 giữ trên 102") quan trọng không kém phần trước: nến 3 *không hồi về* là một nửa của định nghĩa.

### 7.2 Bearish FVG (SIBI)

```text
Candle 1                 Candle 2                    Candle 3
Low = 100   ─┘           BIG BEARISH MOVE            High = 98 ─┘
                         100.4 ────────▶ 97.0

100 ────────────────────────────── distal (L₁)
      ▲
      │  bearish FVG [98, 100]   CE = 99
      ▼
 98 ────────────────────────────── proximal (H₃)
```

- Vùng nằm *trên* giá sau khi hình thành; retrace lên chạm proximal (98) trước.
- Đối xứng hoàn toàn: mọi kết quả mô phỏng trong note được tính gộp hai chiều bằng cách lấy dấu (`d = ±1`).

### 7.3 Cách đọc proximal/distal để không nhầm
"Mép trên/mép dưới" đảo nghĩa giữa bullish và bearish. Luôn dùng **proximal** (mép chạm trước) và **distal** (mép xa, nơi đặt stop/invalidation). v1 §7.2 đã đưa quy ước này — giữ nguyên.

---

## 8. FVG hình thành như thế nào — và vì sao nó không phải "lỗ hổng"

### 8.1 Chuỗi hình thành — đánh giá từng mũi tên

```text
Compression / Balance        (nến chồng lấp, giá ở value)
        ↓   [không bắt buộc]
Aggressive price movement    (dòng lệnh một chiều > thanh khoản kịp bổ sung)
        ↓
Displacement                 (nến 2 lớn so với ATR)
        ↓   [không chắc chắn: cần nến 1/3 không chạm]
Reduced overlap              (H₁ < L₃)
        ↓
FVG identified               (tại close nến 3)
```

| Mũi tên | Bắt buộc? | Ghi chú |
|---|---|---|
| Balance → movement | Không | FVG hình thành cả giữa trend (continuation) |
| Movement → displacement | Gần như (theo nghĩa nến 2 lớn hơn bóng hai bên) | Nhưng 78% FVG có nến 2 < 1.5 ATR (FVG-Sim-01) |
| Displacement → reduced overlap | Không | Nến 3 có thể hồi sâu → không có FVG (FVG-Deep-04) |
| Reduced overlap → FVG | Có (định nghĩa) | Chỉ biết tại close nến 3 |

### 8.2 "Untraded interval" — câu sai phổ biến nhất về FVG

| Câu nói | Đúng / sai | Vì sao |
|---|---|---|
| "Không có candle overlap giữa nến 1 và nến 3 trong vùng" | **Đúng** [OBSERVABLE] | Định nghĩa |
| "Vùng giá chỉ được giao dịch trong một nến, một chiều" | **Đúng** [MATHEMATICAL] (thị trường liên tục) | §2.2 |
| "Ít thời gian / ít volume tại các mức trong vùng" | **Thường đúng** (theo cách FVG được chọn ra) | Sim-06B: trung vị 0.56× |
| "Không có giao dịch nào trong vùng" | **Sai** (trừ khi có session gap / halt) | Nến 2 đi qua vùng |
| "Lệnh limit trong vùng không được khớp, vẫn còn chờ" | **Sai như mặc định** | Lệnh limit nằm sẵn trong vùng sẽ bị nến 2 khớp khi giá đi qua; chỉ lệnh đặt *sau* mới có thể chờ ở đó |
| "Thị trường 'nợ' vùng đó một lần giao dịch nữa" | **Không có cơ sở** | Không có cơ chế nào "ghi nợ"; quay lại là xác suất (§13) |

### 8.3 Khi nào có "lỗ hổng" thật?
- **Session/opening gap** giữa nến (futures mở phiên, cổ phiếu, FX cuối tuần) — một phần vùng thật sự không có giao dịch.
- **Halt / limit-up-limit-down** (futures, cổ phiếu Mỹ).
- **Tin tức với quote đóng băng / spread giãn** — giá nhảy qua nhiều mức trong vài mili-giây; sổ lệnh rỗng thật (v1 W1, EC3).
- **Feed tổng hợp (CFD)** có spike không có trên thị trường gốc (v1 EC1).
- **Tài sản thanh khoản rất mỏng** (altcoin) — các mức trống trong sổ lệnh rộng.

Trong những trường hợp này, FVG có *chất liệu* khác — và hành vi có thể khác — nên v0.1 gắn cờ `session_gap`, `news_window`, `feed` thay vì gộp chung.

### 8.4 Cơ chế theo v1 §14.1 *(v1, nguyên văn — có chú thích v2)*

![[FVG-Deep-Mechanism.svg|720]]
*Sơ đồ: Vì sao gap 3 nến tồn tại trên feed aggregated dù orderbook thật không có "khoảng trống" tuyệt đối — limit order vacuum, market maker inventory skew và phản ứng dealer hedging.*

Đây là điều hầu hết tài liệu ICT không nói rõ: **một FVG trên chart candlestick không có nghĩa là "không ai giao dịch ở mức giá đó."** Order book của bất kỳ thị trường điện tử nào (CME, LMAX, Binance) luôn có một mức giá tốt nhất (best bid/ask) tại mọi thời điểm — không có "lỗ hổng" giá theo nghĩa vật lý. Cái mà FVG thực sự đo là: **tốc độ dịch chuyển của trục giá này nhanh hơn tốc độ limit order mới được đặt vào để lấp đầy các mức đã đi qua.**

Cơ chế cụ thể:
- Khi một lệnh market lớn (hoặc chuỗi lệnh market aggressor) quét qua nhiều mức giá trong sổ lệnh liên tiếp trong thời gian cực ngắn (vài trăm ms đến vài giây), nó tiêu thụ hết thanh khoản limit đang chờ ở các mức đó.
- Market maker/liquidity provider **không kịp** (hoặc chủ động không) đặt lại limit order mới vào đúng những mức vừa bị quét, vì rủi ro bị "adverse selection" — nếu vừa đặt lại ngay sau một cú sweep định hướng mạnh, họ dễ bị ăn tiếp bởi dòng lệnh cùng hướng.
- Kết quả: trên **feed nến aggregated (M1, M5...)**, ba nến liên tiếp cho thấy high nến 1 và low nến 3 không chồng lấp — không phải vì "không ai trade ở đó", mà vì **volume tại các mức giá trung gian trong khung thời gian tạo nến 2 thấp bất thường so với hai bên**, và trên chart OHLC ta chỉ thấy được biên chứ không thấy được mật độ giao dịch bên trong.
- Đây chính là lý do một FVG **không xuất hiện giống nhau trên các độ phân giải khác nhau**: FVG rõ trên M15 có thể "biến mất" khi zoom vào M1, vì trên M1 ta thấy nhiều nến nhỏ hơn đã lấp một phần mức giá trung gian mà M15 gộp lại thành một cây nến displacement.

> [!important] Hệ quả thực chiến
> FVG là **hiện tượng của khung thời gian bạn đang nhìn**, không phải một sự thật tuyệt đối về orderbook. Một trader dùng M5 và một trader dùng M15 có thể thấy hai FVG khác hẳn nhau tại cùng một thời điểm — cả hai đều "đúng" theo khung của họ. Đây là lý do tuyệt đối không nên tranh cãi "FVG có tồn tại hay không" mà không nêu rõ timeframe.

> [!note] Chú thích v2 cho v1 §14.1
> Phần này của v1 **đúng về hướng** và là nền cho §2.2 của v2: FVG đo việc giá dịch chuyển nhanh hơn tốc độ thanh khoản được bổ sung; FVG phụ thuộc độ phân giải. Hai điểm cần chỉnh: (1) câu "một FVG rõ trên M15 có thể 'biến mất' khi zoom vào M1" nên đọc là "*vùng đó vẫn chỉ được đi qua trong thời gian của nến 2 M15, nhưng trên M1 nó được chia cho nhiều nến M1 chồng lấp nhau*" — và trên random walk, 98% H1 FVG vẫn chứa ít nhất một M5 FVG cùng chiều (FVG-Sim-06A); (2) "volume tại các mức giá trung gian thấp bất thường" là **[HYPOTHESIS]** cần footprint để kiểm chứng — OHLC chỉ bảo đảm *thời gian* ngắn, không bảo đảm *volume* thấp.

---

# PART III — VÌ SAO FVG TỒN TẠI?

## 9. Câu hỏi trung tâm: TẠI SAO Fair Value Gap tồn tại?

Brief yêu cầu không dừng ở "vì có khoảng trống giữa nến 1 và nến 3" (đó là định nghĩa). Câu trả lời có ba tầng — và chỉ tầng đầu tiên là chắc chắn.

### 9.1 Câu trả lời ba tầng

| Tầng | Câu trả lời | Độ chắc chắn |
|---|---|---|
| **Hình học** | FVG xuất hiện khi chuyển động ròng của nến 2 lớn hơn tổng các dao động "ngược" của nến 1 và nến 3 (§6.3). Nói gọn: **một nến giữa lớn so với hai nến kề bên**. | **[MATHEMATICAL]** — chắc chắn |
| **Cơ chế** | Nến giữa lớn so với hai bên xảy ra khi trong khung đó dòng lệnh chủ động một chiều vượt thanh khoản sẵn có và kịp bổ sung; trước và sau đó, giao dịch "bình thường" hơn. Nguyên nhân có thể: thông tin, nhu cầu thanh khoản, metaorder, stop cascade, sổ mỏng — hoặc nhiễu. | **[MARKET MECHANICS]** cho các cơ chế; **không quan sát được** cơ chế nào trong một FVG cụ thể |
| **Câu chuyện ICT** | "Smart money" giao giá một chiều, để lại inefficiency mà thuật toán sẽ quay lại rebalance. | **[ICT FRAMEWORK] / [INTERPRETATION]** — không kiểm chứng được từ chart |

### 9.2 Tầng hình học — FVG là "dấu chân" của nến giữa lớn hơn hai bên **[SIMULATION]**

![[FVG-Sim-01-Base-Rate-Footprint.png|900]]
*FVG-Sim-01: (A) FVG xuất hiện liên tục trong nhiễu thuần túy; (B) xác suất có FVG gần như là hàm số của kích thước nến 2 so với ATR; (C) phần lớn FVG rất nhỏ.*

Đọc hình:

1. **Panel A — tần suất trong nhiễu.** Ba null model (Gaussian, Student-t df = 3 đuôi dày, GARCH(1,1) có volatility clustering), nến 15 bước:

| FVG / 100 nến | Gaussian | Student-t(3) | GARCH(1,1) |
|---|---:|---:|---:|
| Mọi kích thước | 30.9 | 33.7 | 30.9 |
| ≥ 0.10 ATR | 26.1 | 28.7 | 25.9 |
| ≥ 0.25 ATR | 19.8 | 22.4 | 19.5 |
| ≥ 0.50 ATR | 11.8 | 14.0 | 11.5 |
| Kích thước trung vị | 0.37 ATR | 0.40 ATR | 0.36 ATR |

   → Trên một chart M5 một phiên New York (~78 nến), nhiễu thuần túy đã cho ~**24 FVG** (~9 FVG ≥ 0.5 ATR). Ngưỡng kích thước 0.25–0.5 ATR **không** lọc được nhiễu.

2. **Panel B — "dấu chân" của nến 2.** P(FVG cùng chiều nến 2 | range nến 2 / ATR): ~10% khi nến 2 < 0.5 ATR, ~50% quanh 1.4 ATR, **~88%** khi ≥ 2 ATR (Gaussian). Với GARCH đường cong thấp hơn (~72% khi ≥ 2 ATR): khi volatility tăng đột ngột, ATR (trung bình 14 nến cũ) chưa kịp tăng nên nến 2 "trông" lớn — nhưng nến 1 và nến 3 cũng lớn → ít FVG hơn. **FVG đo kích thước *tương đối* của nến 2 so với nến 1 và nến 3, không phải kích thước tuyệt đối.**

3. **Panel C — đa số FVG nhỏ, và đa số không đến từ displacement.** **78%** FVG trên random walk có nến 2 < 1.5 ATR; chỉ ~22% đến từ nến 2 "cỡ displacement".

**Hệ quả:** câu hỏi "vì sao FVG tồn tại?" ở tầng hình học có câu trả lời đơn giản đến mức gần như tầm thường: *vì giá biến động, và đôi khi một nến biến động nhiều hơn hai nến bên cạnh*. Mọi ý nghĩa thêm vào phải đến từ **cái gì đã làm nến đó lớn** — tầng cơ chế.

### 9.3 Tầng cơ chế — điều gì làm một nến lớn hơn hai nến kề bên? **[MARKET MECHANICS]**

| Cơ chế | Bằng chứng / nguồn | FVG sinh ra từ đó sẽ… (dự báo) |
|---|---|---|
| **Bùng nổ order flow imbalance** | Δp ≈ OFI / depth trên khoảng ngắn (Cont, Kukanov & Stoikov 2014) | Tùy dòng lệnh đó mang thông tin hay không |
| **Thanh khoản rút đi khi dòng lệnh "độc"** | Market maker giãn spread/rút lệnh khi flow toxicity cao (Easley, López de Prado & O'Hara 2012) | Cú đẩy dài hơn so với lượng lệnh; một phần có thể hồi khi thanh khoản quay lại |
| **Thông tin mới (tin theo lịch)** | Giá nhảy khi công bố số liệu; quote có thể đóng băng | Mức mới có thể giữ (thông tin vĩnh viễn) — nhưng spike quanh tin hay bị đảo nhanh (v1 W1) |
| **Metaorder đang được thực thi** | Dấu của order flow có trí nhớ dài vì lệnh lớn được chia nhỏ (Lillo & Farmer 2004); impact theo căn bậc hai, một phần tạm thời (Moro et al. 2009; Bershova & Rakhlin 2013) | Nếu còn đang thực thi → tiếp diễn cùng chiều; khi kết thúc → hồi khoảng ⅓ đỉnh tác động |
| **Nhu cầu thanh khoản không mang thông tin** | Giá phải nhượng bộ để có người nhận rủi ro; sau đó hồi (Grossman & Miller 1988; Campbell, Grossman & Wang 1993) | Bị lấp sâu/xuyên — "phần thưởng" cho người cung cấp thanh khoản |
| **Stop / liquidation cascade** | Stop tập trung quanh số tròn; vượt mức → giá chạy nhanh hơn, xa hơn (Osler 2003, 2005); flash event GBP 2016 (BIS 2017) | Cú đẩy quá đà do phản hồi dương; dễ hồi khi cascade kết thúc |
| **Volatility clustering** | GARCH — biến động tụ thành cụm | Không có hướng; chỉ làm FVG nhiều hơn trong cụm biến động |
| **Nhiễu** | Random walk | Không có gì để dự báo — chính là null model |

Hai kết luận quan trọng:
1. **Các cơ chế dự báo những điều ngược nhau.** Liquidity-driven → hồi lại (FVG bị lấp/xuyên). Information → giá ở mức mới, sau đó là nhiễu (FVG bị chạm theo hình học, không đặc biệt). Metaorder đang thực thi → tiếp diễn (FVG ít khi bị chạm). Llorente, Michaely, Saar & Wang (2002) cho thấy ở cổ phiếu: giao dịch volume cao do *hedging* thường đi kèm đảo chiều, do *đầu cơ có thông tin* thường đi kèm tiếp diễn — cùng một "nến lớn", hai tương lai.
2. **OHLC không cho biết cơ chế nào.** Đây là lý do FVG-Sim-03/04 xây một toy model ba loại displacement (§30.3) để thấy hệ quả của việc *không biết*.

### 9.4 Năm lớp cho một FVG cụ thể (theo §6 của brief)

| Lớp | Nội dung với một bullish FVG M15 trên EURUSD |
|---|---|
| **Observable** | Giá đi từ 1.08412 lên 1.08455 trong 15 phút của nến 2; nến 1 và nến 3 không chạm đoạn này; size 0.54 ATR; London session; không có tin |
| **Cơ chế có thể** | Dòng lệnh mua chủ động vượt thanh khoản bán ở các mức đó; có thể do thông tin, nhu cầu thanh khoản, metaorder, stop phía trên mức trước… |
| **Diễn giải ICT** | Displacement → BISI; buyside delivery; vùng có thể được rebalance khi giá retrace; CE là mức tham chiếu |
| **Giả thuyết** | Vùng này có xác suất phản ứng (bật ≥ k·ATR) cao hơn vùng đối chứng cùng khoảng cách (HYP-FVG-002); CE có giá trị hơn mức ngẫu nhiên trong vùng (HYP-FVG-006) |
| **Không biết được từ OHLC** | Danh tính và ý định người tham gia; có tổ chức tham gia không; ai đó có "cố ý để lại" vùng này không; còn lệnh chờ trong vùng không; cú đẩy là loại nào |

### 9.5 Diễn giải của ICT **[ICT FRAMEWORK]**

Trong ngôn ngữ ICT: thuật toán giao giá (IPDA) di chuyển từ liquidity tới liquidity; khi giao giá một chiều nhanh, nó để lại "inefficiency"; về sau, giá thường quay lại "rebalance" vùng này (đóng vai PD array) trước khi tiếp tục tới draw on liquidity. Cách diễn đạt này **nhất quán** với hai cơ chế ở §9.3 (transient impact, liquidity provision) — nhưng nó *gắn chủ thể* ("thuật toán", "smart money") và *ý định* ("để lại", "quay lại") cho những thứ chart chỉ cho thấy là *hình dạng*. Note giữ ngôn ngữ ICT khi mô tả cách ICT dùng FVG, và dùng ngôn ngữ cơ chế khi nói về nguyên nhân.

### 9.6 Rà soát tầng WHY của v1 — W0 *(v1, nguyên văn — có rà soát v2)*

"Thị trường quay lại lấp imbalance" nghe như tín điều. Ba cơ chế biến nó thành logic — và phân xử luôn gap nào lấp, gap nào không:

1. **Gap = quãng giá KHÔNG AI KỊP GIAO DỊCH — và các lệnh bị bỏ lại vẫn còn sống.** Khi displacement kéo giá qua một vùng quá nhanh, các lệnh limit mua/bán đặt sẵn trong vùng đó **không được khớp** (giá nhảy qua). Các tổ chức đặt lệnh đó không hủy kế hoạch — lệnh của họ vẫn nằm trong sổ, tại đúng các mức giá bên trong gap. Giá quay lại FVG không phải vì "thị trường công bằng", mà vì **về đó còn thanh khoản chờ sẵn để khớp nốt phần việc dang dở** — với bên đã đẩy giá, đó là nơi rẻ nhất để mua thêm/xả bớt tồn kho. FVG là POI vì nó là *kho lệnh chưa dùng*.
2. **Vì sao CE (50%) hoạt động? Vì nó là điểm cân bằng chi phí của chính bên tạo gap.** Bên khởi xướng displacement có giá vốn trung bình quanh nửa dưới của leg. Cho phép giá retrace *qua* CE của gap do chính mình tạo nghĩa là để vị thế chìm về vùng vốn — mất lợi thế đã trả tiền mua. Vì vậy lớp phòng thủ tự nhiên (mua thêm để chặn) tập trung từ CE trở xuống proximal. CE bị đóng thân xuyên qua đồng nghĩa **bên tạo gap đã bỏ vị thế hoặc bị nuốt** — đó là lý do inversion (IFVG) là bằng chứng đổi delivery chứ không phải pattern trang trí.
3. **Vì sao có gap KHÔNG lấp (breakaway)? Vì không còn tồn kho nào cần cân.** Nếu displacement khởi phát từ một accumulation đã hoàn tất (mọi lệnh đã gom đủ trước đó), bên khởi xướng **không cần quay lại mua thêm** — không có lệnh dang dở trong gap, không có lý do kinh tế nào để redeliver. Câu hỏi "gap này có lấp không?" vì thế quy về: **"bên tạo gap còn việc chưa xong ở đó không?"** — trả lời bằng bối cảnh (gap thoát khỏi POI sau sweep = breakaway; gap giữa leg đang chạy = kho lệnh còn dùng).

Ba cơ chế này chạy xuyên các W bên dưới: news gap không có kho lệnh nào bên trong (W1); grind vào gap = kho lệnh bị rút dần trước khi giá tới (W2); cú chạm ngoài phiên đã tiêu một phần kho (W3).

> [!warning] Rà soát v2 cho W0
> | Luận điểm v1 | Đánh giá v2 | Nhãn |
> |---|---|---|
> | (1) "Gap = quãng giá không ai kịp giao dịch — lệnh bị bỏ lại vẫn còn sống… lệnh limit trong vùng không được khớp (giá nhảy qua)" | **Sai như một cơ chế mặc định.** Trong thị trường liên tục, nến 2 đi qua toàn vùng (§2.2): lệnh limit nằm sẵn ở các mức trong vùng sẽ *bị khớp* khi giá đi qua, không bị "nhảy qua". Chỉ trong news spike/halt/session gap mới có mức bị bỏ qua thật. Lệnh có thể xuất hiện trong vùng *sau đó* (người mới đặt lệnh, thuật toán tái báo giá) — nhưng đó là lệnh mới, không phải "kho lệnh dang dở". | **[INTERPRETATION] — yếu**; phần "lệnh bị nhảy qua" sai trong điều kiện bình thường |
> | (2) "CE hoạt động vì là điểm cân bằng chi phí của bên tạo gap" | Lập luận kinh tế hợp lý về *một* người tham gia giả định, nhưng: không biết ai tạo gap, giá vốn của họ ở đâu, họ có phòng thủ không. Lý thuyết impact (Farmer et al. 2013) gợi ý mức hồi ≈ ⅓ cú đẩy, không trùng CE của gap. Hình học cho CE "giữ" 31% số lần chạm (§16). | **[INTERPRETATION]** — chưa kiểm chứng; không suy ra được từ OHLC |
> | (3) "Gap không lấp (breakaway) vì không còn tồn kho cần cân" | Phù hợp với cơ chế metaorder/information ở §9.3 — nhưng giải thích đơn giản hơn và kiểm chứng được là **drift**: trend 0.2 ATR/nến → 39% FVG cùng chiều không bao giờ bị chạm trong 500 nến (FVG-Sim-02C). | **[INTERPRETATION]**; drift là **[SIMULATION]** |
> | "Câu hỏi đúng: bên tạo gap còn việc chưa xong ở đó không?" | **Đây là trực giác đúng hướng** — nó tương ứng với câu hỏi "cú đẩy là loại liquidity / information / metaorder?" ở §30. Vấn đề là không trả lời được từ OHLC; cần proxy đo được trước. | Giữ như **câu hỏi nghiên cứu** |

### 9.7 Cơ chế theo v1 §14.2–14.3 *(v1, nguyên văn — có chú thích v2)*

#### Liquidity vacuum: vì sao giá "muốn" quay lại *(v1 §14.2)*

Thuật ngữ ICT gọi đây là "rebalance imbalance" — nhưng cơ chế orderflow thật đứng sau là **liquidity vacuum** (chân không thanh khoản):

1. **Stop cluster & limit chưa khớp còn treo lại phía sau giá.** Khi giá bứt nhanh qua một vùng, không phải mọi limit order định hướng ngược lại vùng đó đều bị hủy — nhiều tổ chức dùng thuật toán "resting order" (ví dụ iceberg limit của market maker cung cấp thanh khoản hai chiều) vẫn còn treo tại các mức giá bên trong gap, đơn giản vì thuật toán đó chưa kịp cập nhật lại theo giá mới. Khi giá quay lại, các lệnh này khớp — đó là lý do vùng gap phản ứng.
2. **Chân không thực sự nằm ở phía maker, không phải phía taker.** Aggressor (bên tạo displacement) đã hoàn thành việc — họ không cần quay lại. Nhưng đối trọng của họ (market maker cung cấp hai chiều) cần thời gian để "dựng lại" độ dày sổ lệnh (rebuild depth) sau cú sweep. Trong khoảng thời gian dựng lại này, sổ lệnh tại vùng gap **mỏng hơn bình thường** — bất kỳ dòng lệnh nào quay lại vùng đó sẽ di chuyển giá dễ dàng hơn (ít slippage cản trở) theo cả hai hướng, khiến vùng này trở thành nơi giá "trôi nhanh" khi ghé qua, dù không nhất thiết đảo chiều.
3. **Market maker inventory.** Sau một cú displacement mạnh (ví dụ bên mua áp đảo), dealer/market maker thường kết thúc với inventory lệch (short quá mức nếu họ bán ra để cung thanh khoản cho bên mua). Để cân bằng lại sổ (delta-neutral), họ có động lực đẩy giá hoặc chờ giá **quay lại vùng trung bình vị thế của chính họ** để mua lại phần đã bán — vùng này thường trùng với nửa dưới của displacement leg, gần đúng vị trí CE của FVG. Đây là lời giải thích orderflow cho lý do CE (50%) hoạt động tốt hơn so với mép gap: **CE gần với vùng giá trung bình của dealer hơn là các mép cực trị.**

> [!note] Chú thích v2 cho v1 §14.2
> - Điểm (1) "limit chưa khớp còn treo lại phía sau giá… bên trong gap" — mâu thuẫn với §2.2 trong điều kiện bình thường (xem rà soát W0). Phiên bản đúng hơn: *thanh khoản bị tiêu thụ trong cú đẩy được bổ sung dần sau đó* (resiliency) — lệnh mới đặt vào các mức đó, không phải lệnh cũ còn sót. **[MARKET MECHANICS]** cho resiliency; **[HYPOTHESIS]** cho việc nó tạo phản ứng tại FVG.
> - Điểm (2) "sổ lệnh tại vùng gap mỏng hơn bình thường → giá trôi nhanh khi ghé qua, theo cả hai hướng" — **hợp lý và quan trọng**: nó dự báo vùng FVG là nơi giá *đi nhanh qua* chứ không nhất thiết *phản ứng*. Đây là một giả thuyết đối nghịch với "FVG là hỗ trợ" và cần được test cùng lúc (HYP-FVG-011).
> - Điểm (3) "market maker inventory → vùng giá vốn ≈ CE" — **[INTERPRETATION]**. Cơ chế inventory là có thật trong lý thuyết market making, nhưng vị trí "giá vốn ≈ CE" là suy đoán.

#### Đối chiếu với AMT, Wyckoff, orderflow *(v1 §14.3)*

| Khung lý thuyết | Khái niệm tương đương | Trùng ở đâu | Khác ở đâu |
|---|---|---|---|
| **Auction Market Theory (Market Profile)** | "Single print" / "poor high-low" trong TPO profile | Cả hai đều mô tả vùng giá có **ít thời gian giao dịch** (low time-at-price) do di chuyển nhanh một chiều | AMT đo bằng **thời gian** dừng lại tại mỗi mức giá (TPO count); FVG đo bằng **biên OHLC của 3 nến**. Một "single print" trên Market Profile hôm đó gần như luôn trùng vị trí với một FVG trên chart nến — cùng hiện tượng, khác công cụ đo |
| **Wyckoff** | "No Supply / No Demand" bar, hay giai đoạn Markup/Markdown với "Sign of Strength" | Cả hai đều xem một cây nến/thanh giá biên độ lớn, volume cao, đóng cửa quyết đoán là bằng chứng của **intent tổ chức** | Wyckoff gắn nó với chu kỳ Accumulation → Markup → Distribution → Markdown và volume phân tích rộng hơn; FVG chỉ nhìn 3 nến cục bộ, không bắt buộc gắn với giai đoạn nào của chu kỳ |
| **Orderflow / Footprint (volume tại mỗi mức giá)** | "Volume gap" / "unfinished business" trên footprint chart, "stacked imbalance" | Đây là khung **gần nhất** với FVG — một FVG trên nến thường trùng với vùng có ít giao dịch (volume thấp) trên footprint tại các mức giá tương ứng | Footprint cho biết **chính xác** volume tại từng tick, còn FVG suy luận gián tiếp từ OHLC — footprint là công cụ verify tốt nhất cho một FVG có thật hay chỉ là ảo ảnh của khung thời gian |

> [!tip] Ứng dụng thực chiến của việc đối chiếu này
> Nếu có footprint/volume profile, hãy dùng nó để **lọc FVG giả**: một FVG có volume node rất mỏng bên trong (thật sự ít giao dịch) đáng tin hơn nhiều so với FVG chỉ là ảo ảnh do gộp nến (aggregation artifact) — trường hợp volume bên trong gap thực ra không hề thấp so với xung quanh.

> [!note] Chú thích v2 cho v1 §14.3
> Bảng đối chiếu là phần giá trị nhất của v1 §14. Một hiệu chỉnh: câu "single print… gần như luôn trùng vị trí với một FVG" là **quá mạnh** — single print phụ thuộc độ dài period TPO (thường 30 phút) và vị trí trong phiên; FVG phụ thuộc khung nến và mốc đóng nến. Hai thứ *thường* trùng khi cú đẩy kéo dài cỡ một period; không "gần như luôn". Footprint là công cụ kiểm chứng tốt nhất — đồng ý.

---

## 10. FVG vs Displacement

![[FVG-Deep-04-FVG-vs-Displacement.svg|720]]
*FVG-Deep-04: Bốn ô — displacement có FVG, displacement không FVG, FVG không displacement, không cả hai.*

### 10.1 Hai định nghĩa
- **Displacement** **[ICT FRAMEWORK]**: chuyển động giá mạnh, nhanh, một chiều, thể hiện bằng một hoặc vài nến thân lớn so với biến động gần đây; ICT coi đó là dấu hiệu "có chủ đích". Định nghĩa định lượng và các biến đo đã có ở [[50-Displacement-In-Depth]] (range/ATR, body%, số nến liên tiếp, tốc độ, hậu quả cấu trúc).
- **FVG**: hình học 3 nến (DEF-FVG-01).

### 10.2 Quan hệ
```text
Dòng lệnh mạnh một chiều
        ↓
Displacement (nến 2 lớn so với ATR)
        ↓  thường — nếu nến 1 và nến 3 không chạm lại
FVG
```

| Câu hỏi | Trả lời | Bằng chứng |
|---|---|---|
| Mọi displacement đều tạo FVG? | **Không.** Nến 3 hồi sâu hoặc nến 1 có bóng dài → không FVG | P(FVG \| nến 2 ≥ 2 ATR) ≈ 88% (Gaussian), 72% (GARCH) — FVG-Sim-01B |
| Mọi FVG đều từ displacement? | **Không.** 78% FVG có nến 2 < 1.5 ATR | FVG-Sim-01 |
| FVG nhỏ trong thị trường bình thường có cùng ý nghĩa với FVG từ displacement cực mạnh? | **Không biết** | **[BACKTEST REQUIRED]** — HYP-FVG-001 |
| Displacement nhiều nến? | Leg 2–4 nến lớn liên tiếp tạo *chuỗi* FVG (stacked) hoặc một liquidity void | §11, §27.4 |

### 10.3 Vì sao ICT gắn FVG với displacement — và vì sao điều đó hợp lý
FVG là cách **rẻ nhất để đánh dấu một displacement trên chart** mà không cần ngưỡng: nếu leg có để lại FVG, nó đã đi đủ nhanh so với hai bên. Dùng FVG như *bằng chứng* displacement là hợp lý; dùng FVG như *bằng chứng ý định* thì không (nhiễu cũng tạo FVG).

> [!important] Quy tắc tách biến (v0.1)
> Trong journal và backtest, **không** gộp "FVG hợp lệ" với "displacement hợp lệ". Ghi riêng: `fvg_size_atr`, `c2_range_atr`, `c2_body_pct`, `leg_bars`, `broke_swing_level`. Có tách mới trả lời được câu hỏi brief §12: *FVG từ displacement mạnh có khác FVG thường không?* (HYP-FVG-001). Trường `fvg_valid` trong template backtest hiện tại nên được định nghĩa rõ là "thỏa DEF-FVG-01 + min_size" — không kèm điều kiện context.

---

# PART IV — THUẬT NGỮ

## 11. Gia đình thuật ngữ quanh FVG

### 11.1 Bảng thuật ngữ v2 — định nghĩa theo OHLC, quan hệ với FVG

| Thuật ngữ | Định nghĩa vận hành (khi có thể) | Quan hệ với FVG | Quan sát được từ OHLC? | Note |
|---|---|---|---|---|
| **FVG / BISI / SIBI** | DEF-FVG-01 (§5.7) | — | Có | note này |
| **Imbalance** (ICT) | Gần như đồng nghĩa FVG trong cộng đồng ICT | ≈ FVG | Có (nếu = FVG) | — |
| **Inefficiency** (ICT) | Đoạn giá chỉ được giao một chiều | FVG là một loại | Có | §4 |
| **Liquidity void** | Leg nhiều nến một chiều, ít chồng lấp; ≈ hợp của các FVG liên tiếp | Chứa FVG | Có | [[21-Liquidity-Void]] |
| **Vacuum / Vacuum block** | Vùng giá bị bỏ qua do gap/tin; dùng không nhất quán | Giao với opening gap | Một phần | [[34-Vacuum-Block]] |
| **Volume imbalance** (ICT) | Thân 2 nến kề không chạm, bóng chạm | Mốc nhỏ, hay dính liền FVG | Có | §11.3 |
| **Opening gap / NDOG / NWOG** | Open phiên ≠ close phiên trước | Literal gap; khác FVG | Có | [[23-New-Day-Opening-Gap]] · [[24-New-Week-Opening-Gap]] |
| **Breakaway gap** | Gap/FVG không bị lấp trong leg hiện tại | Một *kết quả* của FVG (không lấp) — chỉ biết ex-post | Ex-post | [[06-Breakaway-Gap]] |
| **BPR** | Vùng chồng lấp của một bullish và một bearish FVG | Tổ hợp 2 FVG | Có | [[03-Balanced-Price-Range]] |
| **Implied FVG** | Không có gap thật; vùng giữa trung điểm bóng nến 1 và nến 3 quanh nến 2 lớn | "FVG ngầm" | Có | [[14-Implied-Fair-Value-Gap]] |
| **IFVG (Inversion)** | FVG bị close xuyên distal rồi được retest từ phía bên kia | Trạng thái sau invalidation | Có | [[17-Inverse-Fair-Value-Gap-iFVG]] · [[46-Reaper-Inversion-Fair-Value-Gap]] |
| **First Presented FVG** | FVG đầu tiên hình thành sau một mốc thời gian (vd 9:30 NY) | Quy tắc *chọn* FVG | Có | [[48-1st-Presented-Fair-Value-Gap]] |
| **Redelivered Rebalanced PR** | Vùng đã được giao hai chiều | Liên quan BPR | Có | [[47-Redelivered-Rebalanced-Price-Range]] |
| **CE / Mean threshold** | Trung điểm của một vùng (FVG, OB, wick) | Mức tham chiếu trong FVG | Có | §16 · [[10-Consequent-Encroachment-Mean-Threshold]] |
| **Proximal / Distal** | Mép chạm trước / mép xa | Mép FVG | Có | §5 |
| **Quadrants** | 25 / 50 / 75% của vùng | Mức trong FVG | Có | §16 |
| **Mitigation** | Dùng lỏng: "giá quay lại vùng" | Xem §17 | Tùy định nghĩa | §17 |
| **Rebalance** | Nhãn ICT cho việc giá quay lại đoạn một chiều | Diễn giải của fill | Không (là nhãn) | §13 |
| **Delivery state** | Buyside / sellside delivery | Diễn giải ICT về chế độ | Không (là nhãn) | §27.3 |

### 11.2 "Gia đình gap" theo v1 *(v1 §7.1, nguyên văn — có chú thích v2)*

Nhiều trader gọi mọi khoảng trống là "FVG" và trade chúng như nhau — đây là sai lầm phân loại. ICT có cả một **taxonomy của inefficiency**, mỗi loại có cấu trúc và cách dùng khác nhau:

![[FVG-Advanced-Gap-Taxonomy.svg|690]]

| Loại | Cấu trúc | Bản chất | Cách dùng thực chiến |
|---|---|---|---|
| **FVG (BISI/SIBI)** | Gap 3 nến: wick nến 1 và nến 3 không chạm nhau | Single-sided delivery do displacement | POI entry / draw; CE là mức chính |
| **Volume Imbalance** | Gap giữa **body** hai nến liên tiếp, nhưng wick chồng lấp | Inefficiency nhỏ giữa close/open | Mốc precision cho entry/target LTF; thường được rebalance nhanh — KHÔNG phải POI chính |
| **[[21-Liquidity-Void]]** | Cả một đoạn nhiều nến one-sided | Vùng thiếu giao dịch quy mô lớn, chứa nhiều FVG con | Draw mạnh; giá thường rebalance phần lớn void; bên trong void chọn FVG con làm mức |
| **[[03-Balanced-Price-Range]] (BPR)** | Bullish FVG chồng lấp Bearish FVG | Vùng đã được giao dịch đủ **hai chiều** | S/R rất "cứng"; CE của BPR là mức phòng thủ; entry chất lượng cao khi retest |
| **[[14-Implied-Fair-Value-Gap]]** | Không có gap thật; đo bằng trung điểm wick nến 1 và nến 3 | "Gap ngầm" trong nến có wick dài | Dùng khi displacement không để lại gap thật; yếu hơn FVG thật |
| **[[06-Breakaway-Gap]]** | Gap sinh ra khi giá thoát khỏi accumulation/POI với intent cực mạnh | Gap KHÔNG có nhu cầu được lấp trong leg hiện tại | Không chờ lấp để entry — dấu hiệu trend rất mạnh; dùng làm bằng chứng bias |
| **[[23-New-Day-Opening-Gap]] / [[24-New-Week-Opening-Gap]]** | Gap giữa close phiên trước và open phiên sau | Reference gap của thuật toán theo thời gian | Mức tham chiếu draw/support-resistance trong ngày/tuần |

> [!important] Hệ quả quan trọng nhất của taxonomy
> **Không phải mọi gap đều "phải" được lấp.** Breakaway gap trong displacement thoát khỏi accumulation thường không được lấp trong cùng một leg. Kỳ vọng "gap nào cũng lấp" là lý do trader counter-trend bị nghiền trong trend mạnh. Câu hỏi đúng không phải "gap này có lấp không?" mà là "**gap này thuộc loại nào, và narrative có cần nó được lấp không?**"

> [!note] Chú thích v2 cho v1 §7.1
> - Bảng taxonomy của v1 là đúng và hữu ích; giữ nguyên.
> - "Breakaway gap… KHÔNG có nhu cầu được lấp trong leg hiện tại" → đúng như *mô tả ex-post*; nhưng chỉ biết một gap là breakaway **sau khi** nó không bị lấp. Ex-ante, giải thích kiểm chứng được là drift (FVG-Sim-02C). Dùng nó như *bằng chứng bias* là đúng hướng: nhiều FVG cùng chiều không bị lấp = drift mạnh.
> - "NDOG/NWOG… reference gap của thuật toán theo thời gian" → **[ICT FRAMEWORK]**; phần "của thuật toán" là **[INTERPRETATION]**.
> - Callout "Không phải mọi gap đều phải được lấp" — **đồng ý**, và §15 cho thấy câu ngược lại ("mọi gap rồi cũng được lấp") đúng với random walk không drift — nghĩa là nó không mang thông tin.

### 11.3 FVG dính liền Volume Imbalance — đo mép nào? *(hình v1, chưa được nhúng ở v1)*

![[FVG-EdgeB-VolumeImbalanceMerge.svg|720]]
*Hình v1 (EdgeB): FVG thật (nến 1–3) dính liền volume imbalance (nến 3–4) — quy tắc gộp thành một vùng.*

> [!note] Nhãn v2
> Quy tắc trong hình (gộp nếu VI ≥ 25% chiều cao FVG, đo CE trên toàn khối) là **[HEURISTIC]** không có nguồn kiểm chứng. Giá trị của nó là *nhất quán*: chọn một quy tắc, ghi `merged_vi = true/false`, và giữ nguyên. Khi backtest, so sánh CE của FVG gốc với CE của khối gộp như hai biến thể (HYP-FVG-006b).

### 11.4 Các từ chỉ hành vi sau khi FVG hình thành
Touch, partial fill, CE reached, full fill, close beyond, inversion, mitigation, rebalance, respect — mỗi từ là một sự kiện khác nhau với xác suất nền khác nhau. Định nghĩa và số liệu ở §14 và §17.

---

## 12. FVG vs các khái niệm hay bị nhầm

![[FVG-Deep-23-FVG-Khong-Phai-La.svg|720]]
*FVG-Deep-23: Tám khái niệm trả lời tám câu hỏi khác nhau. Một FVG có thể đóng vai location bên trong một POI — nhưng không là POI, không là entry, không là liquidity.*

### 12.1 FVG vs Liquidity (brief §18)

| | Liquidity | FVG |
|---|---|---|
| Nói về | Nơi **có thể** có cụm lệnh (stop, limit, breakout) | Đoạn giá **đã** được đi qua nhanh, một chiều |
| Câu hỏi | "Giá có thể tìm đối ứng ở đâu?" | "Cú di chuyển vừa rồi để lại cấu trúc gì?" |
| Thời điểm | Trước sự kiện (mức ex-ante) | Sau sự kiện (known_at = close nến 3) |
| Quan sát | Gián tiếp — suy ra từ mức nổi bật | Trực tiếp từ OHLC |
| Vai trò trong 2022 Model | Mục tiêu (DOL) và sự kiện (sweep) | Location để vào lệnh sau sự kiện |

**Vì sao ICT ghép Liquidity → Displacement → FVG?**
1. *Liquidity event là một nguyên nhân khả dĩ của nến 2*: chạm cụm stop → lệnh market dây chuyền → nến lớn (Osler 2005). Nếu sau đó dòng lệnh đảo chiều mạnh, nến displacement ngược chiều để lại FVG.
2. *Liquidity event là bối cảnh*: FVG ngay sau một sweep có "câu chuyện" (stop đã được dùng làm đối ứng). Câu chuyện này có giá trị dự báo hay không là **[HYPOTHESIS]** (HYP-FVG-008; xem [[20-Liquidity-Sweep]] §15).
3. *FVG là nơi vào lệnh có stop ngắn* sau khi sự kiện đã xảy ra.

**Một nhầm lẫn cần tránh:** "FVG là nơi liquidity nằm" — không có cơ sở (lệnh trong vùng đã bị nến 2 khớp, §2.2). "FVG là một draw on liquidity" — trong ICT, *PD array* (gồm FVG) có thể được coi là draw; với note này đó là **[HYPOTHESIS]** cần so với mức ngẫu nhiên cùng khoảng cách (HYP-FVG-010).

### 12.2 FVG vs Order Block (brief §19)

| Khái niệm | Mô tả | Hình thành | Chức năng trong ICT | Bằng chứng quan sát |
|---|---|---|---|---|
| **FVG** | Đoạn chỉ nến 2 đi qua | Giữa cú đẩy | Location vào lệnh khi retrace; draw | H₁ < L₃ |
| **Order Block** | Nến ngược màu cuối cùng trước cú đẩy | Gốc của cú đẩy | POI; nơi "lệnh tổ chức" được cho là nằm | Nến bearish cuối trước displacement tăng (bullish OB) |

**Quan hệ hình học (một điểm ít được nói):** trong mẫu kinh điển, nến 1 của FVG *chính là* order block (nến bearish cuối trước displacement). Khi đó **distal của bullish FVG = High của OB**: OB [L₁, H₁] nằm *ngay dưới* FVG [H₁, L₃]. Vì vậy "FVG trùng/kề OB" là **trùng hợp theo cấu tạo** trong mẫu này, không phải hai bằng chứng độc lập. Khi đếm "confluence", không đếm hai lần cùng một sự kiện.

```text
Mẫu kinh điển (bullish):
L₃ ──────────── proximal FVG
   ░░ FVG ░░
H₁ ──────────── distal FVG = High của OB
   ▓▓ OB  ▓▓    (nến 1 = nến bearish cuối trước displacement)
L₁ ────────────
```

### 12.3 FVG vs Liquidity Void (brief §20)
- **Liquidity void** **[ICT FRAMEWORK]**: cả một đoạn nhiều nến một chiều, ít chồng lấp — trên khung đang xét thường là chuỗi FVG liên tiếp; ICT mô tả FVG là "typically confirmed with a liquidity void on the lower time frame charts".
- *Mọi liquidity void đều chứa FVG?* Trên khung của nó: gần như (theo định nghĩa leg một chiều). *Mọi FVG đều là liquidity void trên LTF?* Trên random walk, **98%** H1 FVG chứa M5 FVG cùng chiều — và **99.9%** nến H1 lớn *không* tạo FVG cũng chứa M5 FVG (FVG-Sim-06A). "Xác nhận bằng LTF void" vì thế gần như tự động.
- **Thuật ngữ trong cộng đồng không nhất quán**: "liquidity void", "vacuum", "imbalance", "inefficiency" được dùng chồng lên nhau. Note này dùng: FVG = 3 nến (DEF-FVG-01); liquidity void = leg ≥ 2 nến một chiều có ≥ 2 FVG liên tiếp cùng chiều (DEF-FVG-05, v0.1).

![[LiquidityVoid-Advanced-vs-FVG-vs-BPR.svg|720]]
*Hình từ note Liquidity Void: phân biệt Liquidity Void, FVG và BPR.*

### 12.4 FVG vs Gap truyền thống (brief §17)

| Dimension | Conventional gap | FVG |
|---|---|---|
| Hình thành | Open phiên mới ≠ close phiên trước (thị trường đóng) | Cú đẩy trong một nến khiến nến 1 và nến 3 không chạm nhau |
| Cấu trúc nến | 2 nến | 3 nến |
| Phụ thuộc phiên | Có | Không |
| Có giao dịch trong vùng | Không (trên venue đó) | Có — chỉ trong nến 2 |
| Bối cảnh điển hình | Tin qua đêm/cuối tuần, mở phiên | Tin trong phiên, killzone, displacement, nhiễu |
| Diễn giải ICT | NDOG / NWOG / opening gap — mức tham chiếu thời gian | BISI / SIBI — PD array |
| Quan sát từ OHLC | Có | Có |

### 12.5 FVG vs Rejection candle
Rejection candle / rejection block ([[28-Rejection-Block]]) là chuyện của **một nến có bóng dài** — giá đã đi vào một vùng rồi bị đẩy ra *trong cùng nến*. FVG là chuyện của **ba nến không chồng lấp**. Hai khái niệm thường gặp nhau theo hai cách: (1) nến retrace *vào* FVG thường để lại bóng dài (rejection) nếu FVG "giữ"; (2) Implied FVG được đo bằng trung điểm bóng nến khi không có gap thật.

---

# PART V — HÀNH VI SAU KHI FVG HÌNH THÀNH

## 13. Vì sao giá (thường) quay lại FVG? (brief §21)

### 13.1 Câu trả lời KHÔNG được dùng
> "Price always comes back to fill the imbalance."

Ba vấn đề: (1) "always" sai — FVG cùng chiều trend thường không bị chạm (§15); (2) phần đúng của câu ("thường quay lại") cũng đúng với **mọi** vùng giá nằm ngay sau lưng giá (§13.3); (3) "imbalance" là nhãn, không phải cơ chế (§4).

### 13.2 Bảy giả thuyết — tách bạch, có dự báo kiểm chứng được

![[FVG-Deep-06-Vi-Sao-Gia-Quay-Lai.svg|720]]
*FVG-Deep-06: Bảy lời giải thích cho "giá quay lại FVG", xếp theo mức bằng chứng. Chúng không loại trừ nhau.*

| # | Giả thuyết (brief) | Cơ chế | Dự báo phân biệt được | Bằng chứng hiện có | Nhãn |
|---|---|---|---|---|---|
| **F** | Random / conditional price movement | Hình học: vùng nằm sát sau lưng giá; random walk hồi quy | P(chạm) chỉ phụ thuộc khoảng cách & volatility; FVG = vùng đối chứng | Mô phỏng: khớp công thức Brown (FVG-Sim-02B) | **[MATHEMATICAL]** — baseline bắt buộc |
| **D** | Liquidity / order replenishment | Tác động giá của dòng lệnh chủ động có phần tạm thời; sổ lệnh phục hồi | Mức hồi sau cú đẩy ≈ ⅓ đỉnh tác động khi dòng lệnh kết thúc; phụ thuộc metaorder đã xong chưa | Metaorder: impact vĩnh viễn/đỉnh ≈ 0.51 (Tây Ban Nha), 0.69 (London) (Moro et al. 2009); ≈ 2/3 (Bershova & Rakhlin 2013); lý thuyết 2/3 (Farmer et al. 2013) | **[MARKET MECHANICS]** cho cơ chế; **[HYPOTHESIS]** cho FVG |
| **C** | Auction rebalancing | Giá rời value nhanh; thị trường "thử" xem mức mới có được chấp nhận | Sau one-timeframing, retrace vào vùng single print xảy ra *thường xuyên hơn* vùng có nhiều thời gian | AMT là khung mô tả; bằng chứng định lượng công khai hạn chế | **[INTERPRETATION]** |
| **E** | Profit-taking / position adjustment | Người vừa mua trong cú đẩy chốt lời; dealer cân lại inventory | Retrace mạnh hơn khi cú đẩy dài, khi gần mốc thời gian (cuối phiên) | Hợp lý; khó tách khỏi D | **[INTERPRETATION]** |
| **B** | Mean reversion | Lợi suất ngắn hạn tự tương quan âm | Hiệu ứng mạnh hơn khi thanh khoản kém, VIX cao | Short-term reversal (Lehmann 1990; Jegadeesh 1990); lợi nhuận reversal = phần thưởng cung cấp thanh khoản, tăng khi thanh khoản khan hiếm (Nagel 2012) — chủ yếu cổ phiếu, khung ngày/tuần | **[MARKET MECHANICS]** (khung khác) |
| **A** | Retracement after displacement | Tổng hợp của D + E + B quan sát ở cấp nến | Chiều sâu hồi phụ thuộc loại displacement | Toy model: liquidity-type bị xuyên 77%, metaorder 13% (FVG-Sim-03) | **[TOY MODEL]** |
| **G** | Tự hiện thực hóa | Nhiều trader đặt lệnh tại FVG/CE | Hiệu ứng tăng theo mức phổ biến của ICT; tập trung đúng ở mức "nổi" (CE, mép) | "Memory effect" tại mức S/R (Garzarelli et al. 2014) — chưa có bằng chứng riêng cho FVG | **[HYPOTHESIS]** |
| ICT | "Rebalance / mitigate the imbalance" | Nhãn cho hiện tượng | Không đưa ra dự báo định lượng riêng | — | **[ICT FRAMEWORK]** |

> [!important] Câu hỏi then chốt (brief §21): "Có evidence nào chứng minh FVG tự nó *attracts* price?"
> **Hiện chưa có bằng chứng công khai đạt chuẩn** (mẫu lớn, ngoài mẫu, so với đối chứng). Để chứng minh "hút giá", phải cho thấy **P(chạm | FVG ở khoảng cách d) > P(chạm | vùng không-FVG ở cùng khoảng cách d, cùng volatility, cùng trend)**. Mọi so sánh không có vùng đối chứng chỉ đo hình học. Một preprint SSRN (Kondapally, *"Quantifying Fair Value Gaps: A Novel Metric for Price Reaction Prediction"*) có tồn tại nhưng chưa bình duyệt và không truy cập được nội dung trong phiên này — **không trích kết quả**.

### 13.3 Hình học trước tiên **[SIMULATION + MATHEMATICAL]**

![[FVG-Sim-02-Fill-Is-Geometry.png|900]]
*FVG-Sim-02: (A) Trên random walk không drift, gần như mọi FVG cuối cùng đều được chạm và lấp; (B) xác suất chạm trong 20 nến theo khoảng cách khớp công thức first-passage của chuyển động Brown; (C) thêm drift: FVG cùng chiều trend nhiều khả năng không bị chạm — FVG ngược trend bị lấp gần như chắc chắn.*

**Panel A — tỷ lệ tích lũy (random walk không drift, FVG ≥ 0.1 ATR, n = 51,902):**

| Sự kiện | 1 nến | 3 nến | 10 nến | 20 nến | 100 nến | 500 nến | 2000 nến |
|---|---:|---:|---:|---:|---:|---:|---:|
| Chạm proximal | 43% | 61% | 77% | 83% | 92% | 97% | 98% |
| Chạm CE | 27% | 48% | 68% | 77% | 89% | 95% | 98% |
| Full fill (chạm distal) | 18% | 38% | 61% | 71% | 87% | 94% | 97% |
| Close xuyên distal | 11% | 28% | 52% | 64% | 83% | 93% | 96% |

**Panel B — khoảng cách là biến dự báo chính.** P(chạm trong 20 nến) giảm từ ~98% (giá đóng cửa ngay tại proximal) xuống ~49% (cách 2.1 ATR); công thức Brown 2·(1 − Φ(d/(σ√T))) — không chứa bất kỳ thông tin "FVG" nào — khớp sát. Sai lệch nhỏ (mô phỏng thấp hơn công thức 2–3 điểm ở khoảng cách ngắn) đến từ việc ATR là trung bình true range, không phải σ.

**Hệ quả thực hành:** khi bạn thấy "giá quay lại FVG" trên chart, câu hỏi đầu tiên là *"nó cách bao xa và trong bao nhiêu nến?"*. Một FVG có proximal cách close nến 3 dưới 0.3 ATR sẽ bị chạm trong 20 nến ~90% số lần *dù không có gì đặc biệt*.

### 13.4 Correlation ≠ causation — cái bẫy của "FVG hút giá"
Ba yếu tố gây nhiễu (confounders) làm FVG *trông như* hút giá:
1. **Vị trí:** FVG luôn nằm ngay sau lưng giá lúc hình thành (khoảng cách nhỏ theo cấu tạo).
2. **Volatility:** FVG hình thành trong cụm biến động cao — nơi giá đi xa theo cả hai hướng.
3. **Chọn mẫu:** trader nhớ FVG được chạm rồi bật; FVG bị xuyên được "giải thích" bằng IFVG hoặc "thiếu confluence".

Thiết kế kiểm chứng đúng: **matched control** — cùng hướng, cùng khoảng cách, cùng size (ATR), cùng thời điểm trong phiên, cùng trend regime (§41.4).

### 13.5 Transient impact — cơ chế "vật lý" nhất, và vì sao nó không tự động trỏ vào CE
Nếu cú đẩy là thực thi của một metaorder: trong lúc thực thi, giá tăng gần như theo căn bậc hai của khối lượng đã thực thi; khi kết thúc, giá hồi lại và ổn định quanh **≈ 2/3 đỉnh tác động** (fair pricing condition, Farmer et al. 2013) → mức hồi ≈ **⅓ biên độ tác động**.

Áp vào FVG: giả sử leg displacement từ 100 lên 106 (6 điểm, đều là tác động của một metaorder). Hồi ⅓ → về ~104. Vùng FVG có thể nằm ở bất kỳ đâu trong leg tùy hình dạng nến 1/nến 3:
- FVG [103.5, 104.5] (ở phần trên leg) → mức hồi 104 ≈ CE của FVG.
- FVG [101, 102] (ở phần dưới leg) → mức hồi 104 **không chạm** FVG.

→ "Chiều sâu retrace vào FVG" phụ thuộc **vị trí FVG trong leg** — một biến đo được trước: `fvg_pos_in_leg = (CE − leg_low)/(leg_high − leg_low)` (bullish). Đề xuất kiểm định: phản ứng có tập trung quanh một *phần trăm của leg* (⅓, ½) hơn là quanh CE của FVG không? (HYP-FVG-006c). Lưu ý: dữ liệu metaorder trong các nghiên cứu trên là cổ phiếu/thực thi tổ chức; việc áp cho FX/futures intraday là **[HYPOTHESIS]**.

---

## 14. Fill — từ vựng chính xác (brief §22)

![[FVG-Deep-07-Tu-Vung-Fill.svg|720]]
*FVG-Deep-07: Sáu sự kiện khác nhau sau khi FVG hình thành — đừng dùng như từ đồng nghĩa.*

### 14.1 Định nghĩa vận hành — DEF-FVG-02 (v0.1)

| Sự kiện | Định nghĩa (bullish; bearish đối xứng) | Biến ghi | Quan sát từ |
|---|---|---|---|
| **Touch** | Một nến (cùng khung) có Low ≤ proximal | `touched`, `bars_to_touch` | Wick |
| **Partial fill** | 0 < depth < 0.5 | `max_depth` | Wick |
| **CE reached** | depth ≥ 0.5 | `bars_to_ce` | Wick |
| **Full fill** | depth ≥ 1 (Low ≤ distal) | `bars_to_full` | Wick |
| **Close beyond (invalidated)** | Một nến cùng khung đóng cửa < distal | `bars_to_invalidation` | Close |
| **Inversion** | Sau invalidation, giá quay lại vùng từ phía dưới và bị từ chối (đóng cửa lại dưới vùng trong m nến) | `inverted`, `bars_to_inversion` | Close |

với depth = (proximal − Low thấp nhất từ khi biết FVG)/size.

### 14.2 Vì sao định nghĩa quyết định con số
Cùng một tập FVG random walk, cùng cửa sổ 20 nến: touch **83%**, CE **77%**, full **71%**, close beyond **64%**. Một bài viết nói "FVG được tôn trọng 70%" có thể đang đo bất kỳ điều gì trong số này — hoặc "giá bật lên sau khi chạm" theo một ngưỡng tùy ý. **Luôn hỏi: định nghĩa nào, khung nào, cửa sổ bao nhiêu nến, đối chứng là gì?**

### 14.3 Ghi chép tối thiểu cho mỗi FVG được theo dõi
`touched (y/n) · bars_to_touch · max_depth · closed_beyond (y/n) · bars_to_invalidation · reaction_atr (MFE sau touch, đơn vị ATR) · adverse_atr (MAE trước reaction)`. Không gộp thành "respected / failed" — gộp làm mất thông tin và mở cửa cho diễn giải sau sự kiện.

---

## 15. FVG có luôn được lấp không? (brief §23)

### 15.1 Trả lời trực tiếp
**Không được giả định.** Nhưng sự thật thú vị hơn: *trên random walk không drift, câu trả lời gần như là "có, cuối cùng"* — và chính vì vậy câu đó vô nghĩa như một tín hiệu.

**[MATHEMATICAL]** Random walk một chiều là *hồi quy* (định lý Pólya, 1921): với xác suất 1, nó quay lại mọi mức giá hữu hạn. Chuyển động Brown có drift μ hướng *ra xa* một mức ở khoảng cách d thì chỉ chạm được mức đó với xác suất exp(−2μd/σ²) < 1. Nên:
- **Không drift:** "gap nào rồi cũng lấp" ✔ (FVG-Sim-02A: 97% full fill trong 2000 nến).
- **Có drift cùng chiều FVG:** một phần FVG không bao giờ bị lấp.

### 15.2 Drift giải thích FVG không bị lấp **[SIMULATION]**

| Drift (ATR/nến) | FVG cùng chiều trend: không bao giờ bị chạm (500 nến) | Cùng chiều: full fill | FVG ngược trend: không bị chạm | Ngược trend: full fill |
|---|---:|---:|---:|---:|
| 0 | 3% | 95% | 4% | 93% |
| 0.05 | 12% | 79% | 0.3% | 99% |
| 0.10 | 22% | 65% | 0% | 100% |
| 0.20 | 39% | 41% | 0% | 100% |

Và số lượng FVG tự lệch theo trend: với drift 0.2 ATR/nến, **45,327** FVG cùng chiều vs **13,172** ngược chiều. → **Đếm FVG theo hướng và tỷ lệ FVG cùng chiều bị lấp là một thước đo trend** — nhất quán với ý của v1 §7.4 "leg nào có FVG là leg có chủ đích" nhưng giải thích bằng drift thay vì ý định.

### 15.3 Các kiểu "số phận"

| Kiểu | Mô tả | Tỷ lệ nền (random walk, 20 nến) | Ghi chú |
|---|---|---|---|
| Lấp ngay | Chạm ngay nến 4 | 43% chạm, 18% full fill ở nến 4 | "FVG bị lấp ngay" là chuyện thường, không phải "thất bại" |
| Lấp trễ | Chạm sau nhiều nến | 83% − 43% = 40% chạm trong nến 5–23 | Tuổi FVG khác nhau → giá trị khác nhau? (HYP-FVG-003) |
| Lấp một phần rồi đi | Chạm, depth < 1, rồi rời xa | phần còn lại | §16 |
| Lấp nhiều lần | Chạm, rời, chạm lại | phổ biến trên random walk | v1 7.3: "first touch đáng tin nhất" — HYP-FVG-020 |
| Không bao giờ | Không chạm trong cửa sổ | 17% (20 nến), 2% (2000 nến) — tăng mạnh khi có drift | Breakaway (ex-post) |
| Xuyên trước khi "phản ứng" | Close beyond distal | 64% (20 nến) | Invalidation (§19) |

### 15.4 Điều này có ý nghĩa gì với claim "price always fills imbalance"?
- Nếu "always" nghĩa là *cuối cùng*: đúng với cả nhiễu → không chứa thông tin.
- Nếu nghĩa là *trong cửa sổ có ý nghĩa giao dịch* (vd 20 nến): ~71% full fill trên nhiễu → claim chỉ có giá trị nếu dữ liệu thật **khác** con số này *theo chiều có lợi cho chiến lược*.
- FVG không được lấp phần lớn nói về **drift / dòng lệnh tiếp diễn** — không phải về "chất lượng" của FVG.
- **Bằng chứng học thuật gần nhất (về opening gap theo ngày, không phải FVG):** Caporale & Plastun (2017) xét gap giữa close hôm trước và open hôm sau trên cổ phiếu, FX và hàng hóa 2000–2015; kết luận phần lớn hành vi "không mâu thuẫn với thị trường hiệu quả", ngoại lệ là FX nơi một chiến lược khai thác gap cho lợi nhuận bất thường trong mẫu của họ. Đây là loại gap khác (§2.1) — nhưng cho thấy câu hỏi "gap có được lấp một cách khai thác được không" là câu hỏi *thực nghiệm theo từng thị trường*, không có câu trả lời chung.

> [!quote] Liên hệ v1
> Callout v1 §7.1 — "Câu hỏi đúng không phải 'gap này có lấp không?' mà là 'gap này thuộc loại nào, và narrative có cần nó được lấp không?'" — đúng tinh thần. v2 bổ sung: "narrative có cần" phải được thay bằng **biến đo được trước** (trend regime, vị trí so với DOL, loại displacement proxy), nếu không nó trở thành giải thích sau sự kiện.

---

## 16. Consequent Encroachment — CE (brief §24)

### 16.1 Định nghĩa
**[MATHEMATICAL]** CE = (proximal + distal)/2 — trung điểm của vùng. ICT dùng CE cho FVG, OB, và bóng nến ("mean threshold"). Xem thêm [[10-Consequent-Encroachment-Mean-Threshold]].

### 16.2 Vì sao 50%?
- **[ICT FRAMEWORK]** Quy ước của ICT: CE là mức tham chiếu chính để đo "FVG có được tôn trọng" và để vào lệnh với R:R tốt hơn mép.
- **Truyền thống phân tích kỹ thuật:** các tỷ lệ ⅓, ½, ⅔ của một nhịp được coi là vùng hồi phổ biến từ thời Dow Theory (Rhea, 1932, về "secondary reactions"); mức 50% gắn với nhiều trường phái (Gann…). Đây là truyền thống, không phải bằng chứng.
- **Lý do thực hành hợp lệ:** 50% là quy ước *đơn giản, nhất quán, không cần tham số* để (a) đo độ sâu, (b) đặt lệnh limit cân bằng giữa khả năng khớp và khoảng stop. Đây là lý do tốt để *dùng* CE — không phải bằng chứng CE *có lực*.

### 16.3 CE trong hình học: không có điểm gãy tại 50% **[SIMULATION + MATHEMATICAL]**

![[FVG-Sim-04-Matched-Control-CE.png|900]]
*FVG-Sim-04: (A) FVG so với vùng đối chứng cùng hình học; (B) "giữ ở CE" là một đường cong hình học trơn 1/(1+q) — không có điểm gãy tại 0.5; (C) toy model: lệnh limit được khớp nhiều nhất ở loại FVG tệ nhất.*

Sau khi giá chạm proximal, gọi q là độ sâu (phần của size). Với chuyển động Brown không drift, xác suất giá đi sâu hơn q·size **trước khi** bật ra 1·size khỏi proximal là:

$$P(\text{depth} > q) = \frac{1}{1+q}$$

(gambler's ruin: hai rào cản ở −q và +1). Mô phỏng (n = 27,162 FVG được chạm): P(vượt 25%) = 81.6% (công thức 80%), P(vượt CE) = **68.6%** (66.7%), P(vượt 75%) = 59.4% (57.1%), P(vượt distal) = 52.1% (50%).

→ **"Giá chạm CE rồi bật" xảy ra ~31% số lần chạm chỉ do hình học** (với định nghĩa "bật" = rời proximal 1·size). Một claim "CE được tôn trọng" phải cho thấy (1) P(giữ tại 0.5) cao hơn 1/3 đáng kể, **và** (2) cao hơn các mức lân cận (0.4, 0.6) — tức là có *điểm gãy* tại CE, chứ không chỉ cả đường cong dịch lên.

### 16.4 CE — mức mô tả hay mức dự báo?
| Vai trò | Hợp lệ? | Ghi chú |
|---|---|---|
| Thước đo độ sâu (`max_depth` so với 0.5) | ✔ **[OBSERVABLE]** | Rất hữu ích để ghi chép nhất quán |
| Điểm vào limit cân bằng | ✔ **[HEURISTIC]** | Đánh đổi khớp lệnh vs stop (§16.5) |
| Mức có "lực" phản ứng đặc biệt | ? **[HYPOTHESIS]** — HYP-FVG-006 | Cần điểm gãy so với mức lân cận |
| "Close xuyên CE = FVG yếu / invalid" | ? **[HEURISTIC]** | Là một định nghĩa invalidation (I3, §19) — chọn trước, test như biến thể |

### 16.5 Vào lệnh ở mép, CE hay sâu hơn? — đánh đổi

![[FVG-Deep-08-Entry-Depth-Trade-off.svg|720]]
*FVG-Deep-08: Càng vào sâu, stop càng ngắn nhưng càng ít lệnh được khớp — và lệnh được khớp càng hay là lệnh giá đang chạy ngược. Số liệu: đường nền random walk.*

Ba lực cùng lúc:
1. **Xác suất khớp** giảm khi vào sâu (random walk, 20 nến: 83% → 77% → 71%).
2. **Khoảng stop** ngắn lại → R:R danh nghĩa tăng.
3. **Adverse selection:** điều kiện "giá đã đi sâu tới mức của tôi" làm tăng tỷ lệ các trường hợp giá đang thực sự đảo chiều (toy model: liquidity-type chiếm 31% FVG lúc hình thành nhưng 49% các lệnh CE được khớp — §30.4).

Trên random walk ba lực triệt tiêu: mọi mức vào lệnh có excess ≈ 0 so với p_null. Trên thị trường thật, mức vào tối ưu (nếu có) **là câu hỏi thực nghiệm theo từng symbol** — đúng như v1 W4 đã nhận ra.

### 16.6 Giải phẫu FVG: proximal/distal, quadrants và độ sâu fill *(v1 §7.2, nguyên văn — có chú thích v2)*

![[FVG-Advanced-Quadrants.svg|646]]

**Proximal vs Distal edge.** Với một bullish FVG bên dưới giá: mép trên (gần giá) là **proximal edge**, mép dưới (xa giá) là **distal edge**. Mọi kế hoạch entry/stop nên gọi tên hai mép này thay vì "trên/dưới" mơ hồ — vì với bearish FVG thì đảo ngược.

**Quadrant theory.** Chia gap thành 4 phần (0–25–50–75–100%). Ứng dụng:
- Trong displacement **rất mạnh** (nhiều FVG xếp chồng, sweep rõ), giá thường chỉ nhúng tới **upper quadrant hoặc CE** của bullish FVG rồi bật — chờ distal sẽ lỡ tàu.
- Giá lấp tới **lower quadrant / distal** rồi mới bật = phản ứng yếu hơn → hạ kỳ vọng, bắt buộc có LTF MSS trước khi vào, hoặc bỏ.
- **Độ sâu fill là thông tin**, không chỉ là chuyện entry: chạm proximal rồi bay = demand/supply cực mạnh; cần lấp toàn bộ mới bật = sponsorship yếu dần.

**Ba cấp độ entry theo độ sâu:**

| Kiểu entry | Vị trí | Điều kiện cho phép | Trade-off |
|---|---|---|---|
| **Aggressive** | Limit tại proximal edge | Sweep rõ + displacement cực mạnh + FVG chồng OB | Win rate thấp hơn, R:R cao nhất, dễ dính chạm giả |
| **Standard** | Limit/market quanh CE | Điều kiện FVG chuẩn (checklist mục 8) | Mặc định — cân bằng nhất |
| **Conservative** | Sau khi giá reject CE + M1/M5 MSS xác nhận | FVG fill sâu, context kém chắc chắn | Win rate cao hơn, R:R giảm, có thể lỡ move |

**Stop loss:** luôn đặt ngoài **distal edge + buffer** (spread/vài tick) hoặc dưới sweep low — không đặt tại distal chính xác vì thuật toán hay quét đúng mép. Nếu stop hợp lệ khiến size quá lớn so với 0.5% risk → **giảm size, không bóp stop**.

> [!note] Chú thích v2 cho v1 §7.2
> - Quy ước proximal/distal: **giữ nguyên** (đã dùng xuyên suốt v2).
> - "Trong displacement rất mạnh… giá thường chỉ nhúng tới upper quadrant hoặc CE" — **nhất quán** với toy model: FVG từ metaorder (dòng lệnh còn tiếp) hiếm khi bị chạm sâu (FVG-Sim-03: 51% không chạm, 25% chạm nhưng giữ trên CE). Nhưng "displacement rất mạnh" *lúc hình thành* không phân biệt được metaorder với liquidity shock (phân bố kích thước chồng nhau) → **[HYPOTHESIS]**.
> - "Độ sâu fill là thông tin… cần lấp toàn bộ mới bật = sponsorship yếu dần" — **[INTERPRETATION]**; phiên bản kiểm chứng được: *P(reaction | max_depth) có giảm theo depth nhanh hơn đường nền 1/(1+q) không?* (HYP-FVG-006d).
> - Bảng ba cấp entry và quy tắc "giảm size, không bóp stop": **[HEURISTIC]** tốt về quản trị rủi ro — giữ nguyên.

### 16.7 Mức thay thế để test cùng lúc (tránh "chỉ test CE")
Nếu muốn biết CE có đặc biệt không, test **đồng thời** các mức: mép proximal, 25%, CE, 75%, distal; **⅓ và ½ của cả leg displacement** (§13.5); OTE 62–79% của leg ([[26-OTE-Optimal-Trade-Entry]]). Vì test nhiều mức, phải hiệu chỉnh đa kiểm định (§43.3).

---

## 17. Mitigation (brief §25)

### 17.1 "Mitigation" nghĩa chính xác là gì?
Trong ICT, "mitigation" gốc gắn với ý *một bên giảm thiểu (mitigate) vị thế lỗ cũ khi giá quay lại mức vào lệnh của họ* (mitigation block — [[22-Mitigation-Block]]). Với FVG, cộng đồng dùng "FVG đã được mitigate" một cách lỏng, có thể là: đã chạm, đã tới CE, đã full fill, hoặc đã phản ứng. Phần "giảm thiểu vị thế" là **[INTERPRETATION]** (không quan sát được).

### 17.2 Tách bạch sáu từ

| Từ | Nghĩa v0.1 | Có phải là "kết quả tốt"? |
|---|---|---|
| Touch | Chạm proximal | Không nói gì |
| Retracement | Giá quay ngược hướng cú đẩy (có thể chưa tới FVG) | Không nói gì |
| Fill (partial / CE / full) | Độ sâu đi vào vùng | Không nói gì |
| Mitigation | **Không dùng như thuật ngữ đo lường trong v2** — thay bằng touch/fill + reaction | — |
| Reaction | Sau touch, giá rời proximal ≥ k·ATR trong m nến (DEF-FVG-04, k = 1.0, m = 6 — **HEURISTIC**) | Đây mới là "phản ứng" |
| Invalidation | Close cùng khung ngoài distal | Bác bỏ |

### 17.3 Ba câu hỏi của brief
1. *Giá chạm FVG nhưng không phản ứng — FVG còn valid?* Theo DEF-FVG-03 v0.1: **còn**, cho tới khi close xuyên distal hoặc hết hạn. Nhưng ghi `touch_count`; v1 7.3 và W3 đề xuất lần chạm sau kém tin cậy hơn — HYP-FVG-020.
2. *Xuyên qua 50% rồi bật lên — invalidated?* Theo I2 (close xuyên distal): **không**. Theo I3 (close xuyên CE): **có**. Chọn một, ghi rõ (§19).
3. *Full fill nhưng phản ứng mạnh — còn meaningful?* Theo định nghĩa: có (reaction xảy ra, chưa close beyond). Về giá trị dự báo: hình học cho 52% số lần chạm đi tới distal trước khi bật 1·size — full fill rồi bật là *bình thường*.

### 17.4 Năm quy tắc "FVG còn hiệu lực đến khi nào?" — đánh giá

| Quy tắc | Ưu điểm | Nhược điểm |
|---|---|---|
| R-a. Chỉ dùng lần chạm đầu (one-shot) | Đơn giản, tránh "gỡ" | Bỏ FVG HTF được dùng nhiều lần |
| R-b. Còn hiệu lực tới khi close xuyên distal | Chuẩn phổ biến, khách quan | FVG cũ "sống" rất lâu trên chart |
| R-c. Tới khi close xuyên CE | Thoát sớm, R nhỏ | Vô hiệu nhiều FVG vẫn chạy |
| R-d. Tối đa N lần chạm | Bắt ý "cạn dần" | N tùy chọn |
| R-e. Tới khi có reaction, hoặc hết hạn N nến | Gắn với mục đích giao dịch | Hai tham số |

**v0.1 đề xuất:** R-b + hết hạn 48 nến cùng khung cho LTF (M5/M15), không hết hạn cho HTF nhưng ghi `age_bars` — **HEURISTIC**; test R-a vs R-b như một biến thể.

---

## 18. FVG như Support / Resistance (brief §26)

### 18.1 Mô tả ≠ nhân quả
| Câu | Loại | Kiểm chứng được? |
|---|---|---|
| "Giá đã phản ứng quanh FVG" | **Mô tả** [OBSERVABLE] | Có — nhưng cần định nghĩa "phản ứng" |
| "FVG khiến giá phản ứng" | **Nhân quả** | Chỉ gián tiếp — so với vùng đối chứng, và kể cả khi FVG hơn đối chứng, nguyên nhân có thể là biến khác đi kèm FVG (volatility, thời điểm, trend) |
| "FVG có xác suất phản ứng cao hơn vùng đối chứng cùng hình học, sau khi kiểm soát các biến X" | **Giả thuyết dự báo** | Có — đây là dạng claim nên dùng |

### 18.2 Các biến có thể giải thích phản ứng — và trạng thái của chúng
| Biến | Đo bằng | Lý do có thể ảnh hưởng | Trạng thái |
|---|---|---|---|
| HTF context (bias, P/D) | Nhãn D1 ex-ante | Drift cùng chiều → FVG cùng chiều ít bị xuyên (FVG-Sim-02C) | HYP-FVG-004 |
| Chất lượng displacement | `c2_range_atr`, `c2_body_pct`, `broke_swing_level` | Proxy cho loại dòng lệnh | HYP-FVG-001 |
| Vị trí (range, DOL) | `pd_location`, `dist_to_dol_atr` | R:R và drift cục bộ | HYP-FVG-004/005 |
| Liquidity event trước đó | `sweep_before` | Câu chuyện stop-as-counterparty | HYP-FVG-008 |
| Trend / regime | ADX, độ dốc MA, tỷ lệ FVG cùng chiều chưa lấp | Drift | HYP-FVG-009 |
| Volatility | ATR percentile | Độ sâu fill, slippage | HYP-FVG-009 |
| Size | `size_atr` | Vùng rộng = stop xa | HYP-FVG-013 |
| Tuổi | `age_bars` | Thông tin cũ | HYP-FVG-003 |
| Số lần chạm trước | `touch_count` | "Cạn dần" | HYP-FVG-020 |
| Cách tiếp cận | `approach_speed` (v1 W2) | Grind = hấp thụ? | HYP-FVG-015 |
| Thời gian | killzone, macro (v1 7.3) | Thanh khoản, tin | HYP-FVG-018 |
| Nguồn gốc | `news_window`, `session_gap` (v1 W1) | Chất liệu khác | HYP-FVG-017 |
| Confluence | số yếu tố trùng | **Cẩn thận đếm trùng** (OB kề FVG theo cấu tạo, §12.2) | HYP-FVG-002 + đa kiểm định |

> [!warning] "FVG mạnh nếu có confluence" — vì sao câu này nguy hiểm
> (1) Các yếu tố confluence thường **không độc lập** (OB kề FVG theo cấu tạo; sweep và displacement cùng một sự kiện; FVG trong discount của range mà range được vẽ sau). (2) Càng nhiều yếu tố, càng ít mẫu, càng dễ **overfit** (v1 §15.1 điểm 5). (3) Sau khi biết kết quả, luôn tìm được một yếu tố "thiếu" để giải thích lệnh thua. Confluence chỉ có giá trị khi **danh sách yếu tố và cách chấm được khóa trước**, và được test như một biến (§29).

---

## 19. Invalidation — FVG bị vô hiệu khi nào? (brief §39)

![[FVG-Deep-09-Sau-Dinh-Nghia-Invalidation.svg|720]]
*FVG-Deep-09: Sáu định nghĩa invalidation. Chọn MỘT, ghi rõ, giữ nguyên khi backtest.*

### 19.1 So sánh sáu định nghĩa

| Định nghĩa | Điều kiện (bullish) | Ưu điểm | Nhược điểm | Dùng tốt nhất cho |
|---|---|---|---|---|
| **I1. Wick xuyên distal** | Low < distal | Khách quan, sớm | Bị wick/spike/news đánh lừa; phụ thuộc feed | Đặt stop (stop = distal − buffer) |
| **I2. Close xuyên distal** (cùng khung) | Close < distal | Chuẩn phổ biến, ít nhiễu | Trễ một nến; phụ thuộc khung | **Định nghĩa trạng thái v0.1** |
| **I3. Close xuyên CE** | Close < CE | Thoát sớm, stop ngắn | Vô hiệu nhiều FVG vẫn chạy | Biến thể "mean threshold" để test |
| **I4. Full traversal** | Low ≤ distal | Đo "đã rebalance xong" | Không nói về hướng | Thống kê fill |
| **I5. Structural** | Swing low bảo vệ FVG bị phá | Gắn cấu trúc | Cần định nghĩa swing + known_at | Kết hợp MSS ([[21-Market-Structure-Shift]]) |
| **I6. Contextual / time** | DOL đã bị lấy · hết hạn N nến · context D1 đổi | Tránh FVG "mồ côi" | Nhiều tham số | Quản lý danh sách FVG đang theo dõi |

### 19.2 DEF-FVG-03 (v0.1)
**Invalidated** = nến **cùng khung** với FVG đóng cửa ngoài distal (I2). **Expired** = quá N nến (48 cho M5/M15; HTF ghi `age_bars`, không hết hạn) hoặc context hết hiệu lực (I6). Stop thực tế = distal − buffer (0.1·ATR hoặc spread trung bình phiên) — I1 dùng cho *quản trị rủi ro*, I2 cho *trạng thái phân tích*. Đừng trộn: một nến M1 xuyên qua **không** vô hiệu H1 FVG (v1 7.5 điểm 5 — giữ nguyên).

### 19.3 Quy tắc xác nhận / vô hiệu hóa *(v1 §5, nguyên văn — có chú thích v2)*

![[FVG-Sec-05-Xac-Nhan.svg|720]]
*Sơ đồ: Điều kiện FVG được xem là hợp lệ vs bị vô hiệu — phân biệt fill / respect / mitigation / inversion.*

#### Setup được xem là hợp lệ khi
- [ ] FVG sinh ra từ displacement phá cấu trúc (BOS/MSS), có chủ đích.
- [ ] FVG nằm tại POI HTF đồng hướng Daily Bias.
- [ ] FVG đúng phía premium (Short) / discount (Long) của dealing range.
- [ ] Liquidity phía đối diện đã bị sweep trước khi displacement tạo FVG.
- [ ] Giá chạm CE / vùng FVG và **respect** (reject với phản ứng), không xuyên thủng.
- [ ] LTF có MSS + displacement xác nhận khi giá vào FVG.
- [ ] Có target liquidity rõ ràng và R:R đạt kế hoạch.

#### Setup bị vô hiệu khi
- [ ] Giá **đóng nến xuyên qua** toàn bộ FVG và giữ giá ngoài vùng (acceptance) → FVG invalid (có thể chuyển sang IFVG).
- [ ] FVG không sinh ra từ displacement — chỉ là gap nhỏ giữa range.
- [ ] Không có liquidity sweep trước khi vào FVG.
- [ ] FVG ở sai phía premium/discount cho hướng trade.
- [ ] FVG ngược Daily Bias mà không có bằng chứng HTF đảo.
- [ ] FVG đã bị test/ăn mòn nhiều lần, chất lượng giảm.
- [ ] LTF không tạo MSS/displacement khi giá vào FVG — chỉ "rơi xuyên" qua.

#### Fill vs Respect vs Mitigation vs Inversion

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Giá chạm CE (50%) hoặc mép gần FVG rồi reject với displacement ngược | **Respect** | FVG đang giữ; entry hợp lệ quanh CE, chờ LTF confirm |
| Giá lấp một phần FVG (chưa tới CE) rồi reject | **Partial fill / respect** | FVG vẫn còn hiệu lực; phản ứng tại đầu gap |
| Giá lấp toàn bộ FVG, chạm hết gap, rồi mới reject | **Full fill (mitigation)** | Imbalance đã rebalance; chỉ trade nếu có thêm POI/confirmation |
| Giá **đóng nến** xuyên thủng và giữ giá ngoài FVG | **Invalidation** | FVG hết hiệu lực; cảnh giác đảo cực thành IFVG |
| FVG bị xuyên + đóng nến qua → đổi vai trò support/resistance | **Inversion FVG (IFVG)** | Bullish FVG fail → thành kháng cự bearish; bearish FVG fail → thành hỗ trợ bullish |

> [!note]
> **Inversion FVG (IFVG)** là khái niệm mạnh: một FVG thất bại không "biến mất" — nó đảo cực. Khi bullish FVG bị đóng nến xuyên xuống, vùng đó trở thành **kháng cự**; giá retrace lên test lại nó là cơ hội Short (đồng hướng bias bearish mới). Ngược lại với bearish FVG fail thành hỗ trợ. IFVG là dấu hiệu thị trường đã đổi delivery, thường đi kèm MSS.

> [!note] Chú thích v2 cho v1 §5
> - Danh sách "Setup hợp lệ khi" là **danh sách bộ lọc context** (bias, P/D, sweep, LTF MSS…) — mỗi dòng là một giả thuyết đóng góp (HYP-FVG-004/007/008); giữ làm checklist thực hành, không coi là đã kiểm chứng.
> - Bảng "Fill vs Respect vs Mitigation vs Inversion": đúng hướng; v2 tách thêm "reaction" (có ngưỡng + cửa sổ) khỏi "respect" (§17.2) — "respect" không có ngưỡng thì mọi cú bật đều là respect.
> - Callout IFVG: "IFVG là dấu hiệu thị trường đã đổi delivery" → **[ICT FRAMEWORK]**; ở cấp quan sát: *một FVG bị close xuyên rồi giá quay lại vùng từ phía kia*. Giá trị dự báo của inversion → [[17-Inverse-Fair-Value-Gap-iFVG]], **[BACKTEST REQUIRED]**.

---

## 20. Vòng đời và State machine (brief §34, §35)

### 20.1 Vòng đời — phần nào quan sát được, phần nào là diễn giải

![[FVG-Deep-14-Vong-Doi-Quan-Sat-vs-Dien-Giai.svg|720]]
*FVG-Deep-14: Tám giai đoạn; mỗi giai đoạn có phần quan sát được (OHLC) và phần diễn giải ICT.*

Ba câu hỏi brief §34:
- **"Active" nghĩa chính xác là gì?** Không phải thuộc tính vật lý — là **quy ước**: chưa close xuyên distal (I2) và chưa hết hạn (I6). Ghi quy ước trong journal.
- **Lifecycle nào quan sát được?** Formed, touch, depth, full fill, close beyond, retest từ phía kia — đều quan sát được và có known_at. "Rebalanced", "respected", "delivery flipped" là nhãn diễn giải.
- **Invalidated nên định nghĩa bằng wick hay close?** Close (cùng khung) cho trạng thái; wick + buffer cho stop (§19.2).

### 20.2 Đánh giá state machine trong brief
State machine của brief (NO FVG → CREATED → UNMITIGATED → APPROACH → {NO TOUCH, PARTIAL, FULL} → REACTION? → {CONTINUE, REJECTION, ACCEPTANCE}) có năm điểm cần sửa để code được:
1. **Nhánh "NO TOUCH / PARTIAL / FULL" không loại trừ nhau theo thời gian** — một FVG có thể partial hôm nay, full fill ngày mai. Cần trạng thái *tăng dần* (TOUCHED → CE_REACHED → FULL_FILLED) + biến `max_depth`.
2. **"REACTION?" cần ngưỡng và cửa sổ khai báo trước** (k·ATR trong m nến). Không có thì không code được và mọi cú bật đều là reaction.
3. **Thiếu trạng thái kết thúc**: INVALIDATED (close beyond), EXPIRED (tuổi/context), INVERTED (IFVG).
4. **Thiếu PROVISIONAL**: tại close nến 2 chỉ có "gap tạm thời" — nhiều trader vẽ FVG ở đây (look-ahead, §21).
5. **Chuyển trạng thái chỉ tại close nến**, ghi bar index; nhãn **append-only** (không sửa nhãn cũ khi có thông tin mới).

### 20.3 State machine v0.1

![[FVG-Deep-15-State-Machine.svg|720]]
*FVG-Deep-15: State machine v0.1 — PROVISIONAL → ACTIVE_UNTOUCHED → TOUCHED → CE_REACHED → FULL_FILLED → INVALIDATED → INVERTED, cộng REACTED và EXPIRED. Pseudocode ở [[#Phụ lục B — Pseudocode]].*

Tham số v0.1 (**HEURISTIC**, khai báo trước, không chỉnh theo kết quả): `min_size = 0.25·ATR14` · `k = 1.0·ATR` · `m = 6 nến` · `N_expire = 48 nến` (LTF) · `invalidation = close cùng khung ngoài distal` · `buffer = 0.1·ATR`.

**Có thể chuyển FVG thành state machine đủ rõ để code/backtest không?** **Có** — với điều kiện mọi khái niệm "mềm" (reaction, active, valid) được thay bằng ngưỡng + cửa sổ + known_at. Phần *không* code được là chính phần diễn giải ("rebalanced", "smart money defended") — và đó là phần không cần cho backtest.

---

## 21. Real-time vs ex-post (brief §36)

![[FVG-Deep-17-Real-Time-vs-Ex-Post.svg|720]]
*FVG-Deep-17: Cùng một chart tại sáu thời điểm. Vùng xám là tương lai chưa tồn tại.*

### 21.1 Tại mỗi thời điểm, bạn thực sự biết gì?

| Thời điểm | Biết | Chưa biết |
|---|---|---|
| t1 — nến 2 đang chạy | H₁, L₁; giá hiện tại; high/low *tạm thời* của nến 2 | Close nến 2; nến 3; có FVG không |
| t2 — nến 2 đã đóng | Gap tạm thời g = C₂ − H₁ | Nến 3 có rơi về dưới H₁ không |
| t3 — nến 3 đang chạy | Low tạm thời của nến 3 → gap đang co lại | FVG còn hay mất; rộng bao nhiêu |
| **t4 — nến 3 đóng** | **FVG tồn tại; vùng, CE, size; known_at** | Giá có quay lại; sâu tới đâu |
| t5 — retrace | Đã chạm, max_depth hiện tại | Bật hay xuyên |
| t6 — kết quả | Reaction / invalidation (ex-post) | — |

### 21.2 Gap tạm thời ≠ FVG **[SIMULATION]**

![[FVG-Sim-05-Realtime-Lookahead.png|900]]
*FVG-Sim-05: (A) Tại close nến 2, FVG chỉ là một xác suất; (B) cùng FVG, cùng quy tắc — các lỗi backtest phổ biến tự tạo ra "edge".*

Tại close nến 2, nếu C₂ > H₁ thì có "gap tạm thời" g. Trên random walk, chỉ **48%** gap tạm thời sống sót qua nến 3:

| g (ATR) | 0.05 | 0.15 | 0.27 | 0.42 | 0.61 | 0.86 | 1.10 | 1.36 | 1.65 |
|---|---|---|---|---|---|---|---|---|---|
| P(FVG khi nến 3 đóng) | 11% | 22% | 36% | 51% | 65% | 81% | 90% | 96% | 99% |

Và khi sống sót, size cuối cùng chỉ còn ~**0.6–0.8** lần gap tạm thời (nến 3 ăn bớt). Công thức Brown 2Φ(g/σ_bar) − 1 khớp sát. → Vẽ FVG khi nến 3 chưa đóng = dùng thông tin chưa tồn tại; với gap tạm thời < 0.5 ATR, khả năng cao hơn là **không có FVG**.

### 21.3 Look-ahead bias — vì sao backtest FVG "dễ" một cách giả tạo
Cùng FVG (≥ 0.25 ATR), cùng quy tắc (limit tại proximal, stop distal − 0.1 ATR, target 2R), random walk:

| Cách backtest | Win rate | E[R] (fill lý tưởng) |
|---|---:|---:|
| **Đúng**: limit hoạt động từ nến i+1, khớp và phân xử trên đường giá 10 giây | **31.6%** | **−0.05** |
| **Bug 1**: coi low của chính nến 3 là "lần chạm đầu" (vào lệnh ở đáy nến 3 — thời điểm chỉ biết sau khi nến đóng) | **65.3%** | **+0.96** |
| **Bug 2a**: phân xử stop/target bằng OHLC nến H1, nến mơ hồ (chạm cả hai) = thắng | 50.2% | +0.51 |
| **Bug 2b**: như 2a nhưng nến mơ hồ = thua | 27.2% | −0.18 |

Bug 1 rất dễ mắc khi code "touch" bằng `low[j] <= proximal for j >= i` thay vì `j > i`, vì proximal của bullish FVG **chính là** low của nến 3. Bug 2 xảy ra khi backtest setup M5/M15 bằng dữ liệu H1, hoặc backtest tay trên chart khung lớn. **Một backtest FVG không nêu rõ known_at và độ phân giải phân xử không đáng tin.**

### 21.4 Giao thức thời gian thực chống hindsight (v0.1)
1. FVG chỉ được đánh dấu **sau** close nến 3; ghi bar index.
2. Mọi mức tham chiếu (swing, range, DOL) phải có known_at ≤ thời điểm quyết định.
3. Khi review chart cũ: **bar replay**, che phần bên phải, quyết định từng nến.
4. Chọn FVG theo **quy tắc khai báo trước** (vd FVG đầu tiên của leg displacement — [[48-1st-Presented-Fair-Value-Gap]]), không chọn sau khi thấy cái nào chạy.
5. Ghi cả setup **không vào** (missed / skipped) và lý do — dữ liệu cho ablation.
6. Backtest: phân xử stop/target ở khung ≤ 1/5 khung setup, hoặc tick; nến mơ hồ → **thua** (bảo thủ).

---

# PART VI — BỐI CẢNH

## 22. FVG + Market Structure / MSS (brief §29)

![[FVG-Deep-11-FVG-x-MSS.svg|720]]
*FVG-Deep-11: Bốn ô FVG × MSS — bốn ý nghĩa khác nhau.*

### 22.1 Hai câu hỏi độc lập
- **MSS** trả lời: *cấu trúc có đổi không?* — phụ thuộc swing nào bị phá và swing đó có ý nghĩa không ([[21-Market-Structure-Shift]], [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]).
- **FVG** trả lời: *leg đó có để lại vùng ít thời gian không?*

Một leg có thể phá cấu trúc mà không để lại FVG (nến chồng lấp), và có thể để lại FVG mà không phá gì (FVG bên trong range).

### 22.2 Bốn trường hợp
| Trường hợp | Ý nghĩa | Dùng thế nào |
|---|---|---|
| **FVG + MSS + displacement** | Leg vừa có hậu quả cấu trúc vừa để lại vùng một chiều | Ứng viên POI mạnh nhất trong 2022 Model — **vẫn là [HYPOTHESIS]** (HYP-FVG-007) |
| **FVG, không MSS** | FVG nội bộ range / leg con | Mặc định là nhiễu (~31 FVG/100 nến trên random walk) |
| **MSS, không FVG** | Cấu trúc đổi, leg chồng lấp | Không có FVG để retrace — dùng OB/breaker/IFVG hoặc bỏ; **không ép tìm "FVG ẩn"** |
| **Không cả hai** | Không có setup | Đứng ngoài là kết quả hợp lệ |

### 22.3 FVG có "structural meaning" hay chỉ là footprint?
**Footprint.** Ý nghĩa cấu trúc đến từ MSS (swing nào bị phá) và từ vị trí trong dealing range. FVG cho biết *leg đó đi nhanh* — một thuộc tính của *tốc độ*, không phải của *cấu trúc*. Kết hợp hai cái là hợp lý (leg nhanh + phá cấu trúc có ý nghĩa), nhưng đừng để FVG thay thế việc đánh giá swing.

### 22.4 Chuỗi "Displacement → Structural break → FVG → Retracement"
Không phải lúc nào cũng theo thứ tự này: FVG có thể hình thành *trước* khi phá swing (nến 2 lớn nhưng chưa vượt swing; nến 4–5 mới phá). Quy tắc chọn v0.1: **FVG đầu tiên của leg đã phá swing có ý nghĩa** (nếu nhiều FVG — §27.4). Ghi `fvg_before_mss` (y/n).

---

## 23. FVG + Liquidity Sweep (brief §30)

![[FVG-Deep-10-Chuoi-Sweep-FVG.svg|720]]
*FVG-Deep-10: Chuỗi Location → Liquidity event → Displacement → FVG → Retrace → Trigger — mỗi mắt xích là một bộ lọc có thể sai theo cách riêng.*

### 23.1 Trả lời từng câu của brief

| Câu hỏi | Trả lời | Nhãn |
|---|---|---|
| Có bắt buộc sweep trước FVG? | **Không.** Phần lớn FVG không đi sau sweep nào | [OBSERVABLE] |
| Có FVG mà không có sweep? | Có — rất phổ biến | [OBSERVABLE] |
| Có sweep mà không có FVG? | Có — rejection không displacement, hoặc leg chồng lấp | [OBSERVABLE] |
| FVG sau sweep có predictive value cao hơn? | **Chưa biết** | **[BACKTEST REQUIRED]** — HYP-FVG-008 |
| Nếu có, cơ chế là gì? | Các ứng viên: (a) stop bị kích hoạt làm đối ứng cho lệnh lớn ngược chiều → cú đảo có "chủ"; (b) breakout trader bị kẹt phải thoát → thêm dòng lệnh cùng chiều đảo; (c) rejection tại mức nổi bật là *thông tin* (không ai chấp nhận giá ở đó) | [MARKET MECHANICS] cho (a)(b) — Osler 2005; [INTERPRETATION] cho (c) |

### 23.2 Trình tự phổ biến ≠ định luật nhân quả
Chuỗi "Liquidity → Sweep → Displacement → FVG → Retracement" là **mô tả của một kịch bản** mà ICT 2022 Model chọn để giao dịch. Nó không nói kịch bản đó xảy ra thường xuyên hơn các kịch bản khác, cũng không nói rằng khi các bước đầu đã xảy ra thì các bước sau "phải" xảy ra. Phân tích chi tiết từng mắt xích và cách nó sai: [[20-Liquidity-Sweep]] §15.3 (bảng "Có thể sai thế nào / Phép thử").

### 23.3 Ablation — câu hỏi backtest đúng
Bỏ từng mắt xích, expectancy đổi bao nhiêu? Nếu bỏ "sweep" mà expectancy không đổi (trong khoảng tin cậy) → điều kiện sweep không đóng góp thông tin *trong dữ liệu đó*. Thiết kế đầy đủ ở §40 (Model A–D).

---

## 24. FVG + POI (brief §31)

### 24.1 Năm thứ khác nhau
| Thành phần | Câu hỏi | Ví dụ | Sai thế nào |
|---|---|---|---|
| **Location (HTF)** | Ở đâu trong bức tranh lớn? | Discount của dealing range D1 | Range vẽ sau khi thấy giá phản ứng |
| **POI** | Chờ giá ở vùng nào? | D1 bullish FVG 1.0820–1.0860 + OB dưới nó | Chọn POI sau sự kiện |
| **FVG (của leg phản ứng)** | Nếu giá quay lại, vào ở đâu? | H1 FVG 1.0832–1.0841 sau sweep | Chọn FVG "đẹp nhất" sau khi biết |
| **Confirmation** | Phản ứng có hậu quả cấu trúc? | M5 MSS + displacement trong POI | MSS vi mô |
| **Entry trigger** | Khi nào bấm nút? | Limit tại CE của M5 FVG | Fill giả, look-ahead |

### 24.2 FVG có phải POI không?
**Một HTF FVG có thể được *chọn* làm POI** (nó là một vùng giá có định nghĩa). Nhưng "là POI" là quyết định của người phân tích dựa trên context — không phải thuộc tính của FVG. Ngược lại, **FVG không phải entry signal**: nó là *nơi* có thể vào lệnh, còn *khi nào* cần trigger.

### 24.3 Chuỗi đầy đủ và đánh giá

```text
HTF Context (D1: bias, range, DOL)
     ↓   lọc: có hypothesis hướng?               [có thể sai: bias sai — xem 59-Daily-Bias]
POI (vùng chờ)
     ↓   lọc: giá tới POI trong killzone?        [có thể sai: POI chọn sau]
Liquidity Event (H1)
     ↓   lọc: mức ex-ante bị xuyên + rejection?  [có thể sai: nhãn đổi theo khung]
Displacement + MSS
     ↓   lọc: phá swing level ≥ 2?               [có thể sai: MSS vi mô]
FVG (của leg đó)
     ↓   lọc: size ≥ min, quy tắc chọn cố định?  [có thể sai: chọn sau khi biết]
Retracement
     ↓   lọc: quay lại trong W nến? cách tiếp cận?  [có thể sai: không quay lại; grind]
Execution Trigger (M5)
         limit CE / M5 MSS trong FVG             [có thể sai: fill giả, adverse selection]
```

---

## 25. FVG + Dealing Range, Premium / Discount (brief §32)

![[FVG-Deep-20-Dealing-Range-DOL.svg|720]]
*FVG-Deep-20: Cùng là bullish FVG, vị trí trong dealing range và so với DOL thay đổi vai trò: entry (discount), trung tính (EQ), chase (premium), vật cản (bearish FVG chưa lấp trên đường đi).*

### 25.1 Câu hỏi của brief
- **FVG ở discount có khác FVG ở premium không?** Về hình học: không. Về *hệ quả giao dịch*: có — với cùng DOL ở range high, bullish FVG ở discount cho **R:R danh nghĩa lớn hơn** và (nếu bias đúng) drift cùng chiều dài hơn. Nhưng "R:R lớn hơn" không phải "xác suất cao hơn"; với random walk, R:R lớn đi kèm p_null nhỏ hơn đúng tỷ lệ.
- **Bullish FVG ở discount luôn tốt hơn bullish FVG ở premium?** **Không được coi là luật.** Đó là **heuristic ICT** — **[BACKTEST REQUIRED]** (HYP-FVG-004b). Trong trend mạnh, FVG ở premium (continuation) có thể là chỗ duy nhất giá cho retrace.
- **FVG gần equilibrium?** Trung tính; nhiều note trong vault coi EQ là vùng "nhiễu nhất" — giả thuyết hợp lý, chưa kiểm chứng.
- **FVG gần external liquidity?** FVG ngay dưới range high (bullish) = gần target → R:R còn lại nhỏ; FVG ngay trên range low sau sweep SSL = kịch bản 2022 Model.

### 25.2 Cách đo để test
`pd_location = (CE − range_low)/(range_high − range_low)` với range có **known_at** trước FVG; so sánh reaction/expectancy theo quintile của `pd_location` **và** so với vùng đối chứng ở cùng quintile. Range phải được xác định bằng thuật toán khai báo trước ([[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]]).

---

## 26. FVG + Draw on Liquidity (brief §33)

### 26.1 Bốn vai trò của FVG so với DOL

```text
(1) FVG là ENTRY LOCATION                      (2) FVG là CONTINUATION LOCATION
Current Price                                   DOL (BSL)
     ↓ retrace                                    ↑
FVG (cùng chiều DOL)  ← vào lệnh                 FVG mới nhất trên leg đang chạy ← chỗ nghỉ
     ↓                                            ↑
Liquidity → DOL                                  Trend

(3) FVG là REACTION AREA / OBSTACLE            (4) FVG là TARGET (draw)
DOL (BSL)                                       HTF FVG chưa lấp phía trước
     ↑ bị cản?                                    ↑ mục tiêu trung gian?
Bearish FVG chưa lấp ← vật cản                   Giá hiện tại
     ↑
Giá hiện tại
```

### 26.2 Hai chuỗi của brief
- **"Current price → FVG → Liquidity → DOL"**: FVG là trạm dừng trên đường tới DOL — vai trò (1) hoặc (3) tùy chiều.
- **"DOL → Liquidity event → Displacement → FVG → Retracement"**: FVG sinh ra *sau* một sự kiện tại/ngược DOL — kịch bản reversal (§28).

### 26.3 FVG có "ý nghĩa khác" khi nằm trên đường tới DOL?
Về cơ chế: nếu bias và DOL đúng (drift cùng chiều), FVG cùng chiều ít bị xuyên hơn (FVG-Sim-02C) — nhưng đó là hiệu ứng của **drift**, và drift chính là thứ bias đang cố đoán. Câu hỏi kiểm định được: *khi kiểm soát độ chính xác của bias (biết ex-post), FVG có thêm thông tin không?* — HYP-FVG-005. "HTF FVG là target" — HYP-FVG-010 (so với mức ngẫu nhiên cùng khoảng cách).

Xem thêm hệ thống DOL: [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]].

---

## 27. Đa khung D1 → H1 → M5 và Nesting (brief §37, §38)

### 27.1 FVG ở mỗi tầng trả lời một câu hỏi khác

![[FVG-Deep-12-HTF-LTF-Tang-FVG.svg|720]]
*FVG-Deep-12: D1 FVG = location; H1 FVG = setup; M5 FVG = execution. Ba lớp vùng lồng nhau.*

| Tầng | Vai trò FVG | Câu hỏi |
|---|---|---|
| **D1 — CONTEXT** | Location / draw; vùng quan tâm | Vùng nào đáng chờ? FVG có trên đường tới DOL? |
| **H1 — SETUP** | FVG của leg phản ứng trong POI | Phản ứng có hình thành? Leg có phá cấu trúc? |
| **M5 — EXECUTION** | Điểm vào, stop ngắn | Khi nào vào? Stop ở đâu? R:R còn đủ? |

### 27.2 Câu hỏi của brief
- **HTF FVG luôn mạnh hơn LTF FVG?** "Mạnh hơn" theo nghĩa *phản ứng lớn hơn tính bằng giá*: gần như hiển nhiên (vùng và ATR lớn hơn). Theo nghĩa *xác suất phản ứng (chuẩn hóa ATR) cao hơn đối chứng*: **chưa biết** — HYP-FVG-014.
- **M5 FVG chỉ meaningful khi nằm trong H1/D1 context?** Trong framework D1→H1→M5 — **theo quy ước, có**: M5 không được dùng độc lập. Về thực nghiệm, đây là ablation Model A vs Model D (§40).
- **FVG nested trong FVG có ý nghĩa gì?** Một *bộ lọc số lượng* mạnh (§27.3) — nesting giảm số ứng viên ~17 lần; chưa phải bằng chứng.
- **D1 bearish nhưng M5 bullish FVG?** D1 thắng: M5 bullish chỉ là (a) entry short khi bị phá (IFVG), hoặc (b) bỏ qua. Không long ngược D1 trừ khi đang test một model countertrend được ghi riêng.

### 27.3 Mô phỏng: FVG là thuộc tính của khung **[SIMULATION]**

![[FVG-Sim-06-Timeframe-Nesting.png|900]]
*FVG-Sim-06: (A) "LTF void xác nhận HTF FVG" gần như tự động; (B) FVG là vùng ít thời gian tại giá — theo định nghĩa; (C) nesting là bộ lọc số lượng mạnh.*

Trên một random walk 6 triệu phút gộp thành M5 / M15 / H1 (FVG ≥ 0.25 ATR của khung đó):
- **98.2%** H1 FVG chứa ít nhất một M5 FVG cùng chiều hình thành trong nến 2 của H1, phủ trung bình **65%** chiều cao vùng H1.
- **99.9%** nến H1 lớn (≥ 1.5 ATR) *không* tạo H1 FVG cũng chứa M5 FVG cùng chiều → "xác nhận bằng LTF liquidity void" **không phân biệt** được nến H1 có FVG với nến H1 không có FVG.
- Thời gian/đơn vị giá trong vùng H1 FVG: trung vị **0.56×** phần còn lại (IQR 0.37–0.83).
- Có **3.2** M5 FVG mỗi nến H1; chỉ **5.7%** M5 FVG nằm trọn trong một H1 FVG chưa bị phá (cùng chiều), **3.6%** trong M15 FVG, **0.8%** trong cả hai.

### 27.4 Nhiều FVG cùng lúc — xếp chồng, chồng lấn, xung đột, lồng nhau

![[FVG-Deep-13-Nhieu-FVG-Chon-Cai-Nao.svg|720]]
*FVG-Deep-13: Stacked (cùng leg), overlap ngược hướng (BPR), conflict HTF–LTF, nested. Quy tắc chọn phải khai báo trước.*

| Tình huống | Quy tắc v0.1 (**HEURISTIC**) | Vì sao |
|---|---|---|
| Stacked (một leg để lại nhiều FVG) | Chọn **FVG đầu tiên** của leg (first presented) **hoặc** FVG có CE trong discount của leg — chọn MỘT, ghi trước | Tránh chọn sau khi biết cái nào chạy |
| Overlap ngược hướng (BPR) | Ghi là BPR, không coi là FVG đơn | [[03-Balanced-Price-Range]] |
| Conflict HTF ngược LTF | HTF thắng | Framework D1 → M5 |
| Nested | Ghi `nested_in = H1/M15/none` | Biến để test HYP-FVG-014 |
| HTF zone vs LTF precision | HTF cho vùng, LTF cho mức vào; stop theo LTF chỉ khi R:R tính tới HTF target | v1 EC6: fractal conflict |

### 27.5 Mốc đóng nến và "FVG ẩn trong wick" *(hình v1, chưa được nhúng ở v1)*

![[FVG-EdgeB-BrokerOffsetH1.svg|720]]
*Hình v1 (EdgeB): Cùng dữ liệu M1, gộp thành nến H1 theo hai mốc giờ server khác nhau → một broker có FVG, broker kia không.*

> [!note] Nhãn v2
> **[MATHEMATICAL]** — đúng và quan trọng: FVG phụ thuộc mốc gộp nến. Quy tắc trong hình ("xác nhận FVG HTF quan trọng trên ít nhất 2 nguồn dữ liệu / server-time") là **[HEURISTIC]** hợp lý. Với futures, dùng mốc giờ sàn (CME); với FX, ghi rõ giờ server của dữ liệu backtest.

![[FVG-EdgeB-HiddenInHTFWick.svg|720]]
*Hình v1 (EdgeB): M5 FVG "ẩn" trong bóng nến H1 sweep — chỉ thấy khi zoom xuống LTF.*

> [!warning] Rà soát v2 — đây là một bẫy hindsight
> Hình v1 kể rằng "displacement thật xảy ra trên M5, tạo FVG thật sự là POI; nhìn H1 đơn độc sẽ bỏ lỡ lý do đảo chiều". Nhưng FVG-Sim-06A cho thấy **gần như mọi nến H1 lớn đều chứa M5 FVG cùng chiều** — kể cả trên random walk. Vì vậy, *sau khi* thấy giá đảo chiều ở một bóng nến H1, việc tìm được một M5 FVG bên trong là **gần như chắc chắn**, không phải một phát hiện. Phiên bản không hindsight: khai báo trước "M5 FVG đầu tiên sau sweep trong POI H1" là entry, rồi test tần suất nó cho reaction so với đối chứng.

### 27.6 Quy trình đa khung *(v1 §4, nguyên văn)*

![[FVG-Sec-04-Da-Khung.svg|720]]
*Sơ đồ: Luồng phân tích đa khung D1/H4 → H1/M15 → M5/M1 để định vị và vào lệnh tại FVG.*

> [!example] Quy trình 4 câu bắt buộc trước khi dùng FVG
> 1. **FVG này sinh ra từ displacement phá cấu trúc hay chỉ là gap giữa range?**  
> 2. **Nó nằm ở POI HTF nào và đúng premium/discount cho hướng bias không?**  
> 3. **Liquidity đã bị sweep trước khi FVG hình thành chưa?**  
> 4. **CE của FVG ở đâu, và điều gì làm FVG này invalid?**

#### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[59-Daily-Bias]]).
- **HTF FVG / imbalance làm DRAW:** có FVG D1/H4 nào còn mở mà giá bị hút về để rebalance không? Đây thường là **target** chứ không phải entry.
- **HTF FVG làm POI:** có D1/H4 FVG đồng hướng bias, đúng premium/discount, còn unmitigated không?
- **Vị trí premium/discount:** FVG cần Long phải ở discount; FVG cần Short phải ở premium của HTF dealing range.

#### H1 / M15 — POI & Context
- **POI cụ thể:** ghi rõ vùng FVG H1/M15 và mức CE, ví dụ `H1 bullish FVG 1.0820–1.0835, CE = 1.08275`.
- **Lý do POI hợp lệ:** FVG có sinh ra từ displacement không? Có ở đúng premium/discount không? Còn unmitigated không? Đồng hướng draw on liquidity không?
- **Liquidity:** giá đã sweep pool đối diện chưa? Sweep ở đâu, reclaim/reject thế nào?
- **Phân biệt fill vs respect:** giá chạm CE rồi reject (respect) khác với giá lấp toàn bộ FVG rồi đóng nến xuyên qua (invalid).

#### M5 / M1 — Confirmation & Entry
- **Có MSS không?** sau khi giá vào FVG POI, có bullish/bearish MSS xác nhận đảo hướng nội bộ không?
- **Có displacement LTF không?** displacement LTF thường tạo một FVG nhỏ hơn để làm entry refined.
- **Entry tại đâu trong FVG?** ICT thường ưu tiên entry quanh **CE (50%)** thay vì mép xa của gap, để cải thiện R:R.
- **Stop loss logic:** đặt ngoài đầu kia của FVG / ngoài điểm sweep, không đặt tùy ý.

```text
Mẫu ghi nhanh — Bullish FVG Entry
HTF Bias: Bullish | Location: Discount
Draw on liquidity: BSL tại [level]
POI: H1 bullish FVG [low]–[high], CE = [mid]
Sweep: đã quét SSL dưới [level] trước khi displacement
Entry plan: chờ giá retrace về CE của H1 FVG → M5 bullish MSS + FVG → entry quanh CE
Stop: dưới low của FVG / dưới sweep low
Target: internal liquidity trước, BSL chính sau
Invalid: đóng nến M5/H1 xuyên thủng dưới FVG (acceptance) → bỏ / chờ IFVG
```

```text
Mẫu ghi nhanh — Bearish FVG Entry
HTF Bias: Bearish | Location: Premium
Draw on liquidity: SSL tại [level]
POI: H1 bearish FVG [low]–[high], CE = [mid]
Sweep: đã quét BSL trên [level] trước khi displacement
Entry plan: chờ giá retrace lên CE của H1 FVG → M5 bearish MSS + FVG → entry quanh CE
Stop: trên high của FVG / trên sweep high
Target: internal liquidity trước, SSL chính sau
Invalid: đóng nến M5/H1 xuyên thủng trên FVG (acceptance) → bỏ / chờ IFVG
```

> [!warning]
> **FVG trên M5/M1 không "tạo" bias.** Nó chỉ là execution refinement. Một bullish M5 FVG ngược Daily Bearish Bias không cho phép Long, trừ khi HTF narrative đã thực sự đảo.

> [!note] Chú thích v2 cho v1 §4
> Quy trình và mẫu ghi nhanh **giữ nguyên**. Bổ sung khi ghi: `known_at` của FVG H1, `fvg_size_atr`, `fvg_pos_in_leg`, `approach_speed`, `nested_in`, quy tắc chọn FVG (first presented / discount-of-leg). Cảnh báo cuối của v1 ("FVG M5/M1 không tạo bias") là **đúng và quan trọng nhất** của mục này.

### 27.7 FVG theo trục thời gian *(v1 §7.3, nguyên văn — có chú thích v2)*

ICT nhấn mạnh **thời gian đứng trước giá**: cùng một cấu trúc FVG, giá trị hoàn toàn khác nhau tùy thời điểm hình thành.

- **FVG trong Kill Zone > ngoài Kill Zone.** FVG sinh trong London Open / NY AM ([[18-Kill-Zones]]) mang intent của thuật toán ở thời điểm delivery chính. FVG hình thành trong lunch (12:00–13:00 NY) hoặc cuối NY PM thường là nhiễu thanh khoản mỏng.
- **Macro windows.** Các cửa sổ macro (~9:50–10:10, 10:50–11:10, 13:10–13:40, 14:50–15:10 NY time) là lúc thuật toán chạy run-on-liquidity / rebalance. FVG hình thành hoặc được retest trong macro có xác suất phản ứng cao hơn rõ rệt — đặc biệt với NQ.
- **First Presented FVG (FPFVG).** FVG **đầu tiên** hình thành sau 9:30 open của index futures là anchor của NY AM session model: giá thường quay lại rebalance FPFVG trước khi chạy leg chính của phiên sáng. Kết hợp với Silver Bullet window (10:00–11:00: tìm FVG entry đầu tiên trong cửa sổ này) tạo thành playbook thời gian cụ thể cho NQ.
- **Tuổi của FVG.** LTF FVG (M1–M15) hết hạn nhanh — thường chỉ trong phiên; nếu qua ngày mà chưa được dùng, giá trị giảm mạnh. HTF FVG (H4/D1/W) giữ giá trị nhiều ngày tới nhiều tuần. FVG D1/W chưa lấp của tuần trước là draw tự nhiên cho tuần sau.
- **Số lần test.** Mỗi lần giá chạm vào FVG mà chưa xuyên, một phần lệnh trong đó được tiêu thụ → **first touch đáng tin nhất**, từ lần 3 trở đi coi như đã cạn.

> [!note] Chú thích v2 cho v1 §7.3
> | Claim v1 | Nhãn v2 |
> |---|---|
> | "FVG trong Kill Zone > ngoài Kill Zone" | **[HYPOTHESIS]** — HYP-FVG-018; cơ chế hợp lý: thanh khoản và dòng lệnh thật tập trung trong giờ chính |
> | Macro windows "xác suất phản ứng cao hơn rõ rệt — đặc biệt với NQ" | **[HYPOTHESIS]**, chưa có dữ liệu trong vault; "rõ rệt" bỏ cho tới khi có số |
> | FPFVG "giá thường quay lại rebalance FPFVG" | **[ICT FRAMEWORK]**; phần "thường" cần so với đường nền hình học (§13.3) |
> | "LTF FVG hết hạn nhanh; HTF FVG giữ giá trị nhiều ngày" | **[HEURISTIC]** — nhất quán với DEF-FVG-03 (expire 48 nến LTF) |
> | "Mỗi lần chạm tiêu thụ một phần lệnh → first touch đáng tin nhất" | Cơ chế "tiêu thụ lệnh" là **[INTERPRETATION]** (§9.6); claim "first touch tốt hơn" là **[HYPOTHESIS]** — HYP-FVG-020 |

### 27.8 Delivery state và chuỗi re-delivery *(v1 §7.4, nguyên văn — có chú thích v2)*

Đây là tầng hiểu sâu nhất về FVG: **BISI/SIBI không chỉ là "vùng" — chúng mô tả TRẠNG THÁI delivery của thị trường.**

- Một BISI đang được respect nghĩa là thị trường đang ở trạng thái **buy-side delivery** (dòng chào giá lên). Khi giá trade through BISI và đóng nến dưới nó, trạng thái flip sang **sell-side delivery** — và vùng đó trở thành IFVG. Inversion không phải "pattern", nó là **bằng chứng đổi trạng thái delivery**.
- **Chuỗi re-delivery trong trend:** một trend giảm sạch sẽ vận hành theo chu kỳ `tạo SIBI → retrace rebalance SIBI (chạm CE) → expansion xuống tạo SIBI mới → lặp lại`. Trade trend = trade chuỗi rebalance các SIBI liên tiếp; SIBI **mới nhất** (gần giá nhất) được respect trước.
- **Stacked FVGs:** một leg để lại 2–3 FVG cùng hướng xếp chồng = institutional sponsorship mạnh; ưu tiên FVG gần nhất làm entry, các FVG sâu hơn làm phòng tuyến dự phòng.
- **Leg không để lại FVG nào** = thiếu displacement/intent → nhiều khả năng đó là retracement (corrective) chứ không phải impulse. Đây là cách dùng FVG để **đọc cấu trúc**, không chỉ để entry: leg nào có FVG là leg có chủ đích.

> [!note] Chú thích v2 cho v1 §7.4
> - "BISI/SIBI mô tả trạng thái delivery" — **[ICT FRAMEWORK]**; ở cấp quan sát, "trạng thái" có thể đo bằng **tỷ lệ FVG cùng chiều chưa bị close xuyên** trong N nến gần nhất — một proxy của drift (FVG-Sim-02C). Đây là cách biến ý tưởng của v1 thành biến kiểm chứng được (HYP-FVG-009).
> - "Leg không để lại FVG nào = thiếu displacement → nhiều khả năng là retracement" — **[HYPOTHESIS]** hợp lý (leg chồng lấp = tốc độ thấp); test: tỷ lệ leg có FVG trong impulse vs corrective được gán nhãn bằng thuật toán swing khai báo trước.
> - "Stacked FVGs = institutional sponsorship mạnh" — phần "institutional" là **[INTERPRETATION]**; phần "leg dài một chiều" là [OBSERVABLE].

---

# PART VII — ỨNG DỤNG GIAO DỊCH

## 28. FVG → Continuation vs FVG → Reversal (brief §43)

![[FVG-Deep-19-Continuation-vs-Reversal.svg|720]]
*FVG-Deep-19: Cùng hình FVG, hai kịch bản đòi hỏi hai loại bằng chứng khác nhau.*

| Chiều so sánh | FVG → Continuation | FVG → Reversal |
|---|---|---|
| Chuỗi | Trend → displacement → FVG → retrace → tiếp diễn | Liquidity event → displacement → MSS → FVG → retrace → đảo chiều |
| Context | Cấu trúc HTF đã cùng chiều | Giá tại POI HTF, thường ở cực của dealing range |
| Cấu trúc | Leg cùng chiều HH-HL (hoặc LH-LL) | Leg ĐẦU TIÊN phá swing ngược cấu trúc cũ |
| Liquidity | Không bắt buộc sweep; mục tiêu là liquidity phía trước | Sweep mức ex-ante là thành phần chính của câu chuyện |
| DOL | Phía trước, cùng chiều trend | Phía đối diện (vừa đổi) |
| Displacement | Thường vừa phải, lặp lại (chuỗi FVG) | Cần rõ để phân biệt với pullback |
| Timeframe | FVG trên khung setup (H1/M15) | Thường cần MSS trên khung setup + FVG LTF |
| Rủi ro chính | Trend già → retrace sâu thành đảo chiều | Chỉ là pullback của trend cũ (MSS vi mô) |
| Thất bại điển hình | FVG mới nhất bị close xuyên → state đổi | Liquidity-type displacement → lấp hết (FVG-Sim-03) |
| Cơ chế ủng hộ (nếu đúng) | Drift / metaorder tiếp diễn | Stop-as-counterparty; dòng lệnh đảo chiều thật |
| Đường nền hình học | FVG cùng chiều drift ít bị chạm (FVG-Sim-02C) | Không có drift trước sự kiện → hình học thuần |

> [!tip] Hệ quả thực hành
> Continuation FVG được lợi từ **drift** (nếu trend tiếp tục, FVG ít bị xuyên — nhưng cũng ít khi cho entry). Reversal FVG phải tự chứng minh bằng **sự kiện** (sweep + MSS) vì không có drift sẵn hỗ trợ. Ghi `fvg_context = continuation / reversal` để thống kê riêng — gộp chung sẽ che mất cả hai.

---

## 29. FVG Hierarchy và Significance Score (brief §27, §28)

### 29.1 Không phải FVG nào cũng như nhau — nhưng "quan trọng hơn" phải được đo

| Chiều | Biến đo (ex-ante) | Giả định của ICT/v1 | Trạng thái |
|---|---|---|---|
| Timeframe | D1 / H4 / H1 / M15 / M5 / M1 | HTF quan trọng hơn | HYP-FVG-014 |
| Size tương đối | `size_atr` | Đủ lớn nhưng không quá lớn | HYP-FVG-013 |
| Chất lượng displacement | `c2_range_atr`, `c2_body_pct`, `leg_bars` | Mạnh hơn = tốt hơn | HYP-FVG-001 (toy: có thể ngược — §30.4) |
| Hậu quả cấu trúc | `broke_swing_level` (0–5) | Phá swing có ý nghĩa = tốt hơn | HYP-FVG-007 |
| Location | `pd_location` | Discount (long) / premium (short) | HYP-FVG-004b |
| HTF alignment | D1 bias label ex-ante | Cùng chiều = tốt hơn | HYP-FVG-004 |
| Liquidity context | `sweep_before`, `dist_to_opposing_liq_atr` | Sau sweep = tốt hơn | HYP-FVG-008 |
| Freshness | `touch_count`, `age_bars` | First touch, FVG mới = tốt hơn | HYP-FVG-003, 020 |
| Dealing range | `in_range`, `near_external` | — | HYP-FVG-004b |
| DOL | `dist_to_dol_atr`, `between_price_and_dol` | Trên đường tới DOL = tốt hơn | HYP-FVG-005 |
| Market regime | trend proxy, ATR percentile, session | — | HYP-FVG-009 |

### 29.2 FVG Significance Score (FSS) v0.1 — một đề xuất nghiên cứu, không phải quy tắc

Thành phần (mỗi thành phần đo được **trước** khi retrace; tổng 0–14):

| Thành phần | 0 | 1 | 2 |
|---|---|---|---|
| S1 Displacement | c2 range < 1.5 ATR | 1.5–2 ATR | ≥ 2 ATR |
| S2 Cấu trúc | không phá swing | phá swing level 1–2 | phá swing level ≥ 3 |
| S3 Location (so với range có known_at) | sai nửa | đúng nửa | đúng ⅓ ngoài |
| S4 HTF alignment | ngược D1 | D1 trung tính | cùng D1 |
| S5 Liquidity | không có sự kiện | xuyên mức nhỏ | sweep mức ex-ante level ≥ 3 trong ≤ 10 nến trước nến 2 |
| S6 Freshness | đã chạm ≥ 2 lần | đã chạm 1 lần | chưa chạm |
| S7 Thời gian & nguồn gốc | trong news window | ngoài killzone | trong killzone, không tin |

**Có nên score FVG không?** — Đánh giá trung thực:

| Ưu | Nhược |
|---|---|
| Buộc khai báo tiêu chí trước → chống hindsight | Trọng số tùy chọn; tổng cộng giả định các thành phần cộng tính và độc lập |
| Biến "cảm giác FVG đẹp" thành số ghi được | Các thành phần **tương quan** (S1–S2–S5 thường cùng một sự kiện) → đếm trùng |
| Cho phép test theo bậc (FSS thấp/trung/cao) | Nhiều thành phần + ít mẫu = **overfit**; số bậc phải ít |
| — | Tương tác bị che: S1 cao có thể *xấu* khi S5 thấp (liquidity-type) — tổng điểm không thể hiện được |

**Đề xuất sử dụng:** (1) khóa định nghĩa FSS v0.1 trước khi thu dữ liệu; (2) chỉ dùng **3 bậc** (0–5, 6–9, 10–14); (3) báo cáo kết quả từng thành phần riêng (ablation) song song với tổng; (4) với ≥ 1,000 mẫu mới cân nhắc mô hình hồi quy logistic có kiểm định ngoài mẫu. **Biến đo được vs chủ quan:** S1, S5 (nếu mức ex-ante có thuật toán), S6, S7 đo được tự động; S2, S3, S4 phụ thuộc thuật toán swing/range/bias — phải dùng định nghĩa đã chuẩn hóa trong vault ([[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]], [[59-Daily-Bias]]).

### 29.3 Best Practices *(v1 §7.5, nguyên văn — có chú thích v2)*

> [!success] Best Practices
> 1. **Chấm điểm trước khi trade.** Mỗi FVG được chấm theo 5 tiêu chí: (1) sinh từ displacement phá BOS/MSS, (2) tại/trùng POI HTF, (3) đúng premium/discount, (4) sau liquidity sweep, (5) còn unmitigated. **Chỉ trade FVG đạt 4/5 trở lên.**
> 2. **Chọn trước, không vẽ đuổi.** Đánh dấu tối đa 2–3 FVG "đáng theo dõi" từ pre-market. FVG vẽ mới trong lúc giá đang chạy = quyết định FOMO, chất lượng thấp.
> 3. **Confluence thay số lượng.** FVG chồng OB (fair value area), CE trùng OTE/equilibrium, FVG nằm trong HTF FVG — một setup confluence đáng giá hơn năm setup đơn lẻ.
> 4. **Entry mặc định tại CE.** Aggressive tại proximal chỉ khi displacement cực mạnh và sweep rõ; conservative khi fill sâu. Ghi `entry_relative_to_ce` vào journal để backtest.
> 5. **Invalidation đúng timeframe.** FVG H1 cần **H1 đóng nến** xuyên distal mới invalid — một cây M1 xuyên qua không có ý nghĩa. Sai timeframe khi đánh giá invalidation là nguồn thoát non/gồng sai phổ biến nhất.
> 6. **Tôn trọng thời gian.** Ưu tiên FVG hình thành/retest trong kill zone và macro window; với NQ chú ý FPFVG sau 9:30 và Silver Bullet 10:00–11:00.
> 7. **Log để kiểm chứng.** Thêm vào frontmatter trade: `fvg_from_displacement`, `entry_relative_to_ce` (proximal/CE/distal), `fill_depth`, `in_killzone`, `fvg_age` — sau 30+ mẫu mới đủ dữ liệu chỉnh rule.
> 8. **Một FVG fail là dữ liệu, không phải thất bại.** Khi FVG bị xuyên, việc đầu tiên là đánh dấu IFVG và hỏi "delivery state đã flip chưa?" — thay vì tìm FVG khác cùng hướng để "gỡ".

> [!note] Chú thích v2 cho v1 §7.5
> | Điểm v1 | Nhãn / đánh giá v2 |
> |---|---|
> | 1. Chấm 5 tiêu chí, chỉ trade ≥ 4/5 | **[HEURISTIC]** — tiền thân của FSS (§29.2); giữ, và test như biến thể |
> | 2. Chọn trước, không vẽ đuổi | **Xuất sắc** — chính là giao thức chống hindsight (§21.4) |
> | 3. Confluence thay số lượng | Đúng tinh thần; cẩn thận đếm trùng (§12.2, §18.2) |
> | 4. Entry mặc định tại CE | **[HEURISTIC]**; ghi `entry_relative_to_ce` — đúng |
> | 5. Invalidation đúng timeframe | **Đúng** — đưa vào DEF-FVG-03 |
> | 6. Tôn trọng thời gian (killzone, macro, FPFVG, Silver Bullet) | **[HYPOTHESIS]** — HYP-FVG-018 |
> | 7. Log để kiểm chứng; "sau 30+ mẫu mới đủ dữ liệu chỉnh rule" | Đúng hướng, **cỡ mẫu quá nhỏ**: 30 mẫu cho CI win rate ±17.5 điểm (§43.1). 30 mẫu đủ để *phát hiện lỗi thô và sinh giả thuyết*, không đủ để *chỉnh rule* |
> | 8. Một FVG fail là dữ liệu | **Xuất sắc** — giữ nguyên |

---

## 30. Vì sao một FVG "chạy" còn FVG khác thất bại? (brief §40 — câu hỏi nghiên cứu cốt lõi)

### 30.1 Không trả lời bằng "confluence" — tách thành bốn nguồn
| Nguồn | Câu hỏi | Quan sát được? | Proxy ex-ante |
|---|---|---|---|
| **(a) Loại dòng lệnh đã tạo nến 2** | Liquidity shock (tạm thời) / information (nhảy vĩnh viễn) / metaorder (tiếp diễn)? | **Không trực tiếp** | News window, session, sweep trước đó, follow-through nến 3–4, volume (nếu có), cách giá tiếp cận khi retrace |
| **(b) Chế độ drift** | Thị trường đang có trend? | Một phần (qua quá khứ) | Bias D1, tỷ lệ FVG cùng chiều chưa bị lấp, độ dốc MA |
| **(c) Định nghĩa** | Đo "chạy" bằng gì, khung nào, cửa sổ nào? | **Có** — là lựa chọn của bạn | DEF-FVG-02/03/04 |
| **(d) Khớp lệnh** | Lệnh có được khớp, khớp ở giá nào, phân xử stop/target ra sao? | **Có** | Fill rule, spread, độ phân giải |

### 30.2 Biến giải thích vs biến chỉ tương quan
Một biến **giải thích** (explanatory) khi: (1) có cơ chế hợp lý; (2) đo được **trước** quyết định; (3) hiệu ứng **còn lại** sau khi kiểm soát các biến gây nhiễu (khoảng cách, volatility, trend); (4) ổn định ngoài mẫu. Một biến **chỉ tương quan** khi nó là proxy của biến khác hoặc là artefact của cách đo.

| Biến | Cơ chế đề xuất | Biến gây nhiễu có thể | Phép thử |
|---|---|---|---|
| Killzone | Thanh khoản thật, dòng lệnh tổ chức | Volatility cao hơn trong killzone | So FVG killzone vs ngoài killzone **cùng ATR percentile** |
| Sau sweep | Stop làm đối ứng | Sweep thường xảy ra tại cực của range → khoảng cách tới target lớn | Kiểm soát `dist_to_dol_atr` |
| Displacement mạnh | Dòng lệnh "thật" | Nến lớn = FVG lớn = stop xa | Chuẩn hóa theo R; so với đối chứng cùng size |
| HTF aligned | Drift | Bias chỉ đúng ~x% | Phân tích riêng theo bias đúng/sai (ex-post) để tách đóng góp |
| First touch | Lệnh chưa "cạn" | FVG mới = gần giá hơn | Kiểm soát khoảng cách & tuổi |

### 30.3 Toy model: ba loại displacement, cùng một FVG, ba số phận **[TOY MODEL]**

![[FVG-Sim-03-Three-Displacements.png|900]]
*FVG-Sim-03: (A) lúc hình thành, FVG từ ba loại displacement có phân bố kích thước chồng nhau; (B) số phận trong 16 nến khác hẳn nhau; (C) càng nhiều phần "thật" (vĩnh viễn) trong cú đẩy, FVG càng ít bị xuyên.*

![[FVG-Deep-18-Ba-Loai-Displacement.svg|720]]
*FVG-Deep-18: Liquidity shock (hồi lại) · Information (nhảy vĩnh viễn rồi nhiễu) · Metaorder (dòng lệnh còn tiếp) — tóm tắt số liệu toy model.*

Thiết lập: random walk (σ = 1/phút) + cú sốc Poisson (1 lần/600 phút), kích thước U(10, 25) (≈ 1.6–4 ATR nến M15), đẩy trong 6 phút; ba loại xác suất bằng nhau: **liquidity** (tác động tạm thời, phai với τ = 60 phút), **information** (nhảy vĩnh viễn), **metaorder** (nhảy vĩnh viễn + 0.8× kích thước tiếp diễn trong 120 phút). Nến 15 phút. FVG gắn nhãn theo cú sốc bắt đầu trong nến 2.

| Số phận trong 16 nến | Liquidity | Information | Metaorder | Noise-only |
|---|---:|---:|---:|---:|
| Không bao giờ bị chạm | 3% | 22% | **51%** | 20% |
| Chạm, giữ trên CE | 6% | 23% | 25% | 7% |
| Tới CE, chưa full | 9% | 18% | 10% | 6% |
| Full fill, không close xuyên | 4% | 4% | 2% | 7% |
| **Close xuyên distal** | **77%** | 33% | 13% | 60% |
| Size trung vị (ATR) | 1.40 | 1.80 | 1.89 | 0.44 |

Run 2 (liên tục): với phần vĩnh viễn φ ~ U(0, 1), tỷ lệ bị close xuyên giảm từ **76%** (φ ≈ 0.06) xuống **40%** (φ ≈ 0.94); tỷ lệ không bị chạm tăng từ 4% lên 18%.

**Đọc kết quả:** FVG "chạy" hay "fail" phụ thuộc **phần của cú đẩy là thật (vĩnh viễn) và dòng lệnh còn tiếp hay không**. Hai FVG giống nhau về hình có thể đến từ hai thế giới khác nhau. Các tham số là minh họa — mục đích là cơ chế, không phải con số.

### 30.4 Adverse selection — vì sao bộ lọc "đẹp" có thể làm hại **[TOY MODEL]**

Từ FVG-Sim-04 (bước 10 giây; FVG ≥ 0.25 ATR; limit tại CE trong 20 nến; stop distal − 0.1 ATR; target 2R):

| Loại (toy) | Limit CE được khớp | Win khi khớp | p_null | **Excess** |
|---|---:|---:|---:|---:|
| Liquidity | **91%** | 15.3% | 31.3% | **−16.0%** |
| Information | 58% | 27.9% | 31.4% | −3.5% |
| Metaorder | **27%** | 34.3% | 31.3% | +3.0% (SE 2.5%) |
| Noise | 74% | 29.4% | 29.4% | 0.0% |

- Lúc hình thành, các FVG có sự kiện chia ~**31 / 35 / 33%** (liquidity / information / metaorder). Trong các lệnh **được khớp**, tỷ lệ thành **49 / 36 / 16%**.
- Lọc "displacement mạnh" (nến 2 ≥ 2 ATR) tăng tỷ lệ FVG-có-sự-kiện từ **11%** lên **69%** — nhưng vì lệnh limit chủ yếu được khớp ở loại liquidity, excess của FVG lọc là **−7.6%** (SE 0.8%) so với **−1.4%** của vùng đối chứng cùng hình học.

**Bài học cơ chế (không phải số đo thị trường):**
1. **Hiệu quả cần đo có điều kiện theo việc khớp.** "FVG mạnh" lúc hình thành có thể là FVG ít khi cho bạn vào lệnh.
2. **Thứ cần lọc là loại dòng lệnh ở thời điểm KHỚP**, không phải độ đẹp của FVG lúc hình thành. Ứng viên proxy: cách giá tiếp cận (v1 W2: *grind* — trong toy model, tác động tạm thời phai theo hàm mũ chính là một đường "grind" đều đặn về vùng); yêu cầu LTF MSS bên trong FVG trước khi vào (đổi limit thụ động thành vào lệnh có xác nhận); thời gian từ lúc hình thành tới lúc chạm.
3. **Luôn ghi cả setup không được khớp** (`missed_valid_setup`) và kết quả giả định của chúng — so sánh "khớp" vs "không khớp" là cách duy nhất đo adverse selection trên dữ liệu thật (HYP-FVG-016).

### 30.5 Điều kiện thị trường *(v1 §14.4, nguyên văn — có chú thích v2)*

- **Trending vs Ranging:** FVG hình thành trong trend rõ ràng (đặc biệt FVG cùng hướng với chuỗi HH-HL hoặc LH-LL) có tỷ lệ respect cao hơn hẳn FVG hình thành giữa một range hẹp — vì trong range, thanh khoản hai chiều đã tồn tại sẵn quanh khu vực đó, "gap" thường chỉ là nhiễu ngắn hạn dễ bị lấp ngay.
- **Volatility cao vs thấp:** Trong regime volatility cao (VIX cao, ATR giãn), FVG có xu hướng **rộng hơn** nhưng cũng **bị fill sâu hơn** trước khi phản ứng — vì biên độ mỗi nến lớn khiến displacement "quá tay", dealer cần lùi sâu hơn để cân bằng lại risk. Trong volatility thấp, FVG hẹp nhưng phản ứng tại CE "sạch" hơn.
- **Session:** FVG hình thành trong London Open/NY AM (thanh khoản sâu, nhiều thuật toán tham chiến) có chất lượng khác hẳn FVG hình thành trong phiên Á hoặc giờ ăn trưa NY (thanh khoản mỏng — dễ tạo gap "giả" do chỉ một vài lệnh nhỏ cũng đủ đẩy giá qua nhiều mức).
- **Loại tài sản:** độ dày sổ lệnh (order book depth) khác nhau hoàn toàn giữa FX interbank, futures CME và crypto — ảnh hưởng trực tiếp tới tần suất và độ tin cậy của FVG (xem bảng 14.5).

> [!note] Chú thích v2 cho v1 §14.4
> Các claim "trend > range", "volatility cao → fill sâu hơn", "session thanh khoản sâu tốt hơn" là **[HYPOTHESIS]** có cơ chế hợp lý (drift — FVG-Sim-02C; sổ mỏng — §1.2). "Tỷ lệ respect cao hơn hẳn" chưa có số liệu trong vault → bỏ "hẳn" cho tới khi đo.

### 30.6 Hành vi FVG theo loại thị trường *(v1 §14.5, nguyên văn — có chú thích v2)*

| Tiêu chí | FX Majors (EURUSD, GBPUSD) | Index Futures (NQ/ES) | Crypto (BTC/ETH) |
|---|---|---|---|
| **Cấu trúc thanh khoản** | OTC, nhiều venue/dealer khác nhau — không có "một" order book chung; feed có thể lệch nhẹ giữa các broker | Order book tập trung tại CME (Globex) — một nguồn sự thật duy nhất, độ sâu rất lớn tại contract chính | Order book tập trung theo từng sàn (Binance, Coinbase...), nhưng **phân mảnh** giữa nhiều sàn; độ sâu thay đổi mạnh theo giờ |
| **Độ sâu fill điển hình** | Thường fill sâu 60–100% gap trước khi phản ứng (xem mục W4) | Thường fill nông hơn, hay phản ứng ngay tại/trước CE, đặc biệt trong kill zone NY AM | Biến thiên rất lớn theo vốn hóa: BTC/ETH major pairs hành xử gần giống futures; altcoin fill cực sâu hoặc xuyên thẳng do thanh khoản mỏng |
| **Ảnh hưởng tin tức vĩ mô** | Rất mạnh quanh NFP/CPI/lãi suất — FVG sinh trong tin thường là "vết nhảy", không phải dấu vết lệnh thật | Mạnh, nhưng có cơ chế circuit breaker/limit-up-limit-down giúp hạn chế spike cực đoan | Không giới hạn biên độ, không circuit breaker chuẩn hóa — FVG do tin (ETF, SEC, hack sàn) có thể cực đoan và không mean-revert |
| **Thời gian giữ giá trị của HTF FVG** | D1/H4 FVG giữ giá trị nhiều ngày–tuần, thị trường 24/5 liên tục | D1/H4 FVG có thể "nghỉ" qua đêm/cuối tuần (thị trường đóng cửa), tái mở với gap riêng ([[23-New-Day-Opening-Gap]]) | Thị trường 24/7 — FVG không bị gián đoạn bởi giờ đóng cửa, nhưng thanh khoản cuối tuần mỏng làm méo hành vi fill |
| **Vai trò market maker/dealer** | Ngân hàng lớn làm market maker, dealing desk — inventory hedging rất tinh vi, khó quan sát trực tiếp | Market maker HFT đăng ký chính thức tại CME, hành vi khá đồng nhất và có thể suy luận qua Level 2/footprint | Market maker là các quant fund/prop desk crypto-native; hành vi kém đồng nhất hơn, dễ bị thao túng bởi cá voi đơn lẻ trên coin vốn hóa nhỏ |
| **Khuyến nghị thực chiến** | CE là "gợi ý", cho phép fill sâu; đòi LTF MSS nhiều hơn | CE gần như "luật" trong kill zone; ưu tiên Silver Bullet/FPFVG | Chỉ tin FVG trên BTC/ETH khung H4+; tránh trade FVG altcoin thanh khoản thấp bằng size lớn |

> [!warning] Chú thích v2 cho v1 §14.5
> Phần **cấu trúc thị trường** (OTC vs sàn tập trung, circuit breaker, 24/5 vs 24/7, phân mảnh sàn crypto) là **[MARKET MECHANICS]** đúng. Phần **hành vi** ("FX thường fill sâu 60–100%", "NQ phản ứng ngay tại/trước CE", "CE gần như luật trong kill zone") là **số liệu chưa có nguồn** — đánh dấu **[HYPOTHESIS — chưa xác minh]** và thay bằng thống kê `max_depth` theo từng symbol của chính bạn (HYP-FVG-019).

---

## 31. Failure modes (brief §41)

| # | Failure mode | Cơ chế khả dĩ | Đường nền (random walk) | Nhận diện ex-ante | Xử lý |
|---|---|---|---|---|---|
| F1 | **Lấp ngay** (nến 4 đã chạm/full) | Khoảng cách nhỏ; liquidity-type | 43% chạm, 18% full ở nến 4 | Proximal sát close nến 3 (< 0.2 ATR) | Không coi là thất bại; đây là hình học |
| F2 | **Partial fill rồi bị phá** | Grind hấp thụ; liquidity-type | 64% close xuyên trong 20 nến | Cách tiếp cận chậm, đều | Đòi LTF MSS trong vùng; rút limit (v1 W2) |
| F3 | **Xuyên thẳng** (không phản ứng) | Thông tin ngược chiều; sổ mỏng (v1 §14.2 điểm 2) | — | News sắp tới; ngược HTF | Không trade ngược HTF; news filter |
| F4 | **Giữ nhưng không đi xa** | Không có drift; target quá xa | p_null 2R ≈ 1/3 | Range hẹp, R:R tới DOL thấp | Target theo liquidity gần; partial TP |
| F5 | **Phản ứng rồi fail sau đó** | Bias sai; phản ứng chỉ là noise | — | — | Quản trị lệnh: BE theo quy tắc khai báo trước |
| F6 | **Đúng trong hindsight, không giao dịch được real-time** | Chọn FVG sau khi biết; look-ahead | Bug 1: 32% → 65% (Sim-05) | — | Giao thức §21.4 |
| F7 | **Nhiều FVG chồng lấp gây mơ hồ** | Leg dài, nhiều FVG | — | Stacked | Quy tắc chọn cố định (§27.4) |
| F8 | **FVG nhỏ → quá nhiều tín hiệu** | Nhiễu | ~20 FVG ≥ 0.25 ATR / 100 nến | size < 0.25 ATR | min_size + context filter |
| F9 | **FVG lớn → R:R xấu** | Stop xa | — | size > 1.5 ATR | Vào ở LTF FVG bên trong (nested), hoặc bỏ |
| F10 | **Không khớp rồi chạy** (runaway) | Metaorder; trend mạnh | Metaorder: 51% không chạm (toy) | Displacement nhiều nến, trend mạnh | Không chase; chờ FVG con (hình dưới) |

![[FVG-EdgeB-PartialFillRunaway.svg|720]]
*Hình v1 (EdgeB): Partial fill rồi runaway — limit tại CE không khớp; giao thức re-entry không chase.*

> [!note] Nhãn v2
> Giao thức re-entry (không market-order đuổi; chờ FVG con trên leg tiếp diễn; giảm size; nếu không có → No Trade, ghi `missed_valid_setup`) là **[HEURISTIC]** quản trị hành vi tốt — giữ. Câu "fill càng nông = sponsorship càng mạnh → xác suất chạm lại CE giảm mạnh" là **[HYPOTHESIS]** (nhất quán với toy model: metaorder-type ít khi bị chạm sâu).

---

## 32. Khung quyết định thời gian thực (brief §48, project §37)

![[FVG-Deep-16-Cay-Quyet-Dinh-D1-H1-M5.svg|720]]
*FVG-Deep-16: Cây quyết định Q1–Q8. Mỗi nút trả lời được TẠI thời điểm đó; nhánh "không" là kết quả hợp lệ.*

### 32.1 Đánh giá từng nút

| Nút | Câu hỏi | Vì sao cần | Điểm yếu | Cách giảm điểm yếu |
|---|---|---|---|---|
| Q1 | D1 có hypothesis + DOL? | Drift là nguồn lợi thế rõ nhất (Sim-02C) | Bias sai | [[59-Daily-Bias]]: bias là xác suất, ghi confidence |
| Q2 | Giá trong POI HTF, đúng P/D? | Giảm số ứng viên; R:R | POI vẽ sau | known_at cho POI |
| Q3 | Liquidity event tại mức ex-ante? | Câu chuyện stop-as-counterparty | Nhãn đổi theo khung | [[20-Liquidity-Sweep]] DEF-LS |
| Q4 | Displacement + MSS có ý nghĩa? | Hậu quả cấu trúc | MSS vi mô | Swing level ≥ 2 |
| Q5 | FVG ≥ min_size, chọn theo quy tắc? | Location có định nghĩa | Chọn sau khi biết | Quy tắc first-presented |
| Q6 | R:R tới DOL còn đủ? | Expectancy = p·R − (1 − p) | DOL sai | Target theo liquidity gần nhất trước |
| Q7 | Retrace trong W nến? Cách tiếp cận? | Adverse selection (§30.4) | Grind khó đo | `approach_speed` định nghĩa trước |
| Q8 | M5 trigger? | Chuyển từ thụ động sang xác nhận | Lỡ lệnh | Ghi missed |

### 32.2 Điều kiện theo nhóm (project §37)

| Nhóm | Điều kiện (v0.1) |
|---|---|
| **Required** | FVG thỏa DEF-FVG-01 + min_size; known_at = close nến 3; cùng chiều D1 hypothesis (hoặc model countertrend ghi riêng); invalidation & stop xác định trước khi vào |
| **Supporting** | Trong POI HTF đúng P/D; sau liquidity event ex-ante; leg phá swing level ≥ 2; trong killzone; first touch |
| **Optional** | Nested trong HTF FVG; trùng OB (lưu ý đếm trùng); FPFVG |
| **Disqualifying** | News window ±5 phút (không có playbook news); session gap trong 3 nến; FVG đã close xuyên; R:R < kế hoạch; ngược D1 không có playbook |
| **Confirmation** | Reaction ≥ k·ATR sau touch; hoặc M5 MSS bên trong FVG |
| **Invalidation** | Close cùng khung ngoài distal; swing bảo vệ bị phá; hết hạn N nến; DOL đã bị lấy |

### 32.3 INPUT → PROCESS → FILTER → DECISION → EXECUTION → INVALIDATION → OUTPUT
```text
INPUT        OHLC D1/H1/M5 (cùng nguồn, giờ sàn), lịch tin, danh sách mức liquidity có known_at
PROCESS      Phát hiện FVG (DEF-FVG-01) trên mỗi khung; gán thuộc tính (size_atr, c2_range_atr, pd_location, …)
FILTER       Required → Disqualifying → Supporting (đếm FSS, §29.2)
DECISION     Chọn 1 FVG theo quy tắc cố định; đặt kế hoạch: entry (CE / proximal / M5 trigger), stop, target, hạn
EXECUTION    Limit hoặc trigger; ghi fill thực tế (giá, thời gian, spread)
INVALIDATION Close ngoài distal (cùng khung) / hết hạn / context đổi → hủy lệnh chờ
OUTPUT       Journal: mọi trường §41.5, kể cả setup không khớp / bị loại và lý do
```

---

## 33. Ví dụ, case studies, war stories và edge cases

### 33.1 Bối cảnh sử dụng *(v1 §2, nguyên văn)*

![[FVG-Sec-02-Boi-Canh.svg|720]]
*Sơ đồ: Khi nào FVG có giá trị cao (đồng hướng bias, ở discount/premium, sau sweep) và khi nào nên bỏ qua.*

#### Các loại / trạng thái của FVG

| Loại | Thuật ngữ ICT | Cấu trúc | Ý nghĩa thực chiến |
|---|---|---|---|
| **Bullish FVG** | BISI (Buyside Imbalance Sellside Inefficiency) | Gap giữa high nến 1 và low nến 3, nến 2 displacement tăng | Vùng discount để tìm Long khi giá retrace về; hỗ trợ |
| **Bearish FVG** | SIBI (Sellside Imbalance Buyside Inefficiency) | Gap giữa low nến 1 và high nến 3, nến 2 displacement giảm | Vùng premium để tìm Short khi giá retrace về; kháng cự |
| **Inversion FVG (IFVG)** | — | FVG bị đóng nến xuyên qua → đảo cực tính | Bullish FVG fail → thành kháng cự bearish; và ngược lại |
| **Liquidity Void / lớn** | — | Vùng imbalance rất rộng do displacement cực mạnh | Draw mạnh; giá thường rebalance phần lớn void |

> [!tip]
> FVG đóng **hai vai trò** và bạn phải biết mình đang dùng vai nào: (1) **POI để entry** khi giá retrace về; (2) **DRAW / target** khi có một FVG còn mở ở phía xa mà giá bị hút về để rebalance. Cùng một imbalance có thể là entry trên LTF và là target trên HTF.

#### Khi nào khái niệm này có giá trị cao?
- [ ] FVG sinh ra từ **displacement phá cấu trúc** (BOS/MSS), không phải gap giữa range.
- [ ] FVG nằm tại **POI HTF** (D1/H4/H1 FVG hoặc OB) đồng hướng bias.
- [ ] FVG nằm đúng **premium** (cho Short) hoặc **discount** (cho Long) của dealing range.
- [ ] FVG xuất hiện **sau liquidity sweep** đúng thứ tự (sweep → displacement → FVG).
- [ ] FVG còn **unmitigated** (chưa bị lấp / chưa bị xuyên CE).
- [ ] CE (50%) của FVG trùng với một mức tham chiếu khác (OB, equilibrium, OTE).
- [ ] Có liquidity rõ ràng phía bên kia để làm target sau khi entry tại FVG.

#### Khi nào nên bỏ qua?
- [ ] FVG nhỏ, không có displacement rõ, nằm giữa range / quanh equilibrium.
- [ ] FVG ngược Daily Bias mà không có counter-trend playbook riêng.
- [ ] FVG đã bị lấp toàn bộ hoặc bị đóng nến xuyên qua (đã mitigate / invalid).
- [ ] FVG ở sai phía premium/discount (Long ở FVG premium, Short ở FVG discount).
- [ ] FVG xuất hiện trước khi liquidity bị sweep — entry sẽ thành mồi cho sweep.
- [ ] Có hàng loạt FVG chồng chéo, không xác định được cái nào có ý nghĩa.
- [ ] FVG ngoài kill zone / ngoài kế hoạch session.

> [!note] Chú thích v2 cho v1 §2
> - Tip "FVG đóng hai vai trò — POI để entry và DRAW/target" — **đúng và quan trọng**; v2 mở rộng thành bốn vai trò so với DOL (§26.1).
> - Hàng "Liquidity Void / lớn — Draw mạnh; giá thường rebalance phần lớn void" → **[HYPOTHESIS]**; phần "thường" có đường nền hình học (§15).
> - Hai checklist "Khi nào có giá trị cao / Khi nào nên bỏ qua" là **bộ lọc context** — giữ làm checklist thực hành; mỗi dòng là một biến trong §29.1.

### 33.2 Cấu trúc nhận diện trên chart *(v1 §3, nguyên văn)*

![[FVG-Sec-03-Nhan-Dien.svg|720]]
*Sơ đồ: Quy trình nhận diện một FVG hợp lệ trên chart — displacement, gap chưa được lấp, xác định CE.*

#### Dấu hiệu chính
1. **Ba nến:** xác định nến 1, nến 2 (displacement), nến 3. Gap = vùng giữa nến 1 và nến 3, KHÔNG bị thân/bóng nến 2 lấp kín.
2. **Nến giữa là displacement:** nến 2 có body lớn, đóng quyết đoán, thể hiện urgency và single-sided delivery.
3. **Khoảng trống còn thật:** với bullish FVG, low của nến 3 phải nằm CAO hơn high của nến 1; nếu chồng lấp thì không có FVG hợp lệ.
4. **CE 50%:** đánh dấu mức giữa của gap — đây là mức phản ứng quan trọng nhất.
5. **Context phá cấu trúc:** displacement tạo FVG có đi kèm BOS/MSS không? Đó là yếu tố phân biệt FVG chất lượng với gap ngẫu nhiên.

#### Ma trận nhận diện FVG

| Thành phần | Bullish FVG (BISI) | Bearish FVG (SIBI) | Cảnh báo / FVG yếu |
|---|---|---|---|
| **Khoảng gap** | High nến 1 < Low nến 3 | Low nến 1 > High nến 3 | Nến 1 và 3 chồng lấp; gap quá nhỏ |
| **Nến giữa** | Displacement tăng, body lớn, đóng mạnh | Displacement giảm, body lớn, đóng mạnh | Nến 2 doji/body nhỏ, không urgency |
| **Cấu trúc** | Displacement phá swing high → BOS/MSS bullish | Displacement phá swing low → BOS/MSS bearish | Không phá cấu trúc, chỉ dao động nội bộ |
| **Location** | Ở discount của dealing range | Ở premium của dealing range | Quanh equilibrium / sai phía |
| **Liquidity** | Sau sweep SSL → repricing lên | Sau sweep BSL → repricing xuống | Chưa sweep; hoặc đã lấy target rồi |
| **Trạng thái** | Còn unmitigated, CE chưa bị xuyên | Còn unmitigated, CE chưa bị xuyên | Đã lấp toàn bộ / đóng nến xuyên qua |

#### Điều kiện bắt buộc
- [ ] Xác định đúng 3 nến và khoảng gap thật (không bị lấp kín).
- [ ] Nến giữa là displacement có body rõ, không phải nến nhỏ ngẫu nhiên.
- [ ] Xác định được mức CE (50%) của FVG.
- [ ] Xác định FVG đang ở premium hay discount của dealing range phù hợp.
- [ ] Xác định trạng thái: unmitigated / partially filled / fully filled / inverted.

#### Điều kiện tăng xác suất
- [ ] Displacement tạo FVG đồng thời tạo BOS/MSS có ý nghĩa.
- [ ] FVG nằm bên trong hoặc trùng một POI HTF lớn hơn (HTF FVG, OB).
- [ ] FVG xuất hiện ngay sau một liquidity sweep đúng hướng narrative.
- [ ] FVG đúng phía premium/discount cho hướng trade.
- [ ] CE của FVG trùng với equilibrium / OTE / OB → confluence.
- [ ] Còn liquidity rõ ràng (external/internal) làm target sau entry.
- [ ] FVG nằm trong kill zone phù hợp với plan session.

#### Điều kiện làm setup yếu đi
- FVG sinh ra từ nến giữa body nhỏ, không có urgency / không phá cấu trúc.
- FVG nằm giữa range hoặc sai phía premium/discount.
- FVG đã bị giá test nhiều lần, mỗi lần ăn mòn dần (giảm chất lượng).
- FVG xuất hiện sau một expansion lớn đã chạy xa — entry trở thành chase.
- Nhiều FVG chồng chéo gần nhau khiến không có mức tham chiếu rõ.
- FVG ngược Daily Bias mà không có bằng chứng đảo HTF.

> [!note] Chú thích v2 cho v1 §3
> "Nến giữa là displacement" được v1 đặt trong **Dấu hiệu chính** và **Điều kiện bắt buộc**. v2 tách: DEF-FVG-01 *không* đòi displacement; displacement là **biến** (`c2_range_atr`) và là điều kiện **lọc** (S1 của FSS). Lý do: nếu displacement nằm trong định nghĩa, không còn kiểm định được nó có đóng góp thông tin không (HYP-FVG-001). Trong thực hành, checklist của v1 vẫn dùng được nguyên vẹn.

### 33.3 Ví dụ chart và sequence mẫu *(v1 §6, nguyên văn)*

#### Ví dụ đúng — Bullish FVG tại discount POI, Long theo ICT 2022 Model
![[FVG-Example-Correct.png]]

**Mô tả:**  
D1/H4 bullish, draw on liquidity là BSL phía trên. Giá retrace vào discount, sweep sell-side liquidity dưới một đáy ngắn hạn trong kill zone. Ngay sau sweep, một nến displacement tăng mạnh phá swing high nội bộ (MSS bullish) và để lại một bullish FVG (BISI). Giá retrace về **CE (50%)** của FVG, reject, M5 tạo bullish MSS nhỏ. Entry quanh CE; stop dưới low FVG / dưới sweep low; TP hướng về BSL.

**Vì sao đây là ví dụ tốt:**
- FVG sinh ra từ displacement **phá cấu trúc**, không phải gap ngẫu nhiên.
- FVG ở **discount** và đồng hướng Daily Bias bullish.
- Liquidity sweep xảy ra **trước** displacement và FVG.
- Entry quanh **CE** cải thiện R:R; giá respect CE thay vì xuyên thủng.
- Target là liquidity rõ (BSL), không phải TP tùy ý.

#### Ví dụ sai / dễ nhầm — Long mọi bullish FVG giữa range
![[FVG-Example-Wrong.png]]

**Mô tả lỗi:**  
D1 bearish, giá đang ở premium / gần equilibrium. Trader thấy một bullish FVG nhỏ (nến giữa body trung bình, không phá cấu trúc rõ) và Long ngay vì "có FVG". Giá lấp FVG, đóng nến xuyên xuống (FVG invalid → chuyển thành bearish IFVG), rồi tiếp tục delivery xuống lấy SSL. Lệnh Long bị stop.

**Mô tả lỗi:**
- FVG không sinh ra từ displacement phá cấu trúc.
- FVG ngược Daily Bias và ở sai phía (premium) cho Long.
- Không có liquidity sweep trước đó; chưa chờ LTF confirmation.
- Trade FVG như tín hiệu độc lập thay vì điểm tham chiếu trong context.

**Bài học:**
- FVG là **điểm tham chiếu giá**, không phải tín hiệu trade độc lập.
- Không Long chỉ vì thấy bullish FVG; phải đúng bias + discount + sweep + displacement.
- Khi FVG bị đóng nến xuyên qua, nó **đảo cực (IFVG)** — đừng cố giữ lệnh ngược.

---
#### Sequence mẫu — Long với Bullish FVG (BISI)
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Giá về Discount + bullish HTF POI
→ Sweep Sell-Side Liquidity
→ Displacement tăng phá cấu trúc (BOS/MSS) → tạo Bullish FVG (BISI)
→ Giá retrace về CE (50%) của FVG
→ M5/M1 bullish MSS + FVG nhỏ refined
→ Entry quanh CE; Stop dưới low FVG / dưới sweep low
→ Target: Internal liquidity trước, External BSL chính sau
```

#### Sequence mẫu — Short với Bearish FVG (SIBI)
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Giá về Premium + bearish HTF POI
→ Sweep Buy-Side Liquidity
→ Displacement giảm phá cấu trúc (BOS/MSS) → tạo Bearish FVG (SIBI)
→ Giá retrace lên CE (50%) của FVG
→ M5/M1 bearish MSS + FVG nhỏ refined
→ Entry quanh CE; Stop trên high FVG / trên sweep high
→ Target: Internal liquidity trước, External SSL chính sau
```

#### Sequence mẫu — Inversion FVG (IFVG)
```text
Bullish FVG cũ bị đóng nến XUYÊN XUỐNG (invalid)
→ Vùng FVG cũ đảo cực thành KHÁNG CỰ (bearish IFVG)
→ Đồng hướng bias bearish mới + MSS bearish
→ Giá retrace LÊN test lại vùng IFVG
→ Reject tại IFVG → Short
→ Stop trên đỉnh IFVG; Target SSL phía dưới
(Ngược lại cho bullish IFVG: bearish FVG fail → hỗ trợ → Long)
```

> [!note]
> Với ICT 2022 model, FVG có chất lượng không đến từ "thấy gap rồi vào", mà từ sequence: **HTF draw → retrace vào PD Array → liquidity sweep → displacement phá cấu trúc tạo FVG → entry quanh CE**. CE là điểm vào tối ưu giúp R:R đẹp hơn so với vào ở mép gap.

> [!note] Chú thích v2 cho v1 §6
> Hai ảnh ví dụ là **minh họa giáo khoa** (không có symbol/ngày cụ thể). "Ví dụ đúng" mô tả kịch bản 2022 Model; theo v2, điểm duy nhất cần bổ sung là *ghi known_at và quy tắc chọn FVG* để ví dụ có thể lặp lại. "Ví dụ sai" là minh họa tốt cho failure mode F3/F8 (§31). Các sequence mẫu giữ nguyên làm template.

### 33.4 Hai case tái dựng T0 → T5 *(giả định — không phải trade thật, không phải dữ liệu thật)*

> [!info] Vì sao có case giả định
> Brief (project §24) yêu cầu tái dựng theo thời gian để tránh hindsight. Không có dữ liệu thật trong phiên này, nên hai case dưới đây dùng **số giả định** — mục đích là luyện *cách suy nghĩ tại từng thời điểm*, không phải chứng minh setup có lợi.

#### Case H-1 — EURUSD: FVG "đúng sách", hai tương lai có thể (giả định)

| T | Thông tin có tại thời điểm đó | Quyết định hợp lệ |
|---|---|---|
| **T0** (trước London) | D1 bias bullish (confidence trung bình), giá ở discount của range D1; Asia low 1.0745 là mức ex-ante; không có tin trước 13:30 | Chuẩn bị: POI = discount D1; kịch bản = sweep Asia low → displacement |
| **T1** (08:10) | Nến M15 xuyên 1.0745 tới 1.0738, đóng 1.0749 (rejection tạm — PENDING theo [[20-Liquidity-Sweep]]) | Chưa làm gì |
| **T2** (08:45) | Hai nến M15 tăng mạnh (c2 range 2.3 ATR); phá swing high M15 1.0762 (level 2). Tại close nến 3: **bullish FVG M15 [1.0752, 1.0761]**, size 0.6 ATR, CE 1.07565, `fvg_pos_in_leg` 0.45 | FVG known_at = close nến 3. Kế hoạch: limit CE, stop 1.0748, target BSL 1.0820 (R:R ≈ 7) — hết hạn 48 nến |
| **T3** (10:30) | Giá retrace. **Nhánh A (fast tap):** 3 nến M5 rơi nhanh vào 1.0757, bật ngay. **Nhánh B (grind):** 9 nến M5 nhỏ bậc thang gặm từ 1.0761 xuống 1.0755 | Nhánh A: limit khớp theo kế hoạch. Nhánh B: theo HEURISTIC v1 W2 → rút limit, chờ M5 MSS bên trong FVG |
| **T4** | Nhánh A: giá rời proximal ≥ 1 ATR trong 6 nến (REACTED). Nhánh B: không có M5 MSS; nến M15 đóng 1.0747 < distal (INVALIDATED) | Ghi trạng thái + known_at |
| **T5** (ex-post) | A: TP1 tại internal liquidity. B: không vào lệnh — ghi `skipped_reason = grind_no_mss` và *kết quả giả định nếu đã vào* (thua 1R) | Cả hai đều là **dữ liệu**: B đóng góp vào HYP-FVG-015 |

**Bài học:** tại T2, hai nhánh không phân biệt được. Thông tin phân biệt (cách tiếp cận) chỉ xuất hiện ở T3 — và đó là lúc quyết định có nên để limit thụ động hay không. Đây là phiên bản thực hành của adverse selection (§30.4).

#### Case H-2 — NQ: FVG bị lấp ngay mà setup vẫn đúng (giả định)

| T | Thông tin | Quyết định |
|---|---|---|
| **T0** | D1 bearish; giá ở premium; PDH là mức ex-ante | POI = premium; chờ sweep PDH |
| **T1** (09:50 NY) | Nến M5 quét PDH 6 điểm, đóng lại dưới | PENDING |
| **T2** (10:05) | Displacement giảm (c2 range 2.1 ATR), phá swing low M5; **bearish FVG M5** size 0.3 ATR; proximal chỉ cách close nến 3 0.1 ATR | FVG known. Theo §13.3: chạm trong 1–3 nến là **gần như chắc chắn** (hình học) |
| **T3** (10:10) | Nến 4 chạm proximal và CE ngay, full fill ở nến 5 nhưng **không** close xuyên distal | Theo DEF-FVG-03: vẫn ACTIVE. Limit CE đã khớp ở nến 4 |
| **T4** | Nến 6–8 giảm mạnh, REACTED | — |
| **T5** | Lệnh thắng | Ghi `bars_to_touch = 1`, `max_depth = 1.0` |

**Bài học:** "FVG bị lấp ngay / full fill" không phải thất bại theo định nghĩa (F1). Người dùng định nghĩa invalidation I4 ("full traversal") sẽ bỏ lệnh này; người dùng I2 thì không. Chọn định nghĩa **trước**, không sau kết quả.

### 33.5 Tình huống thực chiến — War Stories *(v1, nguyên văn — có nhãn v2)*

> [!info] Vì sao có mục này
> Checklist ở mục 8 lọc FVG *xấu*. Mục này dành cho những FVG **pass toàn bộ checklist** nhưng vẫn thất bại — vì các biến mà lý thuyết chuẩn không đặt tên: chất liệu của nến tạo gap, tốc độ giá tiếp cận gap, lịch sử chạm ngoài phiên của mình, và microstructure của chính công cụ đang trade.

> [!note] Tầng WHY nền tảng W0 của v1 đã được chuyển lên §9.6 (kèm rà soát).

#### W1. FVG sinh từ news candle — cùng hình dạng, khác hẳn "chất liệu"

![[FVG-War-News-Candle-FVG.svg|720]]
*Sơ đồ: FVG từ displacement có cấu trúc được respect tại CE; FVG từ spike CPI/NFP là vùng chân không — giá cắt xuyên không phản ứng.*

**Sách giáo khoa nói:** gap 3 nến + nến giữa displacement = FVG hợp lệ.

**Thực tế phát hiện:** nến 8:30 CPI/NFP thỏa mọi tiêu chí hình học — body khổng lồ, phá cấu trúc, gap rộng. Nhưng gap đó in ra trong lúc **spread giãn và quote gần như đóng băng**: không có chuỗi lệnh thuật toán thật sự được khớp tại các mức giá bên trong gap. Nó là *vết nhảy* của giá, không phải *dấu vết* của lệnh. Hệ quả: không ai có position cần phòng thủ tại CE của nó → khi giá quay lại, vùng này bị cắt xuyên với tần suất cao hơn hẳn FVG cùng kích thước sinh trong kill zone không có tin.

**Rule đo được:**
- FVG sinh trong ±2 phút quanh high-impact news → gắn nhãn riêng, **mặc định không dùng làm POI entry**.
- Nó chỉ "tốt nghiệp" thành POI khi giá **re-deliver** qua vùng đó lần nữa bằng displacement có cấu trúc (sweep đứng trước, không có tin) — lúc đó vẽ lại theo leg mới.
- Journal: `fvg_origin` (killzone_algo / news_spike / thin_liquidity). Sau 30 mẫu, so respect-rate tại CE giữa các nhóm — chênh lệch thường đủ lớn để tự nó thành rule.

#### W2. Tốc độ tiếp cận FVG — "rơi nhanh chạm bật" vs "bò từ từ vào"

![[FVG-War-Approach-Speed.svg|720]]
*Sơ đồ: fast tap (rebalance chuẩn — giữ plan) vs slow grind bậc thang (hấp thụ — rút limit, đòi LTF MSS).*

**Sách giáo khoa nói:** chờ giá retrace về CE rồi entry.

**Thực tế phát hiện sau nhiều lần bị xuyên limit:** *cách* giá đi vào FVG dự báo kết quả tốt hơn cả chất lượng của chính FVG. Hai chế độ:
- **Fast tap:** 2–4 nến dốc rơi thẳng vào gap, chạm CE, bật ra trong 1–2 nến. Đây là hành vi rebalance — thuật toán quay lại "lấy nốt hàng" ở giá tốt rồi tiếp tục. Limit tại CE hoạt động đúng thiết kế.
- **Slow grind:** chuỗi nến nhỏ bậc thang gặm dần vào gap, mỗi nến một chút, không có nỗ lực đẩy ra. Đây là hành vi **hấp thụ**: lệnh nằm trong gap đang bị tiêu hoá dần bởi một dòng lệnh kiên nhẫn ngược hướng. Khi giá tới CE thì phòng tuyến đã mỏng — xuyên thủng là kết cục phổ biến.

**Rule đo được:**
- Giá tiếp cận FVG bằng grind (nhiều hơn ~5–6 nến LTF liên tiếp cùng hướng, body nhỏ, không có displacement ngược nào xen giữa) → **rút limit order**, chuyển sang chế độ "chỉ vào nếu có LTF MSS trong gap".
- Journal: `approach_speed` (fast_tap / grind) — biến này kết hợp với `entry_relative_to_ce` là cặp thống kê giá trị nhất về FVG.

#### W3. "First touch" giả — cú chạm thật đã xảy ra ngoài phiên của bạn

**Tình huống:** bạn đánh dấu một H1 FVG chưa mitigate từ hôm qua, sáng nay giá quay về, bạn coi là first touch (đáng tin nhất). Lệnh fail. Mở M5 xem lại: **lúc 3 giờ sáng giờ mình ngủ**, giá đã wick vào gap một lần trong phiên Á thanh khoản mỏng. Trên H1 wick đó gần như vô hình (nằm trong bóng một nến dài), nhưng phần lệnh trong gap đã bị tiêu thụ một phần — cú chạm của bạn thực chất là **lần chạm thứ hai**.

**Rule đo được:**
- Trước khi tin một "first touch": thả xuống M5/M15 và **tua lại toàn bộ lịch sử giá từ lúc FVG hình thành** — đếm số lần wick đã vào gap, kể cả ngoài phiên. Mất 60 giây, cứu nhiều lệnh.
- Journal: `touch_count_actual` (đếm trên LTF, không phải trên khung đang trade).

#### W4. CE là "luật" trên NQ nhưng chỉ là "gợi ý" trên EURUSD — hiệu chỉnh theo từng công cụ

**Tình huống:** cùng một playbook FVG, backtest trên NQ cho thấy giá respect CE rất sạch (chạm 50%, bật); mang nguyên sang EURUSD thì liên tục "thua oan" — giá thường xuyên fill sâu 75–100% gap, thậm chí wick qua distal vài pip rồi mới đảo. Không phải model sai — **độ sâu fill điển hình là thuộc tính riêng của từng thị trường** (độ dày thanh khoản, tick size, mức độ tham gia của thuật toán CME vs interbank khác nhau).

**Rule đo được:**
- Không dùng chung một quy tắc entry-depth cho mọi market. Thống kê `fill_depth` **theo từng symbol** trong backtest (NQ riêng, EURUSD riêng, XAUUSD riêng) rồi mới đặt rule entry/stop cho từng cái.
- Với market hay fill sâu: entry mặc định dời từ CE xuống lower quadrant, hoặc luôn đòi LTF MSS; stop buffer sau distal cũng phải rộng hơn (đặc biệt XAUUSD).
- Đây là ứng dụng trực tiếp của nguyên tắc trong thư mục `04 - Backtesting/`: dữ liệu của chính mình trên chính market đó là trọng tài, không phải video ICT quay trên ES.

#### W5. Limit tại mép FVG không khớp — vì chart của bạn là bid-chart

**Tình huống (FX/CFD):** bạn đặt sell limit tại proximal edge của một bearish FVG trên EURUSD/XAUUSD. Giá "chạm đúng mép" trên chart rồi rơi thẳng — nhưng lệnh không khớp, hoặc khớp trong backtest mà không bao giờ khớp live. Lý do: **chart vẽ giá bid**, trong khi sell limit khớp theo bid nhưng cú chạm bạn thấy có thể chỉ là ask chạm (hoặc ngược lại với buy limit — ask đã chạm mức từ trước khi chart hiển thị). Trên gold spread 20–40 cent, sai số này nuốt trọn những cú "chạm mép rồi bay".

**Rule đo được:**
- Entry mặc định tại **CE thay vì mép** — vừa cải thiện R:R vừa tạo buffer tự nhiên cho spread.
- Nếu vẫn muốn mép: cộng/trừ spread trung bình của phiên vào giá limit (buy limit đặt cao hơn mép một spread; sell limit thấp hơn một spread).
- Backtest phải mô phỏng spread — mọi entry "khớp đúng đỉnh wick chạm mép" cần bị nghi ngờ là phantom fill (cùng họ với bài học W3 bên [[20-Liquidity-Sweep]]).

> [!success] Tổng kết mục War Stories
> Một FVG không chỉ có *hình dạng* — nó có **chất liệu** (nến gì tạo ra nó — W1), **cách bị tiếp cận** (W2), **lịch sử chạm thật** (W3), **quốc tịch** (market nào — W4) và **cơ chế khớp lệnh** quanh nó (W5). Journal fields: `fvg_origin`, `approach_speed`, `touch_count_actual`, `fill_depth` theo symbol.

> [!note] Nhãn v2 cho War Stories W1–W5
> | War story | Phần giữ nguyên | Nhãn v2 |
> |---|---|---|
> | W1 — FVG từ news candle | Gắn nhãn `fvg_origin`, mặc định không dùng news-FVG làm POI | Cơ chế "quote đóng băng → không có lệnh thật trong gap" **[MARKET MECHANICS]** hợp lý cho spike; "bị cắt xuyên với tần suất cao hơn hẳn" **[HYPOTHESIS]** — HYP-FVG-017. Câu "không có ai có position cần phòng thủ tại CE" dựa trên lập luận W0 đã rà soát (§9.6) |
> | W2 — fast tap vs grind | Biến `approach_speed`, rút limit khi grind | **[HYPOTHESIS]** — HYP-FVG-015; toy model cho một cơ chế ủng hộ (phai tác động tạm thời = grind đều) — §30.4. Ngưỡng "5–6 nến" là **HEURISTIC** |
> | W3 — first touch giả | Đếm `touch_count_actual` trên LTF | **[HEURISTIC]** tốt về đo lường; "lệnh trong gap bị tiêu thụ một phần" là **[INTERPRETATION]** |
> | W4 — CE theo từng công cụ | Thống kê `fill_depth` theo symbol | **Đúng phương pháp**; các mô tả "NQ respect CE sạch", "EURUSD fill sâu 75–100%" là **chưa xác minh** — HYP-FVG-019 |
> | W5 — bid chart & limit | Entry tại CE thay vì mép; mô phỏng spread | **[MARKET MECHANICS]** đúng (chart bid, buy limit khớp theo ask); khớp với lỗi fill ở §21.3 |

### 33.6 Edge cases thực chiến *(v1 §16, nguyên văn — có nhãn v2)*

![[FVG-Edge-Cases.svg|720]]
*Sơ đồ: Hai edge case đắt giá nhất — feed lệch giữa CFD broker và CME futures tạo FVG "ảo"; và nến rollover 00:00 server time tạo gap giả trên M1-M5.*

#### EC1. FVG "chỉ có" trên feed CFD broker, không có trên CME futures

**Tình huống:** trade NQ qua CFD broker (giá tham chiếu từ một liquidity provider tổng hợp), thấy một bullish FVG rõ trên M5. Vào lệnh theo đúng sách. Đối chiếu lại với dữ liệu CME Globex thật (qua TradingView futures NQ1! hoặc Sierra Chart), FVG đó **không tồn tại** — vì nguồn giá CFD có một cú spike nhỏ (do aggregation từ nhiều LP, hoặc do broker đó có spread/liquidity riêng) mà CME không có.

**Vì sao bẫy được cả trader có kinh nghiệm:** hầu hết trader dùng nền tảng phổ biến (MT4/MT5 broker CFD) không nhận ra rằng feed của họ **không phải** là feed CME gốc — nó là một bản tổng hợp/derivative giá. Với các broker uy tín thấp, những cú spike/wick giả (đặc biệt cuối phiên thanh khoản mỏng) khá phổ biến và đôi khi tạo ra đúng hình dạng của một FVG "đẹp".

**Cách nhận diện sớm:** nếu FVG hình thành trong khung giờ thanh khoản mỏng (rollover, tin tức, cuối phiên NY) và trông "quá đẹp" so với context, đối chiếu nhanh với một nguồn feed futures gốc (barchart.com, CME DataMine, hoặc broker ECN uy tín) trước khi tin.

**Cách xử lý:** với NQ/ES, ưu tiên nạp dữ liệu từ nguồn futures gốc thay vì CFD tổng hợp nếu có thể; nếu bắt buộc dùng CFD, chỉ tin các FVG hình thành trong kill zone thanh khoản sâu (London/NY overlap, NY AM) và bỏ qua FVG hình thành quanh 00:00–02:00 giờ server hoặc weekend gap.

#### EC2. Nến rollover 00:00 server time tạo gap giả trên M1-M5

**Tình huống:** phần lớn broker MT4/MT5 reset "ngày nến" theo giờ server (thường GMT+2/+3), không phải theo NY midnight. Tại đúng thời điểm rollover, nhiều broker cộng thêm swap/rollover fee vào giá hoặc trải qua một khoảnh khắc spread giãn đột ngột — tạo ra một "nến" M1 có wick bất thường, đôi khi đủ để hình thành một FVG 3 nến trên M1/M5 không phản ánh giao dịch thật.

**Vì sao bẫy được cả trader có kinh nghiệm:** vì nó xảy ra đều đặn mỗi ngày, một số trader vô tình "học" nhầm rằng đây là một loại setup có quy luật (ví dụ ngộ nhận là "silver bullet" tự nhiên), trong khi thực chất là nhiễu cơ chế broker.

**Cách nhận diện sớm:** kiểm tra giờ server của broker so với giờ NY; đánh dấu khung 00:00±5 phút giờ server như "vùng nghi ngờ", đặc biệt trên EURUSD/GBPUSD.

**Cách xử lý:** loại trừ FVG hình thành trong cửa sổ rollover khỏi danh sách POI; nếu muốn kiểm tra, so sánh cùng thời điểm đó trên biểu đồ từ 2-3 broker khác nhau — nếu chỉ một broker có gap, đó là nhiễu feed, không phải FVG thật.

#### EC3. FVG hình thành trong nến tin (CPI/NFP/FOMC) — slippage khi entry, stop bị nhảy qua

**Tình huống:** một nến tin tạo displacement khổng lồ để lại FVG rất rộng, trông như cơ hội R:R tuyệt vời. Đặt limit order tại CE, chờ giá retrace. Giá có retrace về đúng vùng — nhưng do biến động tin còn dư âm, spread giãn 5-10x bình thường và thanh khoản mỏng, lệnh khớp với slippage lớn, hoặc tệ hơn: giá **gap through** (nhảy qua) mức stop loss mà không khớp đúng giá, gây lỗ vượt xa kế hoạch.

**Vì sao bẫy được cả trader có kinh nghiệm:** FVG tin trông "hợp lệ về hình học" (đủ 3 nến, đủ displacement, đủ phá cấu trúc) — checklist kỹ thuật thuần túy không phân biệt được nguồn gốc của displacement.

**Cách nhận diện sớm:** gắn nhãn `fvg_origin: news_spike` ngay khi thấy FVG hình thành trong ±2-5 phút quanh lịch kinh tế high-impact.

**Cách xử lý:** mặc định không dùng FVG tin làm POI entry cho tới khi giá re-deliver qua vùng đó bằng một displacement mới, sạch, không tin tức; nếu bắt buộc trade quanh tin, luôn dùng lệnh market thay vì limit tại mép chính xác, và giảm size để bù rủi ro slippage.

#### EC4. DST (giờ mùa hè/đông) làm lệch kill zone và giờ hình thành FVG "đúng ngữ cảnh"

**Tình huống:** playbook cá nhân ghi "FVG chất lượng cao nhất hình thành 9:30-10:00 NY time". Vào cuối tháng 3 và đầu tháng 11, khi Mỹ và châu Âu chuyển đổi DST **không cùng ngày** (thường lệch 1-2 tuần), khung giờ NY 9:30 theo giờ địa phương của trader (nếu trader ở châu Á/châu Âu) bị dịch chuyển 1 tiếng so với thói quen — dẫn tới trader canh sai giờ, bỏ lỡ hoặc vào nhầm khung đúng giờ nến tin/kill zone thật.

**Vì sao bẫy được cả trader có kinh nghiệm:** vì độ lệch chỉ là 1 tiếng và chỉ xảy ra 2 lần/năm trong giai đoạn ngắn, nhiều trader quên cập nhật lại giờ trên nền tảng phân tích, dẫn tới nhận diện sai FVG "trong kill zone" khi thực ra nó hình thành lệch giờ.

**Cách nhận diện sớm:** luôn kiểm tra lịch DST của Mỹ (thường Chủ Nhật thứ 2 tháng 3 và Chủ Nhật đầu tháng 11) và EU (Chủ Nhật cuối tháng 3 và cuối tháng 10) — hai lịch KHÔNG trùng nhau.

**Cách xử lý:** dùng đồng hồ hiển thị giờ NY tuyệt đối (không phải giờ tương đối theo múi giờ cá nhân) trên nền tảng chart trong 2 tuần giao thời DST mỗi năm.

#### EC5. Tuần đáo hạn quyền chọn/rollover hợp đồng futures — FVG hình thành do cơ học hợp đồng, không phải orderflow tự nhiên

**Tình huống:** vào tuần thứ Sáu thứ 3 của tháng (options expiration) hoặc ngày rollover hợp đồng futures quý (ví dụ NQ chuyển từ hợp đồng tháng 3 sang tháng 6), khối lượng giao dịch dồn vào việc đóng/mở vị thế hợp đồng, đôi khi tạo displacement không phản ánh ý định định hướng thị trường thực sự, mà chỉ là cơ học tái cân bằng vị thế (gamma hedging, roll spread).

**Vì sao bẫy được cả trader có kinh nghiệm:** displacement trong các phiên này có thể rất mạnh về hình dạng nến, dễ nhầm với FVG "chất lượng cao" thông thường.

**Cách nhận diện sớm:** kiểm tra lịch đáo hạn quyền chọn hàng tháng (thường thứ Sáu thứ 3) và lịch rollover futures quý (khoảng 8 ngày trước ngày đáo hạn hợp đồng, tùy sàn) trước khi tin tưởng FVG hình thành trong các phiên này.

**Cách xử lý:** giảm trọng số tin tưởng cho FVG hình thành trong tuần đáo hạn/rollover; nếu vẫn trade, đòi hỏi thêm xác nhận LTF mạnh hơn bình thường và giảm size.

#### EC6. HTF đúng nhưng LTF entry fail liên tục — fractal conflict giữa nhiều tầng FVG

**Tình huống:** D1 bias bullish rõ ràng, giá đang ở discount HTF. Nhưng trên M5, mỗi lần retrace vào một FVG nhỏ để tìm Long entry, giá lại xuyên qua và tạo IFVG, khiến liên tiếp 3-4 lệnh Long M5 bị stop trước khi cú tăng HTF thực sự diễn ra.

**Vì sao bẫy được cả trader có kinh nghiệm:** HTF bias đúng không đảm bảo mọi LTF FVG đều là entry tốt — thị trường có thể trải qua nhiều đợt "shake out" ở LTF (tạo FVG giả, quét stop) trước khi thực sự di chuyển theo hướng HTF. Đây là **fractal conflict**: cấu trúc M5 đang trong pha điều chỉnh/tích lũy trong khi D1 đang trong pha xu hướng.

**Cách nhận diện sớm:** nếu 2 lệnh LTF FVG liên tiếp thất bại theo cùng kiểu (bị xuyên rồi tiếp tục đi ngược), đó là dấu hiệu tầng LTF chưa đồng bộ với HTF — cần lùi lên khung cao hơn (H1 thay vì M5) để tìm FVG có ý nghĩa hơn, thay vì tiếp tục "chase" trên M5.

**Cách xử lý:** áp dụng quy tắc "2 lần fail liên tiếp trên cùng LTF = dừng, lùi khung"; ưu tiên FVG H1/H4 làm POI chính khi LTF liên tục nhiễu.

#### EC7. Partial fill / limit không khớp đúng mức — giá chạm thiếu 1-2 tick rồi chạy

**Tình huống:** đặt limit buy tại CE của một bullish FVG trên XAUUSD, mức 2385.40. Giá chart hiển thị đã chạm 2385.35 (vượt qua CE) rồi bật tăng mạnh — nhưng lệnh limit của bạn không khớp, hoặc trên một số broker khớp muộn với giá tệ hơn 20-30 cent. Nhìn lại thấy "đúng sách" nhưng bị bỏ lỡ hoàn toàn move.

**Vì sao bẫy được cả trader có kinh nghiệm:** đây là hiện tượng **front-run bởi thuật toán tốc độ cao** — các HFT market maker phát hiện dòng lệnh limit dồn về một mức giá "hiển nhiên" (CE, mức tròn) và có xu hướng lấy hết thanh khoản ngay trước mức đó rồi đẩy giá đi tiếp, khiến limit order "chạm nhưng không khớp" (hoặc khớp một phần rất nhỏ). Cũng liên quan tới hiện tượng bid/ask chart quy chiếu (xem mục W5 trong War Stories).

**Cách nhận diện sớm:** nếu backtest cho thấy tỷ lệ "chạm nhưng không khớp" cao bất thường tại các mức giá tròn/CE rõ ràng, đó là dấu hiệu của front-running hoặc lệch bid/ask.

**Cách xử lý:** đặt limit order **lệch một chút** vào phía trong gap (không đặt đúng tại CE lý thuyết mà đặt sâu hơn vài tick/pip) để tăng khả năng khớp; hoặc dùng market order với LTF MSS xác nhận thay vì limit order thụ động tại múc chính xác.

#### EC8. FVG hoạt động khác hẳn trong trend một chiều mạnh — không retrace về POI

**Tình huống:** thị trường vào giai đoạn trend một chiều cực mạnh (ví dụ NQ trong giai đoạn risk-on liên tục nhiều tuần, hoặc BTC trong đợt bull run parabolic). FVG hình thành liên tục trên đường đi nhưng **không bao giờ được retrace đầy đủ** — giá chỉ chạm nhẹ proximal edge rồi tiếp tục chạy, khiến limit order tại CE hoặc distal không bao giờ khớp.

**Vì sao bẫy được cả trader có kinh nghiệm:** trader quen với hành vi "retrace về CE" trong thị trường bình thường sẽ liên tục đặt limit quá sâu và bỏ lỡ toàn bộ trend, hoặc tệ hơn cố "đợi giá về" và bỏ lỡ hàng chục điểm trong khi thị trường không bao giờ quay lại.

**Cách nhận diện sớm:** khi 2-3 FVG liên tiếp cùng hướng chỉ được test tới upper/lower quadrant (không tới CE) rồi tiếp tục chạy, đó là dấu hiệu trend đang ở chế độ "không cần rebalance sâu" — thường trùng với breakaway gap (xem mục 7.1).

**Cách xử lý:** trong trend xác nhận cực mạnh, chuyển entry mode sang "Aggressive" (gần proximal edge) thay vì chờ CE, hoặc chấp nhận bỏ lỡ một phần move và chờ cấu trúc điều chỉnh rõ ràng hơn thay vì cố ép limit sâu.

> [!note] Nhãn v2 cho Edge Cases EC1–EC8
> - **EC1, EC2, EC4, EC5** (feed CFD, rollover, DST, expiration/roll): **[MARKET MECHANICS]** về dữ liệu — đúng và quan trọng cho backtest; v2 đưa vào trường `feed`, `session_gap`, `news_window`, `roll_week`.
> - **EC3** (news slippage): đúng; kết hợp Bug 2 ở §21.3 (phân xử trên nến lớn che slippage).
> - **EC6** (fractal conflict): nhất quán với FVG-Sim-06 — mỗi nến H1 lớn chứa ~3 M5 FVG; quy tắc "2 lần fail → lùi khung" là **HEURISTIC** hợp lý.
> - **EC7** (limit chạm thiếu / front-run): phần "HFT front-run tại mức hiển nhiên" là **[INTERPRETATION]**; phần quan sát (chạm nhưng không khớp, bid/ask) là thật.
> - **EC8** (trend mạnh không retrace): chính là **drift** (FVG-Sim-02C: drift 0.2 ATR/nến → 39% FVG cùng chiều không bị chạm).

### 33.7 Case studies của v1 — số liệu chưa xác minh *(v1 §17, nguyên văn)*

> [!warning] Đọc trước khi dùng
> Bốn case dưới đây (EURUSD, NQ, XAUUSD, BTCUSD) có giá, giờ và R-multiple cụ thể nhưng **không có nguồn dữ liệu / screenshot / trade log đi kèm trong vault** (theo quy tắc CLAUDE.md: không bịa dữ liệu trade). v2 giữ nguyên làm **minh họa giáo khoa**, không dùng làm bằng chứng. Hai hình `FVG-CaseStudy-B1/B2` (chưa được nhúng ở v1) ghi "tái dựng minh họa từ mẫu backtest" nhưng không có dữ liệu gốc → không nhúng.

![[FVG-Case-Study.svg|720]]
*Sơ đồ: Diễn biến Case 1 — EURUSD Long sau sweep London, displacement phá BOS tạo FVG, entry tại CE, target liquidity xa (+9.8R trung bình).*

#### Case 1 — EURUSD, Long thắng đúng sách tại H1 bullish FVG sau sweep London

**Bối cảnh HTF:** EURUSD, thứ Ba 14/04, D1 bias bullish (chuỗi HL trên D1 từ đáy 1.0680, giá đang hồi về vùng discount của dealing range D1 1.0680–1.0920). Draw on liquidity: BSL tại 1.0910 (đỉnh dao động 3 ngày trước).

**Setup:** phiên London Open (08:00–09:00 London), giá quét xuống dưới đáy phiên Á tại 1.0745 (sweep SSL), sau đó một chuỗi 2 nến H1 displacement tăng mạnh (đóng cửa lần lượt tại 1.0761 và 1.0779, mỗi nến thân >25 pip) phá qua swing high nội bộ 1.0758 (MSS bullish), để lại bullish FVG H1 vùng 1.0752–1.0761, CE = 1.07565.

**Diễn biến & execution:** 11:20 London, giá retrace về 1.0757 (trong vùng FVG, gần CE). Trên M5 xuất hiện bullish MSS nhỏ tại 1.0755 sau khi phá swing high M5 1.0759. Entry Long tại 1.0758 (limit gần CE). Stop đặt dưới low FVG + buffer, tại 1.0748 (10 pip risk). Target 1: internal liquidity 1.0820 (đóng 50% vị thế, R:R ~6.2). Target 2: BSL chính 1.0910 (đóng phần còn lại).

**Kết quả bằng số:** giá chạy lên 1.0822 lúc 15:40 cùng ngày (chạm TP1, +6.4R trên phần đóng), tiếp tục lên 1.0908 vào phiên NY hôm sau trước khi retrace (TP2 gần đạt, đóng thủ công tại 1.0898 do dấu hiệu suy yếu momentum, +14R trên phần còn lại). R-multiple trung bình toàn lệnh: **+9.8R**.

**Bài học chỉ rút ra được nhờ case này:** thứ tự sweep → displacement phá cấu trúc → FVG → entry tại CE hoạt động rất sạch khi cả 4 yếu tố (HTF discount, sweep rõ, MSS thật, session thanh khoản sâu — London Open) đồng thời xuất hiện; đây là mẫu hình "giáo khoa" hiếm khi xảy ra hoàn hảo đến vậy, nên được dùng làm chuẩn tham chiếu (benchmark) khi đánh giá các setup khác có "thiếu" yếu tố nào.

#### Case 2 — NQ, setup "đẹp như sách" nhưng THUA: bullish FVG đúng mọi tiêu chí, vẫn bị xuyên và đảo IFVG

**Bối cảnh HTF:** NQ futures, thứ Năm 05/06, D1 bias bullish (giá đã tạo higher-high liên tục 5 phiên, đang ở discount của dealing range ngắn hạn 18,150–18,540 sau một nhịp điều chỉnh). Draw on liquidity: BSL tại 18,510.

**Setup:** trong Silver Bullet window (10:00–11:00 NY), giá quét xuống 18,238 (sweep SSL dưới đáy phiên sáng), sau đó nến displacement tăng mạnh (18,241 → 18,297, +56 point trong 5 phút) phá swing high M5 nội bộ tại 18,265 (MSS bullish rõ ràng, kèm volume spike), để lại bullish FVG M5 vùng 18,255–18,265, CE = 18,260. Toàn bộ checklist chấm 5/5: displacement phá cấu trúc ✓, POI đồng hướng HTF discount ✓, sau sweep ✓, trong kill zone (Silver Bullet) ✓, còn unmitigated ✓.

**Diễn biến & execution:** 10:22 NY, giá retrace về đúng CE 18,260. M1 xuất hiện tín hiệu MSS nhỏ giả (phá một swing rất nhỏ không ý nghĩa). Entry Long tại 18,261. Stop dưới low FVG, tại 18,251 (10 point risk = 200 USD/contract). Target: BSL 18,510.

11:05 NY, một chuỗi 3 nến M5 nhỏ dần (grind, không phải fast tap — xem mục W2 trong War Stories) gặm dần qua FVG, cuối cùng đóng nến M5 tại 18,247 — xuyên qua toàn bộ vùng FVG. Stop bị chạm tại 18,251 trước khi nến đóng hẳn. Vùng FVG cũ ngay sau đó đảo cực thành bearish IFVG (xem [[17-Inverse-Fair-Value-Gap-iFVG]]) và giá tiếp tục giảm về 18,190.

**Kết quả bằng số:** lỗ **-1R** (200 USD/contract), đúng theo kế hoạch risk nhưng là một trong những lệnh "đau" nhất vì mọi tiêu chí checklist đều đạt.

**Bài học chỉ rút ra được nhờ case này:** checklist 5/5 tiêu chí **không loại trừ được rủi ro cơ bản** — trong trường hợp này, tín hiệu MSS M1 lúc 10:22 là MSS giả (phá một đỉnh không có ý nghĩa cấu trúc thật), và cách giá *tiếp cận* lại FVG (grind bậc thang thay vì fast tap) đã là cảnh báo sớm bị bỏ qua vì quá tự tin vào checklist tổng quát. Đây là lý do phần "Phân tích chuyên sâu" (mục 14) và War Stories (mục W2) phải được xem như lớp lọc **bổ sung**, không phải thay thế, cho checklist chuẩn — checklist chỉ lọc được các FVG "về mặt hình học", không lọc được chất lượng vi mô của cú tiếp cận.

#### Case 3 — XAUUSD, đứng ngoài đúng: skip trade nhờ nhận ra red flag trước FOMC

**Bối cảnh HTF:** XAUUSD, thứ Tư 18/03, ngày có cuộc họp FOMC lúc 14:00 ET. D1 bias bullish nhẹ (giá dao động 2620–2660 nhiều ngày, chưa có xu hướng rõ). Giá đang ở khoảng giữa dealing range (gần equilibrium, không rõ premium/discount).

**Setup quan sát được:** lúc 13:15 ET (45 phút trước FOMC), một cây nến H1 displacement tăng bất thường (2634 → 2649, +15 USD trong một nến, thanh khoản mỏng vì thị trường đang "nín thở" chờ FOMC) để lại một bullish FVG H1 rõ ràng vùng 2636–2642.

**Vì sao chọn đứng ngoài — red flag nhận diện được:**
1. Displacement xảy ra **ngay trước** một sự kiện vĩ mô cực lớn (FOMC) trong khi thanh khoản thị trường đã co lại rõ rệt (spread giãn nhẹ, volume giảm so với trung bình giờ) — dấu hiệu điển hình của một cú "false move" trước tin, không phải dòng lệnh có chủ đích bền vững.
2. Giá đang ở **giữa range** (gần equilibrium), không đúng discount hay premium rõ ràng cho bất kỳ hướng nào — FVG không nằm tại POI HTF có ý nghĩa.
3. Không có liquidity sweep rõ ràng trước displacement — không có SSL/BSL nào bị quét, nghĩa là "chưa xong việc" theo logic thanh khoản.

**Quyết định:** không vào lệnh, ghi chú "no trade — pre-FOMC false move, sai vị trí P/D, không sweep" vào journal.

**Kết quả xác nhận quyết định đúng:** FOMC 14:00 ra thông điệp hawkish hơn kỳ vọng, giá lập tức đảo chiều giảm mạnh, xuyên thẳng qua toàn bộ vùng FVG vừa hình thành (đóng nến H1 tại 2609), xác nhận displacement 13:15 chỉ là nhiễu trước tin, không phải delivery thật.

**Bài học chỉ rút ra được nhờ case này:** khả năng **không trade** dựa trên nhận diện đúng 3 red flag (thời điểm sát tin lớn, sai vị trí P/D, thiếu sweep) có giá trị tương đương một lệnh thắng — case này minh họa trực tiếp quy tắc "không có lệnh" ở mục 8.C không phải là lý thuyết suông mà là kỹ năng cần luyện tập chủ động, đặc biệt trong ngày có lịch vĩ mô lớn.

#### Case 4 — BTCUSD, Short với bearish FVG trong xu hướng giảm — case đa dạng tài sản

**Bối cảnh HTF:** BTCUSD (Binance spot/perp), thứ Hai 09/09, D1 bias bearish rõ (giá đã phá qua đáy tuần trước tại 58,200, tạo lower-low, đang hồi về premium của leg giảm gần nhất: dealing range 61,800–58,200, premium quanh 60,000–61,800).

**Setup:** phiên NY PM (giờ thanh khoản Mỹ), giá hồi lên quét thanh khoản mua tại 60,850 (BSL từ một đỉnh dao động nhỏ 2 ngày trước), sau đó một nến H1 displacement giảm mạnh (60,890 → 60,210, -680 USD trong một nến, tương đương khoảng 1.1% trong 1 giờ) phá swing low nội bộ tại 60,340 (MSS bearish), để lại bearish FVG H1 vùng 60,340–60,590, CE = 60,465.

**Diễn biến & execution:** 21:40 UTC, giá retrace lên 60,470 (sát CE). M15 xuất hiện bearish MSS sau khi phá swing low M15 tại 60,390. Entry Short tại 60,460. Stop trên high FVG + buffer, tại 60,610 (150 USD risk, tương đương ~0.25% tài khoản với size phù hợp). Target 1: internal liquidity 59,400 (R:R ~7). Target 2: SSL chính tại 58,200.

Lưu ý đặc thù crypto: do BTC giao dịch 24/7 và perpetual futures có funding rate, trader kiểm tra funding rate tại thời điểm vào lệnh (funding dương cao bất thường — nhiều vị thế Long đòn bẩy đang trả phí cho Short) — đây là confluence bổ sung đặc thù crypto không tồn tại ở FX/futures truyền thống, củng cố thêm luận điểm còn nhiều Long yếu cần bị ép bán.

**Kết quả bằng số:** giá giảm về 59,380 sau 14 giờ (chạm TP1, đóng 50% vị thế, +6.8R), tiếp tục giảm về 58,150 hai ngày sau (chạm gần TP2, đóng phần còn lại tại 58,240, +14.5R). R-multiple trung bình: **+10.65R**.

**Bài học chỉ rút ra được nhờ case này:** trên crypto, FVG kết hợp với dữ liệu đặc thù thị trường (funding rate, open interest) tạo thêm một lớp confluence không có ở FX/index futures — nhưng cấu trúc cốt lõi (sweep → displacement phá cấu trúc → FVG → entry tại CE) hoàn toàn giống nhau giữa các loại tài sản, xác nhận đây là hiện tượng orderflow phổ quát chứ không phải đặc thù riêng của một thị trường.

> [!note] Chú thích v2 cho case studies v1
> - Case 1 (thắng đúng sách) và Case 4 (BTC short): minh họa trình tự 2022 Model; "+9.8R / +10.65R" không phải thống kê.
> - **Case 2 (thua dù 5/5)** là case có giá trị nhất: nó chính là adverse selection của §30.4 (grind vào FVG, limit khớp, bị xuyên) và failure mode F2.
> - **Case 3 (đứng ngoài trước FOMC)**: minh họa Disqualifying condition (news window) — giữ làm mẫu cho `skipped_reason`.
> - Câu kết Case 4 "xác nhận đây là hiện tượng orderflow phổ quát" — **[INTERPRETATION]**; hai case không xác nhận được tính phổ quát.

---

## 34. Checklist trước khi áp dụng vào trade

### 34.1 Checklist của v1 *(v1 §8, nguyên văn)*

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> FVG chỉ có giá trị khi nằm đúng **context + timeframe + liquidity narrative**. KHÔNG trade mọi FVG.

#### A. Context (HTF)
- [ ] Daily Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] FVG đồng hướng bias, không phải FVG ngược.
- [ ] FVG nằm đúng premium (Short) / discount (Long) của HTF dealing range.
- [ ] FVG nằm tại / trùng một POI HTF có ý nghĩa.
- [ ] Có draw on liquidity rõ ràng làm target.
- [ ] FVG sinh ra từ displacement phá cấu trúc, không phải gap giữa range.
- [ ] Xác định mức CE (50%) và level invalidation của FVG.

#### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã vào vùng FVG đúng premium/discount cho hướng trade.
- [ ] Đã có liquidity sweep hợp lý TRƯỚC khi displacement tạo FVG.
- [ ] Giá respect CE / mép FVG (reject), không đóng nến xuyên qua.
- [ ] Có LTF MSS + displacement xác nhận khi giá vào FVG.
- [ ] Entry quanh CE, không chase ở mép xa.
- [ ] Stop loss logic: ngoài đầu kia FVG / ngoài điểm sweep.
- [ ] Target là liquidity rõ; đường tới target không bị FVG/imbalance cản trở chưa xử lý.
- [ ] R:R tối thiểu đạt kế hoạch.

#### C. Quy tắc "không có lệnh"
- [ ] FVG không sinh ra từ displacement → không trade.
- [ ] FVG ngược bias / sai premium-discount → không trade.
- [ ] Chưa có liquidity sweep → không trade.
- [ ] FVG đã bị đóng nến xuyên qua (invalid) → không trade (trừ kế hoạch IFVG riêng).
- [ ] FVG giữa range / không có POI HTF → không trade.

### 34.2 D. Bổ sung v2 — giao thức thời gian thực
- [ ] FVG được đánh dấu **sau** close nến 3; đã ghi `known_at` (bar index / giờ).
- [ ] FVG được chọn theo **quy tắc khai báo trước** (first presented / discount-of-leg), không phải "cái đẹp nhất".
- [ ] Đã ghi: `size_atr`, `c2_range_atr`, `fvg_pos_in_leg`, `pd_location`, `sweep_before`, `news_window`, `session_gap`, `nested_in`.
- [ ] Đã chọn **một** định nghĩa invalidation (mặc định I2 — close cùng khung ngoài distal) và một mức hết hạn.
- [ ] Đã xác định cách vào: limit thụ động (CE/proximal) hay trigger (M5 MSS trong FVG) — và quy tắc rút limit khi grind.
- [ ] Nếu không vào: ghi `skipped_reason` và theo dõi kết quả giả định.
- [ ] Backtest: phân xử stop/target ở khung ≤ 1/5 khung setup; nến mơ hồ = thua; mô phỏng spread.

---

# PART VIII — PHÂN TÍCH PHẢN BIỆN

## 35. Mười ngộ nhận phổ biến (brief §42)

| # | Ngộ nhận | Sự thật | Bằng chứng / mục |
|---|---|---|---|
| 1 | **Mọi FVG đều sẽ được lấp** | Trên random walk không drift: đúng *cuối cùng* (97% trong 2000 nến) — nên không mang thông tin. Có drift: FVG cùng chiều trend thường không bị chạm (39% với drift 0.2 ATR/nến) | §15; FVG-Sim-02 |
| 2 | **FVG là vùng không có giao dịch** | Nến 2 đi qua toàn vùng (thị trường liên tục) — vùng có giao dịch, chỉ ít thời gian | §2.2; FVG-Deep-01 |
| 3 | **FVG tự động nghĩa là có hoạt động tổ chức** | Random walk tạo ~31 FVG/100 nến; danh tính người tham gia không quan sát được từ OHLC | §9.2; FVG-Sim-01 |
| 4 | **FVG tự động là support/resistance** | "Phản ứng gần FVG" xảy ra theo hình học; S/R phải được chứng minh hơn vùng đối chứng | §18; FVG-Sim-04A |
| 5 | **FVG tự nó là tín hiệu vào lệnh** | FVG là location; cần trigger và context. "FVG alone" không hơn đối chứng trên nhiễu | §24; §40 |
| 6 | **Mọi displacement đều tạo FVG có ý nghĩa** | ~88% nến 2 ≥ 2 ATR tạo FVG trên random walk; "có ý nghĩa" là giả thuyết; toy model: displacement mạnh có thể là loại tạm thời | §10; §30.3 |
| 7 | **Mọi FVG đều quan trọng như nhau** | Đúng là không như nhau — nhưng "quan trọng hơn" phải đo ex-ante và test (FSS) | §29 |
| 8 | **50% của FVG luôn là entry tốt nhất** | CE là quy ước; hình học không có điểm gãy tại 0.5; mức tối ưu (nếu có) theo từng symbol | §16; FVG-Sim-04B |
| 9 | **FVG + liquidity sweep bảo đảm đảo chiều** | Sweep là phép thử, không phải tín hiệu; FVG sau sweep có thể là liquidity-type → bị lấp | §23; [[20-Liquidity-Sweep]] |
| 10 | **Bullish FVG phải dẫn tới tăng tiếp** | Bullish FVG chỉ mô tả cú đẩy đã xảy ra; tương lai phụ thuộc drift và loại dòng lệnh | §30 |

Bổ sung từ v2:

| # | Ngộ nhận | Sự thật |
|---|---|---|
| 11 | "LTF liquidity void xác nhận HTF FVG" | 98% H1 FVG chứa M5 FVG — và 99.9% nến H1 lớn *không* có H1 FVG cũng chứa M5 FVG → xác nhận tự động (§27.3) |
| 12 | "Backtest của tôi cho win rate 60–70% với FVG" | Hãy kiểm tra Bug 1 (low nến 3 = lần chạm đầu) và Bug 2 (phân xử bằng nến lớn): trên nhiễu chúng cho 65% và 50% (§21.3) |
| 13 | "Lọc displacement mạnh luôn cải thiện kết quả" | Toy model: lọc này có thể làm kết quả tệ hơn do adverse selection (§30.4) |
| 14 | "Lệnh chờ bị bỏ lại trong gap kéo giá về" | Lệnh chờ trong vùng đã bị nến 2 khớp; chỉ lệnh mới có thể nằm đó (§9.6) |

---

## 36. Hindsight, look-ahead, narrative, nhân quả

### 36.1 Sáu lỗi suy luận và cách chặn

| Lỗi | Biểu hiện với FVG | Cách chặn |
|---|---|---|
| **Hindsight bias** (Fischhoff 1975) | Nhìn chart cũ thấy FVG "rõ ràng" ở điểm đảo chiều | Bar replay; che bên phải; ghi quyết định trước khi xem nến tiếp |
| **Look-ahead bias** | Dùng low nến 3 như lần chạm; vẽ FVG trước close nến 3; dùng swing chưa xác nhận | known_at cho mọi thứ; code `j > i` |
| **Selection / survivorship** | Ảnh chụp FVG đẹp trên mạng; nhớ FVG thắng | Ghi mọi FVG thỏa quy tắc, cả cái không vào |
| **Narrative fallacy** | "Smart money để lại FVG để quay lại khớp nốt" | Tách 5 lớp (§9.4) — câu chuyện chỉ ở lớp ICT |
| **Correlation ≠ causation** | "Giá bật ở FVG → FVG gây ra bật" | Vùng đối chứng cùng hình học |
| **Multiple testing / overfit** | Thử 20 bộ lọc, giữ cái đẹp nhất | Khóa giả thuyết trước; hiệu chỉnh α; out-of-sample (§43) |

### 36.2 Unfalsifiability — dấu hiệu nhận biết
Một framework FVG trở nên **không thể bác bỏ** khi mọi lệnh thua đều có lời giải thích sau sự kiện: "thiếu confluence", "nến tin", "phải chờ IFVG", "sai khung". Cách chặn: viết **trước** điều gì sẽ bác bỏ giả thuyết (§43.5) và đếm tỷ lệ lệnh thua mà bạn giải thích bằng một yếu tố *không có trong checklist trước đó*. Nếu tỷ lệ này cao, framework đang được vá theo kết quả.

---

## 37. Phản biện & giới hạn

### 37.1 Phản biện của v1 *(v1 §15, nguyên văn)*

FVG là PD array bị phản biện nhiều nhất trong toàn bộ hệ ICT — chính vì nó dễ vẽ, dễ thấy, và được quảng bá rộng rãi trên mạng xã hội trading như một "chén thánh". Đáng để mổ xẻ thẳng thắn.

#### 15.1. Phản biện từ góc nhìn khoa học/quant

1. **Tính chủ quan khi vẽ.** Cho hai trader cùng nhìn một chart, gần như chắc chắn sẽ có bất đồng: nến nào là "displacement" đủ mạnh để tính là nến 2? Gap 2 pip có tính hay không? FVG bị "ăn mòn" 80% có còn tính là FVG "sống" không? Không có định nghĩa toán học cứng nào được ICT chính thức hóa cho ngưỡng "đủ lớn" — mọi threshold (kích thước tối thiểu, tỷ lệ body/range của nến giữa) đều là quy ước cá nhân của người backtest.
2. **Hindsight bias & confirmation bias.** Trader nhớ rất rõ những lần FVG "đẹp" dẫn tới một cú reversal ngoạn mục, nhưng quên hàng chục FVG hình thành mỗi ngày trên mọi khung thời gian mà không dẫn tới gì cả. Vì FVG xuất hiện ở MỌI nơi trên chart (gần như mọi cây nến displacement đều để lại ít nhất một gap nhỏ nào đó ở khung thời gian nào đó), việc "tìm thấy" một FVG trùng với điểm đảo chiều sau khi nó đã xảy ra là gần như tất yếu về mặt thống kê — không chứng minh được nhân quả.
3. **Thiếu backtest công khai đạt chuẩn thống kê.** Không có nghiên cứu định lượng công khai, peer-reviewed hoặc từ quỹ định lượng lớn nào xác nhận FVG có edge dương sau phí giao dịch và slippage trên mẫu đủ lớn (hàng nghìn setup, nhiều regime thị trường, out-of-sample). Phần lớn "bằng chứng" là ảnh chụp màn hình chọn lọc (cherry-picked) từ cộng đồng ICT, không phải equity curve từ dữ liệu tick đầy đủ.
4. **Unfalsifiable khi thất bại.** Khi một FVG "đẹp như sách" fail, phản xạ phổ biến trong cộng đồng ICT không phải là kết luận "concept sai", mà là tìm lý do bổ sung: "thiếu confluence", "chưa đúng kill zone", "đó là nến tin nên không tính", "phải chờ IFVG". Cơ chế thêm điều kiện *sau khi biết kết quả* khiến giả thuyết gần như không thể bị bác bỏ bằng dữ liệu — đặc điểm kinh điển của một lý thuyết thiếu tính khoa học theo tiêu chuẩn Popper.
5. **Overfitting khi thêm filter.** Càng thêm điều kiện lọc (đúng bias + đúng premium/discount + sau sweep + trong kill zone + CE trùng OTE...) để "cứu" tỷ lệ thắng, số lượng setup đạt đủ điều kiện càng ít đi, và càng dễ rơi vào bẫy tối ưu hóa cho đúng đúng dữ liệu lịch sử cụ thể đã dùng để chỉnh rule (curve-fitting) — không đảm bảo hoạt động tốt trên dữ liệu tương lai.
6. **Backtest độc lập cho kết quả trái chiều.** Một số trader định lượng backtest FVG một cách máy móc (không context) và công bố kết quả gần với random hoặc thậm chí âm sau phí; trong khi một số khác báo cáo kết quả dương khi thêm bộ lọc HTF bias. Sự trái chiều này bản thân nó là bằng chứng cho thấy **edge (nếu có) không nằm ở bản thân hình dạng gap**, mà nằm hoàn toàn ở các điều kiện lọc xung quanh — và các điều kiện đó lại quay về vấn đề (1) và (5).
7. **Giải thích thay thế đơn giản hơn.** Hiện tượng "giá quay lại lấp gap rồi tiếp tục" có thể được giải thích đầy đủ bằng các khái niệm thống kê không cần khái niệm "imbalance": **mean reversion ngắn hạn** (giá luôn có xu hướng dao động quanh một đường trung bình động sau một cú di chuyển mạnh — hiệu ứng được ghi nhận rộng rãi trong tài chính định lượng, không liên quan ICT), **volatility clustering** (một cú nến lớn thường theo sau bởi các nến biên độ nhỏ hơn — GARCH effect chuẩn), và đặc tính tự nhiên của **random walk có drift** (bất kỳ chuỗi giá ngẫu nhiên nào cũng sẽ tạo ra các "khoảng trống" giữa local extremes, không cần một "cơ chế institutional" đặc biệt nào để giải thích).

#### 15.2. Phản biện của phản biện

- **Phần phải chấp nhận hoàn toàn:** điểm (1) tính chủ quan và (3) thiếu backtest chuẩn hóa công khai là đúng và không thể bác bỏ — đây là giới hạn thật của FVG như một khái niệm được truyền miệng qua cộng đồng thay vì được công thức hóa học thuật. Điểm (7) cũng đúng ở chỗ: nhiều hiện tượng FVG "giải thích" thực ra chỉ là biểu hiện khác của mean reversion đã biết từ lâu trong tài chính định lượng — ICT không phát minh ra hiện tượng, chỉ đặt tên và framework hóa nó theo ngôn ngữ orderflow.
- **Phần có thể trả lời được:**
  - **Quy tắc hóa cứng để backtest được:** vấn đề (1) có thể giảm đáng kể (không loại bỏ hoàn toàn) bằng cách định nghĩa toán học rõ ràng trước khi backtest: gap tối thiểu bao nhiêu ATR, nến giữa tối thiểu bao nhiêu % range trung bình, đo trên timeframe cố định nào. Nhiều trader định lượng nghiêm túc đã làm việc này và nhận được kết quả nhất quán hơn (dù vẫn khiêm tốn) so với việc vẽ "bằng mắt".
  - **FVG là framework đọc chart, không phải tín hiệu máy móc:** phản biện (2)-(4) phần lớn nhắm vào việc trade FVG như một tín hiệu độc lập ("thấy gap → vào lệnh") — đây đúng là cách dùng sai mà chính tài liệu này (mục 1, "FVG không phải là gì") đã cảnh báo. Nếu FVG được dùng như một **điểm tham chiếu để định vị risk** (nơi đặt limit order chờ, nơi đặt stop logic) trong một hệ thống có bias HTF + liquidity + risk management chặt, thì "edge" không cần đến từ bản thân hình dạng gap mà đến từ **cấu trúc quản trị rủi ro xung quanh nó** — một khẳng định khác hẳn với khẳng định "FVG dự đoán được giá".
  - **Edge từ risk management + location, không phải "dự đoán":** ngay cả khi chấp nhận giả thuyết (7) rằng phần lớn hiện tượng chỉ là mean reversion tự nhiên, một trader vẫn có thể khai thác nó có lợi nhuận nếu (a) vào lệnh tại vùng có xác suất mean-reversion cao hơn trung bình (CE của một displacement rõ, tại POI HTF), (b) luôn có invalidation rõ ràng (đóng nến xuyên qua), và (c) R:R được cấu trúc thiên về phía có lợi (stop ngắn ngoài distal, target là liquidity xa). Đây là logic "positive expectancy từ vị trí đặt cược + kiểm soát thua lỗ", không phải "dự đoán chính xác hướng đi" — khác biệt quan trọng về mặt triết học giữa "trading edge" và "market prediction".

#### 15.3. Giới hạn cứng phải chấp nhận

- Không có ngưỡng kích thước tối thiểu được chuẩn hóa cho một "FVG hợp lệ" — mọi số liệu (ví dụ "gap phải ≥ 20% ATR") đều là quy ước tự đặt, không có cơ sở lý thuyết duy nhất đúng.
- FVG **thay đổi hình dạng theo timeframe quan sát** — không có một "FVG khách quan" độc lập với khung thời gian bạn chọn để nhìn.
- Không thể phân biệt bằng mắt thường (không có footprint/volume-at-price) một FVG "thật" (ít giao dịch nội tại) với một FVG "ảo ảnh gộp nến" (do OHLC aggregation che khuất giao dịch thật) — hai loại này trông giống hệt nhau trên chart nến thường.
- Không có bằng chứng định lượng công khai, đủ mẫu và ngoài mẫu, chứng minh FVG là yếu tố **dự đoán độc lập** có ý nghĩa thống kê sau khi đã kiểm soát cho các yếu tố khác (trend, volatility, thời điểm trong ngày).
- Thị trường thay đổi hành vi liên tục — participant mix, tốc độ thuật toán, độ sâu thanh khoản đều biến đổi theo thời gian; ngay cả nếu FVG "có edge" trong một giai đoạn lịch sử, không có gì đảm bảo edge đó bền vững (edge decay là hiện tượng phổ biến trong toàn ngành quant, không riêng gì FVG).

> [!quote] Kết luận trung thực
> FVG là một cách hữu ích để **định vị nơi đặt lệnh và đặt stop** trong một hệ thống trade có bias HTF, liquidity context và risk management rõ ràng — nó tổ chức lại sự chú ý của trader vào những vùng giá có xác suất phản ứng cao hơn ngẫu nhiên, không phải một công cụ dự đoán chính xác điểm đảo chiều. Đừng tin bất kỳ ai khẳng định FVG "luôn được lấp" hay có tỷ lệ thắng cố định nào đó mà không kèm dữ liệu backtest ngoài mẫu của chính họ. Dùng FVG như một trong nhiều lớp confluence, luôn tự backtest trên chính thị trường và khung thời gian mình trade, và coi mọi con số về "hiệu quả FVG" trên mạng xã hội là marketing cho tới khi tự kiểm chứng được.

### 37.2 Bổ sung v2 — điều chúng ta thực sự biết sau nghiên cứu này

> [!note] Đánh giá v1 §15
> Phản biện của v1 **đúng và trung thực**; v2 không bác bỏ điểm nào. Ba bổ sung: (1) điểm 7 (giải thích thay thế: mean reversion, volatility clustering, random walk) nay có **số đo** (FVG-Sim-01/02/04); (2) điểm 6 ("backtest trái chiều") có thể được giải thích một phần bằng **lỗi look-ahead và độ phân giải** (FVG-Sim-05) — hai backtest "cùng chiến lược" có thể khác nhau 30 điểm win rate chỉ vì cách code "touch"; (3) "edge từ risk management + location" (§15.2 của v1) — đúng về mặt khái niệm, nhưng *location* chỉ tạo edge khi xác suất tại location đó **khác** đường nền; risk management không tạo expectancy dương từ một chuỗi có expectancy 0.

**Điều đã biết [MATHEMATICAL / SIMULATION]:**
1. FVG là vùng chỉ nến 2 đi qua; không phải vùng không giao dịch.
2. Tần suất FVG trên nhiễu cao (~31/100 nến); FVG gần như là hàm của nến 2 lớn tương đối.
3. Chạm/lấp FVG trên nhiễu tuân theo hình học khoảng cách; "gap nào cũng lấp" là tính hồi quy.
4. CE không có điểm gãy hình học.
5. Lỗi look-ahead/độ phân giải có thể tạo "edge" rất lớn.
6. FVG phụ thuộc khung và mốc nến; xác nhận LTF gần như tự động.

**Điều có cơ sở cơ chế nhưng chưa kiểm chứng cho FVG [MARKET MECHANICS → HYPOTHESIS]:**
7. Transient impact và phần thưởng cung cấp thanh khoản có thể làm FVG từ dòng lệnh không mang thông tin bị lấp sâu hơn hình học.
8. Dòng lệnh có trí nhớ dài (metaorder) có thể làm FVG cùng chiều ít bị chạm hơn hình học.
9. Adverse selection có thể làm lệnh limit tại FVG kém hơn FVG lúc hình thành.

**Điều chưa biết [BACKTEST REQUIRED]:**
10. Trên dữ liệu thật của bạn, FVG có khác vùng đối chứng không — và khác ở đâu (symbol, khung, session, context).

### 37.3 Phản biện của chính v2 — giới hạn của mô phỏng
- **Random walk thiếu cấu trúc vi mô thật:** không có spread, sổ lệnh, giờ giao dịch, volatility theo giờ trong ngày, tin tức. Thị trường thật có thể có tính chất làm FVG hành xử khác — đó chính là điều cần test. Mô phỏng chỉ cho **đường nền**.
- **Toy model có tham số tùy chọn:** tỷ lệ ba loại displacement, τ, kích thước — đều minh họa. Kết quả "lọc displacement làm tệ hơn" phụ thuộc tỷ lệ đó. Thông điệp đúng là *cơ chế adverse selection tồn tại*, không phải *dấu của hiệu ứng*.
- **Không có bằng chứng ≠ bằng chứng không có:** note không chứng minh FVG vô dụng. Nó chứng minh rằng *những gì thường được đưa ra làm bằng chứng* (FVG xuất hiện, được lấp, được chạm ở CE, backtest win rate cao) **không phân biệt** được thế giới có edge với thế giới không có edge.

---

## 38. Lỗi thường gặp

### 38.1 Lỗi thực thi *(v1 §9, nguyên văn)*

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade mọi FVG | Vẽ FVG khắp chart, vào lệnh ở bất kỳ gap nào | Phần lớn FVG là nhiễu, không có edge | Chỉ trade FVG tại POI HTF + đúng bias + sau sweep |
| FVG không có displacement | Nến giữa body nhỏ, không phá cấu trúc | Không phản ánh intent, dễ bị xuyên qua | Yêu cầu displacement phá BOS/MSS mới tính FVG chất lượng |
| Bỏ qua premium/discount | Long ở FVG premium, Short ở FVG discount | Entry trở thành chase, R:R xấu | Long chỉ ở FVG discount, Short chỉ ở FVG premium |
| Vào trước liquidity sweep | Giá chưa quét đỉnh/đáy đã entry tại FVG | Stop nằm đúng nơi market còn muốn quét | Chờ sweep → displacement → FVG, đúng thứ tự |
| Nhầm fill với invalidation | Coi giá lấp FVG là "fail" và thoát sớm | Lấp tới CE/full fill có thể vẫn respect | Phân biệt respect (reject) vs đóng nến xuyên qua (invalid) |
| Bỏ qua CE | Entry ở mép xa gap, không dùng 50% | R:R kém; bỏ lỡ mức phản ứng quan trọng nhất | Ưu tiên entry quanh CE; coi CE là mức xác nhận |
| Không nhận ra IFVG | FVG bị xuyên rồi vẫn cố giữ lệnh ngược | FVG fail đảo cực thành S/R ngược hướng | Khi FVG bị đóng nến xuyên qua, đảo tư duy sang IFVG |
| Trade FVG ngược bias | Bullish FVG đẹp nhưng HTF bearish | Target ngược hướng thiếu room, xác suất thấp | Chỉ trade FVG đồng hướng Daily Bias |
| Chọn sai FVG khi chồng chéo | Nhiều FVG gần nhau, vào đại một cái | Mức tham chiếu mơ hồ, stop/target không logic | Chọn FVG trùng POI HTF / có confluence rõ nhất |
| Chase FVG sau expansion lớn | Vào FVG hình thành cuối một leg đã chạy xa | Phần lớn range đã tiêu thụ, dễ retrace | Chờ FVG tại POI HTF mới hoặc bỏ qua |

### 38.2 Lỗi suy luận (v2)

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Coi "FVG được lấp" là bằng chứng | "Thấy chưa, giá đã quay lại FVG" | Random walk lấp 71% trong 20 nến | So với vùng đối chứng (§13.4) |
| Không nêu định nghĩa respect | "FVG được tôn trọng 70%" | Touch/CE/full/close cho số khác nhau 20 điểm | DEF-FVG-02/03/04 |
| Vẽ FVG trước close nến 3 | Limit đặt khi nến 3 đang chạy | 52% gap tạm thời biến mất | known_at |
| Đếm low nến 3 là lần chạm | Backtest win rate cao bất thường | Bug 1: 32% → 65% trên nhiễu | `j > i` |
| Phân xử trên khung lớn | Backtest M5 bằng chart H1 | Bug 2a: 32% → 50% | Khung ≤ 1/5 khung setup |
| Đếm confluence trùng | OB + FVG + displacement = "3 yếu tố" | Cùng một sự kiện | §12.2, §18.2 |
| Chỉnh rule sau 30 lệnh | "Đổi entry từ CE sang 75%" | CI ±17.5 điểm | ≥ vài trăm mẫu, out-of-sample |
| Tìm "FVG ẩn" sau khi thấy đảo chiều | Zoom xuống LTF tìm lý do | Gần như luôn tìm thấy (Sim-06) | Quy tắc chọn LTF FVG khai báo trước |
| Bỏ qua setup không khớp | Chỉ thống kê lệnh đã vào | Che adverse selection | Ghi `missed_valid_setup` + kết quả giả định |

---

# PART IX — ĐỊNH LƯỢNG

## 39. Từ điển biến — tách *biến quan sát* khỏi *ngưỡng đề xuất* (brief §45)

### 39.1 Biến hình học & displacement (biết tại close nến 3)

| Biến | Công thức (bullish; bearish lấy dấu) | Ngưỡng đề xuất (HEURISTIC) |
|---|---|---|
| `size` | L₃ − H₁ | — |
| `size_atr` | size / ATR14[i] | min 0.25 cho setup; > 1.5 = "quá rộng" |
| `c2_range_atr` | (H₂ − L₂) / ATR14[i−1] | ≥ 1.5 "displacement-sized"; ≥ 2 "mạnh" |
| `c2_body_pct` | \|C₂ − O₂\| / (H₂ − L₂) | ≥ 0.6 |
| `leg_bars` | Số nến cùng chiều liên tiếp của leg chứa FVG | — |
| `fvg_pos_in_leg` | (CE − leg_low) / (leg_high − leg_low) | — (biến cho HYP-FVG-006c) |
| `dist_close_prox_atr` | (C₃ − proximal) / ATR | — (biến kiểm soát khoảng cách) |
| `broke_swing_level` | Level swing cao nhất bị phá bởi leg (theo thuật toán swing của vault) | ≥ 2 |
| `stacked_rank` | Thứ tự FVG trong leg (1 = first presented) | — |

### 39.2 Biến bối cảnh (biết trước khi retrace — phải có known_at)

| Biến | Công thức | Ghi chú |
|---|---|---|
| `htf_bias` | Nhãn D1 ex-ante (bull/bear/neutral) + confidence | [[59-Daily-Bias]] |
| `pd_location` | (CE − range_low)/(range_high − range_low), range có known_at | Discount < 0.5 |
| `dist_to_dol_atr` | \|DOL − entry\| / ATR | R:R danh nghĩa |
| `dist_to_opp_liq_atr` | Khoảng cách tới liquidity đối diện | Rủi ro bị quét |
| `sweep_before` | Có liquidity event ex-ante trong ≤ 10 nến trước nến 2 | [[20-Liquidity-Sweep]] |
| `session`, `killzone`, `macro` | Theo giờ sàn | [[18-Kill-Zones]] |
| `news_window` | ±5 phút quanh tin high-impact | — |
| `session_gap`, `feed`, `roll_week` | Cờ dữ liệu | §8.3, v1 EC |
| `nested_in` | none / M15 / H1 / D1 | §27 |
| `trend_proxy` | Tỷ lệ FVG cùng chiều chưa bị close xuyên trong 50 nến; độ dốc MA | Proxy drift |
| `atr_pct` | Percentile ATR 100 nến | Regime volatility |

### 39.3 Biến sau hình thành (cập nhật tại mỗi close nến)

| Biến | Công thức | Ghi chú |
|---|---|---|
| `bars_to_touch` | Số nến tới lần chạm đầu | Hình học: 43% = 1 nến |
| `touch_count` | Số lần chạm (đếm trên LTF — v1 W3) | — |
| `max_depth` | (proximal − cực trị)/size | 0.5 = CE; 1 = full |
| `fill_pct` | min(max_depth, 1) | — |
| `approach_speed` | Số nến LTF liên tiếp cùng chiều về FVG ngay trước touch; độ dốc trung bình / ATR | "Grind" nếu ≥ 6 nến, body < 0.5 ATR (HEURISTIC, v1 W2) |
| `age_bars` | Nến hiện tại − i | — |
| `state` | PROVISIONAL / ACTIVE / TOUCHED / CE / FULL / REACTED / INVALIDATED / INVERTED / EXPIRED | §20 |

### 39.4 Biến kết quả và khớp lệnh

| Biến | Công thức | Ghi chú |
|---|---|---|
| `reaction_atr` | MFE sau touch trong m nến, đơn vị ATR | Reaction nếu ≥ k (1.0) |
| `reaction_speed` | reaction_atr / số nến tới MFE | — |
| `mae_r`, `mfe_r` | MAE/MFE đơn vị R | Tối ưu stop/target |
| `filled`, `fill_price`, `fill_time` | Thực tế, không lý tưởng | Adverse selection |
| `r_multiple` | (exit − entry)/risk | Fill thực tế |
| `p_null` | (fill − stop)/(target − stop) | Đường nền hình học |
| `excess` | win − p_null | Thước đo chính |
| `missed_valid_setup`, `skipped_reason` | — | Để đo adverse selection |

---

## 40. FVG có predictive value độc lập không? (brief §44)

### 40.1 Câu hỏi đúng
Không hỏi "FVG có work không?" mà hỏi **"FVG có *incremental* predictive value không?"** — tức là, thêm FVG vào một mô hình (hoặc thay một vùng đối chứng bằng FVG) có làm kết quả tốt hơn *một cách có ý nghĩa thống kê, ngoài mẫu* không?

### 40.2 Bốn mô hình lồng nhau

| Model | Điều kiện | So với |
|---|---|---|
| **A — FVG alone** | Mọi FVG ≥ min_size; limit CE; stop distal − b; target cố định R | Vùng đối chứng cùng hình học (A₀) |
| **B — FVG + HTF context** | A + cùng chiều D1 bias + đúng P/D | B₀: vùng đối chứng cùng điều kiện context |
| **C — FVG + event** | B + liquidity event + MSS + displacement trên leg | C₀: cùng điều kiện, vùng đối chứng trên cùng leg |
| **D — Full framework** | C + killzone + D1→H1→M5 + trigger M5 | D₀; và D không có FVG (vào bằng OB/limit ở mức khác của leg) |

**Hai loại so sánh:**
- *Dọc* (A → B → C → D): bộ lọc có thêm giá trị không? (ablation)
- *Ngang* (X vs X₀): ở mỗi tầng, **FVG có hơn vùng đối chứng** không? — đây mới là câu hỏi "FVG có giá trị không".

Nếu B ≫ A nhưng B ≈ B₀ → giá trị đến từ **context**, không từ FVG. Nếu C > C₀ → FVG có giá trị *trong điều kiện sự kiện* (HYP-FVG-007/008). Đây là cách duy nhất trả lời câu hỏi của brief: *"FVG có edge độc lập hay chỉ hữu ích khi kết hợp với context?"*

### 40.3 Chỉ số so sánh
Win rate, p_null, **excess**, expectancy (R), median R, profit factor, max drawdown (R), MAE/MFE, tần suất lệnh/tháng, độ ổn định theo năm/symbol/session (robustness), độ nhạy theo regime. Báo cáo **khoảng tin cậy** (bootstrap theo ngày) cho mọi chỉ số chính.

### 40.4 Diễn giải các kết quả có thể

| Kết quả | Nghĩa |
|---|---|
| A ≈ A₀, B ≈ B₀, C ≈ C₀, D ≈ D₀ | FVG không thêm thông tin so với vị trí cùng khoảng cách; giá trị (nếu có) nằm ở context/trigger/quản trị |
| A ≈ A₀ nhưng C > C₀ | FVG có giá trị *có điều kiện* — chỉ sau sự kiện |
| A > A₀ | FVG có giá trị độc lập (đáng ngạc nhiên — kiểm tra kỹ look-ahead) |
| X < X₀ | FVG *kém* đối chứng — kiểm tra adverse selection (§30.4); cân nhắc entry có xác nhận |
| Kết quả tốt in-sample, mất out-of-sample | Overfit |

---

# PART X — BACKTEST

## 41. Thiết kế backtest (brief §46, project §22)

### 41.1 Đặc tả nghiên cứu (17 mục)

| # | Mục | Đặc tả v0.1 |
|---|---|---|
| 1 | Hypothesis | HYP-FVG-002: P(reaction \| FVG) > P(reaction \| control zone cùng hình học); và các HYP khác (§42) |
| 2 | Population | Mọi FVG thỏa DEF-FVG-01, size ≥ 0.25 ATR, trên khung setup |
| 3 | Timeframe | Setup: M15 và H1; phân xử: M1 (hoặc tick) |
| 4 | Market | Mỗi symbol riêng: NQ1 (CME), EURUSD, GBPUSD, XAUUSD — không gộp trước khi xem riêng |
| 5 | Sample size | ≥ 700 lệnh mỗi nhóm cho excess +5 điểm; ≥ 1,500 mỗi nhóm cho so sánh FVG vs control (§43.1) |
| 6 | Inclusion | known_at hợp lệ; dữ liệu đầy đủ; không trong news window (trừ khi test HYP-FVG-017) |
| 7 | Exclusion | Session gap trong 3 nến; roll week (futures); feed lỗi; ngày lễ thanh khoản thấp |
| 8 | Entry | Biến thể khai báo trước: E1 limit proximal; E2 limit CE; E3 M5 MSS trong FVG (market); W = 20 nến |
| 9 | Stop | distal − 0.1·ATR (hoặc − spread trung bình phiên, lấy lớn hơn) |
| 10 | Target | T1: 2R cố định (để có p_null rõ); T2: liquidity gần nhất có known_at |
| 11 | Session | Ghi; test riêng killzone vs ngoài (HYP-FVG-018) |
| 12 | Spread/slippage | Mô phỏng spread theo giờ; stop khớp tại giá M1/tick đầu tiên vượt stop (gap-through) |
| 13 | Look-ahead | FVG chỉ từ close nến 3; touch từ nến i+1; mọi mức tham chiếu có known_at; nến mơ hồ = thua |
| 14 | Survivorship | Dùng hợp đồng liên tục có roll rõ ràng (futures); không loại symbol "không hiệu quả" sau khi thấy kết quả |
| 15 | Outcome | `r_multiple`, `win`, `p_null`, `excess`, `reaction_atr`, `max_depth`, `mae_r`, `mfe_r` |
| 16 | Metrics | Win, excess, E[R], median R, PF, max DD, streaks, CI bootstrap theo ngày |
| 17 | Robustness | Theo năm, symbol, session, ATR regime, trend regime; độ nhạy tham số ±25%; walk-forward |

### 41.2 Quy tắc v0.1 dạng IF–THEN (ví dụ Model C, long)

```text
IF   D1 bias = bullish (ex-ante, known_at ≤ ngày hiện tại)
AND  giá trong discount của dealing range H4/D1 (range known_at trước sự kiện)
AND  liquidity event: một nến H1/M15 xuyên mức SSL ex-ante rồi đóng lại bên trên (DEF-LS)
AND  trong ≤ 6 nến sau đó: leg tăng phá swing high level ≥ 2, nến 2 có c2_range_atr ≥ 1.5
AND  leg để lại bullish FVG (DEF-FVG-01), size_atr ∈ [0.25, 1.5]; chọn FVG đầu tiên của leg
AND  giá chạm CE trong ≤ 20 nến kể từ known_at, chưa có close xuyên distal
THEN long tại CE (limit); stop = distal − max(0.1·ATR, spread); target = 2R (T1) hoặc liquidity gần nhất (T2)
EXIT stop / target / hết 48 nến kể từ entry (đóng tại close)
LOG  mọi trường ở §41.5, kể cả khi KHÔNG khớp (missed_valid_setup)
```

### 41.3 Năm thiết kế nghiên cứu

| Thiết kế | Câu hỏi | Ưu điểm | Nhược điểm |
|---|---|---|---|
| **Event study** (không trade) | Sau FVG, phân bố max_depth, reaction, invalidation khác đối chứng thế nào? | Nhiều mẫu, ít tham số | Chưa tính khớp lệnh |
| **Trade study** (bracket cố định) | Excess và E[R] với quy tắc cố định | Gần thực tế | Kết quả phụ thuộc bracket |
| **Matched control** | FVG vs vùng cùng hình học | Trả lời "FVG có giá trị không" | Cần xây control cẩn thận (§41.4) |
| **Ablation** (Model A–D) | Bộ lọc nào đóng góp? | Tránh overfit qua checklist | Nhiều so sánh → hiệu chỉnh α |
| **Forward test** (paper/live nhỏ) | Có tái lập được không? | Không có look-ahead | Chậm, mẫu nhỏ |

### 41.4 Xây vùng đối chứng — DEF-FVG-06 (v0.1)
Với mỗi FVG (hướng d, known_at i, khoảng cách close→proximal δ = d·(C₃ − proximal)/ATR, size s = size/ATR):
1. Chọn ngẫu nhiên một nến t (cùng symbol, cùng khung) với cùng **session**, cùng **quintile ATR percentile**, cùng **trend_proxy quintile**, và **không** có FVG cùng chiều ở t−2…t.
2. Vùng đối chứng: proximal_c = C[t] − d·δ·ATR[t]; distal_c = proximal_c − d·s·ATR[t].
3. Áp dụng **đúng** quy tắc entry/stop/target/hết hạn như FVG.
4. Lặp 3–5 lần mỗi FVG (nhiều control/FVG giảm phương sai).

Biến thể mạnh hơn: control **trên cùng leg** — vùng cùng size đặt ở vị trí khác của leg displacement (không phải FVG) — tách "FVG" khỏi "leg displacement".

### 41.5 Schema journal (bổ sung cho template backtest — không thay thế)

```yaml
# --- FVG (v0.1) — bổ sung cho 08 - Templates/Backtest templete.md ---
fvg_tf: M15                # khung của FVG
fvg_known_at: 2026-10-07T08:45   # close nến 3 (giờ sàn)
fvg_dir: bull              # bull | bear
fvg_size_atr: 0.54
fvg_c2_range_atr: 2.1
fvg_c2_body_pct: 0.78
fvg_pos_in_leg: 0.45
fvg_stacked_rank: 1        # 1 = first presented trong leg
fvg_dist_close_prox_atr: 0.12
fvg_broke_swing_level: 2
fvg_context: reversal      # reversal | continuation
fvg_pd_location: 0.31
fvg_sweep_before: true
fvg_news_window: false
fvg_session_gap: false
fvg_nested_in: H1          # none | M15 | H1 | D1
fvg_fss: 9                 # FVG Significance Score v0.1 (0–14)
fvg_entry_mode: CE_limit   # proximal_limit | CE_limit | M5_MSS
fvg_approach_speed: fast   # fast | grind (định nghĩa §39.3)
fvg_touch_count_actual: 1  # đếm trên LTF (v1 W3)
fvg_bars_to_touch: 7
fvg_max_depth: 0.62
fvg_state_final: REACTED   # REACTED | INVALIDATED | EXPIRED | FULL_FILLED | ...
fvg_invalidation_rule: I2  # I1..I6 (§19)
fvg_filled: true
fvg_missed_valid_setup: false
fvg_skipped_reason:        # vd grind_no_mss, news_window, rr_too_low
p_null: 0.33
excess: 0.67               # win(1/0) − p_null — tổng hợp ở dashboard
```

Trường `fvg_valid` hiện có trong template nên được định nghĩa lại là: *thỏa DEF-FVG-01 + min_size* (không kèm context), để dashboard tách được "FVG hợp lệ" khỏi "setup hợp lệ".

---

## 42. Giả thuyết kiểm chứng được (brief §47)

| Brief | ID | Giả thuyết | Biến | Phép thử chính | Bác bỏ nếu |
|---|---|---|---|---|---|
| H1 | **HYP-FVG-001** | FVG từ displacement mạnh hơn có xác suất reaction cao hơn | `c2_range_atr` | Reaction/excess theo quintile, so với control cùng quintile | Không đơn điệu, hoặc control cùng xu hướng |
| H2 | **HYP-FVG-003 / 020** | FVG mới / first touch tốt hơn FVG đã bị chạm | `touch_count`, `age_bars` | So sánh có kiểm soát khoảng cách | Hiệu ứng biến mất khi kiểm soát khoảng cách |
| H3 | **HYP-FVG-004** | FVG cùng chiều HTF tốt hơn ngược chiều | `htf_bias` | Excess theo nhóm | Chênh lệch ≤ CI |
| H4 | **HYP-FVG-005 / 008** | FVG gần liquidity liên quan (sau sweep, trên đường tới DOL) khác FVG đơn lẻ | `sweep_before`, `dist_to_dol_atr` | Ablation C vs B; control | C ≈ C₀ |
| H5 | **HYP-FVG-013** | Size tương đối ảnh hưởng hành vi | `size_atr` | Event study theo quintile | — (mô tả) |
| H6 | **HYP-FVG-006** | CE có giá trị dự báo hơn mức ngẫu nhiên trong vùng | `max_depth` | Điểm gãy tại 0.5 so với 1/(1+q) và mức 0.4/0.6 | Không có điểm gãy |
| H7 | **HYP-FVG-007** | FVG + MSS hơn FVG alone | `broke_swing_level` | Model C vs A, so control | C − C₀ ≈ A − A₀ |
| H8 | **HYP-FVG-008** | FVG + sweep + displacement hơn FVG alone | như trên | như trên | như trên |
| H9 | **HYP-FVG-009** | Hiệu quả FVG thay đổi theo regime | `trend_proxy`, `atr_pct` | Phân tầng | Ổn định qua regime (khi đó H9 bị bác bỏ — điều tốt) |
| H10 | **HYP-FVG-014** | Predictive value khác nhau theo khung | `fvg_tf` | Excess theo khung | — |
| — | **HYP-FVG-002** | FVG có reaction rate cao hơn vùng đối chứng cùng hình học | — | Matched control (Model A) | A ≈ A₀ |
| — | **HYP-FVG-010** | FVG HTF chưa lấp "hút" giá hơn mức ngẫu nhiên cùng khoảng cách | khoảng cách | P(chạm \| FVG, d) vs P(chạm \| control, d) | Bằng nhau |
| — | **HYP-FVG-011** | Vùng FVG là nơi giá *đi nhanh qua* (sổ mỏng), không phải hỗ trợ | tốc độ trong vùng | Thời gian/đơn vị giá khi retrace qua FVG vs control | — |
| — | **HYP-FVG-015** | Grind approach → tỷ lệ invalidation cao hơn fast tap | `approach_speed` | So sánh có kiểm soát depth | Không khác |
| — | **HYP-FVG-016** | Hiệu quả có điều kiện theo việc khớp (filled) kém hơn hiệu quả theo lúc hình thành (adverse selection) | `filled`, kết quả giả định của missed | So sánh filled vs missed | Không khác |
| — | **HYP-FVG-017** | FVG trong news window bị xuyên nhiều hơn | `news_window` | Event study | Không khác |
| — | **HYP-FVG-018** | FVG trong killzone tốt hơn (kiểm soát volatility) | `killzone`, `atr_pct` | Phân tầng | Hết hiệu ứng khi kiểm soát ATR |
| — | **HYP-FVG-019** | Độ sâu fill điển hình khác nhau theo symbol | `max_depth` theo symbol | Phân phối theo symbol | Giống nhau |
| — | **HYP-FVG-006c** | Phản ứng tập trung theo % của leg (⅓, ½) hơn là CE của FVG | `fvg_pos_in_leg` | So sánh các mức | — |
| — | **HYP-FVG-012** | FVG xác nhận bằng footprint (volume thấp trong vùng) tốt hơn | volume/level | Cần dữ liệu tick | — |

---

## 43. Cỡ mẫu, kiểm định, robustness

### 43.1 Cỡ mẫu — các con số cần biết trước khi bắt đầu **[MATHEMATICAL]**
α = 0.05 hai phía, power 80%:

| Mục tiêu phát hiện | Cỡ mẫu cần |
|---|---|
| Win rate hơn 1/3 (bracket 2R) +3 điểm % | **1,962** lệnh |
| … +5 điểm | **711** |
| … +8 điểm | **280** |
| … +10 điểm | **180** |
| FVG vs control chênh 3 điểm | **4,011** mỗi nhóm |
| … 5 điểm | **1,444** mỗi nhóm |
| … 8 điểm | **564** mỗi nhóm |
| Expectancy +0.1R (bracket 2R) | **1,641** lệnh |
| … +0.2R | **424** |
| … +0.3R | **193** |
| Với 10 giả thuyết (Bonferroni α = 0.005): +5 điểm | **1,201** |

Độ chính xác của một journal (win rate thật ~40%): **30 lệnh → ±17.5 điểm**; 50 → ±13.6; 100 → ±9.6; 300 → ±5.5 (95% CI).

→ Backtest tay 30–50 setup đủ để **phát hiện lỗi thô và sinh giả thuyết**; không đủ để chỉnh rule hay kết luận edge. Event study tự động trên nhiều năm dữ liệu M15 cho hàng chục nghìn FVG — đủ cho phần lớn câu hỏi.

### 43.2 Kiểm định
- **Đơn vị độc lập:** nhiều FVG trong cùng ngày không độc lập → bootstrap theo **khối ngày** (block bootstrap), hoặc lấy một setup/ngày.
- **So sánh tỷ lệ:** two-proportion z-test hoặc bootstrap cho excess; với expectancy, bootstrap phân phối R.
- **Tránh p-hacking:** khóa giả thuyết, tham số, metric trước (pre-registration trong vault: ghi vào `/ICT/16_Hypotheses/` trước khi chạy).

### 43.3 Đa kiểm định
Test 5 mức entry × 4 symbol × 3 session = 60 so sánh → ~3 kết quả "có ý nghĩa" ở α = 0.05 *chỉ do may rủi*. Dùng Holm–Bonferroni (kiểm soát FWER) hoặc Benjamini–Hochberg (FDR), và **xác nhận ngoài mẫu** mọi phát hiện.

### 43.4 Robustness & regime
1. **Chia mẫu theo thời gian:** in-sample (vd 60%) → out-of-sample (40%); hoặc walk-forward theo năm.
2. **Theo symbol, session, năm** — hiệu ứng thật thường không chỉ tồn tại ở một ô.
3. **Độ nhạy tham số:** min_size, k, m, buffer ±25% — kết quả phải không sụp đổ.
4. **Regime:** trend vs range (trend_proxy), ATR thấp/cao, trước/sau sự kiện cấu trúc thị trường (vd thay đổi giờ giao dịch, tick size).
5. **Chi phí:** spread theo giờ, commission, slippage stop.

### 43.5 Falsification — điều gì sẽ bác bỏ framework
Khai báo trước:
- Nếu **Model A ≈ A₀** và **C ≈ C₀** trên ≥ 2 symbol, ngoài mẫu → FVG không thêm giá trị so với vị trí cùng khoảng cách trong framework này; giữ FVG như *công cụ định vị/quản trị*, không như *bộ dự báo*.
- Nếu excess của setup đầy đủ (D) ≤ 0 sau chi phí, ngoài mẫu → playbook không có edge trong dạng hiện tại.
- Nếu kết quả tốt chỉ tồn tại với phân xử trên nến lớn hoặc khi sửa `j > i` thành `j ≥ i` → kết quả là artefact.

---

# PART XI — MÔ HÌNH TƯ DUY CUỐI CÙNG

## 44. Giải thích FVG cho một đứa trẻ 5 tuổi (brief §49)

![[FVG-Deep-22-Giai-Thich-5-Tuoi.svg|720]]
*FVG-Deep-22: Dấu chân trên hành lang — đi bộ để lại nhiều dấu chân trên mọi viên gạch; chạy vụt qua một đoạn chỉ để lại một dấu chân trên mỗi viên.*

**Câu đầu tiên (không thuật ngữ):** Khi con đi bộ trên hành lang, viên gạch nào cũng có nhiều dấu chân của con; nhưng nếu con bỗng chạy thật nhanh qua một đoạn, những viên gạch ở đoạn đó chỉ có đúng một dấu chân mỗi viên.

Rồi từng bước ánh xạ:

```text
Hành lang, viên gạch, dấu chân          (ẩn dụ)
        ↓  viên gạch = một mức giá; dấu chân = thời gian / giao dịch tại mức đó
Giá đi qua các mức                      (price movement)
        ↓  có lúc giá "chạy" rất nhanh theo một chiều
Displacement                            (một cây nến lớn hơn hẳn hai cây bên cạnh)
        ↓  so cây nến trước và cây nến sau cú chạy
Cấu trúc 3 nến                          (nến 1 — cú chạy — nến 3)
        ↓  đoạn mà nến 1 và nến 3 đều không chạm tới
FVG                                     (đoạn "thưa dấu chân": có đi qua, nhưng chỉ một lần, một chiều)
        ↓  giá có thể quay lại đoạn đó — thường là vì nó ở ngay phía sau
Retracement                             (quay lại — chuyện xác suất, không phải lời hứa)
        ↓  khi quay lại, giá có thể bật ra hoặc đi xuyên qua
Reaction / continuation  hoặc  Acceptance / invalidation
```

Và câu kết cho đứa trẻ: *"Con có quay lại đoạn hành lang đó không thì tùy vì sao con chạy: nếu con chạy vì quên đồ, con sẽ quay lại; nếu con chạy vì đã tới giờ ăn cơm, con sẽ không quay lại; còn nếu con chạy chỉ vì vui, thì ai mà biết."* — đó chính là ba loại displacement (§30.3) và null model.

### 44.1 Sáu cách giải thích cùng một khái niệm (brief Part XI)

| Cho ai | Giải thích |
|---|---|
| **Trẻ 5 tuổi** | Đoạn hành lang con chạy vụt qua — có đi qua, nhưng ít dấu chân. |
| **Người mới** | Ba cây nến liên tiếp; cây giữa rất dài; cây đầu và cây cuối không chạm nhau. Khoảng giữa chúng là FVG. Giá có thể quay lại đó — nhưng không phải lúc nào cũng vậy. |
| **Kỹ thuật** | Bullish FVG tại i ⇔ L[i] > H[i−2]; vùng [H[i−2], L[i]]; known_at = close i; size chuẩn hóa ATR; CE = trung điểm. |
| **Cơ chế** | Trong một khung nến, dòng lệnh chủ động một chiều vượt thanh khoản sẵn có và kịp bổ sung; vùng giá được đi qua một lần, ít thời gian. Tương lai của vùng phụ thuộc phần tác động là tạm thời hay vĩnh viễn, và dòng lệnh còn tiếp hay không. |
| **ICT** | BISI/SIBI — vùng price delivery một phía; PD array dùng làm điểm vào khi retrace sau sweep + displacement + MSS; CE là mức tham chiếu; thất bại → IFVG. |
| **Backtest** | Phát hiện bằng DEF-FVG-01; state machine §20; so với vùng đối chứng cùng hình học; Model A–D; ≥ vài trăm–vài nghìn mẫu; fill thực tế; ngoài mẫu. |

---

## 45. Tổng hợp — trả lời trực tiếp 15 câu hỏi (brief §50)

**1. FVG thực sự là gì?** Đoạn giá mà trong ba nến liên tiếp chỉ nến giữa đi qua — một vùng ít thời gian tại giá, được biết khi nến 3 đóng cửa (DEF-FVG-01).

**2. FVG không phải là gì?** Không phải vùng không có giao dịch, không phải bằng chứng của tổ chức, không phải liquidity, không phải OB, không phải POI tự thân, không phải tín hiệu vào lệnh, không phải lời hứa giá sẽ quay lại, không phải thực thể độc lập với khung thời gian (§5.9, §12).

**3. Tại sao FVG hình thành?** Hình học: nến giữa có chuyển động ròng lớn hơn các dao động ngược của hai nến bên cạnh. Cơ chế: bùng nổ dòng lệnh một chiều so với thanh khoản (§9).

**4. Market mechanics nào giải thích sự hình thành?** Order flow imbalance trên sổ lệnh có độ sâu hữu hạn (Cont et al. 2014; Kyle 1985); thanh khoản rút đi khi dòng lệnh "độc" (Easley et al. 2012); thông tin mới; metaorder (Lillo & Farmer 2004); stop cascade (Osler 2005); volatility clustering; và nhiễu (§9.3).

**5. Phần nào chỉ là ICT interpretation?** "Smart money / thuật toán để lại inefficiency", "rebalance", "delivery state", "intent", "kho lệnh dang dở", "CE là giá vốn của bên tạo gap", "FVG hút giá" (§9.5, §9.6).

**6. Tại sao giá đôi khi quay lại FVG?** Trước hết vì hình học (vùng ngay sau lưng giá; random walk hồi quy). Thêm vào đó có thể: tác động tạm thời phai, phần thưởng cho người cung cấp thanh khoản, short-term reversal, chốt lời, tự hiện thực hóa (§13).

**7. Tại sao đôi khi không quay lại?** Drift (trend), và dòng lệnh còn tiếp (metaorder) hoặc thông tin vĩnh viễn kéo giá đi xa (§15.2, §30.3).

**8. Tại sao FVG này được respect còn FVG kia bị phá?** Bốn nguồn: loại dòng lệnh tạo nến 2 (tạm thời / thông tin / metaorder), chế độ drift, định nghĩa "respect", và khớp lệnh — cộng thêm adverse selection của lệnh limit (§30).

**9. FVG có predictive value độc lập không?** Trên nhiễu: không (và không thể). Trên thị trường thật: **chưa biết** — chưa có bằng chứng công khai đạt chuẩn; cần Model A vs A₀ (§40).

**10. FVG cần context gì để meaningful?** Theo framework: D1 hypothesis + DOL, POI đúng P/D, liquidity event, MSS có ý nghĩa, killzone. Về thực nghiệm: mỗi yếu tố là một giả thuyết đóng góp (HYP-FVG-004/007/008/018); context có giá trị khi nó là proxy đo được trước của drift hoặc loại dòng lệnh (§30.1).

**11. FVG có thể dùng như POI không?** HTF FVG có thể được *chọn* làm POI hoặc location bên trong POI — đó là quyết định của người phân tích (§24.2).

**12. FVG có phải entry signal không?** Không. FVG là *nơi*; entry cần *khi nào* (trigger: limit tại mức khai báo trước, hoặc M5 MSS trong FVG) (§24).

**13. FVG liên hệ thế nào với Liquidity, MSS, Displacement, DOL, Dealing Range?** Liquidity event có thể là nguyên nhân/bối cảnh của nến 2; displacement là chuyển động mà FVG là dấu vết; MSS là hậu quả cấu trúc (độc lập với FVG về định nghĩa); dealing range cho location và R:R; DOL cho hướng và vai trò của FVG (entry / continuation / vật cản / target) (§22–26).

**14. FVG có thể định nghĩa đủ objective để backtest không?** **Có** — DEF-FVG-01..07, state machine §20, quy tắc §41. Phần không định nghĩa được (ý định, "smart money") cũng không cần cho backtest.

**15. Phần nào vẫn là hypothesis?** Gần như mọi claim về *giá trị dự báo*: FVG hơn đối chứng, CE đặc biệt, first touch tốt hơn, displacement mạnh tốt hơn, sau sweep tốt hơn, killzone tốt hơn, HTF tốt hơn, FVG hút giá, grind xấu hơn fast tap (§42).

---

## 46. Mô hình tri thức cuối cùng (brief §51)

![[FVG-Deep-21-Mo-Hinh-Tu-Duy.svg|720]]
*FVG-Deep-21: Bên trái — chuỗi cơ chế có thể; bên phải — vị trí của FVG trong D1 → H1 → M5.*

```text
                         THỊ TRƯỜNG (lệnh chờ + lệnh chủ động)
                                      │
                                      ↓
                             PRICE DISCOVERY (giá dịch tới nơi có đối ứng)
                                      │
                                      ↓
            DÒNG LỆNH MỘT CHIỀU MẠNH  — vì: thông tin | thanh khoản | metaorder | stop cascade | nhiễu
                                      │
                                      ↓
                          DISPLACEMENT (nến lớn so với ATR)
                                      │
                                      ↓
                      ┌──────────────────────────────────┐
                      │  HÌNH HỌC 3 NẾN: L₃ > H₁ (bull)   │   known_at = close nến 3
                      └──────────────────────────────────┘
                                      │
                                      ↓
                                     FVG
                                      │
                    ┌─────────────────┴─────────────────┐
                    ↓                                   ↓
            KHÔNG RETRACE                          RETRACE  (hình học + transient impact)
        (drift / metaorder: lỡ tàu)                     │
                                         ┌─────────────┴─────────────┐
                                         ↓                           ↓
                                     REACTION                    ACCEPTANCE
                                  (≥ k·ATR trong m nến)        (close ngoài distal)
                                         │                           │
                                         ↓                           ↓
                              CONTINUATION / REVERSAL         INVALIDATION / IFVG
```

Đặt vào framework ICT:

```text
D1 ── Context ── Dealing Range ── Liquidity ── DOL ── HTF FVG (location / draw)
 │
 ↓
H1 ── Structure ── Liquidity event ── POI ── H1 FVG (setup, trên leg phá cấu trúc)
 │
 ↓
M5 ── Sweep ── MSS ── Displacement ── M5 FVG ── Execution (trigger, stop, invalidation)
```

> [!important] Nhấn mạnh cuối cùng
> **Đây là framework nghiên cứu và mô hình giao dịch, không phải định luật nhân quả của thị trường.** Mũi tên trong sơ đồ là *trình tự mô tả*, không phải *lực*. Mỗi mũi tên có thể sai; mỗi mũi tên có một phép thử.

### 46.1 Ba câu trader phải trả lời được khi nhìn một FVG (brief §54)
1. **Tôi đang nhìn thấy gì?** — Ba nến; vùng [distal, proximal]; size/ATR; known_at; vị trí trong leg, range, so với DOL.
2. **Tôi biết gì / chưa biết gì?** — Biết: hình học, thời điểm, context đã có known_at. Chưa biết: ai giao dịch, cú đẩy là loại nào, giá có quay lại không.
3. **Điều gì phải xảy ra tiếp để hypothesis được xác nhận — và điều gì bác bỏ nó?** — Xác nhận: reaction ≥ k·ATR trong m nến sau touch (hoặc M5 MSS trong FVG). Bác bỏ: close cùng khung ngoài distal; swing bảo vệ bị phá; hết hạn; context đổi.

---

## 47. Tự kiểm tra, Flashcards, Lesson Learned, Mức độ thành thạo

### 47.1 Câu hỏi tự kiểm tra *(v1 §10, nguyên văn)*

- Mình có giải thích được FVG (BISI/SIBI) và cấu trúc 3 nến trong 30 giây không?
- FVG này sinh ra từ displacement phá cấu trúc hay chỉ là gap giữa range?
- Mức CE (50%) của FVG nằm ở đâu? Giá đang respect hay xuyên qua nó?
- FVG đang ở premium hay discount của **dealing range nào**?
- Liquidity đã bị sweep trước khi FVG hình thành chưa?
- FVG đang đóng vai POI để entry hay DRAW để làm target?
- Điều gì làm FVG này invalid, và nếu invalid thì IFVG sẽ ở đâu?
- FVG này có đồng hướng Daily Bias không?
- Nếu mình không trade FVG này, lý do "No Trade" là gì?
- Setup nào trong trade journal đã dùng FVG đúng/sai context?
- *(bổ sung)* FVG trên chart nến thực ra đo cái gì trên order book thật — và vì sao nó "biến mất" khi đổi timeframe?
- *(bổ sung)* Vì sao CE gần với vùng giá trung bình của dealer/market maker hơn là mép gap?
- *(bổ sung)* Điểm yếu lớn nhất của FVG khi soi bằng tiêu chuẩn khoa học/quant là gì, và phần nào trong đó không thể khắc phục?
- *(bổ sung)* Vì sao một FVG đạt đủ 5/5 tiêu chí checklist vẫn có thể thua — case nào minh họa rõ nhất?

### 47.2 Câu hỏi chẩn đoán (v2)
1. Chứng minh trong 3 dòng vì sao nến 2 đi qua toàn bộ vùng FVG. Khi nào chứng minh này không còn đúng?
2. Trên random walk, bao nhiêu % FVG bị chạm trong 20 nến? Vì sao con số này quan trọng khi ai đó nói "giá đã quay lại FVG"?
3. "CE giữ được 31% số lần chạm" — đây là edge hay hình học? Bạn cần thấy gì để nói CE đặc biệt?
4. Bạn code `touched = low[j] <= proximal for j in range(i, i+20)`. Lỗi ở đâu và nó làm win rate thay đổi thế nào?
5. Vì sao lọc "displacement mạnh" có thể làm kết quả *tệ hơn*? Bạn sẽ đo điều đó trên dữ liệu thật bằng cách nào?
6. Ba loại displacement là gì? Biến nào đo được trước có thể là proxy cho từng loại?
7. Một FVG H1 "được xác nhận bởi liquidity void M5" — vì sao câu này gần như không mang thông tin?
8. Viết DEF-FVG-03 của bạn. Một nến M1 xuyên distal của H1 FVG — FVG còn hiệu lực không?
9. Thiết kế vùng đối chứng cho một bullish FVG M15 cụ thể trong journal của bạn.
10. Cần bao nhiêu lệnh để phát hiện excess +5 điểm so với 1/3? Journal hiện tại của bạn có bao nhiêu?

### 47.3 Flashcards *(v1 §11, nguyên văn)*

#### Q1
**Hỏi:** Fair Value Gap được tạo bởi mấy nến, và bullish FVG nằm ở đâu?  
**Đáp:** 3 nến. Bullish FVG (BISI) là khoảng trống giữa HIGH của nến 1 và LOW của nến 3, với nến 2 là displacement tăng mạnh (single-sided delivery).

#### Q2
**Hỏi:** BISI và SIBI nghĩa là gì?  
**Đáp:** BISI = Buyside Imbalance Sellside Inefficiency (bullish FVG). SIBI = Sellside Imbalance Buyside Inefficiency (bearish FVG).

#### Q3
**Hỏi:** CE (Consequent Encroachment) là gì và vì sao quan trọng?  
**Đáp:** CE là mức 50% của gap — mức phản ứng quan trọng nhất. Giá thường tôn trọng CE; entry tối ưu thường nằm quanh CE và CE dùng để xác nhận FVG đang được respect.

#### Q4
**Hỏi:** FVG đóng vai trò kép nào trong ICT?  
**Đáp:** (1) POI để vào lệnh khi giá retrace về FVG; (2) DRAW — giá bị hút về để lấp/rebalance imbalance còn mở.

#### Q5
**Hỏi:** Inversion FVG (IFVG) là gì?  
**Đáp:** Khi một FVG bị giá đóng nến xuyên thủng qua, nó đảo cực tính: bullish FVG fail → thành kháng cự bearish; bearish FVG fail → thành hỗ trợ bullish.

#### Q6
**Hỏi:** Điều gì phân biệt một FVG chất lượng cao với một FVG yếu?  
**Đáp:** FVG tốt sinh ra từ displacement PHÁ CẤU TRÚC (BOS/MSS) có chủ đích, nằm tại POI HTF, đúng premium/discount, đồng hướng bias và sau liquidity sweep. FVG nhỏ giữa range, không displacement = yếu.

#### Q7
**Hỏi:** Phân biệt "respect" và "invalidation" của một FVG?  
**Đáp:** Respect = giá chạm CE / mép gap rồi reject (kể cả full fill rồi quay đầu). Invalidation = giá đóng nến xuyên qua và giữ giá ngoài FVG → FVG hết hiệu lực, có thể đảo thành IFVG.

#### Q8
**Hỏi:** Tại sao KHÔNG nên trade mọi FVG?  
**Đáp:** Phần lớn FVG là nhiễu giữa range, không có edge. Chỉ FVG tại POI HTF, đúng context bias, đúng premium/discount và sau sweep mới có xác suất cao.

### 47.4 Flashcards bổ sung (v2)

#### Q9
**Hỏi:** FVG có phải là vùng "không có giao dịch" không?
**Đáp:** Không. Trong thị trường liên tục, Open₂ ≤ H₁ và Close₂ ≥ L₃ ⇒ nến 2 đi qua toàn bộ vùng. FVG là vùng chỉ *một* nến đi qua — ít thời gian, một chiều. Ngoại lệ: session gap, halt, news spike.

#### Q10
**Hỏi:** Trên random walk có bao nhiêu FVG / 100 nến?
**Đáp:** ~31 (mọi kích thước); ~20 (≥ 0.25 ATR); ~12 (≥ 0.5 ATR). Sự xuất hiện của FVG không mang thông tin.

#### Q11
**Hỏi:** "Gap nào cũng được lấp" — đúng hay sai?
**Đáp:** Trên random walk không drift: đúng *cuối cùng* (97% trong 2000 nến) — vì random walk hồi quy. Vì vậy câu này không phân biệt FVG với vùng bất kỳ. Có drift: FVG cùng chiều trend thường không bị chạm.

#### Q12
**Hỏi:** Công thức hình học cho P(giá đi sâu hơn q·size trước khi bật 1·size) sau khi chạm?
**Đáp:** 1/(1+q). Tại CE (q = 0.5): 2/3 đi sâu hơn → "giữ ở CE" 1/3 chỉ do hình học. Không có điểm gãy tại 0.5.

#### Q13
**Hỏi:** Ba loại displacement trong toy model và số phận FVG của chúng?
**Đáp:** Liquidity (tác động tạm thời) — 77% bị close xuyên; information (nhảy vĩnh viễn) — 33%; metaorder (dòng lệnh tiếp tục) — 13%, 51% không bao giờ bị chạm.

#### Q14
**Hỏi:** Adverse selection của lệnh limit tại FVG là gì?
**Đáp:** Lệnh limit được khớp nhiều nhất khi giá thực sự đảo ngược (liquidity-type) và ít khi khớp khi dòng lệnh còn tiếp (metaorder). Toy model: 31% liquidity lúc hình thành → 49% trong các lệnh được khớp.

#### Q15
**Hỏi:** Bug look-ahead phổ biến nhất khi backtest FVG?
**Đáp:** Coi low của nến 3 (chính là proximal) là lần chạm đầu → vào lệnh tại cực trị nến 3. Trên random walk: win 32% → 65%, E[R] −0.05 → +0.96.

#### Q16
**Hỏi:** Tại close nến 2, gap tạm thời 0.27 ATR có bao nhiêu % trở thành FVG?
**Đáp:** ~36% trên random walk (công thức 2Φ(g/σ) − 1). Tổng thể chỉ ~48% gap tạm thời sống sót qua nến 3.

#### Q17
**Hỏi:** "Fair value" trong FVG có phải fair value kinh tế học không?
**Đáp:** Không. ICT dùng "fair" cho giá được chào hai phía; FVG là đoạn chỉ được chào một phía. Không phải tuyên bố định giá.

#### Q18
**Hỏi:** Vì sao "FVG kề OB" không phải hai yếu tố confluence độc lập trong mẫu kinh điển?
**Đáp:** Vì nến 1 của FVG thường chính là OB → distal FVG = High OB theo cấu tạo.

#### Q19
**Hỏi:** Câu hỏi đúng để biết FVG có giá trị là gì?
**Đáp:** FVG có xác suất phản ứng / expectancy cao hơn **vùng đối chứng cùng hướng, cùng khoảng cách, cùng size, cùng context** không — ngoài mẫu, sau chi phí?

#### Q20
**Hỏi:** Cần bao nhiêu lệnh để phát hiện win rate hơn 1/3 thêm 5 điểm?
**Đáp:** ~711 (α = 0.05, power 80%). FVG vs control chênh 5 điểm: ~1,444 mỗi nhóm. 30 lệnh cho CI ±17.5 điểm.

### 47.5 Lesson Learned *(v1 §12, nguyên văn)*

#### Bài học chính
- FVG là **điểm tham chiếu giá / price inefficiency**, không phải tín hiệu trade độc lập.
- FVG chất lượng phải có **intent**: sinh ra từ displacement phá cấu trúc, không phải gap ngẫu nhiên.
- **CE (50%)** là mức quan trọng nhất: entry quanh CE cải thiện R:R và là mức để đo respect/invalidation.
- FVG có vai trò kép — biết rõ mình đang dùng nó làm **POI để entry** hay **DRAW để target**.
- Khi FVG bị đóng nến xuyên qua, nó **đảo cực thành IFVG** — đừng cố giữ lệnh ngược.
- Không trade mọi FVG; chỉ FVG đúng bias + premium/discount + sau sweep mới đáng vào.

#### Quy tắc cá nhân rút ra
- [ ] Tôi không gọi một gap là "FVG đáng trade" nếu nến giữa không phải displacement phá cấu trúc.
- [ ] Tôi chỉ Long ở FVG discount và Short ở FVG premium, đồng hướng Daily Bias.
- [ ] Tôi luôn chờ liquidity sweep TRƯỚC khi vào lệnh tại FVG.
- [ ] Tôi ưu tiên entry quanh CE và đặt stop ngoài đầu kia của FVG / ngoài điểm sweep.
- [ ] Khi FVG bị đóng nến xuyên qua, tôi chuyển tư duy sang IFVG thay vì cố giữ lệnh cũ.
- [ ] Khi nhiều FVG chồng chéo, tôi chỉ chọn cái trùng POI HTF / có confluence rõ nhất.

#### Câu nhắc nhở khi trade
> **"FVG không phải là lệnh — nó là nơi tôi chờ. Chỉ vào khi displacement có chủ đích, đúng premium/discount, sau sweep, và giá respect CE."**

### 47.6 Bài học bổ sung từ nghiên cứu v2
- FVG **mô tả chắc chắn**, **dự báo chưa chứng minh**. Giữ hai điều này tách biệt trong mọi ghi chép.
- "Giá quay lại FVG" trước hết là **khoảng cách + thời gian**; đừng coi nó là bằng chứng.
- Câu hỏi có giá trị nhất về một FVG không phải "nó đẹp không" mà là **"cú đẩy tạo ra nó thuộc loại nào, và mình có proxy đo được trước không?"**
- Lệnh limit thụ động có **adverse selection** — hãy đo kết quả của cả setup không được khớp.
- Một backtest FVG không ghi rõ **known_at** và **độ phân giải phân xử** không đáng tin — kể cả backtest của mình.

### 47.7 Quy tắc cá nhân bổ sung (v2)
- [ ] Tôi chỉ đánh dấu FVG sau khi nến 3 đóng cửa, và ghi known_at.
- [ ] Tôi chọn FVG theo quy tắc khai báo trước, không chọn "cái đẹp nhất" sau khi giá phản ứng.
- [ ] Tôi ghi `approach_speed` và rút limit khi giá grind vào FVG mà không có LTF MSS.
- [ ] Tôi ghi mọi setup không khớp / bị bỏ, kèm lý do.
- [ ] Tôi không chỉnh rule FVG khi chưa có vài trăm mẫu và kiểm định ngoài mẫu.

### 47.8 Mức độ thành thạo *(v1 §13, nguyên văn — có bổ sung v2)*

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt BISI/SIBI, CE, và vai trò POI vs DRAW không? |
| Nhận diện trên chart |  | Có xác định đúng 3 nến, gap thật và mức CE không? |
| Biết khi nào bỏ qua |  | Có dám bỏ FVG giữa range / không displacement / ngược bias không? |
| Kết hợp với context HTF |  | FVG có được đặt trong narrative bias + premium/discount + sweep không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra quanh CE sau sweep + displacement không? |
| Review sau trade |  | Có kiểm tra chất lượng FVG bằng dữ liệu journal thay vì cảm xúc không? |

**Kế hoạch review tiếp theo:**  
- [ ] Thu thập tối thiểu 20–30 setup có gắn tag `[[13-FVG-Fair-Value-Gap|Fair Value Gap]]`.
- [ ] Review riêng: FVG có displacement vs không; entry tại CE vs mép gap; FVG sau sweep vs trước sweep.
- [ ] Thống kê win rate, average R, lỗi lặp lại theo `fvg_from_displacement` và `entry_relative_to_ce`.
- [ ] Cập nhật rule chỉ khi dữ liệu backtest/forward test đủ mẫu.

| Tiêu chí bổ sung (v2) | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Phân biệt mô tả / cơ chế / ICT / giả thuyết |  | Có gắn nhãn đúng các câu trong journal? |
| Nắm đường nền hình học |  | Nhớ được tỷ lệ chạm/lấp trên random walk và công thức 1/(1+q)? |
| Backtest không look-ahead |  | Code/quy trình có known_at, `j > i`, phân xử khung nhỏ? |
| Dùng vùng đối chứng |  | Đã từng so FVG với control trên dữ liệu của mình? |

---

## 48. Registers — Definitions, Rules, Hypotheses, câu hỏi nghiên cứu

### 48.1 Definitions Register (v0.1)

| ID | Tên | Định nghĩa | Mục |
|---|---|---|---|
| **DEF-FVG-01** | Fair Value Gap | Bull: L[i] > H[i−2]; Bear: H[i] < L[i−2]; vùng, proximal, distal, CE, size_atr; known_at = close i | §5.7 |
| **DEF-FVG-02** | Touch / fill depth | touch = wick chạm proximal; depth = (proximal − cực trị)/size; CE = depth ≥ 0.5; full = depth ≥ 1 | §14.1 |
| **DEF-FVG-03** | Invalidation / expiry | Close cùng khung ngoài distal; expire 48 nến (LTF) | §19.2 |
| **DEF-FVG-04** | Reaction | Sau touch, rời proximal ≥ k·ATR (k = 1.0) trong m = 6 nến | §17.2 |
| **DEF-FVG-05** | Liquidity void | Leg ≥ 2 nến một chiều có ≥ 2 FVG liên tiếp cùng chiều | §12.3 |
| **DEF-FVG-06** | Control zone | Vùng cùng hướng, khoảng cách, size (ATR), session, ATR & trend quintile, tại nến không có FVG | §41.4 |
| **DEF-FVG-07** | State machine | PROVISIONAL → ACTIVE → TOUCHED → CE → FULL → {REACTED, INVALIDATED → INVERTED, EXPIRED}; chuyển tại close; append-only | §20.3 |

### 48.2 Rules Register — OLD / NEW (project §29)

> [!note] Không rule nào của v1 bị xóa. Thay đổi dưới đây là *cách phát biểu và trạng thái bằng chứng*.

| ID | OLD (v1) | NEW (v0.1) | REASON | EXPECTED EFFECT | BACKTEST? |
|---|---|---|---|---|---|
| RULE-FVG-01 | "Nến giữa là displacement" là điều kiện bắt buộc của FVG | FVG theo DEF-FVG-01; displacement là biến `c2_range_atr` và điều kiện *lọc* (S1) | Tách định nghĩa khỏi bộ lọc để kiểm định được HYP-FVG-001 | Không đổi thực hành; journal ghi thêm biến | Có |
| RULE-FVG-02 | "Chỉ trade FVG đạt 4/5 tiêu chí" | FSS v0.1 (0–14), 3 bậc; báo cáo từng thành phần | Khai báo rõ, tránh đếm trùng | Ít "lách" tiêu chí sau sự kiện | Có |
| RULE-FVG-03 | "Entry mặc định tại CE" | Giữ; thêm biến thể E1/E3 và quy tắc rút limit khi grind | Adverse selection (§30.4); W2 | Ít lệnh thua kiểu Case 2 (giả thuyết) | Có — HYP-FVG-015/016 |
| RULE-FVG-04 | "Invalidation khi đóng nến xuyên qua toàn bộ FVG" | DEF-FVG-03: close **cùng khung** ngoài distal; stop = distal − max(0.1·ATR, spread) | Chuẩn hóa; tách trạng thái khỏi stop | Không đổi; rõ hơn | Không (định nghĩa) |
| RULE-FVG-05 | "Sau 30+ mẫu mới đủ dữ liệu chỉnh rule" | 30–50 mẫu: phát hiện lỗi & sinh giả thuyết; chỉnh rule cần ≥ vài trăm mẫu + ngoài mẫu | Power analysis (§43.1) | Ít thay đổi rule theo nhiễu | — |
| RULE-FVG-06 | "First touch đáng tin nhất; từ lần 3 coi như cạn" | Giữ như HEURISTIC; đếm `touch_count_actual` trên LTF | Chưa kiểm chứng; W3 | — | Có — HYP-FVG-020 |
| RULE-FVG-07 | (v1 W1) FVG trong news ±2 phút mặc định không làm POI | Mở rộng thành `news_window` ±5 phút, cờ Disqualifying | Nhất quán EC3 | — | Có — HYP-FVG-017 |
| RULE-FVG-08 | (mới) | FVG chỉ được đánh dấu sau close nến 3; backtest touch từ nến i+1 | Look-ahead (FVG-Sim-05) | Loại "edge ảo" | — |
| RULE-FVG-09 | (mới) | Chọn FVG theo quy tắc khai báo trước (first presented hoặc discount-of-leg) | Hindsight | — | Có (so sánh 2 quy tắc) |
| RULE-FVG-10 | (mới) | Ghi setup không khớp + kết quả giả định | Đo adverse selection | — | Có — HYP-FVG-016 |

### 48.3 Hypothesis Register
Tất cả HYP-FVG-001 … 020 (§42) có trạng thái **UNTESTED**. Không có giả thuyết nào ở trạng thái SUPPORTED. Kết quả mô phỏng chỉ xác định **đường nền** (null) cho các phép thử.

### 48.4 Câu hỏi nghiên cứu — ưu tiên cho giai đoạn foundation
1. **(Rẻ nhất, giá trị nhất)** Event study Model A vs A₀ trên M15 của 1–2 symbol, 3+ năm dữ liệu: FVG có khác vùng đối chứng về P(reaction), max_depth, P(invalidation) không? (HYP-FVG-002)
2. Phân phối `max_depth` theo symbol — có điểm gãy tại CE không? (HYP-FVG-006, 019)
3. Trong journal/backtest tay hiện có: tỷ lệ `approach_speed = grind` trong lệnh thua vs thắng (HYP-FVG-015) — dùng làm giả thuyết, không kết luận.
4. Model C vs C₀ khi đã có thuật toán swing/range/sweep chuẩn hóa (HYP-FVG-007/008).
5. Filled vs missed — đo adverse selection (HYP-FVG-016).

### 48.5 Liên kết trong vault

| Loại | Liên kết |
|---|---|
| Nền tảng | [[50-Displacement-In-Depth]] · [[19-Liquidity]] · [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[12-Dealing-Range]] · [[27-Premium-Discount]] |
| Họ FVG | [[10-Consequent-Encroachment-Mean-Threshold]] · [[14-Implied-Fair-Value-Gap]] · [[17-Inverse-Fair-Value-Gap-iFVG]] · [[46-Reaper-Inversion-Fair-Value-Gap]] · [[48-1st-Presented-Fair-Value-Gap]] · [[03-Balanced-Price-Range]] · [[47-Redelivered-Rebalanced-Price-Range]] · [[21-Liquidity-Void]] · [[29-Sell-side-Imbalance-Buy-side-Inefficiency]] · [[06-Breakaway-Gap]] · [[23-New-Day-Opening-Gap]] · [[24-New-Week-Opening-Gap]] |
| Bối cảnh | [[59-Daily-Bias]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]] · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] · [[25-OB-Order-Block]] · [[55-Order-Block-OB-Nghien-cuu-chuyen-sau-Selection-Hierarchy-Backtest]] · [[18-Kill-Zones]] · [[26-OTE-Optimal-Trade-Entry]] |
| Model | [[01 - ICT 2022 Model\|ICT 2022 Model]] · [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]] · [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]] |
| Mistakes | [[10-Mistake-FVG-Not-Valid]] · [[08-Mistake-Weak-Displacement]] · [[02-Mistake-Enter-before-liquidity-sweep]] · [[04-Mistake-FOMO-Entry]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[12-Mistake-Log-Data-Mismatch-Backtest]] |

**Nơi lưu register (theo cấu trúc Claude Project):** DEF-FVG/RULE-FVG → `/ICT/17_Rules/`; HYP-FVG → `/ICT/16_Hypotheses/`; event/trade study → `/ICT/13_Backtesting/`; Case H-1/H-2 → `/ICT/14_Case_Studies/` (tag `hypothetical`).

---

## Tài liệu tham khảo

**Market microstructure & bằng chứng thực nghiệm (Tier 1–2)**

- Bershova, N., & Rakhlin, D. (2013). *The non-linear market impact of large trades: evidence from buy-side order flow.* Quantitative Finance, 13(11), 1759–1778.
- BIS Markets Committee (2017). *The sterling 'flash event' of 7 October 2016.* Bank for International Settlements. https://www.bis.org/publ/mktc09.htm
- Campbell, J. Y., Grossman, S. J., & Wang, J. (1993). *Trading Volume and Serial Correlation in Stock Returns.* Quarterly Journal of Economics, 108(4), 905–939.
- Caporale, G. M., & Plastun, A. (2017). *Price gaps: Another market anomaly?* Investment Analysts Journal, 46(4), 279–293. https://essuir.sumdu.edu.ua/handle/123456789/65434 *(về opening gap theo ngày, không phải FVG)*
- Cont, R., Kukanov, A., & Stoikov, S. (2014). *The Price Impact of Order Book Events.* Journal of Financial Econometrics, 12(1), 47–88.
- Easley, D., López de Prado, M. M., & O'Hara, M. (2012). *Flow Toxicity and Liquidity in a High-frequency World.* Review of Financial Studies, 25(5), 1457–1493.
- Fama, E. F. (1970). *Efficient Capital Markets: A Review of Theory and Empirical Work.* Journal of Finance, 25(2), 383–417.
- Farmer, J. D., Gerig, A., Lillo, F., & Waelbroeck, H. (2013). *How efficiency shapes market impact.* Quantitative Finance, 13(11). https://arxiv.org/pdf/1102.5457 — fair pricing condition; impact vĩnh viễn ≈ 2/3 đỉnh; trích Moro et al. (0.51 / 0.69) và Bershova & Rakhlin (≈ 2/3).
- Garzarelli, F., Cristelli, M., Pompa, G., Zaccaria, A., & Pietronero, L. (2014). *Memory effects in stock price dynamics: evidences of technical trading.* Scientific Reports, 4, 4487.
- Glosten, L. R., & Milgrom, P. R. (1985). *Bid, ask and transaction prices in a specialist market with heterogeneously informed traders.* Journal of Financial Economics, 14(1), 71–100.
- Grossman, S. J., & Miller, M. H. (1988). *Liquidity and Market Structure.* Journal of Finance, 43(3), 617–633.
- Jegadeesh, N. (1990). *Evidence of Predictable Behavior of Security Returns.* Journal of Finance, 45(3), 881–898.
- Kyle, A. S. (1985). *Continuous Auctions and Insider Trading.* Econometrica, 53(6), 1315–1335.
- Lehmann, B. N. (1990). *Fads, Martingales, and Market Efficiency.* Quarterly Journal of Economics, 105(1), 1–28.
- Lillo, F., & Farmer, J. D. (2004). *The Long Memory of the Efficient Market.* Studies in Nonlinear Dynamics & Econometrics, 8(3).
- Llorente, G., Michaely, R., Saar, G., & Wang, J. (2002). *Dynamic Volume-Return Relation of Individual Stocks.* Review of Financial Studies, 15(4), 1005–1047.
- Moro, E., Vicente, J., Moyano, L. G., Gerig, A., Farmer, J. D., Vaglica, G., Lillo, F., & Mantegna, R. N. (2009). *Market impact and trading profile of hidden orders in stock markets.* Physical Review E, 80, 066102.
- Nagel, S. (2012). *Evaporating Liquidity.* Review of Financial Studies, 25(7), 2005–2039.
- Osler, C. L. (2003). *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.* Journal of Finance, 58(5), 1791–1819.
- Osler, C. L. (2005). *Stop-loss orders and price cascades in currency markets.* Journal of International Money and Finance, 24(2), 219–241.

**Toán, phương pháp, nhận thức**

- Pólya, G. (1921). *Über eine Aufgabe der Wahrscheinlichkeitsrechnung betreffend die Irrfahrt im Straßennetz.* Mathematische Annalen, 84, 149–160 (tính hồi quy của random walk).
- Fischhoff, B. (1975). *Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty.* Journal of Experimental Psychology: Human Perception and Performance, 1(3).
- IASB (2011). *IFRS 13 — Fair Value Measurement.*
- (Đa kiểm định, data snooping, overfitting: xem references của [[59-Daily-Bias]] và [[20-Liquidity-Sweep]].)

**Auction Market Theory & trading literature (Tier 3)**

- Steidlmayer, J. P., & Koy, K. (1986). *Markets and Market Logic.* Porcupine Press.
- Dalton, J. F., Jones, E. T., & Dalton, R. B. (1990; rev. 2007). *Mind Over Markets.* Wiley.
- ATAS (2020). *Analyzing TPO: 5 important elements in Jim Dalton's opinion.* https://atas.net/volume-analysis/basics-of-volume-analysis/analyzing-tpo-5-important-elements-in-jim-daltons-opinion (single prints)
- Rhea, R. (1932). *The Dow Theory.* Barron's (secondary reactions ⅓–⅔).

**ICT & tài liệu cộng đồng (Tier 3–4 — chỉ dùng cho định nghĩa/cách dùng, không phải bằng chứng)**

- ICT Mentorship Core Content — Month 04 — *ICT Fair Value Gaps (FVG)* — trích qua bản tóm tắt transcript: https://videohighlight.com/v/FgacYSN9QEo
- LuxAlgo — *Fair Value Gap* (định nghĩa công cụ; ví dụ cho câu "untraded span"): https://www.luxalgo.com/library/concept/fair-value-gap/
- Kondapally, A. — *Quantifying Fair Value Gaps: A Novel Metric for Price Reaction Prediction in Financial Markets*, SSRN (preprint, chưa bình duyệt; **không truy cập được nội dung** trong phiên này — không trích kết quả).

**Tài liệu nội bộ**

- Note v1 của chính file này (sao lưu: `Claude outputs/backups/13-FVG-Fair-Value-Gap.2026-10-07.md.bak`).
- [[20-Liquidity-Sweep]] v2 — quy ước nhãn, known_at, p_null, hệ thống LS-Sim.
- [[59-Daily-Bias]] v2 · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] · Claude Project: `ICT/02_Liquidity/Liquidity Sweep — Deep Research v0.1`, `ICT/03_Dealing_Range/…`.

---

## Phụ lục A — Ghi chú mô phỏng

| Figure | Mô hình | Kích thước | Kết quả chính |
|---|---|---|---|
| **FVG-Sim-01** | RW Gaussian / Student-t(3) / GARCH(1,1) (α = 0.06, β = 0.93), bước 1 phút, nến 15 bước; aggregation 5/15/60/240 bước (Gaussian) | 3,000,000 bước mỗi mô hình (200,000 nến) | FVG/100 nến (mọi size / ≥ 0.1 / ≥ 0.25 / ≥ 0.5 ATR): Gaussian 30.9 / 26.1 / 19.8 / 11.8; t(3) 33.7 / 28.7 / 22.4 / 14.0; GARCH 30.9 / 25.9 / 19.5 / 11.5. Size trung vị 0.37 / 0.40 / 0.36 ATR. P(FVG \| nến 2 ≥ 2 ATR) 88% / 87% / 72%; P(FVG \| nến 2 < 1 ATR) 17% / 20% / 20%. 78% / 72% / 75% FVG có nến 2 < 1.5 ATR. Aggregation: 37.9 / 30.9 / 26.5 / 24.7 |
| **FVG-Sim-02** | RW Gaussian bước 1 phút, nến 15 bước, FVG ≥ 0.1 ATR; Panel C thêm drift 0 / 0.05 / 0.10 / 0.20 ATR/nến | 3,000,000 bước mỗi lần; n = 51,902 FVG (driftless) | Chạm/CE/full/close-beyond trong 1, 3, 10, 20, 100, 500, 2000 nến (bảng §13.3); P(chạm 20 nến) vs khoảng cách khớp 2(1 − Φ(d/σ√T)); drift 0.2: 39% FVG cùng chiều không chạm (500 nến), ngược chiều 0%; 45,327 vs 13,172 FVG |
| **FVG-Sim-03** | **TOY MODEL**: RW σ = 1/phút + sốc Poisson 1/600 phút, size U(10, 25), ramp 6 phút; liquidity (tạm thời, τ = 60 phút), information (vĩnh viễn), metaorder (vĩnh viễn + 0.8× trong 120 phút), xác suất 1/3; run 2: φ ~ U(0, 1); nến 15 phút; cửa sổ 16 nến | 3,000,000 phút mỗi run; 1,368 / 1,433 / 1,454 FVG có nhãn + 52,577 noise | Close xuyên distal: 77% / 33% / 13% / 60%; không chạm: 3% / 22% / 51% / 20%; size trung vị 1.40 / 1.80 / 1.89 / 0.44 ATR. Run 2: close xuyên 76% (φ ≈ 0.06) → 40% (φ ≈ 0.94) |
| **FVG-Sim-04** | Bước 10 giây (σ phút = 1), nến 15 phút, FVG ≥ 0.25 ATR; limit CE 20 nến; stop distal ± 0.1 ATR; target 2R; p_null từ giá tại bước khớp; control cùng hình học tại nến ngẫu nhiên; RW Gaussian, GARCH, toy (Sim-03, 3 loại) | 18,000,000 bước mỗi thị trường; ~22,000–25,000 lệnh khớp mỗi nhóm | Excess FVG vs control: Gaussian +1.6% vs +1.9%; GARCH +2.0% vs +2.2% (offset chung do lấy mẫu p_null); toy −0.8% vs −1.1%; toy nến 2 ≥ 2 ATR −7.6% (n = 2,624) vs −1.4% (n = 2,881). Theo loại (toy): fill 91 / 58 / 27 / 74%, excess −16.0 / −3.5 / +3.0 / 0.0%; mix lúc hình thành 31/35/33% → trong lệnh khớp 49/36/16%. Panel B (n = 27,162): P(vượt 0.25/0.5/0.75/1.0) = 81.6 / 68.6 / 59.4 / 52.1% vs 1/(1+q) = 80 / 66.7 / 57.1 / 50% |
| **FVG-Sim-05** | Bước 10 giây, nến 15 phút; gap tạm thời tại close nến 2; trade: limit proximal, stop distal − 0.1 ATR, 2R; bug 1 = vào tại cực trị nến 3; bug 2 = phân xử bằng OHLC nến H1 (gồm cả nến khớp) | 18,000,000 bước; 24,641 lệnh (đúng), 29,581 (bug 1) | 48% gap tạm thời sống sót; P(sống) theo g (bảng §21.2), khớp 2Φ(g/σ) − 1; size cuối ≈ 0.6–0.8 × gap tạm thời. Win / E[R]: đúng 31.6% / −0.05; bug 1 65.3% / +0.96; bug 2a 50.2% / +0.51; bug 2b 27.2% / −0.18 |
| **FVG-Sim-06** | Một RW 6,000,000 phút gộp M5 / M15 / H1; FVG ≥ 0.25 ATR của khung; "unfilled" = chưa close xuyên distal (tối đa 48 nến); nested = vùng M5 nằm trọn trong vùng HTF cùng chiều | 317,115 M5 / 78,989 M15 / 15,544 H1 FVG | H1 FVG chứa M5 FVG cùng chiều trong nến 2: 98.2% (nến H1 ≥ 1.5 ATR không có H1 FVG: 99.9%); phủ 65% vùng; time-at-price trong/ngoài trung vị 0.56 (IQR 0.37–0.83); 3.17 M5 FVG/nến H1; nested 5.7% (H1), 3.6% (M15), 0.8% (cả hai) |
| **Bảng §43.1** | Xấp xỉ chuẩn, α = 0.05 hai phía, power 80% | Giải tích | Xem bảng |

**Giới hạn chung:** lợi nhuận Gaussian (trừ t(3)/GARCH) không có hồ sơ biến động theo giờ, không có spread, không có tin; bước rời rạc làm cực trị trong nến bị ước lượng thấp và tạo sai số nhỏ cho p_null (offset ~+2% chung cho FVG và control ở Sim-04); toy model có tham số minh họa, không hiệu chỉnh từ dữ liệu. Các kết quả mô tả **mô hình null / toy**, không mô tả thị trường thật.

**Tái lập:** script Python (numpy/scipy/matplotlib) và kết quả JSON ở `Claude outputs/fvg-v2-sims/` (seed cố định trong từng script); script vẽ 23 sơ đồ `FVG-Deep-*` ở `Claude outputs/fvg-v2-sims/diagrams/`.

---

## Phụ lục B — Pseudocode

```python
# FVG engine v0.1 — mọi hàm chỉ đọc bars[: t+1] (không nhìn tương lai)
# Tham số khai báo trước (HEURISTIC): MIN_SIZE=0.25, K_REACT=1.0, M_REACT=6, N_EXPIRE=48, BUFFER=0.1 (đơn vị ATR14)

def detect_fvg_at_close(bars, i, atr):
    """Gọi tại close của nến i (nến 3). Trả về FVG mới hoặc None."""
    h1, l1 = bars.high[i-2], bars.low[i-2]
    h3, l3 = bars.high[i],   bars.low[i]
    if l3 > h1:   d, prox, dist = +1, l3, h1        # bullish
    elif h3 < l1: d, prox, dist = -1, h3, l1        # bearish
    else:         return None
    size = abs(prox - dist)
    return dict(id=(i, d), d=d, prox=prox, dist=dist, ce=(prox+dist)/2, size=size,
                size_atr=size/atr[i], known_at=i, state="ACTIVE_UNTOUCHED",
                max_depth=0.0, touch_count=0, history=[("ACTIVE_UNTOUCHED", i)],
                c2_range_atr=(bars.high[i-1]-bars.low[i-1])/atr[i-1],
                flags=dict(session_gap=session_gap(bars, i-2, i), news=in_news_window(bars, i-1)))

def update_fvg_at_close(f, bars, t, atr):
    """Gọi tại close của mỗi nến t > known_at (cùng khung). Append-only."""
    if f["state"] in ("INVALIDATED", "EXPIRED", "INVERTED"): return f
    d = f["d"]
    ext = bars.low[t] if d > 0 else bars.high[t]                    # cực trị phía về vùng
    depth = d * (f["prox"] - ext) / f["size"]                       # >0 khi đi vào vùng
    touching = depth >= 0
    if touching and not f.get("was_touching", False):
        f["touch_count"] += 1                                       # lần chạm mới (nến trước không chạm)
    f["was_touching"] = touching
    if touching:
        f["max_depth"] = max(f["max_depth"], depth)
        new = "FULL_FILLED" if f["max_depth"] >= 1 else "CE_REACHED" if f["max_depth"] >= 0.5 else "TOUCHED"
        if new != f["state"]: f["state"] = new; f["history"].append((new, t))
    close = bars.close[t]
    if d * (close - f["dist"]) < 0:                                 # DEF-FVG-03: close cùng khung ngoài distal
        f["state"] = "INVALIDATED"; f["history"].append(("INVALIDATED", t)); return f
    if f["touch_count"] > 0 and reacted(f, bars, t, atr, K_REACT, M_REACT):
        f["state"] = "REACTED"; f["history"].append(("REACTED", t))
    if t - f["known_at"] > N_EXPIRE:
        f["state"] = "EXPIRED"; f["history"].append(("EXPIRED", t))
    return f

def reacted(f, bars, t, atr, k, m):
    """DEF-FVG-04: trong m nến kể từ lần chạm gần nhất, giá rời proximal ≥ k·ATR theo hướng FVG."""
    t_touch = last_touch_bar(f)
    if t - t_touch > m: return False
    best = max(bars.high[t_touch:t+1]) if f["d"] > 0 else min(bars.low[t_touch:t+1])
    return f["d"] * (best - f["prox"]) >= k * atr[f["known_at"]]

def control_zone(f, bars, atr, rng, pool):
    """DEF-FVG-06: cùng hướng, khoảng cách, size (ATR) tại nến t ngẫu nhiên cùng session/ATR/trend quintile."""
    i, d = f["known_at"], f["d"]
    delta = d * (bars.close[i] - f["prox"]) / atr[i]
    s = f["size"] / atr[i]
    t = rng.choice(pool.matching(session=session(i), atr_q=atr_quintile(i), trend_q=trend_quintile(i), no_fvg=d))
    prox_c = bars.close[t] - d * delta * atr[t]
    return dict(d=d, prox=prox_c, dist=prox_c - d * s * atr[t], known_at=t, size=s * atr[t])

def simulate_trade(zone, fine_path, bar_to_fine, entry="CE", W=20, RR=2.0, buffer_atr=0.1, atr=None):
    """Phân xử trên đường giá mịn (M1/tick). Limit chỉ hoạt động từ nến known_at+1 (chống Bug 1)."""
    d = zone["d"]; E = zone["ce"] if entry == "CE" else zone["prox"]
    S = zone["dist"] - d * buffer_atr * atr[zone["known_at"]]
    T = E + d * RR * abs(E - S)
    start = bar_to_fine(zone["known_at"] + 1); end = bar_to_fine(zone["known_at"] + 1 + W)
    k = first_index(d * (fine_path[start:end] - E) <= 0)
    if k is None: return dict(filled=False)                          # ghi missed_valid_setup
    kf = start + k; p_fill = fine_path[kf]
    p_null = d * (p_fill - S) / (d * (T - S))
    ks = first_index(d * (fine_path[kf+1:] - S) <= 0); kt = first_index(d * (fine_path[kf+1:] - T) >= 0)
    win = kt is not None and (ks is None or kt < ks)
    exit_px = fine_path[kf+1+kt] if win else fine_path[kf+1+ks]      # fill thực tế (gap-through)
    return dict(filled=True, win=win, p_null=p_null, r=d * (exit_px - E) / abs(E - S))
```

---

## Changelog

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| v1 | 2026-06-22 → 2026-07-28 | Note gốc: mục 1–13 theo template concept, Advanced 7.1–7.5, War Stories W0–W5, mục 14–17 (cơ chế, phản biện, edge cases, case studies) |
| v2 | 2026-10-07 | Hợp nhất với *Fair Value Gap — Deep Research v0.1* (brief 54 mục, Part I–XI). Thêm: nền tảng lệnh/sổ lệnh/AMT (§1), first principle "gap" + chứng minh nến 2 đi qua toàn vùng (§2), "fair value" 6 nghĩa (§3), inefficiency/imbalance (§4), 6 tầng + DEF-FVG-01 (§5), vì sao 3 nến (§6), bullish/bearish từ số 0 (§7), "không phải lỗ hổng" (§8), câu hỏi trung tâm + rà soát W0/§14 (§9), FVG vs displacement (§10), thuật ngữ & phân biệt (§11–12), vì sao quay lại / fill / luôn lấp? / CE / mitigation / S-R / invalidation / state machine / real-time (§13–21), bối cảnh MSS/sweep/POI/range/DOL/đa khung (§22–27), continuation vs reversal, FSS, ba loại displacement & adverse selection, failure modes, khung quyết định, case H-1/H-2 (§28–34), misconceptions & phản biện (§35–38), định lượng & backtest (§39–43), mô hình tư duy & registers (§44–48). 23 sơ đồ `FVG-Deep-*`, 6 hình mô phỏng `FVG-Sim-*`. Thêm frontmatter `markets`, `importance`, `confidence` (để trống — tự đánh giá), `version`, `prerequisites`; tags `trading/deep-dive`. **Không rule nào của v1 bị xóa** — thay đổi trình bày dạng OLD/NEW (§48.2) |

**Link hỏng đã sửa:** `common_mistakes` của v1 — `[[Mistake - Trade Every FVG]]`, `[[Mistake - FVG Without Displacement]]`, `[[Mistake - Entry Before Liquidity Sweep]]` trỏ tới note không tồn tại → thay bằng [[10-Mistake-FVG-Not-Valid]], [[08-Mistake-Weak-Displacement]], [[02-Mistake-Enter-before-liquidity-sweep]] (+ ba note mistake liên quan có thật). Trong thân bài: `[[04 - Backtesting]]` → thư mục `04 - Backtesting/`; self-link `[[13-FVG-Fair-Value-Gap|mục W4]]` → "mục W4"; `` `[[Fair Value Gap]]` `` → `` `[[13-FVG-Fair-Value-Gap|Fair Value Gap]]` ``. **Đề xuất:** tạo note `06 - Mistake Database/14-Mistake-Lookahead-FVG-Touch.md` (lỗi Bug 1 ở §21.3 chưa có note tương ứng).

**Hình trong vault không được nhúng (có chủ đích):** `FVG-EdgeB-OvernightRespectRate.svg` (chứa "backtest… N=520 mẫu", tỷ lệ 71/41/22/13% không có nguồn); `FVG-CaseStudy-B1-XAUUSD-Chase-Loss.svg`, `FVG-CaseStudy-B2-NQ-HiddenFVG-Win.svg` (ghi "tái dựng minh họa từ mẫu backtest", R-multiple cụ thể, không có dữ liệu gốc). Theo quy tắc không dùng số liệu chưa xác minh, chúng không được đưa vào note; các file vẫn nằm nguyên trong `attachments/`. **Hình v1 chưa từng được nhúng nay được nhúng kèm nhãn v2:** `FVG-EdgeB-VolumeImbalanceMerge.svg` (§11.3), `FVG-EdgeB-BrokerOffsetH1.svg` và `FVG-EdgeB-HiddenInHTFWick.svg` (§27.5, kèm rà soát hindsight), `FVG-EdgeB-PartialFillRunaway.svg` (§31). Mọi hình v1 đã nhúng được giữ nguyên.

**Bản đồ di chuyển nội dung v1 → v2**

| v1 | v2 |
|---|---|
| Tóm tắt 1 câu, Nguyên tắc cốt lõi | Viết lại; nguyên tắc v1 giữ trong callout "Nguyên tắc cốt lõi (v2)" |
| §1 Định nghĩa (khái niệm, BISI/SIBI, bản chất, CE, mục đích, câu hỏi) + hình Sec-01 | §5.8 (nguyên văn + bảng chú thích) |
| §1 "Không phải là gì" | §5.9 (+ 7 dòng v2) |
| §2 Bối cảnh sử dụng | §33.1 |
| §3 Cấu trúc nhận diện | §33.2 |
| §4 Quy trình đa khung + mẫu ghi nhanh | §27.6 |
| §5 Quy tắc xác nhận / vô hiệu (+ bảng Fill/Respect/Mitigation/Inversion, IFVG) | §19.3 |
| §6 Ví dụ chart & sequence | §33.3 |
| §7.1 Gia đình gap · §7.2 Quadrants · §7.3 Time & Price · §7.4 Delivery state · §7.5 Best practices | §11.2 · §16.6 · §27.7 · §27.8 · §29.3 |
| War Stories — intro, W0, W1–W5 | §33.5 (intro, W1–W5) · §9.6 (W0 + rà soát) |
| §8 Checklist | §34.1 (+ §34.2 v2) |
| §9 Lỗi thường gặp | §38.1 (+ §38.2 v2) |
| §10 Câu hỏi · §11 Flashcards Q1–Q8 | §47.1 · §47.3 (+ §47.2, Q9–Q20) |
| §12 Lesson learned · §13 Thành thạo | §47.5 (+ §47.6–47.7) · §47.8 (+ tiêu chí v2) |
| §14 intro + 14.1 · 14.2 · 14.3 · 14.4 · 14.5 | §8.4 · §9.7 · §9.7 · §30.5 · §30.6 |
| §15 Phản biện (15.1–15.3) | §37.1 (+ §37.2–37.3) |
| §16 Edge cases EC1–EC8 | §33.6 |
| §17 Case studies 1–4 | §33.7 (đánh dấu chưa xác minh) |
