from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
P=Path(__file__).parent;D='2026-10-20';S=json.loads((P/f'{D}-sources.json').read_text())['stories']
NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';INK='#233746';GRAY='#586976';BG='#F7F9FB'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'axes.labelcolor':INK,'xtick.color':GRAY,'ytick.color':INK,'svg.fonttype':'none'})
def page(title,subtitle,caption):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG)
 f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY))
 f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold')
 f.text(.96,.947,'20 OCT 2026',color='#B7D1DF',fontsize=14,ha='right')
 f.text(.04,.84,title,fontsize=25,weight='bold')
 f.text(.04,.775,subtitle,fontsize=16,color=GRAY)
 f.text(.04,.055,caption,fontsize=14,color=GRAY,linespacing=1.5)
 return f
def box(f,x,y,w,h,title,body,color=BLUE):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF',lw=1.3))
 f.text(x+.018,y+h-.045,title,color=color,weight='bold',fontsize=19,va='top')
 f.text(x+.018,y+h-.115,body,fontsize=18,va='top',linespacing=1.5)
def arrow(f,start,end):f.patches.append(FancyArrowPatch(start,end,transform=f.transFigure,arrowstyle='->',mutation_scale=18,color=GRAY))
def save(f,name):
 for ext in ['png','svg']:f.savefig(P/f'{name}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f=page('AuDQ: evidence before agentic rule discovery','October 19, 2026 preprint • Conceptual implementation map','Source: Biggiogera et al., arXiv:2610.26031v1, Oct 19, 2026.\nPreliminary finance/retail tests; the complete governance layer remains a research vision.')
box(f,.04,.48,.44,.22,'1 / DETERMINISTIC PROFILE','Compute data statistics; no LLM')
box(f,.52,.48,.44,.22,'2 / ONTOLOGY','Map entities and relationships')
box(f,.04,.22,.44,.22,'4 / IMPLEMENT RULES','Keep versioned execution artifacts')
box(f,.52,.22,.44,.22,'3 / DISCOVER + REVIEW','Agentic rules; human review gate',GOLD)
arrow(f,(.48,.59),(.52,.59));arrow(f,(.74,.48),(.74,.44));arrow(f,(.52,.33),(.48,.33))
f.text(.04,.16,'Shared versioned repository links evidence, rules and review decisions.',fontsize=18,weight='bold')
save(f,f'{D}-story-1-{S[0]["slug"]}')
f=page('RegimeRank: inputs, conditioning and sector ranking','October 19, 2026 research • Conceptual architecture, not a return forecast','Source: Koa et al., arXiv:2610.26456v1, Oct 19, 2026.\nWeekly 2002–2024 data; forward labels reduce usable end dates. Ranking gains ≠ net returns.')
box(f,.04,.31,.285,.39,'SIGNAL FEATURES','Fundamental + technical\nTemporal characteristics\nConditioned on\nlearned macro factors')
box(f,.357,.31,.285,.39,'SECTOR RELATIONS','Cross-sector attention\nInformation shared\nacross related sectors\nAttribution diagnostics')
box(f,.674,.31,.285,.39,'RANKING OUTPUT','Forward active Sharpe\n52-week labels\nPurging + embargo\nFew independent periods')
arrow(f,(.325,.51),(.357,.51));arrow(f,(.642,.51),(.674,.51))
f.text(.04,.20,'Next test: chronological walk-forward + turnover costs + frozen baseline.',fontsize=19,weight='bold')
save(f,f'{D}-story-2-{S[1]["slug"]}')
f=page('October 19 closing index changes','Daily price change (%) • Completed session, not October 20 futures','Source: Reuters / LSEG, October 19, 2026 final-close report.\nIndex gains do not establish broad participation; NYSE decliners exceeded advancers.')
a=f.add_axes([.23,.31,.67,.38]);names=['Dow','S&P 500','Nasdaq Composite','Semiconductors'];vals=[-.07,.41,1.11,1.6]
a.barh(names,vals,color=BLUE,edgecolor=NAVY,height=.56);a.invert_yaxis();a.axvline(0,color=NAVY,lw=1.2);a.set_xlim(-.25,1.95);a.set_xticks([0,.5,1,1.5]);a.set_xlabel('Daily change (%)');a.grid(axis='x',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals):a.text(v+.04 if v>=0 else .04,i,f'{v:+.2f}%',va='center',fontsize=19,weight='bold')
f.text(.04,.17,'NYSE declining / advancing issues: 1.69 to 1',fontsize=22,weight='bold')
save(f,f'{D}-story-3-{S[2]["slug"]}')
f=page('October housing-market sentiment: index levels','NAHB / Wells Fargo HMI • Seasonally adjusted • Released October 19, 2026','Source: NAHB, “Builder Sentiment Falls on Rising Rates,” Oct 19, 2026.\nAggregate and components overlap; do not add. Survey perceptions, not housing starts.')
a=f.add_axes([.27,.31,.65,.38]);names=['Headline HMI','Current sales','Six-month outlook','Buyer traffic'];vals=[29,33,32,18]
a.barh(names,vals,color=BLUE,edgecolor=NAVY,height=.55);a.invert_yaxis();a.set_xlim(0,60);a.set_xticks([0,10,20,30,40,50,60]);a.set_xlabel('Index points');a.axvline(50,color=GOLD,linestyle='--',lw=1.6);a.grid(axis='x',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals):a.text(v+1,i,str(v),va='center',fontsize=21,weight='bold')
f.text(.04,.17,'50 = balance threshold for good versus poor conditions, not growth.',fontsize=19,weight='bold')
save(f,f'{D}-story-4-{S[3]["slug"]}')
f=page('Micron labor dispute: two different union roles','October 22, 2026 planned action • Reuters report October 20','Source: Reuters, Oct 20, 2026, 02:06 UTC; union statement Oct 19.\nPlanned action, not an observed shutdown. Duration and production effects are unknown.')
box(f,.04,.30,.445,.40,'TAOYUAN UNION','Plans Thursday strike\nOctober 22\nSolidarity action')
box(f,.515,.30,.445,.40,'TAICHUNG UNION','Mediation Thursday\nOctober 22\nHas not voted to strike',GOLD)
f.text(.04,.20,'Do not infer an island-wide shutdown or a quantity of lost output.',fontsize=20,weight='bold')
save(f,f'{D}-story-5-{S[4]["slug"]}')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY)
f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold');f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold');f.text(.05,.63,'OCTOBER 20, 2026',fontsize=20,color='#B8C8D2')
f.text(.05,.40,'Auditable AI\n& sector rotation',fontsize=38,color='white',weight='bold',linespacing=1.3)
f.text(.05,.18,'Data-quality rules • Ranking tests • Housing confidence',fontsize=19,color='#B8C8D2');f.text(.05,.08,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2')
save(f,f'{D}-linkedin-cover')
print('Rendered five story graphics and cover in dated PNG/SVG files.')
