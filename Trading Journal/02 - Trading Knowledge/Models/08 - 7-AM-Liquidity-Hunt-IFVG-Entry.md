---
type: ict-concept
concept: 07:00 AM Liquidity Hunt + IFVG Entry
aliases:
  - 07:00 AM Liquidity Hunt + IFVG Entry
  - 7 AM IFVG Model
  - ICT 2024 Lecture 2 Model
  - AM Session IFVG
tags:
  - trading/ict/model
  - trading/study
  - "#ict2024"
  - "#ifvg"
  - "#ny-open"
status: developing
category: Entry Model
last_reviewed: 2026-07-05
created: 2026-07-04
updated: 2026-07-28
---

# 08 - 07:00 AM Liquidity Hunt + IFVG Entry

> [!info] Link
> [ICT 2024 Mentorship Lecture 2 Notes — 07:00 AM IFVG Model + PDF](https://innercircletrader.net/tutorials/ict-2024/mentorship-lecture-2/)

> [!summary] Tóm tắt 1 câu
> **Mô hình 07:00 AM (ICT 2024, Lecture 2) chuyển entry từ mốc 08:30 sang nhịp hồi AM-session sau 07:00: giá hồi về range London, hunt relative equal highs/lows, tạo [[21-Market-Structure-Shift|MSS]]; vào lệnh tại 50% CE ([[10-Consequent-Encroachment-Mean-Threshold|consequent encroachment]]) của [[17-Inverse-Fair-Value-Gap-iFVG|IFVG]] (FVG đầu tiên trước cú hunt) — hoặc breaker nếu không có IFVG; chốt lời bằng Fib -2/-2.5.**

> [!important] Nguyên tắc cốt lõi
> **IFVG là FVG ĐẦU TIÊN ngay trước cú stop-hunt** — sau MSS nó bị đảo vai (support↔resistance) và trở thành vùng nhạy nhất. Entry chuẩn là **50% CE của IFVG**, không phải vào lúc MSS. Và luôn nhớ **lưu ý 30 phút đầu**: sau 07:00/08:00/09:00 giá thường đi NGƯỢC bias để hunt thanh khoản trước.

> [!tip] Bản đồ đọc note này
> Mục 1–2 = *thời điểm + định nghĩa*. Mục 3 = *WHY (vì sao IFVG nhạy)*. Mục 4–7 = *HOW (bearish/bullish, Fib, lưu ý 30')*. Mục 8–11 = *thị trường, so 08:30, ví dụ*. Mục 12–18 = *thực chiến & prop-firm*. Mới học: 1→7; đã trade: nhảy 8–12.

---

## 1. Thời điểm & bối cảnh

![[AM0700IFVG-Advanced-Timeline.svg|697]]
> [!info] Mô tả hình
> Timeline ngang từ London Open qua ba mốc 07:00/08:00/09:00 NY; range London được đánh dấu là DOL; tại mỗi mốc giờ có một ô nhỏ "30' đầu: counter-move" trước khi mũi tên hunt+MSS dẫn ra khỏi range.

- **Ngồi trước máy trước 07:00 NY.** Nếu mới, đừng nhìn gì trước đó; nếu có kinh nghiệm, chỉ xem **đỉnh & đáy phiên London** (= draw on liquidity).
- **Đặc tính đầu tiên của AM-session:** giá **hồi lại vào trong range London**.
- **Đừng dự đoán** — chờ giá tự in relative equal highs/lows trên **5m/1m**.
- **Khung thời gian:** 15m · 5m · 1m · thêm **15 giây** cho entry tinh.
- **Mốc giờ chính:** 07:00 · 08:00 · 09:00 (NY).

---

## 2. Định nghĩa chủ chốt

- **SIBI** = FVG down-closed (giảm); **BISI** = FVG up-closed (tăng).
- **IFVG** = [[17-Inverse-Fair-Value-Gap-iFVG|Inversion Fair Value Gap]] — FVG bị giá đóng xuyên qua sau MSS, đảo vai.
- **Breaker** = một [[25-OB-Order-Block|Order Block]] **thất bại** (dùng làm entry dự phòng khi không có IFVG).
- **Relative Equal High/Low** — đỉnh/đáy có swing đối diện thấp/cao hơn ở bên phải (swing failure).
- **Fractal** — tính lặp lại của hành vi giá trên mọi khung.
- **"Specific"** — **FVG đầu tiên ngay trước stop-hunt** là IFVG nhạy nhất.
- **Consequent Encroachment (CE)** — mức 50% (giữa) của một PD array. Xem [[10-Consequent-Encroachment-Mean-Threshold]].
- **Fibonacci inputs:** 0 · 0.5 · 1 · **-2** · **-2.5**.

---

## 3. IFVG — vì sao là entry nhạy nhất

![[AM0700IFVG-Advanced-IFVG-Concept.svg|697]]
> [!info] Mô tả hình
> Chart khái niệm: nhịp tăng tạo FVG tăng (BISI, hỗ trợ) → giá hunt relative equal highs (quét thanh khoản) → displacement xuống tạo MSS đóng xuyên FVG → vùng FVG đảo màu thành IFVG (kháng cự) với đường 50% CE; nến retest từ dưới bị từ chối tại CE.

Một FVG tăng (BISI) là **support** khi giá đi lên. Nhưng sau khi giá **hunt thanh khoản** rồi tạo **MSS** và **đóng xuyên** qua nó, FVG đó **đảo vai** thành **kháng cự** = **IFVG**. FVG **đầu tiên trước cú hunt** là IFVG nhạy nhất — đây chính là vùng ta canh **50% CE** để vào lệnh.

![[AM0700IFVG-WhyItWorks.svg|697]]
> [!info] Mô tả hình
> Sơ đồ flow 5 khối ngang: Dòng lệnh sai hướng tạo FVG → Lệnh mắc kẹt tích tụ tại FVG này → Hunt thanh khoản + MSS đảo chiều → FVG đảo vai thành IFVG → Test lại 50% CE để giải quyết lệnh mắc kẹt. Sơ đồ khái niệm, không phải chart giá thật.

> [!important] Vì sao "FVG ĐẦU TIÊN trước hunt" chứ không phải FVG nào khác?
> FVG đầu tiên ngay trước cú stop-hunt là **dấu vết cuối cùng của dòng lệnh sai hướng** trước khi thuật toán đảo chiều. Đó là nơi tập trung nhiều lệnh mắc kẹt nhất. Khi giá đóng xuyên qua nó (đảo vai) rồi quay lại test, đây là mức phải được "giải quyết" → phản ứng nhạy và dứt khoát nhất. Đánh dấu FVG sau đó (đã nằm trong chân displacement) hoặc FVG trước đó (quá xa cú hunt) đều cho entry kém nhạy hơn.

> [!note] Vì sao AM session (sau 07:00) là bối cảnh lý tưởng
> Đặc tính đầu phiên AM là giá **hồi lại vào trong range London** — và range London (đỉnh/đáy) chính là draw on liquidity. Cú hồi này tạo ra hunt relative equal + IFVG một cách tự nhiên. Đây là lý do bạn *chờ giá hồi về range*, không đuổi theo cú mở phiên. Liên hệ [[38-Liquidity-Reflexivity-Bay-dam-dong-ICT]]: đám đông đặt lệnh quanh relative equal → trở thành nhiên liệu cho cú hunt.

---

## 4. Kịch bản BEARISH

![[AM0700IFVG-Advanced-Bearish.svg|697]]
> [!info] Mô tả hình
> Chart kịch bản Bearish: nhịp tăng grab relative equal highs (sweep) → FVG đầu tiên trước cú hunt được đánh dấu → displacement xuống phá swing low tạo MSS → FVG đảo vai thành IFVG với 50% CE = điểm SELL → giá tiếp tục xuống; stop đặt trên swing high post-07:00.

1. Giá hình thành và **grab relative equal highs** sau 07:00.
2. Chờ quay lại range và **đóng dưới swing low = MSS** xuống.
3. Đánh dấu **FVG đầu tiên trước cú hunt** làm **IFVG**, và **bearish breaker** sau khi phá swing low.
4. Vào **SELL** tại **50% CE của IFVG**. Nếu không có IFVG → vào **bearish breaker**.
5. **Stop trên swing high** hình thành post-07:00 hunt.
6. **TP:** next draw on liquidity, hoặc Fib từ **đỉnh post-07:00 → lowest low tại 07:00 (open)**, chốt tại **-2 / -2.5**.

---

## 5. Kịch bản BULLISH

![[AM0700IFVG-Advanced-Bullish.svg|697]]
> [!info] Mô tả hình
> Chart kịch bản Bullish: nhịp giảm grab relative equal lows (sweep) → FVG đầu tiên trước cú hunt được đánh dấu → displacement lên phá swing high tạo MSS → FVG đảo vai thành IFVG với 50% CE = điểm BUY → giá tiếp tục lên; stop đặt dưới swing low post-07:00.

1. Giá hình thành và **grab relative equal lows** sau 07:00.
2. Chờ quay lại range và **đóng trên swing high = MSS** lên.
3. Đánh dấu **FVG đầu tiên trước cú hunt** làm **IFVG**, và **bullish breaker**.
4. Vào **BUY** tại **50% CE của IFVG**. Nếu không có IFVG → vào **bullish breaker**.
5. **Stop dưới swing low** hình thành post-07:00 hunt.
6. **TP:** next DOL, hoặc Fib từ **đáy post-07:00 → highest high tại 07:00 (open)**, chốt tại **-2 / -2.5**.

---

## 6. Mục tiêu Fibonacci + Entry CE

![[AM0700IFVG-Advanced-Fib-Targets.svg|697]]
> [!info] Mô tả hình
> Chart minh họa các mức Fibonacci 0 (swing post-07:00) · 0.5 · 1 (open 07:00) · -2 · -2.5 vẽ ngang qua một nhịp displacement mẫu; đánh dấu điểm chốt bậc thang: một phần tại -2 (dời SL về BE), phần còn lại tại -2.5.

Dùng Fib với inputs **0 · 0.5 · 1 · -2 · -2.5**. Vẽ từ swing hình thành post-07:00 hunt **về** giá mở cửa 07:00. Chốt **theo bậc thang**: một phần tại **-2**, phần còn lại tại **-2.5** — đóng hết tại -2 sẽ bỏ lỡ phần lớn của move. Có thể thay bằng next draw on liquidity làm target. Liên hệ [[31-Standard-Deviation|Standard Deviation]] projections.

![[AM0700IFVG-CE-Entry.svg|697]]
> [!info] Mô tả hình
> Chart so sánh entry: đánh dấu IFVG với đường 50% CE là nơi đặt limit đúng chuẩn; đối chiếu một điểm entry SAI (vào market ngay tại nến MSS, ký hiệu X đỏ) với điểm entry ĐÚNG (chờ retrace về CE, ký hiệu check xanh).

> [!example] Mẫu ghi nhanh — 07:00 IFVG (Bearish)
> ```text
> DOL: London H = [level], London L = [level]
> (1) Sau 07:00: giá hồi vào range, hunt relative equal highs @ [level]
> (2) MSS: đóng dưới [swing low] + displacement xuống
> (3) IFVG = FVG đầu tiên TRƯỚC hunt: [low]-[high], CE = [mid]
> (4) Entry SELL @ 50% CE [mid] (breaker dự phòng nếu không có IFVG)
> (5) Stop trên swing high post-07:00 @ [level]
> (6) Fib: 0=[swing high] → 1=[open 07:00]; T1 = -2, T2 = -2.5
> Macro: 07:00 / 08:50 / 09:50 | Lưu ý 30': counter-move đầu giờ
> Invalid: đóng nến trên swing high post-07:00
> ```

---

## 7. Lưu ý 30 phút đầu — kỳ vọng move NGƯỢC

![[AM0700IFVG-Advanced-30min-Reversal.svg|697]]
> [!info] Mô tả hình
> Chart minh họa: 30 phút đầu sau mốc giờ giá đi counter-move (ngược bias, tô cam) và hunt relative equal lows/highs đối diện; sau đó move thật (tô xanh) mới bắt đầu theo đúng bias — nhấn mạnh bẫy vào sớm trong khung 30 phút đầu.

**Sau 07:00, 08:00 và 09:00, trong 30 phút đầu (pre-session range), giá thường đi NGƯỢC** với relative trend / relative equal H/L. Ví dụ: bias bullish nhưng 30 phút đầu giá đi bearish để hunt thanh khoản trước khi đảo. Đây là cảnh báo counter-move **có sẵn trong khung Lecture 2** — quên nó = vào ngược move thật.

> [!warning] Đây là "bộ lọc kiên nhẫn" của model
> Nhiều lệnh thua đến từ việc vào ngay khi thấy giá đi *đúng* bias trong 5–10 phút đầu — nhưng đó thường là counter-move sắp bị đảo. Hãy để 30 phút đầu **lộ ra cú hunt** (thường ngược bias), *sau đó* mới tìm MSS + IFVG theo hướng thật.

---

## 8. 07:00 IFVG so với 08:30 NY — chọn model nào?

![[AM0700IFVG-vs-0830.svg|697]]
> [!info] Mô tả hình
> Sơ đồ hai cột song song so sánh 07:00 IFVG (Lecture 2) và 08:30 NY (Lecture 1): DOL, trigger giờ, vùng entry, target — mỗi cột 4 khối tương ứng để nhìn nhanh sự khác biệt giữa hai model cùng họ ICT 2024.

Hai model cùng họ ICT 2024, cùng trình tự hunt → MSS, nhưng khác ở **vùng entry chính xác** và **cách định target**.

| Khía cạnh | 07:00 IFVG (Lecture 2) | 08:30 NY (Lecture 1) |
|---|---|---|
| DOL tham chiếu | Đỉnh/đáy **London** (giá hồi về range) | Từ **bias 15m** (BSL/SSL) |
| Trigger | 07:00 / 08:00 / 09:00 | Sau **08:30** (giờ tin Mỹ) |
| Vùng entry | **50% CE của IFVG** (breaker dự phòng) | PD array **đầu tiên** bất kỳ (OB/FVG/breaker) |
| Target | Next DOL hoặc **Fib -2 / -2.5** | Draw on liquidity kế (cấu trúc) |
| Điểm mạnh | Entry precision, target đo được | Linh hoạt PD array, đơn giản |
| Khi nào ưu tiên | Muốn precision cao, có IFVG rõ | Ngày có tin 08:30, PD array rõ |

> [!tip] Khi hai model hội tụ
> Nếu IFVG **trùng breaker** (chồng lấn) → thực chất là một [[07 - Unicorn Model|Unicorn]], chất lượng **A+**. Và nếu setup 07:00 chưa hoàn tất, một setup [[08 - 08 30 AM NY Model|08:30]] có thể "nối tiếp" cùng hướng ngay sau đó — nhiều ngày cho cả hai cơ hội.

---

## 9. Ví dụ chart

### Ví dụ đúng
![[AM0700IFVG-Example-Correct.svg|697]]
> [!info] Mô tả hình
> Chart đầy đủ 6 bước: (1) range London làm DOL, (2) hunt relative equal highs sau 07:00, (3) MSS xuống phá swing low, (4) IFVG = FVG đầu tiên trước hunt với 50% CE là điểm SELL, (5) stop trên swing high post-07:00, (6) hai mức Fib -2/-2.5 làm target chốt bậc thang.

**Mô tả:** dùng London H/L làm DOL; hunt relative equal highs sau 07:00; MSS; đánh dấu IFVG (FVG đầu tiên); vào 50% CE; chốt Fib -2/-2.5.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp NQ/NAS100: đánh dấu (1) đỉnh/đáy London, (2) cú hunt sau 07:00, (3) MSS, (4) IFVG = FVG đầu tiên trước hunt + mức 50% CE khớp lệnh, (5) stop ngoài swing post-07:00, (6) Fib -2/-2.5. Ghi giờ ET.*

### Ví dụ sai / dễ nhầm
![[AM0700IFVG-Example-Wrong.svg|697]]
> [!info] Mô tả hình
> Chart minh họa lỗi: entry market ngay tại nến MSS (đánh dấu X đỏ), FVG được khoanh sai (đã nằm trong chân displacement, quá muộn) trong khi IFVG thật (nằm trước cú hunt) bị bỏ qua; giá sau đó retest đúng IFVG thật ở mức cao hơn, quét stop của entry sớm.

**Bài học:** các lỗi này được ICT nêu trực tiếp trong Lecture 2 — xem mục 11.

> [!note] Ảnh chart thực tế (dán screenshot của bạn)
> ![[paste-image-here.png]]
> *Chụp một lần bạn đánh dấu sai IFVG (không phải FVG đầu tiên) hoặc vào ngược trong 30' đầu — đánh dấu vì sao. Tư liệu quý cho review.*

---

## Phản biện & Giới hạn của mô hình

> [!warning] Đọc trước khi tin mô hình 100%
> Phần này không phủ nhận model — nó đặt model vào đúng vị thế: **một heuristic có edge thống kê khi dùng đúng ngữ cảnh**, không phải "quy luật thị trường" được chứng minh. Mục tiêu là giúp bạn tự kiểm định thay vì tin theo uy tín người dạy.

### A. Vấn đề nhận thức luận (epistemic issues)

**"Smart money"/IPDA là narrative không thể kiểm chứng trực tiếp.** ICT diễn giải hành vi giá là do một "thuật toán ngân hàng" (IPDA) chủ đích săn thanh khoản rồi đảo chiều. Đây là một mô hình giải thích — không phải sự kiện quan sát được. Không ai truy được lệnh của ngân hàng trung ương hay tổ chức tại từng nến M1 để xác nhận "IPDA đang chạy". Điều quan sát được thực sự chỉ là: **giá thường quét qua các mức thanh khoản rõ (equal highs/lows) rồi đảo chiều trong khung giờ mở phiên**. Cơ chế nhân quả phía sau ("ai" gây ra, "vì sao" đúng lúc đó) vẫn là suy luận, không phải bằng chứng.

**Các lời giải thích thay thế cùng tương thích với dữ liệu quan sát:**
- **Auction Market Theory (Market Profile):** giá dao động quanh vùng "value area", việc chạm ra ngoài range rồi quay lại là hành vi tự nhiên của một thị trường đấu giá hai chiều tìm điểm cân bằng cung-cầu, không cần giả định có "thuật toán săn thanh khoản" chủ đích.
- **Mean-reversion quanh tin tức/mở phiên:** phiên London/NY mở ra biến động cao rồi co lại là hiện tượng volatility clustering đã được ghi nhận rộng rãi trong tài chính định lượng (GARCH-type), không đặc thù cho ICT.
- **Tính tự ứng nghiệm do đông người theo cùng model:** nếu đủ nhiều trader retail cùng đặt SL/TP tại các mức "equal highs/lows" và cùng chờ "IFVG 50% CE" sau 07:00, chính hành vi tập thể này có thể tạo ra một phần chuyển động khớp với mô hình — không cần có "thuật toán ngân hàng" nào cả. Model có thể đúng một phần **vì nó phổ biến**, không phải vì nó phản ánh đúng cơ chế thị trường nguyên bản.

Không có cách nào phân biệt dứt điểm giữa ba lời giải thích trên và narrative IPDA chỉ bằng cách nhìn chart — cả bốn đều dự đoán ra hành vi giá tương tự trong nhiều trường hợp.

### B. Rủi ro thống kê khi backtest mô hình này

- **Hindsight bias khi chọn IFVG "đúng":** sau khi biết kết quả, việc chỉ ra đâu là "FVG đầu tiên trước hunt" luôn dễ hơn nhiều so với việc xác định real-time — đặc biệt khi có nhiều FVG chồng lấn trong 10-15 phút đầu. Case study minh họa (kể cả trong chính tài liệu này) được chọn *sau khi* biết giá đi đâu.
- **Degrees of freedom / overfitting quy tắc phụ:** model có nhiều tham số ẩn có thể "vặn" để khớp quá khứ — chọn M1 hay M5 để xác nhận MSS, chọn 30 hay 45 phút cho "counter-move window", chọn body-close hay wick để tính inversion, chọn Fib -2 hay -1.5 làm target đầu. Mỗi lựa chọn là một bậc tự do; với đủ bậc tự do, gần như mọi lịch sử giá có thể được "diễn giải" thành công.
- **Mẫu nhỏ, không đại diện:** hầu hết trader (bao gồm tài liệu này) minh họa model qua vài chục case quan sát thủ công, không phải hàng trăm/nghìn phiên đếm tự động — sai số chuẩn của winrate ước lượng từ mẫu <50 là rất lớn, đủ để một "70% winrate" quan sát được chỉ là nhiễu thống kê ở mức tin cậy thông thường.
- **Survivorship/selection bias của case chia sẻ:** case được đăng công khai (trong blog, X, hay tài liệu học) gần như luôn là case đẹp — win rõ ràng hoặc loss "dạy được bài học sạch". Các phiên nhiễu, không rõ ràng, hoặc chart xấu xí thường bị loại khỏi tư liệu chia sẻ, khiến người học đánh giá quá cao tần suất setup "sách giáo khoa".

### C. Điều kiện thị trường phá vỡ mô hình

- **Volatility rất thấp** (ví dụ giữa tuần lễ nghỉ, thị trường mùa hè thấp thanh khoản): không có đủ energy để tạo displacement rõ sau hunt → MSS mù mờ, IFVG không phản ứng, tín hiệu giả tăng mạnh.
- **News-driven day** (NFP, FOMC, CPI): giá bị chi phối bởi một cú spike tin tức chứ không phải cấu trúc IPDA nội tại của phiên — 07:00 hunt có thể chỉ là nhiễu trước khi tin ra lúc 08:30 xóa sạch toàn bộ cấu trúc.
- **Trend ngày cực mạnh (trending day) không có "range" để hunt:** nếu Asia + London đã đi một chiều dứt khoát, thị trường không tạo relative equal H/L đối xứng cho "hunt" — model cần một range/equilibrium tồn tại trước, thiếu điều kiện này thì cấu trúc "hunt → MSS → IFVG" không thành hình đúng nghĩa.
- **Chuyển đổi giờ mùa DST không đồng bộ (Mỹ đổi giờ sớm/muộn hơn châu Âu 1-3 tuần mỗi năm):** trong khoảng đó, "07:00 NY" không còn cùng pha với London mà thị trường quen phản ứng, làm mốc giờ lệch thực tế so với kỳ vọng behavior.

### D. Phương pháp tự kiểm định khách quan (khuyến nghị)

1. **Pre-registration quy tắc trước khi xem dữ liệu mới:** viết checklist "thế nào là IFVG hợp lệ, entry hợp lệ" ra văn bản cố định trước khi backtest phiên tiếp theo — tránh việc âm thầm chỉnh quy tắc theo kết quả (data snooping).
2. **Forward test thay vì chỉ backtest:** dữ liệu quá khứ luôn có thể bị diễn giải có lợi; chỉ số liệu thu thập *sau* khi quy tắc đã cố định (forward, chưa biết kết quả) mới có giá trị kiểm định thật.
3. **Đếm cả setup KHÔNG vào (missed setup) và False signal, không chỉ đếm trade đã vào:** nếu chỉ log các lệnh đã đặt, bạn bỏ sót toàn bộ các trường hợp IFVG hình thành nhưng không dẫn tới move — làm winrate quan sát bị lệch lạc quan (chỉ đếm "khi nó work").
4. **Walk-forward theo từng chu kỳ (rolling window), không tối ưu 1 lần trên toàn bộ lịch sử:** chia dữ liệu thành nhiều đoạn, kiểm tra quy tắc có ổn định qua các đoạn hay chỉ đúng vì fit cho một giai đoạn cụ thể.
5. **Cỡ mẫu tối thiểu ≥100 lần lặp trên mỗi regime thị trường** (trend/range, volatility cao/thấp) trước khi tin vào một winrate cụ thể — dưới ngưỡng này, kết luận "model work" hay "model không work" đều chưa đủ ý nghĩa thống kê để hành động (xem thêm phần loss-streak binomial ở Chuyên sâu B).

### E. Phản biện đặc thù cho 07:00 IFVG (không áp dụng chung cho mọi ICT model)

> [!info] Mô tả hình
> Sơ đồ 4 cột đối chiếu: (1) 07:00 là quy ước con người vs London/NY session thật không có ranh giới cứng, (2) IFVG winrate cao/thấp theo volatility, (3) inversion thật (body-close + retest) vs wick-only (không phải inversion), (4) DST làm 07:00 NY trôi so với London 1 giờ trong 2-4 tuần/năm.
![[AM0700IFVG-Advanced-ModelCritique.svg|720]]

- **"07:00 NY" là mốc quy ước, không phải ranh giới vật lý của thị trường.** ICT chọn 07:00 vì đây là giờ nhiều bàn giao dịch London-New York overlap bắt đầu hoạt động mạnh trên forex — nhưng **hợp đồng futures chỉ số Mỹ (ES, NQ) có pre-market riêng, thanh khoản pre-market thấp hơn RTH (regular trading hours, mở 09:30) rất nhiều**. Một "hunt 07:00" trên NQ pre-market có thể chỉ là biến động do thanh khoản mỏng (dễ bị vài lệnh lớn đẩy giá), khác bản chất với "hunt" trên EURUSD lúc 07:00 — nơi thanh khoản London-NY overlap thật sự sâu. Áp cùng một logic "IPDA hunt" cho cả hai loại thị trường là đánh đồng hai cơ chế vi cấu trúc khác nhau.
- **IFVG có tỷ lệ tín hiệu giả (false signal) tăng mạnh khi volatility thấp.** Về bản chất IFVG cần một cú đảo chiều đủ mạnh (displacement) để "xuyên" FVG cũ và đảo vai — nếu ATR/range ngày đang co hẹp (ví dụ giữa tuần hè, trước kỳ nghỉ lớn), MSS thường chỉ đóng xuyên FVG một chút rồi giá đi ngang, IFVG không có "sức nặng" thật, phản ứng tại 50% CE trở nên ngẫu nhiên hơn hẳn so với ngày biến động chuẩn.
- **Phân biệt "inversion thật" và wick xuyên giả:** một FVG chỉ nên được coi là đã "đảo vai" (inverted) khi có **nến đóng (body close)** vượt qua toàn bộ vùng FVG, sau đó có ít nhất một lần **retest xác nhận vùng đó phản ứng theo vai trò mới**. Nếu giá chỉ **wick xuyên qua rồi đóng cửa lại bên trong/trước FVG**, đây **không phải inversion hợp lệ** — nhiều trader mới nhầm "chạm qua" với "đảo vai", dẫn tới đặt IFVG sai vị trí và entry tại vùng chưa từng được xác nhận đảo.
- **DST (Daylight Saving Time) làm lệch pha 07:00 NY so với London.** Mỹ và châu Âu đổi giờ vào các ngày khác nhau (thường lệch 1-3 tuần mỗi mùa xuân/thu) — trong giai đoạn lệch đó, "07:00 NY" tương ứng với 12:00 London (giờ mùa đông) hoặc 11:00 London (giờ mùa hè) tùy giai đoạn, thay vì mốc quen thuộc. Hành vi phiên London-NY overlap mà model dựa vào có thể chưa/đã dịch pha, khiến "hunt 07:00" trong 1-2 tuần chuyển giao DST kém tin cậy hơn phần còn lại của năm — nên **giảm size hoặc bỏ qua model trong tuần chuyển đổi DST của Mỹ và Anh (thường không cùng ngày)**.

---

## Chuyên sâu A — Edge cases & Failure modes (thực chiến 07:00 IFVG)

![[AM0700IFVG-Advanced-EdgeCase-Matrix.svg|720]]
> [!info] Mô tả hình
> Ma trận 6 ô (3x2) mỗi ô một edge case: sai IFVG, vào ngược 30', front-run, sai breaker, wick tin XAU, chốt hết tại -2 — tên ngắn + mô tả 2 dòng mỗi ô.

Model 07:00 IFVG rất "sạch" trên lý thuyết, nhưng phần lớn lệnh thua không đến từ việc *chưa hiểu* mô hình — mà từ sáu tình huống rìa (edge case) lặp đi lặp lại khi vào thị trường thật. Dưới đây là sáu failure mode, mỗi cái theo trục **dấu hiệu → cơ chế → xử lý**. Hãy đọc chúng như một danh sách `missing_step` để kiểm lại sau mỗi lệnh.

**① Đánh dấu sai IFVG (không phải FVG ĐẦU TIÊN ngay trước hunt).**
- *Dấu hiệu:* bạn khoanh một FVG nằm *sau* cú hunt (đã trong chân displacement) hoặc một FVG quá xa phía trước làm IFVG.
- *Cơ chế:* chỉ **FVG đầu tiên ngay trước stop-hunt** mới là dấu vết cuối cùng của dòng lệnh sai hướng; các FVG khác không tập trung lệnh mắc kẹt nên phản ứng tại [[10-Consequent-Encroachment-Mean-Threshold|50% CE]] yếu và trễ.
- *Xử lý:* luôn quay ngược từ cú hunt và chọn **FVG liền kề trước nó** — nếu phân vân giữa hai FVG, chọn cái sát cú hunt hơn.

**② Vào ngược trong 30′ đầu (counter-move của lưu ý 30 phút).**
- *Dấu hiệu:* ngay sau 07:00 giá đi "đúng bias" 5–10 phút, bạn vào luôn vì sợ lỡ.
- *Cơ chế:* 30 phút đầu sau 07:00/08:00/09:00 thường là **counter-move để hunt thanh khoản trước** — move bạn thấy chính là cái sắp bị đảo.
- *Xử lý:* để 30 phút đầu **lộ ra cú hunt** (thường ngược bias), rồi *mới* tìm [[21-Market-Structure-Shift|MSS]] + IFVG theo hướng thật.

**③ Front-run trước cú hunt / pre-position.**
- *Dấu hiệu:* đặt lệnh khi chưa có sweep nào, chỉ vì "cấu trúc trông giống".
- *Cơ chế:* không có sweep = **không có trigger**; bạn đang đoán DOL thay vì phản ứng với dấu vết dòng lệnh.
- *Xử lý:* coi **cú sweep relative equal post-07:00 là điều kiện cần** — chưa hunt thì chưa có setup, dù chart đẹp đến đâu.

**④ Không có IFVG sạch → dùng breaker dự phòng nhưng chọn SAI breaker.**
- *Dấu hiệu:* không có FVG "đầu tiên trước hunt" rõ, bạn chuyển sang breaker nhưng khoanh nhầm một nến bất kỳ trong swing.
- *Cơ chế:* breaker chuẩn là **nến cuối cùng** (order block thất bại) ngay trước khi cấu trúc bị phá; chọn nến khác cho vùng entry lệch.
- *Xử lý:* xác định đúng **nến cuối trước displacement**; nếu breaker cũng mờ → về ④ nghĩa là **no-trade**, đừng cố ép.

**⑤ XAU quanh tin: wick dài quét stop dù hướng cuối đúng.**
- *Dấu hiệu:* hướng phân tích đúng nhưng một wick biến động tin xuyên qua stop rồi giá mới đi.
- *Cơ chế:* quanh tin (08:30) XAU giãn biên độ bất thường; stop siết vào pivot MSS bị "gánh" bởi nhiễu.
- *Xử lý:* **nới stop ra ngoài toàn bộ swing post-07:00** và **giảm size** để rủi ro tiền không đổi; hoặc tránh XAU sát giờ tin.

**⑥ Chốt hết tại -2 → bỏ lỡ phần lớn move (sai cách chốt bậc thang).**
- *Dấu hiệu:* đóng 100% vị thế ngay khi chạm -2.
- *Cơ chế:* phân bố kỳ vọng của model kéo tới **-2.5**; đóng hết ở -2 cắt cụt phần đuôi lời lớn nhất.
- *Xử lý:* **chốt bậc thang** — một phần tại -2 (dời stop về BE), phần còn lại tại -2.5; backtest riêng tỉ lệ đạt -2 vs -2.5 để chỉnh phân bổ.

**⑦ IFVG bị re-invert lần hai (double inversion) — IFVG "gãy" ngược trở lại FVG gốc.**
- *Dấu hiệu:* bạn vào lệnh tại 50% CE của IFVG theo đúng chuẩn, nhưng sau một nhịp phản ứng ngắn, giá **đóng nến xuyên ngược lại qua toàn bộ IFVG** — tức FVG quay lại vai trò gốc (support/resistance ban đầu) lần thứ hai.
- *Cơ chế:* thị trường không phải lúc nào chỉ đảo vai một lần; khi dòng lệnh phía sau cú MSS đầu cũng yếu (không đủ lực), một cú hunt/MSS thứ hai theo hướng ngược lại có thể "giải phóng" lại IFVG về trạng thái FVG ban đầu. Về bản chất đây là dấu hiệu **cả hai phía đều đang có lệnh mắc kẹt cạnh nhau** — thị trường sạc lại (recharge) trước khi chọn hướng thật.
- *Xử lý:* coi lần inversion thứ hai là **tín hiệu hủy bỏ giả thuyết ban đầu**, không phải "thêm cơ hội vào giá tốt hơn". Thoát vị thế hoặc siết SL về BE ngay khi có nến đóng xuyên ngược; không gồng chờ IFVG "trở lại". Ghi `missing_step: reinvert` nếu bạn từng gồng qua tình huống này.
- *Bài học:* một IFVG chỉ nên được tin **một lần phản ứng** — nếu nó "vỡ" theo chiều ngược, đó là dữ liệu mới, không phải nhiễu để bỏ qua.

**⑧ 07:00 sweep xảy ra nhưng displacement thật chỉ xuất hiện sau tin 08:30.**
- *Dấu hiệu:* cú hunt relative equal đúng giờ 07:00, nhưng MSS chỉ mờ, giá đi ngang/rung lắc, và displacement rõ chỉ bùng ra sau khi tin 08:30 (NFP/CPI/retail sales) được công bố.
- *Cơ chế:* cú hunt 07:00 là thật (dấu vết dòng lệnh sai hướng có tồn tại), nhưng "chất xúc tác" khiến MSS đủ mạnh để tạo IFVG đáng tin lại đến từ catalyst tin tức của giờ sau — hai cấu trúc (07:00 IFVG và 08:30 NY model) đang **chồng lấn theo thời gian** chứ không tách biệt độc lập như hai model riêng ở mục 8.
- *Xử lý:* nếu 07:00-07:30 chỉ có hunt mà MSS yếu, **đừng hủy giả thuyết** — giữ nguyên vùng IFVG tạm đã khoanh, chờ xem 08:30 có "hoàn thiện" displacement không. Nếu có, entry tại 50% CE vẫn hợp lệ nhưng hiểu đây là setup lai (hybrid) giữa hai model, không phải 07:00 IFVG "sạch".
- *Bài học:* đừng ép khung giờ cứng nhắc; cấu trúc `hunt → MSS → IFVG` có thể kéo dài qua nhiều mốc giờ liền kề, và tin tức 08:30 thường là "người hoàn thiện" cho displacement mà 07:00 mới chỉ khởi động.

**⑨ IFVG trên M1 và M5 mâu thuẫn nhau (đa khung mất đồng bộ).**
- *Dấu hiệu:* trên M5 bạn thấy một IFVG rõ ràng đã hình thành và giá đang tiến về 50% CE; nhưng khi zoom vào M1, cấu trúc MSS lại cho thấy một IFVG khác — ở vị trí giá lệch, có khi ngược hướng.
- *Cơ chế:* MSS trên M1 nhạy hơn nhiều (nhiễu cao hơn) so với M5 — một cú "phá cấu trúc" trên M1 có thể chỉ là nhiễu nội bộ của nhịp M5 lớn hơn, chưa đủ để tính là MSS thật ở khung thời gian bạn dùng làm chuẩn.
- *Xử lý:* **chọn một khung làm chuẩn trước khi vào lệnh** (khuyến nghị M5 làm khung xác nhận MSS/IFVG, M1 chỉ dùng để tinh chỉnh entry tại vùng CE đã xác định trên M5) — không nhảy qua nhảy lại giữa hai khung để "tìm" cấu trúc ủng hộ ý muốn chủ quan.
- *Bài học:* mâu thuẫn đa khung không có nghĩa "cả hai đều đúng cùng lúc" — nó có nghĩa bạn cần phân cấp khung: khung lớn quyết định bias & vùng, khung nhỏ chỉ tinh chỉnh điểm vào, không được đảo ngược vai trò.

**⑩ Ngày không có 7AM raid vì Asia đã trend mạnh trước đó (không có range để hunt).**
- *Dấu hiệu:* phiên Asia đi một chiều dứt khoát (không dao động quanh vùng cân bằng), khiến tới 07:00 NY thị trường không hề có "relative equal highs/lows" sạch để hunt — giá chỉ tiếp tục trôi theo trend.
- *Cơ chế:* model 07:00 IFVG giả định có một **range/equilibrium tồn tại từ trước** để tạo ra hai phía thanh khoản đối xứng (equal highs và equal lows) làm "món mồi". Khi Asia đã trend áp đảo, không có cấu trúc range đối xứng này, nên không tồn tại "cú hunt" đúng nghĩa — chỉ có tiếp diễn trend.
- *Xử lý:* trước 07:00, luôn kiểm tra: *Asia session có tạo được range rõ (đỉnh & đáy cách nhau hợp lý, giá dao động qua lại) hay chỉ đi một chiều?* Nếu là trend ngày, chuyển hẳn sang logic "continuation" (chờ pullback theo trend, không chờ hunt-reversal) hoặc đứng ngoài model này.
- *Bài học:* 07:00 IFVG là model **đảo chiều sau hunt** — nó cần một range để "săn" hai phía. Ép áp dụng nó vào một ngày trend thuần là nhầm công cụ cho đúng việc.

**⑪ Spread giãn bất thường tại đúng khung giờ entry (07:00 hoặc rollover 17:00 NY) ăn hết R:R.**
- *Dấu hiệu:* tính toán R:R trên chart đẹp, nhưng khi đặt lệnh thật, spread/slippage tại đúng phút 07:00 (broker forex) hoặc quanh giờ rollover 17:00 NY giãn rộng bất thường so với giờ bình thường trong phiên.
- *Cơ chế:* nhiều broker retail forex tăng spread hoặc giảm thanh khoản matching tại các mốc chuyển phiên/rollover; nến 07:00 trên chart (giá giữa - mid price) không phản ánh giá thực thi (ask/bid) bạn nhận được.
- *Xử lý:* backtest R:R cần **trừ hao spread trung bình thực tế đo được tại đúng khung giờ đó** (không dùng spread trung bình cả ngày); nếu R:R dự kiến sát biên (ví dụ 1:1.2), spread giãn tại 07:00 có thể ăn hết edge thống kê. Ưu tiên broker/loại tài khoản có spread ổn định quanh mốc giờ này, hoặc chờ 1-2 phút sau 07:00 đúng để spread bình thường hóa trước khi đặt limit.
- *Bài học:* edge trên chart lý thuyết và edge sau chi phí thực thi tại đúng khung giờ nhạy cảm là hai con số khác nhau — đừng nhầm cái đầu là kết quả cuối.

**⑫ FVG chỉ bị chạm mép (partial wick fill), giá không vào tới 50% CE rồi đi luôn.**
- *Dấu hiệu:* sau MSS, giá quay lại chạm đúng mép ngoài của IFVG (ví dụ 10-20% vùng) nhưng không tới được 50% CE, rồi bật đi theo hướng dự đoán mà không lấp đầy lệnh limit đặt tại CE.
- *Cơ chế:* mức lấp đầy (fill) một FVG/IFVG không cố định ở 50% trong mọi trường hợp — biến động cao và dòng lệnh mạnh có thể chỉ cần "chạm nhẹ" vùng mất cân bằng để giải quyết đủ lệnh mắc kẹt, không cần lấp tới điểm giữa lý thuyết.
- *Xử lý:* nếu muốn tăng tỷ lệ khớp, có thể chia limit thành hai mức (ví dụ 20-30% vùng và 50% CE) với size nhỏ hơn ở mức nông — đánh đổi tỷ lệ khớp cao hơn với R:R thấp hơn một chút. Ghi rõ trong journal đây là biến thể entry, không phải lỗi "chờ sai".
- *Bài học:* 50% CE là điểm kỳ vọng trung tâm hợp lý để chuẩn hóa, không phải luật vật lý — trong biến động cao, chấp nhận việc nhiều setup đẹp sẽ "bay mất" vì giá không lấp đủ sâu là một phần chi phí cơ hội của việc chờ giá tốt.

> [!note] Nguyên tắc xuyên suốt
> Mười hai edge case trên đều quy về **một kỷ luật**: chỉ hành động khi có *dấu vết dòng lệnh thật* (hunt → MSS → IFVG đầu tiên → 50% CE) và **tôn trọng 30 phút đầu**. Mỗi lần thua, gán đúng `missing_step` (`prehunt`/`ifvg`/`mss`/`30min`/`ce`/`target`/`stop`/`reinvert`/`htf-conflict`/`no-range`/`spread`/`fill`) — sửa quy trình quan trọng hơn sửa từng lệnh.

---

## Chuyên sâu B — Kinh nghiệm live/backtest thực chiến

![[AM0700IFVG-Advanced-Experience.svg|720]]
> [!info] Mô tả hình
> Danh sách 7 dòng tóm tắt các kinh nghiệm live/backtest chính: London H/L làm mốc, chờ 30' lộ hunt, IFVG đầu tiên là dấu vết dòng lệnh sai hướng cuối, khác biệt theo market, stop ngoài toàn bộ swing, chốt bậc thang, kỷ luật missing_step + cỡ mẫu.

Những bài học dưới đây chắt ra từ việc chạy model qua nhiều phiên live và backtest — chúng bổ sung *cảm giác thực chiến* cho khung lý thuyết ở các mục trên.

1. **London H/L là mốc DUY NHẤT cần chuẩn bị trước 07:00.** Đừng nạp thêm bias rối; chỉ cần đỉnh/đáy phiên London làm draw on liquidity rồi để giá tự kể chuyện.
2. **Để 30′ đầu lộ cú hunt rồi mới tìm MSS + IFVG.** Kiên nhẫn ở đây *chính là bộ lọc* — phần lớn lệnh thua sinh ra trong 30 phút đầu vì vào theo counter-move.
3. **IFVG đầu tiên là dấu vết dòng lệnh sai hướng cuối cùng — nên nhạy nhất.** Khi bị đóng xuyên rồi test lại, đây là vùng "phải được giải quyết"; vào [[17-Inverse-Fair-Value-Gap-iFVG|IFVG]] tại 50% CE cho phản ứng dứt khoát nhất.
4. **Khác biệt theo market.** NQ1 cho hunt + IFVG *sạch nhất*; EURUSD/GBPUSD hồi về range London rất rõ (hợp model); XAU *thất thường quanh tin* — dễ dính edge case ⑤.
5. **Stop ra ngoài TOÀN BỘ swing post-07:00**, không siết vào pivot MSS. Wick quét stop rồi đi đúng hướng là kiểu thua gây ức chế và hoàn toàn tránh được.
6. **Chốt bậc thang: -2 (dời BE) rồi -2.5.** Backtest **riêng** tỉ lệ đạt -2 vs -2.5 theo từng market để biết nên chốt bao nhiêu % ở mỗi bậc — đừng dùng một tỉ lệ cho mọi thị trường.
7. **Kỷ luật `missing_step` là công cụ tiến bộ.** Mỗi lệnh thua/BE gán một trong các nhãn ở mục Chuyên sâu A; cuối tuần thống kê tại [[07 - Reviews]] — giá trị nào >40% lệnh thua là ưu tiên sửa. **Gom ≥30 mẫu** trước khi nghĩ đến tăng size.

### Những điều ít người nói ra khi backtest/live model này

8. **Spread/slippage thực tế tại đúng khung giờ entry luôn xấu hơn bạn nghĩ khi backtest trên chart mid-price.** Backtest thường dùng giá đóng nến (mid) để giả định fill tại đúng 50% CE — thực tế lúc đặt limit/market quanh 07:00 hoặc 08:30, spread có thể giãn gấp 2-3 lần so với giữa phiên London yên tĩnh (xem edge case ⑪). Nếu bạn backtest ra R:R 1:2 nhưng chưa trừ hao spread đúng khung giờ, con số live thực tế thường tệ hơn 10-20% so với kỳ vọng trên giấy — đừng ngạc nhiên khi kết quả forward test kém hơn backtest, đó là hiện tượng bình thường, không phải bạn "làm sai gì đó".
9. **Demo, live cá nhân, và tài khoản funded (prop-firm) là ba trải nghiệm tâm lý khác nhau, dù chart giống nhau 100%.** Trên demo, không có gì cản bạn chờ đúng 50% CE; trên live cá nhân, sợ mất tiền khiến nhiều người vào sớm hơn CE vài pip "cho chắc"; trên tài khoản funded, **quy tắc drawdown hàng ngày/tổng** (ví dụ mất X% là bị khóa tài khoản) khiến trader thường siết SL chặt hơn kế hoạch gốc hoặc né hẳn setup vào cuối ngày drawdown gần chạm ngưỡng — cả hai hành vi này đều làm méo quy trình đã backtest, tạo ra kết quả live tệ hơn backtest dù "hiểu" model giống nhau.
10. **Tâm lý sau 2-3 lần thua liên tiếp là điểm rơi phổ biến nhất của việc phá vỡ kỷ luật.** Sau một chuỗi thua ngắn, phản ứng tự nhiên là: (a) doubt cả model — bỏ qua setup A+ tiếp theo dù đúng chuẩn, hoặc (b) revenge trade — vào setup không đủ điều kiện để "gỡ" nhanh. Cả hai đều không phải phản ứng dựa trên dữ liệu, mà là phản ứng cảm xúc trước một chuỗi ngắn hoàn toàn bình thường về mặt thống kê.
11. **Losing streak không có nghĩa model hỏng — nó tuân theo phân phối nhị thức (binomial) của chính winrate model.** Nếu model có winrate thật là 55%, xác suất gặp một chuỗi ≥4 lệnh thua liên tiếp trong 30 lệnh **không hề nhỏ** — với xác suất thua mỗi lệnh ≈45%, xác suất có *ít nhất một* chuỗi 4 thua liên tiếp trong 30 lệnh độc lập đã ở mức đáng kể (ước lượng bằng công thức chuỗi Markov/runs, không phải hiếm). Nói cách khác: **gặp 3-4 lệnh thua liên tiếp là hoàn toàn bình thường với một model có edge dương**, không phải dấu hiệu cần đổi chiến lược ngay. Việc cần làm là kiểm tra `missing_step` của từng lệnh thua trong chuỗi đó — nếu tất cả đều `none` (đúng quy trình), đó là biến động thống kê bình thường; nếu phần lớn có `missing_step` cụ thể, đó là lỗi thực thi, không phải lỗi model.
12. **Journaling phải ghi `missing_step` ngay cả cho lệnh WIN, không chỉ lệnh thua.** Một lệnh thắng nhưng vào sai quy trình (ví dụ vào tại MSS thay vì chờ CE, rồi vẫn ăn may) là "bad win" — nếu không ghi lại, bạn sẽ vô tình học sai bài học rằng "vào sớm cũng được", làm hỏng dữ liệu tự đánh giá dài hạn nghiêm trọng hơn một lệnh thua có kỷ luật.
13. **Setup A+ (đủ hunt sạch + MSS dứt khoát + IFVG đầu tiên rõ + retest đúng 50% CE) thực tế không xảy ra mỗi ngày.** Kỳ vọng thực tế qua backtest nhiều phiên: setup đạt đủ tiêu chuẩn A+ theo đúng nghĩa hẹp thường chỉ xuất hiện một số phiên trong tuần, không phải mọi ngày giao dịch — phần còn lại là no-trade đúng (Case 4, 7) hoặc setup B/C cần giảm size. Kỳ vọng "phải có lệnh mỗi sáng 07:00" là nguồn gốc của phần lớn việc ép setup không đủ điều kiện (edge case ③, ④).
14. **Chỉ tăng size sau khi có đủ cỡ mẫu cho ĐÚNG THỊ TRƯỜNG và ĐÚNG REGIME đang giao dịch — không tính chung tất cả lệnh.** Ví dụ: 30 lệnh NQ1 trong giai đoạn trend không đại diện cho hiệu suất model trên XAU quanh tin hay trên EURUSD giai đoạn range hẹp. Điều kiện hợp lý để tăng size: (a) ≥30-50 mẫu cùng market + cùng regime volatility, (b) tỷ lệ `missing_step: none` trong các lệnh thua ổn định qua thời gian (không phải một đợt May mắn ngắn), (c) đã trải qua ít nhất một losing streak "bình thường" (3-4 lệnh) mà không phá vỡ kỷ luật để xác nhận tâm lý đủ vững ở size hiện tại trước khi lên size mới.

> [!tip]
> Một câu để nhớ: *"Mốc London, chờ hunt sau 07:00, vào 50% CE của IFVG ĐẦU TIÊN, chốt bậc thang — và để dữ liệu `missing_step` dạy mình, đừng để cảm xúc."*

---

## Chuyên sâu C — Case studies mổ xẻ chuyên sâu (kịch bản minh họa)

> [!info] Về bảy ca dưới đây
> Đây là **kịch bản minh họa (hypothetical)**, dựng để luyện *đọc quy trình*, **không kèm P&L thật**. Ta chấm điểm **process** (đủ hunt + MSS + IFVG đầu tiên + 50% CE + tôn trọng 30′) chứ không chấm thắng/thua. Một "good loss" đúng quy trình vẫn quý hơn một "bad win".

### Case 1 — NQ1 Win (đúng chuẩn)

![[AM0700IFVG-Advanced-CaseStudy-Win.svg|720]]
> [!info] Mô tả hình
> Chart case Win: hunt relative equal highs → MSS xuống → IFVG (FVG đầu tiên trước hunt) với 50% CE → SELL đúng nhịp retest → giá chạy tiếp tới vùng chốt bậc thang -2/-2.5; ghi chú grade A, missing_step: none.

**Chuỗi:** dùng London H/L làm DOL; sau 07:00 giá hồi vào range rồi hunt **relative equal highs**; giá đóng dưới swing low tạo [[21-Market-Structure-Shift|MSS]] xuống kèm displacement; đánh dấu **IFVG = FVG đầu tiên ngay trước cú hunt**; chờ giá retest và vào **SELL tại 50% CE** ([[10-Consequent-Encroachment-Mean-Threshold|consequent encroachment]]) của IFVG; vẽ Fib từ swing post-07:00 về open 07:00, chốt **bậc thang -2 rồi -2.5**.
**Chẩn đoán:** đủ **hunt + MSS + IFVG**; entry đúng 50% CE (không vào lúc MSS); stop ngoài swing; chốt đúng bậc thang → `missing_step: none`.
**Bài học:** khi ba dấu vết (hunt → MSS → IFVG đầu tiên) hội tụ và entry nằm đúng CE, đây là kết cấu A của model — chỉ cần lặp lại kỷ luật này, không cần "sáng tạo".

### Case 2 — Loss (đánh dấu sai IFVG / vào lúc MSS)

![[AM0700IFVG-Advanced-CaseStudy-Loss.svg|720]]
> [!info] Mô tả hình
> Chart case Loss: entry SELL market ngay tại nến MSS (X đỏ) với FVG bị khoanh sai (muộn, trong chân displacement); IFVG thật (nằm trước cú hunt, tô mờ) bị bỏ qua; giá sau đó retest đúng IFVG thật ở mức cao hơn, quét stop entry sớm.

**Chuỗi (gãy):** giá hunt highs và bắt đầu MSS xuống; thay vì chờ, trader **vào SELL ngay tại nến MSS** và khoanh nhầm một FVG *muộn* (đã nằm trong chân displacement) làm IFVG. Giá sau đó **retest vùng IFVG THẬT cao hơn** rồi mới đi — entry sớm bị quét trước khi move thật diễn ra.
**Chẩn đoán:** `missing_step: ifvg` (sai IFVG) và `ce` (không chờ retest 50% CE của IFVG thật) — vào lúc MSS là biểu hiện điển hình.
**Bài học:** MSS chỉ là **xác nhận đảo chiều**, không phải điểm vào. Điểm vào là **50% CE của IFVG đầu tiên**; nếu chưa retest tới CE thì chưa có lệnh.

### Case 3 — Bẫy 30 phút đầu / ngược DOL (bối cảnh sai)

![[AM0700IFVG-Advanced-CaseStudy-Nested-Trap.svg|720]]
> [!info] Mô tả hình
> Chart case Nested-Trap: giá đi "đúng bias" trong 5-10 phút đầu (tô xanh) khiến trader vào sớm (X đỏ); ngay sau đó giá đảo mạnh và hunt relative equal đối diện, quét stop trước khi move thật bắt đầu.

**Chuỗi (gãy):** trong 30 phút đầu sau 07:00, giá đi "đúng bias" 5–10 phút; trader vào ngay. Nhưng đó là **counter-move**: giá đảo lại và hunt thanh khoản đối diện (relative equal highs) — đúng như **lưu ý 30 phút** cảnh báo — quét stop trước khi move thật bắt đầu.
**Chẩn đoán:** `missing_step: 30min` — vào trong cửa sổ counter-move, chưa để cú hunt thật lộ ra.
**Bài học:** 30 phút đầu là **bộ lọc kiên nhẫn** của model, không phải tín hiệu vào. Chờ hunt thật (thường ngược move đầu giờ) rồi mới tìm MSS + IFVG.

### Case 4 — No-Trade đúng (không hồi về range / không IFVG rõ)

![[AM0700IFVG-Advanced-CaseStudy-NoTrade.svg|720]]
> [!info] Mô tả hình
> Chart case No-Trade: giá lình xình dưới range London (DOL) suốt phiên, không hồi lên tới range, không in relative equal sạch, không hình thành IFVG rõ ràng — kết luận No-Trade đúng, bảo toàn vốn.

**Chuỗi:** sau 07:00 giá **KHÔNG hồi về range London**, lình xình dưới range, không in relative equal sạch, không có IFVG "đầu tiên trước hunt" rõ ràng. Trader **đứng ngoài**.
**Chẩn đoán:** thiếu trigger cốt lõi (hunt + MSS + IFVG/breaker) → **no-trade đúng**, bảo toàn vốn; đây không phải lỗi mà là kỷ luật.
**Bài học:** model chỉ tính là setup khi **đủ hunt + MSS + IFVG/breaker theo hướng DOL**. Không đủ điều kiện thì không có "setup yếu" — chỉ có no-trade. Đối chiếu [[08 - 08 30 AM NY Model]] nếu muốn cơ hội tiếp theo trong ngày.

### Case 5 — Double Inversion: vào đúng CE nhưng IFVG "gãy" ngược (Loss có kỷ luật)

> [!info] Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa.

![[AM0700IFVG-Advanced-CaseStudy-DoubleInversion.svg|720]]
> [!info] Mô tả hình
> Timeline: hunt → MSS → IFVG hình thành → entry SELL tại 50% CE đúng chuẩn → giá phản ứng ngắn theo hướng dự đoán → sau đó một nến đóng xuyên NGƯỢC lại toàn bộ IFVG (mũi tên cam ngược hướng) → SL tại BE bị chạm, không phải SL gốc.

**Bối cảnh HTF:** GBPUSD, phiên London đóng một range hẹp bất thường (thấp volatility so với trung bình 20 ngày) — dấu hiệu cảnh báo (xem Phản biện mục C) mà trader đã bỏ qua vì "cấu trúc trông vẫn chuẩn".

**Diễn biến từng bước:**
1. 07:04 — giá hunt relative equal highs của range London, đóng nến quét đỉnh.
2. 07:11 — displacement xuống đủ mạnh để MSS đóng xuyên FVG tăng trước đó → FVG đảo vai thành IFVG.
3. 07:18 — giá retest đúng 50% CE của IFVG; trader vào SELL, SL trên swing high post-07:00, TP theo Fib -2/-2.5 — tất cả đúng checklist.
4. 07:26 — giá đi đúng hướng khoảng 0.6R, trader dời SL về BE theo đúng kỷ luật "bậc thang".
5. 07:33 — một nến đóng ngược, xuyên toàn bộ vùng IFVG theo chiều lên (re-invert) — vùng vừa là kháng cự giờ lại có dấu hiệu trở lại support. SL tại BE bị chạm.

**Quyết định & lý do:** trader không gồng chờ IFVG "quay lại làm việc" — thoát tại BE ngay khi nến đóng xác nhận re-invert, đúng theo edge case ⑦.

**Kết quả (R):** 0R (breakeven, không lỗ thêm nhờ dời SL đúng lúc ở bước 4).

**Đúng/sai quy trình:** hoàn toàn đúng process ở giai đoạn vào lệnh (hunt → MSS → IFVG → CE); "lỗi" duy nhất là không kiểm tra volatility nền trước khi tin cấu trúc — đây là bài học bổ sung, không phải lỗi thực thi.

**Bài học → quy tắc:** trước khi vào lệnh tại 50% CE, so nhanh range 30 phút gần nhất với ATR trung bình; nếu thấp bất thường, giảm size 30-50% vì tỷ lệ double-inversion tăng trong điều kiện này (edge case ⑦ + phản biện mục C).

---

### Case 6 — 8:30 News hoàn thiện displacement mà 07:00 chỉ khởi động (Win, entry trễ có chủ đích)

> [!info] Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa.

![[AM0700IFVG-Advanced-CaseStudy-NewsCompletion.svg|720]]
> [!info] Mô tả hình
> Timeline hai giai đoạn: 07:00-07:30 hunt xảy ra nhưng MSS chỉ "mờ" (nến nhỏ, tô xám) → khoảng lặng đi ngang → 08:30 tin ra, nến displacement lớn (tô xanh đậm) hoàn thiện MSS thật → IFVG hình thành từ vùng FVG của giai đoạn 1 → entry tại 50% CE sau 08:30.

**Bối cảnh HTF:** chỉ số NQ1, ngày có lịch NFP 08:30. Asia và London đều đi trong range hẹp, không có bias rõ trước giờ Mỹ mở cửa.

**Diễn biến từng bước:**
1. 07:02 — giá hunt relative equal lows sạch của range London.
2. 07:06 — có một nến đóng hơi vượt qua FVG giảm trước đó nhưng biên độ rất nhỏ — MSS "kỹ thuật" xảy ra nhưng không đủ dứt khoát để tin tưởng hoàn toàn (đúng dấu hiệu edge case ⑧).
3. 07:10-08:25 — giá đi ngang hẹp, không retest rõ vùng IFVG tạm.
4. 08:30 — NFP công bố, một nến displacement lớn đóng xuyên sâu hơn nhiều qua đúng vùng FVG ban đầu — xác nhận MSS thật, IFVG giờ "chắc" hơn nhiều so với dấu hiệu yếu lúc 07:06.
5. 08:36 — giá retest 50% CE của IFVG (đã được xác nhận lại bởi displacement 08:30); trader vào theo hướng MSS, SL ngoài swing tổng hợp của cả hai giai đoạn.

**Quyết định & lý do:** trader không vào lúc 07:06 vì displacement yếu (đúng kỷ luật, tránh edge case ①/③); giữ nguyên vùng IFVG tạm đã khoanh và kiên nhẫn chờ xác nhận — khi 08:30 "hoàn thiện" cấu trúc, coi đây là setup lai hợp lệ theo edge case ⑧, không phải hai model tách biệt.

**Kết quả (R):** +2.3R, chốt bậc thang tại -2 và -2.5 theo Fib đo từ swing tổng hợp.

**Đúng/sai quy trình:** đúng — điểm mấu chốt là trader **không** tự ép mình phải có kết quả trước 08:00, biết chờ catalyst hoàn thiện cấu trúc.

**Bài học → quy tắc:** khi MSS lúc 07:00-07:30 chỉ mờ chứ không rõ, đừng hủy giả thuyết ngay — giữ vùng IFVG tạm và theo dõi tiếp qua mốc tin 08:30 nếu ngày đó có lịch kinh tế quan trọng; chỉ hủy hẳn nếu qua 09:00 vẫn không có xác nhận nào.

---

### Case 7 — Asia trend mạnh, không có 7AM raid: No-Trade đúng dù "nhìn giống setup"

> [!info] Case tái dựng từ pattern lặp lại trong backtest, số liệu minh họa.

![[AM0700IFVG-Advanced-CaseStudy-NoRangeNoTrade.svg|720]]
> [!info] Mô tả hình
> Chart: phiên Asia đi một chiều dốc liên tục (không có đỉnh/đáy đối xứng) → London tiếp tục cùng hướng, không tạo range mới → tới 07:00 không có relative equal highs/lows nào để hunt → nhãn "NO RANGE = NO HUNT = NO-TRADE" nổi bật.

**Bối cảnh HTF:** EURUSD, một ngày có tin vĩ mô châu Âu quan trọng công bố sớm giờ Á/Âu, khiến Asia và đầu London trend dứt khoát một chiều xuống, không dao động qua lại.

**Diễn biến từng bước:**
1. 00:00-06:55 — giá giảm liên tục qua Asia và đầu London, không hình thành đỉnh/đáy đối xứng nào — chỉ có các đáy thấp dần (lower lows) liên tiếp, không có "equal lows" hai lần chạm cùng mức.
2. 07:00 — giá tiếp tục giảm nhẹ, không có cú hunt/sweep rõ rệt lên phía trên; không có MSS đảo chiều nào xuất hiện.
3. 07:00-07:30 — trader quan sát thấy displacement giảm liên tục và cảm giác "giống MSS" nhưng nhận ra đây chỉ là tiếp diễn trend, không phải đảo chiều sau hunt.
4. 07:30 — trader kết luận: không có range để hunt = không có setup 07:00 IFVG hợp lệ, đứng ngoài.

**Quyết định & lý do:** đúng theo edge case ⑩ — thiếu điều kiện cần (range/equilibrium trước đó để tạo hai phía thanh khoản đối xứng); tiếp tục theo trend thuần không phải là "hunt", nên model này không áp dụng được cho cấu trúc ngày đó.

**Kết quả (R):** 0R — không có lệnh; vốn được bảo toàn, không mất cơ hội thật (không có setup 07:00 IFVG hợp lệ nào bị bỏ lỡ, chỉ có continuation trend không thuộc phạm vi model này).

**Đúng/sai quy trình:** đúng hoàn toàn — điểm mạnh của case này là khả năng **phân biệt trend thuần với cấu trúc hunt-reversal**, tránh việc gán nhãn "MSS" cho bất kỳ cú phá cấu trúc nào chỉ vì nó tồn tại.

**Bài học → quy tắc:** trước 07:00, luôn tự hỏi "Asia + đầu London có tạo được range hai chiều hay chỉ trend một hướng?" — nếu là trend thuần, chuyển hẳn tư duy sang continuation-only hoặc đứng ngoài; đừng cố tìm "MSS" trong một xu hướng chưa từng có range để đảo.

---

> [!summary] Bảy ca — một thông điệp
> Cả bảy ca cùng nói một điều: **kết quả không định nghĩa chất lượng lệnh — quy trình mới định nghĩa.** Case 1 & 6 thắng vì đủ hunt → MSS → IFVG đầu tiên → 50% CE (Case 6 còn cho thấy nên kiên nhẫn chờ catalyst hoàn thiện cấu trúc); Case 2, 3 & 5 có kết quả xấu hoặc BE vì cắt bớt quy trình hoặc gặp double-inversion (⑦) dù vào đúng CE; Case 4 & 7 "không lệnh" nhưng đúng nhất vì tôn trọng đúng điều kiện thiếu (không IFVG rõ / không có range để hunt). Ghi `missing_step` cho mọi ca không phải Win để biến từng phiên thành dữ liệu sửa quy trình.

---

## 10. Thực hành tốt nhất (Best Practices)

> [!summary]
> Thói quen chuẩn prop-firm cho model 07:00 IFVG — phân biệt trader vào đúng 50% CE của IFVG thật với trader "thấy FVG nào cũng vào". Mục tiêu: đánh dấu đúng IFVG, tôn trọng lưu ý 30', chốt bậc thang Fib, và không front-run.

> [!tip] Quy tắc 07:00 IFVG Model (5 điều cốt lõi)
> 1. **London H/L = DOL** — tham chiếu duy nhất cần từ trước 07:00.
> 2. **Không dự đoán** — chờ relative equal in ra, chờ hunt, chờ MSS.
> 3. **IFVG = FVG ĐẦU TIÊN trước hunt** — đánh dấu sai = entry kém nhạy.
> 4. **Vào 50% CE của IFVG** (breaker là dự phòng), không vào lúc MSS.
> 5. **Chốt bậc thang -2 / -2.5**, tôn trọng lưu ý 30 phút đầu.

### Quy trình pre-session (trước 07:00 NY)
1. Đánh dấu **đỉnh & đáy phiên London** (DOL) — chỉ cần bấy nhiêu nếu bạn còn mới.
2. Kiểm tra lịch tin: có tin 08:30 (CPI/NFP) ngày đó không → ảnh hưởng biến động cú hunt.
3. Viết sẵn kịch bản: "*Nếu* giá hồi về range rồi hunt relative equal highs → chờ MSS xuống → SELL 50% CE của IFVG đầu tiên; Fib -2/-2.5."
4. Đặt sẵn ngưỡng **no-trade**: không hồi về range / không có IFVG rõ / chưa qua 30' hunt → đứng ngoài.

### Kỷ luật `missing_step` — nghi thức review tuần
- Với mỗi lệnh 07:00 thua/BE, bắt buộc điền `missing_step`: `prehunt` (front-run, chưa có hunt), `ifvg` (đánh dấu sai IFVG), `mss` (vào khi chưa MSS), `30min` (vào ngược trong 30' đầu), `ce` (vào lệch 50% CE), `target` (chốt hết tại -2 hoặc sai Fib), `stop` (stop trong swing thay vì ngoài).
- Cuối tuần ([[07 - Reviews]]): giá trị nào >40% lệnh thua = ưu tiên sửa; gắn `[[Mistake - ...]]`.

### Kỳ vọng thực tế
- **Không phải ngày nào cũng có IFVG rõ.** Nếu không hình thành IFVG "đầu tiên trước hunt" sạch, dùng breaker dự phòng — hoặc bỏ qua. Chỉ tính là setup khi đủ **hunt + MSS + IFVG/breaker theo hướng DOL**.
- Lưu ý 30' đầu là bộ lọc: đừng sốt ruột vào ngay đầu giờ.

### Scale size chỉ sau khi có dữ liệu
- Tối thiểu **≥30 mẫu backtest** 07:00 IFVG (tag frontmatter đầy đủ) qua [[04 - Backtesting|_Backtest Dashboard]], rồi forward-test 15–20 lệnh trước khi về ≤0.5%/lệnh. Backtest riêng: tỉ lệ đạt -2 vs -2.5 để tinh chỉnh cách chốt bậc thang.

### Amateur vs Professional

| Khía cạnh | Amateur | Professional (chuẩn prop-firm) |
|---|---|---|
| Trước 07:00 | Đoán hướng, vào sớm | Chỉ đánh dấu London H/L, chờ |
| 30 phút đầu | Vào ngay khi giá đi "đúng bias" | Chờ counter-move hunt lộ ra |
| Đánh dấu IFVG | FVG nào cũng nhận | Chỉ FVG **đầu tiên** ngay trước hunt |
| Entry | Market lúc MSS | Limit tại 50% CE của IFVG |
| Chốt lời | Đóng hết tại -2 | Bậc thang -2 (BE) rồi -2.5 |
| Stop | Trong swing MSS | Ngoài toàn bộ swing post-07:00 |
| Sau lệnh thua | Trade gỡ | Ghi `missing_step`, chờ setup thật |

> [!tip]
> Tóm một câu: **"London H/L làm mốc, chờ hunt sau 07:00, vào 50% CE của IFVG ĐẦU TIÊN, chốt bậc thang Fib — tôn trọng 30' đầu."**

---

## 11. Lỗi thường gặp (theo Lecture 2)

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Pre-position trước 07:00 | Vào khi chưa có hunt | Đoán mò, không trigger | Cú sweep post-07:00 mới là trigger |
| Sai IFVG | Đánh dấu FVG sau/trước không đúng | Entry kém nhạy, phản ứng yếu | IFVG = FVG **đầu tiên** ngay trước hunt |
| Bỏ qua MSS | Vào bằng wick đơn thuần | Chưa xác nhận đảo chiều | MSS là bước xác nhận bắt buộc |
| Quên lưu ý 30 phút | Vào ngược move thật đầu giờ | Bị counter-move quét | Nhớ counter-move 30′ sau 07/08/09 |
| Stop quá chặt | Đặt tại pivot MSS | Bị wick quét vô lý | Stop ngoài toàn bộ swing post-07:00 |
| Chốt một phát | Đóng hết tại -2 | Bỏ lỡ phần lớn move | Chốt bậc thang -2 rồi -2.5 |

---

## 12. Flashcards / Active Recall

**Q1 — IFVG trong mô hình này là FVG nào?**
FVG **đầu tiên ngay trước cú stop-hunt** — sau MSS nó đảo vai, là vùng nhạy nhất.

**Q2 — Vào lệnh tại đâu?**
**50% CE (consequent encroachment)** của IFVG; nếu không có IFVG thì vào breaker.

**Q3 — TP được xác định thế nào?**
Next DOL, hoặc Fib (0/0.5/1/-2/-2.5) từ swing post-07:00 về open 07:00 — chốt bậc thang -2 rồi -2.5.

**Q4 — Vì sao IFVG đầu tiên nhạy nhất?**
Vì nó là dấu vết cuối cùng của dòng lệnh sai hướng ngay trước khi đảo chiều; khi bị đóng xuyên rồi test lại, đây là nơi lệnh mắc kẹt phải được giải quyết.

**Q5 — Lưu ý 30 phút đầu là gì?**
Sau 07:00/08:00/09:00, 30' đầu giá thường đi NGƯỢC bias để hunt thanh khoản trước khi đảo — đừng vào vội theo move đầu giờ.

**Q6 — Khác biệt chính với 08:30 NY?**
07:00 chuyên **50% CE của IFVG** + target Fib -2/-2.5; 08:30 vào **PD array bất kỳ** (OB/FVG/breaker) tại retest + target theo DOL cấu trúc.

---

## 13. Liên kết với Trade Journal

### Lệnh áp dụng đúng model này
```dataview
TABLE date, symbol, position, pnl, r_multiple
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, pnl, r_multiple, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

### Gợi ý frontmatter bổ sung cho mỗi trade
```yaml
model: 0700-IFVG # 0700-IFVG | 0830-NY | Unicorn | ICT-2022 | MMBM | MMSM
bias: bearish # bullish | bearish
hunt: relEQ-highs # relEQ-highs | relEQ-lows (đã hunt gì post-07:00)
mss: true
entry_type: ifvg-ce # ifvg-ce | breaker (dự phòng)
ce_50: true # vào đúng 50% CE
fib_target: -2.5 # -2 | -2.5 | next-DOL
london_dol: true # dùng London H/L làm DOL
respected_30min: true # tôn trọng lưu ý 30 phút đầu
rr_planned: 5.0
missing_step: none # none | prehunt | ifvg | mss | 30min | ce | target | stop
```

> [!tip]
> Với lệnh thua, ghi `missing_step` — phổ biến nhất là `ifvg` (đánh dấu sai IFVG) và `30min` (vào ngược trong 30' đầu).

---

## 14. Lesson Learned

### Bài học chính
- IFVG = **FVG đầu tiên trước hunt**, đảo vai sau MSS → vùng nhạy nhất; vào **50% CE** (breaker dự phòng).
- **London H/L = DOL**; chờ giá hồi về range, hunt relative equal, rồi MSS.
- **Tôn trọng 30 phút đầu** — kỳ vọng counter-move hunt trước khi đảo thật.
- **Chốt bậc thang Fib -2 / -2.5** (không đóng hết tại -2); stop ngoài swing post-07:00.
- Khi IFVG trùng breaker → Unicorn A+.

### Quy tắc cá nhân rút ra
- [ ] Tôi chỉ đánh dấu IFVG là **FVG đầu tiên** ngay trước hunt.
- [ ] Tôi chờ hết 30' đầu để hunt lộ ra, không vào vội.
- [ ] Tôi vào tại 50% CE, không vào lúc MSS.
- [ ] Tôi chốt bậc thang -2 rồi -2.5.
- [ ] Khi thua, tôi ghi `missing_step` để sửa.

### Câu nhắc khi trade
> **"London H/L làm mốc. Chờ hunt, chờ MSS, vào 50% CE của IFVG đầu tiên. Tôn trọng 30' đầu, chốt bậc thang Fib."**

---

## 15. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Hiểu định nghĩa IFVG | | Phân biệt FVG / IFVG / breaker? |
| Hiểu cơ chế (WHY) | | Vì sao FVG đầu tiên nhạy nhất? |
| Đánh dấu đúng IFVG | | Chọn đúng "FVG đầu tiên trước hunt"? |
| Chờ hunt + MSS, tôn trọng 30' | | Không front-run, không vào ngược 30' đầu? |
| Entry 50% CE + Fib target | | Vào đúng CE, chốt bậc thang? |
| Áp dụng vào trade thực tế | | Entry thật ở 50% CE của IFVG? |
| Review sau trade | | Có gắn `missing_step` + review bằng dữ liệu? |

**Kế hoạch review tiếp theo:**
- [ ] Thu thập ≥20–30 setup tag `[[07:00 AM Liquidity Hunt + IFVG Entry]]`.
- [ ] Review theo `missing_step`: hay sai ở `ifvg`, `30min`, hay `ce`.
- [ ] Thống kê win-rate theo `entry_type` (ifvg-ce vs breaker), `fib_target` (-2 vs -2.5), `respected_30min`.
- [ ] Cập nhật rule khi đủ mẫu; nâng `confidence` khi đạt mastery.
