#Part 1
with open('input.txt') as f:
    priorities = 0
    lines = f.readlines()
    for line in lines:
        first_compartment = line[:len(line)//2]
        second_compartment = line[len(line)//2:]
        shared_type = [el for el in first_compartment if el in second_compartment]
        if len(shared_type) > 0:
            el = shared_type[0]
            if el.upper() == el:
                priorities += ord(el) - 38
            else:
                priorities += ord(el) - 96
    print(priorities)

#Part 2
with open('input.txt') as f:
    priorities = 0
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        group = lines[i:i+3]
        shared_type_ones = [el for el in group[0] if el in group[1] and el in group[2]]
        el = shared_type_ones[0]
        if el.upper() == el:
            priorities += ord(el) - 38
        else:
            priorities += ord(el) - 96
    print(priorities)