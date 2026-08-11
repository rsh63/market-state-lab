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

Practical ETF proxies are used for interpretability:

| Factor | Proxy |
|---|---|
| Momentum | MTUM |
| Value | VLUE or VTV |
| Quality | QUAL |
| Size | IWM |
| Growth | VUG |
| Low volatility | USMV |

Short and medium horizons are reported only when data are comparably timestamped. Otherwise the panel is marked as an indicative, non-synchronous snapshot.

## Market microstructure

Execution notes distinguish between structural patterns and verified session data. Claims about current spread, queue depth, fill probability, option open interest, gamma exposure, dealer positioning, or dark-pool activity require a traceable current source. Without one, the issue supplies a conservative execution rule rather than a fabricated estimate.

## Research standards

- Use point-in-time universes and corporate-action-adjusted data.
- Purge and embargo overlapping labels during cross-validation.
- Include realistic spread, fee, impact, latency, and missed-fill assumptions.
- Report non-results and sensitivity to parameter choice.
- Separate research, paper-trading, and production results.
- Preserve source snapshots and correction history.
