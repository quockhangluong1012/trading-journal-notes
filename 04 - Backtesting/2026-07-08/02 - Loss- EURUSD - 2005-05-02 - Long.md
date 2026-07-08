---
type: backtest
backtest_date: 2026-07-08
trade_date: 2005-05-02
symbol:
  - EURUSD
position: Long
result:
  - Loss
session: London
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct:
  - Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: No
mss: No
fvg_valid: No
entry_price: 1.28639
stop_loss: 1.28392
take_profit: 1.29304
r_planned: 2.76
r_multiple: -1
grade: D
followed_plan: No
tags:
  - backtest
  - ICT2022
---

# Backtest 2005-05-02 — EURUSD Long

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2005-05-02     |
| Position             | Long           |
| Result               | Loss           |
| Session              | London         |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bullish        |
| Bias Correct?        | Yes            |
| Entry                | 1.28639        |
| Stop Loss            | 1.28392        |
| Take Profit          | 1.29304        |
| R Planned            | 2.76           |
| R Multiple (kết quả) | -1             |
| Grade                | D              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 giá hình thành Market Structure Shift với các nến lớn (displacement) phá 1 swing low lớn
  - Cấu trúc chuyển sang HH/HL
  - Nhịp displacement có tạo FVG khung D1
  - => Bias chuyển sang Bullish
  - Giá đang trong nhịp Pullback -> Chờ tín hiệu Reversal khung H1
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Previous Day/Week High
  - Sell-side liquidity: Previous Day/Week Low 
![[Pasted image 20260708075445.png]]
### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- LH/LL
	- Giá đang trong Bearish Bias
	- Chờ tín hiệu Reversal tại các POI, D1 Bias đang là Bullish
- **Dealing Range**: 
	- High: 1.31266
	- Low 1.27670: Giá đã phá Dealing Range Low con nằm bên trong dealing range lớn -> Dời Low xuống Dealing Range chính
	- Giá đang di chuyển trong vùng Discount (đúng theo bias Bullish), tuy nhiên cấu trức vẫn là LH/LL
- **POI chính**: 
	- Order Block : 1.28503 - 1.28249
- **Liquidity cần chờ sweep**:
  - Vùng Order Block
  - Vùng Breaker Block
  - Đặc biệt quan sát giá phản ứng tại vùng Unicorn
### Phân Tích:
- Ngày 15/04/2005 Giá có 1 nhịp đẩy mạnh cới các nến displacement và đồng thời tạo MSS khung H1
- Chân cú displacement đó hình thành 1 Bullish Order Block
- Giá di chuyển mạnh lên tạo cấu trúc tăng (HH/HL) sau đó và tạo đỉnh dealing range ngày 21/04/2005
- Sau đó giá tạo MSS đảo chiều và retrace về Order Block (của ngày 15/04) vào ngày 02 tháng 5/2005
- Giá quét gần tới CE của Order Block và bật lên với 1 nến lớn và các nến nhỏ (nghi ngờ - không có displacement)
- Giá sau nhịp tăng fake đó đã quét xuống sâu hơn chạm CE với 1 nến lớn và ngày sau đó bật lên với 1 nến lớn khác
- Tuy nhiên nhịp tăng đó không tạo displacement và MSS
- Giá tiếp tục quét xuyên qua CE với nên lớn và đóng nến 1 phần bên dưới CE, sau đó giá tạo 4 nên nhỏ consilodate bên dưới CE 1 khoảng nhỏ, các râu nến quét lên CE
- Sau nhịp consolidation đó giá có 1 cú displacement mạnh phá lên các định (swing high) tạo ra trong các nhịp phản ứng giả trước đó
- Giá tạo MSS với các nên displacement mạnh
- Nhịp tăng đó tạo ra FVG (đây là entry tốt hội đủ các yếu tố)
- Giá retrace về FVG
- Xuống khung nhỏ quan sát
![[Pasted image 20260708075420.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
- Giá chạm Order Block khung H1 và xuất hiện dấu hiệu reject
- Stoploss đặt bên dưới điểm sweep 
- **Entry trigger**:
  - Liquidity Sweep: Quét các old lows tạo ra trước đó + quét qua 50% Order Block khung H1
  - MSS: Giá tạo MSS ( tại thời điểm FOMO entry KHÔNG có MSS - Nhịp fake rejection lần 1)
  - Displacement: có displacement (tại thời điểm FOMO entry KHÔNG có displacement - Nhịp fake rejection lần 1)
  - FVG: Giá tạo FVG
- **Entry reason**:
  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là Order Block H1)
- **Invalidation reason**:
  - Giá đóng qua đáy sweep/Order Block
- **Tôi có chờ đủ điều kiện không?** Không

![[Pasted image 20260708081410.png]]
---

## 2. ICT 2022 Model — Entry Sequence

Đánh dấu theo đúng thứ tự checklist của mô hình:

- [x] **1. Liquidity Sweep** — giá quét thanh khoản (Equal H/L, swing, Asia range...)
  - Loại: Internal / External / Equal Highs / Equal Lows
- [ ] **2. Displacement** — nến đẩy mạnh, tạo FVG, phá cấu trúc nội bộ
- [ ] **3. Market Structure Shift (MSS)** — phá swing point ngược hướng sweep
- [x] **4. FVG / OB hợp lệ** hình thành trong displacement leg
- [x] **5. Entry** — limit trong FVG/OB (CE - Consequent Encroachment) trong Kill Zone
- [ ] **6. Stop Loss** — phía trên/dưới điểm sweep (invalidation)
- [x] **7. Take Profit** — opposing liquidity / PD array kế tiếp

---

## 3. Setup Quality Checklist

- [x] Bias D1/H4 rõ ràng, không mâu thuẫn H1
- [x] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [x] Có Liquidity Sweep trước entry
- [ ] Có Displacement rõ ràng (không phải nến yếu)
- [ ] Có MSS hợp lệ
- [x] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [x] Entry trong POI hợp lệ, không đua giá
- [ ] SL ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: Stoploss
- **Tại sao lệnh thắng/thua?**
  - FOMO vào lệnh khi giá xuất hiện reject + FVG nhỏ tại Order Block H1 ( nhịp reject đầu tiên)
  - Sau nhịp quét đầu tiên bị stop, giá quét thêm 2 lần nữa xuống Order Block. 1 lần chạm đúng C#, 1 lần quét xuống dưới CE 1 khoảng nhỏ và consolidation sau đó
  - Sau nhịp quét xuống CE giá phá mạnh lên tạo displacement + MSS phá cá swing high tạo trong nhịp fake rejection trước đó
- **Thị trường có cho tín hiệu cảnh báo trước không?**
  - Không có Displacement
  - Không có MSS
  - FVG tạo từ những nến thân nhỏ
  - Sau nhịp giá đẩy đó toàn là nến nhỏ + doji. Không có nến thân lớn
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 40% ( Vào vội không chờ tín hiệu xác nhận)
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Chờ MSS hình thành
  - Có Displacement
  - FVG chất lượng (tạo từ nến displacement với thân lớn)

---

## 5. Lesson Learned

> [!summary] Kết luận 1 câu
> Bias, POI và RR đều ĐÚNG — lệnh thua **không phải vì đọc sai thị trường**, mà vì **bấm cò sai thời điểm**: vào trên nhịp reject ĐẦU TIÊN tại Order Block khi mô hình 2022 chưa hoàn tất (thiếu Displacement + MSS). Đây là lỗi *timing*, không phải lỗi *analysis*.

### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**

- [[04 - Mistake - FOMO Entry]] — Vào lệnh trên phản ứng đầu tiên tại POI vì sợ lỡ sóng. Đây là gốc rễ; ba lỗi bên dưới đều là **hệ quả tất yếu** của việc vào sớm, không phải lỗi độc lập.

**Triệu chứng (symptoms) — sinh ra từ root cause:**

- [[06 - Mistake - Not Have Market Structure Shift]] — Tại thời điểm entry, giá **chưa phá swing point ngược hướng sweep**. Không có MSS = chưa có bằng chứng smart money đảo hướng. Đây là "giấy xác nhận" bắt buộc của 2022 Model mà lệnh này bỏ qua.
- [[08 - Mistake - Weak Displacement]] — Nhịp bật khỏi OB chỉ gồm **nến thân nhỏ + doji**, không phải nến displacement thân lớn. Displacement yếu = không có lực tổ chức thật đứng sau.
- [[10 - Mistake - FVG Not Valid]] — FVG dùng để entry sinh ra từ nến thân nhỏ → **không hợp lệ**. FVG chỉ có giá trị khi nó là dấu vết của một displacement leg thực sự.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**

Cú reject đầu tiên tại OB là một **bẫy thanh khoản (liquidity trap)**. Giá bật fake lên → hút lệnh buy vào sớm (như lệnh này) → quay đầu **quét đúng stop**. Sau đó giá còn quét thêm **2 lần** xuống sâu hơn (1 lần chạm CE, 1 lần xuyên dưới CE rồi consolidation 4 nến, râu liếm CE) để **gom nốt thanh khoản** trước khi đảo chiều thật. Chỉ SAU khi gom xong, giá mới bung **displacement thật + MSS thật + FVG chất lượng** → đó mới là entry đúng. Bài học: *ta đã cung cấp thanh khoản cho smart money thay vì đi theo họ.* Khoảng cách giữa lệnh thua và lệnh thắng chỉ là **sự kiên nhẫn chờ MSS xác nhận** (< 25 pips về giá, nhưng khác nhau cả một thế giới về xác suất).

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- **Pattern chính:** [[04 - Mistake - FOMO Entry]] → vào trên nhịp reject đầu tiên tại POI, trước khi có xác nhận displacement + MSS.
- **Dấu hiệu nhận biết sớm (early warning) để lần sau tự bắt được mình:**
  - Đang định vào khi giá **vừa mới chạm** POI và mới có 1 nến reject → DỪNG LẠI.
  - Nhịp bật gồm nến thân nhỏ / doji, chưa phá swing point nào → **chưa phải tín hiệu**.
  - Cảm giác "sợ giá đi mất không có mình" xuất hiện → đó chính là FOMO đang lên tiếng, không phải setup.
- **Kiểm chứng qua data:** Cần tra Mistake Dashboard xem [[04 - Mistake - FOMO Entry]] đã xuất hiện bao nhiêu lần trong bộ backtest gần nhất. Nếu đây là lỗi tái diễn nhiều lần → đây là **rò rỉ edge lớn nhất hiện tại**, cần ưu tiên xử lý trước mọi thứ khác.

### 5.3. Rule cần thêm/cập nhật vào Playbook

> [!warning] Rule bắt buộc — "No MSS, No Entry"
> Trong ICT 2022 Model, **TUYỆT ĐỐI không entry nếu chưa có Displacement + MSS xác nhận trên khung entry (M5)**. Nến reject đầu tiên tại POI **không phải** tín hiệu — nó chỉ có nghĩa "giá chạm vùng". Tín hiệu thật = giá **RỜI** vùng bằng displacement thân lớn → phá swing point ngược hướng sweep (MSS) → mới retrace vào FVG/OB để entry.

> [!tip] Quy trình "cò 2 tầng" (two-step trigger) — thuốc giải cho FOMO
> 1. **Trước khi giá tới POI:** đánh dấu sẵn **swing point cần phá** để tạo MSS. Xác định điểm này *trước* biến quyết định vào lệnh từ cảm tính thành cơ học.
> 2. **Chỉ đặt lệnh** sau khi một nến **ĐÓNG CỬA** phá swing point đó bằng displacement (không dùng râu nến).
> 3. Nếu FVG hình thành từ nến thân nhỏ / doji → **HỦY setup**, không giao dịch. Thà bỏ lỡ còn hơn vào lệnh không hợp lệ.

> [!note] Định lượng "Displacement hợp lệ" (bỏ tranh cãi cảm tính)
> - Thân nến displacement ≥ **1.5–2× ATR** trung bình của khung entry.
> - FVG do nó tạo ra phải rộng tối thiểu một ngưỡng pip cố định (cần backtest thêm để chốt con số cho EURUSD M5).
> - Có tiêu chí định lượng → câu hỏi "nến này đủ mạnh chưa?" tự trả lời, không phụ thuộc cảm xúc.

> [!danger] Kỷ luật journaling
> Lệnh này là **THUA + SAI QUY TRÌNH** (`followed_plan: No`, `r_multiple: -1`). Phải ghi nhận trung thực để pattern FOMO đủ "đau" mà khắc vào phản xạ. Nhắc lại nguyên tắc vàng: *một lệnh thua đúng quy trình còn quý hơn một lệnh thắng sai quy trình* — nhưng lệnh này không nằm ở nhóm đó.

---
