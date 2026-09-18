# MATLAB Event-Risk and Execution Checklist

Use this checklist before testing or deploying a MATLAB strategy around macro releases, Federal Reserve decisions, index rebalances, monthly expiry, earnings, or other scheduled events.

It is a research-control framework—not a trading signal or individualized financial advice.

## 1. Define the event before using the data

- Record the event name, scheduled timestamp, timezone, release source, and revision policy.
- Store the first-known value and timestamp separately from revised observations.
- Define pre-event, announcement, price-discovery, and post-event windows before testing.
- Keep unscheduled headlines and scheduled announcements in different event classes.
- Mark holidays, shortened sessions, expiry dates, auctions, and settlement windows.

## 2. Validate the market data

- Confirm symbol, venue, timezone, session, adjustment method, and price basis.
- Reject stale, crossed, zero-bid, one-sided, or obviously erroneous quotes.
- Preserve quote age, spread, displayed depth, volume, and trading-halt state.
- Treat premarket, regular trading, closing auction, and overnight trading as separate liquidity regimes.
- Use point-in-time constituents and corporate-action data to prevent survivorship and look-ahead bias.

## 3. Build an event-state vector

Candidate state variables include:

- Surprise relative to the timestamped consensus.
- Two-year and ten-year yield changes.
- NQ–ES relative strength.
- SPY/QQQ gap and opening-auction imbalance.
- VIX level and VX term-structure slope.
- Oil, dollar, and credit-spread changes.
- Factor dispersion across momentum, value, quality, size, growth, and low volatility.
- Quote age, spread, depth, auction state, expiry state, and time since the announcement.

Do not allow the learned policy to infer event timing from future bars or revised data.

## 4. Model executable costs

- Use prevailing bid/ask quotes rather than closing prices or midpoint fills by default.
- Model spread, fees, partial fills, queue position, latency, market impact, and nonlinear slippage.
- Increase costs when depth falls, volatility rises, or participation exceeds a defined share of volume.
- Rebuild option surfaces after the event; do not carry stale pre-event volatility, skew, or gamma assumptions into the post-event book.
- Separate opening-auction, continuous-session, and closing-auction cost models.

## 5. Keep risk constraints outside the reward

Enforce independent limits for:

- Drawdown and daily loss.
- Gross and net exposure.
- Concentration and correlated exposure.
- Turnover and order participation.
- Minimum liquidity and maximum spread.
- Stale data, rejected orders, and disconnected market feeds.

The reward can penalize downside risk and implementation shortfall, but it should not be the only enforcement layer.

## 6. Use a defensible evaluation design

- Apply purged, embargoed walk-forward validation.
- Freeze benchmarks, features, cost assumptions, and decision rules before the final test.
- Preserve untouched event blocks for final evaluation.
- Use multiple random seeds for stochastic models and policies.
- Compare against simple baselines: no trade, buy-and-hold, linear models, and deterministic event rules.
- Report performance by event type, volatility regime, liquidity regime, and direction—not only an aggregate score.
- Retain rejected trials and correct for multiple testing.

## 7. Stress the failure modes

Randomize or replay:

- Gaps and reversals.
- Curve shocks and volatility repricing.
- Spread widening and depth collapse.
- Partial fills and delayed fills.
- Stale quotes and missing observations.
- Latency and rejected orders.
- Trading halts and shortened sessions.
- Options pinning, expiry flows, and nonlinear impact.

## 8. MATLAB implementation pattern

- Align market, macro, auction, and event data with `timetable`, `retime`, and `synchronize`.
- Preallocate episode and cost buffers.
- Vectorize feature calculations where possible.
- Profile environment steps before adding parallel execution.
- Run parallel `bayesopt` only across independent purged folds.
- Use reproducible random streams and log seed, code version, data version, and parameter set.
- Keep data, feature, environment, execution-cost, risk-constraint, agent, and evaluation modules separate.
- Reserve GPUs for workloads large enough to benefit from them; keep data movement in the timing benchmark.

## 9. Pre-deployment gate

Do not deploy unless all answers are **yes**:

- Are timestamps, revisions, sessions, and corporate actions controlled?
- Are the fills executable under the modeled spread, depth, and latency?
- Did the strategy survive untouched event blocks and stronger cost assumptions?
- Are risk controls independent of the model and tested under failure injection?
- Can the system stop safely when quotes, connectivity, or orders become unreliable?
- Can every decision be reconstructed from immutable logs?

## 10. Post-event review

- Compare forecast, decision, order, fill, and realized-cost timestamps.
- Attribute P&L separately to signal, beta, volatility, carry, and execution.
- Record rejected orders, stale data, overrides, and risk-limit activations.
- Recalibrate only after the review window closes; never rewrite the original decision record.
- Add the event to the next walk-forward cycle without contaminating the test that just concluded.

---

Published by **Market State Lab** as a companion to the free *Quant Market Brief*.

- [Subscribe by email](https://market-state-lab.ghost.io/?utm_source=github&utm_medium=checklist&utm_campaign=qmb_growth#/portal/signup)
- [Read the LinkedIn newsletter](https://www.linkedin.com/newsletters/market-state-lab-7492957414569324544/)
- [Browse the Quant Market Brief archive](https://github.com/rsh63/market-state-lab)

