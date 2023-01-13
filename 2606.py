from collections import deque

num_of_pc=int(input())
num_of_con=int(input())
connection=[[] for i in range(num_of_con)]
for i in range(num_of_con):
    connection[i]=list(map(int,input().split()))

graph=[[] for i in range(num_of_pc+1)]
for con in connection:
    for i in range(1,num_of_pc+1):
        if i in con:
            graph[i]+=con
            graph[i].remove(i)

new_graph=[]
for i in graph:
    new_graph.append(list(set(i)))

graph=new_graph[:]
# print(graph)

visited=[False]*num_of_pc

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

            