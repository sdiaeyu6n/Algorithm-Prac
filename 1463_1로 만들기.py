N=int(input())

d=[0]*(N+1)

#초기값
d[1]=0

#점화식
for i in range(2,N+1):
    temp=d[i-1]
    if i%3==0:
        temp=min(temp,d[i//3])
    if i%2==0:
        temp=min(temp,d[i//2])
    d[i]=temp+1

print(d[N])