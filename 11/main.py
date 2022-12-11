n=0
M=[]
s=1
f=10000
for l in open(0).read().split('Monkey')[1:]:
 l=l.split('\n')
 S=lambda n:l[n].split(":")[1][1:]
 N=lambda n:int(S(n).split()[-1])
 M+=[0,[*map(int,S(1).split(','))],S(2),N(3),N(4),N(5)],
 s*=N(3)
 n+=1
for _ in range(1,f+1):
 for m in M:
  while m[1]:
   m[0]+=1
   old=m[1].pop(0)
   exec(m[2])
   i=new%s
   M[[m[5],m[4]][i%m[3]==0]][1]+=i,
 if _ in [20,f]:
  I=sorted([m[0] for m in M])[::-1]
  print(I[0]*I[1])