from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent; D='2026-10-23'
NAVY='#0D2638'; BLUE='#197D96'; GOLD='#BE8C35'; INK='#233746'; GRAY='#586976'; BG='#F7F9FB'; OPEN='#DCEBF0'; NEG='#9A5E58'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'axes.labelcolor':INK,'xtick.color':GRAY,'ytick.color':INK,'svg.fonttype':'none'})
def page(title,subtitle,caption):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG)
 f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY))
 f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold')
 f.text(.96,.947,'23 OCT 2026',color='#B7D1DF',fontsize=14,ha='right')
 f.text(.04,.84,title,fontsize=25,weight='bold')
 f.text(.04,.775,subtitle,fontsize=18,color=GRAY)
 f.text(.04,.043,caption,fontsize=16,color=GRAY,linespacing=1.35)
 return f
def box(f,x,y,w,h,title,body,color=BLUE):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF',lw=1.3))
 f.text(x+.018,y+h-.045,title,color=color,weight='bold',fontsize=20,va='top')
 f.text(x+.018,y+h-.115,body,fontsize=20,va='top',linespacing=1.4)
def arrow(f,a,b): f.patches.append(FancyArrowPatch(a,b,transform=f.transFigure,arrowstyle='->',mutation_scale=20,color=GRAY,lw=1.4))
def save(f,name):
 for ext in ['png','svg']: f.savefig(P/f'{name}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f=page('METTA separates two timescales of RL adaptation','Conceptual architecture • evaluated on nonfinancial tasks','Source: Najar et al., arXiv:2610.31656v1, submitted October 22, 2026.\nConceptual diagram; no calibrated trading result. Transfer to execution is untested.')
box(f,.05,.38,.39,.31,'WITHIN AN EPISODE','Causal neural memory\nFine-grained adaptation\nLinear sequence complexity')
box(f,.56,.38,.39,.31,'ACROSS EPISODES','Compact summaries\nLong-range task inference\nNo full-history attention',GOLD)
arrow(f,(.44,.535),(.56,.535))
f.text(.05,.24,'MATLAB research implication:\nSeparate execution state from regime context.',fontsize=20,weight='bold',linespacing=1.35)
f.text(.05,.15,'Trading transfer is a hypothesis to test, not a reported result.',fontsize=20,color=GRAY)
save(f,f'{D}-story-1-metta-adaptive-memory')
f=page('Volatility and spreads in competitive market making','Theoretical mechanism • at least two strategic market makers','Source: Onger & Foscari, arXiv:2610.30891v1, submitted October 22, 2026.\nIllustrative and uncalibrated. Model assumptions do not identify an executable spread.')
box(f,.05,.46,.36,.23,'HIGHER VOLATILITY','Greater uncertainty in\nunderlying asset value')
box(f,.59,.46,.36,.23,'WIDER SPREAD','Strict widening at\nmodel equilibrium',GOLD)
arrow(f,(.41,.575),(.59,.575))
box(f,.05,.19,.90,.20,'LEARNING RESULT — ADDITIONAL ASSUMPTIONS','As ticks shrink, no-internal-regret learning\napproaches the Nash price envelope.',BLUE)
save(f,f'{D}-story-2-competitive-market-making')
f=page('Thursday’s ETF returns show a concentrated selloff','October 22, 2026 • close-to-close price returns (%)','Source: ChartExchange completed ETF bars, October 22 versus October 21, 2026.\nPrior-close observations; these bars do not describe Friday’s opening liquidity.')
a=f.add_axes([.17,.29,.74,.42]); names=['SPY','QQQ','IWM']; vals=[-1.181,-2.859,.069]
a.barh(names,vals,color=[BLUE,NEG,GOLD],edgecolor=NAVY,height=.56); a.invert_yaxis(); a.axvline(0,color=NAVY,lw=1.3); a.set_xlim(-3.5,.6); a.set_xlabel('Price change (%)'); a.grid(axis='x',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals): a.text(v-.08 if v<0 else v+.08,i,f'{v:+.2f}%',va='center',ha='right' if v<0 else 'left',fontsize=20,weight='bold')
f.text(.05,.17,'QQQ: 64.55m shares • 13.53-point intraday range',fontsize=20,weight='bold')
save(f,f'{D}-story-3-tech-close-divergence')
f=page('Initial and continuing claims move in opposite directions','Seasonally adjusted advance estimates • different reference weeks','Source: U.S. Department of Labor, released October 22, 2026 at 8:30 a.m. ET.\nBoth axes start at zero; panels use different scales. Advance estimates can be revised.')
for left,title,dates,vals,top in [(.09,'Initial claims',['Oct 10','Oct 17'],[200,194],230),(.59,'Continuing claims',['Oct 3','Oct 10'],[1703,1728],1950)]:
 a=f.add_axes([left,.28,.33,.40]); a.bar(dates,vals,color=[OPEN,BLUE],edgecolor=NAVY,width=.54);a.set_ylim(0,top);a.set_title(title,fontsize=21,weight='bold',pad=12);a.set_ylabel('Thousands');a.set_xlabel('Week ending, 2026');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
 for i,v in enumerate(vals):a.text(i,v+top*.025,f'{v:,}',ha='center',fontsize=20,weight='bold')
save(f,f'{D}-story-4-weekly-claims-divergence')
f=page('Solidigm’s proposed U.S. listing is on hold','Financing-path diagram • reported October 23 in Seoul','Source: Reuters, October 22–23, 2026; company statement described in the report.\nA financing pause does not by itself establish weaker end demand or canceled investment.')
box(f,.05,.42,.39,.27,'PROPOSED U.S. IPO','ON HOLD\nMarket volatility\nShareholder concerns',GOLD)
box(f,.56,.42,.39,.27,'EXPANSION FUNDING','UNDER REVIEW\nTiming and financing\nremain unsettled',BLUE)
arrow(f,(.44,.55),(.56,.55))
f.text(.05,.24,'No IPO proceeds, valuation or replacement financing are asserted.',fontsize=20,weight='bold')
save(f,f'{D}-story-5-solidigm-ipo-pause')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold');f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold');f.text(.05,.63,'OCTOBER 23, 2026',fontsize=20,color='#B8C8D2')
f.text(.05,.40,'Adaptive memory\n& tech rotation',fontsize=38,color='white',weight='bold',linespacing=1.3)
f.text(.05,.18,'RL state • Market-making costs • Concentration risk',fontsize=19,color='#B8C8D2');f.text(.05,.08,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2')
save(f,f'{D}-linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))]
ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG))
qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
print('Rendered five dated graphics, cover, and newsletter-width QA montage.')
