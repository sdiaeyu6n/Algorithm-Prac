import sys, math

M,N=map(int,sys.stdin.readline().split())
num_list=[False,False]+[True]*(N-1)
primes=[]

for i in range(2,N+1):
    if num_list[i]:
        primes.append(i)
        for j in range(2*i,N+1,i):
            num_list[j]=False

for i in primes:
    if i>=M:
        print(i)