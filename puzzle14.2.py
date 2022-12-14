#!/usr/bin/python3

rocks = []
cave = []
maxx = 0
maxy = 0
minx = 100000
miny = 0
sandcount = 0

def set_rock(sx,sy,ex,ey):
    #print("set_rock",sx,sy,ex,ey)
    if sx == ex:
        if sy > ey:
            sy, ey = ey, sy
        for y in range(sy,ey+1):
            cave[y][sx-minx+1] = "#"
    if sy == ey:
        if sx > ex:
            sx, ex = ex, sx
        for x in range(sx,ex+1):
            cave[sy][x-minx+1] = "#"

with open("input14") as file:

    while (line := file.readline().strip()):
        points = line.split(" -> ")
        rock = []
        for p in points:
            x,y = [ int(n) for n in p.split(",") ]
            maxx = max(maxx,x)
            maxy = max(maxy,y)
            minx = min(minx,x)
            miny = min(miny,y)
            rock.append([x,y])
        rocks.append(rock)

maxy += 2
minx = 500-maxy
maxx = 500+maxy
rocks.append([[minx,maxy],[maxx,maxy]])

print(rocks,maxx,maxy,minx,miny)

for i in range(miny,maxy+3): # one extra at the bottom
    cave.append([ "." for i in range(minx,maxx+3) ]) # one extra left and right

for path in rocks:
    start = None
    for p in path:
        if start != None:
            set_rock(start[0],start[1],p[0],p[1])
        start = p

abyss = False

# sand simulation
while not abyss:

    sandcount += 1
    curx = 500-minx+1
    cury = 0

    while True:
        if cury >= maxy:
            abyss = True
            break
        if cave[cury+1][curx] == ".":
            cury += 1
            continue
        if cave[cury+1][curx-1] == ".":
            cury += 1
            curx -= 1
            continue
        if cave[cury+1][curx+1] == ".":
            cury += 1
            curx += 1
            continue
        cave[cury][curx] = "o"
        if cury == 0:
            abyss = True
        break

for l in cave:
    print("".join(l))

print(sandcount)
