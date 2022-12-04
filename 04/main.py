
def ex(s):
    x = list(map(int,s.split('-')))
    return set(range(x[0], x[1]+1))

def solution_a(data):
    def d(A,B):
        return A.issubset(B) or B.issubset(A)
    print(sum([1 if d(*map(ex, l)) else 0 for l in data]))


def solution_b(data):
    print(sum([1 if set.intersection(*map(ex, l)) else 0 for l in data]))

def main():
    from aoc import data
    data = [l.split(',') for l in data.splitlines()]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()


