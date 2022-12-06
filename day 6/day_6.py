#Part 1
with open('input.txt') as f:
    line = f.readline()
    for i in range(3, len(line)):
        possible_marker = line[i-3:i+1]
        if len(possible_marker) == len((set(possible_marker))):
            print(i+1)
            break
#Part 2
with open('input.txt') as f:
    line = f.readline()
    for i in range(13, len(line)):
        possible_marker = line[i-13:i+1]
        if len(possible_marker) == len((set(possible_marker))):
            print(i+1)
            break