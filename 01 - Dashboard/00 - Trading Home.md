---
type: dashboard
dashboard: Trading Home
---

# Trading Home

> **Folder mapping**
> - Trade notes: `05 - Live Trading Journal/Trades`
> - Mistake database: `06 - Mistake Database`
> - Dashboards: `01 - Dashboard`
>
> Các dashboard này tự đọc trade note ở mọi thư mục con bên dưới `05 - Live Trading Journal/Trades`, ví dụ:
> `05 - Live Trading Journal/Trades/2026/06/17/...`


## Overview

```dataviewjs
const TRADE_FOLDER = '"05 - Live Trading Journal/Trades"';

function first(t, names) {
  for (const n of names) {
    if (t[n] !== undefined && t[n] !== null && t[n] !== "") return t[n];
  }
  return null;
}

function toText(v) {
  if (v === null || v === undefined) return "";
  if (typeof v === "string") return v.replaceAll("[[", "").replaceAll("]]", "").trim();
  if (v.path) return v.path.split("/").pop().replace(/\.md$/, "");
  if (v.display) return String(v.display);
  return String(v);
}

function toArray(v) {
  if (v === null || v === undefined) return [];
  if (Array.isArray(v)) return v;
  if (v.array) return v.array();
  return [v];
}

function tradeDate(t) {
  const d = first(t, ["date", "trade_date", "tradeDate"]);
  if (d?.toISODate) return d.toISODate();
  if (d) return String(d).slice(0, 10);
  const m = t.file.name.match(/\d{4}-\d{2}-\d{2}/);
  if (m) return m[0];
  return t.file.cday?.toISODate?.() ?? "";
}

function result(t) {
  const raw = toText(first(t, ["result", "outcome", "status", "exit_reason"])).toLowerCase();
  const name = t.file.name.toLowerCase();

  if (raw.includes("win") || raw.includes("profit") || raw.includes("take profit") || raw === "tp" || name.includes("win")) return "Win";
  if (raw.includes("loss") || raw.includes("stop") || raw.includes("stoploss") || raw.includes("stop loss") || raw === "sl" || name.includes("loss")) return "Loss";
  if (raw.includes("be") || raw.includes("break even") || raw.includes("breakeven")) return "BE";
  return "Unknown";
}

function num(v) {
  if (v === null || v === undefined) return null;
  const m = String(v).replaceAll(",", "").replaceAll("−", "-").match(/-?\d+(\.\d+)?/);
  return m ? Number(m[0]) : null;
}

function rValue(t) {
  const explicit = num(first(t, ["r_multiple", "r", "R", "rMultiple", "r-multiple"]));
  if (explicit !== null) return explicit;

  // Fallback để dashboard vẫn chạy khi note cũ chưa có r_multiple.
  // Nên thay bằng R thực tế sau khi review.
  if (result(t) === "Loss") return -1;
  if (result(t) === "Win") return 1;
  return 0;
}

function mistakes(t) {
  let out = [];
  for (const key of ["mistakes", "mistake", "Mistake", "errors", "error"]) {
    out.push(...toArray(t[key]));
  }

  return [...new Set(out.map(toText).filter(Boolean))];
}

function symbol(t) {
  return toText(first(t, ["symbol", "ticker", "pair", "instrument"])) || "-";
}

function direction(t) {
  return toText(first(t, ["direction", "position", "side"])) || "-";
}

const trades = dv.pages(TRADE_FOLDER)
  .where(t => t.file && !String(t.file.path).includes("Template"))
  .array();

trades.sort((a, b) => tradeDate(a).localeCompare(tradeDate(b)));

const total = trades.length;
const wins = trades.filter(t => result(t) === "Win").length;
const losses = trades.filter(t => result(t) === "Loss").length;
const be = trades.filter(t => result(t) === "BE").length;
const winrate = (wins + losses) > 0 ? (wins / (wins + losses) * 100) : 0;
const totalR = trades.reduce((sum, t) => sum + rValue(t), 0);

const allMistakes = {};
for (const t of trades) {
  for (const m of mistakes(t)) allMistakes[m] = (allMistakes[m] ?? 0) + 1;
}
const topMistake = Object.entries(allMistakes).sort((a, b) => b[1] - a[1])[0];

dv.container.innerHTML = `
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:16px 0;">
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;">
    <div style="font-size:12px;opacity:.7;">Total trades</div>
    <div style="font-size:28px;font-weight:700;">${total}</div>
  </div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;">
    <div style="font-size:12px;opacity:.7;">Win / Loss / BE</div>
    <div style="font-size:28px;font-weight:700;">${wins}/${losses}/${be}</div>
  </div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;">
    <div style="font-size:12px;opacity:.7;">Winrate</div>
    <div style="font-size:28px;font-weight:700;">${winrate.toFixed(1)}%</div>
  </div>
  <div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;">
    <div style="font-size:12px;opacity:.7;">Total R</div>
    <div style="font-size:28px;font-weight:700;">${totalR.toFixed(2)}R</div>
  </div>
</div>

<div style="border:1px solid var(--background-modifier-border);border-radius:12px;padding:14px;margin:12px 0;">
  <div style="font-size:12px;opacity:.7;">Top repeated mistake</div>
  <div style="font-size:18px;font-weight:650;">${topMistake ? `${topMistake[0]} × ${topMistake[1]}` : "No mistake data found"}</div>
</div>
`;

dv.header(2, "Recent Trades");

dv.table(
  ["Date", "Trade", "Symbol", "Direction", "Result", "R", "Mistakes"],
  trades.slice(-10).reverse().map(t => [
    tradeDate(t),
    t.file.link,
    symbol(t),
    direction(t),
    result(t),
    `${rValue(t).toFixed(2)}R`,
    mistakes(t).join(", ")
  ])
);
```

## Notes

- Nếu trade note chưa có `r_multiple`, dashboard sẽ tạm tính **Loss = -1R**, **Win = +1R** để chart vẫn chạy.
- Khi review xong, nên cập nhật R thực tế để Performance Dashboard chính xác hơn.
