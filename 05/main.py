import re

def T(d):
    I = [[*map(int, re.findall(r'\d+',s))] for s in d[1].splitlines()]
    B = [[s[x] for x in range(1,len(s),4)] for s in d[0].splitlines()]
    B = [[x for x in b if x != ' '] for b in [*map(list, zip(*B[:-1][::-1]))]]
    return I, B

def p(B):
    print(''.join([b[-1] for b in B]))

def q1(I, B):
    for n, c1, c2 in I:
        [B[c2-1].append(B[c1-1].pop()) for i in range(n)]
    p(B)

def q2(I, B):
    for n, c1, c2 in I:
        B[c2-1].extend([B[c1-1].pop() for i in range(n)][::-1])
    p(B)

def main():
    import aoc 
    d = aoc.get(2022,5).split('\n\n')
    q1(*T(d))
    q2(*T(d))

if __name__ == "__main__":
    main()

