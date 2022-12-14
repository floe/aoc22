#!/usr/bin/python3

def item_score(c):
    if c.isupper():
        return(ord(c)-ord("A")+27)
    if c.islower():
        return(ord(c)-ord("a")+1)

total_score = 0

with open("input03") as file:
    while (line1 := file.readline().strip()):
        line2 = file.readline().strip()
        line3 = file.readline().strip()
        print(line1,line2,line3)

        for c in line1:
            if c in line2 and c in line3:
                print(c)
                total_score += item_score(c)
                break

print(total_score)
