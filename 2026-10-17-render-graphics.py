from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
OUT=Path(__file__).parent
NAVY='#0B2237'; INK='#162B3D'; BLUE='#087CAB'; GOLD='#C98017'; MUTED='#536577'; BG='#F7F9FB'; GRID='#D9E1E7'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
def base(cat,title,sub):
 f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=BG);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(675,0));a.axis('off')
 a.add_patch(Rectangle((0,0),1200,68,color=NAVY));a.text(44,42,'MARKET STATE LAB / '+cat,color='white',fontsize=15,weight='bold');a.text(1156,42,'17 OCT 2026',ha='right',color='#ABD6E6',fontsize=13)
 a.text(44,120,title,color=INK,fontsize=26,weight='bold');a.text(44,160,sub,color=MUTED,fontsize=15)
 return f,a
def box(a,x,y,w,h,title,body):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='white',edgecolor=GRID,lw=1.5));a.text(x+20,y+35,title,color=BLUE,fontsize=18,weight='bold');a.text(x+20,y+72,body,color=INK,fontsize=17,va='top',linespacing=1.5)
def foot(a,take,source,note):
 a.plot([44,1156],[540,540],color=GRID);a.text(44,577,take,color=INK,fontsize=18,weight='bold');a.text(44,615,source,color=MUTED,fontsize=12);a.text(44,645,note,color=MUTED,fontsize=12)
def save(f,name):
 for ext in ['png','svg']:f.savefig(OUT/('2026-10-17-'+name+'.'+ext),dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
# Graphic contracts: exact static newsletter exports; blue/gold plus neutrals;
# no decorative quantitative curves; zero baselines for both bar charts.
f,a=base('AI / OPEN WEIGHTS','Muse Spark Open: model specifications','Meta release, October 15, 2026 • company-reported architecture and context capacity')
for x,t,b in [(44,'TOTAL PARAMETERS','816 billion\nAcross the full model'),(430,'ACTIVE PARAMETERS','42 billion\nActive per token'),(816,'CONTEXT WINDOW','1 million tokens\nReported context capacity')]:box(a,x,230,340,170,t,b)
a.text(600,470,'Active compute size does not equal total weight-memory needs.',ha='center',fontsize=21,color=GOLD,weight='bold')
foot(a,'Test memory, latency, permissions and license terms before rollout.','Source: Meta AI Research, Muse Spark Open announcement, October 15, 2026. Market State Lab.','Different measures, not additive. Open weights use the Muse Model License with limited commercial terms.')
save(f,'story-1-muse-spark-open')
f,a=base('QUANT / INFORMATION CLOCKS','Earnings-call benchmarks: input availability','Ma et al., October 15, 2026 • conceptual availability contract, not a calibrated timeline')
for x,t,b in [(44,'INPUT BOUNDARY','Text/audio included\nInput completion time'),(430,'AVAILABILITY PROOF','Evidence for completion\nAllow processing delay'),(816,'OUTCOME START','Start target after input\nis usable for a decision')]:box(a,x,225,340,178,t,b)
for x in [388,774]:a.annotate('',xy=(x+32,312),xytext=(x,312),arrowprops=dict(arrowstyle='->',color=GOLD,lw=2))
a.text(600,471,'9.4% of return signs changed in the authors’ baseline.',ha='center',fontsize=23,color=GOLD,weight='bold')
foot(a,'Chronological train/test splits do not fix within-event leakage.','Source: Ma et al., arXiv:2610.21659v1, October 15, 2026. Market State Lab.','552 calls / 24 firms; call-start vs completion proxy, fixed return endpoint. Timing evidence limits claims.')
save(f,'story-2-earnings-availability')
f,a=base('U.S. MARKETS','Friday U.S. index returns','October 16, 2026 cash-session close • percentage change from the preceding close')
z=f.add_axes([.27,.31,.62,.39],facecolor=BG);vals=[-.3,-1.1,-1.7,-2.1];names=['Dow industrials','S&P 500','Russell 2000','Nasdaq Composite'];ys=[3,2,1,0]
z.barh(ys,vals,color=BLUE,height=.48);z.axvline(0,color=INK,lw=1);z.set(xlim=(-2.7,.12),yticks=ys,yticklabels=names,xticks=[-2.5,-2,-1.5,-1,-.5,0]);z.set_xticklabels(['−2.5%','−2.0%','−1.5%','−1.0%','−0.5%','0']);z.tick_params(labelsize=14,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for y,v in zip(ys,vals):z.text(v-.06,y,f'{v:.1f}%',ha='right',va='center',fontsize=19,weight='bold',color=INK)
foot(a,'Closing returns describe the session; they do not show fillability.','Source: Associated Press, Friday October 16, 2026 closing summary. Market State Lab.','Reported changes rounded to one decimal. Cash indexes, not ETFs or futures; no weekend live quotes.')
save(f,'story-3-friday-index-declines')
f,a=base('ECONOMY / TRADE PRICES','September import and export price changes','BLS release, October 16, 2026 • month-over-month percent, not seasonally adjusted')
z=f.add_axes([.10,.32,.82,.36],facecolor=BG);vals=[1.1,4.8,.7,2.2];z.bar(range(4),vals,width=.55,color=BLUE);z.set(ylim=(0,5.8),yticks=[0,1,2,3,4,5],xticks=range(4),xticklabels=['All imports','Fuel imports','Nonfuel imports','All exports']);z.set_ylabel('Monthly change (%)',fontsize=13);z.tick_params(labelsize=14,length=0,pad=10);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for x,v in enumerate(vals):z.text(x,v+.16,f'+{v:.1f}%',ha='center',fontsize=21,weight='bold',color=INK)
foot(a,'Price pressure extends beyond fuel; isolate components in tests.','Source: U.S. Bureau of Labor Statistics, September 2026 MXP release. Market State Lab.','Zero-based scale. Overlapping categories are not additive contributions. Import prices are not CPI or PCE.')
save(f,'story-4-september-trade-prices')
f,a=base('BUSINESS / EARNINGS QUALITY','Travelers: diluted earnings per share','Third quarter, 2025 vs 2026 • dollars per diluted share; company-reported results')
z=f.add_axes([.13,.32,.77,.36],facecolor=BG);x=[0,1];v25=[8.24,8.14];v26=[9.04,9.18];z.bar([q-.17 for q in x],v25,width=.3,color='white',edgecolor=BLUE,lw=1.8,label='Q3 2025');z.bar([q+.17 for q in x],v26,width=.3,color=BLUE,edgecolor=BLUE,label='Q3 2026');z.set(ylim=(0,11.8),yticks=[0,3,6,9],xticks=x,xticklabels=['GAAP net income EPS','Core income EPS (non-GAAP)']);z.set_ylabel('Dollars per diluted share',fontsize=13);z.tick_params(labelsize=14,length=0,pad=10);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False);z.legend(loc='upper left',ncol=2,frameon=False,fontsize=13)
for xx,v in zip([-.17,.83],v25):z.text(xx,v+.2,f'${v:.2f}',ha='center',fontsize=17,color=INK)
for xx,v in zip([.17,1.17],v26):z.text(xx,v+.2,f'${v:.2f}',ha='center',fontsize=17,weight='bold',color=INK)
foot(a,'Core income grew 4%; core EPS grew 13%. Share count fell 7%.','Source: Travelers, Q3 2026 earnings release, October 16, 2026. Market State Lab.','Zero-based scale. Core EPS is company-defined non-GAAP. Buybacks affect per-share comparisons.')
save(f,'story-5-travelers-earnings')
f=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(627,0));a.axis('off')
for x,y,t,size,col in [(60,73,'MARKET STATE LAB',19,'#64C1DF'),(60,160,'Quant Market Brief',38,'white'),(60,216,'OCTOBER 17, 2026',20,'#B8CDDC'),(60,335,'Tech selloff',37,'white'),(60,402,'& information clocks',37,'white'),(60,489,'Open weights • Import prices • Earnings quality',19,'#B8CDDC'),(60,582,'Weekend edition. Friday data; practical quant implications.',17,'#64C1DF')]:a.text(x,y,t,fontsize=size,color=col,weight='bold' if y in [73,160,335,402] else 'normal')
save(f,'linkedin-cover')
