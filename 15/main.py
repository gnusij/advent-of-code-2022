import re

def show(G):
    print()
    for line in G:
        print(''.join(line))
    print()

def fill(G, dist, originx, originy, minx, miny):
    print(f"checking {originx, originy}") 
    print(f"checking {originx-minx, }") 
    print(f"checking {G[originy-miny][originx-minx]}") 
    ox = originx-minx
    oy = originy-miny
    for j in range(originy-dist-miny, originy+dist-miny+1):
        for i in range(originx-dist-minx, originx+dist-minx+1):
            d = abs(originx-i-minx) + abs(originy-j-miny)
            print(f"{i, j}") 
            if G[j][i] == '.' and d<=dist:
                G[j][i] = '#'
    return G

S = set(); B = set()
minx = 0;miny = 0;maxx = 0;maxy = 0
for line in open(0).read().splitlines():
    tmp = line.split(',')
    sx = int(tmp[0].split('=')[1].strip())
    sy = int(tmp[1].split('=')[1].split(':')[0])
    bx = int(tmp[1].split('=')[2].strip())
    by = int(tmp[2].split('=')[1].strip())
    dist = abs(bx-sx) + abs(by-sy)
    S.add((sx, sy, dist))
    B.add((bx, by))
    minx = min(minx, sx, bx)
    maxx = max(maxx, sx, bx)
    miny = min(miny, sy, by)
    maxy = max(maxy, sy, by)

def check(S,x,y):
    for sx,sy,dist in S:
        d = abs(sx-x) + abs(sy-y)
        if d<=dist:
            return 0
    return 1

def edges(x,y,dist):
    #edges = []
    #for j in range(y-dist, y+dist+1):
    #    for i in range(x-dist, y+dist+1):
    #        if abs(x-i)+abs(y-j) == dist+1:
    #            edges.append((i,j))
    #return edges
    for dx in range(dist+1+1):
        dy = dist+1-dx
        for X,Y in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            x = X*dx + sx
            y = Y*dy + sy
            yield x,y

# PART 1
miny-=1000000
maxy+=1000000
minx-=1000000
maxx+=1000000
s = 0
y = 2000000
for x in range(minx, maxx):
    if (x,y) not in B and not check(S,x,y):
        s +=1
print(s)


m = 4000000
#for y in range(0, m+1):
#    FILL = set()
#    for x in range(0, m+1):
#        if (x,y) not in B and not check(S,x,y):
#            continue
#        elif (x,y) not in B and checkSen(S,x,y):
#            print(x,y)
#            print(x*4000000+y)


#for sx,sy,dist in S:
#    for x,y in edges(sx,sy,dist):
#        if 0<x<m+1 and 0<y<m+1:
#            if check(S,x,y): 
#                print(x,y)
#                print(x*4000000+y)
#                break


#print(miny, maxy, minx, maxx)
#print(S, B)
#G = []
#for j,y in enumerate(range(miny, maxy)):
#    G.append([])
#    for i,x in enumerate(range(minx, maxx)):
#        if (x,y) in S:
#            G[j].append('S')
#        elif (x,y) in B:
#            G[j].append('B')
#        else:
#            G[j].append('.')
#show(G)
#for i,sensor in enumerate(S):
#    sx,sy = S[i]
#    bx,by = B[i]
#    dist = abs(bx-sx) + abs(by-sy)
#    print(dist, sx, sy)
#    G = fill(G, dist, sx, sy, minx, miny)
#show(G)
#print(len([x for x in G[10-miny] if x=='#']))

for sx,sy,dist in S:
    for x,y in edges(sx,sy,dist):
        if 0<x<m and 0<y<m and check(S,x,y):
            print(x*4000000 + y)
            break
    else:
        continue
    break