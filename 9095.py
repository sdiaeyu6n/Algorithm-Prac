T=int(input()) #테스트 케이스의 개수
for i in range(T):
    n=int(input())
    d=[0]*11

    d[1]=1
    d[2]=2
    d[3]=4

    for i in range(4,n+1):
        d[i]=d[i-3]+d[i-2]+d[i-1]
    
    print(d[n])