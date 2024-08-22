# 체스판 다시 칠하기

import sys

N,M = map(int,sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

result = sys.maxsize

for i in range(N-7):
    for j in range(M-7):
        black = 0
        white = 0
        for k in range(i,8+i):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != "W":
                        white+=1
                    else:
                        black+=1
                else:
                    if board[k][l] != "B":
                        white += 1
                    else:
                        black += 1
        result = min(result,white,black)

print(result)