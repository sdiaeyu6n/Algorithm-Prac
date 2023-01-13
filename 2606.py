from collections import deque

num_of_pc=int(input())
num_of_con=int(input())
connection=[[] for i in range(num_of_con)]
graph=[[] for i in range(num_of_pc+1)]
for i in range(num_of_con):
    n1,n2=map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1) # 양방향 그래프

visited=[False]*(num_of_pc+1)

def bfs(start,visited,graph):
    global count
    count=0
    queue=deque()
    queue.append(start)
    visited[start]=True
    while queue:
        v=queue.popleft()
        for n in graph[v]:
            if not visited[n]:
                queue.append(n)
                visited[n]=True
                count+=1
    return count

print(bfs(1,visited,graph))