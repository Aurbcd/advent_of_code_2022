#Part 1
with open('input.txt') as f:
    count = 0
    lines = f.readlines()
    for line in lines:
        l = line.split(",")
        elf1, elf2 = l[0], l[1]
        elf1 = elf1.split("-")
        elf2 = elf2.split("-")
        if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
            count += 1
        elif int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
            count += 1
    print(count)

#Part 2
with open('input.txt') as f:
    count = 0
    lines = f.readlines()
    for line in lines:
        l = line.split(",")
        elf1, elf2 = l[0], l[1]
        elf1 = [i for i in range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)]
        elf2 = [i for i in range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1)]
        if len(set(elf1).intersection(set(elf2))) > 0:
            count += 1
    print(count)