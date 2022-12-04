
O = {
    'A':'r',
    'B':'p',
    'C':'s',
}
M = {
    'X':'r',
    'Y':'p',
    'Z':'s',
}
S = "rps"


def solution_a(data):
    print(sum(["rrppssrpsr".count(o+m)*3+S.find(m)+1 for o, m in data]))


def solution_b(data):
    print(sum([m*3+S.find(S[(S.find(o)+m-1)%3])+1 for o, m in data]))
    

def main():
    import aoc
    data = [x.split() for x in aoc.get(2022,2).splitlines()]
    solution_a([[O[o],M[m]] for o,m in data])
    solution_b([[O[o],"XYZ".find(m)] for o,m in data])


if __name__ == "__main__":
    main()
