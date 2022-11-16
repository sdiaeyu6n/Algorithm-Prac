N = int(input())
people_list = []

for i in range(N):
    people_list.append(list(map(int, input().split())))
smaller = [0 for i in range(N)]
for j in range(N):
    for k in range(N):
        if min((people_list[j], people_list[k]), key=lambda x: x[1]) == people_list[j] \
                and min((people_list[j], people_list[k])) == people_list[j]:
            smaller[j] += 1

rank=[]
for i in range(N):
    rank.append(smaller[i])

for i in rank:
    print(i, end=' ')