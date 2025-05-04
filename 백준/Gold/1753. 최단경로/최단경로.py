# 1753. 최단경로
import math
import sys
import heapq
input = sys.stdin.readline

N,K = map(int,input().split())
start = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(K):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

costs = [math.inf] * (N+1)
heap = []
heapq.heappush(heap,[0,start])
costs[start] = 0

while heap:
    cost,vertex = heapq.heappop(heap)

    if cost > costs[vertex]:
        continue

    for i in graph[vertex]:
        if cost + i[0] < costs[i[1]]:
            heapq.heappush(heap,[i[0] + cost,i[1]])
            costs[i[1]] = cost + i[0]

for i in range(1,len(costs)):
    if costs[i] == math.inf:
        print("INF")
    else:
        print(costs[i])
