---
type: backtest
backtest_date: 2026-07-10
trade_date: 2021-05-07
symbol: EURUSD
position: Short
result: Loss
session: Asia
setup: ICT 2022 Model
entry_model: ICT 2022 Model
entry_timeframe: M5
htf_bias: Bearish
bias_correct: Yes
poi_type: "[[01 - ICT 2022 Model|2022 Model]]"
liquidity_swept: Yes
displacement: Yes
mss: Yes
fvg_valid: Yes
entry_price: 1.20805
stop_loss: 1.20931
take_profit: 1.20381
r_planned: 3.39
r_multiple: -1
grade: C
followed_plan: No
tags:
  - backtest
  - ICT2022
---

# Backtest 2021-05-03 — EURUSD Short

> [!info] Mục đích backtest
> Replay dữ liệu quá khứ để luyện nhận diện **ICT 2022 Model entry** trên EURUSD. Mỗi file = 1 setup. Mục tiêu: lặp lại đủ nhiều để bias → POI → sweep → MSS → FVG entry trở thành phản xạ, và tích luỹ lesson learned.

---

## 0. Backtest Summary

| Field                | Value          |
| -------------------- | -------------- |
| Symbol               | EURUSD         |
| Trade Date (dữ liệu) | 2021-05-03     |
| Position             | Short          |
| Result               | Loss            |
| Session              | Asia       |
| Setup                | ICT 2022 Model |
| Entry Model          | ICT 2022 Model |
| Entry Timeframe      | M5             |
| HTF Bias             | Bearish        |
| Bias Correct?        | Yes            |
| Entry                | 1.20805         |
| Stop Loss            | 1.20931        |
| Take Profit          | 1.20381        |
| R Planned            | 3.39          |
| R Multiple (kết quả) | -1          |
| Grade                | D              |

> ⚠️ Nhớ điền các field tương ứng trong **frontmatter** (phía trên) để Dataview dashboard tự tổng hợp.

---

## 1. HTF Context & Bias

### D1 / H4 — Daily Bias

- **Bias**: Bearish
- **Market Condition**: Trending
- **Lý do xác định bias** (PD array, draw on liquidity):
  - Khung D1 đang trong trend giảm
  - Hình thành các LH/LL
  - Sau đó có 1 nhịp Pullback lớn, tuy nhiên chưa phá được protected high -> chưa đổi bias, chỉ là pullback 
- **Draw on Liquidity (mục tiêu giá hướng tới)**:
  - Buy-side liquidity: 
	  - Dealing Range High = 1.23473
  - Sell-side liquidity: Giá đang hướng tới vùng
	  - Swing low: 1.17149 (Swing low quan trọng)
	  - Bullish Order Block: 1.16576 - 1.16197
	  - EQL dưới OB: 1.16045

![[Pasted image 20260710114911.png]]

### H1 — Cấu trúc & POI
- **Cấu trúc H1**: 
	- LH/LL
- **Dealing Range**: 
	- High: 1.21058
	- Low 1.19436
- **POI chính**: 
	- Order Block: 1.20884 - 1.20780
	- Order Block: 1.20678 - 1.20611
- **Liquidity cần chờ sweep**:
	- Các vùng Order Block và swing high trên gần Order Block
	  
### Phân Tích:
	-  Giá tạo Order block (30/04/2026) và Order Block ngày (03/05/2026) bằng các nhịp đẩy giá mạnh (bearish displacement)
	- Sau khi tạo đáy ngày 05/05/2026, giá retrace về vùng Order Block 1 (thấp hơn)
	- Giá quét qua cạnh trên của OB 1 và đóng nến lại bên torng (Liquidity Sweep)
	- Tuy nhiên sau đó giá đóng nến và giữ bên trên OB 1 này -> Tạo thành Breaker Block
	- Cây nến phá OB 1 là 1 nến Bullish displacement mạnh có tạo FVG khi phá lên
	- Giá tiếp tục di chuyển về vùng OB 2 (OB cao hơn)
	- Giá cũng quét lên và ra ngoài cạnh trên OB nhưng sau đó đóng trở lại vào bên trong (Liquidity Sweep)
	- Sau đó xuất hiện các nến rejection
	- Xuống khung M5 quan sát giá

![[Pasted image 20260710114842.png]]

## M5 - Xác nhận và điểm vào lệnh

### Phân tích:
	- Sau khi quét cạnh trên OB khung H1, giá bật ngược lại bên trong
	- Nhịp bật ra có các nến displacement (Không quá lớn) + có FVG
	- Nhịp displacement đồng thời tạo MSS
	- Entry khi giá retrace về FVG M5
	- Sau đó giá di chuyển xuống đúng kế hoạch về vùng OB 1
	- Tuy nhiên khi vào lệnh tôi mới phát hiện mình vào sai KillZone (thời điểm vào lệnh là Asia - 10:05 UTC+7)
	- Giá về quét OB 1 và sau đó 1 nến bullish displacement rất hơn hình thành và quét xuyên qua OB 2 và stop loss của tôi
	- 1 nến diplacement quét thẳng tới 1 OB trên cao nhất (1.21296 - 1.21227)
	- Stop loss vì sai Killzone
- **Entry trigger**:
	  - Liquidity Sweep: 
		  - Quét qua cạnh trên + Swing high sát cạnh trên OB
	  - MSS: Giá tạo MSS
	  - Displacement: có displacement (Nến không quá lớn)
	  - FVG: Giá tạo FVG
- **Entry reason**:
	  - Giá hình thành Setup theo mô hình ICT 2022: Sweep -> MSS + Displacement + FVG -> retrace FVG -> Entry (POI là OB H1)
	  - Tuy nhiên sai KillZone
- **Invalidation reason**:
  - Giá đóng qua cạnh trên OB
- **Tôi có chờ đủ điều kiện không?** Không

![[Pasted image 20260710115115.png]]

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
- [ ] Giá nằm trong Kill Zone (London / NY AM 8:30–11:00 ET)
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng (không phải nến yếu)
- [x] Có MSS hợp lệ
- [x] FVG / OB nằm trong Discount (buy) hoặc Premium (sell)
- [x] Entry trong POI hợp lệ, không đua giá
- [x] SL ở vùng invalidation hợp lý
- [x] RR tối thiểu đạt ≥ 1:2

---

## 4. Phân tích sau lệnh (Replay)

- **Result**: 
	- Stop loss
- **Tại sao lệnh thắng/thua?**
	  - Setup đủ các điều kiện tuy nhiên khi vào lệnh mới phát hiện sai KillZone. Setup đang nằm trong phiên Asia
- **Thị trường có cho tín hiệu cảnh báo trước không?**
	  - Có Displacement
	  - Có MSS
	  - FVG hợp lệnh, tạo từ nến thân lớn sau 1 nhịp quét Unicorn
- **Setup này khớp bao nhiêu % với mô hình chuẩn?** 
	- 40%
	- Giá không nằm trong vùng OTE
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - Cải thiện tâm lý giao dịch

---

## 5. Lesson Learned

> [!summary] Root cause (1 câu)
> **Vào lệnh ngoài Kill Zone (Asia, 10:05 UTC+7).** ICT 2022 Model là mô hình *phụ thuộc Kill Zone*; bỏ qua điều kiện tiên quyết này biến một setup "đẹp" thành một lệnh không có edge.

### 5.1. Bài học kỹ thuật

Setup được đọc rất tốt về mặt cấu trúc (bias → dealing range → sweep → breaker → displacement + FVG → MSS → retrace entry), nhưng **giá trị của ICT 2022 Model là *có điều kiện*** — nó chỉ có edge khi diễn ra trong London KZ / NY AM KZ, nơi dòng lệnh tổ chức tạo ra displacement *thật*. Trong phiên **Asia thanh khoản mỏng**, cái "sweep" và "displacement" mà tôi thấy phần lớn là chuyển động nội bộ (internal), dễ tạo cảm giác có setup nhưng không có lực đẩy institution phía sau. Đây là lý do lệnh thua — **không phải do tâm lý, mà do lỗi quy trình (thiếu cổng kiểm tra Kill Zone trước lệnh).**

**Triệu chứng (symptoms) — sinh ra từ root cause:**
- Chỉ **phát hiện sai Kill Zone SAU khi đã đặt lệnh** → checklist Kill Zone bị bỏ trống nhưng vẫn bấm lệnh (cổng kiểm tra không được đặt *trước* khi phân tích M5).
- **Displacement yếu** — chính tôi ghi chú "nến không quá lớn" tới 2 lần nhưng vẫn vào. Displacement yếu là dấu hiệu suy giảm của mô hình, đã bị hợp lý hóa.
- **Entry không nằm trong OTE / không kiểm tra Premium** cho leg bán (tự chấm 40% khớp mô hình, "giá không nằm trong vùng OTE"). Short mà không bán từ premium/OTE làm giảm edge và tăng xác suất bị chạy qua.
- **SL đặt ngay trên OB gần** (trên điểm sweep OB2) → trong phiên mỏng, cụm stop này trở thành *nam châm* cho một nhịp quét.

**Cơ chế thị trường đã diễn ra (hiểu để không lặp lại):**
- Cú "sweep" cạnh trên OB2 mà tôi coi là tín hiệu vào thực chất chỉ là **internal liquidity nông**. **Buy-side thật sự vẫn chưa bị lấy** — nó nằm ở OB cao hơn (1.21296–1.21227) phía trên.
- Draw on liquidity *ngắn hạn* đang hướng **LÊN** (đi lấy buy-side + cụm SL của phe short) chứ không phải xuống ngay. Sau khi nhử phe short vào, chỉ cần **một nến bullish displacement đơn lẻ** trong phiên mỏng là đủ để chạy xuyên OB2 + SL của tôi để với tới buy-side phía trên.
- Bài học cốt lõi: **một pattern "đủ điều kiện" trong sai bối cảnh (session/premium) KHÔNG phải là một setup hợp lệ.** Checklist thiếu đúng cái gate quan trọng nhất (Kill Zone) đáng lẽ phải là NO-TRADE, chứ không phải "gần đủ nên vào".

### 5.2. Pattern lặp lại (điều cần để ý lần sau)

- **"Đủ checklist pattern nhưng thiếu cổng quan trọng nhất" → vẫn vào.** Kill Zone bỏ trống mà vẫn bấm lệnh. Đây là lỗi kỷ luật quy trình, không phải lỗi đọc chart.
- **Hợp lý hóa tín hiệu yếu** (displacement "không quá lớn" nhưng vẫn coi là hợp lệ).
- **Quy loss cho "tâm lý"** ("Nếu vào lại: cải thiện tâm lý") — chẩn đoán sai gốc rễ. Gốc rễ là **rule/process** (Kill Zone gate + OTE), không phải cảm xúc. Đổ lỗi cho tâm lý sẽ che mất lỗi thật và khiến nó lặp lại.

### 5.3. Rule cần thêm/cập nhật vào Playbook

1. **HARD GATE — Kill Zone:** Không entry nếu không nằm trong **London KZ** hoặc **NY AM KZ**. Kiểm tra Kill Zone *TRƯỚC* khi xuống M5 phân tích entry, không phải sau khi đặt lệnh. Ngoài KZ = NO-TRADE tuyệt đối.
2. **HARD GATE — OTE/Premium:** Với lệnh Short, POI phải nằm trong **premium** và lý tưởng chạm **OTE 62–79%** của leg/dealing range liên quan. Không đạt = bỏ.
3. **Định nghĩa displacement khách quan:** range ≥ ngưỡng ATR đã định, phá cấu trúc nội bộ dứt khoát, để lại FVG rõ. **Displacement yếu = no trade.**
4. **Sample hygiene:** Lệnh vào ngoài Kill Zone **KHÔNG được tính** vào thống kê edge của 2022 Model (win rate / expectancy). Tag `invalid - out of KZ` và loại khỏi cohort chính, hoặc để riêng cohort "Asia session" nếu muốn nghiên cứu độc lập.
5. **SL logic:** Xác định buy-side/OB lớn phía trên như *mục tiêu quét tiềm năng* trước khi vào; tránh đặt SL ngay sát một OB gần dễ bị nhử trong phiên mỏng.
6. **Data integrity:** Đồng bộ `trade_date` (title/frontmatter ghi 2021-05-07, nhưng heading & bảng Summary ghi 2021-05-03), `grade` (frontmatter C vs bảng D), và các mốc ngày trong phần Phân Tích (đang ghi nhầm 2026 thay vì 2021).

> [!warning] Liên kết Mistake Database
> Tạo/liên kết tới `[[Mistake - Vào lệnh sai Kill Zone]]` và `[[Mistake - Hợp lý hóa displacement yếu]]` để dashboard mistake tổng hợp được tần suất lỗi này.

### 5.4. Sai lầm SÂU hơn cả Kill Zone: nhầm giữa HTF bias và short-term draw on liquidity

> [!danger] Đây là bài học quan trọng nhất, quan trọng hơn cả lỗi Kill Zone
> Ngay cả khi lệnh này rơi vào **London/NY KZ**, nó vẫn là một lệnh **premature short** — vì short-term draw on liquidity lúc đó đang hướng **LÊN**, không phải xuống.

HTF bias **Bearish là đúng** (đã được xác nhận: kết cấu D1 giảm, LH/LL, pullback chưa phá protected high). Nhưng **"bias đúng" và "thời điểm entry đúng" là hai chuyện hoàn toàn khác nhau** — và đây chính là cái bẫy nhận thức đã khiến lệnh này thua kể cả về mặt logic ICT, không chỉ vì session.

Cơ chế thực tế: phía trên entry còn một cụm **buy-side liquidity chưa bị lấy** — cạnh trên OB cao nhất `1.21296–1.21227` và cụm stop của phe short (trong đó có SL của chính tôi tại `1.20931`). Trong ICT, giá **đi tìm liquidity chưa bị chạm** trước khi đảo chiều theo bias lớn. Khi buy-side phía trên còn nguyên, kịch bản xác suất cao nhất trong ngắn hạn là:

> giá **nhử phe short vào** (tạo cảm giác có sweep + MSS trên M5) → **chạy ngược lên lấy buy-side + quét cụm SL** → *sau đó* mới quay đầu theo bias giảm.

Cú "sweep cạnh trên OB2" mà tôi coi là tín hiệu entry chỉ là **internal liquidity nông** — không phải là *raid* buy-side thật. Đây là lỗi kinh điển: **đọc đúng hướng dài hạn nhưng đứng sai phía của liquidity gần nhất.** Short đúng bias nhưng vào *trước khi* buy-side trên bị dọn = tự đặt lệnh vào đúng đường đạn của lần quét kế tiếp.

**Quy tắc rút ra:** Trước mỗi entry, hỏi một câu bắt buộc — *"Liquidity chưa-bị-lấy gần nhất nằm ở phía nào so với entry của tôi?"* Nếu nó nằm **cùng phía với SL** (tức giá còn lý do để chạy vào SL trước), thì đó là **NO-TRADE hoặc phải chờ nó bị quét xong**, bất kể pattern đẹp đến đâu.

### 5.5. Những điều "tưởng đúng nhưng lại sai" (cognitive traps)

Phần này bóc tách các tín hiệu tôi *tin là xác nhận* nhưng thực chất là nhiễu — vì đây là loại lỗi nguy hiểm nhất (nó cảm giác giống như đang làm đúng):

- **"Bias correct = Yes → nên short"**: Bias đúng chỉ trả lời *hướng cuối cùng*, không trả lời *điểm & thời điểm vào*. Đây là ngộ nhận gốc, đã phân tích ở 5.4.
- **"Có Liquidity Sweep → có tín hiệu"**: Nhầm **internal liquidity nông** thành **external/buy-side thật**. Không phải cứ quét-rồi-đóng-lại là một raid hợp lệ. Phải phân loại: sweep này lấy *loại* thanh khoản nào, và *thanh khoản mục tiêu lớn hơn* đã bị lấy chưa.
- **"Có MSS trên M5 → xác nhận đảo chiều"**: Một MSS trên M5 trong **phiên Asia mỏng** có **trọng số rất thấp** — dễ bị tạo ra bởi vài lệnh nhỏ và bị phủ định ngay sau đó. MSS chỉ có giá trị khi đi kèm displacement thật của dòng lệnh tổ chức (tức trong KZ).
- **"R planned 3.39 → lệnh đáng vào"**: RR đẹp là *ảo giác an toàn*. RR chỉ có ý nghĩa khi **xác suất chạm TP trước SL** đủ cao; ở đây SL nằm ngay dưới một buy-side chưa bị lấy → xác suất chạm SL trước bị đội lên rất mạnh, làm RR 3.39 trên giấy trở nên vô nghĩa. **RR không bao giờ được dùng để bù cho một entry sai bối cảnh.**
- **Checklist Section 2 đánh dấu `[x]` mục 5 ("Entry ... trong Kill Zone")** trong khi thực tế KHÔNG ở Kill Zone → checklist bị tick "cho đủ" chứ không phản ánh sự thật. Section 3 (Setup Quality) đã trung thực để trống ô Kill Zone — **hai mục đang mâu thuẫn nhau trong cùng file.** Bài học meta: *checklist chỉ có giá trị nếu được tick trung thực; một ô tick sai còn nguy hiểm hơn không có checklist* vì nó tạo cảm giác đã kiểm tra.

### 5.6. Cổng vào lệnh (pre-trade gate) — áp dụng ngay từ lệnh backtest tiếp theo

Chuyển bài học thành một quy trình **IF-THEN** không thể lách:

1. **Session gate**: Đang trong London KZ hay NY AM KZ? → Nếu KHÔNG: **NO-TRADE**, dừng, không xuống M5. *(Đặt gate này TRƯỚC khi phân tích entry, không phải sau.)*
2. **Draw gate**: Liquidity chưa-bị-lấy gần nhất nằm phía nào? → Nếu cùng phía SL: **chờ nó bị quét xong** rồi mới tìm entry ngược lại.
3. **Location gate**: POI có nằm trong **Premium (cho Short)** và lý tưởng chạm **OTE 62–79%** không? → Nếu KHÔNG: bỏ.
4. **Signal-quality gate**: Displacement có đạt ngưỡng ATR khách quan + để lại FVG rõ không? → "Nến không quá lớn" = **displacement yếu = NO-TRADE.**
5. Chỉ khi **cả 4 gate = PASS** mới được đặt lệnh.

> [!note] Sample hygiene — bắt buộc để backtest có giá trị thống kê
> Lệnh này vào **ngoài Kill Zone** ⇒ **KHÔNG được tính** vào cohort chính đo edge của ICT 2022 Model (win rate / expectancy). Gắn tag `invalid-out-of-KZ` và loại khỏi mẫu chính — nếu không, một lệnh phá luật sẽ làm bẩn số liệu và khiến tôi đánh giá sai edge thực của mô hình. Đây không phải "một lệnh thua", mà là **"một lệnh không nên tồn tại trong dữ liệu edge".**

> [!tip] Chẩn đoán lại root cause — sửa dòng "cải thiện tâm lý"
> Ô "Nếu được vào lại, tôi sẽ làm gì khác? → Cải thiện tâm lý" là **chẩn đoán sai gốc rễ.** Không có lỗi tâm lý nào ở đây cả — có một lỗi **quy trình** (thiếu 4 gate ở trên) và một lỗi **nhận thức** (nhầm bias với draw). Đổ cho tâm lý là cách nhanh nhất để *không sửa được gì*, vì nó biến một lỗi có-thể-lập-trình-thành-luật thành một khuyết điểm mơ hồ về tính cách. **Sửa lại thành: "Thêm 4-gate pre-trade checklist và bắt buộc PASS cả 4 trước khi đặt lệnh."**

---
