s=t=0
for o,_,m in open(0).read().split('\n'):
 o,m=ord(o)-65,ord(m)-88
 s+=(m-o+1)%3*3+m+1;t+=m*3+(o+m-1)%3+1
print(s,t)