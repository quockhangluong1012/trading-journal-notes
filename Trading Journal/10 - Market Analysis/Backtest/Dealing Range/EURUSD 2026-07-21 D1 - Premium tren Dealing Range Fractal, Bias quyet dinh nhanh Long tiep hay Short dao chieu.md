---
type: market-analysis
status: watchlist
date: 2026-07-21
symbol: EURUSD
timeframe: "D1 (dealing range đang xét) → H1 (chưa vẽ, chờ xác định bias trước khi xuống), chart FXReplay/OANDA, giai đoạn hiển thị Nov 2019 – Sep 2020 (~nhịp phục hồi sau đáy COVID)"
session: replay
htf_bias: "CHƯA XÁC ĐỊNH RÕ — đây chính là nội dung chính của note.  quan sát D1 đang ở Premium của một dealing range (giá gần đỉnh mới ~1.20135 sau khi tăng liên tục từ vùng đáy COVID), nhưng chưa chốt bias là Bullish-continuation hay đã có lý do Bearish-reversal. Toàn bộ hành động tiếp theo (chờ hay xuống H1 ngay) phụ thuộc vào câu trả lời này."
setup: "Bài học framework: phân biệt hai nhánh hành động khi giá ở Premium của D1 dealing range — (A) Bias vẫn Bullish → Premium nghịch hướng, phải chờ retrace về Discount trước khi xuống H1 tìm Long; (B) Bias đã chuyển Bearish/nghi ngờ đảo chiều → Premium đúng hướng, xuống H1 ngay để re-map range mới và tìm Short. Không có case thực thi lệnh nào ở note này."
in_trade: false
draw_on_liquidity: "Chưa xác định vì bias chưa chốt. Các mốc đã đánh dấu trên chart (đọc ước lượng từ ảnh, CẦN verify lại trên platform): 1.20135 (đỉnh mới nhất — có thể là external BSL nếu bias Bullish, hoặc chính là điểm sweep nếu đang tìm Short), 1.19076 (đường chấm — nhiều khả năng old high/CE đã bị tái chiếm), 1.17999 (mốc EQ  tự đánh dấu), 1.16010 và 1.11730 (hai mốc thấp hơn, vai trò chưa rõ — có thể là SSL của range gốc hoặc mốc tham chiếu từ một range khác)."
key_poi: "Chưa có — chưa xuống H1 nên chưa có POI cụ thể. Đây là điểm mấu chốt: note này dừng ở bước xác định bias/vị trí, chưa tới bước tìm PD Array."
invalidation: "Không áp dụng (chưa có giả thuyết entry). Điều kiện để chuyển từ 'watchlist framework' sang 'có setup thật':  phải tự xác định được D1/H4 bias bằng cấu trúc (có MSS chưa, có SMT divergence với DXY không, nhịp tăng đã suy yếu chưa) — không được suy ra bias chỉ từ việc giá đang premium hay discount."
topic: "Premium/Discount là bộ lọc vị trí chứ không phải tín hiệu vào lệnh; Nested Dealing Range đa khung (D1 vs H1) và quy tắc HTF governs bias, LTF chỉ tinh entry; hai nhánh hành động đối lập tại cùng một vị trí Premium tuỳ theo Bias; đọc quartile/độ nông của retrace để đánh giá sức khỏe trend; lỗi phổ biến 'sốt ruột xuống khung nhỏ tìm discount giả trong khi HTF vẫn premium'."
tags:
  - analysis
  - watchlist
  - EURUSD
  - premium-discount
  - dealing-range
  - nested-timeframe
  - daily-bias
  - ict-2022
  - learning
---

# EURUSD D1 — Premium trên Dealing Range Fractal & Bias quyết định nhánh Long tiếp hay Short đảo chiều — 2026-07-21

> [!info] Trạng thái
> **WATCHLIST / LUYỆN FRAMEWORK — không có lệnh, không có case thực thi.** Note này ghi lại một buổi học khái niệm:  gửi ảnh D1 EURUSD (FXReplay/OANDA, dữ liệu lịch sử ~Nov 2019–Sep 2020), tự đánh dấu dealing range và nhận ra giá đang trên 50% (Premium), rồi hỏi liệu có bắt buộc phải chờ D1 về Discount trước khi xuống H1 hay không. Câu trả lời không phải một quy tắc cứng, mà là một cây quyết định phụ thuộc vào Bias — đây là nội dung chính cần nắm.

> [!warning] Ảnh gốc chưa được lưu vào Attachments
> Ảnh chart D1 EURUSD  gửi trong phiên chat chưa có mặt trong `10 - Market Analysis/Attachments/`. Hãy paste lại ảnh đó vào Obsidian ngay dưới dòng này (Obsidian sẽ tự tạo file `Pasted image ...png` và embed đúng theo quy ước đã dùng ở các note trước) để lần sau đối chiếu chính xác thay vì đọc lại theo trí nhớ.

---

## 0. Bối cảnh & câu hỏi gốc

 đang học kết hợp **Dealing Range** với **ICT 2022 Model**. Trên D1 EURUSD,  tự vẽ dealing range và đánh dấu equilibrium; giá hiện tại nằm trên mức 50% đó (Premium). Câu hỏi gốc: *"Tôi có cần chờ khung D1 về vùng discount trước khi xuống khung H1 vẽ dealing range và chờ giá vào discount của H1 và tìm POI không?"*

Đây là câu hỏi rất đáng hỏi — nó chạm đúng vào lỗi phổ biến nhất được cảnh báo trong [[12-Dealing-Range]] và [[27-Premium-Discount]]: nhầm lẫn giữa "có một vị trí đẹp" và "có bias cho phép hành động tại vị trí đó".

---

## 1. Quan sát trên chart D1 (đọc ước lượng — cần verify lại)

Từ ảnh D1 (FXReplay/OANDA, EURUSD, đơn vị UTC+7 theo quy ước vault), các mốc giá được đánh dấu:

| Mốc | Giá (ước lượng) | Vai trò khả dĩ |
|---|---|---|
| Đỉnh mới nhất | **1.20135** | Có thể là external BSL đang mở (nếu Bullish) hoặc chính điểm cần sweep (nếu tìm Short) |
| Đường chấm (dotted) | **1.19076** | Nhiều khả năng là old high / CE đã bị tái chiếm gần đây — cần xác nhận |
| Equilibrium tự đánh dấu | **1.17999** | Mốc 50%  dùng để kết luận "đang premium" |
| Mốc thấp hơn | 1.16010 | Vai trò chưa rõ — có thể SSL nội bộ hoặc biên một range khác |
| Mốc thấp hơn | 1.11730 | Vai trò chưa rõ — khoảng cách rất xa so với giá hiện tại, cần xem đây có còn liên quan tới price delivery hiện tại không (xem cảnh báo War Story W3 trong [[12-Dealing-Range]] về "range quá rộng") |

> [!warning] Không bịa số — cần  tự xác nhận
> Bảng trên là đọc trực quan từ ảnh chụp màn hình, **không phải giá trích xuất chính xác từ platform**. Trước khi dùng các mốc này cho bất kỳ quyết định nào, verify lại chính xác trên chart gốc, đặc biệt là **hai đầu thật của dealing range** (đáy nào, đỉnh nào tạo ra 50% = 1.17999) — vì hiện tại chưa rõ range  dùng là từ đáy nào đến đỉnh nào.

Quan sát cấu trúc tổng thể: đây là một nhịp tăng mạnh, gần như liên tục, từ vùng đáy COVID (~1.069, tháng 3/2020) chạy một mạch lên hiện tại, vừa phá tiếp lên đỉnh mới sau khi tái chiếm một mức cũ (đường chấm 1.19076). Không có pullback sâu trong suốt chặng đường.

---

## 2. Nguyên tắc gốc: Premium/Discount là bộ lọc VỊ TRÍ, không phải tín hiệu

Theo [[27-Premium-Discount]]:

> "Mua ở Discount, Bán ở Premium — nhưng CHỈ khi đồng hướng Daily Bias VÀ tại một PD Array hợp lệ."

Giá đang premium chỉ trả lời "giá đang đắt hay rẻ". Nó **không** tự quyết định Long hay Short — việc đó do **Daily Bias** quyết định. Câu hỏi đúng không phải "giá đang premium thì làm gì", mà là:

**"Bias D1/H4 của tôi là Bullish hay Bearish — và premium hiện tại có đồng hướng bias đó không?"**

Từ đây tách thành hai nhánh đối lập hoàn toàn.

---

## 3. Hai nhánh hành động — cùng một vị trí Premium, hai kết luận trái ngược

### Nhánh A — Bias vẫn Bullish (còn muốn Long tiếp)

Premium lúc này **ngược hướng bias**. Theo [[12-Dealing-Range]], mục A2 (ma trận nested alignment):

| Vị trí D1 | Vị trí H1 nếu vẽ ngay bây giờ | Kết luận |
|---|---|---|
| Premium | Discount | **Bẫy phổ biến nhất** — "discount H1" nhưng thực chất vẫn mua premium D1 |
| Premium | Premium | Cộng hưởng Short (ngược bias Bullish → vẫn không action) |

→ **Không nên** xuống H1 để "cố tìm Long" ngay bây giờ. Bất kỳ Long nào tìm được ở H1 lúc D1 còn premium gần như chắc chắn là mua premium trá hình dưới tên "discount H1". Hành động đúng: **chờ D1 retrace về Discount** (lý tưởng vào vùng OTE 0.62–0.79 của chính nhịp tạo ra range) rồi mới xuống H1 vẽ range con và tìm POI.

### Nhánh B — Đã có lý do nghi ngờ đảo chiều (bắt đầu tìm Short)

Nếu có bằng chứng cụ thể (MSS bearish đầu tiên trên H4, SMT divergence với DXY, chạm đúng vùng target Standard Deviation đã tính trước — **không phải chỉ vì "giá đã tăng nhiều rồi"**), premium chính là vùng cần. Lúc này:

1. Xuống H1 **ngay bây giờ**, re-map dealing range trên chính nhịp tăng vừa rồi (đáy gốc của leg → đỉnh mới 1.20135) theo quy trình 5 bước của [[37-Re-mapping-Dealing-Range-sau-Displacement]].
2. Chờ H1 có **Buy-Side Liquidity sweep** (quét 1.20135 hoặc equal high gần đó) + **bearish MSS**.
3. POI = bearish FVG/OB của chính nhịp giảm đó, nằm ở premium/deep-premium của H1 range mới.
4. Target: internal trước (có thể là 1.19076 nếu nó đóng vai trò hỗ trợ nội bộ), external SSL sau (1.17999 → 1.16010).

Đây đúng sequence "Short from Premium" trong [[01 - ICT 2022 Model]]: `Bias → Premium → Sweep BSL → Bearish MSS/Displacement → FVG → Entry → Target SSL`.

> [!important] Điểm mấu chốt của cả note
> **Không có quy tắc "luôn phải chờ discount" hay "luôn được xuống khung ngay" — có quy tắc duy nhất: hành động phải khớp với Bias đã xác lập bằng cấu trúc, không phải suy ra Bias từ vị trí giá.** Nhầm nhân-quả này (thấy premium → tự động nghĩ nên tìm Short, hoặc thấy premium → tự động nghĩ phải chờ) là sai ở cả hai chiều nếu chưa xác định Bias trước.

---

## 4. Đọc đặc thù của chart này — retrace nông = trend khỏe

Theo mục nâng cao "quartile" trong [[27-Premium-Discount]]:

> "Trong bullish delivery mạnh, các cú retrace chỉ về tới discount nông rồi chạy tiếp — retrace càng nông trend càng khỏe."

Nhịp tăng trên chart gần như không có pullback sâu suốt từ đáy COVID tới giờ — đây là dấu hiệu điển hình của **continuation mạnh**, không tự nhiên là dấu hiệu đảo chiều. Nếu  chưa có lý do HTF cụ thể để coi đây là điểm đảo, mặc định nên coi mình đang ở **Nhánh A** và hành động đúng là kiên nhẫn chờ.

---

## 5. Lỗi cần tránh

Việc tự hỏi "có cần chờ không" là bản năng phòng thủ đúng — vì đây chính là nơi trader mới hay phạm lỗi: **thấy giá đang chạy (premium, có momentum) → sốt ruột → xuống khung nhỏ hơn để "tìm được cái gì đó để trade"**, trong khi HTF chưa cho phép. Hai dạng lỗi cụ thể:

- Đi tìm Long ở "discount H1" trong khi D1 đang premium sâu → mua đắt tưởng mua rẻ (lỗi gốc rễ trong [[12-Dealing-Range]], mục 9).
- Coi premium D1 là tín hiệu Short ngay lập tức mà chưa có sweep + MSS xác nhận trên H1 → chase, vào lệnh không có cấu trúc.

Quy tắc "không có lệnh" áp dụng: nếu range con mới vẽ không có PD Array hợp lệ đúng nửa range cho hướng bias, kết luận là *có range nhưng không có lệnh* — đứng ngoài là đúng, không phải thất bại phân tích.

---

## 6. Checklist tổng hợp

| Hạng mục | Trạng thái |
|---|---|
| Dealing range D1 đã vẽ | ⚠️ Có nhưng hai đầu chính xác chưa được verify lại |
| Equilibrium D1 xác định | ⚠️  tự đánh dấu 1.17999 — chưa xác nhận range gốc |
| Vị trí hiện tại | ✅ Premium (trên EQ) |
| D1/H4 Bias đã xác định bằng cấu trúc | ❌ **CHƯA — đây là việc cần làm trước, không phải câu hỏi premium/discount** |
| Có MSS bearish nào trên H4/D1 chưa | ❓ Chưa kiểm tra |
| Có SMT divergence với DXY chưa | ❓ Chưa kiểm tra |
| Đã xuống H1 vẽ range con | ❌ Chưa — đúng, vì bias chưa chốt |
| Kết luận | **Xác định Bias trước bằng cấu trúc, rồi mới chọn Nhánh A hay B** |

---

## 7. Concept đã áp dụng

- [[27-Premium-Discount]] · [[12-Dealing-Range]] · [[37-Re-mapping-Dealing-Range-sau-Displacement]]
- [[01 - ICT 2022 Model]] · [[32-Top-down-Analysis-Multiple-Timeframes]]
- [[59-Daily-Bias]] · [[16-Internal-External-Range-Liquidity-IRL-ERL]]
- [[26-OTE-Optimal-Trade-Entry]]

---

## 8. Bài học rút ra

1. **Premium/Discount là bộ lọc vị trí, không phải tín hiệu vào lệnh.** Giá ở premium không tự động nói "tìm Short" hay "phải chờ" — nó chỉ nói "giá đang đắt". Bias mới quyết định hành động.
2. **HTF range quyết định hướng, LTF range không được phủ quyết.** Xuống H1 sớm khi D1 còn premium (và bias vẫn Bullish) chỉ tạo ra ảo giác "discount H1" trong khi thực chất vẫn mua đắt.
3. **Cùng một vị trí Premium, hai bias khác nhau cho hai hành động đối lập hoàn toàn** — chờ (Nhánh A) hay xuống khung ngay để tìm đảo chiều (Nhánh B). Không có công thức chung, chỉ có Bias đã xác lập bằng cấu trúc là biến số quyết định.
4. **Retrace càng nông trong một trend mạnh, trend càng khỏe** — không nên tự suy ra "đảo chiều" chỉ vì giá đã chạy xa và đang premium.
5. **Sốt ruột xuống khung nhỏ khi HTF chưa cho phép là lỗi phổ biến nhất** ở giai đoạn học kết hợp Dealing Range + Premium/Discount đa khung.

---

## 9. Câu hỏi cần chốt (chưa xác nhận)

- D1/H4 EURUSD hiện tại: bias là Bullish (continuation) hay đã có lý do cụ thể coi là Bearish (reversal)? Đây là câu hỏi quan trọng nhất, cần trả lời trước khi làm bất cứ điều gì khác.
- Hai đầu chính xác của dealing range D1 mà  đang dùng để tính EQ = 1.17999 là đáy/đỉnh nào? (cần verify để mọi phép đo phía sau có nghĩa — theo đúng cảnh báo "chọn sai range" trong [[12-Dealing-Range]]).
- Đường chấm 1.19076 có đúng là một old high đã bị tái chiếm (reclaim) hay là một CE của FVG nào đó? Vai trò này ảnh hưởng tới việc nó có phải internal liquidity đáng tin cậy cho target/stop hay không.
- Hai mốc 1.16010 và 1.11730 có phải là external liquidity của cùng một range D1, hay thuộc về một range khác/khung khác đã cũ (xem War Story W3 — "range quá rộng" trong [[12-Dealing-Range]])?

## 10. Next steps

- Xác định D1/H4 bias bằng cấu trúc (structure) trước — không suy luận từ vị trí giá. Nếu chưa có MSS bearish rõ ràng trên HTF, mặc định giữ Nhánh A (chờ, không hành động).
- Nếu chọn Nhánh A: đặt alert quanh vùng Discount/OTE của D1 range (sau khi đã verify đúng hai đầu range), chưa vẽ range H1.
- Nếu tìm được lý do cụ thể cho Nhánh B (SMT divergence, MSS bearish HTF...): quay lại note này, bổ sung bằng chứng, rồi tạo một file backtest riêng theo `04 - Backtesting/` nếu tiến tới xác nhận sweep + MSS thật trên H1, cross-link ngược về note này.
- Paste ảnh gốc D1 vào Attachments (xem cảnh báo đầu note) để các mốc giá không còn là ước lượng.

---
*Ghi chú: `date` = ngày thực hiện phân tích (VN, UTC+7), không phải ngày trên chart (chart là dữ liệu lịch sử FXReplay ~2019–2020). Không log backtest vì không có lệnh — đây là note phân tích/luyện framework thuần khái niệm. Mọi mức giá là ước lượng đọc từ ảnh chụp màn hình, không phải giá trích xuất chính xác từ nền tảng — verify lại trên chart gốc trước khi dùng cho quyết định giao dịch thật.*
