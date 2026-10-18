from pathlib import Path
import json,textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
P=Path(__file__).parent; D='2026-10-18'
S=json.loads((P/f'{D}-sources.json').read_text())['stories']
NAVY='#0D2638'; BLUE='#197D96'; GOLD='#BE8C35'; INK='#233746'; GRAY='#586976'; BG='#F7F9FB'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':17,'text.color':INK,'axes.labelcolor':INK,'xtick.color':GRAY,'ytick.color':INK,'svg.fonttype':'none'})
def page(title,subtitle,caption):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG)
 f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY))
 f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold')
 f.text(.96,.947,'18 OCT 2026',color='#B7D1DF',fontsize=14,ha='right')
 f.text(.04,.84,title,fontsize=25,weight='bold')
 f.text(.04,.775,subtitle,fontsize=16,color=GRAY)
 f.text(.04,.055,caption,fontsize=13,color=GRAY,linespacing=1.5)
 return f
def box(f,x,y,w,h,title,body,color=BLUE):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF',lw=1.3))
 f.text(x+.018,y+h-.05,title,color=color,weight='bold',fontsize=18,va='top')
 f.text(x+.018,y+h-.12,body,fontsize=17,va='top',linespacing=1.6)
def save(f,name):
 for ext in ['png','svg']: f.savefig(P/f'{name}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)

f=page('Independent evaluator access: three tiers','Anthropic announcement October 15; project terms clarified October 16, 2026','Source: Anthropic, “An update on independent evaluators,” Oct 15–16, 2026.\nConceptual comparison. Access and publication rights do not prove model safety.')
box(f,.04,.29,.285,.40,'TIER 1','Narrow investigation\nAccess set by company\nPublication requires\ncompany approval')
box(f,.357,.29,.285,.40,'TIER 2','More information\nPublish without veto\nDefined redactions;\ncan contest limits')
box(f,.674,.29,.285,.40,'TIER 3 / METR','Employee-like access\nSimilar rights to tier 2\nSix embedded staff\nProtected categories')
f.text(.04,.20,'Key limit: Anthropic decides whether information fits redaction categories.',fontsize=17)
save(f,f'{D}-story-1-{S[0]["slug"]}')

f=page('StochLOB: training noise and deterministic inference','October 15, 2026 arXiv preprint • Conceptual method map','Source: Abolghasemi et al., arXiv:2610.21081v1, submitted Oct 15, 2026.\nIllustrative architecture, not a calibrated timeline or performance comparison.')
box(f,.04,.32,.285,.38,'TRAINING NOISE','Gaussian baseline\nversus jump-Lévy\nand clipped\nalpha-stable noise')
box(f,.357,.32,.285,.38,'SCORE MATCHING','Train on perturbed\norder-book data\nKeep chronological\nheld-out tests')
box(f,.674,.32,.285,.38,'DEPLOYMENT','Deterministic predictor\nNo reverse-time\ndiffusion sampling\nat inference')
for a,b in [(.325,.357),(.642,.674)]: f.patches.append(FancyArrowPatch((a,.51),(b,.51),transform=f.transFigure,arrowstyle='->',mutation_scale=18,color=GRAY))
f.text(.04,.21,'Trading test: calibration + tail losses + costs + market-rule constraints.',fontsize=18,weight='bold')
save(f,f'{D}-story-2-{S[1]["slug"]}')

f=page('S&P 500 constituent breadth: week ended October 16','Share of index constituents by weekly price direction • Reported October 17, 2026','Source: MarketWatch citing Dow Jones Market Data, Oct 17, 2026, 7:30 a.m. ET.\nCount shares, not capitalization weights or returns. Underlying constituent data not reconstructed.')
a=f.add_axes([.07,.39,.86,.25]);a.barh([0],[70],color=BLUE,height=.5,edgecolor=NAVY);a.barh([0],[30],left=[70],color='#D6E4EB',height=.5,edgecolor=NAVY)
a.text(35,0,'70% rose',ha='center',va='center',color='white',fontsize=24,weight='bold');a.text(85,0,'30% fell',ha='center',va='center',fontsize=23,weight='bold')
a.set(xlim=(0,100),yticks=[],xticks=[0,25,50,75,100],xlabel='Percent of constituents');a.spines[['left','right','top']].set_visible(False)
f.text(.06,.245,'The cap-weighted index still lost almost 2% that week.',fontsize=22,weight='bold')
save(f,f'{D}-story-3-{S[2]["slug"]}')

f=page('September industrial output: monthly change','Seasonally adjusted percent change • Preliminary September 2026 data','Source: Federal Reserve G.17, released Oct 16, 2026.\nTotal industry overlaps its components; the bars must not be added together.')
a=f.add_axes([.24,.31,.68,.37]);names=['Total industry','Manufacturing','Mining','Utilities'];vals=[.7,.3,.2,3.5]
a.barh(names,vals,color=BLUE,edgecolor=NAVY,height=.55);a.invert_yaxis();a.set_xlim(0,4.0);a.set_xlabel('Monthly change (%)');a.set_xticks([0,1,2,3,4]);a.grid(axis='x',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals):a.text(v+.07,i,f'+{v:.1f}%',va='center',fontsize=19)
f.text(.04,.16,'Capacity utilization: 76.9% • Below its long-run average',fontsize=18,weight='bold')
save(f,f'{D}-story-4-{S[3]["slug"]}')

f=page('Solar manufacturing: proposed technology controls','China ministry proposal October 16 • Reuters report October 18, 2026','Source: Reuters, Oct 18, 2026, 06:22:59 UTC. Public consultation closes Nov 15.\nProposed catalogue categories, not final law; company-level effects remain uncertain.')
box(f,.04,.29,.445,.41,'PROPOSED PROHIBITIONS','Selected thin-wafer processes\nPerovskite / tandem cells\nLarge-scale fluidized-bed\npolysilicon production')
box(f,.515,.29,.445,.41,'RESTRICTED, NOT PROHIBITED','Advanced cell-making processes:\nTOPCon\nHJT\nXBC',GOLD)
f.text(.04,.20,'12 technologies covered by proposal • Verify final scope before acting.',fontsize=18,weight='bold')
save(f,f'{D}-story-5-{S[4]["slug"]}')

f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold');f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold');f.text(.05,.63,'OCTOBER 18, 2026',fontsize=20,color='#B8C8D2')
f.text(.05,.40,'Market breadth\n& robust evaluation',fontsize=36,color='white',weight='bold',linespacing=1.3)
f.text(.05,.18,'Independent review • Heavy-tailed training • Industrial output',fontsize=19,color='#B8C8D2');f.text(.05,.08,'Weekend edition • Dated facts, explicit uncertainty',fontsize=16,color='#78BDD2')
save(f,f'{D}-linkedin-cover')
print('Rendered five story graphics and one cover in PNG/SVG.')
