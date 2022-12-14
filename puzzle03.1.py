#!/usr/bin/python3

def item_score(c):
    if c.isupper():
        return(ord(c)-ord("A")+27)
    if c.islower():
        return(ord(c)-ord("a")+1)

total_score = 0

with open("input03") as file:
    for line in file:
        line = line.strip()
        mid = int(len(line)/2)
        part1 = line[0:mid]
        part2 = line[mid:]
        print(part1)
        print(part2)

        for c in part1:
            if c in part2:
                print(c)
                total_score += item_score(c)
                break

print(total_score)
