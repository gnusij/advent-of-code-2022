
def T(d):
    def e(l):
        x = [*map(int,l.split('-'))]
        return {*range(x[0],x[1]+1)}
    return [[*map(e, l.split(','))] for l in d.splitlines()]

def solution_a(data):
    def d(A,B):
        return A.issubset(B) or B.issubset(A)
    print(sum([1 if d(*s) else 0 for s in T(data)]))

def solution_b(data):
    print(sum([1 if set.intersection(*s) else 0 for s in T(data)]))

def main():
    from aoc import data
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()


