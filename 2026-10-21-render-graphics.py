from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

P=Path(__file__).parent; D='2026-10-21'
NAVY='#0D2638'; BLUE='#197D96'; GOLD='#BE8C35'; INK='#233746'; GRAY='#586976'; BG='#F7F9FB'; OPEN='#DCEBF0'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'axes.labelcolor':INK,'xtick.color':GRAY,'ytick.color':INK,'svg.fonttype':'none'})

def page(title,subtitle,caption):
    f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG)
    f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY))
    f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold')
    f.text(.96,.947,'21 OCT 2026',color='#B7D1DF',fontsize=14,ha='right')
    f.text(.04,.84,title,fontsize=25,weight='bold')
    f.text(.04,.775,subtitle,fontsize=16,color=GRAY)
    f.text(.04,.055,caption,fontsize=13.5,color=GRAY,linespacing=1.45)
    return f
def box(f,x,y,w,h,title,body,color=BLUE):
    f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF',lw=1.3))
    f.text(x+.018,y+h-.045,title,color=color,weight='bold',fontsize=18,va='top')
    f.text(x+.018,y+h-.115,body,fontsize=17,va='top',linespacing=1.45)
def arrow(f,start,end): f.patches.append(FancyArrowPatch(start,end,transform=f.transFigure,arrowstyle='->',mutation_scale=18,color=GRAY))
def save(f,name):
    for ext in ['png','svg']: f.savefig(P/f'{name}.{ext}',dpi=100,facecolor=f.get_facecolor())
    plt.close(f)

# 1 — conceptual optimizer map; no invented performance curve.
f=page('Hybrid Momentum: two gradient timescales','October 20, 2026 preprint • Conceptual mechanism, not a performance forecast','Source: Xu et al., arXiv:2610.27674v1, submitted Oct 20, 2026.\nReported validation results are author experiments; independent replication is pending.')
box(f,.05,.35,.36,.33,'LONGER MEMORY','Linearly weighted\npast gradients\nGrowing history span')
box(f,.59,.35,.36,.33,'FAST RESPONSE','Geometric / EMA\nrecent gradients\nFixed short timescale',GOLD)
arrow(f,(.41,.515),(.49,.515)); arrow(f,(.59,.515),(.51,.515))
box(f,.37,.20,.26,.11,'HYBRID UPDATE','',BLUE)
f.text(.05,.145,'Test matched compute, seeds and schedules before attributing gains\nto the optimizer.',fontsize=17,weight='bold',linespacing=1.3)
save(f,f'{D}-story-1-hybrid-momentum-training')

# 2 — quantitative interval from abstract with square-root reference.
f=page('LOB-Impact benchmark: measured impact exponents','Five autoregressive generators × five Nasdaq stocks • Preprint / ICAIF 2026','Source: Nigmatulin et al., arXiv:2610.27100v1; surfaced Oct 21, 2026.\nReported range across tested model–stock pairs. No impact decay observed in the tested relaxation windows.')
a=f.add_axes([.16,.33,.76,.28]); a.set_xlim(.35,1.3); a.set_ylim(-.7,.7); a.set_yticks([]); a.set_xlabel('Impact-law exponent')
a.axvline(.5,color=GOLD,lw=2,linestyle='--'); a.text(.5,.5,'Traditional square-root reference 0.50',rotation=90,va='top',ha='right',color=GOLD,fontsize=14)
a.plot([.63,1.21],[0,0],color=BLUE,lw=14,solid_capstyle='round'); a.scatter([.63,1.21],[0,0],s=150,color=NAVY,zorder=3)
a.text(.63,.18,'0.63',ha='center',weight='bold'); a.text(1.21,.18,'1.21',ha='center',weight='bold'); a.grid(axis='x',color='#E0E5E9'); a.spines[['top','right','left']].set_visible(False)
f.text(.06,.19,'Benchmark isolates learned response with visible versus blind\nmetaorder injections.',fontsize=17,weight='bold',linespacing=1.3)
save(f,f'{D}-story-2-lob-impact-benchmark')

# 3 — market rotation bars.
f=page('October 20 close: rotation away from megacap growth','Completed-session index / style changes (%) • Not October 21 cash performance','Source: Reuters / LSEG, Oct 20, 2026 final-close report.\nValue/growth are S&P 500 style indexes; Russell 2000 is a small-cap index.')
a=f.add_axes([.27,.28,.66,.42]); names=['Dow','S&P 500','Nasdaq','Russell 2000','S&P value','S&P growth']; vals=[1.02,.28,-.02,1.70,.90,-.20]
colors=[BLUE if v>=0 else OPEN for v in vals]; a.barh(names,vals,color=colors,edgecolor=NAVY,height=.56); a.invert_yaxis(); a.axvline(0,color=NAVY,lw=1.2); a.set_xlim(-.55,1.95); a.set_xlabel('Daily change (%)'); a.grid(axis='x',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals): a.text(v+.05 if v>=0 else v-.05,i,f'{v:+.2f}%',va='center',ha='left' if v>=0 else 'right',fontsize=17,weight='bold')
f.text(.05,.16,'Small caps and value led; technology and growth lagged.',fontsize=19,weight='bold')
save(f,f'{D}-story-3-october-20-rotation')

# 4 — official housing changes with uncertainty note.
f=page('September residential construction: mixed directions','Month-over-month change (%) • Seasonally adjusted annual rates • Released Oct 20','Source: U.S. Census Bureau, New Residential Construction, Sept 2026.\nAsterisks in the release indicate estimates not statistically different from zero at the stated level.')
a=f.add_axes([.24,.30,.68,.40]); names=['Permits','Housing starts','Completions','Single-family starts']; vals=[-.2,-5.2,2.2,-4.6]
a.barh(names,vals,color=[OPEN if v<0 else BLUE for v in vals],edgecolor=NAVY,height=.56); a.invert_yaxis(); a.axvline(0,color=NAVY,lw=1.2); a.set_xlim(-7,4); a.set_xlabel('Monthly change (%)'); a.grid(axis='x',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals): a.text(v+.25 if v>=0 else v-.25,i,f'{v:+.1f}%',va='center',ha='left' if v>=0 else 'right',fontsize=18,weight='bold')
f.text(.05,.16,'Starts 1.221m SAAR • Permits 1.400m • Completions 1.192m',fontsize=19,weight='bold')
save(f,f'{D}-story-4-september-housing-construction')

# 5 — reported process map, clearly conditional.
f=page('SpaceX–Tesla: formal talks, no agreed transaction','Reuters report October 20, 2026 • Deal outcome remains uncertain','Source: Reuters, Oct 20, 2026. Reported talks and committees; no terms agreed.\nShareholders would ultimately need to approve a transaction; committees may never reach a deal.')
box(f,.05,.36,.34,.30,'SPACEX COMMITTEE','Independent directors\nReview potential terms')
box(f,.61,.36,.34,.30,'TESLA COMMITTEE','Independent directors\nReview potential terms',GOLD)
arrow(f,(.39,.51),(.61,.51)); arrow(f,(.61,.45),(.39,.45))
box(f,.35,.21,.30,.12,'NO AGREED DEAL','',NAVY)
f.text(.05,.14,'Do not treat “a good idea” as an announced merger\nor completed transaction.',fontsize=17,weight='bold',linespacing=1.3)
save(f,f'{D}-story-5-spacex-tesla-talks')

f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold'); f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold'); f.text(.05,.63,'OCTOBER 21, 2026',fontsize=20,color='#B8C8D2')
f.text(.05,.40,'Hybrid momentum\n& market impact',fontsize=38,color='white',weight='bold',linespacing=1.3)
f.text(.05,.18,'Optimizer memory • LOB realism • Value rotation',fontsize=19,color='#B8C8D2'); f.text(.05,.08,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2')
save(f,f'{D}-linkedin-cover')
print('Rendered five story graphics and dated cover.')
