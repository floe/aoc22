#!/usr/bin/python3

import numpy as np

maze = []
last = False
steps = ""

with open("input22.tiny") as file:
#with open("input21") as file:
    for line in file:
        line = line.strip("\n")
        if line == "":
            last = True
            continue
        if not last:
            maze.append(line)
        else:
            steps = line

print(maze,steps)
