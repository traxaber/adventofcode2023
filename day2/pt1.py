f = open("input.txt", "r").read().splitlines()

total = 0
for l in f:
    invalid = False
    gameId = l.split()[1][:-1]
    relevantValues = l.strip('Game %s'%(gameId)).replace(":","").replace(",","").replace(";","").split()
    for i in range(0, len(relevantValues), 2):
        count = int(relevantValues[i])
        color = relevantValues[i + 1]
        if (color == "red" and count > 12) or (color == "green" and count > 13) or (color == "blue" and count > 14):
            invalid = True
    if not invalid:
        total += int(gameId)

print(total)
    

