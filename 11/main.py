from collections import deque
class Monkey:
    def __init__(self,mn):
        self.mn = mn
        self.items = deque()
        self.op = ''
        self.opn = ''
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
        monkeys[mn].items = deque([*map(int, line.split(": ")[1].split(','))])
    if "Operation" in line:
        monkeys[mn].op = line.split(": ")[1].rstrip()
        monkeys[mn].opn = monkeys[mn].op.split()[-1]
    if "Test: "in line:
        monkeys[mn].test = int(line.split(": ")[1].rstrip().split()[-1])
    if "If true"in line:
        monkeys[mn].testtrue = int(line.split(": ")[1].rstrip().split()[-1])
    if "If false"in line:
        monkeys[mn].testfalse = int(line.split(": ")[1].rstrip().split()[-1])

super_modulo = 1
for mon in monkeys:
    super_modulo *= mon.test

for r in range(1,10000+1):

    for mon in monkeys:
        while mon.items:
            mon.i += 1
            old = mon.items.popleft()
            exec(mon.op)
            item = new % super_modulo
            if item%mon.test == 0:
                monkeys[mon.testtrue].items.append(item)
            else:
                monkeys[mon.testfalse].items.append(item)

    if r in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        print(f"Round {r}")
        print([mon.i for mon in monkeys])

I = sorted([mon.i for mon in monkeys])[::-1]
print(I[0]*I[1])