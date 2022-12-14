#!/usr/bin/python3

pairs = []
pairsum = 0

def check_order(prefix,part1,part2):
    #print(prefix+"check_order",part1,part2)

    if isinstance(part1,int) and isinstance(part2,int):
        #print(prefix+"checking ints: ",part1,part2)
        if part1 < part2:
            return(True)
        if part1 > part2:
            return(False)
        return(None)

    if isinstance(part1,list) and isinstance(part2,list):
        #print(prefix+"checking lists: ",part1,part2)
        index = 0
        res = None
        while res == None:
            #print(prefix+"checking index "+str(index))
            if index >= len(part1) and index >= len(part2):
                return(None)
            if index >= len(part1):
                return(True)
            if index >= len(part2):
                return(False)
            res = check_order(prefix+"  ",part1[index],part2[index])
            index += 1
        return(res)

    if isinstance(part1,int) and isinstance(part2,list):
        return(check_order(prefix+"  ",[part1],part2))

    if isinstance(part1,list) and isinstance(part2,int):
        return(check_order(prefix+"  ",part1,[part2]))

    # never come here
    you_shall_not_pass()

with open("input13") as file:

    parts = []
    while (line := file.readline()):
        line = line.strip()
        if line == "":
            continue
        part = eval(line)
        parts.append(part)
        if len(parts) == 2:
            pairs.append(parts)
            parts = []

for i in range(0,len(pairs)):
    pair = pairs[i]
    print(pair)
    if check_order("  ",pair[0],pair[1]):
        pairsum += i+1

print(pairsum)
