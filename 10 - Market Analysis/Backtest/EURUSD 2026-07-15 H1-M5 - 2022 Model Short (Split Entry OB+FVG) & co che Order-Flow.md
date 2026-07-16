---
type: market-analysis
status: backtest
date: 2026-07-15
trade_date: 2016-11-30
symbol: EURUSD
timeframe: H1 / M5
session: London/NY (replay - du lieu doc tu truc H1 ~28 Nov - 02 Dec 2016)
htf_bias: bearish (H1 premium OB reject sau khi quet BSL)
setup: 2022 Model Short - BSL sweep -> MSS (M5) -> FVG/OB -> split entry (premium + discount)
in_trade: true
result: Win (leg FVG khop & hit TP; leg OB premium khong khop)
entry_approach: split 50/50 (scale-in / laddering)
entry_A_price: 1.06599
entry_B_price: 1.06434
stop_loss: 1.06668
take_profit: "leg A: 1.06196 | leg B: 1.05888 (~1.0595 hit)"
grade: A- (cau truc) / entry approach = scale-in
key_poi: "Bearish OB M5 1.06591-1.06610 (leg A - premium) | FVG M5 1.06414-1.06453 (leg B - discount)"
draw_on_liquidity: "BSL da quet: dinh sweep ~1.0666 | SSL muc tieu: H1 Bullish OB ~1.0588-1.0595, day lon 1.05653"
invalidation: dong nen reclaim tren sweep high ~1.06668
topic: split entry OB (premium) + FVG (discount), tradeoff fill-rate vs RR, va co che order-flow (vi sao gia di tu BSL sang SSL)
tags:
  - analysis
  - methodology
  - EURUSD
  - ict-2022
  - buy-side-liquidity
  - sell-side-liquidity
  - liquidity-sweep
  - market-structure-shift
  - aggressive-displacement-entry
  - fair-value-gap
  - order-block
  - premium-discount
  - draw-on-liquidity
  - internal-external-range-liquidity
  - expectancy
  - entry-selection
  - scale-in
---

# EURUSD H1 -> M5 - 2022 Model Short (BSL Sweep -> MSS -> FVG) - Split Entry OB+FVG & co che order-flow - 2026-07-15

> [!info] Trang thai
> **CASE STUDY - lenh backtest da vao (split entry, WIN).** Note tong hop tron phien phan tich [[01 - ICT 2022 Model]] Short tren EURUSD (replay ~28/11-02/12/2016). Cau truc **sweep -> MSS -> FVG** da verify hop le. Diem dat gia: thay vi cho 1 trong 2 POI, Khang **chia entry 50/50** - 0.5 tai FVG (SL xa) + 0.5 tai Bearish OB (premium). Ket qua: **gia quet len tren FVG roi dao manh** xuong TP tai H1 Bullish OB. Note nay giai quyet dut diem cau hoi entry, va them phan **"vi sao gia di nhu vay"** theo dung mong muon phan tich sau cua Khang.
> Note phuong phap + lenh da vao (`in_trade: true`). Gia doc tu chart, co the lam tron.

> [!note] Chart goc
> Dan cac anh cua ban vao day de doi chieu: (1) H1 zoom out - OB + DOL; (2) M5 zoom - sweep/MSS/FVG; (3) M5 markup Bearish OB vs FVG; (4) M5 split entry + ket qua. Vd: `![[EURUSD-20161130-M5-splitentry.png]]`.

## 0. Tom tat lenh

| Field | Value |
|---|---|
| Symbol / Position | EURUSD / **Short** |
| Data (replay) | ~30/11/2016 - Session London/NY |
| Setup | ICT 2022 Model (LTF entry M5) |
| Bias HTF | **Bearish** - H1 premium OB reject sau BSL sweep |
| Entry approach | **Split 50/50 (scale-in)** |
| Leg A (0.5) | **Bearish OB Sell limit 1.06599** (premium) - **KHONG khop** (gia chi len ~1.0655) |
| Leg B (0.5) | **FVG 1.06434** (discount), SL xa - **KHOP** |
| SL (chung) | tren sweep high **~1.06668** |
| TP | leg A 1.06196 / leg B **1.05888** (**~1.0595 hit**) = H1 Bullish OB / SSL |
| Ket qua | **WIN** (leg FVG); gia quet len tren FVG roi drop manh ve TP |

---

## 1. HTF context (H1) - bias & draw on liquidity

Tren H1, gia day len test **[[25 - OB - Order Block|OB]] vung premium ~1.0658-1.0667** roi reject -> bias **bearish**. Nguyen tac [[32 - Top-down Analysis (Multiple Timeframes)|top-down]]: HTF cho "O DAU" (POI + huong), LTF cho "KHI NAO" (trigger).

**[[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)|Draw on Liquidity]]:**
- **BSL (da quet):** buy-stops tren cac dinh cu -> bi purge tai dinh sweep ~1.0666 (dieu kien #1).
- **SSL (muc tieu Short):** **H1 Bullish OB ~1.0588-1.0595 (1.05823)**; sau hon la **day lon 1.05653**. Downside co cho de di.

## 2. M5 - xac nhan 3 dieu kien (da verify)

- [x] **[[20 - Liquidity Sweep|BSL sweep]]** - dinh phai nho len tren dinh trai (~1.06638) roi **dong cua lai xuong duoi** = purge that.
- [x] **[[21 - Market Structure Shift|MSS]]** - nen [[35 - Aggressive Displacement Entry|displacement]] dong cua xuyen **2 internal low lien tiep** (~1.06478 & ~1.06378) -> MSS quyet doan.
- [x] **[[13 - FVG  - Fair Value Gap|FVG]]** - nen giua than lon, gap 3 nen ro (1.06414-1.06453).

=> Bo **sweep -> MSS -> FVG** day du va sach. Bias bearish M5 xac nhan.

## 3. Nut that: hai POI - hai ho so rui ro khac han

![[OB-vs-FVG-entry-20260715.svg]]

| Tieu chi | **Bearish OB (1.06591-1.06610)** | **FVG (1.06414-1.06453)** |
|---|---|---|
| Vi tri | **Premium** (cao) - sat sweep high | **Discount** (thap) - day displacement |
| Cach gia (1.06395) | **Xa (~20 pip)** -> cho retrace sau | **Sat gia** -> gan nhu cham |
| SL (tren sweep high ~1.06668) | risk **~7-8 pip** | risk **~24 pip** |
| RR | **cao (~10R)** | **thap (~2.5R)** |
| Xac suat khop | **Thap** | **Cao** |
| Ket qua THAT | **KHONG khop** | **KHOP -> WIN** |

The luong nan: OB cho gia tot + SL gon nhung **kho khop**; FVG **de khop** nhung ban re + SL rong.

## 4. FVG day displacement - "bay" hay khong? Phai noi cho chinh xac

> [!summary] Nguyen tac: SHORT thi ban o PREMIUM
> Voi Sell, entry cang cao cang tot. OB (1.0660) = ban dat + SL gon; FVG (1.0643) = ban re + SL rong. Xem [[27 - Premium Discount]].

**Dieu chinh lai luan diem truoc do cho dung:** FVG khong phai luc nao cung la bay. Chinh xac hon la:
- **FVG + SL sat (ngay tren FVG ~1.0646) = bay that.** Gia hay quet len tren FVG roi moi dao -> SL sat se bi quet oan. **Case nay chung minh dieu do**: gia da len ~1.0655 (tren ca FVG) roi moi drop.
- **FVG + SL xa (tren sweep high) nhu mot phan cua scale-in = cong cu tham gia hop le.** Day chinh la cach Khang da lam.

Loi can tranh van la **phan vai (role confusion)** kieu "vao FVG voi SL sat de RR dep" - do la [[04 - Mistake - FOMO Entry]] + [[05 - Mistake - Not enough RR]]. Nhung "vao FVG voi SL xa, size nho, trong mot ke hoach scale" thi khac han.

## 5. Giai phap Khang ap dung: Split entry 50/50 (scale-in)

Thay vi ep chon 1 trong 2, Khang **chia lenh**: **0.5 slot @ FVG (SL xa)** + **0.5 slot @ Bearish OB (premium)**, cung SL tren sweep high. Day la cach xu ly the luong nan **fill-rate vs RR** mot cach ky su:

- Leg FVG **bao dam duoc tham gia** (fill cao) - khong bo lo keo.
- Leg OB **nang gia trung binh va RR** neu gia retrace du sau.
- Size moi leg nho -> rui ro tong van trong khung ([[07 - Mistake - Risk more than 0.5% total account]], [[43 - Position Sizing]]).

**Dien bien that (rat dat gia de hoc):**

1. Gia retrace **quet len tren FVG entry** toi ~1.0655 - nhung **KHONG cham OB limit 1.06599** -> **leg OB khong khop**.
2. Tu ~1.0655 gia **dao manh**, displacement xuong tan **H1 Bullish OB ~1.0588-1.0595** -> **leg FVG hit TP = WIN**.

> [!warning] Ba insight trung thuc tu ket qua nay
> **(a) Neu cho OB-only, ban da MISS ca keo.** Gia khong bao gio cham 1.06599. Chinh leg FVG - cai ma ban lo lang - moi la cai thang. Day la bang chung song dong vi sao **fill-rate quan trong** trong expectancy, va vi sao truc giac "dung chi ngoi cho mo hinh hoan hao" cua ban la dung.
> **(b) SL xa cua leg FVG chinh la thu cuu no.** Gia quet len tren FVG (~1.0655) roi moi dao - neu SL sat tren FVG (~1.0646) thi da bi quet truoc khi drop. Dung y canh bao truoc do.
> **(c) Canh bao outcome bias:** 1 lenh thang KHONG chung minh phuong phap. Leg thang la leg RR thap (~2.5R) + SL rong; leg RR cao (OB) khong dong gop gi. Phai do split-entry bang **expectancy tren sample**, khong bang keo nay.

> [!summary] Danh doi cua split (phai biet ro)
> Split lam **giam size o gia tot nhat** (chi 0.5 o OB) va **tang size o gia xau hon** (0.5 o FVG). Neu gia retrace sau roi dao (ca 2 khop), avg entry tot; neu gia dao ngay tu FVG (nhu case nay), ban chi lai o size nho hon so voi all-in FVG. Khong co bua an mien phi - split mua su **on dinh ket qua (lower variance)**, doi lai **upside toi da thap hon**.

## 6. Vi sao gia di nhu vay (co che order-flow)

Day la phan Khang muon dao sau - khong chi "cho mo hinh" ma hieu **tai sao**. Toan bo di chuyen la mot chuoi **di san thanh khoan** giua cac pool doi ung:

1. **Len quet BSL o premium (ERL tren):** gia can day len vung dinh de cham **buy-stops** (breakout buyers + stop cua shorts som). Do la noi co **doi ung mua** du lon de smart money **ban vao** ma khong truot gia. Khong co thanh khoan tren do -> khong co ban lon -> khong co reversal. Xem [[16 - Internal & External Range Liquidity (IRL & ERL)]], [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]].
2. **Displacement xuong (MSS):** sau khi da hap thu buy-side, dong lenh doi chieu -> pha cau truc, tao FVG (dau chan cua su mat can bang delivery).
3. **Retrace quet len tren FVG (IRL noi bo):** nhip hoi khong phai "ngau nhien" - no len **grab internal buy-side** (stop cua nhung ai ban som tai FVG + buy-stops nho phia tren FVG) va **rebalance FVG**, dong thoi chao mot lan **ban premium** nua gan OB. Sau khi quet xong internal liquidity -> het nhien lieu de len -> tiep dien.
4. **Giao ve SSL/discount OB (ERL duoi):** muc tieu cuoi la **draw on liquidity** phia duoi - noi sell-stops + resting buy orders nam (H1 Bullish OB 1.0588-1.0595). Gia di tu ERL tren -> ERL duoi, con FVG/OB chi la **tram trung chuyen**.

> [!summary] Khung tu duy "vi sao"
> Gia khong di theo hinh - gia di tu **pool thanh khoan** nay sang **pool thanh khoan** khac. Mo hinh (2022 Model) chi la **cach dong goi** hanh vi do. Khi backtest, tap hoi 3 cau: (1) Thanh khoan nao vua bi lay? (2) Thanh khoan doi ung ke tiep o dau (draw)? (3) Gia dang o premium hay discount cua leg lien quan? Tra loi duoc 3 cau nay la ban dang doc order-flow, khong con "cho mo hinh". Xem them [[37 - Re-mapping Dealing Range sau Displacement]].

## 7. Recap chuoi ICT 2022 Model

- [x] **Liquidity Sweep** - quet BSL tai dinh ([[20 - Liquidity Sweep]], [[07 - Buy-side Liquidity]])
- [x] **Displacement** - nen manh tao FVG, pha 2 internal low ([[35 - Aggressive Displacement Entry]])
- [x] **MSS** - dong cua xuyen swing low bao ve ([[21 - Market Structure Shift]])
- [x] **FVG / OB hop le** trong premium ([[13 - FVG  - Fair Value Gap]], [[25 - OB - Order Block]])
- [x] **Entry** - split 50/50 (FVG + OB), SL chung tren sweep high
- [x] **SL** ~1.06668 - **TP** SSL 1.0588-1.0595 -> 1.0565 ([[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]], [[30 - Sell-side Liquidity]])

## 8. Concept da ap dung

- [[01 - ICT 2022 Model]] - [[20 - Liquidity Sweep]] - [[21 - Market Structure Shift]] - [[35 - Aggressive Displacement Entry]]
- [[13 - FVG  - Fair Value Gap]] - [[25 - OB - Order Block]] - [[27 - Premium Discount]] - [[26 - OTE - Optimal Trade Entry]]
- [[07 - Buy-side Liquidity]] - [[30 - Sell-side Liquidity]] - [[39 - Draw on Liquidity (Tại sao giá di chuyển & ai là đối ứng)]] - [[16 - Internal & External Range Liquidity (IRL & ERL)]]
- [[38 - Liquidity Reflexivity (Bẫy đám đông ICT)]] - [[37 - Re-mapping Dealing Range sau Displacement]] - [[32 - Top-down Analysis (Multiple Timeframes)]] - [[43 - Position Sizing]]

## 9. Bai hoc rut ra

1. **Split entry (scale-in) la giai phap hop le** cho the luong nan fill-rate vs RR: fill (FVG) + gia tot (OB), size nho moi leg.
2. **Trong case nay OB khong khop** - neu cho OB-only ban da miss. Fill-rate la ly do ton tai cua leg FVG.
3. **FVG chi hop le khi SL xa** (tren sweep high) - vi gia hay quet len tren FVG roi moi dao. SL sat = bi quet oan.
4. **Split doi upside lay on dinh** - hieu ro danh doi, dung tuong split la "an chac".
5. **Danh gia bang expectancy tren sample**, khong bang 1 ket qua thang (outcome bias).
6. **Gia di tu pool thanh khoan sang pool thanh khoan** (BSL premium -> SSL discount); FVG/OB la tram trung chuyen. Doc order-flow = hoi "thanh khoan nao vua lay / draw ke tiep o dau / premium hay discount".

## 10. Next steps

- Them cot backtest: **"leg nao khop" + "do sau retrace sau MSS"** (OB vs FVG) -> gom ~20-30 mau de biet nen split ty le nao (50/50? 30/70?) cho tung instrument.
- So sanh **expectancy 3 kich ban**: all-in OB / all-in FVG / split 50/50 (tinh ca setup bi miss = 0) -> so lieu chon rule, khong phai cam giac.
- Neu chot split thanh chuan -> viet rule vao `03 - Playbooks/` (dieu kien: displacement manh -> uu tien leg FVG do it retrace sau).
- Tao file backtest chi tiet trong `04 - Backtesting/` cho lenh nay va cross-link nguoc ve note nay.

---
*Ghi chu: chart replay (du lieu ~28/11-02/12/2016); gia doc tu chart, co the lam tron. Lenh da vao dang split (`in_trade: true`): leg FVG khop & WIN, leg OB khong khop. So lieu RR/USD la uoc luong tu chart.*
