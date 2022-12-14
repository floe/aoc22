#!/usr/bin/python

move_scores = { "X": 1, "Y": 2, "Z": 3 }
total_score = 0

with open("input02") as file:
    for line in file:
        moves = line.strip().split()
        them = chr(ord(moves[0])+23)
        mine = moves[1]
        print(them,mine)
        total_score += move_scores[mine]
        if them == mine:
            total_score += 3
        else:
            if them == "X" and mine == "Y":
                total_score += 6
            if them == "Y" and mine == "Z":
                total_score += 6
            if them == "Z" and mine == "X":
                total_score += 6

print(total_score)
