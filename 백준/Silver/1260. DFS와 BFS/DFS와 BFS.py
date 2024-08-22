# DFS와 BFS

import sys
from collections import deque

N,M,V = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited = [0] * (N+1)
def dfs(n):
    print(n,end=" ")
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            dfs(i)

def bfs(n):
    queue = deque([n])
    visited[n] = 1
    while queue:
        vertex = queue.popleft()
        print(vertex,end=" ")
        for i in graph[vertex]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)



dfs(V)
visited = [0] * (N+1)
print("")
bfs(V)