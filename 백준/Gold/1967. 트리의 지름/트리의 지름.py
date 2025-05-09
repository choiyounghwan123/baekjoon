# 1967. 트리의 지름

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
trees = [[] for _ in range(n+1)]

for i in range(n-1):
    u,v,w = map(int,input().split())
    trees[u].append([v,w])
    trees[v].append([u,w])
visited = [-1] * (n+1)
visited[1] = 0

def dfs(start):
    for a,b in trees[start]:
        if visited[a] == -1:
            visited[a] = b + visited[start]
            dfs(a)
dfs(1)

start = visited.index(max(visited))
visited = [-1] * (n+1)
visited[start] = 0
dfs(start)
print(max(visited))