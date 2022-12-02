from pathlib import Path

WIN = {
    'r':'p',
    'p':'s',
    's':'r',
}
LOSE = {
    'r':'s',
    'p':'r',
    's':'p',
}
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
SHAPE = {
    'r':1,
    'p':2,
    's':3,
}

def solution_a(data):
    def play(o, m):
        if o == m:
            return 3 + SHAPE[m]
        elif WIN[o] == m: 
            return 6 + SHAPE[m]
        elif LOSE[o] == m:
            return 0 + SHAPE[m]
    score = 0
    for o, m in data:
        score += play(O[o], M[m])
    print(score)

def solution_b(data):
    def play(o, m):
        if m == "X": 
            return 0 + SHAPE[LOSE[o]]
        elif m == "Y": 
            return 3 + SHAPE[o]
        else: 
            return 6 + SHAPE[WIN[o]]
    score = 0
    for o, m in data:
        score += play(O[o], m)
    print(score)

def main():
    with open(Path(__file__).parent.joinpath('data.txt')) as f:
        data = [x.split() for x in f.read().split('\n')]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()
