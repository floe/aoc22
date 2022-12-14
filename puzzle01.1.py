#!/usr/bin/python

elf_sum = 0
largest = 0

with open("input1") as file:
    for line in file:
        line = line.strip()
        if line == "":
            if elf_sum > largest:
                largest = elf_sum
            elf_sum = 0
            continue
        elf_sum += int(line)

print(largest)
