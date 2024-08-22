# 헌내기는 친구가 필요해

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
campus = []

start = 0

for i in range(N):
    campus.append([])
    row = list(sys.stdin.readline().rstrip())
    for j in range(M):
        if row[j] == "I":
            start = [i, j]
        campus[i].append(row[j])

visited = [[0] * M for _ in range(N)]
visited[start[0]][start[1]] = 1
queue = deque([start])
res = 0
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

while queue:
    y, x = queue.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] == 0 and campus[ny][nx] != "X":
            visited[ny][nx] = 1
            if campus[ny][nx] == "P":
                res += 1
            queue.append([ny, nx])


if res:
    print(res)
else:
    print("TT")