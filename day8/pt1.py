f = open("input.txt", "r").read().splitlines()

directions = f[0].replace('L', '0').replace('R', '1')

d = {}
for l in f[2:]:
    key = l.split()[0]
    left = l.split()[2].strip("(,")
    right = l.split()[3].strip(")")
    d[key] = [left, right]
    
curr = "AAA" 
counter = 0
directionsIndex = -1
while curr != "ZZZ":
    counter += 1
    directionsIndex += 1
    if directionsIndex == len(directions):
        directionsIndex = 0
    curr = d[curr][int(directions[directionsIndex])]

print(counter)
