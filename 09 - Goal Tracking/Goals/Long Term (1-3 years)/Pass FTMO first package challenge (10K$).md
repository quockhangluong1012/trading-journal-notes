---
type: goal
horizon: Long
category: Consistency
status: Not Started
priority: High
progress: 0
metric: Vượt qua 2 phase của FTMO Challenge và nhận tài khoản cấp vốn 10.000$
baseline: Chưa bắt đầu thử thách (0/2 phase)
target: Pass Phase 1 (+10%) → Pass Phase 2 (+5%) → Nhận tài khoản Funded 10K$
phase: Phase 0 - Preparation
start_date: 2026-06-23
due_date: 2027-12-31
tags:
  - goal
  - prop-firm
  - ftmo
---

# Vượt qua FTMO Challenge gói đầu tiên (10.000$)

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Ổn định / Kỷ luật (thực thi edge dưới áp lực luật quỹ)
> - **Vì sao quan trọng:** Đây là bài kiểm tra thực tế xem edge ICT 2022 model + kỷ luật rủi ro của mình có sống được dưới luật quỹ cấp vốn hay không. Pass FTMO = bằng chứng khách quan rằng mình đã sẵn sàng giao dịch vốn của người khác, và mở đường tới payout thật.
> - **Điều kiện thành công:** Hoàn thành cả 2 phase của FTMO 2-Step Challenge mà không vi phạm bất kỳ luật rủi ro nào, sau đó nhận tài khoản FTMO Account (Funded) 10K$.

> [!warning] Luật FTMO 2-Step Challenge — 10K$ (cập nhật 2026)
> **Phase 1 — FTMO Challenge:**
> - Mục tiêu lợi nhuận: **+10%** (≈ +1.000$)
> - Lỗ tối đa trong ngày (Max Daily Loss): **5%** (≈ 500$) — tính trên cả lệnh đã đóng + lệnh đang mở + phí + swap, mốc reset mỗi ngày
> - Lỗ tối đa tổng (Max Loss): **10%** (≈ 1.000$) — equity không bao giờ được xuống dưới 9.000$ (mức tĩnh)
> - Số ngày giao dịch tối thiểu: **4 ngày**
> - Thời gian: **Không giới hạn**
>
> **Phase 2 — Verification:**
> - Mục tiêu lợi nhuận: **+5%** (≈ +500$)
> - Cùng luật Max Daily Loss 5% và Max Loss 10%
> - Số ngày giao dịch tối thiểu: **4 ngày**, thời gian không giới hạn
>
> **Funded:** Sau khi pass, nhận tài khoản FTMO 10K$, profit split khởi điểm **80%** cho trader.
>
> ⚠️ FTMO 2026 có thêm gói **1-Step** (target 10%, daily loss 3%, max loss 10% trailing, có Best Day Rule, split 90%). Mình chọn **2-Step** vì luật drawdown dễ thở hơn cho lần đầu. Luôn kiểm tra lại luật chính thức tại [ftmo.com/trading-objectives](https://ftmo.com/en/trading-objectives/) trước khi mua gói.

## Định nghĩa hoàn thành
- [ ] Pass Phase 1: đạt +10% lợi nhuận, không phá luật, ≥4 ngày giao dịch
- [ ] Pass Phase 2: đạt +5% lợi nhuận, không phá luật, ≥4 ngày giao dịch
- [ ] Nhận tài khoản Funded 10K$ và đăng nhập thành công
- [ ] Không vi phạm Max Daily Loss / Max Loss trong toàn bộ quá trình

## Cách đo lường
- **Chỉ số:** % lợi nhuận hiện tại của mỗi phase + khoảng cách tới giới hạn lỗ ngày/tổng
- **Hiện tại:** Chưa mua gói — 0% tiến độ
- **Mục tiêu:** Phase 1 +10% → Phase 2 +5% → Funded
- **Tần suất review:** Hàng ngày trong lúc đang thi (kiểm tra daily loss), tổng kết hàng tuần

> [!tip] Kỷ luật rủi ro tự đặt ra (chặt hơn luật quỹ)
> - Rủi ro mỗi lệnh tối đa **0,5% – 1%** tài khoản (50$ – 100$), KHÔNG bao giờ vượt.
> - Dừng giao dịch trong ngày nếu lỗ chạm **3%** (300$) — đệm an toàn so với mốc 5% của FTMO.
> - Tối đa **2–3 lệnh/ngày**, chỉ vào setup A+ theo playbook 2022 model.
> - Không tăng size để "gỡ", không giao dịch trả thù, không dời SL.

## Kế hoạch hành động chi tiết (từng bước)

### Giai đoạn 0 — Chuẩn bị (trước khi mua gói)
1. Hoàn thiện backtest 2022 model đạt mẫu đủ lớn (≥100 setup) với win rate & R kỳ vọng ổn định — xem [[Build a statistically validated backtest sample]].
2. Viết playbook A+ rõ ràng: điều kiện vào lệnh, vị trí SL/TP, khung giờ giao dịch (ưu tiên killzone London/New York).
3. Tính sẵn khối lượng lệnh (lot size) cho rủi ro 0,5% và 1% trên tài khoản 10K$ → lập bảng tra nhanh.
4. Mở demo FTMO đúng size 10K$, set sẵn cảnh báo (alert) khi lỗ ngày chạm 3% và khi equity về 9.300$.

### Giai đoạn 1 — Demo thử luật (2 tuần)
5. Giao dịch demo đúng luật FTMO trong 10 ngày giao dịch, ghi nhật ký mỗi lệnh vào [[Trade template]].
6. Mỗi cuối ngày: ghi lại lỗ/lãi ngày, kiểm tra đã giữ dưới mốc 3% tự đặt chưa.
7. Cuối 2 tuần: review — nếu giữ luật + có lãi ròng thì chuyển sang mua gói thật; nếu phá luật, lặp lại demo.

### Giai đoạn 2 — Phase 1 (mục tiêu +10%)
8. Mua gói FTMO Challenge 2-Step 10K$, đăng nhập, xác nhận thông số tài khoản đúng luật.
9. Mỗi ngày trước phiên: kiểm tra lịch tin tức, tránh giao dịch quanh tin đỏ; xác định bias HTF.
10. Vào tối đa 2–3 lệnh A+/ngày, rủi ro ≤1%, ghi lý do vào lệnh.
11. Dừng ngay khi: chạm +10% mục tiêu, HOẶC lỗ ngày chạm 3%, HOẶC đã đủ 2–3 lệnh.
12. Khi đạt +10% và đã giao dịch ≥4 ngày → ngừng giao dịch, chờ FTMO duyệt sang Phase 2.

### Giai đoạn 3 — Phase 2 (mục tiêu +5%)
13. Giữ nguyên kỷ luật, nhưng giảm áp lực: mục tiêu chỉ còn +5% → có thể hạ rủi ro xuống 0,5%/lệnh.
14. Ưu tiên bảo toàn vốn hơn là chạy nhanh; đạt +5% với ≥4 ngày giao dịch là pass.
15. Khi pass → hoàn tất KYC, ký hợp đồng, nhận tài khoản Funded.

### Giai đoạn 4 — Sau khi Funded
16. Đăng nhập tài khoản 10K$, giao dịch đúng playbook để hướng tới payout đầu tiên (split 80%).
17. Cập nhật mục tiêu này thành Done và mở mục tiêu mới: "Nhận payout FTMO đầu tiên".

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [ ] **Chuẩn bị:** Backtest đủ mẫu 2022 model có win rate ổn định + playbook rõ ràng trước khi mua gói
- [ ] **Demo thử luật:** Chạy thử 2 tuần trên demo theo đúng luật FTMO (target 10%, daily loss 5%) không phá luật
- [ ] **Mua gói:** Mua FTMO Challenge 2-Step 10K$ và bắt đầu Phase 1
- [ ] **Phase 1 – nửa chặng:** Đạt +5% mà chưa chạm bất kỳ giới hạn lỗ nào
- [ ] **Pass Phase 1:** Đạt đủ +10%, hoàn thành ≥4 ngày giao dịch
- [ ] **Phase 2 – khởi động:** Vào Verification, giữ nguyên kỷ luật rủi ro
- [ ] **Pass Phase 2:** Đạt đủ +5%, hoàn thành ≥4 ngày giao dịch
- [ ] **Nhận Funded:** Kích hoạt tài khoản FTMO 10K$ thành công

## Nhật ký tiến độ
| Ngày       | Phase    | Lợi nhuận % | Tiến độ % | Ghi chú                                                                |
| ---------- | -------- | ----------: | --------: | ---------------------------------------------------------------------- |
| 2026-06-23 | Chuẩn bị |           0 |         0 | Dựng mục tiêu & ghi luật quỹ. Chưa mua gói — tập trung backtest trước. |
| 2026-07-12 | Chuẩn bị |           0 |         0 | **Phá chuỗi 19 ngày im lặng của log này (gần nhất 2026-06-23).** Chuyển động THẬT duy nhất hôm nay: sửa nhãn `phase` frontmatter **`Phase 4 - Challenge` → `Phase 0 - Preparation`** (nhãn cũ sai — chưa mua gói). ⚠️ **Việc mở khoá thật vẫn CHƯA làm:** bảng lot size 0,5%/1% cho tài khoản 10K$ (bước 3 Giai đoạn 0) — file task 07-12 tick `[x]` nhưng **không có note lot-size nào tồn tại** trong `03 - Playbooks` hay `09 - Goal Tracking`. Đây là overtick, không phải hoàn thành. Progress **vẫn 0%**, cột mốc **0/8**, chưa chạm bước Giai đoạn 0 nào có kết quả. Rào cản #1 tới mốc 2027-01-07 (còn 179 ngày). |
| 2026-07-13 | Chuẩn bị | 0 | 0 | ✅ **Rào cản #1 (overtick nhiều ngày) đã được GỠ THẬT hôm nay.** Bước 3 Giai đoạn 0 ("tính sẵn lot size cho 0,5% và 1% trên 10K$ → bảng tra nhanh") nay có **note THẬT**: `03 - Playbooks/3.1 - Checklists/Lot size 10K.md` (`account: FTMO 10K`) — bảng lot cho **EURUSD, GBPUSD, XAUUSD, NAS100** theo dải SL @ risk $50 (0,5%) và $100 (1%); bảng **expectancy Win%×RR** (R/lệnh + lợi nhuận/tháng @0,5% & 1%); mục **rủi ro & giới hạn FTMO** (daily loss $500/5% trên balance gốc, max loss $1.000/10%, ≥4 ngày giao dịch); mentor note nhấn: ở 1% chỉ **5 lệnh thua liên tiếp** là chạm daily limit, ở 0,5% có đệm **10 lệnh** → khoá 0,5% giai đoạn foundation. Kèm file Excel `[[FTMO 10K - Lot Size & Profit Calculator.xlsx]]`. **Đây là chuyển động THẬT, không phải overtick** — mở khoá bước 3/4 của Giai đoạn 0. **Progress vẫn 0%, cột mốc vẫn 0/8:** cột mốc "Chuẩn bị" đòi trọn gói (backtest đủ mẫu ≥100 + playbook rõ ràng), lot size chỉ là một mảnh — chưa đủ tick. Còn treo trong Giai đoạn 0: mẫu backtest (mới 13/200), playbook A+ thành văn (checklist vào/ra chưa viết), mở demo 10K$ + set alert. 178 ngày tới mốc 2027-01-07 — dư thời gian lịch NẾU giữ nhịp prep; rủi ro thật là **live execution 0 lệnh 25 ngày** (chưa kiểm chứng dưới áp lực luật). |

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Become a consistently profitable ICT trader]], [[Master the ICT 2022 Model]], [[Build a statistically validated backtest sample]], [[Pass The5er first package challenge (10k$)]]
