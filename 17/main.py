class Block:
    def __init__(self, shape, x, y):
        self.shape = shape
        self.x = x 
        self.y = y 

class LightTetris:
    def __init__(self):
        self.blocks = [
            [0,1,2,3],
            [1,4,5,6,9],
            [0,1,2,6,10],
            [0,4,8,12],
            [0,1,4,5],
        ]
        self.block_counter = 0
        self.height = 0
        self.width = 7
        self.field = set() 
        self.new_block()

    def new_block(self):
        shape = self.blocks[self.block_counter%len(self.blocks)]
        self.block = Block(shape, 2, self.height+3)
        self.block_counter += 1
    
    def intersects(self):
        for i in range(4):
            for j in range(4):
                if i*4+j in self.block.shape:
                    if i + self.block.y < 0 or \
                        j + self.block.x > self.width-1 or \
                        j + self.block.x < 0 or \
                        (j+self.block.x,i+self.block.y) in self.field:
                        return True
        return False

    def go_down(self):
        self.block.y -= 1
        if self.intersects():
            self.block.y += 1
            self.freeze()

    def freeze(self):
        maxY = 0
        for i in range(4):
            for j in range(4):
                if i*4+j in self.block.shape:
                    self.field.add((j+self.block.x,i+self.block.y))
                    maxY = max(maxY,i+self.block.y)
        if maxY+1>self.height:
            old_height = self.height
            self.height = maxY+1
        #print(self.height, self.block_counter)
        self.new_block()
        #self.show()
        #print(self.block_counter, self.height)

    def go_side(self, dx):
        if dx == ">":
            dx = 1
        else:
            dx = -1
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x


class Tetris:
    def __init__(self):
        self.blocks = [
            [0,1,2,3],
            [1,4,5,6,9],
            [0,1,2,6,10],
            [0,4,8,12],
            [0,1,4,5],
        ]
        self.block_counter = 0
        self.height = 0
        self.width = 7
        self.field = []

        for i in range(7):
            new_line = []
            for j in range(self.width):
                new_line.append(0)
            self.field.append(new_line)
        self.new_block()

    def new_block(self):
        shape = self.blocks[self.block_counter%len(self.blocks)]
        self.block = Block(shape, 2, self.height+3)
        self.block_counter += 1
    
    def intersects(self):
        for i in range(4):
            for j in range(4):
                if i*4+j in self.block.shape:
                    if i + self.block.y < 0 or \
                        j + self.block.x > self.width-1 or \
                        j + self.block.x < 0 or \
                        self.field[i+self.block.y][j+self.block.x] != 0:
                        return True
        return False

    def go_down(self):
        self.block.y -= 1
        if self.intersects():
            self.block.y += 1
            self.freeze()

    def freeze(self):
        maxY = 0
        for i in range(4):
            for j in range(4):
                if i*4+j in self.block.shape:
                    self.field[i+self.block.y][j+self.block.x] = '#'
                    maxY = max(maxY,i+self.block.y)
        if maxY+1>self.height:
            old_height = self.height
            self.height = maxY+1
            for i in range(self.height-old_height):
                new_line = []
                for j in range(self.width):
                    new_line.append(0)
                self.field.append(new_line)
        self.new_block()
        #self.show()
        #print(self.block_counter, self.height)

    def go_side(self, dx):
        if dx == ">":
            dx = 1
        else:
            dx = -1
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

    def show(self):
        view = [['.']*7 for y in range(self.height+7)]
        for y in range(self.height+7):
            for x in range(7):
                # draw falling object
                if (x,y) == (self.block.x, self.block.y):
                    for i in range(4):
                        for j in range(4):
                            if i*4+j in self.block.shape:
                                X = x+j
                                Y = y+i
                                view[Y][X] = '#'
                # draw existing field    
                elif self.field[y][x] != 0: 
                    view[y][x] = '#'
        print()
        for line in view[::-1]:
            print(''.join(line))

import time

d = [i for i in open(0).read()]
t = LightTetris()
c=0
cc = 0
tick = time.time()

#print(len(d), len(t.blocks), len(d)*len(t.blocks))
old = 0
nold = 1
ntmp = 1
htmp = 0
gains = []
while True: 
    t.go_side(d[c%len(d)])
    t.go_down()
    if t.block_counter > ntmp:
        gains.append(t.height-htmp)
        ntmp = t.block_counter
        htmp = t.height
    if c%(len(d)*len(t.blocks)) == 0:
        print(c, (t.height, t.height-old), (t.block_counter-1, t.block_counter-nold))
        print(gains)
        height_diff = t.height-old
        block_diff = t.block_counter-nold
        old = t.height 
        nold = t.block_counter
        if cc==1: 
            b_height = height_diff
            b_block = block_diff
        elif cc==10:
            break
        cc+=1
        gains = []
    c +=1
num = 2022
num = 1000000000000
cycle = len(d)*len(t.blocks)
block_diff*=1
height_diff*=1

base_block = ((num-b_block)//block_diff)*block_diff + b_block if num-b_block>0 else 0
base_height = ((num-b_block)//block_diff)*height_diff + b_height if num-b_block>0 else 0
res = num-base_block
print()
print("\t Base Height:", base_height)
print("\t Base Block:", base_block)
print("\t Remaining Blocks:",res)
print(base_height+sum([v for i,v in enumerate(gains) if i < res]))