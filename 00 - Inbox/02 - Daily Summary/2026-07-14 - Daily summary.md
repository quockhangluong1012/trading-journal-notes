---
type: daily-summary
date: 2026-07-14
days_to_prop_exam: 177
exam_target: 2027-01-07
backtests_logged: 3
trades_logged: 0
concepts_reviewed: 2
mistakes_triggered: ["[[Mistake - Stop loss đặt sai vị trí]] (chưa có note)", "[[Mistake - Sai lệch dữ liệu nhật ký]] (chưa có note)"]
net_r_today: "+4.87R (backtest: +2.9 / −1 / +2.97; không có lệnh live)"
tags: [daily-summary, prop-firm-prep]
---

# 🌙 Daily Summary — 2026-07-14

> [!info] Đếm ngược
> - **177 ngày** còn lại tới mốc tự đặt **2027-01-07** (song song **FTMO 10K$** + **The5ers High Stakes 10K$** — hai track độc lập, KHÔNG gộp luật).
> - **Giai đoạn hiện tại:** Giai đoạn 1 — Nền tảng ([[01 - Roadmap]]) — ưu tiên (1) nhật ký sạch, (2) mẫu backtest lớn có chấm điểm, (3) cắt lỗi lặp. *Số lượng lệnh live KHÔNG phải ưu tiên lúc này.* **Mode: FOUNDATION** (cả 2 goal challenge `Phase 0 - Preparation`, chưa mua gói) → theo dõi lỗi = lỗi **backtest**.
> - **Theme hôm nay:** *Ngày backtest năng suất nhất về SỐ LƯỢNG — nhưng cũng là ngày lộ rõ rủi ro CHẤT LƯỢNG DỮ LIỆU lớn nhất của cả dự án.* 3 backtest XAUUSD (thị trường thứ 3 của mẫu) đưa chuỗi backtest sang **ngày thứ 9**; nhưng 2/3 note bị **nhiễm dữ liệu copy-paste** và 1 lệnh Loss tự chấm A- dù SL đặt sai — hai thứ trực tiếp đe doạ tính hợp lệ của mẫu thống kê.

> [!warning] ⚠️ Cảnh báo — 3 điểm có tên cụ thể (nhịp độ số lượng vẫn khoẻ)
> Hôm nay KHÔNG thiếu hoạt động (3 backtest + 2 concept + journaling ngày thứ 11). Cảnh báo nằm ở **chất lượng dữ liệu** và **vòng chưa đóng**, không phải lười:
> 1. **[Nghiêm trọng nhất] Nhiễm dữ liệu backtest — [[Mistake - Sai lệch dữ liệu nhật ký]] (note CHƯA tồn tại):** cả 2 note Win hôm nay bị lẫn số liệu do copy từ template/lệnh cũ. Note `01 - Win` tự ghi trong mục 5.2: `htf_bias` từng lẫn Bullish (lệnh là Short), heading lẫn "Long/NAS100", số Dealing Range lẫn số NAS100 (24.570/22.822), POI lẫn giá EURUSD, ngày lẫn 2014↔2026. Note `03 - Win` phải đính chính Entry/SL/TP/R sai (1301.562→1306.90, R 2.9→2.97). **Với backtest, dữ liệu bẩn = mẫu thống kê vô nghĩa ("garbage in, garbage out")** — chính các note tự gọi đây là rủi ro số 1 của dự án. Đây là **pattern lặp lại** (đã xuất hiện rải rác nhiều ngày) → cần diệt tận gốc bằng rule R-BT-01/toàn vẹn dữ liệu.
> 2. **Outcome bias khi chấm grade:** `02 - Loss` tự chấm **A-** dù root cause là **SL đặt ngay mép dưới POI (RB low = 1302.715), bên trong vùng chop, KHÔNG phải trên invalidation thật (đóng trên 1304.109)** — chính note có "mentor note" đề nghị hạ **B/B-**. `01 - Win` tự chấm A nhưng lesson kết luận nên là **A-** vì file lỗi dữ liệu. Grade thổi phồng làm hỏng đúng ràng buộc thật của [[Master the ICT 2022 Model]]: **win rate/expectancy**, không phải số lượng.
> 3. **Vòng #2 từ task sáng nay CHƯA đóng:** cột mốc "Chuẩn bị" ở [[Pass FTMO first package challenge (10K$)]] và [[Pass The5er first package challenge (10k$)]] vẫn `[ ]` → **0/8**, và **chưa có dòng "Nhật ký tiến độ" 2026-07-14** ở cả hai goal (dòng cuối vẫn 07-13). Log 2 track này chỉ còn **2 ngày nữa (07-16)** là chạm ngưỡng "stale 3 ngày". *(Vòng #1 — overtick [[42 - SMT Divergence]]: `last_reviewed` vẫn `2026-07-11`, tức đã để nguyên = coi như chưa ôn — đây là cách xử lý trung thực đúng chỉ dẫn task, không phải lỗi mới.)*
> **Standing note (cấu trúc, không phải lỗi hôm nay):** **26 ngày** không có lệnh live (gần nhất `Loss - 01 - Trade 2026-06-18 NDX Short`). Chấp nhận được trong FOUNDATION, nhưng là **biến số DUY NHẤT chưa kiểm chứng** cho cả hai challenge.

## 📚 Học hôm nay

**2 concept có bằng chứng thật (`last_reviewed: 2026-07-14`):**

- **[[21 - Liquidity Void]]** (`developing`, `last_reviewed` 07-14) — góc ôn: phân biệt *liquidity void* (dải giá bị displacement bỏ qua, gần như không giao dịch 2 chiều) với FVG thường; dùng "void đủ sâu" làm bằng chứng phụ cho gate **Signal quality**. Ứng dụng ngay trong `01 - Win`: giá quét lên **CE của Liquidity Void** (tàn dư nhịp giảm 7/5) rồi bị từ chối tại Premium.
- **[[28 - Rejection Block]]** (`seed → developing`, `last_reviewed` & `updated` = 07-14) — ⭐ **nâng hạng thật hôm nay.** Định nghĩa RB như PD array entry *thay thế* OB khi không có OB sạch (dùng đuôi nến rejection thay thân). Được **áp dụng trực tiếp** làm POI trong `02 - Loss` → đây là "học đi đôi với hành": vừa nâng concept, vừa test nó trên một setup thật (và học được bài học SL từ chính lệnh thua đó).

**Đối chiếu task sáng:** [[06 - Breakaway Gap]] (tuỳ chọn) **không** được ôn — `[ ]` đúng thực tế, không tick khống. Đếm concept `tested` **không đổi** hôm nay (vẫn 7); nhưng nhóm `developing` +1 do #28 lên hạng.

## 📊 Backtest hôm nay

**3 backtest mới** trong `04 - Backtesting/2026-07-14/` — **tất cả XAUUSD Short** (⭐ thị trường thứ 3 của mẫu, sau EURUSD/GBPUSD/NAS100). Cùng một context D1/H1 Bearish (dữ liệu tháng 5/2014), khác nhau ở POI và cách vào lệnh:

| # | Note | Result / Grade tự chấm | POI | Sweep→Disp→MSS→FVG | R_planned / R_multiple | followed_plan |
|---|---|---|---|---|---|---|
| 01 | Win — XAUUSD 2014-05-12 Short | **Win / A** (nên A-) | [[13 - FVG  - Fair Value Gap\|FVG]] H1 | Yes / Yes / Yes / Yes | 2.9 / **2.9** | Yes |
| 02 | Loss — XAUUSD 2014-05-14 Short | **Loss / A-** (nên B/B-) | [[28 - Rejection Block\|Rejection Block]] H1 | Yes / Yes / Yes / Yes | 3.22 / **−1** | Yes |
| 03 | Win — XAUUSD 2014-05-14 Short | **Win / A** | [[03 - Balanced Price Range\|BPR]] M5 (trên CE của FVG H1) | Yes / Yes / Yes / Yes | 2.97 / **2.97** | Yes |

**Phân tích chuỗi (Step 3):**

- **`01 - Win` (FVG entry):** Bias D1 Bearish dựng từ 4 tầng confluence (sweep SSL → Displacement+OB → Bearish MSS+FVG → Premium của Dealing Range) — không cảm tính. Chuỗi ĐỦ và đúng thứ tự: quét CE của Liquidity Void → M1 Bearish displacement tạo MSS + 2 FVG → phân biệt **FVG1 (trước MSS, bỏ)** vs **FVG2 (sau MSS, vào)** tại CE trong OTE. Entry đẹp ở ~0.618, SL gọn ~2.5 giá → R 2.9. **Điểm cần xác minh:** entry ở 0.618 trong khi POI H1 (OB) nằm cao hơn ~0.786 → **SL đang neo theo STH của M1, không theo invalidation của POI H1**; thắng nhờ LTF confirm sớm, nhưng nếu giá retrace sâu về OB thì SL 1304 đã bị quét. Đây là đánh đổi "entry sớm, R cao" vs "chờ POI chính, SL an toàn" — cần thêm mẫu. **Lỗi dữ liệu:** file lẫn số liệu instrument khác (xem ⚠️ Cảnh báo #1) → grade công bằng là **A-**, không phải A.
- **`02 - Loss` (Rejection Block entry):** **Bài học đắt nhất và giá trị nhất của ngày.** Bias đúng (Bearish), phân tích top-down tốt, nhưng thua vì **SL đặt sai vị trí**: neo vào swing high nhỏ M1 (1302.715 = mép dưới RB) thay vì trên invalidation thật của RB H1 (đóng trên 1304.109). SL nằm *bên trong* vùng phản ứng còn hợp lệ → một cú retrace bình thường trong OTE quét stop trước khi luận điểm short kịp chạy ("stopped out on noise inside the POI"). Mâu thuẫn logic cốt lõi: **định nghĩa invalidation theo H1 nhưng đặt SL theo M1**. Hai cảnh báo bị bỏ qua: (a) M5 không tạo FVG (phản ứng bán không sạch — đáng lẽ no-trade), (b) 2 nến Bullish displacement mạnh đẩy vào POI (bán ngược momentum chưa hấp thụ). → R:R 3.22 "đẹp" chỉ là **sản phẩm phụ của SL quá chật**, không phải bằng chứng chất lượng. Rule rút ra: **R do SL đúng quyết định có vào hay không, không phải ngược lại**; SL trong POI → chặn trần grade ở B.
- **`03 - Win` (BPR M5 entry):** Lệnh chất lượng thật nhờ **nested confluence**: D1 Bearish → H1 Premium/OTE → **H1 FVG là POI chính** → M5 **BPR** (overlap 2 FVG ngược chiều) trùng ngay trên **CE của H1 FVG** → entry tại CE BPR. Không entry sớm, để confluence tự xếp chồng. **Điểm siết lại (chính note tự nêu):** "quét cạnh trên FVG" ≠ liquidity sweep — thanh khoản thật bị quét là **swing high phía trên**; ghi sai khái niệm này lặp lại sẽ làm hỏng thống kê "sweep → win rate". Note đã tự đính chính số liệu sai (callout "Toàn vẹn dữ liệu — ĐÃ SỬA").

**Tổng hợp ngày:** 3 backtest / 0 lệnh live. **2 Win / 1 Loss / 0 BE**, net **+4.87R** (backtest: +2.9 / −1 / +2.97). Chuỗi backtest sang **ngày thứ 9 liên tiếp** (07-06→07-14). Về **execution kỹ thuật**, cả 3 đều đủ chuỗi ICT 2022 và `followed_plan: Yes`. Về **chất lượng ghi chép/chấm điểm**, đây là ngày yếu nhất gần đây: 2/3 nhiễm dữ liệu + 2/3 grade thổi phồng → xu hướng số lượng tốt nhưng cảnh báo phải siết kỷ luật dữ liệu để mẫu còn giá trị thống kê.

## 💹 Live Trade hôm nay

**Không có lệnh live nào được log hôm nay.** Thư mục `05 - Live Trading Journal/Trades/2026/07/` vẫn chưa tồn tại — tháng 7 chưa có lệnh live nào. Lệnh gần nhất: **2026-06-18** (`Loss - 01 - Trade 2026-06-18 NDX Short`) → **26 ngày** không có lệnh live. Trong Giai đoạn 1/FOUNDATION đây không phải "thất bại của ngày" (roadmap không ưu tiên volume live), nhưng là biến số chưa kiểm chứng — xem ⚠️ Cảnh báo (standing note).

## 🧠 Phân tích lỗi & tâm lý

**Lỗi backtest bị kích hoạt hôm nay (FOUNDATION mode → theo dõi lỗi backtest, không phải live):**

- **[[Mistake - Stop loss đặt sai vị trí]]** *(note CHƯA tồn tại trong `06 - Mistake Database`)* — restated: neo SL vào swing nhỏ khung entry (mép POI) thay vì trên **invalidation thật của POI đang giao dịch** → bị quét bởi nhiễu bình thường trong OTE chứ không phải bởi tín hiệu phủ định luận điểm. Nguồn: `02 - Loss` hôm nay. **Đây là lỗi mới, KHÔNG nằm trong top-3 backtest hiện tại.**
- **[[Mistake - Sai lệch dữ liệu nhật ký]]** *(note CHƯA tồn tại)* — restated: copy note từ template/lệnh cũ khiến symbol/bias/số Dealing Range/POI/ngày lẫn của instrument khác; Summary table ≠ frontmatter. Nguồn: `01 - Win` và `03 - Win` hôm nay. **Đây là rủi ro hệ thống với cả mẫu backtest, không chỉ một lệnh.**

**Đối chiếu top-3 lỗi backtest hiện tại** ([[06 - Mistake - Not Have Market Structure Shift]], [[08 - Mistake - Weak Displacement]], [[09 - Mistake - Wrong daily bias]]):
- **06 (No MSS):** KHÔNG tái phạm — cả 3 lệnh đều có MSS đóng cửa rõ.
- **09 (Wrong bias):** KHÔNG tái phạm — cả 3 `bias_correct: Yes` (Bearish đúng chiều).
- **08 (Weak Displacement):** *cận biên* — `02 - Loss` có tín hiệu "M5 không tạo FVG / phản ứng bán không sạch" (họ hàng với displacement yếu) nhưng root cause được ghi là SL, không phải displacement. Không tính là tái phạm chính thức, nhưng đáng để ý.
→ **Hai lỗi hôm nay (SL sai vị trí + nhiễm dữ liệu) đều NẰM NGOÀI top-3 hiện tại** → tín hiệu top-3 nên được xem lại khi có note mistake mới, và cần **tạo 2 note mistake còn thiếu** để dashboard đếm được.

**Tâm lý ngày:** kỷ luật vào lệnh tốt (chờ đủ chuỗi, `followed_plan` cả 3), có tinh thần tự phản biện mạnh (mục 5 các note tự vạch lỗi thay vì bào chữa — đúng tinh thần "a good loss beats a bad win"). Điểm rò rỉ là **kỷ luật ghi chép/chấm điểm**, không phải tâm lý vào lệnh.

## 🎯 Đối chiếu mục tiêu

| Goal | Progress (frontmatter) | Cột mốc | Số thật hôm nay | Nhận định |
|---|---|---|---|---|
| [[Pass FTMO first package challenge (10K$)]] | 0% | **0/8** | Không có deliverable mới hôm nay | Lot size đã có (07-13). Cột mốc "Chuẩn bị" đòi trọn (backtest ≥100 + playbook) → chưa tick. Progress 0% **khớp** 0/8. ⚠️ **Vòng #2 chưa đóng:** chưa tick cột mốc + chưa có dòng log 07-14. Log dừng 07-13 (1 ngày). |
| [[Pass The5er first package challenge (10k$)]] | 0% | **0/8** | Phần riêng The5ers vẫn CHƯA làm | Thiếu cột "ngày có lãi = +50$ (0,5%)" + paper-sim daily drawdown từ **equity đóng cửa hôm trước**. Progress 0% khớp 0/8. Cùng tình trạng vòng #2 chưa đóng, log dừng 07-13. |
| [[Build a statistically validated backtest sample]] | **6% → 8%** (sync) | 0/4 | **16/200 backtest = 8%** | +3 backtest hôm nay (13→**16**). Prose "Hiện tại" sync 13→16; frontmatter `progress` 6→**8**. Nhịp thô 16/21 ngày ≈ **0,76/ngày** > nhịp cần ~0,53/ngày (due 2027-06-30) → **trên nhịp**. ✅ Đa dạng thị trường: nay **11 EURUSD + 1 GBPUSD + 1 NAS100 + 3 XAUUSD** → non-EURUSD lên **5/16**. Cột mốc "50 backtest" vẫn 0/4. |
| [[Master the ICT 2022 Model]] | **30%** | **0/5** | **16 setup, 13W/3L ≈ 81%** (n=16 nhỏ) | +3 setup (13→16). Prose sync 13→**16 (13W/3L ≈ 81%)**. ⚠️ **Mismatch tồn tại:** progress ghi 30% nhưng cột mốc **0/5** — 30% là ước lượng tay. Ràng buộc thật = **win rate >55% với n đủ lớn**; win% giảm nhẹ (85%→81%) do +1 Loss, vẫn > ngưỡng nhưng n=16 chưa kết luận được. ⚠️ Grade 2/3 note hôm nay thổi phồng → nếu chấm đúng (A-, B, A) thì chất lượng mẫu thấp hơn con số nhìn thấy. |
| [[Hold daily journaling and process discipline]] | **50%** | **2/4** | **Ngày journaling thứ 11; chuỗi 10 ngày liên tiếp** (07-05→07-14) | Chuỗi dài nhất từ trước tới nay. Progress 50% khớp cột mốc 2/4. Cột mốc #3 ("4 tuần liên tiếp") — chuỗi 10 ngày ≈ 1,4 tuần, **chưa chạm**. Track **khoẻ nhất, thói quen đã thành hình.** |
| [[Cut my top 3 repeated mistakes]] | **20%** | 0/4 | Tần suất lỗi live KHÔNG đổi (0 lệnh live) | ⚠️ Log gần nhất **07-08 = 6 ngày** không dòng mới — nhưng là **stale hợp lệ**: tần suất đo trên lệnh live, 26 ngày không có lệnh → **không thêm dòng rỗng** (Step 6). Progress 20% > cột mốc 0/4 (mismatch tay tồn từ đầu). Lưu ý: 2 lỗi backtest mới hôm nay chưa có note → khi tạo note có thể phải xét lại "top-3". |

**Verdict pace (tới 2027-01-07 = 177 ngày):**
- **Ưu tiên #1 (nhật ký):** ✅ **trên nhịp tuyệt đối** — 10 ngày liên tiếp, thói quen đã hình thành.
- **Ưu tiên #2 (mẫu backtest):** ✅ **trên nhịp về số lượng** — 0,76/ngày. Ở nhịp này tới 2027-01-07 sẽ có ~16 + 177×~0,6 ≈ **120+ backtest** → qua mốc 50, tiến sát 100 trước ngày readiness. **NHƯNG rào cản thật không phải số lượng mà là (a) độ sạch dữ liệu** (2/3 note hôm nay nhiễm → nếu tái diễn, mẫu 120 note vẫn "garbage"), **(b) grade trung thực** để win rate phản ánh edge thật, **(c) n vẫn nhỏ** (16) chưa chốt được win rate >55%.
- **Ưu tiên #3 (cắt lỗi):** ⏸️ đứng yên hợp lệ (không có lệnh live để đo) — nhưng xuất hiện **2 lỗi backtest mới** cần đóng gói thành note.
- **Hai track challenge:** on-track **theo lịch** (177 ngày dư cho prep → demo → mua gói → 2 phase) nhưng **0/8 cột mốc mỗi track**, vòng #2 chưa đóng, log 2 ngày (sắp stale). Rủi ro cấu trúc = **0 lệnh live 26 ngày** (execution chưa kiểm chứng).

## 📈 Cập nhật Nhật ký tiến độ

Đã thêm **1 dòng 2026-07-14** vào **3/6 goal** có chuyển động số THẬT hôm nay:
- ✅ **[[Build a statistically validated backtest sample]]** — +3 backtest XAUUSD (13→16/200 = 8%), chuỗi ngày thứ 9, non-EURUSD lên 5/16; prose sync 13→16; frontmatter `progress` 6→8.
- ✅ **[[Master the ICT 2022 Model]]** — +3 setup (13→16, 13W/3L ≈ 81%); prose sync 13→16; ghi nhận grade thổi phồng 2/3 note.
- ✅ **[[Hold daily journaling and process discipline]]** — ngày journaling thứ 11 / chuỗi 10 ngày liên tiếp; progress giữ 50 (khớp 2/4).

**KHÔNG thêm dòng (tránh dòng rỗng — Step 6):**
- ⏸️ **[[Cut my top 3 repeated mistakes]]** — 0 lệnh live, tần suất live không đổi.
- ⏸️ **[[Pass FTMO first package challenge (10K$)]]** và **[[Pass The5er first package challenge (10k$)]]** — không có deliverable mới hôm nay; vòng #2 (tick cột mốc + log) là **việc của Khang tự xác nhận đủ điều kiện**, routine không tự tick khống. *(Ghi rõ ở đây để mai không quên: 07-16 hai log này chạm ngưỡng stale 3 ngày.)*

## 🔭 Việc cần làm ngày mai

1. **[Ưu tiên #1 — diệt rủi ro dữ liệu] Tạo note [[Mistake - Sai lệch dữ liệu nhật ký]]** trong `06 - Mistake Database` (biện pháp đối phó: rule R-BT-01 "làm sạch file trước khi lưu" + checklist "Summary table = frontmatter, số copy trực tiếp từ chart"), và **rà lại 3 note 07-14** đảm bảo symbol/bias/số liệu/ngày đều đúng XAUUSD (đặc biệt `01 - Win`: kiểm `htf_bias`, Dealing Range, POI, năm dữ liệu).
2. **Tạo note [[Mistake - Stop loss đặt sai vị trí]]** (rule: SL luôn neo trên invalidation của POI đang giao dịch + buffer; R do SL đúng quyết định vào/không, không siết SL cho đẹp R). Cân nhắc gắn vào top-3 nếu tái diễn.
3. **Chấm lại grade trung thực cho 2 note hôm nay:** `02 - Loss` A- → **B/B-** (SL trong POI); `01 - Win` A → **A-** (lỗi dữ liệu) — để win rate/expectancy của [[Master the ICT 2022 Model]] phản ánh chất lượng thật.
4. **[Đóng vòng #2] Phản ánh lot size vào 2 goal challenge:** nếu Khang tự đánh giá đủ điều kiện, tick một phần cột mốc "Chuẩn bị" và **log 1 dòng 2026-07-15 THẬT** vào cả FTMO + The5ers (dẫn `[[Lot size 10K]]`), trước khi log chạm stale 07-16. **Đồng thời làm phần RIÊNG The5ers** còn thiếu: ngưỡng "ngày có lãi = +50$" + ví dụ daily drawdown tính từ equity đóng cửa hôm trước.
5. **Giữ chuỗi backtest sang ngày thứ 10** — ưu tiên non-EURUSD (NAS100/GBPUSD/thêm XAUUSD để đủ ~20 mẫu vàng như note `03` đề xuất, kiểm tra buffer SL cho wick/spread vàng). Chỉ tính entry sau nến ĐÓNG CỬA phá bằng displacement thật.
6. **Verify replay cho `02 - Loss`:** sau khi quét SL, giá có xuống TP 1297.51 không? → phân định đây thuần là lỗi SL (đúng hướng, sai vị trí dừng) hay lỗi timing (vào quá sớm).
7. **Kỷ luật tick trung thực:** giữ nguyên cách xử lý [[42 - SMT Divergence]] (không tick khống). Chỉ `[x]` khi có bằng chứng thật (file tồn tại / `last_reviewed` đổi / dòng log thật).

## 🔗 Liên kết

[[00 - Goal Dashboard]] · [[01 - Roadmap]] · [[02 - Skill Metrics]] · [[_Backtest Dashboard]] · [[02 - Mistake Frequency Dashboard]] · [[03 - Performance Dashboard]] · [[04 - Process Quality Dashboard]]
