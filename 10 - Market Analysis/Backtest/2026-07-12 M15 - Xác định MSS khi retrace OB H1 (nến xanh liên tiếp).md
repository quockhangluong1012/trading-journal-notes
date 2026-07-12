---
type: market-analysis
status: backtest
date: 2026-07-12
symbol: chưa xác định (ảnh chart không có nhãn symbol)
timeframe: M15 (POI trên H1)
session: replay / chart không nhãn
htf_bias: chưa xác nhận (cần HTF H1/H4)
setup: 2022 Model - reversal tại Order Block H1 (premium)
in_trade: false
draw_on_liquidity: BSL phía trên OB (chưa rõ mốc)
key_poi: Order Block H1 (premium)
invalidation: giá đóng cửa trên đỉnh OB / không tạo được MSS
topic: cách xác định MSS khi không có swing low trong chuỗi nến một chiều
tags:
  - analysis
  - methodology
  - ict-2022
  - market-structure-shift
  - order-block
  - displacement
  - premium-discount
---

# M15 — Xác định MSS khi retrace OB H1 (nến xanh liên tiếp) — 2026-07-12

> [!info] Trạng thái
> **METHODOLOGY / WATCHING — không vào lệnh.** Note này ghi lại cách xử lý một tình huống lặp đi lặp lại: giá retrace về **[[25 - OB - Order Block|Order Block]] H1** bằng một chuỗi **nến xanh liên tiếp**, và câu hỏi "làm sao xác định [[21 - Market Structure Shift|MSS]] khi không có swing low?".

![[MSS-no-swing-low-diagram-20260712.svg]]

> [!warning] Screenshot gốc
> Ảnh chart M15 gốc chưa được lưu dạng file. Hãy kéo ảnh vào `10 - Market Analysis/Attachments/` (hoặc `05 - Live Trading Journal/Screenschoots/2026/07/`) rồi thêm dòng `![[tên-ảnh.png]]` bên dưới để embed. Ảnh nên có nhãn symbol + khung thời gian để phân tích chính xác POI.

## 1. Vấn đề — "nến xanh liên tiếp" nghĩa là MSS *chưa* tồn tại

Đây là điểm cốt lõi, và nó đảo ngược cách đặt câu hỏi: nếu đang có chuỗi nến xanh liên tiếp mà "không tìm thấy swing low", thì **không phải tìm sai — mà là MSS chưa hình thành.** Không có mốc tham chiếu thì về mặt định nghĩa chưa thể có Market Structure Shift.

[[21 - Market Structure Shift|MSS]] (nghĩa reversal, phân biệt với BOS tiếp diễn) là hành động giá **đóng cửa phá qua short-term swing point gần nhất theo hướng ngược lại**, kèm displacement. Trong một chuỗi nến xanh đi lên vào OB, mỗi nến chỉ tạo higher high / higher low — nghĩa là **chưa có [[01 - Advance Market Structure ( Short Term Low, Intermediate Term Low & Long Term Low )|short-term low (STL)]] hợp lệ nào** để một cú giảm phá xuống. Swing low chuẩn ICT là fractal 3 nến: nến giữa có low thấp nhất, hai nến kề có low cao hơn. Chuỗi nến một chiều không thỏa mãn điều đó ở bất kỳ đâu.

→ **STL đầu tiên chỉ ra đời sau cú pullback đầu tiên** — cụ thể là nến down-close đầu tiên bẻ gãy nhịp tăng. Trước thời điểm đó, không có gì để phá; mọi ý định "short vì đã chạm OB" đều là *anticipate*, không phải *confirmation*.

## 2. Quy trình xác nhận MSS — 3 bước (đúng như sơ đồ)

> [!summary] 3 bước
> **① Chờ pullback đầu tiên tạo STL.** Khi nhịp xanh chững lại trong OB, nến giảm đầu tiên (hoặc cụm 2–3 nến tạo một đáy nhỏ) chính là STL đầu tiên → đây là **mốc tham chiếu MSS**. Đánh dấu cái low đó.
> **② Xác nhận lower high / phản ứng từ OB.** Lý tưởng: giá đẩy lên lại nhưng tạo high thấp hơn, hoặc chỉ retest mép OB rồi từ chối — dấu hiệu phe mua cạn lực trong vùng premium.
> **③ Displacement đóng cửa dưới STL = MSS.** Bắt buộc là **body close** phá STL, tốt nhất bằng nến [[35 - Aggressive Displacement Entry|displacement]] thân dài để lại [[13 - FVG  - Fair Value Gap|FVG]]. Một wick chọc xuống rồi đóng lại phía trên **không tính** — đó thường chỉ là quét thanh khoản.

Sau MSS: entry khi giá retrace vào FVG / LTF OB do chính cây displacement để lại (kết hợp [[26 - OTE - Optimal Trade Entry|OTE]] nếu có).

## 3. Vũ khí thực dụng: drop xuống LTF (M5/M3/M1)

Đây là câu trả lời sát nhất cho "M15 không có swing low". **Một nến xanh M15 = một chuỗi nhiều nến M5/M1**, và bên trong luôn có cấu trúc vi mô. Cái mà M15 hiển thị như "nến xanh liền mạch không đáy" thì trên M5/M1 sẽ có các internal short-term low rõ ràng.

Quy trình [[01 - ICT 2022 Model]] chuẩn: **HTF (H1) cho bias + POI (cái OB) → LTF (M5/M1) cho MSS + entry.** Không ép M15 phải có MSS; để giá chạm OB H1 rồi **soi MSS trên khung nhỏ hơn**. MSS đầu tiên gần như luôn xuất hiện ở LTF trước khi M15 kịp in ra một đáy — vừa cho entry sớm hơn, vừa cho stop chặt hơn (R cao hơn), đổi lại đòi hỏi kỷ luật chờ body close vì noise LTF nhiều hơn.

## 4. Điều kiện tiên quyết — cái OB phải có *lý do* để đảo chiều

MSS chỉ đáng tin nếu vùng OB có confluence. Kiểm tra trước khi săn MSS:

| Kiểm tra | Câu hỏi |
|---|---|
| Liquidity | Giá có [[20 - Liquidity Sweep\|quét]] một [[07 - Buy-side Liquidity\|BSL]] (đỉnh cũ / equal highs) tại/trên OB không? |
| Vị trí | OB có nằm trong [[27 - Premium Discount\|premium]] của [[12 - Dealing Range\|dealing range]], giá đã chạm [[10 - Consequent Encroachment (Mean Threshold)\|CE]] của OB chưa? |
| Bias | HTF bias có thực sự ủng hộ short, hay đang fade một trend tăng còn nguyên? |

Reversal mạnh nhất xảy ra **sau** một liquidity sweep, không phải khi giá chỉ "chạm rồi quay". Nếu OB bị chạm mà **không sweep, không lý do** → "nến xanh liên tiếp ăn thủng OB" là kịch bản mặc định, và việc không tìm thấy MSS chính là thị trường nói đây **không phải** setup. Đó là tín hiệu đứng ngoài.

## 5. Kỷ luật — cảnh báo thẳng

> [!warning] Đừng anticipate
> Short vào một chuỗi nến tăng mạnh chỉ vì "đã tới OB" là counter-trend guessing — đúng loại lỗi mà mô hình 2022 sinh ra để loại bỏ. **MSS là điều kiện bắt buộc, không phải tùy chọn.** Không có STL → không có mốc → không có MSS → **không có lệnh. Chờ.**

## 6. Về chart cụ thể + câu hỏi cần chốt

Ảnh gửi là chart M15 zoom, **không nhãn giá/symbol/khung**, nên chỉ suy đoán được: vùng xám phía trên ≈ OB/supply (draw phía trên); đường cam chấm-gạch có thể là CE/equilibrium của dealing range; đường xanh nét đứt dưới đáy ≈ một [[30 - Sell-side Liquidity|SSL]] đã bị quét.

Cần chốt để phân tích chính xác:

- **HTF bias (H1/H4) là gì**, và đang định short hay long tại OB này?
- Chuỗi nến xanh đi vào OB **đã quét BSL / equal highs nào chưa**, hay chạm OB từ giữa hư không? Có sweep → độ tin cậy reversal cao hơn hẳn.
- Symbol + khung thời gian (để xác định OB có phải gốc displacement thật — tiêu chí A+).

---
*Ghi chú: date = ngày capture (VN, UTC+7). Không log backtest vì không vào lệnh — đây là note phương pháp. Sơ đồ là minh họa nguyên lý, không phải chart thật.*
