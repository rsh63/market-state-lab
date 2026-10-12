# Methodology and source standards

## Story selection

Each Quant Market Brief contains exactly five non-duplicative stories:

1. AI, machine learning, or MATLAB
2. Algorithmic trading or quantitative finance
3. U.S. markets, SPY/QQQ, or options
4. U.S. economics or the Federal Reserve
5. Major technology or business

Selection favors primary sources, official calendars and data, peer-reviewed research, established wire services, and high-quality financial reporting. A preprint is identified as a preprint. Company guidance is identified as company guidance.

## Data timestamps

Every market datum should be labeled as live, delayed, indicative, prior close, or latest verified snapshot. When the provider does not expose an exact refresh time, the issue states that limitation. Numbers from different as-of dates are not combined into a synthetic precision score.

## Volatility regime

The public regime label uses four states: low, moderate, high, and stressed. Classification weighs:

- implied volatility level and term structure when verified;
- realized range and cross-asset volatility;
- Treasury and credit behavior;
- event risk and gap risk;
- observable liquidity degradation.

If live implied-volatility or depth data are unavailable, the label is a cautious qualitative synthesis with reduced confidence—not a model output.

## Factor panel

Practical ETF proxies are used for interpretability. The defaults below align with the securities used in the October 8–11, 2026 editions; they are an operational convention, not a claim that one ETF is a superior factor measure.

| Factor | Default proxy | Permitted alternative |
|---|---|---|
| Momentum | MTUM | — |
| Value | VLUE | VTV |
| Quality | QUAL | — |
| Size | IWM | — |
| Growth | IWF | VUG |
| Low volatility | SPLV | USMV |

### Selection and disclosure

Use the default consistently across editions and throughout each reported return window. A permitted alternative may be used when comparable, verifiable default-proxy data are unavailable, or for an explicitly identified research comparison. Disclose the actual ticker, reason for substitution, effective date, source, endpoint dates and price-adjustment basis. Do not choose a proxy because its recent performance supports a preferred narrative. If neither proxy has suitable data, omit the return and state the gap.

The ticker printed in a historical edition governs reproduction of that edition. Do not substitute today's default into historical calculations, splice different ETFs into one return series, or treat a proxy change as market performance. For comparisons across a change, recompute a separate, clearly labeled comparison using the same ETF and basis over a common window; retain the original published series.

### Return calculations and dates

The standard panel reports close-to-close, split-adjusted **price returns excluding dividends**:

`Return (%) = 100 × (P_end / P_start − 1)`

Here, both prices are closing prices for the same ETF, from a consistent source and split-adjustment basis. The daily return compares the latest completed trading-session close with the preceding trading-session close. Four weeks means 28 calendar days between target endpoints, not an assumed 20 observations: use the latest completed session as the end and the last common trading session on or before 28 calendar days earlier as the start. Print the actual dates and disclose any holiday adjustment. Weekend editions retain the latest completed session and do not imply new weekend returns.

Use common endpoint dates and adjustment conventions across the panel. If observations cannot be aligned, mark the panel as an indicative, non-synchronous snapshot and avoid a definitive performance ranking. Retain source snapshots and underlying endpoint prices for reproduction; calculate with unrounded prices and round only the displayed percentage.

Do not use a dividend-adjusted “adjusted close” as though it were split-only data. Any dividend-reinvested total-return comparison must be separately labeled and use a verified, consistent total-return series across all ETFs; do not mix it with price returns.

### Comparability and historical reconciliation

ETF returns include differences in holdings, sector weights, index construction, concentration, rebalancing and fund implementation. IWF and VUG, and SPLV and USMV, are alternative exposures, not interchangeable measurements. Price returns omit cash distributions and can change rankings relative to dividend-reinvested returns. Even ETF total returns are not pure-factor returns or evidence of isolated factor premia; IWM is a small-cap exposure proxy, not a size-factor long–short portfolio.

Documentation reconciliation dated October 12, 2026: the prior table listed VUG and USMV, while the [October 8](2026-10-08.md), [October 9](2026-10-09.md), [October 10](2026-10-10.md) and [October 11](2026-10-11.md) editions used IWF and SPLV. Their four-week endpoints were September 9–October 7, September 10–October 8, and September 11–October 9 (the latter for both weekend editions). October 11's reported IWF +4.61% and SPLV −2.24% are split-adjusted price returns excluding dividends. This update reconciles definitions; it does not independently verify endpoint prices or revise historical figures. Numerical corrections require independent verification and a dated correction record.

## Market microstructure

Execution notes distinguish between structural patterns and verified session data. Claims about current spread, queue depth, fill probability, option open interest, gamma exposure, dealer positioning, or dark-pool activity require a traceable current source. Without one, the issue supplies a conservative execution rule rather than a fabricated estimate.

## Research standards

- Use point-in-time universes and corporate-action-adjusted data.
- Purge and embargo overlapping labels during cross-validation.
- Include realistic spread, fee, impact, latency, and missed-fill assumptions.
- Report non-results and sensitivity to parameter choice.
- Separate research, paper-trading, and production results.
- Preserve source snapshots and correction history.
