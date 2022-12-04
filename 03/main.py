
def c(*s):
    def calc(c):
        return ord(c)-96 if c.islower() else ord(c)-38
    return sum([calc(c) for c in set.intersection(*s)])


def solution_a(data):
    def s(l):
        h = len(l)//2
        return [l[:h], l[h:]]
    print(sum([c(*map(lambda x: set(list(x)), s(l))) for l in data]))


def solution_b(data):
    print(sum([c(*map(lambda x: set(list(x)), l)) for l in zip(*[iter(data)]*3)]))


def main():
    import aoc 
    data = aoc.get(2022,3).splitlines()
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()

