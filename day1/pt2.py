f = open("input.txt", "r").read().splitlines()

total = 0
d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9 }

for l in f:
    curr = ""
    for i in range(len(l)):
        nextline = False
        if l[i].isnumeric():
            curr += str(l[i])
            break
        for key in d:
            if key == l[i:i+len(key)]:
                curr += str(d[key])
                nextline = True
                break
        if nextline == True:
            break
    for i in range(len(l)-1, -1, -1):
        nextline = False
        if l[i].isnumeric():
            curr += str(l[i])
            break
        for key in d:
            if key == l[i:i+len(key)]:
                curr += str(d[key])
                nextline = True
                break
        if nextline == True:
            break
    total += int(curr)

print(total)
