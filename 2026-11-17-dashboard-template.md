## Quant & Market Dashboard

### Liquidity and volatility

- **Overnight/premarket:** Regular U.S. cash trading has not opened. Current ES/NQ spreads, depth, overnight volume, executable ETF NBBO and Treasury-market depth remain unverified. Use the prior-close index report in story 3 and Monday ETF closes as cautious state proxies, not executable liquidity. Refresh feeds and do not carry prior-session spreads into the opening auction.
- **Funding:** Latest verified SOFR is **3.90% for November 13**, updated November 16 at **07:02 CST**. This lagged fixing cannot diagnose current stress. [FRED](https://fred.stlouisfed.org/series/SOFR).
- **Regime: Moderate; medium confidence.** VIX was **23.29 on November 17 at 06:18 EST / 05:18 CST**, versus Monday close **22.91**; the provider labels this observation delayed. House bands: below 15 low, 15–25 moderate, 25–35 high, above 35 stressed; descriptive conventions, not calibrated forecasts. Skew, term structure and dealer gamma remain unverified. Opening-gap risk remains. [VIX](https://chartexchange.com/symbol/index-vix/historical/).

### Factor proxies

| Factor | ETF | Nov 13→16 | Oct 9→Nov 16 (~1 month) |
|---|---|---:|---:|
{ROWS}

Source-linked split-adjusted Close-column price returns, excluding distributions, through November 16 at **16:00 EST / 15:00 CST**. All three reference closes were rechecked today. Corporate actions were not independently validated. These imperfect ETF proxies do not isolate factor premia. All six proxies declined Monday; low volatility fell least and remains positive over the longer window.

### Execution and microstructure

- Next regular cash opening auction: **today, Tuesday November 17, 08:30 CST / 14:30 UTC**. Refresh release calendars and overnight positions before staging orders. FOMC minutes are scheduled Wednesday November 18 at 13:00 CST / 19:00 UTC; refresh the other release times before execution. [Fed calendar](https://www.federalreserve.gov/newsevents/2026-november.htm).
- SPY/QQQ: inspect quote age, NBBO spreads, displayed depth, auction imbalances and ES/NQ basis. Use bounded limits and participation caps; stress slippage, gaps, cancellations, latency and missed fills. Small index moves can conceal thin depth or concentrated constituent risks.
- Options: reconcile Friday expiries and verify next-session contracts, deliverables, settlement and exercise obligations. Reject stale, crossed or one-sided quotes. Near-expiry gamma and event-volatility repricing can amplify execution risk; dealer positioning, expiry concentrations, pinning and flow magnitude remain unknown. Do not infer gamma direction from open interest alone.

**Research watchlist:** SPY, QQQ, IWM, RSP, TLT; ES, NQ, ZN, VX; MTUM, VLUE, QUAL, IWF, SPLV; IBM, HD, NVDA; LQD and HYG for credit-risk research.

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

**Do model-transfer stress tests reject strategies that pass ordinary calibration and walk-forward checks?**

Compare policies with matched calibration and walk-forward scores under alternative information-arrival and execution models. Select scenarios within training folds, freeze policies and report net return, tail loss and constraint breaches out of sample. This tests whether familiar validation misses model dependence.
