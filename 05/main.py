"""
TODO: prolly cleaner to have boxes in reverse order
"""
    
import re

def T(d):
    ins = [[*map(int, re.findall(r'\d+',s))] for s in d.split('\n\n')[1].splitlines()]
    crt = [[s[x] for x in range(1,len(s),4)] for s in d.split('\n\n')[0].splitlines()[:-1]]
    return ins, crt 

def print_crates(C):
    " for debugging "
    print()
    [print(c) for c in C]

def find_top(c, n):
    for i in range(len(c)): 
        if c[i][n] != ' ':
            return c[i][n]

def find_top_ind(c, n):
    for i in range(len(c)):
        if c[i][n] != ' ':
            return i
    return len(c)

def print_top_crate_letters(c):
    print(''.join([find_top(c,i) for i in range(len(c[0]))]))

def move_one(c, f, t):
    dest_ind = find_top_ind(c, t)-1
    if dest_ind < 0:
        c.insert(0, [' ']*len(c[0]))
        dest_ind = 0
    orig_ind = find_top_ind(c, f)
    c[dest_ind][t] = str(c[orig_ind][f])
    c[orig_ind][f] = ' '
    return c

def move_n(c, n, f, t):
    dest_ind = find_top_ind(c, t)-n
    orig_ind = find_top_ind(c, f)
    if dest_ind < 0:
        for i in range(abs(dest_ind)):
            c.insert(0, [' ']*len(c[0]))
            dest_ind += 1
            orig_ind += 1
    
    for i in range(n):
        j = dest_ind+i
        c[j][t] = str(c[orig_ind+i][f])
        c[orig_ind+i][f] = ' '
    return c

def q1(d):
    I, C = T(d)
    for i in I:
        for j in range(i[0]):
            C = move_one(C, i[1]-1, i[2]-1)
    print_top_crate_letters(C)

def q2(d):
    I, C = T(d)
    for i in I:
        C = move_n(C, i[0], i[1]-1, i[2]-1)
    print_top_crate_letters(C)

def main():
    import aoc 
    d = aoc.get(2022,5)
    q1(d)
    q2(d)

if __name__ == "__main__":
    main()

