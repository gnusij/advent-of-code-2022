S=lambda n:l[n].split(":")[1][1:]
N=lambda n:int(S(n).split()[-1])
s,*M=1,
for l in open(0).read().split('Monkey')[1:]:
 l=l.split('\n');M+=[0,[*map(int,S(1).split(','))],S(2).split('=')[1],N(3),N(4),N(5)],;s*=N(3)
def d(r):
 for _ in range(r):
  for m in M:
   while m[1]:m[0]+=1;old=m[1].pop(0);n=eval(m[2]);i=[n//3,n%s][r!=20];M[[m[5],m[4]][i%m[3]==0]][1]+=i,
 a,b=sorted([m[0] for m in M])[::-1][:2]
 print(a*b)
d(20),d(10000)