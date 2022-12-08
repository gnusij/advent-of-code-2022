import aoc
d=[sum(map(int,x.split())) for x in aoc.get(2022,1).split('\n\n')]
print(max(d))
print(sum(sorted(d)[::-1][:3]))