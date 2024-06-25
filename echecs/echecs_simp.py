from parties_echecs_simp import *
class Y(Z):
 def st(sf,o=1):
  sf.__init__();sf.p=[[C(sf,x,y)for y in rg(8)]for x in rg(8)];sf.Y=[None]*2;sf.pb=[[],[]];sf.t=1;sf.rt=0;sf.sc=0;sf.l=0;sf.pe=""
  for x in rg(8):sf.p[x][1]=Q(sf,x,1,1);sf.p[x][6]=Q(sf,x,6,0)
  for n in -1,1:sf.p[it(3.5+3.5*n)][0]=T(sf,it(3.5+3.5*n),0,1);sf.p[it(3.5+3.5*n)][7]=T(sf,it(3.5+3.5*n),7,0);sf.p[it(3.5+2.5*n)][0]=V(sf,it(3.5+2.5*n),0,1);sf.p[it(3.5+2.5*n)][7]=V(sf,it(3.5+2.5*n),7,0);sf.p[it(3.5+1.5*n)][0]=F(sf,it(3.5+1.5*n),0,1);sf.p[it(3.5+1.5*n)][7]=F(sf,it(3.5+1.5*n),7,0)
  sf.p[3][0]=D(sf,3,0,1);sf.p[3][7]=D(sf,3,7,0);sf.p[4][0]=R(sf,4,0,1,sf.p[0][0],sf.p[7][0]);sf.p[4][7]=R(sf,4,7,0,sf.p[0][7],sf.p[7][7]);sf.r=[sf.p[4][7],sf.p[4][0]]
  if o:sf.m()
 def sw(sf,o=1):
  sf.__init__();cg=sum(pe,"")
  try:
   sf.p=[[C(sf,x,y)for y in rg(8)]for x in rg(8)];sf.Y=[None]*2;sf.pb=[[],[]];sf.r=[None,None];sf.sc=0;p,ff,v,sf.pe=cg.split("|")
   for x,l in ee(p.split("/")):
    for y,o in ee(l.split(" ")):
     if o:
      a=o.split(",");np=N[a[0].lower()](sf,x,y,a[0]not in N,cg=a[1:])
      if z(np)is R:sf.r[a[0]not in N]=np
      else:sf.sc+=np.pn*(1 if np.c else -1)
      sf.p[x][y]=np
   for i,lst in ee(ff.split("/")):
    for j,pc in ee(lst.split()):pc=pc.split(",");sf.pb[i].append(N[pc[0].lower()](sf,j%8,8.3+(j//8)if i else -1.3-(j//8),i,cg=pc[1:]))
   for o in sf.r:
    xx,yy=o.bt
    if yy==it(yy):xx,yy=it(xx),it(yy);o.bt=sf.p[xx][yy]
    else:
     if o.c:o.bt=sf.pb[1][it(xx+8*(yy==-2.3))]
     else:o.bt=sf.pb[0][it(xx+8*(yy==9.3))]
    xx,yy=o.tb
    if yy==it(yy):xx,yy=it(xx),it(yy);o.tb=sf.p[xx][yy]
    else:
     if o.c:o.tb=sf.pb[1][it(xx+8*(yy==-2.3))]
     else:o.tb=sf.pb[0][it(xx+8*(yy==9.3))]
   sf.t,sf.rt,sf.l=map(it,v.split())
  except E as e:sf.s.e("Erreur chargement partie :"," La partie est corrompue" if cg else " La partie n'existe pas",repr(e));return sf.st(o)
  if o:sf.m()
 def sa(sf):
  try:
   sf.d()
   while 1:
    try:sf.s.h()
    except(H,K):bk()
  except J:
   if ga(sf,"r",0)and all(sf.r):q("Pour sauvegarder la partie,\ncopiez les lignes suivantes et\ncollez-les entres les crochets\ndans le script parties_echecs");q(gm)
 def gs(sf):return [j for i in sf.p for j in i if(j.c==sf.t and j.t())]
 def vb(sf,mv,sv=1):
  if mv["pb"]:
   if sv:sf.pe+=":"+mv["pb"].n+sr(mv["pb"].x)+sr(mv["pb"].y)
   nc=C(sf,mv["pb"].x,mv["pb"].y);sf.p[mv["pb"].x][mv["pb"].y]=nc;nc.d();lb=len(sf.pb[mv["pb"].c]);mv["pb"].x=lb % 8
   if not mv["pb"].c:mv["pb"].y=-1.3-(lb//8);mv["pb"].d(cl=CCB,ps=se[1])
   else:mv["pb"].y=8.3+(lb//8);mv["pb"].d(cl=CCN,ps=se[0])
   sf.pb[mv["pb"].c].append(mv["pb"]);sf.sc+=mv["pb"].pn*(-1 if mv["pb"].c else 1)
  elif sv:sf.pe+=":"
 def ve(sf):
  try:gk(1)
  except(O):sf.s.o()
 def d(sf):
  if se["y"]:c1,c2=CCN,CCB
  else:c1,c2=CCB,CCN
  d(0,0,59,222,c1);d(261,0,59,222,c2)
  for i in sf.pb[0]:sf.ve();i.d(cl=CCB,ps=se[1])
  for i in sf.pb[1]:sf.ve();i.d(cl=CCN,ps=se[0])
  d(59,0,202,19,CD);dt("ECHECS by Caucaucybu",60,0,CX,CD);d(59,19,202,203,CX)
  for i in sf.p:
   for j in i:sf.ve();j.d()
  sf.ve()
  if sf.ms:
   for sp in sf.ms:rd(sp["x"],sp["y"])
   st(*sf.sd)
  elif sf.sd:x,y=sf.sd;sf.p[x][y].d(il=1)
 def gn(sf,pc):
  if sf.w:return sf.pp
  if pc.c:
   ck=CCN;ps=[D(sf,2,4,1),V(sf,3,4,1),T(sf,4,4,1),F(sf,5,4,1)];pt=[[C(sf,i,j)for j in rg(8)]for i in rg(8)]
   for i in ps:pt[i.x][i.y]=i
   x,y=g(2,4)[::se["i"]]
  else:
   ck=CCB;ps=[D(sf,2,3,0),V(sf,3,3,0),T(sf,4,3,0),F(sf,5,3,0)];pt=[[C(sf,i,j)for j in rg(8)]for i in rg(8)]
   for i in ps:pt[i.x][i.y]=i
   x,y=g(2,3)[::se["i"]]
  if se["y"]:d(*[x+30,y+30][::se["i"]]+[-35,-25*4-10][::se["i"]]+[ck])if se["x"]else d(*[x+30,y-5][::se["i"]]+[-35,25*4+10][::se["i"]]+[ck])
  else:d(*[x-5,y+30][::se["i"]]+[35,-25*4-10][::se["i"]]+[ck]) if se["x"]else d(*[x-5,y-5][::se["i"]]+[35,25*4+10][::se["i"]]+[ck])
  for i in ps:sf.ve();i.d(cl=ck)
  xx,yy=ps[0].x,ps[0].y;ps[0].d(cl=ck,il=1);k=-1
  try:
   while k!=4:
    try:k=gk(g=1)
    except O:
     sf.s.o()
     if se["y"]:d(*[x+30,y+30][::se["i"]]+[-35,-25*4-10][::se["i"]]+[ck])if se["x"]else d(*[x+30,y-5][::se["i"]]+[-35,25*4+10][::se["i"]]+[ck])
     else:d(*[x-5,y+30][::se["i"]]+[35,-25*4-10][::se["i"]]+[ck]) if se["x"]else d(*[x-5,y-5][::se["i"]]+[35,25*4+10][::se["i"]]+[ck])
     for i in ps:sf.ve();i.d(cl=ck)
     pt[xx][yy].d(cl=ck,il=1);continue
    lx,ly=xx,yy;xx,yy=sm(pt,xx,yy,k);pt[lx][ly].d(cl=ck);pt[xx][yy].d(cl=ck,il=1)
  except(Fw,Bk,K)as e:bk();[(sf.ve(),sf.p[i][j].d())for i in rg(1,7)for j in rg(2,6)];raise e
  [(sf.ve(),sf.p[i][j].d())for i in rg(1,7)for j in rg(2,6)];return pt[xx][yy]
 def f(sf):
  dt(" "*5,265-260*se["y"],2,CW,CCN);dt(" "*5,5+260*se["y"],2,CW,CCB)
  if sf.s.sc and sf.sc:
   if sf.sc>0:dt(" +"+("" if sf.sc//10 else " ")+sr(sf.sc),5+260*se["y"],2,CX,CCB)
   else:dt(" +"+("" if sf.sc//10 else " ")+sr(abs(sf.sc)),265-260*se["y"],2,CX,CCN)
  if sf.s.w:
   if sf.t:
    if sf.r[1].ec():dt("ECHEC",5+260*se["y"],2,CW,CCB)
   else:
    if sf.r[0].ec():dt("ECHEC",265-260*se["y"],2,CW,CCN)
  sa=[],[]
  for lign in sf.p:
   for o in lign:
    if o:sa[o.c].append(o.n)
  r=""
  if len(sa[0])==len(sa[1])==1:r="NULLE"
  else:
   for i,j in(1,0),(0,1):
    if len(sa[i])==1:
     if len(sa[j])==3 and sa[j].count("c")==2:r="NULLE"
     elif len(sa[j])==2 and("c" in sa[j]or "f" in sa[j]):r="NULLE"
  if not sf.gs():r=" PAT "
  if sf.r[sf.t].ec()and r==" PAT ":
   if sf.t:dt(" MAT ",5+260*se["y"],2,CW,CCB)
   else:dt(" MAT ",265-260*se["y"],2,CW,CCN)
  else:dt(r,265-260*se["y"],2,CW,CCN);dt(r,5+260*se["y"],2,CW,CCB)
  return r+" "
 def fw(sf):
  for i in sf.Y:
   if i!=None:i.sd=0;i.d()
  if len(sf.pe.split())==sf.rt-sf.l:return
  if sf.t:sf.t=0
  else:sf.t=1
  nv=sf.pe.split()[sf.rt-sf.l].split(":");dx,dy=map(it,nv[0]);ax,ay=map(it,nv[1]);pe=sf.p[dx][dy]
  if nv[2]:xx,yy=map(it,nv[2][1:]);pf=sf.p[xx][yy]
  else:pf=None
  try:sf.pp=N[nv[3]](sf,ax,ay,pe.c);sf.w=1
  except IndexError:0
  sf.Y=pe.b(m(ax,ay,pf),sv=0);sf.w=0;sf.rt+=1
 def kb(sf):
  if sf.rt-sf.l:sf.rt-=1
  else:return
  if sf.t:sf.t=0
  else:sf.t=1
  lv=sf.pe.split()[sf.rt-sf.l].split(":");dx,dy=map(it,lv[0]);ax,ay=map(it,lv[1]);pc=sf.p[ax][ay];pc.x,pc.y=dx,dy;sf.p[dx][dy]=pc;pc.sd=0;pc.d();nc=C(sf,ax,ay);sf.p[ax][ay]=nc;nc.sd=0;nc.d()
  try:
   if lv[3]:sf.sc-=(N[lv[3]].pn-1)*(1 if sf.t else -1);np=Q(sf,dx,dy,pc.c);np.gt=pc.gt;sf.p[dx][dy]=np;np.d()
  except IndexError:0
  if lv[2]:
   if pc.c:pf=sf.pb[0].pop()
   else:pf=sf.pb[1].pop()
   pf.d(jg=1,cl=CCN if pf.c else CCB);sf.sc-=pf.pn*(-1 if pf.c else 1);pf.x,pf.y=map(it,lv[2][1:]);sf.p[pf.x][pf.y]=pf;pf.d()
  if z(pc)is Q:
   if abs(dx-ax)==2:pc.gt=0
  elif z(pc)is R:
   if sf.rt==pc.v:pc.v=0
   if dx-ax==2:t=pc.bt;t.x=0;t.v=0;sf.p[t.x][t.y]=t;t.d();sf.p[ax+1][t.y]=C(sf,ax+1,ay);sf.p[ax+1][t.y].d()
   elif ax-dx==2:
    t=pc.tb;t.x=7;t.v=0;sf.p[t.x][t.y]=t;t.d();sf.p[ax-1][t.y]=C(sf,ax-1,ay);sf.p[ax-1][t.y].d()
  elif z(pc)is T:
   if pc.v==sf.rt:pc.v=0
  if sf.rt-sf.l:lv=sf.pe.split()[sf.rt-sf.l-1].split(":");dx,dy=map(it,lv[0]);ax,ay=map(it,lv[1]);sf.Y=[sf.p[dx][dy],sf.p[ax][ay]]
  else:sf.Y=[None]*2
  sf.f()
 def m(sf):
  if not ga(sf,"r",0)or not all(sf.r):sf.sw(0)
  if not sf.s.c:sf.d()
  while 1:
   if sf.f()==" PAT " and sf.s.c:se.update(sf.s.b);sf.d()
   elif sf.s.c:se.update(sf.s.ss[sf.t]);sf.d()
   while sf.f():
    for i in sf.Y:
     if i!=None:i.sd=1;i.d()
    ps=sf.gs()
    if ps:
     pt=[[C(i,j)for j in rg(8)]for i in rg(8)]
     for i in ps:pt[i.x][i.y]=i
     x,y=ps[0].x,ps[0].y;ps[0].d(il=1);sf.sd=x,y
    k=-1
    try:
     while k!=4:
      try:k=gk(g=1)
      except O:sf.s.o();continue
      if ps:lx,ly=x,y;x,y=sm(pt,x,y,k);sf.sd=x,y;sf.p[lx][ly].d();sf.p[x][y].d(il=1)
    except(Bk,Fw)as e:
     if ps:sf.p[x][y].d()
     sf.sd=None
     if z(e)is Bk:sf.kb()
     else:sf.fw()
     continue
    pd=sf.p[x][y];pd.sd=1;pd.d()
    for i in sf.Y:
     if i is not None:i.sd=0;i.d()
    ms=pd.t();sf.ms=ms;mt=[[0]*8 for i in rg(8)]
    for i in ms:mt[i["x"]][i["y"]]=i;rd(i["x"],i["y"])
    k=-1;x,y=ms[0]["x"],ms[0]["y"];sf.sd=x,y;st(x,y)
    try:
     while k!=4:
      try:k=gk(g=1)
      except O:sf.s.o();continue
      lx,ly=x,y;x,y=sm(mt,x,y,k);sf.sd=x,y;sf.p[lx][ly].d();rd(lx,ly);st(x,y)
     sf.sd=None;sf.ms=[]
     for i in ms:sf.ve();sf.p[i["x"]][i["y"]].d()
     sf.pe=" ".join(sf.pe.split()[:sf.rt-sf.l]);sf.pe+=" "
     if sf.pe.startswith(" "):sf.pe=sf.pe[1:]
     if len(sf.pe)>LP:
      ib=0;dec=0
      while len(sf.pe)-ib>LP:
       ib+=1
       if sf.pe[ib]==" ":dec+=1
      while sf.pe[ib]!=" ":
       ib+=1
       if sf.pe[ib]==" ":dec+=1;break
      sf.l+=dec;sf.pe=sf.pe[ib+1:]
     sf.Y=pd.b(mt[x][y])
    except(K,Bk,Fw)as e:
     bk();sf.sd=None;sf.ms=[]
     for i in ms:sf.ve();sf.p[i["x"]][i["y"]].d()
     pd.sd=0;pd.d()
     if z(e)is Bk:sf.kb()
     elif z(e)is Fw:sf.fw()
     continue
    sf.rt+=1
    if sf.t:sf.t=0
    else:sf.t=1
    break
gm=Y();gm.sa()