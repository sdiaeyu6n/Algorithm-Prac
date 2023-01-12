N,M=map(int,input().split())
graph=[[] for i in range(N)]
for i in range(N):
    graph[i]=list(map(int,input()))

def dfs(x,y,graph):
    # 범위를 벗어나는 경우
    if x<0 or x>=N or y<0 or y>=M: 
        return
    # 칸막이가 존재하는 부분인 경우
    if graph[x][y]==1:
        return
    # 방문처리
    graph[x][y]=1 
    # 재귀 호출
    dfs(x-1,y,graph) #상
    dfs(x+1,y,graph) #하
    dfs(x,y-1,graph) #좌
    dfs(x,y+1,graph) #우

count=0
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            dfs(i,j,graph)
            count+=1

print(count)