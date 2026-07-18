---
type: backtest
backtest_date: 2026-07-17
trade_date: 2014-07-17
symbol: GBPUSD
position: Long
result: Loss
session: New York AM
setup: ICT 2022 Model
model_variant: Standard
entry_model: ICT 2022 Model (FVG POI + FVG Entry)
entry_timeframe: M5
htf_bias: Bullish
bias_correct: No
poi_type: FVG
poi_rank: 1
poi_timeframe: H1
poi_location: Discount
poi_in_ote: Yes
ce_ote_overlap: Yes
poi_stack: H1 FVG 1.70873-1.71103 + OTE 0.618-0.786 + M5 FVG 1.70980-1.70988
fvg_high: 1.71103
fvg_low: 1.70873
ce_price: 1.70988
entry_type: CE
entry_precision: CE
entry_in_ote: Yes
limit_filled: Yes
fill_depth_pct: 100
missed_by:
step1_bias_ok: Yes
step2_draw_ok: Yes
step3_sweep_ok: No
step4_displacement_ok: No
step5_poi_ok: Yes
step6_entry_ok: Yes
step7_target_ok: Yes
first_error_step: sweep
missing_step: sweep
chained_fully: No
liquidity_swept: No
sweep_type:
displacement: Yes
displacement_score: 2
mss: Yes
fvg_valid: Yes
confluence_score: 1
smt_confirm: No
cisd_confirm: No
in_macro_time:
nwog_ndog_align: No
sd_target_align: No
idm_swept: No
correlated_asset: none
entry_price: 1.70984
stop_loss: 1.70840
take_profit: 1.71473
r_planned: 3.40
rr_if_ce: 3.40
rr_if_ote:
r_multiple: -1
risk_percent: 0.5
spread_cost:
r_net: -1
grade: C
followed_plan: Yes
confidence: 3
confirmation_type: MSS
tags:
  - backtest
  - ICT2022
  - POI
  - MSS
  - FVG
  - iFVG
  - liquidity
  - good-loss
---

# Backtest 2014-07-17 — GBPUSD Long — FVG POI & FVG Entry (ICT 2022 Model)

> [!warning] Bản chất lệnh này: **"Good loss" về kỷ luật, nhưng "flawed setup selection" về tiêu chí lọc.**
> Lệnh thua nhưng quy trình top-down đúng hướng và kỷ luật thực thi tốt (không dời SL, không gồng). Cái sai KHÔNG nằm ở cơ học entry — nó nằm ở **việc chọn POI nằm ngay trên "móng" của dealing range, phía trên một vùng SSL cấu trúc chưa bị quét**, và vào lệnh **trước khi** thanh khoản đó được lấy. Đây là bài học giá trị nhất của cả setup này.

---

## 0. Backtest Summary

| Field | Value |
| --- | --- |
| Symbol | GBPUSD |
| Model Variant | Standard (D1 -> H1 -> M5) |
| Trade Date (dữ liệu) | 2014-07-17 (replay) |
| Position | Long |
| Result | **Loss** (quét SL 1.70840) |
| Session | New York AM (MSS ~19:15, entry ~22:15 UTC+7) |
| HTF Bias | Bullish (D1 HH/HL) |
| Bias Correct? | **No** — cấu trúc H1 bị lật (xem mục 6) |
| **POI Type** | FVG (H1, Discount) — trong OTE |
| POI Rank (8.1) | 1 (FVG đơn; OTE tính vào confluence, không tính vào rank) |
| POI Timeframe | H1 (entry refine M5) |
| POI Location | Discount (đúng phía cho Long) |
| **Entry Type** | CE của M5 FVG = 1.70984 |
| **Limit Filled?** | Yes |
| **First Error Step** | **Step 3 — Sweep**: vào trước khi SSL cấu trúc bị quét |
| R Planned | 3.40 (risk 14.4 pip / reward 48.9 pip) |
| R Multiple (kết quả) | **-1** (hit SL) |
| Confluence Score | 1/8 |
| Grade | **C** |

> [!info] Kiểm tra lại các con số (data hygiene)
> - **CE FVG H1 = 1.70988** = (1.71103 + 1.70873) / 2. Bạn ghi CE 1.70990 — lệch ~0.2 pip, không đáng kể nhưng nên dùng số tính lại.
> - **RR verify = 3.40**, không phải 3.472. Entry 1.70984, SL 1.70840 -> risk = 14.4 pip; TP 1.71473 -> reward = 48.9 pip; 48.9 / 14.4 = **3.40**. Để ra 3.472 thì risk phải ~14.08 pip (SL ~1.70843). Lệch nhỏ (~0.07R) nhưng nên ghi đúng để thống kê expectancy không bị sai.
> - Entry 1.70984 = CE của **M5 FVG** (1.70980-1.70988) và gần trùng **0.705 (1.70984)** của OTE — trùng khớp đẹp, không sai.

> WARNING: Nhớ đồng bộ các ô trên với **frontmatter** — Dataview đọc frontmatter, không đọc bảng này.

---

## 1. HTF Context & Bias

### D1 — Daily Bias

- **Bias**: Bullish · **Market Condition**: Trending.
- **Lý do**: D1 tạo HH/HL, leg tăng mạnh gần như một mạch tạo ra dealing range 1.70592 -> 1.71924. Nến tăng cây đen lớn cuối cùng có bấc dưới xuyên qua 0.786 rồi đóng cửa trở lại trong FVG — một rejection candle D1 ngay tại POI (có trọng số lớn hơn rejection trên M5/H1).
- **Draw on Liquidity**: Buy-side (BSL phía trên). Tại thời điểm setup, đọc bias Bullish là **hợp lý và đúng quy trình**.

> [!check] Đánh giá phân tích D1 của bạn: **Đúng về phương pháp.** HH/HL + leg impulse + rejection candle tại POI là chuỗi lý luận bias đúng chuẩn. Vấn đề KHÔNG nằm ở bước đọc bias — nó nằm ở điều D1 không trả lời được: **còn bao nhiêu SSL cấu trúc chưa bị quét bên dưới POI.**

![[Pasted image 20260717154911.png]]
### H1 — Cấu trúc, Dealing Range & POI

- **Dealing Range H1**: High **1.71924** / Low **1.70592** -> **EQ (0.5) = 1.71257**.
- **OTE (fib retrace từ đáy range)**: 0.618 = **1.71110** · 0.705 (sweet spot) = **1.70984** · 0.786 = **1.70885**.
- **H1 POI = FVG Bullish 1.70873 – 1.71103**, **CE = 1.70988**.
- **Vị trí FVG trong range**: FVG trùm gần hết dải OTE (0.618 -> 0.786) — đây là confluence loại A (imbalance + discount + OTE + CE ~ 0.705). Về mặt "vùng đẹp", POI này **rất chuẩn**.
- **Điểm mù chết (root cause)**: cạnh dưới FVG (1.70873) cách **rất gần** điểm định nghĩa range (1.70592) và **KHÔNG có EQL / swing nội bộ nào ở giữa** để hấp thụ thanh khoản. POI nằm ngay trên "móng nhà", không có "đệm".
- **Diễn biến**: giá retrace vào FVG lúc ~19:05, MSS M5 lúc 19:15, M5 FVG tạo lúc 22:15, entry CE M5 FVG.

> [!check] Đánh giá phân tích H1 của bạn:
> - Dealing range, OTE, FVG, CE: **đúng** (chỉ sai số nhỏ ở CE như trên).
> - **Thiếu sót**: không kiểm tra khoảng đệm thanh khoản nội bộ giữa POI và điểm định nghĩa range trước khi entry. Đây là mắt xích dẫn tới kết cục.

![[Pasted image 20260717154927.png]]

---

## 2. POI Profile

- **POI Type**: FVG (H1), Discount.
- **POI Rank (8.1)**: 1 (FVG đơn). OTE overlap là confluence riêng (đếm ở mục 5), không nâng rank theo thang 8.1.
- **POI hình thành trên khung**: H1 (entry refine M5).
- **POI nằm ở**: Discount (đúng phía cho Long).
- **POI stack**: H1 FVG (1.70873–1.71103) + OTE (0.618–0.786) + M5 FVG entry (1.70980–1.70988).
- **CE FVG H1 trùng OTE?**: CE = 1.70988 ~ 0.705 (1.70984) -> **Có**, trùng khớp gần tuyệt đối.
- **POI trong OTE?**: **Có** — đây chính là lý do POI trông "đẹp" trên giấy. Nhưng POI đẹp không bù được cho việc nó nằm sát thanh khoản cấu trúc chưa quét.

![[Pasted image 20260717154927.png]]

---

## 3. Entry Precision & Fill

- **Entry Type**: CE của **M5 FVG** = **1.70984** (= 0.705 OTE, = CE M5 FVG). **Về cơ học, entry này chính xác.**
- **Vị trí entry trong POI H1**: giữa FVG H1, tại CE/0.705 — **đúng vùng sweet spot**. Khác hẳn lệnh Win 2014-07-14 (vào nóng nửa trên) — lần này entry KHÔNG nóng.
- **Stop Loss**: **1.70840** (dưới cạnh dưới FVG H1 1.70873 + buffer ~3.3 pip). **Logic SL đúng.**
- **Take Profit**: **1.71473** (BSL phía trên).
- **RR**: **3.40** (verify lại).
- **Fill depth**: giá vào hết FVG và đi xuyên qua (fill_depth 100% rồi vượt) -> quét SL.

### M5 — Xác nhận & Điểm vào lệnh (timeline UTC+7)

1. **19:05** — giá retrace về FVG H1 (POI).
2. **19:15** — MSS + displacement trên M5 (NY session). *Nhưng: MSS xuất hiện khi SSL cấu trúc bên dưới CHƯA bị quét.*
3. **22:15** — M5 FVG hình thành (trễ ~3h sau MSS) -> entry CE M5 FVG = 1.70984.
4. **22:00 (17/7), 05:45 & 08:45 (18/7)** — giá quay lại test đáy gần SL **3 lần** trải dài ~14h qua cả phiên Á và đầu London.
5. Sau đó giá **quét mạnh qua SL**, retrace lên cạnh trên FVG (cổ điển "quét stop rồi mới đi thật"), rồi giáng chuỗi nến bearish displacement liên tiếp **xuyên thủng cả dealing range low (1.70592)**.

> [!warning] Điểm chí mạng: MSS M5 là một **MSS "sớm"**
> MSS 19:15 xuất hiện trên cú tap POI mà SSL cấu trúc (đáy range 1.70592) vẫn còn nguyên bên dưới. Một MSS LTF trong hoàn cảnh này **rất dễ là LTF inducement** — một nhịp quét thanh khoản nội bộ, chưa phải shift thật của HTF. Leg tăng sau MSS lại **chậm và yếu** (3h mới tạo FVG, chỉ lên tới ~1.7115, không tới TP) — củng cố thêm nhận định "phản ứng yếu".

**Entry trigger**: Retrace FVG H1 -> MSS + displacement + FVG M5 -> entry CE FVG M5.
**Invalidation (đúng như kế hoạch)**: đóng nến dưới cạnh dưới FVG H1 / dưới SL 1.70840 -> luận điểm Long vô hiệu. **Bạn đã tôn trọng đúng điểm invalidation này.**

![[Pasted image 20260717154847.png]]
![[Pasted image 20260717154855.png]]

---

## 4. 7-Step Decision Log

| # | Bước | Đúng? | Ghi chú |
|---|---|---|---|
| 1 | Bias | Yes | D1 Bullish, HH/HL + rejection candle tại POI |
| 2 | Draw on Liquidity | Yes | BSL phía trên (TP 1.71473) |
| 3 | Liquidity Sweep | **No** | **SSL cấu trúc (range low 1.70592) CHƯA bị quét trước entry** -> vào INTO liquidity |
| 4 | Displacement + MSS | **No** | MSS có thật nhưng trên tap POI với SSL chưa quét; leg yếu/chậm (score 2/4) |
| 5 | POI (FVG, Discount) | Yes | FVG H1 hợp lệ, đúng phía discount, trong OTE — POI bản thân là tốt |
| 6 | Entry (CE FVG M5) | Yes | Cơ học đúng: retrace về CE, không chase |
| 7 | Target | Yes | BSL hợp lệ, RR 3.40 lành mạnh |

- **First Error Step**: **3 (sweep)** — mắt xích gãy sớm nhất. Bạn chọn đúng POI (bước 5) và vào đúng cơ học (bước 6), nhưng **bước 3 hỏng**: entry được đặt trước khi draw-on-liquidity phía dưới (SSL range low) bị quét. Trong ICT 2022, thứ tự là *sweep -> displacement -> POI entry*; ở đây sweep cấu trúc chưa xảy ra thì MSS đã tới.
- **Missing Step**: sweep.
- **Chained fully?**: **No** (đứt ở bước 3).

> [!note] Vì sao first_error là "sweep" chứ không phải "poi"
> POI (FVG) tự thân hợp lệ, đúng phía, trong OTE — nên bước 5 là Yes. Vấn đề KHÔNG phải POI sai, mà là **thứ tự**: giá chưa lấy SSL cấu trúc thì không nên tin MSS và vào lệnh. Nếu bạn muốn quy về bước chọn POI, cách diễn đạt thay thế là "POI nằm sát móng range, thiếu đệm thanh khoản nội bộ" — hai cách nhìn cũng chỉ một lỗi.

---

## 5. Setup Quality & Confluence

### GATE (pass/fail)

- [x] Bias HTF rõ + draw xác định
- [ ] **Liquidity sweep TRƯỚC displacement** — **FAIL**: SSL cấu trúc chưa bị quét -> theo đúng GATE thì đây đáng lẽ là **No Trade**
- [ ] Displacement hợp lệ (>=3/4) — **weak** (score 2/4)
- [x] MSS hình thành (nhưng "sớm")
- [x] FVG/POI sạch + entry là retrace
- [x] Entry đúng Discount, đồng hướng bias
- [x] Stop có logic + target pool rõ + RR >= kế hoạch (3.40)

> [!warning] GATE luôn thắng SCORE
> Một mục GATE fail (sweep) = về nguyên tắc No Trade, dù các mục khác đẹp. Đây là lỗi filter đầu tiên cần sửa.

### SCORE

| # | Confluence | +1? |
|---|---|---|
| 1 | POI hạng >=3 (Breaker/iFVG/Unicorn) | Không (FVG rank 1) |
| 2 | CE FVG trùng OTE 62–79% | **Có** (CE 1.70988 ~ 0.705) |
| 3 | SMT divergence | Không đánh giá |
| 4 | CISD xác nhận flip (bullish) | Không (CISD sau đó lại xác nhận BEARISH) |
| 5 | Macro time | Chưa đánh giá |
| 6 | NWOG/NDOG / HTF PD align | Không |
| 7 | Target trùng -2SD / ERL | Không |
| 8 | Inducement bị quét TRƯỚC POI | **Không** (đây chính là vấn đề) |

- **Score**: **1/8**.

---

## 6. Phân tích sau lệnh (Replay)

**Result**: Loss — quét SL 1.70840, sau đó giá xuyên thủng cả dealing range low 1.70592.

### 6.1. Những điều tôi làm ĐÚNG

Đây là phần quan trọng để bạn không nghi ngờ cả hệ thống sau một lệnh thua:

- **Chuỗi lý luận top-down D1 -> H1 -> M5**: hoàn chỉnh và objectively identifiable (không hindsight bias). Bias, dealing range, OTE, POI đều đọc đúng phương pháp.
- **Entry cơ học**: vào tại CE M5 FVG ~ 0.705 OTE — chính xác, không nóng (tốt hơn lệnh 2014-07-14).
- **Logic SL**: đặt dưới cạnh dưới FVG H1 + buffer = invalidation point đúng. Không đặt SL bừa theo cấu trúc M5 nóng.
- **RR**: 3.40 — lành mạnh, không phải kiểu 1:1 gồng lỗ.
- **Kỷ luật thực thi**: KHÔNG dời SL, KHÔNG gồng thêm size, KHÔNG vào lại revenge khi bị quét. Tôn trọng đúng điểm invalidation đã định nghĩa. **Đây là hành vi của một trader có kỷ luật.**

### 6.2. Những điều tôi làm SAI (lỗi thật, tránh được)

1. **Vào lệnh trước khi SSL cấu trúc bị quét (first_error = sweep).** Dưới POI, đáy dealing range 1.70592 là một pool sell-side rõ ràng, hiển nhiên, **chưa hề bị quét**. Trong một leg tăng, thị trường thường lấy thanh khoản này TRƯỚC rồi mới expansion. Vào Long ngay trên nó = đi INTO liquidity.
2. **Không có đệm thanh khoản nội bộ.** Giữa cạnh dưới FVG (1.70873) và range low (1.70592) hoàn toàn trống — không EQL/swing nội bộ nào để hấp thụ. Lẽ ra đây phải là cờ giảm confidence/size ngay từ đầu.
   ![[GBPUSD-20140717-liquidity-buffer.svg|760]]
3. **Bỏ qua GATE "sweep trước displacement".** Theo checklist của chính bạn, đây là một No Trade — nhưng MSS "đẹp" đã làm lu mờ điều kiện này.

### 6.3. Những điều tôi NGHĨ là đúng nhưng thực ra SAI (nguy hiểm nhất)

Đây là loại lỗi dễ tái phạm vì nó "cảm giác đúng":

- **"MSS M5 = xác nhận đảo chiều, vào được rồi."** SAI. MSS trên cú tap POI khi SSL cấu trúc chưa quét **rất dễ là LTF inducement**. MSS đáng tin là MSS xuất hiện SAU khi thanh khoản cấu trúc đã được lấy, kèm displacement mạnh — không phải MSS sớm + leg yếu.
   ![[GBPUSD-20140717-premature-mss.svg|760]]
- **"D1 bullish nên xác suất Long cao, cứ vào."** Bạn đúng nhưng chưa đủ. Bias bullish LÀM TĂNG xác suất, nó không xóa bỏ khả năng một nhịp quét thanh khoản cấu trúc sâu hơn trước khi tiếp diễn — và khi POI nằm sát móng range, chính nhịp quét đó sẽ đi qua entry của bạn.
- **"Giá quét xuống rồi sẽ quay lên như các backtest trước."** Đây là mẫu backtest của bạn: giá thường quét POI / swing / EQL **nội bộ** (nằm GIỮA POI và range low) rồi quay lên. Lần này khác về chất: **không có thanh khoản nội bộ**, nên giá đâm thẳng xuống thanh khoản **cấu trúc** (range low). Phân biệt internal vs structural liquidity là mấu chốt.

### 6.4. Range invalidation & iFVG — vì sao đây là Loss "thật sự", không chỉ là SL bị chạm

Sau khi quét SL, giá đóng cửa và duy trì **dưới điểm định nghĩa range (1.70592)** — đây là **CISD (Change in State of Delivery)**: trạng thái giao hàng H1 đổi từ bullish sang bearish. Range low không phải EQL bình thường, nó là **điểm gốc định nghĩa cả leg tăng** mà bạn dùng để vẽ OTE. Khi nó bị đóng cửa xuyên qua (không chỉ wick), tiền đề "đây là retracement của leg tăng" sụp đổ -> thị trường in **Lower Low** thay vì Higher Low -> FVG không còn là vùng nạp đạn Long. FVG **đảo cực thành iFVG**: giá quay lại test cạnh dưới FVG cũ từ dưới lên và bị từ chối đi xuống — đúng logic polarity-flip.

![[GBPUSD-20140717-ifvg-flip.svg|760]]

> [!note] Quy tắc phân biệt (rút ra từ lệnh này)
> **WICK xuyên range low rồi quay lại = raid nội bộ (POI còn sống).** **ĐÓNG CỬA + acceptance dưới điểm định nghĩa range = CISD -> POI invalidated (không chỉ SL chạm), không re-entry Long tại FVG/OTE cũ.**

### 6.5. Bias có bị phá không?

`bias_correct: No` cho lệnh này (delivery H1 lật bearish, quét SL). Về D1 dài hạn, cần kéo chart sau 18/7 để xác định giá tạo Lower Low thật sự hay chỉ là một cú re-accumulation/liquidity run sâu hơn rồi bullish tiếp. Chart zoom-out cho thấy sau khi chạm 1.70592 giá range 1.7050–1.7090 một thời gian — ít nhất H1 đã chuyển neutral/bearish ngắn hạn. Ghi `No` để thống kê trung thực; nuance D1 để mở.

### 6.6. "Nếu vào lại, làm gì khác?"

- **Kiểm tra đệm thanh khoản nội bộ TRƯỚC entry.** Nếu giữa POI và điểm định nghĩa range không còn EQL/swing chưa quét -> giảm size hoặc đợi xác nhận chặt hơn (vd đợi giá quét range low + reclaim rồi mới tìm Long ở POI mới).
- **Đợi SSL cấu trúc bị quét trước khi tin MSS.** MSS sớm + leg yếu = không vào.
- **Đánh giá tốc độ/độ mạnh của leg displacement** tạo FVG trigger, không chỉ xác nhận nó tồn tại. Leg 3h/không tới TP = cờ cảnh báo.
- Giữ nguyên kỷ luật SL/không gồng (phần này bạn đã làm đúng).

---

## 7. Lesson Learned

> [!summary] Tóm tắt 1 dòng
> POI đẹp (FVG + OTE + CE) nhưng nằm sát "móng" dealing range, phía trên SSL cấu trúc chưa quét và không có đệm thanh khoản nội bộ -> giá đâm thẳng xuyên cả range, đóng cửa dưới range low (CISD) khiến FVG lật thành iFVG. Thua vì **chọn setup INTO liquidity**, không phải vì cơ học entry hay kỷ luật.

> [!warning] Ghi chú của mentor
> "Process over outcome" hoạt động cả hai chiều: đây là lệnh thua nhưng **kỷ luật thực thi tốt** (good loss), đồng thời **tiêu chí lọc còn thiếu** (flawed selection). Đừng nghi ngờ cả hệ thống — chỉ vá đúng một lỗ hổng: kiểm tra internal-liquidity buffer + đợi sweep cấu trúc trước khi tin MSS. Cú quét xuyên range **dự đoán được** (POI sát móng + SSL chưa quét), không phải xui.

### 7.1. Bài học kỹ thuật

- **Internal liquidity vs structural liquidity.** POI sát điểm định nghĩa range = rủi ro cao nếu không có EQL/swing nội bộ ở giữa làm đệm. Xác định điều này TRƯỚC khi vào.
- **MSS "sớm" = LTF inducement.** MSS trên tap POI khi thanh khoản cấu trúc chưa quét, kèm leg yếu -> không đáng tin.
- **Range low bị ĐÓNG CỬA xuyên qua = CISD = POI invalidated.** Khác hẳn wick raid nội bộ. Sau CISD, FVG -> iFVG (đảo cực tính); không re-entry hướng cũ.
- **RR cao (3.40) không cứu được setup chọn sai.** Vị trí entry chuẩn nhưng đặt sai chỗ trong cấu trúc thanh khoản.

### 7.2. Pattern lặp lại (cần theo dõi)

- **"POI sát điểm định nghĩa range, không có đệm thanh khoản nội bộ"** — soi lại toàn bộ ~11 backtest, phân loại: (A) giá quét EQL/swing NỘI BỘ rồi quay lên tôn trọng POI, vs (B) giá đóng cửa xuyên điểm định nghĩa range. So win-rate/expectancy hai nhóm. Nếu nhóm B thua đậm rõ rệt -> biến thành **filter entry thật**.
- **"MSS sớm + leg yếu + nhiều lần test SL kéo dài nhiều phiên rồi thua"** — theo dõi xem có lặp lại ở setup khác không. n=1 hiện tại, chưa đủ để thành rule cứng (tránh curve-fitting).

### 7.3. Rule cần thêm/cập nhật vào Playbook

- [ ] Rule (filter): trước entry tại FVG/OTE, kiểm tra có EQL/swing **nội bộ** chưa quét giữa POI và điểm định nghĩa range không. Nếu KHÔNG -> giảm size hoặc đợi xác nhận chặt hơn.
- [ ] Rule: chỉ tin MSS LTF **sau khi** thanh khoản cấu trúc gần nhất đã bị quét; MSS sớm + leg yếu = bỏ qua (áp dụng GATE "sweep trước displacement").
- [ ] Rule (invalidation): đóng cửa dưới điểm định nghĩa dealing range = POI invalidated + FVG -> iFVG; không re-entry hướng cũ, chuyển sang tìm short tại iFVG nếu bias LTF đã lật.
- [ ] Thêm field schema: `internal_liq_buffer` (Yes/No) và `structural_liq_below` (Yes/No) để lượng hóa mẫu này qua nhiều backtest.
- [ ] (Tùy chọn) rule quản lý lệnh khi giá re-test SL nhiều lần/kéo dài mà không trigger.

---

## 8. Final Grade

| Tiêu chí | Điểm |
|---|---|
| HTF Bias & Draw | 7/10 — đọc bias đúng phương pháp, nhưng không đánh giá SSL cấu trúc chưa quét |
| POI Selection (loại + hạng + P/D) | 5/10 — FVG hợp lệ & trong OTE, nhưng nằm sát móng range, không đệm thanh khoản |
| Liquidity Sweep | **2/10** — GATE fail: vào INTO liquidity, SSL cấu trúc chưa quét |
| Displacement / MSS quality | 4/10 — MSS "sớm" trên tap POI, leg yếu/chậm (2/4) |
| Entry Precision & Fill | 8/10 — CE M5 ~ 0.705, cơ học chính xác (điểm sáng của lệnh) |
| Risk Management (RR & SL) | 7/10 — SL logic đúng, RR 3.40 tốt, kỷ luật không dời SL |

**Overall Grade**: **C** — lệnh thua với **lỗi chọn setup thật (INTO liquidity)** nhưng **kỷ luật thực thi tốt**. Không phải lệnh sai sạch (cơ học + RR + kỷ luật đều ổn), cũng không phải xui rủi — cú quét dự đoán được. Giá trị lớn nhất: bài học phân biệt internal vs structural liquidity + iFVG flip.

> [!tip] Chống curve-fitting
> Trigger (sweep + displacement >=3/4 + POI hợp lệ trong killzone) có nhận diện được TRƯỚC outcome không? -> **Không**: bước sweep cấu trúc chưa xảy ra, displacement yếu. Theo đúng GATE thì đây là No Trade. Ghi nhận để lọc mẫu tương tự về sau.

---

## 9. Phân tích bổ sung chuyên sâu (2026-07-18)

> [!info] Mục này bổ sung 2 tầng còn thiếu so với phân tích gốc: (a) đối chiếu **từng khái niệm ICT đã bị áp dụng sai** với cách dùng đúng, và (b) đặt lệnh này vào **pattern chung của 4 lệnh thua gần nhất** — vì đây không phải lỗi đơn lẻ.

### 9.1. Các khái niệm ICT bị áp dụng SAI

| Khái niệm | Tôi đã dùng như thế nào (SAI) | Cách dùng ĐÚNG | Ảnh hưởng |
|---|---|---|---|
| [[20 - Liquidity Sweep]] | Coi việc "giá retrace về FVG + có MSS" là đủ điều kiện, bỏ qua yêu cầu sweep cấu trúc trước đó | Sweep là **bước 1 của chuỗi 2022**, không phải confluence tùy chọn. Với Long: SSL liên quan (range low 1.70592) phải bị lấy TRƯỚC, rồi mới tới displacement + MSS + POI | Chí mạng — first_error |
| [[21 - Market Structure Shift]] | Tin MSS hình thành ngay trên cú tap đầu tiên vào POI khi SSL còn nguyên bên dưới | MSS chỉ có giá trị xác nhận khi nó là **hệ quả của một cú sweep** (smart money đã fill xong lệnh). MSS xuất hiện TRƯỚC sweep = LTF inducement, không phải shift thật | Chí mạng |
| [[16 - Internal & External Range Liquidity (IRL & ERL)]] | Không phân loại thanh khoản: coi FVG (IRL) là điểm đến cuối của nhịp retrace | Giá luân phiên **ERL ↔ IRL**. Khi giá đã chạm IRL (FVG) mà ERL bên dưới (range low) chưa bị lấy, draw ngắn hạn xác suất cao là ERL — tức đi XUYÊN qua entry Long. Đây chính là tên gọi khái niệm chuẩn của lỗi "thiếu đệm thanh khoản" ở mục 6.2 | Chí mạng |
| [[26 - OTE - Optimal Trade Entry]] | Coi OTE + CE trùng 0.705 là bằng chứng tăng xác suất vô điều kiện | OTE chỉ hợp lệ khi **gốc của leg (range low) đã được bảo vệ bằng một cú sweep**. Fib vẽ trên một leg mà gốc chưa được xác nhận = công cụ đo đúng đặt trên tiền đề sai | Nặng |
| [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] | Chỉ xác định draw dài hạn (BSL phía trên làm TP), không hỏi "pool chưa-bị-lấy GẦN NHẤT nằm phía nào so với SL?" | Draw có 2 cấp: HTF draw (đọc đúng — BSL) và **draw ngắn hạn** (SSL dưới, chưa lấy). Khi 2 cấp ngược chiều nhau → NO-TRADE hoặc chờ pool gần bị quét xong | Nặng |
| [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] | Không áp dụng: POI càng "textbook" (FVG + OTE + CE chồng khít) tôi càng tự tin | POI càng đẹp và hiển nhiên → càng nhiều limit order + stop loss của đám đông tụ quanh nó → càng nhiều "nhiên liệu" cho một engineered sweep xuyên qua. Confluence đẹp phải đi kèm câu hỏi "ai cũng thấy cái này, vậy stop của họ nằm đâu?" | Trung bình |
| [[41 - Change in State of Delivery]] | **(Áp dụng ĐÚNG — sau lệnh)** đọc được acceptance dưới range low = CISD → không re-entry Long | Giữ nguyên cách đọc này. Đây là điểm sáng về khái niệm của bản phân tích — CISD + iFVG flip được nhận diện chuẩn | — |

**Khái niệm cần "nạp lại" ưu tiên số 1: IRL/ERL.** Toàn bộ root cause của lệnh này gói gọn trong một câu của framework đó: *FVG là Internal Range Liquidity; range low là External Range Liquidity; giá di chuyển luân phiên giữa hai loại này.* Trình tự đúng của một Long theo 2022 Model trong range này phải là **ERL trước → IRL sau**: giá quét range low (ERL) → displacement tăng + MSS → retrace về FVG mới hình thành (IRL) → Long. Lệnh của bạn đi ngược trình tự: giá về IRL trong khi ERL còn nguyên — nghĩa là bạn Long tại chính cái vùng mà thuật toán sẽ dùng làm bàn đạp để chạy xuống lấy ERL. Không phải "xui", mà là vào lệnh ngược pha của chu kỳ IRL↔ERL.

### 9.2. Đào sâu root cause: cơ chế "nhiên liệu" của cú quét

Ba tầng cơ chế khiến cú quét xuyên range **dự đoán được**:

1. **Bản đồ stop công khai.** Entry cluster của đám đông (và của bạn) nằm tại CE/0.705 — điểm hợp lưu ai học ICT cũng vẽ ra được. Stop của toàn bộ cụm Long đó nằm ngay dưới cạnh dưới FVG (~1.7084–1.7087). Dưới nữa là khoảng trống hoàn toàn cho tới ERL 1.70592. Với một thuật toán tìm thanh khoản, đây là hai pool xếp thẳng hàng — **một cây displacement giảm duy nhất gom được cả hai trong một nhịp**.
2. **Ba lần test SL trải 14 giờ = absorption, không phải accumulation.** Giá test đáy gần SL 3 lần qua phiên Á và đầu London mà không bật lên nổi — nghĩa là bid tại vùng này đang bị **hấp thụ dần**, không phải được gom để đẩy lên. Một POI thật sự được respect thường cho phản ứng displacement rời khỏi vùng trong 1-2 lần test đầu.
3. **Time-based red flag.** Một entry trigger cấp M5 mà 14 giờ chưa được "trả lời" (không chạy về TP, cũng chưa hit SL) tự nó là tín hiệu setup chết lâm sàng. Trigger M5 đúng thường được resolve trong chính kill zone đó hoặc kill zone kế tiếp. Đề xuất rule bổ sung: **time-stop cho entry M5 — nếu sau 2 kill zone liên tiếp giá vẫn dập dềnh quanh entry, thoát thủ công tại breakeven/loss nhỏ thay vì để lệnh phơi qua nhiều phiên.**

### 9.3. Pattern chung với 3 lệnh thua còn lại (họ lỗi "Unswept Liquidity Path")

| Lệnh | First error | Pool chưa-bị-lấy gần nhất nằm đâu so với entry? | SL có nằm trong đường giá đi lấy pool đó? |
|---|---|---|---|
| **GBPUSD 2014-07-17 Long (file này)** | sweep | SSL/ERL = range low 1.70592, ngay DƯỚI | **Có** |
| [[01 - Loss - XAUUSD - 2014-05-19 - Short]] | poi | OB 0.786 + BSL phía TRÊN BB | **Có** (SL 1301.789 nằm dưới OB) |
| [[02 - Loss- XAUUSD- 2014-05-14- Short]] | poi (SL) | Phần còn lại của chính RB (0.705→RB high) phía TRÊN | **Có** (SL = RB low, trong vùng phản ứng hợp lệ) |
| [[02 - Loss- EURUSD - 2021-05-07- Short]] | draw | BSL = OB 1.21296–1.21227 phía TRÊN | **Có** |

**4/4 lệnh thua gần nhất là cùng một họ lỗi**, chỉ khác lớp vỏ: SL luôn được đặt **bên trong đường đi tới pool thanh khoản chưa bị lấy** — lúc thì ERL cấu trúc (file này), lúc thì POI sâu hơn chưa test (XAU 19/5), lúc thì phần thân còn lại của chính POI (XAU 14/5), lúc thì BSL external (EURUSD). Đây không còn là 4 bài học rời rạc — đây là **một lỗ hổng quy trình duy nhất** cần một gate duy nhất để vá. Chi tiết và checklist: [[13 - Mistake - Trading Into Unswept Liquidity]].

---

### Liên kết

- Model: [[01 - ICT 2022 Model]]
- Khái niệm: [[13 - FVG  - Fair Value Gap|FVG]] · [[17 - Inverse Fair Value Gap - iFVG|iFVG]] · [[10 - Consequent Encroachment (Mean Threshold)|Consequent Encroachment]] · [[26 - OTE - Optimal Trade Entry|OTE]] · [[21 - Market Structure Shift|MSS]] · [[20 - Liquidity Sweep|Liquidity Sweep]] · [[27 - Premium Discount|Premium Discount]] · [[12 - Dealing Range|Dealing Range]] · [[18 - Kill Zones|Kill Zones]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]]
- Lệnh so sánh: [[01 - Win - GBPUSD - 2014-06-25 - Long]] (lỗi entry NÓNG — lần này entry chuẩn nhưng setup sai chỗ)
- Dashboard: [[_POI Analytics Dashboard]] · [[_Backtest Dashboard]]
- Template: [[Backtest template - POI & Step Decision (ICT 2022)]]
- Mistake liên quan: [[02 - Mistake - Enter before liquidity sweep]] · [[13 - Mistake - Trading Into Unswept Liquidity]] (note tổng hợp pattern 4 lệnh thua — thay cho đề xuất "Entry INTO liquidity" trước đây)
