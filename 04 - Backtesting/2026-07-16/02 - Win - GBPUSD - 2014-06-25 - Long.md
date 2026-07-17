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

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- Khái niệm: [[25 - OB - Order Block|Order Block]] · [[13 - FVG  - Fair Value Gap|FVG]] · [[03 - Balanced Price Range|BPR]] · [[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment]] · [[41 - Change in State of Delivery|CISD]] · [[21 - Market Structure Shift|MSS]] · [[20 - Liquidity Sweep|Liquidity Sweep]] · [[27 - Premium Discount|Premium Discount]] · [[12 - Dealing Range|Dealing Range]] · [[18 - Kill Zones|Kill Zones]]
- Dashboard: [[_Backtest Dashboard]]
- Template: [[Backtest template - POI & Step Decision (ICT 2022)]]
- Mistake liên quan: *(chưa có — xem đề xuất ở mục 7.2 nếu pattern đóng runner sớm lặp lại)*
