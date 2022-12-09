import aoc;d=aoc.get(2022,5) 
T=lambda b:[[x for x in b if x!=' '] for b in [*zip(*[[*x[1::4]] for x in b.splitlines()][:-1][::-1])]]
L=lambda B:''.join([b[-1] for b in B])
b,i=d.split('\n\n')
B,M=T(b),T(b)
for n,x,y in zip(*[iter(map(int,i.split()[1::2]))]*3):
 l=[]
 for i in range(n):
  B[y-1]+=B[x-1].pop()
  l+=M[x-1].pop()
 M[y-1].extend(l[::-1])
print(L(B),L(M))