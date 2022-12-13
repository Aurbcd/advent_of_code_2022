#Part 1
with open('input.txt') as f:
    lines = f.readlines()
    X = 1
    cycle = 0
    sum = 0
    for line in lines:
        line = line.split(' ')
        if line[0] == 'addx':
            for _ in range(2):
                cycle += 1
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    sum += cycle * X
            X += float(line[1])
        else:
            cycle += 1
            if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                sum += cycle * X
    print(int(sum))

#Part 2
with open('input.txt') as f:
    lines = f.readlines()
    cycle = 1
    sprite_position = 0
    CRT_row = ""
    for line in lines:
        line = line.split(' ')
        if line[0] == 'addx':
            for _ in range(2):
                cycle += 1
                if sprite_position <= len(CRT_row) % 40 <= sprite_position + 2:
                    CRT_row += "#"
                else:
                    CRT_row += "."
            sprite_position += float(line[1])
        else:
            cycle += 1
            if sprite_position <= len(CRT_row) % 40 <= sprite_position + 2:
                CRT_row += "#"
            else:
                CRT_row += "."
    for i in range(0, len(CRT_row), 40):
        print(CRT_row[i:i+40])