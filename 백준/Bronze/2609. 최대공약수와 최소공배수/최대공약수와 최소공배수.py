N, M = map(int, input().split())
gcf = 0
for i in range(1, max(N, M)+1):
    if N % i == 0 and M % i == 0:
        gcf = i
print(gcf)

for i in range(1, max(N, M)+1):
    for j in range(1, max(N, M)+1):
        if N * i == M * j:
            print(N * i)
            quit()