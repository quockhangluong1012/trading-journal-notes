---
type: backtest
backtest_date: 2026-07-16
trade_date: 2014-06-25
symbol: GBPUSD
position: Long
result: Win
session: London Open KZ
setup: ICT 2022 Model
entry_model: ICT 2022 Model (CISD + BPR Entry)
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[25 - OB - Order Block|Order Block (H1)]]"
liquidity_swept: Yes
displacement: Yes
mss: "Yes (dạng CISD, không phải MSS cổ điển — xem mục 2)"
fvg_valid: Yes
entry_price: 1.69656
stop_loss: 1.69380
take_profit: "TP1 1.70311 (EQH internal) / TP2 1.70634 (H1 DR High external)"
r_planned: 2.47
r_multiple:
entry_type: CE
rr_if_ce: 2.47
grade: B+
followed_plan: "Partial — entry/stop/TP1 đúng plan, quản lý runner lệch khỏi TP2 gốc"
tags:
  - backtest
  - ICT2022
  - CISD
  - BPR
---

# Backtest 2014-06-25 — GBPUSD Long

> [!info] Mục đích backtest
> Replay một setup ICT 2022 Model dùng **CISD (full-leg reclaim)** làm confirmation thay cho MSS phá swing cổ điển, và **BPR (chồng 2 FVG đối nghịch)** làm điểm entry refine thay vì vào thẳng tại Order Block. Ghi lại đầy đủ để so sánh biến thể này với các mẫu MSS-cổ-điển khác trong dashboard sau ~20-30 mẫu.

> [!warning] Dữ liệu cần bạn xác nhận lại trước khi tính là "chốt"
> - **M5 vs M15**: chart gốc ghi tay "M5" nhưng phần diễn giải bằng lời lúc phân tích lại gọi là "khung M15". Tôi đã tạm log `entry_timeframe: M5` theo đúng label trên chart — **hãy sửa lại nếu thực tế là M15**, vì điều này ảnh hưởng cách so sánh mẫu này với các mẫu LTF khác trong dashboard.
> - **Stop loss chính xác**: số `1.69380` là tôi *suy ra ngược* từ risk/reward hiển thị trên platform (risk 0.00276 = 27.6 pip), không phải số bạn cung cấp trực tiếp. Vui lòng đối chiếu với lệnh thật trên platform và sửa nếu lệch.
> - **r_multiple (kết quả cuối)**: để trống vì runner đóng ở một mức giá bạn chưa cung cấp con số cụ thể. Bổ sung giá đóng thực tế của phần runner để tôi/bạn tính r_multiple tổng chính xác.

---

## 0. Backtest Summary

| Field                 | Value                                                              |
| --------------------- | ------------------------------------------------------------------ |
| Symbol                | GBPUSD                                                             |
| Trade Date (dữ liệu)  | 2014-06-25                                                         |
| Position              | Long                                                                |
| Result                | Win (TP1 full, runner đóng sớm — vẫn dương)                        |
| Session               | London Open KZ                                                     |
| Setup                 | ICT 2022 Model                                                     |
| Entry Model           | CISD (full-leg reclaim) + BPR Entry                                 |
| Entry Timeframe       | M5 *(cần xác nhận — xem cảnh báo trên)*                            |
| HTF Bias              | Bullish                                                            |
| Bias Correct?         | Yes                                                                |
| Entry                 | 1.69656 (CE của BPR)                                               |
| Stop Loss             | ~1.69380 *(suy ra từ RR — cần xác nhận)*                            |
| Take Profit           | TP1 1.70311 (EQH, internal) → TP2 1.70634 (H1 DR High, external)   |
| R Planned (TP1)       | 2.47                                                               |
| R Multiple (kết quả)  | *(chưa điền — cần giá đóng thực tế của runner)*                    |
| Entry Type            | CE                                                                  |
| RR nếu vào CE         | 2.47 (đã vào đúng CE, nên bằng R Planned)                          |
| Grade                 | B+ *(đề xuất — xem lý do ở mục 5)*                                 |

> ⚠️ Nhớ điền `r_multiple` vào frontmatter khi có số cuối, để dashboard tổng hợp đúng.

---

## 1. HTF Context & Bias

### D1 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending — giá đang trong nhịp tăng mạnh với cấu trúc **HH/HL** rõ ràng.
- **Lý do xác định bias**: cấu trúc D1 tạo higher-high/higher-low liên tục trước thời điểm setup; không có tín hiệu đảo chiều D1 nào được ghi nhận tại thời điểm phân tích.
- **Draw on Liquidity**:
  - Buy-side liquidity (mục tiêu hướng tới): EQH nội bộ tại 1.70311, xa hơn là H1 Dealing Range High 1.70634.
  - Sell-side liquidity: không phải mục tiêu của lệnh Long này — chỉ liên quan nếu bias bị vô hiệu.

![[Pasted image 20260716173453.png]]
### H1 — Cấu trúc & POI

- **Dealing Range H1**: High **1.70634** / Low **1.69167** → Equilibrium = **1.699005**.
- **H1 POI**: Order Block **1.69562 (high) – 1.69395 (low)**, CE của OB = **1.694785**.
- **Premium/Discount check**: OB (1.69395–1.69562) nằm **hoàn toàn dưới** Equilibrium (1.699005) → đúng phía discount cho một setup Long. Đây là điều kiện *bắt buộc* trước khi coi OB này là POI hợp lệ, và nó thỏa.
- **Phản ứng tại POI**: giá quét bằng bóng nến vào OB nhưng **thân nến đóng lại bên ngoài** OB — dấu hiệu phía bán không đủ lực giữ giá bên trong OB, một trong những kiểu phản ứng "sạch" nhất khi đánh giá độ tin cậy OB.
- **Ghi chú về độ sâu tap**: quan sát trên chart, bóng nến chỉ chọc vào **phần trên** của OB (khoảng 1.6951–1.6953), **không** chạm tới CE của OB (1.694785) hay low của OB (1.69395). Đây là một cú tap **nông** — không sai về nguyên tắc, nhưng là biến số nên theo dõi riêng trong dashboard (tap nông vs tap sâu) để backtest trả lời câu hỏi biến thể nào cho win rate/expectancy tốt hơn, thay vì coi mọi cú tap OB là tương đương.

![[Pasted image 20260716173421.png]]
---

## 2. M5 — Xác nhận & Điểm vào lệnh

### Chuỗi diễn biến

1. **Liquidity sweep vào OB**: bóng nến quét vào phần trên của OB, thân đóng ngoài (như mục 1).
2. **Displacement + FVG (Bullish)**: sau khi bật khỏi OB, giá tạo một nhịp displacement mạnh, để lại một **FVG Bullish** — xác nhận động lượng đảo chiều đủ mạnh để tin vào OB.
3. **CISD (Change in State of Delivery) — full leg reclaim**: giá đóng nến vượt qua **open của toàn bộ cụm nến giảm** trong nhịp retrace về OB (không chỉ 1-2 nến gần nhất). Đây là bản CISD "đầy đủ", mạnh hơn nhiều so với CISD chỉ quét qua nến giảm cuối cùng.
   - **Ghi chú khái niệm quan trọng** (đã thảo luận kỹ trước khi log note này): CISD dùng **open/close (body)** của nến làm mốc, khác hoàn toàn với MSS cổ điển — MSS cổ điển dùng **wick** để định nghĩa swing point, và cần một cây nến **đóng cửa** (không chỉ wick) qua đúng cái wick đó để xác nhận phá vỡ. CISD ở đây là công cụ hợp lệ và đúng chỗ để dùng — nó trả lời câu hỏi "trạng thái giao hàng đã đổi chưa" ở cấp độ vi mô, không thay thế cho một MSS cấu trúc lớn. Trường `mss` trong frontmatter được log là **"Yes (dạng CISD)"** để phản ánh đúng bản chất, tránh lẫn với MSS phá swing-high thật.
4. **BPR hình thành**: nhịp retrace ban đầu (đi vào OB) tạo ra một **FVG Bearish**; nhịp displacement bật ra sau đó tạo một **FVG Bullish**. Hai FVG đối nghịch này chồng lên nhau tạo thành **BPR: 1.69662 (high) – 1.69649 (low)**.
5. **Entry tại CE của BPR**: CE = (1.69662 + 1.69649)/2 = **1.696555 ≈ 1.69656**. Lệnh được xác nhận đặt đúng tại CE (không lệch sang mép BPR như nghi vấn ban đầu).
6. **Stop Loss**: dưới low của OB (1.69395) + buffer nhỏ, ước tính rơi vào khoảng **1.69380** (buffer ~1.5 pip) dựa trên RR hiển thị trên platform — *cần bạn xác nhận số chính xác*.
7. **Take Profit 2 tầng**:
   - **TP1 = 1.70311** — Equal Highs (EQH), internal liquidity. Đáng chú ý: mức này nằm **trên** Equilibrium (1.699005), tức đã ở trong vùng premium của range H1 — hợp lý, vì internal liquidity thường nằm ở nơi các vị thế cũ có khả năng chốt lời/đối ứng, và premium là khu vực điển hình cho việc đó.
   - **TP2 = 1.70634** — H1 Dealing Range High, external liquidity, mục tiêu cuối theo đúng hệ thống phân cấp thanh khoản (internal trước, external sau).
![[Screenshot 2026-07-16 150746 1.png]]
### Entry trigger
- Liquidity Sweep vào H1 OB (wick, thân đóng ngoài)
- Displacement + FVG Bullish trên khung xác nhận (M5/M15)
- CISD full-leg reclaim
- BPR (2 FVG đối nghịch chồng nhau) → entry tại CE

### Entry reason
- Toàn bộ chain: HTF bias Bullish → discount POI (H1 OB) → phản ứng bóng nến sạch → displacement/FVG xác nhận → CISD xác nhận trạng thái giao hàng đã đổi → BPR cho một điểm entry risk thấp hơn OB gốc trong khi vẫn giữ đúng toàn bộ luận điểm HTF.

### Invalidation reason
- Giá đóng nến qua low của H1 Order Block (dưới ~1.69395) → luận điểm Long bị vô hiệu.

### Tôi có chờ đủ điều kiện không?
Có — không đua giá tại displacement, chờ đúng retrace về CE của BPR mới vào.

## Kết quả:
![[Screenshot 2026-07-16 153007.png]]

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1 — Bullish D1, OB H1 nằm đúng phía discount.
- [x] Giá nằm trong Kill Zone (London Open).
- [x] Có Liquidity Sweep trước entry — bóng nến quét vào OB, thân đóng ngoài.
- [x] Có Displacement rõ ràng — nhịp bật khỏi OB tạo FVG Bullish sạch.
- [x] Có MSS hợp lệ *(dạng CISD full-leg reclaim, không phải phá swing-high theo wick — xem mục 2 để hiểu vì sao vẫn hợp lệ)*.
- [x] FVG / OB nằm trong Discount (buy) — OB dưới Equilibrium 1.699005.
- [x] Entry trong POI hợp lệ, không đua giá — vào đúng CE của BPR, chờ retrace.
- [x] SL ở vùng invalidation hợp lý — dưới low OB, nhưng **khá xa** so với entry (điểm cần cải thiện, xem mục 5).
- [x] RR tối thiểu đạt ≥ 1:2 — RR đến TP1 = 2.47.
- [ ] Cú tap vào OB là tap **sâu** (chạm CE/low OB) — **Không**, chỉ tap nông vào phần trên OB. Không phải điều kiện bắt buộc của mô hình, nhưng đáng ghi nhận làm biến số theo dõi.

---

## 4. Phân tích sau lệnh (Replay)

**Result**: TP1 hit đầy đủ (2.47R). Runner: **đóng tay** khi giá quét một internal liquidity high khác (nằm giữa TP1/EQH 1.70311 và TP2/DR High 1.70634) rồi đảo chiều — **không chạm TP2 theo plan gốc**. Replay tiếp sau đó cho thấy giá thực tế **có vượt qua TP2** (1.70634) vào ngày **2014-06-30**, tức **5 ngày sau** khi phần runner đã bị đóng.

### Tại sao lệnh thắng (root cause thật, không chỉ vì "TP1 chạy trúng")

Đi đúng chain lý luận: HTF bias Bullish + OB nằm discount + phản ứng bóng nến sạch tại POI + displacement/FVG xác nhận + CISD full-leg reclaim + entry đúng CE của BPR (risk thấp hơn nhiều so với vào tại OB gốc) + TP1 đặt đúng tại internal liquidity trước khi nhắm external liquidity. Mỗi lớp trong chain này đều có lý do rõ ràng, không có mắt xích nào là "hy vọng" hay curve-fit sau khi biết kết quả — đây là một trong những phần mạnh nhất của lệnh này, và là lý do phần entry/TP1 xứng đáng được ghi công đầy đủ.

### Vấn đề thật sự cần mổ xẻ: quyết định đóng runner sớm

Đây là phần quan trọng nhất của bài học lần này, và cần được nhìn thẳng, không né tránh (đúng vai trò mentor — không tô hồng chỉ vì lệnh vẫn có lãi):

Plan gốc bạn viết rõ: **TP2 = H1 Dealing Range High (1.70634)**, đây là external liquidity, mục tiêu cuối cho phần runner sau khi đã chốt một phần tại TP1. Nhưng thực tế, runner bị đóng tại một mức giá **khác** — một internal liquidity high nằm giữa TP1 và TP2 — ngay khi giá phản ứng/đảo chiều tại đó. Điều này là một **sự lệch khỏi plan đã viết**, dù kết quả cuối cùng vẫn dương.

Theo đúng nguyên tắc "process over outcome" của vault: **một lệnh được đánh giá bằng việc có theo đúng plan đã kiểm định hay không, không phải bằng việc nó có thắng hay không.** Việc giá sau đó (5 ngày sau) thực sự vượt qua TP2 — dữ liệu hindsight này **không** biện minh cho quyết định đóng sớm, và cũng không có nghĩa là quyết định đóng sớm là sai. Nó chỉ cho thấy: nếu bạn có một **rule quản lý runner được định nghĩa rõ từ trước** (ví dụ "chỉ đóng runner khi chạm đúng TP2, hoặc khi có một tín hiệu cấu trúc cụ thể X xảy ra"), bạn sẽ biết chắc lần này có tuân thủ hay không. Vì hiện tại không có rule đó bằng lời, câu hỏi "đây là một quyết định quản lý rủi ro hợp lý, hay là phản xạ chốt lời do sợ mất lợi nhuận khi thấy giá phản ứng tại một high bất kỳ" — **chưa có câu trả lời khách quan**, và chỉ bạn mới biết được cảm giác/lý do thật lúc đóng lệnh đó.

Hai khả năng, và chúng dẫn tới hai bài học rất khác nhau:
- **Nếu bạn đóng vì có một tín hiệu cụ thể** (ví dụ: nến M5/M15 đóng ngược xu hướng ngay tại internal high đó, hoặc một MSS/CISD giảm xuất hiện) → đây là một **exit rule hợp lệ**, chỉ cần viết nó thành luật rõ ràng để áp dụng nhất quán các lần sau (và cập nhật lại TP2 log thành "TP2 có điều kiện" thay vì cố định).
- **Nếu bạn đóng chỉ vì thấy giá phản ứng và muốn "bảo toàn lợi nhuận"** mà không có tín hiệu cấu trúc cụ thể nào phủ định luận điểm Bullish còn lại → đây là **chốt lời theo cảm tính (discretionary profit-taking)**, một pattern cần được gắn nhãn và theo dõi lặp lại, vì nó sẽ làm giảm expectancy trung bình mỗi khi runner thực sự đi xa hơn dự kiến.

Ngoài ra, một góc thực tế đáng cân nhắc: giá chỉ chạm TP2 sau 5 ngày, bao gồm khả năng phải giữ lệnh qua ít nhất một cuối tuần. Nếu đây là một lệnh trong tài khoản FTMO/The5ers thật, việc giữ lệnh qua nhiều ngày/cuối tuần cần được đối chiếu với chính sách swap và rủi ro gap giá cuối tuần của từng challenge — đây là điều bạn nên tự kiểm tra lại trong tài liệu quy định hiện hành của FTMO và The5ers trước khi coi "giữ runner 5 ngày" là một chiến lược mặc định, vì tôi không có dữ liệu đủ mới để khẳng định chắc chắn chính sách hiện tại của họ.

### Setup này khớp bao nhiêu % với mô hình chuẩn?

Ước tính **~85%**.
- Khớp tốt: HTF bias + discount alignment; liquidity sweep sạch tại POI; displacement/FVG xác nhận; CISD full-leg hợp lệ; entry đúng CE của BPR, không đua giá; TP đặt đúng thứ tự internal → external.
- Lệch chuẩn: (a) quản lý runner không theo đúng TP2 đã viết trong plan — điểm trừ lớn nhất; (b) nhãn khung xác nhận M5/M15 không nhất quán giữa chart và mô tả bằng lời; (c) cú tap vào OB là tap nông, chưa chạm CE/low OB — không sai nhưng là một biến thể cần theo dõi riêng, không nên trộn chung thống kê với tap sâu.

### Nếu được vào lại, tôi sẽ làm gì khác?

1. **Viết rõ runner management rule trước khi vào lệnh**, ví dụ: sau TP1, dời stop về breakeven, và chỉ đóng phần còn lại khi (a) chạm đúng TP2, hoặc (b) có một tín hiệu cấu trúc cụ thể (M5/M15 đóng nến ngược xu hướng tại mức giá đó) — không đóng thuần theo phản xạ khi thấy giá phản ứng.
2. **Thống nhất khung xác nhận (M5 hay M15) trước khi log**, để dữ liệu trong dashboard so sánh đúng nhóm biến thể.
3. **Tách biến "độ sâu tap vào OB" (nông/sâu) thành field riêng** để backtest có đủ dữ liệu trả lời câu hỏi biến thể nào cho kết quả tốt hơn.
4. **Xác nhận lại số chính xác của stop loss thật** (hiện đang là số suy ra ngược từ RR) để r_planned/r_net trong dashboard chuẩn xác.

---

## 5. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Chain lý luận HTF-to-entry (bias → discount OB → sweep → displacement/FVG → CISD → BPR/CE) chạy đúng và tạo ra một entry chất lượng cao với RR 2.47 tại TP1 — nhưng phần quản lý runner đã lệch khỏi TP2 đã viết trong plan, và đó là bài học thật của lệnh này, không phải phần entry.

> [!warning] Ghi chú của mentor
> Đừng để việc lệnh này "vẫn thắng" che khuất sự thật: bạn đóng runner ở một mức giá không phải TP2 đã định nghĩa, và giá sau đó **vẫn đi đúng hướng thêm 5 ngày nữa**. Lần này chi phí của việc đó chỉ là "R bị bỏ lại trên bàn". Lần khác, chính phản xạ chốt sớm tại một internal high ngẫu nhiên có thể khiến bạn thoát đúng lúc trước một cú giảm sâu — nhưng nếu không có rule khách quan, bạn sẽ không thể phân biệt được lúc nào phản xạ đó là "đọc thị trường tốt" và lúc nào chỉ là hên. Grade B+ đã tính đến việc phần entry gần như hoàn hảo; nếu quản lý runner tiếp tục là một quyết định tùy hứng ở các mẫu sau, grade tổng thể của biến thể "CISD + BPR" sẽ bị kéo xuống bởi chính biến số này, không phải bởi chất lượng entry.

### 5.1. Bài học kỹ thuật

**CISD full-leg reclaim hoạt động đúng như kỳ vọng** — việc đòi hỏi giá đóng cửa vượt qua open của *toàn bộ* cụm nến giảm (không chỉ 1-2 nến gần nhất) cho một tín hiệu xác nhận mạnh hơn CISD "yếu" (chỉ quét 1 nến). Đáng đưa vào Playbook làm tiêu chuẩn ưu tiên cho biến thể CISD.

**BPR (chồng 2 FVG đối nghịch) là điểm entry hiệu quả về risk** — so với việc vào thẳng tại OB gốc (entry sẽ ở vùng 1.695x, risk tới stop dưới OB gần như bằng 0 vì entry đã sát invalidation), vào tại CE của BPR (1.69656) giữ nguyên toàn bộ luận điểm HTF nhưng cho một mức risk hợp lý hơn để tính RR có ý nghĩa (2.47) — miễn là bạn chấp nhận rủi ro giá không quay lại đủ sâu để fill.

**Internal liquidity (EQH) đúng vai trò TP1** — việc chốt một phần tại EQH trước khi nhắm tới H1 Dealing Range High là áp dụng đúng hệ thống phân cấp thanh khoản internal-trước-external, không nhảy cóc thẳng lên external mục tiêu và bỏ qua điểm phản ứng tiềm năng ở giữa.

**Cần phân biệt rõ MSS (wick-based) và CISD (open/close-based)** khi log dữ liệu — hai công cụ trả lời hai câu hỏi khác nhau (structure vs delivery state), và trộn lẫn chúng trong trường `mss` của frontmatter sẽ làm dashboard so sánh sai nhóm biến thể.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- **Đóng runner sớm tại một internal high không nằm trong plan gốc**, ngay khi thấy giá phản ứng — cần kiểm tra các backtest khác trong `04 - Backtesting/` xem đây là lần đầu hay đã lặp lại nhiều lần. Nếu lặp lại, đây xứng đáng có một note riêng trong `06 - Mistake Database/` (ví dụ "Mistake - Đóng runner sớm không theo TP đã plan") để theo dõi tần suất và ảnh hưởng tới expectancy tổng.
- **Chưa có runner management rule cố định** — mỗi lệnh có khả năng được quản lý khác nhau nếu không viết rule rõ trước khi vào lệnh, làm loãng tính so sánh được của mẫu backtest.
- **Nhãn timeframe không nhất quán giữa hình và lời** (M5 vs M15) — một lỗi nhỏ về data hygiene nhưng dễ tích lũy thành nhiều mẫu bị phân loại sai nếu không sửa ngay từ note đầu tiên phát hiện.

### 5.3. Rule cần thêm/cập nhật vào Playbook

- [ ] Viết rule quản lý runner: sau TP1, dời stop về breakeven; chỉ đóng phần còn lại khi chạm đúng TP2 **hoặc** có tín hiệu cấu trúc cụ thể (định nghĩa rõ tín hiệu đó là gì) — không đóng theo phản xạ khi thấy giá phản ứng tại một high/low bất kỳ.
- [ ] Thêm field theo dõi "độ sâu tap vào POI" (nông / sâu) vào schema backtest.
- [ ] Thống nhất và ghi rõ timeframe xác nhận (M5 hay M15) ngay khi chụp chart, tránh lệch giữa hình và lời tường thuật.
- [ ] Nếu pattern "đóng runner sớm" lặp lại ≥3 lần trong các backtest tiếp theo, tạo note mới trong Mistake Database và bắt đầu track tần suất theo tuần trong Weekly Review.

---

## 6. Final Grade

| Tiêu chí                     | Điểm  |
| ----------------------------- | ----- |
| HTF Bias                      | 9/10  |
| POI Selection                 | 8/10 *(tap nông, chưa chạm CE/low OB)* |
| Liquidity Sweep                | 8/10  |
| MSS/CISD Confirmation           | 8/10 *(hợp lệ nhưng cần phân loại đúng là CISD, không phải MSS wick)* |
| FVG / OB / BPR Entry           | 9/10  |
| Risk Management (RR & quản lý runner) | 6/10 *(entry/stop/TP1 tốt, nhưng runner lệch khỏi TP2 plan gốc)* |

**Overall Grade**: **B+** *(đề xuất — bạn tự điều chỉnh theo cảm nhận thực tế của mình, đặc biệt về lý do đóng runner)*

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- Khái niệm: [[25 - OB - Order Block|Order Block]] · [[13 - FVG  - Fair Value Gap|FVG]] · [[03 - Balanced Price Range|BPR]] · [[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment]] · [[41 - Change in State of Delivery|CISD]] · [[21 - Market Structure Shift|MSS]] · [[20 - Liquidity Sweep|Liquidity Sweep]] · [[27 - Premium Discount|Premium Discount]] · [[12 - Dealing Range|Dealing Range]] · [[18 - Kill Zones|Kill Zones]]
- Dashboard: [[_Backtest Dashboard]]
- Template: [[Backtest templete]]
- Mistake liên quan: *(chưa có — xem đề xuất ở mục 5.2 nếu pattern đóng runner sớm lặp lại)*
