---
type: ict-concept
concept: Reaper Inversion Fair Value Gap
aliases:
  - Reaper Inversion Fair Value Gap
  - Reaper IFVG
  - Reaper FVG
tags:
  - trading/ict/concept
  - trading/study
  - "#pd-array"
  - "#entry-model"
status: seed
category: Entry Model
last_reviewed: 2026-07-09
created: 2026-07-09
updated: 2026-07-09
---

# Reaper Inversion Fair Value Gap

> [!summary] Tóm tắt 1 câu
> **Reaper IFVG là một Inversion Fair Value Gap hình thành NGAY TRƯỚC một Breaker Block, nằm sâu bên trong chân giá của Breaker đó — đây mới là điểm vào thật của tổ chức, là mức giá thị trường chạm tới SAU KHI những trader vào lệnh sớm tại Breaker đã bị trừng phạt.**

> [!important] Nguyên tắc cốt lõi
> Đám đông tin rằng cứ chạm Breaker là giá tiếp diễn ngay, nên họ vào lệnh tại Breaker. Nhưng tổ chức cần **giá tốt hơn**, nên thị trường thường **chạy XUYÊN QUA Breaker** (vào discount với setup bull, vào premium với setup bear), tạo drawdown, quét stop của phe vào sớm — nó "gặt" (reap) chính những người này để lấy thanh khoản — rồi mới đảo chiều từ **Reaper IFVG**, mức nằm sâu hơn trong dealing range với pricing tổ chức tốt hơn. Vì thế: **Breaker = ALERT (cảnh báo), Reaper IFVG = ENTRY (điểm vào)**. Chạm được Reaper IFVG mới chỉ là *cảnh báo*; entry vẫn cần confirmation LTF (MSS / displacement / rejection / sweep). Concept này xây trên nền [[04 - Breaker Block]] và [[17 - Inverse Fair Value Gap - iFVG]].

---

## 1. Định nghĩa

**Nền tảng FVG → IFVG → Reaper.**

- **FVG (Fair Value Gap):** vùng mất cân bằng ba nến do displacement để lại — xem [[13 - FVG  - Fair Value Gap]].
- **IFVG (Inversion FVG):** một FVG bị giá **đóng xuyên qua** rồi **đảo vai trò** — FVG hỗ trợ bị phá thành kháng cự và ngược lại. Xem [[17 - Inverse Fair Value Gap - iFVG]].
- **Reaper IFVG:** một IFVG *đặc biệt về vị trí* — nó nằm **ngay trước** và **bên trong chân giá** tạo ra Breaker Block. Nó không phải một loại gap mới về cấu tạo; nó là **một IFVG được định vị đúng chỗ chiến lược**: sâu hơn Breaker, trong đúng vùng Premium/Discount.

**Khái niệm:** Trong một **bullish Breaker** setup, giá tạo một chân đẩy lên (chân giá Breaker). Bên trong chân đó, ở phần **discount**, có một IFVG. Đây là **Reaper IFVG** — mức giá tổ chức thực sự muốn được lấp. Đám đông thấy Breaker (mức hiển nhiên, cao hơn) và vào lệnh; giá lại chạy sâu xuống Reaper IFVG mới đảo chiều. Bearish là gương phản chiếu trong premium.

![[Reaper-Advanced-Anatomy.svg|697]]

*Bullish Reaper: giá chạm Breaker (mồi nhử) → chạy XUYÊN qua Breaker vào discount (drawdown, quét stop đám đông) → tìm support tại Reaper IFVG nằm sâu hơn + MSS → đảo chiều lên về prev highs / BSL. Stop nằm DƯỚI Reaper IFVG, không phải tại Breaker.*

**Nó giúp trả lời câu hỏi nào trên chart?**

- Tôi nên vào lệnh **chính xác ở đâu** quanh một Breaker — ngay tại Breaker hay chờ sâu hơn?
- Vì sao tôi cứ vào Breaker "đúng hướng" mà vẫn bị stop-out ngay trước khi giá chạy đúng như dự đoán?
- Đâu là mức có **pricing tổ chức tốt nhất** trong chân giá này để entry có R lớn, stop an toàn?

### Reaper IFVG KHÔNG phải là gì

- **Không phải** một loại gap mới — nó vẫn là IFVG, chỉ khác ở **vị trí chiến lược** (trong chân giá Breaker + đúng P/D).
- **Không phải** bản thân Breaker Block — Breaker là mức hiển nhiên/nông hơn; Reaper là mức ẩn/sâu hơn. Gần cùng chỗ nhưng giao dịch khác hẳn.
- **Không phải** trigger vào lệnh — chạm Reaper IFVG là *alert*; vẫn cần confirmation LTF.
- **Không** hợp lệ nếu IFVG nằm **ngoài** chân giá Breaker hoặc **sai** vùng P/D (bull mà ở premium, bear mà ở discount).

---

## 2. Cơ chế sâu — vì sao giá "reap" trader vào Breaker sớm

Đây là phần "why" quyết định. Hiểu cơ chế mới đủ kiên nhẫn để **không** bấm nút tại Breaker.

**(a) Institutions cần pricing tốt hơn.** Lệnh tổ chức có khối lượng lớn; họ không thể lấp toàn bộ tại mức hiển nhiên (Breaker) mà không đẩy giá bất lợi cho chính họ. Họ muốn giá **rẻ hơn** (bull) hoặc **đắt hơn** (bear). Vì vậy engine phân phối giá thường đẩy thị trường **vượt qua** Breaker để chạm mức pricing thật — chính là Reaper IFVG nằm sâu hơn trong dealing range ([[12 - Dealing Range]], [[27 - Premium Discount]]).

**(b) Liquidity harvest — thu hoạch thanh khoản.** Khi giá chạm Breaker, đám đông vào lệnh và đặt stop ngay dưới (bull). Cú chạy xuyên Breaker **quét đúng cụm stop này** cộng với các sell-stop/breakout dưới đó. Đây là nhiên liệu (thanh khoản đối ứng) để tổ chức lấp lệnh lớn — xem [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]. Sau khi thanh khoản đã bị "gặt", không còn nhiên liệu cho chân đi tiếp → giá đảo từ Reaper IFVG.

**(c) Vì sao gọi là "Reaper".** Thị trường "gặt" (reaps) chính những trader vào quá sớm tại Breaker: nó vượt Breaker để tạo drawdown, kích hoạt stop, gom thanh khoản từ phe vào sớm, rồi mới đảo chiều từ điểm vào thật. Trong setup bull, giá có thể trade **dưới** Breaker vào discount trước khi có support tại Reaper IFVG; trong setup bear, **trên** Breaker vào premium trước khi có resistance.

> [!info] Câu thần chú
> *"The Breaker attracts the crowd. The Reaper collects the crowd. Then the real move begins."* — Breaker hút đám đông vào; Reaper gặt đám đông (lấy thanh khoản của họ); sau đó chân đi thật mới bắt đầu. Nếu bạn vào tại Breaker, bạn thuộc nhóm "bị gặt". Nếu bạn chờ Reaper, bạn đi cùng bên gặt.

**(d) Vì sao đây là lỗi phổ biến.** Trader học Breaker thường mặc định "mọi Breaker tiếp diễn ngay lập tức". Họ long tại bullish Breaker, giá tiếp tục giảm, quét stop, **rồi** đảo chiều đúng như họ nghĩ — từ một mức sâu hơn. Cùng một phân tích hướng đi đúng, nhưng entry sai chỗ biến một cú lẽ ra thắng thành một cú thua. Reaper IFVG chính là lời giải cho nghịch lý "đúng hướng mà vẫn thua".

---

## 3. Bối cảnh sử dụng

### Khi nào Reaper IFVG có giá trị cao?

- [ ] Có **HTF bias rõ** (theo [[12 - Daily Bias]] / top-down) và cấu trúc đồng thuận hướng vào lệnh
- [ ] Đã vẽ **dealing range** và xác định vùng Premium/Discount ([[12 - Dealing Range]], [[27 - Premium Discount]])
- [ ] Có một **Breaker Block hợp lệ** (OB bị phá vai trò) làm mốc ALERT
- [ ] Tồn tại một **IFVG bên trong chân giá Breaker**, đúng vùng P/D (bull→discount, bear→premium)
- [ ] Giao dịch trên instrument **thanh khoản cao, delivery sạch** (NQ, ES, EURUSD, GBPUSD, XAUUSD)
- [ ] Có kế hoạch **target** rõ (prev highs/lows, BSL/SSL, HTF liquidity — [[16 - Internal & External Range Liquidity (IRL & ERL)]])

### Khi nào nên bỏ qua?

- [ ] **Không có HTF bias** — trade Reaper ngược/không bias là đoán mò
- [ ] IFVG **nằm ngoài** chân giá Breaker hoặc **sai** vùng P/D → không phải Reaper hợp lệ
- [ ] Instrument **thanh khoản thấp** (cặp exotic, low-volume) — sweep/inversion nhiễu, dễ giả
- [ ] Giá **chưa** tới discount/Reaper IFVG (đừng mua từ Breaker vì sốt ruột)
- [ ] Tới IFVG nhưng **chưa có confirmation** LTF (reaching = alert, chưa phải signal)

---

## 4. Reaper IFVG vs Breaker Block

![[Reaper-Advanced-vs-Breaker.svg|697]]

Hai mức gần như **cùng một chỗ** nhưng giao dịch **hoàn toàn khác**. Breaker là mức hiển nhiên, đông đúc, nơi retail vào (mồi nhử). Reaper IFVG là vùng imbalance sâu hơn trong cùng chân giá, nơi tổ chức được lấp (bẫy/entry).

| Tiêu chí | Breaker Block | Reaper IFVG |
|---|---|---|
| Vai trò | **Mồi nhử (bait)** — hút đám đông | **Bẫy / Entry thật (trap)** — tổ chức lấp |
| Vị trí | Mức hiển nhiên, **nông hơn** | **Sâu hơn** trong chân giá, đúng P/D |
| Ai vào ở đây | Retail vào sớm → bị stop | Smart money → đảo chiều từ đây |
| Dùng để | **ALERT** (cảnh báo, chuẩn bị) | **ENTRY** (điểm vào, sau confirmation) |
| Pricing | Kém (giá đám đông) | Tốt (giá tổ chức) |
| Kết cục nếu vào đây | Thành thanh khoản, drawdown | Vào đúng nhịp đảo |

> [!tip] Nguyên tắc thao tác
> Coi **Breaker là chuông báo thức**: khi giá chạm Breaker, bạn *chuẩn bị*, không *bấm*. Bạn hạ khung, chờ giá đi sâu tới Reaper IFVG, và chỉ vào khi có confirmation. Kiên nhẫn giữa Breaker và Reaper chính là biên độ drawdown mà bạn né được.

---

## 5. Bullish vs Bearish Reaper

![[Reaper-Advanced-BullBear.svg|697]]

**Bullish Reaper (đảo lên):** Trong dealing range có HTF bias bull. Bullish Breaker (một bearish OB bị phá lên) là mức trên. Reaper IFVG nằm **DƯỚI Breaker, trong discount**. Giá chạy xuống xuyên Breaker vào discount, tìm support tại Reaper IFVG → long.

**Bearish Reaper (đảo xuống):** HTF bias bear. Bearish Breaker (một bullish OB bị phá xuống) là mức dưới. Reaper IFVG nằm **TRÊN Breaker, trong premium**. Giá chạy lên xuyên Breaker vào premium, gặp resistance tại Reaper IFVG → short.

> [!tip] Cách nhớ chiều
> Reaper luôn nằm **sâu hơn** về phía "giá tốt cho tổ chức": bull thì tổ chức muốn mua rẻ → Reaper ở **discount** (dưới Breaker); bear thì tổ chức muốn bán đắt → Reaper ở **premium** (trên Breaker). Nếu bạn thấy mình định mua ở premium hoặc bán ở discount, bạn đang làm ngược Reaper.

---

## 6. Golden Rule — điều kiện hợp lệ

![[Reaper-Advanced-GoldenRule.svg|697]]

> [!important] Golden Rule
> Một **Reaper IFVG luôn là FVG/IFVG nằm BÊN TRONG chân giá của Breaker**; trong thị trường bullish nó ở **DISCOUNT**, trong thị trường bearish nó ở **PREMIUM**. Nếu FVG **không** nằm trong chân giá Breaker **và/hoặc không** ở đúng vùng P/D → **KHÔNG** phải Reaper IFVG hợp lệ.

Hai điều kiện phải đúng **đồng thời**:

1. **Trong chân giá Breaker.** Xác định chân đẩy (leg) tạo ra Breaker; IFVG phải nằm trong khoảng giá của chân đó, ngay trước Breaker. IFVG ở một chân khác, hay ngoài chân này, không tính.
2. **Đúng vùng Premium/Discount.** Bull → IFVG phải ở discount (dưới equilibrium của range). Bear → premium. Một IFVG "trong chân" nhưng ở sai nửa P/D là cờ đỏ.

Bên trái (hợp lệ): IFVG nằm trong chân giá **và** ở discount → ✓. Bên phải (sai): IFVG nằm ngoài chân giá, ở premium → ✕. Đây là lỗi đánh dấu phổ biến nhất khiến trader "thấy Reaper ở khắp nơi".

---

## 7. Reaper IFVG đa khung (MTF)

![[Reaper-Advanced-MTF.svg|697]]

Quy trình lồng khung (top-down) — xem thêm [[32 - Top-down Analysis (Multiple Timeframes)]]:

1. **H1 / M15 — bias & map.** Xác định HTF bias, vẽ dealing range, đánh dấu Breaker và Reaper IFVG. Đây là tầng quyết định **hướng** và **vùng POI**.
2. **M5 / M3 — confirmation.** Khi giá đi vào vùng Reaper IFVG, hạ khung để chờ tín hiệu vào: **liquidity sweep** ([[20 - Liquidity Sweep]]) + **rejection**, **MSS** ([[21 - Market Structure Shift]]) và **displacement** lên, hoặc **CISD** ([[41 - Change in State of Delivery]]). Confirmation LTF biến "giá tới POI" thành "điểm vào có trigger".

> [!tip] Khung trên quyết định hướng, khung dưới quyết định giờ
> Đừng để một tín hiệu LTF kéo bạn đi ngược HTF bias. LTF chỉ dùng để *canh giờ vào* tại Reaper IFVG, không dùng để *đổi hướng*. Nếu HTF bull nhưng ở LTF không có MSS lên tại IFVG → đứng ngoài, đó là alert chưa thành signal.

---

## 8. Logic Stop Loss

![[Reaper-Advanced-StopLogic.svg|697]]

Stop đặt **DƯỚI Reaper IFVG** (bull) hoặc **TRÊN Reaper IFVG** (bear), hoặc dưới/trên **swing gần nhất** — **KHÔNG** đặt bên trong gap.

**Vì sao?** Một cú retest hợp lệ thường có **wick chọc sâu vào gap** (thậm chí quét tới CE / Mean Threshold — [[10 - Consequent Encroachment (Mean Threshold)]]) trước khi bật lên. Nếu stop nằm **trong** gap, nó nằm ngay trên đường đi tự nhiên của wick retest → bị quét oan **ngay trước** khi giá đảo chiều thật. Đây đúng là kịch bản "đúng hướng, đúng vùng, nhưng thua vì stop sai chỗ".

**Đánh đổi:** stop dưới gap rộng hơn một chút, nhưng **sống sót** qua cú retest để giữ được lệnh cho cú đảo thật. Bù lại bằng entry sắc hơn ở LTF (chờ sweep + MSS thay vì vào mù cả vùng) để R:R vẫn lành mạnh và tôn trọng **risk ≤0.5%/lệnh** ([[43 - Position Sizing]]).

---

## 9. Quy trình vào lệnh

Quy trình cho **bullish** (bearish là gương phản chiếu trong premium).

**Bước 1 — Xác định bias & dealing range.** HTF bias bull (Daily Bias, cấu trúc bull). Vẽ dealing range, xác định discount. Chỉ tìm long.

**Bước 2 — Tìm bullish Breaker.** Một bearish OB ([[25 - OB - Order Block]]) bị phá vai trò lên → bullish Breaker. Đây là mốc **ALERT**.

**Bước 3 — Định vị Reaper IFVG.** Tìm IFVG **ngay trước** bullish Breaker, **bên trong chân giá** Breaker, ở **discount**. Kiểm tra Golden Rule (mục 6).

**Bước 4 — Chờ giá tới discount / Reaper IFVG.** **KHÔNG** mua từ Breaker. Để giá chạy xuyên Breaker vào discount tới Reaper IFVG. Đây vẫn chỉ là *alert*.

**Bước 5 — Chờ confirmation tại IFVG.** Khi giá vào IFVG: **MSS lên**, **displacement lên**, **rejection candles**, hoặc **liquidity sweep + bullish displacement**. Đây mới là *signal*.

**Bước 6 — Entry, stop, target.** Vào long tại IFVG (mép/CE tùy confirmation). **Stop dưới Reaper IFVG hoặc swing low gần nhất** (không trong gap). Target: prev highs / BSL / equal highs / HTF liquidity. Phân tầng TP theo [[16 - Internal & External Range Liquidity (IRL & ERL)]]: **T1 = IRL** (thanh khoản nội vùng), **T2 = ERL** (prev highs / external draw). Có thể kết hợp [[26 - OTE - Optimal Trade Entry]] nếu IFVG trùng vùng OTE.

> [!note] Bearish (đảo)
> Bias bear → bearish Breaker (bullish OB bị phá xuống) → Reaper IFVG trên Breaker, trong premium → chờ giá chạy xuyên Breaker lên premium → confirmation (MSS xuống / displacement xuống / rejection / sweep + bearish displacement) → short, stop **trên** Reaper IFVG/swing high, target SSL / prev lows / HTF liquidity dưới.

---

## 10. Ví dụ chart

### Ví dụ đúng

![[Reaper-Example-Correct.svg|697]]

**Mô tả:** Bias bull, giá đẩy lên tạo chân giá Breaker. Thay vì mua tại Breaker, chờ giá **chạy xuyên Breaker vào discount** (①), quét stop đám đông. Tại **Reaper IFVG** xuất hiện **support + MSS lên** (②). Retest = **Entry Long** (③), stop dưới Reaper IFVG, target **prev highs / BSL** (④).

**Vì sao tốt:**

- Có **HTF bias bull** rõ — chỉ tìm long.
- Giá chạy **xuyên Breaker vào discount** trước → né hoàn toàn drawdown mà entry-tại-Breaker phải chịu.
- **Support + MSS tại Reaper IFVG** = đủ confirmation (không vào mù).
- **Stop dưới gap** (không bị wick retest quét), R:R lành mạnh (T1=IRL, T2=ERL/prev highs).

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp chart NQ/ES/EURUSD: đánh dấu (1) HTF bias & dealing range, (2) Breaker + Reaper IFVG, (3) cú chạy xuyên Breaker vào discount, (4) confirmation tại IFVG (sweep/MSS/displacement), (5) entry/stop/target.*

### Ví dụ sai

![[Reaper-Example-Wrong.svg|697]]

**Mô tả lỗi:** (①) Vào long **ngay tại Breaker** vì sốt ruột. (②) Giá chạy xuyên qua → trader **trở thành thanh khoản** cho tổ chức. (③) Stop đặt **trong gap** → bị quét. Sau đó giá đảo lên đúng như phân tích — nhưng lệnh đã bị stop-out. Thêm lỗi: **IFVG bị đánh dấu ngoài chân giá / ở premium** (không hợp lệ theo Golden Rule).

**Bài học:**

- Chạm Breaker chỉ là **ALERT**, không phải **signal** — vào ngay = trở thành thanh khoản.
- IFVG phải nằm **trong chân giá Breaker** và đúng **P/D**, không phải trên nó.
- **Stop KHÔNG đặt trong gap** — đặt dưới Reaper IFVG / swing low.
- Đau nhất: **hướng đúng nhưng thực thi sai** → thua đúng cú lẽ ra phải thắng. Reaper sinh ra để chữa đúng lỗi này.

---

## 11. Thực hành tốt nhất (Best Practices)

> [!tip] 7 quy tắc Reaper IFVG
> 1. **Breaker là ALERT, Reaper là ENTRY** — chạm Breaker thì chuẩn bị, không bấm.
> 2. **Luôn có HTF bias** trước khi tìm Reaper — không bias thì không trade.
> 3. **Áp Golden Rule** — IFVG phải trong chân giá Breaker + đúng P/D (bull→discount, bear→premium).
> 4. **Chờ giá tới Reaper IFVG** — đừng mua từ Breaker vì sợ lỡ.
> 5. **Reaching ≠ signal** — vào IFVG mới là alert; chờ MSS/displacement/rejection/sweep mới vào.
> 6. **Stop dưới/trên Reaper IFVG hoặc swing gần nhất** — không đặt trong gap.
> 7. **Ưu tiên instrument delivery sạch** (NQ, ES) — inversion sắc, sweep rõ.

- Ưu tiên **NQ & ES**: CME delivery chặt → displacement sắc, inversion sạch. **EURUSD/GBPUSD/XAUUSD** cũng tốt. **Tránh** cặp low-volume (sweep/inversion nhiễu, Reaper giả).
- Đánh dấu bias/dealing range/Breaker/Reaper trên **H1 & M15**; time entry trên **M5/M3**.
- Ghi vào journal mỗi lần: có chờ Reaper hay vào tại Breaker; drawdown thực tế; kết quả — để đo edge.

> [!warning] Bối cảnh prop-firm (FTMO & The5ers)
> Toàn bộ giá trị của Reaper IFVG là **GIẢM drawdown và stop-out do vào Breaker quá sớm**. Điều này bảo vệ trực tiếp các luật loss:
> - **FTMO** đo daily loss theo **balance cố định** đầu ngày — mỗi cú stop-out oan tại Breaker ăn thẳng vào hạn mức này. Vào tại Reaper (sau khi drawdown đã xảy ra) giúp né đúng phần lỗ đó.
> - **The5ers** tham chiếu **equity đóng cửa hôm trước** cho logic loss — cơ chế khác, đừng trộn lẫn hai bộ luật. Reaper không đổi luật của firm nào; nó chỉ **nâng chất lượng entry** để bạn ít chạm ngưỡng hơn.
> Đừng dùng Reaper để biện minh cho **tăng số lệnh** — **process > outcome**, **risk ≤0.5%/lệnh**. Trong giai đoạn **foundation/backtesting** hiện tại: **backtest Reaper entry vs plain-Breaker entry** trên cùng tập setup để **chứng minh bằng số** mức drawdown giảm được, trước khi tính chuyện mua challenge.

---

## 12. Checklist trước khi dùng

> [!warning] Reaper IFVG không phải nút "mua/bán"
> Chạm được Reaper IFVG chỉ là alert. Entry vẫn cần confirmation LTF + đúng P/D + Golden Rule.

- [ ] Có **HTF bias** rõ và cấu trúc đồng thuận
- [ ] Đã vẽ **dealing range** + xác định Premium/Discount
- [ ] Có **Breaker Block hợp lệ** làm ALERT
- [ ] IFVG nằm **trong chân giá Breaker** (Golden Rule điều kiện 1)
- [ ] IFVG ở **đúng vùng P/D** (bull→discount, bear→premium) (điều kiện 2)
- [ ] Giá đã **chạy xuyên Breaker** tới Reaper IFVG (không mua từ Breaker)
- [ ] Có **confirmation LTF**: MSS / displacement / rejection / sweep
- [ ] **Stop** đặt dưới/trên Reaper IFVG hoặc swing gần nhất (KHÔNG trong gap)
- [ ] **Target** rõ (T1=IRL, T2=ERL/prev highs-lows/HTF liquidity)
- [ ] Instrument **thanh khoản cao, delivery sạch**
- [ ] **Risk ≤0.5%**, tuân daily/weekly loss limit của firm

---

## 13. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Vào tại Breaker | Long/short ngay khi chạm Breaker | Breaker là ALERT; chờ giá tới Reaper IFVG |
| Đánh dấu IFVG ngoài chân giá | "Thấy Reaper khắp nơi" | Áp Golden Rule: IFVG phải trong chân giá Breaker |
| Sai vùng P/D | Bull ở premium, bear ở discount | Bull→discount, bear→premium; loại IFVG sai nửa range |
| Trade không HTF bias | Vào theo cảm giác, ngược cấu trúc | Xác định Daily Bias trước; không bias thì không trade |
| Vào trước confirmation | Vào ngay khi giá chạm IFVG | Reaching = alert; chờ MSS/displacement/rejection/sweep |
| Stop trong gap | Bị wick retest quét rồi giá đảo | Đặt stop dưới/trên Reaper IFVG hoặc swing gần nhất |
| Instrument nhiễu | Reaper giả trên cặp low-volume | Ưu tiên NQ/ES/EURUSD/GBPUSD/XAUUSD |
| Tăng số lệnh vì "an toàn hơn" | Overtrade sau khi học Reaper | Process > outcome; risk ≤0.5%; giữ kỷ luật số lệnh |

---

## 14. Câu hỏi tự kiểm tra

- Tôi giải thích được Reaper IFVG trong 30 giây và phân biệt với Breaker Block không?
- Cơ chế "why" — vì sao giá chạy xuyên Breaker rồi mới đảo từ Reaper?
- Hai điều kiện của Golden Rule là gì? Tôi kiểm chúng đồng thời chứ?
- Trong setup bull, Reaper nằm ở discount hay premium? Tại sao?
- Vì sao stop không được đặt trong gap? Đặt ở đâu là đúng?
- "Reaching the IFVG is the alert, not the signal" — tôi cần thêm gì để có signal?
- Reaper giúp bảo vệ luật loss của FTMO và The5ers khác nhau ra sao?
- Trong journal của tôi, entry-tại-Reaper vs entry-tại-Breaker cho drawdown/expectancy khác nhau thế nào?

---

## 15. Flashcards / Active Recall

### Q1
**Hỏi:** Reaper IFVG là gì trong 1 câu?
**Đáp:** Một IFVG nằm ngay trước và bên trong chân giá của Breaker Block, ở đúng vùng P/D — là điểm vào thật của tổ chức, mức giá chạm tới SAU khi phe vào Breaker sớm đã bị stop.

### Q2
**Hỏi:** Vì sao gọi là "Reaper"?
**Đáp:** Thị trường "gặt" (reaps) trader vào Breaker quá sớm — vượt Breaker để tạo drawdown, quét stop, gom thanh khoản của họ — rồi mới đảo chiều từ điểm vào thật.

### Q3
**Hỏi:** Breaker và Reaper khác nhau về vai trò thế nào?
**Đáp:** Breaker = ALERT/mồi nhử (đám đông vào, bị stop). Reaper IFVG = ENTRY/bẫy (tổ chức lấp, đảo chiều). Coi Breaker là chuông báo, Reaper là điểm vào.

### Q4
**Hỏi:** Golden Rule của Reaper IFVG?
**Đáp:** IFVG phải nằm (1) BÊN TRONG chân giá Breaker VÀ (2) đúng vùng P/D — bull→discount, bear→premium. Thiếu một trong hai → không hợp lệ.

### Q5
**Hỏi:** Trong bull setup, Reaper nằm đâu so với Breaker?
**Đáp:** DƯỚI Breaker, trong DISCOUNT (giá rẻ hơn cho tổ chức mua). Bear thì ngược: TRÊN Breaker, trong PREMIUM.

### Q6
**Hỏi:** Vì sao stop không đặt trong gap?
**Đáp:** Wick retest hợp lệ thường chọc sâu vào gap (tới CE) trước khi bật; stop trong gap bị quét oan ngay trước khi giá đảo. Đặt dưới/trên Reaper IFVG hoặc swing gần nhất.

### Q7
**Hỏi:** Chạm được Reaper IFVG đã đủ để vào lệnh chưa?
**Đáp:** Chưa. Reaching = alert. Cần confirmation LTF: MSS / displacement / rejection candles / liquidity sweep + displacement.

### Q8
**Hỏi:** Reaper liên quan gì tới quản trị rủi ro prop-firm?
**Đáp:** Nó giảm drawdown/stop-out do vào Breaker sớm → bảo vệ daily loss limit (FTMO: balance cố định; The5ers: equity đóng cửa hôm trước — không trộn hai luật). Không dùng để tăng số lệnh; risk ≤0.5%.

---

## 16. Lesson Learned

- **Breaker là chuông, Reaper là cửa.** Nghe chuông thì chuẩn bị, đừng bấm; chỉ vào khi tới đúng cửa và có người mở (confirmation).
- **Đúng hướng vẫn có thể thua** nếu entry sai chỗ. Reaper chữa đúng nghịch lý "long đúng bias mà vẫn bị stop trước khi giá chạy".
- **Kiên nhẫn giữa Breaker và Reaper = drawdown né được.** Đây là biên độ rủi ro tôi tự tặng mình khi không sốt ruột.
- **Stop dưới gap, không trong gap** — một dòng luật nhỏ cứu rất nhiều cú lẽ ra thắng.
- **Foundation phase:** phải backtest Reaper vs plain-Breaker trên NQ/ES để có **bằng chứng số** rằng drawdown giảm — không tin bằng cảm giác.

---

> [!cite] Nguồn
> [ICT Reaper Inversion Fair Value Gap: The Institutional Entry Hidden Behind the Breaker Block](https://innercircletrader.net/tutorials/ict-reaper-inversion-fair-value-gap/)
