import sys

M,N=map(int,sys.stdin.readline().split())
num_list=[0]*(N-M+1)

for i in range(M,N+1):
    if i==1:
        num_list[i-M]+=1
    elif i==2 or i==3 or i==5 or i==7:
        continue
    else:
        if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            num_list[i-M]+=1  
         
for i in range(M,N+1):
    if num_list[i-M]==0:
        print(i)