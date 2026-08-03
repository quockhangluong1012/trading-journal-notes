---
date: 2026-05-13
symbol: NDX
position: Long
result: Win
session: New York
setup: "[[Trading Journal/03 - Playbooks/3.2 - Setups/Venom Model]]"
entry_model: ICT 2022 Model
entry_timeframe: M5
higher_timeframe_bias: D1
bias_correct: Bullish
entry_price: 29,127.50
take_profit: 29,227.10
stop_loss: 28,962.00
pnl: 180
r_multiple:
risk_percent: 5%
mistakes:
  - "[[05 - Mistake - Not enough RR]]"
  - "[[07 - Mistake - Risk more than 0.5% total account]]"
tags:
planned_rr: 0.6
da_verdict: BROKEN
da_evidence_sufficiency: thin
da_objections: {fatal: 2, material: 2, minor: 1}
da_opposite_case: "weaker but non-trivial"
---

# Trade 2026-05-13 - NDX Long Win

## 0. Trade Summary

| Field           | Value                                             |
| --------------- | ------------------------------------------------- |
| Symbol          | NDX                                               |
| Position        | Long                                              |
| Result          | Win                                               |
| Session         | London                                            |
| Setup           | ICT 2022 Model                                    |
| Entry Model     | Liquidity Sweep + MSS + FVG / OB Reaction / Other |
| Entry Timeframe | M1                                                |
| HTF Bias        | Bullish                                           |
| Bias Correct?   | Yes                                               |
| Entry           | 29,127.50                                         |
| Stop Loss       | 28,962.00                                         |
| Take Profit     | 29,227.10                                         |
| PnL             | 180                                               |
| R Multiple      | 1.36                                              |

---

## 1. Pre-market Bias

### D1

- **Bias D1**: Bullish
- **Market Condition**: Trending
- **Lý do xác định bias**:
  - Bullish - Giá đang trong trend tăng sau nhịp hồi
- **Liquidity mục tiêu D1**:
  - Buy-side liquidity:
  - Sell-side liquidity:
- **Ghi chú quan trọng**:
  - 

![[Pasted image 20260620064723.png]]

---

### H1

- **Cấu trúc H1**: HH/HL / LH/LL / Range
- **Dealing Range chính**:
  - High:
  - Low:
  - Premium / Discount:
- **POI chính**:
  - Order Block:
  - FVG:
  - Breaker:
  - Other:
- **Liquidity cần chờ sweep**:
  - Order Block trong vùng discount bên dưới
- **Kịch bản mong muốn**:
  - Quét order block và rejection

![[Pasted image 20260620064732.png]]

---

### M15 / M5

- Giá thực hiện 1 pha quét thanh khoản bên dưới OB và 1 đáy cũ quan trọng
- Giá quét xuống cạnh dưới Venom box (8:00 - 9:30 AM NY)
- Sau khi qua phản ứng tại OB, giá bật hồi lên
- Giá hình thành BPR theo mô hình Venom
- Entry khi giá retrace

- **Giá đã vào POI chưa?** Yes
- **Có Liquidity Sweep chưa?** Yes
- **Sweep loại nào?**
  - Internal liquidity
- **Có Displacement chưa?** Yes
- **Có MSS chưa?** Yes
- **Có FVG hợp lệ chưa?** Yes
- **Entry có nằm trong POI không?** Yes


![[Pasted image 20260620064740.png]]

---

### M1 Entry Timeframe

- **Entry trigger**:
  - Liquidity Sweep:
  - MSS:
  - Displacement:
  - FVG:
  - OB:
- **Entry reason**:
  - 
- **Invalidation reason**:
  - 
- **Tôi có chờ đủ điều kiện không?** Yes / No

![[Pasted image 20260620064749.png]]

---

## 2. Checklist Trước Khi Vào Lệnh

- [x] Đã xác định Daily Bias rõ ràng
- [x] Bias không mâu thuẫn với H1/M15
- [x] Giá đã vào vùng POI hợp lệ
- [x] Có Liquidity Sweep trước entry
- [x] Có Displacement rõ ràng
- [x] Có Market Structure Shift hợp lệ
- [x] Entry nằm trong FVG / OB / PD Array hợp lệ
- [x] Stop loss đặt ở vùng invalidation hợp lý
- [ ] RR tối thiểu đạt yêu cầu
- [x] Đã kiểm tra tin tức quan trọng
- [x] Không vào lệnh vì FOMO
- [x] Không revenge trade
- [x] Không vào lệnh ngoài kế hoạch

---

## 3. Execution Review

### Điều tôi làm đúng

- Xác định đúng daily bias, vùng POI
- Xác định đúng Venum Box
- Chờ giá break 1 cạnh Venom box

### Điều tôi làm sai

- Giá không hình thành BPR của Setup Venom Model nhưng lại vào lệnh theo model này
- Giá tạo MSS + Displacement + FVG và sau đó retrace về FVG -> entry theo mô hình ICT 2022

### Tâm lý khi vào lệnh

- Bình tĩnh
- Ghi chú:
  - Đang học 1 chiến lược giao dịch mới

### Có tuân thủ plan không?

- **No**
- Nếu không, tôi đã phá rule nào?
  - Không chờ giá tạo BPR

---

## 4. Phân Tích Sau Lệnh

- **Result**: Manual Close
- **Mistake chính**:
  - [[Mistake - ]]
- **Nguyên nhân gốc rễ**:
  - `(trống trong bản gốc — dựa trên dữ kiện có trong file: mistake tags frontmatter "05 - Not enough RR" và "07 - Risk more than 0.5%" là hai lỗi tự nhận rõ ràng nhất, khớp trực tiếp với planned_rr: 0.6 và risk_percent: 5% trong frontmatter)`.
- **Tại sao lệnh này thua/thắng?**
  - `(trống — Execution Review "Điều tôi làm sai" cho biết lệnh được vào theo ICT 2022 Model dù ban đầu định theo Venom Model, tức là chuyển đổi tiêu chí entry giữa lúc quan sát, không phải một model cố định từ đầu)`.
- **Thị trường đã cho tín hiệu cảnh báo nào trước khi thua?**
  - `(N/A — lệnh Win, không có cảnh báo thua được ghi)`.
- **Nếu được vào lại, tôi sẽ làm gì khác?**
  - `(trống — dựa trên "Lesson Learned" gốc dưới đây: kiên nhẫn chờ setup Venom hình thành đúng, không chuyển sang ICT 2022 Model giữa chừng)`.

---

## 5. Lesson Learned

### Bài học kỹ thuật

- Học thêm về Venom Model (bullet gốc)
- Lệnh này chuyển đổi tiêu chí entry giữa lúc quan sát: bắt đầu theo dõi theo Venom Model (chờ BPR trong Venom box), khi BPR không hình thành thì chuyển sang dùng tiêu chí ICT 2022 Model (MSS+Displacement+FVG) để entry — đây là một dạng **free parameter chọn sau khi quan sát diễn biến giá**, không phải rule cố định trước (O1, load-bearing).
- Checklist section 2 tick `[x]` 12/13 dòng bao gồm "Có Market Structure Shift hợp lệ" và "Entry nằm trong FVG/OB/PD Array hợp lệ" — khớp với phần narrative M15/M5 tự trả lời "Yes" cho MSS/Displacement/FVG/POI — đây là điểm hiếm hoi trong cụm 05-13 mà checklist và narrative đồng thuận với nhau (khác với 2 file Loss-05-13 đã phân tích).

### Bài học tâm lý

- Kiên nhẫn chờ setup hình thành (bullet gốc)
- "Đang học 1 chiến lược giao dịch mới" (ghi chú tâm lý gốc) — tự nhận đang trong giai đoạn học Venom Model, khớp với việc chuyển đổi model giữa chừng (O1). Đáng chú ý: dù tự nhận phá rule ("Không chờ giá tạo BPR") và mistake tag "Not enough RR", nhãn Result vẫn là Win và Final Grade không bị điền để phản ánh việc phá rule — outcome không tự động sửa hành vi ghi nhận (liên hệ CS-O6, mẫu rule-drift "kết quả quyết định độ khắt khe").

### Bài học quy trình & risk

- risk_percent 5% + planned_rr 0.6 là tổ hợp risk cao/reward thấp nhất trong toàn cụm 05-13 — brief đã lưu ý điều này. RR 0.6 nghĩa là risk 165.5 điểm để đổi lấy reward kế hoạch chỉ 99.6 điểm — risk nhiều hơn reward gấp 1.66 lần, đồng thời risk % gấp 10× rule 0.5% (liên hệ CS-O1, CS-O6, CS-O7 — compounding risk 5% với 4 losses liên tiếp = -18.5% equity).
- Không có gate nào ngăn entry khi checklist "RR tối thiểu đạt yêu cầu" = unchecked `[ ]` — lệnh vẫn được thực hiện dù chính checklist đã đánh dấu không đạt chuẩn RR trước khi entry (O2).
- File này (Win-01) và `Win-02-Trade-2026-05-13-NDX-Long.md` cùng entry 29,127.5 / SL 28,962 nhưng TP khác (29,227.10 vs 29,320) — cần xác định đây là 2 lệnh scale-out của cùng 1 setup hay 2 bản ghi trùng của 1 lệnh, hay 2 lệnh riêng cùng vùng entry sau chuỗi Loss 05-13 (re-entry sau stop) (O3, xem mục 8).

### Rule cần thêm/cập nhật

- [ ] Kiên nhẫn (bullet gốc)
- [ ] **KIỂM TRA ĐƯỢC**: Nếu đã chọn theo dõi một setup theo model A (vd Venom, chờ BPR), không chuyển sang tiêu chí model B (vd ICT 2022, MSS+FVG) để entry cùng một lần quan sát giá — nếu model A không hình thành đúng điều kiện, ghi log "SKIPPED - BPR không hình thành" và dừng, không tự động fallback sang model khác (đóng O1).
- [ ] **KIỂM TRA ĐƯỢC**: Khi checklist "RR tối thiểu đạt yêu cầu" = unchecked, không entry — bất kể các mục khác đã tick đủ; ngưỡng RR tối thiểu cụ thể (vd ≥1.0 hoặc ≥1:3 theo chuẩn của `Win-01-04-20`) cần được ghi rõ trong checklist thay vì để mơ hồ (đóng O2, liên hệ CS-O6).
- [ ] **KIỂM TRA ĐƯỢC**: Trước khi tạo file mới cho một entry zone đã có lệnh khác cùng ngày với entry price giống nhau, ghi rõ trong frontmatter đây là "scale-in", "re-entry sau stop", hay lệnh độc lập — hiện không có field nào phân biệt 3 khả năng này (đóng O3).

---

## 6. Action Items Cho Các Lệnh Sau

- [ ] Trước khi trade phải kiểm tra liquidity sweep
- [ ] Không trade MSS nếu giá chưa nằm trong POI
- [ ] Không entry chỉ vì displacement
- [ ] Không revenge trade sau lệnh thua
- [ ] Luôn kiểm tra economic news trước New York Kill Zone

---

## 7. Final Grade

| Tiêu chí | Điểm |
|---|---|
| Daily Bias | /10 |
| POI Selection | /10 |
| Liquidity Sweep | /10 |
| MSS Confirmation | /10 |
| Entry Execution | /10 |
| Risk Management | /10 |
| Psychology | /10 |

**Overall Grade**: /10

**Trade Quality**: A / B / C / D / F

---

## 8. Devil's Advocate — Phản biện chuyên sâu

**Evidence base**: Prose-only + 4 link chart Obsidian chết (dataset không có ảnh). Sufficiency: **thin** cho claim structure (MSS/FVG/POI — chỉ có "Yes" tự ghi, không kiểm được), nhưng **arithmetic RR và cross-reference với file `Win-02` cùng ngày là kiểm được trực tiếp từ số liệu đã cho**, không cần chart.

**Thesis & claims**:
- C1: HTF bias D1 Bullish, Long khớp hướng, checklist 12/13 tick — setup trông "chuẩn" theo hầu hết tiêu chí ICT 2022 Model.
- C2 (load-bearing): Entry được thực hiện dựa trên chuyển đổi từ Venom Model (chờ BPR, không hình thành) sang ICT 2022 Model (MSS+FVG, có hình thành) — Execution Review tự ghi rõ điều này ("Giá không hình thành BPR... nhưng lại vào lệnh theo model này" / "Giá tạo MSS+Displacement+FVG... entry theo mô hình ICT 2022").
- C3: RR kế hoạch 0.6 (risk 165.5, reward 99.6) — thấp hơn 1.0, tự gắn mistake tag "Not enough RR" (05) đồng thời checklist tick "RR tối thiểu đạt yêu cầu" = unchecked.
- C4: risk_percent 5% — tự gắn mistake tag "Risk more than 0.5%" (07).
- C5: Lệnh thắng (Win, Manual Close, pnl +180) → không có nghĩa gì về việc C2/C3/C4 có đúng process hay không (outcome không phải evidence).

Suy luận: C2 là load-bearing vì nó quyết định lệnh này thực chất theo model nào — nếu Venom Model không hình thành đúng điều kiện (BPR), thì "Entry Model: ICT 2022 Model" trong frontmatter là nhãn được gán *sau khi* đã quyết định vào lệnh, không phải trước.

**Điều gì đứng vững**: Arithmetic khớp — risk = |29,127.50 − 28,962.00| = 165.5; reward (TP) = |29,227.10 − 29,127.50| = 99.6; RR = 99.6/165.5 = **0.602** ≈ `planned_rr: 0.6`. Direction Long khớp cấu trúc SL < Entry < TP. Mistake tags 05 và 07 khớp chính xác với planned_rr 0.6 và risk_percent 5% — đây là một trong ít file tự gắn tag đúng với dữ liệu số, không mâu thuẫn (khác với nhiều file khác trong sample theo CS-O1).

**Objections**:

**O1 · [METHOD] · fatal · attacks C2 (load-bearing)**
Claim: entry_model = "ICT 2022 Model" (frontmatter), setup = "Venom Model" (field setup).
Fails: Execution Review "Điều tôi làm sai" tự ghi rõ: Venom Model được chọn theo dõi trước ("Xác định đúng Venum Box", "Chờ giá break 1 cạnh Venom box"), nhưng khi BPR (điều kiện lõi của Venom Model) **không hình thành**, user chuyển sang dùng tiêu chí của một model khác (MSS+Displacement+FVG, tức ICT 2022 Model) để entry ngay trên cùng một lần quan sát giá. Đây là free parameter chọn *sau khi* biết model A không đạt điều kiện — đổi tiêu chí đánh giá giữa chừng, không phải áp dụng một rule cố định từ đầu.
Evidence: "Giá không hình thành BPR của Setup Venom Model nhưng lại vào lệnh theo model này" + "Nếu không, tôi đã phá rule nào? Không chờ giá tạo BPR" — hai câu tự thuật xác nhận trực tiếp.
Consequence: nhãn "Entry Model: ICT 2022 Model" trong frontmatter không phản ánh một kế hoạch entry đã định trước — nó là nhãn được gán sau khi quyết định đổi hướng. Nếu tiêu chuẩn ICT 2022 Model (MSS+FVG) đã đủ tốt để entry độc lập, thì việc ban đầu theo dõi Venom Model là dư thừa; nếu Venom Model là kế hoạch chính, thì đây là entry ngoài kế hoạch (nhưng checklist lại tick "Không vào lệnh ngoài kế hoạch" = `[x]`, mâu thuẫn trực tiếp với "Có tuân thủ plan không? No").
Your best answer: "MSS+FVG là confluence bổ sung hợp lệ khi Venom Model không đạt, không phải đổi model tùy tiện." — Không cứu được: chính user tự liệt kê đây là "Điều tôi làm sai" và "phá rule" trong Execution Review, tức là user tại thời điểm ghi journal cũng không coi đây là một quyết định hợp lệ.
Retracted by: một rule được viết TRƯỚC lệnh này quy định khi nào được phép chuyển từ Venom Model sang ICT 2022 Model giữa lúc quan sát — hiện không có.

**O2 · [SELF-CONTRADICTION] · fatal · attacks C3**
Claim: checklist "Không vào lệnh ngoài kế hoạch" = `[x]` (tick đạt).
Evidence: Execution Review "Có tuân thủ plan không?" = **"No"**, kèm "Nếu không, tôi đã phá rule nào? Không chờ giá tạo BPR" — trực tiếp mâu thuẫn với tick `[x]` ở checklist section 2 cùng file.
Consequence: ít nhất 1/13 dòng checklist là sai so với chính Execution Review ngay bên dưới — làm giảm độ tin cậy của toàn bộ checklist 12/13 tick còn lại, tương tự pattern đã ghi ở CS-O9 cấp cross-setup. Đồng thời, mistake tag "05 - Not enough RR" khớp đúng với checklist "RR tối thiểu đạt yêu cầu" = unchecked — cho thấy checklist *đôi khi* nhất quán với mistake tag (dòng RR) nhưng *không* nhất quán ở dòng khác (dòng "ngoài kế hoạch") trong cùng file.
Your best answer: "Tick 'không vào lệnh ngoài kế hoạch' áp cho kế hoạch tổng thể ngày đó (đã định trade NDX), còn 'No' ở tuân thủ plan chỉ áp cho chi tiết Venom Model." — Wound nhưng không giải hết: nếu đúng vậy, hai câu hỏi checklist đang đo hai thứ khác nhau dưới cùng một tên gọi mơ hồ ("kế hoạch"), đây vẫn là lỗi định nghĩa không rõ ràng trong template.
Retracted by: định nghĩa rõ ràng "kế hoạch" trong checklist là kế hoạch ngày hay kế hoạch từng model cụ thể.

**O3 · [UNSUPPORTED] · material** — File này và `Win-02-Trade-2026-05-13-NDX-Long.md` có entry 29,127.5(0) / SL 28,962(.00) giống nhau tuyệt đối, nhưng TP khác (29,227.10 vs 29,320) và pnl trùng (180 cả hai) — không đủ dữ liệu (không timestamp, không field phân biệt) để xác định đây là 2 lệnh scale-out của cùng một entry hay 2 bản ghi khác nhau của cùng một sự kiện giao dịch. Nếu là 1 lệnh ghi 2 lần, N=25 (theo CS-O0′) cần trừ thêm; nếu là 2 lệnh scale hợp lệ, cần ghi rõ trong frontmatter (liên hệ CS-O0′, xem thêm mục 9 Opposite Case). Retracted by: xác nhận từ user + timestamp phân biệt 2 sự kiện.

**O4 · [METHOD] · material · attacks context ngày 05-13** — Lệnh này (Win-01, session ghi "New York" trong bảng Trade Summary nhưng field `session:` frontmatter lại ghi "New York" — nhất quán ở đây) xảy ra cùng ngày 05-13 với 2 lệnh Loss (Loss-01 session London) và Win-02 (cùng entry zone). Tính theo trình tự London → NY, đây có khả năng là **re-entry sau 1-2 lệnh Loss cùng vùng giá** trong cùng ngày — brief đã lưu ý "ngày 13/05 có tổng 3-4 lệnh cùng entry zone sau 1 Loss". Không có timestamp giờ:phút để xác nhận thứ tự chính xác, nhưng nếu đúng là re-entry ngay sau stop, đây là hành vi cần đối chiếu với rule "revenge trade" (checklist tick "Không revenge trade" = `[x]`, nhưng re-entry cùng vùng giá ngay sau loss là chính xác kiểu hành vi rule này nhằm ngăn). Your best answer: "NDX Long lặp lại vùng giá là hợp lý nếu đó vẫn là cùng một dealing range/POI, không phải revenge." — Có thể đúng, nhưng không loại trừ được khả năng ngược lại vì thiếu timestamp. Retracted by: thứ tự thời gian chính xác (giờ:phút) của Loss-01, Win-01, Win-02 ngày 05-13.

**O5 · [DOCTRINE] · minor** — RR 0.6 thấp hơn 1.0 nghĩa là risk nhiều hơn reward kế hoạch — không có anchor doctrine cụ thể nào trong `references/doctrine.md` (không tồn tại trong bộ dữ liệu này để trích dẫn trực tiếp) quy định RR tối thiểu tuyệt đối, nhưng theo chính checklist khác trong sample của user (`Win-01-04-20` dùng chuẩn 1:3), RR 0.6 thấp hơn cả chuẩn nội bộ đã từng dùng — đây là doctrine gap ở tầng "chuẩn RR" chưa được cố định trong hệ thống của user (liên hệ CS-O6, bảng rule-drift "RR tối thiểu"). Retracted by: không cần, ghi nhận biên.

Drafted 6, cut 1 (draft về "Venom box time window 8:00-9:30 AM NY" không đủ evidence để tách thành objection riêng — gộp vào O1 vì cùng thuộc load-bearing chuyển đổi model).

**Verdict**: **BROKEN** — load-bearing claim C2 (entry theo ICT 2022 Model là quyết định hợp lệ) sụp vì chính user tự nhận đây là chuyển đổi model giữa chừng sau khi Venom Model thất bại điều kiện (O1), cộng thêm self-contradiction trực tiếp giữa checklist và Execution Review (O2). Evidence thin cho phần structure (MSS/FVG) nhưng O1/O2 không cần chart để phán.
Tôi đã tấn công gì mà không phá được: arithmetic RR (0.6, đúng công thức), hướng lệnh (Long khớp bias Bullish), tính nhất quán giữa mistake tags và số liệu risk/RR (hiếm có trong sample).
Critique này KHÔNG xác lập: (1) MSS/FVG/Displacement ở M15/M5 có tồn tại thật trên chart; (2) đây có phải re-entry sau stop hay không (thiếu timestamp — O4 để mở); (3) quan hệ thật với file `Win-02` cùng ngày (1 lệnh hay 2 — O3 để mở); (4) outcome Win không chứng minh việc đổi model giữa chừng là quyết định đúng.

**Opposite Case**: Đổi vai "chuyển đổi model giữa chừng" — thay vì đọc là free parameter tùy tiện (O1), đọc như việc Venom Model và ICT 2022 Model không loại trừ nhau mà là **hai lớp confluence chồng lên nhau tại cùng một POI** (Venom box và FVG/MSS cùng chỉ về một vùng giá) — nếu vậy, "chuyển đổi" chỉ là cách diễn đạt, còn thực chất entry được hỗ trợ bởi 2 nguồn tín hiệu độc lập cùng đồng thuận, mạnh hơn 1 model đơn lẻ.
Load-bearing claim của kèo ngược: Venom box và FVG/MSS trùng vị trí giá (không phải 2 vùng khác nhau được dùng thay thế nhau).
Strongest self-objection: nếu 2 nguồn tín hiệu thật đồng thuận, tại sao Execution Review tự liệt "Giá không hình thành BPR của Setup Venom Model" là "Điều tôi làm sai"? Nếu 2 confluence hỗ trợ nhau, việc thiếu BPR không nên bị coi là sai — chính cách diễn đạt tự thuật của user đã chọn khung "sai lầm", không phải "confluence mạnh hơn".
Strength label: **weaker but non-trivial** — kèo ngược không vô lý (2 model có thể cùng chỉ về 1 vùng giá hợp lý về logic thị trường), nhưng bị đè bởi cách chính user tự thuật lại (coi là lỗi, không phải xác nhận kép); cần chart để phân biệt rõ.
Observable duy nhất phân biệt hai reading: vị trí chính xác của Venom box (8:00-9:30 AM NY) và FVG/OB trên chart M5/M15 — nếu trùng nhau (cùng vùng giá, cùng thời điểm), kèo ngược có cơ sở; nếu là hai vùng tách biệt được dùng thay thế lẫn nhau, thesis gốc (free parameter) đúng hơn.

## 9. Opposite Case (Counter-Argument)

(Đã trình bày ở mục 8 — Opposite Case. Riêng với câu hỏi "Win-01 và Win-02 là 2 lệnh scale hay ghi trùng": không đủ observable để dựng opposite case tách biệt — xem O3 ở mục 8, đây là câu hỏi UNSUPPORTED cần dữ liệu ngoài file, không phải một cách đọc khác của cùng evidence.)

## 10. Falsification Tests

1. **Test cho O1**: Xin chart M5/M15 thật của khung giờ entry — nếu Venom box và FVG/MSS/OB nằm cùng một vùng giá hẹp (trong vòng vài điểm NDX), O1 giảm về `material` (2 confluence hợp lệ chồng lên nhau); nếu là hai vùng tách biệt, O1 giữ `fatal`.
2. **Test cho O3**: Xin timestamp giờ:phút chính xác của Win-01 và Win-02 — nếu cách nhau đủ xa (>30 phút) với các diễn biến giá khác nhau ở giữa, đây là 2 lệnh riêng (đóng O3 theo hướng "không trùng"); nếu cùng giờ hoặc rất gần, nghi vấn ghi trùng tăng lên `fatal`.
3. **Test cho O4**: Xin timestamp chính xác của Loss-01 (05-13) so với Win-01/Win-02 — nếu Win-01 xảy ra trong vòng <15 phút sau khi Loss-01 đóng, đây là bằng chứng ủng hộ re-entry-sau-stop (đóng O4 theo hướng cần thêm giám sát); nếu cách xa nhiều giờ hoặc session khác hẳn (London vs New York, như field session hiện tại gợi ý), O4 giảm về `minor`.
