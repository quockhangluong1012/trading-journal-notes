---
type: ict-concept
concept: Liquidity Sweep
aliases:
  - Liquidity Sweep
  - Liquidity Run
  - Run on Liquidity
  - Sweep
  - Liquidity Raid
  - Stop Run
  - Stop Hunt
  - Liquidity Grab
  - Stop Raid
  - Turtle Soup
tags:
  - trading/ict/concept
  - trading/study
  - "#LiquiditySweep"
  - "#LiquidityRun"
status: developing
category: Liquidity
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[01 - ICT 2022 Model|ICT 2022]]"
last_reviewed: 2026-10-06
created: 2026-06-22
updated: 2026-10-06
prerequisites:
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[12-Dealing-Range]]"
  - "[[21-Market-Structure-Shift]]"
  - "[[50-Displacement-In-Depth]]"
common_mistakes:
  - "[[02-Mistake-Enter-before-liquidity-sweep]]"
  - "[[13-Mistake-Trading-Into-Unswept-Liquidity]]"
  - "[[08-Mistake-Weak-Displacement]]"
  - "[[06-Mistake-Not-Have-Market-Structure-Shift]]"
  - "[[04-Mistake-FOMO-Entry]]"
---

# Liquidity Sweep / Liquidity Run

> [!summary] Tóm tắt 1 câu
> **Liquidity Sweep là tên gọi cho một sự kiện quan sát được — giá giao dịch xuyên qua một mức tham chiếu đã xác định trước (đỉnh/đáy cũ, equal highs/lows, PDH/PDL…) rồi bị phân xử bằng *rejection* (quay lại bên trong); Liquidity Run là chuỗi nhiều mức cùng phía bị lấy với *acceptance*. Cả hai chỉ được biết sau một độ trễ, đều không tự mang hướng đi kế tiếp, và "liquidity" trong cả hai là một *giả thuyết* về mật độ lệnh có điều kiện quanh mức giá — không phải thứ nhìn thấy được trên chart.**

> [!important] Nguyên tắc cốt lõi (v2)
> **Sweep là một PHÉP THỬ, không phải một TÍN HIỆU.** Khi giá chạm tới vùng có thể có stop, các lệnh đó (nếu có) được kích hoạt và khớp; điều quyết định giá đi đâu tiếp theo là *dòng lệnh tới sau khi stop đã khớp* — thứ không nhìn thấy trên nến. Vì vậy:
> 1. Không phân loại tại wick. Sau nến xuyên mức, trạng thái đúng là **PENDING** cho tới khi có rejection hoặc acceptance trong cửa sổ k nến.
> 2. Rejection chưa phải đảo chiều. Đảo chiều cần **hậu quả cấu trúc** (MSS phá một swing có ý nghĩa) và **displacement** trong cửa sổ m nến.
> 3. Mọi tuyên bố "sweep có edge" phải vượt **baseline hình học** p_null và dùng **fill thực tế**. Trên random walk, khoảng một nửa số lần xuyên mức tự đóng lại bên trong, và "đảo về pool đối diện" xảy ra đúng bằng tỷ lệ mà khoảng cách quy định (LS-Sim-01, LS-Sim-02).
>
> *Nguyên tắc của v1 — "một cú quét chỉ là sweep khi giá reclaim kèm displacement; đóng nến ngoài vùng và đi tiếp là break thật; đừng trade cú quét, trade phản ứng sau cú quét" — **vẫn giữ nguyên giá trị thực hành**. v2 bổ sung: (a) "đóng ngoài" và "reclaim" đều là nhãn tạm thời và có thể bị lật (§12, §21); (b) "reclaim + displacement" là quy tắc phân loại có độ trễ, không phải bằng chứng trực tiếp về việc ai đã làm gì trong order flow (§4.5).*

> [!info] Đây là bản v2 (2026-10-06) — đọc trước khi dùng
> - Note hợp nhất **note v1** (2026-06-22 → 2026-07-28) với nghiên cứu chuyên sâu **Liquidity Sweep / Liquidity Run — Deep Research v0.1** (theo brief 39 mục của bạn, phần bị cắt ở mục 39 đã được hoàn thiện và mở rộng sang định lượng, backtest, registers). Nội dung v1 được giữ **nguyên văn** ở chỗ phù hợp và đánh dấu *(v1)*; nơi v1 có claim cần sửa hoặc gắn nhãn, chú thích v2 đứng ngay cạnh, không xóa bản gốc. Bản đồ di chuyển nội dung ở [[#Changelog]]. Bản v1 nguyên vẹn được sao lưu tại `Claude outputs/backups/20-Liquidity-Sweep.2026-10-06.md.bak`.
> - Ba loạt hình: `LS-Deep-01…18` = sơ đồ khái niệm mới (v2); `LS-Sim-01…07` = **mô phỏng null model / toy model** — baseline mà mọi claim phải vượt, **không phải dữ liệu thị trường**; `Liquidity-Sweep-*` = hình của v1.
> - Mọi ngưỡng số là **HEURISTIC**; mọi `RULE-LS` là **v0.1 — BACKTEST REQUIRED**; mọi `HYP-LS` là **UNTESTED**. Không thành phần nào trong note là edge đã được kiểm chứng trên dữ liệu thật.
> - Note liên quan được dùng làm nền và không lặp lại ở đây: [[19-Liquidity]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[59-Daily-Bias]] · [[12-Dealing-Range]] · [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] · [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]].

> [!abstract]- Mục lục (bấm để mở)
> - **Cách đọc note** — hệ thống nhãn, thang giải thích 6 tầng, ký hiệu
> - **0. Executive Summary** — 20 kết luận
> - **1. Nền tảng: liquidity thực sự là gì** — lệnh, sổ lệnh, maker/taker, impact, chart cho biết gì, liquidity vs volume/order flow/volatility
> - **2. Vì sao liquidity hình thành ở các mức nổi bật** — salience, người tham gia, bảng theo loại mức, equal highs/lows, swing
> - **3. Pool, BSL, SSL** — level/zone/pool/cluster, nghịch lý tên gọi
> - **4. Vì sao giá đi tới liquidity** — bảy cơ chế + baseline hình học; rà soát W0 của v1
> - **5. Liquidity Sweep chính xác là gì** — sáu tầng, định nghĩa vận hành, thuật ngữ sweep/raid/stop run/false breakout…
> - **6. Liquidity Run** — định nghĩa, so sánh với sweep, chuyển trạng thái, run vs trend
> - **7. Taxonomy sự kiện E0–E9** · **8. Vòng đời liquidity** · **9. Internal/External, hierarchy, LSS**
> - **10. Giải phẫu một sweep từng bước** — toy model stop cascade + transient impact
> - **11. Sau sweep** — cây kết quả, sweep ≠ reversal, reclaim giả · **12. Sweep vs Breakout**
> - **13–19.** Sweep + MSS · Displacement · FVG · POI · Dealing Range & P/D · DOL · Run & exhaustion
> - **20. State machine** · **21. Real-time vs ex-post** · **22. D1 → H1 → M5**
> - **23. Ví dụ & case studies** · **24. Counterexamples & edge cases**
> - **25. Định lượng** · **26. Backtest** · **27. Checklist** · **28. Lỗi thường gặp** · **29. Phản biện**
> - **30. Mô hình tư duy cuối cùng** · **31–34.** Câu hỏi · Flashcards · Lesson learned · Thành thạo
> - **35. Registers** — DEF-LS, RULE-LS, HYP-LS, câu hỏi nghiên cứu · Tài liệu tham khảo · Phụ lục · Changelog

---

## Cách đọc note này — hệ thống nhãn

| Nhãn | Ý nghĩa | Mức tin cậy mặc định |
|---|---|---|
| **[OBSERVABLE]** | Điều đọc trực tiếp được từ OHLC + thời gian ("high nến vượt PDH 6 pip, close dưới PDH") | Cao — nhưng chỉ mô tả |
| **[MATHEMATICAL]** | Đúng theo định nghĩa hoặc chứng minh toán học (ví dụ: gambler's ruin, reflection principle) | Cao — về logic, không về thị trường thật |
| **[SIMULATION]** | Kết quả mô phỏng null model (random walk) với seed cố định | Cao về *mô hình null*; không phải dữ liệu thị trường |
| **[TOY MODEL]** | Mô hình cơ chế đơn giản hóa, tham số minh họa, không hiệu chỉnh | Chỉ minh họa *một* cơ chế có thể |
| **[MARKET MECHANICS]** | Giải thích bằng order matching, liquidity, impact, auction — hoặc có bằng chứng thực nghiệm đã công bố | Cao → trung bình tùy bằng chứng |
| **[ICT FRAMEWORK]** | Cách ICT / cộng đồng ICT định nghĩa hoặc dùng thuật ngữ | Cao về *định nghĩa*; không nói gì về *hiệu quả* |
| **[INTERPRETATION]** | Diễn giải hợp lý nhưng không chứng minh được từ OHLC | Trung bình → thấp |
| **[HYPOTHESIS]** | Claim kiểm chứng được | Chưa biết |
| **[BACKTEST REQUIRED]** | Không được coi là edge cho tới khi test đúng phương pháp | — |
| **[HEURISTIC]** | Ngưỡng số được chọn để có một quy tắc nhất quán, không phải hằng số của thị trường | — |

**Về nguồn ICT.** Giáo trình gốc của ICT (Michael J. Huddleston) chủ yếu ở dạng video/mentorship, không có văn bản định nghĩa chính thức. "[ICT FRAMEWORK]" trong note này = *cách hiểu phổ biến trong tài liệu cộng đồng* (Tier 3–4 theo source hierarchy của project), ví dụ innercircletrader.net. Note **không** trích nguyên văn ICT và không gán cho ICT những câu chưa kiểm chứng.

**Về "Smart Money".** Trong note, "Smart Money" luôn được hiểu là **một nhân vật trong câu chuyện của mô hình ICT**, không phải một nhóm người tham gia quan sát được trên chart. Khi một câu cần nói về người tham gia, note dùng thuật ngữ vi cấu trúc có thể định nghĩa: *người cung cấp thanh khoản (maker)*, *người tiêu thụ thanh khoản (taker)*, *lệnh có điều kiện*, *metaorder*, *dòng lệnh ròng*.

**Về mô phỏng.** Bảy hình `LS-Sim-01 … 07` dùng random walk Gaussian không drift (trừ khi ghi rõ), bước 1 phút hoặc 10 giây, tới 24 triệu bước mỗi mô phỏng; hai hình (03, 04) là toy model cơ chế. Mục đích **không** phải chứng minh ICT sai — mà để biết *một hiện tượng xuất hiện thường xuyên tới mức nào khi không có bất kỳ "ý định" nào*. Hiện tượng xuất hiện nhiều trên random walk thì *sự xuất hiện* của nó trên chart thật không phải bằng chứng của edge. Chi tiết ở [[#Phụ lục A — Ghi chú mô phỏng]].

**Thang giải thích 6 tầng** (theo yêu cầu "giải thích cho đứa trẻ 5 tuổi" của brief):

| Tầng | Tên | Mục tiêu |
|---|---|---|
| L1 | Trực giác | Ngôn ngữ đời thường, không thuật ngữ |
| L2 | Ví dụ giá đơn giản | Một chuỗi giá / sơ đồ ASCII |
| L3 | Trading | Thuật ngữ trading phổ thông |
| L4 | Cơ chế thị trường | Order matching, stop/limit/market, khớp lệnh, cung cấp/tiêu thụ thanh khoản, price discovery |
| L5 | ICT | "ICT gọi hiện tượng này là…" — chỉ sau khi đã có L4 |
| L6 | Giới hạn | Chart **không thể** cho biết điều gì |

**Ký hiệu dùng xuyên suốt**

| Ký hiệu | Nghĩa |
|---|---|
| L | Mức tham chiếu (reference level) — đỉnh/đáy cũ, PDH/PDL, EQH/EQL… xác định **trước** sự kiện |
| known_at | Thời điểm (close của nến) mà một mức/nhãn trở nên biết được. Không có known_at = không dùng được trong backtest |
| ε | Dung sai "chạm" (ví dụ 0.05·ATR hoặc 1–2 tick) |
| δ | Biên "quay lại bên trong" để tính rejection (ví dụ 0.25·ATR) |
| k | Timer phân xử: số nến tối đa chờ rejection/acceptance |
| m | Cửa sổ chờ MSS + displacement sau rejection |
| ATR | ATR(14) của khung đang xét, đóng băng tại nến trước sự kiện |
| p_null | Xác suất random walk không drift chạm mục tiêu trước stop = (Stop − Entry)/(Stop − Target) cho lệnh short (đối xứng cho long) |
| SERR | Sweep Excess Reversal Rate = tỷ lệ chạm pool đối diện trước stop **trừ** p_null. Thước đo "đảo chiều vượt hình học" |
| LSS | Liquidity Significance Score (§9.3) |
| E0–E9 | Mã sự kiện (§7) |

---

## 0. Executive Summary

Hai mươi kết luận. Mỗi kết luận được phát triển ở các mục sau.

**1. "Liquidity" trên chart là cách nói tắt cho một giả thuyết.** Câu "có liquidity trên đỉnh cũ" nghĩa đầy đủ là: *có thể* có một mật độ cao hơn bình thường của lệnh có điều kiện (stop-loss, buy-stop breakout, thanh lý ký quỹ) và lệnh chờ (limit) quanh mức giá đó. Không lệnh nào trong số đó hiện trên nến; stop order nói chung **không hiển thị trong sổ lệnh công khai trước khi bị kích hoạt** (§1.2, §1.8). **[MARKET MECHANICS]**

**2. Có bằng chứng thực nghiệm rằng lệnh tập trung quanh mức nổi bật — nhưng bằng chứng hẹp hơn câu chuyện.** Osler (2003, 2005) dùng sổ lệnh của một ngân hàng dealer FX: stop-loss mua tập trung *ngay trên* số tròn, stop-loss bán *ngay dưới*; sau khi giá vượt các mức này, tỷ giá chạy nhanh hơn và kéo dài hơn (price cascade), còn take-profit tạo phản hồi âm (đảo chiều ngắn hạn). Kavajecz & Odders-White (2004): mức support/resistance trùng đỉnh độ sâu của limit order book. Fett & McPhail (CFTC, 2017): trên ES, ZN, CL futures 2014–2016, giao dịch có stop order chỉ chiếm khoảng 0.3–2% hoạt động giao dịch (tùy hợp đồng) và tăng cùng biên độ biến động trong ngày. **Không** có bằng chứng công khai rằng "mọi swing high là pool", hay rằng stop là nguồn đối ứng chủ yếu của lệnh lớn (§2, §4).

**3. Tên gọi BSL/SSL đặt theo phía của LỆNH CHỜ KÍCH HOẠT, không theo hướng giá.** BSL là khối lệnh MUA có thể xuất hiện khi giá vượt đỉnh → nó là **đối ứng cho người muốn BÁN** lượng lớn. Vì vậy câu chuyện ICT "lấy BSL rồi giảm" nhất quán về mặt cơ học — nhưng tính nhất quán đó không chứng minh nó xảy ra thường xuyên hơn baseline (§3).

**4. "Giá đi tìm liquidity" không phải một định luật nhân quả; nó là mô tả hợp nhất của ít nhất bảy cơ chế cộng một baseline hình học.** Ngay cả random walk cũng chạm mức gần trước mức xa với xác suất d_xa/(d_gần + d_xa) — mức cách 1 ATR so với mức cách 3 ATR: **75%** **[MATHEMATICAL]**. Một phần lớn cảm giác "giá luôn đi lấy thanh khoản gần nhất" là hình học + selection bias (ta chỉ nhớ những mức đã bị lấy) (§4).

**5. Hình dạng "xuyên rồi đóng lại bên trong" xảy ra khoảng một nửa số lần mà không cần ai săn stop.** Với chuyển động Brown không drift, *nếu* một nến giao dịch xuyên qua mức, xác suất close nằm lại bên kia mức là đúng 50% (reflection principle) **[MATHEMATICAL]**. Trên random walk rời rạc: 29% (M5) → 38% (M15) → 44% (H1) → 49% (H4) → 52% (D1) — càng nhiều bước nhỏ trong một nến, càng gần 50% (LS-Sim-01A) **[SIMULATION]**. Một bộ sưu tập "sweep đẹp" luôn tìm được, kể cả trên dữ liệu không có edge.

**6. Cùng một sự kiện, hai timeframe, hai nhãn.** Trên random walk, khoảng **39%** lần xuyên mức đầu tiên có nhãn M5 ("sweep"/"break" theo close của nến M5) trái ngược với nhãn của nến H1 chứa nó (LS-Sim-01B) **[SIMULATION]**. "Sweep" là nhãn phụ thuộc độ phân giải, không phải thuộc tính của sự kiện.

**7. "Đảo về pool đối diện" sau sweep = hình học, trừ khi chứng minh được ngược lại.** Trên 23,140 lần xuyên swing high M15 (random walk, bước 10 giây): với lệnh bán tại close nến xuyên, stop trên cực trị + 0.1 ATR, target là swing low gần nhất chưa bị lấy — tỷ lệ chạm target trước stop **nằm trên đường chéo p_null** ở mọi khoảng cách; nhóm "đóng lại bên trong" thắng 20.6% với p_null trung bình 19.4%, R:R trung vị 5.1, **expectancy +0.02R (SE 0.03) ≈ 0** (LS-Sim-02A) **[SIMULATION]**.

**8. Định nghĩa "thành công" quyết định con số.** Cùng tập "sweep" đó trên random walk: "giá giảm ≥ 1 ATR trong 20 nến" = **73%**; "có close dưới low của nến sweep trong 10 nến" = **66%**; "chạm pool đối diện trước stop" = **21%**; expectancy = **0** (LS-Sim-02B). Các con số "sweep đảo chiều 70–80%" phổ biến nhiều khả năng dùng định nghĩa thứ nhất hoặc thứ hai.

**9. Fill lý tưởng tạo edge ảo.** Cùng tập lệnh, nếu giả định stop khớp đúng giá đặt (bỏ qua bước nhảy qua stop), expectancy trên random walk thành **+0.08R (SE 0.03)** — một "edge" hoàn toàn do giả định khớp lệnh. Đây là phiên bản định lượng của War Story W3 (v1) về "phantom R" (§26) **[SIMULATION]**.

**10. Sweep là một phép thử: kết quả do dòng lệnh tới SAU khi stop đã khớp quyết định.** Toy model propagator (LS-Sim-03): cùng một cụm stop, cùng nhiễu, cùng đường giá trước sweep — (A) không có lệnh mới → impact tạm thời phai đi, giá trôi về dưới mức ("sweep" mà không có ai hấp thụ); (B) có người mua bền bỉ → acceptance và run; (C) có người bán xuất hiện → đảo chiều nhanh với "displacement" **[TOY MODEL]**. Hình dạng nến xuyên mức trong ba kịch bản là giống nhau.

**11. Độ sâu của sweep là một tỷ số, không phải một ý định.** Toy model stop cascade tĩnh (LS-Sim-04): giá xuyên sâu bao nhiêu phụ thuộc vào tỷ số giữa khối stop bị kích hoạt và độ sâu lệnh limit đối diện; có một ngưỡng (S/(D·λ) ≈ 1) mà vượt qua thì cascade chạy xuyên cả cụm. Sổ mỏng (phiên Á, lễ, tin tức) → sweep sâu với cùng lượng stop. Điều này khớp với kết luận của BIS (2017) về flash event GBP: thời điểm thanh khoản mỏng + các bộ khuếch đại cơ học (kể cả hedging liên quan quyền chọn) **[TOY MODEL + MARKET MECHANICS]**.

**12. Nhãn sweep/break là tạm thời và thường bị lật.** Với quy tắc v0.1 (REJECTED = close < L − 0.25·ATR; ACCEPTED = 2 close > L hoặc 1 close > L + 0.5·ATR), trên random walk M5: **59%** sự kiện còn PENDING tại close của nến xuyên; nhãn REJECTED bị lật thành ACCEPTED trong 6 nến ở **44%**, trong 48 nến ở **78%** trường hợp (LS-Sim-05) **[SIMULATION]**. Một quy tắc thực tế có giá trị khi flip rate trên dữ liệu thật *thấp hơn rõ rệt* mức này ở các mức có ý nghĩa.

**13. Sweep và Run khác nhau ở cách sự kiện được phân xử, không ở bản thân cú xuyên mức.** Trong cách dùng cộng đồng ICT, "sweep" = lấy liquidity rồi đảo; "run" = lấy liquidity rồi đi tiếp. Đó là phân biệt theo **kết quả**, nên nó chỉ biết được sau một độ trễ và dễ thành lập luận vòng tròn. v2 đề xuất định nghĩa theo hành vi quan sát được: **Sweep = một mức, phân xử bằng rejection; Run = ≥ 2 mức cùng phía, mỗi mức phân xử bằng acceptance** (§6, DEF-LS-04/05).

**14. Run là mô tả của drift, không phải một thực thể dự báo riêng.** Trên random walk H1 không drift: 64% chuỗi "lấy pool cùng phía" dài ≥ 2, **43% dài ≥ 3**, 19% dài ≥ 5. Thêm drift 0.15σ/nến: chuỗi BSL trung bình 3.5 mức, chuỗi SSL 1.9 (LS-Sim-06) **[SIMULATION]**. Câu "giá đang run liquidity" chỉ có giá trị dự báo nếu nó giúp ước lượng drift tốt hơn các thước đo trend thông thường.

**15. Equal highs/lows tự hình thành trên random walk và không "hút" giá hơn đỉnh đơn cùng khoảng cách.** Với dung sai 0.1·ATR: 2.8 EQH / 1,000 nến M15; dung sai 0.3·ATR: 8.0 (LS-Sim-07) **[SIMULATION]**. Cơ chế salience có cơ sở (Osler; Garzarelli et al. 2014 tìm thấy hiệu ứng "nhớ" ở thang 45–90 giây trên cổ phiếu LSE), nhưng "EQH là nam châm" là **[HYPOTHESIS]** cần test so với đỉnh đơn cùng khoảng cách (HYP-LS-006).

**16. Internal/External là quan hệ với một range, không phải thuộc tính của mức giá.** Cùng một mức là external với range H1 và internal với range D1. Mọi nhãn ERL/IRL phải kèm range tham chiếu (§9.1).

**17. Location ≠ Liquidity event ≠ Confirmation ≠ Entry trigger ≠ Invalidation.** Năm thành phần trả lời năm câu hỏi, sai theo năm cách khác nhau, và phải được ghi riêng trong journal. "Sweep là entry" là lỗi gộp phổ biến nhất (§16).

**18. MSS là bằng chứng sweep có hậu quả cấu trúc — không phải thứ sweep "tạo ra".** Bốn ô Sweep×MSS có ý nghĩa dự báo khác nhau; ô "MSS không có sweep tại mức ex-ante" đòi hỏi kiểm tra lại danh sách mức trước khi gọi là sweep (§13).

**19. Một máy trạng thái đủ rõ để code là khả thi** — IDLE → ARMED → PROBING → PENETRATED → PENDING → {REJECTED, ACCEPTED, EXPIRED} → {REVERSAL CONF., STALE, FAILED BO, RUN ACTIVE} → … với chuyển trạng thái chỉ tại bar close, known_at cho mọi nhãn, và nhãn append-only (§20). Đây là điều kiện cần để backtest không bị hindsight.

**20. Kiểm chứng đòi hỏi cỡ mẫu lớn hơn trực giác.** Phát hiện SERR = +5 điểm phần trăm trên baseline 25% (α = 0.05, power 80%) cần ~**610** sự kiện độc lập; +3 điểm cần ~**1,670**. Phát hiện expectancy +0.2R khi win rate ~25% và R:R ~4 cần ~**920** lệnh **[MATHEMATICAL]**. Một backtest tay 30–50 setup chỉ đủ để phát hiện lỗi thô và sinh giả thuyết (§26).

> [!tip] Câu trả lời ngắn cho câu hỏi trung tâm của brief
> *"Tại sao một liquidity event đôi khi dẫn tới reversal, đôi khi continuation?"* — Vì việc chạm tới liquidity chỉ **tiêu thụ** các lệnh có điều kiện đang chờ; nó không quyết định ai tới sau. Nếu sau khi stop đã khớp, dòng lệnh ròng cùng chiều tiếp tục (thông tin mới, trend, người tham gia breakout có vốn thật) → acceptance → run. Nếu không ai tiếp tục, impact tạm thời phai → giá trôi về. Nếu có bên ngược chiều dùng chính các lệnh vừa kích hoạt làm đối ứng → đảo chiều nhanh với displacement. Ba nhánh nhìn giống hệt nhau tại nến xuyên mức. Edge — nếu tồn tại — nằm ở việc **ước lượng xác suất từng nhánh tốt hơn baseline bằng các biến có trước sự kiện** (bối cảnh HTF, vị trí, thời gian, độ sâu sổ, khoảng cách tới pool đối diện), không nằm ở việc gọi tên nhánh sau khi nó đã xảy ra.

---

## 1. Nền tảng: liquidity thực sự là gì

> [!note] Vì sao bắt đầu từ đây
> Mọi câu trong ICT về sweep/run đều đứng trên một từ: *liquidity*. Nếu từ này được hiểu như "một thứ nằm trên chart" thì mọi suy luận phía sau đều trượt theo. Mục này xây nghĩa của từ từ dưới lên: lệnh → sổ lệnh → ai cung cấp/tiêu thụ → vì sao giá dịch chuyển → chart cho biết gì → "liquidity trên chart" thực ra là cách nói tắt cho điều gì.

### 1.1 Giải thích cho đứa trẻ 5 tuổi (L1–L2)

**L1 — Trực giác.** Tưởng tượng một khu chợ chỉ bán một món: táo. Có những người **đứng chờ sẵn** ở các mức giá: "ai bán cho tôi giá 10 thì tôi mua", "ai mua của tôi giá 12 thì tôi bán". Họ không vội — họ *đứng đợi*. Có những người **vội**: "tôi cần mua ngay, giá nào cũng được" — họ đi tới người đang đứng đợi rẻ nhất và mua. Khi người đứng đợi ở giá 12 hết táo, người vội phải trả 12.1, rồi 12.2… → **giá tăng không phải vì ai quyết định cho nó tăng, mà vì những người đứng đợi ở giá thấp hơn đã hết.**

Có một nhóm thứ ba kỳ lạ hơn: những người dặn trước "**nếu** giá táo vượt 13 thì mua giúp tôi ngay, bao nhiêu cũng được". Họ **vô hình** cho tới khi giá chạm 13. Khi đó họ biến thành người vội — và lượng mua đột ngột này có thể đẩy giá chạy tiếp lên 13.5, 14… làm thức dậy thêm những người "nếu…" khác ở 13.5. Đây là hạt giống của mọi câu chuyện về stop và sweep.

**Giới hạn của ẩn dụ:** khu chợ thật có hàng nghìn người, người đứng đợi có thể *rút* lệnh bất cứ lúc nào, và có những người vừa đứng đợi vừa vội (market maker). Ẩn dụ chỉ dùng để nắm ba vai trò; nó không mô tả kích thước hay tốc độ.

**L2 — Ví dụ giá đơn giản.**

```text
Giá
13.4 |                 x   ← "những người nếu…" ở 13.0–13.3 đã thức dậy (mua market)
13.2 |               x
13.0 |- - - - - - - -x- - - - -  đỉnh cũ (mọi người đều thấy)
12.8 |      x      x
12.6 |    x   x  x
12.4 |  x       x
       ------------------------------> thời gian
```

Mọi người đều thấy đỉnh 13.0. Người đang bán khống đặt "nếu vượt 13.05 thì mua lại để cắt lỗ". Người chờ "phá đỉnh thì mua" đặt "nếu vượt 13.05 thì mua". Khi giá chạm 13.05, cả hai nhóm *cùng lúc* trở thành người mua vội. Điều xảy ra tiếp theo phụ thuộc vào việc **có ai đang đứng đợi bán ở 13.05–13.4 hay không, và họ có bao nhiêu hàng**.

### 1.2 Lệnh là gì — market, limit, stop (L3–L4)

![[LS-Deep-01-Ba-Loai-Lenh-Va-So-Lenh.svg|900]]
*Hình LS-Deep-01: Limit order cung cấp độ sâu (hiển thị). Market order tiêu thụ độ sâu. Stop order là lệnh có điều kiện, thường không hiển thị cho tới khi bị kích hoạt — "liquidity trên đỉnh cũ" chủ yếu là loại lệnh vô hình này.*

| Loại lệnh | Làm gì | Vai trò với liquidity | Hiển thị trước khi khớp? | Phản hồi với giá |
|---|---|---|---|---|
| **Market order** | Mua/bán ngay ở giá tốt nhất đang có | **Tiêu thụ** (taker) | Không — khớp ngay | — |
| **Limit order** | Chỉ khớp tại giá đặt hoặc tốt hơn | **Cung cấp** (maker) — tạo "độ sâu" | Có (trừ iceberg/hidden) | Mua khi giá giảm, bán khi giá tăng → **phản hồi âm** (giảm biến động) |
| **Stop-market** | Khi giá chạm trigger → thành market order | **Tiêu thụ có điều kiện** | Nói chung **không** (nằm ở server sàn/broker, không vào sổ công khai) | Mua khi giá tăng qua trigger, bán khi giá giảm qua trigger → **phản hồi dương** (khuếch đại) |
| **Stop-limit** | Khi giá chạm trigger → thành limit order | Tiêu thụ nếu giá limit "marketable", nếu không thì thành maker | Không | Phản hồi dương nhưng có trần trượt giá |
| **Take-profit (limit)** | Limit order chốt lời | Cung cấp | Có | Phản hồi âm (Osler 2003: tạo xu hướng đảo chiều ngắn tại số tròn) |
| **Thanh lý ký quỹ / margin call** | Lệnh market do hệ thống tạo khi ký quỹ không đủ | Tiêu thụ cưỡng bức | Không | Phản hồi dương, có thể dây chuyền (crypto: liquidation cascade) |

**[MARKET MECHANICS]** Ba điểm quan trọng cho mọi phần sau:

1. **Stop là lệnh *tiêu thụ* thanh khoản, không phải lệnh *cung cấp*.** Câu "liquidity nằm ở stop" nghe ngược tai với định nghĩa vi cấu trúc. Nghĩa đúng của nó trong ICT: *stop là một khối lệnh market sẽ xuất hiện tại một mức đoán trước được* → với bên muốn giao dịch **ngược chiều** stop, khối này là đối ứng. Với bên muốn giao dịch **cùng chiều** stop, nó là đối thủ cạnh tranh.
2. **Stop không hiển thị.** Trên futures CME, nghiên cứu CFTC của Fett & McPhail (2017) và các tài liệu sàn mô tả stop là lệnh có điều kiện được giữ cho tới khi trigger; trong FX OTC, stop nằm ở dealer/broker (Osler 2005 dùng chính sổ lệnh nội bộ của một ngân hàng dealer). Không ai ngoài nơi giữ lệnh biết tổng khối lượng stop ở một mức.
3. **Phản hồi dương vs âm là chìa khóa.** Osler (2005) cho thấy sau khi tỷ giá vượt vùng tập trung stop-loss, chuyển động nhanh hơn và kéo dài hơn (hàng giờ) so với sau khi chạm vùng take-profit. Tức là **cơ chế stop thuần túy dự báo *tiếp diễn* sau khi xuyên mức, không phải đảo chiều**. Đảo chiều cần thêm một thứ khác (§10–11).

### 1.3 "Liquidity" trong thị trường nghĩa là gì

**[MARKET MECHANICS]** Trong vi cấu trúc thị trường, liquidity là **khả năng giao dịch một khối lượng mong muốn, nhanh, với chi phí (trượt giá + spread) thấp**. Kyle (1985) tách thành ba chiều; Harris (2003) thêm chiều tức thời:

| Chiều | Câu hỏi | Ví dụ khi thanh khoản tốt | Ví dụ khi thanh khoản kém |
|---|---|---|---|
| **Tightness** (độ chặt) | Spread rộng bao nhiêu? | EURUSD giữa phiên London: spread rất hẹp | 05:00 sáng giờ VN, rollover: spread giãn |
| **Depth** (độ sâu) | Bao nhiêu khối lượng có thể khớp mà giá không dịch chuyển nhiều? | Nhiều lệnh limit ở mỗi mức | Sổ mỏng — một lệnh vừa đủ "xuyên" nhiều mức |
| **Resiliency** (độ hồi phục) | Sau khi bị ăn, độ sâu được bổ sung nhanh không? | Market maker đặt lại quote trong mili-giây | Sau tin tức: quote bị rút, chậm quay lại |
| **Immediacy** (tức thời) | Có khớp ngay được không? | — | Thị trường "đóng băng" quanh tin |

**Hiển thị vs tiềm ẩn.** Bouchaud et al. (2018) phân biệt *displayed liquidity* (lệnh limit đang nằm trên sổ) với *latent liquidity* (ý định giao dịch chưa đặt thành lệnh, chỉ lộ ra khi giá tới gần). Phần lớn "thanh khoản thật" của một thị trường lớn là tiềm ẩn. Hệ quả: **ngay cả người nhìn được toàn bộ sổ lệnh cũng không thấy hết liquidity** — và người chỉ nhìn nến thì không thấy gì cả.

### 1.4 Ai cung cấp, ai tiêu thụ liquidity

| Người tham gia | Thường là | Hành vi điển hình quanh một đỉnh cũ |
|---|---|---|
| Market maker / HFT cung cấp quote | Maker (phần lớn), taker khi cần xả tồn kho | Đặt quote hai phía, rút quote khi biến động/thông tin bất lợi; giới hạn tồn kho |
| Nhà đầu tư tổ chức thực thi lệnh lớn (metaorder) | Hỗn hợp: chia nhỏ, dùng cả limit và market | Thực thi theo VWAP/TWAP/POV; tìm nơi có đối ứng để giảm impact |
| Trader kỹ thuật (retail và chuyên nghiệp) | Taker khi vào breakout, stop-loss | Đặt stop sau đỉnh/đáy, buy-stop vào breakout |
| Người chốt lời / người "fade" mức | Maker | Đặt sell-limit ngay dưới/tại đỉnh cũ |
| Hệ thống thanh lý ký quỹ | Taker cưỡng bức | Tạo lệnh market khi ký quỹ không đủ |

**[INTERPRETATION]** Không có cột "Smart Money" trong bảng này vì đó không phải một vai trò vi cấu trúc. Một quỹ lớn có thể là maker lúc này, taker lúc khác; có thể mua *vào* cú sweep, hoặc *chính nó* là bên bị stop.

### 1.5 Vì sao liquidity quyết định giá dịch chuyển

**[MARKET MECHANICS]** Bốn cơ chế đã được ghi nhận trong tài liệu vi cấu trúc:

1. **Giá dịch chuyển khi dòng lệnh marketable ăn hết độ sâu ở một mức.** Cont, Kukanov & Stoikov (2014) cho thấy biến động giá ngắn hạn được giải thích phần lớn bởi *mất cân bằng dòng lệnh* (order flow imbalance) chia cho độ sâu. Cùng một lượng lệnh mua → giá dịch chuyển nhiều khi sổ mỏng, ít khi sổ dày.
2. **Impact của một lệnh lớn là lõm** (tăng chậm dần theo kích thước — thường được mô tả bằng quy luật căn bậc hai) — xem Bouchaud et al. (2018), chương về metaorder.
3. **Impact có phần tạm thời và phần vĩnh viễn.** Sau khi một metaorder kết thúc, giá hồi lại một phần. Farmer, Gerig, Lillo & Waelbroeck (2013) đưa ra lập luận lý thuyết rằng phần còn lại xấp xỉ 2/3 đỉnh impact trong những điều kiện nhất định; các nghiên cứu thực nghiệm về metaorder (Moro et al. 2009; Bershova & Rakhlin 2013) ghi nhận hiện tượng hồi một phần sau khi lệnh lớn hoàn tất. Mô hình "propagator" (Bouchaud et al. 2004) mô tả impact của mỗi giao dịch phai dần theo thời gian.
4. **Lệnh có điều kiện tạo phản hồi dương.** Stop/liquidation biến chuyển động giá thành thêm lệnh cùng chiều (Osler 2005: price cascades).

> [!important] Hệ quả cho sweep
> Ghép (3) với (4): một cụm stop bị kích hoạt là một **đợt lệnh market "không mang thông tin"** (noninformative — Osler 2005 dùng đúng chữ này). Impact của nó, như mọi impact, có phần tạm thời. Nếu không có dòng lệnh mới nào theo sau, **giá có xu hướng trôi lại một phần mà không cần bất kỳ ai "đảo chiều" nó**. Đây là một lời giải thích cơ học cho hình dạng "xuyên rồi quay lại" — hoàn toàn không cần giả định ý định săn stop (LS-Sim-03, kịch bản A). **[TOY MODEL + MARKET MECHANICS]**

### 1.6 Chart nến cho biết gì và không cho biết gì

| Câu hỏi | Nến OHLC trả lời được? | Cần dữ liệu gì |
|---|---|---|
| Giá có giao dịch trên mức L không? | **Có** (high > L) | — |
| Giá ở trên L bao lâu? | Một phần (số nến; không biết trong nến) | Dữ liệu tick |
| Đóng cửa ở đâu so với L? | **Có** | — |
| Bao nhiêu stop đã bị kích hoạt? | **Không** | Sổ lệnh nội bộ sàn/dealer |
| Ai mua, ai bán ở trên L? | **Không** | Dữ liệu tài khoản (cơ quan quản lý) |
| Có "ý định" săn stop không? | **Không** | Không có trên dữ liệu thị trường |
| Độ sâu sổ lệnh trước khi chạm L? | **Không** | Level 2 / MBO |
| Khối lượng giao dịch tại L? | Không (nến chỉ có tổng volume nếu có) | Volume theo giá / footprint |
| Mức L có nổi bật với người khác không? | **Suy luận được** (PDH, EQH, số tròn…) | — |
| Phản ứng sau đó (rejection/acceptance/MSS)? | **Có — nhưng chỉ sau khi nó xảy ra** | — |

### 1.7 Liquidity vs Volume vs Order flow vs Volatility vs Resting orders

| Khái niệm | Là gì | Đo bằng | Nhầm lẫn phổ biến |
|---|---|---|---|
| **Liquidity** | *Khả năng* giao dịch nhanh, rẻ, khối lượng lớn | Spread, độ sâu, impact, độ hồi phục | Nghĩ rằng liquidity là một "mức giá" |
| **Volume** | *Lượng đã giao dịch* trong một khoảng | Khối lượng khớp | Volume cao ≠ liquidity cao (panic có volume cao, liquidity thấp) |
| **Order flow** | *Dòng* lệnh tới thị trường, có dấu (mua/bán chủ động) | Delta, OFI, tick rule | Nghĩ rằng nến xanh = order flow mua (một nến xanh có thể chứa nhiều bán chủ động bị hấp thụ) |
| **Volatility** | *Độ lớn* biến động giá | ATR, độ lệch chuẩn | Volatility cao thường đi cùng liquidity thấp (quan hệ nghịch, không phải đồng nghĩa) |
| **Resting orders** | Lệnh limit *đang nằm* trên sổ | Sổ lệnh | Lệnh nằm trên sổ có thể bị rút trước khi giá tới (spoofing là phiên bản bất hợp pháp; rút lệnh hợp pháp là chuyện thường ngày) |
| **Conditional orders** | Lệnh *chưa tồn tại* trên sổ cho tới khi điều kiện xảy ra | Không đo được từ bên ngoài | Đây là thứ ICT gọi là "liquidity trên đỉnh", nhưng nó **vô hình** |

### 1.8 "Liquidity trên chart" là cách nói tắt cho điều gì?

**Định nghĩa đề xuất (v0.1).** Khi nói "có buy-side liquidity trên đỉnh X", câu đầy đủ và trung thực là:

> *"Mức X nổi bật với nhiều người tham gia (vì nó là đỉnh/đáy cũ, số tròn, PDH, equal highs…). Do đó **có thể** có mật độ cao hơn bình thường của (a) lệnh mua có điều kiện ngay sau X (stop-loss của vị thế bán, buy-stop vào breakout) và (b) lệnh bán chờ ngay tại/trước X (chốt lời, người bán ở đỉnh). Nếu giá giao dịch qua X, (a) sẽ biến thành lệnh market; điều này có thể khuếch đại chuyển động hoặc cung cấp đối ứng cho người cần bán khối lượng lớn. Chúng ta không quan sát được khối lượng, vị trí chính xác, hay ai sẽ dùng chúng."*

**Tách metaphor khỏi literal fact:**

| Cách nói (metaphor) | Nghĩa đen có thể bảo vệ | Thứ không được ngầm định |
|---|---|---|
| "Liquidity nằm trên đỉnh" | Có thể có mật độ lệnh có điều kiện cao quanh mức nổi bật | Lệnh *chắc chắn* ở đó; số lượng; ai đặt |
| "Giá đi lấy liquidity" | Giá đã giao dịch qua mức đó | Giá "muốn", "cần", "được điều khiển" để làm vậy |
| "Pool đã bị lấy" | Giá đã giao dịch qua mức; lệnh *ở gần mức* (nếu có) đã được kích hoạt | Toàn bộ lệnh đã khớp; không còn lệnh nào sâu hơn |
| "Smart money hunted stops" | Có một đợt lệnh làm giá vượt mức, rồi giá quay lại | Ý định, danh tính, sự phối hợp |

### 1.9 Thang 6 tầng cho "Liquidity"

| Tầng | Giải thích |
|---|---|
| **L1 Trực giác** | Liquidity = có nhiều người sẵn sàng mua/bán ở một chỗ; ở đó mua bán dễ, giá ít bị xô lệch |
| **L2 Ví dụ** | Đỉnh 13.0 mà ai cũng thấy → người bán khống đặt "cắt lỗ nếu vượt 13.05", người chờ breakout cũng đặt "mua nếu vượt 13.05" |
| **L3 Trading** | Pool BSL/SSL = vùng có thể tập trung stop và lệnh breakout quanh swing high/low, PDH/PDL, EQH/EQL |
| **L4 Cơ chế** | Stop = lệnh tiêu thụ có điều kiện, phản hồi dương, vô hình; limit = cung cấp, phản hồi âm, hiển thị; giá dịch chuyển khi dòng marketable ăn hết độ sâu; impact có phần tạm thời |
| **L5 ICT** | ICT gọi vùng này là buy-side / sell-side liquidity; giá được mô tả là "tìm" (seek) liquidity, "raid"/"sweep"/"run" nó; liquidity là "nhiên liệu" cho lệnh lớn |
| **L6 Giới hạn** | Không đo được khối lượng stop từ chart; không biết lệnh nằm sâu bao nhiêu; không biết ai dùng; mọi câu về ý định là diễn giải |

---

## 2. Vì sao liquidity hình thành ở các mức nổi bật

### 2.1 Cơ chế gốc: salience và điểm hội tụ (focal point)

**[MARKET MECHANICS + INTERPRETATION]** Khi hàng nghìn người độc lập phải chọn một mức giá để đặt stop hay để vào lệnh breakout, họ không bàn với nhau — nhưng họ nhìn cùng một chart, học cùng sách, dùng cùng quy tắc ("stop ngay dưới đáy gần nhất"). Schelling (1960) gọi đây là **focal point**: lựa chọn mà mọi người đoán là người khác cũng sẽ chọn. Mức càng "hiển nhiên" (đỉnh rõ, số tròn, PDH, equal highs) thì càng nhiều người dùng nó làm tham chiếu → **có thể** càng nhiều lệnh dồn quanh nó.

Bằng chứng trực tiếp cho FX: Osler (2003, 2005) dùng sổ lệnh của Royal Bank of Scotland (8/1999–4/2000, 9,655 lệnh, tổng mệnh giá > 55 tỷ USD): lệnh stop-loss mua tập trung *ngay trên* số tròn (đuôi 00/50), lệnh stop-loss bán *ngay dưới*; take-profit tập trung *đúng tại* số tròn. Bằng chứng gián tiếp cho cổ phiếu: Kavajecz & Odders-White (2004) — mức S/R trùng đỉnh độ sâu sổ lệnh.

> [!warning] Điều bằng chứng KHÔNG nói
> Osler đo **số tròn**, không đo swing high/low theo nghĩa ICT. Kavajecz & Odders-White đo **lệnh limit** (cung cấp), không đo stop. Không nghiên cứu công khai nào trong danh sách tham khảo đo "mật độ stop ngay trên mọi swing high" hay "trên equal highs". Mở rộng từ số tròn sang swing là **[INTERPRETATION]** hợp lý nhưng chưa được kiểm chứng trực tiếp.

### 2.2 Ai đặt gì quanh một đỉnh cũ

| Người tham gia | Lệnh | Phía | Vị trí so với đỉnh H | Hiển thị? | Phản hồi |
|---|---|---|---|---|---|
| Người đang bán khống (short) | Stop-loss mua | MUA | Ngay **trên** H (+buffer) | Không | Dương |
| Người chờ breakout | Buy-stop vào lệnh | MUA | Ngay **trên** H | Không | Dương |
| Người đang mua (long) chốt lời | Sell-limit | BÁN | **Tại/dưới** H | Có | Âm |
| Người "bán ở đỉnh" (fade) | Sell-limit | BÁN | Tại/trên H | Có | Âm |
| Market maker | Quote hai phía | cả hai | Quanh giá | Có | Tùy tồn kho |
| Người bán quyền chọn / dealer hedge delta | Lệnh hedge (thường thuật toán) | tùy gamma | Quanh strike lớn | Không | Có thể dương (short gamma) hoặc âm (long gamma) |
| Hệ thống thanh lý (đòn bẩy) | Lệnh market cưỡng bức | MUA (short bị thanh lý) | Trên H, theo đòn bẩy | Không | Dương |

**Nhận xét quan trọng:** quanh một đỉnh có **cả lệnh mua có điều kiện** (stop, breakout, thanh lý — vô hình, phản hồi dương) **lẫn lệnh bán chờ** (chốt lời, fade — hiển thị, phản hồi âm). Kết quả khi giá chạm tới phụ thuộc vào tỷ lệ giữa hai nhóm này và dòng lệnh mới tới — đây chính là nội dung của LS-Sim-04.

### 2.3 Bảng theo loại mức

| Loại mức | Vì sao nổi bật | Lệnh có thể tập trung | Bằng chứng | Ghi chú |
|---|---|---|---|---|
| **Swing high/low trước đó** | Quy tắc stop phổ biến "sau đỉnh/đáy gần nhất" | Stop, breakout | [INTERPRETATION] | Mọi swing không như nhau — §2.6 |
| **Equal highs/lows** | Hai lần thất bại tại cùng mức tạo đường "hiển nhiên" | Stop dồn sát một mức | [INTERPRETATION]; Garzarelli et al. 2014 (hiệu ứng nhớ, thang giây) | Tự hình thành trên random walk (LS-Sim-07) |
| **Session high/low** (Asia, London) | Mốc thời gian chung; được đánh dấu bởi indicator phổ biến | Stop của trade trong phiên | [ICT FRAMEWORK] | Ý nghĩa phụ thuộc instrument (FX khác index) |
| **PDH/PDL** | Mốc ngày — mọi nền tảng hiển thị | Stop, breakout, lệnh của trader ngày | [INTERPRETATION] | Xem [[59-Daily-Bias]] §3.8: ít nhất một trong hai mức PDH/PDL bị lấy ở ~90% số ngày trên random walk |
| **PWH/PWL, PMH/PML** | Mốc tuần/tháng | Stop của swing trader | [INTERPRETATION] | Ít sự kiện → khó thống kê |
| **Số tròn** (1.0800, 20,000) | Tâm lý số tròn | Take-profit tại số tròn; stop ngay ngoài | **Osler 2003/2005** (FX) | Bằng chứng mạnh nhất trong bảng |
| **Support/Resistance nhiều lần test** | Được nhìn thấy bởi nhiều trường phái | Limit (cung cấp) + stop sau mức | **Kavajecz & Odders-White 2004** (depth) | Test nhiều lần cũng có thể = hấp thụ đang cạn |
| **Biên dealing range / consolidation** | Biên vùng đi ngang — "hộp" dễ thấy | Stop, breakout | [INTERPRETATION] | Biên range ≠ pool (§17.1) |
| **Strike quyền chọn lớn / barrier** | Hedging của dealer | Lệnh hedge, "phòng thủ barrier" | [MARKET MECHANICS] (BIS 2017 về hedging liên quan quyền chọn) | Chủ yếu FX lớn, index, vàng |

### 2.4 Điều có khả năng vs điều quan sát được

| Câu | Khả năng | Quan sát được trên chart? |
|---|---|---|
| "Có nhiều stop trên PDH hơn trên một mức ngẫu nhiên" | Hợp lý (salience) | Không |
| "Stop nằm trong vòng vài tick sau mức" | Hợp lý cho FX số tròn (Osler) | Không |
| "Giá đã giao dịch qua PDH" | — | **Có** |
| "Sau khi qua PDH, giá tăng tốc" | Kiểm được nếu có dữ liệu tick | Một phần (độ dài nến) |
| "Ai đó đã cố tình đẩy giá tới PDH để lấy stop" | Không loại trừ, không chứng minh | **Không** |

### 2.5 Equal Highs / Equal Lows

![[LS-Deep-08-Equal-Highs-Co-The-vs-Chac-Chan.svg|900]]
*Hình LS-Deep-08: EQH có cơ chế salience hợp lý; "EQH là nam châm hút giá" là giả thuyết chưa có bằng chứng.*

**Vì sao hai đỉnh gần bằng nhau có thể trở thành liquidity reference (L1 → L4):**

- **L1:** hai lần giá đụng trần rồi rơi → ai cũng thấy "trần". Người cược trần sẽ giữ đặt "nếu thủng trần thì tôi thua"; người cược trần sẽ vỡ đặt "nếu thủng trần thì tôi mua". Hai nhóm đặt **cùng một chỗ**.
- **L3:** EQH = double top/triple top trong ngôn ngữ cổ điển. Người short từ H1 và H2 đặt stop trên max(H1, H2); người chờ "phá double top" đặt buy-stop ở cùng vị trí.
- **L4:** nếu các stop dồn trong một dải giá hẹp, khi giá chạm tới chúng kích hoạt *gần như đồng thời* → đợt mua market đậm đặc → xuyên nhanh (LS-Sim-04: mật độ cao trong dải hẹp λ nhỏ cho cascade xuyên ngắn nhưng gắt) **[TOY MODEL]**.
- **L5:** ICT gọi đây là "relative equal highs/lows" — "smooth" highs/lows được coi là liquidity rõ ràng, thường là mục tiêu (DOL) hoặc inducement.
- **L6:** Chart không cho biết có bao nhiêu stop ở đó; và *chính việc EQH được gọi là "liquidity rõ ràng" trong cộng đồng* có thể khiến người ta đặt stop xa hơn hoặc tránh đặt ở đó (phản xạ — xem [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]]).

**"Có thể" vs "chắc chắn":**

| Mệnh đề | Trạng thái |
|---|---|
| EQH **có thể** chứa mật độ stop cao hơn một đỉnh đơn | [HYPOTHESIS] — có cơ chế, chưa có đo lường trực tiếp |
| EQH **chắc chắn** chứa liquidity | **Sai** — không có cách nào xác nhận từ chart |
| Giá **sẽ** quay lại lấy EQH | **Sai về dạng mệnh đề** — xác suất chạm mức phụ thuộc trước hết vào khoảng cách và thời gian |
| EQH bị lấy *nhanh hơn* đỉnh đơn ở cùng khoảng cách | [HYPOTHESIS] HYP-LS-006 — trên random walk hai đường trùng nhau (LS-Sim-07) |
| Sau khi xuyên EQH, giá *tăng tốc mạnh hơn* sau khi xuyên đỉnh đơn | [HYPOTHESIS] HYP-LS-007 — đây mới là dấu vết trực tiếp của cụm stop (kiểu Osler) |

![[LS-Sim-07-Equal-Highs-Null.png]]
*Hình LS-Sim-07 **[SIMULATION]**: (A) EQH tự xuất hiện trên random walk — 1.5 / 2.8 / 5.4 / 8.0 lần mỗi 1,000 nến M15 với dung sai 0.05 / 0.1 / 0.2 / 0.3 ATR. (B) Xác suất mức bị xuyên trong 40 nến theo khoảng cách: EQH và đỉnh đơn trùng nhau — trên một quá trình Markov, khoảng cách là tất cả.*

**Ba bẫy khi dùng EQH:**
1. **Dung sai co giãn.** "Gần bằng" với 0.05 ATR hay 0.3 ATR cho ra số EQH khác nhau ~5 lần. Phải khai báo dung sai **trước** khi đánh dấu, không chỉnh theo chart.
2. **Khung thời gian.** Hai đỉnh M5 "bằng nhau" thường là nhiễu bên trong một nến H1. Ý nghĩa của EQH thuộc về khung mà hai swing được xác nhận (nguyên tắc R7 kế thừa từ Dealing Range DR-v0.1: *ý nghĩa thuộc về swing, không thuộc về chart bạn đang nhìn*).
3. **"Engineered EQH".** Câu chuyện "EQH quá đều, ngay trước POI = mồi được tạo ra" là diễn giải hậu kiểm. Nếu muốn dùng, phải ghi nhãn "engineered?" **trước** khi biết kết quả, rồi đếm tỷ lệ sau 30+ trường hợp. *(Vault có hình `Liquidity-Sweep-EdgeB-EngineeredEQH.svg` từ một phiên trước, chứa thống kê chưa xác minh — không được nhúng vào note này; xem Changelog.)*

### 2.6 Swing high/low như liquidity — khi nào một swing trở thành tham chiếu có ý nghĩa?

**Swing ≠ liquidity.** Mọi đoạn đi lên rồi đi xuống đều tạo một swing high theo định nghĩa fractal; nếu mọi swing đều là pool thì "giá lấy liquidity" mô tả *mọi* chuyển động và không còn nội dung thông tin. Câu hỏi đúng là: *swing nào đủ nổi bật để nhiều người dùng làm tham chiếu?*

Theo framework phân loại swing của project (Level 1 micro → Level 5 HTF major) và bộ biến S/L/D/R/T:

| Biến | Câu hỏi | Ảnh hưởng tới "liquidity significance" |
|---|---|---|
| **S** — structural | Swing có bảo vệ cấu trúc (protected high/low) / định nghĩa dealing range không? | Swing cấu trúc được nhiều người dùng đặt stop "đúng sách" |
| **L** — liquidity | Đã có liquidity bị lấy để tạo swing này không? Swing này có tạo ra pool mới không? | Swing hình thành bằng một cú sweep thường có cực trị rõ (wick) — tham chiếu dễ thấy |
| **D** — displacement | Leg rời khỏi swing có displacement không? | Leg mạnh làm swing "nổi tiếng" (nhiều người thấy), và tạo FVG |
| **R** — reaction | Phản ứng từ swing lớn bao nhiêu (theo ATR)? | Phản ứng lớn = nhiều người nhớ |
| **T** — timeframe | Swing được xác nhận ở khung nào? | D1 swing được nhìn bởi nhiều người hơn M5 swing |

Đề xuất v0.1: một swing được đưa vào **danh sách mức tham chiếu** nếu thỏa các cổng G1–G5 (§9.3) và có LSS vượt ngưỡng khai báo trước. Danh sách được chốt **trước phiên** (RULE-LS-001). Một swing không có trong danh sách mà bị xuyên → ghi là "breach of unlisted level", **không** gọi là sweep.

---

## 3. Liquidity pool, Buy-side và Sell-side Liquidity

### 3.1 Level, zone, pool, cluster — bốn từ, bốn đối tượng

Cộng đồng ICT dùng các từ này lẫn lộn. Không có định nghĩa chính thức thống nhất; dưới đây là **định nghĩa làm việc v0.1** để note và journal dùng nhất quán.

| Thuật ngữ | Định nghĩa làm việc (v0.1) | Quan sát được? | Ví dụ |
|---|---|---|---|
| **Liquidity level** (mức) | Một giá cụ thể L, xác định ex-ante, được giả định là tham chiếu chung | **Có** (giá) | PDH = 1.0868 |
| **Liquidity zone** (vùng) | Dải [L, L + w] phía bên kia mức, nơi lệnh có điều kiện được giả định nằm; w thường tính theo ATR hoặc tick | Biên do mình chọn | 1.0868–1.0875 |
| **Liquidity pool** (pool) | *Tập hợp lệnh* (có điều kiện + chờ) được giả định tập trung trong zone | **Không** | "BSL trên PDH" |
| **Liquidity cluster** (cụm) | Nhiều level nằm sát nhau (≤ x·ATR) — ví dụ PDH + Asia high + số tròn | Có (các mức) | PDH 1.0868, Asia H 1.0871, 1.0870 |

**Hệ quả:** khi viết "giá lấy pool", điều bạn thực sự quan sát là "giá giao dịch qua level/zone". Pool là phần suy luận. Cluster thì quan trọng thực hành: nhiều mức sát nhau có thể là một pool lớn — hoặc là nhiều nhãn cho cùng một vùng (đếm trùng, xem LSS biến V).

### 3.2 Buy-side Liquidity (BSL)

![[LS-Deep-02-BSL-SSL-Ai-Mua-Ai-Ban.svg|900]]
*Hình LS-Deep-02: BSL/SSL đặt tên theo phía của lệnh chờ kích hoạt. BSL là đối ứng cho người muốn BÁN; SSL là đối ứng cho người muốn MUA.*

- **Nằm ở đâu?** Phía **trên** các đỉnh tham chiếu: swing high, EQH, PDH, PWH, Asia/London high, số tròn phía trên.
- **Vì sao gọi là "buy-side"?** Vì các lệnh có điều kiện ở đó, khi kích hoạt, là lệnh **MUA**: stop-loss của người đang short (mua lại để đóng), buy-stop vào breakout, thanh lý vị thế short có đòn bẩy.
- **Có phải toàn bộ là lệnh mua không?** **Không.** Cùng vùng đó có lệnh **BÁN** chờ (sell-limit chốt lời của người long, người bán ở đỉnh). Chính các lệnh bán này là thứ "ăn" lệnh mua bị kích hoạt. Tên "buy-side" chỉ nói về nhóm lệnh có điều kiện.
- **Ai được lợi khi BSL bị kích hoạt?** Người cần **bán** lượng lớn: họ có đối ứng mua đột ngột để khớp mà không tự đẩy giá xuống. Đây là logic cơ học đằng sau câu chuyện ICT "lấy BSL rồi giảm". **[MARKET MECHANICS]** về logic khớp lệnh; **[INTERPRETATION]** về việc ai thực sự đã bán.

### 3.3 Sell-side Liquidity (SSL)

Đối xứng: phía **dưới** đáy tham chiếu; lệnh có điều kiện là **BÁN** (stop-loss của long, sell-stop breakdown, thanh lý long); đối ứng cho người cần **mua** lượng lớn. Cùng vùng có buy-limit chờ (chốt lời short, người bắt đáy).

### 3.4 Vì sao stop của short trên đỉnh trở thành buy-side liquidity — ví dụ số

```text
EURUSD. Đỉnh cũ (PDH) = 1.0868. Giá hiện tại 1.0850.

Trader A short ở 1.0860, stop ở 1.0872  → nếu giá chạm 1.0872: MUA 1 lot (market)
Trader B short ở 1.0865, stop ở 1.0870  → nếu giá chạm 1.0870: MUA 2 lot
Trader C chờ breakout: buy-stop 1.0871  → nếu giá chạm 1.0871: MUA 1 lot
Trader D long từ 1.0820, sell-limit TP 1.0869 → đang chờ BÁN 3 lot tại 1.0869
Quỹ E muốn BÁN 10 lot quanh 1.0870 mà không đạp giá

Giá lên 1.0869 → D bán 3 lot cho người mua đang đẩy giá.
Giá lên 1.0870 → B kích hoạt: MUA 2 lot market.
Giá lên 1.0871 → C kích hoạt: MUA 1 lot.
Giá lên 1.0872 → A kích hoạt: MUA 1 lot.
→ 4 lot mua market xuất hiện trong vài giây. Quỹ E có thể đặt bán vào đúng lúc này.
```

Ba điều ví dụ cho thấy:
1. Nếu E **không tồn tại**, 4 lot mua đó vẫn phải khớp với ai đó (D, market maker, các limit khác) — giá có thể vọt lên rồi trôi lại khi đợt mua kết thúc (§1.5).
2. Nếu E **tồn tại và bán mạnh**, giá có thể đảo nhanh — chuỗi "sweep → displacement" của ICT.
3. Nếu thay vì E, có một **người mua lớn F** tới đúng lúc, 4 lot stop cộng với F đẩy giá đi tiếp — breakout/run.

Trên chart, cả ba trường hợp đều bắt đầu bằng **cùng một nến** vượt 1.0868.

### 3.5 Nghịch lý tên gọi và cách tránh nhầm

| Câu dễ nhầm | Câu chính xác |
|---|---|
| "BSL = nơi người ta mua" | BSL = nơi **lệnh mua có điều kiện** có thể nằm; người hưởng lợi là **người bán** |
| "Giá lấy BSL → bullish" | Giá giao dịch qua vùng BSL → **chưa có hướng**; hướng phụ thuộc phân xử sau đó |
| "Lấy SSL rồi thì chỉ có lên" | Lấy SSL **tiêu thụ** lệnh bán có điều kiện ở gần mức; nó không tạo ra lệnh mua |
| "Pool càng lớn càng chắc đảo" | Pool lớn + sổ mỏng → cascade đi xa hơn (LS-Sim-04) — có thể thành acceptance |

---

## 4. Vì sao giá di chuyển tới liquidity?

### 4.1 Bảy cơ chế và một baseline

![[LS-Deep-04-Bay-Co-Che-Gia-Toi-Liquidity.svg|900]]
*Hình LS-Deep-04: Không cơ chế nào cần giả định một "Smart Money" toàn năng. Ô H là phép thử bắt buộc: random walk cũng "tìm tới" mức gần.*

#### Cơ chế A — Kích hoạt stop (stop activation)
- **Mô tả:** khi giá chạm mức có stop, stop trở thành lệnh market cùng chiều → đẩy giá tiếp → có thể kích hoạt stop kế tiếp (cascade).
- **Dấu vết quan sát:** tăng tốc ngay sau mức; nến dài; wick dài nếu sổ phía sau dày lại.
- **Bằng chứng:** Osler (2005) — price cascade sau khi vượt vùng tập trung stop-loss FX, kéo dài hàng giờ; Fett & McPhail (2017) — stop chiếm tỷ trọng nhỏ nhưng tăng mạnh trong ngày biến động. **[MARKET MECHANICS]**
- **Giới hạn:** cơ chế này giải thích vì sao giá **đi qua** mức nhanh; nó **không** giải thích vì sao giá **tới** mức, và dự báo *tiếp diễn* nhiều hơn đảo chiều.

#### Cơ chế B — Nhu cầu khớp lệnh lớn (order execution)
- **Mô tả:** người cần khớp lượng lớn muốn đối ứng dồi dào để giảm impact. Lệnh có điều kiện bị kích hoạt là nguồn đối ứng tập trung, đoán trước được vị trí.
- **Dấu vết:** không quan sát được ý định; chỉ thấy *có thể* là hấp thụ (giá đứng yên dù volume lớn — nếu có dữ liệu volume).
- **Bằng chứng:** logic chuẩn của lý thuyết impact (Kyle 1985; Bouchaud et al. 2018). Không có bằng chứng công khai rằng lệnh lớn *thường xuyên* chủ động tìm tới cụm stop. **[INTERPRETATION]**
- **Giới hạn:** Fett & McPhail (2017) cho thấy stop chỉ là một phần nhỏ khối lượng — với nhiều thị trường, lệnh limit hiển thị và latent liquidity lớn hơn stop rất nhiều. "Lệnh lớn **cần** sweep để vào hàng" (v1 W0) là phóng đại (§4.5).

#### Cơ chế C — Price discovery
- **Mô tả:** giá là một quá trình dò tìm mức mà cung cầu cân bằng. Vượt qua một mức cũ là một "thử nghiệm" thông tin: nếu có người sẵn sàng giao dịch ở mức mới → acceptance; nếu không → rejection.
- **Dấu vết:** acceptance (giá ở lại, có giao dịch hai chiều ở vùng mới) hoặc rejection (giá quay về nhanh).
- **Bằng chứng:** khung chuẩn của vi cấu trúc và Auction Market Theory. **[MARKET MECHANICS]**
- **Giới hạn:** mô tả được kết quả, khó dự báo trước nhánh nào.

#### Cơ chế D — Người tham gia breakout
- **Mô tả:** trader kỹ thuật vào lệnh khi phá mức (buy-stop) → dòng lệnh cùng chiều tại mức nổi bật.
- **Dấu vết:** volume tăng tại mức (nếu có dữ liệu).
- **Bằng chứng:** Osler (2003) về đặt lệnh quanh số tròn; Kavajecz & Odders-White (2004) về depth tại S/R. **[MARKET MECHANICS]**; hiệu quả của chiến lược breakout là chuyện khác.

#### Cơ chế E — Thuật toán tìm thanh khoản và market making
- **Mô tả:** thuật toán thực thi (VWAP/TWAP/POV, liquidity-seeking) chia lệnh theo nơi có độ sâu; market maker điều chỉnh quote theo tồn kho, có thể rút quote trước mức nhạy cảm.
- **Dấu vết:** chỉ thấy bằng dữ liệu sổ lệnh/khớp lệnh chi tiết.
- **Bằng chứng:** Harris (2003); Bouchaud et al. (2018). **[INTERPRETATION]** khi áp dụng cho một sweep cụ thể.

#### Cơ chế F — Kích hoạt có chủ đích
- **Mô tả:** một bên đẩy giá tới cụm stop để hưởng chuyển động dây chuyền, hoặc giao dịch khai thác người bị buộc phải đóng vị thế. Brunnermeier & Pedersen (2005, "Predatory Trading") mô hình hóa việc bên biết người khác phải bán sẽ bán trước rồi mua lại, làm giá *vượt quá* (overshoot) rồi hồi.
- **Dấu vết:** **không phân biệt được** với cơ chế A trên OHLC.
- **Bằng chứng:** có mô hình lý thuyết và có các hình thức thao túng bị cấm được cơ quan quản lý mô tả; không có cách xác nhận cho một sự kiện cụ thể từ chart. **[INTERPRETATION]**
- **Lưu ý:** đây là cơ chế duy nhất khớp với câu chuyện "stop hunt có chủ đích". Nó có thể xảy ra; nó không phải lời giải thích *mặc định*.

#### Cơ chế G — Động lực đấu giá (Auction Market Theory)
- **Mô tả:** giá "quảng bá" (advertise) tới các mức xa hơn để tìm đối ứng; khi tới mức không còn ai giao dịch ngược chiều thì xuất hiện "excess" (đuôi dài) và giá quay về vùng giá trị.
- **Dấu vết:** đuôi phân phối volume; wick dài + quay về value area.
- **Bằng chứng:** khung lý thuyết thực hành (Steidlmayer / Market Profile); ít bằng chứng thống kê công khai. **[FRAMEWORK — AMT]**

### 4.2 H — Baseline hình học (bắt buộc kiểm trước mọi cơ chế khác)

**[MATHEMATICAL]** Với chuyển động Brown không drift bắt đầu ở x, giữa hai mức a < x < b, xác suất chạm b trước a là (x − a)/(b − a) — bài toán gambler's ruin. Dịch sang ngôn ngữ liquidity: *pool nào gần hơn sẽ bị lấy trước với xác suất cao hơn, chỉ vì nó gần hơn.*

| Khoảng cách tới pool gần (ATR) | Tới pool xa (ATR) | P(pool gần bị chạm trước) |
|---:|---:|---:|
| 1 | 1 | 50% |
| 1 | 2 | 67% |
| 1 | 3 | **75%** |
| 1 | 4 | 80% |
| 0.5 | 3 | 86% |
| 2 | 3 | 60% |

Đây là lý do mà mọi quan sát kiểu "giá luôn lấy thanh khoản gần nhất trước" phải được so với bảng này. Nếu 78% lần giá chạm pool gần trước khi pool cách gấp ba, đó gần như *chỉ là hình học*.

![[LS-Sim-02-Geometry-Baseline.png]]
*Hình LS-Sim-02 **[SIMULATION]**: (A) Trên 23,140 lần xuyên swing high M15 của random walk, tỷ lệ "chạm pool đối diện trước stop" nằm trên đường chéo p_null ở mọi khoảng cách — cho cả nhóm "đóng lại bên trong" (sweep) lẫn "đóng vượt" (break). Nhóm sweep: thắng 20.6%, R:R trung vị 5.1, expectancy +0.02R (SE 0.03) với fill thực tế. (B) Cùng tập sự kiện: "thành công" = 73%, 66% hay 21% tùy định nghĩa; expectancy ≈ 0.*

Hai bổ sung cho bảng:
- **Có drift:** với drift μ và độ biến động σ, công thức đổi thành P = (1 − e^{−2μ(x−a)/σ²}) / (1 − e^{−2μ(b−a)/σ²}) (cho mức trên b). Drift theo hướng nào thì pool phía đó được lợi.
- **Có cửa sổ thời gian:** khi chỉ xét trong T giờ (ví dụ trong ngày), cả hai pool có thể không bị chạm; xác suất phụ thuộc thêm vào σ√T. Xem [[59-Daily-Bias]] §8.2 về first-passage có cửa sổ.

### 4.3 "Price seeks liquidity" — định luật hay mô tả?

**Kết luận: mô tả, không phải định luật.** Lập luận:

1. **Phần hình học (H):** giá luôn sẽ chạm *một* mức nào đó trước; mức gần có lợi thế. Mô tả "giá đi tìm liquidity" đúng một cách tầm thường.
2. **Phần cơ chế (A–G):** có những cơ chế thật khiến mức nổi bật có hành vi khác mức ngẫu nhiên — tăng tốc khi xuyên (A, D), phản ứng tại mức (limit tập trung, take-profit), có thể là hấp thụ (B). Đây là phần có thể có thông tin.
3. **Phần selection bias:** người quan sát đánh dấu rất nhiều mức; mức bị chạm được nhớ và gọi là "pool bị lấy", mức không bị chạm bị quên hoặc được giải thích lại ("chưa tới lúc", "là DOL tuần sau"). Không có danh sách ex-ante thì không thể tính tỷ lệ.
4. **Phần phản xạ:** khi đủ nhiều người tin giá sẽ lấy EQH, hành vi của họ (vào lệnh breakout trước, dời stop) thay đổi chính mật độ lệnh ở đó ([[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]]).

**Câu hỏi kiểm chứng được** thay cho "price seeks liquidity": *"Với danh sách mức ex-ante, xác suất mức thuộc nhóm X (EQH, PDH, LSS cao) bị chạm trong T có lớn hơn xác suất của mức đối chứng cùng khoảng cách không?"* (HYP-LS-006, Event Study §26).

### 4.4 Quan sát — cơ chế có thể — diễn giải ICT — giả thuyết — không biết

![[LS-Deep-03-Thang-Nhan-Thuc-5-Tang.svg|900]]
*Hình LS-Deep-03: Một sự kiện, năm tầng câu chữ. Mỗi tầng cần một loại bằng chứng khác nhau.*

Áp dụng cho câu mẫu trong brief:

| Tầng | Câu |
|---|---|
| **Observable** | Giá giao dịch trên đỉnh trước rồi close lại dưới nó |
| **Possible market mechanism** | Lệnh có điều kiện có thể đã bị kích hoạt và khớp quanh/trên mức đó |
| **ICT interpretation** | Đỉnh trước đại diện buy-side liquidity, và nó đã bị sweep |
| **Hypothesis** | Cú di chuyển có thể đã tiêu thụ liquidity trước khi đảo chiều; sau loại sự kiện này, P(pool đối diện trước stop) > p_null |
| **Unknown** | Danh tính, ý định, việc có tổ chức nào "engineer" cú di chuyển — không suy ra được từ OHLC |

### 4.5 Rà soát "Tầng WHY nền tảng" (W0) của v1

v1 có một đoạn giải thích nền tảng cho mọi War Story. Nó được giữ nguyên văn dưới đây vì là một phần lịch sử tư duy của bạn; sau đó là rà soát từng claim theo hệ thống nhãn.

> [!quote]- Nguyên văn W0 (v1) — bấm để mở
> Trước các tình huống, cần hiểu sweep ở tầng cơ chế — vì mọi rule bên dưới đều suy ra từ đây:
>
> 1. **Vì sao phải quét stop? Vì stop là thanh khoản ĐƯỢC BẢO ĐẢM.** Một quỹ muốn mua 2,000 hợp đồng NQ không thể bấm market buy — họ sẽ tự đẩy giá lên trước khi khớp xong (self-impact). Họ cần một khối lệnh **bán** lớn xuất hiện cùng lúc, tại một giá. Stop loss của người đang Long là *lệnh bán market được hẹn giờ sẵn tại một mức giá biết trước* — kích hoạt cả cụm cùng lúc. Quét xuống dưới đáy không phải trò ác ý; nó là **cách duy nhất để size lớn vào hàng mà không tự phá giá của mình**. Đây là lý do sweep xuất hiện trước gần như mọi leg lớn: leg lớn *cần* cú quét để tồn tại.
> 2. **Vì sao đảo chiều theo sau? Vì bên khởi xướng giờ phải BẢO VỆ tồn kho.** Sau khi khớp xong 2,000 hợp đồng ở đáy quét, bên mua có vị thế khổng lồ với giá vốn ngay tại vùng sweep. Họ không để giá quay lại vùng đó (sẽ lỗ + mất thanh khoản đã gom) → họ đẩy giá đi ngay. **Displacement chính là dấu vết của hành vi bảo vệ tồn kho này** — và đó là lý do "nến sau sweep phải là displacement" không phải quy tắc thẩm mỹ mà là chẩn đoán: không displacement = không có ai vừa gom hàng = cú xuyên mức đó không phải sweep.
> 3. **Vì sao reclaim là ranh giới? Vì nó phân xử AI thắng phiên đấu giá tại mức đó.** Tại đáy bị xuyên có hai dòng lệnh đối đầu: dòng bán (stop bị kích + breakout seller mới) và dòng mua (bên gom). Giá đóng nến trở lại trong range = dòng mua đã **nuốt hết** dòng bán — phe bán tại mức đó đã cạn đạn. Giá giữ ngoài (acceptance) = dòng bán còn sponsor thật → break. Reclaim không phải "pattern nến"; nó là kết quả trận đấu.
>
> Ba cơ chế này giải thích luôn các W bên dưới: reclaim doji = trận đấu chưa ngã ngũ (W1); double sweep = bên gom cần nhiều thanh khoản hơn một pool nông cung cấp được (W2); news spike = thanh khoản bị RÚT khỏi sổ lệnh thay vì được gom (W3).

| Claim của W0 (v1) | Nhãn | Rà soát v2 |
|---|---|---|
| "Stop là thanh khoản ĐƯỢC BẢO ĐẢM" | [INTERPRETATION] — **phóng đại** | Stop không được bảo đảm về khối lượng, vị trí, hay sự tồn tại; nó vô hình và có thể được dời/hủy. Stop chỉ chiếm phần nhỏ hoạt động giao dịch trên futures lớn (Fett & McPhail 2017). Đúng hơn: *"stop là một nguồn đối ứng có thể đoán được vị trí gần đúng"* |
| "Quét xuống dưới đáy là cách DUY NHẤT để size lớn vào hàng" | **Sai về dạng mệnh đề** | Lệnh lớn được thực thi hằng ngày bằng thuật toán chia nhỏ, khớp vào lệnh limit hiển thị và latent liquidity, block trade, dark pool (cổ phiếu)… Sweep là *một* nguồn đối ứng, không phải nguồn duy nhất |
| "Leg lớn CẦN cú quét để tồn tại" | [HYPOTHESIS] — chưa có bằng chứng | Kiểm được: tỷ lệ leg lớn (≥ x ATR) bắt đầu ngay sau một breach của mức ex-ante so với baseline random walk (HYP-LS-001 biến thể). Trên random walk, mọi leg đều bắt đầu từ một cực trị, và cực trị thường vừa vượt một swing nào đó |
| "Bên khởi xướng phải BẢO VỆ tồn kho → displacement là dấu vết" | [INTERPRETATION] | Một lời giải thích có thể. Lời giải thích thay thế: displacement là phần *thông tin* mới (tin, flow lớn) hoặc chỉ là sự kết thúc của đợt mua và impact tạm thời phai (LS-Sim-03 A/C). Không phân biệt được trên OHLC |
| "Không displacement = không có ai vừa gom hàng = không phải sweep" | Quy tắc phân loại hợp lý — **nhưng không phải chẩn đoán order flow** | Giữ như **RULE** phân loại (RULE-LS-003), bỏ phần khẳng định về ai đã làm gì |
| "Reclaim phân xử AI thắng phiên đấu giá tại mức" | [MARKET MECHANICS] một phần | Close quay lại trong range cho biết *trong khung thời gian của nến đó*, phía vừa đẩy giá qua mức không duy trì được giá ở bên kia mức. Nó không cho biết "phe bán đã cạn đạn" — một nến H1 đóng lại trong range có thể chứa một nến M5 acceptance (LS-Sim-01B) |

**Điều giữ lại từ W0:** trực giác rằng *sweep là một trận đấu giữa dòng lệnh vừa bị kích hoạt và dòng lệnh đối ứng*, và kết quả trận đấu đọc được qua reclaim/displacement. v2 chỉ đổi giọng từ "chắc chắn" sang "có thể", và tách *quy tắc phân loại* khỏi *khẳng định về order flow*.

---

## 5. Liquidity Sweep chính xác là gì?

### 5.1 L1 — Giải thích cho trẻ 5 tuổi

Có một hàng rào (đỉnh cũ). Sau hàng rào có rất nhiều quả bóng bay buộc dây (lệnh chờ) — không ai nhìn thấy, nhưng ai cũng đoán là có, vì ai cũng thích buộc bóng ngay sau hàng rào. Giá là một quả bóng lăn. Khi bóng lăn qua hàng rào, dây đứt và bóng bay vụt lên (lệnh bị kích hoạt). Rồi có hai chuyện:
- Quả bóng lăn tiếp ra xa → **đi qua thật** (breakout / acceptance).
- Quả bóng lăn ngược về bên này hàng rào → **"quét" xong rồi quay về** (sweep / rejection).

Lúc bóng vừa qua hàng rào, **chưa ai biết** chuyện nào sẽ xảy ra.

### 5.2 L2 — Chuỗi giá đơn giản

```text
         wick ┐
              │  ← giá giao dịch trên L (lệnh có điều kiện có thể khớp ở đây)
L ────────────┼──────────────────────────
           ┌──┴┐
     ┌─┐   │   │  ← close của nến xuyên nằm DƯỚI L
   ┌─┘ └─┐ │   │ ┌─┐
   │     └─┘   └─┘ └─┐   ← nến sau tiếp tục dưới L (rejection giữ)
                     └─┐
                       └── …
```

### 5.3 L3 — Trading

Sweep (raid, run on stops, stop hunt) = giá vượt qua một đỉnh/đáy tham chiếu trong thời gian ngắn rồi quay lại bên trong vùng giá trước đó. Trader dùng nó như dấu hiệu "liquidity đã bị lấy" và tìm entry theo hướng ngược lại *sau khi có xác nhận*.

### 5.4 L4 — Cơ chế thị trường: điều gì có thể xảy ra với lệnh

1. Giá tiến tới L; lệnh limit bán quanh L có thể được thêm (fade) hoặc rút (market maker tránh rủi ro).
2. Lệnh marketable mua ăn hết lệnh bán ở L → giá in L + 1 tick.
3. Lệnh có điều kiện ở L + 1… kích hoạt → thêm lệnh mua market → giá tiếp tục, phụ thuộc độ sâu (LS-Sim-04).
4. Đợt mua có điều kiện cạn (đã khớp hết lớp gần mức).
5. Từ đây, giá đi đâu phụ thuộc vào dòng lệnh **mới**: không ai → impact tạm thời phai, giá trôi về; người bán xuất hiện → đảo nhanh; người mua tiếp tục → acceptance (LS-Sim-03).

### 5.5 L5 — Cách ICT dùng thuật ngữ **[ICT FRAMEWORK]**

Trong tài liệu cộng đồng ICT, "liquidity sweep" (còn gọi raid, stop run, stop hunt, liquidity grab) mô tả việc giá đi tới vùng BSL/SSL để "lấy" liquidity rồi **đảo chiều**; nó thường được đặt trong chuỗi *sweep → MSS → displacement → FVG → entry* (ICT 2022 Model), trong chu kỳ AMD (sweep = manipulation / Judas swing) và trong mô hình Turtle Soup. Ngược lại, "liquidity run" là khi giá lấy liquidity rồi **đi tiếp** theo hướng chính. Một quy tắc thực hành phổ biến (innercircletrader.net): *nếu hướng HTF đồng thuận với phía vừa bị lấy, kỳ vọng run; nếu ngược, kỳ vọng sweep*. Lưu ý: đây là quy tắc **dự báo** dựa trên bối cảnh — nó cần được kiểm chứng như một giả thuyết (HYP-LS-012), không phải định nghĩa.

### 5.6 L5' — Định nghĩa vận hành v0.1 (cho journal và code)

> [!example] DEF-LS-04 — Liquidity Sweep (v0.1, HEURISTIC)
> Cho một mức tham chiếu **L** (BSL; SSL đối xứng) với known_at < t₀, thỏa các cổng G1–G5 (§9.3). Gọi **j** là nến đầu tiên sau known_at có `high_j > L + ε`.
> - **Sweep** xảy ra nếu tồn tại t ∈ [j, j + k] sao cho `close_t < L − δ`, **và** trước t không có acceptance (không có 2 close liên tiếp > L, không có close > L + 0.5·ATR).
> - **Thời điểm biết (known_at của nhãn)** = close của nến t.
> - **Cực trị sweep** = max(high) từ j tới t.
> - **Độ sâu** = (cực trị − L)/ATR; **thời gian bên kia** = t − j (nến).
> - Nếu tới j + k chưa có rejection lẫn acceptance → **EXPIRED** (không phải sweep).
> - Mặc định đề xuất cho khung M5–M15: ε = 0.02·ATR (hoặc 1 tick), δ = 0.25·ATR, k = 3 nến. **Tham số phải được khai báo trước khi backtest.**

So với v1 ("reclaim + displacement"): DEF-LS-04 **không** đưa displacement vào định nghĩa sweep. Lý do: tách *sự kiện* (sweep) khỏi *xác nhận* (MSS + displacement, DEF-LS-06) để đo được giá trị riêng của từng lớp (ablation §26). Trong thực hành trade, quy tắc v1 vẫn đúng: **không vào lệnh khi chỉ có sweep** (RULE-LS-003).

### 5.7 L6 — Giới hạn: chart không cho phép kết luận gì

- Không kết luận được rằng **có** stop ở trên L, bao nhiêu, hay đã khớp hết.
- Không kết luận được **ai** đã đẩy giá lên và **ai** đã bán ở trên.
- Không kết luận được rằng cú xuyên là **có chủ đích**.
- Tại close của nến xuyên, không kết luận được nhánh tiếp theo (LS-Sim-05: phần lớn sự kiện còn PENDING).
- Không kết luận được rằng một "sweep đẹp" trong ảnh chụp là đại diện — ảnh được chọn vì kết quả.

![[LS-Sim-01-Wick-Through-Base-Rate.png]]
*Hình LS-Sim-01 **[SIMULATION]**: (A) Tỷ lệ nến xuyên đầu tiên close lại bên trong swing high trên random walk: 29% (M5) → 38% (M15) → 44% (H1) → 49% (H4) → 52% (D1); giới hạn liên tục = 50% (reflection principle). Càng ít bước nhỏ trong một nến (đường giá "giật" hơn), càng nhiều overshoot và càng ít close-back. (B) Cùng sự kiện, nhãn theo nến M5 và nhãn theo nến H1 chứa nó bất đồng ở ~39% trường hợp.*

**Đọc hình này thế nào.** Nó không nói "sweep không có thật". Nó nói: *hình dạng* wick-xuyên-rồi-close-lại là chuyện thường của bất kỳ quá trình ngẫu nhiên nào, nên **sự xuất hiện của hình dạng đó không phải bằng chứng** về stop hunt hay về edge. Bằng chứng (nếu có) phải nằm ở **hệ quả** sau đó vượt baseline — §11, §26.

### 5.8 Thuật ngữ: sweep, raid, stop run, stop hunt, false breakout, failed breakout, breakout, rejection, deviation

| Thuật ngữ | Ý chính | Hành vi quan sát được | Cách dùng trong ICT / cộng đồng | Diễn giải cơ chế |
|---|---|---|---|---|
| **Liquidity sweep** | Lấy liquidity rồi quay lại | Xuyên L, rejection trong k nến | Thuật ngữ trung tâm; thường hàm ý đảo chiều | Lệnh có điều kiện khớp; không có dòng lệnh duy trì acceptance |
| **Liquidity raid** | Như sweep, nhấn mạnh tính "đột kích" | Thường xuyên nhanh, sâu hơn | Dùng gần như đồng nghĩa với sweep | Như trên |
| **Stop run** | Giá chạy qua vùng stop | Xuyên L + tăng tốc | ICT dùng "run on stops", "running the stops" — **không** hàm ý đảo chiều | Cascade (cơ chế A) |
| **Stop hunt** | "Săn" stop có chủ đích | Không khác stop run trên chart | Cách nói dân gian, hàm ý ý định | Cơ chế F — không quan sát được |
| **Liquidity grab** | Đồng nghĩa phổ thông (SMC) | Như sweep | Dùng nhiều trong SMC | — |
| **False breakout** | Breakout không giữ được | Xuyên L (thường close bên kia), rồi quay lại | Ngôn ngữ phân tích kỹ thuật cổ điển | Người breakout bị kẹt |
| **Failed breakout** | Như false breakout, nhấn mạnh việc breakout đã được "xác nhận" (close) rồi mới thất bại | E3: close > L rồi close < L − δ | — | Acceptance tạm bị đảo |
| **Breakout** | Giá rời khỏi vùng và ở lại bên kia | E4: acceptance + mở rộng | BOS khi là swing cấu trúc | Có dòng lệnh duy trì |
| **Rejection** | Giá bị đẩy lùi tại/qua một mức | Wick dài, close xa mức | Rejection block, wick | Lệnh đối ứng đủ mạnh trong khung nến |
| **Deviation** | Lệch ra ngoài range rồi quay về (ngôn ngữ range trading / Wyckoff hiện đại) | Xuyên biên range, quay về | Ít dùng trong ICT gốc | Như sweep tại biên range |
| **Turtle Soup** | Mô hình trade ngược breakout 20 ngày | Phá đỉnh/đáy 20 ngày rồi quay lại | ICT dùng tên này cho mô hình fade breakout | Connors & Raschke (1995) — xem [[33-Turtle-Soup]] |
| **Spring / Upthrust** | Wyckoff: phá đáy/đỉnh range rồi quay lại | Như sweep tại biên range trong schematic | Không dùng trong ICT | Kiểm tra cung/cầu tại biên |
| **Judas swing** | Cú di chuyển giả đầu phiên ngược hướng ngày | Sweep một phía đầu phiên rồi đảo | ICT — gắn với thời gian (London/NY open) | Sweep + yếu tố phiên |

**Kết luận về thuật ngữ:** *sweep / raid / grab / stop hunt / false breakout / spring-upthrust / deviation* mô tả **cùng một hình học quan sát được** (xuyên mức rồi quay lại), khác nhau ở *trường phái* và ở *hàm ý về ý định*. *Stop run* là từ trung tính nhất (chỉ nói giá chạy qua vùng stop). *Failed breakout* khác ở chỗ có close bên kia trước khi thất bại (E3 vs E2). Note này dùng "sweep" theo DEF-LS-04 và "run" theo DEF-LS-05; mọi từ khác được ánh xạ về mã E0–E9 (§7) khi ghi journal.

### 5.9 Định nghĩa của v1 *(v1, có chú thích v2)*

![[Liquidity-Sweep-Definition.svg]]
*Hình v1: Phân biệt Sweep (wick xuyên → reclaim + displacement → đảo chiều) với Break thật (đóng nến vượt hẳn + acceptance → tiếp diễn).*

**Khái niệm:**
Liquidity Sweep (còn gọi stop hunt, liquidity grab, stop raid) là khi giá di chuyển vượt qua một mức nơi tập trung lệnh chờ — đỉnh cũ, đáy cũ, equal highs/lows, hoặc đường xu hướng rõ ràng — để **kích hoạt** các lệnh đó, sau đó **đảo chiều**. Nhóm thanh khoản bị quét chính là "nhiên liệu": stop loss của trader đang giữ lệnh + breakout order của trader mới vào, cộng lại tạo đủ khối lượng đối ứng để smart money khớp lệnh lớn của họ.

**Bản chất:** thị trường di chuyển từ một pool liquidity này tới một pool liquidity khác. Trước khi đẩy giá đi xa, market thường **lấy thanh khoản ở phía gần** (quét đỉnh/đáy gần nhất) để (1) gom lệnh đối ứng và (2) "đánh lừa" đám đông vào sai hướng. Sweep là khoảnh khắc manipulation trong chu kỳ [[02-AMD]].

**Sweep vs Break (cực kỳ quan trọng):**
- **Sweep:** giá xuyên qua mức bằng **bóng nến (wick)** hoặc xuyên rồi nhanh chóng bị kéo lại, **đóng nến trở lại bên trong** vùng, kèm displacement ngược → liquidity đã bị lấy, giá đảo chiều.
- **Break thật (BOS):** giá xuyên qua và **đóng nến vượt hẳn** mức đó, có chấp nhận (acceptance), tiếp tục đi theo hướng phá → đây là tiếp diễn xu hướng, KHÔNG phải sweep.

**Mục đích trong ICT:**
- Là **trigger / điều kiện kích hoạt**: gần như mọi entry ICT (FVG, OB, OTE, Silver Bullet) đều muốn thấy một sweep TRƯỚC khi vào.
- Xác nhận **draw on liquidity** đã được "lấy": pool liquidity là mục tiêu, sweep là lúc nó được tiêu thụ.
- Đánh dấu **điểm đảo chiều tiềm năng**: đáy/đỉnh của cú sweep thường là điểm swing quan trọng để đặt stop.
- Là một nửa của cặp **"sweep → displacement"**: sweep lấy thanh khoản, displacement thể hiện intent đẩy giá hướng ngược.

**Vì sao khái niệm này quan trọng:**
Phần lớn trader thua lỗ vì họ **là** thanh khoản: họ đặt stop ngay dưới đáy, mua ngay khi giá phá đỉnh. Hiểu Liquidity Sweep giúp bạn đứng về phía ngược lại — chờ đám đông bị quét rồi mới vào. Đây là chìa khóa biến "stop hunt" từ kẻ thù thành tín hiệu.

**Nó giúp trả lời câu hỏi nào trên chart?**
- Pool liquidity nào vừa bị lấy (BSL hay SSL)?
- Cú vượt mức này là sweep (sẽ đảo) hay break thật (sẽ tiếp diễn)?
- Giá đã reclaim vùng vừa quét chưa, có displacement xác nhận chưa?
- Đáy/đỉnh của cú sweep — nơi đặt stop loss logic — ở đâu?
- Đã đủ điều kiện trigger để tìm entry tại POI chưa?

> [!note] Chú thích v2 cho định nghĩa v1
> - "…gom thanh khoản cho smart money…", "…tạo đủ khối lượng đối ứng để smart money khớp lệnh lớn…" → **[INTERPRETATION]** (cơ chế B/F). Phần quan sát được là: giá vượt mức rồi quay lại.
> - "Thị trường di chuyển từ một pool liquidity này tới một pool liquidity khác" → mô tả hợp nhất (§4.3), đúng một cách tầm thường do hình học; phần có thông tin cần test.
> - "Sweep vs Break" của v1 tương ứng E2 (sweep) vs E4 (break) trong taxonomy v2. v2 bổ sung E3 (đóng vượt rồi quay lại) và trạng thái PENDING.
> - "gần như mọi entry ICT đều muốn thấy một sweep TRƯỚC khi vào" → **[ICT FRAMEWORK]** về cách dùng; giá trị gia tăng của điều kiện sweep là **[HYPOTHESIS]** HYP-LS-010.

**Liquidity Sweep không phải là gì** *(v1 + v2)*

- Không phải "cứ thấy phá đỉnh/đáy là đảo chiều" — phải có reclaim + displacement.
- Không phải tín hiệu entry độc lập — nó là trigger, vẫn cần POI + bias + premium/discount.
- Không phải mọi cú quét đều dẫn tới đảo chiều; sweep thất bại = break thật.
- Không phải lý do để bắt đáy/đỉnh bằng tay ngay trên wick mà không chờ xác nhận.
- Không đồng nghĩa với "stop hunt xấu xa"; đó là cơ chế cung cấp thanh khoản bình thường của thị trường.
- *(v2)* Không phải một đối tượng nằm trên chart — nó là một **sự kiện có thời điểm** (known_at) và **có thể bị đổi nhãn** (rejection → re-break).
- *(v2)* Không phải bằng chứng về ý định hay danh tính người tham gia.
- *(v2)* Không phải đồng nghĩa với "liquidity run" — run là chuỗi acceptance (§6).

---

## 6. Liquidity Run

### 6.1 Liquidity Run là gì — trong cách dùng hiện tại

**[ICT FRAMEWORK]** Trong tài liệu cộng đồng, "liquidity run" (hay "run on liquidity") mô tả việc giá **lấy liquidity tại swing kế tiếp và tiếp tục cùng hướng**, có displacement rời khỏi mức vừa lấy và không quay lại PD array trước đó. Sweep thì "lấy rồi đảo"; run thì "lấy rồi đi tiếp". ICT gốc cũng dùng cụm "run on stops", "running the buy stops" theo nghĩa trung tính: giá chạy qua vùng stop.

**Vấn đề:** phân biệt này dựa trên **kết quả**. Tại nến xuyên mức, không ai biết đó là sweep hay run. Nếu định nghĩa "run = lấy liquidity rồi đi tiếp" và "sweep = lấy liquidity rồi đảo", thì câu "sweep dẫn tới đảo chiều" là đúng **theo định nghĩa** — không chứa thông tin dự báo nào. Đây là kiểu lập luận vòng tròn mà brief yêu cầu tránh.

### 6.2 Sweep và Run khác nhau ở outcome hay ở structure?

| Câu hỏi | Trả lời |
|---|---|
| Khác ở cú xuyên mức? | **Không** — nến xuyên giống nhau (LS-Sim-03) |
| Khác ở outcome? | **Có** — nhưng outcome chỉ biết sau một độ trễ |
| Khác ở structure? | **Có thể đo**: sweep là sự kiện **một mức** được phân xử bằng rejection; run là **chuỗi nhiều mức** cùng phía, mỗi mức phân xử bằng acceptance, giữa các lần lấy không có sự kiện cấu trúc phía đối diện |
| Một run có thể bắt đầu bằng sweep? | **Có** — sweep phía đối diện (SSL) rồi run lên qua các BSL (T2 trong LS-Deep-07). Đây là hai sự kiện, không phải một |
| Một sweep có thể biến thành run? | **Có** — rejection ban đầu, rồi re-break + acceptance (T1). Nhãn "sweep" tại t₁ được *bổ sung* bằng nhãn "rejection failed → acceptance" tại t₂ (append-only) |
| Run kết thúc thế nào? | Thường bằng một **sweep** tại mức cuối (T3), hoặc MSS ngược ở khung run |
| Có tiêu chí khách quan? | **Có, nếu chấp nhận độ trễ**: DEF-LS-05 dưới đây |

### 6.3 Định nghĩa vận hành v0.1

> [!example] DEF-LS-05 — Liquidity Run (v0.1, HEURISTIC)
> Một **run lên** (đối xứng cho run xuống) là chuỗi các mức tham chiếu ex-ante L₁ < L₂ < … < L_n (n ≥ 2, cùng phía BSL) sao cho:
> 1. Mỗi L_i bị xuyên theo thứ tự thời gian và được phân xử bằng **acceptance** (2 close > L_i, hoặc close > L_i + 0.5·ATR) trước khi L_{i+1} bị xuyên;
> 2. Giữa hai lần lấy liên tiếp, **retracement** < r_max của leg trước đó (đề xuất r_max = 50%) **[HEURISTIC]**;
> 3. Không có **sự kiện cấu trúc phía đối diện** ở khung của run (ví dụ: không close dưới higher low gần nhất đã xác nhận);
> 4. **known_at** của nhãn "run" = close của nến xác nhận acceptance tại L₂ (run không tồn tại khi mới có một mức).
>
> Run **kết thúc** (DEF-LS-07) khi xảy ra một trong: rejection tại mức kế tiếp (một sweep), MSS ngược ở khung run, hoặc hết phiên/cửa sổ khai báo.

### 6.4 Bảng so sánh Sweep vs Run (§14 của brief)

| Chiều so sánh | Liquidity Sweep | Liquidity Run |
|---|---|---|
| Hành vi chính | Một mức bị xuyên rồi **quay lại** | Nhiều mức cùng phía bị xuyên và **giữ được** |
| Quan hệ với liquidity | Tiêu thụ lớp lệnh gần mức; không có dòng lệnh duy trì phía bên kia | Tiêu thụ liên tiếp; có dòng lệnh duy trì (hoặc drift) |
| Cấu trúc điển hình | Wick/đuôi dài tại mức; close lại bên trong | Bậc thang: lấy mức → hồi nông → lấy mức tiếp |
| Rejection | **Có** (định nghĩa) | Không tại các mức giữa; có thể có ở mức cuối |
| Continuation | Không (trong cửa sổ k) | **Có** (định nghĩa) |
| Displacement | Có thể theo hướng ngược mức (nếu thành reversal) | Theo hướng run, có thể nhỏ dần khi gần kết thúc |
| MSS | MSS ngược là *xác nhận* tiếp theo, không phải một phần của sweep | Không có MSS ngược (điều kiện 3) |
| DOL | Pool đối diện trở thành mục tiêu *nếu* có xác nhận | Pool kế tiếp cùng phía, cuối cùng là DOL HTF |
| Hàm ý dự báo (cần test) | HYP-LS-001/003: P(pool đối diện trước stop) > p_null sau rejection + MSS | HYP-LS-012: P(pool kế tiếp cùng phía trước pool đối diện) > p_null khi HTF đồng hướng |
| Failure mode | Rejection thất bại → re-break (T1); đảo chậm/lình xình (R2) | Run gãy: rejection tại mức kế (T3) — tức một sweep |
| Thời điểm biết | Close nến rejection (t ≤ j + k) | Close nến acceptance ở mức thứ hai |

**Nói thẳng:** nếu bỏ đi độ trễ, *ranh giới ngữ nghĩa* giữa sweep và run trong cách dùng cộng đồng là **không rõ** — hai từ đôi khi chỉ cùng một cú xuyên mức, gọi tên sau khi biết kết quả. Ranh giới chỉ rõ khi định nghĩa bằng *cách phân xử* + *số mức* + *thời điểm biết*, như DEF-LS-04/05.

### 6.5 Chuyển trạng thái giữa sweep và run

![[LS-Deep-07-Sweep-vs-Run-Va-Chuyen-Trang-Thai.svg|900]]
*Hình LS-Deep-07: Sweep = một mức, rejection. Run = nhiều mức cùng phía, acceptance. T1: sweep bị vô hiệu → run. T2: sweep phía đối diện rồi run. T3: run kết thúc bằng một sweep.*

### 6.6 Liquidity Run vs Trend continuation (§35 của brief)

Câu "giá đang run liquidity vì nó cứ lấy liquidity" là vòng tròn. Tiêu chí quan sát được để tách hai khái niệm:

| Tình huống | Có trend continuation? | Có liquidity run (DEF-LS-05)? | Ghi chú |
|---|---|---|---|
| Trend tăng đều, không có swing high rõ để lấy (grind) | Có | **Không** (không có mức ex-ante bị lấy liên tiếp) | Trend không cần run |
| Giá lấy liên tiếp 3 swing high **bên trong** một range D1 | Có thể không (D1 vẫn range) | **Có** — run nội bộ (internal) ở khung H1 | Run có thể xảy ra trong range |
| Breakout khỏi range, rồi lấy liên tiếp các high của tuần trước | Có | Có | Run sau breakout |
| Giá lấy 2 high, hồi 70% leg, rồi lấy high thứ 3 | Có thể | **Không** theo tiêu chí r_max = 50% | Ranh giới heuristic — phải khai báo trước |
| Giá lấy high, rồi mất HL gần nhất, rồi lấy high tiếp | Không rõ | **Không** (điều kiện 3 bị vi phạm) — đây là hai sự kiện tách rời | |

**Kết luận:** *Trend* là thuộc tính của **đường giá** (drift, chuỗi HH/HL). *Run* là thuộc tính của **quan hệ giữa đường giá và một danh sách mức ex-ante**. Chúng tương quan mạnh (LS-Sim-06B: drift làm run dài hơn) nhưng không đồng nhất.

![[LS-Sim-06-Run-Length-Null.png]]
*Hình LS-Sim-06 **[SIMULATION]**: (A) Trên random walk H1 không drift, chuỗi "lấy pool cùng phía" dài ≥ 2: 64%, ≥ 3: 43%, ≥ 5: 19% (trung bình 2.9). (B) Thêm drift: run cùng phía drift dài hơn, run ngược drift ngắn đi rõ rệt (drift +0.15σ/nến: BSL trung bình 3.5 mức, SSL 1.9). "Run" chủ yếu mô tả drift.*

**Hàm ý thực hành:** một run 3 mức *không tự nó* là bằng chứng của "dòng lệnh tổ chức" — nó xuất hiện ở gần một nửa số chuỗi trên random walk. Giá trị dự báo (nếu có) của khái niệm run phải được đo như: *"sau khi run được xác nhận (L₂ accepted), P(L₃ trước khi mất HL gần nhất) có vượt baseline của cùng hình học không?"* (HYP-LS-012).

---

## 7. Taxonomy sự kiện liquidity — theo hành vi quan sát được

### 7.1 Đánh giá taxonomy trong brief (Type A–H)

Taxonomy đề xuất trong brief (Touch / Penetration / Sweep + Rejection / Sweep + Acceptance / Breakout + Expansion / Sequential consumption / Failed run / Run + structure expansion) là điểm xuất phát tốt, nhưng có bốn vấn đề:

1. **Trộn hai cấp độ.** A–E là sự kiện *một mức*; F–H là *chuỗi* nhiều mức. Gộp chung làm khó đếm (một chuỗi F chứa nhiều sự kiện C/D).
2. **Nhãn phụ thuộc kết quả.** "Sweep + Acceptance" là mâu thuẫn trong thuật ngữ nếu sweep đã hàm ý quay lại; "Breakout + Expansion" cần biết expansion — chỉ biết sau.
3. **Thiếu các loại quan trọng trong thực hành:** không chạm (giá quay đầu *trước* mức — near miss/front-run), nhảy gap qua mức, thọc nhiều lần (multi-poke), quét hai phía (outside/expansion).
4. **Thiếu trạng thái chưa phân xử.** Mọi sự kiện đều đi qua giai đoạn PENDING.

### 7.2 Taxonomy v0.1: hai trục + một lớp chuỗi

**Trục 1 — độ sâu tương tác với mức:** không chạm → chạm → xuyên bằng wick → xuyên bằng close → nhảy qua (gap).
**Trục 2 — cách phân xử:** rejection / acceptance / chưa phân xử (PENDING → EXPIRED).
**Lớp chuỗi:** một mức · nhiều mức cùng phía (run) · hai phía (expansion).

![[LS-Deep-06-Taxonomy-Su-Kien-E0-E9.svg|900]]
*Hình LS-Deep-06: Mã sự kiện E0–E9 dùng để ghi journal — phân loại theo hành vi, không theo câu chuyện.*

| Mã | Tên | Điều kiện quan sát (BSL; SSL đối xứng) | Thời điểm biết sớm nhất | Ánh xạ thuật ngữ |
|---|---|---|---|---|
| **E0** | Không chạm (near-miss) | max(high) trong cửa sổ < L − ε, rồi giá rời đi ≥ x·ATR | Khi giá rời đi đủ xa | "front-run", "chưa lấy liquidity" |
| **E1** | Chạm | \|high − L\| ≤ ε, close < L | Close nến chạm | "touch", "test" |
| **E2** | Xuyên bằng wick → rejection | high > L + ε, close nến đó < L − δ | Close nến xuyên | sweep "sạch", raid, grab |
| **E3** | Đóng vượt → quay lại | close > L (không đủ acceptance), rồi close < L − δ trong k nến | Close nến quay lại | failed breakout, deviation |
| **E4** | Đóng vượt → acceptance | ≥ 2 close > L hoặc close > L + 0.5·ATR | Close nến thỏa | breakout, BOS (nếu L là swing cấu trúc) |
| **E5** | Nhảy gap qua mức | open của nến/phiên mới đã ở bên kia L | Open phiên | "lấy level không có wick" — không có giao dịch tại L |
| **E6** | Thọc nhiều lần (multi-poke) | ≥ 2 lần high > L, mỗi lần close < L, trong một cửa sổ | Close lần thọc thứ hai | multi-poke sweep, "sweep of sweep" |
| **E7** | Chuỗi cùng phía (run) | DEF-LS-05 | Acceptance tại L₂ | liquidity run |
| **E8** | Hai phía (expansion) | Trong cùng phiên/cửa sổ, mức trên và mức dưới đều bị xuyên | Khi phía thứ hai bị xuyên | outside day, range expansion, "quét cả hai đầu" |
| **E9** | Run thất bại | Run (E7) rồi rejection ở L_{n+1} và close lại dưới L_n | Close dưới L_n | run gãy → sweep tại mức cuối |
| **PND / EXP** | Chưa phân xử / hết hạn | Sau xuyên, chưa thỏa E2/E3/E4 trong k nến | Close nến j + k | — |

**Ánh xạ từ taxonomy của brief:** Type A → E1 (hoặc E0); Type B → PENETRATED/PND; Type C → E2/E3; Type D ("sweep + acceptance") → E4; Type E → E4 + mở rộng; Type F → E7; Type G → E9; Type H → E7 + MSS/BOS ở khung HTF.

### 7.3 Các loại sweep theo bối cảnh *(v1)*

![[Liquidity-Sweep-Context-Types.svg]]
*Hình v1: Các loại sweep — SSL Sweep (→ Long), BSL Sweep (→ Short), Turtle Soup, internal vs external.*

| Loại | Mô tả | Ý nghĩa thực chiến |
|---|---|---|
| **SSL Sweep (quét đáy)** | Giá quét xuống dưới đáy cũ / equal lows rồi reclaim | Tín hiệu tìm **Long**: sell-side liquidity đã bị lấy, chờ displacement lên |
| **BSL Sweep (quét đỉnh)** | Giá quét lên trên đỉnh cũ / equal highs rồi reclaim | Tín hiệu tìm **Short**: buy-side liquidity đã bị lấy, chờ displacement xuống |
| **Turtle Soup** | Phá một đáy/đỉnh "rõ ràng" để bẫy breakout trader rồi đảo | Mô hình reversal kinh điển dựa trên sweep |
| **Sweep nội bộ (internal)** | Quét thanh khoản bên trong dealing range | Thường cho move ngắn tới external liquidity |
| **Sweep external (HTF)** | Quét đỉnh/đáy lớn của HTF (PDH/PDL, PWH/PWL) | Điểm đảo chiều lớn, thường mở ra cả một leg |
| **Failed sweep = Break** | Giá xuyên + đóng nến ngoài + đi tiếp | KHÔNG phải sweep; là BOS / tiếp diễn |

> [!tip]
> Hai pool liquidity hay bị quét nhất: **equal highs/lows** (nhiều stop dồn về một mức) và **đỉnh/đáy phiên / ngày trước** (PDH/PDL). Đánh dấu sẵn các mức này trước phiên để nhận diện sweep theo thời gian thực.

> [!note] Chú thích v2
> Cột "Ý nghĩa thực chiến" của v1 ("tín hiệu tìm Long/Short", "điểm đảo chiều lớn") là **[ICT FRAMEWORK]** + **[HYPOTHESIS]**: chúng nói *nên tìm gì*, không nói *xác suất bao nhiêu*. "Failed sweep = Break" của v1 tương ứng E4 (hoặc E3 nếu break sau đó cũng thất bại). "Internal/External" là quan hệ với một range — xem §9.1.

---

## 8. Liquidity hình thành và vòng đời của nó

### 8.1 Đánh giá chuỗi "Price moves → Swing forms → … → New liquidity develops"

| Bước trong brief | Đánh giá | Sửa đề xuất |
|---|---|---|
| Price moves → Swing forms | Đúng, nhưng phụ thuộc định nghĩa swing (fractal n, directional-change θ) và known_at | Ghi rõ thuật toán swing ([[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]]) |
| Market participants recognize level | **Giả định**: chỉ một phần người tham gia; mức D1 được nhìn bởi nhiều người hơn mức M5 | Thay bằng "mức có thuộc tính salience (T, V, Q…)" |
| Orders cluster around level | **Giả định không quan sát được** | "Lệnh *có thể* tập trung — bằng chứng cho số tròn FX; suy rộng là [INTERPRETATION]" |
| Liquidity reference becomes salient | Vòng tròn với bước 3 | Gộp với bước 3 |
| Price revisits level | Không phải luôn luôn; xác suất do khoảng cách/thời gian (H) | "Giá *có thể* quay lại; P theo first-passage" |
| Liquidity consumed / interacted with | Chỉ biết là giá giao dịch qua mức | Tách: *mức bị xuyên* (thấy) vs *lệnh bị khớp* (không thấy) |
| Market rejects or accepts | Thiếu PENDING, thiếu E0/E5/E6 | Dùng taxonomy §7 |
| New structure forms → New liquidity | Đúng — cực trị mới thành mức mới | Mức mới có known_at mới; không hồi tố |

### 8.2 Vòng đời — mức giá và lệnh là hai thứ khác nhau

![[LS-Deep-05-Vong-Doi-Liquidity.svg|900]]
*Hình LS-Deep-05: Chart chỉ thấy MỨC. Các lệnh quanh mức xuất hiện, tăng, dời đi, bị khớp, được bổ sung — gần như hoàn toàn vô hình.*

| Giai đoạn | Cơ chế | Thấy được gì | Hàm ý |
|---|---|---|---|
| **Creation** | Swing được xác nhận; mức trở nên nổi bật | Mức, known_at | Trước known_at, mức không tồn tại cho backtest |
| **Accumulation** | Thời gian trôi; thêm test; EQH hình thành; nhiều người tham chiếu | Tuổi mức, số lần test | Chưa rõ dấu: mức cũ hơn có nhiều lệnh hơn (tích lũy) hay ít hơn (bị quên, stop bị dời)? → biến A trong LSS là **[HYPOTHESIS]** chưa biết dấu |
| **Migration** | Trailing stop dời theo giá; người mới đặt stop theo swing gần hơn | Không thấy | Pool ở swing cũ có thể đã "di cư" sang swing mới — mức cũ bị xuyên mà không có cascade |
| **Interaction / Approach** | Giá tới gần; limit có thể được thêm (fade) hoặc rút (MM tránh rủi ro) | Khoảng cách; tốc độ tiếp cận | Tiếp cận chậm vs nhanh có thể ảnh hưởng phân xử — **[HYPOTHESIS]** |
| **Consumption** | Giá vượt mức; stop kích hoạt và khớp với limit đối diện | Giá vượt; độ sâu | "Pool bị lấy" = trạng thái của lệnh (không thấy) |
| **Partial consumption** | Vượt nông: chỉ lớp stop sát mức kích hoạt; lớp sâu hơn còn | Độ sâu so với ATR | Lý do tồn tại của "double sweep" (W2 của v1): lớp sâu vẫn là mục tiêu |
| **Removal** | Acceptance bên kia: mức không còn là tham chiếu cho nhóm lệnh cũ (stop đã khớp, vị thế đã đóng) | Acceptance | Mức cũ có thể đổi vai (breaker / S-R flip) — nhưng không còn là "pool" theo nghĩa cũ |
| **Replenishment** | Sau sweep, người vào lệnh ngược chiều đặt stop **ngay ngoài cực trị sweep** | Cực trị mới | Cực trị sweep thành mức mới — lý do "sweep of sweep" và lý do stop sát wick dễ bị quét (RULE-LS-004) |
| **New formation** | Cấu trúc mới → swing mới → mức mới | Swing mới | Quay lại Creation |

**Trả lời trực tiếp các câu của brief:**
- *Một pool có thể bị lấy một phần không?* — Có, và thường xuyên: độ sâu xuyên chỉ cho biết lệnh tới mức nào **có thể** đã kích hoạt (LS-Sim-04).
- *Liquidity có thể được "replenish" không?* — Có: sau sweep, stop mới được đặt ngoài cực trị mới; lệnh limit được đặt lại (resiliency).
- *Sau khi bị lấy, liquidity còn tồn tại không?* — **Mức** vẫn tồn tại như một tham chiếu (có thể đổi vai); **lớp lệnh gần mức** thì đã khớp. Phần lệnh sâu hơn (nếu có) vẫn còn.
- *Liquidity có thể dịch chuyển không?* — Có (migration: trailing stop, stop dời theo swing mới).

---

## 9. Internal vs External, hierarchy và Liquidity Significance Score

### 9.1 Internal vs External — từ số 0

![[LS-Deep-09-Internal-External-Tuong-Doi.svg|900]]
*Hình LS-Deep-09: Cùng mức X: external với range H1, internal với range D1. Mọi nhãn ERL/IRL phải kèm range tham chiếu.*

- **External range liquidity (ERL)** của một range R = liquidity được giả định ở **ngoài biên** của R: trên range high (BSL) và dưới range low (SSL).
- **Internal range liquidity (IRL)** của R = các mức **bên trong** R: swing nhỏ hơn, FVG chưa lấp, EQH/EQL bên trong.
- **Vì sao quan trọng [ICT FRAMEWORK]:** ICT mô tả giá "dao động" giữa ERL và IRL — lấy ERL rồi về IRL (FVG), từ IRL đi tới ERL kế tiếp. Xem [[16-Internal-External-Range-Liquidity-IRL-ERL]] và con lắc ERL/IRL ở [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]].

**Tuyệt đối hay tương đối?** **Tương đối.** "External" là quan hệ *mức – range*. Đổi range tham chiếu thì đổi vai. Hệ quả cho framework D1 → H1 → M5:
- Range tham chiếu cho câu "lấy external liquidity" mặc định là **range D1 context** (RULE-LS-009, kế thừa R7).
- Một sweep "external" của range M5 thường chỉ là sweep **internal** của range H1/D1 — ý nghĩa của nó thuộc về swing bị lấy.
- Khi range được re-map sau displacement ([[37-Re-mapping-Dealing-Range-sau-Displacement]]), mọi vai trò phải tính lại; nhãn cũ giữ nguyên (append-only).

### 9.2 Hierarchy liquidity — framework nghiên cứu

> [!warning] Đây là framework nghiên cứu, không phải luật ICT
> Thứ bậc dưới đây là cách tổ chức giả thuyết để test. Không có bằng chứng rằng mức cấp cao hơn "luôn thắng".

| Cấp | Ví dụ | Tiêu chí v0.1 | Kỳ vọng (cần test) |
|---|---|---|---|
| **Micro** | Swing M1/M5 fractal n = 2 | Level 1 swing; không có nhãn phiên | Thường bị lấy liên tục; ít ý nghĩa |
| **Internal** | Swing H1 bên trong range D1; FVG H1 | Level 2 swing; bên trong range context | Mục tiêu trung gian (IRL) |
| **Intermediate** | Asia/London H-L, swing H1 cấu trúc | Level 3; nhãn phiên | Mục tiêu trong ngày; nơi hay có Judas swing [ICT FRAMEWORK] |
| **External** | Biên range D1, PDH/PDL | Level 4; ERL của range context | Mục tiêu DOL ngày; nơi sweep "có nghĩa" cho reversal |
| **HTF** | PWH/PWL, swing D1/W1 lớn | Level 5 | DOL tuần/tháng |

**Yếu tố quyết định importance** (theo brief): timeframe, structural significance, visibility, recency, repeated tests, equal highs/lows, distance, DOL, regime, displacement, reaction, persistence — được gom vào LSS dưới đây.

**Thứ tự tầng pool của v1 (W2):** *"Asia H/L → London H/L → PDH/PDL → PWH/PWL"* là một áp dụng cụ thể của hierarchy này cho phiên giao dịch trong ngày — giữ nguyên như quy tắc lập bản đồ trước phiên.

### 9.3 Liquidity Significance Score (LSS) v0.1

![[LS-Deep-10-Liquidity-Significance-Score.svg|900]]
*Hình LS-Deep-10: Cổng bắt buộc G1–G5 + điểm hỗ trợ S, T, V, Q, N, A, C, D; X (khoảng cách) là biến kiểm soát, không phải điểm.*

**Cổng (thiếu một = loại khỏi danh sách):**

| Cổng | Điều kiện | Lý do |
|---|---|---|
| **G1 Ex-ante** | Mức có known_at trước thời điểm quyết định | Không có G1 → hindsight |
| **G2 Swing đã xác nhận** | Theo thuật toán khai báo (fractal n hoặc directional-change θ) ở khung T | Mức "nhìn bằng mắt" không tái lập được |
| **G3 Chưa bị lấy** | Không có giao dịch vượt mức kể từ known_at | Mức đã bị lấy là sự kiện khác (replenishment ngoài cực trị mới) |
| **G4 Đúng phía** | BSL trên giá hiện tại, SSL dưới | — |
| **G5 Không phải artifact** | Không phải gap rollover/DST, spike dữ liệu bẩn (W6, EC2 của v1) | Mức giả |

**Điểm (mỗi biến chuẩn hóa 0–1):**

| Mã | Thành phần | Biến đo (ví dụ) | Lý do cơ chế | Rủi ro tự lừa |
|---|---|---|---|---|
| S | Cấu trúc | Swing level 1–5; leg rời swing có displacement | Swing cấu trúc → nhiều người đặt stop "đúng sách" | Gán level sau khi biết kết quả |
| T | Timeframe | D1 > H4 > H1 > M15 > M5 | Nhiều người nhìn HTF | "HTF luôn thắng" |
| V | Nhãn phiên/ngày | PDH/PDL, PWH/PWL, Asia/London H-L, số tròn | Mốc chung trên mọi nền tảng | Đếm nhãn trùng nhiều lần |
| Q | Đối xứng | EQH/EQL, \|ΔH\| ≤ tol·ATR | Stop dồn một chỗ | Nới tol cho vừa ý |
| N | Số lần test | Số lần chạm (E1) không vượt | Mức được "xác nhận" nhiều lần (Garzarelli: hiệu ứng nhớ) | Test nhiều lần cũng có thể là hấp thụ đang cạn |
| A | Tuổi | Số nến từ known_at | Tích lũy lệnh? hay migration? | **Chưa biết dấu** |
| C | Bối cảnh range | Là ERL của range context D1? | Biên range được nhiều người dùng | Range chọn sau khi thấy giá |
| D | Liên hệ DOL | Cùng hướng bias ex-ante? | Mục tiêu của framework | Bias viết lại sau sự kiện |
| X | Khoảng cách | (L − giá)/ATR → p_null | **Biến kiểm soát** | Lẫn "gần" với "quan trọng" |

**Công thức và cách dùng:** LSS = Σ wᵢ·zᵢ. **Không chọn trọng số bằng mắt.** Baseline = trọng số bằng nhau. Sau đó ước lượng ngoài mẫu (logistic regression của biến kết quả lên các z, kiểm soát X), hoặc ablation (bỏ từng biến xem dự báo có xấu đi không). Biến kết quả cho LSS **không phải** "có đảo chiều không" mà là các dấu vết cơ chế đo được: *tốc độ sau xuyên (tick/giây hoặc range nến), độ sâu xuyên/ATR, xác suất bị xuyên trong T ở cùng khoảng cách* (HYP-LS-006/007/008).

**Không mặc định rằng mọi thành phần có predictive power.** Rất có thể chỉ T, V và X mang thông tin; Q và N có thể chỉ là nhiễu thị giác. Đó là điều cần đo.

---

## 10. Giải phẫu một sweep — từng bước

### 10.1 Mười ba bước của một BSL sweep → reversal (short)

Ví dụ: H1 swing high L = 1.0868 (known_at hôm qua), D1 bias bearish, giá ở premium của range D1.

| # | Bước | Quan sát được | Cơ chế có thể | ICT diễn giải | Không biết |
|---|---|---|---|---|---|
| 1 | Một high hình thành | Swing high H1 được xác nhận sau n nến | Phản ứng tại vùng cung | "Old high" | Ai bán ở đó |
| 2 | Người tham gia nhìn thấy | — (suy luận salience) | Mức nổi bật → tham chiếu chung | "Obvious high" | Bao nhiêu người dùng mức |
| 3 | Lệnh có thể tập trung | **Không** | Stop của short, buy-stop breakout trên L; sell-limit tại L | "BSL resting above" | Khối lượng, độ sâu |
| 4 | Giá tiếp cận | Khoảng cách, tốc độ, giờ | Limit có thể được thêm/rút | "Price is drawn to BSL" | Vì sao giá đi lên (tin? flow?) |
| 5 | Giá giao dịch trên L | high > L + ε | Lệnh mua có điều kiện kích hoạt | "Raid / sweep" | Bao nhiêu đã khớp |
| 6 | Lệnh có thể bị kích hoạt | Một phần: nến dài/nhanh (nếu có tick) | Cascade (LS-Sim-04) | "Stops taken" | Độ sâu sổ phía trên |
| 7 | Rejection hay acceptance? | Close < L − δ (rejection) hoặc acceptance | Có/không có dòng lệnh duy trì | "Failure to hold above = manipulation" | Dòng lệnh ròng sau đó |
| 8 | Bằng chứng xác nhận rejection | Close xa mức; nến kế tiếp tiếp tục | Impact tạm thời phai / người bán xuất hiện | "Reclaim" | Ai bán |
| 9 | MSS? | Close dưới swing low tham chiếu (swing có ý nghĩa) | Dòng bán đủ bền để phá cấu trúc | "MSS / CHoCH" | — |
| 10 | Displacement? | Nến thân lớn (≥ x·ATR), để lại FVG | Dòng bán mạnh, một chiều | "Displacement = institutional sponsorship" | "Institutional" là diễn giải |
| 11 | Giá quay lại FVG/POI? | Retrace vào FVG | Người bán thêm / chốt lời short ngắn hạn | "Return to PD array → entry" | Có quay lại không (W5 của v1) |
| 12 | Ý nghĩa cơ học | Chuỗi sự kiện đã xảy ra | Lệnh có điều kiện tiêu thụ → dòng ngược chiều chiếm ưu thế | — | Nhân quả |
| 13 | ICT diễn giải toàn chuỗi | — | — | "Smart money engineered BSL, raided it, delivered to SSL" | **Toàn bộ phần ý định** |

**Không được nhảy từ bước 5 sang "Smart Money hunted stops".** Giữa bước 5 và bước 13 có sáu điểm mà kịch bản có thể rẽ nhánh (7, 8, 9, 10, 11 và chính việc stop có tồn tại ở bước 3 hay không).

### 10.2 Toy model 1 — độ sâu của cú xuyên

![[LS-Sim-04-Stop-Cascade-Depth.png]]
*Hình LS-Sim-04 **[TOY MODEL]**: Sổ lệnh tĩnh, độ sâu D mỗi tick phía trên L; stop mua tổng S phân bố mũ (độ rộng λ tick) ngay trên L. (A) Độ xuyên phụ thuộc tỷ số S/(D·λ); vượt ~1 thì cascade chạy xuyên cụm. (B) Cùng lượng stop (S = 120, λ = 6): sổ mỏng (D ≈ 4) → xuyên ~30 tick; D ≈ 7.6 → ~15 tick; D ≥ ~19 → chỉ 1 tick.*

**Đọc hình:**
- Độ sâu của sweep đo **tỷ số giữa lệnh bị kích hoạt và lệnh đối diện**, không đo ý định hay "sức mạnh của Smart Money".
- Cùng một cụm stop cho sweep nông vào giờ London/NY (sổ dày) và sweep sâu vào giờ Á/lễ/tin (sổ mỏng). Điều này nhất quán với kết luận của BIS (2017) về flash event GBP 7/10/2016: thời điểm trong ngày (thanh khoản mỏng) và các bộ khuếch đại cơ học, kể cả hedging liên quan quyền chọn. **[MARKET MECHANICS]**
- Hệ quả cho v1 §7.3 ("độ sâu & tốc độ đọc chữ ký stop run"): độ sâu chỉ có thể diễn giải khi **chuẩn hóa theo thanh khoản của thời điểm** — ít nhất theo giờ trong ngày (HYP-LS-016).

**Giới hạn của toy:** không có replenishment (resiliency), không có lệnh mới, không có stop-limit. Nó chỉ cô lập *một* cơ chế.

### 10.3 Toy model 2 — sau khi stop đã khớp

![[LS-Sim-03-Transient-Impact-Toy.png]]
*Hình LS-Sim-03 **[TOY MODEL]**: Giá = nhiễu random walk + impact propagator của dòng lệnh market, G(τ) = κ[γ + (1−γ)e^(−τ/τ₀)]. Cùng nhiễu, cùng đường giá trước sweep, cùng cụm stop trong cả ba panel. (A) Không có dòng lệnh mới → impact tạm thời phai, giá trôi xuống dưới L — "sweep" mà không có ai hấp thụ hay đảo. (B) Người mua bền bỉ → acceptance → run. (C) Người bán xuất hiện → đảo chiều nhanh, "displacement" xuyên qua range trước đó.*

**Ba bài học từ toy:**
1. **Hình dạng sweep có thể tồn tại mà không cần ai "đảo chiều".** Ở panel A, sau khi đợt mua (cả đợt đẩy giá lên lẫn cụm stop) kết thúc, phần tạm thời của impact phai và giá trôi về. Điều này phù hợp với quan sát thực nghiệm rằng giá hồi một phần sau khi một lệnh lớn hoàn tất (Farmer et al. 2013; Moro et al. 2009; Bershova & Rakhlin 2013).
2. **Displacement ngược chiều là dấu hiệu của dòng lệnh MỚI** (panel C), không phải hệ quả tất yếu của sweep. Nó phân biệt "C" với "A" — và đó chính là lý do có giá trị khi yêu cầu displacement + MSS (RULE-LS-003): nó lọc ra trường hợp có thêm thông tin.
3. **Acceptance (panel B) và "sweep" (panel A) khác nhau chỉ ở dòng lệnh sau** — vốn không thấy trên nến. Đây là cơ sở cơ chế của câu "sweep là một phép thử".

### 10.4 Cơ chế thị trường theo v1 §15 *(v1, có nhãn v2)*

![[Liquidity-Sweep-Deep-Mechanism.svg|720]]
*Hình v1: từ limit order book tới displacement. **Chú thích v2:** hình chứa hai câu mà v2 hiệu đính — "stop loss = thanh khoản được bảo đảm" (xem §4.5) và "reclaim = bằng chứng orderflow khách quan" (reclaim là quan sát khách quan về giá; diễn giải order flow từ nó là [INTERPRETATION]).*

- **Limit order book và "thanh khoản được bảo đảm":** một stop loss là lệnh market ĐÃ ĐẶT SẴN, chờ kích hoạt tại một mức giá cụ thể. Với bên cần khớp lệnh lớn, đây là nguồn đối ứng duy nhất có thể dự đoán trước cả về khối lượng và vị trí — khác hẳn thanh khoản "trôi nổi" trên thị trường mở (không biết khi nào xuất hiện, khối lượng bao nhiêu). Sweep về bản chất là hành vi **thu hoạch thanh khoản đã biết trước vị trí**, không phải khai thác thanh khoản ngẫu nhiên.
- **Dealer hedging và gamma exposure (đặc biệt rõ trên chỉ số & vàng):** market maker/dealer nắm quyền chọn thường phải hedge delta bằng cách mua/bán chính tài sản cơ sở. Khi giá tiến gần một mức có nhiều gamma tập trung (thường trùng các mức tâm lý tròn số/PDH-PDL), động thái hedging của dealer có thể tự khuếch đại một cú sweep thành một chuyển động mạnh hơn dự kiến — đây là lý do một số cú sweep trên ES/NQ có displacement bất thường lớn so với sweep tương tự trên FX (nơi không có cấu trúc quyền chọn tập trung tương tự ở cùng quy mô).
- **TWAP/VWAP execution và "điểm dừng tất yếu":** thuật toán thực thi lớn thường tối ưu theo VWAP trong ngày — khi giá lệch quá xa khỏi VWAP về một hướng, các thuật toán mua/bán đối ứng (mean-reversion desks) có xu hướng vào mạnh hơn tại các mức cực trị, tạo áp lực đảo chiều tự nhiên SAU cú sweep — không cần "âm mưu", chỉ cần đủ số lượng thuật toán mean-reversion cùng phản ứng với cùng một mức giá cực trị.
- **Vì sao "reclaim" là ranh giới khách quan, không phải thẩm mỹ:** tại đúng mức bị xuyên, luôn có hai dòng lệnh đối đầu — dòng lệnh vừa bị kích hoạt (stop + breakout order mới) và dòng lệnh của bên đang gom hàng. Nến đóng cửa trở lại trong range nghĩa là dòng mua/bán gom hàng đã áp đảo hoàn toàn dòng lệnh vừa bị kích hoạt trong đúng khung thời gian một nến — đây là bằng chứng orderflow khách quan, không phải một pattern hình học chủ quan.

| Ý của v1 §15 | Nhãn v2 | Ghi chú |
|---|---|---|
| Stop là "thanh khoản được bảo đảm", nguồn đối ứng duy nhất dự đoán được | [INTERPRETATION], phóng đại | §4.5 |
| Dealer hedging/gamma có thể khuếch đại sweep trên index/vàng | [MARKET MECHANICS] về cơ chế (BIS 2017 có nhắc hedging liên quan quyền chọn trong flash event FX) — [HYPOTHESIS] cho từng sự kiện | Kiểm bằng lịch OPEX + GEX nếu có dữ liệu (HYP-LS-017) |
| Thuật toán mean-reversion quanh VWAP tạo áp lực đảo chiều sau sweep | [INTERPRETATION] | Có thể đúng; không quan sát được trên OHLC |
| Reclaim = "bằng chứng orderflow khách quan" | Một nửa: **reclaim là quan sát khách quan về giá**; "dòng mua đã áp đảo hoàn toàn" là diễn giải | Một nến H1 reclaim có thể chứa M5 acceptance (LS-Sim-01B) |

### 10.5 Giải phẫu cú sweep trên LTF *(v1 §7.5)*

Một wick sweep trên M15 khi thả xuống M1 là **cả một cấu trúc hoàn chỉnh**: micro-downtrend → capitulation vào pool → micro-MSS → displacement ra. Ứng dụng:

- **Entry tinh hơn:** thay vì chờ nến M15 đóng để xác nhận reclaim, đọc M1: khi micro-MSS + M1 displacement xuất hiện bên trong wick đang hình thành, đó là reclaim đang diễn ra theo thời gian thực → entry sớm hơn một nhịp, stop sát hơn.
- **Lọc sweep giả:** nếu trên M1 cú "sweep" không có capitulation + đảo cấu trúc mà chỉ là grind đều xuống, khả năng cao đây là break thật đang diễn ra chậm.
- **Đánh đổi:** M1 nhiều nhiễu — kỹ thuật này chỉ dành cho pool + POI đã lên kế hoạch trước, không phải công cụ đi săn tín hiệu mới trong phiên.

> [!note] Chú thích v2
> Đây là phát biểu dạng fractal của §20 (máy trạng thái chạy ở khung thấp hơn bên trong một nến khung cao). Rủi ro: dùng M1 để "vào sớm hơn một nhịp" làm tăng số quyết định trong trạng thái PENDING — đúng lúc tỷ lệ lật nhãn cao nhất (LS-Sim-05). Nếu dùng, phải ghi riêng nhóm lệnh "vào trong wick" để so sánh expectancy với nhóm "vào sau rejection close".

### 10.6 Độ sâu và tốc độ của cú quét *(v1 §7.3, có nhãn v2)*

Hai biến số của mọi cú xuyên mức: **đi sâu bao nhiêu** và **ở lại bao lâu**.

| Độ sâu qua mức | Thời gian ngoài mức | Cách đọc |
|---|---|---|
| Nông (vài tick/pip, chỉ wick) | Vài giây – 1 nến | **Stop raid sạch** — chỉ cần lượng stop ngay sát mức; reversal thường nhanh và mạnh |
| Vừa (tới inducement/pool tầng 2) | 1–3 nến, có đóng nến nhẹ qua rồi reclaim ngay | **Sweep phân tầng** — quét cả lớp mồi lẫn pool chính; vẫn hợp lệ nếu reclaim + displacement |
| Sâu, càng đi càng **tăng tốc** | Nhiều nến, pullback không reclaim | **Không phải sweep** — có sponsor thật phía sau cú phá; đây là expansion/break; cấm bắt đảo |
| Sâu nhưng **giảm tốc** rồi đứng im | Nhiều nến lình xình ngoài mức | Chưa phân định — chờ; thường kết thúc bằng một trong hai kịch bản trên |

Thước đo bổ trợ: chiếu **standard deviation của Asia range / CBDR** ([[31-Standard-Deviation]], [[08-Central-Bank-Dealers-Range]]) — manipulation leg của London thường dừng quanh 1–2 SD dưới/trên range; cú quét chạy vượt xa 2.5–3 SD mà chưa quay lại là cảnh báo mạnh rằng đây không còn là manipulation. Tốc độ quan trọng hơn độ sâu: **stop run thật rời khỏi hiện trường ngay** — nến sau sweep phải là displacement; sự do dự chính là thông tin phủ định.

> [!note] Chú thích v2
> - Bảng "độ sâu × thời gian ngoài mức" của v1 là **[HYPOTHESIS]** có cơ chế hợp lý (LS-Sim-04 cho thấy độ sâu là tỷ số stop/độ sâu sổ; LS-Sim-03 cho thấy "tăng tốc khi rời mức" phản ánh dòng lệnh mới). Nó chưa được đo.
> - Ngưỡng "1–2 SD / 2.5–3 SD của Asia range/CBDR" là **[HEURISTIC]** → HYP-LS-018.
> - "Stop run thật rời khỏi hiện trường ngay" — nhất quán với Osler (2005): sau khi vượt cụm stop-loss, chuyển động **tiếp diễn** nhanh. Lưu ý chiều: đó là dấu hiệu của **run/acceptance**, không phải của reversal. Câu của v1 nói về *nến sau sweep phải là displacement ngược chiều* — tức dòng lệnh mới ngược chiều (panel C của LS-Sim-03).

### 10.7 Sweep trên ba loại thị trường *(v1 §15)*

| Đặc điểm | FX majors (EURUSD, GBPUSD) | Index Futures (NQ/ES) | Crypto (BTC/ETH) |
|---|---|---|---|
| **Nguồn thanh khoản đối ứng chính** | Interbank + retail stop cluster | Stop cluster + dealer hedging flow (đặc biệt quanh OPEX) | Stop cluster + liquidation cascade (đòn bẩy cao khiến hiệu ứng dây chuyền mạnh hơn) |
| **Đặc điểm displacement sau sweep** | Thường tuyến tính, ít giật cục | Có thể giật mạnh bất thường quanh gamma wall | Có thể cực đoan do liquidation cascade tự khuếch đại (một sweep nhỏ kích hoạt chuỗi thanh lý margin) |
| **Độ tin cậy trung bình theo giờ** | Cao nhất London/NY overlap | Cao nhất trong RTH, đặc biệt mở phiên và power hour | Biến thiên rất lớn theo giờ — không có "giờ giao dịch chính" cố định như FX/futures |
| **Rủi ro đọc sai do feed** | Trung bình — chênh lệch giữa broker vài pip | Thấp trong RTH nếu dùng đúng futures gốc, cao khi so CFD vs futures | Cao — nhiều sàn, độ sâu order book khác nhau đáng kể |
| **Tick/point tham chiếu** | EURUSD tick 0.0001 | NQ 1pt = 20 USD, tick 0.25; ES 1pt = 50 USD, tick 0.25 | Biến động tính theo % hợp lý hơn giá tuyệt đối |

> [!note] Chú thích v2
> Bảng là **[INTERPRETATION]** dựa trên đặc điểm cấu trúc thị trường đã biết (FX OTC phân mảnh; futures có sổ tập trung và quyền chọn trên chỉ số; crypto đòn bẩy cao với cơ chế thanh lý tự động — ví dụ đợt thanh lý dây chuyền khoảng 19 tỷ USD ngày 10/10/2025 được báo cáo rộng rãi). Các hàng "độ tin cậy trung bình theo giờ" là giả thuyết chưa đo.

---

## 11. Sau sweep: điều gì xảy ra tiếp theo

### 11.1 Cây kết quả

![[LS-Deep-11-Cay-Ket-Qua-Sau-Sweep.svg|900]]
*Hình LS-Deep-11: Cùng một cú xuyên mức có thể đi theo sáu nhánh; PENDING là trạng thái hợp lệ.*

Ánh xạ danh sách trong brief vào cây:

| Kết quả trong brief | Nhánh | Định nghĩa quan sát (v0.1) |
|---|---|---|
| Sweep → Immediate reversal | R1 | Rejection ≤ k nến, MSS + displacement ≤ m nến |
| Sweep → MSS | R1 (một phần) | MSS có, displacement có thể yếu |
| Sweep → Displacement | R1 (một phần) | Displacement có, nhưng chưa phá swing có ý nghĩa |
| Sweep → FVG | Phụ của R1 | FVG được tạo trong leg displacement |
| Sweep → Retracement | Sau R1 | Giá quay lại FVG/OB của leg |
| Sweep → Continuation | R3 → A1 | Rejection thất bại, re-break, acceptance |
| Sweep → Range expansion | A2 / E8 | Acceptance hoặc quét cả hai phía |
| Sweep → No reaction | PND → EXP, hoặc R2 | Không phân xử / lình xình |
| Sweep → Failed reversal | R3 hoặc R1 thất bại sau entry | Đảo chiều bắt đầu rồi giá quay lại vượt cực trị sweep |

### 11.2 Tại sao cùng một sweep nhưng kết quả khác nhau?

Đây là câu hỏi trung tâm của brief. Câu trả lời có cấu trúc:

**1. Vì sweep chỉ là sự kiện *tiêu thụ*; kết quả do dòng lệnh *đến sau* quyết định.** (LS-Sim-03.) Sau khi lớp lệnh có điều kiện gần mức đã khớp, có ba khả năng: không ai tới (giá trôi lại — impact tạm thời), người cùng chiều tới (acceptance), người ngược chiều tới (đảo chiều).

**2. Vì dòng lệnh đến sau phụ thuộc vào thông tin và bối cảnh — một phần đo được trước sự kiện:**

| Yếu tố | Đo được trước sự kiện? | Ảnh hưởng giả định | Nhãn |
|---|---|---|---|
| Bias D1 / vị trí trong range D1 | Có (ex-ante) | Sweep ngược hướng drift HTF dễ thành reversal hơn | [HYPOTHESIS] HYP-LS-004 |
| Khoảng cách tới pool đối diện vs pool kế tiếp | Có | Quyết định p_null — baseline của mọi tỷ lệ | [MATHEMATICAL] |
| Chế độ biến động (ATR regime, trend vs range) | Có | Trend regime → acceptance thường hơn ở phía drift | [HYPOTHESIS] |
| Giờ / phiên / killzone | Có | Dòng lệnh mới đổ vào ở giờ mở phiên; sổ mỏng giờ Á | [HYPOTHESIS] HYP-LS-005 |
| Tin tức | Có (lịch) | Dòng thông tin mới quyết định nhánh; spread giãn | [MARKET MECHANICS] |
| Độ sâu sổ (proxy: giờ, spread) | Một phần | Sổ mỏng → xuyên sâu (LS-Sim-04) | [TOY MODEL] |
| LSS của mức | Có | Mức nổi bật hơn → nhiều lệnh hơn → phản ứng rõ hơn? | [HYPOTHESIS] HYP-LS-007 |
| Dòng lệnh ròng sau khi stop khớp | **Không** (chỉ proxy: displacement, volume delta) | Quyết định trực tiếp | — |

**3. Vì hình học tự nó tạo ra mọi tỷ lệ.** Ngay cả khi không có thông tin nào, tỷ lệ của mỗi nhánh vẫn khác 0 và khác nhau — do khoảng cách (LS-Sim-02). Một nhánh "hay xảy ra" chưa phải là thông tin.

### 11.3 Sweep không bằng reversal — tiêu chí phân xử khách quan v0.1

```text
Liquidity taken (PENETRATED)
        │
   ┌────┼──────────┐
   ↓    ↓          ↓
REJECT PENDING   ACCEPT
   │  (timer k)     │
   │    ↓           │
   │  EXPIRED       │
   ↓                ↓
reversal?        continuation?
(MSS+disp ≤ m)   (next pool, run)
```

| Tiêu chí | Rejection (v0.1) | Acceptance (v0.1) | Ghi chú |
|---|---|---|---|
| Vị trí close | close < L − δ (δ = 0.25·ATR) | close > L + 0.5·ATR, **hoặc** | [HEURISTIC] |
| Số close | — | ≥ 2 close liên tiếp > L | Dùng để bắt acceptance chậm |
| Thời gian | Trong k nến kể từ nến xuyên | Trong k nến | k = 3 (M5/M15) [HEURISTIC] |
| Displacement | **Không** thuộc định nghĩa rejection — là lớp xác nhận (DEF-LS-06) | Có thể có theo hướng xuyên | Tách để đo ablation |
| Follow-through | m nến sau rejection: MSS + displacement → REVERSAL CONF. | Lấy mức kế tiếp → RUN ACTIVE | — |
| Biến động | ATR đóng băng tại nến trước xuyên | — | Tránh "ATR co giãn theo sự kiện" |

**Điều phân biệt "sweep có tiềm năng reversal" với "sweep chỉ là sự kiện trong continuation"** — danh sách giả thuyết để test, theo thứ tự ưu tiên:
1. Có MSS của swing **có ý nghĩa** (theo khung của mức bị lấy) + displacement trong m nến (HYP-LS-003, HYP-LS-010).
2. Bối cảnh HTF ngược với hướng xuyên: xuyên BSL khi D1 bearish/ở premium (HYP-LS-004).
3. Mức có LSS cao (ERL của range context, PDH/PWH) thay vì swing vi mô (HYP-LS-007).
4. Thời gian: killzone, không có tin tier-1 trong cửa sổ (HYP-LS-005).
5. Chất lượng thân nến reclaim (W1 của v1: thân ≥ 50% range nến sweep) (HYP-LS-009).
6. SMT divergence tại thời điểm sweep (HYP-LS-014).

### 11.4 Reclaim giả — thị trường "do dự" cũng là một câu trả lời *(v1 W1)*

![[Liquidity-Sweep-War-Fake-Reclaim.svg|720]]
*Sơ đồ v1: cùng một cú quét SSL — reclaim bằng doji lình xình (bẫy, dẫn tới tầng 2) vs reclaim bằng displacement (đảo thật).*

**Sách giáo khoa nói:** sweep + đóng nến trở lại bên trong = hợp lệ, tìm entry.

**Thực tế phát hiện sau nhiều mẫu:** có một lớp bẫy nằm *giữa* sweep và break — giá wick qua mức, đóng nến trở lại bên trong (thỏa định nghĩa reclaim!), nhưng nến reclaim là **doji/thân nhỏ**, rồi 2–3 nến tiếp theo lình xình ngay trên mức. Về mặt checklist thì "đã reclaim"; về mặt order flow thì **không có ai tài trợ cho cú đảo** — smart money lấy stop xong mà không đẩy giá đi nghĩa là họ chưa lấy đủ, và pool sâu hơn đang được chuẩn bị.

**Cơ chế:** displacement sau sweep chính là dấu vết của việc khớp lệnh lớn. Sweep tạo thanh khoản; nếu có bên mua thật sự dùng thanh khoản đó, giá *phải* rời khỏi vùng ngay (nến sau sweep là body lớn). Lình xình = thanh khoản bị lấy nhưng chưa ai dùng → xác suất cao đó chỉ là tầng mồi.

**Rule đo được:**
- Reclaim chỉ được tính khi **thân nến reclaim ≥ ~50% range nến sweep** hoặc nến kế tiếp là displacement rõ.
- **Đếm nến:** quá 2–3 nến sau reclaim mà không có displacement → hủy kịch bản, đứng ngoài. Không "chờ thêm cho chắc" — sự do dự đã là câu trả lời.
- Journal field: `reclaim_body_quality` (displacement / weak / doji) — sau 20+ mẫu sẽ thấy nhóm doji-reclaim thua vượt trội.

> [!note] Chú thích v2
> - Phần "Cơ chế" của W1 (*"smart money lấy stop xong mà không đẩy giá đi nghĩa là họ chưa lấy đủ"*) là **[INTERPRETATION]**. Lời giải thích thay thế không cần ý định: không có dòng lệnh mới sau khi stop khớp → impact tạm thời phai chậm → giá lình xình quanh mức (LS-Sim-03 panel A). Cả hai lời giải thích dẫn tới **cùng một quy tắc hành động**, nên quy tắc vẫn giữ.
> - Rule "thân nến reclaim ≥ ~50% range nến sweep" → **HYP-LS-009 [HEURISTIC]**. Rule "quá 2–3 nến không displacement → hủy" tương đương tham số m trong DEF-LS-06 / trạng thái STALE.
> - Journal field `reclaim_body_quality` được giữ trong schema §26.3.

---

## 12. Liquidity Sweep vs Breakout

### 12.1 Năm biến thể

![[LS-Deep-12-Sweep-vs-Breakout-5-Bien-The.svg|900]]
*Hình LS-Deep-12: Năm biến thể nhìn giống nhau ở nến xuyên, khác nhau theo thời gian.*

| Biến quan sát | Đo thế nào | Sweep (V1) | Breakout thật (V2) | Failed BO (V3) | Accept rồi reclaim (V4) | Retest rồi accept (V5) |
|---|---|---|---|---|---|---|
| Wick penetration | (high − L)/ATR | Bất kỳ | Bất kỳ | Bất kỳ | Bất kỳ | Bất kỳ |
| Close location | (close − L)/ATR; CLV của nến xuyên | < −δ | > 0, thường > +0.5 | > 0 rồi < −δ | > 0 nhiều nến | > 0 |
| Số close bên kia | Đếm trong k nến | 0 | ≥ 2 | 1–2 | ≥ 3 | ≥ 2 |
| Displacement | \|body\|/ATR theo hướng | Ngược hướng (nếu R1) | Theo hướng | Ngược hướng sau đó | Ngược hướng muộn | Theo hướng sau retest |
| Follow-through | Excursion tối đa theo hướng xuyên trong N nến | Nhỏ | Lớn, tăng dần | Nhỏ–vừa | Vừa | Lớn |
| Volume (nếu có) | Volume tại/sau xuyên | ? | ? | ? | ? | ? |
| Volatility | ATR regime | — | — | — | — | — |
| Retest | Giá quay về L từ phía bên kia | — | Không cần | Thất bại | Thất bại muộn | Giữ |
| Structure | MSS/BOS khung của mức | MSS ngược (nếu R1) | BOS theo hướng | — | MSS ngược muộn | BOS theo hướng |
| Acceptance duration | Số nến ở bên kia | < 1 | Kéo dài | Ngắn | Vừa | Kéo dài |

**Cột "Volume" để dấu hỏi có chủ đích:** chưa có bằng chứng đáng tin rằng volume trên OHLC tách được các biến thể; với FX spot, volume là tick volume của broker — rất hạn chế.

### 12.2 Vì sao không có quy tắc một nến nào dùng được

1. **Reflection principle:** khoảng một nửa số lần xuyên sẽ close lại bên trong dù không có gì xảy ra (§5.7, LS-Sim-01A).
2. **Phụ thuộc độ phân giải:** nhãn theo M5 và theo H1 bất đồng ~39% (LS-Sim-01B). Quy tắc "đóng nến trong = sweep" phụ thuộc khung bạn chọn để đóng nến.
3. **Nhãn bị lật theo thời gian:** LS-Sim-05 — trên random walk, nhãn rejection bị lật thành acceptance trong 6 nến ở 44% trường hợp.

### 12.3 Thủ tục phân loại có cửa sổ thời gian (v0.1)

```text
1. Trước phiên: danh sách mức ex-ante (G1–G5), tham số ε, δ, k, m khai báo.
2. Nến j xuyên L          → trạng thái PENDING (không hành động).
3. Trong j … j+k:
     close < L − δ trước acceptance        → REJECTED (E2 nếu ngay nến j, E3 nếu có close > L trước)
     2 close > L hoặc close > L + 0.5·ATR  → ACCEPTED (E4)
4. Hết j+k chưa phân xử    → EXPIRED (bỏ).
5. REJECTED: trong m nến có MSS (swing có ý nghĩa) + displacement → REVERSAL CONF.
             không có → STALE.
             re-break + acceptance → ghi thêm dòng "rejection failed" (không xóa dòng cũ).
6. ACCEPTED: close lại < L − δ → FAILED BO (E3) → xử lý như REJECTED (cần bước 5).
             lấy mức kế tiếp cùng phía → RUN ACTIVE.
```

### 12.4 Sweep thành công vs Sweep thất bại *(v1 §5)*

![[Liquidity-Sweep-Validation.svg]]
*Hình v1: Sweep thành công vs Sweep yếu vs Break thật vs Double sweep.*

#### Setup được xem là hợp lệ khi
- [ ] Pool liquidity bị quét rõ ràng (equal highs/lows, swing cũ, PDH/PDL).
- [ ] Giá reclaim: đóng nến trở lại bên trong vùng vừa quét.
- [ ] Có displacement + MSS xác nhận đảo chiều sau sweep.
- [ ] Sweep tại POI HTF đồng hướng bias, đúng premium/discount.
- [ ] Stop logic nằm ngoài đáy/đỉnh cú sweep; target là pool liquidity đối diện.
- [ ] R:R đạt kế hoạch.

#### Setup bị vô hiệu khi
- [ ] Giá **đóng nến vượt hẳn** mức và giữ ngoài → đó là break thật, không phải sweep.
- [ ] Không có displacement/MSS sau sweep — giá đi ngang quanh mức.
- [ ] Sweep ngược bias / sai premium-discount.
- [ ] Sau khi vào, giá đóng nến lại ngoài đáy/đỉnh sweep (double sweep) → cắt lệnh.
- [ ] Sweep giữa range không có POI / target rõ.

| Quan sát | Tên gọi | Cách đọc hợp lý |
|---|---|---|
| Wick xuyên mức, đóng nến trở lại trong vùng, kèm displacement ngược | **Sweep thành công** | Liquidity đã bị lấy → tìm entry đảo chiều |
| Xuyên mức, đóng nến trở lại nhưng KHÔNG có displacement | **Sweep yếu / chưa xác nhận** | Chờ thêm; có thể chỉ test |
| Đóng nến vượt hẳn mức + acceptance + đi tiếp | **Break thật (BOS)** | Tiếp diễn xu hướng, KHÔNG đảo |
| Reclaim rồi lại bị quét sâu hơn | **Double sweep / failed reversal** | Stop bị quét; cần vùng sâu hơn |

> [!note]
> **Double sweep** là cái bẫy phổ biến: cú sweep đầu kéo bạn vào, cú sweep thứ hai sâu hơn quét stop của bạn rồi mới đảo thật. Vào tại POI HTF lớn hơn và chờ displacement rõ giúp giảm rủi ro này; stop nên nằm ngoài cả vùng POI, không sát mép.

> [!note] Chú thích v2
> Bốn hàng của v1 ánh xạ: "Sweep thành công" = REJECTED + REVERSAL CONF.; "Sweep yếu" = REJECTED → STALE hoặc còn trong cửa sổ m; "Break thật" = ACCEPTED (E4); "Double sweep" = REJECTED → re-break + acceptance tới mức sâu hơn (T1/E6) hoặc E9. "Double sweep" có cấu trúc dự đoán được khi có pool xếp tầng (v1 W2, §23.4).

---

## 13. Liquidity Sweep + Market Structure / MSS

### 13.1 Sweep có "tạo ra" MSS không?

**Không.** Sweep và MSS là hai sự kiện quan sát được *độc lập*, xảy ra ở hai thời điểm khác nhau:

```text
Liquidity (mức ex-ante)
   ↓  [PENETRATED → REJECTED]       ← sự kiện liquidity (khung của MỨC)
Sweep
   ↓  [m nến]
MSS?   ← sự kiện cấu trúc: close qua swing tham chiếu có ý nghĩa (khung của SWING)
   ↓
Displacement?   ← tính chất của leg tạo MSS
   ↓
New structure?  ← chuỗi LH/LL mới ở khung đó
```

Cách đọc đúng: **MSS là bằng chứng rằng rejection có hậu quả cấu trúc** — dòng lệnh ngược chiều đã kéo dài đủ lâu và đủ mạnh để phá một swing mà người khác dùng làm tham chiếu. Sweep không cần MSS để tồn tại (R2), và MSS không cần sweep để tồn tại (ô ③ dưới đây).

### 13.2 Ma trận Sweep × MSS

![[LS-Deep-13-Sweep-x-MSS-Ma-Tran.svg|900]]
*Hình LS-Deep-13: Bốn ô, bốn ý nghĩa dự báo khác nhau — tất cả là giả thuyết cho tới khi đo.*

| Ô | Mô tả | Diễn giải | Hành động (v0.1) | Giả thuyết |
|---|---|---|---|---|
| ① Sweep + MSS (+ displacement) | Rejection tại mức ex-ante → phá swing tham chiếu bằng displacement trong m nến | Ứng viên reversal — lõi ICT 2022 | Tìm trigger (FVG retrace) | HYP-LS-010: E[R] ① > ② và > ③ |
| ② Sweep, không MSS | Rejection có, swing tham chiếu không bị phá | Chưa xác nhận; có thể là pullback trong run (A1) hoặc R2 | Không trade reversal; theo dõi re-break | — |
| ③ MSS, không sweep | Swing bị phá mà không có sự kiện tại mức ex-ante nào | (a) pool ở khung khác/không trong danh sách; (b) đổi hướng không qua liquidity event; (c) continuation sau pullback | Kiểm tra danh sách mức **trước** khi gọi là sweep. Nếu dùng làm setup → ghi `event_code: none` | So sánh E[R] ③ vs ① cho biết giá trị gia tăng của điều kiện sweep |
| ④ Không cả hai | Không sự kiện | Không có setup | Không có lệnh | — |

**Chiều thứ ba — displacement:** MSS bằng nến mở rộng (≥ x·ATR, để lại FVG) khác MSS bằng trôi chậm. Thứ tự và khoảng cách thời gian (sweep → MSS ≤ m nến) phải được ghi; MSS xảy ra 40 nến sau sweep không còn là "sweep + MSS" theo nghĩa của model.

### 13.3 Ý nghĩa thuộc về swing bị phá (R7)

Nguyên tắc kế thừa từ DR-v0.1 và [[59-Daily-Bias]]: *ý nghĩa của một MSS thuộc về swing bị phá, không thuộc về chart nơi bạn nhìn thấy sự kiện*. Áp dụng cho sweep:
- Sweep một swing M5 + MSS phá một swing M5 → sự kiện **M5**. Nó không đảo D1 bias.
- Sweep PDH (mức D1) + MSS phá swing H1 có ý nghĩa → ứng viên reversal **trong ngày**, phù hợp framework D1 → H1 → M5 khi D1 bias đồng hướng.
- Phân biệt "simple swing break" và "meaningful MSS": xem [[21-Market-Structure-Shift]]; trong note này MSS hợp lệ yêu cầu swing tham chiếu thuộc **Level ≥ 2** theo khung setup và close (không chỉ wick) qua swing.

### 13.4 Ranh giới Sweep vs Inducement vs MSS *(v1 §14)*

> [!danger] Góc nhìn từ Liquidity Sweep — vì sao "sweep" là từ bị lạm dụng nhiều nhất trong ba khái niệm
> Trong thực chiến, "sweep" thường bị dùng như một từ chung cho MỌI cú giá xuyên qua một mức rồi quay lại — bất kể đó là quét mồi trung gian (Inducement) hay quét pool chính dẫn tới đảo chiều thật. Bài phân định đầy đủ nằm ở [[21-Market-Structure-Shift]] mục 16; ở đây nhấn vào điểm mà Liquidity Sweep dễ bị hiểu sai nhất — **sweep là một HÀNH ĐỘNG xuất hiện ở cả hai vai trò (mồi và pool chính), không tự nó cho biết vai trò nào**.

**Câu hỏi cốt lõi mà Liquidity Sweep trả lời:** *"Giá VỪA lấy thanh khoản ở đâu, và cú lấy đó có displacement + reclaim hợp lệ không?"* — đây là một quan sát HÀNH ĐỘNG, xác nhận SAU KHI nến đã đóng. Sweep không tự phân loại "đây là mồi" hay "đây là điểm đảo" — việc phân loại đó phụ thuộc vào VỊ TRÍ của pool bị quét (đây chính là câu hỏi mà Inducement trả lời) và liệu có MSS xác nhận đảo chiều theo sau không (câu hỏi mà MSS trả lời).

**Bảng phân định nhanh theo góc nhìn sweep:**

| Loại Sweep | Vị trí pool | Có phải Inducement? | Có kèm MSS ngay sau? | Hành động đúng |
|---|---|---|---|---|
| Sweep pool nhỏ, gần POI HTF | Trung gian, giữa giá và POI | Đúng — đây chính là IDM bị quét | Không (hoặc chỉ micro-MSS không đáng tin) | KHÔNG entry — chờ giá tiếp tục tới POI |
| Sweep pool tại/ngay ngoài POI HTF (OB/FVG) | Tại POI, thường là cực dealing range | Không — đây là external/structural sweep | Có — kèm displacement + phá cấu trúc | Entry hợp lệ SAU reclaim + MSS |
| Sweep equal highs/lows dày (multi-poke) | Có thể là IDM (nếu trung gian) hoặc pool chính (nếu tại POI) | Tùy vị trí | Chỉ tại lần thọc CUỐI kèm displacement rời pool | Không vào theo poke đầu — chờ nhịp rời pool có displacement |
| Sweep trong nến tin tức (spike) | Có thể ở bất kỳ vị trí | Không xác định được chắc chắn trong lúc nến đang chạy | Không xác định được cho tới khi nến đóng ổn định | Chờ nến đóng + 1 nến xác nhận thêm trước khi phân loại |

**Ví dụ minh họa trên NQ — một chuỗi, ba lần dùng từ "sweep" với ba ý nghĩa khác nhau:**
```text
09:32 — "Sweep #1" tại đáy nhỏ 18,175 (đây thực chất là quét IDM, không đảo)
09:41 — "Sweep #2" tại đáy OB 18,135 (đây là quét pool chính tại POI — kèm MSS, đảo thật)
10:15 — "Sweep #3" trong nến CPI tại 18,090 (chưa xác định được là gì cho tới khi nến đóng ổn định)
```
Ba lần dùng đúng một từ "sweep" nhưng ý nghĩa hoàn toàn khác — kỷ luật đọc chart đòi hỏi luôn hỏi thêm "sweep NÀY đóng vai trò gì trong sequence?" trước khi hành động.

**Vì sao đây khác các case study đã có ở MSS/Inducement:** MSS (mục 16 của file MSS) đã cho ví dụ NQ phân định 3 khái niệm trên cùng một sequence tổng quát; Inducement (mục 16 của file Inducement) tập trung vào sự khác nhau giữa "sweep tại IDM" và "sweep tại pool chính". Bảng trên bổ sung góc nhìn thứ ba: từ chính hành động sweep, làm sao KHÔNG phân loại sai loại pool đang bị quét — đây là lỗi phổ biến nhất khi trader mới học, gọi bất kỳ wick nào là "sweep" mà không hỏi tiếp "sweep của POOL NÀO, vai trò gì".

> [!note] Chú thích v2
> Bảng v1 là cách dùng *vai trò của pool* (mồi vs pool chính) — tương thích với LSS (§9.3): pool "trung gian" thường có LSS thấp, pool "tại POI / cực range" có C và T cao. Cảnh báo: phân loại "đây là IDM" thường chỉ chắc chắn **sau** khi biết giá đi tiếp tới POI — tức là nhãn có độ trễ. Ghi nhãn IDM ex-ante (trước khi giá tới) để đo.

---

## 14. Liquidity Sweep + Displacement

### 14.1 Sweep có cần displacement không?

- **Để là sweep (DEF-LS-04):** không. Sweep chỉ cần xuyên + rejection.
- **Để là ứng viên reversal (DEF-LS-06):** có — displacement + MSS là lớp xác nhận.
- **Displacement sau sweep nghĩa là gì?** Dòng lệnh ngược chiều mạnh, một chiều, trong thời gian ngắn — tương ứng panel C của LS-Sim-03 (dòng lệnh mới), không phải panel A (impact phai).
- **Displacement có xác nhận rejection không?** Nó xác nhận rằng có *dòng lệnh mới* ngược chiều; nó không đảm bảo dòng đó kéo dài.
- **Displacement có thể xảy ra mà vẫn continuation không?** **Có.** Ví dụ: trong uptrend H1 mạnh, BSL của một swing M15 bị lấy, rồi một nến giảm thân lớn (displacement xuống) phá swing low M15 — nhưng đó chỉ là pullback về FVG H1; sau đó giá tiếp tục lên lấy BSL H1. Displacement ở khung thấp không vượt được bối cảnh khung cao (R7).

### 14.2 Lượng hóa displacement — biến đo và ngưỡng đề xuất

| Biến | Định nghĩa | Ngưỡng đề xuất (HEURISTIC) | Ghi chú |
|---|---|---|---|
| Body/ATR | \|close − open\| / ATR(14) của nến lớn nhất trong leg | ≥ 1.2–1.5 | ATR đóng băng trước sự kiện |
| Range/ATR | (high − low)/ATR | ≥ 1.5 | Bao gồm wick |
| Tốc độ | Số nến để đi ≥ 1·ATR theo hướng | ≤ 2–3 | Đo trên khung thấp hơn nếu có |
| Nến cùng hướng liên tiếp | Đếm | ≥ 2 | Dễ nhiễu ở M1 |
| FVG | Có gap giữa high nến i−1 và low nến i+1 (giảm) | Có, kích thước ≥ 0.1–0.3·ATR | [[13-FVG-Fair-Value-Gap]] |
| Structure break | Close qua swing tham chiếu Level ≥ 2 | Có | Trùng điều kiện MSS |
| CLV của nến displacement | (close − low)/(high − low) | ≤ 0.25 (giảm) / ≥ 0.75 (tăng) | Close gần cực trị |

Chi tiết và các phiên bản khác: [[50-Displacement-In-Depth]], [[35-Aggressive-Displacement-Entry]]. Tất cả là **[HEURISTIC]**; giá trị nằm ở việc **cố định** chúng trước khi test (v1 §16 phản biện của phản biện, giữ nguyên ý).

---

## 15. Liquidity Sweep + FVG

### 15.1 Vì sao ICT gắn sweep với FVG?

**[ICT FRAMEWORK]** FVG là "dấu chân" của displacement — một vùng giá chỉ được giao dịch một chiều trong khung nến đó; ICT coi nó là PD array nơi giá có xu hướng quay lại (rebalance) và là vị trí entry tinh chỉnh trong ICT 2022 Model.

**[MARKET MECHANICS]** Ở độ phân giải nến, FVG nghĩa là có một khoảng giá mà nến giữa đi qua với hai nến kề không chồng lấn — tức là chuyển động nhanh, một chiều. Nó **không** có nghĩa là "không có giao dịch" ở vùng đó (ở dữ liệu tick vẫn có), và việc giá "phải quay lại lấp" là **[HYPOTHESIS]** (trên random walk, giá quay lại chạm một vùng gần thường xuyên chỉ vì khoảng cách — cùng logic với §4.2).

### 15.2 Tách bốn vai trò

| Vai trò | Trong chuỗi | Câu hỏi | Ví dụ |
|---|---|---|---|
| **Liquidity event** | Sweep | Điều gì vừa xảy ra tại mức ex-ante? | SSL dưới Asia low bị xuyên rồi rejection |
| **Structural evidence** | MSS + displacement | Phản ứng có hậu quả cấu trúc không? | Close trên swing high M5 có ý nghĩa bằng nến 1.6·ATR |
| **Location** | FVG của leg displacement | Nếu giá quay lại, chỗ nào hợp lý để vào? | FVG 1.0812–1.0818 |
| **Execution trigger** | Giá chạm FVG trong m' nến | Khi nào vào? | Limit tại rìa gần FVG |

### 15.3 Đánh giá từng bước của chuỗi "Sweep → Shift → Displacement → FVG → Retracement → Entry"

| Bước | Có thể sai thế nào | Phép thử |
|---|---|---|
| Sweep | Mức không ex-ante; nhãn chỉ đúng ở một khung | Danh sách mức có known_at; nhãn theo khung của mức |
| Structural shift | Phá swing vi mô | Level swing ≥ 2 theo khung setup |
| Displacement | Ngưỡng co giãn | Ngưỡng cố định trước |
| FVG | FVG nhỏ, nhiều FVG chồng — chọn sau | Quy tắc chọn FVG cố định (FVG đầu tiên của leg — [[48-1st-Presented-Fair-Value-Gap]]) |
| Retracement | Không quay lại (v1 W5: lỡ tàu là kết quả trung tính) | Ghi `missed_valid_setup`; không chase |
| Entry | Khớp một phần / không khớp (v1 EC7) | Ghi fill thực tế; backtest với giả định fill bảo thủ |

Mỗi bước là một bộ lọc. Câu hỏi của backtest (ablation): **bỏ từng bước thì expectancy thay đổi bao nhiêu?** Nếu bỏ "sweep" mà expectancy không đổi → điều kiện sweep không đóng góp thông tin (HYP-LS-010).

---

## 16. Liquidity Sweep + POI

### 16.1 Location ≠ Liquidity Event ≠ Confirmation ≠ Entry Trigger ≠ Invalidation

![[LS-Deep-14-Location-Event-Confirmation-Trigger.svg|900]]
*Hình LS-Deep-14: Năm thành phần trả lời năm câu hỏi khác nhau; mỗi cái phải được ghi riêng.*

```text
HTF POI (location, D1/H1)
   ↓
Liquidity Sweep tại mức ex-ante cạnh POI (event, khung của mức)
   ↓
MSS + Displacement (confirmation, H1 → M5)
   ↓
FVG retrace (entry trigger, M5/M1)
   ↓
Stop ngoài cực trị sweep + buffer / acceptance lại bên kia L (invalidation)
```

### 16.2 Bản thân sweep có phải POI không?

**Không.** POI là một *vùng giá* được chọn ex-ante vì lý do cấu trúc (FVG, OB, biên range). Sweep là một *sự kiện*. Cực trị của sweep thì có vai trò: nó là **tham chiếu invalidation** (stop đặt ngoài nó) và trở thành **mức mới** (replenishment — §8.2). Nếu sau này giá quay lại cực trị sweep, đó là một sự kiện mới với mức mới.

**Hai cấu hình thường gặp:**
- *Sweep tại POI:* mức ex-ante nằm trong/ngay ngoài HTF POI (ví dụ SSL ngay dưới H1 bullish FVG). Đây là cấu hình chính của framework.
- *Sweep xa POI:* mức bị lấy ở giữa range, không có POI → trong v1 thuộc "Khi nào nên bỏ qua"; trong v2 là `poi_type: none` — vẫn ghi lại để có nhóm đối chứng.

---

## 17. Liquidity + Dealing Range + Premium/Discount

### 17.1 Biên range ≠ liquidity pool

Biên dealing range (range high/low) **thường trùng** với mức có liquidity (vì nó là swing cấu trúc nổi bật), nhưng hai khái niệm khác nhau:

| | Biên dealing range | Liquidity pool |
|---|---|---|
| Là gì | Mốc hình học định nghĩa container, P/D, EQ | Giả thuyết về mật độ lệnh |
| Chọn thế nào | Thuật toán chọn range (swing significance) — [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] | Danh sách mức ex-ante + LSS |
| Có thể tồn tại riêng? | Có — range có thể neo bởi swing không phải pool rõ | Có — pool bên trong range (IRL: EQL nội bộ) |
| Khi bị xuyên | Có thể dẫn tới re-map range | Sự kiện sweep/run |

Xem phân tích "raid vs break" ở [[12-Dealing-Range]] (hình DR-Deep-07) — note đó đã xử lý khi nào xuyên biên range là raid và khi nào là invalidation range.

### 17.2 Liquidity bên trong và bên ngoài range

- **ERL** (ngoài biên) thường là mục tiêu DOL; **IRL** (FVG, EQL nội bộ) là mục tiêu trung gian hoặc vùng retrace.
- **Con lắc ERL ↔ IRL [ICT FRAMEWORK]:** sau khi lấy ERL, giá được kỳ vọng về IRL; từ IRL đi tới ERL kế tiếp. Đây là mô tả hợp lý của dao động; giá trị dự báo là **[HYPOTHESIS]** — xem [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]].

### 17.3 Liquidity và Premium/Discount

- "BSL ở premium" là **thường đúng về hình học** (BSL nằm trên giá, phần trên của range là premium) — không phải quy luật hành vi.
- "Sweep BSL ở premium → short" là **[ICT FRAMEWORK]** nhất quán với logic mean-reversion trong range. Theo DR-v0.1 và [[27-Premium-Discount]]: dưới martingale, vị trí trong range **không** tạo expectancy; trong trend, giá nằm ở premium phần lớn thời gian (Daily Bias DB-Sim-07: drift +0.1σ/ngày → 66% số ngày ở premium). Vì vậy P/D là **bộ lọc vị trí**, không phải nguồn hướng.
- **Opposing liquidity:** sau một BSL sweep ở premium, "pool đối diện" (SSL dưới) là mục tiêu tự nhiên — nhưng xác suất chạm nó trước stop là p_null cho tới khi chứng minh ngược lại (LS-Sim-02).

---

## 18. Liquidity + Draw on Liquidity

### 18.1 DOL là gì — và DOL khác pool như thế nào

**DOL** (theo các note DOL của vault) là **pool được chọn làm mục tiêu kỳ vọng** của giá trong một khung thời gian, sau khi so sánh các ứng viên hai phía. Mọi DOL là một pool; không phải pool nào cũng là DOL.

| Khái niệm | Định nghĩa ngắn | Khác DOL ở đâu |
|---|---|---|
| Liquidity pool | Mức có thể tập trung lệnh | DOL là pool **được chọn** làm mục tiêu |
| Nearest liquidity | Pool gần nhất | Gần nhất có lợi thế hình học (§4.2), nhưng DOL có thể xa hơn nếu bối cảnh HTF đủ mạnh |
| External liquidity | Pool ngoài range context | Thường là ứng viên DOL ngày/tuần |
| Opposing liquidity | Pool phía ngược với DOL | Chính là **điểm invalidation tự nhiên** của giả thuyết DOL |
| DOL trong range | IRL được chọn làm mục tiêu trung gian | Hợp lệ khi range lớn và giá ở cực |
| DOL ngoài range | ERL | Mặc định của framework |

### 18.2 Vì sao một pool trở thành DOL còn pool khác thì không?

Formalization v0.1 (kế thừa và rút gọn từ [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] và [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]]):

1. **Ứng viên hai phía:** liệt kê pool trên và pool dưới thỏa G1–G5.
2. **Baseline:** tính p_null (có cửa sổ thời gian T của phiên/ngày) cho từng cặp.
3. **Bằng chứng định hướng ex-ante:** D1 bias state, vị trí trong range D1, liquidity đã bị lấy gần đây ở phía nào (pool phía đã bị lấy không còn là ứng viên).
4. **LSS** của từng ứng viên.
5. **Chọn** ứng viên có (bằng chứng định hướng + LSS) vượt baseline theo quy tắc khai báo; nếu không có → DOL = UNCLEAR.
6. **Invalidation:** opposing pool bị lấy với acceptance, hoặc MSS ngược ở khung D1.

### 18.3 Thứ bậc mục tiêu trong một run (§36 của brief)

```text
Current price
   ↓
Nearest liquidity  (thường bị chạm trước — hình học)
   ↓
Next liquidity
   ↓
External liquidity (biên range context)
   ↓
HTF DOL
```

**Không giả định giá luôn lấy pool gần nhất trước.** Ví dụ: hai pool trên ở 1 ATR và 2.5 ATR, một pool dưới ở 1.5 ATR. Xác suất hình học chạm pool trên gần trước pool dưới = 1.5/2.5 = 60%; chạm pool trên xa trước pool dưới = 1.5/4 = 37.5%. Một "run" từ hiện tại tới pool xa mà không chạm pool dưới là sự kiện có xác suất baseline 37.5% — không hiếm. Trong run đã xác nhận (đã có drift), các xác suất này thay đổi theo công thức có drift (§4.2).

**Exhaustion và opposing liquidity:** run càng tiến xa, opposing liquidity (HL gần nhất, swing low của leg cuối) càng *gần* giá → p_null của việc mất nó tăng dần. Đây là một lý do hình học khiến run "dễ gãy" ở cuối — không cần giả định "Smart Money đã đạt mục tiêu".

---

## 19. Liquidity Run và exhaustion

![[LS-Deep-15-Liquidity-Run-Chuoi-Va-Exhaustion.svg|900]]
*Hình LS-Deep-15: Run L1 → L4 với acceptance; L5 bị lấy nông rồi rejection; MSS ngược (mất HL gần nhất) → run có thể đã kết thúc.*

### 19.1 Khi nào một run kết thúc? — các dấu hiệu và mức bằng chứng

| Dấu hiệu | Định nghĩa đo được | Nhãn | Đủ một mình? |
|---|---|---|---|
| Rejection tại mức kế tiếp | Sweep (DEF-LS-04) tại L_{n+1} | [OBSERVABLE] + [HYPOTHESIS] về hàm ý | Không |
| MSS ngược ở khung run | Close qua HL gần nhất (Level ≥ 2) | [OBSERVABLE] | Không — có thể là pullback sâu |
| Retracement sâu dần | r_i tăng qua các lần lấy | [HYPOTHESIS] HYP-LS-013 | Không |
| Displacement theo hướng run nhỏ dần | Body/ATR giảm dần | [HYPOTHESIS] | Không |
| Volatility contraction | ATR khung thấp giảm khi tiến tới mức | [HYPOTHESIS] | Không |
| Đã tới DOL / ERL của range context | Mục tiêu khai báo trước đã bị chạm | [ICT FRAMEWORK] | Không — "đạt mục tiêu" không cấm đi tiếp |
| Opposing liquidity gần | HL gần nhất trong < x·ATR | [MATHEMATICAL] (p_null tăng) | Không |
| Thời gian | Hết killzone / phiên | [HYPOTHESIS] HYP-LS-005 | Không |

### 19.2 Exhaustion scorecard (HYPOTHESIS)

ES = số dấu hiệu xuất hiện trong cửa sổ w nến gần nhất (0–8). Giả thuyết HYP-LS-013: P(run kết thúc trong N nến | ES ≥ 3) > P(… | ES ≤ 1) sau khi kiểm soát khoảng cách tới HL gần nhất. **Không dùng ES để vào lệnh đảo chiều**; dùng để *ngừng tìm setup cùng chiều run* (giảm rủi ro), cho tới khi có REVERSAL CONF. theo quy trình §20.

---

## 20. Máy trạng thái sự kiện liquidity

### 20.1 Đánh giá state machine trong brief

State machine của brief (NO EVENT → APPROACH → TOUCH → PENETRATION → REJECTION/ACCEPTANCE → REVERSAL/CONTINUATION → MSS/LIQUIDITY RUN → DISPLACEMENT/NEXT LIQUIDITY) đúng hướng nhưng chưa code được vì:

1. **Thiếu thời gian.** Không có timer → một sự kiện có thể ở trạng thái PENETRATION mãi. Thiếu PENDING/EXPIRED.
2. **Thứ tự REVERSAL → MSS → DISPLACEMENT bị ngược.** "Reversal" là kết luận; MSS + displacement là bằng chứng *dẫn tới* kết luận. Trong máy trạng thái, REVERSAL CONF. phải đứng **sau** MSS + displacement.
3. **Không có đường quay lại.** Thực tế REJECTED có thể thành ACCEPTED (re-break), ACCEPTED có thể thành FAILED BO. Thiếu các cạnh này thì nhãn trở thành vĩnh viễn — sai.
4. **Không có điều kiện đánh giá.** Phải quy định: chỉ chuyển trạng thái tại bar close của khung nào.
5. **Thiếu trạng thái hệ thống:** IDLE/ARMED (có mức ex-ante gần giá hay không), NEWS SUSPEND.

### 20.2 Máy trạng thái v0.1

![[LS-Deep-16-State-Machine-Su-Kien-Liquidity.svg|900]]
*Hình LS-Deep-16: Chuyển trạng thái chỉ tại bar close; mỗi chuyển ghi known_at; nhãn append-only.*

| Trạng thái | Vào khi | Ra khi | Ghi chú |
|---|---|---|---|
| **IDLE** | Không có mức ex-ante trong ≤ x·ATR | Có mức trong ≤ x·ATR → ARMED | x = 1.5 ATR (HEURISTIC) |
| **ARMED** | Mức L thỏa G1–G5 ở gần; context D1/H1 đã ghi | \|giá − L\| ≤ ε → PROBING; giá rời xa → IDLE | Ghi LSS, p_null tại đây |
| **PROBING** | Giá trong ε của L | high > L + ε → PENETRATED; rời xa → ARMED (ghi E1 nếu chạm, E0 nếu không) | |
| **PENETRATED** | Nến xuyên đóng | Ngay lập tức → PENDING | Ghi độ sâu, giờ, `known_at` |
| **PENDING** | Chưa phân xử | REJECTED / ACCEPTED / EXPIRED (j + k) | **Không hành động** |
| **REJECTED** | close < L − δ trước acceptance | MSS + disp ≤ m → REVERSAL CONF.; hết m → STALE; re-break + acceptance → ACCEPTED (ghi dòng mới) | |
| **ACCEPTED** | 2 close > L hoặc close > L + 0.5·ATR | close < L − δ → FAILED BO; lấy mức kế → RUN ACTIVE | |
| **FAILED BO (E3)** | Sau acceptance, close lại < L − δ | Xử lý như REJECTED (cần MSS + disp) | |
| **REVERSAL CONF.** | DEF-LS-06 thỏa | Trigger trong m' nến → ENTRY; hết m' → hủy | |
| **STALE** | Rejection nhưng không MSS + disp trong m | Kết thúc sự kiện | Nhánh R2 |
| **RUN ACTIVE** | ≥ 2 mức cùng phía accepted | Lấy mức kế → (ARMED mức kế); exhaustion → RUN ENDED | |
| **RUN ENDED** | Rejection tại mức kế / MSS ngược ở khung run | Kết thúc chuỗi | Mức cuối có thể là REJECTED → xét reversal |
| **EXPIRED** | Hết k nến chưa phân xử | Kết thúc | |
| **NEWS SUSPEND** | Cửa sổ tin tier-1 | Hết cửa sổ → trạng thái trước (đánh giá lại từ đầu) | Từ MỌI trạng thái |

### 20.3 Pseudocode (implementable)

```python
# Liquidity event engine v0.1 — mọi hàm chỉ đọc bars[: t+1] (không nhìn tương lai)
# Tham số khai báo trước: EPS, DELTA, K, M, M_ENTRY, X_ARM (đơn vị ATR), ACC_ATR = 0.5

from dataclasses import dataclass, field

@dataclass
class Level:
    price: float
    side: str          # 'BSL' (trên giá) hoặc 'SSL' (dưới giá)
    known_at: int      # chỉ số nến mà mức trở nên biết được
    tf: str            # khung của swing tạo mức
    lss: float = 0.0
    taken: bool = False

@dataclass
class Event:
    level: Level
    state: str = 'ARMED'
    j: int = None              # nến xuyên
    t_state: int = None        # nến vào trạng thái hiện tại
    extreme: float = None      # cực trị của cú xuyên
    atr0: float = None         # ATR đóng băng tại nến trước xuyên
    log: list = field(default_factory=list)   # append-only: (t, state, note)

def sgn(side):            # +1 cho BSL (xuyên lên), -1 cho SSL (xuyên xuống)
    return 1 if side == 'BSL' else -1

def beyond(px, L, s, d=0.0):   # px nằm "bên kia" mức L thêm d theo hướng s
    return s * (px - L) > d

def step(ev, t, bar, atr, news_window, swing_ref, displacement_ok):
    """Gọi tại close của nến t. swing_ref: swing tham chiếu cho MSS (Level>=2, khung setup)."""
    L, s = ev.level.price, sgn(ev.level.side)
    if news_window(t):
        ev.log.append((t, 'NEWS_SUSPEND', '')); ev.state = 'NEWS_SUSPEND'; return ev
    if ev.state in ('ARMED', 'PROBING'):
        hi_or_lo = bar.high if s > 0 else bar.low
        if beyond(hi_or_lo, L, s, EPS * atr):
            ev.j, ev.atr0 = t, atr
            ev.extreme = hi_or_lo
            ev.state, ev.t_state = 'PENDING', t
            ev.log.append((t, 'PENETRATED', f'depth={s*(hi_or_lo-L)/atr:.2f}ATR'))
        # (nếu không: cập nhật ARMED/PROBING theo khoảng cách — lược)
    if ev.state == 'PENDING':
        A = ev.atr0
        ev.extreme = max(ev.extreme, bar.high) if s > 0 else min(ev.extreme, bar.low)
        two_closes = (t > ev.j) and beyond(bar.close, L, s) and beyond(prev_close(t), L, s)
        if beyond(bar.close, L, s, ACC_ATR * A) or two_closes:
            ev.state, ev.t_state = 'ACCEPTED', t; ev.log.append((t, 'ACCEPTED', ''))
        elif beyond(L, bar.close, s, DELTA * A):          # close bên trong, cách L ≥ δ
            ev.state, ev.t_state = 'REJECTED', t; ev.log.append((t, 'REJECTED', ''))
        elif t - ev.j >= K:
            ev.state = 'EXPIRED'; ev.log.append((t, 'EXPIRED', ''))
        return ev
    if ev.state == 'REJECTED':
        mss = beyond(swing_ref, bar.close, s)              # close qua swing ref theo hướng ngược
        if mss and displacement_ok(t, -s):
            ev.state, ev.t_state = 'REVERSAL_CONF', t; ev.log.append((t, 'REVERSAL_CONF', ''))
        elif beyond(bar.close, L, s, ACC_ATR * ev.atr0):   # re-break mạnh
            ev.state, ev.t_state = 'ACCEPTED', t; ev.log.append((t, 'ACCEPTED', 'rejection_failed'))
        elif t - ev.t_state >= M:
            ev.state = 'STALE'; ev.log.append((t, 'STALE', ''))
        return ev
    if ev.state == 'ACCEPTED':
        if beyond(L, bar.close, s, DELTA * ev.atr0):
            ev.state, ev.t_state = 'REJECTED', t; ev.log.append((t, 'FAILED_BO', 'treat_as_rejected'))
        # chuyển sang RUN_ACTIVE do lớp quản lý chuỗi xử lý khi mức kế tiếp cùng phía bị ACCEPTED
        return ev
    return ev
```

**Nguyên tắc của code:** (1) mọi giá trị dùng tại t chỉ đến từ nến ≤ t; (2) swing tham chiếu chỉ dùng khi đã xác nhận (known_at ≤ t); (3) log append-only — không bao giờ sửa một dòng cũ; (4) ATR đóng băng tại nến trước xuyên. Lớp quản lý chuỗi (run) giữ danh sách sự kiện theo phía và đếm số ACCEPTED liên tiếp.

---

## 21. Nhận diện theo thời gian thực vs hậu kiểm

### 21.1 Hai câu hỏi khác nhau

- **Ex-post:** "Đây rõ ràng là một liquidity sweep." — câu nói sau khi đã thấy toàn bộ chart, kể cả phần bên phải.
- **Real-time:** "Tại close của nến này, tôi thực sự biết gì?"

![[LS-Deep-17-Real-Time-vs-Ex-Post.svg|900]]
*Hình LS-Deep-17: t0 → t5. Nhãn "sweep → reversal" chỉ đúng nghĩa ở t5.*

### 21.2 Biết gì, chưa biết gì, tại từng thời điểm

| Thời điểm | Đã biết | Chưa biết | Trạng thái |
|---|---|---|---|
| **t0** — giá tiến tới L | L, known_at, khoảng cách, giờ, context D1/H1, LSS, p_null | Có chạm không | ARMED / PROBING |
| **t1** — giá đang ở trên L (nến chưa đóng) | Giá đã giao dịch trên L (intrabar) | Close ở đâu; sweep hay break | (chưa có trạng thái — chưa phải bar close) |
| **t2** — nến xuyên đóng dưới L | Close < L → rejection **tạm** (E2 nếu < L − δ) | Có re-break không; có MSS không | PENDING hoặc REJECTED |
| **t3** — 1–2 nến sau | Rejection giữ được m₁ nến | MSS? displacement? R1 hay R2? | REJECTED |
| **t4** — MSS + displacement | Swing tham chiếu bị phá bằng displacement | Có retrace vào FVG không; tới target hay stop | REVERSAL CONF. |
| **t5** — kết quả | Tới pool đối diện trước stop (hoặc ngược lại) | — | Ex-post |

Khi giá vừa wick qua high, brief hỏi: *tôi biết gì?* — **Biết:** giá đã giao dịch trên high. **Không biết:** nó sẽ reject hay accept; MSS có xảy ra không; displacement; liệu lệnh có điều kiện có thật sự ở đó; liệu đây là sweep của pool chính hay của inducement; liệu pool sâu hơn còn không.

### 21.3 Bốn cơ chế khiến phân tích trở nên "dễ" một cách giả tạo

1. **Future-dependent labels.** "Sweep", "run", "MSS hợp lệ", "IDM" đều cần dữ liệu *sau* sự kiện. Gán nhãn trên chart đã hoàn tất = dùng thông tin của t5 cho quyết định ở t1–t2.
2. **Confirmation delay.** Swing fractal n chỉ được xác nhận sau n nến; swing directional-change chỉ sau khi giá đi ngược θ. Mức chỉ tồn tại từ known_at.
3. **Repainting.** SMT, "swing hoàn thành", "đỉnh của ngày" — có thể vẽ lại khi giá còn chạy. Indicator vẽ swing/pool hồi tố là nguồn rò rỉ tương lai phổ biến nhất trong backtest thủ công.
4. **Hindsight + survivorship trong ví dụ.** Ảnh chụp chart được chọn vì kết quả đẹp. Trên random walk, 30–50% lần xuyên mức đóng lại bên trong (LS-Sim-01) — một bộ sưu tập "sweep đẹp" luôn tìm được. Fischhoff (1975): biết kết quả làm ta đánh giá kết quả đó là "dễ đoán" hơn thực tế.

### 21.4 Độ trễ và tỷ lệ lật nhãn trên null model

![[LS-Sim-05-Label-Latency.png]]
*Hình LS-Sim-05 **[SIMULATION]**: (A) Với quy tắc v0.1, tại close của nến xuyên 59% sự kiện còn PENDING; sau 1 nến 12%; sau 3 nến < 1%. (B) Tỷ lệ nhãn bị lật (REJECTED → ACCEPTED, hoặc ngược lại): 29% trong 3 nến, 44% trong 6, 58% trong 12, 70% trong 24, 78% trong 48 nến.*

**Đọc hình:** trên random walk, sau khi xuyên mức giá nằm ngay cạnh mức, nên nó qua lại mức thường xuyên — nhãn có tuổi thọ ngắn. Đây là **baseline**: một quy tắc phân loại có giá trị trên dữ liệu thật khi flip rate của nó ở các mức LSS cao **thấp hơn rõ rệt** đường cong này (HYP-LS-011). Nếu flip rate thực tế ≈ null, nhãn sweep/break không mang thông tin về tương lai — chỉ mô tả quá khứ.

### 21.5 Giao thức thực hành chống hindsight

1. **Danh sách mức trước phiên** (RULE-LS-001) — chụp ảnh/ghi file có timestamp.
2. **Bar replay** khi review: che phần bên phải, quyết định từng nến, ghi trạng thái.
3. **Mỗi nhãn có known_at**; nhãn mới không xóa nhãn cũ (RULE-LS-007).
4. **Tách hai cột trong journal:** "nhãn tại thời điểm quyết định" và "nhãn sau expiry". Thống kê chỉ dùng cột thứ nhất cho đánh giá quyết định.
5. **Đếm cả sự kiện không trade:** mọi lần mức ex-ante bị xuyên đều được ghi (event study), không chỉ những lần có setup đẹp.

---

## 22. Áp dụng: D1 → H1 → M5

### 22.1 Vai trò của từng khung với liquidity

| Khung | Câu hỏi liquidity | Output |
|---|---|---|
| **D1 — Context** | Pool nào quan trọng (ERL của range D1, PDH/PDL, PWH/PWL)? Phía nào đã bị lấy gần đây? DOL nào? Bias state? | Danh sách mức HTF + DOL + bias state + invalidation |
| **H1 — Setup** | POI nào nằm cạnh mức liquidity ex-ante phía ngược DOL? Liquidity nào đang được "xây" (EQH/EQL, session H/L)? | Cặp (POI, mức) + kịch bản + giờ dự kiến |
| **M5 — Execution** | Tại mức: sự kiện là gì (E-code)? REJECTED trong k? MSS + displacement trong m? FVG trigger? | Entry / no-trade + log trạng thái |

**Không cho M5 ghi đè D1** (project rule; R7): một M5 sweep + MSS ngược D1 bias không lật bias; nó tối đa là một sự kiện M5.

### 22.2 Quy trình đa khung *(v1 §4)*

![[Liquidity-Sweep-MTF-Workflow.svg]]
*Hình v1: Top-down D1/H4 → H1/M15 → M5/M1 với 4 câu hỏi bắt buộc.*

> [!example] Quy trình 4 câu bắt buộc trước khi dùng Liquidity Sweep
> 1. **Pool liquidity nào đang là mục tiêu, và cú quét vừa rồi lấy pool nào?**
> 2. **Đây là sweep (reclaim + displacement) hay break thật (đóng nến ngoài)?**
> 3. **Sweep có ở đúng POI HTF + premium/discount + đồng hướng bias không?**
> 4. **Đáy/đỉnh sweep ở đâu để đặt stop, và target liquidity phía đối diện ở đâu?**

#### D1 / H4 — Bias & Narrative
- **Bias hiện tại:** Bullish / Bearish / Neutral (xem [[59-Daily-Bias]]).
- **Pool liquidity HTF:** đánh dấu PDH/PDL, PWH/PWL, equal highs/lows lớn — đây là các mức dễ bị sweep và là draw on liquidity.
- **Draw on liquidity:** giá đang bị hút về pool nào? Sweep ở phía ngược thường mở ra leg đi về pool đó.

#### H1 / M15 — POI & Context
- **POI cụ thể:** xác định FVG/OB nơi kỳ vọng sweep xảy ra, ví dụ `giá quét SSL dưới đáy M15 tại 1.0810 ngay trong vùng H1 bullish FVG`.
- **Loại pool:** equal lows / đáy cũ / PDL. Ghi rõ mức.
- **Phân biệt sweep vs break:** chờ nến H1/M15 đóng — đóng lại bên trong = sweep; đóng ngoài = break.

#### M5 / M1 — Confirmation & Entry
- **Reclaim + MSS:** sau khi giá quét pool, chờ M5/M1 reclaim mức và tạo MSS ngược hướng quét.
- **Displacement + FVG:** displacement sau sweep thường để lại FVG nhỏ làm điểm entry refined.
- **Entry:** vào tại FVG/OB của đoạn displacement, hoặc retest mức vừa reclaim.
- **Stop loss logic:** đặt ngay ngoài đáy/đỉnh của cú sweep (nơi liquidity vừa bị lấy) — đây là stop "an toàn" nhất vì market vừa quét xong vùng đó.

```text
Mẫu ghi nhanh — Long sau SSL Sweep
HTF Bias: Bullish | Location: Discount
Pool bị quét: equal lows / PDL tại [level]
Sweep xác nhận: wick xuống + đóng nến TRỞ LẠI trên [level]
POI: H1 bullish FVG/OB [range]
Confirm: M5 reclaim + bullish MSS + displacement
Entry: FVG đoạn displacement / retest mức reclaim
Stop: dưới đáy cú sweep ([sweep low])
Target: BSL phía trên ([level])
Invalid: đóng nến M15/H1 lại xuống dưới [level] (thành break thật)
```

```text
Mẫu ghi nhanh — Short sau BSL Sweep
HTF Bias: Bearish | Location: Premium
Pool bị quét: equal highs / PDH tại [level]
Sweep xác nhận: wick lên + đóng nến TRỞ LẠI dưới [level]
POI: H1 bearish FVG/OB [range]
Confirm: M5 reclaim + bearish MSS + displacement
Entry: FVG đoạn displacement / retest mức reclaim
Stop: trên đỉnh cú sweep ([sweep high])
Target: SSL phía dưới ([level])
Invalid: đóng nến M15/H1 lại lên trên [level] (thành break thật)
```

> [!warning]
> **Đừng trade cú sweep — trade phản ứng sau cú sweep.** Vào lệnh ngay trên wick khi giá còn đang quét là cách nhanh nhất để bị "double sweep" (quét sâu hơn). Luôn chờ reclaim + displacement.

> [!note] Chú thích v2 cho quy trình v1
> - "Chờ nến H1/M15 đóng — đóng lại bên trong = sweep; đóng ngoài = break" → đúng tinh thần, nhưng là nhãn **tạm** (§12, LS-Sim-05). Dùng timer k và trạng thái PENDING.
> - "Stop… ngay ngoài đáy/đỉnh cú sweep — đây là stop 'an toàn' nhất vì market vừa quét xong vùng đó" → **[INTERPRETATION]**. Cực trị sweep là nơi stop mới của người vào lệnh đảo chiều được đặt (replenishment — §8.2), nên chính nó có thể thành pool mới. v1 đã nhận ra điều này ở W2 (double sweep). RULE-LS-004: stop ngoài cực trị + buffer ≥ max(0.15·ATR, 3×spread) hoặc ngoài POI.
> - Mẫu ghi nhanh của v1 được giữ; schema journal đầy đủ ở §26.3.

### 22.3 Thời gian của sweep *(v1 §7.2, có nhãn v2)*

Không phải mọi cú quét đều bình đẳng theo giờ. Các cửa sổ mà sweep mang intent thuật toán:

| Cửa sổ (NY time) | Tên | Hành vi sweep điển hình |
|---|---|---|
| **02:00–05:00** | London KZ | **Judas swing** — quét một đầu Asia range / PDL-PDH, tạo high/low của ngày; sweep quan trọng nhất với FX |
| **07:00–09:00** | NY pre-market | Quét London high/low trước khi NY chọn hướng thật |
| **08:30** | News embargo | Spike tin quét pool hai phía trong vài giây — không trade trong spike, đọc pool nào bị lấy SAU spike |
| **09:30–10:00** | NYSE opening run | Quét đỉnh/đáy pre-market/overnight của index; setup cho leg AM |
| **~09:50–10:10, 10:50–11:10** | Macro windows | Run-on-liquidity ngắn của thuật toán; sweep trong macro thường đảo rất nhanh |
| **12:00–13:00** | Lunch | Sweep giờ này phần lớn là nhiễu thanh khoản mỏng — hạ độ tin xuống mức thấp nhất |

Nguyên tắc: **một sweep đúng chỗ nhưng sai giờ chỉ đáng một nửa độ tin.** Cùng cú quét equal lows tại discount: xảy ra 03:30 trong London KZ = tín hiệu hạng A; xảy ra 12:20 lunch = quan sát, không hành động. Ghi `sweep_time_window` vào journal để tự kiểm chứng trên dữ liệu của chính mình.

> [!note] Chú thích v2
> - Bảng cửa sổ giờ là **[ICT FRAMEWORK]**; mức độ "intent thuật toán" là **[INTERPRETATION]**. Cơ sở cơ chế có thật: dòng lệnh và biến động tập trung theo giờ (mở phiên, tin 08:30), và hồ sơ biến động trong ngày đã được ghi nhận (xem references của [[59-Daily-Bias]]). Nhưng lưu ý baseline: trên random walk *có hồ sơ biến động theo phiên*, cực trị của ngày cũng rơi vào các cửa sổ biến động cao một cách không cân xứng ([[59-Daily-Bias]] §7.1, DB-Sim-04) — tức "sweep hay xảy ra ở London open" một phần là do biến động tập trung ở đó.
> - "Một sweep đúng chỗ nhưng sai giờ chỉ đáng một nửa độ tin" → **[HYPOTHESIS]** HYP-LS-005; trường journal `sweep_time_window` giữ nguyên.

### 22.4 SMT Divergence như lớp xác nhận *(v1 §7.1, có nhãn v2)*

![[Liquidity-Sweep-Advanced-SMT.svg]]

Công cụ mạnh nhất để phân biệt sweep với break thật **trong thời gian thực** (trước khi nến đóng) là so sánh với thị trường tương quan:


- **Nguyên lý:** hai thị trường tương quan chặt (NQ–ES–YM; EURUSD–GBPUSD; DXY nghịch đảo với EURUSD) phải xác nhận lẫn nhau. Khi NQ quét xuống **lower low** mà ES **giữ higher low** (từ chối phá đáy tương ứng), đó là **SMT divergence** — bằng chứng cú phá của NQ là stop run có chủ đích, không phải sell-off thật. Thị trường "khỏe hơn" (không chịu phá đáy) tiết lộ hướng thật.
- **Cách dùng đúng:** SMT là **confirmation, không phải signal**. Chuỗi hợp lệ: giá vào HTF POI đúng premium/discount → sweep pool → **kiểm tra SMT ngay tại thời điểm sweep** → nếu diverge + displacement/MSS → entry với conviction cao hơn. SMT giữa range, ngoài POI = nhiễu (hai thị trường lệch nhau vài phút là chuyện thường).
- **Cảnh giác:** SMT có thể "vẽ lại" khi thị trường còn chạy — divergence chỉ chốt khi swing hoàn thành. Vì vậy vẫn cần displacement làm điều kiện đóng sập. Với NQ: dùng ES làm gương; với EURUSD: liếc GBPUSD và DXY (DXY quét ĐỈNH trong khi EU quét ĐÁY = cộng hưởng hoàn hảo cho Long EU).

> [!note] Chú thích v2
> - "Bằng chứng cú phá của NQ là stop run có chủ đích" → **[INTERPRETATION]**. Quan sát: hai thị trường tương quan không cùng tạo cực trị mới. Diễn giải cơ chế thay thế: khác biệt thành phần chỉ số, khác thời điểm tin riêng, khác thanh khoản tức thời.
> - SMT là **lớp xác nhận** phù hợp với framework; giá trị gia tăng cần đo bằng likelihood ratio (HYP-LS-014, tương tự HYP-DB-015 của Daily Bias). v1 đã nêu đúng rủi ro repainting của SMT.

### 22.5 Turtle Soup — mô hình hóa sweep *(v1 §7.4)*

[[33-Turtle-Soup]] là phiên bản model hóa của liquidity sweep: nguồn gốc từ việc trade ngược tín hiệu breakout 20-day high/low của hệ thống Turtle — tức **chuyên săn false breakout tại các mức ai-cũng-nhìn**. Bản ICT hiện đại:

```text
Turtle Soup Long (đối xứng cho Short):
1. Xác định mức reference "công cộng": old low rõ, PDL, PWL, equal lows nhiều ngày
2. HTF context: giá ở discount, draw HTF hướng lên (bias không chống lại)
3. Giá phá XUỐNG mức đó trong kill zone → kích hoạt sell stops + hút breakout sellers
4. Reclaim trong 1–3 nến + displacement + MSS trên LTF
5. Entry FVG của displacement; stop dưới đáy sweep; target liquidity đối diện
```

Điểm cần hiểu sâu: Turtle Soup có edge vì nó trade **ngược lại hai đám đông cùng lúc** — người bị quét stop (buộc phải bán đúng đáy) và người đu breakout (bán đúng đáy). Cả hai dòng lệnh sell đó chính là thanh khoản cho lệnh buy của smart money — và của mình. Đây là lý do sweep tại mức càng "nổi tiếng" (PDL, đáy tuần, equal lows nhiều lần chạm) thì reversal càng bạo lực.

> [!note] Chú thích v2
> - Nguồn gốc: mô hình "Turtle Soup" được Linda Bradford Raschke và Laurence Connors trình bày trong *Street Smarts* (1995), dựa trên việc fade breakout 20 ngày của hệ thống Turtle. ICT dùng lại tên này.
> - "Edge vì trade ngược hai đám đông" → **[INTERPRETATION]**; "sweep tại mức càng nổi tiếng thì reversal càng bạo lực" → **[HYPOTHESIS]** — lưu ý Osler (2005) dự báo chiều ngược lại cho riêng cơ chế stop: vượt cụm stop lớn → cascade *tiếp diễn* mạnh hơn. Hai dự báo đối lập này chính là thứ đáng test (HYP-LS-007).

### 22.6 Cây quyết định D1 → H1 → M5

![[LS-Deep-18-Cay-Quyet-Dinh-D1-H1-M5.svg|900]]
*Hình LS-Deep-18: Chín câu hỏi; "không" ở bất kỳ bước nào → nhánh bên phải.*

```text
D1 — CONTEXT
Q1 Bias state D1 ∈ {BULLISH, BEARISH}?
 ├─ KHÔNG → NEUTRAL/UNCLEAR/CONFLICTED → chỉ quan sát, ghi journal
 └─ CÓ
Q2 DOL đã chọn (so hai phía, có p_null, có invalidation)?
 ├─ KHÔNG → không có target → không trade reversal
 └─ CÓ
H1 — SETUP
Q3 Có HTF POI + mức liquidity EX-ANTE phía ngược DOL, cạnh POI?
 ├─ KHÔNG → mức vẽ sau khi giá tới không tính (hindsight)
 └─ CÓ
Q4 Giá tới POI/mức trong killzone, ngoài cửa sổ tin tier-1?
 ├─ KHÔNG → SUSPEND hoặc hạ cấp
 └─ CÓ
M5 — EXECUTION
Q5 Sự kiện tại mức là E2/E3 (xuyên rồi về)?
 ├─ E0/E1 → chờ   ├─ E4/E5 → không trade reversal (có thể là run phía DOL? xem RULE-LS-005)
 └─ E2/E3
Q6 REJECTED trong k nến (close < L − δ)?
 ├─ KHÔNG → EXPIRED → bỏ
 └─ CÓ
Q7 MSS (swing Level ≥ 2 khung setup) + displacement trong m nến?
 ├─ KHÔNG → STALE (R2) → bỏ
 └─ CÓ
Q8 FVG/trigger trong m' nến; R:R tới target ≥ tối thiểu?
 ├─ KHÔNG → không chase (W5)
 └─ CÓ
Q9 Stop ngoài cực trị sweep + buffer; risk ≤ 0.5%?
 ├─ KHÔNG → bỏ
 └─ CÓ → ENTRY; ghi event_code, known_at, p_null, LSS, mss_tf, disp_atr
```

### 22.7 Điều kiện theo nhóm (project §37)

| Nhóm | Điều kiện |
|---|---|
| **Required** | Mức ex-ante thỏa G1–G5; D1 bias state hợp lệ; DOL đã chọn; sự kiện E2/E3 → REJECTED trong k; MSS (Level ≥ 2) + displacement trong m; stop hợp lý; R:R ≥ tối thiểu |
| **Supporting** | Mức có LSS cao (ERL range D1, PDH/PWH, EQH); tại HTF POI; đúng P/D; killzone; reclaim body ≥ 50% range nến sweep; SMT divergence |
| **Optional** | Pool xếp tầng đã lập bản đồ (W2); FVG đầu tiên của leg; volume/tick data xác nhận |
| **Disqualifying** | Cửa sổ tin tier-1; tuần rollover/DST với mức nghi artifact (W6); bias UNCLEAR; E4/E5 tại mức; đã có nhiều sweep liên tiếp không rõ pool nào là chính; chase sau displacement > 50% leg |
| **Confirmation** | REJECTED → MSS + displacement (DEF-LS-06) |
| **Invalidation** | Acceptance lại bên kia L; giá vượt cực trị sweep + buffer; MSS ngược khung setup sau entry; hết m' không trigger |

### 22.8 Khi nào khái niệm có giá trị cao / khi nào nên bỏ qua *(v1 §2)*

#### Khi nào khái niệm này có giá trị cao?
- [ ] Có pool liquidity rõ ràng (equal highs/lows, PDH/PDL, swing cũ) ở đúng phía đối diện với hướng bias.
- [ ] Cú quét xảy ra tại **POI HTF** (FVG/OB) đồng hướng Daily Bias.
- [ ] Sweep nằm đúng premium (cho Short) / discount (cho Long).
- [ ] Sweep diễn ra trong **kill zone** (London / NY AM).
- [ ] Sau sweep có **displacement + MSS** xác nhận đảo chiều.

#### Khi nào nên bỏ qua?
- [ ] Giá đóng nến vượt hẳn mức (break thật) — không reclaim.
- [ ] Sweep ngược Daily Bias mà không có bằng chứng HTF đảo.
- [ ] Sweep giữa range / quanh equilibrium, không có POI.
- [ ] Không có displacement sau sweep — chỉ "lửng lơ" quanh mức.
- [ ] Đã quét quá nhiều pool, giá đã chạy xa — entry thành chase.
- [ ] Ngoài kill zone / ngoài plan session.

### 22.9 Cấu trúc nhận diện trên chart *(v1 §3)*

![[Liquidity-Sweep-Structure.svg]]
*Hình v1: Chuỗi 5 dấu hiệu của sweep hợp lệ — Pool → Spike/wick → Reclaim → Displacement → MSS.*

#### Dấu hiệu chính
1. **Pool liquidity được xác định trước:** một mức có nhiều stop (equal highs/lows, đỉnh/đáy cũ rõ).
2. **Spike xuyên mức:** một cú đẩy nhanh vượt qua mức, thường để lại **wick dài**.
3. **Reclaim:** giá đóng nến trở lại bên trong vùng (về phía của mức vừa quét) — đây là dấu hiệu phân biệt sweep với break.
4. **Displacement ngược:** ngay sau reclaim, một nến/đoạn displacement mạnh đẩy giá hướng ngược lại.
5. **MSS:** displacement đó thường phá cấu trúc nội bộ (Market Structure Shift), xác nhận đảo chiều.

#### Ma trận nhận diện Sweep

| Thành phần | SSL Sweep (→ Long) | BSL Sweep (→ Short) | Cảnh báo / Break thật |
|---|---|---|---|
| **Mức bị quét** | Đáy cũ / equal lows | Đỉnh cũ / equal highs | Mức không rõ / random |
| **Cách xuyên** | Wick dài xuống, đóng lại trên | Wick dài lên, đóng lại dưới | Đóng nến VƯỢT HẲN mức |
| **Reclaim** | Đóng nến trở lại trên mức | Đóng nến trở lại dưới mức | Không reclaim, giữ ngoài |
| **Phản ứng** | Displacement tăng + MSS bullish | Displacement giảm + MSS bearish | Tiếp tục theo hướng phá |
| **Location** | Discount của dealing range | Premium của dealing range | Quanh equilibrium |
| **Bias** | Đồng hướng bias bullish | Đồng hướng bias bearish | Ngược bias |

#### Điều kiện bắt buộc
- [ ] Xác định được pool liquidity cụ thể bị quét (mức giá rõ ràng).
- [ ] Có hành vi reclaim: giá đóng nến trở lại bên trong vùng.
- [ ] Có displacement sau sweep (không chỉ một wick rồi đi ngang).
- [ ] Xác định đáy/đỉnh cú sweep để làm mốc stop loss.

#### Điều kiện tăng xác suất
- [ ] Sweep tại POI HTF đồng hướng bias.
- [ ] Sweep đúng premium/discount.
- [ ] Displacement sau sweep tạo MSS + để lại FVG.
- [ ] Sweep xảy ra trong kill zone.
- [ ] Pool bị quét là external HTF (PDH/PDL, PWH/PWL) → đảo chiều mạnh hơn.
- [ ] Có một pool liquidity rõ ở phía đối diện để làm target.

#### Điều kiện làm setup yếu đi
- Cú quét không có wick rõ / đóng nến vượt hẳn (nghi break thật).
- Không có displacement ngược, giá đi ngang sau sweep.
- Sweep ngược bias hoặc giữa range.
- Đã có chuỗi nhiều sweep liên tiếp, không rõ pool nào còn ý nghĩa.

> [!note] Chú thích v2
> Chuỗi 5 dấu hiệu của v1 = ARMED (pool) → PENETRATED (spike) → REJECTED (reclaim) → REVERSAL CONF. (displacement + MSS) trong máy trạng thái §20. "Điều kiện bắt buộc" của v1 tương ứng nhóm Required ở §22.7, trừ việc v2 thêm yêu cầu **mức ex-ante** và **timer**.

### 22.10 Ví dụ đi xuyên ba tầng (giả định — không phải trade thật)

```text
EURUSD, thứ Ba (giả định). Giờ NY.
D1 (trước 00:00): range D1 1.0760–1.0905 (EQ 1.0833); giá 1.0842 — sát EQ, hơi premium.
   Bias state: BULLISH tier B (HL D1 giữ, BSL tuần trước 1.0905 chưa lấy).
   DOL: PWH 1.0905 (p_null trong ngày thấp — khoảng cách 63 pip vs ADR ~70) → DOL tuần, mục tiêu ngày = PDH 1.0871.
   Invalidation thesis: close D1 dưới 1.0760.
H1 (02:00): Asia range 1.0828–1.0846. H1 bullish FVG 1.0815–1.0824 (POI). SSL ex-ante: Asia low 1.0828 (LSS trung bình),
   PDL 1.0819 (LSS cao: D1 + nằm trong POI). → Kịch bản chính: London quét Asia low, có thể tới PDL trong POI.
M5 (03:10): giá xuống 1.0826 (E2 tại Asia low: close 1.0831) → REJECTED nhưng KHÔNG MSS trong m = 6 nến → STALE.
   03:45: giá xuống 1.0816 (xuyên PDL 3 pip, trong POI), close M5 1.0823 → REJECTED (δ = 0.25·ATR M5 ≈ 1.2 pip).
   04:05: close M5 1.0838 qua swing high M5 (Level 2) bằng nến 1.7·ATR, để lại FVG 1.0827–1.0832 → REVERSAL CONF.
   04:20: retrace vào FVG 1.0831 → ENTRY long. Stop 1.0812 (cực trị 1.0816 + buffer 4 pip). Target 1: Asia high 1.0846; Target 2: PDH 1.0871.
   Ghi: event_code E2@PDL, known_at PDL = 00:00, p_null(T2 trước stop) = (1.0831−1.0812)/(1.0871−1.0812) ≈ 0.32, LSS cao, mss_tf M5 (swing L2), disp_atr 1.7.
```

Điều ví dụ minh họa: (1) sweep đầu tiên (Asia low) **không** đủ điều kiện vì thiếu MSS — đúng tinh thần double sweep của v1 W2; (2) p_null ≈ 0.32 nghĩa là trên random walk lệnh này thắng ~32% với R:R ≈ 2.1 → expectancy ≈ 0; mọi edge phải đến từ việc P thực > 0.32 một cách có hệ thống.


### 22.11 Best Practices *(v1 §7.6)*

> [!success] Best Practices
> 1. **Lên danh sách "pool có thể bị quét" trước phiên** (Asia H/L, PDH/PDL, equal H/L, London H/L) — sweep chỉ có nghĩa tại mức đã đánh dấu trước; cú quét ở mức mình chưa từng đánh dấu = không trade.
> 2. **Ba lớp xác nhận theo thứ tự: reclaim → displacement → MSS.** Thiếu lớp nào dừng ở lớp đó. Vào lệnh khi mới có wick = đặt cược, không phải trade.
> 3. **Luôn check SMT tại thời điểm sweep** (NQ↔ES, EU↔GU/DXY). Có divergence = nâng tier setup; không có = vẫn được trade nhưng size chuẩn, không size lớn.
> 4. **Chấm giờ cho mọi sweep:** trong kill zone/macro = hạng A; ngoài giờ = hạ tier hoặc bỏ. Ghi `sweep_time_window` vào journal.
> 5. **Đọc tốc độ rời hiện trường:** nến ngay sau cú quét phải là displacement; giá lình xình ngoài mức quá 2–3 nến → hủy kịch bản reversal, không "chờ thêm cho chắc".
> 6. **Mặc định sweep có thể phân tầng (double sweep):** đặt stop ngoài POI HTF/mốc SD kế tiếp chứ không sát wick; nếu bị quét tầng hai đúng kế hoạch dự phòng, được phép re-entry MỘT lần với setup đầy đủ — không trung bình giá.
> 7. **Sau 8:30 news spike:** không trade trong spike; chờ 5–15 phút xem pool nào bị lấy và giá accept ở đâu rồi mới áp model.
> 8. **Backtest riêng biến `smt_divergence`, `sweep_depth`, `time_window`** — mục tiêu là tìm ra "chữ ký sweep" thắng nhiều nhất với chính thị trường mình trade (NQ khác EURUSD đáng kể ở độ sâu quét điển hình).

> [!note] Chú thích v2
> Tám best practice của v1 đều tương thích với máy trạng thái v2: (1) ↔ RULE-LS-001; (2) ↔ RULE-LS-003; (3) SMT ↔ HYP-LS-014 (dùng để nâng tier chỉ sau khi đo LR); (4) giờ ↔ HYP-LS-005; (5) "lình xình > 2–3 nến → hủy" ↔ STALE (tham số m); (6) ↔ RULE-LS-004/010; (7) ↔ RULE-LS-006; (8) backtest riêng biến ↔ §26.
---

## 23. Ví dụ & Case studies

### 23.1 Ví dụ chart và sequence mẫu *(v1 §6)*

#### Ví dụ đúng — Quét SSL tại discount → displacement + MSS → Long
![[Liquidity-Sweep-Example-Correct.png]]

**Mô tả:**
HTF bias Bullish, draw on liquidity là BSL phía trên. Giá giảm vào discount và hình thành equal lows (SSL). Một cú spike quét xuống dưới SSL (wick dài), nhưng nến đóng **trở lại trên** mức (reclaim). Ngay sau đó là nến displacement tăng mạnh phá swing high nội bộ (MSS bullish), để lại bullish FVG. Giá retrace về POI (FVG/OB), entry tại đó; stop dưới đáy cú sweep; target là BSL phía trên.

**Vì sao đây là ví dụ tốt:**
- Có reclaim rõ + displacement + MSS, không phải break thật.
- Sweep ở **discount**, đồng hướng Daily Bias bullish.
- Entry SAU sweep tại POI, không phải bắt đáy trên wick.
- Stop nằm ngoài đáy sweep (nơi liquidity vừa bị lấy → ít bị quét lại).
- Target là pool liquidity rõ ràng (BSL).

#### Ví dụ sai / dễ nhầm — Long ngay trên wick, nhầm "break thật" là "sweep"
![[Liquidity-Sweep-Example-Wrong.png]]

**Mô tả lỗi:**
Giá giảm về equal lows. Khi giá xuyên xuống dưới SSL, trader lập tức Long ngay trên wick vì "chắc là sweep, sắp đảo". Nhưng nến **không reclaim** — nó đóng hẳn dưới SSL (acceptance), không có displacement ngược. Đây là **break thật**, giá tiếp tục giảm và quét luôn stop của lệnh Long.

**Bài học:**
- Sweep cần **reclaim + displacement**; chỉ một cú xuyên mức chưa đủ.
- Vào ngay trên wick = đặt cược trước khi có xác nhận; rất dễ trúng break thật hoặc double sweep.
- Phân biệt sweep (đóng lại trong vùng) với break (đóng ngoài, đi tiếp) trước khi vào.

---
#### Sequence mẫu — Long sau SSL Sweep
```text
HTF Bullish Bias
→ HTF Dealing Range, Location = Discount
→ Giá về discount + bullish HTF POI
→ Equal lows / SSL bị quét (wick xuống + reclaim)
→ Displacement tăng phá cấu trúc (MSS) → tạo Bullish FVG
→ Giá retrace về POI (FVG/OB)
→ M5/M1 bullish MSS xác nhận
→ Entry; Stop dưới đáy cú sweep
→ Target: Internal liquidity trước, External BSL chính sau
```

#### Sequence mẫu — Short sau BSL Sweep
```text
HTF Bearish Bias
→ HTF Dealing Range, Location = Premium
→ Giá về premium + bearish HTF POI
→ Equal highs / BSL bị quét (wick lên + reclaim)
→ Displacement giảm phá cấu trúc (MSS) → tạo Bearish FVG
→ Giá retrace về POI (FVG/OB)
→ M5/M1 bearish MSS xác nhận
→ Entry; Stop trên đỉnh cú sweep
→ Target: Internal liquidity trước, External SSL chính sau
```

> [!note]
> Liquidity Sweep là "công tắc bật" cho các model còn lại: [[13-FVG-Fair-Value-Gap|Fair Value Gap]], [[25-OB-Order-Block|Order Block]], [[26-OTE-Optimal-Trade-Entry|Optimal Trade Entry]] đều mạnh hơn nhiều khi xuất hiện NGAY SAU một sweep đúng hướng narrative. Thiếu sweep, các POI dễ bị xuyên thủng.

> [!note] Chú thích v2
> - Hai ảnh PNG là minh họa vẽ tay của v1, không phải dữ liệu thật.
> - "Stop nằm ngoài đáy sweep (nơi liquidity vừa bị lấy → ít bị quét lại)" → xem chú thích ở §22.2 và RULE-LS-004: cực trị sweep là nơi stop mới tập trung (replenishment) — "ít bị quét lại" là **[HYPOTHESIS]**, và W2 của chính v1 cho thấy điều ngược lại khi có pool xếp tầng.
> - "Thiếu sweep, các POI dễ bị xuyên thủng" → **[HYPOTHESIS]** — đây đúng là ô ③ vs ① của ma trận §13.2 (HYP-LS-010).

### 23.2 Case studies mới — tái dựng T0 → T5 (giả định, không phải trade thật)

> [!warning] Đọc trước
> Sáu case dưới đây là **giả định có chủ đích**, dựng để minh họa từng nhánh của cây kết quả và từng lỗi suy luận. Giá là số minh họa; không có ngày thật, không có dữ liệu thật. Mỗi case được viết theo thời gian: tại mỗi Tᵢ chỉ dùng thông tin đã có. Phần "Hindsight" ở cuối chỉ ra điều người xem chart sau này sẽ (sai lầm) cho là hiển nhiên.

#### Case A — EURUSD: Sweep PDL trong POI → R1 (nhánh "đúng sách")

| T | Thông tin có | Trạng thái / quyết định |
|---|---|---|
| T0 (00:00 NY) | D1 BULLISH tier B; DOL ngày = PDH 1.0871; POI H1 bullish FVG 1.0815–1.0824; SSL ex-ante: Asia low 1.0828, PDL 1.0819 | ARMED cả hai mức; kịch bản: London quét Asia low, có thể tới PDL |
| T1 (03:10) | Xuyên Asia low 2 pip, close M5 lại trên (E2) | REJECTED tại Asia low; chờ MSS trong m = 6 |
| T2 (03:40) | Không MSS sau 6 nến | **STALE** — không vào |
| T3 (03:45) | Xuyên PDL 3 pip (trong POI), close M5 1.0823 | REJECTED tại PDL |
| T4 (04:05) | Close qua swing high M5 L2 bằng nến 1.7·ATR, FVG 1.0827–1.0832 | REVERSAL CONF. |
| T5 (04:20 → 10:30) | Retrace FVG 1.0831 → entry; tới Asia high rồi PDH | +2.1R (T2) |

**Bài học:** sweep đầu (Asia low) là *đúng một sự kiện liquidity* nhưng *không phải setup* — máy trạng thái tự loại nó (STALE). **Hindsight:** nhìn lại chart, người ta sẽ nói "rõ ràng Asia low là inducement" — nhưng tại T1 nhãn IDM không biết được; điều biết được là "chưa có MSS".

#### Case B — NQ: Rejection tại PDH rồi re-break → T1 (sweep thành run)

| T | Thông tin có | Trạng thái / quyết định |
|---|---|---|
| T0 (09:30) | D1 BEARISH tier C (vừa có HL D1 mới — bằng chứng mâu thuẫn); PDH 18,420 ex-ante | ARMED; ghi "bias tier C" |
| T1 (09:41) | Xuyên PDH 12 điểm, close M5 18,401 (< L − δ) | REJECTED |
| T2 (09:55) | Close qua swing low M5 bằng nến 1.4·ATR → REVERSAL CONF.; FVG 18,395–18,404 | Entry short 18,402, stop 18,447 |
| T3 (10:20) | Giá quay lên, close M5 18,438 rồi 18,445 (2 close > PDH) | Ghi dòng mới: **rejection failed → ACCEPTED** |
| T4 (10:24) | Stop | −1R |
| T5 (11:30) | Giá chạy tới PWH 18,520 | Run (E7) — nhãn tổng: E2 → T1 → E7 |

**Bài học:** (1) tier C ở D1 là cảnh báo đã có từ T0 — supporting condition yếu; (2) nhãn "sweep" tại T1 hoàn toàn đúng *tại T1*; nó bị bổ sung bằng nhãn mới tại T3, không bị "sửa thành sai". (3) Expectancy của setup được đo trên tất cả các lần như T1–T2, bao gồm cả lần này — không được loại ra như "không phải sweep thật". **Hindsight:** "rõ ràng đó là run, ai lại short trong uptrend" — tại T0 D1 vẫn là bearish tier C.

#### Case C — XAUUSD: Bẫy short ngược một run

| T | Thông tin có | Trạng thái / quyết định |
|---|---|---|
| T0 | D1 BULLISH tier A; H1 đang lấy liên tiếp swing high (L1 accepted lúc 08:10) | RUN chưa xác nhận (mới 1 mức) |
| T1 (09:05) | L2 accepted (2 close trên) | **RUN ACTIVE** (DEF-LS-05 thỏa) |
| T2 (09:40) | Wick qua L3 rồi close M5 dưới L3 (E2) | REJECTED tại L3 — nhưng RULE-LS-005: trong RUN ACTIVE, không trade reversal cho tới RUN ENDED |
| T3 (09:55) | Không MSS ở khung run (HL H1 gần nhất còn nguyên); giá đi ngang | STALE; run vẫn active |
| T4 (10:30) | L3 re-break + acceptance | Run tiếp tục (3 mức) |
| T5 | Giá tới DOL D1 | — |

**Bài học:** rejection ở M5 bên trong một run H1 là sự kiện M5 (R7). Run chỉ kết thúc khi có MSS ngược **ở khung run**, không phải khi có một wick M5. **Hindsight:** không có — đây là case "đứng ngoài đúng".

#### Case D — GBPUSD: EQH không bao giờ bị lấy (E0)

| T | Thông tin có | Trạng thái / quyết định |
|---|---|---|
| T0 | D1 BEARISH tier B; EQH H1 tại 1.2780/1.2782 (tol 0.1 ATR) — "liquidity rõ ràng"; bearish H1 OB 1.2760–1.2772 bên dưới EQH | Kịch bản ICT phổ biến: "giá sẽ lấy EQH rồi giảm" |
| T1 (03:30) | Giá vào OB tới 1.2771, cách EQH 9 pip, rồi giảm | E0 (không chạm) — không có sự kiện liquidity tại EQH |
| T2 (03:50) | MSS M5 bearish bằng displacement từ trong OB | Ô ③ của ma trận (MSS không có sweep tại mức ex-ante) |
| T3 → T5 | Giá giảm tới PDL | — |

**Bài học:** (1) EQH không phải nam châm (LS-Sim-07); (2) trader chỉ chấp nhận setup có sweep sẽ đứng ngoài ở case này — đó là *chi phí cơ hội* của điều kiện sweep, phải được đo cùng lợi ích của nó (HYP-LS-010); (3) "front-run" (E0) là một loại sự kiện có thật, cần mã riêng. **Hindsight:** "smart money không cần lấy EQH vì đã đủ thanh khoản" — câu chuyện được viết *sau* khi biết kết quả.

#### Case E — NQ: Tin 08:30 quét hai phía (E8) → SUSPEND

| T | Thông tin có | Trạng thái |
|---|---|---|
| T0 (08:25) | Lịch tin tier-1 lúc 08:30; ARMED với cả overnight high và low | NEWS SUSPEND từ 08:28 tới 08:45 (RULE-LS-006) |
| T1 (08:30–08:31) | Nến M1 xuyên overnight high 25 điểm rồi overnight low 30 điểm | E8 — không phân loại sweep/run trong cửa sổ |
| T2 (08:45) | Hết SUSPEND; giá nằm giữa; cả hai mức đã bị lấy | Danh sách mức mới: cực trị của spike (known_at 08:45) — đánh dấu "dirty level" (W3) |
| T3 → T5 | Đánh giá lại từ đầu với mức mới | — |

**Bài học:** spike tin không phải sweep theo DEF-LS-04 vì nó xảy ra trong cửa sổ bị loại; wick backtest trong spike không khớp được (v1 W3, LS-Sim-02: fill lý tưởng tạo edge ảo +0.08R ngay cả trên random walk).

#### Case F — GBPUSD: Sweep M5 "external" thực ra là internal H1 (R7)

| T | Thông tin có | Trạng thái |
|---|---|---|
| T0 | D1 BULLISH; H1 trong uptrend; range M5 nhỏ trong pullback H1 | ARMED với range high M5 (BSL của range M5) |
| T1 | Xuyên range high M5, close lại dưới (E2) → REJECTED | Trader gọi đây là "sweep external liquidity" |
| T2 | MSS M5 bearish (swing Level 1) | **Không đạt** Level ≥ 2 → không REVERSAL CONF. theo v0.1 |
| T3 | Giá giảm tới H1 bullish FVG (IRL H1), rồi bật lên | Pullback trong uptrend H1 |
| T4 → T5 | Giá lấy BSL H1 | Run H1 |

**Bài học:** "external" của range M5 là "internal" của range H1 (§9.1). Lấy range tham chiếu từ khung context; MSS phải phá swing có ý nghĩa theo khung setup.

### 23.3 Case studies của v1 — số liệu chưa xác minh *(v1 §18)*

> [!warning] Trạng thái dữ liệu
> Bốn case dưới đây được viết trong phiên trước với timestamp và giá cụ thể. Không có liên kết tới trade log hay backtest note trong vault (`05 - Live Trading Journal/`, `04 - Backtesting/`). Chúng được giữ nguyên văn như **case minh họa giả định — số liệu chưa xác minh**, giống cách Daily Bias v2 xử lý case v1 §17. Không dùng các con số R trong đó làm bằng chứng thống kê.

> [!info] Bổ sung, không trùng với các case đã có
> Mục "Ví dụ chart" (§6) đã có 2 sequence mẫu (Long sau SSL / Short sau BSL) mang tính minh họa kỹ thuật thuần túy, và War Stories (W0-W6) là các tình huống tâm lý/vi cấu trúc. Bốn case dưới đây là NHẬT KÝ TRADE ĐẦY ĐỦ với timestamp, số liệu R cụ thể — dùng XAUUSD, NQ, EURUSD, ETHUSD để không trùng bộ instrument đã dùng trong case study của MSS (EURUSD-win/NQ-lose/XAUUSD-skip/BTCUSD-other) và Inducement (GBPUSD-win/ES-lose/XAUUSD-skip/BTCUSD-other) — ở đây đảo vai trò: XAUUSD đóng vai win, NQ đóng vai lose, EURUSD đóng vai skip, ETHUSD (thay vì BTCUSD, tránh trùng hình dạng multi-poke equal-highs đã dùng ở Inducement Case Study D) đóng vai "tài sản khác" với kịch bản single-poke hoàn toàn khác.

#### Case Study A — XAUUSD, Short thắng đúng sách sau BSL Sweep tại premium

**Bối cảnh HTF:** XAUUSD, thứ Ba, Daily Bias Bearish (giá vừa fail tại D1 bearish OB 2 ngày trước, giữ dưới D1 midline). Dealing range H4: 2,355-2,410, giá hiện tại 2,398 (premium rõ).

**Setup:** H1 bearish OB tại 2,405-2,412 (POI thật). BSL target là đỉnh tuần trước (PWH) tại 2,415.

**Diễn biến & execution:**
- 08:40 NY: giá quét lên 2,417 (qua PWH — external sweep, không phải IDM vì đây là pool chính ở cực dealing range), đóng nến M15 trở lại 2,409 — reclaim rõ, thân nến reclaim chiếm ~65% range nến sweep (đạt chuẩn W1).
- 08:55: M5 phá xuống qua higher-low nội bộ 2,403 bằng nến thân lớn (~2.2x ATR(14) M5), để lại FVG 2,398-2,404 — MSS bearish xác nhận, displacement đạt chuẩn.
- 09:08: giá retrace lên 2,401 (trong FVG), Short khớp.
- Stop đặt tại 2,419 (trên sweep high, buffer 2 USD).
- Target 1: internal 2,370. Target 2: SSL sâu hơn 2,348.
- 12:30: chạm T1, dời stop về entry. 15:45: chạm T2, đóng lệnh.

**Kết quả bằng số:** Rủi ro 18 USD/oz. Lợi nhuận 53 USD/oz = **+2.94R**.

**Bài học chỉ rút ra được nhờ case này:** đây là ví dụ sách giáo khoa của external/structural sweep (không phải IDM) — pool bị quét (PWH) nằm ĐÚNG tại cực dealing range, không phải trung gian, và MSS xuất hiện ngay sau (khác hẳn sweep tại IDM, nơi giá tiếp tục đi mà không đảo ngay). Việc phân loại đúng vai trò của pool bị quét (theo bảng ở mục 13.4) là điều quyết định trước khi coi đây là entry hợp lệ.

![[Liquidity-Sweep-Case-Study.svg|720]]
*Diễn biến Case Study A: XAUUSD Short — BSL sweep PWH 08:40 → reclaim mạnh → MSS + FVG → entry 2,401 → target 2,348, +2.94R.*

#### Case Study B — NQ, sweep "đẹp như sách" nhưng THUA vì bỏ qua chữ ký liquidation-style trong phiên có OPEX

**Bối cảnh HTF:** NQ, thứ Sáu OPEX (options expiration — thanh khoản và gamma exposure dealer cao bất thường), Daily Bias Bullish, giá test lại H1 bullish OB 18,240-18,270.

**Setup:** phía dưới OB, SSL tại đáy phiên Á 18,225. Trader áp dụng đúng toàn bộ checklist: chờ sweep + reclaim + displacement + MSS trước khi vào.

**Diễn biến & execution:**
- 09:50 NY: giá quét xuống 18,218 (qua SSL 18,225), đóng nến M5 trở lại 18,232 — reclaim đạt chuẩn (~58% thân nến).
- 09:58: M5 phá lên qua lower-high nội bộ 18,238 bằng nến thân lớn, để lại FVG 18,235-18,248 — MSS bullish xác nhận đầy đủ theo mọi tiêu chí đã học.
- 10:05: giá retrace vào FVG tại 18,240, Long khớp.
- Stop đặt tại 18,212 (dưới sweep low).
- 10:30: giá tăng lên 18,260 (gần chạm T1 18,265)... rồi đảo ngột ngạt, giảm thẳng xuyên qua entry, xuyên qua stop, chạm 18,205 trong vòng 12 phút — đặc trưng "giật cục bất thường quanh gamma wall" đã nêu ở mục 10.7 (bảng so sánh 3 thị trường): đúng ngày OPEX, dealer hedging flow tạo một cú đảo ngược mạnh hơn bất kỳ displacement thông thường, không liên quan gì tới cấu trúc IDM/POI đã phân tích.

**Kết quả bằng số:** Rủi ro 20 point × 20 USD = 400 USD/lot. Kết quả: **-1R**.

**Bài học chỉ rút ra được nhờ case này:** setup thỏa mọi điều kiện kỹ thuật chuẩn (sweep, reclaim, displacement, MSS, FVG entry) vẫn có thể thua vì một biến số nằm NGOÀI khung phân tích liquidity/structure thuần túy — dealer hedging flow quanh OPEX trên index futures là một lớp rủi ro riêng (đã nêu ở mục 10.7) cần được cộng thêm vào checklist cho các ngày OPEX, không chỉ dựa vào chất lượng sweep/MSS.

#### Case Study C — EURUSD, đứng ngoài đúng vì "sweep" chỉ là break thật (acceptance), không phải rejection

**Bối cảnh HTF:** EURUSD, thứ Tư, Daily Bias Bullish, giá đang test PDL 1.0845 trong London KZ, kỳ vọng SSL sweep rồi đảo lên theo bias.

**Diễn biến & execution (quyết định KHÔNG vào):**
- 04:15 NY: giá xuyên xuống 1.0838, đóng nến M15 tại 1.0836 — giá đóng NGOÀI mức PDL, không phải reclaim bên trong (đây chính là break thật/acceptance, đã phân biệt ở mục 12.4: "Sweep thành công vs Sweep thất bại = Break").
- 04:30-05:00: giá tiếp tục dao động dưới PDL, không có dấu hiệu quay lại — thân nến các nến tiếp theo không cho thấy đảo, khối lượng bán vẫn chiếm ưu thế.
- Theo đúng checklist mục 27: "đóng nến ngoài mức = break, không phải sweep — không trade theo kịch bản sweep", trader giữ kỷ luật, KHÔNG cố gọi đây là "sweep sâu, sắp đảo" dù bias H4 vẫn là bullish.
- 08:20: giá tiếp tục giảm xuống 1.0790, xác nhận đây là một breakdown thật, không phải sweep — nếu đã Long "đón đầu" một cú sweep tưởng tượng tại 1.0838, lệnh sẽ lỗ nặng theo toàn bộ nhịp giảm sau đó.
- **Quyết định: đứng ngoài, ghi `outcome: break_not_sweep, action: skip` vào journal.**

**Kết quả bằng số:** 0R (không giao dịch) — tránh một lệnh Long ngược một breakdown thật đang hình thành.

**Bài học chỉ rút ra được nhờ case này:** ranh giới sweep vs break (mục 12.4) không phải lý thuyết suông — đây là ví dụ thực chiến nơi việc tuân thủ nghiêm ngặt định nghĩa "đóng nến bên trong = reclaim, đóng nến ngoài = break" đã bảo vệ trader khỏi một lệnh thua nặng, dù bias HTF vẫn đúng hướng dự kiến (bias đúng không có nghĩa mọi kịch bản dựa trên bias đó đều đúng thời điểm).

#### Case Study D — ETHUSD, Long sau SSL Sweep đơn-lệnh (single-poke) xác nhận KHÔNG phải liquidation cascade

**Bối cảnh HTF:** ETHUSD, chiều thứ Ba (thanh khoản bình thường trong tuần, không phải cuối tuần — chủ đích chọn khung giờ này để tương phản với Case Study D của [[15-Inducement]], nơi bối cảnh là tối thứ Bảy thanh khoản mỏng), Daily Bias Bullish sau khi giá giữ vững trên D1 bullish OB 2 ngày liên tiếp. Giá quanh 3,180.

**Setup:** khác với kịch bản multi-poke equal-highs đã dùng ở Inducement Case Study D, đây là một pool ĐƠN LẺ (single old low, không phải equal lows dày) tại SSL 3,142 — đáy phiên Á duy nhất, chỉ chạm 1 lần trước đó. H1 bullish OB nằm ngay trên pool này tại 3,145-3,158.

**Diễn biến & execution (áp dụng EC5 dù đây không phải cuối tuần — funding rate vẫn cần kiểm tra bất kỳ khi nào sweep có vẻ "quá sâu"):**
- 14:20 UTC: giá thọc xuống 3,138 — SÂU HƠN bình thường so với biên độ dao động trung bình của ETHUSD phiên đó (đo bằng ATR(14) H1: cú thọc này gấp 2.3x ATR, một dấu hiệu CẦN kiểm tra theo EC5 dù không phải cuối tuần).
- Trader kiểm tra funding rate (đang dương nhẹ 0.02%, hoàn toàn bình thường) và OI (đi ngang, không tích lũy đòn bẩy) — xác nhận đây KHÔNG phải liquidation cascade, độ sâu bất thường chỉ do thanh khoản ETHUSD tại đúng phút đó mỏng hơn trung bình (không phải đòn bẩy quá tải).
- Vì đây là single-poke (không phải multi-poke như Inducement Case Study D), điều kiện vào khác hẳn: không cần chờ nhịp "rời pool" qua nhiều lần thọc — chỉ cần MỘT nến reclaim đủ chuẩn (thân ≥ 50% range nến sweep) là đủ, đúng theo rule W1 (không áp dụng rule multi-poke của mục 13.4 vì đây không phải equal-highs/lows dày).
- 14:21: nến reclaim đóng tại 3,159, thân nến chiếm 71% range nến sweep — đạt chuẩn W1 rõ ràng, không doji.
- 14:35: M15 phá lên qua lower-high nội bộ 3,163 bằng displacement (1.6x ATR M15), để lại FVG 3,155-3,161 — MSS bullish xác nhận.
- 14:50: giá retrace về 3,158 (trong FVG), Long khớp.
- Stop dưới sweep low 3,138, cộng buffer, đặt tại 3,131.
- Target: internal 3,225, sau đó BSL sâu hơn 3,268.
- 18:40 UTC: chạm T1, dời stop về entry. 22:15 UTC: chạm T2, đóng lệnh.

**Kết quả bằng số:** Rủi ro 27 USD/ETH. Lợi nhuận 110 USD/ETH = **+4.07R**.

**Bài học chỉ rút ra được nhờ case này (khác hẳn bài học của Inducement Case Study D):** không phải mọi sweep độ sâu bất thường trên crypto đều là cascade, và không phải mọi pool đáng ngờ đều là equal-highs/lows dày cần multi-poke — với pool ĐƠN LẺ, một nến reclaim đạt chuẩn là đủ điều kiện, miễn là đã loại trừ cascade bằng funding/OI. Bài học ở đây là **quy trình kiểm tra EC5 áp dụng cho MỌI độ sâu sweep bất thường, không chỉ giới hạn ở cuối tuần** — khác với Inducement Case Study D vốn tập trung vào rủi ro IDM giả do một lệnh lớn đơn lẻ tạo hình dạng equal-highs giả.

---

> [!note] Chú thích v2 cho case v1
> - Case A (XAUUSD) — tương đương Case A mới; lưu ý ngưỡng "65% thân nến reclaim", "2.2× ATR" là HEURISTIC.
> - Case B (NQ, OPEX) — giải thích "dealer hedging flow" là **[INTERPRETATION]**; giả thuyết OPEX ghi ở HYP-LS-017. Một case thua không đủ để kết luận về OPEX — cần đếm.
> - Case C (EURUSD, break not sweep) — đúng tinh thần v2: acceptance (E4) → không trade reversal.
> - Case D (ETHUSD) — quy trình kiểm tra funding/OI là bổ sung hợp lý cho crypto; ngưỡng "2.3× ATR" và "71% thân nến" là HEURISTIC.

### 23.4 Tình huống thực chiến — War Stories *(v1)*

> [!info] Ghi chú di chuyển
> W0 của v1 đã chuyển lên §4.5 (kèm rà soát). W1 đã chuyển lên §11.4. W2–W6 giữ nguyên dưới đây.

> [!info] Vì sao có mục này
> Các tình huống dưới đây KHÔNG nằm trong định nghĩa chuẩn của sweep. Chúng là những cách mà một cú sweep "đúng sách giáo khoa" vẫn lấy tiền của người đã thuộc bài — chỉ lộ ra sau nhiều mẫu backtest và giờ bay live. Mỗi tình huống kết thúc bằng một rule đo được để đưa vào journal.

#### W2. Double sweep phân tầng — bản đồ pool phải vẽ trước, không vẽ khi đang chảy máu

![[Liquidity-Sweep-War-Double-Sweep-Tiers.svg|720]]
*Sơ đồ: Asia Low là pool mồi, PDL trùng POI HTF là pool chính; stop sát wick sweep #1 chính là thanh khoản cho sweep #2.*

**Sách giáo khoa nói:** double sweep là rủi ro, đặt stop rộng hơn (đã nêu ở mục 12.4).

**Thực tế phát hiện:** double sweep KHÔNG ngẫu nhiên — nó có cấu trúc dự đoán được. Khi có **hai pool xếp tầng gần nhau** (Asia Low nông + PDL sâu hơn vài chục điểm, và PDL trùng H1 FVG), kịch bản xác suất cao nhất không phải "đảo tại Asia Low" mà là: quét Asia Low → hút một lớp trader Long sớm → dùng chính stop của họ làm nhiên liệu chặng hai xuống PDL → đảo thật tại POI. Tức là **cú sweep tầng một tồn tại để tạo ra thanh khoản cho tầng hai.** Nhìn được điều này trước phiên thì sweep #1 không còn là bẫy — nó là *lời hẹn* cho setup tại PDL.

**Rule đo được:**
- Trước phiên, xếp tầng pool: Asia H/L → London H/L → PDH/PDL → PWH/PWL. Nếu pool nông có pool sâu hơn trùng POI HTF ngay dưới/trên nó → **mặc định kịch bản phân tầng**, không trade tầng nông (hoặc size ½).
- Stop luôn ngoài **POI HTF / mốc SD kế tiếp**, không sát wick.
- Bị quét đúng kịch bản dự phòng → được re-entry **một lần** với sequence đầy đủ tại pool sâu. Không có lần ba.
- Journal: `swept_pool_tier`, `re_entry_taken`.

#### W3. Sweep trong news spike — wick backtest không phải giá khớp thật

![[Liquidity-Sweep-War-News-Spike-Fill.svg|720]]
*Sơ đồ: fill trong backtest tại đáy wick vs fill thực tế sau spread giãn — phần chênh là "phantom R" làm expectancy ảo.*

**Sách giáo khoa nói:** sweep quanh 8:30 là manipulation kinh điển, đọc pool bị lấy sau tin.

**Thực tế chỉ thấy khi so backtest với live:** trên chart lịch sử, cú quét NFP/CPI trông giống mọi sweep khác — wick đẹp, reclaim đẹp. Nhưng tại thời điểm đó **spread giãn 3–10 lần, quote đóng băng, requote liên tục**. Lệnh limit trong wick có thể không bao giờ khớp; lệnh market khớp cách đáy wick hàng chục điểm; stop có thể trượt qua mức đặt. Hệ quả nguy hiểm nhất không nằm ở một lệnh thua — nó nằm ở **backtest**: nếu sample chứa các entry "khớp tại đáy wick tin", expectancy của cả model bị thổi phồng bằng những R không tồn tại. Đây là một dạng curve-fitting mà người chỉ backtest không bao giờ tự phát hiện.

**Rule đo được:**
- Không trade trong spike; chờ 5–15 phút, đọc pool bị lấy và vùng acceptance rồi mới áp model.
- Trong backtest: mọi setup có entry rơi vào ±2 phút quanh high-impact news → gắn `news_window: true` và **thống kê tách riêng**. Nếu edge của model biến mất khi loại nhóm này → edge không có thật.
- Swing tạo bởi spike tin là mức "bẩn": stop sau nó cần buffer rộng hơn, và không dùng nó làm reference swing cho MSS về sau.

#### W4. Cùng một "PDL" nhưng hai thị trường nhìn hai mức khác nhau (data feed)

**Tình huống:** bạn đánh dấu PDL trên chart CFD (NAS100 của broker) và chờ sweep. Giá futures NQ đã quét PDL *của futures* và đảo — nhưng trên chart CFD của bạn, wick "chưa chạm mức". Hoặc ngược lại: CFD wick chạm do spread markup, futures không hề chạm. Với FX cũng vậy: đáy của broker A khác broker B vài pip ở các thời điểm thanh khoản mỏng.

**Bản chất:** pool liquidity thật nằm ở nơi **dòng lệnh tập trung** — với chỉ số là futures (CME), với FX là interbank. Chart CFD là bản chiếu có sai số. Sweep "gần chạm mà không chạm" trên chart của bạn có thể đã hoàn thành trên thị trường gốc.

**Rule đo được:**
- Với NQ/NAS100: **đánh dấu level trên chart futures** (NQ, kèm cả ETH/RTH rõ ràng), thực thi trên nền tảng nào cũng được nhưng bản đồ phải là futures.
- Chấp nhận "sweep hụt vài điểm" như một sweep hợp lệ **nếu** thị trường gốc đã quét và mọi lớp xác nhận (reclaim + displacement + SMT) đều có mặt.
- Backtest và live phải cùng một data feed — nếu không, thống kê sweep depth vô nghĩa.

#### W5. Sweep đảo quá nhanh trong macro window — lỡ tàu là một kết quả tốt

**Tình huống:** sweep xảy ra trong macro (~9:50–10:10), reclaim và displacement hoàn thành trong 2–3 nến M1, giá rời đi không retrace. Bạn không kịp vào. Phản xạ sai phổ biến nhất: **market order đuổi theo** ở giá đã chạy 1R — biến một setup A+ (của người khác) thành một lệnh C- (của mình), stop xa, R:R nát.

**Bản chất:** tốc độ đảo là *bằng chứng chất lượng* của sweep — nhưng chất lượng của sweep không chuyển thành chất lượng của entry khi giá đã đi. Trong ICT 2022, entry tồn tại ở FVG của displacement leg; **không có retrace = không có entry = không có lệnh.** Đó là kết quả trung tính, không phải thua.

**Rule đo được:**
- Cấm market order sau khi displacement đã chạy quá mức 50% của leg (không còn OTE).
- Ghi vào journal như một `missed_valid_setup` — số này tăng nghĩa là model đang hoạt động và mình đọc đúng; nó là dữ liệu tốt, không phải nỗi đau. Nếu muốn xử lý có hệ thống: nghiên cứu riêng playbook re-delivery (giá quay lại FVG trong macro kế tiếp) thay vì chase.

#### W6. Sweep tại vùng rollover/DST — pool "mới" hình thành do lệch múi giờ, không phải liquidity thật

**Tình huống:** vào 1-2 tuần giao thời DST (tháng 3, tháng 11 ở US/UK không đổi cùng ngày), hoặc quanh giờ rollover hợp đồng futures (NQ/ES chuyển hợp đồng quý), một "đáy/đỉnh mới" xuất hiện đúng tại điểm nối giữa phiên cũ và phiên mới — trông giống một pool liquidity mới hình thành, nhưng thực chất là artifact của việc lệch giờ hoặc gián đoạn dữ liệu giữa 2 hợp đồng.

**Bản chất:** rollover contract (ví dụ NQZ25 → NQH26) có thể tạo một gap giá nhỏ giữa giá đóng hợp đồng cũ và giá mở hợp đồng mới do chênh lệch cost-of-carry — gap này không phản ánh lệnh thật bị kích hoạt, chỉ là chênh lệch định giá kỹ thuật giữa hai hợp đồng. Tương tự, trong tuần DST, kill zone "London Open" theo đồng hồ quen thuộc của trader có thể lệch thật 1 giờ so với London Open theo giờ UTC, khiến một swing hình thành "ngoài kill zone thật" bị hiểu nhầm là sweep trong kill zone.

**Rule đo được:**
- Trong 1-2 tuần trước/sau ngày rollover contract chính (được lịch sàn công bố trước), không dùng swing hình thành đúng tại thời điểm rollover làm pool liquidity chính — đối chiếu với chart continuous đã điều chỉnh (back-adjusted) để loại artifact gap.
- Trong 1-2 tuần giao thời DST, verify giờ NY/London thật bằng đồng hồ thế giới, không tin nhãn giờ mặc định trên platform.
- Journal field: `rollover_window: true/false`, `dst_transition_week: true/false` — loại các mẫu này ra khỏi thống kê win rate theo kill zone để tránh làm sai lệch dữ liệu.

> [!success] Cập nhật tổng kết War Stories
> W6 bổ sung một biến ẩn thứ sáu vào danh sách ở cuối mục: **artifact lịch/hợp đồng** (rollover, DST) có thể tạo hình dạng giống sweep/pool mới nhưng không phản ánh order flow thật — luôn đối chiếu lịch rollover và lịch DST trước khi tin một swing mới hình thành tại các thời điểm nhạy cảm này.

> [!success] Tổng kết mục War Stories
> Điểm chung của cả 6 tình huống: **sweep không thất bại vì định nghĩa sai, mà vì thiếu một biến ẩn** — chất lượng thân nến reclaim (W1), cấu trúc tầng của pool (W2), microstructure lúc có tin (W3), sai lệch data feed (W4), tốc độ đảo (W5), và artifact lịch/hợp đồng (W6). Tất cả đều đo được. Đưa chúng vào frontmatter journal (`reclaim_body_quality`, `swept_pool_tier`, `news_window`, `missed_valid_setup`) để chính dữ liệu của mình phân xử, đúng tinh thần `04 - Backtesting/`.

> [!note] Chú thích v2 cho W2–W6
> - **W2 (double sweep phân tầng):** phù hợp với vòng đời liquidity (§8.2 — tiêu thụ một phần; stop mới ngoài cực trị sweep #1 trở thành nhiên liệu cho sweep #2). "Không ngẫu nhiên — có cấu trúc dự đoán được" là **[HYPOTHESIS]** HYP-LS-015. Quy tắc "re-entry một lần" → RULE-LS-010.
> - **W3 (news spike):** được định lượng bởi LS-Sim-02 (fill lý tưởng → +0.08R ảo trên random walk). Rule `news_window` giữ nguyên.
> - **W4 (data feed):** quy tắc "bản đồ là futures" giữ nguyên; bổ sung: known_at của mức phải theo feed dùng để backtest.
> - **W5 (lỡ tàu):** khớp với tham số m' (cửa sổ entry) và quy tắc "không chase".
> - **W6 (rollover/DST):** → cổng G5 của LSS.

---

## 24. Counterexamples & Edge cases

### 24.1 Khi nào quy tắc tạo tín hiệu sai — danh sách bắt buộc của project

| # | Counterexample | Quy tắc nào bị đánh lừa | Vì sao xảy ra | Nhận diện sớm (ex-ante) | Xử lý |
|---|---|---|---|---|---|
| CX1 | **Sweep không đảo chiều** (R2/R3) | "Sweep → tìm reversal" | Không có dòng lệnh mới ngược chiều; trend HTF | Bias HTF cùng hướng xuyên; mức LSS thấp | Bắt buộc MSS + disp (RULE-LS-003) |
| CX2 | **MSS không có displacement** | "MSS = đổi hướng" | Trôi chậm qua swing; thanh khoản mỏng | Body/ATR thấp, nhiều nến chồng | Yêu cầu disp_atr ≥ ngưỡng; ghi riêng nhóm MSS-trôi |
| CX3 | **Displacement không tiếp diễn** | "Displacement = intent" | Một đợt lệnh lớn đơn lẻ, impact tạm thời (LS-Sim-03 A) | Displacement trong giờ thanh khoản mỏng; không có lý do HTF | Entry chỉ tại retrace; stop theo cấu trúc |
| CX4 | **FVG được chạm mà không phản ứng** | "FVG là PD array giá phải tôn trọng" | FVG chỉ là vị trí; trên random walk giá chạm vùng gần thường xuyên | FVG ngược hướng HTF; FVG nhỏ | Quy tắc chọn FVG cố định; invalidation khi close qua FVG |
| CX5 | **Xác định sai DOL** | "Sweep phía ngược DOL → đi về DOL" | DOL chọn sau khi thấy giá; bỏ qua pool hai phía | Không có p_null, không có invalidation | Quy trình DOL hai phía §18.2 |
| CX6 | **Internal bị nhầm là external** | "Sweep external = reversal lớn" | Range tham chiếu chọn ở khung thấp | Range từ khung context D1 | RULE-LS-009 |
| CX7 | **LTF reversal ngược HTF trend** | "M5 sweep + MSS = setup" | Pullback trong trend HTF | Kiểm tra trạng thái run H1/D1 | RULE-LS-005; R7 |
| CX8 | **Break cấu trúc giả** | "Close qua swing = BOS/MSS" | Swing vi mô; nến tin | Level swing; cửa sổ tin | Level ≥ 2; NEWS SUSPEND |
| CX9 | **Nhiều pool cạnh tranh** | "Giá sẽ lấy pool X" | Cluster pool sát nhau; không rõ pool chính | Nhiều mức trong < 0.5 ATR | Coi cluster là một vùng; đợi phân xử ở cực của cluster |
| CX10 | **E0 — giá đảo trước mức** | "Phải có sweep mới có setup" | Front-run; lệnh limit lớn ngay trước mức | Mức "quá rõ" (EQH) + POI trước mức | Ghi E0; đo chi phí cơ hội (Case D) |
| CX11 | **E5 — gap qua mức** | Mọi rule đo độ sâu/wick | Không có giao dịch tại mức | Open phiên mới, cuối tuần | Không áp rule sweep; mức "dirty" |
| CX12 | **Nhãn đổi theo khung** | "Đóng nến trong = sweep" | Độ phân giải (LS-Sim-01B) | — | Phân loại theo khung của mức; ghi cả hai |
| CX13 | **Run gãy ngay sau xác nhận** | "Run active → chỉ trade theo run" | p_null của việc mất HL tăng khi run đi xa | Opposing liquidity gần; ES cao | Dừng tìm setup cùng chiều khi ES ≥ 3 |
| CX14 | **Thanh lý dây chuyền giả dạng sweep chất lượng** | "Sweep sâu + reclaim mạnh = đẹp" | Cascade cơ học (crypto) | Funding/OI cực đoan | v1 EC5 |

> [!important] Một framework không giải thích được thất bại của nó là chưa hoàn chỉnh
> Mỗi dòng trên tương ứng một **nhánh** của máy trạng thái hoặc một **cổng** của LSS. Khi một trade thua, journal phải trả lời được: *thua ở nhánh nào, và thông tin để tránh nó có tồn tại tại thời điểm quyết định hay không?* Nếu không tồn tại → đó là thua hợp lệ (kết quả của xác suất), không phải lỗi.

### 24.2 Edge cases thực chiến *(v1 §17)*

![[Liquidity-Sweep-Edge-Cases.svg|720]]
*EC5 minh họa: độ sâu sweep bất thường trên BTCUSD có thể là liquidation cascade giả dạng sweep chất lượng cao — luôn kiểm tra funding rate/OI trước khi tin tưởng.*

#### EC1. Sweep trên chart CFD hụt vài điểm so với sweep trên futures gốc (đã có nền tảng ở W4, mở rộng thêm biến thể ngược)

**Tình huống:** biến thể ngược của W4 — chart CFD của bạn CHẠM và reclaim rõ ràng tại một mức, nhưng trên futures gốc (NQ), giá chỉ chạm hụt vài điểm rồi đảo, chưa thực sự "sweep" theo định nghĩa chuẩn (chưa xuyên qua pool thật).
**Vì sao bẫy:** trên chart CFD, hình dạng trông "hoàn hảo" hơn thực tế — dễ tự tin thái quá vào một setup mà thị trường gốc chưa hề xác nhận.
**Cách nhận diện sớm:** khi setup dựa vào một mức PDH/PDL/Asia H-L quan trọng, luôn mở song song chart futures gốc trước khi vào lệnh.
**Cách xử lý:** ưu tiên futures gốc làm bản đồ quyết định; nếu hai chart mâu thuẫn, hạ tier setup xuống hoặc bỏ qua.

#### EC2. Sweep ngay trước/sau rollover contract quý — độ sâu sweep bị bóp méo bởi cost-of-carry gap

**Đã có nền tảng ở W6** — trọng tâm bổ sung ở đây: không chỉ vị trí pool bị lệch, mà ĐỘ SÂU của cú sweep (dùng để đánh giá "chữ ký" chất lượng theo mục 10.6) cũng bị bóp méo trong tuần rollover, khiến các phép đo tốc độ/độ sâu chuẩn không còn đáng tin cậy trong giai đoạn này — loại các mẫu tuần rollover khỏi thống kê `sweep_depth` và `sweep_speed`.

#### EC3. Sweep trong nến gap thứ Hai — pool "cuối tuần" chưa từng được test bởi thanh khoản thật trong giờ giao dịch

**Tình huống:** giá gap qua một PDL/PWL vào phút mở phiên thứ Hai (đặc biệt sau một sự kiện cuối tuần: tin địa chính trị, on-chain event với crypto), "sweep" luôn ngay pool đó trong nến gap đầu tiên.
**Vì sao bẫy:** hình dạng giống sweep chuẩn (xuyên qua rồi có thể reclaim), nhưng gap nghĩa là không hề có dòng lệnh liên tục "chảy qua" mức đó — không có ai bị stop hunt theo đúng cơ chế W0 mô tả (thanh khoản không được "thu hoạch" tuần tự, mà bị nhảy qua).
**Cách nhận diện sớm:** kiểm tra biểu đồ có khoảng trống giá (gap) giữa nến đóng thứ Sáu và nến mở thứ Hai/thanh khoản đầu tiên không.
**Cách xử lý:** không áp dụng các rule đo lường "chữ ký sweep" (10.6) cho sweep hình thành từ gap; chờ ít nhất 2-3 nến ổn định đầu phiên trước khi đọc lại narrative.

#### EC4. Sweep tại NFP/CPI/FOMC — mở rộng thêm biến thể "reclaim giả kéo dài" khác W1/W3

**Tình huống:** khác với W1 (reclaim doji thường) và W3 (fill giả trong wick), có biến thể thứ ba: nến tin tạo sweep + reclaim RÕ RÀNG (thân lớn, không doji) — nhưng 15-20 phút sau, một nến thứ hai (thường là nến phản ứng phái sinh/thanh khoản tổ chức vào muộn) quét NGƯỢC LẠI qua chính vùng đó theo hướng khác hoàn toàn.
**Vì sao bẫy được cả trader đã biết W1/W3:** nến đầu tiên thỏa mọi điều kiện "sweep hợp lệ" cả về hình dạng lẫn thời gian (không phải doji, không phải chờ trong lúc spike) — chỉ lộ ra là bẫy khi nến thứ hai xuất hiện.
**Cách nhận diện sớm:** trong 20-30 phút đầu sau tin lớn, luôn coi mọi "MSS xác nhận" là tạm thời (provisional) — không tăng size hay dời stop mạnh tay cho tới khi qua mốc 30 phút.
**Cách xử lý:** giữ size nhỏ hơn chuẩn trong 30 phút đầu sau tin lớn dù setup đã "xác nhận đầy đủ"; chỉ tăng về size chuẩn sau khi giá không có nhịp đảo ngược nào trong khung 30 phút.

#### EC5. Sweep trên BTCUSD cuối tuần bị khuếch đại bởi liquidation cascade — độ sâu sweep không phản ánh thanh khoản tự nguyện

**Tình huống:** trên BTCUSD/ETHUSD, một sweep có độ sâu bất thường lớn (vượt xa "chữ ký" chuẩn ở mục 10.6) xảy ra khi thị trường có đòn bẩy cao và giá vừa chạm một mức thanh lý margin hàng loạt (liquidation cascade) — không phải vì có một bên "gom hàng" lớn theo đúng nghĩa W0 mô tả, mà vì lệnh thanh lý tự động kích hoạt dây chuyền.
**Vì sao bẫy:** độ sâu sweep lớn thường được đọc là "dấu hiệu smart money gom mạnh" (theo 10.6) — nhưng trong liquidation cascade, đó chỉ là hiệu ứng cơ học của đòn bẩy, không phản ánh ý định thật của bên nào.
**Cách nhận diện sớm:** kiểm tra open interest và funding rate trước cú sweep nếu có dữ liệu — funding rate cực đoan (dương hoặc âm mạnh) là dấu hiệu cảnh báo cascade sắp xảy ra.
**Cách xử lý:** hạ độ tin tưởng vào "chữ ký chất lượng" của sweep khi biết trước funding rate/OI đang ở mức cực đoan; ưu tiên chờ thêm xác nhận displacement THẬT (không phải chỉ độ sâu wick) trước khi vào.

#### EC6. Sweep xảy ra đồng thời trên HTF và LTF nhưng theo HAI HƯỚNG NGƯỢC NHAU (fractal conflict)

**Tình huống:** H1 vừa sweep BSL (gợi ý bias giảm sắp tới), nhưng đồng thời trên M5, giá cũng vừa sweep một SSL nhỏ nội bộ (gợi ý một nhịp tăng ngắn hạn) — hai "sweep" hợp lệ về kỹ thuật nhưng ngụ ý hai hướng đối lập ở hai khung.
**Vì sao bẫy:** trader chỉ nhìn một khung tại một thời điểm dễ hành động theo tín hiệu của khung đang xem, bỏ sót mâu thuẫn từ khung khác.
**Cách nhận diện sớm:** luôn kiểm tra khung liền kề trên/dưới trước khi hành động theo một sweep — nếu có mâu thuẫn hướng rõ ràng, đó là dấu hiệu của một cấu trúc phức tạp hơn (có thể là distribution/re-accumulation), không phải sweep đơn giản.
**Cách xử lý:** khi có fractal conflict, ưu tiên hướng của khung cao hơn cho bias tổng thể, nhưng giảm size hoặc đứng ngoài cho tới khi khung thấp "đồng thuận" (không còn sweep ngược hướng) trong ít nhất 2-3 nến liên tiếp.

#### EC7. Partial fill khi limit order đặt ngay tại vùng sweep — thuật toán front-run khiến giá không bao giờ chạm đủ sâu

**Tình huống:** đã xác nhận sweep + reclaim + displacement đầy đủ, đặt limit order chờ retrace vào FVG của displacement leg — nhưng giá chỉ chạm rìa xa của FVG (hoặc chạm thiếu 1-2 tick) rồi chạy tiếp, limit không khớp hoặc chỉ khớp một phần nhỏ.
**Vì sao bẫy:** sau khi đã "làm đúng mọi bước" xác nhận sweep, trader dễ chủ quan nghĩ phần khó nhất đã qua, quên rằng chính bước thực thi cuối cùng (limit fill) vẫn có rủi ro riêng, đặc biệt khi FVG mỏng hoặc trong kill zone nhiều thanh khoản cạnh tranh.
**Cách nhận diện sớm:** không thể biết trước chắc chắn, nhưng rủi ro cao hơn khi FVG có độ rộng dưới mức trung bình (ví dụ dưới 5-8 tick trên NQ) và đang trong giờ kill zone đông đúc.
**Cách xử lý:** đặt limit tại rìa GẦN của FVG (gần giá hiện tại hơn) thay vì rìa xa/giữa, đổi lấy tỷ lệ khớp cao hơn với entry hơi kém hơn một chút.

> [!note] Chú thích v2
> Các EC của v1 đều là **biến ẩn đo được** — phù hợp nguyên tắc "đưa vào journal để dữ liệu phân xử". Ngưỡng cụ thể (30 phút sau tin, 5–8 tick FVG trên NQ, 2–3 nến) là HEURISTIC. EC6 (fractal conflict) được xử lý tổng quát bằng R7 + RULE-LS-005.

---

## 25. Định lượng

### 25.1 Từ điển biến — tách *biến quan sát* khỏi *ngưỡng đề xuất*

**A. Thuộc tính của mức (đo tại known_at hoặc khi ARMED)**

| Biến | Định nghĩa | Đơn vị | Ghi chú |
|---|---|---|---|
| `level_price`, `level_side` | Giá L; BSL/SSL | giá | — |
| `level_tf` | Khung của swing tạo mức | D1/H4/H1/M15/M5 | Biến T |
| `level_known_at` | Close của nến xác nhận swing | timestamp | Bắt buộc |
| `swing_level` | 1–5 theo framework swing | ordinal | Biến S |
| `level_tags` | PDH, PDL, PWH, Asia_H, London_L, round, EQH… | list | Biến V (đếm không trùng) |
| `eq_tol_atr` | \|H1 − H2\|/ATR nếu là EQH | ATR | Biến Q |
| `n_tests` | Số lần chạm (E1) không vượt | count | Biến N |
| `age_bars` | Số nến từ known_at | bars | Biến A |
| `is_erl_context` | Là biên range context D1? | bool | Biến C |
| `dol_aligned` | Mức nằm phía ngược DOL ex-ante? | bool | Biến D |
| `dist_atr` | (L − price)/ATR khi ARMED | ATR | Biến X (kiểm soát) |

**B. Thuộc tính của sự kiện (tại và ngay sau xuyên)**

| Biến | Định nghĩa | Đơn vị |
|---|---|---|
| `event_code` | E0–E9 | category |
| `pen_depth_atr` | (cực trị − L)/ATR₀ | ATR |
| `pen_time_bars` | Số nến ở bên kia trước khi phân xử | bars |
| `pen_speed` | Thời gian từ L tới cực trị (tick data) hoặc range nến xuyên/ATR | s hoặc ATR |
| `close_loc_atr` | (close_j − L)/ATR₀ | ATR |
| `clv_breach_bar` | (close − low)/(high − low) của nến xuyên | 0–1 |
| `reclaim_body_ratio` | \|body nến reclaim\| / range nến sweep | 0–1 |
| `resolve_bars` | Số nến tới REJECTED/ACCEPTED | bars |
| `session`, `minute_of_day` | Phiên, phút trong ngày | — |
| `news_window` | Trong ±x phút tin tier-1 | bool |

**C. Hậu quả (sau sự kiện)**

| Biến | Định nghĩa | Đơn vị |
|---|---|---|
| `mss_bars` | Số nến từ REJECTED tới MSS | bars |
| `mss_swing_level` | Level của swing bị phá | ordinal |
| `disp_atr` | Body lớn nhất trong leg MSS / ATR₀ | ATR |
| `fvg_size_atr` | Kích thước FVG đầu tiên / ATR₀ | ATR |
| `retrace_pct` | Độ sâu retrace về FVG/OB theo % leg | % |
| `first_passage` | Chạm target hay stop trước | {T, S, none} |
| `mfe_atr`, `mae_atr` | Max favorable/adverse excursion trong N nến | ATR |
| `label_flip_bars` | Số nến tới khi nhãn bị lật (nếu có) | bars |

**D. Bối cảnh**

| Biến | Định nghĩa |
|---|---|
| `bias_state`, `bias_tier` | Theo Bias Card (ex-ante) — [[59-Daily-Bias]] |
| `range_pos` | Vị trí giá trong range D1 (0–1) |
| `atr_regime` | ATR(14) D1 / trung vị 100 ngày |
| `trend_regime` | TREND/RANGE theo quy tắc khai báo |
| `run_state` | Có RUN ACTIVE ở khung H1 không |
| `smt` | Divergence tại sự kiện (bool) |
| `opex`, `rollover_window`, `dst_week` | bool |

### 25.2 Ngưỡng đề xuất (HEURISTIC — khai báo trước, không chỉnh theo kết quả)

| Tham số | Giá trị đề xuất v0.1 | Lý do chọn | Biến thể để test độ nhạy |
|---|---|---|---|
| ε (chạm) | 0.02·ATR hoặc 1 tick | Loại nhiễu bid/ask | 0, 0.05·ATR |
| δ (rejection) | 0.25·ATR | Đủ xa mức để không phải nhiễu | 0.1, 0.5 |
| Acceptance | 2 close > L hoặc close > L + 0.5·ATR | Bắt cả acceptance nhanh và chậm | 3 close; 0.3/1.0·ATR |
| k (timer phân xử) | 3 nến (M5–M15) | LS-Sim-05: > 99% được phân xử sau 3 nến trên null | 1, 6 |
| m (cửa sổ MSS) | 6 nến M5 | Đủ cho leg ngắn; tránh MSS "muộn" | 3, 12 |
| m' (cửa sổ entry) | 12 nến M5 | Retrace FVG trong ~1 giờ | 6, 24 |
| disp_atr | ≥ 1.3 | Trung gian giữa các ngưỡng phổ biến 1.0–2.0 | 1.0, 1.6, 2.0 |
| Level swing MSS | ≥ 2 theo khung setup | Loại micro swing | ≥ 1, ≥ 3 |
| EQH tol | 0.1·ATR | LS-Sim-07 | 0.05, 0.2 |
| Run r_max | 50% leg | Ranh giới phổ biến của "pullback nông" | 38%, 62% |
| x (ARMED) | 1.5·ATR | Phạm vi "đang tiếp cận" | 1.0, 2.5 |
| Stop buffer | max(0.15·ATR, 3×spread) | Tránh stop sát cực trị (W2) | 0.1, 0.3·ATR |

**Quy tắc khi test độ nhạy:** báo cáo **toàn bộ lưới** kết quả, không chọn ô đẹp nhất. Nếu edge chỉ tồn tại ở một ô → nhiều khả năng là overfitting.

### 25.3 Thước đo chính

**p_null (baseline hình học, short):** p_null = (S − E)/(S − T), với E = entry, S = stop, T = target. Long đối xứng: p_null = (E − S)/(T − S).

**SERR (Sweep Excess Reversal Rate):** SERR = (1/n)·Σ [𝟙(T trước S)ᵢ − p_null,ᵢ]. Trên random walk, E[SERR] ≈ 0 (LS-Sim-02). SERR > 0 có ý nghĩa thống kê = bằng chứng về thông tin vượt hình học.

**Expectancy với fill thực tế:** E[R] = (1/n)·Σ Rᵢ, Rᵢ tính từ **giá khớp thực tế** (stop-market khớp ở giá đầu tiên vượt stop; trừ spread/commission/slippage). Trên random walk với fill thực tế E[R] ≈ 0; với fill lý tưởng có thể > 0 một cách giả tạo (LS-Sim-02: +0.08R).

**Tỷ lệ lật nhãn (flip rate):** F(h) = P(nhãn bị lật trong h nến). So với đường null LS-Sim-05B.

**MAE/MFE theo ATR:** phân phối, không chỉ trung bình — dùng để kiểm tra stop/target có hợp lý không (stop đặt ở phần lõi phân phối MAE của lệnh thắng = stop quá sát).

### 25.4 Công thức hữu ích

- **Gambler's ruin có drift** (μ, σ theo đơn vị giá/thời gian): P(chạm b trước a | x) = [1 − exp(−2μ(x − a)/σ²)] / [1 − exp(−2μ(b − a)/σ²)].
- **Xác suất chạm mức cách d trong thời gian T (không drift):** P = 2·[1 − Φ(d/(σ√T))].
- **Chuẩn hóa ATR:** mọi khoảng cách/độ sâu/body chia cho ATR(14) đóng băng tại nến trước sự kiện.
- **Close Location Value:** CLV = (close − low)/(high − low).
- **Wilson CI** cho tỷ lệ (dùng khi n nhỏ) — xem Phụ lục.

---

## 26. Phương pháp backtest

### 26.1 Đặc tả nghiên cứu (theo 17 mục của project)

| # | Mục | Đặc tả v0.1 |
|---|---|---|
| 1 | **Hypotheses** | HYP-LS-001 … 018 (§35.3). Ưu tiên: 001, 003, 010, 012, 006 |
| 2 | **Population** | Mọi lần một mức ex-ante (G1–G5) bị xuyên — **không chỉ** lần có setup đẹp |
| 3 | **Timeframe** | Mức: H1, H4, D1 (PDH/PDL, session H/L). Sự kiện: phân loại trên M5. Context: D1 |
| 4 | **Market** | NQ (futures, RTH + ETH tách biệt), EURUSD, GBPUSD, XAUUSD — **từng thị trường riêng** |
| 5 | **Sample size** | Xem bảng power §26.4. Mục tiêu tối thiểu: ≥ 600 sự kiện REJECTED/thị trường cho SERR; ≥ 400–900 trade cho expectancy |
| 6 | **Inclusion** | Mức thỏa G1–G5; dữ liệu đầy đủ quanh sự kiện; ATR hợp lệ |
| 7 | **Exclusion** (khai báo trước) | Cửa sổ tin tier-1 (±15 phút); tuần rollover (NQ); ngày lễ thanh khoản mỏng; khoảng trống dữ liệu. **Báo cáo riêng** nhóm bị loại |
| 8 | **Entry rule** (3 biến thể) | V-a: close nến REJECTED (aggressive); V-b: retrace FVG sau REVERSAL CONF. (model); V-c: close nến MSS (không chờ retrace) |
| 9 | **Stop rule** | Cực trị sweep + buffer ≥ max(0.15·ATR, 3×spread); biến thể: ngoài POI |
| 10 | **Target rule** | T1 = pool IRL gần; T2 = pool đối diện ex-ante (DOL ngày); biến thể: R cố định 2R/3R |
| 11 | **Session** | Ghi killzone; phân tích phân tầng theo phiên |
| 12 | **Spread/slippage** | Spread theo giờ (dữ liệu broker/futures); stop-market khớp ở giá đầu tiên vượt stop + slippage giả định (ví dụ 0.5–1 tick NQ, 0.2–0.5 pip EURUSD); limit chỉ khớp khi giá **xuyên qua** giá limit ít nhất 1 tick |
| 13 | **Lookahead prevention** | Mức dùng từ known_at; swing ref cho MSS chỉ dùng khi đã xác nhận; ATR đóng băng; không dùng indicator vẽ hồi tố; replay từng nến |
| 14 | **Survivorship** | Dùng hợp đồng continuous back-adjusted đúng cách (NQ); không chọn thị trường/giai đoạn sau khi thấy kết quả; ghi mọi sự kiện kể cả không trade |
| 15 | **Outcomes** | first_passage, R (fill thực tế), MAE/MFE, resolve_bars, flip, SERR |
| 16 | **Statistics** | Win rate + Wilson CI; SERR + bootstrap CI; E[R] + CI; median R; profit factor; max drawdown (R); phân phối chuỗi thua; so sánh nhóm bằng permutation test |
| 17 | **Robustness** | Lưới tham số (§25.2); chia theo năm; chia theo thị trường; out-of-sample (walk-forward); null comparisons (§26.2 D) |

### 26.2 Bốn thiết kế nghiên cứu

**A. Event Study (rẻ nhất, làm trước):** đơn vị = sự kiện xuyên mức ex-ante. Câu hỏi: phân phối E-code; SERR của REJECTED vs ACCEPTED vs mức đối chứng; flip rate vs null; tốc độ/độ sâu theo LSS và theo giờ. *Không cần entry/exit — chỉ first passage.* Trả lời HYP-LS-001, 002, 006, 007, 008, 011, 016.

**B. Trade Study:** đơn vị = lệnh theo cây quyết định §22.6. Câu hỏi: E[R] với fill thực tế, so với các biến thể bỏ điều kiện. Trả lời HYP-LS-003, 004, 005, 010, 012.

**C. Ablation:** chạy Trade Study nhiều lần, mỗi lần bỏ một lớp (sweep, MSS, displacement, killzone, P/D, bias, SMT). Lớp nào bỏ đi mà E[R] không giảm → lớp đó không đóng góp (hoặc đóng góp chưa đo được với n hiện có).

| Arm | Điều kiện | Mục đích |
|---|---|---|
| A0 | Đầy đủ | Model |
| A1 | Bỏ sweep (MSS + disp tại POI là đủ) | Giá trị của điều kiện sweep (ô ③ vs ①) |
| A2 | Bỏ MSS (vào khi REJECTED) | Giá trị của xác nhận cấu trúc |
| A3 | Bỏ displacement | Giá trị của displacement |
| A4 | Bỏ bias D1 | Giá trị của context |
| A5 | Bỏ killzone | Giá trị của thời gian |

**D. Null comparisons:**
1. **Mức ngẫu nhiên:** thay danh sách mức bằng mức ngẫu nhiên cùng phân phối khoảng cách → nếu kết quả tương tự, "liquidity level" không mang thông tin.
2. **Xáo trộn thời gian:** đảo thứ tự ngày/tuần → phá cấu trúc phụ thuộc.
3. **Random walk khớp volatility:** chạy toàn bộ pipeline trên chuỗi mô phỏng có cùng hồ sơ biến động theo giờ → baseline cho mọi con số (đúng như LS-Sim-01…07).
4. **Đối xứng:** chạy cùng quy tắc theo hướng ngược (BSL sweep → long) — nếu cũng "thắng", kết quả có thể do drift của giai đoạn.

### 26.3 Schema journal (frontmatter đề xuất cho backtest note)

```yaml
# --- Liquidity event (v0.1) — bổ sung cho Backtest template, không thay thế ---
level_price:
level_side:            # BSL | SSL
level_tf:              # D1 | H4 | H1 | M15 | M5
level_known_at:        # YYYY-MM-DD HH:MM (giờ NY)
level_tags: []         # [PDH, Asia_L, EQH, round, ...]
swing_level:           # 1-5
lss:                   # 0-1 (equal weights v0.1)
dist_atr_armed:
p_null:
event_code:            # E0..E9 | PND | EXP
pen_depth_atr:
pen_time_bars:
close_loc_atr:
reclaim_body_ratio:    # = reclaim_body_quality (v1) dạng số
reclaim_body_quality:  # displacement | weak | doji   (v1)
resolve_bars:
state_path: []         # [ARMED, PENETRATED, PENDING, REJECTED, REVERSAL_CONF] — append-only
mss_bars:
mss_swing_level:
disp_atr:
fvg_size_atr:
entry_variant:         # Va | Vb | Vc
first_passage:         # T | S | none
r_fill:                # R theo giá khớp thực tế
mae_atr:
mfe_atr:
label_flip_bars:
swept_pool_tier:       # v1 W2
re_entry_taken:        # v1 W2
sweep_time_window:     # v1 §7.2
smt_divergence:        # v1 §7.1
news_window:           # v1 W3
rollover_window:       # v1 W6
dst_transition_week:   # v1 W6
missed_valid_setup:    # v1 W5
outcome_label_ex_ante: # nhãn tại thời điểm quyết định
outcome_label_ex_post: # nhãn sau expiry
```

Các trường `liquidity_swept`, `displacement`, `mss`, `fvg_valid` của Backtest template hiện có được giữ; schema trên chi tiết hóa chúng.

### 26.4 Cỡ mẫu và kiểm định — số cần biết trước khi bắt đầu

**[MATHEMATICAL]** (α = 0.05 hai phía, power 80%, sự kiện độc lập):

| Mục tiêu phát hiện | Baseline | n cần |
|---|---|---|
| SERR +3 điểm % | p_null = 0.25 | **~1,670** |
| SERR +5 điểm % | p_null = 0.25 | **~610** |
| SERR +10 điểm % | p_null = 0.25 | ~160 |
| SERR +5 điểm % | p_null = 0.20 | ~530 |
| SERR +5 điểm % | p_null = 0.40 | ~760 |
| E[R] = +0.1R | win 25%, R:R 4 (σ_R ≈ 2.17) | ~3,680 |
| E[R] = +0.2R | như trên | **~920** |
| E[R] = +0.3R | như trên | ~410 |
| E[R] = +0.2R | win 35%, R:R 2.5 (σ_R ≈ 1.67) | ~550 |
| E[R] = +0.2R | win 50%, R:R 1.5 (σ_R ≈ 1.25) | ~310 |

**Hàm ý:** chiến lược sweep thường có win rate thấp và R:R cao → **phương sai R lớn** → cần nhiều lệnh hơn trực giác để biết edge có thật. Một backtest tay 30–50 setup không phân biệt được +0.3R với 0 (CI rộng ±0.6R).

**Kiểm định đề xuất:** SERR: bootstrap (resample theo ngày để giữ phụ thuộc trong ngày); so sánh arm: permutation test trên R; nhiều giả thuyết cùng lúc: điều chỉnh (Holm/Benjamini-Hochberg) hoặc tách tập khám phá/kiểm định.

### 26.5 Falsification — điều gì sẽ bác bỏ framework

| Claim | Bị bác bỏ khi | Trạng thái |
|---|---|---|
| Sweep tại mức ex-ante có thông tin đảo chiều (HYP-LS-001) | SERR của REJECTED không khác 0 (CI chứa 0) với n ≥ 600/thị trường, **và** không khác SERR của mức ngẫu nhiên | UNTESTED |
| Điều kiện sweep tăng giá trị model (HYP-LS-010) | E[R](A0) − E[R](A1) không khác 0 | UNTESTED |
| MSS + disp là lớp có giá trị (HYP-LS-003) | E[R](A0) − E[R](A2) không khác 0 | UNTESTED |
| Mức nổi bật có hành vi stop-cluster (HYP-LS-007) | Tốc độ sau xuyên ở LSS cao không khác LSS thấp (kiểm soát giờ, ATR) | UNTESTED |
| Nhãn sweep có thông tin (HYP-LS-011) | Flip rate thực ≈ flip rate null | UNTESTED |

Nếu các claim cốt lõi bị bác bỏ, phần còn lại của framework vẫn có thể có **giá trị quy trình** (giảm số quyết định, buộc viết invalidation, journal có cấu trúc) — giống phân tích "useful process vs useful information vs useful story" của [[59-Daily-Bias]] §0.

---

## 27. Checklist trước khi áp dụng vào trade *(v1 §8, có bổ sung v2)*

> [!warning] Không trade chỉ vì thấy khái niệm xuất hiện
> Một cú quét không phải lệnh. Chỉ vào khi có reclaim + displacement + POI + đúng context.

#### A. Context (HTF)
- [ ] Daily Bias đã rõ: `Bullish / Bearish / Neutral`.
- [ ] Pool liquidity mục tiêu đã đánh dấu (equal highs/lows, PDH/PDL, swing cũ).
- [ ] Cú sweep ở đúng premium (Short) / discount (Long) của dealing range.
- [ ] Sweep tại / trùng một POI HTF có ý nghĩa, đồng hướng bias.
- [ ] Có pool liquidity đối diện làm target.

#### B. Execution (LTF / khi giá tới POI)
- [ ] Giá đã reclaim mức vừa quét (đóng nến trở lại bên trong).
- [ ] Có displacement + MSS xác nhận đảo chiều sau sweep.
- [ ] Displacement để lại FVG/OB làm điểm entry refined.
- [ ] Entry SAU sweep, không phải bắt đáy/đỉnh trên wick.
- [ ] Stop logic: ngoài đáy/đỉnh cú sweep.
- [ ] Target là liquidity rõ; R:R tối thiểu đạt kế hoạch.

#### C. Quy tắc "không có lệnh"
- [ ] Giá đóng nến vượt hẳn mức (break thật) → không trade reversal.
- [ ] Không có displacement/MSS sau sweep → không trade.
- [ ] Sweep ngược bias / sai premium-discount → không trade.
- [ ] Sweep giữa range không POI / không target → không trade.
- [ ] Đã chạy xa sau nhiều sweep → không chase.

#### D. Bổ sung v2 — giao thức thời gian thực

- [ ] Danh sách mức ex-ante đã chốt trước phiên (known_at, LSS, p_null tới target dự kiến).
- [ ] Tham số ε, δ, k, m, m' khai báo; không chỉnh trong phiên.
- [ ] Tại nến xuyên: **không hành động** — trạng thái PENDING.
- [ ] REJECTED trong k nến? Nếu không → EXPIRED.
- [ ] MSS phá swing **Level ≥ 2 của khung setup** + displacement trong m nến? Nếu không → STALE.
- [ ] Đang có RUN ACTIVE ngược hướng ở H1? Nếu có → không trade reversal (RULE-LS-005).
- [ ] Ngoài cửa sổ tin tier-1; không phải tuần rollover với mức nghi artifact.
- [ ] Ghi `state_path`, `outcome_label_ex_ante` trước khi biết kết quả.

---

## 28. Lỗi thường gặp

### 28.1 Lỗi thực thi *(v1 §9)*

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Trade cú wick ngay lập tức | Long/Short ngay khi giá xuyên mức | Dễ trúng double sweep / break thật | Chờ reclaim + displacement rồi mới vào |
| Nhầm break thật là sweep | Giá đóng nến ngoài mà vẫn chờ đảo | Đặt cược ngược xu hướng tiếp diễn | Đợi nến đóng: đóng trong = sweep, đóng ngoài = break |
| Bỏ qua bias | Trade mọi sweep cả 2 chiều | Sweep ngược bias xác suất thấp | Chỉ trade sweep đồng hướng Daily Bias |
| Stop quá sát mép sweep | Stop ngay dưới wick vài pip | Double sweep quét sạch trước khi đảo | Đặt stop ngoài cả vùng POI/sweep, cho dư địa |
| Bỏ qua premium/discount | Long sweep ở premium, Short ở discount | Entry thành chase, R:R xấu | Long sweep ở discount, Short ở premium |
| Vào khi không có displacement | Giá đi ngang sau sweep mà vẫn vào | Chưa có intent đảo chiều | Yêu cầu displacement + MSS trước khi vào |
| Trade sweep giữa range | Quét pool nhỏ quanh equilibrium | Không có draw rõ, dễ nhiễu | Ưu tiên sweep tại POI HTF / external pool |
| Chase sau nhiều sweep | Vào khi giá đã chạy xa | Phần lớn move đã xong | Chờ sweep mới tại POI HTF hoặc bỏ qua |

### 28.2 Lỗi suy luận (v2)

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Gọi mọi wick là sweep | Mức được vẽ sau khi thấy wick | Base rate ~50% close-back (LS-Sim-01) → "sweep" ở khắp nơi | Danh sách mức ex-ante; nhãn "unlisted breach" |
| Đếm "tỷ lệ đảo chiều" bằng định nghĩa lỏng | "Giá có giảm sau đó" | 73% trên random walk (LS-Sim-02B) | Dùng first passage target vs stop; so với p_null |
| Bỏ qua p_null | Thắng 25% với R:R 3 → "edge" | Chính xác bằng hình học → E[R] ≈ 0 | Báo cáo SERR |
| Backtest với fill lý tưởng | Stop khớp đúng giá, limit khớp khi chạm | Edge ảo +0.08R ngay trên random walk | Fill thực tế; limit cần xuyên qua |
| Nhãn hồi tố | "Đó là IDM" sau khi giá tới POI | Hindsight; thống kê vô nghĩa | known_at cho mọi nhãn |
| Loại "trade xấu" khỏi mẫu | "Lần đó không phải sweep thật" | Survivorship → expectancy phóng đại | Định nghĩa trước; không loại sau |
| Trộn khung | M5 sweep coi như D1 event | Internal bị nhầm external (Case F) | R7; range context từ D1 |
| Coi "Smart Money" là nguyên nhân | Giải thích mọi kết quả bằng ý định | Không thể sai → không học được | Viết lại bằng cơ chế + hypothesis |
| Trade ngược run | Short mọi wick trong uptrend | Rejection M5 trong run H1 thường là pullback | RULE-LS-005 |
| Đếm confluence trùng | PDH + Asia H + số tròn cùng vùng = "3 lý do" | Cùng một thông tin đếm ba lần | Cluster = một vùng; V không cộng dồn |

---

## 29. Phản biện & giới hạn (Critique)

### 29.1 Phản biện từ góc nhìn khoa học/quant *(v1 §16.1)*

- **"Reclaim" là một ngưỡng chủ quan được ngụy trang thành khách quan:** dù mục W1 đã cố gắng lượng hóa ("thân nến reclaim ≥ ~50% range nến sweep"), ngưỡng 50% vẫn là một số tùy chọn (arbitrary) — không có cơ sở thống kê công khai nào chứng minh 50% tốt hơn 40% hay 60% trên một tập dữ liệu ngoài mẫu đủ lớn.
- **Không có định nghĩa "displacement" định lượng thống nhất:** "nến thân lớn" là mô tả tương đối — lớn so với ATR bao nhiêu chu kỳ? Các trader khác nhau dùng ngưỡng khác nhau (1.5x ATR, 2x ATR, hoặc thuần cảm quan), khiến việc backtest hai hệ thống "giống nhau về lý thuyết" cho ra kết quả rất khác nhau.
- **Hindsight bias trong việc phân loại sweep vs break:** một cú xuyên mức chỉ được gọi là "sweep" (reclaim, hợp lệ) hoặc "break" (acceptance, vô hiệu setup) SAU KHI biết nến đóng ở đâu — tại thời điểm giá đang xuyên, không có cách phân biệt chắc chắn, nghĩa là mọi phân tích "đã thấy sweep đẹp" đều mang tính hồi cố.
- **Không có backtest công khai đạt chuẩn thống kê (peer-reviewed hoặc dữ liệu mở):** phần lớn "chứng minh" hiệu quả của sweep-based entry đến từ ảnh chụp chart chọn lọc (cherry-picked) trên mạng xã hội, không phải từ bộ dữ liệu đầy đủ, không chọn lọc, kiểm định ngoài mẫu.
- **Nguy cơ curve-fitting khi thêm quá nhiều lớp xác nhận:** SMT Divergence (22.4) + thời gian sweep (22.3) + tốc độ/độ sâu (10.6) + Turtle Soup (22.5) — mỗi lớp lọc thêm giúp câu chuyện "hợp lý hơn" trên các mẫu lịch sử đã biết, nhưng cũng làm tăng số bậc tự do (degrees of freedom) của hệ thống, tăng rủi ro hệ thống chỉ khớp tốt với dữ liệu đã thấy mà không có sức mạnh dự báo thật ra ngoài mẫu.
- **Giải thích thay thế đơn giản hơn — Mean Reversion cổ điển:** hiện tượng "giá xuyên qua một mức cực trị ngắn hạn rồi đảo chiều" hoàn toàn có thể được giải thích bằng lý thuyết mean-reversion thống kê (giá dao động quá xa trung bình động ngắn hạn có xu hướng quay về) — không cần khái niệm "thanh khoản được engineer có chủ đích" để giải thích cùng một hiện tượng quan sát được.

### 29.2 Phản biện của phản biện *(v1 §16.2)*

**Phải chấp nhận hoàn toàn:** các ngưỡng định lượng (50% thân nến, X lần ATR cho displacement) đều là lựa chọn tùy ý chưa được kiểm định thống kê công khai đầy đủ; hindsight bias trong phân loại sweep/break là một hạn chế cấu trúc không thể loại bỏ hoàn toàn.

**Có thể trả lời được:**
- *Cứng hóa ngưỡng để tự backtest:* dù chưa có chuẩn ngành công khai, mỗi trader hoàn toàn có thể tự cứng hóa ngưỡng (ví dụ: displacement = thân nến ≥ 1.5x ATR(14) của khung đang xét) và backtest hệ thống của CHÍNH MÌNH với ngưỡng cố định — giá trị không nằm ở việc tìm "ngưỡng đúng tuyệt đối" mà ở việc có một ngưỡng NHẤT QUÁN để đo lường hiệu quả qua thời gian.
- *Mean-reversion và "engineered liquidity" không loại trừ nhau:* hai lời giải thích có thể đúng CÙNG LÚC ở hai tầng khác nhau — mean-reversion giải thích TẠI SAO giá có xu hướng quay đầu sau khi lệch xa (động lực thống kê), còn "quét thanh khoản trước khi đảo" giải thích CƠ CHẾ VI MÔ khiến đảo chiều xảy ra chính xác tại các mức có stop cluster (không phải tại mọi điểm lệch xa ngẫu nhiên). Đây không phải hai lý thuyết cạnh tranh loại trừ nhau mà là hai tầng mô tả (thống kê vĩ mô vs cơ chế vi mô) của cùng một hiện tượng.
- *Giá trị của nhiều lớp xác nhận nằm ở việc giảm số lượng lệnh, không đảm bảo từng lệnh đúng:* SMT/timing/tốc độ không cần chứng minh mỗi lớp có ý nghĩa dự báo độc lập — vai trò thực tế của chúng là LỌC bớt số lượng setup được trade, giữ lại nhóm có nhiều tín hiệu đồng thuận nhất, tương tự cách một hệ thống định lượng dùng nhiều factor để giảm số lệnh nhưng tăng chất lượng trung bình — miễn là số lớp không tăng vô hạn chỉ để giải thích các trường hợp fail sau khi đã biết kết quả.

### 29.3 Giới hạn cứng phải chấp nhận *(v1 §16.3)*

1. Không có ngưỡng khách quan, được kiểm định công khai cho "displacement đủ mạnh" hay "reclaim đủ tin cậy" — mọi ngưỡng số đều là lựa chọn cá nhân/cộng đồng, chưa qua kiểm định thống kê ngoài mẫu quy mô lớn.
2. Việc phân loại một cú xuyên mức là "sweep" (hợp lệ) hay "break" (vô hiệu) chỉ có thể thực hiện SAU KHI nến đã đóng — tại thời điểm ra quyết định trong lúc nến đang hình thành, luôn có một khoảng không chắc chắn không thể loại bỏ.
3. Wick trên chart lịch sử không đảm bảo có thể khớp lệnh thật tại đó trong điều kiện live (đặc biệt quanh tin tức hoặc thanh khoản mỏng) — điều này làm mọi backtest dựa trên "entry tại đáy wick" có nguy cơ phóng đại expectancy thật (đã nêu ở W3).
4. Trên các cặp tài sản/thời điểm thanh khoản mỏng (crypto cuối tuần, FX phiên Á, sau giờ đóng RTH của futures), không có cách phân biệt chắc chắn giữa "sweep phản ánh hành vi tập thể thật" và "biến động giá do một lệnh lớn đơn lẻ hoặc thanh khoản mỏng gây ra" bằng việc chỉ quan sát hình dạng nến.
5. Chiến lược dựa trên sweep có độ trễ cấu trúc (phải chờ reclaim + displacement trước khi vào) — đây là đánh đổi cố hữu giữa an toàn hơn (tránh vào trước khi xác nhận) và giá vào lệnh kém hơn so với việc "đón đầu" cú sweep, không thể tối ưu cả hai đồng thời.

> [!quote] Kết luận trung thực
> Liquidity Sweep là một khung đọc order flow có cơ sở logic vững — quét thanh khoản trước khi đảo chiều là hành vi hợp lý về mặt thực thi lệnh lớn, không phải chuyện hoang đường. Nhưng các ngưỡng cụ thể (bao nhiêu % thân nến, bao nhiêu ATR) đều là lựa chọn tùy ý cần TỰ backtest và cứng hóa cho từng hệ thống cá nhân, không nên coi là chuẩn ngành đã được chứng minh. Đáng dùng ở mức **một bộ lọc timing + xác nhận trong một hệ thống có bias/POI xác định trước**, KHÔNG đáng dùng như một công cụ dự đoán chính xác từng cú quét sẽ đảo hay tiếp tục. Điều kiện dùng có trách nhiệm: cứng hóa ngưỡng đo lường được, tách riêng các mẫu trong khung giờ tin tức/thanh khoản mỏng khi backtest, và luôn coi reclaim + displacement là điều kiện CẦN chứ không phải ĐỦ để tự tin vào lệnh.

### 29.4 Đối chiếu với các khung lý thuyết khác *(v1 §15)*

| Khung lý thuyết | Khái niệm tương đương | Trùng ở đâu | Khác ở đâu |
|---|---|---|---|
| **Wyckoff** | Spring/Upthrust hoặc "Sign of Weakness/Strength" sau test | Cùng mô tả việc giá xuyên qua một mức rồi bị từ chối, xác nhận hấp thụ | Wyckoff gắn sự kiện này với vị trí trong schematic Accumulation/Distribution; ICT không yêu cầu schematic, chỉ cần vị trí tương đối với dealing range |
| **Auction Market Theory** | Rejection tại "excess" (đuôi phân phối volume) | Cùng ý tưởng: giá bị từ chối mạnh tại vùng thanh khoản mỏng, xác nhận bằng việc không quay lại test | AMT đo bằng volume profile khách quan; ICT đọc qua hình dạng wick + nến đóng, ít định lượng hơn |
| **Orderflow/Footprint** | Absorption/exhaustion tại đáy/đỉnh — lệnh limit lớn chống lại market order đang đẩy giá | Cùng mô tả hiện tượng: lệnh chờ lớn "nuốt" hết áp lực market order tại một mức, tạo đảo chiều | Footprint cho số liệu khớp lệnh thật theo mức giá và theo thời gian thực; ICT chỉ suy luận qua hình dạng nến sau khi đã đóng |
| **Turtle Soup (đã nêu ở mục 22.5)** | Chính là một model đóng gói sẵn của sweep + reclaim | Trùng gần như hoàn toàn về cơ chế | Turtle Soup là chiến lược cụ thể có luật vào/ra cố định; Liquidity Sweep trong ICT là một khái niệm rộng hơn, dùng trong nhiều model khác nhau |

### 29.5 Bổ sung v2 — lời giải thích thay thế và điều chúng ta thực sự biết

**Năm lời giải thích thay thế cho cùng hình ảnh "xuyên mức rồi đảo":**

| Lời giải thích | Cơ chế | Dự báo khác biệt so với câu chuyện "stop hunt" |
|---|---|---|
| **Hình học ngẫu nhiên** | Reflection principle; gambler's ruin | Tỷ lệ "đảo" = p_null; không phụ thuộc LSS |
| **Impact tạm thời** | Đợt lệnh không mang thông tin (stop) có impact phai | Đảo *chậm, một phần*, không có displacement; phụ thuộc kích thước cụm stop |
| **Take-profit / limit tập trung** | Phản hồi âm tại mức (Osler 2003) | Đảo *tại/trước* mức (E0/E1), không cần xuyên |
| **Mean reversion ngắn hạn** | Thống kê (v1 đã nêu) | Đảo sau mọi cực trị ngắn hạn, không riêng mức nổi bật |
| **Dòng lệnh thông tin ngược chiều** | Người có thông tin/vị thế lớn dùng stop làm đối ứng | Đảo *nhanh, có displacement*, phụ thuộc bối cảnh HTF — đây là phiên bản kiểm chứng được của câu chuyện ICT |

Chỉ lời giải thích cuối cùng tạo ra **edge giao dịch được**; bốn lời giải thích đầu tạo ra hình ảnh giống hệt nhưng không có edge (hoặc có edge theo hướng khác — take-profit fade). Thiết kế backtest §26 được xây để tách chúng.

**Điều chúng ta thực sự biết (bằng chứng ngoài ICT):**
1. Lệnh tập trung quanh số tròn trong FX; stop-loss ngay sau, take-profit ngay tại (Osler 2003, 2005).
2. Vượt vùng stop-loss → chuyển động nhanh và kéo dài hơn (Osler 2005).
3. S/R trùng đỉnh độ sâu sổ lệnh (Kavajecz & Odders-White 2004).
4. Có hiệu ứng "nhớ" tại S/R ở thang thời gian ngắn trên cổ phiếu (Garzarelli et al. 2014).
5. Stop order trên futures lớn là phần nhỏ khối lượng, tăng theo biến động (Fett & McPhail 2017).
6. Impact của lệnh lớn có phần tạm thời; giá hồi một phần sau khi lệnh hoàn tất (Farmer et al. 2013; Moro et al. 2009; Bershova & Rakhlin 2013).
7. Flash event có thể do thanh khoản mỏng + bộ khuếch đại cơ học (BIS 2017).

**Điều chúng ta chỉ đang giả định:**
1. Swing high/low theo nghĩa ICT có mật độ stop cao như số tròn.
2. "Sweep → reversal" xảy ra nhiều hơn hình học.
3. MSS + displacement sau sweep phân biệt được nhánh R1 với R2/R3 tốt hơn baseline.
4. Killzone/SMT/P/D gia tăng giá trị dự báo.
5. Có một "ý định" đằng sau sweep.

> [!quote] Kết luận trung thực (v2)
> Liquidity Sweep là một cách đặt tên có ích cho một sự kiện có thật (giá giao dịch qua mức nổi bật rồi bị phân xử), dựa trên một cơ chế có thật (lệnh có điều kiện tập trung quanh mức nổi bật, phản hồi dương khi bị kích hoạt). Phần **chưa được chứng minh** là phần mang tiền: rằng sau loại sự kiện này, xác suất đi về pool đối diện vượt hình học đủ để trả spread, slippage và độ trễ xác nhận. Đáng dùng như **một khung tổ chức quyết định có máy trạng thái rõ ràng và một nghiên cứu có thể bác bỏ**, không đáng dùng như một tín hiệu tự thân. Kết luận của v1 (§29.3 trên) vẫn đúng; v2 thêm các baseline định lượng để biết "đúng" phải vượt mức nào.

---

## 30. Mô hình tư duy cuối cùng

### 30.1 Một câu

**Một liquidity sweep là một phép thử tại một mức nổi bật: các lệnh có điều kiện (nếu có) được tiêu thụ, và điều xảy ra tiếp theo — rejection, acceptance hay không gì cả — do dòng lệnh đến sau quyết định; nhiệm vụ của trader là ước lượng nhánh nào có xác suất vượt hình học bằng thông tin có sẵn TRƯỚC khi nhánh đó hiện ra.**

### 30.2 Chín bước

1. **Danh sách mức ex-ante** (G1–G5, known_at, LSS, p_null).
2. **Bối cảnh D1** (bias state, DOL hai phía, range context, run state).
3. **Kịch bản H1** (POI + mức phía ngược DOL; giờ; tin).
4. **Chờ ARMED → PENETRATED.** Không hành động.
5. **PENDING → phân xử** trong k nến (E-code).
6. **REJECTED → xác nhận** MSS (Level ≥ 2) + displacement trong m nến — hoặc STALE.
7. **Trigger** trong m' nến; R:R; stop ngoài cực trị + buffer.
8. **Ghi log append-only** (state_path, nhãn ex-ante).
9. **Chấm sau expiry** bằng first passage, R thực, SERR — so với baseline.

### 30.3 Trả lời chuỗi WHAT → … → HOW TO BACKTEST của brief

| Câu hỏi | Trả lời ngắn | Mục |
|---|---|---|
| **WHAT** | Sự kiện: giá xuyên mức ex-ante rồi bị phân xử (sweep: rejection; run: acceptance qua nhiều mức) | §5, §6 |
| **WHY** (tồn tại) | Lệnh có điều kiện tập trung quanh mức nổi bật (salience) | §2 |
| **WHERE** | Mức có LSS cao: ERL range context, PDH/PDL, session H/L, EQH/EQL, số tròn | §2.3, §9 |
| **HOW** (hình thành) | Vòng đời: creation → accumulation → migration → interaction → consumption → replenishment | §8 |
| **WHEN** (có ý nghĩa) | Khi mức có ý nghĩa ở khung context, bối cảnh HTF ngược hướng xuyên, thời gian có dòng lệnh mới | §11.3, §22 |
| **WHEN NOT** | Tin, rollover, run ngược hướng, mức vẽ sau, swing vi mô | §22.7, §24 |
| **WHAT HAPPENS AFTER** | Sáu nhánh; do dòng lệnh sau quyết định | §11 |
| **HOW TO IDENTIFY** | Máy trạng thái với timer, bar close, known_at | §20, §21 |
| **HOW TO VALIDATE** | MSS + displacement; chấm bằng first passage vs p_null | §13, §25 |
| **HOW TO TRADE** | Cây quyết định D1 → H1 → M5 | §22.6 |
| **HOW TO QUANTIFY** | Từ điển biến + ngưỡng khai báo trước + SERR | §25 |
| **HOW TO BACKTEST** | Event study → trade study → ablation → null comparisons | §26 |

### 30.4 Ba lớp — và cách nhận ra lớp nào bạn đang ở

| Lớp | Câu nói điển hình | Kiểm tra |
|---|---|---|
| **Useful process** | "Tôi chỉ vào sau REJECTED + MSS; tôi ghi known_at" | Luôn có giá trị: giảm quyết định, có invalidation |
| **Useful information** | "Sau REJECTED tại mức LSS cao, P(target trước stop) > p_null" | Cần backtest — chưa biết |
| **Useful story** | "Smart money vừa lấy BSL để phân phối" | Không kiểm chứng được — đừng dùng để ra quyết định |

---

## 31. Câu hỏi tự kiểm tra

### 31.1 Câu hỏi thực hành *(v1 §10)*

- Mình có phân biệt được Sweep (reclaim) và Break thật (acceptance) trong 30 giây không?
- Pool liquidity nào vừa bị quét, và nó là internal hay external?
- Cú quét này có ở đúng premium/discount và đồng hướng Daily Bias không?
- Đã có displacement + MSS sau sweep chưa, hay mình đang vào trên wick?
- Đáy/đỉnh cú sweep ở đâu để đặt stop logic?
- Target liquidity phía đối diện ở đâu, R:R bao nhiêu?
- Điều gì làm setup này invalid (đóng nến lại ngoài mức)?
- Nếu mình không trade cú sweep này, lý do "No Trade" là gì?
- *(bổ sung)* Pool vừa bị quét nằm TRUNG GIAN (có thể là IDM) hay TẠI/NGOÀI POI (external/structural), và mình đã phân loại đúng trước khi hành động chưa?
- *(bổ sung)* Đây có phải tuần rollover contract hoặc tuần giao thời DST không — nếu có, mức độ tin tưởng vào độ sâu/thời điểm của sweep này cần hạ xuống không?
- *(bổ sung)* Nếu là crypto, mình đã kiểm tra funding rate/open interest để loại trừ khả năng đây là liquidation cascade thay vì sweep thật chưa?
- *(bổ sung)* Khung liền kề (trên/dưới) có đang cho một sweep theo HƯỚNG NGƯỢC LẠI không — đây có phải fractal conflict không?

### 31.2 Câu hỏi chẩn đoán (v2)

1. Mức vừa bị xuyên có trong danh sách ex-ante của bạn không? known_at của nó là lúc nào?
2. Nếu đây là random walk, xác suất lệnh bạn định vào chạm target trước stop là bao nhiêu (p_null)? Bạn có lý do gì *đo được* để tin xác suất thật cao hơn?
3. Tại close của nến này, sự kiện đang ở trạng thái nào trong máy trạng thái? Bạn có đang hành động trong PENDING không?
4. Swing bị phá trong "MSS" của bạn thuộc Level mấy, ở khung nào? Nó có ý nghĩa với khung context không?
5. Nhãn bạn vừa ghi có thể bị lật trong 6 nến tới với xác suất bao nhiêu trên null (LS-Sim-05)? Điều gì làm bạn tin nó ổn định hơn?
6. Nếu bỏ điều kiện "sweep" khỏi setup này, nó còn là setup không (ô ③)? Bạn đã đo ô ③ chưa?

> [!question] Ba câu hỏi chẩn đoán nhanh (trả lời trước khi đọc đáp án ở flashcards Q12–Q14)
> (a) Trên random walk không drift, nếu một nến giao dịch xuyên qua mức L, xác suất nó đóng cửa ở bên kia L là bao nhiêu trong giới hạn liên tục?
> (b) Một lệnh short sau sweep: entry 100, stop 102, target 92. p_null là bao nhiêu? R:R? Expectancy trên random walk?
> (c) Vì sao một cụm stop lớn hơn có thể làm *giảm* xác suất reversal thay vì tăng?

---

## 32. Flashcards / Active Recall

### 32.1 Flashcards của v1

#### Q1
**Hỏi:** Liquidity Sweep là gì và mục đích của nó?
**Đáp:** Là hành động giá quét qua một pool liquidity (đỉnh/đáy, equal highs/lows) để kích hoạt stop + pending order, gom thanh khoản cho smart money, rồi đảo chiều. Mục đích: lấy nhiên liệu để khớp lệnh lớn và bẫy đám đông.

#### Q2
**Hỏi:** Phân biệt Sweep và Break thật?
**Đáp:** Sweep = xuyên mức bằng wick rồi **đóng nến trở lại bên trong** + displacement ngược (đảo chiều). Break thật = **đóng nến vượt hẳn** mức, có acceptance, đi tiếp (tiếp diễn).

#### Q3
**Hỏi:** Vì sao không nên vào lệnh ngay trên wick của cú quét?
**Đáp:** Vì chưa có xác nhận; dễ trúng break thật hoặc double sweep (cú quét sâu hơn) quét sạch stop trước khi đảo thật.

#### Q4
**Hỏi:** Sau một SSL sweep hợp lệ, ta tìm vị thế gì và stop đặt ở đâu?
**Đáp:** Tìm **Long**; stop đặt ngay dưới đáy của cú sweep (nơi liquidity vừa bị lấy).

#### Q5
**Hỏi:** Hai điều kiện xác nhận một sweep đã "thành công"?
**Đáp:** (1) Reclaim — giá đóng nến trở lại bên trong vùng; (2) Displacement + MSS ngược hướng quét.

#### Q6
**Hỏi:** Double sweep là gì?
**Đáp:** Cú sweep đầu kéo trader vào, cú sweep thứ hai sâu hơn quét stop của họ rồi mới đảo chiều thật. Phòng tránh bằng cách vào tại POI HTF lớn và đặt stop ngoài cả vùng.

#### Q7
**Hỏi:** Liquidity Sweep đóng vai trò gì với FVG/OB/OTE?
**Đáp:** Là trigger / điều kiện kích hoạt. Các POI này có xác suất cao hơn nhiều khi xuất hiện ngay SAU một sweep đúng hướng narrative.

#### Q8 *(bổ sung)*
**Hỏi:** Vì sao trên NQ/ES, một cú sweep xảy ra đúng phiên OPEX (options expiration) lại kém tin cậy hơn cùng cú sweep đó vào một ngày thường?
**Đáp:** Vì OPEX tạo dealer hedging flow và gamma exposure bất thường lớn — giá có thể đảo ngược dữ dội quanh "gamma wall" mà không liên quan gì tới cấu trúc thanh khoản thật; một MSS "đẹp như sách" hình thành ngay sau sweep vẫn có thể fail vì lực đảo chiều đến từ dealer hedging, không phải institutional order flow theo đúng nghĩa ICT (xem Case Study B, mục 23.3).

#### Q9 *(bổ sung)*
**Hỏi:** Trên crypto (BTCUSD/ETHUSD), làm sao phân biệt một sweep chất lượng cao với một cú "sweep" thực chất là liquidation cascade?
**Đáp:** Kiểm tra funding rate và open interest (OI) trước khi tin vào cú sweep: funding rate cực đoan (dương/âm mạnh) + OI tăng vọt trước đó là dấu hiệu đòn bẩy tích lũy quá mức — cú "sweep" tiếp theo nhiều khả năng là hiệu ứng cơ học của thanh lý dây chuyền (liquidation cascade), không phải smart money thật sự gom thanh khoản có chủ đích (xem EC5, mục 24.2).

#### Q10 *(bổ sung)*
**Hỏi:** Phân biệt vai trò của Liquidity Sweep so với Inducement khi cả hai đều là "quét thanh khoản" về mặt hành động?
**Đáp:** Liquidity Sweep là HÀNH ĐỘNG (giá quét + reclaim tại bất kỳ pool nào), còn Inducement là VAI TRÒ của một pool cụ thể (pool mồi nằm giữa giá hiện tại và POI thật). Một cú sweep có thể xảy ra tại pool mồi (khi đó gọi là "sweep IDM") hoặc tại pool chính dẫn tới đảo chiều thật (external sweep) — bản thân hành động sweep không tự nó cho biết đó là mồi hay pool chính (xem mục 13.4).

#### Q11 *(bổ sung)*
**Hỏi:** Vì sao một cú sweep hình thành TRONG nến tin tức mạnh (ví dụ CPI) thường kém tin cậy hơn một MSS bình thường dù trông "đẹp" hơn (displacement lớn hơn, FVG sâu hơn)?
**Đáp:** Vì nó phản ánh phản ứng tin tức tức thời, hai chiều, chưa ổn định — không phải order flow tổ chức có chủ đích. Nên chờ 5-15 phút sau tin để spread và biến động ổn định, đọc lại cấu trúc trên nền giá mới, KHÔNG vào ngay tại FVG được tạo trong chính nến tin.

> [!note] Chú thích v2 cho flashcards v1
> - **Q1:** câu "gom thanh khoản cho smart money… mục đích: lấy nhiên liệu để khớp lệnh lớn và bẫy đám đông" là **[INTERPRETATION]**. Đáp án v2 ở Q12.
> - **Q2/Q5:** đúng tinh thần; thêm "tạm thời — có timer k, có thể bị lật".
> - **Q4:** stop "ngay dưới đáy cú sweep" → v2: dưới cực trị + buffer (RULE-LS-004), vì cực trị sweep là nơi stop mới tập trung.
> - **Q7:** "xác suất cao hơn nhiều khi xuất hiện SAU sweep" → **[HYPOTHESIS]** HYP-LS-010.
> - **Q8:** OPEX → HYP-LS-017.

### 32.2 Flashcards bổ sung (v2)

#### Q12
**Hỏi:** Định nghĩa Liquidity Sweep theo DEF-LS-04 (v0.1)?
**Đáp:** Với mức ex-ante L (known_at trước sự kiện, thỏa G1–G5): nến j đầu tiên có high > L + ε; sweep xảy ra nếu trong [j, j + k] có close < L − δ trước khi có acceptance. known_at của nhãn = close nến rejection. Không có phân xử trong k nến → EXPIRED.

#### Q13
**Hỏi:** Trên random walk không drift, nếu một nến xuyên mức L, xác suất close ở lại bên kia L (giới hạn liên tục)?
**Đáp:** 50% (reflection principle). Trên random walk rời rạc: 29% (M5) → 52% (D1) tùy số bước trong nến (LS-Sim-01). Hệ quả: hình dạng wick-close-back không phải bằng chứng.

#### Q14
**Hỏi:** Short sau sweep: entry 100, stop 102, target 92. p_null? R:R? Expectancy trên random walk?
**Đáp:** p_null = (102 − 100)/(102 − 92) = 0.20; R:R = 8/2 = 4; E[R] = 0.2·4 − 0.8 = 0. "Thắng 20% với R:R 4" là đúng bằng hình học — không phải edge.

#### Q15
**Hỏi:** Vì sao cụm stop lớn hơn có thể làm *giảm* xác suất reversal?
**Đáp:** Stop là phản hồi dương: cụm lớn + sổ mỏng → cascade đi xa hơn (LS-Sim-04), có thể tạo acceptance; Osler (2005): vượt vùng stop-loss → tiếp diễn nhanh và kéo dài. Reversal cần một dòng lệnh ngược chiều *khác* hấp thụ cascade.

#### Q16
**Hỏi:** Sweep và Run khác nhau ở đâu theo định nghĩa v2?
**Đáp:** Sweep = MỘT mức, phân xử bằng rejection. Run = ≥ 2 mức cùng phía, mỗi mức phân xử bằng acceptance, retracement < r_max, không có sự kiện cấu trúc phía đối diện. Cả hai chỉ biết sau độ trễ; một sweep có thể chuyển thành run (T1), một run kết thúc bằng sweep (T3).

#### Q17
**Hỏi:** BSL là đối ứng cho ai?
**Đáp:** Cho người muốn **bán** lượng lớn — vì lệnh có điều kiện ở BSL, khi kích hoạt, là lệnh **mua**.

#### Q18
**Hỏi:** "External liquidity" là thuộc tính của mức giá?
**Đáp:** Không — là quan hệ với một range. Cùng mức có thể external với range H1, internal với range D1. Luôn ghi range tham chiếu (lấy từ khung context).

#### Q19
**Hỏi:** Năm thành phần thường bị gộp làm một khi nói "sweep entry"?
**Đáp:** Location (POI) · Liquidity event (sweep) · Confirmation (MSS + displacement) · Entry trigger (FVG retrace) · Invalidation (vượt cực trị + buffer / acceptance lại).

#### Q20
**Hỏi:** SERR là gì và vì sao cần?
**Đáp:** Sweep Excess Reversal Rate = tỷ lệ chạm pool đối diện trước stop − p_null. Cần vì tỷ lệ thắng thô bị khoảng cách quyết định; chỉ phần vượt p_null mới là thông tin.

#### Q21
**Hỏi:** Vì sao backtest với fill lý tưởng nguy hiểm cho chiến lược sweep?
**Đáp:** Entry tại wick và stop khớp đúng giá tạo R không tồn tại. Trên random walk, fill lý tưởng cho +0.08R "edge" trong khi fill thực tế cho ≈ 0 (LS-Sim-02).

#### Q22
**Hỏi:** M5 sweep + M5 MSS ngược D1 bias — có lật bias không?
**Đáp:** Không. Ý nghĩa thuộc về swing bị phá (R7). Đó là sự kiện M5; tối đa là cảnh báo, không phải bằng chứng D1.

---

## 33. Lesson Learned

### 33.1 Bài học chính *(v1)*

- Sweep là **trigger**, không phải tín hiệu entry độc lập.
- Phân biệt **sweep (reclaim) vs break (acceptance)** là kỹ năng cốt lõi — nhầm hai cái này là nguồn thua lỗ lớn.
- Trade **phản ứng sau cú sweep** (displacement + MSS), không trade cú sweep.
- Stop hợp lý nằm **ngoài đáy/đỉnh cú sweep**, đủ dư địa để tránh double sweep.
- Sweep mạnh nhất khi ở **POI HTF + đúng premium/discount + đồng hướng bias + trong kill zone**.

### 33.2 Bài học bổ sung từ nghiên cứu v2

- "Liquidity" trên chart là **giả thuyết** về lệnh vô hình; "sweep" là **sự kiện** có thời điểm; "run" là **chuỗi** sự kiện. Ba đối tượng khác nhau.
- Hình dạng sweep xuất hiện ~một nửa số lần trên random walk; tỷ lệ "đảo về pool đối diện" bằng hình học trên random walk. **Mọi con số phải so với baseline.**
- Sweep là phép thử; dòng lệnh đến sau quyết định kết quả. MSS + displacement là cách quan sát gián tiếp dòng lệnh đó.
- Nhãn có độ trễ và có thể bị lật; ghi known_at; log append-only.
- Cỡ mẫu cần cho kết luận là hàng trăm tới hàng nghìn sự kiện — journal cá nhân phải ghi **mọi** sự kiện, không chỉ trade.

### 33.3 Quy tắc cá nhân rút ra *(v1, kèm bổ sung v2)*

- [ ] Tôi không vào lệnh trên wick; tôi chờ nến đóng để xác nhận reclaim.
- [ ] Tôi chỉ gọi là "sweep" khi có reclaim + displacement; nếu đóng nến ngoài mức, tôi coi là break thật.
- [ ] Tôi chỉ trade sweep đồng hướng Daily Bias và đúng premium/discount.
- [ ] Tôi đặt stop ngoài đáy/đỉnh cú sweep, không sát mép.
- [ ] Khi giá đóng nến lại ngoài vùng sau khi tôi vào (double sweep), tôi cắt lệnh ngay.
- [ ] *(v2)* Tôi chỉ gọi là sweep khi mức nằm trong danh sách ex-ante của tôi.
- [ ] *(v2)* Tôi không hành động ở trạng thái PENDING.
- [ ] *(v2)* Tôi không trade reversal ngược một RUN ACTIVE ở H1.
- [ ] *(v2)* Mọi thống kê tôi tự tính về sweep phải có p_null và fill thực tế.

### 33.4 Câu nhắc nhở khi trade

> **"Tôi không bắt cú quét — tôi bắt phản ứng sau cú quét. Reclaim + displacement, rồi mới vào."**

> **(v2) "Sweep là phép thử, không phải tín hiệu. Tôi chờ thị trường trả lời — rejection, rồi hậu quả cấu trúc — và tôi so câu trả lời với hình học."**

---

## 34. Mức độ thành thạo *(v1 §13)*

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa |  | Có phân biệt sweep vs break, internal vs external không? |
| Nhận diện trên chart |  | Có nhận ra reclaim + displacement theo thời gian thực không? |
| Biết khi nào bỏ qua |  | Có dám bỏ cú "có vẻ sweep" khi đóng nến ngoài mức không? |
| Kết hợp với context HTF |  | Sweep có được đặt trong bias + premium/discount + POI không? |
| Áp dụng vào trade thực tế |  | Entry có thực sự xảy ra SAU reclaim, stop ngoài sweep không? |
| Review sau trade |  | Có kiểm tra bằng dữ liệu journal thay vì cảm xúc không? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập 20–30 setup có tag `[[20-Liquidity-Sweep|Liquidity Sweep]]`.
- [ ] Review riêng: vào trên wick vs sau reclaim; stop sát mép vs ngoài POI.
- [ ] Thống kê win rate, average R theo `reclaim_confirmed` và `displacement_after_sweep`.
- [ ] Cập nhật rule chỉ khi dữ liệu đủ mẫu.
- [ ] *(v2)* Hoàn thành Event Study §26.2 A trên ít nhất một thị trường (≥ 600 sự kiện REJECTED) trước khi kết luận về edge.

---

## 35. Registers — Definitions, Rules, Hypotheses, câu hỏi nghiên cứu

### 35.1 Definitions Register (v0.1)

| ID | Định nghĩa | Mục |
|---|---|---|
| DEF-LS-01 | Liquidity reference level — mức ex-ante thỏa G1–G5 | §9.3 |
| DEF-LS-02 | Breach / PENETRATED — high > L + ε (BSL) | §20.2 |
| DEF-LS-03 | Rejection / Acceptance / Pending / Expired (ε, δ, k) | §11.3 |
| DEF-LS-04 | Liquidity Sweep | §5.6 |
| DEF-LS-05 | Liquidity Run | §6.3 |
| DEF-LS-06 | Reversal confirmation — REJECTED + MSS (Level ≥ 2 khung setup) + displacement trong m nến | §11.3, §13 |
| DEF-LS-07 | Run end — rejection tại mức kế / MSS ngược khung run / hết cửa sổ | §6.3, §19 |
| DEF-LS-08 | Event codes E0–E9 | §7.2 |

### 35.2 Rules Register (v0.1 — HEURISTIC — BACKTEST REQUIRED)

| ID | Nội dung | Mục |
|---|---|---|
| RULE-LS-001 | Danh sách mức ex-ante chốt trước phiên (known_at, LSS, p_null). Mức ngoài danh sách bị xuyên → "unlisted breach", không gọi là sweep | §2.6, §21.5 |
| RULE-LS-002 | Không phân loại tại wick; PENDING với timer k; hết k → EXPIRED | §12.3 |
| RULE-LS-003 | Trade reversal chỉ khi REJECTED + MSS (Level ≥ 2) + displacement trong m nến (= quy tắc "reclaim + displacement" của v1, thêm timer và level swing) | §11.3 |
| RULE-LS-004 | Stop ngoài cực trị sweep + buffer ≥ max(0.15·ATR, 3×spread), hoặc ngoài POI; không đặt sát wick | §22.2 |
| RULE-LS-005 | Khi có RUN ACTIVE ở H1 (hoặc khung context), không trade reversal ngược run cho tới RUN ENDED | §6, §19, Case C |
| RULE-LS-006 | NEWS SUSPEND ±15 phút quanh tin tier-1; mức tạo bởi spike tin là "dirty level" | Case E, v1 W3 |
| RULE-LS-007 | Nhãn append-only, mỗi nhãn có known_at; không sửa nhãn quá khứ | §20, §21 |
| RULE-LS-008 | Mọi thống kê về sweep báo cáo kèm p_null/SERR và dùng fill thực tế | §25 |
| RULE-LS-009 | Ý nghĩa thuộc về swing/mức bị lấy (R7); range tham chiếu ERL/IRL lấy từ khung context | §9.1, §13.3 |
| RULE-LS-010 | Bị quét tầng hai đúng kịch bản dự phòng → tối đa một lần re-entry với sequence đầy đủ (v1 W2) | §23.4 |

Khi thay đổi bất kỳ rule nào: **OLD RULE → NEW RULE → REASON → EXPECTED EFFECT → BACKTEST REQUIRED?** (project §29).

**OLD/NEW so với v1 (không có rule v1 nào bị xóa):**

| OLD (v1) | NEW (v2) | REASON | EXPECTED EFFECT | BACKTEST? |
|---|---|---|---|---|
| "Một cú quét chỉ là sweep khi reclaim + displacement" | DEF-LS-04 (sweep = rejection) + DEF-LS-06 (xác nhận = MSS + disp) + RULE-LS-003 (chỉ trade khi có cả hai) | Tách sự kiện khỏi xác nhận để đo giá trị từng lớp | Hành động không đổi; dữ liệu đo được nhiều hơn | Có (ablation A2/A3) |
| "Chờ nến đóng: trong = sweep, ngoài = break" | PENDING + timer k + quy tắc acceptance 2 close / 0.5·ATR | Nhãn tạm thời bị lật thường xuyên (LS-Sim-05) | Ít quyết định sai trong PENDING | Có |
| "Stop ngay ngoài đáy/đỉnh sweep" | RULE-LS-004 (buffer) | Replenishment tại cực trị sweep; v1 W2 | Ít bị double sweep; R:R giảm nhẹ | Có |
| — | RULE-LS-001 (mức ex-ante) | Chống hindsight | Ít "sweep" hơn, nhưng đo được | Có |

### 35.3 Hypothesis Register

| ID | Hypothesis | Biến chính | Thiết kế | Status |
|---|---|---|---|---|
| HYP-LS-001 | Sau REJECTED tại mức ex-ante, P(pool đối diện trước stop) > p_null (SERR > 0) | SERR | Event study | UNTESTED |
| HYP-LS-002 | SERR(REJECTED tại mức ex-ante) > SERR(cùng quy tắc tại mức ngẫu nhiên cùng khoảng cách) | SERR | Null comparison D1 | UNTESTED |
| HYP-LS-003 | Thêm MSS + displacement sau REJECTED làm tăng SERR và E[R] so với REJECTED đơn thuần | SERR, E[R] | Ablation A2/A3 | UNTESTED |
| HYP-LS-004 | Bối cảnh HTF ngược hướng xuyên (bias ex-ante, ở POI) làm tăng SERR | SERR theo nhóm | Event study phân tầng | UNTESTED |
| HYP-LS-005 | Sự kiện trong killzone có SERR cao hơn ngoài killzone, sau kiểm soát khoảng cách và ATR | SERR theo giờ | Event study | UNTESTED |
| HYP-LS-006 | EQH bị xuyên trong T nhiều hơn đỉnh đơn cùng khoảng cách | P(breach in T) | Event study vs LS-Sim-07 | UNTESTED |
| HYP-LS-007 | Sau khi xuyên mức LSS cao, tốc độ/độ dài chuyển động ngay sau mức lớn hơn mức LSS thấp (dấu vết stop cluster kiểu Osler) | pen_speed, post-breach excursion | Event study (cần tick/M1) | UNTESTED |
| HYP-LS-008 | Độ sâu xuyên (pen_depth_atr) khác phân phối giữa sự kiện về sau REJECTED và ACCEPTED (có thông tin ex-ante?) | pen_depth_atr | Event study | UNTESTED |
| HYP-LS-009 | reclaim_body_ratio ≥ 0.5 dự báo R1 tốt hơn < 0.5 (v1 W1) | P(R1) | Event study | UNTESTED |
| HYP-LS-010 | E[R](sweep + MSS) > E[R](sweep only) và > E[R](MSS only) | E[R] | Ablation A1/A2 | UNTESTED |
| HYP-LS-011 | Flip rate của nhãn REJECTED tại mức LSS cao thấp hơn null (LS-Sim-05) | F(h) | Event study | UNTESTED |
| HYP-LS-012 | Khi HTF đồng hướng với phía bị lấy và đã có acceptance tại L₂, P(L₃ trước mất HL) > p_null (quy tắc "run" của cộng đồng) | P(next pool) | Event study | UNTESTED |
| HYP-LS-013 | Exhaustion score ES ≥ 3 dự báo run kết thúc trong N nến | P(run end) | Event study | UNTESTED |
| HYP-LS-014 | SMT divergence tại sweep có likelihood ratio ≠ 1 cho R1 | LR | Event study (cặp tương quan) | UNTESTED |
| HYP-LS-015 | Khi có pool nông phía trên pool sâu trùng POI HTF, P(pool sâu bị lấy trước reversal) > baseline (v1 W2) | P | Event study | UNTESTED |
| HYP-LS-016 | Độ sâu xuyên chuẩn hóa ATR lớn hơn trong giờ thanh khoản mỏng (toy LS-Sim-04) | pen_depth_atr theo giờ | Event study | UNTESTED |
| HYP-LS-017 | Ngày OPEX làm giảm SERR của sweep trên NQ (v1 Case B) | SERR | Event study phân tầng | UNTESTED |
| HYP-LS-018 | Xuyên vượt 2.5–3 SD của Asia range/CBDR dự báo acceptance (v1 §7.3) | P(ACC) | Event study | UNTESTED |

### 35.4 Câu hỏi nghiên cứu — theo ưu tiên cho giai đoạn foundation

**Ưu tiên cao (làm được với dữ liệu OHLC M1/M5 và Python):**
1. Event study trên EURUSD và NQ: phân phối E-code, SERR của REJECTED so với 0 và so với mức ngẫu nhiên (HYP-LS-001, 002).
2. Flip rate thực tế vs null (HYP-LS-011) — rẻ, trả lời câu "nhãn sweep có mang thông tin không".
3. Ablation A0/A1/A2 trên tập backtest ICT 2022 hiện có trong `04 - Backtesting/` (HYP-LS-003, 010) — kiểm tra trước: tập hiện có có đủ trường để tái dựng không?
4. Kiểm tra kỷ luật: tỷ lệ "unlisted breach" trong journal 8 tuần tới — bao nhiêu "sweep" của bạn là mức đã có trong danh sách trước phiên?

**Ưu tiên trung bình:**
5. EQH vs đỉnh đơn (HYP-LS-006); tốc độ sau xuyên theo LSS (HYP-LS-007, cần M1/tick).
6. Killzone (HYP-LS-005); bối cảnh HTF (HYP-LS-004).
7. Run continuation (HYP-LS-012) và exhaustion (HYP-LS-013).

**Ưu tiên thấp / khám phá:**
8. SMT LR (HYP-LS-014); OPEX (HYP-LS-017); SD của Asia range (HYP-LS-018); độ sâu theo giờ (HYP-LS-016).

### 35.5 Liên kết trong vault

| Chủ đề | Note |
|---|---|
| Liquidity nền tảng | [[19-Liquidity]] · [[19-Liquidity#7. Buy-Side Liquidity (BSL)\|Buy-side Liquidity]] · [[19-Liquidity#8. Sell-Side Liquidity (SSL)\|Sell-side Liquidity]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]] · [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]] · [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]] · [[21-Liquidity-Void]] |
| Draw on Liquidity | [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] · [[52-Draw-on-Liquidity-DOL-Nghien-cuu-chuyen-sau-SOP-dau-ngay-Confluence]] · [[53-Swing-Density-va-DOL-Precedence-Chon-Draw-khi-cau-truc-day-swing]] · [[56-Draw-on-Liquidity-DOL-Ontology-Microstructure-Failure-Model-va-Backtest]] · [[58-Draw-on-Liquidity-DOL-Tong-hop-Deep-Dive-v0.2-Beginner-Friendly]] |
| Cấu trúc & xác nhận | [[21-Market-Structure-Shift]] · [[05-BOS-Break-of-Structure]] · [[09-Change-of-Character]] · [[50-Displacement-In-Depth]] · [[13-FVG-Fair-Value-Gap]] · [[48-1st-Presented-Fair-Value-Gap]] · [[15-Inducement]] · [[54-Thuat-toan-phat-hien-swing-turning-point-Directional-Change-va-Nen-tang-dinh-luong]] |
| Range & vị trí | [[12-Dealing-Range]] · [[57-Dealing-Range-Nghien-cuu-chuyen-sau-Swing-Significance-Selection-Algorithm-Backtest]] · [[37-Re-mapping-Dealing-Range-sau-Displacement]] · [[27-Premium-Discount]] |
| Bối cảnh & thời gian | [[59-Daily-Bias]] · [[02-AMD]] · [[18-Kill-Zones]] · [[40-Macro-Times]] · [[42-SMT-Divergence]] · [[31-Standard-Deviation]] · [[08-Central-Bank-Dealers-Range]] |
| Mô hình | [[01 - ICT 2022 Model]] · [[33-Turtle-Soup]] · [[45-ICT-Reversal-Patterns]] · [[49-Confirmation-Timeframe-Timeframe-Layering-Khu-nhieu-MSS-trong-2022-Model]] |
| Mistakes | [[02-Mistake-Enter-before-liquidity-sweep]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]] · [[08-Mistake-Weak-Displacement]] · [[06-Mistake-Not-Have-Market-Structure-Shift]] · [[04-Mistake-FOMO-Entry]] |

**Nơi lưu register (đề xuất theo cấu trúc Claude Project):** DEF-LS/RULE-LS → `/ICT/17_Rules/`; HYP-LS → `/ICT/16_Hypotheses/`; Event/Trade study → `/ICT/13_Backtesting/`; Case A–F → `/ICT/14_Case_Studies/` (tag `hypothetical`).

---

## Tài liệu tham khảo

**Market microstructure & bằng chứng thực nghiệm (Tier 1–2)**

- BIS Markets Committee (2017). *The sterling 'flash event' of 7 October 2016.* Bank for International Settlements. https://www.bis.org/publ/mktc09.htm
- Bershova, N., & Rakhlin, D. (2013). *The non-linear market impact of large trades: evidence from buy-side order flow.* Quantitative Finance, 13(11), 1759–1778. https://ideas.repec.org/a/taf/quantf/v13y2013i11p1759-1778.html
- Bouchaud, J.-P., Gefen, Y., Potters, M., & Wyart, M. (2004). *Fluctuations and response in financial markets: the subtle nature of 'random' price changes.* Quantitative Finance, 4(2). https://ideas.repec.org/p/sfi/sfiwpa/0307332.html
- Bouchaud, J.-P., Bonart, J., Donier, J., & Gould, M. (2018). *Trades, Quotes and Prices: Financial Markets Under the Microscope.* Cambridge University Press.
- Brunnermeier, M. K., & Pedersen, L. H. (2005). *Predatory Trading.* Journal of Finance, 60(4), 1825–1863. https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.2005.00781.x
- Cont, R., Kukanov, A., & Stoikov, S. (2014). *The Price Impact of Order Book Events.* Journal of Financial Econometrics, 12(1), 47–88.
- Farmer, J. D., Gerig, A., Lillo, F., & Waelbroeck, H. (2013). *How efficiency shapes market impact.* Quantitative Finance, 13(11). https://arxiv.org/pdf/1102.5457
- Fett, N., & McPhail, L. (2017). *Stop Orders in Select Futures Markets.* U.S. Commodity Futures Trading Commission, Office of the Chief Economist. https://www.cftc.gov/sites/default/files/Stoploss_final_ada.pdf
- Garzarelli, F., Cristelli, M., Pompa, G., Zaccaria, A., & Pietronero, L. (2014). *Memory effects in stock price dynamics: evidences of technical trading.* Scientific Reports, 4, 4487. https://www.nature.com/articles/srep04487
- Harris, L. (2003). *Trading and Exchanges: Market Microstructure for Practitioners.* Oxford University Press.
- Kavajecz, K. A., & Odders-White, E. R. (2004). *Technical Analysis and Liquidity Provision.* Review of Financial Studies, 17(4), 1043–1071. https://ideas.repec.org/a/oup/rfinst/v17y2004i4p1043-1071.html
- Kyle, A. S. (1985). *Continuous Auctions and Insider Trading.* Econometrica, 53(6), 1315–1335.
- Moro, E., Vicente, J., Moyano, L. G., Gerig, A., Farmer, J. D., Vaglica, G., Lillo, F., & Mantegna, R. N. (2009). *Market impact and trading profile of hidden orders in stock markets.* Physical Review E, 80, 066102.
- Osler, C. L. (2003). *Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.* Journal of Finance, 58(5), 1791–1819.
- Osler, C. L. (2005). *Stop-loss orders and price cascades in currency markets.* Journal of International Money and Finance, 24(2), 219–241. https://www.newyorkfed.org/research/staff_reports/sr150.html

**Phương pháp, nhận thức & thống kê**

- Fischhoff, B. (1975). *Hindsight ≠ foresight: The effect of outcome knowledge on judgment under uncertainty.* Journal of Experimental Psychology: Human Perception and Performance, 1(3).
- Schelling, T. C. (1960). *The Strategy of Conflict.* Harvard University Press (focal points).
- (Kiểm định nhiều giả thuyết, data snooping, overfitting — xem references của [[59-Daily-Bias]] và DR-v0.1.)

**Trading literature (Tier 3)**

- Connors, L. A., & Raschke, L. B. (1995). *Street Smarts: High Probability Short-Term Trading Strategies.* M. Gordon Publishing (Turtle Soup).

**ICT community documentation (Tier 3–4 — chỉ dùng cho định nghĩa/cách dùng, không phải bằng chứng)**

- innercircletrader.net — *Liquidity Sweep vs Liquidity Run*: https://innercircletrader.net/tutorials/ict-liquidity-sweep-vs-liquidity-run/
- TradingFinder — *ICT Liquidity Sweep & Liquidity Run*: https://tradingfinder.com/education/forex/ict-liquidity-sweep-liquidity-run/

**Bối cảnh sự kiện (tin tức, Tier 4)**

- Báo cáo về đợt thanh lý crypto ngày 10/10/2025 (~19 tỷ USD), ví dụ: Forbes (13/10/2025), FTI Consulting — dùng làm ví dụ về liquidation cascade, không phải bằng chứng thống kê.

**Tài liệu nội bộ**

- Note v1 của chính file này (sao lưu: `Claude outputs/backups/20-Liquidity-Sweep.2026-10-06.md.bak`).
- DR-v0.1 (Claude Project, `ICT/03_Dealing_Range/`) — R7, known_at, martingale null.
- [[59-Daily-Bias]] v2 — p_null có cửa sổ thời gian, ba lớp process/information/story.

---

## Phụ lục A — Ghi chú mô phỏng

| Figure | Mô hình | Kích thước | Kết quả chính |
|---|---|---|---|
| **LS-Sim-01** | Random walk Gaussian, bước 1 phút, không drift; nến M5/M15/H1/H4/D1; swing = fractal 5 hoặc 11 nến (n = 2, 5); sự kiện = nến đầu tiên có high > swing high đã xác nhận | 3,000,000 phút; 58,904 sự kiện (M5, n = 2) … 115 (D1, n = 5) | Tỷ lệ close lại dưới mức: 29% M5, 38% M15, 44% H1, 49% H4, 52% D1 (n = 2); giới hạn liên tục 50%. Panel B: nhãn M5 vs nến H1 chứa nó bất đồng 38.7% (P(H1 reject \| M5 accept) = 38.3%; P(H1 accept \| M5 reject) = 39.6%) |
| **LS-Sim-02** | Bước 10 giây (σ phút = 1), nến M15 (90 bước); swing high n = 3; short tại close nến xuyên; stop = high nến xuyên + 0.1 ATR(14); target = swing low đã xác nhận gần nhất chưa bị lấy; phân xử trên đường 10 giây | 24,000,000 bước; 23,140 sự kiện (10,585 "đóng lại bên trong", 12,555 "đóng vượt") | "Sweep": thắng 20.6% vs p_null TB 19.4%; R:R trung vị 5.1; E[R] fill thực tế +0.019R (SE 0.027); fill lý tưởng +0.078R (SE 0.026). "Break": thắng 7.5% vs 6.7%; E[R] fill thực tế −0.036R (SE 0.048). Định nghĩa: giảm ≥ 1 ATR trong 20 nến 73%; close dưới low nến sweep trong 10 nến 66% |
| **LS-Sim-03** | Toy propagator: p_t = noise_t + Σ G(t−s)q_s; G(τ) = κ[γ + (1−γ)e^(−τ/τ₀)], κ = 0.05, γ = 0.35, τ₀ = 12; 70 đơn vị buy-stop trên 14 mức; nhiễu σ = 0.15/phút | 300 phút × 3 kịch bản (cùng seed) | Đỉnh vượt L ≈ 2.6–3.0 điểm trong cả ba; sau 60 phút: A −1.9, B +3.6, C −6.8 so với L |
| **LS-Sim-04** | Toy sổ lệnh tĩnh: độ sâu D/tick, stop S phân bố mũ (λ tick), đẩy ban đầu 1 tick | Giải tích/số | Ngưỡng S/(D·λ) ≈ 1 (rời rạc: ~1.1–1.2); S = 120, λ = 6: D = 4 → 30 tick; D ≈ 7.6 → 15; D ≈ 11 → 8; D ≥ ~19 → 1 |
| **LS-Sim-05** | Bước 10 giây, nến M5 (30 bước), swing n = 3; quy tắc v0.1 (REJECTED: close < L − 0.25·ATR; ACCEPTED: 2 close > L hoặc close > L + 0.5·ATR) | 14,400,000 bước; 40,897 sự kiện | PENDING tại nến 0: 59%; nến 1: 12%; nến 3: 0.8%. Flip (REJ→ACC): 29% / 44% / 58% / 70% / 78% trong 3 / 6 / 12 / 24 / 48 nến; ACC→REJ tương tự |
| **LS-Sim-06** | Bước 1 phút, nến H1, swing n = 2; sự kiện "lấy pool" gộp theo nến; nến lấy cả hai phía kết thúc run; drift 0, 0.05, 0.15 σ/nến | 6,000,000 phút mỗi mức drift; ~5,800–6,600 run | Không drift: P(≥2) 64%, P(≥3) 43%, P(≥5) 19%, TB 2.9. Drift 0.15: BSL TB 3.5 (P≥3 54%), SSL TB 1.9 (P≥3 23%) |
| **LS-Sim-07** | Bước 1 phút, nến M15, swing n = 3; EQH = hai swing high liên tiếp cách ≥ 6 nến, không có high cao hơn ở giữa, \|ΔH\| ≤ tol·ATR | 6,000,000 phút; 1,107 EQH (tol 0.1) vs 32,753 đỉnh đơn | EQH / 1,000 nến: 1.5 / 2.8 / 5.4 / 8.0 (tol 0.05/0.1/0.2/0.3); P(xuyên trong 40 nến) theo khoảng cách: hai đường trùng trong CI |
| **Bảng power §26.4** | Xấp xỉ chuẩn một mẫu, α = 0.05 hai phía, power 80% | Giải tích | Xem bảng |

**Giới hạn chung:** lợi nhuận Gaussian không có đuôi dày và volatility clustering; không có hồ sơ biến động theo giờ (trừ khi ghi); bước rời rạc làm cực trị trong nến bị ước lượng thấp (đó chính là lý do LS-Sim-01 phụ thuộc số bước/nến); toy model 03/04 có tham số minh họa, không hiệu chỉnh từ dữ liệu. Các kết quả mô tả **mô hình null**, không mô tả thị trường thật.

**Tái lập:** script Python (numpy/matplotlib) và kết quả JSON nằm ở `Claude outputs/liquidity-sweep-v2-sims/` (seed cố định trong từng script).

---

## Changelog

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| v1 | 2026-06-22 → 2026-07-28 | Note gốc: mục 1–13 theo template concept, War Stories W0–W6, mục 14–18 bổ sung (phân định, cơ chế, phản biện, edge cases, case studies) |
| v2 | 2026-10-06 | Hợp nhất với *Liquidity Sweep / Liquidity Run — Deep Research v0.1*. Thêm: nền tảng vi cấu trúc (§1–4), định nghĩa vận hành DEF-LS-01…08, Liquidity Run (§6), taxonomy E0–E9 (§7), vòng đời (§8), LSS (§9.3), toy model (§10), cây kết quả (§11), 5 biến thể sweep/breakout (§12), quan hệ với MSS/displacement/FVG/POI/range/DOL (§13–19), máy trạng thái + pseudocode (§20), real-time vs ex-post (§21), cây quyết định D1→H1→M5 (§22), Case A–F mới (§23.2), counterexamples CX1–CX14 (§24.1), định lượng (§25), backtest (§26), registers (§35). 18 sơ đồ `LS-Deep-*`, 7 hình mô phỏng `LS-Sim-*`. Gắn nhãn cho các claim của v1; case v1 §18 đánh dấu "chưa xác minh". Sửa link hỏng (xem dưới). Thêm `prerequisites`, cập nhật `aliases`, `tags`, `common_mistakes`. **Không rule nào của v1 bị xóa** — thay đổi trình bày dạng OLD/NEW (§35.2) |

**Link hỏng đã sửa:** `[[Fair Value Gap]]` → `[[13-FVG-Fair-Value-Gap|Fair Value Gap]]`; `[[Order Block]]` → `[[25-OB-Order-Block|Order Block]]`; `[[Optimal Trade Entry]]` → `[[26-OTE-Optimal-Trade-Entry|Optimal Trade Entry]]`; `[[Liquidity Sweep]]` → `[[20-Liquidity-Sweep|Liquidity Sweep]]`; `[[04 - Backtesting]]` → thư mục `04 - Backtesting/`. Trong `common_mistakes` của v1, ba link `[[Mistake - Trade The Wick Immediately]]`, `[[Mistake - Confuse Real Break With Sweep]]`, `[[Mistake - Entry Before Reclaim]]` trỏ tới note không tồn tại → thay bằng các note mistake có thật gần nghĩa nhất. **Đề xuất:** tạo note `06 - Mistake Database/14-Mistake-Confuse-Breakout-With-Sweep.md` (lỗi này chưa có note tương ứng).

**Hình trong vault không được nhúng (có chủ đích):** `Liquidity-Sweep-EdgeB-DepthThreshold.svg`, `…-EdgeB-EngineeredEQH.svg`, `…-EdgeB-OpeningGapSweep.svg`, `…-EdgeB-SessionSequencingTemplate.svg`, `…-EdgeB-SweepOfSweep.svg`, `…-CaseStudy-B1-ES-EngineeredTrap-Loss.svg`, `…-CaseStudy-B2-EURUSD-SessionTemplate-Win.svg` — các hình này (từ một phiên trước, không được note v1 nhúng) chứa **thống kê "backtest" không có nguồn** (ví dụ "Reversal sau sweep 73% (N=210)", "N=126 ngày"). Theo quy tắc không dùng số liệu chưa xác minh, chúng không được đưa vào note. `Liquidity-Sweep-Sec-01…05.svg` là bản trùng ý với các hình v1 đã nhúng. Các file vẫn nằm nguyên trong `attachments/`.

**Bản đồ di chuyển nội dung v1 → v2**

| v1 | v2 |
|---|---|
| Tóm tắt 1 câu, Nguyên tắc cốt lõi | Viết lại; nguyên tắc v1 giữ trong callout "Nguyên tắc cốt lõi (v2)" |
| §1 Định nghĩa (khái niệm, bản chất, sweep vs break, mục đích, câu hỏi) | §5.9 (nguyên văn + chú thích) |
| §1 "Không phải là gì" | §5.9 (+3 dòng v2) |
| §2 Các loại/trạng thái (bảng + tip) | §7.3 |
| §2 Khi nào giá trị cao / nên bỏ qua | §22.8 |
| §3 Cấu trúc nhận diện (dấu hiệu, ma trận, điều kiện) | §22.9 |
| §4 Quy trình đa khung + mẫu ghi nhanh | §22.2 |
| §5 Quy tắc xác nhận / vô hiệu (hợp lệ khi, vô hiệu khi, bảng thành công/thất bại, double sweep) | §12.4 |
| §6 Ví dụ chart & sequence | §23.1 |
| §7.1 SMT · §7.2 Thời gian · §7.3 Độ sâu & tốc độ · §7.4 Turtle Soup · §7.5 LTF · §7.6 Best practices | §22.4 · §22.3 · §10.6 · §22.5 · §10.5 · §22.11 |
| War Stories W0 · W1 · W2–W6 | §4.5 (nguyên văn + rà soát) · §11.4 · §23.4 |
| §8 Checklist A/B/C | §27 (+ D v2) |
| §9 Lỗi thường gặp | §28.1 (+ §28.2 v2) |
| §10 Câu hỏi · §11 Flashcards Q1–Q11 | §31.1 · §32.1 (+ Q12–Q22) |
| §12 Lesson learned · §13 Thành thạo | §33 · §34 |
| §14 Phân định Sweep/IDM/MSS | §13.4 |
| §15 Cơ chế (bullets, khung lý thuyết, 3 thị trường) | §10.4 · §29.4 · §10.7 |
| §16 Phản biện (1, 2, 3) | §29.1 · §29.2 · §29.3 |
| §17 Edge cases EC1–EC7 | §24.2 |
| §18 Case studies A–D | §23.3 (đánh dấu chưa xác minh) |
