import sys

N=int(sys.stdin.readline())
num=[0]*10001
for i in range(N):
    number=int(sys.stdin.readline())
    num[number]+=1

for i in range(10001):
    if num[i]!=0:
        for _ in range(num[i]):
            print(i)