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
> **METHODOLOGY / REVIEW — không vào lệnh (miss).** Ghi lại một tình huống lặp lại: giá đảo chiều **ngay từ Order Block H1** nhưng vì đang chờ một vùng **EQH phía trên** bị quét, đã **không vào lệnh** dù M5 đã cho MSS. Đây là lỗi **lệch khung (scale mismatch)**, không phải lỗi thực thi. Khái niệm nền: [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]].

![[EQH-target-vs-trigger-20260712.svg]]

> [!warning] Screenshot gốc
> Ảnh chart H1 gốc chưa lưu dạng file. Kéo ảnh vào `10 - Market Analysis/Attachments/` (nên có nhãn symbol + khung) rồi thêm `![[tên-ảnh.png]]` bên dưới để embed. Sơ đồ ở trên là minh họa nguyên lý, không phải chart thật.

## 1. Bối cảnh & kế hoạch ban đầu

Top-down [[32-Top-down-Analysis-Multiple-Timeframes|D1 → H1 → M5]]:

- **D1 — Bias:** cấu trúc **LH/LL**, phía dưới có vùng **EQL** làm [[39-Draw-on-Liquidity-Tai-sao-gia-di-chuyen-ai-la-doi-ung|draw]] → **Bias Bearish**.
- **H1 — POI:** [[25-OB-Order-Block|Order Block]] **1.75360 – 1.74360** trong [[27-Premium-Discount|premium]]. Kế hoạch: chờ giá retrace về OB, phản ứng, đảo chiều xuống thuận bias.
- **Điều đã xảy ra:** giá retrace tới OB, **quét qua [[10-Consequent-Encroachment-Mean-Threshold|CE]] và qua cạnh trên OB rồi đóng cửa vào lại OB**. Phía trên OB có vùng **EQH (4 đỉnh ngang)** = một bể [[07-Buy-side-Liquidity|BSL]] lớn cấp H1.
- **Quyết định (chỗ sai):** vì giá **không quét EQH phía trên**, kết luận "chưa có [[20-Liquidity-Sweep|liquidity sweep]]" và **không vào** khi M5 tạo [[21-Market-Structure-Shift|MSS]] quay xuống.

## 2. Chẩn đoán — hai lỗi, một gốc

**Gốc:** để một bằng chứng **vắng mặt** (cú quét EQH) phủ quyết một bằng chứng **hiện diện** (M5 MSS tại POI).

**Lỗi #1 — "chưa có liquidity sweep" là sai về sự kiện.** Chính mô tả "quét qua CE + qua cạnh trên OB rồi đóng vào OB" **đã là một liquidity sweep**: cây nến wick lên xuyên mép trên OB đã quét sạch buy stops (BSL cục bộ, các short-term high) đậu ngay trên OB, rồi từ chối. Cú sweep *đã* xảy ra — chỉ là ở một bể khác, gần hơn, nhỏ hơn.

**Lỗi #2 — lệch khung (scale mismatch).** Trong mô hình [[01 - ICT 2022 Model|2022]], chuỗi **Sweep → MSS → FVG diễn ra CÙNG một khung** — khung entry (M5). Cú sweep mà M5 MSS cần là một cú quét **cấp M5** (STH tại POI), **không phải** cú quét vùng **EQH cấp H1**. Việc nâng bể H1 lên đóng vai trò mà một bể M5 phải đảm nhiệm chính là lệch khung → trigger không bao giờ "đủ" theo tiêu chí sai đó → đứng nhìn lệnh trôi. Chi tiết: [[43-Liquidity-Scale-Alignment-Sweep-cung-khung-MSS-FVG-HTF-la-Target]].

## 3. Đọc đúng chuỗi tín hiệu

> [!summary] Trình tự hợp lệ
> **D1 bias giảm → H1 POI = OB premium → giá tap OB, quét CE + BSL cục bộ trên OB, đóng lại → M5 displacement + MSS xuống → FVG entry → target SSL/EQL dưới.**

- Cú quét cục bộ trên OB + M5 MSS = **trigger đầy đủ, cùng scale** → **được phép vào** (SL trên đỉnh phản ứng, target [[30 - Sell-side Liquidity|SSL]] dưới).
- **M5 MSS là trọng tài**: nó bắn ra tại OB nghĩa là thị trường báo "đảo chiều bắt đầu TẠI ĐÂY, không phải tại EQH".

## 4. Mâu thuẫn "purge EQH trước hay không?" — để M5 phân xử

Nỗi lo của bạn **có cơ sở ICT thật**: 4 đỉnh ngang phía trên là bể BSL béo, giá *có thể* chạy lên "dọn" nó trước khi đảo (kịch bản purge-then-reverse). Nhưng không thể biết trước chắc chắn, nên đừng chọn bằng cảm tính — để [[16-Internal-External-Range-Liquidity-IRL-ERL|cấu trúc]] M5 quyết theo thời gian thực:

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

## 8. Tình huống thực chiến (War Stories) — khi nào EQH THẬT SỰ là điều kiện chờ

> [!info] Vì sao có mục này
> Mục 1–7 sửa một lỗi cụ thể: chờ EQH trong khi M5 đã cho MSS tại OB. Nhưng nếu chỉ dừng ở đó, dễ đẻ ra lỗi ngược — không bao giờ chờ EQH nữa, kể cả những lúc **đúng là phải chờ**. Ba tình huống dưới đây, đúc kết từ nhiều năm quan sát loại setup "OB có bể HTF ngay phía trên", vẽ ranh giới rõ cho cả hai chiều sai.

![[MultiPool-Stack-TargetVsTrigger-20260712.svg]]

### W1 — Cú purge thật: khi M5 KHÔNG xác nhận tại OB, và EQH xa mới là nơi MSS thật xuất hiện

**Tình huống:** giá retrace vào OB premium, chạm — nhưng khác với case trong note này, M5 **không cho displacement + MSS** ngay tại lần chạm đầu. Giá chỉ khựng nhẹ rồi tiếp tục grind lên, xuyên qua cả BSL cục bộ mà không để lại dấu vết đảo chiều nào đáng kể, và chạy thẳng tới cụm EQH xa (cấp H1). Chỉ tại đó, sau khi quét sạch bể lớn, M5 mới in ra displacement + MSS thật.

**Bản chất:** đây chính là kịch bản (3) đã nêu ở mục 4 — nhưng phải *thấy nó xảy ra*, không được giả định trước. Cái phân xử duy nhất là bằng chứng M5 tại lần chạm đầu: có hay không có. Không có gì đảm bảo bể gần luôn là bể "đúng" — đôi khi thị trường thực sự cần dọn sạch cả bể xa mới đủ nhiên liệu cho một cú đảo chiều xứng tầm với draw H1/D1 phía sau.

**Rule đo được:** trước khi vào lệnh tại lần chạm OB đầu tiên, chấm hai trường — `m5_confirmed_at_first_tap` (có/không) và nếu không, `htf_pool_intervened` (có/không, điền sau khi biết kết quả). Sau 20–30 mẫu loại "OB có bể HTF ngay trên", tỷ lệ hai nhóm này cho biết setup của  thiên về kịch bản A hay B nhiều hơn — đừng đoán bằng cảm tính, để dữ liệu trả lời.

### W2 — Hối tiếc & rượt giá (chase) sau một cú miss đúng kiểu này

**Tình huống tâm lý rất phổ biến:** sau khi bỏ lỡ một lệnh vì lý do y hệt case này (chờ EQH trong khi M5 đã xác nhận), phản xạ tự nhiên của phần lớn trader — kể cả trader có kinh nghiệm — là dao động sang **cực đoan ngược lại**: lần setup tương tự kế tiếp, nhảy vào **ngay khi vừa chạm OB**, không chờ M5 xác nhận gì cả, chỉ vì "lần trước chờ nên mất lệnh". Đây là **revenge trade trá hình dưới lớp vỏ 'rút kinh nghiệm'** — và nó tệ hơn cái lỗi gốc, vì lỗi gốc chỉ mất một cơ hội, còn lỗi này mất tiền thật trên một entry chưa có trigger.

**Vì sao dễ mắc:** não người xử lý một cơ hội bị bỏ lỡ như một mất mát thực sự (loss aversion), dù chưa từng có tiền trong đó. Cảm giác "lần này không được để lỡ nữa" đủ mạnh để ghi đè lên toàn bộ checklist entry model.

**Rule đo được:** một lệnh miss hợp lệ (đọc đúng nguyên tắc, chỉ là chưa xảy ra) phải được ghi `missed_valid_setup = true` và đóng lại như dữ liệu tốt, không phải vết thương cần trả thù. Chấm thêm `chased_after_miss` (có/không) cho lệnh kế tiếp cùng loại — nếu con số này cao, đó là dấu hiệu kỷ luật đang bị chi phối bởi cảm xúc từ lệnh trước, cần một khoảng dừng (bước ra khỏi chart) trước khi vào lệnh tiếp theo.

### W3 — Nhiều tầng pool chồng lấn: chọn nhầm bể vì "nhìn không đủ xa"

**Tình huống:** trên các symbol thanh khoản cao (NAS100, XAUUSD), rất hay gặp cấu trúc có **hai hoặc ba tầng EQH/BSL xếp chồng** phía trên một OB — một cụm gần (equal highs nhỏ, vài phiên gần nhất) và một cụm xa hơn (đỉnh chu kỳ, vài tuần/tháng). Lỗi định vị hay gặp: trader chỉ nhìn thấy cụm xa (vì nó "to" và dễ vẽ trên HTF), bỏ sót cụm gần — rồi lấy chính cụm xa đó làm điều kiện chờ, trong khi cụm gần mới là bể mà M5 MSS thực sự phản ứng theo (đúng tinh thần mục 5 của note gốc: draw có thể có nhiều lớp, không phải một đường thẳng duy nhất tới đích cuối).

**Cách phòng tránh:** trước khi đặt câu hỏi "đã sweep chưa", liệt kê **toàn bộ** các mức liquidity nằm giữa giá hiện tại và target cuối cùng — không chỉ mức xa nhất. Xếp chúng theo tầng (gần → xa), rồi hỏi từng tầng một: tầng này có phải là bể mà entry model (M5) cần quét không, hay nó chỉ là một trạm dừng/target trung gian?

**Rule đo được:** trong checklist trước lệnh, thêm mục *"Vẽ hết các tầng liquidity giữa giá và target — không chỉ tầng xa nhất"*. Field: `liquidity_layers_mapped` (có/không) trước khi quyết định trigger.

> [!success] Tổng kết mục 8
> Ba tình huống trên xoay quanh một trục: **M5 (khung entry) luôn là trọng tài cuối cùng, không phải khoảng cách hay kích thước của bể liquidity.** W1 cho thấy đôi khi bể xa mới đúng; W2 cảnh báo phản ứng cảm xúc sau một lần chờ đúng; W3 nhắc đừng bỏ sót các tầng ở giữa. Cả ba đều quy về cùng một kỷ luật: quan sát bằng chứng M5 tại thời điểm thật, không quyết định bằng cảm tính hay bằng ký ức của lệnh trước.

---
*Ghi chú: date = ngày capture (VN, UTC+7). Không log backtest vì không vào lệnh (miss) — đây là note phương pháp/review. Giá OB do người dùng cung cấp; symbol/mốc chart chưa xác nhận. Sơ đồ minh họa nguyên lý, không phải chart thật. Các tình huống ở mục 8 là kinh nghiệm tổng hợp mang tính minh họa (composite), không phải nhật ký của một lệnh cụ thể.*


# 🔍 Bổ sung audit cho: 2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)

> [!warning] File gốc không có trong phiên làm việc này
> File note gốc "2026-07-12 H1-M5 - EQH chưa quét - Sweep phải cùng khung MSS-FVG (Target vs Trigger)" không nằm trong các file được tải lên phiên fork này (chỉ 10/15 file gốc có sẵn). Nội dung dưới đây được trích từ bản audit tổng — dán trực tiếp vào cuối file gốc trong vault Obsidian của cậu để hoàn tất việc bổ sung cho case này. Đồng thời sửa frontmatter `status:` thành `methodology` và thêm `evidence_tier: 0`.

> [!info] Nguồn
> Phần dưới đây được trích trực tiếp từ bản audit tổng [[2026-08-02 - Deep Audit 15 Case Studies - Doctrine v2]] (mục 4, case #6/15) và tách vào ngay file gốc để không phải mở file tổng mỗi lần tra cứu. Bảng tra cứu đầy đủ 15 case và các phần audit hệ thống/tranh biện/doctrine dùng chung vẫn nằm ở file tổng.

**Tóm tắt:** Review một lệnh MISS (không phải lệnh thắng/thua). Giá đảo chiều ngay tại OB H1 nhưng vì đang chờ EQH phía trên bị quét, không vào dù M5 đã cho MSS. Chẩn đoán: lỗi lệch khung (scale mismatch) — sweep cho trigger M5 phải cùng khung M5, không phải bể EQH cấp H1.

**Điểm mạnh:** đây là note có chất lượng tranh biện nội tại tốt nhất trong 15 file — tự đặt ra chính xung đột ("purge EQH trước hay không") rồi giải quyết bằng nguyên tắc phân xử theo bằng chứng thời gian thực (mục 4: "để M5 phân xử") thay vì chọn phe cố định; ba War Story (W1, W2, W3) vẽ ranh giới hai chiều sai rất khéo — không chỉ sửa lỗi gốc mà còn cảnh báo lỗi over-correction (W2: chase sau miss).

**Lỗ hổng/điểm mù:** đây cũng là note duy nhất tường minh nói ra tại sao khái niệm "EQH = target không phải trigger" có thể tự mâu thuẫn (mục 5: "nếu giá thật sự lên quét EQH, OB có thể đã bị phá và setup không còn giá trị") nhưng KHÔNG đưa ra cách giải quyết mâu thuẫn đó ngoài "kiểm chứng bằng cách kéo chart sang phải xem sau" — tức là chấp nhận đây là một câu hỏi mở, chưa có quy tắc quyết định trước (ex-ante), chỉ có thể đánh giá sau (ex-post).

> [!question] Tranh biện Devil's Advocate (đa vòng)
> **Luận điểm ban đầu:** "M5 luôn là trọng tài cuối cùng — sweep + MSS cùng khung tại OB là đủ, không cần chờ EQH."
>
> **Phản biện vòng 1:** Nguyên tắc này ưu tiên khung entry (M5) hơn khung target (H1/D1) một cách gần như tuyệt đối. Nhưng nếu bể EQH thực sự "béo" (4 đỉnh ngang, nhiều tuần tích lũy) và OB H1 chỉ là một phản ứng nhỏ mới hình thành, há chẳng phải bể lớn hơn có "trọng lượng hấp dẫn" market-maker mạnh hơn một MSS M5 đơn lẻ? W1 trong chính note này thừa nhận đúng kịch bản này có thể xảy ra ("đôi khi thị trường thực sự cần dọn sạch cả bể xa mới đủ nhiên liệu cho một cú đảo chiều xứng tầm").
>
> **Phản-phản biện:** Đúng, nhưng W1 cũng nói rõ: "cái phân xử duy nhất là bằng chứng M5 tại lần chạm đầu: có hay không có" — nghĩa là nguyên tắc không phải "M5 luôn thắng bất kể", mà là "M5 là bằng chứng CÓ SẴN duy nhất tại thời điểm quyết định TRƯỚC KHI biết bể xa có bị dọn hay không". Đây là khác biệt quan trọng giữa "M5 luôn đúng" (sai) và "M5 là bằng chứng duy nhất khả dụng ex-ante" (đúng, khiêm tốn hơn).
>
> **Phản biện vòng 2:** Nhưng nếu vậy, hai kịch bản (M5 xác nhận tại OB gần / M5 không xác nhận, giá chạy tới EQH xa) đều đúng-về-sau theo cách chính bằng chứng chúng tạo ra — nói cách khác nguyên tắc này không thể sai được bằng thiết kế (unfalsifiable trong ngắn hạn), vì bất kỳ kết quả nào cũng "giải thích được" sau khi nó xảy ra. Đây là dấu hiệu cảnh báo kinh điển của một framework có vẻ chặt chẽ nhưng thực chất mô tả lại quá khứ tốt hơn là dự đoán tương lai.
>
> **Phản-phản biện cuối:** Điểm này đúng về mặt triết học khoa học, nhưng không làm framework vô dụng — nó chỉ có nghĩa framework này thuộc nhóm "quy tắc quyết định hành động tại thời điểm t" (what to do NOW, given evidence NOW), không phải "mô hình dự đoán xác suất". Với một quy tắc hành động (không phải dự đoán), tiêu chuẩn đánh giá đúng không phải "có dự đoán đúng bể nào sẽ bị dọn" mà là "hành động dựa trên nó có nhất quán và có kỷ luật hay không qua nhiều lần lặp lại" — đó là câu hỏi Tier 1 (cần n≥20), chưa trả lời được ở đây.
>
> **Phán quyết:** Nguyên tắc "M5 là trọng tài, đánh giá bằng chứng thời điểm hiện tại thay vì đoán trước" là một **quy tắc quyết định hợp lý về logic** (không unfalsifiable theo nghĩa xấu — nó chỉ đơn giản là một chính sách hành động, không phải một tiên đoán) nhưng **hiệu quả thực của chính sách này (so với các chính sách khác như "luôn chờ bể lớn nhất") chưa được đo** — cần backtest so sánh 2 chính sách trên cùng bộ setup.

**Hành động:** thêm case này vào backlog thu thập dữ liệu Tier 1 — so sánh 2 chính sách (a) vào ngay khi M5 xác nhận tại bể gần vs (b) luôn chờ bể HTF xa bị quét, trên cùng ≥20 setup dạng "OB có bể HTF ngay phía trên".

**Đề xuất field đo lường:** `m5_confirmed_at_first_tap`, `htf_pool_intervened`, `missed_valid_setup`, `chased_after_miss`, `liquidity_layers_mapped` — cả 5 field đã đề xuất sẵn trong note gốc, đưa thẳng vào schema Doctrine v2 §6 Rule 14.

![[liquidity-fractal-scale-alignment-20260802.svg]]


### Tranh biện chéo liên quan

### 5.3 — "Sweep phải cùng khung MSS" (note EQH 07-12) vs "Fractal Liquidity: M15 wick = M1 sweep" (note 07-13)

**Bề mặt có vẻ mâu thuẫn:** note EQH 07-12 nhấn mạnh sweep cho trigger PHẢI cùng khung với MSS/FVG (không lấy bể HTF làm trigger cho MSS LTF). Note 07-13 (Fractal Liquidity) lại nói một wick M15 dài, nhìn không có SSL rõ, thực chất chứa nhiều sweep nội bộ M1/M5 bên trong nó — ngụ ý rằng "khung" nơi sweep xảy ra có thể MƠ HỒ/lồng nhau (một sự kiện M15 = nhiều sự kiện M1).

> [!question] Tranh biện đa vòng
> **Vòng 1:** Nếu sweep M1 "ẩn" bên trong một wick M15, và MSS được xác nhận trên M5, vậy sweep đó có được coi là "cùng khung" với MSS M5 hay không? Về mặt hình thức nhìn từ M15, sự kiện chỉ là "một cái râu nến" (theo đúng câu note 07-13 dùng) — không có sweep M15 riêng biệt để đối chiếu "cùng khung" với MSS M5.
>
> **Vòng 2 — Giải quyết bằng định nghĩa "khung":** Hai note thực ra không mâu thuẫn nếu định nghĩa "khung" đúng là KHUNG ENTRY (nơi MSS được xác nhận), không phải khung mà ta ĐANG NHÌN chart. Note EQH 07-12 nói: sweep phải cùng khung với khung MSS/FVG xác nhận (ví dụ nếu MSS xác nhận trên M5, sweep dùng làm trigger cũng phải là sweep cấp M5, dù ta có thể đang xem chart M15 để có bối cảnh). Note 07-13 chỉ ra: đôi khi để THẤY sweep cấp M5 đó, ta phải zoom vào M1/M5 vì M15 không đủ độ phân giải để hiển thị nó rõ — đây là vấn đề CÔNG CỤ QUAN SÁT (resolution), không phải vấn đề ĐỊNH NGHĨA KHUNG (scale). Hai note đang nói về hai trục khác nhau: EQH 07-12 nói về "sweep phải cùng CẤP ĐỘ (scale) với MSS", 07-13 nói về "để thấy sweep đúng cấp độ, có khi phải đổi khung NHÌN (viewing timeframe) xuống thấp hơn".
>
> **Vòng 3 — Phản biện lại sự "giải quyết" này:** Nhưng nếu phải liên tục đổi khung nhìn xuống M1 để "tìm ra" sweep ẩn bên trong mọi wick M15 nghi ngờ, quy tắc "sweep cùng khung MSS" trở nên gần như luôn luôn ĐÚNG BẰNG ĐỊNH NGHĨA (tautological) — vì bất kỳ MSS nào cũng có thể "tìm thấy" một sweep tương ứng nếu ta đủ kiên nhẫn zoom sâu đủ mức. Điều này làm giảm giá trị phân loại/loại trừ (falsifiability) của quy tắc: nếu không có trường hợp nào mà "sweep cùng khung" có thể bị coi là KHÔNG thỏa mãn (vì luôn tìm ra ở khung đủ nhỏ), quy tắc mất khả năng giúp loại bỏ setup tồi.
>
> **Vòng 4 — Phản-phản biện, khôi phục falsifiability:** Đây là lo ngại hợp lý nhưng note 07-13 tự đưa ra giới hạn: sweep checklist 5 điểm (bể xác định trước, giá thực breach, reject nhanh, tại POI, có displacement/MSS xác nhận SAU) — không phải bất kỳ nhiễu nào trên M1 cũng được tính là "sweep hợp lệ", chỉ những gì thỏa 5 điều kiện đó. Vậy quy tắc vẫn falsifiable: nếu zoom vào M1 mà KHÔNG tìm thấy cấu trúc thỏa 5 điều kiện (chỉ là nhiễu ngẫu nhiên không có pool xác định trước), sweep "cùng khung" thực sự không tồn tại, và MSS đó phải bị coi là thiếu trigger hợp lệ.
>
> **Phán quyết:** Hai note KHÔNG mâu thuẫn về bản chất — chúng nói về hai trục khác nhau (scale của sự kiện vs resolution của công cụ quan sát) — nhưng nếu áp dụng cẩu thả (luôn "tìm ra" sweep bất kể zoom bao sâu), quy tắc có nguy cơ trở thành tautological. Điều kiện phòng vệ: sweep checklist 5 điểm PHẢI được áp dụng nghiêm ngặt ở khung zoom-in, không chỉ "thấy có wick, kết luận có sweep".

**Hành động (Doctrine v2 Rule 3):** khi zoom xuống khung nhỏ hơn để tìm sweep "ẩn" bên trong một wick khung lớn, bắt buộc chấm đủ 5 điều kiện sweep checklist tại khung đã zoom — không được kết luận "có sweep" chỉ vì "có thể zoom vào và thấy một chỗ giá đảo nhẹ".


### 5.4 — "HTF pool = target không phải trigger" (note EQH 07-12) vs "external sweep = narrative confirmation" (note 07-20)

**Bề mặt có vẻ mâu thuẫn:** note EQH 07-12 nói dứt khoát: EQH cấp HTF là TARGET (draw tương lai), không phải điều kiện vào lệnh — đừng chờ nó bị quét mới trigger. Note EURUSD 07-20 lại dùng chính việc "external BSL 1.16874/1.16919 đã bị quét" như một phần bằng chứng CỦNG CỐ narrative bearish, gần như một điều kiện hỗ trợ cho quyết định vào lệnh.

> [!question] Tranh biện đa vòng
> **Vòng 1:** Nếu external sweep đã xảy ra (BSL 1.16874/1.16919 bị quét ở note 07-20) được dùng để "củng cố narrative", vậy nó đang đóng vai trò gần giống một ĐIỀU KIỆN HỖ TRỢ cho quyết định vào lệnh — về bản chất khác gì "chờ EQH bị quét" mà note EQH 07-12 phê phán?
>
> **Vòng 2 — Phân biệt THỜI ĐIỂM sử dụng bằng chứng:** Khác biệt cốt lõi nằm ở THỜI ĐIỂM đánh giá: note EQH 07-12 phê phán việc CHỜ (tương lai, chưa xảy ra) một sự kiện HTF làm điều kiện TRIGGER bắt buộc trước khi hành động. Note 07-20 dùng một sự kiện HTF ĐÃ XẢY RA (quá khứ, external sweep đã hoàn tất) như một mảnh bằng chứng bổ sung cho bức tranh tổng thể, không phải điều kiện phải chờ thêm. Nói cách khác: "external sweep đã xảy ra, đây là một phần bằng chứng của bối cảnh hiện tại" (hợp lệ, không mâu thuẫn với note EQH) khác với "tôi sẽ không vào lệnh cho tới khi external sweep xảy ra" (đây mới là điều bị phê phán).
>
> **Vòng 3 — Phản biện lại sự phân biệt trên:** Nhưng ranh giới giữa "dùng làm bối cảnh" và "dùng làm điều kiện chờ" có thể rất mỏng trong thực hành. Nếu note 07-20 viết narrative theo kiểu "vì external sweep đã xác nhận, tôi tự tin hơn với hướng bearish" — điều gì ngăn cản, ở một setup TƯƠNG LAI mà external sweep CHƯA xảy ra, cùng logic đó bị lật thành "tôi cần chờ external sweep xảy ra trước khi tự tin đủ để vào lệnh" — đúng chính xác cái bẫy mà note EQH 07-12 cảnh báo?
>
> **Vòng 4 — Giải quyết bằng quy tắc thời gian tường minh:** Ranh giới đúng không nằm ở "đã xảy ra hay chưa" một cách chung chung, mà ở việc quy tắc entry (trigger) có PHỤ THUỘC logic vào sự kiện HTF đó hay không. Nếu trigger thực sự là "Sweep M5 + MSS M5 + FVG M5 tại POI" (như note EQH 07-12 định nghĩa) và external sweep HTF chỉ là một dòng ghi chú bối cảnh KHÔNG NẰM trong điều kiện trigger chính thức, thì việc nó "đã xảy ra hay chưa" không ảnh hưởng quyết định vào/không vào — chỉ ảnh hưởng CONFIDENCE/SIZE. Đây chính là điều note 07-20 đang làm đúng: external sweep dùng để tăng/giảm độ tự tin, KHÔNG phải một điều kiện trong checklist trigger chính thức của nó (checklist trigger vẫn là M15 sweep→MSS→displacement, độc lập với external sweep).
>
> **Phán quyết:** Không mâu thuẫn thật khi trigger chính thức được định nghĩa tách bạch khỏi bằng chứng bối cảnh — nhưng đây là ranh giới DỄ BỊ XÓA NHÒA trong thực hành nếu không viết tường minh. Rủi ro thật: nếu một ngày nào đó cậu viết narrative kiểu "chờ external sweep rồi mới chắc" cho một setup TƯƠNG LAI (external sweep chưa xảy ra), đó là lúc quy tắc EQH 07-12 bị vi phạm thật.

**Hành động (Doctrine v2 Rule 4):** trong mọi note tương lai, tách rõ 2 mục trong phần setup: "Trigger chính thức" (điều kiện đủ + cần để vào lệnh, luôn ở khung entry) và "Bối cảnh hỗ trợ" (bao gồm external HTF sweep đã xảy ra, SMT divergence...) — không để hai mục này trộn lẫn trong cùng một đoạn văn xuôi.



### Rule liên quan (Doctrine v2)

### Rule 15 — Taxonomy `status` tách 4 giá trị, đồng bộ với `in_trade`
**Phát biểu:** `status: analysis | watchlist | backtest | live`; `status: backtest` hoặc `live` bắt buộc `in_trade: true` kèm entry/SL/TP/R-multiple; `in_trade: false` chỉ được đi với `analysis` hoặc `watchlist`.
**Tier hiện tại:** N/A (quy ước vận hành, không phải rule thị trường).
**Nguồn:** §3.5.


### Rule 3 — Sweep phải cùng khung (scale) với MSS/FVG; HTF pool là target, không phải trigger
**Phát biểu:** trigger cho một entry (Sweep + MSS + FVG) phải xảy ra cùng cấp độ (scale) với khung entry đã chọn; một bể liquidity ở khung cao hơn (EQH/EQL H1/D1) chỉ đóng vai trò TARGET (draw tương lai), không được dùng làm điều kiện chờ trước khi trigger khung entry được kích hoạt. Khi zoom xuống khung nhỏ hơn để xác nhận sweep "ẩn" trong một wick khung lớn, bắt buộc áp đủ 5 điều kiện sweep checklist tại khung đã zoom.
**Tier hiện tại:** Tier 0 (giả thuyết hợp lý, có 1 case minh họa dạng miss — không có lệnh thật để đo).
**Điều kiện nâng tier:** ≥20 setup dạng "OB có bể HTF ngay phía trên", so sánh 2 chính sách (vào khi M5 xác nhận tại bể gần / chờ bể xa bị quét).
**Nguồn:** case 4.6 (EQH 07-12), case 4.7 (Internal Sweep 07-13), §5.3.
