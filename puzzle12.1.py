#!/usr/bin/python3

heightmap = []
distmap = []
current = 0
start = None
end = None
visited = set()
candidates = []

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

def set_distance(node,d):
    distmap[node[1]][node[0]] = d

def get_next():
    global candidates

    smallest = 10000000
    result = 0
    #print(candidates)
    #print(range(0,len(candidates)))
    for i in range(0,len(candidates)):
        c = candidates[i]
        d = get_distance(c)
        #print(d)
        if d <= smallest:
            smallest = d
            result = i
    #print(result)
    return(candidates.pop(result))

with open("input12") as file:

    while (line := file.readline().strip()):

        distmap.append([ 1000000 for c in line ])
        if "S" in line:
            start = [ line.find("S"), current ]
            line = line.replace("S","a")
        if "E" in line:
            end = [ line.find("E"), current ]
            line = line.replace("E","z")
        heightmap.append([ ord(c)-ord("a") for c in line])
        current += 1
            
print(heightmap)
print(distmap)
print(start,end)

distmap[start[1]][start[0]] = 0

done = False
current = start

while not done:
    print(current,len(visited),len(candidates))
    nbs = get_neighbors(current)
    mydist = get_distance(current)
    for nb in nbs:
        if tuple(nb) in visited:
            continue
        if get_distance(nb) > mydist+1:
            set_distance(nb,mydist+1)
            candidates.append(nb)
    visited.add(tuple(current))
    if current == end:
        break
    current = get_next()

print(get_distance(current))
