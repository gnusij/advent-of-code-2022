class Monkey:
    def __init__(self,mn):
        self.mn = mn
        self.items = []
        self.op = ''
        self.test = 0
        self.tt = 0
        self.tf = 0
        self.i = 0

d = open(0).read().split('\n')
mn = -1
monkeys = []
while d:
    l = d.pop(0)
    if l.startswith("Monkey"):
        monkeys.append(Monkey(mn))
        mn+=1
    if "Starting items" in l:
        monkeys[mn].items = [*map(int, l.split(": ")[1].split(','))]
    if "Operation" in l:
        monkeys[mn].op = l.split(": ")[1].rstrip()
    if "Test: "in l:
        monkeys[mn].test = int(l.split(": ")[1].rstrip().split()[-1])
    if "If true"in l:
        monkeys[mn].tt = int(l.split(": ")[1].rstrip().split()[-1])
    if "If false"in l:
        monkeys[mn].tf = int(l.split(": ")[1].rstrip().split()[-1])

super_modulo = 1
for mon in monkeys:
    super_modulo *= mon.test

for r in range(1,10000+1):

    for mon in monkeys:
        while mon.items:
            mon.i += 1
            old = mon.items.pop(0)
            exec(mon.op)
            item = new % super_modulo
            if item%mon.test == 0:
                monkeys[mon.tt].items.append(item)
            else:
                monkeys[mon.tf].items.append(item)

    if r in [1, 20, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]:
        print(f"Round {r}")
        print([mon.i for mon in monkeys])

I = sorted([mon.i for mon in monkeys])[::-1]
print(I[0]*I[1])