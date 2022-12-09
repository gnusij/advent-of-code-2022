import aoc;d=aoc.get(2022,1)
d=[sum(map(int,x.split())) for x in d.split('\n\n')]
print(max(d),sum(sorted(d)[::-1][:3]))