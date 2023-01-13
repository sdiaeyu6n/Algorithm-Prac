from collections import deque

N=int(input())
graph=[[] for i in range(N)]

for i in range(N):
    graph[i]=list(map(int, input()))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

house_list=[]

def bfs(x,y,graph):
    global count
    count=1
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==1:
                queue.append((nx,ny))
                count+=1
                graph[nx][ny]=0
    house_list.append(count)    
    
for x in range(N):
    for y in range(N):
        if graph[x][y]==1:
            bfs(x,y,graph)
print(len(house_list))
for house in sorted(house_list):
    print(house)