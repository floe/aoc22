#!/usr/bin/python3

samples = [ 20, 60, 100, 140, 180, 220 ]
X = 1
cycle = 1
signal = 0

def step():
    global cycle,signal
    if cycle in samples:
        strength = X * cycle
        signal += strength
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

print(signal)
