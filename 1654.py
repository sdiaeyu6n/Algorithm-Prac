import sys

K,N=map(int, sys.stdin.readline().split())
have=[0]*K
for i in range(K):
    have[i]=int(sys.stdin.readline())

temp_length=0
for i in range(1,max(have)):
    count=0
    for n in have:
        count+=n//i
    if count>=N:
        temp_length=max(temp_length,i)
print(temp_length)