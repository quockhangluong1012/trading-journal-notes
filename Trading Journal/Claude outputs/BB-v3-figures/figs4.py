# -*- coding: utf-8 -*-
from bbdraw import *
from figs1 import base_chart, TX, zig, OBSEQ, TEAL
from figs2 import mini, nums, X2, X3, X4, W2, W3, W4, MIDLEG
from figs3 import rows, PINK

G = '#6B7280'

# ------------------------------------------------------------------ 47 six visible mistakes
def fig47():
    f = Fig(47, 'Sau-Loi-Nhin-Thay-Duoc', 'Sáu lỗi nhận diện nhìn thấy được ngay trên chart',
            'Mỗi ô: hình là cách vẽ SAI (đánh dấu đỏ). Dòng ✗ là suy nghĩ dẫn tới lỗi, dòng ✓ là cách sửa. Danh sách đủ 18 lỗi nằm ở bảng §23.', h=828, tag='LỖI THƯỜNG GẶP')
    y0 = f.top + 6
    it = [('1 · Gọi mọi OB bị thủng là Breaker', 'OB bị đóng xuyên thì là Breaker.', 'Hỏi ba câu: OB ở swing? cực trị cũ? swing bị phá?'),
          ('2 · Nhầm cú quét với cú phá', 'Râu đã vượt đỉnh giữa, coi như đã phá.', 'Chỉ tính khi thân nến ĐÓNG CỬA qua đỉnh giữa.'),
          ('3 · Chọn sai cây nến', 'Breaker là nến giảm ở đáy mới.', 'Bullish Breaker là nến TĂNG ở đỉnh giữa.'),
          ('4 · Vẽ vùng quá rộng', 'Lấy cả cụm nến quanh đỉnh cho chắc.', 'Một cây nến (hoặc chuỗi nến cùng màu liền nhau).'),
          ('5 · Mua ngay khi giá chạm vùng', 'Chạm Breaker là tín hiệu mua.', 'Chạm chỉ là “đến nơi”. Chờ bằng chứng khung nhỏ.'),
          ('6 · Dời vùng sau khi biết kết quả', 'Kéo vùng xuống cho khớp cái râu vừa bật.', 'Khoá vùng lúc xác nhận. Không sửa sau đó.')]
    for k, (tt, bad, good) in enumerate(it):
        x = X3[k % 3]; y = y0 + (k // 3) * 340
        f.card(x, y, W3, 330, tt, tcolor=BAD, tsize=12.8)
        cx, cy, cw_, chh = x + 12, y + 42, W3 - 24, 186
        if k == 0:
            ch = Chart(f, cx, cy, cw_, chh, 48, 88, 17, cw=8); ch.zone(2, 16, 71.6, 75.2, BAD, '“Breaker”?', pos='ar', op=0.14); ch.candles(MIDLEG); ch.level(82, 0, 14, STR, 'đỉnh gốc còn nguyên', pos='l', sw=1, size=9.5)
        elif k == 1:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'wick', n=24, lo=35, hi=80, cw=6.2, small=True, zones=False)
            ch.zone(15, 23, Z_LO, Z_HI, BAD, '“Breaker”?', pos='ur', op=0.14); ch.lab(15, 69.5, 'chỉ là râu', dy=-6, color=BAD, size=9.5)
        elif k == 2:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'base', n=25, lo=35, hi=88, cw=6.2, small=True, zones=False)
            ch.zone(L2 - 1, 24, 41, 50.6, BAD, '“Breaker”?', pos='ur', op=0.14)
            ch.zone(HI, HI, Z_LO, Z_HI, GOOD, op=0, dash=None, sw=1.8); ch.lab(HI, P_H, 'nến đúng', dy=-7, color=GOOD, size=9.5)
        elif k == 3:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'base', n=25, lo=35, hi=88, cw=6.2, small=True, zones=False)
            ch.zone(4, 24, 51, 67.6, BAD, 'vùng quá rộng', pos='ur', op=0.12)
            ch.zone(HI, 24, Z_LO, Z_HI, GOOD, op=0.0, sw=1.4)
        elif k == 4:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'fail', n=26, lo=35, hi=88, cw=6.2, small=True)
            ch.dot(20, 65.4, BAD, 4.5); ch.lab(20, 60.3, 'mua ở đây', dx=0, dy=14, color=BAD, anchor='middle', size=9.5)
        else:
            ch, cs = base_chart(f, cx, cy, cw_, chh, 'base', n=25, lo=35, hi=88, cw=6.2, small=True, zones=False)
            ch.zone(HI, 24, Z_LO, Z_HI, GOOD, 'vùng gốc', pos='ar', op=0.0, sw=1.3); ch.zone(HI, 24, 58, 64.2, BAD, 'vùng đã bị dời', pos='ur', op=0.14)
        f.t(x + 14, y + 256, '✗', 13, True, BAD); f.p(x + 30, y + 256, bad, W3 - 44, 11.8)
        f.t(x + 14, y + 294, '✓', 13, True, GOOD); f.p(x + 30, y + 294, good, W3 - 44, 11.8)
    f.foot('Điểm chung của cả sáu: gọi tên TRƯỚC khi kiểm tra trình tự, hoặc sửa hình SAU khi thấy kết quả. Thuốc chữa chung: ghi lại thời điểm bạn vẽ vùng và lý do, bằng chữ.')
    return f.save()

# ------------------------------------------------------------------ 48 hindsight vs real time
def fig48():
    f = Fig(48, 'Hindsight-vs-Real-Time', 'Cùng một chart: nhìn LẠI thì quá rõ, nhìn TỚI thì toàn dấu hỏi',
            'Bên trái là thứ bạn thấy khi lật lại lịch sử. Bên phải là thứ bạn thật sự có trong tay ngay lúc Breaker vừa được xác nhận. Chỉ bên phải mới là điều kiện giao dịch thật.', h=620, tag='HINDSIGHT')
    y = f.top + 6
    for k in range(2):
        x = X2[k]
        f.card(x, y, W2, 452, 'NHÌN LẠI (ex-post): “Breaker đẹp quá!”' if k == 0 else 'NHÌN TỚI (real-time): nến 17 vừa đóng cửa', tcolor=G if k == 0 else BBC)
        ch, cs = base_chart(f, x + 16, y + 48, W2 - 32, 280, 'base', upto=None if k == 0 else 17, n=25, lo=35, hi=88, cw=9)
        if k == 0:
            ch.ztext(18, 63.6, 'Breaker', BBC, 10); ch.lab(RT, 63.5, 'retest giữ', dy=15, color=GOOD); ch.lab(22.5, 80, 'chạy tới mục tiêu', dx=-14, dy=4, color=GOOD, anchor='end')
            f.p(x + 16, y + 360, 'Mọi thứ khớp: quét đáy, phá đỉnh, quay lại, bật lên. Não tự động kể một câu chuyện liền mạch — và quên rằng lúc đó không ai biết đoạn sau.', W2 - 32, 12.2)
        else:
            ch.fog(17.4)
            f.p(x + 16, y + 360, 'Biết: đủ ba mắt xích → vùng được gọi là Breaker. CHƯA biết: giá có quay lại không, nếu quay lại thì giữ hay thủng. Việc được làm: vẽ vùng, đặt cảnh báo, chờ.', W2 - 32, 12.2)
    f.foot('Phép thử chống hindsight: che nửa phải chart bằng tay rồi tự hỏi “tại nến này, tôi có đủ thông tin để gọi tên vùng chưa? để vào lệnh chưa?”. Hai câu hỏi đó hiếm khi có cùng câu trả lời.')
    return f.save()

# ------------------------------------------------------------------ 49 timeline T1..T9
def fig49():
    f = Fig(49, 'Dong-Thoi-Gian-T1-T9', 'Dòng thời gian T1 → T9: tại mỗi mốc, bạn biết gì và được làm gì',
            'Chart phía trên, bảng phía dưới. Cột nào cũng trả lời ba câu: biết gì — đã được VẼ vùng Breaker chưa — đã được VÀO LỆNH chưa.', h=752, tag='REAL-TIME')
    y0 = f.top + 4
    f.card(28, y0, 944, 300)
    ch, cs = base_chart(f, 46, y0 + 36, 908, 232, lo=35, hi=90, cw=15)
    T = [(7.5, 'T1'), (13.5, 'T2'), (15.5, 'T3'), (16.5, 'T4·T6·T7'), (17.5, 'T5'), (20.5, 'T8'), (21.5, 'T9')]
    for xi, lab in T:
        xx = ch.x + xi * ch.step
        f.ln(xx, y0 + 30, xx, y0 + 290, STR, 1, '4,4'); f.t(xx, y0 + 22, lab, 10.5, True, BBC, 'middle')
    cols = [('T1', 'OB gốc tồn tại', 'Nến tăng ở đỉnh giữa đã rõ (nến bên phải đã đóng).', '✗', '✗'),
            ('T2', 'Giá tiến về OB', 'Đáy cũ đã thủng. Giá đang bật lên phía vùng.', '✗', '✗'),
            ('T3', 'OB bị thử', 'Nến đóng TRONG vùng. Chưa qua đỉnh giữa.', '✗', '✗'),
            ('T4', 'Cấu trúc bị phá', 'Nến đóng TRÊN đỉnh giữa. OB thất bại.', '…', '✗'),
            ('T5', 'Displacement', 'Giá đi tiếp, rời xa vùng.', '…', '✗'),
            ('T6', 'Đánh giá ứng viên', 'Kiểm tra đủ ba mắt xích chưa.', '…', '✗'),
            ('T7', 'Gọi tên Breaker', 'Đủ ba mắt xích. Khoá biên vùng.', '✓', '✗'),
            ('T8', 'Retest', 'Giá quay lại chạm vùng.', '✓', '✗'),
            ('T9', 'Xác nhận vào lệnh', 'Khung nhỏ cho sweep → MSS → FVG (nếu có).', '✓', '✓?')]
    y1 = y0 + 312; cw_ = 944 / 9.0
    f.r(28, y1, 944, 300, fill=CARD, stroke=BORDER, rx=11)
    for k, (t, nm, know, draw, enter) in enumerate(cols):
        x = 28 + k * cw_
        if k: f.ln(x, y1 + 8, x, y1 + 292, BORDER, 1)
        f.pill(x + cw_ / 2, y1 + 12, t, BBC, 11, anchor='middle')
        yy = f.p(x + 7, y1 + 56, nm, cw_ - 14, 11.6, INK, bold=True, anchor='middle', lh=1.28)
        f.p(x + 7, y1 + 96, know, cw_ - 14, 10.6, SUB, anchor='middle', lh=1.36)
        for j, (lab, v) in enumerate((('vẽ Breaker?', draw), ('vào lệnh?', enter))):
            yb = y1 + 196 + j * 50
            f.t(x + cw_ / 2, yb, lab, 10, False, SUB, 'middle')
            col = GOOD if v.startswith('✓') else (BAD if v == '✗' else WARN)
            f.t(x + cw_ / 2, yb + 22, v, 15, True, col, 'middle')
    f.foot('T4, T6, T7 rơi vào cùng một khoảnh khắc: lúc nến 17 đóng cửa. Trong thực tế chúng là ba VIỆC khác nhau làm ngay sau nhau: thấy cú phá → kiểm tra trình tự → gọi tên và khoá vùng.')
    return f.save()

# ------------------------------------------------------------------ 50 decision tree
def fig50():
    f = Fig(50, 'Decision-Tree-Nhan-Dien', 'Cây quyết định: từ “có cây nến nào không?” tới “có lệnh không?”',
            'Ba câu đầu là ĐỊNH NGHĨA (theo ICT). Câu 4 là bộ LỌC của bạn. Câu 5–6 là THỰC THI. Trả lời “không” ở đâu thì dừng ở đó.', h=760, tag='DECISION TREE')
    y = f.top + 10
    qs = [('Có cây nến ngược màu tại đỉnh/đáy giữa (OB gốc) không?', 'Không có gì để gọi tên. Dừng.', G, BBC),
          ('Cực trị cũ (đáy/đỉnh có trước) đã bị vi phạm chưa?', 'Nếu swing giữa vẫn bị phá: đó là Mitigation Block.', TEAL, BBC),
          ('Thân nến đã ĐÓNG CỬA qua swing giữa chưa?', 'Mới là ứng viên. Chờ. Râu vượt qua chưa tính.', WARN, BBC),
          ('Bối cảnh khung lớn có ủng hộ không? (bias, DOL, vị trí)', 'Breaker hợp lệ nhưng không dùng. Chỉ ghi chú.', G, WARN),
          ('Giá đã quay lại vùng chưa?', 'Chờ. Nếu mục tiêu đạt trước → hết hạn, bỏ.', G, GOOD),
          ('Khung nhỏ có sweep → MSS → displacement → FVG không?', 'Không có lệnh. Quan sát, ghi lại kết cục.', BAD, GOOD)]
    for k, (q, no, nc, c) in enumerate(qs):
        yy = y + k * 88 + (20 if k >= 3 else 0) + (20 if k >= 4 else 0)
        f.r(96, yy, 500, 60, fill=CARD, stroke=c, sw=1.6, rx=10); f.badge(118, yy + 30, k + 1, c, 11, 12)
        f.p(140, yy + 26 if tw(q, 12.6, True) <= 440 else yy + 22, q, 444, 12.6, INK, bold=True, lh=1.3)
        f.arrow(598, yy + 30, 650, yy + 30, nc, 2, size=7); f.t(624, yy + 22, 'không', 10.5, True, nc, 'middle')
        f.r(654, yy + 4, 318, 52, fill=nc, stroke=nc, sw=1.2, rx=9, op=0.07); f.p(668, yy + 26 if tw(no, 11.6) <= 290 else yy + 22, no, 292, 11.6)
        if k < 5:
            nyy = y + (k + 1) * 88 + (20 if k + 1 >= 3 else 0) + (20 if k + 1 >= 4 else 0)
            f.arrow(346, yy + 61, 346, nyy - 1, GOOD, 2, size=6); f.t(358, yy + 76, 'có', 10.5, True, GOOD)
    # brackets
    def brk(y1, y2, lab, c):
        f.ln(70, y1, 70, y2, c, 3); f.ln(70, y1, 80, y1, c, 3); f.ln(70, y2, 80, y2, c, 3)
        f.o.append('<text x="54" y="%.1f" font-size="11.5" font-weight="700" fill="%s" text-anchor="middle" transform="rotate(-90 54 %.1f)">%s</text>' % ((y1 + y2) / 2, c, (y1 + y2) / 2, lab))
    brk(y, y + 2 * 88 + 60, 'ĐỊNH NGHĨA', BBC); brk(y + 3 * 88 + 20, y + 3 * 88 + 80, 'LỌC', WARN); brk(y + 4 * 88 + 40, y + 5 * 88 + 100, 'THỰC THI', GOOD)
    f.t(386, y + 2 * 88 + 78, '← đủ ba câu: BREAKER ĐÃ XÁC NHẬN — khoá vùng', 11.5, True, BBC, 'start', halo=True)
    yy = y + 6 * 88 + 40
    f.arrow(346, yy - 27, 346, yy - 1, GOOD, 2, size=6)
    f.r(96, yy, 876, 44, fill=GOOD, stroke=GOOD, sw=1.5, rx=10, op=0.08)
    f.t(116, yy + 27, 'CÓ LỆNH: vào theo kế hoạch, mức dừng theo điều kiện “sai” đã chọn trước, mục tiêu là liquidity. Ghi nhật ký.', 12, True, GOOD)
    f.foot('Chỉ câu 1–3 đến từ lời ICT (và “thân nến đóng cửa” ở câu 3 là quy ước của note). Câu 4–6 là khung ICT 2022 của bạn, không phải điều kiện để một vùng ĐƯỢC GỌI là Breaker.')
    return f.save()

# ------------------------------------------------------------------ 51-56 case studies
def case(num, slug, title, sub, ctx, draw, concl, ccol):
    f = Fig(num, slug, title, sub, h=640, tag='CASE DỰNG')
    y0 = f.top + 4; H = 640 - y0 - 28
    f.card(28, y0, 600, H)
    draw(f, 46, y0 + 28, 564, H - 60)
    x = 642
    f.card(x, y0, 330, H, 'Bối cảnh và diễn biến')
    yy = y0 + 50
    for a, b in ctx:
        f.t(x + 14, yy, a, 11.8, True, BBC)
        yy = f.p(x + 14, yy + 16, b, 302, 11.5) + 7
    nl = len(wrap(concl, 278, 11.6))
    f.note(x + 14, y0 + H - 14 - (nl + 1) * 16.6 - 22, 302, concl, ccol, 'Điều thật sự kết luận được', size=11.6)
    return f.save()

def fig51():
    def d(f, x, y, w, h):
        ch, cs = base_chart(f, x, y, w, h, 'base', lo=35, hi=94)
        ch.level(90, 12, 24, PINK, 'DOL: đỉnh cũ khung lớn', pos='l')
        ch.lab(L1, P_L1, 'đáy phiên trước', dy=15, color=LIQ); ch.lab(HI, P_H, 'đỉnh giữa', dy=-8, color=STR)
        ch.ztext(11, 63.6, 'OB gốc', OBC); ch.ztext(18, 63.6, 'BULLISH\nBREAKER', BBC)
        for i, pv, n, c, dy in ((L2, P_L2, 1, PINK, 18), (CF, 71.5, 2, UP, -20), (RT, Z_LO, 3, INK, 16), (23, 83, 4, GOOD, -20)):
            ch.badge(i, pv, n, c, dy=dy)
    return case(51, 'Case-A-Textbook-Bullish', 'Case A — Bullish Breaker sách giáo khoa, thuận bối cảnh',
                'Khung H1. Khung lớn đang hướng lên, mục tiêu là đỉnh cũ phía trên. Mọi con số là giả định để minh hoạ.', [
                    ('Bối cảnh', 'D1 hướng lên, giá vừa hồi về nửa dưới. Còn đỉnh cũ phía trên chưa bị lấy.'),
                    ('① Liquidity', 'Giá xuống dưới đáy phiên trước — một túi lệnh dễ thấy — rồi dừng.'),
                    ('② Phá cấu trúc', 'Ba nến tăng mạnh, nến thứ năm đóng cửa trên đỉnh giữa. Có displacement.'),
                    ('③ Retest', 'Giá hồi về, râu chạm vùng, đóng cửa trong vùng. Khung nhỏ cho MSS tăng.'),
                    ('④ Kết quả', 'Giá đi tiếp về phía DOL.')], d,
                'Một mẫu mà MỌI thứ cùng chiều. Nó cho thấy trình tự trông thế nào khi chạy đúng — không cho thấy trình tự này chạy đúng bao nhiêu lần.', GOOD)

def fig52():
    def d(f, x, y, w, h):
        ch, cs = base_chart(f, x, y, w, h, 'base', flip=True, lo=30, hi=90)
        ch.level(33, 12, 24, PINK, 'DOL: đáy cũ khung lớn', pos='l', dy=-5)
        ch.lab(L1, P_L1, 'đỉnh phiên trước', dy=15, color=LIQ); ch.lab(HI, P_H, 'đáy giữa', dy=-8, color=STR)
        ch.ztext(11, 63.6, 'OB gốc', OBC); ch.ztext(18, 63.6, 'BEARISH\nBREAKER', BBC)
        for i, pv, n, c, dy in ((L2, P_L2, 1, PINK, 18), (CF, 71.5, 2, DN, -20), (RT, Z_LO, 3, INK, 16), (23, 83, 4, GOOD, -20)):
            ch.badge(i, pv, n, c, dy=dy)
    return case(52, 'Case-B-Textbook-Bearish', 'Case B — Bearish Breaker sách giáo khoa, thuận bối cảnh',
                'Khung H1. Ảnh gương của Case A: khung lớn đang hướng xuống, mục tiêu là đáy cũ phía dưới.', [
                    ('Bối cảnh', 'D1 hướng xuống, giá vừa hồi lên nửa trên. Còn đáy cũ phía dưới chưa bị lấy.'),
                    ('① Liquidity', 'Giá lên trên đỉnh phiên trước rồi dừng.'),
                    ('② Phá cấu trúc', 'Giá rơi mạnh, một nến đóng cửa dưới đáy giữa. Có displacement.'),
                    ('③ Retest', 'Giá hồi lên, râu chạm vùng, đóng cửa trong vùng. Khung nhỏ cho MSS giảm.'),
                    ('④ Kết quả', 'Giá đi tiếp về phía DOL.')], d,
                'Bullish và Bearish Breaker đối xứng hoàn toàn về định nghĩa. Thị trường thật thì không nhất thiết đối xứng: tốc độ rơi và tốc độ tăng có thể khác → ghi riêng hai chiều khi backtest.', GOOD)

def fig53():
    def d(f, x, y, w, h):
        ch = Chart(f, x, y, w, h, 46, 90, 17)
        ch.zone(2, 15, 71.6, 75.2, G, op=0.16); ch.candles(MIDLEG); ch.zone(2, 2, 71.6, 75.2, G, op=0, dash=None, sw=1.8)
        ch.level(82, 0, 15, STR, 'đỉnh gốc của nhịp giảm — CHƯA bị phá', pos='r')
        ch.lab(4.4, 75.2, 'bearish OB giữa nhịp', dy=-7, color=G, anchor='start'); ch.badge(11, 77, 1, BAD, dy=-18)
        ch.lab(11, 78.4, 'đóng cửa trên OB', dx=14, dy=-12, color=BAD, anchor='start'); ch.lab(6, 53, 'đáy', dy=14, color=STR)
        ch.badge(14, 70, 2, G, dy=18)
    return case(53, 'Case-C-Failed-OB-Khong-Phai-Breaker', 'Case C — Order Block thất bại nhưng KHÔNG phải Breaker',
                'Một bearish OB nằm giữa nhịp giảm bị giá đóng cửa xuyên qua. Trông giống “vùng kháng cự bị phá”, nhưng thiếu trình tự swing của Breaker.', [
                    ('OB gốc', 'Nến tăng nhỏ GIỮA một nhịp giảm — không nằm tại đỉnh của nhịp.'),
                    ('① OB thất bại', 'Giá hồi lên và đóng cửa trên OB. Theo nghĩa rộng: Failed Order Block.'),
                    ('Cấu trúc', 'Đỉnh gốc của nhịp giảm chưa bị phá. Chuỗi đỉnh thấp hơn còn nguyên. Không có MSS.'),
                    ('② Sau đó', 'Giá quay xuống qua vùng OB cũ như không có gì ở đó.')], d,
                'Không phải mọi vùng bị đóng xuyên đều đổi vai. Ở đây chỉ nói được: OB này vô hiệu. Không có cơ sở để gọi vùng là Bullish Breaker hay kỳ vọng nó đỡ giá.', G)

def fig54():
    def d(f, x, y, w, h):
        ch, cs = base_chart(f, x, y, w, h, 'tiny', lo=35, hi=90)
        ch.lab(L1, P_L1, 'đáy cũ: một gợn nhỏ', dy=15, dx=-6, color=LIQ); ch.lab(HI, P_H, 'đỉnh giữa', dy=-8, color=STR)
        ch.f.circ(ch.X(10.5), ch.Y(47), 20, 'none', stroke=WARN, sw=2); ch.lab(11.5, 46.4, 'chỉ vượt qua\nmột chút xíu', dx=20, dy=10, color=WARN, anchor='start')
        ch.ztext(11, 63.6, 'OB gốc', OBC); ch.ztext(18, 63.6, 'BREAKER?', BBC)
    return case(54, 'Case-D-Khong-Co-Sweep-Ro-Rang', 'Case D — Breaker không có cú quét rõ ràng',
                'Đáy cũ có bị vi phạm, nhưng chỉ bằng một cái râu rất ngắn, và “đáy cũ” chỉ là một gợn nhỏ. Đúng chữ của định nghĩa — còn đúng ý thì chưa chắc.', [
                    ('Đáy cũ', 'Không phải đáy ngày hay đáy phiên. Chỉ là một nhịp nghỉ nhỏ trong vùng đi ngang.'),
                    ('Vi phạm', 'Giá thò xuống dưới đáy cũ một đoạn rất ngắn. Trên dữ liệu của sàn khác có thể còn không thấy.'),
                    ('Phá cấu trúc', 'Rõ ràng: nến đóng cửa trên đỉnh giữa, có displacement.'),
                    ('Phân loại', 'Theo chữ: Breaker. Theo cách đọc chặt: mơ hồ giữa Breaker và Mitigation Block.')], d,
                'Định nghĩa của ICT chỉ đòi “old low violated”, không nói phải vi phạm bao nhiêu. Khi không quyết được, ghi “mơ hồ (Breaker | Mitigation)” và lý do. Đừng ép về phía mình thích.', WARN)

def fig55():
    def d(f, x, y, w, h):
        ch, cs = base_chart(f, x, y, w, h, 'weakbounce', lo=35, hi=90)
        ch.lab(L1, P_L1, 'đáy cũ', dy=15, color=LIQ); ch.lab(HI, P_H, 'đỉnh giữa', dy=-8, color=STR)
        ch.ztext(11, 63.6, 'OB gốc', OBC); ch.ztext(17.9, 63.6, 'BULLISH\nBREAKER', BBC)
        ch.badge(19.5, 66, 1, INK, dy=-22, dx=4); ch.badge(21, 69.5, 2, WARN, dy=-20); ch.badge(24, 59, 3, BAD, dy=0, dx=22)
        ch.level(90, 14, 26, G, 'đỉnh khung lớn — giá đang ở nửa trên', pos='l', sw=1)
    return case(55, 'Case-E-Breaker-That-Bai', 'Case E — Breaker đúng định nghĩa nhưng không giữ được',
                'Đủ ba mắt xích. Giá quay lại, bật nhẹ một nến rồi đóng cửa xuyên qua vùng. Bối cảnh: khung lớn đang hướng xuống.', [
                    ('Bối cảnh', 'D1 hướng xuống; nhịp tăng H1 này là nhịp hồi vào nửa trên của khoảng giá lớn.'),
                    ('① Retest', 'Giá về vùng, nến đóng cửa trong vùng.'),
                    ('② Phản ứng yếu', 'Một nến tăng nhỏ, không tạo đỉnh mới, không có displacement.'),
                    ('③ Thất bại', 'Nến đóng cửa dưới mép xa của vùng và giá đi tiếp xuống.')], d,
                'Vùng đúng tên, sai bối cảnh. Một mẫu không chứng minh “Breaker ngược khung lớn thì hỏng” — nhưng nó cho một giả thuyết đáng đếm: tỷ lệ giữ khi thuận so với khi ngược khung lớn.', BAD)

def fig56():
    def d(f, x, y, w, h):
        cs = seq('chop'); ch = Chart(f, x, y, w, h, 44, 72, 26)
        ch.level(63.6, 0, 25, STR, 'mép trên vùng đi ngang', pos='l'); ch.level(52.6, 0, 25, STR, 'mép dưới vùng đi ngang', pos='l', dy=14)
        for a, b, lo, hi in ((6, 11, 60.2, 63.4), (9, 15, 52.4, 55.6), (16, 22, 60.4, 64)):
            ch.zone(a, b, lo, hi, BAD, op=0.12)
        ch.candles(cs)
        ch.lab(8.5, 63.4, '“Breaker”?', dy=-8, color=BAD); ch.lab(12, 52.4, '“Breaker”?', dy=15, color=BAD); ch.lab(19, 64, '“Breaker”?', dy=-8, color=BAD)
    return case(56, 'Case-F-Breaker-Trong-Consolidation', 'Case F — “Breaker” mọc khắp nơi trong vùng đi ngang',
                'Giá dao động giữa hai mép. Đỉnh và đáy nhỏ liên tục bị quét rồi bị phá. Áp định nghĩa máy móc sẽ ra rất nhiều “Breaker”.', [
                    ('Cấu trúc', 'Không có chuỗi đỉnh/đáy cao hơn hay thấp hơn. Mọi swing đều là gợn nhỏ bên trong vùng.'),
                    ('Liquidity', 'Các túi lệnh nhỏ trên/dưới từng gợn bị lấy liên tục, không túi nào quan trọng.'),
                    ('Kết cục', 'Mỗi “Breaker” bị xuyên qua sau vài nến. Vai đỡ/chặn đổi liên tục.'),
                    ('Thứ đáng nhìn', 'Hai mép ngoài của vùng đi ngang — nơi có liquidity lớn hơn.')], d,
                'Trong vùng đi ngang, định nghĩa vẫn “đúng” nhưng vô dụng: swing bị phá không quan trọng, liquidity bị lấy không đáng kể. Việc nên làm là chờ giá rời vùng, không phải chọn Breaker đẹp nhất bên trong.', G)

# ------------------------------------------------------------------ 57 what we know vs assume
def fig57():
    f = Fig(57, 'Biet-vs-Gia-Dinh', 'Ta thật sự BIẾT gì, và ta đang GIẢ ĐỊNH gì?',
            'Bốn tầng, từ chắc nhất tới ít chắc nhất. Một câu nói về Breaker thuộc tầng nào thì chỉ đáng tin tới mức của tầng đó.', h=664, tag='TỔNG KẾT BẰNG CHỨNG')
    bands = [('NHÌN THẤY ĐƯỢC trên chart', GOOD, 'Ai nhìn cũng thấy giống nhau', ['Có một cây nến ở đỉnh/đáy giữa', 'Giá đã vượt cực trị cũ', 'Nến đã đóng cửa qua swing giữa', 'Giá đã quay lại vùng', 'Nến đóng trong hay ngoài vùng']),
             ('ICT ĐỊNH NGHĨA', BBC, 'Là tên gọi và cách dùng — không phải bằng chứng về hiệu quả', ['Vùng nến đó tên là Breaker', 'Thiếu vi phạm cực trị cũ → Mitigation Block', 'Giá quay lại = “setup worth considering”', 'Dùng “the entire range” của cây nến']),
             ('CỘNG ĐỒNG THÊM VÀO', WARN, 'Phổ biến, hợp lý, nhưng không có trong bài giảng Breaker đã đối chiếu', ['“Breaker = Failed Order Block”', 'Bắt buộc có displacement', 'Bắt buộc có FVG', 'Breaker mạnh hơn Mitigation Block', 'Vào lệnh ở 50% vùng', 'Lần chạm đầu là tốt nhất']),
             ('KHÔNG AI CHỨNG MINH ĐƯỢC TỪ CHART', BAD, 'Giả định hoặc lời hứa — cần dữ liệu khác, hoặc cần backtest', ['Smart Money cố ý tạo ra vùng này', 'Có lệnh tổ chức nằm trong vùng', 'Người bị kẹt sẽ thoát ở hoà vốn', 'Breaker luôn tạo phản ứng', 'Breaker có lợi thế giao dịch'])]
    y = f.top + 8
    for nm, c, sub, chips in bands:
        f.r(28, y, 944, 118, fill=CARD, stroke=c, sw=1.5, rx=11); f.r(28, y, 8, 118, fill=c, stroke=None, rx=4)
        f.t(50, y + 26, nm, 13.5, True, c); f.t(50, y + 45, sub, 11.4, False, SUB)
        xx = 50; yy = y + 60
        for cpt in chips:
            wd = tw(cpt, 10.8, True) + 16
            if xx + wd > 956: xx = 50; yy += 26
            f.pill(xx, yy, cpt, c, 10.8); xx += wd + 8
        y += 128
    f.foot('Đi từ trên xuống, độ chắc chắn giảm dần. Phần lớn nội dung “dạy Breaker” trên mạng trộn cả bốn tầng trong một câu. Tách chúng ra là việc quan trọng nhất của note này.')
    return f.save()

# ------------------------------------------------------------------ 58 final mental model
def fig58():
    f = Fig(58, 'Final-Mental-Model', 'Toàn bộ cơ chế trong một sơ đồ',
            'ORIGINAL ORDER BLOCK → FAILURE → STRUCTURAL CHANGE → BREAKER FORMATION → RETEST → POSSIBLE REACTION. Mũi tên liền = đã nhìn thấy. Mũi tên đứt = chưa chắc xảy ra.', h=620, tag='MENTAL MODEL')
    y = f.top + 44; w = 146; gap = 13.6
    it = [('ORIGINAL OB', OBC, 8, 'Nến ngược màu ở đỉnh giữa. Vai: chặn giá.'),
          ('FAILURE', DN, 17, 'Giá quay lại, thân nến đóng xuyên qua vùng.'),
          ('STRUCTURAL CHANGE', UP, 17, 'Thủng OB tại swing = thủng swing. Cấu trúc đổi (MSS).'),
          ('BREAKER FORMATION', BBC, 19, 'Vùng cũ được đổi tên, theo dõi với vai mới: đỡ giá.'),
          ('RETEST', INK, 21, 'Giá quay lại vùng. Có thể không bao giờ xảy ra.'),
          ('POSSIBLE REACTION', GOOD, 24, 'Giá có thể bật — hoặc xuyên qua. Cần bằng chứng khung nhỏ.')]
    arrows = ['giá quay lại,\nnến đóng qua', 'vì OB nằm\nngay tại swing', 'đổi tên:\nvùng cũ, vai mới', 'giá hồi về\n(không chắc)', 'bằng chứng\nkhung nhỏ?']
    for k, (nm, c, upto, body) in enumerate(it):
        x = 28 + k * (w + gap)
        f.r(x, y, w, 330, fill=CARD, stroke=c, sw=1.8, rx=11, dash=None if k < 4 else '6,4')
        f.r(x, y, w, 34, fill=c, stroke=None, rx=11, op=0.12); f.t(x + w / 2, y + 22, nm, 10.6, True, c, 'middle')
        ch, cs = base_chart(f, x + 6, y + 48, w - 12, 150, upto=upto, n=25, lo=37, hi=86, cw=3.6, small=True, blue=(k >= 3))
        if k == 1: ch.dot(15, 66, DN)
        if k == 2: ch.dot(CF, 71.5, UP)
        if k == 4: ch.dot(RT, 63.5, INK)
        f.p(x + 10, y + 228, body, w - 20, 11.4)
        if k < 5:
            ax = x + w; dash = None if k < 3 else '4,3'
            f.arrow(ax + 1, y + 120, ax + gap - 1, y + 120, STR, 2, dash, size=6)
            for j, l in enumerate(arrows[k].split('\n')): f.t(ax + gap / 2, y - 26 + j * 12.5, l, 9.6, True, STR if k < 3 else G, 'middle')
            f.ln(ax + gap / 2, y - 4, ax + gap / 2, y + 112, STR if k < 3 else G, 0.8, '2,3')
    yy = y + 346
    f.note(28, yy, 464, 'Giữa ô 1 và ô 2, cực trị cũ phải bị vi phạm (đáy cũ thủng / đỉnh cũ bị vượt). Thiếu bước này, ICT gọi vùng là Mitigation Block.', BBC, 'Mắt xích hay bị quên', size=11.6)
    f.note(508, yy, 464, 'Bốn ô đầu là LỊCH SỬ — đã xảy ra, kiểm tra được. Hai ô cuối là TƯƠNG LAI — một giả thuyết phải chờ thị trường trả lời.', WARN, 'Ranh giới quan trọng nhất', size=11.6)
    f.foot('Breaker là một cái NHÃN dán lên lịch sử giá, kèm một KỲ VỌNG về tương lai. Nhãn thì kiểm tra được ngay. Kỳ vọng thì chỉ backtest của chính bạn mới trả lời được.')
    return f.save()

ALL = [fig47, fig48, fig49, fig50, fig51, fig52, fig53, fig54, fig55, fig56, fig57, fig58]
if __name__ == '__main__':
    for fn in ALL: print(fn())
