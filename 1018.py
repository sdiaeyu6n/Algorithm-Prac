import sys

N,M=map(int,sys.stdin.readline().split())
board=[['0']*M for i in range(N)]
for i in range(N):
    board[i]=list(sys.stdin.readline().rstrip())
board_list = []
for i in range(N-8+1):
    for j in range(M-8+1):
        new_board=[['0']*M for i in range(N)]
        for a in range(8):
            for b in range(8):
                new_board[a][b]=board[i+a][j+b]
        board_list.append(new_board)

graph1=['BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB']

graph2=['WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW',
'WBWBWBWB',
'BWBWBWBW']

temp=9999
for b in board_list:
    count1=0
    count2=0
    for i in range(8):
        for j in range(8):
            if b[i][j]!=graph1[i][j]:
                count1+=1  
            if b[i][j]!=graph2[i][j]:
                count2+=1
    temp=min(temp,count1,count2)

print(temp)