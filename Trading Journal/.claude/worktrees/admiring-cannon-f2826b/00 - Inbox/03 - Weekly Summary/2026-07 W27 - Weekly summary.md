---
type: weekly-summary
week: 2026-W27
start_date: 2026-06-29
end_date: 2026-07-05
days_to_prop_exam: 186
exam_target: 2027-01-07
backtests_logged_week: 0
trades_logged_week: 0
concepts_reviewed_week: 3
net_r_week: 0
days_with_data: 1
tags: [weekly-summary, prop-firm-prep]
---

# 🗓️ Weekly Summary — 2026-W27 (2026-06-29 → 2026-07-05)

> [!warning] Dữ liệu không đủ cho một rollup đầy đủ
> Tuần 2026-W27 chỉ có **1/7 ngày có Daily Summary** (`2026-07-03`). Bốn ngày đầu tuần (`06-29, 06-30, 07-01, 07-02`) **không có file Daily Tasks lẫn Daily Summary nào** — hệ thống nhật ký tự động chỉ bắt đầu chạy từ `2026-07-03`. Hai ngày còn lại (`07-04, 07-05`) có Daily Tasks (kế hoạch) nhưng **không có Daily Summary** (không có bản ghi việc đã thực sự xảy ra).
>
> Theo đúng guardrail của quy trình này: **không có Daily Summary = không có dữ liệu, không phải "không hoạt động gì."** Vì vậy đây là bản tóm tắt rút gọn, chỉ báo cáo những gì thực sự có bằng chứng, thay vì dựng đủ 6 mục phân tích như một tuần đầy dữ liệu.

## 📊 Những gì thực sự biết được

| Ngày             | Daily Tasks | Daily Summary | Ghi chú                                         |
| ---------------- | ----------- | ------------- | ----------------------------------------------- |
| 2026-06-29 (Mon) | ❌           | ❌             | Không có dữ liệu                                |
| 2026-06-30 (Tue) | ❌           | ❌             | Không có dữ liệu                                |
| 2026-07-01 (Wed) | ❌           | ❌             | Không có dữ liệu                                |
| 2026-07-02 (Thu) | ❌           | ❌             | Không có dữ liệu                                |
| 2026-07-03 (Fri) | ✅           | ✅             | Ngày 1 của hệ thống tự động                     |
| 2026-07-04 (Sat) | ✅           | ❌             | Có kế hoạch, không có bản ghi thực tế đã xảy ra |
| 2026-07-05 (Sun) | ✅           | ❌             | Có kế hoạch, không có bản ghi thực tế đã xảy ra |

**Từ ngày duy nhất có Daily Summary (07-03):** `backtests_logged: 0`, `trades_logged: 0`, `concepts_reviewed: 1` ([[33 - Turtle Soup]] — có bằng chứng frontmatter), `mistakes_triggered: []`, `net_r_today: 0`.

**Suy luận gián tiếp (không phải bằng chứng Daily Summary, nhưng đối chiếu được qua frontmatter các note liên quan trong tuần):**
- **Backtest cả tuần vẫn dừng ở 1 note** (`04 - Backtesting/2026-07-01/...`) — không có note backtest mới nào được tạo trong suốt 06-29→07-05. Nhịp backtest đứt ít nhất từ 07-02 tới hết 07-05 (4 ngày+), theo đúng cảnh báo lặp lại trong cả 3 file Daily Tasks của tuần.
- **Không có lệnh live nào** trong `05 - Live Trading Journal/Trades/2026/07/` (thư mục tháng 7 hoàn toàn trống) và cũng không có ngày nào trong 06/29–06/30. Lệnh gần nhất toàn vault vẫn là `Loss - 01 - Trade 2026-06-18 NDX Short` → 17 ngày không lệnh live tính đến 07-05.
- **3 concept chuyển từ `seed` → `developing` với `updated` nằm trong tuần** (06-29→07-05): [[22 - Mitigation Block]] (`updated: 2026-07-02`), [[33 - Turtle Soup]] (`updated: 2026-07-03`), [[21 - Liquidity Void]] (`updated: 2026-07-03`). Đây là `concepts_reviewed_week: 3` ở frontmatter trên — tính theo bằng chứng frontmatter thật, không tính theo checkbox tick.
  > [!info] Lệch ngày cần lưu ý
  > File Daily Tasks `2026-07-04` ghi các mục này là hoàn thành "hôm nay" (07-04), nhưng `updated` của [[22 - Mitigation Block]] lại là `2026-07-02` — sớm hơn 2 ngày so với ngày được tick. Không tự sửa số liệu này — chỉ nêu ra để Khang tự đối chiếu lại xem có phải tick nhầm ngày hay note chỉ được review lại (không sửa nội dung) nên `updated` không đổi.

## 🎯 Đối chiếu mục tiêu (theo công thức cột mốc, không dùng field `progress` ghi tay)

| Goal | `progress` (frontmatter) | Cột mốc | Đúng theo cột mốc | Khớp? | `phase:` có hợp lý? | Nhật ký tiến độ gần nhất |
|---|---:|---|---:|---|---|---|
| [[Pass FTMO first package challenge (10K$)]] | 0% | 0/8 | 0% | ✅ Khớp | ⚠️ Ghi "Phase 4 - Challenge" nhưng kế hoạch hành động nội bộ vẫn ở "Giai đoạn 0 — Chuẩn bị" — nhãn gây hiểu lầm | 2026-06-23 (**12 ngày** không cập nhật) |
| [[Pass The5er first package challenge (10k$)]] | 0% | 0/8 | 0% | ✅ Khớp | ⚠️ Cùng vấn đề nhãn phase như FTMO | 2026-06-23 (**12 ngày**) |
| [[Build a statistically validated backtest sample]] | 25% | 0/4 | 0% | ❌ **Lệch** | Phase 2 hợp lý | 2026-06-23 (**12 ngày**) |
| [[Master the ICT 2022 Model]] | 30% | 0/5 | 0% | ❌ **Lệch** | Phase 2 hợp lý | 2026-06-23 (**12 ngày**) |
| [[Cut my top 3 repeated mistakes]] | 20% | 0/4 | 0% | ❌ **Lệch** | Phase 1 hợp lý | 2026-06-23 (**12 ngày**) |
| [[Hold daily journaling and process discipline]] | 40% | 0/4 | 0% | ❌ **Lệch** | Phase 1 hợp lý | 2026-07-03 (**2 ngày** — mới nhất trong 6 goal) |

Không có gì thay đổi so với đối chiếu trong Daily Summary `2026-07-03` — 4/6 goal vẫn lệch progress% vs cột mốc, và cả 6 goal vẫn 0% theo cột mốc thật sau 12 ngày kể từ `start_date: 2026-06-23`. Bảng "Nhật ký tiến độ" của 5/6 goal (trừ Journaling) vẫn đứng yên đúng từ ngày dựng mục tiêu.

**Vấn đề dữ liệu khác đã biết, vẫn chưa được vá:**
- `baseline: ~15 backtest` của [[Build a statistically validated backtest sample]] vẫn lệch xa với thực tế chỉ **1 note** trong `04 - Backtesting`.
- `baseline: ~20 setup` của [[Master the ICT 2022 Model]] có cùng vấn đề (chỉ 1 backtest note thực tế).
- 3/3 note lỗi top hiện tại — [[06 - Mistake - Not Have Market Structure Shift]], [[09 - Mistake - Wrong daily bias]], [[07 - Mistake - Risk more than 0.5% total account]] — vẫn hoàn toàn rỗng (0 dòng nội dung), chặn cột mốc #2 của [[Cut my top 3 repeated mistakes]] ("viết biện pháp đối phó").

## 🩺 Pace check

Còn **186 ngày** tới hạn tự đặt `2027-01-07`. Backtest vẫn **1/200** (0,5%) sau 12 ngày — nhịp cần thiết để về đích tuyến tính là ~0,5 backtest/ngày, thực tế đang là ~0,08/ngày (1 note / 12 ngày). Cả 6 goal nền tảng/edge/challenge vẫn ở 0% theo cột mốc. Đây là tuần thứ hai liên tiếp (theo cảnh báo lặp lại trong cả 3 Daily Tasks của tuần) mà "phá thế đứt nhịp backtest + cập nhật Nhật ký tiến độ" được đặt làm ưu tiên số một nhưng chưa xong — nhịp hiện tại **chậm hơn nhịp cần thiết**, dù còn nhiều thời gian phía trước nên chưa phải báo động đỏ.

## 🎯 Trọng tâm tuần tới (2026-W28)

1. **Phá chuỗi đứng yên 12 ngày ở bảng "Nhật ký tiến độ"** — ưu tiên tuyệt đối cho ít nhất 1 trong 5 goal đang đứng yên (FTMO, The5ers, Backtest sample, Master 2022 Model, Cut top-3 mistakes), vì đây là nợ cũ nhất, đứng trước cả việc thêm backtest mới.
2. **Log ít nhất 1 backtest thật** vào `04 - Backtesting/2026-07-06/` (hoặc ngày tương ứng) — nợ đã kéo dài từ `2026-07-02`.
3. **Viết nội dung cho ít nhất 1/3 note lỗi rỗng** ([[06 - Mistake - Not Have Market Structure Shift]], [[09 - Mistake - Wrong daily bias]], [[07 - Mistake - Risk more than 0.5% total account]]) — đang chặn cột mốc #2 của [[Cut my top 3 repeated mistakes]] từ `2026-07-03`.
4. Đảm bảo có **Daily Summary cho mọi ngày**, kể cả ngày không có backtest/lệnh live (ghi "0" thay vì bỏ trống) — để tuần `2026-W28` có đủ dữ liệu cho một rollup đầy đủ hơn tuần này.

*(Không có lệnh live nào trong tuần nên không cần chạy Weekly Trading Review đầy đủ — vẫn đúng theo phạm vi Giai đoạn 1.)*

## 📋 Đề xuất cập nhật (dán tay vào file gốc)

**`09 - Goal Tracking/02 - Skill Metrics.md`** — thêm dòng vào "Bảng theo dõi hàng tuần":

```
| 2026-W27 | 0 | 0 |  |  | Tuần đầu hệ thống tự động, chỉ 1/7 ngày có Daily Summary (07-03). 3 concept chuyển seed→developing (Mitigation Block, Turtle Soup, Liquidity Void). 0 backtest mới, 0 lệnh live, 12 ngày đứng yên ở 5/6 bảng Nhật ký tiến độ. |
```
(Chất lượng quy trình và Kỷ luật để trống — Khang tự chấm 1–5.)

**[[Build a statistically validated backtest sample]] → Nhật ký tiến độ** — thêm dòng:
```
| 2026-07-05 | 0 | Hết tuần 2026-W27 vẫn 1/200 backtest (0,5%). Cột mốc thật 0/4, không phải 25% ghi tay. Baseline "~15" vẫn chưa được đối chiếu/sửa. |
```

**[[Hold daily journaling and process discipline]] → Nhật ký tiến độ** — thêm dòng:
```
| 2026-07-05 | 0 | Tuần 2026-W27: 1/7 ngày có Daily Summary, 3/7 ngày có Daily Tasks, 4/7 ngày không có dữ liệu gì. Cột mốc vẫn 0/4 — progress 40% ghi tay chưa khớp thực tế. |
```

## 🔗 Nguồn dữ liệu đã đọc

- `00 - Inbox/01 - Daily Tasks/2026-07-03 tasks.md`
- `00 - Inbox/01 - Daily Tasks/2026-07-04 tasks.md`
- `00 - Inbox/01 - Daily Tasks/2026-07-05 tasks.md`
- `00 - Inbox/02 - Daily Summary/2026-07-03 - Daily summary.md`
- `09 - Goal Tracking/Goals/Long Term (1-3 years)/Pass FTMO first package challenge (10K$).md`
- `09 - Goal Tracking/Goals/Long Term (1-3 years)/Pass The5er first package challenge (10k$).md`
- `09 - Goal Tracking/Goals/Mid Term (6-12 months)/Build a statistically validated backtest sample.md`
- `09 - Goal Tracking/Goals/Mid Term (6-12 months)/Master the ICT 2022 Model.md`
- `09 - Goal Tracking/Goals/Short Term (3-6 months)/Cut my top 3 repeated mistakes.md`
- `09 - Goal Tracking/Goals/Short Term (3-6 months)/Hold daily journaling and process discipline.md`
- `09 - Goal Tracking/01 - Roadmap.md`
- `09 - Goal Tracking/02 - Skill Metrics.md`
- `04 - Backtesting/` (đếm trực tiếp số note thực tế: 1)
- `05 - Live Trading Journal/Trades/2026/06/` và `2026/07/` (xác nhận không có lệnh trong tuần)
- `06 - Mistake Database/` (xác nhận 3 note lỗi top-3 vẫn rỗng)
- `02 - Trading Knowledge/Concepts/22 - Mitigation Block.md`, `33 - Turtle Soup.md`, `21 - Liquidity Void.md` (đối chiếu frontmatter `updated`)

## 🔗 Liên kết

[[00 - Goal Dashboard]] · [[01 - Roadmap]] · [[02 - Skill Metrics]] · [[_Backtest Dashboard]] · [[02 - Mistake Frequency Dashboard]]
