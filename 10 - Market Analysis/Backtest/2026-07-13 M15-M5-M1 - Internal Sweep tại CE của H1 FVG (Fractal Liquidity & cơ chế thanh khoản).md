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

---
*Ghi chú: date = ngày study (VN, UTC+7). Không log backtest vì không vào lệnh — đây là note phương pháp. Giá/level do người dùng cung cấp từ chart study; symbol NAS100 suy từ vùng giá ~23,600. 4 sơ đồ minh họa nguyên lý, không phải chart thật. Concept nền liên quan: [[20 - Liquidity Sweep]], [[13 - FVG  - Fair Value Gap]], [[10 - Consequent Encroachment (Mean Threshold)]], [[16 - Internal & External Range Liquidity (IRL & ERL)]], [[33 - Turtle Soup]].*
