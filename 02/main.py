
def C(o,m):
    return ord(o)-65, ord(m)-88

def solution_a(data):
    print(sum(["0011220120".count(str(o)+str(m))*3+m+1 for o,m in data]))

def solution_b(data):
    print(sum([m*3+(o+m-1)%3+1 for o,m in data]))
    
def main():
    import aoc
    data = [C(*x.split()) for x in aoc.get(2022,2).splitlines()]
    solution_a(data)
    solution_b(data)


if __name__ == "__main__":
    main()
