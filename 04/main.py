
def ex(s):
    x = list(map(int,s.split('-')))
    return set(range(x[0],x[1]+1))

def solution_a(data):
    #p = 0
    #for l in data:
    #    A = ex(l[0])
    #    B = ex(l[1])
    #    if A.issubset(B) or B.issubset(A):
    #        p +=1 
    #print(p)
    def d(A,B):
        if A.issubset(B) or B.issubset(A):
            return 1
    print(sum([1 if d(*map(ex, l)) else 0 for l in data]))


def solution_b(data):
    #o = 0
    #for l in data:
    #    A = ex(l[0])
    #    B = ex(l[1])
    #    if A.intersection(B):
    #        o +=1 
    #print(o)
    print(sum([1 if set.intersection(*map(ex, l)) else 0 for l in data]))

def main():
    from aoc import data
    data = [l.split(',') for l in data.splitlines()]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()


