#!/usr/bin/python3

import itertools,random

class Valve:
    def __init__(self,name,flow,nbs):
        self.name = name
        self.flow = flow
        self.nbs = nbs

locations = {}
valves = []

dist = {}
path = {}

def init_graph():
    for i in locations:
        for j in locations:
            dist[i+j] = 1000000
            path[i+j] = None
 
    for k,v in locations.items():
        dist[k+k] = 0
        path[k+k] = k
        for nb in v.nbs:
            dist[k+nb] = 1
            path[k+nb] = nb
    
    for k in locations:
        for i in locations:
            for j in locations:
                distsum = dist[i+k] + dist[k+j]
                if dist[i+j] > distsum:
                    dist[i+j] = distsum
                    path[i+j] = path[i+k]

    #print(dist["AAHH"])

def find_path(start,end):
    if path[start+end] == None:
        return([])
    mypath = []
    current = start
    while current != end:
        current = path[current+end]
        mypath.append(current)
    return(mypath)

def check_solution(solution):
    
    minutes = 30
    opened = []
    released = 0

    current = locations["AA"]

    while minutes > 0:

        for v in opened:
            released += v.flow

        if len(solution) > 0:
            step = solution.pop(0)
            if "*" in step:
                opened.append(current)
            else:
                if not step in current.nbs:
                    return(-1)
                current = locations[step]

        minutes -= 1
        #print(current,minutes,released)

    return(released)

#with open("input16.tiny") as file:
with open("input16") as file:

    for line in file:
        line = line.strip()
        items = line.split(" ")
        name = items[1]
        flow = int(items[4].strip(";").split("=")[1])
        nbs = [ s.strip(",") for s in items[9:] ]
        newvalve = Valve(name,flow,nbs)
        locations[name] = newvalve
        if flow > 0:
            valves.append(newvalve)
        #print(name,flow,nbs)

init_graph()
#print(find_path("WF","CT"))
#tiny_sol = ["DD","*","CC","BB","*","AA","II","JJ","*","II","AA","DD","EE","FF","GG","HH","*","GG","FF","EE","*","DD","CC","*"]
#print(tiny_sol)
#print(check_solution(tiny_sol))
#test = [locations[n] for n in ['DD', 'BB', 'JJ', 'HH', 'EE', 'CC']]

valves.sort(key=lambda x: x.flow,reverse=True)
'''
values = [v.flow for v in valves]
minutes = 30 
opened = []
released = 0

while minutes > 0:
    for v in opened:
        released += v
    if len(values) > 0 and minutes % 2 == 0:
        opened.append(values.pop(0))
    minutes -= 1
print(released) # 3794, too high
# 2000, still too high
# 818, too low
'''
perms = itertools.permutations(valves)
maxp = 0

count = 0

for order in perms:

    solution = []
    current = locations["AA"]

    #print([ n.name for n in order])
    # one possible valve opening order
    for v in order:
        if v.name in current.nbs:
            solution.append(v.name)
            solution.append("*")
        else:
            tmppath = find_path(current.name, v.name)
            solution.extend(tmppath)
            solution.append("*")
        current = v
    #print(solution)

    result = check_solution(solution)
   
    if result > maxp:
        maxp = result

    count += 1
    if count % 10000 == 0:
        print(maxp)

print(maxp)
