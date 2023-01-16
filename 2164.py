import sys
from collections import deque

N=int(sys.stdin.readline())
card=deque()
for i in range(0,N):
    card.append(i+1)

for _ in range(N-1):
    card.popleft()
    temp=card.popleft()
    card.append(temp)
print(*card)