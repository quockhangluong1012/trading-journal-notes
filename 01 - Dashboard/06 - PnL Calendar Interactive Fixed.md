---
type: dashboard
dashboard: PnL Calendar Interactive Fixed
calendar_year: 2026
calendar_month: 6
---

# P&L Calendar

> Interactive P&L Calendar: nút **‹ / › / This month** và tab **Daily / Weekly / Monthly** hoạt động trực tiếp trong DataviewJS.

```dataviewjs
/******************************************************************
 * Interactive P&L Calendar - Fixed Layout
 * Source: 05 - Live Trading Journal/Trades
 *
 * Recommended trade fields:
 * date: 2026-06-17T20:09:00
 * symbol: EURUSD
 * direction: Long
 * result: Loss
 * pnl: -41.50
 * r_multiple: -1
 ******************************************************************/

const TRADE_FOLDER = '"Trading Journal/05 - Live Trading Journal/Trades"';
const CURRENCY = "$";
const START_WEEK_ON = "MON"; // "SUN" hoặc "MON"

// Ép dashboard full-width trong Reading View để tránh UI bị vỡ do Readable line length.
const previewView = dv.container.closest(".markdown-preview-view");
if (previewView) previewView.classList.add("pnl-fullwidth-view");

const sourceView = dv.container.closest(".markdown-source-view");
if (sourceView) sourceView.classList.add("pnl-fullwidth-view");

// =========================
// Helpers
// =========================
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

function num(v) {
  if (v === null || v === undefined) return null;

  const s = String(v)
    .replaceAll(",", "")
    .replaceAll("−", "-")
    .replace(/[^\d.\-]/g, "");

  if (s === "" || s === "-" || s === ".") return null;

  const n = Number(s);
  return Number.isFinite(n) ? n : null;
}

function tradeDate(t) {
  const d = first(t, ["date", "trade_date", "tradeDate", "entry_date"]);

  if (d?.toISODate) return d.toISODate();
  if (d instanceof Date) return d.toISOString().slice(0, 10);

  if (d) {
    const m = String(d).match(/\d{4}-\d{2}-\d{2}/);
    if (m) return m[0];
  }

  const fromName = t.file.name.match(/\d{4}-\d{2}-\d{2}/);
  if (fromName) return fromName[0];

  const fromPath = t.file.path.match(/\/(\d{4})\/(\d{2})\/(\d{2})\//);
  if (fromPath) return `${fromPath[1]}-${fromPath[2]}-${fromPath[3]}`;

  return t.file.cday?.toISODate?.() ?? "";
}

function result(t) {
  const raw = toText(first(t, ["result", "outcome", "status", "exit_reason"])).toLowerCase();
  const name = t.file.name.toLowerCase();

  if (
    raw.includes("win") ||
    raw.includes("profit") ||
    raw.includes("take profit") ||
    raw === "tp" ||
    name.includes("win")
  ) return "Win";

  if (
    raw.includes("loss") ||
    raw.includes("stop") ||
    raw.includes("stoploss") ||
    raw.includes("stop loss") ||
    raw === "sl" ||
    name.includes("loss")
  ) return "Loss";

  if (
    raw.includes("be") ||
    raw.includes("break even") ||
    raw.includes("breakeven")
  ) return "BE";

  // fallback theo P&L
  const p = pnlValue(t);
  if (p > 0) return "Win";
  if (p < 0) return "Loss";

  return "Unknown";
}

function pnlValue(t) {
  return num(first(t, [
    "pnl",
    "p&l",
    "profit_loss",
    "profitLoss",
    "realized_pnl",
    "net_pnl",
    "pl"
  ])) ?? 0;
}

function rValue(t) {
  return num(first(t, ["r_multiple", "r", "R", "rMultiple"])) ?? 0;
}

function symbol(t) {
  return toText(first(t, ["symbol", "ticker", "pair", "instrument"])) || "-";
}

function direction(t) {
  return toText(first(t, ["direction", "position", "side"])) || "-";
}

function setup(t) {
  return toText(first(t, ["setup", "model", "playbook"])) || "-";
}

function fmtMoney(v, compact = false) {
  const abs = Math.abs(v);
  const sign = v < 0 ? "-" : "";
  let value;

  if (compact && abs >= 1000) {
    value = `${(abs / 1000).toFixed(abs >= 10000 ? 0 : 2).replace(/\.00$/, "")}K`;
  } else {
    value = abs.toLocaleString(undefined, {
      minimumFractionDigits: abs % 1 === 0 ? 0 : 2,
      maximumFractionDigits: 2
    });
  }

  return `${sign}${CURRENCY}${value}`;
}

function fmtSignedMoney(v, compact = false) {
  if (v > 0) return fmtMoney(v, compact);
  if (v < 0) return fmtMoney(v, compact);
  return `${CURRENCY}0`;
}

function ymd(year, month, day) {
  return `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
}

function monthLabel(year, month) {
  return new Date(year, month - 1, 1).toLocaleString("en-US", {
    month: "long",
    year: "numeric"
  });
}

function winrate(day) {
  const decided = day.wins + day.losses;
  if (decided === 0) return 0;
  return Math.round((day.wins / decided) * 100);
}

function getMonthData(year, month) {
  const monthKey = `${year}-${String(month).padStart(2, "0")}`;

  const trades = dv.pages(TRADE_FOLDER)
    .where(t => t.file && !String(t.file.path).includes("Template"))
    .array()
    .filter(t => tradeDate(t).startsWith(monthKey));

  const daily = {};

  for (const t of trades) {
    const d = tradeDate(t);

    daily[d] = daily[d] ?? {
      date: d,
      pnl: 0,
      r: 0,
      count: 0,
      wins: 0,
      losses: 0,
      be: 0,
      unknown: 0,
      trades: []
    };

    daily[d].pnl += pnlValue(t);
    daily[d].r += rValue(t);
    daily[d].count++;

    const res = result(t);
    if (res === "Win") daily[d].wins++;
    else if (res === "Loss") daily[d].losses++;
    else if (res === "BE") daily[d].be++;
    else daily[d].unknown++;

    daily[d].trades.push(t);
  }

  return { trades, daily };
}

function stateClass(value) {
  if (value > 0) return "win";
  if (value < 0) return "loss";
  return "flat";
}

function safePath(path) {
  return String(path).replaceAll('"', "&quot;");
}

// =========================
// State
// =========================
const page = dv.current();
const now = new Date();

const initialYear =
  Number(page.calendar_year) ||
  Number(page.year) ||
  now.getFullYear();

const initialMonth =
  Number(page.calendar_month) ||
  Number(page.month) ||
  now.getMonth() + 1;

let state = {
  year: initialYear,
  month: initialMonth,
  view: "daily"
};

// =========================
// Render parts
// =========================
function renderDailyView(year, month) {
  const { daily } = getMonthData(year, month);

  const firstDay = new Date(year, month - 1, 1);
  const lastDay = new Date(year, month, 0);
  const daysInMonth = lastDay.getDate();

  let startOffset = firstDay.getDay(); // SUN = 0
  if (START_WEEK_ON === "MON") startOffset = (startOffset + 6) % 7;

  const totalCells = Math.ceil((startOffset + daysInMonth) / 7) * 7;
  const weekCount = totalCells / 7;

  const weekdayLabels = START_WEEK_ON === "MON"
    ? ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    : ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

  const weeks = Array.from({ length: weekCount }, (_, i) => ({
    index: i + 1,
    pnl: 0,
    r: 0,
    count: 0,
    activeDays: 0,
    wins: 0,
    losses: 0,
    be: 0
  }));

  let cells = [];

  const today = new Date();
  const todayKey = ymd(today.getFullYear(), today.getMonth() + 1, today.getDate());

  for (let i = 0; i < totalCells; i++) {
    const day = i - startOffset + 1;
    const weekIndex = Math.floor(i / 7);

    if (day < 1 || day > daysInMonth) {
      cells.push(`<div class="pnl-day pnl-empty"></div>`);
      continue;
    }

    const dateKey = ymd(year, month, day);
    const d = daily[dateKey];

    let cellState = "none";
    if (d && d.pnl > 0) cellState = "win";
    else if (d && d.pnl < 0) cellState = "loss";
    else if (d && d.count > 0) cellState = "flat";

    if (d) {
      weeks[weekIndex].pnl += d.pnl;
      weeks[weekIndex].r += d.r;
      weeks[weekIndex].count += d.count;
      weeks[weekIndex].activeDays++;
      weeks[weekIndex].wins += d.wins;
      weeks[weekIndex].losses += d.losses;
      weeks[weekIndex].be += d.be;
    }

    const tradeItems = d
      ? d.trades.map(t => {
        const res = result(t);
        const resClass = res === "Win" ? "trade-win" : res === "Loss" ? "trade-loss" : "trade-flat";
        return `
          <li>
            <span class="${resClass}">${res}</span>
            · ${symbol(t)} ${direction(t)}
            · ${fmtSignedMoney(pnlValue(t))}
            · ${rValue(t) > 0 ? "+" : ""}${rValue(t).toFixed(2)}R
            <br>
            <a href="${safePath(t.file.path)}" class="internal-link">${t.file.name}</a>
          </li>
        `;
      }).join("")
      : "";

    cells.push(`
      <div class="pnl-day ${cellState}">
        <div class="pnl-date ${dateKey === todayKey ? "today" : ""}">${day}</div>

        ${d ? `
          <div class="pnl-day-center">
            <div class="pnl-day-money ${cellState}">${fmtSignedMoney(d.pnl)}</div>
            <div class="pnl-day-trades">${d.count} Trade${d.count > 1 ? "s" : ""}</div>
            <div class="pnl-day-winrate">${winrate(d)}%</div>
          </div>

          <div class="pnl-tooltip">
            <strong>${dateKey}</strong>
            <div>P&L: <strong>${fmtSignedMoney(d.pnl)}</strong></div>
            <div>R: <strong>${d.r > 0 ? "+" : ""}${d.r.toFixed(2)}R</strong></div>
            <div>W/L/BE: <strong>${d.wins}/${d.losses}/${d.be}</strong></div>
            <ul>${tradeItems}</ul>
          </div>
        ` : ""}
      </div>
    `);
  }

  const weekHtml = weeks.map(w => {
    const cls = stateClass(w.pnl);
    return `
      <div class="pnl-week-box">
        <div class="pnl-week-content">
          <div class="pnl-week-title">Week ${w.index}</div>
          <div class="pnl-week-money ${cls}">${fmtSignedMoney(w.pnl, true)}</div>
          <div class="pnl-week-days">${w.activeDays} day${w.activeDays === 1 ? "" : "s"}</div>
        </div>
      </div>
    `;
  }).join("");

  return `
    <div class="pnl-calendar-wrap">
      <div class="pnl-daily-grid">
        <div class="pnl-main-calendar">
          <div class="pnl-weekdays">
            ${weekdayLabels.map(d => `<div class="pnl-weekday">${d}</div>`).join("")}
          </div>

          <div class="pnl-grid" style="--week-count:${weekCount};">
            ${cells.join("")}
          </div>
        </div>

        <div class="pnl-week-panel" style="--week-count:${weekCount};">
          <div class="pnl-week-panel-header"></div>
          ${weekHtml}
        </div>
      </div>
    </div>
  `;
}

function renderWeeklyView(year, month) {
  const { daily } = getMonthData(year, month);

  const firstDay = new Date(year, month - 1, 1);
  const lastDay = new Date(year, month, 0);
  const daysInMonth = lastDay.getDate();

  let startOffset = firstDay.getDay();
  if (START_WEEK_ON === "MON") startOffset = (startOffset + 6) % 7;

  const totalCells = Math.ceil((startOffset + daysInMonth) / 7) * 7;
  const weekCount = totalCells / 7;

  const weeks = Array.from({ length: weekCount }, (_, i) => ({
    index: i + 1,
    pnl: 0,
    r: 0,
    count: 0,
    activeDays: 0,
    wins: 0,
    losses: 0,
    be: 0,
    dates: []
  }));

  for (let i = 0; i < totalCells; i++) {
    const day = i - startOffset + 1;
    if (day < 1 || day > daysInMonth) continue;

    const weekIndex = Math.floor(i / 7);
    const dateKey = ymd(year, month, day);
    const d = daily[dateKey];

    if (d) {
      weeks[weekIndex].pnl += d.pnl;
      weeks[weekIndex].r += d.r;
      weeks[weekIndex].count += d.count;
      weeks[weekIndex].activeDays++;
      weeks[weekIndex].wins += d.wins;
      weeks[weekIndex].losses += d.losses;
      weeks[weekIndex].be += d.be;
      weeks[weekIndex].dates.push(dateKey);
    }
  }

  return `
    <div class="pnl-weekly-view">
      ${weeks.map(w => {
        const cls = stateClass(w.pnl);
        const decided = w.wins + w.losses;
        const wr = decided ? Math.round(w.wins / decided * 100) : 0;

        return `
          <div class="pnl-week-card">
            <div class="pnl-week-card-top">
              <div>
                <div class="pnl-week-card-title">Week ${w.index}</div>
                <div class="pnl-week-card-sub">${w.dates.length ? w.dates.join(" · ") : "No trading days"}</div>
              </div>
              <div class="pnl-week-card-money ${cls}">${fmtSignedMoney(w.pnl, true)}</div>
            </div>

            <div class="pnl-week-card-stats">
              <div><span>Trades</span><strong>${w.count}</strong></div>
              <div><span>Days</span><strong>${w.activeDays}</strong></div>
              <div><span>Winrate</span><strong>${wr}%</strong></div>
              <div><span>R</span><strong>${w.r > 0 ? "+" : ""}${w.r.toFixed(2)}R</strong></div>
              <div><span>W/L/BE</span><strong>${w.wins}/${w.losses}/${w.be}</strong></div>
            </div>
          </div>
        `;
      }).join("")}
    </div>
  `;
}

function renderMonthlyView(year, month) {
  const { trades, daily } = getMonthData(year, month);

  const days = Object.values(daily).sort((a, b) => a.date.localeCompare(b.date));
  const pnl = days.reduce((s, d) => s + d.pnl, 0);
  const r = days.reduce((s, d) => s + d.r, 0);
  const totalTrades = days.reduce((s, d) => s + d.count, 0);
  const winningDays = days.filter(d => d.pnl > 0).length;
  const losingDays = days.filter(d => d.pnl < 0).length;
  const flatDays = days.filter(d => d.pnl === 0 && d.count > 0).length;

  const wins = trades.filter(t => result(t) === "Win").length;
  const losses = trades.filter(t => result(t) === "Loss").length;
  const decided = wins + losses;
  const wr = decided ? Math.round(wins / decided * 100) : 0;

  return `
    <div class="pnl-monthly-view">
      <div class="pnl-month-cards">
        <div class="pnl-summary-card">
          <span>Monthly P&L</span>
          <strong class="${stateClass(pnl)}">${fmtSignedMoney(pnl, true)}</strong>
        </div>
        <div class="pnl-summary-card">
          <span>Total R</span>
          <strong>${r > 0 ? "+" : ""}${r.toFixed(2)}R</strong>
        </div>
        <div class="pnl-summary-card">
          <span>Trades</span>
          <strong>${totalTrades}</strong>
        </div>
        <div class="pnl-summary-card">
          <span>Winrate</span>
          <strong>${wr}%</strong>
        </div>
        <div class="pnl-summary-card">
          <span>Winning days</span>
          <strong class="win">${winningDays}</strong>
        </div>
        <div class="pnl-summary-card">
          <span>Losing days</span>
          <strong class="loss">${losingDays}</strong>
        </div>
        <div class="pnl-summary-card">
          <span>Flat days</span>
          <strong>${flatDays}</strong>
        </div>
      </div>

      <table class="pnl-table">
        <thead>
          <tr>
            <th>Date</th>
            <th>P&L</th>
            <th>R</th>
            <th>Trades</th>
            <th>W/L/BE</th>
            <th>Winrate</th>
          </tr>
        </thead>
        <tbody>
          ${days.map(d => `
            <tr>
              <td>${d.date}</td>
              <td class="${stateClass(d.pnl)}">${fmtSignedMoney(d.pnl)}</td>
              <td>${d.r > 0 ? "+" : ""}${d.r.toFixed(2)}R</td>
              <td>${d.count}</td>
              <td>${d.wins}/${d.losses}/${d.be}</td>
              <td>${winrate(d)}%</td>
            </tr>
          `).join("")}
        </tbody>
      </table>
    </div>
  `;
}

function render() {
  const { trades, daily } = getMonthData(state.year, state.month);
  const days = Object.values(daily);
  const monthlyPnl = days.reduce((s, d) => s + d.pnl, 0);
  const monthlyR = days.reduce((s, d) => s + d.r, 0);
  const monthlyTrades = days.reduce((s, d) => s + d.count, 0);
  const activeDays = days.length;

  const body =
    state.view === "daily"
      ? renderDailyView(state.year, state.month)
      : state.view === "weekly"
        ? renderWeeklyView(state.year, state.month)
        : renderMonthlyView(state.year, state.month);

  dv.container.innerHTML = `
    <style>
      .pnl-fullwidth-view .markdown-preview-sizer,
      .pnl-fullwidth-view .cm-contentContainer,
      .pnl-fullwidth-view .cm-content,
      .pnl-fullwidth-view .markdown-source-view.mod-cm6 .cm-content {
        max-width: none !important;
        width: 100vw !important;
      }

      .pnl-app {
        --pnl-border: var(--background-modifier-border);  
		--pnl-muted: var(--text-muted);  
		--pnl-green: #059669;  
		--pnl-red: #dc2626;  
		--pnl-green-bg: rgba(34, 197, 94, 0.14);  
		--pnl-green-bg-2: rgba(34, 197, 94, 0.06);  
		--pnl-red-bg: rgba(239, 68, 68, 0.12);  
		--pnl-red-bg-2: rgba(239, 68, 68, 0.05);  
		--pnl-flat-bg: rgba(148, 163, 184, 0.08);  
		--pnl-cell-height: 148px;  
		  
		width: min(1500px, calc(100vw));  
		max-width: calc(100vw);  
		  
		border: 1px solid var(--pnl-border);  
		border-radius: 12px;  
		overflow: hidden;  
		background: var(--background-primary);  
		font-family: var(--font-interface);  
		box-shadow: 0 8px 28px rgba(0,0,0,0.05);
      }

      .pnl-toolbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        padding: 18px 22px;
        border-bottom: 1px solid var(--pnl-border);
        background: var(--background-primary);
      }

      .pnl-left,
      .pnl-right {
        display: flex;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
      }

      .pnl-btn {
        height: 34px;
        min-width: 34px;
        padding: 0 11px;
        border: 1px solid var(--pnl-border);
        border-radius: 8px;
        background: var(--background-primary);
        color: var(--text-normal);
        font-size: 14px;
        font-weight: 800;
        cursor: pointer;
        box-shadow: 0 2px 7px rgba(0,0,0,0.07);
      }

      .pnl-btn:hover {
        background: var(--background-secondary);
      }

      .pnl-arrow {
        font-size: 22px;
        line-height: 1;
      }

      .pnl-title {
        font-size: 22px;
        font-weight: 900;
        letter-spacing: -0.03em;
        margin-left: 6px;
        white-space: nowrap;
      }

      .pnl-this-month {
        border: none;
        background: transparent;
        box-shadow: none;
        font-size: 14px;
        margin-left: 8px;
      }

      .pnl-mini-stats {
        display: flex;
        gap: 12px;
        align-items: center;
        color: var(--pnl-muted);
        font-size: 12px;
        font-weight: 800;
        white-space: nowrap;
      }

      .pnl-mini-stats strong {
        color: var(--text-normal);
      }

      .pnl-tabs {
        display: flex;
        align-items: center;
        gap: 2px;
        padding: 3px;
        border-radius: 9px;
        background: var(--background-secondary);
      }

      .pnl-tab {
        border: none;
        background: transparent;
        color: var(--pnl-muted);
        padding: 6px 14px;
        border-radius: 7px;
        font-size: 13px;
        font-weight: 900;
        cursor: pointer;
      }

      .pnl-tab.active {
        background: var(--background-primary);
        color: var(--text-normal);
        box-shadow: 0 1px 6px rgba(0,0,0,0.13);
      }

      .pnl-calendar-wrap {
        width: 100%;
        overflow-x: auto;
      }

      .pnl-daily-grid {
        display: grid;
        grid-template-columns: minmax(760px, 1fr) 142px;
        min-width: 940px;
      }

      .pnl-main-calendar {
        min-width: 0;
      }

      .pnl-weekdays {
        display: grid;
        grid-template-columns: repeat(7, minmax(100px, 1fr));
        height: 52px;
        border-bottom: 1px solid var(--pnl-border);
        background: var(--background-primary);
      }

      .pnl-weekday {
        display: flex;
        align-items: center;
        justify-content: center;
        color: var(--text-muted);
        font-size: 14px;
        font-weight: 900;
        border-right: 1px solid var(--pnl-border);
      }

      .pnl-weekday:last-child {
        border-right: none;
      }

      .pnl-grid {
        display: grid;
        grid-template-columns: repeat(7, minmax(100px, 1fr));
      }

      .pnl-day {
        height: var(--pnl-cell-height);
        position: relative;
        border-right: 1px solid var(--pnl-border);
        border-bottom: 1px solid var(--pnl-border);
        background: var(--background-primary);
        overflow: visible;
      }

      .pnl-day:nth-child(7n) {
        border-right: none;
      }

      .pnl-day.win {
        background: linear-gradient(135deg, var(--pnl-green-bg), var(--pnl-green-bg-2));
      }

      .pnl-day.loss {
        background: linear-gradient(135deg, var(--pnl-red-bg), var(--pnl-red-bg-2));
      }

      .pnl-day.flat {
        background: var(--pnl-flat-bg);
      }

      .pnl-date {
        position: absolute;
        top: 16px;
        left: 18px;
        width: 30px;
        height: 30px;
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        font-weight: 900;
        color: var(--text-muted);
      }

      .pnl-date.today {
        background: #111827;
        color: white;
      }

      .theme-dark .pnl-date.today {
        background: #f8fafc;
        color: #111827;
      }

      .pnl-day-center {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
      }

      .pnl-day-money {
        font-size: 21px;
        line-height: 1.2;
        font-weight: 950;
        letter-spacing: -0.03em;
        margin-bottom: 12px;
      }

      .pnl-day-money.win,
      .pnl-week-money.win,
      .pnl-week-card-money.win,
      .pnl-summary-card .win,
      .pnl-table .win {
        color: var(--pnl-green);
      }

      .pnl-day-money.loss,
      .pnl-week-money.loss,
      .pnl-week-card-money.loss,
      .pnl-summary-card .loss,
      .pnl-table .loss {
        color: var(--pnl-red);
      }

      .pnl-day-money.flat,
      .pnl-week-money.flat,
      .pnl-week-card-money.flat {
        color: var(--text-normal);
      }

      .pnl-day-trades,
      .pnl-day-winrate {
        color: var(--text-muted);
        font-size: 14px;
        font-weight: 900;
      }

      .pnl-day-trades {
        margin-bottom: 9px;
      }

      .pnl-week-panel {
        display: grid;
        grid-template-rows: 52px repeat(var(--week-count), var(--pnl-cell-height));
        border-left: 1px solid var(--pnl-border);
        background: var(--background-secondary);
      }

      .pnl-week-panel-header {
        border-bottom: 1px solid var(--pnl-border);
      }

      .pnl-week-box {
        border-bottom: 1px solid var(--pnl-border);
        display: flex;
        align-items: center;
        justify-content: center;
      }

      .pnl-week-content {
        width: 88px;
      }

      .pnl-week-title {
        color: var(--text-normal);
        font-size: 14px;
        font-weight: 900;
        margin-bottom: 8px;
      }

      .pnl-week-money {
        font-size: 19px;
        font-weight: 950;
        margin-bottom: 7px;
        letter-spacing: -0.03em;
      }

      .pnl-week-days {
        color: var(--text-muted);
        font-size: 14px;
        font-weight: 900;
      }

      .pnl-tooltip {
        display: none;
        position: absolute;
        z-index: 100;
        left: 14px;
        top: 60px;
        width: 300px;
        padding: 12px 14px;
        border: 1px solid var(--pnl-border);
        border-radius: 12px;
        background: var(--background-primary);
        box-shadow: 0 18px 48px rgba(0,0,0,0.20);
        font-size: 12px;
        line-height: 1.55;
      }

      .pnl-tooltip ul {
        margin: 8px 0 0;
        padding-left: 17px;
      }

      .pnl-day:hover .pnl-tooltip {
        display: block;
      }

      .trade-win {
        color: var(--pnl-green);
        font-weight: 900;
      }

      .trade-loss {
        color: var(--pnl-red);
        font-weight: 900;
      }

      .trade-flat {
        color: var(--text-muted);
        font-weight: 900;
      }

      .pnl-weekly-view,
      .pnl-monthly-view {
        padding: 18px;
      }

      .pnl-weekly-view {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
        gap: 12px;
      }

      .pnl-week-card,
      .pnl-summary-card {
        border: 1px solid var(--pnl-border);
        border-radius: 14px;
        padding: 16px;
        background: var(--background-primary);
      }

      .pnl-week-card-top {
        display: flex;
        justify-content: space-between;
        gap: 16px;
        align-items: flex-start;
        margin-bottom: 14px;
      }

      .pnl-week-card-title {
        font-size: 16px;
        font-weight: 950;
      }

      .pnl-week-card-sub {
        color: var(--text-muted);
        font-size: 12px;
        margin-top: 4px;
      }

      .pnl-week-card-money {
        font-size: 22px;
        font-weight: 950;
        white-space: nowrap;
      }

      .pnl-week-card-stats {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 10px;
      }

      .pnl-week-card-stats div {
        border: 1px solid var(--pnl-border);
        border-radius: 10px;
        padding: 10px;
      }

      .pnl-week-card-stats span,
      .pnl-summary-card span {
        display: block;
        color: var(--text-muted);
        font-size: 11px;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: .06em;
      }

      .pnl-week-card-stats strong {
        display: block;
        font-size: 16px;
        margin-top: 5px;
      }

      .pnl-month-cards {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 12px;
        margin-bottom: 18px;
      }

      .pnl-summary-card strong {
        display: block;
        font-size: 24px;
        margin-top: 8px;
        font-weight: 950;
      }

      .pnl-table {
        width: 100%;
        border-collapse: collapse;
        overflow: hidden;
        border: 1px solid var(--pnl-border);
        border-radius: 12px;
      }

      .pnl-table th,
      .pnl-table td {
        border-bottom: 1px solid var(--pnl-border);
        padding: 10px 12px;
        text-align: left;
      }

      .pnl-table th {
        color: var(--text-muted);
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: .06em;
      }

      @media (max-width: 900px) {
        .pnl-toolbar {
          align-items: flex-start;
          flex-direction: column;
        }

        .pnl-mini-stats {
          flex-wrap: wrap;
          white-space: normal;
        }
      }
    </style>

    <div class="pnl-app">
      <div class="pnl-toolbar">
        <div class="pnl-left">
          <button class="pnl-btn pnl-arrow" data-action="prev-month">‹</button>
          <button class="pnl-btn pnl-arrow" data-action="next-month">›</button>
          <div class="pnl-title">${monthLabel(state.year, state.month)}</div>
          <button class="pnl-btn pnl-this-month" data-action="this-month">This month</button>
        </div>

        <div class="pnl-right">
          <div class="pnl-mini-stats">
            <span>P&L: <strong>${fmtSignedMoney(monthlyPnl, true)}</strong></span>
            <span>R: <strong>${monthlyR > 0 ? "+" : ""}${monthlyR.toFixed(2)}R</strong></span>
            <span>Trades: <strong>${monthlyTrades}</strong></span>
            <span>Days: <strong>${activeDays}</strong></span>
          </div>

          <div class="pnl-tabs">
            <button class="pnl-tab ${state.view === "daily" ? "active" : ""}" data-view="daily">Daily</button>
            <button class="pnl-tab ${state.view === "weekly" ? "active" : ""}" data-view="weekly">Weekly</button>
            <button class="pnl-tab ${state.view === "monthly" ? "active" : ""}" data-view="monthly">Monthly</button>
          </div>
        </div>
      </div>

      ${body}
    </div>
  `;

  // Event bindings
  dv.container.querySelector('[data-action="prev-month"]')?.addEventListener("click", () => {
    state.month -= 1;
    if (state.month < 1) {
      state.month = 12;
      state.year -= 1;
    }
    render();
  });

  dv.container.querySelector('[data-action="next-month"]')?.addEventListener("click", () => {
    state.month += 1;
    if (state.month > 12) {
      state.month = 1;
      state.year += 1;
    }
    render();
  });

  dv.container.querySelector('[data-action="this-month"]')?.addEventListener("click", () => {
    const n = new Date();
    state.year = n.getFullYear();
    state.month = n.getMonth() + 1;
    render();
  });

  dv.container.querySelectorAll("[data-view]").forEach(btn => {
    btn.addEventListener("click", () => {
      state.view = btn.dataset.view;
      render();
    });
  });
}

render();
```

## Lưu ý

- Nút **‹ / › / This month** hoạt động trong phiên xem hiện tại, nhưng không tự sửa frontmatter.
- Khi reload note, dashboard quay lại tháng trong frontmatter:

```yaml
calendar_year: 2026
calendar_month: 6
```

- Nếu muốn mặc định luôn mở tháng hiện tại, hãy xóa hoặc để trống `calendar_year` và `calendar_month`.
