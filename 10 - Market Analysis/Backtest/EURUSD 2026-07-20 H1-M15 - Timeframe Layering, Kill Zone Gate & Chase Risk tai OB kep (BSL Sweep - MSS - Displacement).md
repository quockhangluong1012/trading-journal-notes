---
type: market-analysis
status: watchlist
date: 2026-07-20
symbol: EURUSD
timeframe: "H1 (bias/POI) → M15 (confirmation) → M5 (execution dự kiến), chart FXReplay/OANDA hiển thị UTC+0, giai đoạn quanh 26/6–3/7/2018"
session: replay
htf_bias: "D1 Bearish, H1 đồng bias. Draw on liquidity hướng về SSL 1.15266 (còn mở, chưa bị test lại). External BSL 1.16874/1.16919 đã bị quét TRƯỚC khi giá retrace xuống 2 OB đang xét — đây là bằng chứng củng cố narrative bearish, không phải điều kiện chờ để xuống khung."
setup: "Áp dụng Confirmation Timeframe Layering (H1→M15→M5, theo note 49) + Kill Zone GATE (theo note 18) cho một setup Short tại OB kép sau BSL sweep; đồng thời kiểm tra rủi ro chase khi FVG gốc của cú displacement đã bị bỏ lỡ."
in_trade: false
draw_on_liquidity: "SSL 1.15266 (target chính, chưa bị test lại kể từ cú sweep gốc). BSL 1.16874/1.16919 đã bị quét (external, xác nhận narrative bearish ở tầng H1). Pool nội bộ bên trong 2 OB — dùng làm mỏ neo cho MSS tại M15/M5 — CHƯA được xác nhận đã bị quét."
key_poi: "OB kép chồng tầng: tầng nông 1.16580–1.16700 (đã bị xuyên qua, không có phản ứng bullish rõ) và tầng sâu 1.16322–1.16419 (POI Khang chọn để tìm Short, giá đang test, chưa reclaim)."
invalidation: "(1) M15 đóng nến chấp nhận dưới 1.16322 và tiếp tục displacement giảm không hồi → đây là BOS tiếp diễn, không phải nơi chờ phản ứng — cần tìm POI premium mới ở tầng cao hơn cho Short, không phải mua kỳ vọng bật lên tại đây. (2) Giá đóng nến ngược lại xuyên qua toàn bộ OB kép và giữ trên 1.16700 → giả thuyết Short tại vùng này thất bại, cần xem lại toàn bộ bias ngắn hạn H1."
topic: "Confirmation Timeframe Layering (H1→M15→M5) chống nhiễu MSS khi nhảy fractal quá gấp; Kill Zone như một GATE cứng theo note 18 (không chỉ là yếu tố tăng xác suất như cách note Market Structure Shift diễn đạt — có một xung đột nhỏ giữa hai note cần lưu ý); rủi ro chase khi vào muộn tại OB tầng 2 thay vì FVG gốc của displacement (War Story W1 trong note Market Structure Shift); vai trò của external BSL sweep như bằng chứng củng cố narrative H1 chứ không phải trigger để xuống khung thấp hơn."
tags:
  - analysis
  - watchlist
  - EURUSD
  - timeframe-layering
  - kill-zones
  - liquidity-sweep
  - market-structure-shift
  - order-block
  - premium-discount
  - confirmation-timeframe
  - ict-2022
---

# EURUSD H1→M15 — Timeframe Layering, Kill Zone Gate & Chase Risk tại OB kép — 2026-07-20

> [!info] Trạng thái
> **WATCHLIST — không vào lệnh.** Note này tổng hợp 4 lượt trao đổi trong cùng một phiên: (1) đọc H1 tổng quan (dealing range, OB kép, BSL sweep), (2) đọc chi tiết M15 (chuỗi Sweep → MSS → Displacement), (3) làm rõ quy tắc "khi nào xuống khung" bằng [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)|Confirmation Timeframe Layering]], (4) áp thêm GATE thời gian bằng [[18 - Kill Zones]] để giải thích vì sao đứng ngoài là quyết định đúng. Đây là note phân tích/luyện framework, không phải log backtest có kết quả.

![[Pasted image 20260720075842.png]]
![[Pasted image 20260720075849.png]]

---

## 0. Bối cảnh & câu hỏi gốc

Khang gửi ảnh H1 của EURUSD (FXReplay/OANDA), D1 bias đang Bearish, hỏi cách phân tích tiếp khi giá đã "về 2 POI, quét lên trên BSL" nhưng không tìm được tín hiệu để xuống M5 xác nhận. Qua các lượt trao đổi, ba lớp vấn đề lần lượt lộ ra:

1. **Nhảy fractal quá gấp (H1→M5)** — đúng nguyên văn "Ca thực tế của Khang" đã ghi sẵn trong note 49: thiếu tầng M15 làm mỏ neo khiến M5 "mồ côi", mọi wiggle trông giống MSS.
2. **Nhầm lẫn giữa "trigger quan sát" và "trigger vào lệnh"** — giá lấy BSL bên ngoài trước đó là công việc xác nhận narrative ở tầng H1, không phải điều kiện chờ thêm để bấm nút xuống khung; trigger quan sát M15 thực ra chỉ đơn giản là **giá chạm POI**.
3. **Kill Zone GATE** — sau khi đọc kỹ M15 (ảnh thứ ba), Khang tự nhận ra toàn bộ chuỗi Sweep→MSS→Displacement trên H1 diễn ra **ngoài** London/NY Kill Zone, và dùng chính lý do đó để đứng ngoài — một chẩn đoán đúng, được xác nhận lại bằng note 18.

---

## 1. H1 — Cấu trúc, Bias & OB kép

![[EURUSD-H1-StructureMap-20260720.svg]]

| Mốc | Giá | Vai trò |
|---|---|---|
| Swing low lớn | **1.15266** | External SSL — draw on liquidity chính, chưa bị test lại |
| Swing high (lần 1) | 1.16743 / 1.16808 | Mức BSL bị quét trong lượt đọc đầu tiên |
| Swing high (đỉnh thật) | **1.16874 / 1.16919** | External BSL — đã bị quét, xác nhận xong vai trò |
| OB tầng nông | 1.16580 – 1.16700 | Đã bị xuyên qua trong đợt giảm, không có phản ứng bullish rõ |
| OB tầng sâu (POI) | **1.16322 – 1.16419** | POI Khang chọn để tìm Short, giá đang test |

**Equilibrium** = (1.15266 + 1.16919) / 2 ≈ **1.16093**. Cả hai OB (1.1658–1.1670 và 1.1632–1.1642) đều nằm **trên** mức này — tức vẫn ở **Premium** của dealing range, dù giá đã rơi khá sâu từ đỉnh sweep. Đây là điểm quan trọng: bán tại đây là bán tiếp diễn từ premium về SSL, không phải "đuổi xuống discount" — vị trí vẫn hợp lệ theo đúng logic Premium/Discount.

**Kết luận tầng H1:** Bias Bearish có draw on liquidity rõ (SSL 1.15266), external BSL đã bị quét xác nhận narrative, vị trí OB kép đúng phía Premium cho Short. Điều kiện tiên quyết ở tầng H1 đã thỏa — vấn đề nằm ở các tầng dưới.

---

## 2. M15 — Chuỗi Sweep → MSS → Displacement

Đọc trên ảnh M15 (UTC+0): giá tạo higher-highs/higher-lows từ đáy sweep 1.15266 lên đỉnh **1.16894–1.16920** (đây chính là cú BSL sweep). Sau một nhịp double-top nhẹ quanh 1.1680–1.1690, giá **phá xuống dứt khoát qua higher-low ~1.1670** bằng một chuỗi nến thân đen liên tục, không hồi — thoả đủ ba lớp: **Sweep** (BSL) → **MSS** (phá higher-low bằng thân nến đóng cửa) → **Displacement** (chuỗi nến cascade từ ~1.1680 xuống dưới 1.1660, tiếp tục rơi qua 1.1600, 1.1550, 1.1500... tới vùng OB sâu).

Điểm mấu chốt: cú displacement này đã **chạy hết quãng đường** trước khi Khang nhìn lại — nó vừa là bằng chứng M15 xác nhận (tốt), vừa tạo ra câu hỏi ở mục 5 bên dưới: FVG mà nó để lại nằm ở đâu, và giá hiện tại có đang chase một vùng đã cũ hay không.

---

## 3. Vấn đề Timeframe Layering — vì sao M5 "nhiễu"

![[TimeframeLayering-KillZone-Gate-20260720.svg]]

Quy trình gốc của Khang (H1 → M5 trực tiếp) bỏ qua tầng trung gian M15, khiến M5 không có mỏ neo để tự lọc nhiễu — đúng "Ca thực tế của Khang" trong [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)|note 49]]. Quy tắc rút ra trong phiên này:

- **Trigger 1 — bắt đầu quan sát M15:** ngay khi giá **chạm** đúng vùng POI H1 (Premium OB cho Short). Việc BSL bên ngoài đã bị quét trước đó là xác nhận narrative ở tầng H1, **không phải** điều kiện chờ thêm để bấm nút xuống khung.
- **Chạm POI ≠ xác nhận.** Quyền vào lệnh chỉ mở khi M15 tự hoàn thành chuỗi riêng của nó: một pool nội bộ (thường là một inducement) bị quét, rồi MSS bằng displacement để lại FVG.
- **Trigger 2 — xuống M5/M1 để refine entry:** chỉ sau khi M15 đã xác nhận xong toàn bộ chuỗi trên.

![[khi_nao_xuong_khung_h1_m15_m5.svg|697]]

![[Pasted image 20260720075916.png]]
---

## 4. Kill Zone GATE — vì sao đứng ngoài là đúng

Khang tự nhận ra chuỗi Sweep→MSS→Displacement trên H1 diễn ra **ngoài** London/NY Kill Zone, và dùng đó làm lý do không tìm lệnh. Đối chiếu [[18 - Kill Zones]] (note ở trạng thái `status: tested`, tức đã kiểm chứng): mục Quy tắc vô hiệu hóa ghi rõ **"Setup bị vô hiệu (không trade) khi: Ngoài kill zone"** — đây là điều kiện **CẦN**, ngang hàng với bias/sweep/POI, không phải một tuỳ chọn tăng xác suất.

> [!warning] Xung đột nhỏ giữa hai note cần lưu ý
> Note [[21 - Market Structure Shift|Market Structure Shift]] lại xếp Kill Zone vào nhóm "điều kiện tăng xác suất" (mềm hơn), trong khi note "Kill Zones" chuyên đề xếp nó vào nhóm "vô hiệu hóa" (cứng hơn). Vì note Kill Zones ở trạng thái `tested` và là note chuyên đề cho đúng chủ đề này, nó nên được ưu tiên làm nguồn tham chiếu chính. Đáng để Khang thống nhất lại giọng điệu giữa hai note này một lúc nào đó.

Quan trọng: đứng ngoài không có nghĩa là xoá level. Theo War Story **W2 "MSS đúng hình, sai giờ — và cú re-deliver"** trong [[20 - Liquidity Sweep]], một chuỗi hợp lệ về cấu trúc nhưng sai giờ thường được "giao lại" (re-deliver) trong kill zone/macro kế tiếp, với một cú quét sâu hơn và displacement thật. Cách làm đúng: giữ nguyên mốc + FVG như một "kịch bản treo", chờ London Open (13:00–16:00 VN mùa hè) hoặc NY AM (18:00–21:00 VN mùa hè) kế tiếp xem chuỗi có lặp lại đúng trong cửa sổ giờ đó không.

---

## 5. Chase Risk — FVG gốc bị bỏ lỡ vs OB sâu hơn

![[ChaseRisk-FVGGoc-vs-OBSau-20260720.svg]]

Cú displacement mạnh nhất (phá từ ~1.1680 xuống dưới 1.1660) nhiều khả năng để lại FVG hợp lệ ngay trong vùng **1.1660–1.1680** — trùng với một nhịp dừng nhỏ quan sát được trên M15. Nếu Khang chưa vào ở đó, đây mới là điểm entry mà mô hình 2022 gọi tên cho cú MSS này, **không phải** OB tầng sâu (1.1632–1.1642) mà giá đang test bây giờ.

Đúng như War Story **W1 "MSS quá hoàn hảo"** trong [[21 - Market Structure Shift]]: displacement càng mạnh, retrace về FVG càng nông; vào ở một vùng sâu hơn sau khi giá đã chạy hết một quãng dài không hồi là **chase**, không còn là retracement entry đúng nghĩa — trừ khi tầng sâu này tự cho ra một chuỗi mini sweep + MSS + FVG riêng của chính nó.

---

## 6. Checklist tổng hợp áp cho case này

| Hạng mục | Trạng thái |
|---|---|
| HTF bias xác định đúng, đồng hướng D1/H1 | ✅ Bearish |
| Draw on liquidity rõ (SSL 1.15266) | ✅ |
| External BSL sweep xác nhận narrative | ✅ 1.16874/1.16919 |
| Vị trí OB đúng phía Premium | ✅ cả 2 OB đều trên EQ ~1.16093 |
| M15 Sweep + MSS + Displacement hợp lệ | ✅ đã xảy ra (mục 2) |
| Kill Zone GATE | ❌ **Ngoài KZ — lý do chính để đứng ngoài** |
| FVG gốc của displacement đã dùng chưa | ❓ Có thể đã bỏ lỡ (vùng 1.1660–1.1680) |
| Entry tại OB sâu có mini sweep + MSS riêng chưa | ❌ Chưa — nến cuối mới chạm, chưa reclaim |
| Kết luận | **No Trade — chờ re-deliver đúng Kill Zone** |

---

## 7. Concept đã áp dụng

- [[49 - Confirmation Timeframe & Timeframe Layering (Khử nhiễu MSS trong 2022 Model)]] · [[01b - ICT 2022 Model - LTF Intraday (H1-M5-M1)]] · [[32 - Top-down Analysis (Multiple Timeframes)]]
- [[18 - Kill Zones]] · [[40 - Macro Times]]
- [[20 - Liquidity Sweep]] · [[21 - Market Structure Shift]] · [[13 - FVG  - Fair Value Gap]] · [[25 - OB - Order Block]]
- [[27 - Premium Discount]] · [[12 - Dealing Range]] · [[10 - Consequent Encroachment (Mean Threshold)]]
- [[01 - ICT 2022 Model]]

---

## 8. Bài học rút ra

1. **"Chạm POI" là trigger quan sát, không phải trigger vào lệnh.** Việc H1 đã lấy BSL bên ngoài trước đó là xác nhận narrative, không phải điều kiện chờ thêm để bấm nút xuống khung — nhầm hai việc này là nguồn gốc chính của cảm giác mơ hồ ban đầu.
2. **Thiếu tầng M15 khiến M5 "mồ côi".** Nhảy thẳng H1→M5 (cách nhau 12 lần nến) bắt M5 tự sinh xác nhận mà không có mỏ neo — đúng vấn đề note 49 đã cảnh báo trước.
3. **Kill Zone là GATE cứng, không chỉ là điểm cộng** — theo đúng note chuyên đề đã kiểm chứng (`status: tested`), và Khang đã tự áp đúng nguyên tắc này mà không cần nhắc.
4. **Một chuỗi hợp lệ nhưng sai giờ chưa chắc đã chết** — giữ nguyên mốc, chờ re-deliver trong kill zone kế tiếp, thay vì xoá bỏ toàn bộ giả thuyết.
5. **Displacement càng mạnh, FVG entry đúng nghĩa càng nông** — cần tỉnh táo phân biệt giữa "quay lại đúng chân displacement" và "chase xuống một tầng POI sâu hơn, cũ hơn".

---

## 9. Câu hỏi cần chốt (chưa xác nhận)

- Giờ chính xác (UTC) của cây nến MSS/displacement chính trên M15 — để verify chắc chắn nó nằm ngoài London Open (≈ UTC 06:00–09:00 giờ EDT mùa hè) và NY AM (≈ UTC 11:00–14:00).
- Xác nhận chế độ DST hiện tại của Mỹ (EDT hay đã EST) tại thời điểm dữ liệu chart — ảnh hưởng trực tiếp tới bảng quy đổi giờ.
- Biên chính xác của FVG trong vùng 1.1660–1.1680 (fvg_high/fvg_low) — cần zoom kỹ để xác nhận có bị bỏ lỡ hay không.
- Vai trò gốc của 2 OB (đây có phải bullish OB — vùng gốc của nhịp tăng 27/6 — hay một dạng PD array khác) để xác định giá đang test nó với tư cách BOS tiếp diễn hay cần một MSS riêng.
- Phản ứng thực tế của giá tại OB sâu (1.1632–1.1642) sau thời điểm ảnh chụp — đã có mini sweep + MSS trên M5 chưa, hay đã bị xuyên thủng?

## 10. Next steps

- Nếu Khang tiếp tục replay và giá thực sự cho ra mini sweep + MSS + FVG riêng tại OB sâu **trong đúng cửa sổ Kill Zone kế tiếp**, tạo một file backtest riêng theo [[Backtest template - POI & Step Decision (ICT 2022)]] trong `04 - Backtesting/`, cross-link ngược về note này.
- Lưu 3 ảnh gốc (2 H1 + 1 M15) vào `10 - Market Analysis/Attachments/` theo tên gợi ý ở đầu note để lần sau đối chiếu chính xác thay vì đọc lại ước lượng.
- Nếu tình huống "sequence hợp lệ nhưng sai giờ" lặp lại nhiều lần trong quá trình backtest, đây là ứng viên tốt để bổ sung một ví dụ số liệu cụ thể vào mục Best Practices của [[18 - Kill Zones]].
- Cân nhắc thống nhất lại giọng điệu giữa note [[21 - Market Structure Shift]] và [[18 - Kill Zones]] về việc Kill Zone là điều kiện "tăng xác suất" hay "vô hiệu hóa" (xem cảnh báo ở mục 4).

---
*Ghi chú: `date` = ngày thực hiện phân tích (VN, UTC+7), không phải ngày trên chart (chart là dữ liệu lịch sử FXReplay ~2018). Không log backtest vì không vào lệnh — đây là note phân tích/watchlist + luyện tập framework. Mọi mức giá là ước lượng đọc từ ảnh chụp màn hình, không phải giá trích xuất chính xác từ nền tảng — verify lại trên chart gốc trước khi dùng cho quyết định giao dịch thật.*
