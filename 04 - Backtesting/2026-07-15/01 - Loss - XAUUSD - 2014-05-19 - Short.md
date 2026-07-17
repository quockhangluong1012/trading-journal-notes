---
type: backtest
backtest_date: 2026-07-15
trade_date: 2014-05-19
symbol: XAUUSD
position: Short
result: Loss
session: London
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model
entry_timeframe: M1
htf_bias: Bearish
bias_correct: Yes
poi_type: Breaker Block
poi_rank: 3
poi_timeframe: H1
poi_location: Premium
poi_in_ote: Yes
ce_ote_overlap: Yes
poi_stack: H1 Breaker Block (POI đã chọn, sai) + M1 FVG (entry trigger) — H1 Order Block ở 0.786 là POI terminal thật, chưa được test
fvg_high: 1301.239
fvg_low: 1301.098
ce_price: 1301.1685
entry_type: CE
entry_precision: CE
limit_filled: Yes
fill_depth_pct:
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: Yes
step4_displacement_ok: No
step5_poi_ok: No
step6_entry_ok: No
step7_target_ok: NA
first_error_step: poi
missing_step: none
chained_fully: Yes
liquidity_swept: Yes
sweep_type: Internal
displacement: Yes
displacement_score:
mss: Yes
fvg_valid: Yes
confluence_score: 3
smt_confirm: No
cisd_confirm: No
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: Yes
correlated_asset: none
entry_price: 1301.167
stop_loss: 1301.789
take_profit: 1298.732
r_planned: 3.9
rr_if_ce:
rr_if_ote:
r_multiple: -1
risk_percent:
spread_cost:
r_net:
grade: C+
followed_plan: Yes
confidence:
tags:
  - backtest
  - ICT2022
  - POI
  - Breaker Block
---

# Backtest 2014-05-19 — XAUUSD Short — POI & Step Decision (Breaker Block)

> [!info] Ghi chú chuyển đổi (2026-07-17)
> Chuyển từ template cũ sang **Backtest template - POI & Step Decision**. Toàn bộ phân tích gốc (vốn đã rất chi tiết, có sẵn Final Grade theo tiêu chí) được giữ nguyên gần như 100%, chỉ tổ chức lại theo thứ tự mục mới và bổ sung frontmatter chuẩn hoá.
> `step4_displacement_ok` và `step6_entry_ok` được đánh **No** vì phân tích gốc tự nhận: M5 không tạo displacement/FVG sạch (chất lượng yếu) và entry xảy ra khi Bullish Displacement đối nghịch còn đang đẩy mạnh vào vùng — đúng theo GATE checklist gốc (mục 3, 2 dòng bị đánh dấu ❌).
> `step7_target_ok: NA` vì lệnh dính SL trước khi test target — target selection không bị outcome này phủ định hay xác nhận, chỉ được xác nhận đúng hướng sau đó (giá có chạm TP thật, xem mục 6).
> Đây là một trong những mẫu backtest **giá trị nhất** hiện có: đúng hướng, sai POI — dữ liệu phản chứng trực tiếp việc ưu tiên Breaker (0.618) thay vì Order Block (0.786) khi 2 POI xếp chồng trong Premium.

> [!important] Kết quả tóm gọn
> Giá quét qua cạnh trên BB bằng Bullish Displacement → dính SL. Sau đó giá mới retrace lên OB phía trên (0.786), quét OB rồi đảo chiều giảm đúng hướng và chạm TP. → BB không phải POI terminal; OB mới là. SL nằm ngay trên đường thanh khoản mà giá cần lấy để với tới OB.

---

## 0. Backtest Summary

| Field                     | Value                                                       |
| ------------------------- | ----------------------------------------------------------- |
| Symbol                    | XAUUSD                                                       |
| Model Variant             | Standard (D1→H1→M5/M1)                                       |
| Trade Date (dữ liệu)      | 2014-05-19 17:55 (UTC+7)                                     |
| Position                  | Short                                                        |
| Result                    | Loss (Hit Stop Loss)                                         |
| Session                   | London                                                       |
| HTF Bias                  | Bearish                                                      |
| Bias Correct?             | Yes (giá cuối cùng chạm TP, sau khi dính SL)                 |
| **POI Type**              | Breaker Block (0.618) — **sai lựa chọn**, xem Lesson         |
| POI Rank (8.1)            | 3 (Breaker)                                                  |
| POI Timeframe             | H1 (entry refine M1)                                         |
| POI Location              | Premium                                                      |
| **Entry Type**            | CE                                                           |
| **Limit Filled?**         | Yes                                                          |
| **First Error Step**      | poi (chọn BB nông thay vì OB sâu hơn cùng phía)              |
| R Planned (gross)         | 3.9                                                          |
| R Net (sau spread)        | (chưa có dữ liệu)                                            |
| R Multiple (kết quả)      | -1                                                           |
| Confluence Score (0–8)    | 3                                                             |
| Grade                     | C+                                                           |

> ⚠️ Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.
> ⚠️ **Cần xác nhận**: `take_profit = 1298.732` đọc từ order line trên chart H1/D1. Nếu TP thực khác, sửa lại `take_profit` + `r_planned`.

---

## 1. HTF Context & Bias

### D1 — Daily Bias & Context

- **Bias**: Bearish (nghiêng giảm trong nhịp retrace/range lớn) · **Market Condition**: Corrective/Range sau đỉnh
- **Lý do xác định bias**: Sau nhịp tăng dài kết thúc bằng Long Term High tại 1392.098, giá bị bán mạnh xuống ~1280 → Bearish MSS + Displacement khung lớn. Nhịp hồi lên ~1330 tạo lower high, tiếp tục bị đẩy xuống → order flow D1 vẫn nghiêng giảm. Hiện tại giá dao động trong nửa dưới range hậu-đỉnh (~1280–1330), sát vùng 1287–1309. Bên dưới còn D1 demand/OB (~1200–1215) nhưng ở rất xa, không phải target intraday.
- **Draw on Liquidity**: BSL — D1 range high 1392.098, các internal high của range. SSL — đáy range ~1287.66 và 1280 — draw dài hạn phía dưới, thuận hướng Short intraday.

![[Pasted image 20260715100017.png]]

### H1 — Cấu trúc & POI

- **Cấu trúc H1**: Dealing range Low (0)=1287.711 → High (1)=1309.013. Giá rally lên 1309.013 (lấy BSL/tạo swing high), sau đó Bearish Displacement + MSS đẩy xuống → xác nhận bias giảm. Sau MSS, giá xả xuống Discount (~1290/1287), quét SSL, rồi retrace ngược lên Premium để tìm short → đúng kịch bản ICT 2022 (short từ Premium sau khi Discount bị quét).
- **Hai PD Array (POI) trong Premium — điểm mấu chốt của bài học**:
  - **Order Block (OB)**: ~1304.5–1306 (quanh/trên 0.786 = 1304.454). POI sâu hơn, nằm cao hơn trong Premium.
  - **Bearish Breaker Block (BB)**: 1300.545–1301.645 (quanh 0.618=1300.87 → 0.705=1302.729). POI nông hơn, nằm thấp hơn → **đây là POI được chọn để short**.
- **Fib OTE levels**: 0.618=1300.87 · 0.705=1302.729 · 0.786=1304.454.
- **Order plan (đọc trên chart)**: Entry 1301.167 (gray) · SL 1301.789 (red, trên BB) · TP 1298.732 (green, internal SSL dưới đáy M1 ~1299.3).
- **Liquidity cần chờ sweep**: internal BSL của consolidation quanh BB; sau sweep → draw về SSL phía dưới (1299.3 → 1298.7 → xa hơn 1287.66).

![[Pasted image 20260715095910.png]]

### Phân tích context → lệnh

- Bias Bearish (D1+H1 đồng thuận), giá đã quét SSL Discount và đang retrace lên Premium → khung cảnh cho Short hợp lệ.
- Trong Premium có 2 POI xếp chồng: OB (0.786) ở trên, BB (0.618) ở dưới. Quyết định thử BB làm POI (thay vì OB/FVG như thường lệ).
- Kế hoạch: chờ giá về BB (tốt hơn thì tới CE của BB ~1301.095) → xuống M1/M5 tìm Sweep + Displacement + FVG → entry retrace FVG → SL trên cạnh BB + buffer → TP về internal SSL.

---

## 2. POI Profile

- **POI Type đã dùng**: Breaker Block (0.618) — thử nghiệm ưu tiên POI nông hơn thay cho OB quen dùng.
- **POI Rank (8.1)**: 3/5 (Breaker).
- **POI hình thành trên khung**: H1 (entry refine trên M1 FVG).
- **POI nằm ở**: Premium ✓ đúng phía cho Short.
- **POI stack**: BB (0.618–0.705) nằm **dưới** OB (0.786+) trong cùng Premium — 2 PD Array xếp chồng, cùng phía. OB là POI terminal thật (chưa test khi vào lệnh).
- **CE của FVG trùng OTE 62–79%?**: Yes (BB nằm 0.618–0.705).
- **Bounds & CE**: BB High 1301.645 / Low 1300.545. M1 FVG (entry) High 1301.239 / Low 1301.098, CE = 1301.1685 (≈ entry thực tế 1301.167).

![[Pasted image 20260715100207.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE
- **Entry Precision**: CE (M1 FVG)
- **Limit có khớp?**: Yes, khớp tại 1301.167 lúc 17:55
- **Giá đi sâu bao nhiêu vào FVG?**: không có số đo % cụ thể trong bản gốc
- **RR ghi lại**: r_planned 3.9 (Risk 0.622 điểm / Reward 2.435 điểm)

### M5/M1 — Xác nhận & điểm vào lệnh

- **M5**: giá tiến vào vùng BB/OB, có phản ứng bán nhưng **chất lượng displacement không sạch** — nến giằng co, bóng nến overlap, không tạo FVG M5 rõ ràng dứt khoát (tương tự [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]]). Đáng lẽ đây đã là tín hiệu đứng ngoài chờ thêm.
- **M1**: Sweep ~16:50 giá đẩy lên quét minor high 1301.647 (internal BSL). Displacement + FVG: sau sweep, nhịp giảm để lại M1 FVG 1301.239–1301.098 (CE≈1301.169). Entry đặt limit trong FVG, khớp tại 1301.167 lúc 17:55. SL 1301.789 = cạnh trên BB (1301.645) + buffer (~0.14). TP 1298.732 (internal SSL, dưới đáy M1 gần nhất ~1299.3).
- **Entry trigger**: Liquidity Sweep quét minor high 1301.647 trên M1; MSS phá swing low của nhịp sweep; Displacement → M1 FVG 1301.239–1301.098; Retrace về CE FVG → khớp lệnh.
- **Invalidation (kế hoạch)**: giá đóng nến trên cạnh trên BB.
- **Chờ đủ điều kiện?** Có (theo đúng plan đã định) — nhưng plan chọn sai POI.

M5: ![[Pasted image 20260715100315.png]]
M1: ![[Pasted image 20260715100207.png]]
Result: ![[Pasted image 20260715095941.png]]

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Field |
|---|---|---|---|
| 1 | Bias | Yes | `step1_bias_ok` |
| 2 | Draw on Liquidity | Yes | `step2_draw_ok` |
| 3 | Liquidity Sweep | Yes (M1 quét minor high 1301.647) | `step3_sweep_ok` |
| 4 | Displacement + MSS | **No** — M5 không tạo displacement/FVG sạch | `step4_displacement_ok` |
| 5 | POI (Breaker vs Order Block) | **No** — chọn POI nông (BB) khi POI sâu (OB) chưa test | `step5_poi_ok` |
| 6 | Entry (retrace, không chase) | **No** — short khi Bullish Displacement đối nghịch còn đẩy mạnh vào vùng | `step6_entry_ok` |
| 7 | Target | NA — dính SL trước khi test | `step7_target_ok` |

- **First Error Step**: **poi** — bước đầu tiên bị hỏng thật sự là chọn sai PD Array khi có 2 POI xếp chồng.
- **Missing Step**: none (chuỗi đủ, nhưng bị dùng sai từ bước POI trở đi).
- **Đủ chuỗi 7 bước?**: Yes.

> [!warning] Chuỗi "đủ bước" nhưng vẫn thua
> Đủ 7 bước KHÔNG bảo chứng thắng nếu bước 5 (chọn POI) sai. Bước 1–5 diễn ra ở một POI không phải terminal → toàn bộ trigger LTF chỉ là nhiễu trên đường giá đi lấy POI thật (OB).

---

## 5. Setup Quality & Confluence

- [x] Bias D1 rõ ràng, không mâu thuẫn H1
- [ ] **POI selection tối ưu** — ❌ chọn BB (nông) trong khi OB (sâu, 0.786) mới là terminal POI
- [~] Giá nằm trong Kill Zone — cần xác minh (17:55 UTC+7 có thể đã trôi khỏi London KZ chính)
- [x] Có Liquidity Sweep trước entry (M1)
- [ ] **Displacement rõ ràng** — ⚠️ M5 không tạo FVG sạch (displacement yếu)
- [x] Có MSS hợp lệ (M1)
- [x] POI nằm trong Premium (đúng phía cho Short)
- [ ] **Entry trong POI hợp lệ, không đua giá** — ⚠️ short khi Bullish Displacement còn đang đẩy mạnh vào vùng
- [ ] **SL ở vùng invalidation hợp lý** — ❌ SL trên BB nhưng dưới OB → nằm ngay trong đường thanh khoản mà giá cần lấy
- [x] RR ≥ 1:2 (R planned 3.9 — nhưng bị "thổi phồng" bởi SL nông, xem Lesson)

**GATE**: nhiều mục GATE FAIL (Displacement, POI selection, Entry timing, SL placement) → theo đúng tinh thần GATE-trước-SCORE, đây lẽ ra là **No Trade**.

| # | Confluence | +1? | Field |
|---|---|---|---|
| 1 | POI hạng ≥3 (Breaker) | Có | *(suy từ poi_rank=3)* |
| 2 | CE FVG trùng OTE 62–79% | Có | `ce_ote_overlap` |
| 3 | SMT divergence | Không có ghi chú | `smt_confirm` |
| 4 | CISD xác nhận | Không có ghi chú | `cisd_confirm` |
| 5 | Macro time | Chưa đánh giá | `in_macro_time` |
| 6 | NWOG/NDOG | Không có ghi chú | `nwog_ndog_align` |
| 7 | SD target align | Không có ghi chú | `sd_target_align` |
| 8 | Inducement bị quét trước POI | Có (minor high 1301.647) | `idm_swept` |

- **Score**: 3/8 → theo thang quy đổi, 3–4 = A về mặt điểm thuần, nhưng GATE fail chặn hẳn xuống **C+** — đúng tinh thần "GATE luôn thắng SCORE".

---

## 6. Phân tích sau lệnh (Replay)

- **Result**: **Hit Stop Loss** (-1R). Sau khi dính SL, giá tiếp tục lên OB (0.786), quét OB, rồi mới đảo chiều giảm và chạm TP 1298.732.

### Tại sao lệnh thua? (root cause thật)

**Root cause đơn nhất: SAI POI SELECTION** — chọn Bearish Breaker Block (0.618) làm POI trong khi Order Block (0.786) phía trên mới là POI terminal, khiến SL bị đặt ngay trong đường thanh khoản mà giá phải lấy để với tới OB.

Kiểm chứng bằng cấu trúc và số học:
- Trong Premium của range 1287.711→1309.013 có 2 PD Array xếp chồng: OB ~1304.5–1306 (≥0.786, sâu hơn); BB 1300.545–1301.645 (0.618–0.705, nông hơn — đã chọn cái này).
- Khi 2 POI xếp chồng cùng phía, thanh khoản có xu hướng bị kéo tới POI SÂU hơn trước khi đảo chiều. BB nông nằm trên đường đi tới OB.
- SL = 1301.789, chỉ nhỉnh trên cạnh BB (1301.645). Nhưng buy-side liquidity nằm rải rác từ trên BB lên tới OB (1301.6→1306). Để giá với được OB, nó bắt buộc phải đi xuyên qua 1301.789 → SL bị "ăn" như một phần của nhịp gom thanh khoản, không phải vì luận điểm Short bị phủ định.
- Bằng chứng phủ định trực tiếp: sau khi quét SL, giá không tiếp tục tăng vô định — nó lên đúng OB (0.786), quét, rồi đảo chiều xuống chạm TP 1298.732. → Hướng ĐÚNG. Chỉ có POI (và do đó SL) là sai.

### Thị trường có tín hiệu cảnh báo trước không? Có — ít nhất 3:
1. Còn một POI cao hơn chưa được test (OB @ 0.786) — short POI nông khi POI sâu chưa được chạm = short quá sớm.
2. M5 không tạo FVG sạch — phản ứng bán ở vùng yếu/giằng co. Liên kết [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]].
3. Bullish Displacement mạnh đẩy vào vùng ngay trước/tại entry — order flow ngắn hạn phía mua vẫn khỏe.

### Setup khớp bao nhiêu % với mô hình chuẩn? ~70%
Khớp tốt (context & sequence): bias Bearish đúng; SSL Discount đã bị quét; retrace về Premium; chuỗi Sweep→MSS+Displacement+FVG tồn tại trên M1; TP về internal SSL hợp lý; entry đúng CE của FVG. Lệch chuẩn: (a) chọn POI nông thay vì terminal — sai nặng nhất; (b) SL nằm dưới OB, trong đường thanh khoản; (c) vào khi Bullish Displacement đối nghịch còn mạnh; (d) M5 displacement yếu mà vẫn vào.

### Nếu vào lại, làm gì khác?
1. Ưu tiên POI SÂU hơn khi có POI xếp chồng — chờ giá lên OB (0.786) rồi tìm phản ứng + LTF trigger tại đó.
2. Nếu vẫn muốn short từ BB, SL bắt buộc đặt trên OB + buffer (~1306.x) → reward 2.435/risk ~5.0 = ~0.5R → tín hiệu rõ ràng rằng entry BB sai chỗ, nên BỎ lệnh.
3. Coi "M5 không FVG" = no-trade.
4. Không short khi Bullish Displacement vào vùng chưa bị hấp thụ.
5. Xác minh Kill Zone: entry 17:55 UTC+7 có nằm trong London KZ chuẩn không.

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> Bias và phân tích top-down đúng (giá chạm TP sau đó), nhưng thua vì chọn Breaker (0.618) làm POI thay vì Order Block (0.786) — SL nằm ngay trong đường thanh khoản dẫn tới OB, nên giá quét stop trên đường đi lấy POI thật rồi mới đảo chiều đúng hướng.

> [!warning] Ghi chú của mentor
> Đây là một "loss đúng hướng" — loại thua nguy hiểm nhất về mặt tâm lý, vì rất dễ tự nhủ "tôi phân tích đúng mà" và giữ nguyên lỗi. Đúng hướng nhưng sai POI + sai SL vẫn là -1R thật. Đừng để R:R 3.9 đánh lừa: nó là sản phẩm phụ của SL đặt ở POI nông, không phải bằng chứng chất lượng. Grade C+: bias đúng và execution kỷ luật (vào đúng CE, followed plan) kéo điểm lên, nhưng lỗi POI selection + SL trong vùng sweep chặn trần grade.

### 7.1. Bài học kỹ thuật

**Root cause (chỉ MỘT)**: Khi hai PD Array xếp chồng trong cùng Premium (BB@0.618 và OB@0.786), chọn POI nông (BB). Thanh khoản bị kéo tới POI sâu (OB) trước khi đảo chiều, SL đặt trên BB (dưới OB) rơi vào đúng đường gom thanh khoản đó.

**Cơ chế thị trường**: giá vào BB, cho phản ứng LTF nhỏ (đủ tạo M1 sweep/FVG dụ vào lệnh). Nhưng BB chưa hoàn tất "nhiệm vụ" — buy-side liquidity phía trên (gồm SL) và OB@0.786 vẫn chưa bị chạm. Một cây Bullish Displacement đẩy giá xuyên BB, quét SL, chạy lên quét OB, rồi mới đảo chiều giảm về TP. Kịch bản kinh điển: "stopped out trên đường giá đi lấy POI sâu hơn" (raid-then-reverse tại POI terminal).

**Triệu chứng dễ nhầm là "đúng"**: entry đẹp đúng CE của M1 FVG; R:R 3.9 hấp dẫn (do SL nông tạo ra); chuỗi ICT 2022 đủ 7 bước trên M1 (nhưng ở POI sai = trap); "tôi phân tích đúng hướng" (đúng, nhưng không cứu được -1R).

**Insight quan trọng nhất**: OB/FVG vẫn hay được dùng làm POI — và lần này OB chính là nơi giá đảo chiều thật. Thí nghiệm "dùng BB" cho một kết quả phản chứng sạch: với cấu trúc BB-nông + OB-sâu xếp chồng, **OB là POI terminal, BB chỉ là inducement/nơi bị quét**. BB không vô dụng, nhưng không nên được ưu tiên hơn một OB sâu hơn nằm cùng phía chưa được test.

**Cần xác minh thêm**: đo lại mép chính xác của OB (1304.5–1306?); xác nhận TP thực = 1298.732; Kill Zone 17:55 UTC+7 có trong London KZ chuẩn không; BB có được vẽ đúng chuẩn breaker (thân nến của OB tăng thất bại) không.

### 7.2. Pattern lặp lại

- Short POI nông khi còn POI sâu hơn chưa test → giá dễ chạy tới POI sâu, quét mình trên đường đi. Liên kết [[03 - Mistake - Entry When MSS not in POI Zone]].
- Siết SL cho đẹp R:R → đặt SL ở mép POI nông thay vì trên invalidation terminal. Pattern nguy hiểm nhất.
- Tụt khung "moi" setup khi M5 báo phản ứng yếu/không FVG. Liên kết [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]].
- Bán ngược Bullish Displacement đang đẩy vào vùng chưa bị hấp thụ.

### 7.3. Rule cần thêm/cập nhật vào Playbook

1. **Rule POI Priority**: khi ≥2 PD Array xếp chồng cùng phía trong Premium/Discount, ưu tiên POI SÂU hơn làm POI terminal. Chỉ short/long POI nông nếu POI sâu đã bị test và từ chối trước đó.
2. **Rule SL theo POI terminal**: SL luôn neo trên/dưới invalidation của POI SÂU nhất còn hiệu lực + buffer. Nếu SL đúng làm RR < RR floor → BỎ lệnh.
3. **Rule confirmation**: M5 không tạo displacement/FVG sạch → no-trade.
4. **Rule momentum đối nghịch**: không vào ngược một Displacement đang đẩy mạnh vào POI chưa bị hấp thụ.
5. **Rule grading**: lệnh "đúng hướng nhưng SL bị quét do chọn POI nông" chặn trần grade ở C+/B-, bất kể R:R lý thuyết.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 9/10 |
| POI Selection | 3/10 |
| Liquidity Sweep | 7/10 |
| Displacement/MSS quality | 4/10 |
| Entry Precision & Fill | 8/10 |
| Risk Management (SL placement) | 2/10 |

**Overall Grade**: **C+** (đúng hướng + kỷ luật execution — followed plan 8/10 — nhưng POI selection & SL placement là lỗi cấu trúc chặn trần grade)

> [!tip] Chống curve-fitting
> Trigger (M1 sweep + displacement + FVG trong killzone) nhận diện được trước outcome. Nhưng bài học không nằm ở trigger mà ở **POI selection** — thứ cũng phải được quyết định trước. Câu hỏi kiểm tra: trước khi vào, đã hỏi "còn POI nào sâu hơn chưa được test phía trên không?" chưa? Nếu chưa → đó là lỗ hổng quy trình cần đóng.

---

### Liên kết

- Concept POI: [[04 - Breaker Block]] · [[25 - OB - Order Block]] · [[27 - Premium Discount]] · [[26 - OTE - Optimal Trade Entry]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- Bước mô hình: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- Model: [[01 - ICT 2022 Model]]
- Timing: [[18 - Kill Zones]] · [[40 - Macro Times]]
- Mistake liên quan: [[03 - Mistake - Entry When MSS not in POI Zone]] · [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]] · [[05 - Mistake - Not enough RR]]
- Dashboard: [[_Backtest Dashboard]]
