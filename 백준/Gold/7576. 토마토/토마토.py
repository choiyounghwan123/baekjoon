# 토마토

import sys
from collections import deque

M,N = map(int,sys.stdin.readline().split())
graph = []
queue = deque()
for i in range(N):
    graph.append([])
    x = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        if x[j] == 1:
            queue.append([i,j])
        graph[i].append(x[j])

dx,dy = [1,-1,0,0], [0,0,-1,1]
res = 0
visited = [[0] * M for _ in range(N)]
while queue:
    length = len(queue)
    res+=1
    for _ in range(length):
        y,x = queue.popleft()

        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]

            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                queue.append([ny,nx])


for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print("-1")
            exit()

print(res-1)




