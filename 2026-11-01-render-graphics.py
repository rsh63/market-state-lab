from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-11-01';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'01 NOV 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)


import json,textwrap
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
heads=['Adaptive refresh: separate timing and correctness','Passive impact: queue state adds information','Next week: separate event-risk windows','Real GDP growth accelerates in Q3','Orbital TPU: a prototype milestone']
subs=['Conceptual training design • trading transfer untested','Conceptual model summary • no calibrated curves shown','Scheduled events • results unknown as of November 1, 2026','2026 quarterly growth • seasonally adjusted annual rate (%)','Company-reported hardware demonstration • not commercial deployment']
for i,s in enumerate(S,1):
 cap='Source: '+s['credit']
 cap='\n'.join(textwrap.wrap(cap,95))
 f=page(heads[i-1],subs[i-1],cap)
 if i==4:
  vals=[2.2,3.4];labs=['Q2 2026','Q3 2026 (advance)']
  a=f.add_axes([.15,.25,.76,.44]);a.bar(labs,vals,color=[BLUE if v>=0 else GOLD for v in vals],width=.5);a.axhline(0,color=NAVY);a.set_ylim(0,4);a.set_ylabel('Change (%)');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
  for j,v in enumerate(vals):a.text(j,v+(.03 if v>=0 else -.1),f'{v:+.3f}%' if i==3 else f'{v:.1f}%',ha='center',va='bottom' if v>=0 else 'top',fontsize=21,weight='bold')
 else:
  for j,t in enumerate(s['panels']):box(f,.05+j*.48,.39,.42,.30,{1:'TRAINING DESIGN',2:'MODEL COMPONENT',3:'EVENT CALENDAR',5:'PROTOTYPE STATUS'}[i],'\n'.join(textwrap.wrap(t,24)))
  f.text(.05,.22,{1:'Match compute; keep holdouts outside refresh decisions.',2:'Charge latency, cancellations and adverse selection.',3:'November 6 jobs: 08:30 EST / 07:30 CST / 13:30 UTC.',5:'Reliability and lifecycle economics remain unproven.'}[i],fontsize=20,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [(.05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'NOVEMBER 1, 2026',20,'#B8C8D2'),(.05,.4,'Queue-aware execution\n& event risk',34,'white'),(.05,.17,'Adaptive training • GDP • Orbital computing',19,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
