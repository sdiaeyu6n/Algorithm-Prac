import sys, copy
from collections import deque

tc=int(sys.stdin.readline())
for i in range(tc):
    N,order=map(int,sys.stdin.readline().split())
    num=list(map(int,sys.stdin.readline().split()))
    priority=[[] for _ in range(N)]
    for i in range(N):
        priority[i]=[i,num[i]]
    answer=[]
    priority=deque(priority)
    while copy.deepcopy(priority):
        for j in copy.deepcopy(priority):
            if j[1]!=max(num):
                priority.rotate(-1)
            else: 
                answer.append(priority.popleft())
                num.remove(j[1])
    for k in range(N):
        if answer[k][0]==order:
            print(k+1)