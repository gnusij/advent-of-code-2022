import aoc;d=aoc.get(2022,2)
s=t=0
for x in d.splitlines():
 o,_,m=x
 o,m=ord(o)-65,ord(m)-88
 s+="0011220120".count(str(o)+str(m))*3+m+1
 t+=m*3+(o+m-1)%3+1
print(s,t)