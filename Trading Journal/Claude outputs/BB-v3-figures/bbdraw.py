# -*- coding: utf-8 -*-
"""Tiny SVG drawing kit for the Breaker Block v3 figures (schematic candles + diagrams)."""
import os, html, math
from PIL import ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'svg')
FR = '/usr/share/fonts/opentype/inter/Inter-Regular.otf'
FB = '/usr/share/fonts/opentype/inter/Inter-Bold.otf'
FONT = "'Segoe UI', Inter, Roboto, 'Helvetica Neue', Arial, sans-serif"

INK, SUB, BORDER, BG, CARD = '#111827', '#6B7280', '#DADDE3', '#FBFBFD', '#FFFFFF'
UP, DN = '#0E9F6E', '#E5484D'
OBC, BBC, LIQ, FVG, STR = '#D97706', '#2563EB', '#7C3AED', '#0891B2', '#475569'
GOOD, BAD, WARN, GRAY = '#15803D', '#B91C1C', '#B45309', '#94A3B8'
CIRC = '①②③④⑤⑥⑦⑧⑨⑩⑪⑫'

_f = {}
def tw(s, size, bold=False):
    if bold not in _f:
        _f[bold] = ImageFont.truetype(FB if bold else FR, 200)
    return _f[bold].getlength(s) * size / 200.0 * 1.03

def wrap(s, width, size, bold=False):
    out = []
    for para in str(s).split('\n'):
        cur = ''
        for w in para.split(' '):
            t = (cur + ' ' + w).strip()
            if not cur or tw(t, size, bold) <= width:
                cur = t
            else:
                out.append(cur); cur = w
        out.append(cur)
    return out

def esc(s):
    return html.escape(str(s), quote=False)

class Fig:
    def __init__(s, num, slug, title, sub=None, h=600, tag='SƠ ĐỒ DỰNG', w=1000):
        s.name = 'BB-v3-%02d-%s.svg' % (num, slug)
        s.num, s.w, s.h, s.o = num, w, h, []
        s.r(0.75, 0.75, w - 1.5, h - 1.5, fill=BG, stroke=BORDER, sw=1.5, rx=14)
        tgw = tw(tag, 10.5, True) + 26
        ts = 20
        while tw(title, ts, True) > w - 56 - tgw - 12 and ts > 15.5: ts -= 0.5
        assert tw(title, ts, True) <= w - 56 - tgw - 12, 'title too long: ' + title
        s.t(28, 42, title, ts, True)
        s.r(w - 28 - tgw, 23, tgw, 24, fill='#F3F4F6', stroke=BORDER, sw=1, rx=12)
        s.t(w - 28 - tgw / 2, 39.5, tag, 10.5, True, fill='#4B5563', anchor='middle')
        s.top = 70
        if sub:
            s.top = s.p(28, 66, sub, w - 56, 13, SUB) + 4

    # ---- primitives
    def t(s, x, y, txt, size=12, bold=False, fill=INK, anchor='start', halo=False, bx=None, italic=False, op=None):
        a = '' if anchor == 'start' else ' text-anchor="%s"' % anchor
        hl = ' paint-order="stroke" stroke="#FFFFFF" stroke-width="3.2" stroke-linejoin="round"' if halo else ''
        b = '' if bx is None else ' data-bx="%.1f,%.1f"' % bx
        it = ' font-style="italic"' if italic else ''
        opa = '' if op is None else ' opacity="%s"' % op
        s.o.append('<text x="%.1f" y="%.1f" font-size="%s" font-weight="%d" fill="%s"%s%s%s%s%s>%s</text>'
                   % (x, y, size, 700 if bold else 400, fill, a, hl, b, it, opa, esc(txt)))

    def p(s, x, y, txt, width, size=12.5, fill=INK, lh=1.42, bold=False, anchor='start', italic=False):
        for line in wrap(txt, width, size, bold):
            xx = x if anchor == 'start' else (x + width / 2 if anchor == 'middle' else x + width)
            s.t(xx, y, line, size, bold, fill, anchor, bx=(x - 1, x + width + 1), italic=italic)
            y += size * lh
        return y

    def r(s, x, y, w, h, fill=CARD, stroke=BORDER, sw=1.2, rx=10, dash=None, op=None, sop=None):
        d = '' if not dash else ' stroke-dasharray="%s"' % dash
        fo = '' if op is None else ' fill-opacity="%s"' % op
        so = '' if sop is None else ' stroke-opacity="%s"' % sop
        st = ' stroke="%s" stroke-width="%s"' % (stroke, sw) if stroke else ''
        s.o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="%s"%s%s%s%s/>'
                   % (x, y, w, h, rx, fill, fo, st, so, d))

    def ln(s, x1, y1, x2, y2, color=INK, sw=1.5, dash=None, op=None, cap='round'):
        d = '' if not dash else ' stroke-dasharray="%s"' % dash
        o = '' if op is None else ' opacity="%s"' % op
        s.o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" stroke-linecap="%s"%s%s/>'
                   % (x1, y1, x2, y2, color, sw, cap, d, o))

    def head(s, x1, y1, x2, y2, color, size=8):
        ang = math.atan2(y2 - y1, x2 - x1)
        pts = []
        for da in (0, 2.55, -2.55):
            rr = 0 if da == 0 else size
            pts.append('%.1f,%.1f' % (x2 + rr * math.cos(ang + da), y2 + rr * math.sin(ang + da)))
        s.o.append('<polygon points="%s" fill="%s"/>' % (' '.join(pts), color))

    def arrow(s, x1, y1, x2, y2, color=INK, sw=1.8, dash=None, size=8, op=None):
        ang = math.atan2(y2 - y1, x2 - x1)
        s.ln(x1, y1, x2 - (size * 0.75) * math.cos(ang), y2 - (size * 0.75) * math.sin(ang), color, sw, dash, op)
        s.head(x1, y1, x2, y2, color, size)

    def curve(s, x1, y1, cx, cy, x2, y2, color=INK, sw=1.8, dash=None, arrow=True, size=8):
        d = '' if not dash else ' stroke-dasharray="%s"' % dash
        s.o.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round"%s/>'
                   % (x1, y1, cx, cy, x2, y2, color, sw, d))
        if arrow:
            s.head(cx, cy, x2, y2, color, size)

    def poly(s, pts, color=INK, sw=2, dash=None, fill='none', op=None):
        d = '' if not dash else ' stroke-dasharray="%s"' % dash
        o = '' if op is None else ' opacity="%s"' % op
        s.o.append('<polyline points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"%s%s/>'
                   % (' '.join('%.1f,%.1f' % q for q in pts), fill, color, sw, d, o))

    def circ(s, x, y, rad, fill=INK, stroke=None, sw=1.5, op=None):
        st = '' if not stroke else ' stroke="%s" stroke-width="%s"' % (stroke, sw)
        o = '' if op is None else ' fill-opacity="%s"' % op
        s.o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"%s%s/>' % (x, y, rad, fill, st, o))

    def badge(s, x, y, n, color=INK, rad=10, size=11):
        s.circ(x, y, rad, color, stroke='#FFFFFF', sw=1.5)
        s.t(x, y + size * 0.36, str(n), size, True, '#FFFFFF', 'middle')

    def card(s, x, y, w, h, title=None, num=None, fill=CARD, tcolor=INK, tsize=13.5, stroke=BORDER):
        s.r(x, y, w, h, fill=fill, stroke=stroke, rx=11)
        yy = y + 14
        if title:
            tx = x + 14
            if num is not None:
                s.badge(x + 24, y + 21, num, tcolor, 10, 11)
                tx = x + 41
            yy = s.p(tx, y + 25.5, title, x + w - 12 - tx, tsize, tcolor, bold=True, lh=1.3) - 2
        return yy

    def note(s, x, y, w, txt, color=STR, title=None, size=12, pad=10):
        lines = wrap(txt, w - 2 * pad - 4, size)
        tl = wrap(title, w - 2 * pad - 4, size, True) if title else []
        h = pad * 2 + (len(lines) + len(tl)) * size * 1.42 - size * 0.3 + (3 if title else 0)
        s.r(x, y, w, h, fill=color, stroke=color, sw=1, rx=8, op=0.07, sop=0.35)
        s.r(x, y, 4, h, fill=color, stroke=None, rx=2)
        yy = y + pad + size * 0.85
        for l in tl:
            s.t(x + pad + 4, yy, l, size, True, color, bx=(x, x + w)); yy += size * 1.42
        if title: yy += 3
        for l in lines:
            s.t(x + pad + 4, yy, l, size, False, INK, bx=(x, x + w)); yy += size * 1.42
        return y + h

    def pill(s, x, y, txt, color, size=10.5, anchor='start', fill=None):
        wd = tw(txt, size, True) + 16
        if anchor == 'middle': x -= wd / 2
        elif anchor == 'end': x -= wd
        s.r(x, y, wd, size + 9, fill=fill or color, stroke=color, sw=1, rx=(size + 9) / 2, op=None if fill else 0.12)
        s.t(x + wd / 2, y + size + 1.2, txt, size, True, color, 'middle')
        return wd

    def foot(s, txt):
        lines = wrap(txt, s.w - 56, 12)
        y = s.h - 16 - (len(lines) - 1) * 17
        for l in lines:
            s.t(28, y, l, 12, False, SUB, bx=(27, s.w - 27)); y += 17

    def save(s):
        svg = ('<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" font-family="%s">\n%s\n</svg>\n'
               % (s.w, s.h, FONT, '\n'.join(s.o)))
        os.makedirs(OUT, exist_ok=True)
        with open(os.path.join(OUT, s.name), 'w', encoding='utf-8') as fh:
            fh.write(svg)
        return s.name


class Chart:
    def __init__(s, f, x, y, w, h, lo, hi, n, flip=False, cw=None):
        s.f, s.x, s.y, s.w, s.h, s.lo, s.hi, s.n, s.flip = f, x, y, w, h, lo, hi, n, flip
        s.step = w / float(n)
        s.cw = cw or max(3.0, min(s.step * 0.62, 15))

    def X(s, i): return s.x + (i + 0.5) * s.step
    def Y(s, p):
        fr = (p - s.lo) / float(s.hi - s.lo)
        if s.flip: fr = 1 - fr
        return s.y + s.h * (1 - fr)

    def candles(s, cs, i0=0, upto=None, op=None, gray=False):
        o_ = '' if op is None else ' opacity="%s"' % op
        s.f.o.append('<g%s>' % o_)
        for k, (o, h, l, c) in enumerate(cs if upto is None else cs[:upto]):
            up = c >= o
            if s.flip: up = not up
            col = GRAY if gray else (UP if up else DN)
            x = s.X(i0 + k)
            s.f.o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>'
                         % (x, s.Y(h), x, s.Y(l), col, 1.4 if s.cw > 6 else 1.0))
            y1, y2 = sorted((s.Y(o), s.Y(c)))
            s.f.o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1" fill="%s"/>'
                         % (x - s.cw / 2, y1, s.cw, max(1.4, y2 - y1), col))
        s.f.o.append('</g>')

    def _blk(s, x, Y0, dy, txt, size, bold, color, anchor, halo=True):
        lines = str(txt).split('\n'); n = len(lines); lh = size * 1.25; cap = size * 0.72
        H = (n - 1) * lh + cap
        top = (Y0 + dy - H) if dy <= 0 else (Y0 + dy - cap)
        if s.flip: top = 2 * Y0 - (top + H)
        for k, l in enumerate(lines):
            s.f.t(x, top + cap + k * lh, l, size, bold, color, anchor, halo=halo, bx=(s.x - 6, s.x + s.w + 6))

    def zone(s, a, b, p0, p1, color, label=None, pos='tl', dash='5,3', op=0.14, size=10.5, sw=1.2):
        x1 = s.x + a * s.step; x2 = s.x + (b + 1) * s.step
        y1, y2 = sorted((s.Y(p0), s.Y(p1)))
        s.f.r(x1, y1, x2 - x1, y2 - y1, fill=color, stroke=color, sw=sw, rx=2, dash=dash, op=op)
        if label:
            n = len(label.split('\n')); lh = size * 1.25
            if pos == 'tl': s._lines(x1 + 5, y1 + size + 2, label, size, color, 'start', lh)
            elif pos == 'tr': s._lines(x2 - 5, y1 + size + 2, label, size, color, 'end', lh)
            elif pos == 'bl': s._lines(x1 + 5, y2 - 5 - (n - 1) * lh, label, size, color, 'start', lh)
            elif pos == 'br': s._lines(x2 - 5, y2 - 5 - (n - 1) * lh, label, size, color, 'end', lh)
            elif pos == 'c': s._lines((x1 + x2) / 2, (y1 + y2) / 2 + size * 0.36 - (n - 1) * lh / 2, label, size, color, 'middle', lh)
            elif pos == 'al': s._lines(x1 + 2, y1 - 5 - (n - 1) * lh, label, size, color, 'start', lh)
            elif pos == 'ar': s._lines(x2 - 2, y1 - 5 - (n - 1) * lh, label, size, color, 'end', lh)
            elif pos == 'ul': s._lines(x1 + 2, y2 + size + 3, label, size, color, 'start', lh)
            elif pos == 'ur': s._lines(x2 - 2, y2 + size + 3, label, size, color, 'end', lh)
            elif pos == 'r': s._lines(x2 + 6, (y1 + y2) / 2 + size * 0.36 - (n - 1) * lh / 2, label, size, color, 'start', lh)
            elif pos == 'l': s._lines(x1 - 6, (y1 + y2) / 2 + size * 0.36 - (n - 1) * lh / 2, label, size, color, 'end', lh)

    def _lines(s, x, y, txt, size, color, anchor, lh):
        for k, l in enumerate(txt.split('\n')):
            s.f.t(x, y + k * lh, l, size, True, color, anchor, halo=True, bx=(s.x - 6, s.x + s.w + 6))

    def level(s, p, a, b, color, label=None, pos='r', dash='6,4', sw=1.3, size=10.5, dy=-5):
        x1 = s.x + a * s.step; x2 = s.x + (b + 1) * s.step; y = s.Y(p)
        s.f.ln(x1, y, x2, y, color, sw, dash)
        if label:
            if pos == 'r': s._blk(x2 - 2, y, dy, label, size, True, color, 'end')
            elif pos == 'l': s._blk(x1 + 2, y, dy, label, size, True, color, 'start')
            elif pos == 'rr': s._blk(x2 + 5, y, size * 0.36, label, size, True, color, 'start') if not s.flip else s.f.t(x2 + 5, y + size * 0.36, label, size, True, color, 'start', halo=True)
            elif pos == 'c': s._blk((x1 + x2) / 2, y, dy, label, size, True, color, 'middle')

    def lab(s, i, p, txt, dx=0, dy=-7, color=INK, size=10.5, bold=True, anchor='middle', lead=None):
        x = s.X(i) + dx; Y0 = s.Y(p)
        if lead:
            yy = Y0 + (dy if not s.flip else -dy) * 0.55
            s.f.ln(s.X(i), Y0 + (-3 if (dy < 0) != s.flip else 3), x, yy, color, 1, '2,2')
        s._blk(x, Y0, dy, txt, size, bold, color, anchor)

    def badge(s, i, p, n, color=INK, dy=-17, dx=0, rad=9.5):
        y = s.Y(p) + (dy if not s.flip else -dy)
        s.f.badge(s.X(i) + dx, y, n, color, rad, 10.5)

    def arr(s, i0, p0, i1, p1, color=INK, dash=None, sw=1.8, bend=0):
        x1, y1, x2, y2 = s.X(i0), s.Y(p0), s.X(i1), s.Y(p1)
        if bend:
            s.f.curve(x1, y1, (x1 + x2) / 2, (y1 + y2) / 2 + (bend if not s.flip else -bend), x2, y2, color, sw, dash)
        else:
            s.f.arrow(x1, y1, x2, y2, color, sw, dash)

    def ztext(s, i, p, txt, color, size=10.5, anchor='middle'):
        n = len(txt.split('\n')); lh = size * 1.25
        s._lines(s.X(i), s.Y(p) + size * 0.36 - (n - 1) * lh / 2, txt, size, color, anchor, lh)

    def dot(s, i, p, color=INK, rad=3.5):
        s.f.circ(s.X(i), s.Y(p), rad, color, stroke='#FFFFFF', sw=1.2)

    def fog(s, a, label='chưa biết'):
        x1 = s.x + a * s.step
        s.f.r(x1, s.y - 4, s.x + s.w - x1, s.h + 8, fill='#E5E7EB', stroke='#9CA3AF', sw=1, rx=4, dash='4,4', op=0.55)
        if label:
            s.f.t((x1 + s.x + s.w) / 2, s.y + s.h / 2 - 6, '?', 30, True, '#6B7280', 'middle')
            s.f.t((x1 + s.x + s.w) / 2, s.y + s.h / 2 + 16, label, 11, True, '#6B7280', 'middle')


# ---------- candle sequences (internal orientation = bullish breaker; flip the chart for bearish)
def mk(start, closes, over=None, wk=1.0):
    cs = []; o = start; over = over or {}
    for i, c in enumerate(closes):
        uw = wk * (0.5 + 0.55 * ((i * 7 + 3) % 5) / 4.0)
        dw = wk * (0.45 + 0.6 * ((i * 5 + 1) % 4) / 3.0)
        h = max(o, c) + uw; l = min(o, c) - dw
        ov = over.get(i, {})
        if 'o' in ov: o = ov['o']; h = max(h, o); l = min(l, o)
        h = ov.get('h', h); l = ov.get('l', l)
        cs.append((o, h, l, c)); o = c
    return cs

# key indices of the base sequence
L1, HI, L2, CF, RT = 2, 6, 11, 16, 20
P_L1, P_H, P_L2, Z_LO, Z_HI, B_LO, B_HI = 47.0, 67.0, 41.0, 60.3, 67.0, 61.0, 65.0
HEAD = [58, 53, 49, 52, 56, 61, 65, 61, 55.5, 50, 46, 44]
HOV = {2: {'l': 47}, 6: {'h': 67, 'l': 60.3}, 7: {'h': 65.8}, 10: {'l': 44.5}, 11: {'l': 41}}
UPLEG = [51, 59.5, 63, 66, 71.5]
UOV = {15: {'h': 66.7, 'l': 61}, 16: {'l': 64.5}}

def seq(kind='base'):
    ov = dict(HOV)
    if kind == 'base':        # textbook: confirmed, retested, holds
        cl = HEAD + UPLEG + [75, 73, 70, 66.5, 71, 77, 82]; ov.update(UOV); ov[20] = {'l': 63.5}
    elif kind == 'toconfirm':  # stops right after confirmation
        cl = HEAD + UPLEG; ov.update(UOV)
    elif kind == 'fail':      # confirmed, retest closes through the far edge
        cl = HEAD + UPLEG + [75, 73, 69.5, 65, 61, 56.5, 53, 50]; ov.update(UOV)
    elif kind == 'noretest':  # confirmed, never comes back
        cl = HEAD + UPLEG + [75, 74, 78, 81, 80, 84, 87]; ov.update(UOV)
    elif kind == 'obholds':   # old low violated, rally dies INSIDE the OB -> no breaker
        cl = HEAD + [50, 56, 61.5, 59, 54, 49, 44.5, 40.5, 38]; ov[14] = {'h': 64.6}
    elif kind == 'wick':      # wick above the swing high, close back below
        cl = HEAD + [51, 59.5, 63, 65.5, 62, 58, 54.5, 52, 49]; ov[15] = {'h': 69.5}
    elif kind == 'mitig':     # higher low (old low NOT violated) then close above swing high
        cl = [58, 53, 49, 52, 56, 61, 65, 61, 56.5, 53, 51.5, 55.5, 60, 63.5, 66, 71.5, 75, 73, 70, 66.5, 71, 77, 82]
        ov = {2: {'l': 47}, 6: {'h': 67, 'l': 60.3}, 7: {'h': 65.8}, 10: {'l': 50}, 14: {'h': 66.7}, 15: {'l': 64.5}, 19: {'l': 63.5}}
    elif kind == 'weak':      # grinding break, overlapping small candles
        cl = HEAD + [47, 50, 49, 53, 55, 54, 58, 60, 59.5, 63, 62, 65.5, 64.5, 67.8, 66.5, 68.6, 67.5, 66, 64]
    elif kind == 'side':      # old low violated, then nothing: sideways
        cl = HEAD + [47.5, 50.5, 48.5, 52, 50, 53, 50.5, 48.5, 51.5, 49.5, 52]
    elif kind == 'wickretest':  # retest only by a wick
        cl = HEAD + UPLEG + [75, 73, 70.5, 69, 73, 78, 82]; ov.update(UOV); ov[20] = {'l': 65.4}
    elif kind == 'multi':     # several retests
        cl = HEAD + UPLEG + [75, 70, 66.5, 71, 74, 69.5, 65.5, 70, 73, 68, 64.5, 68.5]; ov.update(UOV)
    elif kind == 'revbefore':  # opposite structure shift before the first retest
        cl = HEAD + UPLEG + [75, 78.5, 74.5, 77, 73, 70.5, 68.5, 66]; ov.update(UOV); ov[18] = {'h': 79.6}; ov[19] = {'l': 74}; ov[20] = {'h': 77.6}
    elif kind == 'weakbounce':  # small reaction, then failure
        cl = HEAD + UPLEG + [75, 72, 68, 66, 69.5, 67, 63, 59, 55.5]; ov.update(UOV)
    elif kind == 'tiny':      # old low violated only by a hair (minor pool)
        cl = [58, 53, 49, 52, 56, 61, 65, 61, 56, 52, 49.5, 48.6] + UPLEG + [75, 73, 70, 66.5, 71, 77, 82]
        ov = {2: {'l': 47}, 6: {'h': 67, 'l': 60.3}, 7: {'h': 65.8}, 10: {'l': 47.6}, 11: {'l': 46.4}}; ov.update(UOV); ov[20] = {'l': 63.5}
    elif kind == 'chop':
        return mk(56, [59, 61.5, 58, 55, 57.5, 60.5, 62, 58.5, 55.5, 53.5, 57, 60, 61.5, 58, 56, 59, 62.5, 60, 56.5, 54.5, 57.5, 60, 58, 56, 59],
                  {1: {'h': 63}, 6: {'h': 63.4}, 9: {'l': 52.4}, 16: {'h': 64}, 19: {'l': 53}})
    return mk(62, cl, ov)
