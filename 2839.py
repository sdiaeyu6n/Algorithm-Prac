N=int(input())

d=[-1]*5001

#초기값
d[3]=1
d[5]=1

for i in range(6,N+1):
    if i%5==0:
        d[i]=i//5
    else:
        for k in range(i+1):
            if d[i-k]!=-1 and d[k]!=-1:
                d[i]=d[i-k]+d[k]
print(d[N])