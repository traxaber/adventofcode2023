f = open("input.txt", "r").read().splitlines()

total = 0

for l in f:
    score = 0
    winners = l[10:40].split()
    myNumbers = l[41:].split()
    for num in myNumbers:
        if num in winners:
            score += 1
    total += 2**(score-1) if score > 0 else 0

print(total)