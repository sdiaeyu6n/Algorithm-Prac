N=int(input())
N_list=list(map(int,input().split()))
M=int(input())
M_list=list(map(int,input().split()))

for m in M_list:
    if m in N_list:
        print(1)
    else: print(0)