#!/usr/bin/python3

sensors = []
maxc = 4000000
midx = 0
midy = 0
mdist = 0

def mhd(x1,y1,x2,y2):
    d = abs(x1-x2)+abs(y1-y2)
    #print("mhd",x1,y1,x2,y2,d)
    return(d)

def check_pos(x,y):
    if x < 0 or y < 0 or x >= maxc or y >= maxc:
        return
    scount = 0
    for s in sensors:
        if mhd(s[0],s[1],x,y) <= s[2]:
            scount = 1
            break
    if scount == 0:
        print(x,y,x*maxc+y)
        exit()

def check_sensor(s):
    sx = s[0]
    sy = s[1]
    d = s[2]
    for i in range(0,d+1):
        check_pos(sx+i,sy+d+1-i)
        check_pos(sx+i,sy-d-1+i)
        check_pos(sx-i,sy+d+1-i)
        check_pos(sx-i,sy-d-1+i)

with open("input15") as file:

    for line in file:
        line = line.strip()
        items = line.split(" ")
        sx = int(items[2].strip(",").split("=")[1])
        sy = int(items[3].strip(":").split("=")[1])
        bx = int(items[8].strip(",").split("=")[1])
        by = int(items[9].strip(":").split("=")[1])
        dist = mhd(sx,sy,bx,by)
        sensors.append([sx,sy,dist])

# perhaps faster?
sensors.sort(key=lambda x: x[2])

for s in sensors:
    print(s)
    check_sensor(s)
