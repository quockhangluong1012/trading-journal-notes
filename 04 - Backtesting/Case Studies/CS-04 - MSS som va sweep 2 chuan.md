---
type: case-study
id: CS-04
topic: mss-som-sweep-2-chuan
lenh_lien_quan: 1 (truc) + doi chieu nhieu Win
tags: [case-study, mss, sweep, ltf-inducement, doctrine]
---

# CS-04 · MSS sớm & sweep 2 chuẩn — GBPUSD 17/7 làm trục

## Bối cảnh

[[../2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long|GBPUSD 17/7/2014]] là note tham chiếu chính của toàn vault — mục 9.1 của chính note này đã tự phân loại lỗi thành "MSS sớm/LTF inducement" thay vì MSS thật. Case study này dựng lại anatomie của MSS đáng tin theo canon, đối chiếu với case này, và mở rộng sang vấn đề "sweep" bị dùng theo 2 chuẩn khác nhau xuyên vault.

![[CS-04-mss-som-sweep-2-chuan.svg|760]]

## Anatomie MSS đáng tin (theo canon, `ict-doctrine SKILL.md § MSS`)

> MSS = Reversal (phá swing **ngược** short-term move), thường **sau** sweep + displacement. Không phải mọi "structure trông khác đi".

Trình tự bắt buộc:
1. **Sweep** một liquidity cấu trúc có tên (không phải LTF swing bất kỳ).
2. **Displacement** — expansion một chiều, để lại imbalance.
3. **Body close** phá qua swing significant — đây là MSS thật.

## Case GBPUSD 17/7/2014 — MSS sớm

Theo mục 9.1 của note gốc: MSS được ghi nhận trên **tap đầu tiên** vào vùng giá, trong khi ERL (external range liquidity — ở đây là Range Low **1.70592**) theo hướng ngược lại **chưa từng bị quét**. Trình tự thực tế là:

- Swing LTF bị phá bởi một leg giá → ghi nhận "MSS".
- **Không có** sự kiện sweep cấu trúc có tên xảy ra TRƯỚC bước này.
- SL đặt tại **1.70840**, trong khi ERL thật (1.70592) còn cách một khoảng chưa bị test.

Kết quả: FVG hình thành từ leg này (1.70873–1.71103) được coi là mandate cho entry, nhưng nếu MSS không phải MSS thật (chỉ là LTF inducement — một cú đẩy giá tạm thời để dụ), FVG hình thành từ nó không có "tư cách" (mandate) structural để dùng làm POI.

## Doctrine gap: thứ tự ERL trước IRL

Note gốc mục 11 (doctrine check) đã ra ruling: **yêu cầu ERL phải bị quét trước khi tin IRL/MSS tại POI là một AMBIGUOUS/doctrine gap**, không phải FAIL cứng — canon không fix dứt điểm liệu MSS có bắt buộc phải xảy ra sau khi ERL cùng hướng bị quét hay không, trong mọi cấu trúc lồng nhau. Case study này **giữ nguyên ruling đó**, không tự đặt chuẩn khắt khe hơn canon.

Điều **không** phải doctrine gap: quan sát rằng ERL 1.70592 chưa bị quét khi MSS được ghi nhận là một **fact**, không phải một cách đọc — sự kiện đó có thể được xác nhận/phản bác bằng chart, không phụ thuộc vào việc doctrine có fix ranh giới ERL/IRL hay không.

## Vấn đề mở rộng: "sweep" dùng theo 2 chuẩn xuyên vault

Ngoài case trục, `batchD.md` xác nhận rule drift **hệ thống** ở field `liquidity_swept`/`idm_swept`, xuất hiện ≥3/5 lần trong cụm XAUUSD:

| Chuẩn | Mô tả | Ví dụ dùng đúng |
|---|---|---|
| Chuẩn 1 (đúng canon) | Lấy resting liquidity **có tên** (PDH/PDL/EQH/EQL/session level), giá trị số cụ thể | [[../2026-07-09/01 - Win - EURUSD - 2005-05-11- Short\|EURUSD 11/5/2005]] — neo EQH H1 = **1.28912** |
| Chuẩn 2 (lỏng) | "Giá chạm cạnh một PD array khác" (OB/FVG/Breaker), không kèm tên level thanh khoản | [[../2026-07-10/02 - Loss- EURUSD - 2021-05-07- Short\|EURUSD 7/5/2021]] — gọi "sweep cạnh trên OB" không nêu tên level trước khi coi là sweep |

Đối chiếu các Win có sweep đúng trình tự (chuẩn 1) — vd EURUSD 11/5/2005 — cho thấy khi sweep neo vào một level có tên cụ thể, chuỗi Sweep→Displacement→MSS rõ ràng hơn và không cần tranh luận về AMBIGUOUS. Ngược lại, các case dùng chuẩn 2 (kể cả không phải case Loss) đều khó phân xử dứt điểm bằng doctrine vì thiếu đối tượng tham chiếu rõ ràng để kiểm.

## Gate đề xuất (đo lường được)

1. Field `liquidity_swept`/`idm_swept` chỉ được ghi `Yes` khi kèm **tên level cụ thể** + giá trị số; thiếu tên → ghi `AMBIGUOUS`.
2. Trước khi tin một MSS là shift thật, kiểm tra xem ERL gần nhất theo hướng ngược lệnh đã bị quét chưa — nếu chưa, gắn cờ `mss_premature_risk: Yes` và hạ mandate của bất kỳ FVG hình thành từ MSS đó.
3. Backfill toàn bộ 22 lệnh với field mới này để đo tỷ lệ chuẩn 1 vs chuẩn 2 xuyên vault (hiện chưa có con số tổng, chỉ có xác nhận "≥3/5" ở một batch).

## Kết luận case study

Nhãn "MSS" của GBPUSD 17/7/2014 là **FAIL theo doctrine chặt** (thiếu sweep cấu trúc trước displacement) nếu áp chuẩn nghiêm; là **AMBIGUOUS/doctrine gap** nếu chấp nhận rằng canon không fix cứng thứ tự ERL/IRL trong mọi trường hợp — ruling chính thức tại note gốc đã chọn AMBIGUOUS, và case study này không lật ruling đó vì không có anchor mới. Vấn đề "sweep 2 chuẩn" là finding cấp vault độc lập, không riêng của case này.

## Liên kết

- [[../00 - Tong hop/00 - Backtest Dashboard & Statistics|Dashboard]]
- [[../00 - Tong hop/01 - Cross-Setup Devils Advocate (BACKTEST mode)|Cross-Setup Devil's Advocate]] — O7
- [[../00 - Tong hop/02 - Master Lesson Learned|Master Lesson Learned]] — bài học #1, #2
- Nguồn: [[../2026-07-17/02 - Loss - GBPUSD - 2014-07-17 - Long]] mục 9.1, 11; [[../2026-07-09/01 - Win - EURUSD - 2005-05-11- Short]]
