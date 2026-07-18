---
type: mistake
category: analysis
severity: high
related_model: ICT 2022
frequency: 4
status: active
tags:
  - trading/ict/mistake
  - trading/review
created: 2026-07-18
updated: 2026-07-18
---

# Mistake - Trading Into Unswept Liquidity (SL nằm trong đường thanh khoản chưa bị lấy)

> [!summary] Tóm tắt 1 câu
> Vào lệnh khi **pool thanh khoản chưa-bị-lấy gần nhất nằm cùng phía với Stop Loss** — nghĩa là giá vẫn còn một "lý do thuật toán" để chạy xuyên qua SL trước khi đi theo hướng bias, và SL của chính mình trở thành một phần của pool đó.

> [!danger] Nguyên tắc cốt lõi — câu hỏi gate bắt buộc trước MỌI lệnh
> **"Pool thanh khoản chưa-bị-lấy GẦN NHẤT nằm phía nào so với SL của tôi?"**
> Nếu nó nằm **cùng phía với SL** (phía dưới SL cho Long, phía trên SL cho Short — hoặc trùng luôn vị trí SL): **NO-TRADE hoặc chờ pool đó bị quét xong**, bất kể setup đẹp đến đâu, bất kể R:R trên giấy là bao nhiêu.

---

## 1. Vì sao note này tồn tại

Note này được tạo sau khi review chéo **4 lệnh thua backtest liên tiếp (tháng 7/2026)** và phát hiện chúng KHÔNG phải 4 bài học rời rạc — chúng là **một lỗi duy nhất mặc 4 lớp áo khác nhau**. Cả 4 lệnh: chuỗi 2022 Model "trông đủ", entry cơ học chính xác (đúng CE), R:R kế hoạch đẹp (3.2–3.9), kỷ luật thực thi tốt — và đều -1R vì SL nằm trong đường giá đi lấy một pool thanh khoản chưa bị chạm.

## 2. Bốn biến thể đã xảy ra (case evidence)

| # | Lệnh | Biến thể | Pool chưa-bị-lấy | First error | Kết quả |
|---|---|---|---|---|---|
| 1 | [[02 - Loss- EURUSD - 2021-05-07- Short]] | **External BSL phía trên** — nhầm internal sweep thành raid thật, short khi buy-side (OB 1.21296–1.21227) còn nguyên | BSL external trên entry | draw | -1R |
| 2 | [[02 - Loss- XAUUSD- 2014-05-14- Short]] | **Nội bộ POI** — SL đặt tại mép gần (RB low) của chính POI đang giao dịch; phần thân còn lại của RB là vùng test hợp lệ | Phần còn lại của chính POI | poi (SL) | -1R |
| 3 | [[01 - Loss - XAUUSD - 2014-05-19 - Short]] | **POI sâu hơn chưa test** — short tại BB (0.618) khi OB (0.786) phía trên chưa được chạm; SL nằm giữa BB và OB | OB terminal + cụm SL trên BB | poi | -1R |
| 4 | [[02 - Loss - GBPUSD - 2014-07-17 - Long]] | **ERL cấu trúc bên dưới** — Long tại FVG/OTE sát "móng" dealing range khi SSL (range low) chưa bị quét, không có đệm thanh khoản nội bộ | ERL = range low dưới entry | sweep | -1R |

**Điểm chung của cả 4:**

- Pool chưa-bị-lấy gần nhất luôn nằm **cùng phía với SL** → SL bị "ăn" như một phần của nhịp gom thanh khoản, không phải vì bias sai (3/4 lệnh `bias_correct: Yes`).
- R:R kế hoạch đẹp (3.22–3.9) trong cả 4 lệnh — và trong ít nhất 2 lệnh, chính SL sai chỗ **tạo ra** con số R:R đẹp đó. R:R cao bất thường ở một POI nông là **triệu chứng cảnh báo**, không phải điểm cộng.
- 3/4 lệnh có tín hiệu M5 yếu (không FVG sạch / displacement "không quá lớn") đã bị hợp lý hóa để đi tiếp.

## 3. Cơ chế thị trường (vì sao lỗi này bị trừng phạt gần như chắc chắn)

Trong khuôn khổ ICT, giá không di chuyển ngẫu nhiên — nó được **giao hàng từ pool thanh khoản này sang pool thanh khoản khác** ([[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]]). Một pool rõ ràng chưa bị chạm (equal highs/lows, range extreme, POI sâu chưa test, cụm stop) là một **điểm đến còn nợ**. Khi bạn đặt entry + SL ở giữa đường từ giá hiện tại tới điểm đến đó:

1. SL của bạn (cùng cụm stop của những người vào giống bạn) **cộng thêm nhiên liệu** cho chính cú chạy đó ([[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]]).
2. Setup càng "textbook" (FVG + OTE + CE hợp lưu đẹp) thì cụm stop càng dày → cú quét càng có động cơ.
3. Sau khi quét xong, giá thường đi đúng hướng bias ban đầu — tạo ra loại thua **nguy hiểm nhất về tâm lý**: "tôi phân tích đúng mà, chỉ xui thôi" → lỗi được giữ nguyên và lặp lại.

## 4. Phân loại thanh khoản — kỹ năng nền để không tái phạm

Lỗi này sống được là nhờ **đếm sweep theo hình dạng thay vì theo chức năng**. Trước mỗi lệnh phải phân loại:

- **Internal (IRL)**: FVG, OB, minor swing, thanh khoản nội bộ trong range — bị quét thường xuyên, KHÔNG đủ điều kiện làm "sweep bước 1" cho một quyết định cấp H1. Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]].
- **External / Structural (ERL)**: range high/low, old high/low, điểm định nghĩa dealing range, POI sâu nhất chưa test — đây mới là pool mà mô hình cần thấy bị lấy TRƯỚC khi tin MSS.
- **Scale alignment**: sweep phải cùng cấp với cấu trúc đang giao dịch — sweep M1 không hợp thức hóa được quyết định POI cấp H1 ([[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]]).

## 5. Dấu hiệu nhận biết trước khi bấm lệnh

| Dấu hiệu | Mức độ cảnh báo |
|---|---|
| R:R kế hoạch cao bất thường (>3) nhờ SL "chặt" ở cấu trúc LTF | Amber |
| POI đang định vào có POI khác sâu hơn cùng phía chưa được test | Đỏ |
| Giữa POI và điểm định nghĩa range không còn EQL/swing nội bộ nào làm đệm | Đỏ |
| Range extreme / old high-low / equal H-L rõ ràng còn nguyên phía sau SL | Đỏ |
| MSS xuất hiện ngay cú tap đầu tiên vào POI, TRƯỚC khi pool cấu trúc bị quét | Đỏ |
| Sweep quan sát được chỉ ở cấp LTF (M1) trong khi quyết định ở cấp H1 | Đỏ |
| Khung xác nhận (M5) không in được FVG sạch nhưng vẫn muốn tụt xuống M1 | Đỏ ([[08 - Mistake - Weak Displacement]]) |

Checklist 4 câu trước khi đặt lệnh:

- [ ] Pool chưa-bị-lấy gần nhất nằm phía nào so với SL? (cùng phía SL = dừng)
- [ ] Sweep đã xảy ra là internal hay external/structural? Cùng scale với POI chưa?
- [ ] Nếu đặt SL tại invalidation THẬT (của POI sâu nhất còn hiệu lực), R:R còn lại bao nhiêu? R:R chết = bỏ lệnh, không siết SL.
- [ ] Giữa entry và pool cấu trúc gần nhất có đệm thanh khoản nội bộ không?

## 6. Cách sửa (đưa vào Playbook & schema)

1. **Draw gate (bắt buộc, trước khi mở khung entry)**: xác định pool chưa-bị-lấy gần nhất ở CẢ hai phía. Nếu pool gần nhất cùng phía SL → NO-TRADE hoặc chờ nó bị quét + reclaim rồi mới tìm entry.
2. **Rule POI Priority**: khi ≥2 PD array xếp chồng cùng phía trong Premium/Discount, POI SÂU hơn là terminal. Chỉ giao dịch POI nông sau khi POI sâu đã test-và-từ-chối.
3. **Rule SL theo invalidation thật**: SL neo trên/dưới invalidation của POI sâu nhất còn hiệu lực + buffer. R:R được tính TỪ SL đúng; nếu không đủ → bỏ lệnh.
4. **Rule MSS sau sweep**: chỉ đếm MSS hình thành SAU khi pool cấu trúc liên quan bị lấy. MSS sớm + leg yếu = inducement.
5. **Schema backtest** (bổ sung field để lượng hóa pattern): `internal_liq_buffer` (Yes/No), `structural_liq_behind_sl` (Yes/No), `deeper_poi_untested` (Yes/No). Sau ~10 mẫu mới, so win-rate/expectancy giữa nhóm có/không có cờ này để xác nhận filter bằng dữ liệu (tránh curve-fitting từ n=4).

> [!warning] Chống curve-fitting
> n=4 là đủ để tạo **giả thuyết mạnh** (cả 4 cùng cơ chế, dự đoán được trước outcome), chưa đủ để làm rule thống kê cứng. Cách xử lý đúng: đưa Draw gate vào như rule **quy trình** (nó vốn là một phần chuẩn của 2022 Model — sweep trước entry), đồng thời gắn field schema để dữ liệu tương lai xác nhận/bác bỏ mức độ ảnh hưởng.

## 7. Quan hệ với các mistake khác

- [[02 - Mistake - Enter before liquidity sweep]] — biến thể *entry-timing* của cùng gốc lỗi; note 13 này tổng quát hóa: kể cả khi "có sweep" (nhưng sai loại/sai scale), lỗi vẫn xảy ra.
- [[03 - Mistake - Entry When MSS not in POI Zone]] — MSS sai ngữ cảnh, họ hàng gần của "MSS sớm trước sweep".
- [[04 - Mistake - FOMO Entry]] — động cơ tâm lý thường đứng sau việc không chờ pool bị quét.
- [[05 - Mistake - Not enough RR]] — mặt ngược của "R:R ảo do SL sai chỗ": R:R phải được tính từ invalidation thật.
- [[08 - Mistake - Weak Displacement]] · [[11 - LTF Displacement Not Create FVG, Big Candle But Wick Overlap]] — tín hiệu yếu bị hợp lý hóa xuất hiện trong 3/4 case.

## Liên kết

- Concepts: [[19 - Liquidity]] · [[20 - Liquidity Sweep]] · [[16 - Internal & External Range Liquidity (IRL & ERL)]] · [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] · [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] · [[15 - Inducement]] · [[43 - Liquidity Scale Alignment (Sweep cùng khung MSS-FVG, HTF là Target)]] · [[26 - OTE - Optimal Trade Entry]] · [[21 - Market Structure Shift]]
- Model: [[01 - ICT 2022 Model]]
- Case files: [[02 - Loss - GBPUSD - 2014-07-17 - Long]] · [[01 - Loss - XAUUSD - 2014-05-19 - Short]] · [[02 - Loss- XAUUSD- 2014-05-14- Short]] · [[02 - Loss- EURUSD - 2021-05-07- Short]]
