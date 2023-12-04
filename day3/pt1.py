f = open("input.txt", "r").read().splitlines()

width = len(f[0])
height = len(f)
total = 0

def isSymbol(char):
    return not char.isnumeric() and char != '.'

def shouldInclude(x1, x2, y, num):
    x = x1 - 1 if x1 > 0 else x1
    plus1 = 2 if x1 > 0 else 1
    if y - 1 >= 0:
        for i in range(x, x + len(num) + plus1):
            if i < width:
                if isSymbol(f[y-1][i]):
                    return True
    if y + 1 < height:
        for i in range(x, x + len(num) + plus1):
            if i < width:
                if isSymbol(f[y+1][i]):
                    return True
    if x1 - 1 >= 0:
        if isSymbol(f[y][x1 - 1]):
            return True
    if x2 + 1 < width:
        if isSymbol(f[y][x2 + 1]):
            return True
    return False

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
            if shouldInclude(x1, x2, y, num):
                total += int(num)
        else:
            x += 1
    y += 1
            
print(total)