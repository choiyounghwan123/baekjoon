# 유기농 배추

import sys
from collections import deque


def bfs(i, j, visited, graph, M, N):
    queue = deque([[i, j]])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited[i][j] = 1
    while queue:
        y, x = queue.popleft()

        for o in range(4):
            nx, ny = x + dx[o], y + dy[o]
            if (0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1 and
                    visited[ny][nx] == 0):
                visited[ny][nx] = 1
                queue.append([ny, nx])


for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())

        graph[y][x] = 1
    visited = [[0] * M for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, visited, graph, M, N)
                res += 1

    print(res)
