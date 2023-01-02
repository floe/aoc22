#!/usr/bin/python3

import numpy as np

directions = [ (1,0), (0,1), (-1,0), (0,-1) ]
dirlabel = [ ">","v","<","^" ]
curdir = 0

maze = []
last = False
steps = ""
width = 0
start = None

# input22.tiny:
#   1
# 234
#   56

def find_quadrant(pos):
    x,y = pos
    if y <= 4 and x == 12:
        return(6)
    if y <= 4 and x == 8:
        return(3)
    if y <= 8:
        if x <= 4:
            return( 2 )
        if x <= 8:
            return( 3 )
        if x <= 12:
            return( 4 )
    if y <= 12:
        return( 5 if x <= 12 else 6 )

def find_wrap(pos):
    x,y = pos
    # 1 -> 3 OK
    if x ==  50 and y >=   1 and y <=  50:
        return([1,151-y],0)
    # 3 -> 1 OK
    if x ==   0 and y >= 101 and y <= 150:
        return([51,151-y],0)
    # 6 -> 5 OK?
    if x == 151 and y >=   1 and y <=  50:
        return([100,151-y],2)
    # 5 -> 6 OK?
    if x == 101 and y >= 101 and y <= 150:
        return([150,151-y],2)
    # 6 -> 4 OK?
    if y ==  51 and x >= 101 and x <= 150:
        return([100,x-50],2)
    # 4 -> 6 OK?
    if x == 101 and y >=  51 and y <= 100:
        return([y+50,50],3)
    # 4 -> 3 FIXME???
    if x ==  50 and y >=  51 and y <= 100:
        return([y-50,101],1)
    # 3 -> 4 FIXME???
    if y == 100 and x >=   1 and x <=  50:
        return([51,x+50],0)
    # 5 -> 2 OK
    if y == 151 and x >=  51 and x <= 100:
        return([50,x+100],2)
    # 2 -> 5 OK
    if x ==  51 and y >= 151 and y <= 200:
        return([y-100,150],3)
    # 2 -> 6 OK
    if y == 201 and x >=   1 and x <=  50:
        return([x+100,1],1)
    # 6 -> 2 OK
    if y ==   0 and x >= 101 and x <= 150:
        return([x-100,200],3)
    # 2 -> 1 OK
    if x ==   0 and y >= 151 and y <= 200:
        return([y-100,1],1)
    # 1 -> 2 OK
    if y ==   0 and x >=  51 and x <= 100:
        return([1,x+100],0)
    # never come here
    print(x,y)
 
# input22:
#  16
#  4
# 35
# 2


#with open("input22.tiny") as file:
with open("input22") as file:
    for line in file:
        line = line.strip("\n")
        if line == "":
            last = True
            continue
        if not last:
            maze.append(" "+line+" ")
            if len(line) > width:
                width = len(line)
        else:
            #steps = [ x for x in "15R1L137L5R16L1R4R1L9L1R4L1R8R1L10L2L7" ] # line ]
            #steps = [ x for x in "3R5R6L6L10" ] # line ]
            steps = [ x for x in line ]

maze.append(" "*(width+2))
maze.insert(0," "*(width+2))
steps.append("X")

for i,l in enumerate(maze):
    linelen = len(l)
    if linelen < width+2:
        maze[i] = l + " " * (width+2-linelen)

start = [maze[1].index("."),1]
print(start)

tmp = []
cur = ""
while len(steps) > 0:
    char = steps.pop(0)
    cur+=char
    if not char.isnumeric():
        tmp.append(cur)
        cur=""

steps = tmp
print(steps)

curpos = start

def swap_char(tmpstr,pos):
    return(tmpstr[:pos] + dirlabel[curdir] + tmpstr[pos+1:])

for s in steps:
    count = int(s[0:-1])
    direc = s[-1]
    print(s)
    for i in range(0,count):
        newpos = [ curpos[0]+directions[curdir][0], curpos[1]+directions[curdir][1] ]
        newdir = curdir
        print(count,direc,curpos,curdir,newpos)
        if maze[newpos[1]][newpos[0]] == " ":
            newpos,newdir = find_wrap(newpos)
        if maze[newpos[1]][newpos[0]] == "#":
            break
        curpos = newpos
        curdir = newdir
        maze[newpos[1]] = swap_char(maze[newpos[1]],newpos[0])

    if direc == "R":
        curdir += 1
    elif direc == "L":
        curdir += 3
    curdir = curdir%4

for m in maze:
    print(m)

print(curpos,curdir)
print(curpos[1]*1000+curpos[0]*4+curdir)
