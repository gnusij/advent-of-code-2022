from queue import PriorityQueue
def dijkstra(G,s,t):
    D={v:len(G) for v in range(len(G))}
    D[s]=0
    q=PriorityQueue()
    q.put((0,s))
    while not q.empty():
        (d,v)=q.get()
        for n in G[v]:
            a=D[n]
            b=D[v]+1 
            if b<a:
                q.put((b,n))
                D[n]=b 
    return D[t]

l=[[*l] for l in open(0).read().split('\n')]
h=len(l)
w=len(l[0])

S=[]
for k in range(h*w):
    y=k//w;x=k%w
    if l[y][x]=="S":l[y][x]='a';s=k
    if l[y][x]=="E":l[y][x]='z';t=k
    l[y][x]=ord(l[y][x])-97
    if l[y][x]==0:S+=[k]

G={}
for k in range(h*w):
    y=k//w;x=k%w
    if k not in G:G[k]=[]
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        X,Y=x+dx,y+dy
        if 0<=X<w and 0<=Y<h:
            if l[Y][X]<=l[y][x]+1:
                G[k]+=[Y*w+X]
print(dijkstra(G,s,t))

m=9E9
for s in S:
    m=min(dijkstra(G,s,t),m)
print(m)