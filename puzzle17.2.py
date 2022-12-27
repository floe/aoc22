#!/usr/bin/python3

import itertools,random

chamber = []

def check_plus(x,y):
    return(x >= 0 and x <= 4 and
       chamber[y+1][x+1] == "." and
       chamber[y+1][x  ] == "." and
       chamber[y  ][x+1] == "." and
       chamber[y+1][x+2] == "." and
       chamber[y+2][x+1] == ".")

def check_hbar(x,y):
    return(x >= 0 and x <= 3 and
       chamber[y][x  ] == "." and
       chamber[y][x+1] == "." and
       chamber[y][x+2] == "." and
       chamber[y][x+3] == ".")

def check_vbar(x,y):
    return(x >= 0 and x <= 6 and
       chamber[y  ][x] == "." and
       chamber[y+1][x] == "." and
       chamber[y+2][x] == "." and
       chamber[y+3][x] == ".")

def check_block(x,y):
    return(x >= 0 and x <= 5 and
       chamber[y  ][x  ] == "." and
       chamber[y+1][x  ] == "." and
       chamber[y+1][x+1] == "." and
       chamber[y  ][x+1] == ".")

def check_revl(x,y):
    return(x >= 0 and x <= 4 and
       chamber[y  ][x  ] == "." and
       chamber[y  ][x+1] == "." and
       chamber[y  ][x+2] == "." and
       chamber[y+1][x+2] == "." and
       chamber[y+2][x+2] == ".")

def set_plus(x,y):
    if x < 0 or x > 4:
        return
    chamber[y+1][x+1] = "#"
    chamber[y+1][x  ] = "#"
    chamber[y  ][x+1] = "#"
    chamber[y+1][x+2] = "#"
    chamber[y+2][x+1] = "#"

def set_hbar(x,y):
    #return(x >= 0 x <= 3
    chamber[y][x  ] = "#"
    chamber[y][x+1] = "#"
    chamber[y][x+2] = "#"
    chamber[y][x+3] = "#"

def set_vbar(x,y):
    #return(x >= 0 x <= 6
    chamber[y  ][x] = "#"
    chamber[y+1][x] = "#"
    chamber[y+2][x] = "#"
    chamber[y+3][x] = "#"

def set_block(x,y):
    #return(x >= 0 x <= 5
    chamber[y  ][x  ] = "#"
    chamber[y+1][x  ] = "#"
    chamber[y+1][x+1] = "#"
    chamber[y  ][x+1] = "#"

def set_revl(x,y):
    #return(x >= 0 x <= 4
    chamber[y  ][x  ] = "#"
    chamber[y  ][x+1] = "#"
    chamber[y  ][x+2] = "#"
    chamber[y+1][x+2] = "#"
    chamber[y+2][x+2] = "#"

gasjets = []
curjet = 0

rocks = [ "-", "+", "L", "|", "#" ]
check = [ check_hbar, check_plus, check_revl, check_vbar, check_block ]
setrk = [ set_hbar, set_plus, set_revl, set_vbar, set_block ]
height = [ 1, 3, 3, 4, 2 ]
currock = 0
toppos = 1


#rockcount = 2022
rockcount = 1000000000000

def check_direction(x,y,direc):
    if direc == ">":
        return(check[currock%5](x+1,y))
    if direc == "<":
        return(check[currock%5](x-1,y))
    if direc == "v":
        return(check[currock%5](x,y-1))

def simulate_rock(rocknum,starty):
    #print("simulate: ",rocknum,starty)
    global toppos,curjet
    x = 2
    y = starty
    while True:
        jet = gasjets[curjet % len(gasjets)]
        curjet += 1
        
        if check_direction(x,y,jet):
            if jet == "<":
                x -= 1
            else:
                x += 1
        if check_direction(x,y,"v"):
            y -= 1
        else:
            nextpos = y+height[currock%5]
            if nextpos > toppos:
                toppos = nextpos
            setrk[currock%5](x,y)
            return

#with open("input17.tiny") as file:
with open("input17") as file:

    for line in file:
        line = line.strip()
        for c in line:
            gasjets.append(c)

chamber.append([ "#" for j in range(0,7) ])

for i in range(0,15000): #rockcount//5*13):
    chamber.append([ "." for j in range(0,7) ])

tops = {}

for i in range(0,rockcount):

    if currock % 5 == 0:
        if curjet%len(gasjets) in tops:
            #print(i,toppos-1,curjet,curjet%len(gasjets),tops[curjet%len(gasjets)],len(tops))
            break
        if chamber[toppos-1][3] == "#":
            tops[curjet%len(gasjets)] = [ toppos-1, currock ]

    simulate_rock(currock%5,toppos+3)
    currock += 1

#print(sorted(tops.items()))

loopstart = tops[curjet % len(gasjets)][0]
loopend = toppos-1
looplen = loopend-loopstart

startrock = tops[curjet % len(gasjets)][1]
endrock = currock
rocklen = endrock-startrock

print(loopstart,loopend,looplen)
print(startrock,endrock,rocklen)

rest = rockcount - startrock
iterations = rest // rocklen

remainder = rest % rocklen
print(rest,iterations,remainder)

for i in range(0,remainder):
    simulate_rock(currock%5,toppos+3)
    currock += 1

height = loopstart + (iterations * looplen) + (toppos-1-loopend)
print(height)

