import collections
import copy

f = open("input.txt", "r").read().splitlines()

def determineHandWithJokers(hand):
    if hand == hand[0]*5:
        return determineHand(hand)
    if determineHand(hand) > 0:
        return determineHand(hand.replace('J', collections.Counter(hand.replace('J','')).most_common(1)[0][0]))
    else:
        return determineHand(hand.replace('J', sorted(hand.replace('J',''))[-1]))

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
    hand = l.split()[0].replace('Q','X').replace('K','Y').replace('A','Z')
    bid = int(l.split()[1])
    bidDictionary[hand] = bid
    sortedHands[determineHandWithJokers(hand)].append(hand)

counter = 1
total = 0

for i in range(len(sortedHands)):
    for j in range(len(sortedHands[i])):
        sortedHands[i][j] = sortedHands[i][j].replace('J','1')
    sortedHands[i] = sorted(sortedHands[i])
    for j in range(len(sortedHands[i])):
        total += counter*bidDictionary[sortedHands[i][j].replace('1','J')]
        counter += 1

print(total)
