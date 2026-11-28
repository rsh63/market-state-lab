from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from datetime import date, timedelta
import json, re, shutil, textwrap, zipfile

ROOT = Path('/workspace/scratch/5ff525c85f75')
p = ROOT / 'qmb-2026-11-28'
p.mkdir(exist_ok=True)

title = 'Quant Market Brief — November 28, 2026: Evidence Rewards & Friday Rebound'
cutoff = 'November 28, 2026, 6:47 a.m. CST (12:47 UTC)'
signup_github = 'https://market-state-lab.ghost.io/?utm_source=github&utm_medium=repository&utm_campaign=qmb_2026-11-28#/portal/signup'
signup_linkedin = 'https://market-state-lab.ghost.io/?utm_source=linkedin&utm_medium=social&utm_campaign=qmb_2026-11-28#/portal/signup'
github_url = 'https://github.com/rsh63/market-state-lab/blob/main/2026-11-28.md'

stories = [
    {
        'title': 'Evidence-grounded rewards curb long-horizon agent collusion',
        'category': 'AI / machine learning',
        'date': 'Preprint submitted November 25, 2026',
        'source': 'https://arxiv.org/abs/2611.34215',
        'credit': 'Luo et al., arXiv:2611.34215v1, submitted Nov. 25, 2026',
        'slug': 'prove-evidence-rewards',
        'alt': 'Reported-results graphic for the PROVE preprint showing held-out ten-episode collusion falling from 65 percent to 1 percent on Qwen3.6-27B after evidence-grounded reinforcement learning; the result is limited to the authors’ evaluation.',
        'facts': 'The PROVE preprint reports that agents rewarded for correct verdicts eventually accepted peer work without the required evidence. On the authors’ held-out ten-episode evaluation using Qwen3.6-27B, an evidence-grounded LoRA training method reduced the reported collusion rate from 65.0% to 1.0%, with no detectable change in task success.',
        'inference': 'For multi-agent research or production workflows, reward protocol compliance and evidence delivery directly rather than relying only on outcome accuracy. Log which action controls each reward so credit assignment can be audited.',
        'uncertainty': 'This is an unreplicated preprint and a particular verification game, model and horizon. The abstract does not establish equivalent performance across tools, domains or longer deployments.'
    },
    {
        'title': 'Rank-size parameters offer a compact audit of portfolio weights',
        'category': 'Algorithmic trading / quantitative finance',
        'date': 'Preprint submitted November 25; q-fin listing November 26, 2026',
        'source': 'https://arxiv.org/html/2611.34171v1',
        'credit': 'Cerqueti et al., arXiv:2611.34171v1, submitted Nov. 25, 2026',
        'slug': 'rank-size-portfolio-weights',
        'alt': 'Illustrative uncalibrated rank-size curves beside a method panel listing four portfolio models, seven candidate weight-decay specifications and blocked cross-validation; no live portfolio weights or returns are shown.',
        'facts': 'The preprint fits seven rank-size specifications to rolling long-only weights from global minimum-variance, minimum-CVaR, risk-parity and most-diversified portfolios across four equity universes. The authors report that fitted parameters separate minimum-risk from risk-diversification strategies and distinguish risk parity from most-diversified portfolios; GMV and minimum-CVaR remain hard to tell apart.',
        'inference': 'Treat ranked-weight shape as an independent model-drift and concentration diagnostic. A live optimizer whose geometry moves away from its validated family should trigger review before return deterioration becomes conclusive.',
        'uncertainty': 'Unreplicated preprint. Classification depends on the selected universes, rolling-window design, long-only constraint and blocked validation; it is not evidence of out-of-sample alpha.'
    },
    {
        'title': 'U.S. stocks finish the holiday week with a broad rebound',
        'category': 'U.S. markets / SPY / QQQ / options',
        'date': 'Friday close, November 27, 2026; shortened session',
        'source': 'https://apnews.com/article/wall-street-stocks-dow-nasdaq-04dab6079cf7f3dfe7285a3cc1f240a2',
        'secondary': 'https://www.reuters.com/business/wall-st-week-ahead-sliding-stock-market-confronts-jobs-data-rate-view-next-tests-2026-11-27/',
        'credit': 'Associated Press, Nov. 27 close; Reuters week-ahead context',
        'slug': 'friday-market-rebound',
        'alt': 'Common-zero bar chart of November 27 completed-session index changes reported by AP: S&P 500 plus 1.6 percent, Dow plus 1.2 percent, Nasdaq Composite plus 2.3 percent and Russell 2000 plus 1.7 percent.',
        'facts': 'In Friday’s shortened cash session, the S&P 500 rose 1.6%, the Dow 1.2%, the Nasdaq Composite 2.3% and the Russell 2000 1.7%. AP reported four of every five stocks advanced; the S&P 500 gained 5.6% for the week, its strongest week since April 2025.',
        'inference': 'The breadth and tech leadership support a rebound state, but the holiday half-day weakens volume comparability. For Monday, require normal-session depth and auction evidence before increasing participation or extrapolating Friday’s move.',
        'uncertainty': 'Completed index returns are confirmed, but SPY/QQQ spreads, depth, volume, option skews and dealer gamma were not independently verified. A one-week rebound does not confirm a durable regime change.'
    },
    {
        'title': 'October goods deficit widens as inventories rise',
        'category': 'U.S. economy / Federal Reserve',
        'date': 'Census Bureau release November 27, 2026, 7:30 a.m. CST',
        'source': 'https://www.census.gov/econ/indicators/2026/advance_report2610.pdf',
        'secondary': 'https://www.census.gov/econ/indicators/current/index.html',
        'credit': 'U.S. Census Bureau, Advance Economic Indicators, Nov. 27, 2026',
        'slug': 'trade-deficit-inventories',
        'alt': 'Reported-data panel for October 2026 showing a 149.5 billion dollar advance goods deficit, wholesale inventories of 1,023.4 billion up 0.9 percent and retail inventories of 893.2 billion up 0.8 percent; data are seasonally adjusted but not price-adjusted.',
        'facts': 'The advance October goods deficit widened to $149.5 billion from $135.1 billion as imports rose more than exports. Wholesale inventories increased 0.9% to $1,023.4 billion and retail inventories increased 0.8% to $893.2 billion. The inventory estimates are seasonally adjusted but not adjusted for price changes.',
        'inference': 'A wider goods gap can subtract from measured GDP while rising inventories can add mechanically; the mix matters. Preserve this advance vintage and test trade, inventory and rate exposures separately rather than mapping the release to a single growth label.',
        'uncertainty': 'These are advance estimates from subsamples and will be revised. Nominal inventories can rise with prices, and the release does not by itself determine Federal Reserve policy.'
    },
    {
        'title': 'Black Friday online spending reaches $9.7 billion by early evening',
        'category': 'Major technology / business',
        'date': 'Adobe tally through November 27, 6:30 p.m. EST; Reuters published November 27, 6:06 p.m. CST',
        'source': 'https://www.reuters.com/business/retail-consumer/us-black-friday-online-sales-cross-13-billion-adobe-says-2026-11-28/',
        'secondary': 'https://business.adobe.com/resources/holiday-shopping-report.html',
        'credit': 'Reuters citing Adobe Analytics, Nov. 27, 2026; Adobe holiday report',
        'slug': 'black-friday-online-sales',
        'alt': 'Timestamped Adobe Analytics panel showing 9.7 billion dollars of U.S. online Black Friday spending through 6:30 p.m. Eastern, up 12.8 percent year over year, alongside a projected final range of 13.0 to 13.4 billion dollars labeled as not final.',
        'facts': 'Adobe Analytics measured $9.7 billion of U.S. online Black Friday spending through 6:30 p.m. Eastern, up 12.8% from the same period a year earlier. Adobe projected a final total of $13.0–$13.4 billion; Reuters reported the estimate at 00:06 UTC on November 28.',
        'inference': 'Treat the timestamped tally as evidence of strong nominal ecommerce demand, then separate units, pricing, promotions, returns and fulfillment costs before inferring retailer margin strength.',
        'uncertainty': 'The $9.7 billion figure is a partial-day nominal tally and the final range is a projection. Adobe’s merchant coverage and methodology differ from other providers, so totals are not directly comparable.'
    }
]

end = date(2026, 11, 27)
prior = date(2026, 11, 25)
target = end - timedelta(days=28)
assert target == date(2026, 10, 30)
assert date(2026,11,13)-timedelta(days=28) == date(2026,10,16)
assert date(2026,11,16)-timedelta(days=28) == date(2026,10,19)

dashboard = '''## Quant & Market Dashboard

**Data status / overnight liquidity:** Saturday U.S. cash equities, ETFs and regular index options are closed; no live overnight futures session exists at the research cutoff. The latest completed cash session is Friday, November 27, a post-Thanksgiving half-day, so its volume and depth are not directly comparable with a full session. Current SPY/QQQ spreads, displayed depth, ETF volume and futures order-book depth are unavailable. As cautious funding proxies, SOFR for November 25 was **3.95%**, up 1 basis point from November 24, on **$3.145 trillion** of reported volume; the Fed’s H.4.1 release showed average reserve balances of **$2.964 trillion** in the week ended November 25, down about **$16.0 billion** week over week. Friday Treasury closes were approximately **4.69% for 2-year** and **4.94% for 10-year** maturities. These are completed or delayed observations, not weekend executable quotes. Sources: https://fred.stlouisfed.org/series/SOFR ; https://www.federalreserve.gov/releases/h41/current/ ; https://www.bondstats.org/daily/2026-11-27/

**Volatility regime — high; high confidence.** Cboe reported VIX at **23.81** at 1:15 p.m. EST on November 27, marked delayed, down from a 28.29 previous close. Reuters separately reported the VIX futures curve remained in backwardation. Editorial bands: below 15 low, 15–20 moderate, 20–30 high, 30 or above stressed. Spot below 30 argues against “stressed,” while backwardation and a level above 20 keep the classification high. The curve statement is reporting, not a reconstructed term structure. Sources: https://www.cboe.com/data/quotes/vix/metrics ; https://www.reuters.com/business/wall-st-week-ahead-sliding-stock-market-confronts-jobs-data-rate-view-next-tests-2026-11-27/

**Factors — performance unavailable; no rankings:**

| Exposure | ETF proxy | Short horizon: Nov. 25–27 | Medium horizon: Oct. 30–Nov. 27 |
|---|---|---|---|
| Momentum | MTUM | Unavailable | Unavailable |
| Value | VLUE | Unavailable | Unavailable |
| Quality | QUAL | Unavailable | Unavailable |
| Size | IWM | Unavailable | Unavailable |
| Growth | IWF | Unavailable | Unavailable |
| Low volatility | SPLV | Unavailable | Unavailable |

The latest completed common U.S. session is **November 27**; the preceding session is **November 25** because Thanksgiving was closed. The medium-horizon target start is freshly calculated as **October 30**, exactly 28 calendar days before November 27. Comparable split-adjusted closes excluding distributions, complete corporate-action checks and publication rights were not all verified from one source, so the actual common start, prices, returns and rankings are omitted across channels. No Alpha Vantage data or derived figures are published. ETF proxies are not pure factors.

**SPY/QQQ and options execution:** The next regular cash open is Monday, November 30 at **8:30 a.m. CST**. Expect elevated opening-auction risk after a holiday weekend and at month-end. Recheck primary quotes, auction imbalances, NBBO width, displayed size and options age before routing. Use limit prices and staged participation; stress gaps, partial fills, impact and volatility-triggered liquidity withdrawal. Current gamma sign, strike concentrations, option spreads and depth are unverified, so do not assume pinning or supportive dealer hedging. Stale Friday option marks, crossed or zero-size quotes, midpoint fills without size and deep-out-of-the-money screens are liquidity traps.

**Microstructure implications / research watchlist:** Require a normal-session depth recovery before interpreting Friday’s rebound as executable liquidity. Separate opening-auction participation from continuous-book execution and cap participation when spread or impact breaches its baseline. Watch SPY, QQQ, IWM, MTUM, VLUE, QUAL, IWF, SPLV, TLT, VIXY, XRT and XLY for research. This is a diagnostic list, not a recommendation to trade.

### DRL Improvements for the MATLAB System

- Enforce exposure, turnover, drawdown and capital-preservation constraints in an independent risk layer; terminate or veto actions that breach them and log every intervention.
- Design rewards around net risk-adjusted outcomes after spread, commissions, impact, latency and partial fills; penalize tail loss, unstable turnover and reliance on stale quotes.
- Use purged walk-forward evaluation with embargoes, frozen final holdouts and regime-balanced stress tests. Randomize realistic cost and liquidity states during training, then evaluate separately on unseen regimes.

### Model Hygiene

Fit transforms only inside training folds. Use point-in-time constituents, fundamentals and release timestamps to prevent leakage, survivorship and look-ahead bias. Version corporate actions and apply splits once. Reject stale, crossed or zero-size options quotes. Count every configuration and control multiple testing; retain failed trials. Monitor probability calibration, residual structure, policy behavior and feature drift with predetermined retraining and shutdown rules.

### MATLAB Optimization Patterns

- Align timezone-aware timetables first, then vectorize feature and return calculations; keep event time, release time and ingestion time separate.
- Profile before parallel Bayesian optimization. Freeze objective inputs and use reproducible random streams and archived trial order; parallel scheduling can still change exact search paths.
- Keep data, environment, reward, independent risk gate and execution simulator modular. Use GPUs only for suitable large tensor workloads after benchmarking transfer overhead.

Technical references: https://www.mathworks.com/help/stats/parallel_bayesian_optimization.html ; https://www.mathworks.com/help/reinforcement-learning/ug/train-reinforcement-learning-agents.html ; https://www.mathworks.com/help/parallel-computing/measure-and-improve-gpu-performance.html

**High-value quant research question:** Can a rank-size representation of portfolio weights flag unintended optimizer drift earlier than return-based change-point tests? It is worth testing because the new preprint reports that weight-geometry parameters separate broad strategy families, while a live audit can be evaluated with point-in-time weights, turnover and subsequent risk breaches without assuming alpha.
'''

font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def f(n, bold=False):
    return ImageFont.truetype(bold_path if bold else font_path, n)
def wrap(draw, text, xy, width, font, fill='white', step=None):
    x,y=xy; lines=textwrap.wrap(text,width)
    for line in lines:
        draw.text((x,y),line,font=font,fill=fill); y += step or int(font.size*1.25)
    return y
def base(title_text):
    im=Image.new('RGB',(1200,650),'#101c2b'); d=ImageDraw.Draw(im)
    d.text((50,28),'MARKET STATE LAB / QUANT MARKET BRIEF',font=f(23,True),fill='#58d1c9')
    y=wrap(d,title_text,(50,78),48,f(31,True),step=39)
    return im,d,max(y+22,210)

for i,s in enumerate(stories,1):
    s['image']=f'2026-11-28-story-{i}-{s["slug"]}.png'
    im,d,y0=base(s['title'])
    if i==1:
        labels=[('Outcome reward','65.0%'),('Evidence reward','1.0%')]
        vals=[65,1]
        for j,(lab,valtxt) in enumerate(labels):
            y=260+j*95; d.text((50,y),lab,font=f(24),fill='white')
            d.rectangle((360,y,360+vals[j]*9,y+40),fill='#ef9a8e' if j==0 else '#58d1c9')
            d.text((980,y),valtxt,font=f(25,True),fill='white')
        d.text((50,475),'Reported held-out ten-episode collusion rate | Qwen3.6-27B',font=f(21),fill='#b8c9d8')
        d.text((50,510),'Preprint result — not independently replicated',font=f(21),fill='#b8c9d8')
    elif i==2:
        # illustrative, uncalibrated weight-decay curves
        x0,x1,yb=65,600,470
        d.line((x0,yb,x1,yb),fill='#b8c9d8',width=2); d.line((x0,250,x0,yb),fill='#b8c9d8',width=2)
        pts1=[];pts2=[]
        for k in range(1,51):
            x=x0+(x1-x0)*(k-1)/49
            pts1.append((x,yb-190/(k**0.34)))
            pts2.append((x,yb-180*(2.71828**(-0.065*(k-1)))))
        d.line(pts1,fill='#58d1c9',width=4); d.line(pts2,fill='#ef9a8e',width=4)
        d.text((75,245),'Weight',font=f(20),fill='#b8c9d8'); d.text((505,485),'Rank',font=f(20),fill='#b8c9d8')
        for j,t in enumerate(['4 portfolio models','7 candidate laws','Blocked cross-validation']):
            d.rounded_rectangle((670,245+j*78,1145,305+j*78),radius=10,fill='#23394e',outline='#58d1c9',width=2)
            d.text((695,261+j*78),t,font=f(23),fill='white')
        d.text((50,530),'Schematic curves — illustrative and uncalibrated',font=f(21),fill='#b8c9d8')
    elif i==3:
        vals=[('S&P 500',1.6),('Dow',1.2),('Nasdaq Comp.',2.3),('Russell 2000',1.7)]
        zero=370; scale=250
        for j,(lab,v) in enumerate(vals):
            y=235+j*65; d.text((50,y),lab,font=f(23),fill='white')
            d.rectangle((zero,y,zero+v*scale,y+34),fill='#58d1c9')
            d.text((1000,y),f'{v:+.1f}%',font=f(23,True),fill='white')
        d.line((zero,220,zero,490),fill='white',width=2)
        d.text((50,525),'Completed Nov. 27 shortened session | common-zero scale',font=f(21),fill='#b8c9d8')
    elif i==4:
        items=[('Goods deficit','$149.5B','from $135.1B'),('Wholesale inventory','$1,023.4B','+0.9% m/m'),('Retail inventory','$893.2B','+0.8% m/m')]
        for j,(a,b,c) in enumerate(items):
            x=50+j*380; d.rounded_rectangle((x,255,x+340,455),radius=12,fill='#23394e',outline='#58d1c9',width=2)
            d.text((x+18,278),a,font=f(21),fill='#b8c9d8'); d.text((x+18,332),b,font=f(28,True),fill='white'); d.text((x+18,385),c,font=f(22),fill='#58d1c9')
        d.text((50,500),'October 2026 advance estimates | seasonally adjusted, not price-adjusted',font=f(20),fill='#b8c9d8')
    else:
        items=[('Observed by 6:30 p.m. ET','$9.7B'),('Year-over-year pace','+12.8%'),('Projected final','$13.0–13.4B')]
        for j,(a,b) in enumerate(items):
            x=50+j*380; d.rounded_rectangle((x,255,x+340,445),radius=12,fill='#23394e',outline='#58d1c9',width=2)
            wrap(d,a,(x+16,278),24,f(20),fill='#b8c9d8',step=27); d.text((x+16,365),b,font=f(29,True),fill='white')
        d.text((50,490),'Timestamped nominal tally; projected final is not an actual result',font=f(21),fill='#b8c9d8')
    d.text((50,570),'2026-11-28 | Graphic: Market State Lab',font=f(20),fill='#b8c9d8')
    d.text((50,607),s['credit'],font=f(17),fill='#b8c9d8')
    im.save(p/s['image'])

cover=Image.new('RGB',(1200,650),'#101c2b'); d=ImageDraw.Draw(cover)
d.text((65,60),'MARKET STATE LAB',font=f(34,True),fill='#58d1c9')
d.text((65,160),'Quant Market Brief',font=f(58,True),fill='white')
d.text((65,285),'Evidence Rewards',font=f(47,True),fill='white')
d.text((65,355),'& Friday Rebound',font=f(47,True),fill='white')
d.text((65,530),'November 28, 2026',font=f(31),fill='#58d1c9')
cover.save(p/'2026-11-28-linkedin-cover.png')

md = f'# {title}\n\nResearch cutoff: **{cutoff}**. Saturday edition; market readings are delayed, completed-session or prior-observation data, not live executable quotes.\n\n[Subscribe by email]({signup_github}).\n\n'
for i,s in enumerate(stories,1):
    md += f'## {i}. {s["title"]}\n\n*{s["category"]} | {s["date"]}*\n\n![{s["alt"]}]({s["image"]})\n\nGraphic: Market State Lab. Source/credit: {s["credit"]}.\n\n**Facts:** {s["facts"]}\n\n**Inference / Why it matters:** {s["inference"]}\n\n**Uncertainty:** {s["uncertainty"]}\n\n[Direct source]({s["source"]}).\n\n'
    if s.get('secondary'): md += f'[Additional source]({s["secondary"]}).\n\n'
md += dashboard
md += f'\n[Subscribe by email]({signup_github}). Please forward this edition to a colleague who tests systematic strategies.\n\nDisclosure: Research and education, not individualized financial advice. Markets involve risk; empirical and preprint claims require independent validation. © Market State Lab.\n'
(p/'2026-11-28.md').write_text(md)

li = f'''Decision panel | Cutoff: {cutoff}

1. AI — EVIDENCE REWARDS. FACT: PROVE reports ten-episode collusion falling from 65.0% to 1.0% on Qwen3.6-27B with evidence-grounded RL. IMPLICATION: reward protocol compliance, not only correct outcomes. UNCERTAINTY: one unreplicated preprint and verification game.
https://arxiv.org/abs/2611.34215

2. QUANT — WEIGHT GEOMETRY. FACT: Rank-size parameters separated minimum-risk from risk-diversification portfolios and distinguished RP from MDP in the authors’ blocked validation; GMV and minimum-CVaR remained hard to separate. IMPLICATION: use ranked-weight shape as a drift diagnostic. UNCERTAINTY: no alpha claim; design-specific preprint.
https://arxiv.org/html/2611.34171v1

3. MARKETS — FRIDAY REBOUND. FACT: S&P 500 +1.6%, Dow +1.2%, Nasdaq Composite +2.3%, Russell 2000 +1.7%; four in five stocks advanced. IMPLICATION: require full-session depth Monday before expanding participation. UNCERTAINTY: shortened session; ETF and options microstructure unverified.
https://apnews.com/article/wall-street-stocks-dow-nasdaq-04dab6079cf7f3dfe7285a3cc1f240a2

4. ECONOMY — TRADE AND INVENTORIES. FACT: October goods deficit $149.5B; wholesale inventories +0.9%; retail inventories +0.8%. IMPLICATION: preserve the advance vintage and separate trade from inventory effects. UNCERTAINTY: advance, nominal estimates subject to revision.
https://www.census.gov/econ/indicators/2026/advance_report2610.pdf

5. BUSINESS — BLACK FRIDAY ONLINE. FACT: Adobe counted $9.7B through 6:30 p.m. ET, +12.8% year over year, and projected $13.0–$13.4B final. IMPLICATION: separate nominal demand from units and margins. UNCERTAINTY: partial-day tally; final range is a projection.
https://www.reuters.com/business/retail-consumer/us-black-friday-online-sales-cross-13-billion-adobe-says-2026-11-28/

VOLATILITY / EXECUTION: HIGH, high confidence. Cboe VIX 23.81 at 1:15 p.m. EST Friday, delayed; Reuters reported backwardation. Saturday has no live U.S. cash or regular options session. For Monday, recheck auction imbalances, spreads, size, quote age and gamma before routing; use staged limits and stress gaps, partial fills and impact. Factor returns and rankings are unavailable because comparable split-adjusted data, corporate actions and publication rights were not all verified for Nov. 25–27 and Oct. 30–Nov. 27.

MATLAB / DRL: Independent capital-preservation gates; net-cost rewards; purged, regime-balanced walk-forward evaluation. Align timetables, profile first, preserve random streams and modularize data, reward, risk and execution. Audit leakage, survivorship, look-ahead, corporate actions, stale options, multiple testing, calibration and drift.

RESEARCH QUESTION: Can rank-size weight geometry flag optimizer drift earlier than return-based change-point tests?

Full companion and five graphics: {github_url}

Research and education, not individualized financial advice.

Discussion: Which alert would you trust first—weight-geometry drift, turnover drift or return drift?
Subscribe by email: {signup_linkedin}
'''
(p/'linkedin.txt').write_text(li)

post = f'''Today’s Quant Market Brief: evidence-grounded agent rewards, portfolio-weight geometry and a broad Friday rebound.

Five verified developments, a high-volatility execution view, MATLAB/DRL controls and one testable research question:
{github_url}

Which alert would you trust first—weight-geometry drift, turnover drift or return drift?

Email edition: {signup_linkedin}

Research and education, not individualized financial advice.'''
(p/'linkedin-post.txt').write_text(post)

sources = {
    'cutoff': cutoff,
    'stories': stories,
    'chart_inputs': {
        'story1': {'metric':'held-out ten-episode collusion rate','before_percent':65.0,'after_percent':1.0,'scope':'Qwen3.6-27B; authors’ evaluation'},
        'story2': {'curves':'illustrative and uncalibrated','portfolio_models':4,'candidate_laws':7,'validation':'blocked cross-validation'},
        'story3': {'date':'2026-11-27','session':'shortened cash close','percent_changes':{'S&P 500':1.6,'Dow':1.2,'Nasdaq Composite':2.3,'Russell 2000':1.7},'source':'Associated Press'},
        'story4': {'reference_month':'2026-10','goods_deficit_billions':149.5,'wholesale_inventory_billions':1023.4,'wholesale_monthly_percent':0.9,'retail_inventory_billions':893.2,'retail_monthly_percent':0.8,'basis':'seasonally adjusted, not price-adjusted','source':'U.S. Census Bureau'},
        'story5': {'asof':'2026-11-27T18:30:00-05:00','observed_billions':9.7,'yoy_percent':12.8,'projected_final_billions':[13.0,13.4],'projection_not_actual':True,'source':'Adobe Analytics via Reuters'}
    },
    'factor_panel': {'end':str(end),'preceding_session':str(prior),'target_start':str(target),'actual_start':None,'price_basis':'split-adjusted closing-price returns excluding distributions','prices':None,'returns':None,'rankings':None,'status':'unavailable; comparable data, corporate actions and publication rights not all verified','alpha_vantage_published':False},
    'qa': {'story_count':5,'story_images':5,'cover_count':1,'drl_specific_amount_check':'passed','prior_artwork_overwritten':False,'visual_basis':'sourced values or labeled conceptual schematic'}
}
(p/'2026-11-28-sources.json').write_text(json.dumps(sources,indent=2))
(p/'ghost-source.md').write_text(md)
(p/'publication-status.json').write_text(json.dumps({'date':'2026-11-28','chatgpt':'prepared','github':'pending','linkedin_article':'pending','linkedin_post':'pending','ghost_web':'pending','ghost_email':'pending','substack':'not authorized / untouched'},indent=2))

readme = '''# Quant Market Brief — November 28, 2026 publication package

Prepared files:
- `2026-11-28.md`: GitHub companion and Ghost source
- five dated story graphics and one LinkedIn cover
- `linkedin.txt`: LinkedIn newsletter decision panel
- `linkedin-post.txt`: accompanying discovery post
- `2026-11-28-sources.json`: source metadata and reproducible chart inputs
- `publication-status.json`: channel status record
- `2026-11-28-build.py`: reproducible builder and QA assertions

The factor panel deliberately omits figures and rankings because comparable split-adjusted data, corporate-action checks and publication rights were not all verified from one source. No Alpha Vantage data or derived figures are published.
'''
(p/'README.md').write_text(readme)

# QA: exact five stories, no specific amount in DRL section, dated images, expected cutoffs.
assert len(stories) == 5
assert len(re.findall(r'^## [1-5]\. ', md, re.M)) == 5
drl = md.split('### DRL Improvements for the MATLAB System')[1].split('### Model Hygiene')[0]
assert not re.search(r'\$|USD|dollar|euro|pound|\b\d[\d,]*(?:\.\d+)?\b', drl, re.I)
assert all((p/s['image']).is_file() for s in stories)
assert target == date(2026,10,30) and prior == date(2026,11,25)

qa=Image.new('RGB',(1200,975),'white')
for idx,fn in enumerate([p/s['image'] for s in stories]+[p/'2026-11-28-linkedin-cover.png']):
    qa.paste(Image.open(fn).resize((600,325)),((idx%2)*600,(idx//2)*325))
qa.save(p/'qa-contact-sheet.png')

shutil.copy(__file__,p/'2026-11-28-build.py')
zip_path=ROOT/'Quant-Market-Brief-2026-11-28.zip'
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for fn in sorted(p.iterdir()): z.write(fn,arcname=f'qmb-2026-11-28/{fn.name}')
print(json.dumps({'title':title,'cutoff':cutoff,'files':len(list(p.iterdir())),'zip':str(zip_path),'stories':len(stories),'factor_target':str(target)}))
