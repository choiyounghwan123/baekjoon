# 11725. 트리의 부모 찾기
import sys

sys.setrecursionlimit(10 ** 6)
N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

result = [0] * (N + 1)
visited = [False] * (N + 1)


def dfs(index):
    if visited[index]:
        return
    visited[index] = True
    for i in graph[index]:
        if not visited[i]:
            result[i] = index
            dfs(i)


dfs(1)

for i in range(2, N + 1):
    print(result[i])
