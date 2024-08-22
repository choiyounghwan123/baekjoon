# 쉬운 최단거리

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[0] * M for _ in range(N)]
start = 0

for i in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if x[j] == 2:
            start = [i, j]
        graph[i][j] = x[j]

visited = [[-1] * M for _ in range(N)]
visited[start[0]][start[1]] = 0
queue = deque([start])
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == -1 and graph[ny][nx] == 1:
            queue.append([ny, nx])
            visited[ny][nx] = visited[y][x] + 1

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            visited[i][j] = 0

for i in range(N):
    for j in range(M):
        print(visited[i][j],end=" ")
    print()
