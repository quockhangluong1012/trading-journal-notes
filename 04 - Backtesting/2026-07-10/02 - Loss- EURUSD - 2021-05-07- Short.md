---
type: backtest
backtest_date: 2026-07-10
trade_date: 2021-05-07
symbol: EURUSD
position: Short
result: Loss
session: Asia
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: "Yes"
poi_type: Order Block
poi_rank: 2
poi_timeframe: H1
poi_location: Premium
poi_in_ote: "No"
ce_ote_overlap: "No"
poi_stack: OB+FVG
fvg_high:
fvg_low:
ce_price:
entry_type: CE
entry_precision: CE
limit_filled: "Yes"
fill_depth_pct:
missed_by:
step1_bias_ok: "Yes"
step2_draw_ok: "No"
step3_sweep_ok: "No"
step4_displacement_ok: "No"
step5_poi_ok: "Yes"
step6_entry_ok: "No"
step7_target_ok: NA
first_error_step: draw
missing_step: sweep
chained_fully: "No"
liquidity_swept: "Yes"
sweep_type: Internal
displacement: "Yes"
displacement_score: 1
mss: "Yes"
fvg_valid: "Yes"
confluence_score: 0
smt_confirm:
cisd_confirm:
in_macro_time: "No"
nwog_ndog_align:
sd_target_align:
idm_swept:
correlated_asset:
entry_price: 1.20805
stop_loss: 1.20931
take_profit: 1.20381
r_planned: 3.39
rr_if_ce:
rr_if_ote:
r_multiple: -1
risk_percent:
spread_cost:
r_net:
grade: C
followed_plan: "No"
confidence:
tags:
  - backtest
  - ICT2022
  - POI
---

# Backtest 2021-05-07 — EURUSD Short — POI & Step Decision

> [!info] Ghi chú chuyển đổi template (2026-07-17)
> Convert từ template backtest cũ sang **template POI & Step Decision**. Dữ liệu gốc (entry/SL/TP/result/lesson learned) giữ nguyên. Ba điểm cần lưu ý:
> 1. **Sửa lỗi ngày tháng tồn đọng đã tự phát hiện trong bản gốc**: tiêu đề/heading gốc ghi nhầm "2005-05-02" và bảng Summary ghi nhầm "2021-05-03", trong khi `trade_date` frontmatter và tên file đều là đúng **2021-05-07**. Bản convert này đồng bộ lại ngày ở mọi nơi theo đúng `trade_date`.
> 2. **Grade đang mâu thuẫn giữa frontmatter (C) và bảng Summary gốc (D)** — bản gốc tự flag việc này ở mục Data Integrity nhưng chưa chốt số nào đúng. Bản convert giữ nguyên `grade: C` từ frontmatter (vì đây là nguồn dashboard đọc), nhưng **đề xuất Khang xem lại**: với 3 GATE fail (sai Kill Zone, displacement yếu, chọn sai short-term draw on liquidity) + tự chấm 40% khớp mô hình, D hoặc thậm chí F có thể phản ánh đúng hơn C.
> 3. **Nhãn "Order Block 1" / "Order Block 2" trong bản gốc bị đảo ngược so với mức giá** (OB "1 - thấp hơn" nhưng số lại thấp hơn OB "2 - cao hơn" đúng theo tên, tuy vậy prose mô tả trình tự giá đi ngược lại thứ tự liệt kê). Bản convert dùng trực tiếp **mức giá** thay vì nhãn 1/2 để tránh nhầm lẫn thêm — entry 1.20805 rơi đúng vào vùng OB cao hơn (1.20884–1.20780), đây là POI convert dùng cho frontmatter.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | EURUSD                                                       |
| Model Variant             | Standard (D1/H4→H1→M5)                                       |
| Trade Date (dữ liệu)      | 2021-05-07 (đã sửa từ 2021-05-03/2005-05-02 ghi nhầm)        |
| Position                  | Short                                                        |
| Result                    | Loss                                                         |
| Session                   | Asia — **ngoài Kill Zone** (đây chính là root cause đã ghi) |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes                                                          |
| **POI Type**              | Order Block (H1, vùng 1.20884–1.20780)                       |
| POI Rank (8.1)            | 2 (OB+FVG)                                                   |
| POI Timeframe             | H1                                                           |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | draw *(xem mục 7.4 — sai lầm sâu hơn cả Kill Zone)*          |
| R Planned (gross)         | 3.39                                                         |
| R Net (sau spread)        | —                                                             |
| R Multiple (kết quả)      | -1                                                            |
| Confluence Score (0–8)    | 0                                                             |
| Grade                     | C (frontmatter) — bản gốc từng ghi D, xem ghi chú ở trên     |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** phía trên — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Khung D1 đang trong trend giảm
  - Hình thành các LH/LL
  - Sau đó có 1 nhịp Pullback lớn, tuy nhiên chưa phá được protected high -> chưa đổi bias, chỉ là pullback
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Dealing Range High = 1.23473
  - Sell-side liquidity: Giá đang hướng tới vùng
    - Swing low: 1.17149 (Swing low quan trọng)
    - Bullish Order Block: 1.16576 - 1.16197
    - EQL dưới OB: 1.16045

![[Pasted image 20260710114911.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: LH/LL
- **Dealing Range**: High 1.21058 · Low 1.19436
- **POI chính**:
  - Order Block: 1.20884 - 1.20780
  - Order Block: 1.20678 - 1.20611
- **Liquidity cần chờ sweep**: Các vùng Order Block và swing high trên gần Order Block

### Phân Tích (nguyên văn gốc):

- Giá tạo Order Block (30/04/2021) và Order Block (03/05/2021) bằng các nhịp đẩy giá mạnh (bearish displacement)
- Sau khi tạo đáy ngày 05/05/2021, giá retrace về vùng Order Block thấp hơn
- Giá quét qua cạnh trên của OB này và đóng nến lại bên trong (Liquidity Sweep)
- Tuy nhiên sau đó giá đóng nến và giữ bên trên OB này -> Tạo thành Breaker Block
- Cây nến phá OB đó là 1 nến Bullish displacement mạnh có tạo FVG khi phá lên
- Giá tiếp tục di chuyển về vùng OB cao hơn (1.20884–1.20780)
- Giá cũng quét lên và ra ngoài cạnh trên OB nhưng sau đó đóng trở lại vào bên trong (Liquidity Sweep)
- Sau đó xuất hiện các nến rejection
- Xuống khung M5 quan sát giá

![[Pasted image 20260710114842.png]]

---

## 2. POI Profile — điểm vào tôi đã chọn

- **POI Type đã dùng**: Order Block H1 (vùng 1.20884–1.20780, nơi entry thực tế 1.20805 rơi vào) → `poi_type: Order Block`
- **POI Rank (8.1)**: 2/5 (OB + FVG nhịp bật, chưa tới Breaker/iFVG/Unicorn) → `poi_rank: 2`
- **POI hình thành trên khung**: H1 → `poi_timeframe: H1`
- **POI nằm ở**: Premium — entry 1.20805 nằm trên equilibrium H1 (~1.20247, giữa Dealing Range 1.21058/1.19436), đúng phía cho Short → `poi_location: Premium`
- **POI stack**: OB + FVG M5 hình thành trong nhịp bật khỏi OB → `poi_stack: OB+FVG`
- **CE của FVG có trùng OTE không?**: Không — tự nhận "giá không nằm trong vùng OTE" → `ce_ote_overlap: No`, `poi_in_ote: No`
- **Bounds & CE**: không có số liệu FVG M5 cụ thể trong bản gốc → để trống `fvg_high`/`fvg_low`/`ce_price`

> [!warning] POI đúng loại nhưng KHÔNG đủ điều kiện để trade — xem mục 4 và 7.4
> Đây là trường hợp quan trọng cần phân biệt: **POI (Order Block, đúng Premium) không sai**, nhưng **thời điểm và bối cảnh sử dụng POI này lại sai** — vì short-term draw on liquidity lúc đó đang hướng lên (buy-side phía trên chưa bị lấy), và giao dịch diễn ra ngoài Kill Zone.

---

## 3. Entry Precision & Fill — vào cạnh hay CE, có khớp không?

- **Entry Type**: CE → `entry_type: CE` (checklist gốc đã tick mục 5 "Entry — limit trong FVG/OB (CE) trong Kill Zone")
- **Entry Precision**: CE → `entry_precision: CE`
- **Limit có được khớp không?**: Yes → `limit_filled: Yes`
- **Giá đi sâu bao nhiêu vào FVG?**: không có số liệu FVG M5 cụ thể → để trống `fill_depth_pct`
- **RR ghi lại**: `r_planned` = 3.39 (trên giấy — nhưng xem cảnh báo bên dưới về vì sao RR đẹp không cứu được lệnh này)

### M5 — Xác nhận và điểm vào lệnh (nguyên văn phân tích gốc)

- Sau khi quét cạnh trên OB khung H1, giá bật ngược lại bên trong
- Nhịp bật ra có các nến displacement (không quá lớn) + có FVG
- Nhịp displacement đồng thời tạo MSS
- Entry khi giá retrace về FVG M5
- Sau đó giá di chuyển xuống đúng kế hoạch về vùng OB thấp hơn
- Tuy nhiên khi vào lệnh tôi mới phát hiện mình vào sai Kill Zone (thời điểm vào lệnh là Asia — 10:05 UTC+7)
- Giá về quét OB thấp hơn và sau đó 1 nến bullish displacement rất mạnh hình thành và quét xuyên qua OB cao hơn và stop loss của tôi
- 1 nến displacement quét thẳng tới 1 OB trên cao nhất (1.21296 - 1.21227)
- Stop loss vì sai Kill Zone
- **Entry trigger**:
  - Liquidity Sweep: Quét qua cạnh trên + Swing high sát cạnh trên OB
  - MSS: Giá tạo MSS
  - Displacement: có displacement (nến không quá lớn)
  - FVG: Giá tạo FVG
- **Entry reason**: Giá hình thành Setup theo mô hình ICT 2022: Sweep → MSS + Displacement + FVG → retrace FVG → Entry (POI là OB H1). Tuy nhiên sai Kill Zone
- **Invalidation reason**: Giá đóng qua cạnh trên OB
- **Tôi có chờ đủ điều kiện không?** Không

---

## 4. 7-Step Decision Log — bước nào đúng, bước nào sai

| # | Bước | Đúng? (`Yes/No/NA`) | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | D1 Bearish, LH/LL, pullback chưa phá protected high |
| 2 | Draw on Liquidity | **No** | Short-term draw thực tế đang hướng **lên** (buy-side 1.21296–1.21227 chưa bị lấy) — chọn sai mục tiêu ngắn hạn dù bias dài hạn đúng. Xem mục 7.4 |
| 3 | Liquidity Sweep | **No** | Sweep quan sát được chỉ là **internal liquidity nông**, không phải external/buy-side thật — nhầm loại thanh khoản |
| 4 | Displacement + MSS | **No** | Tự nhận displacement "không quá lớn" 2 lần — dưới ngưỡng hợp lệ |
| 5 | POI (FVG/OB...) | Yes | OB đúng loại, đúng phía Premium |
| 6 | Entry (retrace) | No | Entry ngoài Kill Zone, không xác nhận giờ vào lệnh trước khi bấm |
| 7 | Target | NA | Dính stop trước khi tới target |

- **First Error Step**: `draw` — mắt xích gãy sớm nhất và sâu nhất, theo đúng phân tích mục 7.4 của chính bản ghi gốc: bias đúng nhưng **draw on liquidity ngắn hạn bị chọn sai hướng**, sớm hơn cả lỗi sweep/displacement/Kill Zone
- **Missing Step**: `sweep` (sweep hợp lệ — tức external raid vào đúng thanh khoản mục tiêu — chưa từng xảy ra trước khi entry)
- **Đủ chuỗi 7 bước?**: No

> [!danger] Vì sao `first_error_step = draw` chứ không phải `sweep` hay lỗi Kill Zone
> Bản ghi gốc (mục 5.4) tự nhận đây là bài học **quan trọng hơn cả lỗi Kill Zone**: ngay cả khi lệnh này rơi đúng London/NY KZ, nó vẫn là một **premature short** vì short-term draw on liquidity đang hướng lên. Lỗi Kill Zone (session) là một GATE riêng (`in_macro_time: No`), nhưng lỗi **draw** mới là mắt xích đầu tiên trong chuỗi 7 bước bị gãy.

---

## 5. Setup Quality & Confluence (GATE + SCORE)

**GATE (pass/fail):**

- [x] Bias HTF rõ + draw xác định *(chỉ đúng ở cấp HTF, sai ở cấp short-term — xem 7.4)*
- [ ] Liquidity sweep TRƯỚC displacement + reclaim — **FAIL**: chỉ là internal sweep nông, không phải external/buy-side thật
- [ ] Displacement hợp lệ — **FAIL**: "nến không quá lớn" (tự nhận 2 lần)
- [x] MSS hợp lệ (về mặt cấu trúc — dù trọng số thấp trong phiên Asia mỏng)
- [x] FVG/POI sạch + entry là retrace
- [x] Entry đúng Premium/Discount, đồng hướng bias
- [ ] Session/Kill Zone — **FAIL**: entry lúc 10:05 UTC+7 (phiên Asia), ngoài London/NY KZ

**GATE: FAIL ở 3 mục quan trọng (sweep thật, displacement, Kill Zone) → đúng ra phải là No Trade.**

**SCORE — mỗi confluence +1 (0–8):**

| # | Confluence | +1? | Ghi chú |
|---|---|---|---|
| 1 | POI hạng ≥3 | Không | Rank ước lượng 2 |
| 2 | CE∩OTE overlap | Không | Tự nhận không nằm trong OTE |
| 3 | SMT confirm | Không rõ | Không có dữ liệu gốc |
| 4 | CISD confirm | Không rõ | Không có dữ liệu gốc |
| 5 | In macro time | **Không (0)** | Xác nhận rõ: entry trong phiên Asia, ngoài Kill Zone |
| 6 | NWOG/NDOG align | Không rõ | Không có dữ liệu gốc |
| 7 | −2SD/ERL target | Không rõ | Không có dữ liệu gốc |
| 8 | IDM swept | Không rõ | Không có dữ liệu gốc |

- `confluence_score`: 0
- **Quy đổi điểm → hạng**: 0–1 = C (No Trade theo SCORE) — khớp với `grade: C` hiện có trong frontmatter, nhưng lưu ý mục 0 đã đề xuất xem lại vì mức độ vi phạm GATE khá nặng.

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: Stoploss
- **Tại sao lệnh thắng/thua?**
  - Setup đủ các điều kiện bề mặt tuy nhiên khi vào lệnh mới phát hiện sai Kill Zone. Setup đang nằm trong phiên Asia
- **POI đã chọn có phải lựa chọn tốt nhất không?**
  - Loại POI (Order Block H1, Premium) đúng, nhưng thời điểm dùng nó sai — chưa chờ buy-side phía trên bị quét.
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Có Displacement (nhưng yếu — tự nhận "không quá lớn")
  - Có MSS (nhưng trọng số thấp trong phiên mỏng)
  - FVG hợp lệ về hình thức, nhưng hình thành trong bối cảnh thanh khoản mỏng
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 40% (giá không nằm trong vùng OTE, và như phân tích sâu hơn ở mục 7.4, còn sai cả về draw on liquidity)
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - *(Bản gốc ghi "Cải thiện tâm lý giao dịch" — nhưng chính Lesson Learned bên dưới đã tự phản biện: đây là chẩn đoán SAI gốc rễ, xem mục 7.6)*

---

## 7. Lesson Learned

> [!summary] Root cause (1 câu)
> **Vào lệnh ngoài Kill Zone (Asia, 10:05 UTC+7).** ICT 2022 Model là mô hình *phụ thuộc Kill Zone*; bỏ qua điều kiện tiên quyết này biến một setup "đẹp" thành một lệnh không có edge. *(Nhưng xem mục 7.4 — có một lỗi còn sâu hơn cả điều này.)*

### 7.1. Bài học kỹ thuật

Setup được đọc rất tốt về mặt cấu trúc (bias → dealing range → sweep → breaker → displacement + FVG → MSS → retrace entry), nhưng **giá trị của ICT 2022 Model là *có điều kiện*** — nó chỉ có edge khi diễn ra trong London KZ / NY AM KZ, nơi dòng lệnh tổ chức tạo ra displacement *thật*. Trong phiên **Asia thanh khoản mỏng**, cái "sweep" và "displacement" mà tôi thấy phần lớn là chuyển động nội bộ (internal), dễ tạo cảm giác có setup nhưng không có lực đẩy institution phía sau. Đây là lý do lệnh thua — **không phải do tâm lý, mà do lỗi quy trình** (thiếu cổng kiểm tra Kill Zone trước lệnh).

**Triệu chứng (symptoms) — sinh ra từ root cause:**
- Chỉ **phát hiện sai Kill Zone SAU khi đã đặt lệnh** → checklist Kill Zone bị bỏ trống nhưng vẫn bấm lệnh (cổng kiểm tra không được đặt *trước* khi phân tích M5).
- **Displacement yếu** — chính tôi ghi chú "nến không quá lớn" tới 2 lần nhưng vẫn vào. Displacement yếu là dấu hiệu suy giảm của mô hình, đã bị hợp lý hóa.
- **Entry không nằm trong OTE / không kiểm tra Premium kỹ** cho leg bán (tự chấm 40% khớp mô hình).
- **SL đặt ngay trên OB gần** (trên điểm sweep OB) → trong phiên mỏng, cụm stop này trở thành *nam châm* cho một nhịp quét.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
- Cú "sweep" cạnh trên OB mà tôi coi là tín hiệu vào thực chất chỉ là **internal liquidity nông**. **Buy-side thật sự vẫn chưa bị lấy** — nó nằm ở OB cao hơn (1.21296–1.21227) phía trên.
- Draw on liquidity *ngắn hạn* đang hướng **LÊN** (đi lấy buy-side + cụm SL của phe short) chứ không phải xuống ngay. Sau khi nhử phe short vào, chỉ cần **một nến bullish displacement đơn lẻ** trong phiên mỏng là đủ để chạy xuyên OB + SL của tôi để với tới buy-side phía trên.
- Bài học cốt lõi: **một pattern "đủ điều kiện" trong sai bối cảnh (session/premium) KHÔNG phải là một setup hợp lệ.** Checklist thiếu đúng cái gate quan trọng nhất (Kill Zone) đáng lẽ phải là NO-TRADE, chứ không phải "gần đủ nên vào".

### 7.2. Pattern lặp lại (điều cần để ý lần sau)

- **"Đủ checklist pattern nhưng thiếu cổng quan trọng nhất" → vẫn vào.** Kill Zone bỏ trống mà vẫn bấm lệnh. Đây là lỗi kỷ luật quy trình, không phải lỗi đọc chart.
- **Hợp lý hóa tín hiệu yếu** (displacement "không quá lớn" nhưng vẫn coi là hợp lệ).
- **Quy loss cho "tâm lý"** ("Nếu vào lại: cải thiện tâm lý") — chẩn đoán sai gốc rễ. Gốc rễ là **rule/process** (Kill Zone gate + OTE + draw sai), không phải cảm xúc.

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] **HARD GATE — Kill Zone:** Không entry nếu không nằm trong **London KZ** hoặc **NY AM KZ**. Kiểm tra Kill Zone *TRƯỚC* khi xuống M5 phân tích entry, không phải sau khi đặt lệnh. Ngoài KZ = NO-TRADE tuyệt đối.
- [ ] **HARD GATE — OTE/Premium:** Với lệnh Short, POI phải nằm trong **premium** và lý tưởng chạm **OTE 62–79%** của leg/dealing range liên quan. Không đạt = bỏ.
- [ ] **Định nghĩa displacement khách quan:** range ≥ ngưỡng ATR đã định, phá cấu trúc nội bộ dứt khoát, để lại FVG rõ. **Displacement yếu = no trade.**
- [ ] **Sample hygiene:** Lệnh vào ngoài Kill Zone **KHÔNG được tính** vào thống kê edge của 2022 Model (win rate / expectancy). Tag `invalid-out-of-KZ` và loại khỏi cohort chính.
- [ ] **SL logic:** Xác định buy-side/OB lớn phía trên như *mục tiêu quét tiềm năng* trước khi vào; tránh đặt SL ngay sát một OB gần dễ bị nhử trong phiên mỏng.
- [ ] **Data integrity:** Đã đồng bộ `trade_date` (2021-05-07) ở mọi nơi trong file này.

> [!warning] Liên kết Mistake Database
> [[04 - Mistake - FOMO Entry]] (vào sớm trước khi buy-side bị dọn) · cân nhắc tạo thêm mục Mistake riêng cho "Vào lệnh sai Kill Zone" và "Hợp lý hóa displacement yếu" nếu hai lỗi này lặp lại ở các backtest khác.

### 7.4. Sai lầm SÂU hơn cả Kill Zone: nhầm giữa HTF bias và short-term draw on liquidity

> [!danger] Đây là bài học quan trọng nhất, quan trọng hơn cả lỗi Kill Zone
> Ngay cả khi lệnh này rơi vào **London/NY KZ**, nó vẫn là một lệnh **premature short** — vì short-term draw on liquidity lúc đó đang hướng **LÊN**, không phải xuống.

HTF bias **Bearish là đúng** (đã được xác nhận: kết cấu D1 giảm, LH/LL, pullback chưa phá protected high). Nhưng **"bias đúng" và "thời điểm entry đúng" là hai chuyện hoàn toàn khác nhau** — và đây chính là cái bẫy nhận thức đã khiến lệnh này thua kể cả về mặt logic ICT, không chỉ vì session.

Cơ chế thực tế: phía trên entry còn một cụm **buy-side liquidity chưa bị lấy** — cạnh trên OB cao nhất `1.21296–1.21227` và cụm stop của phe short (trong đó có SL của chính tôi tại `1.20931`). Trong ICT, giá **đi tìm liquidity chưa bị chạm** trước khi đảo chiều theo bias lớn. Khi buy-side phía trên còn nguyên, kịch bản xác suất cao nhất trong ngắn hạn là:

> giá **nhử phe short vào** (tạo cảm giác có sweep + MSS trên M5) → **chạy ngược lên lấy buy-side + quét cụm SL** → *sau đó* mới quay đầu theo bias giảm.

Cú "sweep cạnh trên OB" mà tôi coi là tín hiệu entry chỉ là **internal liquidity nông** — không phải là *raid* buy-side thật. Đây là lỗi kinh điển: **đọc đúng hướng dài hạn nhưng đứng sai phía của liquidity gần nhất.** Short đúng bias nhưng vào *trước khi* buy-side trên bị dọn = tự đặt lệnh vào đúng đường đạn của lần quét kế tiếp.

**Quy tắc rút ra:** Trước mỗi entry, hỏi một câu bắt buộc — *"Liquidity chưa-bị-lấy gần nhất nằm ở phía nào so với entry của tôi?"* Nếu nó nằm **cùng phía với SL** (tức giá còn lý do để chạy vào SL trước), thì đó là **NO-TRADE hoặc phải chờ nó bị quét xong**, bất kể pattern đẹp đến đâu.

### 7.5. Những điều "tưởng đúng nhưng lại sai" (cognitive traps)

- **"Bias correct = Yes → nên short"**: Bias đúng chỉ trả lời *hướng cuối cùng*, không trả lời *điểm & thời điểm vào*. Đây là ngộ nhận gốc, đã phân tích ở 7.4.
- **"Có Liquidity Sweep → có tín hiệu"**: Nhầm **internal liquidity nông** thành **external/buy-side thật**. Không phải cứ quét-rồi-đóng-lại là một raid hợp lệ. Phải phân loại: sweep này lấy *loại* thanh khoản nào, và *thanh khoản mục tiêu lớn hơn* đã bị lấy chưa.
- **"Có MSS trên M5 → xác nhận đảo chiều"**: Một MSS trên M5 trong **phiên Asia mỏng** có **trọng số rất thấp** — dễ bị tạo ra bởi vài lệnh nhỏ và bị phủ định ngay sau đó. MSS chỉ có giá trị khi đi kèm displacement thật của dòng lệnh tổ chức (tức trong KZ).
- **"R planned 3.39 → lệnh đáng vào"**: RR đẹp là *ảo giác an toàn*. RR chỉ có ý nghĩa khi **xác suất chạm TP trước SL** đủ cao; ở đây SL nằm ngay dưới một buy-side chưa bị lấy → xác suất chạm SL trước bị đội lên rất mạnh, làm RR 3.39 trên giấy trở nên vô nghĩa. **RR không bao giờ được dùng để bù cho một entry sai bối cảnh.**
- **Checklist Section "Entry Sequence" đánh dấu đủ 7 mục** trong khi thực tế KHÔNG ở Kill Zone → checklist bị tick "cho đủ" chứ không phản ánh sự thật. Setup Quality Checklist đã trung thực để trống ô Kill Zone — **hai mục đang mâu thuẫn nhau trong cùng file.** Bài học meta: *checklist chỉ có giá trị nếu được tick trung thực; một ô tick sai còn nguy hiểm hơn không có checklist* vì nó tạo cảm giác đã kiểm tra.

### 7.6. Cổng vào lệnh (pre-trade gate) — áp dụng ngay từ lệnh backtest tiếp theo

1. **Session gate**: Đang trong London KZ hay NY AM KZ? → Nếu KHÔNG: **NO-TRADE**, dừng, không xuống M5. *(Đặt gate này TRƯỚC khi phân tích entry, không phải sau.)*
2. **Draw gate**: Liquidity chưa-bị-lấy gần nhất nằm phía nào? → Nếu cùng phía SL: **chờ nó bị quét xong** rồi mới tìm entry ngược lại.
3. **Location gate**: POI có nằm trong **Premium (cho Short)** và lý tưởng chạm **OTE 62–79%** không? → Nếu KHÔNG: bỏ.
4. **Signal-quality gate**: Displacement có đạt ngưỡng ATR khách quan + để lại FVG rõ không? → "Nến không quá lớn" = **displacement yếu = NO-TRADE.**
5. Chỉ khi **cả 4 gate = PASS** mới được đặt lệnh.

> [!note] Sample hygiene — bắt buộc để backtest có giá trị thống kê
> Lệnh này vào **ngoài Kill Zone** ⇒ **KHÔNG được tính** vào cohort chính đo edge của ICT 2022 Model (win rate / expectancy). Gắn tag `invalid-out-of-KZ` và loại khỏi mẫu chính.

> [!tip] Chẩn đoán lại root cause — sửa dòng "cải thiện tâm lý"
> Ô "Nếu được vào lại, tôi sẽ làm gì khác? → Cải thiện tâm lý" là **chẩn đoán sai gốc rễ.** Không có lỗi tâm lý nào ở đây cả — có một lỗi **quy trình** (thiếu 4 gate ở trên) và một lỗi **nhận thức** (nhầm bias với draw). Đổ cho tâm lý là cách nhanh nhất để *không sửa được gì*. **Sửa lại thành: "Thêm 4-gate pre-trade checklist và bắt buộc PASS cả 4 trước khi đặt lệnh."**

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 5/10 (HTF bias đúng nhưng short-term draw chọn sai — xem 7.4) |
| POI Selection (đúng loại + hạng + P/D) | 6/10 |
| Liquidity Sweep | 3/10 (chỉ internal, không phải external thật) |
| Displacement / MSS quality | 3/10 (tự nhận "không quá lớn") |
| Entry Precision & Fill (Edge/CE/OTE) | 4/10 (khớp CE nhưng ngoài Kill Zone) |
| Risk Management (R net, RR) | 3/10 (SL đặt sát nam châm thanh khoản) |

**Overall Grade**: C (frontmatter) — xem đề xuất xem lại ở đầu file

> [!tip] Chống curve-fitting
> Trigger nhìn có vẻ đủ điều kiện nhưng KHÔNG nhận diện được đúng bối cảnh (session + draw ngắn hạn) **trước khi** vào lệnh — đây là bằng chứng cho thấy checklist hiện tại còn thiếu gate, không phải bằng chứng cho một setup hợp lệ. Loại mẫu này khỏi cohort chính đo edge.

---

## 9. Phân tích bổ sung chuyên sâu (2026-07-18)

> [!info] Mục 7.4–7.6 đã phân tích rất sâu tầng "draw vs bias" và cognitive traps. Mục này bổ sung tầng còn thiếu: **đối chiếu từng khái niệm ICT bị áp dụng sai**, lăng kính **AMD/Power of Three** cho lỗi phiên Asia, và vị trí của lệnh này trong **pattern chung của 4 lệnh thua**.

### 9.1. Các khái niệm ICT bị áp dụng SAI

| Khái niệm | Tôi đã dùng như thế nào (SAI) | Cách dùng ĐÚNG | Ảnh hưởng |
|---|---|---|---|
| [[18 - Kill Zones]] | Dùng như một ô confluence để tick SAU khi đã phân tích entry (và phát hiện sai sau khi đặt lệnh) | Kill Zone là **PRECONDITION cấp cổng** của 2022 Model — kiểm tra TRƯỚC khi mở khung M5. Ngoài KZ, displacement/MSS mất luôn ý nghĩa thống kê vì thiếu dòng lệnh tổ chức | Chí mạng (GATE) |
| [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] | Dùng một nửa khái niệm: xác định draw dài hạn (SSL dưới) theo HTF bias, bỏ qua draw NGẮN HẠN đang hướng lên (BSL 1.21296–1.21227 chưa lấy) | Draw phải được xác định ở **cả 2 cấp**; khi draw ngắn hạn ngược bias dài hạn → chờ pool gần bị quét xong rồi mới tìm entry theo bias | Chí mạng — first_error |
| [[16 - Internal & External Range Liquidity (IRL & ERL)]] + [[07 - Buy-side Liquidity]] | Nhầm cú quét cạnh trên OB (internal, nông) thành một raid buy-side thật | Phân loại pool trước khi đếm sweep: sweep hợp lệ cho Short = **external/structural BSL** bị lấy (ở đây là cụm OB 1.21296–1.21227 + swing high liên quan), không phải mọi cú "quét-rồi-đóng-lại" | Chí mạng |
| [[20 - Liquidity Sweep]] | Đếm sweep theo hình dạng nến (wick qua mép OB) thay vì theo **chức năng** (pool nào bị lấy, còn pool nào chưa) | Câu hỏi đúng không phải "có sweep chưa?" mà là "sweep này lấy LOẠI thanh khoản nào, và pool mục tiêu lớn hơn đã bị lấy chưa?" | Nặng |
| [[21 - Market Structure Shift]] | Tin MSS M5 hình thành trong phiên Asia mỏng | Trọng số của MSS tỷ lệ thuận với **lực lượng tham gia tạo ra nó**. MSS trong phiên mỏng có thể bị tạo bởi vài lệnh nhỏ và phủ định ngay khi London mở — chỉ đếm MSS trong KZ | Nặng |
| [[02 - AMD]] (Power of Three) | Không áp dụng: short lúc 10:05 UTC+7 — tức giữa pha **Accumulation** của ngày | Theo AMD, phiên Asia thường là pha A (tích lũy quanh open); nhịp chạy lên quét SL sau đó chính là pha **M (Manipulation / Judas swing)** kinh điển trước khi Distribution theo bias thật. Short trong pha A = tự đặt mình vào đúng hướng của Judas swing sắp tới | Nặng |
| [[26 - OTE - Optimal Trade Entry]] | Tự nhận "không nằm trong OTE" nhưng vẫn vào | Không đạt location gate = bỏ, không có ngoại lệ vì "các yếu tố khác đẹp" | Nặng |
| Displacement ([[08 - Mistake - Weak Displacement]]) | Ghi chú "nến không quá lớn" tới 2 lần nhưng vẫn tick hợp lệ | Displacement là biến định lượng (body-to-range, ATR, có FVG) — không phải cảm giác. Tự ghi "không quá lớn" = đã biết nó fail, hợp lý hóa là lỗi kỷ luật | Nặng |

**Điểm đáng chú ý nhất của bảng này:** lệnh chỉ có MỘT bước tick Yes thật sự (POI đúng loại đúng phía) — mọi khái niệm còn lại đều bị dùng sai hoặc dùng một nửa. Điều đó nhất quán với confluence_score 0/8 và tự chấm 40% khớp mô hình: đây không phải một setup "gần đủ", đây là một **non-setup được các pattern bề mặt ngụy trang**.

### 9.2. Đào sâu: cơ chế phiên Asia + vì sao chỉ cần MỘT nến để giết lệnh

Trong phiên mỏng, order book hai bên đều nông. Điều đó tạo ra hai hệ quả ngược nhau mà lệnh này dính cả hai: (1) **tín hiệu giả rẻ** — chỉ cần khối lượng nhỏ đã in được "sweep + MSS + displacement" đủ đẹp trên M5 để dụ entry; (2) **quét thật cũng rẻ** — khi thuật toán muốn chạy lên lấy BSL 1.21296–1.21227, một nến bullish displacement đơn lẻ là đủ xuyên OB + SL mà không gặp kháng cự, vì không có tầng lệnh dày nào hấp thụ giữa đường. Nói cách khác, phiên Asia **khuếch đại cả mồi lẫn bẫy**. Đây là lý do sâu hơn của HARD GATE Kill Zone: không phải "Asia xấu" một cách mê tín, mà là cấu trúc thanh khoản mỏng làm cho mọi bằng chứng kỹ thuật của 2022 Model mất giá trị xác nhận.

### 9.3. Vị trí trong pattern chung 4 lệnh thua (họ lỗi "Unswept Liquidity Path")

| Lệnh | First error | Pool chưa-bị-lấy gần nhất so với entry | SL nằm trong đường lấy pool đó? |
|---|---|---|---|
| **EURUSD 2021-05-07 Short (file này)** | draw | BSL external = OB 1.21296–1.21227, phía TRÊN | **Có** (SL 1.20931) |
| [[02 - Loss - GBPUSD - 2014-07-17 - Long]] | sweep | ERL = range low 1.70592, phía DƯỚI | **Có** |
| [[01 - Loss - XAUUSD - 2014-05-19 - Short]] | poi | OB 0.786 chưa test, phía TRÊN BB | **Có** |
| [[02 - Loss- XAUUSD- 2014-05-14- Short]] | poi (SL) | Phần thân còn lại của chính RB, phía TRÊN | **Có** |

4/4 lệnh thua cùng một gốc: **entry được đặt khi pool thanh khoản chưa-bị-lấy gần nhất nằm cùng phía với SL**. File này là phiên bản "external BSL", và cũng là phiên bản duy nhất cộng thêm lỗi session. Note tổng hợp + gate kiểm tra bắt buộc trước mọi lệnh: [[13 - Mistake - Trading Into Unswept Liquidity]].

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[25 - OB - Order Block]] · [[13 - FVG  - Fair Value Gap]] · [[04 - Breaker Block]]
- Entry refine: [[10 - Consequent Encroachment (Mean Threshold)]] · [[27 - Premium Discount]]
- Bước: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[18 - Kill Zones]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[04 - Mistake - FOMO Entry]] · [[12 - Mistake - Log Data Mismatch - Backtest]] · [[08 - Mistake - Weak Displacement]] · [[13 - Mistake - Trading Into Unswept Liquidity]]
