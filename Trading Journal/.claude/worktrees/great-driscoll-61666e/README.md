# Trading Journal — AI Second Brain (Obsidian + Claude)

A personal **ICT (Inner Circle Trader)** trading journal and knowledge base, built as an Obsidian vault and designed to be worked on together with Claude. It's not a code project — there's no build or test step — it's a structured set of Markdown notes with Dataview dashboards on top, plus a `CLAUDE.md` that teaches Claude the vault's conventions so it can safely read, log, and analyze trades on your behalf.

## What it's for

The vault covers four jobs for **Luong Quoc Khang**, trading the **ICT 2022 Model** across NQ1/NDX (NAS100), EURUSD, GBPUSD, and XAUUSD:

1. **Logging live trades** — one note per trade, structured frontmatter, linked to mistakes and concepts.
2. **Backtesting** — same structure as live trades, used to validate setups before risking capital.
3. **Learning knowledge base** — ICT concepts, models, and playbooks, cross-linked as they're learned and applied.
4. **Goal & weekly-review tracking** — roadmap, skill metrics, and honest process review.

Risk discipline is a first-class concern: **≤0.5% risk per trade** is a tracked, enforced rule, and reviews are meant to flag violations rather than rationalize them.

## Why Claude is in the loop

`CLAUDE.md` at the repo root documents the vault's folder structure, naming conventions, and exact frontmatter schemas so an AI assistant can:

- Create new trade/backtest/concept/goal notes **from the correct template**, correctly named and filed.
- Fill frontmatter that the Dataview dashboards depend on, **without breaking existing queries**.
- Cross-link trades to mistakes and concepts, and goals to the roadmap and skill metrics.
- Summarize performance by reading dashboard logic and trade frontmatter — never by fabricating numbers.
- Review trades for rule violations honestly, since the point of the journal is process discipline, not flattering the P&L.

If you're using Claude Code or Claude in the Obsidian vault, start by reading `CLAUDE.md` — it is the source of truth for how notes should be structured.

## Vault structure

```
00 - Inbox/              Daily notes, quick capture, daily task lists
01 - Dashboard/          Dataview dashboards (Home, Loss, Mistake, Performance, Process, ICT 2022, PnL Calendar)
02 - Trading Knowledge/  Concepts/ (ICT concepts) and Models/ (ICT 2022, MMBM, MMSM, Venom, One Shot One Kill, etc.)
03 - Playbooks/          3.1 Checklists (entry, risk/circuit breaker) and 3.2 Setups
04 - Backtesting/        Backtest notes + _Backtest Dashboard
05 - Live Trading Journal/  Trades/ (by year/month/day) and Screenschoots/ (sic — existing spelling, kept for compatibility)
06 - Mistake Database/   One note per recurring mistake, linked from trades & reviews
07 - Reviews/            Weekly reviews
08 - Templates/          Source templates — every new note starts here
09 - Goal Tracking/      Goal Dashboard, Roadmap, Skill Metrics, Goals/{Long,Mid,Short Term}
```

## Requirements

- [Obsidian](https://obsidian.md/)
- The **Dataview** community plugin, with **JavaScript Queries (dataviewjs)** enabled — the dashboards under `01 - Dashboard/` and `04 - Backtesting/_Backtest Dashboard.md` depend on it.

## Getting started

1. Open this repo as a vault in Obsidian and enable the Dataview plugin.
2. Open `01 - Dashboard/00 - Trading Home.md` as your daily entry point.
3. To log a new trade, backtest, concept, or goal, **copy the matching template** from `08 - Templates/` rather than writing a note from scratch — this keeps frontmatter and headings compatible with the dashboards.
4. Follow the naming conventions below so files sort and link correctly.

## Naming conventions

| Note type | Location | Filename pattern |
|---|---|---|
| Trade | `05 - Live Trading Journal/Trades/YYYY/MM/DD/` | `Result - NN - Trade YYYY-MM-DD SYMBOL Position.md` (e.g. `Win - 01 - Trade 2026-03-31 NQ1 Long.md`) |
| Screenshot | `05 - Live Trading Journal/Screenschoots/YYYY/MM/` | `SYMBOL-YYYYMMDD-TF-N.png` |
| Backtest | `04 - Backtesting/` | `NAS100-2026-06-18-Long-...md` |
| Concept | `02 - Trading Knowledge/Concepts/` | `<Concept Name>.md` |
| Mistake | `06 - Mistake Database/` | `Mistake - <description>.md` |
| Goal | `09 - Goal Tracking/Goals/<Long\|Mid\|Short Term ...>/` | `<Goal description>.md` |

## Frontmatter dashboards depend on

Dashboards parse frontmatter directly, so keys must match exactly:

- **Trade**: `date, symbol, position, result, session, setup, entry_model, entry_timeframe, higher_timeframe_bias, bias_correct, entry_price, exit_price, take_profit, stop_loss, pnl, r_multiple, planned_rr, risk_percent, confidence, mistakes, emotions, tags`
- **Backtest**: `type: backtest, backtest_date, trade_date, symbol, position, result, session, setup, entry_model, entry_timeframe, htf_bias, bias_correct, poi_type, liquidity_swept, displacement, mss, fvg_valid, entry_price, stop_loss, take_profit, r_planned, r_multiple, grade, followed_plan, tags`
- **ICT concept**: `type: ict-concept, concept, aliases, tags, status (seed|developing|tested|mastered), category, timeframes, models, markets, importance (1-5), confidence (1-5), last_reviewed, created, updated, related_concepts, prerequisites, common_mistakes`
- **Goal**: `type: goal, horizon (Long|Mid|Short), category, status, priority, progress (0-100), metric, baseline, target, phase, start_date, due_date, tags` — progress is computed from checkboxes under the `## Cột mốc` (milestones) heading, so keep that heading exact
- **Weekly review**: `type: weekly-trading-review, week, start_date, end_date, market_focus, strategy, status, tags`

See `CLAUDE.md` for the full schema reference.

## House rules

- **Never fabricate trade data.** Prices, P&L, R-multiples, and screenshots come only from the trader; leave fields blank rather than guessing.
- **Preserve Dataview blocks verbatim** unless a query change is explicitly requested.
- **Cross-link everything**: trades → `[[Mistake - ...]]` and concept notes; goals → `[[01 - Roadmap]]` and `[[02 - Skill Metrics]]`.
- **Respect the risk framework**: ≤0.5% per trade, daily/weekly loss limits, circuit breakers. Reviews should flag violations, not rationalize them — a good loss beats a bad win.
- **Keep the Vietnamese voice** in note bodies, checklists, and callouts, matching existing notes; frontmatter keys and dashboard code stay in English.
- **Use existing callout styles** (`> [!info]`, `> [!warning]`, `> [!summary]`, etc.) consistent with the templates.

## Current contents (snapshot)

- 60 ICT concept notes, 6 model notes (ICT 2022, MMBM, MMSM, Venom, One Shot One Kill, Friday Profit-Taking)
- 7 dashboards (Home, Loss Review, Mistake Frequency, Performance, Process Quality, ICT 2022 Model Review, PnL Calendar)
- 7 mistake-database entries
- 29 logged live trades, plus an ongoing backtesting log
- Goal tracking across Long/Mid/Short-term horizons with a Roadmap and Skill Metrics dashboard
