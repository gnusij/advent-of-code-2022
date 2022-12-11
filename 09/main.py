from time import sleep
import sys
import os

d = open(0).read()

class Grid:
    def __init__(self, l):
        self.x=0 
        self.y=0 
        self.history=set()
        self.chains=[(0,0)]*l
        self.l=l
        self.c=0

    def do(self, inst):
        j,n=inst.split()
        for i in range(int(n)):
            if j=="R": self.x+=1
            elif j=="U": self.y+=1
            elif j=="L": self.x-=1
            elif j=="D": self.y-=1
            
            self.chains[0]=(self.x,self.y)

            if self.c!=0:
                for i in range(1,self.l):
                    self.follow(i)

            if self.chains[-1] not in self.history:
                self.history.add(self.chains[-1])
            self.c+=1

    def follow(self, i):
        a,b=self.chains[i-1]
        A,B=self.chains[i]
        dx = A-a
        dy = B-b
        adx = abs(dx)>1
        ady = abs(dy)>1
        X = [[-1,1][dx>1],0][not adx and ady]
        Y = [[-1,1][dy>1],0][not ady and adx]
        if adx or ady:
            self.chains[i] = (a+X,b+Y)

G=Grid(2)
for inst in d.splitlines():
    G.do(inst)
print(len(G.history))

G=Grid(10)
for inst in d.splitlines():
    G.do(inst)
print(len(G.history))
