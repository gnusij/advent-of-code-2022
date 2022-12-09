import aoc;d=aoc.get(2022,9)
from time import sleep
import sys
import os

class Grid:
    def __init__(self, l):
        self.x=0 # current
        self.y=0 # current
        self.history=set()
        self.chains=[(0,0)]*l
        self.l=l
        self.c=0

    def show(self):
        print(f"{self.chains}")
                
    def show_visited(self):
        xmax = max(max([x[0] for x in self.history]),max([x[0] for x in self.chains]))
        ymax = max(max([x[1] for x in self.history]),max([x[1] for x in self.chains])) 
        xmin = min(min([x[0] for x in self.history]),min([x[0] for x in self.chains]),0)
        ymin = min(min([x[1] for x in self.history]),min([x[1] for x in self.chains]),0)
        S = [['.']*(xmax+abs(xmin)+1) for i in range(ymax+abs(ymin)+1)]
        for n in self.history:
            x,y=n
            S[y+abs(ymin)][x+abs(xmin)]='#'
        S[abs(ymin)][abs(xmin)]='s'
        [print(''.join(s)) for s in S[::-1]]

    def show_chains(self):
        xmax = max(max([x[0] for x in self.history]),max([x[0] for x in self.chains]))
        ymax = max(max([x[1] for x in self.history]),max([x[1] for x in self.chains])) 
        xmin = min(min([x[0] for x in self.history]),min([x[0] for x in self.chains]),0)
        ymin = min(min([x[1] for x in self.history]),min([x[1] for x in self.chains]),0)
        S = [['.']*(xmax+abs(xmin)+1) for i in range(ymax+abs(ymin)+1)]
        for i,n in enumerate(self.chains):
            if i == 0:
                t = 'H'
            else:
                t = str(i)
            x,y=n
            S[y+abs(ymin)][x+abs(xmin)]=t
        S[abs(ymin)][abs(xmin)]='s'
        
        os.system("clear")
        print('\n')
        [print(''.rjust(20)+''.join(s)) for s in S[::-1] ]
        sleep(0.01)
                
    def do(self, inst):
        j,n=inst.split()
        #print(f"== {j} {n} ==")
        for i in range(int(n)):
            if j=="R":
                self.x+=1
            elif j=="U":
                self.y+=1
            elif j=="L":
                self.x-=1
            elif j=="D":
                self.y-=1
            self.chains[0]=(self.x,self.y)
            if self.c!=0:
                for ind in range(1,self.l):
                    self.follow(ind)
            if self.chains[-1] not in self.history:
                self.history.add(self.chains[-1])
            self.c+=1
            #print()
            #self.show_chains()

    def follow(self, ind):
        x1=self.chains[ind-1][0]
        y1=self.chains[ind-1][1]
        x2=self.chains[ind][0]
        y2=self.chains[ind][1]
        if abs(x2-x1)>1 and abs(y2-y1)>1:
            if (x2>x1 and x2-x1>1) and (y2>y1 and y2-y1>1):
                self.chains[ind] = (x1+1,y1+1)
            elif not (x2>x1 and x2-x1>1) and (y2>y1 and y2-y1>1):
                self.chains[ind] = (x1-1,y1+1)
            elif (x2>x1 and x2-x1>1) and not (y2>y1 and y2-y1>1):
                self.chains[ind] = (x1+1,y1-1)
            else:
                self.chains[ind] = (x1-1,y1-1)
        elif abs(x2-x1)>1:
            if x2>x1 and x2-x1>1:
                self.chains[ind] = (x1+1,y1)
            else:
                self.chains[ind] = (x1-1,y1)
        elif abs(y2-y1)>1:
            if y2>y1 and y2-y1>1:
                self.chains[ind] = (x1,y1+1)
            else:
                self.chains[ind] = (x1,y1-1)
def printG(G):
    [print(g) for g in G]

#d="""R 4
#U 4
#L 3
#D 1
#R 4
#D 1
#L 5
#R 2"""
#d="""R 5
#U 8
#L 8
#D 3
#R 17
#D 10
#L 25
#U 20
#"""

G=Grid(10)
for inst in d.splitlines():
    G.do(inst)
G.show_visited()
print(len(G.history))
