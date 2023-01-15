import sys
N,M=map(int,sys.stdin.readline().split())
board=[['0']*M for i in range(N)]
new_board=[['0']*8 for i in range(8)]
for i in range(N):
    board[i]=list(sys.stdin.readline().strip("\n"))


board_list=[]

for i in range(N-8+1):
    for j in range(M-8+1):
        for a in range(8):
            for b in range(8):
                new_board[a][b]=board[i+a][j+b]
        board_list.append(new_board)


for b in board_list:
