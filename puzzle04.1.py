#!/usr/bin/python3

total_score = 0

with open("input04") as file:
    while (line := file.readline().strip()):

        # split each line into start and end number of tasks
        tasks = line.split(",")
        elf0 = tasks[0].split("-")
        elf1 = tasks[1].split("-")

        start0 = int(elf0[0])
        start1 = int(elf1[0])

        end0 = int(elf0[1])
        end1 = int(elf1[1])

        # calculate the number of tasks for each elf
        tasksize0 = end0 - start0 + 1
        tasksize1 = end1 - start1 + 1

        if tasksize0 < tasksize1:
            if end0 <= end1 and start0 >= start1:
                total_score += 1
        else:
            if end1 <= end0 and start1 >= start0:
                total_score += 1
         
        print(elf0,elf1,tasksize0,tasksize1)

print(total_score)
