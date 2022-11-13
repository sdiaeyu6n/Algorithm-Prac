N,K=map(int,input().split())
N_fact=1
K_fact=1
N_K_fact=1
for i in range(1,N+1):
    N_fact=N_fact*i
for i in range(1,K+1):
    K_fact=K_fact*i
for i in range(1,N-K+1):
    N_K_fact=N_K_fact*i

print(int(N_fact/K_fact/N_K_fact))