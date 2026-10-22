from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

P=Path(__file__).parent; D='2026-10-22'
NAVY='#0D2638'; BLUE='#197D96'; GOLD='#BE8C35'; INK='#233746'; GRAY='#586976'; BG='#F7F9FB'; OPEN='#DCEBF0'; NEG='#9A5E58'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'axes.labelcolor':INK,'xtick.color':GRAY,'ytick.color':INK,'svg.fonttype':'none'})

def page(title,subtitle,caption):
    f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG)
    f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY))
    f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold')
    f.text(.96,.947,'22 OCT 2026',color='#B7D1DF',fontsize=14,ha='right')
    f.text(.04,.84,title,fontsize=25,weight='bold')
    f.text(.04,.775,subtitle,fontsize=16,color=GRAY)
    f.text(.04,.055,caption,fontsize=13.5,color=GRAY,linespacing=1.45)
    return f
def box(f,x,y,w,h,title,body,color=BLUE):
    f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF',lw=1.3))
    f.text(x+.018,y+h-.045,title,color=color,weight='bold',fontsize=18,va='top')
    f.text(x+.018,y+h-.115,body,fontsize=17,va='top',linespacing=1.42)
def arrow(f,start,end): f.patches.append(FancyArrowPatch(start,end,transform=f.transFigure,arrowstyle='->',mutation_scale=18,color=GRAY))
def save(f,name):
    for ext in ['png','svg']: f.savefig(P/f'{name}.{ext}',dpi=100,facecolor=f.get_facecolor())
    plt.close(f)

# 1 — conceptual audit design; no synthetic coverage values.
f=page('Conformal coverage can break when inference changes','8 language models × 4 benchmarks × 12 inference configurations','Source: Doula & Mühlhäuser, arXiv:2610.28937v1, submitted Oct 20, 2026; accepted NeurIPS 2026.\nConceptual audit diagram. The paper reports heterogeneous coverage loss; no values are invented here.')
box(f,.05,.37,.36,.30,'CALIBRATION','Model weights fixed\nConfiguration A\nScore distribution A')
box(f,.59,.37,.36,.30,'DEPLOYMENT','Same weights / task\nConfiguration B\nScore distribution shifts',GOLD)
arrow(f,(.41,.52),(.59,.52))
box(f,.34,.19,.32,.12,'EXCHANGEABILITY RISK','',NAVY)
f.text(.05,.135,'Audit temperature, quantization and serving configuration as first-class axes.',fontsize=17,weight='bold')
save(f,f'{D}-story-1-conformal-inference-shift')

# 2 — reported R-squared plus conceptual world-model path.
f=page('A LOB foundation model encodes order-flow imbalance','8.2M-parameter Mamba-3 • eight large-cap U.S. equities','Source: Mohl et al., arXiv:2610.28753v1, submitted Oct 20, 2026; accepted ICAIF 2026.\nR² ≈ 0.59 is author-reported; steering and transfer require independent replication.')
a=f.add_axes([.13,.29,.31,.38]); a.barh(['Order-flow\nimbalance'],[.59],color=BLUE,edgecolor=NAVY,height=.42); a.set_xlim(0,1); a.set_xlabel('Reported decoder R²'); a.grid(axis='x',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False); a.text(.60,0,'0.59',va='center',weight='bold')
box(f,.56,.45,.37,.20,'INTERNAL STATE','Message-stream dynamics\ntransfer to unseen stocks',GOLD)
box(f,.56,.22,.37,.15,'STEERING TEST','Feature-axis intervention',BLUE)
arrow(f,(.745,.45),(.745,.37))
save(f,f'{D}-story-2-lob-foundation-model')

# 3 — Reuters premarket futures snapshot.
f=page('Premarket risk-off move is concentrated in Nasdaq','Reuters snapshot 4:56 a.m. ET • indicative futures, not cash returns','Source: Reuters/LSEG, Oct 22, 2026 at 4:56 a.m. ET.\nFutures were moving; bars do not represent executable ETF spreads, depth or the cash-open result.')
a=f.add_axes([.24,.29,.68,.42]); names=['Dow e-mini','S&P 500 e-mini','Nasdaq-100 e-mini']; vals=[-.69,-1.10,-1.93]
a.barh(names,vals,color=[OPEN,BLUE,NEG],edgecolor=NAVY,height=.56); a.invert_yaxis(); a.axvline(0,color=NAVY,lw=1.2); a.set_xlim(-2.25,.2); a.set_xlabel('Indicative change (%)'); a.grid(axis='x',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals): a.text(v-.06,i,f'{v:.2f}%',va='center',ha='right',fontsize=18,weight='bold')
f.text(.05,.16,'Brent +3% near $112 • 10-year yield around 5.085% • VIX 18.22 at 6:25 a.m. CT',fontsize=17,weight='bold')
save(f,f'{D}-story-3-premarket-risk-off')

# 4 — NAR regional pending sales.
f=page('September pending-home sales weaken in every region','Month-over-month change (%) • leading indicator based on signed contracts','Source: National Association of Realtors, released Oct 20, 2026.\nPending contracts generally lead closings by one to two months; revisions remain possible.')
a=f.add_axes([.25,.29,.67,.42]); names=['Northeast','Midwest','South','West','United States']; vals=[-4.2,-6.5,-8.2,-9.2,-7.3]
a.barh(names,vals,color=[OPEN,OPEN,BLUE,NEG,GOLD],edgecolor=NAVY,height=.55); a.invert_yaxis(); a.axvline(0,color=NAVY,lw=1.2); a.set_xlim(-10.5,.5); a.set_xlabel('September monthly change (%)'); a.grid(axis='x',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals): a.text(v-.2,i,f'{v:.1f}%',va='center',ha='right',fontsize=17,weight='bold')
f.text(.05,.16,'National pending sales were also 11.3% below September 2025.',fontsize=18,weight='bold')
save(f,f'{D}-story-4-pending-home-sales')

# 5 — reported Meta earnings and capex figures with honest units.
f=page('Meta revenue grows while AI spending absorbs cash','Third-quarter 2026 reported figures • $ billions','Source: Reuters, Oct 21–22, 2026.\nRevenue and free cash flow are quarterly; capex is a separate full-year forecast range.')
a=f.add_axes([.08,.30,.38,.37]); vals=[64.6,-2.12]; names=['Revenue','Free cash flow']; a.bar(names,vals,color=[BLUE,NEG],edgecolor=NAVY,width=.55); a.axhline(0,color=NAVY,lw=1.2); a.set_ylabel('$ billions'); a.set_ylim(-10,72); a.grid(axis='y',color='#E0E5E9'); a.set_axisbelow(True); a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals): a.text(i,v+2 if v>=0 else v-2.2,f'{v:.2f}',ha='center',va='bottom' if v>=0 else 'top',weight='bold')
box(f,.55,.39,.38,.24,'2026 CAPEX FORECAST','$135–145bn\nreported range',GOLD)
f.text(.55,.28,'Muse surpassed 10m users\nin the U.S. and Canada.',fontsize=18,weight='bold',linespacing=1.3)
save(f,f'{D}-story-5-meta-ai-spending')

f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold'); f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold'); f.text(.05,.63,'OCTOBER 22, 2026',fontsize=20,color='#B8C8D2')
f.text(.05,.40,'Inference shift\n& AI-capex risk',fontsize=38,color='white',weight='bold',linespacing=1.3)
f.text(.05,.18,'Conformal audits • LOB states • Nasdaq futures',fontsize=19,color='#B8C8D2'); f.text(.05,.08,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2')
save(f,f'{D}-linkedin-cover')
print('Rendered five story graphics and dated cover.')
