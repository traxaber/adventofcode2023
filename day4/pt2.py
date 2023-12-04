f = open("input.txt", "r").read().splitlines()

total = 0

def process(cardNumber):
    if cardNumber > len(f):
        return
    global total
    total += 1
    score = 0
    card = f[cardNumber]
    winners = card[10:40].split()
    myNumbers = card[41:].split()
    for num in myNumbers:
        if num in winners:
            score += 1
    for i in range(cardNumber + 1, cardNumber + score + 1):
        process(i)

for i in range(len(f)):
    process(i)
print(total)