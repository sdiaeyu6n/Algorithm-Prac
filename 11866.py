from collections import deque

N, K = map(int, input().split())

people = deque([i for i in range(1, N + 1)])

people.rotate(-(K-1))

yose=[]
for i in range(N):
    if len(people) < K:
        for j in people:
            yose.append(str(j))
        break
    else:
        yose.append(str(people.popleft()))
        people.rotate(-(K-1))

print("<"+", ".join(yose)+">")