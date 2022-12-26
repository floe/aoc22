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

def find_wrap(pos):
    opp_dir = directions[(curdir+2)%4]
    while maze[pos[1]][pos[0]] != " ":
        pos = [ pos[0]+opp_dir[0], pos[1]+opp_dir[1] ]
    return([ pos[0]-opp_dir[0], pos[1]-opp_dir[1] ])

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

#def swap_char(tmpstr,pos):
#    return(tmpstr[:pos] + dirlabel[curdir] + tmpstr[pos+1:])

for s in steps:
    count = int(s[0:-1])
    direc = s[-1]
    print(s)
    for i in range(0,count):
        newpos = [ curpos[0]+directions[curdir][0], curpos[1]+directions[curdir][1] ]
        print(count,direc,curpos,curdir,newpos)
        if maze[newpos[1]][newpos[0]] == " ":
            newpos = find_wrap(curpos)
        if maze[newpos[1]][newpos[0]] == "#":
            break
        curpos = newpos
        #tmpstr = maze[newpos[1]]
        #maze[newpos[1]] = swap_char(tmpstr,newpos[0])

    if direc == "R":
        curdir += 1
    elif direc == "L":
        curdir += 3
    curdir = curdir%4

for m in maze:
    print(m)

print(curpos,curdir)
print(curpos[1]*1000+curpos[0]*4+curdir)
