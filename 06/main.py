import aoc;d=aoc.get(2022,6)
def f(d,n): 
 i=0
 while not len({*d[i:i+n]})==n:i+=1
 print(i+n)
f(d,4)
f(d,14)