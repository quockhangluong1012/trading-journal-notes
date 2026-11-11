# -*- coding: utf-8 -*-
from chdraw import *
import sys


def side_steps(f, x, y, w, rows, size=11.8, gap=8):
    yy = y
    for n, c, a, b in rows:
        f.badge(x + 12, yy - 4, n, c)
        f.t(x + 30, yy, a, 12.5, True, c)
        yy = f.p(x + 30, yy + 17, b, w - 30, size) + gap
    return yy


# ------------------------------------------------------------------ 14 character weakening
def fig14():
    f = F(14, 'Character-Suy-Yeu-Truoc-CHoCH', 'Character thường suy yếu TRƯỚC khi CHoCH xuất hiện',
          'CHoCH là “phán quyết” cuối cùng. Trước đó thường (không phải luôn luôn) có những dấu hiệu nhỏ hơn. Hai panel dưới cùng kết thúc bằng một CHoCH ↓ giống hệt nhau.', h=600)
    y0 = f.top + 4; H = 600 - y0 - 46
    A = [(0, 40), (1.6, 60), (2.4, 54), (3.6, 68), (4.4, 62), (5.2, 70), (6.4, 57), (7.2, 63), (8.4, 52)]
    B = [(0, 40), (1.6, 60), (2.4, 54), (3.6, 68), (4.4, 62), (5.6, 76), (6.6, 50)]
    for k, (pts, ttl, col) in enumerate([(A, 'Có báo trước (LuxAlgo gọi là CHoCH+ / “supported”)', CHC), (B, 'Không báo trước (“leading” CHoCH)', WARN)]):
        x = 28 + k * 478; w = 466
        f.card(x, y0, w, H, ttl, num=k + 1, tcolor=col)
        ch = Chart(f, x + 20, y0 + 56, w - 40, 260, 36, 82, 9)
        ch.level(62, 4.4, 8, PROT, 'protected low', pos='r', dy=-6, sw=1.4)
        zz(ch, pts, INK, 2.4); dots(ch, pts[1:])
        if k == 0:
            ch.lab(5.2, 70, 'đỉnh chỉ nhỉnh hơn\n(chân tăng ngắn lại)', dy=-10, color=WARN, size=10)
            ch.lab(7.2, 63, 'hồi yếu, đỉnh thấp hơn', dy=-9, color=WARN, size=10)
            ch.lab(6.4, 57, 'CHoCH ↓', dx=-6, dy=16, color=CHC, size=10.5, anchor='end')
            txt = ['Chân tăng cuối ngắn hơn hẳn các chân trước.', 'Pullback sâu và nhanh hơn thường lệ.', 'Sau CHoCH, cú hồi không vượt nổi đỉnh cũ.',
                   'Những dấu hiệu này là [OBSERVABLE]. Chúng tốt hơn hay xấu hơn cho CHoCH là [HYPOTHESIS].']
        else:
            ch.lab(5.6, 76, 'đỉnh mới rất mạnh', dy=-9, color=UP, size=10)
            ch.lab(6.6, 50, 'CHoCH ↓ đột ngột', dx=-6, dy=16, color=CHC, size=10.5, anchor='end')
            txt = ['Chân tăng cuối còn mạnh hơn trước.', 'Không có dấu hiệu yếu nào trước đó.', 'CHoCH đến từ một cú đảo rất nhanh (thường do tin tức hoặc cú quét lớn).',
                   'Loại này khó đoán trước và cũng dễ là “cú giật” rồi tiếp diễn.']
        yy = y0 + 336
        for t_ in txt:
            f.t(x + 22, yy, '•', 12, True, col); yy = f.p(x + 34, yy, t_, w - 56, 12) + 4
    f.foot('Thuật ngữ CHoCH+ / “supported CHoCH” lấy từ tài liệu indicator của LuxAlgo — một quy ước của công cụ, không phải định nghĩa chuẩn của ICT.')
    return f.save()


# ------------------------------------------------------------------ 15 before / at / after
def fig15():
    f = F(15, 'Truoc-Luc-Sau-CHoCH', 'Trước — Lúc — Sau: điều gì thật sự thay đổi khi một CHoCH xảy ra?',
          'Ba ảnh chụp cùng một chart ở ba thời điểm. Vùng xám là tương lai chưa biết. Đọc kỹ dòng “chưa biết”: đó là phần hay bị bỏ qua nhất.', h=650)
    y0 = f.top + 4
    pts = [(0, 40), (1.5, 58), (2.3, 51), (3.8, 68), (4.6, 60), (5.6, 64), (6.6, 48), (7.4, 55)]
    cols = [('TRƯỚC: giá đang lùi về', 5.6, ['Biết: trạng thái TĂNG; protected low = 51.', 'Đổi: chưa có gì.', 'Chưa biết: lần lùi này dừng ở đâu.']),
            ('LÚC: nến đóng dưới 51', 6.6, ['Biết: protected low đã bị đóng nến xuyên → câu “đang tăng” ở lớp này hết hiệu lực.', 'Đổi TỰ ĐỘNG: trạng thái lớp này chuyển sang “đang thử giảm”; mức tham chiếu mới phía trên = đỉnh 68.', 'Chưa biết: đây là đảo chiều, pullback sâu của khung lớn, hay range.']),
            ('SAU: giá hồi lên', 7.4, ['Biết thêm: giá hồi nhưng chưa vượt 68.', 'Đổi: nếu tạo đỉnh thấp hơn rồi thủng 48 → BOS ↓ đầu tiên, cấu trúc giảm mới có hình dạng.', 'Chưa biết: vẫn có thể vượt 68 → CHoCH thất bại.'])]
    for k, (ttl, cut, lines) in enumerate(cols):
        x = 28 + k * 318; w = 306
        f.card(x, y0, w, 540, ttl, num=k + 1, tcolor=CHC if k == 1 else INK)
        ch = Chart(f, x + 16, y0 + 50, w - 32, 200, 40, 74, 9)
        vis = [p for p in pts if p[0] <= cut]
        if k == 0: vis = vis[:-1] + [(5.6, 56)]
        ch.level(51, 2.3, [5.0, 6.6, 7.4][k], PROT if k == 0 else CHC, 'protected low' if k == 0 else 'đã bị phá', pos='l', dy=-6 if k == 0 else 15, sw=1.3)
        zz(ch, vis, INK, 2.3); dots(ch, vis[1:])
        lastx = vis[-1][0]
        ch.fog(lastx + 0.4, 'chưa biết')
        if k >= 1: ch.lab(6.6, 48, 'CHoCH ↓', dy=15, dx=-8, color=CHC, size=10, anchor='end')
        yy = y0 + 280
        for j, l in enumerate(lines):
            c = [GOOD, BOSC, WARN][j]
            yy = f.p(x + 16, yy, l, w - 32, 12, c) + 10
    f.foot('Câu then chốt: CHoCH thay đổi BẢN ĐỒ (mô tả cấu trúc) một cách chắc chắn. Nó KHÔNG thay đổi chắc chắn điều giá sẽ làm tiếp theo.')
    return f.save()


# ------------------------------------------------------------------ 16 mechanism
def fig16():
    f = F(16, 'Co-Che-Khop-Lenh-Sau-CHoCH', 'Cơ chế: vì sao lần trước giá bật lên, còn lần này giá rơi xuyên qua?',
          'Mô hình đơn giản hóa của sổ lệnh quanh một đáy. Thanh xanh = lệnh CHỜ MUA (bị động). Mũi tên đỏ = lệnh BÁN CHỦ ĐỘNG. Thanh tím = lệnh dừng lỗ bán nằm dưới đáy.', h=620, tag='MARKET MECHANICS')
    y0 = f.top + 4; H = 620 - y0 - 46
    levels = ['53', '52', '51 (đáy)', '50', '49', '48', '47']
    panels = [('Lần trước: tạo ra Higher Low', [3, 4, 9, 4, 3, 2, 2], [0, 0, 0, 0, 0, 0, 0], [4, 3, 0, 0, 0, 0, 0], 2, 'Lệnh bán chủ động đến, ăn bớt lệnh chờ mua ở 53, 52… tới 51 thì gặp một “bức tường” lệnh chờ mua dày. Bán không ăn hết → giá ngừng giảm và bật lên. Ta thấy một HL.'),
              ('Lần này: CHoCH', [2, 2, 3, 1, 1, 1, 2], [0, 0, 0, 5, 4, 0, 0], [4, 3, 4, 3, 2, 2, 0], 6, 'Lệnh chờ mua mỏng hơn (có thể đã bị rút). Bán ăn xuyên 51 → kích hoạt các lệnh dừng lỗ bán bên dưới → chúng thành lệnh bán chủ động mới → giá trượt qua nhiều mức rất nhanh: một nến thân to (displacement).')]
    for k, (ttl, bids, stops, sells, stopat, txt) in enumerate(panels):
        x = 28 + k * 478; w = 466
        f.card(x, y0, w, H - 88, ttl, num=k + 1, tcolor=CHC if k else DISP)
        ty = y0 + 56; rh = 30
        for j, lv in enumerate(levels):
            yy = ty + j * rh
            f.r(x + 16, yy, w - 32, rh - 4, fill='#F9FAFB' if j != 2 else '#FEF3C7', stroke=BORDER, sw=0.8, rx=4)
            f.t(x + 26, yy + 18, lv, 11, True, PROT if j == 2 else SUB)
            if bids[j]: f.r(x + 100, yy + 5, bids[j] * 16, rh - 14, fill=DISP, stroke=None, rx=3, op=0.75)
            if stops[j]: f.r(x + 100 + bids[j] * 16 + 4, yy + 5, stops[j] * 16, rh - 14, fill=SWP, stroke=None, rx=3, op=0.75)
            if sells[j]: f.arrow(x + w - 24, yy + rh / 2 - 2, x + w - 24 - sells[j] * 18, yy + rh / 2 - 2, DN, 2.4, size=8)
        stop_y = ty + stopat * rh
        f.arrow(x + w - 40, ty + 6, x + w - 40, stop_y + rh - 8, INK, 1.8, '5,4')
        f.t(x + w - 46, stop_y + rh + 12, 'giá dừng ở đây' if k == 0 else 'giá trượt tới đây', 10.5, True, INK, 'end')
        f.p(x + 18, ty + 7 * rh + 40, txt, w - 36, 12.2)
    f.note(28, y0 + H - 74, 944, 'Trên chart OHLC ta KHÔNG nhìn thấy bảng này. Ta chỉ thấy kết quả (giá đóng dưới 51, nến thân to). Câu “phe mua đã bỏ cuộc” là [INTERPRETATION]; “ai” đã bán và “vì sao” là [NOT ESTABLISHED].', BAD, None, 12)
    f.foot('Cơ chế lệnh chờ / lệnh chủ động / lệnh dừng lỗ là [MARKET MECHANICS] được nghiên cứu học thuật ủng hộ (ví dụ Osler 2003 về lệnh dừng lỗ tụ quanh số tròn). Độ dày từng mức trong hình là minh họa.')
    return f.save()


# ------------------------------------------------------------------ 17 break significance ladder
def fig17():
    f = F(17, 'Nam-Cap-Do-Pha-Cau-Truc', 'Không phải cú phá nào cũng có ý nghĩa như nhau: năm cấp độ swing bị phá',
          'Cùng một xu hướng tăng. Mỗi đáy có “trọng lượng” khác nhau. Cú phá càng xuống sâu trong bảng, nó càng xoá được nhiều câu chuyện hơn.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 46
    f.card(28, y0, 470, H)
    pts = [(0, 30), (2, 52), (3, 44), (5, 70), (5.6, 66), (6, 68), (6.4, 64.5), (6.8, 66), (7.2, 63), (8, 61), (8.6, 63), (9.8, 80), (10.3, 77.5), (10.6, 78.6), (11, 76.6)]
    ch = Chart(f, 46, y0 + 30, 436, H - 60, 24, 86, 11.6)
    marks = [(10.3, 77.5, 'L1', MUTE), (8.6, 63, 'L2', STR), (8, 61, 'L3', BOSC), (8, 61, '', BOSC), (3, 44, 'L5', BAD)]
    zz(ch, pts, INK, 2.2)
    ch.level(77.5, 10.3, 10.6, MUTE, None, dash='3,3', sw=1)
    ch.level(61, 8, 10.6, PROT, 'protected low = L4', pos='r', dy=17, sw=1.5)
    ch.level(44, 3, 10.6, BAD, 'đáy HTF / dealing range = L5', pos='r', dy=17, sw=1.3)
    ch.lab(10.3, 77.5, 'L1 micro', dx=-6, dy=16, color=SUB, size=10, anchor='end')
    ch.lab(6.4, 64.5, 'L2 internal', dx=-4, dy=16, color=STR, size=10, anchor='end')
    ch.lab(8.6, 63, 'L3', dy=-8, color=BOSC, size=10)
    for i, p in pts[1:]: ch.dot(i, p, INK, 2.8)
    x = 512; w = 460
    rows = [['Cấp', 'Phá nó nói lên điều gì?'],
            ['L1 Micro', 'Gần như không gì. Nhiễu trong một cụm vài nến.'],
            ['L2 Internal', 'Đợt hồi đang sâu hơn. Lớp nhỏ có thể đổi chiều (CHoCH internal).'],
            ['L3 Trung gian', 'Một nhịp con của chân sóng bị xoá. Cảnh báo nhưng chưa đổi lớp chính.'],
            ['L4 Protected', 'Cú tăng gần nhất bị xoá. Trạng thái của lớp/khung này đổi: CHoCH đúng nghĩa.'],
            ['L5 External / HTF', 'Ranh của dealing range hoặc swing khung lớn. Đổi câu chuyện của cả khung lớn.']]
    f.card(x, y0, w, H, 'Bảng cấp độ (khung nghiên cứu, không phải luật)')
    yb = f.table(x + 16, y0 + 50, [130, w - 32 - 130], rows, size=11.5, colors={(1, 0): SUB, (2, 0): STR, (3, 0): BOSC, (4, 0): PROT, (5, 0): BAD})
    f.p(x + 16, yb + 22, 'Trọng lượng của một swing đến từ việc nó đã LÀM gì (phóng ra BOS, giới hạn range, bị quét…), không đến từ việc nó “trông to”. Thang L1–L5 dùng chung với note 21 và 57.', w - 32, 11.8, SUB)
    f.foot('Thang L1–L5 là [FRAMEWORK-DEPENDENT]: cách chia cấp là một quy ước nghiên cứu của vault, cần khai báo trước khi backtest.')
    return f.save()


# ------------------------------------------------------------------ 18 not reversal
def fig18():
    f = F(18, 'CHoCH-Khong-Phai-Dao-Chieu', 'CHoCH không phải “đảo chiều”: năm bậc bằng chứng khác nhau',
          'Mỗi bậc cần THÊM thông tin, và vì vậy đến MUỘN hơn. Đa số sai lầm đến từ việc nhảy từ bậc 1 lên bậc 5 trong một bước.', h=620)
    y0 = f.top + 4
    steps = [('Thay đổi tính cách', 'Một cú phá ngược trạng thái ở MỘT lớp, MỘT khung.', 'đèn vàng nháy', WARN),
             ('Cảnh báo sớm', 'Có thêm dấu hiệu: displacement, cú quét trước đó, vị trí HTF hợp lý.', 'đèn vàng', WARN),
             ('Shift internal', 'Lớp nhỏ đã có đáy/đỉnh mới đúng chiều mới (HL hoặc LH) — vẫn trong khung lớn cũ.', 'vàng → xanh nhạt', TEAL),
             ('Shift external', 'Protected swing của LỚP LỚN bị phá, không chỉ lớp nhỏ.', 'xanh nhạt', TEAL),
             ('Đảo chiều được xác nhận', 'Lớp lớn có đáy/đỉnh mới đúng chiều mới VÀ một BOS đầu tiên theo chiều mới.', 'xanh', GOOD)]
    bw = 178; gap = 11
    for k, (a, b, light, c) in enumerate(steps):
        x = 28 + k * (bw + gap); yt = y0 + 300 - k * 52
        f.r(x, yt, bw, 450 - (yt - y0) - 4, fill=CARD, stroke=c, sw=1.6, rx=10)
        f.badge(x + 22, yt + 22, k + 1, c)
        f.p(x + 40, yt + 26, a, bw - 50, 13, c, bold=True, lh=1.25)
        f.p(x + 12, yt + 70, b, bw - 24, 11.6)
        f.pill(x + 12, y0 + 410, light, c, 10)
    f.arrow(60, y0 + 20, 900, y0 + 20 - 0, SUB, 1.6, '6,4')
    f.t(480, y0 + 12, 'thêm bằng chứng — và thêm độ trễ', 11, True, SUB, 'middle')
    f.note(28, y0 + 456, 944, 'Một CHoCH ở bậc 1 vẫn có ích: nó cho phép ĐẶT CÂU HỎI (“xu hướng cũ còn không?”). Nó chưa cho phép TRẢ LỜI (“xu hướng mới đã bắt đầu”).', CHC, None, 12.5)
    f.foot('Bậc 3–5 tương ứng thang G2–G3 và quan hệ nhiều khung ở note 21. Năm bậc ở đây là khung tư duy, không phải tiêu chuẩn ICT.')
    return f.save()


# ------------------------------------------------------------------ 19 bullish choch 7 steps
def bull_chart(f, x, y, w, h, upto=None, labels=True, fv=True):
    cs, tn = bull_seq()
    ch = Chart(f, x, y, w, h, 50, 88, len(cs) + 1)
    k = len(cs) if upto is None else upto
    if fv and k > 31:
        for (i, lo, hi) in fvgs(cs, 28, 32):
            if i == 30: ch.zone(29, k - 1, lo, hi, FVGC, op=0.13, dash='4,3')
    ch.level(72.3, 18, min(k - 1, 33), PROT, 'protected high (LH2)' if labels else None, pos='l', dy=-6, sw=1.5)
    ch.level(56.2, 22, min(k - 1, 28), SWP, None, dash='4,3', sw=1.2)
    ch.level(61.8, 25, min(k - 1, 29), MUTE, None, dash='3,3', sw=1)
    ch.candles(cs, upto=upto)
    return ch, cs


def fig19():
    f = F(19, 'Bullish-CHoCH-7-Giai-Doan', 'Bullish CHoCH, từng giai đoạn một',
          'Sơ đồ dựng. Giá đang trong cấu trúc GIẢM. Đọc theo số. Chú ý: cú phá đỉnh nhỏ ở ⑤ đến TRƯỚC cú phá protected high ở ⑥.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 60
    f.card(28, y0, 600, H)
    ch, cs = bull_chart(f, 44, y0 + 30, 570, H - 52)
    ch.lab(10, 79.3, 'LH1', dy=-8, color=DN); ch.lab(14, 62.7, 'LL1', dy=15, color=DN)
    ch.lab(22, 56.2, 'LL2', dx=-12, dy=15, color=DN)
    ch.badge(14, 62.7, 1, DN, dy=38); ch.badge(22, 56.2, 2, DN, dy=38, dx=-12)
    ch.badge(27, 54.6, 3, SWP, dy=22)
    ch.badge(26, 64, 4, UP, dx=-4)
    ch.badge(28, 62.4, 5, STR, dx=-20, dy=-14)
    ch.badge(31, 77, 6, CHC, dy=-30)
    ch.badge(34, 69.2, 7, BOSC, dy=26)
    ch.lab(31, 77.3, 'đóng trên LH2', dy=-8, dx=-10, color=CHC, anchor='end')
    ch.lab(38, 84.3, 'BOS ↑', dy=-8, color=BOSC)
    ch.ztext(37.2, 69.6, 'FVG', FVGC, 10)
    x = 642; w = 330
    f.card(x, y0, w, H, 'Bảy giai đoạn')
    rows = [(1, DN, 'Cấu trúc giảm', 'Đỉnh thấp dần (LH), đáy thấp dần (LL).'),
            (2, DN, 'Thêm một LL', 'Giá thủng LL1 (BOS ↓). Đỉnh phóng ra cú đó — LH2 — là protected high.'),
            (3, SWP, 'Quét đáy', 'Râu nến chọc dưới LL2 rồi đóng lại phía trên: sell-side bị quét.'),
            (4, UP, 'Giá đi lên', 'Nến tăng thân to xuất hiện liên tiếp.'),
            (5, STR, 'Phá đỉnh nhỏ', 'Vượt đỉnh internal gần nhất. Mới là CHoCH lớp nhỏ.'),
            (6, CHC, 'CHoCH', 'Thân nến đóng trên protected high LH2, có displacement và FVG.'),
            (7, BOSC, 'Cấu trúc mới thành hình', 'Hồi vào FVG, giữ được, rồi vượt đỉnh vừa tạo: BOS ↑ đầu tiên.')]
    side_steps(f, x + 14, y0 + 52, w - 28, rows, 11.4, 6)
    f.foot('Bước 3 (quét) và FVG ở bước 6 là bằng chứng CHẤT LƯỢNG, không phải điều kiện bắt buộc của định nghĩa CHoCH. Bước 7 là thông tin TƯƠNG LAI tại thời điểm bước 6.')
    return f.save()


def mini3(f, num, slug, title, sub, sets, flip=False, foot=''):
    f2 = F(num, slug, title, sub, h=600)
    y0 = f2.top + 4
    for k, (ttl, col, pts, lv, marks, txt, verdict, vc) in enumerate(sets):
        x = 28 + k * 318; w = 306
        f2.card(x, y0, w, 452, ttl, num=k + 1, tcolor=col)
        ch = Chart(f2, x + 16, y0 + 52, w - 32, 220, 36, 84, 9, flip)
        for (p, a, b, c, lab, dy) in lv:
            ch.level(p, a, b, c, lab, pos='r', dy=dy, sw=1.3)
        for z in marks.get('zones', []):
            ch.zone(*z)
        zz(ch, pts, INK, 2.3); dots(ch, pts[1:])
        for (i, p, t_, c, dy, dx, an) in marks.get('labs', []):
            ch.lab(i, p, t_, dy=dy, dx=dx, color=c, size=10, anchor=an)
        f2.p(x + 16, y0 + 300, txt, w - 32, 11.8)
        f2.pill(x + 16, y0 + 414, verdict, vc, 11)
    f2.foot(foot)
    return f2.save()


BULL3 = [('CHoCH chất lượng tốt', GOOD, [(0, 76), (1, 66), (2, 72), (3, 58), (3.8, 63), (4.5, 50), (6, 74), (6.8, 68), (8.2, 80)],
          [(63, 3.8, 8, PROT, 'protected high', -6)], {'labs': [(4.5, 50, 'quét đáy', SWP, 15, 0, 'middle'), (6, 74, 'phá mạnh', CHC, -8, 0, 'middle'), (8.2, 80, 'BOS ↑', BOSC, -8, 0, 'middle')],
                                                         'zones': [(5, 5.6, 61, 66, FVGC, None, 'tl', '4,3', 0.15)]},
          'Quét đáy cũ → nhiều nến tăng thân to → đóng xa phía trên protected high, để lại FVG → hồi giữ được → BOS ↑. Đủ bằng chứng cho cả “cảnh báo” lẫn “cấu trúc mới thành hình”.', 'Valid CHoCH → đã lên bậc 3', GOOD),
         ('CHoCH yếu', WARN, [(0, 76), (1, 66), (2, 72), (3, 58), (3.8, 63), (4.6, 56), (5.2, 60), (5.8, 58.5), (6.6, 64), (7.2, 62), (8.2, 65)],
          [(63, 3.8, 8, PROT, 'protected high', -6)], {'labs': [(4.6, 56, 'không quét', SUB, 15, 0, 'middle'), (6.6, 64, 'bò qua', WARN, 16, 6, 'middle')]},
          'Không quét đáy nào. Giá “bò” lên bằng nến nhỏ chồng lên nhau và đóng nhỉnh hơn protected high một chút. Đây vẫn là CHoCH theo định nghĩa, nhưng ít thông tin.', 'Weak CHoCH → chờ thêm', WARN),
         ('CHoCH thất bại', BAD, [(0, 76), (1, 66), (2, 72), (3, 58), (3.8, 63), (4.5, 52), (5.8, 66), (6.6, 60), (7.4, 62), (8.6, 46)],
          [(63, 3.8, 8, PROT, 'protected high', -6), (52, 4.5, 8, SWP, 'đáy vừa tạo', 15)], {'labs': [(5.8, 66, 'CHoCH ↑', CHC, -8, 0, 'middle'), (8.6, 46, 'thủng đáy', BAD, 15, -4, 'end')]},
          'Có CHoCH, nhưng rồi giá không tạo được đáy cao hơn mà thủng luôn đáy vừa tạo. Cấu trúc giảm tiếp diễn. CHoCH đã là một cảnh báo SAI.', 'CHoCH failed', BAD)]


def fig20():
    return mini3(None, 20, 'Bullish-CHoCH-Tot-Yeu-That-Bai', 'Ba bullish CHoCH: tốt, yếu, và thất bại',
                 'Cả ba đều đóng nến trên cùng một protected high. Khác nhau ở ĐIỀU XẢY RA TRƯỚC, TRONG và SAU cú phá.', BULL3,
                 foot='Phân loại “tốt/yếu” ở ô 1–2 dựa trên thông tin CÓ tại thời điểm phá. Nhãn “thất bại” ở ô 3 chỉ biết được SAU — đó là hindsight, dùng để học chứ không dùng để vào lệnh.')


def fig21():
    f = F(21, 'Bearish-CHoCH-7-Giai-Doan', 'Bearish CHoCH, từng giai đoạn một',
          'Ảnh gương của hình 19. Giá đang trong cấu trúc TĂNG. Cú phá đáy nhỏ ở ⑤ đến trước cú phá protected low ở ⑥.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 60
    f.card(28, y0, 600, H)
    cs, tn = bear_seq()
    ch = Chart(f, 44, y0 + 30, 570, H - 52, 52, 90, len(cs) + 1)
    for (i, lo, hi) in fvgs(cs, 28, 32, bull=False):
        if i == 30: ch.zone(29, 35, lo, hi, FVGC, op=0.13, dash='4,3')
    ch.level(67.7, 18, 33, PROT, 'protected low (HL2)', pos='l', dy=17, sw=1.5)
    ch.level(83.8, 22, 28, SWP, None, dash='4,3', sw=1.2)
    ch.level(78.2, 25, 29, MUTE, None, dash='3,3', sw=1)
    ch.candles(cs)
    ch.lab(10, 60.7, 'HL1', dy=15, color=UP); ch.lab(14, 77.3, 'HH1', dy=-8, color=UP)
    ch.lab(22, 83.8, 'HH2', dx=-12, dy=-8, color=UP)
    ch.badge(14, 77.3, 1, UP, dy=-30); ch.badge(22, 83.8, 2, UP, dy=-30, dx=-12)
    ch.badge(27, 85.4, 3, SWP, dy=-22)
    ch.badge(26, 76, 4, DN, dx=-4)
    ch.badge(28, 77.6, 5, STR, dx=-20, dy=14)
    ch.badge(31, 63, 6, CHC, dy=30)
    ch.badge(34, 70.8, 7, BOSC, dy=-26)
    ch.lab(31, 62.7, 'đóng dưới HL2', dy=15, dx=-10, color=CHC, anchor='end')
    ch.lab(38, 55.7, 'BOS ↓', dy=15, color=BOSC)
    ch.ztext(37.2, 70.4, 'FVG', FVGC, 10)
    x = 642; w = 330
    f.card(x, y0, w, H, 'Bảy giai đoạn')
    rows = [(1, UP, 'Cấu trúc tăng', 'Đáy cao dần (HL), đỉnh cao dần (HH).'),
            (2, UP, 'Thêm một HH', 'Giá vượt HH1 (BOS ↑). Đáy phóng ra cú đó — HL2 — là protected low.'),
            (3, SWP, 'Quét đỉnh', 'Râu nến nhô trên HH2 rồi đóng lại phía dưới: buy-side bị quét.'),
            (4, DN, 'Giá đi xuống', 'Nến giảm thân to liên tiếp.'),
            (5, STR, 'Phá đáy nhỏ', 'Thủng đáy internal gần nhất. Mới là CHoCH lớp nhỏ.'),
            (6, CHC, 'CHoCH', 'Thân nến đóng dưới protected low HL2, có displacement và FVG.'),
            (7, BOSC, 'Cấu trúc mới thành hình', 'Hồi vào FVG, bị từ chối, rồi thủng đáy vừa tạo: BOS ↓ đầu tiên.')]
    side_steps(f, x + 14, y0 + 52, w - 28, rows, 11.4, 6)
    f.foot('Phá một HL nhỏ (bước 5) KHÔNG phải bearish reversal. Chỉ khi protected low bị đóng nến xuyên (bước 6) trạng thái của lớp này mới đổi — và vẫn chỉ là cảnh báo.')
    return f.save()


BEAR3 = [('CHoCH chất lượng tốt', GOOD, [(0, 44), (1, 54), (2, 48), (3, 62), (3.8, 57), (4.5, 70), (6, 46), (6.8, 52), (8.2, 40)],
          [(57, 3.8, 8, PROT, 'protected low', 15)], {'labs': [(4.5, 70, 'quét đỉnh', SWP, -8, 0, 'middle'), (6, 46, 'phá mạnh', CHC, 15, 0, 'middle'), (8.2, 40, 'BOS ↓', BOSC, 15, 0, 'middle')],
                                                       'zones': [(5, 5.6, 54, 59, FVGC, None, 'tl', '4,3', 0.15)]},
          'Quét đỉnh cũ → nhiều nến giảm thân to → đóng xa dưới protected low, để lại FVG → hồi bị từ chối → BOS ↓.', 'Valid CHoCH → đã lên bậc 3', GOOD),
         ('CHoCH yếu', WARN, [(0, 44), (1, 54), (2, 48), (3, 62), (3.8, 57), (4.6, 64), (5.2, 60), (5.8, 61.5), (6.6, 56), (7.2, 58), (8.2, 55)],
          [(57, 3.8, 8, PROT, 'protected low', 15)], {'labs': [(4.6, 64, 'không quét', SUB, -8, 0, 'middle'), (6.6, 56, 'bò qua', WARN, -9, 6, 'middle')]},
          'Không quét đỉnh nào. Giá trôi xuống bằng nến nhỏ, đóng nhỉnh dưới protected low. Vẫn là CHoCH theo định nghĩa, nhưng ít thông tin.', 'Weak CHoCH → chờ thêm', WARN),
         ('CHoCH thất bại', BAD, [(0, 44), (1, 54), (2, 48), (3, 62), (3.8, 57), (4.5, 68), (5.8, 54), (6.6, 60), (7.4, 58), (8.6, 74)],
          [(57, 3.8, 8, PROT, 'protected low', 15), (68, 4.5, 8, SWP, 'đỉnh vừa tạo', -6)], {'labs': [(5.8, 54, 'CHoCH ↓', CHC, 15, 0, 'middle'), (8.6, 74, 'vượt đỉnh', BAD, -8, -4, 'end')]},
          'Có CHoCH, nhưng giá không tạo được đỉnh thấp hơn mà vượt luôn đỉnh vừa tạo. Cấu trúc tăng tiếp diễn. Phá một HL không phải là đảo chiều.', 'CHoCH failed', BAD)]


def fig22():
    return mini3(None, 22, 'Bearish-CHoCH-Tot-Yeu-That-Bai', 'Ba bearish CHoCH: tốt, yếu, và thất bại',
                 'Cả ba đều đóng nến dưới cùng một protected low. Chỉ phần TRƯỚC và SAU cú phá là khác.', BEAR3,
                 foot='Ô 3 là lý do phá một HL — kể cả protected — vẫn chưa phải bearish reversal: cần thêm một đỉnh thấp hơn và một BOS ↓.')


# ------------------------------------------------------------------ 23 BOS vs CHoCH vs MSS
def fig23():
    f = F(23, 'BOS-CHoCH-MSS-Cung-Mot-Cu-Pha', 'BOS, CHoCH hay MSS? Cùng một cú phá đỉnh — tên do TRẠNG THÁI TRƯỚC ĐÓ quyết định',
          'Đoạn cuối (khung tô) trong ba panel giống hệt nhau. Chỉ phần bên trái khác. Thêm displacement thì nhiều nguồn ICT gọi là MSS.', h=600)
    y0 = f.top + 4
    end = [(5, 52), (6.2, 70)]
    sets = [('Trước đó đang TĂNG', [(0, 30), (1.2, 44), (2, 38), (3.2, 56), (4, 49), (5, 52), (6.2, 70)], 'BOS ↑', BOSC, 'Phá THUẬN trạng thái → cấu trúc tăng được gia hạn.', 56),
            ('Trước đó đang GIẢM', [(0, 80), (1.2, 62), (2, 68), (3.2, 50), (4, 56), (5, 44), (6.2, 60)], 'CHoCH ↑', CHC, 'Phá NGƯỢC trạng thái, lần đầu, đúng protected high → “character” đổi. Chưa đòi displacement.', 56),
            ('Giống ô 2 + displacement', [(0, 80), (1.2, 62), (2, 68), (3.2, 50), (4, 56), (5, 44), (6.2, 66)], 'MSS ↑ (G1)', SWP, 'Cùng cú phá ngược trạng thái, nhưng bằng chân sóng nhanh, thân nến lớn, để lại FVG.', 56)]
    for k, (ttl, pts, nm, c, txt, lvl) in enumerate(sets):
        x = 28 + k * 318; w = 306
        f.card(x, y0, w, 410, ttl, num=k + 1, tcolor=c)
        ch = Chart(f, x + 18, y0 + 52, w - 36, 230, 26, 84, 7)
        if k == 0:
            ch.level(56, 3.2, 6.6, BOSC, 'đỉnh gần nhất', pos='l', dy=-6)
        else:
            ch.level(56, 4, 6.6, PROT, 'protected high', pos='l', dy=-6)
        ch.zone(4.8, 6.4, 40, 74, MUTE, op=0.07, dash='3,3')
        zz(ch, pts, INK, 2.3, ); dots(ch, pts[1:])
        if k == 2:
            ch.zone(5.5, 5.9, 49, 56, FVGC, op=0.18, dash=None)
        ch.lab(6.2, pts[-1][1], nm, dx=-10, dy=-9, color=c, size=11, anchor='end')
        f.p(x + 16, y0 + 310, txt, w - 32, 12)
    f.note(28, y0 + 420, 944, 'Không có định nghĩa chuẩn. Đa số tài liệu SMC: CHoCH = cú phá ngược trạng thái đầu tiên (không đòi displacement). innercircletrader.net, ICT 2022: MSS = cú phá đó CÓ displacement. Một số nơi dùng hai chữ như nhau. Vault này: dùng thang G0–G3 (hình 24).', BOSC, None, 12)
    f.foot('Hệ quả: trước khi gọi tên một cú phá, phải khai báo trạng thái hiện tại của lớp và khung đang xét. Không khai báo → hai người gọi cùng một nến bằng hai tên.')
    return f.save()


# ------------------------------------------------------------------ 24 G0-G3 ladder
def fig24():
    f = F(24, 'Thang-G0-G3-Cho-CHoCH', 'Thang bằng chứng của một CHoCH: từ “chạm vạch” đến “xây nhà mới bên kia”',
          'Cùng thang G0–G3 của note 21 (MSS), thêm bậc “chạm” ở dưới cùng. Mỗi bậc thêm thông tin VÀ thêm độ trễ.', h=620)
    y0 = f.top + 4
    rows = [('—', 'Chạm vạch', 'Râu nến xuyên qua protected swing, thân đóng lại bên trong.', 'chưa phải CHoCH', 'ngay khi râu xuất hiện', MUTE),
            ('G0', 'Bước qua vạch', 'Thân nến ĐÓNG ngoài protected swing, ngược trạng thái.', '“CHoCH” (đa số SMC)', 'lúc nến phá đóng cửa', CHC),
            ('G1', 'Bước MẠNH qua vạch', 'G0 + displacement: chân sóng nhanh, thân nến lớn, thường để lại FVG.', '“MSS” (ICT 2022, innercircletrader.net)', 'nến phá (FVG: nến kế tiếp)', SWP),
            ('G2', 'Đứng vững bên kia', 'G1 + giá không đóng ngược trở lại qua mức trong vài nến đã khai báo trước.', '“MSS được chấp nhận”', 'sau vài nến', TEAL),
            ('G3', 'Xây nhà mới bên kia', 'G2 + có HL (hoặc LH) mới VÀ một BOS đầu tiên theo chiều mới.', '“shift thật” / ATAS', 'muộn nhất', GOOD)]
    y = y0 + 6
    for k, (g, eli, d, nm, kn, c) in enumerate(rows):
        hh = 76
        yy = y + (len(rows) - 1 - k) * (hh + 8)
        indent = k * 26
        f.r(28 + indent, yy, 944 - indent, hh, fill=CARD, stroke=c, sw=1.5, rx=10)
        f.r(28 + indent, yy, 64, hh, fill=c, stroke=None, rx=10, op=0.14)
        f.t(60 + indent, yy + 45, g, 20, True, c, 'middle')
        f.t(106 + indent, yy + 26, eli, 14, True, c)
        f.p(106 + indent, yy + 47, d, 430 - indent, 11.8)
        f.t(560, yy + 28, 'Thường được gọi là', 10.5, False, SUB); f.p(560, yy + 46, nm, 200, 11.8, INK, bold=True)
        f.t(780, yy + 28, 'Biết được khi nào', 10.5, False, SUB); f.p(780, yy + 46, kn, 180, 11.8)
    f.note(28, y0 + 6 + 5 * 84 + 4, 944, 'Quy tắc vàng (RULE-MSS-012 của note 21): bậc dùng để LỌC lệnh phải là bậc ĐÃ CÓ tại thời điểm vào lệnh. Lọc bằng G3 nhưng vào lệnh lúc G1 = dùng thông tin tương lai.', BAD, None, 12.2)
    f.foot('Ghi journal theo quy ước của note 21: ví dụ “M5 MSS-I G1” hoặc “H1 MSS-P G2”. Chữ “CHoCH” chỉ dùng khi đọc tài liệu SMC (≈ G0).')
    return f.save()


# ------------------------------------------------------------------ 25 liquidity scenarios
def fig25():
    f = F(25, 'Thanh-Khoan-5-Kich-Ban', 'CHoCH và thanh khoản: năm kịch bản A–E',
          'Tím = cú quét thanh khoản (râu đi qua một đỉnh/đáy cũ rồi quay lại). Hồng = CHoCH. Không kịch bản nào là “luật”; chúng là các trường hợp phải phân biệt.', h=620)
    y0 = f.top + 4
    S = [('A. Quét → CHoCH', [(0, 70), (1, 58), (1.8, 64), (2.8, 52), (3.5, 57), (4.2, 48), (5.6, 68), (6.4, 63)], 52, 57, [(4.2, 48, 'quét', SWP, 15), (5.6, 68, 'CHoCH', CHC, -8)],
          'Thứ tự “đẹp” của ICT 2022. Quét xong, giá đảo và phá protected high.', 'thường gặp trong mô hình'),
         ('B. CHoCH không quét', [(0, 70), (1, 58), (1.8, 64), (2.8, 52), (3.5, 57), (4.2, 53.5), (5.6, 66), (6.4, 61)], 52, 57, [(4.2, 53.5, 'đáy cao hơn,\nkhông quét', SUB, 15), (5.6, 66, 'CHoCH', CHC, -8)],
          'Hợp lệ theo định nghĩa. Thiếu một bằng chứng bối cảnh — không có nghĩa là sai.', '[FRAMEWORK-DEPENDENT]'),
         ('C. Quét, không CHoCH', [(0, 70), (1, 58), (1.8, 64), (2.8, 52), (3.5, 57), (4.2, 48), (5, 55), (6.4, 42)], 52, 57, [(4.2, 48, 'quét', SWP, 15), (6.0, 42.5, 'giảm tiếp', DN, 15)],
          'Quét xong giá bật yếu, không chạm protected high, rồi giảm tiếp. Quét không tự tạo đảo chiều.', 'rất thường gặp'),
         ('D. CHoCH trước, quét sau', [(0, 70), (1, 58), (1.8, 64), (2.8, 52), (3.5, 57), (4.3, 53), (5.2, 61), (5.9, 51.5), (6.8, 66)], 52, 57, [(5.2, 61, 'CHoCH', CHC, -8), (5.9, 51.5, 'quét sau', SWP, 15)],
          'CHoCH rồi giá quay xuống quét đáy cũ, sau đó mới đi lên thật. Ai vào ngay ở CHoCH bị dừng lỗ.', 'có thể xảy ra'),
         ('E. Quét đáy nhỏ → CHoCH', [(0, 70), (1, 58), (1.8, 64), (2.8, 52), (3.5, 57), (4.1, 54), (4.6, 55.6), (5, 53.3), (6, 66), (6.6, 62)], 52, 57, [(5, 53.3, 'quét đáy nhỏ', SWP, 15), (6, 66, 'CHoCH', CHC, -8)],
          'Đáy bị quét chỉ là đáy internal. Thanh khoản mỏng hơn, ý nghĩa thấp hơn kịch bản A.', 'yếu hơn A')]
    for k, (ttl, pts, ll, ph, labs, txt, tg) in enumerate(S):
        x = 28 + k * 190; w = 180
        f.card(x, y0, w, 450, ttl, tcolor=INK, tsize=12.5)
        ch = Chart(f, x + 10, y0 + 54, w - 20, 210, 38, 74, 7.2)
        ch.level(ph, 3.5, 7, PROT, None, sw=1.2)
        ch.level(ll, 2.8, 7, SWP, None, dash='3,3', sw=1)
        zz(ch, pts, INK, 2.1); dots(ch, pts[1:], INK, 3)
        for (i, p, t_, c, dy) in labs: ch.lab(i, p, t_, dy=dy, color=c, size=10)
        f.p(x + 12, y0 + 300, txt, w - 24, 11.5)
        f.pill(x + 12, y0 + 414, tg, SUB, 9.5)
    f.foot('Cam = protected high; tím đứt = đáy cũ (sell-side liquidity). Câu hỏi trung tâm: quét có TẠO RA CHoCH không? Không — quét chỉ là một sự kiện CÓ THỂ đi trước nó.')
    return f.save()


# ------------------------------------------------------------------ 26 sweep vs choch opposite ends
def fig26():
    f = F(26, 'Sweep-va-CHoCH-O-Hai-Dau', 'Quét thanh khoản và CHoCH xảy ra ở HAI ĐẦU khác nhau của chart',
          'Người mới hay nhầm hai thứ này vì cả hai đều là “giá vượt một mức”. Nhưng chúng khác nhau ở MỨC NÀO bị vượt, VƯỢT BẰNG GÌ và Ý NGHĨA.', h=620)
    y0 = f.top + 4; H = 620 - y0 - 60
    f.card(28, y0, 560, H)
    ch, cs = bull_chart(f, 44, y0 + 26, 530, H - 46, upto=33, labels=False, fv=False)
    ch.zone(26.5, 27.5, 54.4, 57.4, SWP, op=0.14, dash=None)
    ch.zone(30.5, 31.5, 72.1, 77.3, CHC, op=0.14, dash=None)
    ch.lab(27, 54.6, 'QUÉT (sweep): râu đi dưới\nđáy cũ, thân đóng lại bên trên', dx=10, dy=18, color=SWP, anchor='start')
    ch.lab(31, 77.3, 'CHoCH: THÂN nến đóng\ntrên protected high', dx=-14, dy=-10, color=CHC, anchor='end')
    ch.lab(22, 56.2, 'đáy cũ (SSL)', dx=-10, dy=15, color=SWP, anchor='end')
    ch.lab(18, 72.3, 'protected high', dy=-8, color=PROT)
    x = 600; w = 372
    rows = [['Tiêu chí', 'Quét (sweep)', 'CHoCH'],
            ['Ở đâu?', 'Đáy cũ PHÍA DƯỚI (bullish case)', 'Đỉnh bảo vệ PHÍA TRÊN'],
            ['Bằng gì?', 'Thường là râu nến', 'Thân nến đóng cửa'],
            ['Nói về?', 'Thanh khoản: lệnh dừng lỗ có thể đã bị khớp', 'Cấu trúc: mô tả “đang giảm” hết hiệu lực'],
            ['Đi trước?', 'Thường xảy ra TRƯỚC', 'Xảy ra SAU (nếu có)'],
            ['Một nến làm cả hai?', 'Có thể (râu quét + thân đóng ngược), hiếm trên khung thực thi', 'Xem false case ở mục 19']]
    f.card(x, y0, w, H, 'So sánh nhanh')
    f.table(x + 12, y0 + 48, [92, 134, 122], rows, size=11, colors={(r, 1): SWP for r in range(1, 6)} | {(r, 2): CHC for r in range(1, 6)})
    f.foot('Quét ở bên dưới là [OBSERVABLE]. “Stop của người bán bị kích hoạt” là [INTERPRETATION]. Quét làm CHoCH đáng tin hơn là [HYPOTHESIS] — BACKTEST REQUIRED.')
    return f.save()


ALL = [fig14, fig15, fig16, fig17, fig18, fig19, fig20, fig21, fig22, fig23, fig24, fig25, fig26]
if __name__ == '__main__':
    sel = sys.argv[1:]
    for fn in ALL:
        if not sel or fn.__name__[3:] in sel:
            print(fn())
