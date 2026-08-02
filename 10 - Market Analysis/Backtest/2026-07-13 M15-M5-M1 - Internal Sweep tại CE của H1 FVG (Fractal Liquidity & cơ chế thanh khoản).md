---
type: market-analysis
status: methodology
date: 2026-07-13
symbol: NAS100 (chart study, vùng giá ~23,600–23,670)
timeframe: H1 (POI) / M15 → M5 → M1 (trigger)
session: chart study
htf_bias: bullish (retrace về H1 FVG discount)
setup: 2022 Model - long từ discount POI (H1 FVG / CE)
in_trade: false
draw_on_liquidity: "target: BSL phía trên (~23,670) | trigger: SSL nội bộ trong POI"
key_poi: H1 FVG (discount), điểm phản ứng tại CE (Mean Threshold)
invalidation: đóng nến dứt khoát dưới FVG low mà không reclaim (breakdown, không phải sweep)
topic: nhận diện liquidity sweep trên LTF, FVG≠Liquidity, fractal liquidity, cơ chế tích tụ thanh khoản & conviction hierarchy
tags:
  - analysis
  - methodology
  - ict-2022
  - liquidity-sweep
  - fair-value-gap
  - consequent-encroachment
  - fractal-liquidity
  - timeframe-alignment
  - internal-liquidity
---

# M15-M5-M1 — Internal Sweep tại CE của H1 FVG: Fractal Liquidity & cơ chế thanh khoản — 2026-07-13

> [!info] Trạng thái
> **METHODOLOGY / STUDY — không vào lệnh.** Tổng hợp một buổi phân tích chuỗi câu hỏi đào sâu về cách nhận diện **[[20 - Liquidity Sweep|liquidity sweep]]** trên khung entry, sự khác nhau giữa **[[13 - FVG  - Fair Value Gap|FVG]]** (POI) và **[[19 - Liquidity|Liquidity]]**, và cơ chế vi cấu trúc của thanh khoản. Bối cảnh: NAS100, [[27 - Premium Discount|discount]], Bias **Bullish**, POI là một **H1 FVG**, tìm trigger trên [[32 - Top-down Analysis (Multiple Timeframes)|M15 → M5 → M1]]. Sơ đồ trong note là minh họa nguyên lý, không phải chart thật.

> [!warning] Screenshot gốc
> Các chart M15/M5/M1 gốc chưa lưu dạng file. Kéo ảnh vào `10 - Market Analysis/Attachments/` (nhãn `NAS100-YYYYMMDD-TF`) rồi thêm `![[tên-ảnh.png]]` để embed.

---

## 1. Nhận diện Liquidity Sweep trên khung entry — bản chất & chuỗi 2022

Sai lầm gốc của đa số trader: đồng nhất **sweep** với **một cú phá vỡ (break) đáy**. Bản chất khác hẳn.

> [!summary] Sweep là gì
> **Sweep = thị trường chủ động chạy tới nơi có stop-loss đang nằm chờ, khớp chúng, rồi TỪ CHỐI và quay đầu.** Nó là hành động *lấy thanh khoản để đảo chiều*, không phải *tiếp diễn xu hướng*. Vì Bias Bullish + đang ở discount POI → thứ cần săn là **[[30 - Sell-side Liquidity|Sellside Liquidity Sweep]] (SSL sweep)**: quét xuống dưới một cái **đáy**, rồi bật lên.

Phân biệt với break thật (đây là ranh giới sống-còn):

- **Sweep (đảo chiều):** xuyên qua đáy → *không giữ được* dưới đó → **đóng nến quay lại lên trên** → theo sau là displacement. Thường để lại **wick dài**.
- **Break thật (tiếp diễn giảm):** đóng nến *dưới* đáy và **ở lại đó**, đi tiếp, không reclaim → POI **fail**.

Sự khác biệt nằm ở **phản ứng NGAY SAU khi chạm mức**, không nằm ở bản thân cú xuyên.

**Checklist một SSL sweep hợp lệ:**

1. Có một pool thanh khoản nhận diện được **trước**: đáy swing, cụm **equal lows (EQL)**, đáy phiên, PDL. *Không chỉ ra được "nó quét cái gì" → không phải sweep.*
2. Giá **thực sự lấy** mức đó (wick/body vượt qua, dù vài tick).
3. **Reject nhanh + reclaim**: đóng nến quay lại trên mức vừa lấy.
4. Xảy ra **đúng trong/ở mép POI** (confluence với discount).
5. **Xác nhận cuối:** theo sau là **displacement + [[21 - Market Structure Shift|MSS]]**.

> [!warning] Sweep chỉ là mắt xích 1 — MSS mới là trọng tài
> Không thể khẳng định 100% một cú quét là "sweep đảo chiều" ngay lúc nó vừa quét (nếu đóng dưới và đi tiếp → thành break). Sweep chỉ *được xác nhận* khi tạo **displacement + MSS**. Trước MSS = **đang dự đoán**; sau MSS = **đã xác nhận**. Kỷ luật prop-firm bắt buộc giao dịch cái thứ hai.

Chuỗi chuẩn: **Sweep SSL → Displacement → MSS → FVG hình thành trên chân displacement → Entry khi retrace về M5 FVG.**

![[M5-sweep-anatomy-20260713.svg]]

---

## 2. FVG KHÔNG phải Liquidity — POI vs Liquidity

Đây là điểm nhầm lẫn cốt lõi nhất. FVG và Liquidity là hai khái niệm khác nhau, trả lời hai câu hỏi khác nhau:

- **POI / PD Array (FVG)** = trả lời **"Ở ĐÂU?"** — vùng *mất cân bằng (imbalance)* nơi giá được kỳ vọng phản ứng, nơi canh vào lệnh. **Không phải** stop-loss.
- **Liquidity ([[30 - Sell-side Liquidity|SSL]] / [[07 - Buy-side Liquidity|BSL]])** = trả lời **"Nhiên liệu ở đâu?"** — các stop *đang nằm chờ* tại **đỉnh/đáy**. Liquidity **luôn ở đỉnh/đáy**, không nằm "trong một cái gap".

> [!info] Khi nào FVG & Liquidity "trùng vùng"?
> Khi có một **đáy swing / cụm EQL** tình cờ nằm *bên trong* hoặc *ngay dưới* phạm vi H1 FVG. Lúc đó stop dưới cái đáy đó (SSL) chồng lên vùng FVG → cú quét cái đáy đó *vô tình* diễn ra trong FVG. Đó là confluence, **không phải** vì FVG "chứa sẵn" liquidity. Thậm chí, chính cục liquidity dưới FVG mới là lý do giá bị kéo xuống lấp FVG ([[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw on liquidity]]): liquidity là *nam châm*, FVG là *điểm phản ứng*.

**Trả lời "giá xuyên xuống FVG rồi bật lại có phải sweep không?" → KHÔNG, tự thân nó không phải.**

- Vào thân FVG rồi bật mà **không lấy đáy nào** = **FVG rebalance / CE tap** — một mô hình entry hợp lệ *khác* ([[26 - OTE - Optimal Trade Entry|OTE]]/FVG thuần), **không phải** "sweep", **không phải** 2022 model.
- Vào FVG **và trong lúc đó xuyên thủng một cái đáy** (lấy SSL) rồi reject = **SSL sweep** trong POI → đây mới là thứ 2022 model yêu cầu.

![[FVG-vs-SSL-sweep-20260713.svg]]

---

## 3. Đọc chart thực chiến — 3 lỗi định vị hay gặp

Qua các chart thực tế đã soi, rút ra 3 lỗi định vị:

**(a) Tìm sweep sai vị trí/chiều.** Setup long-from-discount → cú SSL sweep phải nằm ở **nửa dưới / đáy POI** (nhịp đổ vào discount), **không** ở mép trên POI lúc giá đang tăng. Giá **cắt LÊN qua một đường ngang ≠ sellside sweep** — sweep phải thể hiện bằng **wick chọc XUỐNG dưới một đáy** rồi bật lên.

**(b) Nhầm "đang quét" với "đã quét".** Giá về đúng mức đáy cũ mới chỉ là **[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw on liquidity]]** (bị hút về). Để xác nhận **đã quét**: phải **wick xuống DƯỚI** điểm thấp nhất + **đóng nến quay lại LÊN TRÊN**. Chỉ chạm rồi nảy = thanh khoản dưới đó *còn nguyên*.

**(c) Sweep nông ở mép trên POI.** Cú lấy đáy ở mép trên POI thường **chưa phải đáy thật**. Giá hay tag nhẹ, nảy giả để hút thêm lệnh, rồi mới cắm sâu xuống **giữa/đáy POI** (nơi có CE + pool lớn hơn) để quét cú cuối. Luôn giữ **2 kịch bản song song**: (A) sweep nông → reclaim → MSS → long; (B) xuyên qua → cắm sâu hơn → sweep + MSS ở dưới.

> [!warning] Bẫy hindsight bias
> Đừng gọi *bất kỳ cụm nến giật hai chiều nào* là "sweep". Sweep phải lấy một cái **đáy có tên**. Không chỉ tay được vào cái đáy bị quét → mặc định **không phải sweep**. Đây chính là bias phải loại khỏi backtest 2022.

---

## 4. Nghịch lý "sweep không có SSL" tại CE — Fractal Liquidity

Tình huống tinh tế: giá retrace về gần **[[10 - Consequent Encroachment (Mean Threshold)|CE]]** của FVG, hình thành cụm nến *giống sweep* (chọc xuống, râu dài, đóng lên, displacement) — **nhưng bên trái không thấy SSL nào** trên khung đang xem. Vì sao vẫn hành xử như sweep? Hai lý do, cả hai đều hợp lệ.

**Lý do 1 — Liquidity có tính FRACTAL (phân mảnh).** "Không có SSL trên M15" ≠ "không có liquidity". Cái **râu dài trên M15**, khi zoom xuống **M1/M5**, gần như luôn chứa một cấu trúc nhỏ với **equal lows / internal swing low** — và cái wick đó đã quét đám stop dưới các đáy nội bộ đó rồi reclaim. **Một cú sweep trên M1 nhìn từ M15 chỉ còn là một cái râu nến.**

![[fractal-liquidity-20260713.svg]]

**Lý do 2 — Đây có thể là FVG/CE reaction, không cần sweep.** Có hai cơ chế cùng tạo ra "râu dài + reclaim + displacement":

- **Sweep model:** lấy stop dưới một cái đáy rồi đảo. *Cần* liquidity bị lấy.
- **FVG rebalance model (phản ứng tại CE):** thuật toán kéo giá về **CE** để tái cân bằng inefficiency, chạm rồi reject. **Không bắt buộc** có đáy cũ bên trái — CE của FVG là delivery point, râu dài chỉ là **rejection wick**.

> [!info] Khép vòng qua các khung
> - **M15:** giá phản ứng tại **CE**, *không* lấy FVG low → tưởng "không có SSL".
> - **M1/M5:** đúng tại mức CE đó tồn tại **internal SSL** (đáy nội bộ / EQL). Giá quét nó + reclaim + displacement + MSS → **trigger hợp lệ ngay tại CE**.
>
> Tức là: **HTF cho POI (CE của FVG), LTF cho trigger (sweep nội bộ + MSS)** — đúng cách các khung phối hợp trong [[01 - ICT 2022 Model|2022 Model]]. Xem thêm [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)|Confirmation Timeframe & Layering]].

> [!warning] Rủi ro còn sót
> Nếu phản ứng ở **CE** mà **chưa lấy FVG low**, thì stop dưới FVG low **vẫn còn nguyên** — một nam châm phía dưới. Cú reject tại CE có **conviction thấp hơn** cú "quét đáy rõ ràng rồi reclaim". Quản trị: ý thức FVG low bên dưới là rủi ro, cân nhắc dời SL/chốt một phần.

---

## 5. Cơ chế tích tụ thanh khoản & Conviction Hierarchy

Câu hỏi sâu: *một đáy nội bộ M1 vừa hình thành vài phút, làm sao thanh khoản kịp tích tụ? Nếu ít, quét nó có ý nghĩa gì?*

**Thanh khoản KHÔNG tích tụ dần theo thời gian.** Nó được **đặt vào tức thì, phản xạ**, ngay khi cái đáy thành một mốc nhìn thấy được — một **điểm quy chiếu chung (Schelling point)**:

- Người vừa **long** đặt **SL ngay dưới đáy** (SL = lệnh *bán* thị trường sẽ kích hoạt).
- Người theo **breakout giảm** đặt **sell-stop dưới đáy**.
- Người đang short có thể gia tăng dưới đó.

Cả ba đều là **lệnh BÁN** nằm chờ → **SSL**. Trong phiên sôi động ([[18 - Kill Zones|kill zone]]), order flow M1 chạy nhanh → cụm stop hình thành trong vài giây–vài phút. Đáy càng **rõ ràng / hiển nhiên** (EQL, reject mạnh) → càng nhiều mắt thấy → stop càng dày. Liên hệ: [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)|Liquidity Reflexivity]], [[15 - Inducement|Inducement]].

![[liquidity-buildup-hierarchy-20260713.svg]]

> [!warning] Đừng thần thánh hóa cú quét nội bộ M1
> Đáy M1 vài phút tuổi có pool **nhỏ, conviction thấp**. Nó **không phải** lý do thị trường đảo chiều. Ba vai trò thật của nó:
> 1. **Timing trigger** — thời điểm vào lệnh chính xác trong vùng đã chọn bằng HTF.
> 2. **Invalidation rõ ràng** — SL dưới wick sweep, R lớn.
> 3. **Bằng chứng hấp thụ** — reclaim + displacement chứng minh lượng bán vừa bị nuốt.
>
> **Lý do đảo chiều nằm ở HTF** (POI + discount + HTF draw). Sweep M1 là **cò súng (timing)**, không phải **viên đạn (nguyên nhân)**.

**Reframe — thanh khoản có tính tỉ lệ:** thị trường chỉ cần *đủ* liquidity cho quy mô đang giao dịch tại thời điểm đó. Trên M1, dòng tiền nhỏ hơn → pool nhỏ đã tương xứng. Mỗi khung có liquidity tương ứng cho lớp người chơi tương ứng.

---

## 6. Quy tắc rút ra (chốt cho backtest & checklist)

> [!summary] Nguyên tắc
> 1. **FVG = "Ở ĐÂU phản ứng". Liquidity = "stop dưới cái ĐÁY".** Không chờ "quét vào FVG" — chờ "quét một cái ĐÁY nằm trong FVG".
> 2. **Chạm FVG rồi bật ≠ sweep.** Chỉ khi lấy được một cái đáy mới là SSL sweep.
> 3. **Sweep là bước 1; [[21 - Market Structure Shift|MSS]] là trọng tài.** Không MSS = đang đoán.
> 4. **Sweep phải cùng khung với MSS/FVG** (khung entry). Xem [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)|Liquidity Scale Alignment]].
> 5. **Liquidity là fractal:** không thấy SSL ở HTF → zoom xuống LTF.
> 6. **Phân loại rạch ròi trong journal:** cú này là *SSL sweep* (có đáy/EQL bị lấy) hay *CE reaction* (chỉ phản ứng FVG)? Hai loại có win-rate khác nhau — để dữ liệu của chính mình phân xử.
> 7. **Trọng số theo thứ bậc:** HTF pool (session/PDL/EQL lớn) >> internal M1 low. **Internal sweep chỉ có giá trị TRONG bối cảnh HTF** — tách khỏi HTF là nhiễu.
> 8. **Sweep nông ở mép POI** dễ bị run sâu hơn → giữ 2 kịch bản song song.

---

## 7. Câu hỏi cần chốt (khi log một cú cụ thể)

- Đáy nội bộ có **thực sự undercut** đáy trước rồi reclaim không? (undercut = sweep thật; equal y hệt = double bottom, conviction thấp hơn).
- Đã có **MSS** chưa? Xác định chính xác đỉnh short-term bị phá.
- Cú vào FVG là **SSL sweep** hay **CE reaction thuần**? (phân loại cho thống kê).
- FVG low đã bị test chưa? (nếu chưa → liquidity còn sót phía dưới).
- Có nằm trong **HTF context** (POI + discount + HTF draw) không? Nếu không → bỏ.

## 8. Tình huống thực chiến (War Stories) — cascading sweep & cái giá của việc vào sớm một tầng

> [!info] Vì sao có mục này
> Mục 1–6 đã lập luận chặt: liquidity là fractal, một cú sweep nội bộ M1 vẫn có thể là trigger hợp lệ **nếu** nằm đúng trong bối cảnh HTF (CE/FVG). Nhưng thực chiến — nhất là trên NAS100, symbol có biên độ nội phiên lớn — thường không chỉ có MỘT tầng sweep nội bộ, mà là một **chuỗi nhiều tầng bị quét lần lượt** trước khi cú đảo chiều thật xảy ra. Hai tình huống dưới đây xử lý đúng cái bẫy tinh vi nhất của Conviction Hierarchy: biết nó tồn tại trên lý thuyết là một chuyện, nhận ra mình đang đứng ở tầng nào giữa lúc thị trường di chuyển là chuyện khác hẳn.

![[ConvictionHierarchy-CascadingSweeps-20260713.svg]]

### W1 — Vào lệnh ở tầng 1, bị cuốn qua tầng 2 và 3: bài học "sweep nội bộ đầu tiên không phải là sweep cuối cùng"

**Tình huống rất hay gặp:** giá quét một cụm equal-lows M1, reclaim, có cả một cây nến displacement trông rất thuyết phục — trader vào lệnh ngay vì "đúng công thức sweep + displacement". Nhưng đây chỉ là **tầng 1** trong một chuỗi cascading sweep: vài phút sau, một tầng M5 sâu hơn bị quét tiếp, cuốn theo cả lệnh vừa vào. Nến displacement ở tầng 1 là thật — nhưng nó không đủ "nhiên liệu" để tạo một cú đảo chiều có ý nghĩa, vì tầng 1 chỉ là stop của một nhóm nhỏ vừa hình thành.

**Cách phân biệt (rút từ mục 5 của note):** hỏi ba câu trước khi tin một cú sweep nội bộ là **tầng cuối**: (1) Tầng này có trùng với một POI HTF thật (CE của FVG, OB, hay chỉ là một đáy M1 trơ trọi)? (2) Đã có bao nhiêu tầng bị quét liên tiếp trong vài phút gần nhất — nếu ≥2 tầng vừa bị xuyên mà chưa có phản ứng nào giữ được, tầng hiện tại nhiều khả năng cũng sẽ bị xuyên tiếp. (3) Displacement sau sweep có đủ mạnh để tạo MSS ở khung **cao hơn** M1 (tối thiểu M5) hay chỉ là nhiễu cục bộ?

**Rule đo được:** field `sweep_tier_confirmed_by_htf_poi` (có/không) trước khi vào; nếu không, hạ xuống `watch_only` và chờ tầng kế tiếp. Field `consecutive_internal_sweeps_before_entry` — ghi số tầng đã bị quét liên tục trước tầng mình định vào; con số càng cao, xác suất đây vẫn chưa phải tầng cuối càng lớn (theo đúng nguyên tắc trong sơ đồ trên).

### W2 — Ra quyết định dưới áp lực NY Open: FVG rebalance hay SSL sweep, không đủ thời gian phân tích

**Tình huống:** vào các phiên biến động cực nhanh (NY Open, sau tin lớn), giá có thể chạm CE của FVG và bật lại trong **vài giây** — không đủ thời gian để zoom xuống M1 kiểm tra kỹ có SSL nội bộ hay không như quy trình lý tưởng ở mục 4. Nếu chờ phân tích xong, giá đã chạy mất; nếu vào ngay theo phản xạ, dễ nhầm một cú FVG rebalance thuần (không có sweep) thành một SSL sweep có conviction cao hơn thực tế.

**Cách xử lý thực dụng:** chuẩn bị **trước khi phiên mở** — không phân tích trong lúc giá đang chạy. Trước NY Open, xác định sẵn: vùng CE của FVG là gì, có internal EQL nào nhìn thấy được trên M5 (không cần M1) nằm ngay trong/dưới vùng đó không, và mức stop dự kiến cho cả hai kịch bản (sweep vs rebalance thuần). Khi giá thật sự chạm vùng, việc cần làm chỉ là nhận diện xem kịch bản nào đang diễn ra theo kế hoạch đã vẽ sẵn, không phải phân tích từ đầu.

**Rule đo được:** trước mỗi phiên kill zone có kế hoạch trade, chuẩn bị sẵn `pre_session_poi_map` (CE, FVG range, internal EQL nếu có, hai mức stop dự kiến). Sau phiên, chấm `decision_made_from_preplan` (có/không) — nếu quyết định thực tế không dựa trên bản đồ chuẩn bị sẵn mà là phản xạ tức thời, đó là tín hiệu cần rút ngắn khung thời gian chuẩn bị hoặc luyện thêm phản xạ nhận diện nhanh trước khi trade sống.

> [!success] Tổng kết mục 8
> Hai tình huống đều xoay quanh cùng một sự thật: **Conviction Hierarchy không phải một bảng tra cứu tĩnh — nó phải được áp dụng real-time, dưới áp lực thời gian, và với một chuỗi sweep có thể chưa kết thúc.** W1 dạy cách nhận ra mình đang ở tầng nào giữa một chuỗi cascading; W2 dạy cách chuẩn bị trước để không phải phân tích khi giá đã chạy. Cả hai đều quy về kỷ luật gốc của [[01 - ICT 2022 Model|2022 Model]]: chuẩn bị kỹ trước, chỉ xác nhận lúc live — không phân tích từ số 0 giữa lúc thị trường đang di chuyển.

---
*Ghi chú: date = ngày study (VN, UTC+7). Không log backtest vì không vào lệnh — đây là note phương pháp. Giá/level do người dùng cung cấp từ chart study; symbol NAS100 suy từ vùng giá ~23,600. 5 sơ đồ minh họa nguyên lý, không phải chart thật. Các tình huống ở mục 8 là kinh nghiệm tổng hợp mang tính minh họa (composite), không phải nhật ký của một lệnh cụ thể. Concept nền liên quan: [[20 - Liquidity Sweep]], [[13 - FVG  - Fair Value Gap]], [[10 - Consequent Encroachment (Mean Threshold)]], [[16 - Internal & External Range Liquidity (IRL & ERL)]], [[33 - Turtle Soup]].*
