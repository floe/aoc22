#!/usr/bin/python3

heightmap = []
distmap = []
start = None
end = None
current = 0
w = 0
v = 0

def get_neighbors(node):

    x = node[0]
    y = node[1]

    nbs = []
    cur = heightmap[y][x]

    if y < len(heightmap)-1:
        nb = heightmap[y+1][x]
        if nb <= cur+1:
            nbs.append([x,y+1])

    if x < len(heightmap[0])-1:
        nb = heightmap[y][x+1]
        if nb <= cur+1:
            nbs.append([x+1,y])

    if y > 0:
        nb = heightmap[y-1][x]
        if nb <= cur+1:
            nbs.append([x,y-1])

    if x > 0:
        nb = heightmap[y][x-1]
        if nb <= cur+1:
            nbs.append([x-1,y])

    return(nbs)

def get_distance(node):
    return(distmap[node[1]][node[0]])

def set_distance(n1,n2,d):
    v1 = n1[1]*w + n1[0]
    v2 = n2[1]*w + n2[0]
    distmap[v1][v2] = d
    distmap[v2][v1] = d

with open("input12") as file:

    while (line := file.readline().strip()):

        if "S" in line:
            start = [ line.find("S"), current ]
            line = line.replace("S","a")
        if "E" in line:
            end = [ line.find("E"), current ]
            line = line.replace("E","z")
        heightmap.append([ ord(c)-ord("a") for c in line])
        current += 1

w = len(heightmap[0])
v = len(heightmap)*w

for i in range(0,v):
    distmap.append([ 1000000 for j in range(0,v) ])

for i in range(0,v):
    distmap[i][i] = 0

for y in range(0,len(heightmap)):
    for x in range(0,w):
        node = [x,y]
        nbs = get_neighbors(node)
        for nb in nbs:
            set_distance(node,nb,1)

for k in range(0,v):
    print(k,v)
    for i in range(0,v):
        for j in range(0,v):
            if distmap[i][j] > distmap[i][k] + distmap[k][j]:
                distmap[i][j] = distmap[i][k] + distmap[k][j]

index = end[1]*w+end[0]
res = distmap[index]
print(res)

mindist = 1000000

for c in range(0,len(res)):
    x = c  % w
    y = c // w
    if heightmap[y][x] == 0:
        if res[c] < mindist:
            mindist = res[c]

print(mindist)
