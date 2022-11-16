N=int(input())
coordinate=[]
for i in range(N):
    coordinate.append(list(map(int,input().split())))

for cdn in sorted(coordinate, key=lambda x:(x[0],x[1])):
    print(cdn[0],cdn[1])