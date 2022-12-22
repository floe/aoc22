#!/usr/bin/python3

class Monkey:
    def __init__(self,name,op,n1,n2):
        self.name = name
        self.lp = []
        self.rp = []
        self.op = op
        self.n1 = n1
        self.n2 = n2
        self.result = None
    def __repr__(self):
        return(str([ c.name for c in self.lp])+str([ c.name for c in self.rp])+str(self.n1)+str(self.op)+str(self.n2)+"=="+str(self.result))

monkeys = {}
root = None

opinv = { "+":"-", "-":"+", "*":"/", "/":"*", "x":"" }

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
humn = monkeys["humn"]

root.op = "=="
humn.op = "x"

for name,m in monkeys.items():
    if m.n1 == None:
        continue
    monkeys[m.n1].lp.append(m)
    monkeys[m.n2].rp.append(m)

# propagate values upwards
changed = True
while changed:
    print(monkeys)
    changed = False
    for name,m in list(monkeys.items()):
        if isinstance(m.op,str):
            if not isinstance(m.n1,int) or not isinstance(m.n2,int):
                continue
            tmpstr = str(m.n1)+m.op+str(m.n2)
            tmpnum = int(eval(tmpstr))
            print(tmpstr,tmpnum)
            m.op = tmpnum
            changed = True
        if isinstance(m.op,int):
            for p in m.lp:
                p.n1 = m.op
            for p in m.rp:
                p.n2 = m.op
            monkeys.pop(name)
            changed = True

target = root.n1 if isinstance(root.n1,int) else root.n2
nextmk = root.n2 if isinstance(root.n1,int) else root.n1

nextmk = monkeys[nextmk]
print(target,nextmk)
nextmk.result = target

# propagate results downwards
while nextmk != humn:
    print(nextmk)#,monkeys)
    current = nextmk
    invop = opinv[current.op]

    if current.n1 == None and current.n2 == None:
        break

    if isinstance(current.n1,int): #5-x=10 -> 5-10=x    5+x=10 -> 10-5=x   5/x=10 -> 5/10=x  5*x=10 10/5=x
        if current.op in ["-","/"]:
            tmpstr = str(current.n1)+current.op+str(current.result)
        else:
            tmpstr = str(current.result)+invop+str(current.n1)
        nextmk = monkeys[current.n2]
    else:
        tmpstr = str(current.result)+invop+str(current.n2)
        nextmk = monkeys[current.n1]

    print(tmpstr)
    target = int(eval(tmpstr))
    nextmk.result = target

print(humn.result)
