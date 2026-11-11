# -*- coding: utf-8 -*-
from bbdraw import *
from figs1 import base_chart, TX, zig, OBSEQ, TEAL

X4 = [28 + k * 239 for k in range(4)]; W4 = 227
X3 = [28 + k * 319 for k in range(3)]; W3 = 306
X2 = [28 + k * 484 for k in range(2)]; W2 = 460

def mini(f, x, y, w, h, title, kind='base', flip=False, upto=None, num=None, tcolor=INK, cap=None, lo=35, hi=90, cw=None, blue=True, n=26, tsize=12.5, capsize=11.5, zones=True, capcol=INK, extra=0):
    yy = f.card(x, y, w, h, title, num=num, tcolor=tcolor, tsize=tsize)
    nl = len(wrap(cap, w - 28, capsize)) if cap else 0
    cap_h = nl * capsize * 1.42 + (12 if cap else 0)
    cy = yy + 8; chh = y + h - cy - cap_h - 12 - extra
    ch, cs = base_chart(f, x + 10, cy, w - 20, chh, kind, flip, upto, n=n, lo=lo, hi=hi, cw=cw or max(3.2, min((w - 20) / n * 0.62, 9)), small=True, blue=blue, zones=zones)
    if cap: f.p(x + 14, cy + chh + 22, cap, w - 28, capsize, capcol)
    return ch, cs

def nums(ch, cs, size=8.5):
    for i in range(len(cs)):
        ch.f.t(ch.X(i), ch.y + ch.h + 13, str(i + 1), size, False, '#9CA3AF', 'middle')

# ------------------------------------------------------------------ 15 filmstrip
def fig15():
    f = Fig(15, 'Tam-Buoc-Hinh-Thanh', 'Cơ chế hình thành: tám khung hình của một Bullish Breaker',
            'Mỗi khung chỉ vẽ những cây nến ĐÃ đóng cửa tại thời điểm đó. Đây là cách trader thật sự nhìn thấy: từng nến một, không biết khung kế tiếp.', h=706, tag='CƠ CHẾ')
    steps = [(8, 'OB gốc xuất hiện', 'Giá lên tới đỉnh giữa rồi quay xuống. Nến tăng cuối cùng = bearish OB.', OBC),
             (12, 'Giá rời vùng, đáy cũ thủng', 'Giá rơi qua đáy cũ. Lúc này OB trông như “đã thắng”.', DN),
             (15, 'Giá quay lại vùng OB', 'Giá bật lên và chui vào vùng. OB đang bị thử thách.', WARN),
             (17, 'OB không giữ được', 'Một nến đóng cửa TRÊN đỉnh giữa. OB thất bại, cấu trúc đổi.', UP),
             (19, 'Giá đi tiếp hướng mới', 'Giá tiếp tục tăng, rời xa vùng cũ.', UP),
             (19, 'Vùng cũ được đổi tên', 'Vùng nến ở đỉnh giữa giờ được gọi là Bullish Breaker.', BBC),
             (21, 'Giá quay lại vùng', 'Giá hồi về chạm Breaker. Đây là retest.', BBC),
             (24, 'Có thể phản ứng', 'Lần này giá bật lên. Lần khác có thể thủng.', INK)]
    y0 = f.top + 6
    for k, (upto, tt, cap, c) in enumerate(steps):
        x = X4[k % 4]; y = y0 + (k // 4) * 286
        ch, cs = mini(f, x, y, W4, 276, tt, upto=upto, num=k + 1, tcolor=c, cap=cap, blue=(k >= 5), lo=37, hi=86)
        if k == 0: ch.zone(HI, HI, Z_LO, Z_HI, OBC, op=0, dash=None, sw=1.6)
        if k == 1: ch.dot(L2, P_L2, DN)
        if k == 2: ch.dot(14, 63, WARN)
        if k == 3: ch.dot(CF, 71.5, UP)
        if k == 6: ch.dot(RT, 63.5, BBC)
        if k < 7 and k % 4 != 3: f.arrow(x + W4 + 1, y + 138, x + W4 + 11, y + 138, STR, 2, size=6)
    f.foot('Khung 4 gộp hai việc: “OB thất bại” và “cấu trúc bị phá”. Vì OB nằm ngay tại đỉnh giữa nên một nến đóng trên đỉnh giữa làm cả hai việc cùng lúc.')
    return f.save()

# ------------------------------------------------------------------ 16 what failure means
def fig16():
    f = Fig(16, 'Failure-Co-Bon-Muc', '“OB thất bại” nghĩa là gì? Bốn mức — chỉ mức D mới là thất bại',
            'Cùng một bearish OB ở đỉnh giữa (vùng cam), bốn cách giá quay lại. Chữ “thất bại” phải gắn với NẾN ĐÓNG CỬA ở đâu, không phải cảm giác.', h=600)
    y = f.top + 6
    vs = [('A · Chạm rồi bị đẩy ra', 'obholds', None, GOOD, 'OB GIỮ', 'Giá chui vào vùng, quay đầu, lập đáy thấp hơn nữa. OB làm đúng vai.'),
          ('B · Râu vượt đỉnh, thân đóng lại', 'wick', None, WARN, 'CHƯA THẤT BẠI', 'Râu thò lên trên đỉnh giữa rồi rút về. Đó là một cú quét, không phải cú phá.'),
          ('C · Thân đóng TRONG vùng', 'base', 16, WARN, 'ĐANG BỊ THỬ', 'Nến đóng cửa bên trong vùng, dưới đỉnh giữa. Chưa kết luận được gì.'),
          ('D · Thân đóng TRÊN đỉnh giữa', 'toconfirm', None, BAD, 'OB THẤT BẠI', 'Nến đóng cửa trên đỉnh giữa. Vai “chặn” đã hết và cấu trúc khung này đã đổi.')]
    for k, (tt, kind, upto, c, st, cap) in enumerate(vs):
        ch, cs = mini(f, X4[k], y, W4, 440, tt, kind=kind, upto=upto, tcolor=c, cap=cap, blue=False, lo=35, hi=80, n=22, capsize=12, extra=38)
        f.pill(X4[k] + W4 / 2, y + 404, st, c, 11, anchor='middle')
        if k == 1: ch.lab(15, 69.5, 'râu', dy=-6, color=WARN)
        if k == 2: ch.dot(15, 66, WARN)
        if k == 3: ch.dot(CF, 71.5, BAD)
    f.foot('Trẻ con: A = gõ cửa rồi bỏ đi. B = thò tay qua khe cửa rồi rụt lại. C = đứng ngay ngưỡng cửa. D = đã bước hẳn vào nhà và đóng cửa sau lưng.')
    return f.save()

# ------------------------------------------------------------------ 17 structure before / after
def fig17():
    f = Fig(17, 'Cau-Truc-Truoc-Va-Sau', 'Điều gì thật sự thay đổi? Đọc cấu trúc TRƯỚC và SAU khi đỉnh giữa bị phá',
            'Cùng những cái đỉnh và đáy ấy, nhưng ý nghĩa của chúng đổi hẳn sau một cây nến. Đây là lõi của chữ “Breaker”.', h=600, tag='CƠ CHẾ')
    y = f.top + 6
    pa = [(4, 62), (20, 47), (42, 67), (70, 41), (84, 52)]
    pb = pa[:4] + [(96, 78)]
    for k, (pts, tt, c) in enumerate(((pa, 'TRƯỚC — mọi thứ đang kể chuyện GIẢM', DN), (pb, 'SAU — chuyện GIẢM bị xoá trên khung này', UP))):
        x = X2[k]
        f.card(x, y, W2, 452, tt, tcolor=c)
        o = zig(f, x + 24, y + 56, 412, 240, pts, STR if k == 0 else STR, 2.4, lo=35, hi=82)
        yl = o[2][1]; yo = o[1][1]
        f.ln(o[1][0], yo, o[3][0] + 20, yo, LIQ, 1.2, '5,4'); f.ln(o[2][0], yl, x + W2 - 24, yl, STR, 1.2, '5,4')
        for q in o[:4]: f.circ(q[0], q[1], 4, STR)
        f.t(o[1][0], yo + 18, 'đáy cũ', 11, True, LIQ, 'middle', halo=True)
        f.t(o[3][0], o[3][1] + 18, 'đáy mới (thấp hơn)' if k == 0 else 'đáy mới → đọc lại là “cú quét”', 11, True, DN if k == 0 else LIQ, 'middle', halo=True)
        f.r(o[2][0] - 16, yl - 2, 32, 22, fill=OBC if k == 0 else BBC, stroke=OBC if k == 0 else BBC, sw=1.4, rx=3, op=0.22)
        if k == 0:
            f.t(o[2][0], yl - 24, 'đỉnh giữa = đỉnh ĐƯỢC BẢO VỆ', 11, True, STR, 'middle', halo=True); f.t(o[2][0], yl - 10, 'của nhịp giảm', 11, True, STR, 'middle', halo=True)
            f.t(o[4][0] + 8, o[4][1] + 4, '?', 18, True, SUB)
            body = 'Đáy sau thấp hơn đáy trước → phe bán đang thắng. Đỉnh giữa là nơi cú bán thắng ấy xuất phát. Chừng nào đỉnh này còn nguyên, chuyện “giá đang giảm” còn nguyên. Vùng nến ở đó được nhìn như KHÁNG CỰ.'
        else:
            f.pill(o[2][0] + 150, yl - 26, 'MSS', UP, 11); f.t(o[2][0] - 20, yl - 10, 'đỉnh giữa ĐÃ BỊ PHÁ', 11, True, UP, 'end', halo=True)
            body = 'Đỉnh sinh ra cái đáy mới đã bị vượt bằng thân nến → chuỗi “đỉnh thấp hơn, đáy thấp hơn” không còn. Phe bán đã thua tại chính nơi họ mạnh nhất. Vùng nến ở đó được theo dõi như HỖ TRỢ có thể có.'
        f.p(x + 14, y + 336, body, W2 - 28, 12.2)
    f.foot('Chú ý chữ “được theo dõi như”: cấu trúc đổi là QUAN SÁT. Việc vùng cũ sẽ đỡ giá là kỳ vọng của khung ICT — một giả thuyết, không phải hệ quả tất yếu.')
    return f.save()

# ------------------------------------------------------------------ 18-23 worked examples
def example(num, slug, title, sub, kind, flip, rows, verdict, marks):
    f = Fig(num, slug, title, sub, h=640, tag='VÍ DỤ DỰNG')
    y0 = f.top + 4; H = 640 - y0 - 28
    f.card(28, y0, 600, H)
    cs = seq(kind); n = len(cs) + 1
    ch, cs = base_chart(f, 46, y0 + 26, 564, H - 66, kind=kind, flip=flip, n=n, lo=35, hi=90 if kind != 'obholds' else 80, blue=(kind != 'mitig'))
    nums(ch, cs)
    marks(ch)
    x = 642
    f.card(x, y0, 330, H, 'Đọc từng nến (số ở dưới chart)')
    yy = y0 + 50
    for a, b in rows:
        f.t(x + 14, yy, a, 12, True, BBC)
        yy = f.p(x + 14, yy + 16, b, 302, 11.8) + 7
    c, vt, vb = verdict
    f.note(x + 14, y0 + H - 14 - (len(wrap(vb, 278, 11.8)) + 1) * 16.8 - 20, 302, vb, c, vt, size=11.8)
    return f.save()

def std_marks(flip, kind):
    t = TX[flip]
    def m(ch):
        ch.zone(HI, HI, Z_LO, Z_HI, OBC, op=0, dash=None, sw=1.8)
        ch.lab(L1, P_L1, t['old'].upper(), dy=15, color=LIQ); ch.lab(HI, P_H, t['mid'].upper(), dy=-8, color=STR)
        if kind == 'mitig':
            ch.lab(10, 50, t['old'].split(' ')[0].upper() + ' CAO HƠN' if not flip else 'ĐỈNH THẤP HƠN', dy=15, color=TEAL)
            ch.ztext(17.4, 63.6, 'MITIGATION\nBLOCK', TEAL); ch.ztext(10.5, 63.6, t['ob'].replace('\n', ' '), OBC)
            ch.lab(11, P_L1, '%s KHÔNG bị vi phạm' % t['old'].lower(), dx=40, dy=15, color=LIQ, anchor='start')
        elif kind == 'wick':
            ch.lab(L2, P_L2, t['new'].split(' (')[0].upper(), dy=15, color=DN if not flip else UP)
            ch.ztext(12, 65.4, t['ob'].replace('\n', ' ') + ' — vẫn còn sống', OBC)
            ch.lab(15, 69.5, 'chỉ là RÂU', dy=-7, color=WARN)
        else:
            ch.lab(L2, P_L2, t['new'].split(' (')[0].upper(), dy=15, color=DN if not flip else UP)
            ch.ztext(11, 63.6, t['ob'].replace('\n', ' '), OBC); ch.ztext(18, 63.6, t['bb'].replace(' ', '\n'), BBC)
            if kind == 'fail':
                ch.lab(22, 56.5, 'đóng cửa %s mép xa' % t['below'], dx=-14, dy=4, color=BAD, anchor='end')
    return m

def fig18():
    return example(18, 'Bullish-Vi-Du-1-Textbook', 'Bullish Breaker · Ví dụ 1 — trường hợp sách giáo khoa',
                   'Đủ ba mắt xích, có retest, retest giữ. Vùng cam = OB gốc. Vùng xanh dương = Breaker (từ lúc nến 17 đóng cửa).', 'base', False,
                   [('Nến 3', 'Tạo ĐÁY CŨ. Bên dưới đáy này có thể có lệnh bán chờ.'),
                    ('Nến 7', 'Nến tăng cuối cùng ở đỉnh giữa. Đánh dấu vùng cam ngay lúc này, lấy cả râu.'),
                    ('Nến 8–12', 'Giá rơi. Nến 11 xuống dưới đáy cũ → mắt xích 2 xong. Nến 12 tạo đáy mới.'),
                    ('Nến 13–16', 'Bốn nến tăng liên tiếp. Nến 15–16 vào vùng cam nhưng CHƯA đóng cửa trên đỉnh giữa.'),
                    ('Nến 17', 'Đóng cửa trên đỉnh giữa → mắt xích 3 xong. Vùng cam đổi tên thành Bullish Breaker.'),
                    ('Nến 21', 'Giá hồi về, râu chạm sâu vào vùng, nến đóng cửa trong vùng — không đóng dưới mép xa.'),
                    ('Nến 22–24', 'Giá bật lên. Đây là phản ứng — và ta chỉ biết SAU khi nó xảy ra.')],
                   (GOOD, 'Đủ ba mắt xích → Bullish Breaker', 'Retest giữ. Một mẫu đẹp — và chỉ là MỘT mẫu.'), std_marks(False, 'base'))

def fig19():
    return example(19, 'Bullish-Vi-Du-2-Thieu-Dieu-Kien', 'Bullish Breaker · Ví dụ 2 — trông giống hệt nhưng thiếu một mắt xích',
                   'Giá phá đỉnh giữa, quay lại, bật lên — y như Ví dụ 1. Chỉ khác một chỗ: đáy cũ chưa hề bị vi phạm.', 'mitig', False,
                   [('Nến 3', 'Tạo ĐÁY CŨ.'),
                    ('Nến 7', 'Nến tăng cuối cùng ở đỉnh giữa → vùng cam.'),
                    ('Nến 8–11', 'Giá rơi nhưng DỪNG phía trên đáy cũ (tạo đáy cao hơn). Mắt xích 2 KHÔNG xảy ra.'),
                    ('Nến 12–16', 'Giá tăng trở lại. Nến 16 đóng cửa trên đỉnh giữa.'),
                    ('Nến 20', 'Giá hồi về vùng rồi bật lên — hành vi giống hệt một Breaker.')],
                   (WARN, 'Thiếu mắt xích 2 → Mitigation Block', 'Theo ICT đây là tên khác. Mức “sai” của ý tưởng nằm ở đáy cao hơn, không phải ở một đáy quét. Ghi đúng tên để sau này so sánh được hai loại.'), std_marks(False, 'mitig'))

def fig20():
    return example(20, 'Bullish-Vi-Du-3-That-Bai', 'Bullish Breaker · Ví dụ 3 — đúng định nghĩa, và thất bại',
                   'Mười bảy nến đầu giống hệt Ví dụ 1. Khác biệt chỉ xuất hiện khi giá quay lại: vùng không đỡ được.', 'fail', False,
                   [('Nến 1–17', 'Đủ ba mắt xích. Vùng được gọi là Bullish Breaker — hoàn toàn đúng định nghĩa.'),
                    ('Nến 20–21', 'Giá hồi về. Nến 21 đóng cửa trong vùng.'),
                    ('Nến 22', 'Đóng cửa sát mép xa. Chưa thủng, nhưng không có cây nến tăng nào phản ứng.'),
                    ('Nến 23', 'Đóng cửa DƯỚI mép xa của vùng. Theo quy ước của note: Breaker thất bại.'),
                    ('Nến 24–25', 'Giá đi tiếp xuống. Ai mua “vì giá chạm Breaker” ở nến 21 đang lỗ.')],
                   (BAD, 'Breaker hợp lệ — và thất bại', 'Tên đúng không hứa kết quả. Lệnh chỉ nên có khi khung nhỏ cho bằng chứng phản ứng; ở đây không có.'), std_marks(False, 'fail'))

def fig21():
    return example(21, 'Bearish-Vi-Du-1-Textbook', 'Bearish Breaker · Ví dụ 1 — trường hợp sách giáo khoa',
                   'Ảnh gương của Bullish. Vùng cam = OB gốc (bullish OB ở đáy giữa). Vùng xanh dương = Bearish Breaker (từ lúc nến 17 đóng cửa).', 'base', True,
                   [('Nến 3', 'Tạo ĐỈNH CŨ. Bên trên đỉnh này có thể có lệnh mua chờ.'),
                    ('Nến 7', 'Nến giảm cuối cùng ở đáy giữa. Đánh dấu vùng cam ngay lúc này, lấy cả râu.'),
                    ('Nến 8–12', 'Giá tăng. Nến 11 lên trên đỉnh cũ → mắt xích 2 xong. Nến 12 tạo đỉnh mới.'),
                    ('Nến 13–16', 'Bốn nến giảm liên tiếp. Nến 15–16 vào vùng cam nhưng CHƯA đóng cửa dưới đáy giữa.'),
                    ('Nến 17', 'Đóng cửa dưới đáy giữa → mắt xích 3 xong. Vùng cam đổi tên thành Bearish Breaker.'),
                    ('Nến 21', 'Giá hồi lên, râu chạm sâu vào vùng, nến đóng cửa trong vùng — không đóng trên mép xa.'),
                    ('Nến 22–24', 'Giá rơi tiếp. Đây là phản ứng — và ta chỉ biết SAU khi nó xảy ra.')],
                   (GOOD, 'Đủ ba mắt xích → Bearish Breaker', 'Retest giữ. Một mẫu đẹp — và chỉ là MỘT mẫu.'), std_marks(True, 'base'))

def fig22():
    return example(22, 'Bearish-Vi-Du-2-Thieu-Dieu-Kien', 'Bearish Breaker · Ví dụ 2 — râu đâm qua đáy giữa nhưng thân không đóng qua',
                   'Đỉnh cũ đã bị vi phạm (mắt xích 2 có). Nhưng đáy giữa chỉ bị một cái râu chọc thủng — mắt xích 3 chưa xảy ra.', 'wick', True,
                   [('Nến 3', 'Tạo ĐỈNH CŨ.'),
                    ('Nến 7', 'Nến giảm cuối cùng ở đáy giữa → vùng cam (bullish OB).'),
                    ('Nến 8–12', 'Giá tăng vượt đỉnh cũ, tạo đỉnh mới. Mắt xích 2 xong.'),
                    ('Nến 13–15', 'Giá rơi về vùng cam.'),
                    ('Nến 16', 'Râu đâm xuống DƯỚI đáy giữa, nhưng nến đóng cửa quay lại phía trên. Chỉ là râu.'),
                    ('Nến 17–21', 'Giá bật lên từ vùng. OB gốc GIỮ đúng vai hỗ trợ — không có gì đổi vai cả.')],
                   (WARN, 'Thiếu mắt xích 3 → không phải Breaker', 'Vẽ Bearish Breaker ở nến 16 là vẽ sớm. Thực tế: một bullish OB hoạt động đúng vai, kèm một cú quét dưới đáy giữa.'), std_marks(True, 'wick'))

def fig23():
    return example(23, 'Bearish-Vi-Du-3-That-Bai', 'Bearish Breaker · Ví dụ 3 — đúng định nghĩa, và thất bại',
                   'Mười bảy nến đầu giống hệt Ví dụ 1. Khi giá hồi lên, vùng không chặn được.', 'fail', True,
                   [('Nến 1–17', 'Đủ ba mắt xích. Vùng được gọi là Bearish Breaker — hoàn toàn đúng định nghĩa.'),
                    ('Nến 20–21', 'Giá hồi lên. Nến 21 đóng cửa trong vùng.'),
                    ('Nến 22', 'Đóng cửa sát mép xa. Chưa thủng, nhưng không có cây nến giảm nào phản ứng.'),
                    ('Nến 23', 'Đóng cửa TRÊN mép xa của vùng. Theo quy ước của note: Breaker thất bại.'),
                    ('Nến 24–25', 'Giá đi tiếp lên. Ai bán “vì giá chạm Breaker” ở nến 21 đang lỗ.')],
                   (BAD, 'Breaker hợp lệ — và thất bại', 'Câu hỏi nên đặt: khung lớn đang đi hướng nào? Một Bearish Breaker khung nhỏ ngược hướng khung lớn thường chỉ là một nhịp nghỉ.'), std_marks(True, 'fail'))

# ------------------------------------------------------------------ 24 four kinds of failed OB
MIDLEG = mk(80, [76, 72, 74.5, 69, 64, 59, 55, 59, 64, 69, 73, 77, 75.5, 73, 70], {0: {'h': 82}, 2: {'h': 75.2, 'l': 71.6}, 3: {'h': 74.6}, 6: {'l': 53}})

def fig24():
    f = Fig(24, 'Failed-OB-Bon-Nhanh', 'Một bearish OB bị giá xuyên qua. Nó là gì? Bốn nhánh, bốn cái tên',
            'Ba câu hỏi quyết định tên gọi: (1) OB có nằm tại một swing không? (2) cực trị cũ đã bị vi phạm chưa? (3) thân nến đã đóng qua swing chứa OB chưa?', h=566)
    y = f.top + 6
    vs = [('BREAKER', BBC, 'base', 19, ('✓', '✓', '✓'), 'Đủ cả ba. Vùng đổi vai.'),
          ('MITIGATION BLOCK', TEAL, 'mitig', 18, ('✓', '✗', '✓'), 'Đáy cũ không bị vi phạm (đáy cao hơn).'),
          ('OB VÔ HIỆU (không có tên riêng)', '#6B7280', None, None, ('✗', '–', '✗'), 'OB nằm giữa một nhịp giảm. Giá đóng cửa qua nó nhưng đỉnh gốc của nhịp còn nguyên.'),
          ('OB CHƯA THẤT BẠI', GOOD, 'wick', None, ('✓', '✓', '✗'), 'Chỉ có râu vượt qua. Vùng vẫn đang làm vai cũ.')]
    qs = ['OB nằm tại swing?', 'Cực trị cũ bị vi phạm?', 'Thân nến đóng qua swing?']
    for k, (name, c, kind, upto, ans, cap) in enumerate(vs):
        x = X4[k]
        f.card(x, y, W4, 430, name, tcolor=c, tsize=12.5)
        cy = y + 62
        if kind:
            ch, cs = base_chart(f, x + 10, cy, W4 - 20, 190, kind, upto=upto, n=26, lo=35, hi=84, cw=5, small=True, blue=True)
        else:
            ch = Chart(f, x + 10, cy, W4 - 20, 190, 48, 86, 17, cw=6.5)
            ch.zone(2, 14, 71.6, 75.2, '#6B7280', op=0.16); ch.candles(MIDLEG)
            ch.level(82, 0, 14, STR, 'đỉnh gốc — chưa bị phá', pos='r', sw=1, size=9.5)
            ch.zone(2, 2, 71.6, 75.2, '#6B7280', op=0, dash=None, sw=1.6)
        yy = y + 284
        for q, a in zip(qs, ans):
            col = GOOD if a == '✓' else (BAD if a == '✗' else SUB)
            f.t(x + 14, yy, q, 11.5, False, INK); f.t(x + W4 - 16, yy, a, 14, True, col, 'end'); yy += 24
        f.ln(x + 14, yy - 8, x + W4 - 14, yy - 8, BORDER, 1)
        f.p(x + 14, yy + 14, cap, W4 - 28, 12)
    f.foot('Cả bốn đều bắt đầu bằng một OB bị giá đi vào. “Failed Order Block” là cái tên RỘNG (nhánh 1, 2, 3). “Breaker” là cái tên HẸP — chỉ nhánh 1.')
    return f.save()

# ------------------------------------------------------------------ 25 who is where
def fig25():
    f = Fig(25, 'Ai-Dang-Dung-O-Dau', 'Vì sao vùng có thể đổi vai? Ai đang đứng ở đâu sau cú phá',
            'Bản đồ năm nhóm người CÓ THỂ có mặt quanh một Bullish Breaker ngay sau khi nến xác nhận đóng cửa. Tất cả là [DIỄN GIẢI] — chart nến không cho thấy họ.', h=640, tag='DIỄN GIẢI')
    y0 = f.top + 4; H = 640 - y0 - 62
    f.card(28, y0, 600, H)
    ch, cs = base_chart(f, 46, y0 + 30, 564, H - 62, upto=19, lo=35, hi=88)
    for j, pv in enumerate((68.4, 69.6, 70.8)):
        ch.level(pv, 7, 15, LIQ, sw=2, dash=None)
    ch.badge(8, 63.6, 'A', OBC, dy=0, dx=10); ch.badge(9, 42.5, 'B', DN, dy=0)
    ch.badge(11, 70, 'C', LIQ, dy=-16); ch.badge(13.2, 42.5, 'D', UP, dy=0); ch.badge(21.5, 76, 'E', BBC, dy=0)
    ch.lab(11, 72.4, 'lệnh dừng lỗ (đã bị kích hoạt)', dy=-28, color=LIQ)
    ch.lab(L1, P_L1, 'ĐÁY CŨ', dy=15, color=LIQ); ch.lab(HI, P_H, 'ĐỈNH GIỮA', dy=-8, dx=-26, color=STR)
    ch.arr(21.5, 73.5, 21.5, 67.6, BBC, dash='4,3'); ch.lab(21.5, 81, 'chờ giá\nquay về?', dy=0, color=BBC)
    x = 642
    f.card(x, y0, 330, H, 'Năm nhóm và điều họ có thể làm')
    rows = [('A', OBC, 'Người BÁN quanh đỉnh giữa', 'Giá giờ nằm trên giá vốn → đang lỗ. Nếu giá quay về, có thể mua lại để thoát gần hoà vốn.'),
            ('B', DN, 'Người BÁN ĐUỔI lúc đáy cũ thủng', 'Lỗ nhiều hơn. ICT nói nhóm này “will look to mitigate the loss”.'),
            ('C', LIQ, 'Lệnh dừng lỗ trên đỉnh giữa', 'Khi giá vượt đỉnh, chúng thành lệnh MUA ngay → cú phá hay đi nhanh. Sau đó chúng không còn.'),
            ('D', UP, 'Người MUA gần đáy mới', 'Đang lãi. Có thể mua thêm khi giá hồi.'),
            ('E', BBC, 'Người đứng ngoài, lỡ cú phá', 'Có thể đặt lệnh mua chờ ở mức vừa bị phá.')]
    yy = y0 + 50
    for n, c, a, b in rows:
        f.badge(x + 24, yy - 4, n, c); f.t(x + 42, yy, a, 12, True, c)
        yy = f.p(x + 42, yy + 16, b, 272, 11.6) + 7
    f.note(x + 14, yy + 2, 302, 'A + D + E cùng muốn MUA quanh một vùng → vùng đó CÓ THỂ đỡ giá. Nhưng nếu A đã thoát hết bằng stop (C), nguồn mua chính đã biến mất trước khi giá quay lại.', WARN, 'Hai mặt của cùng câu chuyện', size=11.6)
    f.foot('Đây là câu chuyện hợp lý nhất hiện có, không phải dữ kiện. Không ai đo được nhóm nào đông, nhóm nào đã thoát — nhất là trên FX giao ngay, nơi không có sổ lệnh chung.')
    return f.save()

# ------------------------------------------------------------------ 26 at the break vs at the return
def fig26():
    f = Fig(26, 'Luc-Pha-Va-Luc-Quay-Lai', 'Hai khoảnh khắc, hai cơ chế: LÚC PHÁ và LÚC QUAY LẠI',
            'Lúc phá, lệnh dừng (stop) đẩy giá đi nhanh hơn. Lúc quay lại, lệnh chờ (limit) và người muốn thoát có thể đỡ giá — hoặc không.', h=640, tag='CƠ CHẾ')
    y = f.top + 6
    x = X2[0]
    f.card(x, y, W2, 492, 'LÚC PHÁ — vì sao giá hay vọt qua đỉnh giữa', tcolor=LIQ)
    ly = y + 222
    f.ln(x + 30, ly, x + W2 - 30, ly, STR, 1.6, '6,4'); f.t(x + W2 - 32, ly + 16, 'đỉnh giữa', 11, True, STR, 'end')
    for j, (lab, c) in enumerate((('lệnh dừng lỗ của người đang bán', LIQ), ('lệnh mua đuổi của người chờ breakout', LIQ))):
        f.r(x + 150, ly - 40 - j * 34, 270, 26, fill=c, stroke=c, sw=1, rx=6, op=0.10); f.t(x + 285, ly - 23 - j * 34, lab, 11, True, c, 'middle')
    f.arrow(x + 90, ly + 120, x + 90, ly - 110, UP, 4, size=12)
    f.t(x + 104, ly + 100, 'giá đi lên…', 11.5, True, UP); f.t(x + 104, ly - 100, '…và bị đẩy thêm', 11.5, True, UP)
    f.badge(x + 62, ly, 1, INK); f.t(x + 104, ly + 40, '① chạm mức', 11, False, INK); f.t(x + 104, ly + 56, '② lệnh dừng thành lệnh MUA NGAY', 11, False, INK); f.t(x + 104, ly + 72, '③ mua dồn dập → giá nhảy', 11, False, INK)
    f.note(x + 14, y + 396, W2 - 28, 'Lệnh dừng khi bị chạm sẽ thành lệnh thị trường. Nghiên cứu lệnh FX quanh các mức tròn cho thấy hiệu ứng “thác stop” này (Osler 2003). Nghiên cứu đó KHÔNG nói về Order Block hay Breaker.', FVG, '[CƠ CHẾ] có bằng chứng, nhưng cho mức tròn', size=11.6)
    x = X2[1]
    f.card(x, y, W2, 492, 'LÚC QUAY LẠI — vì sao CÓ THỂ được đỡ, vì sao CÓ THỂ không', tcolor=BBC)
    zy = y + 150
    f.r(x + 30, zy, W2 - 60, 44, fill=BBC, stroke=BBC, sw=1.3, rx=4, dash='5,3', op=0.13); f.t(x + W2 / 2, zy + 27, 'vùng Breaker', 12, True, BBC, 'middle')
    f.arrow(x + W2 / 2, y + 64, x + W2 / 2, zy - 6, STR, 2.4, size=9); f.t(x + W2 / 2 + 12, y + 86, 'giá hồi về', 11, True, STR)
    cw_ = (W2 - 42) / 2
    for j, (hd, c, items) in enumerate((('Có thể ĐỠ, vì:', GOOD, ['Người bán bị kẹt mua lại để thoát gần hoà vốn', 'Người lỡ cú phá đặt lệnh mua chờ', 'Người mua từ đáy mua thêm']),
                                        ('Có thể KHÔNG đỡ, vì:', BAD, ['Người bị kẹt đã thoát hết từ lúc phá', 'Lệnh mua chờ mỏng hơn lượng bán đang tới', 'Khung lớn đang đi hướng ngược lại']))):
        xx = x + 14 + j * (cw_ + 14); yy = zy + 76
        f.t(xx, yy, hd, 12.5, True, c); yy += 22
        for it in items:
            f.circ(xx + 4, yy - 4, 2.6, c); yy = f.p(xx + 14, yy, it, cw_ - 16, 11.8) + 6
    f.note(x + 14, y + 396, W2 - 28, 'Cả sáu dòng trên đều không nhìn thấy được trên chart nến. Điều nhìn thấy được chỉ là: giá chạm vùng, rồi nến đóng cửa ở đâu.', WARN, '[DIỄN GIẢI] hợp lý, không kiểm chứng được bằng OHLC', size=11.6)
    f.foot('Trẻ con: lúc phá giống đám đông đang chạy xô đổ hàng rào. Lúc quay lại giống hỏi “còn ai đứng giữ chỗ hàng rào cũ không?” — có thể còn, có thể đã về hết.')
    return f.save()

# ------------------------------------------------------------------ 27 three outcomes
def fig27():
    f = Fig(27, 'Retest-Ba-Ket-Cuc', 'Sau khi Breaker được gọi tên: ba kết cục, cả ba đều phải được ghi lại',
            'Nếu chỉ nhớ kết cục A, mọi khái niệm đều trông như “luôn chạy”. Tỷ lệ giữa A, B và C là thứ duy nhất nói được Breaker có ích với BẠN hay không.', h=600)
    y = f.top + 6
    vs = [('A · Quay lại và GIỮ', 'base', GOOD, 'Giá chạm vùng, không đóng cửa qua mép xa, rồi đi tiếp hướng mới.', 'ghi: GIỮ'),
          ('B · Quay lại và THỦNG', 'fail', BAD, 'Giá chạm vùng rồi đóng cửa qua mép xa. Breaker thất bại.', 'ghi: THỦNG'),
          ('C · KHÔNG quay lại', 'noretest', '#6B7280', 'Giá đi thẳng. Không có retest, không có lệnh. Đừng đuổi theo.', 'ghi: HẾT HẠN')]
    for k, (tt, kind, c, cap, st) in enumerate(vs):
        ch, cs = mini(f, X3[k], y, W3, 448, tt, kind=kind, tcolor=c, cap=cap, lo=35, hi=92, n=27, capsize=12.2, cw=6.2, extra=38)
        f.pill(X3[k] + W3 / 2, y + 412, st, c, 11, anchor='middle')
    f.foot('Kết cục C hay bị quên nhất. Nhưng một Breaker không bao giờ được chạm lại vẫn là một Breaker đã hình thành — nó phải nằm trong mẫu số khi bạn đếm.')
    return f.save()

# ------------------------------------------------------------------ 28 breaker vs mitigation
def fig28():
    f = Fig(28, 'Breaker-vs-Mitigation-Block', 'Breaker và Mitigation Block: khác nhau ở đúng MỘT chỗ',
            'Cả hai đều là “nến ở đỉnh giữa bị phá rồi được quay lại”. Điểm tách duy nhất: trước khi phá, đáy cũ có bị vi phạm hay không.', h=640)
    y = f.top + 6
    for k, (kind, tt, c) in enumerate((('base', 'BREAKER — đáy cũ BỊ vi phạm (đáy thấp hơn)', BBC), ('mitig', 'MITIGATION BLOCK — đáy cũ GIỮ (đáy cao hơn)', TEAL))):
        x = X2[k]
        f.card(x, y, W2, 490, tt, tcolor=c)
        ch, cs = base_chart(f, x + 16, y + 48, W2 - 32, 290, kind, upto=23, n=24, lo=35, hi=88, cw=9, blue=True)
        ch.lab(L1, P_L1, 'ĐÁY CŨ', dy=14, color=LIQ)
        if k == 0:
            ch.f.circ(ch.X(L2), ch.Y(42.5), 17, 'none', stroke=BAD, sw=2); ch.lab(L2, 41, 'xuống DƯỚI đáy cũ', dx=24, dy=6, color=BAD, anchor='start')
            ch.ztext(19.5, 63.6, 'BREAKER', BBC)
        else:
            ch.ztext(18.6, 63.6, 'MITIGATION', TEAL)
            ch.f.circ(ch.X(10), ch.Y(51), 17, 'none', stroke=GOOD, sw=2); ch.lab(10, 50, 'dừng TRÊN đáy cũ', dx=24, dy=10, color=GOOD, anchor='start')
        rows = [('Trình tự swing', 'Thấp – Cao – THẤP HƠN – Cao hơn' if k == 0 else 'Thấp – Cao – CAO HƠN – Cao hơn'),
                ('Liquidity trước cú phá', 'Túi lệnh dưới đáy cũ đã bị lấy' if k == 0 else 'Túi lệnh dưới đáy cũ còn nguyên'),
                ('Ý tưởng sai khi', 'giá xuống dưới đáy quét' if k == 0 else 'giá xuống dưới đáy cao hơn')]
        yy = y + 386
        for a, b in rows:
            f.t(x + 16, yy, a, 11.5, False, SUB); f.t(x + 168, yy, b, 11.8, True, INK); yy += 24
    f.foot('ICT trình bày cả hai như các “hình thức mitigation”. Câu “Breaker mạnh hơn Mitigation Block” phổ biến trong cộng đồng nhưng không có trong bài giảng đã đối chiếu → [GIẢ THUYẾT].')
    return f.save()

# ------------------------------------------------------------------ 29 the block family
RBSEQ = mk(70, [66, 62, 58, 59.5, 64, 69, 72, 68, 63, 59, 64, 70], {2: {'l': 51}, 3: {'l': 53}, 9: {'l': 54.5}})
RCSEQ = mk(80, [76, 72, 75, 78, 74, 70, 65, 60, 56, 61, 67, 73, 78, 81, 78, 75, 79, 84], {1: {'h': 76.6, 'l': 71.2}, 3: {'h': 79}, 8: {'l': 54}, 15: {'l': 73}})

def fig29():
    f = Fig(29, 'Ho-Hang-Block', 'Họ hàng nhà “block”: năm cái tên, năm cây nến khác nhau (ví dụ phía mua)',
            'Tất cả đều là “một vùng nến mà giá có thể phản ứng khi quay lại”. Khác nhau ở: lấy cây nến NÀO, và nó giữ vai CŨ hay đổi vai MỚI.', h=556)
    y = f.top + 6; w = 180; gap = 11
    items = [('Order Block', OBC, 'Nến giảm cuối trước cú tăng mạnh.', 'Vai: hỗ trợ (vai gốc).'),
             ('Breaker', BBC, 'Nến tăng ở đỉnh giữa, sau khi đáy cũ thủng và đỉnh giữa bị phá.', 'Vai: ĐỔI từ chặn sang đỡ.'),
             ('Mitigation Block', TEAL, 'Như Breaker nhưng đáy cũ không bị vi phạm.', 'Vai: ĐỔI từ chặn sang đỡ.'),
             ('Rejection Block', LIQ, 'Phần RÂU dưới của đáy: từ thân thấp nhất xuống tới đáy râu.', 'Vai: hỗ trợ ngay tại đáy.'),
             ('Reclaimed OB', '#DB2777', 'Một bullish OB cũ từng bị thủng, nay giá quay lại phía trên nó.', 'Vai: LẤY LẠI vai gốc (đỡ).')]
    for k, (name, c, body, role) in enumerate(items):
        x = 28 + k * (w + gap)
        f.card(x, y, w, 408, name, tcolor=c, tsize=13)
        cx, cy, cw_, chh = x + 8, y + 44, w - 16, 200
        if k == 0:
            ch = Chart(f, cx, cy, cw_, chh, 38, 78, 17, cw=5); ch.zone(3, 15, 43.5, 49, c, op=0.2); ch.candles(OBSEQ); ch.zone(3, 3, 43.5, 49, c, op=0, dash=None, sw=1.5)
        elif k == 1:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'base', n=25, lo=36, hi=86, cw=4.2, small=True)
        elif k == 2:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'mitig', n=25, lo=36, hi=86, cw=4.2, small=True, zones=False)
            ch.zone(HI, 23, Z_LO, Z_HI, c, op=0.18)
        elif k == 3:
            ch = Chart(f, cx, cy, cw_, chh, 46, 76, 13, cw=6.5); ch.zone(2, 11, 51, 58, c, op=0.2); ch.candles(RBSEQ)
        else:
            ch = Chart(f, cx, cy, cw_, chh, 50, 88, 19, cw=4.8)
            ch.zone(1, 4, 71.2, 76.6, c, op=0.2); ch.zone(5, 11, 71.2, 76.6, '#9CA3AF', op=0.14); ch.zone(12, 17, 71.2, 76.6, c, op=0.2)
            ch.candles(RCSEQ); ch.zone(1, 1, 71.2, 76.6, c, op=0, dash=None, sw=1.5)
            ch.lab(8, 71.2, 'đã thủng', dy=13, color='#6B7280', size=9.5)
        yy = f.p(x + 12, y + 276, body, w - 24, 11.8)
        f.ln(x + 12, y + 352, x + w - 12, y + 352, BORDER, 1)
        f.p(x + 12, y + 372, role, w - 24, 11.8, c, bold=True)
    f.foot('Reclaimed OB và Rejection Block ghi theo cách dùng phổ biến của cộng đồng ICT; lần nghiên cứu này chưa đối chiếu được bài giảng gốc cho hai tên đó.')
    return f.save()

# ------------------------------------------------------------------ 30 breaker vs S/R vs supply-demand
SRSEQ = mk(50, [55, 60, 56, 52, 57, 61, 57, 54, 58, 63, 67, 70, 66, 63.5, 67, 72], {1: {'h': 62}, 5: {'h': 62.2}, 13: {'l': 61.6}})
SDSEQ = mk(50, [55, 60, 61, 60.2, 61.2, 55, 49, 45, 50, 56, 60.5, 66, 69, 65, 62.6, 67, 72], {2: {'h': 61.8, 'l': 59.6}, 3: {'h': 61.6, 'l': 59.5}, 4: {'h': 62, 'l': 59.7}, 14: {'l': 61}})

def fig30():
    f = Fig(30, 'Breaker-vs-SR-vs-Supply-Demand', 'Breaker không phải “mọi vùng bị phá rồi đổi vai”',
            'Ba ý tưởng cùng nói “thứ từng chặn giờ có thể đỡ”. Breaker là phiên bản HẸP nhất: đòi một cây nến cụ thể và một trình tự swing cụ thể.', h=640)
    y = f.top + 6
    cols = [('Hỗ trợ/kháng cự đổi vai (TA cổ điển)', STR, 'Một MỨC ngang, thường đã bị chạm vài lần.', ('✗', '✗', '✓')),
            ('Supply zone bị phá (Supply/Demand)', WARN, 'Một VÙNG nền (vài nến nhỏ) trước một cú rơi mạnh.', ('✗', '✗', '✓')),
            ('Breaker (ICT)', BBC, 'MỘT cây nến ở đỉnh giữa, trong trình tự: đáy – đỉnh – đáy thấp hơn – phá đỉnh.', ('✓', '✓', '✓'))]
    qs = ['Cần một cây nến cụ thể tại swing?', 'Cần cực trị cũ bị vi phạm trước?', 'Cần giá vượt qua và quay lại?']
    for k, (name, c, body, ans) in enumerate(cols):
        x = X3[k]
        f.card(x, y, W3, 480, name, tcolor=c, tsize=12.8)
        cx, cy, cw_, chh = x + 14, y + 50, W3 - 28, 210
        if k == 0:
            ch = Chart(f, cx, cy, cw_, chh, 46, 76, 17, cw=8); ch.candles(SRSEQ); ch.level(62, 0, 16, c, 'mức ngang', pos='l', size=10)
        elif k == 1:
            ch = Chart(f, cx, cy, cw_, chh, 41, 76, 18, cw=8); ch.zone(2, 17, 59.5, 62, c, 'vùng nền', pos='al', op=0.2); ch.candles(SDSEQ)
        else:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'base', n=25, lo=36, hi=86, cw=6.4, small=True)
        yy = f.p(x + 14, y + 296, body, W3 - 28, 12)
        yy = y + 372
        for q, a in zip(qs, ans):
            f.t(x + 14, yy, q, 11.5, False, INK); f.t(x + W3 - 16, yy, a, 14, True, GOOD if a == '✓' else BAD, 'end'); yy += 25
        f.ln(x + 14, yy - 8, x + W3 - 14, yy - 8, BORDER, 1)
        f.p(x + 14, yy + 12, ['Kể chuyện: “mức này quan trọng vì nhiều người nhìn nó”.', 'Kể chuyện: “còn lệnh chưa khớp ở vùng nền”.', 'Kể chuyện: “có người vừa bị bẫy ở cả hai phía”.'][k], W3 - 28, 11.6, SUB)
    f.foot('ICT phê bình việc chỉ kẻ một đường ngang và đòi phải có một “storyline” giải thích vì sao giá làm vậy. Nhưng câu chuyện hay hơn KHÔNG tự động là lợi thế lớn hơn → [BACKTEST REQUIRED].')
    return f.save()

ALL = [fig15, fig16, fig17, fig18, fig19, fig20, fig21, fig22, fig23, fig24, fig25, fig26, fig27, fig28, fig29, fig30]
if __name__ == '__main__':
    for fn in ALL: print(fn())
