import numpy as np

with open('input.txt') as f:
    lines = f.readlines()
    calories = []
    line_index = 0
    calories.append(0)
    while line_index < len(lines):
        while lines[line_index] != '\n':
            calories[-1] += (int(lines[line_index]))
            line_index += 1
            if line_index == len(lines):
                break
        calories.append(0)
        line_index += 1
    #part 1
    print(max(calories))
    #part 2
    print(np.sum(np.sort(calories)[-3:]))