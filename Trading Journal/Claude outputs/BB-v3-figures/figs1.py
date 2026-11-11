# -*- coding: utf-8 -*-
from bbdraw import *

TEAL = '#0D9488'
CONF = ('base', 'fail', 'noretest', 'toconfirm', 'wickretest', 'multi', 'revbefore', 'weakbounce', 'tiny')
TX = {
    False: dict(old='Đáy cũ', mid='Đỉnh giữa', new='Đáy mới (thấp hơn)', ob='OB gốc\n(bearish OB)', bb='BULLISH BREAKER',
                c_ob='nến TĂNG cuối cùng ở đỉnh', dirv='tăng', opp='giảm', below='dưới', above='trên', side='sell-side', side2='buy-side',
                role0='kháng cự', role1='hỗ trợ', stop0='sell stop', who='người bán'),
    True: dict(old='Đỉnh cũ', mid='Đáy giữa', new='Đỉnh mới (cao hơn)', ob='OB gốc\n(bullish OB)', bb='BEARISH BREAKER',
               c_ob='nến GIẢM cuối cùng ở đáy', dirv='giảm', opp='tăng', below='trên', above='dưới', side='buy-side', side2='sell-side',
               role0='hỗ trợ', role1='kháng cự', stop0='buy stop', who='người mua'),
}

def base_chart(f, x, y, w, h, kind='base', flip=False, upto=None, n=None, lo=35, hi=90, zones=True, lv=True, cw=None, small=False, blue=True):
    cs = seq(kind); n = n or len(cs) + 1
    ch = Chart(f, x, y, w, h, lo, hi, n, flip, cw)
    k = len(cs) if upto is None else upto
    if zones and k > HI:
        conf = blue and kind in CONF
        end_ob = min(k - 1, CF - 1) if conf else (min(k - 1, 14) if kind == 'mitig' else k - 1)
        ch.zone(HI, end_ob, Z_LO, Z_HI, OBC, op=0.16)
        if conf and k > CF:
            ch.zone(CF, n - 1, Z_LO, Z_HI, BBC, op=0.13)
        if kind == 'mitig' and k > 15:
            ch.zone(15, n - 1, Z_LO, Z_HI, TEAL, op=0.14)
    ch.candles(cs, upto=upto)
    if lv:
        if k > L1: ch.level(P_L1, L1, min(k - 1, L2 + 1), LIQ, sw=1.1 if small else 1.3)
        if k > HI: ch.level(P_H, HI, min(k - 1, CF), STR, sw=1.1 if small else 1.3)
    return ch, cs

# ------------------------------------------------------------------ 01 ELI5 house
def fig01():
    f = Fig(1, 'ELI5-Ngoi-Nha-Ba-Tang', 'Breaker cho trẻ 5 tuổi: cái trần nhà bị thủng trở thành sàn nhà',
            'Quả bóng là GIÁ. Ngôi nhà có ba tầng. Hãy xem quả bóng làm gì với cái trần của tầng 1.', h=560, tag='ELI5')
    caps = [('Bóng nảy lên và bị TRẦN chặn lại', 'Bóng nảy lên tới trần tầng 1 thì bị chặn, rơi xuống. Cái trần là chỗ bóng “không qua được”.'),
            ('Bóng rơi THỦNG SÀN, xuống hầm', 'Bóng rơi mạnh tới mức thủng cả sàn cũ, lọt xuống hầm. Ai cũng nghĩ: “bóng sẽ rơi mãi”.'),
            ('Bóng bật lên, XUYÊN THỦNG TRẦN', 'Nhưng bóng bật ngược lên rất mạnh, đục thủng cái trần đã từng chặn nó, lên hẳn tầng 2.'),
            ('Trần cũ giờ là SÀN MỚI. Giữ hay thủng?', 'Bóng rơi lại. Tấm trần cũ giờ nằm dưới chân: có thể đỡ bóng… hoặc thủng tiếp. Không ai biết trước.')]
    for k in range(4):
        x = 28 + k * 239; w = 227; y = f.top + 6
        f.card(x, y, w, 424, caps[k][0], num=k + 1)
        hx, hw = x + 46, w - 66; yt = y + 70
        y2, yc, yf, yb = yt, yt + 78, yt + 178, yt + 250   # top of floor2, ceiling slab, floor slab, bottom
        f.ln(hx, y2, hx, yb, '#9CA3AF', 2); f.ln(hx + hw, y2, hx + hw, yb, '#9CA3AF', 2)
        f.ln(hx, y2, hx + hw, y2, '#9CA3AF', 2); f.ln(hx, yb, hx + hw, yb, '#9CA3AF', 2)
        for lab, yy in (('Tầng 2', (y2 + yc) / 2), ('Tầng 1', (yc + 10 + yf) / 2), ('Hầm', (yf + 10 + yb) / 2)):
            f.t(hx - 6, yy + 4, lab, 10.5, False, SUB, 'end')
        ccol = OBC if k < 3 else BBC
        cx = hx + hw * 0.55
        # ceiling slab
        if k < 2:
            f.r(hx, yc, hw, 10, fill=ccol, stroke=None, rx=2)
        else:
            f.r(hx, yc, cx - hx - 11, 10, fill=ccol, stroke=None, rx=2); f.r(cx + 11, yc, hx + hw - cx - 11, 10, fill=ccol, stroke=None, rx=2)
        # floor slab
        if k < 1:
            f.r(hx, yf, hw, 10, fill='#9CA3AF', stroke=None, rx=2)
        else:
            f.r(hx, yf, cx - hx - 11, 10, fill='#9CA3AF', stroke=None, rx=2); f.r(cx + 11, yf, hx + hw - cx - 11, 10, fill='#9CA3AF', stroke=None, rx=2)
        if k < 3: f.t(hx + 4, yc - 5, 'trần tầng 1', 10, True, ccol)
        else: f.t(hx + 4, yc + 23, 'sàn mới =', 10, True, ccol); f.t(hx + 4, yc + 36, 'BREAKER', 10, True, ccol)
        f.t(hx + 4, yf + 22, 'sàn cũ', 10, True, '#6B7280')
        if k == 0:
            f.arrow(cx - 22, yf - 12, cx - 4, yc + 24, UP, 2); f.arrow(cx + 4, yc + 24, cx + 24, yf - 30, DN, 2)
            f.circ(cx, yc + 20, 8, INK); f.t(cx + 14, yc + 30, 'cộp!', 10.5, True, OBC)
        elif k == 1:
            f.arrow(cx, yc + 20, cx, yb - 34, DN, 2); f.circ(cx, yb - 22, 8, INK)
            f.t(cx + 16, yf + 27, 'thủng!', 10.5, True, DN)
        elif k == 2:
            f.arrow(cx, yb - 28, cx, y2 + 30, UP, 2.2); f.circ(cx, y2 + 22, 8, INK)
            f.t(cx + 14, yc + 24, 'thủng!', 10.5, True, UP)
        else:
            f.circ(cx, y2 + 20, 8, INK)
            f.arrow(cx, y2 + 30, cx, yc - 16, STR, 1.8)
            f.curve(cx - 4, yc - 12, cx - 34, yc - 14, cx - 44, y2 + 22, UP, 2, '5,4'); f.t(hx + 5, y2 + 15, 'nảy lên?', 10, True, UP)
            f.arrow(cx, yc - 8, cx, yf - 22, DN, 2, '5,4'); f.t(cx + 9, yc + 52, 'lọt xuống?', 10, True, DN)
        f.p(x + 14, yb + 34, caps[k][1], w - 28, 12.2)
    f.foot('Giới hạn của ví dụ: thị trường không có “tấm trần” vật lý. Thứ chặn hay đỡ giá là LỆNH của con người — ta không nhìn thấy chúng và chúng có thể đã biến mất.')
    return f.save()

# ------------------------------------------------------------------ 02 story on chart
def fig02():
    f = Fig(2, 'Cau-Chuyen-Tren-Chart', 'Câu chuyện ngôi nhà, vẽ lại bằng nến',
            'Cùng một chuỗi sự kiện, đánh số theo đúng thứ tự thời gian. Vùng cam = “trần” (OB gốc). Vùng xanh dương = cái trần ấy sau khi đổi vai (Breaker).', h=600)
    y0 = f.top + 4
    f.card(28, y0, 610, 600 - y0 - 44)
    ch, cs = base_chart(f, 52, y0 + 28, 560, 600 - y0 - 100)
    ch.lab(L1, P_L1, 'sàn cũ = ĐÁY CŨ', dx=-4, dy=15, color=LIQ)
    ch.lab(HI, P_H, 'trần = ĐỈNH GIỮA', dy=-8, color=STR)
    ch.zone(HI, HI, Z_LO, Z_HI, OBC, op=0.0, dash=None, sw=1.6)
    ch.badge(L1, P_L1, 1, LIQ, dy=34); ch.badge(HI, P_H, 2, OBC, dy=-32)
    ch.badge(L2, P_L2, 3, DN, dy=18); ch.badge(CF, 71.5, 4, UP, dy=-20, dx=-16)
    ch.badge(23, 63.6, 5, BBC, dy=0); ch.badge(RT, Z_LO, 6, INK, dy=16)
    ch.lab(L2, P_L2, 'thủng sàn', dx=44, dy=4, color=DN, anchor='start')
    ch.lab(CF, 71.5, 'đóng nến TRÊN trần', dx=-30, dy=-2, color=UP, anchor='end')
    ch.ztext(18, 63.6, 'trần cũ →\nsàn mới', BBC)
    x = 652; y = y0
    f.card(x, y, 320, 600 - y0 - 44, 'Ghép truyện với chart')
    rows = [(1, LIQ, 'Sàn cũ', 'Một cái đáy đã có từ trước (đáy cũ).'),
            (2, OBC, 'Cái trần', 'Nến tăng cuối cùng ở đỉnh, ngay trước khi giá rơi. ICT gọi đây là bearish Order Block.'),
            (3, DN, 'Thủng sàn', 'Giá đi xuống DƯỚI đáy cũ. ICT gọi là chạy stop / lấy sell-side liquidity.'),
            (4, UP, 'Xuyên trần', 'Giá quay lên và ĐÓNG NẾN trên đỉnh giữa. Cái trần đã thất bại.'),
            (5, BBC, 'Trần thành sàn', 'Từ lúc này vùng nến ở ② được gọi là Bullish Breaker.'),
            (6, INK, 'Bóng rơi lại', 'Giá quay về vùng đó. Có thể bật lên, có thể thủng. Phải quan sát, không đoán.')]
    yy = y + 48
    for n, c, a, b in rows:
        f.badge(x + 24, yy - 4, n, c)
        f.t(x + 42, yy, a, 12.5, True, c)
        yy = f.p(x + 42, yy + 17, b, 264, 12) + 9
    f.foot('Sơ đồ dựng, không phải dữ liệu thị trường. Trục dọc là giá (lên = đắt hơn), trục ngang là thời gian (trái → phải).')
    return f.save()

# ------------------------------------------------------------------ 03 six kinds of statements
def fig03():
    f = Fig(3, 'Sau-Loai-Cau-Noi', 'Cùng một Breaker, sáu loại câu nói khác nhau',
            'Lỗi phổ biến nhất: đọc một câu DIỄN GIẢI như thể nó là QUAN SÁT. Mỗi câu trong note đều mang một trong sáu nhãn này.', h=560, tag='CÁCH ĐỌC NOTE')
    rows = [('[QUAN SÁT]', GOOD, 'Ai nhìn chart cũng thấy giống nhau', '“Giá đi xuống dưới đáy cũ, rồi một cây nến đóng cửa phía trên đỉnh giữa.”'),
            ('[ICT]', BBC, 'Cách ICT đặt tên và sử dụng', '“Nến tăng ở đỉnh giữa, sau trình tự đó, được ICT gọi là Bullish Breaker.”'),
            ('[CƠ CHẾ]', FVG, 'Cách lệnh được khớp — có nghiên cứu ủng hộ', '“Lệnh dừng lỗ hay tụ quanh các mức dễ thấy; khi bị kích hoạt chúng trở thành lệnh thị trường.”'),
            ('[DIỄN GIẢI]', WARN, 'Hợp lý, nhưng chart không chứng minh được', '“Những người bán ở vùng này đang lỗ; khi giá quay lại họ mua vào để thoát hòa vốn.”'),
            ('[GIẢ THUYẾT]', LIQ, 'Có thể kiểm chứng, nhưng chưa kiểm chứng', '“Breaker có displacement mạnh sẽ giữ giá tốt hơn Breaker phá yếu.”'),
            ('[BACKTEST REQUIRED]', BAD, 'Chưa được phép coi là lợi thế giao dịch', '“Vào lệnh tại Breaker cho kết quả tốt hơn vào lệnh tại một vùng bất kỳ.”')]
    y = f.top + 8
    for lab, c, what, ex in rows:
        f.r(28, y, 944, 62, fill=CARD, stroke=BORDER, rx=10)
        f.r(28, y, 6, 62, fill=c, stroke=None, rx=3)
        f.pill(46, y + 12, lab, c, 11)
        f.t(46, y + 51, what, 11.5, False, SUB)
        f.p(330, y + 28, ex, 626, 13, INK, italic=True)
        y += 70
    f.foot('Chỉ hai nhãn đầu là chắc chắn. Bốn nhãn sau là thứ ta NGHĨ hoặc ta HY VỌNG — càng xuống dưới càng cần bằng chứng.')
    return f.save()

# ------------------------------------------------------------------ 04 mental model: three links
def fig04():
    f = Fig(4, 'Mental-Model-Ba-Mat-Xich', 'Mental model: Breaker là một CHUỖI ba mắt xích, không phải một hình chữ nhật',
            'Ví dụ Bullish Breaker. Ba mắt xích phải xảy ra đúng thứ tự. Thiếu một mắt xích → gọi bằng tên khác. Hai ô cuối KHÔNG thuộc định nghĩa.', h=600)
    y = f.top + 6; w = 180; gap = 11
    items = [('Mắt xích 1', 'Có một cây nến để gọi tên', 'Nến tăng cuối cùng ở đỉnh giữa — “cái trần”.', OBC, 8, 'Thiếu → không có vùng nào để gọi là Breaker.'),
             ('Mắt xích 2', 'Đáy cũ bị vi phạm', 'Giá đi xuống dưới đáy cũ — “thủng sàn”.', DN, 12, 'Thiếu → đó là Mitigation Block, không phải Breaker.'),
             ('Mắt xích 3', 'Đỉnh giữa bị phá', 'Nến đóng cửa trên đỉnh giữa — “xuyên trần”.', UP, 17, 'Thiếu → cái trần vẫn đang giữ. Chưa có gì đổi vai.'),
             ('Theo dõi', 'Giá có quay lại không?', 'Không bắt buộc. Nhiều Breaker không bao giờ được chạm lại.', BBC, 21, 'Không quay lại → hết hạn. Không đuổi theo.'),
             ('Theo dõi', 'Nếu quay lại: giữ hay thủng?', 'Chỉ lúc này mới bàn đến chuyện vào lệnh.', INK, 24, 'Thủng → Breaker thất bại. Ghi lại như mọi mẫu khác.')]
    for k, (hd, tt, body, c, upto, miss) in enumerate(items):
        x = 28 + k * (w + gap)
        f.r(x, y, w, 446, fill=CARD, stroke=c if k < 3 else BORDER, sw=1.6 if k < 3 else 1.2, rx=11, dash=None if k < 3 else '6,4')
        f.pill(x + 12, y + 12, hd, c, 10.5)
        yy = f.p(x + 12, y + 54, tt, w - 24, 13.5, c, bold=True, lh=1.28)
        ch, cs = base_chart(f, x + 8, y + 96, w - 16, 196, upto=upto, cw=4.4, small=True, lo=37, hi=85)
        if k == 0: ch.zone(HI, HI, Z_LO, Z_HI, OBC, op=0, dash=None, sw=1.6)
        if k == 1: ch.dot(L2, P_L2, DN)
        if k == 2: ch.dot(CF, 71.5, UP)
        if k == 3: ch.fog(21.2, None); f.t(x + w - 24, y + 170, '?', 22, True, SUB, 'middle')
        if k == 4: ch.dot(RT, 63.5, INK)
        yy = f.p(x + 12, y + 318, body, w - 24, 12)
        f.ln(x + 12, y + 380, x + w - 12, y + 380, BORDER, 1)
        f.p(x + 12, y + 400, miss, w - 24, 11.5, SUB)
        if k < 4:
            f.arrow(x + w + 1, y + 194, x + w + gap - 1, y + 194, STR, 2, size=6)
    f.r(28, y + 458, 562, 30, fill=BBC, stroke=None, rx=8, op=0.10); f.t(309, y + 478, 'ĐỊNH NGHĨA — ba sự kiện nhìn thấy được trên chart', 12, True, BBC, 'middle')
    f.r(601, y + 458, 371, 30, fill='#6B7280', stroke=None, rx=8, op=0.10); f.t(786, y + 478, 'THEO DÕI — chưa xảy ra, không được giả định', 12, True, '#4B5563', 'middle')
    return f.save()

# ------------------------------------------------------------------ 05 candle & swing
def fig05():
    f = Fig(5, 'Nen-Va-Swing', 'Viên gạch đầu tiên: cây nến và điểm xoay (swing)',
            'Mọi thuật ngữ phía sau đều xây từ hai thứ này. Nến tăng = đóng cửa cao hơn mở cửa (up-close). Nến giảm = đóng cửa thấp hơn mở cửa (down-close).', h=600, tag='NỀN TẢNG')
    y = f.top + 6
    f.card(28, y, 460, 430, 'Một cây nến kể bốn con số')
    for k, (cx, up) in enumerate(((120, True), (330, False))):
        col = UP if up else DN
        top, bot, hi, lo = y + 130, y + 300, y + 80, y + 350
        f.ln(cx, hi, cx, lo, col, 2.5); f.r(cx - 24, top, 48, bot - top, fill=col, stroke=None, rx=3)
        f.t(cx, y + 60, 'Nến TĂNG (up-close)' if up else 'Nến GIẢM (down-close)', 12.5, True, col, 'middle')
        for lab, yy in (('cao nhất (high)', hi), ('đóng cửa (close)' if up else 'mở cửa (open)', top), ('mở cửa (open)' if up else 'đóng cửa (close)', bot), ('thấp nhất (low)', lo)):
            f.ln(cx + 28, yy, cx + 44, yy, SUB, 1); f.t(cx + 48, yy + 4, lab, 11, False, INK)
        f.t(cx - 30, (top + bot) / 2 + 4, 'thân', 11, True, col, 'end'); f.t(cx - 8, hi + 26, 'râu', 11, True, col, 'end')
    f.p(42, y + 384, 'Thân = quãng giữa mở cửa và đóng cửa. Râu = phần giá đã tới nhưng không ở lại. Râu rất quan trọng trong bài này: “chạm” khác với “đóng cửa qua”.', 432, 12, SUB)
    f.card(512, y, 460, 430, 'Swing = chỗ giá quay đầu')
    def tri(x0, pts, col):
        for i, (o, h, l, c) in enumerate(pts):
            x = x0 + i * 36; cc = UP if c >= o else DN
            f.ln(x, yb - h * 3.1, x, yb - l * 3.1, cc, 2); yy1, yy2 = sorted((yb - o * 3.1, yb - c * 3.1))
            f.r(x - 10, yy1, 20, yy2 - yy1, fill=cc, stroke=None, rx=2)
    yb = y + 372
    hi_pts = [(30, 44, 28, 42), (42, 60, 40, 56), (56, 80, 52, 60), (60, 64, 44, 46), (46, 50, 30, 34)]
    lo_pts = [(72, 76, 58, 60), (60, 62, 42, 46), (46, 50, 22, 42), (42, 60, 40, 58), (58, 72, 54, 70)]
    tri(548, hi_pts, UP); tri(786, lo_pts, DN)
    f.circ(620, yb - 80 * 3.1, 5, STR); f.t(620, yb - 80 * 3.1 - 12, 'SWING HIGH', 11.5, True, STR, 'middle')
    f.circ(858, yb - 22 * 3.1, 5, STR); f.t(858, yb - 22 * 3.1 + 22, 'SWING LOW', 11.5, True, STR, 'middle')
    f.t(620, y + 62, 'Đỉnh: nến giữa cao hơn hai bên', 12, True, INK, 'middle'); f.t(858, y + 62, 'Đáy: nến giữa thấp hơn hai bên', 12, True, INK, 'middle')
    f.p(526, y + 384, 'Giống ngọn đồi và thung lũng. Chỉ biết đó là đỉnh SAU KHI nến bên phải đã đóng — luôn chậm một nhịp. Đây là mầm của hindsight.', 432, 12, SUB)
    f.foot('Trong note này: “đáy cũ”, “đỉnh giữa”, “đáy mới” đều là các swing. Breaker được định nghĩa bằng thứ tự các swing đó bị vượt qua.')
    return f.save()

def zig(f, x, y, w, h, pts, color=INK, sw=2.2, lo=0, hi=100):
    out = [(x + px / 100.0 * w, y + h - (py - lo) / float(hi - lo) * h) for px, py in pts]
    f.poly(out, color, sw); return out

# ------------------------------------------------------------------ 06 structure BOS vs MSS
def fig06():
    f = Fig(6, 'Cau-Truc-BOS-MSS', 'Cấu trúc thị trường: bậc thang đi lên, bậc thang đi xuống, và hai kiểu “phá”',
            'HH = đỉnh cao hơn, HL = đáy cao hơn, LH = đỉnh thấp hơn, LL = đáy thấp hơn. BOS = phá THEO hướng đang đi. MSS = phá NGƯỢC hướng đang đi.', h=580, tag='NỀN TẢNG')
    y = f.top + 6
    f.card(28, y, 460, 420, 'BOS — đi tiếp con đường cũ', tcolor=UP)
    pts = [(4, 14), (22, 46), (34, 30), (54, 66), (66, 50), (90, 92)]
    o = zig(f, 48, y + 50, 420, 300, pts, UP)
    for (px, py), lab, dy in zip(o, ['đáy', 'HH', 'HL', 'HH', 'HL', 'HH'], [16, -9, 16, -9, 16, -9]):
        f.circ(px, py, 3.5, UP); f.t(px, py + dy, lab, 11, True, INK, 'middle', halo=True)
    f.ln(o[1][0], o[1][1], o[3][0] - 34, o[1][1], STR, 1.2, '5,4'); f.pill(o[1][0] + 42, o[1][1] - 24, 'BOS', UP, 10.5)
    f.ln(o[3][0], o[3][1], o[5][0] - 34, o[3][1], STR, 1.2, '5,4'); f.pill(o[3][0] + 42, o[3][1] - 24, 'BOS', UP, 10.5)
    f.p(42, y + 372, 'Mỗi lần giá vượt đỉnh cũ theo hướng đang đi, cấu trúc tăng được “gia hạn”. Trẻ con: leo thêm một bậc thang.', 432, 12, SUB)
    f.card(512, y, 460, 420, 'MSS — bậc thang bị gãy', tcolor=DN)
    pts = [(4, 20), (22, 56), (34, 40), (54, 84), (66, 62), (76, 74), (94, 30)]
    o = zig(f, 532, y + 50, 420, 300, pts[:5], UP); o2 = zig(f, 532, y + 50, 420, 300, pts[4:], DN); o = o + o2[1:]
    for (px, py), lab, dy in zip(o, ['đáy', 'HH', 'HL', 'HH', 'HL gần nhất', 'LH', ''], [16, -9, 16, -9, 16, -9, 0]):
        f.circ(px, py, 3.5, STR)
        if lab: f.t(px, py + dy, lab, 11, True, INK, 'middle', halo=True)
    f.ln(o[4][0], o[4][1], o[6][0] + 6, o[4][1], DN, 1.4, '5,4'); f.pill(o[5][0] + 30, o[4][1] + 6, 'MSS', DN, 10.5)
    f.p(526, y + 372, 'Giá không lập đỉnh cao hơn nữa (LH), rồi đóng cửa DƯỚI đáy cao hơn gần nhất. Chuỗi “đỉnh cao hơn, đáy cao hơn” đã gãy.', 432, 12, SUB)
    f.foot('Liên hệ Breaker: sự kiện “đóng nến qua đỉnh giữa / đáy giữa” chính là một MSS trên khung đang xét. Gọi nó là BOS hay MSS tuỳ bạn đang so với xu hướng nào (§15).')
    return f.save()

OBSEQ = mk(60, [56, 52, 48.5, 45, 52, 60, 65, 68, 66, 62, 57, 53.5, 57, 63, 69, 73], {3: {'l': 43.5, 'h': 49}, 4: {'l': 44.6}, 11: {'l': 47.5}})

# ------------------------------------------------------------------ 07 order block
def fig07():
    f = Fig(7, 'Order-Block-La-Gi', 'Order Block (OB): cây nến NGƯỢC màu cuối cùng trước một cú chạy mạnh',
            'Bullish OB = nến GIẢM cuối cùng trước khi giá tăng mạnh. Bearish OB = nến TĂNG cuối cùng trước khi giá giảm mạnh. Hai hình là ảnh gương của nhau.', h=590, tag='NỀN TẢNG')
    y = f.top + 6
    for k, flip in enumerate((False, True)):
        x = 28 + k * 484
        f.card(x, y, 460, 430, 'Bullish Order Block — vùng có thể ĐỠ giá' if not flip else 'Bearish Order Block — vùng có thể CHẶN giá', tcolor=UP if not flip else DN)
        ch = Chart(f, x + 30, y + 56, 400, 280, 38, 78, 17, flip)
        ch.zone(3, 15, 43.5, 49, OBC, op=0.15)
        ch.candles(OBSEQ)
        ch.zone(3, 3, 43.5, 49, OBC, op=0, dash=None, sw=1.8)
        ch.lab(3, 43.5, 'nến %s cuối cùng' % ('giảm' if not flip else 'tăng'), dy=16, color=OBC, dx=14, anchor='end')
        ch.lab(5.2, 62, 'cú chạy mạnh\n(displacement)', dx=-10, dy=-4, color=STR, anchor='end')
        ch.lab(11, 43.5, 'giá quay lại, vùng %s' % ('đỡ' if not flip else 'chặn'), dx=-8, dy=16, color=OBC, anchor='start')
        f.p(x + 14, y + 366, ('Trẻ con: chỗ quả bóng “lấy đà” trước khi bật lên. ' if not flip else 'Trẻ con: chỗ quả bóng “khựng lại” trước khi rơi mạnh. ') +
            '[ICT] diễn giải rằng tại đây có lệnh lớn. [QUAN SÁT] chỉ là: sau cây nến này giá chạy rất nhanh.', 432, 12, SUB)
    f.foot('Không phải mọi nến ngược màu đều là OB đáng quan tâm (xem note 25 và 55). Với Breaker, ta chỉ cần OB nằm NGAY TẠI một swing: đỉnh giữa hoặc đáy giữa.')
    return f.save()

# ------------------------------------------------------------------ 08 three fates of an OB
def fig08():
    f = Fig(8, 'OB-Ba-Ket-Cuc', 'Khi giá quay lại một bearish Order Block: ba kết cục',
            'Chỉ kết cục C mới là “OB thất bại”. Và ngay cả C cũng CHƯA đủ để gọi là Breaker (còn thiếu mắt xích “đáy cũ bị vi phạm”).', h=590)
    y = f.top + 6
    head = [58, 62, 66, 62, 57, 53, 50, 54, 59]
    ov = {2: {'h': 68, 'l': 61.5}, 3: {'h': 66.5}}
    vs = [('A · Vùng GIỮ', GOOD, head + [63, 65, 60, 55, 50, 46], {**ov, 10: {'h': 66.4}}, 'Giá chui vào vùng rồi bị đẩy ra. OB làm đúng vai “chặn”. Không có gì thất bại.'),
          ('B · Râu xuyên, thân không qua', WARN, head + [63, 65.5, 61, 56, 51, 47], {**ov, 10: {'h': 70.5}}, 'Râu nến vượt lên trên vùng nhưng nến ĐÓNG CỬA quay lại bên trong. Đây là một cú quét (sweep), chưa phải thất bại.'),
          ('C · Nến đóng cửa xuyên qua', BAD, head + [63, 67, 71, 74, 72, 76], ov, 'Thân nến đóng hẳn phía trên vùng và giá ở lại đó. Vai “chặn” đã hết. OB này thất bại.')]
    for k, (tt, c, cl, o, body) in enumerate(vs):
        x = 28 + k * 319
        f.card(x, y, 306, 440, tt, tcolor=c)
        ch = Chart(f, x + 18, y + 52, 270, 270, 42, 80, 16)
        ch.zone(2, 15, 61.5, 68, OBC, 'bearish OB', pos='ar', op=0.15)
        ch.candles(mk(54, cl, o))
        if k == 1: ch.lab(10, 70.5, 'chỉ là râu', dy=-7, color=WARN)
        if k == 2: ch.lab(11, 71, 'đóng cửa\ntrên vùng', dx=-12, dy=-12, color=BAD, anchor='end')
        f.p(x + 14, y + 356, body, 278, 12.2)
    f.foot('Quy ước dùng trong note: râu qua vùng = chưa thất bại. Thân nến đóng qua mép xa và giá không quay lại ngay = thất bại. Đây là quy ước LÀM VIỆC, không phải lời ICT.')
    return f.save()

# ------------------------------------------------------------------ 09 liquidity
def fig09():
    f = Fig(9, 'Liquidity-Nam-O-Dau', 'Liquidity: những “túi lệnh chờ” nằm sau các đỉnh và đáy dễ thấy',
            'Phía TRÊN đỉnh cũ thường có lệnh mua chờ (buy stop) = buy-side liquidity. Phía DƯỚI đáy cũ thường có lệnh bán chờ (sell stop) = sell-side liquidity.', h=580, tag='NỀN TẢNG')
    y = f.top + 6
    f.card(28, y, 600, 430)
    pts = [(3, 44), (14, 80), (24, 56), (36, 81), (48, 22), (58, 46), (70, 21), (82, 58), (95, 44)]
    o = zig(f, 50, y + 70, 556, 300, pts, STR, 2.2)
    def stack(x1, x2, yy, up, col, lab):
        for j in range(4):
            f.ln(x1, yy + (-1 if up else 1) * (8 + j * 6), x2, yy + (-1 if up else 1) * (8 + j * 6), col, 2, None, 0.9 - j * 0.18)
        f.t((x1 + x2) / 2, yy + (-40 if up else 50), lab, 11.5, True, col, 'middle')
    f.ln(o[1][0] - 10, o[1][1], o[3][0] + 14, o[1][1], LIQ, 1, '4,3')
    stack(o[1][0] - 10, o[3][0] + 14, o[1][1], True, LIQ, 'BUY-SIDE LIQUIDITY — lệnh mua chờ')
    f.ln(o[4][0] - 10, o[4][1], o[6][0] + 14, o[4][1], '#DB2777', 1, '4,3')
    stack(o[4][0] - 10, o[6][0] + 14, o[4][1], False, '#DB2777', 'SELL-SIDE LIQUIDITY — lệnh bán chờ')
    f.t((o[1][0] + o[3][0]) / 2, o[1][1] + 96, 'hai đỉnh bằng nhau (EQH)', 10.5, True, STR, 'middle'); f.t((o[4][0] + o[6][0]) / 2, o[4][1] - 92, 'hai đáy bằng nhau (EQL)', 10.5, True, STR, 'middle')
    x = 642
    f.card(x, y, 330, 430, 'Ai để lệnh ở đó? (cho trẻ 5 tuổi)')
    yy = y + 52
    for hd, body, c in (('Người đang BÁN', 'sợ giá lên quá đỉnh → đặt lệnh “nếu lên tới đây thì mua lại giúp tôi” (stop loss).', LIQ),
                        ('Người chờ MUA đuổi', 'đặt lệnh “nếu vượt đỉnh thì mua giúp tôi” (breakout).', LIQ),
                        ('Dưới đáy thì ngược lại', 'người đang mua đặt lệnh dừng lỗ bán; người chờ bán đuổi đặt lệnh bán.', '#DB2777')):
        f.t(x + 14, yy, hd, 12.5, True, c); yy = f.p(x + 14, yy + 17, body, 302, 12) + 8
    yy = f.note(x + 14, yy + 4, 302, 'Khi giá chạm tới, các lệnh chờ đó biến thành lệnh mua/bán NGAY (market order). Giá vì thế hay “giật” thêm một đoạn qua mức đó.', FVG, '[CƠ CHẾ]')
    f.note(x + 14, yy + 8, 302, 'Chart nến KHÔNG cho thấy các lệnh này. Ta chỉ đoán chúng ở đó vì mức ấy dễ thấy.', WARN, '[GIỚI HẠN]')
    f.foot('Liên hệ Breaker: bước “đáy cũ bị vi phạm” = giá đi vào túi sell-side. Bước “đỉnh giữa bị phá” = giá đi vào túi buy-side nằm trên đỉnh giữa.')
    return f.save()

# ------------------------------------------------------------------ 10 sweep vs structural break
def fig10():
    f = Fig(10, 'Sweep-vs-Structural-Break', 'Liquidity sweep ≠ structural break: thò chân qua vạch rồi rút về, hay bước hẳn sang?',
            'Cả hai đều “vượt qua một mức”. Khác nhau ở chỗ cây nến ĐÓNG CỬA ở đâu và giá Ở LẠI bên nào sau đó.', h=580)
    y = f.top + 6
    a = mk(60, [56, 52, 55, 59, 57, 54, 51.5, 56, 61, 65, 68], {1: {'l': 50}, 6: {'l': 46.5}})
    b = mk(60, [56, 52, 55, 59, 57, 54, 48.5, 46, 47.5, 44, 41], {1: {'l': 50}, 8: {'h': 49.6}})
    for k, (cs, tt, c, body) in enumerate(((a, 'SWEEP — thò chân qua vạch rồi rút về', LIQ, 'Râu nến đi xuống dưới đáy cũ, nhưng nến đóng cửa quay lại PHÍA TRÊN. Giá không ở lại bên dưới. Túi lệnh dưới đáy đã bị lấy, cấu trúc chưa đổi.'),
                                          (b, 'STRUCTURAL BREAK — bước hẳn sang bên kia', DN, 'Thân nến đóng cửa PHÍA DƯỚI đáy cũ và các nến sau tiếp tục ở dưới. Lần quay lại vạch cũ bị từ chối. Cấu trúc đã đổi.'))):
        x = 28 + k * 484
        f.card(x, y, 460, 430, tt, tcolor=c)
        ch = Chart(f, x + 30, y + 56, 400, 270, 38, 72, 12)
        ch.candles(cs)
        ch.level(50, 1, 11, STR, 'đáy cũ', pos='r')
        if k == 0:
            ch.lab(6, 46.5, 'râu qua, thân đóng lại bên trên', dy=16, color=LIQ)
        else:
            ch.lab(6, 48.5, 'thân đóng\nbên dưới', dx=-12, dy=14, color=DN, anchor='end'); ch.lab(8, 49.6, 'quay lại,\nbị từ chối', dx=14, dy=-22, color=DN, anchor='start')
        f.p(x + 14, y + 358, body, 432, 12.2)
    f.foot('Trong một Bullish Breaker có CẢ HAI: đáy cũ bị vi phạm (ICT gọi là chạy stop), sau đó đỉnh giữa bị PHÁ bằng thân nến (structural break). Hai sự kiện, hai vai khác nhau.')
    return f.save()

# ------------------------------------------------------------------ 11 / 12 anatomy
def anatomy(num, flip):
    t = TX[flip]
    f = Fig(num, ('Bearish' if flip else 'Bullish') + '-Breaker-Giai-Phau', 'Giải phẫu một %s Breaker — sáu sự kiện theo đúng thứ tự' % ('Bearish' if flip else 'Bullish'),
            'Đánh số theo thứ tự trader BIẾT được sự kiện. ①–④ là định nghĩa (nhìn thấy được). ⑤ là cái tên. ⑥ là điều có thể xảy ra, không chắc.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 44
    f.card(28, y0, 600, H)
    ch, cs = base_chart(f, 50, y0 + 34, 556, H - 70, flip=flip)
    ch.zone(HI, HI, Z_LO, Z_HI, OBC, op=0, dash=None, sw=1.8)
    ch.lab(L1, P_L1, t['old'].upper(), dx=-2, dy=15, color=LIQ); ch.lab(HI, P_H, t['mid'].upper(), dy=-8, color=STR)
    ch.lab(L2, P_L2, t['new'].upper(), dx=2, dy=15, color=DN)
    ch.badge(L1, P_L1, 1, LIQ, dy=36); ch.badge(HI, P_H, 2, OBC, dy=-34, dx=0); ch.badge(L2, P_L2, 3, DN, dy=36)
    ch.badge(CF, 71.5, 4, UP if not flip else DN, dy=-20, dx=-18); ch.badge(23, 63.6, 5, BBC, dy=0); ch.badge(RT, Z_LO, 6, INK, dy=16)
    ch.ztext(11, 63.6, t['ob'].replace('\n', ' '), OBC)
    ch.ztext(18, 63.6, t['bb'].replace(' ', '\n'), BBC)
    ch.lab(CF, 71.5, 'nến đóng cửa\n%s %s' % (t['above'], t['mid'].lower()), dx=-32, dy=-4, color=UP if not flip else DN, anchor='end')
    x = 642
    f.card(x, y0, 330, H, 'Từng sự kiện nghĩa là gì')
    c4 = UP if not flip else DN
    rows = [(1, LIQ, t['old'] + ' hình thành', 'Một swing có trước. %s nó có thể có lệnh chờ (%s liquidity).' % (('Bên dưới' if not flip else 'Bên trên'), t['side'])),
            (2, OBC, t['mid'] + ' + OB gốc', 'Giá hồi, tạo %s. %s chính là OB gốc.' % (t['mid'].lower(), t['c_ob'].capitalize())),
            (3, DN if not flip else UP, t['old'] + ' bị vi phạm', 'Giá đi xuống %s %s. ICT: “run on stops”. Cùng lúc tạo %s.' % (t['below'], t['old'].lower(), t['new'].split(' (')[0].lower()) if not flip else
             'Giá đi lên trên %s. ICT: “run on stops”. Cùng lúc tạo %s.' % (t['old'].lower(), t['new'].split(' (')[0].lower())),
            (4, c4, t['mid'] + ' bị phá', 'Một thân nến đóng cửa %s %s. OB gốc thất bại; cấu trúc khung này đổi (MSS).' % (t['above'], t['mid'].lower())),
            (5, BBC, 'Đổi tên: ' + t['bb'].title(), 'Vùng nến ở ② được theo dõi với vai ngược lại: từ %s thành %s.' % (t['role0'], t['role1'])),
            (6, INK, 'Retest (nếu có)', 'Giá quay lại vùng. Lúc này mới xuống khung nhỏ tìm bằng chứng. Không có bằng chứng → không có lệnh.')]
    yy = y0 + 50
    for n, c, a, b in rows:
        f.badge(x + 24, yy - 4, n, c); f.t(x + 42, yy, a, 12.5, True, c)
        yy = f.p(x + 42, yy + 17, b, 272, 11.8) + 8
    f.foot('[ICT] dùng chữ “violated / break through”; yêu cầu “thân nến đóng cửa” ở ④ là quy ước làm việc của note này để tránh nhầm với một cú quét bằng râu.')
    return f.save()

# ------------------------------------------------------------------ 13 which candle
def fig13():
    f = Fig(13, 'Nen-Nao-La-Breaker', 'Nến nào là Breaker? Ba cách đánh dấu đang lưu hành (ví dụ Bullish)',
            'Cùng một chuỗi giá, ba người vẽ ba vùng khác nhau. Note này dùng cách A — khớp với lời ICT trong bài giảng Month 04. Cách C là gọi sai tên.', h=626)
    y = f.top + 6
    vs = [('A · Nến TĂNG ở đỉnh giữa', GOOD, 'Dùng trong note này', 'Đúng lời ICT: “up-close candle in the most recent swing high”. Cũng chính là bearish OB đã thất bại.'),
          ('B · Các nến GIẢM của nhịp rơi', WARN, 'Biến thể — ghi rõ nếu dùng', 'Một số thư viện và blog đánh dấu các nến giảm mở đầu nhịp rơi. Vùng thường chồng lên A nhưng rộng và thấp hơn.'),
          ('C · Nến GIẢM ở đáy mới', BAD, 'Sai tên', 'Đây là bullish Order Block của chính nhịp tăng mới — một vùng hợp lệ để theo dõi, nhưng KHÔNG phải Breaker.')]
    for k, (tt, c, st, body) in enumerate(vs):
        x = 28 + k * 319
        f.card(x, y, 306, 470, tt, tcolor=c)
        f.pill(x + 14, y + 40, st, c, 10)
        cs = seq('base'); ch = Chart(f, x + 16, y + 76, 274, 260, 35, 90, 25, cw=6.5)
        if k == 0: ch.zone(HI, 24, Z_LO, Z_HI, BBC, 'vùng A', pos='ur', op=0.16)
        if k == 1: ch.zone(HI + 1, 24, 55, 65.8, WARN, 'vùng B', pos='ur', op=0.16)
        if k == 2: ch.zone(L2 - 1, 24, 41, 50.6, BAD, 'vùng C', pos='ur', op=0.13)
        ch.candles(cs)
        if k == 0: ch.zone(HI, HI, Z_LO, Z_HI, BBC, op=0, dash=None, sw=1.8)
        if k == 1: ch.zone(HI + 1, HI + 2, 55, 65.8, WARN, op=0, dash=None, sw=1.8)
        if k == 2: ch.zone(L2 - 1, L2, 41, 50.6, BAD, op=0, dash=None, sw=1.8)
        ch.level(P_H, HI, CF, STR, sw=1); ch.level(P_L1, L1, L2 + 1, LIQ, sw=1)
        f.p(x + 14, y + 372, body, 278, 12.2)
    f.foot('Vì sao phải chọn MỘT cách và ghi tên nó: đổi cách đánh dấu là đổi vị trí vào lệnh và đổi mức dừng lỗ. Trộn hai cách trong cùng một bộ backtest thì kết quả vô nghĩa.')
    return f.save()

# ------------------------------------------------------------------ 14 zone boundary
def fig14():
    f = Fig(14, 'Bien-Vung-Mep-Gan-Mep-Xa', 'Vẽ vùng Breaker: lấy cả râu hay chỉ thân? Mép nào là “mép gần”?',
            'ICT trong bài giảng nói ông dùng “the entire range” (cả râu). Cộng đồng có nơi chỉ lấy thân. Điều quan trọng hơn: mép gần và mép xa ĐỔI CHỖ khi vùng đổi vai.', h=600)
    y = f.top + 6
    f.card(28, y, 300, 450, 'Phóng to cây nến ở đỉnh giữa')
    cx = 110; hi, top, bot, lo = y + 90, y + 150, y + 330, y + 380
    f.ln(cx, hi, cx, lo, UP, 3); f.r(cx - 30, top, 60, bot - top, fill=UP, stroke=None, rx=3)
    f.r(cx - 52, hi, 104, lo - hi, fill=BBC, stroke=BBC, sw=1.4, rx=3, dash='5,3', op=0.08)
    f.r(cx - 42, top, 84, bot - top, fill='none', stroke=OBC, sw=1.6, rx=3)
    f.t(cx + 60, hi + 4, 'cả râu (full range)', 11, True, BBC); f.t(cx + 60, hi + 19, '← mặc định của note', 10.5, False, BBC)
    f.t(cx + 60, (top + bot) / 2, 'chỉ thân', 11, True, OBC); f.t(cx + 60, (top + bot) / 2 + 15, '(body)', 10.5, False, OBC)
    f.p(42, y + 410, 'Chọn một cách, ghi lại, không đổi sau khi thấy kết quả.', 272, 12, SUB)
    for k, (tt, c, fromabove) in enumerate((('TRƯỚC: bearish OB — giá đến từ DƯỚI', OBC, False), ('SAU: Bullish Breaker — giá đến từ TRÊN', BBC, True))):
        x = 342 + k * 320
        f.card(x, y, 310, 450, tt, tcolor=c)
        zy1, zy2 = y + 190, y + 270
        f.r(x + 40, zy1, 230, zy2 - zy1, fill=c, stroke=c, sw=1.4, rx=3, dash='5,3', op=0.14)
        f.t(x + 155, (zy1 + zy2) / 2 + 4, 'vùng', 12, True, c, 'middle')
        near, far = (zy2, zy1) if not fromabove else (zy1, zy2)
        f.t(x + 276, near + (16 if not fromabove else -7), 'MÉP GẦN', 11, True, GOOD, 'end'); f.t(x + 276, far + (-7 if not fromabove else 16), 'MÉP XA', 11, True, BAD, 'end')
        if not fromabove:
            f.arrow(x + 90, y + 400, x + 90, zy2 + 6, STR, 2); f.t(x + 100, y + 392, 'giá đi lên chạm vùng', 11, False, STR)
            f.t(x + 44, zy1 - 26, 'nến đóng trên mép xa', 11, True, BAD); f.t(x + 44, zy1 - 12, '= OB thất bại', 11, False, BAD)
        else:
            f.arrow(x + 90, y + 70, x + 90, zy1 - 6, STR, 2); f.t(x + 100, y + 84, 'giá đi xuống chạm vùng', 11, False, STR)
            f.t(x + 44, zy2 + 30, 'nến đóng dưới mép xa', 11, True, BAD); f.t(x + 44, zy2 + 44, '= Breaker thất bại', 11, False, BAD)
    f.foot('Lỗi hay gặp: vùng đã đổi vai nhưng vẫn đặt mức “sai” ở mép cũ. Sau khi thành Bullish Breaker, mức cho thấy vùng thất bại là mép DƯỚI, không còn là mép trên.')
    return f.save()

if __name__ == '__main__':
    for fn in (fig01, fig02, fig03, fig04, fig05, fig06, fig07, fig08, fig09, fig10, lambda: anatomy(11, False), lambda: anatomy(12, True), fig13, fig14):
        print(fn())
