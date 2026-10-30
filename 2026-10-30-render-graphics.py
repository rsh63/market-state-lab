from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-10-30';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'30 OCT 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)


import json,textwrap
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
heads=['Unified training: one likelihood-based algorithm','Tail-risk tests: count extreme observations','Technology futures lead early declines','September PCE: headline inflation exceeds core','Amazon: trailing-year free cash flow turns negative']
subs=['Conceptual research summary • trading transfer untested','Conceptual inference summary • effective evidence matters','October 30 at 4:04 a.m. ET / 3:04 CT • reported snapshot','September 2026 • year-over-year price-index change (%)','Trailing twelve months ended September • U.S. dollars, billions']
notes=['Data mixture and scheduling remain experimental choices.','Calendar length alone does not establish a reliable risk ranking.','Percent change from reference levels; no spread or depth information.','Headline monthly +0.5%; core monthly +0.3%; estimates revisable.','Quarterly AWS sales grew 39%; that is a different metric and period.']
for i,s in enumerate(S,1):
 f=page(heads[i-1],subs[i-1],'Source: '+s['credit'].replace('Market State Lab; ','')+'\n'+notes[i-1])
 if i in [3,4,5]:
  vals={3:[-2.16,-1.,-.05],4:[3.6,3.1],5:[14.8,-42.4]}[i];labs={3:['Nasdaq-100','S&P 500','Dow'],4:['Headline PCE','Core PCE'],5:['September 2025','September 2026']}[i]
  a=f.add_axes([.15,.25,.76,.44]);a.bar(labs,vals,color=[BLUE if v>=0 else GOLD for v in vals],width=.5);a.axhline(0,color=NAVY);a.set_ylim({3:(-2.8,.3),4:(0,4.5),5:(-55,25)}[i]);a.set_ylabel('Change (%)' if i!=5 else 'Free cash flow (USD billions)');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
  for j,v in enumerate(vals):a.text(j,v+({3:.08,4:.12,5:2}[i] if v>=0 else -{3:.08,4:.12,5:2}[i]),f'{v:+.2f}%' if i==3 else (f'{v:.1f}%' if i==4 else f'{v:+.1f}'),ha='center',va='bottom' if v>=0 else 'top',fontsize=21,weight='bold')
 else:
  for j,t in enumerate(s['panels']):box(f,.05+j*.48,.39,.42,.30,'TRAINING DESIGN' if i==1 else 'INFERENCE DESIGN','\n'.join(textwrap.wrap(t,23)))
  f.text(.05,.22,'Match compute; freeze data-mixture schedules.' if i==1 else 'Report exceedance counts and uncertainty.',fontsize=20,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [(.05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'OCTOBER 30, 2026',20,'#B8C8D2'),(.05,.4,'Tail-risk evidence\n& tech selloff',34,'white'),(.05,.17,'Training design • Inflation • Cash-flow discipline',19,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
