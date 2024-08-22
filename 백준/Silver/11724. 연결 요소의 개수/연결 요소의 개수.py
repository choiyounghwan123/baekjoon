# 연결 요소의 개수

import sys
sys.setrecursionlimit(10000)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (N + 1)


def dfs(vertex):
    visited[vertex] = 1
    for i in graph[vertex]:
        if visited[i] == 0:
            dfs(i)


res = 0

for i in range(1,N+1):
    if visited[i] == 0:
        dfs(i)
        res+=1
    

print(res)
