import sys

N=int(sys.stdin.readline())
have=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
find=list(map(int,sys.stdin.readline().split()))

num=[0]*20000001

for i in have:
    num[i+10000000]+=1
for i in find:
    print(num[i+10000000],end=" ")