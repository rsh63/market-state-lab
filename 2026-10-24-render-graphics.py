from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyArrowPatch
from PIL import Image,ImageOps
P=Path(__file__).parent;D='2026-10-24';NAVY='#0D2638';BLUE='#197D96';GOLD='#BE8C35';GRAY='#586976';BG='#F7F9FB';OPEN='#DCEBF0';INK='#233746'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':18,'text.color':INK,'svg.fonttype':'none'})
def page(title,sub,cap):
 f=plt.figure(figsize=(12,7.6),dpi=100,facecolor=BG);f.patches.append(Rectangle((0,.91),1,.09,transform=f.transFigure,facecolor=NAVY));f.text(.04,.947,'MARKET STATE LAB / QUANT MARKET BRIEF',color='white',fontsize=15,weight='bold');f.text(.96,.947,'24 OCT 2026',color='#B7D1DF',fontsize=14,ha='right');f.text(.04,.84,title,fontsize=25,weight='bold');f.text(.04,.775,sub,fontsize=18,color=GRAY);f.text(.04,.043,cap,fontsize=16,color=GRAY,linespacing=1.35);return f
def save(f,n):
 for ext in ['png','svg']:f.savefig(P/f'{D}-{n}.{ext}',dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
def box(f,x,y,w,h,title,body):
 f.patches.append(Rectangle((x,y),w,h,transform=f.transFigure,facecolor='white',edgecolor='#CFD8DF'));f.text(x+.02,y+h-.05,title,fontsize=20,color=BLUE,weight='bold',va='top');f.text(x+.02,y+h-.12,body,fontsize=20,va='top',linespacing=1.4)
f=page('Abstention can lower decision cost','Held-out IT-ticket test • illustrative cost units, not trading returns','Source: Gupta, arXiv:2610.31657v1, October 22, 2026.\nPolicy threshold selected on calibration data; results depend on the stated cost model.')
a=f.add_axes([.16,.28,.72,.42]);a.bar(['Always route','Abstention policy'],[.763,.472],color=[OPEN,BLUE],edgecolor=NAVY,width=.5);a.set_ylim(0,.9);a.set_ylabel('Mean test cost');a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i,v in enumerate([.763,.472]):a.text(i,v+.025,str(v),ha='center',weight='bold',fontsize=21)
f.text(.05,.16,'Reported cost reduction: 38.1%\nNo transferable trading threshold',fontsize=19,weight='bold');save(f,'story-1-cost-aware-abstention')
f=page('Separate signal skill from execution role','Institutional intraday-trader study • conceptual observational audit','Source: Hao et al., arXiv:2610.31141v1, October 22, 2026.\nAssociations and hypothetical strategies do not establish causal alpha or attainable returns.')
box(f,.05,.46,.4,.25,'MATCH EXECUTIONS','Buy + sell → position\nHorizon-matched evidence');box(f,.55,.46,.4,.25,'SEPARATE EXPLANATIONS','Forecasting proxy\nPassive execution roles');f.patches.append(FancyArrowPatch((.45,.58),(.55,.58),transform=f.transFigure,arrowstyle='->',mutation_scale=20,color=GRAY));box(f,.05,.19,.9,.20,'AUDIT POSITION P&L','Control information timing, queue access\nand post-fill adverse selection.');save(f,'story-2-institutional-liquidity')
f=page('Friday’s close: Dow leads index losses','October 23, 2026 • close-to-close index returns (%)','Source: Reuters October 23 closing report.\nIndex returns, not ETF returns. Prior-close data do not describe weekend liquidity.')
a=f.add_axes([.28,.28,.61,.43]);vals=[-1.23,-.52,-.21];a.barh(['Dow','S&P 500','Nasdaq Composite'],vals,color=[GOLD,BLUE,OPEN],edgecolor=NAVY,height=.55);a.invert_yaxis();a.set_xlim(-1.65,.1);a.axvline(0,color=NAVY);a.set_xlabel('Index change (%)');a.grid(axis='x',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i,v in enumerate(vals):a.text(v-.04,i,f'{v:.2f}%',ha='right',va='center',weight='bold',fontsize=20)
save(f,'story-3-friday-market-close')
f=page('October sentiment hides diverging components','University of Michigan final survey • index points, not percent changes','Source: University of Michigan, released October 23, 2026.\nSeptember and October final readings. Attitudes are not realized spending or inflation.')
a=f.add_axes([.10,.28,.82,.42]);xs=[0,1,2];p=[48.1,50.9,46.3];q=[48,46.7,48.8];a.bar([x-.19 for x in xs],p,width=.36,color=OPEN,edgecolor=NAVY,label='September');a.bar([x+.19 for x in xs],q,width=.36,color=BLUE,edgecolor=NAVY,label='October');a.set_xticks(xs,['Sentiment','Current conditions','Expectations']);a.set_ylim(0,62);a.set_ylabel('Index points');a.legend(frameon=False,ncol=2,loc='lower center',bbox_to_anchor=(.5,1.00));a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i in xs:
 for dx,v in [(-.19,p[i]),(.19,q[i])]:a.text(i+dx,v+1,f'{v:.1f}',ha='center',fontsize=17,weight='bold')
save(f,'story-4-michigan-sentiment')
f=page('AmEx: reported and adjusted EPS diverge','Third-quarter earnings per share • dollars per share','Source: American Express SEC-filed release, October 23, 2026.\nAdjusted EPS excludes the investment-sale gain net of related restructuring; non-GAAP measure.')
a=f.add_axes([.12,.28,.78,.42]);xs=[0,1];p=[4.14,4.14];q=[5.42,4.68];a.bar([x-.18 for x in xs],p,width=.34,color=OPEN,edgecolor=NAVY,label='Q3 2025');a.bar([x+.18 for x in xs],q,width=.34,color=BLUE,edgecolor=NAVY,label='Q3 2026');a.set_xticks(xs,['Reported EPS','Adjusted EPS']);a.set_ylim(0,6.5);a.set_ylabel('Dollars per share');a.legend(frameon=False,ncol=2,loc='lower center',bbox_to_anchor=(.5,1.00));a.grid(axis='y',color='#E0E5E9');a.set_axisbelow(True);a.spines[['top','right']].set_visible(False)
for i in xs:
 for dx,v in [(-.18,p[i]),(.18,q[i])]:a.text(i+dx,v+.1,f'{v:.2f}',ha='center',fontsize=20,weight='bold')
save(f,'story-5-amex-earnings')
f=plt.figure(figsize=(12,6.75),dpi=100,facecolor=NAVY);f.text(.05,.86,'MARKET STATE LAB',fontsize=18,color='#78BDD2',weight='bold');f.text(.05,.71,'Quant Market Brief',fontsize=34,color='white',weight='bold');f.text(.05,.63,'OCTOBER 24, 2026',fontsize=20,color='#B8C8D2');f.text(.05,.4,'Cost-aware AI\n& consumer divergence',fontsize=36,color='white',weight='bold',linespacing=1.3);f.text(.05,.17,'Abstention • Execution roles • Earnings quality',fontsize=20,color='#B8C8D2');f.text(.05,.07,'Dated evidence • Explicit uncertainty • Execution discipline',fontsize=16,color='#78BDD2');save(f,'linkedin-cover')
ims=[Image.open(x).convert('RGB').resize((600,380)) for x in sorted(P.glob(f'{D}-story-*.png'))];ims.append(ImageOps.pad(Image.open(P/f'{D}-linkedin-cover.png').convert('RGB'),(600,380),color=BG));qa=Image.new('RGB',(1200,1140),BG)
for i,im in enumerate(ims):qa.paste(im,((i%2)*600,(i//2)*380))
qa.save(P/'image-qa.png')
