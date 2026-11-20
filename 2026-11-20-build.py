from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from datetime import date,timedelta
import json,textwrap,re,shutil
p=Path('qmb-2026-11-20');p.mkdir(exist_ok=True)
title='Quant Market Brief — November 20, 2026: Rough Volatility & Expiry Risk'
cutoff='November 20, 2026, 6:34 a.m. CST (12:34 UTC)'
stories=[
dict(title='MIT-led AI audit finds that public code is not necessarily reusable code',category='AI / machine learning',date='MIT report published November 19, 2026',source='https://news.mit.edu/2026/ai-helps-researchers-investigate-how-medical-studies-share-code-1119',credit='MIT News, November 19, 2026',slug='ai-code-reuse-audit',alt='Conceptual audit panel showing LLM screening of nearly 4,000 studies, following repository links, and checking documentation and reuse terms; public code alone does not establish reproducibility.',nodes=['Nearly 4,000 studies\nLLM-assisted screening','Linked repositories\nFollow the evidence','Reuse readiness\nDocs / dependencies'],facts='An MIT and Dana-Farber-led team used LLMs to examine nearly 4,000 clinical prediction studies and assess linked code repositories. Its review found that code sharing was uncommon and public repositories often lacked information needed for scrutiny and reuse.',inference='Require an executable environment, dependency versions, data lineage and test instructions before admitting a shared model into a MATLAB research pipeline.',uncertainty='This is evidence from clinical prediction research, not a measured failure rate for trading repositories. LLM-assisted audits still require validation.'),
dict(title='New preprint links algorithmic market making to rough volatility',category='Algorithmic trading / quantitative finance',date='Submitted November 18; q-fin listing November 19, 2026',source='https://arxiv.org/abs/2611.24028',credit='Ramachandran, arXiv:2611.24028v1',slug='market-making-rough-volatility',alt='Conceptual hypothesis panel linking asynchronous market-maker updates and different lookback horizons to persistent order flow and rough volatility; the mechanism is a research model, not proven for U.S. ETFs.',nodes=['Asynchronous desks\nDifferent lookbacks','Order-book changes\nPersistent order flow','Rough volatility\nModel mechanism'],facts='Sai Niranjan Ramachandran proposes a mechanism in which market makers with different information horizons generate persistent order flow and rough volatility. The author tests model predictions with simulated agents and six months of Binance data containing about 790 million orders.',inference='Test whether volatility persistence and order-flow memory improve execution-cost forecasts before embedding such states in a trading agent.',uncertainty='A new preprint, not established causality or a profitable strategy. Binance perpetual-futures evidence does not establish transfer to SPY/QQQ or U.S. options.'),
dict(title='Nasdaq futures lead early declines after Thursday’s AI selloff',category='U.S. markets / SPY / QQQ',date='November 20, 2026; 4:57 a.m. EST reported snapshot',source='https://www.reuters.com/legal/transactional/wall-st-futures-slip-anthropic-debut-fails-reassure-ai-investors-2026-11-20/',credit='Reuters, November 20, 2026, 4:57 a.m. EST',slug='nasdaq-futures-expiry-risk',alt='Zero-based horizontal bar chart of reported futures changes at 4:57 a.m. EST on November 20: Dow minus 0.20%, S&P 500 minus 0.76%, Nasdaq 100 minus 1.63%.',nodes=[],facts='Reuters reported Dow E-minis down 0.20%, S&P 500 E-minis down 0.76% and Nasdaq 100 E-minis down 1.63% at 4:57 a.m. EST (3:57 a.m. CST), following Thursday’s selloff.',inference='Recheck QQQ concentration and opening capacity; a futures move supplies direction, not evidence of executable ETF liquidity.',uncertainty='An early reported snapshot, not live quotes or a prediction of the cash open. Depth, spreads and current positioning were not verified.'),
dict(title='Paulson favors further tightening while emphasizing the Fed’s reaction function',category='U.S. economy / Federal Reserve',date='Speech and subsequent remarks November 19, 2026',source='https://www.philadelphiafed.org/the-economy/monetary-policy/261119-money-marketeers-speech',credit='Philadelphia Fed / Reuters, November 19, 2026',slug='paulson-policy-reaction-function',alt='Conceptual policy panel showing incoming economic data, the Fed reaction function and policy expectations; Paulson’s views are individual remarks, not a committee rate decision.',nodes=['Incoming data\nInflation / activity','Reaction function\nConditional response','Policy expectations\nUpdate scenarios'],facts='In her November 19 speech, Philadelphia Fed President Anna Paulson emphasized shared understanding of how the Fed responds to economic developments. Reuters reported that, after the speech, she supported additional rate increases because inflation remained too high.',inference='Use conditional rate and inflation scenarios in equity-duration and hedge stress tests; avoid treating speeches as fixed policy promises.',uncertainty='An individual official’s views, not a new FOMC decision or an agreed path. The rate comments were reported from remarks after the prepared speech.',secondary='https://www.reuters.com/business/feds-paulson-says-understanding-not-guidance-drives-effective-communication-2026-11-19/'),
dict(title='Intuit agrees to sell Mailchimp to Bending Spoons',category='Major technology / business',date='Announced November 19, 2026; FY27 Q1 ended October 31',source='https://investors.intuit.com/_assets/_d2e22f68d63e51dea352101f414a0724/intuit/news/2026-11-19_Intuit_Reports_First_Quarter_Results_and_Enters_1331.pdf',credit='Intuit FY27 Q1 release, November 19, 2026',slug='intuit-mailchimp-divestiture',alt='Transaction information panel showing an approximately 3.68 billion dollar Mailchimp sale agreement, Bending Spoons as buyer, and expected early 2027 closing subject to conditions.',nodes=['Mailchimp agreement\nApprox. $3.68 billion','Buyer\nBending Spoons','Expected closing\nEarly 2027'],facts='Intuit announced a definitive agreement to sell Mailchimp to Bending Spoons for approximately $3.68 billion. Mailchimp’s quarterly revenue declined 1% to $313 million. Closing is expected in early calendar 2027, subject to regulatory approvals and customary conditions.',inference='Separate continuing-business growth from divestiture effects when updating INTU valuation and earnings-event models.',uncertainty='The sale has not closed. Intuit’s published guidance excludes its impact and is to be updated at closing; no deal completion or share-price reaction is assumed.')]
end=date(2026,11,19);target=end-timedelta(days=28)
assert target==date(2026,10,22)
assert date(2026,11,13)-timedelta(days=28)==date(2026,10,16)
assert date(2026,11,16)-timedelta(days=28)==date(2026,10,19)
dashboard='''## Quant & Market Dashboard

**Data status / overnight liquidity:** No live executable futures/ETF feed or verified overnight spreads, book depth, volume or funding/repo snapshot was available. Use story three’s timestamped futures direction only as a cautious proxy. A Reuters global-markets report describes safe-haven Treasury buying and a benchmark ten-year yield below 5%; this is reported market context, not a verified Treasury liquidity or bid/ask measure. Source: https://www.reuters.com/world/china/global-markets-global-markets-2026-11-20/

**Volatility regime — high, near the stressed threshold; medium confidence.** Cboe’s quotes page and Yahoo history show VIX at 28.44 for the November 19 close, up from 24.56 on November 18. These are prior-close observations, not live implied volatility or the SPY/QQQ options surface. Editorial thresholds: below 15 low, 15–20 moderate, 20–30 high, 30 or above stressed. VIX cannot establish book liquidity or dealer positioning. Sources: https://www.cboe.com/data/quotes/vix/multiple and https://finance.yahoo.com/quote/%5EVIX/history/

**Factors — performance unavailable, no rankings:**

| Exposure | ETF proxy | One session | Four weeks |
|---|---|---|---|
| Momentum | MTUM | Unavailable | Unavailable |
| Value | VLUE | Unavailable | Unavailable |
| Quality | QUAL | Unavailable | Unavailable |
| Size | IWM | Unavailable | Unavailable |
| Growth | IWF | Unavailable | Unavailable |
| Low volatility | SPLV | Unavailable | Unavailable |

Intended latest completed common-session end: **November 19**; preceding session **November 18**. Four-week target start freshly calculated as **October 22**, exactly 28 calendar days before November 19. Actual common start, comparable prices and adjustments: **unverified; no substitute date used**. Required basis is split-adjusted closing-price return excluding distributions, applying in-window splits once and excluding out-of-window actions. Alpha Vantage’s standard terms provide personal non-commercial use unless otherwise agreed in writing; publication permission for this repository and newsletter use was not verified. No Alpha Vantage prices, corporate actions or derived returns are exported. A publication-cleared comparable alternative was not verified. ETF proxies are not pure factors. Terms: https://www.alphavantage.co/terms_of_service/

**SPY/QQQ and options execution:** U.S. cash opening auction is 8:30 a.m. CST. Michigan’s final November consumer survey is scheduled for **9:00 a.m. CST**, still unreleased at cutoff. November 20 is monthly options expiry. Distinguish AM-settled index contracts from ETF options and PM expiries; confirm contract-specific last trading and settlement terms. Gamma sensitivity can rise near expiry, but dealer gamma sign, concentrations and pin levels are unverified. Use limits, staged participation and quote-age checks. Compare current spreads, executable depth and slippage with time-of-day baselines; thin premarket prints and attractive option midpoints without size are liquidity traps. Reset assumptions after the auction and the release. Calendar sources: https://www.sca.isr.umich.edu/ and https://www.optionseducation.org/referencelibrary/expiration-calendar

**Microstructure implications / research watchlist:** Gate participation on fresh quotes, displayed size and spread relative to baseline; stress partial fills and abrupt liquidity withdrawal. Monitor SPY, QQQ, IWM, MTUM, VLUE, QUAL, IWF, SPLV, TLT, NVDA and INTU. This is a research watchlist, not a recommendation to trade.

### DRL Improvements for the MATLAB System

- Enforce exposure, turnover, drawdown and capital-preservation limits outside the learned policy; log every veto and breach.
- Reward net performance after commissions, spread and impact, penalizing tail losses and unstable turnover. Simulate latency, partial fills and liquidity withdrawal.
- Use purged walk-forward evaluation with embargoes, frozen final holdouts and regime-stratified stress tests. Compare against cash and simple baselines; retain failed trials and execution-cost sensitivity results.

### Model Hygiene

Fit transforms only within training folds. Use point-in-time constituents and release timestamps to prevent survivorship, leakage and look-ahead bias. Version corporate actions and apply adjustments once. Reject stale, crossed or zero-size options quotes. Count all configurations, control multiple testing, and monitor calibration and drift; do not select retraining rules on the final holdout.

### MATLAB Optimization Patterns

- Align timezone-aware timetables before vectorizing features and returns; keep observation dates separate from publication timestamps.
- Profile before parallel Bayesian optimization. Freeze objective inputs and random streams, and archive trial order; parallel timing can still prevent exact reproducibility.
- Keep data, reward, independent risk gates and execution modules separate. Use GPUs for suitable large tensor workloads; benchmark transfer overhead and minimize host/device transfers.

Technical references: https://www.mathworks.com/help/stats/parallel_bayesian_optimization.html ; https://www.mathworks.com/help/reinforcement-learning/ug/train-reinforcement-learning-agents.html ; https://www.mathworks.com/help/parallel-computing/measure-and-improve-gpu-performance.html

**High-value quant research question:** Does adding order-flow persistence to a spread-and-volatility participation gate reduce net SPY/QQQ execution shortfall versus the same gate without memory? Test matched signals in purged walk-forward folds with identical costs and separate expiry-day results. It is worth testing because persistent liquidity changes may matter beyond a single spread snapshot; the preprint does not establish that benefit for U.S. ETFs.
'''
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def f(n):return ImageFont.truetype(font,n)
for i,s in enumerate(stories,1):
 s['image']=f'2026-11-20-story-{i}-{s["slug"]}.png'
 im=Image.new('RGB',(1200,650),'#101c2b');d=ImageDraw.Draw(im)
 d.text((50,30),'MARKET STATE LAB / QUANT MARKET BRIEF',font=f(24),fill='#58d1c9')
 for j,line in enumerate(textwrap.wrap(s['title'],51)):d.text((50,90+j*43),line,font=f(32),fill='white')
 if i==3:
  zero=1040;scale=390
  for j,(label,v) in enumerate([('Dow',-.20),('S&P 500',-.76),('Nasdaq 100',-1.63)]):
   y=245+j*80;d.text((50,y),label,font=f(26),fill='white');x=zero+v*scale;d.rectangle((x,y,zero,y+36),fill='#58d1c9');d.text((x-105,y),f'{v:.2f}%',font=f(23),fill='white')
  d.line((zero,235,zero,485),fill='white',width=2);d.line((260,485,1040,485),fill='white',width=2)
  for v in [-2,-1.5,-1,-.5,0]:
   x=zero+v*scale;d.line((x,485,x,493),fill='white',width=2);d.text((x-25,500),f'{v:g}%',font=f(19),fill='white')
  d.text((50,540),'Reported snapshot: Nov. 20, 4:57 a.m. EST — not live',font=f(22),fill='#b8c9d8')
 else:
  for j,node in enumerate(s['nodes']):
   x=50+j*380;d.rounded_rectangle((x,280,x+340,440),radius=12,fill='#23394e',outline='#58d1c9',width=2)
   for k,line in enumerate(node.split('\n')):d.text((x+15,315+k*44),line,font=f(23),fill='white')
  label='Conceptual hypothesis — not established causality' if i==2 else 'Conceptual information panel — not a forecast'
  d.text((50,490),label,font=f(23),fill='#b8c9d8')
 d.text((50,575),'2026-11-20 | Graphic: Market State Lab',font=f(21),fill='#b8c9d8');d.text((50,610),s['credit'],font=f(19),fill='#b8c9d8');im.save(p/s['image'])
im=Image.new('RGB',(1200,650),'#101c2b');d=ImageDraw.Draw(im)
for y,t,n,c in [(65,'MARKET STATE LAB',35,'#58d1c9'),(170,'Quant Market Brief',60,'white'),(285,'Rough Volatility',50,'white'),(355,'& Expiry Risk',50,'white'),(525,'November 20, 2026',32,'#58d1c9')]:d.text((65,y),t,font=f(n),fill=c)
im.save(p/'2026-11-20-linkedin-cover.png')
signup=lambda ch:f'https://market-state-lab.ghost.io/?utm_source={ch}&utm_medium={"repository" if ch=="github" else "social"}&utm_campaign=qmb_2026-11-20#/portal/signup'
md=f'# {title}\n\nResearch cutoff: {cutoff}. Premarket edition; no live executable feed.\n\n[Subscribe by email]({signup("github")}).\n\n'
for i,s in enumerate(stories,1):
 md+=f'## {i}. {s["title"]}\n\n*{s["category"]} | {s["date"]}*\n\n![{s["alt"]}]({s["image"]})\n\nGraphic: Market State Lab. Source: {s["credit"]}.\n\n**Facts:** {s["facts"]}\n\n**Inference / Why it matters:** {s["inference"]}\n\n**Uncertainty:** {s["uncertainty"]}\n\n[Direct source]({s["source"]}).\n\n'
 if s.get('secondary'):md+=f'[Reporting on post-speech remarks]({s["secondary"]}).\n\n'
md+=dashboard+f'\n[Subscribe by email]({signup("github")}). Please forward this edition to a colleague who tests systematic strategies.\n\nDisclosure: Research and education, not individualized financial advice. Markets involve risk; research claims require independent validation. © Market State Lab.\n'
(p/'2026-11-20.md').write_text(md)
(p/'2026-11-20-sources.json').write_text(json.dumps({'cutoff':cutoff,'stories':stories,'chart_inputs':{'story3':{'labels':['Dow E-minis','S&P 500 E-minis','Nasdaq 100 E-minis'],'percent_change':[-.20,-.76,-1.63],'asof':'2026-11-20T04:57:00-05:00','status':'Reuters reported snapshot, not live'}},'factor_panel':{'end':str(end),'preceding_session':'2026-11-18','target_start':str(target),'actual_start':None,'price_basis':'split-adjusted closing-price returns excluding distributions','prices':None,'status':'unavailable; public dissemination rights and comparable publication-cleared closes not verified','terms':'https://www.alphavantage.co/terms_of_service/'},'qa':{'story_images':5,'drl_amount_check':'passed','prior_artwork_overwritten':False}},indent=2))
li='Decision panel | Cutoff: '+cutoff+'\n\n'
summaries=[
'AI: MIT’s November 19 report describes an LLM-assisted audit of nearly 4,000 clinical prediction studies. Public code often lacked reuse information. Implication: require documented, executable research environments; transfer to trading repositories is unproven.',
'QUANT: A November 18 preprint models how asynchronous market makers with different horizons can create persistent order flow and rough volatility. It uses simulations and Binance data. Implication: test execution-cost states; U.S. ETF transfer is unproven.',
'MARKETS: Reuters’ 4:57 a.m. EST snapshot showed Dow, S&P 500 and Nasdaq 100 futures down 0.20%, 0.76% and 1.63%. Implication: recheck opening capacity. These are early reported moves, not live executable quotes.',
'FED: On November 19 Paulson emphasized understanding the Fed reaction function; Reuters reported her support for more tightening after the speech. Implication: stress conditional rate paths. These are individual views, not an FOMC decision.',
'BUSINESS: Intuit agreed November 19 to sell Mailchimp to Bending Spoons for about $3.68 billion. Closing is expected early 2027, subject to conditions. Implication: separate divestiture effects from continuing growth; the sale is not completed.'
]
for i,(s,sm) in enumerate(zip(stories,summaries),1):li+=f'{i}. {sm}\n{s["source"]}\n'+(s.get('secondary','')+'\n' if s.get('secondary') else '')+'\n'
li+='VOLATILITY / EXECUTION: High, medium confidence; November 19 prior-close VIX 28.44. Live depth, spreads, funding and dealer gamma unverified. Monthly expiry today; opening auction 8:30 a.m. CST, Michigan release 9:00. Stage orders and check quote age. Factor returns unavailable: publication rights and comparable cleared closes unverified; four-week target October 22–November 19. No rankings.\n\nMATLAB / DRL: Independent capital-preservation gates; net-of-cost rewards with partial fills and latency; purged walk-forward regime tests. Profile before parallel optimization, archive random streams and trial order, and audit leakage, actions, survivorship, multiple testing, calibration and drift.\n\nFull dashboard, source links and five graphics: https://github.com/rsh63/market-state-lab/blob/main/2026-11-20.md\n\nResearch and education, not individualized financial advice.\n\nWould adding order-flow persistence to a spread-and-volatility gate reduce SPY/QQQ execution shortfall after costs, including expiry days?\n\nSubscribe by email: '+signup('linkedin')
(p/'linkedin.txt').write_text(li)
section=md.split('### DRL Improvements for the MATLAB System')[1].split('### Model Hygiene')[0]
assert not re.search(r'\$|USD|dollar|\b\d[\d,]*\b',section)
assert len(stories)==len(re.findall(r'^## [1-5]\. ',md,re.M))==5
qa=Image.new('RGB',(1200,975),'white')
for i,fn in enumerate([p/s['image'] for s in stories]+[p/'2026-11-20-linkedin-cover.png']):qa.paste(Image.open(fn).resize((600,325)),((i%2)*600,(i//2)*325))
qa.save(p/'qa.png')
shutil.copy(__file__,p/'2026-11-20-build.py')
print('Prepared exactly five stories, five dated story graphics, cover, sources and dashboard. DRL amount and date checks passed.')
