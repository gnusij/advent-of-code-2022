import aoc;d=aoc.get(2022,4)
def E(l):
 x,y=map(int,l.split('-'))
 return{*range(x,y+1)}
s=t=0
for l in d.split():
 a,b=map(E,l.split(','))
 if a.issubset(b)|b.issubset(a):s+=1
 if set.intersection(a,b):t+=1
print(s,t)