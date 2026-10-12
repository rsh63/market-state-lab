"""Dated QMB graphics. Source URLs and inputs are retained in sources.json."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
OUT=Path(__file__).parent
NAVY='#0B2237'; INK='#162B3D'; BLUE='#087CAB'; GOLD='#C98017'; MUTED='#536577'; BG='#F7F9FB'; GRID='#D9E1E7'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
def base(cat,title,sub):
 f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=BG); a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(675,0));a.axis('off')
 a.add_patch(Rectangle((0,0),1200,68,color=NAVY));a.text(44,42,'MARKET STATE LAB / '+cat,color='white',fontsize=15,weight='bold');a.text(1156,42,'12 OCT 2026',ha='right',color='#ABD6E6',fontsize=13)
 a.text(44,120,title,color=INK,fontsize=26,weight='bold');a.text(44,160,sub,color=MUTED,fontsize=15)
 return f,a
def box(a,x,y,w,h,title,body):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='white',edgecolor=GRID,lw=1.5));a.text(x+20,y+35,title,color=BLUE,fontsize=18,weight='bold');a.text(x+20,y+65,body,color=INK,fontsize=16,va='top',linespacing=1.5)
def foot(a,take,source,note):
 a.plot([44,1156],[540,540],color=GRID);a.text(44,577,take,color=INK,fontsize=18,weight='bold');a.text(44,615,source,color=MUTED,fontsize=12);a.text(44,645,note,color=MUTED,fontsize=12)
def save(f,name):
 for ext in ['png','svg']:f.savefig(OUT/('2026-10-12-'+name+'.'+ext),dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f,a=base('AI / ENTERPRISE','HCLTech–Anthropic enterprise AI partnership','Announced October 12: dedicated business unit and centre of excellence')
box(a,44,220,520,160,'HCLTech','Industry solutions\nEnterprise integration');box(a,636,220,520,160,'Anthropic','Claude, Cowork and Claude Code\nAI products for deployment')
a.add_patch(FancyArrowPatch((574,298),(626,298),arrowstyle='<->',mutation_scale=20,color=GOLD,lw=2));a.text(600,454,'Deployment priorities: safety • cybersecurity • governance',ha='center',fontsize=22,color=INK)
foot(a,'Evaluate controls and task outcomes before expanding agent permissions.','Source: Reuters, October 12, 2026. Graphic: Market State Lab.','Conceptual partnership map; no performance or revenue forecast.')
save(f,'story-1-enterprise-ai')
f,a=base('QUANT / OPTIONS','Supervised initialization before RL fine-tuning','SPX short-straddle exit research • submitted October 9, 2026')
for x,title,body in [(44,'TRAIN','Historical episodes\nOffline exit labels'),(430,'INITIALIZE','Supervised MLP\nHold / exit policy'),(816,'FINE-TUNE','Risk-aware RL\nCompare to MLP')]:box(a,x,225,340,153,title,body)
for x in [384,770]:a.add_patch(FancyArrowPatch((x+6,300),(x+36,300),arrowstyle='->',mutation_scale=18,color=GOLD,lw=2))
a.text(600,452,'Test inputs must contain only information available at the time.',ha='center',color=INK,fontsize=21)
foot(a,'The incremental RL advantage requires a fair baseline comparison.','Source: Wang, Ślepaczuk & Sakowski, arXiv:2610.13126v1. Graphic: Market State Lab.','Conceptual method diagram; no performance guarantee. Severe crisis regimes remain untested.')
save(f,'story-2-options-exits')
f,a=base('U.S. MARKETS','U.S. equity futures: mixed early indications','October 12, 2026, 4:36 a.m. CT • reported percentage changes')
z=f.add_axes([.22,.31,.65,.36],facecolor=BG);vals=[.08,.12,-.05];names=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini']
z.barh([2,1,0],vals,color=BLUE,height=.48);z.axvline(0,color=INK,lw=1);z.set(xlim=(-.10,.16),yticks=[2,1,0],yticklabels=names,xticks=[-.10,-.05,0,.05,.10,.15]);z.set_xticklabels(['−0.10%','−0.05%','0','+0.05%','+0.10%','+0.15%']);z.tick_params(labelsize=13,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for y,v in zip([2,1,0],vals):z.text(v+(.006 if v>=0 else -.006),y,f'{v:+.2f}%',va='center',ha='left' if v>=0 else 'right',fontsize=19,weight='bold',color=INK)
foot(a,'Small price moves do not establish deep or executable liquidity.','Source: Reuters, October 12, 2026, 05:36 a.m. ET snapshot. Graphic: Market State Lab.','Indicative reported futures changes; not live quotes or cash-index returns.')
save(f,'story-3-futures')
f,a=base('ECONOMY / FED','U.S. inflation releases this week','September 2026 reference period • all times Central Daylight Time')
for x,title,body in [(44,'WED • OCT 14','CPI and real earnings\n7:30 a.m. CT'),(430,'THU • OCT 15','Producer Price Index\n7:30 a.m. CT'),(816,'FRI • OCT 16','Import / export prices\n7:30 a.m. CT')]:box(a,x,230,340,160,title,body)
a.text(600,458,'Scheduled releases — results are not yet available',ha='center',color=GOLD,fontsize=24,weight='bold')
foot(a,'Keep release surprises separate from forecasts and prior observations.','Source: U.S. Bureau of Labor Statistics, 2026 release calendar; checked October 12.','8:30 a.m. Eastern = 7:30 a.m. Central. Graphic: Market State Lab.')
save(f,'story-4-inflation-calendar')
f,a=base('TECHNOLOGY / BUSINESS','Tencent’s proposed bond financing','Reported October 12, 2026 • offering size and completion not final')
box(a,44,218,520,173,'U.S. DOLLAR TRANCHES','Proposed maturities\n10 years and 20 years');box(a,636,218,520,173,'OFFSHORE YUAN TRANCHES','Proposed maturities\n10 years and 30 years')
a.text(600,456,'Reported fundraising target: at least US$4.5 billion',ha='center',fontsize=23,color=INK,weight='bold')
foot(a,'Monitor pricing, maturity mix and cash-flow coverage when terms emerge.','Source: Reuters, October 12, 2026, citing a source and term sheet. Market State Lab.','Proposed terms, not completed issuance; final company deal size was not set.')
save(f,'story-5-tencent-financing')
f=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(627,0));a.axis('off')
for x,y,t,size,col in [(60,73,'MARKET STATE LAB',19,'#64C1DF'),(60,160,'Quant Market Brief',38,'white'),(60,216,'OCTOBER 12, 2026',20,'#B8CDDC'),(60,335,'Options exits',37,'white'),(60,402,'& inflation-week execution',34,'white'),(60,481,'Enterprise AI • Holiday liquidity • Financing risk',20,'#B8CDDC'),(60,569,'Five developments. Practical quant and MATLAB implications.',18,'#64C1DF')]:a.text(x,y,t,fontsize=size,color=col,weight='bold' if y in [73,160,335,402] else 'normal')
save(f,'linkedin-cover')
