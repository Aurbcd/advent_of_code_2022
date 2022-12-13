#Part 1
with open('input.txt') as f:
    lines = f.readlines()
    monkeys = []
    monkeys_inspected_times = []
    #round 0
    for i in range(0, len(lines), 7):
        monkeys.append(list(map(int, lines[i+1][17:].split(','))))
        monkeys_inspected_times.append(0)
    for round in range(20):
        #round 1-20
        for i in range(0, len(lines), 7):
            for _ in range(len(monkeys[i//7])):
                monkeys_inspected_times[i//7] += 1
                old = monkeys[i//7].pop(0)
                exec(lines[i+2][13:])
                new = new // 3
                test_value = int(lines[i+3][21:])
                if new % test_value == 0:
                    monkeys[int(lines[i+4][-2])].append(new)
                else:
                    monkeys[int(lines[i+5][-2])].append(new)
    print("Part one :", sorted(monkeys_inspected_times)[-1]*sorted(monkeys_inspected_times)[-2])

#Part 2 NOT SUCEEDED
from math import gcd
import numpy as np

def factorization(n): #utiliser la factorisation en facteurs premiers
    factors = []
    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1
        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)
            cycle_size *= 2
            x_fixed = x
        return factor
    while n > 1:
        next = get_factor(n)
        factors.append(next)
        n //= next
    return list(set(factors))

with open('input.txt') as f:
    lines = f.readlines()
    monkeys = []
    monkeys_inspected_times = []
    #round 0
    for i in range(0, len(lines), 7):
        monkeys.append(list(map(factorization, map(int, lines[i+1][17:].split(',')))))
        monkeys_inspected_times.append(0)
    for round in range(20):
        #print("monkeys:", monkeys)
        #print("compte", monkeys_inspected_times)
        #round 1-20
        for i in range(0, len(lines), 7):
            #print("oui", i//7)
            for _ in range(len(monkeys[i//7])):
                monkeys_inspected_times[i//7] += 1
                old_list = monkeys[i//7].pop(0)
                old = int(np.prod(old_list))
                exec(lines[i+2][13:])
                new = factorization(new//3)
                #print(old, "new", new, int(lines[i+3][21:]))
                test_value = int(lines[i+3][21:])
                if any([x in new for x in factorization(test_value)]):
                    #print("True", new)
                    monkeys[int(lines[i+4][-2])].append(new)
                else:
                    #print("False", new)
                    monkeys[int(lines[i+5][-2])].append(new)
                    #print(monkeys)
        if round % 1000 == 0:
            pass
            #print(round, monkeys_inspected_times)
    #print(sorted(monkeys_inspected_times)[-1]*sorted(monkeys_inspected_times)[-2]) #14412722760 too low