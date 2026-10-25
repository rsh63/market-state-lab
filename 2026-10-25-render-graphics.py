from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-10-25';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'25 OCT 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)
f=page('Audit numerical gradients before trusting training','New softmax / cross-entropy preprint • conceptual failure cases','Source: Barron et al., arXiv:2610.31642v1, October 22, 2026.\nAuthor-reported numerical failures; no claim that a particular MATLAB release is affected.')
box(f,.05,.40,.42,.31,'SOFTMAX COLLAPSE','Dominant target logit\nTarget gradient rounds to zero')
box(f,.53,.40,.42,.31,'SOFTMAX CANCELLATION','Equal student / teacher logits\nNonzero gradient appears')
f.text(.05,.23,'Audit extreme logits, gradient sums and equal-logit cases.',fontsize=21,weight='bold');save(f,'story-1-gradient-integrity')
f=page('Liquidity forecasts depend on regime compatibility','Concentrated-liquidity AMM study • not an equity-book calibration','Source: Lee et al., arXiv:2610.30539v1, October 21, 2026.\nConceptual map; no forecast-error magnitudes or equity returns asserted.')
box(f,.05,.43,.42,.28,'TWO COMPATIBLE POOLS','Lower active-band forecast error\nthan a martingale benchmark')
box(f,.53,.43,.42,.28,'THIRD POOL','Out-of-sample diagnostics\nindicate nonstationarity')
f.text(.05,.22,'Test stationarity and benchmark performance before use.',fontsize=21,weight='bold');save(f,'story-2-liquidity-regimes')
f=page('Reported positioning preference favors quality','Qualitative market context • not a live flow or depth measurement','Source: MarketWatch, updated October 24, 2026 at 9:37 a.m. ET.\nNo flow amounts asserted. Positioning, returns and executable depth are different measures.')
box(f,.05,.43,.42,.28,'QUALITY','Reported investor preference\nfor lower-risk shares')
box(f,.53,.43,.42,.28,'MOMENTUM','Previously strong stocks\nface a change in preference')
f.text(.05,.22,'Confirm the narrative against dated returns and execution data.',fontsize=21,weight='bold');save(f,'story-3-quality-preference')
f=page('U.S. flash PMI eases but remains expansionary','Composite Output PMI • index points, not GDP growth rates','Source: S&P Global October 23, 2026 release and analysis.\nOctober is a flash estimate; the survey also flags stronger selling-price pressure.')
a=f.add_axes([.14,.28,.75,.42]);vals=[58.4,57.6];a.bar(['September','October flash'],vals,color=[OPEN,BLUE],edgecolor=NAVY,width=.5);a.set_ylim(0,70);a.set_ylabel('PMI index points');a.axhline(50,color=GOLD,ls='--',lw=1.5);a.text(.5,51,'Expansion threshold: 50',ha='center',fontsize=16,color=GRAY);a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals):a.text(i,v+1.5,f'{v:.1f}',ha='center',fontsize=22,weight='bold')
save(f,'story-4-flash-pmi')
f=page('Jio IPO: bid demand is not proceeds','Reported subscription demand • October 23, 2026','Source: Reuters, October 23, 2026.\nBids are not funds raised, final allocations or guaranteed aftermarket returns.')
box(f,.05,.41,.42,.30,'REPORTED BIDS','More than $77 billion\nAggregate bid demand')
box(f,.53,.41,.42,.30,'PUBLIC SUBSCRIPTIONS','More than 22×\nShares offered')
f.text(.05,.22,'Separate demand, allocation, valuation and trading liquidity.',fontsize=21,weight='bold');save(f,'story-5-jio-ipo-demand')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY);f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold');f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold');f.text(.05,.63,'OCTOBER 25, 2026',fontsize=20,color='#B8C8D2');f.text(.05,.4,'Gradient integrity\n& PMI pressure',fontsize=36,color='white',weight='bold',linespacing=1.3);f.text(.05,.17,'Numerical checks • Liquidity regimes • Growth and prices',fontsize=19,color='#B8C8D2');f.text(.05,.07,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2');save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
