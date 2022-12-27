#!/usr/bin/python3

numbers_orig = []
numbers = []
zeronum = None

class Mynum:
    def __init__(self,num,pos):
        self.num = num * 811589153
        self.pos = pos
    def __str__(self):
        return(str(self.num))

#with open("input20.tiny") as file:
with open("input20") as file:
    i = 0
    for line in file:
        num = int(line.strip())
        mynum = Mynum(num,i)
        numbers_orig.append(mynum)
        numbers.append(mynum)
        if num == 0:
            zeronum = mynum

count = len(numbers)
print(count)

for i in range(0,10):
    for i,x in enumerate(numbers_orig):
        curpos = numbers.index(x)
        newpos = (curpos+x.num)%(count-1)
        if newpos == count:
            newpos = 0 
        #print(x.num,": from/to: ",curpos,newpos)
        numbers.pop(curpos)
        numbers.insert(newpos,x)
    print([ str(n) for n in numbers ])

zeropos = numbers.index(zeronum)
i1 = (zeropos+1000) % count
i2 = (zeropos+2000) % count
i3 = (zeropos+3000) % count

n1 = numbers[i1].num
n2 = numbers[i2].num
n3 = numbers[i3].num

print(n1,n2,n3,n1+n2+n3)

