
def f(d, n): 
    for i in range(len(d)):
        if len({*d[i:i+n]})==n:
            print(i+n)
            break

def main():
    import aoc 
    d = aoc.get(2022,6).strip()
    f(d, 4)
    f(d, 14)

if __name__ == "__main__":
    main()
