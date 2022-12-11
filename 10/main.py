X=C=1
S=P=0
w,*Q=40,
M=[[' ']*w for i in range(6)]
for i in map(lambda x:x.split(),open(0).read().split('\n')):
    Q+=[i,[0,1][len(i)-1]],
while Q or P:
    if P==0:P=Q.pop(0)
    i,c=P
    if(C-20)%w==0:S+=C*X
    x=C%w-1
    if x in [X-1,X,X+1]:M[C//w][x]='#' 
    P=[0,[i,c-1]][c]
    if c<1and len(i)>1:X+=int(i[1])
    C+=1
print(S)
[print(''.join(m)) for m in M]