"""Reproducible October 11 QMB editorial diagrams; data and sources in manifest.json."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT=Path(__file__).parent/'assets'/'2026-10-11'
OUT.mkdir(parents=True, exist_ok=True)
NAVY='#0B2237'; INK='#162B3D'; BLUE='#087CAB'; GOLD='#C98017'; MUTED='#536577'; BG='#F7F9FB'; GRID='#D9E1E7'
plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'none'})
def base(category,title,sub):
    fig=plt.figure(figsize=(12,6.75),dpi=100,facecolor=BG)
    ax=fig.add_axes([0,0,1,1]); ax.set_xlim(0,1200); ax.set_ylim(675,0); ax.axis('off')
    ax.add_patch(Rectangle((0,0),1200,68,color=NAVY))
    ax.text(44,42,'MARKET STATE LAB  /  '+category,color='white',fontsize=15,weight='bold')
    ax.text(1156,42,'11 OCT 2026',color='#ABD6E6',fontsize=13,ha='right')
    ax.text(44,122,title,color=INK,fontsize=26,weight='bold')
    ax.text(44,160,sub,color=MUTED,fontsize=15)
    return fig,ax
def foot(ax,takeaway,source,note):
    ax.plot([44,1156],[541,541],color=GRID,lw=1)
    ax.text(44,577,takeaway,color=INK,fontsize=18,weight='bold')
    ax.text(44,617,source,color=MUTED,fontsize=11)
    ax.text(44,644,note,color=MUTED,fontsize=11)
def save(fig,name):
    fig.savefig(OUT/(name+'.png'),dpi=100,facecolor=BG)
    fig.savefig(OUT/(name+'.svg'),facecolor=BG)
    plt.close(fig)
def box(ax,x,y,w,h,heading,body,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=12',facecolor='white',edgecolor=GRID,lw=1.5))
    ax.add_patch(Rectangle((x,y+14),5,h-28,color=color))
    ax.text(x+22,y+34,heading,color=color,fontsize=17,weight='bold')
    ax.text(x+22,y+57,body,color=INK,fontsize=15,linespacing=1.5,va='top')

fig,ax=base('AI & GOVERNANCE','China’s AI policy: expansion and controls','A conceptual summary of the guidelines reported on October 9')
box(ax,44,208,340,126,'BUILD','AI research and\ninfrastructure')
box(ax,430,208,340,126,'DEPLOY','Industrial pilots and\nAI applications')
box(ax,816,208,340,126,'MONITOR','Safety systems and\nemergency responses')
ax.add_patch(Rectangle((44,369),1112,117,facecolor='#EAF1F6',edgecolor='none'))
ax.text(68,405,'CAPITAL DISCIPLINE',color=GOLD,fontsize=16,weight='bold')
ax.text(68,448,'Oversight of investment bubbles and excess capacity',color=INK,fontsize=21)
foot(ax,'Research implication: assess deployment controls and economics together.','Source: Reuters, October 9, 2026. Graphic: Market State Lab.','Conceptual summary; policy intent is not evidence of successful implementation.')
save(fig,'story-1-ai-governance')

fig,ax=base('QUANT & EXECUTION','Participation and transient market impact','Conceptual curves — arbitrary units; no empirical calibration')
a=fig.add_axes([.095,.29,.36,.36],facecolor=BG)
x=np.linspace(0,1,100);a.plot(x,np.sqrt(x),color=BLUE,lw=3);a.set_xlim(0,1.05);a.set_ylim(0,1.1)
a.set_xticks([]);a.set_yticks([]);a.set_xlabel('Participation rate →',fontsize=14,color=INK,labelpad=10);a.set_ylabel('Impact →',fontsize=14,color=INK,labelpad=10)
a.set_title('Impact depends on trading rate',loc='left',fontsize=15,color=INK,pad=13)
b=fig.add_axes([.595,.29,.34,.36],facecolor=BG)
t=np.linspace(0,1,100);b.plot(t,.25+.75*np.exp(-4*t),color=GOLD,lw=3);b.set_xlim(0,1.05);b.set_ylim(0,1.1)
b.set_xticks([]);b.set_yticks([]);b.set_xlabel('Time after execution →',fontsize=14,color=INK,labelpad=10);b.set_ylabel('Remaining impact →',fontsize=14,color=INK,labelpad=10)
b.set_title('Impact can decay after trading',loc='left',fontsize=15,color=INK,pad=13)
for z in (a,b):
    z.spines[['top','right']].set_visible(False)
    for side in ['left','bottom']:z.spines[side].set_color(MUTED)
foot(ax,'Test execution assumptions before trusting a strategy ranking.','Context: Julius F. Bonart, arXiv:2610.11691, October 8, 2026. Graphic: Market State Lab.','Schematic teaching curves, not reproduced paper results or SPY/QQQ forecasts. Preprint; not peer reviewed.')
save(fig,'story-2-market-impact')

fig,ax=base('U.S. MARKETS','S&P 500 concentration: the ten largest companies','Approximate share of total index weight; different constituent sets may apply')
z=fig.add_axes([.18,.30,.66,.37],facecolor=BG)
z.barh([1,0],[28,40],color=[BLUE,BLUE],height=.46)
z.set_xlim(0,50);z.set_yticks([1,0],['October 2022','October 2026']);z.set_xticks([0,10,20,30,40,50],[f'{v}%' for v in [0,10,20,30,40,50]])
z.tick_params(axis='both',labelsize=14,colors=INK,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True)
for y,v in [(1,28),(0,40)]:z.text(v+1,y,f'≈{v}%',va='center',fontsize=23,weight='bold',color=INK)
z.spines[['top','right','left','bottom']].set_visible(False)
foot(ax,'Concentration is an exposure measure, not a market-timing signal.','Source: J.P. Morgan Asset Management, as cited by Reuters, October 9 (updated October 10), 2026.','Rounded reported values; not a live holdings calculation. Graphic: Market State Lab.')
save(fig,'story-3-index-concentration')

fig,ax=base('ECONOMY & FED','Household debt payments relative to income','Median ratio among U.S. families with debt; survey years 2022 and 2025')
z=fig.add_axes([.15,.30,.70,.37],facecolor=BG)
z.bar([0,1],[13.4,15.4],color=BLUE,width=.48);z.set_ylim(0,20);z.set_xlim(-.65,1.65)
z.set_xticks([0,1],['2022 survey','2025 survey']);z.set_yticks([0,5,10,15,20],[f'{v}%' for v in [0,5,10,15,20]])
z.tick_params(axis='both',labelsize=14,colors=INK,length=0,pad=10);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True)
for x,v in [(0,13.4),(1,15.4)]:z.text(x,v+.55,f'{v:.1f}%',ha='center',fontsize=24,weight='bold',color=INK)
z.spines[['top','right','left']].set_visible(False);z.spines['bottom'].set_color(GRID)
foot(ax,'The median rose by 2.0 percentage points between surveys.','Source: Federal Reserve, 2025 Survey of Consumer Finances, table 5; October 2026 report.','Lagged survey estimates, not an October 2026 nowcast. Graphic: Market State Lab.')
save(fig,'story-4-household-debt')

fig,ax=base('TECHNOLOGY & BUSINESS','Nvidia and Reflection AI: reported discussions','Status as reported October 10, 2026 — no transaction confirmed')
box(ax,44,230,300,120,'NVIDIA','Potential investor\nor acquirer')
box(ax,856,230,300,120,'REFLECTION AI','AI model developer\nand reported target')
ax.add_patch(FancyArrowPatch((355,291),(844,291),arrowstyle='<->',mutation_scale=20,color=GOLD,lw=2.5,linestyle='--'))
ax.text(600,244,'REPORTED TALKS',ha='center',color=GOLD,fontsize=17,weight='bold')
ax.text(600,329,'Further investment or acquisition',ha='center',color=INK,fontsize=15)
ax.text(600,432,'Structure, price and outcome remain unconfirmed',ha='center',color=INK,fontsize=22,weight='bold')
foot(ax,'Research implication: monitor concentration and platform dependencies.','Source: Reuters, October 10, 2026, citing the Financial Times. Graphic: Market State Lab.','Dashed connection denotes reported discussions, not ownership or a completed deal.')
save(fig,'story-5-nvidia-reflection')

fig=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);ax=fig.add_axes([0,0,1,1]);ax.set_xlim(0,1200);ax.set_ylim(627,0);ax.axis('off')
ax.text(60,73,'MARKET STATE LAB',color='#64C1DF',fontsize=19,weight='bold')
ax.text(60,160,'Quant Market Brief',color='white',fontsize=38,weight='bold')
ax.text(60,216,'OCTOBER 11, 2026',color='#B8CDDC',fontsize=20)
ax.plot([60,1140],[259,259],color='#426077',lw=1)
ax.text(60,335,'Market impact',color='white',fontsize=37,weight='bold')
ax.text(60,397,'& AI concentration',color='white',fontsize=37,weight='bold')
ax.text(60,481,'Execution realism  •  Exposure overlap  •  Household debt',color='#B8CDDC',fontsize=19)
ax.text(60,569,'Five developments. Practical quant and MATLAB implications.',color='#64C1DF',fontsize=18)
fig.savefig(OUT/'linkedin-cover.png',dpi=100,facecolor=NAVY);fig.savefig(OUT/'linkedin-cover.svg',facecolor=NAVY);plt.close(fig)
print('Created five story graphics plus one LinkedIn cover (PNG and SVG).')
