#!/usr/bin/python3

trees = []

count = 0
w = 0
h = 0

def is_visible(x,y):

    if x == 0 or y == 0:
        return True
    if x >= w-1 or y >= h-1:
        return True

    result = 4
    myheight = trees[y][x]

    for dx in range(0,x):
        if trees[y][dx] >= myheight:
            result = result-1
            break

    for dx in range(x+1,w):
        if trees[y][dx] >= myheight:
            result = result-1
            break

    for dy in range(0,y):
        if trees[dy][x] >= myheight:
            result = result-1
            break

    for dy in range(y+1,h):
        if trees[dy][x] >= myheight:
            result = result-1
            break

    return (result != 0)

with open("input08") as file:

    while (line := file.readline().strip()):
        trees.append([int(c) for c in line])

w = len(trees[0])
h = len(trees)

for x1 in range(0,w):
    for y1 in range(0,h):
        if is_visible(x1,y1):
            count += 1
    print(".",end="")

print(count)
