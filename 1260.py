from collections import deque

def DFS(start,graph,visited):
    visited[start]=True
    print(start,end=" ")
    for i in graph[start]:
        if not visited[i]:
            DFS(i,graph,visited)

def BFS(V,graph,visited):
    queue=deque()
    queue.append(V)
    visited[V]=True
    while queue:
        vn=queue.popleft()
        print(vn, end=" ")
        for i in graph[vn]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

N,M,V=map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1) # 간선은 양방향이다.

# 조건(숫자가 작은 노드부터)
for i in range(N+1):
    graph[i].sort()

visited=[False]*(N+1)

DFS(V,graph,visited)
visited=[False]*(N+1)
print()
BFS(V,graph,visited)
