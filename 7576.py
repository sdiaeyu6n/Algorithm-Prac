from collections import deque

M,N=map(int, input().split(" "))
graph=[[] for i in range(N)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(N):
    graph[i]=list(map(int,input().split(" ")))

def bfs(tomatoes,graph):
    day = 0
    queue=deque()
    for t in tomatoes:
        x,y=t
        queue.append((x,y,day))
        #방문처리 - 익었다
        graph[x][y]=1
    # queue에 담는 행위: 방문해야하는 노드를 넣는 행위
    while queue:
        x,y,day=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            # 방문할 노드를 결정하는 조건: 범위 안에 있는지 & 안 익은 토마토만!
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]==0:
                queue.append((nx,ny,day+1))
                graph[nx][ny]=1
    return day

all=True
for x in range(N):
    for y in range(M):
        if graph[x][y]==0:
            all=False
if all==True:
    answer=0

tomatoes=[]
if not all:
    for x in range(N):
        for y in range(M):
            if graph[x][y]==1:
                tomatoes.append((x,y))

    answer=bfs(tomatoes,graph)
    for x in range(N):
        for y in range(M):
            if graph[x][y]==0:
                answer=-1

print(answer)