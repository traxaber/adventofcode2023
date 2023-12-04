f = open("input.txt", "r").read().splitlines()

width = len(f[0])
height = len(f)
total = 0

d = {}

def shouldInclude(x1, x2, y, num):
    x = x1 - 1 if x1 > 0 else x1
    plus1 = 2 if x1 > 0 else 1
    if y - 1 >= 0:
        for i in range(x, x + len(num) + plus1):
            if i < width:
                if f[y-1][i] == '*':
                    if (y-1, i) not in d:
                        d[(y-1, i)] = [int(num)]
                    else:
                        d[(y-1, i)].append(int(num))
    if y + 1 < height:
        for i in range(x, x + len(num) + plus1):
            if i < width:
                if f[y+1][i] == '*':
                    if (y+1, i) not in d:
                        d[(y+1, i)] = [int(num)]
                    else:
                        d[(y+1, i)].append(int(num))
    if x1 - 1 >= 0:
        if f[y][x1 - 1] == '*':
            if (y, x1-1) not in d:
                d[(y, x1-1)] = [int(num)]
            else:
                d[(y, x1-1)].append(int(num))
    if x2 + 1 < width:
        if f[y][x2 + 1] == '*':
            if (y, x2+1) not in d:
                d[(y, x2+1)] = [int(num)]
            else:
                d[(y, x2+1)].append(int(num))

y = 0
while y < len(f):
    x = 0
    while x < len(f[y]):
        if f[y][x].isnumeric():
            num = ""
            x1 = x
            while x < width and f[y][x].isnumeric():
                num += str(f[y][x])
                x2 = x
                x+=1
            shouldInclude(x1, x2, y, num)
        else:
            x += 1
    y += 1

for key in d:
    if len(d[key]) == 2:
        total += d[key][0] * d[key][1]
            
print(total)