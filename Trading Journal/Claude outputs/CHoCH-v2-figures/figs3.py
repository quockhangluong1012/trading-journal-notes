# -*- coding: utf-8 -*-
from chdraw import *
import sys


def cmini(f, x, y, w, h, title, segs, start, lvls, lo, hi, tcolor=INK, over=None, seed=3, n_extra=1, num=None, labs=(), zones=()):
    f.card(x, y, w, h, title, num=num, tcolor=tcolor, tsize=12.5)
    cs, tn = gen(start, segs, u=0.9, seed=seed, over=over)
    ch = Chart(f, x + 12, y + 52, w - 24, h - 66, lo, hi, len(cs) + n_extra)
    for z in zones: ch.zone(*z)
    for (p, a, b, c, lab, pos, dy) in lvls:
        ch.level(p, a, min(b, len(cs) - 1 + n_extra), c, lab, pos=pos, dy=dy, sw=1.3)
    ch.candles(cs)
    for (i, p, t_, c, dy, dx, an) in labs:
        ch.lab(i, p, t_, dy=dy, dx=dx, color=c, size=10, anchor=an)
    return ch, cs, tn


# ------------------------------------------------------------------ 27 displacement ELI5
def fig27():
    f = F(27, 'Displacement-ELI5-Canh-Cua', 'Displacement cho bé: mở cửa từ từ hay đạp tung cánh cửa?',
          'Cả hai cách đều đi qua được cửa (đều “phá” được mức). Nhưng cách đi qua cho ta biết thêm điều gì đó về lực đứng sau.', h=600, tag='ELI5')
    y0 = f.top + 4; H = 600 - y0 - 62
    f.card(28, y0, 300, H, 'Hai cách qua cửa', num=1)
    for k, (yy, lab, c) in enumerate([(y0 + 70, 'Hé từng chút một… kẽo kẹt', WARN), (y0 + 240, 'RẦM! Cửa bật tung', DISP)]):
        f.r(60, yy, 16, 120, fill='#9CA3AF', stroke=None, rx=2)
        if k == 0:
            f.o.append('<polygon points="76,%.1f 120,%.1f 120,%.1f 76,%.1f" fill="#D6B98C" stroke="#92400E" stroke-width="1.2"/>' % (yy, yy + 8, yy + 112, yy + 120))
            f.person(160, yy + 120, INK, 1.1); f.t(190, yy + 60, '…', 22, True, WARN)
        else:
            f.o.append('<polygon points="76,%.1f 170,%.1f 170,%.1f 76,%.1f" fill="#D6B98C" stroke="#92400E" stroke-width="1.2"/>' % (yy, yy - 30, yy + 90, yy + 120))
            f.person(220, yy + 120, INK, 1.1, 'up')
            for d in range(3): f.ln(240 + d * 8, yy + 40 + d * 14, 262 + d * 8, yy + 40 + d * 14, DISP, 2)
        f.t(60, yy + 146, lab, 12.5, True, c)
    f.p(44, y0 + 430, 'Đạp tung cửa không có nghĩa là người đó sẽ đi tiếp mãi. Nó chỉ cho thấy LỰC lúc đi qua rất lớn.', 270, 12)
    segsA = [(60, 4, 'c'), (55, 3, 'c'), (61, 4, 'g'), (58, 2, 'c'), (64, 5, 'g'), (62, 2, 'c'), (66, 3, 'g')]
    segsB = [(60, 4, 'c'), (55, 3, 'c'), (61, 4, 'c'), (57, 2, 'c'), (72, 3, 'i'), (69, 2, 'c'), (74, 2, 'i')]
    for k, (segs, ttl, c, txt) in enumerate([(segsA, 'Phá kiểu “bò qua” (không displacement)', WARN, 'Nến nhỏ, chồng lên nhau, nhiều râu ngược. Đóng nhỉnh hơn mức. Không để lại khoảng trống.'),
                                             (segsB, 'Phá bằng displacement', DISP, 'Vài nến thân to, đóng gần đỉnh nến, ít râu ngược. Giữa nến 1 và nến 3 của cú đẩy còn một khoảng trống: FVG.')]):
        x = 340 + k * 318; w = 306
        ch, cs, tn = cmini(f, x, y0, w, 330, ttl, segs, 52, [(61.3, 0, 30, PROT, 'mức bị phá', 'l', -6)], 50, 76, tcolor=c, num=k + 2, seed=5 + k)
        if k == 1:
            for (i, lo, hi) in fvgs(cs, 13, 17):
                ch.zone(i - 1, i + 1, lo, hi, FVGC, 'FVG' if i == 15 else None, 'r', '4,3', 0.16)
        f.p(x + 14, y0 + 352, txt, w - 28, 12)
    f.note(340, y0 + 424, 632, 'Displacement là thước đo CHẤT LƯỢNG của cú phá, không phải điều kiện ĐỊNH NGHĨA của CHoCH. Có thể có CHoCH không displacement (ô 2), và displacement không phá gì (hình 29).', SWP, None, 12)
    f.foot('Cách đo displacement (thân nến so với nến gần đây, ATR…) ở note 50. Ở đây chỉ dùng mắt: “nhanh, một chiều, thân to, để lại khoảng trống”.')
    return f.save()


# ------------------------------------------------------------------ 28 four separate events
def fig28():
    f = F(28, 'Pha-Displacement-FVG-Xac-Nhan-Tach-Roi', 'Bốn thứ KHÁC NHAU hay bị gộp làm một: phá cấu trúc, displacement, FVG, xác nhận',
          'Ma trận 2×2: hàng = có phá protected swing không; cột = có displacement không. Cả bốn ô đều xảy ra ngoài thị trường.', h=680)
    y0 = f.top + 4
    cells = [('Phá + displacement', GOOD, [(0, 60), (1, 48), (1.8, 53), (2.6, 44), (3.6, 66), (4.3, 61)], 'G1. Bằng chứng mạnh nhất mà cú phá có thể cho. Vẫn có thể thất bại.'),
             ('Phá, KHÔNG displacement', WARN, [(0, 60), (1, 48), (1.8, 53), (2.6, 44), (3, 49), (3.3, 47), (3.8, 52), (4.1, 50.5), (4.6, 55)], 'G0. Vẫn là CHoCH theo định nghĩa. Ít thông tin về lực.'),
             ('Displacement, KHÔNG phá', TEAL, [(0, 60), (1, 48), (1.8, 53), (2.6, 44), (3.4, 52), (4.2, 47)], 'Chân sóng mạnh nhưng dừng dưới protected high. Chưa đổi trạng thái — chỉ là một cú hồi mạnh.'),
             ('Không phá, không displacement', MUTE, [(0, 60), (1, 48), (1.8, 53), (2.6, 44), (3.1, 48), (3.5, 46), (4.2, 50), (4.6, 47)], 'Hồi yếu trong cấu trúc giảm. Không có gì để gọi tên.')]
    for k, (ttl, c, pts, txt) in enumerate(cells):
        r, cc = divmod(k, 2)
        x = 168 + cc * 402; y = y0 + 30 + r * 236; w = 390
        f.card(x, y, w, 226, ttl, tcolor=c)
        ch = Chart(f, x + 14, y + 46, 190, 166, 40, 70, 5)
        ch.level(53, 1.8, 4.6, PROT, None, sw=1.3)
        sw_ = 3.2 if k in (0, 2) else 1.8
        zz(ch, pts, c if k != 3 else INK, sw_)
        if k == 0: ch.zone(2.9, 3.3, 51, 57, FVGC, op=0.2, dash=None)
        f.p(x + 214, y + 64, txt, w - 228, 12)
    f.t(160, y0 + 150, 'PHÁ', 12, True, INK, 'end'); f.t(160, y0 + 166, 'protected', 11, False, SUB, 'end')
    f.t(160, y0 + 386, 'KHÔNG phá', 12, True, INK, 'end')
    f.t(363, y0 + 22, 'CÓ displacement', 12, True, INK, 'middle'); f.t(765, y0 + 22, 'KHÔNG displacement', 12, True, INK, 'middle')
    f.note(28, y0 + 510, 944, 'FVG là DẤU VẾT để lại bởi displacement (khoảng trống giữa nến 1 và nến 3). “Xác nhận” là chuyện của các nến SAU (G2, G3). Bốn thứ này xảy ra ở những thời điểm khác nhau — ghi chúng thành bốn cột riêng trong journal.', BOSC, None, 12.2)
    f.foot('Đường cam = protected high của cấu trúc giảm. Nét dày = chân sóng có displacement. Ô xanh lam nhỏ = FVG.')
    return f.save()


# ------------------------------------------------------------------ 29 five displacement examples
def fig29():
    f = F(29, 'Nam-Vi-Du-Pha-va-Displacement', 'Năm ví dụ: cú phá, displacement và điều xảy ra sau đó',
          'Cùng một cấu trúc giảm với protected high (cam). Mỗi ô thay đổi đúng MỘT yếu tố. Đường xám = phần tương lai mà lúc phá ta chưa biết.', h=600)
    y0 = f.top + 4
    S = [('Phá + displacement + FVG', GOOD, [(56, 4, 'c'), (61, 3, 'c'), (52, 3, 'c'), (66, 3, 'i'), (62, 2, 'c'), (70, 3, 'i')], {}, 'Ví dụ “sách giáo khoa”. Hồi giữ được trên FVG.'),
         ('Phá, không displacement', WARN, [(56, 4, 'c'), (61, 3, 'c'), (52, 3, 'c'), (57, 3, 'g'), (55, 2, 'c'), (62.5, 4, 'g'), (60, 2, 'g')], {}, 'Đóng qua mức bằng nến nhỏ. CHoCH G0. Chưa nói được gì về lực.'),
         ('Displacement, không phá', TEAL, [(56, 4, 'c'), (61, 3, 'c'), (52, 3, 'c'), (59.5, 2, 'i'), (56, 3, 'c'), (50, 3, 'i')], {}, 'Chân tăng mạnh nhưng dừng dưới mức. Không có CHoCH. Giảm tiếp.'),
         ('Râu phá rồi quay về', BAD, [(56, 4, 'c'), (61, 3, 'c'), (52, 3, 'c'), (59, 3, 'c'), (58, 1, 'c'), (53, 3, 'c'), (49, 2, 'i')], {13: {'h': 63}}, 'Chỉ râu vượt mức, thân đóng bên dưới. Chưa phải CHoCH — nhiều khả năng là quét đỉnh.'),
         ('Displacement mạnh rồi thất bại', BAD, [(56, 4, 'c'), (61, 3, 'c'), (52, 3, 'c'), (66, 3, 'i'), (63, 2, 'c'), (55, 2, 'i'), (49, 2, 'i')], {}, 'CHoCH G1 thật. Nhưng giá rơi lại qua cả gốc cú đẩy. Bằng chứng mạnh vẫn có thể sai.')]
    for k, (ttl, c, segs, ov, txt) in enumerate(S):
        x = 28 + k * 190; w = 180
        ch, cs, tn = cmini(f, x, y0, w, 330, ttl, segs, 60, [(61.3, 3, 40, PROT, None, 'r', -6)], 46, 72, tcolor=c, over=ov, seed=9 + k)
        f.p(x + 12, y0 + 352, txt, w - 24, 11.6)
    f.foot('Ô 4 và ô 5 trông giống nhau ở nến phá, khác nhau hoàn toàn ở thân nến đóng cửa và ở tương lai. Chỉ thân nến đóng cửa là biết được ngay lúc đó.')
    return f.save()


# ------------------------------------------------------------------ 30 location / evidence / trigger
def fig30():
    f = F(30, 'Vi-Tri-Bang-Chung-Kich-Hoat', 'Ba câu hỏi khác nhau: Ở ĐÂU? — CẤU TRÚC ĐÃ ĐỔI CHƯA? — VÀO LỆNH KHI NÀO?',
          'CHoCH chỉ trả lời câu hỏi thứ hai. Gộp ba câu làm một là lý do phổ biến nhất của việc “thấy CHoCH là vào lệnh”.', h=625)
    y0 = f.top + 4
    gates = [('LOCATION', 'Giá đang ở đâu?', 'Đúng nhà chưa?', ['HTF POI (FVG, OB… của H1/D1)', 'Premium hay discount của dealing range', 'Gần thanh khoản nào, xa thanh khoản nào'], BOSC,
              'Không thuộc về CHoCH. Trả lời TRƯỚC khi nhìn khung nhỏ.'),
             ('STRUCTURAL EVIDENCE', 'Cấu trúc đã đổi chưa?', 'Cửa đã mở chưa?', ['CHoCH / MSS ở lớp và khung đã khai báo', 'Bậc G0 → G3', 'Có displacement không'], CHC,
              'Đây là việc của CHoCH. Nó là BẰNG CHỨNG, chưa phải lệnh.'),
             ('ENTRY TRIGGER', 'Vào lệnh khi nào, ở đâu?', 'Được mời vào chưa?', ['Giá hồi vào FVG / OB của cú phá', 'Dừng lỗ: bên kia điểm gốc cú phá', 'Mục tiêu: thanh khoản phía trước, R:R đủ'], DISP,
              'Quy tắc của MÔ HÌNH vào lệnh (ICT 2022), không phải của CHoCH.')]
    for k, (en, q, eli, items, c, foot) in enumerate(gates):
        x = 28 + k * 318; w = 306
        f.r(x, y0, w, 440, fill=CARD, stroke=c, sw=1.8, rx=12)
        f.r(x, y0, w, 54, fill=c, stroke=None, rx=12, op=0.12)
        f.badge(x + 26, y0 + 27, k + 1, c, 12, 12)
        f.t(x + 46, y0 + 24, en, 13, True, c); f.t(x + 46, y0 + 42, q, 12, False, INK)
        f.t(x + 18, y0 + 84, 'Cho bé: “' + eli + '”', 12.5, True, c, italic=True)
        yy = y0 + 118
        for it in items:
            f.t(x + 20, yy, '•', 12, True, c); yy = f.p(x + 32, yy, it, w - 52, 12) + 6
        f.note(x + 14, y0 + 330, w - 28, foot, c, None, 12)
        if k < 2: f.arrow(x + w + 1, y0 + 220, x + w + 11, y0 + 220, SUB, 2, size=7)
    f.note(28, y0 + 452, 944, 'Ba câu hỏi phải được trả lời ĐỘC LẬP và THEO THỨ TỰ. Một CHoCH đẹp ở sai nhà (câu 1 sai) vẫn là “không có lệnh”. Một CHoCH đúng nhà nhưng giá không hồi về vùng vào lệnh (câu 3 không xảy ra) cũng là “không có lệnh”.', BAD, None, 12.2)
    f.foot('POI = Point of Interest. FVG/OB = các vùng giá theo ICT. Chi tiết ở note 13, 25, 27, 55.')
    return f.save()


# ------------------------------------------------------------------ 31 what choch leaves behind
def fig31():
    f = F(31, 'CHoCH-De-Lai-Gi-Tren-Chart', 'Một CHoCH để lại gì trên chart? Bản đồ mới sau cú phá',
          'Tiếp tục hình 19. Ngay khi nến CHoCH đóng cửa, ta có thể vẽ lại vài thứ — tất cả đều là ỨNG VIÊN, chưa phải bằng chứng.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 46
    f.card(28, y0, 600, H)
    cs, tn = bull_seq()
    ch = Chart(f, 44, y0 + 26, 570, H - 46, 50, 88, 34)
    ch.zone(27, 33, 54.6, 65.95, UP, None, 'tl', None, 0.06)
    ch.zone(27, 33, 65.95, 77.3, DN, None, 'tl', None, 0.06)
    for (i, lo, hi) in fvgs(cs, 28, 32):
        if i in (29, 30): ch.zone(i - 1, 33, lo, hi, FVGC, None, 'tl', '4,3', 0.15)
    ch.zone(27, 33, 54.6, 61.0, OBC, None, 'tl', '5,3', 0.12)
    ch.level(54.6, 27, 33, PROT, None, sw=1.6)
    ch.level(65.95, 27, 33, STR, None, dash='2,3', sw=1)
    ch.level(72.3, 18, 31, MUTE, None, dash='4,3', sw=1.2)
    ch.level(79.3, 10, 33, SWP, None, dash='4,3', sw=1.2)
    ch.candles(cs, upto=32)
    ch.fog(32.5, None)
    ch.lab(27, 54.6, '① protected low MỚI = đáy quét', dx=-6, dy=16, color=PROT, anchor='end')
    ch.lab(30, 64, '② FVG', dx=8, dy=0, color=FVGC, anchor='start')
    ch.lab(27, 59, '③ OB', dx=-12, dy=4, color=OBC, anchor='end')
    ch.lab(26.6, 65.95, '④ EQ', dx=0, dy=4, color=STR, anchor='end')
    ch.lab(12, 79.3, '⑤ đỉnh LH1: thanh khoản phía trên', dy=-8, color=SWP)
    ch.lab(31, 77.3, 'CHoCH', dy=-8, color=CHC)
    x = 642; w = 330
    f.card(x, y0, w, H, 'Những thứ mới xuất hiện')
    rows = [(1, PROT, 'Mức vô hiệu mới', 'Đáy quét 54.6. Đóng nến dưới nó = câu chuyện tăng sai. Thường là chỗ đặt dừng lỗ.'),
            (2, FVGC, 'FVG trong cú phá', 'Vùng giá có thể được quay lại. Là ỨNG VIÊN vào lệnh, không phải lời hứa.'),
            (3, OBC, 'Order Block gốc', 'Nến giảm cuối cùng trước cú đẩy. Một ứng viên vùng khác.'),
            (4, STR, 'Dealing range mới', 'Từ đáy quét đến đỉnh CHoCH. Dưới đường giữa (EQ) là discount, trên là premium.'),
            (5, SWP, 'Thanh khoản phía trước', 'Đỉnh cũ chưa bị lấy: một ứng viên mục tiêu (DOL).')]
    side_steps(f, x + 14, y0 + 52, w - 28, rows)
    f.foot('Số trên chart là giá minh họa. Vùng xám bên phải = tương lai chưa biết. Không ứng viên nào ở đây đã được chứng minh là có lợi thế — BACKTEST REQUIRED.')
    return f.save()


def side_steps(f, x, y, w, rows, size=11.8, gap=8):
    yy = y
    for n, c, a, b in rows:
        f.badge(x + 12, yy - 4, n, c)
        f.t(x + 30, yy, a, 12.5, True, c)
        yy = f.p(x + 30, yy + 17, b, w - 30, size) + gap
    return yy


# ------------------------------------------------------------------ 32 POI x CHoCH
def fig32():
    f = F(32, 'POI-va-CHoCH-Co-Doc-Lap-Khong', 'POI và CHoCH: hai bằng chứng độc lập, hay một bằng chứng đếm hai lần?',
          'Ma trận vị trí × cấu trúc. Câu hỏi ở dưới cùng quan trọng hơn cả bốn ô.', h=625)
    y0 = f.top + 4
    cells = [('Ở POI + có CHoCH', GOOD, 'Trường hợp mô hình ICT 2022 tìm kiếm. Vẫn chỉ là ứng viên.'),
             ('Ở POI, KHÔNG CHoCH', WARN, 'Giá chạm vùng nhưng cấu trúc khung nhỏ chưa đổi. Chờ — hoặc giá đi xuyên POI.'),
             ('Ngoài POI + có CHoCH', WARN, 'Cấu trúc đổi giữa “không đâu cả”. Có thông tin, nhưng thiếu lý do vị trí.'),
             ('Ngoài POI, KHÔNG CHoCH', MUTE, 'Không có gì để làm.')]
    for k, (ttl, c, txt) in enumerate(cells):
        r, cc = divmod(k, 2)
        x = 168 + cc * 402; y = y0 + 30 + r * 138; w = 390
        f.card(x, y, w, 128, ttl, tcolor=c)
        f.p(x + 16, y + 56, txt, w - 32, 12.2)
    f.t(160, y0 + 96, 'Ở POI', 12, True, INK, 'end'); f.t(160, y0 + 234, 'Ngoài POI', 12, True, INK, 'end')
    f.t(363, y0 + 22, 'CÓ CHoCH khung nhỏ', 12, True, INK, 'middle'); f.t(765, y0 + 22, 'KHÔNG CHoCH', 12, True, INK, 'middle')
    f.note(28, y0 + 316, 944, 'Nếu một POI là nơi giá hay đảo chiều, thì MỖI LẦN giá đảo chiều ở đó, khung nhỏ gần như chắc chắn sẽ in ra một CHoCH — vì đảo chiều nào cũng phải phá một đỉnh/đáy nhỏ. Như vậy CHoCH tại POI một phần là HỆ QUẢ của việc giá đảo chiều tại POI, không phải một bằng chứng hoàn toàn mới. Cộng “điểm POI” với “điểm CHoCH” như hai lý do độc lập có thể là đếm trùng.', BAD, 'Cái bẫy đếm hai lần', 12.4)
    f.note(28, y0 + 436, 944, 'Cách kiểm tra: so sánh kết quả của “POI + CHoCH” với “POI + vào lệnh ở lần chạm đầu” và với “CHoCH ngoài POI”. Nếu cộng thêm CHoCH không cải thiện kỳ vọng (E[R]) so với POI đơn thuần, CHoCH đang không thêm thông tin. [HYPOTHESIS — BACKTEST REQUIRED]', BOSC, 'Kiểm chứng thế nào', 12.4)
    f.foot('“Location” và “structural evidence” vẫn là hai câu hỏi khác nhau (hình 30). Điều chưa biết là chúng có cho hai mẩu thông tin khác nhau hay không.')
    return f.save()


# ------------------------------------------------------------------ 33 D1/H1/M5 nesting
def fig33():
    f = F(33, 'D1-H1-M5-Long-Nhau', 'D1 tăng → H1 hồi giảm → M5 CHoCH tăng: ba câu chuyện lồng vào nhau',
          'Mỗi khung kể một câu chuyện riêng. M5 CHoCH tăng ở đây là tín hiệu “có thể đợt hồi H1 đang kết thúc” — KHÔNG phải tín hiệu đổi D1.', h=665)
    y0 = f.top + 4
    P = [('D1 — CONTEXT', BOSC, [(0, 30), (2, 60), (3, 48), (5, 80), (6.2, 64)], (64, 52, 'POI D1 (discount)'), 'Cấu trúc tăng. Giá đang hồi vào vùng discount, chạm POI D1. Protected low D1 = 48 còn nguyên.'),
         ('H1 — SETUP', CHC, [(0, 80), (1, 72), (1.6, 76), (2.6, 68), (3.2, 71.5), (4.2, 64), (4.8, 66.5), (5.4, 62.5)], (66, 60, 'POI H1 trong POI D1'), 'Bên trong đợt hồi D1, H1 là cấu trúc GIẢM (LH–LL). Đó là “hành khách đi ngược con tàu”.'),
         ('M5 — EXECUTION', DISP, [(0, 66.6), (1, 64.6), (1.6, 65.6), (2.4, 63.4), (3.4, 66.2), (4, 65.1), (5, 67.4)], (65.6, 65.6, None), 'Ở POI H1: quét đáy nhỏ → giá vượt đỉnh M5 gần nhất bằng displacement = M5 CHoCH ↑. Đây là “con kiến đổi hướng”.')]
    for k, (ttl, c, pts, zone, txt) in enumerate(P):
        x = 28 + k * 318; w = 306
        f.card(x, y0, w, 470, ttl, num=k + 1, tcolor=c)
        lo = min(p for i, p in pts) - 4; hi = max(p for i, p in pts) + 4
        if k == 2: lo, hi = 62, 68.5
        ch = Chart(f, x + 16, y0 + 50, w - 32, 230, lo, hi, max(i for i, p in pts) + 1.2)
        if zone[2]:
            ch.zone(max(i for i, p in pts) - 1.4, max(i for i, p in pts) + 0.1, zone[0], zone[1], c, zone[2], 'al', '4,3', 0.12, 10)
        if k == 2:
            ch.level(65.6, 1.6, 4.9, PROT, 'protected high M5', pos='l', dy=-6)
            ch.lab(2.4, 63.4, 'quét', dy=15, color=SWP, size=10); ch.lab(3.4, 66.2, 'CHoCH ↑', dy=-9, color=CHC, size=10)
        zz(ch, pts, INK, 2.3); dots(ch, pts[1:], INK, 3)
        f.p(x + 16, y0 + 310, txt, w - 32, 12)
        if k < 2:
            f.arrow(x + w + 1, y0 + 160, x + w + 11, y0 + 160, SUB, 2, size=7)
    f.note(28, y0 + 480, 944, 'Đọc đúng: D1 vẫn tăng (không cần “xác nhận lại”). H1 đang hồi; M5 CHoCH ↑ tại POI là gợi ý đầu tiên rằng đợt hồi H1 có thể dừng. Muốn nói “H1 đã đổi chiều” cần H1 phá protected high của chính H1 (bậc 4 ở hình 18).', BOSC, None, 12)
    f.foot('Quy tắc phân quyền (RULE-CHOCH-006): mỗi CHoCH chỉ có quyền thay đổi kết luận ở chính khung và lớp của nó.')
    return f.save()


# ------------------------------------------------------------------ 34 internal grows into external
def fig34():
    f = F(34, 'Internal-Lon-Dan-Thanh-External', 'Khi nào một CHoCH nhỏ “lớn lên” thành thay đổi cấu trúc lớn?',
          'Bốn ảnh chụp một đợt hồi giảm của H1. Mỗi bước, lớp lớn hơn mới đổi. Phần lớn các M5 CHoCH dừng lại ở ô 1 hoặc 2.', h=625)
    y0 = f.top + 4
    base = [(0, 80), (1, 72), (1.6, 76), (2.6, 68), (3.2, 71.5), (4.2, 64)]
    S = [('Chỉ M5 CHoCH', base + [(4.8, 67)], 'Đỉnh nhỏ M5 bị vượt. H1 vẫn hoàn toàn giảm.', None),
         ('M5 có cấu trúc tăng', base + [(4.8, 67), (5.2, 65.5), (5.8, 69)], 'M5 có HL mới + BOS ↑. M5 đã đổi. H1 vẫn giảm (dưới 71.5).', None),
         ('H1 CHoCH', base + [(4.8, 67), (5.2, 65.5), (6.2, 73)], 'Giá đóng trên protected high H1 (71.5). Bây giờ H1 mới đổi “character”.', 71.5),
         ('H1 cấu trúc mới', base + [(4.8, 67), (5.2, 65.5), (6.2, 73), (6.9, 69), (7.8, 77)], 'H1 có HL mới và BOS ↑. Đợt hồi H1 đã kết thúc ở lớp này. D1 tăng được tiếp tục.', 71.5)]
    for k, (ttl, pts, txt, ph) in enumerate(S):
        x = 28 + k * 239; w = 227
        f.card(x, y0, w, 440, ttl, num=k + 1, tcolor=[STR, DISP, CHC, BOSC][k])
        ch = Chart(f, x + 12, y0 + 50, w - 24, 230, 60, 84, 8.4)
        ch.level(71.5, 3.2, 7.6, PROT if k < 2 else CHC, 'protected high H1', pos='l', dy=-6, sw=1.3)
        zz(ch, pts, INK, 2.2); dots(ch, pts[1:], INK, 2.8)
        f.p(x + 14, y0 + 304, txt, w - 28, 12)
    f.note(28, y0 + 452, 944, 'Không có quy luật nào nói M5 CHoCH sẽ đi tiếp tới ô 4. Tỷ lệ chuyển từ ô 1 → 2 → 3 → 4 là thứ cần ĐO trên dữ liệu của chính bạn. [BACKTEST REQUIRED]', CHC, None, 12)
    f.foot('Cùng logic cho chiều ngược lại. Một H1 CHoCH cũng chỉ là “ô 1” của D1.')
    return f.save()


# ------------------------------------------------------------------ 35/36 false choch gallery
def gallery(num, slug, title, sub, items, foot):
    f = F(num, slug, title, sub, h=620)
    y0 = f.top + 4
    for k, (ttl, pts, lv, labs, txt, zones) in enumerate(items):
        x = 28 + k * 190; w = 180
        f.card(x, y0, w, 470, ttl, num=k + 1 + (5 if num == 36 else 0), tcolor=BAD, tsize=12)
        n = max(i for i, p in pts) + 1
        ch = Chart(f, x + 10, y0 + 66, w - 20, 200, 36, 84, n)
        for z in zones: ch.zone(*z)
        for (p, a, b, c, d) in lv: ch.level(p, a, b, c, None, dash=d, sw=1.2)
        zz(ch, pts, INK, 2.1); dots(ch, pts[1:], INK, 2.8)
        for (i, p, t_, c, dy) in labs: ch.lab(i, p, t_, dy=dy, color=c, size=9.5)
        f.p(x + 12, y0 + 290, txt, w - 24, 11.3)
    f.foot(foot)
    return f.save()


def fig35():
    items = [('Chỉ râu phá', [(0, 44), (1, 56), (1.8, 50), (3, 66), (3.8, 57), (4.3, 62), (4.8, 55.5), (5.3, 58), (6.5, 72)], [(57, 3.8, 6.4, PROT, None)], [(4.8, 55.5, 'râu', SWP, 14)],
              'Thiếu: thân nến đóng ngoài mức. Đây nhiều khả năng là quét, không phải CHoCH. Từ chối gọi tên cho tới khi có nến đóng.', []),
             ('Phá không displacement', [(0, 44), (1, 56), (1.8, 50), (3, 66), (3.8, 57), (4.3, 60), (4.7, 56), (5.1, 58), (5.5, 55.6), (6, 60), (7, 68)], [(57, 3.8, 6.9, PROT, None)], [(5.5, 55.6, 'bò qua', WARN, 14)],
              'Thiếu: lực. Giá trôi qua mức bằng nến nhỏ rồi quay lại. Hợp lệ G0 nhưng không đủ để hành động.', []),
             ('Internal trong trend mạnh', [(0, 40), (2, 66), (2.6, 60), (3.1, 63), (3.6, 58), (4.4, 74), (5.2, 80)], [(40, 0, 5, PROT, None), (60, 2.6, 3.8, CHC, '3,3')], [(3.6, 58, 'CHoCH internal', CHC, 14)],
              'Thiếu: tầm vóc. Chỉ đáy nhỏ bị phá; protected low external ở tận dưới. Trend lớn tiếp tục.', []),
             ('Trong vùng đi ngang', [(0, 54), (0.8, 64), (1.6, 53), (2.4, 63.5), (3.2, 55), (4, 64.5), (4.8, 52.5), (5.6, 62), (6.4, 55)], [], [(4, 64.5, 'phá?', CHC, -8), (4.8, 52.5, 'phá?', CHC, 14)],
              'Thiếu: trạng thái để bị phá. Đỉnh/đáy chồng lên nhau. Mọi “CHoCH” ở đây đều là nhiễu.', [(0, 6.4, 52, 65, STR, None, 'tl', '4,3', 0.06)]),
             ('Giữa range, ngoài POI', [(0, 76), (1, 64), (1.8, 70), (2.8, 58), (3.6, 63), (4.4, 56), (5.4, 66), (6, 62)], [(63, 3.6, 5.9, PROT, None)], [(5.4, 66, 'CHoCH ↑', CHC, -8)],
              'Thiếu: vị trí. CHoCH ở giữa dealing range, không có POI, không quét. Có, nhưng chẳng chỉ về đâu.', [])]
    return gallery(35, 'False-CHoCH-1-5', 'Mười kiểu CHoCH “giả” hoặc chưa đủ cơ sở (1–5)',
                   'Mỗi ô: điều làm nó TRÔNG GIỐNG CHoCH, và bằng chứng nào CÒN THIẾU. Không gán mọi thất bại cho “thiếu một điều kiện” — xem ô 6 ở hình sau.', items,
                   'Cam = protected swing của lớp đang xét. Đây là sơ đồ dựng; mỗi kiểu là một giả thuyết thất bại cần được đếm trong backtest.')


def fig36():
    items = [('Có quét, xu hướng cũ vẫn chạy', [(0, 76), (1, 64), (1.8, 70), (2.8, 58), (3.6, 63), (4.3, 55), (5.3, 66), (6, 61), (6.6, 64), (7.6, 50)], [(63, 3.6, 7.5, PROT, None), (58, 2.8, 7.5, SWP, '3,3')], [(4.3, 55, 'quét', SWP, 14), (5.3, 66, 'CHoCH', CHC, -8)],
              'Có đủ: quét, CHoCH. Vẫn thất bại. Đây là thất bại BÌNH THƯỜNG của một xác suất, không phải lỗi nhận diện.', []),
             ('FVG không giữ', [(0, 76), (1, 64), (1.8, 70), (2.8, 58), (3.6, 63), (4.3, 55), (5.3, 69), (6.3, 58), (7.2, 52)], [(63, 3.6, 7.1, PROT, None)], [(5.3, 69, 'CHoCH', CHC, -8), (6.3, 58, 'xuyên FVG', BAD, 14)],
              'Giá quay về xuyên qua FVG của cú phá, đóng bên dưới. Lý do để vào lệnh ở đó đã mất.', [(4.6, 4.95, 59, 64, FVGC, None, 'tl', None, 0.2)]),
             ('Phá rồi reclaim nhanh', [(0, 76), (1, 64), (1.8, 70), (2.8, 58), (3.6, 63), (4.3, 57), (4.9, 64.5), (5.4, 60), (6.4, 52)], [(63, 3.6, 6.3, PROT, None)], [(4.9, 64.5, 'đóng trên', CHC, -8), (5.4, 60, 'đóng lại dưới', BAD, 14)],
              'Đóng qua mức một nến rồi ngay nến sau đóng ngược trở lại. Chưa bao giờ lên G2.', []),
             ('Ngược D1', [(0, 50), (1, 60), (1.8, 56), (2.8, 70), (3.6, 64), (4.2, 67), (4.8, 62), (5.6, 72), (6.4, 80)], [(64, 3.6, 6.3, PROT, None)], [(4.8, 62, 'M5 CHoCH ↓', CHC, 14), (5.9, 79, 'D1 tăng tiếp', BOSC, -8)],
              'CHoCH khung nhỏ chống lại xu hướng khung lớn, không ở POI lớn nào. Thường chỉ là một nhịp hồi.', []),
             ('Nến tin tức', [(0, 76), (1, 64), (1.8, 70), (2.8, 58), (3.6, 63), (4.1, 61), (4.4, 72), (4.7, 57), (5.6, 60), (6.4, 52)], [(63, 3.6, 6.3, PROT, None)], [(4.4, 72, 'giật lên', CHC, -8), (4.7, 57, 'giật xuống', BAD, 14)],
              'Một nến tin quét cả hai phía. Spread giãn, râu dài. Cấu trúc trong phút đó ít có ý nghĩa.', [])]
    return gallery(36, 'False-CHoCH-6-10', 'Mười kiểu CHoCH “giả” hoặc chưa đủ cơ sở (6–10)',
                   'Ô 6 là quan trọng nhất: một CHoCH có ĐỦ mọi bằng chứng vẫn có thể thất bại. Không có bộ điều kiện nào biến một cảnh báo thành chắc chắn.', items,
                   'Mỗi thất bại phải được ghi lại trong backtest như mọi mẫu khác — loại bỏ chúng sau khi đã biết kết quả là hindsight.')


# ------------------------------------------------------------------ 37 market conditions
def fig37():
    f = F(37, 'CHoCH-Trong-Bon-Dieu-Kien-Thi-Truong', 'CHoCH trong bốn điều kiện thị trường',
          'Cùng một định nghĩa, nhưng giá trị thông tin rất khác nhau tùy bối cảnh.', h=600)
    y0 = f.top + 4
    S = [('Xu hướng mạnh', [(0, 40), (1.5, 58), (2.1, 54), (2.5, 56), (2.9, 52.5), (4.3, 70), (5, 66), (6.5, 82)], 'CHoCH internal trong pullback là chuyện thường. Thường là điểm KẾT THÚC đợt hồi, không phải đỉnh xu hướng.', BOSC, [(2.9, 52.5, 'CHoCH internal', CHC, 14)]),
         ('Đi ngang', [(0, 56), (0.8, 66), (1.6, 55), (2.4, 65.5), (3.2, 56.5), (4, 67), (4.8, 54), (5.6, 65), (6.5, 57)], 'CHoCH lên, CHoCH xuống liên tục. Phá xong lại quay về. Thông tin thấp nhất.', STR, [(4, 67, 'phá', CHC, -8), (4.8, 54, 'phá', CHC, 14)]),
         ('Đảo chiều thật', [(0, 40), (1.2, 58), (1.9, 52), (3, 72), (3.6, 66), (4.2, 74), (5, 50), (5.7, 60), (6.6, 44)], 'Quét đỉnh → CHoCH ↓ có lực → đỉnh thấp hơn → BOS ↓. Chỉ nhận ra chắc chắn ở bước cuối.', GOOD, [(4.2, 74, 'quét', SWP, -8), (5, 50, 'CHoCH ↓', CHC, 14), (6.1, 44, 'BOS ↓', BOSC, 14)]),
         ('Tin tức', [(0, 56), (1, 62), (1.8, 58), (2.6, 63), (2.9, 74), (3.1, 50), (3.3, 70), (4.2, 60), (5, 64), (6, 59)], 'Một hai nến quét cả hai phía. Mọi mức đều bị “phá”. Nên đứng ngoài và vẽ lại cấu trúc SAU khi biến động lắng xuống.', BAD, [(2.9, 74, 'giật', CHC, -8), (3.1, 50, 'giật', CHC, 14)])]
    for k, (ttl, pts, txt, c, labs) in enumerate(S):
        x = 28 + k * 239; w = 227
        f.card(x, y0, w, 450, ttl, num=k + 1, tcolor=c)
        ch = Chart(f, x + 12, y0 + 50, w - 24, 230, 36, 86, 7)
        zz(ch, pts, INK, 2.2); dots(ch, pts[1:], INK, 2.8)
        for (i, p, t_, cc, dy) in labs: ch.lab(i, p, t_, dy=dy, color=cc, size=10)
        f.p(x + 14, y0 + 304, txt, w - 28, 12)
    f.foot('Bối cảnh (trend, range, tin) không nằm trong định nghĩa CHoCH — nhưng nó quyết định một CHoCH có đáng để đọc hay không.')
    return f.save()


# ------------------------------------------------------------------ 38 real-time T0-T5
def fig38():
    f = F(38, 'Real-Time-T0-T5', 'Real-time: một CHoCH được nhìn qua sáu thời điểm T0 → T5',
          'Phía bên phải đường đứt là tương lai. Ở mỗi thời điểm, chỉ được dùng thứ nằm bên trái. Đây là cách duy nhất để học CHoCH mà không tự lừa mình.', h=640)
    y0 = f.top + 4
    full = [(0, 70), (1, 60), (1.7, 65), (2.6, 55), (3.2, 59), (3.8, 53), (4.6, 63), (5.2, 60), (5.9, 68), (6.5, 65), (7.2, 72)]
    cuts = [(3.2, 'T0', 'Cấu trúc giảm. Protected high = 65. Không có gì để làm.'),
            (3.8, 'T1', 'Giá thủng đáy 55 bằng râu? Mới biết: đáy mới 53. Chưa biết là quét hay giảm tiếp.'),
            (4.6, 'T2', 'Giá đi lên, chưa tới 65. Có thể chỉ là hồi. CHƯA có CHoCH.'),
            (5.9, 'T3', 'Thân nến đóng trên 65 = CHoCH G0/G1. Mới chỉ là cảnh báo.'),
            (6.5, 'T4', 'Giá hồi nhưng giữ trên 60 → có HL ứng viên. Lên G2.'),
            (7.2, 'T5', 'Vượt đỉnh 68 = BOS ↑ đầu tiên → G3. Bây giờ cấu trúc tăng mới có hình dạng.')]
    for k, (cut, tl, txt) in enumerate(cuts):
        r, cc = divmod(k, 3)
        x = 28 + cc * 318; y = y0 + r * 268; w = 306
        f.card(x, y, w, 258, None)
        f.pill(x + 12, y + 12, tl, CHC if k == 3 else (GOOD if k == 5 else INK), 11)
        ch = Chart(f, x + 14, y + 40, w - 28, 130, 50, 75, 8)
        vis = [p for p in full if p[0] <= cut + 1e-9]
        ch.level(65, 1.7, 7.4, PROT, None, sw=1.2)
        zz(ch, vis, INK, 2.2); dots(ch, vis[1:], INK, 2.8)
        ch.fog(cut + 0.35, None)
        f.p(x + 14, y + 194, txt, w - 28, 11.8)
    f.foot('Chú ý T3: đó là lúc gần như mọi người “thấy CHoCH”. Nhưng thông tin làm nó trông đẹp trên chart lưu (T4, T5) chưa tồn tại ở T3.')
    return f.save()


# ------------------------------------------------------------------ 39 hindsight swing
def fig39():
    f = F(39, 'Hindsight-Swing-Va-Nhan-Ve-Lai', 'Hindsight: chart nhìn lại luôn đẹp hơn chart lúc đang chạy',
          'Trái: chart đã xong, mắt ta thấy ngay một “HL” và một “CHoCH”. Phải: cùng chart lúc nến phá vừa đóng cửa — cái “HL” đó chưa bao giờ là swing đã xác nhận.', h=600)
    y0 = f.top + 4; H = 600 - y0 - 46
    cs, tn = gen(60, [(68, 4, 'c'), (64, 2, 'c'), (66, 1, 'c'), (60, 3, 'i'), (55, 3, 'c'), (52, 2, 'c')], u=0.8, seed=21)
    lowi, lowp = tn[1][0], tn[1][1]
    for k, (ttl, upto, c) in enumerate([('Nhìn lại (hindsight)', None, SUB), ('Lúc đang xảy ra (real-time)', 9, CHC)]):
        x = 28 + k * 478; w = 466
        f.card(x, y0, w, H, ttl, num=k + 1, tcolor=c)
        ch = Chart(f, x + 18, y0 + 50, 230, H - 70, 50, 70, len(cs) + 1)
        if k == 0:
            ch.level(lowp, lowi, len(cs) - 1, PROT, '“HL”', pos='l', dy=16)
            ch.candles(cs)
            ch.lab(lowi + 3, lowp - 1.5, 'CHoCH ↓', dx=6, dy=0, color=CHC, anchor='start')
            txt = ['Mắt ta thấy một đáy rõ ràng và một cú phá đẹp.', 'Nhiều indicator vẽ nhãn swing LÙI VỀ đúng cây nến đáy — nhưng nhãn đó chỉ xuất hiện vài nến sau (LuxAlgo ghi rõ điều này).', 'Nhìn chart lưu, gần như mọi CHoCH đều “rõ ràng”.']
        else:
            ch.level(lowp, lowi, upto - 1, MUTE, 'đáy ứng viên', pos='l', dy=16, dash='3,3')
            ch.candles(cs, upto=upto)
            ch.fog(upto + 0.1, 'chưa biết')
            txt = ['Bên phải đáy chỉ có MỘT nến tăng, rồi nến tiếp theo đã đi thấp hơn đáy.', 'Theo quy tắc fractal 2 nến, cái đáy đó KHÔNG BAO GIỜ được xác nhận là swing. Ở lớp này không có “HL” nào để phá.', 'Câu hỏi đúng lúc này: trạng thái đã khai báo là gì, và mức tham chiếu ĐÃ XÁC NHẬN gần nhất nằm ở đâu?']
        yy = y0 + 70
        for t_ in txt:
            f.t(x + 262, yy, '•', 12, True, c); yy = f.p(x + 274, yy, t_, w - 290, 11.8) + 8
    f.foot('Hai lỗi hindsight phổ biến: (1) chọn swing SAU khi biết giá đi đâu; (2) dùng nhãn indicator đã vẽ lùi về quá khứ như thể nó có sẵn tại thời điểm đó.')
    return f.save()


# ------------------------------------------------------------------ 40 authority
def fig40():
    f = F(40, 'D1-H1-M5-Ai-Duoc-Doi-Gi', 'D1 → H1 → M5: CHoCH ở mỗi khung được quyền thay đổi điều gì?',
          'Bối cảnh chảy từ trên xuống. Một CHoCH ở khung nhỏ KHÔNG có quyền thay đổi kết luận của khung lớn.', h=600)
    y0 = f.top + 4
    rows = [('D1', 'CONTEXT', BOSC, 'D1 CHoCH (protected swing D1 bị đóng nến xuyên)', 'Đặt CÂU HỎI cho daily bias. Bias đổi khi có thêm bằng chứng D1 (G2–G3), không phải ngay lập tức.', 'Đổi entry M5? Không trực tiếp.'),
            ('H1', 'SETUP', CHC, 'H1 CHoCH (protected swing H1)', 'Đổi trạng thái setup: đợt hồi H1 có thể đã kết thúc / setup mới đang hình thành.', 'Đổi daily bias? KHÔNG.'),
            ('M5', 'EXECUTION', DISP, 'M5 CHoCH / MSS tại POI H1', 'Là điều kiện kích hoạt cho mô hình vào lệnh — nếu D1, H1 đã cho phép.', 'Đổi H1 / D1? KHÔNG.')]
    y = y0 + 6
    for k, (tf, role, c, ev, can, cannot) in enumerate(rows):
        f.r(28, y, 944, 118, fill=CARD, stroke=c, sw=1.6, rx=12)
        f.r(28, y, 110, 118, fill=c, stroke=None, rx=12, op=0.12)
        f.t(83, y + 54, tf, 26, True, c, 'middle'); f.t(83, y + 78, role, 11, True, c, 'middle')
        f.t(156, y + 28, 'Sự kiện', 10.5, False, SUB); f.p(156, y + 46, ev, 240, 12.2, INK, bold=True)
        f.t(420, y + 28, 'Được quyền', 10.5, False, SUB); f.p(420, y + 46, can, 320, 12.2, GOOD)
        f.t(760, y + 28, 'KHÔNG được quyền', 10.5, False, SUB); f.p(760, y + 46, cannot, 200, 12.2, BAD)
        if k < 2: f.arrow(83, y + 120, 83, y + 136, SUB, 2.2, size=8)
        y += 138
    f.note(28, y + 2, 944, 'Ngoại lệ duy nhất là khi bạn CHỦ ĐỘNG nghiên cứu mô hình ngược xu hướng — khi đó phải khai báo trước, ghi riêng trong journal và backtest riêng. Không được “đổi luật” giữa lệnh.', WARN, None, 12)
    f.foot('Đồng bộ với RULE-MSS-004 (note 21) và state machine D1–H1–M5 (01c - ICT 2022 Model).')
    return f.save()


ALL = [fig27, fig28, fig29, fig30, fig31, fig32, fig33, fig34, fig35, fig36, fig37, fig38, fig39, fig40]
if __name__ == '__main__':
    sel = sys.argv[1:]
    for fn in ALL:
        if not sel or fn.__name__[3:] in sel:
            print(fn())
