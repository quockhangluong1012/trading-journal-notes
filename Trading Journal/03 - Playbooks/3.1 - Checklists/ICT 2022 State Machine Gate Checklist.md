---
type: checklist
category: pre-trade
strategy: ICT 2022 Model
rule_version: "ICT2022-SM v0.1"
markets:
  - NQ1
  - EURUSD
  - GBPUSD
  - XAUUSD
created: 2026-09-29
updated: 2026-09-29
tags:
  - checklist
  - pre-trade
  - ict-2022
  - state-machine
---

# ICT 2022 State Machine Gate Checklist — một trang theo state

> [!info] Dùng file này như thế nào
> Đây là thẻ vận hành của **[[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]]** (spec v0.1). Mỗi khối = một state/gate. **Dừng ở khối đầu tiên có ô không tick được**, ghi `max_state_reached` + `stop_reason` vào Daily State Log — kể cả khi dừng ở S0. Ngưỡng số là `HEURISTIC` — không đổi giữa một đợt log.
> Thẻ nhanh tại hard right edge vẫn là [[ICT 2022 Entry Checklist]]; file này kiểm **thứ tự trạng thái, gate, invalidation và reset**.

---

## ⏱ Clock — trước mọi thứ
- [ ] Nến D1 theo **NY close 17:00** (không có nến Chủ nhật) · NQ theo phiên CME
- [ ] Đã quy đổi DST: 17:00 NY = **04:00 VN (EDT) / 05:00 VN (EST)**
- [ ] Killzone của spec đã khai báo cho thị trường này: `________` (NY time)
- [ ] Lịch tin cấp cao hôm nay đã xem · Risk overlay: ☐ OPEN ☐ CAUTION ☐ **LOCKED → dừng**

## S0 → S2 · D1 Context Card (viết TRƯỚC khi mở H1)
- [ ] Structure state: ☐ BULLISH ☐ BEARISH — *(TRANSITION / RANGE → dừng ở S1)*
- [ ] Protected swing (L4) ghi giá: `______`
- [ ] Dealing range: 2 neo L4, **đóng băng** tại cutoff · z hiện tại = `____`
- [ ] Pool list **hai phía** (L3+, chưa lấy)
- [ ] Primary DOL `______` · Secondary DOL `______` · horizon `__` nến D1 · invalidation viết ra
- [ ] Bias: ☐ BULL ☐ BEAR — *(NEUTRAL → ghi lý do, dừng)*
- [ ] Vùng được phép: D1 POI `[____, ____]` distal **trên** protected swing — hoặc z-zone (đã khai báo trước)

## Gate G1 · D1 → H1
- [ ] Location đúng phía (long: z ≤ 0,5 / trong D1 POI / subtype continuation ghi riêng)
- [ ] Khoảng cách tới primary DOL **≥ 1 ATR(D1)**
- [ ] Không có tin cấp cao chưa xử lý (hoặc event-mode đã khai báo)
- [ ] W1 không ngược hướng **tại** W1 POI ngược hướng
- [ ] Card được viết **trước** khi nhìn H1/M5 hôm nay
- Confidence (đếm supporting: W1 cùng hướng · D1 displacement cùng hướng · opposing liquidity đã lấy · DOL chưa bị wick · DOL ≥ 2 ATR · SMT không ngược) → **0–2 Low · 3–4 Medium · 5–6 High** → risk ≤ **0,25% / 0,4% / 0,5%**

## S4 → S5 · H1 Setup Card
- [ ] Quan hệ H1–D1: ☐ ALIGNED ☐ PULLBACK (chờ) ☐ ARRIVAL — *(THREAT → giảm size · INVALIDATING → báo D1, dừng)*
- [ ] H1 POI qua 5 gate: trong vùng được phép · gốc là displacement · chưa bị accept xuyên · room ≥ 2R · không có opposing pool trong 1R
- [ ] Rank + kế hoạch cascade viết ra (POI B chỉ arm khi A accept-through và giá trên hard floor)
- [ ] **Pool sẽ bị sweep** đánh dấu: `______` · Inducement (nếu có) gán nhãn trước: `______`
- [ ] Target 1 (H1 external liquidity) `______` · TTL: hết killzone / D1 close

## Gate G2 · H1 → M5
- [ ] Context Card **vẫn** hợp lệ (không SUSPEND) · Setup Card vẫn armed
- [ ] **Arrival**: giá trong zone hoặc cách proximal ≤ 0,1 ATR(H1)
- [ ] **Đang trong killzone** đã khai báo
- [ ] **mss_reference** (swing gốc của leg đi vào sweep) đánh dấu **trước sweep**: `______` + screenshot có giờ
- [ ] Room: entry dự kiến → t1 ≥ 2 × stop dự kiến
- [ ] Không có tin cấp cao trong ±15'
- ✖ Dừng nếu: arrival bằng một nến H1 xuyên cả zone · pool sweep nằm dưới D1 POI distal · refs đánh dấu **sau** sweep · đã 2 lần fail trong zone hôm nay

## S7 → S8 · M5 trigger (đúng thứ tự thời gian)
- [ ] **Sweep**: xuyên pool đã đánh dấu → **close lại trong ≤ 3 nến** · không có 2 close dưới pool − 0,5 ATR
- [ ] **MSS**: body close qua mss_reference, **sau** nến reclaim, trong ≤ 12 nến
- [ ] **Displacement**: leg ≥ 2 ATR(M5) · body ≥ 0,6 · efficiency ≥ 0,5 · có FVG ≥ 0,2 ATR · `news_displacement` = ☐ không
- [ ] **FVG** theo quy tắc spec (☐ F1 sát mức MSS ☐ F2 FVG đầu tiên) · entry type (☐ proximal ☐ CE ☐ MSS close)
- [ ] Stop = sweep extreme ± max(2 × spread, 0,1 ATR) · **R(t1) ≥ 2** · size theo confidence, **≤ 0,5%**

## S8 → S10 · lệnh chờ & quản lý
- [ ] Hủy lệnh chờ nếu: close xuyên FVG distal · hết 12 nến / hết killzone · giá tới +1R chưa khớp → log **`missed`**, không đuổi
- [ ] Quản lý theo spec đã khai báo: ☐ v0.1 full exit t1/stop ☐ partial 50% @1R + BE (log thêm `r_if_no_management`)

## ⛔ Invalidation — tầng nào chết thì reset tầng đó
| Sự kiện | Bằng chứng | Reset tới |
|---|---|---|
| Body close D1 xuyên protected swing | D1 close | **S0** |
| Giá xuyên protected > 0,5 ATR trong phiên / tin ngoài lịch | Real-time | **SUSPEND** — không entry mới tới D1 close |
| Primary DOL bị chạm | Chạm | FULFILLED → S2 (re-derive tại D1 close) |
| Secondary DOL bị lấy **và** accept | Close | S2 (có thể lật bias) |
| D1 POI accept-through (2 close không reclaim) | Close | S3 → S2 |
| H1 zone accept-through | 2 close H1 | Cascade POI → S5 / S4 |
| M5 close dưới sweep extreme / MSS fail / FVG fail | Close M5 | S6 nếu zone còn + còn killzone + < 2 fail |
| Hết TTL | Đồng hồ | EXPIRED — ghi riêng, không gộp vào "sai" |

> [!important] Sau mọi kết thúc: reset về **tổ tiên sâu nhất còn hợp lệ**, không về S0. Một lệnh thua **không phải** trigger đổi bias.

## 📝 Daily State Log — bắt buộc mỗi ngày
`date` · `symbol` · `rule_version` · `context_card_written_at` · `max_state_reached` · `stop_reason` · `bias` · `confidence` · `failed_gate` · `shadow_A_R` · `shadow_B_R` · `trade_C` · `failed_layer` · `news_day`

## Liên kết
- Spec đầy đủ: [[01c - ICT 2022 Model - He thong quyet dinh da khung (State Machine D1-H1-M5)]]
- Thẻ nhanh: [[ICT 2022 Entry Checklist]] · [[LTF Drop-Down Confirmation Checklist (Khi nao xuong khung thap tai OB H1)]] · [[Daily Risk & Circuit Breaker Checklist]]
- Mô hình: [[01 - ICT 2022 Model]]
