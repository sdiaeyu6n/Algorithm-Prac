import sys
from collections import deque

N=int(sys.stdin.readline())
deq=deque()
for i in range(N):
    todo=sys.stdin.readline()
    if todo[:10]=='push_front':
        deq.appendleft(int(todo.split()[1]))
    elif todo[:9]=='push_back':
        deq.append(int(todo.split()[1]))
    elif todo.rstrip('\n')=='size':
        print(len(deq))
    elif todo.rstrip('\n')=='empty':
        if len(deq)==0:
            print(1)
        else: print(0)
    elif todo.rstrip('\n')=='pop_front':
        if not deq: # deque이 비어있을 때
            print(-1)
        else: print(deq.popleft())
    elif todo.rstrip('\n')=='pop_back':
        if not deq: # stack이 비어있을 때
            print(-1)
        else: print(deq.pop())
    elif todo.rstrip('\n')=='front':
        if not deq:
            print(-1)
        else: print(deq[0])
    elif todo.rstrip('\n')=='back':
        if not deq:
            print(-1)
        else: print(deq[-1])