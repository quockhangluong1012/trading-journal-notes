---
type: daily-summary
date: 2026-07-13
days_to_prop_exam: 178
exam_target: 2027-01-07
backtests_logged: 1
trades_logged: 0
concepts_reviewed: 1
mistakes_triggered: []
net_r_today: "+2.89R (backtest NAS100; không có lệnh live)"
tags: [daily-summary, prop-firm-prep]
---

# 🌙 Daily Summary — 2026-07-13

> [!info] Đếm ngược
> - **178 ngày** còn lại tới mốc tự đặt **2027-01-07** (song song **FTMO 10K$** + **The5ers High Stakes 10K$** — hai track độc lập, KHÔNG gộp luật).
> - **Giai đoạn hiện tại:** Giai đoạn 1 — Nền tảng ([[01 - Roadmap]]) — ưu tiên (1) nhật ký sạch, (2) mẫu backtest lớn có chấm điểm, (3) cắt lỗi lặp. *Số lượng lệnh live KHÔNG phải ưu tiên lúc này.*
> - **Theme hôm nay:** *Dứt điểm rào cản admin cuối + giữ nhịp nền tảng.* Bảng lot size — bị tick-cho-xong nhiều ngày — **hôm nay đã là file THẬT có số**. Song song: backtest sang **ngày thứ 8 liên tiếp** với **NAS100 (non-EURUSD thứ 2)**, và concept [[35 - Aggressive Displacement Entry]] lên **`tested`**. Một ngày sạch, đúng trọng tâm Giai đoạn 1.

> [!warning] ⚠️ Cảnh báo — 1 điểm duy nhất, đã đặt đúng khung
> Hôm nay **không có lỗi kỷ luật mới** (backtest Grade A followed_plan Yes, không mistake nào bị kích hoạt, không overtick nghiêm trọng). Điểm cần nêu là **cơ cấu**, không phải lười:
> - **0 lệnh live trong 25 ngày** (gần nhất `Loss - 01 - Trade 2026-06-18 NDX Short`). Trong Giai đoạn 1 điều này **chấp nhận được** — roadmap không ưu tiên volume live. NHƯNG đây là **biến số DUY NHẤT chưa được kiểm chứng** cho cả hai challenge: mọi edge đang được xác nhận trên replay/backtest, chưa có bằng chứng execution dưới áp lực luật quỹ + cảm xúc thật. Càng gần 2027-01-07 thì "chưa từng thực chiến" càng là rủi ro lớn nhất, không phải số lượng backtest.
> - **Hai track challenge vẫn 0/8 cột mốc mỗi track.** Dù prep hôm nay có chuyển động thật (lot size), chưa cột mốc Giai đoạn 0 nào ĐÓNG được (cột mốc "Chuẩn bị" đòi trọn: mẫu backtest ≥100 + playbook thành văn). Đây là nơi cần chuyển "động tác lẻ" thành "cột mốc hoàn chỉnh" trong 5 tháng tới.
> - Việc nhỏ còn treo: mục **5. Lesson Learned** của backtest hôm nay **bỏ trống**; task tick [[42 - SMT Divergence]] nhưng note chưa đổi `last_reviewed` (overtick nhẹ).

## 📚 Học hôm nay

- **[[35 - Aggressive Displacement Entry]] → `tested`** (`last_reviewed` & `updated` = 2026-07-13). Đây là chuyển động learning THẬT duy nhất có bằng chứng hôm nay → nhóm `tested` từ 6 lên **7 concept**. Ý nghĩa: chốt định lượng "displacement THẬT" (thân nến đủ mạnh, phá cấu trúc nội bộ, để lại FVG) làm **gate chất lượng tín hiệu** trong 4-gate pre-trade — trực tiếp trị lỗi timing [[08 - Mistake - Weak Displacement]] và củng cố bước Displacement của chuỗi Sweep → Displacement → MSS → FVG/OB → Entry. Backtest NAS100 hôm nay chính là một ứng dụng của gate này (có displacement H1 rõ tạo FVG).
- **Đếm trạng thái concept hiện tại:** 51 note → **17 seed / 27 developing / 7 tested / 0 mastered** (developing 28 → 27, tested 6 → 7 do #35 lên hạng).
- ⚠️ **Overtick cần ghi nhận:** file task tick `[x]` cho ôn [[42 - SMT Divergence]], nhưng frontmatter note vẫn `last_reviewed: 2026-07-11` → **không tính là học hôm nay**. Mục "đẩy 1 concept seed → developing" (tuỳ chọn) cũng chưa làm (seed vẫn 17). Không nghiêm trọng, nhưng nhắc để giữ kỷ luật tick trung thực.

## 📊 Backtest hôm nay

**1 backtest mới** — `04 - Backtesting/2026-07-13/01 - Win - NAS100 - 2026-04-02- Long.md`

| Trường | Giá trị |
|---|---|
| Symbol / Position | **NAS100 / Long** (⭐ non-EURUSD thứ 2) |
| Dữ liệu | 2026-04-02, phiên New York |
| Result / Grade | **Win / A** |
| HTF bias | Bullish — **bias_correct: Yes** |
| POI | FVG (H1) |
| Sweep / Displacement / MSS / FVG valid | Yes / Yes / Yes / Yes |
| Entry / SL / TP | 23.552,4 / 23.394,3 / 24.009 |
| R_planned / R_multiple | **2,89 / 2,89** (khớp) |
| followed_plan | **Yes** |

**Phân tích chuỗi (Step 3):**
- **Bias:** đúng chiều. D1 quét SSL/old lows → reclaim → displacement bullish + FVG D1; giá trong Discount của Dealing Range D1. H1 hình thành MSS, POI = FVG H1 trong Discount. Bias HTF được xác nhận trước khi tìm entry ✅ (trị đúng lỗi [[09 - Mistake - Wrong daily bias]]).
- **Chuỗi entry:** ĐỦ và đúng thứ tự — Liquidity Sweep (SSL D1 + quét CE FVG) → Displacement H1 (tạo FVG) → **MSS M5** lúc 19:20 → retrace về CE FVG mới → Entry. Không khâu nào gãy. Đáng khen: có nhịp giá chạm FVG đầu **KHÔNG vào** vì chưa có sweep + displacement + MSS M5 → kiên nhẫn chờ đúng setup (ngược hẳn lỗi FOMO Grade D ngày 07-08).
- **SL/TP:** SL dưới FVG H1 (vùng invalidation hợp lý), TP tại EQH M15 (24.084) trùng CE FVG D1 → mục tiêu là thanh khoản đối diện hợp lý. RR 2,89 ≥ 1:2 ✅.
- **Tâm lý/root cause thắng:** kỷ luật chờ đồng bias đa khung + chờ CISD/MSS trước khi vào — đúng rule "No MSS No Entry".
- ⚠️ **Điểm chưa hoàn thiện:** mục **5. Lesson Learned** (5.1 root cause / 5.2 pattern / 5.3 rule Playbook) **bỏ trống**; mục 4 tự chấm "90% khớp mô hình" và bỏ ngỏ câu "vào tại cạnh hay tại CE" → cần thêm dữ liệu. Task yêu cầu điền Lesson Learned trong ngày → **việc này chưa xong**, đưa sang mai.

**Tổng hợp ngày:** 1 backtest / 0 lệnh live. **1 Win / 0 Loss / 0 BE**, net **+2,89R** (backtest). Chất lượng execution **tiếp tục xu hướng tốt**: 3 note gần nhất (07-11 EURUSD Win A, 07-12 GBPUSD Win A R3,4, 07-13 NAS100 Win A R2,89) đều Grade A, followed_plan Yes ở 2/3 gần nhất — vượt hẳn giai đoạn đầu tháng có Grade D FOMO (07-08) và lệnh out-of-KZ (07-10).

## 💹 Live Trade hôm nay

**Không có lệnh live nào được log hôm nay.** Thư mục `05 - Live Trading Journal/Trades/2026/07/` chưa tồn tại — tháng 7 chưa có lệnh live nào. Lệnh gần nhất: **2026-06-18** (`Loss - 01 - Trade 2026-06-18 NDX Short`) → **25 ngày** không có lệnh live. Trong Giai đoạn 1 đây không phải "thất bại của ngày", nhưng là biến số chưa kiểm chứng — xem ⚠️ Cảnh báo.

## 🧠 Phân tích lỗi & tâm lý

- **Mistakes bị kích hoạt hôm nay: KHÔNG (danh sách rỗng).** Không có lệnh live để tính vào [[02 - Mistake Frequency Dashboard]]; backtest NAS100 duy nhất là Grade A, followed_plan Yes, đủ chuỗi — không mắc lỗi nào.
- **Top-3 lỗi hiện tại (đếm trên trade live, KHÔNG đổi hôm nay):**
  1. [[06 - Mistake - Not Have Market Structure Shift]] — **14 lần.** Vào lệnh khi chưa có nến đóng cửa phá protected swing bằng displacement ("sweep là câu hỏi, MSS là câu trả lời"). Hôm nay backtest chờ đủ MSS M5 → **không tái phạm**.
  2. [[09 - Mistake - Wrong daily bias]] — **7 lần.** Xác định sai chiều bias HTF trước khi tìm setup. Backtest hôm nay bias_correct = Yes → ngược lỗi này.
  3. [[07 - Mistake - Risk more than 0.5% total account]] — **5 lần.** Rủi ro vượt 0,5% tài khoản. Note lot size làm hôm nay chính là công cụ phòng lỗi này (tra nhanh lot cho $50 = 0,5%).
- **Tâm lý ngày:** kỷ luật, kiên nhẫn (bỏ qua nhịp chạm FVG đầu chưa đủ điều kiện). Không có dấu hiệu FOMO/revenge.

## 🎯 Đối chiếu mục tiêu

| Goal | Progress (frontmatter) | Cột mốc | Số thật hôm nay | Nhận định |
|---|---|---|---|---|
| [[Pass FTMO first package challenge (10K$)]] | 0% | 0/8 | Lot size note THẬT xong (bước 3 G0) | Prep nhích thật, nhưng cột mốc "Chuẩn bị" đòi trọn gói → **chưa tick**. Progress 0% **khớp** cột mốc 0/8. |
| [[Pass The5er first package challenge (10k$)]] | 0% | 0/8 | Lot math dùng chung xong; phần riêng The5ers CHƯA | Thiếu cột "ngày có lãi = +50$" + paper-sim daily drawdown từ equity đóng cửa hôm trước. Progress 0% khớp 0/8. |
| [[Build a statistically validated backtest sample]] | **6%** | 0/4 | **13/200 backtest = 6,5%** | Prose đã sync 12 → 13. Frontmatter giữ 6% (làm tròn xuống, không thổi phồng). Nhịp 0,65/ngày > cần 0,53/ngày → **trên nhịp** cho due 2027-06-30. |
| [[Master the ICT 2022 Model]] | 30% | 0/5 | **13 setup, 11W/2L ≈ 85%** (n=13 nhỏ) | Prose sync 12 → 13. ⚠️ **Mismatch tồn tại:** progress ghi 30% nhưng cột mốc **0/5** — 30% là ước lượng tay, chưa khớp checkbox nào. Ràng buộc thật là win rate >55% với n đủ lớn — chưa đủ dữ liệu. |
| [[Hold daily journaling and process discipline]] | **50%** (sync từ 40%) | 2/4 | **Ngày journaling thứ 10; chuỗi 9 ngày liên tiếp** | ✅ Đã **sửa mismatch**: frontmatter 40 → 50 cho khớp cột mốc 2/4 (Khang tick #1+#2 hôm 07-12). Cột mốc #3 (4 tuần) / #4 (8 tuần) cần thêm thời gian. Track **khoẻ nhất**. |
| [[Cut my top 3 repeated mistakes]] | 20% | 0/4 | Không đổi (0 lệnh live) | ⚠️ Log gần nhất **07-08 = 5 ngày** không có dòng mới — nhưng đây là **stale hợp lệ**: tần suất lỗi đo trên lệnh live, mà 25 ngày không có lệnh nào → **không thêm dòng rỗng** (Step 6). progress 20% > cột mốc 0/4 (mismatch tay tồn từ đầu). |

**Verdict pace (tới 2027-01-07 = 178 ngày):**
- **Ưu tiên #1 (nhật ký):** ✅ trên nhịp tuyệt đối — 9 ngày liên tiếp, thói quen đã hình thành.
- **Ưu tiên #2 (mẫu backtest):** ✅ trên nhịp — 0,65/ngày. Ở nhịp này, tới 2027-01-07 sẽ có ~13 + 178×~0,6 ≈ **120+ backtest** → qua mốc 50 và tiến sát 100 setup trước ngày readiness. Rào cản thật KHÔNG phải số lượng mà là **(a) mẫu vẫn 11/13 EURUSD** (dù non-EURUSD nhích lên 2/13), **(b) n quá nhỏ để chốt win rate >55%**.
- **Ưu tiên #3 (cắt lỗi):** ⏸️ đứng yên hợp lệ — không có lệnh live để đo.
- **Hai track challenge:** on-track **theo lịch** (178 ngày dư cho chuỗi prep → demo → mua gói → 2 phase) nhưng **0/8 cột mốc mỗi track** cho thấy chưa chuyển prep thành cột mốc đóng. Rủi ro cấu trúc = **0 lệnh live 25 ngày** (execution chưa kiểm chứng).

## 📈 Cập nhật Nhật ký tiến độ

Đã thêm **1 dòng 2026-07-13** vào **5/6 goal** có chuyển động thật hôm nay:
- ✅ **[[Build a statistically validated backtest sample]]** — +1 backtest NAS100 (13/200 = 6,5%), chuỗi ngày thứ 8; prose sync 12 → 13; frontmatter progress giữ 6 (làm tròn xuống).
- ✅ **[[Master the ICT 2022 Model]]** — +1 setup (13, 11W/2L ≈ 85%); prose sync 12 → 13; ghi nhận concept #35 lên `tested`.
- ✅ **[[Hold daily journaling and process discipline]]** — ngày journaling thứ 10 / chuỗi 9 ngày; **sửa frontmatter progress 40 → 50** khớp cột mốc 2/4.
- ✅ **[[Pass FTMO first package challenge (10K$)]]** — ghi nhận note lot size THẬT (gỡ overtick nhiều ngày), bước 3 Giai đoạn 0; progress giữ 0% (cột mốc "Chuẩn bị" chưa đủ điều kiện).
- ✅ **[[Pass The5er first package challenge (10k$)]]** — ghi nhận phần lot math dùng chung xong nhưng phần riêng The5ers (ngày-có-lãi + prior-close drawdown) chưa; progress giữ 0%.
- ⏸️ **[[Cut my top 3 repeated mistakes]]** — **KHÔNG thêm dòng**: không có lệnh live, không mistake nào kích hoạt, tần suất không đổi → thêm dòng sẽ là dòng rỗng (đúng Step 6).

## 🔭 Việc cần làm ngày mai

1. **Điền mục 5. Lesson Learned cho backtest NAS100 07-13** (root cause tại sao thắng, pattern lặp lại, rule cần thêm vào Playbook) — việc này bị bỏ trống hôm nay, là món "nợ trong ngày" nhỏ nhất cần đóng đầu tiên.
2. **Thêm phần The5ers vào note lot size** `03 - Playbooks/3.1 - Checklists/Lot size 10K.md`: cột/ghi rõ ngưỡng **"ngày có lãi = +50$ (0,5%)"** + một ví dụ **daily drawdown tính từ equity đóng cửa hôm trước** → đóng bước 2+3 Giai đoạn 0 cho track The5ers (hiện chỉ FTMO được phủ đủ).
3. **Giữ chuỗi backtest sang ngày thứ 9** — ưu tiên tiếp **NAS100/XAUUSD** để đưa non-EURUSD lên **3/13** (mẫu vẫn 11 EURUSD). Bám 4-gate + chỉ tính entry sau nến đóng cửa phá bằng displacement thật.
4. **Learning trung thực:** nếu ôn [[42 - SMT Divergence]] thì cập nhật `last_reviewed` cho khớp (bù overtick hôm nay); ứng viên nâng `tested` kế tiếp nếu dẫn được ≥2 backtest xác nhận.
5. **Nếu có phiên London/NY và muốn vào lệnh live:** kiểm 3 gate lỗi top-3 TRƯỚC entry (có MSS rõ / bias HTF đúng / lot ≤0,5% tra từ note mới) — 25 ngày không thực chiến, mọi lệnh đều là dữ liệu quý cho biến số chưa kiểm chứng.
6. **Kỷ luật tick:** chỉ `[x]` khi có bằng chứng thật (file tồn tại / `last_reviewed` đổi) — hôm nay đã tốt hơn 07-12, giữ vậy.

## 🔗 Liên kết

[[00 - Goal Dashboard]] · [[01 - Roadmap]] · [[02 - Skill Metrics]] · [[_Backtest Dashboard]] · [[02 - Mistake Frequency Dashboard]] · [[03 - Performance Dashboard]] · [[04 - Process Quality Dashboard]]
