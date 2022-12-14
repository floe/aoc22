#!/usr/bin/python

move_scores = { "A": 1, "B": 2, "C": 3 }
lose_moves = { "A": "C", "B": "A", "C": "B" } 
win_moves = { "A": "B", "B": "C", "C": "A" } 
total_score = 0

with open("input02") as file:
    for line in file:
        moves = line.strip().split()
        them = moves[0]
        outcome = moves[1]
        print(them,outcome)

        if outcome == "Y":
            mine = them
            total_score += 3

        if outcome == "X":
            mine = lose_moves[them]

        if outcome == "Z":
            total_score += 6
            mine = win_moves[them]

        total_score += move_scores[mine]

print(total_score)
