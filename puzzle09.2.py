#!/usr/bin/python3

path = set()

knots = [ [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0] ]

def next_head(step,headpos):
    if step == "R":
        headpos[0] += 1
    if step == "L":
        headpos[0] -= 1
    if step == "U":
        headpos[1] += 1
    if step == "D":
        headpos[1] -= 1

def next_tail(headpos,tailpos):
    dx = headpos[0]-tailpos[0]
    dy = headpos[1]-tailpos[1]
    if abs(dx) <= 1 and abs(dy) <= 1:
        return
    if abs(dx) > 2 or abs(dy) > 2:
        you_fucked_up()
    # now the hard part
    if dx == 0:
        tailpos[1] += dy//2
        return
    if dy == 0:
        tailpos[0] += dx//2
        return
    if abs(dx) == 2 and abs(dy) == 1:
        tailpos[1] += dy
        tailpos[0] += dx//2
        return
    if abs(dy) == 2 and abs(dx) == 1:
        tailpos[0] += dx
        tailpos[1] += dy//2
        return
    if abs(dy) == 2 and abs(dx) == 2:
        tailpos[0] += dx//2
        tailpos[1] += dy//2
        return
    # never come here
    you_fucked_up() 

with open("input09") as file:

    while (line := file.readline().strip()):
        step,count = line.split(" ")
        for i in range(0,int(count)):
            next_head(step,knots[0])
            for j in range(0,9):
                next_tail(knots[j],knots[j+1])
            path.add((knots[9][0],knots[9][1]))

print(len(path))
