// render every svg in ./svg (or the names given) to ./png and report text overflow / overlaps
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
(async () => {
  let names = process.argv.slice(2);
  if (!names.length) names = fs.readdirSync('svg').filter(n => n.endsWith('.svg')).sort();
  const b = await chromium.launch(); const p = await b.newPage({ deviceScaleFactor: 1 });
  let bad = 0;
  for (const n of names) {
    const svg = fs.readFileSync(path.join('svg', n), 'utf8');
    const m = svg.match(/viewBox="0 0 (\d+) (\d+)"/); const w = +m[1], h = +m[2];
    await p.setViewportSize({ width: w, height: h });
    await p.setContent(`<html><body style="margin:0">${svg}</body></html>`);
    const issues = await p.evaluate(([w, h]) => {
      const out = []; const ts = [...document.querySelectorAll('text')];
      const bb = ts.map(t => { const r = t.getBBox(); return { x: r.x, y: r.y, w: r.width, h: r.height, s: t.textContent, bx: t.getAttribute('data-bx'), fs: +t.getAttribute('font-size') }; });
      bb.forEach(r => {
        if (r.x < 4 || r.x + r.w > w - 4 || r.y < 2 || r.y + r.h > h - 2) out.push('OUT ' + r.s);
        if (r.bx) { const [a, c] = r.bx.split(',').map(Number); if (r.x < a - 1.5 || r.x + r.w > c + 1.5) out.push('BOX ' + Math.round(Math.max(a - r.x, r.x + r.w - c)) + 'px ' + r.s); }
      });
      for (let i = 0; i < bb.length; i++) for (let j = i + 1; j < bb.length; j++) {
        const a = bb[i], c = bb[j];
        const ix = Math.min(a.x + a.w, c.x + c.w) - Math.max(a.x, c.x); const iy = Math.min(a.y + a.h, c.y + c.h) - Math.max(a.y, c.y);
        if (ix > 3 && iy > Math.min(a.fs, c.fs) * 0.45) out.push('OVERLAP "' + a.s + '" × "' + c.s + '"');
      }
      return out;
    }, [w, h]);
    if (issues.length) { bad++; console.log('## ' + n); issues.forEach(i => console.log('   ' + i)); }
    await p.screenshot({ path: path.join('png', n.replace('.svg', '.png')) });
  }
  console.log(`checked ${names.length}, with issues: ${bad}`);
  await b.close();
})();
