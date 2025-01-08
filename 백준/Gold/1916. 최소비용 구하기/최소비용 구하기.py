# 1916. 최소비용 구하기
from collections import defaultdict
import sys
import heapq

N = int(input())
M = int(input())

graph = defaultdict(list)
costs = [sys.maxsize] * (N+1)

for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append([v,w])

departure, destination = map(int,input().split())

heap = []
heapq.heappush(heap, (0,departure))

while heap:
    cost, node = heapq.heappop(heap)

    if costs[node] < cost:
        continue

    for node_,cost_ in graph[node]:
        if cost + cost_ < costs[node_]:
            costs[node_] = cost + cost_
            heapq.heappush(heap,(costs[node_], node_))

print(costs[destination])



