# -*- coding: utf-8 -*-
from chdraw import *
import sys


def side_steps(f, x, y, w, rows, size=11.6, gap=7):
    yy = y
    for n, c, a, b in rows:
        f.badge(x + 12, yy - 4, n, c)
        f.t(x + 30, yy, a, 12.3, True, c)
        yy = f.p(x + 30, yy + 16, b, w - 30, size) + gap
    return yy


def box(f, x, y, w, h, txt, c, size=11.5, fill=None, bold=True):
    f.r(x, y, w, h, fill=fill or CARD, stroke=c, sw=1.5, rx=9)
    lines = wrap(txt, w - 16, size, bold)
    yy = y + h / 2 - (len(lines) - 1) * size * 1.3 / 2 + size * 0.36
    for l in lines:
        f.t(x + w / 2, yy, l, size, bold, c if bold else INK, 'middle'); yy += size * 1.3


# ------------------------------------------------------------------ 41 ICT 2022 sequence
def fig41():
    f = F(41, 'ICT-2022-Trinh-Tu-Co-CHoCH', 'CHoCH trong ICT 2022: trình tự trong protocol và trình tự theo thời gian thật',
          'Protocol liệt kê CHoCH → Displacement → FVG như ba bước nối tiếp. Trên nến, chúng thường là BA THUỘC TÍNH CỦA CÙNG MỘT CHÂN SÓNG, xảy ra trong cùng vài nến.', h=660)
    y0 = f.top + 4
    steps = ['D1 context', 'H1 cấu trúc + POI', 'Giá tới POI H1', 'M5 liquidity event', 'M5 CHoCH / MSS', 'Displacement', 'FVG', 'Hồi vào FVG', 'Entry']
    f.t(28, y0 + 16, 'Protocol (danh sách)', 12.5, True, SUB)
    bw = 98
    for k, s_ in enumerate(steps):
        x = 28 + k * (bw + 7.5)
        hl = k in (4, 5, 6)
        box(f, x, y0 + 26, bw, 46, s_, CHC if hl else STR, 10.5, fill=PINKBG if hl else None)
        if k < len(steps) - 1: f.arrow(x + bw, y0 + 49, x + bw + 7, y0 + 49, SUB, 1.4, size=5)
    y1 = y0 + 96
    f.card(28, y1, 600, 660 - y1 - 46)
    cs, tn = bull_seq()
    ch = Chart(f, 44, y1 + 24, 570, 660 - y1 - 90, 50, 88, len(cs) + 1)
    ch.zone(27.6, 31.4, 50.5, 87.5, CHC, None, 'tl', '4,3', 0.05)
    for (i, lo, hi) in fvgs(cs, 28, 32):
        if i == 30: ch.zone(29, 38, lo, hi, FVGC, None, 'tl', '4,3', 0.14)
    ch.level(72.3, 18, 33, PROT, 'protected high', pos='l', dy=-6, sw=1.4)
    ch.level(56.2, 22, 28, SWP, None, dash='4,3', sw=1.1)
    ch.level(54.6, 27, 38, BAD, 'stop (dưới đáy quét)', pos='r', dy=15, sw=1.2)
    ch.level(79.3, 10, 38, DISP, 'target ứng viên', pos='r', dy=-6, sw=1.2)
    ch.candles(cs)
    ch.lab(29.5, 86.5, 'MỘT chân sóng:\ndisplacement + CHoCH + FVG', dy=0, color=CHC, size=10.5)
    ch.lab(27, 54.6, 'liquidity event', dx=-8, dy=24, color=SWP, anchor='end')
    ch.lab(34, 69.2, 'entry', dx=8, dy=14, color=DISP, anchor='start')
    x = 642; w = 330
    f.card(x, y1, w, 660 - y1 - 46, 'Thứ tự chính xác hơn')
    rows = [(1, BOSC, 'Bối cảnh trước', 'D1 cho hướng, H1 cho POI. Không có hai điều này → dừng.'),
            (2, SWP, 'Sự kiện thanh khoản', 'Thường (không bắt buộc) có một cú quét tại POI.'),
            (3, CHC, 'Một chân sóng có lực', 'Trong chân sóng này: displacement (cách đi), CHoCH (mức bị phá), FVG (dấu vết) — gần như cùng lúc.'),
            (4, FVGC, 'Chờ hồi', 'Giá có thể không quay lại. Không đuổi.'),
            (5, DISP, 'Entry, stop, target', 'Stop bên kia đáy quét; target là thanh khoản phía trước; R:R phải đủ.')]
    side_steps(f, x + 14, y1 + 50, w - 28, rows)
    f.foot('Ở bước 3, CHoCH là BẰNG CHỨNG cấu trúc; quyết định vào lệnh thuộc về bước 4–5. Trình tự này là giả thuyết của mô hình, cần backtest.')
    return f.save()


# ------------------------------------------------------------------ 42 identification framework
def fig42():
    f = F(42, 'Quy-Trinh-Nhan-Dien-12-Buoc', 'Quy trình nhận diện CHoCH trong 12 bước — mỗi bước có lý do',
          'Ba nhóm: KHAI BÁO (trước khi nhìn cú phá), SỰ KIỆN (cú phá), PHÂN LOẠI (sau cú phá). Thứ tự có chủ ý: khai báo trước để không chọn swing theo kết quả.', h=760)
    y0 = f.top + 4
    groups = [('KHAI BÁO', BOSC, [('Cấu trúc hiện tại', 'Khung nào? Lớp nào? Đang tăng/giảm/không rõ.'),
                                  ('Hành vi hiện tại', 'Chân đẩy và chân hồi trông thế nào? Có suy yếu không?'),
                                  ('Swing liên quan', 'Đỉnh/đáy nào ĐÃ được xác nhận trước thời điểm này?'),
                                  ('Protected high/low', 'Gốc của chân sóng tạo BOS gần nhất.'),
                                  ('Internal hay external', 'Mức đó thuộc lớp nào so với range lớn?')]),
              ('SỰ KIỆN', CHC, [('Bối cảnh thanh khoản', 'Có quét đỉnh/đáy nào phía đối diện không?'),
                                ('Cú phá', 'Thân nến đóng ngoài protected swing? Hay chỉ râu?'),
                                ('Displacement', 'Chân sóng nhanh, thân to, một chiều?'),
                                ('FVG', 'Có khoảng trống để lại không? (ghi riêng)'),
                                ('Follow-through', 'Vài nến sau có đóng ngược trở lại không? (G2)')]),
              ('PHÂN LOẠI', DISP, [('Bối cảnh HTF', 'Có ở POI? Thuận hay ngược khung lớn? Tin tức?'),
                                   ('Kết luận', 'Valid CHoCH · Weak CHoCH · Không phải CHoCH — kèm bậc G và known-at.')])]
    y = y0 + 4; n = 1
    for gi, (gname, c, items) in enumerate(groups):
        f.r(28, y, 944, len(items) * 46 + 12, fill=c, stroke=c, sw=1, rx=12, op=0.05, sop=0.4)
        f.t(46, y + 24, gname, 12, True, c)
        for k, (a, b) in enumerate(items):
            yy = y + 8 + k * 46
            f.r(170, yy, 790, 40, fill=CARD, stroke=BORDER, sw=1, rx=8)
            f.badge(192, yy + 20, n, c)
            f.t(212, yy + 25, a, 12.5, True, c)
            f.t(420, yy + 25, b, 12, False, INK, bx=(418, 958))
            n += 1
        y += len(items) * 46 + 22
    f.foot('Bước 1–5 phải xong TRƯỚC khi nến phá xuất hiện. Nếu bạn chỉ xác định được protected swing sau khi thấy cú phá, đó là dấu hiệu hindsight.')
    return f.save()


# ------------------------------------------------------------------ 43 decision tree
def fig43():
    f = F(43, 'Cay-Quyet-Dinh-CHoCH', 'Cây quyết định: Valid CHoCH · Weak CHoCH · Không phải CHoCH',
          'Đọc từ trên xuống. Mỗi câu hỏi chỉ dùng thông tin đã có tại lúc nến đóng cửa. Các ô xám ở bên phải là chỗ “dừng lại”.', h=720, tag='DECISION TREE')
    y0 = f.top + 6
    Q = [('Đã khai báo khung + lớp + trạng thái (tăng/giảm)?', 'Không → không xét CHoCH (đi ngang / chưa rõ)'),
         ('Mức bị phá là swing ĐÃ XÁC NHẬN trước cú phá?', 'Không → chưa có mức tham chiếu'),
         ('Cú phá NGƯỢC trạng thái đã khai báo?', 'Không → đó là BOS (thuận chiều)'),
         ('THÂN nến đóng ngoài mức (không chỉ râu)?', 'Không → “chạm vạch”: chờ, có thể là quét'),
         ('Mức đó là PROTECTED swing của lớp đã khai báo?', 'Không → break internal / micro: ghi ở lớp nhỏ hơn'),
         ('Cú phá có displacement?', 'Không → WEAK CHoCH (G0): ghi lại, chờ thêm'),
         ('Bối cảnh: đúng POI HTF, không tin tức, không ngược khung lớn vô cớ?', 'Không → VALID nhưng KHÔNG hành động (bối cảnh xấu)')]
    y = y0
    for k, (q, no) in enumerate(Q):
        box(f, 150, y, 470, 50, q, INK, 12, fill=CARD)
        f.badge(128, y + 25, k + 1, BOSC)
        f.arrow(620, y + 25, 664, y + 25, BAD, 1.6, size=6); f.t(642, y + 18, 'không', 10, True, BAD, 'middle')
        f.r(668, y + 4, 304, 42, fill='#F3F4F6', stroke=MUTE, sw=1, rx=8)
        f.p(680, y + 21, no, 284, 11.3, '#374151')
        f.arrow(385, y + 50, 385, y + 66, GOOD, 1.6, size=6); f.t(394, y + 62, 'có', 10, True, GOOD)
        y += 70
    box(f, 150, y, 470, 56, 'VALID CHoCH (G1) — bằng chứng cấu trúc. Chưa phải lệnh: chuyển sang mô hình vào lệnh (hồi về FVG/OB, stop, target).', CHC, 12, fill=PINKBG)
    f.foot('Sau nút cuối, cập nhật bậc khi có thông tin mới: G2 (không bị đóng ngược trong vài nến) và G3 (HL/LH mới + BOS). Bản Mermaid chỉnh sửa được nằm trong note, mục 24.')
    return f.save()


# ------------------------------------------------------------------ case helper
def case(num, slug, title, sub, draw, steps, verdict, vcolor, h=640, foot=''):
    f = F(num, slug, title, sub, h=h, tag='CASE STUDY')
    y0 = f.top + 4; H = h - y0 - 46
    f.card(28, y0, 560, H)
    draw(f, 44, y0 + 26, 528, H - 46)
    x = 600; w = 372
    f.card(x, y0, w, H, None)
    f.pill(x + 14, y0 + 14, verdict, vcolor, 11)
    yy = y0 + 58
    for lab, txt in steps:
        f.t(x + 16, yy, lab, 11, True, SUB)
        yy = f.p(x + 16, yy + 16, txt, w - 32, 11.6) + 6
    f.foot(foot)
    return f.save()


def fig44():
    def d(f, x, y, w, h):
        cs, tn = bull_seq()
        ch = Chart(f, x, y, w, h, 50, 88, len(cs) + 1)
        for (i, lo, hi) in fvgs(cs, 28, 32):
            if i == 30: ch.zone(29, 38, lo, hi, FVGC, None, 'tl', '4,3', 0.14)
        ch.level(72.3, 18, 33, PROT, 'protected high', pos='l', dy=-6, sw=1.4)
        ch.level(56.2, 22, 28, SWP, None, dash='4,3', sw=1.1)
        ch.candles(cs)
        for i, p, t_, c, dy in [(10, 79.3, 'LH1', DN, -8), (18, 72.3, 'LH2', DN, -22), (22, 56.2, 'LL', DN, 15), (27, 54.6, 'quét', SWP, 15), (31, 77.3, 'CHoCH G1', CHC, -8), (34, 69.2, 'HL mới', DISP, 15), (37.4, 84.3, 'BOS ↑ = G3', BOSC, -8)]:
            ch.lab(i, p, t_, dy=dy, color=c)
    steps = [('BỐI CẢNH', 'H1 đang hồi giảm vào POI H1 (discount của dealing range D1 tăng). Đây là giả định của case.'),
             ('CẤU TRÚC M5', 'Giảm: LH1 → LL → LH2 → LL. Trạng thái khai báo: GIẢM, lớp protected.'),
             ('CHỌN SWING', 'LH2 = gốc của chân giảm đã thủng đáy trước → protected high.'),
             ('CHUỖI GIÁ', 'Quét đáy LL → 4 nến tăng thân to → nến thứ 4 đóng trên LH2, để lại FVG.'),
             ('PHÂN LOẠI', 'Valid CHoCH G1 tại lúc đóng nến. G2 khi hồi giữ trên FVG; G3 khi vượt đỉnh CHoCH.'),
             ('HÀM Ý', 'Ứng viên Long theo ICT 2022 khi giá hồi vào FVG; stop dưới đáy quét.'),
             ('VÔ HIỆU', 'Thân nến đóng dưới đáy quét 54.6 → câu chuyện tăng sai.')]
    return case(44, 'Case-A-Bullish-CHoCH-Hop-Le', 'Case A — Bullish CHoCH hợp lệ', 'Cấu trúc giảm → quét → protected high bị phá bằng displacement → cấu trúc tăng thành hình.', d, steps, 'Valid CHoCH → G3', GOOD,
                foot='Sơ đồ dựng, số minh họa. Nhãn “HL mới” và “BOS ↑” là thông tin TƯƠNG LAI so với lúc nến CHoCH đóng cửa.')


def fig45():
    def d(f, x, y, w, h):
        cs, tn = bear_seq()
        ch = Chart(f, x, y, w, h, 52, 90, len(cs) + 1)
        for (i, lo, hi) in fvgs(cs, 28, 32, bull=False):
            if i == 30: ch.zone(29, 38, lo, hi, FVGC, None, 'tl', '4,3', 0.14)
        ch.level(67.7, 18, 33, PROT, 'protected low', pos='l', dy=16, sw=1.4)
        ch.level(83.8, 22, 28, SWP, None, dash='4,3', sw=1.1)
        ch.candles(cs)
        for i, p, t_, c, dy in [(10, 60.7, 'HL1', UP, 15), (18, 67.7, 'HL2', UP, 28), (22, 83.8, 'HH', UP, -8), (27, 85.4, 'quét', SWP, -8), (31, 62.7, 'CHoCH G1', CHC, 15), (34, 70.8, 'LH mới', DN, -8), (37.4, 55.7, 'BOS ↓ = G3', BOSC, 15)]:
            ch.lab(i, p, t_, dy=dy, color=c)
    steps = [('BỐI CẢNH', 'D1 đang ở premium của range, giá tới POI giảm của H1 (giả định của case).'),
             ('CẤU TRÚC', 'Tăng: HL1 → HH → HL2 → HH. Trạng thái khai báo: TĂNG, lớp protected.'),
             ('CHỌN SWING', 'HL2 = gốc của chân tăng đã vượt đỉnh trước → protected low.'),
             ('CHUỖI GIÁ', 'Quét đỉnh HH → nến giảm thân to → thân nến đóng dưới HL2, để lại FVG.'),
             ('PHÂN LOẠI', 'Valid CHoCH G1; lên G2 khi hồi bị từ chối dưới FVG; G3 khi thủng đáy CHoCH.'),
             ('HÀM Ý', 'Ứng viên Short khi giá hồi vào FVG; stop trên đỉnh quét.'),
             ('VÔ HIỆU', 'Thân nến đóng trên đỉnh quét → câu chuyện giảm sai.')]
    return case(45, 'Case-B-Bearish-CHoCH-Hop-Le', 'Case B — Bearish CHoCH hợp lệ', 'Cấu trúc tăng → quét đỉnh → protected low bị phá bằng displacement → cấu trúc giảm thành hình.', d, steps, 'Valid CHoCH → G3', GOOD,
                foot='Ảnh gương của case A. Sơ đồ dựng, số minh họa.')


def zzcase(pts, lvls, labs, lo, hi, zones=()):
    def d(f, x, y, w, h):
        n = max(i for i, p in pts) + 1
        ch = Chart(f, x, y, w, h, lo, hi, n)
        for z in zones: ch.zone(*z)
        for (p, a, b, c, lab, pos, dy, dash) in lvls: ch.level(p, a, b, c, lab, pos=pos, dy=dy, dash=dash, sw=1.4)
        zz(ch, pts, INK, 2.4); dots(ch, pts[1:], INK, 3.2)
        for (i, p, t_, c, dy, dx, an) in labs: ch.lab(i, p, t_, dy=dy, dx=dx, color=c, anchor=an)
    return d


def fig46():
    pts = [(0, 30), (2, 56), (2.6, 50), (3.3, 54), (4, 47), (5.6, 70), (6.3, 64), (6.8, 67), (7.5, 61), (9, 82), (9.6, 77), (11, 94)]
    d = zzcase(pts, [(30, 0, 10.4, PROT, 'protected low external (H1)', 'r', -6, '6,4'), (50, 2.6, 4.4, CHC, None, 'r', 0, '3,3'), (64, 6.3, 7.9, CHC, None, 'r', 0, '3,3')],
               [(4, 47, '“CHoCH” internal', CHC, 15, 0, 'middle'), (7.5, 61, '“CHoCH” internal', CHC, 15, 0, 'middle'), (5.6, 70, 'HH', BOSC, -8, 0, 'middle'), (9, 82, 'HH', BOSC, -8, 0, 'middle'), (11, 94, 'HH', BOSC, -8, -6, 'end')], 24, 100)
    steps = [('BỐI CẢNH', 'H1 tăng mạnh. Khung nhìn: M15 bên trong chân tăng H1.'),
             ('CẤU TRÚC', 'Lớp external: tăng. Lớp internal: mỗi đợt hồi có đỉnh/đáy nhỏ.'),
             ('CHỌN SWING', 'Đáy 50 và 64 là đáy NỘI BỘ của đợt hồi, không phải gốc của BOS H1.'),
             ('CHUỖI GIÁ', 'Mỗi lần hồi, giá thủng một đáy nhỏ → nhiều indicator in “CHoCH”. Sau đó giá vượt đỉnh mới.'),
             ('PHÂN LOẠI', 'CHoCH internal — đúng ở lớp nhỏ, VÔ NGHĨA ở lớp external.'),
             ('HÀM Ý', 'Không Short. Ngược lại: các CHoCH ↑ ở cuối mỗi đợt hồi mới là chỗ cần chú ý.'),
             ('VÔ HIỆU', 'Chỉ khi protected low external bị đóng nến xuyên.')]
    return case(46, 'Case-C-False-CHoCH-Internal', 'Case C — “CHoCH” giả: phá internal, xu hướng external vẫn chạy', 'Nhãn CHoCH đúng về mặt kỹ thuật ở lớp nhỏ nhưng bị đọc sai thành đảo chiều.', d, steps, 'Not CHoCH (ở lớp external)', BAD,
                foot='Đây là lỗi phổ biến nhất khi dùng indicator CHoCH tự động: không khai báo lớp nên mọi cú phá nhỏ đều trông như đảo chiều.')


def fig47():
    pts = [(0, 80), (1, 66), (1.8, 72), (2.8, 58), (3.6, 65), (4.6, 56), (5.4, 61), (6.2, 59), (7.4, 74), (8.1, 69), (9.2, 79)]
    d = zzcase(pts, [(65, 3.6, 8.6, PROT, 'protected high', 'r', -6, '6,4'), (56, 4.6, 6.6, SWP, 'đáy LL — chưa bị quét', 'r', 15, '3,3')],
               [(6.2, 59, 'đáy cao hơn\n(không quét)', SUB, 26, 0, 'middle'), (7.4, 74, 'CHoCH (displacement)', CHC, -8, -4, 'end'), (9.2, 79, 'BOS ↑', BOSC, -8, -4, 'end')], 50, 86,
               zones=[(6.6, 7.0, 63, 69, FVGC, None, 'tl', None, 0.2)])
    steps = [('BỐI CẢNH', 'Giá ở POI H1, phiên London. Không có cú quét rõ ràng.'),
             ('CẤU TRÚC', 'Giảm, protected high = 65.'),
             ('CHUỖI GIÁ', 'Giá tạo một đáy CAO HƠN đáy LL (không quét), rồi đi lên mạnh qua 65.'),
             ('PHÂN LOẠI', 'Valid CHoCH G1 theo định nghĩa. Thiếu một bằng chứng bối cảnh (quét).'),
             ('DIỄN GIẢI', 'Đáy cao hơn có thể cho thấy bên bán yếu dần. Hoặc đáy LL vẫn còn là “nam châm” chưa được lấy — rủi ro giá quay xuống quét nó (kịch bản D, hình 25).'),
             ('HÀM Ý', 'Hợp lệ để theo dõi. Có nên trade hay không tùy quy tắc mô hình của bạn: đó là câu hỏi backtest (HYP-CHOCH-002).'),
             ('VÔ HIỆU', 'Đóng nến dưới đáy cao hơn 59; nguy hiểm hơn nếu thủng 56.')]
    return case(47, 'Case-D-CHoCH-Khong-Co-Quet', 'Case D — CHoCH không có liquidity sweep', 'Hợp lệ về cấu trúc. Câu hỏi là thiếu cú quét làm mất bao nhiêu giá trị — chưa ai đo cho bạn.', d, steps, 'Valid CHoCH, thiếu bối cảnh', WARN,
                foot='[FRAMEWORK-DEPENDENT]: nhiều bản ICT 2022 yêu cầu quét trước MSS; định nghĩa CHoCH thì không. Đừng trộn hai thứ này.')


def fig48():
    pts = [(0, 80), (1, 66), (1.8, 72), (2.8, 58), (3.6, 65), (4.4, 53), (5.4, 62.5), (6.2, 57), (6.8, 60), (8, 46)]
    d = zzcase(pts, [(65, 3.6, 7.9, PROT, 'protected high', 'r', -6, '6,4'), (58, 2.8, 7.9, SWP, 'đáy cũ', 'r', 15, '3,3')],
               [(4.4, 53, 'quét', SWP, 15, 0, 'middle'), (5.4, 62.5, 'bật lên nhưng\nkhông tới 65', WARN, -10, 0, 'middle'), (8, 46, 'giảm tiếp', DN, 15, -6, 'end')], 40, 86)
    steps = [('BỐI CẢNH', 'Giá giảm vào vùng có nhiều đáy cũ.'),
             ('CHUỖI GIÁ', 'Râu nến thủng đáy cũ 58 rồi đóng lại phía trên: một cú quét. Giá bật lên khá mạnh…'),
             ('ĐIỂM MẤU CHỐT', '…nhưng dừng ở 62.5, dưới protected high 65. Không có CHoCH.'),
             ('PHÂN LOẠI', 'Liquidity sweep KHÔNG kèm structural shift. Trạng thái vẫn là GIẢM.'),
             ('DIỄN GIẢI', 'Lệnh dừng lỗ có thể đã được khớp, nhưng lực mua sau đó không đủ để phá mức mà cấu trúc giảm dựa vào.'),
             ('HÀM Ý', 'Không Long chỉ vì “đã quét”. Chờ CHoCH, hoặc chấp nhận giảm tiếp.'),
             ('BÀI HỌC', 'Quét là ĐIỀU KIỆN ĐẦU VÀO có thể có của một đảo chiều, không phải chính đảo chiều.')]
    return case(48, 'Case-E-Quet-Khong-CHoCH', 'Case E — Liquidity sweep nhưng KHÔNG có CHoCH', 'Một sự kiện thanh khoản không đồng nghĩa với thay đổi cấu trúc.', d, steps, 'Sweep only — không CHoCH', BAD,
                foot='Đây là lý do protocol của bạn đặt câu hỏi “liquidity sweep có tạo ra CHoCH không?”. Câu trả lời: không tự động.')


def fig49():
    def d(f, x, y, w, h):
        hpts = [(0, 30), (2, 62), (3, 50), (5, 84), (6.4, 66), (8, 92)]
        ch = Chart(f, x, y, w, h * 0.42, 24, 98, 8.6)
        f.t(x, y + 4, 'H1 (lớp lớn)', 11, True, BOSC)
        ch.zone(5, 6.6, 64, 86, CHC, None, 'tl', '4,3', 0.07)
        zz(ch, hpts, INK, 2.3); dots(ch, hpts[1:], INK, 3)
        ch.level(50, 3, 7.4, PROT, 'protected low H1', pos='r', dy=15, sw=1.3)
        y2 = y + h * 0.5
        f.t(x, y2 + 4, 'M5 bên trong ô tím (đợt hồi H1)', 11, True, CHC)
        mpts = [(0, 72), (1, 84), (1.5, 80), (2, 82.5), (2.6, 77), (3.2, 80), (3.9, 73), (4.4, 76), (5, 69.5), (5.5, 72), (6, 66.5), (7, 75), (7.6, 72.5), (8.6, 80)]
        m = Chart(f, x, y2 + 14, w, h * 0.46, 63, 88, 9)
        zz(m, mpts, INK, 2.1); dots(m, mpts[1:], INK, 2.6)
        m.lab(2.6, 77, 'CHoCH ↓ M5', dy=15, color=CHC, size=10)
        m.level(72, 5.5, 8, CHC, None, dash='3,3', sw=1.2)
        m.lab(7, 75, 'CHoCH ↑ M5', dx=-6, dy=-8, color=CHC, size=10, anchor='end')
        m.lab(6, 66.5, 'đáy hồi', dy=15, color=DISP, size=10)
    steps = [('BỐI CẢNH', 'H1 tăng, protected low H1 = 50 còn nguyên. Giá đang hồi.'),
             ('M5', 'Đầu đợt hồi: CHoCH ↓ M5 (đổi lớp nhỏ sang giảm). Cuối đợt hồi: CHoCH ↑ M5 (đổi lại sang tăng).'),
             ('PHÂN LOẠI', 'Cả hai đều là CHoCH internal. Không cái nào đổi H1.'),
             ('REVERSAL hay PULLBACK?', 'Pullback — vì protected low H1 chưa bị phá. Muốn nói “reversal H1” cần H1 CHoCH ↓ (thủng 50) + LH mới + BOS ↓ trên H1.'),
             ('HÀM Ý', 'CHoCH ↓ M5 ở đầu đợt hồi: không phải lệnh Short. CHoCH ↑ M5 ở cuối đợt hồi, tại POI: ứng viên Long thuận H1.'),
             ('VÔ HIỆU', 'Đóng nến H1 dưới 50.')]
    return case(49, 'Case-F-Internal-CHoCH-Trong-Trend-HTF', 'Case F — CHoCH internal bên trong xu hướng HTF', 'Phân biệt pullback với reversal bằng cách hỏi: protected swing của KHUNG NÀO đã bị phá?', d, steps, 'Internal CHoCH — pullback', TEAL, h=660,
                foot='Cùng một M5 CHoCH ↑ có thể là “kết thúc pullback” (thuận H1) hoặc “hồi trong downtrend H1” (ngược H1). Khung lớn quyết định cách đọc.')


def fig50():
    pts = [(0, 56), (0.8, 66), (1.6, 55), (2.4, 65), (3.2, 56.5), (4, 67), (4.8, 54), (5.6, 66.5), (6.4, 55.5), (7.2, 64), (8.2, 57)]
    d = zzcase(pts, [(66.3, 0.8, 8, STR, 'đỉnh range', 'r', -6, '4,3'), (55, 1.6, 8, STR, 'đáy range', 'r', 15, '4,3')],
               [(4, 67, 'CHoCH ↑?', CHC, -8, 0, 'middle'), (4.8, 54, 'CHoCH ↓?', CHC, 15, 0, 'middle'), (5.6, 66.5, 'CHoCH ↑?', CHC, -8, 0, 'middle'), (6.4, 55.5, '…', CHC, 15, 0, 'middle')], 46, 74,
               zones=[(0.6, 8.2, 54, 67.5, STR, None, 'tl', '4,3', 0.05)])
    steps = [('BỐI CẢNH', 'Giá đi ngang nhiều phiên, biên range rõ ràng.'),
             ('CẤU TRÚC', 'Không có trạng thái: đỉnh/đáy chồng lên nhau.'),
             ('CHUỖI GIÁ', 'Mỗi cạnh range bị phá rồi quay lại. Indicator in CHoCH lên, CHoCH xuống liên tục.'),
             ('PHÂN LOẠI', 'Không phải CHoCH theo note này — không có “character” nào để đổi (bước 1 của cây quyết định).'),
             ('NÊN ĐỌC THẾ NÀO', 'Như một range: thanh khoản ở hai cạnh, các cú quét. Thay đổi thật là khi giá RỜI range bằng displacement và được chấp nhận bên ngoài.'),
             ('HÀM Ý', 'Đứng ngoài với tư cách “CHoCH trader”. Mô hình khác (range) có thể có lệnh.')]
    return case(50, 'Case-G-CHoCH-Trong-Vung-Di-Ngang', 'Case G — CHoCH trong vùng đi ngang', 'Nơi CHoCH gây nhiễu nhiều nhất.', d, steps, 'Not CHoCH — không có trạng thái', BAD,
                foot='Gợi ý backtest: đếm số CHoCH mỗi ngày trên lớp internal; ngày đi ngang thường có nhiều nhãn hơn hẳn ngày có xu hướng. [HYPOTHESIS]')


def fig51():
    def d(f, x, y, w, h):
        cs, tn = gen(70, [(64, 3, 'c'), (67.5, 3, 'c'), (61, 3, 'c'), (64.5, 3, 'c'), (58.5, 3, 'c'), (61.2, 4, 'g'), (59.6, 2, 'g'), (65.8, 6, 'g'), (64, 2, 'g')], u=0.8, seed=31)
        ch = Chart(f, x, y, w, h, 54, 72, len(cs) + 6)
        ch.level(64.8, 9, len(cs) + 4, PROT, 'protected high', pos='r', dy=-6, sw=1.4)
        ch.candles(cs)
        ch.lab(len(cs) - 3, 66.3, 'đóng nhỉnh trên\n(nến nhỏ, chồng nhau)', dx=-6, dy=-12, color=WARN, anchor='end')
        ch.fog(len(cs) + 0.4, 'G2?')
        ch.lab(tn[4][0], tn[4][1], 'không quét', dy=15, color=SUB)
    steps = [('BỐI CẢNH', 'Giá ở POI H1. Cấu trúc M5 giảm, protected high = 64.8.'),
             ('CHUỖI GIÁ', 'Không quét. Giá “bò” lên bằng chuỗi nến nhỏ chồng lên nhau, rồi một nến đóng nhỉnh trên 64.8.'),
             ('PHÂN LOẠI', 'CHoCH G0 (weak). Có thay đổi trạng thái theo định nghĩa, nhưng không có displacement.'),
             ('BẰNG CHỨNG CÓ', 'Trạng thái đổi; giá đang ở POI.'),
             ('BẰNG CHỨNG THIẾU', 'Lực (displacement), FVG để vào lệnh, cú quét, độ chấp nhận.'),
             ('HÀM Ý', 'Không vào lệnh tại G0. Chờ: (a) lên G2 rồi một chân sóng có lực tạo vùng vào lệnh; hoặc (b) bị đóng ngược → bỏ.'),
             ('VÔ HIỆU', 'Đóng nến trở lại dưới 64.8 trong cửa sổ đã khai báo.')]
    return case(51, 'Case-H-CHoCH-Displacement-Yeu', 'Case H — CHoCH với displacement yếu', 'Hợp lệ nhưng ít thông tin. Quyết định đúng thường là “chờ thêm”, không phải “vào” hay “bỏ hẳn”.', d, steps, 'Weak CHoCH (G0) — chờ', WARN,
                foot='Có giả thuyết cho rằng CHoCH không displacement thất bại nhiều hơn. Lưu ý từ note 21: so sánh phải dùng kỳ vọng E[R], không chỉ tỷ lệ thất bại.')


# ------------------------------------------------------------------ 52 mistakes
def fig52():
    f = F(52, 'Muoi-Sau-Loi-Thuong-Gap', 'Mười sáu lỗi thường gặp với CHoCH — và cách sửa trong một dòng',
          'Đỏ = điều hay làm. Xanh = điều nên làm. Phân tích đầy đủ (vì sao xảy ra, vì sao sai) ở mục 27 của note.', h=760)
    y0 = f.top + 4
    M = [('Gọi mọi cú phá swing là CHoCH', 'Chỉ protected swing của lớp đã khai báo'), ('Nhầm CHoCH với BOS', 'Hỏi: phá THUẬN hay NGƯỢC trạng thái?'),
         ('Nhầm CHoCH với MSS', 'Dùng thang G0–G3 thay vì cãi tên'), ('Không tách internal/external', 'Khai báo lớp trước khi nhìn'),
         ('Không xác định protected', 'Gốc chân sóng tạo BOS gần nhất'), ('Chọn swing theo hindsight', 'Swing phải xác nhận TRƯỚC cú phá'),
         ('Râu phá = CHoCH', 'Râu = chạm vạch; chờ thân nến đóng'), ('Thân đóng qua = luôn CHoCH', 'Còn phải đúng mức, đúng lớp'),
         ('Bỏ qua displacement', 'Ghi G0/G1 riêng cho mọi CHoCH'), ('Coi quét là bắt buộc', 'Quét là bối cảnh, ghi riêng'),
         ('CHoCH = đảo chiều', 'CHoCH = câu hỏi; đảo chiều cần G3 lớp lớn'), ('M5 CHoCH đổi Daily Bias', 'Mỗi khung chỉ đổi chính nó'),
         ('Vào lệnh ngay khi CHoCH', 'Chờ vùng vào lệnh của mô hình'), ('Bỏ qua HTF POI', 'Location trước, evidence sau'),
         ('Chọn cấu trúc hợp với bias', 'Khai báo cấu trúc trước khi có bias'), ('Đổi định nghĩa sau kết quả', 'Khóa định nghĩa trước mỗi đợt backtest')]
    for k, (bad, good) in enumerate(M):
        r, c = divmod(k, 4)
        x = 28 + c * 238; y = y0 + r * 150; w = 228
        f.r(x, y, w, 140, fill=CARD, stroke=BORDER, rx=10)
        f.badge(x + 20, y + 20, k + 1, INK, 10, 10.5)
        f.t(x + 38, y + 25, 'Sai', 10.5, True, BAD)
        f.p(x + 14, y + 46, bad, w - 28, 12.2, BAD, bold=True)
        f.ln(x + 14, y + 86, x + w - 14, y + 86, BORDER, 1)
        f.p(x + 14, y + 106, good, w - 28, 12, GOOD)
    f.foot('Lỗi 15 và 16 là hai lỗi nguy hiểm nhất cho backtest: chúng làm kết quả trông tốt hơn thực tế mà người làm không hề nhận ra.')
    return f.save()


# ------------------------------------------------------------------ 53 what we know
def fig53():
    f = F(53, 'Dieu-Ta-Biet-va-Dieu-Ta-Gia-Dinh', 'Điều ta thật sự biết về CHoCH — và điều ta đang giả định',
          'Càng sang phải, độ chắc chắn càng thấp. Một câu nói không đi lên được cột bên trái chỉ vì nó phổ biến trong cộng đồng ICT.', h=640)
    y0 = f.top + 4
    cols = [('QUAN SÁT ĐƯỢC', GOOD, ['Giá tạo đỉnh/đáy; chuỗi HH–HL hoặc LH–LL', 'Một thân nến đóng ngoài một mức', 'Chân sóng nhanh/chậm, có/không để lại FVG', 'Có râu đi qua đỉnh/đáy cũ']),
            ('ĐỊNH NGHĨA / QUY ƯỚC', BOSC, ['Tên CHoCH, BOS, MSS', 'Protected = gốc chân tạo BOS gần nhất', 'Internal vs external', 'Thang G0–G3, cửa sổ chấp nhận']),
            ('DIỄN GIẢI HỢP LÝ', WARN, ['Bên mua/bán không bảo vệ được mức', 'Lệnh dừng lỗ đã bị kích hoạt', 'Character của dòng lệnh đang đổi']),
            ('CHƯA CHẮC — CẦN ĐO', BAD, ['Quét trước làm CHoCH tốt hơn', 'Displacement làm CHoCH tốt hơn', 'CHoCH tại POI tốt hơn ngoài POI', 'CHoCH có lợi thế giao dịch nói chung', '“Smart Money quyết định đảo chiều”'])]
    for k, (ttl, c, items) in enumerate(cols):
        x = 28 + k * 238; w = 228
        f.r(x, y0, w, 470, fill=CARD, stroke=c, sw=1.6, rx=12)
        f.r(x, y0, w, 46, fill=c, stroke=None, rx=12, op=0.12)
        f.t(x + w / 2, y0 + 29, ttl, 12.5, True, c, 'middle')
        yy = y0 + 76
        for it in items:
            f.t(x + 16, yy, '•', 12, True, c); yy = f.p(x + 28, yy, it, w - 42, 12.2) + 12
    f.arrow(60, y0 + 492, 940, y0 + 492, SUB, 1.6)
    f.t(60, y0 + 512, 'chắc chắn', 11, True, GOOD); f.t(940, y0 + 512, 'cần bằng chứng', 11, True, BAD, 'end')
    f.foot('Bảng đầy đủ với từng claim và mức kết luận được ở mục 28 của note.')
    return f.save()


# ------------------------------------------------------------------ 54 final mental model
def fig54():
    f = F(54, 'Mental-Model-Cuoi-Cung', 'Mental model cuối cùng: CHoCH trên một trang',
          'Đọc từ trái sang phải. Dòng trên: câu cho bé 5 tuổi. Dòng dưới: câu kỹ thuật.', h=600, tag='TÓM TẮT')
    y0 = f.top + 6
    S = [('1. Có thói quen', 'Nam leo “tiến ba lùi một”.', 'Khai báo trạng thái: khung, lớp, tăng/giảm.', BOSC),
         ('2. Có bậc lấy đà', 'Bậc giúp Nam leo lần gần nhất.', 'Protected swing = gốc chân tạo BOS gần nhất.', PROT),
         ('3. Thói quen bị phá', 'Nam đứng hẳn xuống dưới bậc lấy đà.', 'Thân nến ĐÓNG ngược trạng thái qua protected swing (G0).', CHC),
         ('4. Phá mạnh hay yếu?', 'Đạp tung cửa hay hé từng chút?', 'Displacement (G1), FVG, quét trước đó: chất lượng, không phải định nghĩa.', SWP),
         ('5. Ở đâu?', 'Đúng nhà chưa?', 'HTF POI, premium/discount, khung lớn — quyết định có nên đọc tiếp.', TEAL),
         ('6. Rồi sao?', 'Leo tiếp? Nghỉ? Đi xuống?', 'G2 (đứng vững) → G3 (HL/LH mới + BOS). Chỉ lúc đó mới bàn đến “xu hướng mới”.', GOOD)]
    bw = 151
    for k, (t_, eli, tech, c) in enumerate(S):
        x = 28 + k * (bw + 7.6)
        f.r(x, y0, bw, 380, fill=CARD, stroke=c, sw=1.6, rx=12)
        f.r(x, y0, bw, 50, fill=c, stroke=None, rx=12, op=0.12)
        f.p(x + 10, y0 + 22, t_, bw - 20, 12.5, c, bold=True, lh=1.25)
        f.t(x + 10, y0 + 76, 'Cho bé', 10.5, True, SUB)
        f.p(x + 10, y0 + 94, eli, bw - 20, 12, INK, italic=True)
        f.ln(x + 10, y0 + 170, x + bw - 10, y0 + 170, BORDER, 1)
        f.t(x + 10, y0 + 192, 'Kỹ thuật', 10.5, True, SUB)
        f.p(x + 10, y0 + 210, tech, bw - 20, 11.6)
    f.note(28, y0 + 396, 944, 'CHoCH trả lời câu hỏi: “Cái thói quen mà cấu trúc này dựa vào có vừa bị phá ở đúng chỗ quan trọng không?” Nó KHÔNG trả lời: “Giá sẽ đi đâu?”, “Ai đang mua?”, hay “Có nên vào lệnh không?”.', CHC, 'Một câu để nhớ', 13)
    f.foot('Mọi thứ trong hình này đã được giải thích chi tiết trong note. Nếu một ô ở đây chưa rõ, quay lại mục tương ứng.')
    return f.save()


ALL = [fig41, fig42, fig43, fig44, fig45, fig46, fig47, fig48, fig49, fig50, fig51, fig52, fig53, fig54]
if __name__ == '__main__':
    sel = sys.argv[1:]
    for fn in ALL:
        if not sel or fn.__name__[3:] in sel:
            print(fn())
