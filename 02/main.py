from pathlib import Path

# WIN = {
#     'r':'p',
#     'p':'s',
#     's':'r',
# }
# LOSE = {
#     'r':'s',
#     'p':'r',
#     's':'p',
# }
# SHAPE = {
#     'r':1,
#     'p':2,
#     's':3,
# }
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
    #def play(o, m):
    #    if o == m:
    #        return 3 + SHAPE[m]
    #    elif WIN[o] == m: 
    #        return 6 + SHAPE[m]
    #    elif LOSE[o] == m:
    #        return 0 + SHAPE[m]
    #print(sum([play(O[o], M[m]) for o, m in data]))
    print(sum(["rrppssrpsr".count(O[o]+M[m])*3+S.find(M[m])+1 for o, m in data]))

def solution_b(data):
    #def play(o, m):
    #    if m == "X": 
    #        return 0 + SHAPE[LOSE[o]]
    #    elif m == "Y": 
    #        return 3 + SHAPE[o]
    #    else: 
    #        return 6 + SHAPE[WIN[o]]
    #print(sum([play(O[o], m) for o, m in data]))
    print(sum(["XYZ".find(m)*3+S.find(S[(S.find(O[o])+"XYZ".find(m)-1)%3])+1 for o, m in data]))
    

def main():
    with open(Path(__file__).parent.joinpath('data.txt')) as f:
        data = [x.split() for x in f.read().split('\n')]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()
