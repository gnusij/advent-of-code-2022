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

def edges(sx,sy,dist):
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
# why my part1 so slow??

m = 4000000
for sx,sy,dist in S:
    for x,y in edges(sx,sy,dist):
        if 0<x<m and 0<y<m and check(S,x,y):
            print(x*m + y)
            break
    else:
        continue
    break