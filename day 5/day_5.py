#Part 1
def get_number_piles(lines):
    i = 0
    while not lines[i].split(' ')[1].isnumeric():
        i += 1
    return int([t for t in lines[i].split() if t.isnumeric()][-1]), i

with open('input.txt') as f:
    lines = f.readlines()
    #Building piles
    n_piles, n = get_number_piles(lines)
    piles = {i+1:[] for i in range(n_piles)}
    for line in lines[:n]:
        for i in range(n_piles):
            el = line[i*4:i*4+3]
            if '[' in el:
                piles[i+1].insert(0, el)
    #Moving the elements
    for line in lines[n+2:]:
        l = line.split(' ')
        number = int(l[1])
        from_pile = int(l[3])
        to_pile = int(l[5])
        for _ in range(number):
            piles[to_pile].append(piles[from_pile].pop(-1))
    display = ""
    for i in [p[-1] for p in piles.values()]:
        display += i[1:-1]
    print(display)

#Part 2
with open('input.txt') as f:
    lines = f.readlines()
    #Building piles
    n_piles, n = get_number_piles(lines)
    piles = {i+1:[] for i in range(n_piles)}
    for line in lines[:n]:
        for i in range(n_piles):
            el = line[i*4:i*4+3]
            if '[' in el:
                piles[i+1].insert(0, el)
    #Moving the elements
    for line in lines[n+2:]:
        l = line.split(' ')
        number = int(l[1])
        from_pile = int(l[3])
        to_pile = int(l[5])
        piles[to_pile] += piles[from_pile][-number:]
        piles[from_pile] = piles[from_pile][:-number]
    display = ""
    for i in [p[-1] for p in piles.values()]:
        display += i[1:-1]
    print(display)