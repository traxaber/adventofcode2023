f = open("input.txt", "r").read().splitlines()

time = int(f[0].replace(' ', '').replace("Time:", ""))
distance = int(f[1].replace(' ', '').replace("Distance:", ""))

i1 = 0
i2 = time 
while True:
    if (time-i1)*i1 > distance:
        break
    i1 += 1
while True:
    if (time-i2)*i2 > distance:
        break
    i2 -= 1

print(i2 - i1 + 1)