pc=int(input())
pair=int(input())
graph=[[] for i in range(pc+1)]

for i in range(pair):
    n1,n2=map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited=[False]*(pc+1)
global count
count=0

def dfs(start,visited,graph):
    global count
    visited[start]=True
    for i in graph[start]:
        if not visited[i]:
            count+=1
            dfs(i,visited,graph)
    return count

print(dfs(1,visited,graph))
