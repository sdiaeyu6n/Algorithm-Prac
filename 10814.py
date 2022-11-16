N = int(input())
member = []
for i in range(N):
    member.append(list(input().split()))
    member[i][0] = int(member[i][0])
    member[i].insert(0, i)
for mem in sorted(member,key=lambda x: (x[1], x[0])):
    print(mem[1],mem[2])