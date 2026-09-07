---
date: 2026-05-13
symbol: NDX
position: Long
result: Win
session: New York
setup: NQ Venom Model
entry_model: Market Structure Shift + Sell-side Liquidity + Order Blocks
entry_timeframe: 
higher_timeframe_bias: Bullish
bias_correct: 
entry_price: 29,127.5
take_profit: 29,320
stop_loss: 28,962
exit_price: 29,227.1
pnl: 180
r_multiple: 0.6
planned_rr: 1.16
risk_percent: 
confidence: 4
emotions:
  - Disciplined
tags:
  - MarketStructureShift
  - SellSideLiquidity
  - OrderBlocks
  - Displacement
  - PremiumVsDiscount
  - KillZones
  - DailyBias
  - Discount
source_id: 2019
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 1, material: 2, minor: 1}
da_opposite_case: "equally viable"
---
# Trade 2026-05-13 - NDX Long Win

## 0. Trade Summary

| Field | Value |
|---|---|
| Symbol | NDX |
| Position | Long |
| Result | Win |
| Session | New York |
| Setup | NQ Venom Model |
| Entry Model | Market Structure Shift + Sell-side Liquidity + Order Blocks |
| HTF Bias | Bullish |
| Premium/Discount | Discount |
| Power of 3 | Manipulation |
| Confidence | 4/5 (High) |
| Entry | 29,127.5 |
| Stop Loss | 28,962 |
| Take Profit | 29,320 |
| Exit | 29,227.1 |
| PnL | 180.0 |
| R Multiple (realized) |  |
| Planned RR |  |
| Risk % |  |
| Closed | 2026-05-12 23:29:00 |

---

## 1. Pre-market Bias & Analysis

- **Daily Bias (app)**: Bullish
- **Premium/Discount**: Discount
- **Power of 3 Phase**: Manipulation

============= D1 =============

- Daily Bias: Bullish - Giá đang trong trend tăng sau nhịp hồi
============= H1 =============

- Giá về vùng OB
============= M15 =============

- Giá thực hiện 1 pha quét thanh khoản bên dưới OB và 1 đáy cũ quan trọng
- Giá vá xuống cạnh dưới Venom box (8:00 - 9:30 AM NY)
============= M5 =============

- Sau khi qua phản ứng tại OB, giá bật hồi lên
- Giá hình thành BPR theo mô hình Venom
- Entry khi giá retrace về BPR

============= Result =============

- Giá chạy theo đúng chiến lược
- Thoát lệnh sớm trước khi gia đặt mục tiêu do đi ngủ

### Charts

![[NDX-20260513-2019-1.png]]
![[NDX-20260513-2019-2.png]]
![[NDX-20260513-2019-3.png]]
![[NDX-20260513-2019-4.png]]

---

## 2. Pre-trade Checklist

- [x] Higher timeframe (Daily/4H) bias is clearly bullish or bearish
- [x] Price is in a premium zone (shorts) or discount zone (longs)
- [x] Break of Structure (BOS) or Change of Character (CHOCH) confirmed
- [x] Previous liquidity (equal highs/lows, stops) has been swept
- [x] Market Structure Shift + Displacement
- [x] Fair Value Gap (FVG) or Order Block (OB) provides confluence
- [x] Trade is during an ICT Killzone (London/NY AM session)
- [x] Clear liquidity target identified (buy-side or sell-side)
- [x] No high-impact news events imminent (check economic calendar)
- [x] Rejection Validation When Enter PD Array Zones
- [x] Not exceeding daily loss limit -- will stop trading if hit
- [x] Stop loss is placed beyond the nearest structure level + Buffer
- [x] Risking no more than 0.5% of account equity

---

## 3. Execution Review

- Giá chạy theo đúng chiến lược
- Quan trọng là chờ giá hồi về vùng PR Array và kèm quét thanh khoản quan trọng
- Thoát lệnh sớm do phải đi ngủ

**Emotions**: Disciplined

---

## 4. Phân Tích Sau Lệnh

- **Result**: Win (Hit Take Profit)
- **Mistake chính**:
  - [[Mistake - ]]
- **Nguyên nhân gốc rễ**:
  - `(trống trong bản gốc — dựa trên dữ kiện có trong file: Execution Review tự ghi "Thoát lệnh sớm trước khi giá đạt mục tiêu do đi ngủ" — đây không phải Hit Take Profit theo đúng nghĩa TP đã định (29,320), mà là manual close ở 29,227.1, thấp hơn TP kế hoạch. Result field ghi "Win (Hit Take Profit)" không khớp với exit_price ≠ take_profit `(mâu thuẫn, xem O1 mục 8)`.)`.

---

## 5. Lesson Learned

### Bài học kỹ thuật

- (Bản gốc để trống — không có bullet gốc.)
- exit_price (29,227.1) ≠ take_profit (29,320) — chênh 92.9 điểm — nhưng Result field ghi "Win (Hit Take Profit)", trong khi narrative "Result" ở mục 1 và Execution Review đều xác nhận đây là **manual close sớm do đi ngủ**, không phải TP bị chạm. Đây là mâu thuẫn trực tiếp giữa field Result và 2 nguồn narrative khác trong cùng file (O1, load-bearing cho r_multiple/planned_rr).
- File này và `Win-01-Trade-2026-05-13-NDX-Long.md` có entry (29,127.5/29,127.50) và SL (28,962/28,962.00) giống nhau tuyệt đối nhưng TP khác (29,320 vs 29,227.10) và cùng pnl = 180 — cần xác định là 2 lệnh scale khác TP hay 2 bản ghi của cùng 1 lệnh (liên hệ mục 8 O2, và CS-O0′ cấp cross-setup).

### Bài học tâm lý

- (Bản gốc để trống.)
- Emotions "Disciplined" + Confidence 4/5 (High) — mức tự tin cao nhất trong cụm 05-13, đi kèm hành vi thoát lệnh sớm vì lý do sinh hoạt cá nhân (đi ngủ) chứ không phải theo tín hiệu kỹ thuật nào — đây là kỷ luật về mặt tâm lý (không FOMO, không hold quá) nhưng đồng thời là exit không theo plan kỹ thuật đã định (TP 29,320).

### Bài học quy trình & risk

- risk_percent để trống hoàn toàn — không thể kiểm lệnh này risk bao nhiêu %, khác với file `Win-01` cùng vùng entry ghi risk_percent 5% (liên hệ CS-O1). Không có cách xác nhận đây là 1 hay 2 lệnh với risk khác nhau.
- r_multiple ghi 0.6 nhưng planned_rr ghi 1.16 — hai số này phản ánh đúng thực tế "thoát sớm" (r_multiple thực tế 0.6 thấp hơn kế hoạch 1.16 vì TP chưa đạt), khác với cách ghi ở `Win-01` (nơi 0.6 là planned_rr, không phải r_multiple thực tế) — cùng con số 0.6 nhưng ý nghĩa khác nhau giữa 2 file, dễ gây nhầm khi so sánh chéo (O3).

### Rule cần thêm/cập nhật

- [ ] **KIỂM TRA ĐƯỢC**: field `Result` chỉ được ghi "Hit Take Profit" khi exit_price = take_profit (chênh lệch ≤ 1 tick); nếu exit_price khác take_profit, ghi "Manual Close" hoặc "Partial/Early Exit" — kiểm bằng so khớp 2 field mỗi lần lưu (đóng O1).
- [ ] **KIỂM TRA ĐƯỢC**: Khi phát hiện 2 file có entry+SL giống nhau tuyệt đối trong cùng ngày, bắt buộc ghi rõ trong frontmatter (field mới, ví dụ `related_trade:` hoặc `is_scale_of:`) liệu đây là lệnh độc lập, scale-in, hay bản ghi trùng — không để mặc định suy đoán (đóng O2, liên hệ CS-O0′).
- [ ] **KIỂM TRA ĐƯỢC**: Không thoát lệnh sớm vì lý do sinh hoạt cá nhân (đi ngủ) khi chưa đặt trailing stop hoặc partial TP tự động — nếu biết trước sẽ không thể theo dõi lệnh, đặt OCO/partial TP tại các mốc R cụ thể trước khi vào lệnh (đóng finding tâm lý ở trên).

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only + 4 link chart Obsidian chết. Sufficiency: **thin** cho structure claims (MSS/OB/sweep — chỉ "Yes" tự ghi), nhưng mâu thuẫn Result/exit_price là kiểm được thuần túy từ số liệu đã cho.

**Thesis & claims**:
- C1: HTF bias Bullish, Long khớp hướng, Discount zone — claim văn xuôi.
- C2: MSS + Sell-side Liquidity sweep + OB là entry model — checklist 13/13 tick `[x]`, không có dòng nào unchecked (khác hẳn `Win-01` cùng ngày có 1 dòng unchecked).
- C3 (load-bearing): Result = "Win (Hit Take Profit)" — lệnh thắng vì đạt đúng mục tiêu TP đã định.
- C4: r_multiple = 0.6, planned_rr = 1.16 — thực hiện chỉ đạt 52% (0.6/1.16) của kế hoạch.

Suy luận: C3 mâu thuẫn trực tiếp với C4 và với narrative "Result" (mục 1) — nếu TP thật đã đạt (29,320), r_multiple phải bằng planned_rr (1.16), không phải 0.6.

**Điều gì đứng vững**: Arithmetic realized R-multiple khớp — risk = |29,127.5 − 28,962| = 165.5; realized reward = |29,227.1 − 29,127.5| = 99.6; r_multiple thật = 99.6/165.5 = **0.602** ≈ field `r_multiple: 0.6`. Planned reward = |29,320 − 29,127.5| = 192.5; planned RR = 192.5/165.5 = **1.163** ≈ field `planned_rr: 1.16`. Cả hai field frontmatter tự nhất quán với nhau và với arithmetic — đây là điểm hiếm hoi trong sample có r_multiple thực và planned_rr tách biệt đúng và khớp toán hoàn toàn.

**Objections**:

**O1 · [SELF-CONTRADICTION] · fatal · attacks C3 (load-bearing)**
Claim: "Result: Win (Hit Take Profit)" (section 4).
Evidence: exit_price = 29,227.1 ≠ take_profit = 29,320 (chênh 92.9 điểm, không phải rounding); narrative "Result" mục 1: "Thoát lệnh sớm trước khi giá đặt mục tiêu do đi ngủ"; Execution Review: "Thoát lệnh sớm do phải đi ngủ". Ba nguồn (arithmetic, narrative mục 1, Execution Review) đều xác nhận đây là **manual close sớm**, không phải TP bị chạm.
Consequence: field "Result: Hit Take Profit" là sai — nhãn kết quả không phản ánh đúng cách lệnh thực sự đóng. r_multiple thật (0.6) là hệ quả trực tiếp của việc thoát sớm, không phải hệ quả của một TP kế hoạch được đạt đúng.
Your best answer: "Có thể có TP từng phần (partial) đã hit trước, phần còn lại đóng sớm." — Không có field nào trong file ghi partial TP hoặc nhiều lần exit; chỉ có một `exit_price` duy nhất.
Retracted by: xác nhận có TP từng phần đã chạm trước khi đóng phần còn lại — hiện không có trong file.

**O2 · [UNSUPPORTED] · material** — File này và `Win-01-Trade-2026-05-13-NDX-Long.md` có entry (29,127.5) và SL (28,962) giống nhau tuyệt đối, cùng pnl = 180, nhưng TP khác nhau (29,320 vs 29,227.10) — không đủ dữ liệu (không timestamp phân biệt, không field `related_trade`) để xác định đây là 2 lệnh scale-out của cùng một setup, hay một lệnh bị ghi 2 lần với TP khác nhau do nhầm lẫn, hay 2 sự kiện giao dịch độc lập trùng vùng giá. Nếu là bản ghi trùng, cách 2 file có TP khác nhau (không giống pattern CS-O0′ đã ghi ở cặp Loss-05-13, nơi TP giống tuyệt đối) làm khả năng "trùng hoàn toàn" thấp hơn, nhưng entry+SL giống tuyệt đối vẫn là bằng chứng mạnh cho khả năng liên quan trực tiếp (cùng setup, scale khác mục tiêu). Retracted by: xác nhận từ user + timestamp phân biệt.

**O3 · [METHOD] · material** — Checklist section 2 của file này tick 13/13 `[x]` hoàn hảo (bao gồm cả "Not exceeding daily loss limit" và "Clear liquidity target identified" — 2 dòng không có trong checklist của `Win-01` cùng ngày, cùng entry zone). Hai file cùng lệnh/cùng vùng entry nhưng dùng 2 template checklist khác nhau (13 dòng vs 13 dòng khác nội dung), khiến không thể đối chiếu chéo trực tiếp xem 2 "lệnh" (hoặc 1 lệnh ghi 2 lần) có nhất quán về điều kiện entry hay không. Retracted by: chuẩn hóa 1 template checklist duy nhất cho các lệnh liên quan.

**O4 · [DOCTRINE] · minor** — Confidence 4/5 (High) + Emotions "Disciplined" được ghi cho một lệnh mà Result field tự mâu thuẫn (O1) — điểm tự tin cao không tương ứng với độ chính xác của chính việc ghi log kết quả. Đây không phải lỗi doctrine ICT, nhưng là gap giữa "tự tin vào quá trình" và "chính xác trong ghi chép" đáng lưu ý khi dùng field confidence để so sánh chéo giữa các lệnh. Retracted by: không cần, ghi nhận biên.

Drafted 4, cut 0.

**Verdict**: **BROKEN** — load-bearing claim C3 (Result = Hit Take Profit) sai trực tiếp so với 3 nguồn độc lập trong cùng file (arithmetic, narrative Result, Execution Review) — đây là lỗi ghi nhãn kết quả rõ ràng, không cần chart để phán (O1).
Tôi đã tấn công gì mà không phá được: r_multiple/planned_rr arithmetic (0.6 và 1.16 đều khớp công thức chính xác); hướng lệnh Long khớp bias Bullish; tính nhất quán tâm lý (Disciplined khớp với hành vi không FOMO, dù không khớp với việc bỏ lỡ TP kế hoạch).
Critique này KHÔNG xác lập: (1) MSS/OB/sweep có tồn tại thật trên chart; (2) quan hệ thật với `Win-01` (1 hay 2 lệnh — O2 để mở); (3) liệu nếu không thoát sớm, giá có thực sự đạt 29,320 hay không — đây là counterfactual không kiểm được.

**Opposite Case**: Đổi vai "thoát lệnh sớm" — thay vì đọc là lỗi ghi nhãn Result (O1), đọc như một quyết định quản trị lệnh chủ động và đúng đắn: "Disciplined" + Confidence cao phản ánh việc chủ động chốt lời sớm để bảo toàn 0.6R thực tế thay vì risk giữ lệnh qua đêm không giám sát (đi ngủ) chờ đạt 1.16R kế hoạch — và Result "Hit Take Profit" đơn giản là lỗi đánh máy/chọn dropdown sai (nên chọn "Manual Close"), không phản ánh gì sâu hơn về chất lượng quyết định.
Load-bearing claim của kèo ngược: quyết định thoát sớm là chủ động và có chủ đích quản trị rủi ro overnight, không phải một sai lệch ghi nhận cần sửa.
Strongest self-objection: nếu là quyết định chủ động, tại sao Execution Review dùng chữ "do đi ngủ" (lý do sinh hoạt cá nhân) thay vì lý do quản trị rủi ro overnight rõ ràng (vd "không muốn hold qua đêm không giám sát")? Cách diễn đạt gốc nghiêng về "bị buộc phải thoát" hơn là "chọn thoát vì lý do risk management".
Strength label: **equally viable** — cả hai đọc đều giải thích được hành vi thoát sớm bằng đúng cùng câu chữ "do đi ngủ"; không có fact nào phân biệt "thoát vì buộc phải" và "thoát vì chủ động quản trị risk overnight" — cả hai chỉ là gán ý nghĩa khác cho cùng một câu.
Observable duy nhất phân biệt hai reading: có tồn tại kế hoạch quản trị risk overnight nào được viết TRƯỚC lệnh này không (vd rule "luôn đóng lệnh trước khi ngủ nếu chưa đạt TP") — nếu có, kèo ngược (chủ động) đúng hơn; nếu không, thesis gốc (lỗi ghi nhãn Result, thoát sớm bị ép buộc bởi hoàn cảnh) đúng hơn. Không có trong file.

## 9. Opposite Case (Counter-Argument)

(Đã trình bày ở mục 8 — Opposite Case, xem trên. Riêng câu hỏi "đây và Win-01 là 2 lệnh scale hay ghi trùng" không đủ observable để dựng thành opposite case tách biệt — xem O2 ở mục 8.)

## 10. Falsification Tests

1. **Test cho O1**: Kiểm tra broker/platform log thật của lệnh này — nếu có 2 exit riêng biệt (partial TP + manual close phần còn lại), O1 giảm về `material`; nếu chỉ có 1 exit duy nhất tại 29,227.1, O1 giữ `fatal` và Result field cần sửa thành "Manual Close".
2. **Test cho O2**: Xin timestamp giờ:phút của file này và `Win-01` — nếu cách nhau đủ xa (khác session rõ, vd Win-01 tính là London theo bảng Summary còn file này New York) với diễn biến giá khác nhau ở giữa, đây là 2 lệnh riêng (đóng O2 theo hướng "không trùng, là scale/lệnh riêng hợp lệ"); nếu trùng giờ, nghi vấn ghi trùng tăng lên `fatal`.
3. **Test cho O3**: Chuẩn hóa 1 template checklist cho mọi lệnh trong cụm 05-13, đối chiếu lại xem tick có đồng nhất giữa các file mô tả cùng vùng giá — nếu tick khác nhau dù dùng chuẩn thống nhất, đây là bằng chứng cho 2 lệnh độc lập với điều kiện entry khác nhau thật.
