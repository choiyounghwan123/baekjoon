# 미로탐색

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().rstrip()))for _ in range(N)]

queue = deque([[0, 0]])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[ny][nx] == 1:
            queue.append([nx, ny])
            board[ny][nx] = board[y][x] + 1

print(board[N-1][M-1])
