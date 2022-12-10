
class Program:
    def __init__(self):
        self.X = 1
        self.cycle = 1
        self.signal_strength = 0
        self.queue = []
        self.proc = None
        self.CRT = [['.' for i in range(40)] for j in range(6)]

    def show(self):
        [print(''.join(c)) for c in self.CRT]

    def read(self, d):
        for inst in d.split('\n'):
            if inst == 'noop':
                self.queue.append([inst, 1])
            else:
                self.queue.append([inst, 2])

    def do(self, d):
        self.read(d)
        print(self.queue)
        while True:
            # Beggining cycle
            if not self.proc:
                self.proc = self.queue.pop(0)
                #print("BEGIN of", self.cycle, "  X:", self.X, "PROC:", self.proc)

            # During cucle
            if self.proc:
                inst,c = self.proc
                # signal_strength
                if (self.cycle-20)%40 == 0:
                    print(f"At cycle {self.cycle} X is {self.X} score {self.cycle * self.X}")
                    self.signal_strength += self.cycle * self.X

                # draw
                y,x = self.cycle//40, self.cycle%40-1
                print(self.cycle, (x, y), self.X)
                if x in [self.X-1, self.X, self.X+1]:
                    self.CRT[y][x]='#' 
            
                # Finish
                if c == 1:
                    if inst != "noop":
                        self.X += int(inst.split()[1])
                        self.proc = None
                    else:
                        self.proc = None
                else:
                    self.proc = [inst, c-1]

            if not self.queue and not self.proc:
                print(f"Finished {self.signal_strength}")
                self.show()
                break
            self.cycle += 1

import aoc;d=aoc.get(2022,10)
d = d.rstrip()
p = Program()
p.do(d)