#!/usr/bin/python3

chars = []
pos = 0

with open("input06") as file:

    line = file.readline().strip()

    for char in line:
        chars.append(char)
        pos += 1
        if len(chars) < 14:
            continue
        if len(chars) > 14:
            chars.pop(0)
        message = True
        for i in range(0,14):
            for j in range(i+1,14):
                if chars[i] == chars[j]:
                    message = False
        if message:
            print(pos)
            break

