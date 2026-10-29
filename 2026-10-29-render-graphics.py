from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-10-29';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'29 OCT 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)


import json,textwrap
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
heads=['Attention gates separate instructions from data','Quote-feed artifacts can mimic excitation','Post-Fed futures: Nasdaq falls, Dow rises','Fed holds target range; two dissent for a hike','Microsoft: cloud growth outpaces total revenue']
subs=['Conceptual defense summary • model-specific preprint evidence','Conceptual event-definition comparison • large-tick stocks','October 29 at 5:18 a.m. ET / 4:18 CT • reported snapshot','October 28 decision • confirmed policy, not a forecast','FY27 Q1 year-over-year growth (%) • overlapping metrics']
notes=['No defense guarantees security; preserve external authority boundaries.','Persistence must be confirmed causally; filtering adds latency.','Percent change from reference levels; no spread or depth information.','Cook and Hammack preferred a quarter-point increase.','Cloud revenue is part of total revenue; these bars are not additive.']
for i,s in enumerate(S,1):
 cap='Source: '+s['credit'].replace('Market State Lab; ','')+'\n'+notes[i-1]
 f=page(heads[i-1],subs[i-1],cap)
 if i in [3,5]:
  a=f.add_axes([.13,.25,.79,.44]);vals=[-1.01,-.26,.51] if i==3 else [19,21,30];labs=['Nasdaq-100','S&P 500','Dow'] if i==3 else ['Total revenue','Operating income','Cloud revenue'];a.bar(labs,vals,color=[BLUE if v>=0 else GOLD for v in vals],width=.5);a.axhline(0,color=NAVY,lw=1);a.set_ylim((-1.35,.75) if i==3 else (0,38));a.set_ylabel('Change (%)');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
  for j,v in enumerate(vals):a.text(j,v+(.02 if v>=0 else -.02) if i==3 else v+(1 if v>=0 else -1),f'{v:+.2f}%' if i==3 else f'{v:+.0f}%',ha='center',va='bottom' if v>=0 else 'top',fontsize=21,weight='bold')
 else:
  for j,t in enumerate(s['panels']):box(f,.05+j*.48,.39,.42,.30,['TRUST BOUNDARY','EVENT DEFINITION','','POLICY DECISION'][i-1], '\n'.join(textwrap.wrap(t,23)))
  f.text(.05,.22,{1:'Process retrieved data without granting execution authority.',2:'Compare raw and confirmed events after latency costs.',4:'A hold does not precommit the next decision.'}[i],fontsize=20,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [(.05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'OCTOBER 29, 2026',20,'#B8C8D2'),(.05,.4,'Fed hold\n& quote-feed integrity',34,'white'),(.05,.17,'Trust boundaries • Causal events • Post-Fed execution',19,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
