# 1167. 트리의 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)
V = int(input())

trees = [[] for _ in range(V+1)]

for _ in range(V):
    a = list(map(int,input().split()))
    for i in range(1,len(a)-1,2):
        trees[a[0]].append([a[i],a[i+1]])
        trees[a[i]].append([a[0],a[i+1]])
visited = [-1] * (V+1)
def dfs(start):
    for a,b in trees[start]:
        if visited[a] == -1:
            visited[a] = b + visited[start]
            dfs(a)
visited[1] = 0
dfs(1)
start = visited.index(max(visited))
visited = [-1] * (V+1)
visited[start] = 0
dfs(start)
print(max(visited))
