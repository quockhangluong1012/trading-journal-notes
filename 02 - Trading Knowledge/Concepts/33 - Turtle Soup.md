---
type: ict-concept
concept: Turtle Soup
aliases:
  - Turtle Soup
  - False Breakout
  - Stop Raid Reversal
tags:
  - trading/ict/concept
  - trading/study
  - "#TurtleSoup"
status: seed
category: Entry Model
timeframes:
  - D1
  - H4
  - H1
  - M15
  - M5
  - M1
models:
  - "[[ICT 2022 Model]]"
importance: 5
confidence: 1
last_reviewed:
created: 2026-06-24
updated: 2026-06-24
related_concepts:
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[Fair Value Gap]]"
  - "[[07 - Buy-side Liquidity]]"
  - "[[30 - Sell-side Liquidity]]"
  - "[[12 - Daily Bias]]"
prerequisites:
  - "[[20 - Liquidity Sweep]]"
  - "[[21 - Market Structure Shift]]"
  - "[[19 - Liquidity]]"
common_mistakes: []
---

# Turtle Soup

> [!summary] Tóm tắt 1 câu
> **Turtle Soup** là mô hình đảo chiều dựa trên một cú **false breakout** — giá phá vỡ một mức swing high/low hiển nhiên để quét stop của breakout traders ([[20 - Liquidity Sweep]]), rồi nhanh chóng **reclaim** (lấy lại) vào trong range và đảo chiều — và ta vào lệnh theo chiều ngược lại với đám đông vừa bị bẫy.

> [!important] Nguyên tắc cốt lõi
> Một cú phá vỡ chỉ trở thành **Turtle Soup** khi giá **RECLAIM** lại mức vừa phá VÀ tạo **displacement** (nến/đoạn dịch chuyển mạnh) ngược chiều, kèm **MSS** trên khung thấp.
> - Nếu giá phá vỡ và **đóng cửa chấp nhận (acceptance) ngoài mức** rồi đi tiếp → đó là **real breakout / continuation**, KHÔNG phải Turtle Soup. Đứng ngoài hoặc trade theo phá vỡ.
> - "Quét rồi quay lại" = Turtle Soup. "Quét rồi đi tiếp" = breakout thật. Toàn bộ edge nằm ở việc phân biệt hai trạng thái này → **đừng dự đoán, hãy chờ phản ứng**.

---

## 1. Định nghĩa

### Khái niệm (nguồn gốc)
**Turtle Soup** là tên một chiến lược cổ điển do Linda Raschke đặt, ban đầu là *phản đòn* (counter-trade) lại hệ thống nổi tiếng của nhóm **Turtle Traders** — những người mua/bán khi giá phá vỡ đỉnh/đáy 20 ngày (20-day high/low). Raschke nhận ra rằng phần lớn các cú phá vỡ đó là **giả**: giá chỉ nhú qua mức rồi quay lại. "Turtle Soup" = "nấu súp từ những con rùa" = ăn tiền của các Turtle bị bẫy bởi false breakout.

ICT (Inner Circle Trader) đã hấp thụ ý tưởng này và đóng khung lại bằng ngôn ngữ thanh khoản: **Turtle Soup là một [[20 - Liquidity Sweep]] của một mức external/hiển nhiên (obvious level) được dùng như tín hiệu vào lệnh đảo chiều.**

### Bản chất (liquidity grab reversal)
Phía sau mỗi đỉnh/đáy rõ ràng là một cụm **stop order** và **breakout order**:
- Trên một old high / equal highs → là [[07 - Buy-side Liquidity]] (BSL): stop của người short + buy-stop của breakout buyers.
- Dưới một old low / equal lows → là [[30 - Sell-side Liquidity]] (SSL): stop của người long + sell-stop của breakout sellers.

Smart money cần thanh khoản để khớp lệnh lớn. Họ đẩy giá **xuyên qua mức** để kích hoạt đám lệnh đó (lấy "nhiên liệu"), rồi đảo chiều. Turtle Soup chính là việc **vào lệnh ngay sau cú quét đó, theo chiều smart money**.

### Quan hệ với [[20 - Liquidity Sweep]]
Turtle Soup gần như **đồng nghĩa với cách dùng đảo chiều của [[20 - Liquidity Sweep]]**:
- [[20 - Liquidity Sweep]] = khái niệm gốc (giá quét qua một pool thanh khoản rồi từ chối).
- **Turtle Soup** = tên *mô hình giao dịch* cụ thể khi cú sweep đó xảy ra ở một **mức external hiển nhiên** (PDH/PDL, equal highs/lows, session H/L, swing high/low) và được dùng làm **entry đảo chiều**.

> Hiểu đơn giản: Turtle Soup là Liquidity Sweep "đóng gói thành một setup có entry/stop/target".

### Phân biệt false breakout vs real breakout
| | False breakout (Turtle Soup) | Real breakout (Continuation) |
|---|---|---|
| Cách đóng nến qua mức | Nến đuôi dài (wick), thân ngắn, **không acceptance** | Thân nến đóng dứt khoát ngoài mức, có **acceptance** |
| Sau khi phá | **Reclaim** nhanh về trong range | Đi tiếp, retest mức như support/resistance mới |
| Displacement | Có, nhưng **ngược chiều** cú phá | Có, **cùng chiều** cú phá |
| Khối lượng/đà | Nhú yếu, hết đà ngay | Mở rộng range, đà mạnh duy trì |

### Mục đích trong ICT
- Cung cấp một **điểm vào đảo chiều xác suất cao** ngay tại đỉnh/đáy của một swing — nơi rủi ro nhỏ (stop sát) còn reward lớn (cả range để chạy).
- Là "công tắc" xác nhận [[12 - Daily Bias]]: nếu bias là long, ta chờ Turtle Soup quét SSL bên dưới rồi mua.

### Vì sao quan trọng
- Nó cho entry tại **external range liquidity** (xem [[16 - Internal & External Range Liquidity (IRL & ERL)]]) — các điểm cực trị nơi đảo chiều thực sự bắt đầu.
- Tránh được cái bẫy lớn nhất của trader mới: **đu theo breakout** đúng lúc smart money đang phân phối.

### Nó giúp trả lời câu hỏi gì?
- "Cú phá đỉnh/đáy này là thật hay là bẫy?"
- "Mức này có phải nơi smart money quét thanh khoản trước khi đảo chiều không?"
- "Tôi nên fade (đánh ngược) cú phá vỡ này hay chạy theo nó?"

### Turtle Soup không phải là gì
- **Không phải** lệnh đoán đáy/đỉnh mù quáng. Phải có sweep + reclaim + displacement + MSS, không chỉ "giá rớt sâu nên mua".
- **Không phải** mọi cú chạm đỉnh/đáy. Cần mức **hiển nhiên/external** mà đám đông nhìn thấy (chứa thanh khoản thật).
- **Không phải** real breakout. Nếu có acceptance ngoài mức → đó là continuation, không phải Turtle Soup.
- **Không phải** entry độc lập với context. Phải khớp với [[12 - Daily Bias]] và vùng [[27 - Premium Discount]].

---

## 2. Bối cảnh sử dụng

### Các loại / trạng thái
| Loại Turtle Soup | Hướng lệnh | Mức bị quét | Thanh khoản | Vào lệnh khi |
|---|---|---|---|---|
| TS Long (bullish) | Mua | Quét **SSL** dưới old low / equal lows / PDL / session low | [[30 - Sell-side Liquidity]] | Giá reclaim lên trên mức + displacement up + MSS bullish |
| TS Short (bearish) | Bán | Quét **BSL** trên old high / equal highs / PDH / session high | [[07 - Buy-side Liquidity]] | Giá reclaim xuống dưới mức + displacement down + MSS bearish |
| TS tại PDH/PDL | Hai chiều | Previous Day High / Low | ERL ngày | Quét PDH→short; quét PDL→long |
| TS tại Equal Highs/Lows | Hai chiều | Hai+ đỉnh/đáy bằng nhau | Pool tập trung, "magnet" | Quét hết equal levels rồi reclaim |
| TS tại Session H/L | Hai chiều | Asia/London/NY high-low | Thanh khoản phiên | Trong kill zone kế tiếp ([[18 - Kill Zones]]) |
| TS tại Swing High/Low cũ | Hai chiều | Swing point rõ trên HTF | ERL cấu trúc | Reclaim swing point + MSS |

### Khi nào giá trị cao?
- [ ] Mức bị quét là **rất hiển nhiên** (PDH/PDL, equal highs/lows, đỉnh/đáy tuần) — chứa nhiều thanh khoản.
- [ ] Cú quét diễn ra trong **[[18 - Kill Zones]]** (London / NY AM) chứ không phải giờ chết.
- [ ] Hướng Turtle Soup **trùng [[12 - Daily Bias]]** và HTF structure.
- [ ] Quét xảy ra tại vùng [[27 - Premium Discount]] đúng phe (quét SSL ở discount để long; quét BSL ở premium để short).
- [ ] Có **displacement rõ** + **MSS** ngay sau cú quét (xem [[Displacement]], [[21 - Market Structure Shift]]).
- [ ] Cú quét để lại **[[Fair Value Gap]]** hoặc [[Order Block]] làm entry refinement.

### Khi nào bỏ qua?
- [ ] Giá **đóng cửa chấp nhận** ngoài mức (real breakout) — không reclaim.
- [ ] Không có displacement ngược chiều, chỉ là wick yếu rồi đi sideway.
- [ ] Hướng setup **ngược [[12 - Daily Bias]]** mạnh trên HTF.
- [ ] Mức bị quét không phải mức hiển nhiên (không ai nhìn thấy → ít thanh khoản → ít ý nghĩa).
- [ ] Tin tức lớn / spread giãn / ngoài kill zone.
- [ ] Còn quá nhiều thanh khoản chưa quét phía xa hơn (giá có thể đi tiếp tới đó trước).

---

## 3. Cấu trúc nhận diện trên chart

### Dấu hiệu chính
1. **Mức target rõ ràng**: một old high/low, equal highs/lows, PDH/PDL hoặc session H/L mà thị trường "nhìn thấy".
2. **Cú quét (sweep)**: giá nhú **qua** mức đó — tạo wick/đuôi dài, lấy thanh khoản.
3. **Từ chối (rejection)**: giá **không đóng cửa chấp nhận** ngoài mức; quay đầu nhanh.
4. **Reclaim**: giá đóng cửa trở lại **bên trong** range (vượt lại mức vừa phá theo chiều ngược).
5. **Displacement**: một đoạn dịch chuyển mạnh, có động lượng, ngược chiều cú quét (thường để lại FVG).
6. **MSS / CHoCH**: phá vỡ cấu trúc vi mô trên khung thấp xác nhận đảo chiều ([[21 - Market Structure Shift]], [[09 - Change of Character]]).

### Ma trận nhận diện
| Yếu tố | Turtle Soup hợp lệ | Mơ hồ / yếu | ⚠️ Cảnh báo real breakout |
|---|---|---|---|
| Đóng cửa qua mức | Wick qua, **thân đóng trong range** | Đóng sát ngay ngoài mức | **Thân đóng dứt khoát ngoài mức (acceptance)** |
| Tốc độ phản ứng | Reclaim nhanh, dứt khoát | Reclaim chậm, do dự | Không reclaim — retest mức như S/R mới |
| Displacement | Mạnh, ngược chiều quét, để lại FVG | Yếu, không FVG rõ | Mạnh **cùng chiều** cú phá |
| MSS khung thấp | Có, rõ ràng | Chỉ minor structure | Không có; structure tiếp diễn cùng chiều phá |
| Mức bị quét | External/hiển nhiên | Mức nội bộ nhỏ | Phá xong tạo loạt high/low mới cao hơn |
| Context bias | Trùng [[12 - Daily Bias]] | Trung tính | Ngược lại — giá đang trending mạnh qua mức |

### Điều kiện
**Bắt buộc:**
- Có một mức thanh khoản hiển nhiên bị quét.
- Giá **reclaim** lại mức (không acceptance ngoài).
- Có **displacement** + **MSS** ngược chiều cú quét.

**Tăng xác suất:**
- Quét trong [[18 - Kill Zones]], đúng vùng [[27 - Premium Discount]].
- Trùng [[12 - Daily Bias]] và HTF POI ([[Order Block]] / [[Fair Value Gap]] HTF).
- Quét **equal highs/lows** (pool dày) hoặc PDH/PDL.
- Để lại FVG sạch để entry/refine.

**Làm yếu đi:**
- Ngoài kill zone, gần tin tức.
- Mức bị quét không hiển nhiên.
- Reclaim yếu, không có FVG, MSS mơ hồ.
- Còn thanh khoản lớn chưa quét ở xa hơn cùng chiều.

---

## 4. Quy trình phân tích đa khung thời gian

### D1 / H4 — Context & Bias
- Xác định [[12 - Daily Bias]]: hôm nay nghiêng long hay short?
- Đánh dấu các **mức external hiển nhiên**: PDH/PDL, weekly H/L, equal highs/lows, swing cũ → đây là *mục tiêu* của cú quét.
- Xác định [[27 - Premium Discount]] của [[12 - Dealing Range]]: ta muốn long từ discount sau khi quét SSL; short từ premium sau khi quét BSL.

### H1 / M15 — Định vị setup
- Chờ giá tiến tới mức đã đánh dấu (giá thường được [[15 - Inducement]] kéo về).
- Quan sát cú **quét đầu tiên**: giá có nhú qua mức rồi từ chối không?
- Khoanh vùng FVG/OB hình thành ngay sau cú quét làm vùng entry tiềm năng.

### M5 / M1 — Trigger & Entry
- Chờ **displacement** + **MSS** xác nhận đảo chiều ([[21 - Market Structure Shift]]).
- Vào lệnh sau reclaim: hoặc market sau MSS, hoặc limit tại [[Fair Value Gap]] / [[Order Block]] của đoạn displacement ([[Optimal Trade Entry]]).
- Stop **bên kia cực trị cú quét** (ngoài wick). Target: thanh khoản đối diện / về trong range.

```text
--- TURTLE SOUP LONG (quick note) ---
HTF bias: BULLISH (D1/H4)
Mức quét: PDL / equal lows / SSL @ [level]
Premium/Discount: giá ở DISCOUNT khi quét  -> OK
Sequence: quét SSL -> reject -> reclaim len tren [level]
          -> displacement UP (FVG @ [range]) -> MSS bullish M5/M1
Entry: limit tai FVG [range]  (hoac market sau MSS)
Stop : duoi swing low cua cu quet  @ [level] - buffer
TP1  : ve trong range / FVG gan @ [level]
TP2  : BSL / PDH doi dien @ [level]
Confidence: __/5   | Kill zone: London/NY AM
```

```text
--- TURTLE SOUP SHORT (quick note) ---
HTF bias: BEARISH (D1/H4)
Mức quét: PDH / equal highs / BSL @ [level]
Premium/Discount: giá ở PREMIUM khi quét  -> OK
Sequence: quét BSL -> reject -> reclaim xuong duoi [level]
          -> displacement DOWN (FVG @ [range]) -> MSS bearish M5/M1
Entry: limit tai FVG [range]  (hoac market sau MSS)
Stop : tren swing high cua cu quet  @ [level] + buffer
TP1  : ve trong range / FVG gan @ [level]
TP2  : SSL / PDL doi dien @ [level]
Confidence: __/5   | Kill zone: London/NY AM
```

> [!warning] Đừng trade cú phá — trade phản ứng sau cú phá
> Sai lầm chết người là vào lệnh **ngay khi giá đang nhú qua mức** vì sợ lỡ. Tại thời điểm đó bạn không biết là sweep hay breakout thật. **Hãy chờ reclaim + displacement + MSS** rồi mới vào. Bạn giao dịch *phản ứng* của giá với mức, không phải bản thân cú chạm mức.

---

## 5. Quy tắc xác nhận / vô hiệu hóa

**Xác nhận (vào lệnh khi đủ):**
- [ ] Mức hiển nhiên bị quét (wick qua, không acceptance).
- [ ] Giá reclaim lại trong range.
- [ ] Displacement ngược chiều cú quét, để lại FVG.
- [ ] MSS / CHoCH trên khung entry.
- [ ] Trùng [[12 - Daily Bias]] + vùng [[27 - Premium Discount]] đúng phe.

**Vô hiệu hóa (huỷ setup khi):**
- [ ] Giá **đóng cửa chấp nhận** ngoài mức (chuyển thành real breakout).
- [ ] Không có MSS sau cú quét trong thời gian hợp lý.
- [ ] Reclaim thất bại — giá quét tiếp xuống/lên xa hơn không quay lại.
- [ ] Sau entry: giá đóng cửa **vượt cực trị cú quét** (stop logic, không chỉ chạm wick).

### Turtle Soup thành công vs Real breakout
| Đặc điểm | Turtle Soup (đảo chiều) | Real Breakout (tiếp diễn) |
|---|---|---|
| Đóng cửa qua mức | Không acceptance, wick reject | Acceptance, thân đóng ngoài |
| Reclaim | Có, nhanh | Không |
| Displacement | Ngược chiều cú phá | Cùng chiều cú phá |
| MSS | Có (đảo chiều) | Không (BOS cùng chiều — xem [[Break of Structure]]) |
| Hành động | Fade cú phá | Theo cú phá / đứng ngoài |

> [!note] Double sweep (quét kép)
> Đôi khi smart money quét **hai lần**: nhú qua mức → kéo lại dụ → nhú sâu hơn lần hai mới đảo. Nếu lần đầu reclaim yếu rồi giá quét sâu hơn, **đừng vội** — chờ cú quét cuối cùng + MSS. Equal lows/highs đặc biệt hay bị double sweep vì pool quá dày.

---

## 6. Ví dụ chart

### Ví dụ ĐÚNG
![[TurtleSoup-Example-Correct.png]]
**Mô tả:** Turtle Soup Long tại PDL/equal lows trong NY AM kill zone, đúng [[12 - Daily Bias]] bullish.
- Giá tiến về cụm **equal lows** (SSL hiển nhiên) — đám đông đặt stop dưới đó.
- Cú quét nhú **qua** equal lows tạo wick dài @ [level], **không đóng cửa chấp nhận** bên dưới.
- Giá **reclaim** nhanh lên trên mức + **displacement up** mạnh để lại [[Fair Value Gap]] @ [range].
- **MSS bullish** trên M5/M1 xác nhận đảo chiều.
- Entry limit tại FVG [range], stop dưới wick @ [level], TP về BSL đối diện @ [level].

### Ví dụ SAI
![[TurtleSoup-Example-Wrong.png]]
**Mô tả:** Vào lệnh fade một cú phá hoá ra là **real breakout** — bài học không reclaim.
- Giá phá đỉnh nhưng **đóng cửa chấp nhận** (thân nến) ngoài mức → đây là acceptance.
- Không có reclaim, không MSS đảo chiều; thay vào đó là **BOS** cùng chiều ([[Break of Structure]]).
- Trader vào short "đoán đỉnh" vì thấy giá lên cao → bị cuốn theo continuation, stop bị quét.
- Bài học: **chờ reclaim + displacement + MSS**, không fade một breakout còn đang có acceptance.

### Giải phẫu (tuỳ chọn)
![[TurtleSoup-Anatomy.png]]
**Mô tả:** Sơ đồ tuần tự: `Mức hiển nhiên → Quét (sweep) → Reject → Reclaim → Displacement (+FVG) → MSS → Entry → Target`.

---

## 7. Entry model liên quan

- [[20 - Liquidity Sweep]] — khái niệm gốc; Turtle Soup là ứng dụng đảo chiều của nó tại mức external.
- [[21 - Market Structure Shift]] — tín hiệu xác nhận đảo chiều sau cú quét.
- [[09 - Change of Character]] — CHoCH khung vi mô đi kèm.
- [[Fair Value Gap]] / [[Order Block]] — vùng refine entry sau displacement.
- [[Optimal Trade Entry]] — fib refinement của đoạn displacement để vào.
- [[Displacement]] — động lượng xác nhận có "ý định" đảo chiều.
- [[12 - Daily Bias]] + [[27 - Premium Discount]] — bộ lọc context.
- [[15 - Inducement]] — thanh khoản "mồi" thường nằm trước mức bị quét.
- [[16 - Internal & External Range Liquidity (IRL & ERL)]] — Turtle Soup quét ERL để vào, chạy tới IRL/ERL đối diện.

```text
--- SEQUENCE: TURTLE SOUP LONG ---
SSL (equal lows/PDL) -> sweep -> reject -> reclaim
   -> displacement UP -> FVG/OB -> MSS bullish
   -> ENTRY (limit @ FVG / market sau MSS)
   -> SL duoi wick cu quet | TP -> BSL doi dien

--- SEQUENCE: TURTLE SOUP SHORT ---
BSL (equal highs/PDH) -> sweep -> reject -> reclaim
   -> displacement DOWN -> FVG/OB -> MSS bearish
   -> ENTRY (limit @ FVG / market sau MSS)
   -> SL tren wick cu quet | TP -> SSL doi dien
```

> [!note] Liên hệ ICT 2022 Model
> Turtle Soup chính là *bước khởi động* của [[ICT 2022 Model]]: **(1) Liquidity Sweep → (2) MSS → (3) FVG retrace → (4) Entry → (5) Target opposite liquidity**. Có thể coi Turtle Soup là tên gọi nhấn mạnh *điểm sweep tại mức hiển nhiên* trong chuỗi đó.

---

## 8. Checklist trước khi áp dụng vào trade

> [!warning] Không tick đủ → KHÔNG vào lệnh. Turtle Soup sai = bắt dao rơi.

**A. Context**
- [ ] [[12 - Daily Bias]] đã xác định và setup **trùng** hướng bias.
- [ ] Mức bị nhắm là **external/hiển nhiên** (PDH/PDL, equal H/L, swing cũ).
- [ ] Giá ở đúng vùng [[27 - Premium Discount]] cho hướng lệnh.
- [ ] Đang trong [[18 - Kill Zones]], không sát tin tức lớn.

**B. Execution**
- [ ] Đã thấy **sweep** (wick qua mức, không acceptance).
- [ ] Đã thấy **reclaim** vào range.
- [ ] Đã thấy **displacement** + **FVG/OB**.
- [ ] Đã thấy **MSS / CHoCH** khung entry.
- [ ] Entry, SL (ngoài cực trị cú quét), TP (thanh khoản đối diện) đều xác định trước.
- [ ] Rủi ro ≤ 0.5% tài khoản; RR ≥ 1:2.

**C. "Không có lệnh" nếu:**
- [ ] Giá có **acceptance** ngoài mức (real breakout).
- [ ] Không có MSS / displacement rõ.
- [ ] Setup ngược bias HTF mạnh.
- [ ] Mức bị quét không hiển nhiên / ít thanh khoản.

---

## 9. Lỗi thường gặp

| Lỗi | Dấu hiệu | Vì sao nguy hiểm | Cách sửa |
|---|---|---|---|
| Fade breakout thật | Vào ngược một cú phá có acceptance | Đánh ngược continuation → bị quét stop | Chờ **reclaim**; nếu thân đóng ngoài mức thì bỏ |
| Vào quá sớm (lúc đang nhú) | Mua/bán ngay khi giá chạm mức | Chưa biết là sweep hay breakout | Chờ reclaim + displacement + MSS |
| Bỏ qua MSS | Không kiểm tra structure khung thấp | Đảo chiều chưa được xác nhận | Bắt buộc có MSS/CHoCH mới vào |
| Stop quá sát wick | Đặt SL ngay sát đỉnh/đáy quét | Bị double sweep quét nốt | Đặt SL ngoài cực trị + buffer; lường double sweep |
| Quét mức không hiển nhiên | Mức nội bộ nhỏ, ít người thấy | Ít thanh khoản → tín hiệu yếu | Chỉ chọn PDH/PDL, equal H/L, swing rõ |
| Ngược bias HTF | Long khi D1 bearish mạnh | Đánh ngược dòng tiền lớn | Lọc bằng [[12 - Daily Bias]] trước |
| Bỏ qua Premium/Discount | Long ở premium, short ở discount | Vào sai phe của range | Long từ discount, short từ premium |
| Tham target | Bỏ TP1 chờ TP2 luôn | Cho lợi nhuận quay đầu | Chốt một phần tại thanh khoản gần |

---

## 10. Câu hỏi tự kiểm tra
1. Cú phá vỡ này có **acceptance** ngoài mức không, hay chỉ là wick rồi reclaim?
2. Mức bị quét có thực sự **hiển nhiên / external** (chứa thanh khoản) không?
3. Sau cú quét có **displacement + MSS** ngược chiều chưa?
4. Hướng setup có trùng [[12 - Daily Bias]] và đúng [[27 - Premium Discount]] không?
5. Stop của tôi có nằm ngoài cực trị cú quét (lường double sweep) không?
6. Nếu đây hoá ra là real breakout, dấu hiệu vô hiệu hoá của tôi là gì?
7. Target là thanh khoản đối diện nào (BSL/SSL/PDH/PDL)?

---

## 11. Flashcards / Active Recall
- **Q1.** Turtle Soup về bản chất là gì theo ngôn ngữ ICT?
  - *A:* Một [[20 - Liquidity Sweep]] của mức external/hiển nhiên, dùng làm entry đảo chiều (false breakout reversal).
- **Q2.** Điều kiện duy nhất biến một cú phá thành Turtle Soup thay vì breakout thật?
  - *A:* Giá **reclaim** lại mức (không acceptance ngoài) + **displacement + MSS** ngược chiều.
- **Q3.** Turtle Soup Long quét loại thanh khoản nào, ở đâu?
  - *A:* Quét **SSL** dưới old low / equal lows / PDL / session low.
- **Q4.** Stop của Turtle Soup đặt ở đâu và vì sao?
  - *A:* Ngoài **cực trị cú quét** + buffer, để tránh bị double sweep quét nốt.
- **Q5.** Vì sao không được vào lệnh ngay lúc giá đang nhú qua mức?
  - *A:* Vì lúc đó chưa phân biệt được sweep và real breakout; phải chờ phản ứng (reclaim + MSS).
- **Q6.** Turtle Soup khớp vào bước nào của [[ICT 2022 Model]]?
  - *A:* Bước sweep/MSS mở đầu: Sweep mức hiển nhiên → MSS → FVG retrace → entry → target.

---

## 12. Lesson Learned
> [!note]
> - (Điền sau mỗi trade dùng Turtle Soup) Cú quét có acceptance hay không? Mình có chờ MSS không?
> - Mức bị quét có hiển nhiên thật không, hay mình tự vẽ ra?
> - Stop có bị double sweep quét không — lần sau nới buffer thế nào?
> - Link tới trade: [[ ]] | Link tới [[Mistake - ...]] nếu có lỗi.

---

## 13. Mức độ thành thạo
| Tiêu chí | Mức (1-5) | Ghi chú |
|---|---|---|
| Hiểu khái niệm | ___ | |
| Phân biệt false vs real breakout | ___ | |
| Nhận diện trên chart realtime | ___ | |
| Định vị entry/SL/TP đúng | ___ | |
| Lọc context (bias, P/D, kill zone) | ___ | |
| Kết quả backtest | ___ | |

**Kế hoạch ôn tập:**
- Backtest ≥ 30 cú Turtle Soup (cả đúng & sai) trên NQ1 / EURUSD, ghi vào [[04 - Backtesting]].
- Đối chiếu mỗi case với [[20 - Liquidity Sweep]] và [[21 - Market Structure Shift]].
- Review lại note này khi `confidence` lên ≥ 3; cập nhật `status` seed → developing → tested.

---

## Appendix — Turtle Soup Quick Reference Card

> [!abstract] Quick Reference (điền nhanh khi trade)
> **Hướng:** Long ☐ (quét SSL) / Short ☐ (quét BSL)
> **Mức bị quét:** PDH/PDL ☐ · Equal H/L ☐ · Session H/L ☐ · Swing cũ ☐ → @ [level]
> **Sweep:** wick qua, không acceptance? ☐
> **Reclaim:** đóng cửa lại trong range? ☐
> **Displacement + FVG:** @ [range] ☐
> **MSS / CHoCH:** ☐
> **Context:** Bias trùng ☐ · Premium/Discount đúng phe ☐ · Kill zone ☐
> **Entry:** [level] (FVG/OB / market sau MSS)
> **SL:** ngoài cực trị quét @ [level] (+buffer)
> **TP1:** trong range @ [level] · **TP2:** thanh khoản đối diện @ [level]
> **Risk:** ≤ 0.5% · **RR:** 1:____
> **Vô hiệu hoá:** acceptance ngoài mức / không MSS / reclaim thất bại
