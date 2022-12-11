import numpy as np
# Part 1
with open('input.txt') as f:
    count = 0
    lines = f.readlines()
    arr = np.array([list(line)[:-1] for line in lines]).astype(int)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[i]) - 1:
                count += 1
                continue
            line_left = arr[:i, j]
            line_right = arr[i + 1:, j]
            column_top = arr[i, :j]
            column_bottom = arr[i, j + 1:]
            if arr[i, j] > np.max(line_left) or arr[i, j] > np.max(line_right) \
                    or arr[i, j] > np.max(column_top) or arr[i, j] > np.max(column_bottom):
                count += 1
    print("Part 1:", count)


# Part 2
def tree_count(line, value):
    k = 0
    for l in range(0, len(line)):
        if line[l] >= value:
            k = l + 1
            break
    else:
        k = len(line)
    return k


with open('input.txt') as f:
    highest_score = 0
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            line_left_reversed = arr[:i, j][::-1]
            line_right = arr[i + 1:, j]
            column_top_reversed = arr[i, :j][::-1]
            column_bottom = arr[i, j + 1:]
            score = tree_count(line_left_reversed, arr[i, j]) * tree_count(line_right, arr[i, j]) \
                    * tree_count(column_top_reversed, arr[i, j]) * tree_count(column_bottom, arr[i, j])
            if score > highest_score:
                highest_score = score
    print("Part 2:", highest_score)