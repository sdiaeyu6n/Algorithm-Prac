import sys
sys.setrecursionlimit(10**6)
def dfs(start,graph,visited):
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            dfs(i,graph,visited)

N,M=map(int, sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]

for i in range(M):
    n1,n2=map(int,sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited=[False]*(N+1)

num=0    
for j in range(1,N+1):
    if not visited[j]:
        dfs(j,graph,visited)
        num+=1
print(num)