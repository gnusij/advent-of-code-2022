def f(d,n): 
 i:=0 while not len({*d[i:i+n]})==n: i+=1
 print(i+n)
import aoc 
d=aoc.get(2022,6).strip()
f(d,4)
f(d,14)