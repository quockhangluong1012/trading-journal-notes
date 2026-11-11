# -*- coding: utf-8 -*-
"""Drawing kit for CHoCH v2 figures — extends bbdraw (BB-v3 style) with zigzags and a candle-path generator."""
from bbdraw import *
import bbdraw

PFX = 'CHoCH-v2'
CHC = '#C026D3'    # CHoCH / change of character
BOSC = '#2563EB'   # BOS
PROT = '#B45309'   # protected swing
SWP = '#7C3AED'    # liquidity / sweep
FVGC = '#0891B2'   # FVG
DISP = '#0E9F6E'
MUTE = '#9CA3AF'
TEAL = '#0D9488'
PINKBG = '#FDF4FF'


class F(Fig):
    def __init__(s, num, slug, title, sub=None, h=600, tag='SƠ ĐỒ DỰNG', w=1000):
        Fig.__init__(s, num, slug, title, sub, h, tag, w)
        s.name = '%s-%02d-%s.svg' % (PFX, num, slug)

    def person(s, x, y, color=INK, sc=1.0, arms='down'):
        """tiny stick figure standing with feet at (x, y)."""
        hd = 6 * sc
        s.circ(x, y - 30 * sc, hd, color)
        s.ln(x, y - 24 * sc, x, y - 11 * sc, color, 2.2 * sc)
        s.ln(x, y - 11 * sc, x - 5 * sc, y, color, 2.2 * sc)
        s.ln(x, y - 11 * sc, x + 5 * sc, y, color, 2.2 * sc)
        if arms == 'up':
            s.ln(x, y - 21 * sc, x - 7 * sc, y - 31 * sc, color, 2 * sc); s.ln(x, y - 21 * sc, x + 7 * sc, y - 31 * sc, color, 2 * sc)
        else:
            s.ln(x, y - 21 * sc, x - 7 * sc, y - 14 * sc, color, 2 * sc); s.ln(x, y - 21 * sc, x + 7 * sc, y - 14 * sc, color, 2 * sc)

    def table(s, x, y, colw, rows, size=11.5, head_fill='#F3F4F6', lh=1.38, pad=8, colors=None, bold_first=True):
        """simple wrapped table; rows[0] is header. returns bottom y."""
        for ri, row in enumerate(rows):
            wrapped = [wrap(c, colw[k] - 2 * pad, size, ri == 0 or (bold_first and k == 0)) for k, c in enumerate(row)]
            nl = max(len(w) for w in wrapped)
            hgt = nl * size * lh + 2 * pad - size * 0.25
            xx = x
            for k, lines in enumerate(wrapped):
                fill = head_fill if ri == 0 else CARD
                s.r(xx, y, colw[k], hgt, fill=fill, stroke=BORDER, sw=1, rx=0)
                yy = y + pad + size * 0.9
                col = INK
                if colors and ri > 0 and colors.get((ri, k)):
                    col = colors[(ri, k)]
                for l in lines:
                    s.t(xx + pad, yy, l, size, ri == 0 or (bold_first and k == 0), col, bx=(xx, xx + colw[k]))
                    yy += size * lh
                xx += colw[k]
            y += hgt
        return y


def zz(ch, pts, color=INK, sw=2.3, dash=None, op=None):
    ch.f.poly([(ch.X(i), ch.Y(p)) for i, p in pts], color, sw, dash, op=op)


def dots(ch, pts, color=INK, rad=3.6):
    for i, p in pts:
        ch.dot(i, p, color, rad)


def gen(start, segs, u=1.0, seed=0, over=None):
    """Candle path generator.
    segs: list of (target, n, style); style 'i' impulse/displacement, 'c' corrective, 'g' grind (overlapping, slow).
    Returns (cs, turns) where turns = list of (idx, extreme, 'H'|'L') at each segment end."""
    cs = []; o = start; turns = []; k = 0
    for si, (tgt, n, sty) in enumerate(segs):
        a = o; d = tgt - a; step = d / float(n)
        for j in range(n):
            r = ((k * 37 + 11 * si + seed * 13) % 17) / 16.0
            r2 = ((k * 23 + 7 * si + seed * 5) % 13) / 12.0
            base = a + step * (j + 1)
            if j == n - 1:
                c = tgt
            elif sty == 'i':
                c = base + step * 0.08 * (r - 0.5)
            elif sty == 'c':
                wig = abs(step) * 0.55 + 0.45 * u
                c = base + (wig if j % 2 == 0 else -wig * 0.7) * (-1 if d > 0 else 1)
            else:  # grind
                wig = abs(step) * 0.9 + 0.35 * u
                c = base + (wig if j % 2 == 0 else -wig * 0.6) * (-1 if d > 0 else 1)
            if sty == 'i':
                uw = (0.12 + 0.18 * r) * u; dw = (0.12 + 0.18 * r2) * u
            else:
                uw = (0.3 + 0.55 * r) * u; dw = (0.3 + 0.55 * r2) * u
            cs.append([o, max(o, c) + uw, min(o, c) - dw, c]); o = c; k += 1
        turns.append((k - 1, tgt, 'H' if d > 0 else 'L'))
    # enforce extremes at turning candles
    for (idx, tgt, kind) in turns[:-1]:
        if kind == 'H':
            hk = tgt + 0.3 * u; cs[idx][1] = hk
            for j in range(max(0, idx - 3), min(len(cs), idx + 4)):
                if j != idx:
                    cs[j][1] = max(max(cs[j][0], cs[j][3]), min(cs[j][1], hk - 0.2 * u))
        else:
            lk = tgt - 0.3 * u; cs[idx][2] = lk
            for j in range(max(0, idx - 3), min(len(cs), idx + 4)):
                if j != idx:
                    cs[j][2] = min(min(cs[j][0], cs[j][3]), max(cs[j][2], lk + 0.2 * u))
    turns = [(i, (cs[i][1] if kd == 'H' else cs[i][2]), kd) for (i, t, kd) in turns]
    for i, ov in (over or {}).items():
        if 'o' in ov: cs[i][0] = ov['o']
        if 'c' in ov: cs[i][3] = ov['c']
        if 'h' in ov: cs[i][1] = ov['h']
        if 'l' in ov: cs[i][2] = ov['l']
        cs[i][1] = max(cs[i][1], cs[i][0], cs[i][3]); cs[i][2] = min(cs[i][2], cs[i][0], cs[i][3])
    return [tuple(c) for c in cs], turns


def fvgs(cs, a=0, b=None, bull=True):
    """list of (mid_idx, lo, hi) bullish (or bearish) FVGs."""
    out = []
    b = len(cs) - 1 if b is None else b
    for i in range(max(1, a), min(b, len(cs) - 1)):
        if bull and cs[i - 1][1] < cs[i + 1][2]:
            out.append((i, cs[i - 1][1], cs[i + 1][2]))
        if not bull and cs[i - 1][2] > cs[i + 1][1]:
            out.append((i, cs[i + 1][1], cs[i - 1][2]))
    return out


def mini(f, x, y, w, h, pts, lo, hi, title=None, tcolor=INK, n=None, flip=False, color=INK, card=True, sw=2.2):
    """mini card with a zigzag chart. returns Chart."""
    top = y
    if card:
        f.r(x, y, w, h, fill=CARD, stroke=BORDER, rx=10)
    if title:
        top = f.p(x + 12, y + 22, title, w - 24, 12.5, tcolor, bold=True, lh=1.28) - 6
    n = n or (max(i for i, p in pts) + 1)
    ch = Chart(f, x + 14, top + 8, w - 28, h - (top - y) - 18, lo, hi, n, flip)
    zz(ch, pts, color, sw)
    return ch


# ---------------------------------------------------------------- canonical sequences
# Bullish CHoCH scenario (bearish structure -> SSL sweep -> displacement up through protected high).
BULL_SEGS = [(80.5, 3, 'c'), (70, 4, 'i'), (79, 4, 'c'), (63, 4, 'i'), (72, 4, 'c'), (56.5, 4, 'i'),
             (61.5, 3, 'c'), (57.3, 2, 'c'), (77, 4, 'i'), (69.5, 3, 'c'), (84, 4, 'i')]


def bull_seq(extra=None):
    ov = {27: {'l': 54.6}}
    ov.update(extra or {})
    cs, tn = gen(86, BULL_SEGS, u=1.0, seed=1, over=ov)
    return cs, tn


def mirror(cs, C=140.0):
    """mirror a candle list vertically (bullish scenario -> bearish scenario)."""
    return [(C - o, C - l, C - h, C - c) for (o, h, l, c) in cs]


def bear_seq(extra=None):
    cs, tn = bull_seq(extra)
    return mirror(cs), [(i, 140.0 - p, 'L' if k == 'H' else 'H') for i, p, k in tn]
