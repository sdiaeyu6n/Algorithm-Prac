import sys
from collections import deque

N=int(sys.stdin.readline())
queue=deque()
for i in range(N):
    todo=sys.stdin.readline()
    if todo[:4]=='push':
        queue.append(int(todo.split()[1]))
    elif todo.rstrip('\n')=='size':
        print(len(queue))
    elif todo.rstrip('\n')=='empty':
        if len(queue)==0:
            print(1)
        else: print(0)
    elif todo.rstrip('\n')=='pop':
        if not queue: # stack이 비어있을 때
            print(-1)
        else: print(queue.popleft())
    elif todo.rstrip('\n')=='front':
        if not queue:
            print(-1)
        else: print(queue[0])
    elif todo.rstrip('\n')=='back':
        if not queue:
            print(-1)
        else: print(queue[-1])