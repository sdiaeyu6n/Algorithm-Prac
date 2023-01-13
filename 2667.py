N=int(input())
graph=[[] for i in range(N)]
for i in range(N):
    graph[i]=list(map(int,input()))

house=[]
count = 0 

def dfs(x,y,graph):
    global count
    #주어진 범위 확인
    if x<0 or y<0 or x>=N or y>=N:
        return 0
    #집이 없으면 return
    if graph[x][y]==0:
        return 0
    
    #방문처리
    graph[x][y]=0
    #집의 개수 +1
    count+=1

    dfs(x-1,y,graph)
    dfs(x+1,y,graph)
    dfs(x,y-1,graph)
    dfs(x,y+1,graph)

    # return count

for i in range(N):
    for j in range(N):
        count=0
        if graph[i][j]==1:
            dfs(i,j,graph)
            house.append(count)

print(len(house))
for i in sorted(house):
    print(i)