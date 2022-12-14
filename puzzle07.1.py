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
        if self.size < 100000 and len(self.children) > 0:
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

print(sum([x.size for x in small_dirs]))
