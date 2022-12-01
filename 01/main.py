from pathlib import Path
import numpy as np

def solution_a(data):
    sums = []
    l = []
    for line in data:
        if line == "":
            sums.append(sum(l))
            l = []
        else:
            l.append(int(line))
    print(max(sums))

def solution_b(data):
    sums = []
    l = []
    for line in data:
        if line == "":
            sums.append(sum(l))
            l = []
        else:
            l.append(int(line))
    print(sum(sorted(sums, reverse=True)[:3]))

def main():
    with open(Path(Path(__file__).parent, 'data.txt')) as f:
        data = [line.strip() for line in f.readlines()]
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()