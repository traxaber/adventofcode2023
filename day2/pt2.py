f = open("input.txt", "r").read().splitlines()

total = 0
for l in f:
    redMax = 0
    greenMax = 0
    blueMax = 0
    gameId = l.split()[1][:-1]
    relevantValues = l.replace('Game %s'%(gameId), "").replace(":","").replace(",","").replace(";","").split()
    for i in range(0, len(relevantValues), 2):
        count = int(relevantValues[i])
        color = relevantValues[i + 1]
        if color == "red" and count > redMax:
            redMax = count
        elif color == "green" and count > greenMax:
            greenMax = count
        elif color == "blue" and count > blueMax:
            blueMax = count
    total += redMax * greenMax * blueMax

print(total)    

