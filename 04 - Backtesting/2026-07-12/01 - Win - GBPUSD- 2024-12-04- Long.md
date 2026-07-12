---
type: backtest
backtest_date: 2026-07-12
trade_date: 2024-12-04
symbol:
  - GBPUSD
position: Long
result:
  - Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct:
  - Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.26615
stop_loss: 1.26494
take_profit: 1.27027
r_planned: 3.4
r_multiple: 3.4
grade: A
followed_plan: Yes
tags:
  - backtest
  - ICT2022
---

# Backtest 2024-12-04 — GBPUSD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên GBPUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | GBPUSD         |
| Trade Date (dữ liệu) | 2024-12-04     |
| Position             | Long           |
| Result               | Win            |
| Session              | New York       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bullish        |
| Bias Correct?        | Yes            |
| Entry                | 1.26615        |
| Stop Loss            | 1.26494        |
| Take Profit          | 1.27027        |
| R Planned            | 3.4           |
| R Multiple (kết quả) | 3.4           |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
	  - Giá đang trong Order Block (tổng quát) Bullish
	  - Tuy nhiên leg gần nhất là 1 Bearish displacement
	  - Sau đó giá có nhịp PullBack hồi lên
	  - Giá vừa quét các old lows, phía trên còn 1 FVG D1 chưa bị mitigate
	  - Lúc này Bias vẫn chưa được xác nhận chính xác, tạm thời tôi đang xác định là Bullish
	  - Bias confirm khi H1 retrace về vùng POI (Order Block) và khung M5 quét OB đó sau đó hình thành CISD nuốt trọn nhịp giảm quét OB trước -> Khi này tôi xác nhạn Bias là Bullish
	  - DOL phía trên là Dealing Range High khung H1 và FVG chưa mitigated khung D1
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: 
	  - H1 Dealing Range High (1.27497)
	  - D1 FVG (1.28586 - 1.27688)
  - Sell-side liquidity: Old low: 
	  - Giá đã quét SSL, SSL hiện tại là old low vừa tạo ra (1.24852)
	  - 1 FVG bến dưới: 1.24187 - 1.23954

![[Pasted image 20260712160925.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- HH/HL
- **Dealing Range**: 
	- High: 1.27497
	- Low 1.26164
	- Giá đang trong vùng Discount cho setup Long
- **POI chính**: 
	- OB vùng 1.26642 - 1.26515
- **Liquidity cần chờ sweep**:
  - Swing low phía dưới OB
  - Vùng OB

### Phân Tích:
	- Cấu trúc H1 đang là HH/HL, Order Flow đang là Bullish
	- Tuy nhiên giá đang ở vùng EQ (50%)
	- Bến dưới có 1 vùng OB hình thành từ nhịp displacement lên đỉnh cũ (1.26642 - 1.26515), tại thời điểm 9:00 AM ngày 04/12/2024
	- Giá retrace về vùng OB này vào thời điểm 16:00 ngày 04/12/2024
	- Xuống khung M5 quan sát giá

![[Pasted image 20260712161058.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Khi giá retrace về vùng OB, 1 câ nến Bearish displacement mạnh đóng nến xuyên qua bên kia (xuống cạnh dưới và ra ngoài OB) OB kèm râu nến
	- Sau đó giá xuất hiện nhiều nến Bullish liên tiếp (có nến thân lớn) nuốt trọng cây nến Bearish displacement (đóng qua OB) trước đó hình thành 1 ** CISD **
	- Giá Quay lại cạnh trên của OB
	- Nhịp CISD đó kèm theo 2 FVG: 1 FVG nằm bên trên OB, 1 FVG nằm ngay CE của OB
	- Sau đó giá retrace về xuyên thùng FVG 1 (trên OB)
	- Giá sau đó retrace về FVG 2 (ngay CE của OB)
	- Tuy nhiên giá chưa chạm tới FVG đã quay đầu
	- Sau nhiều lần backtest tôi nhận ra 1 điều mặc dù vùng CE là điểm entry rất tốt (cho RR đẹp, theo sách giáo khoa) , sẽ có rất nhiều trader đặt Limit order tại đó (điểm này là tôi tự nghĩ sau khi backtest, chưa có bằng chứng cụ thể) -> Lệnh của họ sẽ không được trigger -> lỡ mất 
	- Tôi thấy giá khi retrace rất hay quay về vùng giữa CE và 1 cạnh rồi quay đầu (những lệnh backtest gần đây), tôi cũng bị lỡ 1 số lệnh khi chờ giá về CE
- **Entry trigger**:
	  - Liquidity Sweep: 
		  - Quét các old lows tạo ra trước đó 
		  - Quét qua 50% OB khung H1
	  - MSS: Giá tạo CISD từ 16:05 - 16:50 với các nến Bullish liên tiếp (không có nến Bearish) nuốt trọn nhịp giảm trước đó
	  - Displacement: có displacement lúc 16:30 (tạo FVG số 2 trùng CE OB), 16:40 (FVG 1 cao hơn OB)
- **Entry reason**:
	  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là OB H1, FVG trùng OB)
- **Invalidation reason**:
	  - Giá đóng qua OB H1
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260712162407.png]]

---

## 2. ICT 2022 Model — Entry Sequence

Đánh dấu theo đúng thứ tự checklist của mô hình:

- [x] **1. Liquidity Sweep** — giá quét thanh khoản (Equal H/L, swing, Asia range...)
  - Loại: Internal / External / Equal Highs / Equal Lows
- [x] **2. Displacement** — nến đẩy mạnh, tạo FVG, phá cấu trúc nội bộ
- [x] **3. Market Structure Shift (MSS)** — phá swing point ngược hướng sweep
- [x] **4. FVG / OB hợp lệ** hình thành trong displacement leg
- [x] **5. Entry** — limit trong FVG/OB (CE - Consequent Encroachment) trong Kill Zone
- [x] **6. Stop Loss** — phía trên/dưới điểm sweep (invalidation)
- [x] **7. Take Profit** — opposing liquidity / PD array kế tiếp

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ
- [x] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [x] Entry trong POI hợp lệ, không đua giá
- [x] SL ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Hit TP
- **Tại sao lệnh thắng/thua?**
	  - Kiên nhẫn chờ H1 đồng Bias với khung D1 (Bullish)
	  - Chờ M5, H1 confirm Bias
	  - Chờ H1 quay về vùng Discount
	  - Có quét thanh khoản + CISD
- **Thị trường có cho tín hiệu cảnh báo trước không?**
	  - Có Displacement
	  - Có CISD
	  - Có FVG
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%  (Giá không quay về vùng CE cho RR cao hơn)
- **Nếu được vào lại, tôi sẽ làm gì khác?**
	  - Cần thêm backtest để xem lúc nào nên vào tại cạnh và khi nào vào tại CE

---

## 5. Lesson Learned


### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**

Đây là lệnh **thắng và execution rất sạch**, nên "root cause" ở đây không phải một lỗi gây thua — mà là **điểm quyết định (và đồng thời là mắt xích yếu nhất) của cả setup**: quyết định *entry-level* (vào phía trên CE thay vì tại CE) được đưa ra bằng **cảm nhận chưa có dữ liệu backtest** ("giá hay quay đầu trước CE"). Lệnh thắng, nhưng **thắng không chứng minh giả thuyết đúng** — nó chỉ chưa phủ nhận. Toàn bộ chất lượng lệnh này phụ thuộc vào 1 biến chưa được validate.

**Triệu chứng (symptoms) — sinh ra từ root cause:**

- **Mâu thuẫn nội bộ trong journal**: mục HTF Bias tự ghi *"Bias vẫn chưa được xác nhận chính xác, tạm thời xác định Bullish"*, nhưng ở **Setup Quality Checklist** lại tick *"Bias D1/H4 rõ ràng, không mâu thuẫn H1"*. Ô tick nói một đằng, phân tích nói một nẻo → dấu hiệu **confirmation bias sau khi biết kết quả**.
- **Narrative chưa có bằng chứng đóng vai "sự thật"**: giả định "nhiều trader đặt limit ở CE nên lệnh họ không fill" được ghi nhận là lý do giá không về CE. Đây là **story chưa kiểm chứng** (chính bạn cũng note "tôi tự nghĩ, chưa có bằng chứng").
- **Chấm điểm theo RR thay vì theo tính hợp lệ của trigger**: tự trừ xuống 90% match *chỉ vì giá không về CE cho RR đẹp hơn* — trong khi trigger (sweep + CISD + FVG + entry trong Discount) đã hợp lệ 100%. Việc thiếu "RR đẹp hơn" không làm setup kém chuẩn.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**

Chuỗi đúng chuẩn 2022 Model: giá retrace về **H1 OB (1.26642–1.26515) trong vùng Discount** → một nến **bearish displacement đóng xuyên qua cạnh dưới OB kèm râu** (đây chính là **liquidity sweep** — quét stop dưới OB / old lows) → chuỗi nến bullish **CISD nuốt trọn** nến bearish đó (**MSS**) → leg CISD để lại **2 FVG** (một trên OB, một trùng CE của OB).

Điểm cốt lõi cần hiểu: **sau một CISD mạnh, delivery đã chuyển sang tìm premium**, nên giá thường tiếp tục ngay từ **FVG đầu tiên / cạnh gần POI** chứ không nhất thiết retrace sâu về **CE (50%)**. Việc giá quay đầu trước CE là **hệ quả cơ học của một CISD mạnh**, KHÔNG nhất thiết vì "limit của trader khác ở CE". Nếu chờ CE trong một displacement mạnh, bạn thực chất đang chờ một mức inefficiency sâu hơn mà thị trường không có nghĩa vụ phải cho. Đây là lý do "chờ CE" hay bị lỡ — và nó *nhất quán về mặt cơ chế*, không phải xui.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- **"Lỡ lệnh vì chờ CE"**: bạn đã ghi nhận pattern này lặp lại ở nhiều backtest gần đây. Đây là pattern đáng để **định lượng**, không phải để đổi rule theo cảm giác. Thêm 2 field vào mọi backtest: `entry_zone` (Edge / CE) và `ce_filled` (Yes/No), rồi so **win rate + expectancy** của "vào cạnh" vs "chờ CE" trên **≥ 20–30 mẫu** trước khi kết luận.
- **Confirmation bias ở checklist**: xu hướng tick "bias rõ ràng" dù note tự nói chưa chắc. Lần sau: nếu chữ trong phần phân tích còn từ "tạm thời / chưa xác nhận" thì **không được** tick ô "rõ ràng".
- **Gán narrative cho hành vi giá**: xu hướng giải thích chuyển động giá bằng câu chuyện về "trader khác" thay vì cơ chế delivery. Giữ mô tả ở mức cơ chế (sweep/CISD/FVG/premium-discount), không thêm story không kiểm chứng được.

### 5.3. Rule cần thêm/cập nhật vào Playbook

1. **Entry-level rule (đề xuất, CHỜ dữ liệu xác nhận):** Trong 2022 Model, khi CISD tạo ≥ 2 FVG chồng lên POI, **entry mặc định = 50% (CE) của FVG gần POI nhất**. Chỉ khi backtest chứng minh fill-rate tại CE thấp mới cho phép entry sớm hơn tại **cạnh trên FVG** với SL giữ nguyên dưới sweep. **Điều kiện bắt buộc: phải log `entry_zone` để đo — không đổi rule bằng cảm giác.**
2. **Bias-grade rule:** Nếu D1 bias còn "tentative" (leg gần nhất ngược hướng, như lệnh này leg D1 gần nhất là *bearish displacement*), **grade tối đa = B** cho tới khi H1 + M5 confirm; và **cấm tick "bias rõ ràng"** khi phần phân tích còn ghi "chưa xác nhận". Lệnh này về bản chất là **mua Discount trong một pullback của leg giảm gần nhất trên D1** — hợp lệ nhưng discretionary, nên grade A hiện đang hơi rộng tay.
3. **Kill-zone verify rule:** Ghi rõ **timezone của mọi mốc giờ** (broker/GMT/ET) cạnh giờ vào lệnh (16:00 = giờ gì?). Chỉ tick "trong Kill Zone" sau khi quy đổi về ET và xác nhận rơi vào London hoặc NY AM — không tick chay.
4. **Housekeeping:** Điền `risk_percent` trong frontmatter (chart hiển thị stop = 0.096% biến động giá, nhưng % rủi ro tài khoản phụ thuộc position size — cần con số thật để đối chiếu rule ≤ 0.5%/lệnh).

