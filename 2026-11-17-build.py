from pathlib import Path
import json,re,html,textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image,ImageOps,ImageDraw
P=Path(__file__).parent; D='2026-11-17'; cutoff='November 17, 2026, 6:33 a.m. CST (12:33 UTC)'
title='Quant Market Brief — November 17, 2026: Model Risk & Retail Results'
S=json.loads((P/'2026-11-17-stories.json').read_text())
F=[['Momentum', 'MTUM', 65.71, 67.98, 80], ['Value', 'VLUE', 184.89, 189.18, 199.52], ['Quality', 'QUAL', 55.16, 56.02, 56.78], ['Size', 'IWM', 272.94, 277.54, 278.94], ['Growth', 'IWF', 111.59, 114.89, 127.91], ['Low volatility', 'SPLV', 78.37, 78.44, 72.14]]
rows=''; inputs=[]
for fac,sym,c,p,b in F:
 day=100*(c/p-1);med=100*(c/b-1)
 rows+=f'| {fac} | [{sym}](https://stockanalysis.com/etf/{sym.lower()}/history/) | {day:+.2f}% | {med:+.2f}% |\n'
 inputs.append(dict(factor=fac,symbol=sym,closeNov16=c,closeNov13=p,closeOct9=b,daily=day,oneMonth=med,source=f'https://stockanalysis.com/etf/{sym.lower()}/history/'))
dash=(P/'2026-11-17-dashboard-template.md').read_text().replace('{ROWS}',rows.rstrip())
(P/'dashboard.md').write_text(dash)
intro=f'Research cutoff: **{cutoff}**. Tuesday premarket edition; market data are explicitly timestamped reported/delayed snapshots or prior-close observations, not live executable quotes.'
disclosure='Research and education only—not individualized financial advice. No trading performance is promised.'
cta=lambda c,m:f'https://market-state-lab.ghost.io/?utm_source={c}&utm_medium={m}&utm_campaign=qmb_{D}#/portal/signup'
gh=f'https://github.com/rsh63/market-state-lab/blob/main/{D}.md'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':16,'text.parse_math':False})
for i,s in enumerate(S,1):
 s['image']=f'{D}-story-{i}-{s["slug"]}.png';fig=plt.figure(figsize=(12,6.75),dpi=100,facecolor='#f4f7fa')
 fig.text(.045,.94,'MARKET STATE LAB / QUANT MARKET BRIEF',size=16,color='#0d3543',weight='bold');fig.text(.82,.94,'17 NOV 2026',size=13,color='#0d3543')
 fig.text(.045,.83,'\n'.join(textwrap.wrap(s['head'],55)),size=22,weight='bold',color='#132c3b',va='top')
 for j,l in enumerate(s['labels']):fig.text(.065,.61-j*.115,l,size=21 if len(l)<44 else 18,color='#0e615f',bbox=dict(facecolor='white',edgecolor='#d4dce0',pad=10))
 fig.text(.045,.085,'\n'.join(textwrap.wrap('Source: '+s['credit'],105)),size=11,color='#41586a')
 fig.text(.045,.035,['Survey findings • not causal proof','Conceptual mechanism • illustrative and uncalibrated','November 16 index closes • not live quotes','Scenario remarks • not a rate decision','Reported Q3 results • guidance is forward-looking'][i-1],size=10,color='#41586a')
 fig.savefig(P/s['image']);fig.savefig(P/s['image'].replace('.png','.svg'));plt.close(fig)
fig=plt.figure(figsize=(12,6.75),dpi=100,facecolor='#102c3b');fig.text(.07,.84,'MARKET STATE LAB',color='#93bfc6',size=18);fig.text(.07,.69,'Quant Market Brief',color='white',size=33,weight='bold');fig.text(.07,.59,'NOVEMBER 17, 2026',color='#a9c5d1',size=18);fig.text(.07,.35,'Model risk\n& retail results',color='white',size=34,weight='bold');fig.text(.07,.12,'Decision rights • Hedge robustness • Retail demand',color='#a9c5d1',size=18);fig.savefig(P/f'{D}-linkedin-cover.png');fig.savefig(P/f'{D}-linkedin-cover.svg');plt.close(fig)
body=''
for i,s in enumerate(S,1):body+=f'## {i}. {s["head"]}\n\n![{s["alt"]}]({s["image"]})\n\n*Graphic: Market State Lab; {s["credit"]}.*\n\n**Fact — {s["date"]}:** {s["fact"]} [Direct source]({s["url"]})\n\n**Inference / Why it matters:** {s["why"]}\n\n**Uncertainty:** {s["unc"]}\n\n'
md=f'# {title}\n\n{intro}\n\n[Subscribe by email]({cta("github","technical_archive")}).\n\n'+body+dash+f'\n[Subscribe by email]({cta("github","technical_archive")}).\n\n*{disclosure}*\n'
(P/f'{D}.md').write_text(md)
(P/f'ghost-{D}.md').write_text(f'# {title}\n\n{intro}\n\n'+body+dash+f'\n[Technical companion]({gh}).\n\nPlease forward this edition to one colleague who would find it useful.\n\n*{disclosure}*\n')
li=f'# {title}\n\n{intro}\n\n**Decision panel:** Test model-transfer risk, assign AI decision rights and refresh quotes after Monday’s selloff.\n\n'
for i,s in enumerate(S,1):li+=f'**{i} · {s["cat"]}:** {s["fact"]} **Implication:** {s["why"]} **Caveat:** {s["unc"]} [Source]({s["url"]})\n\n'
li+=f'**Volatility/execution:** Moderate; medium confidence. Delayed VIX 23.29 at November 17, 05:18 CST, versus Monday close 22.91. Cash auction 08:30 CST today. Current executable depth and dealer gamma are unverified.\n\n**MATLAB/DRL:** External risk limits, cost-aware rewards, purged target horizons and a one-use holdout. Profile and use causal timetables.\n\n[GitHub companion]({gh}).\n\n*{disclosure}*\n\n**Discussion:** Do model-transfer stress tests reject strategies that pass ordinary calibration and walk-forward checks?\n\n[Subscribe by email]({cta("linkedin","newsletter")}).\n'
(P/f'linkedin-{D}.md').write_text(li);(P/'title.txt').write_text(title)
(P/f'linkedin-post-{D}.txt').write_text(title+'\n\nDoes a well-calibrated model survive a change in information dynamics? Five stories plus execution controls and MATLAB research ideas.\n\nTechnical companion: '+gh+'\nEmail: '+cta('linkedin','social')+'\n\n'+disclosure)
(P/f'{D}-sources.json').write_text(json.dumps(dict(cutoff=cutoff,stories=S),indent=2));(P/f'{D}-market-inputs.json').write_text(json.dumps(dict(factors=inputs,VIX=dict(value=23.29,timestamp='2026-11-17T05:18:00-06:00',basis='delayed observation; Monday close 22.91'),funding=dict(date='2026-11-13',SOFR=3.90,updated='2026-11-16T07:02:00-06:00')),indent=2))
drl=md.split('### DRL Improvements for the MATLAB System')[1].split('### Model hygiene')[0];assert not re.search(r'[$€£]|\b(?:USD|dollars|million|billion)\b',drl,re.I);assert len(re.findall(r'^## [1-5]\. ',md,re.M))==5;assert md.count('\n![')==5
imgs=[Image.open(P/s['image']).resize((600,338)) for s in S]+[Image.open(P/f'{D}-linkedin-cover.png').resize((600,338))];mont=Image.new('RGB',(1200,1014),'white')
for i,im in enumerate(imgs):mont.paste(im,(i%2*600,i//2*338))
mont.save(P/'image-qa.png')
print(rows)
