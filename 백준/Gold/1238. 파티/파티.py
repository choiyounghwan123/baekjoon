# 1238. 파티
import sys
import math
import heapq

input = sys.stdin.readline
N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s,d,c = map(int,input().split())
    graph[s].append([c,d])

costs = [math.inf] * (N+1)
costs[X] = 0

heap = []
heapq.heappush(heap,[0,X])
while heap:
    dist,vertex = heapq.heappop(heap)

    if costs[vertex] < dist:
        continue

    for i in graph[vertex]:
        if dist + i[0] < costs[i[1]]:
            costs[i[1]] = dist + i[0]
            heapq.heappush(heap,[dist+i[0],i[1]])

result = costs[1:]
for i in range(N):
    costs = [math.inf] * (N+1)
    costs[i+1] = 0
    heap = []
    heapq.heappush(heap,[0,i+1])

    while heap:
        distance, vertex = heapq.heappop(heap)

        if costs[vertex] < distance:
            continue

        for j in graph[vertex]:
            if distance + j[0] < costs[j[1]]:
                costs[j[1]] = distance + j[0]
                heapq.heappush(heap, [distance+j[0],j[1]])
    result[i] += costs[X]
print(max(result))

