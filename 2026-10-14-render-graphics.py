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
 a.add_patch(Rectangle((0,0),1200,68,color=NAVY));a.text(44,42,'MARKET STATE LAB / '+cat,color='white',fontsize=15,weight='bold');a.text(1156,42,'14 OCT 2026',ha='right',color='#ABD6E6',fontsize=13)
 a.text(44,120,title,color=INK,fontsize=26,weight='bold');a.text(44,160,sub,color=MUTED,fontsize=15)
 return f,a
def box(a,x,y,w,h,title,body):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0,rounding_size=10',facecolor='white',edgecolor=GRID,lw=1.5));a.text(x+20,y+35,title,color=BLUE,fontsize=18,weight='bold');a.text(x+20,y+65,body,color=INK,fontsize=16,va='top',linespacing=1.5)
def foot(a,take,source,note):
 a.plot([44,1156],[540,540],color=GRID);a.text(44,577,take,color=INK,fontsize=18,weight='bold');a.text(44,615,source,color=MUTED,fontsize=12);a.text(44,645,note,color=MUTED,fontsize=12)
def save(f,name):
 for ext in ['png','svg']:f.savefig(OUT/('2026-10-14-'+name+'.'+ext),dpi=100,facecolor=f.get_facecolor())
 plt.close(f)
f,a=base('AI / SAFETY','Compute access for agentic safety research','NVIDIA announcement dated October 13, 2026 • five-year commitment')
for x,t,b in [(44,'COMPUTE COMMITMENT','$250 million valuation\nover five years'),(430,'UK CLOUD PARTNERS','Domestic infrastructure\nTerms to be agreed'),(816,'RESEARCH PROGRAM','Agentic AI safeguards\nand robotics safety')]:box(a,x,230,340,165,t,b)
a.text(600,461,'More testing capacity does not establish safer deployed agents.',ha='center',fontsize=21,color=GOLD,weight='bold')
foot(a,'Test permissions, shutdown, recovery and independent monitoring.','Source: NVIDIA Newsroom, October 13, 2026. Graphic: Market State Lab.','Conceptual program summary; compute access, not a cash grant or measured safety improvement.')
save(f,'story-1-agentic-safety')
f,a=base('QUANT / INFRASTRUCTURE','CME cloud migration: client testing comes first','CME announcement, October 12, 2026 • planned milestones')
for x,t,b in [(44,'INITIAL TESTING','Exchange reports faster\ntrading round trips'),(430,'MID-2027 TARGET','Aurora client testing\nand co-location facility'),(816,'LATE-2027 PLAN','Livestock production\nmigration to Aurora')]:box(a,x,230,340,165,t,b)
a.text(600,461,'Client tail latency and failover still require validation.',ha='center',fontsize=23,color=GOLD,weight='bold')
foot(a,'Benchmark queue behavior, jitter, recovery and cancellation paths.','Source: CME Group, October 12, 2026. Graphic: Market State Lab.','Conceptual milestone panel; future dates are targets and initial performance claims are company-reported.')
save(f,'story-2-cme-cloud')
f,a=base('U.S. MARKETS','Dow and S&P futures rise; Nasdaq stalls','October 14, 2026, 4:41 a.m. CT • indicative percentage changes')
z=f.add_axes([.23,.31,.66,.36],facecolor=BG);vals=[.45,.21,-.03];names=['Dow E-mini','S&P 500 E-mini','Nasdaq-100 E-mini']
z.barh([2,1,0],vals,color=[BLUE,BLUE,GOLD],height=.48);z.axvline(0,color=INK,lw=1);z.set(xlim=(-.15,.60),yticks=[2,1,0],yticklabels=names,xticks=[-.1,0,.1,.2,.3,.4,.5,.6]);z.set_xticklabels(['−0.1%','0','+0.1%','+0.2%','+0.3%','+0.4%','+0.5%','+0.6%']);z.tick_params(labelsize=13,length=0,pad=10);z.xaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for y,v in zip([2,1,0],vals):z.text(v+(.025 if v>=0 else -.025),y,f'{v:+.2f}%',va='center',ha='left' if v>=0 else 'right',fontsize=19,weight='bold',color=INK)
foot(a,'CPI at 7:30 a.m. CT can reset the premarket price regime.','Source: Reuters / AOL, October 14, 2026, 5:41 a.m. ET. Graphic: Market State Lab.','Reported futures changes; not executable quotes, cash-index returns, spreads or order-book depth.')
save(f,'story-3-futures-cpi')
f,a=base('ECONOMY / FED','Williams separates 2026 from 2027','October 13 interview, as reported by Reuters • conditional personal assessment')
box(a,44,230,520,165,'2026 ASSESSMENT','One additional rate increase\nmay be appropriate')
box(a,636,230,520,165,'2027 ASSESSMENT','No further increase currently needed\nIncoming data can change the view')
a.text(600,461,'A policymaker’s outlook is not an FOMC commitment.',ha='center',fontsize=23,color=GOLD,weight='bold')
foot(a,'Separate the next meeting decision from the longer policy path.','Source: Reuters, October 13, 2026, reporting a Bloomberg interview. Market State Lab.','Conceptual policy summary; no forecast curve or probability is implied.')
save(f,'story-4-williams-path')
f,a=base('TECHNOLOGY / BUSINESS','ASML: higher sales, then a conditional outlook','October 14, 2026 results • net sales in billions of euros')
z=f.add_axes([.09,.32,.82,.36],facecolor=BG)
z.bar([0,1],[9.326,11.662],width=.52,color=BLUE,label='Reported');z.bar(2,14.2,width=.52,color='none',edgecolor=GOLD,lw=2,label='Q4 guidance');z.bar(2,1,bottom=14.2,width=.52,color=GOLD,alpha=.35)
z.set(ylim=(0,17),yticks=[0,5,10,15],xticks=[0,1,2],xticklabels=['Q2 2026 reported','Q3 2026 reported','Q4 2026 guidance']);z.set_ylabel('Net sales (€ billions)',fontsize=13);z.tick_params(labelsize=14,length=0,pad=10);z.yaxis.grid(True,color=GRID);z.set_axisbelow(True);z.spines[['top','right','left','bottom']].set_visible(False)
for x,v in [(0,9.326),(1,11.662)]:z.text(x,v+.5,f'€{v:.3f}bn',ha='center',fontsize=18,weight='bold',color=INK)
z.text(2,15.8,'€14.2–15.2bn',ha='center',fontsize=18,weight='bold',color=GOLD)
foot(a,'Demand forecasts and capacity plans must convert into shipments.','Source: ASML Q3 2026 results, October 14, 2026. Graphic: Market State Lab.','Zero-based sales scale. Hollow Q4 bar is guidance, not revenue already earned; upper band shows range.')
save(f,'story-5-asml-results')
f=plt.figure(figsize=(12,6.27),dpi=100,facecolor=NAVY);a=f.add_axes([0,0,1,1]);a.set(xlim=(0,1200),ylim=(627,0));a.axis('off')
for x,y,t,size,col in [(60,73,'MARKET STATE LAB',19,'#64C1DF'),(60,160,'Quant Market Brief',38,'white'),(60,216,'OCTOBER 14, 2026',20,'#B8CDDC'),(60,335,'CPI execution risk',37,'white'),(60,402,'& ASML capacity',37,'white'),(60,489,'Agentic safety • CME cloud migration • Fed rate path',19,'#B8CDDC'),(60,582,'Five developments. Practical quant and MATLAB implications.',17,'#64C1DF')]:a.text(x,y,t,fontsize=size,color=col,weight='bold' if y in [73,160,335,402] else 'normal')
save(f,'linkedin-cover')
