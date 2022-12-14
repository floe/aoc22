#!/usr/bin/python

elf_sum = 0
elves = []

with open("input1") as file:
	for line in file:
		line = line.strip()
		if line == "":
			elves.append(elf_sum)
			elf_sum = 0
			continue
		elf_sum = elf_sum + int(line)
		
elves.append(elf_sum)
print(elves)

elves.sort(reverse=True)
print(elves[0]+elves[1]+elves[2])
