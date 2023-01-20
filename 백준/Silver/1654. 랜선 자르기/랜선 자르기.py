import sys

def binary_search(have,min,max):
    if min>max: #이분탐색 종료조건 설정
        return max
    mid=(min+max)//2
    count=0
    for n in have:
        count+=n//mid
    if count>=N:
        return binary_search(have,mid+1,max)
    else: #count<11
        return binary_search(have,min,mid-1)

K,N=map(int, sys.stdin.readline().split())
have=[0]*K
for i in range(K):
    have[i]=int(sys.stdin.readline())

print(binary_search(have,1,max(have)))