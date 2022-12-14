#!/usr/bin/python3

class Monkey:
    def __init__(self):
        self.items = []
        self.op = ""
        self.test = 1
        self.next = { True:0, False:0 }
        self.activity = 0

monkeys = []
business = []
divisor = 1

current = None

with open("input11") as file:

    while (line := file.readline()):

        if line.strip() == "":
            continue

        tmp,num = line.split()
        if tmp == "Monkey":
            current = Monkey()
            monkeys.append(current)

        line = file.readline().strip()
        tmp,items = line.split(":")
        current.items = [ int(x.strip()) for x in items.split(",") ]

        line = file.readline().strip()
        tmp,op = line.split(":")
        current.op = op.split("=")[-1].strip() # TODO how to handle this?

        line = file.readline().strip()
        tmp,op = line.split(":")
        current.test = int(op.split(" ")[-1])
        divisor *= current.test

        line = file.readline().strip()
        tmp,op = line.split(":")
        current.next[True] = int(op.split(" ")[-1])

        line = file.readline().strip()
        tmp,op = line.split(":")
        current.next[False] = int(op.split(" ")[-1])

#for m in monkeys:
#    print(m.items,m.op,m.test,m.next,m.activity)
print(divisor)

# rounds
for r in range(0,10000):
    if r % 10 == 0:
        print(r)
    for m in monkeys:
        while len(m.items) > 0:
            m.activity += 1
            level = m.items.pop(0)
            tmp = m.op.replace("old",str(level))
            level = eval(tmp)
            test = level % m.test
            target = m.next[test == 0]
            level = level % divisor
            monkeys[target].items.append(level)
 
for m in monkeys:
    print(m.op,m.test,m.next,m.activity)
    business.append(m.activity)

business = sorted(business)
print(business[-3:-1])
print(business[-2]*business[-1])
