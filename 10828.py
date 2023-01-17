import sys

N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    todo=sys.stdin.readline()
    if todo[:4]=='push':
        stack.append(int(todo.split()[1]))
    elif todo.rstrip('\n')=='top':
        if not stack:
            print(-1)
        else: print(stack[-1])
    elif todo.rstrip('\n')=='size':
        print(len(stack))
    elif todo.rstrip('\n')=='empty':
        if len(stack)==0:
            print(1)
        else: print(0)
    elif todo.rstrip('\n')=='pop':
        if not stack: # stack이 비어있을 때
            print(-1)
        else: print(stack.pop())