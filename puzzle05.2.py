#!/usr/bin/python3

stacks = []

for i in range(0,9):
    stacks.append([])

with open("input05") as file:

    # header
    while (line := file.readline()):
        print(line)
        if line[1] == "1":
            break
        for i in range(0,9):
            crate = line[i*4+1]
            if crate != " ":
                stacks[i].insert(0,crate)

    print(stacks)

    # body
    while (line := file.readline()):
        tokens = line.split()
        if len(tokens) == 0:
            continue
        c_num = int(tokens[1])
        s_from = int(tokens[3])-1
        s_to = int(tokens[5])-1

        tmp_crates = []
        for i in range(0,c_num):
            tmp_crates.append(stacks[s_from].pop())
        for i in range(0,c_num):
            stacks[s_to].append(tmp_crates.pop())

print(stacks)
print("".join([x[-1] for x in stacks]))

