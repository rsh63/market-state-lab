from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
P=Path(__file__).parent;D='2026-10-19';S=json.loads((P/f'{D}-sources.json').read_text())['stories']
NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';INK='#233746';GRAY='#586976';BG='#F7F9FB'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'axes.labelcolor':INK,'xtick.color':GRAY,'ytick.color':INK,'svg.fonttype':'none'})
def page(title,subtitle,caption):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG)
 f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY))
 f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold')
 f.text(.96,.947,'19 OCT 2026',color='#B7D1DF',fontsize=14,ha='right')
 f.text(.04,.84,title,fontsize=25,weight='bold')
 f.text(.04,.775,subtitle,fontsize=16,color=GRAY)
 f.text(.04,.055,caption,fontsize=14,color=GRAY,linespacing=1.5)
 return f
def box(f,x,y,w,h,title,body,color=BLUE):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF',lw=1.3))
 f.text(x+.02,y+h-.05,title,color=color,weight='bold',fontsize=20,va='top')
 f.text(x+.02,y+h-.14,body,fontsize=19,va='top',linespacing=1.6)
def save(f,name):
 for ext in ['png','svg']:f.savefig(P/f'{name}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f=page('Anthropic Public Benefit Fund: conditional equity','Company announcement October 18, 2026 • Wholly owned LLC','Source: Anthropic, “Investing in the public benefit,” Oct 18, 2026.\nCommitments are not completed cash distributions; governance details are still forthcoming.')
box(f,.04,.30,.445,.40,'INITIAL COMMITMENT','5% of company shares\nSubject to stockholder\napproval')
box(f,.515,.30,.445,.40,'POTENTIAL ADDITIONS','2% for each 50% rise\nin value above a baseline\nAt board discretion',GOLD)
f.text(.04,.20,'Do not read the additions as automatic or the stake as a payout.',fontsize=19,weight='bold')
save(f,f'{D}-story-1-{S[0]["slug"]}')
f=page('Screening needed to offset slower repricing','12-second maker versus 1-second venue • Reported lower-bound calibration','Source: Adadurov et al., arXiv:2610.21510v1, submitted Oct 15, 2026.\nFour USDC–WETH pools, Jun–Aug 2026. Model-conditioned; not an equity-market estimate.')
a=f.add_axes([.29,.34,.63,.32]);a.barh(['Empirical innovations','Gaussian benchmark'],[84.5,71.1],color=BLUE,edgecolor=NAVY,height=.5);a.invert_yaxis();a.set_xlim(0,100);a.set_xticks([0,25,50,75,100]);a.set_xlabel('Informed-flow screening (%)');a.spines[['top','right']].set_visible(False);a.grid(axis='x',color='#E0E5E9');a.set_axisbelow(True)
for i,v in enumerate([84.5,71.1]):a.text(v+1.2,i,f'{v:.1f}%',va='center',fontsize=21,weight='bold')
f.text(.04,.19,'The result motivates testing quote-age controls—not assuming transfer.',fontsize=19,weight='bold')
save(f,f'{D}-story-2-{S[1]["slug"]}')
f=page('December Nasdaq futures: overnight range and quote','October 19, 2026, 6:05 a.m. CDT • Delayed • Index points','Source: MarketWatch / FactSet, Oct 19, 2026, 6:05 a.m. CDT.\nFocused scale; a range snapshot, not the sequence of prices. No book depth is shown.')
a=f.add_axes([.09,.37,.82,.25]);a.plot([29226,29813.5],[0,0],color=BLUE,lw=8,solid_capstyle='butt');a.plot([29226,29813.5],[0,0],'|',color=NAVY,ms=25,mew=2)
a.scatter([29391.5],[0],marker='s',s=150,color=GOLD,zorder=3);a.scatter([29705.75],[0],marker='o',s=160,color=NAVY,zorder=3)
a.text(29391.5,.22,'Prior settlement\n29,391.50',ha='center',fontsize=18);a.text(29705.75,.22,'Delayed last\n29,705.75',ha='center',fontsize=18,weight='bold');a.text(29226,-.40,'Low\n29,226',ha='center',fontsize=18);a.text(29813.5,-.40,'High\n29,813.50',ha='center',fontsize=18)
a.set_xlim(29180,29870);a.set_ylim(-.5,.65);a.axis('off');f.text(.04,.21,'+1.07% versus Friday settlement ≠ a Monday cash-market return',fontsize=21,weight='bold')
save(f,f'{D}-story-3-{S[2]["slug"]}')
f=page('Fed funds liquidity signals: participant type matters','Fed staff research published October 16, 2026 • Conceptual comparison','Source: Anbil, Infante and Senyuz, FEDS Notes, Oct 16, 2026.\nStaff research, not a policy announcement or a real-time funding-stress signal.')
box(f,.04,.29,.445,.41,'ARBITRAGE CHANNEL','FHLBs → foreign banks\nRelatively elastic supply\nCompressed spreads\nLimited bank-liquidity signal')
box(f,.515,.29,.445,.41,'INTERBANK CHANNEL','Banks → banks\nReserve redistribution\nSpreads more sensitive\nto lender reserve positions',GOLD)
f.text(.04,.19,'Aggregate EFFR can miss distributional frictions.',fontsize=22,weight='bold')
save(f,f'{D}-story-4-{S[3]["slug"]}')
f=page('Reported Nvidia custom-HBM supply chain','UNCONFIRMED REPORT • Reuters citing Seoul Economic Daily, October 18','Source: Reuters, Oct 18, 2026, 12:08 UTC, citing Seoul Economic Daily.\nConceptual dependency map, not confirmed company guidance; no capacity or yield data implied.')
box(f,.04,.32,.285,.36,'TSMC','Reported 3-nm\nbase-die process')
box(f,.357,.32,.285,.36,'SAMSUNG','Custom HBM\nmanufacturing')
box(f,.674,.32,.285,.36,'NVIDIA','NVHBM\ncustom memory')
for x,y in [(.325,.357),(.642,.674)]:f.patches.append(FancyArrowPatch((x,.50),(y,.50),transform=f.transFigure,arrowstyle='->',mutation_scale=18,color=GRAY,linestyle='--'))
f.text(.04,.20,'Reported exception ≠ wholesale replacement of standard HBM.',fontsize=21,weight='bold')
save(f,f'{D}-story-5-{S[4]["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold');f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold');f.text(.05,.63,'OCTOBER 19, 2026',fontsize=20,color='#B8C8D2')
f.text(.05,.40,'Rebound risk\n& stale quotes',fontsize=38,color='white',weight='bold',linespacing=1.3)
f.text(.05,.18,'Quote freshness • Funding signals • Custom-memory report',fontsize=19,color='#B8C8D2');f.text(.05,.08,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2')
save(f,f'{D}-linkedin-cover')
print('Rendered five dated story graphics and one dated cover, PNG and SVG.')
