import aoc;d=aoc.get(2022,2)
C=lambda o,m:(ord(o)-65,ord(m)-88)
d=[C(*x.split()) for x in d.splitlines()]
print(sum(["0011220120".count(str(o)+str(m))*3+m+1 for o,m in d]),sum([m*3+(o+m-1)%3+1 for o,m in d]))