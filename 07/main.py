class Dir:
    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.s = 0

class File:
    def __init__(self, p, s, n):
        self.p = p
        self.s = s
        self.n = n

global DIRS
global FILES
DIRS = {}
FILES = {}

def get(d, cwd):
    global DIRS
    global FILES 

    for cmd in d:
        if cmd.startswith('$'):
            break
        elif cmd.startswith('dir'):
            n = cmd.split()[1]
            if cwd not in DIRS:
                DIRS[cwd] = Dir(cwd, n)
        else:
            s = int(cmd.split()[0])
            n = cmd.split()[1]
            FILES[cwd+n] = File(cwd, s, n)

def q1(d):
    cwd = '/'
    for i in range(1, len(d)):
        if d[i].startswith('$ cd ..'):
            cwd = '/'.join(cwd.split('/')[:-2]) + '/'
        elif d[i].startswith('$ cd'):
            n = d[i].split()[2]
            cwd += n +'/'
        elif d[i].startswith('$ ls'):
            get(d[i+1:], cwd)
        if cwd not in DIRS:
            DIRS[cwd] = Dir(cwd, n)

    for f in FILES:
        d = FILES[f].p
        while True:
            DIRS[d].s += FILES[f].s
            if d == '/':
                break
            d = '/'.join(d.split('/')[:-2]) + '/'
    s=0
    for d in DIRS:
        if DIRS[d].s <= 100000:
            s+=DIRS[d].s
    print(s)


def q2(d):
    x = 30000000 - 70000000 + DIRS['/'].s
    print(min([DIRS[d].s for d in DIRS if DIRS[d].s >= x]))


import aoc 
d=aoc.get(2022,7).strip()
d = d.splitlines()
q1(d)
q2(d)

