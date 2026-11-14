## Quant & Market Dashboard

### Liquidity and volatility

- **Overnight/weekend:** U.S. cash markets are closed. Current ES/NQ spreads, depth, overnight volume, executable ETF NBBO and Treasury-market depth remain unverified. Friday close is a cautious state proxy, not current executable liquidity. Refresh feeds when each venue reopens; do not carry Friday spreads into the next session.
- **Funding:** Latest verified SOFR is **3.90% for November 12**, updated November 13 at **07:02 CST**. This lagged fixing cannot diagnose current stress. [FRED](https://fred.stlouisfed.org/series/SOFR).
- **Regime: Moderate; medium confidence.** VIX closed at **19.30 on November 13**, up from **18.70**; the provider labels its 16:00 EST / 15:00 CST observation delayed. House bands: below 15 low, 15–25 moderate, 25–35 high, above 35 stressed; descriptive conventions, not calibrated forecasts. Skew, term structure and dealer gamma remain unverified. Weekend gap risk remains. [VIX](https://chartexchange.com/symbol/index-vix/historical/).

### Factor proxies

| Factor | ETF | Nov 12→13 | Oct 9→Nov 13 (~1 month) |
|---|---|---:|---:|
{ROWS}

Source-linked split-adjusted Close-column price returns, excluding distributions, through November 13 at **16:00 EST / 15:00 CST**. October 9 baselines are archived from earlier editions; latest closes were rechecked today. Corporate actions were not independently validated. These imperfect ETF proxies do not isolate factor premia. Low volatility rose Friday while the other five proxies declined; momentum and growth remain negative over the longer window.

### Execution and microstructure

- Next regular cash opening auction: **Monday November 16, 08:30 CST / 14:30 UTC**. Refresh release calendars and overnight positions before staging orders. Replace pre-PPI flags with the confirmed release vintage; do not reuse stale event-state inputs.
- SPY/QQQ: inspect quote age, NBBO spreads, displayed depth, auction imbalances and ES/NQ basis. Use bounded limits and participation caps; stress slippage, gaps, cancellations, latency and missed fills. Small index moves can conceal thin depth or concentrated constituent risks.
- Options: reconcile Friday expiries and verify next-session contracts, deliverables, settlement and exercise obligations. Reject stale, crossed or one-sided quotes. Near-expiry gamma and event-volatility repricing can amplify execution risk; dealer positioning, expiry concentrations, pinning and flow magnitude remain unknown. Do not infer gamma direction from open interest alone.

**Research watchlist:** SPY, QQQ, IWM, RSP, TLT; ES, NQ, ZN, VX; MTUM, VLUE, QUAL, IWF, SPLV; AMAT, NVDA, IBM.

### DRL Improvements for the MATLAB System

1. Enforce drawdown, exposure, participation and stale-data limits outside the policy, with an explicit safe fallback.
2. Penalize spread, impact, turnover, latency and missed fills; stress permanent and transient impact alongside tail losses.
3. Use purged walk-forward evaluation, training-only preprocessing and an untouched final holdout; separate event and quiet regimes.
4. Randomize depth, observation delays and fill probabilities; test abstention and hard risk compliance under distribution shift.

### Model hygiene

Audit leakage, survivorship bias, look-ahead bias, corporate actions, stale options quotes, multiple testing, calibration and drift. Preserve point-in-time universes, release vintages and actual availability timestamps. Fit preprocessing inside folds. Forecast targets must match feasible actions; daily OHLCV cannot validate order-book fills.

### MATLAB optimization patterns

- Use named-zone timetables and causal synchronization; retain quote and release timestamps separately.
- Vectorize rolling features, preallocate logs and profile bottlenecks.
- Parallelize independent folds or Bayesian trials with reproducible random streams and fixed search budgets.
- Use GPUs for sufficiently large batches; keep forecasts, environments, execution simulation and risk controls modular.

### High-value quant research question

**Does a neural execution surrogate retain its net advantage under held-out impact kernels and realistic fill uncertainty?**

Compare it with the underlying optimizer using matched risk, seeds and action opportunities, measuring cost, constraint breaches and missed fills. This tests whether approximation speed survives model misspecification rather than only interpolation within the training distribution.
