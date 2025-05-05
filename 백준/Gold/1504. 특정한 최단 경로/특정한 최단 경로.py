# 1504. 특정한 최단 경로
import sys
import heapq
input = sys.stdin.readline

N,E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])
    graph[v].append([w,u])

def dijkstra(start):
    heap = []
    costs = [sys.maxsize] * (N+1)
    heapq.heappush(heap, [0, start])
    costs[start] = 0

    while heap:
        cost,vertex = heapq.heappop(heap)
        if cost < costs[vertex]:
            continue

        for i in graph[vertex]:
            if cost + i[0] < costs[i[1]]:
                costs[i[1]] = cost + i[0]
                heapq.heappush(heap, [cost + i[0],i[1]])
    return costs
v1,v2 = map(int,input().split())

a = dijkstra(1)
b = dijkstra(v1)
c = dijkstra(v2)
print(min(a[v1] + b[v2] + c[N], a[v2] + c[v1] + b[N]) if min(a[v1] + b[v2] + c[N], a[v2] + c[v1] + b[N]) < sys.maxsize else -1)