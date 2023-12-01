f = open("input.txt", "r").read().splitlines()

total = 0
for l in f:
    curr = ""
    for char in l:
        if char.isnumeric():
            curr += char
            break
    for i in range(len(l)-1, -1, -1):
        if l[i].isnumeric():
            curr += l[i]
            break
    total += int(curr)

print(total)
