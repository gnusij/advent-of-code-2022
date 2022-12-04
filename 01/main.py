
def solution_a(data):
    print(max(data))

def solution_b(data):
    print(sum(sorted(data)[::-1][:3]))

def main():
    import aoc
    data = [sum(map(int, x.split())) for x in aoc.get(2022,1).split('\n\n')]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()