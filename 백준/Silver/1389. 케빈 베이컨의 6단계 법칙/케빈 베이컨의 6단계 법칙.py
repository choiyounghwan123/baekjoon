# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = [[] * N for _ in range(N + 1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
def bfs(n):
    visited = [0] * (N + 1)
    queue = deque([n])
    visited[n] = 0
    while queue:
      vertex = queue.popleft()

      for i in graph[vertex]:
          if visited[i] == 0:
              visited[i] = visited[vertex] + 1
              queue.append(i)
    visited[n] = 0
    return sum(visited)
res = []
for i in range(1,N+1):
    heapq.heappush(res,(bfs(i),i))

print(heapq.heappop(res)[1])