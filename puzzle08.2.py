#!/usr/bin/python3

trees = []

max_score = 0
w = 0
h = 0

def get_score(x,y):

    if x == 0 or y == 0:
        return 0 
    if x >= w-1 or y >= h-1:
        return 0

    result = 1
    myheight = trees[y][x]

    for dx in range(x-1,-1,-1):
        if trees[y][dx] >= myheight or dx == 0:
            result *= x-dx
            break

    for dx in range(x+1,w):
        if trees[y][dx] >= myheight or dx == w-1:
            result *= dx-x
            break

    for dy in range(y-1,-1,-1):
        if trees[dy][x] >= myheight or dy == 0:
            result *= y-dy
            break

    for dy in range(y+1,h):
        if trees[dy][x] >= myheight or dy == h-1:
            result *= dy-y
            break

    return(result)

with open("input08") as file:

    while (line := file.readline().strip()):
        trees.append([int(c) for c in line])

w = len(trees[0])
h = len(trees)

for x1 in range(0,w):
    for y1 in range(0,h):
        score = get_score(x1,y1)
        if score > max_score:
            max_score = score
    print(".",end="")

print(max_score)
