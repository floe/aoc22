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

def count_outside(c):
    myfaces = 0
    myfaces += cubes[c[0],c[1],c[2]-1]
    myfaces += cubes[c[0],c[1],c[2]+1]
    myfaces += cubes[c[0],c[1]-1,c[2]]
    myfaces += cubes[c[0],c[1]+1,c[2]]
    myfaces += cubes[c[0]-1,c[1],c[2]]
    myfaces += cubes[c[0]+1,c[1],c[2]]
    return(6-myfaces)

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

for c in coords:
    c[0] = c[0]-minx+1
    c[1] = c[1]-miny+1
    c[2] = c[2]-minz+1
    cubes[c[0],c[1],c[2]] = 1

#print(cubes)

faces = 0

for c in coords:
    faces += count_outside(c)

print(faces)
