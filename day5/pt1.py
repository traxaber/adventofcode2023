f = open("input.txt", "r").read().splitlines()

seeds = f[0].replace("seeds:","").split()
minimumOutcome = int(seeds[0]) 
for seed in seeds:
    currentSeed = int(seed)
    mapping = int(seed)
    found = False
    i = 3
    while i < len(f) - 1:
        if found:
            i+=1
        l = f[i]
        if len(l) > 0 and l[0].isnumeric():
            source = int(l.split()[1])
            dest = int(l.split()[0])
            seedRange = int(l.split()[2])
            diff = dest - source
            if source <= currentSeed and currentSeed < source + seedRange:
                mapping = currentSeed + diff
                found = True
        else:
            currentSeed = mapping
            found = False
        i+=1
    if mapping < minimumOutcome:
        minimumOutcome = mapping

print(minimumOutcome)
