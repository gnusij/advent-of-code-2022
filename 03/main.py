import aoc 
d=aoc.get(2022,3).splitlines()
S=lambda l:{*[*l]}
H=lambda l:[l[:len(l)//2],l[len(l)//2:]]
C=lambda*s:sum([ord(c)-96 if c.islower() else ord(c)-38 for c in set.intersection(*s)])
print(sum([C(*map(S,H(l))) for l in d]))
print(sum([C(*map(S,l)) for l in zip(*[iter(d)]*3)]))