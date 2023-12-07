f = open("input.txt", "r").read().splitlines()

def determineHand(hand):
    if hand == hand[0]*5:
        return 6
    d = {}
    for card in hand:
        if card not in d:
            d[card] = 1
        else:
            d[card] += 1
    if len(d) == 2:
        if 4 in d.values():
            return 5
        if 3 in d.values():
            return 4
    if len(d) == 3:
        if 3 in d.values():
            return 3
        if 2 in d.values():
            return 2
    if len(d) == 4:
        return 1
    if len(d) == 5:
        return 0

sortedHands = [[] for i in range(7)]

bidDictionary = {}

for l in f:
    hand = l.split()[0].replace('J','W').replace('Q','X').replace('K','Y').replace('A','Z')
    bid = int(l.split()[1])
    bidDictionary[hand] = bid
    sortedHands[determineHand(hand)].append(hand)

counter = 1
total = 0
for hands in sortedHands:
    for hand in sorted(hands):
        total += counter*bidDictionary[hand]
        counter += 1

print(total)
