f = open("input.txt", "r").read().splitlines()

times = [int(time) for time in f[0].split()[1:]]
distances = [int(distance) for distance in f[1].split()[1:]]
answer = 1

for race in range(len(times)):
    winners = 0
    for i in range(times[race]):
        if (times[race] - i)*i > distances[race]:
            winners += 1
    answer *= winners

print(answer)

