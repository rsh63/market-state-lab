from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-11-04';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'04 NOV 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=15,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)


import json,textwrap
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
heads=['Prism: validate decision calibration','AMM stress: persistence matters','Post-election futures snapshot','Today: separate macro release windows','AMD: Q3 growth by business scope']
subs=['Vendor-reported decision model • not a financial benchmark','Conceptual theory • not an empirical equity-market result','Reported change (%) • 03:22 CST / 04:22 EST • not live','November 4, 2026 • results unknown at 06:34 CST cutoff','Year-over-year growth • total revenue versus data-center segment']
for i,s in enumerate(S,1):
 cap='\n'.join(textwrap.wrap('Source: '+s['credit'],95));f=page(heads[i-1],subs[i-1],cap)
 if i==3:
  vals=[.84,.35,.16];labs=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini'];a=f.add_axes([.14,.27,.80,.42]);a.bar(labs,vals,color=BLUE,width=.5);a.set_ylim(0,1);a.set_ylabel('Change (%)');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False);a.tick_params(axis='x',labelsize=17)
  for j,v in enumerate(vals):a.text(j,v+.035,f'{v:+.2f}%',ha='center',fontsize=22,weight='bold')
 else:
  for j,t in enumerate(s['panels']):box(f,.05+j*.48,.38,.42,.31,{1:'DECISION MODEL',2:'THEORETICAL AMM',4:'RELEASE CALENDAR',5:'REPORTED RESULTS'}[i],'\n'.join(textwrap.wrap(t,25)))
 f.text(.05,.16,{1:'Test calibration and abstention on untouched decisions.',2:'Equal volatility can conceal different stress persistence.',3:'A reversal in price does not establish restored depth.',4:'Trade data also scheduled at 07:30 CST / 13:30 UTC.',5:'Distinct scopes; segment growth is not total growth.'}[i],fontsize=19,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [(.05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'NOVEMBER 4, 2026',20,'#B8C8D2'),(.05,.4,'Post-election repricing\n& AMD growth',34,'white'),(.05,.17,'Decision calibration • Stress persistence • Macro windows',18,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
