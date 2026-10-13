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
 a.add_patch(Rectangle((0,0),1200,68,color=NAVY));a.text(44,42,'MARKET STATE LAB / '+cat,color='white',fontsize=15,weight='bold');a.text(1156,42,'13 OCT 2026',ha='right',color='#ABD6E6',fontsize=13)
 a.text(44,120,title,color=INK,fontsize=26,weight='bold');a.text(44,160,sub,color=MUTED,fontsize=15)
 return f,a
def box(a,x,y,w,h,title,body):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='white',edgecolor=GRID,lw=1.5));a.text(x+20,y+35,title,color=BLUE,fontsize=18,weight='bold');a.text(x+20,y+65,body,color=INK,fontsize=16,va='top',linespacing=1.5)
def foot(a,take,source,note):
 a.plot([44,1156],[540,540],color=GRID);a.text(44,577,take,color=INK,fontsize=18,weight='bold');a.text(44,615,source,color=MUTED,fontsize=12);a.text(44,645,note,color=MUTED,fontsize=12)
def save(f,name):
 for ext in ['png','svg']:f.savefig(OUT/('2026-10-13-'+name+'.'+ext),dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f,a=base('AI / SAFEGUARDS','AI replication research: what was actually tested','Anthropic research published October 12, 2026 • controlled evaluations')
for x,t,b in [(44,'HARDWARE SETUP','A 9B model established\ninference on 8 of 9 types'),(430,'SIMPLIFIED NETWORK','Stronger models completed\na contained replication task'),(816,'REAL-WORLD LIMIT','Trivial access step;\nnot a full rogue replicator')]:box(a,x,230,340,160,t,b)
a.text(600,455,'Capability evidence ≠ demonstrated real-world outbreak',ha='center',fontsize=23,color=GOLD,weight='bold')
foot(a,'Constrain agent permissions and test recovery independently.','Source: Anthropic Frontier Red Team, October 12, 2026. Graphic: Market State Lab.','Conceptual evidence panel; controlled tests and projections do not establish an active outbreak.')
save(f,'story-1-ai-replication')
f,a=base('QUANT / EXECUTION','Market impact is a counterfactual question','Thumm & Chen • arXiv preprint submitted October 8, 2026')
box(a,44,220,520,170,'OBSERVED TAPE','Trading flow + information\nBoth can move prices')
box(a,636,220,520,170,'COUNTERFACTUAL TEST','Price with the order\nversus price without it')
a.add_patch(FancyArrowPatch((574,305),(626,305),arrowstyle='->',mutation_scale=20,color=GOLD,lw=2))
a.text(600,465,'Synthetic causal priors supply the identifying assumptions.',ha='center',fontsize=21,color=INK)
foot(a,'Audit event labels and recalibrate before using estimated costs.','Source: Thumm & Chen, arXiv:2610.12537v1. Graphic: Market State Lab.','Conceptual mechanism; proof of concept. Real-market causal transfer is not proven.')
save(f,'story-2-causal-impact')
f,a=base('U.S. MARKETS','Nasdaq futures lag the Dow before the open','October 13, 2026, 5:54 a.m. CT • indicative percentage changes')
z=f.add_axes([.22,.31,.65,.36],facecolor=BG);vals=[.18,-.13,-.59];names=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini']
z.barh([2,1,0],vals,color=BLUE,height=.48);z.axvline(0,color=INK,lw=1);z.set(xlim=(-.8,.4),yticks=[2,1,0],yticklabels=names,xticks=[-.8,-.6,-.4,-.2,0,.2,.4]);z.set_xticklabels(['−0.8%','−0.6%','−0.4%','−0.2%','0','+0.2%','+0.4%']);z.tick_params(labelsize=13,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for y,v in zip([2,1,0],vals):z.text(v+(.025 if v>=0 else -.025),y,f'{v:+.2f}%',va='center',ha='left' if v>=0 else 'right',fontsize=19,weight='bold',color=INK)
foot(a,'Index divergence is a signal to investigate, not evidence of depth.','Source: Reuters, October 13, 2026, 6:54 a.m. ET snapshot. Graphic: Market State Lab.','Reported indicative futures changes; not live executable quotes or cash-index returns.')
save(f,'story-3-futures')
f,a=base('ECONOMY / FED','Hammack’s conditional policy reaction','October 12 speech • one policymaker’s assessment, not an FOMC decision')
for x,t,b in [(44,'INFLATION','Broad price pressures\nAbove the 2% objective'),(430,'LABOR MARKET','Stable backdrop\nIn her assessment'),(816,'CONDITIONS','Financial conditions\nNeutral, in her assessment')]:box(a,x,230,340,160,t,b)
a.text(600,456,'Supports restrictive policy, conditional on incoming evidence',ha='center',fontsize=22,color=GOLD,weight='bold')
foot(a,'Separate a reaction function from a committed rate path.','Source: Cleveland Fed, “Trimming the Sails,” October 12, 2026. Market State Lab.','Conceptual summary; smaller, quicker adjustments are her preference when feasible.')
save(f,'story-4-hammack-policy')
f,a=base('TECHNOLOGY / BUSINESS','Microsoft’s Maia inference roadmap','Company announcement, October 12, 2026 • deployment plans are conditional')
box(a,44,218,520,173,'MAIA 200 • IN PRODUCTION','Serving Microsoft workloads\nExperience informs next system')
box(a,636,218,520,173,'MAIA 300 • PLANNED 2027','96 accelerators per rack\n167 kW power envelope')
a.add_patch(FancyArrowPatch((574,305),(626,305),arrowstyle='->',mutation_scale=20,color=GOLD,lw=2))
a.text(600,463,'Planned multi-gigawatt scale starting in 2027',ha='center',fontsize=24,color=INK,weight='bold')
foot(a,'Measure workload-level efficiency, cost and software portability.','Source: Official Microsoft Blog, October 12, 2026. Graphic: Market State Lab.','Company-reported specifications and roadmap; no independent performance comparison shown.')
save(f,'story-5-maia-roadmap')
f=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(627,0));a.axis('off')
for x,y,t,size,col in [(60,73,'MARKET STATE LAB',19,'#64C1DF'),(60,160,'Quant Market Brief',38,'white'),(60,216,'OCTOBER 13, 2026',20,'#B8CDDC'),(60,335,'Causal market impact',37,'white'),(60,402,'& chip-sector divergence',37,'white'),(60,489,'AI safeguards • Fed reaction • Inference economics',19,'#B8CDDC'),(60,582,'Five developments. Practical quant and MATLAB implications.',17,'#64C1DF')]:a.text(x,y,t,fontsize=size,color=col,weight='bold' if y in [73,160,335,402] else 'normal')
save(f,'linkedin-cover')
