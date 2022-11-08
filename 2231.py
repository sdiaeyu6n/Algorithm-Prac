N = int(input())
producers = []
for x in range(10):
    for y in range(10):
        for z in range(10):
            if 101 * x + 11 * y + 2 * z == N:
                producers.append(str(x) + str(y) + str(z))
if len(producers) == 0:
    print("0")
else:
    producers_int = list(map(int, producers))
    print(min(producers_int))