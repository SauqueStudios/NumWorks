from kandinsky import fill_rect as d,draw_string as dt,set_pixel as dp
from math import cos,sin,pi
from time import monotonic as h,sleep as p
ee=enumerate
z=type
r=round
ga=getattr
q=print
it=int
ft=float
sr=str
K=KeyboardInterrupt
E=Exception
rg=range
CCN=222,89,0
CCB=255,219,132
CPN=0,0,0
CPB=255,255,255
CT=165,166,165
se={-1:(1,1),0:(1,1),1:(-1,1),"x":0,"y":0,"i":1}
ii=lambda val:-1<val<8
cf=lambda un,de:1 if un and de and(un.c and not de.c or not un.c and de.c)else 0
def g(x,y):
 if se["x"]:x=7-x
 if se["y"]:y=7-y
 x,y=[x,y][::se["i"]];return[r(60+y*25),r(20+x*25)]
def rd(x,y,r=5,cl=0,v=1):
 if v:x,y=g(x,y)
 x+=13;y+=13;cl=cl or CT
 for i in rg(91):c=cos((i*pi)/180)*r;s=sin((i*pi)/180)*r;d(it(x-c),it(y-s),it(2*c),it(2*s),cl)
def st(x,y,c=25,v=1):
 if v:x,y=g(x,y)
 tt=0
 for i in rg(c):
  if c % 2:t=tt
  for j in rg(c):
   if t:dp(x+i,y+j,CT);t=0
   else:t=1
  if tt:tt=0
  else:tt=1
def m(x,y,pb=None):return {"x":x,"y":y,"pb":pb}
class C:
 dn=[]
 def __init__(sf,gm=None,x=-1,y=-1,c=-1):
  sf.gm,sf.x,sf.y,sf.c=gm,x,y,c;sf.sd=0
 def __bool__(sf):return False if sf.c==-1 else True
 def __repr__(sf):return""
 def d(sf,il=0,ps=None,cl=None,pos=None,jg=0,dy=0):
  ps=ps or se[sf.c];x,y=pos or g(sf.x,sf.y);y+=dy
  if cl is None:d(x,y,25,25,CT)if sf.sd else d(x,y,25,25,[CCN,CCB][(sf.x+sf.y)% 2])
  else:d(x,y,25,25,cl)
  if il:st(sf.x,sf.y)
  if not jg:
   for xb,i in ee(sf.dn[::ps[0]]):
    for yb,j in ee("{0:21b}".format(i)):
     xx,yy=[xb,yb][::ps[1]]
     if j=="1":dp(xx+2+x,yy+2+y,CPB if sf.c else CPN)
class P(C):
 n="";pn=0;ms=()
 def __init__(sf,*a,sl=0,cg=None,**ka):
  sf.sl=sl;super().__init__(*a,**ka)
  if cg:sf.sg(cg)
 def __repr__(sf):a=set(dir(sf));return(sf.n.upper()if sf.c else sf.n)+("," if a else"")+",".join([sr(ga(sf,i))for i in set(dir(sf)).difference(["x","y","c"])if z(ga(sf,i))is it])
 def sg(sf,cg):sf.gt=it(cg[0])
 def tg(sf,x,y):
  if sf.sl:return 1
  r=sf.gm.r[sf.c];xx,yy=sf.x,sf.y;sf.gm.p[sf.x][sf.y]=C(sf.gm,sf.x,sf.y);sf.gm.p[x][y],pc_av=sf,sf.gm.p[x][y];sf.x,sf.y=x,y
  if r.ec():r=0
  else:r=1
  sf.gm.p[xx][yy]=sf;sf.gm.p[x][y]=pc_av;sf.x,sf.y=xx,yy;return r
 def t(sf):
  ms=[]
  for i,j in sf.ms:
   av=1
   while ii(sf.x+av*i)and ii(sf.y+av*j):
    ct=sf.gm.p[sf.x+av*i][sf.y+av*j]
    if not ct:
     if sf.tg(sf.x+av*i,sf.y+av*j):ms.append(m(sf.x+av*i,sf.y+av*j))
    else:
     if cf(ct,sf)and sf.tg(sf.x+av*i,sf.y+av*j):ms.append(m(sf.x+av*i,sf.y+av*j,ct))
     break
    av+=1
  return ms
 def b(sf,mv,sv=1):
  if sv:sf.gm.pe+=sr(sf.x)+sr(sf.y)+":"+sr(mv["x"])+sr(mv["y"])
  sf.gm.vb(mv,sv);sf.gm.p[mv["x"]][mv["y"]]=sf;nc=C(sf.gm,sf.x,sf.y);sf.gm.p[sf.x][sf.y]=nc;sf.x,sf.y=mv["x"],mv["y"];sf.d();nc.d();return nc,sf
 def d(sf,*a,**ka):
  av,se["i"]=se["i"],1 if it(sf.y)!=sf.y else se["i"];super().d(*a,**ka);se["i"]=av
class Q(P):
 n="p";pn=1;dn=[0]*7+[7936,16256]+[32704]*4+[16256,7936]+[3584]*2+[7936,32704]+[131056]*2
 def __init__(sf,*a,**ka):sf.gt=-1;super().__init__(*a,**ka)
 def t(sf):
  ms=[];av=1 if sf.c else -1
  if av==-1 and not sf.y or av==1 and sf.y==7:return ms
  if not sf.gm.p[sf.x][sf.y+av]:
   if sf.tg(sf.x,sf.y+av):ms.append(m(sf.x,sf.y+av))
   if (sf.c and sf.y==1 or not sf.c and sf.y==6) and not sf.gm.p[sf.x][sf.y+2*av]and sf.tg(sf.x,sf.y+2*av):ms.append(m(sf.x,sf.y+2*av))
  for i in -1,1:
   if ii(sf.x+i):
    pt=sf.gm.p[sf.x+i][sf.y+av]
    if cf(sf,pt)and sf.tg(sf.x+i,sf.y+av):ms.append(m(sf.x+i,sf.y+av,pt))
    if sf.c and sf.y==4 or not sf.c and sf.y==3:
     pp=sf.gm.p[sf.x+i][sf.y]
     if z(pp)is Q and pp.gt==sf.gm.rt-1:
      sf.gm.p[sf.x+i][sf.y]=None
      if sf.tg(sf.x+i,sf.y+av):ms.append(m(sf.x+i,sf.y+av,pp))
      sf.gm.p[sf.x+i][sf.y]=pp
  return ms
 def b(sf,mv,sv=1):
  if abs(mv["y"]-sf.y)==2:sf.gt=sf.gm.rt
  if mv["y"]==7 or mv["y"]==0:
   xx,yy=sf.x,sf.y
   if sv:sf.gm.pe+=sr(sf.x)+sr(sf.y)+":"+sr(mv["x"])+sr(mv["y"])
   sf.gm.vb(mv,sv);sf.x,sf.y=mv["x"],mv["y"];sf.sd=1;sf.d();nc=C(sf.gm,xx,yy);sf.gm.p[xx][yy]=nc;nc.sd=1;nc.d()
   try:np=sf.gm.gn(sf)
   except(E,K)as e:
    sf.x,sf.y=xx,yy;sf.gm.p[xx][yy]=sf;sf.sd=0;sf.d();lm=sf.gm.pe.split()[-1]
    if lm.split(":")[2]:
     if sf.c:nc=sf.gm.pb[0].pop();nc.d(cl=CCB,jg=1)
     else:nc=sf.gm.pb[1].pop();nc.d(cl=CCN,jg=1)
    else:nc=C(sf.gm)
    nc.x,nc.y=mv["x"],mv["y"];sf.gm.p[nc.x][nc.y]=nc;nc.d();sf.gm.pe=" ".join(sf.gm.pe.split()[:-1]);raise e
   sf.gm.sc+=(np.pn-1)*(1 if sf.c else -1);np.gt=sf.gt;sf.gm.p[sf.x][sf.y]=np;np.x,np.y=sf.x,sf.y
   if sv:sf.gm.pe+=":"+np.n
   return nc,np
  else:return super().b(mv,sv)
class V(P):
 n="c";pn=3;dn=[0]*4+[15872,16256,16320]+[16368]*4+[16128]*6+[32704,65504]+[262136]*2
 def t(sf):
  ms=[]
  for i in 1,-1,2,-2:
   iii=i;i+=sf.x
   for j in 1,-1,2,-2:
    jjj=j;j+=sf.y
    if abs(iii)!=abs(jjj)and ii(i)and ii(j):
     pt=sf.gm.p[i][j]
     if(not pt or cf(sf,pt))and sf.tg(i,j):ms.append(m(i,j,pt))
  return ms
class F(P):n="f";pn=3;dn=[0,1024,3584,7936]+[16256]*2+[32512,32320,31936,32192]+[32704]*2+[16256]+[7936]*3+[16256]*2+[65504]+[262136]*2;ms=(-1,-1),(-1,1),(1,-1),(1,1)
class T(P):
 n="t";pn=5;dn=[0]*3+[118384]*2+[131056]*3+[32704]+[16256]*8+[32704,65504]+[262136]*2;ms=(0,-1),(0,1),(-1,0),(1,0)
 def __init__(sf,*a,**ka):sf.v=0;super().__init__(*a,**ka)
 def sg(sf,cg):
  if len(cg)==2:super().sg(cg);sf.v=it(cg[1])
  else:sf.v=it(cg[0])
 def b(sf,*a,**ka):
  if not sf.v:sf.v=sf.gm.rt
  return super().b(*a,**ka)
class D(P):n="d";pn=9;dn=[0]*7+[394252,986654,1966071,1638371,1576451,1838599,921102,462364,233016,101936]+[52832]*2+[262136]*2;ms=F.ms+T.ms
N={"p":Q,"c":V,"f":F,"t":T,"d":D}