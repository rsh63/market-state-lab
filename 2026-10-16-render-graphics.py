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
 a.add_patch(Rectangle((0,0),1200,68,color=NAVY));a.text(44,42,'MARKET STATE LAB / '+cat,color='white',fontsize=15,weight='bold');a.text(1156,42,'16 OCT 2026',ha='right',color='#ABD6E6',fontsize=13)
 a.text(44,120,title,color=INK,fontsize=26,weight='bold');a.text(44,160,sub,color=MUTED,fontsize=15)
 return f,a
def box(a,x,y,w,h,title,body):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='white',edgecolor=GRID,lw=1.5));a.text(x+20,y+35,title,color=BLUE,fontsize=18,weight='bold');a.text(x+20,y+65,body,color=INK,fontsize=16,va='top',linespacing=1.5)
def foot(a,take,source,note):
 a.plot([44,1156],[540,540],color=GRID);a.text(44,577,take,color=INK,fontsize=18,weight='bold');a.text(44,615,source,color=MUTED,fontsize=12);a.text(44,645,note,color=MUTED,fontsize=12)
def save(f,name):
 for ext in ['png','svg']:f.savefig(OUT/('2026-10-16-'+name+'.'+ext),dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f,a=base('AI / AGENT GOVERNANCE','TaskVM: make state and recovery explicit','Research preprint submitted October 14, 2026 • conceptual framework')
for x,t,b in [(44,'TASK CONTRACT','Desired outcomes\nFacts to preserve'),(430,'STATE VERIFICATION','Observe application state\nVerify outcomes independently'),(816,'ACTION RECOVERY','Reversible / compensatable\n/ irreversible classification')]:box(a,x,230,340,165,t,b)
for x in [388,774]:a.annotate('',xy=(x+32,315),xytext=(x,315),arrowprops=dict(arrowstyle='->',color=GOLD,lw=2))
a.text(600,461,'Interface-governance evidence is not a trading-safety guarantee.',ha='center',fontsize=22,color=GOLD,weight='bold')
foot(a,'Define invariants and recovery paths before giving agents tools.','Source: Yang et al., arXiv:2610.20100v1, October 14, 2026. Market State Lab.','Conceptual mechanism; version 1 is under refinement. No measured financial outcome is depicted.')
save(f,'story-1-taskvm-recovery')
f,a=base('QUANT / REPLAY INTEGRITY','Six backtest/live mismatches from one system','Research preprint submitted October 15, 2026 • authors report one intraday equity system')
for x,t,b in [(44,'DATA — 3 DEFECTS','Opening-volume feed\nDividend-adjusted prices\nAsymmetric downloads'),(430,'CODE — 2 DEFECTS','Sizing-limit mismatch\nUTC / New York confusion'),(816,'CONFIG — 1 DEFECT','Settings enabled but\nnot reaching order code')]:box(a,x,230,340,185,t,b)
a.text(600,477,'The paper makes no claim about strategy profitability.',ha='center',fontsize=23,color=GOLD,weight='bold')
foot(a,'Compare event-level decisions before summary performance.','Source: Vidovich & Zerjal, arXiv:2610.21846v1, October 15, 2026. Market State Lab.','Conceptual defect map from a single case; not a prevalence survey or a performance benchmark.')
save(f,'story-2-backtest-live-parity')
f,a=base('U.S. MARKETS','U.S. equity futures before monthly expiry','October 16, 2026, 5:21 a.m. CT • reported indicative percentage changes')
z=f.add_axes([.24,.31,.63,.36],facecolor=BG);vals=[.39,.16,-.08];names=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini']
z.barh([2,1,0],vals,color=[BLUE,BLUE,GOLD],height=.48);z.axvline(0,color=INK,lw=1);z.set(xlim=(-.22,.59),yticks=[2,1,0],yticklabels=names,xticks=[-.2,-.1,0,.1,.2,.3,.4,.5]);z.set_xticklabels(['−0.2%','−0.1%','0','+0.1%','+0.2%','+0.3%','+0.4%','+0.5%']);z.tick_params(labelsize=13,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for y,v in zip([2,1,0],vals):z.text(v+(.025 if v>=0 else -.025),y,f'{v:+.2f}%',va='center',ha='left' if v>=0 else 'right',fontsize=19,weight='bold',color=INK)
foot(a,'A positive broad-index indication can coexist with tech weakness.','Source: Reuters, October 16, 2026, 6:21 a.m. ET snapshot. Market State Lab.','Reported futures changes are not cash returns, executable quotes, spreads or order-book depth.')
save(f,'story-3-expiry-futures')
f,a=base('ECONOMY / PRODUCER PRICES','September PPI: final-demand price changes','BLS release, October 15, 2026 • month-over-month percent, seasonally adjusted')
z=f.add_axes([.10,.32,.82,.36],facecolor=BG);vals=[1.3,2.6,.8,.5];z.bar(range(4),vals,width=.55,color=[GOLD,BLUE,BLUE,BLUE]);z.set(ylim=(0,3.2),yticks=[0,1,2,3],xticks=range(4),xticklabels=['Final demand','Goods','Services','Less food, energy\nand trade services']);z.set_ylabel('Monthly change (%)',fontsize=13);z.tick_params(labelsize=13,length=0,pad=10);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for x,v in enumerate(vals):z.text(x,v+.12,f'{v:.1f}%',ha='center',fontsize=21,weight='bold',color=INK)
foot(a,'Separate energy, service margins and underlying price pressure.','Source: U.S. Bureau of Labor Statistics, September 2026 PPI. Market State Lab.','Zero-based scale. These overlapping indexes are not additive contributions; PPI is not CPI or PCE.')
save(f,'story-4-september-ppi')
f,a=base('TECHNOLOGY / BUSINESS','Proofpoint–Varonis: acquisition terms','Definitive agreement announced October 15, 2026 • transaction has not closed')
for x,t,b in [(44,'TRANSACTION VALUE','Approximately $6.3 billion\nAll-cash transaction'),(430,'CASH PER SHARE','$49.75 per Varonis share\nin cash at completion'),(816,'EXPECTED CLOSING','First half of 2027\nShareholder / regulatory gates')]:box(a,x,230,340,165,t,b)
a.text(600,461,'Completion and integration remain uncertain.',ha='center',fontsize=21,color=GOLD,weight='bold')
foot(a,'Treat deal terms, closing risk and operating synergies separately.','Source: Varonis SEC Form 8-K, Exhibit 99.1, October 15, 2026. Market State Lab.','Announced terms and management timing expectation; companies remain independent until closing.')
save(f,'story-5-proofpoint-varonis')
f=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(627,0));a.axis('off')
for x,y,t,size,col in [(60,73,'MARKET STATE LAB',19,'#64C1DF'),(60,160,'Quant Market Brief',38,'white'),(60,216,'OCTOBER 16, 2026',20,'#B8CDDC'),(60,335,'Expiry execution',37,'white'),(60,402,'& backtest integrity',37,'white'),(60,489,'Agent recovery • Producer prices • Data-security deal',19,'#B8CDDC'),(60,582,'Five developments. Practical quant and MATLAB implications.',17,'#64C1DF')]:a.text(x,y,t,fontsize=size,color=col,weight='bold' if y in [73,160,335,402] else 'normal')
save(f,'linkedin-cover')
