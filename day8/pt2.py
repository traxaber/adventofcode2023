import numpy as np 

f = open("input.txt", "r").read().splitlines()
directions = f[0].replace('L', '0').replace('R', '1')
d = {}
currs = []
for l in f[2:]:
    key = l.split()[0]
    if key[-1] == 'A':
        currs.append(key)
    left = l.split()[2].strip("(,")
    right = l.split()[3].strip(")")
    d[key] = [left, right]

counter = 0
directionsIndex = -1
solutions = {}
while len(solutions) < 6:
    counter += 1
    directionsIndex += 1
    if directionsIndex == len(directions):
        directionsIndex = 0
    for i in range(len(currs)):
        currs[i] = d[currs[i]][int(directions[directionsIndex])]
        if currs[i][-1] == 'Z':
            if i not in solutions:
                solutions[i] = counter

print(np.lcm.reduce(list(solutions.values())))