import sys, os
from PIL import Image
names = sys.argv[2:]; out = sys.argv[1]
ims = [Image.open('png/' + n.replace('.svg', '.png')) for n in names]
sc = 0.5; cols = 2
W = int(1000 * sc); rows = (len(ims) + 1) // cols
hs = [int(im.height * sc) for im in ims]
rowh = [max(hs[r * cols:(r + 1) * cols]) for r in range(rows)]
sheet = Image.new('RGB', (W * cols + 10, sum(rowh) + 10 * rows), 'white')
y = 0
for r in range(rows):
    for c in range(cols):
        k = r * cols + c
        if k < len(ims):
            sheet.paste(ims[k].resize((W, hs[k])), (c * (W + 10), y))
    y += rowh[r] + 10
sheet.save(out)
