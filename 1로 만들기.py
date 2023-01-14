x=int(input())

d=[0]*30001
d[1]=0

for i in range(2,x+1):
    temp=d[i-1]
    if i%2==0:
        temp=min(temp,d[i//2])
    if i%3==0:
        temp=min(temp, d[i//3])
    if i%5==0:
        temp=min(temp,d[i//5])
    d[i]=temp+1

print(d[x])