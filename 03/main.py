
def S(l):
    return {*[*l]}

def C(*s):
    return sum([ord(c)-96 if c.islower() else ord(c)-38 for c in set.intersection(*s)])

def q1(d):
    def H(l):
        h = len(l)//2
        return [l[:h], l[h:]]
    print(sum([C(*map(S, H(l))) for l in d]))

def q2(d):
    print(sum([C(*map(S, l)) for l in zip(*[iter(d)]*3)]))

def main():
    import aoc 
    d = aoc.get(2022,3).splitlines()
    q1(d)
    q2(d)

if __name__ == "__main__":
    main()

