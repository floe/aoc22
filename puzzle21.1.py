#!/usr/bin/python3

class Monkey:
    def __init__(self,name,op,n1,n2):
        self.name = name
        self.lp = []
        self.rp = []
        self.op = op
        self.n1 = n1
        self.n2 = n2
    def __repr__(self):
        return(str([ c.name for c in self.lp])+str([ c.name for c in self.rp])+str(self.n1)+str(self.op)+str(self.n2))

monkeys = {}
root = None

#with open("input21.tiny") as file:
with open("input21") as file:
    for line in file:
        myname, rest = line.strip().split(":")
        rest = rest.strip()
        if rest.isnumeric():
            monkeys[myname] = Monkey(myname,int(rest),None,None)
        else:
            m1,op,m2 = rest.split(" ")
            monkeys[myname] = Monkey(myname,op,m1,m2)

root = monkeys["root"]

for name,m in monkeys.items():
    if m.n1 == None:
        continue
    monkeys[m.n1].lp.append(m)
    monkeys[m.n2].rp.append(m)

while not isinstance(root.op,int):
    print(monkeys)
    for name,m in list(monkeys.items()):
        if isinstance(m.op,str):
            if not isinstance(m.n1,int) or not isinstance(m.n2,int):
                continue
            tmpstr = str(m.n1)+m.op+str(m.n2)
            tmpnum = int(eval(tmpstr))
            print(tmpstr,tmpnum)
            m.op = tmpnum
        if isinstance(m.op,int):
            for p in m.lp:
                p.n1 = m.op
            for p in m.rp:
                p.n2 = m.op
            monkeys.pop(name)

print(root.op)
