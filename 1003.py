T=int(input())
for i in range(T):

    N=int(input())
    dp_zero=[0]*(N+2)
    dp_one=[0]*(N+2)

    #초기값
    dp_zero[0]=1
    dp_zero[1]=0
    dp_one[0]=0
    dp_one[1]=1
    if N==0:
        print(dp_zero[N], dp_one[N])
        continue
    if N==1:
        print(dp_zero[N], dp_one[N])
        continue

    for i in range(2,N+1):
        dp_zero[i]=dp_zero[i-2]+dp_zero[i-1]
        dp_one[i]=dp_one[i-2]+dp_one[i-1]
    
    print(dp_zero[N], dp_one[N])