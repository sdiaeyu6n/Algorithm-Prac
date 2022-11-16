N = int(input())
member = []
for i in range(N):
    member.append(list(input().split()))
    member[i][0] = int(member[i][0])
    member[i].insert(0, i)
    member.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(member[i][1], member[i][2])