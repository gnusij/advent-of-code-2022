
def compare(A,B):
    if type(A)==int and type(B)==int:
        if A<B:
            return 1
        elif A>B:
            return 0
    elif type(A)==int and type(B)==list:
        return compare([A],B)

    elif type(A)==list and type(B)==int:
        return compare(A,[B])
    else: 
        i = 0
        while i<len(A) and i<len(B):
            c = compare(A[i],B[i])
            if c == 1:
                return 1
            if c == 0:
                return 0
            i += 1
        if i==len(A) and i<len(B):
            return 1
        elif i<len(A) and i==len(B):
            return 0

def bubble_sort(a):
    n = len(a)
    for i in range(n):
        sort = True
        for j in range(n - i - 1):
            if compare(a[j],a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                sort = False
        if sort:
            break
    return a

P = []
s = 0
for i,l in enumerate(open(0).read().split('\n\n')):
    A,B = l.split('\n')
    A = eval(A)
    B = eval(B)
    P.append(A)
    P.append(B)
    if compare(A,B)==1:
        s+=i+1
print(s)

P.append([[2]])
P.append([[6]])
P = bubble_sort(P)[::-1]

d=1
for i,p in enumerate(P):
    if p==[[2]] or p==[[6]]:
        d*=i+1
print(d)