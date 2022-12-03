
def calc_p(char):
    if char.islower():
        return ord(char) - 96
    else:
        return ord(char) - 38


def solution_a(data):
    s = 0
    for l in data:
        A = set(list(l[:int(len(l)/2)]))
        B = set(list(l[int(len(l)/2):]))
        intersect = A.intersection(B)
        for char in intersect:
            s += calc_p(char)  
    print(s)


def solution_b(data):
    s = 0
    for i in range(0,len(data)-1,3):
        A = set(list(data[i]))
        B = set(list(data[i+1]))
        C = set(list(data[i+2]))
        intersect = A.intersection(B, C)
        for char in intersect:
            s += calc_p(char)  
    print(s)


def main():
    from aoc import data
    data = data.split('\n')
    solution_a(data)
    solution_b(data)

if __name__ == "__main__":
    main()

