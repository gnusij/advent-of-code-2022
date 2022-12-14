G = set() 
YY = 0
for line in open(0).read().splitlines():
    d = line.split(' -> ')
    for i in range(len(d)-1):
        x,y = map(int, d[i].split(','))
        X,Y = map(int, d[i+1].split(','))
        if x==X:
            miny = min(y,Y)
            maxy = max(y,Y)
            for j in range(miny,maxy+1):
                G.add((x,j))
        if y==Y:
            minx = min(x,X)
            maxx = max(x,X)
            for i in range(minx,maxx+1):
                G.add((i,y))
        YY = max(Y,y,YY)

def sand(G):
    G = eval(str(G))
    s = 0
    i = 0
    while i<100000 and (500,0) not in G: 
        x,y = 500, 0
        while y<1000: 
            if (x,y+1) not in G:
                y+=1
            elif (x-1,y+1) not in G:
                x-=1
                y+=1
            elif (x+1,y+1) not in G:
                x+=1
                y+=1
            else:
                G.add((x,y)) 
                s+=1
                break
        i+=1
    print(s)

sand(G)
for i in range(-10000,10000):
    G.add((i,YY+2))
sand(G)


# TODO: need to find a way to not use arbitary depth to break the whileloop