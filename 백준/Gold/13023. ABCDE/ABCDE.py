# 13023. ABCDE

N,M = map(int,input().split())

graph = [[] for _ in range(N)]
result = 0
for i in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(vertex,count,visited):
    if count == 5:
        global result
        result = 1
        return
    visited[vertex] = 1

    for i in graph[vertex]:
        if visited[i] == 0:
            dfs(i,count+1,visited)
    visited[vertex] = 0

for i in range(N):
    dfs(i,1,[0] * N)
print(result)