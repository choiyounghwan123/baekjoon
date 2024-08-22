# 바이러스

import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque(graph[1])
visited = [0] * (N+1)
visited[1] = 1

while queue:
    node = queue.popleft()
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 0:
            queue.append(nxt)

print(visited.count(1) - 1)


