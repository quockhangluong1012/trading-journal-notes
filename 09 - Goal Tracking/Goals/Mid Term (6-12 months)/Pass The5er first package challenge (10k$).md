---
type: goal
horizon: Long
category: Consistency
status: Not Started
priority: High
progress: 0
metric: Vượt qua 2 phase của The5ers High Stakes Challenge và nhận tài khoản cấp vốn 10.000$
baseline: Chưa bắt đầu thử thách (0/2 phase)
target: Pass Phase 1 (+10%) → Pass Phase 2 (+5%) → Nhận tài khoản Funded 10K$
phase: Phase 0 - Preparation
start_date: 2026-06-23
due_date: 2027-12-31
tags:
  - goal
  - prop-firm
  - the5ers
---

# Vượt qua The5ers Challenge gói đầu tiên (10.000$)

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Ổn định / Kỷ luật (thực thi edge dưới luật quỹ The5ers)
> - **Vì sao quan trọng:** The5ers là quỹ thứ hai để đa dạng hóa nguồn vốn cấp và kiểm chứng lại edge dưới một bộ luật khác (trailing/daily drawdown khác FTMO). Pass cả hai quỹ chứng minh edge không phụ thuộc vào một bộ luật cụ thể, mà thật sự bền vững.
> - **Điều kiện thành công:** Hoàn thành cả 2 phase của chương trình High Stakes (2-Step) mà không vi phạm luật rủi ro, sau đó nhận tài khoản Funded 10K$.

> [!warning] Luật The5ers High Stakes 2-Step — 10K$ (cập nhật 2026)
> **Phase 1:**
> - Mục tiêu lợi nhuận: **+10%** (≈ +1.000$)
> - Lỗ tối đa trong ngày (Daily Drawdown): **5%** — tính từ số dư/equity ĐÓNG CỬA của ngày hôm trước (lấy mức cao hơn giữa balance và equity)
> - Lỗ tối đa tổng (Max Loss): **10%** tính từ số dư ban đầu (drawdown tuyệt đối, mốc tĩnh)
> - Số ngày có lãi tối thiểu: **3 ngày** — một "ngày có lãi" là ngày các lệnh đã đóng đạt lợi nhuận ≥ **0,5%** số dư ban đầu (≥ 50$)
>
> **Phase 2:**
> - Mục tiêu lợi nhuận: **+5%** (≈ +500$)
> - Cùng luật Daily Drawdown 5% và Max Loss 10%
> - Vẫn cần tối thiểu **3 ngày có lãi** (≥0,5%/ngày)
>
> **Funded:** Sau khi pass, nhận tài khoản 10K$, profit split khởi điểm **80%** (scale dần tới 100%), payout 2 tuần/lần.
>
> ⚠️ Lưu ý khác biệt then chốt so với FTMO: The5ers tính daily drawdown trên **mốc cuối ngày hôm trước** (không reset về balance gốc), và yêu cầu **ngày có lãi ≥0,5%** chứ không chỉ là "ngày giao dịch". Luôn kiểm tra luật chính thức tại [the5ers.com/high-stakes](https://the5ers.com/high-stakes/) trước khi mua gói.

## Định nghĩa hoàn thành
- [ ] Pass Phase 1: đạt +10% lợi nhuận, ≥3 ngày có lãi (≥0,5%/ngày), không phá luật
- [ ] Pass Phase 2: đạt +5% lợi nhuận, ≥3 ngày có lãi, không phá luật
- [ ] Nhận tài khoản Funded 10K$ và đăng nhập thành công
- [ ] Không vi phạm Daily Drawdown / Max Loss trong toàn bộ quá trình

## Cách đo lường
- **Chỉ số:** % lợi nhuận của mỗi phase + số ngày có lãi đã tích lũy + khoảng cách tới mốc daily drawdown
- **Hiện tại:** Chưa mua gói — 0% tiến độ
- **Mục tiêu:** Phase 1 +10% → Phase 2 +5% → Funded
- **Tần suất review:** Hàng ngày trong lúc đang thi, tổng kết hàng tuần

> [!tip] Kỷ luật rủi ro tự đặt ra (chặt hơn luật quỹ)
> - Rủi ro mỗi lệnh tối đa **0,5% – 1%** tài khoản (50$ – 100$).
> - Vì daily drawdown tính trên mốc cuối ngày hôm trước → **chốt lời sớm** một phần để khóa "ngày có lãi" và nâng mốc đệm.
> - Dừng giao dịch trong ngày nếu lỗ chạm **3%** — đệm an toàn so với mốc 5%.
> - Ưu tiên gom đủ 3 ngày có lãi ≥0,5% sớm để giải tỏa áp lực điều kiện ngày.
> - Chỉ vào setup A+ theo playbook 2022 model, tối đa 2–3 lệnh/ngày.

## Kế hoạch hành động chi tiết (từng bước)

### Giai đoạn 0 — Chuẩn bị (trước khi mua gói)
1. Hoàn thiện playbook 2022 model & backtest đủ mẫu — xem [[Build a statistically validated backtest sample]].
2. Học kỹ cách The5ers tính **daily drawdown trên mốc cuối ngày hôm trước** (khác FTMO) → mô phỏng vài tình huống trên giấy.
3. Lập bảng lot size cho rủi ro 0,5% và 1% trên 10K$; xác định ngưỡng "ngày có lãi" = +50$ (0,5%).
4. Mở demo đúng size 10K$, đặt alert khi lỗ ngày chạm 3% và khi chạm mốc max loss 9.000$.

### Giai đoạn 1 — Demo thử luật (2 tuần)
5. Giao dịch demo theo luật The5ers, mục tiêu gom đủ **≥3 ngày có lãi ≥0,5%** mà không phá luật.
6. Tập thói quen **chốt lời một phần sớm** để khóa "ngày có lãi" và nâng mốc đệm daily drawdown.
7. Cuối ngày ghi lại: equity đóng cửa hôm nay (= mốc drawdown cho ngày mai) vào [[Trade template]].
8. Review cuối 2 tuần: giữ luật + đủ ngày có lãi → mua gói thật.

### Giai đoạn 2 — Phase 1 (mục tiêu +10%)
9. Mua gói High Stakes 2-Step 10K$, xác nhận thông số đúng luật.
10. Mỗi ngày: xác định bias HTF, tránh tin đỏ, vào tối đa 2–3 lệnh A+ rủi ro ≤1%.
11. Ưu tiên đóng được tối thiểu +0,5% mỗi ngày giao dịch để tích lũy "ngày có lãi" sớm.
12. Dừng ngày khi: chạm mục tiêu, HOẶC lỗ ngày chạm 3%, HOẶC đủ số lệnh.
13. Khi đạt +10% và đủ ≥3 ngày có lãi → ngừng, chờ duyệt sang Phase 2.

### Giai đoạn 3 — Phase 2 (mục tiêu +5%)
14. Giữ kỷ luật, hạ rủi ro xuống 0,5%/lệnh; mục tiêu +5% và đủ 3 ngày có lãi.
15. Bảo toàn vốn là ưu tiên số một; pass → hoàn tất KYC & ký hợp đồng.

### Giai đoạn 4 — Sau khi Funded
16. Giao dịch tài khoản 10K$ (split 80%, payout 2 tuần/lần) hướng tới payout đầu tiên.
17. Cập nhật mục tiêu này thành Done và mở mục tiêu mới: "Nhận payout The5ers đầu tiên".

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [ ] **Chuẩn bị:** Hoàn thiện playbook 2022 model + nắm rõ cách tính daily drawdown của The5ers
- [ ] **Demo thử luật:** Chạy thử 2 tuần trên demo theo luật The5ers, gom đủ ≥3 ngày có lãi ≥0,5% không phá luật
- [ ] **Mua gói:** Mua The5ers High Stakes 2-Step 10K$ và bắt đầu Phase 1
- [ ] **Đủ điều kiện ngày:** Tích lũy đủ 3 ngày có lãi ≥0,5% ở Phase 1
- [ ] **Pass Phase 1:** Đạt đủ +10%, đủ ngày có lãi
- [ ] **Phase 2 – khởi động:** Vào phase 2, giữ nguyên kỷ luật rủi ro
- [ ] **Pass Phase 2:** Đạt đủ +5%, đủ ngày có lãi
- [ ] **Nhận Funded:** Kích hoạt tài khoản The5ers 10K$ thành công

## Nhật ký tiến độ
| Ngày | Phase | Lợi nhuận % | Ngày có lãi | Tiến độ % | Ghi chú |
|---|---|---:|---:|---:|---|
| 2026-06-23 | Chuẩn bị | 0 | 0 | 0 | Dựng mục tiêu & ghi luật quỹ. Chưa mua gói — tập trung backtest trước. |
| 2026-07-12 | Chuẩn bị | 0 | 0 | 0 | **Phá chuỗi 19 ngày im lặng (gần nhất 2026-06-23).** Chuyển động THẬT hôm nay: sửa nhãn `phase` **`Phase 4 - Challenge` → `Phase 0 - Preparation`**. ⚠️ **Chưa làm:** bảng lot size 0,5%/1% + ngưỡng "ngày có lãi = +50$ (0,5%)" (bước 3 Giai đoạn 0, dùng chung với FTMO) — file task 07-12 tick `[x]` nhưng **không có note lot-size nào tồn tại** → overtick. Nhắc luật riêng cần nắm trước khi làm bảng: daily drawdown The5ers tính từ **equity ĐÓNG CỬA hôm trước** (không reset về balance gốc như FTMO) + cần **≥3 ngày có lãi ≥0,5%**. Progress **vẫn 0%**, cột mốc **0/8**. Rào cản #1 tới mốc 2027-01-07 (còn 179 ngày). |
| 2026-07-13 | Chuẩn bị | 0 | 0 | 0 | ⚠️ **Phần lot size (dùng chung với FTMO) đã làm THẬT hôm nay — nhưng phần RIÊNG của The5ers thì CHƯA.** Note thật `03 - Playbooks/3.1 - Checklists/Lot size 10K.md` phủ toán lot cho EURUSD/GBPUSD/XAUUSD/NAS100 @0,5% & 1% (currency-agnostic → áp dụng được cho The5ers), nhưng note đang gắn `account: FTMO 10K` và **thiếu 2 thứ đặc thù The5ers** của bước 3 Giai đoạn 0: (1) cột/ghi rõ **"ngày có lãi = +50$ (0,5% balance gốc)"**, (2) mô phỏng **daily drawdown tính từ equity ĐÓNG CỬA hôm trước** (không reset về balance gốc như FTMO) — đây là bước 2 Giai đoạn 0 vẫn để trống. Nên: track này nhích một phần nhưng **chưa xong bước 3, và bước 2 (paper-sim luật prior-close) vẫn chưa làm**. **Progress vẫn 0%, cột mốc vẫn 0/8** (cột mốc "Chuẩn bị" đòi playbook + nắm rõ cách tính daily drawdown The5ers — cả hai chưa đủ bằng chứng). Việc mai: thêm mục The5ers vào note lot size (ngưỡng ngày-có-lãi + ví dụ prior-close drawdown) để đóng bước 2+3 cho track này. 178 ngày tới 2027-01-07; rủi ro thật vẫn là **0 lệnh live 25 ngày**. |
| 2026-07-16 | Chuẩn bị | 0 | 0 |Tập trung backtest|
| 2026-07-17 | Chuẩn bị | 0 | 0 |Tập trung backtest|

## Liên kết
- Lộ trình: [[01 - Roadmap]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Become a consistently profitable ICT trader]], [[Master the ICT 2022 Model]], [[Build a statistically validated backtest sample]], [[Pass FTMO first package challenge (10K$)]]
