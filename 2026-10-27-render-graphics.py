from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-10-27';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'27 OCT 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)


import json,textwrap
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
heads=['Falling loss can hide lost information','Round prices: control for queue depth','Monday ETF rebound: completed daily rows','Housing data: reference month versus release time','Anthropic filing: separate loss from cash burn']
subs=['Known-answer synthetic-image test • trading transfer untested','Five Nasdaq stocks, 2025 • empirical preprint','October 26, 2026 • close-to-close price return (%)','Scheduled release • no September result available at cutoff','Public filing reported October 26 • offering terms uncertain']
notes=['Nine of ten seeds declined in factor readability.','More round-level liquidity; no longer depth-adjusted duration.','Source: ChartExchange completed historical rows; not quote-banner ticks.','Source: Census schedule checked October 27, 2026.','Reported net loss includes a large non-operating convertible-bond item.']
for i,s in enumerate(S,1):
 cap='Source: '+s['credit'].replace('Market State Lab; ','')+'\n'+notes[i-1]
 f=page(heads[i-1],subs[i-1],cap)
 if i==3:
  a=f.add_axes([.15,.25,.74,.46]);vals=[.711,1.107];a.bar(['SPY','QQQ'],vals,color=[OPEN,BLUE],edgecolor=NAVY,width=.5);a.set_ylim(0,1.4);a.set_ylabel('Daily price return (%)');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
  for j,v in enumerate(vals):a.text(j,v+.04,f'+{v:.3f}%',ha='center',fontsize=21,weight='bold')
 else:
  for j,t in enumerate(s['panels']):box(f,.05+j*.48,.39,.42,.30,['MONITORING TEST','MICROSTRUCTURE TEST','ETF RETURN','ECONOMIC CALENDAR','ACCOUNTING DISTINCTION'][i-1], '\n'.join(textwrap.wrap(t,24)))
  f.text(.05,.22,['Validate checkpoints on untouched downstream tasks.','Test departure and fill hazards conditional on depth.','','Keep release-time vintages separate from earlier features.','Review operating results, remeasurement and commitments.'][i-1],fontsize=20,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [(.05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'OCTOBER 27, 2026',20,'#B8C8D2'),(.05,.4,'Monitoring blind spots\n& queue depth',34,'white'),(.05,.17,'Checkpoint tests • Market microstructure • Housing data',19,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
