---
type: market-analysis
status: watchlist
date: 2026-07-19
symbol: EURUSD
timeframe: D1 (Daily) — chart FXReplay, giai đoạn khoảng Jun/2012 – Mar/2013
session: replay
htf_bias: "Bullish tổng thể (chuỗi HH/HL từ ~1.205 lên ~1.370), nhưng đang đứng ngay tại decision zone; có ứng viên MSS/CHoCH giảm chưa được xác nhận dứt khoát"
setup: "Phân biệt Pullback sâu (deep pullback) vs MSS thật (Change of Character có displacement + sweep) tại vùng ~1.305 — chính là launch pad / protected HL đã sinh ra leg tăng mạnh nhất (leg 3, từ 1.305 lên 1.370)"
in_trade: false
draw_on_liquidity: "Kịch bản A (pullback): BSL phía trên tại đỉnh chu kỳ ~1.370. Kịch bản B (MSS thật): SSL tại HL#1 ~1.280 (Oct–Nov), xa hơn là đáy chu kỳ ~1.205–1.21"
key_poi: "Vùng ~1.305 — protected HL / launch pad của leg 3, đồng thời là equal-high yếu tháng 12. Đây là decision zone duy nhất của toàn bộ chart"
invalidation: "Kịch bản A vô hiệu nếu D1 đóng cửa dưới 1.305 + retest từ dưới lên bị từ chối. Kịch bản B vô hiệu nếu D1 đóng cửa trở lại trên 1.305 và giữ được (reclaim)"
topic: "Framework 6 tiêu chí phân biệt Pullback sâu vs MSS thật (CHoCH/MSS): internal vs external structure, chất lượng displacement, bối cảnh liquidity sweep (Tier pool), vị trí Fibonacci/OTE, accept vs reject (body close vs wick), yếu tố thời gian — áp dụng vào case EURUSD Daily thực tế"
tags:
  - analysis
  - watchlist
  - EURUSD
  - daily-bias
  - market-structure-shift
  - change-of-character
  - pullback
  - liquidity-sweep
  - premium-discount
  - optimal-trade-entry
  - ict-2022
---

# EURUSD D1 — Pullback sâu vs MSS thật tại decision zone 1.305 — 2026-07-19

> [!info] Trạng thái
> **WATCHLIST — không vào lệnh.** Đây là note tổng hợp và đào sâu buổi phân tích cùng Khang về một chart Daily EURUSD (FXReplay, ~Jun/2012–Mar/2013). Cấu trúc tổng thể là HH/HL (tăng), nhưng nhịp giảm Feb–Mar đang test lại đúng **launch pad ~1.305** — gốc của leg tăng mạnh nhất. Câu hỏi trung tâm: đây là **Pullback sâu** (bias tăng còn nguyên) hay **MSS thật** (bias đổi)? Note này xây một **framework 6 tiêu chí** để trả lời câu hỏi đó một cách có hệ thống, không chỉ cho case này mà cho mọi tình huống tương tự sau này.

![[EURUSD-DailyStructure-Map-20260719.svg]]

> [!warning] Ảnh gốc
> Ảnh chart Khang gửi trong chat chưa được lưu vào vault (không có file upload kèm theo). Nếu muốn tham chiếu lại chính xác, lưu ảnh vào `10 - Market Analysis/Attachments/` với tên gợi ý `EURUSD-20260719-D1-1.png` và thêm dòng `![[EURUSD-20260719-D1-1.png]]` phía trên. Sơ đồ SVG ở trên **tái dựng cấu trúc theo mô tả** (giá xấp xỉ đọc từ ảnh), không phải chart gốc pixel-chính-xác — dùng để minh họa logic, không dùng để đo entry chính xác.

## 0. Bối cảnh & câu hỏi gốc

Khang quan sát: cấu trúc D1 đang là chuỗi **HH/HL** (higher-high / higher-low) — về lý thuyết vẫn là uptrend. Nhưng trong chính nhịp pullback gần nhất (Feb–Mar), Khang phát hiện một cú giảm có **displacement** thật sự, đủ mạnh để đặt câu hỏi: đây còn là một pullback bình thường, hay đã là một **Market Structure Shift (MSS)**?

Đây là đúng loại câu hỏi mà 90% trader ICT trả lời sai theo hướng cảm tính — hoặc giữ bias cũ chỉ vì "structure vẫn là HH/HL" (bỏ qua tín hiệu MSS đang hình thành), hoặc hoảng loạn đổi bias chỉ vì thấy một cú giảm mạnh (bỏ qua rằng HL quan trọng nhất chưa hề bị phá). Cả hai lỗi đều xuất phát từ cùng một nguyên nhân: **thiếu một bộ tiêu chí khách quan để phân xử**, thay vào đó là suy diễn theo mong muốn của bản thân về hướng thị trường.

## 1. HTF Bias — đọc lại structure thật (theo [[12 - Daily Bias]])

Trước khi đi vào framework, cần một bức tranh structure chính xác — vì toàn bộ tranh luận "pullback hay MSS" chỉ có nghĩa khi ta biết chính xác **HL nào đang bị đe dọa**.

| Mốc | Giá xấp xỉ | Vai trò |
|---|---|---|
| Đáy khởi đầu | ~1.205 | Gốc chu kỳ tăng |
| Swing High #1 | ~1.315 (Sep) | BSL đầu tiên |
| HL #1 | ~1.280 (Oct–Nov) | HL được giữ vững — dự phòng làm SSL nếu sau này MSS thật |
| Equal-high yếu | ~1.305–1.31 (Dec) | Đỉnh yếu, gần bằng Swing High #1 |
| **HL #2 = Launch pad** | **~1.305 (đầu Jan)** | **Protected HL quan trọng nhất — gốc của leg 3** |
| Swing High #2 | ~1.370 (Feb) | BSL mới, quét sạch BSL của Swing High #1 trước khi đảo |
| Giá hiện tại | ~1.3075 | Đang test lại chính vùng Launch pad |

Điểm mấu chốt tôi đã nêu ở lượt phân tích trước và cần nhấn mạnh lại: **vùng đường đỏ Khang vẽ không phải một mức ngẫu nhiên** — đó chính xác là launch pad của leg tăng mạnh nhất trong toàn bộ chart (leg 3: 1.305 → 1.370, một cú displacement rất dứt khoát). Theo [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL & ERL]], đây là một **External Range Liquidity / protected swing** thật — không phải một FVG nội bộ nhỏ có thể bỏ qua.

Vì vậy nhịp giảm Feb–Mar đang test đúng vào **cái HL sinh ra chính con sóng tăng chủ đạo**, chứ không phải một pullback nông vào giữa leg. Đây là lý do câu hỏi của Khang đáng để đào sâu bằng một framework đầy đủ, thay vì trả lời bằng trực giác.

## 2. Framework 6 tiêu chí phân biệt Pullback sâu vs MSS thật

Đây là phần lõi. Theo [[21 - Market Structure Shift|MSS]] và [[09 - Change of Character|CHoCH]] trong vault, một cú phá cấu trúc ngược trend **chỉ đáng tin khi đủ điều kiện** — không phải mọi cú giảm mạnh trong uptrend đều là MSS, và không phải mọi retracement sâu đều chỉ là "pullback vô hại". Sáu tiêu chí dưới đây xếp theo đúng thứ tự ưu tiên khi đọc chart.

### (a) Break tại Internal structure hay External (protected) structure?

Đây là gốc rễ của phần lớn nhầm lẫn, và chính là khái niệm **IRL vs ERL** trong vault. Một MSS xảy ra trên **internal structure** (các đáy nhỏ hình thành trong quá trình đẩy giá, tạo bởi vài nến liên tiếp, không có ý nghĩa cấu trúc) chỉ là noise — nó **không** đổi bias của leg lớn hơn, vẫn là một phần của pullback sâu. Một MSS chỉ "thật" theo nghĩa đổi HTF bias khi nó phá vỡ **external / protected structure** — tức chính cái HL đã định nghĩa ra leg đang xét.

![[PullbackVsMSS-Internal-vs-External-20260719.svg]]

**Áp dụng vào case:** vùng 1.305 không phải một micro swing — nó là protected HL, gốc trực tiếp của leg 3. Việc đầu tiên Khang cần làm là xác nhận: cú giảm hiện tại đã **phá xuyên và đóng cửa dưới 1.305** chưa, hay mới chỉ chạm/wick vào? Đây là câu hỏi có tính quyết định nhất trong toàn bộ framework, vì nó xác định ta đang ở tình huống (a)-hợp-lệ-cho-MSS hay không.

### (b) Chất lượng của displacement

Theo nguyên tắc cốt lõi trong [[21 - Market Structure Shift]]: *"MSS bị vô hiệu khi không có displacement — phá bằng wick yếu, không body, không FVG."* MSS thật đi kèm displacement rõ ràng: thân nến lớn hơn hẳn range trung bình gần đó (so với biên độ Daily gần đây), thường để lại FVG, và quan trọng nhất — **đóng cửa (close)**, không chỉ bấc (wick), vượt qua structure point.

Từ ảnh, nhịp giảm tháng 2–3 có 2–3 nến thân dài giảm mạnh (~1.35→1.33, rồi ~1.32→1.30) — có displacement thật, không phải một chuỗi grind từng bước nhỏ. Nhưng câu hỏi mấu chốt là: displacement đó **đã phá qua external structure point (1.305) với một close rõ ràng chưa**, hay energy đã cạn ngay tại vùng đó? Các nến cuối cùng trên chart có vẻ đang consolidate với thân nhỏ lại ngay tại/trên vùng đường đỏ — đây là dấu hiệu displacement có thể đã hết đà đúng ngay tại decision zone, nhưng cần xác nhận bằng dữ liệu close thật.

### (c) Bối cảnh liquidity — có BSL/SSL nào bị quét trước khi đảo chiều không?

Đây là câu hỏi "vì sao" institutional đứng sau move, và là tiêu chí có bằng chứng ủng hộ mạnh nhất trong case này. Theo nguyên tắc phân tầng chất lượng pool trong [[21 - Market Structure Shift]]: *"pool nhiều nhiên liệu (equal highs/lows) tạo ra đảo chiều đáng tin hơn hẳn một micro swing vô nghĩa."*

![[PullbackVsMSS-LiquidityContext-20260719.svg]]

**Áp dụng vào case:** đỉnh 1.370 cao hơn tất cả các đỉnh trước (Swing High #1 ~1.315, equal-high yếu ~1.305–1.31 tháng 12) — nghĩa là nó đã **quét sạch BSL phía trên** (đúng Tier cao theo bảng phân tầng: equal highs) trước khi giảm. Đây là dấu hiệu ủng hộ khả năng đây là một MSS thật (kiểu Smart Money Reversal), chứ không phải pullback ngẫu nhiên, vì có "lý do" institutional để đảo chiều tại đó: hết thanh khoản mua để đẩy giá lên tiếp, quay đầu run xuống lấy SSL bên dưới. Theo [[16 - Internal & External Range Liquidity (IRL & ERL)|IRL/ERL]], sau khi quét ERL đỉnh (BSL 1.370), draw tiếp theo hợp lý là quay vào internal hoặc hướng ra ERL đối diện (SSL tại HL#1 ~1.280, xa hơn là đáy chu kỳ ~1.205–1.21).

### (d) Vị trí trong Fibonacci / OTE của leg trước

Theo [[26 - OTE - Optimal Trade Entry|OTE]], một pullback sâu nhưng vẫn "khỏe mạnh" thường dừng lại trong vùng **OTE (62%–79%)** của leg vừa tạo ra nó. Nếu retracement vượt qua 79%–100%, toàn bộ premium giá vừa tạo ra gần như bị xóa sổ — thị trường đang nói "leg đó không đại diện cho fair value, quay lại điểm xuất phát."

![[PullbackVsMSS-OTE-vs-FullRetrace-20260719.svg]]

**Áp dụng vào case:** giá hiện tại (~1.3075) nằm giữa mức 79% (~1.313) và 100% (~1.305) của leg 3 — tức retracement đã ăn gần hết, xấp xỉ 86–90%+ toàn bộ leg. Đây là một tín hiệu cảnh báo quan trọng: một pullback lành mạnh trong xu hướng tăng **hiếm khi** ăn hết gần trọn leg đẩy mạnh nhất. Retracement sâu đến mức này nghiêng cán cân về phía MSS thật hơn là pullback thông thường — dù chưa hẳn đã "fail" theo đúng nghĩa của mục 5 trong note OTE (giá chưa chắc đã **đóng cửa** vượt hẳn qua 100%, cần kiểm tra kỹ).

### (e) Phản ứng tại vùng test — Accept hay Reject?

Đây là bằng chứng "sống" quan trọng nhất, và cũng là thứ duy nhất một screenshot tĩnh không thể trả lời chắc chắn — chỉ Khang xem chart thật mới xác nhận được.

![[PullbackVsMSS-WickVsClose-20260719.svg]]

Nếu giá chạm vùng 1.305 và bị **reject** ngay với một displacement tăng mạnh (bullish engulfing, FVG tăng hình thành, chỉ wick chạm vùng rồi đóng cửa bên trên) — đó là xác nhận pullback sâu vào một HL/OB hợp lệ, bias tăng vẫn còn nguyên. Nếu giá **đóng cửa dưới** 1.305, sau đó retest lại từ dưới lên (tức 1.305 giờ đóng vai trò resistance thay vì support, đúng logic acceptance trong [[09 - Change of Character]]) — đó là xác nhận MSS thật, bias đảo chiều. Từ ảnh, các nến cuối cùng bên phải có vẻ đang consolidate ngay tại/quanh đường đỏ với thân nhỏ — chưa đủ dữ liệu để kết luận dứt khoát đây là accept hay reject.

### (f) Thời gian — nhịp pullback mất bao lâu so với leg đẩy?

Một correction lành mạnh thường diễn ra nhanh hơn nhiều so với thời gian tạo ra leg mà nó điều chỉnh (logic AMD/[[02 - AMD|Power of Three]] — accumulation dài, manipulation ngắn). Leg 3 (1.305→1.370) mất khoảng 1 tháng; nhịp giảm hiện tại cũng đã chạy khoảng 1–1.5 tháng — thời gian tương đương hoặc dài hơn leg đẩy là một dấu hiệu khác ủng hộ giả thuyết MSS thật hơn là một correction nhanh trong trend.

## 3. Bảng tổng hợp bằng chứng

| Tiêu chí | Bằng chứng ủng hộ Pullback sâu | Bằng chứng ủng hộ MSS thật |
|---|---|---|
| (a) Internal vs External | — | Đang test đúng External/protected HL (launch pad 1.305), không phải micro swing |
| (b) Displacement | Nến cuối consolidate, thân nhỏ dần tại vùng | Có 2–3 nến thân dài giảm mạnh trước đó — displacement thật tồn tại |
| (c) Liquidity context | — | Đỉnh 1.370 là một BSL sweep Tier cao (equal highs) trước khi đảo |
| (d) Vị trí Fibonacci | — | Retracement ~86–90%+ của leg 3 — sâu bất thường so với chuẩn OTE 62–79% |
| (e) Accept/Reject | Chưa xác nhận — cần Khang đọc close thật | Chưa xác nhận — cần Khang đọc close thật |
| (f) Thời gian | — | Thời gian pullback ≥ thời gian leg đẩy — dài bất thường |

> [!summary] Đọc kết quả trung thực
> **4/6 tiêu chí nghiêng về giả thuyết MSS thật; 2/6 tiêu chí (b, e) là "chưa xác nhận" vì phụ thuộc dữ liệu close thật mà chỉ ảnh chụp tĩnh không trả lời được.** Đây không phải kết luận "chắc chắn đảo chiều" — đó là một bias có điều kiện, sẽ được mục 4 trình bày rõ theo đúng tinh thần [[12 - Daily Bias]]: bias là giả thuyết có invalidation, không phải niềm tin.

## 4. Daily Bias có điều kiện (hai kịch bản)

> [!summary] Bias trung thực — không ép một mũi tên
> Tôi sẽ **không** đưa cho Khang một bias "chắc chắn", vì lý do đơn giản: tôi không thể xác nhận chính xác close price của các nến cuối so với đường đỏ chỉ từ ảnh chụp — đây đúng là ranh giới thật giữa (e) accept và reject mà không nên đoán mò. Nhưng dựa trên (a), (c), (d), (f), tôi nghiêng về việc coi đây là một **MSS tiềm năng** chứ không đơn thuần là pullback sâu.

**Kịch bản A — Pullback sâu (nếu reject):** nếu daily có một displacement tăng rõ ràng (thân dài, đóng cửa cao, tạo FVG) ngay tại/trên 1.305 và không đóng cửa dưới mức đó → đây vẫn là pullback sâu hợp lệ vào một HL/Order Block quan trọng. **Bias tăng còn nguyên. Draw on liquidity: BSL phía trên đỉnh 1.370.**

**Kịch bản B — MSS thật (nếu accept):** nếu daily đóng cửa rõ ràng dưới vùng 1.305 (không phải chỉ wick) VÀ sau đó có một retest từ dưới lên bị từ chối tại chính vùng đó (giờ đóng vai trò resistance) → xác nhận MSS thật. **Bias chuyển sang giảm/trung lập. Draw on liquidity: SSL tại HL#1 ~1.280, xa hơn là đáy chu kỳ ~1.205–1.21.**

> [!warning] Lưu ý mentor quan trọng nhất
> Câu hỏi gốc của Khang — *"structure đang là HH/HL nhưng tôi thấy một MSS có displacement trong pullback"* — chính là bẫy kinh điển của ICT. HH/HL là mô tả structure **quá khứ** (lagging); MSS là tín hiệu structure **tương lai** (leading). Rất nhiều trader giữ bias tăng chỉ vì "structure vẫn là HH/HL" trong khi bỏ qua một MSS rõ ràng đang hình thành ngay trước mắt ở đúng external structure point quan trọng nhất. Nếu Khang đã thấy displacement thật ở đây, đừng tự thuyết phục bản thân "chỉ là pullback" vì muốn giữ bias cũ — hãy để tiêu chí (a), (b), (e) quyết định, không phải mong muốn về hướng thị trường. Đây chính xác là loại confirmation bias mà [[01 - ICT 2022 Model|2022 Model]] yêu cầu loại bỏ trước khi entry.

## 5. Concept đã áp dụng

- [[21 - Market Structure Shift]] — [[09 - Change of Character]] — [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[12 - Daily Bias]] — [[26 - OTE - Optimal Trade Entry]] — [[27 - Premium Discount]]
- [[20 - Liquidity Sweep]] — [[07 - Buy-side Liquidity]] — [[30 - Sell-side Liquidity]] — [[12 - Dealing Range]]
- [[02 - AMD]] — [[01 - ICT 2022 Model]]

## 6. Bài học rút ra

1. **IRL/ERL là công cụ đầu tiên để phân xử "pullback hay MSS"**: luôn hỏi swing bị đe dọa có phải là protected/external swing (gốc của leg) hay chỉ một internal micro swing. Chỉ external swing mới có quyền tạo MSS thật.
2. **Retracement vượt sâu qua vùng OTE chuẩn (62–79%), tiến gần 100%, là một tín hiệu cảnh báo độc lập** — không cần chờ MSS xác nhận mới nghi ngờ bias; bản thân độ sâu bất thường của retracement đã là bằng chứng đáng ghi nhận.
3. **BSL/SSL sweep chất lượng cao (equal highs/lows) trước một cú đảo chiều làm tăng đáng kể độ tin cậy của giả thuyết MSS** — đúng theo bảng phân tầng Tier trong note MSS.
4. **Ranh giới quyết định cuối cùng luôn là accept (đóng cửa) vs reject (chỉ wick)** — không có ảnh chụp hay ước lượng nào thay thế được việc đọc đúng giá đóng cửa thật trên chart gốc.
5. **Đừng để "structure vẫn là HH/HL" ru ngủ bias** — đó là thông tin lagging; một MSS đang hình thành tại đúng protected swing quan trọng nhất là tín hiệu leading cần được ưu tiên xem xét nghiêm túc.

## 7. Câu hỏi cần chốt (chưa xác nhận)

- **Nến daily gần nhất đã đóng cửa dưới 1.305 chưa, hay chỉ wick chạm vùng rồi đóng lại bên trên?** Đây là câu hỏi quyết định duy nhất giữa Kịch bản A và B — cần Khang xem trực tiếp trên TradingView/FXReplay.
- **Nếu đã đóng dưới 1.305, đã có retest từ dưới lên chưa, và phản ứng tại đó là gì** (bị từ chối = xác nhận MSS, hay bật xuyên qua tiếp = MSS càng chắc)?
- **Khung thời gian nhỏ hơn (H4/H1) có MSS/displacement nào xác nhận đồng pha không** — theo đúng logic đa khung trong note MSS (HTF cho hướng, LTF cho timing)?
- Symbol/ngày chart chính xác nếu Khang muốn dùng case này để backtest thật (hiện tại đang dùng làm case học tập nguyên lý).

## 8. Next steps

- Nếu Khang xác nhận được câu hỏi mục 7 (accept/reject), cập nhật note này với kết luận cuối cùng, hoặc tạo một backtest note riêng trong `04 - Backtesting/` nếu quyết định dùng case này cho một demo/backtest trade thật.
- Nếu muốn luyện phản xạ, có thể quiz thêm các case tương tự để rèn kỹ năng đọc nhanh 6 tiêu chí này trên chart sống, thay vì chỉ áp dụng lý thuyết.
- Cân nhắc lưu ảnh chart gốc vào `10 - Market Analysis/Attachments/` (tên gợi ý `EURUSD-20260719-D1-1.png`) để tham chiếu chính xác về sau.

---
*Ghi chú: phiên phân tích dựa trên ảnh chart Khang gửi trong chat (FXReplay, EURUSD Daily, giai đoạn ước tính Jun/2012–Mar/2013); `date` = ngày thực hiện phân tích (VN, UTC+7), không phải ngày trên chart. Không log backtest vì không vào lệnh — đây là note phân tích/watchlist + framework học tập. Các mức giá trong note là ước lượng đọc từ ảnh, không phải giá trích xuất chính xác.*
