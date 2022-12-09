import aoc;d=aoc.get(2022,8)
import math
d=[[*map(int,d)] for d in d.splitlines()]
r,w,h,v,*s=range,len(d[0]),len(d),0,
D=lambda x,y:d[y][x]
for y in r(1,h-1):
 for x in r(1,w-1):
  V=[[v<D(x,y) for v in u] for u in [[D(i,y) for i in r(x+1,w)],[D(i,y) for i in r(x)][::-1],[D(x,j) for j in r(y)][::-1],[D(x,j) for j in r(y+1,h)]]]
  S=[len(a) if all(a) else-~a.index(0) for a in V]
  v+=any([all(s) for s in V])
  s+=[math.prod(S)]
print((h+w)*2-4+v,max(s))