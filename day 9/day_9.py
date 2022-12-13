#Part 1
import numpy as np


def is_next_to_head(head, tail):
    return np.linalg.norm(np.array(head) - np.array(tail)) < 1.5

with open('input.txt') as f:
    list_positions = []
    head = (0, 0)
    tail = (0, 0)
    lines = f.readlines()
    for line in lines:
        l = line.split(" ")
        direction = l[0]
        steps = int(l[1])
        for s in range(steps):
            if direction == "R":
                head = (head[0]+1, head[1])
            elif direction == "L":
                head = (head[0]-1, head[1])
            elif direction == "U":
                head = (head[0], head[1]+1)
            elif direction == "D":
                head = (head[0], head[1]-1)
            if not is_next_to_head(head, tail):
                step = np.array(head) - np.array(tail)
                s = [s//2 if (s != -1 and s != 1) else s for s in step]
                tail = (tail[0]+s[0], tail[1]+s[1])
                if tail not in list_positions:
                    list_positions.append(tail)
    print(len(list_positions)) #6189 too low


