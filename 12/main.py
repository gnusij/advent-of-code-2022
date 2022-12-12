from queue import PriorityQueue
from collections import deque, defaultdict 

def dijkstra(G, k, start_vertex):
    D = {v:float('inf') for v in range(len(k))}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():

        (dist, current_vertex) = pq.get()

        for neighbor in G[current_vertex]:
            distance = k[neighbor]
            old_cost = D[neighbor]
            new_cost = D[current_vertex] + distance

            if new_cost < old_cost:
                pq.put((new_cost, neighbor))
                D[neighbor] = new_cost 
    return D

l = [[*l] for l in open(0).read().split('\n')]
h = len(l)
w = len(l[0])

ii = 0 
S = []
for y in range(h):
    for x in range(w):
        if l[y][x] == "S":
            l[y][x] = 'a'
            start = ii
        if l[y][x] == "E":
            target = ii
            l[y][x] = 'z'
        l[y][x] = ord(l[y][x])-97
        if l[y][x] == 0:
            S.append(ii)
        ii += 1

G = defaultdict(list)
k = {}
ii = 0
for y in range(h):
    for x in range(w):
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            X,Y = x+dx, y+dy
            if 0 <= X < w and 0 <= Y < h: 
                if l[Y][X] <= l[y][x] + 1:
                    G[ii].append(Y*w+X)
        k[ii] = 1
        ii += 1
dists = dijkstra(G, k, start)

print(dists[target])
m = 9E9
for start in S:
    m = min(dijkstra(G, k, start)[target], m)
print(m)