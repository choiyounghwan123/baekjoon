# 경로 찾기

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]

for i in range(N):
    queue = deque([i])

    while queue:
        n = queue.popleft()

        for j in range(N):
            if graph[n][j] == 1 and visited[i][j] == 0:
                visited[i][j] =1
                queue.append(j)

for i in range(N):
    for j in range(N):
        print(visited[i][j],end=" ")
    print("")