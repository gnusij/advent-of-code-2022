d = open(0).read()
x=y=0
t=0,0
h,H,c,C={t},{t},[t]*2,[t]*10
def m(c):
 for i in range(1,len(c)):
  a,b=c[i-1];A,B=c[i];d=A-a;D=B-b;u=abs(d)>1;v=abs(D)>1;c[i]=[A,[[a-1,a+1][d>1],a][~u+2 and v]][u or v],[B,[[b-1,b+1][D>1],b][~v+2 and u]][u or v]
 return c
for i in d.split('\n'):
 j,n=i.split()
 for k in range(int(n)):
  if j=="R":x+=1
  elif j=="U":y+=1
  elif j=="L":x-=1
  else:y-=1
  c[0]=C[0]=x,y;c=m(c);C=m(C)
  if{c[-1]}-h:h.add(c[-1])
  if{C[-1]}-H:H.add(C[-1])
print(len(h),len(H))