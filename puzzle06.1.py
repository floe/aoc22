#!/usr/bin/python3

chars = []
pos = 0

with open("input06") as file:

    line = file.readline().strip()

    for char in line:
        chars.append(char)
        pos += 1
        if len(chars) < 4:
            continue
        if len(chars) > 4:
            chars.pop(0)
        if chars[0] == chars[1] or chars[0] == chars[2] or chars[0] == chars[3]:
            continue
        if chars[1] == chars[2] or chars[1] == chars[3] or chars[2] == chars[3]:
            continue
        print(pos)
        break

