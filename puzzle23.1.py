#!/usr/bin/python3

import numpy as np

directions = [ (0,-1), (0,1), (-1,0), (1,0) ]

elves = []
area = []

class Elf:
    def __init__(self,c):
        self.c = c
        self.step = None
    def __repr__(self):
        return(str(self.c)+" "+str(self.step))

with open("input23.tiny") as file:
#with open("input23") as file:
    for line in file:
        current = []
        line = line.strip("\n")
        for c in line:
            if c == "#":
                current.append(Elf(1))
            else:
                current.append(Elf(0))
        current.append(Elf(0))
        current.append(Elf(0))
        current.append(Elf(0))
        current.insert(0,Elf(0))
        current.insert(0,Elf(0))
        current.insert(0,Elf(0))
        area.append(current)

area.insert(0,[ Elf(0) for n in area[0] ])
area.insert(0,[ Elf(0) for n in area[0] ])
area.insert(0,[ Elf(0) for n in area[0] ])
area.append(  [ Elf(0) for n in area[0] ])
area.append(  [ Elf(0) for n in area[0] ])
area.append(  [ Elf(0) for n in area[0] ])

for n in area:
    res = [ str(x.c) for x in n ]
    print("".join(res))

def get_direction(c,x,y):
    step = None
    if c <= 0:
        return(step)
    nbcount = 0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if area[y+dy][x+dx].c > 0:
                nbcount += 1
    if nbcount == 1:
        return(step)
    for i in range(c-1,c+3):
        curdir = directions[i%4]
        nbcount = 0
        for o in [-1,0,1]:
            dx,dy = curdir
            if dx == 0:
                dx = o
            else:
                dy = o
            if area[y+dy][x+dx].c > 0:
                nbcount+=1
                break
        if nbcount == 0:
            step = curdir
            break
    return(step)

movecount = 1

#while movecount > 0:
for iteration in range(0,10):
    movecount = 0

    # determine movement candidates for every elf
    for y,l in enumerate(area):
        for x,c in enumerate(l):
            step = get_direction(c.c,x,y)
            if step == None:
                continue
            #print(c,x,y,step)
            area[y][x].step = step
            area[y+step[1]][x+step[0]].c -= 1

    # actually move those elves that are free to move
    for y,l in enumerate(area):
        for x,c in enumerate(l):
            step = c.step
            if step == None:
                continue
            print(x,y,step)
            if area[y+step[1]][x+step[0]].c != -1:
                continue
            #print(c,x,y,step)
            area[y+step[1]][x+step[0]] = c
            area[y][x] = Elf(0)
            movecount += 1

    # cleanup the movement candidates, increase next step
    for y,l in enumerate(area):
        for x,c in enumerate(l):
            c.step = None
            if c.c < 0:
                c.c = 0
            if c.c > 0:
                c.c += 1
    print(movecount)

    for n in area:
        res = [ str(x.c) for x in n ]
        print("".join(res))
