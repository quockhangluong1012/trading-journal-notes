---
type: ict-concept
concept: Draw On Liquidity (DOL) — Deep Research
aliases:
  - DOL
  - Draw on Liquidity
  - Institutional Target
  - The Draw
tags:
  - trading/ict/concept
  - trading/deep-dive
  - liquidity
  - bias
  - d1-h1-m5
  - 2022-model
status: tested
category: Liquidity
timeframes:
  - D1
  - H1
  - M5
models:
  - ICT 2022 Model
  - PO3/AMD
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
importance: 5
confidence: 4
last_reviewed: 2026-09-13
created: 2026-09-13
updated: 2026-09-26
prerequisites:
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[19-Liquidity]]"
  - "[[16-Internal-External-Range-Liquidity-IRL-ERL]]"
  - "[[59-Daily-Bias]]"
  - "[[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]]"
common_mistakes:
  - dùng pool đã quét làm DOL
  - nhầm Judas target với DOL
  - đặt DOL quá xa reach phiên
  - sửa DOL giữa lệnh
  - short vào SSL trong uptrend (counter-DOL trap)
run_tag: dol-ict-liquidity-bias-6bb05c
---

> Tóm tắt định hướng: Draw on Liquidity (DOL) là pool thanh khoản tiếp theo mà giá đang được đưa tới — đích đến của leg hiện tại. DOL NUÔI daily bias chứ không đồng nhất với nó. Trong cùng một khung thời gian nắm giữ, pool GẦN nhất chưa bị quét theo hướng bias là DOL hành động làm T1; pool khung lớn xa hơn là T2/runner và quyền phủ quyết về khối lượng. Toàn bộ bài này trình bày DOL như một bộ lọc quy trình có cổng loại trừ và điều kiện vô hiệu viết trước — không phải tín hiệu dự báo chắc chắn. Bạn sẽ đi qua 7 phần: DOL là gì, DOL khác bias ra sao, bản đồ pools và thứ bậc, SOP 7 bước đầu ngày, case uptrend nhiều swing low, bộ lọc confluence, lỗi sai và checklist journal cho trader quỹ. Mọi ngưỡng số trong bài (reach phiên, kích thước FVG, R:R, giờ killzone, % size) là thực hành từ nguồn thứ cấp, cần tự kiểm chứng trên data của bạn; bài nhắc lại cảnh báo ở những chỗ trọng yếu nhất thay vì gắn vào từng con số.

## 1. Draw on Liquidity là gì — định nghĩa gốc và bản chất dòng tiền

Mỗi sáng bạn chỉ cần trả lời một câu trước khi mở chart khung nhỏ: hôm nay giá đi ĐÂU? Không phải mô hình nào đẹp, không phải Order Block (OB — cây nến đối ứng cuối cùng trước cú di chuyển mạnh) nào sáng mắt, không phải Fair Value Gap (FVG — khoảng mất cân bằng ba nến) nào chưa lấp. Mà là thuật toán đang đưa giá tới đâu. Câu trả lời chính là Draw on Liquidity, gọi tắt là DOL hay the draw.

Định nghĩa gốc được dạy nhất quán qua nhiều nguồn ICT độc lập: DOL là pool thanh khoản quan trọng tiếp theo mà giá đang được đưa tới — đích đến của institution trong phiên hoặc leg hiện tại [^S1]. Một cách diễn đạt khác nhưng cùng nội dung: DOL là pool gồm resting orders (lệnh chờ, stop) hoặc inefficiency chưa lấp mà giá đang được deliver về phía nó — nam châm hiện tại của thị trường [^S2]. Cách thứ nhất nhấn mạnh *ai* đưa giá đi, cách thứ hai nhấn mạnh *cái gì* hút giá.

Vì sao giá phải đi từ liquidity tới liquidity? Hình dung một quỹ cần mua 500 hợp đồng NQ long: sổ lệnh chỉ khớp vài chục hợp đồng ở giá tốt rồi trượt dần, nên giải pháp duy nhất là đi tới nơi đã có sẵn khối lượng đối ứng khổng lồ đang chờ.

Bên dưới overnight low có một pool Sell-Side Liquidity (SSL — thanh khoản phía bán dưới các đáy): hàng nghìn sell stop của retail nằm đó. Giá được đẩy xuống quét qua pool đó, các sell stop kích hoạt tạo ra khối lượng bán khổng lồ trong vài giây, bên mua lớn khớp lệnh mua với trượt giá tối thiểu. Xong việc giá đảo lên vì không còn lý do giữ giá ở đó [^S3]. Đó là bản chất dòng tiền của DOL: size lớn cần counterparty, pool là kho counterparty có địa chỉ biết trước — hành trình giá là hành trình đi lấy hàng. Khung lý thuyết đứng sau trong ICT gọi là IPDA — Interbank Price Delivery Algorithm: giá được đưa qua lại giữa các pool lệnh và vùng inefficiency cần cân bằng lại. Bạn không cần tin IPDA là cỗ máy có thật. Hãy dùng nó như bản đồ làm việc: đích đến đặt tên được, viết ra giấy được, chấm điểm được cuối ngày [^S2].

Ba thuật ngữ nền tảng cần nắm trước khi đi tiếp. Thứ nhất, liquidity pool: vùng giá tập trung nhiều stop-loss và breakout orders; khi giá chạm tới, lượng lớn lệnh thị trường kích hoạt cùng lúc. Hai loại lớn nhất là Buy-Side Liquidity (BSL — trên các đỉnh cũ, equal highs, Previous Day High) và SSL (dưới các đáy cũ, equal lows, Previous Day Low) [^S1].

Thứ hai, dealing range: khung giá giữa một đỉnh và một đáy swing quan trọng trên một timeframe; mọi khái niệm khác sống bên trong khung này [^S4]. Đỉnh đáy khung gọi là External Range Liquidity (ERL — thanh khoản ngoài vùng), các mức bên trong như FVG, OB, equal highs/lows nội bộ gọi là Internal Range Liquidity (IRL — thanh khoản trong vùng). Điểm giữa 50% gọi là equilibrium (EQ), chia khung thành premium (nửa trên, chỉ tìm bán) và discount (nửa dưới, chỉ tìm mua).

Thứ ba, IRL draw và ERL draw. Mỗi lệnh hoàn chỉnh có hai đích đến song song: IRL draw là pool bên trong range, dùng làm T1 chốt một phần (thường 50% và dời stop về breakeven — hòa vốn); ERL draw là pool ngoài range, dùng làm T2 cho runner giữ tiếp [^S1]. Công thức chuẩn: T1 tại IRL chốt 50%, T2 tại IRL thứ hai 25%, T3 tại ERL 25%. Chu kỳ luân phiên là ERL collection → IRL retracement → ERL kế tiếp — vừa quét external xong thì giá thường hồi về internal trước khi expand tiếp [^S4] [^S5]. Câu cần thuộc lòng: mỗi chu kỳ AMD (Accumulation — tích lũy, Manipulation — thao túng, Distribution — phân phối) hợp lệ đều có draw định trước; entry mà không có draw là trade không có đích đến, và không có draw thì không có trade [^S1].

Ứng dụng mạnh nhất của DOL là quyết định hướng Judas Swing (cú quét thao túng đầu phiên). Trong mô hình AMD/PO3 hợp lệ, Judas quét pool phía NGƯỢC với draw: ngày bullish với draw là BSL trên thì Judas quét SSL dưới trước khi phân phối lên; ngày bearish thì ngược lại [^S1]. Cơ chế: cần counterparty từ cú quét để fill lệnh lớn trước khi deliver về đích. Điều kiện đi kèm quan trọng không kém phát biểu chính: đó mới là Judas khi cú quét nằm đúng pha manipulation, theo sau là close back inside và displacement ngược phía bị quét; mở phiên không sweep ngược draw, hoặc có sweep mà không displacement, thì đừng gắn nhãn Judas — ép price action vào nhãn này là cách narrative tự chữa mình phổ biến nhất. Biết draw trước giờ mở phiên là biết canh Judas phía nào — và phía nào tuyệt đối không entry.

Hai loại nam châm hành xử khác nhau khi giá tới nơi. Resting liquidity (old high/low, equal highs/lows, session extremes) thường tạo sweep-and-reverse (quét rồi đảo) hoặc run-and-continue (quét rồi chạy tiếp). Inefficiencies (FVG, New Week/Day Opening Gap — khoảng trống mở cửa tuần/ngày, liquidity void sau tin) thường tạo fill-and-continue (quay về lấp rồi đi tiếp) [^S2]. Biết mình target loại nào mới biết nên kỳ vọng chốt đảo chiều hay giữ tiếp; logic luân phiên ERL→IRL→ERL đã nêu ở thuật ngữ IRL/ERL draw áp dụng cho draw ngắn hạn. Cấm dùng cách đọc này để chữa lùi: pool bị quét rồi chạy tiếp không biến một cú quét thất bại thành hóa-ra-là-run.

Khung trung thực cho cả bài: pools là có thật, cơ chế quét lấy đối ứng là có thật, staging IRL trước ERL là quản trị hợp lý. Nhưng khả năng gọi tên trước một pool cụ thể và tuyên bố đó là đích đến chắc chắn của hôm nay thì chưa được chứng minh. Học thuật gần gũi nhất là nghiên cứu của Carol Osler tại Fed New York (Journal of International Money and Finance), DOI 10.1016/j.jimonfin.2004.12.002 [^S6].

Cơ chế vi mô giải thích vì sao cùng một level vừa hay fade vừa hay break mạnh: stop clusters nằm TỤ TRÊN/DƯỚI round number (chừng 10% lệnh khớp đúng số tròn; stop-buy đã khớp tập ở digits 01–10 nhiều gấp đôi vùng đối xứng, 14,3% so với 6,9%), trong khi take-profit cụm ngay AT round number và hay gây reversal (giá chạm round đảo chiều 59,3% so với 54,8%, 46/58 khoảng). Vì vậy cross qua cụm stop thì giá tăng tốc, còn chạm take-profit cluster thì fade — hai hành vi trái ngược trên cùng một mức giá đều hợp lý. Response của stop cũng lớn và lâu hơn: reversal do TP thường đóng trong dưới 30 phút, acceleration do crossing kéo dài ≥2 giờ [^S6].

Simulation evidence duy nhất trong corpus ngả về phía sweep có chủ đích là agent-based model trên limit-order-book lịch sử (Liston, Gretton & Lensky, Proceedings of ICAART 2024 vol.1, tr.280–288): nạp stop-loss vào thị trường giả lập tự tạo volatility và cascade potential, và CẤU TRÚC stop-loss order book đủ để một agent lợi dụng time các event cascade mà hưởng lợi [^S7]. Đây là bằng chứng mô phỏng, không phải đo đạc — nó chứng minh tính khả thi cơ chế, không chứng minh cơ chế đang chạy trên NQ hôm nay.

Từ dữ liệu thật, chính Osler đặt ra kỷ luật quan trọng nhất: round-crossings xảy ra khoảng 5 lần mỗi ngày nhưng cascade thật chỉ khoảng 1 lần mỗi tuần; causality không được chứng minh; hiệu ứng chỉ kéo dài hàng giờ, không nói gì về daily bias; round numbers khác swing high/low — đừng đánh đồng hai loại mức giá [^S6]. Tóm lại: chạm pool phần lớn là nhiễu; DOL chỉ giữ được giá trị đã kiểm chứng khi làm bộ lọc loại lệnh với selection rules — pool nào, ngày nào, confluence gì — chứ không phải tín hiệu dự báo [^S8].

> DOL tuyên bố và không tuyên bố: DOL tuyên bố mỗi leg có đích đến đặt tên được kèm giá, Judas quét ngược draw, staging IRL rồi ERL giúp chuẩn hóa chốt lời. DOL không tuyên bố mọi pool đều bị nhắm tới, chạm pool nào cũng đảo chiều, DOL đúng là lệnh thắng. DOL là giả thuyết về đích đến cộng bộ lọc loại lệnh — không phải dự báo chắc chắn.

## 2. DOL khác daily bias ở điểm nào — bảng phân biệt và mối quan hệ

Nhiều trader giỏi entry vẫn thua vì có DOL đúng nhưng bias sai, hoặc bias đúng nhưng không có DOL nên vào ở vị trí tệ. Luận điểm mà bằng chứng hội tụ mạnh nhất: DOL NUÔI daily bias, chứ không đồng nhất với nó — DOL là input cần-nhưng-không-đủ của bias [^S9]. DOL trả lời: giá đi ĐÂU — pool cụ thể, giá cụ thể, loại resting hay inefficiency, tầng IRL hay ERL, đã quét hay chưa [^S1]. Daily bias trả lời: hôm nay đứng VỀ PHÍA NÀO — chỉ canh mua, chỉ canh bán hay đứng ngoài; Judas quét phía nào; entry ở đâu; vô hiệu khi nào [^S10]. Mối quan hệ giữa hai khái niệm nằm ở hàng Quan hệ nhân quả của bảng dưới đây.

| Tiêu chí | DOL | Daily bias |
|---|---|---|
| Định nghĩa | Pool cụ thể gắn giá: resting orders (old high/low, PDH/PDL, PWH/PWL, EQH/EQL, session extreme) hoặc inefficiency (FVG, imbalance, NWOG/NDOG) [^S2] | Conviction hướng giao dịch cho cả session: bullish / bearish / no-trade, kèm phía bị quét, vùng entry, điểm vô hiệu [^S10] |
| Vai trò | Destination và target (IRL làm T1 chốt một phần, ERL làm T2 runner). Quyết định hướng Judas: Judas luôn quét NGƯỢC draw. DOL là target, KHÔNG BAO GIỜ là entry; entry tới từ PD array (OTE, OB, FVG) trên đường đi [^S1] | Filter và execution plan: chọn phía được trade, loại setup ngược bias, định nghĩa chân manipulation vs distribution trong AMD, gắn invalidation và sizing. Không bias rõ thì không entry dù POI đẹp [^S1] |
| Timeframe | Tồn tại ở mọi timeframe theo 4 tầng: intraday IRL, session ERL, weekly ERL, monthly ERL — mỗi timeframe một DOL, weekly có thể ngược intraday. HTF thắng LTF khi xung đột; intraday DOL phải trong session reach (NQ ~100–250 points, EUR/USD 50–150 pips — xa hơn là multi-day target) [^S1] | Thesis của NGÀY, suy top-down: weekly bias làm khung, daily structure làm lõi, intraday scenario làm chi tiết. D1 quyết định vì dòng tiền lớn định vị trên D1; H1/M15 chỉ confirm entry. Weekly profile và macro/news có thể override bias ngày [^S11] |
| Ổn định trong ngày | Bền tới khi bị tiêu thụ hoặc bác bỏ. Hai sự kiện buộc chọn lại: pool bị lấy (trade through kèm displacement, hoặc sweep kèm close đảo chiều — pool spent, con lắc lật sang phía đối diện); pool đối diện bị run kèm acceptance (đọc sai, hủy idea ngay). **Cấm sửa DOL mid-trade** [^S2] | Ổn định theo phiên, chỉ revise khi có structural event. Move ngược bias trong manipulation phase KHÔNG phải invalidation — đổi bias lúc đó là vào sai phía tại điểm tệ nhất. Ngoại lệ: fresh D1 BOS/CHOCH/MSS ngược hướng, hoặc hard invalidation (daily body close vượt biên dealing range) [^S11] |
| Quan hệ nhân quả | Input và neo target/Judas: không DOL đặt tên kèm giá thì chưa có bias; nhưng DOL một mình không suy ra bias | Sản phẩm tổng hợp: DOL + structure (HH/HL, CHOCH/MSS, displacement có FVG hay grind) + location (premium/discount, EQ) + time (killzone, weekly-profile, news) + confirmation (AMD leg đã sweep đúng phía) [^S10] |
| Kiểm tra nhanh | Viết được DOL = pool tại giá X, loại resting/inefficiency, tầng IRL/ERL, unswept? Không viết được thì no-trade | Viết được Bias bullish/bearish/no-trade, vì weekly X cộng daily Y cộng DOL Z cộng location premium/discount cộng plan sweep A rồi entry B rồi target Z, invalid khi C. Nói tôi bullish mà thiếu vế sau là chưa có bias |
| Trùng vs tách | Khi TẤT CẢ factors đồng thuận (all-green), DOL và bias trùng nhau về thực hành — bẫy khiến người học xóa mất điểm phân biệt | Khi xung đột chúng tách nhau: uptrend vẫn có thể bearish-bias một session (daily correction tạo discount cho weekly continuation); sweep-then-flip theo next-day model đã nêu ở SOP [^S11] |

Công thức nhớ: DOL cho ĐÍCH; structure cho ĐƯỜNG; premium/discount cho VỊ TRÍ; time cho HÔM NAY. Thiếu một trong bốn, conviction hạ một bậc [^S9].

Phe thiểu số DOL suy ra bias dạy rất cơ học: trending up thì bias chạy PDH; trending down thì bias chạy PDL; sweep một phía nhưng fail to displace rồi close back inside thì bias đảo về phía đối diện — kèm next-day model [^S12]. Phiên bản mạnh nhất: không đặt tên được draw trong một câu thì bạn chưa có bias, chỉ có phỏng đoán [^S2].

Phe này đúng khi structure, location và time trung tính hoặc đồng thuận; trường hợp tổng quát, DOL và ba yếu tố kia thường xuyên mâu thuẫn, lúc đó DOL-bằng-bias sụp đổ [^S9].

Bằng chứng asymmetry mang tính quyết định: cả hai nguồn mechanical đều tự chứa cửa thoát của phe đa số — sweep rồi close-back thì flip, consolidation thì no bias — tức thừa nhận cần structure-confirm và no-trade state [^S9]. Cộng thêm case uptrend vẫn bearish-bias một session khi magnet lớn gần nhất nằm dưới, và walkthrough EUR/USD daily SSL vs weekly BSL (size nửa, T1 only) — hai case mà DOL đơn độc cho đáp án sai hoặc thiếu. Corroboration độc lập: một guide daily bias khác đặt bias từ weekly trend, nến daily, HTF FVG/OB và macro mà KHÔNG nhắc DOL — bias là framework riêng [^S13].

Thứ bậc xử lý xung đột để tra cứu mỗi khi bối rối. Rule 0 — No-draw/no-bias thì no-trade: không đặt tên được 1 IRL (T1) cộng 1 ERL (T2) unswept theo hướng bias trước killzone thì nghỉ [^S1]. Rule 1 — HTF structure veto (weekly thắng daily thắng intraday): weekly vs daily ngược nhau thì daily move là correction; trade ngược weekly thì max nửa size, T1 only, không runner. Rule 2 — Unswept và timeframe-weight veto: swept pool bị loại; nearest UNSWEPT cùng hướng bias là IRL (T1); monthly thắng weekly thắng daily thắng session thắng Asian; quá xa session reach thì coi như Rule 0. Rule 3 — Premium/discount veto: bullish chỉ optimal trong discount, bearish chỉ trong premium; đúng hướng sai zone thì chờ Judas quét về phía đối diện — London move ngược draw là setup, không phải invalidation. Rule 4 — Time/news veto: tin đỏ, Asian close giữa range, weekly-profile ngày reversal, ngoài killzone thì hạ size hoặc skip; chưa có manipulation sweep đúng phía kèm displacement thì bias mới là hypothesis [^S9].

## 3. Bản đồ liquidity — các pool cạnh tranh và thứ bậc chọn DOL chuẩn

Tài liệu chứa hai phe, đều có văn bản hậu thuẫn.

Phe A — Nearest-first: bullish bias thì scan phía trên tìm nearest unswept BSL (equal highs, PDH, Asian Range High, PWH) — pool gần nhất đó là IRL draw (T1); bearish thì mirror xuống dưới; ERL draw beyond IRL làm T2. Lý do: draw quá xa không phải intraday DOL hành động được; kết luận đúng khi đó là no actionable IRL draw, nghĩa là no trade [^S1].

Phe B — Furthest-magnet: weight draws by timeframe, HTF pool thắng nearby one — Asia high 15 phút không bằng PWH. Mark HTF pools trước (PWH/PWL, PDH/PDL, old high/low untouched, equal highs/lows, large daily FVG chưa fill), mỗi phía giữ 1 ứng viên. PWH/PWL là pool 5 ngày gom stops nên sweep cho move lớn và bền hơn PDH/PDL; PDH xấp xỉ PWH chồng nhau là double-stacked BSL conviction cao nhất tuần [^S4]. Nếu chỉ watch 1 level thì watch PDH/PDL trước, thứ hai mới là Asia high/low [^S14].

Cách resolve giữa hai phe: không tồn tại một DOL duy nhất cho mọi holding period — chuẩn là 1 DOL mỗi timeframe. Cùng timeframe và holding period thì nearest UNSWEPT theo hướng bias thắng làm T1; khác timeframe thì HTF outrank nhưng chỉ để veto và size (giảm nửa size khi xung đột), không thay thế T1 [^S15]. Đây là suy luận hòa giải của báo cáo, không phải đồng thuận nguyên văn của corpus: một transcript gốc ICT nói rõ thứ tự chọn draw, hoặc một backtest 60–100 phiên ghi DOL trước giờ mở, đủ sức lật cách resolve này.

Sáu quy tắc áp dụng. Một, trade timeframe nào thì commit DOL của timeframe đó; khi xung đột HTF thắng — mẫu EUR/SSL-vs-weekly-BSL ở cuối §5 là khuôn chuẩn: short daily nhưng nửa size, T1-only [^S1].

Hai, trong cùng timeframe: nearest UNSWEPT theo hướng bias là DOL hành động (T1); pool HTF xa hơn là T2/runner. Pre-session mark đủ 4 tiers đã liệt ở bản đồ trên, mỗi tầng một vai trò target [^S1].

Ngoại lệ của chính quy tắc này: ngày expansion run-and-continue, giá có thể xuyên thẳng qua IRL/T1 mà không phản ứng — partial tại T1 khớp muộn hoặc không khớp; thân nến đóng ngoài IRL kèm continuation là tín hiệu chuyển kỳ vọng sang ERL. Đặt T1 tại pool gần nhất vì vậy không hàm ý mọi pool gần đều phải tạo phản ứng.

Ba, swept bằng spent bằng loại: pool đã quét kèm displacement rời đi là hết magnet, reselect thường về phía đối diện. Phân biệt ba kịch bản tại pool: sweep-and-reverse (râu dài vượt rồi đóng quay vào — đảo vai, sóng thật ở hướng ngược); breakout-and-acceptance (giữ phía ngoài, xây cấu trúc ngoài — continuation, DOL cũ vẫn sống, không fade); touch-no-sweep (quay đầu không phá qua — thanh khoản còn nguyên) [^S16].

Bốn, tie-break khi hai ứng viên trên/dưới đều khả thi: vị trí trong dealing range — premium thì draw xác suất cao là sell-side dưới, discount thì buy-side trên; market hiếm khi deliver từ premium lên premium cao hơn mà không rebalance [^S2]. Premium đồng thuận cả 3 tầng (monthly+weekly+daily) mới max conviction; chống 1 tầng thì giảm size hoặc bỏ runner [^S4].

Năm, xác nhận bằng displacement chứ không bằng cảm giác: cần fast full-bodied leg phá structure về phía candidate cộng để lại FVG; râu dài drift chồng lấn là chưa chọn [^S2]. Tám tiêu chí DOL-chuẩn chấm mỗi sáng (đủ 5/8 = high confidence): unswept-visible-trong-5-giây, cùng hướng weekly cộng D1, phía đối diện vừa spent, location ủng hộ, displacement xác nhận, PDH/PDL-mechanical đồng thuận, macro/Asian/weekly-profile không chống, IRL trong tầm phiên cộng R:R ≥ 1:2 [^S17].

Sáu, order flow làm tie-break động: khi hai ứng viên ngang tier, hướng thắng là hướng chuỗi break/rejection hiện hành — bullish order flow là phá LÊN các đỉnh sau khi bị từ chối DƯỚI các đáy (mirror cho bearish). Thứ bậc không đóng băng lúc pre-session: mỗi pool bị break hoặc rejection trong phiên là ranking đọc lại theo sequence mới. Nguồn này xếp DOL là ưu tiên số một của toàn bộ phân tích, trước mọi setup [^S18].

Bản đồ 4 tiers mỗi sáng (đúng phân tầng đã nêu ở bảng §2): intraday IRL gồm equal highs/lows trong range, PDH/PDL, ARH/ARL, NY AM high/low, news wick; session ERL là boundary; weekly ERL làm T2; monthly ERL làm multi-day runner [^S1]. Cluster 2–3 PDH chồng nhau trong 10 pips là pool dày gấp đôi.

PDH/PDL là Tier-3 BSL/SSL nhưng đáng tin nhất intraday: visible nhất trên chart — mọi retail đều mark, mọi breakout system đều trigger từ đó — nên institutions target đầu tiên [^S19]. Hai nguồn độc lập xác nhận bộ bốn PDH/PDL/PWH/PWL nằm trong nhóm DOL targets bị đánh trúng ổn định nhất (nested liquidity map cho phiên), và PWH/PWL tích tụ stop năm phiên nên sweep cho move lớn hơn [^S20] [^S21].

Ba vai trò của PDH/PDL: Judas target (bearish thì PDH, bullish thì PDL); IRL target đầu tiên trước external; dealing range reference. Quy tắc vận hành đã nằm ở SOP Bước 3: mark trước London open, entry sau sweep cộng MSS chứ không tại level, target là PDH/PDL đối diện làm T1 [^S19].

Quy tắc flip hai tầng. Tầng selection (khi nào SSL dưới thành DOL mới) cần BSL-trên-swept cộng displacement/CISD/body-close-beyond cộng premium location. Tầng execution cần body-close verdict — close-back-inside thì sweep confirmed, cấm entry trước close; wick đơn độc không displacement mặc định KHÔNG flip — vẫn là fuel. Nếu mọi râu nến đều lật được DOL thì DOL giải thích được mọi kết cục — tức không kiểm chứng được.

Hiệu chỉnh mục tiêu theo tầng pool bị quét: quét Tier 1–2 (equal highs/lows tháng/tuần, weekly extremes) mới nuôi runner về ERL tuần; Tier 3–4 (PDH/PDL, Asian extremes) chỉ kỳ vọng intraday tới pool đối diện cùng session; Tier 5–6 (intraday equal highs/lows, single swing) chỉ scalp về mốc nội bộ gần nhất [^S3]. Quy đổi sang thị trường của vault: GBPUSD dùng đúng bộ mức PDH/PDL/PWH/PWL như EURUSD vì hai cặp cùng chạy bằng đô-la-flow và reach phiên tương đương; XAUUSD có cấu trúc pool mỏng hơn — extreme theo ngày và round-number clusters đóng vai trò BSL/SSL chính, reach phiên rộng nên ngưỡng quá-xa phải đo lại bằng ADR vàng thay vì pip forex [^S2].

## 4. SOP đầu ngày mới — quy trình xác định DOL từng bước

SOP 7 bước thống nhất, làm trong 10–15 phút trước London hoặc New York killzone. **Nguyên tắc sắt: viết DOL ra giấy với GIÁ cụ thể trước giờ mở phiên** (DOL = PDH 21,640). Không viết được thì không trade [^S1]. Đầu mỗi sáng chỉ chấm tối đa hai ứng viên DOL có giá — một trên, một dưới; ứng viên không nhìn ra trong 5 giây thì đó không phải DOL hôm nay [^S8].

Ba trường phái mâu thuẫn về điểm bắt đầu. A — weekly-first top-down (LiquidityScan): chắc, không đánh ngược dòng tiền lớn, giải thích được correction trong trend; nhược: nặng, chậm, người mới dễ bỏ qua PDH/PDL intraday. B — PDH/PDL-mechanical (TTrades, TradingEdge): cực nhanh, kiểm chứng được bằng close nến D1; nhược: mù HTF, dễ short ngay giữa correction của weekly bullish, bỏ premium/discount và macro/news. C — D1-order-flow-first (Strefa): cân bằng bias vs imbalance (giá có thể ghé FVG trước rồi mới tới liquidity); nhược: thiếu weekly profile và Asian/midnight gating [^S17]. Chuẩn hòa giải: weekly-first làm khung, D1-order-flow làm lõi, PDH/PDL-mechanical làm trigger — A cho phép/cấm hướng, C chọn đích, B xác nhận bằng sự kiện giá đóng. Thứ bậc veto khi xung đột: macro/news > weekly ERL > D1 structure > PDH/PDL sweep > Asian/midnight vị trí. SOP này bỏ bước AI-confirmation của bản 7-step gốc — không phải ICT gốc — thay bằng midnight open cộng displacement check; close-vs-midpoint hôm qua chỉ là tín hiệu phụ trọng số gợi-hòa 2:1; Asian range dưới 30–40% ADR mà chưa sweep thì kỳ vọng Judas yếu [^S17].

Bước 1 — Khung tuần: cho phép hay cấm? Mở W1 cộng D1. Đọc weekly structure (HH/HL hay LH/LL), weekly DOL (PWH/PWL, equal highs/lows tuần chưa quét), giá premium hay discount của weekly range (EQ = (high cộng low)/2). Ghi weekly profile: Thứ 2 accumulation, Thứ 3 thiết lập trend, Thứ 4–5 continuation, Thứ 6 reversal/chốt lời [^S22]. Gắn nhãn: thuận weekly (full size, giữ runner) / ngược weekly (nửa size, T1 only). Chấm nhanh các cổng bên dưới: 6–7/7 đồng thuận = high confidence (bản 7-step gốc tự báo 75–85% win-rate full alignment — con số vendor, chưa kiểm chứng), 4–5 = medium, ≤3 = skip; single-factor fail ~40–50%. Thang song song của trường phái D1-core: 3/3 tín hiệu (order flow, imbalance, draw) = confident bias, 2/3 = conditional — hạ size, mỗi tín hiệu một hướng = no-trade [^S17].

Bước 2 — D1 order-flow cộng imbalance: lõi dự báo. Đọc D1 structure (HH/HL bullish, LH/LL bearish; MSS mới trên D1 là lập luận đảo chiều mạnh nhất). Điều kiện để một swing low ĐƯỢC TÍNH là swing: giá thực sự quay đầu khỏi nó và 1–2 nến xác nhận giữ nguyên mức đó — đáy của nến gần nhất chưa phải swing point; nến chồng lấn là range, không đọc hướng; HH/HL gãy khi giá không tạo higher low mới mà đóng THÂN dưới swing low trước (wick chưa tính) [^S23]. Chỉ swing low CONFIRMED gần nhất là mốc cấu trúc — đáy thấp hơn nó chỉ là pool inventory.

Quét FVG D1/H4 chưa lấp cộng NWOG/NDOG cộng weekly gap, close hôm qua vs midpoint (trên midpoint nghiêng continuation — tín hiệu phụ, trọng số 2:1) [^S11]. Veto: D1 sideways, không FVG lớn, giá kẹt giữa EQ — bias unreadable, NO-TRADE.

Bước 3 — Bản đồ 4 tầng cộng chọn IRL-T1 / ERL-T2. Mark PDH/PDL, session high/low, news wick, NY AM high/low hôm qua, cộng PWH/PWL, equal highs/lows, swing D1/H4 [^S14]. Chốt IRL-T1 là pool CHƯA QUÉT gần nhất theo hướng bias; ERL-T2 là pool NGOÀI range. Pool đã quét kèm displacement là SPENT — gạch bỏ; pool chỉ quét râu mà close back inside thì còn hiệu lực nhưng nghiêng đảo chiều theo next-day model [^S12]. Veto: không IRL nào trong tầm phiên (BSL gần nhất vượt xa ADR — kiểu 800 NQ points) thì NO-TRADE intraday; BSL trên và SSL dưới cách đều cộng weekly ở EQ thì accumulation — NO-TRADE [^S1].

Bước 4 — Premium/discount cộng midnight open: cổng location. Fibonacci range D1/H1 gần nhất: trên 50% là premium (chỉ short), dưới 50% là discount (chỉ long); intraday lấy PDH tới PDL làm range ngắn hạn. Cộng midnight open 00:00 ET: giá trên midnight nghiêng bullish, dưới nghiêng bearish [^S24]. EQ = (Range High cộng Range Low) / 2; OTE short ở 0.618/0.705/0.786, OTE long ở 0.382/0.295/0.214; entry ở EQ xác suất thấp trừ khi triple confluence đúng 50% [^S25]. Veto: bias bullish mà giá premium (hoặc bearish ở discount) thì KHÔNG market entry — chỉ chờ Judas quét về phía đối diện.

Bước 5 — Macro cộng calendar cộng Asian range: cổng thời điểm. Check DXY, risk-on/off, lịch đỏ 24h tới (FOMC/NFP/CPI override mọi structure — dời entry ra sau tin hoặc nghỉ) [^S22]. Đọc Asian high/low cộng close: close sát ARL là sellers kiệt — nghiêng bullish; close giữa thì confidence thấp. Veto: tin đỏ trong killzone định đánh thì SKIP window; Asian range dưới 30–40% ADR mà chưa sweep thì Judas yếu — giảm size hoặc chờ New York.

Bước 6 — Viết scenario PO3 (Power of Three) cộng hướng Judas. Viết 1 câu: Bias → DOL IRL-T1 giá X, ERL-T2 giá Y → Judas quét pool đối diện giá Z ở London/NY → entry FVG/OB sau MSS M5/M15 → T1 chốt 50% cộng BE, runner tới ERL. Trong mô hình AMD/PO3 hợp lệ, Judas quét ngược DOL [^S1]. Veto: không viết được Judas target cụ thể thì NO-TRADE; R:R tới T1 tối thiểu 1:2, array tới DOL dưới khoảng 2R thì bỏ dù array đẹp [^S2].

Bước 7 — Xác nhận trong phiên: sweep rồi displacement/MSS rồi FVG. Trong killzone (quy đổi giờ ET sang giờ Việt Nam: cộng 12 giờ mùa EST, 11 giờ mùa EDT — London 2–5AM ET ≈ 14:00–17:00 VN; NY 7–10AM ≈ 19:00–22:00 VN; Silver Bullet 10–11AM ET ≈ 22:00–23:00 VN): chờ sweep pool đối diện DOL; chờ displacement thân lớn kèm phá structure cộng FVG theo hướng DOL; limit 50% CE FVG (Consequent Encroachment), SL vượt râu sweep có buffer, TP theo IRL rồi ERL. Chỉ trade FVG hình thành SAU khi window mở — FVG cũ là stale [^S26]. Veto intraday: FVG không sweep trước trong window thì skip; displacement yếu thì skip; D1/H1 body close vượt biên ngược bias (hard invalidation) thì hủy bias đọc lại từ weekly; Judas chạy quá xa không hồi (soft invalidation) thì đứng ngoài tới close phiên.

Checklist 5 điểm trước nút bấm: window active? bias cộng DOL đã viết? sweep trong window? FVG sạch từ displacement? R:R đạt 1:2 tới T1? Một Không là skip.

## 5. Case study trend tăng HH/HL, nhiều swing low bên dưới — áp dụng thực tế

Đây là tình huống bạn hỏi trực tiếp: W1 bullish, D1 tạo chuỗi higher high/higher low, và bên dưới chân bạn là cả một chồng swing low chưa quét. Trực giác người mới (dưới nhiều low thì giá về lấy low) đi ngược đáp án đúng.

Bối cảnh giả định theo walkthrough NQ gốc (khung số chỉ là ví dụ dạy học — thay bằng giá thực tế của bạn): W1 bullish, D1 HH/HL rõ với S1 21,186 (sâu nhất, chưa quét), S2 21,298, S3 21,332 (cũng là ARL hôm qua), S4 21,372 (gần nhất). Giá 21,388. PDH 21,640 (chưa quét), PWH 21,840 (chưa quét). D1/H4 còn FVG 21,390–21,508 ngay dưới giá. Không tin đỏ. Thứ 3 — ngày thiết lập trend trong weekly profile [^S1].

Chạy SOP. Bước 1 Weekly: bullish cộng Thứ 3 — cho phép long full size, giữ runner — PASS (thuận weekly). Bước 2 D1: HH/HL bullish, không MSS ngược; FVG ngay dưới giá có thể ghé trước; close hôm qua trên midpoint — nghiêng continuation — bias thô BULLISH [^S11]. Lưu ý cấu trúc: S4 21,372 chỉ là swing low hợp lệ nếu đã có 1–2 nến xác nhận quay đầu; chưa confirmed thì mốc cấu trúc vẫn là S3, mọi mức dưới chỉ là inventory [^S23].

Bước 3 — CÂU TRẢ LỜI TRỌNG TÂM: các SSL S1–S4 KHÔNG phải bearish DOL. Trong uptrend HH/HL cộng bias bullish, chúng là Judas fuel — nhiên liệu cho quét — không phải đích đến. Chỉ khi Bước 1/2 đảo (weekly bearish cộng D1 MSS xuống cộng displacement xuống cộng IRL-T1 trên bị lấy) thì SSL mới thăng cấp thành DOL. Chốt: IRL-T1 = PDH 21,640 (BSL gần nhất chưa quét theo hướng bias); ERL-T2 = PWH 21,840; Judas target = ARL/S3 21,332, dự phòng S1 21,186 nếu quét kép. FVG 21,390–21,508 là internal pit-stop: giá có thể tap rồi mới expand — đúng luân phiên external/internal [^S2]. PDH/PWH chưa quét — VALID; S4/S3/S2 dễ bị quét râu — không đặt SL dưới đó.

Bước 4 Location: giá 21,388 dưới midnight open, trong discount range ngắn hạn, ngay trên FVG — ĐẸP cho long — PASS [^S25]. Bước 5 Macro/Asian: không tin đỏ; Asian 21,340–21,420 close sát ARL — sellers kiệt — ủng hộ London quét SSL rồi lên — PASS.

Bước 6 Scenario: Bullish → DOL PDH 21,640 (T1) → PWH 21,840 (T2) → Judas quét ARL 21,332 (sâu nhất 21,186) ở London → long FVG sau MSS M5 → T1 chốt 50% cộng breakeven, runner tới ERL.

Bước 7 diễn biến mẫu: London quét ARL 21,332 (body close back inside 21,348) → displacement cộng BOS M5 cộng FVG 21,390–21,508 → limit 50% CE khoảng 21,444–21,449, SL dưới râu Judas 21,290. T1 PDH hit — chốt 50% cộng breakeven; runner giữ tới PWH [^S1]. Khớp walkthrough NQ: IRL PDH 21,640 cho T1 196 điểm/1.3R lúc 11:04 sáng, ERL PWH 21,840 cho runner 396 điểm/2.6R [^S1]. Chuẩn bị trước diễn biến ngược: London quét ARL rồi displace thẳng qua PDH không chạm entry là expansion run-and-continue — đừng fade, đọc lại luân phiên ERL→IRL cho leg kế tiếp.

Ghi chú trung thực BẮT BUỘC: entry khoảng 21,444, SL 21,290 thì T1 cách 196 pts / risk 154 pts — khoảng 1.3R — chấp nhận được cho runner-style nhưng nếu bạn đòi tối thiểu 1:2 thì phải chờ entry sâu hơn hoặc skip. Đừng lặng lẽ sửa 1.3R thành 2R cho đẹp journal.

Invalidation viết sẵn trước lệnh: NẾU London quét thủng S1 21,186 kèm displacement xuống cộng close dưới thì HỦY bias bullish, không long, đọc lại từ weekly; lúc đó SSL mới thành DOL bearish.

| Tiêu chí | Judas fuel | Bearish DOL thật |
|---|---|---|
| Bias cộng vị trí | Bullish HTF (weekly bullish, daily HH/HL), giá discount; SSL đối diện DOL BSL trên | Bearish HTF hoặc mất bullish: daily LH/LL, giá premium, displacement xuống |
| Lịch sử sweep | SSL chưa quét, dày lên sau mỗi test — chờ sweep | BSL trên vừa bị sweep cộng CISD/CHOCH bearish đóng dưới, hoặc range high bị body-close xuyên — flip |
| Vai phiên | Asia/London sweep ARL/PDL/equal lows rồi close back inside cộng MSS — long về PDH/PWH theo AMD [^S27] | London/New York sweep PDH/PWH rồi hold beyond cộng build structure cộng displacement xuống — short tiếp, retest PDH cũ làm kháng cự [^S28] |
| Cách trade | KHÔNG short vào Judas sweep; chờ MSS rồi long, stop dưới wick, T1 PDH, T2 PWH [^S1] | KHÔNG bắt đáy SSL; chờ sweep BSL cộng MSS bearish rồi short, stop trên wick, T1 PDL, T2 PWL [^S29] |
| Chuyển vai | Khi T1 cộng T2 tăng đã delivered (PDH cộng PWH swept cộng displace rời đi) thì SSL từ fuel thành DOL leg mới (pendulum flip) | Khi leg giảm sweep PDL/PWL cộng bullish CHOCH đóng trên thì DOL giảm spent, flip lại bullish [^S12] |

Lỗi kinh điển: nhầm Judas target với DOL — short vào Judas sweep SSL trong ngày bullish — directional error phổ biến nhất: draw luôn nằm ở hướng phiên phân phối tới — phía ngược Judas [^S1]. Các lỗi còn lại: dùng low đã quét làm DOL; long từ premium sau khi giá chạy tới PDH mà không chờ sweep; dời T1 lên T2 giữa lệnh [^S2].

Case xung đột ngắn để đối chiếu — EUR/USD: daily bearish nhắm SSL 1.08220 nhưng weekly bullish nhắm BSL 1.09180 — quyết định mẫu là vẫn lấy short daily nhưng giảm nửa size, chỉ T1, không runner, đóng toàn bộ ở T1 rồi chờ long weekly từ đó [^S1]. Đó là khuôn mẫu mọi ngày khung lớn và khung nhỏ kéo ngược nhau.

## 6. Điều kiện confluence xác nhận DOL — bộ lọc chuẩn

Mọi ngưỡng số trong mục này là số thực hành từ nguồn thứ cấp — cần tự kiểm chứng trên data của bạn.

Tài liệu liệt kê khoảng 7 nhóm confluence nhưng không xếp hạng. Cách dùng được là chia ba tầng theo hình phạt khi thiếu: veto (thiếu một là nghỉ), cổng bắt buộc (thiếu thì bỏ hoặc hạ cấp theo cây quyết định), nice-to-have (chỉ scale size, không bao giờ cứu setup thiếu cổng).

Tầng veto — thiếu một là đứng ngoài. Veto 1: DOL đặt tên TRƯỚC giờ vào lệnh — pool cụ thể có giá, loại, trạng thái swept/unswept, hướng delivery. Bias mơ hồ kiểu hơi bullish là trượt [^S26].

Veto 2: verdict body-close của sweep — cấm entry trước close: wick vượt level cộng thân đóng ngược vào trong là sweep xác nhận; thân đóng vượt qua cộng nến sau đi tiếp là breakout — cấm fade; entry trong nến mồi là lỗi đắt nhất entering the inducement candle [^S3]. Hai biến thể: Type 2 (displacement sweep) — thân lấn nhẹ qua level nhưng nến sau đảo mạnh vào trong thì vẫn là sweep, SL nới NGOÀI body-close chứ không chỉ ngoài wick; Type 3 (extended sweep) — quét chuỗi nhiều pool liên tiếp thì cấm entry ở pool đầu, chờ pool CUỐI body-close cộng MSS; vì vậy phải mark hết pool có khả năng bị quét từ pre-session.

Veto 3: bộ ba MSS cộng displacement cộng FVG — sweep phải đứng TRƯỚC break; CHOCH đơn độc không sweep trước chỉ là warning, cấm vào hướng mới. Displacement thật có body-to-range ratio trên 70%; grind chậm là nhiễu [^S30]. MSS trigger ở M5/M15, confirm ở 15M/1H [^S31]. Quy tắc alignment: 3 timeframe đồng thuận = Tier 1 setup; 2 timeframe = Tier 2 (hạ size); LTF đẹp mà HTF ngược = skip — counter-trend không có institutional backing.

Veto 4: R:R tối thiểu 1:2 tới T1 — entry 50% CE FVG; cấm entry rìa FVG. Stop ngoài toàn bộ râu quét. FVG chỉ vô hiệu khi thân đóng xuyên biên đối diện; râu chạm 50–70% vẫn còn hiệu lực [^S32].

Tầng cổng bắt buộc — thiếu thì bỏ hoặc hạ cấp.

Cổng 1: đúng phía premium/discount theo EQ đã định nghĩa — trên EQ chỉ short, dưới EQ chỉ long; weekly range cho daily bias, daily range cho intraday, Asian range cho precision entry. OB/FVG bullish trong premium là trượt cổng [^S25].

Cổng 2: killzone timing — đúng các cửa sổ đã chốt ở Bước 7. FVG phải sinh SAU khi window mở (FVG lúc 9:30AM ET với entry 10:05AM không phải Silver Bullet); 11AM–1:30PM ET là dead-zone xác suất thấp; hết window chưa hồi thì cấm đuổi [^S26].

Cổng 3: FVG tươi và chất lượng — chỉ trade 1st Presented (chưa test); hồi đầu tiên sau displacement là entry lý tưởng. Size NQ 20–80 điểm, EUR/USD 8–30 pips; dưới 5 điểm NQ / 3 pips EU là nhiễu; trên 100 điểm NQ dễ front-run trước 50% CE. Entry M5/M15 [^S32]. Cây quyết định: đủ 5/5 filter cộng overlap thì limit mù 50% CE; 4/5 thì chờ giá vào FVG rồi tìm MSS M1 mới vào; từ 3/5 trở xuống thì bỏ.

Cổng 4: inducement (IDM — mồi) khác DOL: IDM luôn nhỏ hơn pool thật, nằm ngay trước POI thật; sau khi IDM bị sweep cộng MSS cộng entry, giá VẪN PHẢI còn đường tới DOL chưa quét [^S33].

Tầng nice-to-have — chỉ scale size. Quy tắc chống tự lừa: sweep cộng MSS cộng FVG cộng killzone cộng đúng phía premium/discount cộng DOL phía trước là setup A+ — SMT, Turtle Soup, PO3 trùng pha chỉ tăng size trong giới hạn risk, không biến setup thiếu cổng thành đủ.

SMT divergence (EU–GU, NQ–ES; gap từ 10–15 pips mới có nghĩa) [^S34]. Bốn quy tắc vận hành biến SMT thành công cụ phân biệt pool thật vs pool giả thay vì trang trí: (a) trade asset TẠO cực giá — EU quét high mà GU không theo thì short EU, không short GU; chỉ so cặp correlated, EU với USDJPY lệch nhau là hành vi bình thường chứ không phải tín hiệu; (b) cả hai chart phải cùng timeframe và trước đó đi cùng hướng, cực mới phải là structural swing — ví dụ corpus: gap 65 pips là divergence valid, gap 3–5 pips chỉ là spread noise; (c) sweep candle là signal, MSS là confirmation, retrace vào FVG/OB mới là entry; SL ngoài SMT wick; (d) SMT phụ thuộc bias: tín hiệu SMT short trong ngày bullish là trade xác suất thấp — scalp nhỏ hoặc bỏ, không full-size như SMT thuận bias [^S34].

Turtle Soup lookback (level giữ tối thiểu 2 sessions; wick sweep NQ 10–30 điểm / ES 5–15 điểm / forex 10–30 pips; MSS 5M trong 3–6 nến sau quét; sweep ngược daily bias) [^S28]. Caveat regime cho đúng tình huống của bạn: fade false-break là read của thị trường RANGE; trong uptrend HH/HL, breakout thường tiếp diễn, nên swing low bị quét trong ngày trend là fuel để mua chứ không phải tín hiệu đảo chiều; trigger là giá quay lại XUYÊN QUA level vừa phá, không phải bản thân cú phá; quản trị: tần suất giới hạn, stop sát ngoài extreme, partial tại midpoint range [^S35] [^S36].

PD-array overlap (FVG chồng OB/Breaker/BPR cùng giá đúng phía) [^S32]. PO3/AMD alignment (chỉ trade pha distribution; daily Asia tích lũy rồi London manipulation rồi New York phân phối; weekly Thứ 2 tích lũy rồi Thứ 3/4 manipulation rồi Thứ 4/5 phân phối; double Judas sweep 2 sâu hơn sweep 1) [^S27]. Silver Bullet sub-window (hoàn tất trong 10:00–10:30 ET mạnh nhất; target 50%/25%/25%).

Chống double-count: Turtle Soup là tên setup cấu trúc, Judas là tên pha AMD, Manipulation là tên chu kỳ macro, Silver Bullet là tên timing window — cùng một nến mang bốn nhãn vẫn là MỘT confluence (sweep-in-context), không phải bốn [^S37]; nguồn turtle-soup thứ hai nói thẳng Judas Swing và Turtle Soup mô tả cùng hành động giá từ hai góc nhìn [^S36]. **Tier 2 không bao giờ thay thế Tier 0–1.**

False-positive cần tách riêng: FVG không phải DOL. FVG là POI entry và inefficiency-draw nội bộ ngắn hạn; DOL là đích đến của leg. Chốt full tại cú lấp nội bộ trong khi delivery thật nằm ở old high phía sau là lỗi staging đắt nhất. FVG HTF (1H/4H/D) nặng ký hơn và FVG trùng đa timeframe cùng giá là entry confluence cao nhất.

Chuỗi ICT 2022 Model theo thứ tự: pre-session đặt tên DOL cộng bias, vẽ dealing range cộng EQ, mark mọi pool cộng tier, xác định pha PO3, đặt alert chờ window; sweep thì chờ close verdict body-close, phân biệt IDM-fuel với DOL-target; MSS cộng displacement thì đo size cộng độ tươi FVG; entry thì limit 50% CE (đủ filter) hoặc MSS M1 trong FVG (thiếu một filter); SL/TP thì stop ngoài râu quét, check R:R ≥ 1:2 tới T1 trước khi bấm, T1 chốt 50% cộng breakeven, cấm đuổi sau window, cấm trade ngược alignment 3 timeframe [^S29].

## 7. Lỗi sai thường gặp, checklist journal và hành động

Năm lỗi đắt nhất cần thuộc lòng. Một, dùng level đã quét làm DOL — draw cũ cho phản ứng yếu. Hai, đặt DOL quá xa reach phiên — draw kiểu 800 điểm NQ trong một session thường là multi-day target; phiên đó coi như không có draw. Ba, bỏ qua DOL khi trade trông đẹp — FVG hoàn hảo mà không draw rõ theo hướng entry là pattern-matching without context. Cả ba lấy từ cùng nguồn walkthrough [^S1]. Bốn, nhầm Judas target với DOL — lỗi hướng phổ biến nhất. Năm, đúng hướng nhưng sai zone — bullish từ premium là chống đường phân phối dù hướng đúng [^S4].

Sáu lỗi trên là lỗi thao tác. Lớp lỗi sâu hơn khiến DOL luôn-đúng sau sự việc — cơ chế tự lựa của chính phương pháp — đáng thuộc lòng không kém: (1) swing selection — cùng chart, hai trader chọn hai swing khác nhau vì không có quy tắc chung wick hay body-close, timeframe nào ưu tiên; (2) liquidity giải thích mọi kết cục — lên là seeking BSL, xuống là targeting SSL, đảo là sweep, chạy là run: mọi outcome đều fit sau sự việc, claim không falsifiable; (3) FVG dày đặc — move mạnh tạo vài gap trong vài phút, không biết gap nào đáng chú ý trước phản ứng; (4) overload thiếu hierarchy — OB nằm trong HTF FVG ngược chiều, discount range này là premium range khác; (5) narrative dịch chuyển sau fail — đổi timeframe/range/pool để reframe, OB fail thành breaker, target hụt thành inducement; (6) premium/discount phụ thuộc anchor — arithmetic khách quan, range selection thì không; cộng irreproducibility giữa hai tester trên cùng dữ liệu [^S38].

Thuốc giải duy nhất: pre-commit — viết DOL, anchor, và điều kiện vô hiệu TRƯỚC khi biết outcome. Điểm công bằng cho cả hai phía: phe hoài nghi cũng không phủ nhận nền tảng — stop clustering và sweeps là hành vi có tài liệu hóa, chỉ tính chủ đích nhắm một mức cụ thể là không chứng minh được; khoảng cách nằm giữa điều liquidity tồn tại và điều đỉnh/đáy này bị target có chủ ý [^S39]. Nếu định nghĩa của bạn chỉ hiện hình sau khi nến đóng, đó là mô tả, không phải dự báo.

Cộng thêm: setup bias sau khi killzone đã mở [^S10]; giữ bias xuyên hard invalidation (daily body close vượt biên ngược bias thì bias SAI — đóng lệnh, đọc lại từ weekly) [^S10]; entry trước close nến sweep [^S3]; sửa DOL giữa lệnh và cộng dồn confluence giả.

Mọi DOL call nên tuân thủ 10 luật khả kiểm chứng: pre-marked (mark tối đa 2 ứng viên có giá trước killzone, 1 trên 1 dưới; ứng viên không nhìn ra trong 5 giây thì đó không phải DOL hôm nay; cấm thêm mid-session trừ khi displacement mới tạo pool mới — ghi lý do); unswept-only (pool đã sweep cộng displace khỏi là spent; vi phạm luật này = auto-grade DOL call invalid DÙ trade thắng); body-close criterion (wick vượt pool cộng body đóng trở vào trong); displacement filter (leg nhanh full-bodied cộng FVG mới nâng hypothesis thành bias tradable — ghi rõ leg nào, giờ nào, timeframe nào trigger upgrade); no-draw-no-trade (không đặt tên được DOL một câu có giá thì nghỉ, no-trade rate phải lớn hơn 0).

Năm luật tiếp: killzone-only grading (chỉ grade accuracy trên setups trong killzone; move ngoài killzone ghi riêng dưới nhãn outside-KZ excursion, không tính vào bias accuracy); fixed anchor (mỗi call nêu anchor range cộng premium/discount — ví dụ D1 swing low→high 23,900→24,300 với EQ 24,100, giá đang discount nên ưu tiên BSL trên); ERL/IRL staging (internal = T1, external = T2; chấm riêng target-staging error).

Ba luật cuối thuộc về hậu kỳ: full journal fields (DOL một dòng có giá cộng loại, anchor cộng premium/discount, sweep Y/N cộng giờ, displacement Y/N, Entry/Stop/T1/T2, Result/R, bias-correct, DOL-reached, note một câu); baseline comparison — mỗi 50-trade block so expectancy DOL-filtered vs unfiltered hoặc random-entry cùng R-multiple: DOL chỉ có edge khi filtered lớn hơn với cùng risk [^S8].

Ngôn ngữ qualified cho journal. Được phép: DOL hôm nay là PWH (BSL chưa quét); bias long CHỈ hiệu lực nếu sweep SSL cộng displacement lên trong NY AM. Cấm: giá chắc chắn lên PWH, DOL đúng 80%, sweep xong luôn reverse, mọi win-rate gắn với ICT như tổng thể — win-rate phải gắn với rule-set cộng market cộng giai đoạn cụ thể [^S8]. Viết DOL mà không viết điều kiện vô hiệu là kể chuyện, không phải phân tích.

Checklist pre-trade chép vào journal:
- [ ] Ngày, session, câu DOL một dòng có giá cộng loại (resting/inefficiency) cộng tầng IRL/ERL; Judas target có giá; điều kiện vô hiệu viết sẵn [^S24]
- [ ] Anchor range cộng premium/discount (EQ = (High cộng Low)/2); weekly profile là thứ mấy; tin đỏ FOMC/CPI/NFP trong 24h? DXY ủng hộ hay chống?
- [ ] R:R tới T1 đạt tối thiểu 1:2? Entry 50% CE, stop ngoài râu sweep, T1 là nearest opposing liquidity, T2 là ERL?

Checklist execution:
- [ ] Sweep trong killzone? (có/không cộng giờ) [^S40]
- [ ] Displacement cộng MSS cộng FVG? (khung nào, body-ratio trên 70%, FVG 1st Presented, size NQ 20–80 / EU 8–30)
- [ ] Entry đúng model ICT 2022 (sweep rồi MSS rồi FVG, killzone active, đúng phía premium/discount, IDM khác DOL)?

Checklist post-trade và review:
- [ ] Kết quả R, bias đúng không, DOL tới chưa (partial/full), một câu lesson
- [ ] Backtest tối thiểu 100 lệnh (20–30 lệnh chưa đủ tách edge khỏi nhiễu; 200–300 mới thấy rõ) theo quy trình chống hindsight: scroll về quá khứ, CHE toàn bộ giá tương lai bằng rectangle/replay, gọi daily bias TRƯỚC khi reveal từng phiên, mark AMD phases khi chúng hình thành, chỉ đặt entry trong killzone như đang live, ghi mọi lệnh như live — call bias sau khi đã thấy close là nguồn win-rate giả 90%+ [^S41]. Cổng tiến cấp: backtest 100+ → forward/demo 50+ → micro live 50+ → full size; backtest không đo được slippage, áp lực cảm xúc, regime change. Review mỗi 50 lệnh: win rate, R trung bình, expectancy, bias accuracy, DOL-hit rate, killzone tốt nhất, no-trade rate; bias accuracy live 55–65% là bình thường [^S42]
- [ ] Mỗi block 50 lệnh so expectancy nhóm có DOL-filter với baseline không filter — DOL chỉ giữ lại khi filtered vượt unfiltered với cùng risk

Khung risk cho prop-firm gắn chặt với DOL. Mỗi lệnh tối đa 0,5% tài khoản; T1 chốt 50% cộng breakeven, runner chỉ nuôi khi quét Tier 1–2 (monthly/weekly extremes) — quét Tier 3–4 (PDH/PDL, Asian extremes) chỉ kỳ vọng intraday tới pool đối diện cùng session; quét Tier 5–6 chỉ scalp về mốc nội bộ gần nhất. FTMO tính daily loss reset trên số dư cố định và yêu cầu tối thiểu 4 ngày trade; The5ers reset từ equity đóng cửa hôm trước và yêu cầu tối thiểu 3 ngày lãi từ 0,5% trở lên (quy định có thể thay đổi theo thời điểm, cần kiểm tra lại trên trang chủ quỹ) — DOL-as-process phục vụ đúng việc này: giảm overtrading bằng no-draw-no-trade cộng killzone-only, chuẩn hóa risk, biến mỗi ngày thành một repetition được chấm điểm. No-trade rate phải lớn hơn 0 — journal 100 ngày mà ngày nào cũng có DOL thì bạn đang rationalize.

Action items 30 ngày tới:

- [ ] Mỗi sáng trước killzone 15 phút: viết 1 câu DOL (IRL-T1 cộng ERL-T2 cộng Judas target) vào journal; không viết được thì nghỉ, log lý do no-trade
- [ ] Gắn mọi lệnh ICT 2022 với đủ 8 cổng Tier 0–1; thiếu 1 cổng thì bỏ qua, log lý do skip
- [ ] Chạy case uptrend HH/HL mục 5 trên 20 phiên backtest NQ1 gần nhất: đếm bao nhiêu lần swing low dưới là Judas fuel cho T1 PDH so với bao nhiêu lần lật thành DOL giảm thật; ghi expectancy DOL-filter vs baseline
- [ ] Review mỗi 50 lệnh: bias accuracy, DOL-hit rate, best killzone, no-trade rate, staging error; risk cố định tối đa 0,5%/lệnh, T1 chốt 50% cộng hòa vốn

Kết luận cam kết: DOL là process-filter có điều kiện; con đường duy nhất biến nó thành edge cá nhân là 100 backtest cộng 50 forward journaled — và chính yêu cầu pre-mark, viết cơ chế bằng quy tắc nhị phân để chấm được một DOL call cũng là yêu cầu mà mọi nghiên cứu kiểm định ICT đều phải tuân. Predictive edge chưa được chứng minh — đừng trade như thể có.

Bằng chứng định lượng gần nhất với rổ lệnh của bạn: một backtest mở trên NQ 5-minute 2019→2026 (~7,5 năm), lookahead-free trên nến đã đóng, fills bảo thủ, chi phí thật ($4,50 + 2 ticks trượt giá), t-stat tính trên daily P&L, train/holdout split — Order Block t = −0,6, FVG t = +1,5, Liquidity Sweep t = −0,8, Silver Bullet t = −2,5 (thua có ý nghĩa thống kê), chỉ OTE t = +6,6 — nhưng OTE mạnh nhất ở retracement 38% (t = 7,4) rồi giảm dần theo độ sâu — 62% t = 6,5, 79% chỉ t = 2,9, 89% âm t = −4,0 — KHÔNG phải vùng Fibonacci 62–79% ICT dạy, và full confluence stack (sweep + HTF FVG + inverse FVG) chỉ ra t = 0,98 với chữ ký overfit kinh điển: in-sample +1,8 lật thành out-of-sample −0,15 [^S43]. Đây là vendor backtest tự công bố — cần verify độc lập — và họ test rules cơ khí, không phải full discretion của bạn; điều nó nói thẳng: entry tại các level-DOL-trigger không có edge độc lập, stacking thêm điều kiện chỉ thu nhỏ sample chứ không tạo edge.

Cùng hướng: repo MQL5 XAUUSD ép toàn bộ ICT thành binary conditions phát hiện vấn đề objectification — nhiều khái niệm ICT kháng định nghĩa hệ thống nếu không đơn giản hóa đáng kể, và chính họ phải bỏ phiên bản đầu vì lỗi để hàng chục lệnh chồng nhau trong 5 phút — với kết quả: baseline no-filter +11,5% nhưng maxDD −39,4%, PF 1,02, Sharpe ~0,29, ~14.500 lệnh, Z-score −22,5; sau bias-alignment còn 338 lệnh, PF 1,16 fragile, Recovery <1, Sharpe ~0,64, avg loss $106 > avg win $86, toàn bộ edge sống nhờ MỘT lệnh hold 328 giờ trong bull-run vàng Sep–Nov 2025 — cắt max-hold dưới 32 giờ thì PF <1,0 [^S44]. Đọc đúng trọng số: practitioner-backtest khác full-discretion nên chỉ đọc như bằng chứng process-chứ-không-falsify-DOL — bias filter giúp thật nhưng không đủ tự tạo systematic edge; DOL phải tự chứng minh phần còn lại trên journal của chính bạn. Process edge thì đo được — và process edge mới là thứ pass FTMO/The5ers: ít lệnh hơn, đúng giờ hơn, đúng phía premium/discount hơn, mục tiêu chia tầng rõ ràng hơn.

---

## Nguồn tham chiếu

> [!warning] Trạng thái nguồn
> Các tham chiếu trong bài từng trỏ tới note nguồn trong research vault (`research/notes/`). Thư mục đó hiện **không còn trong vault**, nên toàn bộ liên kết dạng `[[...]]` đã được chuyển thành chú thích đánh số ở dưới đây để note tự chứa và không còn liên kết chết. Phần phân tích, số liệu và kết luận trong thân bài **không bị thay đổi**. Nguồn `interim-*` là ghi chú nội bộ của pipeline, không phải nguồn ngoài — kết luận của chúng vẫn đọc được trực tiếp trong thân bài.

[^S1]: ICT Draw on Liquidity (DOL) — Picking the Target. Nguồn ICT dạng hướng dẫn; Tier 3.
[^S2]: Draw on Liquidity (DOL) in ICT — LiquidityScan. Tier 3.
[^S3]: ICT Liquidity Sweep: 4 Signs of a Real Raid. Tier 3.
[^S4]: ICT Dealing Range: IRL to ERL in 3 Steps. Tier 3.
[^S5]: Draw on Liquidity: The ICT Concept That Changes Everything. Tier 3.
[^S6]: Osler, C. L. (2005). “Stop-Loss Orders and Price Cascades in Currency Markets.” Journal of International Money and Finance, 24(2), 219–241. DOI: 10.1016/j.jimonfin.2004.12.002. https://doi.org/10.1016/j.jimonfin.2004.12.002 — Nguồn học thuật Tier 2. Kèm: Osler, C. L. (2003). “Currency Orders and Exchange Rate Dynamics: An Explanation for the Predictive Success of Technical Analysis.” Journal of Finance, 58(5), 1791–1819. https://www.newyorkfed.org/research/staff_reports/sr125.html
[^S7]: Liston, Gretton & Lensky (2024). Proceedings of ICAART 2024, vol. 1, tr. 280–288 (SciTePress). Bằng chứng MÔ PHỎNG agent-based trên limit-order-book lịch sử rằng cấu trúc stop-loss order book đủ để một agent lợi dụng time các event cascade. Tier 2 (hội nghị, không phải peer-review tạp chí).
[^S8]: Ghi chú phân tích nội bộ của pipeline nghiên cứu (interim). Nội dung vẫn đọc được trong thân bài mục 1.
[^S9]: Ghi chú phân tích nội bộ của pipeline nghiên cứu (interim, không phải nguồn ngoài). Nội dung kết luận vẫn đọc được trong thân bài mục 2.
[^S10]: ICT Daily Bias: A 5-Step Checklist for Direction. Tier 3.
[^S11]: ICT Daily Bias — How to Set the Direction of the Day (Strefa Tradingu). Tier 3.
[^S12]: ICT Daily Bias — Most Simple Mechanical Framework (TTrades). Tier 3.
[^S13]: Daily Bias Explained — Complete ICT/SMC Guide 2026 (TradingEdge). Tier 3.
[^S14]: The 4 Liquidity Levels to Mark Every Day — NY AM Session H/L, News Wick, PDH/PDL. Tier 3.
[^S15]: Ghi chú phân tích nội bộ của pipeline nghiên cứu (interim). Nội dung vẫn đọc được trong thân bài mục 3.
[^S16]: Previous Day High and Low (PDH/PDL) — GhostTraders. Tier 3.
[^S17]: Ghi chú phân tích nội bộ của pipeline nghiên cứu (interim). Nội dung vẫn đọc được trong thân bài mục 4.
[^S18]: ICT Draw on Liquidity (Stocks & Futures / Trading Magazine). Tier 3.
[^S19]: ICT Previous Day High and Low (PDH/PDL) — Full Guide. Tier 3.
[^S20]: ICT PDH/PDL/PWH/PWL Session Reference Levels (Inner Circle Traders). Tier 3.
[^S21]: Previous Day High and Low (PDH/PDL) in SMC Trading. Tier 3.
[^S22]: ICT Daily Bias 2026: 7-Step Framework + Examples (Take Profit Traders App). Tier 3.
[^S23]: ICT Market Structure: Higher Highs & Lower Lows Explained (Inner Circle Traders). Tier 3.
[^S24]: ICT Daily Bias — How to Determine It (LiquidityScan). Tier 3.
[^S25]: ICT Premium/Discount — Using the 50% Equilibrium. Tier 3.
[^S26]: ICT Silver Bullet: The 10–11 AM Window Setup. Tier 3.
[^S27]: ICT Power of Three (PO3) — Open, Manipulate, Distribute. Tier 3.
[^S28]: ICT Turtle Soup — The False Breakout Reversal Setup. Tier 3.
[^S29]: ICT 2022 Mentorship Model — The Complete Strategy: Sweep → MSS → FVG (Strefa Tradingu). Tier 3.
[^S30]: ICT Market Structure: BOS, CHoCH and MSS Explained. Tier 3.
[^S31]: ICT Liquidity Sweep Trading — How to Spot and Trade It. Tier 3.
[^S32]: ICT Fair Value Gap (FVG) — 3-Candle Rule Entry Guide. Tier 3.
[^S33]: ICT Inducement — How to Spot the Trap Before Entry. Tier 3.
[^S34]: ICT SMT Divergence — Reading NQ vs ES Disagreement. Tier 3.
[^S35]: Turtle Soup / Failed Breakout Explained — Complete ICT/SMC Guide 2026 (TradingEdge). Tier 3.
[^S36]: ICT Turtle Soup Trading Strategy Explained (Inner Circle Traders). Tier 3.
[^S37]: Ghi chú phân tích nội bộ của pipeline nghiên cứu (interim). Nội dung vẫn đọc được trong thân bài mục 6.
[^S38]: ICT Trading Problems: Subjectivity, Hindsight Bias and the Limits of the Method. Tier 3.
[^S39]: Is ICT Trading Legit? Method vs Hype (LiquidityScan). Tier 3.
[^S40]: ICT 2022 Model 2026 — Complete Step-by-Step Guide. Tier 3.
[^S41]: ICT Backtesting — How to Test the Framework (Inner Circle Traders). Tier 3.
[^S42]: ICT Backtesting — A 6-Step Process That Works. Tier 3.
[^S43]: Order Block Trading and Fair Value Gaps Tested on 7 Years of NQ (NQ 5-min 2019–2026; Order Block t = −0,6, FVG t = +1,5, Liquidity Sweep t = −0,8, Silver Bullet t = −2,5, OTE t = +6,6 tại 38%; full confluence stack t = 0,98 với chữ ký overfit in-sample +1,8 → OOS −0,15). Đây là vendor backtest tự công bố — cần verify độc lập. Tier 3.
[^S44]: TuomasLaukala/ICT-strategy-backtest — Backtesting ICT Strategy (GitHub). XAUUSD: baseline no-filter +11,5% nhưng maxDD −39,4%, PF 1,02, ~14.500 lệnh, Z-score −22,5; sau bias-alignment còn 338 lệnh, PF 1,16, Recovery < 1, toàn bộ edge sống nhờ MỘT lệnh hold 328 giờ. Tier 4 (practitioner).
