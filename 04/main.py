
def T(d):
    def E(l):
        x = [*map(int,l.split('-'))]
        return {*range(x[0],x[1]+1)}
    return [[*map(E, l.split(','))] for l in d.splitlines()]

def q1(d):
    def S(A,B):
        return A.issubset(B) or B.issubset(A)
    print(sum([1 if S(*s) else 0 for s in d]))

def q2(d):
    print(sum([1 if set.intersection(*s) else 0 for s in d]))

def main():
    import aoc 
    d = T(aoc.get(2022,4))
    q1(d)
    q2(d)

if __name__ == "__main__":
    main()
