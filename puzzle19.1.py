#!/usr/bin/python3

import copy

class Blueprint:
    def __init__(self,ore_cost,clay_cost,obs_cost1,obs_cost2,ge_cost1,ge_cost2):
        self.ore  = int(ore_cost)  # ore
        self.clay = int(clay_cost) # ore
        self.obs  = [ int(obs_cost1), int(obs_cost2) ] # ore, clay
        self.ge   = [ int(ge_cost1),  int(ge_cost2)  ] # ore, obsidian

class State:
    def __init__(self,ore,clay,obs,geode,ore_rob,clay_rob,obs_rob,ge_rob):
        self.resources = { "ore": ore, "clay": clay, "obs": obs, "geode": geode }
        self.robots = { "ore": ore_rob, "clay": clay_rob, "obs": obs_rob, "geode": ge_rob }

    def __str__(self):
        return(str(self.resources) + " " + str(self.robots))

    def collect(self):
        for k,v in self.robots.items():
            self.resources[k] += v


    def next_states(self,bp):
        result = []

        possible_robots = {}

        if self.resources["ore"] >= bp.ore:
            possible_robots["ore"] = True
        if self.resources["ore"] >= bp.clay:
            possible_robots["clay"] = True
        if self.resources["ore"] >= bp.obs[0] and self.resources["clay"] >= bp.obs[1]:
            possible_robots["obs"] = True
        if self.resources["ore"] >= bp.ge[0] and self.resources["obs"] >= bp.ge[1]:
            possible_robots["geode"] = True

        # collect resources
        newstate = copy.deepcopy(self)
        newstate.collect()

        # do nothing
        result.append(newstate)

        # build a robot
        for k,v in possible_robots.items():
            nextstate = copy.deepcopy(newstate)
            nextstate.robots[k] += 1
            if k == "ore":
                nextstate.resources["ore"] -= bp.ore
            if k == "clay":
                nextstate.resources["ore"] -= bp.clay
            if k == "obs":
                nextstate.resources["ore" ] -= bp.obs[0]
                nextstate.resources["clay"] -= bp.obs[1]
            if k == "geode":
                nextstate.resources["ore"] -= bp.ge[0]
                nextstate.resources["obs"] -= bp.ge[1]
            result.append(nextstate)

        return(result)


blueprints = []

with open("input19.tiny") as file:
#with open("input19") as file:

    for line in file:
        line = line.strip()
        items = line.split(" ")
        bp = Blueprint(items[6],items[12],items[18],items[21],items[27],items[30])
        blueprints.append(bp)

for bp in blueprints:
    print(bp.ge)

startstate = State(0,0,0,0,1,0,0,0)
print(startstate)
options = startstate.next_states(blueprints[0])

for i in range(1,24):
    new_opts = []
    for n in options:
        print(n)
        tmp = n.next_states(blueprints[0])
        for t in tmp:
            print("  "+str(t))
        new_opts.extend(tmp)
    print(len(new_opts))
    options = new_opts
