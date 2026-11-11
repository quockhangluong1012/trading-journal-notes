# CLAUDE.md — Trading Journal

Guide for working in this Obsidian vault. **Instructions are in English; content you write into notes follows the vault's Vietnamese style** (frontmatter keys stay English; prose, headings inside notes, and checklists are Vietnamese where existing notes are).

## What this vault is

A personal ICT (Inner Circle Trader) trading journal for Luong Quoc Khang. It covers four jobs: **logging trades**, **backtesting**, **a learning knowledge base (ICT concepts/models/playbooks)**, and **goal + weekly-review tracking**. Primary strategy is the **ICT 2022 Model**; markets traded include NQ1/NDX (NAS100), EURUSD, GBPUSD, XAUUSD. Risk discipline is strict (≤0.5% per trade is a tracked rule).

## Tooling assumptions

- This is an **Obsidian vault**, not a code project. There is no build/test step.
- Dashboards rely on the **Dataview** plugin with **JavaScript Queries (dataviewjs)** enabled. When you add notes, fill frontmatter correctly so dashboards aggregate them. Do not break existing `dataview`/`dataviewjs` code blocks.
- Links between notes use `[[Wikilinks]]`. Mistakes, concepts, and goals are cross-linked this way.
- Images live alongside notes and are embedded with `![[filename.png]]`.

## Folder map

```
00 - Inbox/              Daily notes, quick capture
01 - Dashboard/          Dataview dashboards (Home, Loss, Mistake, Performance, Process, ICT 2022, PnL Calendar)
02 - Trading Knowledge/  Concepts/ (28 ICT concepts) and Models/ (ICT 2022, MMBM, MMSM, Venom, etc.)
03 - Playbooks/          3.1 Checklists, 3.2 Setups
04 - Backtesting/        Backtest notes + _Backtest Dashboard
05 - Live Trading Journal/  Trades/ and Screenschoots/ (note: existing spelling)
06 - Mistake Database/   One note per mistake type, linked from trades & reviews
07 - Reviews/            Weekly reviews
08 - Templates/          Source templates — copy these, don't reinvent
09 - Goal Tracking/      Goal Dashboard, Roadmap, Skill Metrics, Goals/{Long,Mid,Short Term}
```

## Templates — always start from these

When creating a new note, copy the matching template in `08 - Templates/` and fill it. Never invent a new structure when a template exists.

- **New trade** → `trade log.md`
- **Backtest** → `Backtest templete.md`
- **ICT concept** → `ICT_Concept_Template.md`
- **Goal** → `Goal_Template.md`
- **Weekly review** → `Weekly_Trading_Review_ICT_Obsidian.md`

## Naming & location conventions

- **Trades**: `05 - Live Trading Journal/Trades/YYYY/MM/DD/` with filename `Result - NN - Trade YYYY-MM-DD SYMBOL Position.md` — e.g. `Win - 01 - Trade 2026-03-31 NQ1 Long.md`. `Result` is `Win`/`Loss`/`BE`; `NN` is the trade number that day (01, 02…).
- **Screenshots**: `05 - Live Trading Journal/Screenschoots/YYYY/MM/` named `SYMBOL-YYYYMMDD-TF-N.png` (TF = D1/H1/M5/M1).
- **Backtests**: `04 - Backtesting/`, filename like `NAS100-2026-06-18-Long-...md`.
- **Concepts**: `02 - Trading Knowledge/Concepts/<Concept Name>.md`.
- **Mistakes**: `06 - Mistake Database/Mistake - <description>.md`.
- **Goals**: under `09 - Goal Tracking/Goals/<Long|Mid|Short Term ...>/`.

## Frontmatter that dashboards depend on

Match existing keys exactly — dashboards parse these. Key examples:

- **Trade**: `date, symbol, position, result, session, setup, entry_model, entry_timeframe, higher_timeframe_bias, bias_correct, entry_price, exit_price, take_profit, stop_loss, pnl, r_multiple, planned_rr, risk_percent, confidence, mistakes, emotions, tags`.
- **Backtest**: `type: backtest, backtest_date, trade_date, symbol, position, result, session, setup, entry_model, entry_timeframe, htf_bias, bias_correct, poi_type, liquidity_swept, displacement, mss, fvg_valid, entry_price, stop_loss, take_profit, r_planned, r_multiple, grade, followed_plan, tags`.
- **ICT concept**: `type: ict-concept, concept, aliases, tags, status (seed|developing|tested|mastered), category, timeframes, models, markets, importance (1-5), confidence (1-5), last_reviewed, created, updated, related_concepts, prerequisites, common_mistakes`.
- **Goal**: `type: goal, horizon (Long|Mid|Short), category, status, priority, progress (0-100), metric, baseline, target, phase, start_date, due_date, tags`. Progress is computed from checkboxes under `## Cột mốc` (milestones) — keep that heading exact.
- **Weekly review**: `type: weekly-trading-review, week, start_date, end_date, market_focus, strategy, status, tags`.

## House rules for working here

- **Don't fabricate trade data.** Prices, P&L, R-multiples, and screenshots come from the user. Leave fields blank rather than guessing.
- **Preserve Dataview blocks** verbatim unless explicitly asked to change a query.
- **Cross-link**: tie trades to relevant `[[Mistake - ...]]` and `[[Concept]]` notes; tie goals to `[[01 - Roadmap]]` and `[[02 - Skill Metrics]]`.
- **Respect the risk framework** (e.g. ≤0.5% per trade, daily/weekly loss limits, circuit breakers). When reviewing trades, flag rule violations rather than rationalizing them — the journal's purpose is honest process review, where a "good loss" beats a "bad win".
- **Keep the Vietnamese voice** in note bodies, checklists, and callouts to match the vault; English is fine for new dashboards/frontmatter.
- **Use existing callout styles** (`> [!info]`, `> [!warning]`, `> [!summary]`, etc.) consistent with templates.
- When asked to summarize performance, prefer reading the relevant dashboard's logic and the underlying trade frontmatter over re-deriving numbers by hand.
