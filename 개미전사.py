N=int(input())
food=list(map(int, input().split()))
food.insert(0,0)

d=[0]*(N+1)

#초기값
d[1]=food[1]
d[2]=max(food[1],food[2])

for i in range(3,N+1):
    d[i]=max(d[i-1],d[i-2]+food[i])
print(d[N])