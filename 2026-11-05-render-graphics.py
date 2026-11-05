from pathlib import Path
import json,re,html,textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image,ImageOps,ImageDraw
P=Path(__file__).parent; D='2026-11-05'; cutoff='November 5, 2026, 6:32 a.m. CST (12:32 UTC)'
title='Quant Market Brief — November 5, 2026: Wallet Signals & Nasdaq Divergence'
S=[dict(cat='AI / machine learning',slug='validated-ai-security',head='AI security research scales; validation remains the gate',date='November 4, 2026',url='https://openai.com/index/a-thousand-fewer-paths-to-root/',fact='OpenAI reports a Linux research pipeline progressing from 2,308 candidate findings to 1,724 reproduced vulnerabilities and 948 privilege-escalation exploits, with candidate patches for review.',why='Use staged evidence gates and human review in automated technical workflows.',unc='Vendor-reported controlled research; generated patches are not all deployed fixes.',labels=['2,308 candidate findings','1,724 reproduced vulnerabilities','948 exploit validations','Candidate patches → maintainer review'],credit='OpenAI, November 4, 2026',alt='Four evidence stages distinguish candidate Linux findings, reproduced vulnerabilities, exploit validation and maintainer patch review.'),dict(cat='Quantitative finance',slug='wallet-signal-validation',head='Wallet histories add predictive information in a new microstructure study',date='Preprint submitted November 3, 2026',url='https://arxiv.org/abs/2611.05218',fact='Ding and Zhai report that wallet-attributed features improve short-horizon Hyperliquid forecasts beyond an anonymous benchmark. Their chronological evaluation uses earlier wallet scores.',why='Test feature availability, delayed inputs and matched placebos before trusting predictive gains.',unc='Retrospectively selected specifications, consensus timestamps and data gaps limit deployment claims; executable profit is not demonstrated.',labels=['July 1–10: score wallets','July 11–20: fit models','July 21–27: evaluate','Retrospective choices remain a caveat'],credit='Ding & Zhai, arXiv:2611.05218v1, November 3, 2026',alt='A chronological study timeline separates wallet scoring, model fitting and evaluation, with a retrospective-selection caveat.'),dict(cat='U.S. markets',slug='nasdaq-futures-divergence',head='Nasdaq futures lag while broader contracts hold steadier',date='November 5, 2026; 4:04 a.m. CST snapshot',url='https://ca.finance.yahoo.com/news/p-500-futures-steady-midterm-105838388.html',fact='Reuters reports Dow futures +0.48%, S&P 500 futures +0.01% and Nasdaq-100 futures −0.63% at 5:04 a.m. EST, following Wednesday’s broad rally.',why='Reassess SPY–QQQ relative risk and refresh executable quotes before placing orders.',unc='Earlier press snapshot, not live prices, spreads or depth; no directional trade is implied.',labels=[],credit='Reuters via Yahoo Finance, November 5; 5:04 a.m. EST',alt='Zero-centered bars show Dow futures +0.48%, S&P 500 futures +0.01% and Nasdaq-100 futures −0.63% at 4:04 a.m. CST November 5.'),dict(cat='U.S. economy / Fed',slug='claims-productivity-calendar',head='Claims and productivity share today’s premarket release window',date='November 5, 2026 scheduled events',url='https://www.newyorkfed.org/research/calendars/i-nov26.html',fact='The New York Fed calendar lists initial claims and preliminary productivity/costs for 8:30 a.m. EST today, and the Employment Situation at that time tomorrow.',why='Treat today’s labor/cost releases and Friday’s jobs report as separate information events.',unc='Schedules are tentative; release values and surprises are unknown at cutoff.',labels=['Today 07:30 CST / 13:30 UTC','Initial claims + productivity/costs','Tomorrow 07:30 CST / 13:30 UTC','Employment Situation'],credit='New York Fed November calendar, checked November 5, 2026',alt='Two dated calendar panels show November 5 claims and productivity at 7:30 a.m. CST and November 6 Employment Situation at 7:30 a.m. CST.'),dict(cat='Major technology / business',slug='qualcomm-earnings-quality',head='Qualcomm’s annual earnings rise includes a large tax benefit',date='Results released November 4, 2026',url='https://www.sec.gov/Archives/edgar/data/804328/000080432826000127/qcom092726erex991.htm',fact='Qualcomm reports fiscal-2026 GAAP revenue of $43.120 billion, down 3%, and GAAP EPS of $12.70. Annual GAAP results include a $5.7 billion tax benefit; non-GAAP EPS was $10.54, down 12%.',why='Separate operating results, accounting effects and forecasts when comparing earnings quality.',unc='Non-GAAP measures require reconciliation; management’s diversification targets remain forward-looking.',labels=['FY2026 revenue: $43.120bn (−3%)','GAAP EPS: $12.70','Tax benefit: $5.7bn in annual results','Non-GAAP EPS: $10.54 (−12%)'],credit='Qualcomm earnings exhibit, SEC, November 4, 2026',alt='Four financial labels separate Qualcomm annual revenue, GAAP EPS, the tax benefit and non-GAAP EPS; no additive EPS bridge is implied.')]
F=[('Momentum','MTUM',68.22,69.58,80.61),('Value','VLUE',193.02,192.67,201.10),('Quality','QUAL',56.76,55.48,56.48),('Size','IWM',284.02,279.79,277.70),('Growth','IWF',117.90,117.44,128.76),('Low volatility','SPLV',78.51,76.88,71.22)]
rows=''; inputs=[]
for fac,sym,c,p,b in F:
 day=100*(c/p-1);med=100*(c/b-1)
 rows+=f'| {fac} | [{sym}](https://stockanalysis.com/etf/{sym.lower()}/history/) | {day:+.2f}% | {med:+.2f}% |\n'
 inputs.append(dict(factor=fac,symbol=sym,closeNov4=c,closeNov3=p,closeOct7=b,daily=day,fourWeek=med,source=f'https://stockanalysis.com/etf/{sym.lower()}/history/'))
dash='''## Quant & Market Dashboard

### Liquidity and volatility

- **Overnight:** ES/NQ and ETF spreads, depth and overnight volume are unverified. Futures divergence is a direction proxy, not evidence of executable liquidity. Current Treasury depth and options positioning are unavailable.
- **Prior-close activity, November 4:** SPY completed daily row 766.81, volume 62.13m; QQQ 691.95, volume 62.37m. Provider quote banners differ slightly from daily rows; use completed rows consistently. Volume is an activity proxy, not fill quality. [SPY](https://chartexchange.com/symbol/nyse-spy/historical/) · [QQQ](https://chartexchange.com/symbol/nasdaq-qqq/historical/).
- **Funding:** November 3 SOFR 3.97% versus EFFR 3.88%, a nine-basis-point gap; SOFR is two basis points above November 2. FRED updated these on November 4 at 7:02 and 8:02 a.m. CST. Lagged aggregate context does not establish present funding stress. [SOFR](https://fred.stlouisfed.org/series/SOFR) · [EFFR](https://fred.stlouisfed.org/series/EFFR).
- **Regime: Moderate, easing; medium confidence.** Delayed VIX 16.76 at November 5 5:54 a.m. CST, versus November 4 close 16.61 and November 3 close 20.83. House rule: 15–25 moderate; below 15 low; 25–35 high; above 35 stressed. Cross-asset dispersion and macro windows can still elevate execution risk. Term structure and skew unverified. [VIX](https://chartexchange.com/symbol/index-vix/historical/).

### Factor proxies

| Factor | ETF | Nov 3→4 | Oct 7→Nov 4 (4 weeks) |
|---|---|---:|---:|
'''+rows+'''
Calculated from source-linked Close columns, not adjusted total returns. These are indicative ETF price-return proxies, not isolated factor premia; distributions are excluded. Both endpoints use the same provider scale; corporate-action histories were not independently refreshed. Do not splice these levels into a differently adjusted series. Quality and low volatility led momentum on the day; momentum and growth remained negative over four weeks.

### Execution and microstructure

- Initial claims and productivity/costs: **7:30 a.m. CST / 13:30 UTC**. Cash opening auction: **8:30 a.m. CST / 14:30 UTC**. Recheck quotes after each event and before Friday’s jobs release.
- For SPY/QQQ, inspect NBBO age, spread, depth, auction imbalances and ES/NQ basis. Use bounded limits, participation caps and explicit slippage budgets. Displayed size and high prior volume can hide liquidity traps.
- For options, verify expiry, deliverables, settlement, quote synchronization and package costs. Reject stale, crossed or one-sided markets. Short-dated gamma can magnify moves; dealer gamma sign, pinning and expiry-flow magnitude are unknown.
- Keep venue-specific identity signals separate from anonymous U.S. equity feeds. Test anonymous adverse-selection proxies rather than assuming wallet features transfer.

**Research watchlist:** SPY, QQQ, IWM, RSP, TLT; ES, NQ, ZN, VX; MTUM, VLUE, QUAL, IWF, SPLV; QCOM, SOXX.

### DRL Improvements for the MATLAB System

1. Enforce drawdown, exposure, participation and stale-data constraints outside the policy, with a safe fallback.
2. Penalize spread, market impact, latency, turnover and missed fills; report tail loss and constraint breaches separately from reward.
3. Run purged, embargoed walk-forward tests with matched seeds, locked feature selection and unseen market regimes; stress execution costs and delayed inputs.
4. Add abstention under poor calibration or drift; compare richer state features with a simple volatility/volume baseline.

### Model hygiene

Check leakage, survivorship and look-ahead bias, corporate actions, stale options quotes, multiple testing, calibration and drift. Preserve point-in-time universes, release vintages and availability timestamps. Fit scalers only on training folds. Retrospective feature selection requires a new untouched test.

### MATLAB optimization patterns

- Use named-zone timetables and causal synchronize/retime alignment; never backfill an unreleased observation.
- Vectorize rolling features, preallocate replay logs and profile before optimizing.
- Parallelize independent folds or Bayesian trials with reproducible random streams.
- Use GPUs only for suitable batch workloads; keep data, policy, risk and execution modules separate.

### High-value quant research question

**Do delayed, anonymous adverse-selection proxies improve one-step risk forecasts beyond volatility and volume after realistic costs?**

This tests the transferable mechanism in the wallet study without assuming U.S. equity feeds expose trader identities. Lock features prospectively, compare delayed inputs and assess risk improvement as well as net returns.
'''
(P/'dashboard.md').write_text(dash)
intro=f'Research cutoff: **{cutoff}**. Futures are an earlier reported snapshot; ETF factors are November 4 prior-close, VIX delayed and funding lagged. No live execution feed verified.'
disclosure='Research and education only—not individualized financial advice. No trading performance is promised.'
cta=lambda c,m:f'https://market-state-lab.ghost.io/?utm_source={c}&utm_medium={m}&utm_campaign=qmb_{D}#/portal/signup'
gh=f'https://github.com/rsh63/market-state-lab/blob/main/{D}.md'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16})
for i,s in enumerate(S,1):
 s['image']=f'{D}-story-{i}-{s["slug"]}.png';fig=plt.figure(figsize=(12,6.75),dpi=100,facecolor='#f4f7fa')
 fig.text(.045,.94,'MARKET STATE LAB / QUANT MARKET BRIEF',size=16,color='#0d3543',weight='bold');fig.text(.82,.94,'05 NOV 2026',size=13,color='#0d3543')
 fig.text(.045,.83,'\n'.join(textwrap.wrap(s['head'],55)),size=22,weight='bold',color='#132c3b',va='top')
 if i==3:
  ax=fig.add_axes([.23,.25,.68,.38]);v=[.48,.01,-.63];ax.barh(['Dow','S&P 500','Nasdaq-100'],v,color=['#168275','#168275','#b54d55']);ax.axvline(0,color='#123341');ax.set_xlim(-.8,.8);ax.set_xlabel('Futures change (%) • reported snapshot');ax.invert_yaxis()
  for j,x in enumerate(v):ax.text(x+(.025 if x>=0 else -.025),j,f'{x:+.2f}%',ha='left' if x>=0 else 'right',va='center',size=14)
 else:
  for j,l in enumerate(s['labels']):fig.text(.065,.61-j*.115,l,size=21 if len(l)<44 else 18,color='#0e615f',bbox=dict(facecolor='white',edgecolor='#d4dce0',pad=10))
 fig.text(.045,.085,'\n'.join(textwrap.wrap('Source: '+s['credit'],105)),size=11,color='#41586a')
 fig.text(.045,.035,'Reported data' if i in [1,3,5] else 'Conceptual study/calendar diagram • no calibrated curve',size=10,color='#41586a')
 fig.savefig(P/s['image']);fig.savefig(P/s['image'].replace('.png','.svg'));plt.close(fig)
fig=plt.figure(figsize=(12,6.75),dpi=100,facecolor='#102c3b');fig.text(.07,.84,'MARKET STATE LAB',color='#93bfc6',size=18);fig.text(.07,.69,'Quant Market Brief',color='white',size=33,weight='bold');fig.text(.07,.59,'NOVEMBER 5, 2026',color='#a9c5d1',size=18);fig.text(.07,.35,'Wallet signals\n& Nasdaq divergence',color='white',size=34,weight='bold');fig.text(.07,.12,'Validation gates • Execution risk • Earnings quality',color='#a9c5d1',size=18);fig.savefig(P/f'{D}-linkedin-cover.png');fig.savefig(P/f'{D}-linkedin-cover.svg');plt.close(fig)
body=''
for i,s in enumerate(S,1):body+=f'## {i}. {s["head"]}\n\n![{s["alt"]}]({s["image"]})\n\n*Graphic: Market State Lab; {s["credit"]}.*\n\n**Fact — {s["date"]}:** {s["fact"]} [Direct source]({s["url"]})\n\n**Inference / Why it matters:** {s["why"]}\n\n**Uncertainty:** {s["unc"]}\n\n'
md=f'# {title}\n\n{intro}\n\n[Subscribe by email]({cta("github","technical_archive")}).\n\n'+body+dash+f'\n[Subscribe by email]({cta("github","technical_archive")}).\n\n*{disclosure}*\n'
(P/f'{D}.md').write_text(md)
(P/f'ghost-{D}.md').write_text(f'# {title}\n\n{intro}\n\n'+body+dash+f'\n[Technical companion — pending publication]({gh}).\n\nPlease forward this edition to one colleague who would find it useful.\n\n*{disclosure}*\n')
li=f'# {title}\n\n{intro}\n\n**Decision panel:** Validate richer signals; do not mistake a broad rally for uniform tech strength.\n\n'
for i,s in enumerate(S,1):li+=f'**{i} · {s["cat"]}:** {s["fact"]} **Implication:** {s["why"]} **Caveat:** {s["unc"]} [Source]({s["url"]})\n\n'
li+=f'**Volatility/execution:** Moderate, easing; medium confidence. Delayed VIX 16.76 at 5:54 a.m. CST. Claims/productivity 7:30; cash open 8:30 a.m. CST. Refresh quotes/depth; do not extrapolate yesterday’s fills.\n\n**MATLAB/DRL:** External risk limits, cost-aware rewards, delayed-input tests and purged walk-forward evaluation. Profile and use causal timetables.\n\n[GitHub companion — pending publication]({gh}).\n\n*{disclosure}*\n\n**Discussion:** Do delayed anonymous adverse-selection proxies improve risk forecasts beyond volatility and volume after costs?\n\n[Subscribe by email]({cta("linkedin","newsletter")}).\n'
(P/f'linkedin-{D}.md').write_text(li);(P/'title.txt').write_text(title)
(P/f'linkedin-post-{D}.txt').write_text(title+'\n\nDo delayed adverse-selection proxies add risk information after costs? Five stories, execution view and MATLAB research panel.\n\nTechnical companion (pending): '+gh+'\nEmail: '+cta('linkedin','social')+'\n\n'+disclosure)
(P/f'{D}-sources.json').write_text(json.dumps(dict(cutoff=cutoff,stories=S),indent=2));(P/f'{D}-market-inputs.json').write_text(json.dumps(dict(factors=inputs,VIX=dict(value=16.76,timestamp='2026-11-05T05:54:00-06:00',basis='delayed'),funding=dict(date='2026-11-03',SOFR=3.97,EFFR=3.88)),indent=2))
drl=md.split('### DRL Improvements for the MATLAB System')[1].split('### Model hygiene')[0];assert not re.search(r'[$€£]|\b(?:USD|dollars|million|billion)\b',drl,re.I);assert len(re.findall(r'^## [1-5]\. ',md,re.M))==5;assert md.count('\n![')==5
imgs=[Image.open(P/s['image']).resize((600,338)) for s in S]+[Image.open(P/f'{D}-linkedin-cover.png').resize((600,338))];mont=Image.new('RGB',(1200,1014),'white')
for i,im in enumerate(imgs):mont.paste(im,(i%2*600,i//2*338))
mont.save(P/'image-qa.png')
print(rows)
