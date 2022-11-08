T=int(input())
for i in range(T):
    R,S=map(str,input().split())
    S=list(S)
    P=""
    for j in S:
        for k in range(int(R)):
            P+=j
    print(P)
    
