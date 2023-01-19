import sys

M,N=map(int,sys.stdin.readline().split())
num_list=[0]*(N-M+1)
for i in range(M,N):
    for j in range(2,i):
        if i%j==0:
            num_list[i-M]+=1

for i in range(M,N):
    if num_list[i-M]==0:
        print(i)