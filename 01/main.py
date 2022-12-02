from pathlib import Path

def solution_a(data):
    print(max(data))

def solution_b(data):
    print(sum(sorted(data)[::-1][:3]))

def main():
    with open(Path(__file__).parent.joinpath('data.txt')) as f:
        data = [ sum(map(int, x.split('\n'))) for x in f.read().split('\n\n') ]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()