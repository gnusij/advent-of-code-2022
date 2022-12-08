import aoc
import math
d=[[*map(int, d)] for d in aoc.get(2022,8).splitlines()]
r,w,h,v,*s=range,len(d[0]),len(d),0,
D=lambda x,y:d[y][x]
L=lambda x,y:[[D(i,y) for i in r(x+1,w)],[D(i,y) for i in r(x)][::-1],[D(x,j) for j in r(y)][::-1],[D(x,j) for j in r(y+1,h)]]
V=lambda x,y:[[1 if v<D(x,y) else 0 for v in u] for u in L(x,y)]
S=lambda x,y:[len(a) if all(a) else a.index(0)+1 for a in V(x,y)]
for y in r(1,h-1):
 for x in r(1,w-1):
  v+=any([all(s) for s in V(x,y)])
  s+=[math.prod(S(x,y))]
print((h+w)*2-4+v)
print(max(s))