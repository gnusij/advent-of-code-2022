import aoc 

d=[d.split() for d in aoc.get(2022,7).strip().split("$ ")[1:]][1:]
o=p='/';F={};D={}
f=lambda p,n: o.join(p.split(o)[:-n])+o
for c in d:
    if c[0]=='cd' and c[1]=='..':
        p = f(p,2)
    elif c[0]=='cd':
        p += c[1]+o
    elif c[0]=='ls':
        i=1
        while i<len(c):
            if c[i] != 'dir':
                F[p+c[i+1]] = int(c[i])
            i+=2
    if p not in D: D[p]=0

for p in F:
    d = f(p,1)
    while d:
        D[d] += F[p]
        if d==o: break
        d = f(d,2)
print(sum([D[d] for d in D if D[d]<=100000]))
print(min([D[p] for p in D if D[p]>=30000000-70000000+D[o]]))