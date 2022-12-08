def E(l):
 x,y = [*map(int,l.split('-'))]
 return {*range(x,y+1)}
import aoc 
d=[[*map(E, l.split(','))] for l in aoc.get(2022,4).splitlines()]
print(sum([1 if a.issubset(b) or b.issubset(a) else 0 for a,b in d]))
print(sum([1 if set.intersection(*s) else 0 for s in d]))