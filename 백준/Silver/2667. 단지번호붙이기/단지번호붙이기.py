# 단지번호붙이기

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]


def bfs(x, y):
    queue = deque([[x, y]])
    visited[y][x] = 1
    res = 1

    while queue:
        x_, y_ = queue.popleft()
        for i in range(4):
            nx, ny = x_ + dx[i], y_ + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == "1" and visited[ny][nx] == 0:
                queue.append([nx,ny])
                visited[ny][nx] = 1
                res+=1
    return res

res = []
total = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == "1" and visited[i][j] == 0:
            total += 1
            res.append(bfs(j, i))
print(total)
for i in sorted(res):
    print(i)
