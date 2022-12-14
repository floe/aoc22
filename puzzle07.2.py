#!/usr/bin/python3

small_dirs = []

class DirEntry:

    def __init__(self,parent,size=0):
        self.is_file = False
        self.size = size
        self.children = {}
        self.parent = parent

    def print(self,prefix=""):
        for n,c in self.children.items():
            print(prefix+n+" "+str(c.size))
            c.print(prefix+"  ")

    def calc_size(self):
        self.size = 0
        for n,c in self.children.items():
            if c.size == "dir":
                c.calc_size()
            self.size += int(c.size)
        if len(self.children) > 0:
            small_dirs.append(self)

root = DirEntry(None)
current = root

with open("input07") as file:

    while (line := file.readline().strip()):

        # command
        if line[0] == "$":
            tokens = line.split()
            if tokens[1] == "cd":
                dirname = tokens[2]
                if dirname == "/":
                    current = root
                elif dirname == "..":
                    current = current.parent
                else:
                    if dirname not in current.children:
                        current.children[dirname] = DirEntry(current)
                    current = current.children[dirname]
            #elif tokens[1] == "ls":
            #    print(tokens[1])
        else:
            size,name= line.split()
            current.children[name] = DirEntry(current,size)

root.calc_size()
root.print()

free_space = 70000000 - root.size
missing = 30000000 - free_space
smallest = 10000000000

print(missing)

for d in small_dirs:
    if d.size < missing:
        continue
    if d.size > smallest:
        continue
    smallest = d.size

print(smallest)
