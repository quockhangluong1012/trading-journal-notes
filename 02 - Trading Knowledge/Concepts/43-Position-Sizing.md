---
type: ict-concept
concept: Position Sizing
aliases:
  - Position Sizing
  - Risk Management
  - Khối lượng lệnh
  - Quản lý vốn
  - Lot sizing
tags:
  - trading/ict/concept
  - trading/study
  - "#risk-management"
  - "#prop-firm"
  - trading/deep-dive
status: seed
category: Risk Management
last_reviewed: 2026-07-05
created: 2026-07-05
updated: 2026-07-28
---

# Position Sizing

> [!summary] Tóm tắt 1 câu
> **Position Sizing là việc tính KHỐI LƯỢNG lệnh xuất phát từ SỐ TIỀN RỦI RO cố định trước — không bao giờ ngược lại. Khối lượng luôn là KẾT QUẢ của phép chia (risk $ ÷ stop × giá trị/điểm), không phải một con số bạn "chọn cho quen".**

> [!important] Nguyên tắc cốt lõi
> Trong ICT và trong prop firm, **quản lý rủi ro quan trọng hơn entry**. Một entry hoàn hảo với size sai vẫn có thể thổi bay tài khoản; một entry trung bình với size đúng thì sống sót. Vault này áp **≤0,5% rủi ro/lệnh** làm luật cứng. Câu thần chú: *"Risk quyết định Lot, không bao giờ Lot quyết định Risk."*

---

## 1. Định nghĩa

**Khái niệm:**
**Position Sizing** trả lời câu hỏi *"vào bao nhiêu?"* bằng cách cố định trước **số tiền tối đa được phép mất** nếu lệnh chạm stop, rồi tính ngược ra khối lượng. Ba biến đầu vào: (1) **số tiền rủi ro** = vốn × % rủi ro; (2) **khoảng cách stop** = |entry − stop loss| (do cấu trúc chart quyết định); (3) **giá trị mỗi điểm/pip** của sản phẩm.

**Vì sao đây là kỹ năng số 1 của prop trader:** Bài thi prop firm không thưởng người lãi nhiều nhất — nó loại người **vi phạm giới hạn rủi ro**. Daily loss limit và max drawdown là những "lằn ranh tử thần"; chạm là fail ngay lập tức bất kể lãi trước đó. Position sizing đúng biến các giới hạn này thành **gần như bất khả xâm phạm**.

![[PositionSize-Advanced-Formula.svg|697]]

*Công thức: Khối lượng = Số tiền rủi ro ÷ (Khoảng cách Stop × Giá trị mỗi điểm). Bắt đầu từ risk $ (hằng số của bạn), stop do chart quyết, giá trị/điểm là hằng số theo sản phẩm.*

**Nó giúp trả lời câu hỏi nào?**
- Với stop này, tôi được vào **bao nhiêu lot/contract** để không quá 0,5%?
- Nếu chuỗi thua xảy ra, tôi còn sống sót đến khi edge thể hiện không?
- Size này có an toàn dưới **mọi** giới hạn prop firm (daily + overall + consistency) không?

### Position Sizing KHÔNG phải là gì
- **Không phải** chọn lot theo cảm giác ("2 lot cho quen") rồi đặt stop sau.
- **Không phải** tối đa hóa lợi nhuận mỗi lệnh — mà là **tồn tại lâu dài**.
- **Không phải** cố định lot; nó **thay đổi mỗi lệnh** theo khoảng cách stop.
- **Không** dùng để "gỡ" — tăng size sau thua (martingale) là con đường phá sản chắc chắn.

---

## 2. Công thức lõi & 3 biến

Công thức tổng quát:

```text
Số tiền rủi ro = Vốn × % rủi ro mỗi lệnh
Khối lượng     = Số tiền rủi ro ÷ (Khoảng cách Stop × Giá trị mỗi điểm/pip)
```

**Biến 1 — Số tiền rủi ro (FIX trước):** đây là hằng số của bạn. Vault dùng ≤0,5%. Với tài khoản $100.000 → **$500/lệnh**. Đây là con số bạn quyết **trước khi nhìn chart**.

**Biến 2 — Khoảng cách Stop (do cấu trúc):** ICT đặt stop theo **logic chart** — dưới/trên wick của cú sweep, ngoài POI, ngoài swing tạo MSS/CISD. **Không** ép stop nhỏ lại để vào lot to; stop nhỏ là **hệ quả** của entry tốt (OTE, 50% CE của FVG), không phải mục tiêu.

**Biến 3 — Giá trị mỗi điểm/pip (hằng số sản phẩm):**

| Sản phẩm | Đơn vị | Giá trị |
|---|---|---|
| **NQ** (E-mini Nasdaq) | 1 điểm | **$20** / contract (tick 0,25 = $5) |
| **MNQ** (Micro) | 1 điểm | **$2** / contract |
| **EURUSD / GBPUSD** | 1 pip (0,0001) | **$10** / 1,0 lot ($1 / 0,1 lot; $0,10 / 0,01 lot) |
| **XAUUSD** | $1 giá vàng | **$100** / 1,0 lot ($1 / 0,01 lot) |

> [!tip] Luôn ROUND DOWN
> Khi phép chia ra số lẻ (vd 1,25 contract), **luôn làm tròn XUỐNG** (1 contract). Round up = vượt rủi ro cho phép. Dùng micro (MNQ, 0,01 lot) khi cần độ mịn để bám sát 0,5%.

---

## 3. Ví dụ tính cụ thể (tài khoản $100k, risk 0,5% = $500)

> [!example] NQ / NAS100
> Stop = **20 điểm**. Giá trị = $20/điểm.
> Contracts = 500 ÷ (20 × 20) = 500 ÷ 400 = **1,25** → **vào 1 contract** (risk thực $400).
> Cần độ mịn hơn? Dùng **MNQ**: 500 ÷ (20 × 2) = 12,5 → **12 micro** (risk $480, sát 0,5% hơn).

> [!example] EURUSD
> Stop = **20 pip**. Giá trị = $10/pip/lot.
> Lots = 500 ÷ (20 × 10) = **2,5 lot**. Nếu stop = 25 pip → 500 ÷ 250 = **2,0 lot**.
> → Stop rộng hơn ⇒ lot nhỏ hơn. Rủi ro $ luôn giữ nguyên $500.

> [!example] XAUUSD
> Stop = **$3,00** (300 "pip" 0,01). Giá trị = $100/$1/lot.
> Lots = 500 ÷ (3 × 100) = **1,67 lot**. Nếu stop = $5,00 → 500 ÷ 500 = **1,0 lot**.

Xem thêm chi tiết pip/lot/leverage tại [[36 - Forex CFD Basics ( Pip, Lot, Spread, Swap, Leverage, Margin )]]. Bạn cũng có thể dùng máy tính khối lượng có sẵn:

![[ForexBasics-PositionSize-Calculator-Screenshot.png|697]]

---

## 4. Toán học sống sót — vì sao 0,5%/lệnh

![[PositionSize-Advanced-DrawdownMath.svg|697]]

Chuỗi thua **chắc chắn** xảy ra — kể cả với hệ thống thắng 60%, xác suất thua 6–8 lệnh liên tiếp trong 100 lệnh là rất cao. Rủi ro nhỏ giữ bạn sống qua chuỗi thua để edge có thời gian thể hiện.

**Sụt vốn sau 10 lệnh thua liên tiếp:**
- 0,5%/lệnh → chỉ **−4,9%** (thừa an toàn dưới mọi limit prop firm).
- 2%/lệnh → **−18,3%**.
- 5%/lệnh → **−40,1%** (gần như fail ngay).

**Toán học phục hồi (bất đối xứng):** mất càng sâu, càng khó về bờ.

| Sụt vốn | Cần lãi để hòa |
|---|---|
| −10% | +11,1% |
| −20% | +25,0% |
| −30% | +42,9% |
| −50% | +100% |
| −70% | +233% |

> [!info] Kết luận then chốt
> Drawdown **không tuyến tính** — mất 50% cần gấp đôi để về bờ. Vì thế **phòng thủ vốn quan trọng hơn tối đa hóa lợi nhuận**. Rủi ro nhỏ = tồn tại lâu = edge có thời gian sinh lời. Đây chính là lý do toán học của luật ≤0,5%/lệnh trong vault.

---

## 5. Prop Firm — chồng giới hạn phải vượt qua tất cả

![[PositionSize-Advanced-PropFirmStack.svg|697]]

> [!warning] Con số chỉ mang tính minh họa
> Mỗi prop firm có bộ rule riêng và **thay đổi theo thời gian** — luôn đọc kỹ tài liệu của firm bạn thi. Dưới đây là các *loại* ràng buộc phổ biến trên tài khoản $100k.

Size của bạn bị giới hạn bởi **ràng buộc chặt nhất** trong nhóm sau:

- **Max Overall Loss / Trailing Drawdown (~$6k–$10k):** chạm = fail tài khoản. Ràng buộc tối thượng. Lưu ý **trailing** DD tính từ **đỉnh balance**, không phải vốn ban đầu — càng lãi, "sàn" càng nâng lên.
- **Daily Loss Limit (~$5k / 5%):** chạm trong một ngày = fail; reset mỗi ngày. Đây là lý do phải có **circuit breaker cá nhân** dừng sớm hơn nhiều.
- **Profit Target (~8–10%):** cần đạt để pass — nhưng **đừng vội**; về gần đích thì **giảm** size để bảo vệ, không tăng.
- **Consistency Rule (1 ngày ≤ ~30–40% tổng lãi):** cấm kiểu "một lệnh ăn cả" → buộc size **đều và nhỏ** qua nhiều ngày.

> [!tip] Vì sao 0,5% khiến prop firm "dễ thở"
> Với $500 risk/lệnh, bạn cần **10 lệnh thua liên tiếp** mới chạm daily limit $5k — điều gần như bất khả nếu có circuit breaker dừng ở −2%/ngày. Size nhỏ biến daily limit từ "lằn ranh tử thần" thành "hàng rào ở rất xa".

---

## 6. Fixed Fractional vs Fixed Dollar

![[PositionSize-Advanced-Fixed-vs-Percent.svg|697]]

**% cố định (Fixed Fractional):** risk $ = balance × %. Risk co giãn theo vốn — thắng thì risk $ tăng (lãi kép), thua thì risk $ giảm (tự bảo vệ). Phù hợp **tài khoản cá nhân dài hạn**. Vault dùng cái này (≤0,5% × balance).

**$ cố định (Fixed Dollar):** risk $ là con số cố định (vd $500) bất kể balance. Đơn giản, dễ soi giới hạn, **hợp giai đoạn thi prop firm** (nơi limit là $ tuyệt đối). Nhược điểm: không tự giảm khi drawdown sâu → cần circuit breaker thủ công.

> [!note] Gợi ý thực chiến
> Trong pha thi prop firm, dùng **Fixed Dollar nhỏ** (vd 0,25–0,5% của balance khởi điểm) để dễ kiểm soát limit tuyệt đối. Sau khi funded và rút vốn ổn định, chuyển sang **% cố định** để tận dụng lãi kép.

---

## 7. Quy trình sizing trước mỗi lệnh (5 bước)

**Bước 1 — Xác định risk $ (trước khi nhìn setup).** Balance × % (vd $100k × 0,5% = $500). Đây là hằng số hôm nay.

**Bước 2 — Tìm entry & stop theo cấu trúc.** Entry tại OTE/50% CE FVG/OB; stop sau wick sweep hoặc ngoài POI. Đo khoảng cách stop (điểm/pip).

**Bước 3 — Tra giá trị mỗi điểm/pip** của sản phẩm (bảng mục 2).

**Bước 4 — Tính lot & round DOWN.** Lot = risk $ ÷ (stop × giá trị/điểm). Làm tròn xuống. Dùng micro nếu cần độ mịn.

**Bước 5 — Kiểm tra chồng giới hạn.** Lệnh này + các lệnh mở khác có vượt daily budget không? Có vi phạm consistency không? Nếu nghi ngờ → giảm size hoặc bỏ qua.

---

## 8. Ví dụ

### Ví dụ đúng
> [!success] Sizing chuẩn
> Tài khoản $100k, risk $500. Setup NQ long: entry 20.000, stop 19.980 (**20 điểm** dưới wick sweep), target 20.060 (RR 3:1). Contracts = 500 ÷ (20×20) = 1,25 → **vào 1 contract** (risk $400). Nếu chạm stop mất $400 (0,4%); nếu đạt target lãi ~$1.200 (1,2%). **Risk đã fix trước khi vào**, lot là kết quả.

> [!note] Ảnh chart/nhật ký thực tế (dán của bạn)
> ![[paste-image-here.png]]
> *Chụp lệnh thật: ghi rõ balance, % risk, risk $, khoảng cách stop, giá trị/điểm, số lot tính ra, và risk % thực tế sau khi round down.*

### Ví dụ sai
![[PositionSize-Example-Wrong.svg|697]]

**Ba sai lầm chết người:**
1. **Chọn lot trước rồi đặt stop** → stop rộng + lot to = rủi ro vượt xa 0,5%. *Sửa:* risk $ trước, suy ra lot.
2. **Dời/bỏ stop để "gồng"** → risk thực tế tăng vô hạn, một lệnh phá cả tháng. *Sửa:* stop là bất khả xâm phạm.
3. **Revenge / gấp đôi size để gỡ** → martingale = phá sản toán học, vi phạm daily limit ngay. *Sửa:* size cố định; dừng khi chạm circuit breaker.

---

## 9. Khái niệm liên quan

- [[36 - Forex CFD Basics ( Pip, Lot, Spread, Swap, Leverage, Margin )]] — nền tảng pip/lot/leverage
- [[26 - OTE - Optimal Trade Entry]] — entry tối ưu → stop nhỏ tự nhiên
- [[41 - Change in State of Delivery]] — logic đặt stop sau CISD/sweep
- [[42 - SMT Divergence]] — xác nhận setup để dám dùng đủ size
- [[18 - Kill Zones]] — chỉ chịu rủi ro trong giờ chất lượng

### Chuỗi tư duy sizing
```text
Balance → % risk (≤0,5%) → Risk $ → Entry+Stop (cấu trúc) → Stop distance → Value/point → Lot (round down) → Check limits
```

---

## 10. Thực hành tốt nhất (Best Practices)

> [!tip] 7 quy tắc Position Sizing
> 1. **Risk quyết định Lot** — luôn tính từ risk $, không bao giờ chọn lot trước.
> 2. **≤0,5%/lệnh** làm luật cứng; giảm còn 0,25% khi gần limit hoặc chuỗi thua.
> 3. **Stop theo cấu trúc, round lot XUỐNG** — không ép stop nhỏ để vào lot to.
> 4. **Circuit breaker cá nhân**: dừng sau −2%/ngày HOẶC 3 lệnh thua liên tiếp.
> 5. **Ngân sách rủi ro ngày/tuần**: tổng risk mở đồng thời không vượt giới hạn ngày.
> 6. **Về gần profit target thì GIẢM size** để bảo vệ, đừng tăng để "về đích nhanh".
> 7. **Không tương quan chồng chất**: NQ + ES + EURUSD long cùng lúc = 1 rủi ro USD lớn, không phải 3 rủi ro độc lập → tính gộp.

- Tính sẵn bảng "stop → lot" cho từng sản phẩm ở mức risk $ hôm nay, dán cạnh màn hình → quyết định trong 5 giây, không tính vội lúc lệnh chạy.
- Dùng **micro contract / 0,01 lot** để bám sát 0,5% thay vì nhảy bậc thô.
- Ghi vào journal **risk % thực tế** (sau round down) của mỗi lệnh — đây là kỷ luật cốt lõi để [[01 - Dashboard]] Loss/Process phản ánh đúng.
- Tách bạch **risk mỗi lệnh** với **risk mỗi ngày** với **risk mỗi tuần** — ba tầng phanh khác nhau.
- Khi scale up tài khoản, giữ **cùng % risk**, để lãi kép tự tăng size — không nhảy % lên khi vừa thắng vài lệnh (hưng phấn = kẻ thù).

---

## 11. Checklist trước khi vào lệnh

> [!warning] Không bấm lệnh khi chưa tính xong size
> Size sai một lần có thể xóa nhiều tuần kỷ luật.

- [ ] Đã fix risk $ = balance × % (≤0,5%) TRƯỚC khi nhìn setup
- [ ] Entry & stop đặt theo **cấu trúc** (wick sweep / ngoài POI)
- [ ] Đã đo đúng khoảng cách stop (điểm/pip)
- [ ] Đã tra đúng giá trị mỗi điểm/pip của sản phẩm
- [ ] Lot = risk $ ÷ (stop × value); đã **round down**
- [ ] Risk % thực tế sau round down vẫn ≤ 0,5%
- [ ] Tổng risk các lệnh mở không vượt ngân sách ngày
- [ ] Không vi phạm consistency / daily limit prop firm
- [ ] Chưa chạm circuit breaker (−2%/ngày hoặc 3 thua)
- [ ] Không phải lệnh revenge / tăng size để gỡ

---

## 12. Lỗi thường gặp

| Lỗi | Dấu hiệu | Cách sửa |
|---|---|---|
| Chọn lot trước | "Vào 2 lot cho quen" | Fix risk $ trước → suy ra lot |
| Ép stop nhỏ để vào lot to | Stop sát entry vô lý | Stop theo cấu trúc; lot là hệ quả |
| Dời/bỏ stop | Nới stop khi lỗ | Stop bất khả xâm phạm; chấp nhận thua nhỏ |
| Round up | Làm tròn lên khi lẻ | Luôn round DOWN, dùng micro để mịn |
| Martingale/revenge | Gấp đôi size sau thua | Size cố định; dừng ở circuit breaker |
| Bỏ qua tương quan | Long NQ+ES+EUR cùng lúc | Tính gộp thành 1 rủi ro USD |
| Tăng size gần target | "Về đích cho nhanh" | Gần target thì GIẢM size |

---

## 13. Câu hỏi tự kiểm tra

- Tôi tính được số lot cho một stop 20 điểm NQ ở 0,5% trong 10 giây không?
- Vì sao khối lượng phải là kết quả, không phải lựa chọn?
- 10 lệnh thua ở 0,5% làm sụt bao nhiêu %? Ở 5% thì sao?
- Ràng buộc prop firm nào là "tối thượng"? Trailing DD tính từ đâu?
- Circuit breaker cá nhân của tôi là gì, và tôi có tuân thủ trong journal không?

---

## 14. Flashcards / Active Recall

### Q1
**Hỏi:** Công thức khối lượng?
**Đáp:** Lot = Risk $ ÷ (Khoảng cách Stop × Giá trị mỗi điểm/pip). Risk $ = Balance × % risk (≤0,5%).

### Q2
**Hỏi:** 10 lệnh thua liên tiếp ở 0,5%/lệnh làm sụt bao nhiêu vốn?
**Đáp:** Khoảng **−4,9%** — thừa an toàn dưới mọi giới hạn prop firm.

### Q3
**Hỏi:** Vì sao không được tăng size để gỡ sau chuỗi thua?
**Đáp:** Martingale khuếch đại drawdown theo cấp số nhân → phá sản toán học và vi phạm daily limit ngay lập tức.

---

## 15. Liên kết với Trade Journal

### Lệnh áp dụng đúng khái niệm này
```dataview
TABLE date, symbol, position, risk_percent, r_multiple, pnl
FROM ""
WHERE contains(file.outlinks, this.file.link)
SORT date DESC
```

### Lệnh mắc lỗi liên quan
```dataview
TABLE date, symbol, position, risk_percent, pnl, Mistake
FROM ""
WHERE contains(string(Mistake), this.file.name)
SORT date DESC
```

> [!note]
> Nếu vault dùng path riêng cho trades, thay `FROM ""` bằng ví dụ `FROM "05 - Live Trading Journal/Trades"`.

---

## 16. Nguồn tham khảo
- Kelly Criterion & fixed-fractional risk — nền tảng toán học quản lý vốn.
- ICT — risk management & đặt stop theo cấu trúc (sweep, POI).
- Tài liệu quy tắc các prop firm (daily loss, trailing drawdown, consistency) — đọc bản của firm bạn thi.
- Concept nội bộ: [[36 - Forex CFD Basics ( Pip, Lot, Spread, Swap, Leverage, Margin )]].

---

## 17. Mức độ thành thạo

| Tiêu chí | Điểm 1-5 | Ghi chú |
|---|---:|---|
| Thuộc công thức & 3 biến | | |
| Tính lot nhanh cho NQ/FX/XAU | | |
| Hiểu toán drawdown & phục hồi | | |
| Nắm chồng giới hạn prop firm | | |
| Tuân thủ trong trade thực tế | | |

**Kế hoạch review tiếp theo:**

---

# Phần mở rộng chuyên sâu (Deep Dive)

> [!info] Phần bổ sung 2026-07-28
> Khối này bổ sung: phân tích chuyên sâu, phản biện đa chiều, case study thực tế, và các edge case chỉ lộ ra khi live trade / backtest số lượng lớn. Đọc sau khi đã nắm phần lõi phía trên.

## A. Phân tích chuyên sâu

### A.1 Position sizing không phải "toán học tách biệt" — nó là điểm nối giữa order book và tài khoản

Nhìn từ góc microstructure, position sizing thường bị hiểu nhầm là một bài toán số học độc lập với hành vi thị trường ("cứ chia risk $ cho stop distance"). Thực ra ba biến trong công thức (risk $, stop distance, giá trị/điểm) đều bị **chi phối bởi cấu trúc sổ lệnh tại đúng thời điểm vào lệnh**, không phải các hằng số tĩnh:

- **Stop distance không phải một số cố định do bạn "chọn"** — nó là khoảng cách từ entry tới điểm mà, theo cấu trúc chart (wick sweep, ngoài POI), lệnh của bạn "phải sai" nếu giá đi tới đó. Nhưng khoảng cách này chỉ chính xác **tại đúng lúc bạn đọc chart** — spread, slippage tại thời điểm khớp lệnh (đặc biệt lúc thanh khoản mỏng) làm khoảng cách thực tế giữa entry filled và stop filled khác với khoảng cách lý thuyết trên chart.
- **Giá trị mỗi điểm/pip tưởng là hằng số sản phẩm, nhưng thực ra phụ thuộc vào loại lệnh và điều kiện khớp.** Với CFD, giá trị mỗi pip có thể thay đổi nhẹ nếu broker tính theo giá cross-rate biến động (với các cross không có USD trực tiếp); với futures, giá trị điểm là cố định theo hợp đồng (tick value) nhưng khối lượng khớp có thể bị giới hạn bởi thanh khoản hợp đồng tại các giờ ít giao dịch.
- **Risk $ là biến "sạch" nhất vì do trader tự quyết trước khi nhìn chart** — nhưng ngay cả biến này cũng phụ thuộc gián tiếp vào order book: nếu bạn định risk $500 nhưng cần vào 1.25 contract NQ và buộc phải round xuống 1 (do futures không chia nhỏ được như CFD/micro), risk $ thực tế đã bị lượng tử hoá (quantized) bởi kích thước hợp đồng nhỏ nhất — đây chính là lý do vault gốc khuyên dùng micro (MNQ) để giảm độ "nhảy bậc" này.

### A.2 Lăng kính ngoài-ICT — Kelly Criterion, fixed-fractional, và lý thuyết trò chơi lặp

Position sizing không phải một khái niệm riêng của ICT — nó là một nhánh của **quản lý vốn định lượng** (money management/bet sizing) đã tồn tại rất lâu trước ICT, với hai trường phái lớn:

**Kelly Criterion** (John Kelly, 1956, ban đầu cho lý thuyết thông tin và cờ bạc) đưa ra công thức tối ưu hoá **tốc độ tăng trưởng kỳ vọng theo logarithm của vốn** (log-utility) cho một canh bạc lặp lại có edge dương. Công thức cơ bản cho trò chơi nhị phân (thắng/thua):

```text
f* = p - q/b
```
trong đó `f*` = tỷ lệ vốn nên risk mỗi lần, `p` = xác suất thắng, `q = 1-p` = xác suất thua, `b` = tỷ lệ lãi/lỗ (RR — reward-to-risk). Ví dụ minh hoạ (không phải số liệu ICT thật): nếu một hệ thống có win-rate 50% và RR trung bình 2:1, `f* = 0.5 - 0.5/2 = 0.25` — Kelly đầy đủ gợi ý risk 25%/lệnh. Đây là mức **cực đoan** so với 0,5% mà vault gốc dùng.

**Fixed Fractional** (cách vault gốc dùng, ≤0,5%) không cố gắng tối ưu hoá tốc độ tăng trưởng lý thuyết — nó ưu tiên **kiểm soát variance và drawdown**, đặc biệt quan trọng khi (a) bạn không biết chắc `p` và `b` thật của hệ thống (chỉ có ước lượng từ mẫu backtest hữu hạn, luôn có sai số), và (b) tồn tại các giới hạn cứng bên ngoài hệ thống trading (daily loss limit, trailing drawdown của prop firm) mà Kelly gốc không tính đến.

**Điểm trùng khớp:** cả hai trường phái đều thống nhất về nguyên lý cốt lõi — kích thước vị thế phải là **hàm của edge và variance**, không phải một con số cảm tính; và cả hai đều cảnh báo risk quá cao (dù là "quá Kelly" hay "quá % tài khoản thoải mái") dẫn đến sụp đổ nhanh hơn tuyến tính.

**Điểm khác biệt quan trọng — sai số ước lượng edge:** Kelly đầy đủ giả định bạn biết CHÍNH XÁC `p` và `b` — một giả định hầu như không bao giờ đúng trong trading thật, vì mọi ước lượng win-rate/RR đều từ mẫu hữu hạn có nhiễu thống kê. Sai số nhỏ trong ước lượng `p` bị Kelly full **khuếch đại** thành sai số lớn trong `f*` (đây là lý do dân quant thực hành hầu như không bao giờ dùng Kelly đầy đủ — họ dùng **Half Kelly hoặc Quarter Kelly** để đánh đổi một phần growth rate lý thuyết lấy độ bền vững khi ước lượng edge sai). Fixed Fractional 0,5% của vault, dù không "tối ưu" theo nghĩa Kelly, gần với triết lý Quarter/Eighth Kelly cho các hệ thống có edge chưa được xác nhận chắc chắn — một lựa chọn hợp lý về mặt lý thuyết quản lý vốn, không chỉ là "thận trọng vì thận trọng".

![[PositionSize-DeepDive-KellyVsFractional.svg]]
*Minh hoạ dạng đường cong equity: Full Kelly tối ưu hoá growth rate lý thuyết nhưng biến động rất mạnh (nhạy với sai số ước lượng edge); Half Kelly giảm variance đáng kể; Fixed Fractional nhỏ (0,5%) cho đường equity êm nhất nhưng tăng trưởng chậm hơn về lý thuyết.*

### A.3 Toán học Risk-of-Ruin — vượt xa "sụt vốn sau N lệnh thua"

Mục 4 của phần lõi đã trình bày sụt vốn sau chuỗi thua liên tiếp (một phép tính đơn giản: `(1-r)^n`). Risk-of-ruin là một khái niệm rộng hơn: **xác suất tài khoản chạm mức "ruin"** (thường định nghĩa là mất một tỷ lệ vốn không thể phục hồi, ví dụ mất 100% hoặc chạm giới hạn tài khoản/prop firm) trước khi đạt một mục tiêu lãi nào đó, tính trên toàn bộ phân phối các kết quả có thể xảy ra — không chỉ kịch bản "thua liên tiếp N lần".

Công thức risk-of-ruin cổ điển (gambler's ruin, cho trò chơi nhị phân đơn giản với edge `p` và mỗi lần cược một đơn vị) là:

```text
Risk of Ruin ≈ ((1-edge)/(1+edge))^(vốn / đơn vị risk)
```

Diễn giải định tính (không gán số liệu cụ thể vì công thức đầy đủ phụ thuộc chi tiết vào phân phối RR thật của hệ thống, cần backtest riêng): risk-of-ruin **giảm theo cấp lũy thừa** khi số "đơn vị risk" mà vốn của bạn có thể chịu được tăng lên — tức khi risk%/lệnh giảm (mỗi đơn vị risk nhỏ hơn so với vốn), số đơn vị risk tăng, và risk-of-ruin giảm rất nhanh theo hàm mũ. Đây là lý do toán học sâu hơn của việc chọn 0,5% thay vì 2% hay 5%: không chỉ vì "sụt ít hơn sau 10 lệnh thua" — mà vì risk-of-ruin toàn cục (tính trên toàn bộ path có thể xảy ra, kể cả các path xấu hơn "10 lần thua liên tiếp" đơn giản) giảm theo cấp lũy thừa, không tuyến tính.

![[PositionSize-DeepDive-RiskOfRuin.svg]]
*Minh hoạ định tính: risk-of-ruin tăng phi tuyến (gần cấp lũy thừa) khi risk%/lệnh tăng — vùng 0,5% an toàn hơn rất nhiều so với mức tăng tuyến tính "gấp 4 lần risk = gấp 4 lần rủi ro" mà trực giác thường lầm tưởng.*

> [!tip] Cần backtest xác nhận
> Các con số cụ thể của risk-of-ruin (ví dụ "risk-of-ruin ở 0,5% là X%, ở 2% là Y%") phụ thuộc chặt vào win-rate và RR thật của hệ thống bạn đang dùng — đây là công thức cần bạn tự nhập tham số thật từ backtest, không nên tin vào bất kỳ con số phần trăm cụ thể nào không đi kèm nguồn hoặc giả định rõ ràng.

### A.4 Định lượng hoá — biến nào đo được, ngưỡng nào cần backtest

- **Biến đo được:** risk % thực tế mỗi lệnh (sau round down), R-multiple mỗi lệnh, drawdown tối đa (peak-to-trough), số lệnh thua liên tiếp tối đa quan sát được, risk % gộp khi có nhiều vị thế tương quan mở đồng thời, tần suất chạm circuit breaker cá nhân.
- **Ngưỡng nên backtest riêng cho hệ thống của bạn:** (1) ước lượng khoảng tin cậy của win-rate/RR từ tối thiểu 100+ mẫu (mẫu nhỏ hơn cho sai số ước lượng lớn, làm Kelly — nếu dùng — trở nên nguy hiểm); (2) đo drawdown tối đa thực tế đã xảy ra trong backtest so với drawdown lý thuyết ở các mức risk% khác nhau; (3) đo tỷ lệ % số ngày chạm circuit breaker cá nhân ở từng mức risk%/lệnh.
- **Thiết kế thí nghiệm backtest cho riêng position sizing:** chạy lại **cùng một chuỗi tín hiệu entry/exit** (giữ nguyên logic vào/ra) qua nhiều mức risk%/lệnh khác nhau (0,25% / 0,5% / 1% / 2%) và so sánh: (a) CAGR-tương-đương (tốc độ tăng trưởng), (b) max drawdown, (c) số lần chạm giới hạn prop-firm giả định, (d) Sharpe/Calmar ratio của đường equity. Tối thiểu nên có 100+ lệnh trong backtest gốc để các mức so sánh có ý nghĩa — dưới 30-50 lệnh, sự khác biệt giữa các mức risk% có thể chỉ là nhiễu.

### A.5 Tương tác & mâu thuẫn với các khái niệm ICT khác

- **Với [[26 - OTE - Optimal Trade Entry]]:** không mâu thuẫn, mà cộng sinh — entry tại OTE cho stop tự nhiên nhỏ hơn, làm tăng lot tính ra ở cùng risk $ cố định (RR đẹp hơn không đến từ "cố risk nhiều hơn" mà từ "stop nhỏ hơn"). Mâu thuẫn XUẤT HIỆN khi trader hiểu sai và ép entry gần OTE hơn mức cấu trúc cho phép chỉ để có stop nhỏ hơn, làm giảm chất lượng entry (tăng xác suất bị quét trước khi đảo thật) — đây là lỗi "ép stop nhỏ để vào lot to" nói ngược, tức "ép entry đẹp hơn giả tạo để có cớ risk nhiều hơn".
- **Với [[41 - Change in State of Delivery]]** (logic đặt stop sau CISD/sweep): stop distance trong công thức position sizing PHẢI xuất phát từ logic CISD/sweep này, không phải ngược lại. Mâu thuẫn khi trader tính lot trước (muốn vào N lot) rồi "nắn" stop cho vừa vặn — đây chính là sai lầm số 1 được note gốc liệt ở mục 12 ("Ép stop nhỏ để vào lot to").
- **Với Daily Bias / SMT Divergence (xác nhận setup):** một setup có nhiều confluence (SMT, đúng bias, đúng kill zone) KHÔNG nên tự động được risk cao hơn 0,5% — đây là một cạm bẫy phổ biến ("setup đẹp thì risk nhiều hơn chút cũng được"). Về mặt toán risk-of-ruin, việc thay đổi risk% theo "cảm giác tự tin" phá vỡ toàn bộ giả định của mô hình fixed-fractional (vốn giả định risk% cố định qua mọi lệnh) và làm biến dạng thống kê backtest (không còn so sánh táo với táo).
- **Với giới hạn chồng chất của prop firm (mục 5 phần lõi):** đây không phải mâu thuẫn mà là một **ràng buộc bổ sung lên trên** công thức toán học thuần — công thức risk$ = balance × % chỉ đúng khi không vi phạm daily loss/trailing DD; khi có nhiều lệnh mở cùng lúc hoặc gần cuối ngày đã lỗ, risk $ cho phép của lệnh mới phải được tính lại dựa trên **ngân sách còn lại trong ngày**, không phải công thức gốc áp dụng độc lập cho từng lệnh.

---

### A.6 Vì sao "round down" không chỉ là quy tắc an toàn — nó là điểm nối giữa toán liên tục và thực thi rời rạc

Công thức lot = risk$ ÷ (stop × value) cho một số thực (ví dụ 1,25 hoặc 2,67), nhưng thực thi trên thị trường futures chỉ cho phép các đơn vị hợp đồng nguyên (không có 1,25 contract NQ — chỉ có 1 hoặc 2). Đây là một dạng "lượng tử hoá" (quantization) rất giống với các bài toán tối ưu hoá rời rạc trong toán ứng dụng: giải pháp tối ưu liên tục (1,25 contract) không khả thi, và bạn phải chọn giữa hai lựa chọn rời rạc gần nhất (1 hoặc 2), mỗi lựa chọn tạo ra một risk % thực tế lệch khỏi mục tiêu lý thuyết theo hai hướng ngược nhau.

Luôn làm tròn XUỐNG (chọn 1 thay vì 2 trong ví dụ trên) đảm bảo risk thực tế **luôn ≤ risk mục tiêu**, không bao giờ vượt — đây là một quyết định bất đối xứng có chủ ý: chấp nhận risk% thực tế hơi thấp hơn lý thuyết (lãng phí một phần "hiệu quả" sử dụng vốn) để đổi lấy việc KHÔNG BAO GIỜ vượt giới hạn đã định. Với các tài khoản nhỏ (nơi 1 đơn vị hợp đồng đã chiếm tỷ trọng risk % lớn so với vốn), độ lượng tử hoá này trở nên nghiêm trọng — chính là lý do các sản phẩm micro (MNQ, MES, 0,01 lot forex) tồn tại: chúng giảm "bước nhảy" lượng tử hoá xuống 1/10 hoặc nhỏ hơn, cho phép risk % thực tế bám sát mục tiêu lý thuyết hơn nhiều.

### A.7 Mối liên hệ giữa position sizing và lý thuyết Martingale/Anti-Martingale trong quản lý vốn cờ bạc

Bên ngoài ICT, lý thuyết quản lý vốn cờ bạc/đầu tư phân loại các chiến lược sizing theo hai nhóm lớn: **Martingale** (tăng size sau khi thua, với hy vọng một lần thắng gỡ hết) và **Anti-Martingale** (tăng size sau khi thắng, giảm sau khi thua). Fixed fractional mà vault gốc dùng thực chất là một dạng **Anti-Martingale tự động** — vì risk $ = balance × %, sau một chuỗi thắng balance tăng nên risk $ tự tăng (dùng lãi để tăng size một cách có kiểm soát), và sau một chuỗi thua balance giảm nên risk $ tự giảm (tự bảo vệ, không cần can thiệp thủ công).

Điểm quan trọng cần phân biệt rõ: Anti-Martingale tự động qua % balance là AN TOÀN vì nó co giãn CÙNG HƯỚNG với vốn (thua nhiều → risk $ tự nhỏ lại); Martingale cổ điển (tăng size SAU KHI THUA để gỡ) là nguy hiểm vì nó co giãn NGƯỢC HƯỚNG với vốn (thua nhiều → risk $ tăng, đúng lúc vốn còn lại ít nhất để chịu đựng thêm rủi ro) — về bản chất toán học, Martingale cổ điển có kỳ vọng thắng cược tiến gần 100% trong ngắn hạn NHƯNG risk-of-ruin cũng tiến gần 100% nếu chuỗi thua đủ dài (một quy luật toán học không phụ thuộc vào edge của hệ thống bên dưới, chỉ phụ thuộc vào việc bạn có vốn hữu hạn và casino/thị trường có giới hạn kích thước cược tối đa).

### A.8 Vì sao position sizing là "kỹ năng" chứ không phải "kiến thức" — độ trễ giữa biết và làm

Một quan sát phổ biến ở trader mới (không phải số liệu thống kê, mà là hiện tượng hay được nhắc trong cộng đồng ICT dày dạn): hầu như ai cũng có thể trả lời đúng công thức tính lot trong một bài kiểm tra viết, nhưng tỷ lệ áp dụng đúng 100% trong live trading (đặc biệt lúc thị trường di chuyển nhanh, lúc vừa thua liên tiếp, hoặc lúc setup "quá đẹp") thấp hơn nhiều. Đây là lý do position sizing được xếp vào nhóm kỹ năng cần **rehearsal** (luyện tập lặp lại có ý thức) hơn là kiến thức một lần học là nhớ — tương tự cách một phi công luyện checklist trước cất cánh dù đã "biết" quy trình từ lâu.

Hàm ý thực chiến: việc có sẵn "bảng stop → lot" dán cạnh màn hình (như note gốc khuyến nghị ở mục 10) không chỉ là tiện lợi — nó là một công cụ **giảm tải nhận thức (cognitive load reduction)** tại đúng thời điểm áp lực cảm xúc cao nhất (giá đang chạy, cần quyết định nhanh), giúp quy trình đúng được thực thi mà không cần trader phải "tự tin toán học" ngay lúc đó.

## B. Phản biện & giới hạn — Devil's Advocate

**Falsifiability:** Bản thân công thức toán học của position sizing (`lot = risk$ / (stop × value)`) không phải một tuyên bố cần falsify — đó là đại số thuần, đúng theo định nghĩa. Điều CÓ THỂ và CẦN kiểm định là các tuyên bố định lượng gắn theo nó: "0,5%/lệnh là mức tối ưu", "10 lệnh thua liên tiếp ở 0,5% chỉ lỗ ~4,9%" — những con số này **đúng về toán học thuần** (là phép tính lãi kép đơn giản `(1-0.005)^10 - 1`), nhưng **"0,5% là mức tối ưu cho MỌI hệ thống"** thì không đúng tuyệt đối — mức risk% tối ưu phụ thuộc vào edge thật của hệ thống (theo Kelly) và mức chịu đựng drawdown tâm lý của từng trader, cả hai đều là biến riêng của từng người, không có một hằng số phổ quát.

**Giải thích thay thế đơn giản hơn:** Hiệu quả quan sát được của "risk thấp giúp trader tồn tại lâu hơn" có thể giải thích hoàn toàn bằng thống kê cơ bản của **variance của tổng các biến ngẫu nhiên** — không cần khung ICT hay bất kỳ trường phái trading cụ thể nào. Đây là một sự thật toán học áp dụng cho MỌI hệ thống cược có variance (casino, đầu tư, bảo hiểm) — không có gì đặc thù về ICT trong phần này của khái niệm; commodity hoá triệt để là đúng.

**Giới hạn thực dụng:**
- **Risk per trade khi spread giãn đột ngột** (rollover, tin tức, đầu phiên Á thanh khoản mỏng): công thức tính lot dựa trên stop distance TẠI THỜI ĐIỂM PHÂN TÍCH, nhưng nếu spread giãn mạnh vào lúc entry hoặc exit khớp lệnh, risk THỰC TẾ có thể vượt xa risk đã tính — công thức gốc không tự động điều chỉnh cho rủi ro thanh khoản này.
- **Gap qua đêm với các sản phẩm có phiên đóng/mở** (một số CFD, hoặc futures qua rollover): stop đặt trên chart không đảm bảo được khớp đúng giá đó nếu giá gap qua ngưỡng stop — công thức sizing giả định implicit rằng stop luôn được khớp gần đúng giá đặt, giả định này SAI khi có gap.
- **Prop firm daily drawdown tính theo nhiều kiểu khác nhau** (balance cố định đầu ngày vs equity đóng cửa hôm trước, như note gốc đã nêu ở phần lõi mục 5): một risk% "an toàn" theo tính toán của bạn có thể không an toàn nếu bạn tính nhầm mốc tham chiếu daily limit của đúng firm bạn đang thi.
- **Correlation risk khi vào nhiều cặp cùng chiều USD:** công thức sizing cho MỖI LỆNH riêng biệt hoàn toàn đúng về đại số, nhưng nếu áp dụng máy móc cho nhiều lệnh tương quan cao cùng lúc mà không tính gộp, tổng rủi ro thực tế của "danh mục" vượt xa tổng các risk% riêng lẻ cộng lại theo cách trader tưởng (không phải "1% + 1% = 2% độc lập" mà gần với "2% rủi ro trên MỘT nguồn biến động chung").

**Trả lời phản biện — phần nào trả lời được, phần nào phải chấp nhận là rủi ro mô hình:** Người dùng kỷ luật có thể trả lời phản biện về gap/spread bằng cách **luôn chừa biên an toàn** (risk % tính toán để dưới xa mức giới hạn cứng, không dán sát 0,5% vào đúng ngưỡng daily limit), và trả lời phản biện correlation bằng cách tính gộp risk theo nhóm tài sản tương quan (xem mục D). Nhưng có một phần **không trả lời được và phải chấp nhận như rủi ro mô hình**: risk-of-ruin dựa trên `p` và `b` ước lượng từ backtest — nếu hệ thống của bạn thay đổi hiệu suất thật ngoài mẫu (regime change, hoặc bạn drift khỏi kỷ luật entry), toàn bộ con số risk-of-ruin/Kelly tính trước đó không còn đúng, và **không có cách nào biết trước khi nào điều này xảy ra** — đây là lý do vì sao chọn risk% thấp hơn mức "tối ưu theo backtest" luôn là lựa chọn thận trọng hợp lý, một dạng bảo hiểm cho sai số mô hình không thể loại bỏ.

> [!warning] Kết luận phản biện
> - **Dùng được khi:** bạn đã có ước lượng edge (win-rate, RR) từ mẫu backtest đủ lớn (100+ lệnh), và risk% chọn thấp hơn đáng kể mức Kelly lý thuyết để chịu được sai số ước lượng.
> - **Vô dụng/nguy hiểm khi:** áp dụng công thức máy móc mà không tính gộp correlation risk, không chừa biên cho gap/spread giãn, hoặc dùng mức risk% "tối ưu theo backtest" mà không chiết khấu cho khả năng regime thay đổi.
> - **Không có mức risk% phổ quát đúng cho mọi người** — 0,5% là một lựa chọn thận trọng hợp lý cho môi trường prop firm với giới hạn cứng, không phải một hằng số toán học tuyệt đối.
> - **Đo lường để tự kiểm chứng:** log risk % thực tế mỗi lệnh (sau round down), drawdown tối đa thực tế theo thời gian, và số lần risk gộp (correlation) từng vượt dự tính.

---

## C. Case study

> [!note] Minh họa khái niệm, KHÔNG phải dữ liệu giao dịch thật.

### Case 1 — Thắng đẹp: sizing chuẩn qua chuỗi 3 lệnh liên tiếp trên NQ (case tổng hợp từ backtest)

**Bối cảnh:** Tài khoản demo/backtest $100.000, risk cố định 0,5% ($500/lệnh), giao dịch NQ1 trong 3 phiên NY liên tiếp trong một tuần thi prop firm giả định.

**Diễn biến từng bước:** Phiên 1: setup long tại OTE + FVG, stop 18 điểm dưới wick sweep. Contracts = 500 ÷ (18×20) = 1,39 → vào 1 contract (risk thực $360). Lệnh đạt target 1:3, lãi ~$1.080. Phiên 2: setup short, stop 25 điểm, dùng MNQ cho độ mịn: 500 ÷ (25×2) = 10 micro (risk $500 chẵn). Đạt target 1:2.5, lãi ~$1.250. Phiên 3: setup long tiếp theo bias tuần, stop 15 điểm (entry đẹp hơn, gần OTE), Contracts = 500 ÷ (15×20) = 1,67 → 1 contract (risk $300, thấp hơn 0,5% vì round down). Đạt target 1:4, lãi ~$1.200.

**Quyết định & lý do:** Ở mỗi lệnh, risk $ được cố định TRƯỚC khi nhìn setup — không lệnh nào "cố risk thêm" dù setup phiên 3 "cảm giác chắc" hơn. Sau mỗi lệnh thắng, size của lệnh sau KHÔNG tăng lên (không có "hưng phấn size").

**Kết quả (tính theo R):** Tổng 3 lệnh đạt khoảng +3R đến +3.5R tổng hợp qua 3 phiên tuỳ quy đổi, tổng lãi minh hoạ khoảng $3.500 trên vốn $100k (~3,5%) — đủ để đóng góp đáng kể vào profit target 8-10% của một challenge prop-firm điển hình, mà không lệnh nào vượt quá 0,5% risk.

**Bài học rút ra:** Kỷ luật sizing nhất quán (không thay đổi % theo cảm giác) cho phép "cộng dồn" nhiều lệnh thắng nhỏ thành kết quả đáng kể mà mỗi lệnh riêng lẻ đều an toàn dưới mọi giới hạn — đây chính là cách 0,5%/lệnh "dễ thở" với daily/trailing limit như note gốc mô tả ở mục 5.

### Case 2 — Thua dù làm đúng mọi thứ: sizing chuẩn, entry chuẩn, vẫn dính stop vì gap qua đêm trên XAUUSD (case tổng hợp từ backtest)

**Bối cảnh:** Tài khoản $50.000, risk 0,5% ($250/lệnh), giữ một vị thế XAUUSD qua đêm (setup swing, không phải scalp) dựa trên bias H4 rõ ràng.

**Diễn biến từng bước:** Entry long tại OB H4 discount, stop đặt hợp lý ngoài POI ở khoảng cách $4,00 (400 "pip" theo quy ước 0,01). Lots = 250 ÷ (4×100) = 0,625 lot — vào 0,6 lot (risk thực tế ~$240, dưới 0,5%). Mọi bước tính toán đúng chuẩn theo công thức. Qua đêm, một tin vĩ mô bất ngờ ngoài giờ giao dịch chính (theo giả định minh hoạ, không phải sự kiện lịch sử cụ thể) khiến giá gold gap mạnh khi mở phiên tiếp theo, vượt qua mức stop đã đặt mà không khớp đúng giá đó.

**Quyết định & lý do:** Không có quyết định sai ở khâu vào lệnh — toàn bộ quy trình sizing, entry, stop đều đúng chuẩn theo mọi tiêu chí trong checklist phần lõi.

**Kết quả (tính theo R):** Lệnh bị đóng ở mức giá tệ hơn stop lý thuyết do gap (slippage khi khớp) — risk thực tế chạm khoảng -0,8% đến -1% thay vì -0,5% dự tính, tương đương khoảng -1,6R đến -2R thay vì đúng -1R kế hoạch.

**Bài học rút ra:** Đây là ví dụ kinh điển về **kỳ vọng xác suất và giới hạn của công thức sizing tĩnh**: công thức `lot = risk$/(stop×value)` giả định ngầm rằng stop luôn khớp đúng giá đặt — giả định này đúng đa số thời gian nhưng KHÔNG đúng khi có gap. Bài học thực chiến không phải "công thức sai" mà là: với các vị thế giữ qua đêm/qua weekend, nên tính risk% mục tiêu THẤP HƠN 0,5% một chút (ví dụ 0,3-0,4%) để chừa biên cho slippage gap, hoặc chấp nhận rủi ro này như một phần của chi phí "cầm lệnh xuyên đêm" đã biết trước.

### Case 3 — Suýt vào lệnh nhưng checklist chặn lại: correlation risk giữa EURUSD và GBPUSD (case tổng hợp từ backtest)

**Bối cảnh:** Tài khoản $100.000, risk 0,5%/lệnh, phiên London, DXY (chỉ số USD) đang trong một nhịp giảm rõ theo bias D1.

**Diễn biến từng bước:** Setup long EURUSD xuất hiện đầu tiên tại OB H1 discount, đầy đủ sweep + MSS + FVG. Trader tính risk $500, vào 2,0 lot theo stop 25 pip, đã filled. Ngay sau đó trong cùng phiên, một setup long GBPUSD cũng xuất hiện, cấu trúc tương tự, cũng đầy đủ tiêu chí entry model — về mặt kỹ thuật hoàn toàn là "một lệnh độc lập, risk 0,5% riêng, hợp lệ".

**Quyết định & lý do:** Trước khi bấm lệnh GBPUSD, checklist "không tương quan chồng chất" (mục 10 phần lõi, quy tắc 7) buộc trader tự hỏi: hai lệnh này có thực chất là MỘT cú cược lớn vào "USD yếu" không? Trả lời: có — cả hai đều long một đồng tiền khác so với USD, với LÝ DO GIỐNG NHAU (DXY giảm). Nếu tính risk gộp, hai lệnh 0,5% "độc lập" thực chất tạo ra một rủi ro USD tổng hợp gần 1% trên cùng MỘT nguồn biến động (nếu USD bất ngờ mạnh lên vì tin CPI, cả hai lệnh có xác suất cao dính SL CÙNG LÚC).

**Kết quả:** Trader giảm size lệnh GBPUSD xuống một nửa (0,25% thay vì 0,5%) để tổng risk gộp danh mục không vượt quá 0,75% cho "rủi ro USD" duy nhất này, thay vì coi đó là hai rủi ro độc lập 1% tổng.

**Bài học rút ra:** Đây chính xác là kịch bản "correlation risk khi vào 2 cặp cùng chiều USD" mà mỗi lệnh riêng lẻ đều pass mọi tiêu chí position sizing, nhưng nếu không có bước kiểm tra tương quan, tổng rủi ro danh mục bị đánh giá thấp hơn thực tế. Checklist chặn không phải vì setup xấu — mà vì kích thước TỔNG cần điều chỉnh khi biết trước hai lệnh không thực sự độc lập.

![[PositionSize-DeepDive-CorrelationRisk.svg]]
*Hai lệnh long EURUSD và GBPUSD nhìn riêng lẻ đều "risk 0,5%, an toàn" — nhưng cả hai thực chất là một vị thế short USD lớn; nếu USD đảo chiều bất ngờ, cả hai đều dính SL cùng lúc, risk gộp thực tế vượt xa tổng hai con số 0,5% cộng lại theo cách nghĩ độc lập.*

### Case 4 — Setup biến thái khó nhận diện: sizing đúng công thức nhưng sai đơn vị hợp đồng (NQ vs MNQ, case tổng hợp từ backtest)

**Bối cảnh:** Tài khoản $25.000 (tài khoản nhỏ, giai đoạn đầu funded), risk 0,5% ($125/lệnh), giao dịch chỉ số Nasdaq.

**Diễn biến từng bước:** Trader tính risk $125, stop 15 điểm, dự định dùng NQ (E-mini, $20/điểm): Contracts = 125 ÷ (15×20) = 0,42 — round xuống bằng 0 contract, tức KHÔNG đủ risk budget để vào dù chỉ 1 NQ full-size với stop này trên tài khoản $25k. Nếu trader vô tình nhầm bảng giá trị/điểm (dùng nhầm $20/điểm của NQ để tính cho MNQ, hoặc ngược lại nhầm đơn vị micro thành full-size khi nhập lệnh trên platform), có hai kịch bản sai:

**(a)** Nếu trader tính đúng cần dùng MNQ ($2/điểm) nhưng lúc đặt lệnh trên platform lại chọn nhầm ký hiệu NQ (full-size, gấp 10 lần giá trị điểm), risk thực tế trở thành $125 × 10 = $1.250 — gấp 10 lần dự tính, tương đương 5% tài khoản trong MỘT lệnh, vi phạm nghiêm trọng luật ≤0,5%.

**(b)** Ngược lại, nếu tính cho NQ nhưng đặt nhầm MNQ, risk thực tế chỉ còn $12,50 (0,05%) — không vi phạm rủi ro, nhưng làm lệch hoàn toàn kỳ vọng lãi khi thắng (chỉ lãi 1/10 dự tính), khiến thống kê performance cá nhân bị nhiễu nếu không phát hiện.

**Quyết định & lý do:** Nếu có bước kiểm tra chéo cuối cùng trước khi bấm lệnh ("số lot/contract hiển thị trên platform × giá trị/điểm đúng ký hiệu = risk $ dự tính?"), lỗi (a) — nguy hiểm hơn nhiều — sẽ bị chặn ngay trước khi khớp.

**Kết quả (giả định minh hoạ hai nhánh):** Nhánh (a) nếu không bị chặn: một lệnh thua dính risk 5% tài khoản — đủ để chạm hoặc rất gần daily loss limit của nhiều prop firm chỉ trong MỘT lệnh, hoàn toàn phá vỡ mục đích của toàn bộ hệ thống sizing 0,5%.

**Bài học rút ra:** Đây là "setup biến thái" nguy hiểm nhất trong nhóm edge case position sizing vì nó **không phải lỗi công thức toán** — công thức `risk$/(stop×value)` được áp dụng đúng — mà là lỗi **thực thi/nhập liệu** (chọn nhầm ký hiệu hợp đồng trên platform). Loại lỗi này đặc biệt nguy hiểm vì nó ẩn mình sau một phép tính "trông đúng hoàn toàn" trên giấy, chỉ lộ ra tại bước khớp lệnh thật. Bài học: luôn có một bước xác nhận cuối cùng đối chiếu risk $ HIỂN THỊ trên platform (không chỉ tính trên giấy/excel) trước khi xác nhận lệnh, đặc biệt khi giao dịch nhiều loại hợp đồng có tên gần giống nhau (NQ/MNQ, ES/MES).

---

## D. Edge cases & kinh nghiệm live/backtest

**1. Risk per trade khi spread giãn lúc rollover 17:00 EST hoặc đầu phiên Á.** Vì sao xảy ra: thanh khoản mỏng trong vài phút quanh rollover/đầu phiên Á khiến spread giãn đột ngột (có thể gấp 3-5 lần bình thường ở một số cặp/CFD); nếu bạn đặt lệnh market ngay lúc này, giá khớp lệch xa hơn dự tính, làm risk thực tế vượt kế hoạch dù stop distance trên chart không đổi. Cách xử lý: tránh vào lệnh market mới trong khung 15-30 phút quanh rollover trừ khi setup cực kỳ rõ ràng; nếu buộc phải vào, tính thêm biên spread dự phòng vào stop distance trước khi tính lot.

**2. Sizing với gap qua đêm — đặc biệt trên các sản phẩm có giờ đóng/mở (index CFD, một số FX exotic).** Vì sao xảy ra: giữ lệnh qua đêm nghĩa là stop đặt trên chart chỉ được đảm bảo khớp gần đúng NẾU giá không gap qua nó khi mở phiên tiếp theo; nếu có gap (do tin qua đêm), risk thực tế có thể gấp đôi/gấp ba dự tính. Cách xử lý: với các setup giữ qua đêm, chủ động hạ risk% mục tiêu (ví dụ 0,25-0,3% thay vì 0,5%) để chừa biên cho khả năng gap, hoặc dùng option/hedge nếu công cụ cho phép.

**3. Prop firm daily drawdown — nhầm mốc tham chiếu (balance cố định vs equity đóng cửa hôm trước).** Vì sao xảy ra: các prop firm khác nhau định nghĩa "daily loss limit" theo mốc khác nhau (một số tính theo balance đầu ngày cố định, một số theo equity đóng cửa ngày hôm trước bao gồm cả lãi/lỗ chưa đóng) — nhầm mốc này khiến trader tưởng mình còn nhiều "room" risk hơn thực tế cho phép. Cách xử lý: đọc kỹ đúng văn bản rule của firm đang thi (không suy diễn từ firm khác), và luôn tính circuit breaker cá nhân dựa trên mốc NGHIÊM NGẶT HƠN nếu không chắc chắn.

**4. Tick value NQ vs MNQ nhầm lẫn khi đặt lệnh trên platform (mở rộng Case 4).** Vì sao xảy ra: hai ký hiệu gần giống nhau, giá trị điểm chênh nhau đúng 10 lần — một sai số nhập liệu nhỏ (chọn nhầm dropdown, hoặc broker mặc định symbol khác ý định) tạo ra sai số risk 10 lần. Cách xử lý: luôn xác nhận risk $ hiển thị trên vé lệnh (order ticket) của platform TRÙNG với risk $ đã tính trên giấy/spreadsheet trước khi gửi lệnh — không tin tưởng mù quáng vào phép tính đã làm trước đó.

**5. Compounding (fixed fractional) vs fixed dollar khi tài khoản biến động mạnh trong giai đoạn thi prop firm.** Vì sao xảy ra: nếu dùng fixed fractional (% của balance hiện tại) trong giai đoạn thi có giới hạn $ tuyệt đối (ví dụ daily loss $5k cố định không đổi theo balance), một chuỗi thắng làm balance tăng, kéo theo risk $ mỗi lệnh tăng theo % — có thể vô tình khiến MỘT lệnh thua chiếm tỷ trọng lớn hơn dự tính so với giới hạn $ tuyệt đối cố định của firm. Cách xử lý: trong giai đoạn thi có giới hạn $ tuyệt đối, ưu tiên fixed dollar (tính theo % của balance khởi điểm, không phải balance hiện tại) như note gốc đã khuyến nghị ở mục 6.

**6. Backtest bias khi tính lot theo giá trị/điểm đã thay đổi theo thời gian (ví dụ margin/tick value futures có thể được sàn điều chỉnh).** Vì sao xảy ra: một số hợp đồng futures/CFD có thể thay đổi thông số hợp đồng (tick size, giá trị điểm) qua các kỳ theo quy định sàn — backtest dùng thông số hiện tại áp cho dữ liệu lịch sử cũ có thể tính risk % sai lệch nhẹ so với thực tế lúc đó. Cách xử lý: khi backtest dài hạn qua nhiều năm, kiểm tra xem thông số hợp đồng có thay đổi trong giai đoạn backtest không, đặc biệt với futures.

**7. Khối lượng mẫu nhỏ tạo ảo giác về mức risk% "tối ưu".** Vì sao xảy ra: so sánh hiệu suất giữa các mức risk% (0,5% vs 1% vs 2%) trên một backtest có ít hơn 50-100 lệnh dễ cho kết luận sai — vì ở mẫu nhỏ, thứ tự ngẫu nhiên của các lệnh thắng/thua ảnh hưởng lớn đến kết quả cuối, khiến một mức risk% "trông tốt hơn" chỉ vì maypay ngẫu nhiên các lệnh thắng lớn rơi vào đúng lúc balance đang cao. Cách xử lý: chạy resampling/bootstrap (xáo trộn thứ tự các lệnh nhiều lần) trên cùng tập kết quả để xem drawdown/growth có ổn định qua các thứ tự khác nhau hay không, trước khi tin vào một mức risk% cụ thể.

**8. Tâm lý thực chiến — không dám bấm lệnh sau 2-3 lệnh thua liên tiếp dù setup đúng chuẩn.** Vì sao xảy ra: sau một chuỗi thua (hoàn toàn bình thường về thống kê với bất kỳ hệ thống có win-rate <100%), phản ứng tâm lý tự nhiên là nghi ngờ hệ thống và bỏ lỡ lệnh tốt tiếp theo — hoặc ngược lại, cố "gỡ" bằng cách tăng size (revenge trading), vi phạm chính nguyên tắc cốt lõi của position sizing. Cách xử lý: tách bạch rõ circuit breaker THEO KẾ HOẠCH TRƯỚC (ví dụ dừng sau 3 lệnh thua liên tiếp để nghỉ, KHÔNG dừng vì "cảm thấy sợ") khỏi phản ứng cảm xúc tuỳ hứng — nếu circuit breaker chưa chạm, tiếp tục theo kế hoạch; nếu chạm, dừng đúng như đã định trước, không sớm không muộn hơn vì cảm xúc.

**9. FOMO tăng size khi gần đạt profit target của prop firm challenge.** Vì sao xảy ra: khi gần đạt target (ví dụ đã lãi 8% trong mục tiêu 10%), tâm lý muốn "về đích nhanh" khiến trader tăng size để đạt nốt 2% còn lại trong ít lệnh hơn — đây là hành vi ngược hoàn toàn với khuyến nghị của note gốc ("về gần target thì GIẢM size"). Cách xử lý: thiết lập trước một quy tắc cứng (ví dụ tự động giảm risk% xuống một nửa khi đã đạt 70-80% profit target) để loại bỏ quyết định cảm tính tại đúng thời điểm dễ mắc lỗi nhất.

| Tín hiệu cảnh báo sớm | Hành động |
|---|---|
| Chuẩn bị vào lệnh giữ qua đêm/qua weekend | Hạ risk% mục tiêu (0,25-0,3%) để chừa biên gap; hoặc chấp nhận rủi ro gap như chi phí đã biết |
| Sắp đặt lệnh trong 15-30 phút quanh giờ rollover | Kiểm tra spread hiện tại có giãn bất thường không trước khi gửi market order |
| Có 2+ lệnh mở trên các cặp cùng chiều USD (hoặc cùng nhóm tương quan) | Tính gộp risk như một vị thế duy nhất, giảm size lệnh sau nếu cần |
| Chưa xác nhận risk $ hiển thị trên platform khớp với số đã tính | Dừng lại, đối chiếu lại trước khi gửi lệnh — đặc biệt với NQ/MNQ, ES/MES |
| Vừa thua 3 lệnh liên tiếp | Dừng theo circuit breaker đã định trước, không phải vì cảm xúc lúc đó |
| Đã đạt 70-80% profit target của challenge | Tự động giảm risk%, không tăng để "về đích nhanh" |
| Không chắc mốc tham chiếu daily loss limit của prop firm đang thi | Đọc lại văn bản rule chính thức, tính theo mốc nghiêm ngặt hơn nếu còn nghi ngờ |
| Backtest risk% dựa trên dưới 50 mẫu | Không kết luận mức risk% "tối ưu"; thu thập thêm mẫu hoặc chạy resampling |

## Bổ sung mục D (tiếp) — các edge case còn lại

**10. Slippage & partial fill khi displacement mạnh làm risk thực tế khác risk kế hoạch cả hai chiều (entry và exit).** Vì sao xảy ra: không chỉ exit (stop) bị ảnh hưởng bởi gap/spread — entry cũng có thể bị fill ở giá tệ hơn dự tính nếu vào bằng market order ngay lúc displacement mạnh đang diễn ra, làm cả stop distance THỰC TẾ (đo từ giá filled thật, không phải giá dự kiến) khác với kế hoạch trên giấy theo cả hai đầu. Cách xử lý: với các setup cần vào ngay lúc displacement (aggressive entry), chấp nhận trước rằng risk% thực tế có thể dao động ±0,1-0,2% so với kế hoạch, và không cố "chỉnh" size giữa lúc lệnh đang khớp.

**11. Swap phí giữ lệnh 3 ngày thứ Tư và phí qua weekend gap — ảnh hưởng gián tiếp tới sizing của lệnh giữ dài.** Vì sao xảy ra: với các lệnh forex/CFD giữ qua nhiều ngày, phí swap tích lũy (đặc biệt gấp 3 vào thứ Tư theo quy ước rollover chuẩn) là một chi phí thực nhưng KHÔNG được tính trong công thức risk = stop × value cơ bản — nếu swap đủ lớn (lãi suất chênh lệch cao giữa hai đồng tiền), nó có thể âm thầm làm risk thực tế của một vị thế giữ dài cao hơn risk đã tính chỉ dựa trên khoảng cách stop. Cách xử lý: với các lệnh dự kiến giữ nhiều ngày trên các cặp có swap cao, cộng thêm ước tính phí swap dự kiến vào "chi phí tối đa có thể mất" khi tính risk %, không chỉ tính khoảng cách tới stop.

**12. Margin call cascade khi nhiều lệnh cùng lúc chạm SL trong một cú di chuyển mạnh bất ngờ.** Vì sao xảy ra: nếu tài khoản đang mở nhiều vị thế đồng thời (dù mỗi lệnh risk 0,5% hợp lệ riêng lẻ) và một cú di chuyển vĩ mô mạnh (ví dụ một tin bất ngờ ngoài dự kiến) khiến TẤT CẢ các lệnh dính SL gần như cùng lúc, tổng lỗ thực tế trong vài giây/phút có thể vượt xa tổng risk % dự tính nếu một số lệnh bị slippage nặng do thanh khoản cạn kiệt tạm thời (đặc biệt nguy hiểm nếu các lệnh đó tương quan cao — quay lại vấn đề ở Case 3). Cách xử lý: giới hạn số lệnh mở đồng thời tối đa (không chỉ giới hạn risk% mỗi lệnh), đặc biệt giảm số lệnh mở qua các mốc tin tức lớn đã biết trước.

**13. Backtest bias — look-ahead khi tính lot dựa trên "biết trước" toàn bộ swing đã hình thành.** Vì sao xảy ra: khi backtest thủ công bằng mắt trên chart lịch sử đã đóng, dễ vô thức đặt stop distance "đẹp" hơn thực tế live (vì đã biết giá sẽ đi đâu tiếp theo, nên "chọn" một điểm swing tối ưu cho stop mà lúc live không thể biết trước) — điều này làm risk-of-ruin backtest lạc quan hơn thực tế. Cách xử lý: backtest replay bar-by-bar, cố định logic đặt stop theo quy tắc cứng (ví dụ luôn X điểm ngoài wick sweep gần nhất tại thời điểm đó) không cho phép "nhìn thấy trước" khi đặt.

| Tín hiệu cảnh báo sớm (bổ sung) | Hành động |
|---|---|
| Sắp giữ lệnh forex/CFD nhiều ngày trên cặp có swap cao | Cộng thêm ước tính phí swap vào chi phí tối đa dự kiến trước khi tính risk % |
| Đang mở nhiều lệnh đồng thời, kể cả không tương quan rõ | Giới hạn cứng số lệnh mở đồng thời, không chỉ giới hạn risk%/lệnh |
| Backtest thủ công bằng mắt trên chart đã đóng hoàn toàn | Chuyển sang replay bar-by-bar để loại bỏ look-ahead khi chọn điểm đặt stop |
| Cần vào bằng market order ngay giữa lúc displacement mạnh | Chấp nhận trước biên sai lệch risk% ±0,1-0,2%, không cố chỉnh size giữa chừng |
