---
type: backtest
backtest_date: 2026-07-11
trade_date: 2013-11-21
symbol: EURUSD
position: Long
result: Win
session: New York
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bullish
bias_correct: Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.34239
stop_loss: 1.34085
take_profit: 1.34728
r_planned: 3.41
r_multiple: 3.41
grade: A
followed_plan: Yes
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
| Trade Date (dữ liệu) | 2013-11-21     |
| Position             | Long           |
| Result               | Win            |
| Session              | New York       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bullish        |
| Bias Correct?        | Yes            |
| Entry                | 1.34239        |
| Stop Loss            | 1.34085        |
| Take Profit          | 1.34728        |
| R Planned            | 3.18           |
| R Multiple (kết quả) | 3.18           |
| Grade                | A              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
	  - Giá đang trong trend tăng với các HH/HL
	  - Giá hình thành 1 BOS ngày 18/09/2013 xác định Bullish
	  - Giá có 1 nhịp Pullback từ ngày28/10/2013, tời ngày 20/11/2013 thì nhịp hồi kết thúc bằng 1 CISD phá qua chuỗi nến giảm
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: Liquidity Void (từ nhịp Pullback), đặc biệt FVG từ 1.36970 - 1.35938
  - Sell-side liquidity: Old low: 1.32927

![[Pasted image 20260711155108.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- HH/HL
- **Dealing Range**: 
	- High: 1.35787
	- Low 1.32927
	- Giá đang trong vùng Discount cho setup Long
- **POI chính**: 
	- OB vùng 1.34083 - 1.33909
- **Liquidity cần chờ sweep**:
  - Swing low phía trên OB
  - Vùng OB

### Phân Tích:
	- Ngày 20/11/2013 giá hình thành 1 nến lớn Bearish xuyên thẳng xuống quét qua các higher lows
	- Giá quét vùng inducement (swing low) phía trên OB
	- Sau đó giá quét xuống OB, giá quét xuống 30 pip, để lại râu nến và đóng nến ngay tại cạnh trên OB
	- Sau đó giá quét xuống tới CE và xuất hiện dấu hiệu rejection
	- Sau đó 1 nến bullish mạnh hình thành
	- Xuống khung M5 quan sát

![[Pasted image 20260711155048.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Sau khi giá chạm đúng CE vùng OB abt65 ra tạo thành 1 Bullish FVG
	- Nhịp giảm trước đó kèm theo Bearish FVG nên hình thành 1 vùng BPR khung M5
	- Sau đó giá tạo displacement tăng mạnh + FVG + MSS
	- Giá quét FVG lần đầu tiên tuy nhiên tại thời điểm lần đầu này chưa hình thành MSS nên tôi không vào lệnh 
	- Sau đó giá bật lên ra khỏi BPR - lúc đó tôi tưởng mình đã lỡ nhịp
	- Vài cây nến sau giá quay về chạm cạnh trên BPR 
	- Tôi entry long tại cạnh thay chì chờ giá về CE -> đánh đổi RR thấp hơn để có xác suất vào lệnh
	- Stoploss tối đặt tại cạnh dưới BPR
	- Tỉ lệ RR: 3.18
	- Take profit tại swing high khung M5 (1 bearish order block - internal liquidity)
	- Tôi trade intraday nên thoát lệnh trong ngày, sau đó giá tiếp tục đi lên mạnh
- **Entry trigger**:
	  - Liquidity Sweep: Quét các old lows tạo ra trước đó + quét qua 50% FVG khung H1
	  - MSS: Giá tạo MSS lúc 16:20 ngày 21/11/2013
	  - Displacement: có displacement lúc 15:35 ngày 21/11/2012
	  - Giá tạo vùng BPR: 1.34237 - 1.34-96
- **Entry reason**:
	  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là OB H1, entry BPR khung M5)
- **Invalidation reason**:
	  - Giá đóng qua BPR M5
- **Tôi có chờ đủ điều kiện không?** Có

![[Pasted image 20260711154943.png]]

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
	  - Chờ H1 quay về vùng Discount
- **Thị trường có cho tín hiệu cảnh báo trước không?**
	  - Có Displacement
	  - Có MSS
	  - Có FVG
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 90%  (Giá không quay về vùng CE cho RR cao hơn)
- **Nếu được vào lại, tôi sẽ làm gì khác?**
	  - Cần thêm backtest để xem lúc nào nên vào tại cạnh và khi nào vào tại CE

---

## 5. Lesson Learned


### 5.1. Bài học kỹ thuật

**Root cause (nguyên nhân gốc) — chỉ có MỘT:**
Quyết định điểm entry **không dựa trên một rule đã định nghĩa TRƯỚC lệnh**. Việc chuyển từ "chờ CE" sang "bắt cạnh trên BPR" được quyết định *in-the-moment*, một phần vì cảm giác "tưởng mình đã lỡ nhịp" (FOMO) khi giá bật ra khỏi BPR — chứ không theo một tiêu chí chọn kịch bản A/B cố định. Lệnh thắng, nhưng lý do vào lệnh là *reactive*, không phải *planned*.

**Triệu chứng (symptoms) — sinh ra từ root cause:**
- Bỏ qua lần chạm FVG đầu tiên vì chưa có MSS → phần này **đúng và kỷ luật**. Nhưng khi giá displacement ra khỏi BPR thì tâm lý "đã lỡ" xuất hiện → chuyển sang bắt cạnh khi giá quay lại.
- Checklist tick "Entry — limit trong FVG/OB (CE)" nhưng thực tế entry tại **cạnh trên BPR (1.34239)**, không phải CE → self-report không khớp hành động thực.
- TP đặt tại **internal liquidity M5** (bearish OB) trong khi Draw on Liquidity đã tự xác định ở mục HTF là **FVG D1 1.35938–1.36970** (cao hơn rất nhiều) → TP không tham chiếu DOL đã ghi. Giá đi tiếp mạnh sau khi thoát.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
Sweep inducement (swing low phía trên OB) + quét vào OB H1 → rejection tại CE của OB → displacement tăng tạo FVG + MSS trên M5. Nhịp giảm trước để lại Bearish FVG, nhịp tăng để lại Bullish FVG → chồng lên nhau thành **BPR** — một vùng imbalance đã được "cân bằng", đóng vai trò institutional reference point. Retrace về cạnh trên BPR **vẫn nằm trong vùng imbalance** nên entry vẫn hợp lệ về mặt logic; nhưng entry tại CE cho SL chặt hơn và RR cao hơn đáng kể. Đây là đánh đổi **fill-probability vs RR**, không phải "đúng/sai" tuyệt đối — vấn đề là nó cần được *chọn có chủ đích*, không phải do cảm xúc.

### 5.2. Pattern lặp lại (điều cần để ý lần sau)
- **"Bắt cạnh vì sợ lỡ"**: khi giá rời POI rồi quay lại, có xu hướng vào aggressive để không bỏ lỡ. Cần tách bạch: đây là *aggressive entry hợp lệ* hay là *FOMO đội lốt lý luận EV*? Lần này thắng → rủi ro **outcome bias** củng cố một hành vi **chưa được backtest validate**.
- **TP thiên về internal liquidity gần**, chưa kéo tới HTF draw đã xác định → hệ thống có xu hướng "chốt non" so với bias.

### 5.3. Rule cần thêm/cập nhật vào Playbook
- **Rule Entry (A/B định trước lệnh):** trước khi vào, ghi rõ 2 kịch bản — **(A) CE-entry**: limit tại CE, SL dưới sweep, ưu tiên RR; **(B) Aggressive-entry**: market tại cạnh BPR/FVG *chỉ khi* MSS đã xác nhận. Điều kiện chọn A vs B phải là tiêu chí khách quan (vd: khoảng cách tới CE, thời gian còn lại trong Kill Zone), **không quyết định theo cảm xúc "sợ lỡ"**.
- **Rule TP:** TP mặc định tham chiếu **DOL đã xác định ở mục HTF**. Nếu trade intraday và DOL ở xa → **partial tại internal liquidity + để runner** hướng DOL / hoặc đóng cuối phiên. Ghi rõ lý do nếu chốt sớm hơn DOL.
- **Rule Data Hygiene:** đối chiếu frontmatter khớp bảng Summary trước khi lưu (đặc biệt `r_planned`, `trade_date`, tiêu đề) — sai lệch làm hỏng thống kê expectancy của dashboard.

---
