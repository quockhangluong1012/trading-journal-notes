# -*- coding: utf-8 -*-
from bbdraw import *
from figs1 import base_chart, TX, zig, OBSEQ, TEAL
from figs2 import mini, nums, X2, X3, X4, W2, W3, W4, MIDLEG

PINK = '#DB2777'

def rows(f, x, y, items, w, size=11.8, gap=8, tsize=12.3):
    for n, c, a, b in items:
        if n is not None: f.badge(x + 10, y - 4, n, c)
        xx = x + (28 if n is not None else 0)
        f.t(xx, y, a, tsize, True, c)
        y = f.p(xx, y + size * 1.4, b, w - (28 if n is not None else 0), size) + gap
    return y

# ------------------------------------------------------------------ 31 two liquidity events
def fig31():
    f = Fig(31, 'Hai-Su-Kien-Liquidity', 'Trong một Bullish Breaker có HAI sự kiện liquidity, không phải một',
            'Sự kiện 1 lấy túi lệnh NGƯỢC hướng sắp đi (dưới đáy cũ). Sự kiện 2 lấy túi lệnh CÙNG hướng mới (trên đỉnh giữa). Chỉ sự kiện 1 thì chưa có Breaker.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 44
    f.card(28, y0, 600, H)
    ch, cs = base_chart(f, 46, y0 + 30, 564, H - 62, upto=19, lo=33, hi=88)
    for pv in (45.6, 44.4, 43.2): ch.level(pv, 3, 12, PINK, sw=2, dash=None)
    for pv in (68.4, 69.6, 70.8): ch.level(pv, 7, 16, LIQ, sw=2, dash=None)
    ch.lab(6, 43.2, 'túi SELL-SIDE\ndưới đáy cũ', dx=-6, dy=14, color=PINK, anchor='end')
    ch.lab(10.5, 70.8, 'túi BUY-SIDE trên đỉnh giữa', dy=-7, color=LIQ)
    ch.badge(L2, P_L2, 1, PINK, dy=18); ch.badge(CF, 71.5, 2, LIQ, dy=-22, dx=14)
    ch.lab(L1, P_L1, 'ĐÁY CŨ', dy=-8, dx=-10, color=STR); ch.lab(HI, P_H, 'ĐỈNH GIỮA', dy=-8, dx=-34, color=STR)
    x = 642
    f.card(x, y0, 330, H, 'Hai sự kiện, hai vai')
    yy = rows(f, x + 14, y0 + 52, [
        (1, PINK, 'Lấy sell-side dưới đáy cũ', 'Giá đi xuống dưới đáy cũ. ICT gọi là “run on stops”, và coi đây là một phần của định nghĩa Breaker.'),
        (2, LIQ, 'Lấy buy-side trên đỉnh giữa', 'Giá đóng cửa trên đỉnh giữa. Đây vừa là cú phá cấu trúc, vừa là lúc lệnh dừng của người bán bị kích hoạt.')], 302)
    yy = f.note(x + 14, yy + 4, 302, 'Sự kiện 1 một mình chỉ là một cú quét. Phải có sự kiện 2 thì trình tự mới hoàn tất.', BBC, 'Liquidity sweep ≠ Breaker', size=11.8)
    yy = f.note(x + 14, yy + 8, 302, 'Không có sự kiện 1 (đáy cũ còn nguyên) mà có sự kiện 2 → ICT gọi là Mitigation Block.', TEAL, 'Thiếu sự kiện 1', size=11.8)
    f.note(x + 14, yy + 8, 302, 'Túi lệnh vẽ bằng các vạch chỉ là minh hoạ. Trên chart nến ta không thấy chúng; ta chỉ thấy giá đã đi qua mức đó.', WARN, '[GIỚI HẠN]', size=11.8)
    f.foot('Chất lượng của sự kiện 1 thay đổi rất nhiều: đáy cũ có thể là đáy của cả ngày, hoặc chỉ là một gợn nhỏ. Định nghĩa không phân biệt; việc lọc chất lượng là của bạn.')
    return f.save()

# ------------------------------------------------------------------ 32 after a sweep: three futures
def fig32():
    f = Fig(32, 'Sau-Sweep-Ba-Tuong-Lai', 'Không phải cú quét nào cũng sinh ra Breaker: ba tương lai sau khi đáy cũ thủng',
            'Mười hai nến đầu giống hệt nhau ở cả ba hình. Tại thời điểm đáy cũ vừa bị vi phạm, không có cách nào biết mình đang ở hình nào.', h=600)
    y = f.top + 6
    vs = [('A · Giá quay lên, phá đỉnh giữa', 'toconfirm', GOOD, 'Trình tự hoàn tất → Breaker. Chỉ gọi tên được SAU nến đóng trên đỉnh giữa.', 'BREAKER'),
          ('B · Giá rơi tiếp', 'obholds', BAD, 'Giá hồi vào vùng OB rồi rơi tiếp. “Cú quét” hoá ra là cú phá thật. Bearish OB thắng.', 'KHÔNG CÓ BREAKER'),
          ('C · Giá đi ngang', 'side', '#6B7280', 'Giá lình xình quanh đáy cũ. Không phá được đỉnh giữa. Ứng viên hết hạn.', 'KHÔNG CÓ BREAKER')]
    for k, (tt, kind, c, cap, st) in enumerate(vs):
        ch, cs = mini(f, X3[k], y, W3, 448, tt, kind=kind, tcolor=c, cap=cap, lo=34, hi=82, n=24, capsize=12.2, cw=6.6, extra=38, blue=True)
        f.pill(X3[k] + W3 / 2, y + 412, st, c, 11, anchor='middle')
        x12 = ch.x + 12 * ch.step
        f.ln(x12, ch.y, x12, ch.y + ch.h, STR, 1, '3,3'); f.t(x12 + 4, ch.y + 10, 'từ đây khác nhau', 9.5, False, SUB)
    f.foot('Bài học: “đã quét đáy” không phải tín hiệu mua. Nó chỉ mở ra KHẢ NĂNG có Breaker. Mắt xích thứ ba (đóng nến trên đỉnh giữa) mới là thứ phân biệt A với B và C.')
    return f.save()

# ------------------------------------------------------------------ 33 formation / quality / entry
def fig33():
    f = Fig(33, 'Formation-Chat-Luong-Entry', 'MSS, BOS, displacement, FVG đứng ở đâu? Ba ngăn kéo khác nhau',
            'Lỗi phổ biến: thấy các yếu tố hay đi cùng nhau rồi biến tất cả thành “điều kiện bắt buộc”. Hãy cất mỗi thứ vào đúng ngăn.', h=500, tag='KHUNG PHÂN LOẠI')
    y = f.top + 6
    cols = [('NGĂN 1 · Điều kiện HÌNH THÀNH', BBC, 'Thiếu một thứ → không gọi là Breaker',
             [('Nến tại đỉnh/đáy giữa', 'ICT: up-close / down-close candle ở swing gần nhất.'),
              ('Cực trị cũ bị vi phạm', 'ICT: “prior to an old low/high being violated”.'),
              ('Swing giữa bị phá', 'ICT: “break through that swing high to confirm”. Trên khung đó, sự kiện này là một MSS.')]),
            ('NGĂN 2 · Bằng chứng CHẤT LƯỢNG', WARN, 'Có thì tốt hơn (giả thuyết), thiếu vẫn là Breaker',
             [('Thân nến ĐÓNG qua swing', 'Quy ước của note. ICT không nói rõ thân hay râu.'),
              ('Displacement', 'Cú phá nhanh, thân dài. ICT chỉ tả là “explosive”.'),
              ('FVG trong nhịp phá', 'Không có trong bài giảng Breaker. Chồng lên Breaker → cộng đồng gọi “Unicorn”.'),
              ('Túi liquidity lớn, cùng hướng khung lớn', 'Là bộ lọc của bạn, không phải định nghĩa.')]),
            ('NGĂN 3 · Tín hiệu VÀO LỆNH', GOOD, 'Chỉ xét khi giá ĐÃ quay lại vùng, trên khung nhỏ',
             [('Giá chạm vùng Breaker', 'Mới là “đến nơi”, chưa phải tín hiệu.'),
              ('Sweep nhỏ + MSS khung nhỏ', 'Bằng chứng rằng vùng đang được bảo vệ.'),
              ('Displacement + FVG khung nhỏ', 'Nơi đặt lệnh và nơi đặt mức dừng.')])]
    for k, (hd, c, sub, items) in enumerate(cols):
        x = X3[k]
        f.r(x, y, W3, 344, fill=CARD, stroke=c, sw=1.6, rx=11)
        f.r(x, y, W3, 58, fill=c, stroke=None, rx=11, op=0.10)
        f.t(x + 14, y + 25, hd, 13, True, c); f.t(x + 14, y + 45, sub, 11.2, False, INK)
        yy = y + 84
        for a, b in items:
            f.circ(x + 20, yy - 4, 4, c); f.t(x + 32, yy, a, 12.3, True, INK)
            yy = f.p(x + 32, yy + 17, b, W3 - 46, 11.6, SUB) + 10
        if k < 2: f.arrow(x + W3 + 1, y + 172, x + W3 + 12, y + 172, STR, 2, size=6)
    f.foot('BOS và MSS: cùng một cú phá có thể mang hai tên. So với nhịp vừa tạo cực trị mới thì nó là MSS; nếu khung lớn vốn đang đi cùng hướng thì trên khung lớn nó là BOS (tiếp diễn).')
    return f.save()

# ------------------------------------------------------------------ 34 strong vs weak break
def fig34():
    f = Fig(34, 'Pha-Manh-vs-Pha-Yeu', 'Cùng “đóng nến trên đỉnh giữa”, hai cú phá rất khác nhau',
            'Cả hai đều đủ ba mắt xích nên đều là Breaker theo định nghĩa. Khác biệt nằm ở CÁCH giá đi qua — đây là thứ chữ “displacement” muốn mô tả.', h=620)
    y = f.top + 6
    for k, (kind, tt, c, pts) in enumerate((('base', 'Phá DỨT KHOÁT (có displacement)', GOOD, ['Ít nến, thân dài, râu ngắn', 'Nến đóng cửa xa phía trên đỉnh giữa', 'Thường để lại FVG trong nhịp', 'Giá không quay lại ngay']),
                                            ('weak', 'Phá LÊ LẾT (không có displacement)', WARN, ['Nhiều nến nhỏ chồng lên nhau', 'Nến chỉ nhích qua đỉnh giữa', 'Không để lại khoảng trống nào', 'Vừa qua đã quay lại bên dưới']))):
        x = X2[k]
        f.card(x, y, W2, 470, tt, tcolor=c)
        ch, cs = base_chart(f, x + 16, y + 48, W2 - 32, 250, kind, upto=19 if k == 0 else None, n=32, lo=36, hi=80, cw=7, blue=(k == 0))
        ch.lab(HI, P_H, 'ĐỈNH GIỮA', dy=-8, color=STR)
        if k == 1: ch.level(P_H, HI, 30, STR, sw=1)
        yy = y + 336
        for pt in pts:
            f.circ(x + 22, yy - 4, 3, c); f.t(x + 34, yy, pt, 12, False, INK); yy += 22
        f.pill(x + W2 - 16, y + 428, 'Breaker hợp lệ' if k == 0 else 'Breaker hợp lệ — chất lượng thấp?', c, 10.5, anchor='end')
    f.foot('“Phá dứt khoát thì vùng giữ tốt hơn” là một [GIẢ THUYẾT] hợp lý, chưa phải dữ kiện. Ghi cách phá vào nhật ký cho MỌI mẫu rồi so sánh hai nhóm.')
    return f.save()

# ------------------------------------------------------------------ 35 breaker + FVG
UNI = mk(62, HEAD + [51, 56, 68, 72, 75, 72, 67.5, 72, 77], dict(HOV, **{}) if False else {**HOV, 13: {'h': 57}, 14: {'l': 55.6}, 15: {'l': 63}, 18: {'l': 61.4}})

def fig35():
    f = Fig(35, 'Breaker-va-FVG-Unicorn', 'Breaker và FVG: hai vùng khác nhau, đôi khi chồng lên nhau',
            'Breaker = một cây nến cũ ở đỉnh giữa. FVG = khoảng trống do ba nến của nhịp phá để lại. Khi hai vùng có phần chung, cộng đồng ICT gọi là “Unicorn”.', h=630)
    y = f.top + 6
    for k in range(2):
        x = X2[k]
        f.card(x, y, W2, 452, 'A · FVG CHỒNG lên Breaker (“Unicorn”)' if k == 0 else 'B · FVG nằm RIÊNG, bên dưới Breaker', tcolor=LIQ if k == 0 else STR)
        cs = UNI if k == 0 else seq('base')
        ch = Chart(f, x + 16, y + 48, W2 - 32, 270, 36, 88, 25, cw=9)
        cf = 14 if k == 0 else CF
        g_lo, g_hi = (57, 63) if k == 0 else (cs[12][1], cs[14][2])
        ch.zone(HI, cf - 1, Z_LO, Z_HI, OBC, op=0.16); ch.zone(cf, 24, Z_LO, Z_HI, BBC, op=0.13)
        ch.zone(14 if k == 0 else 13, 24, g_lo, g_hi, FVG, op=0.16)
        if k == 0: ch.zone(14, 24, Z_LO, 63, LIQ, op=0.22, dash=None, sw=1.6)
        ch.candles(cs)
        ch.lab(23.4, Z_HI, 'Breaker', dy=-6, color=BBC, anchor='end'); ch.lab(23.4, g_lo, 'FVG', dy=14, color=FVG, anchor='end')
        if k == 0: ch.ztext(21.2, 61.6, 'phần chung', LIQ, 10)
        f.p(x + 16, y + 350, 'Giá hồi về gặp cả hai cùng lúc. Hai lý do cho cùng một chỗ — nhưng cả hai đều sinh ra từ CÙNG một nhịp tăng, nên không phải hai bằng chứng độc lập.' if k == 0 else
            'Giá hồi về gặp Breaker trước (nông hơn), FVG sau (sâu hơn). Hai ý tưởng riêng, hai mức vào khác nhau, hai mức “sai” khác nhau.', W2 - 32, 12.2)
    f.foot('FVG không phải điều kiện của Breaker: bài giảng Breaker của ICT không nhắc tới nó. “Unicorn giữ tốt hơn Breaker thường” là [GIẢ THUYẾT] → [BACKTEST REQUIRED].')
    return f.save()

# ------------------------------------------------------------------ 36 breaker among other PD arrays
def fig36():
    f = Fig(36, 'Breaker-Giua-Cac-PD-Array', 'Một nhịp tăng, bốn vùng: Breaker đứng ở đâu so với FVG, Order Block, Rejection Block',
            'Khi giá hồi về, nó gặp các vùng theo thứ tự từ nông tới sâu. Bốn vùng này sinh ra từ cùng MỘT nhịp tăng — đừng đếm chúng như bốn phiếu bầu.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 44
    f.card(28, y0, 600, H)
    cs = seq('base'); ch = Chart(f, 46, y0 + 30, 564, H - 62, 33, 92, 25)
    ch.zone(CF, 24, Z_LO, Z_HI, BBC, op=0.14); ch.zone(13, 24, cs[12][1], cs[14][2], FVG, op=0.16)
    ch.zone(11, 24, 44, 46.7, OBC, op=0.2); ch.zone(11, 24, 41, 44, LIQ, op=0.16)
    ch.candles(cs)
    ch.level(88, 14, 24, PINK, 'buy-side liquidity (mục tiêu có thể có)', pos='r')
    for i, (pv, lab, c) in enumerate(((63.6, 'Breaker', BBC), (55.3, 'FVG', FVG), (45.3, 'Order Block', OBC), (42.4, 'Rejection Block', LIQ))):
        ch.badge(23.4, pv, i + 1, c, dy=0); ch.ztext(22.4, pv, lab, c, anchor='end')
    ch.arr(17.5, 74, 19.5, 68, STR, dash='4,3'); ch.lab(17.5, 76, 'giá hồi về', dy=-2, color=STR)
    x = 642
    f.card(x, y0, 330, H, 'Thứ tự giá gặp khi hồi về')
    yy = rows(f, x + 14, y0 + 52, [
        (1, BBC, 'Breaker — nông nhất', 'Nến tăng ở đỉnh giữa đã bị phá. Hồi ít nhất là tới đây.'),
        (2, FVG, 'FVG', 'Khoảng trống của nhịp phá. Sâu hơn Breaker (trong ví dụ này).'),
        (3, OBC, 'Order Block', 'Nến giảm cuối cùng trước nhịp tăng — nằm ở đáy mới.'),
        (4, LIQ, 'Rejection Block', 'Phần râu dưới của đáy mới. Sâu nhất; qua nữa là ý tưởng sai.')], 302, size=11.6)
    f.note(x + 14, yy + 2, 302, 'Vùng nông cho giá vào sớm nhưng mức dừng xa. Vùng sâu cho mức dừng gần nhưng hay lỡ lệnh. Không vùng nào “đúng hơn” — đó là đánh đổi.', STR, 'Chọn vùng nào?', size=11.6)
    f.foot('Nếu hai vùng “nói” khác nhau (Breaker bị thủng nhưng FVG bên dưới giữ): ý tưởng tăng chưa sai, nhưng vùng Breaker đã sai. Ghi riêng từng vùng.')
    return f.save()

# ------------------------------------------------------------------ 37 premium / discount
def fig37():
    f = Fig(37, 'Breaker-Premium-Discount', 'Breaker nằm ở nửa trên hay nửa dưới? Tuỳ bạn đo bằng khoảng giá nào',
            'Premium = nửa trên của một khoảng giá (đắt). Discount = nửa dưới (rẻ). Đây là thông tin về VỊ TRÍ — nó không tạo ra và cũng không xoá bỏ một Breaker.', h=640)
    y = f.top + 6
    vs = [('A · Cú phá đi XA', [(4, 62), (16, 47), (32, 67), (50, 41), (78, 92), (92, 74)], 92, GOOD, 'Breaker nằm ở nửa DƯỚI của nhịp tăng mới. Mua tại đây còn nhiều chỗ để chạy.'),
          ('B · Cú phá chỉ NHÍCH qua', [(4, 62), (16, 47), (32, 67), (50, 41), (78, 72), (92, 66)], 72, WARN, 'Breaker nằm ở nửa TRÊN của nhịp tăng mới. Vẫn là Breaker, nhưng mua tại đây thì gần đỉnh.'),
          ('C · Đo bằng khoảng giá KHUNG LỚN', [(2, 14), (26, 92), (46, 30), (54, 24), (62, 34), (72, 20), (88, 42), (96, 36)], 40, BBC, 'Cùng một Breaker, nhưng đặt trong khoảng giá lớn của khung D1, nó nằm sâu trong discount.')]
    for k, (tt, pts, top, c, cap) in enumerate(vs):
        x = X3[k]
        f.card(x, y, W3, 450, tt, tcolor=c)
        lo, hi = (36, 96) if k < 2 else (8, 98)
        cx, cy, cw_, chh = x + 16, y + 50, W3 - 78, 290
        Y = lambda p: cy + chh - (p - lo) / float(hi - lo) * chh
        rl, rh = (41, top) if k < 2 else (14, 92)
        bx = x + W3 - 52
        f.r(bx, Y(rh), 22, Y((rl + rh) / 2) - Y(rh), fill=BAD, stroke=None, rx=3, op=0.16); f.r(bx, Y((rl + rh) / 2), 22, Y(rl) - Y((rl + rh) / 2), fill=GOOD, stroke=None, rx=3, op=0.16)
        f.ln(bx - 4, Y((rl + rh) / 2), bx + 26, Y((rl + rh) / 2), STR, 1.4, '4,3')
        f.t(bx + 11, Y(rh) - 6, 'P', 11, True, BAD, 'middle'); f.t(bx + 11, Y(rl) + 15, 'D', 11, True, GOOD, 'middle'); f.t(bx + 28, Y((rl + rh) / 2) + 4, '50%', 9.5, False, SUB)
        zl, zh = (60.3, 67) if k < 2 else (30.5, 34)
        zx = cx if k < 2 else cx + cw_ * 0.6
        f.r(zx, Y(zh), cx + cw_ + 10 - zx, Y(zl) - Y(zh), fill=BBC, stroke=BBC, sw=1.2, rx=2, dash='5,3', op=0.16)
        if k == 2:
            f.ln(cx, Y(92), bx + 22, Y(92), GRAY, 1, '3,3'); f.ln(cx, Y(14), bx + 22, Y(14), GRAY, 1, '3,3')
            f.t(cx + cw_ * 0.42, Y(92) - 5, 'đỉnh D1', 10, True, SUB); f.t(cx + 22, Y(14) + 14, 'đáy D1', 10, True, SUB)
        o = zig(f, cx, cy, cw_, chh, pts, STR, 2.2, lo=lo, hi=hi)
        f.t(zx + 4, Y(zh) - 5, 'Breaker', 10.5, True, BBC, halo=True)
        f.p(x + 14, y + 374, cap, W3 - 28, 12.2)
    f.foot('“Mua ở discount, bán ở premium” là một gợi ý về vị trí, không phải luật. Một Bullish Breaker ở premium không bị “loại” — nó chỉ kém hấp dẫn hơn về khoảng chạy còn lại.')
    return f.save()

# ------------------------------------------------------------------ 38 lifecycle
def fig38():
    f = Fig(38, 'Vong-Doi-Breaker', 'Vòng đời của một Breaker: năm trạng thái, ba lối ra giữa đường, ba kết cục',
            'Đọc từ trái sang phải. Ô nét liền = trạng thái. Ô nét đứt = lối ra (vùng bị bỏ). Mỗi mũi tên là MỘT sự kiện nhìn thấy được trên chart.', h=590, tag='VÒNG ĐỜI')
    y = f.top + 22; w = 172; gap = 21
    st = [('OB gốc', OBC, 'Nến tại đỉnh/đáy giữa đã được đánh dấu.'),
          ('ỨNG VIÊN', WARN, 'Cực trị cũ đã bị vi phạm. Chưa có cú phá.'),
          ('ĐÃ XÁC NHẬN', BBC, 'Thân nến đóng qua swing giữa. Vùng được gọi là Breaker.'),
          ('CHỜ RETEST', BBC, 'Giá đã rời vùng. Chưa quay lại.'),
          ('ĐANG RETEST', INK, 'Giá chạm vùng. Xuống khung nhỏ tìm bằng chứng.')]
    ev = ['cực trị cũ\nbị vi phạm', 'nến đóng\nqua swing', 'giá rời\nvùng', 'giá quay\nlại']
    for k, (nm, c, body) in enumerate(st):
        x = 28 + k * (w + gap)
        f.r(x, y, w, 104, fill=CARD, stroke=c, sw=1.8, rx=10); f.r(x, y, w, 30, fill=c, stroke=None, rx=10, op=0.12)
        f.t(x + w / 2, y + 20, nm, 12.5, True, c, 'middle'); f.p(x + 10, y + 50, body, w - 20, 11.3)
        if k < 4:
            f.arrow(x + w + 2, y + 52, x + w + gap - 2, y + 52, STR, 2, size=6)
            for j, l in enumerate(ev[k].split('\n')): f.t(x + w + gap / 2, y - 16 + j * 12, l, 9.6, True, STR, 'middle')
    ex = [(0, 'OB giữ', 'Giá bị đẩy ra khỏi vùng. Không có Breaker; OB vẫn là OB.'),
          (1, 'Hết hạn', 'Giá không phá được swing giữa. Ứng viên bị bỏ.'),
          (3, 'Hết hạn / cũ', 'Giá không quay lại; hoặc mục tiêu đã đạt; hoặc cấu trúc ngược đã hình thành phía trên.')]
    for k, nm, body in ex:
        x = 28 + k * (w + gap)
        f.arrow(x + w / 2, y + 106, x + w / 2, y + 146, GRAY, 1.6, '4,3', size=6)
        f.r(x, y + 148, w, 104, fill='#F9FAFB', stroke=GRAY, sw=1.3, rx=10, dash='5,4')
        f.t(x + w / 2, y + 168, nm, 12, True, '#6B7280', 'middle'); f.p(x + 10, y + 188, body, w - 20, 11.2, SUB)
    x5 = 28 + 4 * (w + gap)
    out = [('GIỮ', GOOD, 'Không đóng qua mép xa; giá đi tiếp hướng mới.'), ('THỦNG', BAD, 'Thân nến đóng qua mép xa và ở lại. Breaker thất bại.'), ('CHƯA RÕ', WARN, 'Đóng trong vùng, lình xình. Chờ, không đoán.')]
    f.arrow(x5 + w / 2, y + 106, x5 + w / 2, y + 286, STR, 1.8, size=6)
    for j, (nm, c, body) in enumerate(out):
        x = 28 + (2 + j) * (w + gap)
        f.r(x, y + 290, w, 96, fill=CARD, stroke=c, sw=1.8, rx=10); f.t(x + w / 2, y + 311, nm, 12.5, True, c, 'middle'); f.p(x + 10, y + 331, body, w - 20, 11.3)
    f.ln(28 + 2 * (w + gap) + w / 2, y + 286, x5 + w / 2, y + 286, STR, 1.8)
    for j in range(2): f.arrow(28 + (2 + j) * (w + gap) + w / 2, y + 286, 28 + (2 + j) * (w + gap) + w / 2, y + 289, STR, 1.8, size=5)
    f.note(28, y + 290, 2 * w + gap - 8, 'Một Breaker “cũ” (stale) không sai — nó chỉ không còn đáng chờ: đã quá xa, đã bị chạm nhiều lần, hoặc mục tiêu mà nó phục vụ đã đạt.', STR, 'Cũ ≠ Vô hiệu', size=11.4)
    f.foot('Vùng chỉ được VẼ như một Breaker từ trạng thái ĐÃ XÁC NHẬN. Lệnh chỉ được XÉT từ trạng thái ĐANG RETEST. Hai mốc này cách nhau có khi vài nến, có khi vài ngày.')
    return f.save()

# ------------------------------------------------------------------ 39 four separate events
def fig39():
    f = Fig(39, 'Bon-Su-Kien-Tach-Biet', 'Bốn sự kiện tách biệt: hình thành ≠ xác nhận ≠ retest ≠ vào lệnh',
            'Gộp bốn mốc này làm một là nguồn gốc của phần lớn lỗi hindsight. Mỗi mốc trả lời một câu hỏi khác và cho phép một việc khác.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 60
    f.card(28, y0, 944, H)
    ch, cs = base_chart(f, 46, y0 + 60, 908, H - 200, lo=35, hi=90, cw=15)
    marks = [(10.5, WARN, '1 · HÌNH THÀNH (ứng viên)', 'Cực trị cũ vừa bị vi phạm. Trình tự đang dở dang.', 'Được: ghi chú, đánh dấu mức cần bị phá.', 0, 11),
             (16.5, BBC, '2 · XÁC NHẬN', 'Nến đóng cửa qua swing giữa. Breaker có tên.', 'Được: vẽ vùng, khoá biên, đặt cảnh báo.', 11, 17),
             (20.5, INK, '3 · RETEST', 'Giá chạm vùng. Mới là “đến nơi”.', 'Được: xuống khung nhỏ quan sát.', 17, 21),
             (22.0, GOOD, '4 · VÀO LỆNH (nếu có)', 'Khung nhỏ cho sweep + MSS + FVG.', 'Được: đặt lệnh theo kế hoạch.', 21, 25)]
    by = y0 + H - 128
    for k, (xi, c, nm, what, can, a, b) in enumerate(marks):
        xx = ch.x + xi * ch.step
        f.ln(xx, ch.y - 30, xx, by - 6, c, 1.4, '5,4'); f.badge(xx, ch.y - 36, k + 1, c)
        bx = 42 + k * 232; bw = 222
        f.r(bx, by, bw, 114, fill=CARD, stroke=c, sw=1.5, rx=9); f.t(bx + 10, by + 20, nm, 11.8, True, c)
        yy = f.p(bx + 10, by + 40, what, bw - 20, 11.2); f.p(bx + 10, yy + 4, can, bw - 20, 11.2, c, bold=True)
    f.foot('Giữa mốc 2 và mốc 3 có thể không có gì xảy ra (giá không quay lại). Giữa mốc 3 và mốc 4 cũng vậy (giá chạm vùng rồi xuyên qua, không cho tín hiệu). Cả hai đều bình thường.')
    return f.save()

# ------------------------------------------------------------------ 40 twelve situations
def fig40():
    f = Fig(40, 'Muoi-Hai-Tinh-Huong', 'Mười hai tình huống hay gặp: hợp lệ, tiềm năng, thất bại, hay không phải Breaker?',
            'Ví dụ phía mua (Bullish). Nhãn màu: xanh lá = Breaker hợp lệ · cam = chưa kết luận · đỏ = Breaker thất bại · xám = không phải Breaker.', h=912)
    y0 = f.top + 6
    G = '#6B7280'
    it = [('1 · OB bị xuyên, cấu trúc chưa phá', None, None, G, 'KHÔNG PHẢI BREAKER'),
          ('2 · OB bị xuyên VÀ cấu trúc bị phá', 'toconfirm', None, GOOD, 'BREAKER ĐÃ XÁC NHẬN'),
          ('3 · Phá cấu trúc, không displacement', 'weak', None, WARN, 'HỢP LỆ · CHẤT LƯỢNG THẤP?'),
          ('4 · Có displacement, không retest', 'noretest', None, G, 'HỢP LỆ · HẾT HẠN'),
          ('5 · Retest rồi xuyên thẳng', 'fail', None, BAD, 'BREAKER THẤT BẠI'),
          ('6 · Chỉ râu chạm vào vùng', 'wickretest', None, GOOD, 'RETEST NÔNG · CÒN HỢP LỆ'),
          ('7 · Nến đóng cửa TRONG vùng', 'base', 21, WARN, 'ĐANG BỊ THỬ · CHƯA RÕ'),
          ('8 · Nến đóng cửa XUYÊN qua vùng', 'fail', 23, BAD, 'VÔ HIỆU'),
          ('9 · Retest nhiều lần', 'multi', None, WARN, 'HỢP LỆ · ĐANG CŨ DẦN?'),
          ('10 · Cấu trúc đảo trước khi retest', 'revbefore', None, WARN, 'CẦN ĐÁNH GIÁ LẠI'),
          ('11 · Bật yếu rồi đi ngược', 'weakbounce', None, BAD, 'BREAKER THẤT BẠI'),
          ('12 · Nằm giữa vùng đi ngang', 'chop', None, G, 'NHIỄU · BỎ QUA')]
    for k, (tt, kind, upto, c, st) in enumerate(it):
        x = X4[k % 4]; y = y0 + (k // 4) * 256
        f.card(x, y, W4, 246, tt, tcolor=INK, tsize=12)
        cx, cy, cw_, chh = x + 10, y + 40, W4 - 20, 160
        if kind is None:
            ch = Chart(f, cx, cy, cw_, chh, 48, 88, 17, cw=6); ch.zone(2, 14, 71.6, 75.2, G, op=0.16); ch.candles(MIDLEG); ch.level(82, 0, 14, STR, sw=1)
        elif kind == 'chop':
            ch = Chart(f, cx, cy, cw_, chh, 46, 70, 27, cw=4.6); ch.candles(seq('chop'))
            ch.level(63.2, 0, 25, STR, sw=1); ch.level(52.6, 0, 25, STR, sw=1)
        else:
            ch, cs = base_chart(f, cx, cy, cw_, chh, kind, upto=upto, n=32 if kind == 'weak' else 30, lo=35, hi=90 if kind != 'weak' else 80, cw=4.4, small=True)
        f.pill(x + W4 / 2, y + 214, st, c, 10, anchor='middle')
    f.foot('Tình huống 3, 9, 10 mang dấu hỏi vì “chất lượng thấp”, “cũ dần”, “cần đánh giá lại” là NHẬN ĐỊNH của khung nghiên cứu này, không phải quy tắc của ICT. Chi tiết từng tình huống: bảng ở §19.')
    return f.save()

# ------------------------------------------------------------------ 41 selection framework
def fig41():
    f = Fig(41, 'Khung-Chon-Breaker', 'Chart nào cũng đầy vùng thất bại. Năm câu hỏi để chọn Breaker đáng chờ',
            'Không chấm điểm, không cộng trừ. Đi từ trên xuống: câu nào trả lời “không” thì dừng ở đó. Qua đủ năm câu mới đáng đặt cảnh báo.', h=700, tag='KHUNG QUYẾT ĐỊNH')
    y = f.top + 8
    qs = [('Có cùng hướng với bối cảnh khung lớn không?', 'D1/H1: bias, DOL. Bullish Breaker khi khung lớn đang hướng lên.', 'BỎ QUA', 'Ngược khung lớn: chỉ ghi chú, không lập kế hoạch.', BAD),
          ('Swing bị phá có quan trọng không?', 'Đỉnh/đáy được bảo vệ của khung đó — hay chỉ là một gợn nhỏ bên trong?', 'HẠ ƯU TIÊN', 'Gợn nhỏ: Breaker “nội bộ”, dễ bị cuốn trôi.', WARN),
          ('Trước cú phá có lấy một túi liquidity đáng kể không?', 'Đỉnh/đáy ngày, phiên, đỉnh/đáy bằng nhau… hay chỉ một đáy vô danh?', 'HẠ ƯU TIÊN', 'Túi nhỏ: đủ định nghĩa, thiếu câu chuyện.', WARN),
          ('Cú phá có dứt khoát không?', 'Thân dài, ít nến, đóng xa swing. Có thể kèm FVG.', 'HẠ ƯU TIÊN', 'Phá lê lết: hay bị kéo ngược lại.', WARN),
          ('Vùng còn mới và còn chỗ chạy không?', 'Chưa bị chạm; mục tiêu chưa đạt; khoảng tới mục tiêu đủ lớn so với mức dừng.', 'BỎ QUA', 'Đã chạm nhiều lần / hết chỗ chạy: hết giá trị.', BAD)]
    for k, (q, hint, verdict, why, c) in enumerate(qs):
        yy = y + k * 96
        f.r(28, yy, 560, 80, fill=CARD, stroke=BBC, sw=1.5, rx=10); f.badge(52, yy + 25, k + 1, BBC, 11, 12)
        f.t(74, yy + 30, q, 13.2, True, INK); f.p(74, yy + 52, hint, 500, 11.6, SUB)
        f.arrow(590, yy + 40, 640, yy + 40, c, 2, size=7); f.t(615, yy + 32, 'không', 10.5, True, c, 'middle')
        f.r(644, yy + 4, 328, 72, fill=c, stroke=c, sw=1.2, rx=10, op=0.07); f.t(658, yy + 28, verdict, 12, True, c); f.p(658, yy + 48, why, 300, 11.4)
        if k < 4:
            f.arrow(308, yy + 81, 308, yy + 95, GOOD, 2, size=6); f.t(320, yy + 93, 'có', 10.5, True, GOOD)
    yy = y + 5 * 96
    f.arrow(308, yy - 15, 308, yy - 1, GOOD, 2, size=6)
    f.r(28, yy, 944, 58, fill=GOOD, stroke=GOOD, sw=1.5, rx=10, op=0.08)
    f.t(48, yy + 25, 'BREAKER ĐÁNG CHỜ', 13.5, True, GOOD); f.t(48, yy + 45, 'Đặt cảnh báo ở mép gần. Khi giá tới: xuống khung nhỏ tìm sweep → MSS → displacement → FVG. Không có chuỗi đó thì không có lệnh.', 11.8, False, INK)
    f.foot('“Hạ ưu tiên” không phải “loại”: bạn vẫn có thể theo dõi, nhưng ghi rõ điểm yếu để sau này biết nhóm nào thật sự kém hơn. Toàn bộ khung này là [GIẢ THUYẾT] cần backtest.')
    return f.save()

# ------------------------------------------------------------------ 42 six market conditions
def fig42():
    f = Fig(42, 'Sau-Boi-Canh-Thi-Truong', 'Cùng một hình Breaker, sáu bối cảnh thị trường khác nhau',
            'Đường xám = giá. Ô xanh dương = vùng Breaker. Hình dạng tại chỗ có thể giống nhau; ý nghĩa thì phụ thuộc vào thứ đang diễn ra xung quanh.', h=760)
    y0 = f.top + 6
    it = [('A · Trong xu hướng TĂNG', GOOD, [(2, 20), (16, 46), (26, 34), (40, 60), (52, 30), (72, 78), (82, 60), (96, 90)], (40, 96, 57, 62), 'Nhịp hồi quét đáy cao hơn rồi phá đỉnh giữa. Bullish Breaker THUẬN xu hướng: bối cảnh ủng hộ.'),
          ('B · Trong xu hướng GIẢM', GOOD, [(2, 86), (16, 60), (26, 72), (40, 46), (52, 76), (72, 28), (82, 46), (96, 16)], (40, 96, 44, 49), 'Ảnh gương: nhịp hồi quét đỉnh thấp hơn rồi phá đáy giữa. Bearish Breaker THUẬN xu hướng.'),
          ('C · Trong vùng ĐI NGANG', '#6B7280', [(2, 50), (12, 62), (22, 44), (34, 64), (44, 42), (56, 66), (66, 46), (78, 62), (88, 48), (96, 58)], (34, 96, 60, 64), 'Đỉnh và đáy bị quét qua lại liên tục. “Breaker” mọc khắp nơi và hay bị xuyên. Phần lớn là nhiễu.'),
          ('D · Lúc ĐẢO CHIỀU xu hướng', WARN, [(2, 88), (14, 64), (24, 76), (38, 50), (50, 62), (62, 34), (80, 72), (88, 61), (96, 80)], (50, 96, 59, 64), 'Breaker đầu tiên NGƯỢC xu hướng cũ. Có thể là đảo chiều thật, có thể chỉ là nhịp hồi sâu. Cần khung lớn ủng hộ.'),
          ('E · Sau một cú PHÁ GIẢ (false breakout)', LIQ, [(2, 40), (14, 60), (26, 46), (40, 60), (52, 48), (64, 70), (76, 38), (86, 47), (96, 26)], (52, 96, 46, 50), 'Giá vượt đỉnh vùng rồi rơi lại: đó là mắt xích 2 của một Bearish Breaker. Phá giả phía này = quét cho phía kia.'),
          ('F · Chỉ có cú QUÉT, không có cú phá', BAD, [(2, 56), (14, 40), (28, 62), (46, 32), (60, 56), (74, 44), (86, 54), (96, 40)], None, 'Đáy cũ bị quét, giá bật lên nhưng KHÔNG vượt được đỉnh giữa. Không có Breaker nào ở đây.')]
    for k, (tt, c, pts, z, cap) in enumerate(it):
        x = X3[k % 3]; y = y0 + (k // 3) * 316
        f.card(x, y, W3, 306, tt, tcolor=c)
        cx, cy, cw_, chh = x + 16, y + 44, W3 - 32, 172
        if z:
            f.r(cx + z[0] / 100 * cw_, cy + chh - z[3] / 100 * chh, (z[1] - z[0]) / 100 * cw_, (z[3] - z[2]) / 100 * chh, fill=BBC, stroke=BBC, sw=1.2, rx=2, dash='5,3', op=0.16)
        if k == 5:
            yy = cy + chh - 62 / 100 * chh; f.ln(cx + 0.28 * cw_, yy, cx + cw_, yy, STR, 1.1, '5,4'); f.t(cx + cw_, yy - 5, 'đỉnh giữa — chưa bị phá', 10, True, STR, 'end')
        if k == 2:
            for pv in (66, 42): f.ln(cx, cy + chh - pv / 100 * chh, cx + cw_, cy + chh - pv / 100 * chh, GRAY, 1, '3,3')
        zig(f, cx, cy, cw_, chh, pts, '#374151', 2.2)
        f.p(x + 14, y + 246, cap, W3 - 28, 11.8)
    f.foot('Thuận xu hướng (A, B) là bối cảnh mà khung ICT kỳ vọng Breaker hoạt động tốt nhất; C và F là nơi nhận diện máy móc gây hại nhiều nhất. Mọi kỳ vọng ở đây là [GIẢ THUYẾT].')
    return f.save()

M5SEQ = mk(80, [77, 74.5, 72, 73.5, 70.5, 68, 66, 68.5, 66.5, 64, 67, 71.5, 74, 72, 70, 73.5, 77, 80, 83],
           {3: {'h': 74.6}, 6: {'l': 65}, 7: {'h': 69.5}, 9: {'l': 62.5}, 10: {'h': 67.6}, 12: {'l': 70.8}, 14: {'l': 69}})

# ------------------------------------------------------------------ 43 D1-H1-M5 nested
def fig43():
    f = Fig(43, 'D1-H1-M5-Long-Nhau', 'Ba khung, ba câu hỏi: D1 = bối cảnh · H1 = setup · M5 = thực thi',
            'Mỗi khung là một lần “phóng to” vào khung trước. Breaker H1 chỉ có nghĩa khi nằm TRONG vùng D1 đang chờ; chuỗi M5 chỉ có nghĩa khi xảy ra TẠI Breaker H1.', h=612, tag='ĐA KHUNG')
    y = f.top + 6
    # D1
    x = X3[0]; f.card(x, y, W3, 444, 'D1 — Đi đâu? Đang ở đâu?', tcolor=STR)
    cx, cy, cw_, chh = x + 16, y + 48, W3 - 32, 250
    Y = lambda p: cy + chh - p / 100.0 * chh
    f.ln(cx, Y(92), cx + cw_, Y(92), PINK, 1.3, '5,4'); f.t(cx + cw_, Y(92) - 5, 'DOL: đỉnh cũ D1 (buy-side)', 10.5, True, PINK, 'end')
    f.r(cx, Y(40), cw_, Y(24) - Y(40), fill=OBC, stroke=OBC, sw=1.2, rx=2, dash='5,3', op=0.14); f.t(cx + cw_ * 0.44, Y(32) + 4, 'vùng D1 đang chờ', 10.5, True, OBC, 'middle', halo=True)
    o = zig(f, cx, cy, cw_, chh, [(2, 10), (22, 60), (34, 44), (56, 88), (80, 34)], '#374151', 2.4)
    f.r(o[4][0] - 26, o[4][1] - 26, 52, 52, fill='none', stroke=BBC, sw=2, rx=6, dash='4,3'); f.t(o[4][0], o[4][1] + 44, 'phóng to → H1', 10.5, True, BBC, 'middle')
    rows(f, x + 14, y + 336, [(None, STR, 'Trả lời:', 'Bias đang hướng lên. Mục tiêu là đỉnh cũ. Giá đã hồi về nửa dưới và chạm vùng D1. → Cho phép tìm setup MUA.')], W3 - 28)
    # H1
    x = X3[1]; f.card(x, y, W3, 444, 'H1 — Trong vùng D1 có setup không?', tcolor=BBC)
    ch, cs = base_chart(f, x + 12, y + 48, W3 - 24, 250, 'base', upto=21, n=25, lo=36, hi=86, cw=6.4, small=True)
    ch.ztext(18.3, 62.4, 'Breaker H1', BBC, 9.5)
    xr = ch.X(RT); yr = ch.Y(64)
    f.r(xr - 16, yr - 22, 32, 44, fill='none', stroke=GOOD, sw=2, rx=6, dash='4,3'); f.t(xr, yr + 38, 'phóng to → M5', 10.5, True, GOOD, 'middle')
    rows(f, x + 14, y + 336, [(None, BBC, 'Trả lời:', 'Giá quét đáy H1, rồi đóng cửa trên đỉnh giữa H1 → Bullish Breaker H1 nằm trong vùng D1. Đặt cảnh báo, chờ giá quay lại.')], W3 - 28)
    # M5
    x = X3[2]; f.card(x, y, W3, 444, 'M5 — Có tín hiệu để vào lệnh không?', tcolor=GOOD)
    ch = Chart(f, x + 12, y + 48, W3 - 24, 250, 56, 88, 20, cw=7.4)
    ch.zone(0, 19, 60.3, 67, BBC, 'Breaker H1', pos='bl', op=0.13); ch.zone(11, 19, 67.6, 70.8, FVG, op=0.2)
    ch.candles(M5SEQ)
    ch.lab(9, 62.9, 'sweep', dx=-9, dy=4, color=LIQ, anchor='end'); ch.level(69.5, 7, 12, STR, sw=1.1); ch.lab(11, 71.5, 'MSS', dx=-10, dy=-8, color=GOOD, anchor='end'); ch.lab(18.4, 70.8, 'FVG', dy=-5, color=FVG, anchor='end')
    ch.dot(14, 69.6, GOOD); ch.lab(14, 69.2, 'entry', dx=9, dy=4, color=GOOD, anchor='start')
    rows(f, x + 14, y + 336, [(None, GOOD, 'Trả lời:', 'Tại Breaker H1: quét đáy M5 → đóng trên đỉnh M5 (MSS) bằng nến mạnh → để lại FVG → vào lệnh khi giá hồi về FVG.')], W3 - 28)
    f.foot('Thứ tự không đảo được: không có câu trả lời D1 thì không tìm setup H1; không có Breaker H1 trong vùng D1 thì chuỗi M5 chỉ là nhiễu. M5 không được quyền tạo ra bối cảnh.')
    return f.save()

# ------------------------------------------------------------------ 44 full ICT 2022 example
def fig44():
    f = Fig(44, 'ICT-2022-Vi-Du-Day-Du', 'Breaker trong ICT 2022 Model: một ví dụ mua hoàn chỉnh trên M5',
            'Dải xanh dương là Breaker H1 (đã được chọn từ trước). Mọi thứ còn lại là điều M5 phải CHO THẤY trước khi có lệnh. Đây là một khung ví dụ, không phải trình tự bắt buộc.', h=700, tag='VÍ DỤ DỰNG')
    y0 = f.top + 4
    chips = ['D1: bias tăng', 'D1: vùng chờ', 'H1: Breaker', 'giá tới Breaker', 'M5 sweep', 'M5 MSS', 'displacement', 'FVG', 'entry', 'stop', 'target']
    xx = 28
    for k, c in enumerate(chips):
        col = STR if k < 2 else (BBC if k < 4 else GOOD)
        wd = f.pill(xx, y0, c, col, 10.5); xx += wd + (6 if k < len(chips) - 1 else 0)
        if k < len(chips) - 1: f.t(xx - 3, y0 + 14, '›', 13, True, SUB, 'middle'); xx += 3
    y1 = y0 + 34; H = 700 - y1 - 60
    f.card(28, y1, 600, H)
    ch = Chart(f, 46, y1 + 26, 540, H - 56, 54, 92, 20, cw=15)
    ch.zone(0, 19, 60.3, 67, BBC, 'BREAKER H1 (vùng đã chọn trước)', pos='bl', op=0.12)
    ch.zone(11, 19, 67.6, 70.8, FVG, op=0.2)
    ch.candles(M5SEQ)
    ch.level(65, 6, 10, LIQ, sw=1.2); ch.lab(6, 65, 'đáy M5', dx=-12, dy=14, color=LIQ, anchor='end')
    ch.level(69.5, 7, 12, STR, sw=1.2); ch.lab(7, 69.5, 'đỉnh M5', dy=-8, color=STR)
    ch.badge(9, 62.5, 1, LIQ, dy=18); ch.badge(11, 71.5, 2, GOOD, dy=-18, dx=-16); ch.badge(12.6, 69.2, 3, FVG, dy=0, dx=30)
    ch.badge(14, 69, 4, GOOD, dy=18)
    ch.level(61.6, 9, 19, BAD, 'mức dừng: dưới đáy vừa quét', pos='c', dash='3,3', dy=-5); ch.badge(19.2, 61.6, 5, BAD, dy=0, dx=4)
    ch.level(88, 12, 19, PINK, 'mục tiêu: đỉnh H1 → DOL D1', pos='l'); ch.badge(19.2, 88, 6, PINK, dy=0, dx=4)
    x = 642
    f.card(x, y1, 330, H, 'Vì sao từng bước cần có')
    rows(f, x + 14, y1 + 52, [
        (1, LIQ, 'Sweep đáy M5 bên trong Breaker', 'Giá vào vùng và lấy túi lệnh dưới đáy M5. Vẫn nằm trên mép xa của Breaker H1.'),
        (2, GOOD, 'MSS: đóng cửa trên đỉnh M5', 'Bằng chứng đầu tiên rằng phe mua đang giữ vùng — không chỉ là “giá chạm vùng”.'),
        (3, FVG, 'Displacement để lại FVG', 'Cú bật đi nhanh. FVG cho một chỗ cụ thể để vào lệnh.'),
        (4, GOOD, 'Entry khi giá hồi về FVG', 'Không mua đuổi. Chờ giá quay lại khoảng trống.'),
        (5, BAD, 'Stop theo điều kiện “sai”', 'Dưới đáy vừa quét. Nếu giá xuống đó, chuỗi M5 đã sai.'),
        (6, PINK, 'Target là liquidity', 'Đỉnh H1 gần nhất trước, sau đó tới DOL của D1.')], 302, size=11.4, gap=6, tsize=12)
    f.foot('Breaker = VỊ TRÍ để chờ. Chuỗi M5 = BẰNG CHỨNG để hành động. Thiếu chuỗi M5 thì dù vùng đẹp đến đâu cũng không có lệnh. Rủi ro mỗi lệnh theo quy tắc của bạn: không quá 0,5%.')
    return f.save()

# ------------------------------------------------------------------ 45 three invalidation levels
def fig45():
    f = Fig(45, 'Ba-Muc-Sai', 'Ba mức “sai” khác nhau — đừng dùng một đường cho tất cả',
            'Mỗi mức trả lời một câu hỏi riêng: lệnh này sai chưa? vùng này sai chưa? cả ý tưởng sai chưa? Mức dừng lỗ nên gắn với câu hỏi bạn đang đặt cược.', h=640)
    y0 = f.top + 4; H = 640 - y0 - 44
    f.card(28, y0, 600, H)
    ch, cs = base_chart(f, 46, y0 + 30, 564, H - 62, upto=22, lo=33, hi=88)
    ch.level(62.6, 18, 24, GOOD, dash='3,3'); ch.level(59.4, 14, 24, WARN, dash='3,3'); ch.level(40.2, 10, 24, BAD, dash='3,3')
    ch.badge(24.2, 62.6, 1, GOOD, dy=0, dx=2); ch.badge(24.2, 59.4, 2, WARN, dy=0, dx=2); ch.badge(24.2, 40.2, 3, BAD, dy=0, dx=2)
    ch.lab(23.4, 62.6, 'dưới đáy cú chạm', dy=-5, color=GOOD, anchor='end', size=10); ch.lab(23.4, 59.4, 'dưới mép xa Breaker', dy=14, color=WARN, anchor='end', size=10); ch.lab(23.4, 40.2, 'dưới đáy mới (đáy quét)', dy=-5, color=BAD, anchor='end', size=10)
    ch.ztext(18, 64.6, 'BREAKER', BBC, 10)
    x = 642
    f.card(x, y0, 330, H, 'Ba câu hỏi, ba mức')
    yy = rows(f, x + 14, y0 + 52, [
        (1, GOOD, 'SETUP sai', 'Giá xuống dưới đáy của cú chạm (trên M5: dưới đáy vừa quét). Chuỗi vào lệnh đã hỏng. Gần nhất → mất ít nhất khi sai, nhưng dễ bị nhiễu quét.'),
        (2, WARN, 'VÙNG sai', 'Thân nến đóng dưới mép xa của Breaker và ở lại. Breaker này thất bại — ý tưởng tăng thì chưa chắc.'),
        (3, BAD, 'Ý TƯỞNG sai', 'Giá xuống dưới đáy mới. Cả câu chuyện “đáy đã bị quét rồi đảo chiều” không còn. Xa nhất → khó bị quét, nhưng mất nhiều nhất khi sai.')], 302, size=11.6)
    f.note(x + 14, yy + 2, 302, 'ICT không nêu nơi đặt stop trong bài giảng Breaker. Ba mức trên là khung làm việc của note; chọn mức nào phải được quyết định TRƯỚC khi vào lệnh và ghi vào nhật ký.', WARN, 'Lưu ý về nguồn', size=11.4)
    f.foot('Quy ước “đóng cửa và ở lại”: một cái râu qua mép xa là cú quét, chưa phải vô hiệu. Vô hiệu khi thân nến đóng qua và vài nến sau vẫn nằm bên kia.')
    return f.save()

# ------------------------------------------------------------------ 46 D1 vs H1 conflict
def fig46():
    f = Fig(46, 'Xung-Dot-D1-H1', 'Khi Breaker H1 nói ngược D1: ai thắng?',
            'D1 đang hướng lên trong cả hai hình. Khác nhau ở chỗ Breaker H1 xuất hiện theo hướng nào — và điều đó quyết định bạn dùng nó hay chỉ ghi chú.', h=620, tag='ĐA KHUNG')
    y = f.top + 6
    vs = [('A · H1 CÙNG hướng D1 — Bullish Breaker trong nhịp hồi', GOOD, [(2, 22), (20, 70), (30, 58), (40, 64), (52, 40), (70, 76), (80, 64), (96, 94)], (40, 96, 60, 65), BBC,
           'D1 tăng, giá hồi về. Trong nhịp hồi, H1 quét đáy rồi phá đỉnh giữa → Bullish Breaker H1 thuận D1. Đây là setup để chờ.'),
          ('B · H1 NGƯỢC hướng D1 — Bearish Breaker giữa xu hướng tăng', WARN, [(2, 20), (22, 58), (32, 48), (46, 72), (56, 52), (66, 60), (76, 44), (96, 90)], (56, 80, 50, 54), WARN,
           'D1 vẫn tăng. H1 quét đỉnh rồi phá đáy giữa → Bearish Breaker H1. Thường đây chỉ là cách nhịp hồi của D1 diễn ra. Không bán theo nó.')]
    for k, (tt, c, pts, z, zc, cap) in enumerate(vs):
        x = X2[k]
        f.card(x, y, W2, 470, tt, tcolor=c, tsize=12.8)
        cx, cy, cw_, chh = x + 20, y + 52, W2 - 40, 270
        f.arrow(cx, cy + chh - 6, cx + cw_, cy + 14, '#D1D5DB', 9, size=16); f.t(cx + cw_ - 60, cy + 54, 'D1: hướng lên', 11, True, SUB, 'end')
        f.r(cx + z[0] / 100 * cw_, cy + chh - z[3] / 100 * chh, (z[1] - z[0]) / 100 * cw_, (z[3] - z[2]) / 100 * chh, fill=zc, stroke=zc, sw=1.2, rx=2, dash='5,3', op=0.18)
        zig(f, cx, cy, cw_, chh, pts, '#374151', 2.3)
        f.t(cx + z[0] / 100 * cw_ + 4, cy + chh - z[2] / 100 * chh + 14, 'Bullish Breaker H1' if k == 0 else 'Bearish Breaker H1', 10.5, True, zc, halo=True)
        f.p(x + 16, y + 362, cap, W2 - 32, 12.2)
        f.pill(x + 16, y + 428, 'DÙNG làm setup POI' if k == 0 else 'CHỈ GHI CHÚ — chờ H1 quay lại thuận D1', c, 10.5)
    f.foot('Quy tắc làm việc: khung lớn quyết định HƯỚNG, khung nhỏ quyết định THỜI ĐIỂM. Bearish Breaker H1 ở hình B còn có ích theo cách khác: khi nó bị phá ngược lại, đó là dấu hiệu nhịp hồi đã xong.')
    return f.save()

ALL = [fig31, fig32, fig33, fig34, fig35, fig36, fig37, fig38, fig39, fig40, fig41, fig42, fig43, fig44, fig45, fig46]
if __name__ == '__main__':
    for fn in ALL: print(fn())
