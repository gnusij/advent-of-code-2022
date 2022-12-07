import aoc 

d=[d.split() for d in aoc.get(2022,7).strip().split("$ ")[1:]][1:]
o=p='/';F={};D={}
f=lambda p: p[:p[:-1].rfind('/')+1]
for c in d:
    if c[1]=='..':
        p = f(p)
    elif c[0]=='cd':
        p += c[1]+o
    elif c[0]=='ls':
        while len(c)>1:
            n,s=[c.pop() for i in [0,1]]
            if s!='dir':
                F[p+n]=int(s)
    if p not in D: D[p]=0

for p in F:
    d = f(p)
    while d:
        D[d] += F[p]
        if d==o: break
        d = f(d)
print(sum([D[p] for p in D if D[p]<=100000]))
print(min([D[p] for p in D if D[p]>=30000000-70000000+D[o]]))