from collections import deque
import sys

def bfs(x,y,graph):
        global count
        queue=deque() 
        queue.append((x,y))
        graph[x][y]=0
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                    queue.append((nx,ny))
                    graph[nx][ny]=0
        count+=1

tc=int(sys.stdin.readline())
for _ in range(tc):
    m,n,k=map(int, sys.stdin.readline().split())
    graph=[[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        y,x=map(int, sys.stdin.readline().split())
        graph[x][y]=1

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    count=0

    for x in range(n):
        for y in range(m):
            if graph[x][y]==1:
                bfs(x,y,graph)

    print(count)