class Monkey:
    def __init__(self,mn):
        self.mn = mn
        self.items = []
        self.op = ''
        self.test = 0
        self.testtrue = 0
        self.testfalse = 0
        self.i = 0

                


#import aoc;d=aoc.get(2022,11)
d=open(0).read()


d = d.split('\n')
mn = -1
monkeys = []
while d:
    line = d.pop(0)
    #print(line)
    if line.startswith("Monkey"):
        mn+=1
        monkeys.append(Monkey(mn))
    if "Starting items" in line:
        monkeys[mn].items = [*map(int, line.split(": ")[1].split(','))]
    if "Operation" in line:
        monkeys[mn].op = line.split(": ")[1].rstrip()
    if "Test: "in line:
        monkeys[mn].test = int(line.split(": ")[1].rstrip().split()[-1])
    if "If true"in line:
        monkeys[mn].testtrue = int(line.split(": ")[1].rstrip().split()[-1])
    if "If false"in line:
        monkeys[mn].testfalse = int(line.split(": ")[1].rstrip().split()[-1])

for r in range(1,20+1):

    for mon in monkeys:
        while mon.items:
            mon.i += 1
            item = mon.items.pop(0)
            old = item
            exec(mon.op)
            #item = new//3
            if item%mon.test == 0:
                monkeys[mon.testtrue].items.append(item)
            else:
                monkeys[mon.testfalse].items.append(item)

I = sorted([mon.i for mon in monkeys])[::-1]
print(I[0]*I[1])