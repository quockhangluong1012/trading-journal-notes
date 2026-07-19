---
type: goal
horizon: Long
category: Consistency
status: Not Started
priority: Medium
progress: 0
metric: Pass cả FTMO 100K và The5ers 100K, nhận 2 tài khoản funded 100.000$
baseline: Chưa đủ điều kiện gate — đang ở giai đoạn chuẩn bị gói 10K
target: Funded FTMO 100K + Funded The5ers 100K trước 2028-06-30
phase: Phase 5 - Scaling
start_date: 2026-07-18
due_date: 2028-06-30
tags:
  - goal
  - prop-firm
  - ftmo
  - the5ers
  - scaling
---

# Pass FTMO & The5ers gói 100.000$ (Scale từ 10K)

> [!info] Tổng quan mục tiêu
> - **Phân loại:** Scaling / Ổn định (nhân edge đã kiểm chứng lên vốn lớn hơn 10 lần)
> - **Vì sao quan trọng:** 10K là nơi *chứng minh* hệ thống; 100K mới là nơi hệ thống *tạo thu nhập có ý nghĩa* cho mục tiêu chuyển nghề. Cùng % rules nhưng con số tuyệt đối lớn gấp 10 (daily loss 5.000$ thay vì 500$) — bài kiểm tra thật sự nằm ở tâm lý, không phải kỹ thuật.
> - **Điều kiện thành công:** Pass cả hai quỹ ở gói 100K mà không vi phạm luật rủi ro nào, kích hoạt 2 tài khoản funded.

> [!warning] Luật hai quỹ — gói 100K (kiểm tra lần cuối: 2026-07-18)
> **FTMO 2-Step 100K** ([nguồn](https://ftmo.com/en/2-step-challenge/)):
> - Phase 1 **+10%** (10.000$) → Phase 2 **+5%** (5.000$)
> - Max Daily Loss **5%** (5.000$) — mốc tĩnh trên balance đầu ngày, reset mỗi ngày 00:00 CE(S)T
> - Max Loss **10%** (10.000$) — equity không được chạm 90.000$
> - Tối thiểu **4 ngày giao dịch**/phase, thời gian không giới hạn, phí ~540$ (hoàn 100% khi pass), profit split tới 90%
>
> **The5ers High Stakes 100K** ([nguồn](https://help.the5ers.com/what-are-the-general-rules-for-the-high-stakes-program/)):
> - **New High Stakes:** Phase 1 **+10%** → Phase 2 **+5%**. **Classic High Stakes:** Phase 1 **+8%** → Phase 2 **+5%** — khi mua phải xác nhận rõ mình mua biến thể nào.
> - Daily Drawdown **5%** — tính từ **closing equity/balance cao hơn của ngày hôm trước**, chốt 00:00 giờ server (KHÔNG reset về balance gốc như FTMO)
> - Max Loss **10%** từ balance ban đầu (mốc tĩnh)
> - Tối thiểu **3 ngày có lãi**, tài khoản hết hạn nếu **30 ngày liên tiếp không giao dịch**, payout mỗi 14 ngày
>
> ⚠️ Luật quỹ thay đổi thường xuyên — bắt buộc đọc lại trang chính thức của cả hai quỹ ngay trước khi mua gói.

> [!tip] Khác biệt cốt lõi so với 10K (đọc kỹ trước khi bắt đầu)
> - **Kỹ thuật giữ nguyên, con số đổi:** risk 0,5%/lệnh = **500$/lệnh**. Nếu 500$ thua trong 1 lệnh làm mình run tay → chưa sẵn sàng, quay lại funded 10K thêm 1 quý.
> - **Đệm tự đặt giữ nguyên theo %:** dừng ngày ở −3% (−3.000$), tối đa 2–3 lệnh A+/ngày.
> - **Không mua 100K bằng tiền túi "gồng":** ưu tiên trả phí bằng payout tích lũy từ tài khoản funded 10K.

## Định nghĩa hoàn thành
- [ ] Pass FTMO 100K Phase 1 (+10%) và Phase 2 (+5%), không vi phạm luật, nhận tài khoản funded
- [ ] Pass The5ers 100K Phase 1 và Phase 2, đủ ngày có lãi, không vi phạm luật, nhận tài khoản funded
- [ ] Không vi phạm Max Daily Loss / Max Loss / Daily Drawdown trong toàn bộ quá trình
- [ ] Nhận payout đầu tiên từ ít nhất một tài khoản 100K

## Điều kiện gate — CHƯA được mua gói 100K khi chưa đủ TẤT CẢ
> [!warning] Gate cứng (chống FOMO scale sớm)
> 1. Đã **funded cả FTMO 10K và The5ers 10K** (hoặc tối thiểu 1 quỹ funded + 1 quỹ pass Phase 1).
> 2. Đã nhận **≥2 payout** từ tài khoản funded 10K (chứng minh sống sót sau khi pass, không chỉ pass).
> 3. **≥3 tháng liên tiếp có lãi** trên tài khoản funded theo tổng R.
> 4. Mistake rate (lỗi/lệnh theo `06 - Mistake Database`) ở mức thấp và **không tăng** trong 3 tháng gần nhất.
> 5. Phí 100K được trả **từ lợi nhuận trading**, không phải từ lương.

## Cách đo lường
- **Chỉ số:** Số điều kiện gate đã đạt (0/5) → sau đó % lợi nhuận từng phase + khoảng cách tới giới hạn lỗ
- **Hiện tại:** 0/5 gate — đang ở Phase 0 của track 10K
- **Mục tiêu:** Funded 2 tài khoản 100K trước 2028-06-30
- **Tần suất review:** Hàng tháng (giai đoạn gate), hàng ngày (khi đang thi)

## Cột mốc
> Mỗi checkbox = một cột mốc. Dashboard đếm các mục này để tính tiến độ.
- [ ] **Gate 1:** Funded cả 2 quỹ gói 10K ([[Pass FTMO first package challenge (10K$)]], [[Pass The5er first package challenge (10k$)]])
- [ ] **Gate 2:** Nhận ≥2 payout từ funded 10K
- [ ] **Gate 3:** 3 tháng liên tiếp có lãi trên funded 10K + mistake rate ổn định thấp
- [ ] **Mua gói:** Mua FTMO 100K bằng lợi nhuận trading, bắt đầu Phase 1
- [ ] **Pass FTMO 100K Phase 1** (+10%, ≥4 ngày giao dịch, không phá luật)
- [ ] **Pass FTMO 100K Phase 2** (+5%) → nhận funded 100K
- [ ] **Mua & Pass The5ers 100K Phase 1** (xác nhận biến thể New/Classic trước khi mua)
- [ ] **Pass The5ers 100K Phase 2** → nhận funded 100K
- [ ] **Payout 100K đầu tiên**

## Nhật ký tiến độ
| Ngày | Tiến độ % | Ghi chú |
|---|---:|---|
| 2026-07-18 | 0 | Tạo mục tiêu. Gate 0/5 — toàn bộ trọng tâm hiện tại vẫn là track 10K (backtest 22/200, playbook chưa thành văn). Mục tiêu này chỉ được kích hoạt sau khi funded 10K. |

## Liên kết
- Lộ trình: [[01 - Roadmap]], [[03 - Lộ trình chi tiết - Từ số 0 đến Funded 100K]]
- Chỉ số: [[02 - Skill Metrics]]
- Mục tiêu liên quan: [[Pass FTMO first package challenge (10K$)]], [[Pass The5er first package challenge (10k$)]], [[Become a consistently profitable ICT trader]]
