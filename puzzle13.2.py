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

class Message:
    def __init__(self,content):
        self.items = content
    def __lt__(self,other):
        return(check_order("",self.items,other.items))

with open("input13") as file:

    while (line := file.readline()):
        line = line.strip()
        if line == "":
            continue
        part = eval(line)
        pairs.append(Message(part))

pairs.append(Message([[2]]))
pairs.append(Message([[6]]))
pairmult = 1

pairs.sort()

for i in range(0,len(pairs)):
    print(pairs[i].items)
    if pairs[i].items == [[2]] or pairs[i].items == [[6]]:
        pairmult *= i+1

print(pairmult)
