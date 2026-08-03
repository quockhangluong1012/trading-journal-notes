---
type: backtest
backtest_date: 2026-07-16
trade_date: 2014-06-25
symbol: GBPUSD
position: Long
result: Win
session: London Open KZ
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model (CISD + BPR Entry)
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: Order Block
poi_rank: 2
poi_timeframe: H1
poi_location: Discount
poi_in_ote:
ce_ote_overlap:
poi_stack: H1 Order Block 1.69395-1.69562 (context, tap nông) + M5 BPR 1.69649-1.69662 (2 FVG đối nghịch overlap, entry)
fvg_high: 1.69662
fvg_low: 1.69649
ce_price: 1.696555
entry_type: CE
entry_precision: CE
limit_filled: Yes
fill_depth_pct:
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: Yes
step5_poi_ok: Yes
step6_entry_ok: Yes
step7_target_ok: Yes
first_error_step: none
missing_step: none
chained_fully: Yes
liquidity_swept: Yes
sweep_type: Internal
displacement: Yes
displacement_score:
mss: Yes
fvg_valid: Yes
confluence_score: 1
smt_confirm: No
cisd_confirm: Yes
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: No
correlated_asset: none
entry_price: 1.69656
stop_loss: 1.6938
take_profit: 1.70311
r_planned: 2.47
rr_if_ce: 2.47
rr_if_ote:
r_multiple:
risk_percent:
spread_cost:
r_net:
grade: B+
followed_plan: Partial
confidence:
confirmation_type: CISD (full-leg reclaim, không phải MSS wick cổ điển)
tp2_extended_target: 1.70634 (H1 DR High, external — không đạt do đóng runner sớm, xem mục 6-7)
tags:
  - backtest
  - ICT2022
  - POI
  - CISD
  - BPR
---

# Backtest 2014-06-25 — GBPUSD Long — POI & Step Decision (CISD + BPR)

> [!info] Ghi chú chuyển đổi (2026-07-17)
> Chuyển từ template cũ sang **Backtest template - POI & Step Decision**. Toàn bộ phân tích gốc giữ nguyên.
> ⚠️ **`mss` chuẩn hoá về scalar `Yes`**: bản gốc ghi `mss: "Yes (dạng CISD, không phải MSS cổ điển...)"` — vi phạm quy tắc "field Yes/No dùng đúng Yes hoặc No, không dùng freetext" của template mới (câu chữ sẽ phá Dataview khi lọc theo `mss = "Yes"`). Đã tách phần diễn giải sang field mở rộng `confirmation_type: CISD (full-leg reclaim)` — giữ được sắc thái quan trọng (CISD ≠ MSS cổ điển) mà không phá field chuẩn.
> ⚠️ **`take_profit` chỉ ghi TP1 (1.70311)`**: template mới chỉ có 1 field `take_profit` scalar, trong khi bản gốc có kế hoạch 2 tầng (TP1 nội bộ 1.70311 / TP2 ngoại vi 1.70634). Vì TP1 là mức đã dùng để tính `r_planned = 2.47` và là mức thực sự đạt được, mình dùng TP1 làm `take_profit` chính thức; TP2 được giữ ở field mở rộng `tp2_extended_target` để không mất thông tin.
> ⚠️ **`r_multiple` để trống**: runner đóng ở một mức giá bạn chưa cung cấp con số cụ thể trong bản gốc — không tự tính để tránh bịa.
> ⚠️ **`stop_loss: 1.6938`**: đây là số *suy ngược* từ RR hiển thị trên platform (risk 0.00276 = 27.6 pip), không phải số đo trực tiếp — bản gốc đã tự flag cần đối chiếu lại lệnh thật.
> ⚠️ **`entry_timeframe: M5`**: chart gốc ghi tay "M5" nhưng phần diễn giải bằng lời gọi là "M15" — giữ theo label trên chart, cần bạn xác nhận.
> `poi_in_ote`/`ce_ote_overlap` để trống vì bản gốc dùng khung Discount/Premium/Equilibrium để đánh giá vị trí POI, không dùng khung OTE fib 62–79% như các file khác — không quy đổi để tránh gán nhầm.
> `followed_plan: Partial` (không phải Yes/No thuần) vì entry/stop/TP1 đúng plan nhưng quản lý runner lệch khỏi TP2 gốc — chi tiết ở mục 6–7.
> `confluence_score = 1` chỉ tính được `cisd_confirm` trong 8 mục cố định của template; các mục khác (SMT, macro time, NWOG...) không được đánh giá theo phong cách phân tích của file này (dùng CISD/BPR/Discount-Premium thay vì OTE fib) — **không nên đọc confluence_score=1 là "confluence yếu"**, xem chi tiết ở mục 5.

---

## 0. Backtest Summary

| Field                 | Value                                                              |
| --------------------- | ------------------------------------------------------------------ |
| Symbol                | GBPUSD                                                             |
| Model Variant         | Standard (D1→H1→M5)                                                |
| Trade Date (dữ liệu)  | 2014-06-25                                                         |
| Position              | Long                                                               |
| Result                | Win (TP1 full, runner đóng sớm — vẫn dương)                        |
| Session               | London Open KZ                                                     |
| HTF Bias              | Bullish                                                            |
| Bias Correct?         | Yes                                                                |
| **POI Type**          | Order Block (H1, Discount)                                        |
| POI Rank (8.1)        | 2 (FVG+OB — BPR lồng cạnh OB)                                      |
| POI Timeframe         | H1 (entry M5 ⚠️ cần xác nhận M5/M15)                               |
| POI Location          | Discount                                                           |
| **Entry Type**        | CE                                                                 |
| **Limit Filled?**     | Yes                                                                |
| **First Error Step**  | none (lỗi nằm ở quản lý runner SAU khi vào lệnh — ngoài 7 bước)    |
| R Planned (TP1)       | 2.47                                                                |
| R Multiple (kết quả)  | (chưa điền — cần giá đóng thực tế của runner)                      |
| Confluence Score (0–8)| 1 (xem ghi chú — khung phân tích khác OTE fib)                     |
| Grade                 | B+ (đề xuất)                                                       |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 — Daily Bias

- **Bias**: Bullish · **Market Condition**: Trending — giá đang trong nhịp tăng mạnh với cấu trúc HH/HL rõ ràng.
- **Lý do xác định bias**: cấu trúc D1 tạo higher-high/higher-low liên tục trước thời điểm setup; không có tín hiệu đảo chiều D1 nào được ghi nhận tại thời điểm phân tích.
- **Draw on Liquidity**: Buy-side (mục tiêu hướng tới) — EQH nội bộ tại 1.70311, xa hơn là H1 Dealing Range High 1.70634. Sell-side — không phải mục tiêu của lệnh Long này, chỉ liên quan nếu bias bị vô hiệu.

![[Pasted image 20260716173453.png]]

### H1 — Cấu trúc & POI

- **Dealing Range H1**: High 1.70634 / Low 1.69167 → Equilibrium = 1.699005.
- **H1 POI**: Order Block 1.69562 (high) – 1.69395 (low), CE của OB = 1.694785.
- **Premium/Discount check**: OB nằm hoàn toàn dưới Equilibrium (1.699005) → đúng phía discount cho setup Long — điều kiện bắt buộc trước khi coi OB là POI hợp lệ, thoả mãn.
- **Phản ứng tại POI**: giá quét bằng bóng nến vào OB nhưng thân nến đóng lại bên ngoài OB — dấu hiệu phía bán không đủ lực giữ giá bên trong OB, một trong những kiểu phản ứng "sạch" nhất khi đánh giá độ tin cậy OB.
- **Ghi chú về độ sâu tap**: bóng nến chỉ chọc vào phần trên của OB (khoảng 1.6951–1.6953), KHÔNG chạm CE (1.694785) hay low của OB (1.69395) — cú tap NÔNG. Không sai về nguyên tắc, nhưng là biến số nên theo dõi riêng (tap nông vs tap sâu) trong dashboard.

![[Pasted image 20260716173421.png]]

---

## 2. POI Profile

- **POI Type đã dùng**: Order Block (H1), Discount.
- **POI Rank (8.1)**: 2 (FVG+OB — BPR hình thành ngay cạnh OB).
- **POI hình thành trên khung**: H1 (entry refine M5).
- **POI nằm ở**: Discount ✓ (đúng phía cho Long).
- **POI stack**: H1 OB (1.69395–1.69562, tap nông) + M5 BPR (1.69649–1.69662, entry).
- **CE của FVG trùng OTE 62–79%?**: không đánh giá theo khung OTE fib trong file này (dùng Discount/Premium/Equilibrium thay thế).
- **Bounds & CE**: BPR High 1.69662 / Low 1.69649, CE = 1.696555 (≈ entry thực tế 1.69656 — khớp gần như tuyệt đối).

![[Pasted image 20260716173421.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE
- **Entry Precision**: CE (BPR)
- **Limit có khớp?**: Yes
- **Giá đi sâu bao nhiêu vào FVG/BPR?**: không có số đo % cụ thể trong bản gốc
- **RR ghi lại**: r_planned (TP1) = rr_if_ce = 2.47

### M5 — Xác nhận & Điểm vào lệnh

1. **Liquidity sweep vào OB**: bóng nến quét vào phần trên của OB, thân đóng ngoài.
2. **Displacement + FVG (Bullish)**: sau khi bật khỏi OB, giá tạo nhịp displacement mạnh, để lại FVG Bullish — xác nhận động lượng đảo chiều đủ mạnh để tin vào OB.
3. **CISD (Change in State of Delivery) — full leg reclaim**: giá đóng nến vượt qua open của toàn bộ cụm nến giảm trong nhịp retrace về OB (không chỉ 1-2 nến gần nhất) — bản CISD "đầy đủ", mạnh hơn CISD chỉ quét qua nến giảm cuối cùng. **Ghi chú khái niệm**: CISD dùng open/close (body) làm mốc, khác MSS cổ điển (dùng wick để định nghĩa swing point, cần nến đóng cửa qua đúng wick đó để xác nhận phá vỡ). CISD ở đây là công cụ hợp lệ, trả lời câu hỏi "trạng thái giao hàng đã đổi chưa" ở cấp vi mô, không thay thế MSS cấu trúc lớn.
4. **BPR hình thành**: nhịp retrace ban đầu (vào OB) tạo FVG Bearish; nhịp displacement bật ra sau đó tạo FVG Bullish. Hai FVG đối nghịch chồng lên nhau → **BPR: 1.69662 (high) – 1.69649 (low)**.
5. **Entry tại CE của BPR**: CE = (1.69662+1.69649)/2 = 1.696555 ≈ 1.69656.
6. **Stop Loss**: dưới low của OB (1.69395) + buffer nhỏ, ước tính ~1.69380 (buffer ~1.5 pip) dựa trên RR hiển thị platform — cần xác nhận số chính xác.
7. **Take Profit 2 tầng**: TP1 = 1.70311 (Equal Highs, internal liquidity — nằm trên Equilibrium 1.699005, tức premium của range H1, hợp lý vì internal liquidity thường nơi vị thế cũ chốt lời). TP2 = 1.70634 (H1 Dealing Range High, external liquidity, mục tiêu cuối theo đúng hệ thống internal-trước-external).

![[Screenshot 2026-07-16 150746 1.png]]

**Entry trigger**: Liquidity Sweep vào H1 OB (wick, thân đóng ngoài) → Displacement + FVG Bullish trên khung xác nhận → CISD full-leg reclaim → BPR (2 FVG đối nghịch chồng nhau) → entry tại CE.

**Entry reason**: chain đầy đủ — HTF bias Bullish → discount POI (H1 OB) → phản ứng bóng nến sạch → displacement/FVG xác nhận → CISD xác nhận trạng thái giao hàng đã đổi → BPR cho điểm entry risk thấp hơn OB gốc trong khi vẫn giữ đúng toàn bộ luận điểm HTF.

**Invalidation**: giá đóng nến qua low của H1 OB (dưới ~1.69395) → luận điểm Long bị vô hiệu.

**Chờ đủ điều kiện?**: Có — không đua giá tại displacement, chờ đúng retrace về CE của BPR mới vào.

## Kết quả:
![[Screenshot 2026-07-16 153007.png]]

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes (wick vào OB, thân đóng ngoài) | `step3_sweep_ok` |
| 4 | Displacement + MSS (dạng CISD) | Yes | `step4_displacement_ok` |
| 5 | POI (Order Block, Discount) | Yes | `step5_poi_ok` |
| 6 | Entry (retrace CE của BPR) | Yes | `step6_entry_ok` |
| 7 | Target (TP1 đạt đúng plan) | Yes | `step7_target_ok` |

- **First Error Step**: none — chuỗi entry hoàn chỉnh và đúng. ⚠️ Lỗi thật của lệnh này (quản lý runner lệch TP2) xảy ra **sau** bước 7, ngoài phạm vi 7 bước của template — xem mục 6-7 để không bỏ sót bài học chính.
- **Missing Step**: none
- **Đủ chuỗi 7 bước?**: Yes

---

## 5. Setup Quality & Confluence

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1 — Bullish D1, OB H1 đúng phía discount.
- [x] Giá nằm trong Kill Zone (London Open).
- [x] Có Liquidity Sweep trước entry — bóng nến quét vào OB, thân đóng ngoài.
- [x] Có Displacement rõ ràng — nhịp bật khỏi OB tạo FVG Bullish sạch.
- [x] Có MSS hợp lệ (dạng CISD full-leg reclaim, không phải phá swing-high theo wick).
- [x] FVG/OB nằm trong Discount (buy) — OB dưới Equilibrium 1.699005.
- [x] Entry trong POI hợp lệ, không đua giá — vào đúng CE của BPR, chờ retrace.
- [x] SL ở vùng invalidation hợp lý — dưới low OB, nhưng khá xa so với entry (điểm cần cải thiện).
- [x] RR tối thiểu đạt ≥1:2 — RR đến TP1 = 2.47.
- [ ] Cú tap vào OB là tap sâu (chạm CE/low OB) — Không, chỉ tap nông vào phần trên OB (không bắt buộc, nhưng là biến số theo dõi).

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không (rank 2) | *(suy từ poi_rank)* |
| 2 | CE FVG trùng OTE 62–79% | Không đánh giá (dùng Discount/Premium thay OTE) | `ce_ote_overlap` |
| 3 | SMT divergence | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | **Có** | `cisd_confirm` |
| 5 | Macro time | Chưa đánh giá | `in_macro_time` |
| 6 | NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | SD target align | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Không rõ ràng (đây là phản ứng tại POI, không phải inducement trước POI) | `idm_swept` |

- **Score**: 1/8 theo 8 mục cố định — **không phản ánh đúng chất lượng thật của lệnh**. Bản thân chain lý luận (bias→discount POI→sweep sạch→displacement/FVG→CISD→BPR/CE) là một dạng confluence rất mạnh nhưng nằm ngoài 8 mục cố định của template (vốn thiên về SMT/macro time/NWOG). Đừng dùng điểm số 1/8 để hạ thấp đánh giá lệnh này.

---

## 6. Phân tích sau lệnh (Replay)

**Result**: TP1 hit đầy đủ (2.47R). Runner: **đóng tay** khi giá quét một internal liquidity high khác (giữa TP1/EQH 1.70311 và TP2/DR High 1.70634) rồi đảo chiều — **không chạm TP2 theo plan gốc**. Replay sau đó cho thấy giá thực tế **có vượt qua TP2** (1.70634) vào ngày 2014-06-30, tức **5 ngày sau** khi phần runner đã bị đóng.

### Tại sao lệnh thắng (root cause thật, không chỉ vì "TP1 chạy trúng")
Đi đúng chain lý luận: HTF bias Bullish + OB discount + phản ứng bóng nến sạch tại POI + displacement/FVG xác nhận + CISD full-leg reclaim + entry đúng CE của BPR (risk thấp hơn nhiều so với vào tại OB gốc) + TP1 đặt đúng tại internal liquidity trước khi nhắm external liquidity. Mỗi lớp trong chain đều có lý do rõ ràng, không có mắt xích nào là "hy vọng" hay curve-fit sau khi biết kết quả.

### Vấn đề thật sự cần mổ xẻ: quyết định đóng runner sớm
Plan gốc viết rõ: TP2 = H1 Dealing Range High (1.70634), external liquidity, mục tiêu cuối cho phần runner sau khi chốt một phần tại TP1. Nhưng thực tế, runner bị đóng tại một mức giá khác — internal liquidity high nằm giữa TP1 và TP2 — ngay khi giá phản ứng/đảo chiều tại đó. Đây là một sự **lệch khỏi plan đã viết**, dù kết quả cuối cùng vẫn dương.

Theo nguyên tắc "process over outcome" của vault: một lệnh được đánh giá bằng việc có theo đúng plan đã kiểm định hay không, không phải bằng việc nó có thắng hay không. Việc giá sau đó (5 ngày sau) vượt qua TP2 — dữ liệu hindsight này KHÔNG biện minh cho quyết định đóng sớm, và cũng không có nghĩa quyết định đóng sớm là sai. Nó chỉ cho thấy: nếu có một rule quản lý runner được định nghĩa rõ từ trước, sẽ biết chắc lần này có tuân thủ hay không.

Hai khả năng, hai bài học khác nhau:
- **Nếu đóng vì có tín hiệu cụ thể** (nến M5/M15 đóng ngược xu hướng tại internal high đó, hoặc MSS/CISD giảm xuất hiện) → đây là exit rule hợp lệ, chỉ cần viết thành luật rõ ràng để áp dụng nhất quán các lần sau (và cập nhật TP2 log thành "TP2 có điều kiện" thay vì cố định).
- **Nếu đóng chỉ vì thấy giá phản ứng và muốn "bảo toàn lợi nhuận"** mà không có tín hiệu cấu trúc cụ thể nào phủ định luận điểm Bullish còn lại → đây là chốt lời theo cảm tính (discretionary profit-taking), pattern cần được gắn nhãn và theo dõi lặp lại vì sẽ làm giảm expectancy trung bình mỗi khi runner thực sự đi xa hơn dự kiến.

Góc thực tế đáng cân nhắc: giá chỉ chạm TP2 sau 5 ngày, bao gồm khả năng phải giữ lệnh qua ít nhất một cuối tuần. Nếu đây là lệnh trong tài khoản FTMO/The5ers thật, việc giữ lệnh qua nhiều ngày/cuối tuần cần được đối chiếu với chính sách swap và rủi ro gap giá cuối tuần của từng challenge — nên tự kiểm tra lại tài liệu quy định hiện hành của FTMO và The5ers trước khi coi "giữ runner 5 ngày" là chiến lược mặc định.

### Setup này khớp bao nhiêu % với mô hình chuẩn?
Ước tính ~85%. Khớp tốt: HTF bias + discount alignment; liquidity sweep sạch tại POI; displacement/FVG xác nhận; CISD full-leg hợp lệ; entry đúng CE của BPR, không đua giá; TP đặt đúng thứ tự internal→external. Lệch chuẩn: (a) quản lý runner không theo đúng TP2 đã viết trong plan — điểm trừ lớn nhất; (b) nhãn khung xác nhận M5/M15 không nhất quán giữa chart và mô tả bằng lời; (c) cú tap vào OB là tap nông, chưa chạm CE/low OB — không sai nhưng là biến thể cần theo dõi riêng.

### Nếu vào lại, làm gì khác?
1. Viết rõ runner management rule trước khi vào lệnh: sau TP1, dời stop về breakeven, chỉ đóng phần còn lại khi (a) chạm đúng TP2, hoặc (b) có tín hiệu cấu trúc cụ thể — không đóng thuần theo phản xạ khi thấy giá phản ứng.
2. Thống nhất khung xác nhận (M5 hay M15) trước khi log.
3. Tách biến "độ sâu tap vào OB" (nông/sâu) thành field riêng.
4. Xác nhận lại số chính xác của stop loss thật (hiện đang suy ngược từ RR).

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Chain lý luận HTF-to-entry (bias→discount OB→sweep→displacement/FVG→CISD→BPR/CE) chạy đúng và tạo ra entry chất lượng cao với RR 2.47 tại TP1 — nhưng phần quản lý runner đã lệch khỏi TP2 đã viết trong plan, và đó là bài học thật của lệnh này, không phải phần entry.

> [!warning] Ghi chú của mentor
> Đừng để việc lệnh này "vẫn thắng" che khuất sự thật: đóng runner ở một mức giá không phải TP2 đã định nghĩa, và giá sau đó vẫn đi đúng hướng thêm 5 ngày nữa. Lần này chi phí chỉ là "R bị bỏ lại trên bàn". Lần khác, chính phản xạ chốt sớm tại một internal high ngẫu nhiên có thể khiến thoát đúng lúc trước một cú giảm sâu — nhưng nếu không có rule khách quan, sẽ không thể phân biệt được lúc nào phản xạ đó là "đọc thị trường tốt" và lúc nào chỉ là hên. Grade B+ đã tính đến việc phần entry gần như hoàn hảo; nếu quản lý runner tiếp tục là quyết định tùy hứng ở các mẫu sau, grade tổng thể của biến thể "CISD + BPR" sẽ bị kéo xuống bởi chính biến số này, không phải bởi chất lượng entry.

### 7.1. Bài học kỹ thuật

**CISD full-leg reclaim hoạt động đúng như kỳ vọng** — đòi hỏi giá đóng cửa vượt qua open của toàn bộ cụm nến giảm (không chỉ 1-2 nến gần nhất) cho tín hiệu xác nhận mạnh hơn CISD "yếu" (chỉ quét 1 nến). Đáng đưa vào Playbook làm tiêu chuẩn ưu tiên cho biến thể CISD.

**BPR (chồng 2 FVG đối nghịch) là điểm entry hiệu quả về risk** — so với vào thẳng tại OB gốc (risk tới stop dưới OB gần như bằng 0 vì entry đã sát invalidation), vào tại CE của BPR (1.69656) giữ nguyên luận điểm HTF nhưng cho mức risk hợp lý hơn để tính RR có ý nghĩa (2.47) — miễn là chấp nhận rủi ro giá không quay lại đủ sâu để fill.

**Internal liquidity (EQH) đúng vai trò TP1** — chốt một phần tại EQH trước khi nhắm H1 DR High là áp dụng đúng hệ thống phân cấp thanh khoản internal-trước-external, không nhảy cóc thẳng lên external và bỏ qua điểm phản ứng tiềm năng ở giữa.

**Cần phân biệt rõ MSS (wick-based) và CISD (open/close-based)** khi log dữ liệu — hai công cụ trả lời hai câu hỏi khác nhau (structure vs delivery state); trộn lẫn chúng trong field `mss` sẽ làm dashboard so sánh sai nhóm biến thể (đã tách bằng field `confirmation_type` trong lần chuyển đổi này).

### 7.2. Pattern lặp lại

- **Đóng runner sớm tại một internal high không nằm trong plan gốc**, ngay khi thấy giá phản ứng — cần kiểm tra các backtest khác trong `04 - Backtesting/` xem đây là lần đầu hay đã lặp lại nhiều lần. Nếu lặp lại, xứng đáng có note riêng trong `06 - Mistake Database/` (ví dụ "Mistake - Đóng runner sớm không theo TP đã plan").
- **Chưa có runner management rule cố định** — mỗi lệnh có khả năng được quản lý khác nhau nếu không viết rule rõ trước khi vào lệnh.
- **Nhãn timeframe không nhất quán giữa hình và lời** (M5 vs M15) — lỗi nhỏ về data hygiene nhưng dễ tích lũy thành nhiều mẫu bị phân loại sai.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] Viết rule quản lý runner: sau TP1, dời stop về breakeven; chỉ đóng phần còn lại khi chạm đúng TP2 **hoặc** có tín hiệu cấu trúc cụ thể (định nghĩa rõ) — không đóng theo phản xạ khi thấy giá phản ứng tại một high/low bất kỳ.
- [ ] Thêm field theo dõi "độ sâu tap vào POI" (nông/sâu) vào schema backtest.
- [ ] Thống nhất và ghi rõ timeframe xác nhận (M5 hay M15) ngay khi chụp chart.
- [ ] Nếu pattern "đóng runner sớm" lặp lại ≥3 lần trong các backtest tiếp theo, tạo note mới trong Mistake Database và bắt đầu track tần suất theo tuần trong Weekly Review.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 |
| POI Selection (tap nông, chưa chạm CE/low OB) | 8/10 |
| Liquidity Sweep | 8/10 |
| Displacement/MSS quality (CISD Confirmation — hợp lệ nhưng cần phân loại đúng là CISD, không phải MSS wick) | 8/10 |
| Entry Precision & Fill (FVG/OB/BPR Entry) | 9/10 |
| Risk Management (RR & quản lý runner) | 6/10 — entry/stop/TP1 tốt, nhưng runner lệch khỏi TP2 plan gốc |

**Overall Grade**: **B+** (đề xuất — tự điều chỉnh theo cảm nhận thực tế, đặc biệt về lý do đóng runner)

---

## 9. Phân tích chuyên sâu bổ sung (2026-08-03)

> [!important] Lưu ý phát hiện quan trọng nhất của cả batch
> File `2026-07-17/01 - Win - GBPUSD - 2014-06-25 - Long.md` (được giao là "note 3", cùng lệnh với note này) thực ra có `trade_date: 2014-07-14` trong frontmatter, KHÔNG PHẢI `2014-06-25` — tên file của bản 07-17 sai (chính bản đó tự cảnh báo trong callout đầu file: "tên file (2014-06-25) không khớp ngày lệnh (2014-07-14)... nên đổi tên"). Đây **không phải hai bản phân tích của cùng một lệnh** như brief mô tả — đây là **hai lệnh GBPUSD Long khác nhau, xảy ra cách nhau ~19 ngày**, vô tình có filename trùng do lỗi đặt tên chưa sửa. Toàn bộ phần so sánh "self-consistency 2 bản cùng lệnh" ở note 3 dưới đây được viết lại thành so sánh **rule drift giữa 2 lệnh khác nhau cùng biến thể** thay vì lỗi diễn giải của cùng 1 lệnh — đây tự nó là một finding data-hygiene cấp batch, không phải lỗi phân tích của bên nào.

**Bản đồ liquidity IRL↔ERL tại thời điểm entry (1.69656).** POI stack: H1 OB (1.69395–1.69562, ERL tương đối vì đây là ranh giới nơi bias được xác nhận) + M5 BPR (1.69649–1.69662, IRL — imbalance nội bộ vừa hình thành từ 2 FVG đối nghịch). Note gốc mô tả cú tap OB là "nông" (chỉ chạm 1.6951–1.6953, không chạm CE/low OB) — nghĩa là ERL-cấp-OB chưa bị lấy dứt điểm trước khi CISD xác nhận. Theo đúng logic ERL→IRL đã áp dụng ở note 4 loss cùng batch ([[02 - Loss - GBPUSD - 2014-07-17 - Long]]), đây lẽ ra là một cờ cảnh báo tương tự "tap nông + MSS sớm = LTF inducement" — nhưng ở đây note gốc lại không đặt câu hỏi này, có thể vì công cụ xác nhận là CISD (open/close) chứ không phải MSS (wick), và bản thân note gốc mục 5 tự flag "SL khá xa entry" như một điểm cần cải thiện chứ không phải một red flag cấu trúc. Đáng đối chiếu: SSL/EQL nội bộ giữa OB low (1.69395) và DR Low H1 (1.69167, không nêu rõ trong note) có bị lấy trước không — note không trả lời, để `[UNSUPPORTED]`.

**Chất lượng CISD.** Note gốc phân biệt đúng CISD (open/close, "full-leg reclaim") với MSS cổ điển (wick-based) — đây là điểm mạnh khái niệm hiếm thấy trong vault (so với note 4 loss, nơi MSS wick-based bị dùng sai vì bỏ qua điều kiện sweep trước). "Full-leg reclaim" (đóng cửa vượt open của TOÀN BỘ cụm nến giảm, không chỉ 1-2 nến gần nhất) là tiêu chuẩn cao hơn CISD "yếu" — nhưng note không định lượng "toàn bộ cụm" là bao nhiêu nến, để đối chiếu định lượng với các CISD khác trong vault sau này.

**Yếu tố thời gian.** Session London Open KZ — killzone chuẩn cho GBP. Note không ghi giờ cụ thể (không có timestamp entry) — thiếu dữ liệu để đo tốc độ resolve từ CISD tới entry, khác với note 4 (có timeline chi tiết theo giờ UTC+7).

**Vị trí entry trong dealing range.** OB nằm hoàn toàn dưới Equilibrium (1.699005) → đúng phía Discount. Nhưng note không dùng khung OTE fib (62–79%) để đánh giá độ sâu — chỉ dùng nhị phân Discount/Premium. Nếu tính theo OTE trên range H1 (Low 1.69167 giả định – High 1.70634): CE BPR 1.696555 nằm ở khoảng fib nào so với 0.618/0.705/0.786 không được tính trong note — một khoảng trống đánh giá so với note 3 và note 4 (cả hai đều dùng khung OTE fib chi tiết).

**So sánh với các lệnh khác cùng mẫu trong vault.**
- Với [[01 - Win - EURUSD - 2016-06-12 - Short|EURUSD 2016-06-12]] (note 1 batch này): cả hai đều là "process win" có root cause tách biệt khỏi phần không hoàn hảo của outcome — EURUSD tách khỏi gap cuối tuần, GBPUSD tách khỏi runner bị đóng sớm. Điểm chung: cả hai note đều tự phê bình rất kỹ, một dấu hiệu tốt về văn hóa backtest của vault này.
- Với [[02 - Loss - GBPUSD - 2014-07-17 - Long]] (note 4 batch này, Loss): note 4 dùng MSS wick-based và bị lỗi bỏ qua sweep cấu trúc; note này dùng CISD open/close và không có lỗi tương tự được nêu — nhưng cũng không kiểm tra ERL bên dưới OB, nên chưa chắc "an toàn hơn" chỉ vì công cụ xác nhận khác, có thể đơn giản là chưa gặp trường hợp bất lợi.
- Với note 3 (07-17, lệnh 2014-07-14 khác) — xem so sánh chi tiết ở mục 10 dưới, vì đây là góc brief yêu cầu tập trung nhất dù đối tượng so sánh thực chất khác lệnh.

![[GBPUSD-20140625-cisd-bpr-runner.svg|760]]

## 10. Phản biện chuyên sâu (Devil's Advocate)

```yaml
type: devils-advocate
mode: REVIEW
instrument: GBPUSD
date: 2014-06-25
timeframes_provided: [D1, H1, M5] (mô tả bằng lời + 4 ảnh PNG không đọc được)
verdict: SURVIVES, WEAKENED
evidence_sufficiency: thin
opposite_case_strength: weaker but non-trivial
objections: {fatal: 0, material: 3, minor: 2}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN, O4 OPEN, O5 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base.** 4 wikilink ảnh (`Pasted image...`, `Screenshot...`) không đọc được trong môi trường này. Toàn bộ evidence base là số liệu + mô tả trong chính note. `evidence_sufficiency = thin` — load-bearing claim (CISD full-leg reclaim là xác nhận hợp lệ) không thể kiểm tra độc lập bằng chart.

**1. Thesis + load-bearing claim.**
- C1: HTF bias Bullish (D1 HH/HL) — mô tả định tính, không kèm số liệu OHLC.
- C2: OB H1 (1.69395–1.69562) nằm dưới Equilibrium → Discount hợp lệ (arithmetic verify: EQ = 1.699005, khớp).
- C3: Phản ứng tại OB là "sạch" (wick vào, thân đóng ngoài) → xác nhận OB.
- C4: CISD full-leg reclaim xác nhận đổi trạng thái giao hàng → entry tại CE BPR hợp lệ (**load-bearing** — toàn bộ chain và grade B+ phụ thuộc vào việc CISD này có thật sự đủ mạnh để thay thế vai trò MSS hay không).
- C5: r_planned = 2.47 tính từ entry 1.69656 / SL 1.6938 / TP1 1.70311.
- Inference: C1+C2+C3 → C4 → entry hợp lệ; C4 độc lập với quyết định đóng runner sớm (ngoài phạm vi 7 bước).

**2. Điều gì survive.** Việc tách biệt "quản lý runner" khỏi "chuỗi entry 7 bước" là kỷ luật phân tích đúng đắn — note không để outcome dương (Win tổng thể) che giấu lỗi lệch plan ở phần runner. Phân biệt CISD (open/close) và MSS (wick) là điểm mạnh khái niệm, đúng theo doctrine.

**3. Objections.**

**O1 · [ARITHMETIC] · material · attacks C5**
Claim: `r_planned: 2.47` từ entry 1.69656, SL 1.6938, TP1 1.70311.
Evidence: Tính lại: risk = |1.69656−1.6938| = 0.00276 (27.6 pip), reward = |1.70311−1.69656| = 0.00655 (65.5 pip) → RR = 65.5/27.6 = **2.373**, không phải 2.47. Chênh lệch ~0.1R (~4%).
Consequence: `r_planned` trong frontmatter không tự nhất quán với chính `entry_price`/`stop_loss`/`take_profit` cũng nằm trong frontmatter — ảnh hưởng trực tiếp tới thống kê expectancy nếu dùng field `r_planned` thay vì tính lại từ giá.
Your best answer: Note tự flag rằng `stop_loss: 1.6938` là số "suy ngược từ RR hiển thị trên platform", không phải đo trực tiếp — nghĩa là 2.47 có thể là RR gốc hiển thị trên platform (dùng SL thật, chưa biết), còn 1.6938 là SL bị suy ngược sai một chút từ chính con số 2.47 đó, tạo ra một vòng lặp tính toán không khớp khi tính xuôi lại.
Retracted by: Cung cấp SL thật đo trực tiếp từ chart (không suy ngược từ RR).

**O2 · [HINDSIGHT] · material · attacks C4**
Claim: "CISD full-leg reclaim hoạt động đúng như kỳ vọng" (Lesson 1, mục 7.1 note gốc) được viết như một kết luận đã kiểm chứng.
Evidence: Kết luận này chỉ dựa trên kết quả của chính lệnh đang được đánh giá (TP1 hit) — không có mẫu độc lập nào khác trong note để so sánh "CISD full-leg" với "CISD yếu" trên cùng điều kiện.
Consequence: Nếu chỉ n=1, "hoạt động đúng như kỳ vọng" là một câu khẳng định vượt quá những gì 1 mẫu chứng minh được — đúng dạng outcome-as-evidence-cho-process mà mode REVIEW phải săn theo brief.
Your best answer: Note không tuyên bố đây là rule đã kiểm chứng qua nhiều mẫu, chỉ đề xuất "đáng đưa vào Playbook làm tiêu chuẩn ưu tiên" — nhưng câu mở đầu "hoạt động đúng như kỳ vọng" vẫn đọc như một xác nhận, không phải một giả thuyết cần thêm mẫu.
Retracted by: Backtest thêm ≥10 mẫu CISD full-leg so với CISD yếu, đo win rate/expectancy riêng.

**O3 · [UNSUPPORTED] · material · attacks C3**
Claim: "phản ứng tại OB là một trong những kiểu phản ứng 'sạch' nhất khi đánh giá độ tin cậy OB."
Evidence: Không có ảnh đọc được hoặc OHLC cụ thể của nến phản ứng (biên độ wick, thân nến) để xác nhận "sạch" theo nghĩa nào — đây là đánh giá định tính không kèm số.
Consequence: Nếu phản ứng thực tế yếu hơn mô tả, độ tin cậy của C2+C3 (nền tảng cho C4) giảm.
Retracted by: OHLC nến phản ứng hoặc ảnh H1 đọc được.

**O4 · [METHOD] · minor**
`followed_plan: Partial` cùng `confluence_score: 1` được note tự giải thích là "không phản ánh đúng chất lượng thật" — một dạng tự miễn trừ điểm số template. Hợp lý về logic (8 mục cố định thiên về SMT/macro time, không đo được chain CISD/BPR) nhưng cũng là điểm cần cảnh giác: mọi lệnh có confluence_score thấp đều có thể viện lý do tương tự để "không tính điểm thấp là điểm thấp thật".
Retracted by: n/a — ghi nhận để theo dõi liệu lý do miễn trừ này có lặp lại có hệ thống ở các note khác trong vault hay không (nếu có, đó là một dạng grade inflation cần soi riêng).

**O5 · [UNSUPPORTED] · minor**
"Ước tính ~85% khớp mô hình chuẩn" không có breakdown cụ thể cấu thành từ đâu.
Retracted by: Bảng điểm chi tiết cho từng thành phần.

Bộ lọc: 6 objection nháp, cắt 1 (một objection về "session không ghi giờ cụ thể" bị coi quá vụn) → còn 5.

**4. Opposite case.** Đọc ngược: CISD full-leg reclaim tại đây có thể chỉ là một retrace bình thường bị đọc quá tay thành "đổi trạng thái giao hàng" — vì cú tap vào OB là NÔNG (không chạm CE/low OB), phản ứng có thể chỉ là một nhịp phục hồi kỹ thuật ngắn hạn (dead-cat bounce trong ngôn ngữ non-ICT) chứ chưa chắc smart money đã thật sự "xong việc" tại OB đó — giống hệt cơ chế mà note 4 cùng batch mô tả cho trường hợp Loss (tap nông + MSS sớm = LTF inducement). Nếu áp cùng chuẩn nghi ngờ đó vào đây, CISD ở CE BPR 1.69656 cũng có thể là một internal inducement trước khi giá quay lại quét sâu hơn vào OB — nhưng thực tế nó không xảy ra (giá chạy thẳng lên TP1). Tự phản biện case ngược: nó không giải thích được tại sao, nếu là inducement, giá lại không quay lại test OB gốc trước khi tiếp tục — dữ liệu thực tế ủng hộ case gốc hơn. Nhãn: **weaker but non-trivial** — case ngược không thắng nhưng cùng khung nghi ngờ ("tap nông = cảnh báo") lẽ ra nên được note gốc tự áp dụng nhất quán thay vì chỉ áp dụng ở note Loss. Observable phân biệt: nếu backtest thêm các case "tap nông + CISD full-leg" khác trong vault mà đa số đều thắng, case gốc được củng cố; nếu nhiều case tương tự thất bại (giá quay lại quét sâu OB trước khi đi), case ngược thắng và "tap nông" cần thành cờ giảm size bất kể công cụ xác nhận là CISD hay MSS.

**5. Verdict: SURVIVES, WEAKENED.** Chain lý luận (C1-C4) không bị phá bởi CHART/DOCTRINE/ARITHMETIC trực tiếp nào — nhưng O1 (arithmetic RR lệch 0.1R) và O2 (hindsight nhẹ ở "CISD hoạt động đúng như kỳ vọng") làm yếu độ tin cậy của các con số và kết luận đi kèm. Điều tôi không phá được: logic entry CISD+BPR và tính hợp lệ Discount/Premium. Điều critique này không xác lập: rằng CISD full-leg reclaim là một công cụ đã kiểm chứng qua nhiều mẫu — vẫn là n=1.

**6. Falsification tests.**
1. Đo lại SL thật bằng chart trực tiếp (không suy ngược từ RR) và tính lại RR — nếu ra đúng 2.47, đóng O1; nếu ra ~2.37 khớp tính toán ở đây, sửa `r_planned` trong frontmatter.
2. Backtest ≥10 mẫu "tap nông vào OB + CISD full-leg xác nhận" so với "tap sâu (chạm CE/low OB) + CISD" — so win rate. Nếu tap nông có win rate thấp hơn rõ rệt, áp cùng logic "tap nông = cờ cảnh báo" đã dùng ở note 4 vào biến thể CISD/BPR.
3. Backtest ≥10 mẫu runner được quản lý theo rule rõ ràng (breakeven sau TP1, đóng chỉ khi chạm TP2 hoặc tín hiệu cấu trúc cụ thể) so với đóng theo phản xạ — đo R trung bình bị "bỏ lại trên bàn" mỗi kiểu.

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Chuỗi Bias(Bullish D1) → Discount POI(H1 OB) → Sweep(tap nông, thân đóng ngoài) → Displacement+CISD(full-leg reclaim) → BPR entry tại CE là một setup Long hợp lệ theo biến thể CISD của ICT 2022 Model.

**Cần sửa** (load-bearing trước):
- C4 (CISD xác nhận là công cụ hợp lệ thay thế MSS) — **AMBIGUOUS** · why: SKILL.md § CISD định nghĩa "đổi state of delivery, dùng open/close, không đồng nghĩa tùy tiện với MSS" — note gốc đã tự phân biệt đúng, nhưng doctrine không quy định rõ ràng CISD có đủ tự thân thay thế vai trò "Displacement + MSS" (bước 4 của 7-step) hay cần đi kèm MSS riêng biệt trên cùng khung → đây là doctrine gap thật sự, không phải lỗi của tác giả → fix: không cần sửa gì thêm phía tác giả, nhưng ghi nhận gap để tránh áp chuẩn khắt khe hơn canon.
- C1 (HH/HL D1) — **UNSUPPORTED** · why: mô tả định tính, không kèm OHLC hay ảnh đọc được → fix: đính kèm số liệu D1 cụ thể.
- C3 (phản ứng "sạch" tại OB) — **UNSUPPORTED** · why: không có OHLC nến phản ứng để đối chiếu "wick vào, thân đóng ngoài" → fix: cung cấp giá cao/thấp/đóng của nến phản ứng.

**PASS:** C2 (Premium/Discount: OB dưới EQ 1.699005 → Discount đúng phía cho Long, arithmetic khớp), C6 (CE BPR = (1.69662+1.69649)/2 = 1.696555, khớp entry 1.69656 gần như tuyệt đối — entry precision đúng chuẩn CE).

**Verdict: PARTIALLY ALIGNED** — load-bearing claim C4 rơi vào AMBIGUOUS do doctrine gap (không phải lỗi tác giả), C1/C3 UNSUPPORTED vì thiếu chart; C2/C6 PASS vững bằng arithmetic. Không có FAIL nào (không claim nào gọi sai tên hiện tượng) nên không rơi xuống NOT ALIGNED, nhưng cũng chưa đủ để DOCTRINE ALIGNED vì load-bearing chưa được evidence hoàn toàn xác nhận.

**Notes:** Doctrine gap ghi nhận — canon (theo SKILL.md hiện có) không nói rõ CISD full-leg reclaim một mình có đủ điều kiện thay thế "Displacement + MSS" ở bước 4 của 7-step hay cần một MSS riêng đi kèm trên cùng khung thời gian. Đề xuất bổ sung vào doctrine.md: làm rõ ranh giới "CISD-as-structural-confirmation" vs "CISD-as-delivery-confirmation-only cần MSS đi kèm".

## 12. Lesson Learned (bản đầy đủ)

### (a) Bài học kỹ thuật
1. **CISD full-leg reclaim là công cụ hợp lệ nhưng chưa kiểm chứng qua nhiều mẫu.** Ví dụ số thật: entry CE BPR 1.69656, CISD xác nhận bằng đóng cửa vượt open của toàn bộ cụm nến giảm trong nhịp retrace về OB. Tổng quát hóa: trước khi coi CISD full-leg là "chuẩn ưu tiên" cho Playbook (như Lesson 1 note gốc đề xuất), cần ≥10 mẫu so sánh với CISD yếu.
2. **Frontmatter tự mâu thuẫn khi một field được suy ngược từ field khác rồi dùng để verify chính field gốc.** Ví dụ số thật: SL 1.6938 suy ngược từ RR 2.47, nhưng tính xuôi lại từ SL đó ra RR 2.373 — vòng lặp không khớp. Tổng quát hóa: bất kỳ trường nào ghi "suy ngược từ X" đều không nên dùng để verify lại X.
3. **Tap nông vào OB xuất hiện ở cả lệnh Win (note này) và Loss (note 4 batch này) — biến số này chưa đủ để tự nó là tín hiệu, cần kết hợp với việc ERL bên dưới có bị quét hay không.**

### (b) Bài học quy trình/checklist
- Thiếu rule quản lý runner viết TRƯỚC khi vào lệnh — dẫn tới lệch TP2 đã plan (note gốc đã tự nêu rất kỹ, ở đây nhấn mạnh lại vì đây là lỗi thật duy nhất của lệnh, nằm ngoài 7 bước).
- Thiếu thống nhất khung xác nhận (M5 vs M15 — note gốc tự flag mâu thuẫn giữa nhãn chart và mô tả lời).
- Thiếu số đo trực tiếp cho SL — dùng số suy ngược từ RR platform là nguồn gốc của O1.

### (c) Bài học tâm lý-hành vi
- Nguy cơ đọc "TP1 hit + tổng thể vẫn dương" thành "lệnh này chứng minh CISD full-leg có edge" — trong khi phần đóng góp lớn nhất vào R thực tế (nếu tính đủ TP2) đã bị bỏ lại trên bàn do phản xạ chốt lời.
- `followed_plan: Partial` + giải thích "confluence_score không phản ánh đúng chất lượng" là một dạng tự biện minh hợp lý về logic nhưng cần cảnh giác nếu lặp lại có hệ thống ở nhiều note khác (grade inflation qua lý do miễn trừ).

### (d) Rule đề xuất cho Playbook
- [ ] Không đưa CISD full-leg reclaim thành "tiêu chuẩn ưu tiên" chính thức cho tới khi có ≥10 mẫu so sánh với CISD yếu và với MSS wick-based trên cùng điều kiện.
- [ ] Cấm dùng field "suy ngược từ X" để verify lại chính X trong bất kỳ báo cáo nào — luôn ghi rõ nguồn số liệu độc lập.
- [ ] Viết rule quản lý runner cố định (breakeven sau TP1; đóng phần còn lại chỉ khi chạm TP2 hoặc có tín hiệu cấu trúc cụ thể được định nghĩa trước) — áp dụng cho mọi lệnh có TP nhiều tầng.
- [ ] Gắn field `poi_tap_depth` (nông/sâu) chuẩn hóa toàn vault, đối chiếu với outcome qua ≥15 mẫu để xác định tap nông có thực sự là biến rủi ro hay không (thay vì chỉ note theo note).

### (e) Điều KHÔNG nên học từ lệnh này (chống overfitting/outcome bias)
- **Không nên** kết luận "CISD full-leg reclaim hoạt động đúng như kỳ vọng" là một quy luật đã kiểm chứng — đây vẫn là n=1, TP1 hit không tự động chứng minh công cụ xác nhận là chuẩn.
- **Không nên** dùng r_planned=2.47 trong frontmatter để tính expectancy tổng mà không sửa lại theo số verify (2.373) — nếu không sửa, mọi thống kê dashboard dựa trên field này sẽ lệch nhẹ một cách có hệ thống.
- **Không nên** coi việc giá "sau đó vẫn vượt TP2 5 ngày sau" là bằng chứng quyết định đóng runner sớm là sai — đây chính là hindsight note gốc đã tự cảnh báo đúng, giữ nguyên quan điểm đó.

---

### Liên kết bổ sung
- So sánh rule drift: [[01 - Win - GBPUSD - 2014-07-14 - Long]] *(lưu ý: file vật lý tên "2026-07-17/01 - Win - GBPUSD - 2014-06-25 - Long.md" nhưng `trade_date` thật trong frontmatter là 2014-07-14 — xem callout đầu mục 9 và mục 10 của note kia)* — hai lệnh Long GBPUSD khác ngày, cùng biến thể entry-tại-CE, đối chiếu chuẩn OTE/Discount khác nhau giữa hai bản.
- Đối chiếu tap nông: [[02 - Loss - GBPUSD - 2014-07-17 - Long]] (tap nông + MSS sớm → Loss) vs note này (tap nông + CISD full-leg → Win) — cùng biến "tap nông", hai outcome khác nhau, cần thêm mẫu để phân biệt.

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- Khái niệm: [[25 - OB - Order Block|Order Block]] · [[13 - FVG  - Fair Value Gap|FVG]] · [[03 - Balanced Price Range|BPR]] · [[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment]] · [[41 - Change in State of Delivery|CISD]] · [[21 - Market Structure Shift|MSS]] · [[20 - Liquidity Sweep|Liquidity Sweep]] · [[27 - Premium Discount|Premium Discount]] · [[12 - Dealing Range|Dealing Range]] · [[18 - Kill Zones|Kill Zones]]
- Dashboard: [[_Backtest Dashboard]]
- Template: [[Backtest template - POI & Step Decision (ICT 2022)]]
- Mistake liên quan: *(chưa có — xem đề xuất ở mục 7.2 nếu pattern đóng runner sớm lặp lại)*
