f = open("input.txt", "r").read().splitlines()

seeds = f[0].replace("seeds: ", "").split()

def inSeeds(mapping):
    for i in range(0, len(seeds), 2):
        if mapping >= int(seeds[i]) and mapping < int(seeds[i]) + int(seeds[i+1]):
            return True
    return False

start = int(f[-1].split()[0])
for l in reversed(f):
    if l[0].isalpha():
        break
    if int(l.split()[0]) < start:
        start = int(l.split()[0])

done = False
while True:
    mapping = start
    for l in reversed(f[3:]):
        l = l.split()
        if len(l) == 0 or l[0][0].isalpha():
            done = False
            continue
        elif done == True:
            continue
        if  mapping >= int(l[0]) and mapping < int(l[0]) + int(l[2]):
            mapping = mapping - int(l[0]) + int(l[1])
            done = True 
    if inSeeds(mapping):
        print(start)
        break
    start += 1