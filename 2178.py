from collections import deque

N,M=map(int,input().split())
graph=[[] for i in range(N)]
for i in range(N):
    graph[i]=list((map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y,graph):
    count=1
    queue=deque()
    queue.append((x,y,count))

    while queue:
        x,y,count=queue.popleft()
        if x==N-1 and y==M-1:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==1:
                queue.append((nx,ny,count+1))
                graph[nx][ny]=0
    return count

print(bfs(0,0,graph))