N = int(input())
people_list = []

for i in range(N):
    people_list.append(list(map(int, input().split())))    # [140,60]  // [140,60]2
rank = [1 for i in range(N)]
for j in range(N):
    for k in range(N):
        if people_list[j][0]<people_list[k][0] and people_list[j][1]<people_list[k][1]:
            rank[j]+=1

for i in rank:
    print(i, end=' ')