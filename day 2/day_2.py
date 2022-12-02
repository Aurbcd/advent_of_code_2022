#Part 1
with open('input.txt') as f:
    score = 0
    lines = f.readlines()
    for line in lines:
        l = line.split(" ")
        will_play, to_play = l[0], l[1][0]
        if to_play == "X":
            score += 1
            if will_play == "A":
                score += 3
            elif will_play == "B":
                score += 0
            elif will_play == "C":
                score += 6
        elif to_play == "Y":
            score += 2
            if will_play == "A":
                score += 6
            elif will_play == "B":
                score += 3
            elif will_play == "C":
                score += 0
        elif to_play == "Z":
            score += 3
            if will_play == "A":
                score += 0
            elif will_play == "B":
                score += 6
            elif will_play == "C":
                score += 3
    print(score)

#Part 2
with open('input.txt') as f:
    score = 0
    lines = f.readlines()
    for line in lines:
        l = line.split(" ")
        will_play, outcome = l[0], l[1][0]
        if outcome == "X":
            score += 0
            if will_play == "A":
                score += 3
            elif will_play == "B":
                score += 1
            elif will_play == "C":
                score += 2
        elif outcome == "Y":
            score += 3
            if will_play == "A":
                score += 1
            elif will_play == "B":
                score += 2
            elif will_play == "C":
                score += 3
        elif to_play == "Z":
            score += 6
            if will_play == "A":
                score += 2
            elif will_play == "B":
                score += 3
            elif will_play == "C":
                score += 1
    print(score)