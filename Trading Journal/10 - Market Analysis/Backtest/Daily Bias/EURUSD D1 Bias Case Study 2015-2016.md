---
type: case-study
instrument: EURUSD
timeframe: D1
method: ICT 2022 Model — Daily Bias / Dealing Range / Premium-Discount / DOL
source: FXReplay (OANDA feed), backtest replay
period_covered: "13/04/2015 → hiện tại (replay), giá hiện tại 1.11927"
status: D1 audit hoàn tất qua 5 vòng devil's-advocate — sẵn sàng xuống H1
tags: [ict, smc, backtest, case-study, eurusd, d1-bias, devils-advocate]
---

# Case Study: Xác định Daily Bias EURUSD (D1) — Từ giả thuyết ban đầu đến bản đã audit đầy đủ

> Ghi chú đọc nhanh: đây là bản tổng hợp một quá trình audit thật — bắt đầu từ một bias D1 tự viết, trải qua 5 vòng phản biện (devil's advocate) với 9 objection được đặt ra, tranh luận, và đóng (hoặc sửa). Giá trị chính của case study này **không nằm ở kết luận cuối** (bullish, dealing range 1.07047–1.13794) mà nằm ở **loại lỗi bị bắt được** và **quy trình được vá lại sau mỗi lỗi**. Đọc phần 8 (Nhật ký audit) nếu muốn thấy rõ nhất bài học.

---
![[Pasted image 20260806085449.png]]
## 1. Tổng quan tình huống

- **Công cụ:** TradingView trên FXReplay, dữ liệu OANDA, khung D1.
- **Chế độ:** LIVE (replay dừng đúng hard-right-edge, không có nến tương lai — người phân tích không biết trước điều gì sẽ xảy ra tiếp theo, giống hệt trading thật).
- **Giá hiện tại:** 1.11927.
- **Mục tiêu bài tập:** xác định Daily Bias, Dealing Range, Premium/Discount, DOL — dừng ở D1, chưa xuống H1 (đúng theo workflow D1 → H1 → M5 của bạn).
- **Vai trò AI trong case study này:** Devil's Advocate — không xác nhận thụ động, mà chủ động tìm điểm gãy trong logic, chạy lại toán học, và chỉ nhượng bộ khi có bằng chứng hoặc lập luận mới thật sự đánh bại được objection.

---

## 2. Cấu trúc D1 — bản đã chỉnh sửa qua audit (không phải bản viết đầu tiên)

![Structure Map](eurusd-d1-structure-map.svg)

Đọc theo trình tự thời gian thật (khác thứ tự bạn viết ban đầu):

| Thời điểm | Sự kiện | Giá | Vai trò cuối cùng (sau audit) |
|---|---|---|---|
| 13–14/04/2015 | Old low | 1.05204 / 1.05316 | Mốc thanh khoản cũ — **không bị quét sạch**, chỉ được test lại 8 tháng sau |
| ~10/2015 | Đỉnh trước khi giảm | 1.16334 | Bối cảnh — nằm ngoài phạm vi mọi range đang xét, quá cũ để tính là DOL gần |
| 12/11/2015 | Internal swing high | 1.08319 | Swing bị MSS phá — **KHÔNG phải** external swing lớn, chỉ là swing nội bộ trong nhịp giảm |
| ~12/2015 | Đáy tháng 12 | 1.05237 | Test lại vùng 13/4/2015, cách 3.3 pip — **không sweep**, chỉ chạm và giữ |
| 05/01/2016 | **Leg start** | 1.07047 | **D1 Dealing Range LOW** — điểm bắt đầu thật của nhịp tăng đang diễn ra |
| sau 05/01/2016 | MSS | phá 1.08319 | Xác nhận đổi hướng delivery (không phải đổi toàn bộ cấu trúc lớn) |
| 01/02/2016 | Đỉnh rally | 1.13794 | **D1 Dealing Range HIGH** |
| 10/03/2016 | Pullback + sweep | 1.08229 | Mid-leg pullback, **KHÔNG phải leg start** dù cũng có sweep + displacement |
| hiện tại | — | 1.11927 | 72.3% của range → **Premium** |
| chưa xảy ra | ERL | 1.14929 / 1.14944 | External liquidity kế tiếp, **chưa bị quét**, target giai đoạn 2 nếu 1.13794 bị phá |

**Điểm mấu chốt bị bỏ sót ở bản viết đầu tiên:** swing 1.08319 (12/11/2015) và ERL (1.14929/1.14944, cũng khoảng tháng 11/2015) là **hai mức hoàn toàn khác nhau**, cách nhau hơn 660 pip. Bản viết đầu gộp mơ hồ "swing high 12/11/2015" khiến không rõ đang nói tới cái nào — và vì ERL nằm ngay trên chart do chính tay vẽ nhưng không được nhắc tới, đây là dạng lỗi "unmentioned alternative" kinh điển: nhìn thấy nhưng không đưa vào câu chuyện vì nó không khớp kết luận đã chọn.

![[Pasted image 20260806085507.png]]

---

## 3. Dealing Range & Premium/Discount (bản cuối)

![Premium Discount Map](eurusd-d1-premium-discount.svg)

- **D1 Dealing Range:** Low 1.07047 (05/01/2016) — High 1.13794 (01/02/2016)
- **Equilibrium (50%):** 1.104205
- **Giá hiện tại:** 1.11927 → **(1.11927−1.07047)/(1.13794−1.07047) = 72.3% → Premium**
- **Plan đã tuyên bố:** không vào lệnh từ premium — chờ retrace về Discount (dưới 1.104205), tìm POI H1 trùng với D1 Discount trước khi tìm entry.

**Vì sao con số 72.3% (không phải 66.5% như bản dealing range cũ) mới là số đúng để dùng:** dealing range cũ (1.08229–1.13794) đã bị bác vì 1.08229 không phải leg start (xem mục 5). Dùng range sai khiến premium bị đo nông hơn thực tế — chênh nhau gần 6 điểm phần trăm, đủ để đổi kích thước vùng chờ discount mà kế hoạch entry sẽ dùng sau này.

**FVG #1 (1.10303–1.10802, CE đúng = 1.10553):** vắt ngang đúng đường equilibrium của range cuối — nửa dưới discount, nửa trên premium. Đã bị mitigate hoàn toàn bởi nến 10/03/2016 (O 1.099996 / H 1.12180 / L 1.08220 / C 1.11786 — nến này xuyên thủng cả 2 biên FVG và đóng cửa cao hơn đỉnh FVG gần 98 pip). Vì đã bị traded-through và đóng cửa vượt hẳn phía trên, đây là ứng viên **inversion FVG** — nếu bị test lại từ trên xuống trong tương lai, nó có thể đóng vai trò kháng cự chứ không còn là hỗ trợ.

---

## 4. MSS & xác nhận cấu trúc

- Swing bị phá: **1.08319** (giá trị đầy đủ của nến: O1.07440 H1.08319 L1.06912 C1.08135, dated 12/11/2015).
- Vai trò: MSS này **đổi hướng delivery hiện tại** (từ giảm sang tăng ngay tại thời điểm đó) — không phải một BOS xác nhận cấu trúc lớn bị đảo hoàn toàn. Phân biệt này quan trọng: swing 1.08319 chỉ là internal swing trong nhịp giảm Oct 2015 → Jan 2016, không mang authority của một external structural swing.
- **Không dùng làm căn cứ:** claim ban đầu rằng MSS "phá qua swing high gần nhất ngày 12/11/2015" khiến người đọc tưởng đó là ERL (1.14929/1.14944) — đã đính chính ở mục 2.

---

## 5. Vì sao 1.08229 KHÔNG phải leg start (bài học quan trọng nhất của case study này)

Đây là phần đáng lưu vào quy trình chuẩn nhất, vì nó là một free-parameter thật sự khó — không giải quyết được chỉ bằng cách nhìn giá.

**Vấn đề:** cả hai mức 1.07047 (05/01/2016) và 1.08229 (10/03/2016) đều thỏa quy tắc bạn tự đặt ra: *"2 swing point đã quét thanh khoản trước đó và kèm displacement theo sau."* 1.08229 thậm chí còn mới hơn. Vậy tại sao chọn 1.07047?

**Tiêu chí phân biệt (rút ra được sau khi audit):** một swing chỉ được tính là **leg-start** — tức biên của dealing range — khi nó đứng **sau một giai đoạn điều chỉnh/consolidation tách biệt** khỏi nhịp đang diễn ra. Nếu swing đó xuất hiện **bên trong** một nhịp mở rộng đã và đang chạy liên tục, nó chỉ là **mid-leg pullback** — dù có sweep + displacement riêng, nó không "bắt đầu" cái gì mới, nó chỉ tạm dừng rồi tiếp diễn cái đang có.

Áp vào case này:
- 1.07047 đứng ngay sau một giai đoạn consolidation/điều chỉnh riêng biệt từ đáy tháng 12/2015 (1.05237) — trước khi nhịp mở rộng sạch (rally tháng 2/2016) bắt đầu. → **leg start hợp lệ.**
- 1.08229 xảy ra **giữa** một nhịp mở rộng đã thiết lập từ 05/01/2016 — nó là một pullback có sweep, không phải khởi đầu nhịp mới. → **mid-leg, không phải boundary.**

**Quy tắc bổ sung vào quy trình (khuyến nghị lưu lại):**
> Một swing low/high chỉ được dùng làm biên dealing range nếu, ngoài "sweep + displacement", nó còn đứng ở ranh giới giữa hai giai đoạn cấu trúc khác nhau (kết thúc một consolidation/điều chỉnh, mở đầu một nhịp mới) — chứ không phải là một pullback bên trong nhịp đang chạy.

---

## 6. DOL / Target — kế hoạch 2 giai đoạn

1. **Target 1:** 1.13794 (D1 DLR High) — nếu bị phá với displacement rõ ràng.
2. **Target 2 (ERL):** 1.14929 / 1.14944 — external liquidity kế tiếp, hiện chưa bị quét, chỉ trở thành DOL thật sự nếu Target 1 bị phá.
3. **Không dùng đồng thời "DOL" cho cả low đã bị swept (1.08229/1.07047, chuyện quá khứ) lẫn target phía trước** — tách rõ: DOL = nơi giá đang được hút tới (phía trước), thanh khoản đã quét = giải thích cho move đã xảy ra (phía sau). Đây là lỗi thuật ngữ nhỏ ở bản viết đầu, đã tự sửa đúng ở các lượt sau.

---

## 7. Sự kiện vĩ mô (bối cảnh, không phải căn cứ kỹ thuật)

Cú đảo chiều dữ dội đầu tháng 12/2015 (từ vùng 1.052–1.070 bật thẳng lên trên 1.08 chỉ trong vài phiên) trùng thời điểm ECB họp chính sách đầu tháng 12/2015 — một trong những đợt short-squeeze EUR mạnh nhất giai đoạn đó theo trí nhớ thị trường chung. Đây là **bối cảnh**, không phải bằng chứng ICT — nó giải thích *tại sao* displacement candle ở đây đủ năng lượng để tạo MSS thật (không phải grind giả), nhưng không thay thế cho việc đọc cấu trúc giá. Nếu muốn dùng làm căn cứ chính thức, nên verify lại ngày giờ chính xác qua nguồn tin tức, không dựa vào trí nhớ.

---

## 8. Nhật ký Audit — Devil's Advocate qua 5 vòng

Bảng trạng thái đầy đủ của mọi objection, để thấy quá trình tư duy chứ không chỉ kết quả cuối:

| # | Vòng phát hiện | Loại | Nội dung | Kết quả |
|---|---|---|---|---|
| O1 | 1 | [CHART] fatal→material | Claim MSS phá "swing high 12/11/2015" — hoá ra đang nhầm với ERL (chưa từng bị phá) | NARROWED (v2) → **CLOSED** (v3, khi tách được swing 1.08319 khỏi ERL) |
| O2 | 1 | [ARITHMETIC]/[DOCTRINE] material | Giá ở 66.5% premium nhưng không hề nhắc premium/discount | **WITHDRAWN** (v2 — user công bố plan chờ discount) |
| O3 | 1 | [UNSUPPORTED] material | Target "1.3221" không xuất hiện trên chart, nghi lỗi gõ | **WITHDRAWN** (v2 — xác nhận target 2 giai đoạn 1.13794→1.14944) |
| O4 | 1 | [DOCTRINE] minor | DOL (quá khứ) và Target (tương lai) bị gộp lẫn | **WITHDRAWN** (v2 — quy trình đầy đủ làm rõ 2 khái niệm) |
| O5 | 1 | [UNSUPPORTED] minor | Old low 13/4/2015 ngoài khung chart, không verify được | **CLOSED** (v3 — chart 5 năm xác nhận trực tiếp) |
| O6 | 1 | [UNSUPPORTED] minor | FVG không có high/low/CE cụ thể | **CLOSED** (v3, kèm 2 correction: CE lệch 1.95 pip; nến 10/3 mitigate toàn bộ chứ không chỉ "gần CE") |
| O7 | 3 | [ARITHMETIC] material | FVG được cho là premium — tính lại ra discount (dùng range cũ) | Corrected — không đổi hành động, chỉ sửa lý do |
| O8 | 4 | [METHOD] material | Free-parameter: 1.07047 hay 1.08229 mới là leg start? | **CLOSED** (v5 — tiêu chí "đứng sau consolidation riêng" phân biệt được, xem mục 5) |
| O9 | 5 | [ARITHMETIC] minor | Đáy 12/2015 (1.05237) có thật sự "quét" low 13/4/2015 (1.05204) không | **CLOSED** — không sweep, chỉ test (cách 3.3 pip), sửa lại C2 |

**Tỷ lệ:** 9 objection được đặt ra, 0 objection còn mở ở tầng D1. 5 trong 9 objection ban đầu tự người phân tích (không phải AI) cung cấp bằng chứng/lập luận để đóng — tỷ lệ tự-sửa cao hơn tỷ lệ AI phải "thắng" bằng cách chỉ ra lỗi không thể chối cãi. Đây là dấu hiệu process tốt: phần lớn sai sót được bắt vì tự kiểm tra lại (equal low re-check ở O_prior, việc chủ động đưa số liệu chính xác), không phải vì bị ép.

---

## 9. Free-Parameter Scorecard (đánh giá quy trình, không phải đánh giá kết luận)

Theo khung 9 tham số của một daily-bias read kiểu ICT 2022:

| # | Tham số | Có rule viết trước không? | Áp dụng nhất quán? |
|---|---|---|---|
| 1 | Timeframe mang bias (D1) | Có — D1→H1→M5 cố định | ✅ |
| 2 | 2 swing bound dealing range | Không ban đầu — chỉ có sau audit (mục 5) | ✅ sau khi vá |
| 3 | Pool nào tính là thanh khoản đã quét | Có (sweep + displacement) | ✅, nhưng ban đầu áp nhầm mức (O1) |
| 4 | Leg nào là displacement | Có (thân nến lớn, để lại imbalance) | ✅ |
| 5 | POI nào tại entry | N/A (chưa xuống H1) | — |
| 6 | Swing nào "structurally significant" cho MSS | Ban đầu mơ hồ, sau rõ (mục 4) | ✅ sau khi vá |
| 7 | Leg đo OTE | N/A (chưa xuống H1) | — |
| 8 | Pool nào là DOL | Có, tách 2 giai đoạn rõ ràng (mục 6) | ✅ |
| 9 | Killzone/clock | N/A ở D1 | — |

Kết luận: 6/6 tham số áp dụng được ở D1 giờ đều có rule tường minh — 2 tham số (#2, #6) chỉ đạt được mức đó **sau** audit, không phải ngay từ đầu. Đây chính là giá trị của quá trình phản biện: không phải tạo ra rule mới từ hư không, mà buộc rule ngầm định phải phát biểu ra thành lời, lúc đó mới lộ ra kẽ hở.

---

## 10. Góc nhìn đối lập (Bearish case) — bản cập nhật đầy đủ

Giữ nguyên toàn bộ fact, đổi vai trò tường thuật:

- Cú reversal đầu tháng 12/2015 → short-squeeze dữ dội nhưng **chưa từng** lấy lại được đỉnh Oct 2015 (1.16334) hay thậm chí ERL (1.14929/1.14944) — hơn 3 tháng sau vẫn giao dịch dưới cả hai mức này khá xa.
- Giá hiện tại (1.11927) đang ở 72.3% premium của dealing range **đã audit đúng** — sâu hơn cả số ước tính ban đầu (66.5%) — ngay dưới một vùng cung external (ERL) chưa từng bị mitigate.
- FVG #1 đã bị nuốt trọn và đóng cửa vượt hẳn phía trên — ứng viên inversion, nghĩa là nếu bị test lại từ trên, nó có thể trở thành kháng cự thay vì hỗ trợ.
- Nhịp tăng hiện tại có thể đọc như: giá đang được đẩy lên từ discount cũ, xuyên qua equilibrium, tiến vào đúng vùng có thể dùng để mồi thanh khoản long muộn trước khi đảo xuống quét lại phần dưới range (hoặc phá sâu hơn 1.07047).

**Tự phản biện case này:** chưa có bất kỳ nến từ chối nào tại vùng 1.137–1.150 — case bearish này thuần túy positional (dựa vào vị trí trong range), chưa được xác nhận bởi price action thật. Cùng trạng thái epistemic với case bullish (cũng chưa breakout xác nhận qua 1.13794).

**Nhãn:** *equally viable* — không nghiêng hẳn về phía nào tính đến thời điểm hiện tại của replay.

**Distinguishing observable duy nhất còn thiếu:** phản ứng giá (đóng nến, có/không rejection) khi chạm lại vùng 1.137–1.150. Chưa xảy ra → chưa thể phân định.

---

## 11. Process Score & Verdict

- **Process Score: 8/10.** Lý do: cấu trúc, dealing range, premium/discount, DOL đều được thiết lập đúng theo phương pháp — nhưng KHÔNG phải ngay từ lần đầu; mất 5 vòng audit để đến bản đúng, với 2 lỗi đáng kể ở lần viết đầu (nhầm MSS-swing với ERL; nhầm mid-leg pullback với leg-start) mà nếu không bị hỏi ngược lại có thể đã lọt qua.
- **Verdict:** `Correct process / chưa có outcome` — đây là bài tập backtest bias thuần túy (không có entry/SL/TP), nên không áp dụng nhãn win/loss. Nếu phải xếp theo tinh thần rubric: **quy trình đúng sau khi tự sửa** — không phải "đúng ngay từ đầu."
- **Điều case study này KHÔNG chứng minh:** rằng bias bullish sẽ đúng; rằng buy từ premium là sai; rằng phần H1/M5 (chưa review) sẽ cho entry hợp lệ.

### Action Items

- [ ] Viết chính thức tiêu chí "leg-start vs mid-leg pullback" (mục 5) vào file quy trình gốc, không chỉ để trong case study này
- [ ] Khi xuống H1: tìm MSS/BOS xác nhận hoặc mâu thuẫn với bias D1 bullish — đây là lỗi lặp lại nhiều nhất theo rubric mentor (counter-HTF entry without H1 validation)
- [ ] Xác định lại FVG #2 (tạo bởi nến 10/03/2016, hiện chưa có số liệu high/low/CE cụ thể) trước khi dùng nó cho bất kỳ mục đích nào
- [ ] Theo dõi phản ứng giá tại vùng 1.137–1.150 làm distinguishing observable cho toàn bộ case — đây là thứ duy nhất sẽ phân định được bull vs bear case
- [ ] Trước khi tìm H1 POI: xác nhận lại premium/discount ở khung H1 có trùng hướng discount của D1 hay không (đúng như plan gốc đã tuyên bố)

---

## 12. Bước tiếp theo

D1 audit coi như hoàn tất — không còn objection mở. Bước kế tiếp đúng theo workflow D1 → H1 → M5: xuống H1, tìm MSS/BOS xác nhận (hoặc phủ nhận) bias bullish này, xác định POI (FVG/OB) tại đúng vùng H1-discount trùng D1-discount như plan đã đề ra ở mục 3.
