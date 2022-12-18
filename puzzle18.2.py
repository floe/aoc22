#!/usr/bin/python3

import numpy as np

minx = 1000
miny = 1000
minz = 1000

maxx = 0
maxy = 0
maxz = 0

coords = []
cubes = None
faces = 0
fillqueue = []
fillcount = 0

def count_outside(c):
    myfaces = 0
    myfaces += cubes[c[0],c[1],c[2]-1]
    myfaces += cubes[c[0],c[1],c[2]+1]
    myfaces += cubes[c[0],c[1]-1,c[2]]
    myfaces += cubes[c[0],c[1]+1,c[2]]
    myfaces += cubes[c[0]-1,c[1],c[2]]
    myfaces += cubes[c[0]+1,c[1],c[2]]
    return(myfaces)

def floodfill(start):
    global fillcount
    fillqueue.append(start)
    while len(fillqueue) > 0:
        c = fillqueue.pop()
        if c[0] < 0 or c[0] >= cubes.shape[0]:
            continue
        if c[1] < 0 or c[1] >= cubes.shape[1]:
            continue
        if c[2] < 0 or c[2] >= cubes.shape[2]:
            continue
        if cubes[c[0],c[1],c[2]] != 0:
            continue

        cubes[c[0],c[1],c[2]] = 1
        #print("filling: ",c)
        fillcount += 1

        fillqueue.append([c[0],c[1],c[2]-1])
        fillqueue.append([c[0],c[1],c[2]+1])
        fillqueue.append([c[0],c[1]-1,c[2]])
        fillqueue.append([c[0],c[1]+1,c[2]])
        fillqueue.append([c[0]-1,c[1],c[2]])
        fillqueue.append([c[0]+1,c[1],c[2]])

#with open("input18.tiny") as file:
with open("input18") as file:

    for line in file:
        line = line.strip()
        x,y,z = [ int(n) for n in line.split(",") ]
        coords.append([x,y,z])
        minx = min(minx,x)
        miny = min(miny,y)
        minz = min(minz,z)

        maxx = max(maxx,x)
        maxy = max(maxy,y)
        maxz = max(maxz,z)

print(maxx,minx,maxy,miny,maxz,minz)
cubes = np.zeros((maxx-minx+3,maxy-miny+3,maxz-minz+3),dtype=np.int64)
print(cubes.shape)

# fill in the cubes themselves
for c in coords:
    c[0] = c[0]-minx+1
    c[1] = c[1]-miny+1
    c[2] = c[2]-minz+1
    cubes[c[0],c[1],c[2]] = 1

# count total outside faces
for c in coords:
    faces += (6-count_outside(c))

# fill everything outside with lava
floodfill([0,0,0])
#floodfill(coords[0])
print(fillcount)

# subtract the air pockets
for c in coords:
    faces -= (6-count_outside(c))

print(faces)
