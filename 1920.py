# 시간복잡도 = O((M+N)logN)
import sys

N=int(sys.stdin.readline())
# Tim Sort -> O(NlogN)
N_list=sorted(list(map(int,sys.stdin.readline().split())))
M=int(sys.stdin.readline())
M_list=list(map(int,sys.stdin.readline().split()))

# 이분탐색 M번 수행 -> O(MlogN)
def binary_search(target,array,start,end):
    if start>end:
        print(0)
        return 0
    mid = (start+end)//2
    if array[mid]==target:
        print(1)
        return 1
    elif array[mid]<target:
        return binary_search(target,array,mid+1,end)
    else:
        return binary_search(target,array,start,mid-1)

for m in M_list:
    binary_search(m,N_list,0,N-1) #범위 유의(end=N-1)