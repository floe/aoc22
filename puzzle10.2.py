#!/usr/bin/python3

screen = [ "." for x in range(0,240) ]
X = 1
cycle = 1

def step():
    global cycle,screen
    if abs(X-((cycle-1)%40)) <= 1:
        screen[cycle-1] = "X"
    #print(cycle,X)
    cycle += 1

with open("input10") as file:

    while (line := file.readline().strip()):
        cmd = line.split(" ")
        if cmd[0] == "noop":
            step()
        else:
            step()
            step()
            X += int(cmd[1])

for l in range(0,6):
    print("".join(screen[l*40:(l+1)*40]))
