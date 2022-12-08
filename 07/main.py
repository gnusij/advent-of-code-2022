import aoc 
d=[d.split() for d in aoc.get(2022,7).split("$ ")[1:]][1:]
o=p='/';F,D={},{};V='..'
f=lambda p,v=V:p[:p[:-1].rfind('/')+1] if v==V else p+v+o
for c in d:
 if c[0]!='cd':
  while~-len(c):
    *c,s,n=c
    if s!='dir':F[p+n]=int(s)
 else:p=f(p,c[1])
 D[p]=0
for p in F:
 d=p
 while d:=f(d):
  D[d]+=F[p]
  if d==o:break
print(sum([D[p] for p in D if D[p]<=100000]))
print(min([D[p] for p in D if D[p]>=30000000-70000000+D[o]]))