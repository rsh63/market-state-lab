from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch,FancyArrowPatch
OUT=Path(__file__).parent
NAVY='#0B2237'; INK='#162B3D'; BLUE='#087CAB'; GOLD='#C98017'; MUTED='#536577'; BG='#F7F9FB'; GRID='#D9E1E7'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
def base(cat,title,sub):
 f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=BG);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(675,0));a.axis('off')
 a.add_patch(Rectangle((0,0),1200,68,color=NAVY));a.text(44,42,'MARKET STATE LAB / '+cat,color='white',fontsize=15,weight='bold');a.text(1156,42,'15 OCT 2026',ha='right',color='#ABD6E6',fontsize=13)
 a.text(44,120,title,color=INK,fontsize=26,weight='bold');a.text(44,160,sub,color=MUTED,fontsize=15)
 return f,a
def box(a,x,y,w,h,title,body):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='white',edgecolor=GRID,lw=1.5));a.text(x+20,y+35,title,color=BLUE,fontsize=18,weight='bold');a.text(x+20,y+65,body,color=INK,fontsize=16,va='top',linespacing=1.5)
def foot(a,take,source,note):
 a.plot([44,1156],[540,540],color=GRID);a.text(44,577,take,color=INK,fontsize=18,weight='bold');a.text(44,615,source,color=MUTED,fontsize=12);a.text(44,645,note,color=MUTED,fontsize=12)
def save(f,name):
 for ext in ['png','svg']:f.savefig(OUT/('2026-10-15-'+name+'.'+ext),dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f,a=base('AI / CALIBRATION','Correct forecast probabilities, not just averages','Probabilistic Bias Correction • Nature publication, October 14, 2026')
for x,t,b in [(44,'EXISTING FORECAST','Weather-model ensemble\nand historical forecasts'),(430,'LEARNED CORRECTION','Identify systematic bias\nin forecast probabilities'),(816,'FORECAST OUTPUT','Two-to-six-week weather\nguidance after correction')]:box(a,x,230,340,165,t,b)
for x in [388,774]:a.annotate('',xy=(x+32,315),xytext=(x,315),arrowprops=dict(arrowstyle='->',color=GOLD,lw=2))
a.text(600,461,'Financial-market transfer remains an untested research idea.',ha='center',fontsize=22,color=GOLD,weight='bold')
foot(a,'Evaluate calibration on held-out periods before changing decisions.','Sources: Microsoft Research; Nature, October 14, 2026. Graphic: Market State Lab.','Conceptual mechanism only; no accuracy curve, financial backtest or calibrated forecast is depicted.')
save(f,'story-1-probability-calibration')
f,a=base('QUANT / MARKET MAKING','Give the quoting policy a causal order-flow memory','Hawkes-Structured Networks • arXiv manuscript submitted October 12, 2026')
for x,t,b in [(44,'ORDER ARRIVALS','Clustered, self-exciting\nflow with persistent history'),(430,'EXPONENTIAL MEMORY','Learnable mixture of\nweighted history filters'),(816,'RL QUOTING POLICY','Jointly learn features\nand quote decisions')]:box(a,x,230,340,165,t,b)
for x in [388,774]:a.annotate('',xy=(x+32,315),xytext=(x,315),arrowprops=dict(arrowstyle='->',color=GOLD,lw=2))
a.text(600,461,'Controlled experiments do not establish live trading profits.',ha='center',fontsize=23,color=GOLD,weight='bold')
foot(a,'Compare flow-memory features with a frozen bar-only baseline.','Source: Acero, Plank & Zhang, arXiv:2610.16524v1. Graphic: Market State Lab.','Conceptual architecture; manuscript marked accepted to ACM ICAIF 2026; no measured return is shown.')
save(f,'story-2-hawkes-memory')
f,a=base('U.S. MARKETS','Nasdaq futures lead the premarket decline','October 15, 2026, 4:50 a.m. CT • reported indicative percentage changes')
z=f.add_axes([.24,.31,.63,.36],facecolor=BG);vals=[.32,-.27,-1.10];names=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini']
z.barh([2,1,0],vals,color=[BLUE,GOLD,GOLD],height=.48);z.axvline(0,color=INK,lw=1);z.set(xlim=(-1.45,.60),yticks=[2,1,0],yticklabels=names,xticks=[-1.25,-1,-.75,-.5,-.25,0,.25,.5]);z.set_xticklabels(['−1.25%','−1.0%','−0.75%','−0.5%','−0.25%','0','+0.25%','+0.5%']);z.tick_params(labelsize=12,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for y,v in zip([2,1,0],vals):z.text(v+(.05 if v>=0 else -.05),y,f'{v:+.2f}%',va='center',ha='left' if v>=0 else 'right',fontsize=19,weight='bold',color=INK)
foot(a,'Check index divergence, then refresh liquidity around the data.','Source: Reuters, October 15, 2026, 5:50 a.m. ET. Graphic: Market State Lab.','Futures changes are not cash-index returns, executable quotes, spreads or order-book depth.')
save(f,'story-3-nasdaq-divergence')
f,a=base('ECONOMY / INFLATION','September CPI: separate monthly and annual rates','BLS release, October 14, 2026 • headline versus excluding food and energy')
for rect,vals,cap,ylim,ticks in [([.10,.32,.34,.35],[.6,.3],'Month over month, SA',.8,[0,.2,.4,.6,.8]),([.58,.32,.34,.35],[3.7,2.6],'Year over year, NSA',4.5,[0,1,2,3,4])]:
 z=f.add_axes(rect,facecolor=BG);z.bar([0,1],vals,width=.52,color=[GOLD,BLUE]);z.set(ylim=(0,ylim),yticks=ticks,xticks=[0,1],xticklabels=['Headline','Core']);z.set_ylabel('Percent',fontsize=13);z.set_title(cap,fontsize=16,color=INK,pad=22);z.tick_params(labelsize=13,length=0,pad=8);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
 for x,v in enumerate(vals):z.text(x,v+ylim*.035,f'{v:.1f}%',ha='center',fontsize=20,weight='bold',color=INK)
foot(a,'One inflation print does not determine the Federal Reserve path.','Source: U.S. Bureau of Labor Statistics, September 2026 CPI. Graphic: Market State Lab.','Both axes start at zero; panels use different scales. SA: seasonally adjusted. NSA: not seasonally adjusted.')
save(f,'story-4-september-cpi')
f,a=base('TECHNOLOGY / BUSINESS','TSMC: reported revenue and forward guidance','October 15, 2026 results • revenue in billions of U.S. dollars')
z=f.add_axes([.14,.32,.72,.36],facecolor=BG);z.bar(0,46.72,width=.5,color=BLUE);z.bar(1,52.3,width=.5,color='none',edgecolor=GOLD,lw=2);z.bar(1,2,bottom=52.3,width=.5,color=GOLD,alpha=.4)
z.set(ylim=(0,65),yticks=[0,10,20,30,40,50,60],xticks=[0,1],xticklabels=['Q3 2026 reported','Q4 2026 guidance']);z.set_ylabel('Revenue (US$ billions)',fontsize=13);z.tick_params(labelsize=14,length=0,pad=10);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
z.text(0,49,'46.72',ha='center',fontsize=22,weight='bold',color=INK);z.text(1,57,'52.3–54.3',ha='center',fontsize=22,weight='bold',color=GOLD)
foot(a,'Track capacity, margins and cash generation alongside demand.','Source: TSMC Q3 2026 earnings release, October 15, 2026. Graphic: Market State Lab.','Zero-based scale; hollow Q4 bar is guidance, not revenue earned. Shaded top band shows guidance range.')
save(f,'story-5-tsmc-guidance')
f=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(627,0));a.axis('off')
for x,y,t,size,col in [(60,73,'MARKET STATE LAB',19,'#64C1DF'),(60,160,'Quant Market Brief',38,'white'),(60,216,'OCTOBER 15, 2026',20,'#B8CDDC'),(60,335,'Post-CPI execution',37,'white'),(60,402,'& TSMC guidance',37,'white'),(60,489,'Forecast calibration • Order-flow memory • Index divergence',18,'#B8CDDC'),(60,582,'Five developments. Practical quant and MATLAB implications.',17,'#64C1DF')]:a.text(x,y,t,fontsize=size,color=col,weight='bold' if y in [73,160,335,402] else 'normal')
save(f,'linkedin-cover')
