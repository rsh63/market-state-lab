from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-11-02';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'02 NOV 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=15,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)


import json,textwrap
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
heads=['JEPA alignment: positive views matter','Risk automation: synchronization matters','Early futures: November 2 snapshot','Today: a simultaneous release window','Marvell–Lumentum: fixed share ratio']
subs=['Conceptual mechanism • theorem assumptions apply • trading transfer untested','Conceptual model summary • simulation, not a live-market causal estimate','Reported change (%) • 06:01 CST / 07:01 EST • historical, not live','Scheduled November 2, 2026 • results unknown at 08:42 CST cutoff','Announced November 2, 2026 • agreement is not a completed transaction']
for i,s in enumerate(S,1):
 cap='\n'.join(textwrap.wrap('Source: '+s['credit'],95))
 f=page(heads[i-1],subs[i-1],cap)
 if i==3:
  vals=[.49,.46,.74];labs=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini']
  a=f.add_axes([.14,.27,.80,.42]);a.bar(labs,vals,color=BLUE,width=.5);a.axhline(0,color=NAVY);a.set_ylim(0,1);a.set_ylabel('Change (%)');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False);a.tick_params(axis='x',labelsize=17)
  for j,v in enumerate(vals):a.text(j,v+.035,f'{v:+.2f}%',ha='center',fontsize=22,weight='bold')
  f.text(.05,.16,'Requote after the cash open; direction does not measure depth.',fontsize=19,weight='bold')
 else:
  panels={1:['Two observations\nof one scene','Alignment up to\na rotation'],2:['Common risk cuts\ncan synchronize flows','Stage execution; cap\naggregate participation'],4:['ISM Manufacturing\n09:00 CST / 15:00 UTC','Construction\n09:00 CST / 15:00 UTC'],5:['1 Lumentum share\n→ 4.500 Marvell shares','Closing conditional;\nexpected H1 2028']}[i]
  for j,t in enumerate(panels):box(f,.05+j*.48,.38,.42,.31,{1:'UNDER GOOD-VIEW ASSUMPTIONS',2:'AUTOMATION DESIGN',4:'RELEASE CALENDAR',5:'AGREEMENT TERMS'}[i],t)
  f.text(.05,.22,{1:'Test causal view design at matched data and compute.',2:'Preserve hard risk limits in every execution schedule.',4:'Refresh liquidity and preserve each release vintage.',5:'Fixed ratio: consideration moves with Marvell stock.'}[i],fontsize=20,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [(.05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'NOVEMBER 2, 2026',20,'#B8C8D2'),(.05,.4,'Risk synchrony\n& AI connectivity',34,'white'),(.05,.17,'JEPA views • Data window • Fixed-ratio deal',19,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
