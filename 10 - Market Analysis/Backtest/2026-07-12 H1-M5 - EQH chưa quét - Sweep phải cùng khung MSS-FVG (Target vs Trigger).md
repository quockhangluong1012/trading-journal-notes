---
type: market-analysis
status: backtest
date: 2026-07-12
symbol: chưa xác định rõ (chart replay, vùng giá ~1.74–1.75, có thể GBPUSD, mốc chart Oct 2008)
timeframe: H1 (POI) / M5 (entry)
session: replay
htf_bias: bearish (D1 cấu trúc LH/LL, EQL bên dưới làm draw)
setup: 2022 Model - reversal tại Order Block H1 (premium)
in_trade: false
draw_on_liquidity: "target: SSL/EQL dưới | phía trên OB: EQH (BSL) - unfinished"
key_poi: Order Block H1 1.75360 - 1.74360 (premium)
invalidation: đóng cửa H1 trên đỉnh phản ứng (trên mép OB) / mất cấu trúc giảm
topic: sweep phải cùng khung với MSS & FVG - EQH là target không phải trigger
tags:
  - analysis
  - methodology
  - ict-2022
  - liquidity-sweep
  - order-block
  - timeframe-alignment
  - target-vs-trigger
  - premium-discount
---

# H1-M5 — EQH chưa quét: Sweep phải cùng khung với MSS/FVG (Target vs Trigger) — 2026-07-12

> [!info] Trạng thái
> **METHODOLOGY / REVIEW — không vào lệnh (miss).** Ghi lại một tình huống lặp lại: giá đảo chiều **ngay từ Order Block H1** nhưng vì đang chờ một vùng **EQH phía trên** bị quét, đã **không vào lệnh** dù M5 đã cho MSS. Đây là lỗi **lệch khung (scale mismatch)**, không phải lỗi thực thi. Khái niệm nền: [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]].

![[EQH-target-vs-trigger-20260712.svg]]

> [!warning] Screenshot gốc
> Ảnh chart H1 gốc chưa lưu dạng file. Kéo ảnh vào `10 - Market Analysis/Attachments/` (nên có nhãn symbol + khung) rồi thêm `![[tên-ảnh.png]]` bên dưới để embed. Sơ đồ ở trên là minh họa nguyên lý, không phải chart thật.

## 1. Bối cảnh & kế hoạch ban đầu

Top-down [[32 - Top-down Analysis (Multiple Timeframes)|D1 → H1 → M5]]:

- **D1 — Bias:** cấu trúc **LH/LL**, phía dưới có vùng **EQL** làm [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|draw]] → **Bias Bearish**.
- **H1 — POI:** [[25 - OB - Order Block|Order Block]] **1.75360 – 1.74360** trong [[27 - Premium Discount|premium]]. Kế hoạch: chờ giá retrace về OB, phản ứng, đảo chiều xuống thuận bias.
- **Điều đã xảy ra:** giá retrace tới OB, **quét qua [[10 - Consequent Encroachment (Mean Threshold)|CE]] và qua cạnh trên OB rồi đóng cửa vào lại OB**. Phía trên OB có vùng **EQH (4 đỉnh ngang)** = một bể [[07 - Buy-side Liquidity|BSL]] lớn cấp H1.
- **Quyết định (chỗ sai):** vì giá **không quét EQH phía trên**, kết luận "chưa có [[20 - Liquidity Sweep|liquidity sweep]]" và **không vào** khi M5 tạo [[21 - Market Structure Shift|MSS]] quay xuống.

## 2. Chẩn đoán — hai lỗi, một gốc

**Gốc:** để một bằng chứng **vắng mặt** (cú quét EQH) phủ quyết một bằng chứng **hiện diện** (M5 MSS tại POI).

**Lỗi #1 — "chưa có liquidity sweep" là sai về sự kiện.** Chính mô tả "quét qua CE + qua cạnh trên OB rồi đóng vào OB" **đã là một liquidity sweep**: cây nến wick lên xuyên mép trên OB đã quét sạch buy stops (BSL cục bộ, các short-term high) đậu ngay trên OB, rồi từ chối. Cú sweep *đã* xảy ra — chỉ là ở một bể khác, gần hơn, nhỏ hơn.

**Lỗi #2 — lệch khung (scale mismatch).** Trong mô hình [[01 - ICT 2022 Model|2022]], chuỗi **Sweep → MSS → FVG diễn ra CÙNG một khung** — khung entry (M5). Cú sweep mà M5 MSS cần là một cú quét **cấp M5** (STH tại POI), **không phải** cú quét vùng **EQH cấp H1**. Việc nâng bể H1 lên đóng vai trò mà một bể M5 phải đảm nhiệm chính là lệch khung → trigger không bao giờ "đủ" theo tiêu chí sai đó → đứng nhìn lệnh trôi. Chi tiết: [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]].

## 3. Đọc đúng chuỗi tín hiệu

> [!summary] Trình tự hợp lệ
> **D1 bias giảm → H1 POI = OB premium → giá tap OB, quét CE + BSL cục bộ trên OB, đóng lại → M5 displacement + MSS xuống → FVG entry → target SSL/EQL dưới.**

- Cú quét cục bộ trên OB + M5 MSS = **trigger đầy đủ, cùng scale** → **được phép vào** (SL trên đỉnh phản ứng, target [[30 - Sell-side Liquidity|SSL]] dưới).
- **M5 MSS là trọng tài**: nó bắn ra tại OB nghĩa là thị trường báo "đảo chiều bắt đầu TẠI ĐÂY, không phải tại EQH".

## 4. Mâu thuẫn "purge EQH trước hay không?" — để M5 phân xử

Nỗi lo của bạn **có cơ sở ICT thật**: 4 đỉnh ngang phía trên là bể BSL béo, giá *có thể* chạy lên "dọn" nó trước khi đảo (kịch bản purge-then-reverse). Nhưng không thể biết trước chắc chắn, nên đừng chọn bằng cảm tính — để [[16 - Internal & External Range Liquidity (IRL & ERL)|cấu trúc]] M5 quyết theo thời gian thực:

1. Giá vào OB, quét CE + mép trên OB, đóng lại → **chờ M5**.
2. M5 có displacement + MSS + FVG (lý tưởng thêm SMT) → **đảo chiều bắt đầu tại OB, vào. Không cần EQH.** ← *ca này*.
3. M5 **không** xác nhận, giá cứ đẩy lên → khi đó mới là kịch bản purge EQH; chờ giá quét EQH rồi mới tìm M5 MSS.

## 5. EQH = TARGET, không phải TRIGGER

- **Draw/Target:** EQL/SSL dưới (theo bias D1) là nơi giá **hướng tới**; EQH trên OB là *unfinished business* — mục tiêu cho tương lai hoặc rủi ro cạnh tranh, **không phải điều kiện vào lệnh**.
- Đòi giá lên quét EQH mới cho short *từ dưới* EQH thường **tự mâu thuẫn**: nếu giá thật sự lên quét EQH, OB có thể đã bị phá và setup không còn giá trị. Bạn chờ một điều kiện mà nếu nó xảy ra thì thường *hủy* chính setup.
- Kiểm chứng: kéo chart sang phải sau mốc này xem EQH có bị quét ở nhịp sau không (draw cho tương lai).

## 6. Kỷ luật & quy tắc rút ra

> [!warning] Đừng để bể HTF làm trigger
> "Chờ" chỉ là kỷ luật khi mình chờ **đúng** điều kiện của entry model. Chờ một bể HTF bị quét — khi entry model M5 không yêu cầu điều đó — là **lỗi**, không phải kiên nhẫn.

- Trước setup, ghi rõ: **TRIGGER = sweep + MSS + FVG cấp M5 tại POI**; **TARGET = EQH/EQL cấp HTF**.
- Cú sweep cho entry phải **cùng khung** với MSS/FVG.
- Nếu bể HTF quá sát/béo ngay trên POI → hạ size / scale-in, đừng biến nó thành lý do bỏ lệnh.
- Bổ sung vào checklist: *"POI của tôi có phải chính là mốc liquidity không? Nếu không → không lấy cú quét bể HTF làm điều kiện vào lệnh."*

## 7. Câu hỏi cần chốt (để log chính xác)

- **Symbol + khung chart thật** (xác nhận OB là gốc displacement thật — tiêu chí A+).
- Cây retrace vào OB **đã quét STH/equal-highs cục bộ nào** trên khung entry? (Có → độ tin cậy reversal cao hơn.)
- M5 MSS có **displacement + FVG** rõ không, hay chỉ là wick? (Body close mới tính.)
- SMT với cặp tương quan (nếu forex): có phân kỳ tại đỉnh phản ứng không?

---
*Ghi chú: date = ngày capture (VN, UTC+7). Không log backtest vì không vào lệnh (miss) — đây là note phương pháp/review. Giá OB do người dùng cung cấp; symbol/mốc chart chưa xác nhận. Sơ đồ minh họa nguyên lý, không phải chart thật.*
