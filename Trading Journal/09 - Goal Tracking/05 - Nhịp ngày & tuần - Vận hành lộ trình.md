---
type: routine
dashboard: Daily Rhythm
created: 2026-09-07
updated: 2026-09-07
tags:
  - routine
  - daily
  - discipline
  - streak
---

# ⏱️ Nhịp ngày & tuần — vận hành lộ trình

> [!summary] Note này trả lời đúng một câu hỏi: **"Hôm nay tôi mở file nào và làm gì?"**
> - [[03 - Lộ trình chi tiết - Từ số 0 đến Funded 100K]] nói **đi đâu** (giai đoạn + gate).
> - [[04 - Phương pháp luyện tập, vòng lặp AI & giữ động lực]] nói **luyện thế nào** (trần 3–4h, retrieval, 7 bước backtest).
> - Note này nói **hôm nay làm gì, bao lâu, và bằng chứng nào trong vault chứng minh đã làm**.
>
> Ba luật nền, không thương lượng:
> 1. **Chuỗi > khối lượng.** Chỉ số chính là *"tuần thứ N liên tiếp có ≥5 ngày log"*, không phải *"còn 178/200 mẫu"*.
> 2. **Trần 3–4h luyện sâu/ngày, 5–6 ngày/tuần, MỌI tuần.** Vượt trần là làm mạnh hơn đúng cái pattern đã sụp tháng 7/2026.
> 3. **Ngày tối thiểu 20 phút luôn tồn tại.** Chuỗi 6 ngày bị phá không vì ngày thứ 7 quá khó, mà vì **không có bản nhỏ của ngày thứ 7**.

## 1. Ba loại ngày — mỗi sáng chọn đúng một

| Loại | Khi nào chọn | Thời lượng | Nội dung bắt buộc | Tính vào chuỗi |
|---|---|---|---|---|
| 🟢 **Tối thiểu** | Ngày mệt, deadline dev, đi công tác, tâm lý kém | **20'** | Đúng 3 mục ở §3, không hơn | ✅ Có |
| 🔵 **Chuẩn** | Ngày làm việc bình thường (T2–T6) | **2–3h** | Retrieval 30' + Sản xuất 45–90' + Đóng vòng 20' | ✅ Có |
| 🟣 **Sâu** | T7/CN — tối đa **2 ngày/tuần** | **3–4h** (trần cứng) | 2–3 phiên replay + 1 khối viết + Đóng vòng | ✅ Có |

> [!danger] Không tồn tại loại ngày thứ tư tên là "hôm nay bỏ"
> Khi thấy mình đang định bỏ cả ngày — đó là tín hiệu **chọn 🟢**, không phải tín hiệu nghỉ. Ngày 🟢 giữ chuỗi sống; ngày bỏ đặt chuỗi về 0. Và theo dữ liệu của chính vault này, chuỗi về 0 thường kéo theo nhiều tuần im lặng.

## 2. Nhịp một ngày 🔵 chuẩn (giờ VN, vẫn còn việc dev)

Neo theo nhịp thật: **thức 04:00, làm việc từ 04:00**. File task được routine sinh sẵn lúc 04:00 nên khối đầu tiên mở ra là đã có việc cụ thể.

| Giờ (gợi ý) | Khối | Thời lượng | Việc | Bằng chứng khi xong |
|---|---|---|---|---|
| 04:15–04:45 | 🧠 **Retrieval** | 30' | 1 concept theo lịch tuần — **viết từ trí nhớ trước**, mở note sau | `last_reviewed` + điểm bảng `## 13` trong concept note |
| 05:00–05:45 | 📊 **Sản xuất** | 45' | Việc chính của giai đoạn đang mở (§4) | 1 file mới/đổi trong `04 - Backtesting` hoặc file GĐ tương ứng |
| 21:00–21:20 | 🌙 **Đóng vòng** | 20' | Daily Summary + đẩy số vào goal note | `00 - Inbox/02 - Daily Summary/YYYY-MM-DD - Daily summary.md` |

> [!note] Dịch giờ thì được, đổi thứ tự thì không
> Retrieval **trước** sản xuất (lôi lý thuyết ra khỏi đầu trước khi áp vào chart). Đóng vòng **trong cùng ngày** — log viết sáng mai là ghi lại *ký ức*, không phải ghi lại *phép đo*.
> Khối 📊 có thể dời xuống 12:15–13:00 những ngày sáng bị chiếm; khối 🌙 thì không dời sang mai.

> [!warning] Buổi tối KHÔNG mở chart live cho tới GĐ3
> GĐ0–GĐ2 (nay → ~06/2027): buổi tối là khối đóng vòng 20', không phải khối chart. Killzone chỉ mở lại từ **GĐ3 — Ổn định**, và khi đó chạy đúng §1 của [[2022 Model A+ Setup]]: chuẩn bị 19:00–20:15 · KZ 20:30–23:00 · journal 23:15 · không mở lại chart sau đó.

## 3. Ngày tối thiểu — định nghĩa cứng (copy nguyên văn vào mọi file task)

- [ ] **1 phiên replay có pre-registration** — thesis + **invalidation** (giá nào thì tôi sai) + **target có tên** (pool nào). Kết luận "No-Trade" vẫn tính là XONG.
- [ ] **1 dòng log thật** vào Daily Summary hôm nay — 1–3 câu, **có số**.
- [ ] **1 field được cập nhật ở nơi dashboard đọc được** — `last_reviewed`, `r_net`, hoặc 1 checkbox cột mốc goal.

> [!danger] Luật trung thực của ngày tối thiểu
> Làm 1/3 hay 2/3 mục → ngày đó **là ngày đứt**, ghi đúng như vậy. Không tick bù. Không dồn 3 mẫu vào một ngày rồi ghi lùi ngày. **Một `[ ]` thành thật hơn một `[x]` giả** — luật này đúng từ 2026-07-13 và vẫn đúng.

## 4. Menu việc theo giai đoạn — chỉ làm giai đoạn đang mở

### 🔓 GĐ0 — Sửa hệ đo · 2026-09-07 → 2026-10-22 · **ĐANG MỞ**

Goal nhận bằng chứng: [[Sua he do - du lieu dang tin truoc khi dat gate]] (8/11 cột mốc tại 2026-09-07)

| Khối | Việc hàng ngày trong GĐ0 |
|---|---|
| 🧠 Retrieval 30' | 1 concept/ngày, **3 concept/tuần**. Thứ tự ưu tiên: `importance: 5` còn `seed` → hiện chỉ còn **[[08-Central-Bank-Dealers-Range]]** (`last_reviewed: 2026-07-02`); hết nhóm này thì lấy `developing` có `last_reviewed` cũ nhất. |
| 📊 Sản xuất 45' | **Đúng một mục sửa hệ đo mỗi ngày**, lấy từ 3 cột mốc còn hở: (1) chốt một bản live journal duy nhất · (2) tạo `30-Sell-side-Liquidity` (đang bị link 38 lần nhưng không tồn tại) · (3) điền `r_multiple` cho 10 lệnh live hoặc đánh dấu **không đo được**. Hết 3 mục → **đo lại 14 mẫu trong phạm vi**: `exit_price` đo thật, `spread_cost`, `r_net`. |
| 🌙 Đóng vòng 20' | Daily Summary + 1 dòng "Nhật ký tiến độ" vào goal GĐ0 **khi có cột mốc đổi thật** (không viết dòng rỗng — "có dòng nhưng rỗng nội dung" là lỗi riêng, đã bị gọi tên 2026-07-17). |

> [!important] Trong GĐ0 replay vẫn chạy hàng ngày — nhưng mẫu chỉ được ĐẾM khi đủ chuẩn mới
> Một mẫu tính vào 200 chỉ khi đủ **7 bước**: random start · hard right edge · quyết định ở tốc độ thật · pre-registration · **ghi cả setup bị bỏ qua** · exit đo thật có `r_net` · giữ out-of-sample.
> **22 mẫu cũ giữ làm tư liệu học, đếm vào mẫu 200 = 0** (16/18 lệnh thắng có `r_multiple` == `r_planned` → cột R đang ghi kế hoạch, không phải kết quả). Bộ sản phẩm từ nay: **chỉ NAS100 + EURUSD**.

### 🔒 GĐ1 — Playbook & liên tục · 2026-10 → 2026-12

Gate: playbook chấm khách quan được · 3 xung đột định nghĩa đã phân xử · **8 tuần liên tiếp ≥5 ngày log**.

| Khối | Việc hàng ngày trong GĐ1 |
|---|---|
| 🧠 Retrieval 30' | Giữ 3 concept/tuần + **chấm bảng `## 13. Mức độ thành thạo`** (36 bảng hiện trống 100% cột điểm) — mỗi ngày 1 bảng. |
| 📊 Sản xuất 45–90' | Xoay vòng 4 việc: (a) **bài kiểm tra khách quan playbook** — chấm 10 setup theo GATE 7 bước, làm 2 lượt cách nhau ≥3 ngày, kết quả phải trùng; (b) phân xử 3 xung đột định nghĩa (MSS vs CHoCH vs CISD · IFVG hai nghĩa · SIBI nhận hai lần); (c) thu hoạch 12 định nghĩa `CONFIRMED` từ `ict_definitions.json` sang concept note; (d) tạo 3 note còn thiếu (PD Arrays/MOC · Silver Bullet · `30-Sell-side-Liquidity` nếu GĐ0 chưa làm). |
| 🌙 Đóng vòng 20' | Daily Summary + đếm ngày log của tuần (đây là **gate chính của GĐ1**, không phải số mẫu). |

> [!tip] Playbook A+ đã tồn tại từ 2026-09-07 (v1.0, [[2022 Model A+ Setup]])
> Nút thắt "playbook chưa thành văn" đã được mở sớm. Từ hôm nay **mọi phiên replay đều chấm bằng GATE 7 bước của playbook** — dùng nó ngay; còn *bài kiểm tra tính khách quan* thì vẫn thuộc GĐ1 theo đúng thứ tự gate. Không nhảy cóc, nhưng cũng không để công cụ đã có nằm không.

### 🔒 GĐ2 — Dựng edge · 2027-01 → 2027-05

Gate: 200 mẫu NAS100+EURUSD có `r_net` · expectancy ≥ +0.3R trên 100 mẫu gần nhất.

| Nhịp | Số mẫu/ngày | Mẫu/tuần |
|---|---:|---:|
| 🔵 Ngày chuẩn (T2–T6) | 2 | 10 |
| 🟣 Ngày sâu (T7 hoặc CN) | 3 | +3 |
| **Tổng thực tế** | — | **~10–13** → 200 mẫu trong **~18–20 tuần** |

- Mỗi phiên ghi **dòng survivorship**: số setup đã xét / số vào lệnh / số bỏ qua + **vì sao bỏ**. Không có dòng này thì win rate vô nghĩa.
- Mỗi **25 mẫu**: một debate vòng 2 — **1 file markdown**, không contract/schema, lưu ở `10 - Market Analysis/Debates/`.
- Checkpoint **50 / 100 / 200 mẫu**: win rate · average R · expectancy · **max losing streak** · phân rã theo session/symbol/grade → ghi vào [[Build a statistically validated backtest sample]].

### 🔒 GĐ3 — Ổn định (forward test demo) · 2027-06 → 2027-09

Gate: 3 tháng liên tiếp ≥+1% · max DD <4% · `risk_percent ≤ 0.5` ở **100%** lệnh.

- Buổi tối chuyển từ "đóng vòng 20'" sang **nhịp killzone đầy đủ** theo [[2022 Model A+ Setup]] §1 + §5.
- Luật cứng mỗi ngày: **≤2 lệnh · risk ≤0,5% · daily stop cá nhân −1% · thua 2 lệnh liên tiếp = hết ngày**.
- **Ngày không có setup vẫn phải có note** — "no-trade day" đúng playbook là một ngày THẮNG về quy trình, và hiện chưa có chỗ nào ghi nhận loại thắng đó.
- Chỉ số tuần: % `followed_plan` (>90%) · mistake rate · expectancy forward vs backtest (lệch xa = đang trade khác playbook).

### 🔒 GĐ4 trở đi

Nhịp một ngày thi đã viết sẵn ở **Phụ lục B** của [[03 - Lộ trình chi tiết - Từ số 0 đến Funded 100K]]. Không chi tiết hoá bây giờ — sẽ lỗi thời trước khi dùng tới.

## 5. Nhịp tuần

| Khi nào | Thời lượng | Việc | Bằng chứng |
|---|---|---|---|
| **Thứ Hai** | 10' | Mở tuần: chọn **3 concept** cho tuần · chọn `symbol_focus` (NAS100/EURUSD) · đặt `day_type` dự kiến cho 7 ngày | Ghi ngay trong file task T2 |
| **Thứ Sáu** | 10' | Vệ sinh dữ liệu: mẫu tuần này đã có `r_net` chưa? note nào thiếu Lesson Learned? concept đã ôn có `last_reviewed` chưa? | Sửa tại chỗ, không lập danh sách nợ |
| **Chủ Nhật** | 45–60' | Đóng tuần: weekly review theo [[Weekly_Trading_Review_ICT_Obsidian]] → dán **1 dòng** vào [[02 - Skill Metrics]] → cập nhật `progress` mọi goal **theo tỉ lệ checkbox** → ghi số ngày log của tuần | 1 file weekly + 1 dòng bảng |

> [!warning] Dòng Skill Metrics phải dán TRONG ngày Chủ Nhật
> W27/W28 từng trễ 6–7 ngày mới dán bù; W29→W36 thì không bao giờ được dán. **Dòng dán muộn là dòng viết bằng ký ức** — và ký ức luôn tô hồng mức độ tuân thủ.

## 6. Nhịp tháng & mốc 90 ngày

- **Cuối tháng:** 1 file trong `00 - Inbox/04 - Monthly Review` (thư mục hiện trống) — đối chiếu gate của giai đoạn đang mở với [[01 - Roadmap]]. Trượt gate → **ở lại thêm 4 tuần**, không chuyển giai đoạn chỉ vì hết thời gian dự kiến.
- **Mỗi 90 ngày:** kiểm tra gate + **đọc lại note của chính mình cách 6 tháng** — đây là cách trực tiếp nhất để *nhìn thấy* năng lực đã tăng khi plateau đang che mất tiến bộ.
- **Mốc 90 ngày đang chạy: 2026-09-07 → 2026-12-06.** Đích: hệ đo sạch (gate GĐ0) · playbook đã kiểm tính khách quan · **≥8 tuần liên tiếp ≥5 ngày log**.

## 7. Bằng chứng cho mỗi khối — chống overtick

> [!danger] Overtick là lỗi đã tái diễn nhiều lần trong hệ thống này
> 2026-07-10 tick 2 concept mà `last_reviewed` không đổi. 2026-07-12/13 tick "bảng lot size" khi file chưa tồn tại. Quy tắc: **`[x]` chỉ hợp lệ khi có FILE thay đổi.** Không có file đổi thì để `[ ]` và ghi lý do.

| Khối | Chỉ được tick `[x]` khi | File phải thay đổi |
|---|---|---|
| 🧠 Retrieval | Đã viết từ trí nhớ **rồi mới** đối chiếu note, và đã chấm điểm | `02 - Trading Knowledge/Concepts/<...>.md` — `last_reviewed`, `confidence`, bảng `## 13` |
| 📊 Replay | Có pre-registration ghi **trước** khi tua tiếp + dòng survivorship | `04 - Backtesting/YYYY-MM-DD/<...>.md` |
| 📊 Sửa hệ đo | Khuyết tật đã hết, kiểm tra lại trực tiếp | File bị sửa + checkbox trong goal GĐ0 |
| 🌙 Đóng vòng | Daily Summary tồn tại và có **số**, không phải cảm nhận | `00 - Inbox/02 - Daily Summary/YYYY-MM-DD - Daily summary.md` |
| 📅 Đóng tuần | Dòng Skill Metrics đã dán | `09 - Goal Tracking/02 - Skill Metrics.md` |

## 8. Luật chống đứt chuỗi — quyết TRƯỚC, không quyết lúc đang mệt

| Tình huống | Phản ứng đã cam kết |
|---|---|
| Mệt / deadline dev / đi công tác | Chuyển sang 🟢 **ngày tối thiểu 20'**. Không bỏ ngày. |
| Không thể mở laptop cả ngày | Phiên bản mobile: retrieval nói to 30 giây + 1 dòng log trên điện thoại. Đánh `day_type: minimum-mobile`, **tối đa 1 lần/tuần**. |
| Bỏ 1 ngày | Ngày mai KHÔNG làm bù gấp đôi. Quay lại 🔵 bình thường; chuỗi tuần vẫn sống nếu tuần đó ≥5 ngày. |
| Đứt >1 tuần | **Chuỗi về 0.** Ghi vào [[02 - Skill Metrics]] như một sự thật (đã làm đúng thế cho W29→W36). Không backfill số giả. |
| Cảm giác "phải làm 8h để bù" | Đó là pattern đã sụp tháng 7. Trần 4h là trần cứng — giờ dư dùng cho việc *khác loại* (viết note, dọn dữ liệu), không phải thêm replay. |
| Thua 2 lệnh liên tiếp (từ GĐ3) | Hết ngày. Đóng chart. |
| Tháng demo âm | Không đổi hệ thống. Phân loại **thua-đúng-hệ-thống** vs **thua-do-phá-luật**. |

## 9. Chuỗi hiện tại (tự đếm — nguồn: Daily Summary)

```dataviewjs
function ymd(v){
  if(!v) return null;
  if(typeof v === "string") return v.slice(0,10);
  if(v.toISODate) return v.toISODate();
  return String(v).slice(0,10);
}
const dt = dv.luxon.DateTime;
const days = new Set();
for(const p of dv.pages('"00 - Inbox/02 - Daily Summary"')){
  const d = ymd(p.date) || ymd(p.file.name);
  if(d && /^\d{4}-\d{2}-\d{2}$/.test(d)) days.add(d);
}
const today = dt.now().startOf("day");
let last7 = 0;
for(let i = 0; i < 7; i++){ if(days.has(today.minus({days:i}).toISODate())) last7++; }
let streak = 0;
let cur = days.has(today.toISODate()) ? today : today.minus({days:1});
while(days.has(cur.toISODate())){ streak++; cur = cur.minus({days:1}); }
function wk(d){ return d.weekYear + "-W" + String(d.weekNumber).padStart(2,"0"); }
const perWeek = {};
for(const d of days){ const k = wk(dt.fromISO(d)); perWeek[k] = (perWeek[k] || 0) + 1; }
let weeks = 0;
let w = today.startOf("week").minus({weeks:1});
while((perWeek[wk(w)] || 0) >= 5){ weeks++; w = w.minus({weeks:1}); }
const thisWeek = perWeek[wk(today)] || 0;
function card(label, value, sub){
  return `<div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;"><div style="font-size:12px;opacity:.7;">${label}</div><div style="font-size:28px;font-weight:700;">${value}</div><div style="font-size:11px;opacity:.6;">${sub || ""}</div></div>`;
}
dv.container.innerHTML = `
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin:16px 0;">
  ${card("Tuần liên tiếp ≥5 ngày", weeks, "gate GĐ1 cần 8")}
  ${card("Ngày log / 7 ngày qua", last7 + "/7", "mục tiêu ≥5")}
  ${card("Chuỗi ngày liên tiếp", streak, "tham khảo, không phải gate")}
  ${card("Tuần này (" + wk(today) + ")", thisWeek + " ngày", "tính tới hôm nay")}
</div>`;
```

> [!note] Vì sao đếm bằng Daily Summary chứ không bằng file task
> File task chứng minh *đã lên kế hoạch*; Daily Summary chứng minh *đã đóng vòng*. Chỉ số chuỗi phải đo cái thứ hai.

## Liên kết
- Lộ trình tổng: [[01 - Roadmap]] · Chi tiết 8 giai đoạn: [[03 - Lộ trình chi tiết - Từ số 0 đến Funded 100K]]
- Phương pháp luyện tập: [[04 - Phương pháp luyện tập, vòng lặp AI & giữ động lực]] · Chỉ số: [[02 - Skill Metrics]]
- Playbook thi hành: [[2022 Model A+ Setup]] · Checklist: [[ICT 2022 Entry Checklist]]
- Template ngày: [[Daily_Tasks_Template]] · Dashboard: [[00 - Goal Dashboard]]
