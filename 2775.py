T = int(input())
for i in range(T):
    k = int(input())  # 층
    n = int(input())  # 호
    apt = [[0 for k in range(0,n)] for j in range(0,k+1)]
    for l in range(0,k+1):
        for m in range(0, n):
            if m == 0: #1호인 경우
                apt[l][m] = 1
            elif l == 0: #0층인 경우
                apt[l][m] = m+1
            else:
                apt[l][m]=apt[l][m-1]+apt[l-1][m]
    print(apt[k][n-1])