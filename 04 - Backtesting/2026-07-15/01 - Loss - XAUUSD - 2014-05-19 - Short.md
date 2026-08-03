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

## 9. Phân tích bổ sung chuyên sâu (2026-07-18)

### 9.1. Các khái niệm ICT bị áp dụng SAI

| Khái niệm | Tôi đã dùng như thế nào (SAI) | Cách dùng ĐÚNG | Ảnh hưởng |
|---|---|---|---|
| [[04 - Breaker Block]] | Dùng BB (0.618) làm **terminal POI** khi phía trên còn OB (0.786) chưa test | BB đáng tin nhất khi nó là PD array CUỐI CÙNG còn hiệu lực trên đường đi (các pool/POI sâu hơn đã bị dọn). Khi BB xếp chồng DƯỚI một OB chưa test cùng phía, BB nông gần như mặc định là trạm trung chuyển, không phải điểm đảo chiều | Chí mạng — first_error |
| [[15 - Inducement]] | Không nhận diện rằng chính BB là inducement | Inducement không chỉ là swing nhỏ trước POI — **một PD array nông "trông như POI" nằm trước POI thật** là dạng inducement cao cấp nhất, vì nó dụ được cả trader có học SMC. BB 0.618 + cụm SL trên nó chính là mồi kéo giá lên OB | Chí mạng |
| [[25 - OB - Order Block]] | Hiểu đúng khái niệm OB nhưng bỏ qua nguyên tắc thứ tự: POI sâu nhất chưa test trong Premium là **điểm đến** của thanh khoản | Khi ≥2 PD array xếp chồng cùng phía: OB/POI sâu hơn là terminal; chỉ giao dịch POI nông sau khi POI sâu đã được test-và-từ-chối | Chí mạng |
| [[27 - Premium Discount]] + [[26 - OTE - Optimal Trade Entry]] | Coi "chạm 0.618 = đã vào Premium đủ sâu để short" | 0.618 là **mép ngoài** của OTE. Khi phía trên còn PD array + BSL chưa lấy, terminal delivery thường ở sweet spot sâu (0.705–0.79). Vào ở mép ngoài = trả giá bằng việc đứng trước cả đoạn đường còn lại | Nặng |
| [[20 - Liquidity Sweep]] + [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]] | Dùng cú sweep minor high **M1** (1301.647) để hợp thức hóa một quyết định POI cấp **H1** | Sweep phải cùng cấp với cấu trúc đang giao dịch: short từ Premium H1 đòi hỏi buy-side CẤP H1 (cụm thanh khoản BB→OB, đỉnh 0.786) bị lấy trước. Sweep M1 chỉ đủ tin cho một target M1 | Nặng |
| [[13 - FVG  - Fair Value Gap]] | Chấp nhận việc M5 không tạo FVG sạch, tụt xuống M1 tìm trigger | FVG là **bằng chứng khách quan** của displacement thật. M5 không in được FVG = order flow bán chưa áp đảo = đứng ngoài ([[08 - Mistake - Weak Displacement]]) | Nặng |

### 9.2. Những điều tôi NGHĨ là đúng nhưng thật ra SAI

Đây là các "cảm giác đúng" đã dẫn tới quyết định — loại lỗi dễ tái phạm nhất:

1. **"Breaker rank 3 cao hơn OB rank 2, nên BB là POI tốt hơn."** SAI về bản chất của thang rank: rank đo **độ tin cậy của phản ứng khi POI đó là terminal** (được giá tìm đến sau khi mọi thứ phía trước đã dọn xong), KHÔNG phải thứ tự ưu tiên khi 2 POI xếp chồng. Khi xếp chồng cùng phía, **độ sâu thắng rank**. Một OB rank 2 ở 0.786 chưa test đứng trên một BB rank 3 ở 0.618 → OB thắng.
2. **"Tôi phân tích đúng hướng, thua chỉ là xui."** SAI — và nguy hiểm nhất về tâm lý (mentor note đã cảnh báo). Giá chạm TP sau đó không hoàn lại -1R. "Đúng hướng + sai vị trí" là một lỗi hệ thống **lặp lại được và sửa được**; gọi nó là xui đồng nghĩa từ chối sửa.
3. **"Chuỗi Sweep → MSS → Displacement → FVG trên M1 đã đủ = mô hình 2022 hoàn chỉnh."** SAI cấp độ: chuỗi đầy đủ nhưng chạy ở **sai POI** thì toàn bộ trigger chỉ là nhiễu trên đường giá đi lấy OB. Mô hình 2022 không phải "cứ đủ 7 bước ở đâu đó là vào" — 7 bước phải diễn ra tại đúng terminal POI.
4. **"SL trên cạnh BB + buffer là an toàn."** SAI: buffer chỉ chống wick nhiễu, không chống được một cú draw có chủ đích tới pool sâu hơn. SL 1301.789 nằm **giữa BB và OB** = nằm giữa đường đạn.
5. **"Entry khớp đúng CE của FVG = entry chất lượng."** SAI khi tách rời bối cảnh: độ chính xác cơ học (8/10) không bù được POI selection (3/10). Entry đẹp tại vùng sai vẫn là lệnh sai.

### 9.3. Đào sâu: góc nhìn Liquidity Reflexivity + pattern chéo

**Vì sao BB 0.618 lại "được chọn" làm mồi?** Theo [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]: BB ở 0.618 là vùng **dễ nhìn thấy nhất** đối với đám đông SMC (fib 0.618 + breaker structure — hai thứ được dạy nhiều nhất). Càng nhiều người short tại đó, cụm SL phía trên BB càng dày → cụm SL đó **tự trở thành buy-side liquidity bổ sung** kéo giá lên OB. Bạn không chỉ chọn sai POI — bạn chọn đúng cái POI mà thuật toán *muốn* đám đông chọn. Ngược lại, OB 0.786 "khó vào" hơn về tâm lý (phải chờ giá chạy ngược sâu hơn) — và chính vì ít người dám đợi, nó mới là nơi đảo chiều thật.

**Vị trí trong họ lỗi chung:** lệnh này là biến thể "POI sâu chưa test" của cùng một pattern xuất hiện ở cả 4 lệnh thua gần nhất — SL luôn nằm trong đường giá đi lấy thanh khoản chưa bị lấy (GBPUSD 17/7: ERL dưới POI; XAU 14/5: phần thân còn lại của chính RB; EURUSD 7/5: BSL external phía trên). Xem phân tích tổng hợp + gate kiểm tra bắt buộc tại [[13 - Mistake - Trading Into Unswept Liquidity]].

---

## 10. Phản biện chuyên sâu (Devil's Advocate)

![[XAUUSD-20140519-poi-stack-priority.svg|760]]

```yaml
type: devils-advocate
mode: REVIEW
instrument: XAUUSD
date: 2014-05-19
timeframes_provided: [D1/H4 (mô tả), H1 (mô tả + ảnh không đọc được), M5 (mô tả), M1 (mô tả)]
verdict: SURVIVES THIS ATTACK
evidence_sufficiency: thin
opposite_case_strength: weaker
objections: {fatal: 1, material: 2, minor: 1}
open_objections: "O1 OPEN, O2 OPEN, O3 OPEN"
tags: [ict, devils-advocate, review]
```

**0. Evidence base**: Mô tả bằng lời + số liệu frontmatter/mục 9. Ảnh không đọc được. `evidence_sufficiency = thin` — nhưng note gốc đã tự làm việc replay khá kỹ ("right direction, wrong POI" đã tự xác nhận bằng quan sát giá SAU ĐÓ đảo đúng hướng), nên phần lớn objections ở đây nhắm vào layer METHOD/DOCTRINE hơn là tái phát hiện fact mới.

**1. Thesis + load-bearing claim**: C1 Bias D1/H1 Bearish, Premium. C2 Có 2 POI cùng phía xếp chồng: Breaker Block nông (0.618, 1300.545–1301.645) và Order Block sâu (0.786, ~1304.5–1306) chưa test. C3 Chọn Breaker Block (nông hơn) làm entry thay vì chờ OB sâu hơn. C4 SL bị quét trên đường tới OB, giá sau đó đảo đúng hướng xuống TP (quan sát bằng replay). C5 (từ C2+C3) first_error = poi — chọn sai cấp độ POI trong stack, không phải sai bias/hướng. **Load-bearing: C2 — nếu Breaker Block ở đây không thỏa canon (đòi hỏi chuỗi OB-thất-bại-thật + đảo cực), toàn bộ khung "POI nông vs POI sâu" bị đặt sai tên, và bài học "nên chờ OB sâu hơn" có thể chỉ đúng vì OB, không phải vì Breaker kém hơn về bản chất.**

**2. What survives**: C1 (bias, nhất quán với cả cụm 4 lệnh và đã qua kiểm chứng ở replay). C4 — quan sát "giá đảo đúng hướng sau khi quét SL" là claim REVIEW hợp lệ (không phải hindsight vì đây đúng là mục đích của bài replay post-mortem, không phải justification cho quyết định TẠI thời điểm entry) — nhưng cảnh báo: nó không được dùng làm bằng chứng "quyết định entry đúng", mà chỉ dùng để định vị first_error chính xác là poi-selection chứ không phải bias. Note gốc đã làm đúng phân biệt này.

**3. Objections**

**O1 · [METHOD] · fatal · attacks C2 (load-bearing)**
Claim: vùng 1300.545–1301.645 được gán nhãn "Breaker Block".
Fails: Breaker theo canon (SKILL.md § Breaker) = "OB thất bại sau khi lấy liquidity + phá structure, đảo cực — cần chuỗi sự kiện, không chỉ một nến". Note không mô tả rõ: (a) OB gốc là gì trước khi "thất bại", (b) liquidity nào bị lấy ngay trước khi nó thất bại, (c) structure nào bị phá bởi chính cú thất bại đó. Nếu thiếu 1 trong 3, đây là quy trình chọn nhãn theo cùng khuôn mẫu đã gặp ở note 02 (RB) — gán tên khái niệm "nghe advanced hơn" cho một vùng phản ứng giá mà chưa xác nhận đủ điều kiện chuỗi sự kiện.
Evidence: mục 1/2 note gốc mô tả Breaker chỉ bằng range giá + vị trí OTE 0.618, không có narrative "OB này từng thất bại giữ giá lúc nào, structure nào bị phá bởi sự thất bại đó".
Consequence: nếu nhãn Breaker không đứng vững, C5 (first_error=poi, đóng khung là "chọn nhầm cấp độ trong đúng một họ POI") phải mở rộng thành "chọn một nhãn có thể sai từ gốc, không chỉ sai cấp độ" — bài học rút ra (mục 9, "nên chờ POI sâu hơn khi có stack") vẫn đúng về mặt thực dụng (OB sâu hơn thắng), nhưng lý do lý thuyết đằng sau ("Breaker yếu hơn OB vì đã unwind") không được xác lập nếu Breaker chưa từng đúng là Breaker.
Your best answer: "Breaker được xác nhận qua confluence_score=3, mức cao nhất trong các loss của cụm — nhiều xác nhận độc lập." Không cứu O1 — confluence_score đo SỐ LƯỢNG yếu tố hội tụ (OTE, sweep, MSS...), không đo tính hợp lệ của NHÃN Breaker riêng lẻ; có thể có 3 yếu tố hội tụ tại một vùng bị gán nhãn sai.
Retracted by: mô tả cụ thể OB gốc (giá, thời điểm) + liquidity bị lấy ngay trước khi nó thất bại + structure cụ thể bị phá bởi cú thất bại đó — đủ 3 mắt xích theo canon.

**O2 · [DOCTRINE] · material · attacks C3**
Claim (ngụ ý): việc có 2 POI cùng phía xếp chồng (Breaker 0.618, OB 0.786) tự nó là lý do nên ưu tiên POI ở Fib sâu hơn.
Fails: SKILL.md § OTE chỉ định nghĩa dải 0.618–0.786 là vùng entry hợp lệ, KHÔNG xếp hạng ưu tiên giữa các mức trong dải đó, và § Premium/Discount cũng không đưa ra quy tắc "luôn chọn POI xa hơn khi có stack". Việc ưu tiên OB sâu hơn Breaker nông là một suy luận thực dụng (từ kết quả), không phải một điều khoản doctrine có sẵn.
Evidence: SKILL.md bảng định nghĩa nhanh — không có mục nào về "thứ tự ưu tiên POI khi stack cùng phía".
Consequence: bài học "nên chờ OB sâu hơn" (mục 9) là một heuristic rút ra từ QUAN SÁT THỰC NGHIỆM (POI rank cao thua, OB thắng ở nơi khác trong cụm), không phải một luật doctrine đã tồn tại trước — cần được gắn nhãn đúng bản chất: rule tự đúc kết từ dữ liệu nhỏ (n rất nhỏ), không phải "vi phạm canon".
Your best answer: đã tự flag đúng ở mục 9 (nếu note gốc đã nói rõ đây là bài học kinh nghiệm chứ không phải trích dẫn canon) — cần xác nhận note không lỡ trình bày heuristic này như một luật ICT có sẵn.
Retracted by: note gốc dẫn rõ nguồn của quy tắc "ưu tiên POI sâu hơn khi stack" là kinh nghiệm cá nhân/quan sát, không phải trích dẫn canon — nếu đã vậy, objection tự đóng ở mức ghi nhận, không cần sửa gì thêm.

**O3 · [HINDSIGHT] · minor · attacks C5**
Claim: "right direction, wrong POI" được dùng làm kết luận chẩn đoán chính.
Fails: nhãn này sử dụng thông tin đường đi giá SAU điểm quyết định entry (giá tiếp tục xuống sau khi quét SL) — đúng như brief đã cảnh báo cho REVIEW mode. Tuy nhiên, đây là replay post-mortem có mục đích rõ ràng: định vị first_error đúng loại (poi, không phải bias) — không phải biện minh ngược cho một quyết định. Note gốc đã tự phân biệt điều này (mục 9 gốc), objection ở đây chỉ gắn nhãn tier cho một pattern đã tồn tại, không phải phát hiện lỗi mới.
Consequence: không đổi kết luận, chỉ cần nêu rõ trong log rằng "đúng hướng sau đó" là quan sát REVIEW-only, không phải yếu tố có thể biết tại M1 lúc entry.
Retracted by: đã đủ điều kiện — note gốc dùng đúng mục đích, giữ objection ở minor để hoàn thiện ledger.

Drafted: 4. Cut: 1 (một nghi vấn về `idm_swept` tương tự note 02 — bị cắt vì note 04 đã có mô tả rõ hơn về sweep tại mục 9 gốc, không thiếu số giá như note 02).

**4. Opposite case (cùng evidence)**: Đọc ngược C5 — first_error không phải "poi" mà là "risk/stacking" tổng quát hơn: có 2 POI cùng phía đã là tín hiệu KHÔNG NÊN VÀO LỆNH ở cấp nông trước khi biết cấp sâu phản ứng ra sao (chờ xác nhận thất bại tại Breaker bằng một dấu hiệu LTF trước khi entry, thay vì entry ngay tại chạm đầu tiên) — tức lỗi là "entry sớm trong một stack chưa phân giải", không phải "chọn nhầm loại nhãn". Tự phản biện case ngược: đây gần như tương đương C5 về hệ quả thực hành (cả hai đều dẫn tới "nên đợi/ưu tiên POI sâu hơn"), khác nhau chủ yếu ở FRAMING nguyên nhân gốc (nhãn sai vs thời điểm sớm) — không đủ khác biệt observable để tách hai case dứt điểm từ dữ liệu hiện có. **Strength: weaker** — case ngược không thêm được insight mới ngoài đổi tên nguyên nhân, và không giải quyết được câu hỏi cốt lõi O1 (Breaker có đúng nhãn không).
Distinguishing observable: nếu xác nhận đủ 3 mắt xích Breaker theo canon (O1) → case gốc (C5, lỗi chọn cấp poi) đứng vững nguyên dạng. Nếu KHÔNG xác nhận được (Breaker thực ra chỉ là vùng phản ứng giá bất kỳ) → case ngược có lý hơn, vì khi đó "loại nhãn" không còn ý nghĩa để so sánh, chỉ còn "thời điểm entry trong một stack".

**5. Verdict: SURVIVES THIS ATTACK.** Kết luận chính của note gốc (first_error=poi, nên ưu tiên OB sâu hơn Breaker nông khi stack) không bị BROKEN bởi các objections này — nhưng O1 (fatal, nhắm vào nhãn Breaker) có nghĩa là **lý do lý thuyết cho bài học** (Breaker "yếu hơn" OB) chưa được xác lập chắc chắn; may mắn là bài học THỰC HÀNH (chờ POI sâu hơn khi stack) không phụ thuộc vào việc nhãn có đúng tuyệt đối hay không — nó vẫn đúng dưới cả hai cách đọc (case gốc và opposite case ở mục 4). `evidence_sufficiency=thin`.

**6. Falsification tests**:
1. Đối chiếu ảnh H1 gốc xác nhận đủ 3 mắt xích Breaker (OB gốc, liquidity bị lấy, structure bị phá bởi sự thất bại) — đóng dứt điểm O1.
2. Kiểm xem note có dẫn nguồn rõ cho heuristic "ưu tiên POI sâu hơn khi stack" là kinh nghiệm cá nhân hay bị trình bày nhầm thành canon — đóng O2.
3. Rà vault tìm thêm case có stack 2 POI cùng phía (không chỉ XAU cluster này) để kiểm heuristic "ưu tiên sâu hơn" có giữ vững ở mẫu lớn hơn n=1 hay không.

---

## 11. Doctrine check (ICT 2022 canon)

**Thesis**: Short XAUUSD 19/5, có 2 POI cùng phía stack (Breaker Block 0.618, Order Block 0.786 chưa test), chọn Breaker (nông hơn) làm entry; SL bị quét trên đường tới OB, giá sau đó đảo đúng hướng.

**Cần sửa** (load-bearing trước):
- C2 "vùng 1300.545–1301.645 = Breaker Block" — **UNSUPPORTED** (load-bearing) · why: thiếu cả 3 mắt xích bắt buộc theo canon (SKILL.md § Breaker: "OB thất bại sau khi lấy liquidity + phá structure, đảo cực — cần chuỗi sự kiện") — note mô tả vùng bằng vị trí Fib/range giá, không bằng chuỗi sự kiện → fix: bổ sung narrative xác nhận OB gốc, liquidity bị lấy, và structure bị phá bởi sự thất bại đó, hoặc hạ nhãn xuống "vùng phản ứng giá tại 0.618" (không gọi Breaker).
- C-heuristic "nên ưu tiên OB sâu hơn khi stack cùng phía" — **AMBIGUOUS** · doctrine gap: SKILL.md không có mục xếp hạng ưu tiên giữa các PD array cùng phía trong một dải OTE; đây là quan sát thực nghiệm hợp lý nhưng không thể chấm PASS/FAIL theo canon vì canon không phát biểu về nó — cần gắn nhãn "heuristic tự đúc kết", không trích dẫn như luật ICT có sẵn.

**PASS**: C1 (bias D1/H1 Bearish, nhất quán toàn cụm) · C4 (mô tả replay giá đảo hướng sau SL — đúng dùng cho mục đích chẩn đoán post-mortem, không lẫn vào justification tại thời điểm entry, theo đúng phân biệt REVIEW mode).

**Verdict**: **INSUFFICIENT EVIDENCE** — load-bearing claim C2 (nhãn Breaker) là UNSUPPORTED do thiếu chuỗi sự kiện bắt buộc; không phải NOT ALIGNED (không có mâu thuẫn arithmetic/structure rõ ràng để FAIL dứt điểm), nhưng không đủ căn cứ để PASS. Vì đây là load-bearing, verdict giữ ở INSUFFICIENT EVIDENCE dù bài học thực hành rút ra (ưu tiên OB sâu hơn) vẫn có giá trị độc lập với việc nhãn có đúng hay không.

**Notes**: Đây là gap thứ 3 trong batch xuất phát từ cùng một pattern: khái niệm "nghe advanced" (Rejection Block ở note 02, Breaker Block ở đây) được gán dựa trên vị trí/hình dạng giá mà chưa xác nhận đủ chuỗi sự kiện bắt buộc theo canon. Đề xuất bổ sung vào SKILL.md một checklist evidence bar cụ thể hơn cho cả RB và Breaker (hiện bảng định nghĩa nhanh có nêu yêu cầu định tính "cần chuỗi sự kiện" nhưng không có checklist 3 bước cụ thể để tự kiểm khi ghi log).

---

## 12. Lesson Learned (bản đầy đủ)

> Phần này CHỈ mở rộng — không lặp lại nội dung mục 9 (đã có "Phân tích bổ sung chuyên sâu", bao gồm bảng khái niệm bị áp dụng sai và phần "Liquidity Reflexivity").

### (a) Bài học kỹ thuật

1. **Khi có ≥2 PD array cùng loại/cùng phía xếp chồng trong cùng dải OTE, khoảng cách Fib giữa chúng nên được đo và ghi lại TRƯỚC khi chọn entry, không chỉ mô tả bằng lời "có 2 vùng".** Ví dụ số thật: Breaker tại 0.618 (1300.545–1301.645) và OB tại 0.786 (~1304.5–1306) — khoảng cách ~3-4 điểm ngay trên đường SL. Tổng quát: ghi rõ khoảng cách này giúp câu hỏi "SL có nằm trên đường tới POI sâu hơn không" trở thành một phép đo, không phải trực giác sau khi thua.
2. **Một nhãn PD array "cao cấp" (Breaker, Rejection Block, iFVG) cần đủ 3 mắt xích sự kiện được ghi rõ ràng — vị trí Fib + hình dạng giá không đủ để tự nó xác nhận nhãn.** Ví dụ số thật: Breaker ở đây được mô tả chỉ bằng range 1300.545–1301.645 + Fib 0.618, không có narrative OB-gốc/liquidity-bị-lấy/structure-bị-phá. Tổng quát: mọi nhãn "cao cấp" cần một dòng chuỗi sự kiện bắt buộc, không chỉ tọa độ.

### (b) Bài học quy trình/checklist

3. **Heuristic tự đúc kết từ backtest (ví dụ "ưu tiên POI sâu hơn khi stack") phải được ghi rõ nguồn là kinh nghiệm cá nhân, tách biệt khỏi trích dẫn canon ICT — nếu không, hai loại tri thức (luật cố định vs quan sát thực nghiệm còn ít mẫu) bị trộn lẫn và có thể bị đối xử với độ tin cậy sai.**

### (c) Bài học tâm lý-hành vi

4. **"Giá đảo đúng hướng sau khi quét SL" tạo cảm giác tiếc nuối mạnh ("chỉ cần chờ POI sâu hơn") — cảm giác này dễ bị biến thành quy tắc cứng ("luôn chờ POI sâu nhất trong stack") dù mẫu chỉ có n=1 trong cụm này. Cần phân biệt rõ giữa "bài học đáng cân nhắc" và "luật đã được validate".**

### (d) Rule đề xuất cho Playbook

- [ ] **R-BD-10**: Khi có ≥2 PD array cùng phía trong cùng dải OTE, đo và ghi khoảng cách Fib giữa chúng trước khi chọn POI entry.
- [ ] **R-BD-11**: Trước khi gán nhãn Breaker Block hoặc Rejection Block, điền đủ 3 trường bắt buộc: OB gốc (giá/thời điểm), liquidity bị lấy ngay trước sự thất bại, structure bị phá bởi sự thất bại đó — thiếu 1 trong 3 thì hạ nhãn xuống "vùng phản ứng giá" chung.
- [ ] **R-BD-12**: Heuristic backtest tự đúc kết phải ghi kèm tag `[HEURISTIC - n=X]` để phân biệt với trích dẫn canon, X = số lệnh đã quan sát pattern này.

### (e) Điều KHÔNG nên học từ lệnh này

- KHÔNG kết luận "Breaker Block luôn kém tin cậy hơn Order Block" từ một mẫu — cần thêm dữ liệu, và ngay cả trong mẫu này, danh tính "Breaker" của POI chưa được xác nhận đủ điều kiện canon (O1).
- KHÔNG biến "ưu tiên POI sâu hơn khi stack" thành luật cứng áp dụng máy móc — trong nhiều tình huống khác (ví dụ note 01, nơi giá KHÔNG đi tới OB sâu 0.786 trước khi đảo chiều thắng), việc chờ POI sâu hơn có thể khiến bỏ lỡ hoàn toàn; đây là heuristic có điều kiện, không phải quy tắc tuyệt đối.
- KHÔNG dùng confluence_score=3 (cao nhất trong các loss của cụm) để kết luận "confluence score không dự đoán được kết quả" một cách tổng quát — cần đối chiếu với cách tính confluence có tính đúng nhãn PD array (Breaker) hay không trước, vì nếu nhãn sai, điểm confluence được tính trên một nền không vững.


---

### Liên kết

- Concept POI: [[04 - Breaker Block]] · [[25 - OB - Order Block]] · [[27 - Premium Discount]] · [[26 - OTE - Optimal Trade Entry]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- Bước mô hình: [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]
- Model: [[01 - ICT 2022 Model]]
- Timing: [[18 - Kill Zones]] · [[40 - Macro Times]]
- Mistake liên quan: [[03 - Mistake - Entry When MSS not in POI Zone]] · [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]] · [[05 - Mistake - Not enough RR]] · [[13 - Mistake - Trading Into Unswept Liquidity]]
- Dashboard: [[_Backtest Dashboard]]
