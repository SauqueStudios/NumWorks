from pieces_echecs_simp import *
from ion import keydown as ke
CW=(255,125,123)
CX=(99,60,0)
CD=(239,154,66)
CR=(255,0,0)
CU=(140,134,140)
class R(P):
 n="r";pn=ft("inf");dn=[1024]+[3584]*3+[32704,65504,32704,396812,986654,1966071,1638371,1576451,1838599,921102,462364,233016,101936]+[52832]*2+[262136]*2
 def __init__(sf,gm=None,x=-1,y=-1,c=-1,bt=None,tb=None,*a,**ka):
  sf.bt,sf.tb=bt,tb;sf.v=0;super().__init__(gm,x,y,c,*a,**ka)
 def __repr__(sf):return super().__repr__()+","+",".join([sr(sf.bt.x),sr(sf.bt.y),sr(sf.tb.x),sr(sf.tb.y)])
 def sg(sf,cg):sf.v=it(cg[0]);sf.bt,sf.tb=map(ft,cg[1:3]),map(ft,cg[3:])
 def t(sf):
  ms=[]
  for i in 1,-1,0:
   for j in 1,-1,0:
    if(i or j)and ii(sf.x+i)and ii(sf.y+j):
     ct=sf.gm.p[sf.x+i][sf.y+j]
     if not ct:
      if sf.tg(sf.x+i,sf.y+j):ms.append(m(sf.x+i,sf.y+j))
     elif cf(sf,ct):
      if sf.tg(sf.x+i,sf.y+j):ms.append(m(sf.x+i,sf.y+j,ct))
  if not sf.sl and not sf.v and not sf.ec():
   sf.gm.p[sf.x][sf.y]=None
   for i in 1,2:
    if sf.gm.p[sf.x+i][sf.y]or not sf.tg(sf.x+i,sf.y):break
   else:
    if not sf.tb.v:ms.append(m(sf.x+i,sf.y))
   for i in -1,-2:
    if sf.gm.p[sf.x+i][sf.y]or not sf.tg(sf.x+i,sf.y):break
   else:
    if not sf.bt.v and not sf.gm.p[1][sf.y]:ms.append(m(sf.x+i,sf.y))
   sf.gm.p[sf.x][sf.y]=sf
  return ms
 def b(sf,mv,sv=1):
  if not sf.v:sf.v=sf.gm.rt
  if sf.x-mv["x"]==2:sf.bt.b(m(mv["x"]+1,sf.y),0)
  elif mv["x"]-sf.x==2:sf.tb.b(m(mv["x"]-1,sf.y),0)
  return super().b(mv,sv)
 def ec(sf):
  a=sf.gm,sf.x,sf.y,sf.c;ka={"sl":1};c=V(*a,**ka);t=T(*a,**ka);f=F(*a,**ka);p=Q(*a,**ka);r=R(*a,**ka)
  for i in c.t():
   if z(i["pb"])is V and cf(i["pb"],sf):return 1
  for i in t.t():
   if(z(i["pb"])is T or z(i["pb"])is D)and cf(i["pb"],sf):return 1
  for i in f.t():
   if(z(i["pb"])is F or z(i["pb"])is D)and cf(i["pb"],sf):return 1
  for i in p.t():
   if z(i["pb"])is Q and cf(i["pb"],sf):return 1
  for i in r.t():
   if z(i["pb"])is R and cf(i["pb"],sf):return 1
  return 0
N["r"]=R
def bk():
 try:
  while ke(5):0
 except K:bk()
class Bk(E):0
class Fw(E):0
class O(E):0
class J(E):0
class H(E):0
ks=[[-1,1]for i in rg(6)];lv=-1
def gk(s=0,g=0):
 global lv;tt=h()
 if s and tt-lv<.05:return
 lv=tt
 while 1:
  if ke(6):p(.3);raise H()
  if ke(8):p(.3);raise O()
  if ke(5):
   if ks[5][0]==-1:ks[5][0]=0;raise K
  else:
   if not ks[5][0]:ks[5][0]=-1
  if ke(48):raise J
  if s:return
  for i in rg(5):
   if ke(i):
    if ks[i][0]==-1:ks[i][0]=h();return i
    elif ks[i][1]and h()-ks[i][0]>.3:ks[i][0]=h();ks[i][1]=0;return i
    elif not ks[i][1]and h()-ks[i][0]>0.07:ks[i][0]=h();return i
   else:
    if ks[i][0]!=-1:ks[i]=[-1,1]
  if g and ke(12):
   while ke(12):0
   raise Bk()
  if g and ke(17):
   while ke(17):0
   raise Fw()
def sm(p,x,y,k):
 pv=[[p[j][i]for j in rg(len(p[0]))]for i in rg(len(p))]
 def mvm(x,y,p,pi,r,pri=1):
  if pri:
   if r[0]<0 and any(p[x][max(y-len(p[0])+1,0):y])or r[0]>0 and any(p[x][y+1:min(y+len(p[0])-1,len(p[0]))]):
    for i in rg(y+r[0],*r[1:]):
     if p[x][i]:return x,i
  for i in rg(y+r[0],*r[1:]):
   if any(pi[i]):
    for j in rg(max(x,len(p[0])-1-x)+1):
     for s in 1,-1:
      if ii(x+j*s)and pi[i][x+j*s]:return x+j*s,i
  return x,y
 if se["i"]==-1:
  if not k:k=1
  elif k==1:k=0
  elif k==2:k=3
  elif k==3:k=2
 if not k:
  if se["y"]:k=3
 elif k==3:
  if se["y"]:k=0
 elif k==1:
  if se["x"]:k=2
 elif k==2:
  if se["x"]:k=1
 if not k:
  if se["i"]==-1:pri=1
  else:pri=0
  return mvm(x,y,p,pv,(-1,-1,-1),pri)
 elif k==3:
  if se["i"]==-1:pri=1
  else:pri=0
  return mvm(x,y,p,pv,(1,len(p[0])),pri)
 elif k==2:
  if se["i"]==1:pri=1
  else:pri=0
  return list(mvm(y,x,pv,p,(1,len(p[0])),pri))[::-1]
 elif k==1:
  if se["i"]==1:pri=1
  else:pri=0
  return list(mvm(y,x,pv,p,(-1,-1,-1),pri))[::-1]
 else:
  return x,y
def fn():raise J()
class S:
 def __init__(sf,gm,w=1,sc=1,c=1):sf.gm,sf.w,sf.sc,sf.c=gm,w,sc,c;sf.ss=[{0:(1,-1),1:(1,-1),"x":1,"y":0,"i":-1},{0:(1,-1),1:(1,-1),"x":0,"y":1,"i":-1}];sf.b={i:ga(se[i],"copy",lambda:se[i])()for i in se}
 def h(sf):
  r=" Nouvelle partie","Continuer partie"," Charger partie ","   Parametres   ","     Quitter    ";a=sf.gm.st,sf.gm.m,sf.gm.sw,sf.p,fn;s=0;d(65,25,190,190,CD);k=-1
  for i,v in ee(r):dt(v,80,40+i*35,CX,CD)
  while k!=4:
   dt(">"+r[s]+"<",70,40+s*35,CR,CD)
   try:k=gk()
   except O:
    sf.o();d(65,25,190,190,CD)
    for i,v in ee(r):dt(v,80,40+i*35,CX,CD)
    continue
   except(K,H):
    bk()
    if ga(sf.gm,"r",0)and all(sf.gm.r):s=1;break
    else:raise J()
   dt(" "+r[s]+" ",70,40+s*35,CX,CD);s+=(k==2)-(k==1)-(k==3)-(k==0);s%=len(r)
  try:a[s]()
  except(J,H,K)as e:raise e
  except E as e:sf.e(e)
 def p(sf):
  d(65,25,190,190,CD);s=0;ts=0;p=Q(sf.gm,3,3,1),Q(sf.gm,3,4,0),Q(sf.gm,4,3,1),Q(sf.gm,4,4,0);pt=(1,-1),(1,1),(-1,-1),(-1,1);tt={"x":0,"y":0,"i":1},{"x":0,"y":1,"i":-1},{"x":1,"y":1,"i":1},{"x":1,"y":0,"i":-1};av=[0]*3
  if ts==1:g=sf.ss[1]
  elif ts==2:g=sf.ss[0]
  else:g=sf.b
  for i in rg(4):
   tp=tt[i]
   if g["x"]==tp["x"]and g["y"]==tp["y"]and g["i"]==tp["i"]:av[0]=i
   if g[1]==pt[i]:av[1]=i
   if g[0]==pt[i]:av[2]=i
  op=(" Ne pas changer "," Changer plateau"),(" Tout les tours ","   Tour blanc   ","    Tour noir   "),"Tourner plateau"," Tourner blancs"," Tourner noirs ";ca=(op[0][sf.c],op[1][ts])+op[2:];ds=(35,58,135,160,185);dt("<"+ca[0]+">",70,35,CR,CD);dt(ca[1],80,58,CX if sf.c else CU,CD)
  for i in p:i.d(dy=-15)
  for i,v in ee(op[2:]):dt(v,80,135+25*i,CX,CD)
  while 1:
   try:k=gk()
   except O:sf.o();continue
   dt(" "+ca[s]+" ",70,ds[s],CX,CD);s+=(k==2)-(k==1);s%=5
   if s==1 and not sf.c:s+=(k==2)-(k==1)
   if k in(0,3,4):
    if s==0:
     sf.c=not sf.c
     if not sf.c:ts=0;dt(op[1][0],80,ds[1],CU,CD)
     else:dt(op[1][ts],80,ds[1],CX,CD)
    elif s==1:
     ts+=(k==4)+(k==3)-(k==0);ts%=3
     if ts==1:g=sf.ss[1]
     elif ts==2:g=sf.ss[0]
     else:g=sf.b
     for i in rg(4):
      tp=tt[i]
      if g["x"]==tp["x"]and g["y"]==tp["y"]and g["i"]==tp["i"]:av[0]=i
      if g[1]==pt[i]:av[1]=i
      if g[0]==pt[i]:av[2]=i
    else:av[s-2]+=(k==4)+(k==3)-(k==0);av[s-2]%=4
    if ts==1:g=sf.ss[1]
    elif ts==2:g=sf.ss[0]
    else:g=sf.b
    g.update({1:pt[av[1]],0:pt[av[2]]});g.update(tt[av[0]]);se.update(g)
   ca=(op[0][sf.c],op[1][ts])+op[2:]
   for i in p:i.d(dy=-15)
   dt("<"+ca[s]+">",70,ds[s],CR,CD)
 def o(sf):
  d(0,0,320,222,(0,)*3)
  while 1:
   try:gk()
   except(E,K)as e:
    bk()
    if z(e)is O:sf.gm.d();return
 def e(sf,*m):
  q("-"*6+" Error "+"-"*6)
  if m:
   for a in m:q(a)
  else:q("Unknow Error")
  q("-"*19);d(10,70,300,60,CR)
  if m:
   for i,a in ee(m):dt(sr(a),30,75+20*i,CW,CR)
  else:dt("Unknow Error",60,90,CW,CR)
  try:gk()
  except O:sf.o()
  except K:bk()
  except:0
class Z:
 def __init__(sf):
  if not ga(sf,"p",0):sf.s=S(sf)
  sf.w,sf.sd,sf.ms=0,None,[];sf.p=[[C(sf,x,y)for y in rg(8)]for x in rg(8)];sf.pb=[[],[]]
 def __repr__(sf):
  p="/".join([" ".join(map(repr,i))for i in sf.p]);ps="/".join([" ".join(map(repr,sf.pb[i]))for i in(0,1)]);v=" ".join([sr(sf.t),sr(sf.rt),sr(sf.l)]);e="|".join([p,ps,v,sf.pe]);s=""
  for _ in rg(len(e)//200+1):s,e=s+"\""+e[:200]+"\",\n",e[200:]
  return s
LP=250

pe=[
# Coller ici les lignes
# de la partie que vous
# voulez sauvegarder






]