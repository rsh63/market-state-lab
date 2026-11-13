## Quant & Market Dashboard

### Liquidity and volatility

- **Overnight:** The reported 05:33 CST futures snapshot shows small, mixed moves. Current ES/NQ spreads, displayed depth, overnight volume, executable ETF NBBO and Treasury-market depth remain unverified. Direction is a cautious sentiment proxy, not a liquidity rating; refresh execution feeds before trading.
- **Funding:** Latest verified SOFR is **3.89% for November 10**, updated November 12 at **07:02 CST**. Today's update was unavailable at cutoff. This lagged fixing cannot diagnose current funding stress. [FRED](https://fred.stlouisfed.org/series/SOFR).
- **Regime: Moderate; medium confidence, with concentrated event risk.** Delayed VIX was **18.22 at November 13 07:04 EST / 06:04 CST**, versus November 12 close **18.70**. House bands: below 15 low, 15–25 moderate, 25–35 high, above 35 stressed; descriptive conventions, not calibrated forecasts. Skew, term structure and dealer gamma remain unverified. [VIX](https://chartexchange.com/symbol/index-vix/historical/).

### Factor proxies

| Factor | ETF | Nov 11→12 | Oct 9→Nov 12 (~1 month) |
|---|---|---:|---:|
{ROWS}

Source-linked split-adjusted Close-column price returns, excluding distributions, through November 12 at **16:00 EST / 15:00 CST**. October 9 baselines are archived from earlier editions; latest closes were rechecked today. Corporate actions were not independently validated. These imperfect ETF proxies do not isolate factor premia. Momentum rose slightly Thursday while the other five proxies declined; low volatility remains positive over the longer window.

### Execution and microstructure

- PPI: **07:30 CST / 13:30 UTC today**; cash opening auction: **08:30 CST / 14:30 UTC**. Results remain unknown at cutoff. Separate observations and risk settings across the release; recheck other calendars before staging orders. [BLS calendar](https://www.bls.gov/schedule/2026/11_sched_list.htm).
- SPY/QQQ: inspect quote age, NBBO spreads, displayed depth, auction imbalances and ES/NQ basis. Use bounded limits and participation caps; stress slippage, gaps, cancellations, latency and missed fills. Small index moves can conceal thin depth or concentrated constituent risks.
- Options: verify Friday expiries, deliverables, settlement and exercise obligations. Reject stale, crossed or one-sided quotes. Near-expiry gamma and event-volatility repricing can amplify execution risk; dealer positioning, expiry concentrations, pinning and flow magnitude remain unknown. Do not infer gamma direction from open interest alone.

**Research watchlist:** SPY, QQQ, IWM, RSP, TLT; ES, NQ, ZN, VX; MTUM, VLUE, QUAL, IWF, SPLV; CSCO, NVDA, GOOGL.

### DRL Improvements for the MATLAB System

1. Enforce drawdown, exposure, participation and stale-data limits outside the policy, with an explicit safe fallback.
2. Penalize spread, impact, turnover, latency and missed fills; include forecast instability and tail losses in evaluation.
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

**At matched risk and trading costs, do action-aligned distributional forecasts improve net decisions more than a more accurate but less stable point forecast?**

Compare identical policies with and without forecast inputs, matching seeds, search budgets and action opportunities across held-out regimes. This tests decision value and stability rather than predictive accuracy alone; electricity-market simulation evidence does not establish transfer to equities.
