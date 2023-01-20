import sys

def binary_search(have,start,end):
    if start>end:
        return end
    mid=(start+end)//2
    count=0
    for n in have:
        count+=n//mid
    if count>=N:
        return binary_search(have,mid+1,end)
    else: #count<11
        return binary_search(have,start,mid-1)

K,N=map(int, sys.stdin.readline().split())
have=[0]*K
for i in range(K):
    have[i]=int(sys.stdin.readline())

print(binary_search(have,1,max(have)))
