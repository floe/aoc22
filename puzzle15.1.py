#!/usr/bin/python3

sensors = []
xmid = 0
#qy = 10
qy = 2000000

def mhd(x1,y1,x2,y2):
    d = abs(x1-x2)+abs(y1-y2)
    #print("mhd",x1,y1,x2,y2,d)
    return(d)

def exclude_count(direction):
    excluded = 0
    xpos = xmid
    scount = 0
    while True:
        for s in sensors:
            if mhd(s[0],s[1],xpos,qy) <= s[2]:
                scount += 1
                break
        #print(xpos,scount,excluded)
        if scount == 0:
            break
        xpos += direction
        excluded += 1
        scount = 0
    return(excluded-1)

with open("input15") as file:

    for line in file:
        line = line.strip()
        items = line.split(" ")
        sx = int(items[2].strip(",").split("=")[1])
        sy = int(items[3].strip(":").split("=")[1])
        bx = int(items[8].strip(",").split("=")[1])
        by = int(items[9].strip(":").split("=")[1])
        dist = mhd(sx,sy,bx,by)
        xmid += sx
        sensors.append([sx,sy,dist])

xmid = xmid//len(sensors)
print(xmid)

r1 = exclude_count(1)
r2 = exclude_count(-1)

print(r1+r2)
