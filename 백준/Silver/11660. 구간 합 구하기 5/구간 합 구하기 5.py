# 구간 합 구하기 5

import sys

N,M = map(int,sys.stdin.readline().split())
board = [[0] * (N+1)]

for _ in range(N):
    board.append([0] + list(map(int,sys.stdin.readline().split())))

D = [[0] * (N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] + board[i][j] - D[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(D[x2][y2] - D[x1-1][y2] - D[x2][y1-1]+D[x1-1][y1-1])


