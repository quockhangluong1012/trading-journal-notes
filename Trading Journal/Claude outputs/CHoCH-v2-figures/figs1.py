# -*- coding: utf-8 -*-
from chdraw import *
import sys

SAND, SEA, SEAL = '#F6E7C8', '#93C5FD', '#DBEAFE'


def polyfill(f, pts, fill, op=1.0):
    f.o.append('<polygon points="%s" fill="%s" fill-opacity="%s"/>' % (' '.join('%.1f,%.1f' % q for q in pts), fill, op))


# ------------------------------------------------------------------ 01 ELI5 staircase
def fig01():
    f = F(1, 'ELI5-Nam-Leo-Cau-Thang', 'CHoCH cho bé 5 tuổi: bạn Nam leo cầu thang kiểu “tiến ba, lùi một”',
          'Nam leo lên ba bậc rồi lùi một bậc để nghỉ, cứ thế mãi. Hãy để ý cái bậc Nam dùng để lấy đà cho lần leo gần nhất (màu cam).',
          h=600, tag='ELI5')
    paths = [[0, 3, 2, 5, 4, 7], [0, 3, 2, 5, 3], [0, 3, 2, 5, 1], [0, 3, 2, 5, 1]]
    caps = [('Leo đều: thói quen rất rõ', 'Mỗi lần lùi, Nam vẫn đứng cao hơn chỗ nghỉ lần trước. Mỗi lần leo, Nam lên cao hơn lần trước. Đó là “tính cách” leo lên.'),
            ('Lùi hơi nhiều — vẫn chưa đổi', 'Lần này Nam lùi 2 bậc. Hơi lạ, nhưng Nam vẫn đứng TRÊN bậc lấy đà. Thói quen cũ vẫn chưa bị phá.'),
            ('Lùi xuống DƯỚI bậc lấy đà', 'Nam đi xuống thấp hơn cả cái bậc đã giúp Nam leo lần trước. Cả lần leo đó coi như bị xoá. Thói quen “tiến ba lùi một” vừa bị phá.'),
            ('Rồi sao nữa? Chưa ai biết', 'Nam có thể leo tiếp, đứng nghỉ lâu, hoặc đi xuống luôn. Phá thói quen là một LỜI CẢNH BÁO, chưa phải câu trả lời.')]
    for k in range(4):
        x = 28 + k * 239; w = 227; y = f.top + 4
        f.card(x, y, w, 452, caps[k][0], num=k + 1, tcolor=CHC if k == 2 else INK)
        x0 = x + 18; sw_, rise = 24, 25; ybot = y + 342
        pts = [(x0, ybot)]
        for s_ in range(8):
            pts += [(x0 + s_ * sw_, ybot - (s_ + 1) * rise), (x0 + (s_ + 1) * sw_, ybot - (s_ + 1) * rise)]
        f.poly(pts, '#9CA3AF', 2.4)
        # launch step
        f.ln(x0 + 2 * sw_, ybot - 3 * rise, x0 + 3 * sw_, ybot - 3 * rise, PROT, 5)
        f.ln(x0 + 2 * sw_ - 4, ybot - 3 * rise, x + w - 12, ybot - 3 * rise, PROT, 1.2, '4,3')
        f.t(x + w - 14, ybot - 3 * rise + 15, 'bậc lấy đà', 10.5, True, PROT, 'end')
        P = lambda s_: (x0 + s_ * sw_ + sw_ / 2, ybot - (s_ + 1) * rise - 3)
        ph = paths[k]
        f.poly([P(s_) for s_ in ph], CHC if k >= 2 else INK, 1.8, '5,4')
        for j, s_ in enumerate(ph[:-1]):
            f.circ(*P(s_), 3.2, SUB)
        last = P(ph[-1])
        f.person(last[0], last[1] + 2, CHC if k >= 2 else INK, 0.95, 'up' if k == 0 else 'down')
        if k == 0:
            f.t(P(5)[0] - 2, P(5)[1] - 40, 'cao nhất', 10, True, BOSC, 'middle')
            f.t(P(4)[0] + 2, P(4)[1] + 18, 'chỗ nghỉ', 10, True, DISP, 'middle')
        if k == 2:
            f.t(last[0] + 12, last[1] + 16, 'thấp hơn bậc lấy đà!', 10, True, CHC)
        if k == 3:
            cx, cy = last
            f.curve(cx + 6, cy - 16, cx + 40, cy - 70, cx + 96, cy - 110, UP, 1.8, '5,4'); f.t(cx + 98, cy - 112, 'leo tiếp?', 10, True, UP, 'end')
            f.arrow(cx + 10, cy - 8, cx + 84, cy - 10, STR, 1.8, '5,4'); f.t(cx + 92, cy - 22, 'đứng nghỉ?', 10, True, STR, 'end')
            f.curve(cx + 6, cy + 4, cx + 30, cy + 26, cx + 70, cy + 40, DN, 1.8, '5,4'); f.t(cx + 74, cy + 56, 'đi xuống?', 10, True, DN, 'end')
        f.p(x + 14, ybot + 30, caps[k][1], w - 28, 12)
    f.foot('Giới hạn của ví dụ: Nam tự quyết định bước chân của mình. Giá thì không có “một người” quyết định — nó là kết quả của rất nhiều lệnh mua bán gặp nhau.')
    return f.save()


# ------------------------------------------------------------------ 02 ELI5 tide
def fig02():
    f = F(2, 'ELI5-Thuy-Trieu', 'Một ví dụ khác cho bé: “tính cách” của sóng biển khi thủy triều lên và đổi chiều',
          'Đứng trên bãi cát, mỗi con sóng vào rồi rút. Ta đánh dấu chỗ xa nhất nước tràn tới và chỗ nước rút về. Trục dọc: càng cao = nước càng lên sâu vào bãi cát.',
          h=560, tag='ELI5')
    y0 = f.top + 4
    panels = [('Triều đang lên', [(0, 30), (1.4, 46), (2.4, 38), (3.8, 55), (4.8, 47), (6.2, 64), (7.2, 56), (8.6, 72)], None),
              ('Triều bắt đầu đổi', [(0, 30), (1.4, 46), (2.4, 38), (3.8, 58), (4.8, 50), (6.2, 56), (7.4, 41), (8.6, 48)], 1)]
    for k, (ttl, pts, chg) in enumerate(panels):
        x = 28 + k * 478; w = 466
        f.card(x, y0, w, 380, ttl, num=k + 1, tcolor=CHC if k else INK)
        ch = Chart(f, x + 16, y0 + 50, w - 32, 250, 20, 82, 9.5)
        top = ch.Y(82); bot = ch.Y(20)
        f.r(ch.x, top, ch.w, bot - top, fill=SAND, stroke=None, rx=4)
        poly = [(ch.X(i), ch.Y(p)) for i, p in pts]
        polyfill(f, [(ch.x, bot)] + [(ch.x, poly[0][1])] + poly + [(ch.x + ch.w, poly[-1][1]), (ch.x + ch.w, bot)], SEA, 0.55)
        zz(ch, pts, '#1D4ED8', 2.4)
        f.t(ch.x + 8, top + 16, 'bãi cát (khô)', 10.5, True, '#92400E')
        f.t(ch.x + 8, bot - 8, 'biển', 10.5, True, '#1E3A8A')
        for j, (i, p) in enumerate(pts[1:], 1):
            hi = (j % 2 == 1)
            ch.dot(i, p, '#1D4ED8', 3.6)
        if k == 0:
            for (i, p) in pts[1::2]: ch.lab(i, p, 'vào xa hơn', dy=-9, color=BOSC, size=10)
            for (i, p) in pts[2::2]: ch.lab(i, p, 'rút ít hơn', dy=15, color=DISP, size=10)
        else:
            ch.lab(1.4, 46, 'vào xa hơn', dy=-9, color=BOSC, size=10)
            ch.lab(3.8, 58, 'vào xa nhất', dy=-9, color=BOSC, size=10)
            ch.lab(4.8, 50, 'vạch rút cuối', dy=15, color=PROT, size=10)
            ch.level(50, 4.3, 9.0, PROT, None, dash='5,4', sw=1.3)
            ch.lab(6.2, 56, 'không vào tới\nvạch cũ', dy=-9, color=WARN, size=10)
            ch.lab(7.4, 41, 'rút SÂU HƠN vạch rút cũ\n= tính cách đổi', dy=15, color=CHC, size=10.5)
        f.p(x + 16, y0 + 330, ['Mỗi con sóng vào xa hơn con trước, mỗi lần rút cũng không rút về sâu bằng lần trước. Nhìn là biết triều đang lên.',
                               'Một con sóng không vào tới vạch cũ (dấu hiệu sớm). Rồi lần rút về sâu hơn vạch rút cuối cùng — “tính cách” của sóng đã khác.'][k], w - 32, 12.2)
    f.foot('Giới hạn: thủy triều đổi theo mặt trăng, đoán trước được bằng lịch. Giá thì không có “mặt trăng” — không có lịch nào nói trước khi nào xu hướng đổi.')
    return f.save()


# ------------------------------------------------------------------ 03 story on chart
def fig03():
    f = F(3, 'Tu-Cau-Chuyen-Len-Chart', 'Câu chuyện cầu thang, vẽ lại bằng nến (bearish CHoCH)',
          'Cùng một chuỗi sự kiện, đánh số theo thứ tự thời gian. Đường cam = “bậc lấy đà” = protected low. Đây là sơ đồ dựng, không phải dữ liệu thị trường.', h=620)
    y0 = f.top + 4; H = 620 - y0 - 44
    f.card(28, y0, 610, H)
    cs, tn = bear_seq()
    ch = Chart(f, 46, y0 + 30, 574, H - 54, 50, 90, len(cs) + 1)
    ch.level(67.7, 18, 33, PROT, 'protected low (HL2)', pos='l', dy=17, sw=1.5)
    ch.level(78.2, 25, 29, MUTE, None, dash='3,3', sw=1)
    ch.candles(cs)
    ch.lab(10, 60.7, 'HL1', dy=15, color=DISP); ch.badge(10, 60.7, 1, DISP, dy=38)
    ch.lab(14, 77.3, 'HH1', dy=-8, color=BOSC); ch.badge(14, 77.3, 2, BOSC, dy=-30)
    ch.badge(18, 67.7, 3, PROT, dy=40)
    ch.lab(22, 83.8, 'HH2', dy=-8, color=BOSC)
    ch.badge(25, 78.2, 4, STR, dy=22)
    ch.lab(27, 85.4, 'vượt đỉnh một chút', dx=12, dy=-8, color=SWP, anchor='start'); ch.badge(27, 85.4, 5, SWP, dy=-30)
    ch.badge(31, 62.7, 6, CHC, dy=18, dx=-14)
    ch.lab(33, 62, 'ĐÓNG NẾN dưới protected\nlow = CHoCH ↓', dx=14, dy=34, color=CHC, anchor='end')
    x = 652
    f.card(x, y0, 320, H, 'Ghép truyện với chart')
    rows = [(1, DISP, 'Chỗ nghỉ', 'Một đáy cao hơn đáy trước: Higher Low (HL).'),
            (2, BOSC, 'Chỗ cao nhất', 'Đỉnh cao hơn đỉnh trước: Higher High (HH). Mỗi lần vượt đỉnh cũ gọi là BOS.'),
            (3, PROT, 'Bậc lấy đà', 'Đáy đã phóng ra cú tăng vượt đỉnh gần nhất. Tên kỹ thuật: protected low.'),
            (4, STR, 'Lùi hơi sâu', 'Một đáy nhỏ bên trong bị phá — nhưng vẫn trên bậc lấy đà. Chỉ là chuyện nội bộ (internal).'),
            (5, SWP, 'Chạm cao hơn một chút', 'Giá nhô qua đỉnh cũ rồi rút về (cú quét thanh khoản — học ở mục 15).'),
            (6, CHC, 'Lùi dưới bậc lấy đà', 'Thân nến đóng dưới protected low. Thói quen “đáy sau cao hơn đáy trước” bị phá: Change of Character.')]
    yy = y0 + 50
    for n, c, a, b in rows:
        f.badge(x + 24, yy - 4, n, c)
        f.t(x + 42, yy, a, 12.5, True, c)
        yy = f.p(x + 42, yy + 17, b, 264, 11.8) + 8
    f.foot('Trục dọc là giá (lên = đắt hơn), trục ngang là thời gian (trái → phải). Nến xanh: đóng cao hơn mở. Nến đỏ: đóng thấp hơn mở.')
    return f.save()


# ------------------------------------------------------------------ 04 labels
def fig04():
    f = F(4, 'Tam-Loai-Cau-Noi', 'Cùng MỘT cây nến CHoCH, tám loại câu nói khác nhau',
          'Lỗi lớn nhất khi học CHoCH: nói một câu DIỄN GIẢI bằng giọng chắc chắn của câu QUAN SÁT. Mỗi câu trong note mang một nhãn.', h=640, tag='CÁCH ĐỌC NOTE')
    rows = [('[OBSERVABLE]', GOOD, 'Ai nhìn chart cũng thấy giống nhau', '“Thân nến H1 đóng cửa thấp hơn đáy 1.0850 — đáy đã phóng ra cú tăng gần nhất.”'),
            ('[MARKET MECHANICS]', FVGC, 'Giải thích bằng cách lệnh được khớp', '“Giá đi xuống khi lệnh bán chủ động ăn hết lệnh chờ mua ở các mức giá bên dưới.”'),
            ('[ICT FRAMEWORK]', BOSC, 'Cách ICT / SMC đặt tên và dùng', '“Phá ngược trạng thái lần đầu = CHoCH; có displacement thì nhiều người gọi là MSS.”'),
            ('[INTERPRETATION]', WARN, 'Hợp lý, nhưng OHLC không chứng minh được', '“Phe mua đã không bảo vệ mức này; có thể stop của người mua bên dưới đã bị kích hoạt.”'),
            ('[HYPOTHESIS]', SWP, 'Có thể kiểm chứng, chưa kiểm chứng', '“CHoCH xảy ra sau một cú quét thanh khoản sẽ ít thất bại hơn CHoCH không có quét.”'),
            ('[FRAMEWORK-DEPENDENT]', TEAL, 'Đúng hay sai tùy định nghĩa của từng trường phái', '“Râu nến vượt đáy là đủ để gọi CHoCH.” (có nguồn chấp nhận, có nguồn không)'),
            ('[NOT ESTABLISHED]', GRAY, 'Chưa có bằng chứng đủ để khẳng định', '“Smart Money đã quyết định đảo chiều ở đây.”'),
            ('[BACKTEST REQUIRED]', BAD, 'Không được coi là lợi thế khi chưa đo', '“Vào lệnh theo CHoCH tại POI cho kết quả tốt hơn vào lệnh ngẫu nhiên.”')]
    y = f.top + 6
    for lab, c, what, ex in rows:
        f.r(28, y, 944, 56, fill=CARD, stroke=BORDER, rx=10)
        f.r(28, y, 6, 56, fill=c, stroke=None, rx=3)
        f.pill(46, y + 9, lab, c, 10.5)
        f.t(46, y + 46, what, 11, False, SUB)
        f.p(350, y + 25, ex, 606, 12.5, INK, italic=True)
        y += 62
    f.foot('Chỉ nhãn đầu tiên là chắc chắn. Càng xuống dưới, câu nói càng là thứ ta NGHĨ hoặc HY VỌNG, và càng cần bằng chứng. Mức giá 1.0850 là số minh họa.')
    return f.save()


# ------------------------------------------------------------------ 05 swing formation
def fig05():
    f = F(5, 'Swing-Sinh-Ra-Nhu-The-Nao', 'Swing high được sinh ra như thế nào — và vì sao ta chỉ biết nó MUỘN',
          'Trái: ví dụ cho bé. Phải: cùng ý tưởng trên nến. Một đỉnh chỉ trở thành “swing high” khi giá đã đi xuống khỏi nó một đoạn.', h=600)
    y0 = f.top + 4; H = 600 - y0 - 46
    f.card(28, y0, 400, H, 'Ném quả bóng lên trời', num=1)
    cx, base = 228, y0 + 360
    for j, t in enumerate([0, 1, 2, 3, 4, 5, 6]):
        xx = 70 + j * 52; yy = base - (240 - 20 * (t - 3) ** 2)
        f.circ(xx, yy, 9, '#F59E0B' if j != 3 else BOSC, stroke='#FFFFFF')
        f.t(xx, yy + 25, 't%d' % (j + 1), 10, True, SUB, 'middle')
    f.ln(50, base + 8, 410, base + 8, '#9CA3AF', 2)
    f.t(226, base - 268, 'cao nhất ở t4', 11, True, BOSC, 'middle')
    f.p(44, base + 34, 'Ở đúng lúc t4, bạn KHÔNG biết đó là điểm cao nhất — có thể bóng còn bay tiếp. Chỉ khi thấy bóng rơi xuống ở t5, t6, bạn mới nói: “À, đỉnh là t4”.', 370, 12.2)
    x = 442; w = 530
    f.card(x, y0, w, H, 'Trên chart: đỉnh fractal 5 nến', num=2)
    cs = [(60, 64, 59, 63), (63, 67, 62, 66), (66, 71.5, 65, 70), (70, 73, 66.5, 67), (67, 69, 63.5, 64), (64, 66, 61, 62), (62, 64.5, 58.5, 59)]
    ch = Chart(f, x + 20, y0 + 56, 300, 280, 55, 76, 8)
    ch.candles(cs)
    for i in range(7):
        ch.f.t(ch.X(i), ch.Y(55) + 16, str(i + 1), 10.5, True, SUB, 'middle')
    ch.level(73, 1, 6, BOSC, 'đỉnh = nến 4', pos='l', dy=-6)
    ch.f.r(ch.X(5) - 12, ch.y - 4, 26, ch.h + 8, fill=CHC, stroke=CHC, sw=1, rx=4, op=0.08, dash='4,3')
    ch.lab(5, 66, 'xác nhận\ntại đây', dy=-18, color=CHC, size=10)
    yy = y0 + 74
    for t_, c_ in [('Nến 1–3: giá đi lên, mỗi nến cao hơn nến trước.', INK), ('Nến 4: cao nhất. Lúc nến 4 đóng cửa, ta CHƯA biết nó là đỉnh.', BOSC),
                   ('Nến 5: thấp hơn nến 4. Vẫn chưa chắc.', INK), ('Nến 6 đóng cửa: đã có 2 nến thấp hơn ở bên phải → nến 4 được XÁC NHẬN là swing high.', CHC),
                   ('Bài học: swing luôn đến trễ. Một cú “phá swing” chỉ có nghĩa nếu swing đó đã được xác nhận TRƯỚC cú phá.', PROT)]:
        yy = f.p(x + 336, yy, t_, 180, 11.6, c_) + 8
    f.foot('Quy tắc “2 nến mỗi bên” là một quy ước (fractal), không phải luật. Có nhiều cách định nghĩa swing; mỗi cách cho độ trễ khác nhau — xem note 54.')
    return f.save()


# ------------------------------------------------------------------ 06 visible / significant / protected
def fig06():
    f = F(6, 'Visible-Significant-Protected', 'Ba thứ khác nhau: swing NHÌN THẤY ≠ swing CÓ Ý NGHĨA ≠ swing ĐƯỢC BẢO VỆ',
          'Cùng một đoạn xu hướng tăng. Rất nhiều đáy nhìn thấy được, chỉ vài đáy có ý nghĩa cấu trúc, và chỉ MỘT đáy là protected low tại thời điểm cuối chart.', h=620)
    y0 = f.top + 4; H = 620 - y0 - 46
    f.card(28, y0, 590, H)
    pts = [(0, 40), (1, 46), (1.6, 44), (2.4, 50), (3, 47), (4, 56), (4.8, 51), (5.4, 53), (6.2, 49), (7.4, 62), (8, 59), (8.6, 61), (9.4, 57),
           (10.6, 70), (11.2, 66), (11.8, 68), (12.6, 63.5), (13.4, 66), (14, 64.5), (15.4, 76)]
    ch = Chart(f, 46, y0 + 24, 556, H - 50, 36, 80, 16.4)
    ch.level(63.5, 12.6, 15.9, PROT, 'protected low', pos='r', dy=17, sw=1.5)
    zz(ch, pts, INK, 2.2)
    lows = [p for p in pts[1:] if p[0] in (1.6, 3, 4.8, 6.2, 8, 9.4, 11.2, 12.6, 14)]
    for i, p in lows: ch.dot(i, p, MUTE, 3.4)
    for i, p in [(3, 47), (6.2, 49), (9.4, 57)]:
        f.circ(ch.X(i), ch.Y(p), 8, '#FFFFFF', stroke=BOSC, sw=2, op=0)
    f.circ(ch.X(12.6), ch.Y(63.5), 11, '#FFFFFF', stroke=PROT, sw=3, op=0)
    for i, p in [(4, 56), (7.4, 62), (10.6, 70), (15.4, 76)]:
        ch.lab(i, p, 'BOS', dy=-8, color=BOSC, size=9.5)
    ch.lab(9.4, 57, 'có ý nghĩa', dy=26, color=BOSC, size=10)
    ch.lab(6.2, 49, 'có ý nghĩa', dy=26, color=BOSC, size=10)
    ch.lab(4.8, 51, 'chỉ nhìn thấy', dx=-4, dy=-10, color=SUB, size=10)
    ch.lab(11.2, 66, 'chỉ nhìn thấy', dx=-6, dy=-14, color=SUB, size=10, anchor='end')
    x = 632; w = 340
    f.card(x, y0, w, H, 'Ba vòng tròn lồng nhau')
    cx, cy = x + w / 2, y0 + 150
    f.circ(cx, cy, 104, '#F3F4F6', stroke=MUTE, sw=1.5)
    f.circ(cx, cy + 26, 70, '#EFF6FF', stroke=BOSC, sw=1.5)
    f.circ(cx, cy + 52, 36, '#FEF3C7', stroke=PROT, sw=2)
    f.t(cx, cy - 80, 'VISIBLE', 11.5, True, SUB, 'middle'); f.t(cx, cy - 66, 'mọi đáy/đỉnh nhìn thấy', 10, False, SUB, 'middle')
    f.t(cx, cy - 18, 'SIGNIFICANT', 11.5, True, BOSC, 'middle'); f.t(cx, cy - 4, 'gánh một việc cấu trúc', 10, False, BOSC, 'middle')
    f.t(cx, cy + 51, 'PROTECTED', 11, True, PROT, 'middle'); f.t(cx, cy + 65, 'chỉ 1 mỗi lớp', 9.5, False, PROT, 'middle')
    yy = y0 + 286
    for t_, c_ in [('Visible: bất kỳ chỗ giá quay đầu. Rất nhiều, phần lớn là nhiễu.', SUB),
                   ('Significant: đã xác nhận, và đã làm một việc cấu trúc (ví dụ phóng ra một BOS, hoặc là ranh của dealing range).', BOSC),
                   ('Protected: đáy (đỉnh) mà NẾU bị phá thì câu “đang tăng (giảm)” ở lớp này không còn đúng. Tại một thời điểm, mỗi lớp chỉ có MỘT.', PROT)]:
        yy = f.p(x + 16, yy, t_, w - 32, 11.8, c_) + 7
    f.foot('Định nghĩa vận hành của vault (kế thừa note 21 và 57): protected low = đáy thấp nhất của chân sóng đã tạo ra BOS tăng gần nhất.')
    return f.save()


# ------------------------------------------------------------------ 07 bullish & bearish structure
def fig07():
    f = F(7, 'Cau-Truc-Tang-va-Giam', 'Cấu trúc tăng (HH–HL) và cấu trúc giảm (LH–LL): mỗi nhãn đang nói điều gì?',
          'Số trên chart là giá minh họa. Đừng học thuộc nhãn — hãy đọc câu tiếng Việt bên dưới mỗi nhãn: đó mới là ý nghĩa.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 46
    sets = [('Cấu trúc TĂNG', UP, [(0, 100), (1, 110), (2, 105), (3, 118), (4, 111), (5, 125)], False,
             [('HH', 'đẩy được lên chỗ mới'), ('HL', 'lùi, nhưng có người mua sớm hơn')],
             'HL quan trọng vì nó cho thấy người mua chấp nhận trả giá CAO HƠN lần trước. Đáy nào phóng ra cú vượt đỉnh gần nhất (ở đây: 111) là protected low. Mất nó = câu “đang tăng” sai.'),
            ('Cấu trúc GIẢM', DN, [(0, 125), (1, 112), (2, 119), (3, 104), (4, 112), (5, 96)], True,
             [('LL', 'đẩy được xuống chỗ mới'), ('LH', 'hồi, nhưng có người bán sớm hơn')],
             'LH quan trọng vì nó cho thấy người bán chấp nhận bán ở giá THẤP HƠN lần trước. Đỉnh phóng ra cú thủng đáy gần nhất (ở đây: 112) là protected high. Mất nó = câu “đang giảm” sai.')]
    for k, (ttl, col, pts, bear, labs, txt) in enumerate(sets):
        x = 28 + k * 478; w = 466
        f.card(x, y0, w, H, ttl, tcolor=col)
        ch = Chart(f, x + 40, y0 + 58, w - 80, 290, 92, 130, 6)
        zz(ch, pts, col, 2.6)
        for j, (i, p) in enumerate(pts):
            ch.dot(i, p, INK, 3.6)
            up = (j % 2 == 1) != bear
            ch.lab(i, p, str(p), dy=-9 if up else 16, color=INK, size=10.5)
        if not bear:
            for i, p, l in [(1, 110, 'HH'), (3, 118, 'HH'), (5, 125, 'HH')]: ch.lab(i, p, l, dy=-24, color=BOSC, size=11)
            for i, p, l in [(2, 105, 'HL'), (4, 111, 'HL')]: ch.lab(i, p, l, dy=32, color=DISP, size=11)
            ch.level(111, 4, 5, PROT, 'protected low', pos='r', dy=16)
            ch.level(110, 1, 3.2, BOSC, None, dash='3,3', sw=1); ch.level(118, 3, 5.2, BOSC, None, dash='3,3', sw=1)
        else:
            for i, p, l in [(1, 112, 'LL'), (3, 104, 'LL'), (5, 96, 'LL')]: ch.lab(i, p, l, dy=32, color=BOSC, size=11)
            for i, p, l in [(2, 119, 'LH'), (4, 112, 'LH')]: ch.lab(i, p, l, dy=-24, color=DN, size=11)
            ch.level(112, 4, 5, PROT, 'protected high', pos='r', dy=-6)
        yy = y0 + 380
        for a, b in labs:
            f.t(x + 18, yy, a, 12.5, True, BOSC if a in ('HH', 'LL') else (DISP if a == 'HL' else DN))
            f.t(x + 54, yy, '= ' + b, 12.2, False, INK); yy += 21
        f.p(x + 18, yy + 6, txt, w - 36, 12, INK)
    f.foot('Đây là định nghĩa kiểu Dow Theory (cuối thế kỷ 19), không phải phát minh của ICT. ICT/SMC thêm tên gọi cho các cú phá: BOS, CHoCH, MSS.')
    return f.save()


# ------------------------------------------------------------------ 08 three states
def fig08():
    f = F(8, 'Ba-Trang-Thai-CHoCH-Can-Co-Trang-Thai', 'Không có “tính cách” thì không có “thay đổi tính cách”',
          'CHoCH chỉ có nghĩa khi TRƯỚC ĐÓ đã có một trạng thái rõ ràng để bị phá. Trong vùng đi ngang, mọi cú phá đều “ngược chiều” với một cái gì đó — nên chẳng nói lên gì.', h=590)
    y0 = f.top + 4
    sets = [('Đang TĂNG', UP, [(0, 40), (1, 52), (2, 46), (3, 60), (4, 53), (5, 68), (6, 61)], 'Có thói quen rõ: đáy sau cao hơn đáy trước. Phá protected low = CHoCH có nghĩa.', GOOD, 'CHoCH có nghĩa'),
            ('Đang GIẢM', DN, [(0, 68), (1, 56), (2, 62), (3, 48), (4, 55), (5, 41), (6, 47)], 'Có thói quen rõ: đỉnh sau thấp hơn đỉnh trước. Phá protected high = CHoCH có nghĩa.', GOOD, 'CHoCH có nghĩa'),
            ('ĐI NGANG', STR, [(0, 50), (1, 60), (2, 47), (3, 61), (4, 46), (5, 59.5), (6, 48)], 'Đỉnh, đáy chồng lên nhau, không có thói quen. Phá đỉnh nhỏ hay đáy nhỏ đều không đổi “tính cách” nào cả.', BAD, 'CHoCH vô nghĩa')]
    for k, (ttl, col, pts, txt, vc, vt) in enumerate(sets):
        x = 28 + k * 318; w = 306
        f.card(x, y0, w, 410, ttl, tcolor=col)
        ch = Chart(f, x + 22, y0 + 52, w - 44, 220, 36, 72, 7)
        if k == 2:
            ch.zone(0, 6, 46, 61, STR, op=0.07, dash='4,3')
        zz(ch, pts, col, 2.4)
        dots(ch, pts[1:])
        f.p(x + 16, y0 + 304, txt, w - 32, 12)
        f.pill(x + 16, y0 + 372, vt, vc, 11)
    f.foot('Hệ quả thực hành: bước đầu tiên của mọi nhận diện CHoCH là KHAI BÁO trạng thái hiện tại (trên khung nào, ở lớp nào). Không khai báo được → không gọi CHoCH.')
    return f.save()


# ------------------------------------------------------------------ 09 boat ELI5
def fig09():
    f = F(9, 'ELI5-Con-Tau-Hanh-Khach-Con-Kien', 'Internal vs External cho bé: con tàu, hành khách và con kiến',
          'Ba chuyển động lồng vào nhau. Cái nhỏ đi ngược cái lớn không có nghĩa cái lớn đã đổi hướng.', h=570, tag='ELI5')
    y0 = f.top + 10
    f.r(28, y0, 944, 300, fill='#EFF6FF', stroke=BORDER, rx=12)
    wy = y0 + 230
    f.o.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="#475569"/>' % (190, wy - 70, 810, wy - 70, 760, wy - 10, 240, wy - 10))
    f.r(300, wy - 128, 380, 58, fill='#CBD5E1', stroke='#475569', sw=1.5, rx=6)
    for j in range(5): f.r(318 + j * 72, wy - 116, 42, 24, fill='#E0F2FE', stroke='#475569', sw=1, rx=3)
    f.o.append('<path d="M40 %.1f Q120 %.1f 200 %.1f T360 %.1f T520 %.1f T680 %.1f T840 %.1f T960 %.1f" fill="none" stroke="#3B82F6" stroke-width="3"/>' % (wy, wy - 12, wy, wy, wy, wy, wy, wy))
    f.arrow(560, y0 + 40, 860, y0 + 40, BOSC, 4, size=13); f.t(710, y0 + 30, 'CON TÀU đi sang phải (D1)', 13, True, BOSC, 'middle')
    f.person(540, wy - 70, CHC, 1.15)
    f.arrow(520, wy - 108, 410, wy - 108, CHC, 3, size=11); f.t(470, wy - 140, 'HÀNH KHÁCH đi sang trái (H1)', 12, True, CHC, 'middle')
    f.circ(552, wy - 74, 3, '#111827'); f.arrow(556, wy - 84, 600, wy - 84, DISP, 2, size=7)
    f.t(605, wy - 79, 'con kiến trên giày bò sang phải (M5)', 11, True, DISP)
    cols = [('Con tàu (D1)', BOSC, 'Đi sang phải suốt. Đây là cấu trúc EXTERNAL lớn nhất.'),
            ('Hành khách (H1)', CHC, 'Đi ngược về bên trái — một pullback. Đổi hướng của hành khách KHÔNG làm con tàu quay đầu.'),
            ('Con kiến (M5)', DISP, 'Bò sang phải trên giày người đang đi trái. Một M5 CHoCH tăng trong H1 đang giảm có thể chỉ là “kiến đổi hướng”.')]
    for k, (a, c, b) in enumerate(cols):
        x = 28 + k * 318
        f.card(x, y0 + 312, 306, 150, a, tcolor=c)
        f.p(x + 14, y0 + 366, b, 278, 12)
    f.foot('Muốn biết con tàu có quay đầu không, phải nhìn con tàu (khung lớn, lớp external). Nhìn con kiến thì chỉ biết con kiến.')
    return f.save()


# ------------------------------------------------------------------ 10 internal vs external on chart
def fig10():
    f = F(10, 'Internal-vs-External-Tren-Chart', 'Một chân tăng external chứa cả một cấu trúc giảm internal',
          'Trong đợt hồi (pullback) của xu hướng tăng lớn, giá tạo LH–LL nhỏ và hai lần CHoCH internal. Protected low external chưa hề bị chạm.', h=600)
    y0 = f.top + 4; H = 600 - y0 - 46
    f.card(28, y0, 944, H)
    pts = [(0, 40), (2.2, 71), (2.5, 68), (3, 78), (3.8, 72), (4.4, 75), (5.2, 66), (5.8, 70), (6.6, 63.5), (7.3, 67.5), (8.2, 61.5), (9.2, 69.5), (9.7, 66.5), (11, 84), (12.4, 92)]
    ch = Chart(f, 50, y0 + 34, 600, H - 60, 34, 96, 13.5)
    ch.level(40, 0, 12.4, PROT, 'protected low EXTERNAL — chưa bị chạm', pos='r', dy=-6, sw=1.6)
    ch.level(78, 3, 12, BOSC, None, dash='5,4')
    ch.level(68, 2.5, 5.4, CHC, None, dash='3,3', sw=1.2)
    ch.level(67.5, 7.3, 9.4, CHC, None, dash='3,3', sw=1.2)
    ch.zone(3, 10, 60, 80, CHC, op=0.04, dash='4,3')
    zz(ch, pts, INK, 2.4)
    for i, p in pts[1:]: ch.dot(i, p, INK, 3)
    ch.lab(3, 78, 'đỉnh external', dy=-9, color=BOSC, size=10)
    ch.lab(2.5, 68, 'HL nhỏ', dx=-8, dy=6, color=DISP, size=10, anchor='end')
    for i, p in [(4.4, 75), (5.8, 70), (7.3, 67.5)]: ch.lab(i, p, 'LH', dy=-8, color=DN, size=10)
    for i, p in [(5.2, 66), (6.6, 63.5), (8.2, 61.5)]: ch.lab(i, p, 'LL', dy=15, color=DN, size=10)
    ch.lab(4.95, 67, 'CHoCH ↓\ninternal', dx=-10, dy=30, color=CHC, size=10, anchor='end')
    ch.lab(9.2, 69.5, 'CHoCH ↑\ninternal', dx=8, dy=-12, color=CHC, size=10, anchor='start')
    ch.lab(11, 84, 'BOS ↑ external', dx=-8, dy=-8, color=BOSC, size=10.5, anchor='end')
    x = 664; yy = y0 + 30
    f.t(x, yy, 'Đọc từng lớp', 14, True)
    for t_, c_ in [('External (lớp lớn): 40 → 78 → (hồi) → 92. Trạng thái TĂNG chưa bao giờ đổi, vì protected low 40 còn nguyên.', BOSC),
                   ('Internal (lớp nhỏ, bên trong đợt hồi): đỉnh thấp dần, đáy thấp dần → trạng thái GIẢM nội bộ.', DN),
                   ('CHoCH ↓ internal: đầu đợt hồi, giá phá cái HL nhỏ 68 trong chân tăng. Chỉ lớp nhỏ đổi chiều.', CHC),
                   ('CHoCH ↑ internal: cuối đợt hồi, giá vượt LH nhỏ gần nhất 67.5. Đây là loại CHoCH mà mô hình ICT 2022 dùng để vào lệnh THUẬN chiều lớn.', CHC),
                   ('Cùng một chart: lớp nhỏ đổi chiều hai lần, lớp lớn không đổi lần nào.', PROT)]:
        yy = f.p(x, yy + 22, t_, 296, 12, c_) - 8
    f.foot('“Internal” và “external” là quan hệ tương đối với một chân sóng/range đã chọn, không gắn cứng với khung thời gian (LuxAlgo cũng định nghĩa như vậy).')
    return f.save()


# ------------------------------------------------------------------ 11 protected low = launch pad
def fig11():
    f = F(11, 'Protected-Low-La-Cho-Lay-Da', 'Vì sao phá protected low lại quan trọng: nó XOÁ cả cú tăng gần nhất',
          'Protected low là cái đáy đã “phóng” ra cú tăng vượt đỉnh gần nhất. Giá quay về dưới nó = toàn bộ thành quả của cú tăng đó bị lấy lại.', h=600)
    y0 = f.top + 4; H = 580 - y0 - 46
    f.card(28, y0, 370, H, 'Cho bé: nhảy xa', num=1)
    gy = y0 + 250
    f.ln(50, gy, 380, gy, '#9CA3AF', 2.5)
    f.r(120, gy - 3, 8, 6, fill=PROT, stroke=None, rx=1); f.t(124, gy + 22, 'vạch giậm nhảy', 10.5, True, PROT, 'middle')
    f.person(110, gy, INK, 0.9)
    f.curve(124, gy - 30, 200, gy - 120, 290, gy - 4, BOSC, 2, '5,4')
    f.person(300, gy, BOSC, 0.9); f.t(300, gy + 22, 'tiếp đất xa', 10.5, True, BOSC, 'middle')
    f.arrow(296, gy - 50, 100, gy - 50, CHC, 2.2, '6,4'); f.t(200, gy - 58, 'bị kéo lùi qua vạch giậm', 10.5, True, CHC, 'middle')
    f.p(46, gy + 50, 'Bé giậm ở vạch cam và nhảy rất xa. Nếu sau đó bé bị kéo lùi về SAU vạch giậm, cú nhảy coi như chưa từng có. Bé đang đứng ở chỗ còn tệ hơn trước khi nhảy.', 336, 12.2)
    x = 412; w = 560
    f.card(x, y0, w, H, 'Trên chart', num=2)
    pts = [(0, 52), (1, 64), (2, 57), (3.4, 76), (4.4, 66), (5.4, 70), (6.6, 54)]
    ch = Chart(f, x + 24, y0 + 54, 330, H - 80, 46, 82, 7.4)
    ch.zone(2, 3.4, 57, 76, BOSC, op=0.08, dash=None)
    zz(ch, pts, INK, 2.4); dots(ch, pts[1:])
    ch.level(64, 1, 4, BOSC, 'đỉnh cũ', pos='l', dy=-6, dash='3,3')
    ch.level(57, 2, 6.4, PROT, 'protected low', pos='r', dy=16, sw=1.6)
    ch.lab(3.4, 76, 'BOS', dy=-8, color=BOSC)
    ch.lab(2.7, 68, 'chân sóng\nđã tạo BOS', dx=-30, dy=0, color=BOSC, size=10, anchor='end')
    ch.lab(6.6, 54, 'đóng dưới → CHoCH ↓', dy=16, dx=-6, color=CHC, size=10.5, anchor='end')
    yy = y0 + 64
    for t_, c_ in [('Cú tăng từ 57 lên 76 đã làm một việc: vượt đỉnh cũ 64 (BOS).', BOSC),
                   ('Đáy 57 là điểm xuất phát của cú tăng đó → protected low.', PROT),
                   ('Giá đóng dưới 57: mọi thứ cú tăng đó tạo ra đã bị trả lại hết. Câu “đáy sau cao hơn đáy trước” không còn đúng ở lớp này.', CHC),
                   ('Còn đáy 66 (giữa đường)? Phá nó chỉ là pullback sâu hơn, chưa xoá cú tăng nào.', SUB)]:
        yy = f.p(x + 370, yy, t_, 176, 11.6, c_) + 9
    f.foot('Đây là lý do “protected” không có nghĩa là “có người đang bảo vệ”. Nó có nghĩa: cả câu chuyện cấu trúc của lớp này DỰA trên mức đó.')
    return f.save()


# ------------------------------------------------------------------ 12 protected lifecycle
def fig12():
    f = F(12, 'Vong-Doi-Protected-Low', 'Vòng đời của một protected low: ứng viên → được bảo vệ → bị dời → bị tiêu thụ',
          'Một đáy không “sinh ra” là protected. Nó trở thành protected khi phóng ra một BOS, và mất vai trò khi có BOS mới hoặc khi bị phá.', h=560)
    y0 = f.top + 4
    base = [(0, 40), (1, 56), (2, 48)]
    stages = [('Ứng viên', base + [(2.8, 53)], 'Đáy 48 mới hình thành. Nó CHƯA phóng ra BOS nào → chưa protected. Protected vẫn là đáy 40.', None, (40, 'protected = 40')),
              ('Được bảo vệ', base + [(3.6, 63)], 'Giá từ 48 vượt đỉnh 56 (BOS). Đáy 48 được “thăng chức” thành protected low.', (48,), (48, 'protected = 48')),
              ('Bị dời lên', base + [(3.6, 63), (4.6, 55), (5.8, 71)], 'Từ đáy 55 có BOS mới qua 63. Protected dời lên 55. Đáy 48 thành mức tham chiếu sâu.', (55,), (55, 'protected = 55')),
              ('Bị tiêu thụ', base + [(3.6, 63), (4.6, 55), (5.8, 71), (7, 51)], 'Giá đóng dưới 55: protected low bị phá = CHoCH ↓ ở lớp này. Kết luận “đang tăng” mất hiệu lực.', (55,), (55, 'đã bị phá'))]
    for k, (ttl, pts, txt, mk_, lv) in enumerate(stages):
        x = 28 + k * 239; w = 227
        f.card(x, y0, w, 420, ttl, num=k + 1, tcolor=CHC if k == 3 else INK)
        ch = Chart(f, x + 14, y0 + 52, w - 28, 210, 36, 75, 7.6)
        ch.level(lv[0], 0 if lv[0] == 40 else [i for i, p in pts if p == lv[0]][0], 6.6, PROT if k < 3 else CHC, lv[1], pos='r', dy=16 if k != 3 else -6, sw=1.5)
        zz(ch, pts, INK, 2.2); dots(ch, pts[1:])
        if k >= 1: ch.lab(3.6, 63, 'BOS', dy=-8, color=BOSC, size=10)
        if k >= 2: ch.lab(5.8, 71, 'BOS', dy=-8, color=BOSC, size=10)
        if k == 3: ch.lab(7, 51, 'CHoCH ↓', dy=16, dx=-10, color=CHC, size=10.5, anchor='end')
        f.p(x + 14, y0 + 290, txt, w - 28, 12)
    f.foot('Cái bẫy: nhiều người coi MỌI đáy gần nhất là protected (như ở ô 1). Khi đó “CHoCH” xuất hiện liên tục và bias bị lật qua lật lại.')
    return f.save()


# ------------------------------------------------------------------ 13 market character
def fig13():
    f = F(13, 'Market-Character-La-Gi', '“Character” của thị trường gồm những gì? Bốn đặc điểm ta QUAN SÁT được',
          'Trend chỉ là HƯỚNG. Character là CÁCH giá đi theo hướng đó. Ví dụ dưới là một character tăng khỏe.', h=620)
    y0 = f.top + 4; H = 620 - y0 - 46
    f.card(28, y0, 470, H)
    cs, tn = gen(40, [(58, 3, 'i'), (52, 4, 'c'), (70, 3, 'i'), (64, 4, 'c'), (83, 3, 'i'), (77, 4, 'c')], u=1.0, seed=2)
    ch = Chart(f, 46, y0 + 30, 436, H - 60, 36, 88, len(cs) + 1)
    ch.level(64, tn[3][0], len(cs), PROT, 'protected low', pos='r', dy=17, sw=1.4)
    ch.candles(cs)
    ch.badge(tn[2][0], tn[2][1], 1, BOSC, dy=-20); ch.badge(tn[3][0], tn[3][1], 2, DISP, dy=22)
    ch.badge(tn[4][0] - 1, 75, 3, UP, dx=-22); ch.badge(len(cs) - 1, 64, 4, PROT, dy=-16)
    ch.lab(tn[1][0] + 2, 74, 'chân tăng: ít nến,\nthân to, đi nhanh', dx=0, dy=-40, color=UP, size=10)
    ch.lab(tn[3][0] - 1, 59, 'chân giảm: nhiều nến\nnhỏ, chồng lên nhau', dx=0, dy=40, color=DN, size=10)
    x = 512; w = 460
    f.card(x, y0, w, H, 'Bốn đặc điểm (bullish character)')
    items = [(1, BOSC, 'Ai tạo được cực trị mới?', 'Chỉ chân TĂNG vượt được đỉnh cũ. Chân giảm không bao giờ thủng được đáy cũ.'),
             (2, DISP, 'Pullback dừng ở đâu?', 'Mỗi lần lùi đều dừng ở mức CAO HƠN lần trước (HL).'),
             (3, UP, 'Chân đẩy vs chân hồi', 'Chân tăng ít nến, thân to, đi nhanh. Chân giảm nhiều nến nhỏ, chồng lên nhau, đi chậm.'),
             (4, PROT, 'Mức nào được giữ?', 'Đáy đã phóng ra cú tăng gần nhất (protected low) chưa bao giờ bị đóng nến xuyên qua.')]
    yy = y0 + 54
    for n, c, a, b in items:
        f.badge(x + 26, yy - 4, n, c)
        f.t(x + 44, yy, a, 13, True, c)
        yy = f.p(x + 44, yy + 18, b, w - 64, 12) + 12
    f.note(x + 16, yy + 4, w - 32, 'CHoCH xảy ra khi đặc điểm ① và ④ bị đảo: lần đầu tiên chân NGƯỢC chiều làm được việc mà trước đây chỉ chân thuận chiều làm được — phá mức mà cả cấu trúc dựa vào. Đặc điểm ② và ③ thường suy yếu TRƯỚC đó.', CHC, 'Change of Character = ① và ④ bị đảo', 12)
    f.foot('[OBSERVABLE] cả bốn đặc điểm đều đọc được từ OHLC. Còn “phe mua mạnh/yếu” là [INTERPRETATION] của những quan sát đó.')
    return f.save()


ALL = [fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08, fig09, fig10, fig11, fig12, fig13]
if __name__ == '__main__':
    sel = sys.argv[1:]
    for fn in ALL:
        if not sel or fn.__name__[3:] in sel:
            print(fn())
