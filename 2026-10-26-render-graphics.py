from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-10-26';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'26 OCT 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)

import json,textwrap
S=json.loads((P/'story-inputs.json').read_text())
for i,s in enumerate(S,1):
 title=['Robustness needs a perturbation map','Neural factors for Monte Carlo stratification','Premarket futures: a dated positive snapshot','FOMC: confirmed meeting dates','Meta launches financing for AI expansion'][i-1]
 subtitle=['17 algorithms • 273 configurations • nonfinancial benchmark','Conceptual pricing workflow • no speedup magnitude asserted','Indicative press snapshot • not executable liquidity','Calendar facts • no policy outcome assumed','Approximately $35bn announced offering • not completed proceeds'][i-1]
 cap='Source: '+s['credit'].replace('Market State Lab; ','')+'\n'+['Trading transfer remains untested.','Continuity has limits; results concern specified pricing models.','Reuters snapshot: 05:19 ET / 04:19 CT, October 26.','Verify release times before trading; dates do not determine the decision.','Final pricing, dilution and proceeds remain subject to terms.'][i-1]
 f=page(title,subtitle,cap)
 for j,t in enumerate(s['panels']):
  box(f,.05+j*.48,.39,.42,.30,['BENCHMARK','PRICING STEP','INDICATIVE MOVE','MEETING DATE','OFFERING COMPONENT'][i-1], '\n'.join(textwrap.wrap(t,25)))
 f.text(.05,.22,['Evaluate named disruptions, not average reward alone.','Compare variance and total compute cost at matched paths.','Refresh basis, quotes and auction state before the open.','Separate pre-decision and post-decision observations.','Separate capital raised, dilution and spending commitments.'][i-1],fontsize=20,weight='bold')
 save(f,f'story-{i}-{s["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
for x,y,t,sz,c in [( .05,.86,'MARKET STATE LAB',18,'#78BDD2'),(.05,.71,'Quant Market Brief',34,'white'),(.05,.63,'OCTOBER 26, 2026',20,'#B8C8D2'),(.05,.4,'Robust RL\n& AI financing',36,'white'),(.05,.17,'Perturbation tests • Pricing efficiency • Event risk',19,'#B8C8D2')]:f.text(x,y,t,fontsize=sz,color=c,weight='bold',linespacing=1.3)
save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
