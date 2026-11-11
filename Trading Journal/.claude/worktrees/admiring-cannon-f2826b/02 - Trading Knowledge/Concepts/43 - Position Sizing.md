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
status: seed
category: Risk Management
last_reviewed: 2026-07-05
created: 2026-07-05
updated: 2026-07-05
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
