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
> 2. **Grade đang mâu thuẫn giữa frontmatter (C) và bảng Summary gốc (D)** — bản gốc tự flag việc này ở mục Data Integrity nhưng chưa chốt số nào đúng. Bản convert giữ nguyên `grade: C` từ frontmatter (vì đây là nguồn dashboard đọc), nhưng **đề xuất  xem lại**: với 3 GATE fail (sai Kill Zone, displacement yếu, chọn sai short-term draw on liquidity) + tự chấm 40% khớp mô hình, D hoặc thậm chí F có thể phản ánh đúng hơn C.
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
> [[04-Mistake-FOMO-Entry]] (vào sớm trước khi buy-side bị dọn) · cân nhắc tạo thêm mục Mistake riêng cho "Vào lệnh sai Kill Zone" và "Hợp lý hóa displacement yếu" nếu hai lỗi này lặp lại ở các backtest khác.

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
| [[18-Kill-Zones]] | Dùng như một ô confluence để tick SAU khi đã phân tích entry (và phát hiện sai sau khi đặt lệnh) | Kill Zone là **PRECONDITION cấp cổng** của 2022 Model — kiểm tra TRƯỚC khi mở khung M5. Ngoài KZ, displacement/MSS mất luôn ý nghĩa thống kê vì thiếu dòng lệnh tổ chức | Chí mạng (GATE) |
| [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung]] | Dùng một nửa khái niệm: xác định draw dài hạn (SSL dưới) theo HTF bias, bỏ qua draw NGẮN HẠN đang hướng lên (BSL 1.21296–1.21227 chưa lấy) | Draw phải được xác định ở **cả 2 cấp**; khi draw ngắn hạn ngược bias dài hạn → chờ pool gần bị quét xong rồi mới tìm entry theo bias | Chí mạng — first_error |
| [[16-Internal-External-Range-Liquidity-IRL-ERL]] + [[07-Buy-side-Liquidity]] | Nhầm cú quét cạnh trên OB (internal, nông) thành một raid buy-side thật | Phân loại pool trước khi đếm sweep: sweep hợp lệ cho Short = **external/structural BSL** bị lấy (ở đây là cụm OB 1.21296–1.21227 + swing high liên quan), không phải mọi cú "quét-rồi-đóng-lại" | Chí mạng |
| [[20-Liquidity-Sweep]] | Đếm sweep theo hình dạng nến (wick qua mép OB) thay vì theo **chức năng** (pool nào bị lấy, còn pool nào chưa) | Câu hỏi đúng không phải "có sweep chưa?" mà là "sweep này lấy LOẠI thanh khoản nào, và pool mục tiêu lớn hơn đã bị lấy chưa?" | Nặng |
| [[21-Market-Structure-Shift]] | Tin MSS M5 hình thành trong phiên Asia mỏng | Trọng số của MSS tỷ lệ thuận với **lực lượng tham gia tạo ra nó**. MSS trong phiên mỏng có thể bị tạo bởi vài lệnh nhỏ và phủ định ngay khi London mở — chỉ đếm MSS trong KZ | Nặng |
| [[02-AMD]] (Power of Three) | Không áp dụng: short lúc 10:05 UTC+7 — tức giữa pha **Accumulation** của ngày | Theo AMD, phiên Asia thường là pha A (tích lũy quanh open); nhịp chạy lên quét SL sau đó chính là pha **M (Manipulation / Judas swing)** kinh điển trước khi Distribution theo bias thật. Short trong pha A = tự đặt mình vào đúng hướng của Judas swing sắp tới | Nặng |
| [[26-OTE-Optimal-Trade-Entry]] | Tự nhận "không nằm trong OTE" nhưng vẫn vào | Không đạt location gate = bỏ, không có ngoại lệ vì "các yếu tố khác đẹp" | Nặng |
| Displacement ([[08-Mistake-Weak-Displacement]]) | Ghi chú "nến không quá lớn" tới 2 lần nhưng vẫn tick hợp lệ | Displacement là biến định lượng (body-to-range, ATR, có FVG) — không phải cảm giác. Tự ghi "không quá lớn" = đã biết nó fail, hợp lý hóa là lỗi kỷ luật | Nặng |

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

4/4 lệnh thua cùng một gốc: **entry được đặt khi pool thanh khoản chưa-bị-lấy gần nhất nằm cùng phía với SL**. File này là phiên bản "external BSL", và cũng là phiên bản duy nhất cộng thêm lỗi session. Note tổng hợp + gate kiểm tra bắt buộc trước mọi lệnh: [[13-Mistake-Trading-Into-Unswept-Liquidity]].

---

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

![[EURUSD-20210507-draw-vs-bias.svg|760]]

```yaml
mode: REVIEW
instrument: EURUSD
date: 2021-05-07
timeframes_provided: "D1/H4, H1, M5 — 2 ảnh PNG không đọc được + tường thuật rất chi tiết đã có ở mục 7.4/9.1"
verdict: BROKEN
evidence_sufficiency: partial
opposite_case_strength: not viable
objections: {fatal: 2, material: 1, minor: 1}
```

> [!info] Không lặp lại nội dung mục 9 — mục này chỉ thêm lớp đối kháng mới: kiểm claim gốc bằng cách cố phá nó, không mô tả lại pattern 4 lệnh hay bảng khái niệm sai đã có sẵn.

**0. Evidence base.** Tường thuật rất chi tiết (mục 1, 3, 7.4-7.6, 9.1-9.3) + frontmatter đầy đủ. 2 PNG không đọc được nội dung hình ảnh. Vì tường thuật đã tự phân tích sâu và nhất quán nội bộ, evidence cho load-bearing claim (draw ngắn hạn sai hướng) là **partial** — đủ để đánh giá logic, không đủ để xác nhận độc lập hình dạng nến/sweep trên chart.

**1. Thesis + load-bearing claim.**
- C1: D1 bias Bearish đúng (LH/LL, pullback chưa phá protected high).
- C2: H1 có 2 Order Block đúng phía Premium, entry rơi vào OB cao hơn (1.20884-1.20780).
- C3: Sweep quan sát được (cạnh trên OB) chỉ là internal liquidity nông, không phải external BSL thật.
- C4 **(load-bearing)**: Short-term draw on liquidity tại thời điểm entry đang hướng LÊN (BSL 1.21296-1.21227 chưa bị lấy), ngược với hướng lệnh Short — đây là first_error thực sự, sâu hơn cả lỗi Kill Zone.
- C5: Entry ngoài Kill Zone (Asia, 10:05 UTC+7) — lỗi GATE độc lập, cộng dồn.
- C6: SL 1.20931 nằm trong đường đi tới BSL chưa quét — đây là "nam châm thanh khoản" theo chính note.
- C7: Kết quả Loss, đúng theo dự đoán từ C4+C6.

Load-bearing: **C4** — toàn bộ khung "Unswept Liquidity Path" (mục 9.3) và cả bài học chính (mục 7.4) phụ thuộc vào việc draw ngắn hạn thực sự hướng lên tại thời điểm entry, không phải hindsight dựng lại sau khi thấy giá chạy lên.

**2. What survives.** C1, C2, C5 không tranh chấp — bias D1, vị trí OB, và vi phạm Kill Zone (giờ cụ thể 10:05 UTC+7) đều là fact có thể kiểm tra khách quan (giờ) hoặc nhất quán nội bộ. C7 là outcome đã biết.

**3. Objections**

**O1 · [HINDSIGHT] · fatal · attacks C4 (load-bearing)**
Claim: "Draw on liquidity ngắn hạn lúc đó đang hướng LÊN" và toàn bộ khung "giá nhử phe short vào → chạy ngược lên lấy buy-side + quét SL → sau đó mới quay đầu theo bias giảm" (mục 7.4).
Fails: đây chính xác là mô tả những gì ĐÃ XẢY RA (giá quét SL, chạy lên OB 1.21296-1.21227) được viết lại thành "điều lẽ ra phải nhận ra trước". Note không trích dẫn được bất kỳ dấu hiệu nào tồn tại TRƯỚC entry (10:05 UTC+7) — ví dụ một swing high chưa bị test cụ thể được nhìn thấy trên chart tại thời điểm đó — mà chỉ suy ngược từ việc SL sau đó bị quét.
Evidence: mục 7.4 dùng chính từ "kịch bản xác suất cao nhất" ở thì tương lai giả định, nhưng luận cứ duy nhất được đưa ra để chứng minh nó "cao xác suất" là... nó đã xảy ra. Không có mốc giá cụ thể nào được nêu là "tại 10:05 UTC+7, tôi thấy OB 1.21296-1.21227 chưa bị test và đó là lý do tôi phải dự đoán giá sẽ chạy lên trước" — con số OB đó chỉ xuất hiện trong mục Draw on Liquidity D1/H4 (mục 1, cấp HTF dài hạn: "Buy-side liquidity: Dealing Range High = 1.23473"), KHÔNG phải trong phần short-term draw tại M5/H1 lúc entry.
Consequence: nếu draw-ngắn-hạn-hướng-lên chỉ được xác lập SAU khi thấy kết quả, thì "first_error_step: draw" là một chẩn đoán hindsight — nguyên nhân thật của Loss có thể đơn giản là lỗi Kill Zone (C5, đã biết TRƯỚC vì có giờ cụ thể) cộng với volatility ngẫu nhiên của phiên mỏng, không phải một lỗi "đọc sai draw" có thể phòng tránh bằng quan sát tại thời điểm đó.
Your best answer: "OB 1.21296-1.21227 là một cấu trúc H1/H4 đã tồn tại từ trước, không phải bịa ra sau" — đúng, nhưng việc một OB *tồn tại* trên chart không chứng minh rằng nó là "draw ngắn hạn ưu tiên" tại thời điểm entry; cần một tiêu chí độc lập với outcome để xác định OB đó có "ưu tiên hơn" SSL phía dưới target hay không TẠI THỜI ĐIỂM 10:05 UTC+7 — note không cung cấp tiêu chí đó, chỉ cung cấp kết quả.
Retracted by: nếu note trích được ghi chú TRƯỚC entry (không phải viết lại sau) nêu rõ OB 1.21296-1.21227 là "chưa test, cần chờ" ĐƯỢC XÁC ĐỊNH TRƯỚC KHI BẤM LỆNH — nhưng theo chính 7-Step Log (mục 4), bước 2 "Draw on Liquidity" được đánh dấu **No** chỉ trong bản ghi backtest, không có bằng chứng đây là nhận thức tại real-time.

**O2 · [METHOD] · fatal · attacks toàn bộ khung "Unswept Liquidity Path" (mục 9.3, không lặp lại nội dung, chỉ tấn công phương pháp)**
Claim ngầm: 4/4 lệnh thua trong bảng mục 9.3 chia sẻ cùng gốc "pool chưa-bị-lấy gần nhất nằm cùng phía SL" → đây là một pattern có giá trị dự báo.
Fails: đây là "Texas sharpshooter" cổ điển — bảng chỉ liệt kê **các lệnh ĐÃ THUA** rồi tìm điểm chung sau đó (mọi lệnh thua đều có SL bị quét, và SL-bị-quét-tức-là-đường-tới-1-pool-nào-đó gần như luôn đúng theo định nghĩa, vì thị trường luôn có pool ở đâu đó gần SL). Không có nhóm đối chứng: bao nhiêu lệnh THẮNG cũng có "pool chưa-bị-lấy nằm cùng phía SL" nhưng giá không chạy tới đó trước khi đảo chiều theo bias? Nếu tỷ lệ đó cũng cao ở nhóm Win, "Unswept Liquidity Path" không phải yếu tố phân biệt, chỉ là mô tả hậu-nghiệm của mọi lệnh thua vì SL kề bên.
Evidence: bảng mục 9.3 chỉ có 4 dòng, toàn bộ đều là Loss — không có cột "n lệnh Win cũng có pool cùng phía SL nhưng không bị quét".
Consequence: nếu đây là selection bias, thì rule đề xuất ở mục 7.4/7.6 ("hỏi liquidity chưa-bị-lấy gần nhất nằm phía nào") có thể đúng về mặt logic ICT (đáng làm) nhưng **chưa được validate bằng dữ liệu này** — dữ liệu này chỉ mô tả lại 4 lần thua, không chứng minh rule sẽ ngăn được thua lần sau mà không đồng thời ngăn cả các lệnh sẽ thắng.
Your best answer: rule "draw gate" trong ICT canon là một nguyên tắc độc lập (SKILL.md § Liquidity/Target — "mô tả draw on liquidity, không phải khuyến nghị trade") có thể đúng theo doctrine mà không cần bằng chứng thống kê từ 4 case này — nhưng note trình bày bảng 9.3 NHƯ MỘT BẰNG CHỨNG THỰC NGHIỆM ("4/4 lệnh thua cùng một gốc"), đó là điểm bị FAIL ở đây: dùng ngôn ngữ thống kê cho một mẫu không có nhóm đối chứng.
Retracted by: kiểm tra lại toàn bộ lệnh Win trong vault, đếm bao nhiêu % cũng có pool cùng phía SL — nếu tỷ lệ đó thấp hơn đáng kể so với nhóm Loss, pattern được validate và objection retract.

**O3 · [ARITHMETIC] · material · attacks C_RR (risk management)**
Claim: `r_planned: 3.39`.
Fails một phần: risk = |1.20931-1.20805| = 0.00126, reward = |1.20805-1.20381| = 0.00424 → RR = 3.365, gần khớp 3.39 (chênh 0.025R, nhỏ, trong ngưỡng làm tròn) — **không phải discrepancy đáng kể** như ở note 07-10/01 (chênh gần 1R). Ghi nhận ở đây để đối chiếu cấp portfolio: RR ghi trong log này đáng tin cậy hơn.
Evidence: tính trực tiếp từ 3 số frontmatter.
Consequence: không đổi kết luận nào — chỉ củng cố nhận định "RR 3.39 trên giấy không cứu được lệnh" (đã có ở mục 7.5) bằng số chính xác hơn thay vì số làm tròn.
Retracted by: không cần — đây gần như PASS, ghi mức material chỉ vì chênh lệch (dù nhỏ) chưa được chính note xác nhận bằng phép tính tường minh.

**O4 · [UNSUPPORTED] · minor** — `sweep_type: Internal` được gán nhãn nhưng không có mô tả định lượng (bao nhiêu pip vượt ra ngoài OB, độ dài bấc) để phân biệt khách quan Internal vs External — dựa hoàn toàn vào diễn giải tường thuật. Không phải sai, nhưng thiếu evidence bar theo SKILL.md § Sweep ("named level được dùng"). Retracted by: bổ sung số liệu cụ thể (giá cao nhất bấc, thời gian giữ).

Đã soạn 4, cắt 0 — O1 và O2 đều fatal vì tấn công đúng 2 trụ cột khác nhau của load-bearing claim (O1: bản thân C4 là hindsight; O2: bằng chứng hỗ trợ C4 ở cấp portfolio là selection bias).

**4. Opposite case.** Từ cùng evidence: "Nguyên nhân Loss duy nhất có thể XÁC NHẬN TẠI THỜI ĐIỂM ĐÓ (không cần hindsight) là lỗi Kill Zone (C5) — một GATE khách quan đo bằng đồng hồ, không cần diễn giải. Khung 'draw sai hướng' tuy hấp dẫn về mặt tường thuật nhưng là một lớp diễn giải được xây dựng SAU khi biết kết quả, và khi tổng quát hóa thành pattern 4 lệnh (mục 9.3) mắc lỗi thiếu nhóm đối chứng."
- Load-bearing của case ngược: "chỉ có 1 lỗi thật sự xác nhận được trước outcome — Kill Zone; 'draw' là chẩn đoán hậu nghiệm."
- Tự phản bác: draw on liquidity là một khái niệm ICT canon hợp lệ độc lập với outcome (SKILL.md § Liquidity/Target) — về mặt doctrine, hỏi "pool chưa lấy nằm phía nào" là câu hỏi ĐÚNG phải hỏi trước mọi lệnh, bất kể case này có chứng minh được bằng thống kê hay không. Nói cách khác: **rule thì đúng** (theo canon), nhưng **bằng chứng cho rule trong chính note này** (bảng 9.3) là yếu.
- Strength label: **not viable** để BÁC BỎ HOÀN TOÀN draw gate như một nguyên tắc — nhưng **viable** để bác bỏ cách note trình bày bảng 9.3 như "bằng chứng thực nghiệm 4/4".
- Distinguishing observable: nếu tìm được ghi chú thời gian-thực (không phải hồi tưởng) từ trước 10:05 UTC+7 xác nhận nhận thức "BSL trên chưa test" tại đúng thời điểm — case gốc thắng hoàn toàn về phần hindsight. Nếu kiểm tra nhóm Win cũng có tỷ lệ cao "pool cùng phía SL nhưng giá không chạy tới" — case ngược thắng phần selection bias.

**5. Verdict: BROKEN.**
Load-bearing claim C4, khi đọc như "đã được nhận biết TẠI THỜI ĐIỂM entry", không có evidence độc lập với outcome để đứng vững (O1). Bằng chứng hỗ trợ nó ở cấp portfolio (mục 9.3) mắc lỗi phương pháp thiếu nhóm đối chứng (O2). Điều không phá được: bias D1, vị trí OB, và vi phạm Kill Zone (C1, C2, C5) — đây là fact khách quan, không phụ thuộc diễn giải. Điều critique này không xác lập: liệu "draw sai hướng" có thực sự là nguyên nhân độc lập với Kill Zone hay chỉ là cùng một hiện tượng (thanh khoản mỏng phiên Asia) được mô tả hai lần dưới hai tên khác nhau.

**6. Falsification tests (tối đa 3)**
1. Tìm bất kỳ ghi chú/ảnh chụp thời gian-thực nào (trước 10:05 UTC+7) xác nhận nhận thức về BSL 1.21296-1.21227 tại đúng thời điểm — nếu có, đóng O1 theo hướng thắng cho note gốc.
2. Chạy thống kê toàn vault: % lệnh Win có "pool named cùng phía SL nhưng chưa bị quét tại entry" so với % lệnh Loss cùng điều kiện — nếu chênh lệch rõ rệt (vd Loss cao hơn hẳn), đóng O2, pattern 9.3 được validate.
3. Tách biệt 2 giả thuyết bằng cách tìm case tương tự nhưng ĐÚNG Kill Zone (London/NY) và ĐÚNG draw sai hướng — nếu case đó cũng thua, ủng hộ draw là nguyên nhân độc lập; nếu thắng, ủng hộ Kill Zone là nguyên nhân chính và draw chỉ là hindsight dư thừa.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis:** Lệnh Short tại OB H1 Premium, sweep chỉ đạt mức internal, thiếu Kill Zone, và draw ngắn hạn (theo note) hướng ngược bias — Loss với first_error=draw.

**Cần sửa** (load-bearing trước):
- C4 "draw ngắn hạn hướng lên được nhận biết tại entry" — **HINDSIGHT** · lập luận chỉ đứng vững nhờ thông tin xuất hiện sau (giá đã chạy lên lấy BSL) — không có mốc quan sát TRƯỚC entry nào được trích dẫn độc lập với outcome (xem O1 mục 10) → fix: tách rõ "draw nên được ưu tiên theo canon" (đúng, độc lập outcome) khỏi "draw này đã được nhận ra tại thời điểm đó" (chưa chứng minh được).  ← (load-bearing)
- C_sweep "sweep chỉ là internal, không phải external" — **UNSUPPORTED** · SKILL.md § Sweep yêu cầu "level có tên và được dùng"; note tự nhận không có số liệu định lượng phân biệt Internal/External (chỉ diễn giải) → fix: bổ sung độ sâu bấc/pip vượt ra ngoài OB.
- C_pattern "4/4 lệnh thua cùng họ Unswept Liquidity Path" — **AMBIGUOUS** · doctrine (Liquidity/Target trong SKILL.md) không có ngưỡng thống kê để xác nhận một pattern portfolio, và bảng thiếu nhóm đối chứng (Win) → đây là doctrine gap ở cấp phương pháp luận, không phải lỗi định nghĩa ICT term.

**PASS:** C1 (D1 Bearish, LH/LL — SKILL.md không có tranh chấp định nghĩa ở đây), C2 (OB Premium — SKILL.md § Premium/Discount, entry trên EQ H1 1.20247, đúng phía cho Short), C5 (Kill Zone — SKILL.md § Killzone/Time, giờ cụ thể 10:05 UTC+7 đã nêu, không suy diễn).

**Verdict:** NOT ALIGNED — load-bearing claim C4 mang HINDSIGHT khi đọc theo nghĩa "đã biết trước", điều này theo verdict decision rule (ict-doctrine SKILL.md) tự động dẫn tới NOT ALIGNED bất kể C1/C2/C5 PASS.

**Notes:** Đây là ca đặc biệt: Doctrine check ở cấp CLAIM ĐƠN LẺ (C4 là hindsight) khác với việc RULE ĐỀ XUẤT (draw gate) có sai theo canon hay không (nó không sai — canon ủng hộ hỏi draw trước mọi lệnh). Bài học meta cho vault: một lesson-learned có thể ĐÚNG VỀ MẶT DOCTRINE (nên làm) trong khi CHẨN ĐOÁN NGUYÊN NHÂN của chính lệnh đang xét lại mang tính hindsight — hai việc này cần được note tách bạch rõ hơn trong các lần viết tiếp theo.

---

## 12. Lesson Learned (bản đầy đủ)

> [!info] Không lặp lại các rule đã có ở mục 7.3/7.6/9. Phần dưới đây bổ sung lớp CHƯA có: phân biệt rule-đúng-theo-canon với chẩn-đoán-hindsight, và anti-overfitting cho chính bảng 9.3.

### (a) Bài học kỹ thuật

1. **"First error step" cần phân biệt giữa lỗi xác nhận được TRƯỚC outcome và lỗi chỉ nhìn thấy được SAU outcome.** Ví dụ số thật: Kill Zone (10:05 UTC+7, GATE khách quan đo bằng đồng hồ) là lỗi xác nhận được TRƯỚC; "draw ngắn hạn hướng lên" chỉ được note xác nhận bằng cách trỏ tới OB 1.21296-1.21227 đã tồn tại — nhưng không có ghi chú thời gian-thực nào xác nhận đây là nhận thức tại 10:05 UTC+7, không phải suy ngược. Tổng quát hóa: khi ghi `first_error_step`, luôn tự hỏi "tôi có thể chứng minh mình biết điều này TRƯỚC khi thấy kết quả không?" — nếu không, gắn field phụ `diagnosed_with_hindsight: true`.
2. **Pattern portfolio (bảng kiểu 9.3) cần nhóm đối chứng để có giá trị thống kê, không chỉ liệt kê các lệnh thua.** Ví dụ số thật: 4/4 lệnh Loss có "pool cùng phía SL" nghe thuyết phục, nhưng nếu 8/10 lệnh Win cũng có đặc điểm này mà không được đếm, tỷ lệ 4/4 không có ý nghĩa phân biệt. Tổng quát hóa: mọi bảng "X/X lệnh thua chia sẻ đặc điểm Y" trong vault cần đi kèm "Z/N lệnh thắng có đặc điểm Y hay không" trước khi được dùng làm cơ sở rule.

### (b) Bài học quy trình/checklist

- Rule "draw gate" (hỏi pool chưa-lấy nằm phía nào trước mọi lệnh) đúng theo canon ICT độc lập với việc case này có chứng minh được bằng thống kê hay không — nên **giữ nguyên rule đó trong Playbook** (đã có ở mục 7.6), nhưng tách nhãn nguồn gốc: "rule theo canon" vs "rule được validate bằng N case trong vault" là hai mức độ tin cậy khác nhau, cần ghi rõ khi báo cáo.
- Đề xuất thêm field `narrative_written_before_or_after_outcome` (before/after) cho mọi đoạn Lesson Learned mô tả cơ chế thị trường — giúp người đọc sau này tự phân biệt được hindsight risk mà không cần suy luận lại.

### (c) Bài học tâm lý-hành vi

- Việc note tự phát hiện và sửa "cải thiện tâm lý" thành "lỗi quy trình + nhận thức" (mục 7.6) là hành vi tốt, cần giữ nguyên — không lặp lại chi tiết ở đây.
- Rủi ro mới phát hiện: một lời giải thích cơ chế thị trường càng chi tiết, càng "logic ICT" (như mục 7.4, 9.1, 9.2) càng dễ khiến người đọc (và chính người viết ở lần sau) tin rằng đó là điều đã biết trước, dù thực chất một phần là tái dựng sau outcome — độ chi tiết của narrative không phải bằng chứng cho tính real-time của nó.

### (d) Rule đề xuất cho Playbook

- [ ] Khi viết Lesson Learned mô tả "draw/pool nào đang chi phối", bắt buộc trích dẫn ghi chú hoặc mốc giá **có timestamp trước entry** — nếu không có, gắn nhãn `retrospective_inference` thay vì trình bày như quan sát real-time.
- [ ] Mọi bảng pattern portfolio kiểu "N/N lệnh thua chia sẻ X" phải kèm cột đối chứng (bao nhiêu lệnh thắng cũng có X) trước khi dùng làm căn cứ rule mới.
- [ ] Định lượng hóa `sweep_type: Internal/External` bằng số cụ thể (pip vượt ra ngoài level, số nến giữ ngoài) thay vào diễn giải thuần tường thuật.

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG nên coi bảng 9.3 ("4/4 lệnh thua cùng họ Unswept Liquidity Path") là một pattern đã được validate thống kê — đây mới là quan sát hậu nghiệm trên đúng 4 case Loss, chưa có nhóm đối chứng Win.
- KHÔNG nên áp dụng "hỏi draw ngắn hạn trước mọi lệnh" như thể lệnh này đã CHỨNG MINH được giá trị của gate đó bằng dữ liệu thực nghiệm — giá trị của gate đến từ canon ICT, không phải từ n=1 case Loss này (dù case này minh họa tốt cho lý do TẠI SAO canon có gate đó).
- KHÔNG nên dùng chi tiết narrative phong phú (mục 7.4, 9.1, 9.2) làm thước đo độ tin cậy của chẩn đoán — một lời giải thích dài và logic không tự động có nghĩa là nó được biết trước outcome.


### Liên kết

- Model: [[01 - ICT 2022 Model]]
- POI ladder: [[25-OB-Order-Block]] · [[13-FVG-Fair-Value-Gap]] · [[04-Breaker-Block]]
- Entry refine: [[10-Consequent-Encroachment-Mean-Threshold]] · [[27-Premium-Discount]]
- Bước: [[20-Liquidity-Sweep]] · [[21-Market-Structure-Shift]] · [[18-Kill-Zones]]
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Mistakes: [[04-Mistake-FOMO-Entry]] · [[12-Mistake-Log-Data-Mismatch-Backtest]] · [[08-Mistake-Weak-Displacement]] · [[13-Mistake-Trading-Into-Unswept-Liquidity]]
